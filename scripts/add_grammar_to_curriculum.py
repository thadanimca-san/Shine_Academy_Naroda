import json
import os

CURRICULUM_PATH = '/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/master_curriculum.json'

with open(CURRICULUM_PATH, 'r', encoding='utf-8') as f:
    curriculum = json.load(f)

# Find cbse_class10_english and add grammar chapters if they don't exist
class_key = "cbse_class10"
if class_key in curriculum["classes"]:
    subjects = curriculum["classes"][class_key]["subjects"]
    english_subject = next((s for s in subjects if s["id"] == "cbse_class10_english"), None)
    
    if english_subject:
        # Check if grammar section exists
        grammar_chapters = [
            {"id": "cbse_class10_english_grammar_ch1", "title": "Tenses: The Master Clock"},
            {"id": "cbse_class10_english_grammar_ch2", "title": "Modals: The Mood Ring"},
            {"id": "cbse_class10_english_grammar_ch3", "title": "Subject-Verb Concord"},
            {"id": "cbse_class10_english_grammar_ch4", "title": "Reported Speech"},
            {"id": "cbse_class10_english_grammar_ch5", "title": "Determiners"}
        ]
        
        existing_ids = [ch["id"] for ch in english_subject.get("chapters", [])]
        added = 0
        for ch in grammar_chapters:
            if ch["id"] not in existing_ids:
                english_subject["chapters"].append(ch)
                added += 1
                
        if added > 0:
            with open(CURRICULUM_PATH, 'w', encoding='utf-8') as f:
                json.dump(curriculum, f, indent=2, ensure_ascii=False)
            print(f"Added {added} grammar chapters to master_curriculum.json")
        else:
            print("Grammar chapters already exist in master_curriculum.json")
    else:
        print("Could not find cbse_class10_english subject")
else:
    print("Could not find cbse_class10 class")
