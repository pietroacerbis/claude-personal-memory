# distil, variant learning

Opened at stop 0 when the request asks what we learned, or on the weekly review. The mistakes log keeps what went wrong. This variant keeps what went right and came back: the way of working worth repeating on purpose.

## Read

1. `04-memory/MEMORY.md`, whole: `## Recent learnings` is the destination, and `## Mistakes log` is read so a learning never restates a mistakes row.
2. The journals since the last learning run:

        python3 ${CLAUDE_SKILL_DIR}/scripts/journals.py learning

    The script takes the date from `## Last runs` of memory.md, else from the newest date in `## Recent learnings`, else the last 30 days, and prints which one it used. `0 journals`: STOP. A journal it does not list is not read, even when it sits in the same folder.
3. Each journal it lists, whole: every `## Session` block, its `**Done:**`, `**Decisions:**` and `**Carries:**`, and `## Carryover in`.

## What counts as a learning

| Kind | The test | Example |
|---|---|---|
| approved twice | the same way of working, approved in two sessions or more | the draft shown in chat before the file, approved both times |
| a decision that held | a choice made in one session that a later one built on without reopening it | numbers before narrative in the update, sent unchanged |
| a step that saved a correction | something done before the work that a block shows spared a redo | `latest.md` read first, so the settled question stayed settled |

Not a learning: what was done (the journal already holds it), a correction (the mistakes log), a fact about one project (its `latest.md` and `history.md`), a fact about the user (`USER.md`), anything seen once with no outcome.

## The row

One line under `## Recent learnings`, written as a rule a later session can follow, then the journals it comes from, relative to `04-memory/`:

    - Show the draft in chat before writing the file: approved both times. From sessions/2026-11/2026-11-12.md, sessions/2026-11/2026-11-13.md

A date inside the row is written in full, `2026-11-12`, never `11-12`. New rows go at the bottom. A row that already says the same thing gets the new journal added to its sources, never a second row. Past 30 rows, by `caps.py`, the oldest rows at the top move to `04-memory/archive/learnings-YYYY-MM.md`, with one line left under the section: `Older rows: [archive/learnings-YYYY-MM.md](archive/learnings-YYYY-MM.md)`.

## The gate list

One line per row, as it will be written, with the kind it passed as:

    1. Add (approved twice): - Show the draft in chat before writing the file: approved both times. From sessions/2026-11/2026-11-12.md, sessions/2026-11/2026-11-13.md
    2. Add the 2026-11-13 journal to the sources of the row "Ask for the three priorities before planning the day"

## The log line

    YYYY-MM-DD | [memory] 2 recent learnings from 2 journals -> 04-memory/MEMORY.md

## STOP records

- `STOP: no new journal` when `journals.py` prints `0 journals`. Name the date it counted from, and write nothing.
- `STOP: nothing repeated` when the journals hold no learning by the test above. Name the journals read. `## Last runs` stays as it was, so next week's run reads these journals again with the new ones, where a way of working seen once may show up a second time.
