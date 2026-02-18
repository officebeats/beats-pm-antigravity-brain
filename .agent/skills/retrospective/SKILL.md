---
name: retrospective
description: Facilitate sprint and PI retrospectives with structured formats and action tracking.
triggers:
  - "/retro"
  - "/retrospective"
  - "/postmortem"
  - "/reflect"
version: 1.0.0 (Antigravity-First)
author: Beats PM Brain
---

# Retrospective Skill

> **Role**: The Growth Engine. Retrospectives are not optional therapy sessions — they are the mechanism by which teams get better. You ensure every retro produces actions, every action is tracked, and patterns are spotted before they become crises.

## 1. Runtime Capability

- **Antigravity**: Parallel extraction of themes from input + cross-reference with previous retros.
- **CLI**: Guided facilitation prompts with sequential capture.

## 2. Native Interface

- **Inputs**: `/retro`, `/retrospective`, `/postmortem`
- **Context**: `3. Meetings/retros/`, `5. Trackers/TASK_MASTER.md`
- **Tools**: `view_file`, `write_to_file`, `grep_search`

## 3. Cognitive Protocol

### A. Format Selection

**Ask the user** which format to use. Recommend based on context:

| Format | Best For | Structure |
| :--- | :--- | :--- |
| **4Ls** | General sprint retros | Liked / Learned / Lacked / Longed For |
| **Start-Stop-Continue** | Quick tactical retros | Start doing / Stop doing / Keep doing |
| **Sailboat** | Vision-oriented teams | Wind (helps) / Anchor (holds back) / Rocks (risks) / Island (goal) |
| **Mad-Sad-Glad** | Emotionally charged sprints | What made you Mad / Sad / Glad |
| **5 Whys** | Incident postmortems | Root cause analysis chain |
| **Timeline** | Complex PI retros | Chronological event review |

### B. Facilitation Protocol

1.  **Set the Stage** (2 min):
    - Read sprint/PI summary from `5. Trackers/TASK_MASTER.md`.
    - State the Prime Directive: "Regardless of what we discover, we understand and truly believe that everyone did the best job they could, given what they knew at the time, their skills and abilities, the resources available, and the situation at hand."
2.  **Gather Data** (10 min):
    - Prompt for input in the chosen format.
    - If working from a transcript, auto-extract statements into categories.
3.  **Generate Insights** (5 min):
    - Group related items into themes.
    - Identify the top 3 themes by frequency/impact.
4.  **Decide What to Do** (5 min):
    - For each top theme, define exactly ONE action item.
    - Action items MUST have: Owner, Due Date, Definition of Done.
5.  **Close** (2 min):
    - Rate the retro (1-5 usefulness).
    - Reminder: "A retro without action items is just venting."

### C. Pattern Detection (Cross-Retro Analysis)

1.  **Scan**: Read previous retros from `3. Meetings/retros/`.
2.  **Detect**: Flag themes that appear in ≥2 consecutive retros.
3.  **Escalate**: Recurring themes get elevated to team-level systemic issues.
4.  **Output**:

```markdown
## 🔄 Recurring Patterns

| Theme | Occurrences | First Seen | Action Taken? |
| :--- | :--- | :--- | :--- |
| [Theme] | 3 retros | [Date] | ❌ Not addressed |
```

### D. Action Item Routing

All retro action items are automatically routed:
- **Task**: Append to `5. Trackers/TASK_MASTER.md` with tag `[RETRO]`.
- **Process Change**: Log to `5. Trackers/DECISION_LOG.md`.
- **Tool Request**: Route to `engineering-collab`.
- **People Issue**: Route to `stakeholder-mgr` (sensitive — no names in tracker).

### E. Improvement Velocity Tracker

Track whether retro actions actually get completed:

```markdown
## 📈 Retro Action Completion Rate

| Sprint/PI | Actions Generated | Actions Completed | Rate |
| :--- | :--- | :--- | :--- |
| Sprint 12 | 3 | 2 | 67% |
| Sprint 11 | 4 | 1 | 25% ← ⚠️ |
```

**Target**: ≥75% completion rate. Below 50% = escalate as systemic issue.

## 4. Output Format

### Sprint Retro

```markdown
# 🔄 Retrospective: [Sprint/PI Name]

> **Date**: [Date] | **Facilitator**: [Name] | **Format**: [4Ls/SSC/etc.]
> **Participants**: [List]

## 👍 [Category 1] (e.g., Liked / Start / Wind)
- [Item 1]
- [Item 2]

## 👎 [Category 2] (e.g., Lacked / Stop / Anchor)
- [Item 1]
- [Item 2]

## 💡 [Category 3] (e.g., Learned / Continue / Island)
- [Item 1]

## 🎯 Top Themes
1. **[Theme A]**: [1-sentence summary]
2. **[Theme B]**: [1-sentence summary]

## ✅ Action Items

| Action | Owner | Due | DoD | Status |
| :--- | :--- | :--- | :--- | :--- |
| [Action] | @name | [Date] | [Criteria] | 🟡 Open |
```

### Incident Postmortem (5 Whys)

```markdown
# 🔍 Postmortem: [Incident Title]

> **Date**: [Date] | **Severity**: [P0/P1] | **Duration**: [Time]

## Timeline
| Time | Event |
| :--- | :--- |
| [Time] | [What happened] |

## 5 Whys
1. Why? → [Answer]
2. Why? → [Answer]
3. Why? → [Answer]
4. Why? → [Answer]
5. Why? → **Root Cause**: [Answer]

## Action Items
[Same table as above]
```

## 5. Output Rules

1.  **Maximum 3 Action Items**: More than 3 = nothing gets done. Force prioritize.
2.  **No Blaming**: Frame issues as systemic, not personal.
3.  **Time-Boxed**: Retro itself should take ≤30 minutes.
4.  **Saved**: `3. Meetings/retros/YYYY-MM-DD_[Sprint/PI]_retro.md`

## 6. Safety Rails

- Never skip the action item step. A retro without actions is a waste.
- Flag if the same person owns >2 retro actions (overload risk).
- Anonymize sensitive team dynamics before saving to file.
- Require retro at least once per sprint/PI (flag if >3 weeks since last retro).
