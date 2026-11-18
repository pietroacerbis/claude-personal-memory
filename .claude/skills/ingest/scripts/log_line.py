#!/usr/bin/env python3
"""Check one log line and insert it at the top of log.md, under ## Entries.

    python3 log_line.py "YYYY-MM-DD | [area] what changed -> path"

Run from the workspace root, the folder that holds USER.md. The line must be one
line: a real date, an area in kebab-case, what changed, and the path of a file
or folder that exists in the workspace. It goes first under "## Entries", so the
log stays newest first. A log.md or an Entries heading that is missing is created.

Exit 2 with the reason: no USER.md, a line out of shape, a path that does not
exist or leaves the workspace, a line already in the log (a line is written once,
never rewritten). Prints the line written. Standard library only.
"""
import argparse
import datetime
import pathlib
import re
import sys

SHAPE = re.compile(r"(\d{4}-\d{2}-\d{2}) \| \[([a-z0-9]+(?:-[a-z0-9]+)*)\] (\S.*?) -> (\S+)")
ENTRIES = re.compile(r"(?m)^## Entries[ \t]*\n?")


def stop(reason: str) -> int:
    print(f"STOP: {reason}")
    return 2


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("line")
    args = ap.parse_args()

    root = pathlib.Path.cwd().resolve()
    if not (root / "USER.md").is_file():
        return stop("no USER.md here. Run from the workspace root, or say 'setup' first.")
    line = args.line.strip()
    if "\n" in line:
        return stop("the log line must be one line.")
    m = SHAPE.fullmatch(line)
    if not m:
        return stop("the line must read 'YYYY-MM-DD | [area] what changed -> path', area in kebab-case.")
    try:
        datetime.date.fromisoformat(m.group(1))
    except ValueError:
        return stop(f"{m.group(1)} is not a real date.")
    target = (root / m.group(4)).resolve()
    if root != target and root not in target.parents:
        return stop(f"{m.group(4)} is outside the workspace. Give the path from the workspace root.")
    if not target.exists():
        return stop(f"{m.group(4)} does not exist. The path is the file that holds the change now.")

    log = root / "log.md"
    text = log.read_text(encoding="utf-8") if log.exists() else "# Log\n\n## Entries\n"
    if any(existing.strip() == line for existing in text.splitlines()):
        return stop("this line is already in log.md. A line is written once.")
    heading = ENTRIES.search(text)
    if not heading:
        text = text.rstrip("\n") + "\n\n## Entries\n"
        heading = ENTRIES.search(text)
    rest = text[heading.end():].lstrip("\n")
    log.write_text(text[: heading.start()] + "## Entries\n\n" + line + "\n" + rest, encoding="utf-8")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
