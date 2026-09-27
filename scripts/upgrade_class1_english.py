import json

def upgrade_class1_english():
    print("Upgrading Class 1 English Chapters...")
    
    # Chapter 1: Alphabet Review
    ch1 = {
        "metadata": {
            "id": "class1_english_ch1",
            "title": "Alphabet Review",
            "subject": "English",
            "difficulty": "Beginner",
            "estimated_minutes": 15
        },
        "blocks": [
            {"id": "KOBJ_C1_ENG_1_01", "type": "hook", "title": "Let's Review!", "body": "Do you remember your ABCs? Let's trace and learn!"},
            {"id": "KOBJ_C1_ENG_1_02", "type": "trace_alphabet", "letter": "A"},
            {"id": "KOBJ_C1_ENG_1_03", "type": "flashcard", "front": "A is for Apple", "back": "Apple", "color": "0xFFE91E63"},
            {"id": "KOBJ_C1_ENG_1_04", "type": "trace_alphabet", "letter": "B"},
            {"id": "KOBJ_C1_ENG_1_05", "type": "flashcard", "front": "B is for Ball", "back": "Ball", "color": "0xFF2196F3"}
        ]
    }
    
    # Chapter 2: Vowels and Consonants
    ch2 = {
        "metadata": {
            "id": "class1_english_ch2",
            "title": "Vowels and Consonants",
            "subject": "English",
            "difficulty": "Beginner",
            "estimated_minutes": 15
        },
        "blocks": [
            {"id": "KOBJ_C1_ENG_2_01", "type": "hook", "title": "Vowels are Special!", "body": "There are 5 special letters in the alphabet. Can you name them?"},
            {"id": "KOBJ_C1_ENG_2_02", "type": "flashcard", "front": "What are the 5 Vowels?", "back": "A, E, I, O, U", "color": "0xFFFF9800"},
            {"id": "KOBJ_C1_ENG_2_03", "type": "theory", "title": "Consonants", "body": "All the other letters are called Consonants!\nLike B, C, D, F, G..."},
            {"id": "KOBJ_C1_ENG_2_04", "type": "quiz", "question": "Is the letter 'A' a vowel or a consonant?", "options": ["Vowel", "Consonant"], "correct_index": 0, "explanation": "A is the first vowel!"}
        ]
    }
    
    # Chapter 3: Sight Words
    ch3 = {
        "metadata": {
            "id": "class1_english_ch3",
            "title": "Sight Words",
            "subject": "English",
            "difficulty": "Beginner",
            "estimated_minutes": 15
        },
        "blocks": [
            {"id": "KOBJ_C1_ENG_3_01", "type": "hook", "title": "Magic Words", "body": "These are words you will see everywhere! Try to read them fast!"}
        ]
    }
    words = ["The", "And", "You", "That", "It"]
    for i, word in enumerate(words):
        ch3["blocks"].append({
            "id": f"KOBJ_C1_ENG_3_{i+2:02d}",
            "type": "flashcard",
            "front": f"Read this: {word}",
            "back": word,
            "color": "0xFF9C27B0"
        })
        
    # Chapter 4: Nouns (Naming Words)
    ch4 = {
        "metadata": {
            "id": "class1_english_ch4",
            "title": "Nouns (Naming Words)",
            "subject": "English",
            "difficulty": "Beginner",
            "estimated_minutes": 15
        },
        "blocks": [
            {"id": "KOBJ_C1_ENG_4_01", "type": "hook", "title": "What's in a Name?", "body": "Everything around you has a name! People, places, animals, and things."},
            {"id": "KOBJ_C1_ENG_4_02", "type": "theory", "title": "What is a Noun?", "body": "A noun is a naming word. Examples: Boy, Dog, School, Apple."},
            {"id": "KOBJ_C1_ENG_4_03", "type": "quiz", "question": "Which of these is a noun?", "options": ["Run", "Cat", "Jump"], "correct_index": 1, "explanation": "Cat is an animal, so it is a noun!"}
        ]
    }
    
    # Chapter 5: Verbs (Action Words)
    ch5 = {
        "metadata": {
            "id": "class1_english_ch5",
            "title": "Verbs (Action Words)",
            "subject": "English",
            "difficulty": "Beginner",
            "estimated_minutes": 15
        },
        "blocks": [
            {"id": "KOBJ_C1_ENG_5_01", "type": "hook", "title": "Lights, Camera, Action!", "body": "What are you doing right now? Reading? Sitting? Those are action words!"},
            {"id": "KOBJ_C1_ENG_5_02", "type": "theory", "title": "What is a Verb?", "body": "A verb shows action. Examples: Run, Jump, Play, Eat."},
            {"id": "KOBJ_C1_ENG_5_03", "type": "quiz", "question": "Which of these is a verb?", "options": ["Tree", "Dog", "Run"], "correct_index": 2, "explanation": "Run is an action you can do!"}
        ]
    }
    
    chapters = [ch1, ch2, ch3, ch4, ch5]
    
    for i, ch in enumerate(chapters):
        filepath = f"app_core/chapters/class1_english_ch{i+1}.json"
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(ch, f, indent=2, ensure_ascii=False)
            
    print("Successfully upgraded Class 1 English!")

if __name__ == "__main__":
    upgrade_class1_english()
