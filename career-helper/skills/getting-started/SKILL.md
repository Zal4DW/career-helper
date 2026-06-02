---
name: getting-started
description: This skill should be used when the user asks "how do I get started", "how do I use career-helper", "how do I get the best results", "what should I prepare", "what order should I use the skills", "tips for using career-helper", "show me how this plugin works", "give me the guide", "getting the best guide", or "can I get a guide to share". Provides a comprehensive guide covering preparation checklists, recommended workflows, skill-by-skill tips, power-user strategies, and a downloadable getting the best guide for maximising career-helper output quality.
tags: getting-started, guide, help, how-to, tips, workflow, best-practices, onboarding
---

# Getting Started Guide

Get the most out of Career Helper. Whether you are a graduate writing your first CV, mid-career and planning a move, or an experienced professional navigating a changing market - this guide shows you what to use, when, and how to get the best results.

## Capabilities

| # | Capability | When to Use |
|:--|:-----------|:------------|
| 1 | Full Overview | See everything career-helper can do with real examples |
| 2 | Preparation Checklist | Before you start - gather the right materials |
| 3 | Workflow Planner | Get a personalised skill sequence for your situation |
| 4 | Skill-by-Skill Tips | Maximise results from any specific skill |
| 5 | Power User Strategies | Advanced techniques for experienced users |
| 6 | Getting the Best Guide | Comprehensive downloadable guide with scenario-based walkthroughs |
| 7 | Scheduled Routines (Cowork) | Set up recurring job-search tasks in Claude Cowork |

## Quick Start

```
"How do I get the best out of career-helper?"
"Show me what career-helper can do"
"What should I have ready before I start?"
"What order should I use the skills in?"
"Give me tips for using the application optimiser"
"Show me advanced ways to use career-helper"
"Can I get the getting the best guide?"
"Give me the guide to share with someone"
"Can I automate my job search?"
"Set up a weekly routine for my job search"
```

---

## Accessibility

**At skill start**, check for `career-helper-preferences.md` in the current working directory using the Glob tool. If found, read the YAML frontmatter and apply:

- **dyslexia_friendly: true** → Use short sentences. Number all lists and options (never unnumbered). One decision per message. No idioms or metaphors — use plain replacements. Explicit signposting at every transition. Refer to saved files by description, not filename.
- **colour_blind: true** → Never use colour alone to convey meaning. Use labels, text, or icons for all status indicators.

If **no preferences file exists** and this skill was invoked directly (not dispatched by Tim): ask once — "Do you have any accessibility preferences I should know about? For example, if you're dyslexic I can adjust how I format things." If yes, save to `career-helper-preferences.md` using the format documented in the Tim skill before continuing. If the user declines or says no, proceed without creating the file.

These rules apply to **all communication with the user** and to the **formatting of output documents**.

---

## 6. Getting the Best Guide

**What you need:** Nothing - works for everyone
**Load:** @references/getting-the-best-guide.md
**PDF:** @references/getting-the-best-guide.pdf

A comprehensive guide covering installation, folder setup, and three scenario-based walkthroughs: graduates starting out, experienced professionals between roles, and employed professionals wanting better positioning. Includes skill connection maps, common mistakes to avoid, and practical advice on LinkedIn copy/paste workflows.

**Core approach:**
- If the user asks for the guide, a downloadable version, or "how to get the best out of career-helper", present the key points from the guide conversationally and offer to save the PDF to their working folder
- Use the guide content to answer specific questions about workflows, skill ordering, or what to prepare
- The PDF version can be shared with others who want to use career-helper

**Output:** Conversational guidance from the guide content; optionally saves `getting-the-best-from-career-helper.pdf` to the user's working folder

---

## 1. Full Overview

**What you need:** Nothing - this works for everyone
**Load:** @references/full-overview.md

Walk the user through everything career-helper can do, with concrete real-world examples showing exactly when and how to use each skill. This is the "show me everything" capability.

**Core approach:**
- Present all 11 skills and their capabilities with plain-language explanations
- For each skill, include a real-world scenario showing exactly what to say and what you get back
- Show the complete plugin ecosystem: skills, commands, output files, and how they connect
- End with "What's your situation? I'll tell you exactly where to start"

**Output:** Interactive overview in conversation, ending with routing to the right skill

---

## 2. Preparation Checklist

**What you need:** Your current situation and goals
**Load:** @references/preparation-checklist.md

Help the user gather everything they need before diving into skills. Ask what they plan to work on, then provide a tailored checklist.

**Core approach:**
- Ask what the user wants to achieve (new role, interview prep, career change, LinkedIn improvement)
- Provide a specific, prioritised list of materials to gather
- Explain WHY each item matters and what happens without it
- Distinguish between essential and nice-to-have items

**Output:** Checklist presented in conversation (copy-paste ready)

---

## 3. Workflow Planner

**What you need:** Career situation, goals, timeline, materials available
**Load:** @references/workflow-planner.md

Create a personalised skill sequence based on the user's specific situation. Not a generic list - a tailored plan.

**Core approach:**
- Gather context via AskUserQuestion (situation, goals, urgency, materials on hand)
- Map their situation to the optimal skill sequence
- Explain why each step matters and what it feeds into
- Identify dependencies (e.g. "research brief feeds into CV optimisation")
- Set expectations for what each step produces

**Output:** Personalised workflow plan in conversation

