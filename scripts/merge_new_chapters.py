import os
import json

chapters_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"
master_file = "/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/master_curriculum.json"

print("Loading master_curriculum.json...")
with open(master_file, 'r', encoding='utf-8') as f:
    master_data = json.load(f)

count = 0
for file in sorted(os.listdir(chapters_dir)):
    if file.endswith(".json"):
        filepath = os.path.join(chapters_dir, file)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                chapter_data = json.load(f)
            
            # Extract chapter_id from filename or metadata
            chapter_id = file.replace(".json", "")
            if "metadata" in chapter_data and "id" in chapter_data["metadata"]:
                chapter_id = chapter_data["metadata"]["id"]
                
            master_data[chapter_id] = chapter_data
            count += 1
            print(f"  [+] Merged {chapter_id}")
        except Exception as e:
            print(f"  [!] Error processing {file}: {e}")

print(f"Writing updated data to {master_file}...")
with open(master_file, 'w', encoding='utf-8') as f:
    json.dump(master_data, f, indent=2, ensure_ascii=False)

print(f"Successfully merged {count} newly generated chapters into master_curriculum.json!")
