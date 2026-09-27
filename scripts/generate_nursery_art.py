import json

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def generate_nursery_art():
    chapters = [
        ("apple", "Color the Apple", "Apples are delicious and healthy!", "What color is an apple? It can be Red or Green!"),
        ("star", "Color the Star", "Twinkle twinkle little star!", "Stars shine bright in the night sky. Usually we color them Yellow."),
        ("heart", "Color the Heart", "A heart means love!", "We usually color a heart Red or Pink."),
        ("sun", "Color the Sun", "The sun gives us light and keeps us warm.", "The sun is very bright! We color it Yellow or Orange."),
        ("car", "Color the Car", "Vroom vroom! Let's go for a ride.", "Cars can be any color! What is your favorite color for a car?")
    ]
    
    for i, (shape, title, hook, body) in enumerate(chapters):
        chapter_id = f"nursery_art_ch{i+1}"
        
        data = {
            "metadata": {
                "id": chapter_id,
                "title": title,
                "subject": "Art & Craft",
                "difficulty": "Beginner",
                "estimated_minutes": 10
            },
            "blocks": [
                {
                    "id": f"KOBJ_NUR_ART_{i+1}_01",
                    "type": "hook",
                    "title": "Art Time!",
                    "body": hook
                },
                {
                    "id": f"KOBJ_NUR_ART_{i+1}_02",
                    "type": "theory",
                    "title": "Let's Learn Colors",
                    "body": body
                },
                {
                    "id": f"KOBJ_NUR_ART_{i+1}_03",
                    "type": "color_canvas",
                    "shape": shape
                },
                {
                    "id": f"KOBJ_NUR_ART_{i+1}_04",
                    "type": "reflection",
                    "title": "Great Job!",
                    "body": f"You made a beautiful {shape}! What other colors would look nice on it?"
                }
            ]
        }
        
        filepath = f"app_core/chapters/{chapter_id}.json"
        save_json(data, filepath)
        
    print("Generated all 5 Nursery Art & Craft chapters!")

if __name__ == "__main__":
    generate_nursery_art()
