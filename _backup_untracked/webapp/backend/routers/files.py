"""
Files router — browse and read local repo files.
Uses system/content_index.json (GPS index) when available.
"""
import json
from pathlib import Path
from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import PlainTextResponse

router = APIRouter(prefix="/api/files", tags=["files"])

BRAIN_ROOT = Path(__file__).resolve().parents[3]

# Directories exposed to the browser (privacy: 1-5 folders are .gitignored but readable locally)
ALLOWED_ROOTS = [
    "0. Incoming",
    "1. Company",
    "2. Products",
    "3. Meetings",
    "4. People",
    "5. Trackers",
    "docs",
    "system",
    ".agent",
]

MAX_FILE_SIZE = 512 * 1024  # 512 KB


def _safe_path(rel: str) -> Path:
    """Resolve a relative path and ensure it stays within BRAIN_ROOT."""
    resolved = (BRAIN_ROOT / rel).resolve()
    if not str(resolved).startswith(str(BRAIN_ROOT.resolve())):
        raise HTTPException(status_code=403, detail="Path traversal not allowed")
    return resolved


@router.get("/tree")
def get_file_tree(root: Optional[str] = Query(None)):
    """Return a directory tree. If root is None, returns top-level allowed dirs."""
    if root is None:
        nodes = []
        for name in ALLOWED_ROOTS:
            p = BRAIN_ROOT / name
            if p.exists():
                nodes.append({
                    "name": name,
                    "path": name,
                    "type": "directory",
                    "children": None,
                })
        return nodes

    base = _safe_path(root)
    if not base.exists():
        raise HTTPException(status_code=404, detail="Path not found")

    def build_tree(p: Path, depth: int = 0):
        if depth > 4:
            return None
        rel = str(p.relative_to(BRAIN_ROOT)).replace("\\", "/")
        if p.is_file():
            return {"name": p.name, "path": rel, "type": "file", "size": p.stat().st_size}
        children = []
        try:
            entries = sorted(p.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
            for child in entries:
                if child.name.startswith(".") and child.name not in (".agent",):
                    continue
                node = build_tree(child, depth + 1)
                if node:
                    children.append(node)
        except PermissionError:
            pass
        return {"name": p.name, "path": rel, "type": "directory", "children": children}

    return build_tree(base)


@router.get("/content")
def get_file_content(path: str = Query(...)):
    """Return the text content of a file."""
    p = _safe_path(path)
    if not p.exists() or not p.is_file():
        raise HTTPException(status_code=404, detail="File not found")
    if p.stat().st_size > MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail="File too large (>512 KB)")
    try:
        content = p.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return PlainTextResponse(content)


@router.get("/index")
def get_content_index():
    """Return the GPS content index (system/content_index.json)."""
    index_path = BRAIN_ROOT / "system" / "content_index.json"
    if not index_path.exists():
        return {"entries": [], "generated_at": None, "note": "Run python system/scripts/gps_indexer.py to generate"}
    with open(index_path) as f:
        return json.load(f)
