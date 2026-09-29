# Bio Library Templates

Capability D of the personal-brand skill. Produces a coherent set of bios across LinkedIn About, X/Twitter, speaker bio, podcast guest bio, conference proposal bio, About page, email signature, and (where relevant) board bio.

UK English. No em dashes. No emojis. Oxford comma. Second person.

---

## Role and Objective

You are writing every public-facing bio surface a user will need. The aim is consistency: every bio should sound like the same person, told at different lengths, for different purposes, with the same Why You, Why Them, Why Now underneath.

What "consistency" means in practice:

- The distinct angle is the same across every surface
- The audience is named or implied in every surface
- The proof points are reused (with different framing depending on length)
- The voice does not lurch from buttoned-up on LinkedIn to flippant on X

What it does not mean:

- Bios should not be carbon copies. Length, channel, and reader intent change what to lead with.

Output: a single document with bios at every length the user actually needs, drafted, with two or three options where useful, ready to be reviewed and confirmed by the user.

---

## Inputs Required

- The foundation document (Capability A output) at minimum
- Existing bios the user wants to refresh (paste them in)
- Any specific contexts the user is preparing for (e.g., "I have a podcast pitch on Friday, I need the guest bio version")

If the foundation does not exist, do not invent one. Run a short version of Capability A first.

---

## Critical Principles

**Lead with proof, not adjectives.** The first sentence of any bio is the hardest. It must place the user (role, sector, signal of credibility) without reaching for "passionate" or "highly experienced". Use specific facts.

**Audience first, not chronologically.** Bios are not CVs. The audience does not need the user's career in order; they need to know in three seconds whether this is the right person for them. Lead with the position; the chronology, if useful, is a supporting line.

**Same proof, different framing.** A two-exits founder appears as "two prior exits" in a one-line bio, "founded and exited two B2B SaaS businesses (placeholder, confirm names)" in a paragraph bio, and "founder, two exits in B2B SaaS, now working as fractional CTO" in a podcast bio. Same fact, different framing.

**Cite carefully.** This is the highest-risk area for confabulation. Names, employers, awards, publications, and speaking history must be confirmed by the user. Use `{{PLACEHOLDER}}` for anything unconfirmed; do not invent.

---

## The Bio Library

Each bio uses the foundation document. Where length forces a cut, cut adjectives before facts.

### 1. LinkedIn About (long, 1,500 to 2,000 characters)

Used by: recruiters, hiring managers, prospective clients, audience members coming via posts.

Structure:

```text
[Two-sentence hook: distinct angle plus audience plus why-now.]

[Three to four sentences of permission slip: roles, projects, scars, results, told as a thread, not a list.]

[Two to three sentences naming the audience and the problem you help with: "I work with [audience] who [problem]."]

[One paragraph of optional context: previous chapters of the career, or specific themes you write about, or current focus.]

[A short closing line on what to do next: "If you are [audience] working on [problem], I am most reachable at {{CONTACT_METHOD}}."]
```

Length target: 1,500 characters. LinkedIn allows up to 2,600; using all of it is rarely worth it.

### 2. LinkedIn About (medium, 800 to 1,200 characters)

Same structure, with the optional context paragraph removed and the permission slip tightened to two sentences.

Use this for users who genuinely have less to say, or for users early in a career chapter where padding would force invention.

### 3. LinkedIn About (trimmed, 400 to 600 characters)

Two-sentence hook, two-sentence permission slip, one-line audience and contact. Use when the user does not want to commit to a longer version yet, or is testing positioning.

### 4. LinkedIn Headline (220 characters max)

Cross-reference: `@../linkedin-coach/references/linkedin-headline.md` for goal-specific formulas. The personal-brand version is positioning-led:

```text
[Distinct angle in 4 to 6 words] for [audience] | [proof point in 4 to 6 words] | [optional why-now in 3 to 5 words]
```

Example shape (illustrative; never invent for a real user):

> Boring AI for regulated boards | ex-FCA, two boards | post-AI Act readiness

Provide three options with different emphases (proof-led, audience-led, why-now-led) and let the user pick.

### 5. X/Twitter Bio (160 characters)

Constraint: 160 characters including spaces. Punchy, audience-aware, voice-true.

Pattern:

```text
[Distinct angle, 4 to 8 words]. [Audience, 3 to 5 words]. [Proof, 3 to 8 words]. [Optional link or handle reference.]
```

Example shape (illustrative):

> Boring AI for regulated boards. NEDs, governors, trustees. Ex-FCA. Currently writing about post-AI-Act board readiness.

Provide two or three options. Read-aloud test: if it cannot be said in one breath, cut.

### 6. Speaker Bio (one-paragraph, 80 to 120 words)

Used by: conference programmes, panel introductions, podcast show notes.

Structure:

```text
[Sentence 1: current role, distinct angle, audience, in third person.]
[Sentence 2: permission slip; the strongest two or three proof points.]
[Sentence 3: what the user writes, speaks, or works on, with one specific recent example if available.]
[Sentence 4: a personal touch (book, hobby, location), one line, optional, never twee.]
```

