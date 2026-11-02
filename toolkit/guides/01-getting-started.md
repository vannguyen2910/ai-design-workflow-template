# Getting Started

Everything for the first session, in order: the setup checklist, getting the folder onto your machine, and setting up your first project.

---

## Setup Checklist (Session 0)

Do this **before the first session**, on your own, in about 45 minutes. Each step ends with a **Done when** line: check it on your screen before you move on. If a step does not match what you see, stop there and send a screenshot with the step number. Do not skip ahead.

You do not need to know Git. You click buttons once to set things up, then the AI tool saves your work for you (step 9).

**What you need:** a Mac or Windows computer, an internet connection, and the AI coding tool the programme uses.

---

### 1. Create a GitHub account

1. Go to [github.com](https://github.com) and click **Sign up**. The free plan is enough.
2. Confirm your email.

**Done when:** you are signed in on github.com and see your profile picture at the top right.

### 2. Install GitHub Desktop

1. Download it from [desktop.github.com](https://desktop.github.com). It is **not** in the App Store.
2. Mac: if the page asks which version, check your chip first: Apple menu → **About This Mac**. "Chip: Apple M…" means **Apple silicon**; "Processor: Intel…" means **Intel**.
3. Open the app and sign in with the GitHub account from step 1.

**Done when:** GitHub Desktop opens, and **Settings → Accounts** (Windows: **File → Options → Accounts**) shows your GitHub name.

### 3. Install your AI coding tool

1. Install the AI coding tool the programme uses and sign in.
2. Find the menu item that opens a folder (usually **File → Open Folder**). You will use it in step 6.

**Done when:** the tool opens and you know where **Open Folder** is.

### 4. Create your own repo from the template

1. Open the template link you received.
2. Click the green **Use this template** button → **Create a new repository**.
3. Name it, for example `my-design-workflow`, and choose **Private**.
4. Click **Create repository**.

**Done when:** your browser shows `github.com/<your-name>/<repo-name>`, the folders `demo-project` and `toolkit` are listed, and the word **Private** is next to the repo name.

No **Use this template** button? Message the person who shared the link. Do not download the original repo instead.

### 5. Bring the repo to your machine (clone)

1. In GitHub Desktop: **File → Clone repository**.
2. On the **GitHub.com** tab, choose the repo from step 4.
3. In **Local path**, choose `Documents`. **Not** Google Drive, iCloud, OneDrive or Dropbox: a syncing folder can break files while the AI writes them.
4. Click **Clone**.

**Done when:** `Documents/<repo-name>` exists, and inside it you see `README.md`, `toolkit` and `demo-project`.

### 6. Open the workspace in your AI tool

1. In the AI tool: **File → Open Folder**, then choose `Documents/<repo-name>` (the whole workspace, not a project folder).

**Done when:** the file list in the AI tool shows `AGENTS.md`, `toolkit` and `demo-project`.

### 7. Create your project

1. In the AI tool's chat, type: *"Tạo một dự án mới tên …"* (or *"Create a new project called …"*), with your project name.
2. Mac only: if a window asks to install "command line developer tools", click **Install**, wait, then ask again.

**Done when:** a new folder with your project name appears next to `demo-project`, and the AI tells you the path of the new folder.

### 8. Open the report

1. Double-click `index.html` at the workspace root.
2. Click the card of your project.

**Done when:** your browser shows a card with your project name, and clicking it opens the **Overview** of your project.

### 9. Save and publish your work

1. In the AI tool: **File → Open Folder**, then choose **your project folder** (from step 7). From now on you always open the project folder, not the workspace.
2. In the chat, type: *"Lưu và đăng lên"* (or *"Save and publish"*).
3. The AI lists the files it will save and sends them to GitHub.

**Done when:** on github.com your repo shows your project folder, and GitHub Desktop says **No local changes**.

Two phrases are all you need from now on:

| You say | The AI does |
|---|---|
| *"Lưu lại"* / *"Save"* | Saves a checkpoint on your machine (a commit), with a one-line note |
| *"Lưu và đăng lên"* / *"Save and publish"* | Saves a checkpoint and sends it to GitHub (commit and push) |

---

### When something goes wrong

| You see | Do this |
|---|---|
| GitHub Desktop is not in the App Store | That is normal: download it from desktop.github.com (step 2) |
| The repo is in Google Drive or iCloud | In GitHub Desktop: **Repository → Remove**, then clone again into `Documents` (step 5) |
| The AI cannot find `new-project.py` | You opened a project folder instead of the workspace. Open the workspace folder (step 6) |
| A page opens but tables and links look raw | You opened a `.md` file. Open `index.html` instead (step 8) |
| "Push" or "authentication" error | Open GitHub Desktop, check you are signed in (step 2), then say *"Lưu và đăng lên"* again |
| Anything else | Screenshot + the step number, sent to the person running the programme |

### Not in Session 0

Branches, pull requests and a public link (GitHub Pages) come later, when you have work to share. See [`02-github-sharing-and-obsidian.md`](02-github-sharing-and-obsidian.md#github-basics) and [`02-github-sharing-and-obsidian.md`](02-github-sharing-and-obsidian.md#share-your-hub).

---

## Get the Folder

Setting up for the first time? The [setup checklist](01-getting-started.md#setup-checklist-session-0) walks you through everything in order, with a check after each step. This guide explains the options in more detail.

This guide helps you get the workspace onto your machine. There are two ways, and you only need to pick one.

**Never used GitHub? Pick option A.** You can use this workspace without an account.

| | Way | GitHub account needed | Backed up | Good when |
|---|---|---|---|---|
| A | Download ZIP | No | No, you back it up yourself | You want to start right away |
| B | Use this template, then GitHub Desktop | Yes (free) | Yes, with change history | You want an automatic backup |

### Where to keep it

Put the folder somewhere ordinary on your machine, for example `Documents`.

**Do not put it in Google Drive, iCloud, OneDrive or Dropbox.** An AI coding tool writes many files at once, and a folder that syncs to the cloud can break halfway. If you want a backup, use option B.

### Option A: Download ZIP

1. Open the GitHub page of the repo (the link comes from whoever shared the template).
2. Click the green **Code** button, then choose **Download ZIP**.
3. Unzip the file you just downloaded:
   - Mac: double-click the file.
   - Windows: right-click, choose **Extract All**.
4. Drag the unzipped folder into `Documents`.
5. Open the folder. You will see `README.md`, `toolkit` and `demo-project`.

**Backup:** from time to time, compress your project folder into a ZIP file and put it away, or copy it to another drive. The end of each work session is a good moment.

### Option B: Use this template, then GitHub Desktop

This creates your own **repo** (a repo is a folder stored on GitHub). You keep it **Private**, so only you can see it.

#### Part 1: Create your repo

1. Go to [github.com](https://github.com) and sign in. No account yet? Click **Sign up** (free).
2. Open the GitHub page of the repo that the template's sharer sent.
3. Click the green **Use this template** button, then choose **Create a new repository**.
4. In the **Repository name** box, enter a name, for example `my-design-workflow`.
5. Choose **Private**.
6. Click **Create repository**.

Cannot see the **Use this template** button? Use option A, or message the person who shared the template.

> **Do not download the original repo directly to save your work.** You have no write access to it, so your changes cannot be saved there. Create your own repo with **Use this template** first.

#### Part 2: Bring the repo to your machine

1. Install **GitHub Desktop** from [desktop.github.com](https://desktop.github.com) and sign in with your GitHub account.
2. Choose **File**, then **Clone repository**. (Clone means download a repo to your machine.)
3. On the **GitHub.com** tab, choose the repo you just created.
4. In the **Local path** box, choose `Documents`.
5. Click **Clone**.
6. Choose **Repository**, then **Show in Finder** (Mac) or **Show in Explorer** (Windows) to open the folder.

#### Part 3: Save your work

Do this after each time you finish a piece of work:

1. Open GitHub Desktop. The left column lists the files you changed.
2. At the bottom left, type a one-line summary, for example `Discover: scope and user-voice synthesis`.
3. Click **Commit to main**. (A commit saves a point of change, with a message. `main` is the main branch, just leave it as it is.)
4. Click **Push origin** in the top bar. (Push sends those points to GitHub.)

These four actions are everything you need to know about Git. The words you just met are explained further in [`02-github-sharing-and-obsidian.md`](02-github-sharing-and-obsidian.md#github-basics).

### Check before you start

- [ ] The folder is in `Documents`, not in a folder that syncs to the cloud.
- [ ] You can see `toolkit` and `demo-project` in the folder.
- [ ] You can open `demo-project/README.md` and read it.

Opens, but tables and links look raw? That is normal: Markdown files need a viewer. See "View markdown files" in [`01-getting-started.md`](01-getting-started.md#set-up-your-project).

---

## Set Up Your Project

This guide helps you name your project, understand what each folder is for, and know how to work with an AI tool in this folder.

### Step 1: Name your project

1. Open Terminal at the workspace root folder and run:

   ```
   python3 toolkit/tools/new-project.py onboarding-redesign
   ```

   Add `--title "Onboarding redesign"` if you want a display name that differs from the folder name.
2. A folder name uses lowercase letters joined with hyphens, no spaces. For example: `onboarding-redesign`, `checkout-flow`. Pick a name that tells you what the project is about, because you will see it at the start of every path. A plain name such as "Trip Planner" also works: the command turns it into a folder name.
3. The command creates a new folder next to `demo-project`, clean and ready to fill in.

If you have two projects, run the command twice with two different names.

**Cannot use Terminal?** Ask the AI tool to run it for you: say *"Create a new project called … ."*

### Step 2: Understand the folders

Folders are named after **what you do** there:

| Folder | Use it for | When |
|---|---|---|
| `context/` | **Background:** product, users, data rules, design system. You give it to the AI to read first in every step | When you start the project, add to it over time |
| `work/` | **The working files of each stage:** `scope.md`, `user-voice-synthesis.md`, `competitor-analysis.md` (Discover), `problem-brief.md` (Define), `options.md`, `alignment.md` (Develop), `test-plan.md`, `findings.md`, `handoff.md`, `measurement-plan.md` (Deliver). The stage pages in `stages/` are built from these files | Throughout the project |
| `work/sources/` | `anonymised/` holds anonymised data, `_raw-private/` holds original data | Discover |
| `work/prototype/` | Prototype code. Created when you start building, by copying `toolkit/skills/prototype/starter/` | The Develop stage |
| `stages/` | **One page per stage**, built from `work/` and `insights/` by the Pages table in `stages/README.md`; you do not write here | Edit the table only to change the order or add a stage |
| `insights/` | **The linked items:** needs, hypotheses, decisions, evidence, findings, metrics; one file per item, in the folder of its type | Update when something changes |
| `standards/` | **Reference:** gates, principle checks, severity levels, project log. Drop a new `.md` file here and it shows in the report by itself | When you need to look something up |
| `../toolkit/skills/` and `../toolkit/tools/` | (in `toolkit/`, outside the project) The skills (step cards with their templates and examples), the scripts that build the `index.html` report, and the templates no skill uses. Shared by every project | When you run a step; rarely opened by hand |
| `_personal/` | Private notes, not given to the AI | Whenever you want |

The `README.md` at the root of the project folder has a "What do you want to do?" table with sample sentences for each job, so when you do not know where to start, read it.

### Step 3: Fill in the first files

When you start the project, fill in the files in `context/` and one separate file:

1. `context/product-and-users.md`: what the product is, who the users are, what you know and what you do not.
2. `context/accessibility-rules.md`: the accessibility requirements the design must meet.
3. `context/data-rules.md`: three lines in your own words: what you may give the AI, what you will not, which tool you use for what.
4. `context/open-questions.md`: the questions the AI says it needs answered.
5. `_personal/my-direction.md`: two or three lines about the career direction you lean toward. This is a private note, so it sits outside the working folders and is not given to the AI.

Each file comes with hint lines. Replace the hints with your own content, and keep the headings as they are.

### Step 4: Work with an AI tool

This folder is built so an AI tool knows what to do by itself, thanks to four things:

| Thing | What it is |
|---|---|
| `AGENTS.md` | A file with the "rules of the game" already written. The AI tool reads it by itself when you open the folder, so you do not have to repeat the rules every time. If your tool reads its rules file under another name, copy the content to that name |
| `../toolkit/skills/*/SKILL.md` | The **step cards**: each step says who does it (the AI or you), which files to read, where to write |
| `work/sources/` | The AI may read `anonymised/`. `_raw-private/` is never given to the AI and never goes to GitHub |
| `insights/` | Each decision, hypothesis and evidence is one file. The summary tables are rebuilt by the AI |

A session with the AI looks like this:

1. **Open exactly one project folder** as the project in the AI tool. Do not open the root folder, and do not open two projects at the same time, or the data of the two projects will mix.
2. **Save a checkpoint before the AI writes files.** If your folder is on GitHub, say "Lưu lại" (or "Save") to the AI tool, or click Commit in GitHub Desktop (see [`02-github-sharing-and-obsidian.md`](02-github-sharing-and-obsidian.md#github-basics)). If not, copy the project folder into a `...-backup` copy. That way, if the AI breaks something, you can go back.
3. **Say one sentence to the tool**, for example: *"Run step 5 of `../toolkit/skills/user-voice-synthesis/SKILL.md`."* The tool reads only the files the step card lists.
4. **Read the result and check it yourself** in the next step. The AI draft and the version you corrected sit in two separate places.
5. **Write a line in `insights/project-log.md`:** what you decided, why, and where the AI helped.

### Step 5: Use the hub

The hub is where you answer the question: "Which user need is this decision based on?"

- **Each design decision is its own file.** For example decision `D2` lives at `insights/decisions/D2.md`.
- **You write each fact in one place only.** Decision `D2` says which hypothesis it tests; the hub works out the reverse direction.
- **After each update,** run `python3 ../toolkit/tools/build-report.py` (or ask the AI tool to) so the report rebuilds the summary tables and warnings.

How the hub works is in `toolkit/guides/03-how-the-hub-works.md`.

### View markdown files

An `.md` file is plain text, so **any tool that can open a folder will do**. Pick by what you need:

| Tool | What it does |
|---|---|
| **AI coding tool** | Open the whole project folder as the project. The tool reads `AGENTS.md`, reads and edits files directly, and runs the step cards. This is how you work with the AI |
| **Obsidian** (free) | Open the whole project folder as a vault. Adds Graph view, Backlinks and tables by item type. See [`02-github-sharing-and-obsidian.md`](02-github-sharing-and-obsidian.md#obsidian) |
| **VS Code** (free) | Install it from [code.visualstudio.com](https://code.visualstudio.com), open the whole project folder, click an `.md` file, then press `Cmd+Shift+V` (Mac) or `Ctrl+Shift+V` (Windows) to see the rendered version |
| **GitHub** | If you saved the folder to a Private repo, open the repo on github.com; Markdown is already rendered |
| **Browser** (nothing to install) | Double-click the `index.html` at the root of the project folder: that is the home page of the hub. After you edit the hub, ask the AI tool to run `python3 ../toolkit/tools/build-report.py` to rebuild it. See [`02-github-sharing-and-obsidian.md`](02-github-sharing-and-obsidian.md#share-your-hub) |

Open the **whole folder**, not single files: the links between pages only work when the whole folder is open.

**A note on links:** items link to each other with `[[ ]]` in the properties block at the top of a file. Only Obsidian turns them into clickable links. Other tools can still read and edit them because they are just text, and an AI coding tool understands them normally.

### Make it your own

| You want to | How |
|---|---|
| Add your own folder (notes, images, recordings) | Create a new folder at the same level as `work/`, for example `notes/` |
| Remove a file you do not use | Delete it. If a page in `stages/` uses that file, remove it from the From work column in the Pages table in `stages/README.md`. If it is an item, run `python3 ../toolkit/tools/build-report.py` again |
| Add a stage page | Add a row to the Pages table in `stages/README.md`: set an Id, pick the file in the From work column and the item tables you want to show. No new file needed |
| Add an item (need, hypothesis, decision...) | Run `python3 ../toolkit/tools/new-item.py` in the project folder: the command asks one question at a time, picks the next code and links the relationships for you |
| Add a document (competitor analysis, persona, flow, prototype...) | Copy a template from `toolkit/skills/<skill>/templates/` into `work/`, or create a folder and drop images, PDFs, HTML into it. See `work/README.md` |
| Add a decision or a test | Run `python3 ../toolkit/tools/new-item.py D` (or `E`): the command picks the new code and links the relationships for you |
| Use your company's design system | Write your `context/design-system-notes.md` and use `toolkit/skills/prototype/starter/` as the model |
| Write the files in Vietnamese | You can. Only keep file names and folder names in English |

### Keep it safe

- **Anonymise before giving anything to an AI tool or sharing it outside.**
- **Do not keep passwords, users' personal data or unpublished financial figures in this folder**, even when the repo is Private.
- The hub is private by default. How to let others see it is in [`02-github-sharing-and-obsidian.md`](02-github-sharing-and-obsidian.md#share-your-hub).
