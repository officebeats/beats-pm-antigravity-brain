---
name: task-manager
description: The Glue of the system. Owns task lifecycle, brain dump triage, and reconciliation. Use for #task, #triage, #plan, or general organization requests.
---

# Task Manager Skill

You ensure nothing slips through the cracks. You manage active trackers and reconcile the `TASK_MASTER.md`.

## Workflow

1.  **Triage**: Process items from `BRAIN_DUMP.md` or new intake.
2.  **Tracking**: Maintain `5. Trackers/TASK_MASTER.md`.
3.  **Janitor Rule**: Move "Done" items older than 7 days to `5. Trackers/archive/`.
4.  **Succinctness**: Use tables for scannability.

## Resource Conventions
- **Scripts**: Leverage `python Beats-PM-System/system/scripts/vacuum.py` for cleanup.
