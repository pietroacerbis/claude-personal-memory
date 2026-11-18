#!/bin/bash
set -e
mkdir -p "$(dirname "USER.md")"
cat > "USER.md" <<'FIXTURE_EOF'
# USER, Ana

## Role
Founder, Tallyline

## Language
English

## How to talk to me
- Short and direct, the answer first.
FIXTURE_EOF
mkdir -p "$(dirname "01-workstreams/sales/01-knowledge/.gitkeep")"
touch "01-workstreams/sales/01-knowledge/.gitkeep"
mkdir -p "$(dirname "01-workstreams/sales/02-artifacts/.gitkeep")"
touch "01-workstreams/sales/02-artifacts/.gitkeep"
mkdir -p "$(dirname "01-workstreams/sales/03-archive/.gitkeep")"
touch "01-workstreams/sales/03-archive/.gitkeep"
mkdir -p "$(dirname "01-workstreams/sales/README.md")"
cat > "01-workstreams/sales/README.md" <<'FIXTURE_EOF'
# Sales

Finding and closing the first ten teams. Folders: 01-knowledge, 02-artifacts, 03-archive.
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/_TEMPLATE/history.md")"
cat > "02-projects/_TEMPLATE/history.md" <<'FIXTURE_EOF'
# History

Newest first. One line per entry: `YYYY-MM-DD | [type] **what happened**, who decided: the detail`.

YYYY-MM-DD | [milestone] **Project opened**
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/_TEMPLATE/latest.md")"
cat > "02-projects/_TEMPLATE/latest.md" <<'FIXTURE_EOF'
# latest, YYYY-MM-DD

**Last point.** YYYY-MM-DD: what just happened.

**Next step.** One.

**Blockers.** What stops the next step, or none.
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/_TEMPLATE/map.md")"
cat > "02-projects/_TEMPLATE/map.md" <<'FIXTURE_EOF'
# {Project}, the map

- **What it produces**: TODO
- **Why now**: TODO
- **Done when**: TODO, a date and the result that proves it
- **Owner**: TODO
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/onboarding/history.md")"
cat > "02-projects/onboarding/history.md" <<'FIXTURE_EOF'
# History

2026-11-12 | [milestone] **Project opened**
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/onboarding/latest.md")"
cat > "02-projects/onboarding/latest.md" <<'FIXTURE_EOF'
# latest, 2026-11-12

**Last point.** 2026-11-12: project opened.

**Next step.** Draft email one.

**Blockers.** none
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/onboarding/map.md")"
cat > "02-projects/onboarding/map.md" <<'FIXTURE_EOF'
# Onboarding emails, the map

- **What it produces**: five emails for a new trial
- **Why now**: half the trials never invite a second user
- **Done when**: 2026-12-20, the five emails are live
- **Owner**: Ana
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/pricing/03-artifacts/copy.md")"
cat > "02-projects/pricing/03-artifacts/copy.md" <<'FIXTURE_EOF'
# Pricing page copy

Starter and Growth. Enterprise on request.
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/pricing/history.md")"
cat > "02-projects/pricing/history.md" <<'FIXTURE_EOF'
# History

2026-11-16 | [decision] **Two tiers only**, Ana: enterprise on request
2026-11-10 | [milestone] **Project opened**
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/pricing/latest.md")"
cat > "02-projects/pricing/latest.md" <<'FIXTURE_EOF'
# latest, 2026-11-16

**Last point.** 2026-11-16: copy drafted, see [copy.md](03-artifacts/copy.md).

**Next step.** Ask Jo for the enterprise line.

**Blockers.** none
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/pricing/map.md")"
cat > "02-projects/pricing/map.md" <<'FIXTURE_EOF'
# Pricing page, the map

- **What it produces**: the new pricing page
- **Why now**: trials stall on the price question
- **Done when**: 2026-12-15, the page is live
- **Owner**: Ana
FIXTURE_EOF
mkdir -p "$(dirname "04-memory/MEMORY.md")"
cat > "04-memory/MEMORY.md" <<'FIXTURE_EOF'
# MEMORY, Ana

## Active work
- Pricing page, [02-projects/pricing/](../02-projects/pricing/)
- Onboarding emails, [02-projects/onboarding/](../02-projects/onboarding/)

## Decisions
- 2026-11-10, [two tiers only](decisions/2026-11-10-two-tiers.md)

## Mistakes log
| Rule | When it applies |
| --- | --- |
| Never send a draft without the numbers checked | an email to an investor |
| Say the price in euros first | any pricing copy |
| The answer first, then the reasons | every reply |
| Dates as YYYY-MM-DD | every file |
| One question at a time | when something is unclear |
| No tables in a message to a customer | customer emails |
| Name the file you changed | after every write |
| Keep a subject line under eight words | outbound emails |
| Ask before renaming a folder | any move |
| Quote the customer's own words | call notes |
| Round revenue to the thousand | investor updates |
| Write the next step as a verb | latest.md |
| Never promise a date for a feature | customer replies |
| Show the diff before a rewrite | any edit over ten lines |
| Use the customer's company name, never 'the client' | every draft |
| Put the ask in the first paragraph | emails to Jo |
| Mark a guess as a guess | research notes |
| Keep a post under 200 words | LinkedIn drafts |
| Spell Tallyline with one capital | every file |
| Never paste a full transcript into a project | after a call |
| Link the source of every number | the board deck |
| Close with the one next action | every plan |
| Name trial users by first name only | notes and drafts |
| Monthly price before yearly price | pricing copy |
| Write 'team' where it says 'seat' | pricing copy |
| Check the calendar before proposing a slot | scheduling emails |
| No exclamation marks | anything sent out |

