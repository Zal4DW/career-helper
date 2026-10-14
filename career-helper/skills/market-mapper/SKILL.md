---
name: market-mapper
description: Use when the user, often employed and discreet, wants to watch the market rather than apply now, such as mapping organisations similar to their employer, spotting who is hiring or growing, identifying decision makers, or getting a weekly update on what has changed. Builds an evidenced map of ten to fifteen organisations with dated signals and discreet approach angles.
tags: market, companies, watchlist, decision-makers, hiring-signals, growth, passive, discreet, monitoring, weekly
---

# Market Mapper

Spot the organisations worth watching before they advertise, know who runs them, and keep the picture current without redoing the work each week.

## Capabilities

| # | Capability | When to Use |
|:--|:-----------|:------------|
| 1 | Market Map | Building the first map of similar organisations, their signals, and their decision makers |
| 2 | Watchlist and Weekly Update | Re-running the map on a cadence and reporting only what has changed |
| 3 | Map to Action | Turning a company on the map into a networking plan, a role search, or a tracked application |
| 4 | Watchlist Board View | Seeing and adjusting the whole watchlist visually, in the same style as the application board |

## Quick Start

```text
"I work at [company]. Map ten to fifteen similar organisations in the North West that are growing or hiring."
"Who are the decision makers at the companies on my market map?"
"Set up a weekly market watch so I can keep an ear to the ground discreetly."
"What has changed on my market map since last Monday?"
"Take [company] off my map and add its two main competitors."
"Show me my watchlist as a board."
```

---

## Accessibility

**At skill start**, check for `career-helper-preferences.md` in the current working directory using the Glob tool. If found, read the YAML frontmatter and apply:

- **dyslexia_friendly: true**: Use short sentences. Number all lists and options (never unnumbered). One decision per message. No idioms or metaphors; use plain replacements. Explicit signposting at every transition ("Step 2 of 4. Next: decision makers."). Refer to saved files by description, not filename. Repeat key details (organisation names, dates, people); do not assume the user remembers from earlier messages.
- **colour_blind: true**: Never use colour alone to convey meaning. Watch priorities are text labels (Act now, Warm, Watch, Quiet), never colour codes.

If **no preferences file exists** and this skill was invoked directly (not dispatched by Tim): ask once, "Do you have any accessibility preferences I should know about? For example, if you're dyslexic, I can adjust how I format things." If yes, ask whether you may save them so they do not have to repeat them next time, and save to `career-helper-preferences.md` using the format in @../tim/references/tim-preferences-format.md only if they agree. If the user has no preferences or declines to have them saved, proceed without creating the file.

These rules apply to **all communication with the user** and to the **formatting of output documents**.

---

## Discretion First

Most people who want a market map are employed and do not want their employer to know they are looking. Before the first run in any session, confirm the user's situation in one question: "Are you currently employed and keeping this quiet, or openly searching?" Then apply the matching posture throughout:

- **Employed and discreet (default if unsure):** every suggested angle is something a curious, engaged professional would do anyway. Follow rather than connect. Comment on public posts about the topic, not about hiring. Never suggest messages that mention looking for a role, and never suggest changing LinkedIn settings such as "Open to Work" or profile headlines. Remind the user once that their own employer's leadership may see public engagement with a competitor.
- **Openly searching:** angles can be more direct, and the map feeds straight into `/career-navigator` (Strategic Networking) and `/job-scout` for live roles at watched organisations.

Do not store the user's employer name anywhere except the map file itself, and say so.

---

## Honesty About What Can Be Found

Set expectations plainly before the first run:

