# Validation results

Snapshot of official UD validator results for the enriched files. The enrichment only
inserts comment lines, so **input and enriched validate identically** — any finding is a
property of the upstream/source treebank, not of the enrichment.

Validator: `python3 tools/validate.py --lang=sl <file>`
(https://universaldependencies.org/contributing/validation.html). Last run: **2026-06-03**.

## SST — full validation, identical before and after

| Split | Warnings | Syntax errors |
|-------|---------:|--------------:|
| train | 870 | 78 |
| dev   | 132 | 8 |
| test  | 145 | 18 |

These are pre-existing in the upstream UD_Slovenian-SST files.

## GOS — identical before and after

The GOS treebank is an **automatic** annotation, so it does not pass validation on its own.
The counts are the same on the input `gos.conllu` and the enriched `gos-enriched.conllu`:

| Level | Result |
|-------|--------|
| L1–L2 (format + morphology) | 30 syntax + 64,912 metadata errors |
| L3+ (syntax) | validator crashes (same crash on input and enriched) |

- The **64,912 metadata errors** are `missing-text`: the `Artur` sentences have no `# text`
  line (a property of the auto-annotation; the enrichment does not add text).
- The **L3+ crash** is triggered by 10 tokens with an empty `DEPREL` in the auto-annotation
  (`tools/udtools` raises on them); it happens identically on both files.

Fixing these would mean correcting the automatic annotation — outside the scope of metadata
enrichment.

## Proof the enrichment changed nothing else

- **SST:** re-running the pipeline reproduces the committed `*-enriched.conllu` byte-for-byte.
- **GOS:** removing the inserted comment lines from `gos-enriched.conllu` reproduces the input
  `gos.conllu` byte-for-byte.

Both are re-checkable with `python scripts/verify.py`, which also reports GOS coverage
(1534 documents, 187,414 sentences, 187,264 with a speaker, 150 without a sentence-level
speaker block). Of the 150 no-speaker sentences, 36 have no available TEI `who=` metadata and
114 are Artur sentence-level speaker edge cases: 112 contain multiple known TEI speakers, and
2 combine one known speaker with tokens from a no-`who` utterance.
