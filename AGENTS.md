# Principles — Software Engineering Reference Library

## Overview
A curated collection of software engineering principles as beautifully styled HTML reference pages. This repository is consumed by other projects via the `principle-aware-planning` and `principle-aware-issue-review` Hermes skills.

## Files

| File | Contents |
|---|---|
| `software-principles.html` | General software engineering principles (DRY, KISS, YAGNI, separation of concerns, etc.) |
| `solid-principles.html` | SOLID principles — Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion |
| `database-principles.html` | Database design principles — normalization, indexing, query optimization, schema design |

## How This Repository Is Used

1. **Hermes Agent** — The `principle-aware-planning` skill auto-enforces these principles when creating plans or architectures for any project. The `principle-aware-issue-review` skill audits GitHub issues against them.
2. **Manual reference** — Open any HTML file in a browser to browse the principles visually.
3. **AI coding assistants** — Any AI tool working on projects that reference these principles should read the relevant HTML file for context.

## Routing

| Task | Read |
|---|---|
| Reviewing code architecture | `software-principles.html` |
| Checking class/interface design | `solid-principles.html` |
| Reviewing database schema | `database-principles.html` |
| All three | Read all — they complement each other |

## Important Notes
- Changes here affect **all projects** that use principle-aware planning.
- The HTML files are self-contained (inline CSS, Google Fonts) — no build step needed.
- Style: dark theme, JetBrains Mono + Syne fonts, green (#00e5a0) for good patterns, red (#ff4d6d) for anti-patterns.
