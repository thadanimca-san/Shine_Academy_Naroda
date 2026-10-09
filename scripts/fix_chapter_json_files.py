#!/usr/bin/env python3
import json
import glob
import os

CHAPTERS_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

def fix_chapter_file(filepath):
    print(f"Checking {os.path.basename(filepath)}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"Error loading {filepath}: {e}")
            return
            
    is_list = isinstance(data, list)
    blocks = data if is_list else data.get('blocks', [])
    
    modified = False
    for i, b in enumerate(blocks):
        if not isinstance(b, dict):
            continue
            
        # Convert "content" -> "body" for theory, definition, worked_example, common_mistakes, etc.
        if 'content' in b and 'body' not in b:
            if isinstance(b['content'], str):
                b['body'] = b['content']
                modified = True
                
        # Ensure title_hi and title_gu don't equal English if missing
        btype = b.get('type', 'theo')
        if not b.get('id'):
            fname = os.path.basename(filepath).replace('.json', '')
            b['id'] = f"KOBJ_{fname.upper()}_{btype.upper()[:4]}_{i+1:03d}"
            modified = True
            
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Fixed {os.path.basename(filepath)}")
    else:
        print(f"No changes needed for {os.path.basename(filepath)}")

def main():
    json_files = glob.glob(f"{CHAPTERS_DIR}/*.json")
    for jf in json_files:
        fix_chapter_file(jf)

if __name__ == '__main__':
    main()
