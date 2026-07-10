# Role Discovery

**Purpose:** Find live, real openings that match the user's profile and constraints, from as many reachable sources as practical, while being honest about what automated search can and cannot see.

---

## Step 1: Capture Constraints Before Searching

Ask for these once, then reuse them for the whole session:

1. **Target role or direction** (titles, level, and acceptable variants).
2. **Location and pattern** (cities, remote, hybrid; days-in-office tolerance).
3. **Hard deal-breakers**: minimum salary if the user has one, sectors they will not work in, visa or right-to-work needs, travel limits, contract versus permanent.
4. **Soft preferences**: sectors they favour, organisation size, mission alignment.

Deal-breakers filter results before ranking. Soft preferences influence scores. Keep the two separate; do not silently promote a preference to a filter.

If a three-month plan (`three-month-plan.md`) or tracker exists, read them first: the target direction and volume goals may already be defined.

---

## Step 2: Search Across Source Types in Parallel

Run parallel WebSearch and WebFetch calls across different source types. Each type fails differently, which is why breadth matters.

| Source type | Examples | Reliability notes |
|:------------|:---------|:------------------|
| General boards | Indeed, Reed, Totaljobs, CV-Library | Often block fetches; search-engine results may be stale |
| Professional networks | LinkedIn Jobs | Mostly behind login; prefer Claude in Chrome here |
| Curated aggregators | Otta / Welcome to the Jungle, Escape the City, workinstartups | Better for tech and startup roles; smaller coverage |
| Sector boards | CharityJob, jobs.ac.uk, Civil Service Jobs, TechJobs | Usually unauthenticated and current; strong for sector targets |
| Executive and interim | Nurole, exec search firm listings | NED and senior roles; some behind registration |
| Employer careers pages | Target companies' own sites | Most current source; use for any named target company |
| Search engines directly | `site:` queries, e.g. `site:apply.workable.com "head of data" London` | Finds ATS-hosted postings (Workable, Greenhouse, Lever, Teamtailor) that boards miss |

Useful query patterns:

- `"{role title}" jobs {location} posted this week`
- `site:boards.greenhouse.io OR site:jobs.lever.co "{role title}" {location}`
- `"{target company}" careers "{role keyword}"`
- Sector board searches with the board named, so results stay on-board.

Cover at least three source types per run. Note which sources were unreachable; that goes in the coverage statement.

---

## Step 3: Offer Claude in Chrome for Logged-In Boards

When LinkedIn or Indeed coverage matters, or a board blocks fetches, offer once:

"The strongest listings are often behind logins that I cannot reach from here. If you install the Claude for Chrome extension, I can search LinkedIn or Indeed in your own browser, logged in as you, and read the full postings. Would you like to do that, or shall I continue with the sources I can reach?"

If the user takes the browser route, drive their browser to run the saved searches, open each promising posting, and capture role title, organisation, location, salary if stated, closing date, and the requirements list. Capture text immediately; do not rely on the URL staying live.

If the user declines, continue without it and reflect the narrower coverage honestly in the output.

---

## Step 4: Deduplicate and Verify

1. **Deduplicate** on organisation plus role title plus location. The same role commonly appears on two or three boards; keep the version closest to the source (employer page or ATS link beats an aggregator copy).
2. **Verify liveness** where possible: fetch the application link; a 404 or "no longer accepting applications" page removes the role.
3. **Record for every survivor**: source URL, date seen, posting date if shown, and closing date or `[NOT STATED]`.
4. **Discard on deal-breakers** immediately, but tell the user what was discarded and why, in one line each; a wrongly-inferred deal-breaker should be correctable.

---

## Step 5: State Coverage Honestly

End every discovery run with a short coverage statement before handing over to ranking:

- Which source types were searched, and which were unreachable or blocked.
- How fresh the results are likely to be.
- What the run cannot claim: "This is what was reachable today, not the whole market."
- The standing mitigations: saved alerts on two or three boards, direct careers page checks for target companies, and Claude in Chrome for logged-in boards.

A short, honest coverage statement protects the user from the worst failure mode of automated search: quietly mistaking partial results for the market.

---

## What Not to Do

- Do not fabricate or embellish listings. If a search result shows only a title and company, record only that and mark the rest `[NOT STATED]` until the posting is fetched.
- Do not present aggregator summaries as the posting text; fetch the original where reachable.
- Do not keep searching past useful volume. Ten well-verified roles beat forty unverified links; stop when the shortlist has enough credible candidates to rank.
- Do not scrape aggressively. If a site blocks access, respect it, note it, and move to the browser-extension route or another source; do not attempt to circumvent blocks.
