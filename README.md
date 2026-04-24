# SST-improve

Enrichment of the UD_Slovenian-SST CoNLL-U dev file with speaker and event metadata from GOS.

## Source and output

- Official UD treebank: https://github.com/UniversalDependencies/UD_Slovenian-SST
- Upstream dev file used as source: https://github.com/UniversalDependencies/UD_Slovenian-SST/blob/dev/sl_sst-ud-dev.conllu
- Enriched output in this repo: [src/sst/sl_sst-ud-dev-enriched.conllu](src/sst/sl_sst-ud-dev-enriched.conllu)

## Coconstructions check

This repository contains the enriched SST dev file and can also serve as the working baseline for a coconstruction review or correction pass on top of that enrichment.

For background on `Backchannel=` / `Coconstruct=` annotation and for a fuller end-to-end workflow, see `unidive-cocos`:

- Repository: https://github.com/hulln/unidive-cocos
- Workflow overview: https://github.com/hulln/unidive-cocos/blob/main/README.md
- Coconstructions workflow: https://github.com/hulln/unidive-cocos/blob/main/docs/COCONSTRUCTIONS_EXTRACTION.md

## Validation

To validate the output file, follow the official UD instructions:
https://universaldependencies.org/contributing/validation.html

### Results after metadata enrichment (April 2026)

Validated with `validate.py --lang=sl --max-err=0` on both the original and enriched file. Results were identical — the enrichment introduced no new errors or warnings.

- **Warnings: 132** — pre-existing; mostly `fixed-without-extpos` (fixed expressions missing `ExtPos` feature) and `pron-det-without-prontype` (determiners missing `PronType`)
- **SYNTAX errors: 8** — pre-existing; `rel-upos-advmod` and `rel-upos-cc` mismatches (e.g. `se pravi` annotated with `cc` relation)
