import json
import re

filepath = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch9.json'
with open(filepath, 'r') as f:
    data = json.load(f)

blocks = data.get('blocks', [])

# Fix socratic blocks (1, 4, 7)
socratic_titles = {
    1: {"en": "Knowledge Check: Refraction", "hi": "ज्ञान की जांच: अपवर्तन", "gu": "જ્ઞાનની ચકાસણી: વક્રીભવન"},
    4: {"en": "Knowledge Check: Mirror Formula", "hi": "ज्ञान की जांच: दर्पण सूत्र", "gu": "જ્ઞાનની ચકાસણી: અરીસાનું સૂત્ર"},
    7: {"en": "Knowledge Check: Lens Power", "hi": "ज्ञान की जांच: लेंस की क्षमता", "gu": "જ્ઞાનની ચકાસણી: લેન્સનો પાવર"}
}
for idx, titles in socratic_titles.items():
    if idx < len(blocks):
        blocks[idx]['title'] = titles['en']
        blocks[idx]['title_hi'] = titles['hi']
        blocks[idx]['title_gu'] = titles['gu']

# Fix MCQ blocks (8 to 24)
for i in range(8, len(blocks)):
    b = blocks[i]
    q_num = i - 7
    
    # Set titles
    b['title'] = f"NCERT Exercise Q{q_num}"
    b['title_hi'] = f"NCERT अभ्यास Q{q_num}"
    b['title_gu'] = f"NCERT સ્વાધ્યાય Q{q_num}"
    
    # Remove prefix like "NCERT Ex 1: " or "NCERT प्रश्न 1: " or "NCERT પ્રશ્ન 1: "
    if 'question' in b:
        b['question'] = re.sub(r'^NCERT Ex \d+:\s*', '', b['question'])
    if 'question_hi' in b:
        b['question_hi'] = re.sub(r'^NCERT प्रश्न \d+:\s*', '', b['question_hi'])
    if 'question_gu' in b:
        b['question_gu'] = re.sub(r'^NCERT પ્રશ્ન \d+:\s*', '', b['question_gu'])

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Fixed chapter 9 JSON!")
