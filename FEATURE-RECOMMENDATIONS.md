# Career Helper: High-Value Feature Recommendations

**Analysis Date:** 30 December 2025
**Analyst:** Claude (Opus 4.5)
**Current Version:** 0.4.0

---

## Executive Summary

Career Helper is a comprehensive career coaching skill with 9 major capabilities covering the traditional job search journey. After thorough analysis of the codebase, current job market trends, and emerging career patterns, I've identified **15 high-value feature opportunities** across 5 strategic categories.

The most impactful additions focus on:
1. **Salary Negotiation** - Major gap in the current offering
2. **Non-Traditional Career Paths** - Fractional, portfolio, and entrepreneurial careers
3. **Enhanced LinkedIn Capabilities** - Video, skills verification, and engagement optimization
4. **AI Readiness & Skills Development** - Critical for 2025+ job market
5. **Advanced Interview Support** - Mock interviews and real-time coaching

---

## Regional Considerations

**Critical:** Many career features have significant regional variation. All new features must account for:

| Factor | Regional Variations |
|--------|---------------------|
| **Currency** | GBP (UK), EUR (EU), USD (USA), AUD/NZD (APAC), CAD (Canada) |
| **Salary Norms** | Annual vs monthly quoting; bonus structures; equity practices |
| **Tax & Benefits** | National Insurance (UK), Social Security (USA), mandatory benefits (EU) |
| **Employment Law** | Notice periods, garden leave, non-competes, redundancy |
| **Job Market Data** | Different sources per region; salary benchmarks vary |
| **Platform Usage** | LinkedIn dominant globally but local platforms matter (XING in DACH, Naukri in India) |
| **CV/Resume Format** | CV (UK/EU) vs Resume (USA); photo inclusion varies |
| **Negotiation Culture** | Acceptable tactics differ by region and industry |

**Implementation Principle:** All salary, compensation, and market-related features must:
- Ask for user's target region/market
- Adapt currency and formats accordingly
- Use region-appropriate data sources
- Respect local employment law context
- Default to UK English but adapt to US English for US roles

---

## Gap Analysis: What's Missing

### Current Coverage (Strong)
- LinkedIn profile optimization
- ATS CV optimization
- Company research
- Interview preparation (questions & STAR frameworks)
- Networking intelligence
- Post-rejection coaching
- Application strategy & timeline
- 3-month job search planning

### Critical Gaps Identified
| Gap | Impact | Notes |
|-----|--------|-------|
| **Salary negotiation** | Critical | 58% of job seekers don't negotiate; potential £10,000+ value |
| **Offer evaluation** | High | No framework for comparing multiple offers |
| **Fractional/portfolio careers** | High | Only covers traditional employment |
| **Entrepreneurial transitions** | High | No support for starting a consultancy |
| **LinkedIn video optimization** | Medium | New 30-second video feature not addressed |
| **Skills verification strategy** | Medium | LinkedIn's 2025 verified skills not covered |
| **AI readiness assessment** | High | No guidance on demonstrating AI competency |
| **Mock interview practice** | High | Prep exists, but no simulation mode |
| **Executive transition specifics** | Medium | C-suite moves have unique challenges |
| **Counter-offer navigation** | Medium | What to do when current employer counters |

---

## Recommended Features (Priority Ordered)

### TIER 1: High Impact, High Value

---

#### 1. Salary Negotiation Coach
**Priority:** Critical
**Effort:** Medium
**User Value:** Extremely High (potential £10,000+ / $15,000+ / €12,000+ impact per user)

**The Gap:**
Only 42% of job seekers negotiate their salary, yet 9 out of 10 succeed when they try. Current skill has zero coverage of this critical moment.

**Proposed Capability:**
```
When to use: After receiving a job offer
What you need: Offer details + target region + user priorities
Load: @supporting-prompts/salary-negotiation.md
Template: @templates/negotiation-strategy-template.md
```

