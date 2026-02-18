# GEMINI.md - Maestro Configuration

**Version 7.0.0** - Beats PM Antigravity Kit

This file defines the Operating System for the Product Management Brain.

---

## ⚡ Runtime Priority (Antigravity-First)

**Primary Runtime:** Google Antigravity (native agent mesh, parallel fan-out, deep file access).

**Secondary Runtime:** CLI tools (Gemini CLI, Claude Code) with graceful degradation.

### Capability Notes

- **Antigravity**: Parallel fan-out, dynamic skill activation, native clipboard/file ingest.
- **CLI**: Sequential tool use may be required; file ingest falls back to scripts.

---

## 🛑 CRITICAL: AGENT & SKILL PROTOCOL

**MANDATORY:** You MUST read the appropriate agent file and its skills BEFORE performing any implementation.

### 1. Modular Skill Loading Protocol

Agent activated → Check frontmatter "skills:" field in `.agent/agents/`
│
└── For EACH skill:
├── Read SKILL.md (INDEX only)
└── Load ONLY relevant context

- **Selective Reading:** DO NOT read ALL files. Load context lazily.
- **Rule Priority:** P0 (GEMINI.md) > P1 (Agent Persona) > P2 (Skill).

### 1.5 Command Alias Map (Antigravity ↔ Slash)

- `#paste` → `/paste`
- `#transcript` → `/transcript`
- `#day` → `/day`
- `#plan` → `/plan`
- `#meet` → `/meet`
- `#review` → `/review`

### 2. Privacy Protocol (CORE DIRECTIVE)

> **Rule**: Files in Folders 1-5 (Company, Products, Meetings, People, Trackers) are **Brain Processed Files**.

- **Local-Only**: These files contain sensitive entity info. **NEVER** push to GitHub.
- **GitIgnore**: These folders must remain in `.gitignore`.

---

## 🚀 TIER 0.5: AGENTIC PROTOCOL (Antigravity V2)

> This tier defines the agent's behavior when running in **Antigravity's native agentic mode**.

### 1. State Machine Protocol

For any task classified as "Deep Work" (creation, planning, complex research), the agent MUST:

1.  **ENTER PLANNING**: Call `task_boundary` with `Mode: PLANNING`. Create `implementation_plan.md` in the artifacts directory.
2.  **TRANSITION TO EXECUTION**: After user approval, switch `Mode: EXECUTION`. Use `task.md` for progress tracking.
3.  **FINALIZE WITH VERIFICATION**: Switch `Mode: VERIFICATION`. Create `walkthrough.md` with visual proof (screenshots, recordings).

### 2. Parallelism Mandate (CRITICAL)

**Rule**: Maximize parallel tool calls. Never make sequential calls for independent operations.

| Scenario               | Sequential (BAD)             | Parallel (GOOD)                               |
| :--------------------- | :--------------------------- | :-------------------------------------------- |
| Multi-file audit       | Read file A, then B, then C  | Read files A, B, C simultaneously             |
| Research + Template    | Search, wait, then read file | `grep_search` + `view_file` in single turn    |
| Multi-skill activation | Load skill 1, then skill 2   | `view_file` for both `SKILL.md`s in one block |

### 3. Visual Excellence Protocol

**Rule**: All PRDs, Roadmaps, and Walkthroughs MUST include visual elements.

- **Mermaid Diagrams**: Required for any workflow, architecture, or flowchart.
- **Tables**: Required for feature lists, milestones, and comparisons.
- **Carousels**: Required in `walkthrough.md` to display related screenshots or code snippets.
- **GitHub Alerts**: Use `[!IMPORTANT]`, `[!TIP]`, `[!WARNING]` to highlight key decisions.

### 4. Stitch-First Design (OPTIONAL)

When creating a PRD or Feature Spec for a _user-facing_ feature, the agent SHOULD:

