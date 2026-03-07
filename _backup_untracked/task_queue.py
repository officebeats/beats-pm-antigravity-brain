"""Background task queue for heavy operations."""

from __future__ import annotations

import json
import time
import traceback
from pathlib import Path
from typing import Any, Dict

import sys

# Path setup (MUST be before 'system.*' imports)
CURRENT_FILE = Path(__file__).resolve()
SYSTEM_ROOT = CURRENT_FILE.parent.parent
BRAIN_ROOT = SYSTEM_ROOT.parent
sys.path.insert(0, str(BRAIN_ROOT))

from system.utils.config import get_root_directory
from system.utils.ui import print_gray, print_cyan, print_error


class TaskQueue:
    def __init__(self) -> None:
        self.root = Path(get_root_directory())
        self.queue_dir = self.root / "system" / "queue"
        self.pending_dir = self.queue_dir / "pending"
        self.processing_dir = self.queue_dir / "processing"
        self.completed_dir = self.queue_dir / "completed"
        self.failed_dir = self.queue_dir / "failed"
        self._ensure_dirs()

    def _ensure_dirs(self) -> None:
        for d in [self.pending_dir, self.processing_dir, self.completed_dir, self.failed_dir]:
            d.mkdir(parents=True, exist_ok=True)

    def submit_job(self, job_type: str, payload: Dict[str, Any]) -> str:
        job = {
            "id": f"{int(time.time())}_{job_type}",
            "type": job_type,
            "timestamp": time.time(),
            "payload": payload,
        }
        job_file = self.pending_dir / f"{job['id']}.json"
        job_file.write_text(json.dumps(job, indent=2), encoding="utf-8")
        return job["id"]

    def _execute_job(self, data: Dict[str, Any]) -> None:
        job_type = data.get("type")
        if job_type == "structure_enforce":
            from system.scripts.enforce_structure import main as enforce

            enforce()
        elif job_type == "vacuum":
            from system.scripts.vacuum import main as vacuum

            vacuum()
        elif job_type == "gps_index":
            from system.scripts.gps_indexer import scan_files

            scan_files()
        else:
            raise ValueError(f"Unknown job type: {job_type}")

    def process_next(self) -> bool:
        files = sorted(list(self.pending_dir.glob("*.json")))
        if not files:
            return False

        job_file = files[0]
        processing_path = self.processing_dir / job_file.name

        try:
            job_file.rename(processing_path)
        except Exception:
            return False

        print_gray(f"[Background] Processing {job_file.name}...")
        try:
            data = json.loads(processing_path.read_text(encoding="utf-8"))
            self._execute_job(data)
            processing_path.rename(self.completed_dir / job_file.name)
        except Exception as exc:
            print_error(f"Job Failed: {exc}")
            processing_path.rename(self.failed_dir / job_file.name)
            (self.failed_dir / f"{job_file.name}.log").write_text(
                traceback.format_exc(), encoding="utf-8"
            )
        return True


def run_worker_daemon() -> None:
    queue = TaskQueue()
    print_cyan("⚡ Async Worker Started")
    while True:
        if not queue.process_next():
            time.sleep(2)


if __name__ == "__main__":
    run_worker_daemon()
