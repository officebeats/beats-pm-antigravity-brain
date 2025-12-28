# 🧠 Beats PM Antigravity Brain

> **Your AI-powered Product Management second brain.**  
> Capture chaos. Surface patterns. Never let critical items slip.

[![Made for Antigravity](https://img.shields.io/badge/Made%20for-Antigravity-blueviolet?style=for-the-badge)](https://deepmind.google/antigravity/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

---

## ⚡ Get Started in 60 Seconds

### Prerequisites

- [Google Antigravity](https://deepmind.google/antigravity/) installed on your computer
- A folder where you want to keep your PM brain

---

### Step 1: Download This Brain

Click the green **"Code"** button above → **"Download ZIP"** → Extract to a folder you'll remember (e.g., `Documents/my-pm-brain`)

_Or if you're comfortable with git:_

```bash
git clone https://github.com/officebeats/beats-pm-antigravity-brain.git
```

---

### Step 2: Install the Auto-Accept Extension (Recommended)

This extension lets Antigravity work faster by auto-accepting safe file operations. Here's how to install it:

1. **Open Antigravity**
2. **Open the Extensions panel** (`Ctrl+Shift+X` on Windows/Linux, `Cmd+Shift+X` on Mac)
3. **Click the three dots (⋯)** in the top-right of the Extensions panel
4. **Select "Install from VSIX..."** → No wait, easier method:
5. **Go to the extension page**: [Antigravity Auto Accept](https://open-vsx.org/extension/pesosz/antigravity-auto-accept)
6. **Click "Download"** to get the `.vsix` file
7. **In Antigravity**, drag the `.vsix` file into the window, or:
   - Open Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
   - Type: `Extensions: Install from VSIX...`
   - Select the downloaded file
8. **Reload Antigravity** when prompted

✅ Now Antigravity can work autonomously without constant approval clicks!

---

### Step 3: Open in Antigravity

1. Open **Google Antigravity**
2. Click **"Open Folder"** (or drag your folder onto Antigravity)
3. Select the folder you just downloaded

---

### Step 4: Run the Setup Wizard

Once the folder is open in Antigravity, simply type:

```
Help me set up my PM brain. Walk me through the first-time setup.
```

Antigravity will:

- ✅ Ask you simple questions about your role, team, and schedule
- ✅ Generate your personalized settings
- ✅ Create your first week action plan
- ✅ Show you how to capture your first items

**That's it! You're ready to go.** 🎉

---

## 🚀 The Power of Parallel Agents

**This is what makes Antigravity + PM Brain special.**

When you paste a meeting transcript or raw notes, Antigravity doesn't just file it away—it **runs multiple specialized agents in parallel**:

```
📝 You paste: "Meeting notes - boss wants metrics by Friday, checkout is broken,
              Jake will spike the API, Lisa doing mockups..."

                              ⬇️

┌─────────────────────────────────────────────────────────────────┐
│                   MEETING SYNTHESIZER                           │
│                   (parses everything)                           │
└─────────────────────────────────────────────────────────────────┘
              ⬇️           ⬇️           ⬇️           ⬇️
        ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
        │   Boss   │ │   Bug    │ │   Eng    │ │   UX     │
        │ Tracker  │ │  Chaser  │ │  Collab  │ │  Collab  │
        └──────────┘ └──────────┘ └──────────┘ └──────────┘
              ⬇️           ⬇️           ⬇️           ⬇️
        Creates      Creates      Creates      Creates
        boss req     bug entry    eng item     UX task

✅ All in parallel. 10-minute task → 10 seconds.
```

**One input. Multiple organized outputs. Zero manual routing.**

---

## 🎯 What Can It Do?

| Say This to Antigravity                               | What Happens                                   |
| ----------------------------------------------------- | ---------------------------------------------- |
| _"My boss just asked for a metrics report by Friday"_ | Creates a tracked boss request with deadline   |
| _"Bug: checkout page is broken on mobile"_            | Logs bug with SLA tracking                     |
| `#day`                                                | Get a brief right now (adapts to time of day)  |
| `#transcript` + paste a call                          | **Parallel agents** extract & route everything |
| `#meeting` + paste notes                              | Same as above, for hand-written notes          |
| _"What's on my plate this week?"_                     | Shows all active items by priority             |
| _"Draft an update for Sarah on Project X"_            | Generates stakeholder update email             |

---

## 💬 Commands Reference

### Capture Commands

| Command               | What It Does                                   |
| --------------------- | ---------------------------------------------- |
| `#boss [request]`     | Track a boss request (auto-Critical)           |
| `#bug [description]`  | Log a bug with SLA tracking                    |
| `#task [description]` | Create a task                                  |
| `#feature [idea]`     | Log a feature request                          |
| `#ux [task]`          | UX design task                                 |
| `#eng [item]`         | Engineering item                               |
| `#note [anything]`    | Quick note                                     |
| `#transcript`         | Paste a meeting/call transcript for processing |

### Meeting/Notes Commands (Triggers Parallel Agents)

| Command           | What It Does                         |
| ----------------- | ------------------------------------ |
| `#transcript`     | Paste call transcripts or recordings |
| `#meeting`        | Paste hand-crafted meeting notes     |
| `#notes`          | Raw notes dump                       |
| `#call [subject]` | Quick call capture                   |
| `#1on1 [person]`  | 1:1 meeting notes                    |
| `#standup`        | Standup notes                        |

### Brief Commands

| Command    | What It Does                                               |
| ---------- | ---------------------------------------------------------- |
| `#day`     | **On-demand brief** - adapts to current time of day        |
| `#morning` | Morning brief - critical items + calendar + overnight sync |
| `#lunch`   | Midday brief - progress + inbox + afternoon priorities     |
| `#eod`     | End of day - wrap up + accomplishments + tomorrow prep     |
| `#weekly`  | Weekly summary - metrics + strategy pulse                  |
| `#monthly` | Monthly rollup - trends + achievements + next month focus  |

---

## 📁 What's Inside

```
your-pm-brain/
├── 📄 SETTINGS.md          ← Your personalized config (auto-generated)
├── 📥 _INBOX/              ← Drop anything here - AI organizes it
├── 🔥 CRITICAL/            ← Boss requests & escalations
├── 🐛 BUGS/                ← Bug tracking with SLAs
├── 💬 FEEDBACK/            ← Feature requests & user feedback
├── 👥 PEOPLE/              ← Stakeholders & team collaboration
├── 📊 PROJECTS/            ← Active project tracking
├── 🎯 STRATEGY/            ← Opportunities & decisions
├── 📅 MEETINGS/            ← Briefs & meeting notes
└── 🤖 _AGENTS/             ← AI prompts (the magic behind it all)
```

---

## 🏷️ Priority System

| Priority     | Emoji | When to Use                          |
| ------------ | ----- | ------------------------------------ |
| **Critical** | 🔥    | Production down, boss deadline TODAY |
| **Now**      | ⚡    | Needs attention this week            |
| **Next**     | 📌    | Planned for next sprint              |
| **Later**    | 📋    | Backlog, will do eventually          |
| **Sometime** | 💭    | Ideas to explore                     |

---

## 🔧 Works With Other Tools Too

While **Antigravity is the recommended way** to use this brain, it works with any AI tool:

| Tool            | Setup Guide                                |
| --------------- | ------------------------------------------ |
| **Claude Code** | [docs/claude-code.md](docs/claude-code.md) |
| **Gemini CLI**  | [docs/gemini-cli.md](docs/gemini-cli.md)   |
| **Cursor**      | [docs/cursor.md](docs/cursor.md)           |
| **Obsidian**    | [docs/obsidian.md](docs/obsidian.md)       |
| **Notion**      | [docs/notion.md](docs/notion.md)           |
| **Any LLM**     | [docs/anyllm.md](docs/anyllm.md)           |

---

## ❓ FAQ

<details>
<summary><strong>Do I need to know how to code?</strong></summary>

Nope! Just type naturally to Antigravity. It handles everything.

</details>

<details>
<summary><strong>Where is my data stored?</strong></summary>

Everything stays in local markdown files on your computer. Nothing is uploaded anywhere unless you choose to sync with GitHub or cloud storage.

</details>

<details>
<summary><strong>Can I customize it?</strong></summary>

Absolutely. Edit `SETTINGS.md` or ask Antigravity to help you customize anything.

</details>

<details>
<summary><strong>How do I update to the latest version?</strong></summary>

If you cloned with git: `git pull`. If you downloaded the ZIP: download again and copy over (your data in the folders is safe).

</details>

<details>
<summary><strong>What is the #transcript command?</strong></summary>

Paste any meeting transcript, call recording text, or raw notes after `#transcript` and the AI will extract action items, decisions, follow-ups, and route them to the appropriate places in your brain.

</details>

---

## 🤝 Contributing

Contributions welcome! Submit PRs or open issues.

---

## 📄 License

MIT - Use it, modify it, share it.

---

## 👤 Created By

**Ernesto** — Product Management leader & AI enthusiast

<p>
  <a href="https://www.linkedin.com/in/productmg/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://x.com/officebeats"><img src="https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white" alt="X/Twitter"></a>
  <a href="mailto:Ernesto@ProductMG.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
</p>

---

<p align="center">
  <strong>Built by PMs, for PMs.</strong><br>
  <em>Stop drowning in chaos. Start surfacing what matters.</em>
</p>
