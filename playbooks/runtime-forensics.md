# Runtime forensics

> Ported from [pstack](https://github.com/cursor/plugins/tree/main/pstack) (MIT, Lauren Tan), rewritten
> for Hermes primitives. See `../CREDITS.md`.

**You own the diagnosis. Instrument the live process, do not theorise from source.** The deliverable is a
cited diagnosis, not a fix.

1. **Capture the live signal on the matching surface.** A CPU profile for a spinning process, a heap
   snapshot for a leak, a CDP trace or screencast for a visual glitch, a packet or query log for a stall.
   A real artifact, not a guess. On this kind of work the capture command is usually the whole trick, so
   write the command in the reply even when it failed.
2. **Reduce the artifact to the smoking gun.** The function on the hot path, the retainer chain from the
   leaked object to a GC root, the loop firing without input, the request that never returns. Parse large
   artifacts inside a `delegate_task` subagent and give it file paths, not inlined payloads. Keep the
   reduced finding in the main thread (`guard-the-context-window`).
3. **Prove the mechanism before believing it.** Cheapest first: instrument the running process (CDP eval
   through `browser_exec`, a debugger attach, a temporary counter), or hot-fix the live code without a
   reload. Confirm the hypothesis without editing source for real.
4. **Map the finding back to source:** file, symbol, and the line that allocates or schedules.
5. **Say what you did not establish.** An unexplained remainder is part of the diagnosis. Name it rather
   than rounding it off.

**Reply:** the signal captured and the command that captured it, the reduced finding, how you proved the
mechanism, the source location, and the artifact paths. No fix unless asked. Hand back to Bug fix or a
performance run once the cause is known.
