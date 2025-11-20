---
name: career-helper
description: End-to-end career support for job seekers at all levels. Optimizes LinkedIn profiles, rewrites CVs for ATS systems, provides interview preparation with cited answers, researches companies and roles, identifies hiring managers and networking opportunities. Use when applying for jobs, preparing interviews, optimizing professional profiles, managing career transitions, or researching target companies and roles.
---

# Career Helper

## Quick Start

**First time using this skill?** → Load @`supporting-prompts/usage-guide.md`

**Common requests:**
- "Help me optimize my CV for [job description]" → CV/ATS optimization
- "Who should I connect with at [Company]?" → Strategic networking
- "I have an interview at [Company] next week" → Interview prep + research
- "Build me a LinkedIn content strategy" → Content coaching + calendar
- "Research [Company] before I apply" → Company intelligence
- "Review my LinkedIn profile for [role]" → Profile audit

**Need help or want to explore all capabilities?** Say: "What can you do?" or "How do I use this?"

## Getting Help

**If user asks "how do I use this?" or "what can you do?"** → Load @`supporting-prompts/usage-guide.md`

The usage guide contains quick start examples, what to have ready, and detailed capability lists. Only load it when the user explicitly asks for help or needs orientation.

## Core Capabilities

This skill provides six integrated services:

1. **LinkedIn Profile Optimization** - Headline, about section, skills ordering, API consistency
2. **ATS-Optimized CV Rewriting** - Keyword saturation, semantic alignment, parsing safety
3. **Company & Role Research** - Market analysis, company intelligence, hiring manager identification
4. **Interview Preparation** - Role-specific questions, evidence-backed answers with citations
5. **Strategic Networking Intelligence** - High-value LinkedIn connections, personalized outreach strategies
6. **Application Strategy** - Timeline planning, follow-up protocols, stakeholder mapping

## About This Skill

**Created by:** Paul Bratcher
**Organization:** Prosper Consulting
**Repository:** https://github.com/Zal4DW/career-helper
**LinkedIn:** https://www.linkedin.com/in/paul-bratcher/

**Feedback Welcome:**
- Found this helpful? Share your success story!
- Feature requests or bugs? Open an issue on GitHub
- Questions? Use GitHub Discussions or connect on LinkedIn

This skill is actively maintained and improved based on user feedback.

---

## Available Capabilities

Choose what you need. These can be used independently or together:

### 1. Company & Role Research

**When to use:** Researching target company before applying or interviewing
**What you need:** Company name, job description (optional but helpful)
**Load:** @`supporting-prompts/company-research.md`

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

### 2. CV Optimization for ATS

**When to use:** Tailoring CV for specific role to pass ATS screening
**What you need:** Your current CV + target job description
**Load:** @`supporting-prompts/ATS-Helper.md`

NLP and recruitment AI specialist approach:
- Keyword and concept extraction from job description
- ATS-safe CV rewrite with quantified achievements
- Keyword coverage analysis
- LinkedIn API consistency checks
- Formatting and parsing safety verification

**Output:** `{role-slug}-cv-optimized.md` + `{role-slug}-linkedin-updates.md`

---

### 3. LinkedIn Profile Optimization

**When to use:** Improving profile visibility, recruiter discoverability, or content strategy
**What you need:** LinkedIn profile URL + career goals

**Option A - Comprehensive Profile Audit:**
**Load:** @`supporting-prompts/linkedin-profile-review.md`
- Complete profile sections review (photo to recommendations)
- Headline and about section optimization
- Skills reordering (RSC API top 3)
- Discoverability and recruiter search optimization
- Activity and content strategy

**Option B - Content Review (Reactive):**
**Load:** @`supporting-prompts/linkedin-posts-helper.md`
- Recent post analysis against target audience
- Decision-maker pain points identification
- Content recommendations for thought leadership

**Option C - Content Strategy Coaching (Proactive):**
**Load:** @`supporting-prompts/content-strategy-coaching.md`
- Develop sustainable 3x/week posting strategy
- Identify authentic content pillars from real expertise
- Build engagement network (20-30 strategic connections)
- Create 4-week content calendar with specific topics
- Thread series guidance (when/why multi-post sequences)
- Voice coaching (write authentically, not templates)
- Professional, non-cheesy guidance grounded in experience

**Output:** `{role-slug}-linkedin-profile-review.md` or `{role-slug}-content-strategy.md` + `{role-slug}-content-calendar.md`

---

### 4. Interview Preparation

**When to use:** Preparing for upcoming interview
**What you need:** CV + job description + company research + interview stage
**Load:** @`supporting-prompts/interview-prep.md`

Role-specific preparation engine:
- 15-20 likely questions (behavioral, technical, situational, company-specific)
- STAR answer frameworks using your actual experience
- 5-7 pre-prepared adaptable stories
- 8-10 intelligent questions to ask (by interviewer type)
- Talking points, concern mitigation, execution tips
- Post-interview follow-up templates

All answers cite your real experience with evidence.

**Output:** `{role-slug}-interview-prep.md`

---

### 5. Strategic Networking Intelligence

**When to use:** Identifying who to connect with on LinkedIn for target role/company
**What you need:** Company name + target role + your background/LinkedIn
**Load:** @`supporting-prompts/networking-strategy.md`

