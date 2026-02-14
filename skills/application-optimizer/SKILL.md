---
name: application-optimizer
description: ATS-optimised CV rewriting, company and role research with agentic parallel intelligence gathering, and application strategy planning. Use when tailoring CVs for ATS systems, researching target companies, or planning comprehensive application approaches.
tags: cv, ats, resume, company, research, application, strategy
---

# Application Optimizer

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
**Load:** @supporting-prompts/company-research.md
**Template:** @templates/research-brief-template.md

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
**Load:** @supporting-prompts/ATS-Helper.md
**Templates:**
- @templates/cv-template.md for CV output
- @templates/application-strategy-template.md for LinkedIn sync notes

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
**Template:** @templates/application-strategy-template.md

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
**Load:** @supporting-prompts/deep-research-reflection.md

- **Gap Analysis** - After initial search, identify what's missing
- **Counter-Evidence Search** - Actively search for contradicting information
- **Source Credibility Scoring** - SEC filings > news > Glassdoor > blogs
- **Red Flag Hunting** - Proactively search for negative information
- **Citation Requirements** - All factual claims include source URLs and access dates

## Reflective Validation

After generating content, validate before presenting:
**Load:** @supporting-prompts/reflect-validate.md

**For CV/ATS:** Keyword coverage 70%+? Achievements quantified? ATS-safe formatting?
**For Research:** All claims cited? Sources recent (<12mo)? All sections present?

```
Generate -> Evaluate -> If NEEDS_IMPROVEMENT -> Refine -> Re-evaluate (max 3 iterations)
```

---

## Output Standards

- **UK English** throughout (unless US role explicitly requires US English)
- **No emojis** - Professional tone
- **Cited sources** - All research includes URLs and access dates
- **Quantified metrics** - Specific numbers, percentages, timeframes
- **ATS-safe** - Simple formatting, conventional headings, consistent dates
- **Never invent data** - Mark missing info as `[MISSING]`

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

*Application Optimizer v1.0.0 | Career Helper Plugin | Prosper AI Consulting, UK*
