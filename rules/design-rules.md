# Design rules

Rules for what a good design includes and how its words are written. They sit on top of [`ai-rules.md`](ai-rules.md). The project's own `context/accessibility-rules.md`, `context/design-system-notes.md` and `standards/severity-levels.md` are the details; this page does not repeat them, it says when to apply them.

These are defaults. The owner may relax one for a specific screen, but must record why in `insights/project-log.md`.

## 1. Complete screens: states

1. **Every screen and component lists its states.** Use this set and mark the ones that do not apply: default, hover, focus, pressed, disabled, loading, empty, error, success.
2. **Empty, loading and error are designed, not left to the developer.** Say what the user sees, what they can do next, and how long a wait can last before something changes.
3. **Every flow has a way back and a way out.** The user can see where they are, go back one step without losing what they typed, and leave without penalty.
4. **Forms keep what the user typed after an error.** Never clear a field because another one failed.
5. **A destructive action is either confirmed or undoable.** If neither is possible, say so in the design notes and treat it as severity 4 until it is solved.
6. **If a state is missing, list it as missing.** Do not invent a design for it and present it as decided.

## 2. Accessibility

Apply `context/accessibility-rules.md`. If the project has no such file, use these as the minimum (WCAG 2.2 AA):

1. **Text contrast of at least 4.5:1,** and 3:1 for large text and interface parts such as input borders and icons that carry meaning.
2. **Touch and click targets of at least 24 × 24 px, and 44 × 44 px where there is room.** The 24 px figure is the minimum in WCAG 2.2 AA; 44 px is the recommended size.
3. **Everything works with a keyboard,** in a sensible order, and the focus is always visible and not hidden by a sticky header or an overlay.
4. **Anything done by dragging has another way** that needs only a single tap or click.
5. **Colour is never the only signal.** An error or a status also has text or an icon.
6. **Every input has a visible label.** Placeholder text is not a label.
7. **Images that carry meaning have a text alternative.** Decorative ones are marked as decoration.

Check contrast and target sizes with numbers, not by eye. If you cannot measure, say you did not.

## 3. Severity when you review

1. **Use the 0 to 4 scale in `standards/severity-levels.md`** for every issue, with a short reason for levels 3 and 4.
2. **Rate the effect on the user, not the effort to fix.**
3. **One rater is unreliable.** When the AI rates, it gives its rating as a draft; the owner (or better, two or three people) confirms before it is used to block or release work.
4. **Do not set `resolution` on a finding yourself** (already in the AGENTS rules).

## 4. Copy

Writing for the screen: buttons, labels, errors, empty states, short instructions. For deeper work use the `ux-copy` skill; these are the rules that always apply.

1. **A button says what will happen,** with a verb and the object: "Book a ticket", not "Submit" or "OK". If two buttons sit together, their labels must differ clearly.
2. **An error says what went wrong and how to fix it,** in words the user uses. No error codes, no system words, no blame. Avoid "invalid" and "incorrect", which say nothing about the fix: say what is needed ("Enter a date like 12/03/2026").
3. **Show all the errors of one submission together,** with a summary at the top that links to each field. Do not show them one after another as pop-ups.
4. **Put the message next to the problem and keep it until it is fixed.** A message that disappears on its own cannot be read by everyone.
5. **An empty state says why it is empty and what to do next.**
6. **Short sentences, active voice, one idea each.** Around 15 words on average is a good target. Prefer the word the user would say over the word the team uses.
7. **Keep one word for one thing.** Check `context/glossary.md` before you name something, and do not use two words for the same thing on different screens.
8. **Do not use colour, capital letters or exclamation marks to carry meaning or to push the user.**
9. **Copy in a design is a draft until the owner approves it.** Mark text that the AI wrote as a draft, and never present it as tested wording.

## What the AI must do

- When you are asked to review or build a screen, list the states you found and the ones missing, before anything else.
- When you cannot measure contrast or size, say so instead of saying it passes.
- When you write copy, say which rules it was checked against, and flag any that conflict with `context/glossary.md` or the brand voice.
