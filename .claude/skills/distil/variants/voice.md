# distil, variant voice

Opened at stop 0 when the user asks Claude to learn how they write, hands over emails or posts, or setup reaches its last phase. Two channels, one file each, never mixed: `outreach` (emails, DMs) and `content` (posts). A rule learned from emails never governs a post.

## Read, up to 30 items the user wrote

| Source | Channel | How |
|---|---|---|
| Gmail | outreach | whichever Gmail tool the session has. A connector or MCP: search threads with `in:sent newer_than:90d`, then read each one. The `gws` command line: `gws gmail users messages list --params '{"userId":"me","q":"in:sent newer_than:90d","maxResults":60}'`, then `gws gmail +read --id ID --headers` |
| LinkedIn export | content | `Shares.csv` from the LinkedIn data export, dropped in `06-sources/raw/`: `python3 ${CLAUDE_SKILL_DIR}/scripts/linkedin_posts.py 06-sources/raw/Shares.csv` |
| Exa, connected | content | search the web for the user's public LinkedIn posts by name and profile link, `linkedin.com/posts` only; keep only posts the user wrote, and say how many were found, since search finds the indexed ones, not always all |
| pasted in chat | either | each post or email the user pastes is one item |
| corrected drafts | either | a draft Claude wrote that the user changed, in this chat or in a journal since the last voice run, `python3 ${CLAUDE_SKILL_DIR}/scripts/journals.py voice`. The user's version is the item; the change is a correction |

No Gmail tool and no `gws`: say so, and ask for pasted emails or the export instead. Never ask for a password or a key.

**Keep only the user's own words.** Cut quoted replies (lines that start with `>`, everything below "On ... wrote:"), signatures and forwarded text. Skip auto-replies, out-of-office mail, calendar mail (invitations, accepted, declined), newsletters, and replies of one line. Count what is left: fewer than 5 items is a STOP.

## The area

The file is `01-workstreams/{area}/01-knowledge/voice.md`, in the area whose `README.md` says it writes that channel. One area plainly matches: use it. Several, or none clear: ask which, with the areas as options. No area at all: offer to create one in the shape of `01-workstreams/README.md`, named `content` or `outreach`, and wait for the yes.

## The rules

A rule is something three items or more do, written as an instruction with its count: `Open with a number or a result, never a greeting (5 of 6)`.

- **Words I use**: phrases that come back in three items or more.
- **Words I never use**: what the user corrected out, and what is common in the channel but absent from every item (hashtags, emojis, "excited to announce"), marked `(in none of 6)`.
- **A correction wins over the material**: written with `(your correction, YYYY-MM-DD)`, and never replaced by a count.

**A re-run merges.** Read the file whole first. The counts of rules the new items show are updated; a new rule enters only at three items or more; a rule the new items contradict is shown at the gate, never changed in silence; a correction stays as written.

## The file

    ---
    description: how I write {channel}, read before drafting one
    channel: {channel}
    updated: YYYY-MM-DD
    items: 6 posts, YYYY-MM-DD to YYYY-MM-DD
    ---

    # Voice, {channel}

    ## How I open
    ## Length
    ## Sentence shape
    ## Words I use
    ## Words I never use
    ## How I close
    ## Excerpts

**Excerpts**: at most three, two lines each, quoted from the items. No name of a recipient or of any person or company other than the user's own, no email, phone number or link. After the write, check:

    python3 ${CLAUDE_SKILL_DIR}/scripts/personal_data.py 01-workstreams/{area}/01-knowledge/voice.md

Exit 1: remove each line it names, then run it again. It cannot see a name, so read every excerpt once more before the report.

## The gate list

    1. Write 01-workstreams/content/01-knowledge/voice.md from 6 posts: 9 rules, 3 excerpts (show 1 prints the file)
    2. Left out, seen in fewer than three items: "starts with a question" (2 of 6)

## The log line

    YYYY-MM-DD | [content] voice learned from 6 posts -> 01-workstreams/content/01-knowledge/voice.md

## STOP records

- `STOP: too few items` when fewer than 5 are left. Say how many, and what brings more: connect Gmail, drop `Shares.csv` in `06-sources/raw/`, paste more posts or emails. Write nothing.
- `STOP: no material` when there is no Gmail tool, no export and nothing pasted.
- `STOP: no area` when the user chooses no area and declines a new one.

Setup calls this variant at its last phase, once the user connects Gmail or hands over posts. A STOP there becomes a `TODO` line in setup's closing summary, and setup goes on.
