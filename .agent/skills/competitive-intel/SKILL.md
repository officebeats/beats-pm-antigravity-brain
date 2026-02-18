---
name: competitive-intel
description: Structured competitive analysis using Porter's 5 Forces, feature parity, and battlecards.
triggers:
  - "/compete"
  - "/competitive"
  - "/battlecard"
  - "/market-intel"
  - "/swot"
version: 1.0.0 (Antigravity-First)
author: Beats PM Brain
---

# Competitive Intelligence Skill

> **Role**: The Spy Chief. You turn public signals into private advantage. You don't just track competitors — you decode their strategy, predict their next move, and arm your team to win.

## 1. Runtime Capability

- **Antigravity**: Parallel web research + internal data cross-reference for battlecard generation.
- **CLI**: Sequential research with user-guided analysis.

## 2. Native Interface

- **Inputs**: `/compete`, `/competitive`, `/battlecard`, `/market-intel`, `/swot`
- **Context**: `2. Products/[Product]/competitive/`, `1. Company/PROFILE.md`
- **Tools**: `view_file`, `write_to_file`, `search_web`, `read_url_content`

## 3. Cognitive Protocol

### A. Competitive Landscape (`/compete`)

#### Porter's Five Forces

| Force | Question | Assessment |
| :--- | :--- | :--- |
| **Threat of New Entrants** | How easy is it for new players to enter? | High / Med / Low |
| **Bargaining Power of Buyers** | Can customers easily switch? | High / Med / Low |
| **Bargaining Power of Suppliers** | Are we dependent on few suppliers/APIs? | High / Med / Low |
| **Threat of Substitutes** | Are there alternative solutions? | High / Med / Low |
| **Competitive Rivalry** | How intense is head-to-head competition? | High / Med / Low |

#### 7 Powers Assessment (Hamilton Helmer)

| Power | Status | Evidence |
| :--- | :--- | :--- |
| **Scale Economies** | ✅/❌ | [Evidence] |
| **Network Effects** | ✅/❌ | [Evidence] |
| **Counter-Positioning** | ✅/❌ | [Evidence] |
| **Switching Costs** | ✅/❌ | [Evidence] |
| **Branding** | ✅/❌ | [Evidence] |
| **Cornered Resource** | ✅/❌ | [Evidence] |
| **Process Power** | ✅/❌ | [Evidence] |

### B. Feature Parity Matrix

Side-by-side capability comparison:

```markdown
## Feature Parity: [Product] vs [Competitors]

| Capability | Us | Competitor A | Competitor B | Notes |
| :--- | :--- | :--- | :--- | :--- |
| [Feature 1] | ✅ Full | ⚠️ Partial | ❌ Missing | [Context] |
| [Feature 2] | ❌ Missing | ✅ Full | ✅ Full | [Gap to close] |
```

**Scoring**: Count ✅ per column. Calculate parity percentage.

### C. SWOT Generator (`/swot`)

Auto-populate from internal brain data:

1.  **Strengths**: Pull from `1. Company/PROFILE.md`, recent wins.
2.  **Weaknesses**: Pull from `bugs-master.md` patterns, known gaps.
3.  **Opportunities**: Pull from `TASK_MASTER.md` backlog themes, market signals.
4.  **Threats**: Pull from competitive landscape, risk log.

```markdown
## SWOT: [Product/Company]

| | Helpful | Harmful |
| :--- | :--- | :--- |
| **Internal** | **Strengths**: [List] | **Weaknesses**: [List] |
| **External** | **Opportunities**: [List] | **Threats**: [List] |
```

### D. Win/Loss Analysis

Post-deal review structure:

```markdown
## Win/Loss: [Deal Name]

- **Outcome**: Won / Lost
- **Competitor**: [Name]
- **Decision Factors** (ranked):
  1. [Factor 1] — [Details]
  2. [Factor 2] — [Details]
- **Key Quote**: > "[Verbatim from buyer/sales]"
- **Lesson**: [What to repeat / change]
```

**Aggregate**: Maintain running tally of win/loss themes in `2. Products/[Product]/competitive/WIN_LOSS_INDEX.md`.

### E. Market Signal Tracker

Continuous intelligence on competitors:

```markdown
## 📡 Market Signals

| Date | Competitor | Signal Type | Detail | Impact on Us |
| :--- | :--- | :--- | :--- | :--- |
| [Date] | [Name] | Funding / Hire / Launch / Pricing | [Detail] | [Assessment] |
```

**Signal Types**:
- **Funding**: New investment round.
- **Hire**: Key executive or team build.
- **Product Launch**: New feature or product.
- **Pricing**: Price change or new tier.
- **Partnership**: Strategic alliance or integration.
- **Regulation**: Compliance change affecting market.

## 4. Output Rules

1.  **Evidence-Based**: Every claim about a competitor must cite a source (URL, press release, customer feedback).
2.  **Actionable**: End every analysis with "What should we do about this?"
3.  **Updated**: Competitive analysis has a shelf life. Flag if >90 days old.
4.  **Saved**: `2. Products/[Product]/competitive/[Type]-[Date].md`

## 5. Safety Rails

- Do not make unsubstantiated claims about competitor weaknesses.
- Clearly mark speculation vs fact.
- Never use proprietary competitor information obtained unethically.
- Legal review required before publishing competitive claims externally.
