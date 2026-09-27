import json
import os
import time
from googletrans import Translator

# Initialize translator
translator = Translator()

def safe_translate(text, dest_lang):
    if not text:
        return ""
    try:
        # time.sleep(0.1) # Avoid rate limiting
        return translator.translate(text, src='en', dest=dest_lang).text
    except Exception as e:
        print(f"Translation failed for '{text[:20]}...': {e}")
        return text

def translate_block(block):
    """Dynamically translates fields that don't have _hi or _gu variants yet."""
    translated_block = block.copy()
    keys_to_translate = []
    
    for key, value in block.items():
        if isinstance(value, str) and not key.endswith('_hi') and not key.endswith('_gu') and key not in ['id', 'type', 'media_url']:
            keys_to_translate.append(key)
            
    for key in keys_to_translate:
        val = block[key]
        if key + '_hi' not in block:
            translated_block[key + '_hi'] = safe_translate(val, 'hi')
        if key + '_gu' not in block:
            translated_block[key + '_gu'] = safe_translate(val, 'gu')
            
    # Handle nested options array in MCQs
    if 'options' in block:
        options_hi = []
        options_gu = []
        for opt in block['options']:
            options_hi.append(safe_translate(opt, 'hi'))
            options_gu.append(safe_translate(opt, 'gu'))
        translated_block['options_hi'] = options_hi
        translated_block['options_gu'] = options_gu
            
    return translated_block

metadata = {
    "id": "CBSE_CLASS12_ECONOMICS_CH1",
    "title": "Chapter 1: National Income and Related Aggregates",
    "title_hi": "अध्याय 1: राष्ट्रीय आय और संबंधित समुच्चय",
    "title_gu": "પ્રકરણ 1: રાષ્ટ્રીય આવક અને સંબંધિત સમુચ્ચય",
    "subject": "Economics",
    "class": "Class 12",
    "board": "CBSE"
}

