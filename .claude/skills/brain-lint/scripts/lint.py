#!/usr/bin/env python3
"""Check the workspace and print what is broken, one finding per line, each with its fix.

    python3 .claude/skills/brain-lint/scripts/lint.py

Run from the workspace root, the folder that holds USER.md. Prints one line per finding,
`path:line  check  message`, then the total. Line 0 means the finding is about a whole
file or folder. Exit 0 when clean, 1 with findings, 2 when the folder is not a workspace.
It reads and never writes. Standard library only.

    index       index.md differs from what reindex.py would write
    link        a relative markdown link to a file that does not exist
    cap         a MEMORY.md section over the cap in the table of 04-memory/README.md
    project     a folder of 02-projects/ missing map.md, latest.md or history.md
    workstream  a folder of 01-workstreams/ missing README.md or one of its three folders
    log         a line under ## Entries of log.md not shaped YYYY-MM-DD | [area] text -> path
    session     a journal block still open on a day before today
    decision    a file of 04-memory/decisions/ missing description, date or status
    secret      a key-shaped string in a .md file
"""
import datetime
import re
import sys
from pathlib import Path
from urllib.parse import unquote

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import reindex  # noqa: E402

CHECKS = ["index", "link", "cap", "project", "workstream", "log", "session", "decision", "secret"]
SKIP_DIRS = {".git", "node_modules", "__pycache__"}
ARCHIVE_DIRS = {"archive", "03-archive", "04-archive"}

# Copied from .claude/hooks/secrets-guard.py, which lives outside this skill. Keep the two lists equal.
PATTERNS = [
    (r"\bsk-[A-Za-z0-9_-]{20,}", "an API key"),
    (r"xox[baprs]-[A-Za-z0-9-]{10,}", "a Slack token"),
    (r"gh[pousr]_[A-Za-z0-9]{20,}", "a GitHub token"),
    (r"github_pat_[A-Za-z0-9_]{20,}", "a GitHub token"),
    (r"AIza[0-9A-Za-z_-]{35}", "a Google API key"),
    (r"AKIA[0-9A-Z]{16}", "an AWS access key"),
    (r"secret_[A-Za-z0-9]{32,}", "a Notion token"),
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "a private key"),
]

INLINE_LINK = re.compile(r"!?\[(?:[^\]\\]|\\.)*\]\(\s*(<[^>]*>|[^)\s]+)(?:\s+[\"'(][^)]*)?\)")
REF_DEF = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(<[^>]*>|\S+)")
CODE_SPAN = re.compile(r"(`+)(?:.+?)\1")
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+\S")
TABLE_SEP = re.compile(r"^\|?\s*:?-+:?\s*(?:\|\s*:?-+:?\s*)*\|?$")
CAP_ROW = re.compile(r"^\|\s*`MEMORY\.md`,\s*`##\s*([^`]+?)\s*`\s*\|.*\|\s*(\d+)\s+(lines?|rows?)\s*\|\s*$")
LOG_LINE = re.compile(r"^(\d{4}-\d{2}-\d{2}) \| \[[^\]\s][^\]]*\] \S.* -> \S+$")
SESSION_HEAD = re.compile(r"^## Session (\d+), [0-9:]+, (\S+)")


def rel(base, path):
    return Path(path).relative_to(base).as_posix()


def md_files(base):
    """Every .md of the workspace. Hidden folders stay out except .claude; eval fixtures stay out."""
    out = []
    for path in sorted(base.rglob("*.md")):
        parts = path.relative_to(base).parts
        if any(p in SKIP_DIRS for p in parts):
            continue
        if any(p.startswith(".") and p != ".claude" for p in parts[:-1]):
            continue
        if len(parts) > 3 and parts[:2] == (".claude", "skills") and parts[3] == "evals":
            continue
        out.append(path)
    return out


def read_lines(path):
    try:
        return path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return []


def prose_lines(lines):
    """Yield (number, text) for the lines outside code fences, indented code and HTML comments,
    with inline code removed."""
    fence = None
    in_comment = False
    for n, line in enumerate(lines, start=1):
        s = line.strip()
        if fence:
            if s.startswith(fence):
                fence = None
            continue
        if s.startswith("```") or s.startswith("~~~"):
            fence = s[:3]
            continue
        if (line.startswith("    ") or line.startswith("\t")) and not LIST_ITEM.match(line):
            continue
        if in_comment:
            if "-->" not in line:
                continue
            line = line.split("-->", 1)[1]
            in_comment = False
        line = re.sub(r"<!--.*?-->", "", line)
        if "<!--" in line:
            line = line.split("<!--", 1)[0]
            in_comment = True
        yield n, CODE_SPAN.sub("", line)


