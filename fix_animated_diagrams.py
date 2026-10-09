import os
import glob
import json

json_files = glob.glob('app_core/chapters/*.json')
fixed_count = 0

for jf in json_files:
    try:
        with open(jf, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        modified = False
        
        # Determine the root structure
        blocks = None
        if isinstance(data, list):
            blocks = data
        elif isinstance(data, dict):
            if 'learning_blocks' in data:
                blocks = data['learning_blocks']
            elif 'blocks' in data:
                blocks = data['blocks']
                
        if blocks and isinstance(blocks, list):
            for i, b in enumerate(blocks):
                if isinstance(b, dict) and b.get('type') == 'animated_diagram':
                    # Check if this is the corrupted version created by process_images.py
                    if 'asset_path' in b and 'content' not in b:
                        b['type'] = 'image'
                        b['image_url'] = b['asset_path']
                        del b['asset_path']
                        modified = True
                        fixed_count += 1
                        
        if modified:
            with open(jf, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                
    except Exception as e:
        print(f"Error processing {jf}: {e}")

print(f"Fixed {fixed_count} corrupted animated_diagram blocks across JSON files.")
