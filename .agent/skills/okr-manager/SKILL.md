---
name: okr-manager
description: The Strategy Executor. Manages the hierarchy of Annual Goals -> Quarterly Objectives -> Weekly Key Results to ensure alignment.
---

# OKR Manager (`#okr`)

**Purpose**: Translate high-level strategy into verifiable weekly outcomes.

## 🧠 Brain Logic

1.  **Trigger**:
    - Command: `#okr` or `/okr`
    - Intent: "Draft OKRs", "Update Goals", "Check alignment".

2.  **Context Resolution**:
    - **Input**: specific strategy documents (e.g., `1. Company/STRATEGY_2026.md`) or previous OKRs.
    - **Reference**: `SETTINGS.md` for "North Star" or "Mission".

3.  **Core Process (The Cascade)**:
    - **Level 1: Annual** (The Mission). What is the one thing we must achieve this year?
    - **Level 2: Quarterly** (The Objectives). 3-5 Qualitative Goals.
    - **Level 3: Key Results** (The Metrics). 3-5 Quantitative Measures per Objective. Must be numeric (0.0 -> 1.0).

## 📝 Output Formats

### 1. The Strategy File (`1. Company/OKRs/FY[Year]-Q[Quarter].md`)

```markdown
# FY2026 Q1 OKRs: [Theme Name]

> **Theme**: [e.g., "Operational Velocity"]
> **Status**: [DRAFT/FINAL]

## 🎯 Objective 1: [Inspirational qualitative goal]

- [ ] **KR 1.1**: Increase [Metric] from X to Y. (Confidence: 8/10)
- [ ] **KR 1.2**: Ship [Feature] with < 5 bugs.
- [ ] **KR 1.3**: Achieve [Outcome].

## 🎯 Objective 2: ...
```

### 2. Daisy-Chain Handoff

If chained (e.g., `#okr -> #task`), output:
`[OUTPUT_MANIFEST]: {"okr_file": "1. Company/OKRs/FY[Year]-Q[Quarter].md", "objectives": ["Obj 1", "Obj 2"]}`

## ⚙️ Execution Rules

- **Formula**: All KRs must follow "Measured by [Metric] changing from [X] to [Y]".
- **Limit**: Max 5 Objectives. Max 4 KRs per Objective. Focus is key.
- **Auto-Directory**: Create `1. Company/OKRs/` if missing.
