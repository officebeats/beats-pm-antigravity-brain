"""Performance benchmarks for Antigravity core scripts."""

from __future__ import annotations

import time
from pathlib import Path
import sys

# Path setup (MUST be before 'system.*' imports)
CURRENT_FILE = Path(__file__).resolve()
SYSTEM_ROOT = CURRENT_FILE.parent.parent
BRAIN_ROOT = SYSTEM_ROOT.parent
sys.path.insert(0, str(BRAIN_ROOT))

from system.scripts import gps_indexer
from system.utils.ui import print_cyan, print_success


def benchmark_gps() -> float:
    start_time = time.perf_counter()
    gps_indexer.scan_files()
    duration = time.perf_counter() - start_time
    print_success(f"GPS Indexer Duration: {duration:.4f}s")
    return duration


def main() -> None:
    print_cyan("\n⚡ Performance Benchmarks")
    benchmark_gps()


if __name__ == "__main__":
    main()
