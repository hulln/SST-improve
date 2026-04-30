# coco_01

## current

```conllu
# sent_id = Gos009.s225
# speaker_id = Tf-stud-06580
# sound_url = https://nl.ijs.si/project/gos20/Gos009/Gos009.s225.mp3
# text = nisem ga iskala , ampak sem srečala v tečaj slovenščine na začetku , eem , sem srečala moj z- zdaj- , eee , moj
1	nisem	biti	AUX	Va-r1s-y	Mood=Ind|Number=Sing|Person=1|Polarity=Neg|Tense=Pres|VerbForm=Fin	3	aux	_	pronunciation=nisem|Gos2.1_token_id=Gos009.tok1770
2	ga	on	PRON	Pp3msa--y	Case=Acc|Gender=Masc|Number=Sing|Person=3|PronType=Prs|Variant=Short	3	obj	_	pronunciation=ga|Gos2.1_token_id=Gos009.tok1771
3	iskala	iskati	VERB	Vmpp-sf	Aspect=Imp|Gender=Fem|Number=Sing|VerbForm=Part	0	root	_	pronunciation=iskala|Gos2.1_token_id=Gos009.tok1772
4	,	,	PUNCT	Z	_	7	punct	_	_
5	ampak	ampak	CCONJ	Cc	_	7	cc	_	pronunciation=ampak|Gos2.1_token_id=Gos009.tok1773
6	sem	biti	AUX	Va-r1s-n	Mood=Ind|Number=Sing|Person=1|Polarity=Pos|Tense=Pres|VerbForm=Fin	7	aux	_	pronunciation=sem|Gos2.1_token_id=Gos009.tok1774
7	srečala	srečati	VERB	Vmep-sf	Aspect=Perf|Gender=Fem|Number=Sing|VerbForm=Part	3	conj	_	pronunciation=srečala|Gos2.1_token_id=Gos009.tok1775
8	v	v	ADP	Sa	Case=Acc	9	case	_	pronunciation=v|Gos2.1_token_id=Gos009.tok1776
9	tečaj	tečaj	NOUN	Ncmsan	Animacy=Inan|Case=Acc|Gender=Masc|Number=Sing	7	obl	_	pronunciation=tečaj|Gos2.1_token_id=Gos009.tok1777
10	slovenščine	slovenščina	NOUN	Ncfsg	Case=Gen|Gender=Fem|Number=Sing	9	nmod	_	pronunciation=slovenščine|Gos2.1_token_id=Gos009.tok1778
11	na	na	ADP	Sl	Case=Loc	12	case	_	pronunciation=na|Gos2.1_token_id=Gos009.tok1779
12	začetku	začetek	NOUN	Ncmsl	Case=Loc|Gender=Masc|Number=Sing	17	obl	_	pronunciation=začetku|Gos2.1_token_id=Gos009.tok1780
13	,	,	PUNCT	Z	_	14	punct	_	_
14	eem	eem	INTJ	I	_	17	discourse:filler	_	pronunciation=eem|Gos2.1_token_id=Gos009.tok1781
15	,	,	PUNCT	Z	_	14	punct	_	_
16	sem	biti	AUX	Va-r1s-n	Mood=Ind|Number=Sing|Person=1|Polarity=Pos|Tense=Pres|VerbForm=Fin	17	aux	_	pronunciation=sem|Gos2.1_token_id=Gos009.tok1782
17	srečala	srečati	VERB	Vmep-sf	Aspect=Perf|Gender=Fem|Number=Sing|VerbForm=Part	3	parataxis	_	pronunciation=srečala|Gos2.1_token_id=Gos009.tok1783
18	moj	moj	DET	Ps1msns	Case=Nom|Gender=Masc|Number=Sing|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs	24	reparandum	_	pronunciation=moj|Gos2.1_token_id=Gos009.tok1784|Coconstruct=reparandum::Gos009.s227::4
19	z-	z-	X	Xt	_	24	reparandum	_	pronunciation=z…|Gos2.1_token_id=Gos009.tok1785
20	zdaj-	zdaj-	X	Xt	_	24	reparandum	_	pronunciation=zdaj…|Gos2.1_token_id=Gos009.tok1786
21	,	,	PUNCT	Z	_	22	punct	_	_
22	eee	eee	INTJ	I	_	17	discourse:filler	_	pronunciation=eee|Gos2.1_token_id=Gos009.tok1787
23	,	,	PUNCT	Z	_	22	punct	_	_
24	moj	moj	DET	Ps1msns	Case=Nom|Gender=Masc|Number=Sing|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs	17	obj	_	pronunciation=moj|Gos2.1_token_id=Gos009.tok1788|Coconstruct=reparandum::Gos009.s227::4

# sent_id = Gos009.s227
# speaker_id = Af-prof-06578
# sound_url = https://nl.ijs.si/project/gos20/Gos009/Gos009.s227.mp3
# text = mojo cimro , mojega cimra .
1	mojo	moj	DET	Ps1fsas	Case=Acc|Gender=Fem|Number=Sing|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs	2	det	_	pronunciation=mojo|Gos2.1_token_id=Gos009.tok1789
2	cimro	cimra	NOUN	Ncfsa	Case=Acc|Gender=Fem|Number=Sing	5	reparandum	_	pronunciation=cimro|Gos2.1_token_id=Gos009.tok1790
3	,	,	PUNCT	Z	_	2	punct	_	_
4	mojega	moj	DET	Ps1msas	Case=Acc|Gender=Masc|Number=Sing|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs	5	det	_	pronunciation=mojega|Gos2.1_token_id=Gos009.tok1791
5	cimra	cimer	NOUN	Ncmsay	Animacy=Anim|Case=Acc|Gender=Masc|Number=Sing	0	root	_	pronunciation=cimra|Gos2.1_token_id=Gos009.tok1792|Coconstruct=obj::Gos009.s225::17
6	.	.	PUNCT	Z	_	5	punct	_	_
```

## proposed

Remove Coconstruct from Speaker 1's tokens 18 and 24 (forward pointers violate the rule that Coconstruct is only on the responding token). Speaker 2's cimra (s227:5) correctly points back to srečala (s225:17) with obj — the slot Speaker 1 left open. No other changes.

```conllu
# sent_id = Gos009.s225
# speaker_id = Tf-stud-06580
# sound_url = https://nl.ijs.si/project/gos20/Gos009/Gos009.s225.mp3
# text = nisem ga iskala , ampak sem srečala v tečaj slovenščine na začetku , eem , sem srečala moj z- zdaj- , eee , moj
1	nisem	biti	AUX	Va-r1s-y	Mood=Ind|Number=Sing|Person=1|Polarity=Neg|Tense=Pres|VerbForm=Fin	3	aux	_	pronunciation=nisem|Gos2.1_token_id=Gos009.tok1770
2	ga	on	PRON	Pp3msa--y	Case=Acc|Gender=Masc|Number=Sing|Person=3|PronType=Prs|Variant=Short	3	obj	_	pronunciation=ga|Gos2.1_token_id=Gos009.tok1771
3	iskala	iskati	VERB	Vmpp-sf	Aspect=Imp|Gender=Fem|Number=Sing|VerbForm=Part	0	root	_	pronunciation=iskala|Gos2.1_token_id=Gos009.tok1772
4	,	,	PUNCT	Z	_	7	punct	_	_
5	ampak	ampak	CCONJ	Cc	_	7	cc	_	pronunciation=ampak|Gos2.1_token_id=Gos009.tok1773
6	sem	biti	AUX	Va-r1s-n	Mood=Ind|Number=Sing|Person=1|Polarity=Pos|Tense=Pres|VerbForm=Fin	7	aux	_	pronunciation=sem|Gos2.1_token_id=Gos009.tok1774
7	srečala	srečati	VERB	Vmep-sf	Aspect=Perf|Gender=Fem|Number=Sing|VerbForm=Part	3	conj	_	pronunciation=srečala|Gos2.1_token_id=Gos009.tok1775
8	v	v	ADP	Sa	Case=Acc	9	case	_	pronunciation=v|Gos2.1_token_id=Gos009.tok1776
9	tečaj	tečaj	NOUN	Ncmsan	Animacy=Inan|Case=Acc|Gender=Masc|Number=Sing	7	obl	_	pronunciation=tečaj|Gos2.1_token_id=Gos009.tok1777
10	slovenščine	slovenščina	NOUN	Ncfsg	Case=Gen|Gender=Fem|Number=Sing	9	nmod	_	pronunciation=slovenščine|Gos2.1_token_id=Gos009.tok1778
11	na	na	ADP	Sl	Case=Loc	12	case	_	pronunciation=na|Gos2.1_token_id=Gos009.tok1779
12	začetku	začetek	NOUN	Ncmsl	Case=Loc|Gender=Masc|Number=Sing	17	obl	_	pronunciation=začetku|Gos2.1_token_id=Gos009.tok1780
13	,	,	PUNCT	Z	_	14	punct	_	_
14	eem	eem	INTJ	I	_	17	discourse:filler	_	pronunciation=eem|Gos2.1_token_id=Gos009.tok1781
15	,	,	PUNCT	Z	_	14	punct	_	_
16	sem	biti	AUX	Va-r1s-n	Mood=Ind|Number=Sing|Person=1|Polarity=Pos|Tense=Pres|VerbForm=Fin	17	aux	_	pronunciation=sem|Gos2.1_token_id=Gos009.tok1782
17	srečala	srečati	VERB	Vmep-sf	Aspect=Perf|Gender=Fem|Number=Sing|VerbForm=Part	3	parataxis	_	pronunciation=srečala|Gos2.1_token_id=Gos009.tok1783
18	moj	moj	DET	Ps1msns	Case=Nom|Gender=Masc|Number=Sing|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs	24	reparandum	_	pronunciation=moj|Gos2.1_token_id=Gos009.tok1784
19	z-	z-	X	Xt	_	24	reparandum	_	pronunciation=z…|Gos2.1_token_id=Gos009.tok1785
20	zdaj-	zdaj-	X	Xt	_	24	reparandum	_	pronunciation=zdaj…|Gos2.1_token_id=Gos009.tok1786
21	,	,	PUNCT	Z	_	22	punct	_	_
22	eee	eee	INTJ	I	_	17	discourse:filler	_	pronunciation=eee|Gos2.1_token_id=Gos009.tok1787
23	,	,	PUNCT	Z	_	22	punct	_	_
24	moj	moj	DET	Ps1msns	Case=Nom|Gender=Masc|Number=Sing|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs	17	obj	_	pronunciation=moj|Gos2.1_token_id=Gos009.tok1788

# sent_id = Gos009.s227
# speaker_id = Af-prof-06578
# sound_url = https://nl.ijs.si/project/gos20/Gos009/Gos009.s227.mp3
# text = mojo cimro , mojega cimra .
1	mojo	moj	DET	Ps1fsas	Case=Acc|Gender=Fem|Number=Sing|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs	2	det	_	pronunciation=mojo|Gos2.1_token_id=Gos009.tok1789
2	cimro	cimra	NOUN	Ncfsa	Case=Acc|Gender=Fem|Number=Sing	5	reparandum	_	pronunciation=cimro|Gos2.1_token_id=Gos009.tok1790
3	,	,	PUNCT	Z	_	2	punct	_	_
4	mojega	moj	DET	Ps1msas	Case=Acc|Gender=Masc|Number=Sing|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs	5	det	_	pronunciation=mojega|Gos2.1_token_id=Gos009.tok1791
5	cimra	cimer	NOUN	Ncmsay	Animacy=Anim|Case=Acc|Gender=Masc|Number=Sing	0	root	_	pronunciation=cimra|Gos2.1_token_id=Gos009.tok1792|Coconstruct=obj::Gos009.s225::17
6	.	.	PUNCT	Z	_	5	punct	_	_
```

