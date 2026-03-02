---
name: interview-master
description: This skill should be used when the user asks to "prepare for an interview", "do a mock interview", "what do interviewers look for", "I got rejected", "help me after an interview", "I think I was rejected because of my age", "ageism", "age discrimination", or "I'm being told I'm overqualified". Provides interview preparation with STAR frameworks, interviewer perspective reports, realistic mock interview simulation, post-interview coaching for rejection recovery, and comprehensive ageism support including UK law, practical strategies, and emotional resilience.
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

## Quick Start

```
"I have an interview at [Company] next week"
"What are interviewers really looking for?"
"Let's do a mock interview"
"I just got rejected - help me understand what happened"
"I think I was rejected because of my age"
"I keep getting told I'm overqualified - what can I do?"
"I was made redundant after 25 years and I'm struggling"
```

---

## 1. Interview Preparation

**What you need:** CV + job description + company name + interview stage
**Load:** @references/interview-prep.md
**Template:** @references/interview-prep-template.md

Role-specific preparation:
- 15-20 likely questions (behavioural, technical, situational, company-specific)
- STAR answer frameworks using your actual experience
- Interviewer's perspective for each question
- 5-7 pre-prepared adaptable stories
- 8-10 intelligent questions to ask (by interviewer type)
- Talking points, concern mitigation, execution tips
- Post-interview follow-up templates

All answers cite your real experience with evidence.

**Output:** `{role-slug}-interview-prep.md`

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

**Output:** `{role-slug}-interviewer-perspective.md`

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

**Output:** `{role-slug}-post-interview-debrief.md`

**Suggested next steps:**
- Skill gap? "Want me to help update your CV to address this?"
- Signal gap? "Shall we refine your interview prep stories?"
- Fit/timing? "Let's identify similar roles at competitor companies"

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
- Avoid hyperbole and cinema poster phrasing (not "game-changing", "revolutionary", or "supercharge your career")
- Use the **Oxford comma** (serial comma: "skills, experience, and qualifications")
- Never use em dashes. Use commas, semicolons, colons, or full stops instead

### Template Usage

When a capability specifies a template, you MUST:
1. Load the template first using @ symbol
2. Follow the template structure exactly
3. Preserve template footers

---

## Related Skills

- **/application-optimiser** - Research the company and optimise your CV first
- **/linkedin-coach** - Update your LinkedIn after interview learnings
- **/career-navigator** - Negotiate offers, evaluate multiple options

---

*Interview Master v1.4.0 | Career Helper Plugin | Prosper AI Consulting, UK*