**Features:**
- **Market compensation research** - WebSearch for salary bands by role/location/level (region-specific sources)
- **Leverage assessment** - Competing offers, unique skills, market demand analysis
- **Negotiation script generator** - Personalised scripts for phone, email, in-person (culturally adapted)
- **Counter-offer language** - Templates for base, bonus, equity, benefits, start date
- **Risk assessment** - When to push, when to accept, red flags that offer may be rescinded
- **Total compensation framework** - Evaluate beyond base: equity, pension, benefits, WFH, growth potential
- **Common objections** - How to handle "this is our final offer", "budget is fixed", etc.
- **Acceptance/decline templates** - Professional responses for either outcome

**Regional Adaptations:**
| Region | Considerations |
|--------|---------------|
| **UK** | Pension contributions, notice periods, garden leave, bonus timing |
| **USA** | Equity/RSUs, health insurance value, 401k match, signing bonus |
| **EU** | Mandatory benefits, works councils, 13th month salary, notice periods |
| **APAC** | Variable bonus structures, housing allowances, education benefits |

**Template Output:** `{role-slug}-negotiation-strategy.md`

---

#### 2. Offer Evaluation Framework
**Priority:** Critical
**Effort:** Low-Medium
**User Value:** High (prevents costly wrong decisions)

**The Gap:**
No structured way to compare multiple offers or evaluate a single offer against alternatives.

**Proposed Capability:**
```
When to use: Evaluating job offer(s)
What you need: Offer details + current situation + career priorities + region
```

**Features:**
- **Weighted decision matrix** - Customisable factors (comp, growth, culture, location, mission)
- **Total compensation calculator** - Normalise offers accounting for:
  - Currency conversion (if cross-border)
  - Cost of living adjustments
  - Tax implications by jurisdiction
  - Benefits value (pension, healthcare, equity)
- **Career trajectory analysis** - Which offer best positions for 3-5 year goals?
- **Culture fit scoring** - Based on prior company research
- **Risk assessment** - Startup vs established, industry trends, company health
- **Opportunity cost analysis** - What are you giving up? Counter-offer considerations

**Template Output:** `offer-evaluation.md`

---

#### 3. Portfolio & Fractional Career Support
**Priority:** High
**Effort:** High
**User Value:** High (36% of US workforce, 25% of UK workforce now gig/portfolio)

**The Gap:**
Career Helper assumes traditional full-time employment. No support for fractional executives, portfolio careers, or hybrid income models.

**Market Context:**
- 70+ million Americans in gig economy (36% of workforce)
- UK self-employment at 4.3 million (13% of workforce)
- EU freelance platforms growing 30%+ annually
- Fractional C-suite roles growing rapidly globally

**Proposed Capability:**
```
When to use: Considering or building a fractional/portfolio career
What you need: Skills inventory + income goals + time availability + target regions
Load: @supporting-prompts/portfolio-career.md
Template: @templates/portfolio-career-template.md
```

**Features:**
- **Portfolio career design** - Map multiple income streams and time allocation
- **Fractional executive positioning** - How to pitch for fractional CFO, CMO, CTO roles
- **Rate setting guidance** - Market rates by skill, experience, engagement type (region-specific)
- **Client pipeline building** - Networking for ongoing work, not one-time jobs
- **Contract considerations** - Retainer vs project, scope protection, payment terms (jurisdiction-specific)
- **Tax & structure basics** - Self-employment considerations by country
- **Portfolio CV format** - Different from traditional CV; emphasises versatility and outcomes
- **LinkedIn optimisation for fractional** - Profile that attracts multiple client types

**Regional Adaptations:**
| Region | Key Considerations |
|--------|-------------------|
| **UK** | IR35, limited company vs sole trader, NI implications |
| **USA** | 1099 vs W-2, self-employment tax, state variations |
| **EU** | VAT registration thresholds, cross-border invoicing, local regulations |
| **APAC** | Varies significantly by country; contractor vs employee classification |

