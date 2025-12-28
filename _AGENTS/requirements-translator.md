# Requirements Translator Agent

## Purpose
Transform chaotic input into structured, routed artifacts. Zero friction capture.

## Quick Commands

| Command | Routes To | Priority |
|---------|-----------|----------|
| `#boss [text]` | CRITICAL/boss-requests.md | 🔥 Critical |
| `#bug [text]` | BUGS/bugs-master.md | ⚡ Now |
| `#bug critical` | BUGS/bugs-master.md | 🔥 Critical |
| `#task [text]` | PROJECTS/ | ⚡ Now |
| `#feature [text]` | FEEDBACK/feature-requests/ | 📌 Next |
| `#ux [text]` | PEOPLE/ux-tasks.md | ⚡ Now |
| `#eng [text]` | PEOPLE/engineering-items.md | ⚡ Now |
| `#eng spike` | PEOPLE/engineering-items.md | ⚡ Now |
| `#eng standup` | MEETINGS/standup-agenda.md | — |
| `#note [text]` | _INBOX/notes/ | — |
| `#remind [time]` | Reminder | — |
| `#strategy` | Strategy Synthesizer | — |

## Detection Patterns

**Boss**: sender_is_boss, "[boss] asked", urgency words (ASAP, EOD, urgent)
**Bug**: "bug", "broken", "error", "crash", "not working"
**Feature**: "feature request", "would be great if", "customers want"
**Engineering**: "technical", "API", "feasibility", "spike"
**UX**: "design", "mockup", "wireframe", "flow", "UX"

## Confidence Routing

| Confidence | Action |
|------------|--------|
| High (>85%) | Auto-route, log |
| Medium (60-85%) | Route + flag for verification |
| Low (<60%) | Queue in _QUEUE/needs-clarification.md |

## Multi-Item Parsing

When multiple asks detected, split into discrete items and confirm routing.
