"""
Prepare and refresh per-split description translation files.

For each SST split, this script writes:
  - docs/working/descriptions/descriptions-<split>-slovenian.txt
  - docs/working/descriptions/descriptions-<split>-english.txt
  - docs/working/descriptions/descriptions-<split>-for-translation.tsv

The Slovenian file is always regenerated from GOS metadata in the exact doc order
used by the split's CoNLL-U file. If an English file already exists and has the
same number of lines, its contents are used to refresh the TSV. Otherwise, the
script seeds the TSV from existing translations (if any), the legacy dev
DESCRIPTION dict, or leaves the English column blank.
"""

import csv
import re
from pathlib import Path

from enrich_conllu import DESCRIPTION


ROOT = Path(__file__).resolve().parent.parent
WORKING_DIR = ROOT / "docs" / "working" / "descriptions"
SST_DIR = ROOT / "src" / "sst"
GOS_SPEECHES = ROOT / "src" / "gos" / "Gos-speeches.tsv"
SPLITS = ("train", "dev", "test")


def ordered_doc_ids(conllu_path: Path) -> list[str]:
    text = conllu_path.read_text(encoding="utf-8")
    return list(dict.fromkeys(re.findall(r"^# newdoc id = (.+)$", text, re.M)))


def load_titles(path: Path) -> dict[str, str]:
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        return {row["TEXT-ID"].strip(): row["TITLE"].strip() for row in reader}


def load_existing_tsv(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}

    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        return {
            row["doc_id"].strip(): (row.get("english") or "").strip()
            for row in reader
        }


def load_english_lines(path: Path) -> list[str] | None:
    if not path.exists():
        return None

    return path.read_text(encoding="utf-8").splitlines()


def seed_english(doc_ids: list[str], titles: dict[str, str], existing: dict[str, str]) -> list[str]:
    seeded = []
    for doc_id in doc_ids:
        english = existing.get(doc_id, "").strip()
        if english:
            seeded.append(english)
            continue

        if doc_id in DESCRIPTION:
            seeded.append(DESCRIPTION[doc_id])
            continue

        title = titles[doc_id]
        seeded.append(title if title == doc_id else "")
    return seeded


def expand_english_lines(doc_ids: list[str], titles: dict[str, str], lines: list[str], path: Path) -> list[str]:
    if len(lines) == len(doc_ids):
        return lines

    titled_doc_ids = [doc_id for doc_id in doc_ids if titles[doc_id] != doc_id]
    if len(lines) == len(titled_doc_ids):
        expanded = []
        idx = 0
        for doc_id in doc_ids:
            if titles[doc_id] == doc_id:
                expanded.append(doc_id)
            else:
                expanded.append(lines[idx])
                idx += 1
        return expanded

    if any(line.strip() for line in lines):
        raise ValueError(
            f"{path} has {len(lines)} lines, expected either {len(doc_ids)} full rows "
            f"or {len(titled_doc_ids)} rows without doc-id-only entries."
        )

    return []


def write_lines(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_tsv(path: Path, doc_ids: list[str], titles: dict[str, str], english_lines: list[str]) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(["doc_id", "slovenian", "english"])
        for doc_id, english in zip(doc_ids, english_lines):
            writer.writerow([doc_id, titles[doc_id], english])


def main() -> None:
    WORKING_DIR.mkdir(parents=True, exist_ok=True)
    titles = load_titles(GOS_SPEECHES)

    for split in SPLITS:
        conllu_path = SST_DIR / f"sl_sst-ud-{split}.conllu"
        sl_path = WORKING_DIR / f"descriptions-{split}-slovenian.txt"
        en_path = WORKING_DIR / f"descriptions-{split}-english.txt"
        tsv_path = WORKING_DIR / f"descriptions-{split}-for-translation.tsv"

        doc_ids = ordered_doc_ids(conllu_path)
        existing = load_existing_tsv(tsv_path)
        raw_english_lines = load_english_lines(en_path)
        if raw_english_lines is None:
            english_lines = seed_english(doc_ids, titles, existing)
        else:
            english_lines = expand_english_lines(doc_ids, titles, raw_english_lines, en_path)
            if not english_lines:
                english_lines = seed_english(doc_ids, titles, existing)

        write_lines(sl_path, [titles[doc_id] for doc_id in doc_ids])
        write_lines(en_path, english_lines)
        write_tsv(tsv_path, doc_ids, titles, english_lines)

        filled = sum(1 for line in english_lines if line.strip())
        print(f"{split}: wrote {len(doc_ids)} rows, {filled} English descriptions filled")


if __name__ == "__main__":
    main()
