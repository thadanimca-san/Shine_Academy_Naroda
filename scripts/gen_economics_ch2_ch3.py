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


# CHAPTER 2: Money and Banking
ch2_metadata = {
    "id": "cbse_class12_economics_ch2",
    "title": "Chapter 2: Money and Banking",
    "title_hi": "अध्याय 2: मुद्रा और बैंकिंग",
    "title_gu": "પ્રકરણ 2: નાણું અને બેંકિંગ",
    "subject": "Economics",
    "class": "Class 12",
    "board": "CBSE"
}

ch2_blocks = [
    {
        "id": "CBSE_CLASS12_ECO_CH2_001",
        "type": "theory",
        "title": "A World Without Money",
        "body": "Imagine you are a farmer who grows wheat, but you desperately need a pair of shoes. You find a cobbler, but the cobbler doesn't want wheat; he wants apples. You now have to find someone with apples who wants wheat, trade with them, and then take the apples to the cobbler! This frustrating nightmare is called the 'Double Coincidence of Wants' under the Barter System. How did humanity solve this?"
    },
    {
        "id": "CBSE_CLASS12_ECO_CH2_002",
        "type": "socratic_question",
        "question": "If you print your own pieces of paper and write '₹2000' on them, will shopkeepers accept them? Why do people accept the papers printed by the RBI, but not yours?",
        "hint": "Think about authority, legal backing, and trust in the government."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH2_003",
        "type": "theory",
        "title": "What is Money?",
        "body": "Money is anything that is generally accepted as a medium of exchange, a measure of value, a store of value, and a standard for deferred payments.\n\nThe modern Rupee notes you hold are 'Fiat Money'. They have no intrinsic value (the paper itself is worthless), but they act as money by the 'fiat' (order) of the government. It is legally mandated to be accepted for settling debts."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH2_004",
        "type": "theory",
        "title": "The Magic of Credit Creation",
        "body": "Did you know commercial banks 'create' money out of thin air? When you deposit ₹1,000 in a bank, the bank knows you won't withdraw it all tomorrow. So, keeping a small percentage aside (Cash Reserve Ratio, say 10%), they lend out the remaining ₹900. When that ₹900 is spent and redeposited by someone else, they lend out 90% of that again! \n\nThis continuous chain means an initial deposit of ₹1,000 can result in a total money supply of ₹10,000 in the economy. This is the Money Multiplier effect!"
    },
    {
        "id": "CBSE_CLASS12_ECO_CH2_005",
        "type": "mcq",
        "question": "If the Legal Reserve Ratio (LRR) set by the Central Bank is 20%, what is the value of the Money Multiplier?",
        "options": [
            "2",
            "4",
            "5",
            "10"
        ],
        "correct_index": 2,
        "explanation": "The formula for the Money Multiplier is 1 / LRR. Therefore, 1 / 0.20 = 5. This means every ₹1 of initial deposit can create ₹5 of total credit."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH2_006",
        "type": "theory",
        "title": "The Boss: The Central Bank (RBI)",
        "body": "The Reserve Bank of India (RBI) is the apex institution that controls the entire banking system. Its main functions are:\n1. **Bank of Issue:** Monopoly rights to issue currency notes.\n2. **Banker to the Government:** Manages government accounts and buys/sells securities for them.\n3. **Banker's Bank:** Holds cash reserves of commercial banks and acts as a Lender of Last Resort.\n4. **Controller of Credit:** Controls the money supply to fight inflation or deflation."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH2_007",
        "type": "practice_question",
        "question": "Explain how the Central Bank uses 'Repo Rate' to control inflation in the economy.",
        "solution": "# Pedagogical Solving Guide\n\n**Step 1: Define Repo Rate**\n- The Repo Rate is the interest rate at which the Central Bank (RBI) lends short-term funds to commercial banks.\n\n**Step 2: Connect Repo Rate to Commercial Banks**\n- If the RBI wants to control inflation (too much money chasing too few goods), it will **INCREASE** the Repo Rate.\n- This makes borrowing expensive for commercial banks.\n\n**Step 3: Connect to the Public**\n- Because their cost of funds increased, commercial banks will increase the interest rates on the loans they offer to the public (car loans, home loans).\n- As a result, the public borrows less, spends less, and investment falls.\n\n**Step 4: Conclusion**\n- A decrease in aggregate demand leads to a fall in prices, successfully controlling inflation."
    }
]

