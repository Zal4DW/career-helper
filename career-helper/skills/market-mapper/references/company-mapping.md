# Company Mapping

**Purpose:** Build an evidenced map of ten to fifteen organisations similar to the user's current or recent employer, showing which are growing, hiring, or investing, who runs them, and how the user might approach each one without announcing a job search.

---

## Step 1: Confirm the Posture

Ask once, then apply for the whole session:

- **Employed and discreet.** The default if the user is unsure. Angles are limited to following, reading, and commenting on topic-relevant public posts. No connection requests to hiring managers, no messages that mention a move, no LinkedIn setting changes. Warn once that public engagement with a competitor is visible to the user's own leadership.
- **Openly searching.** Angles may include connection requests and direct messages; the map feeds `/career-navigator` (Strategic Networking) and `/job-scout` without restriction.

Record the posture in the map header. It changes every angle downstream.

---

## Step 2: Build the Seed Profile

"Similar" is meaningless until defined. Establish the seed from the user's current or most recent employer and confirm it before searching:

| Dimension | What to capture | Why it matters |
|:----------|:----------------|:---------------|
| Sector and sub-sector | e.g. "industrial automation, not general engineering" | Keeps comparables genuinely comparable |
| Size band | Headcount and revenue band (e.g. 200 to 1,000 staff, 20m to 100m turnover) | A 50-person scale-up and a FTSE 250 hire differently |
| Geography | Where the user can work: cities, regions, remote tolerance | Filters out organisations with no relevant site |
| Products, services, and target markets | What they sell and to whom | Surfaces adjacent-sector peers with the same customer base |
| Ownership and stage | PLC, private equity backed, founder led, public sector, charity | Signals how they hire and how fast they change |
| Function and level the user wants | e.g. "head of operations, or a step up to director" | Drives which hiring signals count |

Read `three-month-plan.md`, `skills-inventory.md`, and `applications/tracker.md` first if they exist; the direction and level may already be defined. Apply the user's exclusions: their own employer and its group companies always; anywhere covered by a non-compete or restrictive covenant; anywhere the user has said no to.

Play the seed back in five or six lines and get a yes before searching.

**Dyslexia-friendly mode:** play the seed back as a numbered list, one dimension per line. Ask for the yes on its own, with no other question in the same message. Signpost each pass as you go ("Pass 1 of 4: the seed profile. Next: comparables.").

---

## Step 3: Assemble the Comparables

Run parallel WebSearch and WebFetch across these routes. Each finds a different slice; cover at least three.

| Route | How | Typical yield |
|:------|:----|:--------------|
| Direct competitors | `"{seed company}" competitors`, sector league tables, trade-body member lists, "companies like {seed}" | The obvious names; usually four to six |
| Adjacent-sector peers | Same customers, different product; same product, different vertical | The names the user has not thought of |
| Suppliers and customers | The seed's public case studies, partner pages, and contract announcements | Organisations that already value the user's domain knowledge |
| Function-led | Recent postings for the user's function and level in the geography, then the employers behind them | Organisations hiring the user's job right now |
| Regional business press | BusinessLive, Insider Media, TheBusinessDesk, Prolific North, regional Chambers of Commerce, growth-index lists (e.g. Sunday Times 100, Northern Tech Awards, FT 1000) | Growing organisations the national press ignores |
| UK company data | Companies House (incorporation, officers, filings, charges), Contracts Finder and Find a Tender (public contracts), The Gazette (notices), Innovate UK grant awards | Verifiable signals with dates |
| Funding and deals | Crunchbase, Beauhurst (paid; use what is public), press releases, BVCA and regional fund announcements | Investment signals |

Aim for ten to fifteen organisations. Twelve well-evidenced beats fifteen padded. If the reachable sources produce fewer than eight, deliver what exists and say why; do not fill the gaps with guesses.

For each candidate, capture the canonical website, the careers page URL, the LinkedIn company page URL if it resolves publicly, and the size band with its source.

---

## Step 4: Gather Dated Signals

Default window: the last three months. State the window on the map. Record every signal as one line with source URL and date seen, grouped as follows.

### Signal taxonomy

| Group | Positive signals | Negative or cautionary signals |
|:------|:-----------------|:-------------------------------|
| Hiring | Posting volume on the careers page; new roles in the user's function; a talent or recruitment lead hired; a new office or team announced with headcount | Hiring freeze reported; roles withdrawn; the same senior role re-advertised repeatedly |
| Growth | Contract wins (Contracts Finder, press); new sites, plants, or offices; revenue growth in filed accounts; new product lines; awards for growth | Profit warnings; lost contracts; site closures |
| Investment | Funding rounds; grants (Innovate UK, regional funds); acquisitions made; capital expenditure announced; new debt facility (Companies House charges) | Emergency funding; asset sales; distressed refinancing |
| Change | New CEO, COO, CFO, or function head; board appointments; restructure creating a new division | Redundancy consultations; leadership departures; administration or strike-off notices in The Gazette |

Rules:

1. **Date every signal.** A signal without a date is not a signal. If the source shows no date, record the date seen and mark the event date `[NOT STATED]`.
2. **One source per signal minimum.** A second, independent source upgrades confidence; note it.
3. **Record negatives.** A company shedding staff in the user's function is important information, and pretending otherwise is the failure mode this skill exists to avoid.
4. **Careers page counts are evidence; interpretation is inference.** "Eleven live roles, four in operations (seen 2026-09-12)" is a fact. "Building out operations" is inference; label it.
5. **No public signals found** is a legitimate finding. Write it plainly; do not fill the row with generic sector commentary.

