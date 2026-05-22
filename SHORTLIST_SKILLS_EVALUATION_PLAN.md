# Shortlist Skills Evaluation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Evaluate the shortlisted repositories, packs, and skills below; remove duplicates against the current catalog; and add only new or meaningfully distinct skills using the repository standard: original link, short purpose, and install guidance.

**Architecture:** Keep `README.md`, `SKILLS.md`, and `CURATION.md` as the public entry points. Add new entries to the closest existing `SKILLS.md` section first, and add a dedicated `Installation Notes` section if the new entries need install commands without rewriting every existing row. Treat aggregator repositories as discovery indexes, not as original sources.

**Tech Stack:** Markdown, GitHub CLI, GitHub API, official skill directories, `npx skills`, Claude plugin marketplace links, link checking with Python standard library, and Git.

---

## Repository Rules

- Keep every file in English.
- Do not add a skill twice under the same name and source.
- Prefer original source links over aggregator links.
- If two sources provide the same skill name, either choose the stronger source or qualify the name with the source.
- Every new entry must include a short English description.
- Every new highlighted entry must include an install command or explicit installation note.
- Validate links, duplicates, and language before committing.
- Commit and push after the final review.

## Implementation Decision Log

Implemented on 2026-05-22 after verifying repository metadata, skill paths, public pages, install commands, duplicates, language, and links.

| Candidate group | Decision | Result |
|---|---|---|
| Addy Osmani Agent Skills pack | `add` | Added as a pack-level Software Engineering entry. |
| Addy `code-simplification`, `incremental-implementation`, `code-review-and-quality`, `debugging-and-error-recovery`, `api-and-interface-design`, `deprecation-and-migration`, `context-engineering`, `source-driven-development`, `doubt-driven-development`, `planning-and-task-breakdown`, `frontend-ui-engineering`, `browser-testing-with-devtools` | `add` | Added to the closest catalog categories with original GitHub links. |
| Addy `test-driven-development` | `add-source-qualified` | Added as `addy-test-driven-development` because `test-driven-development` already exists from Superpowers. |
| Addy `/code-simplify` | `add-install-note-only` | Added as an installation note because it is a command in the Addy pack, not a separate catalog row. |
| Superpowers `subagent-driven-development` | `add` | Added as a specific workflow entry. |
| Superpowers `systematic-debugging` | `add-install-note-only` | Already existed; not duplicated. |
| GStack pack and commands `/review`, `/plan-eng-review`, `/codex`, `/design-review`, `/plan-design-review` | `add` | Added as source-qualified GStack entries. |
| alirezarezvani pack and `senior-architect`, `api-design-reviewer`, `migration-architect`, `observability-designer`, `pr-review-expert`, `skill-security-auditor` | `add` | Added with original GitHub links and Codex install guidance. |
| OpenAI `figma-implement-design`, `security-best-practices`, `security-threat-model`, `playwright`, `screenshot` | `add-install-note-only` | Already existed; install notes were added without duplicate rows. |
| OpenAI `frontend-skill` | `add` | Added from the official skill page with verified install guidance. |
| Browserbase `ui-test` | `add` | Added as `browserbase-ui-test` with verified official page and install guidance. |
| `pyright-lsp` plugin | `add` | Added as a plugin entry because the public plugin page and install path resolved. |
| Google Stitch `design-md`, `react-components`, `shadcn-ui`, `stitch-loop` | `watchlist` | Official pages resolved, but the public GitHub install targets returned 404 during link validation, so they were not added to `SKILLS.md`. |
| Codex GitHub code review | `watchlist` | Kept out of `SKILLS.md` because it is a platform capability, not a standalone skill with a catalog-ready install path. |

## Current Catalog Baseline

The current catalog already includes these relevant entries:

