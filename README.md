# Spoken-corpus metadata enrichment (SST + GOS)

Adds **speaker** and **event** metadata (from the GOS 2.1 corpus) to UD Slovenian spoken
CoNLL-U files. One corpus-agnostic pipeline currently covers two corpora and can be pointed
at more. It **only inserts comment lines** — it never changes tokens, trees, or sentence
segmentation.

For project history, the task timeline, and full data provenance, see
[docs/background.md](docs/background.md).

What gets added — event metadata per document, speaker metadata per sentence:

```
# newdoc id = Gos013
# event_type = info-education
# event_domain = 2nd triennium, natural sciences
# event_channel = in-person
# event_description = Science and technology lesson in Year 5 of primary school; ...
# sent_id = Gos013.s1
# speaker_id = Am-prof-05653
# speaker_gender = male
# speaker_age = 30 to 59
# speaker_education = university or more
# speaker_residence = goriška
# text = ...
```

## The two corpora

| | SST | GOS |
|---|---|---|
| What it is | UD_Slovenian-SST — hand-corrected UD treebank | the **whole GOS**, automatically annotated in-house |
| Size | 344 docs / ~6,100 sentences | 1534 docs / 187,414 sentences |
| Subcorpora | a subset of GOS (287 Gos + 57 Artur) | Gos (287) · Artur-P/N/J (1192) · GosVL lectures (55) |
| Already has `# newdoc`/`# speaker_id`? | yes | no — reconstructed from sent_id, `# newpar id` and TEI |

**SST ⊂ GOS:** all 344 SST documents also exist in the GOS file (0 missing). They overlap in
*content* but differ in *annotation*: SST is hand-corrected; GOS is raw automatic annotation.

All metadata for **both** corpora comes from the same GOS 2.1 files under `metadata/gos/`.
Where the data comes from and the exact field→source mapping:
[metadata/gos/sources.md](metadata/gos/sources.md).

### Mixed-speaker Artur sentences

Artur sentences are resegmented UD sentences, not always original speech turns. For Artur,
speaker metadata is emitted only when the token-level `OriginalUtteranceId` values resolve
through TEI `who=` to exactly one speaker and no token-level utterance is unresolved. An audit
found 112 Artur sentences whose tokens map to more than one TEI speaker (3 with no strict
majority), plus 2 sentences that combine one known speaker with no-`who` utterance tokens.
These 114 cases are intentionally left without a singular sentence-level `# speaker_id`; for
review, speaker ranges are recorded in custom comments such as
`# suggested_speaker_segments = 1-2:SPK1(...); 3-4:SPK2(...)`.
Those custom comments, including `# mixed_speaker`, are audit/proposal annotations only; they
are not part of the current enriched corpus schema. See
[docs/working/artur-speaker-edge-cases/](docs/working/artur-speaker-edge-cases/).

## Repository layout

```
corpora/sst/   sl_sst-ud-{train,dev,test}.conllu            input  (gitignored)
               sl_sst-ud-{train,dev,test}-enriched.conllu   output (committed)
corpora/gos/   gos.conllu                                    input  (gitignored, ~400 MB)
               gos-enriched.conllu                           output (~408 MB, see note below)
metadata/gos/  Gos-speakers.tsv  Gos-speeches.tsv            GOS 2.1 metadata (shared)
               descriptions-en.tsv   utterance-speaker.tsv   generated lookup tables
               *.zip   sources.md                            sources (zips gitignored)
scripts/       enrich.py  corpora.py  translations.py  sources.py  build_*.py
```

> **GOS output size:** `gos-enriched.conllu` is ~408 MB. GitHub rejects files >100 MB on
> push, so either track it with **Git LFS** or share it outside git (OneDrive), the way the
> input was received. It is regenerated in ~20 s by `python scripts/enrich.py gos`.

## How to reproduce

Requires **Python 3.10+** (standard library only — no packages to install). The UD
validator under `tools/` is optional and used only for validation.

```
# 1. (once, or when GOS sources change) build the lookup tables
python scripts/build_utterance_speaker_map.py   # TEI -> utterance-speaker.tsv
python scripts/build_descriptions.py            # -> descriptions-en.tsv

# 2. enrich
python scripts/enrich.py sst     # -> corpora/sst/*-enriched.conllu
python scripts/enrich.py gos     # -> corpora/gos/gos-enriched.conllu
```

### What each script does

| Script | Role |
|--------|------|
| `scripts/translations.py` | Slovenian→English value maps (gender, age, education, type, domain, channel) |
| `scripts/build_utterance_speaker_map.py` | reads `Gos.TEI.zip`, writes `utterance-speaker.tsv` (utterance id → speaker id, from the TEI `who=` attribute) |
| `scripts/build_descriptions.py` | merges English titles from `docs/working/descriptions/*.tsv` into `descriptions-en.tsv` |
| `scripts/report_mixed_speaker_sentences.py` | writes the Artur speaker edge-case TSV/mini CoNLL-U under `docs/working/artur-speaker-edge-cases/` |
| `scripts/sources.py` | loads the four metadata tables |
| `scripts/corpora.py` | registry of corpora → their input/output files |
| `scripts/enrich.py` | the engine + CLI; streams a file and inserts the comment lines |
| `scripts/verify.py` | re-checks SST parity + GOS non-destructiveness, reports coverage |

To add a future corpus: drop its files under `corpora/<name>/` and add one entry to
`scripts/corpora.py`. The engine adapts to whatever the input already provides.

## Translations

Metadata values and event descriptions are translated Slovenian→English. The mapping tables
and the description workflow are in [docs/translations.md](docs/translations.md); the
field→source routing is in [metadata/gos/sources.md](metadata/gos/sources.md).

## Validation

The enrichment only inserts comment lines, so **input and enriched validate identically**.
Re-check anytime with **`python scripts/verify.py`** (SST parity + GOS non-destructiveness +
coverage). Official UD validator figures are recorded in
[docs/validation-results.md](docs/validation-results.md).

## Coconstructions check

This repo can also serve as the baseline for a coconstruction review on top of the
enrichment. Per-split workflow files live under `docs/working/coconstructions/`. Background:
`unidive-cocos` (https://github.com/hulln/unidive-cocos).
