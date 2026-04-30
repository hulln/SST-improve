# SST-improve

Enrichment of the UD_Slovenian-SST CoNLL-U files with speaker and event metadata from GOS.

## Source and output

- Official UD treebank: https://github.com/UniversalDependencies/UD_Slovenian-SST
- Upstream files used as source:
  - `sl_sst-ud-train.conllu`
  - `sl_sst-ud-dev.conllu`
  - `sl_sst-ud-test.conllu`
- Enriched outputs in this repo:
  - [src/sst/sl_sst-ud-train-enriched.conllu](src/sst/sl_sst-ud-train-enriched.conllu)
  - [src/sst/sl_sst-ud-dev-enriched.conllu](src/sst/sl_sst-ud-dev-enriched.conllu)
  - [src/sst/sl_sst-ud-test-enriched.conllu](src/sst/sl_sst-ud-test-enriched.conllu)

## Coconstructions check

This repository contains enriched SST files and can also serve as the working baseline for a coconstruction review or correction pass on top of that enrichment.

Per-split coconstruction workflow files live under `docs/working/coconstructions/`:

- `coconstruction-train-review.tsv` / `coconstruction-train-proposed-changes.md`
- `coconstruction-dev-review.tsv` / `coconstruction-dev-proposed-changes.md`
- `coconstruction-test-review.tsv` / `coconstruction-test-proposed-changes.md`

For background on `Backchannel=` / `Coconstruct=` annotation and for a fuller end-to-end workflow, see `unidive-cocos`:

- Repository: https://github.com/hulln/unidive-cocos
- Workflow overview: https://github.com/hulln/unidive-cocos/blob/main/README.md
- Coconstructions workflow: https://github.com/hulln/unidive-cocos/blob/main/docs/COCONSTRUCTIONS_EXTRACTION.md

## Validation

To validate the output file, follow the official UD instructions:
https://universaldependencies.org/contributing/validation.html

### Results after metadata enrichment for all splits (April 2026)

Validated with the repo-local UD validator:
`python3 tools/validate.py --lang=sl --no-warnings --max-err=0 <file>`

For `train`, `dev`, and `test`, the original and enriched files produced identical validation summaries. The enrichment introduced no new warnings or errors.

| Split | Before enrichment | After enrichment |
|-------|-------------------|------------------|
| `train` | Warnings: 870; SYNTAX errors: 78 | Warnings: 870; SYNTAX errors: 78 |
| `dev` | Warnings: 132; SYNTAX errors: 8 | Warnings: 132; SYNTAX errors: 8 |
| `test` | Warnings: 145; SYNTAX errors: 18 | Warnings: 145; SYNTAX errors: 18 |

These validator failures are pre-existing in the upstream SST files; they are not caused by the metadata enrichment.
