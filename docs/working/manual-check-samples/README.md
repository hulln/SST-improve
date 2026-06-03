# Manual check samples for GOS enrichment

This folder contains deterministic random samples for manual inspection.

Start with `sample-report.md`, then compare:

- `input-samples.conllu` against `corpora/gos/gos.conllu`
- `enriched-samples.conllu` against `corpora/gos/gos-enriched.conllu`
- `source-mapping.tsv` against the metadata source files listed in its `source_file` and `line` columns

Seed: `20260603`
Sample count: `10`

The selected set includes normal document-start event+speaker cases, ordinary speaker-only sentences, one multiple-speaker Artur case, one known+unresolved Artur case, and one no-`who` unavailable-speaker case. For Gos/GosVL sentences, the report tracks carried `# newpar id` values the same way the enrichment script does.

Note: event metadata is emitted only at document start. In `source-mapping.tsv`, event rows for ordinary non-document-start samples are included only as document context and are marked that way.
