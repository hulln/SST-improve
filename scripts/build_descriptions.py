"""
Build / refresh the unified English event-description table for GOS documents.

Only the ``Gos`` and ``GosVL`` subcorpora have real (Slovenian) event descriptions;
``Artur`` "titles" are just document ids, so the engine falls back to the raw title
for those and they are intentionally excluded here.

Output ``metadata/gos/descriptions-en.tsv`` has columns ``doc_id``, ``slovenian``,
``english``. English is seeded, in priority order, from:

  1. the existing ``descriptions-en.tsv`` (so manually added translations persist),
  2. the per-split SST translation files
     ``docs/working/descriptions/descriptions-{split}-for-translation.tsv``.

Slovenian is always taken from the canonical ``Gos-speeches.tsv`` TITLE. Docs left
with an empty English column still need translating (reported on stderr).
"""

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEECHES = ROOT / "metadata" / "gos" / "Gos-speeches.tsv"
OUT_TSV = ROOT / "metadata" / "gos" / "descriptions-en.tsv"
WORKING = ROOT / "docs" / "working" / "descriptions"

REAL_DESCRIPTION_SUBCORPORA = {"Gos", "GosVL"}


def load_titles() -> dict[str, tuple[str, str]]:
    """doc_id -> (subcorpus, slovenian title) for Gos/GosVL docs."""
    titles: dict[str, tuple[str, str]] = {}
    with open(SPEECHES, encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            sub = row["SUBCORPUS"].strip()
            if sub in REAL_DESCRIPTION_SUBCORPORA:
                titles[row["TEXT-ID"].strip()] = (sub, row["TITLE"].strip())
    return titles


def load_english_seed() -> dict[str, str]:
    """doc_id -> english, merged by priority (existing table first, then SST TSVs)."""
    english: dict[str, str] = {}

    def absorb(path: Path, sl_col: str, en_col: str) -> None:
        if not path.exists():
            return
        with open(path, encoding="utf-8") as f:  # text mode normalises CRLF
            for row in csv.DictReader(f, delimiter="\t"):
                doc = row["doc_id"].strip()
                en = (row.get(en_col) or "").strip()
                if en and doc not in english:
                    english[doc] = en

    absorb(OUT_TSV, "slovenian", "english")
    for path in sorted(WORKING.glob("descriptions-*-for-translation.tsv")):
        absorb(path, "slovenian", "english")
    return english


def main() -> None:
    titles = load_titles()
    english = load_english_seed()

    rows = sorted(titles.items())
    with open(OUT_TSV, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["doc_id", "slovenian", "english"])
        for doc, (_sub, sl) in rows:
            w.writerow([doc, sl, english.get(doc, "")])

    missing = sorted(doc for doc, (_s, _t) in rows if not english.get(doc))
    by_sub: dict[str, int] = {}
    for doc, (sub, _t) in rows:
        by_sub[sub] = by_sub.get(sub, 0) + 1
    print(f"Wrote {OUT_TSV}: {len(rows)} docs ({by_sub})", file=sys.stderr)
    print(f"Missing English: {len(missing)}", file=sys.stderr)
    if missing:
        print("  " + ", ".join(missing[:60]), file=sys.stderr)


if __name__ == "__main__":
    main()
