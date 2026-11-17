#!/usr/bin/env python3
"""Close one session block of the journal, and hand tomorrow what it needs.

    python3 close_session.py WORKSTREAM BODY_FILE [--day YYYY-MM-DD] [--carry CARRY_FILE]

Run from the workspace root. BODY_FILE holds the close fields as they will read,
starting at "**Done:**". The script fills the open block whose heading carries
WORKSTREAM and flips its Status to closed. Scope and Opened belong to the opening
and are never touched. --day is the day the session OPENED, needed when the close
comes after midnight. --carry appends the file's lines to "## Carryover in" of the
next day's journal, creating it when missing.

Refuses, with exit 2: no block for WORKSTREAM, more than one, a block already
closed, a body that does not start at **Done:**. Standard library only.
"""
import argparse
import datetime
import pathlib
import re
import sys


def journal_path(root: pathlib.Path, day: str) -> pathlib.Path:
    return root / "04-memory" / "sessions" / day[:7] / f"{day}.md"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("workstream")
    ap.add_argument("body_file")
    ap.add_argument("--day", default=datetime.date.today().isoformat())
    ap.add_argument("--carry")
    args = ap.parse_args()

    root = pathlib.Path.cwd()
    journal = journal_path(root, args.day)
    if not journal.is_file():
        print(f"STOP: no journal for {args.day}. Pass --day with the day the session opened.")
        return 2
    body = pathlib.Path(args.body_file).read_text(encoding="utf-8").strip()
    if not body.startswith("**Done:**"):
        print("STOP: the body must start at **Done:**.")
        return 2

    text = journal.read_text(encoding="utf-8")
    blocks = list(re.finditer(rf"(?ms)^## Session (\d+), [0-9:]+, {re.escape(args.workstream)}\s*$(.*?)(?=^## |\Z)", text))
    if not blocks:
        print(f"STOP: no session block for '{args.workstream}' in {journal}.")
        return 2
    if len(blocks) > 1:
        print(f"STOP: {len(blocks)} blocks carry '{args.workstream}'. Close by hand which one, or rename one.")
        return 2
    block = blocks[0]
    content = block.group(2)
    if "**Status:** closed" in content:
        print(f"STOP: session {block.group(1)} is already closed.")
        return 2
    kept = content.split("**Done:**")[0].replace("**Status:** open", "**Status:** closed")
    text = text[: block.start(2)] + kept + body + "\n" + ("\n" if block.end() < len(text) else "") + text[block.end():]
    journal.write_text(text, encoding="utf-8")

    if args.carry:
        lines = pathlib.Path(args.carry).read_text(encoding="utf-8").strip()
        nxt = (datetime.date.fromisoformat(args.day) + datetime.timedelta(days=1)).isoformat()
        tomorrow = journal_path(root, nxt)
        tomorrow.parent.mkdir(parents=True, exist_ok=True)
        if not tomorrow.exists():
            tomorrow.write_text(f"# Day {nxt}\n\nsessions: 0\n\n## Carryover in\n", encoding="utf-8")
        t = tomorrow.read_text(encoding="utf-8")
        entry = f"\nFrom {args.day}, session {block.group(1)}, {args.workstream}:\n{lines}\n"
        if "## Carryover in" in t:
            head, _, rest = t.partition("## Carryover in\n")
            nxt_heading = re.search(r"(?m)^## ", rest)
            cut = nxt_heading.start() if nxt_heading else len(rest)
            section = rest[:cut].strip("\n")
            t = head + "## Carryover in\n" + (("\n" + section + "\n") if section else "") + entry + ("\n" + rest[cut:] if nxt_heading else "")
        else:
            t = t.rstrip("\n") + "\n\n## Carryover in\n" + entry
        tomorrow.write_text(t, encoding="utf-8")

    print(block.group(1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
