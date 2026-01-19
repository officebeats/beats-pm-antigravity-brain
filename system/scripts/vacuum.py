"""
Vacuum Script (Centrifuge Protocol)

Archives completed tasks and manages the Tiered Memory System (Hot/Warm/Cold).
Optimized for speed and long-term retrieval.
"""

import sys
import time
from datetime import datetime
from pathlib import Path
from typing import List, Tuple

# Path setup
CURRENT_FILE = Path(__file__).resolve()
SYSTEM_ROOT = CURRENT_FILE.parent.parent  # system/
BRAIN_ROOT = SYSTEM_ROOT.parent           # brain root/

# Add BRAIN_ROOT to path for 'system.*' imports
sys.path.insert(0, str(BRAIN_ROOT))

# Configuration
TRACKERS_DIR = BRAIN_ROOT / "5. Trackers"
ARCHIVE_DIR = TRACKERS_DIR / "archive"
MEETINGS_DIR = BRAIN_ROOT / "3. Meetings"

# Time Constants
AGE_HOT_limit = 30 * 24 * 60 * 60  # 30 days
AGE_WARM_limit = 365 * 24 * 60 * 60  # 1 year

def ensure_dirs():
    """Ensure all tiered memory directories exist."""
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    (MEETINGS_DIR / "transcripts").mkdir(parents=True, exist_ok=True)
    (MEETINGS_DIR / "summaries").mkdir(parents=True, exist_ok=True)
    (MEETINGS_DIR / "archive").mkdir(parents=True, exist_ok=True)

def update_index(entry: str, category: str):
    """Append a retrievable entry to the Global Archive Index."""
    index_file = ARCHIVE_DIR / "INDEX.md"
    timestamp = datetime.now().strftime("%Y-%m-%d")
    
    if not index_file.exists():
        with open(index_file, "w", encoding="utf-8") as f:
            f.write("# Global Archive Index\n\n| Date | Category | Summary | Location |\n|---|---|---|---|\n")
            
    row = f"| {timestamp} | {category} | {entry} | `archive/` |\n"
    
    with open(index_file, "a", encoding="utf-8") as f:
        f.write(row)

def vacuum_tracker(filename: str) -> int:
    """
    Move completed items to a yearly archive file.
    Returns count of moved items.
    """
    filepath = TRACKERS_DIR / filename
    if not filepath.exists():
        return 0

    print(f"  Scanning {filename}...", end=" ")
    
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    active = []
    completed = []

    for line in lines:
        if line.strip().startswith("- [x]"):
            completed.append(line)
        else:
            active.append(line)

    if not completed:
        print("Clean.")
        return 0

    # Write Active
    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(active)

    # Appending to Yearly Archive
    year = datetime.now().year
    archive_file = ARCHIVE_DIR / f"archive_{year}_{filename}"
    
    header = f"\n\n### Vacuumed on {datetime.now().strftime('%Y-%m-%d')}\n"
    
    with open(archive_file, "a", encoding="utf-8") as f:
        f.write(header)
        f.writelines(completed)

    print(f"Moved {len(completed)} items to {archive_file.name}")
    
    # Update Index with a summary
    summary = f"Archived {len(completed)} items from {filename}"
    update_index(summary, "Tracker")
    
    return len(completed)

