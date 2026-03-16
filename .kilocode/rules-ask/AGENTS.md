# Project Documentation Rules (Non-Obvious Only)

- Runtime behavior and routing precedence are defined in `.agent/rules/GEMINI.md` (pointed to by `system/config.json["files"]["kernel"]`); treat it as the authoritative policy doc — root `GEMINI.md` and `KERNEL.md` are secondary.
- `system/content_index.json` is the canonical file index — use it to locate files instead of crawling the filesystem. Regenerate with `python system/scripts/gps_indexer.py`.
- Tracker paths in `system/config.json["trackers"]` are the ground truth: flat filenames like `5. Trackers/BUG_TRACKER.md`. Old nested paths (e.g., `5. Trackers/bugs/bugs-master.md`) referenced in older docs are stale.
- `README.md` lines 118–152 contain unresolved git merge conflict markers — do not cite README as authoritative until resolved.
- `.agent/` is the canonical source for all rules, templates, and skills; `.gemini/`, `.claude/`, `.kilocode/` are symlinks to it.
