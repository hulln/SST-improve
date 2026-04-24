# Slovenian → English value mappings

Used for enriching the SST CoNLL-U file with GOS metadata.
Sources: Excel statistics file (gender, age, education, disc-type, channel); DeepL (domain); manual UK English (descriptions).

---

## speaker_gender (SEX)

Source: Excel statistics file.

| Slovenian | English |
|-----------|---------|
| ženski | female |
| moški | male |
| - | unknown |

---

## speaker_age (AGE)

Source: Excel statistics file. "do 10 let" and "10 do 18 let" are merged into 0-18 following the Excel.

| Slovenian | English |
|-----------|---------|
| do 10 let | 0-18 |
| 10 do 18 let | 0-18 |
| 18 do 34 let | 18 to 34 |
| 30 do 59 let | 30 to 59 |
| nad 60 let | 60+ |
| - | unknown |

---

## speaker_education (EDUCATION)

Source: Excel statistics file.

| Slovenian | English |
|-----------|---------|
| OŠ ali manj | primary or less |
| srednja šola | high-school |
| višja ali visoka šola | college |
| fakulteta ali več | university or more |
| - | unknown |

---

## speaker_residence (PERM-RESD)

First-listed region only. Slovenian name kept as-is — no English translation in source doc.

| Example raw value | Value used |
|-------------------|------------|
| osrednjeslovenska | osrednjeslovenska |
| gorenjska, osrednjeslovenska | gorenjska |
| podravska, savinjska | podravska |
| - | unknown |

---

## event_type (TYPE)

Source: Excel statistics file.

| Slovenian | English |
|-----------|---------|
| informativno-izobraževalni | info-education |
| zasebni | private |
| nezasebni | non-private |
| razvedrilni | entertainment |

---

## event_channel (CHANNEL)

Source: Excel statistics file.

| Slovenian | English |
|-----------|---------|
| osebni stik | in-person |
| radio | radio |
| televizija | TV |
| telefon | telephone |
| internet | internet |
| - | unknown |

---

## event_domain (DOMAIN)

Source: DeepL (Slovenian → British English). Full list in [domain-translations.md](domain-translations.md).

Only values present in the SST dev corpus are listed here.

| Slovenian | English |
|-----------|---------|
| 2. triletje, družboslovje | 2nd triennium, social sciences |
| Belvi, jutranji | Belvi, Morning Edition |
| Center, jutranji | Center, Morning Edition |
| Koroški, Salter | Koroški, Salter |
| Koroški, intervju | Koroški, interview |
| Krka, intervju | Krka, interview |
| Maxi, Pižama bar | Maxi, Pižama bar |
| PopTV, 24ur | PopTV, 24ur |
| PopTV, Trenja | PopTV, Trenja |
| PopTV, predvolilna | PopTV, Pre-election |
| Val202, Aktualna | Val202, Aktualna |
| doma, družina | home, family |
| doma, prijatelji | home, friends |
| formalni delovni sestanek | formal work meeting |
| gimnazija, družboslovje | high school, social sciences |
| informacije | information |
| klic prijatelju | call to a friend |
| klic sorodniku | call to a relative |
| neformalni delovni sestanek | informal work meeting |
| novinarska konferenca | press conference |
| okrogla miza | roundtable |
| prodaja/trgovina | sales/retail |
| prosti dialog med dvema sogovornikoma | free dialogue between two interlocutors |
| prosti monološki govor | free monologue |
| seja državnega zbora | session of the National Assembly |
| storitev | service |
| zunaj doma, prijatelji | away from home, friends |

---

## event_description (TITLE)

Source: DeepL (Slovenian → British English). No English translation in source Excel or GOS data.

All 39 GOS titles present in SST dev are translated in `scripts/enrich_conllu.py` (`DESCRIPTION` dict).
The 5 Artur docs have no real title in the source data; the doc ID is used as-is.
