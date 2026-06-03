"""
Enrich a UD CoNLL-U file with GOS speaker and event metadata.

Usage:
    python scripts/enrich.py <corpus>     # e.g. sst, gos

The engine streams the input one sentence at a time (so it handles the ~400 MB GOS
file) and is corpus-agnostic. Per document it inserts, after ``# newdoc id``:

    # event_type, # event_domain, # event_channel, # event_description

and per sentence, after ``# sent_id`` (or after an existing ``# speaker_id``):

    # speaker_id, # speaker_gender, # speaker_age, # speaker_education, # speaker_residence

Document id, utterance and speaker are resolved with whatever the input provides:
  - doc id      = ``# newdoc id`` if present, else the sent_id prefix (Artur).
  - speaker     = existing ``# speaker_id`` (SST), else the speaker of the sentence's
                  utterance, found via ``# newpar id`` (Gos/GosVL) or MISC
                  ``OriginalUtteranceId`` (Artur), mapped through utterance-speaker.tsv.
                  If an Artur sentence's tokens point to multiple speakers, or to both
                  resolved and unresolved utterances, no sentence-level speaker is emitted.
"""

import argparse
import sys
from collections import Counter
from pathlib import Path

from corpora import (
    CORPORA,
    DESCRIPTIONS_TSV,
    SPEAKERS_TSV,
    SPEECHES_TSV,
    UTTERANCE_SPEAKER_TSV,
)
from sources import (
    load_descriptions,
    load_speakers,
    load_speeches,
    load_utterance_speaker,
)

EVENT_FIELDS = ("event_type", "event_domain", "event_channel", "event_description")
SPEAKER_FIELDS = ("speaker_gender", "speaker_age", "speaker_education", "speaker_residence")
_UTT_MARKER = "OriginalUtteranceId="


class Context:
    """Holds the loaded metadata and renders the comment blocks to insert."""

    def __init__(self, speakers, speeches, utt2spk):
        self.speakers = speakers
        self.speeches = speeches
        self.utt2spk = utt2spk

    def event_block(self, doc_id: str) -> str:
        ev = self.speeches.get(doc_id)
        if not ev:
            return ""
        return "".join(f"# {k} = {ev[k]}\n" for k in EVENT_FIELDS)

    def speaker_block(self, speaker_id: str) -> str:
        sp = self.speakers.get(speaker_id)
        if not sp:
            return ""
        return "".join(f"# {k} = {sp[k]}\n" for k in SPEAKER_FIELDS)


def comment_key(raw: str) -> str | None:
    """For a comment line ``# key = value`` return ``key`` (else None)."""
    s = raw.lstrip()
    if not s.startswith("#"):
        return None
    content = s[1:].strip()
    return content.split(" = ", 1)[0] if " = " in content else content


def comment_value(raw: str) -> str:
    return raw.split(" = ", 1)[1].rstrip("\r\n")


def speaker_from_sentence(
    token_lines: list[str],
    fallback_utterance: str | None,
    utt2spk: dict[str, str],
) -> tuple[str | None, bool]:
    """Return (speaker_id, ambiguous) for a sentence.

    Artur token rows carry ``OriginalUtteranceId``. A sentence-level speaker is
    safe only if every token-level utterance with speaker information resolves
    to the same speaker and no token-level utterance is unresolved. If no
    token-level utterance is present, fall back to ``# newpar id`` for Gos/GosVL.
    """
    utterances: Counter[str] = Counter()
    for line in token_lines:
        i = line.find(_UTT_MARKER)
        if i == -1:
            continue
        start = i + len(_UTT_MARKER)
        end = line.find("|", start)
        uid = line[start:] if end == -1 else line[start:end]
        utterances[uid.rstrip("\r\n")] += 1

    if utterances:
        speakers: set[str] = set()
        unresolved = False
        for utt in utterances:
            speaker = utt2spk.get(utt)
            if speaker is None:
                unresolved = True
            else:
                speakers.add(speaker)
        if len(speakers) == 1 and not unresolved:
            return next(iter(speakers)), False
        return None, len(speakers) > 1 or bool(speakers and unresolved)

    if fallback_utterance:
        return utt2spk.get(fallback_utterance), False
    return None, False


