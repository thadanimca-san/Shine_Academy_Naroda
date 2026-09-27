import json
import os

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def generate_class1_maths():
    topics = [
        ("Numbers 1-100", "Let's count all the way to 100!"),
        ("Addition (1-digit)", "Putting things together! 1 + 1 = 2"),
        ("Subtraction (1-digit)", "Taking things away! 2 - 1 = 1"),
        ("Shapes Around Us", "Circles, Squares, Triangles!"),
        ("Time", "Tick tock! Reading a clock."),
        ("Money", "Coins and Notes!"),
        ("Measurement", "Long and Short, Heavy and Light.")
    ]
    
    chapters = []
    for i, (title, hook) in enumerate(topics):
        chapter_id = f"class1_maths_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "Mathematics", "difficulty": "Beginner", "estimated_minutes": 15},
            "blocks": [
                {"id": f"KOBJ_C1_MAT_{i+1}_01", "type": "cross_subject_link", "target_chapter_id": "ukg_numbers_ch1", "title": "Revision", "description": "Review what we learned in UKG!"},
                {"id": f"KOBJ_C1_MAT_{i+1}_02", "type": "hook", "title": "Let's Learn Math!", "body": hook},
                {"id": f"KOBJ_C1_MAT_{i+1}_03", "type": "theory", "title": title, "body": f"Today we will understand {title}. Math is everywhere!"},
                {"id": f"KOBJ_C1_MAT_{i+1}_04", "type": "quiz", "question": f"Are you excited to learn {title}?", "options": ["Yes!", "Very excited!"], "correct_index": 0, "explanation": "Let's begin!"}
            ]
        }
        save_json(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_class1_english():
    topics = [
        ("Alphabet Review", "A to Z!"),
        ("Vowels and Consonants", "A, E, I, O, U!"),
        ("Sight Words", "Words we see all the time."),
        ("Nouns (Naming Words)", "Names of people, places, animals, and things!"),
        ("Verbs (Action Words)", "Jump, Run, Play!"),
        ("Pronouns", "He, She, It, They!"),
        ("Adjectives", "Describing words like big, small, red!"),
        ("Reading Comprehension", "Let's read a short story.")
    ]
    chapters = []
    for i, (title, hook) in enumerate(topics):
        chapter_id = f"class1_english_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "English", "difficulty": "Beginner", "estimated_minutes": 15},
            "blocks": [
                {"id": f"KOBJ_C1_ENG_{i+1}_01", "type": "hook", "title": "English Magic", "body": hook},
                {"id": f"KOBJ_C1_ENG_{i+1}_02", "type": "theory", "title": title, "body": f"Let's master {title} in English grammar."},
                {"id": f"KOBJ_C1_ENG_{i+1}_03", "type": "quiz", "question": "Ready to practice?", "options": ["Yes!"], "correct_index": 0, "explanation": "Great!"}
            ]
        }
        save_json(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_class1_evs():
    topics = [
        "About Me", "My Body", "My Family", "My Home", "My School", 
        "Food We Eat", "Water", "Clothes We Wear", "Air", "Keeping Clean and Healthy",
        "Safety Habits", "People Who Help Us", "Festivals", "Plants", "Animals", 
        "Transport", "The Sky Above Us"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"class1_evs_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "EVS", "difficulty": "Beginner", "estimated_minutes": 15},
            "blocks": [
                {"id": f"KOBJ_C1_EVS_{i+1}_01", "type": "hook", "title": "Our World", "body": f"Let's discover more about {title}!"},
                {"id": f"KOBJ_C1_EVS_{i+1}_02", "type": "theory", "title": title, "body": f"The environment is everything around us. Today we focus on {title}."},
                {"id": f"KOBJ_C1_EVS_{i+1}_03", "type": "quiz", "question": f"Is {title} important?", "options": ["Yes", "No"], "correct_index": 0, "explanation": "It sure is!"}
            ]
        }
        save_json(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_class1_hindi():
    topics = [
        ("Varnamala (Swar)", "अ, आ, इ, ई..."),
        ("Varnamala (Vyanjan)", "क, ख, ग, घ..."),
        ("Bina Matra Wale Shabd", "कल, चल, जल..."),
        ("Aa Ki Matra", "आम, काम, नाम..."),
        ("I & Ee Ki Matra", "दिन, नदी..."),
        ("Fruits & Vegetables", "फल और सब्जियां"),
        ("Animals & Birds", "पशु और पक्षी")
    ]
    chapters = []
    for i, (title, hook) in enumerate(topics):
        chapter_id = f"class1_hindi_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "Hindi", "difficulty": "Beginner", "estimated_minutes": 15},
            "blocks": [
                {"id": f"KOBJ_C1_HIN_{i+1}_01", "type": "hook", "title": "हिंदी", "body": hook},
                {"id": f"KOBJ_C1_HIN_{i+1}_02", "type": "theory", "title": title, "body": f"Let's learn {title} in Hindi."},
                {"id": f"KOBJ_C1_HIN_{i+1}_03", "type": "quiz", "question": "Can you read it?", "options": ["हाँ (Yes)", "नहीं (No)"], "correct_index": 0, "explanation": "बहुत बढ़िया! (Very good!)"}
            ]
        }
        save_json(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def update_class1_curriculum():
    filepath = "app_core/curriculum/class1.json"
    data = load_json(filepath)
    
    maths_ch = generate_class1_maths()
    eng_ch = generate_class1_english()
    evs_ch = generate_class1_evs()
    hindi_ch = generate_class1_hindi()
    
    for subj in data['subjects']:
        if subj['id'] == 'maths':
            subj['chapters'] = maths_ch
        elif subj['id'] == 'english':
            subj['chapters'] = eng_ch
        elif subj['id'] == 'evs':
            subj['chapters'] = evs_ch
        elif subj['id'] == 'hindi':
            subj['chapters'] = hindi_ch
            
    save_json(data, filepath)
    print(f"Updated {filepath} and generated all Class 1 chapters.")

if __name__ == "__main__":
    print("Generating Class 1 chapters...")
    update_class1_curriculum()
    print("Done!")
