import os
import re
import json

SOURCE_DIR = 'lib/features/learning/school/maths_simulation/data/chapters/class10'
TARGET_DIR = 'lib/content_database/class10_maths'

if not os.path.exists(TARGET_DIR):
    os.makedirs(TARGET_DIR)

# Basic regex for extracting from the Dart ChapterModel
name_re = re.compile(r'chapterName:\s*"([^"]+)"')
id_re = re.compile(r'chapterId:\s*"([^"]+)"')

def parse_dart_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    name_match = name_re.search(content)
    id_match = id_re.search(content)

    ch_name = name_match.group(1) if name_match else "Unknown"
    ch_id = id_match.group(1) if id_match else "unknown_id"

    # We will wrap the existing questions into our JSON schema structure
    # For now, we will extract numerical problems
    numerical_re = re.finditer(r'NumericalProblem\([^)]+question:\s*"([^"]+)"[^)]+numericAnswer:\s*([\d.]+)[^)]+\)', content)
    
    blocks = []
    
    # Let's add a Socratic Hook first to follow the Gold Pedagogy Standard
    blocks.append({
        "type": "hook",
        "id": f"{ch_id}_hook",
        "title": f"Welcome to {ch_name}",
        "title_hi": f"{ch_name} में आपका स्वागत है",
        "body": "Before we dive in, let's look at a real-life example of this concept.",
        "body_hi": "इससे पहले कि हम शुरू करें, आइए इस अवधारणा का एक वास्तविक जीवन उदाहरण देखें।"
    })

    # Add extracted problems
    for i, match in enumerate(numerical_re):
        question = match.group(1)
        answer = match.group(2)
        blocks.append({
            "type": "worked_example",
            "id": f"{ch_id}_ex_{i}",
            "title": f"Example {i+1}",
            "title_hi": f"उदाहरण {i+1}",
            "body": question,
            "body_hi": question, # Translate later
            "answer": answer
        })

    json_payload = {
        "metadata": {
            "id": ch_id,
            "title": ch_name,
            "subject": "Mathematics",
            "grade": 10,
            "board": "CBSE/GSEB"
        },
        "blocks": blocks
    }

    return ch_id, json_payload

def main():
    if not os.path.exists(SOURCE_DIR):
        print(f"Source dir {SOURCE_DIR} not found.")
        return
        
    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith('.dart')]
    print(f"Found {len(files)} files to migrate.")

    for f_name in files:
        filepath = os.path.join(SOURCE_DIR, f_name)
        ch_id, json_data = parse_dart_file(filepath)
        
        target_file = os.path.join(TARGET_DIR, f"{ch_id}.json")
        with open(target_file, 'w', encoding='utf-8') as out_f:
            json.dump(json_data, out_f, indent=2, ensure_ascii=False)
            
        print(f"Migrated {f_name} -> {target_file}")

if __name__ == '__main__':
    main()
