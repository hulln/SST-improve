# Artur sentence-level speaker edge cases

This directory lists Artur UD sentences that should not receive one
singular sentence-level speaker ID.

- Affected sentences: 114
- Sentences with multiple known TEI speakers: 112
- Sentences with one known speaker plus unresolved/no-`who` utterance tokens: 2
- Affected sentences with no strict majority speaker: 3
- Affected sentences with at least one TEI `trans="overlap"` utterance: 34
- Affected sentences crossing an utterance document boundary: 4
- By subcorpus: Artur-J=110, Artur-N=2, Artur-P=2

Why this happens: Artur was resegmented into UD sentences. A UD sentence
is not always the same thing as an original speech turn. Sometimes a UD
sentence spans adjacent utterances, and sometimes the TEI marks the
utterances as overlapping speech. Two additional sentences combine
one known speaker with tokens from an utterance that has no TEI `who=`.

Overlap status comes from TEI `trans="overlap"`, not from CoNLL-U.
The CoNLL-U rows only preserve `OriginalUtteranceId`; speaker and
overlap metadata are recovered through TEI.

Recommended policy: do not emit a singular `# speaker_id` for these
sentences. The mini CoNLL-U uses custom comments instead:

- `# recommended_speaker_id = _`
- `# suggested_speaker_ids = ...`
- `# suggested_speaker_segments = token-range:speaker(utterance); ...`

Files:

- `speaker-edge-case-sentences.tsv`: one row per affected sentence.
- `speaker-edge-case-sentences.conllu`: mini CoNLL-U with only affected
  sentences and suggested speaker-segment comments.

Example:

- `Artur-J-Gvecg-P500001.resegsent153` at source line 4784
- Speaker token counts: Artur-J-G3006:14; Artur-J-G3003:8
- Segments: 1-14:Artur-J-G3006(Artur-J-Gvecg-P500001.u61); 15-22:Artur-J-G3003(Artur-J-Gvecg-P500001.u62)
