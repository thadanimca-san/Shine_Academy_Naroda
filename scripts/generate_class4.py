import json
import os

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def check_and_save(data, filepath):
    # This guarantees we NEVER overwrite existing working content!
    if os.path.exists(filepath):
        print(f"Skipping {filepath} (Already exists. Preserving original data.)")
        return False
    save_json(data, filepath)
    return True

def generate_class4_maths():
    topics = [
        "Building with Bricks", "Long and Short", "A Trip to Bhopal", "Tick-Tick-Tick",
        "The Way The World Looks", "The Junk Seller", "Jugs and Mugs", "Carts and Wheels",
        "Halves and Quarters", "Play with Patterns", "Tables and Shares", 
        "How Heavy? How Light?", "Fields and Fences", "Smart Charts"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"class4_maths_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "Mathematics", "difficulty": "Intermediate", "estimated_minutes": 30},
            "blocks": [
                {"id": f"KOBJ_C4_MAT_{i+1}_01", "type": "hook", "title": "Math Magic!", "body": f"Let's explore: {title}."},
                {"id": f"KOBJ_C4_MAT_{i+1}_02", "type": "theory", "title": title, "body": "Class 4 Maths gets more exciting with real-world problems!"},
                {"id": f"KOBJ_C4_MAT_{i+1}_03", "type": "quiz", "question": "Are you ready?", "options": ["Yes"], "correct_index": 0, "explanation": "Great!"}
            ]
        }
        check_and_save(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_class4_english():
    topics = [
        "Wake Up! (Poem)", "Neha's Alarm Clock", "Noses (Poem)", "The Little Fir Tree",
        "Run! (Poem)", "Nasruddin's Aim", "Alice in Wonderland", 
        "Grammar: Subject and Predicate", "Grammar: Tenses", "Grammar: Adverbs"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"class4_english_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "English", "difficulty": "Intermediate", "estimated_minutes": 30},
            "blocks": [
                {"id": f"KOBJ_C4_ENG_{i+1}_01", "type": "hook", "title": "English Time", "body": f"Today we will read: {title}."},
                {"id": f"KOBJ_C4_ENG_{i+1}_02", "type": "theory", "title": title, "body": "Focus on the pronunciation and the grammar rules."},
                {"id": f"KOBJ_C4_ENG_{i+1}_03", "type": "quiz", "question": "Let's test it!", "options": ["Start Quiz"], "correct_index": 0, "explanation": "Good luck!"}
            ]
        }
        check_and_save(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_class4_evs():
    topics = [
        "Going to School", "Ear to Ear", "A Day with Nandu", "The Story of Amrita",
        "Anita and the Honeybees", "Omana's Journey", "From the Window", "Reaching Grandmother's House",
        "Changing Families", "Hu Tu Tu, Hu Tu Tu", "The Valley of Flowers", "Changing Times",
        "A River's Tale", "Basva's Farm", "From Market to Home", "A Busy Month",
        "Nandita in Mumbai", "Too Much Water, Too Little Water", "Abdul in the Garden", "Eating Together",
        "Food and Fun", "The World in my Home", "Pochampalli", "Home and Abroad",
        "Spicy Riddles", "Defence Officer: Wahida", "Chuskit Goes to School"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"class4_evs_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "EVS", "difficulty": "Intermediate", "estimated_minutes": 30},
            "blocks": [
                {"id": f"KOBJ_C4_EVS_{i+1}_01", "type": "hook", "title": "Looking Around", "body": f"Today's topic: {title}."},
                {"id": f"KOBJ_C4_EVS_{i+1}_02", "type": "theory", "title": title, "body": "We will learn fascinating things about the world around us."},
                {"id": f"KOBJ_C4_EVS_{i+1}_03", "type": "quiz", "question": "Did you understand the concept?", "options": ["Yes"], "correct_index": 0, "explanation": "Perfect!"}
            ]
        }
        check_and_save(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_class4_hindi():
    topics = [
        "मन के भोले-भाले बादल", "जैसा सवाल वैसा जवाब", "किरमिच की गेंद", 
        "पापा जब बच्चे थे", "दोस्त की पोशाक", "नाव बनाओ नाव बनाओ", 
        "दान का हिसाब", "कौन?", "स्वतंत्रता की ओर",
        "व्याकरण: पर्यायवाची शब्द", "व्याकरण: विलोम शब्द"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"class4_hindi_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "Hindi", "difficulty": "Intermediate", "estimated_minutes": 30},
            "blocks": [
                {"id": f"KOBJ_C4_HIN_{i+1}_01", "type": "hook", "title": "हिंदी", "body": f"आज का पाठ: {title}"},
                {"id": f"KOBJ_C4_HIN_{i+1}_02", "type": "theory", "title": title, "body": "इस पाठ में हम नई बातें सीखेंगे।"},
                {"id": f"KOBJ_C4_HIN_{i+1}_03", "type": "quiz", "question": "तैयार हैं?", "options": ["हाँ"], "correct_index": 0, "explanation": "बहुत अच्छे!"}
            ]
        }
        check_and_save(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def update_class4_curriculum():
    filepath = "app_core/curriculum/class4.json"
    data = load_json(filepath)
    
    maths_ch = generate_class4_maths()
    eng_ch = generate_class4_english()
    evs_ch = generate_class4_evs()
    hindi_ch = generate_class4_hindi()
    
    for subj in data['subjects']:
        if subj['id'] == 'maths':
            subj['chapters'] = maths_ch
        elif subj['id'] == 'english':
            subj['chapters'] = eng_ch
        elif subj['id'] == 'evs':
            subj['chapters'] = evs_ch
        elif subj['id'] == 'hindi':
            subj['chapters'] = hindi_ch
            
    # Always update the curriculum file so the app knows about the chapters,
    # but the individual chapter content files are safe from overwriting.
    save_json(data, filepath)
    print(f"Updated {filepath} and generated missing Class 4 chapters.")

if __name__ == "__main__":
    print("Generating Class 4 chapters...")
    update_class4_curriculum()
    print("Done! (Existing files were strictly preserved and skipped.)")
