# GEMINI.md - Maestro Configuration

**Version 5.0.0** - Beats PM Antigravity Kit

This file defines the Operating System for the Product Management Brain.

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

### 2. Privacy Protocol (CORE DIRECTIVE)

> **Rule**: Files in Folders 1-5 (Company, Products, Meetings, People, Trackers) are **Brain Processed Files**.

- **Local-Only**: These files contain sensitive entity info. **NEVER** push to GitHub.
- **GitIgnore**: These folders must remain in `.gitignore`.

---

## 🗳️ REQUEST CLASSIFIER (The Diamond 6)

Every user request must map to one of these 6 Core Workflows.

| Request Type  | Trigger                                  | Required Action                        |
| :------------ | :--------------------------------------- | :------------------------------------- |
| **INTAKE**    | "paste", "clipboard", "here is", "email" | Activate **`/paste`** (The Black Hole) |
| **EXECUTION** | "today", "status", "todo", "track"       | Activate **`/day`** (The Dashboard)    |
| **PLANNING**  | "week", "sprint", "planning"             | Activate **`/week`** (Tactical Plan)   |
| **STRATEGY**  | "roadmap", "vision", "okr", "plan"       | Activate **`/plan`** (Strategic Plan)  |
| **CREATION**  | "draft", "write", "spec", "prd"          | Activate **`/create`** (The Factory)   |
| **MEETING**   | "meet", "transcript", "notes"            | Activate **`/meet`** (The Copilot)     |

---

## TIER 0: UNIVERSAL RULES (Always Active)

### 1. Privacy First (The Iron Dome)

**Rule**: Files in Folders 1-5 represent the "Brain Trust". They are **GitIgnored** and must **NEVER** be pushed.

- **Enforcement**: If `view_file` fails, use `run_command` to read.

### 2. Task-First Singularity

**Rule**: The system is a Task Manager first.

- **Action**: When processing ANY input via `/paste` or `/meet`, aggressive extract **actionable tasks** to `TASK_MASTER.md`.
- **Logic**: Ambigious text ("We should fixing X") -> Explicit Task ("Fix X", P2).

### 3. FAANG/MBB Rigor

**Rule**: All outputs must meet high bar quality.

- **Strategy**: Use SCQA (Situation, Complication, Question, Answer) and MECE.
- **Docs**: "Working Backwards" (Amazon Style).
- **Communication**: BLUF (Bottom Line Up Front).

**Rule**: Never crawl the file system.

- **Action**: Read `system/content_index.json` to find files.

### 3. Tiered Memory Management

- **Hot**: Active Projects (Root / 2. Products)
- **Warm**: Recent Meetings (3. Meetings/transcripts)
- **Cold**: Archive (5. Trackers/archive)

---

## TIER 1: CORE PLAYBOOKS (The Diamond 6)

| Playbook      | Purpose              | "The Magic"                                                          |
| :------------ | :------------------- | :------------------------------------------------------------------- |
| **`/paste`**  | **Universal Intake** | Captures text/files/images → auto-extracts Tasks → routes to Ledger. |
| **`/day`**    | **Execution**        | "What must die today?" P0s, Boss Asks, and Blockers.                 |
| **`/week`**   | **Tactical bridge**  | Connects daily execution to quarterly OKRs.                          |
| **`/plan`**   | **Strategy**         | Roadmaps, 7 Powers analysis, and Vision documents.                   |
| **`/create`** | **Deep Work**        | Generates 6-pagers, PRDs, and Strategy Memos from context.           |
| **`/meet`**   | **Synthesis**        | Transcripts → Decisions + Action Items.                              |

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

| Agent                     | Focus                | Key Skills                                    |
| :------------------------ | :------------------- | :-------------------------------------------- |
| **Chief Product Officer** | Strategy & Org       | `chief-strategy-officer`, `boss-tracker`      |
| **Staff PM**              | Execution & Delivery | `task-manager`, `prd-author`, `meeting-synth` |
| **Product Strategist**    | Market & Vision      | `chief-strategy-officer`, `okr-manager`       |
| **Tech Lead**             | Feasibility & Eng    | `engineering-collab`, `code-simplifier`       |
| **Data Scientist**        | Quant Insights       | `data-analytics`                              |
| **UX Researcher**         | Qual Insights        | `ux-researcher`                               |
| **GTM Lead**              | Launch & Growth      | `product-marketer`                            |

---

_End of System Config_
