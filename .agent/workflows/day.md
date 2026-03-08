---
description: Daily briefing and planning.
---

> **Compatibility Directive**: This component is optimized primarily for the Google Antigravity runtime, but gracefully degrades to support Gemini CLI, Claude Code, and Kilocode CLI.

### Daily Workflow

1. Activate `daily-synthesizer` with the `/day` trigger.
2. After the briefing is generated, trigger the `memory-consolidator` skill over the prior 24 hours of tasks, PRDs, and transcripts. Follow the output rules of the skill.

### Retro Workflow

7. **Save**: Write retro to `3. Meetings/retros/YYYY-MM-DD_[Sprint/PI]_retro.md`

8. **Memory Consolidation**:
   - Execute the `memory-consolidator` skill, feeding ALL prior retros from `3. Meetings/retros/` to identify cross-cutting, systemic issues that survived across multiple sprints.
   - Prepend these meta-insights to the `STRATEGIC_INSIGHTS.md` ledger.
