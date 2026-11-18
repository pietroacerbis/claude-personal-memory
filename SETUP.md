# SETUP, the guided onboarding

**For Claude.** You are here because `USER.md` is missing at the root, or because the user said "setup". You build their workspace with them in this one conversation: seven phases here, then the tour of [TOUR.md](TOUR.md) as phase 8.

## How every phase runs

1. **Say the quoted lines as written**, without the quote marks, in the user's language, filling only the `{braces}`. A phase's first message opens with its first quoted line, before any lookup result or question. Add nothing technical around them: no command, no command output, unless something failed. One phase per message, unless the phase says to go straight on.
2. **Narrate before you act.** Before a read or a search, say in one plain line what you are about to do and why: "Now I'm reading your GitHub profile, to fill in your name."
3. **Choices are clicks.** A question with proposed answers is asked with AskUserQuestion: the proposals are the options, your recommendation first and marked "(Recommended)", two questions at most per call. The user can always type their own.
4. **Use what you have, ask what you lack.** Whatever this session can already read about the user fills the proposals: their GitHub profile, a connected Slack, Google or other tool, what they said earlier in this setup. Each proposal names its source: "from your Slack profile". What no source says is asked in plain chat, with no proposal. Never guess.
5. **Write, show, then ask.** Write the file first: in this setup the snapshot after the write is the review, so a file is never shown twice, whatever `USER.md` says about showing text before writing. After a write, the next message shows what you wrote: a snapshot of three to eight lines, every file written as a markdown link the user can click, such as `[USER.md](USER.md)`, and the quoted lines the phase gives. Only after that message comes the AskUserQuestion "Does this look right?", naming the file, with Looks right, next phase (Recommended) and Change something.
6. **You ask, you write.** The user never opens a file to type in it. A gap becomes your question, and you write the answer. No message ends by sending the user to edit a file.
7. **A line to paste goes alone in a fenced code block**, so the app shows its copy button.
8. **Check before you ask.** When a phase's file already exists, show it and ask whether to keep it or redo it.
9. **Run every command yourself.** Ask the user only for answers, clicks and sign-ins.
10. **A refusal costs one line.** When a tool or a command is refused, or the user declines a permission, say in one line what waits on it, mark it for the close, and go on with the phase. Never troubleshoot permissions or settings with the user during the setup.

---

## Phase 1 of 8, welcome

**Check, silently.** `git remote get-url origin`. When it points to `pietroacerbis/claude-personal-memory`, the folder is still tied to the kit: run `git remote remove origin`.

**Say:**

> "Welcome! In eight short phases we build your workspace together, one file at a time. You answer and click, I write.
>
> 1. Welcome
> 2. You: your profile
> 3. Your areas of work
> 4. Your projects
> 5. Your goals and your memory
> 6. Your rhythm
> 7. Your tools and your voice
> 8. A tour of what you now have"

**Ask** (one call): "Which language should we use?" English (Recommended), Italiano, Español, Français. Every line from here on is in that language.

## Phase 2 of 8, you, `USER.md`

**Say:**

> "Phase 2 of 8, you. First your profile, USER.md. Every session reads it before anything else, so I know who you are and how you want me to work with you."

**Look up**, narrating it: the GitHub profile when `gh auth status` answers (`gh api user`: name, company), the user's own profile on a connected Slack (name, title) or Google account. Never `git config`: it often holds a username.

**Ask** (one call), from what the lookup found, each option naming its source: "What should I call you?" and "What is your role, and at which company?". A question no source answers goes in plain chat, with no proposal.

**Ask** (one call): "How should we build your profile?"

- Start from the preset (Recommended): "Rules tested over months of daily work on how I answer you, how I read your requests and how I work with you. You can change or delete any line."
- Build mine from scratch: "Two questions now, and the rest fills as we work."

On the preset: copy `.claude/templates/USER-preset.md` and fill name, role, company and language. From scratch: ask "How should I talk to you?" Short and direct, the answer first (Recommended), Step by step with the reasoning, Short by default, detail when I ask; then, multi-select, "What annoys you in AI answers?" Long introductions, Hedging and caveats, Jargon, Lists for everything, Closing offers like "let me know if". Build `USER.md` with the sections Role, Language, How to talk to me, Tools I use, How I work.

**Ask** "Which tools do you use every day?" When this session already reaches some, ask with AskUserQuestion, multi-select, the connected ones as options marked "connected", and the user types the rest. With none connected, ask in plain chat: "Write them in one line, for example: Gmail, Google Calendar, Slack, Notion, HubSpot." Write them under `## Tools I use`.

