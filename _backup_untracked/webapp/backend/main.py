"""
Beats PM Antigravity Brain — Companion Web App Backend
FastAPI server that reads local repo files and serves a REST API.

Run from webapp/backend/:
    uvicorn main:app --reload --port 8000
"""
import sys
from pathlib import Path

# Path bootstrap: ensure system.* imports work
CURRENT_FILE = Path(__file__).resolve()
BACKEND_ROOT = CURRENT_FILE.parent
WEBAPP_ROOT = BACKEND_ROOT.parent
BRAIN_ROOT = WEBAPP_ROOT.parent
sys.path.insert(0, str(BACKEND_ROOT))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from routers import trackers, files, search

app = FastAPI(
    title="Beats PM Brain API",
    description="Companion API for the Beats PM Antigravity Brain kit",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# CORS — allow Vite dev server and production build
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:4173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(trackers.router)
app.include_router(files.router)
app.include_router(search.router)


@app.get("/api/health")
def health():
    return {"status": "ok", "brain_root": str(BRAIN_ROOT)}


@app.get("/api/config")
def get_config():
    """Return the system config (non-sensitive fields only)."""
    import json
    config_path = BRAIN_ROOT / "system" / "config.json"
    if not config_path.exists():
        return JSONResponse(status_code=404, content={"detail": "system/config.json not found"})
    with open(config_path) as f:
        cfg = json.load(f)
    # Strip any sensitive keys if added in future
    return cfg
