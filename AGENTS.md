# AGENTS.md

This file provides guidance to AI coding agents working in this repository.

## Project Overview

**Beats PM Antigravity Kit** is an AI-powered Product Management operating system. It provides structured workflows, skills, and virtual agent personas to automate PM tasks like task tracking, PRD creation, meeting synthesis, and boss 1:1 preparation.

**Primary Runtime**: Google Antigravity (VS Code extension) - Full interactive workflow menu support
**Secondary Runtimes**: Gemini CLI, Claude Code, Kilo Code - Manual command entry only

### Command Support

| Runtime | Interactive Menu | Command Trigger | Status |
|---------|------------------|-----------------|--------|
| Antigravity | ✅ Type `/` to see options | `/vacuum`, `/boss`, etc. | Full support |
| Claude Code | ❌ Manual only | Type `/vacuum`, `/boss` | Available |
| Kilo Code | ❌ Manual only | Type `/vacuum`, `/boss` | Available |
| Gemini CLI | ❌ Manual only | Type `#vacuum`, `#boss` | Available |

> **Note**: Antigravity offers the complete `/` menu experience. CLI tools require typing the full command name manually.

## Development Commands

### Running Tests

```bash
# Run all tests (Python unittest)
python system/scripts/run_tests.py

# Run tests directly with unittest
python -m unittest discover -s system/tests -p 'test_*.py' -v

# Run a single test
python -m unittest system.tests.test_vacuum.TestVacuum.test_vacuum_tracker_file
```

### Utility Scripts

| Script | Purpose |
|--------|---------|
| `system/scripts/vacuum.py` | System cleanup and archival |
| `system/scripts/gps_indexer.py` | Generate `system/content_index.json` for file navigation |
| `system/scripts/vibe_check.py` | System health diagnostics |
| `system/scripts/enforce_structure.py` | Validate folder hierarchy compliance |

## Architecture

### Three-Layer System

```
┌─────────────────────────────────────────────┐
│  WORKFLOWS (24)                             │
│  Playbooks triggered by /commands           │
│  Location: .agent/workflows/                │
├─────────────────────────────────────────────┤
│  SKILLS (26)                                │
│  Modular AI expertise, loaded on-demand     │
│  Location: .agent/skills/                   │
├─────────────────────────────────────────────┤
│  AGENTS (7)                                 │
│  Virtual team personas with behaviors       │
│  Location: .agent/agents/                   │
└─────────────────────────────────────────────┘
```

### Single Source of Truth

`.agent/` is the canonical source for all AI configuration. Other tool directories are symlinks:
- `.gemini/` → symlinks to `.agent/`
- `.claude/` → symlinks to `.agent/`
- `.kilocode/` → symlinks to `.agent/`

**Rule**: Edit files in `.agent/` only. Never edit directly in `.gemini/`, `.claude/`, or `.kilocode/`.

### Symlink Management

If symlinks break (common with relative paths), run:
```bash
python3 system/scripts/fix_symlinks.py
```

Or manually:
```bash
REPO_ROOT="$(pwd)"
ln -sf "$REPO_ROOT/.agent/workflows" .claude/commands
ln -sf "$REPO_ROOT/.agent/workflows" .kilocode/workflows
ln -sf "$REPO_ROOT/.agent/workflows" .gemini/workflows
```

## Privacy Model

Folders 0-5 contain **local-only sensitive data** and are gitignored. Never push content from these folders to git.

## Routing Precedence

Task items route to specific tracker files:
1. Boss Ask → `5. Trackers/critical/boss-requests.md`
2. Bug → `5. Trackers/bugs/bugs-master.md`
3. Task → `5. Trackers/TASK_MASTER.md`
4. Decision → `5. Trackers/DECISION_LOG.md`
5. Delegated → `5. Trackers/DELEGATED_TASKS.md`

## Code Style Guidelines

### Python Scripts (`system/scripts/`)

**Imports**: Always start with path setup before system imports:
```python
from pathlib import Path
import sys

CURRENT_FILE = Path(__file__).resolve()
SYSTEM_ROOT = CURRENT_FILE.parent.parent
BRAIN_ROOT = SYSTEM_ROOT.parent
sys.path.insert(0, str(BRAIN_ROOT))

from system.utils.ui import print_cyan
from system.scripts import sys_config
```

**Type Hints**: Use `typing` module for complex types:
```python
from typing import Optional, List, Tuple, Union, Dict, Any
```

**Path Handling**: Always use `pathlib.Path` for file operations. Use `Union[str, Path]` type hints for path parameters.

**Naming Conventions**:
- Functions: `snake_case` with descriptive verbs (`ensure_directory`, `vacuum_tracker`)
- Classes: `PascalCase` (`TestVacuum`, `DualWriter`)
- Constants: `UPPER_SNAKE_CASE` (`TRACKERS_DIR`, `ARCHIVE_DIR`)
- Private functions: `_leading_underscore`

**Error Handling**: Use try-except blocks with UI error reporting:
```python
try:
    return Path(path).read_text(encoding=encoding)
except (IOError, UnicodeDecodeError) as e:
    from .ui import print_error
    print_error(f"Failed to read file {path}: {e}")
    return None
```

**File Encoding**: Always use `utf-8` encoding for file operations.

**Docstrings**: Use triple-quoted double strings for module/function docstrings.

### Testing (`system/tests/`)

- Use `unittest` framework (no pytest)
- Test class names: `Test<ModuleName>`
- Test methods: `test_<specific_behavior>`
- Use `setUp()` and `tearDown()` for fixture management
- Mock system utils: `sys.modules["utils"] = MagicMock()`
- Path setup pattern:
```python
import sys
import os
from pathlib import Path

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)
```

### Markdown Files

- Use YAML frontmatter for metadata (`description:`, `skills:`, etc.)
- Use Mermaid diagrams for workflows
- Use tables for data presentation
- Trackers use GitHub-flavored markdown checkboxes `- [ ]` / `- [x]`
