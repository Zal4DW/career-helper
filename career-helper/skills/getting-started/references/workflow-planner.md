# Workflow Planner

Create a personalised skill sequence based on the user's specific situation. This is not a generic workflow - it adapts to what they have, what they need, and how urgent it is.

## How to Use This Reference

1. Gather context using AskUserQuestion (see questions below)
2. Match their situation to a workflow pattern
3. Present the sequence with dependencies and expected outputs
4. Offer to start the first step immediately

## Context Questions

Ask using AskUserQuestion tool:

**Question 1:** "What best describes your situation?"
- Actively applying for roles
- Have an interview coming up
- Just starting a job search
- Want to check my digital footprint
- Considering a career change
- Exploring alternatives to traditional employment (starting a business, public sector, charity, etc.)
- Want to improve my professional presence
- Want to build or refresh my personal brand (positioning, audience, content, bios)
- Employed, but want to keep an ear to the ground discreetly

**Question 2 (based on answer):**
- Applying → "Do you have a specific role in mind, or are you exploring?"
- Interview → "When is the interview, and what stage is it?"
- Starting search → "Are you currently employed or between roles?"
- Career change → "What kind of change - new industry, freelance/fractional, or upskilling?"
- Alternatives to employment → "What are you most drawn to: starting your own business, public sector, charity/social enterprise, or are you not sure yet?"
- Professional presence → "Is this for job search, thought leadership, or client acquisition?"
- Personal brand → "Are you starting from scratch (positioning), refreshing existing bios, or building a content plan? And is this for fractional, board work, a sector pivot, or something else?"
- Ear to the ground → "Which employer is the starting point for similar organisations, and which region and function matter most? How discreet do you need to be?"

## Workflow Patterns

### Pattern A: Targeting a Specific Role

**Best for:** User has identified a company and role they want to apply for.

```
Step 0: /employer-footprint (Full Footprint Analysis) [OPTIONAL]
        Input: Name + social handles + CV + target company
        Output: {name}-footprint-dashboard.md
        Why first: Know what employers will find before you apply
            ↓
Step 1: /application-optimiser (Company Research)
        Input: Company name + job description
        Output: {role}-research-brief.md
        Why first: Everything else builds on understanding the company
            ↓
Step 2: /application-optimiser (CV Optimisation)
        Input: CV + job description + research brief
        Output: {role}-cv-optimized.md
        Why second: Research insights inform how you position yourself
            ↓
Step 3: /linkedin-coach (Profile Audit)
        Input: LinkedIn URL + career goals
        Output: {role}-linkedin-profile-review.md
        Why third: LinkedIn should align with your optimised CV
            ↓
Step 4: /interview-master (Interview Preparation)
        Input: CV + JD + research brief
        Output: {role}-interview-prep.md
        Why fourth: Best prep uses all previous research
            ↓
Step 5: /interview-master (Mock Interview)
        Input: Interview prep document
        Output: Feedback in conversation
        Why fifth: Practice after preparation, not before
```

**Dependencies:** Each step's output improves the next step's quality. Skipping Step 1 weakens Steps 2-5.

### Pattern B: Interview Imminent

**Best for:** User has an interview in the next few days and needs to prepare fast.

```
Step 1: /interview-master (Interview Preparation)
        Input: CV + job description + company name
        Output: {role}-interview-prep.md
        Why first: Most urgent need
            ↓
Step 2: /interview-master (Interviewer's Perspective)
        Input: Job description + CV
        Output: {role}-interviewer-perspective.md
        Why second: Understand what they're really assessing
            ↓
Step 3: /interview-master (Mock Interview)
        Input: Interview prep document
        Output: Feedback in conversation
        Why third: Practice with the prep you've built
```

**Optional add-on:** If there is time, run `/application-optimiser` (Company Research) before Step 1 to strengthen preparation.

### Pattern C: Starting from Scratch

**Best for:** User is beginning a job search without a specific target.

```
Step 0: /employer-footprint (Full Footprint Analysis) [RECOMMENDED]
        Input: Name + social handles + CV
        Output: {name}-footprint-dashboard.md
        Why first: Understand your digital presence before employers see it
            ↓
Step 1: /career-navigator (3-Month Plan)
        Input: Career stage, situation, goals
        Output: three-month-plan.md
        Why first: Strategy before tactics
            ↓
Step 2: /linkedin-coach (Profile Audit)
        Input: LinkedIn URL + career goals
        Output: linkedin-profile-review.md
        Why second: LinkedIn is your passive job search tool
            ↓
Step 3: /linkedin-coach (Content Strategy)
        Input: Role, expertise, goals
        Output: content-strategy.md + content-calendar.md
        Why third: Build visibility while searching
            ↓
Step 4: /career-navigator (Networking Intelligence)
        Input: Target companies + your background
        Output: {company}-networking-intelligence.md
        Why fourth: Strategic connections accelerate everything
```

