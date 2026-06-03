# GOS data sources

## Metadata (the values used for enrichment)

The zip files in this directory are downloaded from the CLARIN.SI repository:

**Entry:** https://www.clarin.si/repository/xmlui/handle/11356/1863 (GOS 2.1)

| File | Contents |
|------|----------|
| Gos.TEI.zip | TEI XML transcriptions + `Gos-speeches.tsv` + `Gos-speakers.tsv` |
| Gos.TRS.zip | TRS transcription files |
| Gos.TXT.zip | Plain text transcriptions |
| Gos.vert.zip | Vertical (corpus) format |

The extracted files used for enrichment:
- `Gos-speeches.tsv` — document-level metadata (type, domain, channel, title)
- `Gos-speakers.tsv` — speaker-level metadata (age, sex, education, residence)

## The treebank being enriched (`corpora/gos/gos.conllu`)

- **Origin:** GOS, **automatically annotated in-house** by the project team and shared
  internally (via OneDrive) by a project collaborator. It is *not* a published treebank
  release, so it has no CLARIN
  link of its own; its linguistic annotation (UPOS/lemma/syntax) is the team's automatic
  output and may differ from any public version.
- **Identity verified against GOS 2.1:** although the annotation is in-house, the document
  and speaker identity are GOS 2.1's. Checked when building this pipeline:
  - all **1534** document ids in the file are present in `Gos-speeches.tsv` (0 unmatched);
  - **90,300 / 90,303** referenced utterance ids resolve to a speaker in the TEI
    (the 3 that do not are utterances the TEI itself leaves without a `who` attribute).
  Because the join keys (document id, utterance id) are exact GOS 2.1 ids, the metadata is
  attached to the correct documents and speakers regardless of the automatic annotation.

## What field comes from where (enrichment output)

| Output comment | Source column / file | Transformation |
|----------------|----------------------|----------------|
| `# event_type` | `Gos-speeches.tsv` TYPE | fixed SL→EN map (`scripts/translations.py`) |
| `# event_domain` | `Gos-speeches.tsv` DOMAIN | fixed SL→EN map |
| `# event_channel` | `Gos-speeches.tsv` CHANNEL | fixed SL→EN map |
| `# event_description` | `Gos-speeches.tsv` TITLE | English from `descriptions-en.tsv`, else raw SL title |
| `# speaker_id` | TEI `who="#..."` (→ `utterance-speaker.tsv`) | none |
| `# speaker_gender` | `Gos-speakers.tsv` SEX | fixed SL→EN map |
| `# speaker_age` | `Gos-speakers.tsv` AGE | fixed SL→EN map |
| `# speaker_education` | `Gos-speakers.tsv` EDUCATION | fixed SL→EN map |
| `# speaker_residence` | `Gos-speakers.tsv` PERM-RESD | kept in Slovenian (first region) |

English event descriptions come from `descriptions-en.tsv`; for how they are produced and
which were translated when, see [../../docs/translations.md](../../docs/translations.md).
