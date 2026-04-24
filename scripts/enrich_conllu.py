"""
Enrich UD_Slovenian-SST CoNLL-U file with speaker and event metadata from GOS TSVs.

Speaker metadata (per sentence, after # speaker_id):
    # speaker_gender, # speaker_age, # speaker_education, # speaker_residence

Event metadata (per document, after # newdoc id):
    # event_type, # event_domain, # event_channel, # event_description
"""

import csv
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Translation tables
# ---------------------------------------------------------------------------

SEX = {
    "moški": "male",
    "ženski": "female",
    "-": "unknown",
}

AGE = {
    "do 10 let": "0-18",
    "10 do 18 let": "0-18",
    "18 do 34 let": "18 to 34",
    "30 do 59 let": "30 to 59",
    "nad 60 let": "60+",
    "-": "unknown",
}

EDUCATION = {
    "OŠ ali manj": "primary or less",
    "srednja šola": "high-school",
    "višja ali visoka šola": "college",
    "fakulteta ali več": "university or more",
    "-": "unknown",
}

TYPE = {
    "informativno-izobraževalni": "info-education",
    "zasebni": "private",
    "nezasebni": "non-private",
    "razvedrilni": "entertainment",
    "-": "_",
}

CHANNEL = {
    "osebni stik": "in-person",
    "radio": "radio",
    "televizija": "TV",
    "telefon": "telephone",
    "internet": "internet",
    "-": "unknown",
}