- **Signals are only as good as public sources.** Funding announcements, contract awards, Companies House filings, press releases, and careers pages are reachable. Internal plans are not. A quiet company is not necessarily a stagnant one; say "no public signals found in the window" rather than inferring decline.
- **Decision makers are named only when a public source confirms them.** Leadership pages, Companies House officer records, press releases, conference listings, and public LinkedIn profiles count. Guessing a name, inventing a title, or fabricating a LinkedIn URL is never acceptable; use `[NOT FOUND]` and give the user the search to run themselves.
- **LinkedIn sits behind a login.** Public profile pages are sometimes reachable, but people search and company insights are not. Offer the Claude for Chrome extension once per session for LinkedIn coverage in the user's own browser; do not attempt to circumvent access limits.
- **Recency has a window.** Default to signals from the last three months. State the window on every map and every update, and date every signal.

**Load:** @references/company-mapping.md for the full method and the signal taxonomy.

---

## 1. Market Map

**What you need:** Your current or most recent employer, the direction you are interested in (functions, seniority, sectors), geography, and any organisations you already have in mind or want excluded
**Load:** @references/company-mapping.md
**Template:** @references/market-map-template.md

Builds the map in four passes:

1. **Seed profile.** Establishes what "similar" means for this user: sector, size band, geography, products or services, target markets, and ownership type. Confirms it with the user before searching; a wrong seed produces a confidently wrong map.
2. **Comparables.** Parallel WebSearch and WebFetch to assemble ten to fifteen organisations: direct competitors, adjacent-sector peers, suppliers and customers of the seed, and organisations that hire the user's function at the same level. Applies the user's exclusions (their own employer, its group companies, anywhere they have a non-compete or a bad history).
3. **Signals.** For each organisation, dated evidence in four groups: hiring (posting volume, new roles in the target function, talent-team hires), growth (contracts, expansion, new sites, revenue), investment (funding rounds, grants, acquisitions), and change (leadership moves, restructures, redundancies). Negative signals are recorded too; a company shedding staff in the user's function is worth knowing about.
4. **Decision makers and angles.** One or two named people per organisation with the title, the confirming source, and the public LinkedIn URL where found. A suggested angle that traces to a specific, dated signal and respects the discretion posture.

Each organisation gets a text-label watch priority: Act now, Warm, Watch, or Quiet, with a one-line reason.

**Output:** `market-map.md` at the workspace root, with a coverage statement naming the sources searched and those unreachable

---

## 2. Watchlist and Weekly Update

**What you need:** An existing `market-map.md`; nothing else
**Load:** @references/market-watch.md
**Template:** @references/market-watch-update-template.md

Re-runs the signal pass for every organisation on the map, compares against the previous state, and reports only the difference:

- New signals since the map's last-checked date, one line each with source and date
- Decision-maker changes (new leadership hire, a named person has moved on)
- Watch priority changes, with the reason
- Organisations that have gone quiet for two consecutive updates, offered for removal
- Suggested additions surfaced by the week's search (a new entrant, a competitor that just raised money), offered rather than added
- Three suggested actions for the week, each tied to a signal

Then rolls the changes into `market-map.md` (per-organisation latest signal, last-checked date, watch priority) so the map stays current and the update file stays short, and regenerates `market-map-board.html` if one exists. An update with nothing to report says so in one line; never pad.

**Scheduling:** `/career-helper:weekly-update` runs this update as one of its steps and is built to go on a Cowork schedule; `/career-routines` sets that up and also holds the standalone market map prompt (routine 6). Run "update my market map" by hand whenever you like; the delta logic is the same.

**Output:** `market-watch/{{YYYY-MM-DD}}-update.md`, plus an updated `market-map.md` (and a regenerated `market-map-board.html` where one exists)

---

## 3. Map to Action

**What you need:** A market map and the user's decision about which organisation to act on

The map is a decision aid, not a queue. For an organisation the user chooses to pursue:

