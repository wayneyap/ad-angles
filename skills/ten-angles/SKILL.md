---
name: ten-angles
description: Use when someone wants to test several advertising angles (for example "10 angles") without spending hours writing ad copy, asks for a batch of ads from a product description or URL, or says "run ten-angles". Produces a tagged batch of ready-to-launch ads plus the rules for reading the results.
---

# Ten angles

The person has a product and little time. Their time goes on three short decisions; everything else is yours. Target: **about 20 minutes of their attention** for a batch of 10 angles x 3 openings.

| Their time | What they do |
|---|---|
| ~10 min | Answer the setup questions once (skipped on later runs) |
| ~5 min | Cut your angle list to the ones worth testing |
| ~5 min | Read the finished batch and strike what they would not run |

Do not ask them to write, rewrite or brainstorm. Ask them to choose.

This skill is the conductor. The three skills below hold the method; load each when its step starts:

- `ad-angle-testing`: what an angle is, how a batch is laid out, how results are read
- `briefing-cold-ads`: what each ad has to say, in order
- `writing-ad-copy`: how it is written, and the checks before it ships

## Files (all in the person's project, under `ads/`)

| File | What it is |
|---|---|
| `ads/product.md` | The truth packet: facts, exact product words, real customer language |
| `ads/house-rules.md` | What this business will not say or do in an ad |
| `ads/banned-words.txt` | Optional. One word or phrase per line; the lint fails on them |
| `ads/batches/<date>/` | One batch: `angles.md`, one file per angle, `ads.csv`, `launch.md` |
| `ads/results-log.md` | What each angle taught, batch after batch |

Copy the starting files from this plugin's `templates/` folder if they are missing.

## Step 1. Setup (once)

If `ads/product.md` exists and is filled in, skip to step 2.

Otherwise, gather before asking. If they gave a URL or a repo, read it: the site, the pricing page, the sign-up flow, any reviews. Then search for the customer's own words: reviews of this product and its closest competitors, Reddit and forum threads about the problem (search the pain, not the brand), comments on competitors' ads. Copy phrases exactly, with where each came from.

Then ask only what you could not find, in one message, numbered, each with your best guess for them to confirm or fix:

1. Who buys this, and what was happening the week they went looking?
2. What did they try before, and why did it not work?
3. The offer a stranger gets: price, trial, guarantee, exact terms.
4. Anything you must never say or imply (claims, comparisons, topics).
5. Where the ads run and what counts as a result (purchase, sign-up, lead).
6. Rough test budget and how long they can let it run.

Write `ads/product.md` and `ads/house-rules.md`. Mark anything you inferred as INFERRED. If no real customer language exists anywhere, say so in the file: every angle is then a hypothesis.

## Step 2. Angles (their second decision)

Follow `ad-angle-testing` and step 2 of `writing-ad-copy`. Write **at least 20** candidate angles using every lens in `writing-ad-copy/mechanisms.md` at least once, then cut:

- Run the swap test. An angle that works under a competitor's name goes.
- Keep at most one of the first three that came to mind.
- Spread across awareness levels. At least three of the final ten open for people who do not yet know the product exists.

Show the survivors (aim for 12 to 14 so they can cut to 10) as one table and stop for their pick:

| # | Angle in one line | Who it is for | Awareness level | Rests on (packet item, or SPECULATIVE) | How common in this market |
|---|---|---|---|---|---|

Ask for one reply: the numbers to drop, and anything missing. No other questions.

## Step 3. Briefs and copy (yours, in parallel)

One fresh subagent per angle, so ten angles do not come back in one voice. Each gets the full `ads/product.md` and `ads/house-rules.md` as files (never your summary), its one angle row, and the instruction to follow `briefing-cold-ads` then `writing-ad-copy`. Each returns one file, `ads/batches/<date>/NN-<angle-slug>.md`:

- The tags: angle, persona, awareness level, format, mechanism, object, **what this ad is built to learn**
- The filled brief table (empty rows named as empty)
- **Three openings** that differ only in the opening (first line, or first frame for video)
- One primary text, one headline, one call to action
- The landing page line: the headline the click should land on, in the same words as the ad

Default format is the cheapest one that can carry the message (an image or a native-looking text post). Propose video only for an angle that needs it, and say why.

## Step 4. Checks (yours)

1. A fresh subagent that did not write anything reads the whole batch against the packet and house rules: invented facts, claims the business cannot back, anything a competitor could run unchanged. Fix what it finds, one round.
2. Batch check from `writing-ad-copy`: no sentence shape or phrase in more than a third of the ads.
3. Run the lint on every file: `python3 <writing-ad-copy skill directory>/copy_lint.py ads/batches/<date>/*.md`. Fix errors; weigh warnings.

## Step 5. Hand over (their third decision)

Write three things into the batch folder:

- `angles.md`: the grid, one row per ad, with its tags.
- `ads.csv`: one row per ad, ready to paste into an ads manager or a script. Columns: `ad_name, angle, persona, awareness, format, opening, primary_text, headline, cta, landing_headline, built_to_learn`. Name ads `<angle-slug>__<opening-number>` so results can be grouped by angle later.
- `launch.md`: one ad set per angle, three openings inside it (see `meta-campaign-structure` if they are on Meta). Then the rules, **written before launch**: the spend per ad that triggers a first look, the cost per result that stops an ad, the soft signals that buy an ad more time, and how many days it runs. If the budget is too small to read ten angles, say so and recommend how many to launch first.

Then show them the batch in the chat as a short list (angle, best opening, what it is built to learn) and ask which to strike. Do not launch, spend or change anything in an ad account without their explicit yes.

## Later: reading results

When they come back with numbers (pasted, a CSV export, or an ads connector), group by angle, not by ad. Use the "Read a test" table in `ad-angle-testing`. For each angle say: dead, alive in one opening, or proven, and what to make next. Append the lesson to `ads/results-log.md` as "this angle beat that angle for this audience". The next batch starts from that log: new openings on proven angles, new angles in place of dead ones.

## Common mistakes

- Asking the person open questions when a table to choose from would do.
- Writing all ten angles in one context: they come back as one idea ten times.
- Ten rewordings of one reason to care. Ten angles means ten different reasons.
- Shipping copy with no "built to learn" tag: the result will teach nothing.
- Inventing a customer quote, a number or a deadline to make an angle work. Mark it SPECULATIVE or drop it.
