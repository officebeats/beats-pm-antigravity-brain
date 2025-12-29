---
description: Release a new version of the brain (Tag + GitHub Release)
---

1. Update version strings in `README.md`, `SETTINGS_TEMPLATE.md`, and `_AGENTS/*.md`.
2. Commit the changes: `git commit -a -m "chore: Release vX.Y.Z"`
3. Tag the release: `git tag vX.Y.Z`
4. Push to remote: `git push origin main && git push origin vX.Y.Z`
   // turbo
5. Create GitHub Release: `gh release create vX.Y.Z --title "vX.Y.Z Title" --notes "Release notes here"`
   - _Note_: If `gh` is not found, verify PATH or ask user to authenticate.
