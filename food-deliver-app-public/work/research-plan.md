---
type: "research-plan"
title: "Research plan"
stage: "Discover"
status: "draft"
summary: "How the case study will analyse the user guidance of a food delivery app: three core functions, the methods for each, the usability test set-up, the data rules and the open decisions to confirm. Draft for Alternative C, Process Mapping."
---

# Research plan

**Status:** draft. The app, country, language, device and three functions are decided. Everything still marked **To confirm** is a proposal you decide before you start phase 3.

## 1. Purpose

The module asks for a case study that reconstructs and analyses an existing user experience, evaluates it, and ends in recommendations. For Alternative C, the focus is **user guidance**: how well the app leads people through its key processes.

**Main question:** How well does the food delivery part of the app guide users through finding, paying for and receiving an order, and what would improve it?

**Sub-questions:**

1. Where do the three core processes have unnecessary steps, unclear decisions or likely breakdowns?
2. Which parts of each process cost users the most mental effort?
3. How do users feel and what do they expect at each touchpoint across the whole journey?
4. Which usability problems do experts find, and which do real users actually hit?
5. Which changes would make the guidance clearer, faster and more supportive?

## 2. Case study

| | |
|---|---|
| **App** | Grab, food delivery part only. Decided. Grab is a large provider and the brief prefers a medium-sized one, so justify the choice in the introduction |
| **Why this app** | It gives access to a real service, it has more than three connected functions (search, ordering, payment, tracking, chat with the driver), and it is widely used in Asia |
| **Country and language** | Vietnam, with the app and the tests in English. Decided. Vietnam makes it easier to recruit participants and run the tests. State the country, language and app version in the paper. Check that the Vietnam version of the app offers an English interface |
| **Device** | The mobile app on an iPhone. Decided. App version recorded: v33437965. **To confirm:** the exact iPhone model and iOS version, and use the same phone for all screenshots so the screens match |
| **Out of scope** | Ride-hailing, parcel delivery, the payments wallet as its own product, and the merchant or driver apps |

## 3. The three core functions

The brief asks for three core functions rebuilt as user flows. Decided:

| # | Function | Starts when | Ends when |
|---|---|---|---|
| 1 | Find and order food | The user opens the food section | Items are in the cart and the user moves to checkout |
| 2 | Check out and pay | The user opens the cart | The order is confirmed |
| 3 | Track the order and fix problems | The order is confirmed | The food arrives, or the user cancels or asks for support |

These are connected: the end of one is the start of the next, which also supports the "at least three interconnected functions" requirement.

## 4. Methods

Each method answers a different question, so together they cover the process from several sides.

| Method | What it gives | Used on | Output |
|---|---|---|---|
| **User flows** | A map of steps, decision points and possible breakdowns | The three functions, from your own walk-through of the app | Three flow diagrams |
| **Task analysis** | The user's goals, the actions required, and where effort or friction appears | Each flow | A task breakdown per function |
| **User journey** | The whole experience across touchpoints, with emotions, expectations and pain points | All three functions together | One journey map |
| **Heuristic evaluation** | Usability problems found by an expert against recognised heuristics (for example Nielsen's ten) | Each flow, screen by screen | An issue list with severity |
| **Cognitive walkthrough** | Whether a first-time user would know what to do at each step | Each flow | Answers to the walkthrough questions for every step |
| **Usability test** | Problems real users actually meet while doing realistic tasks | The three functions | Task results, observations and quotes |

Use only sources that can be cited for the theory behind each method. Verify any rule of thumb in a citable source before it goes into the paper.

### Heuristic evaluation

- Evaluator: you. A single evaluator finds fewer problems than several, so state this as a limit in the paper. If you can, ask one more person to do a second pass.
- Rate each issue by severity on a simple scale (for example from 0, not a problem, to 4, usability catastrophe) and write down which heuristic it breaks.
- Record the screen, the step in the flow and a screenshot for every issue.

### Cognitive walkthrough

For each step in each flow, answer the standard questions: will the user try to achieve the right effect, will they notice the right action is available, will they connect the action with their goal, and will they see that progress was made after acting. Mark every step where the answer is no.

## 5. Usability test

| | |
|---|---|
| **Goal** | See where real users struggle in the three functions and how the findings compare with the expert evaluation |
| **Participants** | **To confirm.** Proposal: a small group of regular food delivery users. A group of about five is a common choice for this kind of qualitative test, but verify the claim in a citable source before you rely on it. Include some people who know Grab and some who do not, if you can |
| **Recruiting** | Friends, classmates or colleagues who order food online. No names in the paper |
| **Format** | One-to-one session of about 30 minutes, think-aloud, on the participant's own phone or yours (**To confirm**) |
| **Consent** | Short written or spoken consent: purpose, voluntary, recording, anonymous, can stop any time |

### Tasks

One scenario per function, in plain words, without telling the user which buttons to press:

1. *You want dinner for two tonight. Find a restaurant that suits you and put your meal in the cart.*
2. *You are ready to order. Pay in the way you normally would and place the order.*
3. *Your order is on its way. Find out when it will arrive. Then imagine something is wrong with it and find out how to get help.*

Real orders cost money. **To confirm:** stop each session before the final confirmation, or let participants use their own accounts and order for real with a small budget you cover.

### What to measure

- Task success: completed, completed with help, or failed.
- Time on task.
- Errors and wrong turns, noted by the observer.
- One easy rating after each task (for example how easy it felt, on a 7-point scale).
- Overall impression and quotes at the end of the session.

### Procedure

1. Welcome, explain the test, get consent.
2. Short questions about their food delivery habits.
3. The three tasks, with think-aloud.
4. Rating after each task.
5. Closing questions: what was easiest, what was most annoying, what would you change.

## 6. Data and privacy

- Anonymise before anything goes to the paper or to an AI tool: no real names, phone numbers, addresses or account details. Blur personal data in screenshots.
- Store recordings, notes and raw answers in `work/sources/_raw-private/` only. Never give that folder to an AI tool.
- Put anonymised results in `work/sources/anonymised/`.
- Record the date, country, device and app version for every screenshot and every session.

## 7. From data to results

1. Flows, task analysis and journey map come from your own walk-through of the app.
2. The expert evaluation and the walkthrough give a list of issues.
3. The usability test confirms, adds to or contradicts that list.
4. Group the issues by function and by cause, and rank them by severity and how many users were affected.
5. Write one recommendation for each key problem, and say which evidence supports it.

This matches the order of the paper: introduction, methodological approach, documentation, analysis, findings, recommendations, reflection.

## 8. Limits to state in the paper

- One evaluator for the heuristic evaluation.
- A small number of participants, so the results show problems, not statistics.
- One country (Vietnam), one device and one app version.
- Participants in Vietnam use the English interface, which may affect how they understand labels. State this and note which participants speak English as a second language.
- Real order costs may limit how far the checkout test can go.

## 9. Schedule

Follows `submission-timeline.md`: planning in phase 2, documentation in phase 3, flows in phase 4, task analysis and journey in phase 5, the evaluation in phase 6, the test in phase 7 and the findings in phase 8.

## 10. Decisions still open

| Decision | Who decides | Needed by |
|---|---|---|
| Talk to the module manager about the schedule and the planned February 2027 submission | You | 29 Nov 2026 |
| Which iPhone model and iOS version? | You | 6 Dec 2026 |
| Number of participants and how to recruit them | You | 6 Dec 2026 |
| How to handle real order costs in the test | You | 6 Dec 2026 |
| A second evaluator for the heuristic evaluation | You | 6 Dec 2026 |
