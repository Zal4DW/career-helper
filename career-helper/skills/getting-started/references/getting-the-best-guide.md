# Getting the Best from **Career Helper**

Career Helper is a plugin for [Cowork](https://claude.ai), the desktop companion in the Claude app by Anthropic. It gives you a set of AI-powered career skills covering everything from CV optimisation and company research to interview preparation, LinkedIn coaching, and salary negotiation. It runs locally on your machine, saves files to a folder you choose, and builds on its own outputs across sessions.

## First Things First: Getting Career Helper Installed

You need the Claude desktop app with Cowork mode. If you do not have it yet, download it from [claude.ai](https://claude.ai).

Once you are in Cowork, you need to add Career Helper as a personal plugin. It is not in the default "By Anthropic & Partners" tab, so you will not find it by searching there. Here is how:

1. Open Cowork and go to **Manage Plugins** (or Settings > Plugins).
2. Click the **Personal** tab.
3. Click the **+** button to add a new personal plugin.
4. Enter `Zal4DW/career-helper` as the source.
5. That is it. The skills are now available in every Cowork session.

The source repository is at [github.com/Zal4DW/career-helper](https://github.com/Zal4DW/career-helper) if you want to browse the code, check for updates, or raise an issue.

---

## What You Get

Career Helper is not a single tool. It is a set of eleven skills plus a guided coach, each designed for a different part of the career journey. You do not need to use them all, and you do not need to use them in order. Pick the ones that fit your situation, or let Tim (your career coach) figure it out for you. Here is the quick summary; the rest of this guide shows you exactly how to put them together.

| Skill | What It Does |
|:----|:----|
| `/career-helper:career-coach` | **Tim, your career coach.** Understands your situation, runs the right skills in the right order, checks in between each one. Start here if you are unsure |
| `/social-media-review` | Quick social media check through a recruiter's eyes |
| `/employer-footprint` | Full digital footprint audit with a scored dashboard |
| `/application-optimiser` | Company research, ATS CV optimisation, cover letters and supporting statements, and application strategy |
| `/linkedin-coach` | Profile audit, headline crafting, content strategy, and video intro scripts |
| `/interview-master` | Interview prep, mock interviews, post-rejection coaching, reference and referee prep, and ageism support |
| `/career-navigator` | Networking intelligence, 3-month plans, salary negotiation, offer evaluation, an application tracker, and a learnings loop that turns interviews, rejections, and wins into synthesised patterns |
| `/career-transitions` | Fractional/portfolio careers, AI readiness, and non-linear career exploration (entrepreneurship, startups, public sector, charity, intrapreneurship) |
| `/ai-impact-assessment` | Honest assessment of AI disruption risk for your role, with a 6-month mitigation plan |
| `/ned-ai-helper` | AI governance for Non-Executive Directors, Governors, and Trustees |
| `/personal-brand` | Why You, Why Them, Why Now positioning, audience and channel map, content pillars, and a bio library |
| `/getting-started` | Full overview, preparation checklists, workflow planning, and this guide |

**Accessibility:** Career Helper adapts for dyslexia and colour-blindness across every skill. Tim will ask about your preferences at the start, or you can mention them at any point. If you are dyslexic, you will get shorter sentences, numbered options, explicit signposting, and confirmation checks. All scoring and status indicators use text labels, never colour alone.

Now, before you run any of them, there are two things worth knowing.

---

## Using Tim (Your Career Coach)

You do not have to figure out which skills to run or what order to run them in. Tim does that for you.

Run `/career-helper:career-coach` and Tim will ask a few questions about your situation, then start working. He picks the right skill, runs it, shows you what was done, and checks in before moving to the next thing. If something difficult comes up (redundancy, rejection, age concerns), he adjusts the pace and acknowledges it before pressing on.

**When to use Tim:**
- You are new to Career Helper and do not know where to start
- You are not sure what direction you want; Tim can help you find one before diving into applications
- You want someone to manage the process while you focus on the content
- You are dealing with a lot at once and want a guided approach
- You have been here before and want to pick up where you left off

**When to run skills yourself:**
- You know exactly what you need (e.g., "optimise my CV for this job description")
- You want to run one specific skill without the coaching wrapper
- You are a returning user who just needs one thing done

Tim saves your preferences (with your permission) so returning sessions pick up where you left off, including any accessibility preferences and notes about how things were going. Everything in this guide works both ways: with Tim guiding you, or with you running skills directly.

---

## Set Up a Folder (This Really Matters)

Career Helper saves files as it works. Research briefs, optimised CVs, interview prep packs, content calendars, and footprint dashboards all get written to your working folder. If you start a new Cowork session each time without selecting the same folder, those outputs are lost between sessions. Worse, later skills cannot build on what earlier skills produced.

**How to do it:**

1. Create a folder on your computer called something like `Career Helper` or `Job Search 2026`.
2. When you open Cowork, use the "Work in a folder" option and select that folder.
3. Every session after that, select the same folder.

Career Helper organises your files automatically. When you start working on an application, it creates a subfolder for that role inside an `applications/` directory. Everything for that application; your research brief, tailored CV, interview prep, and strategy; lives together in one place. Shared files like your three-month plan and preferences stay in the root folder.

```
Your folder/
├── career-helper-preferences.md
├── three-month-plan.md
├── applications/
│   ├── marketing-manager-greenfield/
│   │   ├── research-brief.md
│   │   ├── cv-optimised.md
│   │   └── interview-prep.md
│   └── head-fundraising-macmillan/
│       ├── research-brief.md
│       └── cv-optimised.md
```

This means your optimised CV from last Tuesday is still there when you run interview prep on Thursday. Your company research brief feeds directly into your application strategy. Your LinkedIn audit references your updated CV. The skills are designed to chain together, and a persistent folder is what makes that possible.

If you forget and work without a folder, you can still use the skills, but you will need to re-upload materials each time and you will lose the cumulative benefit.

### A Note on LinkedIn and Copy/Paste

LinkedIn actively blocks most AI tools from accessing profile data directly. This means Career Helper cannot just read your LinkedIn profile from a URL. For the LinkedIn Coach and Employer Footprint skills to work well, you will need to help out with a bit of copy and paste. The easiest approaches are: export your LinkedIn profile as a PDF (go to your profile, click "More", then "Save to PDF"), copy and paste sections of your profile text into the chat, or take screenshots of your profile and upload them. It is a small extra step, but it means the skills can give you specific, personalised advice rather than generic guidance. The same applies to other people's LinkedIn profiles when running networking intelligence or company research.

---

## Is This You? "I've just finished studying and I need to find my first proper role"

You have a degree (or equivalent), limited professional experience, and honestly quite a lot of uncertainty about where to even start. That is completely normal. Career Helper is built to support you just as much as it supports someone with twenty years of experience. Here is how to get the most from it.

### What to Have Ready

Before you dive in, spend ten minutes gathering these. The skills work without them, but they work much better with them.

- **Your CV** as a Word document or PDF. Even if it is rough, upload what you have. The skill will improve it.
- **A job description** for a role you are interested in. It does not need to be "the one"; any relevant listing will do. Paste it into the chat or save it as a file in your folder.
- **Your LinkedIn profile URL.** If you do not have a LinkedIn profile yet, that is fine; the LinkedIn Coach skill will help you build one.
- **Your social media handles.** Instagram, Twitter/X, TikTok, whatever you use. The social media review needs these to check what a recruiter would see.
- **The name of a company you would like to work for.** Even a rough idea helps the research skills produce targeted output rather than generic advice.

If you do not have all of these right now, start with what you have. You can always come back and run skills again with more materials later.

### Your Recommended Workflow

**Step 1: Social Media Review**

Before anything else, run `/social-media-review`. This is the lightweight social check designed specifically for people in your position. It looks at your public profiles through a recruiter's eyes and tells you what to tidy up. It will not catastrophise about a photo from a night out; it focuses on what actually matters and gives you quick wins you can fix in ten minutes.

If you want the full scored dashboard with Google presence mapping and CV cross-referencing, you can upgrade to `/employer-footprint` later. For now, the social media review is the right starting point.

**Step 2: CV Optimisation**

Run `/application-optimiser` with your CV and a job description you are interested in. Even if you are not applying to that exact role, the ATS optimisation process teaches you how to structure your CV properly. The skill has a specific early career persona that understands university projects, placements, and part-time work are valid experience. It will not leave you with a blank page because you have not been a marketing director.

Upload your CV as a Word document or PDF. Paste the job description into the chat. The skill produces an ATS-optimised version of your CV and a set of LinkedIn update recommendations so the two stay consistent.

**Step 3: Company Research**

When you find a company you want to apply to, run `/application-optimiser` again but this time ask it to research the company. It runs parallel searches covering leadership, culture, Glassdoor analysis, market position, and red flags. You get a research brief you can use to tailor your application and prepare for interviews.

**Step 4: LinkedIn Coach**

Run `/linkedin-coach` for a full profile audit. For graduates, the focus is on building presence rather than overhauling an established profile. The headline optimisation alone is worth running. Most graduates have a headline that reads "Recent Graduate from University of X" when it should be positioning them for the role they want.

The content strategy capability is also valuable here. You do not need to be a thought leader to post on LinkedIn. Three posts a week about what you are learning, what interests you in your field, and what problems you would like to solve builds a signal that recruiters notice.

**Step 5: Interview Prep**

When you get an interview, run `/interview-master`. It generates 15 to 20 likely questions tailored to the specific role, builds STAR answer frameworks using your actual experience (including university projects), and can run a mock interview simulation. The early career persona adapts all advice to your level. You will not be told to "reference your P&L management experience".

**Step 6: When Things Do Not Go to Plan**

Rejection is a normal part of job searching, especially early on. If you do not hear back, or you get a "no" after an interview, run `/interview-master` in post-interview coaching mode. Tell it what happened, share any feedback you received, and it will diagnose whether it was a skill gap, a signal gap (you had the experience but did not frame it well), or a fit/timing gap (right person, wrong moment). It then feeds those learnings back into your CV and interview prep so the next application is stronger.

This is not a one-and-done process. The folder you set up keeps everything connected, so each iteration builds on the last.

### A Few More Things Worth Knowing

- You can run `/career-navigator` to build a 3-month job search plan. It includes wellbeing practices, which matters because job searching as a graduate is emotionally harder than most people acknowledge.
- If you are unsure where to start at all, run `/career-helper:career-coach` and Tim will guide you through the whole process.
- Do not skip the social media review. Recruiters do check, and it takes five minutes.

---

## Is This You? "I've just finished my apprenticeship and I'm looking for my next role"

You have something most graduates do not: real work experience. You have been in a workplace, you have delivered actual outputs, and you have professional references. That is a genuine advantage. But apprenticeship CVs have their own challenges: your experience might be deep but narrow, your job title might not reflect what you actually did, and you may not know how to position yourself against people with degrees.

Career Helper understands apprenticeships. You will not get advice designed for someone with a dissertation and a summer internship.

### What to Have Ready

- **Your CV** as a Word document or PDF. Even if it is rough. Include your apprenticeship details, any projects you worked on, and your end-point assessment result if you have one.
- **A job description** for a role you are interested in. Does not need to be perfect; any relevant listing helps the skills calibrate.
- **Your LinkedIn profile URL.** If you do not have one yet, the LinkedIn Coach will help you build one that leads with your practical experience.
- **Your social media handles.** Same as for graduates; recruiters check.
- **Details of your apprenticeship.** Level, standard, employer, what you actually did day to day. The skills use this to find transferable skills you might not realise you have.

### Your Recommended Workflow

**Step 1: Social Media Review**

Same as for graduates. Run `/social-media-review` first. Quick, painless, and it catches anything that might put an employer off before you start applying.

**Step 2: CV Optimisation**

Run `/application-optimiser` with your CV and a target job description. The key difference from the graduate workflow: your apprenticeship experience is professional experience, and the skill treats it that way. It will not bury your work history under an "Education" heading.

The skill focuses on extracting achievements from your apprenticeship. "Completed Level 3 Business Administration" is a qualification. "Managed supplier onboarding for 40 accounts, reducing processing time by 30%" is an achievement. The skill helps you find those achievements in your experience.

**Step 3: Company Research**

When you have a target company, run `/application-optimiser` for company research. The intelligence brief helps you write targeted applications and prepare for interviews. Even at early career level, showing you know the company's priorities makes you stand out.

**Step 4: LinkedIn Coach**

Run `/linkedin-coach` for a profile audit. Your headline should not say "Recently Completed Apprenticeship". It should say what you do and what value you bring. The skill helps you position your practical experience as the asset it is.

**Step 5: Interview Prep**

Run `/interview-master` when you get an interview. The early career persona understands that your STAR examples come from your apprenticeship, not from managing a department. It builds realistic answer frameworks from your actual experience.

**Step 6: When Things Do Not Go to Plan**

Rejection hurts at any stage, but it can hit harder when you are early in your career and still building confidence in your professional identity. Run `/interview-master` in post-interview coaching mode. It diagnoses what happened and feeds the learning into your next application.

### A Few More Things Worth Knowing

- Your apprenticeship portfolio, end-point assessment, and any workplace projects are valid evidence for STAR answers. The interview prep skill will help you frame them.
- If you are considering a different direction from your apprenticeship field, run `/career-transitions` to explore your options. Your practical skills transfer more broadly than you might think.
- If the whole process feels overwhelming, run `/career-helper:career-coach` and let Tim guide you through it step by step.

---

## Is This You? "I'm experienced, I'm between roles, and I need to get moving"

You have years of solid experience behind you, but right now you are between roles. Maybe it was redundancy, maybe a contract ended, maybe you took a break and now you are ready to get back in. Whatever brought you here, you want to move with purpose, not panic. Career Helper has specific adaptations for your situation, including support for age-related concerns if they are relevant.

### What to Have Ready

You probably have most of this already, but pulling it together in one place before you start saves time and means the skills can do their best work from the first session.

- **Your current CV** as a Word document or PDF. If you have multiple versions, use the most recent one. The skill will tailor it from there.
- **Target job descriptions.** Save two or three listings that interest you. Paste them into the chat or drop them in your folder. The more specific the job description, the better the ATS optimisation and interview prep.
- **Your LinkedIn profile URL.** Copy the URL from your browser. If you have a PDF export, even better, but the URL is enough to start.
- **Your social media handles.** LinkedIn, Twitter/X, and anything else that is public. The employer footprint analysis needs these.
- **Target company names.** Even one is enough to start. The company research skill produces intelligence briefs that feed into everything else.
- **Any feedback from recent applications or interviews.** Rejection emails, recruiter notes, your own recollection of how an interview went. The post-interview coaching skill uses this to diagnose what happened and what to change.
- **Salary expectations and current/previous compensation.** If you plan to negotiate an offer, having your numbers ready means the negotiation coach can give you specific guidance rather than ranges.

### Your Recommended Workflow

**Step 1: Employer Footprint Analysis**

Start with `/employer-footprint`. This is the full digital audit, not the lightweight social scan. It runs eight parallel research agents across Google, LinkedIn, Twitter, GitHub, news media, and more, producing a scored dashboard with text-label ratings (GREEN/AMBER/RED) across eight dimensions. At your level, your digital footprint is part of your candidacy whether you like it or not. This tells you exactly what an employer will find and what to do about it.

If you have a target company in mind, provide it. The skill maps your online presence against the company's stated values and culture.

**Step 2: Company Research and CV Optimisation**

Run `/application-optimiser` with both your CV and a target job description. At senior level, the ATS optimisation becomes even more important because your CV is likely longer and more complex, which means more opportunities for keyword mismatches. The skill extracts keywords and concepts from the job description and rewrites your CV to hit 70%+ coverage while keeping your achievements quantified and your narrative coherent.

If you have been made redundant or have a career gap, the skill has a career returner persona that loads specific guidance on framing gaps positively and handling the narrative.

Run the company research capability too. The intelligence brief covers leadership, financial health, hiring context, and red flags. When you are applying to roles at director level and above, knowing who the hiring manager reports to and what the board's strategic priorities are gives you a tangible edge.

When a role needs a cover letter or a supporting statement, run `/application-optimiser` for that too. It drafts from your verified CV and the research brief, sources your motivation from you rather than inventing it, and is the right place to address an overqualification concern or a career gap that the CV cannot explain on its own.

**Step 3: LinkedIn Overhaul**

Run `/linkedin-coach` for the full profile audit. At your level, the content strategy capability is particularly valuable. Three posts a week, mixing tactical advice, strategic observations, and stories from your career, positions you as active and relevant. This directly counters any perception that you are "winding down" or out of touch.

The headline optimisation capability is also critical. "Experienced Operations Director" says nothing. A headline that communicates the value you deliver and the problems you solve is what makes recruiters stop scrolling.

**Step 4: Networking Intelligence**

Run `/career-navigator` and ask for strategic networking intelligence for your target companies. It identifies 8 to 12 people you should connect with, prioritised in three tiers (decision makers, influencers, and warm introduction paths), with personalised connection message templates.

Also build a 3-month job search plan. At senior level, this is not about applying to 50 roles a week. It is about targeted approaches, relationship building, and strategic positioning. The plan includes weekly task breakdowns, progress tracking, and wellbeing practices.

**Step 5: Interview Preparation**

When you secure an interview, run `/interview-master`. The preparation pack includes 15 to 20 role-specific questions with STAR frameworks built from your actual experience. The interviewer's perspective report is especially useful at senior level because it shows you what the panel is really assessing behind each question.

The mock interview simulation can be set to "sceptical" or "panel" mode for realistic practice.

**Step 6: If You Suspect Age Is a Factor**

Let's be direct about this. If you are over 45 and job searching, you may have already noticed that something feels off. Interviews that go well but lead nowhere. Feedback about being "overqualified". A sense that younger candidates are getting through while you are not.

Career Helper does not pretend this does not happen. `/interview-master` has comprehensive ageism support covering three areas: UK employment law (the Equality Act 2010, your rights, the reality of proving discrimination, and when it is worth pursuing a complaint), practical strategies (CV techniques, interview tactics, digital presence updates, and skills to prioritise that signal relevance), and emotional resilience (the psychological impact of age-related rejection, support resources, and cognitive reframing approaches). You can access this by mentioning age concerns in any conversation with the interview master skill.

This is not a token feature. It is built from real experience of what people face.

**Step 7: After Every Interview**

Win or lose, run `/interview-master` in post-interview coaching mode after every interview. Share what happened, any feedback you received, and your own impression of how it went. The skill diagnoses whether the issue was a skill gap, a signal gap (strong background but poor framing), or a fit/timing gap (right person, wrong moment). It cross-references gaps against the World Economic Forum Future of Jobs 2025 report to prioritise development that matters both now and long term.

Critically, it feeds those learnings back into your CV and interview prep. Each rejection makes the next application stronger, but only if you capture the insight. Your folder keeps the full chain: research brief, CV, interview prep, post-interview debrief, updated CV.

### A Few More Things Worth Knowing

- Run `/career-transitions` if you are considering going fractional or portfolio. It covers readiness assessment, rate setting, IR35 considerations, and client acquisition strategy.
- Use `/career-navigator` to evaluate and negotiate offers. The salary negotiation coach is region-aware (UK, US, EU, APAC) and covers total compensation including pension, equity, notice periods, and garden leave.
- When you are juggling several applications, run `/career-navigator` and build an application tracker. It is a single plain-text board of every role, its stage, and its next action, stored locally and read by `/career-helper:status`. It is the private alternative to a job-search spreadsheet.
- When references are requested, run `/interview-master` for reference and referee prep. It helps you choose credible referees, ask them well, and brief each one on what the role values, with practical options when you cannot use your current employer yet.
- Your research briefs, CV versions, and interview prep all save to per-application folders. When you are managing five active applications simultaneously, each one has its own folder with everything in one place. That is the difference between preparation and chaos.
- If you would rather have someone manage the sequencing for you, run `/career-helper:career-coach`. Tim handles the routing and checks in between each skill, useful when you are juggling a lot and do not want to think about what to run next.

---

## Is This You? "I'm happily employed, but I want to be more visible and better positioned"

You are not in crisis mode. You have a job, it is fine, but you know you could be doing more to build your profile. You want to be the person who gets approached, not the person endlessly scrolling job boards. Career Helper is not just for active job seekers, and this section is for you.

### What to Have Ready

Your prep is lighter because you are not under time pressure, but having these ready makes the first session much more productive.

- **Your LinkedIn profile URL.** This is the starting point for everything in your situation. Copy your profile URL from a browser.
- **A rough idea of what "better positioned" means for you.** Are you aiming for a promotion? A move to a different company? A board role? Speaking at conferences? The more specific you are, the more tailored the advice.
- **Your social media handles.** Even if you think your socials are fine, the footprint check might surprise you.
- **Your CV** (optional but useful). Even if you are not applying anywhere, the AI readiness assessment and content strategy skills work better when they know your full background.
- **Examples of content you admire.** If there is someone on LinkedIn whose posts you think are good, note their name or save a couple of examples. The content strategy skill can use these as reference points for finding your own voice.

### Your Recommended Workflow

**Step 1: LinkedIn Profile Audit**

Run `/linkedin-coach` and ask for a full profile audit. The skill reviews your photo, banner, headline, about section, skills ordering, and activity. More importantly, it assesses your discoverability: can recruiters find you for the roles you want?

The headline optimisation is a quick win. If your headline is just your current job title, you are invisible to anyone searching for your expertise rather than your employer.

**Step 2: Content Strategy**

This is where the real value is for your situation. Run `/linkedin-coach` and ask it to build a content strategy. The skill discovers 3 to 5 authentic content pillars based on your real expertise (not generic "leadership" or "innovation"), builds a 3x per week posting cadence with a tactical/strategic/story mix, identifies 20 to 30 strategic connections to build an engagement network, and produces a 4-week content calendar with specific topics.

The output includes voice coaching so you write authentically rather than sounding like every other LinkedIn poster using the same templates.

**Step 3: Employer Footprint Check**

Run `/employer-footprint` to see how your digital presence looks to the outside world. Even if you are not applying anywhere, knowing your baseline is valuable. The thought leadership scoring dimension tells you exactly where you stand and what would move the needle.

**Step 4: AI Readiness Assessment**

Run `/career-transitions` and ask for an AI readiness assessment. This evaluates your current AI proficiency against your role and target direction, produces a tiered upskilling roadmap, and gives you CV and LinkedIn integration strategies. Whether or not you are changing roles, demonstrating AI fluency is becoming a differentiator across almost every profession.

**Step 5: Strategic Networking**

Run `/career-navigator` for networking intelligence, even without a specific target company. Ask it to help you identify the right people to connect with in your industry. Building relationships before you need them is the definition of strategic networking.

**When an Opportunity Does Come Along**

You are not actively searching, but opportunities will appear. When one does, you have everything you need. Run `/application-optimiser` to research the company and optimise your CV for that specific role. Run `/interview-master` to prepare. And if it does not work out, run the post-interview coaching to understand why, so you are even better prepared for the next one.

Because you have been maintaining your folder all along, the skills already know your background, your content strategy, and your professional positioning. You are not starting from scratch; you are just adding a targeted application to an already strong foundation.

### A Few More Things Worth Knowing

- The content strategy output includes a content calendar. Treat it seriously. Consistency over three months builds more visibility than one viral post.
- Run `/linkedin-coach` in content review mode after you have been posting for a few weeks. It analyses your existing posts for audience alignment and suggests improvements.
- Ask for a video introduction script. A 30-second profile video significantly increases profile engagement.
- You do not need to be in a crisis to use Career Helper. The skills for content strategy, AI readiness, and networking intelligence are just as useful for career maintenance as they are for active job searching.
- Tim (`/career-helper:career-coach`) works just as well for strategic positioning as for active job searching. He can sequence LinkedIn optimisation, content strategy, and networking intelligence into a coherent plan.

---

## Is This You? "I'm returning to work after a break"

Whether you took time out for parenting, caring, health, travel, or simply because you needed to stop for a while, the gap feels bigger from the inside than it does from the outside. Employers care less about gaps than you think, but they do care about how you frame them. Career Helper has specific personas across multiple skills designed for exactly your situation.

### What to Have Ready

- **Your most recent CV.** Even if it is years old. The skill needs a starting point.
- **A job description** for the kind of role you are targeting. Does not need to be exact; even a rough direction helps.
- **A brief summary of your break.** You do not need to justify it. Just a line or two so the skills can help you frame it positively.
- **Any skills you developed during your break.** Project management through home renovation, financial management, volunteering, freelance work, courses: all of it counts if positioned well.

### Your Recommended Workflow

**Step 1: Employer Footprint**

Run `/employer-footprint` first. After a career break, your online presence may be outdated: an old LinkedIn profile with a previous job title, dormant professional accounts, or nothing at all. The footprint audit shows you what employers will find right now and what needs updating before you start applying.

**Step 2: CV Optimisation**

Run `/application-optimiser` with your CV and a target job description. The career returner persona loads automatically when you mention a career break. It focuses on framing your gap as a chapter, not a void: what you did, what you gained, and how it connects to what you are doing next.

The skill produces a 30-second gap explanation you can use in applications and interviews. This is one of the most useful outputs for returners: a confident, prepared response to the question you are dreading.

**Step 3: LinkedIn Rebuild**

Run `/linkedin-coach`. If your profile is dormant, the skill helps you rebuild it from the ground up with a headline that positions you for where you are going, not where you were. If it is reasonably current, it focuses on updating your narrative to include your return.

**Step 4: Interview Preparation**

Run `/interview-master` when you get an interview. The career returner persona generates specific preparation for gap-related questions, confidence-building exercises, and STAR frameworks that draw on both your professional history and your break experiences.

**Step 5: Building a Plan**

Run `/career-navigator` for a 3-month job search plan. Returning to work is a process, not a single application. The plan includes pacing that accounts for the adjustment period and wellbeing practices that help with the transition.

### A Few More Things Worth Knowing

- If the whole thing feels overwhelming, run `/career-helper:career-coach` and let Tim manage the process. He will ask about your situation, check how you are doing, and sequence the right skills at the right pace.
- You do not need to explain your break to Career Helper in detail. "Career break, parenting" or "Health break, now recovered" is enough for the skills to adapt.
- If you are also dealing with confidence issues after your break, Tim's wellbeing awareness means he will notice and adjust: slower pace, more check-ins, more encouragement grounded in your actual strengths.

---

## Is This You? "I'm thinking about doing something completely different"

Maybe you are tired of the corporate ladder. Maybe you have always wanted to run your own business. Maybe you are curious about the public sector, the charity world, or building something from scratch. Maybe you just know that "more of the same" is not the answer, even if you are not sure what is.

Career Helper does not assume everyone wants a bigger version of their current job. The Career Transitions skill has a full non-linear career explorer covering entrepreneurship, startups, public sector, charity, intrapreneurship, and multi-role skilling, with honest assessments, not cheerleading.

### What to Have Ready

- **Your CV.** Even if you are moving away from your current field, your transferable skills are the foundation.
- **A rough idea of what "different" means to you.** Even "I think I want to work for myself" or "I'm curious about the charity sector" is enough to start.
- **Your financial situation (roughly).** Some paths require a runway. The skill includes financial readiness assessments so you can make informed decisions, not leap-of-faith ones.

### Your Recommended Workflow

**Step 1: Explore Your Options**

Run `/career-transitions` and tell it you want to explore alternatives. The non-linear career explorer covers:

- **Entrepreneurship**: business readiness assessment, legal structures, funding, financial modelling, failure rate data
- **Startup founding**: VC vs bootstrapping, co-founder dynamics, accelerators, equity and dilution, realistic success rates
- **Public sector**: private-to-public transition, Success Profiles framework, Civil Service values, salary comparison
- **Charity and non-profit**: career paths, the "passion tax" reality, sector resources
- **Intrapreneurship**: innovating within your current organisation
- **Multi-role skilling**: skill stacking, unique intersections, hybrid career models

The output includes a weighted decision matrix with reversibility assessment, so you know which options you can try and walk back from, and which ones are harder to reverse.

**Step 2: AI Impact Assessment**

Run `/ai-impact-assessment` to understand whether AI disruption is a factor in your decision. If your current role is at risk, that changes the urgency. If your target direction is AI-resilient, that is useful data.

**Step 3: Transferable Skills Audit**

The career transitions skill includes a transferable skills audit that identifies meta-skills and unique intersections. "15 years in supply chain" might seem narrow, but the planning, stakeholder management, systems thinking, and crisis response skills transfer to dozens of directions.

**Step 4: Financial Readiness**

If your chosen direction involves self-employment, the skill includes financial readiness assessment with regional guidance. It is honest about what things cost and how long before you earn.

**Step 5: Narrative Development**

Whatever direction you choose, you need a story. The skill produces career narrative versions: 30-second, 2-minute, LinkedIn, and interview formats. "I spent 15 years in supply chain and now I'm exploring consulting" is not a story. "I realised that the problem-solving I loved was being automated, so I'm repositioning the strategic thinking that AI cannot do." That is a story.

### A Few More Things Worth Knowing

- If you are not sure whether to stay or go, that is a valid starting point. The skill does not assume you have decided.
- Run `/career-helper:career-coach` if you want Tim to help you think it through. He can run the AI impact assessment, career transitions explorer, and LinkedIn repositioning in sequence.
- **The skill starts with a reality check.** Before exploring options, it walks you through the actual realities of working hours, sales, loneliness, family impact, and failure. This is not to put you off; it is to make sure your decision is clear-eyed. If you still want to do it after that conversation, you are better prepared than most.
- **Thinking about joining a startup rather than founding one?** The skill covers that too, including the equity conversation: vesting schedules, liquidation preferences, dilution, exercise windows, and the honest maths of salary-vs-equity trade-offs. Most startup equity is worth nothing. That does not mean you should not join one, but you should join for the learning and network, not the lottery ticket.

---

## Is This You? "I'm overwhelmed and don't know where to start"

This is exactly what Tim is for.

Run `/career-helper:career-coach`. Tim will ask you three questions: your situation, what would help most, and whether you have any accessibility preferences. Then he starts working. You do not need to know which skill to run. You do not need a plan. Tim builds the plan from what you tell him.

If you have just been made redundant, are dealing with multiple rejections, or are simply paralysed by the number of things you think you should be doing, Tim adjusts the pace. He does not rush you through a checklist. He acknowledges what is hard, then helps you do one concrete thing. Then another. Progress builds confidence; stalling erodes it.

If you would rather not use Tim, start with `/getting-started` for a full overview, or `/social-media-review` for a quick win that takes five minutes and gives you something tangible to show for your first session.

---

## Is This You? "I don't know what I want to do next"

This is different from being overwhelmed by the process. Here the problem is direction: you can say what you do not want, but not what you do. That is common, especially after redundancy, a long stretch in one role, or a career break.

Run `/career-helper:career-coach` and tell Tim you are not sure what you want. Rather than pushing you into a CV or an application, which give you little when you have no target, Tim can walk you through four short direction-finding questions based on the ikigai idea:

1. What do you enjoy doing?
2. What are you good at?
3. What problems do you care about?
4. What can you realistically be paid for?

Tim looks for the overlaps in your answers, then routes you to the right next step: `/application-optimiser` if a clear role emerges, `/career-transitions` if you are drawn to non-traditional paths, or `/career-navigator` for a plan if you have the skills but not the market clarity. If a clear topic and audience emerge and you want to be known for it, those same four answers feed straight into `/personal-brand`, so the brand work does not start from a blank page.

It is offered, not imposed. If it is not clicking, Tim drops it and simply talks the decision through with you instead. If you find the exercise useful, Tim can also turn your answers into the classic ikigai diagram as an interactive page you can keep and revisit.

---

## Is This You? "I keep getting rejected and I don't know why"

Run `/interview-master` in post-interview coaching mode. Tell it what happened: the role, the stage you reached, any feedback you received, and your own impression of how it went.

The skill diagnoses whether the problem is:

- **A skill gap**: you lack something they need (and it tells you what to develop)
- **A signal gap**: you have the experience but are not framing it well (CV positioning, interview delivery, or both)
- **A fit/timing gap**: you were the right person at the wrong moment (nothing to fix, but patterns worth watching)

If you have been rejected multiple times, share all of them. The skill looks for patterns across rejections, not just individual failures. A pattern of "great interview but didn't progress" points to a different problem than "never hear back after applying".

After diagnosis, the skill feeds improvements directly back into your CV and interview prep. Each rejection genuinely makes the next application stronger, but only if you capture what went wrong.

Over a long search, run `/career-navigator` and use the application learnings loop to keep this honest. It turns each interview, rejection, and win into a short structured note, then periodically synthesises those notes into a single patterns file so you can see what is actually working across dozens of applications, rather than relearning the same lesson each time. The synthesised patterns feed back into `/interview-master` (recurring objections worth drilling) and `/application-optimiser` (a gap your CV keeps underselling), and `/career-helper:status` surfaces the most useful current pattern when you check where you are.

If the rejections are hitting you emotionally (and they do, for everyone), run `/career-helper:career-coach` instead. Tim will run the rejection analysis but will also check how you are doing and adjust the pace.

---

## Is This You? "I'm worried AI is going to affect my job"

Run `/ai-impact-assessment`. Give it your current job title, a brief description of what you do day to day, and your industry. It researches current AI capabilities against your specific tasks and gives you a straight answer.

The output includes:

- **What is at risk**: specific tasks in your role that AI can already do or will be able to do soon, with evidence and timelines
- **What is resilient**: the parts of your role that remain human-centric and why
- **A certainty level**: how confident the assessment is, based on evidence quality
- **A 6-month mitigation plan**: month-by-month actions to protect your position, build new capabilities, and make your AI awareness visible to employers

This is not a generic "AI is coming for everyone" scare piece. It is specific to your role, based on current research, and honest about what it does and does not know.

If the assessment shows significant risk, the skill routes you to `/career-transitions` for AI readiness upskilling or non-linear career exploration. If it shows your role is resilient, it tells you that too, and suggests how to position your human-centric skills as a differentiator.

---

## Is This You? "I think my age is working against me"

You might be right. Age discrimination in hiring is real, it is widespread, and it is difficult to prove. Career Helper does not pretend otherwise.

Run `/interview-master` and mention your age concerns. The ageism persona loads automatically and covers three areas:

**UK employment law:** The Equality Act 2010, your rights, the burden of proof, Employment Tribunal process, time limits, compensation, and an honest assessment of the practical reality versus the letter of the law. This is not legal advice, but it is thorough enough to help you decide whether a formal route is worth pursuing.

**Practical strategies:** CV techniques that reduce age signals without hiding experience (functional formats, achievement-led structure, skills currency), interview tactics for "overqualified" concerns, digital presence updates that signal relevance, and specific skills to develop that counter the "out of touch" perception.

**Emotional resilience:** The psychological impact of age-related rejection is different from other rejection: it hits identity, not just career prospects. The skill includes support resources (NHS Talking Therapies, Samaritans 116 123), cognitive reframing approaches, and honest acknowledgment that this is genuinely hard.

If you are also between roles and need the full job search support, run `/career-helper:career-coach`. Tim understands age-related concerns and will weave the ageism support into the broader coaching, not as a separate topic but as context that shapes everything from CV optimisation to interview prep.

---

## Is This You? "I've been offered a role. Should I take it?"

Run `/career-navigator` and ask for offer evaluation. Upload or paste the offer details: salary, benefits, bonus, equity, pension, notice period, location, and anything else included.

The skill produces a weighted decision framework covering:

- **Total compensation analysis**: not just salary but the full package, region-adjusted (UK, US, EU, APAC) including pension contributions, equity vesting, bonus structure, and benefits value
- **Role fit assessment**: how well the role matches your stated goals and career direction
- **Red flags**: anything in the offer or from your research that warrants caution
- **Comparison framework**: if you have multiple offers, a side-by-side weighted comparison

If you want to negotiate, the salary negotiation coach walks you through the conversation: what to ask for, how to frame it, what levers to pull beyond base salary, and when to accept.

If you are unsure whether to take it at all, that is a harder question. Run `/career-helper:career-coach` and Tim can help you think through the decision in the context of your broader situation, not just whether the money is right, but whether the role is right for where you want to go.

---

## Is This You? "I want to slow down: fewer days, better balance, or a step toward retirement"

Not every career move is a step up. Sometimes the right move is a step back, deliberately, on your terms. You might want to drop to four days a week. You might want to transition from a full-time role to consulting two days a week. You might be thinking about phased retirement but you are not ready to stop completely. Or you might just want to reclaim time for family, health, or the things you have been putting off for twenty years.

Career Helper can help you plan this, even though "slowing down" is not a crisis. The challenge is positioning a step back so it does not look like a step down, and finding the right arrangement rather than just accepting less.

### Your Recommended Workflow

**Step 1: Understand Your Options**

Run `/career-transitions` and explain what you are looking for. The non-linear career explorer covers:

- **Portfolio and fractional careers**: working 2-3 days a week across multiple clients instead of one full-time role. This is not freelancing; it is structured, senior, and increasingly common at director level and above. The skill covers rate setting, IR35 considerations, and client acquisition.
- **Multi-role skilling**: combining part-time employment with consulting, board roles, mentoring, or teaching. The skill helps you identify which combination of your skills has the most value at reduced hours.
- **Phased retirement planning**: how to negotiate a transition from five days to three, or from executive to advisory, without losing your professional identity or your leverage.

The output includes a financial readiness assessment. Slowing down means earning less, and the skill is honest about what that looks like.

**Step 2: LinkedIn Repositioning**

Run `/linkedin-coach` once you know your direction. Your LinkedIn profile needs to signal "strategic choice" not "winding down". The skill helps you rewrite your headline and about section to position reduced availability as a feature: "I now work with select clients on strategic operations challenges" reads very differently from "Looking for part-time opportunities".

The content strategy capability is especially useful here. Thought leadership on your terms (two posts a week about what you have learned over your career) builds the inbound enquiries that make fractional and portfolio work sustainable.

**Step 3: Networking Intelligence**

Run `/career-navigator` for networking intelligence. The contacts you need when slowing down are different from job search contacts: you are looking for people who commission fractional work, chair boards that need non-executive directors, or run organisations that value experience on a part-time basis.

**Step 4: If You Are Negotiating with Your Current Employer**

If you want to reduce your hours with your current employer rather than leave, run `/career-navigator` for negotiation support. Frame it as a business case: what you will deliver in fewer days, how the arrangement benefits them (retention of institutional knowledge, reduced cost), and what the transition looks like. The skill helps you structure the conversation.

### A Few More Things Worth Knowing

- A NED, governor, or trustee role can be an excellent complement to reduced working hours. If that interests you, run `/ned-ai-helper` for AI governance support or ask Tim about board-level positioning.
- Run `/ai-impact-assessment` to check whether the parts of your role you want to keep are the parts that will remain human-centric. No point building a three-day-a-week consultancy around tasks that AI will handle in two years.
- If you are approaching this because of health, caring responsibilities, or burnout (not just preference), run `/career-helper:career-coach`. Tim adjusts the pace and acknowledges that this is about more than career strategy.

---

## How the Skills Connect

Career Helper skills are designed to feed into each other. Here is the chain:

| What You Run First | What It Feeds Into |
|:----|:----|
| Social media review or employer footprint | Identifies what to fix before applications |
| Company research (application optimiser) | Informs CV tailoring, interview prep, and networking |
| CV optimisation (application optimiser) | Produces a CV that LinkedIn coach and interview master reference |
| Cover letter (application optimiser) | Says what the CV cannot: motivation, fit, and context for a gap or pivot |
| LinkedIn coach (profile audit) | Creates consistency between CV and LinkedIn |
| LinkedIn coach (content strategy) | Builds ongoing visibility and thought leadership |
| Career navigator (networking intelligence) | Identifies who to connect with at target companies |
| Career navigator (3-month plan) | Structures the entire search with wellbeing built in |
| Interview master (preparation) | Uses research brief and CV to build role-specific prep |
| Interview master (mock interview) | Practises with realistic simulation |
| Interview master (post-interview coaching) | Diagnoses rejection and feeds back into CV/prep refinement |
| Interview master (reference and referee prep) | Helps you choose, ask, and brief referees at offer stage |
| Career navigator (salary negotiation) | Coaches through offer negotiation with region-specific guidance |
| Career navigator (offer evaluation) | Compares multiple offers with weighted decision framework |
| Career navigator (application tracker) | Indexes every live application, its stage, and its next action |
| Career navigator (learnings loop) | Turns interviews, rejections, and wins into synthesised patterns that sharpen CV and interview work |

The persistent folder is what holds this chain together. Without it, each skill starts from scratch.

---

## Common Mistakes to Avoid

**Starting with CV optimisation before research.** The CV optimisation works best when you have already run company research. The research brief informs the keyword strategy.

**Skipping the digital footprint.** Your online presence is part of your application whether you manage it or not. Five minutes with the social media review (or twenty minutes with the full footprint analysis) can prevent problems you did not know existed.

**Not using a folder.** This is worth repeating. Select a folder in Cowork before you start. Use the same folder every time. The skills save files that later skills reference. Without a folder, you lose the compound benefit.

**Running skills once and moving on.** Career Helper works iteratively. After a rejection, run the post-interview coaching, then update your CV, then refine your interview prep. The folder keeps everything in one place so this iteration is seamless.

**Ignoring the wellbeing elements.** The 3-month job search plan includes wellbeing practices for a reason. Job searching is stressful at every level. Using them is not a sign of weakness; it is part of a sustainable approach.

---

## What Career Helper Gives You

To summarise, here is what you get across the full skill set:

- **ATS-optimised CVs** tailored to specific job descriptions with 70%+ keyword coverage
- **Cover letters and supporting statements** drafted from verified content, with the same anti-hallucination guardrails as the CV work
- **Company intelligence briefs** covering leadership, culture, financials, red flags, and hiring context
- **Digital footprint dashboards** scored across eight dimensions with text-label ratings
- **LinkedIn profile audits** with headline optimisation, content strategy, and 4-week posting calendars
- **Interview preparation packs** with 15 to 20 role-specific questions, STAR frameworks, and mock simulation
- **Networking intelligence** identifying 8 to 12 strategic contacts at target companies with outreach templates
- **3-month job search plans** with weekly task breakdowns, progress tracking, and integrated wellbeing practices
- **Salary negotiation coaching** covering total compensation analysis across UK, US, EU, and APAC markets
- **Offer evaluation frameworks** with weighted decision matrices for comparing multiple opportunities
- **Post-rejection coaching** that diagnoses where things went wrong and feeds improvements back into your materials
- **Reference and referee prep** to choose, ask, and brief your referees, with UK conventions and regulated-role notes
- **An application tracker** that keeps every live application, its stage, and its next action in one plain-text board you own
- **An application learnings loop** that captures each interview, rejection, and win as a structured note and synthesises them into the patterns that are actually shaping your search
- **Scheduled routines for Claude Cowork** that put a Monday standup, market monitor, and follow-up check on repeat between sessions
- **AI readiness assessments** with tiered upskilling roadmaps
- **AI impact assessments** that research whether your role faces material disruption, with 6-month mitigation plans
- **Fractional and portfolio career planning** including rate setting, IR35 guidance, and client acquisition strategy
- **Non-linear career exploration** covering entrepreneurship, startups, public sector, charity, intrapreneurship, and multi-role skilling with honest assessments and decision frameworks
- **Ageism support** with UK employment law, practical strategies, and emotional resilience resources
- **Social media reviews** from a quick recruiter-eye scan to a full 8-agent deep research audit
- **Guided coaching with Tim** who understands your situation, runs the right skills in the right order, reads emotional signals, and checks in between each step
- **Accessibility** across every skill: dyslexia-friendly enhanced mode and colour-blind safe output, stored in your preferences

All of it saves to your folder, builds on previous outputs, and adapts to your career stage, whether you are an apprentice, a graduate, mid-career, a senior leader, or approaching retirement.

---

## Share This Guide

If you found this useful, share it with someone who could benefit. Whether they are an apprentice looking for their next step, a graduate starting out, a professional between roles, someone returning after a break, someone considering a completely different direction, or someone wanting to slow down on their own terms, Career Helper works for all of them.

If you have suggestions, feature requests, or you have hit a problem, you can [raise an issue on GitHub](https://github.com/Zal4DW/career-helper/issues). If you would prefer a conversation, drop Paul a message on [LinkedIn](https://www.linkedin.com/in/paul-bratcher/). We genuinely read everything and it helps us make the plugin better.

---

## About Prosper AI Consulting

Career Helper is built by Prosper AI Consulting. We help organisations connect AI to real business outcomes. If your organisation is exploring how to use AI practically, we would welcome a conversation. Visit [prosperconsulting.ai](https://prosperconsulting.ai) to find out more.

---

*Career Helper Plugin | Prosper AI Consulting, UK*
