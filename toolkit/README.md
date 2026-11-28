# Toolkit

Everything shared by the projects in this workspace. The home page that lists every project is the `index.html` at the workspace root. **You do not fill anything in here.** The agents, rules and skills are in their own folders at the workspace root (`agents/`, `rules/`, `skills/`), and each project (`travel-app`, your own) is in `project/`.

| Folder | What it holds | When to open it |
|---|---|---|
| `guides/` | Three guides: getting started (setup checklist, get the folder, set up a project: start here), GitHub, sharing and Obsidian, and how the hub works | The first time, or when you are stuck |
| `tools/` | The scripts: `new-project.py` (create a project with one command), `build-report.py` and `build-home.py` (build the `index.html` pages), `new-item.py`, `serve-hub.py`, `flow-from-mermaid.py` | When you want a new project; the AI tool runs the others |

Create a new project (from the workspace root):

```
python3 toolkit/tools/new-project.py project-name
```

Details: [`guides/01-getting-started.md`](guides/01-getting-started.md#set-up-your-project).
