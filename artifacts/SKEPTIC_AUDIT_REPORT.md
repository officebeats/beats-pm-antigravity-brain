# 🔍 Code Skeptic Audit — Beats PM Antigravity Brain

**Date**: 2026-02-19  
**Auditor**: Code Skeptic Mode  
**Verdict**: ⚠️ BROKEN TEST SUITE + ZERO FAN-OUT CAPABILITY. The "Parallelism Mandate" exists ONLY in documentation.

> "Show me the logs or it didn't happen."

---

## 📊 Executive Summary

**Test Results (PROOF):** `FAILED (failures=17, errors=12, skipped=4)` out of 74 tests.

The system CLAIMS to be a cutting-edge agent mesh with "parallel fan-out" and "dynamic skill activation." The CODE delivers a sequential file-based queue that can only process 4 hard-coded job types and has never been correctly pointed at its actual queue directory.

---

## 🔴 P0 — CRITICAL BLOCKERS (Fix These First)

### P0-1: Test Suite Has 29 Failures/Errors — Nothing Is "Working"

**Claim**: The system is functional and production-ready.  
**Reality**: `python3 -m unittest discover -s system/tests -p 'test_*.py'` → **17 failures, 12 errors**.

Root failures block entire test modules:

| Error | File | Root Cause |
|-------|------|-----------|
| `ModuleNotFoundError: No module named 'scripts'` | `test_core_setup.py`, `test_features.py` | `SYSTEM_DIR = ROOT_DIR / 'Beats-PM-System' / 'system'` — this path **does not exist** |
| `ModuleNotFoundError: No module named 'yaml'` | `test_skills_v2.py` | PyYAML not installed; `.venv` never activated |
| `FileNotFoundError: ux-collab/SKILL.md` | `test_skills_validation.py` | Skill renamed to `ux-collaborator` but tests still reference `ux-collab` |
| `AssertionError: Missing critical files: ['KERNEL.md']` | `test_structure.py` | File renamed to `GEMINI.md`; test not updated |

**The path `ROOT_DIR / 'Beats-PM-System' / 'system'` appears 3 times across test files.** This is a ghost directory from an old repo rename. No test can import `scripts.kernel_utils` via this path.

---

### P0-2: Queue Paths Point to Non-Existent `Beats-PM-System/` Ghost Directory

Every queue implementation uses the wrong root path:

```python
# dispatch.py line 19 — WRONG
QUEUE_DIR = ROOT_DIR / "Beats-PM-System/system/queue"

# task_queue.py line 29 — ALSO WRONG
self.queue_dir = self.root / "Beats-PM-System/system/queue"

# queue_worker.py line 15 — HARDCODED STRING, ALSO WRONG
QUEUE_DIR = os.path.join(ROOT_DIR, "Beats-PM-System", "system", "queue")
```

**The actual queue is at `system/queue/`** (relative to brain root). The `Beats-PM-System/` prefix is a corpse from an old directory rename.

**Proof**: `system/queue/failed/` has 2 jobs from January 2026 that were submitted but never worked off because the worker was watching the wrong directory. They sit there today:
- `1768698081_f78272b6-...` (type: `invalid_type`, Jan 17 2026)
- `1768861756_b47c587f-...` (second failed job)

**Fix**: All three files must use `BRAIN_ROOT / "system/queue"`.

---

### P0-3: Two Incompatible Queue Implementations — Neither Is Canonical

| File | Protocol Name | Job ID Format | Status |
|------|--------------|---------------|--------|
| `dispatch.py` + `queue_worker.py` | "Centrifuge Protocol" | `{timestamp}_{uuid4}` | Path broken |
| `turbo_dispatch.py` + `task_queue.py` | "Turbo Dispatcher" | `{timestamp}_{job_type}` | Path broken |

`queue_worker.py` only handles `transcript_archive` and `echo`.  
`task_queue.py` only handles `structure_enforce`, `vacuum`, `optimize_skills`, `gps_index`.

