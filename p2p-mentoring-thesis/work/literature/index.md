---
type: "generic"
title: "Source library"
stage: "Discover"
status: "draft"
summary: "Literature index with IDs, quality tiers and tags; per-source notes in notes/."
supports: []
---
# Source Library

**Topic:** Designing a Peer-to-Peer Mentoring Service (global, with a focus on Vietnam)
**Citation style:** APA 7
**Linked files:** [research-timeline.md](../research-timeline.md) · [research-log.md](../research-log.md)
**Last updated:** 2026-10-08

> **How this library grows (Claude maintains it)**
> - A source used or mentioned in our chats is added to the index with its tags.
> - A link or PDF you paste becomes an entry with a short summary.
> - Each entry records the log entry and timeline step that used it.
> - Before submission, sources never cited in the paper are flagged.
> - The APA citation is generated from the details I can verify. Anything I can't confirm (page numbers, DOI, publisher) is marked `[verify]` for you to check against the original.

---

## Conventions

### Source ID
`Author_Year_Keyword`, with no spaces. For an organisation, use its short name. Examples: `OECD_2024_SkillsOutlook`, `EU_2024_PlatformWorkDirective`, `Nguyen_2023_MentoringVN`. If two sources collide, add `a` or `b` after the year.

### Source note file (only when a source needs a summary or quotes)
Saved as `notes/<Source ID>.md` using the template below. Small sources can stay as an index row only.

### Quality tier

| Tier | Meaning | Examples |
|---|---|---|
| **A** | Peer-reviewed | Journal article, conference paper |
| **B** | Official or institutional | OECD, EU, Eurostat, government and statistics offices, World Bank |
| **C** | Industry or company | Consulting report, company blog, platform data (ADPList, Preply) |
| **D** | News, blog or opinion | Press article, personal blog |

Rule of thumb: use A and B for claims, C for market examples, D only as a pointer to something better.

### Reading status
`To read` → `Read` → `Cited` (used in the paper) or `Dropped` (with the reason in Notes).

### Tags
Same tags as the research log, plus a method tag.
- Factor: `#political` `#economic` `#social` `#technological` `#environmental` `#legal`
- Scope: `#vietnam` `#global` `#eu`
- Technological subtopics (use together with `#technological`):
  `#tech-ai` AI and automation in mentoring · `#tech-access` digital access and infrastructure · `#tech-platform` platform technology (video, scheduling, payments, trust tools) · `#tech-pace` pace of innovation · `#tech-data` data, privacy and security technology (cross-link to Legal)
- Social subtopics (use together with `#social`, draft list, to confirm when we reach the Social factor):
  `#social-motivation` learner motivation and engagement · `#social-trust` trust in non-credentialed experts · `#social-career` career anxiety and the AI-driven job market · `#social-community` community, reputation and recognition · `#social-culture` culture and norms around mentoring in Vietnam
- Method: `#pestel` `#competitor` `#interview` `#survey` `#theory`
- Add a new tag only if you will search for it later.

---

## Source index

