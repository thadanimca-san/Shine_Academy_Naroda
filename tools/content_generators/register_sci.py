"""Registers a Class 10 science chapter: python3 register_sci.py N folder 'Title' (run from the repo root)."""
import json, sys
n, folder, title = int(sys.argv[1]), sys.argv[2], sys.argv[3]
cid, prev = f"cbse.c10.science.ncert_rationalised.ch{n:02d}", f"cbse.c10.science.ncert_rationalised.ch{n-1:02d}"
path = f"app_core/content/cbse/class10/science/ncert_rationalised/{folder}"
d = json.load(open("app_core/content/index.json"))
lst = next(v for v in d.values() if isinstance(v, list) and any(isinstance(x, dict) and x.get("id") == prev for x in v))
if not any(x.get("id") == cid for x in lst):
    i = [x.get("id") for x in lst].index(prev)
    lst.insert(i + 1, {"id": cid, "path": path, "board": "CBSE", "class": 10, "subject": "science", "chapter_number": n, "title": title, "aliases": [f"ncert_class10_science_ch{n}"]})
    open("app_core/content/index.json", "w").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
s = open("pubspec.yaml").read()
if folder not in s:
    prev_line = next(l for l in s.splitlines(True) if f"/ncert_rationalised/ch{n-1:02d}_" in l and "science" in l)
    s = s.replace(prev_line, prev_line + prev_line.split("ch")[0] + prev_line[len(prev_line.split("ch")[0]):].replace(prev_line.strip().split("/")[-2], folder), 1)
    open("pubspec.yaml", "w").write(s)
t = open("test/quiz_game_screen_test.dart").read()
if f"science_ch{n}'" not in t:
    t = t.replace(f"'ncert_class10_science_ch{n-1}']", f"'ncert_class10_science_ch{n-1}', 'ncert_class10_science_ch{n}']")
    open("test/quiz_game_screen_test.dart", "w").write(t)
