# Highlighted Agent Skills Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Review every highlighted Claude/Codex skill listed in this plan, verify the original source link, and add the qualified entries to this repository with clear categories, brief descriptions, and install instructions.

**Architecture:** Keep the public catalog Markdown-first and easy to browse, but require each new entry to carry four pieces of evidence: original source link, category, short purpose, and installation path. New skills should be organized in `SKILLS.md` under the closest existing category, while any future category split should preserve `README.md`, `SKILLS.md`, and `CURATION.md` as the public entry points.

**Tech Stack:** Markdown, GitHub CLI, GitHub API, `npx skills`, HTTP link checks, and manual source review of each `SKILL.md` or upstream documentation page.

---

## Non-Negotiable Repository Rules

- Keep every repository file in English.
- Use original skill links, not only aggregator links.
- Add a brief "what it is" description for every skill.
- Add an install command or explicit installation note for every skill.
- Validate links before committing.
- Commit and push to `main` after the review is complete.

## Target Categories

Use these categories when adding the highlighted skills:

| Category | Purpose |
|---|---|
| Refactoring & Code Quality | Architecture cleanup, code hygiene, DDD, maintainability, PR risk, and entropy control. |
| Agents & Engineering Workflows | TDD, multi-agent execution, planning, issue creation, skeptical design review, and workflow orchestration. |
| UI, Design & Frontend | Official UI design skills, accessibility review, design-to-code flows, variants, and Tailwind-friendly output. |
| Security & Quality | OWASP, secret safety, destructive git protection, secure defaults, and autonomous workflow guardrails. |
| Python Architecture & Systems | Clean architecture, full-stack systems, FastAPI/Python relevance, graph memory, and long-term codebase context. |

## Required Entry Format

Every added skill must follow this data shape in the catalog:

| Skill | Original link | Category | What it is | Install |
|---|---|---|---|---|
| `skill-name` | `original source URL` | `Category Name` | One sentence explaining the practical use. | `npx skills add owner/repo --skill skill-name` |

If a source does not support `npx skills add`, use one of these installation notes:

- `Manual: copy the upstream SKILL.md into .claude/skills/<skill-name>/SKILL.md`
- `Bundle: install the upstream collection, then enable this skill from the bundle`
- `Verify upstream install instructions before adding`

Do not invent install commands. When in doubt, mark the entry as `Verify upstream install instructions before adding` and keep it out of "Top Picks" until verified.

## Candidate Skills To Review

### Refactoring & Code Quality

| Candidate | Source to verify | Expected original link | Category | Planned description | Planned install |
|---|---|---|---|---|---|
| `improve-codebase-architecture` | `mattpocock/skills` | https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture | Refactoring & Code Quality | Analyzes shallow modules and coupled code clusters, then proposes testable architecture boundaries and refactor RFCs. | `npx skills add mattpocock/skills --skill improve-codebase-architecture` |
| `hone` collection | `cdd.dev/skills/hone` | https://cdd.dev/skills/hone | Refactoring & Code Quality | Code hygiene cadence for method brevity, naming clarity, duplication, magic numbers, and test naming. | Verify upstream install instructions before adding |
| `swe` collection | `cdd.dev/skill/` | https://cdd.dev/skill/ | Refactoring & Code Quality | SWE skill suite for PR risk, performance audits, security audits, ownership maps, refactor opportunities, and incident follow-up. | `npx skills install ckorhonen/swe-skills` |
| `systematic-debugging` | `obra/superpowers` via aggregators | https://github.com/obra/superpowers/tree/main/skills/systematic-debugging | Refactoring & Code Quality | Forces evidence-based debugging before proposing fixes for bugs, test failures, or unexpected behavior. | `npx skills add obra/superpowers --skill systematic-debugging` |

### Agents & Engineering Workflows

| Candidate | Source to verify | Expected original link | Category | Planned description | Planned install |
|---|---|---|---|---|---|
| `tdd` | `mattpocock/skills` | https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd | Agents & Engineering Workflows | Enforces a real red-green-refactor loop with behavior-focused tests and one vertical slice at a time. | `npx skills add mattpocock/skills --skill tdd` |
| `grill-me` | `mattpocock/skills` | https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me | Agents & Engineering Workflows | Makes the agent interrogate a plan until every important decision branch is resolved before coding. | `npx skills add mattpocock/skills --skill grill-me` |
| `subagent-driven-development` | `obra/superpowers` via aggregators | https://github.com/obra/superpowers/tree/main/skills/subagent-driven-development | Agents & Engineering Workflows | Dispatches independent subagents per task with review checkpoints between iterations. | `npx skills add obra/superpowers --skill subagent-driven-development` |
| `to-issues` | `mattpocock/skills` | https://github.com/mattpocock/skills/tree/main/skills/engineering/to-issues | Agents & Engineering Workflows | Breaks plans, specs, or PRDs into independent GitHub issues by vertical slice. | `npx skills add mattpocock/skills --skill to-issues` |
| `to-prd` | `mattpocock/skills` | https://github.com/mattpocock/skills/tree/main/skills/engineering/to-prd | Agents & Engineering Workflows | Converts conversation context into a PRD and prepares it for GitHub issue creation. | `npx skills add mattpocock/skills --skill to-prd` |

