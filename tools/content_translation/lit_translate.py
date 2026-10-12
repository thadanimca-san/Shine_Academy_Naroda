"""Adds Hindi and Gujarati to an English literature chapter (First Flight, Footprints).

usage: python3 lit_translate.py <chapter folder> <translation module>

The module (tr_ffNN.py) defines:
  META     = {"title": (hi, gu)}
  SECTIONS = {"s1": (hi, gu), ...}
  T        = {"s2.thm.body": (hi, gu), "ex1.question": (hi, gu), "ex1.answer_steps": [(hi, gu), ...], ...}
             keyed by block or question id (without the chapter prefix) and field
  E        = {"english text": (hi, gu), ...}  for options, feedback and short repeated texts
Common phrases (Correct!, True/False, marking schemes, extract instructions) are built in.
Extract questions keep the quoted English lines; only the instructions and sub-questions
are translated (sub-questions and answers are looked up in E or T as "extN.q1"/"extN.a1").
Nothing is written unless every text is translated; missing texts are listed."""
import importlib, json, os, re, sys

sys.path.insert(0, os.path.dirname(__file__))

COMMON = {
    "Correct!": ("सही!", "સાચું!"),
    "True": ("सत्य", "સાચું"),
    "False": ("असत्य", "ખોટું"),
    "Read the extract and answer the questions.": ("अंश पढ़िए और प्रश्नों के उत्तर दीजिए।", "અંશ વાંચો અને પ્રશ્નોના જવાબ આપો."),
    "Read the passage (based on the lesson) and answer the questions.": ("पाठ पर आधारित गद्यांश पढ़िए और प्रश्नों के उत्तर दीजिए।", "પાઠ પર આધારિત ગદ્યાંશ વાંચો અને પ્રશ્નોના જવાબ આપો."),
    "1 mark: content point 1": ("1 अंक: विषय-वस्तु बिंदु 1", "1 ગુણ: વિષયવસ્તુ મુદ્દો 1"),
    "1 mark: content point 2": ("1 अंक: विषय-वस्तु बिंदु 2", "1 ગુણ: વિષયવસ્તુ મુદ્દો 2"),
    "1 mark: expression and accuracy (40-50 words)": ("1 अंक: अभिव्यक्ति और शुद्धता (40-50 शब्द)", "1 ગુણ: અભિવ્યક્તિ અને શુદ્ધતા (40-50 શબ્દો)"),
    "3 marks: content (relevant points from the text)": ("3 अंक: विषय-वस्तु (पाठ से प्रासंगिक बिंदु)", "3 ગુણ: વિષયવસ્તુ (પાઠમાંથી સંબંધિત મુદ્દા)"),
    "2 marks: organisation and coherence": ("2 अंक: संगठन और सुसंगति", "2 ગુણ: ગોઠવણી અને સુસંગતતા"),
    "1 mark: accuracy of language (100-120 words)": ("1 अंक: भाषा की शुद्धता (100-120 शब्द)", "1 ગુણ: ભાષાની શુદ્ધતા (100-120 શબ્દો)"),
    "1 mark: first point": ("1 अंक: पहला बिंदु", "1 ગુણ: પહેલો મુદ્દો"),
    "1 mark: second point": ("1 अंक: दूसरा बिंदु", "1 ગુણ: બીજો મુદ્દો"),
    # Hindi Course B marking schemes.
    "1 mark: content (correct point from the text)": ("1 अंक: विषय-वस्तु (पाठ से सही बिंदु)", "1 ગુણ: વિષયવસ્તુ (પાઠમાંથી સાચો મુદ્દો)"),
    "1 mark: expression in Hindi (25-30 words)": ("1 अंक: हिंदी में अभिव्यक्ति (25-30 शब्द)", "1 ગુણ: હિંદીમાં અભિવ્યક્તિ (25-30 શબ્દો)"),
    "2 marks: content (relevant points from the text)": ("2 अंक: विषय-वस्तु (पाठ से प्रासंगिक बिंदु)", "2 ગુણ: વિષયવસ્તુ (પાઠમાંથી સંબંધિત મુદ્દા)"),
    "1 mark: expression in Hindi (50-60 words)": ("1 अंक: हिंदी में अभिव्यक्ति (50-60 शब्द)", "1 ગુણ: હિંદીમાં અભિવ્યક્તિ (50-60 શબ્દો)"),
    "The poet": ("कवि", "કવિ"),
    "The writer": ("लेखक", "લેખક"),
    # Block titles shared by every chapter.
    "Memory tricks": ("याद रखने की तरकीबें", "યાદ રાખવાની યુક્તિઓ"),
    "Common mistakes": ("आम ग़लतियाँ", "સામાન્ય ભૂલો"),
    "Try this in class": ("कक्षा में करके देखें", "વર્ગમાં કરી જુઓ"),
    "Think and explain": ("सोचिए और समझाइए", "વિચારો અને સમજાવો"),
    "Where this leads": ("आगे कहाँ", "આગળ ક્યાં"),
    "Mastery challenge": ("महारत चुनौती", "નિપુણતા પડકાર"),
    "Summary": ("सारांश", "સારાંશ"),
    "Exam tips": ("परीक्षा सुझाव", "પરીક્ષા માટેની ટિપ્સ"),
    "What the poem says": ("कविता क्या कहती है", "કવિતા શું કહે છે"),
    "Remember, avoid, practise": ("याद रखें, बचें, अभ्यास करें", "યાદ રાખો, ટાળો, અભ્યાસ કરો"),
    "The poem and its meaning": ("कविता और उसका अर्थ", "કવિતા અને તેનો અર્થ"),
}
for part in ("i", "ii", "iii", "iv", "v"):
    COMMON[f"({part}) 1 mark"] = (f"({part}) 1 अंक", f"({part}) 1 ગુણ")