**Show** the snapshot with the link, then say:

> "This is [USER.md](USER.md). It grows in two ways, whichever start you picked. When you tell me something stable about you, like 'I never take calls on Friday', I write it here in the same turn. When you correct how I work, the rule goes to your mistakes log, which we build in phase 5. You never have to edit it yourself, though you always can."

## Phase 3 of 8, your areas of work, `01-workstreams/`

**Say:**

> "Phase 3 of 8, your areas of work. An area is work that comes back every week and never ends, like sales or hiring. Each one gets a folder with the same shape: 01-knowledge for what I should know there, 02-artifacts for what we produce, 03-archive for what you no longer use. So I always know where to read and where to write."

**Ask** (multi-select, at most four picked): "Which areas do you work on every week?" Propose four from the role and the tools, each with one line on what it would hold. For a founder: Sales (call notes, account research, outreach drafts), Product (specs, roadmap, user feedback), Fundraising (investor notes, pitch material, updates), Content (posts, newsletters, events). More than four picked: ask which four to keep.

**Then, for each area picked, one call with two questions**, each with two proposals drawn from the role, the tools and the earlier answers, and the user's own:

1. "What does {area} cover for you?" For Sales, for example: "Founder-led sales to mid-market SaaS teams".
2. "What should I always know when we work on {area}?" For Sales, for example: "Who we sell to and at what price", "The deal stages and who decides".

**Build**, for each area, `01-workstreams/{area}/` with `README.md` (what the area covers, in one line from answer 1, and its three folders), `02-artifacts/` and `03-archive/` holding an empty `.gitkeep` each, and `01-knowledge/context.md`:

    ---
    description: what Claude should know when we work on {area}
    ---

    # {Area}, context

    ## What it covers
    {answer 1}

    ## What Claude should always know
    - {answer 2, one line per point}

    ## Still to learn
    - {two or three questions this area will need answered, drawn from the answers: for Sales, "the deal stages", "the objections we hear most"}

**Show** the tree with one line per area and the link to each `context.md`, then say:

> "These files start from your two answers. They grow every time you hand me a source with ingest: a call transcript, a document, a link. The 'Still to learn' lines are what I'll ask you about as we work. In the tour at the end I'll show you how to bring in the projects and folders you already have: nothing to do now."

## Phase 4 of 8, your projects, `02-projects/`

**Say:**

> "Phase 4 of 8, your projects. A project is different from an area: it starts, it ends, and it has a result that proves it is done, like 'the first sales hire signed by March'. Each project gets three files: map.md with what it produces, why now and when it is done; latest.md with where it stands and the next step; history.md with every decision, newest first."

**Ask** (multi-select, two or three picked): "Which projects matter most right now?" Propose three from the role and the areas, each with one line. Then, for each project picked, two calls. First: "What does it produce, and what proves it is done?" with two proposals drawn from its name and the role; and "When is it done?" with a date one month out (Recommended), the end of the quarter, a date the user types. Second: "Why now?" with two proposals drawn from the role and the user's own words as the option to type.

**Build** `02-projects/{slug}/` as a copy of `02-projects/_TEMPLATE/`, with the head of `map.md` filled from the answers, `latest.md` saying the project opened today and what the first step is, and the first line of `history.md`.

**Show**, for each project, its four head lines (what it produces, why now, done when, owner) and its three files as links, then say:

> "When you name a project, I open its latest.md first. At the end of every session I rewrite latest.md and add the decisions to history.md, after your yes: you never write in them yourself. A project you already run, in claude.ai or in a folder on this computer, comes in during the tour."

## Phase 5 of 8, your goals and your memory, `04-memory/MEMORY.md`

**Say:**

> "Phase 5 of 8, your goals and your memory. MEMORY.md is what I read at every open, right after your profile: where you are going this quarter, the steps to get there, and everything you teach me. Let's start from your goals."

**Ask** (multi-select): "What are your goals for this quarter?" Propose three from the role, the areas and the projects, each written with its measure, for example "Close 10 new customers". The user can type their own.

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

and `04-memory/remaining-todos.md` with the sections `## P0, blocks someone`, `## P1, next`, `## P2, backlog`.

**Show** the goals and the roadmap with the link, then say:

> "This is [MEMORY.md](04-memory/MEMORY.md). The goals and the roadmap are yours: I read them at every open, and when a session moves a goal, the brief says so. The other sections fill as we work, never by your hand:
>
> - Decisions: when a session decides something that reaches across projects, I write it in 04-memory/decisions/ and add a line here. Say 'write this down as a decision' to do it on the spot.
> - Mistakes log: the moment you correct me, the rule and when it applies land here, in the same turn.
> - Recent learnings: once a week, distil reads the journals and writes what worked and what you repeated.
>
> Over time I'll propose improvements: when the same correction comes back, distil sharpens the rule instead of adding a second one, and you approve every change. At the start of next quarter we set the new goals together."

## Phase 6 of 8, your rhythm, `RHYTHM.md`

**Say:**

> "Phase 6 of 8, your rhythm. RHYTHM.md lists what you do with me on which day. Every session reads it and puts today's rows in front of you, and you decide at the open whether to run them first. A task that must run on its own at a fixed hour, with no chat open, is a Claude Code routine on claude.ai instead."

**Ask** (multi-select): "What should come up on its own?" Propose three or four rows drawn from the role, the areas and the goals, among them "Friday: distil and lint, so the workspace keeps itself clean", for example "Every day: plan the day, three priorities" or "Monday: pipeline review" for a Sales area.

**Build** `RHYTHM.md`:

    # RHYTHM

    `Day` takes mon, tue, wed, thu, fri, sat, sun, daily, or fri-last for the last Friday of the month.

    | Day | What | How |
    |---|---|---|
    | {day} | {what} | {the prompt or the skill to run} |

**Show** the rows with the link, then say:

> "This is [RHYTHM.md](RHYTHM.md). On {the next weekday with a row}, when you open with 'good morning', I'll ask whether to start with {that row}."

## Phase 7 of 8, your tools and your voice

**Say:**

> "Phase 7 of 8, your tools and your voice. First I check what I can already reach, then I help you connect what is missing, then I learn how you write."

**Check**, narrating it: name what this session can reach from its own tool list, `claude mcp list`, and the command lines on the path (`gh`, `gws`), and prove each one answers with one small read. Compare the list with the tools in `USER.md`.

**Say** which tools are connected and which are missing, in one list. For each missing one, ask: "Connect {tool} now?" Yes, guide me (Recommended), Later. On yes, one step per message, waiting for the user each time:

1. Gmail, Google Calendar, Google Drive, Slack, Notion, Exa and the other connectors claude.ai lists: open https://claude.ai/settings/connectors, click Connect next to the tool, sign in and allow. A connector added now loads in a new session on this folder: say so, and offer to finish this phase there with "continue setup".
2. A tool claude.ai does not list: open the tool's own MCP page, which you search for and link, and add it with the line it gives, for example `claude mcp add --transport http {name} {url}`.

**Then the voice**, through `distil`, variant `voice`. **Say:**

> "Now your voice. Each one starts from a preset of base rules, tested on months of posts and emails. What I learn from your own writing goes on top, and a rule of yours always wins over a base rule."

- **Emails**, the `outreach` channel. With Gmail connected: "I can learn how you write emails from the ones you sent: I read up to 30 of your sent emails from the last 90 days and write down the rules, never the emails." Ask: Yes, learn my email voice (Recommended), Not now.
- **Posts**, the `content` channel: "To learn how you write posts, I need your posts. LinkedIn does not let me open your profile." Ask:
  - Connect Exa and find my public posts (Recommended): "Exa is a web search with a free plan. It finds the posts search engines index, often most of them." Guide it as step 1 above, or add its free server with `claude mcp add --transport http exa https://mcp.exa.ai/mcp`, which works without an account at lower limits. Then ask for the profile link.
  - I'll paste five or more posts here.
  - I'll drop the LinkedIn export: LinkedIn, Settings, Data privacy, Get a copy of your data, Posts, then the file into `06-sources/raw/`.
  - Not now.

Each voice lives in `01-workstreams/{area}/01-knowledge/voice.md`, in the area that writes that channel. No such area: ask which area writes it, with the areas as options and Skip this voice. A channel left at "Not now" still gets its preset, so drafts follow the base rules until there is material.

**Show** each voice file written as a link, then say:

> "From now on I read these files before I draft an email or a post. When you correct a draft, the correction goes in the file, and distil turns the corrections that come back into rules."

## Phase 8 of 8, the tour

**Say:**

> "Phase 8 of 8: a short tour of what you now have."

Then open [TOUR.md](TOUR.md) and run it, with the rules of this file.
