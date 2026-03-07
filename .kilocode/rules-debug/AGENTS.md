# Project Debug Rules (Non-Obvious Only)

- `system/tests/` does not exist — do not run `python -m unittest` without first creating test files.
- `system/scripts/vacuum.py` updates yearly archives and `5. Trackers/archive/INDEX.md`; debug failures may be side effects of archive index writes.
- `README.md` lines 118–152 contain live git merge conflict markers (`<<<<<<< Updated upstream` / `>>>>>>> Stashed changes`) — do not use README as a reliable reference until resolved.
- `system/content_index.json` is the GPS index; if file lookups fail, regenerate it with `python system/scripts/gps_indexer.py`.
- Background jobs dispatched via [`system/scripts/turbo_dispatch.py`](system/scripts/turbo_dispatch.py) land in `system/queue/pending/` — check there for stuck or failed jobs.
- All file writes in scripts must use [`system/utils/filesystem.py::atomic_write()`](system/utils/filesystem.py); direct `open(..., 'w')` writes risk partial-write corruption that can be hard to diagnose.
