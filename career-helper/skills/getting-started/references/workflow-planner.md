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
- Want to improve my professional presence

**Question 2 (based on answer):**
- Applying → "Do you have a specific role in mind, or are you exploring?"
- Interview → "When is the interview, and what stage is it?"
- Starting search → "Are you currently employed or between roles?"
- Career change → "What kind of change - new industry, freelance/fractional, or upskilling?"
- Professional presence → "Is this for job search, thought leadership, or client acquisition?"

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

### Pattern D: Career Transition

**Best for:** User considering fractional, portfolio, freelance, or industry change.

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
