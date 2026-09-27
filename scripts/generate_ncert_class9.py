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

def generate_ncert_class9_maths():
    topics = [
        "Number Systems", "Polynomials", "Coordinate Geometry", "Linear Equations in Two Variables",
        "Introduction to Euclid's Geometry", "Lines and Angles", "Triangles", "Quadrilaterals",
        "Areas of Parallelograms and Triangles", "Circles", "Constructions", "Heron's Formula",
        "Surface Areas and Volumes", "Statistics", "Probability"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"ncert_class9_maths_ch{i+1}"
        chapters.append({"chapter_id": chapter_id, "title": f"Chapter {i+1}: {title}", "module_id": chapter_id})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "Mathematics", "difficulty": "Advanced", "estimated_minutes": 55},
            "blocks": [
                {"id": f"KOBJ_NC9_MAT_{i+1}_01", "type": "hook", "title": "Maths Mastery", "body": f"Topic: {title}."},
                {"id": f"KOBJ_NC9_MAT_{i+1}_02", "type": "theory", "title": title, "body": "Class 9 Maths is the stepping stone to board exams."},
                {"id": f"KOBJ_NC9_MAT_{i+1}_03", "type": "quiz", "question": "Are you ready?", "options": ["Yes"], "correct_index": 0, "explanation": "Let's begin!"}
            ]
        }
        check_and_save(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_ncert_class9_science():
    topics = [
        "Matter in Our Surroundings", "Is Matter Around Us Pure", "Atoms and Molecules", 
        "Structure of the Atom", "The Fundamental Unit of Life", "Tissues", 
        "Diversity in Living Organisms", "Motion", "Force and Laws of Motion", 
        "Gravitation", "Work and Energy", "Sound", "Reproduction", 
        "Natural Resources", "Improvement in Food Resources"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"ncert_class9_science_ch{i+1}"
        chapters.append({"chapter_id": chapter_id, "title": f"Chapter {i+1}: {title}", "module_id": chapter_id})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "Science", "difficulty": "Advanced", "estimated_minutes": 55},
            "blocks": [
                {"id": f"KOBJ_NC9_SCI_{i+1}_01", "type": "hook", "title": "Science Exploration", "body": f"Topic: {title}."},
                {"id": f"KOBJ_NC9_SCI_{i+1}_02", "type": "theory", "title": title, "body": "Science reveals the logic behind natural events."},
                {"id": f"KOBJ_NC9_SCI_{i+1}_03", "type": "quiz", "question": "Let's test it!", "options": ["Start"], "correct_index": 0, "explanation": "Perfect!"}
            ]
        }
        check_and_save(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_ncert_class9_social():
    topics = [
        "The French Revolution", "Socialism in Europe & Russian Revolution", "Nazism and the Rise of Hitler",
        "Forest Society and Colonialism", "Pastoralists in the Modern World", "India – Size and Location",
        "Physical Features of India", "Drainage", "Climate", "Natural Vegetation and Wildlife",
        "Population", "What is Democracy? Why Democracy?", "Constitutional Design", "Electoral Politics",
        "Working of Institutions", "Democratic Rights", "The Story of Village Palampur",
        "People as Resource", "Poverty as a Challenge", "Food Security in India"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"ncert_class9_social_science_ch{i+1}"
        chapters.append({"chapter_id": chapter_id, "title": f"Chapter {i+1}: {title}", "module_id": chapter_id})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "Social Science", "difficulty": "Advanced", "estimated_minutes": 55},
            "blocks": [
                {"id": f"KOBJ_NC9_SOC_{i+1}_01", "type": "hook", "title": "Social Studies", "body": f"Topic: {title}."},
                {"id": f"KOBJ_NC9_SOC_{i+1}_02", "type": "theory", "title": title, "body": "Understanding society, history, and economics."},
                {"id": f"KOBJ_NC9_SOC_{i+1}_03", "type": "quiz", "question": "Did you understand?", "options": ["Yes"], "correct_index": 0, "explanation": "Great!"}
            ]
        }
        check_and_save(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_ncert_class9_english():
    topics = [
        "The Fun They Had", "The Sound of Music", "The Little Girl", "A Truly Beautiful Mind",
        "The Snake and the Mirror", "My Childhood", "Packing", "Reach for the Top",
        "The Bond of Love", "Kathmandu", "If I Were You"
    ]
    chapters = []
    for i, title in enumerate(topics):
        chapter_id = f"ncert_class9_english_ch{i+1}"
        chapters.append({"chapter_id": chapter_id, "title": f"Chapter {i+1}: {title}", "module_id": chapter_id})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "English", "difficulty": "Advanced", "estimated_minutes": 55},
            "blocks": [
                {"id": f"KOBJ_NC9_ENG_{i+1}_01", "type": "hook", "title": "Beehive Literature", "body": f"Chapter: {title}"},
                {"id": f"KOBJ_NC9_ENG_{i+1}_02", "type": "theory", "title": title, "body": "English language builds communication skills."},
                {"id": f"KOBJ_NC9_ENG_{i+1}_03", "type": "quiz", "question": "Ready?", "options": ["हाँ (Yes)"], "correct_index": 0, "explanation": "बहुत अच्छे!"}
            ]
        }
        check_and_save(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def update_ncert_class9_curriculum():
    filepath = "app_core/curriculum/ncert_class9.json"
    data = load_json(filepath)
    
    maths_ch = generate_ncert_class9_maths()
    sci_ch = generate_ncert_class9_science()
    soc_ch = generate_ncert_class9_social()
    eng_ch = generate_ncert_class9_english()
    
    # Update or add subjects dynamically
    def update_or_add_subject(subj_id, name, chapters):
        for subj in data.get('subjects', []):
            if subj.get('id') == subj_id:
                subj['chapters'] = chapters
                return
        # If not found, add it
        if 'subjects' not in data:
            data['subjects'] = []
        data['subjects'].append({
            "id": subj_id,
            "name": name,
            "chapters": chapters
        })
        
    update_or_add_subject('ncert_class9_maths', 'Maths', maths_ch)
    update_or_add_subject('ncert_class9_science', 'Science', sci_ch)
    update_or_add_subject('ncert_class9_social_science', 'Social Science', soc_ch)
    update_or_add_subject('ncert_class9_english', 'English', eng_ch)
            
    save_json(data, filepath)
    print(f"Updated {filepath} and added missing subjects (Maths, Social Science, English).")

if __name__ == "__main__":
    print("Generating NCERT Class 9 chapters...")
    update_ncert_class9_curriculum()
    print("Done! (Existing files were strictly preserved and skipped.)")