blocks = [
    # STEP 1: HOOK
    {
        "id": "CBSE_CLASS12_ECO_CH1_001",
        "type": "theory",
        "title": "The 5 Trillion Dollar Dream",
        "body": "In 2026, you constantly hear news anchors debating whether India will reach a '5 Trillion Dollar Economy'. But what exactly are they measuring? Are they counting your pocket money? The value of a new highway? Or the profits of a multinational tech company? Let's decode the biggest number in economics: The National Income."
    },
    # STEP 2: SOCRATIC THINKING
    {
        "id": "CBSE_CLASS12_ECO_CH1_002",
        "type": "socratic_question",
        "question": "If you sell your old, used bicycle to your friend for ₹2,000, do you think this ₹2,000 should be added to the country's GDP for this year? Why or why not?",
        "hint": "Think about whether any *new* production actually happened when you handed over the old bicycle."
    },
    # STEP 3: DISCOVERY
    {
        "id": "CBSE_CLASS12_ECO_CH1_003",
        "type": "theory",
        "title": "The Circular Flow of Income",
        "body": "Imagine an economy with only two actors: Households (like your family) and Firms (like a factory). Households provide 'Factors of Production' (Land, Labour, Capital, Entrepreneurship) to the Firms. In return, Firms pay 'Factor Incomes' (Rent, Wages, Interest, Profit). \n\nThen, Households use this income to buy the goods and services produced by the Firms. This endless loop is the Circular Flow of Income. It proves a fundamental economic rule: **One person's expenditure is always another person's income.**"
    },
    # STEP 4: REVEAL
    {
        "id": "CBSE_CLASS12_ECO_CH1_004",
        "type": "theory",
        "title": "What is Gross Domestic Product (GDP)?",
        "body": "Gross Domestic Product (GDP) is the total market value of all **final** goods and services produced within the **domestic territory** of a country during a given period of time (usually a year).\n\nKey rules:\n1. **Final Goods Only:** We don't count intermediate goods (like flour used to make bread) to avoid double counting.\n2. **Domestic Territory:** It must be produced within the economic boundaries of the country, regardless of who produces it (an Indian or a foreigner).\n3. **Current Production:** Second-hand goods (like your old bicycle) are not included because they were already counted in the year they were manufactured."
    },
    # STEP 5: KNOWLEDGE CHECK
    {
        "id": "CBSE_CLASS12_ECO_CH1_005",
        "type": "mcq",
        "question": "Which of the following is included in the calculation of India's GDP?",
        "options": [
            "The sale of a 5-year-old used car.",
            "Flour purchased by a bakery to make bread.",
            "A new smartphone manufactured in a factory in Noida.",
            "Financial help (scholarship) received by a student from the government."
        ],
        "correct_index": 2,
        "explanation": "Only the new smartphone is a final good produced currently. Used cars were counted previously, flour is an intermediate good here, and scholarships are transfer payments (no productive service rendered)."
    },
    # STEP 6: REFLECTION
    {
        "id": "CBSE_CLASS12_ECO_CH1_006",
        "type": "teacher_tip",
        "title": "Teacher's Insight on 'Domestic' vs 'National'",
        "body": "Many students confuse 'Domestic' with 'National'. Think of it this way: 'Domestic' cares about WHERE it is produced (inside India's borders). 'National' cares about WHO produces it (normal residents of India, even if they are temporarily abroad).\n\nTo go from Domestic to National, we just add the Net Factor Income from Abroad (NFIA)."
    },
    # STEP 7: CONNECTION
    {
        "id": "CBSE_CLASS12_ECO_CH1_007",
        "type": "theory",
        "title": "The Magic Formulas (Aggregates)",
        "body": "In macroeconomics, there are 8 related aggregates. You can jump between them using three simple rules:\n\n1. **Gross vs Net:** \n   Gross - Depreciation = Net\n2. **Domestic vs National:** \n   Domestic + NFIA = National\n3. **Market Price (MP) vs Factor Cost (FC):** \n   Market Price - Net Indirect Taxes (NIT) = Factor Cost\n\n*Note: National Income is formally known as Net National Product at Factor Cost (NNPfc).*"
    },
    # STEP 8: MASTERY (Solved Numerical)
    {
        "id": "CBSE_CLASS12_ECO_CH1_008",
        "type": "practice_question",
        "question": "Calculate National Income (NNPfc) from the following data:\n1. GDP at Market Price (GDPmp) = ₹ 1,00,000 Crores\n2. Depreciation (Consumption of Fixed Capital) = ₹ 10,000 Crores\n3. Net Factor Income from Abroad (NFIA) = ₹ 2,000 Crores\n4. Indirect Taxes = ₹ 15,000 Crores\n5. Subsidies = ₹ 5,000 Crores",
        "solution": "# Pedagogical Solving Guide\n\n**Step 1: Convert Gross to Net**\n- Rule: Net = Gross - Depreciation\n- NDPmp = GDPmp - Depreciation\n- NDPmp = 1,00,000 - 10,000 = ₹ 90,000 Crores\n\n**Step 2: Convert Domestic to National**\n- Rule: National = Domestic + NFIA\n- NNPmp = NDPmp + NFIA\n- NNPmp = 90,000 + 2,000 = ₹ 92,000 Crores\n\n**Step 3: Convert Market Price to Factor Cost**\n- Rule: Factor Cost = Market Price - Net Indirect Taxes (NIT)\n- First, calculate NIT = Indirect Taxes - Subsidies = 15,000 - 5,000 = 10,000\n- NNPfc (National Income) = NNPmp - NIT\n- NNPfc = 92,000 - 10,000 = **₹ 82,000 Crores**"
    },
    # TEXTBOOK EXERCISE QUSETIONS
    {
        "id": "CBSE_CLASS12_ECO_CH1_009",
        "type": "mcq",
        "question": "Net Factor Income from Abroad (NFIA) is defined as:",
        "options": [
            "Factor income received from abroad minus factor income paid abroad.",
            "Export of goods minus import of goods.",
            "Direct taxes minus indirect taxes.",
            "Gross investment minus depreciation."
        ],
        "correct_index": 0,
        "explanation": "NFIA is the difference between factor income earned by our residents from the rest of the world and factor income earned by non-residents within our domestic territory."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH1_010",
        "type": "mcq",
        "question": "Which of the following is a 'Transfer Payment' and thus NOT included in National Income?",
        "options": [
            "Salary paid to a government school teacher.",
            "Bonus paid to factory workers.",
            "Old age pension given by the government.",
            "Commission paid to a real estate agent."
        ],
        "correct_index": 2,
        "explanation": "Old age pension is a transfer payment because it is a one-sided payment without any corresponding productive service in the current year. Salaries, bonuses, and commissions are factor payments."
    }
]

def main():
    print("Translating and generating CBSE Class 12 Economics Chapter 1...")
    translated_blocks = []
    
    total = len(blocks)
    for i, block in enumerate(blocks):
        print(f"Translating block {i+1}/{total}: {block['id']}...")
        translated = translate_block(block)
        translated_blocks.append(translated)
        
    final_data = {
        "metadata": metadata,
        "blocks": translated_blocks
    }
    
    output_path = 'app_core/chapters/cbse_class12_economics_ch1.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)
        f.write('\n')
        
    print(f"Successfully generated {output_path}")

if __name__ == "__main__":
    main()
