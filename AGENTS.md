# Principles — Software Engineering Reference Library

> An open, community-driven reference library of software engineering principles as beautifully styled HTML pages.

## Overview

A curated collection of software engineering principles as self-contained, dark-themed HTML reference pages. Originally built for Hermes Agent, now open for anyone to use, contribute to, or fork.

## Files

| File | Contents |
|---|---|
| `software-principles.html` | General software engineering principles — DRY, KISS, YAGNI, separation of concerns, etc. |
| `solid-principles.html` | SOLID principles — Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion |
| `database-principles.html` | Database design — normalisation, indexing, query optimisation, schema design |
| `api-design-principles.html` | API design — REST conventions, GraphQL schema-first, versioning, error handling, pagination, auth |
| `testing-principles.html` | Testing — test pyramid, unit/integration/E2E strategy, mocking philosophy, coverage pragmatism |
| `security-principles.html` | Security — defence in depth, OWASP Top 10 mindset, input validation, secrets management, secure defaults |
| `cicd-principles.html` | CI/CD — pipeline design, build, test, deploy, monitor |
| `observability-principles.html` | Observability — metrics, logs, traces, SLOs, alerting |
| `performance-principles.html` | Performance — measurement, optimisation strategies, caching, database, frontend |
| `documentation-principles.html` | Documentation — types, clarity, maintenance, examples |
| `accessibility-principles.html` | Accessibility — semantic HTML, keyboard navigation, ARIA, colour contrast, screen readers |
| `internationalization-principles.html` | Internationalisation — locale awareness, text encoding, RTL support, date/time, pluralisation |
| `error-handling-principles.html` | Error handling — fail fast, propagation, custom types, circuit breakers, resilience |
| `logging-principles.html` | Logging — log levels, structured logging, security, correlation, retention |
| `architecture-principles.html` | Architecture — monolith vs microservices, event-driven, CQRS, clean architecture, distributed systems |
| `git-workflow-principles.html` | Git workflow — commit conventions, branching strategy, PR etiquette, merge vs rebase |
| `naming-conventions.html` | Naming — consistency, domain naming, clarity, booleans, abbreviations |
| `refactoring-principles.html` | Refactoring — when to refactor, strangler fig, boy scout rule, technical debt |
| `code-review-principles.html` | Code review — what to review, giving feedback, author responsibilities, tone |

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
| Designing APIs | `api-design-principles.html` |
| Writing or reviewing tests | `testing-principles.html` |
| Security review | `security-principles.html` |
| CI/CD pipeline review | `cicd-principles.html` |
| Observability review | `observability-principles.html` |
| Performance review | `performance-principles.html` |
| Documentation review | `documentation-principles.html` |
| Accessibility review | `accessibility-principles.html` |
| Internationalisation review | `internationalization-principles.html` |
| Error handling review | `error-handling-principles.html` |
| Logging review | `logging-principles.html` |
| Architecture design | `architecture-principles.html` |
| Git workflow review | `git-workflow-principles.html` |
| Naming / code clarity | `naming-conventions.html` |
| Refactoring decisions | `refactoring-principles.html` |
| Code review | `code-review-principles.html` |
| All nineteen | Read all — they complement each other |

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Design Notes

- Changes here affect all projects that use `principle-aware` planning.
- HTML files are self-contained (inline CSS, Google Fonts) — no build step needed.
- Style: dark theme (`#0a0a0f`), JetBrains Mono + Syne fonts, green (`#00e5a0`) for good patterns, red (`#ff4d6d`) for anti-patterns.
