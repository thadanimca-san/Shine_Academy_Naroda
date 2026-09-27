import sys
import json
import os
from googletrans import Translator

def inject_solution(json_file_path, block_id, md_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as f:
        guide_en = f.read().strip()
        
    print(f"Read guide from {md_file_path} ({len(guide_en)} chars).")
    
    print("Translating to Hindi and Gujarati...")
    translator = Translator()
    
    try:
        guide_hi = translator.translate(guide_en, src='en', dest='hi').text
        guide_gu = translator.translate(guide_en, src='en', dest='gu').text
    except Exception as e:
        print(f"Translation failed: {e}")
        guide_hi = guide_en
        guide_gu = guide_en
        
    print("Loading JSON file...")
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    blocks = data.get('blocks', [])
    updated = False
    
    for block in blocks:
        if block.get('id') == block_id:
            block['solution'] = guide_en
            block['solution_hi'] = guide_hi
            block['solution_gu'] = guide_gu
            updated = True
            break
            
    if updated:
        with open(json_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write('\n')
        print(f"Successfully updated block {block_id} in {json_file_path}!")
    else:
        print(f"Error: Block {block_id} not found in {json_file_path}!")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 inject_solution.py <json_file_path> <block_id> <md_file_path>")
        sys.exit(1)
        
    inject_solution(sys.argv[1], sys.argv[2], sys.argv[3])
