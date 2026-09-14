# Credits

## pstack (cursor/plugins)

`INDEX.md`, `index.json` and the playbooks under `playbooks/` derive from **pstack**, published in
[cursor/plugins](https://github.com/cursor/plugins/tree/main/pstack) by **Lauren Tan**.

MIT licensed. The licence text is reproduced below as the licence requires.

What was borrowed:

- The 23 principle **names**, and the trigger text in `index.json`'s `trigger` field, taken from the
  `description:` line of each `principle-*/SKILL.md`.
- The step structure of the five ported playbooks: `bug-fix`, `runtime-forensics`, `hillclimb`,
  `babysit`, `shipping`.

What was changed:

- Rules, anchor mappings and the determination that a principle has no page in this library are this
  repository's own work.
- The playbooks are rewritten for Hermes primitives (`delegate_task`, `todo_list`, `terminal`,
  `browser_exec`, `gh`). Cursor-specific machinery is removed: `poteto-agent` subagents, `/loop`,
  the `control-ui` / `control-cli` skills from `cursor-team-kit`, the Origin forge, the `watch-pr`
  helper, and model-role routing. Where a step depended on something Hermes does not have, the step
  states the capability it needs instead of naming a tool.

Not ported: the remaining 18 playbooks, the 24 workflow skills, the model-role setup, and the `benny`
automation pack. See pstack upstream if you want them.

---

```
MIT License

Copyright (c) 2026 Lauren Tan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
