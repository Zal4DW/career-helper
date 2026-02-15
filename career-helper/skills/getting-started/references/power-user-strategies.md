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
1. Run `/application-optimizer` (Company Research) for each target company separately
2. Start with one full CV optimisation as your "base" optimised CV
3. For subsequent roles, provide both the new JD and your already-optimised CV - ask to adapt rather than rebuild from scratch
4. Each role gets its own set of output files with the role slug prefix

**Key insight:** Company research briefs are always unique. CVs can be adapted between similar roles. Interview prep should always be role-specific.

**File organisation tip:** Output files use `{role-slug}` prefixes automatically. For multiple applications, you will accumulate files like:
```
senior-pm-google-research-brief.md
senior-pm-google-cv-optimized.md
head-product-startup-research-brief.md
head-product-startup-cv-optimized.md
```

Use `/career-helper:status` to see everything you have generated.

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
1. Run `/application-optimizer` (Company Research) for 2-3 target companies
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
1. `/application-optimizer` (Company Research) on your own company - see it from the outside
2. `/application-optimizer` (CV Optimisation) with the internal role description
3. `/interview-master` (Interview Prep) adapted for internal interviews (different dynamics)

### Return from Career Break

1. `/career-navigator` (3-Month Plan) with explicit mention of the break
2. `/career-transitions` (AI Readiness) to demonstrate current technical awareness
3. `/linkedin-coach` (Profile Audit) to reposition the break as intentional
4. `/application-optimizer` (CV Optimisation) with focus on transferable skills and break narrative

### Redundancy Response

1. `/career-navigator` (3-Month Plan) with urgency context
2. `/linkedin-coach` (Profile Audit) - immediate LinkedIn update
3. `/career-navigator` (Networking Intelligence) for target companies
4. `/application-optimizer` for first target applications

### Board or Advisory Positioning

1. `/career-transitions` (Portfolio/Fractional) to explore advisory structures
2. `/linkedin-coach` (Profile Audit) repositioned for board visibility
3. `/linkedin-coach` (Content Strategy) focused on thought leadership
4. `/career-navigator` (Networking Intelligence) targeting board networks

---

## Strategy 7: Output Maintenance

**When to use:** You have generated multiple outputs over time and want to keep them current.

**Approach:**
- Run `/career-helper:status` periodically to see all generated files
- When your CV changes, re-run CV optimisation for active applications
- When goals shift, re-run the 3-month plan
- Research briefs older than 3 months should be refreshed - company situations change

**File management:** All outputs are markdown files in your working directory. You can:
- Convert to PDF for submission
- Copy sections into application forms
- Share with mentors or coaches for feedback
- Use as reference during real interviews

---

## Presenting These Strategies

When sharing with the user, pick the 2-3 most relevant strategies for their situation rather than listing all seven. Ask what they are working on and recommend accordingly.