| Already in `SKILLS.md` | Source currently used | Deduplication impact |
|---|---|---|
| `openai/skills` entries | OpenAI Skills | Do not re-add `figma-implement-design`, `security-best-practices`, `security-threat-model`, `playwright`, or `screenshot` unless adding install notes. |
| `test-driven-development` | `obra/superpowers` | Addy's `test-driven-development` must be treated as a source-qualified alternative, not a duplicate replacement. |
| `systematic-debugging` | `obra/superpowers` | Do not add aggregator duplicates from Awesome Agent Skills. |
| `subagent-driven-development` | Not currently listed by name | Add from `obra/superpowers` if verified. |
| `frontend-design` | `anthropics/skills` | Keep Anthropic as canonical; do not add aggregator duplicates. |
| `Vercel Agent Skills` | `vercel-labs/agent-skills` | Add `web-design-guidelines` as a specific skill if verified. |
| `Awesome Agent Skills` | `VoltAgent/awesome-agent-skills` | Keep as discovery index only; do not use it as the original link for individual skills. |

## Priority Repository Review

Verify these repositories before changing `SKILLS.md`. Star counts are volatile and must be refreshed during implementation.

| Priority | Repository / pack | Verified source | Why it matters | Catalog action |
|---:|---|---|---|---|
| 1 | Addy Osmani Agent Skills | https://github.com/addyosmani/agent-skills | Production-grade engineering skills for specs, planning, incremental implementation, TDD, review, simplification, frontend, APIs, security, performance, ADRs, and shipping. | Add new high-impact skills that are not already covered. |
| 2 | OpenAI Skills | https://github.com/openai/skills | Canonical Codex source for Figma, frontend, security, threat modeling, Playwright, screenshots, and documents. | Keep existing entries; add install notes and missing official skills only. |
| 3 | Superpowers | https://github.com/obra/superpowers | Disciplined workflow layer for spec, plan, TDD, subagents, and verification. | Add missing specific workflow entries such as `subagent-driven-development`. |
| 4 | GStack | https://github.com/garrytan/gstack | Opinionated virtual team with engineering review, design review, QA, shipping, benchmarks, security officer, and Codex second opinion. | Add as a collection and add key slash-command entries if useful. |
| 5 | alirezarezvani/claude-skills | https://github.com/alirezarezvani/claude-skills | Large multi-tool library for architecture, PR review, migrations, observability, CI/CD, MCP, and skill auditing. | Add verified engineering skills and the collection entry. |
| 6 | Anthropic Skills | https://github.com/anthropics/skills | Official Claude source and canonical structure reference. | Keep as canonical for official Claude entries. |
| 7 | VoltAgent and Composio discovery indexes | https://github.com/VoltAgent/awesome-agent-skills and https://github.com/ComposioHQ/awesome-claude-skills | Broad discovery indexes for Claude, Codex, Gemini CLI, Cursor, and community skills. | Use only for discovery; verify original links before adding. |

## Candidate Skills By Objective

### Refactoring And Code Quality

