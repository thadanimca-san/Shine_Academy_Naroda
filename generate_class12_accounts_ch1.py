import json
import time
from deep_translator import GoogleTranslator, MyMemoryTranslator

# Dual-translation setup
g_translator = GoogleTranslator(source='en', target='hi')
m_translator = MyMemoryTranslator(source='en-US', target='hi-IN')

def translate_text(text):
    if not text or not isinstance(text, str):
        return text
    try:
        time.sleep(0.5)
        return g_translator.translate(text)
    except Exception as e:
        print(f"GoogleTranslator failed for '{text[:20]}': {e}. Trying MyMemory...")
        try:
            time.sleep(1)
            return m_translator.translate(text)
        except Exception:
            print(f"Both failed for '{text[:20]}'.")
            return text

def build_chapter():
    chapter = {
        "metadata": {
            "id": "gseb_class12_accounts_ch1",
            "title": "Introduction to Partnership",
            "subject": "Accountancy",
            "grade": 12,
            "board": "GSEB",
            "language": "en",
            "difficulty": "Beginner",
            "estimated_minutes": 45
        },
        "blocks": [
            {
                "id": "ACC12_CH1_001",
                "type": "hook",
                "title": "The Lemonade Stand Dilemma",
                "body": "Imagine you have a highly successful lemonade stand (a Sole Proprietorship). You want to expand and open 5 new stalls across the city. You have the secret recipe, but you don't have the money or the time to manage 5 stalls alone. Your friend has money and a car, but doesn't know how to make lemonade. What should you do?"
            },
            {
                "id": "ACC12_CH1_002",
                "type": "socratic_thinking",
                "question": "If you decide to join hands with your friend and run the business together, what is the biggest risk you might face in the future?",
                "options": [
                  "You will make too much money.",
                  "You might fight over how to divide the profits.",
                  "The business will automatically become illegal."
                ],
                "correct_index": 1,
                "explanation": "Money changes things! Without clear rules, disputes over effort, profit sharing, and decision-making are guaranteed."
            },
            {
                "id": "ACC12_CH1_003",
                "type": "theory",
                "title": "The Power of Teamwork (Exploration)",
                "body": "Think of business growth like carrying a heavy load. One person (Sole Proprietor) can only lift 50kg. But two people working together can lift 150kg! By combining your recipe (skill) with your friend's money (capital), you create a Partnership. A Partnership overcomes the limitations of a Sole Proprietorship: limited capital, limited managerial ability, and limited risk-taking capacity."
            },
            {
                "id": "ACC12_CH1_004",
                "type": "definition",
                "title": "Definition of Partnership",
                "body": "According to Section 4 of the Indian Partnership Act, 1932: 'Partnership is the relation between persons who have agreed to share the profits of a business carried on by all or any of them acting for all.'\n\nKey terminology:\n- Partners: The individuals who join the business.\n- Firm: The partners collectively.\n- Firm Name: The name under which the business is carried on."
            },
            {
                "id": "ACC12_CH1_005",
                "type": "mcq",
                "question": "What is the minimum and maximum number of partners allowed in an ordinary business according to the Companies Act, 2013?",
                "options": [
                  "Minimum 1, Maximum 10",
                  "Minimum 2, Maximum 50",
                  "Minimum 2, Maximum 100",
                  "Minimum 2, No limit"
                ],
                "correct_index": 1,
                "explanation": "A minimum of 2 persons are required to form a partnership. The Companies Act, 2013 restricts the maximum number of partners to 50."
            },
            {
                "id": "ACC12_CH1_006",
                "type": "reflection",
                "title": "Think of Real Partnerships",
                "body": "Think of famous global companies. Did you know Google was started by Larry Page and Sergey Brin as a partnership? Apple was started by Steve Jobs, Steve Wozniak, and Ronald Wayne! Can you think of any famous partnerships in your own city?"
            },
            {
                "id": "ACC12_CH1_007",
                "type": "hook",
                "title": "The Courtroom Drama",
                "body": "Two best friends, Rahul and Amit, start a shoe store. They agree verbally to split profits 50-50. Five years later, the store is making millions. Amit secretly takes 80% of the cash, claiming he works more hours. Rahul takes Amit to court. But the judge asks, 'Where is your written proof?' Rahul has none. He loses half his wealth. How could this have been avoided?"
            },
            {
                "id": "ACC12_CH1_008",
                "type": "theory",
                "title": "The Partnership Deed (साझेदारी संलेख)",
                "body": "To prevent the 'Rahul and Amit' disaster, partners must have a clear agreement. A written agreement containing the terms and conditions of partnership is called a Partnership Deed. It acts as the constitution of the firm. It contains details like:\n1. Name and address of the firm.\n2. Capital contributed by each partner.\n3. Profit and loss sharing ratio.\n4. Interest on Capital, Drawings, and Loans.\n5. Salaries or commissions payable to partners.\n\nNote: A written deed is NOT legally compulsory, but it is highly desirable to prevent disputes!"
            },
            {
                "id": "ACC12_CH1_009",
                "type": "memory_trick",
                "title": "Rules in Absence of Partnership Deed",
                "body": "What happens if partners are lazy and don't make a Partnership Deed? The Indian Partnership Act, 1932 enforces strict rules! Memorize them with the acronym 'ESN' (Equal, Six, No):\n\n- E (Equal): Profits and losses are shared EQUALLY, no matter who invested more capital!\n- S (Six): Interest on a partner's loan to the firm is given at 6% p.a.\n- N (No): NO Interest on Capital, NO Interest on Drawings, NO Salary or Commission to any partner."
            },
            {
                "id": "ACC12_CH1_010",
                "type": "mcq",
                "question": "A and B are partners without a partnership deed. A invested ₹5,00,000 and B invested ₹1,00,000. How will the profit of ₹60,000 be distributed?",
                "options": [
                  "A: ₹50,000, B: ₹10,000 (Capital Ratio)",
                  "A: ₹30,000, B: ₹30,000 (Equally)",
                  "A gets all the profit because he invested more."
                ],
                "correct_index": 1,
                "explanation": "In the absence of a Partnership Deed, profits are always shared EQUALLY, regardless of the capital invested. So both get ₹30,000."
            },
            {
                "id": "ACC12_CH1_011",
                "type": "theory",
                "title": "Profit and Loss Appropriation Account (The Pizza Analogy)",
                "body": "In Class 11, you learned to make the Profit & Loss (P&L) A/c to find Net Profit. But in a partnership, the Net Profit belongs to multiple people!\n\nThink of the Net Profit as a giant pizza. Before the partners can eat it, they must pay for 'extra toppings'. The firm opens a special account called the Profit and Loss Appropriation Account to distribute this pizza. \n\nWe CREDIT the Net Profit and Interest on Drawings to this account (more pizza). We DEBIT Interest on Capital, Partners' Salaries, and Commission (the extra toppings). Whatever pizza is left at the end is the 'Divisible Profit', which is finally given to the partners in their profit-sharing ratio!"
            },
            {
                "id": "ACC12_CH1_012",
                "type": "mcq",
                "question": "Where is the 'Interest on Partner's Capital' recorded by the firm?",
                "options": [
                  "Debit side of Profit & Loss Account",
                  "Debit side of Profit & Loss Appropriation Account",
                  "Credit side of Profit & Loss Appropriation Account"
                ],
                "correct_index": 1,
                "explanation": "It is an appropriation (distribution) of profit. The firm is paying the partners, so it is an expense for the firm. Hence, it is recorded on the DEBIT side of the P&L Appropriation Account."
            }
        ]
    }
    
    print("Starting translation phase...")
    for idx, block in enumerate(chapter["blocks"]):
        print(f"Translating block {idx+1}/{len(chapter['blocks'])} ({block['type']})...")
        
        if "title" in block:
            block["title_hi"] = translate_text(block["title"])
            
        if "body" in block:
            block["body_hi"] = translate_text(block["body"])
            
        if "question" in block:
            block["question_hi"] = translate_text(block["question"])
            
        if "explanation" in block:
            block["explanation_hi"] = translate_text(block["explanation"])
            
        if "options" in block:
            block["options_hi"] = [translate_text(opt) for opt in block["options"]]
            
    # Save the file
    out_file = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_accounts_ch1.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(chapter, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {out_file} with dual-language support!")

if __name__ == "__main__":
    build_chapter()
