"""Thin dispatcher for background jobs."""

from __future__ import annotations

from pathlib import Path
import sys

# Path setup (MUST be before 'system.*' imports)
CURRENT_FILE = Path(__file__).resolve()
SYSTEM_ROOT = CURRENT_FILE.parent.parent
BRAIN_ROOT = SYSTEM_ROOT.parent
sys.path.insert(0, str(BRAIN_ROOT))

from system.scripts.task_queue import TaskQueue

_queue_instance: TaskQueue | None = None


def get_queue() -> TaskQueue:
    global _queue_instance
    if _queue_instance is None:
        _queue_instance = TaskQueue()
    return _queue_instance


def submit(job_type: str, payload: dict) -> str:
    return get_queue().submit_job(job_type, payload)
