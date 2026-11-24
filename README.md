# ad-angles

Test ten advertising angles without sitting down to write ad copy.

A Claude Code plugin. You describe the product once, pick from a table of angles, and get back a tagged batch of ads (10 angles x 3 openings) plus the rules for reading the results. About 20 minutes of your attention; the rest is the agent's.

## Install

In Claude Code:

```
/plugin marketplace add wayneyap/ad-angles
/plugin install ad-angles@ad-angles
```

## Use

Open Claude Code in any project folder (your product's repo is ideal, since the agent can read it) and say:

```
Run ten-angles for https://yourproduct.com
```

What happens:

1. **Setup, once (~10 min of you).** The agent reads your site, hunts for real customer language (reviews, Reddit, competitor ad comments), then asks only what it could not find. It writes `ads/product.md` and `ads/house-rules.md`.
2. **Angles (~5 min of you).** You get a table of 12 to 14 angles, each tagged with who it is for, how aware that person is, and what real material it rests on. Reply with the numbers to drop.
3. **Briefs and copy (none of you).** One fresh subagent per angle writes a brief, three openings, a primary text, a headline and the landing page line. A separate agent that wrote nothing checks the batch for invented facts and same-sounding lines, then a lint script runs.
4. **Hand over (~5 min of you).** In `ads/batches/<date>/`:
   - `angles.md`: the grid
   - `ads.csv`: one row per ad, named `<angle>__<opening>`, ready for an ads manager or a script
   - `launch.md`: the ad set layout and the stop rules, written before any money is spent
5. **Later.** Paste your results back and say "read the results". It groups by angle, says which are dead, alive or proven, and logs what to make next in `ads/results-log.md`.

## Why it works this way

- **More ads is the wrong lever.** Thirty ads on three ideas are three ads. A batch is a grid of angles x variations, and every ad is tagged with what it is built to learn.
- **An angle is a reason to care, not a wording.** Asking a model for "20 headlines" gives one idea twenty times. Angles are forced apart with a set of lenses and a swap test (if it works under a competitor's name, it goes).
- **The edge is the material.** Every model knows the formulas. Copy gets distinctive when it is built from things only your business has: a real screen, a real number, the customer's exact words. That is why setup builds a truth packet first.
- **Writers do not share a context.** Ten angles written in one sitting drift into one voice. Each gets its own agent and the raw packet.
- **Decide how to read the test before it runs.** Stop rules are written at launch, and results are read per angle.

## The skills

| Skill | Use it for |
|---|---|
| `ten-angles` | The whole run, start to finish. Start here. |
| `ad-angle-testing` | Planning a batch, reading results, iterating a winner, auditing an account |
| `briefing-cold-ads` | Deciding what an ad for strangers has to say, before writing |
| `writing-ad-copy` | Writing and checking the copy; includes `copy_lint.py` |
| `meta-campaign-structure` | Laying the batch out in a Meta ads account |

Each works on its own. Claude picks them up when the task matches, or call one by name: `/ad-angles:ad-angle-testing`.

## Your files

Everything lives in `ads/` in your project, as plain text you can edit and commit.

```
ads/
  product.md          truth packet (template in templates/)
  house-rules.md      what you will not say (template in templates/)
  banned-words.txt    optional, one phrase per line; the lint fails on them
  voice.md            optional, 2 to 5 finished pieces that sound like you
  results-log.md      what each angle taught
  batches/<date>/     angles.md, one file per angle, ads.csv, launch.md
```

## No Claude Code?

The skills are plain markdown. Paste `skills/ten-angles/SKILL.md` and the three skills it names into any capable chat model along with your product details. You lose the parallel writers and the lint, so ask it for one angle at a time.

## Credits

These skills condense other people's published practice, in our own words, with their claims left as their claims: Adam Taylor (angle testing), Derick Carneiro (the cold ad brief), Nick Theriot (Meta account structure), Dean Jackson (all cheese, no whiskers), and the direct-response record from Caples to Schwartz (the mechanisms list). Built and used on real ad accounts before being shared.

## License

MIT
