import json
import glob
import uuid

def add_missing_ids(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if 'blocks' not in data:
            return
            
        modified = False
        for i, block in enumerate(data['blocks']):
            if 'id' not in block:
                block['id'] = f"KOBJ_AUTO_{uuid.uuid4().hex[:6].upper()}"
                modified = True
                
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Fixed missing IDs in {filepath}")
            
    except Exception as e:
        print(f"Error in {filepath}: {e}")

files = glob.glob('app_core/chapters/*class10_maths_ch1.json')
for f in files:
    add_missing_ids(f)
