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
    print(f"Translating Hook {idx}...")
    return {
        "id": idx, "type": "hook",
        "title": title, "title_hi": translate_safe(title, 'hi'), "title_gu": translate_safe(title, 'gu'),
        "body": body, "body_hi": translate_safe(body, 'hi'), "body_gu": translate_safe(body, 'gu')
    }

def build_socratic(idx, title, body):
    print(f"Translating Socratic {idx}...")
    return {
        "id": idx, "type": "socratic_question",
        "question": body, "question_hi": translate_safe(body, 'hi'), "question_gu": translate_safe(body, 'gu'),
        "options": ["Option 1", "Option 2"], "options_hi": ["Option 1", "Option 2"], "options_gu": ["Option 1", "Option 2"],
        "correct_index": 0, "explanation": "Wait", "explanation_hi": "Wait", "explanation_gu": "Wait"
    } # Note: In actual implementation, we'll use a real socratic block without options if it's just a thought, but let's just use theory with a question format.
    
# Let's adjust socratic to just use 'theory' type with a socratic style title to prevent any parsing issues with missing options.
def build_socratic_as_theory(idx, title, body):
    print(f"Translating Socratic Theory {idx}...")
    return build_theory(idx, title, body)

def build_theory(idx, title, body):
    print(f"Translating Theory {idx}...")
    return {
        "id": idx, "type": "theory",
        "title": title, "title_hi": translate_safe(title, 'hi'), "title_gu": translate_safe(title, 'gu'),
        "body": body, "body_hi": translate_safe(body, 'hi'), "body_gu": translate_safe(body, 'gu')
    }

def build_markdown_table(idx, title, table_md):
    print(f"Translating Markdown Table {idx}...")
    return {
        "id": idx, "type": "markdown_table",
        "title": title, "title_hi": translate_safe(title, 'hi'), "title_gu": translate_safe(title, 'gu'),
        "table_markdown": table_md
    }

def build_mcq(idx, q, opts, ans, expl):
    print(f"Translating MCQ {idx}...")
    q_hi = translate_safe(q, 'hi')
    q_gu = translate_safe(q, 'gu')
    opts_hi = [translate_safe(opt, 'hi') for opt in opts]
    opts_gu = [translate_safe(opt, 'gu') for opt in opts]
    expl_hi = translate_safe(expl, 'hi')
    expl_gu = translate_safe(expl, 'gu')
    return {
        "id": idx, "type": "mcq",
        "question": q, "question_hi": q_hi, "question_gu": q_gu,
        "options": opts, "options_hi": opts_hi, "options_gu": opts_gu,
        "correct_index": ans, "explanation": expl, "explanation_hi": expl_hi, "explanation_gu": expl_gu
    }

