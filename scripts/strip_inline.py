import json
import os
import glob
import re

inline_trans_pattern = re.compile(r'[\(\'\"\[]?\s*[\u0900-\u097F]+[\s/\|\\]+[\u0A80-\u0AFF]+\s*[\)\'\"\]]?')

def clean_inline_text(text):
    if not text or not isinstance(text, str):
        return text
    cleaned = inline_trans_pattern.sub('', text)
    cleaned = re.sub(r'\s*\(\s*\)\s*', ' ', cleaned)
    cleaned = re.sub(r'\s{2,}', ' ', cleaned)
    return cleaned.strip()

def process_file(file_path):
    print(f"Processing: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        modified = False
        blocks = []
        
        if 'blocks' in data:
            blocks = data['blocks']
        elif 'content' in data and isinstance(data['content'], list):
            blocks = data['content']
            
        if not blocks:
            return False

        for block in blocks:
            for field in ['body', 'content', 'title', 'question', 'feedback_correct', 'term', 'definition', 'tip', 'guidance']:
                if field in block and block[field]:
                    original_text = block[field]
                    cleaned_text = clean_inline_text(original_text)
                    if cleaned_text != original_text:
                        block[field] = cleaned_text
                        modified = True
                        
                        # Also delete the hi/gu fields so they get dynamically recreated from the clean text
                        if f"{field}_hi" in block:
                            del block[f"{field}_hi"]
                        if f"{field}_gu" in block:
                            del block[f"{field}_gu"]

        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Successfully cleaned: {file_path}")
            return True
        return False
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

# Specifically target the file in the screenshot
process_file('app_core/chapters/gseb_class10_science_ch1.json')
process_file('app_core/chapters/ncert_class10_science_ch1.json')

