#!/usr/bin/env python3
"""Open today's journal and claim the next session block in it.

    python3 claim_session.py WORKSTREAM [--day YYYY-MM-DD]

Run from the workspace root, the folder that holds USER.md. Creates
04-memory/sessions/YYYY-MM/YYYY-MM-DD.md when it is missing, appends
"## Session N, HH:MM, WORKSTREAM" with its empty fields, and keeps "sessions: N"
equal to the number of blocks. Two chats claiming at once get two numbers: a lock
folder makes the claim atomic.

Prints the number claimed. Exit 2 with the reason on any failure.
Standard library only.
"""
import argparse
import datetime
import pathlib
import re
import sys
import time

HEADER = "# Day {day}\n\nsessions: 0\n"
BLOCK = """
## Session {n}, {time}, {workstream}

**Status:** open
**Scope:** [session-start]
**Opened:** [session-start]
**Done:** [session-end]
**Decisions:** [session-end]
**Carries:** [session-end]
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("workstream")
    ap.add_argument("--day", default=datetime.date.today().isoformat())
    args = ap.parse_args()

    root = pathlib.Path.cwd()
    if not (root / "USER.md").is_file():
        print("STOP: no USER.md here. Run from the workspace root, or say 'setup' first.")
        return 2
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", args.workstream):
        print(f"STOP: workstream '{args.workstream}' must be kebab-case, for example 'pricing-page'.")
        return 2
    journal = root / "04-memory" / "sessions" / args.day[:7] / f"{args.day}.md"
    journal.parent.mkdir(parents=True, exist_ok=True)

    lock = journal.with_suffix(".lock")
    for _ in range(50):
        try:
            lock.mkdir()
            break
        except FileExistsError:
            time.sleep(0.1)
    else:
        print(f"STOP: {lock} is held by another chat. Try again in a few seconds.")
        return 2
    try:
        if not journal.exists():
            journal.write_text(HEADER.format(day=args.day), encoding="utf-8")
        text = journal.read_text(encoding="utf-8")
        n = len(re.findall(r"(?m)^## Session ", text)) + 1
        text += BLOCK.format(n=n, time=datetime.datetime.now().strftime("%H:%M"), workstream=args.workstream)
        text = re.sub(r"(?m)^sessions: \d+$", f"sessions: {n}", text, count=1)
        journal.write_text(text, encoding="utf-8")
    finally:
        lock.rmdir()
    print(n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
