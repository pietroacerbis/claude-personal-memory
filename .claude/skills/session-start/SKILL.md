---
name: session-start
description: "Open a working session with your memory loaded: claim a block in today's journal, read who you are, what you corrected before, what yesterday left open and what today's rhythm asks, and brief you in eight lines before any work starts. Not for: closing a session (session-end), the first setup of the workspace (say 'setup'), a quick question that needs no memory."
when_to_use: "At the start of every chat that does real work, the first of the day and the fifth alike. Triggers: 'good morning', 'let's start', 'buongiorno', 'iniziamo', 'ciao claude, iniziamo?', 'resume', 'riprendiamo', or the first task of a new chat."
goal: "Every session starts from what the last one learned, without paying for a memory tool."
outcome: "04-memory/sessions/YYYY-MM/YYYY-MM-DD.md, one block claimed, and the brief in chat"
inputs:
  required: [workspace-root]
  recommended: [session-subject]
tier: personal
validation: verifiable
status: active
mcps_used: []
feeds_into: [session-end]
version: 1
last_updated: 2026-11-17
---

# session-start

The open reads this workspace back, so a new chat starts from what the last one learned. Every open runs the same stops, whatever the hour.

The workspace root is the current working directory, where `USER.md` sits: read every file and run every command from there, never from this skill's folder.

## How it works

### Stop 0, memory and the workspace

Read [memory.md](memory.md). Then check `USER.md` in the current working directory with `ls USER.md`. Missing: STOP, say the workspace is not set up yet, and offer to start with "setup", which follows `SETUP.md`.

### Stop 1, claim the block

Pick a short kebab-case name for the session's subject, from the user's first message: `pricing-page`, `investor-update`. No subject yet: use `general` and rename nothing later.

    python3 ${CLAUDE_SKILL_DIR}/scripts/claim_session.py WORKSTREAM

The script creates today's journal when it is missing and prints the session number. Exit 2: report its line and STOP. Never write a block by hand.

Then fill `**Scope:**` and `**Opened:**` in that block, and nothing else in the file.

### Stop 2, read

Five reads, in this order, each one bounded:

| # | File | What to take |
|---|---|---|
| 1 | `USER.md` | how the user wants to be spoken to |
| 2 | `04-memory/MEMORY.md` | the whole file: quarter goals, roadmap, active work, decisions, the mistakes log, recent learnings |
| 3 | today's journal | `## Carryover in` and the other `## Session` blocks still open |
| 4 | `RHYTHM.md` | the rows whose `Day` is today's weekday, or `daily` |
| 5 | `02-projects/*/latest.md` | only the project the subject names |

A file missing is a line in the brief, never a reason to stop. When the open hook already handed you rows 1 to 4, in a block that starts with "Memory loaded at the open", take them from there and read only what it lacks.

### Stop 3, brief

At most eight lines, in the user's language:

- the session number, and the other sessions still open today
- the carryover lines that bear on this subject
- one mistakes-log row, only when its trigger matches the subject
- the quarter goal the subject moves, when it moves one
- today's rhythm rows, as a question: "Today is Friday: shall we run the weekly review first?"
- where the named project stands, from its `latest.md`

Then ask what the session is about when the first message did not say, and wait.

## Output

- One block claimed in `04-memory/sessions/YYYY-MM/YYYY-MM-DD.md`, with `Scope` and `Opened` filled.
- The brief, in chat.
- STOP record: no `USER.md`, or the claim script refused. The reason goes to the user in one line, and to [memory.md](memory.md).

## References

- What earlier opens taught, read at stop 0: [memory.md](memory.md)
- The claim, atomic and numbered: [scripts/claim_session.py](scripts/claim_session.py)
- The paired close: `.claude/skills/session-end/SKILL.md`
