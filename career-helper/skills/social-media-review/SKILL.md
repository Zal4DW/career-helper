---
name: social-media-review
description: This skill should be used when the user asks to "review my social media", "check my socials", "how do I look on social media", "clean up my online presence", "is my Instagram/Twitter/Facebook okay for employers", or "social media audit". Provides a lightweight, approachable social media review through the eyes of a recruiter or employer. Especially useful for graduates, early career, and anyone re-entering the job market.
tags: social-media, audit, review, instagram, twitter, facebook, tiktok, graduate, online-presence, recruiter
---

# Social Media Review

A quick, friendly check of your social media through a recruiter's eyes. Find out what's helping, what's hurting, and what to fix - without the full employer footprint deep-dive.

## Capabilities

| # | Capability | When to Use |
|:--|:-----------|:------------|
| 1 | Quick Social Scan | Fast review across all your platforms |
| 2 | Platform Deep-Dive | Detailed review of one specific platform |
| 3 | Privacy & Cleanup Guide | What to lock down, delete, or change |

## Quick Start

```
"Review my social media before I start applying"
"Is my Instagram okay for employers to see?"
"Check my Twitter for anything that might look bad"
"I'm a graduate - what should I clean up online?"
"How do I look on social media to a recruiter?"
```

---

## How It Works

Unlike the full `/employer-footprint` analysis (which runs 8 parallel research agents, maps company culture, and produces a scored dashboard), this skill is **lighter, faster, and more conversational**. Think of it as a quick health check rather than a full medical.

**Best for:**
- Graduates and early career professionals cleaning up before their first job search
- Anyone who hasn't thought about their social media from an employer's perspective
- A quick check before hitting "apply"
- People who want practical cleanup advice, not a formal report

**For a comprehensive analysis** with scoring, company culture mapping, CV cross-referencing, and interview question generation, use `/employer-footprint` instead.

---

## Input Gathering

Collect the following via AskUserQuestion:

**Question 1: Platforms**
"Which social media platforms do you use? Share your usernames or URLs for any you'd like me to check:"
- Instagram handle
- Twitter/X handle
- Facebook (note: I can only check public content)
- TikTok handle
- LinkedIn URL
- YouTube channel
- Any others (Snapchat, Reddit, BeReal, Threads, etc.)

**Question 2: Privacy Awareness**
"Do you know which of your accounts are set to public vs private?"

**Question 3: Context** (optional, helps focus the review)
"Are you targeting any specific type of role or industry? Some industries care more about social media than others."

---

## 1. Quick Social Scan

**What you need:** Social media handles (at least 2-3 platforms)
**Load:** @references/social-scan-methodology.md

A fast recruiter-eye review across all provided platforms:

### What Gets Checked

| Check | Why It Matters |
|:------|:-------------|
| **Profile photos** | First visual impression - professional enough? |
| **Bios** | What does your one-liner say about you? |
| **Public posts (recent 20-30)** | Tone, content, anything an employer would notice |
| **Privacy settings** | Is personal content actually private? |
| **Searchability** | Can you be found by name? Is there name confusion? |
| **Cross-platform consistency** | Same name/photo/story, or contradictory? |

### What We Flag

**GREEN flags** (things that help):
- Professional-looking profiles
- Industry-relevant content or interests
- Consistent personal brand across platforms
- Evidence of hobbies, creativity, or community involvement

**AMBER flags** (worth considering):
- Excessive partying photos (public)
- Political content that could polarise
- Inactive/abandoned profiles that look dated
- Inconsistent information across platforms

**RED flags** (fix before applying):
- Offensive language, slurs, or discriminatory content
- Drug references or illegal activity
- Aggressive or confrontational interactions
- Sexually explicit public content
- Complaints about current/former employers
- Inconsistencies that suggest dishonesty

**Important:** Having a social life is normal and healthy. Recruiters are not looking for robots. They are checking that nothing raises serious concerns. A photo at a festival is fine. A photo doing something illegal is not.

### Output

Results presented in conversation with clear, actionable recommendations. Optionally saved to `{name-slug}-social-media-review.md` if the user wants a file.

---

## 2. Platform Deep-Dive

**What you need:** Username/URL for one specific platform
**Load:** @references/social-scan-methodology.md

A detailed review of one platform. Useful when you know a specific account needs attention.

### Platform-Specific Focus

