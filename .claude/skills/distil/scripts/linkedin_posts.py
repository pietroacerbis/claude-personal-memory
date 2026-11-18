#!/usr/bin/env python3
"""Print the newest posts with text from a LinkedIn data export.

    python3 linkedin_posts.py PATH [--max 30]

PATH is Shares.csv from the LinkedIn export ("Get a copy of your data"), dropped in
06-sources/raw/. Reads the Date and ShareCommentary columns, skips reshares with no text
of their own, and prints the newest posts first, each under "### Post N, YYYY-MM-DD", then
"N posts with text". Exit 2 when the file is missing or has no ShareCommentary column.
Standard library only.
"""
import argparse
import csv
import pathlib
import sys


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--max", type=int, default=30)
    args = ap.parse_args()
    path = pathlib.Path(args.path)
    if not path.is_file():
        print(f"STOP: {path} not found. Drop Shares.csv from the LinkedIn export in 06-sources/raw/.")
        return 2
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        cols = {c.strip().lower(): c for c in (reader.fieldnames or [])}
        text_col, date_col = cols.get("sharecommentary"), cols.get("date")
        if not text_col:
            print(f"STOP: {path.name} has no ShareCommentary column. Is it Shares.csv?")
            return 2
        posts = []
        for row in reader:
            text = (row.get(text_col) or "").strip().strip('"').strip()
            if text:
                posts.append(((row.get(date_col) or "") if date_col else "", text))
    posts.sort(key=lambda p: p[0], reverse=True)
    posts = posts[: args.max]
    for i, (date, text) in enumerate(posts, start=1):
        print(f"### Post {i}, {date[:10] or 'undated'}\n\n{text}\n")
    print(f"{len(posts)} posts with text")
    return 0


if __name__ == "__main__":
    sys.exit(main())
