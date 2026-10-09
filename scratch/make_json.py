import json
import urllib.request
import urllib.parse
import re
import os
import time

def translate(text, to_lang):
    if not text: return ""
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={to_lang}&dt=t&q={urllib.parse.quote(text)}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))
        return "".join([d[0] for d in data[0]])
    except Exception as e:
        print(f"Translation failed for {text}: {e}")
        return text + f" [{to_lang}]"

def parse_txt():
    with open('scratch/gseb_ch10.txt', 'r', encoding='utf-8') as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]

    mcqs = []
    current_q = None
    options = []
    
    for line in lines:
        if re.match(r'^\d+\.\s+', line):
            if current_q:
                mcqs.append((current_q, options))
            current_q = re.sub(r'^\d+\.\s+', '', line)
            options = []
        elif line.startswith('[A]'):
            opts = re.findall(r'\[([A-D])\]\s([^\[]+)', line)
            if not opts:
                opts = []
                # Fallback splitting
                parts = re.split(r'\[[A-D]\]\s', line)
                if len(parts) > 1:
                    for i, p in enumerate(parts[1:]):
                        opts.append((chr(65+i), p.strip()))
            for letter, opt_text in opts:
                options.append(opt_text.strip())
        elif options and len(options) < 4 and line.startswith('('):
            # Continued line
            options[-1] += ' ' + line
        elif options and len(options) < 4 and not line.startswith('['):
            options[-1] += ' ' + line

    if current_q:
        mcqs.append((current_q, options))
    
    return mcqs

def build_json():
    mcqs_data = parse_txt()
    
    blocks = []
    
    # 8-step arc theory blocks
    theory = [
        {
            "id": "gseb_class10_english_ch10_hook_01",
            "type": "theory",
            "title": "The Mystery of Tricki",
            "body": "Have you ever seen a dog so fat it looks like a bloated sausage with legs? Let's dive into the story of Tricki!"
        },
        {
            "id": "gseb_class10_english_ch10_socratic_01",
            "type": "socratic_question",
            "title": "Think About It",
            "body": "Why would an owner overfeed their pet even when it's harmful? Is it out of love or ignorance?"
        },
        {
            "id": "gseb_class10_english_ch10_discovery_01",
            "type": "theory",
            "title": "Exploring the Problem",
            "body": "Mrs. Pumphrey loved Tricki too much. She fed him cakes, chocolates, and wine. Tricki became extremely lazy and sick. Dr. Herriot knew the only cure was to cut his food and make him exercise."
        },
        {
            "id": "gseb_class10_english_ch10_reveal_01",
            "type": "definition",
            "title": "A Triumph of Surgery",
            "body": "The 'surgery' here is not an operation. It's the veterinary hospital where Dr. Herriot treated Tricki with just water and strict diet, saving his life."
        }
    ]
    
    for t in theory:
        t["title_hi"] = translate(t["title"], "hi")
        t["body_hi"] = translate(t["body"], "hi")
        t["title_gu"] = translate(t["title"], "gu")
        t["body_gu"] = translate(t["body"], "gu")
        blocks.append(t)
        time.sleep(0.5)

    # MCQs
    for i, (q, opts) in enumerate(mcqs_data):
        correct_index = 0
        clean_opts = []
        for j, opt in enumerate(opts):
            if '(Correct)' in opt or '(Co rrect)' in opt or '(Correc t)' in opt:
                correct_index = j
            clean_opts.append(re.sub(r'\s*\(Corr?ec\s*t\)\s*', '', opt, flags=re.IGNORECASE).strip())
        
        while len(clean_opts) < 4:
            clean_opts.append("Option")
            
        block = {
            "id": f"gseb_class10_english_ch10_mcq_{i+1:02d}",
            "type": "mcq",
            "question": q,
            "question_hi": translate(q, "hi"),
            "question_gu": translate(q, "gu"),
            "options": clean_opts,
            "options_hi": [translate(o, "hi") for o in clean_opts],
            "options_gu": [translate(o, "gu") for o in clean_opts],
            "correct_index": correct_index,
            "explanation": "Correct answer from the text.",
            "explanation_hi": translate("Correct answer from the text.", "hi"),
            "explanation_gu": translate("Correct answer from the text.", "gu")
        }
        blocks.append(block)
        print(f"Processed MCQ {i+1}/{len(mcqs_data)}")
        time.sleep(0.5)
        
    chapter_json = {
        "id": "GSEB_CLASS10_ENG_CH10",
        "title": "A Triumph of Surgery",
        "subtitle": "Chapter 10",
        "subject": "English",
        "grade": 10,
        "board": "GSEB",
        "blocks": blocks
    }
    
    os.makedirs('app_core/chapters', exist_ok=True)
    with open('app_core/chapters/gseb_class10_english_ch10.json', 'w', encoding='utf-8') as f:
        json.dump(chapter_json, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    build_json()
