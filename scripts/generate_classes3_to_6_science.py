import json
import os

classes = [3, 4, 5, 6]
chapters_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

for cls in classes:
    fpath = f"/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/gseb_class{cls}.json"
    with open(fpath, "r") as f:
        data = json.load(f)
        
    for sub in data["subjects"]:
        if sub["name"] == "Science":
            for ch in sub["chapters"]:
                original_id = ch.get("chapter_id")
                title = ch.get("title")
                
                # Remove _mock to get the real chapter ID
                if original_id.endswith("_mock"):
                    real_id = original_id[:-5]
                else:
                    real_id = original_id
                    
                print(f"Generating skeleton for {real_id}: {title}")
                
                skeleton = {
                    "metadata": {
                        "id": real_id,
                        "title": title,
                        "subject": "Science",
                        "class_level": f"Class {cls}",
                        "difficulty": "Beginner",
                        "estimated_minutes": 30
                    },
                    "blocks": [
                        {
                            "type": "real_world_example",
                            "metadata": {"difficulty": "Beginner", "bloom": "Understand"},
                            "content": {
                                "title": "The Hook",
                                "text": f"Imagine you are exploring {title}. What would you do? Let's discover the magic behind it!"
                            }
                        },
                        {
                            "type": "ai_tutor_prompt",
                            "metadata": {"difficulty": "Beginner", "bloom": "Analyze"},
                            "content": {
                                "question": f"Why do you think learning about {title} is important?",
                                "options": ["It is fun", "It helps us understand the world", "It is just for exams"],
                                "correct_answer": "It helps us understand the world",
                                "feedback_on_correct": "Spot on! Science is about understanding the world.",
                                "feedback_on_incorrect": "Not quite! Think about the real world."
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
                            "type": "definition",
                            "metadata": {"difficulty": "Intermediate", "bloom": "Remember"},
                            "content": {
                                "term": "Key Term",
                                "definition": f"A fundamental building block of {title}."
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
                        },
                        {
                            "type": "reflection",
                            "metadata": {"difficulty": "Advanced", "bloom": "Evaluate"},
                            "content": {
                                "prompt": f"Reflect on what you have learned in {title}. Can you explain it to a friend?",
                                "guidance": "Think about the simplest way to describe it."
                            }
                        }
                    ]
                }
                
                output_path = os.path.join(chapters_dir, f"{real_id}.json")
                with open(output_path, "w") as f:
                    json.dump(skeleton, f, indent=2)
                    
print("Skeleton generation complete!")
