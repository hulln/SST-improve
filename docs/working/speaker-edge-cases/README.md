# Speaker-level edge cases (no single sentence-level speaker)

GOS UD sentences for which the enrichment pipeline emits **no** singular
`# speaker_id`. The enriched corpus is left as-is (the speaker block is simply
omitted); this folder documents *why* each one is blank, by case.

- Affected sentences: 150

By case type:

- `multiple_known_speakers` (112): the UD sentence spans 2+ known speakers (Artur resegmentation crosses turns).
- `known_plus_unresolved_utterance` (2): one known speaker plus an utterance that has no TEI `who=`.
- `unknown_speaker` (36): the utterance(s) have no TEI `who=` at all, so the speaker identity is unknown.

By subcorpus: Artur-J=111, Artur-N=11, Artur-P=6, GosVL=22

By case type x subcorpus:

- `multiple_known_speakers`: Artur-J=110, Artur-N=2
- `known_plus_unresolved_utterance`: Artur-P=2
- `unknown_speaker`: Artur-J=1, Artur-N=9, Artur-P=4, GosVL=22

## Why these happen

- **multiple_known_speakers / known_plus_unresolved_utterance** are Artur-only.
  Artur was resegmented into UD sentences, and a UD sentence is not always one
  speech turn: it can span adjacent utterances (sometimes TEI `trans="overlap"`),
  including an utterance that itself has no `who=`.
- **unknown_speaker** occurs in any subcorpus (Gos/GosVL/Artur): the source TEI
  `<u>` simply has no `who=` attribute (audience turns, backchannels, unidentified
  voices). There is no speaker to attach, so the field is left blank rather than guessed.

Speaker and overlap metadata are recovered through the TEI; the CoNLL-U rows
only preserve `OriginalUtteranceId` (Artur) or the carried `# newpar id` (Gos/GosVL).

## Output convention

Do not emit a singular `# speaker_id`. The mini CoNLL-U records, per sentence:

- `# speaker_edge_case = <type>`
- `# recommended_speaker_id = _`
- `# carried_newpar_id = ...` (Gos/GosVL sentences only)
- `# suggested_speaker_ids = ...` and `# suggested_speaker_segments = ...` (when any speaker is known)
- `# unresolved_utterances = ...` (utterances with no `who`)

Files:

- `speaker-edge-case-sentences.tsv`: one row per affected sentence.
- `speaker-edge-case-sentences.conllu`: mini CoNLL-U with only affected sentences.

## Examples

- `multiple_known_speakers` — `Artur-J-Gvecg-P500001.resegsent153` (Artur-J, source line 4784)
  - speakers: Artur-J-G3006:14; Artur-J-G3003:8
  - segments: 1-14:Artur-J-G3006(Artur-J-Gvecg-P500001.u61); 15-22:Artur-J-G3003(Artur-J-Gvecg-P500001.u62)
- `known_plus_unresolved_utterance` — `Artur-P-G7002-P700444.resegsent43454` (Artur-P, source line 1081433)
  - speakers: Artur-P-G7002:37
  - unresolved utterances: Artur-P-G7002-P700444.u21:5
  - segments: 1-5:_(Artur-P-G7002-P700444.u21); 6-42:Artur-P-G7002(Artur-P-G7002-P700444.u23)
- `unknown_speaker` — `Artur-J-Gvecg-P580051.resegsent19750` (Artur-J, source line 576572)
  - unresolved utterances: Artur-J-Gvecg-P580051.u427:5
  - segments: 1-5:_(Artur-J-Gvecg-P580051.u427)
