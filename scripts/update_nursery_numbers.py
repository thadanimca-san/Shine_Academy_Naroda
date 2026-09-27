import json
import os

def update_nursery_numbers():
    print("Updating Nursery Numbers chapters 1-10...")
    
    emojis = {
        1: "🍎", # 1 Apple
        2: "🎈", # 2 Balloons
        3: "⭐️", # 3 Stars
        4: "🚗", # 4 Cars
        5: "🌸", # 5 Flowers
        6: "🦋", # 6 Butterflies
        7: "🐟", # 7 Fish
        8: "🐶", # 8 Dogs
        9: "🍓", # 9 Strawberries
        10: "⚽️" # 10 Footballs
    }
    
    updated_count = 0
    
    for i in range(1, 11):
        filepath = f"app_core/chapters/nursery_numbers_ch{i}.json"
        
        if not os.path.exists(filepath):
            continue
            
        data = {
            "metadata": {
                "id": f"nursery_numbers_ch{i}",
                "title": f"Number {i}",
                "subject": "Numbers",
                "difficulty": "Beginner",
                "estimated_minutes": 15
            },
            "blocks": [
                {
                    "id": f"KOBJ_NUR_NUM_{i}_01",
                    "type": "hook",
                    "title": "Let's Count!",
                    "body": f"Today we are going to learn the number {i}!"
                },
                {
                    "id": f"KOBJ_NUR_NUM_{i}_02",
                    "type": "counting_game",
                    "target_number": i,
                    "item_emoji": emojis.get(i, "⭐️")
                },
                {
                    "id": f"KOBJ_NUR_NUM_{i}_03",
                    "type": "trace_alphabet",
                    "letter": str(i)
                },
                {
                    "id": f"KOBJ_NUR_NUM_{i}_04",
                    "type": "quiz",
                    "question": f"Which number comes after {i-1 if i > 1 else 0}?",
                    "options": [str(i), str(i+1), str(i+2)],
                    "correct_index": 0,
                    "explanation": f"Exactly! The number is {i}."
                }
            ]
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        updated_count += 1
        
    print(f"Updated {updated_count} Nursery Number chapters.")

if __name__ == "__main__":
    update_nursery_numbers()
