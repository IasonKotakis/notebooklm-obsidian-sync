"""Transform NotebookLM artifacts into Obsidian notes and Canvas files."""

import json
import math
import re
from pathlib import Path


# Canvas layout constants
CHILD_RADIUS = 400
GRANDCHILD_RADIUS = 800
NODE_WIDTH = 200
NODE_HEIGHT = 60


def convert_mindmap(input_path: Path, output_path: Path) -> None:
    """Convert NotebookLM mind map JSON to Obsidian Canvas format.

    Handles both 'children' (hierarchical tree) and 'nodes'/'edges'
    (graph) formats produced by notebooklm-py.
    """
    data = json.loads(input_path.read_text(encoding="utf-8"))

    if "nodes" in data and "edges" in data:
        canvas = _convert_graph_format(data)
    else:
        canvas = _convert_tree_format(data)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(canvas, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def _make_node(node_id: str, text: str, x: int, y: int) -> dict:
    return {
        "id": node_id,
        "type": "text",
        "text": text,
        "x": x - NODE_WIDTH // 2,
        "y": y - NODE_HEIGHT // 2,
        "width": NODE_WIDTH,
        "height": NODE_HEIGHT,
    }


def _make_edge(edge_id: str, from_node: str, to_node: str) -> dict:
    return {"id": edge_id, "fromNode": from_node, "toNode": to_node}


def _convert_tree_format(data: dict) -> dict:
    """Convert hierarchical children-based mind map to Canvas."""
    nodes = []
    edges = []
    counter = [0]

    def _recurse(
        node_data: dict,
        parent_id: str | None,
        x: int,
        y: int,
        radius: int,
        angle_start: float,
        angle_end: float,
    ) -> None:
        label = node_data.get("name", node_data.get("label", ""))
        node_id = f"node_{counter[0]}"
        counter[0] += 1
        nodes.append(_make_node(node_id, label, x, y))

        if parent_id is not None:
            edges.append(_make_edge(f"edge_{len(edges)}", parent_id, node_id))

        children = node_data.get("children", [])
        if not children:
            return

        n = len(children)
        for i, child in enumerate(children):
            if n == 1:
                angle = (angle_start + angle_end) / 2
            else:
                angle = angle_start + (angle_end - angle_start) * i / (n - 1)
            cx = int(x + radius * math.cos(angle))
            cy = int(y + radius * math.sin(angle))
            span = (angle_end - angle_start) / max(n, 1)
            next_radius = radius + (GRANDCHILD_RADIUS - CHILD_RADIUS)
            _recurse(child, node_id, cx, cy, next_radius, angle - span / 2, angle + span / 2)

    _recurse(data, None, 0, 0, CHILD_RADIUS, 0, 2 * math.pi)
    return {"nodes": nodes, "edges": edges}


def _convert_graph_format(data: dict) -> dict:
    """Convert nodes/edges graph format to Canvas format."""
    nodes = []
    edges = []

    raw_nodes = data.get("nodes", [])
    n = len(raw_nodes)
    for i, raw in enumerate(raw_nodes):
        node_id = str(raw.get("id", i))
        label = raw.get("label", raw.get("text", raw.get("name", "")))
        if i == 0:
            x, y = 0, 0
        else:
            angle = 2 * math.pi * i / max(n - 1, 1)
            x = int(CHILD_RADIUS * math.cos(angle))
            y = int(CHILD_RADIUS * math.sin(angle))
        nodes.append(_make_node(node_id, label, x, y))

    for i, raw in enumerate(data.get("edges", [])):
        from_id = str(raw.get("source", raw.get("fromNode", "")))
        to_id = str(raw.get("target", raw.get("toNode", "")))
        edges.append(_make_edge(f"edge_{i}", from_id, to_id))

    return {"nodes": nodes, "edges": edges}


SYSTEM_PROMPT = """You are an Obsidian note writer. Given a NotebookLM study guide report and an audio overview transcript, produce a single structured Obsidian markdown note.

RULES:
- Output ONLY the markdown note — no preamble, no explanation
- Use [[wikilinks]] for key concepts, proper nouns, frameworks, people, and topics that deserve their own Obsidian node. Be selective: 5-15 wikilinks per note is ideal.
- Write in clear, concise prose suitable for a personal knowledge base
- The YAML frontmatter must come first

OUTPUT FORMAT:
---
title: "NOTEBOOK_TITLE"
tags: [seedling, notebooklm]
source: notebooklm
date: DATE
status: seedling
---

## Core Idea
One paragraph capturing the central thesis or insight of this notebook.

## Key Concepts
3-7 bullet points, each explaining a key concept. Use [[wikilinks]] for concepts worth linking.

## Connections
A sentence or two identifying how this topic connects to other ideas. Include [[wikilinks]] to related concepts.

## Questions This Raises
3-5 bullet points of open questions or areas worth exploring further."""


def generate_note(
    report_path: Path,
    transcript_path: Path | None,
    title: str,
    date: str,
    output_path: Path,
    video_vault_path: str | None = None,
) -> None:
    """Call Claude to transform report + transcript into a structured Obsidian note.

    Args:
        report_path: Path to the downloaded report markdown file.
        transcript_path: Path to the Whisper transcript markdown (may be None if transcription failed).
        title: Notebook title for YAML frontmatter.
        date: ISO date string (YYYY-MM-DD) for frontmatter.
        output_path: Where to write the generated .md file.
        video_vault_path: Vault-relative path to video file (e.g. '07 - Sources/...'), or None.
    """
    import anthropic
    import os

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY not set. Check your .env file.")

    report_text = report_path.read_text(encoding="utf-8")
    transcript_text = ""
    if transcript_path and transcript_path.exists():
        transcript_text = f"\n\n---\n\n{transcript_path.read_text(encoding='utf-8')}"

    video_instruction = ""
    if video_vault_path:
        video_instruction = (
            f"\n\nA video overview is available. Include this section at the end of the note "
            f"(after Questions This Raises):\n\n"
            f"## Resources\n\n"
            f"- Video Overview: [[{video_vault_path}]]\n"
        )

    user_content = (
        f"Notebook title: {title}\n"
        f"Date: {date}\n\n"
        f"=== STUDY GUIDE REPORT ===\n{report_text}"
        f"{transcript_text}"
        f"{video_instruction}"
    )

    try:
        from sync.state import load_config
        cfg = load_config()
        model = cfg.get("anthropic", {}).get("model", "claude-sonnet-4-20250514")
        max_tokens = cfg.get("anthropic", {}).get("max_tokens", 4096)
    except SystemExit:
        raise
    except Exception:
        model = "claude-sonnet-4-20250514"
        max_tokens = 4096

    client = anthropic.Anthropic(api_key=api_key)

    print(f"    [transform] Calling Claude...", end="", flush=True)

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=[
            {
                "type": "text",
                "text": SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": user_content}],
    )

    note_text = response.content[0].text
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(note_text, encoding="utf-8")
    print(" done")


def format_quiz_note(quiz_json_path: Path, output_path: Path, title: str, date: str) -> None:
    """Convert quiz JSON into an Obsidian note with hidden answers in callout blocks.

    Each question becomes a heading; the correct answer and hint are hidden
    inside an Obsidian 'answer' callout so they stay collapsed by default.
    """
    data = json.loads(quiz_json_path.read_text(encoding="utf-8"))
    questions = data.get("questions", [])
    quiz_title = data.get("title", title)

    lines = [
        "---",
        f'title: "{quiz_title} - Quiz"',
        "tags: [seedling, notebooklm, quiz]",
        "source: notebooklm",
        f"date: {date}",
        "status: seedling",
        "---",
        "",
        f"# {quiz_title} - Quiz",
        "",
    ]

    for i, q in enumerate(questions, 1):
        question_text = q.get("question", "")
        options = q.get("answerOptions", [])
        hint = q.get("hint", "")

        lines.append(f"## Question {i}")
        lines.append("")
        lines.append(question_text)
        lines.append("")

        # Show all options with letters (A, B, C, D)
        correct_letter = ""
        correct_text = ""
        for j, opt in enumerate(options):
            letter = chr(ord("A") + j)
            lines.append(f"- **{letter}.** {opt.get('text', '')}")
            if opt.get("isCorrect"):
                correct_letter = letter
                correct_text = opt.get("text", "")

        lines.append("")

        # Hide answer in collapsed callout
        answer_lines = [f"> [!answer]- Answer"]
        if correct_letter:
            answer_lines.append(f"> **{correct_letter}.** {correct_text}")
        if hint:
            answer_lines.append(f">")
            answer_lines.append(f"> **Hint:** {hint}")
        lines.extend(answer_lines)
        lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


SOURCE_NOTE_SYSTEM_PROMPT = """You are an Obsidian note writer creating atomic source notes for a personal knowledge base.

Given source content (web page, YouTube video, PDF, or document), produce a concise structured Obsidian note capturing the key ideas from that source.

RULES:
- Output ONLY the markdown note — no preamble, no explanation
- Use [[wikilinks]] for key concepts, proper nouns, frameworks, and topics (5-10 per note)
- Write concisely — this is an atomic note about a single source
- The YAML frontmatter must come first

OUTPUT FORMAT:
---
title: "SOURCE_TITLE"
url: SOURCE_URL
source_type: SOURCE_TYPE
tags: [seedling, source]
date: DATE
status: seedling
notebook: "[[NOTEBOOK_TITLE]]"
---

## Core Content
2-4 sentences capturing the main ideas from this source.

## Key Points
3-5 bullet points with the most important facts, arguments, or concepts. Use [[wikilinks]].

## Back to Notebook
Part of [[NOTEBOOK_TITLE]]."""


def generate_source_note(
    fulltext,
    notebook_title: str,
    date: str,
    output_path: Path,
) -> None:
    """Call Claude to generate an atomic Obsidian note for a single source.

    Args:
        fulltext: SourceFulltext object with content, title, url, kind.
        notebook_title: Parent notebook title for backlinking.
        date: ISO date string (YYYY-MM-DD).
        output_path: Where to write the source note .md file.
    """
    import anthropic
    import os

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY not set. Check your .env file.")

    # Truncate very long fulltexts to keep API costs manageable
    content = fulltext.content or ""
    if len(content) > 12000:
        content = content[:12000] + "\n\n[content truncated]"

    source_type = str(fulltext.kind) if fulltext.kind else "unknown"
    url = fulltext.url or ""

    user_content = (
        f"Source title: {fulltext.title}\n"
        f"Source URL: {url}\n"
        f"Source type: {source_type}\n"
        f"Notebook title: {notebook_title}\n"
        f"Date: {date}\n\n"
        f"=== SOURCE CONTENT ===\n{content}"
    )

    try:
        from sync.state import load_config
        cfg = load_config()
        model = cfg.get("anthropic", {}).get("model", "claude-sonnet-4-20250514")
    except SystemExit:
        raise
    except Exception:
        model = "claude-sonnet-4-20250514"

    client = anthropic.Anthropic(api_key=api_key)

    response = client.messages.create(
        model=model,
        max_tokens=1024,
        system=[
            {
                "type": "text",
                "text": SOURCE_NOTE_SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": user_content}],
    )

    note_text = response.content[0].text
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(note_text, encoding="utf-8")


def generate_sources_index(
    fulltexts: list,
    notebook_title: str,
    date: str,
    output_path: Path,
) -> None:
    """Write a sources index note listing all sources with URLs and links to their notes.

    This is a deterministic transformation — no Claude call needed.
    """
    lines = [
        "---",
        f'title: "Sources - {notebook_title}"',
        "tags: [seedling, sources, notebooklm]",
        "source: notebooklm",
        f"date: {date}",
        "status: seedling",
        f'notebook: "[[{notebook_title}]]"',
        "---",
        "",
        f"# Sources: [[{notebook_title}]]",
        "",
        f"| Title | Type | URL |",
        f"|-------|------|-----|",
    ]

    for ft in fulltexts:
        safe_title = _safe_source_filename(ft.title or "Untitled")
        source_type = str(ft.kind) if ft.kind else "unknown"
        url = ft.url or ""
        url_cell = f"[link]({url})" if url else ""
        lines.append(f"| [[{safe_title}]] | {source_type} | {url_cell} |")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _safe_source_filename(title: str) -> str:
    """Sanitize a source title for use as an Obsidian filename (no extension)."""
    sanitized = re.sub(r'[:/\\?*"<>|]', "-", title)
    sanitized = sanitized.replace("--", "-").rstrip("-")
    return sanitized.strip()[:80]  # cap at 80 chars
