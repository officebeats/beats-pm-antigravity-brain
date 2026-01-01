# Regression Test Suite: Neural Mesh v1.3.0

This suite defines standardized test scenarios for the Antigravity Brain agents to ensure orchestration, routing, and artifact generation remain consistent across structural changes.

---

## 🏎️ Execution Protocol

1. **Reset**: Ensure `00-DROP-FILES-HERE-00/` is clear.
2. **Inject**: Provide the "Input Signal" to Antigravity.
3. **Validate**: Check the "Expected Outcome" (Artifacts created, correct folders, context preservation).
4. **Mesh Check**: Verify if secondary agents were correctly triggered.

---

## 🛠️ Agent Test Scenarios

### 1. Requirements Translator (The Router)

| ID        | Title        | Input Signal                                                     | Expected Outcome                                                           |
| :-------- | :----------- | :--------------------------------------------------------------- | :------------------------------------------------------------------------- |
| **RT-01** | Direct Cmd   | `#bug login is slow`                                             | Entry added to `tracking/bugs/bugs-master.md`.                             |
| **RT-02** | Multi-Intent | `The boss wants a new dashboard and the checkout button is red.` | Routes to **Boss Tracker** AND **UX Collaborator**.                        |
| **RT-03** | File Ref     | `Review the roadmap in Roadmap.xlsx #strategy`                   | Executes `capture-clipboard.ps1` (if #paste used) or reads from drop zone. |

### 2. Boss Tracker (The Executive)

| ID        | Title         | Input Signal                             | Expected Outcome                                                         |
| :-------- | :------------ | :--------------------------------------- | :----------------------------------------------------------------------- |
| **BT-01** | High Priority | `#boss we need the Q1 budget by Friday.` | Added to `tracking/critical/boss-requests.md` with 🔥 Priority.          |
| **BT-02** | Fuzzy Match   | `Ricky asked for the deck.`              | Resolves "Ricky" to "Ricardo Regalado" (from SETTINGS) and logs request. |
| **BT-03** | Auto-Escalate | (Audit) Item with 48h no update.         | `#day` brief flags item as `🟠 Stale`.                                   |

### 3. Bug Chaser (The Quality Guard)

| ID        | Title      | Input Signal                     | Expected Outcome                                                                  |
| :-------- | :--------- | :------------------------------- | :-------------------------------------------------------------------------------- |
| **BC-01** | Direct Log | `Bug: 404 on profile page.`      | Logged in `tracking/bugs/bugs-master.md` with auto-product detection.             |
| **BC-02** | Visual Bug | `#screenshot` of a crash screen. | **Visual Processor** hands off to **Bug Chaser**; logs with "Source: Screenshot". |
| **BC-03** | SLA Check  | `#status` check.                 | Correctly classifies bug as 🔥 Critical or ⚡ Now based on date.                  |

### 4. Visual Processor (The Eyes)

| ID        | Title       | Input Signal                                    | Expected Outcome                                              |
| :-------- | :---------- | :---------------------------------------------- | :------------------------------------------------------------ |
| **VP-01** | OCR Routing | Screenshot of a Slack message from the Boss.    | Extracts text and routes to **Boss Tracker**.                 |
| **VP-02** | UI Feedback | Screenshot of a mockup with "Too blue".         | Extracts "Too blue" and routes to **UX Collaborator**.        |
| **VP-03** | Batch Paste | 3 screenshots of different errors + `#process`. | Identifies 3 distinct bugs and logs them to `tracking/bugs/`. |

### 5. Task Manager (The State)

| ID        | Title         | Input Signal                           | Expected Outcome                                                       |
| :-------- | :------------ | :------------------------------------- | :--------------------------------------------------------------------- |
| **TM-01** | Deduplication | `Email the team` (twice).              | Detects >80% similarity; appends context instead of creating new task. |
| **TM-02** | Brain Dump    | `I'm thinking about a space elevator.` | Logs to `BRAIN_DUMP.md` (no immediate action).                         |
| **TM-03** | Triage        | `#day` with pending items in dump.     | Moves actionable items from dump to `ACTION_PLAN.md`.                  |

### 6. Meeting Synthesizer (The Ear)

| ID        | Title       | Input Signal                           | Expected Outcome                                                    |
| :-------- | :---------- | :------------------------------------- | :------------------------------------------------------------------ |
| **MS-01** | Standup     | Paste 5 lines of standup notes.        | Updates individual progress in `tracking/people/`.                  |
| **MS-02** | 1:1 Capture | `#1on1` notes with manager.            | Extracts feedback and adds to `tracking/critical/boss-requests.md`. |
| **MS-03** | Transcript  | Full transcript of a feature kick-off. | Creates a new feature doc in `tracking/feedback/feature-requests/`. |

### 7. Strategy Synthesizer (The Brain)

| ID        | Title       | Input Signal                                 | Expected Outcome                                                          |
| :-------- | :---------- | :------------------------------------------- | :------------------------------------------------------------------------ |
| **SS-01** | Pattern Map | 3 different bugs in the "Payments" module.   | Identifies "Payment Hotspot" and logs to `tracking/strategy/patterns.md`. |
| **SS-02** | Opp Card    | `Market research says users love dark mode.` | Creates `tracking/strategy/opportunities/OPP-dark-mode.md`.               |
| **SS-03** | Competitive | `#strategy competitor X just launched Y.`    | Updates competitive landscape in `vault/research/competitors.md`.         |

### 8. Stakeholder Manager (The diplomat)

| ID        | Title         | Input Signal                                 | Expected Outcome                                                |
| :-------- | :------------ | :------------------------------------------- | :-------------------------------------------------------------- |
| **SH-01** | Update Ask    | `What's the status of the API for Mark?`     | Scans trackers and drafts an update in `system/inbox/drafts/`.  |
| **SH-02** | Feedback Loop | `Stakeholder Sarah says she hates the font.` | Logs feedback to `tracking/people/stakeholders.md` under Sarah. |
| **SH-03** | Cadence Check | `#weekly` review.                            | Flags stakeholders who haven't heard from you in 1 week.        |

### 9. Engineering Collaborator (The Architect)

| ID        | Title       | Input Signal                                | Expected Outcome                                                          |
| :-------- | :---------- | :------------------------------------------ | :------------------------------------------------------------------------ |
| **EC-01** | Tech Spike  | `We need to research GraphQL.`              | Creates a Spike artifact in `tracking/people/engineering-items.md`.       |
| **EC-02** | ADR         | `We are choosing AWS over Azure because...` | Creates Architecture Decision Record (ADR) in `vault/data/architecture/`. |
| **EC-03** | Code Review | `#eng review this PR logic [paste code].`   | Analyzes for logic errors and logs findings.                              |

### 10. UX Collaborator (The Designer)

| ID        | Title         | Input Signal                                          | Expected Outcome                                 |
| :-------- | :------------ | :---------------------------------------------------- | :----------------------------------------------- |
| **UC-01** | Wireframe     | `#ux new wireframe for settings [link].`              | Logs to `tracking/people/ux-tasks.md`.           |
| **UC-02** | Visual QA     | Paste screenshot with "Alignment is off".             | Logs a visual bug specifically for the UX track. |
| **UC-03** | User Research | `User test notes: they can't find the 'save' button.` | Logs to `vault/research/user-testing/`.          |

### 11. Daily Synthesizer (The Pulse)

| ID        | Title             | Input Signal | Expected Outcome                            |
| :-------- | :---------------- | :----------- | :------------------------------------------ |
| **DS-01** | Morning           | `#morning`   | Succinct table of Criticals + Today's Plan. |
| **DS-02** | EOD Recap         | `#eod`       | Accomplishments list + Tomorrow's preview.  |
| **DS-03** | Dashboard Refresh | `#status`    | Fully updates the root `STATUS.md`.         |

### 12. Weekly Synthesizer (The Auditor)

| ID        | Title      | Input Signal | Expected Outcome                                                                   |
| :-------- | :--------- | :----------- | :--------------------------------------------------------------------------------- |
| **WS-01** | Cleanup    | `#weekly`    | Archives items marked `[x]` for >7 days.                                           |
| **WS-02** | Stale Flag | `#weekly`    | Flags active items older than 14 days as `⚠️ Stale`.                               |
| **WS-03** | Rollup     | `#weekly`    | Generates a high-density PDF/Markdown summary in `vault/meetings/weekly-digests/`. |

---

## 🕸️ Mesh Orchestration Tests (Inter-Agent)

| ID          | Title                    | Scenario                                       | Expected Mesh Flow                                                                         |
| :---------- | :----------------------- | :--------------------------------------------- | :----------------------------------------------------------------------------------------- |
| **MESH-01** | **The Bug-to-ADR**       | Bug report reveals a major architectural flaw. | **Bug Chaser** -> **Enineering Collaborator** (Creates ADR).                               |
| **MESH-02** | **The Boss-to-Brief**    | Boss asks for status on a complex feature.     | **Boss Tracker** -> **Stakeholder Manager** -> **Daily Synthesizer** (Prominent in Brief). |
| **MESH-03** | **The Visual-to-Sprint** | User pastes mockup feedback from a client.     | **Visual Processor** -> **UX Collaborator** -> **Task Manager** (Adds to Sprint).          |
