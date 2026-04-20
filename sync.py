"""NotebookLM to Obsidian sync script.

Usage:
    python sync.py           # Sync changed notebooks only
    python sync.py --force   # Re-sync all notebooks
"""

import argparse
import asyncio
import traceback
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync NotebookLM to Obsidian")
    parser.add_argument("--force", action="store_true", help="Re-sync all notebooks")
    return parser.parse_args()


async def sync_notebook(client, notebook, state, vault_root: Path, inbox: Path, sources_dir: Path, force: bool) -> bool:
    """Sync a single notebook. Returns True if notebook was synced, False if skipped."""
    from sync.fetcher import fetch_notebook_artifacts
    from sync.transcriber import transcribe
    from sync.transformer import (
        convert_mindmap,
        format_quiz_note,
        generate_note,
        generate_source_note,
        generate_sources_index,
        _safe_source_filename,
    )
    from sync.state import sanitize_title

    notebook_id = notebook.id
    title = notebook.title or notebook_id
    safe_title = sanitize_title(title)
    output_dir = inbox / safe_title
    video_dir = sources_dir / safe_title
    today = date.today().isoformat()

    print(f"\n[sync] {title}")

    # Always fetch artifacts to get current hashes
    try:
        hashes, fulltexts = await fetch_notebook_artifacts(
            client, notebook_id, output_dir, video_dir
        )
    except Exception as e:
        print(f"  [error] Fetch failed: {e}")
        return False

    # Check if transformation is needed
    if not state.needs_sync(notebook_id, hashes, force=force):
        print(f"  up to date, skipping.")
        return False

    # --- Transcribe audio ---
    mp3_path = output_dir / "audio_overview.mp3"
    transcript_path = output_dir / "transcript.md"
    try:
        transcribe(mp3_path, transcript_path, force=force)
    except Exception as e:
        print(f"  [warn] Transcription failed: {e}. Continuing without transcript.")
        transcript_path = None

    # --- Determine video vault path for note linking ---
    video_mp4 = video_dir / "video_overview.mp4"
    video_vault_path = None
    if video_mp4.exists():
        video_vault_path = str(video_mp4.relative_to(vault_root)).replace("\\", "/")

    # --- Generate main Obsidian note via Claude ---
    report_path = output_dir / "report.md"
    note_path = output_dir / f"{safe_title}.md"
    try:
        generate_note(
            report_path, transcript_path, title, today, note_path,
            video_vault_path=video_vault_path,
        )
    except Exception as e:
        print(f"  [error] Claude note generation failed: {e}")
        return False

    # --- Convert mind map to Canvas ---
    mindmap_path = output_dir / "mindmap.json"
    canvas_path = output_dir / f"{safe_title}.canvas"
    try:
        convert_mindmap(mindmap_path, canvas_path)
        print(f"    [transform] Canvas written.")
    except Exception as e:
        print(f"  [warn] Canvas conversion failed: {e}")

    # --- Format quiz note ---
    quiz_json_path = output_dir / "quiz.json"
    if quiz_json_path.exists():
        quiz_note_path = output_dir / "quiz.md"
        try:
            format_quiz_note(quiz_json_path, quiz_note_path, title, today)
            print(f"    [transform] Quiz note written.")
        except Exception as e:
            print(f"  [warn] Quiz formatting failed: {e}")

    # --- Generate source notes ---
    if fulltexts:
        sources_out = output_dir / "sources"
        sources_out.mkdir(parents=True, exist_ok=True)
        print(f"    [transform] Generating {len(fulltexts)} source note(s)...")
        for ft in fulltexts:
            safe_source = _safe_source_filename(ft.title or "Untitled")
            source_note_path = sources_out / f"{safe_source}.md"
            try:
                print(f"      - {ft.title or 'Untitled'}...", end="", flush=True)
                generate_source_note(ft, title, today, source_note_path)
                print(" done")
            except Exception as e:
                print(f" failed: {e}")

        index_path = sources_out / "index.md"
        try:
            generate_sources_index(fulltexts, title, today, index_path)
            print(f"    [transform] Sources index written.")
        except Exception as e:
            print(f"  [warn] Sources index failed: {e}")

    # --- Update sync state ---
    state.update(notebook_id, title, hashes)
    print(f"    [write] {output_dir.relative_to(vault_root)}")
    return True


async def main() -> None:
    args = parse_args()

    from sync.state import ensure_setup, SyncState, load_config
    ensure_setup()

    cfg = load_config()
    vault_root = Path(cfg["obsidian"]["vault_path"])
    inbox_folder = cfg.get("sync", {}).get("inbox_folder", "00 - Inbox")
    sources_folder = "07 - Sources"
    inbox = vault_root / inbox_folder
    sources_dir = vault_root / sources_folder

    from notebooklm import NotebookLMClient
    from notebooklm.exceptions import AuthError
    from sync.fetcher import list_notebooks, handle_auth_error

    state = SyncState()

    try:
        async with await NotebookLMClient.from_storage() as client:
            notebooks = await list_notebooks(client)
            print(f"[sync] Found {len(notebooks)} notebook(s)")

            synced = 0
            skipped = 0

            for notebook in notebooks:
                try:
                    was_synced = await sync_notebook(
                        client, notebook, state,
                        vault_root=vault_root,
                        inbox=inbox,
                        sources_dir=sources_dir,
                        force=args.force,
                    )
                    if was_synced:
                        synced += 1
                    else:
                        skipped += 1
                except Exception as e:
                    print(f"  [error] Unexpected error for notebook {notebook.id}: {e}")
                    traceback.print_exc()
                    skipped += 1
                    continue

            print(f"\n[sync] Complete. {synced} synced, {skipped} skipped.")

    except AuthError:
        handle_auth_error()


if __name__ == "__main__":
    asyncio.run(main())