TF_Q = "State whether the following statement is true or false: "
TF_Q_TR = ("बताइए कि निम्नलिखित कथन सत्य है या असत्य: ", "નીચેનું વિધાન સાચું છે કે ખોટું તે જણાવો: ")
FEEDBACK_PREFIX = {"Correct! ": ("सही! ", "સાચું! "), "Not quite. ": ("पूरी तरह नहीं। ", "બરાબર નથી. ")}
PARTS = ("i", "ii", "iii", "iv", "v")
TEXT = ["title", "body", "question", "explanation", "front", "back", "person", "future"]
LISTS = ["options", "option_feedback", "answer_steps", "marking_scheme"]

folder, module = sys.argv[1], sys.argv[2]
M = importlib.import_module(module)
T, E = getattr(M, "T", {}), {**COMMON, **getattr(M, "E", {})}
missing = []


def plain(text):
    """Translation of a whole text by English lookup or a built-in pattern, or None."""
    if text in E:
        return E[text]
    if not re.search(r"[A-Za-z]", text):
        return (text, text)
    for prefix, (hi, gu) in FEEDBACK_PREFIX.items():
        if text.startswith(prefix) and text[len(prefix):] in E:
            rest = E[text[len(prefix):]]
            return (hi + rest[0], gu + rest[1])
    m = re.match(r"^\((i|ii|iii|iv|v)\) (.+)$", text, re.S)
    if m and m.group(2) in E:
        return (f"({m.group(1)}) " + E[m.group(2)][0], f"({m.group(1)}) " + E[m.group(2)][1])
    return None


def extract_question(lid, text):
    """'Intro\n\n*quote*\n*quote*\n\n(i) q ...' : keep the quote, translate the rest."""
    parts = text.split("\n\n")
    intro, quote, subs = parts[0], parts[1], parts[2:]
    out = [E.get(intro) or T.get(f"{lid}.intro")]
    if out[0] is None:
        missing.append(f"{lid}.intro: {intro!r}")
        return None
    hi, gu = [out[0][0], quote], [out[0][1], quote]
    for k, sub in enumerate(subs, 1):
        m = re.match(r"^\((i|ii|iii|iv|v)\) (.+)$", sub, re.S)
        tr = T.get(f"{lid}.q{k}") or E.get(m.group(2))
        if tr is None:
            missing.append(f"{lid}.q{k}: {m.group(2)!r}")
            return None
        hi.append(f"({m.group(1)}) {tr[0]}")
        gu.append(f"({m.group(1)}) {tr[1]}")
    return ("\n\n".join(hi), "\n\n".join(gu))


