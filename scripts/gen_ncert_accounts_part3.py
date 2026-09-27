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
ch203_items = [
    {"type": "hook", "title": "The Report Card of a Business", "body": "Just like a school issues a report card at the end of the year to show how you performed, a company prepares Financial Statements to show how much profit it made and what its financial position is. These are the Balance Sheet and the Statement of Profit & Loss. Investors read this 'report card' before giving their money to the company!"},
    {"type": "socratic", "title": "Think About It...", "body": "Why can't a company just show its bank passbook to prove it's doing well? Why do we need complex Financial Statements?"},
    {"type": "theory", "title": "Schedule III of Companies Act, 2013", "body": "Unlike a sole proprietorship where you can draw a Balance Sheet horizontally (T-shape), companies in India MUST follow a strict vertical format prescribed by Schedule III of the Companies Act, 2013. The Balance Sheet is divided into two main parts: I. Equity and Liabilities, II. Assets."},
    {"type": "theory", "title": "Numerical Illustration: Vertical Balance Sheet", "body": "Let's look at the correct format of a Company's Balance Sheet (extract) under Schedule III."},
    {"type": "markdown_table", "title": "Solution: Balance Sheet Extract", "table_markdown": "| Particulars | Note No. | Current Year (₹) | Previous Year (₹) |\n| :--- | :--- | :--- | :--- |\n| **I. EQUITY AND LIABILITIES** | | | |\n| **1. Shareholders' Funds** | | | |\n| (a) Share Capital | 1 | 5,00,000 | 4,00,000 |\n| (b) Reserves and Surplus | 2 | 1,50,000 | 1,00,000 |\n| **2. Non-Current Liabilities** | | | |\n| (a) Long-term borrowings | | 2,00,000 | 2,00,000 |\n| **Total** | | **8,50,000** | **7,00,000** |"},
    {"type": "mcq", "q": "Which Act prescribes the format of a company's Balance Sheet in India?", "opts": ["Partnership Act 1932", "Income Tax Act 1961", "Companies Act 2013", "Reserve Bank Act 1934"], "ans": 2, "expl": "Schedule III of the Companies Act 2013 prescribes the format."},
    {"type": "mcq", "q": "In a company's Balance Sheet, under which head is 'Reserves and Surplus' shown?", "opts": ["Current Liabilities", "Non-Current Liabilities", "Shareholders' Funds", "Fixed Assets"], "ans": 2, "expl": "Reserves and Surplus belong to the owners, so it is part of Shareholders' Funds."}
]

ch206_items = [
    {"type": "hook", "title": "Where Did the Cash Go?", "body": "You started the year with ₹10,000 in your pocket. You made a profit of ₹50,000. But at the end of the year, your pocket is empty! How is that possible? A Profit & Loss account shows profit, but it doesn't show Cash! You might have used the cash to buy a machine or pay a loan. A Cash Flow Statement tracks the exact movement of cash in and out of the business."},
    {"type": "socratic", "title": "Think About It...", "body": "Is it possible for a company to be highly profitable on paper, but still go bankrupt because it has no cash?"},
    {"type": "theory", "title": "Three Activities of Cash Flow", "body": "AS-3 (Accounting Standard 3) divides cash flows into three activities: 1. Operating (Daily business like selling goods) 2. Investing (Buying/Selling fixed assets) 3. Financing (Issuing shares, taking loans, paying dividends)."},
    {"type": "theory", "title": "Numerical Illustration: Cash Flow Statement", "body": "Net Profit is ₹50,000. Depreciation added back is ₹10,000. Decrease in Debtors is ₹5,000. Increase in Creditors is ₹2,000. Let's calculate Cash Flow from Operating Activities."},
    {"type": "markdown_table", "title": "Solution: Cash Flow from Operating Activities", "table_markdown": "| Particulars | Amount (₹) |\n| :--- | :--- |\n| Net Profit as per P&L | 50,000 |\n| Add: Non-cash expenses (Depreciation) | 10,000 |\n| **Operating Profit before Working Capital Changes** | **60,000** |\n| Add: Decrease in Current Assets (Debtors) | 5,000 |\n| Add: Increase in Current Liabilities (Creditors) | 2,000 |\n| **Cash Generated from Operations** | **67,000** |"},
    {"type": "mcq", "q": "Which Accounting Standard governs the Cash Flow Statement?", "opts": ["AS-1", "AS-2", "AS-3", "AS-4"], "ans": 2, "expl": "AS-3 (Accounting Standard 3) prescribes the preparation of Cash Flow Statements."},
    {"type": "mcq", "q": "Where is 'Dividend Paid' classified in a Cash Flow Statement?", "opts": ["Operating Activities", "Investing Activities", "Financing Activities", "Cash Equivalents"], "ans": 2, "expl": "Paying dividend is related to the financing structure (share capital), so it is a Financing Activity."}
]

if __name__ == "__main__":
    process_chapter("ncert_class12_accounts_leac203", "Accountancy - Financial Statements", ch203_items)
    process_chapter("ncert_class12_accounts_leac206", "Accountancy - Cash Flow Statement", ch206_items)
