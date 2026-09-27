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

# CHAPTER 6: Development Experience (1947-90) and Economic Reforms since 1991
ch6_metadata = {
    "id": "cbse_class12_economics_ch6",
    "title": "Chapter 6: Development Experience and Economic Reforms",
    "title_hi": "अध्याय 6: विकास का अनुभव और आर्थिक सुधार",
    "title_gu": "પ્રકરણ 6: વિકાસનો અનુભવ અને આર્થિક સુધારા",
    "subject": "Economics",
    "class": "Class 12",
    "board": "CBSE"
}

ch6_blocks = [
    {
        "id": "CBSE_CLASS12_ECO_CH6_001",
        "type": "theory",
        "title": "The Golden Bird in Chains",
        "body": "Before the British arrived, India was known as the 'Golden Bird', contributing to over 20% of the world's GDP. We were famous globally for our exquisite cotton, silk textiles, and spices. But by the time the British left in 1947, India was left impoverished, with a stagnant agricultural sector, destroyed handicrafts, and an alarming life expectancy of just 32 years. How did an empire systematically drain a subcontinent's wealth?"
    },
    {
        "id": "CBSE_CLASS12_ECO_CH6_002",
        "type": "socratic_question",
        "question": "If you were the Prime Minister of newly independent India in 1947, would you open up the country's borders to foreign trade immediately, or would you protect local industries? Why?",
        "hint": "Think about whether a newly born, weak domestic industry can survive competition against massive British or American factories."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH6_003",
        "type": "theory",
        "title": "The Inward-Looking Trade Policy (1950-1990)",
        "body": "India chose 'Import Substitution'. The idea was simple: instead of importing goods like cars or electronics, we will produce them domestically. \n\nTo protect these domestic industries from fierce international competition, the government imposed heavy **Tariffs** (taxes on imported goods, making them expensive) and **Quotas** (strict limits on how much can be imported). While this protected local industries, it also meant they had no incentive to improve quality, leading to the infamous 'License Raj' era of poor-quality goods."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH6_004",
        "type": "theory",
        "title": "The Crisis of 1991 & The LPG Reforms",
        "body": "By 1991, India was on the brink of bankruptcy. We had only enough foreign exchange reserves to pay for 2 weeks of imports! To secure a bailout loan from the World Bank and IMF, India was forced to fundamentally change its economic model.\n\nFinance Minister Dr. Manmohan Singh introduced the New Economic Policy (NEP), famously known as the **LPG Reforms**: \n1. **Liberalisation:** Freeing the economy from direct government controls (License Raj).\n2. **Privatisation:** Selling off loss-making government companies (PSUs) to the private sector.\n3. **Globalisation:** Opening up the economy to the world by reducing tariffs and encouraging Foreign Direct Investment (FDI)."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH6_005",
        "type": "mcq",
        "question": "Which of the following was the main objective of 'Import Substitution' policy adopted by India before 1991?",
        "options": [
            "To increase imports from foreign countries.",
            "To encourage multi-national corporations (MNCs) to set up factories in India.",
            "To protect domestic industries from foreign competition.",
            "To completely ban agricultural farming."
        ],
        "correct_index": 2,
        "explanation": "Import substitution aimed at replacing imported goods with domestically produced goods to protect local infant industries from foreign competition using tariffs and quotas."
    }
]

# CHAPTER 7: Current Challenges facing Indian Economy
ch7_metadata = {
    "id": "cbse_class12_economics_ch7",
    "title": "Chapter 7: Current Challenges facing Indian Economy",
    "title_hi": "अध्याय 7: भारतीय अर्थव्यवस्था के सामने वर्तमान चुनौतियाँ",
    "title_gu": "પ્રકરણ 7: ભારતીય અર્થતંત્ર સમક્ષ વર્તમાન પડકારો",
    "subject": "Economics",
    "class": "Class 12",
    "board": "CBSE"
}

