# SETUP, the guided onboarding

**For Claude.** You are here because `USER.md` is missing at the root, or because the user said "setup". You build their workspace with them, one phase at a time, in this one conversation.

## How every phase runs

1. **Where we are.** Open the phase with its line: "Phase 3 of 8, your areas of work".
2. **Explain.** What this piece is, what it is for, and what Claude does with it later, in two to four plain lines, with an example tied to the user's role.
3. **Propose and ask.** Ask with AskUserQuestion: proposed answers are the options, drawn from what the user already told you in this setup, your recommendation first and marked "(Recommended)". Two questions at most per call. The user can always type their own.
4. **Build and show.** Write the file right after the answer. Then show a snapshot in chat, three to eight lines (the key lines of the file, or the tree with one line per folder), and the file as a link the user can open beside the chat.
5. **Confirm.** Ask with AskUserQuestion: "Does this look right?", naming what the snapshot shows. Looks right, next phase (Recommended), Change something. Never ask about a file you did not show. Move on only after the answer.

Always:

- **Never invent an answer, and never guess one.** A proposal comes from what the user said in this setup or from the tool that answers, named in the option: "from your GitHub profile". A skipped question leaves a `TODO:` line in the file.
- **List, never read.** Reading the user's email, calendar, chat or profile waits for their yes in this setup.
- **Check before you ask.** When a phase's file already exists, show it and ask whether to keep it or redo it.
- **The user's language** from phase 1 for every message. The files are written in the language the user picks.
- **Run every command yourself.** Ask the user only for answers and clicks.

---

## Phase 1 of 8, welcome

**Check, silently.** `git remote get-url origin`. When it points to `pietroacerbis/claude-personal-memory`, this folder is still tied to the kit: run `git remote remove origin`.

**Say**, short:

> "Welcome. In eight short phases we build your workspace, one file at a time:
> 1. Welcome
> 2. You: your profile
> 3. Your areas of work
> 4. Your projects
> 5. Your goals and your memory
> 6. Your rhythm
> 7. Your tools and your voice
> 8. What is installed, and your existing work"

**Ask** (one call): "Which language should we use?" English (Recommended), Italiano, Español, Français.

## Phase 2 of 8, you, `USER.md`

**Explain:** "`USER.md` is your profile. Every session reads it before anything else, so Claude knows who you are and how you want to be treated."

**Ask in plain chat**, no options, one message: "What should I call you, and what is your role, at which company?" When `gh auth status` answers, add: "Your GitHub profile says {gh api user --jq .name}: is that the name to use?" Without GitHub, ask with no proposal. Never propose a name from `git config`: it is often a username.

**Ask** (one call): "How should we build your profile?"

- Start from the preset (Recommended): "Rules tested over months of daily work on how Claude answers you, how it reads your requests and how it works with you. You can change or delete any line."
- Build mine from scratch: "Two questions now, and the rest fills as we work."

On the preset: copy `.claude/templates/USER-preset.md`, fill name, role, company and language. On from scratch: ask "How should I talk to you?" Short and direct, the answer first (Recommended), Step by step with the reasoning, Short by default, detail when I ask. Then, multi-select: "What annoys you in AI answers?" Long introductions, Hedging and caveats, Jargon, Lists for everything, Closing offers like "let me know if". Build `USER.md` with the sections Role, Language, How to talk to me, Tools I use, How I work.

**Ask in plain chat**, no options: "Which tools do you use every day? Write them in one line, for example: Gmail, Google Calendar, Slack, Notion, HubSpot." Write them under `## Tools I use`: phase 7 connects them.

**Show** the snapshot and the link, then **explain how it grows**, before the confirmation: "This file grows in two ways, whichever start you picked. When you tell me something stable about you, like 'I never take calls on Friday', I write it here in the same turn. When you correct how I work, the rule goes to the mistakes log in your memory, which we build in phase 5. You can also open the file and edit any line yourself."

## Phase 3 of 8, your areas of work, `01-workstreams/`

**Explain:** "An area is work that comes back every week and never ends, like sales. Each area gets a folder with the same shape: `01-knowledge` for the rules and facts of that area, `02-artifacts` for what you produce, `03-archive` for what you no longer use. So Claude always knows where to read and where to write."