| ID | Citation (APA 7) | Tier | Tags | Status | Used in (log date · timeline #) | Summary (2 to 3 lines) |
|---|---|---|---|---|---|---|
| Wang_2026_AIMCMatching | Wang, S.-M., Yaqin, M. A., & Phan, M. N. (2026). Optimizing mentor-mentee matching: A framework for AI-MC as a UX approach in online learning. *Interactive Learning Environments, 34*(4). `[verify pages/DOI]` https://rnd.ntut.edu.tw/p/16-1042-155956.php?Lang=en | A | #technological #tech-ai #tech-platform #global #pestel | Read (abstract only), see [notes](notes/Wang_2026_AIMCMatching.md) | 2026-10-08 · 1.1 | AI-mediated communication framework for the first pairing phase of mentors and mentees. |
| Chang_2024_AIMentorsSTEM | Chang, C.-N., Hui, J., Justus-Smith, C., & Wang, T.-W. (2024). Navigating STEM careers with AI mentors: A new IDP journey. *Frontiers in Artificial Intelligence*. https://doi.org/10.3389/frai.2024.1461137 `[verify vol/article no.]` | A | #technological #tech-ai #tech-data #global #pestel | Read, see [notes](notes/Chang_2024_AIMentorsSTEM.md) | 2026-10-08 · 1.1 | AI mentor (Gemini) in career planning; proposes hybrid human plus AI mentoring models; flags bias, privacy, misinformation. |
| OECD_2026_DigitalEducationOutlook | OECD. (2026). *OECD digital education outlook 2026: Exploring effective uses of generative AI in education*. OECD Publishing. `[verify DOI]` https://www.oecd.org/en/publications/oecd-digital-education-outlook-2026_062a7394-en.html | B | #technological #tech-ai #tech-pace #global #pestel | Read via secondary summary only, see [notes](notes/OECD_2026_DigitalEducationOutlook.md) | 2026-10-08 · 1.1 | Evidence synthesis on GenAI in education; task success with GenAI does not always mean learning. |
| DataReportal_2025_Vietnam | DataReportal. (2025). *Digital 2025: Vietnam*. https://datareportal.com/reports/digital-2025-vietnam `[verify author/date]` | C | #technological #tech-access #vietnam #pestel | To read | 2026-10-08 · 1.1 | Internet, mobile and social media usage in Vietnam (early 2025). Compiled from other sources. |
| KenResearch_2025_VNeLearning | Ken Research. (n.d.). *Vietnam e-learning market*. https://www.kenresearch.com/industry-reports/vietnam-e-learning-market.md `[verify]` | C | #technological #tech-access #economic #vietnam #pestel | To read | 2026-10-08 · 1.1 | Market-size estimates. Figures differ between providers, so cross-check before use. |
| Mentorloop_2025_AICantReplace | Mentorloop. (n.d.). *Why AI can't replace mentors (but it can supercharge them)*. https://mentorloop.com/blog/why-ai-cant-replace-mentors/ `[verify date]` | C | #technological #tech-ai #global #pestel | To read | 2026-10-08 · 1.1 | Vendor blog on hybrid human plus AI mentoring. Commercial interest. |
| GovTech_AITutors | GovTech. (n.d.). *Can AI fully replace student tutors? Some experts think not*. https://www.govtech.com/education/k-12/can-ai-fully-replace-student-tutors-some-experts-think-not `[verify author/date]` | D | #technological #tech-ai #global #pestel | To read | 2026-10-08 · 1.1 | News article: human connection remains key in tutoring. |
| eLearningIndustry_AIMentoring | eLearning Industry. (n.d.). *Can AI truly help democratize mentoring and career development?* https://elearningindustry.com/can-ai-truly-help-democratize-mentoring-and-career-development `[verify author/date]` | D | #technological #tech-ai #global #pestel | To read | 2026-10-08 · 1.1 | Opinion piece on AI and access to mentoring. |
| WorldBank_2021_TakingStockDigitalVN | World Bank. (2021). *Taking stock: Digital Vietnam, the path to tomorrow* (Vietnam Taking Stock report). World Bank Group. https://documents.worldbank.org/en/publication/documents-reports/documentdetail/522031629469673810 `[verify DOI/series]` | B | #technological #tech-access #tech-data #tech-pace #vietnam #pestel | Read (text version), see [notes](notes/WorldBank_2021_TakingStockDigitalVN.md) | 2026-10-08 · 1.1 | Main World Bank source on Vietnam's digital economy: connectivity, skills, e-commerce, innovation, cybersecurity and data protection, with three recommendation areas. Data refers to about 2020 to 2021. |
| WorldBank_2020_DigitalEconomyVN | Dione, O. (2020, February 5). *Digital economy in Vietnam: Building the foundations for future growth* [Blog post]. World Bank Blogs. https://blogs.worldbank.org/en/eastasiapacific/digital-economy-vietnam-building-foundations-future-growth `[verify]` | B (blog, low weight) | #technological #tech-access #vietnam #pestel | Read, low priority | 2026-10-08 · 1.1 | Short blog based on a 2019 regional report: internet reach about 64%, digital payments and bank accounts low, skills gap. Old data. Prefer the 2021 report. |
| ADB_2022_UnequalAccessVN | Dao, N. D., Phan, T. H., & Chau, H. M. T. (2022). *Tackling unequal access to digital education in Viet Nam during the COVID-19 pandemic* (ADBI Development Case Study No. 2022-3). Asian Development Bank Institute. https://doi.org/10.56506/OMLV4181 `[verify author order]` | B (teaching case study, use with care) | #technological #tech-access #social #vietnam #pestel | Read, see [notes](notes/ADB_2022_UnequalAccessVN.md) | 2026-10-08 · 1.1 | Who lacked online education access in Vietnam during 2019 to 2021 and why. |
| Bao_2023_OnlineLearningVN | Bao, D. (2023). The impacts of the global pandemic on online learning in Vietnam. *English Language Teaching Educational Journal, 6*(2), 84–94. https://doi.org/10.12928/eltej.v6i2.9217 `[verify year: PDF says Aug 2023, DOAJ says Jan 2024]` | A (low weight: reflective essay, no primary data) | #technological #tech-access #social #social-motivation #vietnam #pestel | Read, see [notes](notes/Bao_2023_OnlineLearningVN.md) | 2026-10-08 · 1.1 | Pandemic boosted online learning adoption in Vietnam; digital inequality and limited social interaction remained. Modest journal, so check quality. |
| Tadelis_2016_ReputationFeedback | Tadelis, S. (2016). Reputation and feedback systems in online platform markets. *Annual Review of Economics, 8*, 321–340. https://doi.org/10.1146/annurev-economics-080315-015325 `[verify DOI]` | A | #technological #tech-platform #global #pestel | Read (abstract only), see [notes](notes/Tadelis_2016_ReputationFeedback.md) | 2026-10-11 · 1.1 | Survey of how reputation and feedback systems build trust on online platforms: theory, how they work, evidence, bias problems, design improvements. Specific flaws not yet verified. |
| UU_P2PReputationMeta | *Reputation effects in peer-to-peer online markets: A meta-analysis*. `[verify authors/year/journal]` https://research-portal.uu.nl/en/publications/reputation-effects-in-peer-to-peer-online-markets-meta-analyses-a/ | A | #technological #tech-platform #global #pestel | To read | 2026-10-10 · 1.1 | Meta-analysis of 107 studies: seller reputation affects selling performance in P2P markets. |
| Qooper_n.d._MentoringFeatures | Qooper. (n.d.). *Mentoring software engagement features*. https://www.qooper.io/blog/mentoring-software-engagement-features `[verify date]` | C (vendor, commercial interest) | #technological #tech-platform #global #pestel | To read | 2026-10-10 · 1.1 | Vendor view of the features of mentoring software (matching, scheduling, reminders, mobile, analytics). Use as an example list only. |
| HAI_2026_AIIndex | Stanford Institute for Human-Centered AI. (2026). *The AI index report 2026*. https://hai.stanford.edu/ai-index/2026-ai-index-report `[verify authors/edition]` | B | #technological #tech-pace #global #pestel | To read | 2026-10-10 · 1.1 | Annual data on AI capability, adoption and responsible AI. Generative AI reached about 53% population adoption within three years (per secondary summaries; verify in the report). |
| WEF_2025_FutureOfJobs | World Economic Forum. (2025). *The future of jobs report 2025*. https://www.weforum.org/publications/the-future-of-jobs-report-2025/ | B | #technological #tech-pace #social-career #economic #global #pestel | To read | 2026-10-10 · 1.1 | Employer survey: about 22% of jobs disrupted by 2030, nearly 40% of skills change, 63% of employers cite skills gap. Numbers come from the WEF summary pages; verify in the report. |
| UNESCO_2023_GenAIGuidance | UNESCO. (2023). *Guidance for generative AI in education and research*. UNESCO. https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research `[this is the article page; find the report on unesdoc.unesco.org and cite that]` | B | #technological #tech-data #global #pestel | To read | 2026-10-10 · 1.1 | Calls for data protection and privacy standards for GenAI in education and an age limit of 13 for classroom use. School-focused. |
| Tandirerung_2025_AIEducationSecurity | Tandirerung, V. A. (n.d.). Security and privacy threats in AI-driven education systems: A narrative literature review. *Journal of Embedded System Security and Intelligent Systems, 6*(4). https://doi.org/10.59562/jessi.v6i4.10902 `[verify year]` | A (low weight: single author, narrative review, K-12 scope) | #technological #tech-data #global #pestel | **Dropped** 2026-10-11: not relevant (K-12 minors, weak venue). See [notes](notes/Tandirerung_2025_AIEducationSecurity.md) | 2026-10-11 · 1.1 | Narrative review of security and privacy risks of generative AI in adolescent education: minors' data exposure, prompt-injection, profiling, misinformation, governance gaps. |
| Jekabsone_2023_GDPROnlineAdultEducation | Jekabsone, I. (2023). Selected legal issues in online adult education: Compliance of online learning and teaching process with GDPR. *TalTech Journal of European Studies, 13*(2), 46–58. https://doi.org/10.2478/bjes-2023-0015 `[verify pages/year]` | A | #technological #tech-data #legal #global #pestel | Read, see [notes](notes/Jekabsone_2023_GDPROnlineAdultEducation.md) | 2026-10-11 · 1.1 | GDPR analysis for online adult education: recording consent, platform providers as processors or joint controllers, unauthorised access, data loss, cyberattacks. Survey of 60 Latvian providers. |
| A29WP_2018_ProfilingGuidelines | Article 29 Data Protection Working Party. (2018). *Guidelines on automated individual decision-making and profiling for the purposes of Regulation 2016/679* (WP251 rev.01; endorsed by the EDPB). https://ec.europa.eu/newsroom/article29/items/612053 `[verify]` | B (official guidance) | #technological #tech-data #legal #global #pestel | To read | 2026-10-11 · 1.1 | Official EU guidance on profiling and automated decisions (GDPR Art. 22), including transparency, data subject rights and children. Relevant to AI matching and profiling of mentors and mentees. |
| SRH_2024_ThesisBriefing | SRH Fernhochschule. (n.d.). *Preparing for your Master Thesis* [Presentation slides]. SRH Fernhochschule – The Mobile University. `[verify year]` | B | #setup #theory | Read | 2026-10-08 · 0.5 | Thesis requirements, ethics principles, milestones, structure, grading. Benchmarks: 100+ survey respondents, 5+ interviews, 60 to 80 pages. |

---

## How to capture a source (link vs file vs notes)

Do not convert whole articles to markdown. Keep a link, an archive copy for sources you will cite, and short evidence notes.

| Source type | Keep |
|---|---|
| Tier A or B you will cite | Link + a PDF or archived copy (in `pdfs/`, named with the Source ID) + a note file with evidence cards |
| Tier C | Link + archive copy + 2 to 3 evidence cards (data points only) |
| Tier D | Link + 1 line on why it is useful. No note file unless cited |
| Web pages that can change | Also save a web.archive.org snapshot link, and record the date you retrieved it |

**Evidence card** (inside the note file, one per usable point): the point in your own words, the page or table number, the year the data refers to, and where you will use it. Use direct quotes rarely and keep them short. When you write the paper, you write from the cards, and the link is only for checking.

---

## Source note template

```
# <Source ID>

- **Retrieved:** (date) · **Archive link / PDF file:**

- **APA 7 citation:**
- **Link / DOI / file:**
- **Tier:** A / B / C / D
- **Tags:**
- **Status:** To read / Read / Cited / Dropped
- **Used in:** (log date · timeline #)

## Summary
(2 to 3 lines: what it says, in my own words)

## Credibility note
(Who produced it, method, sample or data, date, bias or limitation)

## Evidence cards
- Point (own words): ... · Page/Table: __ · Data year: __ · Use in: __
- Short quote (rarely): "..." (p. __)

## How I use it in the thesis
(Which claim or section, e.g. PESTEL · Legal · Vietnam)

## Notes
```

---

## Pre-submission checks (run in the last 3 weeks)

- [ ] Every source marked `Cited` appears in the reference list
- [ ] Every reference-list item appears in this index
- [ ] No source is left as `To read`
- [ ] All `[verify]` marks are resolved against the originals
- [ ] Sources with no use are marked `Dropped` or removed
