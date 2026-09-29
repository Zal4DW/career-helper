---
name: interview-master
description: Use when the user is preparing for, practising, or recovering from interviews, including mock interviews, what interviewers look for, post-interview or post-rejection coaching, references, and concerns about ageism or being called overqualified. Covers STAR frameworks, UK age-discrimination law, practical strategies, and emotional resilience.
tags: interview, preparation, mock, practice, rejection, coaching, star, ageism, age-discrimination, overqualified
---

# Interview Master

Complete interview support - before, during practice, and after.

## Capabilities

| # | Capability | When to Use |
|:--|:-----------|:------------|
| 1 | Interview Preparation | Preparing for an upcoming interview |
| 2 | Interviewer's Perspective | Understanding what interviewers really assess |
| 3 | Mock Interview | Practising with realistic simulation |
| 4 | Post-Interview Coaching | After a rejection or unsuccessful interview |
| 5 | Reference & Referee Prep | Choosing, asking, and briefing your referees |

## Quick Start

```
"I have an interview at [Company] next week"
"What are interviewers really looking for?"
"Let's do a mock interview"
"I just got rejected - help me understand what happened"
"I think I was rejected because of my age"
"I keep getting told I'm overqualified - what can I do?"
"I was made redundant after 25 years and I'm struggling"
"They asked for references - who should I use and how do I brief them?"
```

---

## Accessibility

**At skill start**, check for `career-helper-preferences.md` in the current working directory using the Glob tool. If found, read the YAML frontmatter and apply:

- **dyslexia_friendly: true** → Use short sentences. Number all lists and options (never unnumbered). One decision per message. No idioms or metaphors; use plain replacements. Explicit signposting at every transition ("Step 2 of 4. Next: mock interview."). Refer to saved files by description, not filename. Repeat key details (company names, role titles, dates); do not assume the user remembers from earlier messages.
- **colour_blind: true** → Never use colour alone to convey meaning. Use labels, text, or icons for all status indicators.

If **no preferences file exists** and this skill was invoked directly (not dispatched by Tim): ask once, "Do you have any accessibility preferences I should know about? For example, if you're dyslexic, I can adjust how I format things." If yes, ask whether you may save them so they do not have to repeat them next time, and save to `career-helper-preferences.md` using the format in @../tim/references/tim-preferences-format.md only if they agree. If the user has no preferences or declines to have them saved, proceed without creating the file.

These rules apply to **all communication with the user** and to the **formatting of output documents**.

---

## 1. Interview Preparation

**What you need:** CV + job description + company name + interview stage
**Load:** @references/interview-prep.md
**Template:** @references/interview-prep-template.md

Role-specific preparation, built from a competency map outwards:
- A competency map of 8-12 competencies from the job description: why each matters, the evidence in the spec, how likely it is to be tested, and the interview style it will take
- CV alignment per competency with a text-label rating (Strong, Partial, Gap), the evidence behind it, and what may concern the assessor; a Gap is recorded, never stretched
- The top five risks, ranked from the map, each with a mitigation
- 15-20 likely questions (behavioural, technical, situational, company-specific), each with what not to say
- STAR answer frameworks using your actual experience
- Interviewer's perspective for each question
- 5-7 pre-prepared adaptable stories
- Two or three timed openers ("tell me about yourself", "why this role, why now") as talking points with a word count, not scripts
- 8-10 intelligent questions to ask (by interviewer type)
- Talking points and execution tips
- Objection handling for every risk in four steps: acknowledge, reframe, evidence, close
- A one-page dashboard at the front: readiness by competency (Ready, Needs work, Gap: a preparation verdict distinct from the evidence rating, so a Strong competency with no story prepared yet is Needs work), up to five things they will like, top five concerns, top five stories, top ten questions to practise, and one thing to do today
- Post-interview follow-up templates

All answers cite your real experience with evidence. There is no overall readiness score: a single number invites you to optimise the number rather than the gap.

**Output:** `applications/{role-slug}/interview-prep.md`

**Suggested next steps:**
- "Want me to generate an Interviewer's Perspective report?"
- "Shall we do a mock run-through?"

