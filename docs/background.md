# Background

Plain-English context for this repository. The detailed task briefs sent during the work are
kept locally under `docs/instructions/` and are **not committed** (private); this file is the
public summary. For what the repo does and how to run it, see [../README.md](../README.md).

## Timeline

### Task 1 — SST metadata enrichment (April 2026)
- Added speaker and event metadata to the **UD_Slovenian-SST** treebank
  (source: https://github.com/UniversalDependencies/UD_Slovenian-SST).
- Metadata values and event descriptions were translated Slovenian → English.
- A related **coconstruction** review scaffold was produced for the SST splits
  (`docs/working/coconstructions/`).

### Task 2 — GOS metadata enrichment + general pipeline (June 2026)
- Applied the same metadata to the **full GOS** treebank (composition in the README).
- Generalised the one-off SST script into a corpus-agnostic, config-driven pipeline
  (`scripts/`), and re-ran SST through it to confirm byte-for-byte identical output.

## See also

- Data provenance + field→source mapping (GOS): [../metadata/gos/sources.md](../metadata/gos/sources.md)
- Translation tables + description workflow: [translations.md](translations.md)
- Official UD validator results: [validation-results.md](validation-results.md)
