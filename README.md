# 🧠 Beats PM Antigravity Brain

> **Your AI-powered Product Management second brain.**  
> Capture chaos. Surface patterns. Never let critical items slip.

[![Made for Antigravity](https://img.shields.io/badge/Made%20for-Antigravity-blueviolet?style=for-the-badge)](https://antigravity.google/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

---

## ⚡ Get Started in 60 Seconds

### Prerequisites

- [Google Antigravity](https://antigravity.google/) installed on your computer
- A folder where you want to keep your PM brain

---

### Step 1: Download This Brain

Click the green **"Code"** button above → **"Download ZIP"** → Extract to a folder you'll remember (e.g., `Documents/my-pm-brain`)

_Or if you're comfortable with git:_

```bash
git clone https://github.com/officebeats/beats-pm-antigravity-brain.git
```

---

---

### Step 2: Open in Antigravity

1. Open **Google Antigravity**
2. Click **"Open Folder"** (or drag your folder onto Antigravity)
3. Select the folder you just downloaded

---

### Step 3: Run the Setup Wizard

Once the folder is open, simply type:

```
Help me set up my PM brain.
```

**Antigravity will:**

- ✅ **Initialize your files** (runs the setup scripts for you)
- ✅ **Customize your settings** (asks about your role/team)
- ✅ **Secure your privacy** (configures git-ignore rules)

**That's it! You're ready to go.** 🎉

---

## 🚀 Why Antigravity? Built for PMs, Not Devs

**This PM Brain works with any AI coding tool** (see [docs/claude-code.md](docs/claude-code.md)), but Antigravity is the **recommended experience** — especially if you're not a developer.

### 🎯 The Killer Feature: Screenshot → Task

Antigravity is powered by **Gemini** — Google's multimodal AI with world-class image understanding. This means:

- 📸 **Paste a screenshot** of a bug → Antigravity reads the UI, identifies the product, and logs it to the right tracker
- 📊 **Drop a slide deck** → Key decisions get extracted and routed
- 🎨 **Share a design mock** → UX feedback gets captured with visual context

This isn't just "image support" — it's **native vision** that understands what it's looking at. Claude Code can process images, but Gemini's multimodal architecture was built for this from day one.

### The Real Difference

| What Matters for PMs    | Antigravity                                 | Claude Code                     |
| ----------------------- | ------------------------------------------- | ------------------------------- |
| **Interface**           | ✅ Visual editor (VS Code-based)            | Terminal-only                   |
| **Setup**               | ✅ Drag folder → start talking              | Requires CLI comfort            |
| **Learning Curve**      | ✅ Click buttons, paste screenshots         | Commands, flags, config files   |
| **File Drop Zone**      | ✅ Drag files into `00-DROP-FILES-HERE-00/` | Manual `cat` or path references |
| **Screenshot Analysis** | ✅ Paste image → instant routing            | Works, but less seamless        |
| **Built-in Browser**    | ✅ Visual testing & demos included          | Requires MCP setup              |
| **Image Generation**    | ✅ Native support                           | Requires external tools         |

### What About Claude Code's Agents?

**Technically, Claude Code can do most of what Antigravity does.** You can configure custom agents via `CLAUDE.md`, add skills, and set up MCP tools. Power users can achieve similar orchestration.

**But here's the catch**: Claude Code is built for developers who live in the terminal. If you're comfortable with `git`, `npx`, and YAML configs, it's excellent.

For PMs who just want to:

- 📂 **Drag a folder** and start talking
- 📸 **Paste a screenshot** and have it auto-triaged
- 📝 **Edit markdown** in a visual editor
- 🚀 **Skip the terminal** entirely

...Antigravity is the path of least resistance.

> **Bottom Line**: Claude Code is a power tool. Antigravity is the power tool with training wheels pre-installed — and for most PMs, that's exactly what you want.

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

| Command                 | Action                       |
| ----------------------- | ---------------------------- |
| `#boss [request]`       | Track a boss request         |
| `#bug [description]`    | Log a bug                    |
| `#task [description]`   | Create a task                |
| `#feature [idea]`       | Log a feature request        |
| `#ux [task]`            | UX design task               |
| `#eng [item]`           | Engineering item             |
| `#note [anything]`      | Quick note                   |
| `#screenshot`           | Capture image from clipboard |
| `#clipboard` / `#paste` | Capture ALL from clipboard   |
| `#process`              | Process staged batch         |
| `#latest` / `#status`   | Succinct time-aware brief    |
| `#update`               | Pull latest version          |

### 📂 File Drop Zone & Clipboard (The Workaround)

Antigravity does not natively support "file uploads" or "image pasting" directly into the chat box like some web apps. To work around this, the Beats Brain provides two primary ingestion methods:

1.  **Direct Drop**: Drag files into the **`00-DROP-FILES-HERE-00/`** folder and say "Check [filename]".
2.  **Clipboard Ingestion (Recommended)**:
    - **Step 1**: Copy any file(s), screenshot, or text to your OS clipboard (Ctrl+C).
    - **Step 2**: Type **`#clipboard`**, **`#paste`**, or **`#screenshot`** in the chat.
    * **Step 3**: The AI will autonomously reach out, grab your clipboard contents, and save them to **`00-DROP-FILES-HERE-00/`**.
    * **Step 4**: Provide context (e.g., "Analyze this") or type **`#process`** to commit the data.

**Note**: All status/briefing commands (`#day`, `#status`, etc.) generate **succinct, table-based outputs** optimized for fast scanning.

## ⚡ The Workflow: Chaos vs. Order

This system is designed for **low-friction capture** and **high-focus execution**.

### 1. 🌪️ Chaos Mode (Capture)

- **Thoughts?** Open **`BRAIN_DUMP.md`** and just type.
- **Chat?** Just tell Antigravity random things.
  - _Actionable:_ "Fix the bug" → **I do it.**
  - _Random:_ "We should explore dark mode" → **I park it in Brain Dump.**
- **Files?** Drag them into **`00-drop-files-here-00/`**.
- **Screenshots?** Paste them into chat and say `#screenshot`.

### 2. ⚖️ Order Mode (Organize)

When you're ready to make sense of the chaos:

- **What happens:** The AI scans your brain dump and file drops, then organizes actionable items into your **`ACTION_PLAN.md`**.

### 3. 🎯 Focus Mode (Execute)

- **Open:** **`ACTION_PLAN.md`**
- This is your single source of truth for the day. Execute the checklist. Ignore everything else.

---

## 🚦 Quick Commands

| Command          | Action                                                                   |
| :--------------- | :----------------------------------------------------------------------- |
| **`#day`**       | **Start/Update Day**. Processes brain dump & file drops.                 |
| **`#b`**         | **Log Bug**. Example: `#b login failed on iOS`                           |
| **`#t`**         | **Log Task**. Example: `#t email boss re: budget`                        |
| **`#braindump`** | **Append/Process**. `#braindump [text]` to add, `#braindump` to process. |
| **`#update`**    | **Refresh**. Pulls all latest changes if you edited files manually.      |

> **Pro Tip:** You don't need to memorize commands. Just talk naturally. "Here is a file", "Note this down", "What's next?".

---

## Director-Level Organization

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
<summary><strong>Any tips for power users?</strong></summary>

**Install the Auto-Accept Extension**: This lets Antigravity work faster by auto-accepting safe file operations.

1. Download from [Open VSX](https://open-vsx.org/extension/pesosz/antigravity-auto-accept)
2. Drag the `.vsix` file into Antigravity.
3. Reload.

**Install the Antigravity Cockpit Extension**: Track your LLM token usage in real-time so you know when you're approaching context limits.

1. Download from [Open VSX](https://open-vsx.org/vscode/item?itemName=jlcodes.antigravity-cockpit)
2. Drag the `.vsix` file into Antigravity.
3. Reload.
</details>

<details>
<summary><strong>Do I need to know how to code?</strong></summary>

Nope! Just type naturally to Antigravity. It handles everything.

</details>

<details>
<summary><strong>Where is my data stored?</strong></summary>

Everything stays in local markdown files on your computer. Nothing is uploaded anywhere.

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
