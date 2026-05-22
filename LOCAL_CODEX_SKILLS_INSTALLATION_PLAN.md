# Local Codex Skills Installation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Iterate through every entry in `SKILLS.md`, classify what can be installed locally for Codex, install every verified installable skill into the local Codex skills directory, and leave a reproducible manifest for updates.

**Architecture:** Treat `SKILLS.md` as the source of truth, but do not blindly install every link. Build a local inventory that classifies each row as `codex-skill`, `pack`, `plugin`, `command`, `collection`, `watchlist`, or `skip`, then install only rows with a verified Codex-compatible installation path. Use an idempotent installer so future catalog updates can be re-run without duplicating or corrupting local skills.

**Tech Stack:** Markdown, Python standard library, GitHub CLI, `npx skills`, `npx agent-skills-cli`, local Codex directory `~/.codex/skills`, shell scripts, and Git.

---

## Operating Rules

- Keep repository files in English.
- Do not install unverified community skills without recording their source and install method.
- Prefer `npx skills add <repo> --skill <skill-name>` when the source follows the Agent Skills format.
- Prefer official pack installers for repositories that publish Codex-specific setup, such as GStack or `agent-skills-cli`.
- Treat discovery indexes as catalogs, not install targets.
- Treat Claude-only plugins as optional unless they also expose Codex-compatible skill files.
- Never delete existing local Codex skills without a backup and an explicit restore path.
- Keep secrets, tokens, and private config out of the repo.

## Target State

After implementation:

- `~/.codex/skills` contains all verified Codex-compatible skills from `SKILLS.md`.
- Non-installable entries are documented with a clear reason.
- A generated manifest records source link, category, install command, local path, install status, and verification result.
- A summary report lists installed, skipped, failed, and watchlist entries.
- Re-running the installer is safe and idempotent.

## Implementation Result

Executed on 2026-05-22.

| Check | Result |
|---|---|
| Catalog entries represented in manifest | 140 |
| Installable entries | 129 |
| Installation failures | 0 |
| Manual-review entries | 1: `frontend-skill`, because the official page resolves but the current OpenAI skills package does not expose that skill name to the installer. |
| Collection-only entries | 9 |
| Plugin-optional entries | 1 |
| Local top-level Codex `SKILL.md` files | 76 |
| `skills ls -g -a codex --json` entries | 210 |
| Duplicate top-level local skill directory names | 0 |
| Backup archive | Created under `~/.codex/backups/`. |

## Files And Responsibilities

| Path | Action | Responsibility |
|---|---|---|
| `SKILLS.md` | Read | Source catalog with 140 entries. |
| `LOCAL_CODEX_SKILLS_INSTALLATION_PLAN.md` | Create | Human-readable implementation plan. |
| `data/local-codex-install-manifest.json` | Create during execution | Machine-readable install manifest generated from `SKILLS.md`. |
| `reports/local-codex-skills-installation.md` | Create during execution | Human-readable install report with decisions and failures. |
| `scripts/build_local_codex_skill_manifest.py` | Create during execution | Parses `SKILLS.md`, classifies entries, and emits the manifest. |
| `scripts/install_local_codex_skills.py` | Create during execution | Executes verified install commands and records outcomes. |
| `scripts/verify_local_codex_skills.py` | Create during execution | Verifies installed skill folders, `SKILL.md` files, duplicate names, and local accessibility. |

## Classification Rules

Use these rules when transforming catalog rows into install decisions:

| Decision | Meaning | Install behavior |
|---|---|---|
| `install-direct` | A row points to a specific Codex-compatible skill path or official skill page. | Install via `npx skills add` or copy from a verified local clone. |
| `install-pack` | A row is a pack with a Codex-compatible installer. | Install the pack using the upstream documented command. |
| `install-via-pack` | A row is a command or source-qualified skill included in an installed pack. | Install the parent pack and verify the specific skill exists locally. |
| `plugin-optional` | A row is a Claude plugin or language-server plugin, not a Codex skill. | Record as optional; do not install into `~/.codex/skills` unless Codex support is verified. |
| `collection-only` | A row is a discovery index or broad repository. | Do not install; record as a source for future discovery. |
| `manual-review` | A row has no reliable `SKILL.md`, installer, or public raw source. | Do not install automatically; record reason. |
| `skip-duplicate` | A row duplicates an installed skill without adding a distinct source. | Skip and reference the installed canonical source. |

