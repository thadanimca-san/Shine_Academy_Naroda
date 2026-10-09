import json
import os

curriculum_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum'

deo_bank_subject = {
    "id_suffix": "_deo_bank_2026",
    "name": "question Question Bank 2026",
    "color_hex": "0xFFFFD700", # Premium Gold
    "icon": "diamond",
    "chapters": [
        "Science question Bank 2026 (Part 1 - MCQs)",
        "Science question Bank 2026 (Part 2 - Subjective)",
        "Maths (Basic) question Bank 2026",
        "Maths (Standard) question Bank 2026",
        "Social Science question Bank 2026",
        "English (FL) question Bank 2026",
        "Gujarati (SL) question Bank 2026"
    ]
}

files_to_update = ['ncert_class10.json', 'gseb_class10.json', 'cbse_class10.json']

for filename in files_to_update:
    filepath = os.path.join(curriculum_dir, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r') as f:
        data = json.load(f)
        
    prefix = filename.split('_')[0]
    
    # 1. Remove the old "_board_papers" subject
    new_subjects = []
    for s in data.get('subjects', []):
        if not s.get('id').endswith('_board_papers'):
            new_subjects.append(s)
    data['subjects'] = new_subjects
    
    # 2. Add the new "_deo_bank_2026" subject
    sub_id = f"{prefix}_class10{deo_bank_subject['id_suffix']}"
    
    subject_obj = None
    for s in data['subjects']:
        if s.get('id') == sub_id:
            subject_obj = s
            break
            
    if not subject_obj:
        subject_obj = {
            "id": sub_id,
            "name": deo_bank_subject['name'],
            "color_hex": deo_bank_subject['color_hex'],
            "icon": deo_bank_subject['icon'],
            "chapters": []
        }
        data['subjects'].append(subject_obj)
        
    subject_obj['chapters'] = []
    for i, title in enumerate(deo_bank_subject['chapters']):
        subject_obj['chapters'].append({
            "chapter_id": f"{sub_id}_ch{i+1}",
            "title": title,
            "module_id": f"{sub_id}_ch{i+1}"
        })

    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
        
    print(f"Updated {filename}: Removed old papers and added question Bank.")
