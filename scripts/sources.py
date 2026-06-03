"""
Loaders for the shared GOS metadata used to enrich CoNLL-U files.

All four sources live under ``metadata/gos/`` and are shared by every corpus:
  - ``Gos-speakers.tsv``     -> per-speaker attributes (gender/age/education/residence)
  - ``Gos-speeches.tsv``     -> per-document event attributes (type/domain/channel/description)
  - ``descriptions-en.tsv``  -> English event descriptions (built by build_descriptions.py)
  - ``utterance-speaker.tsv``-> utterance id -> speaker id (built by build_utterance_speaker_map.py)
"""

import csv
from pathlib import Path

import translations as T


def load_speakers(path: Path) -> dict[str, dict[str, str]]:
    """PRS-ID -> {speaker_gender, speaker_age, speaker_education, speaker_residence}."""
    result: dict[str, dict[str, str]] = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            pid = row["PRS-ID"].strip()
            if pid in ("-", "audience", "all", ""):
                continue
            result[pid] = {
                "speaker_gender": T.SEX.get(row["SEX"].strip(), row["SEX"].strip()),
                "speaker_age": T.AGE.get(row["AGE"].strip(), row["AGE"].strip()),
                "speaker_education": T.EDUCATION.get(row["EDUCATION"].strip(), row["EDUCATION"].strip()),
                "speaker_residence": T.translate_region(row["PERM-RESD"].strip()),
            }
    return result


def load_descriptions(path: Path) -> dict[str, str]:
    """doc_id -> English event description (only rows with a non-empty translation)."""
    if not path.exists():
        return {}
    result: dict[str, str] = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            en = (row.get("english") or "").strip()
            if en:
                result[row["doc_id"].strip()] = en
    return result


def load_speeches(path: Path, descriptions: dict[str, str] | None = None) -> dict[str, dict[str, str]]:
    """TEXT-ID -> {event_type, event_domain, event_channel, event_description}."""
    descriptions = descriptions or {}
    result: dict[str, dict[str, str]] = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            tid = row["TEXT-ID"].strip()
            result[tid] = {
                "event_type": T.TYPE.get(row["TYPE"].strip(), row["TYPE"].strip()),
                "event_domain": T.translate_domain(row["DOMAIN"].strip()),
                "event_channel": T.CHANNEL.get(row["CHANNEL"].strip(), row["CHANNEL"].strip()),
                "event_description": descriptions.get(tid) or row["TITLE"].strip(),
            }
    return result


def load_utterance_speaker(path: Path) -> dict[str, str]:
    """utterance_id -> speaker_id (PRS-ID)."""
    if not path.exists():
        raise FileNotFoundError(
            f"Missing {path}. Run: python scripts/build_utterance_speaker_map.py"
        )
    result: dict[str, str] = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            result[row["utterance_id"].strip()] = row["speaker_id"].strip()
    return result