## Recent learnings
- 2026-11-14 · Short briefs get read, long ones get skipped.
FIXTURE_EOF
mkdir -p "$(dirname "04-memory/README.md")"
cat > "04-memory/README.md" <<'FIXTURE_EOF'
# 04-memory

What makes Claude remember.

| File | Holds | Cap |
|---|---|---|
| `MEMORY.md`, `## Quarter goals` | the goals of this quarter | 5 lines |
| `MEMORY.md`, `## Roadmap` | the steps toward those goals | 12 lines |
| `MEMORY.md`, `## Active work` | one line per piece of work in progress | 12 lines |
| `MEMORY.md`, `## Decisions` | the ten newest decisions | 10 lines |
| `MEMORY.md`, `## Mistakes log` | each correction: the rule, and when it applies | 25 rows |
| `MEMORY.md`, `## Recent learnings` | what worked | 30 lines |
| `archive/` | rows moved out of `MEMORY.md` when a section passes its cap | none |
FIXTURE_EOF
mkdir -p "$(dirname "04-memory/decisions/2026-11-10-two-tiers.md")"
cat > "04-memory/decisions/2026-11-10-two-tiers.md" <<'FIXTURE_EOF'
---
description: show two tiers, enterprise on request
date: 2026-11-10
status: active
---

# Two tiers only

**Why:** a third tier confused the trial users.
FIXTURE_EOF
mkdir -p "$(dirname "04-memory/decisions/2026-11-12-hire.md")"
cat > "04-memory/decisions/2026-11-12-hire.md" <<'FIXTURE_EOF'
---
description: hire a part-time designer in January
date: 2026-11-12
---

# Hire a part-time designer

**Why:** the pricing page needs real visuals.
FIXTURE_EOF
mkdir -p "$(dirname "04-memory/sessions/2026-11/2026-11-16.md")"
cat > "04-memory/sessions/2026-11/2026-11-16.md" <<'FIXTURE_EOF'
# Day 2026-11-16

sessions: 1

## Session 1, 09:00, pricing-page

**Status:** closed
**Scope:** pricing page copy
**Opened:** USER.md, 04-memory/MEMORY.md
**Done:** copy drafted, 02-projects/pricing/03-artifacts/copy.md
**Decisions:** two tiers only, 04-memory/decisions/2026-11-10-two-tiers.md
**Carries:** none

## Session 2, 15:00, outbound

**Status:** open
**Scope:** first outbound list
**Opened:** USER.md, 04-memory/MEMORY.md
**Done:** [session-end]
**Decisions:** [session-end]
**Carries:** [session-end]
FIXTURE_EOF
mkdir -p "$(dirname "index.md")"
cat > "index.md" <<'FIXTURE_EOF'
# Index

Every file of this workspace with its description. Claude reads this first and opens only what the task needs.
Rebuilt after every write by `.claude/skills/brain-lint/scripts/reindex.py`: never edit it by hand.

## Root

- [USER.md](USER.md): Founder, Tallyline

## 01-workstreams

- [01-workstreams/sales/README.md](01-workstreams/sales/README.md): Finding and closing the first ten teams. Folders: 01-knowledge, 02-artifacts, 03-archive.

## 02-projects

- [02-projects/onboarding/history.md](02-projects/onboarding/history.md): 2026-11-12 | [milestone] Project opened
- [02-projects/onboarding/latest.md](02-projects/onboarding/latest.md): Last point. 2026-11-12: project opened.
- [02-projects/onboarding/map.md](02-projects/onboarding/map.md): What it produces: five emails for a new trial
- [02-projects/pricing/history.md](02-projects/pricing/history.md): 2026-11-16 | [decision] Two tiers only, Ana: enterprise on request
- [02-projects/pricing/latest.md](02-projects/pricing/latest.md): Last point. 2026-11-16: copy drafted, see copy.md.
- [02-projects/pricing/map.md](02-projects/pricing/map.md): What it produces: the new pricing page
- [02-projects/pricing/03-artifacts/copy.md](02-projects/pricing/03-artifacts/copy.md): Starter and Growth. Enterprise on request.

## 04-memory

- [04-memory/MEMORY.md](04-memory/MEMORY.md): Pricing page, 02-projects/pricing/
- [04-memory/README.md](04-memory/README.md): What makes Claude remember.
- [04-memory/decisions/2026-11-10-two-tiers.md](04-memory/decisions/2026-11-10-two-tiers.md): show two tiers, enterprise on request
- [04-memory/decisions/2026-11-12-hire.md](04-memory/decisions/2026-11-12-hire.md): hire a part-time designer in January
FIXTURE_EOF
mkdir -p "$(dirname "log.md")"
cat > "log.md" <<'FIXTURE_EOF'
# Log

What happened in this workspace, newest first, one line per event.

    YYYY-MM-DD | [area] what changed -> path

## Entries

2026-11-16 | [pricing] decided two tiers only -> 02-projects/pricing/history.md
2026-11-12 | [onboarding] project opened -> 02-projects/onboarding/map.md
2026-11-10 | [pricing] project opened -> 02-projects/pricing/map.md
FIXTURE_EOF
