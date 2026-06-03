"""
Report Artur sentences that should not get a singular sentence-level speaker.

This is an audit helper. It does not change the corpus. It writes:

  docs/working/artur-speaker-edge-cases/speaker-edge-case-sentences.tsv
  docs/working/artur-speaker-edge-cases/speaker-edge-case-sentences.conllu
  docs/working/artur-speaker-edge-cases/README.md

The mini CoNLL-U keeps the original sentences and adds custom explanatory
comments with all speaker IDs and token ranges.
"""

from __future__ import annotations

import csv
import re
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
GOS = ROOT / "corpora" / "gos" / "gos.conllu"
OUT_DIR = ROOT / "docs" / "working" / "artur-speaker-edge-cases"
UTTERANCE_SPEAKER = ROOT / "metadata" / "gos" / "utterance-speaker.tsv"
SPEECHES = ROOT / "metadata" / "gos" / "Gos-speeches.tsv"
SPEAKERS = ROOT / "metadata" / "gos" / "Gos-speakers.tsv"
TEI_ZIP = ROOT / "metadata" / "gos" / "Gos.TEI.zip"

UTT_RE = re.compile(r"OriginalUtteranceId=([^|\s]+)")
NS = {"tei": "http://www.tei-c.org/ns/1.0"}
XML_ID = "{http://www.w3.org/XML/1998/namespace}id"


@dataclass
class TokenInfo:
    token_id: str
    form: str
    utterance_id: str | None
    speaker_id: str | None


@dataclass
class MixedCase:
    start_line: int
    end_line: int
    doc_id: str
    subcorpus: str
    sent_id: str
    comments: list[str]
    tokens: list[str]
    token_info: list[TokenInfo]
    utterance_counts: Counter[str]
    speaker_counts: Counter[str]
    unresolved_utterance_counts: Counter[str]


def load_utterance_speakers() -> dict[str, str]:
    with open(UTTERANCE_SPEAKER, encoding="utf-8") as f:
        return {
            row["utterance_id"].strip(): row["speaker_id"].strip()
            for row in csv.DictReader(f, delimiter="\t")
        }


def load_speeches() -> dict[str, dict[str, str]]:
    with open(SPEECHES, encoding="utf-8") as f:
        return {
            row["TEXT-ID"].strip(): row
            for row in csv.DictReader(f, delimiter="\t")
        }


def load_speakers() -> dict[str, dict[str, str]]:
    with open(SPEAKERS, encoding="utf-8") as f:
        return {
            row["PRS-ID"].strip(): row
            for row in csv.DictReader(f, delimiter="\t")
            if row["PRS-ID"].strip() not in {"", "-", "audience", "all"}
        }


def comment_value(comments: list[str], key: str) -> str | None:
    prefix = f"# {key} = "
    for line in comments:
        if line.startswith(prefix):
            return line[len(prefix):].rstrip("\n")
    return None


def original_utterance(token_line: str) -> str | None:
    match = UTT_RE.search(token_line)
    return match.group(1) if match else None


def token_infos(tokens: list[str], utt2spk: dict[str, str]) -> list[TokenInfo]:
    result: list[TokenInfo] = []
    for line in tokens:
        fields = line.rstrip("\n").split("\t")
        if len(fields) < 2:
            continue
        uid = original_utterance(line)
        result.append(
            TokenInfo(
                token_id=fields[0],
                form=fields[1],
                utterance_id=uid,
                speaker_id=utt2spk.get(uid) if uid else None,
            )
        )
    return result


