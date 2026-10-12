---
type: "generic"
title: "Master Thesis Exposé (draft)"
stage: "Setup"
status: "draft"
summary: "Working exposé: problem statement, research questions and approach for the P2P mentoring service thesis."
supports: []
---
<!-- original frontmatter
title: "Master Thesis Exposé"
subtitle: "Designing a Peer-to-Peer Mentoring Service: Matching Independent Experts with Learners Across Domains, Without Formal Educator Credentials"
author: "[Your full name]"
student_id: "[Student ID]"
program: "Master of UX and Service Design, SRH Fernhochschule – The Mobile University"
supervisor: "[Supervisor name – to be confirmed]"
date: "[Date]"
-->
## Working Title

*Designing a Peer-to-Peer Mentoring Service: Matching Independent Experts with Learners Across Domains, Without Formal Educator Credentials*

*(Working title, to refine with the supervisor once the topic is confirmed.)*

---

## 1. Background and Problem Statement

Professionals with real expertise, whether in coding, languages, design, leadership, or career coaching, increasingly want to earn money by mentoring or teaching. On the other side, learners want exactly that kind of guidance: individual, practical, tied to someone's actual experience rather than a fixed curriculum. The demand on both sides is real. What sits between them is not.

That motivation is broader than income alone. In a job market that feels increasingly unstable, especially as AI reshapes what employers value, packaging and sharing expertise is also a way for professionals to build something more durable than a single job: a reputation, a community, a visible track record that they know what they're doing. For some, mentoring is mainly a passion project or a way to give back and build community around their field. For others, it doubles as a form of career insurance, evidence of impact that doesn't disappear if their current role does. Money is one reward among several, credit, reputation, recognition, and a supportive professional community all count as value too, and a service designed around this problem needs to account for all of them, not just the transaction.

Today, mentors compete hard for visibility on crowded platforms with no guarantee they will find a mentee they can actually work with over time, and a lot of them simply don't know how to turn what they know into something teachable or sellable. Learners have the mirror problem. Established mentors are expensive to access, and even when a learner finds someone who seems right, that mentor is often unavailable. So the market has a strange shape: mentoring is costly to get on one side, while a large pool of capable experts sits unmonetised on the other. That's not really a supply problem. It's a matching and enablement problem.

A second pattern grows out of the first. Most mentoring today is short and transactional, a session here, a few calls there, while the guidance that actually changes someone's trajectory usually takes sustained practice and feedback over weeks or months. This thesis treats that short-engagement pattern as a symptom rather than a separate issue: when expectations, level, and format aren't aligned from the start, there's little reason for a relationship to continue. Get the match right, and both problems move at once, experts can monetise their knowledge without becoming professional educators, and the relationships that form have a real chance of lasting.

The specific pain points bear this out. Mentors describe not knowing where to start when structuring an offer, and spending significant unpaid effort proving themselves on competitive platforms with no guarantee it pays off. Mentees describe struggling to find a suitable mentor at all, or finding the right one and discovering they're unavailable. Many mentees are newcomers to their field with no case study of their own, which is exactly the kind of concrete, specific guidance a good match should give them. Different symptoms, same root cause: no service reliably connects what one side expects with what the other side can actually offer.

Existing platforms only cover part of this. They're almost all single-domain, design mentoring on ADPList, language tutoring on Preply, coding mentorship on Codementor, so none of them has had to treat matching and onboarding as a domain-agnostic service problem. Whether one shared service model can hold up across very different kinds of expertise, and where it would need to bend, is the question this thesis sets out to answer.

### 1.1 Current Landscape

A quick scan of the market explains why this gap has persisted. ADPList is free, design- and product-focused, with plenty of mentor supply but weak monetisation and inconsistent matching. Preply and iTalki have solved pricing and trust for language learning specifically, but go no further than that. Codementor and similar tools serve developers on a pay-per-session basis with little support for anything longer-term. Superpeer, Clarity.fm, and MentorCruise are more general, but they treat matching as browse-and-search rather than fit-to-expectations, and none of them help a first-time mentor package their expertise in the first place. This fragmented, domain-by-domain landscape is the backdrop for the domain-agnostic alternative this thesis proposes, and it's examined more closely through the competitor analysis in Section 7.

---

## 2. Relevance — Why Now

Three things make this worth doing now rather than five years ago, or five years from now.

**Labour market pressure.** Skills are turning over faster than formal retraining can keep up with. The World Economic Forum expects 39% of workers' core skills to change by 2030, and US job postings requiring AI-related skills grew 144% year-over-year as of April 2026, against 7% overall job growth (Gloat, 2026). At that pace, people need faster, more flexible ways to pick up skills than formal education or corporate L&D can provide on their own timeline, and peer-to-peer mentoring is one of the few channels that can move that fast. That same instability cuts both ways: it's also pushing experienced professionals to diversify how they demonstrate and monetise what they know, since a single employer or job title no longer feels like enough security on its own.

