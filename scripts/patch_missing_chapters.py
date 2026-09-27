import json
import os

curriculum_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum"
chapters_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

missing_count = 0

for file in os.listdir(curriculum_dir):
    if not file.endswith(".json"):
        continue
        
    filepath = os.path.join(curriculum_dir, file)
    with open(filepath, "r") as f:
        data = json.load(f)
        
    for sub in data.get("subjects", []):
        for ch in sub.get("chapters", []):
            module_id = ch.get("module_id") or ch.get("chapter_id")
            title = ch.get("title", "Untitled Chapter")
            
            if not module_id:
                continue
                
            # Remove _mock if it's there
            if module_id.endswith("_mock"):
                module_id = module_id[:-5]
                
            chapter_filepath = os.path.join(chapters_dir, f"{module_id}.json")
            
            if not os.path.exists(chapter_filepath):
                print(f"Missing chapter found: {module_id} in {file}")
                
                # Generate a generic skeleton
                skeleton = {
                    "metadata": {
                        "id": module_id,
                        "title": title,
                        "subject": sub.get("name", "Unknown"),
                        "difficulty": "Beginner",
                        "estimated_minutes": 30
                    },
                    "blocks": [
                        {
                            "type": "real_world_example",
                            "metadata": {"difficulty": "Beginner", "bloom": "Understand"},
                            "content": {
                                "title": "The Hook",
                                "text": f"Welcome to {title}! Let's explore the real-world applications of this topic."
                            }
                        },
                        {
                            "type": "ai_tutor_prompt",
                            "metadata": {"difficulty": "Beginner", "bloom": "Analyze"},
                            "content": {
                                "question": f"Why do you think {title} is an important concept?",
                                "options": ["It helps us solve problems", "It is just for exams", "It is boring"],
                                "correct_answer": "It helps us solve problems",
                                "feedback_on_correct": "Spot on!",
                                "feedback_on_incorrect": "Not quite! Think about how it helps us."
                            }
                        },
                        {
                            "type": "theory",
                            "metadata": {"difficulty": "Intermediate", "bloom": "Understand"},
                            "content": {
                                "title": "Core Concept",
                                "text": f"This is the core concept of {title}. Learning this will give you a strong foundation."
                            }
                        },
                        {
                            "type": "practice_question",
                            "metadata": {"difficulty": "Intermediate", "bloom": "Apply"},
                            "content": {
                                "question": f"What is the most important aspect of {title}?",
                                "options": ["Option A", "Option B", "Option C", "Option D"],
                                "correct_answer": "Option A",
                                "explanation": "Option A is correct because it directly relates to the concept."
                            }
                        }
                    ]
                }
                
                with open(chapter_filepath, "w") as out_f:
                    json.dump(skeleton, out_f, indent=2)
                missing_count += 1
                
print(f"Generated {missing_count} missing chapters to prevent crashes.")
