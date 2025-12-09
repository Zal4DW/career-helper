# Career Helper - Claude Code Skill

End-to-end career support for job seekers at all levels. Research-driven, ATS-optimized assistance for landing your next role faster.

**Created by:** Paul Bratcher | [LinkedIn](https://www.linkedin.com/in/paul-bratcher/) | [GitHub Issues](https://github.com/Zal4DW/career-helper/issues)

---

## 📦 Installation

### Option 1: Upload via Claude Code App (Easiest)

1. Go to [Releases](https://github.com/Zal4DW/career-helper/releases)
2. Download the latest `career-helper.zip`
3. Open Claude Code application
4. Go to **Settings** → **Capabilities** → **Skills**
5. Click **"Upload Skill"** or **"Add Skill"**
6. Select the downloaded `career-helper.zip` file
7. The skill will be automatically installed and activated

### Option 2: Manual Installation

1. Go to [Releases](https://github.com/Zal4DW/career-helper/releases)
2. Download the latest `career-helper.zip`
3. Extract the zip file
4. Copy the `Career-Helper` folder to your Claude Code skills directory:
   - **macOS/Linux:** `~/.claude/skills/`
   - **Windows:** `%USERPROFILE%\.claude\skills\`
5. Restart Claude Code or reload skills

### Option 3: Clone from GitHub

```bash
# Navigate to your Claude Code skills directory
cd ~/.claude/skills/  # macOS/Linux
# or
cd %USERPROFILE%\.claude\skills\  # Windows

# Clone the repository
git clone https://github.com/Zal4DW/career-helper.git Career-Helper
```

### Option 4: Manual Download from GitHub

1. Click the green "Code" button on this repo
2. Select "Download ZIP"
3. Extract the zip file
4. Rename the folder from `career-helper-main` to `Career-Helper`
5. Move to your Claude Code skills directory (see paths above)
6. Restart Claude Code or reload skills

### Verify Installation

**In Claude Code CLI:**
```
/skills
```
You should see `career-helper` in the list.

**In Claude Desktop or Web App:**

To activate and use the skill, simply say:
```
use skill career-helper
```

Or jump straight to using it:
```
"Help me optimize my CV for this job description"
```

The skill will automatically load when you ask questions related to job search, LinkedIn, or career assistance.

---

## ✨ Features

### 🎯 LinkedIn Optimization (3 Modes)

**Mode A: Full Profile Audit**
- Comprehensive review from photo to recommendations
- Headline and about section optimization
- Skills reordering for ATS/recruiter systems

**Mode B: Content Review (Reactive)**
- Analyze existing posts for audience alignment
- Decision-maker pain point identification
- Improvement recommendations

**Mode C: LinkedIn Thought Leader Content Planner (NEW)**

Build your professional presence with authentic, sustainable content strategy:

- **Content Pillar Discovery:** Identify 3-5 authentic topics from your real expertise (not generic)
- **Sustainable Posting Strategy:** 3x/week cadence (Tactical/Strategic/Story post mix)
- **Engagement Network Building:** 20-30 strategic connections organized in 3 tiers
  - Tier 1: Industry leaders (5-7 people) for visibility
  - Tier 2: Peers & target connections (8-12 people)
  - Tier 3: Rising voices (10-15 people) for genuine relationships
- **4-Week Content Calendar:** Specific topics mapped out with post types
- **Thread Series Guidance:** When/why to use multi-post sequences (problem → solution → proof → lessons)
- **Voice Coaching:** Write authentically, not from templates
- **Professional, Non-Cheesy:** Grounded in experience, no hustle culture BS

Creates comprehensive tracking system with:
- Weekly activity plans with time estimates
- Content engagement tracker
- Success metrics dashboard
- Topic bank for future ideas

### 📄 ATS CV Optimization
- Keyword extraction & gap analysis from job descriptions
- CV rewrite optimized for ATS systems (keyword, TF-IDF, semantic ranking)
- LinkedIn/CV consistency checks
- Parsing safety verification

### 🔍 Company Intelligence
- Parallel agentic research: financials, culture, red flags, hiring context
- Glassdoor analysis, market position, leadership profiling
- Hiring manager and stakeholder identification
- All findings cited with sources and dates

### 💼 Interview Preparation
- 15-20 role-specific questions (not generic)
- STAR answer frameworks using your real experience
- Intelligent questions to ask by interviewer type
- Post-interview follow-up templates

### 🎯 Interviewer's Perspective Reports (NEW)
- See interview questions from the interviewer's viewpoint
- What they're REALLY assessing behind each question
- What makes a strong answer (criteria, not scripted responses)
- Red flags interviewers watch for
- How to THINK about your answer (mental frameworks, not memorization)
- Available standalone or integrated into full interview prep

### 🤝 Strategic Networking
- Identify 8-12 high-value LinkedIn connections
- 3-tier prioritization (hiring managers, recruiters, stakeholders)
- Personalized connection messages
- Engagement strategy and timing guidance

### 📋 Application Strategy
- Timeline planning with milestones
- Stakeholder mapping and connection strategy
- Risk mitigation for identified gaps
- Cover letters, follow-up protocols, decision frameworks

### 📅 3-Month Job Search Plan (NEW)
Build a structured, sustainable job search with wellbeing at the core:
- **Audacious Goal Setting:** Define 3-4 meaningful Month 3 goals, then back-solve into smaller milestones
- **12-Week Breakdown:** Specific focus areas and tasks for each week
- **Daily Rhythm Template:** Realistic activity schedules adapted to your career level
- **Wellbeing Integration:** Structure protects mental health; practices woven throughout
- **Research-Backed:** 2025 UK job search data and networking statistics
- **Generational Adaptations:** Tailored advice from Gen Z to Boomers
- **UK Resources:** Government programmes, recruitment partners, mental health support
- **Human-in-the-Loop:** Collaborative planning, not prescriptive templates

Creates comprehensive activity plan with:
- Monthly checkpoints and milestones
- Weekly task checklists (recurring and one-time)
- Progress tracking metrics
- Reflection prompts for continuous improvement

---

## 🎓 Adaptive Intelligence

### Career Stage Guidance
The skill adapts advice based on your career stage:

- **Early Career (Gen Z/Alpha):** Building presence, demonstrating potential, portfolio emphasis
- **Mid-Career (Millennials):** Career pivots, IC→management transitions, explaining gaps
- **Experienced (Gen X):** Age discrimination mitigation, tech fluency signals, avoiding "overqualified"
- **Late Career (Boomers):** Ageism handling, fractional/advisory positioning, board opportunities

### Universal Support
- **All career levels:** Graduate → C-suite → Board
- **All sectors:** Private, public, non-profit, academic
- **All geographies:** UK English default, US adaptable

### Human-in-the-Loop
- Screenshot fallback for blocked content (LinkedIn, Glassdoor, paywalled)
- Read tool processes images, PDFs, copy/paste
- Only requests critical content (top 3-5 priority items)

---

## 🚀 Quick Start Guide

### Using the Skill

In Claude Code, activate the skill:
```
use skill career-helper
```

Or ask directly:
```
"Help me optimize my CV for this job description"
"Who should I connect with on LinkedIn at [Company]?"
"I have an interview next week at [Company], help me prepare"
"What are interviewers really looking for in my answers?"
"Build me a LinkedIn content strategy"
"Help me create a 3-month job search plan"
```

### What You'll Need

**For LinkedIn Review:**
- Your LinkedIn profile URL
- Target role/level

**For LinkedIn Content Strategy:**
- Current role and years of experience
- Expertise areas
- Career goals
- Target audience

**For CV/ATS Optimization:**
- Your current CV (file path)
- Target job description

**For Interview Prep:**
- CV + job description
- Company name
- Interview stage

**For Company Research:**
- Company name
- Job description (optional)

**For Networking Strategy:**
- Company name
- Target role
- Your LinkedIn URL
- Brief background

**For 3-Month Job Search Plan:**
- Current situation (employed, recently redundant, etc.)
- Career stage and target direction
- Financial runway/constraints
- Existing materials (CV, LinkedIn status)
- How you're feeling about the process

### Understanding Outputs

All outputs are saved to `career-outputs/` in your project directory:

```
career-outputs/
├── {role-slug}-research-brief.md
├── {role-slug}-cv-optimized.md
├── {role-slug}-linkedin-updates.md
├── {role-slug}-content-strategy.md
├── {role-slug}-content-calendar.md
├── {role-slug}-networking-intelligence.md
├── {role-slug}-interview-prep.md
├── {role-slug}-interviewer-perspective.md
├── {role-slug}-application-strategy.md
└── three-month-plan.md
```

**Note:** Skills cannot write to their own directory due to Claude Code sandboxing. Outputs always go to the project working directory.

---

## 📖 How It Works

The skill uses **progressive disclosure** - loading specialized prompts only when needed:

1. **Tell me what you need** - The skill asks clarifying questions
2. **Loads only what's needed** - Using @ symbol for on-demand context
3. **Get actionable outputs** - Optimized files, research briefs, prep guides
4. **Iterate together** - Refine based on feedback, dig deeper as needed

**You're in control** - Skip capabilities, go out of order, pivot mid-stream. This is a conversation, not a checklist.

---

## 🎯 Example Workflows

### Full Application Support
```
1. "Research [Company Name] before I apply"
   → Get company intelligence, culture, hiring context, red flags

2. "Optimize my CV for this role at [Company]"
   → ATS-optimized CV + LinkedIn profile updates

3. "Who should I connect with on LinkedIn?"
   → Strategic networking plan with 8-12 prioritized contacts

4. "Help me prepare for the interview"
   → Role-specific questions with STAR answers + talking points

5. "Create an application strategy"
   → Timeline, stakeholder mapping, follow-up protocols
```

### LinkedIn Thought Leadership Strategy
```
1. "Help me build a LinkedIn content strategy - I want to post consistently but don't know what to share"
   → Interactive session to discover your authentic content pillars
   → Build 3x/week posting strategy with specific topics
   → Identify 20-30 strategic people to engage with (3-tier network)
   → Create 4-week content calendar with Tactical/Strategic/Story mix
   → Thread series planning (when to use multi-post sequences)
   → Voice coaching to write authentically, not from templates
   → Outputs: content-strategy.md + content-calendar.md with tracking tables

2. "Review my LinkedIn profile for [target role]"
   → Full profile audit with optimization recommendations

3. "Review this post before I publish it"
   → Audience alignment and improvement suggestions
```

### Interview Preparation Only
```
1. "I have an interview at [Company] for [Role] next Tuesday"
   → Company research + interview prep + questions to ask

2. "What are interviewers really looking for?"
   → Interviewer's Perspective report showing:
   → What they assess, red flags, how to think about answers
   → Mental frameworks instead of memorized scripts
```

### Structured Job Search Plan
```
1. "I've just been made redundant and need help getting organised"
   → Interactive session to understand your situation
   → Define audacious but achievable Month 3 goals
   → Back-solve into weekly milestones and daily tasks
   → Wellbeing practices integrated throughout
   → Output: three-month-plan.md with full activity breakdown

2. "I'm feeling overwhelmed by my job search"
   → Collaborative planning to create structure
   → Realistic daily rhythm for your career level
   → Progress tracking to see momentum
   → Encouragement without toxic positivity
```

---

## 🔧 Advanced Features

### Career Stage Context
When you mention age, experience level, or stage-related concerns, the skill automatically loads career-stage-specific guidance to adapt all advice.

### Deep Research Validation (NEW)
All research uses a rigorous multi-cycle validation workflow:
- **Gap Analysis** - After initial search, explicitly identify what's missing
- **Counter-Evidence Search** - Actively search for information that contradicts initial findings
- **Source Credibility Scoring** - Weight sources by reliability (SEC filings > news > Glassdoor > blogs)
- **Red Flag Hunting** - Proactively search for negative information, layoffs, lawsuits, controversies
- **Citation Requirements** - All factual claims include source URLs and access dates

This ensures you get balanced, validated intelligence - not just the first search results.

### WebFetch Fallback
When content is blocked (LinkedIn profiles, Glassdoor reviews, paywalled articles), the skill asks you to provide it via:
- Screenshot (recommended - Read tool processes images)
- Copy/paste text
- PDF export

### Thread Series Strategy
For LinkedIn content, the skill provides guidance on when to use multi-post thread series:
- Framework series (problem → solution → proof → mistakes)
- Career transition series (4-post narrative)
- Spacing (2-4 days between posts)

---

## 📚 Documentation

For detailed documentation, when using the skill, ask:
```
"How do I use this skill?"
"What can you do?"
```

This loads the comprehensive usage guide with:
- All capabilities explained
- What to have ready for each
- Quick start examples
- Full feature documentation

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Reporting Issues
Found a bug or have a feature request? [Open an issue](https://github.com/Zal4DW/career-helper/issues)

### Suggesting Improvements
Have ideas for new capabilities or improvements? [Start a discussion](https://github.com/Zal4DW/career-helper/discussions)

### Sharing Success Stories
Did this skill help you land a role? We'd love to celebrate with you! Share your story on [GitHub Discussions](https://github.com/Zal4DW/career-helper/discussions) or [LinkedIn](https://www.linkedin.com/in/paul-bratcher/)

### Pull Requests
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📋 Output Quality Standards

All outputs follow these standards:
- **Research-driven** - All claims cited with source URLs and access dates
- **Professional tone** - Appropriate for target role level (no emojis, no marketing fluff)
- **Specific & actionable** - Quantified metrics, concrete next actions
- **Grounded in experience** - Uses your actual CV, not generic examples
- **ATS-safe** - Simple formatting, conventional headings, consistent dates

---

## ⚙️ Technical Details

**Model:** Sonnet (balance of capability, speed, cost)
**Language:** UK English default (US adaptable)
**Sandboxing:** Outputs to `career-outputs/` in project working directory
**Progressive Disclosure:** Loads only needed context via @ symbol
**Agentic Research:** Parallel WebSearch/WebFetch for company intelligence and networking

---

## 📄 License

This skill is provided as-is for use with Claude Code. See repository for license details.

---

## 💬 Support & Contact

- **GitHub Issues:** [Report bugs or request features](https://github.com/Zal4DW/career-helper/issues)
- **GitHub Discussions:** [Ask questions or share feedback](https://github.com/Zal4DW/career-helper/discussions)
- **LinkedIn:** [Connect with Paul Bratcher](https://www.linkedin.com/in/paul-bratcher/)

---

## 🙏 Acknowledgments

Built with [Claude Code](https://claude.com/claude-code) by Anthropic.

Your feedback helps make this skill better for everyone in the job search journey!

---

**Version:** Check [Releases](https://github.com/Zal4DW/career-helper/releases) for latest version
**Last Updated:** 2025-12-01