Agentic parallel research to identify high-value connections:
- Hiring managers and direct team members
- Internal recruiters and talent acquisition
- Executive stakeholders and decision makers
- Company alumni who share your background
- Mutual connection paths for warm introductions
- Recent joiners and technical thought leaders
- Personalized connection strategies and message templates
- Timing and sequencing guidance

Uses parallel WebSearch to find 8-12 strategic people, prioritized in 3 tiers.

**Output:** `{role-slug}-networking-intelligence.md` (uses networking-intelligence-template.md with clear tabular contact plan)

---

### 6. Application Strategy & Timeline

**When to use:** Planning comprehensive application approach
**What you need:** All above outputs + timeline constraints
**Load:** @`templates/application-strategy-template.md`

Comprehensive planning:
- Timeline and milestone planning
- Stakeholder mapping and connection strategy
- Risk mitigation for identified gaps
- Follow-up protocols and decision framework

**Output:** `{role-slug}-application-strategy.md`

## Output Standards

All outputs must follow these standards:

- **UK English** throughout (unless US role explicitly requires US English)
- **No emojis** - Professional tone appropriate for target role level
- **No marketing fluff** - Data-driven, evidence-based recommendations
- **Cited sources** - All research findings include URLs and dates accessed
- **Quantified metrics** - Specific numbers, percentages, timeframes
- **Actionable steps** - Concrete next actions, not vague advice

## File Organization

**Templates (read-only, in skill folder):**
```
.claude/skills/Career-Helper/templates/
├── research-brief-template.md
├── cv-template.md
├── linkedin-updates-template.md
├── content-calendar-template.md
├── interview-prep-template.md
├── networking-intelligence-template.md
└── application-strategy-template.md
```

**Generated outputs (write to project root):**
```
career-outputs/
├── {role-slug}-research-brief.md
├── {role-slug}-cv-optimized.md
├── {role-slug}-linkedin-updates.md
├── {role-slug}-content-strategy.md
├── {role-slug}-content-calendar.md
├── {role-slug}-networking-intelligence.md
├── {role-slug}-interview-prep.md
└── {role-slug}-application-strategy.md
```

Skills cannot write to their own directory. All generated files go to `career-outputs/` in the project working directory.

## Supporting Prompts (Load On-Demand)

Use @ symbol to load these specialized prompts only when needed:

- **@supporting-prompts/career-stage-context.md** - Generation-specific challenges and adaptive strategies (early career, mid-career, experienced, late career)
- **@supporting-prompts/company-research.md** - Agentic parallel company research with WebSearch/WebFetch/Task tool
- **@supporting-prompts/networking-strategy.md** - Agentic parallel networking intelligence to identify strategic LinkedIn connections
- **@supporting-prompts/ATS-Helper.md** - NLP recruitment AI specialist for CV optimization and keyword analysis
- **@supporting-prompts/linkedin-profile-review.md** - Comprehensive profile audit and recruiter search optimization
- **@supporting-prompts/linkedin-posts-helper.md** - Content review and audience alignment (reactive analysis of existing posts)
- **@supporting-prompts/content-strategy-coaching.md** - Content strategy coaching for sustainable 3x/week posting with authentic topics
- **@supporting-prompts/interview-prep.md** - Role-specific question generation with STAR frameworks from real experience
- **@supporting-prompts/usage-guide.md** - How to use this skill, quick start examples, capabilities list

**Progressive disclosure:** Don't load all at once. Load only what's needed for the current task to keep context efficient.

## Quality Standards

For whatever capabilities you use, maintain these standards:

- **Never invent data** - Mark missing info as `[MISSING]`, don't fabricate experience
- **Cite sources** - All research includes URLs and access dates
- **Use real experience** - Answers reference user's actual CV, not generic examples
- **Be specific** - Quantified metrics, concrete actions, no vague buzzwords
- **Match language** - UK English unless US role specified
- **ATS-safe** - Simple formatting, conventional headings, consistent dates
- **Actionable** - Clear next steps, not just analysis

Adapt these standards to what you're actually delivering - don't apply CV standards to interview prep.

## When Things Are Missing or Uncertain

**Incomplete information:**
- Never invent experience, dates, or qualifications
- Mark gaps as `[MISSING: what's needed]` and continue
- Work with what you have, offer to refine later
- Ask user if specific missing info is critical to their goal

**Research limitations:**
- Be honest about what you couldn't find
- Explain why (not public, paywalled, company too private, etc.)
- Suggest alternative approaches or manual research steps
- Don't speculate - distinguish fact from inference

**Working with blocked content:**
When WebFetch fails (LinkedIn, Glassdoor, paywalled content):
- Ask user to screenshot the page and provide file path (Read tool can process images)
- Or ask user to copy/paste text directly
- Or ask user to save as PDF and provide path
- Only request screenshots for critical content (top 3-5 priority items)
- Explain value: "This will help me provide [specific benefit]"

**Uncertain advice:**
- If multiple valid approaches exist, explain trade-offs
- If user's situation is unusual, say so
- Don't force-fit generic advice to unique situations

## Model & Reasoning

This skill uses **sonnet** for balance of capability, speed, and cost.

Use **extended thinking** when:
- Deep company research with many sources to synthesize
- Interview question generation requiring creativity and specificity
- Complex gap analysis or strategy recommendations

Trust the model to make good decisions, but verify outputs against quality standards.
