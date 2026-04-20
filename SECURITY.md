# Security

## Data flow

Understanding what stays local and what leaves your machine:

```
Google (NotebookLM) ──── notebooklm-py ────► fetcher.py
                                                  │
                                                  ▼
                                         report.md  (local)
                                         mindmap.json (local)
                                         audio_overview.mp3 (local)
                                         quiz.json (local)
                                                  │
                                                  ▼
                                         transcriber.py  ◄── Whisper (local)
                                                  │
                                                  ▼
                                         transcript.md (local)
                                                  │
                                     ┌────────────▼────────────┐
                                     │  transformer.py         │
                                     │  report text +          │──► Anthropic API
                                     │  transcript text        │◄── generated note
                                     └─────────────────────────┘
                                                  │
                                                  ▼
                                         Obsidian vault (local)
```

**Only one outbound call**: the extracted text content (study guide report + audio transcript) sent to the Anthropic API for note generation.

---

## API key handling

- Your `ANTHROPIC_API_KEY` is stored in a `.env` file in the project directory.
- `.env` is listed in `.gitignore` and will never be committed.
- The key is loaded into the process environment at startup via `python-dotenv`.
- It is never logged, printed, or transmitted anywhere other than the Anthropic API request header.

---

## Google authentication cookies

- `notebooklm-py` stores Google session cookies locally (managed entirely by that library).
- This project never reads, logs, or transmits those cookies.
- Cookie handling is entirely the responsibility of the `notebooklm-py` library.

---

## Audio and transcription

- Audio overview MP3 files are downloaded locally.
- Transcription runs entirely on-device using the [Whisper](https://github.com/openai/whisper) model.
- Audio is never sent to any external service.

---

## What IS sent to Anthropic

Only the following text is sent to the Anthropic API:

1. The study guide report text (plain markdown from NotebookLM)
2. The Whisper-generated transcript text (if available)
3. The notebook title and date

No audio, no cookies, no file paths, no personal identifiers beyond what is present in the notebook content itself.

---

## No telemetry

This project contains no analytics, telemetry, tracking pixels, or any external calls beyond:

- `notebooklm-py` → Google (to fetch your notebooks)
- `transformer.py` → Anthropic API (to generate notes)

---

## Reporting a vulnerability

Open an issue tagged `[security]` in this repository. For sensitive disclosures, email the maintainer directly.
