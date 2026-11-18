# 04-memory

What makes Claude remember. Every session reads `MEMORY.md` and the day's journal at the open, and writes the journal at the close.

| File | Holds | Cap |
|---|---|---|
| `MEMORY.md`, `## Quarter goals` | the goals of this quarter, each with its measure and its date | 5 lines |
| `MEMORY.md`, `## Roadmap` | the steps toward those goals, month by month | 12 lines |
| `MEMORY.md`, `## Active work` | one line per piece of work in progress | 12 lines |
| `MEMORY.md`, `## Decisions` | the ten newest decisions, each a link to its file in `decisions/` | 10 lines |
| `MEMORY.md`, `## Mistakes log` | each correction you gave: the rule, and when it applies | 25 rows |
| `MEMORY.md`, `## Recent learnings` | what worked, what a session taught about how you work | 30 lines |
| `decisions/` | one file per decision across projects, [decisions/README.md](decisions/README.md) | none |
| `remaining-todos.md` | open todos under P0, P1, P2. A closed todo is deleted | none |
| `sessions/YYYY-MM/YYYY-MM-DD.md` | the day's journal: one block per session, and the carryover from the day before | none |
| `archive/` | rows moved out of `MEMORY.md` when a section passes its cap | none |

**Why caps.** `MEMORY.md` is read at every open. A memory that grows without limit costs more to read every day and buries the rows that matter, so past a cap the oldest rows move to `archive/` with a link, and `session-end` or `brain-lint` says when.

## How each section fills

| Section | Written when | By |
|---|---|---|
| Quarter goals, Roadmap | at setup, then at the start of each quarter | you, with Claude |
| Active work | a project opens or closes | `session-end` |
| Decisions | a session decides something that reaches across projects | `session-end`, or on the spot when you say "write this down as a decision" |
| Mistakes log | the moment you correct Claude, in the same turn | Claude, on your words |
| Recent learnings | once a week, from the journals: what worked and what you repeated | `distil`, variant `learning` |

When the same correction comes back, `distil`, variant `mistakes`, sharpens the row instead of adding a second one.