### UI, Design & Frontend

| Candidate | Source to verify | Expected original link | Category | Planned description | Planned install |
|---|---|---|---|---|---|
| `frontend-design` | `anthropics/skills` | https://github.com/anthropics/skills/tree/main/skills/frontend-design | UI, Design & Frontend | Official Anthropic skill for purpose-driven frontend design before implementation. | `npx skills add anthropics/skills --skill frontend-design` |
| `web-design-guidelines` | `vercel-labs/agent-skills` | https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines | UI, Design & Frontend | Reviews UI code against web interface rules for accessibility, performance, focus states, labels, and touch targets. | `npx skills add vercel-labs/agent-skills --skill web-design-guidelines` |
| `Stitch UI Bundle` | `rohitg00/awesome-claude-code-toolkit` | https://github.com/rohitg00/awesome-claude-code-toolkit | UI, Design & Frontend | Discovery bundle for brief-to-screen, variants, and Tailwind-friendly UI workflows using Stitch-related tooling. | Bundle: install the upstream collection, then enable the relevant Stitch/UI skill |

### Security & Quality

| Candidate | Source to verify | Expected original link | Category | Planned description | Planned install |
|---|---|---|---|---|---|
| `owasp-security` | `agamm/claude-code-owasp` via aggregators | https://github.com/agamm/claude-code-owasp | Security & Quality | OWASP-focused Claude Code skill with review checklists, secure patterns, and language-specific security quirks. | `npx skills add agamm/claude-code-owasp` |
| `git-guardrails-claude-code` | `mattpocock/skills` | https://github.com/mattpocock/skills/tree/main/skills/misc/git-guardrails-claude-code | Security & Quality | Prevents destructive git operations such as force push, hard reset, and clean before autonomous execution. | `npx skills add mattpocock/skills --skill git-guardrails-claude-code` |
| `varlock-claude-skill` | `wrsmith108/varlock-claude-skill` via VoltAgent/BehiSecc | https://github.com/wrsmith108/varlock-claude-skill | Security & Quality | Keeps secrets and environment variables out of Claude sessions, terminals, logs, and commits. | `npx skills add wrsmith108/varlock-claude-skill` |

### Python Architecture & Systems

| Candidate | Source to verify | Expected original link | Category | Planned description | Planned install |
|---|---|---|---|---|---|
| `software-architecture` | Aggregator entry to verify | Verify original source before adding | Python Architecture & Systems | Clean Architecture, SOLID, design-pattern, and decision-framework support for Python, FastAPI, Go, GraphQL, React, and Postgres systems. | Verify upstream install instructions before adding |
| `data-structure-protocol` | `k-kolomeitsev/data-structure-protocol` | https://github.com/k-kolomeitsev/data-structure-protocol | Python Architecture & Systems | Graph-based long-term memory for coding agents, improving context retrieval and safer refactors. | `npx skills add k-kolomeitsev/data-structure-protocol` |
| `claude-skills` full-stack collection | `Jeffallan/claude-skills` | https://github.com/Jeffallan/claude-skills | Python Architecture & Systems | Full-stack skill collection covering React, NestJS, Python, DevOps, and many framework workflows. | Bundle: install the upstream collection, then enable the relevant framework skills |

## Key Sources To Explore

| Source | Verified link | Notes |
|---|---|---|
| mattpocock/skills | https://github.com/mattpocock/skills | High-signal engineering discipline skills including architecture, TDD, planning, and git guardrails. |
| cdd.dev hone | https://cdd.dev/skills/hone | Validate the page and installation path before adding any hone entry to the catalog. |
| cdd.dev SWE skills | https://cdd.dev/skill/ | Public SWE skills page with install command and named `swe:` workflows. |
| ComposioHQ Awesome Claude Skills | https://github.com/ComposioHQ/awesome-claude-skills | Aggregator for discovery, not a substitute for original links. |
| BehiSecc Awesome Claude Skills | https://github.com/BehiSecc/awesome-claude-skills | Aggregator for discovery, not a substitute for original links. |
| Anthropic Skills | https://github.com/anthropics/skills | Official Claude skills source. |
| Vercel Agent Skills | https://github.com/vercel-labs/agent-skills | Official Vercel agent skills collection. |
| VoltAgent Awesome Agent Skills | https://github.com/VoltAgent/awesome-agent-skills | Large cross-agent discovery index. |
| rohitg00 Awesome Claude Code Toolkit | https://github.com/rohitg00/awesome-claude-code-toolkit | Broad toolkit and discovery source for Claude Code agents, skills, hooks, commands, and plugins. |