# Domain translations — source: DeepL (Slovenian → British English)
DOMAIN = {
    "2. triletje, družboslovje": "2nd triennium, social sciences",
    "2. triletje, naravoslovje": "2nd triennium, natural sciences",
    "3. triletje, družboslovje": "3rd triennium, social sciences",
    "3. triletje, naravoslovje": "3rd triennium, natural sciences",
    "Aktual, Aktualno": "Aktual, Aktualno",
    "Aktual, Na sredi": "Aktual, Na sredi",
    "Belvi, jutranji": "Belvi, Morning Edition",
    "Capris, jutranji": "Capris, Morning Edition",
    "Center, jutranji": "Center, Morning Edition",
    "City, jutranji": "City, Morning Edition",
    "Fantasy, jutranji": "Fantasy, Morning Edition",
    "Koroški, Salter": "Koroški, Salter",
    "Koroški, intervju": "Koroški, interview",
    "Kranj, intervju": "Kranj, interview",
    "Krka, intervju": "Krka, interview",
    "Krka, potovanja": "Krka, travel",
    "Maribor1, Tribuna": "Maribor1, Tribuna",
    "Maribor1, jutranji": "Maribor1, morning",
    "Maxi, Pižama bar": "Maxi, Pižama bar",
    "Maxi, Pod brajdami": "Maxi, Pod brajdami",
    "Ognjišče, Naš gost": "Ognjišče, Naš gost",
    "Ognjišče, Pogovor o": "Ognjišče, Pogovor o",
    "PopTV, 24ur": "PopTV, 24ur",
    "PopTV, As ti tud": "PopTV, As ti tud",
    "PopTV, Desetka": "PopTV, Desetka",
    "PopTV, Kmetija": "PopTV, Kmetija",
    "PopTV, Preverjeno": "PopTV, Preverjeno",
    "PopTV, Trenja": "PopTV, Trenja",
    "PopTV, Vzemi ali pusti": "PopTV, Vzemi ali pusti",
    "PopTV, predvolilna": "PopTV, Pre-election",
    "Slovenija1, Intervju": "Slovenija1, Interview",
    "TVSlo, NLP": "TVSlo, NLP",
    "TVSlo, Odmevi": "TVSlo, Odmevi",
    "TVSlo, Piramida": "TVSlo, Piramida",
    "TVSlo, Polemika": "TVSlo, Polemika",
    "TVSlo, StudioCity": "TVSlo, StudioCity",
    "TVSlo, šport": "TVSlo, sports",
    "Val202, Aktualna": "Val202, Aktualna",
    "Val202, Na sceni": "Val202, Na sceni",
    "Val202, Vroči mikrofon": "Val202, Vroči mikrofon",
    "akademski, družboslovje": "academic, social sciences",
    "akademski, humanistika": "academic, humanities",
    "akademski, naravoslovje": "academic, natural sciences",
    "akademski, tehnika": "academic, technology",
    "delovno mesto, sodelavci": "workplace, colleagues",
    "doma, družina": "home, family",
    "doma, prijatelji": "home, friends",
    "formalni delovni sestanek": "formal work meeting",
    "formalni razgovor": "formal interview",
    "gimnazija, družboslovje": "high school, social sciences",
    "gimnazija, naravoslovje": "high school, natural sciences",
    "informacije": "information",
    "intervju": "interview",
    "javno predavanje": "public lecture",
    "javno predavanje, animalistična etika": "public lecture, animal ethics",
    "javno predavanje, biologija": "public lecture, biology",
    "javno predavanje, celiakija": "public lecture, celiac disease",
    "javno predavanje, celice": "public lecture, cells",
    "javno predavanje, delovne kariere": "public lecture, professional careers",
    "javno predavanje, digitalna komunikacija": "public lecture, digital communication",
    "javno predavanje, droge": "public lecture, drugs",
    "javno predavanje, dužboslovna imaginacija": "public lecture, social science imagination",
    "javno predavanje, ekonomija": "public lecture, economics",
    "javno predavanje, ekspertni sistemi": "public lecture, expert systems",
    "javno predavanje, farmacija": "public lecture, pharmacy",
    "javno predavanje, fitoterapija": "public lecture, phytotherapy",
    "javno predavanje, geologija": "public lecture, geology",
    "javno predavanje, hiše": "public lecture, houses",
    "javno predavanje, izobraževanje": "public lecture, education",
    "javno predavanje, jeklo": "public lecture, steel",
    "javno predavanje, jezik": "public lecture, language",
    "javno predavanje, karcinom": "public lecture, carcinoma",
    "javno predavanje, kazenske sankcije": "public lecture, criminal sanctions",
    "javno predavanje, kemične prvine v tleh": "public lecture, chemical elements in soil",
    "javno predavanje, kiparstvo": "public lecture, sculpture",
    "javno predavanje, literarna zgodovina": "public lecture, literary history",
    "javno predavanje, matematika": "public lecture, mathematics",
    "javno predavanje, matematična morfologija": "public lecture, mathematical morphology",
    "javno predavanje, mediji": "public lecture, media",
    "javno predavanje, meditacija": "public lecture, meditation",
    "javno predavanje, meningoencefalitis": "public lecture, meningoencephalitis",
    "javno predavanje, nanomateriali": "public lecture, nanomaterials",
    "javno predavanje, nanotehnologija": "public lecture, nanotechnology",
    "javno predavanje, oceani": "public lecture, oceans",
    "javno predavanje, okolje": "public lecture, environment",
    "javno predavanje, omrežja": "public lecture, networks",
    "javno predavanje, partnerstvo": "public lecture, partnership",
    "javno predavanje, podjetništvo": "public lecture, entrepreneurship",
    "javno predavanje, pozitivna psihologija": "public lecture, positive psychology",
    "javno predavanje, pravo": "public lecture, law",
    "javno predavanje, pujski": "public lecture, piglets",
    "javno predavanje, računalništvo": "public lecture, computer science",
    "javno predavanje, računske metode": "public lecture, computational methods",
    "javno predavanje, slovanski mikrojeziki": "public lecture, Slavic microlanguages",
    "javno predavanje, sociologija": "public lecture, sociology",
    "javno predavanje, spletna varnost": "public lecture, internet security",
    "javno predavanje, srednjeevropske identitete": "public lecture, Central European identities",
    "javno predavanje, staranje": "public lecture, ageing",
    "javno predavanje, strojništvo": "public lecture, mechanical engineering",
    "javno predavanje, tekočekristalne modre faze": "public lecture, liquid crystal blue phases",
    "javno predavanje, umetnost": "public lecture, art",
    "javno predavanje, uvodni govor": "public lecture, opening speech",
    "javno predavanje, zastoj srca": "public lecture, cardiac arrest",
    "javno predavanje, čuječnost": "public lecture, mindfulness",
    "jezikovni tečaj za tujce": "language course for foreigners",
    "klic prijatelju": "call to a friend",
    "klic sorodniku": "call to a relative",
    "konzultacija": "consultation",
    "moderirani pogovor": "moderated discussion",
    "nagovor na dogodku": "speech at an event",
    "neformalni delovni sestanek": "informal work meeting",
    "novinarska konferenca": "press conference",
    "okrogla miza": "roundtable",
    "poklicna strokovna, družboslovje": "vocational/professional, social sciences",
    "poklicna strokovna, naravoslovje": "vocational/professional, natural sciences",
    "prodaja/trgovina": "sales/retail",
    "prosti dialog med dvema sogovornikoma": "free dialogue between two interlocutors",
    "prosti monološki govor": "free monologue",
    "razlaganje in opisovanje": "explanation and description",
    "seja državnega zbora": "session of the National Assembly",
    "spletni dogodek": "online event",
    "storitev": "service",
    "svetovanje": "consulting",
    "tajništvo": "secretarial work",
    "zunaj doma, družina": "away from home, family",
    "zunaj doma, prijatelji": "away from home, friends",
    "Štajerski, intervju": "Štajerski, interview",
}