**Template Output:** `portfolio-career-strategy.md`

---

#### 4. Entrepreneurial Transition Support
**Priority:** High
**Effort:** High
**User Value:** High (growing demand for career-to-founder paths)

**The Gap:**
Many mid-career and senior professionals consider starting a business or consultancy. No support for this transition.

**Proposed Capability:**
```
When to use: Considering transition from employment to entrepreneurship/consultancy
What you need: Expertise areas + financial runway + risk tolerance + target market
Load: @supporting-prompts/entrepreneurial-transition.md
Template: @templates/entrepreneurial-transition-template.md
```

**Features:**
- **Consultancy launch planning** - Packaging expertise into service offerings
- **Business model assessment** - Which model fits skills and goals
- **Financial runway analysis** - When to leap, how much buffer needed (currency-appropriate)
- **Personal brand to business brand** - Transitioning LinkedIn presence
- **First client acquisition strategy** - Leveraging existing network
- **Pricing strategy** - Value-based vs hourly, retainer structures (market-appropriate)
- **Risk mitigation** - Side hustle first? Pilot projects? Notice period planning
- **Legal/structural basics** - Entity types by jurisdiction, contracts, IP considerations

**Template Output:** `entrepreneurial-transition-plan.md`

---

### TIER 2: High Impact, Medium Effort

---

#### 5. LinkedIn Video Introduction Optimiser
**Priority:** Medium-High
**Effort:** Low
**User Value:** Medium-High (new LinkedIn feature, early adoption advantage)

**The Gap:**
LinkedIn now allows 30-second profile videos. This is a major differentiator but not covered by current skill.

**Proposed Capability:**
```
When to use: Creating or improving LinkedIn profile video
What you need: Target audience + key messages + career goals
```

**Features:**
- **Script generator** - 30-second elevator pitch tailored to goals
- **Structure framework** - Hook → Value proposition → Call to action
- **Delivery guidance** - Eye contact, pacing, background, lighting basics
- **Goal-specific variations** - Job seeker vs thought leader vs client acquisition
- **Review existing video** - Critique and improvement suggestions (via screenshot/description)

---

#### 6. AI Readiness & Skills Assessment
**Priority:** High
**Effort:** Medium
**User Value:** High (critical for 2025+ job market globally)

**The Gap:**
The 2025 job market requires demonstrating AI literacy. No current support for assessing or showcasing AI readiness.

**Market Context:**
- AI-related job postings grew 38% globally from 2020-2024
- Employers now expect AI literacy across all roles, all regions
- 54% of freelancers report advanced AI skills vs 38% of employees
- Entry-level white-collar roles declining; AI-augmented roles growing

**Proposed Capability:**
```
When to use: Assessing and improving AI readiness for job search
What you need: Current role + target roles + existing AI experience
Load: @supporting-prompts/ai-readiness.md
Template: @templates/ai-readiness-template.md
```

**Features:**
- **AI skills gap assessment** - What AI competencies does target role require?
- **AI experience inventory** - Help user articulate existing AI-adjacent work
- **Upskilling roadmap** - Specific skills and projects to build credibility
- **CV/LinkedIn AI integration** - How to weave AI capabilities into existing materials
- **Interview AI readiness prep** - Questions to expect about AI, frameworks to answer
- **Portfolio project ideas** - Demonstrable AI projects by domain

**Template Output:** `ai-readiness-plan.md`

---

#### 7. LinkedIn Skills Verification Strategy
**Priority:** Medium
**Effort:** Low
**User Value:** Medium-High (recruiter search visibility boost)

**The Gap:**
LinkedIn's 2025 skills verification feature (badges, assessments) not addressed.

**Proposed Capability:**
```
When to use: Optimising LinkedIn skills for recruiter visibility
What you need: Target roles + current skills list
```

