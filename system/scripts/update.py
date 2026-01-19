"""
Update Script (Evolution Protocol)

orchestrates the system update process:
1. Git Pull (Update Code)
2. Core Setup (Verify Structure & Templates)
3. Migration Scan (Move files if architecture changed)
4. Vacuum (Clean up)
5. Vibe Check (Verify System Health)
"""

import sys
import subprocess
import os
from pathlib import Path

# Path setup
CURRENT_FILE = Path(__file__).resolve()
SYSTEM_ROOT = CURRENT_FILE.parent.parent      # system/
BRAIN_ROOT = SYSTEM_ROOT.parent               # brain/
SCRIPTS_DIR = SYSTEM_ROOT / "scripts"

# Add BRAIN_ROOT to path for imports
sys.path.insert(0, str(BRAIN_ROOT))

from system.utils.ui import print_cyan, print_success, print_error, print_warning

def run_step(description, command, cwd=None, ignore_error=False):
    """Run a shell command as a step."""
    print_cyan(f"\n🔄 {description}...")
    try:
        result = subprocess.run(
            command,
            cwd=cwd or str(BRAIN_ROOT),
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        print_success("Done.")
        return True
    except subprocess.CalledProcessError as e:
        if ignore_error:
            print_warning(f"Warning: {e.stderr}")
            return True
        else:
            print_error(f"Failed: {e.stderr}")
            return False

def git_update():
    """Pull latest changes from GitHub."""
    return run_step("Pulling latest code from GitHub", "git pull origin main")

def verify_structure():
    """Run core_setup.py to enforce directory structure and templates."""
    script_path = SCRIPTS_DIR / "core_setup.py"
    return run_step("Verifying System Structure", f'python "{script_path}" --headless')

def run_vacuum():
    """Run vacuum.py to clean up task lists and memory."""
    script_path = SCRIPTS_DIR / "vacuum.py"
    return run_step("Running System Vacuum", f'python "{script_path}"')

def vibe_check():
    """Run vibe_check.py to verify system health."""
    script_path = SCRIPTS_DIR / "vibe_check.py"
    return run_step("Final Vibe Check", f'python "{script_path}"')

def main():
    print_cyan("--- 🚀 System Update Protocol ---")
    
    # 1. GIT PULL
    if not git_update():
        print_error("Update aborted due to git error.")
        sys.exit(1)

    # 2. STRUCTURE & MIGRATION
    # core_setup.py handles directory creation and template updates.
    if not verify_structure():
        print_error("Structure verification failed.")
        sys.exit(1)

    # 3. VACUUM
    # Cleans up and performs Privacy Audit.
    if not run_vacuum():
        print_warning("Vacuum process had issues, but continuing...")

    # 4. VIBE CHECK
    if not vibe_check():
        print_warning("System Health Check flagged issues.")

    print_success("\n✅ System Update Complete. Ready for action.")

if __name__ == "__main__":
    main()
