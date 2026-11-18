# How we work in this workspace

Claude reads this file at the start of every session. It holds the rules that stay true whatever we are working on. Everything about me is in `USER.md`, everything we learned together is in `04-memory/MEMORY.md`.

**This file is rewritten from scratch on: {six months after setup, YYYY-MM-DD}.** Rules written for an older model can hold a newer one back. When that date has passed, tell me at the open.

## The workspace

| Home | What lives there |
|---|---|
| `index.md` | every file with its description, rebuilt after every write. Read first |
| `log.md` | what happened, one line per event, newest first |
| `USER.md` | who I am and how I want you to talk to me. Read first |
| `RHYTHM.md` | what I run on which day, read at every open |
| `01-workstreams/` | the areas of work I come back to every week, one folder each, with no end date |
| `02-projects/` | work with a start and an end, one folder each, from `_TEMPLATE/` |
| `03-learning/` | what I am learning: notes on what I read, lessons that are not about you |
| `04-memory/` | `MEMORY.md`, the day journals in `sessions/`, `decisions/`, `remaining-todos.md`, `archive/` |
| `05-inbox/` | what I captured and have not placed yet |
| `06-sources/` | raw material, kept as it came: `raw/` and `research/` |

## Before acting

0. **No `USER.md` at the root means the workspace is not set up.** Whatever my first message says, open `SETUP.md` and follow it.
1. **Read `index.md` first.** It lists every file with its description: open only what the task needs, never search blind.
2. **Open with `session-start`, close with `session-end`.** The open reads the memory back, the close writes it.
3. **Inside a folder, open its `README.md` first.** It says what the folder holds and how a file in it is written.
4. **A project starts at its `latest.md`.** It says where the work stands and what comes next.
5. **A file named in a request is read whole before you answer about it.**

## Skills and hooks

| Skill | When |
|---|---|
| `session-start` | a chat opens |
| `session-end` | the work ends |
| `ingest` | I hand you a source: a document, a link, a transcript, an export |
| `query` | a question this workspace can answer |
| `distil` | once a week, or when a correction comes back: mistakes, learnings, my voice |
| `brain-lint` | once a week, or after a big change: broken links, a stale index, a section over its cap |

Three hooks in `.claude/settings.json` run without being asked: the memory is handed to you at every open, a write carrying a key is refused, and `index.md` is rebuilt after every write.

## Rules

1. **One home per fact.** A fact is written once. Every other mention points at that file.
2. **Every output has a home.** No work starts without the path its result lands in.
3. **Stopping is a result.** When something is missing or unclear, stop, say what, and write nothing. A guess is worse than a question.
4. **One live version.** When something changes, the old version moves to an `archive/` folder and only the new one stays live.
5. **One line in `log.md` per event**: a source ingested, a decision, a project opened or closed, a voice updated. `YYYY-MM-DD | [area] what changed -> path`, newest first, never rewritten.
6. **A decision has one home.** About a project: that project's `history.md`. Across projects, or about where I am going: a file in `04-memory/decisions/`, and a line in the `## Decisions` of `MEMORY.md`.

## Working standards

1. **Plan first.** A task with three or more steps gets its plan in chat before the first file is written. When the work goes sideways, stop and plan again.
2. **A correction lands at once.** When I correct you, write the rule and what triggers it into the mistakes log of `04-memory/MEMORY.md` in the same turn, never at the end of the session. Sharpen an existing row before adding a new one. When I tell you something stable about me, my role, a tool I use, how I like to work, it goes into `USER.md` in the same turn.
3. **Verify before you say done.** Name the check that proved it. When a check did not run, say so. "It should work" is not a result.
4. **Chat first, file second.** Show me the content in chat, take my reaction, then write the file.
5. **Facts are yours to report, choices are mine.** Lay out the options, say which one you would pick and why, then wait for me.
6. **Short by default.** `MEMORY.md`, the inbox and the journals are read all the time: one or two lines per entry, the detail in an archive file with a link.
7. **A small yes is done at once.** When I confirm a small, specific change, do it in the same turn and report it.

## Principles

1. **Open only what the task needs**: this file, then the folder's `README.md`, then the page.
2. **Think before acting.** When a simpler path exists, say so. When a request has two readings, name both and ask once.
3. **The smallest change that does what I asked.** No page, section or abstraction I did not ask for.
4. **Touch only what the request needs**, and match the style of the file you edit.

## Formatting

- Absolute dates, `YYYY-MM-DD`, never "today" or "next week" inside a file.
- Files and folders in kebab-case. A date in the name only for files that pile up, like journals, never for files that get edited.
