# SETUP, the guided onboarding

**For Claude.** You are here because `USER.md` is missing at the root, or because the user said "setup". You build their workspace with them, one phase at a time, in this one conversation.

## How every phase runs

1. **Where we are.** Open the phase with its line: "Phase 3 of 7, your areas of work".
2. **Explain.** What this piece is, what it is for, and what Claude does with it later, in two to four plain lines, with an example tied to the user's role.
3. **Propose and ask.** Ask with AskUserQuestion: proposed answers are the options, drawn from what the user already told you, your recommendation first and marked "(Recommended)". Two questions at most per call. The user can always type their own.
4. **Build and show.** Write the file right after the answer, show its content in chat, and link it.
5. **Confirm.** Ask with AskUserQuestion: "Does this look right?" Looks right, next phase (Recommended), Change something. Move on only after the answer.

Always:

- **Never invent an answer.** A skipped question leaves a `TODO:` line in the file.
- **Check before you ask.** When a phase's file already exists, show it and ask whether to keep it or redo it.
- **The user's language** from phase 1 for every message. The files are written in the language the user picks.
- **Run every command yourself.** Ask the user only for answers and clicks.

---

## Phase 1 of 7, welcome

**Check.** `git remote get-url origin`. When it points to `pietroacerbis/claude-personal-memory`, this folder is still tied to the kit: run `git remote remove origin`. When `gh auth status` answers, offer later in this phase to create the user's own private copy. When the remote is the user's own and `gh repo view --json visibility` says public, warn: "Your copy on GitHub is public, and this folder will hold your notes. I recommend making it private: Settings, Danger zone, Change visibility."

**Say**, short:

> "Welcome. In seven short phases we build your workspace, one file at a time:
> 1. Welcome
> 2. You: your profile
> 3. Your areas of work
> 4. Your projects
> 5. Your goals and your memory
> 6. Your rhythm
> 7. Your tools and your voice"

**Ask** (one call): "Which language should we use?" English (Recommended), Italiano, Español, Français. With `gh` signed in, a second question: "Keep a private copy of this workspace on your GitHub?" Yes, create it (Recommended), Not now. On yes: `gh repo create {folder-name} --private --source . --push`.

## Phase 2 of 7, you, `USER.md`

**Explain:** "`USER.md` is your profile. Every session reads it before anything else, so Claude knows who you are and how you want to be treated."

**Ask** (AskUserQuestion, two calls):

1. "What should I call you?" (offer the name from `gh api user --jq .name` or `git config user.name`) and "What is your role, and at which company?"
2. "How should I talk to you?" Short and direct, the answer first (Recommended), Step by step with the reasoning, Short by default, detail when I ask. Then, multi-select: "What annoys you in AI answers?" Long introductions, Hedging and caveats, Jargon, Lists for everything, Closing offers like "let me know if".

**Ask in plain chat**, no options: "Which tools do you use every day? Write them in one line, for example: Gmail, Google Calendar, Slack, Notion, HubSpot." Keep the list: phase 7 connects them.

**Build** `USER.md`:

    # USER, {name}

    ## Role
    {role}, {company}

    ## Language
    {language}

    ## How to talk to me
    - {the style picked, as a rule}
    - Never: {each annoyance picked, one line each}

    ## Tools I use
    {the tools, one per line}

    ## How I work
    Filled as we work: what Claude learns about me that stays true.

**Then explain how it grows:** "This file grows in two ways. When you tell me something stable about you, like 'I never take calls on Friday', I write it here in the same turn. When you correct how I work, the rule goes to the mistakes log in your memory, which we build in phase 5. You can also open this file and edit it yourself."

## Phase 3 of 7, your areas of work, `01-workstreams/`

**Explain:** "An area is work that comes back every week and never ends, like sales. Each area gets a folder with the same shape: `01-knowledge` for the rules and facts of that area, `02-artifacts` for what you produce, `03-archive` for what you no longer use. So Claude always knows where to read and where to write."

**Ask** (multi-select, at most four picked): "Which areas do you work on every week?" Propose four from the role, each with one line on what it would hold. For a COO of a startup: Operations (processes, suppliers, internal tools), Hiring (job descriptions, candidates, interview notes), Sales (call notes, account research, outreach drafts), Content (posts, newsletters, event material). More than four picked: ask which four to keep.

**Build**, for each area, `01-workstreams/{area}/` with `README.md` (what the area is for in one line, and its three folders), `01-knowledge/`, `02-artifacts/`, `03-archive/`, each holding an empty `.gitkeep` so git keeps it. Show the tree.

## Phase 4 of 7, your projects, `02-projects/`

**Explain:** "Projects are different from areas: they start and they end. Each one gets a `map.md` with its plan, a `latest.md` that says where it stands, and a `history.md` with its decisions. Claude opens `latest.md` first when you name the project."

