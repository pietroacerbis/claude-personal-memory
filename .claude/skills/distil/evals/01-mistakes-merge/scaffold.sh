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
mkdir -p "$(dirname "04-memory/MEMORY.md")"
cat > "04-memory/MEMORY.md" <<'FIXTURE_EOF'
# MEMORY, Ana

## Active work
- Pricing page, 02-projects/pricing/

## Mistakes log
| Rule | When it applies |
| --- | --- |
| The answer first, then the reasons | every reply |
| Never send an email without showing me the draft | any email or DM |
| Lead with the conclusion and put the explanation after it | status updates and summaries |
| Dates as YYYY-MM-DD inside files | any file |

## Recent learnings
FIXTURE_EOF
mkdir -p "$(dirname "log.md")"
cat > "log.md" <<'FIXTURE_EOF'
# Log

What happened in this workspace, newest first, one line per event.

    YYYY-MM-DD | [area] what changed -> path

## Entries

2026-11-10 | [pricing] project opened -> 02-projects/pricing/map.md
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/pricing/map.md")"
cat > "02-projects/pricing/map.md" <<'FIXTURE_EOF'
# Pricing page, the map

- **What it produces**: the new pricing page
FIXTURE_EOF
