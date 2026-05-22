from __future__ import annotations

import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "local-codex-install-manifest.json"
REPORT = ROOT / "reports" / "local-codex-skills-verification.md"
CODEX_SKILLS = Path.home() / ".codex" / "skills"


def skill_dirs() -> list[Path]:
    return sorted(path for path in CODEX_SKILLS.iterdir() if (path / "SKILL.md").exists())


def main() -> int:
    manifest = json.loads(MANIFEST.read_text())
    installable = [
        item
        for item in manifest
        if item["decision"] in {"install-direct", "install-pack", "install-via-pack"}
    ]
    dirs = skill_dirs()
    names = [path.name for path in dirs]
    duplicates = sorted(name for name, count in Counter(names).items() if count > 1)

    lines = [
        "# Local Codex Skills Verification Report",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        f"Codex skills directory: `{CODEX_SKILLS}`",
        f"Manifest entries: {len(manifest)}",
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
