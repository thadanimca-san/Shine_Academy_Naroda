import json
import os
import glob

def load_json(filepath):
    if not os.path.exists(filepath): return None
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def upgrade_alphabets(pattern, start_id, subject_title):
    files = glob.glob(f"app_core/chapters/{pattern}")
    count = 0
    for filepath in files:
        data = load_json(filepath)
        if not data: continue
        title = data["metadata"].get("title", "")
        # Assuming title is like "Letter A"
        letter = title.split()[-1] if title else "A"
        if len(letter) > 1: letter = letter[0]
        
        blocks = [
            {
                "id": f"KOBJ_{start_id}_{count}_01",
                "type": "trace_alphabet",
                "letter": letter
            },
            {
                "id": f"KOBJ_{start_id}_{count}_02",
                "type": "flashcard",
                "front": f"What starts with {letter}?",
                "back": f"Apple! (Or another word for {letter})",
                "color": "0xFFE91E63"
            }
        ]
        data["blocks"] = blocks
        save_json(filepath, data)
        count += 1
    return count

def upgrade_rhymes(pattern, start_id):
    files = glob.glob(f"app_core/chapters/{pattern}")
    count = 0
    for filepath in files:
        data = load_json(filepath)
        if not data: continue
        title = data["metadata"].get("title", "Rhyme")
        
        blocks = [
            {
                "id": f"KOBJ_{start_id}_{count}_01",
                "type": "nursery_rhyme",
                "title": title,
                "lyrics": f"{title}, {title}, sing along!\nThis is a beautiful song.",
                "media_url": ""
            }
        ]
        data["blocks"] = blocks
        save_json(filepath, data)
        count += 1
    return count

def upgrade_flashcards(pattern, start_id, prompt):
    files = glob.glob(f"app_core/chapters/{pattern}")
    count = 0
    for filepath in files:
        data = load_json(filepath)
        if not data: continue
        title = data["metadata"].get("title", "Word")
        word = title.split()[-1] if title else "Word"
        
        blocks = [
            {
                "id": f"KOBJ_{start_id}_{count}_01",
                "type": "hook",
                "title": "Let's learn a word!",
                "body": f"Tap the card to learn about {word}!"
            },
            {
                "id": f"KOBJ_{start_id}_{count}_02",
                "type": "flashcard",
                "front": word,
                "back": f"{prompt} {word}!",
                "color": "0xFF2196F3"
            }
        ]
        data["blocks"] = blocks
        save_json(filepath, data)
        count += 1
    return count

def upgrade_numbers(pattern, start_id):
    files = glob.glob(f"app_core/chapters/{pattern}")
    count = 0
    for filepath in files:
        data = load_json(filepath)
        if not data: continue
        title = data["metadata"].get("title", "Number")
        num_str = ''.join(filter(str.isdigit, title))
        num = int(num_str) if num_str.isdigit() else 1
        
        emojis = ["🍎", "🎈", "⭐️", "🚗", "🌸", "🦋", "🐟", "🐶", "🍓", "⚽️"]
        emoji = emojis[num % len(emojis)]
        
        blocks = [
            {
                "id": f"KOBJ_{start_id}_{count}_01",
                "type": "counting_game",
                "target_number": num,
                "item_emoji": emoji
            },
            {
                "id": f"KOBJ_{start_id}_{count}_02",
                "type": "trace_alphabet",
                "letter": str(num)
            }
        ]
        data["blocks"] = blocks
        save_json(filepath, data)
        count += 1
    return count

def upgrade_ukg_art():
    files = glob.glob(f"app_core/chapters/ukg_art_*.json")
    shapes = ["tree", "house", "rainbow", "ball", "cat"]
    count = 0
    for filepath in files:
        data = load_json(filepath)
        if not data: continue
        
        shape_name = shapes[count % len(shapes)]
        blocks = [
            {
                "id": f"KOBJ_UKG_ART_{count}_01",
                "type": "color_canvas",
                "shape": shape_name
            }
        ]
        data["blocks"] = blocks
        save_json(filepath, data)
        count += 1
    return count

def main():
    print("Upgrading Nursery...")
    c = upgrade_alphabets("nursery_alphabets_*.json", "NUR_ALPH", "Alphabets")
    print(f" - Nursery Alphabets: {c}")
    c = upgrade_flashcards("nursery_action_words_*.json", "NUR_ACT", "I can")
    print(f" - Nursery Action Words: {c}")
    c = upgrade_flashcards("nursery_phonics_vocab_*.json", "NUR_VOCAB", "Let's say")
    print(f" - Nursery Vocab: {c}")
    
    print("Upgrading LKG...")
    c = upgrade_alphabets("lkg_alphabets_*.json", "LKG_ALPH", "Alphabets")
    print(f" - LKG Alphabets: {c}")
    c = upgrade_alphabets("lkg_vowels_*.json", "LKG_VOW", "Vowels")
    print(f" - LKG Vowels: {c}")
    c = upgrade_numbers("lkg_numbers_*.json", "LKG_NUM")
    print(f" - LKG Numbers: {c}")
    
    print("Upgrading UKG...")
    c = upgrade_ukg_art()
    print(f" - UKG Art: {c}")
    c = upgrade_numbers("ukg_numbers_*.json", "UKG_NUM")
    print(f" - UKG Numbers: {c}")
    c = upgrade_rhymes("ukg_rhymes_*.json", "UKG_RHYMES")
    print(f" - UKG Rhymes: {c}")
    c = upgrade_flashcards("ukg_sight_words_*.json", "UKG_SIGHT", "Read:")
    print(f" - UKG Sight Words: {c}")
    c = upgrade_flashcards("ukg_grammar_*.json", "UKG_GRAMMAR", "Grammar rule:")
    print(f" - UKG Grammar: {c}")

if __name__ == "__main__":
    main()
