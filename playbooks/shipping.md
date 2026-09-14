# Shipping

> Ported from [pstack](https://github.com/cursor/plugins/tree/main/pstack) (MIT, Lauren Tan), rewritten
> for Hermes primitives. See `../CREDITS.md`.

**You own what lands. Verify each PR independently, land only the verified run from the bottom, then keep
your hands off the queue.** This is the half after `babysit.md`.

**Hard gate:** never merge without an explicit instruction from the user containing "merge". A green
stack and a completed verification are not that instruction.

1. **Verify every PR independently.** One `delegate_task` subagent per PR, not batched, each exercising
   the real surface (the UI through `browser_exec` and the `dogfood` skill, the CLI through `terminal`,
   the API through a real request) against parent versus head. Each returns `PASS`, `PASS+NOTES` or
   `FAIL`, and posts that verdict as a comment on its own PR along with the exact command or step it ran.
   Safe means a verdict from an agent that did not write the code. CI green is not a verdict, and an
   approving bot review is not a verdict.
2. **Land only the contiguous verified run rooted at the bottom.** Walk up from the lowest unmerged PR and
   stop at the first one without a passing verdict, where both `PASS` and `PASS+NOTES` pass. A verified PR
   sitting above an unverified one is not landable. Report the ceiling as a PR number and say what breaks
   the chain.
3. **Re-check that each verdict still describes the patch.** Record in the verdict comment the head SHA,
   the base SHA, and the stable `git patch-id` of that PR's base-to-head diff. A rebase or base retarget
   rewrites SHAs and can silently invalidate a verdict without touching a check. Compare the recorded
   patch-id with the current one before landing. Re-verify when the patch changed; when it did not, keep
   the code verdict but re-run mergeability and CI at the current head. Never use matching commit messages
   or a green check from an older SHA as a substitute.
4. **Prepare only the bottom PR.** Fetch current trunk. If needed, rebase the lowest verified branch onto
   the exact trunk tip, push it, and retarget only that PR (`gh pr edit <pr> --base <trunk>`). Re-run step
   3 after the push. Do not retarget, arm, or merge descendants yet.
5. **Land one PR at a time.** With the explicit merge instruction, squash the bottom PR
   (`gh pr merge <pr> --squash`). If checks are still running and the user asked for merge-when-ready,
   arm only that PR (`gh pr merge <pr> --squash --auto`) and wait for it to merge before preparing the
   next one.
6. **Watch the current frontier until it merges or fails, and do not mutate the queue around it.** Use a
   background `terminal` process with `notify` calling
   `gh pr view <pr> --json state,mergedAt,mergeStateStatus,statusCheckRollup,autoMergeRequest`, and ignore
   `READY` until `mergedAt` is non-null or `state` is `MERGED`. Hard-fail only when `state` is `CLOSED`
   with no `mergedAt`, a required check concludes `FAILURE` or `CANCELLED` after auto-merge is no longer
   pending, or `mergeStateStatus` is `UNSTABLE` or `DIRTY` with no auto-merge pending. If the queue stalls,
   diagnose before mutating.
7. **Recompute after every merge.** Fetch trunk, confirm the merged SHA is present, drop the merged PR
   from the bottom-to-top list, and inspect the new bottom PR's base, head, checks and patch-id. A host may
   retarget a child automatically; do not assume it did. Repeat steps 3 through 6 for that one PR.
   Independent work stays outside this chain and ships on its own.
8. **Stop at the ceiling.** When the verified run has merged, report what landed, what the next unverified
   PR is, and what verifying it would take. Extending the run is a new pass through step 1.

**Reply:** the verified run and its ceiling, each PR's verdict and who produced it, what you armed and how
you confirmed it, and what landed.
