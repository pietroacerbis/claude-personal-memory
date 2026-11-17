# 04-memory

What makes Claude remember. Every session reads `MEMORY.md` and the day's journal at the open, and writes the journal at the close.

| File | Holds | Cap |
|---|---|---|
| `MEMORY.md`, `## Active work` | one line per piece of work in progress | 12 lines |
| `MEMORY.md`, `## Mistakes log` | each correction you gave: the rule, and when it applies | 25 rows |
| `MEMORY.md`, `## Recent learnings` | what a session taught about how you work | 30 lines |
| `remaining-todos.md` | open todos under P0, P1, P2. A closed todo is deleted | none |
| `sessions/YYYY-MM/YYYY-MM-DD.md` | the day's journal: one block per session, and the carryover from the day before | none |
| `archive/` | rows moved out of `MEMORY.md` when a section passes its cap | none |

**Why caps.** `MEMORY.md` is read at every open. A memory that grows without limit costs more to read every day and buries the rows that matter, so past a cap the oldest rows move to `archive/` with a link, and `session-end` says when.

**A correction lands at once.** The moment you correct Claude, the rule goes into the mistakes log, in the same turn, never at the end of the session.
