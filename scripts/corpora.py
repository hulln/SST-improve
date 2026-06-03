"""
Corpus registry for the enrichment pipeline.

Every corpus is enriched from the same shared GOS metadata under ``metadata/gos/``;
a corpus differs only in which CoNLL-U files it reads and writes. To add a future
corpus, append an entry to ``CORPORA`` with its input -> output file pairs.

The enrichment engine itself is corpus-agnostic: it auto-detects whether the input
already carries ``# newdoc id`` / ``# speaker_id`` comments (as SST does) or whether
they must be reconstructed from sentence ids, ``# newpar id`` and MISC
``OriginalUtteranceId`` (as the raw GOS treebank requires).
"""

from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
METADATA = ROOT / "metadata" / "gos"
SPEAKERS_TSV = METADATA / "Gos-speakers.tsv"
SPEECHES_TSV = METADATA / "Gos-speeches.tsv"
DESCRIPTIONS_TSV = METADATA / "descriptions-en.tsv"
UTTERANCE_SPEAKER_TSV = METADATA / "utterance-speaker.tsv"


@dataclass(frozen=True)
class Corpus:
    name: str
    io: tuple[tuple[Path, Path], ...]  # (input, output) pairs


def _sst() -> Corpus:
    d = ROOT / "corpora" / "sst"
    io = tuple(
        (d / f"sl_sst-ud-{split}.conllu", d / f"sl_sst-ud-{split}-enriched.conllu")
        for split in ("train", "dev", "test")
    )
    return Corpus("sst", io)


def _gos() -> Corpus:
    d = ROOT / "corpora" / "gos"
    return Corpus("gos", ((d / "gos.conllu", d / "gos-enriched.conllu"),))


CORPORA: dict[str, Corpus] = {c.name: c for c in (_sst(), _gos())}