## Initial Install Strategy

Start with sources already known to expose Codex-compatible installation paths:

| Source | Strategy |
|---|---|
| OpenAI Skills | `npx skills add openai/skills --skill <skill-name>` for curated and system skills. |
| Superpowers | `npx skills add obra/superpowers --skill <skill-name>` for individual skills. |
| Addy Osmani Agent Skills | `npx skills add addyosmani/agent-skills --skill <skill-name>` for individual skills; install pack only when command workflows are needed. |
| alirezarezvani/claude-skills | `npx agent-skills-cli add alirezarezvani/claude-skills --agent codex` for the full Codex-compatible library. |
| GStack | Clone GStack and run `./setup --host codex`; verify `gstack-*` folders under `~/.codex/skills`. |
| Anthropic Skills | Install only if `npx skills add anthropics/skills --skill <skill-name>` resolves; otherwise mark for manual review. |
| Trail of Bits Skills | Install only verified plugin paths with a `SKILL.md`; otherwise mark for manual review. |
| OfficialSkills pages | Use only when the page exposes a working GitHub source and install command. |

## Task 1: Build The Catalog Inventory

**Files:**
- Create: `scripts/build_local_codex_skill_manifest.py`
- Create: `data/local-codex-install-manifest.json`
- Read: `SKILLS.md`

- [ ] **Step 1: Create the manifest builder**

Create `scripts/build_local_codex_skill_manifest.py` with this behavior:

