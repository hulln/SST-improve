"""
Build per-split coconstruction review scaffolds from SST CoNLL-U files.

This script reads existing `Coconstruct=` links from the raw SST splits and writes:
  - docs/working/coconstructions/coconstruction-<split>-review.tsv
  - docs/working/coconstructions/coconstruction-<split>-proposed-changes.md

It does not modify any CoNLL-U files.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SST_DIR = ROOT / "src" / "sst"
WORKING_DIR = ROOT / "docs" / "working" / "coconstructions"
TOKEN_RE = re.compile(r"^(\d+)\t([^\t]+)\t")


@dataclass
class Token:
    token_id: str
    form: str
    misc: str
    raw_line: str


@dataclass
class Sentence:
    sent_id: str
    doc_id: str
    speaker_id: str
    text: str
    order: int
    block_lines: list[str]
    tokens: dict[str, Token]


@dataclass
class Edge:
    source_sent_id: str
    source_token_id: str
    source_form: str
    relation: str
    target_sent_id: str
    target_token_id: str


def parse_conllu(path: Path) -> tuple[dict[str, Sentence], list[Edge]]:
    sentences: dict[str, Sentence] = {}
    edges: list[Edge] = []

    block_lines: list[str] = []
    comments: dict[str, str] = {}
    tokens: dict[str, Token] = {}
    sent_order = 0

    def flush_sentence() -> None:
        nonlocal block_lines, comments, tokens, sent_order
        sent_id = comments.get("sent_id")
        if not sent_id:
            block_lines = []
            comments = {}
            tokens = {}
            return

        doc_id = sent_id.split(".s", 1)[0]
        sentence = Sentence(
            sent_id=sent_id,
            doc_id=doc_id,
            speaker_id=comments.get("speaker_id", ""),
            text=comments.get("text", ""),
            order=sent_order,
            block_lines=block_lines[:],
            tokens=tokens.copy(),
        )
        sentences[sent_id] = sentence
        sent_order += 1

        for token in sentence.tokens.values():
            match = re.search(r"(?:^|\|)Coconstruct=([^|\n]+)", token.misc)
            if not match:
                continue
            relation, target_sent_id, target_token_id = match.group(1).split("::")
            edges.append(
                Edge(
                    source_sent_id=sentence.sent_id,
                    source_token_id=token.token_id,
                    source_form=token.form,
                    relation=relation,
                    target_sent_id=target_sent_id,
                    target_token_id=target_token_id,
                )
            )

        block_lines = []
        comments = {}
        tokens = {}

    for line in path.read_text(encoding="utf-8").splitlines():
        if not line:
            flush_sentence()
            continue

        block_lines.append(line)

        if line.startswith("# "):
            key, value = line[2:].split(" = ", 1)
            comments[key] = value
            continue

        token_match = TOKEN_RE.match(line)
        if not token_match:
            continue

        cols = line.split("\t")
        token = Token(
            token_id=cols[0],
            form=cols[1],
            misc=cols[9],
            raw_line=line,
        )
        tokens[token.token_id] = token

    flush_sentence()
    return sentences, edges


def pair_edges(sentences: dict[str, Sentence], edges: list[Edge]) -> list[list[Edge]]:
    grouped: dict[tuple[str, str], list[Edge]] = defaultdict(list)
    for edge in edges:
        sent_pair = tuple(
            sorted(
                [edge.source_sent_id, edge.target_sent_id],
                key=lambda sent_id: sentence_sort_key(sentences, sent_id),
            )
        )
        grouped[sent_pair].append(edge)

    return [
        grouped[pair]
        for pair in sorted(
            grouped,
            key=lambda pair: (
                sentence_sort_key(sentences, pair[0]),
                sentence_sort_key(sentences, pair[1]),
            ),
        )
    ]


def sentence_sort_key(sentences: dict[str, Sentence], sent_id: str) -> int:
    return sentences[sent_id].order


def token_sort_key(token_id: str) -> tuple[int, str]:
    return (int(token_id), token_id)


def review_row(case_id: str, sentences: dict[str, Sentence], comp_edges: list[Edge]) -> list[str]:
    sent_ids = sorted(
        {edge.source_sent_id for edge in comp_edges} | {edge.target_sent_id for edge in comp_edges},
        key=lambda sent_id: sentence_sort_key(sentences, sent_id),
    )
    first_sent_id, second_sent_id = sent_ids
    first = sentences[first_sent_id]
    second = sentences[second_sent_id]

    ordered_edges = sorted(
        comp_edges,
        key=lambda edge: (
            sentence_sort_key(sentences, edge.source_sent_id),
            token_sort_key(edge.source_token_id),
        ),
    )
    links = " | ".join(
        f"{edge.source_sent_id}:{edge.source_token_id}:{edge.source_form}->"
        f"{edge.relation}::{edge.target_sent_id}::{edge.target_token_id}"
        for edge in ordered_edges
    )

    return [
        case_id,
        first.doc_id,
        first.sent_id,
        first.speaker_id,
        first.text,
        second.sent_id,
        second.speaker_id,
        second.text,
        links,
        "",
        "",
        "",
    ]


def current_block(sentences: dict[str, Sentence], comp_edges: list[Edge]) -> str:
    sent_ids = sorted(
        {edge.source_sent_id for edge in comp_edges} | {edge.target_sent_id for edge in comp_edges},
        key=lambda sent_id: sentence_sort_key(sentences, sent_id),
    )
    blocks = ["\n".join(sentences[sent_id].block_lines) for sent_id in sent_ids]
    return "\n\n".join(blocks)


def write_review(path: Path, rows: list[list[str]]) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(
            [
                "case_id",
                "doc_id",
                "first_sent_id",
                "first_speaker",
                "first_text",
                "second_sent_id",
                "second_speaker",
                "second_text",
                "existing_links",
                "decision",
                "proposed_root_only_annotation",
                "notes",
            ]
        )
        writer.writerows(rows)


def write_proposed_changes(path: Path, sentences: dict[str, Sentence], components: list[list[Edge]]) -> None:
    if not components:
        path.write_text("# No coconstruction cases found.\n", encoding="utf-8")
        return

    sections: list[str] = []
    for idx, comp_edges in enumerate(components, 1):
        case_id = f"coco_{idx:02d}"
        sections.append(f"# {case_id}")
        sections.append("")
        sections.append("## current")
        sections.append("")
        sections.append("```conllu")
        sections.append(current_block(sentences, comp_edges))
        sections.append("```")
        sections.append("")
        sections.append("## proposed")
        sections.append("")
        sections.append("hold")
        sections.append("")
        sections.append("no proposed change yet")
        sections.append("")

    path.write_text("\n".join(sections).rstrip() + "\n", encoding="utf-8")


def build_split(split: str, force: bool) -> None:
    conllu_path = SST_DIR / f"sl_sst-ud-{split}.conllu"
    review_path = WORKING_DIR / f"coconstruction-{split}-review.tsv"
    proposed_path = WORKING_DIR / f"coconstruction-{split}-proposed-changes.md"

    if not conllu_path.exists():
        raise FileNotFoundError(f"Missing input file: {conllu_path}")

    if not force and (review_path.exists() or proposed_path.exists()):
        print(f"{split}: skipped existing workflow files")
        return

    sentences, edges = parse_conllu(conllu_path)
    components = pair_edges(sentences, edges)

    rows = [
        review_row(f"coco_{idx:02d}", sentences, comp_edges)
        for idx, comp_edges in enumerate(components, 1)
    ]
    write_review(review_path, rows)
    write_proposed_changes(proposed_path, sentences, components)
    print(f"{split}: wrote {len(rows)} coconstruction cases")


def main() -> None:
    WORKING_DIR.mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--splits",
        nargs="+",
        default=["train", "dev", "test"],
        choices=["train", "dev", "test"],
    )
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    for split in args.splits:
        build_split(split, args.force)


if __name__ == "__main__":
    main()
