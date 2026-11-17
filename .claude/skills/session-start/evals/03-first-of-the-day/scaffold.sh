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
mkdir -p "$(dirname "RHYTHM.md")"
cat > "RHYTHM.md" <<'FIXTURE_EOF'
# RHYTHM

| Day | What | How |
|---|---|---|
| daily | Plan the day | ask me for my three priorities |
FIXTURE_EOF
