import json
import re
import time
from deep_translator import GoogleTranslator

with open('/home/ubuntu/Shine_Academy_Naroda/scratch/gseb_ch10.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

questions = []
current_q = None

for line in lines:
    line = line.strip()
    # skip metadata at the top
    if not line or line.startswith('Shine Academy') or line.startswith('E-06') or line.startswith('10 | English') or line.startswith('Date:'):
        continue
    # Match "1. Who is..."
    m = re.match(r'^(\d+)\.\s+(.*)', line)
    if m:
        if current_q:
            questions.append(current_q)
        current_q = {
            'q_num': int(m.group(1)),
            'question': m.group(2),
            'options_str': ""
        }
    elif current_q and ('[A]' in line or current_q['options_str']):
        # sometimes options span multiple lines
        current_q['options_str'] += line + " "

if current_q:
    questions.append(current_q)

# Now parse options
for q in questions:
    opt_str = q['options_str']
    opts = []
    correct_idx = -1
    
    # regex to find [A] text [B] text etc
    # We can split by [A], [B], [C], [D]
    parts = re.split(r'\[[A-D]\]', opt_str)
    # parts[0] is empty, parts[1] is A, parts[2] is B etc
    for i in range(1, 5):
        if i < len(parts):
            opt_text = parts[i].strip()
            # Match variations of (Correct)
            if re.search(r'\(\s*C\s*o\s*r\s*r\s*e\s*c\s*t\s*\)', opt_text, re.IGNORECASE):
                correct_idx = i - 1
                opt_text = re.sub(r'\(\s*C\s*o\s*r\s*r\s*e\s*c\s*t\s*\)', '', opt_text, flags=re.IGNORECASE).strip()
            opts.append(opt_text)
        else:
            opts.append("")
    
    q['options'] = opts
    q['correct_idx'] = correct_idx if correct_idx != -1 else 0

blocks = []
def add_block(b):
    b['id'] = f"gseb_class10_english_ch10_{len(blocks)+1:03d}"
    blocks.append(b)

# 1. Hook
add_block({
    "type": "theory",
    "title": "1. Hook - A Pampered Pet",
    "body": "Have you ever seen a pet that is treated like a prince, fed rich food until it can barely walk? What happens when love becomes harmful?"
})
# 2. Socratic Question
add_block({
    "type": "socratic_question",
    "title": "2. Socratic Question",
    "body": "If your dog is getting sick from overeating, what is the best way to show your love: giving it more treats or putting it on a strict diet?"
})
# 3. Discovery
add_block({
    "type": "theory",
    "title": "3. Discovery - Tricki's Trouble",
    "body": "Mrs Pumphrey loved her little dog Tricki so much that she overfed him with cakes, chocolates, and wine. Tricki became hugely fat and stopped moving, making her think he was seriously ill."
})
# 4. Reveal
add_block({
    "type": "theory",
    "title": "4. Reveal - The Doctor's Secret",
    "body": "The veterinary surgeon, Mr. Herriot, knew Tricki's only fault was greed. He took the dog to his surgery and gave him no medicine and no extra food—just plenty of water and exercise with other dogs. Within weeks, Tricki was completely transformed!"
})

# 5. Knowledge Check (MCQs)
for i, q in enumerate(questions):
    add_block({
        "type": "mcq",
        "question": q['question'],
        "options": q['options'],
        "correct_index": q['correct_idx'],
        "explanation": "This is the correct answer based on the chapter 'A Triumph of Surgery'."
    })

# 6. Reflection
add_block({
    "type": "reflection",
    "title": "6. Reflection",
    "body": "Think about a time when someone's overindulgence caused problems. How did discipline and a simple routine help fix the situation?"
})
# 7. Connection
add_block({
    "type": "theory",
    "title": "7. Connection",
    "body": "This story connects to health and lifestyle. Just like animals, humans also need a balanced diet and regular exercise to stay healthy and active."
})
# 8. Mastery
add_block({
    "type": "theory",
    "title": "8. Mastery",
    "body": "Write a short diary entry from the perspective of Tricki after returning home from the surgery, describing how he feels now compared to before."
})

# Translate
translator_hi = GoogleTranslator(source='en', target='hi')
translator_gu = GoogleTranslator(source='en', target='gu')

def trans(text, lang, retries=3):
    if not text: return text
    for _ in range(retries):
        try:
            if lang == 'hi':
                return translator_hi.translate(text)
            else:
                return translator_gu.translate(text)
        except Exception as e:
            time.sleep(1)
    return text

print("Translating blocks...")
for i, b in enumerate(blocks):
    print(f"Translating block {i+1}/{len(blocks)}")
    if 'title' in b:
        b['title_hi'] = trans(b['title'], 'hi')
        b['title_gu'] = trans(b['title'], 'gu')
    if 'body' in b:
        b['body_hi'] = trans(b['body'], 'hi')
        b['body_gu'] = trans(b['body'], 'gu')
    if 'question' in b:
        b['question_hi'] = trans(b['question'], 'hi')
        b['question_gu'] = trans(b['question'], 'gu')
    if 'options' in b:
        b['options_hi'] = [trans(o, 'hi') for o in b['options']]
        b['options_gu'] = [trans(o, 'gu') for o in b['options']]
    if 'explanation' in b:
        b['explanation_hi'] = trans(b['explanation'], 'hi')
        b['explanation_gu'] = trans(b['explanation'], 'gu')

chapter = {
    "id": "gseb_class10_english_ch10",
    "title": "A Triumph of Surgery",
    "title_hi": trans("A Triumph of Surgery", 'hi'),
    "title_gu": trans("A Triumph of Surgery", 'gu'),
    "subject": "English",
    "grade": "10",
    "board": "GSEB",
    "blocks": blocks
}

out_file = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch10.json'
with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(chapter, f, ensure_ascii=False, indent=2)

print("Done! Saved to", out_file)
