"""Transcribe MP3 audio using Whisper small model."""

from pathlib import Path


def transcribe(mp3_path: Path, output_path: Path, force: bool = False) -> None:
    """Run Whisper on mp3_path and write transcript markdown to output_path.

    Skips if output_path already exists and force is False.
    """
    if not mp3_path.exists():
        print(f"    [transcribe] No audio file, skipping transcript.")
        return

    if output_path.exists() and not force:
        print(f"    [transcribe] Transcript exists, skipping.")
        return

    print(f"    [transcribe] Running Whisper small...", end="", flush=True)

    import time
    import whisper

    t0 = time.time()
    model = whisper.load_model("small")
    result = model.transcribe(str(mp3_path))
    elapsed = time.time() - t0

    transcript_text = result["text"].strip()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        f"## Audio Overview Transcript\n\n{transcript_text}\n",
        encoding="utf-8",
    )
    print(f" done ({elapsed:.0f}s)")
