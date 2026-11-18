#!/usr/bin/env python3
"""Write one event line into log.md, as the first line under "## Entries".

    python3 log_line.py "YYYY-MM-DD | [area] what changed -> path"

Run from the workspace root. Refuses, with exit 2: no log.md, no "## Entries" heading, a
line not in the shape above, a path after "->" that does not exist. The log is newest
first and never rewritten, so the line goes on top and nothing below it moves.
Standard library only.
"""
import pathlib
import re
import sys

SHAPE = r"\d{4}-\d{2}-\d{2} \| \[[a-z0-9]+(?:-[a-z0-9]+)*\] \S.* -> (\S+)"


def main() -> int:
    if len(sys.argv) != 2:
        print('usage: log_line.py "YYYY-MM-DD | [area] what changed -> path"')
        return 2
    line = sys.argv[1].strip()
    m = re.fullmatch(SHAPE, line)
    if not m:
        print("STOP: the line must read 'YYYY-MM-DD | [area] what changed -> path', area in kebab-case.")
        return 2
    root = pathlib.Path.cwd()
    if not (root / m.group(1)).exists():
        print(f"STOP: {m.group(1)} does not exist. The path is the file that holds the change now.")
        return 2
    log = root / "log.md"
    if not log.is_file():
        print("STOP: no log.md here. Run from the workspace root.")
        return 2
    text = log.read_text(encoding="utf-8")
    head = re.search(r"(?m)^## Entries[ \t]*\n", text)
    if not head:
        print("STOP: log.md has no '## Entries' heading.")
        return 2
    rest = text[head.end():].lstrip("\n")
    log.write_text(text[: head.end()] + "\n" + line + "\n" + rest, encoding="utf-8")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
