# Index

Route from the situation you are in to the principle that governs it, and to the page you can
open. Written for an agent with a task in hand, not for a reader browsing topics. `AGENTS.md`
routes by task type; this routes by what the work currently feels like.

Two kinds of row. Where `Read` names a page and an anchor, that exact heading or panel label
exists in that file: cite it verbatim, and open it before citing. Where it says no page, the
principle is agent conduct that this library does not cover as a topic page. Say that plainly
rather than implying a citation, the same rule `principle-anchored-review` applies to gaps.

| Situation | Principle | Rule | Read |
|---|---|---|---|
| after finishing a task, before declaring done | **prove-it-works** | Verify against the real artifact: run the feature, read the value, inspect the diff. Never a proxy, a self-report, or 'it compiles'. | no page. Closest: testing-principles.html: "Real DB — Preferred" |
| before writing logic: core types, data structures, ordering | **foundational-thinking** | Get the core types and data structures right before the logic. Downstream code should then be obvious. | no page. Agent conduct, argued from this index. |
| code that is hard to trace, or shaping code for a reader | **minimize-reader-load** | Count the layers between question and answer, and the hidden state in a reader's head. Collapse one-caller wrappers and shrink mutable scope. | "Clarity Is More Important Than Brevity" in `naming-conventions.html` |
| concurrent actors writing the same file, branch or key | **separate-before-serializing-shared-state** | Eliminate the sharing first. Serialize only when one shared writer is a real invariant rather than a convenience. | no page. Agent conduct, argued from this index. |
| context filling up with large outputs or repeated reads | **guard-the-context-window** | Route bulk to subagents and keep reduced findings in the main thread, never raw payloads. | no page. Agent conduct, argued from this index. |
| debugging a symptom | **fix-root-causes** | Trace each symptom to its root cause and fix it there. Reproduce first, and resist the nil-check guard that only silences the crash. | no page. Closest: error-handling-principles.html: "Errors Should Gain Context as They Bubble Up" |
| designing commands or loops that run amid crashes and retries | **make-operations-idempotent** | Commands, lifecycle steps and loops converge to the same end state regardless of partial prior runs. | no page. Closest: database-principles.html: "After — Explicit Transaction" |
| designing types or reviewing a signature in a typed language | **type-system-discipline** | Make illegal states unrepresentable, brand semantic primitives, parse external data at boundaries, exhaust variants, and never lie to the compiler. | "Errors Are Types — Give Them Structure" in `error-handling-principles.html` |
| integrating a new requirement into an existing design | **redesign-from-first-principles** | Redesign as if the new requirement had been a day-one assumption, instead of bolting it onto the current shape. | "Start Simple — The Monolith Is Not a Mistake" in `architecture-principles.html` |
| introducing a new internal API while old callers exist | **migrate-callers-then-delete-legacy-apis** | Migrate the callers and delete the old API in the same wave. Do not keep a compatibility layer alive. | "Strangler fig — Preferred" in `refactoring-principles.html` |
| multi-step work, and how commits or PRs are stacked | **sequence-verifiable-units** | Break work into small units that each end in a verifiable state, check each before the next, and order delivery so the sequence proves itself to a reviewer. | "Atomic commits — Preferred" in `git-workflow-principles.html` |
| non-trivial or bulk work: edits, migrations, checks | **build-the-lever** | Build the tool that does the work or proves it, rather than doing bulk work by hand. The tool is the artifact a reviewer can rerun. | no page. Agent conduct, argued from this index. |
| novel UI or architecture decision with no precedent | **exhaust-the-design-space** | With no precedent in the codebase, build two or three competing prototypes and compare them side by side before committing. | no page. Agent conduct, argued from this index. |
| planned rewrites with explicit phase boundaries | **outcome-oriented-execution** | Converge on the target architecture. Do not spend effort preserving a smooth intermediate state. | "Outcome test — Preferred" in `testing-principles.html` |
| product, UX or feature-scope tradeoffs | **experience-first** | Choose user delight over implementation convenience. Fewer polished features beat more rough ones. | no page. Agent conduct, argued from this index. |
| refactoring, sizing a diff, tempted to add a layer | **laziness-protocol** | Bias to deletion, and to the smallest change that solves the problem. If a maintainer would find it exhausting, it is the wrong solution. | "DRY · YAGNI · KISS" in `software-principles.html` |
| sequencing an addition, refactor or rewrite | **subtract-before-you-add** | Remove dead code, redundant validators and stub references first, then build on the simpler base. | "Leave the Code Cleaner Than You Found It" in `refactoring-principles.html` |
| stateful logic, heavy branching, a shape repeated across files | **model-the-domain** | Encode the domain in a structure instead of repeating a shape assumption as scattered conditionals. | "Name for the Domain — Not the Implementation" in `naming-conventions.html` |
| tempted to ask 'should I do X?' on reversible work | **never-block-on-the-human** | On reversible work, proceed and present the result. Reserve confirmation for irreversible actions. | no page. Agent conduct, argued from this index. |
| two fixes sharing one premise failed the same gate | **attack-the-premise** | When two fixes sharing one premise fail the same gate, census which actors hold the imbalance and question the premise instead of writing a third fix that assumes it. | no page. Closest: code-review-principles.html: "Review the Intent, Not Just the Implementation" |
| wiring validation, error handling or a framework adapter | **boundary-discipline** | Concentrate guards at system boundaries (CLI, config, network, external APIs). Trust internal types and keep business logic in pure functions. | "Detect Errors at the Boundary — Not Deep in the Logic" in `error-handling-principles.html` |
| writing the same instruction a second time | **encode-lessons-in-structure** | A rule written twice becomes a lint, flag, check or script, not more prose. | no page. Agent conduct, argued from this index. |
| writing, changing or keeping a test | **test-behavior-not-implementation** | Call the code the way its users do and assert the observed result against a literal. If it passes when every import returns undefined, rewrite or delete it. | "Behaviour-based — Preferred" in `testing-principles.html` |

Source of truth: `index.json`. Regenerate this file with `python scripts/build_index.py`,
which fails if any anchor above stops matching its page. Add a principle by adding a row there,
never by editing this file.

## Provenance

The 23 principle names, and the trigger phrasing behind the Situation column, come from
[pstack](https://github.com/cursor/plugins/tree/main/pstack) by Lauren Tan, MIT licensed. The rules, the anchor mapping and the
no-page determinations are this repository's own. See `CREDITS.md`.

## Playbooks

The workflows that apply these principles step by step live in `playbooks/`: bug fix, runtime
forensics, hillclimb, babysit and shipping. They are ports of pstack's playbooks onto Hermes
primitives, and each one names the principles it leans on.
