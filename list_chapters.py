import json
import os

for cls in [3, 4, 5, 6]:
    fpath = f"/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/gseb_class{cls}.json"
    with open(fpath, "r") as f:
        data = json.load(f)
    for sub in data["subjects"]:
        if sub["name"] == "Science":
            print(f"--- Class {cls} Science Chapters ---")
            for ch in sub["chapters"]:
                print(f"{ch.get('chapter_id')}: {ch.get('title')}")
