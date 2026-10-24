# Workflow: Prototype

Build a clickable prototype of the direction you chose, one screen at a time, with the AI coding tool using only your design system. You check every screen before the next one.

*Status: draft. Try it on a real project and adjust it to how you work before you rely on it.*

| | |
|---|---|
| Working folder | `work/prototype/` (copy it from `../toolkit/templates/prototype-starter/` if it is not there yet). The file `work/prototype/index.md` is the working file and holds the screen plan and the known gaps |
| Sources | `work/options.md` (the chosen direction), `work/problem-brief.md`, `work/user-flow.md` or the flow you drew (if any), `context/design-system-notes.md`, `standards/principle-checks.md` |
| Rules file | `work/prototype/project-rules.md` (give it to the AI coding tool at every build step) |
| Original data | `work/sources/_raw-private/` (the AI does not read it) |
| Final output | A prototype that runs in a browser, `work/prototype/index.md` with the scope and known gaps, and decision files for what you chose on the way |
| Related | `ideation.md` is the step before; `../toolkit/skills/build-process-map.md` for the flow diagram; `../toolkit/skills/add-media.md` to show it in the report |

The prototype is a **reference for developers and a thing to test with users**, not production code. Use the design system you have; the AI must not invent colours, components or sizes.

## Sections of the working file (`work/prototype/index.md`)

| Section | Filled in step | By |
|---|---|---|
| `## Scope` (flow, screens, fidelity) | 1 | YOU |
| `## Screen plan (AI draft)` | 2 | AI. **Do not edit** |
| `## Screen plan` | 3 | YOU: the final list |
| `## Build log` | 4 and 5 | AI lists the changed files, YOU record the verdict per screen |
| `## Rule check (AI)` | 6 | AI. **Do not edit** |
| `## Known gaps` | 7 | YOU |

Two rules: the AI changes only the files for the screen you asked for, and the AI's report of what it did is never accepted until you opened the files and the page.

## If a gate is not met

| Gate | After step | If the answer is no |
|---|---|---|
| A: a plan you can build and test? | 3 | Cut screens until one flow can be completed from start to end |
| B: this screen is right? | 5 | Ask the AI to fix only that screen, then check it again before the next one |
| C: honest and ready to test? | 7 | Write the gaps down, or fix them before you test with users |

---

## Step 1: Set the scope

**Who:** YOU
**Input:** `work/options.md`, `context/design-system-notes.md`
**Output:** `## Scope` in `work/prototype/index.md`

Write: the one flow to prototype (start, goal, end); the number of screens (aim for 3 to 6); the fidelity (clickable HTML with real content, not a mock of every state); which design system you use. Using the starter? Copy `toolkit/templates/prototype-starter` to `work/prototype`. Using your own? Fill in `context/design-system-notes.md` and replace the tokens and components in the folder, and tell the AI so in the rules file. Write the real content the screens need (names, labels, messages) in a short list.

