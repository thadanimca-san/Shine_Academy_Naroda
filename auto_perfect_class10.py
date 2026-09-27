import json
import glob
import time
import uuid
import sys
from deep_translator import GoogleTranslator

files = glob.glob('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/*class10*.json')
translator = GoogleTranslator(source='en', target='hi')

def translate_safe(text):
    if not text or not isinstance(text, str):
        return text
    try:
        # Avoid translating math formulas entirely if they are purely math, but deep-translator handles strings.
        # Add a tiny sleep to avoid rate limits
        time.sleep(0.5)
        res = translator.translate(text)
        return res
    except Exception as e:
        print(f"Translation error for text: {text[:30]}... -> {e}")
        time.sleep(5)
        try:
            return translator.translate(text)
        except:
            return text # Fallback to original

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Skipping {file_path}: {e}")
        return False
        
    if not isinstance(data, dict) or 'blocks' not in data:
        return False
        
    changed = False
    
    # 1. Ensure chapter ID
    if 'metadata' in data and 'id' in data['metadata']:
        ch_id = data['metadata']['id']
    else:
        ch_id = file_path.split('/')[-1].replace('.json', '')
        if 'metadata' not in data:
            data['metadata'] = {}
        data['metadata']['id'] = ch_id
        changed = True

    # 2. Fix blocks
    for idx, block in enumerate(data['blocks']):
        if not isinstance(block, dict):
            continue
            
        b_type = block.get('type', 'theory')
        
        # Add ID if missing
        if 'id' not in block or block['id'] == 'UNKNOWN_ID':
            block['id'] = f"{ch_id.upper()}_{b_type.upper()}_{idx:03d}"
            changed = True
            
        # Add missing Hindi translations
        if b_type in ['theory', 'hook', 'teacher_tip', 'memory_trick', 'common_mistakes', 'real_world_example', 'insight']:
            if 'title' in block and 'title_hi' not in block:
                print(f"[{ch_id}] Translating title...")
                block['title_hi'] = translate_safe(block['title'])
                changed = True
            if 'body' in block and 'body_hi' not in block:
                print(f"[{ch_id}] Translating body...")
                block['body_hi'] = translate_safe(block['body'])
                changed = True
        elif b_type in ['quiz', 'mcq', 'quiz_multiple_choice']:
            if 'question' in block and 'question_hi' not in block:
                print(f"[{ch_id}] Translating question...")
                block['question_hi'] = translate_safe(block['question'])
                changed = True
            if 'options' in block and 'options_hi' not in block:
                print(f"[{ch_id}] Translating options...")
                block['options_hi'] = [translate_safe(opt) for opt in block['options']]
                changed = True
            if 'explanation' in block and 'explanation_hi' not in block:
                print(f"[{ch_id}] Translating explanation...")
                block['explanation_hi'] = translate_safe(block['explanation'])
                changed = True
                
        # If any other fields like 'content' need it
        if 'content' in block and 'content_hi' not in block:
            if isinstance(block['content'], str):
                print(f"[{ch_id}] Translating content...")
                block['content_hi'] = translate_safe(block['content'])
                changed = True

    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Updated {file_path}")
        return True
    return False

total_updated = 0
for fp in files:
    if process_file(fp):
        total_updated += 1
        
print(f"Processing complete. Updated {total_updated} files.")
