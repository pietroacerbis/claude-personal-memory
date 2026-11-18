#!/usr/bin/env python3
"""Search the places index.md leaves out, and print every match newest first.

    python3 search.py PATTERN [--all] [--archive] [--max N]

Run from the workspace root, the folder that holds USER.md. PATTERN is one
case-insensitive regular expression, for example "northwind|pilot start".

By default it searches the four places index.md does not describe line by line:
the day journals in 04-memory/sessions/, 04-memory/decisions/, log.md and
06-sources/. --all searches every text file of the workspace instead. Archive
folders stay out unless --archive is given, since what they hold is no longer live.

Each match carries a date: the date the line starts with (a log.md or history.md
line), else the `date:` in the file's frontmatter, else the last date in the
file's path, else "undated". Newest first, at most --max matches (default 25).
A decision file shows its `status`. Every place with no match is named, so the
answer can say what was checked. Writes nothing.

Exit 2 with the reason when USER.md is missing or PATTERN is not valid.
Standard library only.
"""
import argparse
import pathlib
import re
import sys

PLACES = ["04-memory/sessions", "04-memory/decisions", "log.md", "06-sources"]
SKIP_DIRS = {".git", ".claude", "node_modules", "__pycache__"}
ARCHIVE_DIRS = {"archive", "03-archive", "04-archive"}
TEXT = {".md", ".txt", ".csv", ".json", ".yaml", ".yml", ".vtt", ".srt"}
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
LINE_DATE = re.compile(r"\s*[-*]?\s*(\d{4}-\d{2}-\d{2})\b")
WIDTH = 200


def files(base: pathlib.Path, archive: bool):
    if base.is_file():
        yield base
        return
    for f in sorted(base.rglob("*")):
        dirs = set(f.relative_to(base).parts[:-1])
        if dirs & SKIP_DIRS or any(d.startswith(".") for d in dirs):
            continue
        if not archive and dirs & ARCHIVE_DIRS:
            continue
        if f.is_file() and f.suffix.lower() in TEXT and f.name != "index.md":
            yield f


def frontmatter(lines: list) -> dict:
    meta = {}
    if lines and lines[0].strip() == "---":
        for line in lines[1:]:
            if line.strip() == "---":
                break
            m = re.match(r"(date|status):\s*(.+)", line.strip())
            if m:
                meta[m.group(1)] = m.group(2).strip().strip("\"'")
    return meta


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pattern")
    ap.add_argument("--all", action="store_true", help="search every text file, not only the four places")
    ap.add_argument("--archive", action="store_true", help="include archive folders")
    ap.add_argument("--max", type=int, default=25)
    args = ap.parse_args()

    root = pathlib.Path.cwd()
    if not (root / "USER.md").is_file():
        print("STOP: no USER.md here. Run from the workspace root, or say 'setup' first.")
        return 2
    try:
        rx = re.compile(args.pattern, re.IGNORECASE)
    except re.error as e:
        print(f"STOP: '{args.pattern}' is not a valid regular expression: {e}")
        return 2

    places = ["."] if args.all else PLACES
    matches, empty, missing = [], [], []
    for place in places:
        base = root / place
        if not base.exists():
            missing.append(place)
            continue
        found = 0
        for f in files(base, args.archive):
            rel = f.relative_to(root).as_posix()
            lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
            meta = frontmatter(lines)
            in_path = DATE.findall(rel)
            file_date = meta.get("date") if DATE.fullmatch(meta.get("date", "")) else (in_path[-1] if in_path else "")
            tag = f" [status: {meta['status']}]" if "status" in meta else ""
            for n, line in enumerate(lines, start=1):
                if not rx.search(line):
                    continue
                m = LINE_DATE.match(line)
                when = m.group(1) if m else file_date
                text = line.strip()
                if len(text) > WIDTH:
                    text = text[:WIDTH] + "..."
                matches.append((when, f"{when or 'undated':<10}  {rel}:{n}{tag}  {text}"))
                found += 1
        if not found:
            empty.append(place)

    where = "the whole workspace" if args.all else ", ".join(PLACES)
    print(f'search "{args.pattern}" in {where}' + ("" if args.archive else ", archives out"))
    matches.sort(key=lambda m: m[0], reverse=True)
    for _, out in matches[: args.max]:
        print(out)
    if len(matches) > args.max:
        print(f"{len(matches) - args.max} more matches not shown, older or undated: narrow the pattern")
    if not matches:
        print("no match anywhere searched")
    elif empty:
        print("no match in: " + ", ".join(empty))
    if missing:
        print("missing: " + ", ".join(missing))
    return 0


if __name__ == "__main__":
    sys.exit(main())
