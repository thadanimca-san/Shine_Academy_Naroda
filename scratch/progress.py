import json
import os
import glob

curriculum_files = glob.glob('/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/*.json')
total_chapters = 0
completed_chapters = 0

chapter_files = set([os.path.basename(f) for f in glob.glob('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/*.json')])

for cfile in curriculum_files:
    try:
        with open(cfile, 'r') as f:
            data = json.load(f)
            for subject in data.get('subjects', []):
                for chapter in subject.get('chapters', []):
                    total_chapters += 1
                    module_id = chapter.get('module_id')
                    if module_id and f"{module_id}.json" in chapter_files:
                        # Check if file has substantial content
                        file_path = f"/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/{module_id}.json"
                        if os.path.exists(file_path):
                            with open(file_path, 'r') as cf:
                                cdata = json.load(cf)
                                if len(cdata.get('blocks', [])) > 5:
                                    completed_chapters += 1
    except Exception as e:
        pass

print(f"Total mapped chapters in curriculum: {total_chapters}")
print(f"Chapters with substantial JSON files: {completed_chapters}")
if total_chapters > 0:
    print(f"Percentage Completion (Data/Content): {completed_chapters/total_chapters * 100:.2f}%")
