import json
import os

def patch_cbse():
    path = "/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/cbse_class9.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    for subject in data.get("subjects", []):
        if subject.get("id") == "cbse_class9_science":
            for ch in subject.get("chapters", []):
                if ch.get("chapter_id") == "cbse_class9_science_ch1":
                    ch["title"] = "Chapter 1: Exploration: Entering the World of Secondary Science"
                    ch["module_id"] = "ncert_class9_science_ch1"
                    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def patch_ncert():
    path = "/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/ncert_class9.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    for subject in data.get("subjects", []):
        if subject.get("id") == "ncert_class9_science":
            for ch in subject.get("chapters", []):
                if ch.get("chapter_id") == "ncert_class9_science_ch1":
                    ch["title"] = "Chapter 1: Exploration: Entering the World of Secondary Science"
                    ch["module_id"] = "ncert_class9_science_ch1"
                    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    patch_cbse()
    patch_ncert()
    print("Patched cbse_class9.json and ncert_class9.json")
