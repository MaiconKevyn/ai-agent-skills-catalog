from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "SKILLS.md"
OUT = ROOT / "data" / "local-codex-install-manifest.json"


COLLECTION_NAMES = {
    "AI Engineering Toolkit",
    "Agent Verifier",
    "Awesome Agent Skills",
    "Composio Awesome Claude Skills",
    "Trail of Bits Skills",
    "Vercel Agent Skills",
    "antfu skills",
    "pm-skills",
    "testing-handbook-skills",
}

PLUGIN_NAMES = {
    "pyright-lsp plugin",
}

PACK_COMMANDS = {
    "Superpowers": {
        "command": "npx --yes skills add obra/superpowers -g -a codex --all --copy --full-depth",
        "args": [
            "npx",
            "--yes",
            "skills",
            "add",
            "obra/superpowers",
            "-g",
            "-a",
            "codex",
            "--all",
            "--copy",
            "--full-depth",
        ],
    },
    "Addy Osmani Agent Skills": {
        "command": "npx --yes skills add addyosmani/agent-skills -g -a codex --all --copy --full-depth",
        "args": [
            "npx",
            "--yes",
            "skills",
            "add",
            "addyosmani/agent-skills",
            "-g",
            "-a",
            "codex",
            "--all",
            "--copy",
            "--full-depth",
        ],
    },
    "GStack": {
        "command": "install GStack with ./setup --host codex from a local cache",
        "args": [],
        "special": "gstack",
    },
    "alirezarezvani/claude-skills": {
        "command": "npx --yes agent-skills-cli install alirezarezvani/claude-skills -g -a codex -y",
        "args": [
            "npx",
            "--yes",
            "agent-skills-cli",
            "install",
            "alirezarezvani/claude-skills",
            "-g",
            "-a",
            "codex",
            "-y",
        ],
    },
}

PACK_REPOS = {
    "addyosmani/agent-skills": "Addy Osmani Agent Skills",
    "obra/superpowers": "Superpowers",
}

REPO_ALIASES = {
    "https://github.com/openai/skills": "openai/skills",
    "https://github.com/browserbase/skills": "browserbase/skills",
}

SKILL_ALIASES = {
    "ai-engineer-skill": "ai-engineer",
    "csv-data-wrangler-skill": "csv-data-wrangler",
    "data-analyst-skill": "data-analyst",
    "data-scientist-skill": "data-scientist",
    "database-optimizer-skill": "database-optimizer",
    "llm-architect-skill": "llm-architect",
    "mlops-engineer-skill": "mlops-engineer",
    "workflow-skill-design": "designing-workflow-skills",
}

MULTI_SKILL_ALIASES = {
    "static-analysis": {
        "repo": "trailofbits/skills",
        "skills": ["codeql", "sarif-parsing", "semgrep"],
        "reason": "Catalog row points to a plugin group; install its concrete static-analysis skills.",
    }
}