```python
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "SKILLS.md"
OUT = ROOT / "data" / "local-codex-install-manifest.json"

INSTALLABLE_REPOS = {
    "openai/skills": "npx skills add openai/skills --skill {skill}",
    "obra/superpowers": "npx skills add obra/superpowers --skill {skill}",
    "addyosmani/agent-skills": "npx skills add addyosmani/agent-skills --skill {skill}",
}

PACKS = {
    "GStack": "git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.cache/ai-agent-skills-catalog/gstack && cd ~/.cache/ai-agent-skills-catalog/gstack && ./setup --host codex",
    "alirezarezvani/claude-skills": "npx agent-skills-cli add alirezarezvani/claude-skills --agent codex",
}

COLLECTION_NAMES = {
    "Awesome Agent Skills",
    "Composio Awesome Claude Skills",
    "Trail of Bits Skills",
    "Vercel Agent Skills",
    "Agent Verifier",
    "AI Engineering Toolkit",
    "pm-skills",
    "antfu skills",
}

PLUGIN_NAMES = {
    "pyright-lsp plugin",
}


def parse_rows() -> list[dict[str, str]]:
    rows = []
    current_category = ""
    for line in SKILLS.read_text().splitlines():
        if line.startswith("## "):
            current_category = line.removeprefix("## ").strip()
        if not line.startswith("|") or line.startswith("|---") or line.startswith("| Skill"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 3:
            rows.append({
                "name": cells[0],
                "link": cells[1],
                "description": cells[2],
                "category": current_category,
            })
    return rows


def github_repo(link: str) -> str:
    parsed = urlparse(link)
    parts = [part for part in parsed.path.split("/") if part]
    if parsed.netloc == "github.com" and len(parts) >= 2:
        return f"{parts[0]}/{parts[1]}"
    return ""


def skill_from_link(name: str, link: str) -> str:
    if "skills/.curated/" in link:
        return link.rsplit("/", 1)[-1]
    if "skills/.system/" in link:
        return link.rsplit("/", 1)[-1]
    match = re.search(r"/skills/([^/#?]+)", link)
    if match:
        return match.group(1)
    return name


def classify(row: dict[str, str]) -> dict[str, str]:
    name = row["name"]
    link = row["link"]
    repo = github_repo(link)
    skill = skill_from_link(name, link)

    if name in PLUGIN_NAMES:
        return {"decision": "plugin-optional", "install_command": "", "reason": "Plugin entry, not a Codex skill folder."}
    if name in COLLECTION_NAMES:
        return {"decision": "collection-only", "install_command": "", "reason": "Collection or discovery index."}
    if name in PACKS:
        return {"decision": "install-pack", "install_command": PACKS[name], "reason": "Pack has Codex-compatible install command."}
    if repo in INSTALLABLE_REPOS and "/skills/" in link:
        return {
            "decision": "install-direct",
            "install_command": INSTALLABLE_REPOS[repo].format(skill=skill),
            "reason": "Known Agent Skills-compatible repository.",
        }
    if name.startswith("gstack-"):
        return {"decision": "install-via-pack", "install_command": PACKS["GStack"], "reason": "GStack command installed via GStack pack."}
    if repo == "alirezarezvani/claude-skills":
        return {"decision": "install-via-pack", "install_command": PACKS["alirezarezvani/claude-skills"], "reason": "Installed through the alirezarezvani Codex pack."}
    if "officialskills.sh/openai/skills/" in link:
        skill_name = link.rstrip("/").rsplit("/", 1)[-1]
        return {
            "decision": "install-direct",
            "install_command": f"npx skills add https://github.com/openai/skills --skill {skill_name}",
            "reason": "OfficialSkills page exposes OpenAI install command.",
        }
    if "officialskills.sh/browserbase/skills/" in link:
        skill_name = link.rstrip("/").rsplit("/", 1)[-1]
        return {
            "decision": "install-direct",
            "install_command": f"npx skills add https://github.com/browserbase/skills --skill {skill_name}",
            "reason": "OfficialSkills page exposes Browserbase install command.",
        }
    return {"decision": "manual-review", "install_command": "", "reason": "No verified Codex install command in current catalog."}


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    manifest = []
    for row in parse_rows():
        manifest.append({**row, **classify(row)})
    OUT.write_text(json.dumps(manifest, indent=2) + "\n")
    counts: dict[str, int] = {}
    for item in manifest:
        counts[item["decision"]] = counts.get(item["decision"], 0) + 1
    print(json.dumps({"entries": len(manifest), "counts": counts}, indent=2))


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run the builder**

```bash
python3 scripts/build_local_codex_skill_manifest.py
```

Expected: the command prints a JSON summary with `entries` equal to the current number of rows in `SKILLS.md`.

- [ ] **Step 3: Review manual decisions**

```bash
python3 - <<'PY'
import json
from pathlib import Path

manifest = json.loads(Path("data/local-codex-install-manifest.json").read_text())
for item in manifest:
    if item["decision"] in {"manual-review", "plugin-optional", "collection-only"}:
        print(f'{item["decision"]}: {item["name"]} -> {item["link"]} ({item["reason"]})')
PY
```

Expected: every non-installed entry has an explicit reason.

## Task 2: Verify Install Commands Before Running Them

**Files:**
- Modify: `data/local-codex-install-manifest.json`
- Create: `reports/local-codex-install-command-review.md`

- [ ] **Step 1: List unique commands**

```bash
python3 - <<'PY'
import json
from pathlib import Path

manifest = json.loads(Path("data/local-codex-install-manifest.json").read_text())
commands = sorted({item["install_command"] for item in manifest if item["install_command"]})
for command in commands:
    print(command)
PY
```

Expected: repeated pack commands appear once in the output.

- [ ] **Step 2: Confirm required executables**

```bash
for tool in node npm npx git gh python3; do
  command -v "$tool" >/dev/null && echo "ok $tool" || echo "missing $tool"
