from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "local-codex-install-manifest.json"
REPORT = ROOT / "reports" / "local-codex-skills-installation.md"
CODEX_SKILLS = Path.home() / ".codex" / "skills"
GSTACK_CACHE = Path.home() / ".cache" / "ai-agent-skills-catalog" / "gstack"


def run_args(args: list[str], dry_run: bool) -> tuple[str, str]:
    if dry_run:
        return "dry-run", ""
    result = subprocess.run(args, text=True, capture_output=True)
    output = (result.stdout + result.stderr).strip()
    return ("ok" if result.returncode == 0 else f"failed:{result.returncode}", output)


def run_gstack(dry_run: bool) -> tuple[str, str]:
    if dry_run:
        return "dry-run", ""
    if shutil.which("bun") is None:
        return "failed:missing-bun", "GStack setup requires bun, but bun is not installed."

    GSTACK_CACHE.parent.mkdir(parents=True, exist_ok=True)
    if (GSTACK_CACHE / ".git").exists():
        update = subprocess.run(
            ["git", "-C", str(GSTACK_CACHE), "pull", "--ff-only"],
            text=True,
            capture_output=True,
        )
    else:
        update = subprocess.run(
            ["git", "clone", "--single-branch", "--depth", "1", "https://github.com/garrytan/gstack.git", str(GSTACK_CACHE)],
            text=True,
            capture_output=True,
        )
    if update.returncode != 0:
        return f"failed:{update.returncode}", (update.stdout + update.stderr).strip()

    setup = subprocess.run(
        ["./setup", "--host", "codex"],
        cwd=GSTACK_CACHE,
        text=True,
        capture_output=True,
        env={**os.environ, "CI": "1"},
    )
    output = (update.stdout + update.stderr + setup.stdout + setup.stderr).strip()
    return ("ok" if setup.returncode == 0 else f"failed:{setup.returncode}", output)


def run_item(item: dict[str, object], dry_run: bool) -> tuple[str, str]:
    if item.get("special") == "gstack":
        return run_gstack(dry_run)
    args = item.get("install_args") or []
    if not isinstance(args, list) or not args:
        return f"skipped:{item['decision']}", str(item["reason"])
    return run_args([str(arg) for arg in args], dry_run)


def compact_output(output: str) -> str:
    output = output.replace("|", "/").replace("\r", "")
    if len(output) > 1000:
        return output[-1000:]
    return output


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    manifest = json.loads(MANIFEST.read_text())
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    CODEX_SKILLS.mkdir(parents=True, exist_ok=True)

    seen_commands: set[str] = set()
    rows: list[dict[str, object]] = []

    for item in manifest:
        decision = str(item["decision"])
        command = str(item.get("install_command") or "")
        if decision in {"install-direct", "install-pack", "install-via-pack"} and command:
            if command in seen_commands:
                status, output = "skipped-duplicate-command", "Covered by a previously executed install command."
            else:
                seen_commands.add(command)
                status, output = run_item(item, dry_run)
        else:
            status, output = f"skipped:{decision}", str(item["reason"])
        rows.append({**item, "status": status, "output": compact_output(output)})

    lines = [
        "# Local Codex Skills Installation Report",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        f"Mode: {'dry-run' if dry_run else 'install'}",
        f"Codex skills directory: `{CODEX_SKILLS}`",
        "",
        "| Name | Decision | Status | Reason |",
        "|---|---|---|---|",
    ]
    for row in rows:
        reason = str(row["reason"]).replace("|", "/")
        lines.append(f'| {row["name"]} | {row["decision"]} | {row["status"]} | {reason} |')

    failed_rows = [row for row in rows if str(row["status"]).startswith("failed:")]
    if failed_rows:
        lines.extend(["", "## Failure Details", ""])
        for row in failed_rows:
            lines.extend(
                [
                    f"### {row['name']}",
                    "",
                    f"- Command: `{row.get('install_command', '')}`",
                    f"- Status: `{row['status']}`",
                    "",
                    "```text",
                    str(row["output"]),
                    "```",
                    "",
                ]
            )

    REPORT.write_text("\n".join(lines) + "\n")
    print(
        json.dumps(
            {
                "mode": "dry-run" if dry_run else "install",
                "entries": len(rows),
                "failed": len(failed_rows),
                "report": str(REPORT),
            },
            indent=2,
        )
    )
    return 1 if failed_rows and not dry_run else 0


if __name__ == "__main__":
    raise SystemExit(main())
