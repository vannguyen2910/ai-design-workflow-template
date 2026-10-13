# Gates

The four gates (checkpoints) a project goes through. Each check has a status: `open` (not done), `passed` or `failed`. **Do not rename a check, only change its status.** A gate passes when all of its checks pass.

## Gate 1: Discover (Question + evidence)

| Check | What | Status |
|---|---|---|
| 1a | The business question and outcome are agreed with the product owner, or marked **assumed** with the agreement status | open |
| 1b | Every insight traces back to a source you can open | open |
| 1c | Nothing is guessed: unknowns and counterexamples are recorded; the AI draft sits next to the checked version, with the error rate | open |

## Gate 2: Define (Evidence + agreement)

| Check | What | Status |
|---|---|---|
| 2a | Every opportunity points to the evidence behind it | open |
| 2b | The problem brief is signed by product and business, or the agreement status is recorded | open |
| 2c | Every hypothesis has a test and a metric (an unconfirmed metric is marked **assumed**) | open |
| 2d | The principle checks are written as yes/no questions | open |

## Gate 3: Develop (Alignment)

| Check | What | Status |
|---|---|---|
| 3a | At least three different directions were explored; the choice and its reason are recorded | open |
| 3b | Every decision traces back to an opportunity with evidence and to a hypothesis (no decision without a user need, no opportunity left out) | open |
| 3c | Every decision passes the principle checks, or the conflict is recorded as a trade-off | open |
| 3d | The prototype uses the design system and the accessibility rules that were checked | open |

## Gate 4: Deliver (Real users + buildability)

| Check | What | Status |
|---|---|---|
| 4a | Real users tested the hypotheses; results are set next to the baseline | open |
| 4b | Findings trace back to the original notes or recordings and are ranked by importance | open |
| 4c | A developer can build without coming back with questions (handoff pack and decision log are complete) | open |
| 4d | The measurement plan was given to the product owner | open |

The **Automatic check** column (in the report) shows whether the current data meets that check. It does not change the status you set; if you set `passed` and the data does not support it, the report shows a warning.

After you change a status here, ask the AI tool to update the Gates table on the Overview page ([`README.md`](../README.md)).