**Neither handles the same job types.** `turbo_dispatch.py` delegates to `task_queue.py`, but `dispatch.py` has no relation to `task_queue.py`. These are two separate incomplete implementations that were never consolidated.

**AGENTS.md says**: `dispatch.submit_job("transcript_archive", {"file": "meeting.txt"})` — this routes to `queue_worker.py`, but `turbo_dispatch.submit()` routes to `task_queue.py` which doesn't know `transcript_archive`. The two stacks are incompatible.

---

### P0-4: `quill_mcp_client.py` Has Hardcoded Personal Absolute Paths

```python
# system/scripts/quill_mcp_client.py line 17-21
BRAIN_DIR = Path("/Users/ernesto/Library/Mobile Documents/...")
MCP_BRIDGE_PATH = "/Users/ernesto/Library/Application Support/Quill/mcp-stdio-bridge.js"
```

This script is completely non-portable. It contains a hardcoded username (`ernesto`) and a macOS-specific application support path. **Zero other users can run this.** This must use `Path(__file__).resolve()` for relative positioning.

---

## 🟠 P1 — HIGH PRIORITY (Architecture Gaps)

### P1-1: "Agent Fan-Out" Does Not Exist in Code — Only in Documentation

**GEMINI.md claims** (Tier 0.5, Section 2):
> "Rule: Maximize parallel tool calls. Never make sequential calls for independent operations."

**Reality**: The task queue is a sequential FIFO processor:

```python
# task_queue.py line 59-63 — SEQUENTIAL, not parallel
def process_next(self):
    files = sorted(list(self.pending_dir.glob("*.json")))
    if not files:
        return False
    job_file = files[0]  # ONE JOB AT A TIME
```

There is **no mechanism** for:
- Spawning multiple agents simultaneously (no `ThreadPoolExecutor`, no `asyncio.gather`, no subprocess pool)
- Decomposing a PM task into parallel sub-tasks
- Assigning sub-tasks to specific agent personas
- Collecting and synthesizing results from parallel agents
- Inter-agent communication or conflict resolution

The "fan-out" described in every `SKILL.md` as "In a SINGLE TURN" is an **LLM prompt instruction**, not executable code. It instructs the AI to make parallel tool calls in its context window — this never fans out to separate agent processes.

**To actually implement fan-out**, the system needs:
1. Task decomposition engine (WorkBreaker → sub-task graph)
2. Agent-to-skill capability registry (exists partially in `skills.json`, but incomplete)
3. Concurrent dispatch (Python `concurrent.futures.ThreadPoolExecutor` or `asyncio`)
4. Result aggregation layer (merge outputs from parallel agents)
5. Shared-state conflict resolution (two agents cannot overwrite the same tracker file)

---

### P1-2: `skills.json` Is Stale and Incorrect

`skills.json` lists **19 skills**. The `.agent/skills/` directory has **38 skill directories**. Over half of all skills are invisible to the index.

**Missing from `skills.json`** (sample):
- `communication-crafter`, `competitive-intel`, `context-retriever`
- `cover-letter-writer`, `discovery-coach`, `document-exporter`
- `okr-manager`, `prioritization-engine`, `release-manager`
- `retrospective`, `risk-guardian`, `stitch`, `visual-architect`
- `vacuum-protocol`, `ux-researcher`, `ux-collaborator`

**Wrong entry in `skills.json`**:
```json
"key-result-tracker": {
  "path": ".agent/skills/key-result-tracker/SKILL.md"
```
This skill directory does not exist. The OKR skill is `okr-manager`.

GEMINI.md's "Modular Skill Loading Protocol" says agents check the `skills:` frontmatter field and load SKILL.md files. If `skills.json` is the index, it's broken. If agents scan `.agent/skills/` directly, then `skills.json` is redundant dead weight.

---

### P1-3: Broken YAML Frontmatter on Two Skills

Both `delegation-manager/SKILL.md` and `weekly-synth/SKILL.md` are missing their **opening `---` delimiter**:

```
# delegation-manager/SKILL.md — ACTUAL CONTENT (line 1):
name: delegation-manager
description: Track delegated tasks...
triggers:
- "/delegate"
```

This is NOT valid YAML frontmatter — it's raw YAML without delimiters. Any parser that calls `content.startswith("---")` will fail. The closing `---` appears on line 12, making the content look like a malformed YAML document.

**Test proof**: `AssertionError: False is not true : delegation-manager: Missing frontmatter`

---

### P1-4: Skill Naming Inconsistencies Break Tests

| Test Expects | Actual Directory | Impact |
|-------------|-----------------|--------|
| `ux-collab` | `ux-collaborator` | `FileNotFoundError` in tests |
| `KERNEL.md` | `GEMINI.md` | `AssertionError: Missing KERNEL.md` |
| `dispatch.py` in `Beats-PM-System/system/scripts/` | `system/scripts/dispatch.py` | `AssertionError: Missing dispatch.py` |

These are all the same root cause: the codebase was refactored/renamed without updating the test fixture constants.

---

### P1-5: `system/queue/` Is Incomplete — Missing 3 Required Subdirectories

The queue design requires `pending/`, `processing/`, `completed/`, `failed/`. But:

```
system/queue/
└── failed/          ← exists (has 2 stale jobs)
    ├── 1768698081_f78272b6-...json
    └── 1768861756_b47c587f-...json
```

`pending/`, `processing/`, `completed/` **do not exist**. Workers call `.mkdir(parents=True, exist_ok=True)` at startup — but since the path itself is wrong, they've been creating directories in the ghost `Beats-PM-System/` path instead.

---

## 🟡 P2 — MEDIUM PRIORITY (Quality & Reliability)

### P2-1: PRD Author Skill Missing RICE/MoSCoW Content

`test_skills_validation.py` expects `RICE`, `User Stories`, and `Success Metrics` in `prd-author/SKILL.md`. The RICE scoring framework is referenced in the PRD template (`templates/docs/prioritization-scorecard.md`) but missing from the skill itself.

**Test proof**: `AssertionError: 'RICE' not found in prd-author SKILL.md`

---

### P2-2: `resource_warning` — Unclosed File Handle in `vacuum.py` (via Tests)

```
ResourceWarning: unclosed file <_io.TextIOWrapper
  name='.../archive_2026_test_tasks.md' mode='r'>
  # system/tests/test_vacuum.py:121
```

A file is opened for reading without a context manager (`with open(...)`). This is a resource leak that will surface under load.

---

### P2-3: Symlinks Are Absolute Paths — Fragile Across Machines

```
.claude/commands → /Users/ernesto/Library/Mobile Documents/.../beats-pm-antigravity-brain/.agent/workflows
.gemini/workflows → /Users/ernesto/Library/Mobile Documents/.../beats-pm-antigravity-brain/.agent/workflows
```

These symlinks use **absolute** personal paths. `AGENTS.md` even acknowledges this:
> "If symlinks break (common with relative paths), run `python3 system/scripts/fix_symlinks.py`"

But the real problem is `fix_symlinks.py` itself creates ABSOLUTE symlinks using `$(pwd)`. If the repository is cloned to a different machine or a different directory, all symlinks break immediately.

**`fix_symlinks.py` should use `os.path.relpath()` to create relative symlinks.**

---

### P2-4: `vibe_check.py` Reports "SETTINGS.md: CRITICAL MISSING" in Production

`vibe_check.py` checks for `SETTINGS.md` but this file is gitignored and not committed. On a fresh clone, users get a CRITICAL MISSING error without a clear "create this from template" workflow.

`system/config.json` line 21: `"settings": "SETTINGS.md"` — this file must exist for skills to function (multiple SKILL.md files say "read SETTINGS.md for product context"). New users will hit this wall immediately.

---

### P2-5: `task_queue.py` Uses a Bare `except:` That Swallows All Exceptions

```python
# task_queue.py line 71-72
try:
    job_file.rename(processing_path)
except:
    return False  # Race condition or file lock
```

