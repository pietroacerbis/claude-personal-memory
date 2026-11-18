#!/usr/bin/env python3
"""List the day journals newer than the last run of a distil variant.

    python3 journals.py VARIANT [--today YYYY-MM-DD]

Run from the workspace root. The boundary is, in this order:
  1. the line "- VARIANT: YYYY-MM-DD" under "## Last runs" of the skill's memory.md;
  2. for learning only, the newest date written in "## Recent learnings" of 04-memory/MEMORY.md,
     since every learning row names the journal it comes from;
  3. 30 days before today, on a first run.
Prints the boundary and where it came from, then one journal path per line, oldest first,
then "N journals". A journal is 04-memory/sessions/YYYY-MM/YYYY-MM-DD.md dated after the
boundary, up to today. Exit 2 when VARIANT is unknown. Standard library only.
"""
import argparse
import datetime
import pathlib
import re
import sys

VARIANTS = ("mistakes", "learning", "voice")
DATE = r"\d{4}-\d{2}-\d{2}"


def from_memory(variant: str):
    memory = pathlib.Path(__file__).resolve().parent.parent / "memory.md"
    if not memory.is_file():
        return None
    m = re.search(rf"(?m)^- {variant}: ({DATE})\s*$", memory.read_text(encoding="utf-8"))
    return m.group(1) if m else None


def from_learnings(root: pathlib.Path):
    path = root / "04-memory" / "MEMORY.md"
    if not path.is_file():
        return None
    m = re.search(r"(?ms)^## Recent learnings[ \t]*\n(.*?)(?=^## |\Z)", path.read_text(encoding="utf-8"))
    dates = re.findall(DATE, m.group(1)) if m else []
    return max(dates) if dates else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("variant")
    ap.add_argument("--today", default=datetime.date.today().isoformat())
    args = ap.parse_args()
    if args.variant not in VARIANTS:
        print(f"STOP: unknown variant '{args.variant}'. One of: {', '.join(VARIANTS)}.")
        return 2

    root = pathlib.Path.cwd()
    today = datetime.date.fromisoformat(args.today)
    since, source = from_memory(args.variant), "the last run in memory.md"
    if not since and args.variant == "learning":
        since, source = from_learnings(root), "the newest date in ## Recent learnings"
    if not since:
        since, source = (today - datetime.timedelta(days=30)).isoformat(), "first run, the last 30 days"

    found = []
    for path in sorted((root / "04-memory" / "sessions").glob("*/*.md")):
        if re.fullmatch(rf"{DATE}\.md", path.name) and since < path.stem <= today.isoformat():
            found.append(path.relative_to(root).as_posix())
    print(f"since {since} ({source})")
    for rel in found:
        print(rel)
    print(f"{len(found)} journals")
    return 0


if __name__ == "__main__":
    sys.exit(main())