| Candidate | Original source to verify | Current catalog status | Planned action | Install guidance |
|---|---|---|---|---|
| `code-simplification` | https://github.com/addyosmani/agent-skills/tree/main/skills/code-simplification | New | Add under Software Engineering or Refactoring & Code Quality. | `npx skills add addyosmani/agent-skills --skill code-simplification` |
| `code-simplify` command | https://github.com/addyosmani/agent-skills | New command reference | Mention in installation notes if the upstream README confirms the command. | Install Addy pack, then use `/code-simplify`. |
| `test-driven-development` | https://github.com/addyosmani/agent-skills/tree/main/skills/test-driven-development | Name exists from Superpowers | Add only as `Addy test-driven-development` or keep as install note if source-qualified entry is useful. | `npx skills add addyosmani/agent-skills --skill test-driven-development` |
| `incremental-implementation` | https://github.com/addyosmani/agent-skills/tree/main/skills/incremental-implementation | New | Add for safe vertical-slice implementation. | `npx skills add addyosmani/agent-skills --skill incremental-implementation` |
| `code-review-and-quality` | https://github.com/addyosmani/agent-skills/tree/main/skills/code-review-and-quality | New | Add for pre-merge risk and quality review. | `npx skills add addyosmani/agent-skills --skill code-review-and-quality` |
| `pr-review-expert` | https://github.com/alirezarezvani/claude-skills/tree/main/engineering/skills/pr-review-expert | New | Add for large PR review, blast-radius analysis, security scan, and coverage deltas. | Manual or `npx agent-skills-cli add alirezarezvani/claude-skills --agent codex` after verification. |
| GStack `/review` | https://github.com/garrytan/gstack/tree/main/review | New command entry | Add as GStack command if the catalog supports command-style entries. | Install GStack, then use `/review`. |
| Codex GitHub code review | https://developers.openai.com/codex/integrations/github | New platform capability | Add as platform capability, not as a skill, if it fits curation rules. | Configure Codex GitHub integration. |
| `debugging-and-error-recovery` | https://github.com/addyosmani/agent-skills/tree/main/skills/debugging-and-error-recovery | New | Add as Addy's debugging complement; keep Superpowers `systematic-debugging` unchanged. | `npx skills add addyosmani/agent-skills --skill debugging-and-error-recovery` |
| `systematic-debugging` | https://github.com/obra/superpowers/tree/main/skills/systematic-debugging | Already present | Do not duplicate; optionally add install note. | `npx skills add obra/superpowers --skill systematic-debugging` |

### Python Architecture, Backend, And Large Systems

| Candidate | Original source to verify | Current catalog status | Planned action | Install guidance |
|---|---|---|---|---|
| `senior-architect` | https://github.com/alirezarezvani/claude-skills/tree/main/engineering-team/skills/senior-architect | New | Add for architecture trade-offs, boundaries, and system design. | Manual or `npx agent-skills-cli add alirezarezvani/claude-skills --agent codex` after verification. |
| `api-and-interface-design` | https://github.com/addyosmani/agent-skills/tree/main/skills/api-and-interface-design | New | Add for API contracts, module boundaries, versioning, payloads, and ergonomics. | `npx skills add addyosmani/agent-skills --skill api-and-interface-design` |
| `api-design-reviewer` | https://github.com/alirezarezvani/claude-skills/tree/main/engineering/skills/api-design-reviewer | New | Add for reviewing existing REST APIs and breaking changes. | Manual or `npx agent-skills-cli add alirezarezvani/claude-skills --agent codex` after verification. |
| `migration-architect` | https://github.com/alirezarezvani/claude-skills/tree/main/engineering/skills/migration-architect | New | Add for framework, database, dependency, and legacy migration planning. | Manual or `npx agent-skills-cli add alirezarezvani/claude-skills --agent codex` after verification. |
| `deprecation-and-migration` | https://github.com/addyosmani/agent-skills/tree/main/skills/deprecation-and-migration | New | Add as transition, compatibility, deprecation, and rollback discipline. | `npx skills add addyosmani/agent-skills --skill deprecation-and-migration` |
| `observability-designer` | https://github.com/alirezarezvani/claude-skills/tree/main/engineering/skills/observability-designer | New | Add for logs, metrics, traces, alerts, health checks, and diagnosis. | Manual or `npx agent-skills-cli add alirezarezvani/claude-skills --agent codex` after verification. |
| `security-best-practices` | https://github.com/openai/skills/tree/main/skills/.curated/security-best-practices | Already present | Do not duplicate; add install note if needed. | `npx skills add openai/skills --skill security-best-practices` |
| `security-threat-model` | https://github.com/openai/skills/tree/main/skills/.curated/security-threat-model | Already present | Do not duplicate; add install note if needed. | `npx skills add openai/skills --skill security-threat-model` |
| `pyright-lsp` plugin | https://claude.com/plugins/pyright-lsp | New plugin, not a skill | Add to an optional "Plugins" section only if plugin entries are accepted. | `/plugin install pyright-lsp@claude-plugins-official` |

