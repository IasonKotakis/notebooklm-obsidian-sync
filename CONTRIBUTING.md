# Contributing to notebooklm-obsidian-sync

Thanks for your interest in contributing.

---

## Dev environment setup

```bash
git clone https://github.com/[your-username]/notebooklm-obsidian-sync
cd notebooklm-obsidian-sync
pip install -r requirements.txt
cp config.yaml.example config.yaml   # fill in vault_path
cp .env.example .env                 # fill in ANTHROPIC_API_KEY
```

---

## Running tests

```bash
pytest tests/ -v
```

All tests must pass before submitting a PR. Tests do not require a live NotebookLM or Anthropic account — they use fixtures and mocks.

---

## Pull request guidelines

- **One feature or fix per PR.** Mixed concerns make review harder.
- **Tests required.** If your PR adds or changes behaviour, include tests that cover it.
- **Describe the blast radius.** In the PR description, answer: *what breaks if this PR is NOT merged?* This helps reviewers understand urgency and scope.
- **Keep commits clean.** Squash work-in-progress commits before opening the PR.

---

## Upstream dependency note

`notebooklm-py` is a community-built, unofficial client for NotebookLM. We have no control over it. If Google changes their platform and something breaks:

- Tag the issue `[upstream]`
- Link to the relevant `notebooklm-py` issue if one exists
- Do not patch around upstream breakage inside this repo unless there is no other option

---

## Code style

- Python 3.12+, typed where practical
- No external formatters enforced — just be consistent with the surrounding code
- Keep functions focused; if a function is doing two things, split it
