"""Registers a Class 10 English grammar chapter: python3 register_grammar.py N folder 'Title' legacy_alias (run from the repo root).
The alias is the old module id (e.g. ncert_class10_grammar_ch1), so the existing English Grammar list opens the new content."""
import json, sys
n, folder, title, alias = int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4]
cid = f"cbse.c10.english.grammar.ch{n:02d}"
path = f"app_core/content/cbse/class10/english/grammar/{folder}"
d = json.load(open("app_core/content/index.json"))
if not any(x["id"] == cid for x in d["chapters"]):
    d["chapters"].append({"id": cid, "path": path, "board": "CBSE", "class": 10, "subject": "english_grammar", "chapter_number": n, "title": title, "aliases": [alias]})
    open("app_core/content/index.json", "w").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
s = open("pubspec.yaml").read()
if path + "/" not in s:
    last = [l for l in s.splitlines(True) if "app_core/content/cbse/class10/" in l][-1]
    s = s.replace(last, last + last.split("- ")[0] + f"- {path}/\n", 1)
    open("pubspec.yaml", "w").write(s)
t = open("test/quiz_game_screen_test.dart").read()
if f"'{alias}'" not in t:
    t = t.replace("'ncert_class10_science_ch13'", f"'ncert_class10_science_ch13', '{alias}'", 1) if "grammar" not in t else \
        t.replace("']) {", f"', '{alias}']) {{", 1)
    open("test/quiz_game_screen_test.dart", "w").write(t)