**Features:**
- **Skill prioritisation matrix** - Which skills to verify based on role demand and recruiter searches
- **Assessment preparation** - LinkedIn's assessment format and study strategies
- **Certification integration** - How to upload/display verified certifications
- **Skills ordering strategy** - Top 3 skills for RSC API optimisation
- **Endorsement strategy** - Who to ask, how to reciprocate
- **Hidden gem skills** - Underrated skills that differentiate in your domain

---

#### 8. LinkedIn Engagement Optimiser
**Priority:** Medium-High
**Effort:** Medium
**User Value:** Medium-High (visibility multiplier)

**The Gap:**
Current content strategy focuses on posting. Engagement (commenting, reacting) often more impactful for visibility.

**Proposed Capability:**
```
When to use: Building visibility through strategic engagement
What you need: Target audience + time availability + content goals
```

**Features:**
- **Engagement target identification** - Who to follow and engage with strategically
- **Comment strategy** - How to write comments that get noticed (add value, not "Great post!")
- **Time-efficient engagement routine** - 15-30 min daily habits that compound
- **Engagement network building** - The 20-30 people who will amplify your content
- **DM strategy** - When to take conversations private, templates that convert
- **Event follow-up** - Post-conference, post-webinar connection sequences

---

#### 9. Mock Interview Simulation
**Priority:** High
**Effort:** Medium-High
**User Value:** High (practice is critical for performance)

**The Gap:**
Current interview prep generates questions and frameworks, but no simulation/practice mode.

**Proposed Capability:**
```
When to use: Practising before actual interview
What you need: Interview prep document + preferred interview type
Load: @supporting-prompts/mock-interview.md
```

**Features:**
- **Simulated interview mode** - Claude acts as interviewer, user responds
- **Real-time feedback** - Critique of answers as practice progresses
- **STAR compliance check** - Did answer follow STAR format?
- **Follow-up questions** - Realistic drilling down on initial responses
- **Difficult interviewer personas** - Practice with challenging styles (sceptical, rapid-fire, silent)
- **Time management** - Feedback on answer length and pacing
- **Confidence building** - Constructive feedback with encouragement

---

### TIER 3: Medium Impact, Strategic Value

---

#### 10. Executive Transition Specialist
**Priority:** Medium
**Effort:** Medium
**User Value:** High (for senior users)

**The Gap:**
C-suite transitions have unique challenges not covered by general career advice.

**Market Context:**
"Executives stepping into the 2025 job market face overlapping technological, organisational and cultural shifts... The capabilities that earned executives their C-suite promotion rarely match what the role actually demands."

**Proposed Capability:**
```
When to use: C-suite or VP-level transitions
What you need: Current level + target roles + transition type + target regions
Load: @supporting-prompts/executive-transition.md
Template: @templates/executive-transition-template.md
```

**Features:**
- **Executive search process navigation** - How retained search differs from job boards
- **Board and investor relationship prep** - Unique to C-suite transitions
- **Reference orchestration** - Strategic reference selection for executive roles
- **Equity negotiation specifics** - Options, RSUs, cliff, acceleration clauses (region-specific)
- **First 100 days planning** - Executive onboarding blueprint
- **Leadership brand positioning** - Thought leadership at executive level
- **Confidential search guidance** - How to search while employed at senior levels

**Template Output:** `executive-transition-brief.md`

---

#### 11. Counter-Offer Navigator
**Priority:** Medium
**Effort:** Low
**User Value:** High (common, high-stakes scenario)

**The Gap:**
No guidance for when current employer makes a counter-offer.

**Proposed Capability:**
```
When to use: Current employer counters after resignation
What you need: Counter details + original reasons for leaving + new offer details
```

**Features:**
- **Counter-offer analysis framework** - Why most counter-accepts fail within 18 months
- **Decision matrix** - Money vs underlying issues assessment
- **Conversation scripts** - How to decline gracefully
- **Bridge-burning prevention** - Leaving on good terms regardless of decision
- **Legal considerations** - Notice period, garden leave, non-compete (jurisdiction-specific)

