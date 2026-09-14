# Hillclimb

> Ported from [pstack](https://github.com/cursor/plugins/tree/main/pstack) (MIT, Lauren Tan), rewritten
> for Hermes primitives. See `../CREDITS.md`.

**You own the metric and the experiment's integrity. Supervise and review, delegate the attempts.** For
sustained, iterative improvement of one measurable thing against a target. A one-off fix is Bug fix. This
is the loop.

Core discipline: one change, one measurement, keep or revert. Never stack untested changes, and never claim
a win from code inspection (`prove-it-works`).

1. **Ground the workload before choosing the metric.** Name the workload dimensions that can actually move
   the result (data size, history, state, concurrency, cache temperature) and select the case that
   reproduces the user's complaint. If no case reproduces it, fix the repro instead of hillclimbing. Then
   fix one metric, the direction that counts as better, and a stop predicate that pairs a target with a
   floor on attempts, so an early lucky win cannot end the run. "At least 50% better than baseline and at
   least 10 iterations" is that shape. Use the user's numbers when he gives them, otherwise agree them
   before you start.
2. **Build the measurement harness, prove its sensitivity, then freeze it** (`build-the-lever`). Run
   contrasting realistic workloads and confirm the target case reproduces the symptom while the easier
   cases separate as expected. If the harness cannot tell them apart, fix the workload or the metric
   first. Once frozen, one repeatable command emits the metric, sampled enough to clear the noise (median
   of N, never a single run). Record the baseline, and a green run of the regression gate, before any
   change.
3. **Open the decision log.** A `decision.tsv`, gitignored, one row per attempt: id, hypothesis, change,
   before, after, delta, tests, verdict (kept or reverted), note. Read it before each attempt so you are
   not retrying something already disproved.
4. **Ground each hypothesis in the model from step 1** so it names a specific mechanism ("defer X off the
   boot path because it blocks first paint"), not "try memoising something".
5. **Loop, one hypothesis per iteration.**
   - Hand the change to a coding subagent (`codex`, `claude-code`) with a tight scope, or type it
     yourself. Either way you review the diff. With several independent hypotheses live, run them in
     separate worktrees (`separate-before-serializing-shared-state`).
   - Measure before and after with the frozen harness, and run the regression gate.
   - Accept only when the metric moves past noise and the gate stays green. Otherwise revert the change in
     full. A tweak that "might help" is not kept.
   - One commit per accepted change, staging only the files you touched (`git add <files>`, never `-A`).
     Log the row either way, kept or reverted.
   Each iteration ends in a check before the next begins (`sequence-verifiable-units`). For an unattended
   run, keep the loop alive with a background `terminal` process and `notify` rather than polling in the
   foreground.
6. **Push past the first plateau.** On a stall, or several rejects in a row, change category: combine
   near-misses, re-read the source, or try something more radical before concluding the hill is climbed.
   Correctness and simplicity outrank the number. Revert a win that breaks behaviour, and keep a
   simplification that holds the number (`laziness-protocol`).
7. **Stop when the predicate is met**, or when the remaining ideas are marginal and not worth their cost.
   Do not relax the predicate to meet it, and do not quit while cheap untried hypotheses remain. If you
   are stuck, surface it instead of spinning.
8. **Open a PR** with the accepted commits stacked in the order they landed.

**Reply:** the metric and target, baseline to final with the percent delta, iterations run (kept vs
reverted), each accepted change on one line, the `decision.tsv` path, and the best idea you would try next
if pushed further.
