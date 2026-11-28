# AGENTS.md

This is the **workspace root**: it holds several projects (one folder each in `project/`) and the shared `agents/`, `rules/`, `skills/` and `toolkit/`. Rules for working *inside* a project are in that project's own `AGENTS.md` (for example `project/travel-app/AGENTS.md`). When you work inside a project, read that file, not this one.

## Structure

| Path | What it is | What you do |
|---|---|---|
| `project/` | Every project, one folder each | Work inside the project the owner names |
| `project/travel-app/` | The sample project (Travel Buddy) | Read for reference, do not edit unless asked |
| `project/<name>/` | The owner's project | Follow that project's `AGENTS.md` |
| `agents/` | Read-only helpers: user researcher, UI designer, handoff reader, design QA reviewer | Read, do not edit unless asked |
| `rules/` | Rules every project's AI tool follows | Read, do not edit unless asked |
| `skills/` | Step cards (`SKILL.md`), templates, examples | Read, do not edit unless asked |
| `toolkit/` | Guides and scripts; `toolkit/project-template/` is the blank project that `new-project.py` copies | Read, do not edit unless asked |
| `index.html` | Home page, one card per project | Never edit by hand; build it (see Commands) |

## Commands

Run from the workspace root unless noted.

```bash
python3 toolkit/tools/new-project.py "<Project name>"   # create a project (add --title "…" for a different display name)
python3 toolkit/tools/build-home.py                     # rebuild the home page
python3 toolkit/tools/check-toolkit.py                  # check skills and paths
cd project/<name> && python3 ../../toolkit/tools/build-report.py   # rebuild one project's report, inside the project folder
```

## Creating a new project

Triggers: "Create a new project called …", "Tạo một dự án mới tên …", "Start the project …".

1. Ask for the project name if it is not given. One question is enough.
2. Run `new-project.py`. Do not copy a folder yourself. It turns the name into a folder name, removes the `[EXAMPLE]` items, fills in the project name, builds the project's `index.html` and adds a home page card.
3. Tell the owner: the path of the new folder, that the home page has a card for it, and the first step: fill in the Project card in the project's `README.md` (the **Overview** line is the card's introduction), then `context/product-and-users.md` and `context/data-rules.md`.
4. Do not fill it in for them. Do not invent the product name, users or figures; leave unknowns empty.

If the folder name already exists, the command stops. Do not delete or overwrite it; ask the owner for another name.

## Other requests

| Request | What to do |
|---|---|
| See a project's report | Open `project/<name>/index.html` |
| Add a document to a project | Copy a template from `skills/<skill>/templates/` into that project's `work/`, then follow that project's `AGENTS.md` |
| Draw a process map, swimlane or user flow | Follow `skills/build-process-map/SKILL.md` (uses `skills/diagram-design/`); template: `skills/build-process-map/templates/process-map.md` |
| "Lưu lại", "Lưu và đăng lên", "Save and publish" | Ask which project, then follow **Save and publish** in that project's `AGENTS.md`. Changes to the workspace itself (for example `toolkit/`) follow the same steps, staging only the files that changed |
| Unclear which project | Ask one question; do not guess |

## Boundaries

**Never**
- Read `_personal/` or `work/sources/_raw-private/` of any project.
- Edit `toolkit/project-template/`; it must stay as the template.
- Use real names of people, companies or real figures before they are anonymised.

**Ask first**
- Anything that creates or changes many files: propose it and wait for the owner's approval.

## Style

- Answer in the language the owner writes in.
- Write plain, clean content. In the body of a document leave out item codes (O1, H2, D3), counts such as `(n=13)`, file paths and skill names; say it in words and keep the codes in the file's properties. Full rule: `rules/ai-rules.md`.