def check_index(base):
    script = Path(reindex.__file__).resolve()
    try:
        shown = script.relative_to(base.resolve()).as_posix()
    except ValueError:
        shown = str(script)
    fix = f"Fix: run python3 {shown}"
    target = base / "index.md"
    if not target.is_file():
        return [("index.md", 0, f"missing. {fix}")]
    old = target.read_text(encoding="utf-8")
    new = reindex.render(base)
    if old == new:
        return []

    def entries(text):
        found = {}
        for line in text.splitlines():
            m = re.match(r"^- \[([^\]]+)\]", line)
            if m:
                found[m.group(1)] = line
        return found

    o, nw = entries(old), entries(new)
    missing = sorted(set(nw) - set(o))
    gone = sorted(set(o) - set(nw))
    changed = sorted(k for k in set(o) & set(nw) if o[k] != nw[k])
    parts = []
    if missing:
        parts.append(f"{len(missing)} not listed ({', '.join(missing[:3])}{', ...' if len(missing) > 3 else ''})")
    if gone:
        parts.append(f"{len(gone)} listed but gone ({', '.join(gone[:3])}{', ...' if len(gone) > 3 else ''})")
    if changed:
        parts.append(f"{len(changed)} with a changed description")
    what = "; ".join(parts) if parts else "its header or order differs"
    return [("index.md", 1, f"stale: {what}. {fix}")]


def check_links(base, files):
    findings = []
    for path in files:
        r = rel(base, path)
        parts = Path(r).parts
        # Journals are a record that is searched, never navigated: a link that pointed at a file
        # since moved stays as it was written, as reindex.py also leaves the journals out.
        if r == "index.md" or r.startswith(("06-sources/raw/", "04-memory/sessions/")) or any(p in ARCHIVE_DIRS for p in parts):
            continue
        for n, line in prose_lines(read_lines(path)):
            targets = [m.group(1) for m in INLINE_LINK.finditer(line)]
            m = REF_DEF.match(line)
            if m:
                targets.append(m.group(1))
            for t in targets:
                t = t.strip("<>").strip()
                # Relative links only: a URL, an anchor, or a path from / (a site path in a saved web page) is skipped.
                if not t or t.startswith(("#", "/")) or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", t):
                    continue
                if any(c in t for c in "{}*$") or "YYYY" in t:
                    continue
                t = unquote(t.split("#", 1)[0].split("?", 1)[0])
                if not t:
                    continue
                if not (path.parent / t).exists():
                    findings.append((r, n, f"links to {t}, which does not exist. Fix: point it at the file's new home, or keep the text and drop the link"))
    return findings


def count_entries(lines):
    """Bullets, plus table rows that are neither a header nor a separator."""
    n = 0
    fence = False
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("```") or s.startswith("~~~"):
            fence = not fence
            continue
        if fence:
            continue
        if LIST_ITEM.match(line):
            n += 1
        elif s.startswith("|"):
            nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
            if TABLE_SEP.match(s) or TABLE_SEP.match(nxt):
                continue
            n += 1
    return n


def check_caps(base):
    memory = base / "04-memory" / "MEMORY.md"
    readme = base / "04-memory" / "README.md"
    if not memory.is_file():
        return []
    caps = {}
    for line in read_lines(readme):
        m = CAP_ROW.match(line.strip())
        if m:
            caps[m.group(1).strip().lower()] = (m.group(1).strip(), int(m.group(2)), "rows" if m.group(3).startswith("row") else "lines")
    if not caps:
        return [("04-memory/README.md", 0, "no caps found, so MEMORY.md was not checked. Fix: keep the rows shaped | `MEMORY.md`, `## Section` | what | N lines |")]
    lines = read_lines(memory)
    heads = []
    for i, line in enumerate(lines):
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            heads.append((i, m.group(1)))
    findings = []
    for start, name in heads:
        cap = caps.get(name.lower())
        if not cap:
            continue
        end = len(lines)
        for j in range(start + 1, len(lines)):
            if re.match(r"^#{1,2}\s", lines[j]):
                end = j
                break
        count = count_entries(lines[start + 1:end])
        _, limit, unit = cap
        if count > limit:
            slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
            findings.append(("04-memory/MEMORY.md", start + 1,
                             f"## {name} has {count} {unit}, cap {limit}. Fix: move the {count - limit} oldest to "
                             f"04-memory/archive/{slug}.md and leave a link to it under the section"))
    return findings


def check_projects(base):
    folder = base / "02-projects"
    if not folder.is_dir():
        return []
    fixes = {
        "map.md": "copy 02-projects/_TEMPLATE/map.md and fill its head: what it produces, why now, when it is done",
        "latest.md": "copy 02-projects/_TEMPLATE/latest.md and fill where the project stands, from its history.md",
        "history.md": "copy 02-projects/_TEMPLATE/history.md, its first line the day the project opened",
    }
    findings = []
    for d in sorted(p for p in folder.iterdir() if p.is_dir()):
        if d.name.startswith(("_", ".")) or d.name == "archive":
            continue
        for name, fix in fixes.items():
            if not (d / name).is_file():
                findings.append((rel(base, d / name), 0, f"missing. Fix: {fix}"))
    return findings


