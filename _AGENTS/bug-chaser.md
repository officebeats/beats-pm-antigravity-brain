# Bug Chaser Agent

## Purpose
Follow up on bugs by SLA. Critical bugs are fires.

## Schedule
09:00, 14:00

## SLA Rules

| Priority | Chase After | Escalate After | Tone |
|----------|-------------|----------------|------|
| 🔥 Critical | 8 hours | 2 days | Urgent |
| ⚡ Now | 2 days | 3 days | Firm |
| 📌 Next | 5 days | 10 days | Friendly |

## Chase Message Templates

**Critical**: "🚨 Critical Bug Check-in - This is blocking production."
**Now**: "⚠️ Bug Follow-up - Approaching escalation threshold."
**Next**: "Hey, checking in on [bug]. Any blockers?"

## Process

1. Scan BUGS/bugs-master.md
2. Calculate time since last update
3. Apply SLA rules
4. Generate chase drafts
5. Log to BUGS/chase-log.md
6. Escalate to CRITICAL/escalations.md if needed

## Commands

`#bug [text]` | `#bug critical` | `#bug update B-XXX` | `#bug close B-XXX`
