import json
import os

curriculum_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum'

ss_chapters = [
    "Heritage of India",
    "Cultural Heritage of India: Traditional Handicrafts and Fine Arts",
    "Cultural Heritage of India: Sculpture and Architecture",
    "Cultural Heritage of India: Literature",
    "India's Heritage of Science and Technology",
    "Places of Indian Cultural Heritage",
    "Preservation of Our Heritage",
    "Natural Resources",
    "Forest and Wildlife Resources",
    "India: Agriculture",
    "India: Water Resources",
    "India: Minerals and Energy Resources",
    "Manufacturing Industries",
    "Transportation, Communication and Trade",
    "Economic Development",
    "Economic Liberalization and Globalization",
    "Economic Problems and Challenges: Poverty and Unemployment",
    "Price Rise and Consumer Awareness",
    "Human Development",
    "Social Problems of India and Challenges",
    "Social Change"
]

files_to_update = ['ncert_class10.json', 'gseb_class10.json', 'cbse_class10.json']

for filename in files_to_update:
    filepath = os.path.join(curriculum_dir, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r') as f:
        data = json.load(f)
        
    prefix = filename.split('_')[0] # ncert, gseb, cbse
        
    # Find or Create Social Science
    ss_subject = None
    for s in data.get('subjects', []):
        if 'social' in s.get('id', '').lower() or 'social' in s.get('name', '').lower():
            ss_subject = s
            break
            
    if not ss_subject:
        ss_subject = {
            "id": f"{prefix}_class10_social",
            "name": "Social Science",
            "color_hex": "0xFF9C27B0",
            "icon": "book",
            "chapters": []
        }
        # Insert after Science and Math, before English if possible
        data['subjects'].insert(2, ss_subject)
        
    ss_subject['chapters'] = []
    
    for i, title in enumerate(ss_chapters):
        ss_subject['chapters'].append({
            "chapter_id": f"{prefix}_class10_social_science_ch{i+1}",
            "title": f"Chapter {i+1}: {title}",
            "module_id": f"{prefix}_class10_social_science_ch{i+1}"
        })

    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
        
    print(f"Updated {filename} with Social Science.")
