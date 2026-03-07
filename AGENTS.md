# AGENTS.md

This file provides guidance to agents when working with code in this repository.

## Non-obvious project rules

- **Tests:** `system/tests/` does not exist. No test files are present in the repo. Do not run `python -m unittest` without first creating tests.
- **Tracker paths (from `system/config.json`):** Boss → `5. Trackers/BOSS_REQUESTS.md`, Bug → `5. Trackers/BUG_TRACKER.md`, Projects → `5. Trackers/PROJECT_TRACKER.md`, Decision → `5. Trackers/DECISION_LOG.md`, Delegated → `5. Trackers/DELEGATED_TASKS.md`, Eng → `5. Trackers/ENG_TASKS.md`, UX → `5. Trackers/UX_TASKS.md`. (Old nested paths like `5. Trackers/bugs/bugs-master.md` are stale — do not use.)
- **Never crawl the filesystem:** Read `system/content_index.json` to find files (per `KERNEL.md`). Regenerate with `python system/scripts/gps_indexer.py`.
- **Single source of truth:** `.agent/` is canonical. `.gemini/`, `.claude/`, `.kilocode/` are symlinks to it — edit only in `.agent/`.
- **Path bootstrap (Python scripts):** Scripts under `system/scripts/` must set `CURRENT_FILE → SYSTEM_ROOT → BRAIN_ROOT → sys.path.insert(0, str(BRAIN_ROOT))` *before* any `system.*` imports (see [`vacuum.py`](system/scripts/vacuum.py)).
- **Canonical config:** All runtime paths in `system/config.json`; do not hardcode paths in scripts. `files.kernel` points to `.agent/rules/GEMINI.md` (not root `GEMINI.md`).
- **Atomic writes:** Use [`system/utils/filesystem.py::atomic_write()`](system/utils/filesystem.py) for all file writes in scripts to prevent corruption.
- **Background jobs:** Dispatch async work via [`system/scripts/turbo_dispatch.py`](system/scripts/turbo_dispatch.py); jobs land in `system/queue/pending/`.
- **Hierarchy enforcement:** No loose files at root of `1. Company`, `2. Products`, or `4. People`; only `PROFILE.md`/`stakeholders.md` allowed (enforced by vacuum rules).
- **Vacuum side effects:** `system/scripts/vacuum.py` moves completed tracker items into yearly archives and updates `5. Trackers/archive/INDEX.md`.
- **Symlink repair:** If tool dirs drift, `system/scripts/fix_symlinks.py` re-links `.claude/`, `.gemini/`, `.kilocode/` to `.agent/`.
- **Default AI model:** `gemini-3-flash-preview` (set in `system/config.json` under `ai.default_model`).
- **README merge conflict:** `README.md` lines 118–152 contain live `<<<<<<< Updated upstream` / `>>>>>>> Stashed changes` markers — resolve before using README as reference.