**Instagram:**
- Public vs private status
- Profile photo and bio
- Grid aesthetic and content themes
- Stories highlights (if public)
- Tagged photos (can others tag you in content you don't control?)
- Comment tone on others' posts

**Twitter/X:**
- Bio and profile presentation
- Recent tweets (last 50): tone, topics, controversy
- Retweets and likes (what you amplify matters)
- Replies (constructive or combative?)
- Ratio of professional to personal content
- Old tweets that might resurface

**Facebook:**
- Privacy settings (what's actually public?)
- Profile and cover photos
- Public posts and check-ins
- Group memberships (visible to others?)
- Tagged photos and posts by others
- About section accuracy

**TikTok:**
- Account privacy status
- Content themes and tone
- Comments on others' videos
- Profile bio and presentation

**LinkedIn** (redirects to /linkedin-coach for full audit):
- If user asks for a LinkedIn review, recommend `/linkedin-coach` for a comprehensive professional audit
- This skill focuses on the "social" platforms recruiters check informally

**Other platforms** (Reddit, YouTube, Threads, etc.):
- Username searchability
- Public content review
- Comment history tone

### Output

Detailed findings for the specific platform, presented in conversation.

---

## 3. Privacy & Cleanup Guide

**What you need:** List of platforms used (handles not required for this capability)
**Load:** @references/privacy-cleanup-guide.md

A practical guide to locking down and cleaning up your social media:

- Platform-by-platform privacy settings walkthrough
- What to make private vs what to leave public
- How to find and review old posts efficiently
- Google yourself: how to check what employers will find
- Managing tagged content you don't control
- Deactivation vs deletion vs privacy (when to use each)
- Building a positive public presence alongside cleanup

### Output

Privacy guide presented in conversation. Optionally saved to `{name-slug}-social-cleanup-guide.md`.

---

## Career Stage Adaptation

This skill adapts its tone and focus based on who is using it:

| Career Stage | Tone | Focus |
|:-------------|:-----|:------|
| **Graduate / Apprentice** | Friendly, non-judgemental, reassuring | University era content, party photos, immature posts. Normalise having a social life while showing what to tidy up. |
| **Early Career (1-5 years)** | Practical, direct | Professional vs personal balance, building a positive presence |
| **Mid-Career** | Professional, efficient | Quick scan for anything that doesn't match their seniority |
| **Career Returner** | Supportive, encouraging | Outdated profiles, dormant accounts, refreshing presence |
| **Experienced / Senior** | Respectful, focused | Thought leadership positioning, legacy content from earlier career |

### Graduate-Specific Guidance

For graduates and early career users, include:

- **"Everyone has this stuff"** - Normalise that university social media exists. Don't catastrophise.
- **"Here's what actually matters"** - Most recruiters spend 30 seconds. Focus on what they'll actually notice.
- **"Quick wins"** - 5 things you can fix in 10 minutes that make the biggest difference.
- **"Leave these alone"** - Content that's fine to keep (having friends, hobbies, and a life is not a red flag).
- **"The 3-second test"** - If a recruiter glances at your profile for 3 seconds, what impression do they get?

---

## Output Standards

- **UK English** throughout (unless US role context)
- **No emojis** - Professional tone
- **Non-judgemental** - Flag issues objectively, don't moralise
- **Actionable** - Every flag comes with a specific fix
- **Privacy-conscious** - Only analyse publicly available content
- **Proportionate** - Don't catastrophise minor issues

### Tone of Voice
- Avoid hyperbole and cinema poster phrasing (not "game-changing", "revolutionary", or "supercharge your career")
- Use the **Oxford comma** (serial comma: "skills, experience, and qualifications")
- Never use em dashes. Use commas, semicolons, colons, or full stops instead

---

## Relationship to /employer-footprint

This skill is the **lightweight version** of the social media audit within `/employer-footprint`:

| Feature | /social-media-review | /employer-footprint |
|:--------|:--------------------|:-------------------|
| Social media check | Yes | Yes (deeper) |
| Google presence search | Basic | Comprehensive |
| CV cross-reference | No | Yes |
| Company culture mapping | No | Yes |
| Scored dashboard (1-10) | No | Yes |
| Interview questions | No | Yes |
| Parallel research agents | No | Yes (8 agents) |
| Best for | Quick check, graduates | Full pre-application audit |

**Upgrade path:** After a social media review, suggest `/employer-footprint` for users who want the full analysis:

"Want a deeper analysis? `/employer-footprint` produces a full scored dashboard, cross-references your CV, and if you have a target company, maps your presence against their values."

---

## Related Skills

After cleaning up your social media:
- **/linkedin-coach** - Full LinkedIn profile optimisation (the professional platform)
- **/employer-footprint** - Complete digital footprint analysis with scored dashboard
- **/application-optimiser** - Research companies and optimise your CV
- **/interview-master** - Prepare for interviews

---

*Social Media Review v1.0.0 | Career Helper Plugin | Prosper AI Consulting, UK*