---

## 2. Interviewer's Perspective Report

**What you need:** Job description + CV (optional but helpful)
**Load:** @references/interviewer-perspective-guide.md
**Template:** @references/interviewer-perspective-template.md

See questions from the interviewer's viewpoint:
- What they're REALLY assessing behind each question
- What makes a strong answer (criteria, not scripts)
- Red flags interviewers watch for
- How to THINK about your answer (mental frameworks, not memorised responses)
- Your experience to draw from

Question categories covered:
- Behavioural (past behaviour as predictor)
- Situational (hypothetical judgement tests)
- Role-specific (technical/functional competency)
- Cultural fit (values and working style)
- "Why" questions (motivation and fit)

**Output:** `applications/{role-slug}/interviewer-perspective.md`

---

## 3. Mock Interview Simulation

**What you need:** Interview prep document, interview type, persona preference
**Load:** @references/mock-interview.md

Realistic interview practice:
- Interviewer personas: recruiter, hiring manager, technical, panel, executive
- Simulated interview with realistic questions and follow-ups
- Real-time or end-of-session feedback
- STAR compliance checking
- Difficult modes: silent, sceptical, rapid-fire
- Comprehensive debrief with improvement recommendations

**Output:** Feedback in conversation; can update interview prep document with learnings

---

## 4. Post-Interview Coaching & Recovery

**What you need:** CV + job description + interview recollection + any feedback received
**Load:** @references/post-interview-coaching.md
**Template:** @references/post-interview-debrief-template.md

**Stage-Specific Diagnosis:**
- WHERE rejection occurred (Application, Recruiter Screen, HM Screen, Technical, Final)
- Each stage filters for different things - diagnosis adapts

**Gap Analysis:**
- **Skill Gap** - Missing core capability (fixable with training)
- **Signal Gap** - Strong background but poor framing (fixable with practice)
- **Fit/Timing Gap** - Right person, wrong moment (often external factors)

**Future Skills Alignment (WEF 2025):**
- Cross-references gaps against World Economic Forum Future of Jobs 2025 report
- Prioritises development by role need AND future demand

**Wellbeing & Resilience:**
- Calibrated to rejection severity
- Normalises rejection with data (6-10 rejections average before offer)
- "What's Still True" evidence anchor from CV
- Pattern tracking across multiple rejections

**Output:** `applications/{role-slug}/post-interview-debrief.md`

**Suggested next steps:**
- Skill gap? "Want me to help update your CV to address this?"
- Signal gap? "Shall we refine your interview prep stories?"
- Fit/timing? "Let's identify similar roles at competitor companies"

---

## 5. Reference & Referee Prep

**What you need:** The role and what it values + who you are considering as referees + any constraints (current employer, difficult last manager, first job)
**Load:** @references/referee-prep.md
**Template:** @references/referee-prep-template.md

Prepare your references before you are asked, usually at late interview or offer stage:
- Choose referees who are credible and relevant to this specific role
- Ask permission well, in a way that lets a lukewarm referee decline gracefully
- Brief each referee on what this role values and the verified examples they witnessed
- Handle common constraints: a current employer who cannot be contacted yet, a UK factual-only reference policy, a difficult last manager, or a first job with no prior employer
- Anticipate the questions referees are typically asked, including the more formal checks for regulated and safeguarding roles

All referee details come from you; nothing is invented. Briefs match verified shared history, never coaching exaggeration.

**Output:** `applications/{role-slug}/referee-prep.md`

**Suggested next steps:**
- "Want me to draft the brief to send each referee?"
- "Ready for the offer and negotiation stage?" (route to `/career-navigator`)

---

## Application Folder

All role-specific outputs are saved in `applications/{role-slug}/`. When running any capability for a role, check if the folder exists first using Glob. If it doesn't, create it when saving the first output. If a research brief or CV already exists in the folder from a previous skill run, use those to inform interview preparation.

---

## Career Stage Adaptation