A bare `except:` catches `SystemExit`, `KeyboardInterrupt`, and `MemoryError`. This is an anti-pattern. At minimum it should be `except (OSError, PermissionError)`.

---

### P2-6: `content_index.json` Is Never Auto-Updated

`GEMINI.md` mandates: "Read `system/content_index.json` to find files." But:
- `gps_indexer.py` must be **manually run** to update this index
- No workflow triggers an automatic refresh when files are created/moved
- The index would go stale immediately after any `/create`, `/prd`, or `/vacuum` run

The `turbo_dispatch` job type `gps_index` exists but nothing triggers it automatically post-write.

---

## 🟢 P3 — LOW PRIORITY (Technical Debt)

### P3-1: Agent Count Inconsistencies Across Documentation

| Source | Agent Count |
|--------|-------------|
| `AGENTS.md` | "11 agents" |
| `.agent/agents/` directory | 12 files |
| `GEMINI.md` Virtual Team table | 8 roles |

No source agrees. `AGENTS.md` has not been updated since agents were added.

### P3-2: `kernel_utils.py` Template Mapping References `.agent/templates/` Directly

```python
# kernel_utils.py line 103
"meeting_notes": ".agent/templates/meeting-notes.md",
```

But `templates/meetings/meeting-notes.md` is the actual file (inside `meetings/` subdirectory). The flat paths in `kernel_utils` don't match the real hierarchical template structure.

### P3-3: `dispatch.py` Root Path Calculation Is Off By Two Levels

```python
# dispatch.py line 18 — resolves 4 parents up from system/scripts/
ROOT_DIR = CURRENT_FILE.parent.parent.parent.parent
```

From `system/scripts/dispatch.py`, four parents resolves to: `scripts → system → brain-root → Vibe-Coding → Mobile Documents`. This is **two levels too many**. The correct brain root needs only **two** parents.

### P3-4: `perf_benchmark.py` Is a Stub — 778 Bytes of Nothing

```
system/scripts/perf_benchmark.py  # 778 chars
```

If this is aspirational, delete it. If it's needed, implement it. Stubs in a codebase that claims FAANG-level standards are not acceptable.

---

## 🚀 Implementation Roadmap — Most Efficient Path to Real Fan-Out

### Phase 1: Stop the Bleeding (1–2 days)

| # | Action | File(s) | Risk |
|---|--------|---------|------|
| 1 | Fix queue paths: `BRAIN_ROOT / "system/queue"` everywhere | `dispatch.py`, `task_queue.py`, `queue_worker.py` | Low |
| 2 | Fix test fixture paths: remove `Beats-PM-System/` ghost prefix | `test_regression.py`, `test_core_setup.py`, `test_features.py` | Low |
| 3 | Fix `KERNEL.md` → `GEMINI.md` reference in tests | `test_structure.py`, `test_regression.py` | Low |
| 4 | Fix `ux-collab` → `ux-collaborator` in tests | `test_skills_validation.py`, `test_regression.py` | Low |
| 5 | Add opening `---` to `delegation-manager/SKILL.md` and `weekly-synth/SKILL.md` | Both SKILL.md files | Low |
| 6 | Install PyYAML: `pip install pyyaml` and add to `requirements.txt` | `requirements.txt` (create if missing) | Low |
| 7 | Fix `quill_mcp_client.py` hardcoded paths | `quill_mcp_client.py` lines 17-21 | Low |

**Target**: Get the test suite from 17 failures down to 0. **Do not claim victory until `python3 -m unittest discover` shows `OK`.**

---

### Phase 2: Unify the Queue (3–5 days)

Pick ONE queue implementation and delete the other. Recommendation: keep `task_queue.py` + rename `turbo_dispatch.py` as the single path, fix the queue directory, expand `_execute_job()` to handle all job types from `queue_worker.py` too.