def translate(item, prefix):
    lid = item["id"][len(prefix) + 1:].replace("q.", "", 1) if item["id"].startswith(prefix + ".q.") else item["id"][len(prefix) + 1:]
    is_extract = item.get("type") == "case_based"
    for field in TEXT:
        english = item.get(field)
        if not isinstance(english, str) or not english.strip():
            continue
        tr = T.get(f"{lid}.{field}")
        if tr is None and field == "question" and is_extract:
            tr = extract_question(lid, english)
            if tr is None:
                continue
        if tr is None and field == "question" and english.startswith(TF_Q):
            rest = T.get(f"{lid}.statement") or E.get(english[len(TF_Q):])
            if rest:
                tr = (TF_Q_TR[0] + rest[0], TF_Q_TR[1] + rest[1])
        if tr is None:
            tr = plain(english)
        if tr is None:
            missing.append(f"{lid}.{field}: {english[:80]!r}")
            continue
        item[f"{field}_hi"], item[f"{field}_gu"] = tr
    for field in LISTS:
        english = item.get(field)
        if not isinstance(english, list) or not english:
            continue
        given = T.get(f"{lid}.{field}")
        if given is not None:
            if len(given) != len(english):
                missing.append(f"{lid}.{field}: {len(given)} entries, English has {len(english)}")
                continue
            pairs = given
        else:
            pairs = []
            for k, e in enumerate(english, 1):
                tr = plain(e)
                if tr is None and field == "option_feedback":
                    # 'Correct! <explanation>' / 'Not quite. <explanation>' reuse the item's explanation.
                    for pre, (phi, pgu) in FEEDBACK_PREFIX.items():
                        expl = T.get(f"{lid}.explanation")
                        if e.startswith(pre) and expl and e[len(pre):] == item.get("explanation"):
                            tr = (phi + expl[0], pgu + expl[1])
                if tr is None and is_extract and field == "answer_steps":
                    m = re.match(r"^\((i|ii|iii|iv|v)\) (.+)$", e, re.S)
                    a = T.get(f"{lid}.a{k}")
                    tr = (f"({m.group(1)}) {a[0]}", f"({m.group(1)}) {a[1]}") if (m and a) else None
                if tr is None:
                    missing.append(f"{lid}.{field}[{k - 1}]: {e[:80]!r}")
                pairs.append(tr)
            if None in pairs:
                continue
        item[f"{field}_hi"] = [p[0] for p in pairs]
        item[f"{field}_gu"] = [p[1] for p in pairs]


chapter_path, questions_path = f"{folder}/chapter.json", f"{folder}/questions.json"
chapter = json.load(open(chapter_path, encoding="utf-8"))
bank = json.load(open(questions_path, encoding="utf-8"))
prefix = chapter["sections"][0]["blocks"][0]["id"].split(".")[0]

chapter["title_hi"], chapter["title_gu"] = M.META["title"]
for section in chapter["sections"]:
    if section["id"] in M.SECTIONS or section["title"] in E:
        section["title_hi"], section["title_gu"] = M.SECTIONS.get(section["id"]) or E[section["title"]]
    else:
        missing.append(f"section {section['id']} title")
    for block in section["blocks"]:
        translate(block, prefix)
for q in bank["questions"]:
    translate(q, prefix)

if missing:
    print(f"{len(missing)} texts still need Hindi/Gujarati:")
    for m in missing:
        print("  " + m)
    sys.exit(1)
chapter["languages"] = ["en", "hi", "gu"]
for path, data in ((chapter_path, chapter), (questions_path, bank)):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
print(f"Hindi and Gujarati complete for {chapter['title']}")
