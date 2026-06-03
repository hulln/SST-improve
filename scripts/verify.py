"""
Re-runnable correctness checks for the enrichment. Run: python scripts/verify.py

It proves the two invariants this project relies on:

  SST  — re-running the pipeline reproduces the committed *-enriched.conllu byte-for-byte
         (so the metadata step changed nothing vs. the reviewed SST output).
  GOS  — removing the inserted comment lines from gos-enriched.conllu reproduces the input
         gos.conllu byte-for-byte (so the enrichment is purely additive — no token, tree or
         segmentation was touched). It also reports document/speaker coverage.

Exit code is non-zero if any check fails. Needs the (git-ignored) input files present.
"""

import re
import sys
import tempfile
from pathlib import Path

from corpora import (
    CORPORA,
    DESCRIPTIONS_TSV,
    SPEAKERS_TSV,
    SPEECHES_TSV,
    UTTERANCE_SPEAKER_TSV,
)
from enrich import Context, enrich_file
from sources import (
    load_descriptions,
    load_speakers,
    load_speeches,
    load_utterance_speaker,
)

# Lines the engine inserts (so we can strip them back out for the GOS check).
# Note: in the raw GOS file only Artur documents lack a "# newdoc id"; those are the
# only newdoc lines the engine synthesises, hence the Artur-specific newdoc pattern.
INSERTED = re.compile(
    r"^# (event_(type|domain|channel|description)"
    r"|speaker_(id|gender|age|education|residence)) = "
    r"|^# newdoc id = Artur"
)


def _context() -> Context:
    speakers = load_speakers(SPEAKERS_TSV)
    descriptions = load_descriptions(DESCRIPTIONS_TSV)
    speeches = load_speeches(SPEECHES_TSV, descriptions)
    utt2spk = load_utterance_speaker(UTTERANCE_SPEAKER_TSV)
    return Context(speakers, speeches, utt2spk)


def check_sst(ctx: Context) -> bool:
    ok = True
    for in_path, out_path in CORPORA["sst"].io:
        if not in_path.exists() or not out_path.exists():
            print(f"  SKIP {out_path.name} (input or committed output missing)")
            continue
        with tempfile.NamedTemporaryFile("w+", suffix=".conllu", delete=False) as tmp:
            tmp_path = Path(tmp.name)
        enrich_file(in_path, tmp_path, ctx)
        identical = tmp_path.read_bytes() == out_path.read_bytes()
        tmp_path.unlink()
        print(f"  {'OK  ' if identical else 'FAIL'} {out_path.name}: "
              f"{'byte-for-byte identical to committed' if identical else 'DIFFERS'}")
        ok = ok and identical
    return ok


def check_gos(ctx: Context) -> bool:
    ok = True
    for in_path, out_path in CORPORA["gos"].io:
        if not in_path.exists() or not out_path.exists():
            print(f"  SKIP {out_path.name} (input or enriched output missing)")
            continue
        docs = sents = spk = 0
        with open(in_path, encoding="utf-8") as fin, open(out_path, encoding="utf-8") as fout:
            mismatch_line = 0
            in_iter = iter(fin)
            for ln, line in enumerate(fout, 1):
                if line.startswith("# newdoc id = "):
                    docs += 1
                elif line.startswith("# sent_id = "):
                    sents += 1
                elif line.startswith("# speaker_id = "):
                    spk += 1
                if INSERTED.match(line):
                    continue  # an inserted line -> should not be in the input
                orig = next(in_iter, None)
                if orig != line:
                    mismatch_line = ln
                    break
            leftover = next(in_iter, None)
        additive = mismatch_line == 0 and leftover is None
        print(f"  {'OK  ' if additive else 'FAIL'} {out_path.name}: "
              f"{'enriched minus inserted lines == input (purely additive)' if additive else f'mismatch near enriched line {mismatch_line}'}")
        print(f"       coverage: {docs} docs, {sents} sentences, {spk} with speaker "
              f"({sents - spk} unresolved)")
        ok = ok and additive
    return ok


def main() -> int:
    ctx = _context()
    print("SST parity:")
    sst_ok = check_sst(ctx)
    print("GOS non-destructiveness:")
    gos_ok = check_gos(ctx)
    print()
    if sst_ok and gos_ok:
        print("ALL CHECKS PASSED")
        return 0
    print("SOME CHECKS FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
