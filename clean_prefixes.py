import os
import json
import re

chapters_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/'

prefix_pattern = re.compile(r'^(?:NCERT\s+)?(?:Exercise|Ex)\s+\d+\.\d+\s+(?:-\s+)?Q\d+[:\-]?\s*', re.IGNORECASE)
prefix_pattern_2 = re.compile(r'^Q\d+\.?\s*', re.IGNORECASE)
prefix_pattern_3 = re.compile(r'^Question\s+\d+[:\-\.]?\s*', re.IGNORECASE)
prefix_pattern_4 = re.compile(r'^(?:NCERT\s+)?(?:Exercise|Ex)\s+\d+\.\d+\s*-\s*', re.IGNORECASE)

keys_to_clean = [
    'body', 'body_hi', 'body_gu',
    'question', 'question_hi', 'question_gu',
    'question_en', 'question_text', 'question_text_hi', 'question_text_gu',
    'front', 'front_hi', 'front_gu'
]

def clean_text(text):
    if not isinstance(text, str):
        return text
    
    original = text
    text = prefix_pattern.sub('', text)
    text = prefix_pattern_2.sub('', text)
    text = prefix_pattern_3.sub('', text)
    text = prefix_pattern_4.sub('', text)
    
    return text, original != text

total_modifications = 0
files_modified = 0

for filename in os.listdir(chapters_dir):
    if not filename.endswith('.json'):
        continue
    filepath = os.path.join(chapters_dir, filename)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        modified_file = False
        
        blocks = []
        if isinstance(data, dict) and 'blocks' in data:
            blocks = data['blocks']
        elif isinstance(data, list):
            blocks = data
            
        for block in blocks:
            content = block.get('content', block) if isinstance(block, dict) else None
            if not isinstance(content, dict):
                continue
            
            for key in keys_to_clean:
                if key in content and content[key]:
                    cleaned, was_modified = clean_text(content[key])
                    if was_modified:
                        content[key] = cleaned
                        modified_file = True
                        total_modifications += 1
                        print(f"[{filename}] Cleaned: {cleaned[:50]}...")
                        
        if modified_file:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            files_modified += 1
            
    except Exception as e:
        print(f"Error processing {filename}: {e}")

print(f"\nModified {total_modifications} fields across {files_modified} files.")