# coco_02

## current

```conllu
# sent_id = Gos017.s284
# speaker_id = Rm-ucen-07121
# sound_url = https://nl.ijs.si/project/gos20/Gos017/Gos017.s284.mp3
# text = eee , štiri sem imel še vedno , samo pol je bilo pač
1	eee	eee	INTJ	I	_	5	discourse:filler	_	pronunciation=eee|Gos2.1_token_id=Gos017.tok1891
2	,	,	PUNCT	Z	_	1	punct	_	_
3	štiri	štirje	NUM	Mlcfpa	Case=Acc|Gender=Fem|Number=Plur|NumForm=Word|NumType=Card	5	obj	_	pronunciation=štiri|Gos2.1_token_id=Gos017.tok1892
4	sem	biti	AUX	Va-r1s-n	Mood=Ind|Number=Sing|Person=1|Polarity=Pos|Tense=Pres|VerbForm=Fin	5	aux	_	pronunciation=sem|Gos2.1_token_id=Gos017.tok1893
5	imel	imeti	VERB	Vmpp-sm	Aspect=Imp|Gender=Masc|Number=Sing|VerbForm=Part	0	root	_	pronunciation=mel|Gos2.1_token_id=Gos017.tok1894
6	še	še	PART	Q	_	5	advmod	_	pronunciation=še|Gos2.1_token_id=Gos017.tok1895
7	vedno	vedno	ADV	Rgp	Degree=Pos	5	advmod	_	pronunciation=vedno|Gos2.1_token_id=Gos017.tok1896
8	,	,	PUNCT	Z	_	12	punct	_	_
9	samo	samo	PART	Q	_	12	cc	_	pronunciation=sam|Gos2.1_token_id=Gos017.tok1897
10	pol	pol	DET	Rgp	Degree=Pos	12	advmod	_	pronunciation=po|Gos2.1_token_id=Gos017.tok1898|Coconstruct=advmod::Gos017.s285::3
11	je	biti	AUX	Va-r3s-n	Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin	12	aux	_	pronunciation=je|Gos2.1_token_id=Gos017.tok1899
12	bilo	biti	VERB	Va-p-sn	Gender=Neut|Number=Sing|VerbForm=Part	5	conj	_	pronunciation=blo|Gos2.1_token_id=Gos017.tok1900|Coconstruct=cop::Gos017.s285::3
13	pač	pač	PART	Q	_	12	advmod	_	pronunciation=pač|Gos2.1_token_id=Gos017.tok1901|Coconstruct=advmod::Gos017.s285::3

# sent_id = Gos017.s285
# speaker_id = Af-prof-07104
# sound_url = https://nl.ijs.si/project/gos20/Gos017/Gos017.s285.mp3
# text = bolj trdno štiri .
1	bolj	bolj	ADV	Rgc	Degree=Cmp	2	advmod	_	pronunciation=bolj|Gos2.1_token_id=Gos017.tok1902
2	trdno	trden	ADJ	Agpfsa	Case=Acc|Degree=Pos|Gender=Fem|Number=Sing	3	amod	_	pronunciation=trdno|Gos2.1_token_id=Gos017.tok1903
3	štiri	štirje	NUM	Mlcfpa	Case=Acc|Gender=Fem|Number=Plur|NumForm=Word|NumType=Card	0	root	_	pronunciation=štiri|Gos2.1_token_id=Gos017.tok1904|Coconstruct=parataxis::Gos017.s284::12
4	.	.	PUNCT	Z	_	3	punct	_	_
```

## proposed

This is 4.2 stacking: Speaker 1 already realized "štiri" (four) but then hedges with "pol je bilo pač" (it was kind of half). Speaker 2 provides "bolj trdno štiri" (more solidly four) — a reformulation targeting the same referent (the grade/amount). Per the PDF, reformulations where conjuncts denote the same referent → `conj:reform`, not `parataxis`.

Changes:
- Remove Coconstruct from s284 tokens 10, 12, 13 (forward pointers — wrong direction)
- Change Coconstruct on s285:3 (štiri): relation `parataxis→conj:reform`, anchor stays at `s284::12` (bilo = head of the first denotation "samo pol je bilo pač", the clause Speaker 2 is reformulating). Per the PDF: "In all cases, ⟨tok_id⟩ points to the head of the first denotation."

```conllu
# sent_id = Gos017.s284
# speaker_id = Rm-ucen-07121
# sound_url = https://nl.ijs.si/project/gos20/Gos017/Gos017.s284.mp3
# text = eee , štiri sem imel še vedno , samo pol je bilo pač
1	eee	eee	INTJ	I	_	5	discourse:filler	_	pronunciation=eee|Gos2.1_token_id=Gos017.tok1891
2	,	,	PUNCT	Z	_	1	punct	_	_
3	štiri	štirje	NUM	Mlcfpa	Case=Acc|Gender=Fem|Number=Plur|NumForm=Word|NumType=Card	5	obj	_	pronunciation=štiri|Gos2.1_token_id=Gos017.tok1892
4	sem	biti	AUX	Va-r1s-n	Mood=Ind|Number=Sing|Person=1|Polarity=Pos|Tense=Pres|VerbForm=Fin	5	aux	_	pronunciation=sem|Gos2.1_token_id=Gos017.tok1893
5	imel	imeti	VERB	Vmpp-sm	Aspect=Imp|Gender=Masc|Number=Sing|VerbForm=Part	0	root	_	pronunciation=mel|Gos2.1_token_id=Gos017.tok1894
6	še	še	PART	Q	_	5	advmod	_	pronunciation=še|Gos2.1_token_id=Gos017.tok1895
7	vedno	vedno	ADV	Rgp	Degree=Pos	5	advmod	_	pronunciation=vedno|Gos2.1_token_id=Gos017.tok1896
8	,	,	PUNCT	Z	_	12	punct	_	_
9	samo	samo	PART	Q	_	12	cc	_	pronunciation=sam|Gos2.1_token_id=Gos017.tok1897
10	pol	pol	DET	Rgp	Degree=Pos	12	advmod	_	pronunciation=po|Gos2.1_token_id=Gos017.tok1898
11	je	biti	AUX	Va-r3s-n	Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin	12	aux	_	pronunciation=je|Gos2.1_token_id=Gos017.tok1899
12	bilo	biti	VERB	Va-p-sn	Gender=Neut|Number=Sing|VerbForm=Part	5	conj	_	pronunciation=blo|Gos2.1_token_id=Gos017.tok1900
13	pač	pač	PART	Q	_	12	advmod	_	pronunciation=pač|Gos2.1_token_id=Gos017.tok1901

# sent_id = Gos017.s285
# speaker_id = Af-prof-07104
# sound_url = https://nl.ijs.si/project/gos20/Gos017/Gos017.s285.mp3
# text = bolj trdno štiri .
1	bolj	bolj	ADV	Rgc	Degree=Cmp	2	advmod	_	pronunciation=bolj|Gos2.1_token_id=Gos017.tok1902
2	trdno	trden	ADJ	Agpfsa	Case=Acc|Degree=Pos|Gender=Fem|Number=Sing	3	amod	_	pronunciation=trdno|Gos2.1_token_id=Gos017.tok1903
3	štiri	štirje	NUM	Mlcfpa	Case=Acc|Gender=Fem|Number=Plur|NumForm=Word|NumType=Card	0	root	_	pronunciation=štiri|Gos2.1_token_id=Gos017.tok1904|Coconstruct=conj:reform::Gos017.s284::12
4	.	.	PUNCT	Z	_	3	punct	_	_
```

# coco_03

## current

```conllu
# sent_id = Gos020.s407
# speaker_id = Mf-prof-01061
# sound_url = https://nl.ijs.si/project/gos20/Gos020/Gos020.s407.mp3
# text = se pravi , rezultat za Žide je bil , v katerem koli taborišču že so se znašli , isti
1	se	se	PRON	Px------y	PronType=Prs|Reflex=Yes|Variant=Short	19	cc	_	pronunciation=se|Gos2.1_token_id=Gos020.tok3097
2	pravi	praviti	VERB	Vmbr3s	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	1	fixed	_	pronunciation=pravi|Gos2.1_token_id=Gos020.tok3098
3	,	,	PUNCT	Z	_	1	punct	_	_
4	rezultat	rezultat	NOUN	Ncmsn	Case=Nom|Gender=Masc|Number=Sing	19	nsubj	_	pronunciation=rezultat|Gos2.1_token_id=Gos020.tok3099
5	za	za	ADP	Sa	Case=Acc	6	case	_	pronunciation=za|Gos2.1_token_id=Gos020.tok3100
6	Žide	Žid	PROPN	Npmpa	Case=Acc|Gender=Masc|Number=Plur	19	obl	_	pronunciation=Žide|Gos2.1_token_id=Gos020.tok3101
7	je	biti	AUX	Va-r3s-n	Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin	19	aux	_	pronunciation=je|Gos2.1_token_id=Gos020.tok3102
8	bil	biti	AUX	Va-p-sm	Gender=Masc|Number=Sing|VerbForm=Part	19	cop	_	pronunciation=bil|Gos2.1_token_id=Gos020.tok3103
9	,	,	PUNCT	Z	_	17	punct	_	_
10	v	v	ADP	Sl	Case=Loc	13	case	_	pronunciation=v|Gos2.1_token_id=Gos020.tok3104
11	katerem	kateri	DET	Pq-nsl	Case=Loc|Gender=Neut|Number=Sing|PronType=Int	13	det	_	pronunciation=kateremkolu|Gos2.1_token_id=Gos020.tok3105n1
12	koli	koli	PART	Q	_	11	fixed	_	pronunciation=kateremkolu|Gos2.1_token_id=Gos020.tok3105n2
13	taborišču	taborišče	NOUN	Ncnsl	Case=Loc|Gender=Neut|Number=Sing	17	obl	_	pronunciation=taborišču|Gos2.1_token_id=Gos020.tok3106
14	že	že	PART	Q	_	13	advmod	_	pronunciation=že|Gos2.1_token_id=Gos020.tok3107
15	so	biti	AUX	Va-r3p-n	Mood=Ind|Number=Plur|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin	17	aux	_	pronunciation=so|Gos2.1_token_id=Gos020.tok3108
16	se	se	PRON	Px------y	PronType=Prs|Reflex=Yes|Variant=Short	17	expl	_	pronunciation=se|Gos2.1_token_id=Gos020.tok3109
17	znašli	znajti	VERB	Vmep-pm	Aspect=Perf|Gender=Masc|Number=Plur|VerbForm=Part	19	advcl	_	pronunciation=znašli|Gos2.1_token_id=Gos020.tok3110
18	,	,	PUNCT	Z	_	17	punct	_	_
19	isti	isti	DET	Pi-msn	Case=Nom|Gender=Masc|Number=Sing|PronType=Ind	0	root	_	pronunciation=isti|Gos2.1_token_id=Gos020.tok3111

# sent_id = Gos020.s408
# speaker_id = Jm-ucen-01064
# sound_url = https://nl.ijs.si/project/gos20/Gos020/Gos020.s408.mp3
# text = slab .
1	slab	slab	ADJ	Agpmsnn	Case=Nom|Definite=Ind|Degree=Pos|Gender=Masc|Number=Sing	0	root	_	pronunciation=slab|Gos2.1_token_id=Gos020.tok3112|Coconstruct=conj::Gos020.s407::19
2	.	.	PUNCT	Z	_	1	punct	_	_
```

## proposed

This is 4.2 stacking: Speaker 1 produces the complete clause "rezultat...je bil...isti" (the result was the same). Speaker 2 says "slab" (bad) — a different characterization of the same referent (the result). Both "isti" and "slab" target the same predicative slot. Per the PDF, this is reformulation → `conj:reform`, not plain `conj`.

