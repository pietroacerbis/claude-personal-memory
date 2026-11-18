---
name: distil
description: "Turn what repeats into a rule: merge and sharpen the mistakes log, write what worked into recent learnings, learn how you write from your own emails and posts. Shows every write for your approval first. Not for: checking the workspace for broken links, a stale index or a section over its cap (brain-lint), closing a session (session-end), filing a document, a link or an export you hand over (ingest)."
when_to_use: "Once a week, when a correction comes back, or at the last phase of setup. Triggers: 'distil', 'what did we learn this week', 'clean up the mistakes log', 'learn my voice', 'learn how I write', 'distilla', 'cosa abbiamo imparato questa settimana', 'pulisci il mistakes log', 'impara come scrivo', 'impara la mia voce', '/distil'."
goal: "What happened three times becomes one rule every later session reads, and the memory stays short enough to read."
outcome: "04-memory/MEMORY.md (## Mistakes log or ## Recent learnings) with 04-memory/archive/ past a cap, or 01-workstreams/{area}/01-knowledge/voice.md; one line in log.md"
inputs:
  required: [workspace-root, variant]
  recommended: [voice-material, channel]
tier: personal
validation: verifiable
status: active
mcps_used: ["gmail, optional: any Gmail connector or MCP, or the gws command line"]
feeds_into: [session-start]
version: 1
last_updated: 2026-11-18
---

# distil

A correction given once is an edit. Given three times, it is a rule. This skill reads back what piled up, finds what repeats, and writes it as one line that later sessions read, so the memory gets sharper without getting longer.

The workspace root is the current working directory, where `USER.md` sits: read every file and run every command from there, never from this skill's folder.

## How it works

### Stop 0, memory, the workspace and the variant

Read [memory.md](memory.md). Then check `USER.md` with `ls USER.md`. Missing: STOP, say the workspace is not set up yet, and offer "setup".

Resolve the variant once, from the request, and open its file. It is the only variant file the run reads, and it holds what to read, what to write, the gate list and its own STOP records.

| Variant | The request sounds like | Writes | File |
|---|---|---|---|
| `mistakes` | "clean up the mistakes log", a correction that came back | `## Mistakes log`, `04-memory/archive/` | [variants/mistakes.md](variants/mistakes.md) |
| `learning` | "what did we learn this week", the weekly review | `## Recent learnings` | [variants/learning.md](variants/learning.md) |
| `voice` | "learn my voice", emails or posts handed over, setup's last phase | `01-workstreams/{area}/01-knowledge/voice.md` | [variants/voice.md](variants/voice.md) |

A bare "distil" with no other words: ask once which of the three, with `learning` recommended, and write nothing until the answer.

### Stop 1, read

Read what the variant file names, in its order. Read the destination whole before any candidate: a rule already written is sharpened in place, never written a second time.

### Stop 2, find what repeats

Apply the variant's test. Counting is the scripts' job, judgment is yours: two rows in different words can ask for the same thing, and the same words can hide two different rules. Leave out what does not pass the test, and keep it for the report.

### Stop 3, the gate

Show every write as one numbered list, one line each: what changes, in which file, and the evidence behind it (the journals, the rows, the number of items). The variant gives the shape of its lines. Then wait for one of:

    approve all · approve 1,3 · skip all · show 2

An approval already given in the request counts. A bare "ok" gets one question back. `show 2` prints item 2 in full, as it will be written. `skip all` writes nothing in the workspace.

From here the run counts as done: set this variant's line under `## Last runs` of [memory.md](memory.md) to today, whatever the verdict, so the next run starts after this one.

### Stop 4, write

1. The approved items, in the shape the variant gives, and nothing else.
2. One line in `log.md` per file written, through the script, never by hand:

        python3 ${CLAUDE_SKILL_DIR}/scripts/log_line.py "YYYY-MM-DD | [area] what changed -> path"

    `area` is `memory` for mistakes and learning, the workstream folder name for voice. The script puts the line first under `## Entries` and refuses a line out of shape or a path that does not exist. Exit 2: fix the line and run it again.

### Stop 5, report

In chat, short:

- what was written, with each file as a link
- `python3 ${CLAUDE_SKILL_DIR}/scripts/caps.py`: the two sections against their caps, 25 rows and 30 rows
- what was left out and why: seen once, seen twice, approved at no gate

## Output

- The writes of the variant, in its declared homes, and one line per file in `log.md`.
- The date of the run under `## Last runs` of [memory.md](memory.md).
- STOP record: no `USER.md`, a variant nobody chose, or the variant's own. Nothing in the workspace is written. The reason goes to the user in one line, and to [memory.md](memory.md) under `## STOP records`.

## Scripts

Run from the workspace root. Python 3, standard library only.

| Script | Does |
|---|---|
| `caps.py` | counts `## Mistakes log` and `## Recent learnings` against their caps |
| `journals.py VARIANT` | lists the journals newer than the variant's last run, and says where that date came from |
| `log_line.py "LINE"` | checks the log line's shape and writes it first under `## Entries` |
| `linkedin_posts.py PATH` | prints the newest posts with text from the LinkedIn export's `Shares.csv` |
| `personal_data.py FILE` | flags an email, a phone number, a link or an @handle in a voice file |

## References

- What earlier runs taught, the last run of each variant, read at stop 0: [memory.md](memory.md)
- The three variants: [variants/mistakes.md](variants/mistakes.md), [variants/learning.md](variants/learning.md), [variants/voice.md](variants/voice.md)
- The sections, their caps and who fills them: `04-memory/README.md`
- The journal block these runs read: `.claude/skills/session-end/SKILL.md`, its Output section
