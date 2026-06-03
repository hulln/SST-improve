# Verification summary

Date: 2026-06-04

**Source archive** (`metadata/gos/Gos.TEI.zip`)
- MD5 `3ee81e8e495ddfd58c2898cf08975b85` matches the value published for GOS 2.1
  on CLARIN.SI (handle 11356/1863) → genuine, uncorrupted file.
- All 1551 zip entries pass their CRC check → not corrupted/truncated.

**Extraction** (`metadata/gos/utterance-speaker.tsv`)
- Re-derived from the TEI two independent ways (XML parser + the build regex);
  both agree with each other and equal the committed file row-for-row:
  108,581 / 108,581, with 0 extra, 0 missing, 0 wrong.
- 19,023 utterances have no `who` in the TEI and are correctly left unmapped.

**The 10 manual samples** (`sample-report.md`)
- S01–S07: event and speaker labels each trace back to a real metadata row.
- S08 / S09 / S10: correctly emit NO speaker — two distinct speakers (S08),
  one known speaker plus an unresolved gap (S09), and no `who` at all (S10).

Conclusion: download is genuine and intact, extraction is faithful, and every
blank speaker comes from the source — not from a processing mistake.
