# Claude personal memory

Claude Code already keeps some memory: the `CLAUDE.md` files you write and the notes it saves on its own for each project. This workspace gives it a memory with a shape you design and can read whole: who you are, where you are going this quarter, how you want it to work, what you corrected last week, what yesterday left open.

It is a small personal brain: a folder of plain markdown files you own, six skills that read and write them, and three hooks that run on their own. Two skills open and close every session; the others bring sources in, answer from your files, turn repeated corrections into rules, and check the whole folder. There is no memory service to pay for and nothing hidden, so you can open and edit every line Claude remembers.

## Start in the Claude Desktop app

1. Download [QUICKSTART.md](QUICKSTART.md): on its page, the **Download raw file** button.
2. Open the Claude Desktop app, click **Code**, and start a session on your Downloads folder, with the **Worktree** button off.
3. Write: `Install my workspace: follow QUICKSTART.md in my Downloads folder.`

Claude checks git and Python, puts the workspace in `~/Documents/claude-workspace` and unhooks it from this repository, so it is yours. Then you open that folder in a new session and write `Good morning Claude, let's set up my workspace.` Claude walks you through eight phases: you, your areas of work, your projects, your goals, your rhythm, your tools and your voice, then a tour of what you now have, where you can bring in your existing projects and folders. Every phase says what it builds and why, asks with options you click, builds the file and shows it to you before moving on.

Prefer the terminal? `git clone https://github.com/pietroacerbis/claude-personal-memory claude-workspace && cd claude-workspace && claude "setup"`

## The daily loop

| When | You say | What happens |
|---|---|---|
| a chat opens | "good morning" | `session-start` claims a block in today's journal and briefs you in eight lines: yesterday's carryover, today's rhythm, the goal the work moves. A hook has already handed Claude your profile and your memory |
| you hand over a source | "ingest this call" | `ingest` keeps the raw in `06-sources/raw/` and updates the pages it changes, after your yes |
| you ask | "what did we decide on pricing?" | `query` answers from your files and names each one |
| you correct Claude | "no, always do X" | the rule lands in the mistakes log of `MEMORY.md` on the spot; a fact about you lands in `USER.md` |
| once a week | "distil" | `distil` merges repeated corrections, writes what worked into your learnings, and keeps your writing voice current |
| once a week | "lint" | `brain-lint` finds broken links, a stale index and sections over their cap, and fixes them on your yes |
| the work ends | "that's it for today" | `session-end` writes what was done, decided and left open, carries it into tomorrow's journal, and shows you every write before it happens |

Several chats can run on the same day: each one claims its own numbered block, so two sessions never write over each other.

## What is inside

```
index.md           every file with its description, rebuilt after every write
log.md             what happened, one line per event
USER.md            who you are and how you want Claude to talk to you
RHYTHM.md          what comes up on which day
CLAUDE.md          the rules every session follows
QUICKSTART.md      the install, in the Claude Desktop app
SETUP.md           the guided onboarding
TOUR.md            its last phase: what you now have, and your existing work brought in
01-workstreams/    the areas you work on every week
02-projects/       work with a start and an end, from _TEMPLATE/
03-learning/       what you are learning
04-memory/         MEMORY.md, decisions/, the day journals, the todos, the archive
05-inbox/          what you captured and have not placed yet
06-sources/        raw material, kept as it came
.claude/skills/    session-start, session-end, ingest, query, distil, brain-lint
.claude/hooks/     the memory at every open, no key ever written into a file
```

`USER.md`, `RHYTHM.md` and `04-memory/MEMORY.md` do not exist until you run `setup`, which writes them from your answers. Three hooks in `.claude/settings.json` run on their own: they hand Claude your memory at every open, refuse a write that carries a key, and rebuild `index.md` after every write.

## Why files

- **You can read your memory.** Every rule Claude follows is a line in `MEMORY.md`, in your words. Wrong rule: delete the line.
- **A correction becomes a rule.** "When I ask for a summary, the answer comes first" sits in a table with the situation it applies to, and every session reads it.
- **Every session has its record.** The journal of each day keeps one block per chat: what it did, what it decided, what it left for tomorrow.
- **Git keeps the history.** You can see what Claude learned last month, and undo it.

## Your rhythm

`RHYTHM.md` is a table of what you do with Claude on which day: plan the day every morning, review the week on Friday, check the projects on the last Friday of the month. Every session reads today's rows and asks whether to run them first. A task that must run on its own at a fixed hour, with no chat open, belongs to a Claude Code routine on claude.ai instead: `RHYTHM.md` holds the work you do together when you open a chat.

## Rewrite CLAUDE.md every six months

`CLAUDE.md` holds the rules every session follows, and `setup` writes a rewrite date into it, six months out. Rules written for an older model can hold back a newer one: [Boris Cherny](https://www.instagram.com/reel/DbXhiv2s5wg/), who created Claude Code, tells developers to delete old instructions regularly, because newer models no longer need many of them. On that date, delete the rules and write them again from what you need now.

## Works with

Claude Code, in any of its apps: the skills read and write this folder. On claude.ai, where Claude has no folder to write into, the files still work as project knowledge, without the open and the close.

## The Skill kit

This repository is one of four:

- [How to build a skill](https://github.com/pietroacerbis/how-to-build-a-skill): the guide, the format, a template, and two skills that create and review skills.
- [Claude Code daily](https://github.com/pietroacerbis/claude-code-daily): the Claude Code tools I use every day, by category, with the install lines.
- Claude personal memory: this one.
- [Claude antislop](https://github.com/pietroacerbis/claude-antislop): keeps the tells of AI writing out of what Claude writes, with a list of 61 patterns, hooks that check every file and reply, and a skill that rewrites a draft until it is clean.

<!-- CTA -->
---

## Want the same memory for your whole team?

At gaja we build two things for go-to-market teams:

- **The knowledge your Claude reads**: your ICP, your deal stages, your objections, your voice, built from your calls, docs, tools and team.
- **The shared skills your team runs**: written on the processes you already follow, deployed to the whole team, all reading the same knowledge.

Get in touch:

- Pietro Acerbis, Co-founder at gaja: pietro@trygaja.com, [LinkedIn](https://www.linkedin.com/in/pietroacerbis-gaja/)
- gaja: [trygaja.com](https://trygaja.com), [LinkedIn](https://www.linkedin.com/company/gaja-brain/)

MIT licence.
