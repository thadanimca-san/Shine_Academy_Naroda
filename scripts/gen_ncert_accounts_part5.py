import os
import json
import time
from googletrans import Translator

CHAPTERS_DIR = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
translator = Translator()

def translate_safe(text, dest_lang):
    if not text: return ""
    for attempt in range(5):
        try:
            res = translator.translate(text, dest=dest_lang)
            time.sleep(0.1)
            return res.text
        except Exception as e:
            print(f"Translation failed for '{text[:20]}...' to {dest_lang}. Retrying {attempt+1}...")
            time.sleep(2)
    return text + f" ({dest_lang})"

def build_hook(idx, title, body):
    return {
        "id": idx, "type": "hook",
        "title": title, "title_hi": translate_safe(title, 'hi'), "title_gu": translate_safe(title, 'gu'),
        "body": body, "body_hi": translate_safe(body, 'hi'), "body_gu": translate_safe(body, 'gu')
    }

def build_socratic_as_theory(idx, title, body):
    return build_theory(idx, title, body)

def build_theory(idx, title, body):
    return {
        "id": idx, "type": "theory",
        "title": title, "title_hi": translate_safe(title, 'hi'), "title_gu": translate_safe(title, 'gu'),
        "body": body, "body_hi": translate_safe(body, 'hi'), "body_gu": translate_safe(body, 'gu')
    }

def build_markdown_table(idx, title, table_md):
    return {
        "id": idx, "type": "markdown_table",
        "title": title, "title_hi": translate_safe(title, 'hi'), "title_gu": translate_safe(title, 'gu'),
        "table_markdown": table_md
    }

def build_mcq(idx, q, opts, ans, expl):
    return {
        "id": idx, "type": "mcq",
        "question": q, "question_hi": translate_safe(q, 'hi'), "question_gu": translate_safe(q, 'gu'),
        "options": opts, "options_hi": [translate_safe(o, 'hi') for o in opts], "options_gu": [translate_safe(o, 'gu') for o in opts],
        "correct_index": ans, "explanation": expl, "explanation_hi": translate_safe(expl, 'hi'), "explanation_gu": translate_safe(expl, 'gu')
    }

def process_chapter(ch_id, title, items):
    file_path = os.path.join(CHAPTERS_DIR, f"{ch_id}.json")
    blocks = []
    for i, item in enumerate(items):
        t = item['type']
        idx = f"KOBJ_{ch_id}_{t.upper()}_{i+1}"
        if t == 'hook': blocks.append(build_hook(idx, item['title'], item['body']))
        elif t == 'theory': blocks.append(build_theory(idx, item['title'], item['body']))
        elif t == 'socratic': blocks.append(build_socratic_as_theory(idx, item['title'], item['body']))
        elif t == 'markdown_table': blocks.append(build_markdown_table(idx, item['title'], item['table_markdown']))
        elif t == 'mcq': blocks.append(build_mcq(idx, item['q'], item['opts'], item['ans'], item['expl']))

    full_json = {
        "metadata": {"id": ch_id, "title": title, "subject": "Accountancy", "grade": "12", "curriculum": ["NCERT", "CBSE"]},
        "blocks": blocks
    }
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(full_json, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Generated {file_path}")

# --- DATA ---
ch204_items = [
    {"type": "hook", "title": "Detectives of the Numbers", "body": "Looking at a Balance Sheet is like looking at a fingerprint. To the untrained eye, it's just a bunch of numbers. But a financial detective (analyst) can analyze it to find out if the company is growing, stagnating, or about to collapse! We use tools like Comparative Statements and Common-Size Statements to solve the mystery."},
    {"type": "socratic", "title": "Think About It...", "body": "If Profit increased from ₹1 Lakh to ₹2 Lakhs, is it definitely a good thing? What if Sales increased from ₹10 Lakhs to ₹100 Lakhs in the same period?"},
    {"type": "theory", "title": "Comparative Statements", "body": "A Comparative Statement places the financial data of two or more years side-by-side to calculate the Absolute Change (Current Year - Previous Year) and the Percentage Change. This helps in identifying trends over time."},
    {"type": "theory", "title": "Numerical Illustration: Comparative Balance Sheet", "body": "Share Capital in 2022 was ₹5,00,000. In 2023, it is ₹6,00,000. Let's calculate the Absolute Change and Percentage Change."},
    {"type": "markdown_table", "title": "Solution: Comparative Analysis", "table_markdown": "| Particulars | 2022 (₹) | 2023 (₹) | Absolute Change (₹) | % Change |\n| :--- | :--- | :--- | :--- | :--- |\n| Share Capital | 5,00,000 | 6,00,000 | 1,00,000 | (1,00,000 / 5,00,000) * 100 = **20%** |"},
    {"type": "mcq", "q": "What does a Comparative Statement analyze?", "opts": ["Data of a single year", "Trends over two or more years", "Only the Cash Flow", "Only the Tax amount"], "ans": 1, "expl": "Comparative statements compare data over multiple years to identify trends."},
    {"type": "mcq", "q": "If previous year value is ₹4,00,000 and current year value is ₹5,00,000, what is the Percentage Change?", "opts": ["25%", "20%", "50%", "10%"], "ans": 0, "expl": "Absolute change is 1,00,000. (1,00,000 / 4,00,000) * 100 = 25%."}
]

if __name__ == "__main__":
    process_chapter("ncert_class12_accounts_leac204", "Accountancy - Analysis of Financial Statements", ch204_items)
