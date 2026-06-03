"""
Build the utterance -> speaker map from the GOS TEI archive.

The GOS UD CoNLL-U files identify each utterance (``# newpar id`` for Gos/GosVL,
``OriginalUtteranceId=`` in MISC for Artur) but never the speaker. The TEI source
maps every utterance to its speaker via ``<u xml:id="..." who="#PRS-ID">``.

This one-off build step extracts that mapping once into a small TSV so the
enrichment engine does not need to open the 60 MB TEI archive on every run.

Output: ``metadata/gos/utterance-speaker.tsv`` with columns ``utterance_id``,
``speaker_id`` (one row per utterance that has a ``who`` attribute).
"""

import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEI_ZIP = ROOT / "metadata" / "gos" / "Gos.TEI.zip"
OUT_TSV = ROOT / "metadata" / "gos" / "utterance-speaker.tsv"

# Each <u> opening tag; attributes parsed individually so order does not matter.
U_TAG = re.compile(rb"<u\b[^>]*>")
XMLID = re.compile(rb'xml:id="([^"]+)"')
WHO = re.compile(rb'who="#?([^"]+)"')


def build(tei_zip: Path, out_tsv: Path) -> None:
    if not tei_zip.exists():
        raise FileNotFoundError(f"Missing TEI archive: {tei_zip}")

    rows: list[tuple[str, str]] = []
    n_utts = 0
    n_no_who = 0

    with zipfile.ZipFile(tei_zip) as zf:
        for name in zf.namelist():
            if not name.endswith(".xml") or "/schema/" in name:
                continue
            data = zf.read(name)
            for tag in U_TAG.finditer(data):
                chunk = tag.group(0)
                m_id = XMLID.search(chunk)
                if not m_id:
                    continue
                n_utts += 1
                uid = m_id.group(1).decode("utf-8")
                m_who = WHO.search(chunk)
                if not m_who:
                    n_no_who += 1
                    continue
                rows.append((uid, m_who.group(1).decode("utf-8")))

    rows.sort()
    with open(out_tsv, "w", encoding="utf-8") as f:
        f.write("utterance_id\tspeaker_id\n")
        for uid, spk in rows:
            f.write(f"{uid}\t{spk}\n")

    print(f"Utterances total:        {n_utts}", file=sys.stderr)
    print(f"  with who (written):    {len(rows)}", file=sys.stderr)
    print(f"  without who (skipped): {n_no_who}", file=sys.stderr)
    print(f"Wrote {out_tsv}", file=sys.stderr)


if __name__ == "__main__":
    build(TEI_ZIP, OUT_TSV)
