"""Setup, .env management, and sync state tracking."""

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent
ENV_PATH = PROJECT_ROOT / ".env"
STATE_PATH = PROJECT_ROOT / ".sync_state.json"
_CONFIG_PATH = PROJECT_ROOT / "config.yaml"


def load_config() -> dict:
    """Load config.yaml from project root. Exits with clear error if not found."""
    if not _CONFIG_PATH.exists():
        print(
            "config.yaml not found. Copy config.yaml.example to config.yaml and "
            "set your vault path."
        )
        sys.exit(1)
    import yaml
    return yaml.safe_load(_CONFIG_PATH.read_text(encoding="utf-8"))


# Keep VAULT_ROOT as an alias so existing internals that reference it still work.
VAULT_ROOT = PROJECT_ROOT


def sanitize_title(title: str) -> str:
    """Replace filesystem-forbidden characters and strip whitespace."""
    sanitized = re.sub(r'[:/\\?*"<>|]', "-", title)
    sanitized = sanitized.replace("--", "-").rstrip("-")
    return sanitized.strip()


def ensure_setup() -> None:
    """Install missing packages and prompt for API key on first run."""
    _ensure_packages(["anthropic", "python-dotenv"])
    _ensure_env()
    _load_env()


def _ensure_packages(packages: list[str]) -> None:
    for package in packages:
        module_name = package.replace("-", "_")
        try:
            __import__(module_name)
        except ImportError:
            print(f"[setup] Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "-q"])
            print(f"[setup] {package} installed.")


def _ensure_env() -> None:
    if ENV_PATH.exists():
        return
    print("[setup] First run: ANTHROPIC_API_KEY not found.")
    key = input("Enter your Anthropic API key: ").strip()
    if not key:
        print("[setup] No key provided. Exiting.")
        sys.exit(1)
    ENV_PATH.write_text(f"ANTHROPIC_API_KEY={key}\n")
    print(f"[setup] API key saved to {ENV_PATH}")


def _load_env() -> None:
    from dotenv import load_dotenv
    load_dotenv(ENV_PATH)


class SyncState:
    """Reads and writes .sync_state.json."""

    def __init__(self, path: Path = STATE_PATH):
        self._path = path
        self._data: dict = {}
        if path.exists():
            self._data = json.loads(path.read_text(encoding="utf-8"))

    def needs_sync(self, notebook_id: str, new_hashes: dict[str, str], force: bool) -> bool:
        """Return True if this notebook needs to be transformed."""
        if force:
            return True
        entry = self._data.get(notebook_id)
        if not entry:
            return True
        return entry.get("artifact_hashes") != new_hashes

    def update(self, notebook_id: str, title: str, hashes: dict[str, str]) -> None:
        """Persist updated state for a notebook."""
        self._data[notebook_id] = {
            "last_synced": datetime.now(timezone.utc).isoformat(),
            "title": title,
            "artifact_hashes": hashes,
        }
        self._path.write_text(
            json.dumps(self._data, indent=2, ensure_ascii=False), encoding="utf-8"
        )
