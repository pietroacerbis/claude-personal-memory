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

## Recent learnings
FIXTURE_EOF
mkdir -p "$(dirname "04-memory/sessions/2026-11/2026-11-16.md")"
cat > "04-memory/sessions/2026-11/2026-11-16.md" <<'FIXTURE_EOF'
# Day 2026-11-16

sessions: 1

## Session 1, 09:00, pricing-page

**Status:** open
**Scope:** finish the pricing page copy
**Opened:** USER.md, 04-memory/MEMORY.md
**Done:** [session-end]
**Decisions:** [session-end]
**Carries:** [session-end]
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/pricing/map.md")"
cat > "02-projects/pricing/map.md" <<'FIXTURE_EOF'
# Pricing page, the map

- **What it produces**: the new pricing page
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/pricing/latest.md")"
cat > "02-projects/pricing/latest.md" <<'FIXTURE_EOF'
# latest, 2026-11-10

**Last point.** 2026-11-10: project opened.

**Next step.** Draft the copy.

**Blockers.** none
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/pricing/history.md")"
cat > "02-projects/pricing/history.md" <<'FIXTURE_EOF'
# History

2026-11-10 | [milestone] **Project opened**
FIXTURE_EOF
mkdir -p "$(dirname "02-projects/pricing/03-artifacts/copy.md")"
cat > "02-projects/pricing/03-artifacts/copy.md" <<'FIXTURE_EOF'
# Pricing page copy

Starter, Growth, and Enterprise on request.
FIXTURE_EOF
