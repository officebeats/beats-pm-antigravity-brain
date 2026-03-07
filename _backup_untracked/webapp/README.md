# Beats PM Brain — Companion Web App

A beautiful, performant companion app for the Beats PM Antigravity Brain kit.
Reads your local tracker files and presents them in multiple views.

## Features

- **Board View** — Overview of all trackers with progress bars and stats
- **List View** — Virtualized flat list with section grouping and filters
- **Kanban View** — Drag-and-drop columns (Pending → In Progress → Done)
- **Search View** — Fuzzy full-text search across all tracker items (Fuse.js)
- **Dark Mode** — Automatic system preference detection + manual toggle
- **Live Edits** — Click status circles to cycle through states; changes write back to markdown files atomically

## Quick Start (Windows)

```bat
webapp\start.bat
```

Then open **http://localhost:5173** in your browser.

## Manual Start

### Backend (FastAPI)

```bash
cd webapp/backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

API docs: http://localhost:8000/api/docs

### Frontend (React + Vite)

```bash
cd webapp/frontend
npm install
npm run dev
```

## Architecture

```
webapp/
├── backend/                  # Python FastAPI
│   ├── main.py               # App entry point, CORS, routes
│   ├── requirements.txt
│   ├── models/
│   │   └── tracker.py        # Pydantic models
│   └── routers/
│       ├── trackers.py       # Tracker CRUD (reads system/config.json for paths)
│       ├── files.py          # File browser + content_index.json
│       └── search.py         # Server-side search
└── frontend/                 # React 18 + TypeScript + Vite
    └── src/
        ├── App.tsx
        ├── stores/useStore.ts # Zustand global state
        ├── components/        # Sidebar, Header, ItemRow, TrackerCard
        └── views/             # BoardView, ListView, KanbanView, SearchView
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.10+, FastAPI, uvicorn |
| Frontend | React 18, TypeScript, Vite |
| Styling | Tailwind CSS (Apple design tokens) |
| Animation | Framer Motion |
| Drag & Drop | @dnd-kit |
| Virtual Scroll | @tanstack/react-virtual |
| Search | Fuse.js (client-side fuzzy) |
| State | Zustand |

## Data Flow

1. Backend reads `system/config.json` for tracker file paths
2. Parses markdown checklist items (`- [ ]`, `- [x]`, `- [-]`)
3. Serves structured JSON via REST API
4. Frontend fetches on load, caches in Zustand store
5. Status updates write back to markdown files atomically (temp file → rename)

## Notes

- Tracker paths come from `system/config.json["trackers"]` — never hardcoded
- File writes use atomic temp-file-then-rename to prevent corruption
- The GPS content index (`system/content_index.json`) is exposed at `/api/files/index`
- Folders 1–5 are `.gitignored` — data stays local, never pushed to GitHub
