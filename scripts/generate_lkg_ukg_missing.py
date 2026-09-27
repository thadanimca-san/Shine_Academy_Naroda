import json
import os

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def update_curriculum(class_name, numbers_chapters, art_chapters):
    filepath = f"app_core/curriculum/{class_name}.json"
    data = load_json(filepath)
    
    for subj in data['subjects']:
        if subj['id'] == 'numbers':
            subj['chapters'] = numbers_chapters
        elif subj['id'] == 'art':
            subj['chapters'] = art_chapters
            
    save_json(data, filepath)
    print(f"Updated {filepath} with Numbers and Art chapters.")

def generate_lkg_numbers():
    chapters = []
    number_words = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty"]
    for i in range(11, 21):
        num = i
        word = number_words[i-11]
        chapter_id = f"lkg_numbers_ch{i-10}"
        chapters.append({"chapter_number": i-10, "title": f"Number {num}", "module_id": chapter_id, "is_available": True, "status": "Available"})
        
        data = {
            "metadata": {"id": chapter_id, "title": f"Number {num} ({word})", "subject": "Numbers", "difficulty": "Beginner", "estimated_minutes": 15},
            "blocks": [
                {"id": f"KOBJ_LKG_NUM_{num}_01", "type": "cross_subject_link", "target_chapter_id": "nursery_numbers_ch10", "title": "Revision: Numbers 1-10", "description": "Let's remember how to count up to 10!"},
                {"id": f"KOBJ_LKG_NUM_{num}_02", "type": "hook", "title": "Let's Count Higher!", "body": f"What comes after {num-1}? It's {num}!"},
                {"id": f"KOBJ_LKG_NUM_{num}_03", "type": "theory", "title": f"This is the Number {num}", "body": f"The number {num} is written as '{num}'. That is 10 and {num-10} more!"},
                {"id": f"KOBJ_LKG_NUM_{num}_04", "type": "trace_alphabet", "letter": str(num)},
                {"id": f"KOBJ_LKG_NUM_{num}_05", "type": "quiz", "question": f"Which number is {word}?", "options": [str(num), str(num-1), str(num+1)], "correct_index": 0, "explanation": "Perfect!"}
            ]
        }
        save_json(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_lkg_art():
    art_list = [("Color the Tree", "tree", "Trees give us fresh air."), ("Color the House", "house", "Houses keep us safe."), ("Color the Rainbow", "rainbow", "Rainbows have seven colors."), ("Color the Ball", "ball", "Balls are round and fun to bounce."), ("Color the Cat", "cat", "Cats say meow!")]
    chapters = []
    for i, (title, shape, desc) in enumerate(art_list):
        chapter_id = f"lkg_art_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "Art & Craft", "difficulty": "Beginner", "estimated_minutes": 15},
            "blocks": [
                {"id": f"KOBJ_LKG_ART_{i+1}_01", "type": "hook", "title": "Art Time!", "body": f"Let's color a {shape} today. {desc}"},
                {"id": f"KOBJ_LKG_ART_{i+1}_02", "type": "color_canvas", "shape": shape if shape in ['apple','star','heart','sun','car'] else 'star'},
                {"id": f"KOBJ_LKG_ART_{i+1}_03", "type": "reflection", "title": "Great Job!", "body": "You are a great artist!"}
            ]
        }
        save_json(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_ukg_numbers():
    topics = [("Counting by 10s", "10, 20, 30..."), ("Counting to 100", "Let's reach 100!"), ("Simple Addition (+1)", "Adding 1"), ("Simple Addition (+2)", "Adding 2"), ("Simple Subtraction (-1)", "Taking away 1")]
    chapters = []
    for i, (title, hook) in enumerate(topics):
        chapter_id = f"ukg_numbers_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "Numbers", "difficulty": "Beginner", "estimated_minutes": 15},
            "blocks": [
                {"id": f"KOBJ_UKG_NUM_{i+1}_01", "type": "cross_subject_link", "target_chapter_id": "lkg_numbers_ch10", "title": "Revision: Numbers up to 20", "description": "Review the number 20 before we go higher!"},
                {"id": f"KOBJ_UKG_NUM_{i+1}_02", "type": "hook", "title": "Math Magic", "body": hook},
                {"id": f"KOBJ_UKG_NUM_{i+1}_03", "type": "theory", "title": "Let's Learn", "body": f"Today we will learn about {title}."},
                {"id": f"KOBJ_UKG_NUM_{i+1}_04", "type": "quiz", "question": "Are you ready?", "options": ["Yes!", "Ready!"], "correct_index": 0, "explanation": "Let's go!"}
            ]
        }
        save_json(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

def generate_ukg_art():
    art_list = ["Paper Boat Craft", "Coloring a Scenery", "Origami Dog", "Hand Painting", "Drawing a Face"]
    chapters = []
    for i, title in enumerate(art_list):
        chapter_id = f"ukg_art_ch{i+1}"
        chapters.append({"chapter_number": i+1, "title": title, "module_id": chapter_id, "is_available": True, "status": "Available"})
        data = {
            "metadata": {"id": chapter_id, "title": title, "subject": "Art & Craft", "difficulty": "Beginner", "estimated_minutes": 15},
            "blocks": [
                {"id": f"KOBJ_UKG_ART_{i+1}_01", "type": "hook", "title": "Creative Masterpiece", "body": f"Get your materials ready for {title}!"},
                {"id": f"KOBJ_UKG_ART_{i+1}_02", "type": "theory", "title": "Steps", "body": "Follow the teacher's instructions carefully to make this craft."}
            ]
        }
        save_json(data, f"app_core/chapters/{chapter_id}.json")
    return chapters

if __name__ == "__main__":
    print("Generating LKG chapters...")
    lkg_num = generate_lkg_numbers()
    lkg_art = generate_lkg_art()
    update_curriculum("lkg", lkg_num, lkg_art)
    
    print("Generating UKG chapters...")
    ukg_num = generate_ukg_numbers()
    ukg_art = generate_ukg_art()
    update_curriculum("ukg", ukg_num, ukg_art)
    
    print("Done generating! Run merge_new_chapters.py next.")
