import json
import os

OUT_DIR = "app_core/chapters"

def write_json(filename, data):
    path = os.path.join(OUT_DIR, filename)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Generated {filename}")

def generate_alphabets():
    for i in range(26):
        letter = chr(97 + i)  # 'a' to 'z'
        upper_letter = chr(65 + i)
        chapter_id = f"lkg_alphabets_ch{i+1}"
        title = f"Tracing Letter {letter}"
        
        data = {
            "metadata": {
                "id": chapter_id,
                "title": title,
                "subject": "Lowercase Alphabets",
                "difficulty": "Beginner",
                "estimated_minutes": 10
            },
            "blocks": [
                {
                    "id": f"KOBJ_LKG_ALPH_{upper_letter}_01",
                    "type": "hook",
                    "title": "Meet the lowercase letter!",
                    "body": f"We learned the big '{upper_letter}' in Nursery. Now let's meet the small '{letter}'!"
                },
                {
                    "id": f"KOBJ_LKG_ALPH_{upper_letter}_02",
                    "type": "theory",
                    "title": f"The Sound of {letter}",
                    "body": f"The letter '{letter}' makes the sound /_{letter}_/."
                },
                {
                    "id": f"KOBJ_LKG_ALPH_{upper_letter}_03",
                    "type": "trace_alphabet",
                    "letter": letter
                },
                {
                    "id": f"KOBJ_LKG_ALPH_{upper_letter}_04",
                    "type": "quiz",
                    "question": f"Which of these is the small letter '{letter}'?",
                    "options": [
                        chr(97 + (i+1)%26), 
                        letter, 
                        chr(97 + (i+2)%26)
                    ],
                    "correct_index": 1,
                    "explanation": f"Yes! '{letter}' is the correct lowercase letter."
                }
            ]
        }
        write_json(f"{chapter_id}.json", data)

def generate_vowels():
    chapter_id = "lkg_vowels_ch1"
    title = "Meet the Vowels"
    data = {
        "metadata": {
            "id": chapter_id,
            "title": title,
            "subject": "Vowels & Consonants",
            "difficulty": "Beginner",
            "estimated_minutes": 15
        },
        "blocks": [
            {
                "id": "KOBJ_LKG_VOW_01",
                "type": "hook",
                "title": "The Magic Letters",
                "body": "Did you know that 5 special letters are called VOWELS? They are like magic glue for words!"
            },
            {
                "id": "KOBJ_LKG_VOW_02",
                "type": "flashcard",
                "front": "Vowels",
                "back": "The 5 vowels are A, E, I, O, U.",
                "example": "All other letters are called Consonants."
            },
            {
                "id": "KOBJ_LKG_VOW_03",
                "type": "teacher_tip",
                "content": "Sing the vowels to the tune of 'BINGO' (A-E-I-O-U) to help kids memorize them!"
            },
            {
                "id": "KOBJ_LKG_VOW_04",
                "type": "quiz",
                "question": "Which of these is a VOWEL?",
                "options": ["B", "C", "A"],
                "correct_index": 2,
                "explanation": "A is the first vowel! A, E, I, O, U."
            }
        ]
    }
    write_json(f"{chapter_id}.json", data)

def generate_phonics():
    groups = [
        ("The 'A' Blend (am, an, at, as)", ["am", "an", "at", "as"], "a"),
        ("The 'I' Blend (in, is, it, if)", ["in", "is", "it", "if"], "i"),
        ("The 'O' Blend (on, of, or, ox)", ["on", "of", "or", "ox"], "o"),
        ("The 'U' Blend (up, us)", ["up", "us"], "u")
    ]
    
    for i, (title, words, vowel) in enumerate(groups):
        chapter_id = f"lkg_phonics_ch{i+1}"
        blocks = [
            {
                "id": f"KOBJ_LKG_PHON_{vowel.upper()}_01",
                "type": "hook",
                "title": "Let's blend!",
                "body": f"Let's put the vowel '{vowel}' with another letter to make a word!"
            }
        ]
        
        for j, word in enumerate(words):
            blocks.append({
                "id": f"KOBJ_LKG_PHON_{vowel.upper()}_{j+2:02d}",
                "type": "theory",
                "title": f"Read: {word}",
                "body": f"Sound it out: /{word[0]}/ + /{word[1]}/ = {word}"
            })
            
        blocks.append({
            "id": f"KOBJ_LKG_PHON_{vowel.upper()}_99",
            "type": "quiz",
            "question": f"Which word has the '{vowel}' sound?",
            "options": [words[0], "zoo", "car"],
            "correct_index": 0,
            "explanation": f"Yes, '{words[0]}' starts with '{vowel}'!"
        })
            
        data = {
            "metadata": {
                "id": chapter_id,
                "title": title,
                "subject": "Two-Letter Phonics",
                "difficulty": "Beginner",
                "estimated_minutes": 15
            },
            "blocks": blocks
        }
        write_json(f"{chapter_id}.json", data)

def generate_rhymes():
    rhymes = [
        ("Hickory Dickory Dock", "Hickory dickory dock,\nThe mouse ran up the clock.", "Talk about how clocks tick-tock."),
        ("Rain Rain Go Away", "Rain, rain, go away,\nCome again another day.", "Talk about weather and playing outside."),
        ("Old MacDonald", "Old MacDonald had a farm,\nE-I-E-I-O.", "Practice animal sounds! Oink, moo, baa!"),
        ("If You're Happy", "If you're happy and you know it,\nClap your hands!", "Encourage kids to clap their hands."),
        ("Five Little Monkeys", "Five little monkeys jumping on the bed,\nOne fell off and bumped his head.", "Count down from five on your fingers."),
        ("London Bridge", "London Bridge is falling down,\nFalling down, falling down.", "Play the London Bridge falling game."),
        ("Mulberry Bush", "Here we go round the mulberry bush,\nThe mulberry bush, the mulberry bush.", "Hold hands and walk in a circle."),
        ("I'm a Little Teapot", "I'm a little teapot, short and stout,\nHere is my handle, here is my spout.", "Act out being a teapot with your arms."),
        ("Two Little Dicky Birds", "Two little dicky birds sitting on a wall,\nOne named Peter, one named Paul.", "Use your index fingers as the two birds."),
        ("Ding Dong Bell", "Ding dong bell,\nPussy's in the well.", "Discuss the sound of bells ringing.")
    ]
    
    for i, (title, lyrics, tip) in enumerate(rhymes):
        chapter_id = f"lkg_rhymes_ch{i+1}"
        data = {
            "metadata": {
                "id": chapter_id,
                "title": title,
                "subject": "Rhymes & Poems",
                "difficulty": "Beginner",
                "estimated_minutes": 10
            },
            "blocks": [
                {
                    "id": f"KOBJ_LKG_RHYME_{i+1:02d}_01",
                    "type": "nursery_rhyme",
                    "title": title,
                    "lyrics": lyrics,
                    "media_url": ""
                },
                {
                    "id": f"KOBJ_LKG_RHYME_{i+1:02d}_02",
                    "type": "teacher_tip",
                    "content": tip
                },
                {
                    "id": f"KOBJ_LKG_RHYME_{i+1:02d}_03",
                    "type": "quiz",
                    "question": f"Did you enjoy singing '{title}'?",
                    "options": ["Yes!", "I loved it!"],
                    "correct_index": 0,
                    "explanation": "Great job singing!"
                }
            ]
        }
        write_json(f"{chapter_id}.json", data)
if __name__ == "__main__":
    generate_alphabets()
    generate_vowels()
    generate_phonics()
    generate_rhymes()
    print("Successfully generated all LKG English chapters!")
