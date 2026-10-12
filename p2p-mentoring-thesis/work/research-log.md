---
type: "generic"
title: "Research log"
stage: "Discover"
status: "draft"
summary: "Dated log of every research method step, with decisions and reasons."
supports: []
---
# Research Log

**Topic:** Designing a Peer-to-Peer Mentoring Service (global, with a focus on Vietnam)
**Companion file:** [research-timeline.md](research-timeline.md) (plan and status). This file holds the details of what actually happened.

> **How to use**
> - Add one entry per work session or per method step. Newest entry at the top of the Entries section.
> - Always include the date and the timeline number (for example `1.1`), so the log and the timeline stay linked.
> - Record decisions and their reasons, not only results. This is what the methodology chapter and the supervisor will ask about.
> - Copy the entry template below for each new entry.

> **Tag list (keep it short):**
> - Factor: `#political` `#economic` `#social` `#technological` `#environmental` `#legal`
> - Scope: `#vietnam` `#global`
> - Type: `#decision` `#problem` `#quote` `#setup`
> - Add a new tag only if you will search for it later.

> **File naming for research outputs:** prefix with the timeline number and keep outputs in a phase folder, for example `1_Discovery/1.1_PESTEL.md`. Use `_v2` at the end for revisions. The three tracker files keep their plain names.

---

## Entry template

```
### YYYY-MM-DD · <timeline #> <method name> · <sub-topic>
- **Tags:** #factor/scope/type (for example #legal #vietnam #decision)
- **Goal of this session:**
- **What I did:**
- **Sources / data used:** (author, year, link or file name)
- **Findings:**
- **Decisions and why:**
- **Problems / open questions:**
- **Next step:**
- **Time spent:** (hours)
```

---

## Entries

### 2026-10-11 · 1.1 Desk research · PESTEL, Technological: replacement sources for tech-data
- **Tags:** #pestel #technological #tech-data #legal
- **Goal of this session:** Replace the dropped Tandirerung source with stronger sources for `#tech-data`
- **What I did:** Searched and read Jekabsone 2023 in full (GDPR in online adult education); added the Article 29 Working Party profiling guidelines (official, not read yet)
- **Sources / data used:** Jekabsone_2023_GDPROnlineAdultEducation, A29WP_2018_ProfilingGuidelines
- **Findings:** Five GDPR challenges for online adult education; consent must be freely given; platforms are processors or joint controllers. Not about AI profiling and not about Vietnam
- **Decisions and why:** Jekabsone is the main `#tech-data` source; A29WP covers AI matching and profiling. Vietnam data protection (Decree 13/2023 and newer law) goes to the Legal factor
- **Problems / open questions:** Need the official text of Vietnam's data protection decree or law (not only law-firm summaries)
- **Next step:** Read A29WP guidelines (focus on Art. 22 and profiling), then `#tech-pace`
- **Time spent:**

---

### 2026-10-11 · 1.1 Desk research · PESTEL, Technological: Tadelis 2016 (abstract only)
- **Tags:** #pestel #technological #tech-platform
- **Goal of this session:** Get the main points of Tadelis (2016) for `#tech-platform`
- **What I did:** Full text is paywalled, so I used the abstract and wrote a note file. Corrected the library summary: the specific flaws (inflation, retaliation, selective reviewing) came from other search results, not from Tadelis
- **Sources / data used:** Tadelis_2016_ReputationFeedback
- **Findings:** Reputation and feedback systems build trust under asymmetric information; the article reviews theory, mechanisms, evidence, bias problems and design improvements
- **Decisions and why:** Use as a theory base for the trust mechanism of the platform. Do not cite specific flaws until the full text is read
- **Problems / open questions:** Need the full text via the SRH library. Check the related NBER paper 20830
- **Next step:** Read the Stanford AI Index and WEF summaries for `#tech-pace`
- **Time spent:**

---