**When a target role emerges:** Switch to Pattern A.

### Pattern D: Career Transition (Fractional/Portfolio)

**Best for:** User considering fractional, portfolio, or freelance career models.

```
Step 1: /career-transitions (Portfolio/Fractional Careers)
        Input: Skills inventory, income goals, region
        Output: portfolio-career-strategy.md
        Why first: Validate the direction before optimising for it
            ↓
Step 2: /career-transitions (AI Readiness)
        Input: Current role, target roles, AI experience
        Output: ai-readiness-plan.md
        Why second: AI competency increasingly differentiates candidates
            ↓
Step 3: /linkedin-coach (Profile Audit)
        Input: LinkedIn URL + new career direction
        Output: linkedin-profile-review.md
        Why third: Reposition LinkedIn for the new direction
            ↓
Step 4: /career-navigator (3-Month Plan)
        Input: Transition strategy + career goals
        Output: three-month-plan.md
        Why fourth: Structured plan for the transition
```

### Pattern D2: Non-Linear Career Exploration

**Best for:** User questioning the traditional career ladder. Considering entrepreneurship, startup founding, public sector, charity, intrapreneurship, or multi-role career models. Not sure which direction is right.

```text
Step 1: /career-transitions (Non-Linear Career Explorer)
        Input: Current situation, motivations, financial readiness, skills, risk tolerance
        Output: non-linear-career-exploration.md
        Why first: Structured exploration before committing to a direction
            ↓
Step 2: Based on chosen direction:
        - Entrepreneurship/Startup → /career-transitions (Portfolio/Fractional) for financial modelling
        - Public sector → /application-optimiser (CV for Success Profiles framework)
        - Charity/Non-profit → /application-optimiser (CV for sector) + /linkedin-coach (repositioning)
        - Intrapreneurship → /linkedin-coach (internal visibility) + stay in current role
        - Multi-role/Skill stacking → /career-navigator (3-Month Plan with non-linear goals)
        - Still deciding → /career-navigator (3-Month exploration plan)
            ↓
Step 3: /linkedin-coach (Profile Audit)
        Input: LinkedIn URL + new career direction
        Output: linkedin-profile-review.md
        Why: Reposition LinkedIn for chosen direction
            ↓
Step 4: /career-navigator (3-Month Plan)
        Input: Chosen path + career goals + transition timeline
        Output: three-month-plan.md
        Why: Structured action plan for the transition
```

**Key insight:** Non-linear career exploration should come before committing to a specific path. The exploration output identifies the best-fit option based on evidence, not just intuition.

### Pattern E: Post-Rejection Recovery

**Best for:** User has been rejected and wants to understand what happened and improve.

```
Step 1: /interview-master (Post-Interview Coaching)
        Input: CV + JD + what you remember + any feedback
        Output: {role}-post-interview-debrief.md
        Why first: Diagnose before prescribing
            ↓
Step 2: Based on diagnosis:
        - Skill gap → /career-transitions (AI Readiness) or upskilling plan
        - Signal gap → /interview-master (Interview Prep) for next opportunity
        - Fit/timing gap → /application-optimiser (Company Research) for alternative targets
```

### Pattern G: Personal Brand Build

**Best for:** User wants to build or refresh a personal brand. They have direction (a topic or a role they want to be known for) but not yet positioning.

```text
Step 1: /personal-brand (Capability A: Brand Foundation)
        Input: distinct angle, proof points, target audience, why-now anchor (or ikigai answers from Tim)
        Output: personal-brand-foundation.md
        Why first: pillars, channels, and bios are downstream of positioning; a generic foundation produces generic everything else
            ↓
Step 2: /personal-brand (Capability B: Audience and Channel Map)
        Input: positioning statement, weekly time budget
        Output: personal-brand-audience-channels.md
        Why second: the channel matrix follows the audience profile; reversing the order produces a plan the user does not run
            ↓
Step 3: /personal-brand (Capability C: Content Pillars and Cadence)
        Input: foundation document, audience map
        Output: personal-brand-content-plan.md
        Why third: pillars come from the intersection of Why You and Why Them; the audience map sharpens both
            ↓
Step 4: /personal-brand (Capability D: Bio Library)
        Input: foundation document, existing bios to refresh (if any)
        Output: personal-brand-bio-library.md
        Why fourth: bios reuse the same proof points framed differently; producing them last ensures consistency across LinkedIn, X, speaker bio, podcast bio, About page, and board bio
            ↓
Step 5 (optional): /linkedin-coach (Profile Audit)
        Input: positioning statement, bio library
        Output: linkedin-profile-review.md
        Why optional: turns the brand layer into LinkedIn-shaped tactics. Skip if LinkedIn is not the primary channel.
```

