import json
import os
from datetime import datetime

def migrate_spcc_12():
    learning_modules_dir = 'app_core/learning_modules'
    chapters_dir = 'app_core/chapters'
    index_file = os.path.join(learning_modules_dir, 'gseb_class12_spcc_chapters.json')
    
    with open(index_file, 'r', encoding='utf-8') as f:
        chapters_index = json.load(f)
        
    for ch in chapters_index:
        module_id = ch['id']  # e.g., gseb_class12_spcc_ch1
        title = ch['title']
        description = ch.get('description', '')
        
        blocks_file = os.path.join(learning_modules_dir, module_id, 'blocks.json')
        if not os.path.exists(blocks_file):
            print(f"Skipping {module_id}, blocks.json not found.")
            continue
            
        with open(blocks_file, 'r', encoding='utf-8') as f:
            blocks = json.load(f)
            
        final_json = {
            "metadata": {
                "id": module_id,
                "title": title,
                "title_hi": title,
                "title_gu": title,
                "subtitle": description,
                "subject": "SPCC",
                "grade": "12",
                "board": "GSEB",
                "curriculum": ["GSEB"],
                "language": "en, hi, gu",
                "difficulty": "Intermediate",
                "estimated_minutes": ch.get('duration_minutes', 30),
                "version": "2.0.0",
                "author": "Antigravity_EduOS",
                "reviewed_by": "System",
                "last_updated": datetime.utcnow().isoformat() + "Z",
                "tags": ["spcc", "class12", "gseb"],
                "learning_outcomes": [description],
                "ai_context": {
                    "learning_goal": description,
                    "common_misconceptions": [],
                    "tutor_hint": "",
                    "next_topics": []
                }
            },
            "blocks": blocks
        }
        
        out_file = os.path.join(chapters_dir, f"{module_id}.json")
        with open(out_file, 'w', encoding='utf-8') as f:
            json.dump(final_json, f, indent=4, ensure_ascii=False)
        print(f"Created {out_file} with {len(blocks)} blocks.")

if __name__ == '__main__':
    migrate_spcc_12()
