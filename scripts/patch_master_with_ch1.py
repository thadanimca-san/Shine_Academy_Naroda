import json

master_file = "/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/master_curriculum.json"

with open(master_file, 'r', encoding='utf-8') as f:
    master_data = json.load(f)

for board in ['gseb', 'cbse', 'ncert']:
    module_id = f"{board}_class10_maths_ch1"
    chapter_file = f"/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/{module_id}.json"
    try:
        with open(chapter_file, 'r', encoding='utf-8') as f:
            chapter_data = json.load(f)
            
        blocks = chapter_data.get('blocks', [])
        
        if module_id in master_data:
            master_data[module_id]['blocks'] = blocks
            print(f"Updated {module_id} in master_curriculum with {len(blocks)} blocks.")
    except Exception as e:
        print(f"Error reading {chapter_file}: {e}")

with open(master_file, 'w', encoding='utf-8') as f:
    json.dump(master_data, f, indent=2, ensure_ascii=False)
    
print("Successfully patched master_curriculum.json")