**Check:** Can someone finish the flow in one sitting? Is each hypothesis you want to test (H#) reachable in this flow?
**Failure sign:** "The whole app"; no real content; no design system and no decision to use the starter.

## Step 2: Plan the screens

**Who:** AI
**Input:** `## Scope`, `work/options.md` (the chosen direction), `context/design-system-notes.md`, `work/prototype/design-system/components.html` (only to see what exists)
**Output:** `## Screen plan (AI draft)`

**Instruction:**
> Use only the scope, the chosen direction and the design system below. List the screens of the flow in order. For each screen: its purpose in one sentence; the content it shows (use my content list, write "unknown" where I did not give it); the components from the design system it needs; the states it must handle (empty, loading, error, success), and where the user goes next. Mark every component the design system does not have as "MISSING" and do not invent it. Do not describe visual style beyond the design system. Say what you are unsure about. Return only this section.

**Failure sign:** A component that is not in `components.css`; invented content; a screen that does not lead anywhere.

## Step 3: Review the plan · Gate A

**Who:** YOU
**Input:** `## Screen plan (AI draft)`
**Output:** `## Screen plan` (final)

Walk the flow as the user: does each screen move them closer to the goal? Cut screens that do not. For each "MISSING" component decide: use an existing one, or add it yourself to the design system (the AI does not add it for you). Fill the gaps in the content. Add the error and empty states the plan skipped.

**Gate A:** Can the flow be completed with the screens listed? Does each screen link to the opportunity or hypothesis it serves? Is every component either existing or decided?
**Failure sign:** The AI plan kept as is; "MISSING" components left for the AI to improvise.

## Step 4: Build one screen

**Who:** AI
**Input:** `work/prototype/project-rules.md`, `work/prototype/design-system/`, the one screen from `## Screen plan`, and the files the screen needs. Run this step once per screen
**Output:** The screen files in `work/prototype/`, and a line in `## Build log`

**Instruction:**
> Read `project-rules.md` first. Build only the screen "<name>" from my screen plan. Use only the variables in `tokens.css` and the components in `components.css`; no raw colours, sizes or fonts, no libraries. Use my real content; if something is missing write "unknown" and ask. Make it work with the keyboard, with a visible focus, and move focus to the new heading when the screen changes. Do not touch any file I did not name. When you finish, list every file you changed and every place you were unsure.

**Failure sign:** Files changed that you did not ask for; a new CSS file; a hard-coded colour; "lorem ipsum".

## Step 5: Check the screen · Gate B

**Who:** YOU
**Input:** The screen in a browser (open `work/prototype/index.html`; if the screens are separate files or links break, ask the AI to start a local preview), `## Screen plan`
**Output:** Your verdict in `## Build log` (ok / fix: what), and a saved checkpoint

Open the page and use it: click every control, then tab through it with the keyboard only. Check against the plan (content, states, next step). Search the CSS the AI touched for raw values (`#` colours, `px` sizes outside the tokens). Compare with `components.html`: does it look like the same system? If it is right, say **"Lưu lại"** so the AI saves a checkpoint, then go back to step 4 for the next screen. If not, send back only the fix for this screen.

**Gate B:** Does it match the plan? Does it work with a keyboard? Is every colour and size from the design system? Is the checkpoint saved?
**Failure sign:** You read the AI's report instead of opening the page; two screens built before the first was checked.

## Step 6: Rule check

**Who:** AI
**Input:** The finished prototype in `work/prototype/`, `project-rules.md`, `standards/principle-checks.md`
**Output:** `## Rule check (AI)`

**Instruction:**
> Check the prototype against `project-rules.md` and the principle checks, without changing any file. List every place that breaks a rule: raw colour or size values, components not in the design system, an input without a visible label, an error without a message beside the field, meaning carried by colour alone, a touch target under 44 px, a screen with more than one `<h1>`, focus not moved on a screen change. For each, give the file and line. Then list which principles each screen is most likely to break. Do not fix anything. If you cannot check something from the files, say so.

**Check:** Open three of the places it lists. Are they real? Is anything you noticed yourself missing from the list?
**Failure sign:** A list with no file and line; "no issues found" without saying what was checked.

## Step 7: Record the gaps · Gate C

**Who:** YOU
**Input:** `## Rule check (AI)`, `## Build log`, `## Scope`
**Output:** `## Known gaps`, and the decisions you made on the way

Fix the rule breaks that matter, or write them down. Write what the prototype does **not** do (states not built, content faked, screens missing, anything that would not survive a real developer), so nobody tests or hands off something that looks finished but is not. Record the choices you made on the way as decisions: `new-item.py D --title "..." --reason "..." --state proposed`. Add the prototype to the report with `../toolkit/skills/add-media.md`, linked to the hypotheses you want to test.

**Gate C:** Can a tester complete the flow? Is every gap written down? Does the report claim no more than what was built?
**Failure sign:** An empty "Known gaps"; decisions made in the chat that exist nowhere in the project.

---

## The limit to state plainly

A prototype that runs shows the idea **can** work, not that it **does**. It is a thing to test, not a result. The AI's report that a screen is done is only a summary: the proof is the page you opened and used yourself.
