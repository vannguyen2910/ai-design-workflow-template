---
type: "process-map"
title: "E2E process map"
stage: "Develop"
status: "draft"
summary: "The Travel Buddy journey step by step, with four actors (traveler, Travel Buddy, a local, a companion or contact): who does each step, what happens, which planned solution carries it and where the step comes from. Before the trip, on the trip and after it."
takeaways:
  - "Every planned solution in the pool has a step on the map; a step with no solution is a handover or a choice the traveler makes."
  - "A visitor can browse without an account, and the chat with a local only opens when both sides have shown interest."
  - "Four steps have no source yet: the sign-up screen, where the crowd signal gets its data, how a traveler finds one specific local, and editing what was recorded before the journal is built."
supports:
  - "[[D2]]"
  - "[[D3]]"
  - "[[D4]]"
  - "[[D5]]"
  - "[[D6]]"
  - "[[D7]]"
source: "process-map-diagram/process-map.html"
media:
  - "process-map-diagram/process-map.html"
embed: true
---
# E2E process map

The end-to-end journey of Travel Buddy, written as a list of steps. It is the **main flow document** of this project. Each row says **who does the step, what happens, and which planned solution carries it**, so a reader can follow every handover between the traveler, the app, a local and a companion.

The swimlane diagram of the same journey is shown on this page. The original written flow is kept as a source document.

## How to read it

- One row is one step, in the order it happens. **Who** is the actor that owns the step.
- **Planned solution** is the idea from the solution pool that the step relies on. A dash means the step needs no solution of its own.
- In the diagram each column is one actor and a line that crosses into another column is a handover. The small line under a step names its planned solution; orange marks the steps with no source yet.
- **Source** says where the step comes from: the written flow, the process map diagram, a decision, or the simulated usability round. **unknown** means no source describes the step yet.

## Before the trip

| # | Step | Who | What happens | Planned solution | Source |
|---|---|---|---|---|---|
| 1 | Opens the app | Traveler | Arrives from a referral, the app store or social media | — | Written flow |
| 2 | Shows tips right away | Travel Buddy | The feed opens with no account needed | No-account browsing | Written flow |
| 3 | Wants to save a tip or message someone | Traveler | If yes, sign-up is asked for; if no, keeps browsing and signs up later | No-account browsing | Decision |
| 4 | Signs up | Traveler | Creates an account | — | **unknown** |
| 5 | Answers three questions | Traveler | Gives travel style, interests and home city, nothing else | Lightweight onboarding | Written flow |
| 6 | Opens free access | Travel Buddy | The core features are free from the first session | Free-first model | Written flow |
| 7 | Shows a first personal result | Travel Buddy | The feed is matched to the traveler's style in the first session | Value-first onboarding | Written flow |
| 8 | Sets location controls | Traveler | Chooses what is recorded and when | Granular location controls | Written flow |
| 9 | Write tips | Locals and other travelers | Tips come from people, with no ads or paid placements | Peer-sourced tip feed | Process map |
| 10 | Shows the tip feed | Travel Buddy | Each tip shows who wrote it | Peer-sourced tip feed | Written flow |
| 11 | Filters by travel style | Traveler | Sees tips from people who travel the same way | Traveler-style matching | Written flow |
| 12 | Shows a crowd signal | Travel Buddy | Marks places that are overcrowded or commercialised | Crowd signal | Decision |
| 13 | Feeds the crowd signal | Travel Buddy | Where the data comes from, reports from users or a calculation, is not decided | Crowd signal | **unknown** |
| 14 | Watches a short video | Traveler | Sees what a place really feels like | Video tip snippets | Written flow |
| 15 | Reads safety notes | Traveler | Sees safety context from recent travelers for the destination | Safety context | Written flow |
| 16 | Saves a tip with one tap | Traveler | The tip goes to the trip shortlist without leaving the feed | One-tap save | Decision |
| 17 | Pastes an AI-made itinerary | Traveler | Travel Buddy turns the pasted text into shortlist items | AI itinerary import | Decision |
| 18 | Keeps a living shortlist | Travel Buddy | Saved places sit in a list that can be reordered, not a fixed day plan | Living shortlist | Written flow |
| 19 | Invites a companion | Traveler | Sends an invitation to plan together | Collaborative planning | Written flow |
| 20 | Edits the same shortlist | Companion | Views and changes the shared shortlist | Collaborative planning | Process map |
| 21 | Checks the map | Traveler | Sees all saved places on a map, then leaves for the trip | Map view | Written flow |