### Agent Skills And Autonomous Execution

| Candidate | Original source to verify | Current catalog status | Planned action | Install guidance |
|---|---|---|---|---|
| `subagent-driven-development` | https://github.com/obra/superpowers/tree/main/skills/subagent-driven-development | New specific entry | Add under Software Engineering or AI Architecture. | `npx skills add obra/superpowers --skill subagent-driven-development` |
| `context-engineering` | https://github.com/addyosmani/agent-skills/tree/main/skills/context-engineering | New | Add for collecting the right context before coding. | `npx skills add addyosmani/agent-skills --skill context-engineering` |
| `source-driven-development` | https://github.com/addyosmani/agent-skills/tree/main/skills/source-driven-development | New | Add for grounding framework decisions in official sources. | `npx skills add addyosmani/agent-skills --skill source-driven-development` |
| `doubt-driven-development` | https://github.com/addyosmani/agent-skills/tree/main/skills/doubt-driven-development | New | Add for reducing hallucination through explicit doubt and verification. | `npx skills add addyosmani/agent-skills --skill doubt-driven-development` |
| `planning-and-task-breakdown` | https://github.com/addyosmani/agent-skills/tree/main/skills/planning-and-task-breakdown | New | Add for turning large requests into reviewable implementation plans. | `npx skills add addyosmani/agent-skills --skill planning-and-task-breakdown` |
| GStack `/plan-eng-review` | https://github.com/garrytan/gstack/tree/main/plan-eng-review | New command entry | Add if command-style virtual-team entries are accepted. | Install GStack, then use `/plan-eng-review`. |
| GStack `/codex` | https://github.com/garrytan/gstack/tree/main/codex | New command entry | Add as cross-model second-opinion workflow. | Install GStack, then use `/codex`. |
| `skill-security-auditor` | https://github.com/alirezarezvani/claude-skills/tree/main/engineering/skills/skill-security-auditor | New | Add as a pre-install security reviewer for third-party skills. | Manual or `npx agent-skills-cli add alirezarezvani/claude-skills --agent codex` after verification. |

### UI, Design, Figma, And Visual Review

| Candidate | Original source to verify | Current catalog status | Planned action | Install guidance |
|---|---|---|---|---|
| `figma-implement-design` | https://github.com/openai/skills/tree/main/skills/.curated/figma-implement-design | Already present | Do not duplicate; add install note if needed. | `npx skills add openai/skills --skill figma-implement-design` |
| `frontend-skill` | https://officialskills.sh/openai/skills/frontend-skill | New if original source resolves | Add only after verifying why it is not exposed in the OpenAI GitHub tree. | Verify official install command before adding. |
| `frontend-ui-engineering` | https://github.com/addyosmani/agent-skills/tree/main/skills/frontend-ui-engineering | New | Add for frontend components, states, responsiveness, accessibility, and integration. | `npx skills add addyosmani/agent-skills --skill frontend-ui-engineering` |
| GStack `/design-review` | https://github.com/garrytan/gstack/tree/main/design-review | New command entry | Add for real-site visual audits, fixes, and before/after screenshots. | Install GStack, then use `/design-review`. |
| GStack `/plan-design-review` | https://github.com/garrytan/gstack/tree/main/plan-design-review | New command entry | Add for design plan review before implementation. | Install GStack, then use `/plan-design-review`. |
| `browser-testing-with-devtools` | https://github.com/addyosmani/agent-skills/tree/main/skills/browser-testing-with-devtools | New | Add for browser runtime inspection with DevTools. | `npx skills add addyosmani/agent-skills --skill browser-testing-with-devtools` |
| `playwright` | https://github.com/openai/skills/tree/main/skills/.curated/playwright | Already present | Do not duplicate; add install note if needed. | `npx skills add openai/skills --skill playwright` |
| `screenshot` | https://github.com/openai/skills/tree/main/skills/.curated/screenshot | Already present | Do not duplicate; add install note if needed. | `npx skills add openai/skills --skill screenshot` |
| Browserbase `ui-test` | https://officialskills.sh/browserbase/skills/ui-test | New if source resolves | Add as browser UI testing entry if original skill page is accepted. | Verify official install command before adding. |
| Google Stitch `design-md` | https://officialskills.sh/google-labs-code/skills/design-md | New if source resolves | Add as optional Stitch skill for design documentation. | Verify official install command before adding. |
| Google Stitch `react-components` | https://officialskills.sh/google-labs-code/skills/react-components | New if source resolves | Add as optional Stitch skill for React component generation. | Verify official install command before adding. |
| Google Stitch `shadcn-ui` | https://officialskills.sh/google-labs-code/skills/shadcn-ui | New if source resolves | Add as optional Stitch skill for shadcn/ui workflows. | Verify official install command before adding. |
| Google Stitch `stitch-loop` | https://officialskills.sh/google-labs-code/skills/stitch-loop | New if source resolves | Add as optional Stitch iterative design-to-code loop. | Verify official install command before adding. |

