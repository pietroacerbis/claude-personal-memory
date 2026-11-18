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

## How I work
TODO: what I want Claude to know about how I work. It fills in as we go.
FIXTURE_EOF
mkdir -p "$(dirname "index.md")"
cat > "index.md" <<'FIXTURE_EOF'
# Index

Every file of this workspace with its description. Claude reads this first and opens only what the task needs.
Rebuilt after every write by `.claude/skills/brain-lint/scripts/reindex.py`: never edit it by hand.

## Root

- [USER.md](USER.md): Founder, Tallyline

## 01-workstreams

- [01-workstreams/sales/README.md](01-workstreams/sales/README.md): Sales: finding, closing and keeping Tallyline's customers.
- [01-workstreams/sales/01-knowledge/customers.md](01-workstreams/sales/01-knowledge/customers.md): Every customer and prospect, one section each: who they are, who decides, where we stand.
- [01-workstreams/sales/01-knowledge/pricing.md](01-workstreams/sales/01-knowledge/pricing.md): Tallyline's price list and the discounts Ana allows.

## 02-projects

- [02-projects/README.md](02-projects/README.md): Work with a start and an end. Copy _TEMPLATE/ to 02-projects/{slug}/ to open one, or let SETUP.md do it.
- [02-projects/quillmoor-pilot/history.md](02-projects/quillmoor-pilot/history.md): Newest first. One line per entry: YYYY-MM-DD | [type] what happened, who decided: the detail...
- [02-projects/quillmoor-pilot/latest.md](02-projects/quillmoor-pilot/latest.md): Last point. 2026-11-10: Jo agreed to a pilot in principle.
- [02-projects/quillmoor-pilot/map.md](02-projects/quillmoor-pilot/map.md): What it produces: a paid pilot of Tallyline at Quillmoor Foods
FIXTURE_EOF
mkdir -p "$(dirname "log.md")"
cat > "log.md" <<'FIXTURE_EOF'
# Log

What happened in this workspace, newest first, one line per event: a source ingested, a decision, a project opened or closed, a voice updated. The skill that made the change writes the line; a line is never rewritten.

    YYYY-MM-DD | [area] what changed -> path

`area` is a workstream, a project, `memory` or `workspace`. The path is the file that holds the change now.

## Entries

2026-11-10 | [quillmoor-pilot] project opened -> 02-projects/quillmoor-pilot/map.md
FIXTURE_EOF
mkdir -p "$(dirname "01-workstreams/sales/README.md")"
cat > "01-workstreams/sales/README.md" <<'FIXTURE_EOF'
# Sales

Sales: finding, closing and keeping Tallyline's customers.

| Folder | Holds |
|---|---|
| `01-knowledge/` | customers, prices, how a deal runs |
| `02-artifacts/` | proposals and quotes sent |
| `03-archive/` | what retired |
FIXTURE_EOF
mkdir -p "$(dirname "01-workstreams/sales/01-knowledge/customers.md")"
cat > "01-workstreams/sales/01-knowledge/customers.md" <<'FIXTURE_EOF'
# Customers

Every customer and prospect, one section each: who they are, who decides, where we stand.

## Quillmoor Foods

- Regional food distributor, 40 people in the back office.
- Contact: Jo Brannick, head of operations.
- Pilot agreed in principle on 2026-11-10.

## Fenmarsh Freight

- Freight forwarder, first met at a trade fair on 2026-11-05.
- Contact: Dario Velt, operations director.
FIXTURE_EOF
mkdir -p "$(dirname "01-workstreams/sales/01-knowledge/pricing.md")"
cat > "01-workstreams/sales/01-knowledge/pricing.md" <<'FIXTURE_EOF'
# Pricing

Tallyline's price list and the discounts Ana allows.

- Starter: 19 euros per seat per month.
- Growth: 39 euros per seat per month, from 10 seats.
- Discounts: up to 10% on annual prepay, nothing else without Ana.
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/README.md")"
cat > "02-projects/README.md" <<'FIXTURE_EOF'
# 02-projects

Work with a start and an end. Copy `_TEMPLATE/` to `02-projects/{slug}/` to open one, or let `SETUP.md` do it.

| File | Holds | How it changes |
|---|---|---|
| `map.md` | what the project produces, why now, when it is done, and its tickets | its head changes only with a decision logged in `history.md` |
| `latest.md` | where it stands: the last point, the next step, the blockers | rewritten at every close, at most fifteen lines |
| `history.md` | decisions, milestones, changes of plan, newest first | lines are added, never rewritten |
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/quillmoor-pilot/map.md")"
cat > "02-projects/quillmoor-pilot/map.md" <<'FIXTURE_EOF'
# Quillmoor pilot, the map

- **What it produces**: a paid pilot of Tallyline at Quillmoor Foods
- **Why now**: their year-end close runs in January
- **Done when**: 2026-12-15, the pilot is signed and live
- **Owner**: Ana

## Tickets

Status: ✅ done, ⏳ running, 🟢 ready, 🔒 blocked.

| # | Ticket | What it does | Output | Status | Blocked by |
|---|---|---|---|---|---|
| 1 | Scoping call | agree seats and start date with Jo | the pilot scope | 🟢 | none |
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/quillmoor-pilot/latest.md")"
cat > "02-projects/quillmoor-pilot/latest.md" <<'FIXTURE_EOF'
# latest, 2026-11-10

**Last point.** 2026-11-10: Jo agreed to a pilot in principle.

**Next step.** Book the scoping call with Jo.

**Blockers.** none
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/quillmoor-pilot/history.md")"
cat > "02-projects/quillmoor-pilot/history.md" <<'FIXTURE_EOF'
# History

Newest first. One line per entry: `YYYY-MM-DD | [type] **what happened**, who decided: the detail`. Types: `[decision]`, `[milestone]`, `[deviation]` when the plan changed, `[finding]` when a fact changed the plan.

2026-11-10 | [milestone] **Project opened**
FIXTURE_EOF
mkdir -p "06-sources/raw"
touch "06-sources/raw/.gitkeep"
