---
name: application-optimiser
description: This skill should be used when the user asks to "optimise my CV", "fix my CV", "improve my CV", "tailor my CV for ATS", "research a company", "help me apply for a role", "plan my application", "make a PDF of my CV", or "get my CV ready to upload". Provides ATS-optimised CV rewriting, company and role research with parallel intelligence gathering, application strategy planning, and verified CV PDF production with layout and ATS text-layer checks.
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
| 4 | Cover Letter | Writing a cover letter, supporting statement, or application message |
| 5 | CV PDF Production | Turning the finished CV or letter into a verified, submission-ready PDF |

## Quick Start

```text
"Research [Company] before I apply"
"Help me optimise my CV for this job description"
"Plan my application to [Company] for [Role]"
"Write a cover letter for this role"
"Help me with the supporting statement for this application"
"Make me a PDF of my CV I can upload"
```

---

## Accessibility

**At skill start**, check for `career-helper-preferences.md` in the current working directory using the Glob tool. If found, read the YAML frontmatter and apply:

- **dyslexia_friendly: true** → Use short sentences. Number all lists and options (never unnumbered). One decision per message. No idioms or metaphors — use plain replacements. Explicit signposting at every transition ("Step 2 of 4. Next: CV optimisation."). Refer to saved files by description, not filename. Repeat key details (company names, role titles, dates) — do not assume the user remembers from earlier messages.
- **colour_blind: true** → Never use colour alone to convey meaning. Use labels, text, or icons for all status indicators.

If **no preferences file exists** and this skill was invoked directly (not dispatched by Tim): ask once — "Do you have any accessibility preferences I should know about? For example, if you're dyslexic I can adjust how I format things." If yes, save to `career-helper-preferences.md` using the format documented in the Tim skill before continuing. If the user declines or says no, proceed without creating the file.

These rules apply to **all communication with the user** and to the **formatting of output documents**.

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

**Output:** `applications/{role-slug}/research-brief.md`

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
- `applications/{role-slug}/cv-optimised.md`
- `applications/{role-slug}/linkedin-updates.md` (LinkedIn sync recommendations)

---

## 3. Application Strategy & Timeline

**What you need:** Research brief + optimised CV + timeline constraints
**Template:** @references/application-strategy-template.md

Comprehensive planning:
- Timeline and milestone planning
- Stakeholder mapping and connection strategy
- Risk mitigation for identified gaps
- Follow-up protocols and decision framework
- Cover letter approach (for a full draft, use Capability 4)

**Output:** `applications/{role-slug}/application-strategy.md`

---

## 4. Cover Letter & Supporting Statement

**What you need:** Job description + your CV (or master facts) + research brief if one exists + your own reasons for wanting the role
**Load:** @references/cover-letter.md
**Template:** @references/cover-letter-template.md

Drafts a cover letter, competency-based supporting statement, or short application message, with every claim traceable to verified content:
- Confirms which format the application actually requires before drafting
- Mirrors job-description language only where the underlying fact genuinely matches
- Sources motivation from you, never inventing reasons you care about the organisation
- Addresses overqualification, career change, or gaps honestly where the CV cannot
- Runs the same anti-hallucination guardrails and reflective validation as CV work

**Output:**
- `applications/{role-slug}/cover-letter.md` (full letter)
- `applications/{role-slug}/supporting-statement.md` (competency-based applications)

---

## 5. CV PDF Production

**What you need:** A finished `cv-optimised.md` (or cover letter) with no unfilled placeholders
**Load:** @references/cv-pdf-production.md
**Scripts:** `scripts/generate_cv_pdf.py` and `scripts/verify_cv_pdf.py`

A generate-verify loop, never generate-and-hope:
- Renders the markdown to a deliberately plain, single-column, ATS-safe PDF (three themes: standard, compact, relaxed)
- Extracts the PDF text layer the way parsing software reads it, and fails if content did not survive
- Flags documents over the page limit rather than shrinking the font
- Renders each page to an image for visual inspection: orphaned headings, overflow, cramped spacing
- Fix problems in the markdown and regenerate; a PDF is never hand-edited
- HTML fallback when WeasyPrint is unavailable; verification applies whatever produced the PDF

**Output:** `applications/{role-slug}/cv.pdf` (and `cover-letter.pdf` when requested)

---

## Application Folder

All role-specific outputs are saved in `applications/{role-slug}/`. When running any capability for a role, check if the folder exists first using Glob. If it doesn't, create it when saving the first output. The `{role-slug}` is derived from the role title and company (e.g., "Marketing Manager at Greenfield & Co" becomes `marketing-manager-greenfield`).

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
- Address the user as "you", not by name, in coaching and strategy content: "Your CV highlights..." not "Bethan's CV highlights..." — default to second person for warmth and engagement; occasional name use is fine for emphasis. (CVs themselves are naturally written in third person about the candidate)
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

*Application Optimiser v1.5.0 | Career Helper Plugin | Prosper AI Consulting, UK*
