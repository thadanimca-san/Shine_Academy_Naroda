import json
import os
import glob

curriculum_files = glob.glob('app_core/curriculum/*class10*.json')
chapters_dir = 'app_core/chapters/'

missing_files = []
total_chapters = 0
existing_chapters = 0

for c_file in curriculum_files:
    try:
        with open(c_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            board = c_file.split('/')[-1].replace('.json', '')
            
            for subject in data.get('subjects', []):
                for chapter in subject.get('chapters', []):
                    total_chapters += 1
                    module_id = chapter.get('module_id')
                    if module_id:
                        file_name = f"{module_id}.json"
                        full_path = os.path.join(chapters_dir, file_name)
                        if not os.path.exists(full_path):
                            missing_files.append((board, subject.get('name'), chapter.get('title'), file_name))
                        else:
                            existing_chapters += 1
    except Exception as e:
        print(f"Error reading {c_file}: {e}")

print(f"Total Chapters defined in curriculum: {total_chapters}")
print(f"Existing Chapter Files: {existing_chapters}")
print(f"Missing Chapter Files: {len(missing_files)}")

if missing_files:
    print("\nSample missing files:")
    for m in missing_files[:20]:
        print(m)