## Implementation Tasks

### Task 1: Verify Original Sources

**Files:**
- Validate: `SKILLS.md`
- Validate: upstream source pages listed above

- [ ] **Step 1: Check each GitHub repository**

```bash
for repo in \
  mattpocock/skills \
  anthropics/skills \
  vercel-labs/agent-skills \
  agamm/claude-code-owasp \
  wrsmith108/varlock-claude-skill \
  k-kolomeitsev/data-structure-protocol \
  Jeffallan/claude-skills \
  rohitg00/awesome-claude-code-toolkit \
  VoltAgent/awesome-agent-skills \
  ComposioHQ/awesome-claude-skills \
  BehiSecc/awesome-claude-skills
do
  gh repo view "$repo" --json nameWithOwner,description,stargazerCount,url
done
```

Expected: every repository resolves. If a repository does not resolve, do not add entries from it until a replacement original link is found.

- [ ] **Step 2: Check each expected skill path**

```bash
for path in \
  skills/engineering/improve-codebase-architecture \
  skills/engineering/tdd \
  skills/productivity/grill-me \
  skills/engineering/to-issues \
  skills/engineering/to-prd \
  skills/misc/git-guardrails-claude-code
do
  gh api "repos/mattpocock/skills/contents/$path" --jq '.[].name'
done
```

Expected: each path lists a `SKILL.md` or equivalent skill files.

- [ ] **Step 3: Verify non-GitHub sources**

```bash
python3 - <<'PY'
from urllib.request import Request, urlopen

for url in [
    "https://cdd.dev/skills/hone",
    "https://cdd.dev/skill/",
]:
    request = Request(url, method="GET", headers={"User-Agent": "catalog-check"})
    with urlopen(request, timeout=15) as response:
        print(response.status, response.geturl())
PY
```

Expected: both URLs return an HTTP status below 400. If `hone` resolves to a generic page rather than a specific skill page, mark it as "needs source confirmation" instead of adding it as a verified skill.

### Task 2: Decide What To Add

**Files:**
- Modify: `SKILLS.md`
- Modify: `CURATION.md` only if curation rules need clearer install/source requirements

- [ ] **Step 1: Classify every candidate**

Use this classification:

| Status | Rule |
|---|---|
| `add` | Original link verified, purpose clear, install path clear enough. |
| `add-as-collection` | Useful collection, but individual skill names inside must be selected later. |
| `watchlist` | Useful signal, but original link or install path needs more validation. |
| `reject` | No original source, unclear scope, dead link, or unsafe automation. |

- [ ] **Step 2: Record rejected or watchlist entries**

If a candidate is not added to `SKILLS.md`, add a short note in the commit message body or final report explaining why.

### Task 3: Add Catalog Entries

**Files:**
- Modify: `SKILLS.md`

- [ ] **Step 1: Add Refactoring & Code Quality entries**

Add verified entries for:

- `improve-codebase-architecture`
- `hone` collection only if its original page and install path are verified
- `swe` collection
- `systematic-debugging` if not already present with the correct original link

- [ ] **Step 2: Add Agents & Engineering Workflows entries**

Add verified entries for:

- `tdd`
- `grill-me`
- `subagent-driven-development`
- `to-issues`
- `to-prd`

- [ ] **Step 3: Add UI, Design & Frontend entries**

Add verified entries for:

- `frontend-design` if not already present with the correct original link
- `web-design-guidelines`
- `Stitch UI Bundle` only if the exact upstream skill or bundle path is verified

- [ ] **Step 4: Add Security & Quality entries**

Add verified entries for:

- `owasp-security`
- `git-guardrails-claude-code`
- `varlock-claude-skill`

- [ ] **Step 5: Add Python Architecture & Systems entries**

Add verified entries for:

- `software-architecture` only after the original source is verified
- `data-structure-protocol`
- `claude-skills` full-stack collection

### Task 4: Add Installation Guidance

**Files:**
- Modify: `SKILLS.md`

- [ ] **Step 1: Extend the table shape or add an installation section**

Use one of these approaches:

1. Add an `Install` column to every table in `SKILLS.md`.
2. Keep existing tables unchanged and add a new section named `Installation Notes` with a table for highlighted skills.

