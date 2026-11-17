---
name: session-end
description: "Close a working session so the next one starts from it: fill this session's block in the journal with what was done, decided and left open, put each decision where it belongs, carry forward what tomorrow needs, and show every write for your approval first. Not for: opening a session (session-start), saving a correction the moment it happens (it goes to MEMORY.md right away), writing a document drafted in chat."
when_to_use: "When a task is finished or the day ends. Triggers: 'that's it for today', 'close the session', 'we're done', 'chiudo qui', 'abbiamo finito', 'basta per oggi', 'a domani', '/session-end'."
goal: "Nothing a session learned is lost when the chat is closed."
outcome: "04-memory/sessions/YYYY-MM/YYYY-MM-DD.md, the block closed, and the next day's carryover"
inputs:
  required: [workspace-root, session-evidence]
  recommended: [touched-project]
tier: personal
validation: verifiable
status: active
mcps_used: []
feeds_into: [session-start]
version: 1
last_updated: 2026-11-17
---

# session-end

One weight for every close, the last of the day included. A close speaks for its own block only: several chats can run on the same day.

The workspace root is the current working directory, where `USER.md` sits: read every file and run every command from there, never from this skill's folder.

## How it works

### Stop 0, memory and the block

Read [memory.md](memory.md). Find this session's block in the journal of **the day the session opened**, by the workstream in its heading. No block, because the chat opened without `session-start`: claim one now with the start skill's script, then go on.

### Stop 1, compile from evidence

Read back what this chat did: files written, decisions taken, what stayed open. Never credit work that left no file or no decision. Three fields:

- `**Done:**` one line per result, with its file. Past five lines, group them under bold headings.
- `**Decisions:**` one line each, with where it was written, or `none`.
- `**Carries:**` what the next session needs, at most five lines, or `none`.

### Stop 2, one home per decision

| The decision is about | It goes to |
|---|---|
| a project | that project's `history.md`, one dated line, and its `latest.md` rewritten |
| how the user wants Claude to work | `04-memory/MEMORY.md`, `## Mistakes log` or `## Recent learnings` |
| anything else | the journal block only |

A correction should already be in `MEMORY.md` from the moment it happened. Here you check that it landed, and write it only when it did not.

### Stop 3, the gate

Show every write as one numbered list, one line each: the block, the decisions with their homes, the memory rows, the todos ticked, the carryover. Then wait for one of:

    approve all · approve 1,3 · skip all · show 2

An approval already given in the request counts. A bare "ok" gets one question back. `skip all` still closes the block, since the block is the record of the session.

### Stop 4, write

1. The block, through the script, never by hand. Write the three fields to a temporary file starting at `**Done:**`, and the carryover lines to another:

        python3 ${CLAUDE_SKILL_DIR}/scripts/close_session.py WORKSTREAM BODY_FILE --day YYYY-MM-DD --carry CARRY_FILE

    `--day` is the day the session opened. `--carry` writes the lines into `## Carryover in` of the next day's journal, where tomorrow's open reads them. Exit 2: report its line and STOP.
2. The decisions, in the homes of stop 2.
3. `04-memory/remaining-todos.md`: tick what this session provably closed. A close never adds a todo.

### Stop 5, report

In chat: the block number, the files written, and the counts of the memory sections against their caps in `04-memory/README.md`. Over a cap: name the rows to move to `04-memory/archive/`, and move nothing without a yes.

## Output

- The block closed in `04-memory/sessions/YYYY-MM/YYYY-MM-DD.md`, in this shape:

        ## Session N, HH:MM, workstream
        **Status:** closed
        **Scope:** one line
        **Opened:** the files read
        **Done:** one line per result, with its file
        **Decisions:** one line each, with its home, or none
        **Carries:** at most five lines, or none

- The carryover in the next day's journal, under `## Carryover in`.
- STOP record: nothing to close (the block records the empty session and why), or the script refused. The reason goes to the user, and to [memory.md](memory.md).

## References

- What earlier closes taught, read at stop 0: [memory.md](memory.md)
- The close and the carryover, refusing every wrong block: [scripts/close_session.py](scripts/close_session.py)
- The paired open and its claim script: `.claude/skills/session-start/SKILL.md`