This skill adapts advice based on your career stage:
- **Early Career** - Building presence, demonstrating potential
- **Mid-Career** - Pivots, IC-to-management transitions, explaining gaps
- **Experienced** - Age discrimination mitigation, tech fluency signals, ageism support (law, strategies, emotional resilience)
- **Late Career** - Ageism handling, fractional/advisory positioning, ageism support (law, strategies, emotional resilience)

---

## Persona Adaptation

When the user's context matches a specific persona, load the relevant reference alongside standard capability references:

| Persona | Load Reference | Trigger |
|:--------|:--------------|:--------|
| Career Returner | @references/career-returner-interview-prep.md | User mentions career break, returning to work, redundancy, maternity/paternity |
| Early Career | @references/early-career-interview-prep.md | User is a graduate, apprentice, school leaver, or attending first professional interviews |
| NED | @references/ned-interview-prep.md | User is preparing for a board interview or nomination committee meeting |
| Fractional | @references/fractional-discovery-prep.md | User is preparing for a client discovery call or fractional engagement pitch |
| Ageism / Age Discrimination | @references/ageism-in-employment.md + @references/age-discrimination-strategies.md + @references/emotional-support-resilience.md | User mentions age discrimination, ageism, being "too old", being "overqualified" as age proxy, long service redundancy (20+ years), feeling their age is held against them, younger candidates being preferred, or age-related rejection patterns |

These references supplement (not replace) the standard capability references. Load both the persona reference and the standard one.

### Ageism Persona: Additional Guidance

When the ageism persona is triggered, load ALL THREE ageism references alongside the standard capability reference (e.g., post-interview-coaching.md for Capability 4). The three references serve distinct purposes:

| Reference | Purpose | When Most Relevant |
|:----------|:--------|:-------------------|
| **ageism-in-employment.md** | UK law (Equality Act 2010), rights, tribunal process, practical reality of proving discrimination, whistleblowing routes, evidence gathering | When the user wants to understand their legal position or is considering whether to pursue a complaint |
| **age-discrimination-strategies.md** | Practical CV strategies, interview tactics, digital presence, skills to update, age-friendly employers, networking | When helping the user strengthen their approach and reduce age bias exposure in future applications |
| **emotional-support-resilience.md** | Psychological impact, identity crisis after long service, NHS and charity support, resilience strategies, crisis contacts, cognitive reframing | When the user is emotionally distressed, processing redundancy grief, or showing signs of withdrawal or confidence erosion |

**Tone calibration for ageism:** This is an area where candidates are particularly vulnerable. The emotional impact of being told you are too old, explicitly or implicitly, is uniquely corrosive because age cannot be changed. Calibrate your response to acknowledge this reality before moving to practical advice. Do not rush past the emotional dimension. Equally, do not dwell so long that you reinforce hopelessness. The goal is: validate, inform, equip, and mobilise.

---

## Output Standards

- **UK English** throughout (unless US role explicitly requires)
- **No emojis** - Professional tone appropriate for target role
- **Evidence-backed** - Answers reference your actual CV
- **STAR format** - Behavioural answers use Situation, Task, Action, Result
- **Role-specific** - Questions tailored to the actual role, not generic

### Tone of Voice
- Address the user as "you", not by name: "You should prepare for..." not "Bethan should prepare for..."; default to second person for warmth and engagement; occasional name use is fine for emphasis
- Avoid hyperbole and cinema poster phrasing (not "game-changing", "revolutionary", or "supercharge your career")
- Use the **Oxford comma** (serial comma: "skills, experience, and qualifications")
- Never use em dashes. Use commas, semicolons, colons, or full stops instead

### Template Usage

When a capability names a template, load it with the @ reference before writing, and follow its structure and footer. Users and other skills rely on the same headings appearing in the same places.

---

## Related Skills

- **/application-optimiser** - Research the company and optimise your CV first
- **/skills-radar** - A Gap rating in the competency map is the same evidence its gap analysis wants; run it when the same Gap recurs across interviews
- **/linkedin-coach** - Update your LinkedIn after interview learnings
- **/career-navigator** - Negotiate offers, evaluate multiple options

---

*Interview Master | Career Helper Plugin | Prosper AI Consulting, UK*
