# decisions

One file per decision that reaches across projects or sets where you are going: a hire, a market, a price, a tool you commit to. A decision about one project stays in that project's `history.md`.

Name: `YYYY-MM-DD-{slug}.md`, the day it was taken. Written by `session-end` when a session decided something, or on the spot when you say "write this down as a decision".

    ---
    description: the decision in one line
    date: YYYY-MM-DD
    status: active
    ---

    # {the decision}

    **Why:** the reasons, in your words
    **Alternatives:** what was weighed and dropped
    **Revisit:** a date, or the event that reopens it

When a decision changes, the old file takes `status: superseded` and a link to the new one; it is never deleted. The ten newest active ones are listed in `## Decisions` of `04-memory/MEMORY.md`.
