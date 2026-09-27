import json
import os

curriculum_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum'

class10_math_chapters = [
    "Real Numbers", "Polynomials", "Linear Equations", "Quadratic Equations",
    "Arithmetic Progressions", "Triangles", "Coordinate Geometry", "Trigonometry",
    "Applications of Trigonometry", "Circles", "Constructions", "Areas Related to Circles",
    "Surface Areas and Volumes", "Statistics", "Probability"
]

class10_english_chapters = [
    "A Letter to God (First Flight)",
    "Nelson Mandela: Long Walk to Freedom",
    "Two Stories about Flying",
    "From the Diary of Anne Frank",
    "The Hundred Dresses - I",
    "The Hundred Dresses - II",
    "Glimpses of India",
    "Mijbil the Otter",
    "Madam Rides the Bus",
    "The Sermon at Benares",
    "The Proposal",
    "A Triumph of Surgery (Supplementary)",
    "The Thief's Story (Supplementary)",
    "The Midnight Visitor (Supplementary)",
    "A Question of Trust (Supplementary)",
    "Footprints without Feet (Supplementary)"
]

class10_science_chapters = [
    "Chemical Reactions and Equations",
    "Acids, Bases and Salts",
    "Metals and Non-metals",
    "Carbon and its Compounds",
    "Life Processes",
    "Control and Coordination",
    "How do Organisms Reproduce?",
    "Heredity and Evolution",
    "Light - Reflection and Refraction",
    "The Human Eye and the Colourful World",
    "Electricity",
    "Magnetic Effects of Electric Current",
    "Our Environment"
]

files_to_update = ['ncert_class10.json', 'gseb_class10.json', 'cbse_class10.json']

for filename in files_to_update:
    filepath = os.path.join(curriculum_dir, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r') as f:
        data = json.load(f)
        
    prefix = filename.split('_')[0] # ncert, gseb, cbse
        
    # Find Maths
    math_subject = None
    for s in data.get('subjects', []):
        if 'math' in s.get('id', '').lower() or 'math' in s.get('name', '').lower():
            math_subject = s
            break
            
    if math_subject:
        math_subject['chapters'] = []
        for i, title in enumerate(class10_math_chapters):
            math_subject['chapters'].append({
                "chapter_id": f"{prefix}_class10_math_ch{i+1}",
                "title": f"Chapter {i+1}: {title}",
                "module_id": f"{prefix}_class10_maths_ch{i+1}" # Maths module ids usually have 'maths' not 'math'
            })
            
        # Fix color_hex and icon if missing
        if 'color_hex' not in math_subject:
            math_subject['color_hex'] = "0xFFE91E63"
        if 'icon' not in math_subject:
            math_subject['icon'] = "calculate"
            
    # Find or Create English
    eng_subject = None
    for s in data.get('subjects', []):
        if 'english' in s.get('id', '').lower() or 'english' in s.get('name', '').lower():
            eng_subject = s
            break
            
    if not eng_subject:
        eng_subject = {
            "id": f"{prefix}_class10_english",
            "name": "English",
            "color_hex": "0xFFFF9800",
            "icon": "language",
            "chapters": []
        }
        data['subjects'].append(eng_subject)
        
    eng_subject['chapters'] = []
    
    # First Flight (1-11)
    for i in range(11):
        eng_subject['chapters'].append({
            "chapter_id": f"{prefix}_class10_english_ch{i+1}",
            "title": f"Chapter {i+1}: {class10_english_chapters[i]}",
            "module_id": f"{prefix}_class10_english_ch{i+1}"
        })
        
    # Footprints Without Feet (Supplementary 1-5)
    for i in range(11, 16):
        sup_index = i - 10
        eng_subject['chapters'].append({
            "chapter_id": f"{prefix}_class10_english_sup_ch{sup_index}",
            "title": f"Chapter {i+1}: {class10_english_chapters[i]}",
            "module_id": f"{prefix}_class10_english_sup_ch{sup_index}"
        })
        
    # Find or Create Science
    sci_subject = None
    for s in data.get('subjects', []):
        if 'science' in s.get('id', '').lower() or 'science' in s.get('name', '').lower():
            if 'social' not in s.get('name', '').lower() and 'social' not in s.get('id', '').lower():
                sci_subject = s
                break
                
    if not sci_subject:
        sci_subject = {
            "id": f"{prefix}_class10_science",
            "name": "Science",
            "color_hex": "0xFF4CAF50",
            "icon": "science",
            "chapters": []
        }
        data['subjects'].append(sci_subject)
        
    sci_subject['chapters'] = []
    
    # Board Exam Paper 1
    sci_subject['chapters'].append({
        "chapter_id": f"{prefix}_class10_science_mock_exam_1",
        "title": "Board Exam: Full Science Paper 1 (With Solutions)",
        "module_id": f"{prefix}_class10_science_mock_exam_1"
    })
    
    for i, title in enumerate(class10_science_chapters):
        sci_subject['chapters'].append({
            "chapter_id": f"{prefix}_class10_science_ch{i+1}",
            "title": f"Chapter {i+1}: {title}",
            "module_id": f"{prefix}_class10_science_ch{i+1}"
        })

    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
        
    print(f"Updated {filename}")
