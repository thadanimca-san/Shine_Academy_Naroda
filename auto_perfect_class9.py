import json
import glob
import time
import sys
from deep_translator import GoogleTranslator, MyMemoryTranslator

files = glob.glob('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/*class9*.json')
g_translator = GoogleTranslator(source='en', target='hi')
m_translator = MyMemoryTranslator(source='en-US', target='hi-IN')

def translate_safe(text):
    if not text or not isinstance(text, str):
        return text
    try:
        time.sleep(0.5)
        return g_translator.translate(text)
    except Exception as e:
        print(f"GoogleTranslator failed for '{text[:20]}': {e}. Trying MyMemoryTranslator...")
        try:
            time.sleep(1)
            return m_translator.translate(text)
        except Exception as e2:
            print(f"Both translators failed for '{text[:20]}'. Skipping translation.")
            return None # Return None if translation completely fails!

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception:
        return False
        
    if not isinstance(data, dict) or 'blocks' not in data:
        return False
        
    changed = False
    
    if 'metadata' in data and 'id' in data['metadata']:
        ch_id = data['metadata']['id']
    else:
        ch_id = file_path.split('/')[-1].replace('.json', '')
        if 'metadata' not in data:
            data['metadata'] = {}
        data['metadata']['id'] = ch_id
        changed = True

    for idx, block in enumerate(data['blocks']):
        if not isinstance(block, dict):
            continue
            
        b_type = block.get('type', 'theory')
        
        if 'id' not in block or block['id'] == 'UNKNOWN_ID':
            block['id'] = f"{ch_id.upper()}_{b_type.upper()}_{idx:03d}"
            changed = True
            
        def try_translate_field(key):
            nonlocal changed
            if key in block and f"{key}_hi" not in block:
                print(f"[{ch_id}] Translating {key}...")
                translated = translate_safe(block[key])
                if translated:
                    block[f"{key}_hi"] = translated
                    changed = True

        if b_type in ['theory', 'hook', 'teacher_tip', 'memory_trick', 'common_mistakes', 'real_world_example', 'insight']:
            try_translate_field('title')
            try_translate_field('body')
        elif b_type in ['quiz', 'mcq', 'quiz_multiple_choice']:
            try_translate_field('question')
            try_translate_field('explanation')
            if 'options' in block and 'options_hi' not in block:
                print(f"[{ch_id}] Translating options...")
                opts_hi = []
                for opt in block['options']:
                    tr = translate_safe(opt)
                    if tr:
                        opts_hi.append(tr)
                if len(opts_hi) == len(block['options']):
                    block['options_hi'] = opts_hi
                    changed = True
                
        if 'content' in block and 'content_hi' not in block and isinstance(block['content'], str):
            try_translate_field('content')

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