def enrich_file(in_path: Path, out_path: Path, ctx: Context) -> dict:
    stats = {
        "docs": 0,
        "docs_no_event": 0,
        "sents": 0,
        "speaker_from_comment": 0,
        "speaker_resolved": 0,
        "speaker_no_attrs": 0,
        "speaker_unresolved": 0,
        "speaker_ambiguous": 0,
    }
    current_doc: str | None = None
    current_doc_from_marker = False
    current_newpar: str | None = None
    comments: list[str] = []
    tokens: list[str] = []

    def flush(fout) -> None:
        nonlocal current_doc, current_doc_from_marker, current_newpar
        if not comments and not tokens:
            return
        parsed = {comment_key(c): c for c in comments}
        sent_id = comment_value(parsed["sent_id"]) if "sent_id" in parsed else None
        if "newpar id" in parsed:
            current_newpar = comment_value(parsed["newpar id"])

        # Explicit "# newdoc id" markers are authoritative for doc boundaries. The
        # sent_id prefix is only trusted in a marker-less region (raw GOS Artur),
        # because in SST sentences are resegmented and their prefixes do not align
        # with the marker-defined documents.
        has_newdoc = "newdoc id" in parsed
        if has_newdoc:
            doc_id = comment_value(parsed["newdoc id"])
            is_new_doc = doc_id != current_doc
            current_doc_from_marker = True
        elif current_doc_from_marker:
            doc_id = current_doc
            is_new_doc = False
        elif sent_id is not None:
            doc_id = sent_id.split(".", 1)[0]
            is_new_doc = doc_id != current_doc
        else:
            doc_id = current_doc
            is_new_doc = False

        has_speaker = "speaker_id" in parsed
        if has_speaker:
            speaker_id = comment_value(parsed["speaker_id"])
            speaker_ambiguous = False
        else:
            speaker_id, speaker_ambiguous = speaker_from_sentence(tokens, current_newpar, ctx.utt2spk)

        event_block = ctx.event_block(doc_id) if is_new_doc else ""
        speaker_block = ctx.speaker_block(speaker_id) if speaker_id else ""

        # ---- stats ----
        if is_new_doc:
            stats["docs"] += 1
            if not event_block:
                stats["docs_no_event"] += 1
        if sent_id is not None:
            stats["sents"] += 1
            if has_speaker:
                stats["speaker_from_comment"] += 1
            elif speaker_ambiguous:
                stats["speaker_ambiguous"] += 1
            elif speaker_id is None:
                stats["speaker_unresolved"] += 1
            elif speaker_block:
                stats["speaker_resolved"] += 1
            else:
                stats["speaker_no_attrs"] += 1

        # ---- write, preserving original line bytes; inserted lines use \n ----
        if is_new_doc and not has_newdoc:
            fout.write(f"# newdoc id = {doc_id}\n")
            fout.write(event_block)
        for raw in comments:
            fout.write(raw)
            key = comment_key(raw)
            if key == "newdoc id" and is_new_doc:
                fout.write(event_block)
            elif key == "sent_id" and not has_speaker and speaker_id is not None:
                fout.write(f"# speaker_id = {speaker_id}\n")
                fout.write(speaker_block)
            elif key == "speaker_id":
                fout.write(speaker_block)
        for raw in tokens:
            fout.write(raw)

        current_doc = doc_id if doc_id is not None else current_doc
        comments.clear()
        tokens.clear()

    with open(in_path, encoding="utf-8") as fin, open(out_path, "w", encoding="utf-8") as fout:
        for line in fin:
            if not line.strip():
                flush(fout)
                fout.write(line)
            elif line.lstrip().startswith("#"):
                comments.append(line)
            else:
                tokens.append(line)
        flush(fout)

    return stats


def report(name: str, in_path: Path, stats: dict) -> None:
    print(f"[{name}] {in_path.name}", file=sys.stderr)
    print(f"    docs:               {stats['docs']} (no event metadata: {stats['docs_no_event']})", file=sys.stderr)
    print(f"    sentences:          {stats['sents']}", file=sys.stderr)
    print(f"    speaker from input: {stats['speaker_from_comment']}", file=sys.stderr)
    no_speaker = stats["speaker_unresolved"] + stats["speaker_ambiguous"]
    print(f"    speaker resolved:   {stats['speaker_resolved']} (resolved id, no attrs: {stats['speaker_no_attrs']})", file=sys.stderr)
    print(f"    speaker no block:   {no_speaker} "
          f"(metadata unavailable: {stats['speaker_unresolved']}; "
          f"ambiguous/mixed: {stats['speaker_ambiguous']})", file=sys.stderr)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("corpus", choices=sorted(CORPORA), help="corpus to enrich")
    args = ap.parse_args()

    speakers = load_speakers(SPEAKERS_TSV)
    descriptions = load_descriptions(DESCRIPTIONS_TSV)
    speeches = load_speeches(SPEECHES_TSV, descriptions)
    utt2spk = load_utterance_speaker(UTTERANCE_SPEAKER_TSV)
    ctx = Context(speakers, speeches, utt2spk)

    corpus = CORPORA[args.corpus]
    for in_path, out_path in corpus.io:
        if not in_path.exists():
            raise FileNotFoundError(f"Missing input file: {in_path}")
        stats = enrich_file(in_path, out_path, ctx)
        report(corpus.name, in_path, stats)
        print(f"    -> {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
