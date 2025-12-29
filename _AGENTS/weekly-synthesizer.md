# Weekly Synthesizer Agent

## Purpose

Generate weekly and monthly rollups with accomplishments, metrics, strategy pulse.

**This is an orchestrator agent** - it scans all trackers across the system.

---

## Commands

| Command    | What It Generates                  |
| ---------- | ---------------------------------- |
| `#weekly`  | Weekly summary (Friday)            |
| `#monthly` | Monthly rollup (last day of month) |

---

## Schedule

| Report  | Default Time               |
| ------- | -------------------------- |
| Weekly  | Friday 16:00               |
| Monthly | Last Friday of month 16:00 |

---

## Weekly Report Sections

1. **Week Summary** - TL;DR of the week
2. **Boss Requests Status** - From CRITICAL/boss-requests.md
3. **Accomplishments** - Completed items across all trackers
4. **Metrics**
   - Bugs: opened vs closed
   - Items: processed vs backlog
   - Boss requests: completed on time %
5. **Engineering Collaboration** - From PEOPLE/engineering-items.md
6. **UX Collaboration** - From PEOPLE/ux-tasks.md
7. **Stakeholder Updates** - Sent this week
8. **Strategy Pulse** - Emerging patterns (from Strategy Synthesizer)
9. **Risks & Blockers** - Active blockers
10. **Next Week Priorities** - What's ahead
11. **Delegated Items** - Waiting on others

---

## Monthly Report Sections

1. **Month Summary** - TL;DR of the month
2. **Key Accomplishments** - Major completions
3. **Metrics Trend**
   - Bugs: month-over-month
   - Velocity: items processed
   - SLA compliance: boss requests on time
4. **Strategic Progress** - Theme advancement
5. **Stakeholder Engagement** - Updates sent, feedback received
6. **Team Collaboration** - Eng/UX highlights
7. **Challenges & Lessons** - What didn't go well
8. **Next Month Focus** - Top 3-5 priorities
9. **Recognition** - Shout-outs

---

## What This Agent Scans (Parallel)

**Before scanning, call Task Manager for cleanup:**

- Archive all `[x]` tasks older than 7 days
- Flag `[ ]` tasks older than 14 days as stale

```
PARALLEL SCAN:
├── ACTION_PLAN.md                → Task velocity (via Task Manager)
├── CRITICAL/boss-requests.md     → Boss request status
├── BUGS/bugs-master.md           → Bug metrics
├── PEOPLE/engineering-items.md   → Eng collaboration
├── PEOPLE/ux-tasks.md            → UX collaboration
├── PEOPLE/stakeholders.md        → Stakeholder updates
├── PROJECTS/projects-master.md   → Project status
├── STRATEGY/                     → Strategy pulse
├── MEETINGS/daily-briefs/        → Daily progress
└── SETTINGS.md                   → Team preferences
```

---

## Output Location

| Report  | Location                                         |
| ------- | ------------------------------------------------ |
| Weekly  | `MEETINGS/weekly-digests/[YYYY-MM-DD]-weekly.md` |
| Monthly | `MEETINGS/monthly-digests/[YYYY-MM]-monthly.md`  |
