"""Generate system/content_index.json for fast file lookups."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

import sys

# Path setup (MUST be before 'system.*' imports)
CURRENT_FILE = Path(__file__).resolve()
SYSTEM_ROOT = CURRENT_FILE.parent.parent
BRAIN_ROOT = SYSTEM_ROOT.parent
sys.path.insert(0, str(BRAIN_ROOT))

from system.utils.config import get_config
from system.utils.filesystem import atomic_write
from system.utils.ui import print_cyan, print_success, print_warning

INDEX_FILE = SYSTEM_ROOT / "content_index.json"

SCAN_DIRS = [
    "1. Company",
    "2. Products",
    "3. Meetings",
    "4. People",
    "5. Trackers",
    ".agent",
]

EXCLUDE_DIRS = {".git", ".pytest_cache", "node_modules", "__pycache__"}


def _should_index(path: Path) -> bool:
    if path.name.startswith(".") and path.parent.name not in {".agent"}:
        return False
    if path.is_dir():
        return False
    return True


def _scan_directory(root: Path) -> List[Dict[str, str]]:
    entries: List[Dict[str, str]] = []
    for path in root.rglob("*"):
        if any(part in EXCLUDE_DIRS for part in path.parts):
            continue
        if not _should_index(path):
            continue
        rel_path = path.relative_to(BRAIN_ROOT).as_posix()
        entries.append(
            {
                "path": rel_path,
                "name": path.name,
                "ext": path.suffix.lower(),
            }
        )
    return entries


def scan_files() -> int:
    print_cyan("\n🧭 Building content index...")
    index: Dict[str, List[Dict[str, str]]] = {"files": []}
    for rel_dir in SCAN_DIRS:
        target = BRAIN_ROOT / rel_dir
        if not target.exists():
            print_warning(f"Missing scan dir: {rel_dir}")
            continue
        index["files"].extend(_scan_directory(target))

    index_path = get_config("paths.index", str(INDEX_FILE))
    index_target = Path(index_path)
    if not index_target.is_absolute():
        index_target = BRAIN_ROOT / index_target

    payload = json.dumps(index, indent=2)
    if not atomic_write(index_target, payload):
        raise RuntimeError("Failed to write content index")

    print_success(f"Indexed {len(index['files'])} files")
    return len(index["files"])


if __name__ == "__main__":
    scan_files()