Recommended: add a dedicated `Installation Notes` section first, because it avoids rewriting all existing 108 rows.

- [ ] **Step 2: Add this table shape**

```markdown
## Installation Notes

| Skill | Install |
|---|---|
| improve-codebase-architecture | `npx skills add mattpocock/skills --skill improve-codebase-architecture` |
```

Expected: every newly added highlighted skill has an installation command or a clear verification note.

### Task 5: Validate The Catalog

**Files:**
- Validate: `README.md`
- Validate: `SKILLS.md`
- Validate: `CURATION.md`
- Validate: `SKILL_EXPANSION_PLAN.md`

- [ ] **Step 1: Verify no non-English text was introduced**

```bash
rg -n "[^\\x00-\\x7F]" .
```

Expected: no results, except project names or external URLs that intentionally contain non-ASCII characters. Also manually review changed prose for English-only wording.

- [ ] **Step 2: Verify links**

```bash
python3 - <<'PY'
from pathlib import Path
import re
import urllib.error
import urllib.request

text = "\n".join(Path(path).read_text() for path in ["README.md", "SKILLS.md", "CURATION.md", "SKILL_EXPANSION_PLAN.md"])
links = sorted(set(re.findall(r"https?://[^\s)>\"`]+", text)))
failed = []
for link in links:
    request = urllib.request.Request(link, method="HEAD", headers={"User-Agent": "catalog-link-check"})
    try:
        with urllib.request.urlopen(request, timeout=12) as response:
            code = response.status
    except urllib.error.HTTPError as exc:
        if exc.code in (403, 405):
            try:
                request = urllib.request.Request(link, method="GET", headers={"User-Agent": "catalog-link-check"})
                with urllib.request.urlopen(request, timeout=12) as response:
                    code = response.status
            except Exception as retry_exc:
                failed.append((link, type(retry_exc).__name__, str(retry_exc)[:120]))
                continue
        else:
            failed.append((link, "HTTPError", str(exc.code)))
            continue
    except Exception as exc:
        failed.append((link, type(exc).__name__, str(exc)[:120]))
        continue
    if code >= 400:
        failed.append((link, "status", str(code)))

print(f"checked={len(links)} failed={len(failed)}")
for item in failed:
    print("|".join(item))
raise SystemExit(1 if failed else 0)
PY
```

Expected: `failed=0`.

- [ ] **Step 3: Verify duplicate names**

```bash
python3 - <<'PY'
from pathlib import Path

names = []
for line in Path("SKILLS.md").read_text().splitlines():
    if not line.startswith("|") or line.startswith("|---") or line.startswith("| Skill"):
        continue
    parts = [part.strip() for part in line.strip("|").split("|")]
    if len(parts) >= 3:
        names.append(parts[0])

seen = set()
duplicates = []
for name in names:
    if name in seen and name not in duplicates:
        duplicates.append(name)
    seen.add(name)

print("entries=" + str(len(names)))
print("duplicates=" + str(len(duplicates)))
for duplicate in duplicates:
    print(duplicate)
raise SystemExit(1 if duplicates else 0)
PY
```

Expected: `duplicates=0`.

### Task 6: Commit And Push

**Files:**
- Commit: `SKILLS.md`
- Commit: `CURATION.md` if changed
- Commit: `SKILL_EXPANSION_PLAN.md`

- [ ] **Step 1: Review status and diff**

```bash
git status --short --branch
git diff --stat
git diff -- SKILLS.md CURATION.md SKILL_EXPANSION_PLAN.md
```

Expected: only intended catalog and plan changes are present.

- [ ] **Step 2: Stage files explicitly**

```bash
git add SKILLS.md CURATION.md SKILL_EXPANSION_PLAN.md
```

Expected: only intended files are staged.

- [ ] **Step 3: Commit**

```bash
git commit -m "docs: plan highlighted skills expansion"
```

Expected: commit succeeds.

- [ ] **Step 4: Push**

```bash
git push origin main
```

Expected: `main` is updated on GitHub.

- [ ] **Step 5: Confirm remote state**

```bash
git status --short --branch
git rev-parse HEAD
git rev-parse origin/main
git ls-remote origin refs/heads/main
```

Expected: worktree is clean and all three SHAs match.

## Acceptance Checklist

- [ ] Every cited skill or collection has been reviewed.
- [ ] Every added entry uses the original source link.
- [ ] Every added entry has a brief English description.
- [ ] Every added entry has an install command or explicit installation note.
- [ ] Unverified aggregator-only items are marked as watchlist or omitted.
- [ ] The repository remains English-only.
- [ ] Link checks pass.
- [ ] Duplicate checks pass.
- [ ] Changes are committed and pushed to `main`.
