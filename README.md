# Claude personal memory

Claude starts every chat from zero. This workspace makes it remember: who you are, how you want it to work, what you corrected last week, what yesterday left open.

It is a folder of plain markdown files you own, and two skills: one reads the files back when a session opens, the other writes them when it closes. There is no memory service to pay for and nothing hidden, so you can open and edit every line Claude remembers.

## Start in three steps

1. Click **Use this template** and create a **private** repository. Your notes and projects will live here.
2. Clone it and open the folder in Claude Code: the terminal, VS Code, JetBrains or the desktop app.
3. Type `setup`.

Claude then walks you through nine short phases, about fifteen minutes. It says what it is about to build, asks with options you click, and builds one file at a time. You end with a profile, a memory, your areas of work, your first project and your weekly rhythm.

## The daily loop

| When | You say | What happens |
|---|---|---|
| a chat opens | "good morning" | `session-start` claims a block in today's journal, reads your profile, your memory, yesterday's carryover and today's rhythm, and briefs you in eight lines |
| you correct Claude | "no, always do X" | the rule lands in the mistakes log of `MEMORY.md` on the spot, and every later session reads it |
| the work ends | "that's it for today" | `session-end` writes what was done, decided and left open, carries it into tomorrow's journal, and shows you every write before it happens |

Several chats can run on the same day: each one claims its own numbered block, so two sessions never write over each other.

## What is inside

```
USER.md            who you are and how you want Claude to talk to you
RHYTHM.md          what comes up on which day
CLAUDE.md          the rules every session follows
SETUP.md           the guided onboarding
01-workstreams/    the areas you work on every week
02-projects/       work with a start and an end, from _TEMPLATE/
03-learning/       what you are learning
04-memory/         MEMORY.md, the day journals, the todos, the archive
05-inbox/          what you captured and have not placed yet
06-sources/        raw material, kept as it came
.claude/skills/    session-start and session-end
```

`USER.md`, `RHYTHM.md` and `04-memory/MEMORY.md` do not exist until you run `setup`, which writes them from your answers.

## Why files

- **You can read your memory.** Every rule Claude follows is a line in `MEMORY.md`, in your words. Wrong rule: delete the line.
- **A correction becomes a rule.** "When I ask for a summary, the answer comes first" sits in a table with the situation it applies to, and every session reads it.
- **Every session has its record.** The journal of each day keeps one block per chat: what it did, what it decided, what it left for tomorrow.
- **Git keeps the history.** You can see what Claude learned last month, and undo it.

## A rhythm instead of routines

Claude has no alarm clock. `RHYTHM.md` is a table of what you run on which day: plan the day every morning, review the week on Friday, check the projects on the last Friday of the month. Every session reads today's rows and asks whether to run them first, so the routine happens because you opened a chat, with no scheduler to set up.

## Rewrite CLAUDE.md every six months

`CLAUDE.md` holds the rules every session follows, and `setup` writes a rewrite date into it, six months out. Rules written for an older model can hold back a newer one: [Boris Cherny](https://www.instagram.com/reel/DbXhiv2s5wg/), who created Claude Code, tells developers to delete old instructions regularly, because newer models no longer need many of them. On that date, delete the rules and write them again from what you need now.

## Works with

Claude Code, in any of its apps: the skills read and write this folder. On claude.ai, where Claude has no folder to write into, the files still work as project knowledge, without the open and the close.

## The Skill kit

This repository is one of three:

- [How to build a skill](https://github.com/pietroacerbis/how-to-build-a-skill): the guide, the format, a template, and two skills that create and review skills.
- [Claude Code daily](https://github.com/pietroacerbis/claude-code-daily): the Claude Code tools I use every day, by category, with the install lines.
- Claude personal memory: this one.

<!-- CTA -->
---

## Want the same memory for your whole team?

This workspace remembers one person. At gaja we build the same thing for a go-to-market team: what your buyers say on calls, what your deals teach, what your best reps do, kept in one brain every rep's Claude reads.

- Pietro Acerbis, pietro@trygaja.com, [LinkedIn](https://www.linkedin.com/in/pietroacerbis-gaja/)
- [trygaja.com](https://trygaja.com)

MIT licence.
