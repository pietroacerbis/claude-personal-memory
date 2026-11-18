#!/usr/bin/env python3
"""Hand Claude the memory at the start of every session, whatever the first message says.

Runs at SessionStart (.claude/settings.json). It prints, as context for the session:
  - USER.md, whole;
  - 04-memory/MEMORY.md, whole;
  - today's journal: the carryover and the session blocks;
  - the RHYTHM.md rows for today.
With no USER.md it says the workspace is not set up, so the first reply starts SETUP.md.
Each file is cut at a fixed size, so the context stays small however the files grow.
"""
import datetime
import json
import os
import re
import sys
from pathlib import Path

CAP = 12000
DAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]


def read(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    if len(text) > CAP:
        text = text[:CAP] + f"\n[cut at {CAP} characters: open {path.name} for the rest]\n"
    return text


def rhythm_rows(text: str, today: datetime.date) -> list:
    day = DAYS[today.weekday()]
    last_friday = day == "fri" and (today + datetime.timedelta(days=7)).month != today.month
    rows = []
    for line in text.splitlines():
        cells = [c.strip().lower() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or not line.lstrip().startswith("|"):
            continue
        if cells[0] in (day, "daily") or (cells[0] == "fri-last" and last_friday):
            rows.append(line.strip())
    return rows


def main() -> int:
    try:
        sys.stdin.read()
    except Exception:
        pass
    base = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path.cwd())
    if not (base / "USER.md").exists():
        if (base / "SETUP.md").exists():
            context = ("This workspace is not set up yet: USER.md is missing. Whatever the user's first "
                       "message says, open SETUP.md and follow it from phase 1.")
        else:
            return 0
    else:
        today = datetime.date.today()
        journal = base / "04-memory" / "sessions" / today.strftime("%Y-%m") / f"{today.isoformat()}.md"
        parts = [f"Memory loaded at the open, {today.isoformat()}. Re-read a file from disk before a write depends on it."]
        for label, path in (("USER.md", base / "USER.md"), ("04-memory/MEMORY.md", base / "04-memory" / "MEMORY.md")):
            text = read(path)
            if text:
                parts.append(f"===== {label}\n{text}")
        jtext = read(journal)
        if jtext:
            parts.append(f"===== today's journal, {journal.relative_to(base).as_posix()}\n{jtext}")
        rows = rhythm_rows(read(base / "RHYTHM.md"), today)
        if rows:
            parts.append("===== RHYTHM.md, today's rows\n" + "\n".join(rows))
        context = "\n\n".join(parts)
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": context}}))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)
