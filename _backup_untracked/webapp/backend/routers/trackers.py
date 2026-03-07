"""
Tracker router — reads, parses, and serves tracker markdown files.
Tracker paths are sourced from system/config.json (never hardcoded).
"""
import json
import re
import hashlib
from pathlib import Path
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query

from models.tracker import TrackerItem, TrackerFile, ItemStatus, UpdateItemRequest

router = APIRouter(prefix="/api/trackers", tags=["trackers"])

# ── Config ────────────────────────────────────────────────────────────────────
BRAIN_ROOT = Path(__file__).resolve().parents[3]  # repo root
CONFIG_PATH = BRAIN_ROOT / "system" / "config.json"

TRACKER_LABELS = {
    "bugs_master": "Bug Tracker",
    "boss_requests": "Boss Requests",
    "decision_log": "Decision Log",
    "projects_master": "Project Tracker",
    "delegated_tasks": "Delegated Tasks",
    "eng_tasks": "Eng Tasks",
    "ux_tasks": "UX Tasks",
}

TRACKER_ICONS = {
    "bugs_master": "bug",
    "boss_requests": "star",
    "decision_log": "scale",
    "projects_master": "folder",
    "delegated_tasks": "users",
    "eng_tasks": "code",
    "ux_tasks": "palette",
}


def _load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return json.load(f)


def _item_id(tracker_key: str, line_number: int, text: str) -> str:
    raw = f"{tracker_key}:{line_number}:{text}"
    return hashlib.md5(raw.encode()).hexdigest()[:12]


def _parse_status(marker: str) -> ItemStatus:
    m = marker.strip().lower()
    if m == "x":
        return ItemStatus.done
    if m == "-":
        return ItemStatus.in_progress
    return ItemStatus.pending


def _extract_tags(text: str) -> List[str]:
    return re.findall(r"#(\w+)", text)


def _extract_priority(text: str) -> Optional[str]:
    m = re.search(r"\[P([0-3])\]", text, re.IGNORECASE)
    return f"P{m.group(1)}" if m else None


def parse_tracker_file(path: Path, key: str) -> TrackerFile:
    label = TRACKER_LABELS.get(key, key.replace("_", " ").title())
    items: List[TrackerItem] = []

    if not path.exists():
        return TrackerFile(
            key=key, label=label, path=str(path.relative_to(BRAIN_ROOT)),
            items=[], total=0, pending=0, in_progress=0, done=0,
        )

    content = path.read_text(encoding="utf-8", errors="replace")
    lines = content.splitlines()
    current_section: Optional[str] = None

    for i, line in enumerate(lines):
        # Track section headers
        if line.startswith("## "):
            current_section = line[3:].strip()
            continue
        if line.startswith("# "):
            current_section = line[2:].strip()
            continue

        # Match checklist items: - [ ], - [x], - [-]
        m = re.match(r"^\s*-\s+\[([x\-\s])\]\s+(.*)", line, re.IGNORECASE)
        if m:
            marker, text = m.group(1), m.group(2).strip()
            status = _parse_status(marker)
            item = TrackerItem(
                id=_item_id(key, i, text),
                tracker=key,
                tracker_label=label,
                section=current_section,
                text=text,
                status=status,
                raw_line=line,
                line_number=i,
                tags=_extract_tags(text),
                priority=_extract_priority(text),
            )
            items.append(item)

    counts = {s: sum(1 for it in items if it.status == s) for s in ItemStatus}
    return TrackerFile(
        key=key,
        label=label,
        path=str(path.relative_to(BRAIN_ROOT)),
        items=items,
        total=len(items),
        pending=counts[ItemStatus.pending],
        in_progress=counts[ItemStatus.in_progress],
        done=counts[ItemStatus.done],
    )


def _get_all_trackers() -> List[TrackerFile]:
    config = _load_config()
    tracker_paths = config.get("trackers", {})
    result = []
    for key, rel_path in tracker_paths.items():
        abs_path = BRAIN_ROOT / rel_path
        result.append(parse_tracker_file(abs_path, key))
    return result


# ── Routes ────────────────────────────────────────────────────────────────────

@router.get("/", response_model=List[TrackerFile])
def list_trackers():
    """Return all tracker files with their parsed items."""
    return _get_all_trackers()


@router.get("/items", response_model=List[TrackerItem])
def list_all_items(
    status: Optional[ItemStatus] = Query(None),
    tracker: Optional[str] = Query(None),
    section: Optional[str] = Query(None),
):
    """Flat list of all items across all trackers, with optional filters."""
    trackers = _get_all_trackers()
    items = [item for t in trackers for item in t.items]
    if status:
        items = [i for i in items if i.status == status]
    if tracker:
        items = [i for i in items if i.tracker == tracker]
    if section:
        items = [i for i in items if i.section and section.lower() in i.section.lower()]
    return items


@router.get("/{tracker_key}", response_model=TrackerFile)
def get_tracker(tracker_key: str):
    """Return a single tracker file by key."""
    config = _load_config()
    tracker_paths = config.get("trackers", {})
    if tracker_key not in tracker_paths:
        raise HTTPException(status_code=404, detail=f"Tracker '{tracker_key}' not found")
    abs_path = BRAIN_ROOT / tracker_paths[tracker_key]
    return parse_tracker_file(abs_path, tracker_key)


@router.patch("/{tracker_key}/items/{item_id}", response_model=dict)
def update_item(tracker_key: str, item_id: str, body: UpdateItemRequest):
    """
    Update an item's status or text in the markdown file.
    Writes atomically to prevent corruption.
    """
    config = _load_config()
    tracker_paths = config.get("trackers", {})
    if tracker_key not in tracker_paths:
        raise HTTPException(status_code=404, detail=f"Tracker '{tracker_key}' not found")

    abs_path = BRAIN_ROOT / tracker_paths[tracker_key]
    if not abs_path.exists():
        raise HTTPException(status_code=404, detail="Tracker file not found on disk")

    tracker = parse_tracker_file(abs_path, tracker_key)
    target = next((i for i in tracker.items if i.id == item_id), None)
    if not target:
        raise HTTPException(status_code=404, detail=f"Item '{item_id}' not found")

    lines = abs_path.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
    line = lines[target.line_number]

    if body.status is not None:
        marker_map = {
            ItemStatus.pending: " ",
            ItemStatus.in_progress: "-",
            ItemStatus.done: "x",
        }
        line = re.sub(r"\[([x\-\s])\]", f"[{marker_map[body.status]}]", line, count=1, flags=re.IGNORECASE)

    if body.text is not None:
        line = re.sub(r"(\[([x\-\s])\]\s+).*", rf"\g<1>{body.text}", line, count=1, flags=re.IGNORECASE)

    lines[target.line_number] = line

    # Atomic write via temp file
    import tempfile, os
    tmp = abs_path.with_suffix(".tmp")
    try:
        tmp.write_text("".join(lines), encoding="utf-8")
        os.replace(tmp, abs_path)
    except Exception as e:
        tmp.unlink(missing_ok=True)
        raise HTTPException(status_code=500, detail=str(e))

    return {"ok": True, "item_id": item_id}
