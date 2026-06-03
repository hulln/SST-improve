# GOS manual check samples

Generated with deterministic random seed `20260603`.

Open these files together:
- `samples.tsv`: compact index of all samples
- `input-samples.conllu`: exact selected blocks from `corpora/gos/gos.conllu`
- `enriched-samples.conllu`: exact selected blocks from `corpora/gos/gos-enriched.conllu`
- `source-mapping.tsv`: exact source files/line numbers and expected mapped values

Manual check rule: for resolved speaker samples, the sentence utterance maps through `metadata/gos/utterance-speaker.tsv` to the same `# speaker_id`, and that speaker's row in `metadata/gos/Gos-speakers.tsv` gives the inserted `speaker_*` comments. For event samples, the `TEXT-ID` row in `metadata/gos/Gos-speeches.tsv` gives the inserted `event_*` comments, with English translations applied by the pipeline. For mixed or unavailable samples, there should be no singular sentence-level `# speaker_id`.

## S01 - doc_start_event_and_speaker_Gos

- `sent_id`: `Gos224.s1`
- document: `Gos224` (`Gos`)
- input lines: `corpora/gos/gos.conllu:2754727-2754734`
- enriched lines: `corpora/gos/gos-enriched.conllu:3483524-3483540`
- utterance source: `carried # newpar id`
- utterance ids checked: `Gos224.u1`
- mapped speaker candidates: `Af-prij-07190`
- enriched speaker_id: `Af-prij-07190`
- text preview: tam smo vidli pa

Expected event comments from source tables:
```text
# event_type = private
# event_domain = home, friends
# event_channel = in-person
# event_description = A conversation between two older friends about church, chores, livestock, health...
```
Source event row: `metadata/gos/Gos-speeches.tsv:225`
Description override row: `metadata/gos/descriptions-en.tsv:225`

Expected speaker comments from source tables:
```text
# speaker_id = Af-prij-07190
# speaker_gender = female
# speaker_age = 60+
# speaker_education = primary or less
# speaker_residence = posavska
```
Source speaker row: `metadata/gos/Gos-speakers.tsv:1706`

Utterance mapping rows to check:
```text
utterance_id	speaker_id	source_line
Gos224.u1	Af-prij-07190	metadata/gos/utterance-speaker.tsv:78574
```

## S02 - doc_start_event_and_speaker_GosVL

- `sent_id`: `GosVL14_karci.s1`
- document: `GosVL14_karci` (`GosVL`)
- input lines: `corpora/gos/gos.conllu:3202173-3202190`
- enriched lines: `corpora/gos/gos-enriched.conllu:4102688-4102714`
- utterance source: `carried # newpar id`
- utterance ids checked: `GosVL14_karci.u1`
- mapped speaker candidates: `Sm-vl022`
- enriched speaker_id: `Sm-vl022`
- text preview: veseli me da lahko danes predstavm en del del eee rezultatov naše programske skupine

Expected event comments from source tables:
```text
# event_type = info-education
# event_domain = public lecture, carcinoma
# event_channel = in-person
# event_description = Treatment of inoperable squamous cell …
```
Source event row: `metadata/gos/Gos-speeches.tsv:302`
Description override row: `metadata/gos/descriptions-en.tsv:302`

Expected speaker comments from source tables:
```text
# speaker_id = Sm-vl022
# speaker_gender = male
# speaker_age = unknown
# speaker_education = unknown
# speaker_residence = unknown
```
Source speaker row: `metadata/gos/Gos-speakers.tsv:2019`

Utterance mapping rows to check:
```text
utterance_id	speaker_id	source_line
GosVL14_karci.u1	Sm-vl022	metadata/gos/utterance-speaker.tsv:107812
```

## S03 - doc_start_event_and_speaker_Artur-J

- `sent_id`: `Artur-J-Gvecg-P580017.resegsent10614`
- document: `Artur-J-Gvecg-P580017` (`Artur-J`)
- input lines: `corpora/gos/gos.conllu:328335-328348`
- enriched lines: `corpora/gos/gos-enriched.conllu:381370-381393`
- utterance source: `token OriginalUtteranceId`
- utterance ids checked: `Artur-J-Gvecg-P580017.u1`
- mapped speaker candidates: `Artur-J-G4544`
- enriched speaker_id: `Artur-J-G4544`
- text preview: tudi zato , ker ta občina v teh dneh praznuje svoj praznik .

Expected event comments from source tables:
```text
# event_type = info-education
# event_domain = interview
# event_channel = radio
# event_description = Artur-J-Gvecg-P580017
```
Source event row: `metadata/gos/Gos-speeches.tsv:403`

Expected speaker comments from source tables:
```text
# speaker_id = Artur-J-G4544
# speaker_gender = female
# speaker_age = 60+
# speaker_education = high-school
# speaker_residence = unknown
```
Source speaker row: `metadata/gos/Gos-speakers.tsv:2262`

