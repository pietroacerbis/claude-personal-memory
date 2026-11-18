# Quickstart

From a computer without the workspace to a workspace that knows who you are, in the Claude Desktop app. Claude does the work: you answer and click. Tested on macOS.

## Before you start

- **The Claude Desktop app**, signed in, from https://claude.com/download. You work in its **Code** tab.
- **Worktree off, always.** In the Code tab, the row under the prompt box holds a **Worktree** button. It must be off before you send the first message of a session. When it is on, Claude works in a separate copy of the folder, and what it writes stays in that copy. The app remembers your choice: turn it off once, then glance at it each time you start a session.
- **Gmail connected to Claude**, if you can: on https://claude.ai, **Settings**, **Connectors**, **Gmail**, **Connect**. The setup reads your sent mail, with your yes, to learn how you write.

## How to start

1. Download this file: on its GitHub page, the **Download raw file** button. It lands in your Downloads folder.
2. Open the Claude Desktop app, click **Code**, and start a session on your Downloads folder, with Worktree off.
3. Write: `Install my workspace: follow QUICKSTART.md in my Downloads folder.`

Claude installs the workspace (part A). Then you open it in a new session, where Claude walks you through the setup, one phase at a time.

**The workspace is already on your computer?** Start a session on its folder, `claude-workspace` in your Documents folder, with Worktree off, and write: `Good morning Claude, let's set up my workspace.`

## Part A, Claude installs the workspace

**For Claude.** You are running outside the workspace, on a computer that does not have it yet, because the user pointed you at this file. Run A1 to A4 in order. Say the quoted lines as written, without the quote marks, and add nothing around them. Run every command yourself. The user answers and clicks: nothing else. When a command asks for permission, they click **Yes**.

The workspace lives at `~/Documents/claude-workspace`. Use that absolute path in every command, whatever folder this session opened in.

### A1. Hello

**Check.** `ls ~/Documents/claude-workspace/CLAUDE.md` answers: the workspace is already here, so go straight to A4.

**Say.**

> "Hi! I'm going to install your Claude workspace on this computer. It takes a couple of minutes and I run every command. When I ask permission to run a command, click Yes, and if your computer asks whether Claude may open a folder, click OK."

### A2. Git and Python

**Check.** Both print a version: `git --version` and `python3 --version`.

**Write**, only for the one that fails. Tell the user first, in one line: the workspace's hooks are written in Python, so it goes in now. On a Mac, `git --version` or `python3 --version` itself opens the offer to install the command line developer tools, which bring git and Python 3 together: tell the user to click **Install** and wait for it to finish.

**Prove.** Both checks pass.

### A3. Get the workspace

**Write.**

    git clone https://github.com/pietroacerbis/claude-personal-memory ~/Documents/claude-workspace
    git -C ~/Documents/claude-workspace remote remove origin

The second line unhooks the folder from the kit, so it is the user's own. The setup offers to keep a private copy on their GitHub.

**Prove.** `git -C ~/Documents/claude-workspace log --oneline -1` prints a commit, and `git -C ~/Documents/claude-workspace remote` prints nothing.

### A4. Open it

The user opens the workspace in a new session: you cannot open it for them.

**Say**, when A2 installed nothing:

> "Done, your workspace is on your computer! Now open it in a new session: press Cmd+N. In the row under the prompt box, choose the folder claude-workspace in your Documents folder, and check that the Worktree button is off. If the app asks whether you trust the folder, say yes. Then paste this:
>
>     Good morning Claude, let's set up my workspace.
>
> See you there!"

**Say**, when A2 installed something:

> "Done, your workspace is on your computer! One restart first, so the app sees what we just installed: quit the Claude app completely with Cmd+Q, and open it again. Then go to the Code tab and start a new session with Cmd+N. In the row under the prompt box, choose the folder claude-workspace in your Documents folder, and check that the Worktree button is off. If the app asks whether you trust the folder, say yes. Then paste this:
>
>     Good morning Claude, let's set up my workspace.
>
> See you there!"

## Part B, with Claude

In the new session, `USER.md` is missing, so `CLAUDE.md` sends Claude to [SETUP.md](SETUP.md), the guided onboarding in seven phases.