## Recommended Starting Stack

After deduplication, prefer this lean first wave for Python, product, and UI teams:

| Layer | Skills |
|---|---|
| Week 1: Quality and refactoring | `code-simplification`, `test-driven-development`, `incremental-implementation`, `code-review-and-quality`, `debugging-and-error-recovery`, `pr-review-expert` |
| Week 2: Python/backend architecture | `senior-architect`, `api-and-interface-design`, `api-design-reviewer`, `migration-architect`, `observability-designer`, `security-best-practices`, `security-threat-model` |
| Week 3: Agent workflow | `planning-and-task-breakdown`, `context-engineering`, `source-driven-development`, `doubt-driven-development`, `subagent-driven-development` |
| Week 4: UI/design | `figma-implement-design`, `frontend-skill`, `frontend-ui-engineering`, `design-review`, `browser-testing-with-devtools`, `playwright`, `screenshot` |

## Required Repo Setup Guidance

If the implementation adds a setup section, document this recommended project structure for Python repositories:

```text
.agents/skills/
.claude/skills/
AGENTS.md
CLAUDE.md
```

`AGENTS.md` and `CLAUDE.md` should explicitly define:

- test command, for example `uv run pytest -q`;
- lint command, for example `uv run ruff check .`;
- typecheck command, for example `uv run pyright` or `uv run mypy`;
- architecture boundaries and forbidden dependencies;
- refactoring rules that preserve behavior and update tests first;
- UI rules for browser validation, before/after screenshots, responsiveness, and accessibility;
- security rules for secrets, trust boundaries, and external input validation.

## Implementation Tasks

### Task 1: Refresh Source Evidence

**Files:**
- Validate: upstream repositories and current `SKILLS.md`

- [x] **Step 1: Refresh repository metadata**

```bash
for repo in \
  addyosmani/agent-skills \
  openai/skills \
  obra/superpowers \
  garrytan/gstack \
  alirezarezvani/claude-skills \
  anthropics/skills \
  VoltAgent/awesome-agent-skills \
  ComposioHQ/awesome-claude-skills
do
  gh repo view "$repo" --json nameWithOwner,description,stargazerCount,url
done
```

Expected: all repositories resolve. Update any star counts only if the README or catalog mentions them.

- [x] **Step 2: Export current catalog names**

```bash
python3 - <<'PY'
from pathlib import Path

for line in Path("SKILLS.md").read_text().splitlines():
    if not line.startswith("|") or line.startswith("|---") or line.startswith("| Skill"):
        continue
    print(line.strip("|").split("|")[0].strip())
PY
```

Expected: use this list to identify duplicate names before adding anything.

