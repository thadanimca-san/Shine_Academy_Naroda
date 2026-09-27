import json
import time
from googletrans import Translator

translator = Translator()

def safe_translate(text, dest_lang):
    if not text or not isinstance(text, str) or not text.strip():
        return text
    try:
        res = translator.translate(text, src='en', dest=dest_lang)
        time.sleep(0.5)
        return res.text
    except Exception as e:
        print(f"Failed to translate: {text[:20]}... Error: {e}")
        return text

file_path = 'app_core/chapters/ncert_class10_maths_ch1.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

modified = False
for idx, block in enumerate(data.get('blocks', [])):
    # Explanations
    if 'explanation' in block and block['explanation']:
        if 'explanation_gu' not in block:
            print(f"Translating explanation for block {idx}")
            block['explanation_gu'] = safe_translate(block['explanation'], 'gu')
            modified = True
            
    # Options (list of strings)
    if 'options' in block and isinstance(block['options'], list):
        if 'options_gu' not in block or len(block['options_gu']) != len(block['options']):
            print(f"Translating options for block {idx}")
            opts_gu = []
            for opt in block['options']:
                if isinstance(opt, str):
                    opts_gu.append(safe_translate(opt, 'gu'))
                else:
                    opts_gu.append(opt) # fallback if dict
            block['options_gu'] = opts_gu
            modified = True

if modified:
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved: {file_path}")
else:
    print("No missing options/explanations found.")
