---
type: regex
target: { source: file, path: "log.md" }
pattern: '## Entries\s+(?!2026-11-10)\d{4}-\d{2}-\d{2} \| \[[a-z0-9-]+\] [^\n]+ -> \S+\n+2026-11-10'
---