def translate_domain(raw: str) -> str:
    if not raw or raw == "-":
        return "_"
    return DOMAIN.get(raw, raw)


def translate_region(raw: str) -> str:
    if not raw or raw == "-":
        return "unknown"
    # Take first listed region, keep Slovenian name
    return raw.split(",")[0].strip()


# ---------------------------------------------------------------------------
# Event description translations (UK English)
# Only covers doc IDs present in SST dev; Artur docs have no real title.
# ---------------------------------------------------------------------------

# Event description translations — source: DeepL (Slovenian → British English)
DESCRIPTION = {
    "Gos018": "A primary school lesson on social studies, reviewing the natural features of the local landscape, learning about different types of settlements and dwellings, and completing worksheets on the characteristics of local settlements.",
    "Gos034": "Discussion on the theatre's programme for 2009.",
    "Gos042": "Discussion on the discontinuation of funding for community service as an alternative to a prison sentence.",
    "Gos051": "Slovenian language lesson at secondary school. They studied literature and poetry. During the lesson, they reviewed what they had learnt in previous lessons.",
    "Gos052": "Second year of secondary school",
    "Gos072": "Pre-election debate between party leaders.",
    "Gos073": "Programme with guests on the sale of a majority stake in a major Slovenian retail company.",
    "Gos076": "Graffiti on a church.",
    "Gos099": "Court ruling in favour of a teacher.",
    "Gos131": "Morning radio programme.",
    "Gos132": "Morning radio programme.",
    "Gos141": "Morning radio programme.",
    "Gos148": "Interview with a traveller from Iran.",
    "Gos149": "Interview with a successful Slovenian skier.",
    "Gos150": "Interview with a radio presenter.",
    "Gos153": "Student radio programme.",
    "Gos155": "Local radio programme in which listeners' music requests are played.",
    "Gos176": "Meeting of the language department at the university.",
    "Gos184": "A conversation between three employees at a hunting and fishing shop: about working over the holidays, sending greeting cards to business partners, the stock-take at the start of the year, debts, customers, thefts, etc. As all three speakers work in a family business, much of the conversation is personal and unrelated to the business.",
    "Gos192": "A conversation between a hairdresser, the customer he is cutting, and a third (regular) customer who is present during the haircut.",
    "Gos197": "A conversation in a dentist's surgery between a patient, the dentist and the assistant.",
    "Gos198": "A conversation between a customer and a sales assistant in a jewellery shop.",
    "Gos202": "A conversation between a customer and an employee of a telecommunications service provider.",
    "Gos211": "A telephone conversation between a customer and an operator at the call centre of a company marketing telecommunications services.",
    "Gos212": "A telephone conversation between a customer and an operator at the call centre of a company marketing telecommunications services.",
    "Gos218": "A conversation between a grandmother, her granddaughter and her great-granddaughter whilst spending a free morning together. Topics include colouring a picture book, various incidents, doing sums...",
    "Gos222": "A conversation between two friends about landlords and other events.",
    "Gos230": "A daughter tells her mother about a film she has watched, events that took place over the weekend...",
    "Gos236": "A family gathering to celebrate a family member passing a professional exam. Topics include the upcoming holiday, anecdotes from two family members' travels, stories that happened to friends, and travel experiences with travel agencies in general.",
    "Gos243": "A conversation between three members of an alternative music band after a rehearsal; topics mostly revolve around music, weekend events and plans for the coming days.",
    "Gos247": "A mother and daughter chat over coffee about building a house, work, dreams, etc.",
    "Gos248": "A grandmother and granddaughter are talking about volunteering on a European project, football, etc.",
    "Gos249": "A father is telling his daughter about his memories from school, etc.",
    "Gos261": "A conversation in a café between a foreigner and a local, who are meeting for the first time during this conversation, about the foreigner's impressions and life.",
    "Gos265": "A conversation between two friends about various current topics (a new dog, planning a trip, the situation in the choir, their mutual acquaintances, etc.).",
    "Gos271": "A telephone conversation with a friend, mainly to arrange when and where they will meet.",
    "Gos273": "A telephone conversation between two female friends about various topics, mostly about a trip from which one has recently returned.",
    "Gos274": "A conversation between a brother and sister about what happened that day.",
    "Gos287": "A conversation between a couple about current affairs and planning a holiday.",
}


