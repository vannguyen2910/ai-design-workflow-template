# Agents

Small, read-only helpers that work in their own context and return a report. A **skill** (in `../skills/`) is a procedure with steps, some of them yours. An **agent** is for a second opinion or a fresh pair of eyes: it reads, checks, and hands back a draft or a list. The owner or the main session decides what to write into the project.

| Agent | Use it when | Reads |
|---|---|---|
| [`user-researcher`](user-researcher.md) | You plan research, synthesise anonymised interviews or quotes, or want counterexamples to an insight | `context/`, `work/sources/anonymised/` |
| [`handoff-reader`](handoff-reader.md) | The design is ready for developers and you want to know what they would still have to ask | `work/handoff.md`, `work/measurement-plan.md`, what they link to |
| [`design-qa-reviewer`](design-qa-reviewer.md) | A prototype or build can be opened and you want differences, missing states and accessibility measured and rated | The design files, `context/`, the prototype in a browser |

All three:

- follow `../rules/ai-rules.md`, and the product and design rules in this folder's sibling `../rules/`;
- never read `_personal/` or `work/sources/_raw-private/`;
- never edit a file, so the hard rules about drafts and "(verified)" sections stay true.

## Using them in Claude Code

Claude Code looks for agents in `.claude/agents/`. Link them once from the workspace root:

```bash
mkdir -p .claude/agents && ln -s ../../toolkit/agents/user-researcher.md ../../toolkit/agents/handoff-reader.md ../../toolkit/agents/design-qa-reviewer.md .claude/agents/
```

Then ask: *"Use the handoff-reader agent on this project."* In another AI tool, paste the agent's file as the instruction.

## Add your own

One Markdown file per agent, with `name`, a one-sentence `description` that says when to use it, and `tools` (give only what it needs; read-only by default). Say what it reads, what it checks, and exactly what it returns.
