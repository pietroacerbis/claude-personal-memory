#!/usr/bin/env python3
"""Count the two sections distil writes in 04-memory/MEMORY.md against their caps.

    python3 caps.py

Run from the workspace root. A row of `## Mistakes log` is a table row: the header and the
separator line do not count. A row of `## Recent learnings` is a bullet line. A line that
links to the archive is not a row. Prints one line per section, with "over by N" past the
cap. Exit 2 when MEMORY.md or a section is missing. Standard library only.
"""
import pathlib
import re
import sys

CAPS = {"Mistakes log": 25, "Recent learnings": 30}


def section(text: str, name: str):
    m = re.search(rf"(?ms)^## {re.escape(name)}[ \t]*\n(.*?)(?=^## |\Z)", text)
    return m.group(1) if m else None


def rows(name: str, body: str) -> int:
    lines = [line.strip() for line in body.splitlines()]
    if name == "Mistakes log":
        table = [line for line in lines if line.startswith("|")]
        return max(0, len([line for line in table if not re.fullmatch(r"\|[\s:|-]+\|?", line)]) - 1)
    return len([line for line in lines if re.match(r"[-*] |\d+\. ", line)])


def main() -> int:
    memory = pathlib.Path.cwd() / "04-memory" / "MEMORY.md"
    if not memory.is_file():
        print("STOP: no 04-memory/MEMORY.md here. Run from the workspace root, or say 'setup' first.")
        return 2
    text = memory.read_text(encoding="utf-8")
    missing = 0
    for name, cap in CAPS.items():
        body = section(text, name)
        if body is None:
            print(f"{name}: section missing")
            missing += 1
            continue
        n = rows(name, body)
        over = f", over by {n - cap}" if n > cap else ""
        print(f"{name}: {n} of {cap}{over}")
    return 2 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