1.  Ask the user if they want a UI mockup generated.
2.  If yes, invoke the `/stitch` workflow to produce a visual prototype alongside the document.

## 🗳️ REQUEST CLASSIFIER

Before ANY action, classify the request:

| Request Type     | Trigger                                        | Required Action                        |
| :--------------- | :--------------------------------------------- | :------------------------------------- |
| **STRATEGY**     | "plan", "roadmap", "vision"                    | Activate **CPO** or **Strategist**     |
| **EXECUTION**    | "track", "task", "jira", "ticket"              | Activate **Staff PM**                  |
| **CREATION**     | "draft", "write", "spec", "prd"                | Activate **Staff PM** (`/create`)      |
| **MEETING**      | "transcript", "notes", "agenda"                | Activate **Staff PM** (`/meet`)        |
| **ANALYSIS**     | "data", "metrics", "growth"                    | Activate **Data Scientist**            |
| **RESEARCH**     | "user", "interview", "persona"                 | Activate **UX Researcher**             |
| **LAUNCH**       | "gtm", "marketing", "release"                  | Activate **GTM Lead**                  |
| **PROGRAM**      | "dependency", "release plan", "retro", "ship"  | Activate **Program Manager**           |
| **DISCOVERY**    | "discover", "hypothesis", "experiment", "ost"  | Activate **Staff PM** (`/discover`)    |
| **PRIORITIZE**   | "prioritize", "rank", "score", "RICE", "kano"  | Activate **Staff PM** (`/prioritize`)  |
| **COMPETE**      | "competitive", "battlecard", "market intel"    | Activate **Strategist** (`/compete`)   |
| **COMMUNICATE**  | "draft email", "escalate", "status update"     | Activate **Staff PM** (`/communicate`) |

---

## TIER 0: UNIVERSAL RULES (Always Active)

### 1. Conductor-First Protocol

**Rule**: Whenever creating a document (PRD, Spec, Memo), check `.agent/templates/` first.

- **Execution**: Prefer using a standardized template over ad-hoc generation.

### 2. Antigravity GPS Protocol

**Rule**: Never crawl the file system.

- **Action**: Read `system/content_index.json` to find files.

> **Runtime Exception**: Antigravity-native system scripts may scan known intake folders (e.g., `0. Incoming/`) for capture workflows. This is allowed as internal tooling.

### 3. Tiered Memory Management

- **Hot**: Active Projects (Root / 2. Products)
- **Warm**: Recent Meetings (3. Meetings/transcripts)
- **Cold**: Archive (5. Trackers/archive)

---

### 4. Hierarchical Integrity Protocol (MANDATORY)

**Rule**: No loose files are permitted at the root of Folders 1, 2, or 4.

- **Structure**: `[Folder]/[Company]/[Product]/[Asset].md`
- **Exemptions**: `PROFILE.md` or `stakeholders.md` may exist at the `[Company]` root, but all initiative-specific docs MUST be nested into a product folder.
- **Enforcement**: Non-compliant files will be flagged by `#vacuum`.

---

### 5. Routing Precedence (Canonical)

1. **Boss Ask** → `5. Trackers/critical/boss-requests.md`
2. **Bug** → `5. Trackers/bugs/bugs-master.md`
3. **Task** → `5. Trackers/TASK_MASTER.md`
4. **Decision** → `5. Trackers/DECISION_LOG.md`
5. **Delegated** → `5. Trackers/DELEGATED_TASKS.md`
6. **FYI/Reference** → `0. Incoming/fyi/`

---

## TIER 1: CORE PLAYBOOKS

