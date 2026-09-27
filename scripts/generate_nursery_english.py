import json
import os

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def generate_alphabet_chapters():
    for i in range(26):
        letter = chr(65 + i)
        chapter_id = f"nursery_alphabets_ch{i+1}"
        
        data = {
            "metadata": {
                "id": chapter_id,
                "title": f"Tracing Letter {letter}",
                "subject": "Alphabets",
                "difficulty": "Beginner",
                "estimated_minutes": 15
            },
            "blocks": [
                {
                    "id": f"KOBJ_NUR_ALPH_{letter}_01",
                    "type": "hook",
                    "title": "Meet the Letter!",
                    "body": f"Have you ever wondered what the letter {letter} looks like? Let's find out!"
                },
                {
                    "id": f"KOBJ_NUR_ALPH_{letter}_02",
                    "type": "theory",
                    "title": "Socratic Question",
                    "body": f"Can you look around the room and find something that starts with the letter {letter}?"
                },
                {
                    "id": f"KOBJ_NUR_ALPH_{letter}_03",
                    "type": "trace_alphabet",
                    "letter": letter
                },
                {
                    "id": f"KOBJ_NUR_ALPH_{letter}_04",
                    "type": "reveal",
                    "title": f"{letter} is for...",
                    "body": f"{letter} is for Apple!" if letter == 'A' else f"{letter} is for something special!"
                },
                {
                    "id": f"KOBJ_NUR_ALPH_{letter}_05",
                    "type": "quiz",
                    "question": f"Which letter did we just learn to trace?",
                    "options": [letter, chr(65 + (i+1)%26), chr(65 + (i+2)%26)],
                    "correct_index": 0,
                    "explanation": f"We just learned the letter {letter}!"
                }
            ]
        }
        
        filepath = f"app_core/chapters/{chapter_id}.json"
        save_json(data, filepath)

def generate_rhymes_chapters():
    rhymes = [
        {"title": "Twinkle Twinkle", "content": "Twinkle, twinkle, little star,\nHow I wonder what you are!", "audio": "assets/audio/twinkle_star.mp3"},
        {"title": "Baa Baa Black Sheep", "content": "Baa baa black sheep,\nHave you any wool?", "audio": None},
        {"title": "Humpty Dumpty", "content": "Humpty Dumpty sat on a wall,\nHumpty Dumpty had a great fall.", "audio": None},
        {"title": "Jack and Jill", "content": "Jack and Jill went up the hill\nTo fetch a pail of water.", "audio": None},
        {"title": "Mary Had a Little Lamb", "content": "Mary had a little lamb,\nWhose fleece was white as snow.", "audio": None},
        {"title": "Incy Wincy Spider", "content": "Incy wincy spider climbed up the water spout,\nDown came the rain and washed the spider out.", "audio": None},
        {"title": "Ring-a-Ring o' Roses", "content": "Ring-a-ring o' roses,\nA pocket full of posies.", "audio": None},
        {"title": "Row, Row, Row Your Boat", "content": "Row, row, row your boat,\nGently down the stream.", "audio": None},
        {"title": "Johny Johny Yes Papa", "content": "Johny Johny!\nYes Papa?\nEating sugar?\nNo Papa!", "audio": None},
        {"title": "Wheels on the Bus", "content": "The wheels on the bus go round and round,\nRound and round, round and round.", "audio": None},
    ]

    for i in range(10):
        if i >= len(rhymes):
            break
            
        rhyme = rhymes[i]
        chapter_id = f"nursery_rhymes_ch{i+1}"
        data = {
            "metadata": {
                "id": chapter_id,
                "title": rhyme["title"],
                "subject": "Rhymes",
                "difficulty": "Beginner",
                "estimated_minutes": 10
            },
            "blocks": [
                {
                    "id": f"KOBJ_NUR_RHYME_{i+1}_01",
                    "type": "hook",
                    "title": "Let's Sing!",
                    "body": f"Are you ready to sing {rhyme['title']}? It is one of the most fun songs!"
                },
                {
                    "id": f"KOBJ_NUR_RHYME_{i+1}_02",
                    "type": "nursery_rhyme",
                    "title": rhyme["title"],
                    "content": rhyme["content"]
                },
                {
                    "id": f"KOBJ_NUR_RHYME_{i+1}_03",
                    "type": "teacher_tip",
                    "title": "For Parents & Teachers",
                    "content": "Encourage the child to do the hand actions while singing this rhyme to build motor skills."
                }
            ]
        }
        
        if rhyme["audio"]:
            data["blocks"][1]["audio_url"] = rhyme["audio"]
            
        filepath = f"app_core/chapters/{chapter_id}.json"
        save_json(data, filepath)

