import json
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest


def test_sanitize_title_removes_forbidden_chars():
    from sync.state import sanitize_title
    assert sanitize_title("My Note: Part 1/2") == "My Note- Part 1-2"


def test_sanitize_title_strips_leading_trailing_spaces():
    from sync.state import sanitize_title
    assert sanitize_title("  My Note  ") == "My Note"


def test_sanitize_title_handles_question_marks():
    from sync.state import sanitize_title
    assert sanitize_title("What is AI?") == "What is AI"


def test_needs_sync_returns_true_when_no_state(tmp_path):
    from sync.state import SyncState
    state = SyncState(tmp_path / ".sync_state.json")
    assert state.needs_sync("nb_abc", {"report": "hash1"}, force=False) is True


def test_needs_sync_returns_false_when_hashes_match(tmp_path):
    from sync.state import SyncState
    state_path = tmp_path / ".sync_state.json"
    state_path.write_text(json.dumps({
        "nb_abc": {
            "last_synced": "2026-01-01T00:00:00",
            "title": "Test",
            "artifact_hashes": {"report": "hash1", "audio": "hash2", "mind_map": "hash3"}
        }
    }))
    state = SyncState(state_path)
    assert state.needs_sync("nb_abc", {"report": "hash1", "audio": "hash2", "mind_map": "hash3"}, force=False) is False


def test_needs_sync_returns_true_when_hash_changed(tmp_path):
    from sync.state import SyncState
    state_path = tmp_path / ".sync_state.json"
    state_path.write_text(json.dumps({
        "nb_abc": {
            "last_synced": "2026-01-01T00:00:00",
            "title": "Test",
            "artifact_hashes": {"report": "old_hash"}
        }
    }))
    state = SyncState(state_path)
    assert state.needs_sync("nb_abc", {"report": "new_hash"}, force=False) is True


def test_needs_sync_returns_true_when_force(tmp_path):
    from sync.state import SyncState
    state_path = tmp_path / ".sync_state.json"
    state_path.write_text(json.dumps({
        "nb_abc": {
            "last_synced": "2026-01-01T00:00:00",
            "title": "Test",
            "artifact_hashes": {"report": "hash1"}
        }
    }))
    state = SyncState(state_path)
    assert state.needs_sync("nb_abc", {"report": "hash1"}, force=True) is True


def test_update_writes_state(tmp_path):
    from sync.state import SyncState
    state_path = tmp_path / ".sync_state.json"
    state = SyncState(state_path)
    state.update("nb_abc", "My Notebook", {"report": "hash1"})
    data = json.loads(state_path.read_text())
    assert data["nb_abc"]["title"] == "My Notebook"
    assert data["nb_abc"]["artifact_hashes"]["report"] == "hash1"
    assert "last_synced" in data["nb_abc"]
