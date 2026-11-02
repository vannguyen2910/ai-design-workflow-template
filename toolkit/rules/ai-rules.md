# Rules for the AI tool

The rules every project shares. Each project's `AGENTS.md` points here, so there is one copy to keep up to date. The rules that depend on a single project (its map, where files go, the reading order, the steps to run) stay in that project's `AGENTS.md`.

## Hard rules

1. **Return only the section you were asked for.** Do not edit other sections or other files. The owner pastes the result in, or you write exactly into the section you were pointed to.
2. **Do not edit an "(AI draft)" section after you created it, and do not edit the owner's "(verified)" section** unless you were asked for exactly that section. Drafts and checked versions always sit in two separate sections.
3. **Use only sources in `work/sources/anonymised/`.** Never invent a quote, a figure, a product name or a source. If it is not in the sources, write `unknown`.
4. **Quote verbatim, with the ID.** Do not rewrite or shorten.
5. **Any number that is not confirmed is `assumed`.** An inference that is not in the sources is `inferred`.
6. **Stop and tell the owner** if you see data that looks not anonymised (names, emails, usernames, company names) in a folder you are allowed to read.
7. **Say what you are unsure about.** List the items you are unsure of instead of guessing a link or a relationship.
8. **Never make a copy of an item.** An item exists only in its own file (`insights/decisions/D2.md`...). Relationships live in the properties (the `---` block at the top of the file) as wikilinks in quotes, declared in one direction only. Tables elsewhere are `generated` blocks; do not fill them by hand.
9. **If the folder is a git repo with uncommitted changes,** suggest the owner says "Lưu lại" before you write files, so there is a point to go back to (see Save and publish).

## Writing

- Answer in the language the owner writes in. Write document content in the language of the source material and the owner (Vietnamese if that is what they use), and keep trade terms in English (insight, hypothesis, opportunity, handoff...).
- Keep section headings in English: the step cards and the hub refer to them by those names.
- Write content to be read by people, not by a database. In the body of a document, do not show item codes (O1, H2, D3, E1, RH6), counts like `(n=13)` or `9/13`, file paths, step-card or skill names, or labels like `assumed` and `unknown`. Say it in plain words instead: "most travellers we surveyed", "not known yet", "a target nobody has confirmed". The codes stay in the properties at the top of the file (`supports`, `tests`...), where the report uses them to link pages. Keep a source by naming it in words ("the interview", "the survey"). Keep quotes word for word.
