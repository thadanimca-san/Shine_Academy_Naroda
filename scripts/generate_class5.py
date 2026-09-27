import json
import os

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def check_and_save(data, filepath):
    if os.path.exists(filepath):
        print(f"Skipping {filepath} (Already exists. Preserving original data.)")
        return False
    save_json(data, filepath)
    return True

def generate_class5_maths():
    topics = [
        "The Fish Tale", "Shapes and Angles", "How Many Squares?", "Parts and Wholes",
        "Does it Look the Same?", "Be My Multiple, I'll be Your Factor", "Can You See the Pattern?",
        "Mapping Your Way", "Boxes and Sketches", "Tenths and Hundredths", 
        "Area and its Boundary", "Smart Charts", "Ways to Multiply and Divide", "How Big? How Heavy?"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"class5_maths_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "Mathematics", "difficulty": "Intermediate", "estimated_minutes": 35},
            "blocks": [
                {"id": f"KOBJ_C5_MAT_{i+1}_01", "type": "hook", "title": "Maths Mastery", "body": f"Let's dive into: {title}."},
                {"id": f"KOBJ_C5_MAT_{i+1}_02", "type": "theory", "title": title, "body": "Class 5 Mathematics is full of real-life applications."},
                {"id": f"KOBJ_C5_MAT_{i+1}_03", "type": "quiz", "question": "Are you excited?", "options": ["Absolutely!"], "correct_index": 0, "explanation": "Let's go!"}
            ]
        }
        check_and_save(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_class5_english():
    topics = [
        "Ice-cream Man (Poem)", "Wonderful Waste!", "Teamwork (Poem)", "Flying Together",
        "My Shadow (Poem)", "Robinson Crusoe", "Crying (Poem)", 
        "Grammar: Articles", "Grammar: Prepositions", "Grammar: Active & Passive Voice"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"class5_english_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "English", "difficulty": "Intermediate", "estimated_minutes": 35},
            "blocks": [
                {"id": f"KOBJ_C5_ENG_{i+1}_01", "type": "hook", "title": "Literature & Grammar", "body": f"Welcome to: {title}."},
                {"id": f"KOBJ_C5_ENG_{i+1}_02", "type": "theory", "title": title, "body": "Enjoy the literature and understand the grammar rules clearly."},
                {"id": f"KOBJ_C5_ENG_{i+1}_03", "type": "quiz", "question": "Ready?", "options": ["Yes"], "correct_index": 0, "explanation": "Let's begin."}
            ]
        }
        check_and_save(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_class5_evs():
    topics = [
        "Super Senses", "A Snake Charmer's Story", "From Tasting to Digesting", "Mangoes Round the Year",
        "Seeds and Seeds", "Every Drop Counts", "Experiments with Water", "A Treat for Mosquitoes",
        "Up You Go!", "Walls Tell Stories", "Sunita in Space", "What if it Finishes...?",
        "A Shelter so High!", "When the Earth Shook!", "Blow Hot, Blow Cold", "Who will do this Work?",
        "Across the Wall", "No Place for Us?", "A Seed tells a Farmer's Story", "Whose Forests?",
        "Like Father, Like Daughter"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"class5_evs_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "EVS", "difficulty": "Intermediate", "estimated_minutes": 35},
            "blocks": [
                {"id": f"KOBJ_C5_EVS_{i+1}_01", "type": "hook", "title": "Environmental Studies", "body": f"Topic: {title}."},
                {"id": f"KOBJ_C5_EVS_{i+1}_02", "type": "theory", "title": title, "body": "Class 5 EVS introduces us to deep concepts about our world."},
                {"id": f"KOBJ_C5_EVS_{i+1}_03", "type": "quiz", "question": "Let's test it!", "options": ["Go!"], "correct_index": 0, "explanation": "Perfect!"}
            ]
        }
        check_and_save(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_class5_hindi():
    topics = [
        "राख की रस्सी", "फसलों के त्योहार", "खिलौनेवाला", "नन्हा फनकार", 
        "जहाँ चाह वहाँ राह", "चिट्ठी का सफर", "डाकिए की कहानी", "वे दिन भी क्या दिन थे",
        "एक माँ की बेबसी", "व्याकरण: मुहावरे", "व्याकरण: अनेक शब्दों के लिए एक शब्द"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"class5_hindi_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "Hindi", "difficulty": "Intermediate", "estimated_minutes": 35},
            "blocks": [
                {"id": f"KOBJ_C5_HIN_{i+1}_01", "type": "hook", "title": "हिंदी", "body": f"आज का विषय: {title}"},
                {"id": f"KOBJ_C5_HIN_{i+1}_02", "type": "theory", "title": title, "body": "कहानियों से सीखें और व्याकरण को समझें।"},
                {"id": f"KOBJ_C5_HIN_{i+1}_03", "type": "quiz", "question": "शुरू करें?", "options": ["हाँ"], "correct_index": 0, "explanation": "बहुत अच्छे!"}
            ]
        }
        check_and_save(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def update_class5_curriculum():
    filepath = "app_core/curriculum/class5.json"
    data = load_json(filepath)
    
    maths_ch = generate_class5_maths()
    eng_ch = generate_class5_english()
    evs_ch = generate_class5_evs()
    hindi_ch = generate_class5_hindi()
    
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
    print(f"Updated {filepath} and generated missing Class 5 chapters.")

if __name__ == "__main__":
    print("Generating Class 5 chapters...")
    update_class5_curriculum()
    print("Done! (Existing files were strictly preserved and skipped.)")
