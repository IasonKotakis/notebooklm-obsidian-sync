# notebooklm-obsidian-sync

`notebooklm-obsidian-sync` turns your NotebookLM notebooks into structured, interlinked Obsidian notes — automatically. One command and your study guides, mind maps, audio transcripts, quizzes, and source notes land in your vault, ready to think with.

![Python](https://img.shields.io/badge/python-3.12-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Status](https://img.shields.io/badge/status-beta-yellow)

---

## How it works

You run `python sync.py`. That's it.

Behind the scenes, it connects to your NotebookLM account and fetches every notebook you have. For each one, it downloads the study guide report, the mind map, the audio overview, any quizzes, and the full text of all your sources.

The audio overview gets transcribed locally on your machine using Whisper — nothing leaves your computer for that step. Then the report and transcript get sent to Claude, which transforms them into a clean, structured Obsidian note with YAML frontmatter, wikilinks, key concepts, and open questions — the kind of note you'd actually want to read and link from.

The mind map becomes an Obsidian Canvas file. The quiz becomes a note with collapsible answer callouts. Each source gets its own atomic note. Everything lands in your vault under `00 - Inbox/[notebook-title]/`, already interlinked and ready to connect to the rest of your knowledge graph.

On subsequent runs, only notebooks that have actually changed get re-processed. Already up-to-date notebooks are skipped in milliseconds.

---

## What you get

For each notebook, the tool creates:

- **`[Title].md`** — the main Obsidian note: frontmatter, core idea, key concepts, connections, open questions, wikilinks throughout
- **`[Title].canvas`** — the mind map as an Obsidian Canvas file, laid out spatially
- **`transcript.md`** — the audio overview, transcribed locally via Whisper
- **`quiz.md`** — multiple-choice questions with answers hidden in collapsed callouts
- **`sources/[source].md`** — one atomic note per source (web page, PDF, YouTube video)
- **`sources/index.md`** — a table of all sources with types and URLs

Everything is plain markdown. No lock-in, no proprietary formats, no cloud sync required.

---

## ⚠️ Important disclaimers

- **notebooklm-py** is an unofficial, community-built Python client. It is **not** affiliated with or supported by Google. It may break without warning if Google changes their platform.
- **This tool requires your own Anthropic API key.** You will be billed directly by Anthropic for API usage. Estimated cost: ~$0.03–$0.04 per notebook (default mode); ~$0.11–$0.15 per notebook with source notes enabled.
- **Audio and content stay local.** Only the extracted text (study guide report + Whisper transcript) is sent to Anthropic. Audio files, cookies, and file paths never leave your machine.

---

## Prerequisites

- Python 3.12+
- [Obsidian](https://obsidian.md) with an existing vault
- An [Anthropic account](https://console.anthropic.com) with an API key
- A Google account with existing [NotebookLM](https://notebooklm.google.com) access

---

## Installation

```bash
# 1. Clone the repo
git clone https://github.com/IasonKotakis/notebooklm-obsidian-sync
cd notebooklm-obsidian-sync

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create your config file
cp config.yaml.example config.yaml          # Mac/Linux
# copy config.yaml.example config.yaml     # Windows

# 4. Set your Obsidian vault path
#    Open config.yaml and set obsidian.vault_path to your vault location

# 5. Create your .env file
cp .env.example .env                         # Mac/Linux
# copy .env.example .env                    # Windows

# 6. Add your Anthropic API key
#    Open .env and set ANTHROPIC_API_KEY=your-key-here

# 7. Authenticate with NotebookLM (first run only)
notebooklm login

# 8. Run the sync
python sync.py
```

---

## What's inside

```
sync/
├── fetcher.py       — downloads all artifacts from NotebookLM (report, audio, mindmap, quiz, sources)
├── transcriber.py   — runs Whisper locally to transcribe audio overviews
├── transformer.py   — calls Claude to generate structured Obsidian notes; converts mindmaps to Canvas
└── state.py         — tracks which notebooks have changed so unchanged ones are skipped
```

`sync.py` is the entry point. It wires everything together and writes all output into your vault.

---

## Cost

| Step | Tool | Cost |
|------|------|------|
| Fetch notebooks | notebooklm-py | Free |
| Transcribe audio | Whisper (local) | Free |
| Generate main Obsidian note | Anthropic API | ~$0.03–$0.04 per notebook |
| Generate source notes (optional) | Anthropic API | ~$0.008 per source |

**Default mode** (no source notes): ~$0.03–$0.04 per notebook.
**With source notes**: ~$0.11–$0.15 per notebook (assumes ~10 sources).
A vault of 50 notebooks costs roughly $1.50–$2.00 for the initial sync; subsequent runs are near-zero since only changed notebooks are re-processed.

Only the Claude transformation step costs money.

---

## Philosophy

- **Local-first** — audio, transcription, and your vault never leave your machine
- **Single command** — no dashboards, no UI, no manual steps
- **Incremental** — only changed notebooks are re-processed; the rest are skipped instantly
- **Plain files** — everything is markdown; works with any Obsidian setup

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup instructions, how to run tests, and PR guidelines.

Note that `notebooklm-py` is a dependency we don't control. If something breaks because Google changed their platform, tag the issue `[upstream]`.

---

## License

MIT — see [LICENSE](LICENSE).
