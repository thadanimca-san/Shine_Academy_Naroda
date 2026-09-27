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
ch104_items = [
    {"type": "hook", "title": "Closing the Doors", "body": "What happens when a business completely shuts down? It's not as simple as locking the front door. You have to sell every chair, every computer, and every machine. Then you use that money to pay off all your loans and creditors. Whatever is left over is finally given back to the owners. This process of selling assets and paying liabilities to close the firm is called Dissolution."},
    {"type": "socratic", "title": "Think About It...", "body": "If you sell an asset for more than its book value during dissolution, do you record the profit in the Revaluation Account or somewhere else? Why is Revaluation no longer useful?"},
    {"type": "theory", "title": "Realisation Account", "body": "On dissolution, we do NOT open a Revaluation Account because the firm is not continuing. Instead, we open a 'Realisation Account'. We transfer all assets (except cash/bank) to its debit side, and all outside liabilities to its credit side. Then we record the actual cash received from selling assets and cash paid to settle liabilities."},
    {"type": "theory", "title": "Numerical Illustration: Realisation", "body": "A and B dissolve their firm. Total Sundry Assets are ₹1,00,000. Sundry Creditors are ₹30,000. The assets realized (sold for) ₹80,000. Creditors were paid in full. Let's prepare the Realisation Account."},
    {"type": "markdown_table", "title": "Solution: Realisation Account", "table_markdown": "| Particulars (Dr.) | Amount (₹) | Particulars (Cr.) | Amount (₹) |\n| :--- | :--- | :--- | :--- |\n| To Sundry Assets A/c (Transfer) | 1,00,000 | By Sundry Creditors A/c (Transfer) | 30,000 |\n| To Cash/Bank A/c (Creditors paid) | 30,000 | By Cash/Bank A/c (Assets realized) | 80,000 |\n| | | By Loss transferred to Capital A/cs: | |\n| | | A : 10,000 | |\n| | | B : 10,000 | 20,000 |\n| **Total** | **1,30,000** | **Total** | **1,30,000** |"},
    {"type": "mcq", "q": "Which account is prepared on the dissolution of a firm?", "opts": ["Revaluation Account", "Realisation Account", "Profit and Loss Adjustment Account", "Suspense Account"], "ans": 1, "expl": "Realisation account is prepared to calculate the final profit/loss on closing the books."},
    {"type": "mcq", "q": "Are Cash and Bank balances transferred to the Realisation Account?", "opts": ["Yes, always", "No, they are already realized", "Only if they are negative", "Only if partners agree"], "ans": 1, "expl": "Cash and bank are already in liquid form, so they are not transferred to Realisation."}
]

ch201_items = [
    {"type": "hook", "title": "Slicing the Giant Cake", "body": "Imagine a company needs ₹100 Crores to build a factory. No single person has that much money! So, the company divides this huge amount into 1 Crore tiny 'slices' of ₹100 each. These slices are called 'Shares'. Anyone who buys a share becomes a part-owner of the company. This is the magic of Share Capital!"},
    {"type": "socratic", "title": "Think About It...", "body": "If you buy a share for ₹100, do you have to pay the full ₹100 immediately, or can the company ask for it in installments?"},
    {"type": "theory", "title": "Issue of Shares in Installments", "body": "Companies often collect the share money in installments: 1. Application Money (Paid when applying) 2. Allotment Money (Paid when shares are given) 3. Call Money (First Call, Second Call, etc. when needed)."},
    {"type": "theory", "title": "Numerical Illustration: Issue of Shares", "body": "X Ltd. issued 10,000 shares of ₹10 each payable as: ₹3 on Application, ₹4 on Allotment, and ₹3 on First & Final Call. All money was duly received. Let's pass the journal entries."},
    {"type": "markdown_table", "title": "Solution: Journal Entries in the books of X Ltd.", "table_markdown": "| Date | Particulars | L.F. | Debit (₹) | Credit (₹) |\n| :--- | :--- | :--- | :--- | :--- |\n| 1 | Bank A/c ... Dr. | | 30,000 | |\n| | To Share Application A/c | | | 30,000 |\n| | *(Received application money 10,000 x 3)* | | | |\n| 2 | Share Application A/c ... Dr. | | 30,000 | |\n| | To Share Capital A/c | | | 30,000 |\n| | *(Transferred to Capital)* | | | |\n| 3 | Share Allotment A/c ... Dr. | | 40,000 | |\n| | To Share Capital A/c | | | 40,000 |\n| | *(Allotment due 10,000 x 4)* | | | |\n| 4 | Bank A/c ... Dr. | | 40,000 | |\n| | To Share Allotment A/c | | | 40,000 |\n| | *(Received allotment money)* | | | |\n| 5 | Share First & Final Call A/c ... Dr. | | 30,000 | |\n| | To Share Capital A/c | | | 30,000 |\n| | *(Call money due)* | | | |\n| 6 | Bank A/c ... Dr. | | 30,000 | |\n| | To Share First & Final Call A/c | | | 30,000 |\n| | *(Received call money)* | | | |"},
    {"type": "mcq", "q": "What is the first installment of share capital called?", "opts": ["Allotment", "Application", "First Call", "Premium"], "ans": 1, "expl": "The first installment paid by the public to buy shares is the Application money."},
    {"type": "mcq", "q": "Where is the Application money transferred after allotment?", "opts": ["Bank Account", "Profit & Loss Account", "Share Capital Account", "Reserve Capital"], "ans": 2, "expl": "Once shares are allotted, the application money becomes part of the company's Share Capital."}
]

if __name__ == "__main__":
    process_chapter("ncert_class12_accounts_leac104", "Accountancy - Dissolution of Partnership", ch104_items)
    process_chapter("ncert_class12_accounts_leac201", "Accountancy - Share Capital", ch201_items)
