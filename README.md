# Principles — Software Engineering Reference Library

> Beautifully styled HTML reference pages for software engineering principles. DRY, SOLID, KISS, YAGNI, database design, and more.

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen)

## What Is This?

A curated collection of software engineering principles presented as self-contained, dark-themed HTML pages. Each page is a visual reference guide — open it in any browser and you get a beautifully styled document with examples, anti-patterns, and best practices.

## Principles

| File | Topic |
|---|---|
| `software-principles.html` | DRY, KISS, YAGNI, Separation of Concerns, Law of Demeter, etc. |
| `solid-principles.html` | Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion |
| `database-principles.html` | Normalization, indexing, query optimization, schema design |

## Usage

### Manual
Just open any `.html` file in your browser. No build step, no dependencies.

### AI Coding Assistants
Any AI working on projects that follow these principles should read the relevant HTML file before planning or reviewing code.

### Hermes Agent
The `principle-anchored-review` skill audits code, PRs and plans against these documents, and `principle-anchored-planning` anchors plans to them. `INDEX.md` routes from the situation you are in to the principle and the exact anchor to read, and `playbooks/` holds the workflows that apply them step by step.

### Other agents
`AGENTS.md` is the machine-readable entry point. Point any agent at it, and at `INDEX.md` for situation-based routing.

## Provenance

`INDEX.md`, `index.json` and `playbooks/` derive from [pstack](https://github.com/cursor/plugins/tree/main/pstack) by Lauren Tan (MIT). See [CREDITS.md](CREDITS.md).

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT — see [LICENSE](LICENSE)