**Ask** (multi-select, at most four picked): "Which areas do you work on every week?" Propose four from the role and the tools of phase 2, each with one line on what it would hold. For a founder: Sales (call notes, account research, outreach drafts), Product (specs, roadmap, user feedback), Fundraising (investor notes, pitch material, updates), Content (posts, newsletters, events). More than four picked: ask which four to keep.

**Build**, for each area, `01-workstreams/{area}/` with `README.md` (what the area is for in one line, and its three folders), `01-knowledge/`, `02-artifacts/`, `03-archive/`, each holding an empty `.gitkeep` so git keeps it. **Show** the tree with each area's one line, and the link to each `README.md`.

## Phase 4 of 8, your projects, `02-projects/`

**Explain:** "Projects are different from areas: they start and they end. Each one gets a `map.md` with its plan, a `latest.md` that says where it stands, and a `history.md` with its decisions. Claude opens `latest.md` first when you name the project."

**Ask** (multi-select, two or three picked): "Which projects matter most right now?" Propose three from the role and the areas, each with one line. Then, for each project picked, two calls. First: "What does it produce, and what proves it is done?" with two proposals drawn from its name and the role, for example "a playbook the new reps use from their first day"; and "When is it done?" with a date one month out (Recommended), the end of the quarter, a date the user types. Second: "Why now?" with two proposals drawn from the role and the user's own words as the option to type.

**Build** `02-projects/{slug}/` as a copy of `02-projects/_TEMPLATE/`, with the head of `map.md` filled from the answers, `latest.md` saying the project opened today, and the first line of `history.md`. **Show**, for each project, its four head lines (what it produces, why now, done when, owner) and the link to its `map.md`.

## Phase 5 of 8, your goals and your memory, `04-memory/MEMORY.md`

**Explain:** "`MEMORY.md` is what Claude reads at every open, after your profile: where you are going this quarter, the steps to get there, and everything you taught it."

**Ask** (multi-select): "What are your goals for this quarter?" Propose three from the role and the areas, each written with its measure, for example "Close 10 new customers". The user can type their own.

**Challenge each goal the way a good manager would.** A goal with no number gets the question "how much?". A number gets its consequence worked out and proposed as the measure: a quota of 50k, at the usual three times coverage, needs about 150k of pipeline by the end of the quarter. One call per goal: "How do we measure it?" with that worked measure (Recommended), a second proposal, and the user's own; and "By when?" with the end of the quarter (Recommended) or a date the user types.

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

and `04-memory/remaining-todos.md` with the sections `## P0, blocks someone`, `## P1, next`, `## P2, backlog`. **Show** the goals and the roadmap, and the link.

**Then explain how the rest fills**, as this table:

| Section | Fills when |
|---|---|
| Decisions | a session decides something that reaches across projects: `session-end` writes a file in `04-memory/decisions/` and a line here. Say "write this down as a decision" to do it on the spot |
| Mistakes log | the moment you correct me: the rule and when it applies, in the same turn |
| Recent learnings | once a week, `distil` reads the journals and writes what worked and what you repeated |

## Phase 6 of 8, your rhythm, `RHYTHM.md`

**Explain:** "This file lists what you do with me on which day. Every session reads it and puts today's rows in front of you, and you decide at the open whether to run them first. A task that must run on its own at a fixed hour, with no chat open, is a Claude Code routine on claude.ai instead."

**Ask** (multi-select): "What should come up on its own?" Propose three or four rows drawn from the role, the areas and the goals, for example "Every day: plan the day, three priorities", "Friday: review the week against the goals", "Monday: pipeline review" for a Sales area.

**Build** `RHYTHM.md`:

    # RHYTHM

    `Day` takes mon, tue, wed, thu, fri, sat, sun, daily, or fri-last for the last Friday of the month.

    | Day | What | How |
    |---|---|---|
    | {day} | {what} | {the prompt or the skill to run} |

**Show** the rows and the link.

## Phase 7 of 8, your tools and your voice

**Check by listing, never by reading.** Name what this session can reach from its own tool list, `claude mcp list`, and the command lines on the path (`gh`, `gws`). Do not call a tool to check it. Compare the list with the tools of phase 2.

