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

## Gap Analysis: What's Missing

### Current Coverage (Strong)
✅ LinkedIn profile optimization
✅ ATS CV optimization
✅ Company research
✅ Interview preparation (questions & STAR frameworks)
✅ Networking intelligence
✅ Post-rejection coaching
✅ Application strategy & timeline
✅ 3-month job search planning

### Critical Gaps Identified
❌ **Salary negotiation** - Entirely missing, yet 58% of job seekers don't negotiate
❌ **Offer evaluation** - No framework for comparing multiple offers
❌ **Fractional/portfolio careers** - Only covers traditional employment
❌ **Entrepreneurial transitions** - No support for starting a business or consultancy
❌ **LinkedIn video optimization** - New 30-second video feature not addressed
❌ **Skills verification strategy** - LinkedIn's 2025 verified skills not covered
❌ **AI readiness assessment** - No guidance on demonstrating AI competency
❌ **Mock interview practice** - Prep exists, but no simulation/practice mode
❌ **Executive transition specifics** - C-suite moves have unique challenges
❌ **Counter-offer navigation** - What to do when current employer counters

---

## Recommended Features (Priority Ordered)

### 🏆 TIER 1: High Impact, High Value

---

#### 1. Salary Negotiation Coach
**Priority:** Critical
**Effort:** Medium
**User Value:** Extremely High (potential $10,000+ impact per user)

**The Gap:**
Only 42% of job seekers negotiate their salary, yet 9 out of 10 succeed when they try. Current skill has zero coverage of this critical moment.

**Proposed Capability:**
```
When to use: After receiving a job offer
What you need: Offer details + market research + user priorities
```

**Features:**
- **Market compensation analysis** - Research salary bands for role/location/level using WebSearch
- **Leverage calculator** - Assess negotiating position based on competing offers, unique skills, market demand
- **Negotiation script generator** - Personalized scripts for different scenarios (phone, email, in-person)
- **Counter-offer templates** - Specific language for base, bonus, equity, benefits, start date
- **Risk assessment** - When to push, when to accept, red flags that offer may be rescinded
- **Total compensation framework** - Evaluate beyond base salary (equity, benefits, WFH, growth potential)
- **Practice dialogues** - Common objections and how to handle them
- **Acceptance/decline templates** - Professional responses for either outcome

**Template Output:** `{role-slug}-negotiation-strategy.md`