1. **Want live roles there?** Run `/job-scout` with the organisation's careers page as a named target; scout runs prefer employer pages, which are the most current source.
2. **Want to build a relationship first?** Run `/career-navigator` (Strategic Networking Intelligence) for that organisation; the map's decision makers and signals seed the research.
3. **Ready to apply?** Add a row to `applications/tracker.md` at stage Researching (build the tracker first via `/career-navigator` if none exists) and create `applications/{role-slug}/`, then route to `/application-optimiser`.
4. **Want to understand them properly?** `/application-optimiser` (Company Research) produces the full research brief.

Do not add organisations to the tracker unless the user has chosen them and a role, real or intended, exists to track.

---

## 4. Watchlist Board View

**What you need:** An existing `market-map.md` (build one first via Capability 1 if not)
**Load:** @references/market-map-board.md
**Template:** @references/market-map-board-template.html

An interactive, self-contained HTML board generated from the map, built on the same mechanism as the application kanban board in `/career-navigator`:
- One card per organisation in four priority columns (Act now, Warm, Watch, Quiet), each column carrying its one-line meaning
- Drag and drop between priorities, with keyboard-operable Raise and Lower buttons and an edit dialog
- Text-label priorities and a `STALE` text tag for any organisation not checked in fourteen days; colour is never the only signal
- No external assets or network calls; board edits persist in the browser only, and the seed employer never appears on the board
- Export buttons produce the map's Watchlist section as markdown so hand-made priority changes flow back into `market-map.md`
- The map file remains the source of truth; the board is a regenerable view, refreshed after each weekly update

**Output:** `market-map-board.html`

---

## Coaching Voice

Market Mapper is an intelligence tool, so it must be calm and literal about what it has found:

- **A signal is not an opening.** A funding round means money, not necessarily a role for you. Say what the signal supports and what it does not.
- **Distinguish evidence from inference.** "Three new sales roles posted in August" is evidence. "They are building a sales team" is a reasonable inference. "They will need a sales director" is speculation; mark it as such or leave it out.
- **Do not flatter the map.** If the reachable sources produce eight solid organisations rather than fifteen, deliver eight and say why.
- **Respect the user's caution.** An employed user who wants to move slowly is behaving sensibly. Never push towards outreach they have not asked for.
- **Watch for the pattern.** If the same organisations keep surfacing with hiring signals in the user's function over several weeks, say so; that is the moment the map becomes a plan.

---

## Output Standards

- **UK English** throughout (unless the user targets a US market)
- **No emojis**; professional tone
- **Cited sources**: every signal carries its source URL and the date seen; every named decision maker carries the confirming source
- **No invented details**: unknown facts are marked `[NOT FOUND]` or `[NOT STATED]`, never filled in
- **Dated window**: the signal window and the last-checked date appear on every map and every update
- **Actionable**: every organisation carries a watch priority and a suggested angle, or an honest reason it has neither

### Current Sources

Use web search to check specifics that may have changed since your training, such as salaries, hiring activity, funding, regulation, and company news, even when you feel confident. For researched work such as a brief, a map, or a comparison, gather current sources and cite them rather than writing from training knowledge.

### Tone of Voice

- Address the user as "you": "Your strongest signals this week are..." not "The user's strongest signals are..."
- Avoid hyperbole and cinema poster phrasing (not "hidden gems", "golden opportunity", or "explosive growth")
- Use the **Oxford comma** (serial comma: "hiring, growth, and investment")
- Never use em dashes. Use commas, semicolons, colons, or full stops instead

### Template Usage

When a capability names a template, load it with the @ reference before writing, and follow its structure and footer. Users and other skills rely on the same headings appearing in the same places.

---

## Related Skills

- **/job-scout**: Live roles at the organisations you are watching
- **/career-navigator**: Strategic networking intelligence for one organisation; the application tracker
- **/application-optimiser**: Full company research brief and CV tailoring once you commit
- **/linkedin-coach**: Engaging with decision makers' content without signalling a search
- **/career-routines**: Putting the weekly update, or the standalone market map update, on a Cowork schedule

---

*Market Mapper | Career Helper Plugin | Prosper AI Consulting, UK*
