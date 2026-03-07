# Project Coding Rules (Non-Obvious Only)

- Keep `system/scripts/` path bootstrap order (`CURRENT_FILE` → `SYSTEM_ROOT` → `BRAIN_ROOT` → `sys.path.insert`) before any `system.*` imports (see [`vacuum.py`](system/scripts/vacuum.py)).
- Use `system/config.json` as the single source of truth for runtime paths; avoid hardcoding paths in new scripts.
- Use [`system/utils/filesystem.py::atomic_write()`](system/utils/filesystem.py) for all file writes in scripts — prevents partial-write corruption.
- Dispatch background/async work via [`system/scripts/turbo_dispatch.py`](system/scripts/turbo_dispatch.py); jobs land in `system/queue/pending/`.
- Tracker flat-file paths come from `system/config.json["trackers"]` — do not use old nested paths like `5. Trackers/bugs/bugs-master.md`.
- `.agent/` is the canonical source; `.gemini/`, `.claude/`, `.kilocode/` are symlinks — always edit files under `.agent/`, never the symlink targets directly.
