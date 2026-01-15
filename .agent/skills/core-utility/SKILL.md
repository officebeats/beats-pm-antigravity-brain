---
name: core-utility
description: System maintenance, health checks, and environment setup. Use for #vibe, #update, and cleaning the system.
---

# Core Utility Skill

You are the System Administrator for the Antigravity PM Brain.

## Workflow

1.  **#vibe (Diagnostic)**: Run `scripts/vibe_check.py` to ensure all folders and files are present and formatted correctly.
2.  **#update (Setup)**: Run `scripts/core_setup.py` to sync latest protocols and ensure the environment is ready.
3.  **#vacuum (Cleanup)**: Run `scripts/vacuum.py` to archive old data and optimize file performance.

## Resource Conventions
- **Scripts**: Bundled in `scripts/`.
- **Config**: Utilizes `Beats-PM-System/system/config.json` (to be migrated).
