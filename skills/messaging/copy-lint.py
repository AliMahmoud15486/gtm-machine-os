#!/usr/bin/env python3
"""Copy linter — GTM Engine (generic).

Usage:  python3 05_copy-lint.py <file> [<file> ...]  [--phrases path/to/05_banned-phrases.txt]

Checks every line of the given copy files against a banned-phrase list.
- Phrase file format: one phrase per line.  '#' starts a comment.
  Prefix 'warn:' for phrases that need a human check (e.g. "never" is OK only with a condition).
  Optional reason after ' || '.
- Arabic is normalised (diacritics, tatweel, alef/ya/ta-marbuta forms) before matching; Latin is case-insensitive.
- Skip a line containing 'lint:ignore'. Skip a block between '<!-- lint:off -->' and '<!-- lint:on -->'
  (use for reference sections that *quote* banned phrases, e.g. a "Never say" list).
Exit code: 1 if any ERROR, else 0.  WARN never fails the run.
"""
import os, re, sys

def norm(s: str) -> str:
    s = re.sub(r"[ً-ْٰـ]", "", s)          # diacritics, superscript alef, tatweel
    s = re.sub(r"[أإآٱ]", "ا", s).replace("ى", "ي").replace("ة", "ه").replace("ؤ", "و").replace("ئ", "ي")
    s = re.sub(r"[-_]", " ", s)   # fake-order → fake order
    return s.lower()

def load(path):
    rules = []
    for raw in open(path, encoding="utf-8"):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        level = "ERROR"
        if line.lower().startswith("warn:"):
            level, line = "WARN", line[5:].strip()
        phrase, _, reason = line.partition(" || ")
        phrase = phrase.strip()
        if phrase:
            rules.append((level, phrase, norm(phrase), reason.strip()))
    return rules

def main(argv):
    phrases = os.path.join(os.path.dirname(os.path.abspath(__file__)), "05_banned-phrases.txt")
    files = []
    it = iter(argv)
    for a in it:
        if a == "--phrases":
            phrases = next(it)
        else:
            files.append(a)
    if not files:
        print(__doc__); return 2
    rules = load(phrases)
    errors = warns = 0
    for f in files:
        off = False
        for n, line in enumerate(open(f, encoding="utf-8"), 1):
            if "<!-- lint:off -->" in line: off = True; continue
            if "<!-- lint:on -->" in line: off = False; continue
            if off or "lint:ignore" in line:
                continue
            nl = norm(line)
            for level, phrase, np, reason in rules:
                # word-ish boundary for short Latin words; substring for Arabic/multi-word
                if " " not in np and not re.search(r"[%]", np):
                    # single word (Latin or Arabic): whole-word match so «ابدا» doesn't hit inside «ابدا» variants of other words
                    # letters = Latin, digits, Arabic letters; Arabic one-letter prefixes (و ف ب ل ك ال) are allowed before the word
                    suffix = r"[a-z]*" if re.fullmatch(r"[a-z]+", np) else r"(?:ه|ات|يه|يات|ا|ين|ون|ي|ها|هم|كم)?"
                    hit = re.search(rf"(?<![\w\u0621-\u064A])(?:و|ف|ب|ل|ك|ال|وال|بال|لل)?{re.escape(np)}{suffix}(?![\w\u0621-\u064A])", nl)
                else:
                    hit = np in nl
                if hit:
                    if level == "ERROR": errors += 1
                    else: warns += 1
                    print(f"{level}  {f}:{n}  «{phrase}»{('  — ' + reason) if reason else ''}\n        {line.strip()[:160]}")
    print(f"\n{errors} error(s), {warns} warning(s) — phrases: {phrases}")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
