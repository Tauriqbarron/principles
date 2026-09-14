# Bug fix

> Ported from [pstack](https://github.com/cursor/plugins/tree/main/pstack) (MIT, Lauren Tan), rewritten
> for Hermes primitives. See `../CREDITS.md`.

**You own this task. Plan, review, verify.** Delegate the investigation and the fix, stay in the lead.

Be scientific. Every shipped line traces to runtime evidence. Belt-and-suspenders that "might help" is a
hypothesis, not a fix, and it does not ship. When evidence refutes a hypothesis, revert what it motivated.
The smallest change the evidence justifies ships, nothing more.

1. **Reproduce it yourself, on the matching surface.** Do not hand the repro to the user. Drive the real
   runtime: `terminal` for a CLI or service, `browser_exec` for the UI, the actual data path for a data
   bug. A protocol that says "ask the user to check" does not override this. Ask only when the surface is
   genuinely unreachable, and only after driving it as far as it goes. If it will not reproduce, force it:
   synthesise the trigger, tighten the conditions, instrument until it fires.
2. **Binary-search the cause.** Write the candidate hypotheses down, then eliminate until one survives.
   Delegate the archaeology reads (regression history, who calls this, what changed) to `delegate_task`
   subagents and keep the reduced finding in the main thread (`guard-the-context-window`). Each pass: take
   the split that cuts the most remaining problem space, get runtime evidence, eliminate. When program
   state is unclear, add instrumentation and read it as the code runs. Do not guess. Confirm the surviving
   **mechanism** with runtime evidence before you plan a fix. `systematic-debugging` is the long form of
   this step.
3. **Plan the fix.** If it crosses a function boundary, plan it against the library first
   (`principle-anchored-planning`). Implement with a tight, stated scope, either directly or through a
   coding subagent (`codex`, `claude-code`). Review the diff yourself rather than accepting a summary.
4. **Verify on the same surface.** The original repro now passes there. "Inconclusive" and "wrong surface"
   are not passes. Flag them. Unit tests show branch behaviour, not the absence of the bug
   (`prove-it-works`).
5. **Order the commits so the failing repro lands first.** See `test-driven-development` for the
   failing-test-first cadence when the bug has a cheap local test path; skip it when the test would be
   expensive, integration-heavy, or unclear. This is `sequence-verifiable-units`: the failing check first,
   the fix on top.
6. **Open the PR** through the `github` skill, and do not merge it without an explicit instruction
   containing "merge".

**Reply:** what was broken, the root cause, the fix, and how you verified it. Paste the failing-then-passing
repro output verbatim.
