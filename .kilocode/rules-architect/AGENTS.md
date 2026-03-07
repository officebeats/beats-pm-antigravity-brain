# Project Architecture Rules (Non-Obvious Only)

- The system enforces "no loose files" at the root of `1. Company`, `2. Products`, and `4. People`; only `PROFILE.md`/`stakeholders.md` are allowed (enforced by vacuum rules).
- Tracker routing is canonical: paths come from `system/config.json["trackers"]` (flat filenames, e.g., `5. Trackers/BUG_TRACKER.md`). Old nested subdirectory paths are stale.
- `.agent/` is the single source of truth for all rules, templates, and skills. `.gemini/`, `.claude/`, `.kilocode/` are symlinks — architectural changes to rules/templates must target `.agent/` only.
- `system/content_index.json` is the GPS index powering file discovery; it must be regenerated via `python system/scripts/gps_indexer.py` after structural changes.
- Background job architecture: [`system/scripts/turbo_dispatch.py`](system/scripts/turbo_dispatch.py) writes jobs to `system/queue/pending/`; workers pick them up from there. Do not bypass the queue for async work.
- All file I/O in scripts must go through [`system/utils/filesystem.py::atomic_write()`](system/utils/filesystem.py) — direct writes are an architectural anti-pattern here.
- `system/config.json` is the single runtime config; `files.kernel` points to `.agent/rules/GEMINI.md` (not root `GEMINI.md`). New architectural paths must be registered here.
