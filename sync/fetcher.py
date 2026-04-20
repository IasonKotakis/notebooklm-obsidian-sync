"""Download artifacts from NotebookLM notebooks.

Output paths are passed in by sync.py, which resolves them from config.yaml.
"""

import hashlib
import json
import sys
import time
from pathlib import Path
from typing import Any

from notebooklm import NotebookLMClient
from notebooklm.exceptions import AuthError, ArtifactNotReadyError
from notebooklm.types import SourceFulltext


def _sha256(path: Path) -> str:
    """Compute SHA-256 hash of a file."""
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return f"sha256:{h.hexdigest()}"


def _sha256_str(text: str) -> str:
    """Compute SHA-256 hash of a string."""
    return f"sha256:{hashlib.sha256(text.encode()).hexdigest()}"


async def list_notebooks(client: NotebookLMClient) -> list[Any]:
    """Return all notebooks from NotebookLM."""
    return await client.notebooks.list()


async def ensure_report(client: NotebookLMClient, notebook_id: str, output_path: Path) -> str:
    """Download study guide report, generating it first if missing."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    reports = await client.artifacts.list_reports(notebook_id)
    completed = [r for r in reports if r.is_completed]

    if not completed:
        print(f"    [fetch] Report missing - generating...", end="", flush=True)
        t0 = time.time()
        status = await client.artifacts.generate_study_guide(notebook_id)
        if status.is_failed:
            raise RuntimeError(f"Report generation failed immediately: {status.error or 'RPC error'}")
        status = await client.artifacts.wait_for_completion(
            notebook_id, status.task_id, timeout=600.0
        )
        elapsed = time.time() - t0
        if status.is_failed:
            raise RuntimeError(f"Report generation failed: {status.error or 'unknown error'}")
        print(f" done ({elapsed:.0f}s)", flush=True)
        print(f"    [fetch] Downloading report...", end="", flush=True)
    else:
        print(f"    [fetch] Downloading report...", end="", flush=True)

    await client.artifacts.download_report(notebook_id, str(output_path))
    print(" done")
    return _sha256(output_path)


async def ensure_audio(client: NotebookLMClient, notebook_id: str, output_path: Path) -> str | None:
    """Download audio overview MP3, generating it first if missing.

    Returns the SHA-256 hash of the downloaded file, or None if audio
    generation/download failed (audio is optional).
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        audios = await client.artifacts.list_audio(notebook_id)
        completed = [a for a in audios if a.is_completed]

        if not completed:
            print(f"    [fetch] Audio overview missing - generating...", end="", flush=True)
            t0 = time.time()
            status = await client.artifacts.generate_audio(notebook_id)
            if status.is_failed:
                print(f" skipped")
                print(f"  [warn] Audio generation failed immediately: {status.error or 'RPC error'}. Skipping audio.")
                return None
            status = await client.artifacts.wait_for_completion(
                notebook_id, status.task_id, timeout=600.0
            )
            elapsed = time.time() - t0
            if status.is_failed:
                print(f" skipped")
                print(f"  [warn] Audio generation failed: {status.error or 'RPC error'}. Skipping audio.")
                return None
            print(f" done ({elapsed:.0f}s)", flush=True)
            print(f"    [fetch] Downloading audio...", end="", flush=True)
        else:
            print(f"    [fetch] Downloading audio...", end="", flush=True)

        await client.artifacts.download_audio(notebook_id, str(output_path))
        print(" done")
        return _sha256(output_path)

    except Exception as e:
        print(f" skipped")
        print(f"  [warn] Audio unavailable: {e}. Skipping audio.")
        return None


async def ensure_video(client: NotebookLMClient, notebook_id: str, output_path: Path) -> str | None:
    """Download video overview MP4, generating it first if missing.

    Returns the SHA-256 hash of the downloaded file, or None if video
    generation/download failed (video is optional).
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        videos = await client.artifacts.list_video(notebook_id)
        completed = [v for v in videos if v.is_completed]

        if not completed:
            print(f"    [fetch] Video overview missing - generating...", end="", flush=True)
            t0 = time.time()
            status = await client.artifacts.generate_video(notebook_id)
            if status.is_failed:
                print(f" skipped")
                print(f"  [warn] Video generation failed immediately: {status.error or 'RPC error'}. Skipping video.")
                return None
            status = await client.artifacts.wait_for_completion(
                notebook_id, status.task_id, timeout=600.0
            )
            elapsed = time.time() - t0
            if status.is_failed:
                print(f" skipped")
                print(f"  [warn] Video generation failed: {status.error or 'RPC error'}. Skipping video.")
                return None
            print(f" done ({elapsed:.0f}s)", flush=True)
            print(f"    [fetch] Downloading video...", end="", flush=True)
        else:
            print(f"    [fetch] Downloading video...", end="", flush=True)

        await client.artifacts.download_video(notebook_id, str(output_path))
        print(" done")
        return _sha256(output_path)

    except Exception as e:
        print(f" skipped")
        print(f"  [warn] Video unavailable: {e}. Skipping video.")
        return None


async def ensure_mindmap(client: NotebookLMClient, notebook_id: str, output_path: Path) -> str:
    """Download mind map JSON, generating it first if missing."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    mind_maps = await client.notes.list_mind_maps(notebook_id)

    if not mind_maps:
        print(f"    [fetch] Mind map missing - generating...", end="", flush=True)
        t0 = time.time()
        await client.artifacts.generate_mind_map(notebook_id)
        elapsed = time.time() - t0
        print(f" done ({elapsed:.0f}s)", flush=True)
        print(f"    [fetch] Downloading mind map...", end="", flush=True)
    else:
        print(f"    [fetch] Downloading mind map...", end="", flush=True)

    await client.artifacts.download_mind_map(notebook_id, str(output_path))
    print(" done")
    return _sha256(output_path)