**Persona variations:**

- **Fractional or Portfolio:** before Step 1, run /career-transitions (Portfolio/Fractional Careers) if the user has not yet committed to going fractional. Brand work for a path the user has not committed to produces output that gets binned. Once committed, Steps 1 to 4 load the fractional persona guide.
- **NED, Governor, or Trustee:** Steps 1 to 4 load the NED persona guide. The channel matrix in Step 2 weights relational channels (chairs, head-hunters, sector publications) above broad social. If AI governance is the topic, also run /ned-ai-helper.
- **Career Returner:** Steps 1 and 4 load the career returner persona guide. Step 4 disproportionately weights LinkedIn About; Steps 2 and 3 are optional during the active-return phase.

**Key insight:** Run Step 1 before any other capability. The foundation is the spine; the rest is dressing.

### Pattern H: Brand Refresh

**Best for:** User has an existing online presence that has drifted from where they want to be. Bios are inconsistent, content pillars no longer fit, channels no longer match audience.

```text
Step 1: /personal-brand (Capability E: Brand Refresh)
        Input: links to current LinkedIn, personal site, recent talks or posts; intended positioning
        Output: personal-brand-refresh-plan.md
        Why first: the audit identifies drift before any rewrite
            ↓
Step 2 (conditional, based on what the audit surfaces):
        - Risky or off-brand legacy content → /social-media-review
        - Need a deeper scored employer-impression dashboard → /employer-footprint
        - Positioning has changed but is not yet documented → /personal-brand (Capability A) before continuing
            ↓
Step 3: /personal-brand (Capability D: Bio Library)
        Input: refreshed positioning, surfaces flagged in the refresh plan
        Output: personal-brand-bio-library.md
        Why: rewrite every surface the audit flagged as drifted, in one consistent pass
            ↓
Step 4 (optional): /linkedin-coach (Profile Audit)
        Input: refreshed bio library
        Output: linkedin-profile-review.md
        Why optional: applies the refreshed bios to LinkedIn at the platform-tactic layer
```

### Pattern I: Employed and Quietly Exploring

**Best for:** User is in a role, not actively applying, and wants to know which organisations like their employer are growing or hiring without announcing a search.

```text
Step 1: /market-mapper (Market Map)
        Input: current employer as the seed, region, target function and level, exclusions, discretion posture
        Output: market-map.md
        Why first: it defines what "similar" means and gathers dated signals before any outreach is considered
            ↓
Step 2: /market-mapper (Watchlist and Weekly Update), on a Cowork schedule via /career-routines or run manually
        Input: the existing map
        Output: market-watch/{date}-update.md, updated market map board
        Why: only what changed is reported, so the weekly read stays short
            ↓
Step 3 (optional): /market-mapper (Watchlist Board View)
        Output: the market map board, opened to change priorities
        Why optional: the board exists from step 1; open it when you want to reprioritise
            ↓
Step 4 (when an organisation reaches Act now): /career-navigator (Strategic Networking Intelligence)
        Input: the organisation, its decision makers and signals from the map
        Output: applications/{role-slug}/networking-intelligence.md
        Why: relationship first, at the user's pace; nothing here obliges an application
            ↓
Step 5 (when a role appears): /job-scout with the organisation's careers page as a named target, then /application-optimiser
```

**Key insight:** the discretion posture set in Step 1 governs every later step. An employed user's angles stay at follow, read, and comment until they decide otherwise.

### Pattern F: Offer Stage

**Best for:** User has received one or more offers.

```
Step 1: /career-navigator (Salary Negotiation)
        Input: Offer details, region, competing offers
        Output: {role}-negotiation-strategy.md
        Why first: Negotiate before accepting
            ↓
Step 2: /career-navigator (Offer Evaluation)
        Input: All offer details, priorities
        Output: offer-evaluation.md
        Why second: Structured decision-making after negotiation
```

## Presentation Format

Present the workflow as a numbered sequence with clear dependencies. Example:

```
Based on your situation, here's my recommended approach:

1. Company Research (/application-optimiser)
   → Produces: research-brief.md
   → Feeds into: CV optimisation and interview prep

2. CV Optimisation (/application-optimiser)
   → Needs: research brief + your CV + job description
   → Produces: cv-optimized.md

3. Interview Preparation (/interview-master)
   → Needs: research brief + optimised CV + job description
   → Produces: interview-prep.md

Shall I start with Step 1?
```

## Key Principles

- Always explain dependencies between steps
- Never present a generic workflow - adapt to the user's actual situation
- Offer to start the first step immediately after presenting the plan
- If the user is missing inputs for the first step, route to Capability 1 (Preparation Checklist) first