**Research Sources:**
- [The Salary Negotiator](https://www.thesalarynegotiator.com/) - Guaranteed coaching model
- [Levels.fyi](https://www.levels.fyi/services/) - Compensation data and negotiation
- [Fearless Salary Negotiation](https://fearlesssalarynegotiation.com/) - High-earner strategies

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
What you need: Offer details + current situation + career priorities
```

**Features:**
- **Weighted decision matrix** - Customizable factors (comp, growth, culture, location, mission, etc.)
- **Total compensation calculator** - Normalize offers for comparison (equity, benefits, taxes, cost of living)
- **Career trajectory analysis** - Which offer best positions for 3-5 year goals?
- **Culture fit scoring** - Based on prior company research
- **Risk assessment** - Startup vs. established, industry trends, company health
- **Opportunity cost analysis** - What are you giving up? Counter-offer considerations
- **"Regret minimization" framework** - Bezos-style decision making for big career moves

**Template Output:** `offer-evaluation.md`

---

#### 3. Portfolio & Fractional Career Support
**Priority:** High
**Effort:** High
**User Value:** High (36% of US workforce now gig/portfolio)

**The Gap:**
Career Helper assumes traditional full-time employment. No support for fractional executives, portfolio careers, or hybrid income models.

**Research Context:**
- 70+ million Americans in gig economy (36% of workforce)
- Gen Z leading the charge (53% prefer freelancing)
- Fractional C-suite roles growing rapidly
- Traditional career paths being replaced by portfolio careers

**Proposed Capability - Fractional Career Strategy:**
```
When to use: Considering or building a fractional/portfolio career
What you need: Skills inventory + income goals + time availability
```

**Features:**
- **Portfolio career design** - Map multiple income streams and time allocation
- **Fractional executive positioning** - How to pitch yourself for fractional CFO, CMO, CTO roles
- **Platform strategy** - Which platforms for which work (Toptal, Catalant, Graphite, etc.)
- **Rate setting guidance** - Market rates by skill, experience, engagement type
- **Client pipeline building** - Networking for ongoing work, not one-time jobs
- **Contract negotiation** - Retainer vs. project, scope creep protection, payment terms
- **Tax & benefits planning** - Self-employment considerations, retirement, insurance
- **Portfolio CV format** - Different from traditional CV; emphasizes versatility and outcomes
- **LinkedIn optimization for fractional** - Profile that attracts multiple client types

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
What you need: Expertise areas + financial runway + risk tolerance
```

**Features:**
- **Consultancy launch planning** - Packaging expertise into service offerings
- **Business model assessment** - Which model fits skills and goals (agency, productized service, SaaS)
- **Financial runway analysis** - When to leap, how much buffer needed
- **Personal brand to business brand** - Transitioning LinkedIn presence
- **First client acquisition strategy** - Leveraging existing network
- **Pricing strategy** - Value-based vs. hourly, retainer structures
- **Risk mitigation** - Side hustle first? Pilot projects? Notice period planning
- **Legal/structural basics** - Entity types, contracts, IP considerations

**Template Output:** `entrepreneurial-transition-plan.md`

---

### 🥈 TIER 2: High Impact, Medium Effort

---

#### 5. LinkedIn Video Introduction Optimizer
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
- **Delivery tips** - Eye contact, pacing, background, lighting basics
- **Goal-specific variations** - Job seeker vs. thought leader vs. client acquisition
- **A/B testing guidance** - How to iterate and improve
- **Review existing video** - Critique and improvement suggestions (via screenshot/description)

---

#### 6. AI Readiness & Skills Assessment
**Priority:** High
**Effort:** Medium
**User Value:** High (critical for 2025+ job market)

**The Gap:**
The 2025 job market requires demonstrating AI literacy. No current support for assessing or showcasing AI readiness.

**Research Context:**
- AI-related job postings grew 38% from 2020-2024
- Employers now expect AI literacy across all roles
- "Sell your AI readiness" is critical advice for all levels
- Major banks increased AI headcount 13% in just 6 months

**Proposed Capability:**
```
When to use: Assessing and improving AI readiness for job search
What you need: Current role + target roles + existing AI experience
```

**Features:**
- **AI skills gap assessment** - What AI competencies does target role require?
- **AI experience inventory** - Help user articulate existing AI-adjacent work
- **Upskilling roadmap** - Specific courses, certifications, projects to build credibility
- **CV/LinkedIn AI integration** - How to weave AI capabilities into existing materials
- **Interview AI readiness prep** - Questions to expect about AI, frameworks to answer
- **Portfolio project ideas** - Demonstrable AI projects by domain
- **Tool proficiency guidance** - Which AI tools matter for which roles

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
When to use: Optimizing LinkedIn skills for recruiter visibility
What you need: Target roles + current skills list
```

**Features:**
- **Skill prioritization matrix** - Which skills to verify based on role demand and recruiter searches
- **Assessment prep tips** - LinkedIn's assessment format and study strategies
- **Certification integration** - How to upload/display verified certifications
- **Skills ordering strategy** - Top 3 skills for RSC API optimization
- **Endorsement strategy** - Who to ask, how to reciprocate
- **Hidden gem skills** - Underrated skills that differentiate in your domain

---

#### 8. LinkedIn Engagement Optimizer
**Priority:** Medium-High
**Effort:** Medium
**User Value:** Medium-High (visibility multiplier)

**The Gap:**
Current content strategy focuses on posting. Engagement (commenting, reacting) often more impactful for visibility.

**Research Context:**
"The simplest and most powerful activity that significantly boosts your visibility is commenting on your network's posts."

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
When to use: Practicing before actual interview
What you need: Interview prep document + preferred interview type
```

**Features:**
- **Simulated interview mode** - Claude acts as interviewer, user responds
- **Real-time feedback** - Critique of answers as practice progresses
- **STAR compliance check** - Did answer follow STAR format?
- **Follow-up questions** - Realistic drilling down on initial responses
- **Difficult interviewer personas** - Practice with challenging styles (skeptical, rapid-fire, silent)
- **Time management** - Feedback on answer length and pacing
- **Confidence building** - Positive reinforcement with constructive feedback
- **Recording recommendations** - Tips for self-review practice

---

### 🥉 TIER 3: Medium Impact, Strategic Value

---

#### 10. Executive Transition Specialist
**Priority:** Medium
**Effort:** Medium
**User Value:** High (for senior users)

**The Gap:**
C-suite transitions have unique challenges not covered by general career advice.

**Research Context:**
"Executives stepping into the 2025 job market face overlapping technological, organizational and cultural shifts... The capabilities that earned executives their C-suite promotion rarely match what the role actually demands."

**Proposed Capability:**
```
When to use: C-suite or VP-level transitions
What you need: Current level + target roles + transition type
```

**Features:**
- **Executive search process navigation** - How retained search differs from job boards
- **Board and investor relationship prep** - Unique to C-suite transitions
- **Reference orchestration** - Strategic reference selection for executive roles
- **Equity negotiation specifics** - Options, RSUs, cliff, acceleration clauses
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
- **Decision matrix** - Money vs. underlying issues assessment
- **Conversation scripts** - How to decline gracefully
- **Bridge-burning prevention** - Leaving on good terms regardless of decision
- **Legal considerations** - Notice period, garden leave, non-compete

---

#### 12. Career Pivot Advisor
**Priority:** Medium
**Effort:** Medium
**User Value:** High (growing need for career pivots)

**The Gap:**
Current skill optimizes for same-field progression. No support for major career pivots.

**Proposed Capability:**
```
When to use: Considering significant career change (new industry/function)
What you need: Current background + target direction + constraints
```

**Features:**
- **Transferable skills mapping** - Bridge current experience to new field
- **Skill gap analysis** - What's needed for credible pivot
- **Bridge role identification** - Intermediate steps that build credibility
- **Credibility building plan** - Projects, certifications, volunteering to demonstrate commitment
- **Pivot CV formatting** - Functional vs. chronological, highlighting transferable skills
- **Story crafting** - Narrative that makes pivot logical, not random
- **Network pivot strategy** - Building connections in new field

**Template Output:** `career-pivot-plan.md`

---

#### 13. Remote/Hybrid Optimization
**Priority:** Medium
**Effort:** Low
**User Value:** Medium (work pattern optimization)

**The Gap:**
No specific guidance for targeting remote/hybrid roles or optimizing for distributed work.

**Proposed Capability:**
```
When to use: Prioritizing remote work or optimizing remote search
What you need: Location preferences + time zone + remote experience
```

**Features:**
- **Remote-friendly company identification** - Research company remote policies
- **Remote work CV optimization** - Highlighting remote-relevant skills
- **Time zone strategy** - How to position for async-friendly or specific TZ roles
- **Remote interview preparation** - Technical setup, virtual presence
- **Remote culture assessment** - Questions to evaluate remote-friendliness
- **LinkedIn "Open to Work" optimization** - Remote/hybrid preference settings

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
2. **LinkedIn Video Introduction Optimizer** - Low effort, timely (new LinkedIn feature)

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

### Tool Usage
- **Salary/Offer features**: WebSearch for market data, compensation research
- **Portfolio/Fractional features**: WebSearch for platform research, rate data
- **Mock Interview**: New interaction pattern (Claude as interviewer)
- **AI Readiness**: WebSearch for current AI skill demands by role

### Quality Standards
All new features should maintain:
- UK English default
- No emojis
- Citation requirements for research
- Template-based consistent output
- Actionable, specific recommendations

---

## Sources

### Job Market Trends
- [SkillUp Coalition - AI Job Search Tools](https://skillup.org/resources/ai-job-search-tools)
- [Novoresume - AI Job Search Trends 2025](https://novoresume.com/career-blog/ai-job-search-trends)
- [Josh Bersin - AI Job Market Impact](https://joshbersin.com/2025/12/yes-ai-is-really-impacting-the-job-market-heres-what-to-do/)
- [Built In - AI and Work 2025](https://builtin.com/articles/ai-work-2025-year-in-review)

### Salary Negotiation
- [The Salary Negotiator](https://www.thesalarynegotiator.com/)
- [Levels.fyi Services](https://www.levels.fyi/services/)
- [IGotAnOffer - Salary Negotiation Services](https://igotanoffer.com/en/advice/best-salary-negotiation-services)
- [Career Agents - Salary Negotiation Tool](https://careeragents.org/salary-negotiation-tool/)

### Executive Transitions
- [Deliberate Directions - Executive Coaching 2025](https://deliberatedirections.com/executive-coaching-career-transitions/)
- [Find My Profession - Career Transition Coaches](https://www.findmyprofession.com/career-advice/coaching-services-career-transition/)
- [Career Ahead - Mid-Career Executive Coaching](https://careeraheadonline.com/what-mid-career-professionals-need-to-know-about-executive-coaching-in-2025/)

### LinkedIn Features
- [Resume Faster - LinkedIn 2025 Updates](https://resumefaster.com/linkedin-2025-essential-updates-you-cant-miss/)
- [Supergrow - LinkedIn Personal Branding 2025](https://www.supergrow.ai/blog/linkedin-personal-branding)
- [LAKSN - LinkedIn 2025 Features](https://www.laksn.com/linkedin-in-2025-benefits-features-how-to-grow-professionally)
- [Roel Timmermans - LinkedIn Trends 2025](https://www.roeltimmermans.com/blog/linkedin-marketing-trends-2025)

### Portfolio & Gig Economy
- [Carry - Gig Economy Trends 2025](https://carry.com/learn/gig-economy-trends-for-freelancers-and-self-employed-workers)
- [Giggle Finance - Future of Gig Economy](https://gigglefinance.com/future-of-gig-economy/)
- [Greenhouse - Freelancers in 2025 Talent Plan](https://www.greenhouse.com/blog/welcome-to-the-gig-economy-why-hiring-freelancers-needs-to-be-part-of-your-2025-talent-plan)
- [Tufts Alumni - Creating a Portfolio Career](https://alumniandfriends.tufts.edu/attend-events-reunions/working-gig-economy-creating-portfolio-career)

---

*This analysis was generated by Career Helper skill review using Claude Opus 4.5*
