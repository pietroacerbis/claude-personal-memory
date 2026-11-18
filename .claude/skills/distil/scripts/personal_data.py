#!/usr/bin/env python3
"""Check a voice file for personal data a pattern can see.

    python3 personal_data.py FILE

Flags, with the line number: an email address, a phone number, a link, an @handle.
It cannot see a name: the excerpts are still read by eye before they are written.
Exit 0 when clean, 1 with one line per hit, 2 when FILE is missing. Standard library only.
"""
import pathlib
import re
import sys

PATTERNS = [
    ("an email address", r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+"),
    ("a link", r"https?://\S+|www\.\S+|lnkd\.in/\S+"),
    ("an @handle", r"(?<![\w.])@[A-Za-z0-9_]{2,}"),
]


def has_phone(line: str) -> bool:
    """Nine digits or more in one run of digits, spaces, dots, dashes and brackets. A date is not one."""
    for m in re.finditer(r"(?<![\w-])\+?\d[\d ().-]{6,}\d(?![\w-])", line):
        if not re.search(r"\d{4}-\d{2}-\d{2}", m.group(0)) and len(re.sub(r"\D", "", m.group(0))) >= 9:
            return True
    return False


def main() -> int:
    if len(sys.argv) != 2 or not pathlib.Path(sys.argv[1]).is_file():
        print("STOP: usage personal_data.py FILE, and the file must exist.")
        return 2
    hits = 0
    for n, line in enumerate(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").splitlines(), start=1):
        found = [what for what, pattern in PATTERNS if re.search(pattern, line)]
        found += ["a phone number"] if has_phone(line) else []
        for what in found:
            print(f"line {n}: {what}")
            hits += 1
    if hits:
        print(f"{hits} hits: remove them, then run this check again.")
        return 1
    print(f"clean: no email, phone number, link or @handle in {sys.argv[1]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