### Task 2: Verify Original Skill Links

**Files:**
- Validate: upstream skill paths

- [x] **Step 1: Verify Addy Osmani skill paths**

```bash
for path in \
  skills/code-simplification \
  skills/test-driven-development \
  skills/incremental-implementation \
  skills/code-review-and-quality \
  skills/debugging-and-error-recovery \
  skills/api-and-interface-design \
  skills/deprecation-and-migration \
  skills/context-engineering \
  skills/source-driven-development \
  skills/doubt-driven-development \
  skills/planning-and-task-breakdown \
  skills/frontend-ui-engineering \
  skills/browser-testing-with-devtools
do
  gh api "repos/addyosmani/agent-skills/contents/$path" --jq '.[].name'
done
```

Expected: each path resolves and contains a `SKILL.md` or equivalent skill content.

- [x] **Step 2: Verify alirezarezvani skill paths**

```bash
for path in \
  engineering-team/skills/senior-architect \
  engineering/skills/api-design-reviewer \
  engineering/skills/migration-architect \
  engineering/skills/observability-designer \
  engineering/skills/pr-review-expert \
  engineering/skills/skill-security-auditor
do
  gh api "repos/alirezarezvani/claude-skills/contents/$path" --jq '.[].name'
done
```

Expected: each path resolves and includes `SKILL.md`.

- [x] **Step 3: Verify GStack command paths**

```bash
for path in review plan-eng-review codex design-review plan-design-review benchmark cso qa ship
do
  gh api "repos/garrytan/gstack/contents/$path" --jq '.[].name'
done
```

Expected: each command path resolves. If GStack is added as a collection only, individual command entries may remain in installation notes.

- [x] **Step 4: Verify official and marketplace pages**

```bash
python3 - <<'PY'
from urllib.request import Request, urlopen

urls = [
    "https://github.com/openai/skills/tree/main/skills/.curated/figma-implement-design",
    "https://github.com/openai/skills/tree/main/skills/.curated/security-best-practices",
    "https://github.com/openai/skills/tree/main/skills/.curated/security-threat-model",
    "https://github.com/openai/skills/tree/main/skills/.curated/playwright",
    "https://github.com/openai/skills/tree/main/skills/.curated/screenshot",
    "https://officialskills.sh/openai/skills/frontend-skill",
    "https://officialskills.sh/browserbase/skills/ui-test",
    "https://officialskills.sh/google-labs-code/skills/design-md",
    "https://officialskills.sh/google-labs-code/skills/react-components",
    "https://officialskills.sh/google-labs-code/skills/shadcn-ui",
    "https://officialskills.sh/google-labs-code/skills/stitch-loop",
    "https://claude.com/plugins/pyright-lsp",
]

for url in urls:
    request = Request(url, method="GET", headers={"User-Agent": "catalog-check"})
    with urlopen(request, timeout=15) as response:
        print(response.status, response.geturl())
PY
```

Expected: every URL returns a status below 400.

### Task 3: Classify Candidates

**Files:**
- Modify: `SKILLS.md`

- [x] **Step 1: Assign a decision to each candidate**

Use this decision table:

| Decision | Meaning |
|---|---|
| `add` | New skill, verified original source, clear purpose, clear install guidance. |
| `add-source-qualified` | Same name as an existing skill, but a different source provides meaningfully different behavior. |
| `add-install-note-only` | Already in the catalog; add install guidance without duplicating the row. |
| `collection-only` | Add the pack once, but do not list every command as a separate skill. |
| `watchlist` | Useful, but source or install path needs stronger verification. |
| `reject` | Duplicate, unclear, inaccessible, unsafe, or too broad. |

- [x] **Step 2: Record duplicates**

At minimum, treat these as duplicates or install-note candidates:

- `figma-implement-design`
- `security-best-practices`
- `security-threat-model`
- `playwright`
- `screenshot`
- `systematic-debugging`
- `frontend-design`
- `test-driven-development` unless source-qualified