---

#### 12. Career Pivot Advisor
**Priority:** Medium
**Effort:** Medium
**User Value:** High (growing need for career pivots)

**The Gap:**
Current skill optimises for same-field progression. No support for major career pivots.

**Proposed Capability:**
```
When to use: Considering significant career change (new industry/function)
What you need: Current background + target direction + constraints
Load: @supporting-prompts/career-pivot.md
Template: @templates/career-pivot-template.md
```

**Features:**
- **Transferable skills mapping** - Bridge current experience to new field
- **Skill gap analysis** - What's needed for credible pivot
- **Bridge role identification** - Intermediate steps that build credibility
- **Credibility building plan** - Projects, certifications, volunteering to demonstrate commitment
- **Pivot CV formatting** - Functional vs chronological, highlighting transferable skills
- **Story crafting** - Narrative that makes pivot logical, not random
- **Network pivot strategy** - Building connections in new field

**Template Output:** `career-pivot-plan.md`

---

#### 13. Remote/Hybrid Optimisation
**Priority:** Medium
**Effort:** Low
**User Value:** Medium (work pattern optimisation)

**The Gap:**
No specific guidance for targeting remote/hybrid roles or optimising for distributed work.

**Proposed Capability:**
```
When to use: Prioritising remote work or optimising remote search
What you need: Location preferences + time zone + remote experience
```

**Features:**
- **Remote-friendly company identification** - Research company remote policies
- **Remote work CV optimisation** - Highlighting remote-relevant skills
- **Time zone strategy** - How to position for async-friendly or specific TZ roles
- **Remote interview preparation** - Technical setup, virtual presence
- **Remote culture assessment** - Questions to evaluate remote-friendliness
- **Cross-border considerations** - Tax, visa, employment law implications

---

#### 14. Career Insurance (Continuous Profile Maintenance)
**Priority:** Low-Medium
**Effort:** Low
**User Value:** Medium (proactive career management)

**The Gap:**
Skill is reactive (activated during job search). No proactive career maintenance mode.

**Proposed Capability:**
```
When to use: Not actively searching, but maintaining career readiness
What you need: Current role + career trajectory + industry
```

**Features:**
- **Quarterly review checklist** - What to update even when not searching
- **Achievement capture template** - Log wins throughout the year for future CV updates
- **Network maintenance calendar** - Keep warm connections active
- **Skills evolution tracking** - What's changing in your field, what to learn next
- **Market position check** - Are you still competitive? Salary benchmarking
- **Passive opportunity signals** - How to attract recruiters while employed

---

#### 15. Reference Strategy & Orchestration
**Priority:** Low-Medium
**Effort:** Low
**User Value:** Medium

**The Gap:**
No guidance on reference selection, preparation, or orchestration.

**Proposed Capability:**
```
When to use: Preparing references for job search
What you need: Reference list + target roles
```

**Features:**
- **Reference portfolio design** - Mix of reference types for different needs
- **Reference preparation scripts** - What to tell references before calls
- **Reference-role matching** - Which reference for which role/question type
- **Reference request templates** - Professional ask messages
- **Reference refresh guidance** - Re-engaging dormant references
- **Reference red flags** - When NOT to use someone as a reference

---

## Implementation Recommendations

### Phase 1: Quick Wins (1-2 features)
1. **Salary Negotiation Coach** - Highest user value, fills critical gap
2. **LinkedIn Video Introduction Optimiser** - Low effort, timely (new LinkedIn feature)

### Phase 2: Core Expansion (2-3 features)
3. **Offer Evaluation Framework** - Natural companion to salary negotiation
4. **AI Readiness Assessment** - Critical for 2025 job market
5. **Mock Interview Simulation** - Completes the interview prep experience

### Phase 3: Non-Traditional Paths (2 features)
6. **Portfolio & Fractional Career Support** - Major differentiator, growing market
7. **Entrepreneurial Transition Support** - Natural extension of fractional work