done
```

Expected: `ok` for every required tool. If `npx agent-skills-cli` is not available, the installer will call it through `npx`.

- [ ] **Step 3: Verify local Codex directory**

```bash
mkdir -p ~/.codex/skills
test -d ~/.codex/skills && echo "ok ~/.codex/skills"
```

Expected: `ok ~/.codex/skills`.

- [ ] **Step 4: Create a backup before installing**

```bash
mkdir -p ~/.codex/backups
tar -czf ~/.codex/backups/skills-before-catalog-install-$(date +%Y%m%d-%H%M%S).tar.gz -C ~/.codex skills
ls -1 ~/.codex/backups/skills-before-catalog-install-*.tar.gz | tail -n 1
```

Expected: a backup archive path is printed.

## Task 3: Implement The Local Installer

**Files:**
- Create: `scripts/install_local_codex_skills.py`
- Read: `data/local-codex-install-manifest.json`
- Write: `reports/local-codex-skills-installation.md`

- [ ] **Step 1: Create the installer script**

Create `scripts/install_local_codex_skills.py` with this behavior:

```python
from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "local-codex-install-manifest.json"
REPORT = ROOT / "reports" / "local-codex-skills-installation.md"
CODEX_SKILLS = Path.home() / ".codex" / "skills"


def run(command: str, dry_run: bool) -> tuple[str, str]:
    if dry_run:
        return "dry-run", ""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    output = (result.stdout + result.stderr).strip()
    return ("ok" if result.returncode == 0 else f"failed:{result.returncode}", output)


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    manifest = json.loads(MANIFEST.read_text())
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    CODEX_SKILLS.mkdir(parents=True, exist_ok=True)

    seen_commands: set[str] = set()
    rows: list[dict[str, str]] = []

    for item in manifest:
        command = item.get("install_command", "")
        if item["decision"] in {"install-direct", "install-pack", "install-via-pack"} and command:
            if command in seen_commands and item["decision"] in {"install-pack", "install-via-pack"}:
                status, output = "skipped-duplicate-command", ""
            else:
                seen_commands.add(command)
                status, output = run(command, dry_run)
        else:
            status, output = f'skipped:{item["decision"]}', item["reason"]
        rows.append({**item, "status": status, "output": output[-1000:]})

    lines = [
        "# Local Codex Skills Installation Report",
        "",
        f"Generated: {datetime.utcnow().isoformat(timespec='seconds')}Z",
        f"Mode: {'dry-run' if dry_run else 'install'}",
        f"Codex skills directory: `{CODEX_SKILLS}`",
        "",
        "| Name | Decision | Status | Reason |",
        "|---|---|---|---|",
    ]
    for row in rows:
        reason = row["reason"].replace("|", "/")
        lines.append(f'| {row["name"]} | {row["decision"]} | {row["status"]} | {reason} |')
    REPORT.write_text("\n".join(lines) + "\n")

    failed = [row for row in rows if row["status"].startswith("failed:")]
    print(json.dumps({
        "mode": "dry-run" if dry_run else "install",
        "entries": len(rows),
        "failed": len(failed),
        "report": str(REPORT),
    }, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 2: Run dry-run mode**

```bash
python3 scripts/install_local_codex_skills.py --dry-run
```

Expected: the command exits `0`, writes `reports/local-codex-skills-installation.md`, and reports `failed: 0`.

- [ ] **Step 3: Inspect dry-run report**

```bash
sed -n '1,220p' reports/local-codex-skills-installation.md
```

Expected: direct installs, pack installs, collection skips, plugin skips, and manual-review entries are visible.

## Task 4: Install Verified Skills Locally

**Files:**
- Read: `data/local-codex-install-manifest.json`
- Modify local machine: `~/.codex/skills`
- Write: `reports/local-codex-skills-installation.md`

- [ ] **Step 1: Run the installer**

```bash
python3 scripts/install_local_codex_skills.py
```

Expected: the command exits `0` or fails only for entries that need manual source remediation.

- [ ] **Step 2: If installation fails, isolate failures**

```bash
rg -n "failed:" reports/local-codex-skills-installation.md
```

Expected: no results. If results appear, do not retry blindly; inspect the failed command, source link, and upstream install documentation.

- [ ] **Step 3: Count local skills**

```bash
find ~/.codex/skills -mindepth 2 -maxdepth 2 -name SKILL.md | wc -l
```

Expected: the count increases after installation.

## Task 5: Verify Local Codex Skill Integrity

**Files:**
- Create: `scripts/verify_local_codex_skills.py`
- Read: `data/local-codex-install-manifest.json`
- Read local machine: `~/.codex/skills`
- Write: `reports/local-codex-skills-verification.md`

- [ ] **Step 1: Create verification script**

Create `scripts/verify_local_codex_skills.py` with this behavior:

```python
from __future__ import annotations

import json
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "local-codex-install-manifest.json"
REPORT = ROOT / "reports" / "local-codex-skills-verification.md"
CODEX_SKILLS = Path.home() / ".codex" / "skills"


def skill_dirs() -> list[Path]:
    return sorted(path.parent for path in CODEX_SKILLS.glob("**/SKILL.md"))


def main() -> int:
    manifest = json.loads(MANIFEST.read_text())
    installable = [item for item in manifest if item["decision"] in {"install-direct", "install-pack", "install-via-pack"}]
    dirs = skill_dirs()
    names = [path.name for path in dirs]
    duplicates = sorted(name for name, count in Counter(names).items() if count > 1)

    lines = [
        "# Local Codex Skills Verification Report",
        "",
        f"Generated: {datetime.utcnow().isoformat(timespec='seconds')}Z",
        f"Codex skills directory: `{CODEX_SKILLS}`",
        f"Manifest installable entries: {len(installable)}",
        f"Local `SKILL.md` files: {len(dirs)}",
        f"Duplicate local skill directory names: {len(duplicates)}",
        "",
    ]
    if duplicates:
        lines.append("## Duplicate Names")
        lines.extend(f"- {name}" for name in duplicates)
        lines.append("")
    lines.append("## Local Skill Files")
    lines.extend(f"- `{path / 'SKILL.md'}`" for path in dirs)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n")
    print(json.dumps({"local_skill_files": len(dirs), "duplicates": duplicates, "report": str(REPORT)}, indent=2))
    return 1 if duplicates else 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 2: Run verification**

```bash
python3 scripts/verify_local_codex_skills.py
```

Expected: the command exits `0` and reports `Duplicate local skill directory names: 0`.

- [ ] **Step 3: Confirm Codex can discover installed skills**

```bash
find ~/.codex/skills -mindepth 2 -maxdepth 2 -name SKILL.md | sort | sed -n '1,120p'
```

Expected: installed skills appear as local `SKILL.md` files.

## Task 6: Update Repository Documentation

**Files:**
- Modify: `README.md`
- Modify: `SKILLS.md` only if installation notes need corrections
- Modify: `CURATION.md` only if install policy changed

- [ ] **Step 1: Add local installation section to README**

Add a short section that links to:

```markdown
## Local Codex Installation

Local installation is tracked by [LOCAL_CODEX_SKILLS_INSTALLATION_PLAN.md](LOCAL_CODEX_SKILLS_INSTALLATION_PLAN.md). The plan generates a manifest, installs verified Codex-compatible skills into `~/.codex/skills`, and records skipped entries with reasons.
```

Expected: the README explains where the local installation plan lives without duplicating all commands.

- [ ] **Step 2: Keep generated machine reports out of the main README**

Do not paste `reports/local-codex-skills-installation.md` into `README.md`. Keep the README focused and link to the plan instead.

## Task 7: Validate Repository And Local Install State

**Files:**
- Validate: `README.md`
- Validate: `SKILLS.md`
- Validate: `CURATION.md`
- Validate: `LOCAL_CODEX_SKILLS_INSTALLATION_PLAN.md`
- Validate: generated scripts and reports

- [ ] **Step 1: Verify English-only repository content**

```bash
rg -n "[^\\x00-\\x7F]" .
```

Expected: no results unless a future source name intentionally requires non-ASCII.

- [ ] **Step 2: Verify catalog duplicates**

```bash
python3 - <<'PY'
from collections import Counter
from pathlib import Path

names = []
for line in Path("SKILLS.md").read_text().splitlines():
    if line.startswith("|") and not line.startswith("|---") and not line.startswith("| Skill"):
        names.append(line.strip("|").split("|")[0].strip())
duplicates = {name: count for name, count in Counter(names).items() if count > 1}
print(f"names={len(names)} unique={len(set(names))} duplicates={len(duplicates)}")
for name, count in sorted(duplicates.items()):
    print(f"{name}: {count}")
raise SystemExit(1 if duplicates else 0)
PY
```

Expected: `duplicates=0`.

- [ ] **Step 3: Verify links in maintained docs**

```bash
python3 - <<'PY'
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import re
import urllib.error
import urllib.request

files = [
    "README.md",
    "SKILLS.md",
    "CURATION.md",
    "LOCAL_CODEX_SKILLS_INSTALLATION_PLAN.md",
]
links = sorted(set(
    link.rstrip(".,;")
    for path in files
    for link in re.findall(r"https?://[^\\s)>\\\"`]+", Path(path).read_text())
))

def check(link: str):
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(link, method=method, headers={"User-Agent": "catalog-link-check"})
        try:
            with urllib.request.urlopen(request, timeout=10) as response:
                return None if response.status < 400 else (link, "status", str(response.status))
        except urllib.error.HTTPError as exc:
            if method == "HEAD" and exc.code in (403, 405, 429):
                continue
            if exc.code == 429:
                return None
            return (link, "HTTPError", str(exc.code))
        except Exception as exc:
            if method == "HEAD":
                continue
            return (link, type(exc).__name__, str(exc)[:160])
    return None

failed = []
with ThreadPoolExecutor(max_workers=24) as pool:
    for future in as_completed({pool.submit(check, link): link for link in links}):
        result = future.result()
        if result:
            failed.append(result)

print(f"checked={len(links)} failed={len(failed)}")
for item in sorted(failed):
    print("|".join(item))
raise SystemExit(1 if failed else 0)
PY
```

Expected: `failed=0`.

- [ ] **Step 4: Verify local install reports exist**

```bash
test -s reports/local-codex-skills-installation.md
test -s reports/local-codex-skills-verification.md
```

Expected: both commands exit `0` after installation execution.

## Task 8: Commit And Push

**Files:**
- Commit: `LOCAL_CODEX_SKILLS_INSTALLATION_PLAN.md`
- Commit after execution: `scripts/build_local_codex_skill_manifest.py`
- Commit after execution: `scripts/install_local_codex_skills.py`
- Commit after execution: `scripts/verify_local_codex_skills.py`
- Commit after execution: `data/local-codex-install-manifest.json`
- Commit after execution: `reports/local-codex-skills-installation.md`
- Commit after execution: `reports/local-codex-skills-verification.md`
- Commit after execution: `README.md` if updated

- [ ] **Step 1: Review intended files**

```bash
git status --short --branch
git diff --stat
```

Expected: only plan, generated scripts, generated manifest, generated reports, and intentional docs are changed.

- [ ] **Step 2: Stage explicitly**

```bash
git add LOCAL_CODEX_SKILLS_INSTALLATION_PLAN.md scripts/ data/ reports/ README.md SKILLS.md CURATION.md
```

Expected: only intended files are staged.

- [ ] **Step 3: Commit**

```bash
git commit -m "docs: plan local codex skills installation"
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

Expected: worktree is clean and all printed SHAs match.

## Acceptance Checklist

- [ ] Every row in `SKILLS.md` is represented in `data/local-codex-install-manifest.json`.
- [ ] Every row has a clear install decision and reason.
- [ ] Every verified Codex-compatible skill is installed or has a recorded failure.
- [ ] Discovery indexes are not blindly installed.
- [ ] Optional plugins are documented separately from Codex skill folders.
- [ ] Local `~/.codex/skills` has a backup before installation.
- [ ] Local verification report exists and shows no duplicate local skill directory names.
- [ ] Repository docs remain English-only.
- [ ] Link and duplicate checks pass.
- [ ] Commit and push are completed.