def parse_mixed_cases(
    utt2spk: dict[str, str],
    speeches: dict[str, dict[str, str]],
) -> list[MixedCase]:
    cases: list[MixedCase] = []
    comments: list[str] = []
    tokens: list[str] = []
    start_line = 1

    def flush(end_line: int) -> None:
        if not comments and not tokens:
            return
        sent_id = comment_value(comments, "sent_id")
        if not sent_id or not sent_id.startswith("Artur"):
            return
        doc_id = sent_id.split(".", 1)[0]
        infos = token_infos(tokens, utt2spk)
        utterance_counts: Counter[str] = Counter()
        speaker_counts: Counter[str] = Counter()
        unresolved_utterance_counts: Counter[str] = Counter()
        for info in infos:
            if info.utterance_id:
                utterance_counts[info.utterance_id] += 1
            if info.speaker_id:
                speaker_counts[info.speaker_id] += 1
            elif info.utterance_id:
                unresolved_utterance_counts[info.utterance_id] += 1
        has_multiple_speakers = len(speaker_counts) > 1
        has_known_plus_unresolved = len(speaker_counts) == 1 and bool(unresolved_utterance_counts)
        if not (has_multiple_speakers or has_known_plus_unresolved):
            return
        cases.append(
            MixedCase(
                start_line=start_line,
                end_line=end_line,
                doc_id=doc_id,
                subcorpus=speeches.get(doc_id, {}).get("SUBCORPUS", ""),
                sent_id=sent_id,
                comments=list(comments),
                tokens=list(tokens),
                token_info=infos,
                utterance_counts=utterance_counts,
                speaker_counts=speaker_counts,
                unresolved_utterance_counts=unresolved_utterance_counts,
            )
        )

    with open(GOS, encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if not line.strip():
                flush(line_no)
                comments.clear()
                tokens.clear()
                start_line = line_no + 1
            elif line.startswith("#"):
                comments.append(line)
            else:
                tokens.append(line)
        flush(line_no)

    return cases


def range_label(start: str, end: str) -> str:
    return start if start == end else f"{start}-{end}"


def utterance_doc_id(utterance_id: str) -> str:
    return utterance_id.rsplit(".u", 1)[0]


def speaker_segments(case: MixedCase) -> list[tuple[str, str | None, str | None]]:
    segments: list[tuple[str, str | None, str | None]] = []
    if not case.token_info:
        return segments
    start = case.token_info[0].token_id
    prev = case.token_info[0]
    for info in case.token_info[1:]:
        if info.speaker_id == prev.speaker_id and info.utterance_id == prev.utterance_id:
            prev = info
            continue
        segments.append((range_label(start, prev.token_id), prev.speaker_id, prev.utterance_id))
        start = info.token_id
        prev = info
    segments.append((range_label(start, prev.token_id), prev.speaker_id, prev.utterance_id))
    return segments


def conllu_text(case: MixedCase) -> str:
    pieces: list[str] = []
    for info in case.token_info:
        pieces.append(info.form)
    return " ".join(pieces)


def case_type(case: MixedCase) -> str:
    if len(case.speaker_counts) > 1:
        return "multiple_known_speakers"
    if case.speaker_counts and case.unresolved_utterance_counts:
        return "known_plus_unresolved_utterance"
    return "other"


def parse_tei_times(cases: list[MixedCase], speeches: dict[str, dict[str, str]]) -> dict[str, str]:
    needed_utts = {uid for case in cases for uid in case.utterance_counts}
    needed_docs = {utterance_doc_id(uid) for uid in needed_utts}
    result: dict[str, str] = {}

    with zipfile.ZipFile(TEI_ZIP) as zf:
        names = set(zf.namelist())
        for doc_id in sorted(needed_docs):
            subcorpus = speeches.get(doc_id, {}).get("SUBCORPUS")
            name = f"Gos.TEI/{subcorpus}/{doc_id}.xml"
            if name not in names:
                continue
            root = ET.fromstring(zf.read(name))
            times: dict[str, str] = {}
            for when in root.findall(".//tei:when", NS):
                xml_id = when.attrib.get(XML_ID)
                interval = when.attrib.get("interval")
                if xml_id:
                    times[xml_id] = interval or "0.000"
            for utt in root.findall(".//tei:u", NS):
                uid = utt.attrib.get(XML_ID)
                if uid not in needed_utts:
                    continue
                start = utt.attrib.get("start", "").lstrip("#")
                end = utt.attrib.get("end", "").lstrip("#")
                trans = utt.attrib.get("trans", "")
                who = utt.attrib.get("who", "").lstrip("#")
                start_time = times.get(start, "?")
                end_time = times.get(end, "?")
                label = f"{uid}:{who}:{start_time}-{end_time}"
                if trans:
                    label += f":trans={trans}"
                result[uid] = label
    return result


def speaker_details(speaker_id: str, speakers: dict[str, dict[str, str]]) -> str:
    row = speakers.get(speaker_id)
    if not row:
        return speaker_id
    return (
        f"{speaker_id}"
        f"(SEX={row['SEX']}, AGE={row['AGE']},"
        f" EDUCATION={row['EDUCATION']}, PERM-RESD={row['PERM-RESD']})"
    )


def write_tsv(
    cases: list[MixedCase],
    speakers: dict[str, dict[str, str]],
    tei_times: dict[str, str],
) -> None:
    path = OUT_DIR / "speaker-edge-case-sentences.tsv"
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")
        writer.writerow(
            [
                "subcorpus",
                "case_type",
                "doc_id",
                "sent_id",
                "source_start_line",
                "source_end_line",
                "token_count",
                "speaker_count",
                "top_speaker_share",
                "has_strict_majority",
                "speaker_token_counts",
                "speaker_details",
                "utterance_token_counts",
                "unresolved_utterance_token_counts",
                "utterance_doc_ids",
                "crosses_utterance_doc",
                "speaker_segments",
                "tei_utterance_times",
                "recommendation",
                "text",
            ]
        )
        for case in cases:
            total = len(case.token_info)
            top = case.speaker_counts.most_common(1)[0][1]
            segment_text = "; ".join(
                f"{rng}:{speaker or '_'}({utt or '_'})"
                for rng, speaker, utt in speaker_segments(case)
            )
            utterance_docs = sorted({utterance_doc_id(utt) for utt in case.utterance_counts})
            writer.writerow(
                [
                    case.subcorpus,
                    case_type(case),
                    case.doc_id,
                    case.sent_id,
                    case.start_line,
                    case.end_line,
                    len(case.token_info),
                    len(case.speaker_counts),
                    f"{top / total:.3f}" if total else "",
                    "yes" if top * 2 > total else "no",
                    "; ".join(f"{spk}:{n}" for spk, n in case.speaker_counts.most_common()),
                    "; ".join(
                        speaker_details(spk, speakers)
                        for spk in case.speaker_counts
                    ),
                    "; ".join(f"{utt}:{n}" for utt, n in case.utterance_counts.most_common()),
                    "; ".join(f"{utt}:{n}" for utt, n in case.unresolved_utterance_counts.most_common()),
                    "; ".join(utterance_docs),
                    "yes" if any(doc != case.doc_id for doc in utterance_docs) else "no",
                    segment_text,
                    "; ".join(tei_times.get(utt, utt) for utt in case.utterance_counts),
                    "omit sentence-level speaker_id; use suggested_speaker_segments",
                    conllu_text(case),
                ]
            )


def write_mini_conllu(cases: list[MixedCase]) -> None:
    path = OUT_DIR / "speaker-edge-case-sentences.conllu"
    with open(path, "w", encoding="utf-8") as f:
        for case in cases:
            counts = "; ".join(f"{spk}:{n}" for spk, n in case.speaker_counts.most_common())
            segments = "; ".join(
                f"{rng}:{speaker or '_'}({utt or '_'})"
                for rng, speaker, utt in speaker_segments(case)
            )
            utterance_speakers = "; ".join(
                f"{utt}:{next((i.speaker_id for i in case.token_info if i.utterance_id == utt), '_')}:{n}"
                for utt, n in case.utterance_counts.most_common()
            )
            inserted = False
            for line in case.comments:
                f.write(line)
                if line.startswith("# sent_id = ") and not inserted:
                    f.write("# mixed_speaker = yes\n")
                    f.write("# recommended_speaker_id = _\n")
                    f.write("# speaker_edge_case = " + case_type(case) + "\n")
                    f.write("# suggested_speaker_ids = " + ", ".join(case.speaker_counts) + "\n")
                    f.write("# suggested_speaker_token_counts = " + counts + "\n")
                    f.write("# suggested_utterance_speakers = " + utterance_speakers + "\n")
                    f.write("# suggested_speaker_segments = " + segments + "\n")
                    f.write("# mixed_text = " + conllu_text(case) + "\n")
                    f.write(
                        "# note = This UD sentence crosses original utterance/speaker boundaries; "
                        "do not emit one unqualified sentence-level speaker_id.\n"
                    )
                    inserted = True
            for line in case.tokens:
                f.write(line)
            f.write("\n")


def write_readme(cases: list[MixedCase], tei_times: dict[str, str]) -> None:
    path = OUT_DIR / "README.md"
    affected = len(cases)
    mixed = sum(1 for case in cases if len(case.speaker_counts) > 1)
    known_unresolved = sum(1 for case in cases if case_type(case) == "known_plus_unresolved_utterance")
    no_majority = sum(
        1
        for case in cases
        if case.speaker_counts.most_common(1)[0][1] * 2 <= len(case.token_info)
    )
    cross_doc = sum(
        1
        for case in cases
        if any(utterance_doc_id(utt) != case.doc_id for utt in case.utterance_counts)
    )
    overlap = sum(
        1
        for case in cases
        if any("trans=overlap" in tei_times.get(utt, "") for utt in case.utterance_counts)
    )
    by_sub = Counter(case.subcorpus for case in cases)
    example = cases[0]
    path.write_text(
        "\n".join(
            [
                "# Artur sentence-level speaker edge cases",
                "",
                "This directory lists Artur UD sentences that should not receive one",
                "singular sentence-level speaker ID.",
                "",
                f"- Affected sentences: {affected}",
                f"- Sentences with multiple known TEI speakers: {mixed}",
                f"- Sentences with one known speaker plus unresolved/no-`who` utterance tokens: {known_unresolved}",
                f"- Affected sentences with no strict majority speaker: {no_majority}",
                f"- Affected sentences with at least one TEI `trans=\"overlap\"` utterance: {overlap}",
                f"- Affected sentences crossing an utterance document boundary: {cross_doc}",
                "- By subcorpus: "
                + ", ".join(f"{sub}={count}" for sub, count in sorted(by_sub.items())),
                "",
                "Why this happens: Artur was resegmented into UD sentences. A UD sentence",
                "is not always the same thing as an original speech turn. Sometimes a UD",
                "sentence spans adjacent utterances, and sometimes the TEI marks the",
                "utterances as overlapping speech. Two additional sentences combine",
                "one known speaker with tokens from an utterance that has no TEI `who=`.",
                "",
                "Overlap status comes from TEI `trans=\"overlap\"`, not from CoNLL-U.",
                "The CoNLL-U rows only preserve `OriginalUtteranceId`; speaker and",
                "overlap metadata are recovered through TEI.",
                "",
                "Recommended policy: do not emit a singular `# speaker_id` for these",
                "sentences. The mini CoNLL-U uses custom comments instead:",
                "",
                "- `# recommended_speaker_id = _`",
                "- `# suggested_speaker_ids = ...`",
                "- `# suggested_speaker_segments = token-range:speaker(utterance); ...`",
                "",
                "Files:",
                "",
                "- `speaker-edge-case-sentences.tsv`: one row per affected sentence.",
                "- `speaker-edge-case-sentences.conllu`: mini CoNLL-U with only affected",
                "  sentences and suggested speaker-segment comments.",
                "",
                "Example:",
                "",
                f"- `{example.sent_id}` at source line {example.start_line}",
                "- Speaker token counts: "
                + "; ".join(f"{spk}:{n}" for spk, n in example.speaker_counts.most_common()),
                "- Segments: "
                + "; ".join(
                    f"{rng}:{speaker or '_'}({utt or '_'})"
                    for rng, speaker, utt in speaker_segments(example)
                ),
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    utt2spk = load_utterance_speakers()
    speeches = load_speeches()
    speakers = load_speakers()
    cases = parse_mixed_cases(utt2spk, speeches)
    tei_times = parse_tei_times(cases, speeches)
    write_tsv(cases, speakers, tei_times)
    write_mini_conllu(cases)
    write_readme(cases, tei_times)
    print(f"Wrote {len(cases)} Artur speaker edge-case sentences to {OUT_DIR}")


if __name__ == "__main__":
    main()
