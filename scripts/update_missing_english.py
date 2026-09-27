import json

def update_missing_english():
    print("Fixing missing Class 1 English chapters...")
    
    # Chapter 6: Pronouns
    ch6 = {
        "metadata": {
            "id": "class1_english_ch6",
            "title": "Pronouns",
            "subject": "English",
            "difficulty": "Beginner",
            "estimated_minutes": 15
        },
        "blocks": [
            {"id": "KOBJ_C1_ENG_6_01", "type": "hook", "title": "Who is Who?", "body": "Instead of saying a name again and again, what do we use?"},
            {"id": "KOBJ_C1_ENG_6_02", "type": "theory", "title": "Pronouns", "body": "Words like He, She, It, and They are Pronouns!\nWe use them instead of a Noun."},
            {"id": "KOBJ_C1_ENG_6_03", "type": "flashcard", "front": "A boy", "back": "He", "color": "0xFF2196F3"},
            {"id": "KOBJ_C1_ENG_6_04", "type": "flashcard", "front": "A girl", "back": "She", "color": "0xFFE91E63"},
            {"id": "KOBJ_C1_ENG_6_05", "type": "flashcard", "front": "A dog", "back": "It", "color": "0xFFFF9800"},
            {"id": "KOBJ_C1_ENG_6_06", "type": "quiz", "question": "For a boy, we use the word:", "options": ["She", "He", "It"], "correct_index": 1, "explanation": "'He' is used for a boy or a man."}
        ]
    }
    
    # Chapter 7: Adjectives
    ch7 = {
        "metadata": {
            "id": "class1_english_ch7",
            "title": "Adjectives",
            "subject": "English",
            "difficulty": "Beginner",
            "estimated_minutes": 15
        },
        "blocks": [
            {"id": "KOBJ_C1_ENG_7_01", "type": "hook", "title": "Describing Things", "body": "How do you tell someone about your new toy? Is it big? Is it red?"},
            {"id": "KOBJ_C1_ENG_7_02", "type": "theory", "title": "Adjectives", "body": "Adjectives describe Nouns!\nWords like Big, Small, Red, and Happy."},
            {"id": "KOBJ_C1_ENG_7_03", "type": "flashcard", "front": "The elephant is...", "back": "Big!", "color": "0xFF9C27B0"},
            {"id": "KOBJ_C1_ENG_7_04", "type": "flashcard", "front": "The sun is...", "back": "Hot!", "color": "0xFFFFC107"},
            {"id": "KOBJ_C1_ENG_7_05", "type": "quiz", "question": "Which of these is an Adjective?", "options": ["Happy", "Dog", "Run"], "correct_index": 0, "explanation": "'Happy' describes how you feel!"}
        ]
    }

    # Chapter 8: Reading Comprehension
    ch8 = {
        "metadata": {
            "id": "class1_english_ch8",
            "title": "Reading Comprehension",
            "subject": "English",
            "difficulty": "Beginner",
            "estimated_minutes": 15
        },
        "blocks": [
            {"id": "KOBJ_C1_ENG_8_01", "type": "hook", "title": "Let's Read a Story!", "body": "Read the story and answer the questions."},
            {"id": "KOBJ_C1_ENG_8_02", "type": "theory", "title": "Tom's Cat", "body": "Tom has a cat. The cat is black. The cat likes to sleep on the mat."},
            {"id": "KOBJ_C1_ENG_8_03", "type": "quiz", "question": "Who has a cat?", "options": ["Tom", "Jerry", "Sam"], "correct_index": 0, "explanation": "The story says 'Tom has a cat.'"},
            {"id": "KOBJ_C1_ENG_8_04", "type": "quiz", "question": "What color is the cat?", "options": ["White", "Black", "Brown"], "correct_index": 1, "explanation": "The story says 'The cat is black.'"},
            {"id": "KOBJ_C1_ENG_8_05", "type": "quiz", "question": "Where does the cat sleep?", "options": ["On the bed", "On the mat", "In a box"], "correct_index": 1, "explanation": "The cat likes to sleep on the mat."}
        ]
    }
    
    chapters = [ch6, ch7, ch8]
    
    for i, ch in enumerate(chapters):
        filepath = f"app_core/chapters/class1_english_ch{i+6}.json"
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(ch, f, indent=2, ensure_ascii=False)
            
    print("Successfully updated missing Class 1 English chapters!")

if __name__ == "__main__":
    update_missing_english()
