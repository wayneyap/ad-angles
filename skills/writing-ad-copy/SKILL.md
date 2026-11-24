---
name: writing-ad-copy
description: Use when writing, rewriting or reviewing ads, hooks, headlines, landing pages or video scripts when briefing agents to write them, or when copy reads generic, choppy, same-sounding, or could run unchanged under a competitor's name.
---

# Writing ad copy

**The edge is the material, not the technique.** Every model knows the formulas, so formula-led copy lands in the middle of what everyone else writes. Copy gets distinctive when it is built from things only this business has: a real object, a real moment, real words. Technique comes last.

**House rules win.** Read `ads/house-rules.md` first if it exists. Nothing invented: no made-up numbers, customers, stories or proof.

## Before any line is written

For an ad, video or ad landing page aimed at strangers, fill the brief in `briefing-cold-ads` first: it decides what gets said, this skill decides how.

Read `ads/product.md`, the truth packet (real product material, exact screen words, real customer language, facts; template in this plugin's `templates/product.md`). If it does not exist or is thin, build it first; do not write around the gap. Writers and agents get the packet as an input file, never a summary of it.

## The steps

1. **Pick the object.** One concrete real thing the piece turns on: a screen, a number, a part, a step in her routine. Curiosity needs an object ("these mistakes", not "mistakes"). No object, no piece.
2. **Angles before lines, spread wide.** Write ten angles first: different reasons to care, not different wordings. Each angle changes the problem, the moment, the cause, the comparison or the proof, and cites the packet item it rests on. No packet item: mark it SPECULATIVE. Beside each, note how common it is in this market (seen everywhere / sometimes / rarely). The first three that come to mind are usually the ones everyone runs: keep at most one of them. Use `mechanisms.md` to spread them out.
3. **Swap test.** Put a competitor's name on it. If it still works, drop it.
4. **Write the whole path as one piece.** Ad opening, ad text, headline, landing page, first screen: the same question in the same words all the way down, ending on words the product really shows. Never write the ad and the page in separate sittings.
5. **Diagnose in a fresh context, then one revision.** The critic must not be the writer: hand the draft to a fresh subagent with the truth packet and the house rules, never your reasoning. Separate reads, each with one job: the customer (would she say this?), the skeptic (what sounds too convenient?), the swap test, the rule check, the rhythm read. Rank the worst problems. Fix only those. One round, two at most: polishing in a loop sands off the sharp part.
5b. **Batch check.** When several pieces ship together, read them side by side. No sentence shape, turn or phrase in more than a third of them (count it). Vary length on purpose: some very short, some longer. One idea can run through a batch; one sentence cannot.
6. **Rhythm pass** (below), then run `python3 copy_lint.py <file>` (the script sits in this skill's directory; it flags stock AI phrasing, choppy rhythm and any words listed in `ads/banned-words.txt`).
7. **Tag it** with angle, mechanism and object, so a result says what to make next. Record results in `ads/results-log.md` as "this angle beat that angle for this audience", not "headline B won".

## Rhythm (read it aloud)

Two ways to get it wrong: a staccato run of five-word sentences, and thick paragraphs of long joined sentences. Land between them.

- A paragraph is one or two sentences. Three is rare. Leave white space.
- Lengths rise and fall: a longer sentence, then a short one. After two of similar length, change it.
- Do not pad a sentence with "and", "so" or "since" to make it longer. Split it where the turn is.
- Break a rule on purpose a few times per piece, where it adds voice: a one-word sentence as its own paragraph, a fragment, a sentence that starts with "Because", "And" or "But". Each has to be earned by the line before it.
- A run of five short sentences reads like slogans. Join some.
- Line breaks are for drama: break before the turn, and let the line that matters stand alone.
- Give it character: concrete nouns, odd true details, an opinion now and then.
- Vary the real objects: check which examples other pieces already use before picking one.
- These are guides for the ear, not counts to hit.

## Forms

| Form | Shape |
|---|---|
| Opening (image or video) | Her situation in her words, plus the object. Readable at a glance. |
| Ad text | One or two full sentences: the moment, what she does, what she gets. The offer inside the first lines, not after the cut. |
| Landing page from an ad | One screen. The ad's question as the headline, one sentence of what happens next, one real object, one button, the offer terms beside it. Nothing else to read, nowhere else to go. |
| Email | Subject and preview text written as a pair (the preview finishes the thought, it does not repeat it). One story, one link. A P.S. that carries the link or one more true detail. In a sequence, the last lines leave one thread open that the next email picks up. |
| Video script | The object arrives early. The real screen is the turn of the story. End on the action and the offer, spoken. |

## Voice file

If `ads/voice.md` exists, writers get it as an input file: measurable rules plus two to five finished pieces the owner picked as "this is us". Examples teach voice better than adjectives. More than five examples adds noise.

## Common mistakes

- Starting from the product ("write a page for X") instead of from what she must notice first.
- Asking for "20 headlines": you get one idea twenty times.
- Handing writers a facts summary: five writers then produce one vote.
- Specificity that was made up to sound specific.
- A hook that implies the product knows something it cannot know.
