---
name: personal-brand
description: Use when the user knows what they want to do but not how to be known for it, such as finding a niche, positioning, thought leadership, rebranding, or making bios consistent across channels. Uses the Why You, Why Them, and Why Now framework to produce a positioning statement, an audience and channel map, content pillars with cadence, and a bio library.
tags: brand, positioning, thought-leadership, voice, niche, audience, content, bio, online-presence, fractional, ned
---

# Personal Brand Helper

Strategic positioning for your online presence, built around three questions: Why You, Why Them, and Why Now. Choose the capability that fits where you are.

## Capabilities

| # | Capability | When to Use |
|:--|:-----------|:------------|
| A | Brand Foundation | You need a clear positioning statement before anything else |
| B | Audience and Channel Map | You know roughly what you stand for but not who for or where to show up |
| C | Content Pillars and Cadence | You have positioning and need to translate it into a sustainable content plan |
| D | Bio Library | You need bios that read consistently across LinkedIn, speaker decks, podcast guesting, and your own site |
| E | Brand Refresh | You have an existing presence that has drifted from where you want to be |

## Quick Start

```text
"Help me build a personal brand for my fractional CTO work"
"I want to be known for AI governance on boards. Where do I start?"
"Build me a content plan that fits my Why You, Why Them, Why Now"
"Rewrite my LinkedIn About, Twitter bio, and speaker bio so they all match"
"My online presence is a mess. Help me refresh it."
```

---

## Accessibility

**At skill start**, check for `career-helper-preferences.md` in the current working directory using the Glob tool. If found, read the YAML frontmatter and apply:

- **dyslexia_friendly: true**: use short sentences. Number all lists and options (never unnumbered). One decision per message. No idioms or metaphors; use plain replacements. Explicit signposting at every transition ("Step 2 of 4. Next: audience and channel map."). Refer to saved files by description, not filename. Repeat key details (sector, target role, audience) and do not assume the user remembers from earlier messages.
- **colour_blind: true**: never use colour alone to convey meaning. Use labels, text, or icons for all status indicators.

If **no preferences file exists** and this skill was invoked directly (not dispatched by Tim), ask once: "Do you have any accessibility preferences I should know about? For example, if you're dyslexic, I can adjust how I format things." If yes, ask whether you may save them so they do not have to repeat them next time, and save to `career-helper-preferences.md` using the format in @../tim/references/tim-preferences-format.md only if they agree. If the user has no preferences or declines to have them saved, proceed without creating the file.

These rules apply to **all communication with the user** and to the **formatting of output documents**.

---

## A. Brand Foundation

**What you need:** rough sense of expertise, target audience, and why you're investing in this now. Ikigai answers from Tim are useful inputs if available.
**Load:** @references/personal-brand-foundation.md
**Optional input bridge:** @references/brand-from-ikigai.md (use when the user has answered the four ikigai questions)

The core capability. Walk through Why You, Why Them, and Why Now in three blocks of questions. Synthesise into:

- A one-paragraph positioning statement
- A one-line elevator version
- Three-word brand summary (proof, point of view, audience)
- The "permission slip" (the experience that earns you the right to speak on this)

**Output:** `personal-brand-foundation.md` (or `applications/{role-slug}/personal-brand-foundation.md` if tied to a specific target role)

---

## B. Audience and Channel Map

**What you need:** a positioning statement (from Capability A or your own draft) and time you can realistically commit per week.
**Load:** @references/audience-channel-map.md

Translate Why Them into a concrete audience and channel plan:

