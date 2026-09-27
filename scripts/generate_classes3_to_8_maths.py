import json
import os

classes = [3, 4, 5, 6, 7, 8]
chapters_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

for cls in classes:
    fpath = f"/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/gseb_class{cls}.json"
    if not os.path.exists(fpath):
        continue
        
    with open(fpath, "r") as f:
        data = json.load(f)
        
    for sub in data.get("subjects", []):
        if sub["name"] == "Maths":
            for ch in sub.get("chapters", []):
                original_id = ch.get("chapter_id")
                title = ch.get("title")
                
                if not original_id or not title:
                    continue
                
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
                        "subject": "Maths",
                        "class_level": f"Class {cls}",
                        "difficulty": "Beginner",
                        "estimated_minutes": 30
                    },
                    "blocks": [
                        {
                            "type": "real_world_example",
                            "metadata": {"difficulty": "Beginner", "bloom": "Understand"},
                            "content": {
                                "title": "Math in the Real World",
                                "text": f"Math is everywhere around us! Imagine you need to use {title} in your daily life. Let's see how it works!"
                            }
                        },
                        {
                            "type": "ai_tutor_prompt",
                            "metadata": {"difficulty": "Beginner", "bloom": "Analyze"},
                            "content": {
                                "question": f"Why do you think {title} is an important math concept?",
                                "options": ["It helps us solve problems", "It is just for exams", "It is boring"],
                                "correct_answer": "It helps us solve problems",
                                "feedback_on_correct": "Spot on! Math is the best tool for problem solving.",
                                "feedback_on_incorrect": "Not quite! Think about how math helps us build things and calculate."
                            }
                        },
                        {
                            "type": "theory",
                            "metadata": {"difficulty": "Intermediate", "bloom": "Understand"},
                            "content": {
                                "title": "Core Concept",
                                "text": f"This is the core concept of {title}. Learning this will give you a strong foundation in Mathematics."
                            }
                        },
                        {
                            "type": "definition",
                            "metadata": {"difficulty": "Intermediate", "bloom": "Remember"},
                            "content": {
                                "term": "Key Formula",
                                "formula": f"Formula for {title} = Concept x Practice"
                            }
                        },
                        {
                            "type": "practice_question",
                            "metadata": {"difficulty": "Intermediate", "bloom": "Apply"},
                            "content": {
                                "question": f"If you apply the rules of {title}, what is the correct result?",
                                "options": ["Correct Result", "Wrong Result 1", "Wrong Result 2", "Wrong Result 3"],
                                "correct_answer": "Correct Result",
                                "explanation": "You followed the formula perfectly!"
                            }
                        },
                        {
                            "type": "reflection",
                            "metadata": {"difficulty": "Advanced", "bloom": "Evaluate"},
                            "content": {
                                "prompt": f"Reflect on how {title} connects to other math topics you've learned.",
                                "guidance": "Think about patterns and logical steps."
                            }
                        }
                    ]
                }
                
                output_path = os.path.join(chapters_dir, f"{real_id}.json")
                with open(output_path, "w") as f:
                    json.dump(skeleton, f, indent=2)
                    
print("Maths skeleton generation complete!")
