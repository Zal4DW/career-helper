---
name: interview-master
description: Interview preparation with role-specific questions and STAR frameworks, interviewer perspective reports showing what they really assess, realistic mock interview simulation with multiple personas, and post-interview coaching for rejection recovery. Use when preparing for interviews, understanding interviewer thinking, practising with mock interviews, or recovering from rejections.
tags: interview, preparation, mock, practice, rejection, coaching, star
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
```

---

## 1. Interview Preparation

**What you need:** CV + job description + company name + interview stage
**Load:** @supporting-prompts/interview-prep.md
**Template:** @templates/interview-prep-template.md

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
**Load:** @supporting-prompts/interviewer-perspective-guide.md
**Template:** @templates/interviewer-perspective-template.md

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
**Load:** @supporting-prompts/mock-interview.md

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
**Load:** @supporting-prompts/post-interview-coaching.md
**Template:** @templates/post-interview-debrief-template.md

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
- **Experienced** - Age discrimination mitigation, tech fluency signals
- **Late Career** - Ageism handling, fractional/advisory positioning

---

## Output Standards

- **UK English** throughout (unless US role explicitly requires)
- **No emojis** - Professional tone appropriate for target role
- **Evidence-backed** - Answers reference your actual CV
- **STAR format** - Behavioural answers use Situation, Task, Action, Result
- **Role-specific** - Questions tailored to the actual role, not generic

### Template Usage

When a capability specifies a template, you MUST:
1. Load the template first using @ symbol
2. Follow the template structure exactly
3. Preserve template footers

---

## Related Skills

- **/application-optimizer** - Research the company and optimise your CV first
- **/linkedin-coach** - Update your LinkedIn after interview learnings
- **/career-navigator** - Negotiate offers, evaluate multiple options

---

*Interview Master v1.0.0 | Career Helper Plugin | Prosper AI Consulting, UK*
