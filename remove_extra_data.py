import json
import os
import glob
import re

directory = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/'
pattern_en = re.compile(r'^(NCERT\s*(Ex|Exercise|Q|Question)[\w\s]*:|Q\d+:)\s*', re.IGNORECASE)
pattern_hi = re.compile(r'^(NCERT\s*प्रश्न[\w\s]*:|प्रश्न\s*\d+:)\s*', re.IGNORECASE)
pattern_gu = re.compile(r'^(NCERT\s*પ્રશ્ન[\w\s]*:|પ્રશ્ન\s*\d+:)\s*', re.IGNORECASE)

files = glob.glob(os.path.join(directory, '*.json'))

fixed_count = 0
for filepath in files:
    with open(filepath, 'r') as f:
        data = json.load(f)
        
    if isinstance(data, list):
        blocks = data
    elif isinstance(data, dict):
        blocks = data.get('blocks', [])
    else:
        continue
        
    changed = False
    for b in blocks:
        if 'question' in b and b['question'] and isinstance(b['question'], str):
            if pattern_en.search(b['question']):
                b['question'] = pattern_en.sub('', b['question']).strip()
                changed = True
        if 'question_hi' in b and b['question_hi'] and isinstance(b['question_hi'], str):
            if pattern_hi.search(b['question_hi']):
                b['question_hi'] = pattern_hi.sub('', b['question_hi']).strip()
                changed = True
        if 'question_gu' in b and b['question_gu'] and isinstance(b['question_gu'], str):
            if pattern_gu.search(b['question_gu']):
                b['question_gu'] = pattern_gu.sub('', b['question_gu']).strip()
                changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Fixed extra data in {os.path.basename(filepath)}")
        fixed_count += 1

print(f"Total files fixed: {fixed_count}")
