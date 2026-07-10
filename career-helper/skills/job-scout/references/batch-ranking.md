# Batch Ranking

**Purpose:** Score a set of postings against the user's verified profile so they apply to the right roles first. Ranking is triage: its value is in the order and in what it discards, not in flattering scores.

---

## Inputs

1. **The postings**: from a discovery run, or pasted or linked by the user. Fetch full posting text where reachable; a title alone cannot be scored, so mark unscoreable entries as such rather than guessing.
2. **The profile**: the user's CV, LinkedIn summary, or an earlier career-helper profile. Score against what the profile evidences, not against what the user might plausibly be able to do. If `applications/learnings/patterns.md` exists, read it; recurring objections from real interviews are evidence about winnability.
3. **The deal-breakers**: captured during discovery, or asked for now if ranking pasted postings directly.

---

## Step 1: Deal-Breaker Vetting

Before any scoring, test every posting against the hard constraints. A role that fails one is tiered Discard with the reason named, regardless of how well it scores elsewhere. List discards briefly so the user can rescue a role if the constraint was misapplied.

---

## Step 2: Score Five Dimensions

Score each surviving role 1 to 5 on each dimension, with one line of rationale per dimension. Rationale must trace to the posting text and the profile; no vibes.

| Dimension | What it measures | 5 looks like | 1 looks like |
|:----------|:-----------------|:-------------|:-------------|
| Skills and experience fit | Posting requirements the profile actually evidences | Nearly all must-haves evidenced with recent examples | Multiple must-haves missing entirely |
| Level and trajectory fit | Seniority match and direction of travel | Right level, and the role moves the user towards their stated direction | Big level mismatch in either direction, or a sideways move away from the goal |
| Practical fit | Location, pattern, salary where stated, contract type | Meets all stated preferences comfortably | Meets them only with sacrifices the user has said they will not make |
| Organisation signals | Stability and culture evidence available in the public record | Healthy signals, no visible red flags | Layoffs, churn, or culture red flags in recent coverage |
| Winnability | Realistic chance of reaching interview | Strong match plus a network path or scarce skills | Heavy competition, missing credentials, no route in |

Weighting: default to equal weights. If the user's priorities are known (from a three-month plan or offer criteria), weight accordingly and say what weighting was used.

**Scoring integrity rules:**

- Score against the profile as evidenced. If the user claims a skill the CV does not show, note it as unevidenced and suggest `/skills-radar` to surface or close the gap.
- `[NOT STATED]` salary or location scores Practical fit at 3 by default, with the uncertainty named.
- Organisation signals may need a quick WebSearch for larger employers. When no public record exists (common for tiny organisations), score the dimension a neutral 3 and add an uncertainty note ("no public signals found") to the rationale; never invent signals, and never leave the dimension unscored, because a missing score would distort the average and shift tiers based only on source availability.

---

## Step 3: Tier and Flag

Convert scores to tiers, then adjust for judgement and deadlines. Tiers are text labels, never colours.

| Tier | Default range (average score) | Meaning |
|:-----|:------------------------------|:--------|
| Apply first | 4.0 and above | Strong match, act this week |
| Apply | 3.0 to 3.9 | Worth an application once Apply first roles are moving |
| Park | 2.0 to 2.9 | Revisit if the pipeline thins or new evidence emerges |
| Discard | Below 2.0, or any deal-breaker failure | Named reason; do not carry it forward |

Adjustments:

- **Deadline flag:** any role closing within seven days gets a `CLOSING SOON: {date}` flag. A Park-tier role closing soon stays Park; deadlines change urgency, not quality.
- **Stretch flag:** a role one level up with most must-haves evidenced gets `STRETCH`, kept in Apply with the risk named.
- **Judgement beats arithmetic:** if the numbers say Apply but a single dominating weakness makes it unwinnable, move it down and say why. Never move a role up without evidence.

---

## Step 4: Present the Shortlist

Load `@references/shortlist-template.md` and save to `applications/shortlist.md`. Present:

1. The ranked table, Apply first at the top.
2. One short paragraph per Apply first role: why it leads, its biggest risk, and the suggested next step.
3. The discard list with one-line reasons.
4. The coverage statement carried over from discovery, so the shortlist's limits stay visible.

Then ask which roles the user wants to pursue, and hand those to the Shortlist to Tracker capability. Do not push; the user decides the queue.

---

## Re-Ranking

Shortlists go stale. Re-rank rather than append when:

- A new discovery run adds roles: merge, re-score only the new entries, and re-sort.
- The user's profile materially changes (new CV, new evidence via `/skills-radar`): offer to re-score Skills fit and Winnability across the open list.
- A deadline passes: move the role to Discard with reason `deadline passed`, never delete silently.

Keep `applications/shortlist.md` as the single current shortlist; do not accumulate dated copies.
