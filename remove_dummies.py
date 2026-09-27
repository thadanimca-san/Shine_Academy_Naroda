import json
import glob

files = glob.glob('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/*.json')
total_removed = 0

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except Exception as e:
            continue
    
    if not isinstance(data, dict) or 'blocks' not in data:
        continue
        
    original_len = len(data['blocks'])
    new_blocks = []
    
    for block in data['blocks']:
        if not isinstance(block, dict):
            new_blocks.append(block)
            continue
            
        is_dummy = False
        if block.get('type') in ['quiz', 'quiz_multiple_choice']:
            q = block.get('question', '')
            if 'Sample mock test question' in str(q):
                is_dummy = True
        
        if not is_dummy:
            new_blocks.append(block)
            
    removed = original_len - len(new_blocks)
    if removed > 0:
        data['blocks'] = new_blocks
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Removed {removed} dummy blocks from {file_path}")
        total_removed += removed

print(f"Total dummy blocks removed: {total_removed}")
