"""Registers a Class 10 Social Science chapter: python3 register_ss.py subject N folder 'Title' (run from the repo root).
Alias = the old module id ncert_class10_<subject>_chN used by app_core/curriculum/cbse_class10.json."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from ss_common import path as ss_path
subject, n, folder, title = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
cid, alias, p = f"cbse.c10.{subject}.ncert.ch{n:02d}", f"ncert_class10_{subject}_ch{n}", ss_path(subject, folder)
d = json.load(open("app_core/content/index.json"))
if not any(x["id"] == cid for x in d["chapters"]):
    d["chapters"].append({"id": cid, "path": p, "board": "CBSE", "class": 10, "subject": subject, "chapter_number": n, "title": title, "aliases": [alias]})
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
