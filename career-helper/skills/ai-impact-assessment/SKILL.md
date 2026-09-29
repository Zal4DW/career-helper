---
name: ai-impact-assessment
description: Use when the user is worried about or curious how AI and automation will affect their current or target role. Runs a live research assessment of whether the role faces material AI disruption in the next 12 months, then gives a frank verdict and a 6-month mitigation plan.
tags: ai-impact, automation, disruption, future-proofing, career-risk, mitigation, ai-jobs
---

# AI Impact Assessment

An honest assessment of whether AI will materially change your role in the next 12 months, followed by a practical plan to stay ahead.

## Capabilities

| # | Capability | When to Use |
|:--|:-----------|:------------|
| 1 | AI Impact Assessment | You want to know if your role is at risk from AI and what to do about it |

## Quick Start

```
"Will AI affect my job as a [role]?"
"Is my role at risk from automation?"
"How will AI change marketing/finance/engineering jobs?"
"Should I be worried about AI replacing my role?"
"I'm applying for [role] - is it future-proof?"
```

---

## Accessibility

**At skill start**, check for `career-helper-preferences.md` in the current working directory using the Glob tool. If found, read the YAML frontmatter and apply:

- **dyslexia_friendly: true** → Use short sentences. Number all lists and options (never unnumbered). One decision per message. No idioms or metaphors; use plain replacements. Explicit signposting at every transition. Refer to saved files by description, not filename. Repeat key details (role titles, company names); do not assume the user remembers from earlier messages.
- **colour_blind: true** → Never use colour alone to convey meaning. Use labels, text, or icons for all status indicators. Risk levels must use text labels (e.g. "HIGH RISK"), not colour coding.

If **no preferences file exists** and this skill was invoked directly (not dispatched by Tim): ask once, "Do you have any accessibility preferences I should know about? For example, if you're dyslexic I can adjust how I format things." If yes, save to `career-helper-preferences.md` using the format in `${CLAUDE_PLUGIN_ROOT}/skills/tim/references/tim-preferences-format.md` before continuing. If the user declines or says no, proceed without creating the file.

These rules apply to **all communication with the user** and to the **formatting of output documents**.

---

## 1. AI Impact Assessment

**What you need:** Your current role or target role(s), industry, and ideally your CV or a description of your day-to-day responsibilities
**Load:** `references/ai-impact-research.md`
**Load:** `references/assessment-and-plan.md`
**Template:** `references/ai-impact-template.md`

This skill runs in two phases:

**Phase 1: Research (runs in extended thinking, not shown to user)**
- Gathers everything known about the user from conversation context, CV, and prior skill outputs in the working folder
- Runs targeted WebSearch queries against the user's specific role(s) and industry
- Cross-references credible sources: WEF Future of Jobs, McKinsey, ONS, Brookings, industry-specific reports
- Assesses which specific tasks and responsibilities face disruption vs which remain resilient
- Evaluates timeline and certainty level

**Phase 2: Assessment and Plan (visible to user)**
- Delivers a direct, evidence-based verdict on the user's role
- Identifies what is at risk, what is resilient, and the likely timeline
- Builds a 6-month month-by-month mitigation plan with specific actions
- Saves output file

**Important:** This assessment may be difficult for the user to hear. Be straightforward, empathetic, and pragmatic. Do not sugar-coat, but do not catastrophise. Open with facts, not reassurance. End with agency and a plan.

**Output:** `{role}-ai-impact-assessment.md`

---

## Output Standards

- **UK English** throughout
- **No emojis** - Professional tone
- **Cited sources** - All research includes URLs and access dates
- **Evidence-based** - Claims backed by specific data, not general impressions
- **Actionable** - Every finding links to a specific mitigation action
- **Current** - Research must use WebSearch for the latest data, not training knowledge alone

### Current Sources

Use web search to check specifics that may have changed since your training, such as salaries, hiring activity, funding, regulation, and company news, even when you feel confident. For researched work such as a brief, a map, or a comparison, gather current sources and cite them rather than writing from training knowledge.

### Tone of Voice

This skill requires particular care with tone:

- **Straightforward:** Do not hedge or bury bad news in qualifiers. If a role is at significant risk, say so clearly.
- **Empathetic:** Acknowledge that hearing your role may be disrupted is unsettling. "This is not easy to read, and it is reasonable to feel unsettled by it."
- **Not sycophantic:** Do not soften the message with false reassurance. "Your role is changing" is different from "you will be unemployed", but both need saying when true.
- **Pragmatic:** Every assessment ends with actions the user can take. The plan exists so they can act, not just worry.
- **Second person:** Address the user as "you", not by name: "Your role faces..." not "Bethan's role faces..."; default to second person for warmth and engagement; occasional name use is fine for emphasis
- Avoid hyperbole and cinema poster phrasing (not "game-changing", "revolutionary", or "supercharge your career")
- Use the **Oxford comma** (serial comma: "skills, experience, and qualifications")
- Never use em dashes. Use commas, semicolons, colons, or full stops instead

---

## Related Skills

After your assessment, consider:
- **/career-transitions** - AI readiness assessment and upskilling roadmap
- **/application-optimiser** - Research and apply for roles in growing areas
- **/linkedin-coach** - Reposition your profile for AI-resilient positioning
- **/career-navigator** - Build a structured plan if a career pivot is needed

---

*AI Impact Assessment | Career Helper Plugin | Prosper AI Consulting, UK*