Change: Coconstruct on s408:1 (slab) from `conj` → `conj:reform`. Anchor (s407::19 = isti) is correct.

```conllu
# sent_id = Gos020.s407
# speaker_id = Mf-prof-01061
# sound_url = https://nl.ijs.si/project/gos20/Gos020/Gos020.s407.mp3
# text = se pravi , rezultat za Žide je bil , v katerem koli taborišču že so se znašli , isti
1	se	se	PRON	Px------y	PronType=Prs|Reflex=Yes|Variant=Short	19	cc	_	pronunciation=se|Gos2.1_token_id=Gos020.tok3097
2	pravi	praviti	VERB	Vmbr3s	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	1	fixed	_	pronunciation=pravi|Gos2.1_token_id=Gos020.tok3098
3	,	,	PUNCT	Z	_	1	punct	_	_
4	rezultat	rezultat	NOUN	Ncmsn	Case=Nom|Gender=Masc|Number=Sing	19	nsubj	_	pronunciation=rezultat|Gos2.1_token_id=Gos020.tok3099
5	za	za	ADP	Sa	Case=Acc	6	case	_	pronunciation=za|Gos2.1_token_id=Gos020.tok3100
6	Žide	Žid	PROPN	Npmpa	Case=Acc|Gender=Masc|Number=Plur	19	obl	_	pronunciation=Žide|Gos2.1_token_id=Gos020.tok3101
7	je	biti	AUX	Va-r3s-n	Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin	19	aux	_	pronunciation=je|Gos2.1_token_id=Gos020.tok3102
8	bil	biti	AUX	Va-p-sm	Gender=Masc|Number=Sing|VerbForm=Part	19	cop	_	pronunciation=bil|Gos2.1_token_id=Gos020.tok3103
9	,	,	PUNCT	Z	_	17	punct	_	_
10	v	v	ADP	Sl	Case=Loc	13	case	_	pronunciation=v|Gos2.1_token_id=Gos020.tok3104
11	katerem	kateri	DET	Pq-nsl	Case=Loc|Gender=Neut|Number=Sing|PronType=Int	13	det	_	pronunciation=kateremkolu|Gos2.1_token_id=Gos020.tok3105n1
12	koli	koli	PART	Q	_	11	fixed	_	pronunciation=kateremkolu|Gos2.1_token_id=Gos020.tok3105n2
13	taborišču	taborišče	NOUN	Ncnsl	Case=Loc|Gender=Neut|Number=Sing	17	obl	_	pronunciation=taborišču|Gos2.1_token_id=Gos020.tok3106
14	že	že	PART	Q	_	13	advmod	_	pronunciation=že|Gos2.1_token_id=Gos020.tok3107
15	so	biti	AUX	Va-r3p-n	Mood=Ind|Number=Plur|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin	17	aux	_	pronunciation=so|Gos2.1_token_id=Gos020.tok3108
16	se	se	PRON	Px------y	PronType=Prs|Reflex=Yes|Variant=Short	17	expl	_	pronunciation=se|Gos2.1_token_id=Gos020.tok3109
17	znašli	znajti	VERB	Vmep-pm	Aspect=Perf|Gender=Masc|Number=Plur|VerbForm=Part	19	advcl	_	pronunciation=znašli|Gos2.1_token_id=Gos020.tok3110
18	,	,	PUNCT	Z	_	17	punct	_	_
19	isti	isti	DET	Pi-msn	Case=Nom|Gender=Masc|Number=Sing|PronType=Ind	0	root	_	pronunciation=isti|Gos2.1_token_id=Gos020.tok3111

# sent_id = Gos020.s408
# speaker_id = Jm-ucen-01064
# sound_url = https://nl.ijs.si/project/gos20/Gos020/Gos020.s408.mp3
# text = slab .
1	slab	slab	ADJ	Agpmsnn	Case=Nom|Definite=Ind|Degree=Pos|Gender=Masc|Number=Sing	0	root	_	pronunciation=slab|Gos2.1_token_id=Gos020.tok3112|Coconstruct=conj:reform::Gos020.s407::19
2	.	.	PUNCT	Z	_	1	punct	_	_
```

# coco_04

## current

```conllu
# sent_id = Gos021.s149
# speaker_id = Sf-prof-01049
# sound_url = https://nl.ijs.si/project/gos20/Gos021/Gos021.s149.mp3
# text = prej je bil moder , polovica je še vedno moder , ostala polovica pa je že
1	prej	prej	ADV	Rgc	Degree=Cmp	4	advmod	_	pronunciation=prej|Gos2.1_token_id=Gos021.tok859
2	je	biti	AUX	Va-r3s-n	Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin	4	aux	_	pronunciation=je|Gos2.1_token_id=Gos021.tok860
3	bil	biti	AUX	Va-p-sm	Gender=Masc|Number=Sing|VerbForm=Part	4	cop	_	pronunciation=bil|Gos2.1_token_id=Gos021.tok861
4	moder	moder	ADJ	Agpmsnn	Case=Nom|Definite=Ind|Degree=Pos|Gender=Masc|Number=Sing	0	root	_	pronunciation=moder|Gos2.1_token_id=Gos021.tok862
5	,	,	PUNCT	Z	_	10	punct	_	_
6	polovica	polovica	NOUN	Ncfsn	Case=Nom|Gender=Fem|Number=Sing	10	nsubj	_	pronunciation=polovica|Gos2.1_token_id=Gos021.tok863
7	je	biti	AUX	Va-r3s-n	Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin	10	cop	_	pronunciation=je|Gos2.1_token_id=Gos021.tok864
8	še	še	PART	Q	_	10	advmod	_	pronunciation=še|Gos2.1_token_id=Gos021.tok865
9	vedno	vedno	ADV	Rgp	Degree=Pos	10	advmod	_	pronunciation=vedno|Gos2.1_token_id=Gos021.tok866
10	moder	moder	ADJ	Agpmsnn	Case=Nom|Definite=Ind|Degree=Pos|Gender=Masc|Number=Sing	4	parataxis	_	pronunciation=moder|Gos2.1_token_id=Gos021.tok867
11	,	,	PUNCT	Z	_	15	punct	_	_
12	ostala	ostal	ADJ	Appfsn	Case=Nom|Degree=Pos|Gender=Fem|Number=Sing|VerbForm=Part	13	amod	_	pronunciation=ostala|Gos2.1_token_id=Gos021.tok868
13	polovica	polovica	NOUN	Ncfsn	Case=Nom|Gender=Fem|Number=Sing	15	nsubj	_	pronunciation=polovica|Gos2.1_token_id=Gos021.tok869|Coconstruct=nsubj::Gos021.s150::1
14	pa	pa	CCONJ	Cc	_	15	advmod	_	pronunciation=pa|Gos2.1_token_id=Gos021.tok870|Coconstruct=advmod::Gos021.s150::1
15	je	biti	VERB	Va-r3s-n	Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin	10	parataxis	_	pronunciation=je|Gos2.1_token_id=Gos021.tok871|Coconstruct=cop::Gos021.s150::1
16	že	že	PART	Q	_	15	advmod	_	pronunciation=že|Gos2.1_token_id=Gos021.tok872|Coconstruct=advmod::Gos021.s150::1

# sent_id = Gos021.s150
# speaker_id = Pn-vsiucenci-10000
# sound_url = https://nl.ijs.si/project/gos20/Gos021/Gos021.s150.mp3
# text = rdeča .
1	rdeča	rdeč	ADJ	Agpfsn	Case=Nom|Degree=Pos|Gender=Fem|Number=Sing	0	root	_	pronunciation=rdeča|Gos2.1_token_id=Gos021.tok873|Coconstruct=parataxis::Gos021.s149::4
2	.	.	PUNCT	Z	_	1	punct	_	_
```

## proposed

This is 4.1 Completion of an Open Dependency Slot. Speaker 1 says "ostala polovica pa je že [missing adjective]" — token 15 (je, VERB, head of the third clause) projects the missing predicative complement. Speaker 2 provides "rdeča" (red) to fill that slot.

