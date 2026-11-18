#!/bin/bash
set -e
mkdir -p "$(dirname "log.md")"
cat > "log.md" <<'FIXTURE_EOF'
# Log

What happened in this workspace, newest first, one line per event. The skill that made the change writes the line; a line is never rewritten.

    YYYY-MM-DD | [area] what changed -> path

## Entries
FIXTURE_EOF
mkdir -p "06-sources/raw"
touch "06-sources/raw/.gitkeep"
