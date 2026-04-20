import json
from dataclasses import dataclass
from unittest.mock import MagicMock

import pytest


SIMPLE_MINDMAP = {
    "name": "AI Basics",
    "children": [
        {"name": "Machine Learning"},
        {"name": "Neural Networks", "children": [
            {"name": "Backpropagation"},
        ]},
    ]
}

NODES_FORMAT_MINDMAP = {
    "nodes": [
        {"id": "1", "label": "Root"},
        {"id": "2", "label": "Child A"},
    ],
    "edges": [{"source": "1", "target": "2"}]
}


def test_convert_mindmap_produces_valid_canvas(tmp_path):
    from sync.transformer import convert_mindmap
    input_path = tmp_path / "mindmap.json"
    output_path = tmp_path / "output.canvas"
    input_path.write_text(json.dumps(SIMPLE_MINDMAP))

    convert_mindmap(input_path, output_path)

    canvas = json.loads(output_path.read_text())
    assert "nodes" in canvas
    assert "edges" in canvas


def test_convert_mindmap_root_at_origin(tmp_path):
    from sync.transformer import convert_mindmap
    input_path = tmp_path / "mindmap.json"
    output_path = tmp_path / "output.canvas"
    input_path.write_text(json.dumps(SIMPLE_MINDMAP))

    convert_mindmap(input_path, output_path)

    canvas = json.loads(output_path.read_text())
    root = next(n for n in canvas["nodes"] if n["text"] == "AI Basics")
    assert root["x"] == -100  # centered: 0 - NODE_WIDTH//2
    assert root["y"] == -30   # centered: 0 - NODE_HEIGHT//2


def test_convert_mindmap_children_count(tmp_path):
    from sync.transformer import convert_mindmap
    input_path = tmp_path / "mindmap.json"
    output_path = tmp_path / "output.canvas"
    input_path.write_text(json.dumps(SIMPLE_MINDMAP))

    convert_mindmap(input_path, output_path)

    canvas = json.loads(output_path.read_text())
    # Root + 2 children + 1 grandchild = 4 nodes
    assert len(canvas["nodes"]) == 4
    # 2 parent→child edges + 1 child→grandchild edge = 3 edges
    assert len(canvas["edges"]) == 3


def test_convert_mindmap_nodes_format(tmp_path):
    from sync.transformer import convert_mindmap
    input_path = tmp_path / "mindmap.json"
    output_path = tmp_path / "output.canvas"
    input_path.write_text(json.dumps(NODES_FORMAT_MINDMAP))

    convert_mindmap(input_path, output_path)

    canvas = json.loads(output_path.read_text())
    assert "nodes" in canvas
    assert len(canvas["nodes"]) == 2


# --- Quiz tests ---

SAMPLE_QUIZ_JSON = {
    "title": "DevOps Quiz",
    "questions": [
        {
            "question": "What does CI stand for?",
            "answerOptions": [
                {"text": "Continuous Integration", "isCorrect": True},
                {"text": "Continuous Inspection", "isCorrect": False},
                {"text": "Code Infrastructure", "isCorrect": False},
            ],
            "hint": "Think about merging code often.",
        },
        {
            "question": "Which tool is used for container orchestration?",
            "answerOptions": [
                {"text": "Docker", "isCorrect": False},
                {"text": "Kubernetes", "isCorrect": True},
            ],
        },
    ],
}


def test_format_quiz_note_produces_markdown(tmp_path):
    from sync.transformer import format_quiz_note
    quiz_path = tmp_path / "quiz.json"
    output_path = tmp_path / "quiz.md"
    quiz_path.write_text(json.dumps(SAMPLE_QUIZ_JSON))

    format_quiz_note(quiz_path, output_path, "DevOps", "2026-04-20")

    content = output_path.read_text()
    assert "## Question 1" in content
    assert "## Question 2" in content


def test_format_quiz_note_has_answer_callout(tmp_path):
    from sync.transformer import format_quiz_note
    quiz_path = tmp_path / "quiz.json"
    output_path = tmp_path / "quiz.md"
    quiz_path.write_text(json.dumps(SAMPLE_QUIZ_JSON))

    format_quiz_note(quiz_path, output_path, "DevOps", "2026-04-20")

    content = output_path.read_text()
    assert "[!answer]" in content
    assert "Continuous Integration" in content


def test_format_quiz_note_has_hint(tmp_path):
    from sync.transformer import format_quiz_note
    quiz_path = tmp_path / "quiz.json"
    output_path = tmp_path / "quiz.md"
    quiz_path.write_text(json.dumps(SAMPLE_QUIZ_JSON))

    format_quiz_note(quiz_path, output_path, "DevOps", "2026-04-20")

    content = output_path.read_text()
    assert "Think about merging code often." in content


def test_format_quiz_note_has_yaml_frontmatter(tmp_path):
    from sync.transformer import format_quiz_note
    quiz_path = tmp_path / "quiz.json"
    output_path = tmp_path / "quiz.md"
    quiz_path.write_text(json.dumps(SAMPLE_QUIZ_JSON))

    format_quiz_note(quiz_path, output_path, "DevOps", "2026-04-20")

    content = output_path.read_text()
    assert content.startswith("---")
    assert "status: seedling" in content
    assert "date: 2026-04-20" in content


# --- Sources index tests ---

def _make_fulltext(title, url, kind_str="web_page"):
    ft = MagicMock()
    ft.title = title
    ft.url = url
    ft.kind = kind_str
    return ft


def test_generate_sources_index_creates_table(tmp_path):
    from sync.transformer import generate_sources_index
    fulltexts = [
        _make_fulltext("Article A", "https://example.com/a"),
        _make_fulltext("Video B", "https://youtube.com/watch?v=xyz", "youtube"),
    ]
    output_path = tmp_path / "index.md"

    generate_sources_index(fulltexts, "My Notebook", "2026-04-20", output_path)

    content = output_path.read_text()
    assert "[[Article A]]" in content
    assert "[[Video B]]" in content
    assert "https://example.com/a" in content


def test_generate_sources_index_links_to_notebook(tmp_path):
    from sync.transformer import generate_sources_index
    fulltexts = [_make_fulltext("Article A", "https://example.com/a")]
    output_path = tmp_path / "index.md"

    generate_sources_index(fulltexts, "My Notebook", "2026-04-20", output_path)

    content = output_path.read_text()
    assert "[[My Notebook]]" in content
