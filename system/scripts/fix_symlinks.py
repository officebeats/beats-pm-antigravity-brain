#!/usr/bin/env python3
"""
Symlink Setup Script

Ensures all tool directories have properly configured symlinks to .agent/
This supports Gemini CLI, Claude Code, and Kilo Code.
"""
from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()
SYSTEM_ROOT = CURRENT_FILE.parent.parent
REPO_ROOT = SYSTEM_ROOT.parent
AGENT_DIR = REPO_ROOT / ".agent"

def fix_workflows_symlinks():
    """Fix workflows symlinks for all tools using absolute paths."""

    workflows_dir = AGENT_DIR / "workflows"

    tool_configs = {
        ".claude/commands": REPO_ROOT / ".claude" / "commands",
        ".kilocode/workflows": REPO_ROOT / ".kilocode" / "workflows",
        ".gemini/workflows": REPO_ROOT / ".gemini" / "workflows"
    }

    for target_path, link_path in tool_configs.items():
        if link_path.exists():
            if link_path.is_symlink():
                link_path.unlink()
            else:
                print(f"⚠️  {link_path} is not a symlink, skipping")
                continue

        link_path.symlink_to(workflows_dir, target_is_directory=True)
        print(f"✅ Created symlink: {link_path} -> {workflows_dir}")

if __name__ == "__main__":
    fix_workflows_symlinks()
