# notebooklm-obsidian-sync

Sync your NotebookLM notebooks into structured Obsidian notes with a single command.

![Python](https://img.shields.io/badge/python-3.12-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Status](https://img.shields.io/badge/status-beta-yellow)

---

## What it does

`notebooklm-obsidian-sync` fetches your NotebookLM notebooks, transcribes audio overviews locally using Whisper, sends the extracted text to the Anthropic API, and writes structured Obsidian markdown notes — including Canvas mind maps, quiz notes, and source notes. One command: `python sync.py`.

```
NotebookLM → fetcher.py  (local)
           → transcriber.py  (local Whisper)
           → transformer.py  (Anthropic API ← only external call)
           → Obsidian vault  (local)
```

---

## ⚠️ Important disclaimers

- **notebooklm-py** is an unofficial, community-built Python client. It is **not** affiliated with or supported by Google. It may break without warning if Google changes their platform.
- **This tool requires your own Anthropic API key.** You will be billed directly by Anthropic for API usage. Estimated cost: ~$0.01 per notebook synced.
- **Audio and content stay local.** Only the transformed text (study guide report + transcript) is sent to Anthropic for note generation. Nothing else leaves your machine.

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
git clone https://github.com/[your-username]/notebooklm-obsidian-sync
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

## Cost

| Step | Tool | Cost |
|------|------|------|
| Fetch notebooks | notebooklm-py | Free |
| Transcribe audio | Whisper (local) | Free |
| Generate Obsidian notes | Anthropic API | ~$0.01 per notebook |

Only the Claude transformation step costs money.

---

## Current status / roadmap

**Working:**
- Study guide reports → structured Obsidian notes
- Mind maps → Obsidian Canvas files
- Audio overviews → local Whisper transcription
- Quiz JSON → collapsible quiz notes

**In progress:**
- Video overviews
- Source URL extraction
- Quiz generation improvements

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

MIT — see [LICENSE](LICENSE).
