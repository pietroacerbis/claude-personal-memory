#!/usr/bin/env python3
"""Keep a source as it came, in 06-sources/raw/, under one header line.

    python3 save_raw.py SLUG --origin "TEXT" [--from FILE] [--day YYYY-MM-DD] < source

Run from the workspace root, the folder that holds USER.md. Reads the source from
--from FILE, or from stdin, and writes 06-sources/raw/YYYY-MM-DD-SLUG.md:

    Origin: TEXT | saved: YYYY-MM-DD

    the source, unchanged

Never overwrites: a name already taken gets -2, -3. The same text already saved
in raw/ returns that file instead of a second copy. A --from file already inside
06-sources/raw/ is used as it is. The last line printed is the raw file's path.

Exit 2 with the reason: no USER.md, a slug that is not kebab-case, a bad --day,
an origin on two lines, a source that is missing, empty or not text, or one that
carries a key (the patterns of .claude/hooks/secrets-guard.py, when the workspace
has it). Standard library only.
"""
import argparse
import datetime
import importlib.util
import pathlib
import re
import sys

RAW = pathlib.Path("06-sources") / "raw"
HEADER = "Origin: {origin} | saved: {day}\n\n"


def stop(reason: str) -> int:
    print(f"STOP: {reason}")
    return 2


def key_patterns(root: pathlib.Path) -> list:
    guard = root / ".claude" / "hooks" / "secrets-guard.py"
    if not guard.is_file():
        return []
    try:
        spec = importlib.util.spec_from_file_location("secrets_guard", guard)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return list(getattr(module, "PATTERNS", []))
    except Exception:
        return []


def body_of(path: pathlib.Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    if text.startswith("Origin: ") and "\n\n" in text:
        return text.split("\n\n", 1)[1]
    return text


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--origin", required=True)
    ap.add_argument("--from", dest="source")
    ap.add_argument("--day", default=datetime.date.today().isoformat())
    args = ap.parse_args()

    root = pathlib.Path.cwd().resolve()
    if not (root / "USER.md").is_file():
        return stop("no USER.md here. Run from the workspace root, or say 'setup' first.")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", args.slug):
        return stop(f"slug '{args.slug}' must be kebab-case, for example 'call-quillmoor'.")
    try:
        datetime.date.fromisoformat(args.day)
    except ValueError:
        return stop(f"--day '{args.day}' is not a date in the form YYYY-MM-DD.")
    origin = args.origin.strip()
    if not origin or "\n" in origin:
        return stop("--origin must be one line naming where the source came from.")

    raw_dir = root / RAW
    if args.source:
        src = pathlib.Path(args.source).expanduser()
        if not src.is_absolute():
            src = root / src
        if not src.is_file():
            return stop(f"cannot read {args.source}: no such file.")
        src = src.resolve()
        if src.parent == raw_dir.resolve():
            print("kept as it is, already in 06-sources/raw/")
            print(src.relative_to(root).as_posix())
            return 0
        try:
            text = src.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            return stop(f"{args.source} is not text. Read it with the Read tool and pass the text on stdin.")
    else:
        text = sys.stdin.read()
    if not text.strip():
        return stop("the source is empty.")
    for pattern, what in key_patterns(root):
        if re.search(pattern, text):
            return stop(f"the source carries what looks like {what}. A key never enters the workspace: "
                        "remove it from the source and hand it over again.")

    raw_dir.mkdir(parents=True, exist_ok=True)
    for old in sorted(raw_dir.glob("*.md")):
        if body_of(old).strip() == text.strip():
            print("already saved, the same text")
            print(old.relative_to(root).as_posix())
            return 0
    n = 1
    while True:
        suffix = "" if n == 1 else f"-{n}"
        target = raw_dir / f"{args.day}-{args.slug}{suffix}.md"
        try:
            with open(target, "x", encoding="utf-8") as f:
                f.write(HEADER.format(origin=origin, day=args.day) + text)
            break
        except FileExistsError:
            n += 1
    print(target.relative_to(root).as_posix())
    return 0


if __name__ == "__main__":
    sys.exit(main())
