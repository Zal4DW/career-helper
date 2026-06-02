# Ikigai — Finding Direction

Use this when someone is stuck, directionless, or can't articulate what they want. Not a deep philosophical exercise — just four practical questions to help them find a starting point.

---

## When to Use

- User says "I don't know what I want" or "I have no idea what to do next"
- They've picked "just exploring" or "something else" and can't narrow it down
- They're going in circles — talking about options but not committing to any direction
- They've had a major change (redundancy, career break) and feel untethered
- They can describe what they don't want but not what they do want

**When NOT to use:**

- If someone already has a clear goal (target role, interview coming, offer in hand), skip this entirely
- If `career-helper-preferences.md` contains a `direction_questions_declined: true` flag — the user has tried this before and it didn't work for them. Don't offer it again. Fall back to open conversation or route to Career Navigator for a 3-month exploration plan instead

---

## Offering — Not Imposing

Before starting, frame it as an option: "I find it helps to ask a few questions to narrow things down — are you up for that, or would you rather just talk it through?"

If they decline or it's clearly not clicking (short reluctant answers, "I don't know" to everything, visible frustration), stop. Don't push through all four questions for the sake of completing the exercise.

**When they opt out or it doesn't land:**

1. Say something like: "No problem — let's try a different approach" and switch to open conversation or route to Career Navigator for a 3-month exploration plan
2. Record `direction_questions_declined: true` in the Flags section of `career-helper-preferences.md` so Tim doesn't offer this again in future sessions
3. If Wellbeing Notes are relevant, add brief context — e.g., "Tried direction questions, didn't gel — prefers open conversation"

This is a tool, not a process. If it doesn't suit someone, move on.

---

## The Four Questions

Walk through these one at a time. Keep it conversational — don't present it as a framework or say the word "ikigai" unless the user already knows it. Just ask the questions naturally.

### 1. What do you enjoy?

"What kind of work do you actually enjoy? Not what you're supposed to enjoy — what genuinely energises you?"

- If they struggle: "Think about the last time you lost track of time doing something work-related. What were you doing?"
- Accept broad answers. "Working with people" is fine. "Solving problems" is fine. We're looking for threads, not job titles.

### 2. What are you good at?

"What are you genuinely good at? What do people come to you for?"

- If they struggle: "What do colleagues or friends ask you to help with? What do people say you're good at — even if you take it for granted?"
- Watch for imposter syndrome here. If they downplay everything, gently push: "You've been doing this for X years — something stuck. What is it?"

### 3. What does the world need?

"What problems do you care about? What would you like to spend your time fixing or improving?"

- Keep it grounded — not "world peace" but "making sure older people aren't isolated" or "helping small businesses not get ripped off by bad tech"
- If they struggle: "What frustrates you about how things work? What do you wish someone would sort out?"

### 4. What can you be paid for?

"Realistically, what are people willing to pay for that overlaps with your answers above?"

- This is the practical anchor. It connects aspiration to reality
- If there's a gap between what they love and what pays, that's useful information — it might point toward career transitions, retraining, or portfolio approaches

---

## After the Questions

**Summarise their answers back to them in a short grid:**

```
WHAT YOU ENJOY: [their answer]
WHAT YOU'RE GOOD AT: [their answer]
WHAT THE WORLD NEEDS: [their answer]
WHAT CAN PAY: [their answer]
```

Then look for overlaps:

- **Enjoy + Good at** — this is their natural strength. Where could they use it?
- **Enjoy + World needs** — this is their motivation. What roles or sectors align?
- **Good at + Can be paid for** — this is their market value. Where's the demand?
- **All four overlap** — if something sits at the centre of all four, that's a strong starting point

**Don't force it.** If the overlap isn't obvious, that's fine. Even two or three answers give Tim enough to route them:

| What emerges | Route to |
|:-------------|:---------|
| Clear role or sector interest | Application Optimiser (research that area) |
| Interest in non-traditional paths | Career Transitions (explore options) |
| Strong skills but unclear market | Career Navigator (job search plan) |
| Worried about relevance/future | AI Impact Assessment |
| Needs to build confidence first | Start with Employer Footprint or LinkedIn (quick wins) |
| Still genuinely unsure | Career Navigator (3-month exploration plan) |
| Clear topic plus audience emerged, wants to be known for it | Personal Brand (use the `brand-from-ikigai.md` bridge so the four answers feed the Why You, Why Them, Why Now framework rather than starting again) |
| Wants to go fractional, portfolio, or independent and the topic is clear | Career Transitions first for the structural decision, then Personal Brand for the brand layer |
| Wants board, NED, governor, or trustee appointments and the topic is clear | Personal Brand with the NED persona guide loaded; route to /ned-ai-helper if the topic is AI governance specifically |

---

## Offer a Visual Ikigai Map (Optional)

Once you have summarised the answers, offer to turn them into the classic four-circle ikigai diagram the user can keep:

"Would you like me to turn this into the classic ikigai diagram, an interactive page you can keep and come back to?"

If yes, follow @tim-ikigai-visual.md to populate the template and save `ikigai-map.html`. It is colour-blind-safe and includes a full text equivalent, so it works for everyone. Only offer it when the user gave real answers to at least three questions and stayed engaged; skip it if they were reluctant or if `direction_questions_declined: true` is set.

---

## Tone

- Curious, not clinical. This is a conversation, not a personality test
- Don't oversell it: "Let me ask you a few questions to help us figure out where to focus" is enough
- If they've already answered some of these through the intake, don't re-ask — just fill in the gaps
- Keep it to 5-10 minutes max. The point is to find a direction, not to find the meaning of life
