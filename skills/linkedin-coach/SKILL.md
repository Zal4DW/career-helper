---
name: linkedin-coach
description: LinkedIn profile optimisation, headline crafting, content strategy coaching, post review, and video introduction scripts. Covers five modes from full profile audit to headline-only optimisation. Use when optimising LinkedIn profiles, building content strategy, reviewing posts, crafting headlines, or creating video introductions.
tags: linkedin, profile, content, headline, video, social, career
---

# LinkedIn Coach

Comprehensive LinkedIn optimisation across five modes. Choose the one that fits your situation.

## Capabilities

| # | Capability | When to Use |
|:--|:-----------|:------------|
| A | Full Profile Audit | Complete profile review and optimisation |
| B | Content Review | Analyse existing posts for audience alignment |
| C | Content Strategy | Build sustainable 3x/week posting strategy |
| D | Headline Optimisation | Quick headline-only focus |
| E | Video Introduction | 30-second profile video script |

## Quick Start

```
"Review my LinkedIn profile for [target role]"
"Build me a LinkedIn content strategy"
"Review this post before I publish it"
"Rewrite my LinkedIn headline"
"Help me create a LinkedIn video introduction"
```

---

## A. Full Profile Audit

**What you need:** LinkedIn profile URL + career goals
**Load:** @supporting-prompts/linkedin-profile-review.md
**Template:** @templates/linkedin-updates-template.md

Complete profile sections review:
- Photo, banner, headline, about section
- Skills reordering (RSC API top 3)
- Discoverability and recruiter search optimisation
- Activity and content strategy recommendations

**Output:** `{role-slug}-linkedin-profile-review.md`

---

## B. Content Review (Reactive)

**What you need:** Posts to review + target audience
**Load:** @supporting-prompts/linkedin-posts-helper.md

Analyse existing posts:
- Audience alignment assessment
- Decision-maker pain point identification
- Content improvement recommendations

**Output:** `{role-slug}-content-review.md`

---

## C. Content Strategy Coaching (Proactive)

**What you need:** Role, expertise areas, career goals, target audience
**Load:** @supporting-prompts/content-strategy-coaching.md
**Template:** @templates/content-calendar-template.md

Build a sustainable posting strategy:
- Discover 3-5 authentic content pillars from real expertise
- 3x/week cadence (Tactical/Strategic/Story mix)
- Build engagement network (20-30 strategic connections in 3 tiers)
- 4-week content calendar with specific topics
- Thread series guidance (when/why to use multi-post sequences)
- Voice coaching - write authentically, not from templates

**Output:** `{role-slug}-content-strategy.md` + `{role-slug}-content-calendar.md`

---

## D. Headline-Only Optimisation

**What you need:** Career goals + target audience
**Load:** @supporting-prompts/linkedin-headline.md

Goal-first headline optimisation:
- Job search, thought leadership, client acquisition, networking, or board/advisory
- Headlines as value statements, not job titles
- Goal-aligned formulas for different structures
- Keyword strategy by target audience
- 3 options with trade-off analysis

**Output:** Headline recommendations in conversation (copy-paste ready)

---

## E. Video Introduction Optimiser

**What you need:** Career goals, target audience, key messages
**Load:** @supporting-prompts/linkedin-video.md

30-second profile video script:
- Hook, Value, Proof, CTA structure
- Goal-specific templates
- Recording and delivery guidance
- Technical setup checklist
- 3 script options with trade-offs

**Output:** Video script in conversation (copy-paste ready)

---

## Output Standards

- **UK English** throughout (unless US role explicitly requires US English)
- **No emojis** - Professional tone
- **Cited sources** where applicable
- **Actionable steps** - Concrete next actions, not vague advice

### Template Usage

When a capability specifies a template, you MUST:
1. Load the template first using @ symbol
2. Follow the template structure exactly
3. Preserve template footers

---

## Related Skills

After optimising your LinkedIn, you might want:
- **/application-optimizer** - Optimise your CV to match your updated LinkedIn
- **/career-navigator** - Build a networking strategy and 3-month plan
- **/interview-master** - Prepare for interviews

---

*LinkedIn Coach v1.0.0 | Career Helper Plugin | Prosper AI Consulting, UK*
