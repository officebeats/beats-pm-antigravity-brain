"""
Kilocode Skill Installer

This script installs the skills from this repository into the global `kilocode` CLI environment.
It creates symlinks (where possible) or copies the skills to the user's `.kilocode/skills` directory.
"""

import os
import sys
import shutil
import platform
from pathlib import Path

# Path setup
CURRENT_FILE = Path(__file__).resolve()
SYSTEM_ROOT = CURRENT_FILE.parent.parent      # system/
BRAIN_ROOT = SYSTEM_ROOT.parent               # brain/

# Add BRAIN_ROOT to path for imports
sys.path.insert(0, str(BRAIN_ROOT))

from system.utils.ui import print_cyan, print_green, print_yellow, print_error, print_success
from system.utils.filesystem import ensure_directory

def get_kilocode_config_dir():
    """
    Detect the global kilocode configuration directory.
    Defaults to ~/.kilocode
    """
    home = Path.home()
    default_path = home / ".kilocode"
    return default_path

def ask_yes_no(question, default='y'):
    """Ask a yes/no question."""
    choices = " [Y/n]" if default.lower() == 'y' else " [y/N]"
    response = input(f"{question}{choices}: ").strip().lower()
    if not response:
        return default.lower() == 'y'
    return response.startswith('y')

def install_skills(target_dir):
    """
    Install skills from .agent/skills to target_dir/skills.
    """
    source_skills_dir = BRAIN_ROOT / ".agent" / "skills"
    target_skills_dir = target_dir / "skills"

    if not source_skills_dir.exists():
        print_error(f"Source skills directory not found: {source_skills_dir}")
        return

    ensure_directory(target_skills_dir)
    print_cyan(f"\nInstalling skills to: {target_skills_dir}")

    count = 0
    for item in source_skills_dir.iterdir():
        if item.is_dir():
            skill_name = item.name
            target_skill_path = target_skills_dir / skill_name
            
            # Check if destination exists
            if target_skill_path.exists():
                print_yellow(f"  [skip] {skill_name} (Already exists)")
                continue

            try:
                # Try creating a symlink first
                try:
                    os.symlink(item, target_skill_path, target_is_directory=True)
                    print_success(f"  [link] {skill_name}")
                except OSError:
                    # Fallback to copy if symlinks fail (common on Windows without admin)
                    if platform.system() == "Windows":
                         # On Windows, we might need to copy if we can't symlink
                         print_yellow(f"  [copy] {skill_name} (Symlink failed, copying instead)")
                         shutil.copytree(item, target_skill_path)
                    else:
                         raise

                count += 1
            except Exception as e:
                print_error(f"  [fail] {skill_name}: {e}")

    print_green(f"\n✅ Installed {count} new skills.")

def main():
    print_cyan("\n🔌 Kilocode Skill Installer")
    print_cyan("===========================")

    kilocode_dir = get_kilocode_config_dir()
    
    print(f"Detected Kilocode configuration at: {kilocode_dir}")
    
    if not kilocode_dir.exists():
        print_yellow(f"Directory {kilocode_dir} does not exist.")
        if ask_yes_no("Create it?"):
            ensure_directory(kilocode_dir)
        else:
            print_error("Aborting installation.")
            return

    # specific check for skills directory
    target_skills = kilocode_dir / "skills"
    
    if not target_skills.exists():
         ensure_directory(target_skills)

    path_str = str(kilocode_dir)
    confirm = input(f"Install skills to {path_str}? [Enter to confirm, or type path]: ").strip()
    
    if confirm:
        target_path = Path(confirm)
        if not target_path.exists():
             print_yellow(f"Directory {target_path} does not exist.")
             if ask_yes_no("Create it?"):
                 ensure_directory(target_path)
             else:
                 print_error("Aborting.")
                 return
        kilocode_dir = target_path

    install_skills(kilocode_dir)
    
    print_cyan("\nRestart your Kilocode CLI/IDE to load new skills.")

if __name__ == "__main__":
    main()