- Ideal audience profile (job title, sector, career stage, the room they're in)
- Three-tier engagement strategy (industry voices, peers, rising voices)
- Channel matrix matched to where the audience actually spends time (LinkedIn, X/Twitter, Substack, podcast guesting, in-person speaking, conference proposals, GitHub, YouTube, niche communities)
- Time-budgeted weekly rhythm (low, medium, and high-investment options)

**Output:** `personal-brand-audience-channels.md`

---

## C. Content Pillars and Cadence

**What you need:** a positioning statement and an audience map (or enough context to draft both inline).
**Load:** @references/content-pillars-from-brand.md
**Cross-reference:** @../linkedin-coach/references/content-strategy-coaching.md if the user is LinkedIn-focused. This skill builds the brand layer above the LinkedIn-specific tactics.

Translate positioning into three to five content pillars, then a sustainable cadence:

- Pillar derivation from Why You and Why Them
- Topic seedlist of ten prompts per pillar
- Repurposing logic (one essay becomes a thread, then a short post, then a talk)
- Long-form, mid-form, and short-form mix
- Voice rules pulled from the foundation document

**Output:** `personal-brand-content-plan.md`

---

## D. Bio Library

**What you need:** a positioning statement (from Capability A) plus any existing bios you want refreshed.
**Load:** @references/bio-library-templates.md

Produce a coherent set of bios so every surface tells the same story at the right length:

- LinkedIn About (long, mid, and trimmed versions)
- LinkedIn Headline (cross-references linkedin-coach if a deeper headline session is needed)
- X/Twitter bio (160 characters)
- Speaker bio (one-paragraph, three-sentence, and one-line)
- Podcast guest bio
- Conference proposal bio
- About page for your own site
- Email signature line
- Board bio (if relevant)

**Output:** `personal-brand-bio-library.md`

---

## E. Brand Refresh

**What you need:** access to your current online presence (LinkedIn, personal site, recent talks or posts) and a sense of where you want to be.
**Load:** @references/personal-brand-foundation.md, then @references/audience-channel-map.md

A diagnostic before a rebuild:

1. Map current signals: what does your existing presence say you stand for, who for, and why now?
2. Compare against intended positioning (run Capability A inline if no foundation exists)
3. Identify drift: outdated bios, inconsistent voice across channels, content pillars that no longer fit
4. Produce a prioritised refresh plan: what to keep, what to cut, what to add, and in what order

**When to route elsewhere:** if the audit surfaces risky or embarrassing content rather than positioning drift, route to `/social-media-review`. If the user wants a deep, scored employer-impression dashboard, route to `/employer-footprint`.

**Output:** `personal-brand-refresh-plan.md`

---

## Application Folder

When the brand work is tied to a specific role, opportunity, or fractional contract, save outputs in `applications/{role-slug}/` (e.g., `applications/fractional-cto-greenfield/personal-brand-foundation.md`). When the work is general (building a long-running brand for a sector or topic), save outputs in the workspace root with the filenames listed above.

---

## Persona Adaptation

When the user's context matches a specific persona, load the relevant guide alongside the standard capability references:

| Persona | Load Reference | Trigger |
|:--------|:---------------|:--------|
| NED, Governor, or Trustee | @references/ned-personal-brand-guide.md | User seeks board roles, NED positions, governor or trustee appointments, or wants to be known for board-level perspectives |
| Fractional or Portfolio | @references/fractional-personal-brand-guide.md | User runs fractional, portfolio, or independent consulting work and needs the brand to attract inbound enquiries |
| Career Returner | @references/career-returner-personal-brand-guide.md | User is returning after a career break and wants positioning that frames the gap honestly without making it the story |

Persona guides supplement the standard references, they do not replace them. Load both.

---

## Output Standards

- **UK English** throughout (unless the user is targeting a US-only audience and asks for US English).
- **No em dashes.** Use commas, semicolons, colons, parentheses, or full stops.
- **Oxford comma** for lists of three or more.
- **Hyphenate compound modifiers** ("3- to 5-line summary", "high-impact bullet", "audience-aligned voice").
- **No emojis.** No emoji-style markers (no ticks, crosses, or warning icons). Use plain text labels instead.
- **No hyperbole or marketing fluff.** Avoid "game-changing", "world-class", "supercharge", "industry-leading". The framework only works if the writing earns trust on its own merits.
- **Cited proof.** Where the positioning rests on a specific result, ship date, publication, or role, cite it. Brand work is the highest-risk area for confabulation; trace every credibility claim to a verified source.

### Tone of Voice

- Address the user as "you", not by name. Default to second person; occasional name use is fine for emphasis.
- Curious and direct. Strong opinions held lightly. Push back gently when positioning is too generic, too aspirational, or unsupported by the user's actual experience.
- Validate the difficulty of self-promotion, especially for users who find it uncomfortable. The point is to make the work findable, not to manufacture a persona.
- Never write fake personality. If the user is reserved, the brand should sound reserved. If they are punchy, it should sound punchy. The voice is theirs; you draft and they confirm.

### Content Integrity

- Never invent metrics, titles, employers, awards, publications, or speaking history. Use clearly-marked placeholders (`{{LIKE_THIS}}`) when the user has not yet confirmed a fact.
- Do not borrow language from competitors' bios. The framework should produce a position the user can defend, not a remix of someone else's.
- If the user says "I want to be known for X" but their experience does not yet support X, name the gap and offer two routes: build the proof (with a 6 to 12-month plan) or pick adjacent positioning that does match their proof today.

### Template Usage

When a capability names a template, load it with the @ reference before writing, and follow its structure and footer. Users and other skills rely on the same headings appearing in the same places.

---

## Related Skills

- **/career-helper:career-coach (Tim)**: if you are not sure brand work is the right next step, start with Tim. Tim can run the ikigai questions first and route into this skill once direction is clear.
- **/linkedin-coach**: deeper tactics for the LinkedIn-specific layer (headline mechanics, post review, video script). This skill produces the brand strategy; LinkedIn Coach turns it into LinkedIn-shaped output.
- **/career-transitions**: for fractional, portfolio, or non-linear positioning, run career-transitions for the financial and structural plan, then this skill for the brand layer.
- **/employer-footprint**: if you also want a scored audit of what employers can see about you online, run that before refreshing the brand.
- **/social-media-review**: if cleanup of risky or off-brand legacy content is the priority, start there.
- **/career-navigator**: for a 3-month plan that includes brand-building activity (talks pitched, articles published, communities joined) alongside applications and networking.

---

*Personal Brand Helper | Career Helper Plugin | Prosper AI Consulting, UK*
