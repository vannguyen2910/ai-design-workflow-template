# GitHub, Sharing and Obsidian

Three optional guides for after you have started: GitHub basics, sharing your hub with others, and using Obsidian.

---

## GitHub Basics

This guide is for people who have never used GitHub. You do not need to read it to get started: option A in [`01-getting-started.md`](01-getting-started.md#get-the-folder) needs no account. Read it when you want to save your work to GitHub.

### Seven words

| Word | Meaning | Picture it as |
|---|---|---|
| **Git** | Software that records the history of changes of a folder | An "undo" button for a whole folder |
| **GitHub** | A website that stores folders that use Git | Google Drive, but it remembers every change |
| **Repository** (repo) | A folder stored on GitHub | A project folder |
| **Template** | A sample repo you create your own copy from | A sample file you "Save as" |
| **Clone** | Download a repo to your machine | Download the folder |
| **Commit** | Save a point of change, with a one-line note | A "Save" button with a message attached |
| **Push** | Send the saved points from your machine to GitHub | Sync your copy to the internet |

### What you need to do

You only do four things, all by clicking buttons in **GitHub Desktop**, no commands to type:

1. **Clone** your repo to your machine. Once.
2. Work in the folder as usual.
3. **Commit** when you finish a piece of work, with a one-line note.
4. **Push** so your copy goes to GitHub.

The detailed clicks are in the "Option B" part of [`01-getting-started.md`](01-getting-started.md#get-the-folder).

### Private or public?

| | Private | Public |
|---|---|---|
| Who sees it | Only you, and the people you invite | Anyone with the link, including search engines |
| Use it for | A full project: context, data sources, working files | Only a project you are allowed to share in full |
| Markdown shown on GitHub | Yes, for invited people | Yes, for everyone |

A simple rule: **the repo that holds your project stays Private.** Only create a separate Public repo, from a cleaned copy, when the whole project may be shared. See [`02-github-sharing-and-obsidian.md`](02-github-sharing-and-obsidian.md#share-your-hub).

### Common worries

| You worry | In reality |
|---|---|
| "If I click wrong I lose files" | Each commit is a point. You can always go back to an earlier version |
| "Can anyone see my work?" | In a Private repo only you can see it. Others see it only when you invite them or send the link |
| "I got a strange message" | Take a screenshot and ask whoever shared the template, or a colleague. Meanwhile you can keep working: Git does not stop you from editing files |
| "Everything is a mess" | Download a fresh ZIP, then copy the files you edited into the new folder |

### Do not commit

Do not save these in the repo, even a Private one:

- Passwords, API keys, tokens
- Users' personal data (names, emails, phone numbers, recordings with real names)
- Unpublished financial or strategic figures of the company
- Company files you are not allowed to take outside

A Private repo is still a place on the internet. If you are not sure, anonymise before saving.

---

## Share Your Hub

Your hub is private by default: it lives in the project folder on your machine, and nobody sees it unless you send it. This guide explains how to let others see it, from the least risky way to the most risky.

### Choose how to share

| You want | Way | The recipient needs |
|---|---|---|
| A stakeholder to read it, with nothing to install | **HTML report** (Option 1) or **PDF** (Option 2) | A browser |
| To send the whole folder to a colleague | **ZIP file** (Option 3) | Obsidian or VS Code to view it nicely |
| One person to view it directly on GitHub | **Invite to a Private repo** (Option 4) | A free GitHub account |
| Anyone with the link to view it | **Public repo** (Option 5), only when the project may be shared | Nothing |

**For real company work, use Option 1 or 2.**

### Option 1: HTML report

One self-contained HTML file with a menu, opened by double-clicking in a browser, and sendable by email.

1. **Build the report.** The easiest way: ask the AI tool that has the project folder open to run `python3 ../toolkit/tools/build-report.py`.
   - Running it yourself on Mac: right-click the project folder, choose **New Terminal at Folder**, then type the command above.
   - Running it yourself on Windows: open the project folder, click the address bar, type `cmd`, press Enter, then type the command above.
   - The machine needs Python 3. A Mac may ask you to install a set of tools the first time; Windows needs Python installed from [python.org](https://www.python.org).
2. **Open the file** `index.html` at the root of the project folder in a browser (double-click).
3. **Check before sending.** If there is a black bar at the top saying "sample content or blanks remain", the hub still has sample content or empty places. Fill them in or delete them, then rebuild.
4. **Send the file.** Copy `index.html` out and rename it so it is easy to recognise, for example `onboarding-redesign-report.html`. The recipient only needs a browser.

If you use GitHub, `index.html` is also **rebuilt automatically** after each push (the `Update index.html` workflow). You only need to download the repo, or choose **Fetch origin** and then **Pull** in GitHub Desktop, to get the latest copy, with no command to run.

The report contains only the hub, the decision log and the principles. It has no working files or AI drafts.

To send a compact package (images and prototype included, without exposing raw working files): run `python3 ../toolkit/tools/build-report.py --bundle folder-name --zip` and send the ZIP file. The recipient unzips it and double-clicks `index.html`.

### Option 2: PDF

1. Open the hub page you want to send: in the HTML report from Option 1, or in Obsidian or VS Code.
2. Print that page (`Cmd+P` on Mac, `Ctrl+P` on Windows) and choose **Save as PDF**.
3. Repeat for the main pages: Overview, Problem brief, Findings.
4. Send the PDF files, or attach them to the company wiki.

### Option 3: ZIP file

1. Compress the **whole project folder**, not only `insights/`, because the pages in the report link to `work/`, `standards/` and the working files.
2. Send the ZIP file. The recipient unzips it and opens the whole folder in Obsidian or VS Code.
3. Try opening it on another machine before you send it.

### Option 4: Invite one person to a Private repo

1. Open your repo on GitHub, choose **Settings**, then **Collaborators**.
2. Click **Add people** and enter that person's account name or email.
3. They get an invitation email. After they accept, they read the hub right on GitHub.

You can revoke access at any time on the same screen.

### Option 5: Public repo

GitHub shows Markdown directly, so no website needs building: the link to the repo is the hub.

Only do this when the **whole project folder** may be shared, for example the sample project, or a cleaned copy of real work. The report links to files across the project folder, so publishing only part of it would break those links.

1. Create a **new** repo on GitHub and choose **Public**. Do not switch the Private repo you are using to Public, because the old history stays in it.
2. Copy the cleaned project folder into the new repo.
3. Open the repo link in a **private window** to see exactly what others see.

### Before you share anything

- **Do not put up confidential company figures,** details of an unreleased product, users' personal data, or passwords. Check your company's policy first.
- **A public link can be forwarded** to anyone.
- **Your GitHub account name is part of the repo address.** Pick a name you are comfortable seeing there.
- **You are the one sharing and you are responsible** for the link and the content. Nobody posts for you.
- **Use anonymised or fake data** for anything public.

---

## Obsidian

This guide is **optional**. The hub works in any tool that can open a folder (see [`01-getting-started.md`](01-getting-started.md#set-up-your-project)). Obsidian is an extra choice for when you want to see the relationships between decisions, hypotheses and tests as a picture, and to have tables by type without running a script.

### Setup

1. Install Obsidian from [obsidian.md](https://obsidian.md) (free for personal use). You need version **1.9 or later** to use Bases.
2. Open Obsidian and choose **Open folder as vault**. (A vault is what Obsidian calls a folder that it manages.)
3. Choose **your project folder** (for example `onboarding-redesign`). Do not choose the workspace root folder.
4. Obsidian will create an extra `.obsidian/` folder in the project folder to store settings. You do not need to touch it.
5. Open **Settings**, choose **Core plugins**, and turn on **Bases** if it is not already on.

Obsidian may ask whether you want to turn on "community plugins". You do not need them.

### What you get

| Feature | Use it to | How |
|---|---|---|
| **Tables by type** | See every decision, hypothesis, test at once | Open `insights/traceability.base`, then switch between the tabs: Opportunities, Hypotheses, Decisions, Tests, Metrics |
| **Properties** | Link one item to another without typing a code | Open an item file, click the `tests` line, type `[[`, then choose a file from the list |
| **Backlinks** | See which items link to this one | Open the Backlinks pane in the right sidebar while an item is open |
| **Graph view** | See the whole network of relationships in one picture | `Cmd+G` (Mac) or `Ctrl+G` (Windows) |
| **Search** | Find by code or keyword | `Cmd+Shift+F` or `Ctrl+Shift+F`, for example `file:/^D\d+/ P8` (decision files only) |

### Make the graph readable

By default Graph view shows the working files too. To see only the hub:

1. In Graph view, open the **Filters** pane and type `path:insights` into the search box.
2. Open **Groups** and add one group per type, each in its own colour:
   - `file:/^O\d+/`
   - `file:/^H\d+/`
   - `file:/^D\d+/`
   - `file:/^T\d+/`
   - `file:/^M\d+/`
3. An item that stands alone, with no line connecting it, is an item that is not linked to any need. That is exactly a "warning" of the hub.

### Rules that keep it working

- **A value that links items is a code in double square brackets and quotes**, for example `"[[H1]]"`. If you enter it with Obsidian's Properties pane, the quotes are added automatically.
- **Declare in one direction only.** A decision says which hypothesis it tests; Obsidian shows the reverse direction in Backlinks by itself.
- **Keep the item file names as they are.** The file name is the item's code.
- **Anonymise before you put data in this folder.** Obsidian opens the `_raw-private/` and `_personal/` folders too.

### Limits

- **Links in Properties are only clickable in Obsidian.** On GitHub they show as plain text. To share with others, build the HTML report (see [`02-github-sharing-and-obsidian.md`](02-github-sharing-and-obsidian.md#share-your-hub)).
- **AI plugins in Obsidian can read the whole folder**, including `_raw-private/`. If you install a plugin like that, apply the same data rules as for an AI coding tool.
- **Bases is still new**, so the display may differ between Obsidian versions. If `traceability.base` shows an error, delete that file. The hub still works normally because the data lives in the item files.