Always offer a third-person and a first-person version. Conferences default to third person; podcasts vary.

### 7. Speaker Bio (three-sentence)

A tighter version for printed programmes and panel boards:

```text
[Role, distinct angle, audience.]
[Strongest two proof points.]
[One line on the current focus or one specific recent piece of work.]
```

### 8. Speaker Bio (one-line, 25 to 35 words)

For spoken introductions and lower-thirds:

```text
[Name] is [distinct angle] for [audience], with [proof in 5 to 8 words].
```

### 9. Podcast Guest Bio (60 to 90 words)

Used by: hosts when introducing the user. This is where the user wants the host to be able to say something specific that primes the conversation.

Structure:

```text
[Sentence 1: the position, told for a listening audience.]
[Sentence 2: the proof, told as a story moment, not a list.]
[Sentence 3: the current focus or argument the user is working on, so the host has a hook.]
```

Avoid jargon. The audience is listening, often distracted, often new to the user.

### 10. Conference Proposal Bio

Submitted alongside a talk proposal. Bias is toward credibility for that specific talk:

```text
[Sentence 1: position relative to the talk topic.]
[Sentence 2: proof points specifically relevant to the talk topic.]
[Sentence 3: previous talks, panels, or publications on the topic, if any.]
[Sentence 4: current role and one line on what the talk argues.]
```

If the user has not given the talk before, that is fine; do not invent prior talks. Lead with the strongest adjacent proof.

### 11. About Page (the user's own site, 200 to 400 words)

This is the canonical version. It can be longer because the reader has chosen to be there.

Structure:

```text
[Opening paragraph: distinct angle, audience, why-now. Written to feel like a person, not a press release.]
[Middle paragraph: permission slip; the proof, told as a thread of work, not a list.]
[Optional paragraph: themes the user writes or speaks about, with three to five linked examples if they exist.]
[Closing paragraph: how to get in touch, what kinds of conversation are welcome, and what to expect.]
```

The About page is where voice matters most. Read aloud. Cut anything that makes the user wince.

### 12. Email Signature Line

A single line, often overlooked, that gets read by every recipient:

```text
[Name] | [distinct angle, 5 to 8 words] | [link to site or canonical bio]
```

Optional second line for current focus:

```text
Currently: [one specific thing the user is working on or writing about].
```

The "Currently" line is the most-read piece of personal-brand content most users have. Update it monthly.

### 13. Board Bio (where relevant)

Used by: NED applications, governor and trustee panels, committee invitations. This bio is the most formal and the most fact-dense.

Structure:

```text
[Sentence 1: name, current board roles or executive role.]
[Sentence 2: most senior or relevant prior board roles, with sectors and dates if confirmed.]
[Sentence 3: distinct angle relevant to a board context (governance specialism, sector knowledge, regulatory background).]
[Sentence 4: notable executive roles and outcomes, framed for board credibility.]
[Sentence 5: optional: relevant memberships, qualifications, or chartered status.]
```

Cross-reference: `@ned-personal-brand-guide.md` if the user is positioning specifically for board work.

---

## Step-by-Step

1. Load the foundation document.
2. Confirm with the user which surfaces they actually need. Do not generate every bio in this library if half are not relevant.
3. Draft each requested bio using the templates above. Where two or three options would help, provide them with one-line trade-off notes.
4. Use `{{PLACEHOLDER}}` for any name, employer, metric, award, publication, or talk that is not confirmed.
5. Run the quality checks below.
6. Save to the output document.

---

## Quality Checks Before Delivering

1. **Consistency check**: read all bios aloud, in order from longest to shortest. Do they sound like the same person? If a tone shift happens, fix it.
2. **Length check**: each bio is within its stated character or word range. LinkedIn About at 2,500 characters is too long; X bio at 165 characters will not save.
3. **Confabulation sweep**: every employer, role, metric, award, publication, and talk is either confirmed by the user or marked as `{{PLACEHOLDER}}`. No exceptions.
4. **Hyperbole sweep**: search for "world-class", "transformational", "industry-leading", "passionate", "highly experienced", "results-driven", "strategic visionary". Cut and rewrite with the specific underlying claim.
5. **Audience presence**: the audience appears, named or implied, in every bio long enough to mention it. If the audience is missing, add it.
6. **Voice fit**: the bios match the voice rules from the foundation. Read each bio aloud; if any of it makes the user wince, rewrite.

---

## Output

Save to `personal-brand-bio-library.md` (workspace root) or `applications/{role-slug}/personal-brand-bio-library.md` (role-specific).

Use the structure in `@personal-brand-output-template.md`. Preserve the footer.

---

## Tone

- Spare. Bios reward concision; almost every draft is too long on the first pass.
- Honest. If a claim cannot be made cleanly, do not make it. Reach for the nearest defensible version.
- Voice-faithful. If the user is dry, the bios are dry. If the user has a streak of warmth, let it land.
- Patient with the user when they wince. Most people find their own bio harder to read than a stranger's. That is normal; it is not a sign the bio is wrong.
