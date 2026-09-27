import json
import os

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def generate_class2_maths():
    topics = [
        ("Numbers up to 1000", "Let's count beyond 100!"),
        ("Addition (2-digit)", "Adding bigger numbers together."),
        ("Subtraction (2-digit)", "Subtracting bigger numbers."),
        ("Introduction to Multiplication", "Adding the same number again and again!"),
        ("Time and Calendar", "Days, Weeks, Months, and Clocks!"),
        ("Money", "Buying things and getting change!"),
        ("Measurement", "Length, Weight, and Capacity."),
        ("Shapes and Patterns", "2D and 3D shapes!")
    ]
    chapters = []
    for i, (title, hook) in enumerate(topics):
        chapter_id = f"class2_maths_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "Mathematics", "difficulty": "Beginner", "estimated_minutes": 20},
            "blocks": [
                {"id": f"KOBJ_C2_MAT_{i+1}_01", "type": "cross_subject_link", "target_chapter_id": "class1_maths_ch1", "title": "Revision", "description": "Review Class 1 Mathematics concepts before we dive deeper!"},
                {"id": f"KOBJ_C2_MAT_{i+1}_02", "type": "hook", "title": "Math Magic", "body": hook},
                {"id": f"KOBJ_C2_MAT_{i+1}_03", "type": "theory", "title": title, "body": f"Today we will explore {title}. Mathematics is fun!"},
                {"id": f"KOBJ_C2_MAT_{i+1}_04", "type": "quiz", "question": f"Are you ready for {title}?", "options": ["Yes!", "Absolutely!"], "correct_index": 0, "explanation": "Let's begin!"}
            ]
        }
        save_json(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_class2_english():
    topics = [
        ("Sentences", "What makes a complete sentence?"),
        ("Nouns (Common & Proper)", "Special names vs everyday names!"),
        ("Pronouns", "Replacing nouns to sound better!"),
        ("Adjectives", "Words that paint a picture!"),
        ("Verbs & Tenses", "Past, Present, and Future actions!"),
        ("Prepositions", "In, On, Under, Above!"),
        ("Conjunctions", "And, But, Or... the joining words!"),
        ("Reading Fables", "Stories with a moral!")
    ]
    chapters = []
    for i, (title, hook) in enumerate(topics):
        chapter_id = f"class2_english_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "English", "difficulty": "Beginner", "estimated_minutes": 20},
            "blocks": [
                {"id": f"KOBJ_C2_ENG_{i+1}_01", "type": "hook", "title": "English Grammar", "body": hook},
                {"id": f"KOBJ_C2_ENG_{i+1}_02", "type": "theory", "title": title, "body": f"Let's master {title}."},
                {"id": f"KOBJ_C2_ENG_{i+1}_03", "type": "quiz", "question": "Let's practice!", "options": ["Start"], "correct_index": 0, "explanation": "Good job."}
            ]
        }
        save_json(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_class2_evs():
    topics = [
        "My Body", "My Family", "Food", "Water", "Shelter", 
        "Clothes", "Air", "Cleanliness and Health", "Safety Rules", "Neighbourhood",
        "Festivals", "Plants Around Us", "Animals Around Us", "Transport", "Communication", 
        "Earth and Sky", "Time and Directions"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"class2_evs_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "EVS", "difficulty": "Beginner", "estimated_minutes": 20},
            "blocks": [
                {"id": f"KOBJ_C2_EVS_{i+1}_01", "type": "hook", "title": "Discovering Our World", "body": f"Let's dive deeper into {title}!"},
                {"id": f"KOBJ_C2_EVS_{i+1}_02", "type": "theory", "title": title, "body": f"Understanding our environment is crucial. Today's focus is {title}."},
                {"id": f"KOBJ_C2_EVS_{i+1}_03", "type": "quiz", "question": f"Is learning about {title} fun?", "options": ["Yes!", "Of course!"], "correct_index": 0, "explanation": "I agree!"}
            ]
        }
        save_json(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_class2_hindi():
    topics = [
        ("Bhasha (Language)", "हम कैसे बात करते हैं?"),
        ("Vyakaran Basics", "व्याकरण क्या है?"),
        ("Sangya (Noun)", "नाम वाले शब्द!"),
        ("Ling (Gender)", "स्त्रीलिंग और पुल्लिंग"),
        ("Vachan (Number)", "एकवचन और बहुवचन"),
        ("Sarvanam (Pronoun)", "संज्ञा के स्थान पर आने वाले शब्द"),
        ("Visheshan (Adjective)", "विशेषता बताने वाले शब्द"),
        ("Kriya (Verb)", "काम वाले शब्द"),
        ("Kahani Padhna", "रोचक कहानियाँ")
    ]
    chapters = []
    for i, (title, hook) in enumerate(topics):
        chapter_id = f"class2_hindi_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "Hindi", "difficulty": "Beginner", "estimated_minutes": 20},
            "blocks": [
                {"id": f"KOBJ_C2_HIN_{i+1}_01", "type": "hook", "title": "हिंदी व्याकरण", "body": hook},
                {"id": f"KOBJ_C2_HIN_{i+1}_02", "type": "theory", "title": title, "body": f"Let's learn {title} in Hindi."},
                {"id": f"KOBJ_C2_HIN_{i+1}_03", "type": "quiz", "question": "क्या आप तैयार हैं?", "options": ["हाँ (Yes)"], "correct_index": 0, "explanation": "बहुत बढ़िया!"}
            ]
        }
        save_json(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def update_class2_curriculum():
    filepath = "app_core/curriculum/class2.json"
    data = load_json(filepath)
    
    maths_ch = generate_class2_maths()
    eng_ch = generate_class2_english()
    evs_ch = generate_class2_evs()
    hindi_ch = generate_class2_hindi()
    
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
    print(f"Updated {filepath} and generated all Class 2 chapters.")

if __name__ == "__main__":
    print("Generating Class 2 chapters...")
    update_class2_curriculum()
    print("Done!")
