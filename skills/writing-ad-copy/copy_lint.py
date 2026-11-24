#!/usr/bin/env python3
"""Lint copy for AI-sounding patterns and banned words. Usage: copy_lint.py FILE [...]. Exit 1 on errors.

Banned words: one word or phrase per line in ads/banned-words.txt (relative to where you run it)."""
import os, re, sys, statistics

STOCK = ["unlock", "journey", "delve", "dive into", "tapestry", "embark", "elevate", "seamless",
         "empower", "transform", "navigate", "harness", "fast-paced", "game-changer", "game changer",
         "deep dive", "ever-evolving", "whether you're", "whether you are", "in today's", "rich tapestry"]
OPENERS = [r"^\s*imagine\b", r"^\s*have you ever wondered", r"^\s*picture this"]
CLAIMS = ["guaranteed result", "miracle"]
if os.path.exists("ads/banned-words.txt"):
    CLAIMS += [l.strip().lower() for l in open("ads/banned-words.txt", encoding="utf-8") if l.strip() and not l.startswith("#")]
NOT_X_Y = [r"\bnot (just|only|merely) [^.;]{1,60}?,? but\b", r"\bit'?s not [^.;]{1,50}?[,;—-]+ ?it'?s\b",
           r"\bisn'?t (just|only) [^.;]{1,50}?[,;—-]+ ?it'?s\b", r"\bnot a [^.;]{1,40}?\. (it'?s|it is) a\b"]

HEDGES = ["arguably", "it is worth noting", "it's worth noting", "in many cases", "studies show", "experts agree", "serves as", "stands as a", "in today's"]

def sentences(t):
    return [s for s in re.split(r"(?<=[.!?])\s+", t) if s.strip()]

def lint(text):
    errs, warns = [], []
    low = text.lower()
    words = len(text.split()) or 1
    for w in STOCK:
        if w in low: errs.append(f"stock word/phrase: '{w}'")
    for w in HEDGES:
        if w in low: warns.append(f"hedge or vague authority: '{w}'")
    for p in OPENERS:
        if re.search(p, text, re.I | re.M): errs.append(f"cliché opener: /{p}/")
    for c in CLAIMS:
        if re.search(r"\b" + re.escape(c), low): errs.append(f"banned or risky claim: '{c}'")
    for p in NOT_X_Y:
        for m in re.finditer(p, text, re.I): errs.append(f"'not X, it's Y' pattern: '{m.group(0)[:60]}'")
    dashes = text.count("—") + text.count(" -- ")
    if dashes > max(1, words // 300): errs.append(f"em dashes: {dashes} (max {max(1, words//300)})")
    if "!" in text: errs.append("exclamation mark")
    if re.search(r"\b\w+, \w+,? and \w+\b", text) and len(re.findall(r"\b\w+, \w+,? and \w+\b", text)) >= 2:
        warns.append("repeated three-item lists")
    ss = [len(s.split()) for s in sentences(text)]
    if len(ss) >= 6 and statistics.pstdev(ss) < 3.5:
        warns.append(f"uniform sentence length (stdev {statistics.pstdev(ss):.1f})")
    run = best = 0
    for n in ss:
        run = run + 1 if n <= 7 else 0
        best = max(best, run)
    if best >= 3:
        warns.append(f"choppy: {best} short sentences in a row (join some; keep short beats rare)")
    if len(ss) >= 5 and sum(1 for n in ss if n <= 7) / len(ss) > 0.5:
        warns.append("choppy: more than half the sentences are 7 words or fewer")
    if re.search(r"\?\s+[A-Z][^.?!]{0,60}\.", text) and text.count("?") >= 3:
        warns.append("many rhetorical questions")
    return errs, warns

if __name__ == "__main__":
    bad = False
    for f in sys.argv[1:]:
        e, w = lint(open(f, encoding="utf-8").read())
        print(f"{f}: {len(e)} errors, {len(w)} warnings")
        for x in e: print("  ERROR", x)
        for x in w: print("  warn ", x)
        bad |= bool(e)
    sys.exit(1 if bad else 0)
