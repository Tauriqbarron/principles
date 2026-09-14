# Principles — Software Engineering Reference Library

> An open, community-driven reference library of software engineering principles as beautifully styled HTML pages.

## Overview

A curated collection of software engineering principles as self-contained, dark-themed HTML reference pages. Originally built for Hermes Agent, now open for anyone to use, contribute to, or fork.

## Files

| File | Contents |
|---|---|
| `software-principles.html` | General software engineering principles — DRY, KISS, YAGNI, separation of concerns, etc. |
| `solid-principles.html` | SOLID principles — Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion |
| `architecture-principles.html` | Architecture — monolith vs microservices, event-driven, CQRS, clean architecture, distributed systems |
| `database-principles.html` | Database design — normalisation, indexing, query optimisation, schema design |
| `api-design-principles.html` | API design — REST conventions, GraphQL schema-first, versioning, error handling, pagination, auth |
| `testing-principles.html` | Testing — test pyramid, unit/integration/E2E strategy, mocking philosophy, coverage pragmatism |
| `security-principles.html` | Security — defence in depth, OWASP Top 10 mindset, input validation, secrets management, secure defaults |
| `error-handling-principles.html` | Error handling — fail fast, propagation, custom types, circuit breakers, resilience |
| `git-workflow-principles.html` | Git workflow — commit conventions, branching strategy, PR etiquette, merge vs rebase |
| `naming-conventions.html` | Naming — consistency, domain naming, clarity, booleans, abbreviations |
| `refactoring-principles.html` | Refactoring — when to refactor, strangler fig, boy scout rule, technical debt |
| `code-review-principles.html` | Code review — what to review, giving feedback, author responsibilities, tone |
| `frontend-bible.html` | Frontend — documenting functions and types, atomic design layering (atoms to pages), tests, ternary and currying style |

Thirteen pages exist. If you add or remove one, update this table, the routing table below, and any count in prose in the same commit.

Non-page artifacts, none of which are citable anchors: `INDEX.md` (generated, do not hand-edit), `index.json` (its source), `playbooks/`, `CREDITS.md`, `scripts/`.

## Planned, not yet written

Earlier revisions of this file listed the pages below as if they existed. They do not, and nothing should cite them until they are written:

`cicd-principles.html`, `observability-principles.html`, `performance-principles.html`, `documentation-principles.html`, `accessibility-principles.html`, `internationalization-principles.html`, `logging-principles.html`

## How This Repository Is Used

1. **Manual reference** — Open any HTML file in a browser to browse the principles visually. No build step, no dependencies.
2. **AI coding assistants** — Any AI tool working on projects that reference these principles should read the relevant HTML file for context.
3. **Hermes Agent** — the `principle-anchored-review` skill anchors code, PR and plan critiques to these documents, citing the principle by name so a finding is traceable rather than opinion. `principle-anchored-planning` does the same for plans.
4. **Situation routing** — `INDEX.md` maps the situation you are in to the principle that governs it, and to the page and exact anchor to read. Start there when the question is "which principle applies?" rather than "which page covers this topic?".
5. **Playbooks** — `playbooks/` holds step-by-step workflows (bug fix, runtime forensics, hillclimb, babysit, shipping) that name the principles they lean on.

## Routing

| Task | Read |
|---|---|
| Reviewing code architecture | `software-principles.html`, `architecture-principles.html` |
| Checking class/interface design | `solid-principles.html` |
| Reviewing database schema | `database-principles.html` |
| Designing APIs | `api-design-principles.html` |
| Writing or reviewing tests | `testing-principles.html` |
| Security review | `security-principles.html` |
| Error handling review | `error-handling-principles.html` |
| Git workflow review | `git-workflow-principles.html` |
| Naming / code clarity | `naming-conventions.html` |
| Refactoring decisions | `refactoring-principles.html` |
| Code review | `code-review-principles.html` |
| Frontend / UI review | `frontend-bible.html` |
| Which principle applies to the situation I am in | `INDEX.md`, then the page and anchor it names |
| Executing a bug fix, babysitting a PR, landing a stack | `playbooks/`, then the pages its steps cite |
| All thirteen | Read all — they complement each other |

## Agent conduct

A code-craft library does not answer every question an agent at work has. These rules govern how the work is done, not how the code is shaped. They are named so they can be cited like any other principle, and this library has no page for them: say that the rule is agent conduct, rather than implying a citation.

| Principle | Rule |
|---|---|
| **prove-it-works** | Verify against the real artifact: run the feature, read the value, inspect the diff. Never a proxy, a self-report, or "it compiles". |
| **never-block-on-the-human** | On reversible work, proceed and present the result. Reserve confirmation for irreversible actions. |
| **guard-the-context-window** | Route bulk output to subagents and keep reduced findings in the main thread, never raw payloads. |
| **build-the-lever** | Build the tool that does the work or proves it, rather than doing bulk work by hand. The tool is the artifact a reviewer can rerun. |
| **encode-lessons-in-structure** | A rule written twice becomes a lint, flag, check or script, not more prose. |

The remaining agent-conduct principles, with their triggers, are in `INDEX.md`. They come from pstack; see `CREDITS.md`.

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Design Notes

- Changes here affect all projects that use Hermes `principle-anchored-review`.
- HTML files are self-contained (inline CSS, Google Fonts) — no build step needed.
- Style: dark theme (`#0a0a0f`), JetBrains Mono + Syne fonts, green (`#00e5a0`) for good patterns, red (`#ff4d6d`) for anti-patterns.
- `INDEX.md` is generated. Add or change a principle in `index.json`, then run `python scripts/build_index.py`, which fails if any anchor no longer matches its page.