---

## Step 5: Identify Decision Makers

For each organisation, aim for one or two people who would own a hire in the user's function at the user's level. Typical targets by level:

| User's target level | Likely decision maker | Also worth noting |
|:--------------------|:----------------------|:------------------|
| Executive or director | CEO, MD, or the relevant C-suite owner; chair for board roles | Head of talent or people director |
| Head of function | The C-suite or director who owns the function | Talent acquisition lead |
| Manager or senior individual contributor | The head of function | Internal recruiter for the area |

Sources that confirm a person, in order of preference:

1. The organisation's own leadership or team page
2. Companies House officer records (directors and secretaries, with appointment dates)
3. Press releases and news coverage naming the person in role
4. Conference speaker listings, podcast appearances, trade-body profiles
5. A public LinkedIn profile page that resolves without login

Rules:

- **Never guess a name, title, or URL.** If no source confirms a person, write `[NOT FOUND]` and give the search the user can run themselves (for example, "LinkedIn: people at {organisation} with title containing 'operations director'").
- **A LinkedIn URL is recorded only if it was actually retrieved.** Do not construct a URL from a name.
- **Check recency.** A leadership page can be stale; cross-check against Companies House or a dated press mention where the person matters.
- **Note the appointment date** where known; a director appointed six weeks ago is a change signal in their own right.

Offer the Claude for Chrome extension once per session if LinkedIn coverage matters: "LinkedIn people search sits behind a login I cannot reach from here. If you have the Claude for Chrome extension, I can look up these organisations in your own browser and read the public profiles. Would you like that, or shall I continue with the sources I can reach?" If declined, reflect the narrower coverage in the coverage statement.

---

## Step 6: Suggest an Angle

An angle is a specific, low-effort action that traces to one dated signal and fits the posture. It is never a template message and never mentions a job.

| Posture | Acceptable angles | Not acceptable |
|:--------|:------------------|:---------------|
| Employed and discreet | Follow the organisation and the named person; comment substantively on a public post about the signal topic; read their filed accounts or strategy page and note two questions for later | Connection requests to hiring managers; any message; "Open to Work"; liking every post in one sitting; attending an event to meet them, which is visible to your own leadership |
| Openly searching | All of the above plus attending a public event they are speaking at; a connection request with a note that references the signal; a short message congratulating a public milestone and asking one question about the work | Attaching a CV; asking about vacancies in the first message; contacting several people at the same organisation in one week |

Write each angle as one line: the action, the person or channel, and the signal it draws on. Example shape (placeholders, not an actual recommendation): "Comment on {{PERSON}}'s post about the {{CONTRACT}} win (seen {{DATE}}) with a specific observation about delivery risk in the first year."

---

## Step 7: Assign Watch Priority

Text labels only, one per organisation, with a one-line reason:

| Priority | Meaning |
|:---------|:--------|
| Act now | A dated hiring signal in the user's function at the user's level within the window, or a leadership change that creates one; the angle should be taken this week |
| Warm | Growth or investment signals within the window but no direct hiring signal yet; engage and keep watching |
| Watch | Similar organisation, no signals in the window; stays on the map for the next update |
| Quiet | No signals for two consecutive updates, or a negative signal that reduces the prospect; offered for removal |

Priority reflects evidence, not the user's preference. A favourite organisation with no signals is Watch, and the map should say so.

---

## Step 8: Write the Coverage Statement

Every map ends with a short coverage statement before the next actions:

- Which routes and sources were searched, and which were unreachable or behind logins
- The signal window and the date of the run
- What the map cannot claim: "This is what public sources showed in the window, not a full picture of any organisation's plans."
- The standing mitigations: the Claude for Chrome extension for LinkedIn, the weekly update to catch what this run missed, and the user's own network as a source the map cannot see

---

## Dyslexia-Friendly Output

When `career-helper-preferences.md` sets `dyslexia_friendly: true`, the map keeps the same content in a shape that does not need visual scanning:

1. Replace the eight-column watchlist table with a numbered list, one organisation per entry, each field on its own short labelled line (Organisation, What they do, Latest signal and date, Decision maker, Angle, Priority, Last checked).
2. Keep the per-organisation signal table to three columns (Date, Signal, Source) or use a numbered list.
3. Write each angle as one short sentence with no idiom ("Follow the company page and read their strategy page", not "keep an ear to the ground").
4. Repeat the organisation name in every line that refers to it.
5. Put the coverage statement as a numbered list and the next actions as one action per number.
6. In conversation, refer to the map as "your market map", never by filename, and present one decision at a time (for example, which organisation to act on first, then whether to schedule the update).

With `colour_blind: true` nothing changes: priorities are text labels already.

---

## What Not to Do

- Do not invent decision makers, titles, or LinkedIn URLs. This is the most damaging failure the skill can produce, because the user may act on it.
- Do not present sector commentary as a company signal. If nothing was found for an organisation, say so.
- Do not infer decline from silence. A quiet careers page is not a hiring freeze.
- Do not suggest outreach that would expose an employed user. When in doubt, the angle is "follow and read".
- Do not keep the user's employer name anywhere except the map header, and tell the user that is where it is.
- Do not scrape aggressively or attempt to work around a login or a block. Note the gap, offer the browser extension, and move on.
