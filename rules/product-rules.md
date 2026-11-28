# Product rules

Rules for product decisions: what to test, when work is ready to hand over, and how research data is handled. They sit on top of [`ai-rules.md`](ai-rules.md) and the project's gates (`standards/gates.md`). Where a gate already covers a point, this page only says how to apply it.

These are defaults. The owner may relax one for a specific piece of work, but must record why in `insights/project-log.md`.

## 1. Assumptions and tests

The map of assumptions is `work/assumptions-map.md`. Tests are written as hypotheses and measured through metrics.

1. **Give every assumption one type:** desirability (do they want it), viability (does it work for the business), feasibility (can we build it), usability (can they use it) or ethical (could it harm someone). If it fits two, split it into two assumptions.
2. **Rank by importance and by how little is known.** The ones to test first are important and poorly known. Do not rank by how easy the test is.
3. **Test the riskiest assumption with the smallest test that can answer it,** for example a five-person usability test or a prototype of one screen. Do not build the feature to find out.
4. **Write what counts as pass and fail before the test runs.** Put it in the metric's `target` and name the test in the hypothesis statement. Never set or change a `target` after the result is known.
5. **Record the result as it came out.** `met`, `missed` or `inconclusive` in `verdict`. A missed target is a result, not a reason to change the target.
6. **Do not fix a metric's `baseline` or `target` by guessing.** Leave it `unknown` or `assumed` until the owner confirms (see the hard rules).
7. **Mix kinds of evidence for a decision that matters:** what people said (interview, survey) next to what they did (test, analytics). Say in the opportunity or decision which kind is missing.
8. **An assumption nobody can test stays an assumption.** Do not turn it into a finding, and do not use it to justify a decision as if it were evidence.

*Why: teams usually fail by building before they know, and by moving the goalposts after the result. Rules 3 and 4 prevent both.*

## 2. Handoff: ready and done

A handoff is the moment the work passes to the people who build it. Treat both lists as a guide, not a gate that blocks work for its own sake: tick what applies to this piece of work and say why the rest does not. Gate 4 in `standards/gates.md` is the hard check.

**Ready to hand over** (the design side is finished enough that a developer does not have to guess):

- The flow or screens in the handoff are the latest version, and the version is named.
- Every decision in the handoff traces back to an opportunity and a hypothesis.
- Each screen lists its states (see [`design-rules.md`](design-rules.md), rule 1).
- The measurement plan names what will be measured, the target and who reads it.
- Findings of severity 4 are fixed, and each finding of severity 3 is either fixed or accepted with a reason (see `standards/severity-levels.md`).
- Open questions are listed with an owner, not hidden in the design.

**Done** (the work is built and can be closed):

- Every state in the handoff exists in the build, not only the default one.
- Design assets and component changes are in the shared place the team uses.
- The handoff notes say what was changed from the design, and why.
- The design QA (`work/design-qa.md`) has been run against the build.
- The measurement from the plan is switched on.

*Why: most rework comes from a developer finding a missing state or an unanswered question late. A short shared list catches it early; a long strict one turns into a waterfall.*

## 3. Research data and consent

Gate 1f is the hard stop for consent and anonymising. These rules add the details.

1. **Consent covers each research activity.** One consent for an interview does not cover a later survey or a recording being used for something else.
2. **Say who else touches the data.** If a transcription service or an AI tool processes a recording or notes, the participant is told before, in plain words.
3. **Removing names is not enough.** A job title, a team size, a small town or an unusual event can identify a person. When anonymising, also remove or generalise these. If a person could still be recognised, the data is not anonymised.
4. **Keep raw data apart.** Recordings and raw transcripts stay in `work/sources/_raw-private/`. Only the anonymised version is in `work/sources/anonymised/`. Never move raw data across.
5. **Set a retention date for raw data and keep it.** The owner decides the period, following the company policy and local law. As a starting point, a shorter period is better than a longer one: raw data loses value fast, the anonymised insights do not. Delete raw data that has no record of consent.
6. **Delete contact details as soon as they are no longer needed** to run the research or pay the participant.
7. **Pay or thank participants fairly,** and do not pressure anyone to continue or to answer a question.
8. **Say when you used AI to process research data.** Log the tool and what it did (gate 1g).

*Why: research is done by people who also carry the duty of care, because there is usually no ethics committee. Writing it down once is cheaper than deciding it each time.*

## What the AI must do

- Before you write a test, check that the metric has a `target` written first. If not, stop and ask the owner for it.
- Before you mark work as ready or done, list which items you could not check, and why.
- If research data looks like it is not anonymised under rule 3 above (not only names), stop and tell the owner.
