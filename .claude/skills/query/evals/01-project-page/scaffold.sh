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
- Never: long introductions.
FIXTURE_EOF
mkdir -p "$(dirname "index.md")"
cat > "index.md" <<'FIXTURE_EOF'
# Index

Every file of this workspace with its description. Claude reads this first and opens only what the task needs.
Rebuilt after every write by `.claude/skills/brain-lint/scripts/reindex.py`: never edit it by hand.

## Root

- [USER.md](USER.md): Founder, Tallyline

## 01-workstreams

- [01-workstreams/sales/README.md](01-workstreams/sales/README.md): Finding and closing the teams that buy Tallyline. Folders: 01-knowledge, 02-artifacts, 03-archive.
- [01-workstreams/sales/01-knowledge/pricing.md](01-workstreams/sales/01-knowledge/pricing.md): Tallyline plans and prices, as sold today

## 02-projects

- [02-projects/northwind-pilot/history.md](02-projects/northwind-pilot/history.md): 2026-10-28 | [milestone] Pilot plan agreed with Priya Raman
- [02-projects/northwind-pilot/latest.md](02-projects/northwind-pilot/latest.md): Last point. 2026-10-28: pilot plan agreed with Priya Raman.
- [02-projects/northwind-pilot/map.md](02-projects/northwind-pilot/map.md): What it produces: a six-week paid pilot of Tallyline with the ops team of Northwind Freight
- [02-projects/website-redesign/history.md](02-projects/website-redesign/history.md): 2026-11-14 | [milestone] Homepage wireframes approved by Marta
- [02-projects/website-redesign/latest.md](02-projects/website-redesign/latest.md): Last point. 2026-11-14: Marta approved the homepage wireframes.
- [02-projects/website-redesign/map.md](02-projects/website-redesign/map.md): What it produces: the new Tallyline website, homepage and pricing page

## 04-memory

- [04-memory/MEMORY.md](04-memory/MEMORY.md): 40 paying teams by 2026-12-31
- [04-memory/decisions/2026-09-15-monthly-and-annual.md](04-memory/decisions/2026-09-15-monthly-and-annual.md): Sell monthly and annual plans side by side
- [04-memory/decisions/2026-11-04-annual-plans-only.md](04-memory/decisions/2026-11-04-annual-plans-only.md): Annual plans only, monthly billing dropped

## 06-sources

- [06-sources/research/2026-10-20-competitor-pricing.md](06-sources/research/2026-10-20-competitor-pricing.md): What three competitors charged on 2026-10-20
FIXTURE_EOF
mkdir -p "$(dirname "04-memory/MEMORY.md")"
cat > "04-memory/MEMORY.md" <<'FIXTURE_EOF'
# MEMORY, Ana

## Quarter goals
- 40 paying teams by 2026-12-31

## Active work
- Website redesign, 02-projects/website-redesign/
- Northwind pilot, 02-projects/northwind-pilot/

## Decisions
- 2026-11-04 Annual plans only, monthly billing dropped -> 04-memory/decisions/2026-11-04-annual-plans-only.md

## Mistakes log
| Rule | When it applies |
| --- | --- |
| The answer first, then the reasons | every reply |

## Recent learnings
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/website-redesign/map.md")"
cat > "02-projects/website-redesign/map.md" <<'FIXTURE_EOF'
# Website redesign, the map

- **What it produces**: the new Tallyline website, homepage and pricing page
- **Why now**: the old site still sells the 2025 product
- **Done when**: the new homepage is live, by 2026-12-15
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/website-redesign/latest.md")"
cat > "02-projects/website-redesign/latest.md" <<'FIXTURE_EOF'
# latest, 2026-11-14

**Last point.** 2026-11-14: Marta approved the homepage wireframes.

**Next step.** Brief the copywriter, Luca Ferri, on the homepage copy by 2026-11-21.

**Blockers.** The new logo files from the studio are late, promised for 2026-11-19.
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/website-redesign/history.md")"
cat > "02-projects/website-redesign/history.md" <<'FIXTURE_EOF'
# History

2026-11-14 | [milestone] **Homepage wireframes approved** by Marta
2026-10-30 | [decision] **Two pages first**: homepage and pricing page, the blog waits for 2027
2026-10-20 | [milestone] **Project opened**
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/northwind-pilot/map.md")"
cat > "02-projects/northwind-pilot/map.md" <<'FIXTURE_EOF'
# Northwind pilot, the map

- **What it produces**: a six-week paid pilot of Tallyline with the ops team of Northwind Freight
- **Why now**: Northwind is the first logistics customer, and the reference for the next three
- **Done when**: Priya Raman, head of operations at Northwind, signs the pilot report
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/northwind-pilot/latest.md")"
cat > "02-projects/northwind-pilot/latest.md" <<'FIXTURE_EOF'
# latest, 2026-10-28

**Last point.** 2026-10-28: pilot plan agreed with Priya Raman.

**Next step.** The pilot starts on 2026-11-24 with the Northwind ops team, twelve users.

**Blockers.** none
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/northwind-pilot/history.md")"
cat > "02-projects/northwind-pilot/history.md" <<'FIXTURE_EOF'
# History

2026-10-28 | [milestone] **Pilot plan agreed** with Priya Raman
2026-10-15 | [milestone] **Project opened**
FIXTURE_EOF
mkdir -p "$(dirname "01-workstreams/sales/README.md")"
cat > "01-workstreams/sales/README.md" <<'FIXTURE_EOF'
# Sales

