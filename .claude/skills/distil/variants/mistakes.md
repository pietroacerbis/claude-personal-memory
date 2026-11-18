# distil, variant mistakes

Opened at stop 0 when the request is about the mistakes log. Each row lands in the moment, one correction at a time, so the log drifts: two rows that ask for the same thing in other words, a correction that came back in a situation its row does not name, more rows than a session reads with care. This variant puts it back to one row per rule.

## Read

1. `## Mistakes log` of `04-memory/MEMORY.md`, whole. The table is `| Rule | When it applies |`, newest rows at the bottom.
2. The journals since the last mistakes run:

        python3 ${CLAUDE_SKILL_DIR}/scripts/journals.py mistakes

    In each block, look for a correction given again: a `**Decisions:**` line that points at the mistakes log, a `**Done:**` line that says something was redone because of the user's correction.
3. `python3 ${CLAUDE_SKILL_DIR}/scripts/caps.py`, for the row count against 25.

## The three moves

| Move | When | What it writes |
|---|---|---|
| merge | two rows ask for the same behaviour, in different words | one row: the sharper of the two rules, and both triggers in `When it applies`. The other row goes |
| sharpen | a journal shows a row's correction came back in a situation the row does not name | that row's `When it applies` gains the new situation. Never a second row |
| archive | the table holds more than 25 rows once the merges are counted | the oldest rows, at the top of the table, move to `04-memory/archive/mistakes-YYYY-MM.md` until 25 remain |

**Two rows are the same** when following one of them would always satisfy the other. Same topic, different behaviour asked, is two rows: "short replies" and "no emojis" both concern replies and stay apart.

**The user's words stay.** A merge keeps the wording of the sharper row and adds the other row's trigger; it never rewrites a rule in new words. A sharpen adds a few words to `When it applies` and leaves the rule alone. No move adds a rule that no correction gave.

## The gate list

Each line quotes the rows as they stand and the row as it will read:

    1. Merge rows 1 and 3 into: | The answer first, then the reasons | every reply, summaries and status updates included |
    2. Sharpen row 2, from the 2026-11-14 journal: | Never send an email without showing me the draft | any email or DM, and LinkedIn messages |
    3. Archive the 2 oldest rows, 1 and 2, to 04-memory/archive/mistakes-2026-11.md

## The archive file

`04-memory/archive/mistakes-YYYY-MM.md`, the month of the run. Created when missing, rows appended at the bottom when it exists:

    # Mistakes log, archive YYYY-MM

    Rows moved out of 04-memory/MEMORY.md when the log passed 25 rows, oldest first.

    | Rule | When it applies |
    | --- | --- |

In `MEMORY.md`, one line under the table per archive file, written once and never counted as a row:

    Older rows: [archive/mistakes-YYYY-MM.md](archive/mistakes-YYYY-MM.md)

## The log line

    YYYY-MM-DD | [memory] mistakes log: 1 merge, 1 sharpen -> 04-memory/MEMORY.md

An archive move adds a second line, `-> 04-memory/archive/mistakes-YYYY-MM.md`.

## STOP records

- `STOP: no mistakes log` when `04-memory/MEMORY.md` or its `## Mistakes log` is missing. Say so, and point to setup.
- `STOP: nothing to tidy` when no two rows say the same thing, no correction came back, and the log is within 25 rows. Give the row count, and write nothing.
