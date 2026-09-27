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
ch202_items = [
    {"type": "hook", "title": "The Grand Loan", "body": "What if a company wants ₹50 Crores, but doesn't want to make people owners (shareholders)? They can ask the public for a loan! They issue a certificate called a 'Debenture' promising to pay regular interest and return the money after a few years. Unlike shareholders, debenture holders are lenders, not owners!"},
    {"type": "socratic", "title": "Think About It...", "body": "If the company goes bankrupt and shuts down, who gets paid first from the remaining money: the Shareholders or the Debenture holders?"},
    {"type": "theory", "title": "Issue of Debentures at Discount", "body": "A company can issue debentures at a Discount (e.g. asking for ₹95 but promising to pay back ₹100). The ₹5 difference is a Loss on Issue of Debentures. Note: A company cannot issue *shares* at a discount, but it *can* issue debentures at a discount!"},
    {"type": "theory", "title": "Numerical Illustration: Debentures", "body": "Y Ltd. issued 5,000, 9% Debentures of ₹100 each at a discount of 5%. The full amount was payable on application. Let's pass the journal entries."},
    {"type": "markdown_table", "title": "Solution: Journal Entries for Debentures", "table_markdown": "| Date | Particulars | L.F. | Debit (₹) | Credit (₹) |\n| :--- | :--- | :--- | :--- | :--- |\n| 1 | Bank A/c ... Dr. | | 4,75,000 | |\n| | To Debenture Application & Allotment A/c | | | 4,75,000 |\n| | *(Received application money: 5000 x 95)* | | | |\n| 2 | Debenture App & Allotment A/c ... Dr. | | 4,75,000 | |\n| | Discount on Issue of Debentures A/c ... Dr. | | 25,000 | |\n| | To 9% Debentures A/c | | | 5,00,000 |\n| | *(Debentures issued at 5% discount)* | | | |"},
    {"type": "mcq", "q": "Debenture holders are:", "opts": ["Owners of the company", "Creditors of the company", "Customers of the company", "Directors of the company"], "ans": 1, "expl": "Debenture holders lend money to the company, so they are its creditors."},
    {"type": "mcq", "q": "Can debentures be issued at a discount?", "opts": ["Yes", "No", "Only with RBI permission", "Only for Rs. 10"], "ans": 0, "expl": "Yes, while shares cannot be issued at a discount, debentures can be."}
]

ch205_items = [
    {"type": "hook", "title": "The Pulse of the Business", "body": "A doctor checks your pulse and blood pressure to know if you are healthy. A financial analyst checks 'Accounting Ratios' to know if a business is healthy! If a company has ₹1 Lakh in cash but owes ₹10 Lakhs tomorrow, it's sick. The Current Ratio helps diagnose this!"},
    {"type": "socratic", "title": "Think About It...", "body": "Is having a massive amount of inventory (unsold stock) always a sign of a strong business? How does it affect liquidity?"},
    {"type": "theory", "title": "Liquidity Ratios", "body": "Liquidity ratios measure the firm's ability to pay its short-term debts. \n1. Current Ratio = Current Assets / Current Liabilities. Ideal ratio is 2:1.\n2. Quick Ratio (Liquid Ratio) = Quick Assets / Current Liabilities. Ideal is 1:1. Quick Assets = Current Assets - Inventory - Prepaid Expenses."},
    {"type": "theory", "title": "Numerical Illustration: Current Ratio", "body": "A company has Current Assets of ₹4,00,000 and Current Liabilities of ₹2,00,000. Inventory is ₹1,00,000. Let's calculate Current Ratio and Quick Ratio."},
    {"type": "markdown_table", "title": "Solution: Ratio Calculations", "table_markdown": "| Ratio | Formula | Calculation | Result |\n| :--- | :--- | :--- | :--- |\n| **Current Ratio** | Current Assets / Current Liabilities | 4,00,000 / 2,00,000 | **2:1** |\n| **Quick Assets** | Current Assets - Inventory | 4,00,000 - 1,00,000 | **3,00,000** |\n| **Quick Ratio** | Quick Assets / Current Liabilities | 3,00,000 / 2,00,000 | **1.5:1** |"},
    {"type": "mcq", "q": "What is the ideal Current Ratio?", "opts": ["1:1", "2:1", "1:2", "3:1"], "ans": 1, "expl": "An ideal current ratio is 2:1, meaning you have twice as many assets to pay your short-term liabilities."},
    {"type": "mcq", "q": "Which of the following is NOT included in Quick Assets?", "opts": ["Cash", "Debtors", "Inventory", "Marketable Securities"], "ans": 2, "expl": "Inventory (stock) takes time to sell, so it is not a 'quick' asset."}
]

if __name__ == "__main__":
    process_chapter("ncert_class12_accounts_leac202", "Accountancy - Issue of Debentures", ch202_items)
    process_chapter("ncert_class12_accounts_leac205", "Accountancy - Accounting Ratios", ch205_items)
