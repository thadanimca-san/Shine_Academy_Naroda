import json
import os

curriculum_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum'

board_papers_subject = {
    "id_suffix": "_board_papers",
    "name": "Past Board Papers (Solved)",
    "color_hex": "0xFFD32F2F", # Deep Red
    "icon": "history_edu",
    "chapters": [
        "Science - March 2026 (Solved)",
        "Maths (Standard) - March 2026 (Solved)",
        "Social Science - March 2026 (Solved)",
        "English (First Language) - March 2026 (Solved)",
        "Science - March 2025 (Solved)",
        "Maths (Standard) - March 2025 (Solved)",
        "Social Science - March 2025 (Solved)",
        "English (First Language) - March 2025 (Solved)",
        "Science - March 2024 (Solved)",
        "Maths (Standard) - March 2024 (Solved)",
        "Social Science - March 2024 (Solved)",
        "English (First Language) - March 2024 (Solved)"
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
    
    sub_id = f"{prefix}_class10{board_papers_subject['id_suffix']}"
    
    # Find if it already exists
    subject_obj = None
    for s in data.get('subjects', []):
        if s.get('id') == sub_id:
            subject_obj = s
            break
            
    if not subject_obj:
        subject_obj = {
            "id": sub_id,
            "name": board_papers_subject['name'],
            "color_hex": board_papers_subject['color_hex'],
            "icon": board_papers_subject['icon'],
            "chapters": []
        }
        data['subjects'].append(subject_obj)
        
    subject_obj['chapters'] = []
    for i, title in enumerate(board_papers_subject['chapters']):
        subject_obj['chapters'].append({
            "chapter_id": f"{sub_id}_ch{i+1}",
            "title": title,
            "module_id": f"{sub_id}_ch{i+1}"
        })

    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
        
    print(f"Updated {filename} with 2024-2026 Board Papers.")