def generate_phonics_vocab():
    chapters = [
        ("Vowels & Consonants", "The Two Letter Families", "Did you know letters have two families? The Singers and the Quiet ones!", "Vowels are A, E, I, O, U. They sing loudly! The others are consonants.", ["A, E, I, O, U", "B, C, D", "X, Y, Z"], 0),
        ("Fruits", "Sweet & Healthy", "What is sweet, juicy, and very healthy to eat? Fruits!", "Apple is red, Banana is yellow, and Mango is the king of fruits!", ["Mango", "Potato", "Carrot"], 0),
        ("Vegetables", "Strong & Green", "Want to become super strong? Let's eat vegetables!", "Carrots make your eyes sharp, and spinach makes your muscles strong.", ["Chocolate", "Carrot", "Candy"], 1),
        ("Domestic Animals", "Our Pet Friends", "Who says 'Meow' and who says 'Woof'?", "Dogs protect our house, and cows give us milk. They are domestic animals.", ["Lion", "Tiger", "Cow"], 2),
        ("Wild Animals", "Kings of the Jungle", "Who is the biggest animal in the forest?", "Lions roar and Elephants have long trunks. They live in the wild jungle.", ["Dog", "Cat", "Lion"], 2),
        ("Vehicles", "Vroom Vroom", "How do we travel very fast from one place to another?", "Cars run on roads, trains run on tracks, and airplanes fly in the sky!", ["Car", "Tree", "House"], 0),
    ]

    for i, (title, hook_title, hook_body, reveal, options, correct) in enumerate(chapters):
        chapter_id = f"nursery_phonics_vocab_ch{i+1}"
        data = {
            "metadata": {
                "id": chapter_id,
                "title": title,
                "subject": "Vocabulary & Phonics",
                "difficulty": "Beginner",
                "estimated_minutes": 15
            },
            "blocks": [
                {
                    "id": f"KOBJ_NUR_VOCAB_{i+1}_01",
                    "type": "hook",
                    "title": hook_title,
                    "body": hook_body
                },
                {
                    "id": f"KOBJ_NUR_VOCAB_{i+1}_02",
                    "type": "theory",
                    "title": "Let's Discover!",
                    "body": reveal
                },
                {
                    "id": f"KOBJ_NUR_VOCAB_{i+1}_03",
                    "type": "flashcard",
                    "front": title,
                    "back": reveal
                },
                {
                    "id": f"KOBJ_NUR_VOCAB_{i+1}_04",
                    "type": "quiz",
                    "question": f"Which of these belongs to {title}?",
                    "options": options,
                    "correct_index": correct,
                    "explanation": "Great job! You remembered perfectly."
                }
            ]
        }
        save_json(data, f"app_core/chapters/{chapter_id}.json")

def generate_action_words():
    chapters = [
        ("Daily Actions", "Things We Do", "What are you doing right now? You are learning! Learning is an action.", "Walking, jumping, eating, and sleeping are all actions we do every day.", ["Jumping", "Apple", "Red"], 0),
        ("Morning Routine", "Wake Up!", "What is the first thing you do when the sun comes up?", "We wake up, brush our teeth, and wash our face. These are morning actions.", ["Sleep", "Brush", "Moon"], 1),
        ("Opposites", "Up and Down", "If you look up, you see the sky. If you look down, you see the ground!", "Up and Down, Big and Small, Hot and Cold are called Opposites.", ["Big and Small", "Red and Blue", "Cat and Dog"], 0)
    ]
    
    for i, (title, hook_title, hook_body, reveal, options, correct) in enumerate(chapters):
        chapter_id = f"nursery_action_words_ch{i+1}"
        data = {
            "metadata": {
                "id": chapter_id,
                "title": title,
                "subject": "Action Words",
                "difficulty": "Beginner",
                "estimated_minutes": 15
            },
            "blocks": [
                {
                    "id": f"KOBJ_NUR_ACTION_{i+1}_01",
                    "type": "hook",
                    "title": hook_title,
                    "body": hook_body
                },
                {
                    "id": f"KOBJ_NUR_ACTION_{i+1}_02",
                    "type": "theory",
                    "title": "Let's Learn Action Words!",
                    "body": reveal
                },
                {
                    "id": f"KOBJ_NUR_ACTION_{i+1}_03",
                    "type": "flashcard",
                    "front": title,
                    "back": reveal
                },
                {
                    "id": f"KOBJ_NUR_ACTION_{i+1}_04",
                    "type": "quiz",
                    "question": f"Which of these is an example of {title}?",
                    "options": options,
                    "correct_index": correct,
                    "explanation": "Perfect!"
                }
            ]
        }
        save_json(data, f"app_core/chapters/{chapter_id}.json")

