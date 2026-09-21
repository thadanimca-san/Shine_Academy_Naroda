import os
import json

curriculum_dir = "../curriculum"
learning_modules_dir = "."

# Mapping of curriculum IDs to specific "WOW" blocks for their first subject.
# The default fallback will just be a generic introduction.
wow_blocks = {
    "nursery": [
        {"type": "theory", "title": "Twinkle Twinkle", "difficulty": "Beginner", "bloom": "Remember", "estimated_minutes": 2, "content": "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky."},
        {"type": "flashcard", "front": "What shines in the sky at night?", "back": "A Star! ⭐️", "difficulty": "Beginner", "bloom": "Remember", "estimated_minutes": 1}
    ],
    "lkg": [
        {"type": "theory", "title": "The Alphabet", "difficulty": "Beginner", "bloom": "Remember", "estimated_minutes": 2, "content": "A is for Apple 🍎. B is for Ball ⚽️. C is for Cat 🐱."},
        {"type": "quiz", "question": "Which letter comes after A?", "options": ["C", "B", "D", "Z"], "correct_index": 1, "explanation": "B comes right after A! A, B, C, D...", "difficulty": "Beginner", "bloom": "Remember", "estimated_minutes": 1}
    ],
    "class1": [
        {"type": "theory", "title": "Addition (+)", "difficulty": "Beginner", "bloom": "Understand", "estimated_minutes": 2, "content": "Addition means putting things together. If you have 1 apple, and your friend gives you 1 more apple, you now have 2 apples! 1 + 1 = 2."},
        {"type": "quiz", "question": "What is 2 + 2?", "options": ["3", "4", "5", "22"], "correct_index": 1, "explanation": "If you have 2 fingers up, and raise 2 more, you have 4 fingers up!", "difficulty": "Beginner", "bloom": "Apply", "estimated_minutes": 1}
    ],
    "class11_science": [
        {"type": "theory", "title": "Units and Measurements", "difficulty": "Beginner", "bloom": "Understand", "estimated_minutes": 3, "content": "Physics is a quantitative science, based on measurement of physical quantities. Certain physical quantities have been chosen as fundamental or base quantities (like Length, Mass, Time)."},
        {"type": "flashcard", "front": "What is the SI unit of Time?", "back": "The second (s).", "difficulty": "Beginner", "bloom": "Remember", "estimated_minutes": 1}
    ],
    "neet": [
        {"type": "theory", "title": "Photosynthesis", "difficulty": "Advanced", "bloom": "Understand", "estimated_minutes": 3, "content": "Photosynthesis is a physico-chemical process by which green plants use light energy to drive the synthesis of organic compounds. It takes place primarily in the chloroplasts."},
        {"type": "quiz", "question": "Which of the following is NOT required for photosynthesis?", "options": ["Sunlight", "Carbon Dioxide", "Oxygen", "Chlorophyll"], "correct_index": 2, "explanation": "Oxygen is a BYPRODUCT of photosynthesis, not a requirement! Plants require CO2, water, sunlight, and chlorophyll.", "difficulty": "Advanced", "bloom": "Analyze", "estimated_minutes": 2}
    ],
    "ca_foundation": [
        {"type": "theory", "title": "Double Entry System", "difficulty": "Intermediate", "bloom": "Understand", "estimated_minutes": 3, "content": "The double-entry system of accounting or bookkeeping means that for every business transaction, amounts must be recorded in a minimum of two accounts. The accounting equation must always balance: Assets = Liabilities + Equity."},
        {"type": "flashcard", "front": "If an asset increases, do you debit or credit it?", "back": "DEBIT. An increase in assets is always recorded as a debit.", "difficulty": "Intermediate", "bloom": "Apply", "estimated_minutes": 1}
    ]
}

def get_default_blocks(subject_name):
    return [
        {"type": "theory", "title": f"Introduction to {subject_name}", "difficulty": "Beginner", "bloom": "Understand", "estimated_minutes": 2, "content": f"Welcome to the incredible world of {subject_name}! This module will lay the foundation for everything you are about to learn."},
        {"type": "quiz", "question": f"Are you ready to master {subject_name}?", "options": ["Yes!", "Absolutely!", "Let's go!"], "correct_index": 0, "explanation": "That's the spirit! Let's dive in.", "difficulty": "Beginner", "bloom": "Apply", "estimated_minutes": 1}
    ]

# Ensure we are in learning_modules directory
os.makedirs(learning_modules_dir, exist_ok=True)

# Iterate through all curriculum JSONs
for filename in os.listdir(curriculum_dir):
    if filename.endswith(".json"):
        filepath = os.path.join(curriculum_dir, filename)
        with open(filepath, 'r') as f:
            data = json.load(f)
            
        curr_id = data.get("curriculum_id")
        subjects = data.get("subjects", [])
        
        if not curr_id or not subjects:
            continue
            
        # We don't want to overwrite class9 since we built massive chapters for it!
        if curr_id == "gseb_class9":
            continue
            
        # Pick the first subject
        first_subject = subjects[0]
        subj_id = first_subject.get("id")
        subj_name = first_subject.get("name")
        
        # 1. Create chapters.json
        chapters_filename = f"{curr_id}_{subj_id}_chapters.json"
        chapters_filepath = os.path.join(learning_modules_dir, chapters_filename)
        
        # Don't overwrite if it exists (e.g. gseb_class12_commerce_accountancy_chapters.json might exist)
        if not os.path.exists(chapters_filepath):
            chapters_data = [
                {
                    "id": f"{curr_id}_{subj_id}_ch1",
                    "title": f"Chapter 1: Basics of {subj_name}",
                    "description": f"A fully functional introduction to {subj_name}.",
                    "duration_minutes": 10,
                    "order": 1
                }
            ]
            with open(chapters_filepath, 'w', encoding='utf-8') as f:
                json.dump(chapters_data, f, indent=2)
            print(f"Generated {chapters_filepath}")
            
        # 2. Create the ch1 folder and blocks.json
        ch_dir = os.path.join(learning_modules_dir, f"{curr_id}_{subj_id}_ch1")
        os.makedirs(ch_dir, exist_ok=True)
        blocks_filepath = os.path.join(ch_dir, "blocks.json")
        
        if not os.path.exists(blocks_filepath):
            blocks_data = wow_blocks.get(curr_id, get_default_blocks(subj_name))
            with open(blocks_filepath, 'w', encoding='utf-8') as f:
                json.dump(blocks_data, f, indent=2)
            print(f"Generated {blocks_filepath}")

print("Successfully generated all concepts across the framework!")