def manage_tiered_memory():
    """
    Migrate files through Hot -> Warm -> Cold tiers.
    Hot: < 30 days (Transcripts folder)
    Warm: 30-365 days (Summaries folder, stripped of heavy raw text)
    Cold: > 1 year (Archive folder)
    """
    print("\nRunning Tiered Memory Migration...")
    
    transcripts_dir = MEETINGS_DIR / "transcripts"
    summaries_dir = MEETINGS_DIR / "summaries"
    archive_dir = MEETINGS_DIR / "archive"
    
    now = time.time()
    moved_warm = 0
    moved_cold = 0

    # 1. Hot -> Warm
    for file in transcripts_dir.glob("*.md"):
        age = now - file.stat().st_mtime
        if age > AGE_HOT_limit:
            # Move to Warm
            # Ideally, we would compress/summarize here. 
            # For speed, we just move it for now, but a sophisticated skill would replace it with a summary.
            dest = summaries_dir / file.name
            file.rename(dest)
            moved_warm += 1
            update_index(f"Migrated to Warm: {file.name}", "Memory")

    # 2. Warm -> Cold
    for file in summaries_dir.glob("*.md"):
        age = now - file.stat().st_mtime
        if age > AGE_WARM_limit:
            dest = archive_dir / file.name
            file.rename(dest)
            moved_cold += 1
            update_index(f"Migrated to Cold: {file.name}", "Memory")

    if moved_warm or moved_cold:
        print(f"  Hot -> Warm: {moved_warm} files")
        print(f"  Warm -> Cold: {moved_cold} files")
    else:
        print("  Memory Tiers are balanced.")

from system.scripts import kernel_utils
import subprocess
import os

def check_system_access():
    """
    Validation: Ensure the System (Python) can access the GitIgnored "Dark Matter".
    """
    print("\n👁️  System Vision Check...")
    
    sensitive_roots = [
        "1. Company",
        "2. Products",
        "3. Meetings", 
        "4. People", 
        "5. Trackers"
    ]
    
    accessible_count = 0
    total_checked = 0
    
    for folder in sensitive_roots:
        path = BRAIN_ROOT / folder
        # Only check existence if we expect it (though these are required folders)
        if path.exists():
            total_checked += 1
            # Check read AND write access
            if os.access(path, os.R_OK) and os.access(path, os.W_OK):
                 accessible_count += 1
            else:
                 print(f"  🛑 Restricted Permissions: {folder}")
        else:
             print(f"  ⚠️ Missing Directory: {folder}")
             
    if accessible_count == total_checked and total_checked > 0:
        print(f"  ✅ System has full Read/Write access to all {accessible_count} private folders.")
    elif total_checked == 0:
        print("  ⚠️ No private folders found to check.")
    else:
        print(f"  ⚠️ System has access to {accessible_count}/{total_checked} folders.")

def check_git_safety():
    """
    Privacy Audit: Ensure no sensitive Brain files are being verified by Git.
    """
    print("\n🔒 Privacy Check...")
    
    # 1. Ask Git what it is tracking or seeing
    try:
        # Check staged and untracked files
        result = subprocess.run(
            ["git", "status", "--porcelain"], 
            capture_output=True, 
            text=True, 
            cwd=str(BRAIN_ROOT)
        )
        if result.returncode != 0:
            print("  ⚠️ Git check failed (is this a git repo?). Skipping.")
            return

        files = []
        for line in result.stdout.splitlines():
            # "M  file.ext" -> "file.ext"
            # "?? file.ext" -> "file.ext"
            parts = line.strip().split(" ", 1)
            if len(parts) > 1:
                files.append(parts[1])
                
        # 2. Audit against Kernel Rules
        passed, violations = kernel_utils.check_privacy_rule(files)
        
        if passed:
            print("  ✅ All sensitive files are successfully ignored.")
        else:
            print(f"  🛑 WARNING: Found {len(violations)} sensitive files visible to Git!")
            for v in violations:
                print(f"     - {v}")
            print("  ACTION: These files should be ignored via .gitignore.")

    except Exception as e:
        print(f"  ⚠️ Could not run git check: {e}")

def main():
    ensure_dirs()
    print("--- 🧹 System Vacuum Protocol ---")
    
    # Vaccum Trackers
    targets = ["tasks.md", "bugs-master.md", "boss-requests.md", "TASK_MASTER.md"]
    total_cleaned = 0
    for t in targets:
        total_cleaned += vacuum_tracker(t)
        
    # Manage Memory Tiers
    manage_tiered_memory()

    # Privacy & Access Checks
    check_system_access()
    check_git_safety()
    
    print("\n✅ Optimization Complete.")

if __name__ == "__main__":
    main()

