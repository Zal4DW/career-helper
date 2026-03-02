---
name: application-optimiser
description: This skill should be used when the user asks to "optimise my CV", "fix my CV", "improve my CV", "tailor my CV for ATS", "research a company", "help me apply for a role", or "plan my application". Provides ATS-optimised CV rewriting, company and role research with parallel intelligence gathering, and application strategy planning.
tags: cv, ats, resume, company, research, application, strategy
---

# Application Optimiser

Research companies, optimise your CV for ATS systems, and plan your application strategy.

## Capabilities

| # | Capability | When to Use |
|:--|:-----------|:------------|
| 1 | Company Research | Before applying or interviewing at a target company |
| 2 | CV/ATS Optimisation | Tailoring your CV for a specific role |
| 3 | Application Strategy | Planning your full application approach |

## Quick Start

```
"Research [Company] before I apply"
"Help me optimise my CV for this job description"
"Plan my application to [Company] for [Role]"
```

---

## 1. Company & Role Research

**What you need:** Company name, job description (optional but helpful)
**Load:** @references/company-research.md
**Template:** @references/research-brief-template.md

Agentic parallel research covering:
- Company fundamentals, leadership, financial health
- Market position, competitors, strategic direction
- Culture, employee experience (Glassdoor analysis)
- Hiring context and team structure
- People intelligence (hiring manager, key stakeholders)
- Red flags and risk assessment

Uses parallel WebSearch, WebFetch, and Task tool for comprehensive intelligence.

**Output:** `{role-slug}-research-brief.md`

---

## 2. CV Optimisation for ATS

**What you need:** Your current CV + target job description
**Load:** @references/ATS-Helper.md
**Templates:**
- @references/cv-template.md for CV output
- @references/application-strategy-template.md for LinkedIn sync notes

NLP and recruitment AI specialist approach:
- Keyword and concept extraction from job description
- ATS-safe CV rewrite with quantified achievements
- Keyword coverage analysis (target: 70%+ of JD terms)
- LinkedIn API consistency checks
- Formatting and parsing safety verification

**Output:**
- `{role-slug}-cv-optimized.md`
- `{role-slug}-linkedin-updates.md` (LinkedIn sync recommendations)

---

## 3. Application Strategy & Timeline

**What you need:** Research brief + optimised CV + timeline constraints
**Template:** @references/application-strategy-template.md

Comprehensive planning:
- Timeline and milestone planning
- Stakeholder mapping and connection strategy
- Risk mitigation for identified gaps
- Follow-up protocols and decision framework
- Cover letter approach

**Output:** `{role-slug}-application-strategy.md`

---

## Deep Research Validation

All research uses a rigorous multi-cycle validation workflow:
**Load:** @references/deep-research-reflection.md

- **Gap Analysis** - After initial search, identify what's missing
- **Counter-Evidence Search** - Actively search for contradicting information
- **Source Credibility Scoring** - SEC filings > news > Glassdoor > blogs
- **Red Flag Hunting** - Proactively search for negative information
- **Citation Requirements** - All factual claims include source URLs and access dates

## Reflective Validation

After generating content, validate before presenting:
**Load:** @references/reflect-validate.md

**For CV/ATS:** Keyword coverage 70%+? Achievements quantified? ATS-safe formatting?
**For Research:** All claims cited? Sources recent (<12mo)? All sections present?

```
Generate -> Evaluate -> If NEEDS_IMPROVEMENT -> Refine -> Re-evaluate (max 3 iterations)
```

---

## Persona Adaptation

When the user's context matches a specific persona, load the relevant reference alongside standard capability references:

| Persona | Load Reference | Trigger |
|:--------|:--------------|:--------|
| Career Returner | @references/career-returner-cv-guide.md | User mentions career break, returning to work, redundancy, maternity/paternity, illness, caregiving |
| Early Career | @references/early-career-cv-template.md | User is a graduate, apprentice, school leaver, or has limited professional experience |
| NED | @references/ned-cv-template.md | User seeks board roles, NED positions, governor or trustee appointments |
| Fractional | @references/fractional-cv-template.md | User is going fractional, portfolio, or independent consulting |

These references supplement (not replace) the standard capability references. Load both the persona reference and the standard one.

---

## Output Standards

- **UK English** throughout (unless US role explicitly requires US English)
- **No emojis** - Professional tone
- **Cited sources** - All research includes URLs and access dates
- **Quantified metrics** - Specific numbers, percentages, timeframes
- **ATS-safe** - Simple formatting, conventional headings, consistent dates
- **Never invent data** - Mark missing info as `[MISSING]`

### Tone of Voice
- Avoid hyperbole and cinema poster phrasing (not "game-changing", "revolutionary", or "supercharge your career")
- Use the **Oxford comma** (serial comma: "skills, experience, and qualifications")
- Never use em dashes. Use commas, semicolons, colons, or full stops instead

### Template Usage

When a capability specifies a template, you MUST:
1. Load the template first using @ symbol
2. Follow the template structure exactly
3. Preserve template footers

### Working with Blocked Content

When WebFetch fails (LinkedIn, Glassdoor, paywalled content):
- Ask user to screenshot the page (Read tool processes images)
- Or copy/paste text directly
- Or save as PDF and provide path
- Only request screenshots for critical content (top 3-5 items)

---

## Related Skills

After optimising your application:
- **/linkedin-coach** - Update your LinkedIn to match your CV
- **/interview-master** - Prepare for interviews at this company
- **/career-navigator** - Build networking strategy and plan your search

---

*Application Optimiser v1.3.0 | Career Helper Plugin | Prosper AI Consulting, UK*