```python
# New unified _execute_job routing:
JOB_HANDLERS = {
    "structure_enforce": lambda p: __import__("scripts.enforce_structure").main(),
    "vacuum": lambda p: __import__("scripts.vacuum").main(),
    "optimize_skills": lambda p: __import__("scripts.optimize_skills").index_skills(),
    "gps_index": lambda p: __import__("scripts.gps_indexer").scan_files(),
    "transcript_archive": lambda p: __import__("scripts.vacuum").archive_transcripts(),
    "echo": lambda p: print(p),
}
```

---

### Phase 3: Agent Fan-Out Engine (1–2 weeks)

This is the actual cutting-edge work. The architecture requires a new layer:

```
.agent/
└── workflows/
    └── fan-out-engine.md    # New: fan-out coordinator workflow

system/scripts/
├── agent_dispatcher.py      # NEW: breaks tasks → sub-tasks, maps to agents
├── fan_out_worker.py        # NEW: ThreadPoolExecutor-based parallel runner
└── result_synthesizer.py    # NEW: merges outputs from parallel agents
```

**`agent_dispatcher.py` design:**
```python
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

AGENT_SKILLS = {
    "staff-pm": ["task-manager", "prd-author", "meeting-synth"],
    "program-manager": ["dependency-tracker", "release-manager", "retrospective"],
    "data-scientist": ["data-analytics"],
    "ux-researcher": ["ux-researcher", "ux-collaborator"],
    "strategist": ["chief-strategy-officer", "competitive-intel", "okr-manager"],
}

def fan_out(task: dict, agents: list[str]) -> list[dict]:
    """Dispatch task to multiple agents in parallel, collect results."""
    with ThreadPoolExecutor(max_workers=len(agents)) as executor:
        futures = {executor.submit(invoke_agent, agent, task): agent for agent in agents}
        results = []
        for future in as_completed(futures):
            agent = futures[future]
            result = future.result()
            results.append({"agent": agent, "output": result})
    return results
```

**The `GEMINI.md` Request Classifier table already defines the routing logic** — it just needs to be turned into code:

```python
CLASSIFIER_ROUTES = {
    ("plan", "roadmap", "vision"):          ["cpo", "strategist"],
    ("track", "task", "jira"):              ["staff-pm"],
    ("draft", "write", "spec", "prd"):      ["staff-pm"],
    ("data", "metrics", "growth"):          ["data-scientist"],
    ("dependency", "release", "retro"):     ["program-manager", "staff-pm"],
}
```

---

### Phase 4: Skills Registry Repair (1 day)

Run `python3 system/scripts/optimize_skills.py` THEN verify `skills.json` is regenerated correctly from the 38 actual skill directories. Delete the hardcoded `key-result-tracker` entry. Add all missing skills.

If `optimize_skills.py` doesn't regenerate `skills.json` properly, it needs to be fixed to scan `.agent/skills/` and write accurate entries.

---

### Phase 5: Fix Symlinks to Use Relative Paths (2 hours)

Replace hardcoded absolute symlinks with relative ones:

```bash
# system/scripts/fix_symlinks.py — should use:
os.symlink(
    os.path.relpath(".agent/workflows", start=".kilocode"),
    ".kilocode/workflows"
)
```

---

## Summary Scorecard

| Category | Score | Evidence |
|----------|-------|----------|
| Test Suite | ❌ 0/5 | 17 failures, 12 errors |
| Queue Infrastructure | ❌ 1/5 | Two broken implementations, wrong paths, stale jobs |
| Agent Fan-Out | ❌ 0/5 | Does not exist — aspirational documentation only |
| Skills Registry | ⚠️ 2/5 | 19/38 skills indexed; 1 wrong key |
| Skill Quality | ⚠️ 3/5 | 2 broken frontmatters; PRD missing RICE |
| Symlinks | ⚠️ 3/5 | Work on current machine; break on clone |
| Documentation | ✅ 4/5 | GEMINI.md is thorough and well-structured |
| Portability | ❌ 1/5 | Hardcoded absolute paths; ghost directory refs |

**Overall: 14/40 — Do not ship.**

---

*The documentation architecture is excellent. The code that's supposed to execute it is broken. Fix the tests first so you can verify each fix as you make it.*
