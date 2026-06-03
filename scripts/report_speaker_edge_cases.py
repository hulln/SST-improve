"""
Report GOS sentences that do not get a singular sentence-level speaker.

This is an audit helper. It does not change the corpus. It writes:

  docs/working/speaker-edge-cases/speaker-edge-case-sentences.tsv
  docs/working/speaker-edge-cases/speaker-edge-case-sentences.conllu
  docs/working/speaker-edge-cases/README.md

It reproduces the exact blanking decision of scripts/enrich.py and labels every
affected sentence with its case type:

  - multiple_known_speakers          : the UD sentence spans 2+ known speakers
  - known_plus_unresolved_utterance  : one known speaker + an utterance with no `who`
  - unknown_speaker                  : no `who` at all -> speaker identity unknown

The first two are Artur-only (Artur was resegmented, so a UD sentence can cross
original utterance/speaker boundaries). The third occurs in any subcorpus
(Gos/GosVL/Artur) wherever the source TEI utterance has no `who=` attribute.

The mini CoNLL-U keeps the original sentences and adds custom explanatory
comments. The enriched corpus itself is left unchanged (it simply omits the
speaker block for these sentences).
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
OUT_DIR = ROOT / "docs" / "working" / "speaker-edge-cases"
UTTERANCE_SPEAKER = ROOT / "metadata" / "gos" / "utterance-speaker.tsv"
SPEECHES = ROOT / "metadata" / "gos" / "Gos-speeches.tsv"
SPEAKERS = ROOT / "metadata" / "gos" / "Gos-speakers.tsv"
TEI_ZIP = ROOT / "metadata" / "gos" / "Gos.TEI.zip"

UTT_RE = re.compile(r"OriginalUtteranceId=([^|\s]+)")
NS = {"tei": "http://www.tei-c.org/ns/1.0"}
XML_ID = "{http://www.w3.org/XML/1998/namespace}id"

CASE_TYPES = (
    "multiple_known_speakers",
    "known_plus_unresolved_utterance",
    "unknown_speaker",
)


@dataclass
class TokenInfo:
    token_id: str
    form: str
    utterance_id: str | None
    speaker_id: str | None


@dataclass
class EdgeCase:
    start_line: int
    end_line: int
    doc_id: str
    subcorpus: str
    sent_id: str
    case_type: str
    fallback_utterance: str | None  # carried "# newpar id" for Gos/GosVL sentences
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


def classify(speaker_counts: Counter[str], unresolved: bool) -> str | None:
    """Return the edge-case type, or None if the sentence resolves cleanly.

    Mirrors scripts/enrich.py speaker_from_sentence: a sentence keeps a single
    speaker only when exactly one known speaker is present and nothing is
    unresolved. Everything else is an edge case.
    """
    if len(speaker_counts) > 1:
        return "multiple_known_speakers"
    if len(speaker_counts) == 1:
        return "known_plus_unresolved_utterance" if unresolved else None
    return "unknown_speaker"  # zero known speakers


def parse_cases(
    utt2spk: dict[str, str],
    speeches: dict[str, dict[str, str]],
) -> list[EdgeCase]:
    cases: list[EdgeCase] = []
    comments: list[str] = []
    tokens: list[str] = []
    start_line = 1
    current_newpar: str | None = None  # carried across blocks, like enrich.py

    def flush(end_line: int) -> None:
        nonlocal current_newpar
        if not comments and not tokens:
            return
        # Update the carried newpar first (it may live in this very block).
        newpar = comment_value(comments, "newpar id")
        if newpar is not None:
            current_newpar = newpar

        sent_id = comment_value(comments, "sent_id")
        if not sent_id:
            return
        # A pre-existing speaker_id in the input is authoritative; not an edge case.
        if comment_value(comments, "speaker_id") is not None:
            return

        doc_id = sent_id.split(".", 1)[0]
        infos = token_infos(tokens, utt2spk)
        has_token_utts = any(info.utterance_id for info in infos)

        fallback_utterance: str | None = None
        if not has_token_utts:
            # Gos/GosVL: the sentence's utterance is the carried "# newpar id".
            fallback_utterance = current_newpar
            spk = utt2spk.get(fallback_utterance) if fallback_utterance else None
            infos = [
                TokenInfo(i.token_id, i.form, fallback_utterance, spk) for i in infos
            ]

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

        unresolved = bool(unresolved_utterance_counts)
        ctype = classify(speaker_counts, unresolved)
        if ctype is None:
            return  # resolves to a single speaker -> not an edge case

        cases.append(
            EdgeCase(
                start_line=start_line,
                end_line=end_line,
                doc_id=doc_id,
                subcorpus=speeches.get(doc_id, {}).get("SUBCORPUS", ""),
                sent_id=sent_id,
                case_type=ctype,
                fallback_utterance=fallback_utterance,
                comments=list(comments),
                tokens=list(tokens),
                token_info=infos,
                utterance_counts=utterance_counts,
                speaker_counts=speaker_counts,
                unresolved_utterance_counts=unresolved_utterance_counts,
            )
        )

    with open(GOS, encoding="utf-8") as f:
        line_no = 0
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


def speaker_segments(case: EdgeCase) -> list[tuple[str, str | None, str | None]]:
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


def conllu_text(case: EdgeCase) -> str:
    return " ".join(info.form for info in case.token_info)


def parse_tei_metadata(
    cases: list[EdgeCase], speeches: dict[str, dict[str, str]]
) -> dict[str, str]:
    """For each relevant utterance, recover `uid:who:start-end[:trans=...]` from TEI.

    For unknown_speaker cases `who` comes back empty, which independently
    confirms the source really has no speaker for that utterance.
    """
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
                label = f"{uid}:who={who or '(none)'}:{start_time}-{end_time}"
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


def recommendation_for(ctype: str) -> str:
    if ctype == "unknown_speaker":
        return "omit sentence-level speaker_id; speaker identity unavailable (no TEI who=)"
    return "omit sentence-level speaker_id; see suggested_speaker_segments"


def note_for(ctype: str) -> str:
    if ctype == "multiple_known_speakers":
        return ("This UD sentence spans multiple known speakers; "
                "no single sentence-level speaker_id is emitted.")
    if ctype == "known_plus_unresolved_utterance":
        return ("This UD sentence mixes one known speaker with an utterance that has "
                "no TEI who=; no single sentence-level speaker_id is emitted.")
    return ("The utterance(s) for this sentence have no TEI who=; the speaker identity "
            "is unknown, so no sentence-level speaker_id is emitted.")


def write_tsv(
    cases: list[EdgeCase],
    speakers: dict[str, dict[str, str]],
    tei_meta: dict[str, str],
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
                "carried_newpar_id",
                "speaker_token_counts",
                "speaker_details",
                "utterance_token_counts",
                "unresolved_utterance_token_counts",
                "utterance_doc_ids",
                "crosses_utterance_doc",
                "speaker_segments",
                "tei_utterances",
                "recommendation",
                "text",
            ]
        )
        for case in cases:
            total = len(case.token_info)
            top = case.speaker_counts.most_common(1)[0][1] if case.speaker_counts else 0
            segment_text = "; ".join(
                f"{rng}:{speaker or '_'}({utt or '_'})"
                for rng, speaker, utt in speaker_segments(case)
            )
            utterance_docs = sorted({utterance_doc_id(utt) for utt in case.utterance_counts})
            writer.writerow(
                [
                    case.subcorpus,
                    case.case_type,
                    case.doc_id,
                    case.sent_id,
                    case.start_line,
                    case.end_line,
                    total,
                    len(case.speaker_counts),
                    f"{top / total:.3f}" if total and case.speaker_counts else "",
                    "yes" if case.speaker_counts and top * 2 > total else "no",
                    case.fallback_utterance or "",
                    "; ".join(f"{spk}:{n}" for spk, n in case.speaker_counts.most_common()),
                    "; ".join(speaker_details(spk, speakers) for spk in case.speaker_counts),
                    "; ".join(f"{utt}:{n}" for utt, n in case.utterance_counts.most_common()),
                    "; ".join(f"{utt}:{n}" for utt, n in case.unresolved_utterance_counts.most_common()),
                    "; ".join(utterance_docs),
                    "yes" if any(doc != case.doc_id for doc in utterance_docs) else "no",
                    segment_text,
                    "; ".join(tei_meta.get(utt, utt) for utt in case.utterance_counts),
                    recommendation_for(case.case_type),
                    conllu_text(case),
                ]
            )


def write_mini_conllu(cases: list[EdgeCase]) -> None:
    path = OUT_DIR / "speaker-edge-case-sentences.conllu"
    with open(path, "w", encoding="utf-8") as f:
        for case in cases:
            counts = "; ".join(f"{spk}:{n}" for spk, n in case.speaker_counts.most_common())
            segments = "; ".join(
                f"{rng}:{speaker or '_'}({utt or '_'})"
                for rng, speaker, utt in speaker_segments(case)
            )
            utterance_speakers = "; ".join(
                f"{utt}:{next((i.speaker_id for i in case.token_info if i.utterance_id == utt), '_') or '_'}:{n}"
                for utt, n in case.utterance_counts.most_common()
            )
            unresolved = "; ".join(
                f"{utt}:{n}" for utt, n in case.unresolved_utterance_counts.most_common()
            )
            inserted = False
            for line in case.comments:
                f.write(line)
                if line.startswith("# sent_id = ") and not inserted:
                    f.write(f"# speaker_edge_case = {case.case_type}\n")
                    f.write("# recommended_speaker_id = _\n")
                    if case.fallback_utterance:
                        f.write(f"# carried_newpar_id = {case.fallback_utterance}\n")
                    if case.speaker_counts:
                        f.write("# suggested_speaker_ids = " + ", ".join(case.speaker_counts) + "\n")
                        f.write("# suggested_speaker_token_counts = " + counts + "\n")
                        f.write("# suggested_utterance_speakers = " + utterance_speakers + "\n")
                        f.write("# suggested_speaker_segments = " + segments + "\n")
                    if unresolved:
                        f.write("# unresolved_utterances = " + unresolved + "\n")
                    f.write("# edge_case_text = " + conllu_text(case) + "\n")
                    f.write("# note = " + note_for(case.case_type) + "\n")
                    inserted = True
            for line in case.tokens:
                f.write(line)
            f.write("\n")


def _example(cases: list[EdgeCase], ctype: str) -> EdgeCase | None:
    return next((c for c in cases if c.case_type == ctype), None)


def write_readme(cases: list[EdgeCase]) -> None:
    path = OUT_DIR / "README.md"
    by_type = Counter(c.case_type for c in cases)
    by_sub = Counter(c.subcorpus for c in cases)
    by_type_sub = Counter((c.case_type, c.subcorpus) for c in cases)

    lines: list[str] = [
        "# Speaker-level edge cases (no single sentence-level speaker)",
        "",
        "GOS UD sentences for which the enrichment pipeline emits **no** singular",
        "`# speaker_id`. The enriched corpus is left as-is (the speaker block is simply",
        "omitted); this folder documents *why* each one is blank, by case.",
        "",
        f"- Affected sentences: {len(cases)}",
        "",
        "By case type:",
        "",
        f"- `multiple_known_speakers` ({by_type['multiple_known_speakers']}): "
        "the UD sentence spans 2+ known speakers (Artur resegmentation crosses turns).",
        f"- `known_plus_unresolved_utterance` ({by_type['known_plus_unresolved_utterance']}): "
        "one known speaker plus an utterance that has no TEI `who=`.",
        f"- `unknown_speaker` ({by_type['unknown_speaker']}): "
        "the utterance(s) have no TEI `who=` at all, so the speaker identity is unknown.",
        "",
        "By subcorpus: " + ", ".join(f"{sub}={n}" for sub, n in sorted(by_sub.items())),
        "",
        "By case type x subcorpus:",
        "",
    ]
    for ctype in CASE_TYPES:
        subs = sorted((sub, n) for (ct, sub), n in by_type_sub.items() if ct == ctype)
        lines.append(f"- `{ctype}`: " + (", ".join(f"{sub}={n}" for sub, n in subs) or "0"))
    lines += [
        "",
        "## Why these happen",
        "",
        "- **multiple_known_speakers / known_plus_unresolved_utterance** are Artur-only.",
        "  Artur was resegmented into UD sentences, and a UD sentence is not always one",
        "  speech turn: it can span adjacent utterances (sometimes TEI `trans=\"overlap\"`),",
        "  including an utterance that itself has no `who=`.",
        "- **unknown_speaker** occurs in any subcorpus (Gos/GosVL/Artur): the source TEI",
        "  `<u>` simply has no `who=` attribute (audience turns, backchannels, unidentified",
        "  voices). There is no speaker to attach, so the field is left blank rather than guessed.",
        "",
        "Speaker and overlap metadata are recovered through the TEI; the CoNLL-U rows",
        "only preserve `OriginalUtteranceId` (Artur) or the carried `# newpar id` (Gos/GosVL).",
        "",
        "## Output convention",
        "",
        "Do not emit a singular `# speaker_id`. The mini CoNLL-U records, per sentence:",
        "",
        "- `# speaker_edge_case = <type>`",
        "- `# recommended_speaker_id = _`",
        "- `# carried_newpar_id = ...` (Gos/GosVL sentences only)",
        "- `# suggested_speaker_ids = ...` and `# suggested_speaker_segments = ...` "
        "(when any speaker is known)",
        "- `# unresolved_utterances = ...` (utterances with no `who`)",
        "",
        "Files:",
        "",
        "- `speaker-edge-case-sentences.tsv`: one row per affected sentence.",
        "- `speaker-edge-case-sentences.conllu`: mini CoNLL-U with only affected sentences.",
        "",
        "## Examples",
        "",
    ]
    for ctype in CASE_TYPES:
        ex = _example(cases, ctype)
        if not ex:
            continue
        seg = "; ".join(
            f"{rng}:{speaker or '_'}({utt or '_'})"
            for rng, speaker, utt in speaker_segments(ex)
        )
        lines.append(f"- `{ctype}` — `{ex.sent_id}` ({ex.subcorpus}, source line {ex.start_line})")
        if ex.speaker_counts:
            lines.append("  - speakers: " + "; ".join(f"{s}:{n}" for s, n in ex.speaker_counts.most_common()))
        if ex.unresolved_utterance_counts:
            lines.append("  - unresolved utterances: "
                         + "; ".join(f"{u}:{n}" for u, n in ex.unresolved_utterance_counts.most_common()))
        lines.append(f"  - segments: {seg}")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    utt2spk = load_utterance_speakers()
    speeches = load_speeches()
    speakers = load_speakers()
    cases = parse_cases(utt2spk, speeches)
    cases.sort(key=lambda c: (CASE_TYPES.index(c.case_type), c.subcorpus, c.start_line))
    tei_meta = parse_tei_metadata(cases, speeches)
    write_tsv(cases, speakers, tei_meta)
    write_mini_conllu(cases)
    write_readme(cases)
    by_type = Counter(c.case_type for c in cases)
    print(f"Wrote {len(cases)} speaker edge-case sentences to {OUT_DIR}")
    for ctype in CASE_TYPES:
        print(f"  {ctype}: {by_type[ctype]}")


if __name__ == "__main__":
    main()
