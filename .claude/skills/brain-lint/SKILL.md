---
name: brain-lint
description: "Check the workspace and report what is broken, each finding with its fix: a stale index.md, a link to a file that is gone, a memory section over its cap, a project or an area missing a file, a log line out of shape, a session left open, a decision missing its fields, a key written into a file. Fixes only on your yes. Not for: merging corrections that keep coming back into one sharper rule (distil), closing a session, even one this check finds left open (session-end)."
when_to_use: "Once a week, after a big change such as a folder moved or renamed, or when a link or the index feels off. Triggers: 'brain lint', 'check the workspace', 'what is broken', 'health check', '/brain-lint', 'fai il lint', 'controlla il workspace', 'cosa non va nel workspace', 'controlla i link'."
goal: "Every link opens, the index is current and the memory stays under its caps, so each session reads a workspace it can trust."
outcome: "the report in chat; on a yes, the fixed files, with rows over a cap moved to 04-memory/archive/{section}.md"
inputs:
  required: [workspace-root]
  recommended: [fix-approval]
tier: personal
validation: verifiable
status: active
mcps_used: []
feeds_into: [session-end]
version: 1
last_updated: 2026-11-18
---

# brain-lint

A workspace breaks a little as it grows: a file moves and the links to it point at nothing, the mistakes log passes its cap, a chat ends without its close. One script finds all of it, this skill says how to fix each finding, and it fixes only what the user approves.

The workspace root is the current working directory, where `USER.md` sits: read every file and run every command from there, never from this skill's folder.

## How it works

### Stop 0, memory and the workspace

Read [memory.md](memory.md). Then check `USER.md` in the current working directory with `ls USER.md`. Missing: STOP, say the workspace is not set up yet, and offer to start with "setup", which follows `SETUP.md`.

### Stop 1, run the checks

    python3 ${CLAUDE_SKILL_DIR}/scripts/lint.py

It prints one line per finding, `path:line  check  message`, then the total. Line 0 means a whole file or folder. Exit 0: say in one line that the workspace is clean, and stop. Exit 1: go on. Exit 2: report its line and STOP.

The script is the check. Never re-check by reading what it covers, and never add a finding it did not print. When it missed something the user can see, say so, and write it to [memory.md](memory.md).

| Check | Finds | Fix |
|---|---|---|
| `index` | `index.md` differs from what `reindex.py` would write | run `python3 ${CLAUDE_SKILL_DIR}/scripts/reindex.py` |
| `link` | a relative link to a file that does not exist | search the file name with `find . -name`: one match, point the link at it; none or several, ask |
| `cap` | a `MEMORY.md` section over its cap in `04-memory/README.md` | move the oldest rows to the archive, stop 3 |
| `project` | a project missing `map.md`, `latest.md` or `history.md` | copy the file from `02-projects/_TEMPLATE/`, filled from what the project already holds |
| `workstream` | an area missing `README.md`, `01-knowledge/`, `02-artifacts/` or `03-archive/` | create the folder with an empty `.gitkeep`; a README says in one line what the area is for |
| `log` | a line under `## Entries` of `log.md` out of the shape `YYYY-MM-DD \| [area] what changed -> path` | reshape it, keeping its date and its words |
| `session` | a journal block still open on a day before today | hand it to `session-end` with the day it opened: this skill never closes a block |
| `decision` | a file in `04-memory/decisions/` missing `description`, `date` or `status` | add the field: the date from the file name, `status: active`, a description drafted from its heading |
| `secret` | a key-shaped string in a `.md` file | replace the value with where the key is kept, "in .env, as STRIPE_KEY"; revoking the key is the user's job |

### Stop 2, report

In chat, in the user's language, grouped by check in the order of the table. Under each check, first the script's lines for it, pasted unchanged in a code block, so every path opens as printed. A journal path holds the month twice, as in `04-memory/sessions/2026-11/2026-11-16.md`: keep both. Then each finding in plain words with its fix, naming the file by its base name only: a retyped path loses a folder. End with the total the script printed.

Never quote a secret's value: name the file, the line and the kind of key.

### Stop 3, the gate

Turn the fixes into one numbered list, one item per finding, naming the files it changes and what goes in. A move to the archive is one item, so its two halves are approved together. Then wait for one of:

    approve all · approve 1,3 · skip all

An approval already given in the request counts. A bare "ok" gets one question back. Nothing is written before the answer.

Every fix follows three rules:

- **Never delete a file.** A file in the wrong place moves. A file nobody needs moves to the `archive/` beside it.
- **Rows over a cap move, oldest first.** Oldest by the date a row carries; with no date, the first rows of the section, because a new row goes at the end. They go to the archive file the script names, `04-memory/archive/{section}.md`, appended under `## Moved YYYY-MM-DD`, with the table header when the section is a table. Under the section, after a blank line, leave one plain line, never a bullet or a row: `Older rows: [archive/mistakes-log.md](archive/mistakes-log.md)`. A section keeps one such line, however many moves.
- **The user's words stay the user's.** What an area is for, where a project stands: the fix list carries a draft, marked as a draft, and the file gets what the user approves.

### Stop 4, apply and check again

Apply the approved fixes and nothing else. Then rebuild the index and run the checks a second time:

    python3 ${CLAUDE_SKILL_DIR}/scripts/reindex.py
    python3 ${CLAUDE_SKILL_DIR}/scripts/lint.py

Report the files changed, the new total, and each finding still open with its reason: skipped by the user, or handed to another skill.

## Output

- The report in chat: the findings grouped by check, each with its fix, and the total from the script.
- On a yes: the fixed files, the rows over a cap in `04-memory/archive/{section}.md` with one link left under the section, and the total of the second run.
- STOP record: no `USER.md`, or the script exited 2. The reason goes to the user in one line, and to [memory.md](memory.md).

## References

- What earlier runs taught, read at stop 0: [memory.md](memory.md)
- The nine checks, read only, standard library: [scripts/lint.py](scripts/lint.py)
- The index, also rebuilt after every write by the hook in `.claude/settings.json`: [scripts/reindex.py](scripts/reindex.py)
- The caps and why they exist: `04-memory/README.md`
- Where a session left open goes: `.claude/skills/session-end/SKILL.md`