## On the trip

| # | Step | Who | What happens | Planned solution | Source |
|---|---|---|---|---|---|
| 1 | Arrives at the destination | Traveler | The trip starts | — | Process map |
| 2 | Reorders the shortlist | Traveler | Changes the order as plans shift | Living shortlist | Written flow |
| 3 | Checks the connection | Travel Buddy | With internet the live feed stays open; without it the shortlist, map and notes still work | Offline access | Written flow |
| 4 | Records places in the background | Travel Buddy | Location and time are logged with no action from the traveler | Auto-capture | Written flow |
| 5 | Suggests locals | Travel Buddy | Matches the traveler with locals by declared interests and travel style | Interest and style matching | Written flow |
| 6 | Looks for one specific local | Traveler | There is no search and no invitation, so a known person cannot be found | — | **unknown** |
| 7 | Opens a local's profile | Traveler | From a tip or from the Locals tab | — | Process map |
| 8 | Shows who the local is | Travel Buddy | Verified identity, interests and languages | Verified identity | Written flow |
| 9 | Keeps the profile up to date | Local | Verified profile and availability | Verified identity | Process map |
| 10 | Frames the exchange | Travel Buddy | Free and two-way: no payment, no booking | Reciprocal exchange | Written flow |
| 11 | Sends a first message | Traveler | Asks for a recommendation | In-app messaging | Written flow |
| 12 | Opens the chat | Travel Buddy | Only when both sides have shown interest | In-app messaging | Decision |
| 13 | Reads the message | Local | Sees the shared interests; if not happy to meet, the chat ends | — | Process map |
| 14 | Replies with a time and place | Local | Free of charge | Reciprocal exchange | Process map |
| 15 | Meets the local | Traveler | In person | — | Process map |
| 16 | Reports or blocks | Traveler | Available on every profile if something feels wrong; the connection is closed | Report and block | Written flow |

## After the trip

| # | Step | Who | What happens | Planned solution | Source |
|---|---|---|---|---|---|
| 1 | The trip ends | Traveler | Returns home | — | Process map |
| 2 | Reviews what was recorded | Traveler | Removes records they do not want before the journal is built | — | **unknown** |
| 3 | Builds the journal | Travel Buddy | Lays out the recorded places and people met; the traveler does not design it | Auto-generated layout | Written flow |
| 4 | Keeps the journal private | Travel Buddy | Nobody else sees it unless the traveler chooses | Private-first journal | Decision |
| 5 | Decides whether to share | Traveler | If yes, picks specific contacts; nothing is posted publicly | Selective sharing | Written flow |
| 6 | View the journal | Chosen contacts | See only what was shared with them | Selective sharing | Process map |
| 7 | Keeps a memory archive | Travel Buddy | The journal can be searched and is tied to real place names | Contextual memory layer | Written flow |
| 8 | Starts the next trip | Traveler | Goes back to the tip feed with the past trips as a reference | Peer-sourced tip feed | Written flow |

## How it relates to the decisions

| Moment on the map | Decision |
|---|---|
| Shows tips right away, no account needed | Browse without an account |
| Tips come with a crowd signal and safety notes | Crowd signal and safety notes |
| Saves a tip with one tap | One-tap save |
| Turns a pasted AI itinerary into shortlist items | Import an AI itinerary |
| Opens the chat only when both sides show interest | Chat opens on mutual interest |
| The journal is private unless contacts are chosen | Private journal by default |

## Tensions the map makes visible

- **Recording against privacy.** Recording places in the background needs location access all the time, while the traveler was promised full control over what is recorded.
- **Short onboarding against good matching.** Three questions keep the start light, but style filtering and matching with locals work better with a fuller profile.
- **Recording everything against control.** Travelers also want to remove records they do not want, which is why the review step after the trip is still open.

## What it does not show

- The map shows the **main path**. Error states and edge cases are not listed.
- It is a design artifact, not a test result. Whether users follow these paths is not confirmed: the only usability round so far is simulated.
