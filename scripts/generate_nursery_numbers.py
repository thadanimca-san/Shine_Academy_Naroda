import json
import os

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def generate_nursery_numbers():
    # We generate numbers 1 to 10
    number_words = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
    
    for i in range(1, 11):
        num = i
        word = number_words[i-1]
        chapter_id = f"nursery_numbers_ch{i}"
        
        if num == 1:
            hook = "Look up at the sky at night! How many moons do you see? Just ONE!"
            examples = "One sun, one moon, one nose."
            items = "apple"
        elif num == 2:
            hook = "Look at your face in the mirror! How many eyes do you have? TWO!"
            examples = "Two eyes, two ears, two hands."
            items = "cats"
        elif num == 3:
            hook = "Have you seen a tricycle? How many wheels does it have? THREE!"
            examples = "Three wheels on a tricycle, three colors in a traffic light."
            items = "dogs"
        elif num == 4:
            hook = "Look at a table or a chair. How many legs do they have? FOUR!"
            examples = "Four legs on a dog, four wheels on a car."
            items = "birds"
        elif num == 5:
            hook = "Look at your hand! How many fingers are on one hand? Let's count... FIVE!"
            examples = "Five fingers on a hand, five toes on a foot."
            items = "stars"
        elif num == 6:
            hook = "Did you know insects like ants and butterflies have SIX legs?"
            examples = "Six legs on an ant."
            items = "balls"
        elif num == 7:
            hook = "Look at a beautiful rainbow! Do you know how many colors it has? SEVEN!"
            examples = "Seven colors in a rainbow, seven days in a week."
            items = "balloons"
        elif num == 8:
            hook = "Have you seen an octopus in the ocean? It has EIGHT long arms!"
            examples = "Eight arms on an octopus, eight legs on a spider."
            items = "fish"
        elif num == 9:
            hook = "If you have 10 fingers and you hide one, how many are left? NINE!"
            examples = "Nine planets (historically), nine bowling pins in a standard game (wait, that's 10... let's stick to counting 9 things!)."
            items = "apples"
        else: # 10
            hook = "Show me both your hands! Let's count all your fingers. TEN!"
            examples = "Ten fingers, ten toes."
            items = "fingers"
            
        data = {
            "metadata": {
                "id": chapter_id,
                "title": f"Number {num} ({word})",
                "subject": "Numbers",
                "difficulty": "Beginner",
                "estimated_minutes": 15
            },
            "blocks": [
                {
                    "id": f"KOBJ_NUR_NUM_{num}_01",
                    "type": "hook",
                    "title": "Let's Count!",
                    "body": hook
                },
                {
                    "id": f"KOBJ_NUR_NUM_{num}_02",
                    "type": "theory",
                    "title": f"This is the Number {num}",
                    "body": f"The number {num} is written as '{num}'. {examples}"
                },
                {
                    "id": f"KOBJ_NUR_NUM_{num}_03",
                    "type": "trace_alphabet",
                    "letter": str(num)
                },
                {
                    "id": f"KOBJ_NUR_NUM_{num}_04",
                    "type": "quiz",
                    "question": f"How many {items} are represented by the number {num}?",
                    "options": [str(num), str((num % 10) + 1), str(((num+1) % 10) + 1)],
                    "correct_index": 0,
                    "explanation": f"Exactly! {num} {items}."
                },
                {
                    "id": f"KOBJ_NUR_NUM_{num}_05",
                    "type": "reflection",
                    "title": "Look Around",
                    "body": f"Can you find {num} things in your room right now?"
                }
            ]
        }
        
        filepath = f"app_core/chapters/{chapter_id}.json"
        save_json(data, filepath)
        
    print("Generated all 10 Nursery Number chapters!")

if __name__ == "__main__":
    generate_nursery_numbers()