---

## 4. Skill-by-Skill Tips

**What you need:** The skill(s) the user wants tips for
**Load:** @references/skill-tips.md

Practical guidance for getting the best results from each skill. Not a repeat of help - specific tips on inputs, prompting, and iteration.

**Core approach:**
- Ask which skill they want tips for (or cover all eleven)
- Provide input quality tips (what makes a good CV upload, how to share a LinkedIn profile, what details to include in a job description)
- Common mistakes and how to avoid them
- How to iterate and refine outputs
- How each skill's output feeds into the next

**Output:** Tips presented in conversation

---

## 5. Power User Strategies

**What you need:** Some familiarity with career-helper basics
**Load:** @references/power-user-strategies.md

Advanced techniques for users who have used the basic skills and want more.

**Core approach:**
- Multi-role targeting (running skills in parallel for different roles)
- Iterative refinement (feeding outputs back for improvement)
- Cross-skill connections (using research briefs to strengthen interview prep)
- Comparative analysis (running multiple company research briefs to compare opportunities)
- Output management (organising and maintaining generated files)
- Combining skills for specific scenarios (e.g. internal promotion, career pivot, return from break)

**Output:** Strategies presented in conversation

---

## 7. Scheduled Routines (Cowork)

**What you need:** Claude Cowork on Claude Desktop, on a paid plan
**Load:** @references/scheduled-routines.md

Help the user turn their job search into a living process using Claude Cowork's scheduled tasks. Cowork can run a saved prompt on a schedule with full access to the Career Helper skills and the user's workspace folder.

**Core approach:**
- Explain how `/schedule` works and the two honest limitations: the computer must be awake with Claude Desktop open, and scheduling is a Cowork feature, not part of the plugin (CLI and web users can run the same prompts manually)
- Offer the ready-made routines: Monday job-search standup, weekly market monitor, LinkedIn posting reminder, follow-up check, and pre-interview nudge
- Recommend starting with one routine (usually the Monday standup) rather than all five
- Keep the "do not invent" instruction in any prompt the user edits

**Output:** Conversational setup guidance and copy-paste `/schedule` prompts

---

## Response Approach

When the user invokes this skill without specifying a capability:

1. Ask (using AskUserQuestion): "What would be most helpful right now?"
   - "Show me everything career-helper can do" → Capability 1
   - "I want to know what to prepare before I start" → Capability 2
   - "I need a plan for which skills to use and in what order" → Capability 3
   - "I want tips for getting better results from a specific skill" → Capability 4
   - "Give me the getting the best guide" → Capability 6
   - "I want to automate or schedule parts of my job search" → Capability 7

2. If the user is brand new or unsure, default to Capability 1 (Full Overview).

3. If the user describes a specific situation, infer the right capability and proceed.

---

## Career-Level Awareness

This skill adapts to every career stage. Adjust your tone and recommendations based on who is in front of you:

- **Graduates and Apprentices** - May feel overwhelmed or unsure what belongs on a CV. Guide patiently. Their projects, placements, and education ARE valid experience.
- **Early Career** - Eager but often comparing themselves to peers. Help them articulate early wins.
- **Mid-Career** - Balancing ambition with practical constraints. Focus on strategic positioning.
- **Experienced (15+ years)** - May face "overqualified" concerns. Help them signal relevance and energy.
- **Late Career / 50+** - Age discrimination is real. Provide specific mitigation strategies, not platitudes.
- **Career Returners** - Gaps create anxiety. Help frame the narrative positively.
- **Redundancy** - Shock and urgency. Provide immediate structure and acknowledge the emotional reality.

Job searching is emotionally challenging at every level. Never minimise this. A graduate terrified of their first interview deserves the same quality of support as a VP negotiating a package.

---

## Output Standards

- **UK English** throughout
- **No emojis** - Professional tone
- **Practical** - Specific, actionable guidance, not theory
- **Concise** - Respect the user's time; bullet points over paragraphs
- **Honest** - Set realistic expectations about what each skill can and cannot do
- **Inclusive** - Examples and language that work for all career levels, not just senior professionals

### Tone of Voice
- Address the user as "you", not by name: "You might want to start with..." not "Bethan might want to start with..." — default to second person for warmth and engagement; occasional name use is fine for emphasis
- Avoid hyperbole and cinema poster phrasing (not "game-changing", "revolutionary", or "supercharge your career")
- Use the **Oxford comma** (serial comma: "skills, experience, and qualifications")
- Never use em dashes. Use commas, semicolons, colons, or full stops instead

---

## Related Skills

Ready to get started? Use the skill that fits:
- **/employer-footprint** - See what employers will find about you online
- **/social-media-review** - Quick social media check (great for graduates)
- **/application-optimiser** - Research companies and optimise your CV
- **/linkedin-coach** - Optimise your LinkedIn profile and content
- **/interview-master** - Prepare for interviews
- **/career-navigator** - Plan your search, negotiate offers
- **/career-transitions** - Explore portfolio/fractional career paths, entrepreneurship, public sector, charity, and non-linear alternatives
- **/personal-brand** - Build or refresh a personal brand using Why You, Why Them, Why Now positioning, with audience and channel map, content pillars, and a bio library

Or run **/career-helper:quick-start** if you want guided routing.

---

*Getting Started Guide v1.13.0 | Career Helper Plugin | Prosper AI Consulting, UK*
