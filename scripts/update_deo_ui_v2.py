import json
import os

curriculum_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum'

deo_bank_subject = {
    "id_suffix": "_deo_bank_2026",
    "name": "question Question Bank 2026",
    "color_hex": "0xFFFFD700", # Premium Gold
    "icon": "diamond",
    "chapters": [
        "Science question Bank (Part 1 - MCQs)",
        "Science question Bank (Part 2 - Subject)",
        "Maths Basic question Bank (Part 1 - MCQs)",
        "Maths Basic question Bank (Part 2 - Subject)",
        "Maths Standard question Bank (Part 1 - MCQs)",
        "Maths Standard question Bank (Part 2 - Subject)",
        "Social Science question Bank (Part 1 - MCQs)",
        "Social Science question Bank (Part 2 - Subject)",
        "English (FL) question Bank (Part 1 - MCQs)",
        "English (FL) question Bank (Part 2 - Subject)",
        "Gujarati (SL) question Bank (Part 1 - MCQs)",
        "Gujarati (SL) question Bank (Part 2 - Subject)"
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
    sub_id = f"{prefix}_class10{deo_bank_subject['id_suffix']}"
    
    subject_obj = None
    for s in data['subjects']:
        if s.get('id') == sub_id:
            subject_obj = s
            break
            
    subject_obj['chapters'] = []
    for i, title in enumerate(deo_bank_subject['chapters']):
        subject_obj['chapters'].append({
            "chapter_id": f"{sub_id}_ch{i+1}",
            "title": title,
            "module_id": f"{sub_id}_ch{i+1}"
        })

    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
        
    print(f"Updated {filename}: Added Part 1 and Part 2 for all subjects.")