**Ask** (multi-select, two or three picked): "Which projects matter most right now?" Propose three from the role and the areas, each with one line. Then, for each project picked, two calls. First: "What does it produce, and what proves it is done?" with two proposals drawn from its name and the role, for example "a playbook the new reps use from their first day"; and "When is it done?" with a date one month out (Recommended), the end of the quarter, a date the user types. Second: "Why now?" with two proposals drawn from the role and the user's own words as the option to type.

**Build** `02-projects/{slug}/` as a copy of `02-projects/_TEMPLATE/`, with the head of `map.md` filled from the answers, `latest.md` saying the project opened today, and the first line of `history.md`.

## Phase 5 of 7, your goals and your memory, `04-memory/MEMORY.md`

**Explain:** "`MEMORY.md` is what Claude reads at every open, after your profile: where you are going this quarter, the steps to get there, and everything you taught it."

**Ask** (multi-select): "What are your goals for this quarter?" Propose three from the role and the areas, each written with its measure, for example "Close 10 new customers". The user can type their own. Then one call per goal: "How do we measure it?" with two proposals and the user's own, and "By when?" with the end of the quarter (Recommended) or a date the user types.

**Propose the roadmap** from the role and the goals: for each month left in the quarter, the step toward each goal, one line each. Ask: "Keep this roadmap?" Keep it (Recommended), Change some steps.

**Build** `04-memory/MEMORY.md`:

    # MEMORY, {name}

    ## Quarter goals
    - {goal}: {measure}, by {YYYY-MM-DD}

    ## Roadmap
    - {YYYY-MM}: {step}

    ## Active work
    - {each project of phase 4, one line, with its link}

    ## Decisions

    ## Mistakes log
    | Rule | When it applies |
    | --- | --- |

    ## Recent learnings

and `04-memory/remaining-todos.md` with the sections `## P0, blocks someone`, `## P1, next`, `## P2, backlog`.

**Then explain how the rest fills**, as this table:

| Section | Fills when |
|---|---|
| Decisions | a session decides something that reaches across projects: `session-end` writes a file in `04-memory/decisions/` and a line here. Say "write this down as a decision" to do it on the spot |
| Mistakes log | the moment you correct me: the rule and when it applies, in the same turn |
| Recent learnings | once a week, `distil` reads the journals and writes what worked and what you repeated |

## Phase 6 of 7, your rhythm, `RHYTHM.md`

**Explain:** "Claude has no alarm clock. Every session reads this file and puts today's rows in front of you, so the routines happen without a scheduler."

**Ask** (multi-select): "What should come up on its own?" Propose three or four rows drawn from the role, the areas and the goals, for example "Every day: plan the day, three priorities", "Friday: review the week against the goals", "Monday: pipeline review" for a Sales area.

**Build** `RHYTHM.md`:

    # RHYTHM

    `Day` takes mon, tue, wed, thu, fri, sat, sun, daily, or fri-last for the last Friday of the month.

    | Day | What | How |
    |---|---|---|
    | {day} | {what} | {the prompt or the skill to run} |

## Phase 7 of 7, your tools and your voice

**Check first, ask nothing yet.** List what this session can already reach: the connectors and MCP servers among your tools, `claude mcp list`, and the command lines on the path (`gh`, `gws`). Compare it with the tools of phase 2.

**Say** which tools are connected and which are missing, in one list. For each missing one, ask: "Connect {tool} now?" Yes, guide me (Recommended), Later. On yes, one step per message, waiting for the user each time:

1. Gmail, Google Calendar, Google Drive, Slack, Notion and the other connectors claude.ai lists: open https://claude.ai/settings/connectors, click Connect next to the tool, sign in and allow. Then type `/mcp` here and check the tool shows as connected.
2. A tool claude.ai does not list: open the tool's own MCP page, which you search for and link, and add it with the line it gives, for example `claude mcp add --transport http {name} {url}`.
3. After each one, prove it works with one read, for example the subject of the newest email. A tool that does not answer stays on the list for later.

**Then the voice**, through `distil`, variant `voice`:

- **Gmail connected**: "I can learn how you write emails from the ones you sent. I read up to 30 of your sent emails from the last 90 days and write down the rules, never the emails." Ask: Yes, learn my email voice (Recommended), Not now. On yes, run the outreach channel.
- **LinkedIn**: "To learn how you write posts, I need your posts. LinkedIn does not let me read your profile, so either paste five or more posts here, or download your data (LinkedIn, Settings, Data privacy, Get a copy of your data, Posts) and drop the file into `06-sources/raw/`." Ask: I'll paste posts, I'll drop the export, Not now. Run the content channel on what arrives.

**Close**, in three lines: write the rewrite date into `CLAUDE.md`, six months from today, and add one line to `log.md`: `{YYYY-MM-DD} | [workspace] workspace set up: {n} areas, {n} projects, {n} goals -> USER.md`. Then say: "Your workspace is ready. Open every chat with 'good morning' and close it with 'that's it for today'. On {rewrite date} we write the rules in `CLAUDE.md` again from scratch, since newer models need fewer of them." List every `TODO:` left by a skipped question, if any.
