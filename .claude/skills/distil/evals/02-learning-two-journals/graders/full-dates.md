---
type: regex
target: { source: file, path: "04-memory/MEMORY.md" }
pattern: '(?<!\d{4}-)\b\d{2}-\d{2}\b(?!-\d)'
match: not_contains
---
