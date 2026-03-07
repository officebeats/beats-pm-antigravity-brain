"""
Search router — full-text search across tracker items and file index.
Uses simple substring + regex matching (Fuse.js handles fuzzy on the frontend).
"""
import re
from pathlib import Path
from typing import List, Optional
from fastapi import APIRouter, Query

from models.tracker import TrackerItem, ItemStatus
from routers.trackers import _get_all_trackers

router = APIRouter(prefix="/api/search", tags=["search"])

BRAIN_ROOT = Path(__file__).resolve().parents[3]


def _score(text: str, query: str) -> float:
    """Simple relevance score: exact match > word boundary > substring."""
    t, q = text.lower(), query.lower()
    if t == q:
        return 1.0
    if re.search(rf"\b{re.escape(q)}\b", t):
        return 0.8
    if q in t:
        return 0.5 + (len(q) / len(t)) * 0.3
    return 0.0


@router.get("/items")
def search_items(
    q: str = Query(..., min_length=1),
    status: Optional[ItemStatus] = Query(None),
    tracker: Optional[str] = Query(None),
    limit: int = Query(50, le=200),
):
    """Search tracker items by text query."""
    trackers = _get_all_trackers()
    items: List[TrackerItem] = [item for t in trackers for item in t.items]

    if status:
        items = [i for i in items if i.status == status]
    if tracker:
        items = [i for i in items if i.tracker == tracker]

    scored = []
    for item in items:
        search_text = f"{item.text} {item.section or ''} {item.tracker_label} {' '.join(item.tags)}"
        score = _score(search_text, q)
        if score > 0:
            scored.append({"item": item, "score": score, "matches": [item.text]})

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:limit]