NOT_INSTALLABLE = {
    "frontend-skill": "OfficialSkills page resolves, but the OpenAI skills package no longer exposes this skill name to the installer.",
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
            rows.append(
                {
                    "name": cells[0],
                    "link": cells[1],
                    "description": cells[2],
                    "category": current_category,
                }
            )
    return rows


def github_repo(link: str) -> str:
    parsed = urlparse(link)
    parts = [part for part in parsed.path.split("/") if part]
    if parsed.netloc == "github.com" and len(parts) >= 2:
        return f"{parts[0]}/{parts[1]}"
    return ""


def github_path(link: str) -> str:
    parsed = urlparse(link)
    parts = [part for part in parsed.path.split("/") if part]
    if parsed.netloc == "github.com" and len(parts) >= 5 and parts[2] in {"tree", "blob"}:
        return "/".join(parts[4:])
    return ""


def officialskills_source(link: str) -> tuple[str, str] | None:
    parsed = urlparse(link)
    parts = [part for part in parsed.path.split("/") if part]
    if parsed.netloc != "officialskills.sh" or len(parts) < 3 or parts[1] != "skills":
        return None
    owner = parts[0]
    skill = parts[2]
    if owner == "openai":
        return REPO_ALIASES["https://github.com/openai/skills"], skill
    if owner == "browserbase":
        return REPO_ALIASES["https://github.com/browserbase/skills"], skill
    return None


def skill_from_link(name: str, link: str) -> str:
    source = officialskills_source(link)
    if source:
        return source[1]
    path = github_path(link)
    if path:
        return path.rsplit("/", 1)[-1]
    return name


def npx_skill_command(repo: str, skill: str | list[str]) -> tuple[str, list[str]]:
    skills = [skill] if isinstance(skill, str) else skill
    args = [
        "npx",
        "--yes",
        "skills",
        "add",
        repo,
        "-g",
        "-a",
        "codex",
        "-s",
        *skills,
        "-y",
        "--copy",
        "--full-depth",
    ]
    return " ".join(args), args


def npx_pack_command(repo: str) -> tuple[str, list[str]]:
    args = [
        "npx",
        "--yes",
        "skills",
        "add",
        repo,
        "-g",
        "-a",
        "codex",
        "--all",
        "--copy",
        "--full-depth",
    ]
    return " ".join(args), args


def classify(row: dict[str, str]) -> dict[str, object]:
    name = row["name"]
    link = row["link"]
    repo = github_repo(link)
    path = github_path(link)
    skill = skill_from_link(name, link)
    official = officialskills_source(link)

    if name in NOT_INSTALLABLE:
        return {
            "decision": "manual-review",
            "install_command": "",
            "install_args": [],
            "reason": NOT_INSTALLABLE[name],
        }

    if name in MULTI_SKILL_ALIASES:
        alias = MULTI_SKILL_ALIASES[name]
        command, args = npx_skill_command(str(alias["repo"]), list(alias["skills"]))
        return {
            "decision": "install-direct",
            "install_command": command,
            "install_args": args,
            "reason": str(alias["reason"]),
        }

    if name in PLUGIN_NAMES:
        return {
            "decision": "plugin-optional",
            "install_command": "",
            "install_args": [],
            "reason": "Plugin entry, not a Codex skill folder.",
        }

    if name in PACK_COMMANDS:
        command = PACK_COMMANDS[name]
        return {
            "decision": "install-pack",
            "install_command": command["command"],
            "install_args": command.get("args", []),
            "special": command.get("special", ""),
            "reason": "Pack has a Codex-compatible install path.",
        }

    if name in COLLECTION_NAMES:
        return {
            "decision": "collection-only",
            "install_command": "",
            "install_args": [],
            "reason": "Collection or discovery index; do not install blindly.",
        }

    if name.startswith("gstack-"):
        command = PACK_COMMANDS["GStack"]
        return {
            "decision": "install-via-pack",
            "install_command": command["command"],
            "install_args": command.get("args", []),
            "special": command.get("special", ""),
            "reason": "GStack command is installed through the GStack pack.",
        }

    if repo == "alirezarezvani/claude-skills":
        command = PACK_COMMANDS["alirezarezvani/claude-skills"]
        return {
            "decision": "install-via-pack",
            "install_command": command["command"],
            "install_args": command["args"],
            "reason": "Installed through the alirezarezvani Codex pack.",
        }

    if repo in PACK_REPOS:
        pack_name = PACK_REPOS[repo]
        command = PACK_COMMANDS[pack_name]
        return {
            "decision": "install-via-pack",
            "install_command": command["command"],
            "install_args": command["args"],
            "reason": f"Installed through the {pack_name} pack.",
        }

    if official:
        repo, skill = official
        skill = SKILL_ALIASES.get(name, skill)
        command, args = npx_skill_command(repo, skill)
        return {
            "decision": "install-direct",
            "install_command": command,
            "install_args": args,
            "reason": "OfficialSkills page exposes a Codex-compatible install command.",
        }

    if repo and path:
        skill = SKILL_ALIASES.get(name, skill)
        command, args = npx_skill_command(repo, skill)
        return {
            "decision": "install-direct",
            "install_command": command,
            "install_args": args,
            "reason": f"GitHub skill path `{path}` can be installed by skill name.",
        }

    if repo and not path:
        command, args = npx_pack_command(repo)
        return {
            "decision": "install-pack",
            "install_command": command,
            "install_args": args,
            "reason": "Repository root may expose one or more skills; install all discovered skills.",
        }

    return {
        "decision": "manual-review",
        "install_command": "",
        "install_args": [],
        "reason": "No verified Codex install command in current catalog.",
    }


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    manifest = []
    for row in parse_rows():
        manifest.append({**row, **classify(row)})
    OUT.write_text(json.dumps(manifest, indent=2) + "\n")
    counts: dict[str, int] = {}
    for item in manifest:
        decision = str(item["decision"])
        counts[decision] = counts.get(decision, 0) + 1
    print(json.dumps({"entries": len(manifest), "counts": counts}, indent=2))


if __name__ == "__main__":
    main()
