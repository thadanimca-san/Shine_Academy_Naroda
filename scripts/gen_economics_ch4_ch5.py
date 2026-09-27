import json
import os
from googletrans import Translator

translator = Translator()

def safe_translate(text, dest_lang):
    if not text: return ""
    try:
        return translator.translate(text, src='en', dest=dest_lang).text
    except Exception as e:
        print(f"Translation failed: {e}")
        return text

def process_chapter(chapter_data):
    print(f"Processing {chapter_data['metadata']['title']}...")
    translated_blocks = []
    
    for block in chapter_data['blocks']:
        t_block = block.copy()
        keys_to_translate = [k for k, v in block.items() if isinstance(v, str) and not k.endswith('_hi') and not k.endswith('_gu') and k not in ['id', 'type', 'media_url']]
        
        for key in keys_to_translate:
            val = block[key]
            if key + '_hi' not in block: t_block[key + '_hi'] = safe_translate(val, 'hi')
            if key + '_gu' not in block: t_block[key + '_gu'] = safe_translate(val, 'gu')
                
        if 'options' in block:
            t_block['options_hi'] = [safe_translate(opt, 'hi') for opt in block['options']]
            t_block['options_gu'] = [safe_translate(opt, 'gu') for opt in block['options']]
            
        translated_blocks.append(t_block)
        
    final_data = {
        "metadata": chapter_data['metadata'],
        "blocks": translated_blocks
    }
    
    filename = chapter_data['metadata']['id'].lower() + '.json'
    output_path = os.path.join('app_core/chapters', filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(f"Saved {output_path}")

# CHAPTER 4: Government Budget and the Economy
ch4_metadata = {
    "id": "cbse_class12_economics_ch4",
    "title": "Chapter 4: Government Budget and the Economy",
    "title_hi": "अध्याय 4: सरकारी बजट और अर्थव्यवस्था",
    "title_gu": "પ્રકરણ 4: સરકારી અંદાજપત્ર અને અર્થતંત્ર",
    "subject": "Economics",
    "class": "Class 12",
    "board": "CBSE"
}

ch4_blocks = [
    {
        "id": "CBSE_CLASS12_ECO_CH4_001",
        "type": "theory",
        "title": "February 1st: The Big Day",
        "body": "Every year on February 1st, millions of Indians tune in to watch the Finance Minister carry a red briefcase into the Parliament. The stock market swings wildly, businesses hold their breath, and citizens wait to see if taxes will go up or down. But what exactly is inside that briefcase? It is the blueprint of the nation's financial future for the next year: The Union Budget."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH4_002",
        "type": "socratic_question",
        "question": "If the government decides to print unlimited money to build free hospitals and schools for everyone, what do you think would happen to the price of an apple in the market?",
        "hint": "Think about what happens to the value of money when there is too much of it chasing the same amount of goods."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH4_003",
        "type": "theory",
        "title": "What is a Government Budget?",
        "body": "A Government Budget is an annual statement showing item-wise estimates of expected receipts (incomes) and anticipated expenditure of the government for a fiscal year (April 1 to March 31). \n\nRemember, it is an **estimate**, not the actual numbers. The government prepares it to achieve goals like economic growth, reducing inequalities, and maintaining price stability."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH4_004",
        "type": "theory",
        "title": "Revenue vs Capital: The Golden Rule",
        "body": "The budget is strictly divided into Revenue and Capital components. How do you tell the difference?\n\n**Revenue Receipts/Expenditure:** They do NOT create any assets or cause any reduction in liabilities. (Example: Tax collected, Salary paid to government employees. It's routine and recurring).\n\n**Capital Receipts/Expenditure:** They EITHER create an asset OR reduce a liability. (Example: Government takes a loan, or builds a new Metro line. It's structural)."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH4_005",
        "type": "mcq",
        "question": "Which of the following is an example of a Capital Receipt for the Government of India?",
        "options": [
            "Income tax collected from citizens.",
            "Dividends received from a Public Sector Undertaking (PSU).",
            "Borrowings from the World Bank.",
            "Fines and penalties collected by the traffic police."
        ],
        "correct_index": 2,
        "explanation": "Borrowings create a liability for the government (they have to pay it back). Anything that creates a liability is a Capital Receipt. Taxes, dividends, and fines do not create a liability, so they are Revenue Receipts."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH4_006",
        "type": "teacher_tip",
        "title": "Teacher's Insight on Deficits",
        "body": "When expenditure > receipts, we have a deficit. You must know the 3 types of deficits:\n1. **Revenue Deficit:** Revenue Exp - Revenue Receipts. (Shows government can't meet routine expenses).\n2. **Fiscal Deficit:** Total Exp - Total Receipts (excluding borrowings). **This is exactly equal to the total borrowing requirement of the government!**\n3. **Primary Deficit:** Fiscal Deficit - Interest Payments. (Shows how much the government is borrowing *this year*, ignoring past debts)."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH4_007",
        "type": "practice_question",
        "question": "Calculate the Fiscal Deficit and Primary Deficit from the given data:\n- Revenue Expenditure = ₹ 80,000 Crores\n- Capital Expenditure = ₹ 20,000 Crores\n- Revenue Receipts = ₹ 60,000 Crores\n- Capital Receipts net of Borrowings (e.g., Disinvestment) = ₹ 10,000 Crores\n- Interest Payments = ₹ 5,000 Crores",
        "solution": "# Pedagogical Solving Guide\n\n**Step 1: Calculate Total Expenditure**\n- Total Exp = Revenue Exp + Capital Exp\n- Total Exp = 80,000 + 20,000 = ₹ 1,00,000 Crores\n\n**Step 2: Calculate Total Receipts (Excluding Borrowings)**\n- Total Receipts = Revenue Receipts + Capital Receipts (net of borrowings)\n- Total Receipts = 60,000 + 10,000 = ₹ 70,000 Crores\n\n**Step 3: Calculate Fiscal Deficit**\n- Rule: Fiscal Deficit = Total Exp - Total Receipts (exc. borrowings)\n- Fiscal Deficit = 1,00,000 - 70,000 = **₹ 30,000 Crores**\n\n**Step 4: Calculate Primary Deficit**\n- Rule: Primary Deficit = Fiscal Deficit - Interest Payments\n- Primary Deficit = 30,000 - 5,000 = **₹ 25,000 Crores**"
    }
]

# CHAPTER 5: Balance of Payments
ch5_metadata = {
    "id": "cbse_class12_economics_ch5",
    "title": "Chapter 5: Balance of Payments",
    "title_hi": "अध्याय 5: भुगतान संतुलन",
    "title_gu": "પ્રકરણ 5: ચૂકવણીનું સંતુલન (Balance of Payments)",
    "subject": "Economics",
    "class": "Class 12",
    "board": "CBSE"
}

ch5_blocks = [
    {
        "id": "CBSE_CLASS12_ECO_CH5_001",
        "type": "theory",
        "title": "The Price of an iPhone",
        "body": "When you buy an iPhone manufactured in the USA, you pay in Indian Rupees (₹). But Apple's employees in California want to be paid in US Dollars ($). How does your ₹ magically convert into $? Who tracks this money leaving India? \n\nEvery single economic transaction between India and the rest of the world—whether it's exporting software, importing oil, or sending money to a relative abroad—is meticulously recorded in a ledger called the Balance of Payments (BoP)."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH5_002",
        "type": "socratic_question",
        "question": "If India imports more goods than it exports, money is leaving the country. How do you think the government covers this shortfall so the country doesn't go bankrupt?",
        "hint": "Think about investments, taking loans from other countries, or NRIs sending money back home."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH5_003",
        "type": "theory",
        "title": "Current Account vs Capital Account",
        "body": "The BoP has two main accounts:\n\n**1. Current Account:** Records exports/imports of goods (visible trade), services (invisible trade), and unilateral transfers (gifts/donations). It does *not* impact the asset-liability status of the country.\n\n**2. Capital Account:** Records all transactions that *do* affect the asset-liability status of the country, such as Foreign Direct Investment (FDI), taking loans from the World Bank, or buying real estate abroad."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH5_004",
        "type": "theory",
        "title": "Foreign Exchange Rate",
        "body": "The Foreign Exchange Rate is the rate at which one currency can be exchanged for another (e.g., $1 = ₹83). \n\nIn a **Flexible Exchange Rate System**, this rate is determined entirely by the market forces of Demand and Supply of foreign currency. If Indians suddenly want to buy a lot of American goods, the demand for Dollars will increase, making the Dollar more expensive (and the Rupee will *depreciate*)."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH5_005",
        "type": "mcq",
        "question": "If the exchange rate changes from $1 = ₹80 to $1 = ₹85, what will likely happen to India's exports to the USA?",
        "options": [
            "Exports will decrease because Indian goods became more expensive for Americans.",
            "Exports will increase because Indian goods became cheaper for Americans.",
            "Exports will remain unchanged.",
            "Imports from the USA will increase."
        ],
        "correct_index": 1,
        "explanation": "This is a depreciation of the Rupee. Previously, an American could buy ₹80 worth of goods with $1. Now, they can buy ₹85 worth of goods with that same $1. Since Indian goods are now cheaper for them, they will buy more, causing India's exports to increase."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH5_006",
        "type": "teacher_tip",
        "title": "Teacher's Insight on BoP Always Balancing",
        "body": "In the accounting sense, the Balance of Payments *always* balances (BoP = 0). \n\nIf we have a deficit in the Current Account (we imported more than we exported), we must finance it by having a surplus in the Capital Account (e.g., taking foreign loans or getting FDI) or by withdrawing from our Official Reserves at the RBI."
    }
]

if __name__ == "__main__":
    process_chapter({"metadata": ch4_metadata, "blocks": ch4_blocks})
    process_chapter({"metadata": ch5_metadata, "blocks": ch5_blocks})