ch7_blocks = [
    {
        "id": "CBSE_CLASS12_ECO_CH7_001",
        "type": "theory",
        "title": "The True Wealth of a Nation",
        "body": "Is a country wealthy because it has a lot of gold, or because its citizens are educated and healthy? \n\nPhysical capital (like machines and factories) is useless without human intelligence to operate it. This is why economists argue that investing in Education, Health, and Skill Development—known as **Human Capital Formation**—is the ultimate driver of long-term economic growth. You are not just a student; you are India's future human capital!"
    },
    {
        "id": "CBSE_CLASS12_ECO_CH7_002",
        "type": "theory",
        "title": "The Challenge of Employment",
        "body": "In recent years (up to 2026), India has experienced strong GDP growth, but economists are worried about 'Jobless Growth'. This happens when the economy produces more goods and services, but without creating a proportionate number of new jobs.\n\nFurthermore, over 80% of India's workforce is engaged in the **Informal Sector** (like street vendors, daily wage labourers, or small farmers). These workers lack job security, pensions, and social safety nets, making them highly vulnerable."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH7_003",
        "type": "mcq",
        "question": "Which of the following best describes 'Jobless Growth'?",
        "options": [
            "When unemployment increases but GDP decreases.",
            "When the level of output (GDP) increases without a corresponding increase in employment.",
            "When everyone has a job but their salaries are very low.",
            "When the government bans the use of machines in factories."
        ],
        "correct_index": 1,
        "explanation": "Jobless growth refers to a situation where an economy's GDP grows primarily due to better technology or productivity, but it fails to generate adequate new employment opportunities for the growing workforce."
    }
]

# CHAPTER 8: Development Experience of India - A Comparison with Neighbours
ch8_metadata = {
    "id": "cbse_class12_economics_ch8",
    "title": "Chapter 8: Development Experience of India - A Comparison with Neighbours",
    "title_hi": "अध्याय 8: भारत का विकास अनुभव - पड़ोसियों के साथ तुलना",
    "title_gu": "પ્રકરણ 8: ભારતનો વિકાસ અનુભવ - પડોશીઓ સાથે તુલના",
    "subject": "Economics",
    "class": "Class 12",
    "board": "CBSE"
}

ch8_blocks = [
    {
        "id": "CBSE_CLASS12_ECO_CH8_001",
        "type": "theory",
        "title": "The Asian Giants: India, China, and Pakistan",
        "body": "India, Pakistan, and China started their modern developmental journey at almost the same time. India and Pakistan became independent in 1947, and the People's Republic of China was established in 1949. All three relied on Five-Year Plans initially. \n\nHowever, their paths drastically diverged. Today, China's economy is a global powerhouse, far larger than India's, while Pakistan faces severe economic crises. How did three nations that started at the same starting line end up in such different places?"
    },
    {
        "id": "CBSE_CLASS12_ECO_CH8_002",
        "type": "theory",
        "title": "China's Secret to Rapid Growth",
        "body": "China's explosive growth can be traced back to its bold economic reforms introduced in 1978 (much earlier than India's 1991 reforms). \n\nKey drivers included:\n1. **Special Economic Zones (SEZs):** Areas set up with flexible laws to attract foreign investors.\n2. **Township and Village Enterprises (TVEs):** Encouraging local industrial production.\n3. **Dual Pricing:** In agriculture, farmers had to sell a fixed quota to the government but could sell the surplus at market prices, heavily incentivizing production."
    },
    {
        "id": "CBSE_CLASS12_ECO_CH8_003",
        "type": "mcq",
        "question": "Which demographic policy did China implement in 1979 that drastically slowed its population growth (but also led to a rapidly aging population later)?",
        "options": [
            "The Make in China Policy",
            "The Great Leap Forward",
            "The One-Child Policy",
            "The Cultural Revolution"
        ],
        "correct_index": 2,
        "explanation": "The One-Child Policy, implemented in 1979, was a strict population control measure. While it successfully curbed population growth, it has resulted in a declining workforce and an aging population, prompting China to relax it to a two-child (and later three-child) policy."
    }
]

if __name__ == "__main__":
    process_chapter({"metadata": ch6_metadata, "blocks": ch6_blocks})
    process_chapter({"metadata": ch7_metadata, "blocks": ch7_blocks})
    process_chapter({"metadata": ch8_metadata, "blocks": ch8_blocks})
