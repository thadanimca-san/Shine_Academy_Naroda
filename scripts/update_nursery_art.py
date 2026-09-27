import json
import os

def update_nursery_art():
    print("Updating Nursery Art chapters 1-5...")
    
    shapes = {
        1: "apple",
        2: "star",
        3: "heart",
        4: "sun",
        5: "car"
    }
    
    updated_count = 0
    
    for i in range(1, 6):
        filepath = f"app_core/chapters/nursery_art_ch{i}.json"
        
        if not os.path.exists(filepath):
            continue
            
        shape_name = shapes[i]
        
        data = {
            "metadata": {
                "id": f"nursery_art_ch{i}",
                "title": f"Color the {shape_name.capitalize()}",
                "subject": "Art & Craft",
                "difficulty": "Beginner",
                "estimated_minutes": 15
            },
            "blocks": [
                {
                    "id": f"KOBJ_NUR_ART_{i}_01",
                    "type": "hook",
                    "title": "Time for Magic!",
                    "body": f"Let's bring this {shape_name} to life with some beautiful colors!"
                },
                {
                    "id": f"KOBJ_NUR_ART_{i}_02",
                    "type": "color_canvas",
                    "shape": shape_name
                },
                {
                    "id": f"KOBJ_NUR_ART_{i}_03",
                    "type": "quiz",
                    "question": f"Did you enjoy coloring the {shape_name}?",
                    "options": ["Yes! I love it!", "It was okay."],
                    "correct_index": 0,
                    "explanation": "Art is amazing! Keep exploring your creativity."
                }
            ]
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        updated_count += 1
        
    print(f"Updated {updated_count} Nursery Art chapters.")

if __name__ == "__main__":
    update_nursery_art()
