import json
import time
from deep_translator import GoogleTranslator

file_path = 'ncert_class10_maths_ch1.json'

translator = GoogleTranslator(source='en', target='gu')

def translate_to_gu(text):
    if not text:
        return text
    try:
        time.sleep(0.5) # Avoid rate limits
        return translator.translate(text)
    except Exception as e:
        print(f"Translation failed for '{text[:20]}...': {e}")
        return text

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for block in data.get('blocks', []):
    if 'question' in block and 'question_gu' not in block:
        block['question_gu'] = translate_to_gu(block['question'])
        count += 1
        
    if 'options' in block and 'options_gu' not in block:
        block['options_gu'] = [translate_to_gu(opt) for opt in block['options']]
        count += 1
        
    if 'explanation' in block and 'explanation_gu' not in block:
        block['explanation_gu'] = translate_to_gu(block['explanation'])
        count += 1
    elif 'explanation_en' in block and 'explanation_gu' not in block:
        block['explanation_gu'] = translate_to_gu(block['explanation_en'])
        count += 1
        
    if 'title' in block and 'title_gu' not in block:
        block['title_gu'] = translate_to_gu(block['title'])
        count += 1
        
    if count > 50: # save periodically
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        count = 0

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Translation completed and saved.")
