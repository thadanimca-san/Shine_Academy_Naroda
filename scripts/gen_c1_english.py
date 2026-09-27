import json

def load_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return None

def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def upgrade_class1_english():
    print("Generating Gold Standard Class 1 English...")
    
    # 1. Alphabet Review
    ch1 = load_json("app_core/chapters/class1_english_ch1.json")
    if ch1:
        ch1["blocks"] = [
            {"id": "KOBJ_C1_ENG_1_01", "type": "hook", "title": "The Magic of Letters", "body": "Did you know that just 26 letters can make every word in the world? Let's review them!"},
            {"id": "KOBJ_C1_ENG_1_02", "type": "quiz", "question": "What is the first letter of the alphabet?", "options": ["Z", "A", "M"], "correct_index": 1, "explanation": "A is the first letter!"},
            {"id": "KOBJ_C1_ENG_1_03", "type": "trace_alphabet", "letter": "A"},
            {"id": "KOBJ_C1_ENG_1_04", "type": "theory", "title": "Uppercase and Lowercase", "body": "Every letter has a BIG (Uppercase) version and a small (Lowercase) version. A and a. B and b."},
            {"id": "KOBJ_C1_ENG_1_05", "type": "quiz", "question": "Which one is an UPPERCASE letter?", "options": ["g", "R", "t"], "correct_index": 1, "explanation": "'R' is big!"},
            {"id": "KOBJ_C1_ENG_1_06", "type": "teacher_tip", "title": "Starting Sentences", "body": "We always use a BIG letter to start a sentence!"},
            {"id": "KOBJ_C1_ENG_1_07", "type": "trace_alphabet", "letter": "Z"},
            {"id": "KOBJ_C1_ENG_1_08", "type": "quiz", "question": "What is the last letter of the alphabet?", "options": ["Z", "X", "Y"], "correct_index": 0, "explanation": "Z is the 26th and last letter!"}
        ]
        save_json("app_core/chapters/class1_english_ch1.json", ch1)

    # 2. Vowels and Consonants
    ch2 = load_json("app_core/chapters/class1_english_ch2.json")
    if ch2:
        ch2["blocks"] = [
            {"id": "KOBJ_C1_ENG_2_01", "type": "hook", "title": "The 5 Super Letters", "body": "There are 5 letters that are so important, you can't make most words without them!"},
            {"id": "KOBJ_C1_ENG_2_02", "type": "quiz", "question": "Are 'A, E, I, O, U' vowels or consonants?", "options": ["Vowels", "Consonants"], "correct_index": 0, "explanation": "They are the 5 vowels!"},
            {"id": "KOBJ_C1_ENG_2_03", "type": "flashcard", "front": "The Vowels", "back": "A, E, I, O, U", "color": "0xFFFF9800"},
            {"id": "KOBJ_C1_ENG_2_04", "type": "theory", "title": "Consonants", "body": "All the other 21 letters are called Consonants! B, C, D, F, G..."},
            {"id": "KOBJ_C1_ENG_2_05", "type": "quiz", "question": "Is 'C' a vowel?", "options": ["Yes", "No"], "correct_index": 1, "explanation": "No, C is a consonant."},
            {"id": "KOBJ_C1_ENG_2_06", "type": "teacher_tip", "title": "Why are vowels special?", "body": "Vowels make the main sound in a syllable. Try to find a word without A, E, I, O, or U! (Hint: 'Fly' uses Y as a vowel)."},
            {"id": "KOBJ_C1_ENG_2_07", "type": "flashcard", "front": "Word: CAT", "back": "Vowel: A, Consonants: C, T", "color": "0xFF2196F3"},
            {"id": "KOBJ_C1_ENG_2_08", "type": "quiz", "question": "How many vowels are in the word 'DOG'?", "options": ["1", "2", "3"], "correct_index": 0, "explanation": "Only 'O' is a vowel!"}
        ]
        save_json("app_core/chapters/class1_english_ch2.json", ch2)

    # 3. Sight Words
    ch3 = load_json("app_core/chapters/class1_english_ch3.json")
    if ch3:
        ch3["blocks"] = [
            {"id": "KOBJ_C1_ENG_3_01", "type": "hook", "title": "Magic Words", "body": "Some words don't follow normal spelling rules. You just have to know them by sight!"},
            {"id": "KOBJ_C1_ENG_3_02", "type": "quiz", "question": "Which of these is a very common word?", "options": ["Zebra", "The", "Helicopter"], "correct_index": 1, "explanation": "'The' is used all the time!"},
            {"id": "KOBJ_C1_ENG_3_03", "type": "flashcard", "front": "T-H-E", "back": "The", "color": "0xFFE91E63"},
            {"id": "KOBJ_C1_ENG_3_04", "type": "theory", "title": "Why learn sight words?", "body": "If you memorize words like 'The', 'And', 'Is', and 'You', reading becomes much faster!"},
            {"id": "KOBJ_C1_ENG_3_05", "type": "quiz", "question": "Fill in the blank: ___ are my friend.", "options": ["You", "The", "And"], "correct_index": 0, "explanation": "You are my friend!"},
            {"id": "KOBJ_C1_ENG_3_06", "type": "flashcard", "front": "Y-O-U", "back": "You", "color": "0xFF00BCD4"},
            {"id": "KOBJ_C1_ENG_3_07", "type": "flashcard", "front": "A-N-D", "back": "And", "color": "0xFF4CAF50"},
            {"id": "KOBJ_C1_ENG_3_08", "type": "quiz", "question": "Find the sight word: 'I like apples _ bananas.'", "options": ["The", "And", "Is"], "correct_index": 1, "explanation": "Apples AND bananas!"}
        ]
        save_json("app_core/chapters/class1_english_ch3.json", ch3)

    # 4. Nouns (Naming Words)
    ch4 = load_json("app_core/chapters/class1_english_ch4.json")
    if ch4:
        ch4["blocks"] = [
            {"id": "KOBJ_C1_ENG_4_01", "type": "hook", "title": "Everything Has a Name", "body": "Look around you. A chair, a dog, a teacher. They all have names!"},
            {"id": "KOBJ_C1_ENG_4_02", "type": "quiz", "question": "What do we call a naming word?", "options": ["Verb", "Noun", "Vowel"], "correct_index": 1, "explanation": "A noun is a naming word!"},
            {"id": "KOBJ_C1_ENG_4_03", "type": "flashcard", "front": "Noun", "back": "A person, place, animal, or thing.", "color": "0xFF9C27B0"},
            {"id": "KOBJ_C1_ENG_4_04", "type": "theory", "title": "Types of Nouns", "body": "Person: Boy, Girl, Doctor.\nPlace: Park, School, City.\nAnimal: Cat, Elephant, Bird.\nThing: Car, Book, Apple."},
            {"id": "KOBJ_C1_ENG_4_05", "type": "quiz", "question": "Which of these is a Place?", "options": ["School", "Pencil", "Dog"], "correct_index": 0, "explanation": "School is a place you go to!"},
            {"id": "KOBJ_C1_ENG_4_06", "type": "teacher_tip", "title": "Noun Test", "body": "Can you touch it? Can you go there? Is it alive? Then it's probably a noun!"},
            {"id": "KOBJ_C1_ENG_4_07", "type": "theory", "title": "Proper Nouns", "body": "Special names are Proper Nouns and start with a BIG letter! Like 'India', 'Rohan', or 'Sunday'."},
            {"id": "KOBJ_C1_ENG_4_08", "type": "quiz", "question": "Find the noun in this sentence: 'The cat is sleeping.'", "options": ["The", "cat", "sleeping"], "correct_index": 1, "explanation": "'Cat' is an animal, so it is a noun!"}
        ]
        save_json("app_core/chapters/class1_english_ch4.json", ch4)

    # 5. Verbs (Action Words)
    ch5 = load_json("app_core/chapters/class1_english_ch5.json")
    if ch5:
        ch5["blocks"] = [
            {"id": "KOBJ_C1_ENG_5_01", "type": "hook", "title": "Lights, Camera, Action!", "body": "What are you doing right now? Sitting? Reading? Those are actions!"},
            {"id": "KOBJ_C1_ENG_5_02", "type": "quiz", "question": "What do we call an action word?", "options": ["Noun", "Verb", "Consonant"], "correct_index": 1, "explanation": "A verb is an action word!"},
            {"id": "KOBJ_C1_ENG_5_03", "type": "flashcard", "front": "Verb", "back": "An action you can do (Run, Jump, Eat).", "color": "0xFFFF5722"},
            {"id": "KOBJ_C1_ENG_5_04", "type": "theory", "title": "Examples of Verbs", "body": "I **run** in the park.\nShe **reads** a book.\nThe dog **barks**."},
            {"id": "KOBJ_C1_ENG_5_05", "type": "quiz", "question": "Which of these is a verb?", "options": ["Tree", "Blue", "Jump"], "correct_index": 2, "explanation": "You can jump! It's an action."},
            {"id": "KOBJ_C1_ENG_5_06", "type": "teacher_tip", "title": "The Action Test", "body": "To check if a word is a verb, ask: 'Can I do it?' Can you 'Tree'? No. Can you 'Run'? Yes!"},
            {"id": "KOBJ_C1_ENG_5_07", "type": "theory", "title": "Verbs in sentences", "body": "Every complete sentence must have a verb!"},
            {"id": "KOBJ_C1_ENG_5_08", "type": "quiz", "question": "Find the verb: 'Ravi drinks milk.'", "options": ["Ravi", "drinks", "milk"], "correct_index": 1, "explanation": "'Drinks' is the action Ravi is doing!"}
        ]
        save_json("app_core/chapters/class1_english_ch5.json", ch5)

    # 6. Pronouns
    ch6 = load_json("app_core/chapters/class1_english_ch6.json")
    if ch6:
        ch6["blocks"] = [
            {"id": "KOBJ_C1_ENG_6_01", "type": "hook", "title": "Who is Who?", "body": "Saying 'Rahul' again and again is boring. 'Rahul has a dog. Rahul likes the dog.' Let's fix this!"},
            {"id": "KOBJ_C1_ENG_6_02", "type": "quiz", "question": "What word can replace a boy's name?", "options": ["She", "He", "It"], "correct_index": 1, "explanation": "We use 'He' for boys!"},
            {"id": "KOBJ_C1_ENG_6_03", "type": "flashcard", "front": "Pronoun", "back": "A word used instead of a Noun (He, She, It, They).", "color": "0xFF009688"},
            {"id": "KOBJ_C1_ENG_6_04", "type": "theory", "title": "Using Pronouns", "body": "Boy/Man -> He\nGirl/Woman -> She\nAnimal/Thing -> It\nMany people -> They"},
            {"id": "KOBJ_C1_ENG_6_05", "type": "quiz", "question": "Which pronoun replaces 'My mother'?", "options": ["He", "It", "She"], "correct_index": 2, "explanation": "Mother is a woman, so we use 'She'."},
            {"id": "KOBJ_C1_ENG_6_06", "type": "teacher_tip", "title": "Better Sentences", "body": "Instead of 'Rahul has a dog. Rahul likes the dog.' we say 'Rahul has a dog. He likes it.' Much better!"},
            {"id": "KOBJ_C1_ENG_6_07", "type": "flashcard", "front": "Rahul and Priya", "back": "They", "color": "0xFF607D8B"},
            {"id": "KOBJ_C1_ENG_6_08", "type": "quiz", "question": "Find the pronoun: 'It is a big car.'", "options": ["It", "big", "car"], "correct_index": 0, "explanation": "'It' is a pronoun used for the car."}
        ]
        save_json("app_core/chapters/class1_english_ch6.json", ch6)

    # 7. Adjectives
    ch7 = load_json("app_core/chapters/class1_english_ch7.json")
    if ch7:
        ch7["blocks"] = [
            {"id": "KOBJ_C1_ENG_7_01", "type": "hook", "title": "Describing Things", "body": "If you lost your bag, how would you describe it? Is it red? Is it small? These are describing words!"},
            {"id": "KOBJ_C1_ENG_7_02", "type": "quiz", "question": "What do we call a describing word?", "options": ["Verb", "Adjective", "Pronoun"], "correct_index": 1, "explanation": "Adjectives describe things!"},
            {"id": "KOBJ_C1_ENG_7_03", "type": "flashcard", "front": "Adjective", "back": "A word that describes a Noun (Red, Big, Happy).", "color": "0xFFFFC107"},
            {"id": "KOBJ_C1_ENG_7_04", "type": "theory", "title": "Types of Adjectives", "body": "Colors: A **blue** bird.\nSizes: A **huge** elephant.\nFeelings: A **sad** boy."},
            {"id": "KOBJ_C1_ENG_7_05", "type": "quiz", "question": "Which word describes the Sun?", "options": ["Cold", "Hot", "Wet"], "correct_index": 1, "explanation": "The sun is hot!"},
            {"id": "KOBJ_C1_ENG_7_06", "type": "teacher_tip", "title": "Adjective Position", "body": "Adjectives usually come right BEFORE the noun! Like 'sweet apple'."},
            {"id": "KOBJ_C1_ENG_7_07", "type": "flashcard", "front": "Opposite of Big", "back": "Small", "color": "0xFF795548"},
            {"id": "KOBJ_C1_ENG_7_08", "type": "quiz", "question": "Find the adjective: 'The soft pillow.'", "options": ["The", "soft", "pillow"], "correct_index": 1, "explanation": "'Soft' describes how the pillow feels."}
        ]
        save_json("app_core/chapters/class1_english_ch7.json", ch7)

    # 8. Reading Comprehension
    ch8 = load_json("app_core/chapters/class1_english_ch8.json")
    if ch8:
        ch8["blocks"] = [
            {"id": "KOBJ_C1_ENG_8_01", "type": "hook", "title": "Story Time!", "body": "Reading is fun, but understanding what you read is even better. Let's read a short story!"},
            {"id": "KOBJ_C1_ENG_8_02", "type": "quiz", "question": "What is 'Comprehension'?", "options": ["Understanding what you read", "Writing fast", "Talking loud"], "correct_index": 0, "explanation": "It means to understand!"},
            {"id": "KOBJ_C1_ENG_8_03", "type": "theory", "title": "The Story of Max", "body": "Max is a small dog. Max has a red ball. Max loves to run in the park."},
            {"id": "KOBJ_C1_ENG_8_04", "type": "quiz", "question": "Who is Max?", "options": ["A cat", "A dog", "A boy"], "correct_index": 1, "explanation": "The story says 'Max is a small dog'."},
            {"id": "KOBJ_C1_ENG_8_05", "type": "quiz", "question": "What color is Max's ball?", "options": ["Blue", "Red", "Green"], "correct_index": 1, "explanation": "The story says 'Max has a red ball'."},
            {"id": "KOBJ_C1_ENG_8_06", "type": "teacher_tip", "title": "Reading Tip", "body": "If you don't know the answer, read the story again carefully. The answer is always there!"},
            {"id": "KOBJ_C1_ENG_8_07", "type": "theory", "title": "Part 2 of the Story", "body": "One day, Max lost his ball. He was sad. Then, his friend Sam found it!"},
            {"id": "KOBJ_C1_ENG_8_08", "type": "quiz", "question": "Who found the ball?", "options": ["Max", "Sam", "No one"], "correct_index": 1, "explanation": "His friend Sam found it!"}
        ]
        save_json("app_core/chapters/class1_english_ch8.json", ch8)


if __name__ == "__main__":
    upgrade_class1_english()
