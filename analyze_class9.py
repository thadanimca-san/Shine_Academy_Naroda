import glob
import json
import os

chapter_files = glob.glob('app_core/chapters/*class9*.json')
curriculum_files = glob.glob('app_core/curriculum/*class9*.json')
chapters_dir = 'app_core/chapters/'

missing_curriculum_files = []
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
                            missing_curriculum_files.append(file_name)
                        else:
                            existing_chapters += 1
    except Exception as e:
        print(f"Error reading {c_file}: {e}")

blocks_checked = 0
missing_ids = 0
missing_translations = 0

for f in chapter_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for block in data.get('blocks', []):
                blocks_checked += 1
                if 'id' not in block or block['id'] == 'UNKNOWN_ID':
                    missing_ids += 1
                
                # Check translations based on block type
                keys_to_check = []
                if block['type'] == 'theory':
                    keys_to_check = ['title', 'body']
                elif block['type'] == 'mcq':
                    keys_to_check = ['question', 'options', 'explanation']
                elif block['type'] == 'practice_question':
                    keys_to_check = ['title', 'body']
                    
                for key in keys_to_check:
                    if key in block and f"{key}_hi" not in block:
                        missing_translations += 1
                        break
    except Exception as e:
        pass

print("=== Class 9 Analysis ===")
print(f"Total Curriculum Files: {len(curriculum_files)}")
print(f"Total Chapters defined: {total_chapters}")
print(f"Existing Chapters: {existing_chapters}")
print(f"Missing Chapters: {len(missing_curriculum_files)}")
if missing_curriculum_files:
    print(f"Missing sample: {missing_curriculum_files[:5]}")

print(f"\nTotal Blocks Checked: {blocks_checked}")
print(f"Blocks missing IDs: {missing_ids}")
print(f"Blocks missing Hindi translations: {missing_translations}")