### 2026-10-11 · 1.1 Desk research · PESTEL, Technological: Tandirerung (abstract only)
- **Tags:** #pestel #technological #tech-data
- **Goal of this session:** Get the main points of the JESSI narrative review on security and privacy threats in AI education
- **What I did:** The journal site blocked my reader, so I used the abstract from a search index and wrote a note file. Renamed the entry to Tandirerung_2025 (author found)
- **Sources / data used:** Tandirerung_2025_AIEducationSecurity
- **Findings:** Five risk clusters (minors' data exposure, prompt-injection, profiling, misinformation, governance gaps) and four responses (privacy by design, cybersecurity, AI governance, educator training). Scope is K-12, so indirect for mentoring
- **Decisions and why:** Low weight source (single author, narrative review, embedded-systems journal). **Update, same day: dropped as not relevant** (K-12 scope). `#tech-data` still needs a stronger source besides UNESCO 2023 and Chang 2024
- **Problems / open questions:** Full text not read. Year not confirmed
- **Next step:** Get the full text through the DOI or the SRH library
- **Time spent:**

---

### 2026-10-10 · 1.1 Desk research · PESTEL, Technological: sources for thin subtopics
- **Tags:** #pestel #technological #tech-platform #tech-pace #tech-data
- **Goal of this session:** Find Tier A and B sources for `#tech-platform`, `#tech-pace` and `#tech-data`
- **What I did:** Claude searched and added 7 sources to the library as "To read" (3 for platform, 2 for pace, 2 for data)
- **Sources / data used:** Tadelis_2016, UU_P2PReputationMeta, Qooper_n.d., HAI_2026_AIIndex, WEF_2025_FutureOfJobs, UNESCO_2023_GenAIGuidance, JESSI_n.d.
- **Findings:** None yet. Nothing has been read
- **Decisions and why:** Platform evidence will come from the general platform-market literature (reputation and trust), because I found no peer-reviewed work on mentoring-platform features; only vendor sources
- **Problems / open questions:** Gap: no Tier A or B source on mentoring-specific platform features. Several citation details need verification (authors and years for the meta-analysis and the JESSI review; UNESCO document page)
- **Next step:** Read Tadelis 2016 and the Stanford and WEF summaries, then decide if the Technological factor is covered enough
- **Time spent:**

---

### 2026-10-10 · 1.1 Desk research · PESTEL, Technological: Bao 2023 read
- **Tags:** #pestel #technological #tech-access #social #vietnam
- **Goal of this session:** Read the last Tier A source on Vietnam access
- **What I did:** Read the full PDF and wrote `notes/Bao_2023_OnlineLearningVN.md`. Renamed the entry from ELTJ_2024 to Bao_2023 (author and year were wrong in my first listing)
- **Sources / data used:** Bao_2023_OnlineLearningVN
- **Findings:** It is a reflective essay with no primary data. Useful for framing (motivation, engagement, home environment) and as a pointer to underlying Vietnamese studies. It claims city and countryside students get equal digital skills education, which conflicts with World Bank 2021 and ADB 2022
- **Decisions and why:** Treat as low-weight evidence. Chase the studies it cites (Tran 2020/2021, Van & Thi 2021, Pham & Van Nghiem 2022, Dinh & Nguyen 2020)
- **Problems / open questions:** Resolve the rural–urban conflict by reading Tran et al. (2020) and the World Bank Table 2.1
- **Next step:** Find the missing Tier A/B sources for tech-platform, tech-pace and tech-data, and newer Vietnam figures (ITU or GSO)
- **Time spent:**

---

### 2026-10-08 · 1.1 Desk research · PESTEL, Technological: Vietnam access sources
- **Tags:** #pestel #technological #tech-access #vietnam
- **Goal of this session:** Fill the Vietnam access gap with Tier A and B sources and decide how to capture sources for the paper
- **What I did:** Claude found 3 new sources (World Bank, ADB, one journal article), added them to the library as "To read", and I updated the library with a capture rule (link + archive copy + evidence cards, not whole-article markdown)
- **Sources / data used:** WorldBank_2020_DigitalEconomyVN (renamed from 2022; a 2020 blog), ADB_2022_UnequalAccessVN, ELTJ_2024_OnlineLearningVN. Correction on 2026-10-08: the CHIP and rural-gap findings belong to WorldBank_2021_TakingStockDigitalVN, not the blog
- **Findings:** None yet. Internet-use figures for Vietnam differ by source and year, so pick one primary official source and state its year
- **Decisions and why:** Keep evidence as short cards with page numbers instead of converting full articles, for copyright, link rot and manageability
- **Problems / open questions:** No GSO or ITU page confirmed yet (ITU DataHub: datahub.itu.int). Find the original World Bank report behind the blog post
- **Next step:** Download PDFs of the Tier A and B sources and start evidence cards
- **Time spent:**

---

### 2026-10-08 · 1.1 Desk research · PESTEL, Technological: 5 subtopics
- **Tags:** #pestel #technological #decision
- **Goal of this session:** Break the Technological factor into manageable subtopics
- **What I did:** Compared my initial list (technology intensity, innovation, automation, R&D) with a topic-specific one, and tagged the 8 starter sources
- **Sources / data used:** See literature/index.md
- **Findings:** Coverage by subtopic: tech-ai 6 sources (no gaps in volume, but only 2 Tier A/B); tech-access 2 (both Tier C, no A/B); tech-platform 1 (Tier A); tech-pace 1 (Tier B); tech-data 1 (Tier A)
- **Decisions and why:** Use 5 subtopics: (1) AI and automation in mentoring, (2) digital access and infrastructure, (3) platform technology, (4) pace of innovation, (5) data, privacy and security technology (cross-linked to Legal). R&D activity moved to Political or Economic, since it is a national-level topic. "Technology intensity" split into access and adoption
- **Problems / open questions:** Need Tier A/B sources for tech-access (Vietnam), tech-platform, tech-pace and tech-data
- **Next step:** Read the Tier A and B sources, then find the missing ones
- **Time spent:**

---

### 2026-10-08 · 1.1 Desk research · PESTEL, Technological: starter sources
- **Tags:** #pestel #technological #global #vietnam
- **Goal of this session:** Get a starter reading list for the Technological factor, one set per quality tier. Claude supplies the links only; the analysis and writing are mine
- **What I did:** Claude searched and listed 8 sources (2 Tier A, 1 Tier B, 3 Tier C, 2 Tier D), added to the source library as "To read"
- **Sources / data used:** See literature/index.md (Wang 2026, Chang 2024, OECD 2026, DataReportal 2025, Ken Research, Mentorloop, GovTech, eLearning Industry)
- **Findings:** None yet. Nothing has been read
- **Decisions and why:** Start with Technological only. Vietnam internet figures differ between sources (DataReportal early 2025 vs Ken Research end 2025), so cross-check dates
- **Problems / open questions:** No Tier B Vietnam source found yet (try ITU, World Bank, Vietnam General Statistics Office, Ministry of Information and Communications). Check 1 or 2 more Tier A sources on AI tutoring and on platform technology
- **Next step:** Read the Tier A and B sources and take notes in the source library
- **Time spent:**

---

### 2026-10-08 · 0.5 Set-up · Ethics and consent draft
- **Tags:** #setup #legal #global #vietnam #decision
- **Goal of this session:** Work out the ethics and consent requirements for interviews, survey and user testing
- **What I did:** Read the SRH "Preparing for your Master Thesis" briefing and wrote `context/ethics-and-consent.md`: the 7 SRH principles applied to the project, a GDPR and Vietnam data plan, recruitment rules, three consent form templates and a checklist
- **Sources / data used:** SRH briefing, work/thesis-brief/general-information-master-thesis.pdf (Tier B)
- **Findings:** SRH expects ethics in the planning phase; typical empirical work is 100+ survey respondents and 5+ interviews
- **Decisions and why:** Survey target set to 100+ and interviews to 5+ (SRH benchmark). No under-18 participants. Participants coded P01, P02…
- **Problems / open questions:** (1) Formal ethics review needed? (2) Retention period for recordings? (3) Is APA 7 required? Also decide the storage place and transcription tool. Vietnam legal references are marked `[verify]`
- **Next step:** Send the three questions to the supervisor, then finalise the consent forms and Vietnamese versions
- **Time spent:**

---

### 2026-10-08 · 0.4 Set-up · Source library created
- **Tags:** #setup #decision
- **Goal of this session:** Set up the source library with naming and tagging
- **What I did:** Created `work/literature/index.md` with the ID convention, quality tiers, reading status, tags, an index table, a note template and pre-submission checks
- **Sources / data used:** None
- **Findings:** None
- **Decisions and why:** Markdown (not Zotero) so it can be updated automatically from our chats and syncs with Drive. Citation style APA 7. Each source records quality tier, summary, quotes with page numbers, and where it was used
- **Problems / open questions:** Confirm with the supervisor that APA 7 is the required style. Zotero can still be added later for the final reference list
- **Next step:** 0.5 ethics and consent check
- **Time spent:**

---

### 2026-10-08 · 0.3 Set-up · Research log created
- **Tags:** #setup #decision
- **Goal of this session:** Plan the research process and create the tracking files
- **What I did:** Converted the chosen design process into a timeline file, confirmed the deadline (28 Mar 2027), and created this log
- **Sources / data used:** None
- **Findings:** None
- **Decisions and why:** Market scope is global with a Vietnam layer, and the work is for the thesis. Topic and supervisor were confirmed on 2026-09-08
- **Problems / open questions:** Ethics and consent requirements still to check (0.5). Source library still to set up (0.4)
- **Next step:** Finish 0.4 and 0.5, then start 1.1 Desk research (PESTEL) on 2026-10-12
- **Time spent:**

---

## Decision register (short list of key decisions)

| Date | Decision | Reason | Timeline # |
|---|---|---|---|
| 2026-09-08 | Topic and supervisor confirmed | Agreed with professor | 0.1 |
| 2026-10-08 | Scope: global, with a Vietnam layer | Thesis requirement | 1.1 |
| 2026-10-08 | Submission deadline 28 Mar 2027, with a 1-week buffer | Fit the plan to the deadline | 0.2 |

---

## Source index (running list; move to the reference manager later)

| # | Author, year, title | Type | Used in | Notes |
|---|---|---|---|---|
| | | | | |
