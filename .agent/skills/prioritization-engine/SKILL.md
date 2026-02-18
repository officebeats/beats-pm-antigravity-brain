---
name: prioritization-engine
description: Score and rank backlogs using RICE, ICE, MoSCoW, Kano, and weighted scoring.
triggers:
  - "/prioritize"
  - "/rank"
  - "/score"
  - "/rice"
  - "/kano"
version: 1.0.0 (Antigravity-First)
author: Beats PM Brain
---

# Prioritization Engine Skill

> **Role**: The Tiebreaker. When everything is "P0", you bring quantitative rigor. You replace gut-feel prioritization with structured, defensible frameworks that stakeholders can align on.

## 1. Runtime Capability

- **Antigravity**: Parallel scoring across multiple frameworks; generate comparison table in one turn.
- **CLI**: Sequential item-by-item scoring with user input.

## 2. Native Interface

- **Inputs**: `/prioritize`, `/rank`, `/score`, `/rice`, `/kano`
- **Context**: `5. Trackers/TASK_MASTER.md`, `2. Products/[Product]/`, `SETTINGS.md`
- **Tools**: `view_file`, `write_to_file`

## 3. Cognitive Protocol

### A. Framework Selection

**Rule**: Always ask which framework to use unless the user specifies. Recommend based on context:

| Context | Recommended Framework |
| :--- | :--- |
| Backlog with mixed features/bugs | **RICE** |
| Quick triage, small team | **ICE** |
| Stakeholder alignment needed | **MoSCoW** |
| Customer-facing feature roadmap | **Kano** |
| Strategic initiative ranking | **Weighted Scoring** |
| Opportunity assessment | **Opportunity Scoring (Ulwick)** |

### B. RICE Scoring (`/rice`)

Score each item on 4 dimensions:

| Dimension | Scale | Definition |
| :--- | :--- | :--- |
| **Reach** | # users/quarter | How many users will this impact in a quarter? |
| **Impact** | 0.25 / 0.5 / 1 / 2 / 3 | Minimal / Low / Medium / High / Massive |
| **Confidence** | 50% / 80% / 100% | How sure are we? (Data > Anecdote > Gut) |
| **Effort** | Person-months | How much work is this? |

**Formula**: `RICE Score = (Reach × Impact × Confidence) / Effort`

**Output Table**:
```markdown
| Rank | Initiative | Reach | Impact | Confidence | Effort | RICE Score |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | [Name] | 5000 | 2 | 80% | 3 | 2667 |
```

### C. ICE Scoring

Lighter-weight alternative for quick triage:

| Dimension | Scale (1-10) |
| :--- | :--- |
| **Impact** | How much will this move our target metric? |
| **Confidence** | How sure are we of the impact? |
| **Ease** | How easy is this to implement? |

**Formula**: `ICE Score = Impact × Confidence × Ease`

### D. MoSCoW Classification

For stakeholder alignment and scope negotiation:

| Category | Definition | Rule |
| :--- | :--- | :--- |
| **Must Have** | Non-negotiable. Ship fails without it. | ≤60% of capacity |
| **Should Have** | Important but not fatal if missing. | ~20% of capacity |
| **Could Have** | Nice-to-have. Only if time permits. | ~20% of capacity |
| **Won't Have** | Explicitly out of scope this cycle. | Documented for future |

**Validation**: If "Must Haves" exceed 60% of estimated capacity, force the user to re-negotiate scope.

### E. Kano Model

Classify features by customer response:

| Category | Definition | Example |
| :--- | :--- | :--- |
| **Must-Be** | Expected. Absence = dissatisfaction. | Login works. |
| **Performance** | More is better. Linear satisfaction. | Faster load times. |
| **Attractive** | Unexpected delight. Absence ≠ dissatisfaction. | AI autocomplete. |
| **Indifferent** | No impact on satisfaction. | Backend refactor. |
| **Reverse** | Presence = dissatisfaction for some users. | Forced tutorials. |

**Method**: Survey or heuristic classification. Plot on Kano diagram.

### F. Weighted Scoring Model

For strategic decisions with custom criteria:

1.  **Define Criteria**: 3-5 dimensions (e.g., Revenue Impact, Strategic Alignment, Customer Demand, Technical Feasibility, Time to Market).
2.  **Assign Weights**: Sum to 100%. Get stakeholder agreement on weights BEFORE scoring.
3.  **Score**: Each item 1-5 per criterion.
4.  **Calculate**: Weighted sum.

```markdown
| Initiative | Revenue (30%) | Strategy (25%) | Demand (20%) | Feasibility (15%) | Speed (10%) | Total |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [Name] | 4 (1.2) | 5 (1.25) | 3 (0.6) | 4 (0.6) | 3 (0.3) | 3.95 |
```

### G. Opportunity Scoring (Ulwick)

Based on Outcome-Driven Innovation:

1.  **List Outcomes**: What the customer is trying to achieve.
2.  **Survey**: Importance (1-10) and Satisfaction (1-10).
3.  **Formula**: `Opportunity = Importance + max(Importance - Satisfaction, 0)`
4.  **Target**: High Importance, Low Satisfaction = underserved opportunities.

## 4. Stack Rank Protocol

After scoring, generate a force-ranked list:

1.  **Sort** by score (highest first).
2.  **Justify**: For each adjacent pair, explain why #N ranks above #N+1.
3.  **Capacity Check**: Draw a "cut line" based on available resources.
4.  **Publish**: Save to `2. Products/[Product]/backlog-score.md` or append to `TASK_MASTER.md`.

## 5. Output Rules

1.  **Show Your Work**: Always display the scoring table, never just the final rank.
2.  **Stakeholder Ready**: Output should be presentable in a planning meeting.
3.  **Versioned**: Include date and participants in the scoring session header.
4.  **Link to Source**: Every scored item links to its TASK_MASTER or PRD entry.

## 6. Safety Rails

- Never let one person score alone. Flag if <2 scorers participated.
- Recalibrate if all scores cluster (indicates poor differentiation).
- Re-score quarterly or when market conditions change significantly.
