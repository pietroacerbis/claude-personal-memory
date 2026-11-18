# TOUR, what you now have

**For Claude.** This is phase 8 of [SETUP.md](SETUP.md), run with its rules. Run it also whenever the user asks for a tour of the workspace.

Before T1, claim a block in today's journal, so the close in T8 has one to fill: `python3 .claude/skills/session-start/scripts/claim_session.py onboarding`, once per conversation. It prints the block number; a line starting with `STOP` is reported as it is.

One stop per message, never two. Close each stop with its links and with "Open it, and tell me when you're done.", then wait. A stop that asks a question ends on the question instead. Keep each stop short: the user is shown where things are, never asked to learn them. Every link is a markdown link they can click.

### T1. Your files

> "Your workspace is plain files in this folder, and five of them matter today: [USER.md](USER.md), who you are; [MEMORY.md](04-memory/MEMORY.md), your goals and what you teach me; [RHYTHM.md](RHYTHM.md), your week; your areas in 01-workstreams; your projects in 02-projects. One more is worth knowing: [index.md](index.md), the catalog of every file with one line each. I read it first, so I open only what a task needs."

### T2. The machinery

> "Behind the files sits the .claude folder, the machinery. Hooks are small scripts that run on their own: one hands me your memory at every open, one refuses a write that carries a password or a key, one rebuilds index.md after every write. Skills are my doers, six of them, each with one job. You start every one of them by talking, never with a command."

The links: [.claude/settings.json](.claude/settings.json), where the hooks are registered, and the six `SKILL.md` files under `.claude/skills/`.

### T3. Your day: session-start and session-end

> "Two skills run every day. When you greet me, 'good morning', session-start opens a numbered block in today's journal, reads your memory and tells you in a few lines where things stand: yesterday's open points, today's rhythm, the goal the work moves. When you write 'that's it for today', session-end writes what we did and decided, puts each decision where it belongs and carries what tomorrow needs, after your yes. Nothing a session learns is lost when you close the chat. Here is today's journal, with the block of this session."

The link: today's journal, `04-memory/sessions/{YYYY-MM}/{YYYY-MM-DD}.md`.

### T4. Filling your knowledge

> "Right now your workspace knows little: two answers per area, and the 'Still to learn' lines in each context.md. Let's fill some of it now, while we are here. I can ask you questions, or you can give me context: a document, a link, a call transcript, notes. Whatever you give me goes through ingest: I keep the original in 06-sources/raw, untouched, and update the pages it changes, after your yes, every fact with a link back to its source."

Ask with AskUserQuestion: "How do we fill it?" Ask me questions (Recommended), I'll give you context, Later.

- **Ask me questions.** Take each area's `## Still to learn` lines as the questions, one area per message, at most three questions per area, each with proposals drawn from what the workspace already says and the user's own. Write each answer into that area's `context.md`, under the section it belongs to, and remove the line from `## Still to learn`. After each area, show its `context.md` as a link.
- **I'll give you context.** Ask for it: pasted text, a link, or a file dragged into the chat. Run `ingest` on each piece.
- **Later.** Say: "Any time, say 'ingest this' with a document, or 'ask me about {area}', and we fill it together."

Then go on to T5: the question there can now be answered from what was just filled.

### T5. Asking: query

> "query answers from your files and names every file it used, so you can check each answer. Pick a question, or type your own."

Ask with AskUserQuestion three questions built from this workspace: "What are my goals this quarter?", "Where does {a project of phase 4} stand?", "What should you always know about {an area of phase 3}?". Answer with `query`, every file used as a link. Then offer one more question, any question.

### T6. Keeping it sharp: distil and brain-lint

> "Two skills keep the workspace sharp over time. distil, once a week: a correction that came back becomes one sharper rule, what worked goes into your learnings, and your voice files get the rules from your latest writing. brain-lint, once a week: broken links, a stale index, a section over its limit, each with its fix, applied on your yes."

When `RHYTHM.md` has no row for them, ask with AskUserQuestion: "Add 'Friday: distil and lint' to your rhythm?" Yes, add it (Recommended), No. On yes, add the row and show [RHYTHM.md](RHYTHM.md).

### T7. Your existing work

> "Last stop: the work you already have. I can bring in your projects from claude.ai, with a prompt you paste inside each one, and folders from this computer, which I copy and never move."

Ask with AskUserQuestion, multi-select: "What should we bring in?" Projects from claude.ai, Folders on this computer, Later. One step per message, waiting for the user each time:

- **Projects from claude.ai.** For each project, say: "Open the project on claude.ai, start a new chat inside it, paste the prompt below, and paste its whole answer back here." Then the prompt, alone in a fenced code block:

      Summarise this project for my workspace, using only what this project's files and chats say. Use these headings: What it produces. Why now. Done when. Owner. Where it stands: last point, next step, blockers. Decisions so far, one dated line each. Open questions. Write "unknown" where the project does not say.

  Run `ingest` on each answer: the raw in `06-sources/raw/`, then `02-projects/{slug}/` built from it, after the user's yes, every file shown as a link. For the chats themselves, the export is on claude.ai, Settings, Privacy, Export data: it holds the conversations, not the files uploaded to them, and the zip goes into `06-sources/raw/`.
- **Folders on this computer.** Ask for the folder: its path, or the folder dragged into the chat. List what it holds, then propose a home for each part: a project, an area's `01-knowledge/`, or `06-sources/raw/` only. Copy, never move: the originals stay where they are. Run `ingest` one part at a time, each after the user's yes.

### T8. The close

Write the rewrite date into `CLAUDE.md`, six months from today, and add one line to `log.md`: `{YYYY-MM-DD} | [workspace] workspace set up: {n} areas, {n} projects, {n} goals -> USER.md`. When `gh auth status` answers, ask: "Keep a private copy of this workspace on your GitHub? It is your backup, and it keeps the history of what I learned." Yes, create it (Recommended), Not now. On yes: `gh repo create {folder-name} --private --source . --push`. Without GitHub, ask nothing.

> "Tour done! Your workspace is ready: you know where things live, what the skills do and how to ask me anything. On {rewrite date} we rewrite the rules in CLAUDE.md from scratch, since newer models need fewer of them. One habit to keep: when you stop, write 'that's it for today'. Try it now."

When the user writes it, `session-end` runs, its gate included. Its report comes first, with every `TODO:` and every item marked for the close listed as a question you will ask at the next open. The last message of the setup ends with today's journal as a link and these two lines, as written:

> "Every session leaves its trace there, and the next one starts from it. Tomorrow, open with 'good morning'."