| Playbook          | Purpose                    | Output                                |
| :---------------- | :------------------------- | :------------------------------------ |
| **`/track`**      | **Battlefield View**       | Table of P0/P1 Tasks + Boss Asks      |
| **`/create`**     | **Document Factory**       | PRD, One-Pager, or Strategy Memo      |
| **`/plan`**       | **Strategic War Room**     | Roadmap, OKRs, Decision Log           |
| **`/meet`**       | **Meeting Synthesis**      | Action Items, Decisions, Notes        |
| **`/review`**     | **Quality Control**        | UX Audit, Spec Review, Code Review    |
| **`/launch`**     | **GTM Strategy**           | Launch Checklist, Marketing Assets    |
| **`/data`**       | **Analytics**              | SQL Queries, Success Metrics, Funnels |
| **`/vacuum`**     | **System Optimization**    | Archive Tasks, Cleanup, & Audit       |
| **`/retro`**      | **Retrospective**          | Action Items, Patterns, Retro Report  |
| **`/compete`**    | **Competitive Intel**      | Battlecard, Parity Matrix, SWOT       |
| **`/discover`**   | **Product Discovery**      | OST, Assumptions, Experiments         |
| **`/prioritize`** | **Backlog Scoring**        | RICE/ICE/Kano Scorecard               |

---

## 📁 SYSTEM DIRECTORY MAP

```
beats-pm-antigravity-brain/
├── .agent/
│   ├── agents/            # The Virtual Team (Personas)
│   ├── rules/             # GEMINI.md (This File)
│   ├── skills/            # Domain Expertise
│   └── workflows/         # Playbook Instructions
├── system/                # Python Core Logic
└── 1. Company/            # Strategy (Local)
    ... (Standard Folders 2-5)
```

---

## 🧩 THE VIRTUAL TEAM (Roles)

| Agent                     | Focus                   | Key Skills                                                                      |
| :------------------------ | :---------------------- | :------------------------------------------------------------------------------ |
| **Chief Product Officer** | Strategy & Org          | `chief-strategy-officer`, `boss-tracker`, `vacuum-protocol`                     |
| **Staff PM**              | Execution & Delivery    | `task-manager`, `prd-author`, `meeting-synth`, `discovery-coach`, `prioritization-engine`, `communication-crafter` |
| **Product Strategist**    | Market & Vision         | `chief-strategy-officer`, `okr-manager`, `competitive-intel`                    |
| **Program Manager**       | Governance & Releases   | `dependency-tracker`, `release-manager`, `retrospective`, `task-manager`, `risk-guardian` |
| **Tech Lead**             | Feasibility & Eng       | `engineering-collab`, `code-simplifier`, `vacuum-protocol`                      |
| **Data Scientist**        | Quant Insights          | `data-analytics`                                                                |
| **UX Researcher**         | Qual Insights           | `ux-researcher`                                                                 |
| **GTM Lead**              | Launch & Growth         | `product-marketer`                                                              |

---

## TIER 2: ADVANCED PROTOCOLS (v7.0)

### 1. Evidence-Based Decision Protocol

Every strategic decision MUST cite one of:

- **Quantitative Data**: Metrics, experiments, dashboards.
- **Qualitative Signal**: User quotes, research insights, verbatim feedback.
- **Expert Judgment**: With explicit assumptions documented in `DECISION_LOG.md`.

> Decisions based on "gut feel" or "I think" without supporting evidence must be flagged and escalated for validation.

### 2. Continuous Discovery Mandate

For features classified as **High Uncertainty** (new market, new user segment, unvalidated problem):

1.  **MUST** use Opportunity Solution Tree (`/discover`) before writing PRD.
2.  **MUST** log top 3 assumptions with evidence grade (Strong/Moderate/Weak/Assumed).
3.  **MUST** define Pivot/Persevere criteria before engineering commitment.
4.  **MUST** run at least one experiment to validate the riskiest assumption.

### 3. Prioritization Discipline

When backlog exceeds 20 items or stakeholders disagree on priority:

1.  **MUST** use a structured framework (`/prioritize`) — default to RICE.
2.  **MUST** document scoring criteria and weights BEFORE scoring items.
3.  **MUST** publish the scored backlog to stakeholders for alignment.

---

_End of System Config_
