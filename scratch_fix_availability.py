import json
import os
import glob

curriculum_dir = "app_core/curriculum"
master_file = "app_core/learning_modules/master_curriculum.json"

with open(master_file, "r", encoding="utf-8") as f:
    master_db = json.load(f)
    available_modules = set(master_db.keys())

for file_path in glob.glob(os.path.join(curriculum_dir, "*.json")):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    modified = False
    for subject in data.get("subjects", []):
        for chapter in subject.get("chapters", []):
            mod_id = chapter.get("module_id")
            if mod_id in available_modules:
                if not chapter.get("is_available"):
                    chapter["is_available"] = True
                    modified = True
    
    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            print(f"Updated {file_path}")

