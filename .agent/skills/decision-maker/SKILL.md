---
name: decision-maker
description: The Executive Decider. Forces a structured decision-making process (Context > Options > Criteria > Decision) to prevent "waffling" and ensure accountability.
---

# Decision Maker (`#decide`)

**Purpose**: Create a rigid, immutable record of a product or strategic decision. Use this when the user is weighing options for a complex problem.

## 🧠 Brain Logic

1.  **Trigger**:
    - Command: `#decide` or `/decide`
    - Intent: "Help me choose between X and Y" or "Document this decision."

2.  **Context Resolution**:
    - Check `KERNEL.md` and `SETTINGS.md` for current Priorities and OKRs to align decision criteria.
    - Check `5. Trackers/DECISION_LOG.md` for precedence (previous similar decisions).

3.  **Core Process (The "Decision Diamond")**:
    - **Step 1: Frame the Problem**. What are we solving? Why now?
    - **Step 2: Identify Options**. Divergent thinking. List at least 3 distinct paths (including "Do Nothing").
    - **Step 3: Define Criteria**. How will we judge? (e.g., Velocity vs. Quality, Cost vs. Scale).
    - **Step 4: The Decision**. Convergent thinking. Pick one.
    - **Step 5: The "Why" (Justification)**. Defend the choice against the rejected options.
    - **Step 6: Pre-Mortem**. What will go wrong?

## 📝 Output Formats

### 1. The Decision Log Entry (Append to `5. Trackers/DECISION_LOG.md`)

```markdown
## [YYYY-MM-DD] [Title of Decision]

**Context**: [Brief 1-line summary of the problem]
**Owner**: [User Name] | **Status**: [DECIDED]

### ⚖️ Options Considered

1. **[Option A]**: [Pros/Cons]
2. **[Option B]**: [Pros/Cons]
3. **[Option C]**: [Pros/Cons]

### 🏆 The Verdict

**Decision**: [Option Selected]
**Rationale**: We chose [Option] because [Primary Driver]. We traded off [Trade-off] to gain [Benefit].

### 🔮 Pre-Mortem & Risks

- [Risk 1]: [Mitigation]
```

### 2. Daisy-Chain Handoff

If this skill is chained (e.g., `#decide -> #task`), output the following manifesto line:
`[OUTPUT_MANIFEST]: {"decision_log": "5. Trackers/DECISION_LOG.md", "decision_context": "[Summary String]"}`

## ⚙️ Execution Rules

- **Zero Ambiguity**: Do not let the user end with "we'll see." Force a stance.
- **Link to OKRs**: Explicitly mention which OKR this decision supports if applicable.
- **File Anchor**: Ensure `5. Trackers/DECISION_LOG.md` exists. If not, create it.
