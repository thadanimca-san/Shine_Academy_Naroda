"""Registers an English literature chapter (run from the repo root):
    python3 register_lit.py key N folder 'Title' alias [book]
book is first_flight (default) or footprints. Prose aliases are the old module ids (cbse_class10_english_chN,
cbse_class10_english_sup_chN) so the existing English list opens the new content; poems
(cbse_class10_english_poemN) and Footprints chapters missing from the list are added to
app_core/curriculum/cbse_class10.json."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from lit_common import path as lit_path, SUBJECT

key, n, folder, title, alias = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5]
book = sys.argv[6] if len(sys.argv) > 6 else "first_flight"
cid, p = f"cbse.c10.english.{book}.{key}", lit_path(folder, book)

d = json.load(open("app_core/content/index.json"))
if not any(x["id"] == cid for x in d["chapters"]):
    d["chapters"].append({"id": cid, "path": p, "board": "CBSE", "class": 10, "subject": SUBJECT, "chapter_number": n, "title": title, "aliases": [alias]})
    open("app_core/content/index.json", "w").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")

s = open("pubspec.yaml").read()
if p + "/" not in s:
    last = [l for l in s.splitlines(True) if "app_core/content/cbse/class10/" in l][-1]
    s = s.replace(last, last + last.split("- ")[0] + f"- {p}/\n", 1)
    open("pubspec.yaml", "w").write(s)

t = open("test/quiz_game_screen_test.dart").read()
if f"'{alias}'" not in t:
    t = t.replace("']) {", f"', '{alias}']) {{", 1)
    open("test/quiz_game_screen_test.dart", "w").write(t)

cur = json.load(open("app_core/curriculum/cbse_class10.json"))
subjects = cur["subjects"] if isinstance(cur, dict) and "subjects" in cur else cur
eng = next(x for x in subjects if x.get("id") == "cbse_class10_english")

# Poems are new to the English chapter list: add them after the last First Flight entry.
if alias.startswith("cbse_class10_english_poem"):
    if not any(c["chapter_id"] == alias for c in eng["chapters"]):
        at = max(i for i, c in enumerate(eng["chapters"]) if not c["chapter_id"].startswith("cbse_class10_english_sup")) + 1
        eng["chapters"].insert(at, {"chapter_id": alias, "title": f"Poem {n - 9}: {title} (First Flight)", "module_id": alias})
        open("app_core/curriculum/cbse_class10.json", "w").write(json.dumps(cur, ensure_ascii=False, indent=2) + "\n")

# Footprints chapters: one consistent title, added at the end of the list when missing.
if alias.startswith("cbse_class10_english_sup_ch"):
    entry = {"chapter_id": alias, "title": f"Footprints {n - 19}: {title} (Supplementary)", "module_id": alias}
    old = next((c for c in eng["chapters"] if c["chapter_id"] == alias), None)
    if old is None:
        eng["chapters"].append(entry)
    else:
        old["title"] = entry["title"]
    open("app_core/curriculum/cbse_class10.json", "w").write(json.dumps(cur, ensure_ascii=False, indent=2) + "\n")
print("registered", cid, alias)
