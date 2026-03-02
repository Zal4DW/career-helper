---
name: career-navigator
description: This skill should be used when the user asks to "plan my job search", "build a networking strategy", "negotiate my salary", "evaluate a job offer", "compare offers", or "create a 3-month plan". Provides strategic networking intelligence, job search planning with wellbeing integration, salary negotiation coaching (UK/US/EU/APAC), and multi-offer evaluation frameworks.
tags: networking, salary, negotiation, offers, planning, job-search, strategy
---

# Career Navigator

Plan your search, build your network, and navigate offers.

## Capabilities

| # | Capability | When to Use |
|:--|:-----------|:------------|
| 1 | Strategic Networking | Identifying who to connect with at target companies |
| 2 | 3-Month Job Search Plan | Structuring your entire job search |
| 3 | Salary Negotiation | After receiving an offer |
| 4 | Offer Evaluation | Comparing multiple offers or evaluating a single one |

## Quick Start

```
"Who should I connect with at [Company]?"
"Help me create a 3-month job search plan"
"I got an offer - help me negotiate"
"I have multiple offers - help me decide"
```

---

## 1. Strategic Networking Intelligence

**What you need:** Company name + target role + your background/LinkedIn
**Load:** @references/networking-strategy.md
**Template:** @references/networking-intelligence-template.md

Agentic parallel research to identify high-value connections:
- Hiring managers and direct team members
- Internal recruiters and talent acquisition
- Executive stakeholders and decision makers
- Company alumni who share your background
- Mutual connection paths for warm introductions
- Personalised connection strategies and message templates
- Timing and sequencing guidance

Uses parallel WebSearch to find 8-12 strategic people, prioritised in 3 tiers.

**Output:** `{role-slug}-networking-intelligence.md`

---

## 2. 3-Month Job Search Plan

**What you need:** Career stage, current situation, target direction, constraints, existing materials
**Load:** @references/three-month-plan.md
**Template:** @references/three-month-plan-template.md

Comprehensive activity planning:
- Define 3-4 audacious but achievable Month 3 goals
- Back-solve into Month 2 and Month 1 milestones
- 12-week breakdown with specific focus areas
- Daily rhythm template adapted to career level
- Weekly task checklists (recurring and one-time)
- Wellbeing practices integrated throughout
- Progress tracking metrics and reflection prompts
- UK-specific resources and support
- Generational adaptations (Gen Z to Boomers)

**Approach:** Collaborative, human-in-the-loop planning. Professional but warm tone. Acknowledges emotional reality of job searching.

**Output:** `three-month-plan.md`

---

## 3. Salary Negotiation Coach

**What you need:** Offer details, target region (UK/US/EU/APAC), competing offers (if any), priorities
**Load:** @references/salary-negotiation.md
**Template:** @references/negotiation-strategy-template.md

Region-aware negotiation coaching:
- Market compensation research via WebSearch
- Leverage assessment and positioning strategy
- Counter-offer scripts (phone, email, in-person)
- Total compensation framework (base, bonus, equity, pension, benefits)
- Common objection handling
- Risk assessment (when to push, when to accept)
- Acceptance and decline templates

**Regional Adaptations:**
- UK: Pension contributions, notice periods, garden leave, bonus timing
- US: Equity/RSUs, health insurance value, 401k match, signing bonus
- EU: Mandatory benefits, works councils, 13th month salary
- APAC: Variable bonus structures, housing allowances

**Output:** `{role-slug}-negotiation-strategy.md`

---

## 4. Offer Evaluation Framework

**What you need:** Offer details, current situation, career priorities, region
**Load:** @references/offer-evaluation.md
**Template:** @references/offer-evaluation-template.md

Comprehensive offer analysis:
- Total compensation normalisation (currency, CoL, tax, benefits)
- Career trajectory analysis for each option
- Culture and fit assessment
- Risk evaluation (company health, role clarity)
- Weighted decision matrix based on your priorities
- Intuition check and regret minimisation framework
- Scenario planning (best/likely/worst cases)

**Output:** `offer-evaluation.md`

---

## Career Stage Adaptation

**Load:** @references/career-stage-context.md

This skill adapts advice based on your career stage:
- **Early Career (Gen Z/Alpha)** - Building presence, demonstrating potential, portfolio emphasis
- **Mid-Career (Millennials)** - Career pivots, IC-to-management transitions, explaining gaps
- **Experienced (Gen X)** - Age discrimination mitigation, tech fluency signals
- **Late Career (Boomers)** - Ageism handling, fractional/advisory positioning, board opportunities

When the user mentions age, experience level, or stage-related concerns, load career-stage-context.md to adapt all advice.

---

## Persona Adaptation

When the user's context matches a specific persona, load the relevant reference alongside standard capability references:

| Persona | Load Reference | Trigger |
|:--------|:--------------|:--------|
| Career Returner | @references/career-returner-strategy.md | User mentions career break, returning to work, redundancy, maternity/paternity, caregiving |
| Early Career | @references/early-career-search-strategy.md | User is a graduate, apprentice, school leaver, or searching for their first professional role |
| NED | @references/ned-search-strategy.md | User seeks board roles, NED positions, governor or trustee appointments |

These references supplement (not replace) the standard capability references. Load both the persona reference and the standard one.

---

## Output Standards

- **UK English** throughout (unless US role explicitly requires)
- **No emojis** - Professional tone
- **Cited sources** - Research includes URLs and access dates
- **Quantified metrics** - Specific numbers, percentages, timeframes
- **Region-aware** - Adapt to UK, US, EU, or APAC as needed
- **Actionable** - Clear next steps, not just analysis

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

- **/application-optimiser** - Research companies and optimise your CV
- **/linkedin-coach** - Optimise your LinkedIn profile and content
- **/interview-master** - Prepare for interviews
- **/career-transitions** - Explore portfolio/fractional career paths

---

*Career Navigator v1.3.0 | Career Helper Plugin | Prosper AI Consulting, UK*