Finding and closing the teams that buy Tallyline. Folders: 01-knowledge, 02-artifacts, 03-archive.
FIXTURE_EOF
mkdir -p "$(dirname "01-workstreams/sales/01-knowledge/pricing.md")"
cat > "01-workstreams/sales/01-knowledge/pricing.md" <<'FIXTURE_EOF'
---
description: Tallyline plans and prices, as sold today
---

# Pricing

| Plan | Price | Who |
|---|---|---|
| Starter | 600 EUR a year | up to 5 users |
| Growth | 1,500 EUR a year | up to 20 users |

Annual billing only, [the decision](../../../04-memory/decisions/2026-11-04-annual-plans-only.md).
FIXTURE_EOF
mkdir -p "$(dirname "04-memory/decisions/2026-09-15-monthly-and-annual.md")"
cat > "04-memory/decisions/2026-09-15-monthly-and-annual.md" <<'FIXTURE_EOF'
---
description: Sell monthly and annual plans side by side
date: 2026-09-15
status: superseded
---

# Monthly and annual plans side by side

**Why:** monthly lowers the first step for small teams
**Alternatives:** annual only
**Revisit:** after 20 paying teams

Superseded on 2026-11-04 by [annual plans only](2026-11-04-annual-plans-only.md).
FIXTURE_EOF
mkdir -p "$(dirname "04-memory/decisions/2026-11-04-annual-plans-only.md")"
cat > "04-memory/decisions/2026-11-04-annual-plans-only.md" <<'FIXTURE_EOF'
---
description: Annual plans only, monthly billing dropped
date: 2026-11-04
status: active
---

# Annual plans only

**Why:** monthly teams churned at three times the rate of annual ones, for the same support cost
**Alternatives:** keep monthly at a higher price, dropped
**Revisit:** at 40 paying teams
FIXTURE_EOF
mkdir -p "$(dirname "04-memory/sessions/2026-11/2026-11-12.md")"
cat > "04-memory/sessions/2026-11/2026-11-12.md" <<'FIXTURE_EOF'
# Day 2026-11-12

sessions: 2

## Session 1, 09:30, northwind-pilot

**Status:** closed
**Scope:** the pilot kickoff call with Northwind
**Opened:** USER.md, 04-memory/MEMORY.md, 02-projects/northwind-pilot/latest.md
**Done:** Kickoff call with Priya Raman
**Decisions:** Pilot start moved to 2026-12-08: Northwind needs two more weeks to export their shipment data
**Carries:** none

## Session 2, 15:00, sales

**Status:** closed
**Scope:** pipeline review
**Opened:** USER.md, 04-memory/MEMORY.md
**Done:** Intro call with Brightwave Studios booked for 2026-11-20
**Decisions:** none
**Carries:** prepare the Brightwave intro deck
FIXTURE_EOF
mkdir -p "$(dirname "04-memory/sessions/2026-11/2026-11-13.md")"
cat > "04-memory/sessions/2026-11/2026-11-13.md" <<'FIXTURE_EOF'
# Day 2026-11-13

sessions: 1

## Carryover in

From the day before, session 2, sales:
- prepare the Brightwave intro deck

## Session 1, 10:00, sales

**Status:** closed
**Scope:** the enterprise line
**Opened:** USER.md, 04-memory/MEMORY.md, 01-workstreams/sales/01-knowledge/pricing.md
**Done:** Call with Jo Lindqvist on the enterprise line
**Decisions:** Enterprise line agreed with Jo: 90 EUR per seat a year, minimum 25 seats
**Carries:** add the enterprise line to 01-workstreams/sales/01-knowledge/pricing.md
FIXTURE_EOF
mkdir -p "$(dirname "log.md")"
cat > "log.md" <<'FIXTURE_EOF'
# Log

What happened in this workspace, newest first, one line per event: a source ingested, a decision, a project opened or closed, a voice updated. The skill that made the change writes the line; a line is never rewritten.

    YYYY-MM-DD | [area] what changed -> path

`area` is a workstream, a project, `memory` or `workspace`. The path is the file that holds the change now.

## Entries

2026-11-14 | [website-redesign] homepage wireframes approved -> 02-projects/website-redesign/history.md
2026-11-04 | [memory] decision: annual plans only -> 04-memory/decisions/2026-11-04-annual-plans-only.md
2026-10-28 | [northwind-pilot] pilot plan agreed -> 02-projects/northwind-pilot/history.md
2026-10-20 | [website-redesign] project opened -> 02-projects/website-redesign/map.md
2026-10-15 | [northwind-pilot] project opened -> 02-projects/northwind-pilot/map.md
2026-10-01 | [workspace] workspace set up: 1 area, 2 projects, 1 goal -> USER.md
FIXTURE_EOF
mkdir -p "$(dirname "06-sources/research/2026-10-20-competitor-pricing.md")"
cat > "06-sources/research/2026-10-20-competitor-pricing.md" <<'FIXTURE_EOF'
---
description: What three competitors charged on 2026-10-20
---

# Competitor pricing, 2026-10-20

- Quillmark: 12 EUR per seat a month, monthly or annual
- Tabsy: 9 EUR per seat a month, annual only
- Fernbook: free up to 3 users, then 15 EUR per seat a month
FIXTURE_EOF