Utterance mapping rows to check:
```text
utterance_id	speaker_id	source_line
Artur-J-Gvecg-P580017.u1	Artur-J-G4544	metadata/gos/utterance-speaker.tsv:2489
```

## S04 - doc_start_event_and_speaker_Artur-N

- `sent_id`: `Artur-N-G5038-P600037.resegsent28429`
- document: `Artur-N-G5038-P600037` (`Artur-N`)
- input lines: `corpora/gos/gos.conllu:719196-719218`
- enriched lines: `corpora/gos/gos-enriched.conllu:861446-861478`
- utterance source: `token OriginalUtteranceId`
- utterance ids checked: `Artur-N-G5038-P600037.u2`
- mapped speaker candidates: `Artur-N-G5038`
- enriched speaker_id: `Artur-N-G5038`
- text preview: in sicer : najprej , eee , vzameš tristo gramov moke , lahko je bela , lahko dodaš še malo polnozrnate .

Expected event comments from source tables:
```text
# event_type = private
# event_domain = free monologue
# event_channel = in-person
# event_description = Artur-N-G5038-P600037
```
Source event row: `metadata/gos/Gos-speeches.tsv:487`

Expected speaker comments from source tables:
```text
# speaker_id = Artur-N-G5038
# speaker_gender = female
# speaker_age = 30 to 59
# speaker_education = university or more
# speaker_residence = pomurska
```
Source speaker row: `metadata/gos/Gos-speakers.tsv:2423`

Utterance mapping rows to check:
```text
utterance_id	speaker_id	source_line
Artur-N-G5038-P600037.u2	Artur-N-G5038	metadata/gos/utterance-speaker.tsv:9838
```

## S05 - doc_start_event_and_speaker_Artur-P

- `sent_id`: `Artur-P-G7181-P701995.resegsent63049`
- document: `Artur-P-G7181-P701995` (`Artur-P`)
- input lines: `corpora/gos/gos.conllu:1617263-1617287`
- enriched lines: `corpora/gos/gos-enriched.conllu:1937393-1937427`
- utterance source: `token OriginalUtteranceId`
- utterance ids checked: `Artur-P-G7181-P701995.u1`
- mapped speaker candidates: `Artur-P-G7181`
- enriched speaker_id: `Artur-P-G7181`
- text preview: torej , na našem ministrstvu že od januarja dva tisoč dvanajst dalje teče postopek priprave držaunega prostorskega načrta za hidroelektrarno hrastje-mota na Muri .

Expected event comments from source tables:
```text
# event_type = info-education
# event_domain = session of the National Assembly
# event_channel = in-person
# event_description = Artur-P-G7181-P701995
```
Source event row: `metadata/gos/Gos-speeches.tsv:1450`

Expected speaker comments from source tables:
```text
# speaker_id = Artur-P-G7181
# speaker_gender = male
# speaker_age = unknown
# speaker_education = unknown
# speaker_residence = unknown
```
Source speaker row: `metadata/gos/Gos-speakers.tsv:3378`

Utterance mapping rows to check:
```text
utterance_id	speaker_id	source_line
Artur-P-G7181-P701995.u1	Artur-P-G7181	metadata/gos/utterance-speaker.tsv:14543
```

## S06 - ordinary_gos_sentence_speaker_only

- `sent_id`: `Gos059.s171`
- document: `Gos059` (`Gos`)
- input lines: `corpora/gos/gos.conllu:1983559-1983564`
- enriched lines: `corpora/gos/gos-enriched.conllu:2428860-2428870`
- utterance source: `carried # newpar id`
- utterance ids checked: `Gos059.u144`
- mapped speaker candidates: `Lf-ucen-02196`
- enriched speaker_id: `Lf-ucen-02196`
- text preview: mislim … čas

Expected speaker comments from source tables:
```text
# speaker_id = Lf-ucen-02196
# speaker_gender = female
# speaker_age = 0-18
# speaker_education = primary or less
# speaker_residence = savinjska
```
Source speaker row: `metadata/gos/Gos-speakers.tsv:621`

Utterance mapping rows to check:
```text
utterance_id	speaker_id	source_line
Gos059.u144	Lf-ucen-02196	metadata/gos/utterance-speaker.tsv:31658
```

## S07 - ordinary_artur_sentence_speaker_only

- `sent_id`: `Artur-P-G7030-P700134.resegsent46706`
- document: `Artur-P-G7030-P700134` (`Artur-P`)
- input lines: `corpora/gos/gos.conllu:1169420-1169447`
- enriched lines: `corpora/gos/gos-enriched.conllu:1404275-1404307`
- utterance source: `token OriginalUtteranceId`
- utterance ids checked: `Artur-P-G7030-P700134.u1`
- mapped speaker candidates: `Artur-P-G7030`
- enriched speaker_id: `Artur-P-G7030`
- text preview: s strani Držaunega odvetništva smo bili obveščeni , da je Europska komisija petega desetega dva osəmnajst ložila tožbo in sodišču predlaga , da Sloveniji naloži globe .