Changes vs. the original current:
- Remove Coconstruct from s149 tokens 13, 14, 15, 16 (forward pointers — wrong direction)
- Fix Coconstruct on rdeča: anchor changes from token 4 (moder, unrelated first clause) → token 15 (je, the verbal head of the unfinished clause); relation changes from parataxis → xcomp (the slot rdeča fills in Speaker 1's structure)

```conllu
# sent_id = Gos021.s149
# speaker_id = Sf-prof-01049
# sound_url = https://nl.ijs.si/project/gos20/Gos021/Gos021.s149.mp3
# text = prej je bil moder , polovica je še vedno moder , ostala polovica pa je že
1	prej	prej	ADV	Rgc	Degree=Cmp	4	advmod	_	pronunciation=prej|Gos2.1_token_id=Gos021.tok859
2	je	biti	AUX	Va-r3s-n	Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin	4	aux	_	pronunciation=je|Gos2.1_token_id=Gos021.tok860
3	bil	biti	AUX	Va-p-sm	Gender=Masc|Number=Sing|VerbForm=Part	4	cop	_	pronunciation=bil|Gos2.1_token_id=Gos021.tok861
4	moder	moder	ADJ	Agpmsnn	Case=Nom|Definite=Ind|Degree=Pos|Gender=Masc|Number=Sing	0	root	_	pronunciation=moder|Gos2.1_token_id=Gos021.tok862
5	,	,	PUNCT	Z	_	10	punct	_	_
6	polovica	polovica	NOUN	Ncfsn	Case=Nom|Gender=Fem|Number=Sing	10	nsubj	_	pronunciation=polovica|Gos2.1_token_id=Gos021.tok863
7	je	biti	AUX	Va-r3s-n	Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin	10	cop	_	pronunciation=je|Gos2.1_token_id=Gos021.tok864
8	še	še	PART	Q	_	10	advmod	_	pronunciation=še|Gos2.1_token_id=Gos021.tok865
9	vedno	vedno	ADV	Rgp	Degree=Pos	10	advmod	_	pronunciation=vedno|Gos2.1_token_id=Gos021.tok866
10	moder	moder	ADJ	Agpmsnn	Case=Nom|Definite=Ind|Degree=Pos|Gender=Masc|Number=Sing	4	parataxis	_	pronunciation=moder|Gos2.1_token_id=Gos021.tok867
11	,	,	PUNCT	Z	_	15	punct	_	_
12	ostala	ostal	ADJ	Appfsn	Case=Nom|Degree=Pos|Gender=Fem|Number=Sing|VerbForm=Part	13	amod	_	pronunciation=ostala|Gos2.1_token_id=Gos021.tok868
13	polovica	polovica	NOUN	Ncfsn	Case=Nom|Gender=Fem|Number=Sing	15	nsubj	_	pronunciation=polovica|Gos2.1_token_id=Gos021.tok869
14	pa	pa	CCONJ	Cc	_	15	advmod	_	pronunciation=pa|Gos2.1_token_id=Gos021.tok870
15	je	biti	VERB	Va-r3s-n	Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin	10	parataxis	_	pronunciation=je|Gos2.1_token_id=Gos021.tok871
16	že	že	PART	Q	_	15	advmod	_	pronunciation=že|Gos2.1_token_id=Gos021.tok872

# sent_id = Gos021.s150
# speaker_id = Pn-vsiucenci-10000
# sound_url = https://nl.ijs.si/project/gos20/Gos021/Gos021.s150.mp3
# text = rdeča .
1	rdeča	rdeč	ADJ	Agpfsn	Case=Nom|Degree=Pos|Gender=Fem|Number=Sing	0	root	_	pronunciation=rdeča|Gos2.1_token_id=Gos021.tok873|Coconstruct=xcomp::Gos021.s149::15
2	.	.	PUNCT	Z	_	1	punct	_	_
```

# coco_05

## current

```conllu
# sent_id = Gos045.s301
# speaker_id = Cm-gost-02143
# sound_url = https://nl.ijs.si/project/gos20/Gos045/Gos045.s301.mp3
# text = glejte , zdaj ne vem , koliko jih v- , jih je bilo takrat prisotnih na tem , eee , krpanju , ampak skušamo vse zadevo
1	glejte	gledati	VERB	Vmpm2p	Aspect=Imp|Mood=Imp|Number=Plur|Person=2|VerbForm=Fin	5	parataxis:discourse	_	pronunciation=glejte|Gos2.1_token_id=Gos045.tok3567
2	,	,	PUNCT	Z	_	1	punct	_	_
3	zdaj	zdaj	ADV	Rgp	Degree=Pos	5	discourse	_	pronunciation=zdaj|Gos2.1_token_id=Gos045.tok3568
4	ne	ne	PART	Q	Polarity=Neg	5	advmod	_	pronunciation=ne|Gos2.1_token_id=Gos045.tok3569
5	vem	vedeti	VERB	Vmpr1s	Aspect=Imp|Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=vem|Gos2.1_token_id=Gos045.tok3570
6	,	,	PUNCT	Z	_	15	punct	_	_
7	koliko	koliko	DET	Rgp	PronType=Int	11	det	_	pronunciation=koliko|Gos2.1_token_id=Gos045.tok3571
8	jih	on	PRON	Pp3mpg--y	Case=Gen|Gender=Masc|Number=Plur|Person=3|PronType=Prs|Variant=Short	11	reparandum	_	pronunciation=jih|Gos2.1_token_id=Gos045.tok3572
9	v-	v-	X	Xt	_	11	reparandum	_	pronunciation=v…|Gos2.1_token_id=Gos045.tok3573
10	,	,	PUNCT	Z	_	9	punct	_	_
11	jih	on	PRON	Pp3mpg--y	Case=Gen|Gender=Masc|Number=Plur|Person=3|PronType=Prs|Variant=Short	15	nsubj	_	pronunciation=jih|Gos2.1_token_id=Gos045.tok3574
12	je	biti	AUX	Va-r3s-n	Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin	15	aux	_	pronunciation=je|Gos2.1_token_id=Gos045.tok3575
13	bilo	biti	AUX	Va-p-sn	Gender=Neut|Number=Sing|VerbForm=Part	15	cop	_	pronunciation=blo|Gos2.1_token_id=Gos045.tok3576
14	takrat	takrat	ADV	Rgp	Degree=Pos	15	advmod	_	pronunciation=takrat|Gos2.1_token_id=Gos045.tok3577
15	prisotnih	prisoten	ADJ	Agpmpg	Case=Gen|Degree=Pos|Gender=Masc|Number=Plur	5	ccomp	_	pronunciation=prisotnih|Gos2.1_token_id=Gos045.tok3578
16	na	na	ADP	Sl	Case=Loc	21	case	_	pronunciation=na|Gos2.1_token_id=Gos045.tok3579
17	tem	ta	DET	Pd-nsl	Case=Loc|Gender=Neut|Number=Sing|PronType=Dem	21	det	_	pronunciation=tem|Gos2.1_token_id=Gos045.tok3580
18	,	,	PUNCT	Z	_	19	punct	_	_
19	eee	eee	INTJ	I	_	15	discourse:filler	_	pronunciation=eee|Gos2.1_token_id=Gos045.tok3581
20	,	,	PUNCT	Z	_	19	punct	_	_
21	krpanju	krpanje	NOUN	Ncnsl	Case=Loc|Gender=Neut|Number=Sing	15	obl	_	pronunciation=krpanju|Gos2.1_token_id=Gos045.tok3582
22	,	,	PUNCT	Z	_	15	punct	_	_
23	ampak	ampak	CCONJ	Cc	_	24	cc	_	pronunciation=ampak|Gos2.1_token_id=Gos045.tok3583
24	skušamo	skušati	VERB	Vmpr1p	Aspect=Imp|Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin	5	conj	_	pronunciation=skušamo|Gos2.1_token_id=Gos045.tok3584
25	vse	ves	DET	Pg-nsa	Case=Acc|Gender=Neut|Number=Sing|PronType=Tot	26	det	_	pronunciation=vse|Gos2.1_token_id=Gos045.tok3585
26	zadevo	zadeva	NOUN	Ncfsa	Case=Acc|Gender=Fem|Number=Sing	24	obj	_	pronunciation=zadevo|Gos2.1_token_id=Gos045.tok3586

# sent_id = Gos045.s302
# speaker_id = Af-mode-02141
# sound_url = https://nl.ijs.si/project/gos20/Gos045/Gos045.s302.mp3
# text = na generalno gledati na racionalnost , eee , izkušnje so , če gledamo , kaj delate izvajalci po Sloveniji , kar , eee , takšne , da moramo biti zelo previdni .
1	na	na	ADP	Sa	Case=Acc	2	reparandum	_	pronunciation=na|Gos2.1_token_id=Gos045.tok3587
2	generalno	generalno	ADV	Rgp	Degree=Pos	3	advmod	_	pronunciation=generalno|Gos2.1_token_id=Gos045.tok3588
3	gledati	gledati	VERB	Vmpn	Aspect=Imp|VerbForm=Inf	0	root	_	pronunciation=gledat|Gos2.1_token_id=Gos045.tok3589|Coconstruct=xcomp::Gos045.s301::24
4	na	na	ADP	Sa	Case=Acc	5	case	_	pronunciation=na|Gos2.1_token_id=Gos045.tok3590
5	racionalnost	racionalnost	NOUN	Ncfsa	Case=Acc|Gender=Fem|Number=Sing	3	obl	_	pronunciation=racionalnost|Gos2.1_token_id=Gos045.tok3591
6	,	,	PUNCT	Z	_	25	punct	_	_
7	eee	eee	INTJ	I	_	25	discourse:filler	_	pronunciation=eee|Gos2.1_token_id=Gos045.tok3592
8	,	,	PUNCT	Z	_	7	punct	_	_
9	izkušnje	izkušnja	NOUN	Ncfpn	Case=Nom|Gender=Fem|Number=Plur	25	nsubj	_	pronunciation=izkušne|Gos2.1_token_id=Gos045.tok3593
10	so	biti	AUX	Va-r3p-n	Mood=Ind|Number=Plur|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin	25	cop	_	pronunciation=so|Gos2.1_token_id=Gos045.tok3594
11	,	,	PUNCT	Z	_	13	punct	_	_
12	če	če	SCONJ	Cs	_	13	mark	_	pronunciation=če|Gos2.1_token_id=Gos045.tok3595
13	gledamo	gledati	VERB	Vmpr1p	Aspect=Imp|Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin	25	advcl	_	pronunciation=gledamo|Gos2.1_token_id=Gos045.tok3596
14	,	,	PUNCT	Z	_	16	punct	_	_
15	kaj	kaj	PRON	Pq-nsa	Case=Acc|Gender=Neut|Number=Sing|PronType=Int	16	obj	_	pronunciation=kaj|Gos2.1_token_id=Gos045.tok3597
16	delate	delati	VERB	Vmpr2p	Aspect=Imp|Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin	13	ccomp	_	pronunciation=delate|Gos2.1_token_id=Gos045.tok3598
17	izvajalci	izvajalec	NOUN	Ncmpn	Case=Nom|Gender=Masc|Number=Plur	16	nsubj	_	pronunciation=izvajalci|Gos2.1_token_id=Gos045.tok3599
18	po	po	ADP	Sl	Case=Loc	19	case	_	pronunciation=po|Gos2.1_token_id=Gos045.tok3600
19	Sloveniji	Slovenija	PROPN	Npfsl	Case=Loc|Gender=Fem|Number=Sing	17	nmod	_	pronunciation=Sloveniji|Gos2.1_token_id=Gos045.tok3601
20	,	,	PUNCT	Z	_	16	punct	_	_
21	kar	kar	ADV	Rgp	Degree=Pos	25	advmod	_	pronunciation=kr|Gos2.1_token_id=Gos045.tok3602
22	,	,	PUNCT	Z	_	23	punct	_	_
23	eee	eee	INTJ	I	_	25	discourse:filler	_	pronunciation=eee|Gos2.1_token_id=Gos045.tok3603
24	,	,	PUNCT	Z	_	23	punct	_	_
25	takšne	takšen	DET	Pd-fpn	Case=Nom|Gender=Fem|Number=Plur|PronType=Dem	3	parataxis	_	pronunciation=takšne|Gos2.1_token_id=Gos045.tok3604
26	,	,	PUNCT	Z	_	28	punct	_	_
27	da	da	SCONJ	Cs	_	28	mark	_	pronunciation=da|Gos2.1_token_id=Gos045.tok3605
28	moramo	morati	VERB	Vmpr1p	Aspect=Imp|Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin	25	acl	_	pronunciation=moramo|Gos2.1_token_id=Gos045.tok3606
29	biti	biti	AUX	Va-n	VerbForm=Inf	31	cop	_	pronunciation=bit|Gos2.1_token_id=Gos045.tok3607
30	zelo	zelo	ADV	Rgp	Degree=Pos	31	advmod	_	pronunciation=zelo|Gos2.1_token_id=Gos045.tok3608
31	previdni	previden	ADJ	Agpmpn	Case=Nom|Degree=Pos|Gender=Masc|Number=Plur	28	xcomp	_	pronunciation=previdni|Gos2.1_token_id=Gos045.tok3609
32	.	.	PUNCT	Z	_	3	punct	_	_
```

## proposed

Annotation is correct as-is. This is 4.1 Completion: Speaker 1 says "skušamo vse zadevo" (we're trying everything) — skušamo (token 24) projects an unrealized xcomp infinitive. Speaker 2 provides "gledati" (to look at it). Coconstruct=xcomp::Gos045.s301::24 on gledati correctly points back to skušamo with the right relation. No forward pointers on Speaker 1. No changes needed.

# coco_06

## current

```conllu
# sent_id = Gos053.s461
# speaker_id = Af-prof-07037
# sound_url = https://nl.ijs.si/project/gos20/Gos053/Gos053.s461.mp3
# text = če atom odda elektrone , nastane
1	če	če	SCONJ	Cs	_	3	mark	_	pronunciation=če|Gos2.1_token_id=Gos053.tok2974
2	atom	atom	NOUN	Ncmsn	Case=Nom|Gender=Masc|Number=Sing	3	nsubj	_	pronunciation=atom|Gos2.1_token_id=Gos053.tok2975
3	odda	oddati	VERB	Vmer3s	Aspect=Perf|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	6	advcl	_	pronunciation=odda|Gos2.1_token_id=Gos053.tok2976
4	elektrone	elektron	NOUN	Ncmpa	Case=Acc|Gender=Masc|Number=Plur	3	obj	_	pronunciation=elektrone|Gos2.1_token_id=Gos053.tok2977
5	,	,	PUNCT	Z	_	3	punct	_	_
6	nastane	nastati	VERB	Vmer3s	Aspect=Perf|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=nastane|Gos2.1_token_id=Gos053.tok2978

# sent_id = Gos053.s462
# speaker_id = Dm-ucen-07041
# sound_url = https://nl.ijs.si/project/gos20/Gos053/Gos053.s462.mp3
# text = kation .
1	kation	kation	NOUN	Ncmsn	Case=Nom|Gender=Masc|Number=Sing	0	root	_	pronunciation=kation|Gos2.1_token_id=Gos053.tok2979|Coconstruct=nsubj::Gos053.s461::6
2	.	.	PUNCT	Z	_	1	punct	_	_
```

## proposed

```conllu
# sent_id = Gos053.s461
# speaker_id = Af-prof-07037
# sound_url = https://nl.ijs.si/project/gos20/Gos053/Gos053.s461.mp3
# text = če atom odda elektrone , nastane
1	če	če	SCONJ	Cs	_	3	mark	_	pronunciation=če|Gos2.1_token_id=Gos053.tok2974
2	atom	atom	NOUN	Ncmsn	Case=Nom|Gender=Masc|Number=Sing	3	nsubj	_	pronunciation=atom|Gos2.1_token_id=Gos053.tok2975
3	odda	oddati	VERB	Vmer3s	Aspect=Perf|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	6	advcl	_	pronunciation=odda|Gos2.1_token_id=Gos053.tok2976
4	elektrone	elektron	NOUN	Ncmpa	Case=Acc|Gender=Masc|Number=Plur	3	obj	_	pronunciation=elektrone|Gos2.1_token_id=Gos053.tok2977
5	,	,	PUNCT	Z	_	3	punct	_	_
6	nastane	nastati	VERB	Vmer3s	Aspect=Perf|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=nastane|Gos2.1_token_id=Gos053.tok2978

# sent_id = Gos053.s462
# speaker_id = Dm-ucen-07041
# sound_url = https://nl.ijs.si/project/gos20/Gos053/Gos053.s462.mp3
# text = kation .
1	kation	kation	NOUN	Ncmsn	Case=Nom|Gender=Masc|Number=Sing	0	root	_	pronunciation=kation|Gos2.1_token_id=Gos053.tok2979|Coconstruct=nsubj::Gos053.s461::6
2	.	.	PUNCT	Z	_	1	punct	_	_
```

# coco_07

## current

```conllu
# sent_id = Gos190.s165
# speaker_id = Cf-stra-02265
# sound_url = https://nl.ijs.si/project/gos20/Gos190/Gos190.s165.mp3
# text = ker jaz sem , ej , zdaj pa še mi samo povej , jaz imam družinsko srečo , saj veš , že
1	ker	ker	SCONJ	Cs	_	3	mark	_	pronunciation=ker|Gos2.1_token_id=Gos190.tok963
2	jaz	jaz	PRON	Pp1-sn	Case=Nom|Number=Sing|Person=1|PronType=Prs	3	nsubj	_	pronunciation=jaz|Gos2.1_token_id=Gos190.tok964
3	sem	biti	VERB	Va-r1s-n	Mood=Ind|Number=Sing|Person=1|Polarity=Pos|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=sn|Gos2.1_token_id=Gos190.tok965
4	,	,	PUNCT	Z	_	5	punct	_	_
5	ej	ej	INTJ	I	_	12	discourse	_	pronunciation=ej|Gos2.1_token_id=Gos190.tok966
6	,	,	PUNCT	Z	_	5	punct	_	_
7	zdaj	zdaj	ADV	Rgp	Degree=Pos	12	advmod	_	pronunciation=zaj|Gos2.1_token_id=Gos190.tok967
8	pa	pa	CCONJ	Cc	_	12	advmod	_	pronunciation=pa|Gos2.1_token_id=Gos190.tok968
9	še	še	PART	Q	_	12	advmod	_	pronunciation=še|Gos2.1_token_id=Gos190.tok969
10	mi	jaz	PRON	Pp1-sd--y	Case=Dat|Number=Sing|Person=1|PronType=Prs|Variant=Short	12	iobj	_	pronunciation=mi|Gos2.1_token_id=Gos190.tok970
11	samo	samo	PART	Q	_	12	advmod	_	pronunciation=samo|Gos2.1_token_id=Gos190.tok971
12	povej	povedati	VERB	Vmem2s	Aspect=Perf|Mood=Imp|Number=Sing|Person=2|VerbForm=Fin	3	parataxis:restart	_	pronunciation=povej|Gos2.1_token_id=Gos190.tok972
13	,	,	PUNCT	Z	_	15	punct	_	_
14	jaz	jaz	PRON	Pp1-sn	Case=Nom|Number=Sing|Person=1|PronType=Prs	15	nsubj	_	pronunciation=jez|Gos2.1_token_id=Gos190.tok973
15	imam	imeti	VERB	Vmpr1s-n	Aspect=Imp|Mood=Ind|Number=Sing|Person=1|Polarity=Pos|Tense=Pres|VerbForm=Fin	12	parataxis	_	pronunciation=mam|Gos2.1_token_id=Gos190.tok974
16	družinsko	družinski	ADJ	Agpfsa	Case=Acc|Degree=Pos|Gender=Fem|Number=Sing	17	amod	_	pronunciation=družinsko|Gos2.1_token_id=Gos190.tok975
17	srečo	sreča	NOUN	Ncfsa	Case=Acc|Gender=Fem|Number=Sing	15	obj	_	pronunciation=srečo|Gos2.1_token_id=Gos190.tok976
18	,	,	PUNCT	Z	_	20	punct	_	_
19	saj	saj	CCONJ	Cc	_	20	cc	_	pronunciation=se|Gos2.1_token_id=Gos190.tok977
20	veš	vedeti	VERB	Vmpr2s	Aspect=Imp|Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin	15	parataxis	_	pronunciation=veš|Gos2.1_token_id=Gos190.tok978
21	,	,	PUNCT	Z	_	22	punct	_	_
22	že	že	PART	Q	_	20	advmod	_	pronunciation=že|Gos2.1_token_id=Gos190.tok979|Coconstruct=advmod::Gos190.s167::2

# sent_id = Gos190.s167
# speaker_id = Af-stra-02276
# sound_url = https://nl.ijs.si/project/gos20/Gos190/Gos190.s167.mp3
# text = par let .
1	par	par	DET	Rgp	PronType=Ind	2	det	_	pronunciation=por|Gos2.1_token_id=Gos190.tok980
2	let	leto	NOUN	Ncnpg	Case=Gen|Gender=Neut|Number=Plur	0	root	_	pronunciation=let|Gos2.1_token_id=Gos190.tok981|Coconstruct=obl::Gos190.s165::15
3	.	.	PUNCT	Z	_	2	punct	_	_
```

## proposed

This is 4.1 Completion: Speaker 1 says "jaz imam družinsko srečo...že" — imam (token 15) projects an unrealized obl duration slot ("for X years"). Speaker 2 provides "par let" (a few years). Coconstruct=obl::Gos190.s165::15 on let correctly points back to imam with the right relation.

Change: Remove Coconstruct from s165 token 22 (že) — it's a forward pointer on Speaker 1's token, which violates the rule. Speaker 2's let (s167:2) already has the correct backward pointer. No other changes.

```conllu
# sent_id = Gos190.s165
# speaker_id = Cf-stra-02265
# sound_url = https://nl.ijs.si/project/gos20/Gos190/Gos190.s165.mp3
# text = ker jaz sem , ej , zdaj pa še mi samo povej , jaz imam družinsko srečo , saj veš , že
1	ker	ker	SCONJ	Cs	_	3	mark	_	pronunciation=ker|Gos2.1_token_id=Gos190.tok963
2	jaz	jaz	PRON	Pp1-sn	Case=Nom|Number=Sing|Person=1|PronType=Prs	3	nsubj	_	pronunciation=jaz|Gos2.1_token_id=Gos190.tok964
3	sem	biti	VERB	Va-r1s-n	Mood=Ind|Number=Sing|Person=1|Polarity=Pos|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=sn|Gos2.1_token_id=Gos190.tok965
4	,	,	PUNCT	Z	_	5	punct	_	_
5	ej	ej	INTJ	I	_	12	discourse	_	pronunciation=ej|Gos2.1_token_id=Gos190.tok966
6	,	,	PUNCT	Z	_	5	punct	_	_
7	zdaj	zdaj	ADV	Rgp	Degree=Pos	12	advmod	_	pronunciation=zaj|Gos2.1_token_id=Gos190.tok967
8	pa	pa	CCONJ	Cc	_	12	advmod	_	pronunciation=pa|Gos2.1_token_id=Gos190.tok968
9	še	še	PART	Q	_	12	advmod	_	pronunciation=še|Gos2.1_token_id=Gos190.tok969
10	mi	jaz	PRON	Pp1-sd--y	Case=Dat|Number=Sing|Person=1|PronType=Prs|Variant=Short	12	iobj	_	pronunciation=mi|Gos2.1_token_id=Gos190.tok970
11	samo	samo	PART	Q	_	12	advmod	_	pronunciation=samo|Gos2.1_token_id=Gos190.tok971
12	povej	povedati	VERB	Vmem2s	Aspect=Perf|Mood=Imp|Number=Sing|Person=2|VerbForm=Fin	3	parataxis:restart	_	pronunciation=povej|Gos2.1_token_id=Gos190.tok972
13	,	,	PUNCT	Z	_	15	punct	_	_
14	jaz	jaz	PRON	Pp1-sn	Case=Nom|Number=Sing|Person=1|PronType=Prs	15	nsubj	_	pronunciation=jez|Gos2.1_token_id=Gos190.tok973
15	imam	imeti	VERB	Vmpr1s-n	Aspect=Imp|Mood=Ind|Number=Sing|Person=1|Polarity=Pos|Tense=Pres|VerbForm=Fin	12	parataxis	_	pronunciation=mam|Gos2.1_token_id=Gos190.tok974
16	družinsko	družinski	ADJ	Agpfsa	Case=Acc|Degree=Pos|Gender=Fem|Number=Sing	17	amod	_	pronunciation=družinsko|Gos2.1_token_id=Gos190.tok975
17	srečo	sreča	NOUN	Ncfsa	Case=Acc|Gender=Fem|Number=Sing	15	obj	_	pronunciation=srečo|Gos2.1_token_id=Gos190.tok976
18	,	,	PUNCT	Z	_	20	punct	_	_
19	saj	saj	CCONJ	Cc	_	20	cc	_	pronunciation=se|Gos2.1_token_id=Gos190.tok977
20	veš	vedeti	VERB	Vmpr2s	Aspect=Imp|Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin	15	parataxis	_	pronunciation=veš|Gos2.1_token_id=Gos190.tok978
21	,	,	PUNCT	Z	_	22	punct	_	_
22	že	že	PART	Q	_	20	advmod	_	pronunciation=že|Gos2.1_token_id=Gos190.tok979

# sent_id = Gos190.s167
# speaker_id = Af-stra-02276
# sound_url = https://nl.ijs.si/project/gos20/Gos190/Gos190.s167.mp3
# text = par let .
1	par	par	DET	Rgp	PronType=Ind	2	det	_	pronunciation=por|Gos2.1_token_id=Gos190.tok980
2	let	leto	NOUN	Ncnpg	Case=Gen|Gender=Neut|Number=Plur	0	root	_	pronunciation=let|Gos2.1_token_id=Gos190.tok981|Coconstruct=obl::Gos190.s165::15
3	.	.	PUNCT	Z	_	2	punct	_	_
```

# coco_08

## current

```conllu
# sent_id = Gos200.s115
# speaker_id = Af-info-05596
# sound_url = https://nl.ijs.si/project/gos20/Gos200/Gos200.s115.mp3
# text = eee , ja , eee , veste kaj , pa tudi najbrž ste gor prebrali , da , eem , je določen rok , mislim , da štirinajst dni
1	eee	eee	INTJ	I	_	15	discourse:filler	_	pronunciation=eee|Gos2.1_token_id=Gos200.tok1117
2	,	,	PUNCT	Z	_	1	punct	_	_
3	ja	ja	PART	Q	_	15	discourse	_	pronunciation=ja|Gos2.1_token_id=Gos200.tok1118
4	,	,	PUNCT	Z	_	3	punct	_	_
5	eee	eee	INTJ	I	_	15	discourse:filler	_	pronunciation=eee|Gos2.1_token_id=Gos200.tok1119
6	,	,	PUNCT	Z	_	5	punct	_	_
7	veste	vedeti	VERB	Vmpr2p	Aspect=Imp|Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin	15	parataxis:discourse	_	pronunciation=veste|Gos2.1_token_id=Gos200.tok1120
8	kaj	kaj	PRON	Pq-nsa	Case=Acc|Gender=Neut|Number=Sing|PronType=Int	7	obj	_	pronunciation=kaj|Gos2.1_token_id=Gos200.tok1121
9	,	,	PUNCT	Z	_	7	punct	_	_
10	pa	pa	CCONJ	Cc	_	15	advmod	_	pronunciation=pa|Gos2.1_token_id=Gos200.tok1122
11	tudi	tudi	PART	Q	_	15	advmod	_	pronunciation=tudi|Gos2.1_token_id=Gos200.tok1123
12	najbrž	najbrž	PART	Q	_	15	advmod	_	pronunciation=najbrž|Gos2.1_token_id=Gos200.tok1124
13	ste	biti	AUX	Va-r2p-n	Mood=Ind|Number=Plur|Person=2|Polarity=Pos|Tense=Pres|VerbForm=Fin	15	aux	_	pronunciation=ste|Gos2.1_token_id=Gos200.tok1125
14	gor	gor	ADV	Rgp	Degree=Pos	15	advmod	_	pronunciation=gor|Gos2.1_token_id=Gos200.tok1126
15	prebrali	prebrati	VERB	Vmep-pm	Aspect=Perf|Gender=Masc|Number=Plur|VerbForm=Part	0	root	_	pronunciation=prebrali|Gos2.1_token_id=Gos200.tok1127
16	,	,	PUNCT	Z	_	23	punct	_	_
17	da	da	SCONJ	Cs	_	23	mark	_	pronunciation=da|Gos2.1_token_id=Gos200.tok1128
18	,	,	PUNCT	Z	_	19	punct	_	_
19	eem	eem	INTJ	I	_	23	discourse:filler	_	pronunciation=eem|Gos2.1_token_id=Gos200.tok1129
20	,	,	PUNCT	Z	_	19	punct	_	_
21	je	biti	AUX	Va-r3s-n	Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin	23	cop	_	pronunciation=je|Gos2.1_token_id=Gos200.tok1130
22	določen	določen	ADJ	Appmsnn	Case=Nom|Definite=Ind|Degree=Pos|Gender=Masc|Number=Sing|VerbForm=Part	23	amod	_	pronunciation=določen|Gos2.1_token_id=Gos200.tok1131
23	rok	rok	NOUN	Ncmsn	Case=Nom|Gender=Masc|Number=Sing	15	ccomp	_	pronunciation=rok|Gos2.1_token_id=Gos200.tok1132
24	,	,	PUNCT	Z	_	25	punct	_	_
25	mislim	misliti	VERB	Vmpr1s	Aspect=Imp|Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	23	parataxis	_	pronunciation=mislim|Gos2.1_token_id=Gos200.tok1133
26	,	,	PUNCT	Z	_	29	punct	_	_
27	da	da	SCONJ	Cs	_	29	mark	_	pronunciation=da|Gos2.1_token_id=Gos200.tok1134
28	štirinajst	štirinajst	NUM	Mlc-pa	Case=Acc|Number=Plur|NumForm=Word|NumType=Card	29	nummod	_	pronunciation=štirinajst|Gos2.1_token_id=Gos200.tok1135
29	dni	dan	NOUN	Ncmpg	Case=Gen|Gender=Masc|Number=Plur	25	ccomp	_	pronunciation=dni|Gos2.1_token_id=Gos200.tok1136

# sent_id = Gos200.s116
# speaker_id = Bm-klic-02237
# sound_url = https://nl.ijs.si/project/gos20/Gos200/Gos200.s116.mp3
# text = aha , v katerem
1	aha	aha	INTJ	I	_	4	discourse	_	pronunciation=aha|Gos2.1_token_id=Gos200.tok1137
2	,	,	PUNCT	Z	_	1	punct	_	_
3	v	v	ADP	Sl	Case=Loc	4	case	_	pronunciation=v|Gos2.1_token_id=Gos200.tok1138
4	katerem	kateri	DET	Pq-msl	Case=Loc|Gender=Masc|Number=Sing|PronType=Int	0	root	_	pronunciation=katerem|Gos2.1_token_id=Gos200.tok1139|Coconstruct=acl::Gos200.s115::23
```

## proposed

BORDERLINE CASE. Speaker 1's sentence ("je določen rok, mislim, da štirinajst dni") is syntactically complete — rok does not have an unrealized acl projected within it. Speaker 2 says "aha, v katerem" (in which [month?]) — this is a clarifying question, not a syntactic completion of an open slot. This may not qualify as a 4.1 coconstruction at all under the PDF's criteria.

If kept: the annotation has no forward pointers on Speaker 1 (which is correct), and the backward pointer on katerem (acl::s115::23 → rok) is formally plausible. No Coconstruct changes strictly required, but the case should be flagged for human review to decide whether to keep or remove the Coconstruct link entirely.

# coco_09

## current

```conllu
# sent_id = Gos233.s364
# speaker_id = Tm-otro-03016
# sound_url = https://nl.ijs.si/project/gos20/Gos233/Gos233.s364.mp3
# text = ne , ta naša samohodka je kriza , ker
1	ne	ne	PART	Q	Polarity=Neg	7	discourse	_	pronunciation=ne|Gos2.1_token_id=Gos233.tok1969
2	,	,	PUNCT	Z	_	1	punct	_	_
3	ta	ta	DET	Pd-fsn	Case=Nom|Gender=Fem|Number=Sing|PronType=Dem	5	det	_	pronunciation=ta|Gos2.1_token_id=Gos233.tok1970
4	naša	naš	DET	Ps1fsnp	Case=Nom|Gender=Fem|Number=Sing|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs	5	det	_	pronunciation=naša|Gos2.1_token_id=Gos233.tok1971
5	samohodka	samohodka	NOUN	Ncfsn	Case=Nom|Gender=Fem|Number=Sing	7	nsubj	_	pronunciation=samohodka|Gos2.1_token_id=Gos233.tok1972
6	je	biti	AUX	Va-r3s-n	Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin	7	cop	_	pronunciation=je|Gos2.1_token_id=Gos233.tok1973
7	kriza	kriza	NOUN	Ncfsn	Case=Nom|Gender=Fem|Number=Sing	0	root	_	pronunciation=kriza|Gos2.1_token_id=Gos233.tok1974
8	,	,	PUNCT	Z	_	9	punct	_	_
9	ker	ker	SCONJ	Cs	_	7	advcl	_	pronunciation=k|Gos2.1_token_id=Gos233.tok1975|Coconstruct=mark::Gos233.s366::2

# sent_id = Gos233.s366
# speaker_id = Bm-star-03014
# sound_url = https://nl.ijs.si/project/gos20/Gos233/Gos233.s366.mp3
# text = vse raztepe pa razm- , ostane na tleh .
1	vse	ves	DET	Pg-nsa	Case=Acc|Gender=Neut|Number=Sing|PronType=Tot	2	obj	_	pronunciation=vse|Gos2.1_token_id=Gos233.tok1976
2	raztepe	raztepsti	VERB	Vmer3s	Aspect=Perf|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=raztepe|Gos2.1_token_id=Gos233.tok1977|Coconstruct=advcl::Gos233.s364::7
3	pa	pa	CCONJ	Cc	_	6	cc	_	pronunciation=pa|Gos2.1_token_id=Gos233.tok1978
4	razm-	razm-	X	Xt	_	6	reparandum	_	pronunciation=razm…|Gos2.1_token_id=Gos233.tok1979
5	,	,	PUNCT	Z	_	4	punct	_	_
6	ostane	ostati	VERB	Vmer3s	Aspect=Perf|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	2	conj	_	pronunciation=ostane|Gos2.1_token_id=Gos233.tok1980
7	na	na	ADP	Sl	Case=Loc	8	case	_	pronunciation=na|Gos2.1_token_id=Gos233.tok1981
8	tleh	tla	NOUN	Ncnpl	Case=Loc|Gender=Neut|Number=Plur	6	obl	_	pronunciation=tleh|Gos2.1_token_id=Gos233.tok1982
9	.	.	PUNCT	Z	_	2	punct	_	_
```

## proposed

This is 4.1 Completion: Speaker 1 says "ta naša samohodka je kriza, ker" — ker (SCONJ) opens an advcl clause that remains unrealized. Speaker 2 provides the body: "vse raztepe pa ostane na tleh" (it scatters everything and stays on the ground). The token that PROJECTS the unrealized advcl is kriza (token 7 of s364), since kriza is the main predicate that takes the because-clause.

Change: Remove Coconstruct from s364 token 9 (ker) — forward pointer on Speaker 1, wrong direction. Speaker 2's raztepe (s366:2) already has the correct backward pointer Coconstruct=advcl::Gos233.s364::7.

```conllu
# sent_id = Gos233.s364
# speaker_id = Tm-otro-03016
# sound_url = https://nl.ijs.si/project/gos20/Gos233/Gos233.s364.mp3
# text = ne , ta naša samohodka je kriza , ker
1	ne	ne	PART	Q	Polarity=Neg	7	discourse	_	pronunciation=ne|Gos2.1_token_id=Gos233.tok1969
2	,	,	PUNCT	Z	_	1	punct	_	_
3	ta	ta	DET	Pd-fsn	Case=Nom|Gender=Fem|Number=Sing|PronType=Dem	5	det	_	pronunciation=ta|Gos2.1_token_id=Gos233.tok1970
4	naša	naš	DET	Ps1fsnp	Case=Nom|Gender=Fem|Number=Sing|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs	5	det	_	pronunciation=naša|Gos2.1_token_id=Gos233.tok1971
5	samohodka	samohodka	NOUN	Ncfsn	Case=Nom|Gender=Fem|Number=Sing	7	nsubj	_	pronunciation=samohodka|Gos2.1_token_id=Gos233.tok1972
6	je	biti	AUX	Va-r3s-n	Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin	7	cop	_	pronunciation=je|Gos2.1_token_id=Gos233.tok1973
7	kriza	kriza	NOUN	Ncfsn	Case=Nom|Gender=Fem|Number=Sing	0	root	_	pronunciation=kriza|Gos2.1_token_id=Gos233.tok1974
8	,	,	PUNCT	Z	_	9	punct	_	_
9	ker	ker	SCONJ	Cs	_	7	advcl	_	pronunciation=k|Gos2.1_token_id=Gos233.tok1975

# sent_id = Gos233.s366
# speaker_id = Bm-star-03014
# sound_url = https://nl.ijs.si/project/gos20/Gos233/Gos233.s366.mp3
# text = vse raztepe pa razm- , ostane na tleh .
1	vse	ves	DET	Pg-nsa	Case=Acc|Gender=Neut|Number=Sing|PronType=Tot	2	obj	_	pronunciation=vse|Gos2.1_token_id=Gos233.tok1976
2	raztepe	raztepsti	VERB	Vmer3s	Aspect=Perf|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=raztepe|Gos2.1_token_id=Gos233.tok1977|Coconstruct=advcl::Gos233.s364::7
3	pa	pa	CCONJ	Cc	_	6	cc	_	pronunciation=pa|Gos2.1_token_id=Gos233.tok1978
4	razm-	razm-	X	Xt	_	6	reparandum	_	pronunciation=razm…|Gos2.1_token_id=Gos233.tok1979
5	,	,	PUNCT	Z	_	4	punct	_	_
6	ostane	ostati	VERB	Vmer3s	Aspect=Perf|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	2	conj	_	pronunciation=ostane|Gos2.1_token_id=Gos233.tok1980
7	na	na	ADP	Sl	Case=Loc	8	case	_	pronunciation=na|Gos2.1_token_id=Gos233.tok1981
8	tleh	tla	NOUN	Ncnpl	Case=Loc|Gender=Neut|Number=Plur	6	obl	_	pronunciation=tleh|Gos2.1_token_id=Gos233.tok1982
9	.	.	PUNCT	Z	_	2	punct	_	_
```

# coco_10

## current

```conllu
# sent_id = Gos233.s388
# speaker_id = Tm-otro-03016
# sound_url = https://nl.ijs.si/project/gos20/Gos233/Gos233.s388.mp3
# text = ja , pa
1	ja	ja	PART	Q	_	3	discourse	_	pronunciation=ja|Gos2.1_token_id=Gos233.tok2068|Coconstruct=discourse::Gos233.s389::1
2	,	,	PUNCT	Z	_	1	punct	_	_
3	pa	pa	CCONJ	Cc	_	0	root	_	pronunciation=pa|Gos2.1_token_id=Gos233.tok2069|Coconstruct=advmod::Gos233.s389::1

# sent_id = Gos233.s389
# speaker_id = Bm-star-03014
# sound_url = https://nl.ijs.si/project/gos20/Gos233/Gos233.s389.mp3
# text = more pobirati .
1	more	moči	VERB	Vmpr3s	Aspect=Imp|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=more|Gos2.1_token_id=Gos233.tok2070|Coconstruct=parataxis::Gos233.s388::3
2	pobirati	pobirati	VERB	Vmpn	Aspect=Imp|VerbForm=Inf	1	xcomp	_	pronunciation=pobirat|Gos2.1_token_id=Gos233.tok2071
3	.	.	PUNCT	Z	_	1	punct	_	_
```

## proposed

This is 4.1 Completion: Speaker 1 produces "ja, pa" (yeah, and/then) — a discourse particle + coordinator fragment with no main verb. Speaker 2 provides "more pobirati" (can pick up) as the completing predicate. Coconstruct=parataxis::Gos233.s388::3 on more (pointing back to pa, the local root of s388) is appropriate at the clause level.

Change: Remove Coconstruct from s388 token 1 (ja) and token 3 (pa) — both are forward pointers on Speaker 1, wrong direction. Speaker 2's more already has the correct backward pointer. No other changes.

```conllu
# sent_id = Gos233.s388
# speaker_id = Tm-otro-03016
# sound_url = https://nl.ijs.si/project/gos20/Gos233/Gos233.s388.mp3
# text = ja , pa
1	ja	ja	PART	Q	_	3	discourse	_	pronunciation=ja|Gos2.1_token_id=Gos233.tok2068
2	,	,	PUNCT	Z	_	1	punct	_	_
3	pa	pa	CCONJ	Cc	_	0	root	_	pronunciation=pa|Gos2.1_token_id=Gos233.tok2069

# sent_id = Gos233.s389
# speaker_id = Bm-star-03014
# sound_url = https://nl.ijs.si/project/gos20/Gos233/Gos233.s389.mp3
# text = more pobirati .
1	more	moči	VERB	Vmpr3s	Aspect=Imp|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=more|Gos2.1_token_id=Gos233.tok2070|Coconstruct=parataxis::Gos233.s388::3
2	pobirati	pobirati	VERB	Vmpn	Aspect=Imp|VerbForm=Inf	1	xcomp	_	pronunciation=pobirat|Gos2.1_token_id=Gos233.tok2071
3	.	.	PUNCT	Z	_	1	punct	_	_
```

# coco_11

## current

```conllu
# sent_id = Gos233.s415
# speaker_id = Tm-otro-03016
# sound_url = https://nl.ijs.si/project/gos20/Gos233/Gos233.s415.mp3
# text = saj veš , da , da , da , kdor ti bo reklamo poslal
1	saj	saj	CCONJ	Cc	_	2	advmod	_	pronunciation=sej|Gos2.1_token_id=Gos233.tok2219
2	veš	vedeti	VERB	Vmpr2s	Aspect=Imp|Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=veš|Gos2.1_token_id=Gos233.tok2220
3	,	,	PUNCT	Z	_	4	punct	_	_
4	da	da	SCONJ	Cs	_	8	reparandum	_	pronunciation=da|Gos2.1_token_id=Gos233.tok2221
5	,	,	PUNCT	Z	_	6	punct	_	_
6	da	da	SCONJ	Cs	_	8	reparandum	_	pronunciation=da|Gos2.1_token_id=Gos233.tok2222
7	,	,	PUNCT	Z	_	8	punct	_	_
8	da	da	SCONJ	Cs	_	14	mark	_	pronunciation=da|Gos2.1_token_id=Gos233.tok2223|Coconstruct=mark::Gos233.s417::1
9	,	,	PUNCT	Z	_	14	punct	_	_
10	kdor	kdor	PRON	Pr-msn	Case=Nom|Gender=Masc|Number=Sing|PronType=Rel	14	nsubj	_	pronunciation=kdor|Gos2.1_token_id=Gos233.tok2224|Coconstruct=nsubj::Gos233.s417::1
11	ti	ti	PRON	Pp2-sd--y	Case=Dat|Number=Sing|Person=2|PronType=Prs|Variant=Short	14	iobj	_	pronunciation=ti|Gos2.1_token_id=Gos233.tok2225
12	bo	biti	AUX	Va-f3s-n	Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Fut|VerbForm=Fin	14	aux	_	pronunciation=bo|Gos2.1_token_id=Gos233.tok2226
13	reklamo	reklama	NOUN	Ncfsa	Case=Acc|Gender=Fem|Number=Sing	14	obj	_	pronunciation=reklamo|Gos2.1_token_id=Gos233.tok2227
14	poslal	poslati	VERB	Vmep-sm	Aspect=Perf|Gender=Masc|Number=Sing|VerbForm=Part	2	ccomp	_	pronunciation=poslal|Gos2.1_token_id=Gos233.tok2228|Coconstruct=advcl::Gos233.s417::1

# sent_id = Gos233.s417
# speaker_id = Bm-star-03014
# sound_url = https://nl.ijs.si/project/gos20/Gos233/Gos233.s417.mp3
# text = zaračuna .
1	zaračuna	zaračunati	VERB	Vmer3s	Aspect=Perf|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=zaračuna|Gos2.1_token_id=Gos233.tok2229|Coconstruct=ccomp::Gos233.s415::2
2	.	.	PUNCT	Z	_	1	punct	_	_
```

## proposed

This is 4.1 Completion: Speaker 1 says "saj veš, da, kdor ti bo reklamo poslal" (you know that, whoever sent you an advertisement...) — veš (token 2) takes a ccomp (da-clause) whose main verb is unrealized. Speaker 2 provides "zaračuna" (charges). Coconstruct=ccomp::Gos233.s415::2 on zaračuna correctly points back to veš.

Change: Remove Coconstruct from s415 tokens 8 (da), 10 (kdor), 14 (poslal) — all forward pointers on Speaker 1. Speaker 2's zaračuna already has the correct backward pointer. No other changes.

```conllu
# sent_id = Gos233.s415
# speaker_id = Tm-otro-03016
# sound_url = https://nl.ijs.si/project/gos20/Gos233/Gos233.s415.mp3
# text = saj veš , da , da , da , kdor ti bo reklamo poslal
1	saj	saj	CCONJ	Cc	_	2	advmod	_	pronunciation=sej|Gos2.1_token_id=Gos233.tok2219
2	veš	vedeti	VERB	Vmpr2s	Aspect=Imp|Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=veš|Gos2.1_token_id=Gos233.tok2220
3	,	,	PUNCT	Z	_	4	punct	_	_
4	da	da	SCONJ	Cs	_	8	reparandum	_	pronunciation=da|Gos2.1_token_id=Gos233.tok2221
5	,	,	PUNCT	Z	_	6	punct	_	_
6	da	da	SCONJ	Cs	_	8	reparandum	_	pronunciation=da|Gos2.1_token_id=Gos233.tok2222
7	,	,	PUNCT	Z	_	8	punct	_	_
8	da	da	SCONJ	Cs	_	14	mark	_	pronunciation=da|Gos2.1_token_id=Gos233.tok2223
9	,	,	PUNCT	Z	_	14	punct	_	_
10	kdor	kdor	PRON	Pr-msn	Case=Nom|Gender=Masc|Number=Sing|PronType=Rel	14	nsubj	_	pronunciation=kdor|Gos2.1_token_id=Gos233.tok2224
11	ti	ti	PRON	Pp2-sd--y	Case=Dat|Number=Sing|Person=2|PronType=Prs|Variant=Short	14	iobj	_	pronunciation=ti|Gos2.1_token_id=Gos233.tok2225
12	bo	biti	AUX	Va-f3s-n	Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Fut|VerbForm=Fin	14	aux	_	pronunciation=bo|Gos2.1_token_id=Gos233.tok2226
13	reklamo	reklama	NOUN	Ncfsa	Case=Acc|Gender=Fem|Number=Sing	14	obj	_	pronunciation=reklamo|Gos2.1_token_id=Gos233.tok2227
14	poslal	poslati	VERB	Vmep-sm	Aspect=Perf|Gender=Masc|Number=Sing|VerbForm=Part	2	ccomp	_	pronunciation=poslal|Gos2.1_token_id=Gos233.tok2228

# sent_id = Gos233.s417
# speaker_id = Bm-star-03014
# sound_url = https://nl.ijs.si/project/gos20/Gos233/Gos233.s417.mp3
# text = zaračuna .
1	zaračuna	zaračunati	VERB	Vmer3s	Aspect=Perf|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=zaračuna|Gos2.1_token_id=Gos233.tok2229|Coconstruct=ccomp::Gos233.s415::2
2	.	.	PUNCT	Z	_	1	punct	_	_
```

# coco_12

## current

```conllu
# sent_id = Gos233.s441
# speaker_id = Bm-star-03014
# sound_url = https://nl.ijs.si/project/gos20/Gos233/Gos233.s441.mp3
# text = in taisti stane v trgovini
1	in	in	CCONJ	Cc	_	3	cc	_	pronunciation=in|Gos2.1_token_id=Gos233.tok2362
2	taisti	taisti	DET	Pd-msn	Case=Nom|Gender=Masc|Number=Sing|PronType=Dem	3	nsubj	_	pronunciation=taisti|Gos2.1_token_id=Gos233.tok2363
3	stane	stati	VERB	Vmpr3s	Aspect=Imp|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=stane|Gos2.1_token_id=Gos233.tok2364
4	v	v	ADP	Sl	Case=Loc	5	case	_	pronunciation=v|Gos2.1_token_id=Gos233.tok2365
5	trgovini	trgovina	NOUN	Ncfsl	Case=Loc|Gender=Fem|Number=Sing	3	obl	_	pronunciation=trgovini|Gos2.1_token_id=Gos233.tok2366

# sent_id = Gos233.s442
# speaker_id = Tm-otro-03016
# sound_url = https://nl.ijs.si/project/gos20/Gos233/Gos233.s442.mp3
# text = devetsto evrov .
1	devetsto	devetsto	NUM	Mlc-pa	Case=Acc|Number=Plur|NumForm=Word|NumType=Card	2	nummod	_	pronunciation=devetsto|Gos2.1_token_id=Gos233.tok2367
2	evrov	evro	NOUN	Ncmpg	Case=Gen|Gender=Masc|Number=Plur	0	root	_	pronunciation=evrov|Gos2.1_token_id=Gos233.tok2368|Coconstruct=obl::Gos233.s441::3
3	.	.	PUNCT	Z	_	2	punct	_	_
```

## proposed

```conllu
# sent_id = Gos233.s441
# speaker_id = Bm-star-03014
# sound_url = https://nl.ijs.si/project/gos20/Gos233/Gos233.s441.mp3
# text = in taisti stane v trgovini
1	in	in	CCONJ	Cc	_	3	cc	_	pronunciation=in|Gos2.1_token_id=Gos233.tok2362
2	taisti	taisti	DET	Pd-msn	Case=Nom|Gender=Masc|Number=Sing|PronType=Dem	3	nsubj	_	pronunciation=taisti|Gos2.1_token_id=Gos233.tok2363
3	stane	stati	VERB	Vmpr3s	Aspect=Imp|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=stane|Gos2.1_token_id=Gos233.tok2364
4	v	v	ADP	Sl	Case=Loc	5	case	_	pronunciation=v|Gos2.1_token_id=Gos233.tok2365
5	trgovini	trgovina	NOUN	Ncfsl	Case=Loc|Gender=Fem|Number=Sing	3	obl	_	pronunciation=trgovini|Gos2.1_token_id=Gos233.tok2366

# sent_id = Gos233.s442
# speaker_id = Tm-otro-03016
# sound_url = https://nl.ijs.si/project/gos20/Gos233/Gos233.s442.mp3
# text = devetsto evrov .
1	devetsto	devetsto	NUM	Mlc-pa	Case=Acc|Number=Plur|NumForm=Word|NumType=Card	2	nummod	_	pronunciation=devetsto|Gos2.1_token_id=Gos233.tok2367
2	evrov	evro	NOUN	Ncmpg	Case=Gen|Gender=Masc|Number=Plur	0	root	_	pronunciation=evrov|Gos2.1_token_id=Gos233.tok2368|Coconstruct=obl::Gos233.s441::3
3	.	.	PUNCT	Z	_	2	punct	_	_
```

Note on coco_12: Annotation is correct as-is. This is 4.1 Completion: Speaker 1 says "in taisti stane v trgovini" (and that one costs in the store) — stane (token 3) projects a price/amount obl slot. Speaker 2 provides "devetsto evrov" (900 euros). No forward pointers on Speaker 1. No changes needed.

# coco_13

## current

```conllu
# sent_id = Gos246.s352
# speaker_id = Am-soro-07522
# sound_url = https://nl.ijs.si/project/gos20/Gos246/Gos246.s352.mp3
# text = in da še vedno
1	in	in	CCONJ	Cc	_	4	cc	_	pronunciation=in|Gos2.1_token_id=Gos246.tok3671|Coconstruct=cc::Gos246.s353::3
2	da	da	SCONJ	Cs	_	4	mark	_	pronunciation=da|Gos2.1_token_id=Gos246.tok3672|Coconstruct=mark::Gos246.s353::3
3	še	še	PART	Q	_	4	orphan	_	pronunciation=še|Gos2.1_token_id=Gos246.tok3673|Coconstruct=advmod::Gos246.s353::3
4	vedno	vedno	ADV	Rgp	Degree=Pos	0	root	_	pronunciation=vedno|Gos2.1_token_id=Gos246.tok3674|Coconstruct=advmod::Gos246.s353::3

# sent_id = Gos246.s353
# speaker_id = Mm-star-07523
# sound_url = https://nl.ijs.si/project/gos20/Gos246/Gos246.s353.mp3
# text = p- , pozna še to , ja .
1	p-	p-	X	Xt	_	3	reparandum	_	pronunciation=p…|Gos2.1_token_id=Gos246.tok3675
2	,	,	PUNCT	Z	_	1	punct	_	_
3	pozna	poznati	VERB	Vmpr3s	Aspect=Imp|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=pozna|Gos2.1_token_id=Gos246.tok3676|Coconstruct=parataxis::Gos246.s352::4
4	še	še	PART	Q	_	5	advmod	_	pronunciation=še|Gos2.1_token_id=Gos246.tok3677
5	to	ta	DET	Pd-nsa	Case=Acc|Gender=Neut|Number=Sing|PronType=Dem	3	obj	_	pronunciation=to|Gos2.1_token_id=Gos246.tok3678
6	,	,	PUNCT	Z	_	7	punct	_	_
7	ja	ja	PART	Q	_	3	discourse	_	pronunciation=ja|Gos2.1_token_id=Gos246.tok3679
8	.	.	PUNCT	Z	_	3	punct	_	_
```

## proposed

This is 4.1 Completion: Speaker 1 produces "in da še vedno" — a clause fragment with function words (cc, mark, advmod) but no main verb. The root "vedno" is an orphan standing in for the missing verb. Speaker 2 provides "pozna" (knows/recognizes) as the completing predicate. Coconstruct=parataxis::Gos246.s352::4 on pozna (pointing to vedno, the local root of s352) is acceptable given the constraint that s352 has no actual verb anchor.

Change: Remove Coconstruct from s352 tokens 1 (in), 2 (da), 3 (še), 4 (vedno) — all four are forward pointers on Speaker 1. Speaker 2's pozna already has the correct backward pointer. No other changes.

```conllu
# sent_id = Gos246.s352
# speaker_id = Am-soro-07522
# sound_url = https://nl.ijs.si/project/gos20/Gos246/Gos246.s352.mp3
# text = in da še vedno
1	in	in	CCONJ	Cc	_	4	cc	_	pronunciation=in|Gos2.1_token_id=Gos246.tok3671
2	da	da	SCONJ	Cs	_	4	mark	_	pronunciation=da|Gos2.1_token_id=Gos246.tok3672
3	še	še	PART	Q	_	4	orphan	_	pronunciation=še|Gos2.1_token_id=Gos246.tok3673
4	vedno	vedno	ADV	Rgp	Degree=Pos	0	root	_	pronunciation=vedno|Gos2.1_token_id=Gos246.tok3674

# sent_id = Gos246.s353
# speaker_id = Mm-star-07523
# sound_url = https://nl.ijs.si/project/gos20/Gos246/Gos246.s353.mp3
# text = p- , pozna še to , ja .
1	p-	p-	X	Xt	_	3	reparandum	_	pronunciation=p…|Gos2.1_token_id=Gos246.tok3675
2	,	,	PUNCT	Z	_	1	punct	_	_
3	pozna	poznati	VERB	Vmpr3s	Aspect=Imp|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=pozna|Gos2.1_token_id=Gos246.tok3676|Coconstruct=parataxis::Gos246.s352::4
4	še	še	PART	Q	_	5	advmod	_	pronunciation=še|Gos2.1_token_id=Gos246.tok3677
5	to	ta	DET	Pd-nsa	Case=Acc|Gender=Neut|Number=Sing|PronType=Dem	3	obj	_	pronunciation=to|Gos2.1_token_id=Gos246.tok3678
6	,	,	PUNCT	Z	_	7	punct	_	_
7	ja	ja	PART	Q	_	3	discourse	_	pronunciation=ja|Gos2.1_token_id=Gos246.tok3679
8	.	.	PUNCT	Z	_	3	punct	_	_
```

# coco_14

## current

```conllu
# sent_id = Gos254.s615
# speaker_id = Dm-prij-06009
# sound_url = https://nl.ijs.si/project/gos20/Gos254/Gos254.s615.mp3
# text = podpišeš , potem pa
1	podpišeš	podpisati	VERB	Vmer2s	Aspect=Perf|Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=podpišeš|Gos2.1_token_id=Gos254.tok3266
2	,	,	PUNCT	Z	_	3	punct	_	_
3	potem	potem	ADV	Rgp	Degree=Pos	1	parataxis	_	pronunciation=te|Gos2.1_token_id=Gos254.tok3267|Coconstruct=reparandum::Gos254.s616::1
4	pa	pa	CCONJ	Cc	_	3	orphan	_	pronunciation=pa|Gos2.1_token_id=Gos254.tok3268|Coconstruct=reparandum::Gos254.s616::2

# sent_id = Gos254.s616
# speaker_id = Mm-prij-06007
# sound_url = https://nl.ijs.si/project/gos20/Gos254/Gos254.s616.mp3
# text = potem pa se zgodi , ne .
1	potem	potem	ADV	Rgp	Degree=Pos	4	advmod	_	pronunciation=te|Gos2.1_token_id=Gos254.tok3269
2	pa	pa	CCONJ	Cc	_	4	advmod	_	pronunciation=pa|Gos2.1_token_id=Gos254.tok3270
3	se	se	PRON	Px------y	PronType=Prs|Reflex=Yes|Variant=Short	4	expl	_	pronunciation=se|Gos2.1_token_id=Gos254.tok3271
4	zgodi	zgoditi	VERB	Vmer3s	Aspect=Perf|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=zgodi|Gos2.1_token_id=Gos254.tok3272|Coconstruct=parataxis::Gos254.s615::1
5	,	,	PUNCT	Z	_	6	punct	_	_
6	ne	ne	PART	Q	Polarity=Neg	4	discourse	_	pronunciation=nej|Gos2.1_token_id=Gos254.tok3273
7	.	.	PUNCT	Z	_	4	punct	_	_
```

## proposed

This is 4.1 Completion with internal repetition. Speaker 1 says "podpišeš, potem pa [missing verb]" — potem pa opens a clause continuation whose main verb is unrealized. Speaker 2 starts by REPEATING "potem pa" (a restart/continuation cue) and then provides the completing verb "se zgodi" (it happens).

Two things to fix:
1. The reparandum relation for the repetition of "potem pa" must be on SPEAKER 2's tokens pointing BACK to Speaker 1 (not on Speaker 1 pointing forward).
2. Speaker 2's zgodi already has a correct backward Coconstruct=parataxis::s615::1 pointing to podpišeš.

Changes:
- Remove Coconstruct from s615 tokens 3 (potem) and 4 (pa) — forward pointers, wrong direction
- Add Coconstruct=reparandum::Gos254.s615::3 to s616 token 1 (potem) — Speaker 2 repeats Speaker 1's word
- Add Coconstruct=reparandum::Gos254.s615::4 to s616 token 2 (pa) — Speaker 2 repeats Speaker 1's word
- Keep Coconstruct=parataxis::Gos254.s615::1 on s616 token 4 (zgodi) — correct as-is

```conllu
# sent_id = Gos254.s615
# speaker_id = Dm-prij-06009
# sound_url = https://nl.ijs.si/project/gos20/Gos254/Gos254.s615.mp3
# text = podpišeš , potem pa
1	podpišeš	podpisati	VERB	Vmer2s	Aspect=Perf|Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=podpišeš|Gos2.1_token_id=Gos254.tok3266
2	,	,	PUNCT	Z	_	3	punct	_	_
3	potem	potem	ADV	Rgp	Degree=Pos	1	parataxis	_	pronunciation=te|Gos2.1_token_id=Gos254.tok3267
4	pa	pa	CCONJ	Cc	_	3	orphan	_	pronunciation=pa|Gos2.1_token_id=Gos254.tok3268

# sent_id = Gos254.s616
# speaker_id = Mm-prij-06007
# sound_url = https://nl.ijs.si/project/gos20/Gos254/Gos254.s616.mp3
# text = potem pa se zgodi , ne .
1	potem	potem	ADV	Rgp	Degree=Pos	4	advmod	_	pronunciation=te|Gos2.1_token_id=Gos254.tok3269|Coconstruct=reparandum::Gos254.s615::3
2	pa	pa	CCONJ	Cc	_	4	advmod	_	pronunciation=pa|Gos2.1_token_id=Gos254.tok3270|Coconstruct=reparandum::Gos254.s615::4
3	se	se	PRON	Px------y	PronType=Prs|Reflex=Yes|Variant=Short	4	expl	_	pronunciation=se|Gos2.1_token_id=Gos254.tok3271
4	zgodi	zgoditi	VERB	Vmer3s	Aspect=Perf|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	pronunciation=zgodi|Gos2.1_token_id=Gos254.tok3272|Coconstruct=parataxis::Gos254.s615::1
5	,	,	PUNCT	Z	_	6	punct	_	_
6	ne	ne	PART	Q	Polarity=Neg	4	discourse	_	pronunciation=nej|Gos2.1_token_id=Gos254.tok3273
7	.	.	PUNCT	Z	_	4	punct	_	_
```
