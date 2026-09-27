import json
import glob

files = glob.glob('app_core/chapters/*.json')
updated_files = 0
total_replaced = 0

for file_path in files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        continue
        
    blocks_list = []
    is_list = False
    
    if isinstance(data, list):
        blocks_list = data
        is_list = True
    elif isinstance(data, dict) and 'blocks' in data:
        blocks_list = data['blocks']
    else:
        continue
        
    changed = False
    for block in blocks_list:
        if isinstance(block, dict) and block.get('type') == 'quiz_multiple_choice':
            block['type'] = 'mcq'
            changed = True
            total_replaced += 1
            
    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        updated_files += 1

print(f"Replaced {total_replaced} 'quiz_multiple_choice' types with 'mcq' across {updated_files} files.")