# CHAPTER 3: Determination of Income and Employment
ch3_metadata = {
    "id": "cbse_class12_economics_ch3",
    "title": "Chapter 3: Determination of Income and Employment",
    "title_hi": "अध्याय 3: आय और रोजगार का निर्धारण",
    "title_gu": "પ્રકરણ 3: આવક અને રોજગારીનું નિર્ધારણ",
    "subject": "Economics",
    "class": "Class 12",
    "board": "CBSE"
}

ch3_blocks = [
    {
        "id": "CBSE_CLASS12_ECO_CH3_001",
        "type": "theory",
        "title": "The Great Depression & John Maynard Keynes",
        "body": "In the 1930s, the world economy crashed. Millions were unemployed, factories sat empty, but classical economists insisted, 'Don't worry, the free market will fix itself eventually.' \n\nA brilliant economist named John Maynard Keynes famously replied, *'In the long run, we are all dead.'* He argued that governments MUST step in to boost demand when the economy crashes. Welcome to Keynesian Economics, the foundation of modern macroeconomic policy!"
    },
    {
        "id": "CBSE_CLASS12_ECO_CH3_002",
        "type": "socratic_question",
        "question": "If everyone in the country decides to suddenly save 80% of their income out of fear of a recession, what will actually happen to the economy's total wealth?",
        "hint": "Remember the circular flow: Your expenditure is someone else's income. If no one spends, what happens to factories?"
    },
    {
        "id": "CBSE_CLASS12_ECO_CH3_003",
        "type": "theory",
        "title": "Aggregate Demand (AD) and its Components",
        "body": "Aggregate Demand is the total demand for final goods and services in an economy at a given price level during an accounting year. It represents planned expenditure, not actual expenditure.\n\n**Components in a Two-Sector Economy:**\n**AD = C + I**\nWhere:\n- **C = Consumption Expenditure:** Spending by households on goods and services.\n- **I = Investment Expenditure:** Spending by firms on capital goods (machinery, factories). In our syllabus, we assume 'I' is autonomous (constant)."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH3_004",
        "type": "theory",
        "title": "The Consumption Function (Propensity to Consume)",
        "body": "The Consumption Function shows the relationship between consumption (C) and income (Y).\n**C = \u0101 + bY**\n- **\u0101 (Autonomous Consumption):** Minimum consumption needed for survival even when income is zero (funded by past savings or borrowing).\n- **b (Marginal Propensity to Consume - MPC):** The ratio of change in consumption to change in income (ΔC / ΔY). It shows what percentage of *additional* income is spent."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH3_005",
        "type": "mcq",
        "question": "If your income increases by ₹1,000 and your consumption increases by ₹800, what is your Marginal Propensity to Save (MPS)?",
        "options": [
            "0.8",
            "0.2",
            "800",
            "200"
        ],
        "correct_index": 1,
        "explanation": "MPC = ΔC / ΔY = 800 / 1000 = 0.8. Since income can only be consumed or saved, MPC + MPS = 1. Therefore, MPS = 1 - 0.8 = 0.2."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH3_006",
        "type": "teacher_tip",
        "title": "Teacher's Insight on Equilibrium",
        "body": "Equilibrium in an economy is achieved when what producers plan to produce (Aggregate Supply) is exactly equal to what buyers plan to buy (Aggregate Demand). \n\n**AD = AS** (or **S = I**). \n\nIf AD > AS, there is excess demand. Inventories will fall, and producers will increase production and employment to catch up. If AD < AS, inventories pile up, leading to a cut in production and job losses."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH3_007",
        "type": "practice_question",
        "question": "Calculate the Equilibrium Level of Income for an economy where:\nAutonomous Consumption (\u0101) = ₹ 100 Crores\nMarginal Propensity to Consume (MPC) = 0.5\nInvestment (I) = ₹ 200 Crores",
        "solution": "# Pedagogical Solving Guide\n\n**Step 1: State the Equilibrium Condition**\n- The economy is in equilibrium when Aggregate Demand (AD) equals Aggregate Supply (AS or Y).\n- Therefore, **Y = AD**\n- Since AD = C + I, we can write: **Y = C + I**\n\n**Step 2: Substitute the Consumption Function**\n- We know C = \u0101 + bY\n- Substitute this into the equation: **Y = \u0101 + bY + I**\n\n**Step 3: Plug in the Values**\n- Y = 100 + 0.5Y + 200\n\n**Step 4: Solve for Y algebraically**\n- Y - 0.5Y = 300\n- 0.5Y = 300\n- Y = 300 / 0.5\n- Y = **₹ 600 Crores**"
    }
]

if __name__ == "__main__":
    process_chapter({"metadata": ch2_metadata, "blocks": ch2_blocks})
    process_chapter({"metadata": ch3_metadata, "blocks": ch3_blocks})
