import json
import os

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def generate_class3_maths():
    topics = [
        "Where to Look From", "Fun with Numbers", "Give and Take", "Long and Short",
        "Shapes and Designs", "Fun with Give and Take", "Time Goes On", "Who is Heavier?",
        "How Many Times?", "Play with Patterns", "Jugs and Mugs", "Can We Share?",
        "Smart Charts!", "Rupees and Paise"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"class3_maths_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "Mathematics", "difficulty": "Intermediate", "estimated_minutes": 25},
            "blocks": [
                {"id": f"KOBJ_C3_MAT_{i+1}_01", "type": "hook", "title": "Maths is Fun!", "body": f"Welcome to the chapter: {title}."},
                {"id": f"KOBJ_C3_MAT_{i+1}_02", "type": "theory", "title": title, "body": "In this chapter, we will solve interesting puzzles and problems."},
                {"id": f"KOBJ_C3_MAT_{i+1}_03", "type": "quiz", "question": "Are you ready to use your brain?", "options": ["Yes, I am!", "Let's do it!"], "correct_index": 0, "explanation": "Perfect!"}
            ]
        }
        if i == 0:
            data["blocks"].insert(0, {"id": f"KOBJ_C3_MAT_{i+1}_00", "type": "cross_subject_link", "target_chapter_id": "class2_maths_ch1", "title": "Revision", "description": "Review Class 2 concepts."})
        save_json(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_class3_english():
    topics = [
        "Nouns (Singular, Plural, Gender)", "Pronouns (Personal, Possessive)", 
        "Adjectives (Degrees)", "Verbs (Main and Helping)", "Adverbs", 
        "Prepositions", "Conjunctions", "The Magic Garden (Story)", 
        "The Enormous Turnip (Story)", "A Little Fish Story"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"class3_english_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "English", "difficulty": "Intermediate", "estimated_minutes": 25},
            "blocks": [
                {"id": f"KOBJ_C3_ENG_{i+1}_01", "type": "hook", "title": "Language Arts", "body": f"Let's explore {title}."},
                {"id": f"KOBJ_C3_ENG_{i+1}_02", "type": "theory", "title": title, "body": "Read carefully and try to understand the rules and the story."},
                {"id": f"KOBJ_C3_ENG_{i+1}_03", "type": "quiz", "question": "Let's test your reading skills!", "options": ["Start"], "correct_index": 0, "explanation": "Good luck."}
            ]
        }
        save_json(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_class3_evs():
    topics = [
        "Poonam's Day Out", "The Plant Fairy", "Water O' Water!", "Our First School", 
        "Chhotu's House", "Foods We Eat", "Saying without Speaking", "Flying High", 
        "It's Raining", "What is Cooking", "From Here to There", "Work We Do", 
        "Sharing Our Feelings", "The Story of Food", "Making Pots", "Games We Play", 
        "Here comes a Letter", "A House Like This", "Our Friends - Animals", "Drop by Drop", 
        "Families can be Different", "Left-Right", "A Beautiful Cloth", "Web of Life"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"class3_evs_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "EVS", "difficulty": "Intermediate", "estimated_minutes": 25},
            "blocks": [
                {"id": f"KOBJ_C3_EVS_{i+1}_01", "type": "hook", "title": "Environmental Studies", "body": f"Today we learn about '{title}'."},
                {"id": f"KOBJ_C3_EVS_{i+1}_02", "type": "theory", "title": title, "body": "Observe your surroundings. Nature teaches us many things."},
                {"id": f"KOBJ_C3_EVS_{i+1}_03", "type": "quiz", "question": "Did you observe carefully?", "options": ["Yes"], "correct_index": 0, "explanation": "Observation is key to science!"}
            ]
        }
        save_json(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_class3_hindi():
    topics = [
        "कक्कू (कविता)", "शेखीबाज़ मक्खी", "चाँद वाली अम्मा", "मन करता है", 
        "बहादुर बित्तो", "संज्ञा (Noun)", "लिंग और वचन", 
        "सर्वनाम (Pronoun)", "विशेषण (Adjective)", "क्रिया (Verb)"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"class3_hindi_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "Hindi", "difficulty": "Intermediate", "estimated_minutes": 25},
            "blocks": [
                {"id": f"KOBJ_C3_HIN_{i+1}_01", "type": "hook", "title": "हिंदी पाठ", "body": f"आज हम पढ़ेंगे: {title}"},
                {"id": f"KOBJ_C3_HIN_{i+1}_02", "type": "theory", "title": title, "body": "इस पाठ को ध्यान से पढ़ें।"},
                {"id": f"KOBJ_C3_HIN_{i+1}_03", "type": "quiz", "question": "क्या आपने पाठ पढ़ लिया?", "options": ["हाँ"], "correct_index": 0, "explanation": "शाबाश!"}
            ]
        }
        save_json(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def update_class3_curriculum():
    filepath = "app_core/curriculum/class3.json"
    data = load_json(filepath)
    
    maths_ch = generate_class3_maths()
    eng_ch = generate_class3_english()
    evs_ch = generate_class3_evs()
    hindi_ch = generate_class3_hindi()
    
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
    print(f"Updated {filepath} and generated all Class 3 chapters.")

if __name__ == "__main__":
    print("Generating Class 3 chapters...")
    update_class3_curriculum()
    print("Done!")