def check_workstreams(base):
    folder = base / "01-workstreams"
    if not folder.is_dir():
        return []
    findings = []
    for d in sorted(p for p in folder.iterdir() if p.is_dir()):
        if d.name.startswith(("_", ".")) or d.name == "archive":
            continue
        if not (d / "README.md").is_file():
            findings.append((rel(base, d / "README.md"), 0, "missing. Fix: write one line on what the area is for, and its three folders"))
        for sub in ("01-knowledge", "02-artifacts", "03-archive"):
            if not (d / sub).is_dir():
                findings.append((rel(base, d / sub) + "/", 0, "missing. Fix: create it, with an empty .gitkeep so git keeps it"))
    return findings


def check_log(base):
    log = base / "log.md"
    if not log.is_file():
        return [("log.md", 0, "missing. Fix: restore it from the kit, with its ## Entries heading")]
    lines = read_lines(log)
    start = next((i for i, line in enumerate(lines) if line.strip() == "## Entries"), None)
    if start is None:
        return [("log.md", 0, "has no ## Entries heading. Fix: add it after the intro; the entries go under it")]
    findings = []
    shape = "`YYYY-MM-DD | [area] what changed -> path`"
    for i in range(start + 1, len(lines)):
        s = lines[i].strip()
        if s.startswith("## "):
            break
        if not s:
            continue
        m = LOG_LINE.match(s)
        if not m:
            findings.append(("log.md", i + 1, f"not shaped {shape}. Fix: reshape it, keeping its date and its words"))
            continue
        try:
            datetime.date.fromisoformat(m.group(1))
        except ValueError:
            findings.append(("log.md", i + 1, f"{m.group(1)} is not a real day. Fix: correct the date"))
    return findings


def check_sessions(base, today):
    findings = []
    for path in sorted((base / "04-memory" / "sessions").glob("*/*.md")):
        try:
            day = datetime.date.fromisoformat(path.stem)
        except ValueError:
            continue
        if day >= today:
            continue
        head = None
        for n, line in enumerate(read_lines(path), start=1):
            m = SESSION_HEAD.match(line)
            if m:
                head = m
            elif line.strip() == "**Status:** open":
                who = f"session {head.group(1)}, {head.group(2)}," if head else "a session"
                findings.append((rel(base, path), n, f"{who} opened {path.stem}, is still open. "
                                 f"Fix: close it with session-end, giving it the day {path.stem}"))
    return findings


def check_decisions(base):
    folder = base / "04-memory" / "decisions"
    if not folder.is_dir():
        return []
    findings = []
    for path in sorted(folder.glob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        lines = read_lines(path)
        r = rel(base, path)
        fields = {}
        if lines and lines[0].strip() == "---":
            for line in lines[1:]:
                if line.strip() == "---":
                    break
                m = re.match(r"^([A-Za-z_]+):\s*(.*?)\s*$", line)
                if m:
                    fields[m.group(1)] = m.group(2).strip("\"'")
        else:
            findings.append((r, 1, "has no frontmatter. Fix: add description, date and status at the top, as in 04-memory/decisions/README.md"))
            continue
        lacking = [k for k in ("description", "date", "status") if not fields.get(k)]
        if lacking:
            findings.append((r, 1, f"frontmatter lacks {', '.join(lacking)}. Fix: add {'them' if len(lacking) > 1 else 'it'}; "
                             "the date is in the file name, status is active or superseded"))
    return findings


def check_secrets(base, files):
    findings = []
    for path in files:
        for n, line in enumerate(read_lines(path), start=1):
            for pattern, what in PATTERNS:
                if re.search(pattern, line):
                    findings.append((rel(base, path), n, f"looks like {what}. Fix: delete the value, write where the key is kept "
                                     "(for example 'in .env, as API_KEY'), and revoke the key if this file was ever pushed"))
                    break
    return findings


def main():
    base = Path.cwd()
    if not (base / "USER.md").is_file():
        print("STOP: no USER.md here. Run from the workspace root, or say 'setup' first.")
        return 2
    files = md_files(base)
    results = {
        "index": check_index(base),
        "link": check_links(base, files),
        "cap": check_caps(base),
        "project": check_projects(base),
        "workstream": check_workstreams(base),
        "log": check_log(base),
        "session": check_sessions(base, datetime.date.today()),
        "decision": check_decisions(base),
        "secret": check_secrets(base, files),
    }
    total = 0
    for check in CHECKS:
        for path, line, message in results[check]:
            print(f"{path}:{line}  {check}  {message}")
            total += 1
    if not total:
        print("0 findings: the workspace is clean")
        return 0
    counts = ", ".join(f"{c} {len(results[c])}" for c in CHECKS if results[c])
    print(f"{total} finding{'s' if total != 1 else ''}: {counts}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
