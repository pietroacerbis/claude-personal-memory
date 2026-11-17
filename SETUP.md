# SETUP, the guided onboarding

**For Claude.** You are here because `USER.md` is missing at the root, or because the user said "setup". You build their workspace with them, one piece at a time, in this one conversation. About fifteen minutes.

## How every phase runs

1. **Say what you are about to build, and why, in one or two plain lines.** Then ask.
2. **Ask with AskUserQuestion.** Two questions at most per message. Proposed answers are the options, your recommendation first and marked "(Recommended)". The user can always type their own.
3. **Build right after the answer**, and show the file as a link they can click. Then move to the next phase in the same message.
4. **Never invent an answer.** A skipped question leaves a `TODO` line in the file, and the closing summary lists it.
5. **Check before you ask.** When a phase's file already exists, show it and ask whether to keep it or redo it.
6. **The user's language.** Ask in phase 1, then run everything in it. The files stay in the language the user picks.
7. **Run every command yourself.** Ask the user only for answers and clicks.

---

## Phase 1, welcome

**Check.** `git remote -v`. When the remote is a public GitHub repository (`gh repo view --json visibility`), warn first:

> "Before we start: this workspace will hold your notes, your projects and how you like to work. Your copy on GitHub is public. I recommend making it private: Settings, Danger zone, Change visibility."

**Say:**

> "Welcome. In the next fifteen minutes we build your workspace: a profile Claude reads at every session, a memory that keeps your corrections, a journal per day, your areas of work, your projects and your weekly rhythm. Everything is plain files in this folder, and you own them. I ask, you answer, I build."

**Ask** (one call, two questions):

1. "Which language should we use?" English (Recommended), Italiano, Español, Français.
2. "Ready to start?" Let's go (Recommended), Show me what you will create first.

When they ask to see first, list the files of phases 2 to 7 in one table, then ask again.

## Phase 2, you, `USER.md`

**Say:** "First your profile. Every session reads it before anything else, so this is where you tell Claude how you want to be treated."

**Ask** (two calls):

1. "What should I call you?" and "What is your role, and at which company?" Offer the name from `gh api user --jq .name` or `git config user.name` when one answers.
2. "How should I talk to you?" Short and direct, the answer first (Recommended), Explain the reasoning step by step, Mixed: short by default, detail when I ask. Then, multi-select: "What annoys you in AI answers?" Long introductions, Hedging and caveats, Jargon, Lists for everything, Emojis, Closing offers like "let me know if...".

**Build** `USER.md`:

    # USER, {name}

    ## Role
    {role}, {company}

    ## Language
    {language}

    ## How to talk to me
    - {the style picked, as a rule}
    - Never: {each annoyance picked, one line each}

    ## How I work
    TODO: what I want Claude to know about how I work. It fills in as we go.

## Phase 3, your areas of work, `01-workstreams/`

**Say:** "Now the areas you come back to every week, with no end date. Each one gets a folder with the same shape, so you always know where a file goes."

**Ask:** "Which areas do you work on every week?" Multi-select. Propose four from the role of phase 2, for example for a founder: Sales, Product, Fundraising, Content. The user can add their own.

**Build**, for each area, `01-workstreams/{area}/` with:

- `README.md`: what the area is for, in one line, and its folders.
- `01-knowledge/`: what governs this area: notes, references, the facts Claude needs here.
- `02-artifacts/`: what the area produced.
- `03-archive/`: what retired.

Show the tree.

## Phase 4, your projects, `02-projects/`

**Say:** "Projects are different: they start and they end. Each one has a map with its plan, a `latest.md` that says where it stands, and a `history.md` with its decisions. Let's set up the one that matters most right now."

**Ask:** "What is the project that matters most right now?" free text, then "When is it done?" with a proposed date one month out, and "Why now?" free text. Two calls.

**Build** `02-projects/{slug}/` as a copy of `02-projects/_TEMPLATE/`, with the head of `map.md` filled from the answers, `latest.md` saying the project opened today, and the first line of `history.md`. Then ask whether there is a second project; build it the same way, or move on.

## Phase 5, your memory, `04-memory/`

**Say:** "Now your memory. Every time you correct Claude, the rule goes into this file at once, and every session reads it back."

**Build**, with no question:

`04-memory/MEMORY.md`:

    # MEMORY, {name}

    ## Active work
    - {each project of phase 4, one line, with its link}

    ## Mistakes log
    | Rule | When it applies |
    | --- | --- |

    ## Recent learnings

`04-memory/remaining-todos.md`:

    # Todos

    ## P0, blocks someone
    ## P1, next
    ## P2, backlog

**Say:** "The mistakes log starts empty. The first time you correct me, try it: say 'remember this' and watch the row appear."

## Phase 6, your rhythm, `RHYTHM.md`

**Say:** "Claude has no alarm clock. Instead, every session reads your rhythm and puts today's rows in front of you, so the routines happen without a scheduler."

**Ask:** "What should come up on its own?" Multi-select: Plan the day, every day (Recommended), Plan the week on Monday, Review the week on Friday, Clear the inbox on Wednesday, Review the projects on the last Friday of the month. The user can add their own.

**Build** `RHYTHM.md`:

    # RHYTHM

    `Day` takes mon, tue, wed, thu, fri, sat, sun, daily, or fri-last for the last Friday of the month.

    | Day | What | How |
    |---|---|---|
    | {day} | {what} | {the prompt or the skill to run} |

## Phase 7, the rules, `CLAUDE.md`

**Say:** "Last, the rules every session follows. I'll show you the ones in `CLAUDE.md`; keep them, or tell me what to change."

Show the section titles of `CLAUDE.md` in one list, and ask: "Keep these rules?" Keep them (Recommended), Change some. On a change, edit that rule only, with the user's words.

Then write the rewrite date into `CLAUDE.md`: six months from today. **Say:** "On that date we delete these rules and write them again from scratch. Boris Cherny, who created Claude Code, tells developers to delete old instructions regularly, because newer models no longer need many of them."

## Phase 8, the first session

**Say:** "Your workspace is ready. Now the loop you will use every day."

Run `session-start` with the workstream `onboarding`. Its brief is the proof that the memory is read back.

**Say:**

> "That's the loop. Open every chat with 'good morning' and Claude reads your memory. Close it with 'that's it for today' and Claude writes what happened and what tomorrow needs. When I get something wrong, correct me: the rule lands in your memory on the spot."

## Phase 9, done

List every file built, as links, and every `TODO` left by a skipped question. Then close the onboarding session with `session-end`.