**Say** which tools are connected and which are missing, in one list. For each missing one, ask: "Connect {tool} now?" Yes, guide me (Recommended), Later. On yes, one step per message, waiting for the user each time:

1. Gmail, Google Calendar, Google Drive, Slack, Notion, Exa and the other connectors claude.ai lists: open https://claude.ai/settings/connectors, click Connect next to the tool, sign in and allow. A connector added now loads in a new session on this folder: say so, and offer to finish this phase there with "continue setup".
2. A tool claude.ai does not list: open the tool's own MCP page, which you search for and link, and add it with the line it gives, for example `claude mcp add --transport http {name} {url}`.

**Then the voice**, through `distil`, variant `voice`:

- **Gmail connected**: "I can learn how you write emails from the ones you sent. I read up to 30 of your sent emails from the last 90 days and write down the rules, never the emails." Ask: Yes, learn my email voice (Recommended), Not now. On yes, run the outreach channel.
- **LinkedIn**: "To learn how you write posts, I need your posts. LinkedIn does not let me open your profile." Ask:
  - Connect Exa and find my public posts (Recommended): "Exa is a web search with a free plan. It finds the posts search engines index, often most of them." Guide it as step 1 above, Exa in the connector list, or add its free server with `claude mcp add --transport http exa https://mcp.exa.ai/mcp`, which works without an account at lower limits. Then ask for the profile link.
  - I'll paste five or more posts here.
  - I'll drop the LinkedIn export: LinkedIn, Settings, Data privacy, Get a copy of your data, Posts, then the file into `06-sources/raw/`.
  - Not now.

  Run the content channel on what arrives.

## Phase 8 of 8, what is installed, and your existing work

**Show** what came with the workspace, as this table:

| Skill | You say | It does |
|---|---|---|
| `session-start` | "good morning" | reads your memory back and briefs you |
| `session-end` | "that's it for today" | writes what was done and decided, carries tomorrow |
| `ingest` | "ingest this" | keeps a source in `06-sources/raw/` and updates the pages it changes |
| `query` | "what did we decide on...?" | answers from your files, naming each one |
| `distil` | "distil" | turns repeated corrections into rules, writes what worked, keeps your voice current |
| `brain-lint` | "lint" | finds broken links, a stale index, sections over their cap |

Then one line on the hooks: "Three hooks run on their own: they hand me your memory at every open, refuse a write that carries a key, and rebuild `index.md` after every write."

**Ask** (multi-select): "Bring your existing work in now?" Projects from claude.ai, Folders on this computer, Later. One step per message, waiting for the user each time:

- **Projects from claude.ai.** For each project: "Open the project on claude.ai, start a new chat inside it, paste the prompt below, and paste its whole answer back here." The prompt:

      Summarise this project for my workspace, using only what this project's files and chats say. Use these headings: What it produces. Why now. Done when. Owner. Where it stands: last point, next step, blockers. Decisions so far, one dated line each. Open questions. Write "unknown" where the project does not say.

  Run `ingest` on each answer: the raw in `06-sources/raw/`, then `02-projects/{slug}/` built from it, after the user's yes. For the chats themselves, the export is on claude.ai, Settings, Privacy, Export data: it holds the conversations, not the files uploaded to them; the zip goes into `06-sources/raw/`.
- **Folders on this computer.** Ask for the folder: its path, or the folder dragged into the chat. List what it holds, then propose a home for each part: a project, an area's `01-knowledge/`, or `06-sources/raw/` only. Copy, never move: the originals stay where they are. Run `ingest` one part at a time, each after the user's yes.

**Close.** Write the rewrite date into `CLAUDE.md`, six months from today, and add one line to `log.md`: `{YYYY-MM-DD} | [workspace] workspace set up: {n} areas, {n} projects, {n} goals -> USER.md`. When `gh auth status` answers, ask: "Keep a private copy of this workspace on your GitHub? It is your backup, and it keeps the history of what I learned." Yes, create it (Recommended), Not now. On yes: `gh repo create {folder-name} --private --source . --push`. Without GitHub, ask nothing. Then say: "Your workspace is ready. Open every chat with 'good morning' and close it with 'that's it for today'. On {rewrite date} we write the rules in `CLAUDE.md` again from scratch, since newer models need fewer of them." List every `TODO:` left by a skipped question, if any.