### Phase 4: Advanced Capabilities (remaining features)
8-15. LinkedIn enhancements, executive transitions, career pivots, etc.

---

## Technical Considerations

### Template Requirements
Each new capability should have:
- Supporting prompt file in `supporting-prompts/`
- Output template in `templates/`
- Addition to SKILL.md capabilities table
- Update to README.md feature list
- Version bump in version.json

### Regional Implementation
- All salary/compensation features must ask for target region
- WebSearch queries should include region-specific terms
- Currency formatting must be locale-appropriate
- Employment law context must be jurisdiction-aware
- Default to UK English; adapt for US roles

### Quality Standards
All new features should maintain:
- UK English default (US English for US-targeted roles)
- No emojis
- Citation requirements for research
- Template-based consistent output
- Actionable, specific recommendations
- Region-appropriate advice

---

## Research Sources (Validated)

### Job Market & AI Trends
- [Josh Bersin - AI Job Market Impact (Dec 2025)](https://joshbersin.com/2025/12/yes-ai-is-really-impacting-the-job-market-heres-what-to-do/)
- [Built In - How AI Changed the Job Market in 2025](https://builtin.com/articles/ai-work-2025-year-in-review)
- [Novoresume - AI Job Search Trends 2025](https://novoresume.com/career-blog/ai-job-search-trends)
- [SkillUp Coalition - AI Job Search Tools 2025](https://skillup.org/resources/ai-job-search-tools)

### Salary Negotiation Research
- [The Salary Negotiator](https://www.thesalarynegotiator.com/) - $10K guarantee model, 7% success fee
- [Levels.fyi Services](https://www.levels.fyi/services/) - Tech-focused, $10K-$40K guarantees by level
- [IGotAnOffer - Salary Negotiation Services Review](https://igotanoffer.com/en/advice/best-salary-negotiation-services)
- [Fearless Salary Negotiation](https://fearlesssalarynegotiation.com/) - High-earner focus ($400K+)
- [Career Agents - Salary Negotiation Tool](https://careeragents.org/salary-negotiation-tool/) - Free leverage calculator

### Executive & Career Transitions
- [Deliberate Directions - Executive Coaching Career Transitions 2025](https://deliberatedirections.com/executive-coaching-career-transitions/)
- [Find My Profession - Career Transition Coaches 2025](https://www.findmyprofession.com/career-advice/coaching-services-career-transition/)
- [Career Ahead Online - Mid-Career Executive Coaching 2025](https://careeraheadonline.com/what-mid-career-professionals-need-to-know-about-executive-coaching-in-2025/)

### LinkedIn 2025 Features
- [Resume Faster - LinkedIn 2025 Essential Updates](https://resumefaster.com/linkedin-2025-essential-updates-you-cant-miss/)
- [Supergrow - LinkedIn Personal Branding Strategy 2025](https://www.supergrow.ai/blog/linkedin-personal-branding)
- [LAKSN Technologies - LinkedIn 2025 Features](https://www.laksn.com/linkedin-in-2025-benefits-features-how-to-grow-professionally)
- [Roel Timmermans - LinkedIn Marketing Trends 2025](https://www.roeltimmermans.com/blog/linkedin-marketing-trends-2025)

### Gig Economy & Portfolio Careers
- [Carry - Gig Economy Trends 2025](https://carry.com/learn/gig-economy-trends-for-freelancers-and-self-employed-workers) - 70M+ US gig workers
- [Giggle Finance - Future of Gig Economy 2025](https://gigglefinance.com/future-of-gig-economy/) - $582B global market
- [Greenhouse - Freelancers in 2025 Talent Plans](https://www.greenhouse.com/blog/welcome-to-the-gig-economy-why-hiring-freelancers-needs-to-be-part-of-your-2025-talent-plan)

---

*This analysis was generated by Career Helper skill review using Claude Opus 4.5*
*All sources validated via WebSearch on 30 December 2025*
