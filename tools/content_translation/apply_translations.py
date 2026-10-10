# Part of tools/content_translation. Chapter-specific translation tables are
# written per chapter (see tr_*.py examples in docs) and passed by module name.
"""Writes Hindi/Gujarati fields into a chapter's chapter.json and questions.json.

usage: apply_translations.py <chapter folder> <lesson module> <questions module>

Stops with a list of every untranslated text, so nothing is silently left in
English. Marks the chapter as available in en/hi/gu only when complete."""
import importlib, json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common_translations import MARKING, AR_OPTIONS, AR_LABELS, ar_feedback, by_template, is_math_only

TEXT = ["title", "body", "question", "explanation", "problem", "given", "formula", "answer", "front", "back",
        "person", "quote", "future", "feedback_incorrect", "statement"]
LISTS = ["options", "option_feedback", "steps", "answer_steps", "marking_scheme"]
LANGS = [("hi", 0), ("gu", 1)]

folder, lesson_mod, question_mod = sys.argv[1:4]
L = importlib.import_module(lesson_mod)
QM = importlib.import_module(question_mod)
missing = []

def auto(text, lang, field):
    if is_math_only(text):
        return text
    t = by_template(text, lang)
    if t is not None:
        return t
    if field == "marking_scheme" and text in MARKING:
        return MARKING[text][0 if lang == "hi" else 1]
    return None

def translate_item(item, table):
    iid = item["id"]
    for field in TEXT + LISTS:
        english = item.get(field)
        if english in (None, "", []) or not isinstance(english, (str, list)):
            continue
        key = f"{iid}.{field}"
        for lang, idx in LANGS:
            if key in table:
                value = table[key][idx]
                if isinstance(english, list) and len(value) != len(english):
                    missing.append(f"{key} [{lang}]: {len(value)} entries, English has {len(english)}")
                    continue
                item[f"{field}_{lang}"] = value
            elif isinstance(english, str):
                value = auto(english, lang, field)
                if value is None:
                    missing.append(f"{key} [{lang}]: {english[:70]!r}")
                else:
                    item[f"{field}_{lang}"] = value
            else:
                out = []
                for i, e in enumerate(english):
                    v = auto(e, lang, field) if isinstance(e, str) else e
                    if v is None:
                        missing.append(f"{key}[{i}] [{lang}]: {e[:70]!r}")
                    out.append(v)
                if None not in out:
                    item[f"{field}_{lang}"] = out
    figure = item.get("figure")
    if isinstance(figure, dict) and figure.get("title"):
        key = f"{iid}.figure.title"
        if key in table:
            figure["title_hi"], figure["title_gu"] = table[key]
        else:
            missing.append(f"{key}: {figure['title']!r}")

chapter_path, questions_path = f"{folder}/chapter.json", f"{folder}/questions.json"
chapter = json.load(open(chapter_path, encoding="utf-8"))
bank = json.load(open(questions_path, encoding="utf-8"))

chapter["title_hi"], chapter["title_gu"] = L.META["title"]
for section in chapter["sections"]:
    if section["id"] in L.SECTIONS:
        section["title_hi"], section["title_gu"] = L.SECTIONS[section["id"]]
    else:
        missing.append(f"section {section['id']} title")
    for block in section["blocks"]:
        translate_item(block, L.T)

for q in bank["questions"]:
    if q["type"] == "assertion_reason":
        spec = QM.AR.get(q["id"])
        if spec is None:
            missing.append(f"{q['id']}: assertion-reason translation"); continue
        a_hi, r_hi, a_gu, r_gu, wa_hi, wr_hi, wa_gu, wr_gu, ex_hi, ex_gu = spec
        for lang, a, r, wa, wr, ex, idx in (("hi", a_hi, r_hi, wa_hi, wr_hi, ex_hi, 0), ("gu", a_gu, r_gu, wa_gu, wr_gu, ex_gu, 1)):
            la, lr = AR_LABELS[idx]
            q[f"question_{lang}"] = f"{la} {a}\n\n{lr} {r}"
            q[f"explanation_{lang}"] = ex
            q[f"options_{lang}"] = AR_OPTIONS[idx]
            q[f"option_feedback_{lang}"] = ar_feedback(q["correct_index"], wa, wr, lang)
        ms = q.get("marking_scheme")
        if ms:
            translate_item({"id": q["id"], "marking_scheme": ms}, {})
        continue
    translate_item(q, QM.Q)

if missing:
    print(f"{len(missing)} texts still need translation:")
    print("\n".join(missing))
    sys.exit(1)

chapter["languages"] = ["en", "hi", "gu"]
for path, data in ((chapter_path, chapter), (questions_path, bank)):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
print("Translations applied: Hindi and Gujarati complete for", chapter["title"])