**Market readiness.** People are already paying for this, informally. The mentoring and coaching software market is forecast at roughly USD 855 million in 2026, growing at a 14.9% compound annual rate (360iResearch, 2026). The broader creator economy sits around USD 200 billion in 2025 and is expected to grow at 22.7% CAGR toward more than USD 800 billion by the early 2030s, with coaching and courses now the second and third most common ways creators monetise what they know (51% offer coaching or services, 53% sell courses) (Circle, 2026). The behaviour already exists at scale. What's missing is a service layer that does it well.

**Technological readiness.** Turning expertise into teachable material used to require instructional design skill or a lot of spare time, neither of which most independent experts have. That's changed. AI-assisted tools can now generate quizzes, coaching prompts, and structured session material from raw expertise, cutting out most of the packaging work. That's the exact barrier this thesis is about: an expert no longer has to become a professional educator to teach well, because the tooling can do a lot of that work for them now.

---

## 3. Research Objectives

This thesis has two objectives:

1. **Design and evaluate a service concept** that lets independent experts across varied domains package and share their knowledge through mentoring, capturing monetary value as well as non-monetary value such as reputation, recognition, and community, without needing formal teaching qualifications.
2. **Enable learners to find the right-fit mentor** against their own expectations, on the premise that a stronger match should, as a downstream outcome, sustain a longer and more effective mentoring relationship than the short, ad hoc engagements common today.

---

## 4. Key Research Questions

**Primary research question**

> How can a peer-to-peer service be designed to match independent experts with learners based on expectations, and enable effective teaching, without relying on formal educator credentials?

**Supporting questions**

1. What pain points and workarounds do professionals currently rely on to monetise their expertise and find mentees or mentors?
2. What criteria do mentees actually use to judge "the right mentor," and do those criteria hold across a hard skill like coding versus a soft skill like leadership coaching, or do they diverge?
3. What stops capable experts from packaging their knowledge into paid, teachable formats, and which of those barriers can service design actually solve, as opposed to pedagogical training?
4. Does match quality, meaning fit against a learner's expectations, correlate with how long a mentoring relationship lasts, compared with the shorter, one-off engagements that dominate today?
5. How does a prototype of the matching and onboarding flow hold up when tested with real mentors and mentees?
6. What distinct mentee profiles exist across the studied domains, and what attributes, motivation, experience level, expectations, and budget, define each?
7. What distinct mentor profiles exist across the studied domains, and what attributes, expertise level, teaching/coaching style, availability, and pricing approach, define each?
8. Beyond direct income, what motivates professionals to package and share their expertise, passion, community-building, reputation, recognition, or job-market and career-security concerns, and how do these motivations shape what they want from the service?

---

## 5. Scope

This study covers expertise broadly rather than staying inside one field, because the central question, whether one matching and enablement model can work across very different kinds of expertise, only gets answered credibly with contrast built into the research. Rather than trying to cover "any skill" at once, the study uses a small number of contrasting domains as comparative cases: coding (a hard skill with established platforms), a language (a hard skill where pricing and trust norms are already standardised through platforms like Preply), design (a hybrid, creative skill still mostly informal and unpaid via platforms like ADPList), and a soft skill such as leadership or career coaching (the most intangible of the four, and the hardest to package into teachable units).

This is a deliberate choice, not a shortcut. A small, purposive, cross-domain sample stress-tests whether a single service model holds up or needs to flex by domain, which a large survey covering every possible field couldn't do as well. Recruitment leans on the researcher's own network (ADPList, an internal mentoring practice, the design community) for the design domain, and on outreach through the relevant peer platforms and referrals for coding, language, and soft-skill coaching.

---

## 6. Theoretical Grounding

The thesis is grounded primarily in service design theory, particularly service blueprinting and co-creation as set out by Stickdorn, Hormess, Lawrence, and Schneider (2018), which structures both the research process and the move from findings to a testable service concept rather than stopping at a list of insights.

Matching and enablement also draw on the literature around communities of practice and social learning (Wenger, 1998). That work treats expertise-sharing as something socially situated, built on mutual engagement and shared practice, rather than a simple transfer of information. It suggests "the right match" might be as much about shared context and working style as technical fit, which is exactly what the interview research is designed to test.

A third strand concerns trust and reputation on peer-to-peer and two-sided platforms, drawing on research into how trust substitutes for formal credentials in marketplaces like Airbnb and Uber. This matters here because the service under study depends on trust between two parties with no institutional credentialing behind them, and it shapes how the matching mechanism and onboarding flow are designed to surface credibility signals.

Motivation is treated as more than financial, drawing on self-determination theory (Deci & Ryan, 2000), which separates intrinsic motivations such as autonomy, mastery, and relatedness from extrinsic ones such as income or career security. This matters because the problem framing above suggests mentors are driven by a mix of both: some mainly by passion or community-building, others by reputation and career insurance in an unstable job market, many by some combination. The service concept needs to design for that mix rather than assuming money is the only reward worth building around.

The full literature review, including a systematic comparison of existing single-domain platforms (ADPList, Preply, Codementor, Superpeer, Clarity.fm, MentorCruise), follows in the main body of the thesis. This section stays brief at the exposé stage on purpose, naming the anchors rather than reviewing them in full.