### Task 4: Update The Catalog

**Files:**
- Modify: `SKILLS.md`
- Modify: `README.md` only if the public skill count or roadmap changes
- Modify: `CURATION.md` only if install-source requirements need to be made explicit

- [x] **Step 1: Add repository pack entries**

Add or update pack-level entries for:

- `addyosmani/agent-skills`
- `GStack`
- `alirezarezvani/claude-skills`
- `ComposioHQ/awesome-claude-skills` as a discovery index if not already present

- [x] **Step 2: Add selected skill entries**

Add verified, non-duplicate skills from:

- Addy Osmani engineering skills;
- GStack virtual team commands;
- alirezarezvani engineering skills;
- OpenAI missing official skills;
- Browserbase and Google Stitch only if original pages and install paths are verified.

- [x] **Step 3: Add installation guidance**

Add or update a section like this:

```markdown
## Installation Notes

| Skill or pack | Install |
|---|---|
| addyosmani/agent-skills | `npx skills add addyosmani/agent-skills` |
| code-simplification | `npx skills add addyosmani/agent-skills --skill code-simplification` |
```

Expected: every newly added highlighted skill has installation guidance.

### Task 5: Validate The Repository

**Files:**
- Validate: `README.md`
- Validate: `SKILLS.md`
- Validate: `CURATION.md`
- Validate: `SKILL_EXPANSION_PLAN.md`
- Validate: `SHORTLIST_SKILLS_EVALUATION_PLAN.md`

- [x] **Step 1: Verify English-only content**

```bash
rg -n "[^\\x00-\\x7F]" .
```

Expected: no results, except external names or URLs that intentionally contain non-ASCII characters.

- [x] **Step 2: Verify links**

```bash
python3 - <<'PY'
from pathlib import Path
import re
import urllib.error
import urllib.request

files = [
    "README.md",
    "SKILLS.md",
    "CURATION.md",
    "SKILL_EXPANSION_PLAN.md",
    "SHORTLIST_SKILLS_EVALUATION_PLAN.md",
]
text = "\n".join(Path(path).read_text() for path in files if Path(path).exists())
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

- [x] **Step 3: Verify duplicates**

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
- Commit: `SHORTLIST_SKILLS_EVALUATION_PLAN.md`
- Commit: `SKILLS.md` if updated
- Commit: `README.md` if updated
- Commit: `CURATION.md` if updated

- [x] **Step 1: Review status and diff**

```bash
git status --short --branch
git diff --stat
git diff -- SHORTLIST_SKILLS_EVALUATION_PLAN.md SKILLS.md README.md CURATION.md
```

Expected: only intended files are changed.

- [x] **Step 2: Stage files explicitly**

```bash
git add SHORTLIST_SKILLS_EVALUATION_PLAN.md SKILLS.md README.md CURATION.md
```

Expected: only intended files are staged.

- [x] **Step 3: Commit**

```bash
git commit -m "docs: plan shortlist skills evaluation"
```

Expected: commit succeeds.

- [x] **Step 4: Push**

```bash
git push origin main
```

Expected: `main` is updated on GitHub.

- [x] **Step 5: Confirm remote state**

```bash
git status --short --branch
git rev-parse HEAD
git rev-parse origin/main
git ls-remote origin refs/heads/main
```

Expected: worktree is clean and all three SHAs match.

## Acceptance Checklist

- [x] Every shortlisted repository or pack has been evaluated.
- [x] Every skill candidate has a decision: add, add-source-qualified, install-note-only, collection-only, watchlist, or reject.
- [x] No existing skill is duplicated without source qualification.
- [x] New entries use original source links.
- [x] New entries have short English descriptions.
- [x] New entries have install commands or explicit installation notes.
- [x] Repository content remains English-only.
- [x] Link and duplicate checks pass.
- [x] Commit and push are completed.