def generate_colors_shapes():
    chapters = [
        ("Primary Colors", "The Magic Three", "Did you know that you can paint the whole world with just 3 colors?", "Red, Blue, and Yellow are Primary colors. The sun is yellow, the sky is blue, and apples are red.", ["Red, Blue, Yellow", "Pink, Purple, Green", "Black, White, Gray"], 0),
        ("Secondary Colors", "Mixing Magic", "What happens if we mix Red and Yellow together?", "If we mix Red and Yellow, we get Orange! Mixing Primary colors gives us Secondary colors like Green, Orange, and Purple.", ["Green", "Blue", "Red"], 0),
        ("Basic Shapes", "Shapes Everywhere", "Look at your room's door. What shape is it?", "A door is a Rectangle. A ball is a Circle. A pizza slice is a Triangle.", ["Circle", "Water", "Sky"], 0)
    ]
    
    for i, (title, hook_title, hook_body, reveal, options, correct) in enumerate(chapters):
        chapter_id = f"nursery_colors_shapes_ch{i+1}"
        data = {
            "metadata": {
                "id": chapter_id,
                "title": title,
                "subject": "Colors & Shapes",
                "difficulty": "Beginner",
                "estimated_minutes": 15
            },
            "blocks": [
                {
                    "id": f"KOBJ_NUR_COLOR_{i+1}_01",
                    "type": "hook",
                    "title": hook_title,
                    "body": hook_body
                },
                {
                    "id": f"KOBJ_NUR_COLOR_{i+1}_02",
                    "type": "theory",
                    "title": "Let's Discover!",
                    "body": reveal
                },
                {
                    "id": f"KOBJ_NUR_COLOR_{i+1}_03",
                    "type": "flashcard",
                    "front": title,
                    "back": reveal
                },
                {
                    "id": f"KOBJ_NUR_COLOR_{i+1}_04",
                    "type": "quiz",
                    "question": f"Which of these is an example for {title}?",
                    "options": options,
                    "correct_index": correct,
                    "explanation": "Well done! You got it right."
                }
            ]
        }
        save_json(data, f"app_core/chapters/{chapter_id}.json")


def update_curriculum():
    filepath = "app_core/curriculum/nursery.json"
    data = load_json(filepath)
    
    existing_subject_ids = [s['id'] for s in data['subjects']]
    
    new_subjects = [
        {
            "id": "phonics_vocab",
            "name": "Vocabulary & Phonics",
            "color_hex": "0xFF4CAF50",
            "icon": "translate",
            "chapters": [
                {"chapter_number": 1, "title": "Vowels & Consonants", "module_id": "nursery_phonics_vocab_ch1", "is_available": True, "status": "Available"},
                {"chapter_number": 2, "title": "Fruits", "module_id": "nursery_phonics_vocab_ch2", "is_available": True, "status": "Available"},
                {"chapter_number": 3, "title": "Vegetables", "module_id": "nursery_phonics_vocab_ch3", "is_available": True, "status": "Available"},
                {"chapter_number": 4, "title": "Domestic Animals", "module_id": "nursery_phonics_vocab_ch4", "is_available": True, "status": "Available"},
                {"chapter_number": 5, "title": "Wild Animals", "module_id": "nursery_phonics_vocab_ch5", "is_available": True, "status": "Available"},
                {"chapter_number": 6, "title": "Vehicles", "module_id": "nursery_phonics_vocab_ch6", "is_available": True, "status": "Available"}
            ]
        },
        {
            "id": "action_words",
            "name": "Action Words",
            "color_hex": "0xFF00BCD4",
            "icon": "directions_run",
            "chapters": [
                {"chapter_number": 1, "title": "Daily Actions", "module_id": "nursery_action_words_ch1", "is_available": True, "status": "Available"},
                {"chapter_number": 2, "title": "Morning Routine", "module_id": "nursery_action_words_ch2", "is_available": True, "status": "Available"},
                {"chapter_number": 3, "title": "Opposites", "module_id": "nursery_action_words_ch3", "is_available": True, "status": "Available"}
            ]
        },
        {
            "id": "colors_shapes",
            "name": "Colors & Shapes",
            "color_hex": "0xFFE91E63",
            "icon": "palette",
            "chapters": [
                {"chapter_number": 1, "title": "Primary Colors", "module_id": "nursery_colors_shapes_ch1", "is_available": True, "status": "Available"},
                {"chapter_number": 2, "title": "Secondary Colors", "module_id": "nursery_colors_shapes_ch2", "is_available": True, "status": "Available"},
                {"chapter_number": 3, "title": "Basic Shapes", "module_id": "nursery_colors_shapes_ch3", "is_available": True, "status": "Available"}
            ]
        }
    ]
    
    for subj in new_subjects:
        if subj['id'] not in existing_subject_ids:
            data['subjects'].append(subj)
            
    # Also fix Rhyme ch1 which had data_file instead of module_id
    for subj in data['subjects']:
        if subj['id'] == 'rhymes':
            if 'data_file' in subj['chapters'][0]:
                del subj['chapters'][0]['data_file']
                subj['chapters'][0]['module_id'] = 'nursery_rhymes_ch1'
                subj['chapters'][0]['is_available'] = True
                
    save_json(data, filepath)
    print(f"Updated {filepath}")
    
    generate_phonics_vocab()
    generate_action_words()
    generate_colors_shapes()
    print("Generated all extra Nursery chapters!")

if __name__ == "__main__":
    print("Generating Alphabet chapters...")
    generate_alphabet_chapters()
    
    print("Generating Rhymes chapters...")
    generate_rhymes_chapters()
    
    print("Updating curriculum & generating new subjects...")
    update_curriculum()
    print("Done!")
