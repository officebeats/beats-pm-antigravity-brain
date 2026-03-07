"""Memory helpers for logs and session state."""

from __future__ import annotations

from pathlib import Path

from .config import get_root_directory


def _append_to_log(filepath: str, content: str) -> bool:
    """Append a new line to a log file."""
    try:
        root = get_root_directory()
        full_path = Path(root) / filepath
        full_path.parent.mkdir(parents=True, exist_ok=True)
        with full_path.open("a", encoding="utf-8") as f:
            f.write(content + "\n")
        return True
    except Exception:
        return False


def get_session_memory() -> str:
    """Read the last known state from SESSION_MEMORY.md."""
    root = get_root_directory()
    full_path = Path(root) / "SESSION_MEMORY.md"
    try:
        if full_path.exists():
            return full_path.read_text(encoding="utf-8")
    except Exception:
        pass
    return "No previous session memory found."
