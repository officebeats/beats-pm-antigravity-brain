# Daily Synthesizer Agent

## Purpose
Generate morning, midday, and evening briefs. Critical items always first.

## Schedule

| Brief | Time | Focus |
|-------|------|-------|
| Morning | 06:00 | Critical + calendar + overnight sync |
| Midday | 12:00 | Progress + inbox + afternoon |
| Evening | 17:00 | Wrap + accomplishments + tomorrow |

## Priority Order (Always)

1. 🔥 Boss requests
2. 🔥 Critical bugs
3. ⚡ Now bugs approaching escalation
4. 🔴 Stale items (48+ hrs)
5. 🚧 Blocked items
6. 📤 Stakeholder updates due
7. 🔧 Engineering items waiting
8. 🎨 UX items waiting
9. 📅 Calendar
10. 📥 External tool sync (Notion/Obsidian/Trello)
11. ✅ Progress

## External Tool Sync

At each brief, pull from:
- _INBOX/notion/ (Notion exports)
- _INBOX/obsidian/ (Obsidian sync)
- _INBOX/trello/ (Trello exports)

## Output

MEETINGS/daily-briefs/[YYYY-MM-DD]-[morning|midday|evening].md
