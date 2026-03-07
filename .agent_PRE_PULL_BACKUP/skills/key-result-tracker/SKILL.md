---
name: key-result-tracker
description: Track OKRs and key results with owners, targets, and status.
triggers:
  - "/okr"
  - "/krs"
  - "/keyresults"
  - "/key-results"
version: 1.0.0 (Antigravity-First)
author: Beats PM Brain
---

# Key Result Tracker Skill

> **Role**: Make objectives measurable and keep key results on track with owners, baselines, and targets.

## 1. Runtime Capability

- **Antigravity**: Parallel extraction of objectives, baselines, targets, and owners.
- **CLI**: Sequential prompts for missing OKR fields.

## 2. Native Interface

- **Inputs**: `/okr`, `/krs`
- **Context**: `1. Company/`, `2. Products/`, `5. Trackers/`
- **Tools**: `view_file`, `write_to_file`

## 3. Cognitive Protocol

1. **Define Objective**: Short, qualitative statement.
2. **Define KRs**: 2–5 measurable outcomes with baselines and targets.
3. **Assign**: Owner + due date for each KR.
4. **Log**: Append to `5. Trackers/OKR_LOG.md` and link to the relevant product/company.

## 4. Output Format

```markdown
# OKR Update — [Date]

## Objective: [Statement]

| KR | Baseline | Target | Owner | Due | Status |
| :-- | :------- | :----- | :---- | :-- | :----- |
| KR1 | 10% | 25% | @name | YYYY-MM-DD | On Track |
```

## 5. Safety Rails

- Do not invent baselines or targets; ask once if missing.
- Ensure each KR is measurable and time-bound.
