# Principles — Software Engineering Reference Library

> An open, community-driven reference library of software engineering principles as beautifully styled HTML pages.

## Overview

A curated collection of software engineering principles as self-contained, dark-themed HTML reference pages. Originally built for Hermes Agent, now open for anyone to use, contribute to, or fork.

## Files

| File | Contents |
|---|---|
| `software-principles.html` | General software engineering principles (DRY, KISS, YAGNI, separation of concerns, etc.) |
| `solid-principles.html` | SOLID principles — Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion |
| `database-principles.html` | Database design principles — normalization, indexing, query optimization, schema design |

## How This Repository Is Used

1. **Manual reference** — Open any HTML file in a browser to browse the principles visually. No build step, no dependencies.
2. **AI coding assistants** — Any AI tool working on projects that reference these principles should read the relevant HTML file for context.
3. **Hermes Agent** — The `principle-aware-planning` skill auto-enforces these principles when creating plans or architectures. The `principle-aware-issue-review` skill audits GitHub issues against them.

## Routing

| Task | Read |
|---|---|
| Reviewing code architecture | `software-principles.html` |
| Checking class/interface design | `solid-principles.html` |
| Reviewing database schema | `database-principles.html` |
| All three | Read all — they complement each other |

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Design Notes

- Changes here affect all projects that use `principle-aware` planning.
- HTML files are self-contained (inline CSS, Google Fonts) — no build step needed.
- Style: dark theme (`#0d1117`), JetBrains Mono + Syne fonts, green (`#00e5a0`) for good patterns, red (`#ff4d6d`) for anti-patterns.