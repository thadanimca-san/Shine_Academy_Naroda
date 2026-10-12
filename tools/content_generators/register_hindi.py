"""Registers a Hindi Course B chapter (run from the repo root):
    python3 register_hindi.py book key N folder 'Title' alias
The alias is the module id in app_core/curriculum/cbse_class10.json (cbse_class10_hindiB_chN), so the existing
Hindi B list opens the new content."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from hindi_common import path as h_path, SUBJECT

book, key, n, folder, title, alias = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5], sys.argv[6]
cid, p = f"cbse.c10.hindi_b.{book}.{key}", h_path(book, folder)
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
print("registered", cid, alias)