# ---------------------------------------------------------------------------
# Load TSVs
# ---------------------------------------------------------------------------

def load_speakers(path: Path) -> dict:
    """PRS-ID → {gender, age, education, residence}"""
    result = {}
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            pid = row["PRS-ID"].strip()
            if pid in ("-", "audience", "all", ""):
                continue
            result[pid] = {
                "speaker_gender": SEX.get(row["SEX"].strip(), row["SEX"].strip()),
                "speaker_age": AGE.get(row["AGE"].strip(), row["AGE"].strip()),
                "speaker_education": EDUCATION.get(row["EDUCATION"].strip(), row["EDUCATION"].strip()),
                "speaker_residence": translate_region(row["PERM-RESD"].strip()),
            }
    return result


def load_speeches(path: Path) -> dict:
    """TEXT-ID → {event_type, event_domain, event_channel, event_description}"""
    result = {}
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            tid = row["TEXT-ID"].strip()
            result[tid] = {
                "event_type": TYPE.get(row["TYPE"].strip(), row["TYPE"].strip()),
                "event_domain": translate_domain(row["DOMAIN"].strip()),
                "event_channel": CHANNEL.get(row["CHANNEL"].strip(), row["CHANNEL"].strip()),
                "event_description": DESCRIPTION.get(tid, row["TITLE"].strip()),
            }
    return result


# ---------------------------------------------------------------------------
# Process CoNLL-U
# ---------------------------------------------------------------------------

def enrich(conllu_path: Path, speakers: dict, speeches: dict, out_path: Path):
    with open(conllu_path, encoding="utf-8") as fin, \
         open(out_path, "w", encoding="utf-8") as fout:

        missing_speakers = set()
        missing_docs = set()

        for line in fin:
            fout.write(line)
            stripped = line.rstrip("\n")

            if stripped.startswith("# newdoc id = "):
                doc_id = stripped[len("# newdoc id = "):].strip()
                if doc_id in speeches:
                    ev = speeches[doc_id]
                    fout.write(f"# event_type = {ev['event_type']}\n")
                    fout.write(f"# event_domain = {ev['event_domain']}\n")
                    fout.write(f"# event_channel = {ev['event_channel']}\n")
                    fout.write(f"# event_description = {ev['event_description']}\n")
                else:
                    missing_docs.add(doc_id)

            elif stripped.startswith("# speaker_id = "):
                spk_id = stripped[len("# speaker_id = "):].strip()
                if spk_id in speakers:
                    sp = speakers[spk_id]
                    fout.write(f"# speaker_gender = {sp['speaker_gender']}\n")
                    fout.write(f"# speaker_age = {sp['speaker_age']}\n")
                    fout.write(f"# speaker_education = {sp['speaker_education']}\n")
                    fout.write(f"# speaker_residence = {sp['speaker_residence']}\n")
                else:
                    missing_speakers.add(spk_id)

        if missing_docs:
            print(f"WARNING: {len(missing_docs)} doc IDs not found in speeches.tsv: {sorted(missing_docs)}", file=sys.stderr)
        if missing_speakers:
            print(f"WARNING: {len(missing_speakers)} speaker IDs not found in speakers.tsv: {sorted(missing_speakers)}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    base = Path(__file__).parent.parent / "src"
    gos_dir = base / "gos"
    sst_dir = base / "sst"

    speakers = load_speakers(gos_dir / "Gos-speakers.tsv")
    speeches = load_speeches(gos_dir / "Gos-speeches.tsv")

    conllu_in = sst_dir / "sl_sst-ud-dev.conllu"
    conllu_out = sst_dir / "sl_sst-ud-dev-enriched.conllu"

    enrich(conllu_in, speakers, speeches, conllu_out)
    print(f"Done. Output: {conllu_out}")
