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
mkdir -p "$(dirname "log.md")"
cat > "log.md" <<'FIXTURE_EOF'
# Log

What happened in this workspace, newest first, one line per event.

    YYYY-MM-DD | [area] what changed -> path

## Entries

2026-11-10 | [pricing] project opened -> 02-projects/pricing/map.md
FIXTURE_EOF
mkdir -p "$(dirname "01-workstreams/content/README.md")"
cat > "01-workstreams/content/README.md" <<'FIXTURE_EOF'
# Content

My LinkedIn posts and the monthly newsletter.

| Folder | Holds |
|---|---|
| `01-knowledge/` | what governs my writing |
| `02-artifacts/` | the posts, drafts and published |
| `03-archive/` | what retired |
FIXTURE_EOF
mkdir -p "01-workstreams/content/01-knowledge" "01-workstreams/content/02-artifacts" "01-workstreams/content/03-archive"
mkdir -p "$(dirname "01-workstreams/sales/README.md")"
cat > "01-workstreams/sales/README.md" <<'FIXTURE_EOF'
# Sales

Outreach emails, follow-ups and the pipeline.

| Folder | Holds |
|---|---|
| `01-knowledge/` | what governs my outreach |
| `02-artifacts/` | sequences and templates |
| `03-archive/` | what retired |
FIXTURE_EOF
mkdir -p "01-workstreams/sales/01-knowledge" "01-workstreams/sales/02-artifacts" "01-workstreams/sales/03-archive"
mkdir -p "$(dirname "02-projects/pricing/map.md")"
cat > "02-projects/pricing/map.md" <<'FIXTURE_EOF'
# Pricing page, the map

- **What it produces**: the new pricing page
FIXTURE_EOF
