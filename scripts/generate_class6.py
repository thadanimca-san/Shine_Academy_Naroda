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

def generate_class6_maths():
    topics = [
        "Knowing Our Numbers", "Whole Numbers", "Playing with Numbers", "Basic Geometrical Ideas",
        "Understanding Elementary Shapes", "Integers", "Fractions", "Decimals",
        "Data Handling", "Mensuration", "Algebra", "Ratio and Proportion",
        "Symmetry", "Practical Geometry"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"class6_maths_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "Mathematics", "difficulty": "Intermediate", "estimated_minutes": 40},
            "blocks": [
                {"id": f"KOBJ_C6_MAT_{i+1}_01", "type": "hook", "title": "Advanced Maths", "body": f"Welcome to Class 6 Mathematics. Topic: {title}."},
                {"id": f"KOBJ_C6_MAT_{i+1}_02", "type": "theory", "title": title, "body": "Maths is the language of the universe."},
                {"id": f"KOBJ_C6_MAT_{i+1}_03", "type": "quiz", "question": "Are you ready?", "options": ["Yes"], "correct_index": 0, "explanation": "Let's begin!"}
            ]
        }
        check_and_save(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_class6_science():
    topics = [
        "Food: Where does it come from?", "Components of Food", "Fibre to Fabric", "Sorting Materials into Groups",
        "Separation of Substances", "Changes Around Us", "Getting to Know Plants", "Body Movements",
        "The Living Organisms and Their Surroundings", "Motion and Measurement of Distances", 
        "Light, Shadows and Reflections", "Electricity and Circuits", "Fun with Magnets", 
        "Water", "Air Around Us", "Garbage In, Garbage Out"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"class6_science_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "Science", "difficulty": "Intermediate", "estimated_minutes": 40},
            "blocks": [
                {"id": f"KOBJ_C6_SCI_{i+1}_01", "type": "hook", "title": "Science Exploration", "body": f"Today we discover: {title}."},
                {"id": f"KOBJ_C6_SCI_{i+1}_02", "type": "theory", "title": title, "body": "Observe, experiment, and conclude."},
                {"id": f"KOBJ_C6_SCI_{i+1}_03", "type": "quiz", "question": "Let's test it!", "options": ["Start"], "correct_index": 0, "explanation": "Perfect!"}
            ]
        }
        check_and_save(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_class6_social():
    topics = [
        "What, Where, How and When? (History)", "On the Trail of the Earliest People", "From Gathering to Growing Food",
        "In the Earliest Cities", "What Books and Burials Tell Us", "The Earth in the Solar System (Geography)",
        "Globe: Latitudes and Longitudes", "Motions of the Earth", "Maps", "Major Domains of the Earth",
        "Understanding Diversity (Civics)", "Diversity and Discrimination", "What is Government?", "Panchayati Raj"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"class6_social_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "Social Science", "difficulty": "Intermediate", "estimated_minutes": 40},
            "blocks": [
                {"id": f"KOBJ_C6_SOC_{i+1}_01", "type": "hook", "title": "Social Studies", "body": f"Topic: {title}."},
                {"id": f"KOBJ_C6_SOC_{i+1}_02", "type": "theory", "title": title, "body": "Learn about our past, our planet, and our society."},
                {"id": f"KOBJ_C6_SOC_{i+1}_03", "type": "quiz", "question": "Did you understand?", "options": ["Yes"], "correct_index": 0, "explanation": "Great!"}
            ]
        }
        check_and_save(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_class6_english():
    topics = [
        "Who Did Patrick's Homework?", "How the Dog Found Himself a New Master!", "Taro's Reward", 
        "An Indian - American Woman in Space", "A Different Kind of School", "Who I Am", 
        "Fair Play", "A Game of Chance", "Desert Animals", "The Banyan Tree"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"class6_english_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "English", "difficulty": "Intermediate", "estimated_minutes": 40},
            "blocks": [
                {"id": f"KOBJ_C6_ENG_{i+1}_01", "type": "hook", "title": "English Literature", "body": f"Chapter: {title}"},
                {"id": f"KOBJ_C6_ENG_{i+1}_02", "type": "theory", "title": title, "body": "Enjoy reading the story."},
                {"id": f"KOBJ_C6_ENG_{i+1}_03", "type": "quiz", "question": "Ready?", "options": ["हाँ (Yes)"], "correct_index": 0, "explanation": "बहुत अच्छे!"}
            ]
        }
        check_and_save(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def update_class6_curriculum():
    filepath = "app_core/curriculum/class6.json"
    data = load_json(filepath)
    
    maths_ch = generate_class6_maths()
    sci_ch = generate_class6_science()
    soc_ch = generate_class6_social()
    eng_ch = generate_class6_english()
    
    for subj in data['subjects']:
        if subj['id'] == 'maths':
            subj['chapters'] = maths_ch
        elif subj['id'] == 'science':
            subj['chapters'] = sci_ch
        elif subj['id'] == 'social':
            subj['chapters'] = soc_ch
        elif subj['id'] == 'english':
            subj['chapters'] = eng_ch
            
    save_json(data, filepath)
    print(f"Updated {filepath} and generated missing Class 6 chapters.")

if __name__ == "__main__":
    print("Generating Class 6 chapters...")
    update_class6_curriculum()
    print("Done! (Existing files were strictly preserved and skipped.)")
