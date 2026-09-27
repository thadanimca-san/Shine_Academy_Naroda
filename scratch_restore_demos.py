import json
import os

def restore_demo(file_path, subject_id, chapter_title, data_file):
    if not os.path.exists(file_path): return
    with open(file_path, 'r') as f:
        data = json.load(f)
    for subj in data.get('subjects', []):
        if subj['id'] == subject_id:
            for ch in subj.get('chapters', []):
                # We can just check chapter_number == 1 or title match
                if ch.get('chapter_number') == 1 or chapter_title in ch.get('title', ''):
                    ch['data_file'] = data_file
                    if 'module_id' in ch:
                        del ch['module_id']
                    print(f"Restored {data_file} in {file_path}")
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

restore_demo('app_core/curriculum/nursery.json', 'rhymes', 'Twinkle', 'assets/chapters/nursery_rhymes.json')
restore_demo('app_core/curriculum/lkg.json', 'english', 'Alphabet', 'assets/chapters/alphabet_tracing.json')
restore_demo('app_core/curriculum/class1.json', 'maths', 'Basics', 'assets/chapters/basic_math.json')
restore_demo('app_core/curriculum/gseb_class9.json', 'science', 'Matter', 'assets/chapters/cbse_class9_science_ch1.json')
