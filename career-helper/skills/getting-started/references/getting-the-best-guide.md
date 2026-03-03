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

Career Helper is not a single tool. It is a set of ten skills, each designed for a different part of the career journey. You do not need to use them all, and you do not need to use them in order. Pick the ones that fit your situation. Here is the quick summary; the rest of this guide shows you exactly how to put them together.

| Skill | What It Does |
|:----|:----|
| `/social-media-review` | Quick social media check through a recruiter's eyes |
| `/employer-footprint` | Full digital footprint audit with a scored dashboard |
| `/application-optimiser` | Company research, ATS CV optimisation, and application strategy |
| `/linkedin-coach` | Profile audit, headline crafting, content strategy, and video intro scripts |
| `/interview-master` | Interview prep, mock interviews, and post-rejection coaching |
| `/career-navigator` | Networking intelligence, 3-month plans, salary negotiation, and offer evaluation |
| `/career-transitions` | Fractional/portfolio careers and AI readiness assessment |
| `/ai-impact-assessment` | Honest assessment of AI disruption risk for your role, with a 6-month mitigation plan |
| `/ned-ai-helper` | AI governance for Non-Executive Directors, Governors, and Trustees |
| `/getting-started` | Full overview, preparation checklists, workflow planning, and this guide |

Now, before you run any of them, there is one thing to do.

---

## Set Up a Folder (This Really Matters)

Career Helper saves files as it works. Research briefs, optimised CVs, interview prep packs, content calendars, and footprint dashboards all get written to your working folder. If you start a new Cowork session each time without selecting the same folder, those outputs are lost between sessions. Worse, later skills cannot build on what earlier skills produced.

**How to do it:**

1. Create a folder on your computer called something like `Career Helper` or `Job Search 2026`.
2. When you open Cowork, use the "Work in a folder" option and select that folder.
3. Every session after that, select the same folder.

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
- If you are wondering whether the roles you are applying for have a future, run `/ai-impact-assessment`. It researches whether AI will materially change the role in the next 12 months and gives you a 6-month plan to stay ahead. Better to know now than find out after you start.
- If you are unsure where to start at all, just type "how do I get started" and Career Helper will route you.
- Do not skip the social media review. Recruiters do check, and it takes five minutes.

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

Start with `/employer-footprint`. This is the full digital audit, not the lightweight social scan. It runs eight parallel research agents across Google, LinkedIn, Twitter, GitHub, news media, and more, producing a scored dashboard with traffic-light indicators across eight dimensions. At your level, your digital footprint is part of your candidacy whether you like it or not. This tells you exactly what an employer will find and what to do about it.

If you have a target company in mind, provide it. The skill maps your online presence against the company's stated values and culture.

**Step 2: Company Research and CV Optimisation**

Run `/application-optimiser` with both your CV and a target job description. At senior level, the ATS optimisation becomes even more important because your CV is likely longer and more complex, which means more opportunities for keyword mismatches. The skill extracts keywords and concepts from the job description and rewrites your CV to hit 70%+ coverage while keeping your achievements quantified and your narrative coherent.

If you have been made redundant or have a career gap, the skill has a career returner persona that loads specific guidance on framing gaps positively and handling the narrative.

Run the company research capability too. The intelligence brief covers leadership, financial health, hiring context, and red flags. When you are applying to roles at director level and above, knowing who the hiring manager reports to and what the board's strategic priorities are gives you a tangible edge.

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

- Run `/ai-impact-assessment` before committing to a target role. If you are pivoting after redundancy or considering a new direction, this tells you whether AI is likely to disrupt that role in the next 12 months. It also provides a 6-month plan to position yourself ahead of the change.
- Run `/career-transitions` if you are considering going fractional or portfolio. It covers readiness assessment, rate setting, IR35 considerations, and client acquisition strategy.
- Use `/career-navigator` to evaluate and negotiate offers. The salary negotiation coach is region-aware (UK, US, EU, APAC) and covers total compensation including pension, equity, notice periods, and garden leave.
- Your research briefs, CV versions, and interview prep all save to your folder. When you are managing five active applications simultaneously, this is the difference between preparation and chaos.

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

**Step 4: AI Impact Assessment**

Run `/ai-impact-assessment` to get an honest picture of how AI is likely to affect your current role over the next 12 months. Even if you are not planning to move, knowing which of your day-to-day tasks are at risk and which are resilient helps you prioritise what to invest your development time in. The skill produces a specific, evidence-based assessment and a 6-month plan.

**Step 5: AI Readiness Assessment**

Run `/career-transitions` and ask for an AI readiness assessment. This evaluates your current AI proficiency against your role and target direction, produces a tiered upskilling roadmap, and gives you CV and LinkedIn integration strategies. Whether or not you are changing roles, demonstrating AI fluency is becoming a differentiator across almost every profession.

