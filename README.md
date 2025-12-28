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

## 🚀 Antigravity Director Mode (v1.0)

**This system is now powered by a Neural Mesh of agents.**

Unlike standard bots, these agents:

1.  **Talk to Each Other**: The `Meeting Synthesizer` can trigger the `Bug Chaser` who triggers the `Strategy Synthesizer`.
2.  **Understand Context**: Paste a screenshot. The system checks your `PRODUCTS/` folder, identifies it's your "Mobile App", and routes the bug accordingly.
3.  **Run in Parallel**: One raw dump → 5 organized outputs instantly.

---

## 🎯 What Can It Do?

| Say This to Antigravity         | What Happens (Orchestration)                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------- |
| `#transcript` + paste call      | **Parallel Execution**: Routes boss asks, bugs, eng items, and design tasks simultaneously. |
| `#screenshot` + paste image     | **Visual Analysis**: Identifies product, logs bug/task based on what it sees.               |
| `#day`                          | **Adaptive Brief**: Gives you exactly what you need for this specific time of day.          |
| _"My boss just asked for..."_   | **Boss Tracker**: Logs critical request with SLA monitoring.                                |
| _"Bug: checkout failed on iOS"_ | **Context Routing**: Detects "iOS" → logs to "Mobile App" product tracker.                  |

---

## � Privacy Mode (100% Secure)

This repo is configured to be **safe for real-world work**.

1.  **Git Ignore**: `SETTINGS.md` and all active trackers (`BUGS/*.md`, `PEOPLE/*.md`) are ignored.
2.  **Antigravity Ignore**: Large data folders are hidden from the AI context unless asked.
3.  **Templates**: The repo only tracks `*_TEMPLATE.md` files.

**How to sync between computers (Mac <-> PC):**

1.  `git pull` on the new machine.
2.  Run `Setup-Brain` (cmd or command).
3.  It downloads new templates but **keeps your local data private**.

---

## �💬 Commands Reference

### Universal Capture (Any Agent can handle these)

| Command               | Action                |
| --------------------- | --------------------- |
| `#boss [request]`     | Track a boss request  |
| `#bug [description]`  | Log a bug             |
| `#task [description]` | Create a task         |
| `#feature [idea]`     | Log a feature request |
| `#ux [task]`          | UX design task        |
| `#eng [item]`         | Engineering item      |
| `#note [anything]`    | Quick note            |
| `#screenshot`         | process pasted image  |

### Orchestrators (The Heavy Lifters)

| Command       | What It Does                                     |
| ------------- | ------------------------------------------------ |
| `#transcript` | **Meeting Synthesizer**: Parses calls/recordings |
| `#meeting`    | **Meeting Synthesizer**: Parses raw notes        |
| `#day`        | **Daily Synthesizer**: Time-adaptive brief       |
| `#weekly`     | **Weekly Synthesizer**: Portfolio rollup         |

---

## � Director-Level Organization

```
your-pm-brain/
├── KERNEL.md               ← The "System Prompt" connecting all agents
├── PRODUCTS/               ← 🧠 Your Portfolio Context (New!)
│   ├── mobile-app.md       ← Detects "iOS", "Android", "Checkout"
│   └── data-platform.md    ← Detects "API", "AWS", "Pipeline"
├── SETTINGS.md             ← Config
├── _AGENTS/                ← The Neural Mesh
├── CRITICAL/               ← Global Authority (Boss/Escalations)
├── BUGS/                   ← Global Quality (All Products)
└── ...
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
<summary><strong>How do I manage multiple products? (Director Mode)</strong></summary>

Easy. Just add a new file to the `PRODUCTS/` folder for each product (e.g. `mobile-app.md`). Antigravity will auto-detect which product you're talking about based on keywords you define in that file.

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
