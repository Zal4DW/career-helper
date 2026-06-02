# Power User Strategies

Advanced techniques for users who have used the basic skills and want to extract more value from career-helper.

## How to Use This Reference

- Present these strategies conversationally, not as a wall of text
- Ask which strategy interests the user, or recommend based on their situation
- These assume the user has already used at least one skill

---

## Strategy 1: Multi-Role Targeting

**When to use:** You are applying to multiple roles simultaneously and want tailored materials for each.

**Approach:**
1. Run `/application-optimiser` (Company Research) for each target company separately
2. Start with one full CV optimisation as your "base" optimised CV
3. For subsequent roles, provide both the new JD and your already-optimised CV - ask to adapt rather than rebuild from scratch
4. Each role gets its own set of output files with the role slug prefix

**Key insight:** Company research briefs are always unique. CVs can be adapted between similar roles. Interview prep should always be role-specific.

**File organisation:** Each application gets its own folder automatically. For multiple applications, your workspace looks like:
```text
applications/
├── marketing-manager-greenfield/
│   ├── research-brief.md
│   └── cv-optimised.md
├── head-fundraising-macmillan/
│   ├── research-brief.md
│   └── cv-optimised.md
└── senior-planner-birmingham-council/
    └── research-brief.md
```

Use `/career-helper:status` to see everything you have generated across all applications.

---

## Strategy 2: Cross-Skill Reinforcement

**When to use:** You want each skill's output to strengthen the others.

**The chain:**
1. Company research reveals what the company values
2. CV optimisation uses those values to frame achievements
3. LinkedIn audit aligns your profile with the optimised CV
4. Interview prep references all three to build cohesive answers

**How to do it:** When starting each subsequent skill, explicitly mention the outputs you have already generated. Example: "I've already done company research and CV optimisation for this role - the files are in my working directory. Use those to inform the interview preparation."

The skills automatically look for existing output files, but explicitly pointing them out ensures nothing is missed.

---

## Strategy 3: Comparative Company Analysis

**When to use:** You are deciding between multiple companies or want to understand how different organisations compare before choosing where to apply.

**Approach:**
1. Run `/application-optimiser` (Company Research) for 2-3 target companies
2. After generating all research briefs, ask: "Compare the research briefs for [Company A], [Company B], and [Company C] - which looks like the best fit for my background?"
3. This works because the research briefs follow a consistent template, making comparison straightforward

**Output:** Comparison analysis in conversation, highlighting culture fit, growth trajectory, compensation norms, and red flags across targets.

---

## Strategy 4: Interview Feedback Loop

**When to use:** You are going through multiple interview processes and want to improve between them.

**The loop:**
1. `/interview-master` (Interview Prep) for Role A
2. Real interview happens
3. `/interview-master` (Post-Interview Coaching) to diagnose what worked and what did not
4. Apply learnings to `/interview-master` (Interview Prep) for Role B
5. Explicitly say: "I previously struggled with [specific area from debrief] - focus extra attention on that"

**Key insight:** Post-interview coaching identifies whether gaps are skill, signal, or fit/timing issues. This diagnosis directly improves the next preparation cycle.

---

## Strategy 5: LinkedIn Content Pipeline

**When to use:** You want to build sustained LinkedIn visibility alongside your job search.

**Approach:**
1. `/linkedin-coach` (Profile Audit) to establish your baseline
2. `/linkedin-coach` (Content Strategy) to define pillars and cadence
3. Use the generated content calendar as a recurring reference
4. Periodically run `/linkedin-coach` (Content Review) on your published posts to get feedback and improve

**Advanced move:** After company research for a target, use insights to inform LinkedIn content. Writing knowledgeably about industry trends relevant to your target company demonstrates domain expertise to their employees who may see your posts.

---

## Strategy 6: Scenario-Specific Combinations

### Internal Promotion

Not just for external job searches. Adapt the tools:
1. `/application-optimiser` (Company Research) on your own company - see it from the outside
2. `/application-optimiser` (CV Optimisation) with the internal role description
3. `/interview-master` (Interview Prep) adapted for internal interviews (different dynamics)

### Return from Career Break

1. `/career-navigator` (3-Month Plan) with explicit mention of the break
2. `/career-transitions` (AI Readiness) to demonstrate current technical awareness
3. `/linkedin-coach` (Profile Audit) to reposition the break as intentional
4. `/application-optimiser` (CV Optimisation) with focus on transferable skills and break narrative

### Redundancy Response

1. `/career-navigator` (3-Month Plan) with urgency context
2. `/linkedin-coach` (Profile Audit) - immediate LinkedIn update
3. `/career-navigator` (Networking Intelligence) for target companies
4. `/application-optimiser` for first target applications

### Board or Advisory Positioning

1. `/personal-brand` (Brand Foundation, with NED persona guide loaded) for board-credible positioning that respects confidentiality, conflict of interest, and director duties
2. `/personal-brand` (Audience and Channel Map) weighting chairs, head-hunters, and trusted sector publications above broad social
3. `/personal-brand` (Bio Library) including the Board Bio as a primary surface
4. `/linkedin-coach` (Profile Audit) to apply the bio library to LinkedIn
5. `/career-navigator` (Networking Intelligence) targeting board networks
6. `/ned-ai-helper` if AI governance is the topic the user wants to be known for

### Non-Linear Career Pivot

Not sure if another employed role is right? Explore alternatives systematically:
1. `/career-transitions` (Non-Linear Career Explorer) to assess motivations, finances, and options
2. Based on outcome:
   - Entrepreneurship → `/career-transitions` (Portfolio/Fractional) for financial modelling
   - Public sector → `/application-optimiser` for Success Profiles CV
   - Charity → `/application-optimiser` for sector-specific CV + `/linkedin-coach` for repositioning
   - Intrapreneurship → `/linkedin-coach` for internal visibility