Expected speaker comments from source tables:
```text
# speaker_id = Artur-P-G7030
# speaker_gender = male
# speaker_age = unknown
# speaker_education = unknown
# speaker_residence = unknown
```
Source speaker row: `metadata/gos/Gos-speakers.tsv:2673`

Utterance mapping rows to check:
```text
utterance_id	speaker_id	source_line
Artur-P-G7030-P700134.u1	Artur-P-G7030	metadata/gos/utterance-speaker.tsv:13735
```

## S08 - mixed_multiple_known_speakers_no_sentence_speaker

- `sent_id`: `Artur-J-Gvecg-P580013.resegsent10183`
- document: `Artur-J-Gvecg-P580013` (`Artur-J`)
- input lines: `corpora/gos/gos.conllu:317380-317398`
- enriched lines: `corpora/gos/gos-enriched.conllu:368270-368288`
- utterance source: `token OriginalUtteranceId`
- utterance ids checked: `Artur-J-Gvecg-P580013.u88; Artur-J-Gvecg-P580013.u89`
- mapped speaker candidates: `Artur-J-G4543; Artur-J-G4531`
- enriched speaker_id: `_`
- edge-case type: `multiple_known_speakers`
- proposed segments from audit: `1-4:Artur-J-G4543(Artur-J-Gvecg-P580013.u88); 5-18:Artur-J-G4531(Artur-J-Gvecg-P580013.u89)`
- text preview: naj vam bo srečno Hvala za tvoj obisk v studiu Štajerskega vala , hvala za to voščilo .

Expected speaker result:
No sentence-level `# speaker_id`, because the sentence maps to multiple speakers or to known+unresolved utterance tokens.

Utterance mapping rows to check:
```text
utterance_id	speaker_id	source_line
Artur-J-Gvecg-P580013.u88	Artur-J-G4543	metadata/gos/utterance-speaker.tsv:2346
Artur-J-Gvecg-P580013.u89	Artur-J-G4531	metadata/gos/utterance-speaker.tsv:2347
```

## S09 - known_plus_unresolved_utterance_no_sentence_speaker

- `sent_id`: `Artur-P-G7041-P701501.resegsent47979`
- document: `Artur-P-G7041-P701501` (`Artur-P`)
- input lines: `corpora/gos/gos.conllu:1201676-1201762`
- enriched lines: `corpora/gos/gos-enriched.conllu:1443131-1443217`
- utterance source: `token OriginalUtteranceId`
- utterance ids checked: `Artur-P-G7041-P701501.u6; Artur-P-G7041-P701501.u8; Artur-P-G7041-P701501.u9; Artur-P-G7041-P701501.u11`
- mapped speaker candidates: `Artur-P-G7041`
- enriched speaker_id: `_`
- edge-case type: `known_plus_unresolved_utterance`
- proposed segments from audit: `1-36:Artur-P-G7041(Artur-P-G7041-P701501.u6); 37-66:Artur-P-G7041(Artur-P-G7041-P701501.u8); 67-68:_(Artur-P-G7041-P701501.u9); 69-86:Artur-P-G7041(Artur-P-G7041-P701501.u11)`
- text preview: potem vemo , da je pred nami , eee , resən problem , ki terja , eee , zelo , em , ki terja poenotenje , in , em , čimprejšne poenotenje in , em , področje je potrebno uredit čim prej , usekakor še pred nasledno krizo ...

Expected speaker result:
No sentence-level `# speaker_id`, because the sentence maps to multiple speakers or to known+unresolved utterance tokens.

Utterance mapping rows to check:
```text
utterance_id	speaker_id	source_line
Artur-P-G7041-P701501.u6	Artur-P-G7041	metadata/gos/utterance-speaker.tsv:13795
Artur-P-G7041-P701501.u8	Artur-P-G7041	metadata/gos/utterance-speaker.tsv:13796
Artur-P-G7041-P701501.u9	_	metadata/gos/utterance-speaker.tsv:MISSING
Artur-P-G7041-P701501.u11	Artur-P-G7041	metadata/gos/utterance-speaker.tsv:13792
```

## S10 - unavailable_no_who_no_sentence_speaker

- `sent_id`: `GosVL39_skrek.s89`
- document: `GosVL39_skrek` (`GosVL`)
- input lines: `corpora/gos/gos.conllu:3303538-3303548`
- enriched lines: `corpora/gos/gos-enriched.conllu:4232397-4232407`
- utterance source: `carried # newpar id`
- utterance ids checked: `GosVL39_skrek.u9`
- mapped speaker candidates: `_`
- enriched speaker_id: `_`
- text preview: ampak je pa problem s čiščenjem s formatom podatkov

Expected speaker result:
No sentence-level `# speaker_id`, because the relevant utterance has no available `who` mapping in `utterance-speaker.tsv`.

Utterance mapping rows to check:
```text
utterance_id	speaker_id	source_line
GosVL39_skrek.u9	_	metadata/gos/utterance-speaker.tsv:MISSING
```

