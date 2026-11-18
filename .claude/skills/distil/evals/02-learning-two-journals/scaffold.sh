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
- Investor update, 02-projects/investor-update/
- Pricing page, 02-projects/pricing/

## Mistakes log
| Rule | When it applies |
| --- | --- |
| The answer first, then the reasons | every reply |

## Recent learnings
- Ask for the three priorities before planning the day. From sessions/2026-11/2026-11-05.md
FIXTURE_EOF
mkdir -p "$(dirname "log.md")"
cat > "log.md" <<'FIXTURE_EOF'
# Log

What happened in this workspace, newest first, one line per event.

    YYYY-MM-DD | [area] what changed -> path

## Entries

2026-11-10 | [investor-update] project opened -> 02-projects/investor-update/map.md
FIXTURE_EOF
mkdir -p "$(dirname "04-memory/sessions/2026-11/2026-11-03.md")"
cat > "04-memory/sessions/2026-11/2026-11-03.md" <<'FIXTURE_EOF'
# Day 2026-11-03

sessions: 1

## Session 1, 09:00, onboarding

**Status:** closed
**Scope:** set up the workspace
**Opened:** SETUP.md
**Done:** tagline drafted in Italian first and translated after; Ana approved it in one pass, 02-projects/pricing/03-artifacts/tagline.md
**Decisions:** none
**Carries:** none
FIXTURE_EOF
mkdir -p "$(dirname "04-memory/sessions/2026-11/2026-11-12.md")"
cat > "04-memory/sessions/2026-11/2026-11-12.md" <<'FIXTURE_EOF'
# Day 2026-11-12

sessions: 2

## Session 1, 09:10, investor-update

**Status:** closed
**Scope:** draft the November investor update
**Opened:** USER.md, 04-memory/MEMORY.md, 02-projects/investor-update/latest.md
**Done:** outline shown in chat before any file; Ana approved it as it stood, then it was written to 02-projects/investor-update/03-artifacts/outline.md
**Decisions:** numbers before narrative in every investor update, 02-projects/investor-update/history.md
**Carries:** write the full draft from the outline

## Session 2, 15:30, pricing-page

**Status:** closed
**Scope:** the pricing page FAQ
**Opened:** 02-projects/pricing/latest.md
**Done:** latest.md read before starting showed enterprise was already settled as "on request", so the FAQ did not reopen it; FAQ written to 02-projects/pricing/03-artifacts/faq.md
**Decisions:** none
**Carries:** none
FIXTURE_EOF
mkdir -p "$(dirname "04-memory/sessions/2026-11/2026-11-13.md")"
cat > "04-memory/sessions/2026-11/2026-11-13.md" <<'FIXTURE_EOF'
# Day 2026-11-13

sessions: 2

## Carryover in

From 2026-11-12, session 1, investor-update:
- write the full draft from the outline

## Session 1, 10:00, investor-update

**Status:** closed
**Scope:** the full investor update
**Opened:** 02-projects/investor-update/latest.md, 02-projects/investor-update/03-artifacts/outline.md
**Done:** draft shown in chat section by section before the file; Ana approved every section without changes; written to 02-projects/investor-update/03-artifacts/draft.md. Numbers stayed before narrative, as decided on 2026-11-12, and Ana sent it unchanged
**Decisions:** none
**Carries:** none

## Session 2, 16:00, pricing-page

**Status:** closed
**Scope:** pricing page, the tier table
**Opened:** 02-projects/pricing/latest.md
**Done:** latest.md read first again: it named the open blocker, the enterprise line from Jo, so the session started there instead of redoing the tier table; table written to 02-projects/pricing/03-artifacts/tiers.md
**Decisions:** none
**Carries:** none
FIXTURE_EOF
