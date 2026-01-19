
import os
import sys
import unittest
import time
from pathlib import Path

# Setup Paths
CURRENT_FILE = Path(__file__).resolve()
SYSTEM_DIR = CURRENT_FILE.parent.parent
REPO_ROOT = SYSTEM_DIR.parent.parent
BEATS_PM_SYSTEM = REPO_ROOT / "Beats-PM-System"
DEBUG_LOG_DIR = BEATS_PM_SYSTEM / "debug_logs"

def setup_logging():
    """Ensure debug log directory exists and handle rotation (Max 2 files)."""
    if not DEBUG_LOG_DIR.exists():
        DEBUG_LOG_DIR.mkdir(parents=True)
        print(f"Created debug log directory: {DEBUG_LOG_DIR}")
        return

    # Get all log files
    files = sorted(DEBUG_LOG_DIR.glob("vacuum_debug_*.txt"), key=os.path.getmtime)
    
    # Keep max 1 existing file (so new one makes 2)
    MAX_LOGS = 2
    if len(files) >= MAX_LOGS:
        files_to_delete = files[:-(MAX_LOGS - 1)]
        for f in files_to_delete:
            try:
                f.unlink()
                print(f"Rotated (Deleted): {f.name}")
            except Exception as e:
                print(f"Failed to delete {f.name}: {e}")

def run_vacuum_debug():
    """Run vacuum tests and save output to new log file."""
    setup_logging()
    
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    log_file = DEBUG_LOG_DIR / f"vacuum_debug_{timestamp}.txt"
    
    print(f"Running Vacuum Debug... Logging to: {log_file}")
    
    # Redirect stdout/stderr to file
    with open(log_file, "w", encoding="utf-8") as f:
        # Capture both stream (runner) and prints
        class DualWriter:
            def __init__(self, file):
                self.file = file
                self.stdout = sys.stdout

            def write(self, message):
                self.file.write(message)
                self.stdout.write(message)
                self.file.flush()
                self.stdout.flush()

            def flush(self):
                self.file.flush()
                self.stdout.flush()

        original_stdout = sys.stdout
        original_stderr = sys.stderr
        
        sys.stdout = DualWriter(f)
        sys.stderr = DualWriter(f)
        
        try:
            # Run only test_vacuum.py
            loader = unittest.TestLoader()
            tests_dir = BEATS_PM_SYSTEM / "tests"
            suite = loader.discover(str(tests_dir), pattern='test_vacuum.py')
            
            runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
            result = runner.run(suite)
            
            if not result.wasSuccessful():
                print("\nVACUUM DEBUG FAILED.")
                sys.exit(1)
            else:
                print("\nVACUUM DEBUG PASSED.")
                
        finally:
            sys.stdout = original_stdout
            sys.stderr = original_stderr

if __name__ == "__main__":
    sys.path.insert(0, str(REPO_ROOT))
    run_vacuum_debug()