3. `/career-navigator` (3-Month Plan) with non-linear goals
4. `/ai-impact-assessment` to check future resilience of chosen direction

### Entrepreneurship Validation

Testing a business idea alongside your job search:
1. `/career-transitions` (Non-Linear Career Explorer) for honest business readiness assessment
2. `/linkedin-coach` (Content Strategy) to build thought leadership in your domain
3. `/career-navigator` (3-Month Plan) combining job search with business validation activities
4. Keep your options open: pursue both paths until one clearly wins

### Going Fractional with an Inbound-Generating Brand

For users who have committed to going fractional, portfolio, or independent and need a brand that does the heavy lifting:
1. `/career-transitions` (Portfolio/Fractional Careers) for the structural and financial decision (skip if already committed)
2. `/personal-brand` (Brand Foundation, with fractional persona guide) for stage- and sector-specific positioning that filters the right enquiries up front
3. `/personal-brand` (Audience and Channel Map) prioritising LinkedIn plus a personal "work with me" page; conversion infrastructure matters as much as content
4. `/personal-brand` (Content Pillars and Cadence) at medium-investment level by default; daily LinkedIn presence plus monthly long-form
5. `/personal-brand` (Bio Library) including a "work with me" page and a first-message-to-founder template
6. `/linkedin-coach` (Profile Audit + Content Strategy) to apply the brand to LinkedIn-specific tactics
7. `/career-navigator` (Networking Intelligence) for warm reconnections with pre-pivot network

**Key insight:** the buyer's risk-reducer is whether you have done the role at this stage in this sector with this kind of founder. The brand needs to make that explicit; vague fractional brands attract vague enquiries at lower rates.

### Returner Brand Build

For users returning after a career break who want positioning that frames the gap honestly without making it the story:
1. `/personal-brand` (Brand Foundation, with career returner persona guide) for a positioning that frames the gap as a chapter rather than a hole
2. `/personal-brand` (Bio Library) with disproportionate focus on LinkedIn About; this is the surface doing the most work for an active return
3. `/application-optimiser` (with career returner persona) to align the CV with the brand
4. `/linkedin-coach` (with career returner reference) for platform-specific tactics
5. `/career-navigator` (3-Month Plan with career returner persona) to combine brand-build activity with applications

**Key insight:** the brand work is also confidence work. Read the bios aloud; the user's first reaction often reveals whether the positioning sounds like them or like an over-corrected version.

---

## Strategy 7: Footprint-First Approach

**When to use:** You want to start your job search with full awareness of how you appear online.

**Approach:**
1. `/employer-footprint` (Full Footprint Analysis) to see your digital presence through employer eyes
2. Address RED and AMBER scores immediately:
   - LinkedIn issues → `/linkedin-coach` (Profile Audit)
   - Content gaps → `/linkedin-coach` (Content Strategy)
   - CV inconsistencies → `/application-optimiser` (CV Optimisation)
3. If targeting a specific company, run `/employer-footprint` (Employer Impression Report) to map your presence against their values
4. Use the generated interview questions from your footprint as input to `/interview-master`

**Key insight:** Running a footprint audit first reveals issues you might never discover otherwise. A LinkedIn profile that says "Director" when your CV says "Senior Manager" is an immediate red flag for recruiters. Better to find this yourself.

**Advanced move:** After fixing issues, re-run the footprint analysis to confirm improvements. The before/after comparison demonstrates tangible progress.

---

## Strategy 8: Output Maintenance

**When to use:** You have generated multiple outputs over time and want to keep them current.

**Approach:**
- Keep an application tracker (`/career-navigator`, Application Tracker) as the index of everything in flight; `/career-helper:status` reads it first
- Run `/career-helper:status` periodically to see all generated files and the tracker board together
- When your CV changes, re-run CV optimisation for active applications
- When goals shift, re-run the 3-month plan
- Research briefs older than 3 months should be refreshed - company situations change

**File management:** All outputs are markdown files organised in per-application folders. You can:
- Open any application folder to see everything for that role in one place
- Convert files to PDF for submission
- Copy sections into application forms
- Share with mentors or coaches for feedback
- Use as reference during real interviews
- Archive completed application folders when a role is finished

---

## Strategy 9: Automate the Search with Scheduled Tasks (Claude Cowork)

**When to use:** You run Career Helper inside Claude Cowork on Claude Desktop and want the search to keep moving between sessions rather than only when you sit down to work on it.

**Approach:**
1. Keep an application tracker (`/career-navigator`) so a scheduled task has something to read
2. Use Cowork's `/schedule` to set up recurring routines (see `/getting-started`, Scheduled Routines):
   - **Monday standup** (weekly): reads the tracker, flags overdue actions, names the three things to do this week
   - **Market monitor** (weekly): watches for new roles and news in your target area
   - **Follow-up check** (weekdays): catches the follow-ups that slip
   - **Posting reminder** (weekly): keeps your LinkedIn content cadence on track
3. Start with one routine, usually the Monday standup, and add others once it is part of your week

**Key insight:** the value compounds with a persistent workspace folder and a current tracker. Each scheduled run reads the same files, so the routines get more useful as your search progresses.

**Two honest caveats:** scheduled tasks only run while your computer is awake with Claude Desktop open, and scheduling is a Cowork feature rather than part of the plugin. If you use the CLI or web app, run the same prompts manually.

---

## Presenting These Strategies

When sharing with the user, pick the 2-3 most relevant strategies for their situation rather than listing all of them. Ask what they are working on and recommend accordingly.
