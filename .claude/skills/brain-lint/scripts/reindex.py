#!/usr/bin/env python3
"""Rebuild index.md, the catalog of this workspace: one line per file, with its description.

Run from the workspace root, or let the hook in .claude/settings.json run it after every write.

    python3 .claude/skills/brain-lint/scripts/reindex.py            rebuild, print what changed
    python3 .claude/skills/brain-lint/scripts/reindex.py --check    exit 1 when index.md is stale
    python3 .claude/skills/brain-lint/scripts/reindex.py --hook     rebuild silently, never fail

A file's description is its frontmatter `description:` when it has one, else its first line
of prose. Journals, archives, raw sources, templates and the system folder stay out: they are
searched when needed, never navigated.
"""
import os
import re
import sys
from pathlib import Path

SKIP_DIRS = {".git", ".claude", "node_modules", "_TEMPLATE", "archive", "03-archive", "04-archive", "sessions", "raw"}
SKIP_FILES = {"index.md", "log.md"}
TOP_FILES = ["USER.md", "RHYTHM.md", "CLAUDE.md", "SETUP.md", "README.md"]
MAX_DESC = 120


def root() -> Path:
    env = os.environ.get("CLAUDE_PROJECT_DIR")
    return Path(env) if env else Path.cwd()


def describe(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    lines = text.splitlines()
    body_start = 0
    if lines and lines[0].strip() == "---":
        for i, line in enumerate(lines[1:], start=1):
            if line.strip() == "---":
                body_start = i + 1
                break
            m = re.match(r"description:\s*(.+)", line)
            if m:
                return clip(m.group(1).strip().strip('"\''))
    in_code = False
    for line in lines[body_start:]:
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not s or s.startswith(("#", "|", ">", "<!--", "---")):
            continue
        s = re.sub(r"^[-*]\s+|^\d+\.\s+", "", s)
        s = re.sub(r"\*\*|`", "", s)
        s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
        return clip(s)
    return ""


def clip(s: str) -> str:
    if len(s) <= MAX_DESC:
        return s
    cut = s[:MAX_DESC].rsplit(" ", 1)[0]
    return cut.rstrip(",;:") + "..."


def collect(base: Path) -> dict:
    groups = {"": []}
    for name in TOP_FILES:
        if (base / name).is_file():
            groups[""].append(name)
    for dirpath, dirnames, filenames in os.walk(base):
        rel_dir = Path(dirpath).relative_to(base)
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS and not d.startswith("."))
        if rel_dir == Path("."):
            continue
        top = rel_dir.parts[0]
        for f in sorted(filenames):
            if f.endswith(".md") and f not in SKIP_FILES:
                groups.setdefault(top, []).append((rel_dir / f).as_posix())
    return groups


def render(base: Path) -> str:
    out = [
        "# Index",
        "",
        "Every file of this workspace with its description. Claude reads this first and opens only what the task needs.",
        "Rebuilt after every write by `.claude/skills/brain-lint/scripts/reindex.py`: never edit it by hand.",
        "",
    ]
    for top, files in collect(base).items():
        if not files:
            continue
        out.append(f"## {top or 'Root'}")
        out.append("")
        for rel in files:
            desc = describe(base / rel)
            out.append(f"- [{rel}]({rel})" + (f": {desc}" if desc else ""))
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    base = root()
    if mode == "--hook":
        try:
            sys.stdin.read()
        except Exception:
            pass
        if not (base / "USER.md").exists() and not (base / "SETUP.md").exists():
            return 0
    target = base / "index.md"
    new = render(base)
    old = target.read_text(encoding="utf-8") if target.exists() else ""
    if mode == "--check":
        if new != old:
            print("index.md is stale: run python3 .claude/skills/brain-lint/scripts/reindex.py")
            return 1
        print("index.md is current")
        return 0
    if new != old:
        try:
            target.write_text(new, encoding="utf-8")
        except OSError as e:
            if mode == "--hook":
                return 0
            print(f"could not write index.md: {e}")
            return 2
        if mode != "--hook":
            print(f"index.md rebuilt, {new.count(chr(10) + '- [')} files")
    elif mode != "--hook":
        print("index.md already current")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        if "--hook" in sys.argv:
            sys.exit(0)
        raise
