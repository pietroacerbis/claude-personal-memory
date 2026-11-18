#!/usr/bin/env python3
"""Refuse a write that would put a secret into a file of this workspace.

Runs before every Write and Edit (.claude/settings.json). Two refusals:
  - a write to .env, where live keys live, outside what Claude should touch;
  - content carrying the shape of a key or a token.
A refusal exits 2 with the reason, which Claude reads. Anything it cannot inspect passes.
"""
import json
import re
import sys

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


def main() -> int:
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except Exception:
        return 0
    tool_input = data.get("tool_input") or {}
    path = str(tool_input.get("file_path", ""))
    if path == ".env" or path.endswith("/.env"):
        sys.stderr.write("BLOCKED: .env holds live keys. Ask the user to edit it by hand.\n")
        return 2
    content = str(tool_input.get("content") or tool_input.get("new_string") or "")
    for pattern, what in PATTERNS:
        if re.search(pattern, content):
            sys.stderr.write(
                f"BLOCKED: this write carries what looks like {what}. A key never goes into a file "
                "of the workspace: write where it is kept (for example 'in .env, as OPENAI_API_KEY'), never its value.\n"
            )
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