---

## 7. Research Methodology

The project follows a Double Diamond process, pairing qualitative comparative-case research with a designed and tested service artifact. The methods below are scoped to what's needed to answer the research questions, not the full service design toolkit.

**Discover** — figuring out what "good matching" actually looks like from both sides, before designing anything.
- Desk research and a competitor / service safari review of existing single-domain mentoring platforms, to see where current services succeed and fail
- Semi-structured interviews with mentors and mentees across the four domains, including retrospective questions about past mentoring relationships that ended early versus ones that lasted. This is how research question 4, match quality versus duration, gets investigated, since actual duration can't be observed directly within the thesis timeline

**Define** — turning the research into a scoped, evidence-based problem statement.
- Thematic analysis of the interviews, coded for matching criteria, onboarding barriers, and relationship-duration factors
- Personas for mentor and mentee segments across domains
- Jobs-to-be-Done framing of what each side is actually trying to achieve, including mentors' non-monetary motivations (research question 8)
- A revised problem statement, grounded in the findings, replacing the exploratory one in Section 1

**Develop** — turning the problem statement into something concrete and testable.
- Concept ideation and opportunity mapping against the defined problem
- User flows for the matching and onboarding journey
- A service blueprint of the proposed future-state experience, showing frontstage and backstage actions for both sides
- Wireframes of the core matching and onboarding flow

**Deliver** — testing whether the concept actually holds up, and where it needs to adapt by domain.
- A high-fidelity, clickable prototype of the matching and onboarding flow
- Usability and desirability testing with a subset of participants across the sampled domains
- Iteration based on what testing shows
- A reflection on generalisability: where the model held across domains, and where it had to bend

---

## 8. Expected Outcome and Contribution

The output is a validated service concept, a future-state service blueprint plus a tested prototype, for matching independent experts with learners on expectations, and for helping those experts teach well without formal teaching credentials. Academically, the contribution is an evidence-based answer to whether a single matching and enablement model generalises across genuinely different types of expertise, something the current literature and platform landscape hasn't really addressed, since it's split by domain. Practically, the concept is meant to work as the actual foundation for a service the researcher plans to run for fellow designers and other professionals.

---

## 9. Assumptions and Limitations

This research trades breadth for depth on purpose. A small, purposive sample across four contrasting domains tests whether a service model generalises; a large-scale survey might claim statistical representativeness but wouldn't deliver the kind of design-oriented, qualitative insight this thesis needs. So the findings should be read as indicative of where a domain-agnostic model holds or breaks, not as proof it holds everywhere.

The study also assumes recruitment is realistic across all four domains within the timeline. The researcher's existing network gives strong access to the design domain; coding, language, and soft-skill coaching participants will need to come through their own platforms or referrals, which carries more schedule risk and will need close attention once research begins.

And because the timeline doesn't allow a real service to run long enough to watch mentoring relationships end naturally, relationship duration (research question 4) gets studied through retrospective interview accounts rather than direct longitudinal observation. That's a reasonable proxy, not a substitute for a live, long-running study, and it's named here as a limitation rather than something to gloss over.

---

## 10. Preliminary Timeline

*(Indicative only, to be aligned with the official milestone dates once the topic and supervisor are confirmed.)*

| Phase | Focus | Approx. duration |
|---|---|---|
| Discover | Desk research, competitor analysis, expert interviews | 3–4 weeks |
| Define | Synthesis, personas, JTBD, problem statement | 2–3 weeks |
| Develop | Concept ideation, service blueprint, wireframes | 3–4 weeks |
| Deliver | Prototype, usability testing, iteration | 3–4 weeks |
| Write-up | Full thesis drafting, review, submission | 4–6 weeks |

---

## 11. Confidentiality

This thesis is built on the researcher's own service concept and independent research, not proprietary employer material, so confidentiality isn't expected to be an issue. Any anecdote drawn from the researcher's professional mentoring practice will be abstracted to remove identifiable employer or client detail, in line with standard practice for professional portfolio material. To confirm with the supervisor and course director against SRH's confidentiality provisions.

---

## Preliminary References

*(To expand during the literature review; formatting to align with SRH's required citation style.)*

- 360iResearch. (2026). *Mentoring software market size & demand analysis*. https://www.360iresearch.com/library/intelligence/mentoring-software
- Circle. (2026). *Creator economy statistics for 2026*. https://circle.so/blog/creator-economy-statistics
- Deci, E. L., & Ryan, R. M. (2000). The "what" and "why" of goal pursuits: Human needs and the self-determination of behavior. *Psychological Inquiry*, 11(4), 227–268.
- Gloat. (2026). *AI workforce trends 2026 (Q3 update)*. https://gloat.com/blog/ai-workforce-trends/
- Stickdorn, M., Hormess, M., Lawrence, A., & Schneider, J. (2018). *This is service design doing: Applying service design thinking in the real world*. O'Reilly Media.
- Wenger, E. (1998). *Communities of practice: Learning, meaning, and identity*. Cambridge University Press.