**Step 6: Strategic Networking**

Run `/career-navigator` for networking intelligence, even without a specific target company. Ask it to help you identify the right people to connect with in your industry. Building relationships before you need them is the definition of strategic networking.

**When an Opportunity Does Come Along**

You are not actively searching, but opportunities will appear. When one does, you have everything you need. Run `/application-optimiser` to research the company and optimise your CV for that specific role. Run `/interview-master` to prepare. And if it does not work out, run the post-interview coaching to understand why, so you are even better prepared for the next one.

Because you have been maintaining your folder all along, the skills already know your background, your content strategy, and your professional positioning. You are not starting from scratch; you are just adding a targeted application to an already strong foundation.

### A Few More Things Worth Knowing

- The content strategy output includes a content calendar. Treat it seriously. Consistency over three months builds more visibility than one viral post.
- Run `/linkedin-coach` in content review mode after you have been posting for a few weeks. It analyses your existing posts for audience alignment and suggests improvements.
- Ask for a video introduction script. A 30-second profile video significantly increases profile engagement.
- You do not need to be in a crisis to use Career Helper. The skills for content strategy, AI readiness, and networking intelligence are just as useful for career maintenance as they are for active job searching.

---

## How the Skills Connect

Career Helper skills are designed to feed into each other. Here is the chain:

| What You Run First | What It Feeds Into |
|:----|:----|
| Social media review or employer footprint | Identifies what to fix before applications |
| Company research (application optimiser) | Informs CV tailoring, interview prep, and networking |
| CV optimisation (application optimiser) | Produces a CV that LinkedIn coach and interview master reference |
| LinkedIn coach (profile audit) | Creates consistency between CV and LinkedIn |
| LinkedIn coach (content strategy) | Builds ongoing visibility and thought leadership |
| Career navigator (networking intelligence) | Identifies who to connect with at target companies |
| Career navigator (3-month plan) | Structures the entire search with wellbeing built in |
| Interview master (preparation) | Uses research brief and CV to build role-specific prep |
| Interview master (mock interview) | Practises with realistic simulation |
| Interview master (post-interview coaching) | Diagnoses rejection and feeds back into CV/prep refinement |
| Career navigator (salary negotiation) | Coaches through offer negotiation with region-specific guidance |
| Career navigator (offer evaluation) | Compares multiple offers with weighted decision framework |
| AI impact assessment | Identifies which tasks in your role face AI disruption, informing upskilling and pivot decisions |

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
- **Company intelligence briefs** covering leadership, culture, financials, red flags, and hiring context
- **Digital footprint dashboards** scored across eight dimensions with traffic-light indicators
- **LinkedIn profile audits** with headline optimisation, content strategy, and 4-week posting calendars
- **Interview preparation packs** with 15 to 20 role-specific questions, STAR frameworks, and mock simulation
- **Networking intelligence** identifying 8 to 12 strategic contacts at target companies with outreach templates
- **3-month job search plans** with weekly task breakdowns, progress tracking, and integrated wellbeing practices
- **Salary negotiation coaching** covering total compensation analysis across UK, US, EU, and APAC markets
- **Offer evaluation frameworks** with weighted decision matrices for comparing multiple opportunities
- **Post-rejection coaching** that diagnoses where things went wrong and feeds improvements back into your materials
- **AI readiness assessments** with tiered upskilling roadmaps
- **Fractional and portfolio career planning** including rate setting, IR35 guidance, and client acquisition strategy
- **AI impact assessments** with task-level disruption analysis, evidence-cited verdicts, and 6-month mitigation plans
- **Social media reviews** from a quick recruiter-eye scan to a full 8-agent deep research audit

All of it saves to your folder, builds on previous outputs, and adapts to your career stage.

---

## Share This Guide

If you found this useful, share it with someone who could benefit. Whether they are a graduate starting out, a professional between roles, or someone wanting to raise their profile, Career Helper works for all of them.

If you have suggestions, feature requests, or you have hit a problem, you can [raise an issue on GitHub](https://github.com/Zal4DW/career-helper/issues). If you would prefer a conversation, drop Paul a message on [LinkedIn](https://www.linkedin.com/in/paul-bratcher/). We genuinely read everything and it helps us make the plugin better.

---

## About Prosper AI Consulting

Career Helper is built by Prosper AI Consulting. We help organisations connect AI to real business outcomes. If your organisation is exploring how to use AI practically, we would welcome a conversation. Visit [prosperconsulting.ai](https://prosperconsulting.ai) to find out more.

---

*Career Helper Plugin | Prosper AI Consulting, UK*
