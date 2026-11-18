---
name: query
description: "Answer a question about your own work from the files of this workspace and name the file behind every fact: read index.md, open the pages it points to, search the journals, decisions, log and sources when the pages fall short, and say plainly what the workspace does not hold. Read-only, it writes nothing. Not for: landing a new source in the workspace (ingest), opening a session with the memory loaded (session-start)."
when_to_use: "When the answer should already be in a file here: a decision, a date, a price, where a project stands, where something lives, what a session did. Triggers: 'what did we decide about', 'cosa avevamo deciso su', 'where is', 'dov'è', 'where does X stand', 'a che punto è', 'what did we agree with', 'cosa abbiamo concordato con', 'when did we', 'quando abbiamo', 'what do I know about', 'cosa so di', '/query'."
goal: "Every answer about your own work comes from your files, with the path to check it."
outcome: "chat only: the answer, a link to the file behind each fact, and what the workspace does not hold. No file written"
inputs:
  required: [workspace-root, question]
  recommended: [project-or-area, time-window]
tier: personal
validation: verifiable
status: active
mcps_used: []
feeds_into: []
version: 1
last_updated: 2026-11-18
---

# query

The answer to a question about your own work is in a file of this workspace, or it is not here at all. This skill finds the file, answers from it and names it, so every fact can be checked in one click. It writes nothing, not even a log line: asking changes no file.

The workspace root is the current working directory, where `USER.md` sits: read every file and run every command from there, never from this skill's folder.

## How it works

### Stop 0, memory, the workspace, the question

Read [memory.md](memory.md). Then check `USER.md` with `ls USER.md`. Missing: STOP, say the workspace is not set up yet, and offer to start with "setup", which follows `SETUP.md`.

Restate the question in one line and take two to four search terms from it: a name, a project slug, the topic word, a date.

A question no file here could answer, such as a general fact, a public price or the news: STOP. Say in one line that this workspace does not cover it, and open nothing. When the user wants it answered anyway, the answer says it comes from general knowledge or the web, never from the files.

### Stop 1, the index

Read `index.md`: one line per file, with its description. Pick at most five candidates whose path or description matches the terms. Where each kind of answer lives:

| The question is about | Open first |
|---|---|
| where a project stands, what comes next | `02-projects/{slug}/latest.md` |
| a decision about one project | `02-projects/{slug}/history.md` |
| a decision across projects | `04-memory/decisions/`, and `## Decisions` in `04-memory/MEMORY.md` |
| an area of work | `01-workstreams/{area}/01-knowledge/` |
| how the user wants Claude to work | `USER.md`, `04-memory/MEMORY.md` |
| what a session did, decided or carried | the journals, at stop 2 |

`index.md` leaves out the journals, `log.md`, `06-sources/raw/` and every archive. No `index.md`: say so in one line, list the `.md` files with Glob, and pick from their names.

### Stop 2, open, then search

Open the candidates whole. When they do not answer, search what the index leaves out:

    python3 ${CLAUDE_SKILL_DIR}/scripts/search.py "PATTERN"

PATTERN is one case-insensitive regular expression built from the terms, such as `northwind|pilot start`. The script searches the four places below, prints every match with its date, newest first, and names each place with no match. It writes nothing.

| Place | Holds |
|---|---|
| `04-memory/sessions/` | the day journals: what each session did, decided and carried |
| `04-memory/decisions/` | one file per decision, with its `status` |
| `log.md` | one line per event, newest first |
| `06-sources/` | raw material, kept as it came |

Open the files behind the newest matches, at most five. One more run is allowed when the first found nothing: a wider pattern, or `--all` to search every file of the workspace. A third run is not. Archives stay out; add `--archive` only when the question is about history: "what did we decide before", "how did this change".

**A page is true as of its date.** When the answer is a fact that moves, a date, a price, a status, a decision, run the script once with its key term even when a page already answered, and compare the dates.

### Stop 3, the answer

In chat, in the user's language, the answer in the first line:

- **Every fact carries its file**, as a link whose text is the path from the workspace root, written `[02-projects/website/latest.md](02-projects/website/latest.md)`. A verdict no file states, such as "on track" or "at risk", stays out: that judgment is the user's.
- **A dated fact carries its date**: the date of the line, the journal or the file it came from.
- **Two files disagree: the newer one wins, and both are named**, each with its date, so the user can correct the older one. This skill corrects nothing.
- **A decision with `status: superseded`** enters only when the question is about history, quoted with its date. Otherwise the answer gives the decision that replaced it.
- **What the workspace does not hold is said plainly**, with what was checked. Never fill the gap from general knowledge or the web without saying that is where it comes from.

Close with one `Checked:` line: the files opened and the searches run. A worked example, two files that disagree:

    The print run is on 2026-03-02: the printer asked for one more week on 2026-02-11 ([04-memory/sessions/2026-02/2026-02-11.md](04-memory/sessions/2026-02/2026-02-11.md)). [02-projects/spring-brochure/latest.md](02-projects/spring-brochure/latest.md), as of 2026-02-04, still says 2026-02-23.

    Checked: index.md, 02-projects/spring-brochure/latest.md, search "brochure|print run" in the journals, decisions, log.md and 06-sources.

## Output

- The answer in chat, in the shape of stop 3. No file is written, this skill's memory included.
- A question the workspace cannot answer still gets an answer: what was checked, and that nothing there holds it.
- STOP records, said in chat in one line, with nothing opened after the stop: no `USER.md` (offer "setup"); a question that is not about this workspace (say so, answer nothing from the files).

## References

- What earlier runs taught, read at stop 0: [memory.md](memory.md)
- The bounded search, newest first: [scripts/search.py](scripts/search.py)
- Where each kind of file lives: `CLAUDE.md`, and the `README.md` of each folder
- What writes the journals, the decisions and `latest.md`: `.claude/skills/session-end/SKILL.md`
