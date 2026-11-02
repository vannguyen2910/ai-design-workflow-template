# Toolkit

Everything shared by the projects in this workspace. The home page that lists every project is the `index.html` at the workspace root. **You do not fill anything in here.** Each project (`demo-project`, your own) sits outside this folder.

| Folder | What it holds | When to open it |
|---|---|---|
| `guides/` | Three guides: getting started (setup checklist, get the folder, set up a project: start here), GitHub, sharing and Obsidian, and how the hub works | The first time, or when you are stuck |
| `templates/` | The one template no skill uses (`generic.md`). The other templates sit inside each skill | When you start a new document |
| `rules/` | `ai-rules.md`: the hard rules and writing rules shared by every project's `AGENTS.md` | Before you change how the AI tool should behave |
| `skills/` | One folder per skill: the steps for the AI tool (`SKILL.md`), its templates and examples. Includes the `diagram-design` skill the AI tool uses to draw process maps, user flows and other diagrams | Rarely: the AI tool reads them itself |
| `tools/` | The scripts: `new-project.py` (create a project with one command), `build-report.py` and `build-home.py` (build the `index.html` pages), `new-item.py`, `serve-hub.py`, `flow-from-mermaid.py` | When you want a new project; the AI tool runs the others |

Create a new project (from the workspace root):

```
python3 toolkit/tools/new-project.py project-name
```

Details: [`guides/01-getting-started.md`](guides/01-getting-started.md#set-up-your-project).