async def ensure_quiz(client: NotebookLMClient, notebook_id: str, output_path: Path) -> str | None:
    """Download quiz JSON, generating it first if missing.

    Returns the SHA-256 hash of the downloaded file, or None if quiz
    generation/download failed (quiz is optional).
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        quizzes = await client.artifacts.list_quizzes(notebook_id)
        completed = [q for q in quizzes if q.is_completed]

        if not completed:
            print(f"    [fetch] Quiz missing - generating...", end="", flush=True)
            t0 = time.time()
            status = await client.artifacts.generate_quiz(notebook_id)
            if status.is_failed:
                print(f" skipped")
                print(f"  [warn] Quiz generation failed immediately: {status.error or 'RPC error'}. Skipping quiz.")
                return None
            status = await client.artifacts.wait_for_completion(
                notebook_id, status.task_id, timeout=600.0
            )
            elapsed = time.time() - t0
            if status.is_failed:
                print(f" skipped")
                print(f"  [warn] Quiz generation failed: {status.error or 'RPC error'}. Skipping quiz.")
                return None
            print(f" done ({elapsed:.0f}s)", flush=True)
            print(f"    [fetch] Downloading quiz...", end="", flush=True)
        else:
            print(f"    [fetch] Downloading quiz...", end="", flush=True)

        await client.artifacts.download_quiz(notebook_id, str(output_path), output_format="json")
        print(" done")
        return _sha256(output_path)

    except Exception as e:
        print(f" skipped")
        print(f"  [warn] Quiz unavailable: {e}. Skipping quiz.")
        return None


async def fetch_sources(client: NotebookLMClient, notebook_id: str) -> tuple[list[SourceFulltext], str]:
    """Fetch fulltext for all ready sources in a notebook.

    Returns a tuple of (list of SourceFulltext, sources_hash).
    The hash is computed from source IDs+titles so adding/removing a source
    triggers re-processing without re-fetching all fulltexts.
    """
    print(f"    [fetch] Fetching sources...", end="", flush=True)

    try:
        sources = await client.sources.list(notebook_id)
        ready = [s for s in sources if s.is_ready]

        fulltexts = []
        for source in ready:
            try:
                ft = await client.sources.get_fulltext(notebook_id, source.id)
                fulltexts.append(ft)
            except Exception as e:
                print(f"\n  [warn] Could not get fulltext for source '{source.title}': {e}")

        # Hash based on sorted source IDs+titles to detect additions/removals
        source_fingerprint = json.dumps(
            sorted([(s.id, s.title or "") for s in ready]), sort_keys=True
        )
        sources_hash = _sha256_str(source_fingerprint)

        print(f" {len(fulltexts)} source(s) fetched")
        return fulltexts, sources_hash

    except Exception as e:
        print(f" skipped")
        print(f"  [warn] Could not fetch sources: {e}")
        return [], ""


async def fetch_notebook_artifacts(
    client: NotebookLMClient,
    notebook_id: str,
    output_dir: Path,
    video_dir: Path,
) -> tuple[dict[str, str], list[SourceFulltext]]:
    """Download all artifact types. Returns (hashes_dict, source_fulltexts).

    Optional artifact hashes (audio, video, quiz) are omitted from the dict
    if generation failed, so subsequent runs will retry without forcing a
    full re-sync of artifacts that succeeded.
    """
    report_path = output_dir / "report.md"
    audio_path = output_dir / "audio_overview.mp3"
    mindmap_path = output_dir / "mindmap.json"
    video_path = video_dir / "video_overview.mp4"
    quiz_path = output_dir / "quiz.json"

    hashes: dict[str, str] = {}

    hashes["report"] = await ensure_report(client, notebook_id, report_path)

    audio_hash = await ensure_audio(client, notebook_id, audio_path)
    if audio_hash is not None:
        hashes["audio"] = audio_hash

    video_hash = await ensure_video(client, notebook_id, video_path)
    if video_hash is not None:
        hashes["video"] = video_hash

    hashes["mind_map"] = await ensure_mindmap(client, notebook_id, mindmap_path)

    quiz_hash = await ensure_quiz(client, notebook_id, quiz_path)
    if quiz_hash is not None:
        hashes["quiz"] = quiz_hash

    fulltexts, sources_hash = await fetch_sources(client, notebook_id)
    if sources_hash:
        hashes["sources"] = sources_hash

    return hashes, fulltexts


def handle_auth_error() -> None:
    """Print auth error message and exit."""
    print("\n[error] NotebookLM session expired or invalid.")
    print("        Run: notebooklm login")
    sys.exit(1)
