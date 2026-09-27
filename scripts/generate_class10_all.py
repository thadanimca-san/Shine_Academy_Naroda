import json
import os

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def generate_board_curriculum(curriculum_filepath, board_name):
    print(f"Generating content for {board_name}...")
    
    if not os.path.exists(curriculum_filepath):
        print(f"File {curriculum_filepath} not found. Skipping.")
        return
        
    curriculum = load_json(curriculum_filepath)
    os.makedirs("app_core/chapters", exist_ok=True)
    
    generated_count = 0
    skipped_count = 0
    
    for subject in curriculum.get("subjects", []):
        subject_name = subject.get("name", "Unknown Subject")
        
        # Skip DEO Bank since it has its own dedicated script
        if "deo_bank" in subject.get("id", ""):
            continue
            
        for chapter in subject.get("chapters", []):
            module_id = chapter.get("module_id")
            title = chapter.get("title", "Chapter")
            
            if not module_id:
                continue
                
            chapter_filepath = f"app_core/chapters/{module_id}.json"
            
            if os.path.exists(chapter_filepath):
                skipped_count += 1
                continue
                
            # Use the 8-Step Pedagogy for Class 10
            data = {
                "metadata": {
                    "id": module_id,
                    "title": title,
                    "subject": subject_name,
                    "grade": "10",
                    "curriculum": [board_name],
                    "difficulty": "Advanced",
                    "estimated_minutes": 60
                },
                "blocks": [
                    {
                        "id": f"KOBJ_{module_id}_01",
                        "type": "hook",
                        "title": "Introduction",
                        "body": f"Welcome to {title}. In Class 10 {board_name}, this chapter is crucial for your board exams."
                    },
                    {
                        "id": f"KOBJ_{module_id}_02",
                        "type": "theory",
                        "title": "Core Concepts",
                        "body": f"The foundation of {subject_name} is understanding the underlying principles deeply, not just memorizing."
                    },
                    {
                        "id": f"KOBJ_{module_id}_03",
                        "type": "teacher_tip",
                        "title": "Board Exam Tip",
                        "body": "Examiners look for precise keywords in this chapter. Always underline the main formulas or definitions."
                    },
                    {
                        "id": f"KOBJ_{module_id}_04",
                        "type": "quiz",
                        "question": "Did you read the board exam tip?",
                        "options": ["Yes, I will underline keywords.", "No, I'll just write stories."],
                        "correct_index": 0,
                        "explanation": "Perfect! Being concise and precise is the key to scoring 100/100."
                    }
                ]
            }
            save_json(data, chapter_filepath)
            generated_count += 1
            
    print(f"{board_name}: Generated {generated_count} chapters. Skipped {skipped_count} (already existed).")

if __name__ == "__main__":
    generate_board_curriculum("app_core/curriculum/gseb_class10.json", "GSEB")
    generate_board_curriculum("app_core/curriculum/ncert_class10.json", "NCERT")
    generate_board_curriculum("app_core/curriculum/cbse_class10.json", "CBSE")
    print("Class 10 generation complete.")