def process_chapter(ch_id, title, items):
    file_path = os.path.join(CHAPTERS_DIR, f"{ch_id}.json")
    blocks = []
    
    for i, item in enumerate(items):
        t = item['type']
        idx = f"KOBJ_{ch_id}_{t.upper()}_{i+1}"
        if t == 'hook':
            blocks.append(build_hook(idx, item['title'], item['body']))
        elif t == 'theory':
            blocks.append(build_theory(idx, item['title'], item['body']))
        elif t == 'socratic':
            blocks.append(build_socratic_as_theory(idx, item['title'], item['body']))
        elif t == 'markdown_table':
            blocks.append(build_markdown_table(idx, item['title'], item['table_markdown']))
        elif t == 'mcq':
            blocks.append(build_mcq(idx, item['q'], item['opts'], item['ans'], item['expl']))

    full_json = {
        "metadata": {
            "id": ch_id,
            "title": title,
            "subject": "Accountancy",
            "grade": "12",
            "curriculum": ["NCERT", "CBSE"]
        },
        "blocks": blocks
    }
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(full_json, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Generated {file_path}")

# --- DATA ---

ch101_items = [
    {"type": "hook", "title": "The Business Marriage", "body": "Imagine you want to start a massive restaurant, but you only have half the money and you don't know how to cook. You find a friend who has the other half of the money and is a master chef. You join hands to run the business together. This 'joining of hands' to share capital, skills, and profits is called a Partnership! Let's explore how we record this business marriage in accounting."},
    {"type": "socratic", "title": "Think About It...", "body": "If you and your friend start a partnership without writing down the rules, what happens if your friend later demands a salary for cooking? How does accounting solve this?"},
    {"type": "theory", "title": "Partnership Deed", "body": "A Partnership Deed is a written agreement containing the terms of partnership. If there is no written deed, the Indian Partnership Act, 1932 applies: 1. Profits are shared equally. 2. No interest on capital. 3. No salary to partners. 4. 6% p.a. interest on partner's loan to the firm."},
    {"type": "theory", "title": "Profit and Loss Appropriation Account", "body": "In a sole proprietorship, all net profit goes to the single owner. In a partnership, the net profit from the P&L Account is transferred to a special account called 'Profit and Loss Appropriation Account'. Here, the profit is distributed among partners in the form of interest on capital, salary, commission, and finally, share of profit."},
    {"type": "theory", "title": "Numerical Illustration: P&L Appropriation", "body": "A and B started a partnership on 1st April 2023 with capitals of ₹1,00,000 and ₹60,000 respectively. According to the deed: (a) Interest on Capital is 10% p.a. (b) B gets a salary of ₹3,000 per month. (c) Profits are shared in 3:2. The firm earned a net profit of ₹80,000 for the year. Let's prepare the P&L Appropriation Account."},
    {"type": "markdown_table", "title": "Solution: P&L Appropriation Account for the year ended 31st March 2024", "table_markdown": "| Particulars (Dr.) | Amount (₹) | Particulars (Cr.) | Amount (₹) |\n| :--- | :--- | :--- | :--- |\n| **To Interest on Capital:** | | **By Profit & Loss A/c (Net Profit)** | 80,000 |\n| A (10% of 1,00,000) : 10,000 | | | |\n| B (10% of 60,000) : 6,000 | 16,000 | | |\n| **To B's Salary** (3,000 x 12) | 36,000 | | |\n| **To Profit transferred to Cap A/cs:** | | | |\n| A (3/5 of 28,000) : 16,800 | | | |\n| B (2/5 of 28,000) : 11,200 | 28,000 | | |\n| **Total** | **80,000** | **Total** | **80,000** |"},
    {"type": "mcq", "q": "In the absence of a Partnership Deed, how are profits shared?", "opts": ["In capital ratio", "Equally", "Given to the senior partner", "Based on time devoted"], "ans": 1, "expl": "According to the Indian Partnership Act 1932, profits are shared equally in the absence of a deed."},
    {"type": "mcq", "q": "Where is partner's salary recorded?", "opts": ["Trading Account", "Profit & Loss Account", "Profit & Loss Appropriation Account", "Balance Sheet directly"], "ans": 2, "expl": "Partner's salary is an appropriation of profit, hence recorded in the P&L Appropriation Account."}
]

ch103_items = [
    {"type": "hook", "title": "When a Player Leaves the Game", "body": "Imagine a 3-player relay race team. Suddenly, one player decides to retire or sadly passes away. The remaining two players must now cover the entire track themselves. They 'gain' the portion of the track the retiring player used to run. In a partnership, when a partner retires, the continuing partners 'gain' their profit share, and the retiring partner must be paid out their fair share of capital and goodwill."},
    {"type": "socratic", "title": "Think About It...", "body": "If a partner retires after 20 years of building the firm's reputation, shouldn't they be compensated for the firm's brand value (goodwill) they helped create?"},
    {"type": "theory", "title": "Gaining Ratio & Goodwill", "body": "Gaining Ratio = New Ratio - Old Ratio. The retiring partner is entitled to their share of goodwill, which is contributed by the continuing partners in their gaining ratio. Entry: Gaining Partners' Capital A/c Dr. To Retiring Partner's Capital A/c."},
    {"type": "theory", "title": "Numerical Illustration: Retirement", "body": "X, Y, and Z are partners sharing profits in 3:2:1. Y retires. Goodwill of the firm is valued at ₹60,000. X and Z decide to share future profits equally (1:1). Let's calculate the gaining ratio and pass the journal entry for goodwill."},
    {"type": "markdown_table", "title": "Solution: Gaining Ratio Calculation", "table_markdown": "| Partner | New Share | Old Share | Gain (New - Old) |\n| :--- | :--- | :--- | :--- |\n| X | 1/2 (or 3/6) | 3/6 | 3/6 - 3/6 = 0 (No Gain) |\n| Z | 1/2 (or 3/6) | 1/6 | 3/6 - 1/6 = 2/6 (Gain) |"},
    {"type": "theory", "title": "Analysis of Goodwill", "body": "Y's share of goodwill = 2/6 of 60,000 = ₹20,000. Since only Z is gaining, Z alone will compensate Y."},
    {"type": "markdown_table", "title": "Solution: Journal Entry", "table_markdown": "| Date | Particulars | L.F. | Debit (₹) | Credit (₹) |\n| :--- | :--- | :--- | :--- | :--- |\n| | Z's Capital A/c ... Dr. | | 20,000 | |\n| | To Y's Capital A/c | | | 20,000 |\n| | *(Being Y's share of goodwill adjusted through Z's capital)* | | | |"},
    {"type": "mcq", "q": "What is the formula for Gaining Ratio?", "opts": ["Old Ratio - New Ratio", "New Ratio - Old Ratio", "Sacrificing Ratio - Old Ratio", "New Ratio + Old Ratio"], "ans": 1, "expl": "Gaining Ratio is calculated by subtracting the old share from the new share."},
    {"q": "How is the retiring partner's share of goodwill treated?", "opts": ["Paid in cash by the firm", "Debited to retiring partner", "Credited to retiring partner and debited to gaining partners", "Ignored entirely"], "ans": 2, "expl": "Gaining partners compensate the retiring partner by debiting their capital accounts and crediting the retiring partner.", "type": "mcq"}
]

if __name__ == "__main__":
    process_chapter("ncert_class12_accounts_leac101", "Accountancy - Partnership Basics", ch101_items)
    process_chapter("ncert_class12_accounts_leac103", "Accountancy - Retirement/Death of a Partner", ch103_items)
