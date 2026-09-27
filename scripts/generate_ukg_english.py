import json
import os

OUT_DIR = "app_core/chapters"

def write_json(filename, data):
    path = os.path.join(OUT_DIR, filename)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Generated {filename}")

def generate_phonics():
    vowels = [
        ("The 'a' sound (CVC)", "a", ["cat", "bat", "mat"]),
        ("The 'e' sound (CVC)", "e", ["red", "bed", "pen"]),
        ("The 'i' sound (CVC)", "i", ["pin", "bin", "lip"]),
        ("The 'o' sound (CVC)", "o", ["dog", "log", "pot"]),
        ("The 'u' sound (CVC)", "u", ["sun", "bun", "cup"])
    ]
    
    for i, (title, vowel, words) in enumerate(vowels):
        chapter_id = f"ukg_phonics_ch{i+1}"
        
        blocks = [
            {
                "id": f"KOBJ_UKG_PHON_{vowel.upper()}_01",
                "type": "hook",
                "title": f"The CVC Magic with '{vowel}'",
                "body": f"Let's learn how to read 3-letter words with the '{vowel}' sound!"
            }
        ]
        
        for j, word in enumerate(words):
            blocks.append({
                "id": f"KOBJ_UKG_PHON_{vowel.upper()}_{j+2:02d}",
                "type": "theory",
                "title": f"Read: {word}",
                "body": f"Sound it out: /{word[0]}/ - /{word[1]}/ - /{word[2]}/ = {word}"
            })
            
        blocks.append({
            "id": f"KOBJ_UKG_PHON_{vowel.upper()}_99",
            "type": "quiz",
            "question": f"Which word has the '{vowel}' sound?",
            "options": [words[0], "zoo", "car"],
            "correct_index": 0,
            "explanation": f"Yes, '{words[0]}' has the middle sound '{vowel}'!"
        })
            
        data = {
            "metadata": {
                "id": chapter_id,
                "title": title,
                "subject": "Phonics & Words",
                "difficulty": "Beginner",
                "estimated_minutes": 15
            },
            "blocks": blocks
        }
        write_json(f"{chapter_id}.json", data)

def generate_sight_words():
    chapters = [
        ("Common Sight Words", ["the", "and", "is", "it", "to"]),
        ("Action Words", ["run", "jump", "play", "eat"])
    ]
    
    for i, (title, words) in enumerate(chapters):
        chapter_id = f"ukg_sight_words_ch{i+1}"
        
        blocks = [
            {
                "id": f"KOBJ_UKG_SIGHT_{i+1:02d}_01",
                "type": "hook",
                "title": "Sight Words!",
                "body": "Sight words are words we see very often. We learn them by looking at them!"
            }
        ]
        
        for j, word in enumerate(words):
            blocks.append({
                "id": f"KOBJ_UKG_SIGHT_{i+1:02d}_{j+2:02d}",
                "type": "flashcard",
                "front": word,
                "back": f"Say it out loud: {word}",
                "example": f"I know the word '{word}'!"
            })
            
        blocks.append({
            "id": f"KOBJ_UKG_SIGHT_{i+1:02d}_99",
            "type": "quiz",
            "question": f"Which of these is the word '{words[0]}'?",
            "options": ["cat", words[0], "dog"],
            "correct_index": 1,
            "explanation": f"Great job spotting '{words[0]}'!"
        })
            
        data = {
            "metadata": {
                "id": chapter_id,
                "title": title,
                "subject": "Sight Words",
                "difficulty": "Beginner",
                "estimated_minutes": 10
            },
            "blocks": blocks
        }
        write_json(f"{chapter_id}.json", data)

def generate_grammar():
    grammar_topics = [
        ("A and An", "Article A/An", "Use 'A' before consonants, and 'An' before vowels.", "A cat, An apple"),
        ("This and That", "This/That", "Use 'This' for things near, and 'That' for things far.", "This is my book. That is a tree."),
        ("These and Those", "These/Those", "Use 'These' for plural near, and 'Those' for plural far.", "These are my pencils. Those are birds."),
        ("One and Many", "Plurals", "Add 's' to make one thing into many.", "One cat, Many cats."),
        ("Opposites", "Opposites", "Words with completely different meanings.", "Hot/Cold, Big/Small")
    ]
    
    for i, (title, term, definition, example) in enumerate(grammar_topics):
        chapter_id = f"ukg_grammar_ch{i+1}"
        
        blocks = [
            {
                "id": f"KOBJ_UKG_GRAM_{i+1:02d}_01",
                "type": "hook",
                "title": f"Let's learn about {title}!",
                "body": "English has some cool rules to help us speak clearly!"
            },
            {
                "id": f"KOBJ_UKG_GRAM_{i+1:02d}_02",
                "type": "theory",
                "title": term,
                "body": definition
            },
            {
                "id": f"KOBJ_UKG_GRAM_{i+1:02d}_03",
                "type": "flashcard",
                "front": "Example",
                "back": example,
                "example": "Read it out loud!"
            },
            {
                "id": f"KOBJ_UKG_GRAM_{i+1:02d}_04",
                "type": "quiz",
                "question": "Did you understand the rule?",
                "options": ["Yes!", "I need more practice."],
                "correct_index": 0,
                "explanation": "You are a grammar star!"
            }
        ]
            
        data = {
            "metadata": {
                "id": chapter_id,
                "title": title,
                "subject": "Basic Grammar",
                "difficulty": "Beginner",
                "estimated_minutes": 15
            },
            "blocks": blocks
        }
        write_json(f"{chapter_id}.json", data)

def generate_rhymes():
    rhymes = [
        ("Jingle Bells", "Jingle bells, jingle bells,\nJingle all the way.", "Talk about winter and sleighs."),
        ("Little Miss Muffet", "Little Miss Muffet\nSat on a tuffet.", "Discuss what a tuffet and curds are."),
        ("Head, Shoulders, Knees and Toes", "Head, shoulders, knees and toes,\nKnees and toes.", "Point to your body parts!"),
        ("Hot Cross Buns", "Hot cross buns!\nHot cross buns!\nOne a penny, two a penny.", "Pretend to bake buns!"),
        ("Teddy Bear, Turn Around", "Teddy bear, teddy bear, turn around,\nTeddy bear, teddy bear, touch the ground.", "Do the actions with the song!")
    ]
    
    for i, (title, lyrics, tip) in enumerate(rhymes):
        chapter_id = f"ukg_rhymes_ch{i+1}"
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
                    "id": f"KOBJ_UKG_RHYME_{i+1:02d}_01",
                    "type": "nursery_rhyme",
                    "title": title,
                    "lyrics": lyrics,
                    "media_url": ""
                },
                {
                    "id": f"KOBJ_UKG_RHYME_{i+1:02d}_02",
                    "type": "teacher_tip",
                    "content": tip
                },
                {
                    "id": f"KOBJ_UKG_RHYME_{i+1:02d}_03",
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
    generate_phonics()
    generate_sight_words()
    generate_grammar()
    generate_rhymes()
    print("Successfully generated all UKG English chapters!")
