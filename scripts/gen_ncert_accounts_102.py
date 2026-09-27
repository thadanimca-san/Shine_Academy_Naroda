import os
import json

CHAPTERS_DIR = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
FILE_PATH = os.path.join(CHAPTERS_DIR, 'ncert_class12_accounts_leac102.json')

blocks = [
    {
        "id": "KOBJ_LEAC102_HOOK_1",
        "type": "hook",
        "title": "Admitting a New Partner: The Pizza Analogy",
        "title_hi": "नए साझेदार का प्रवेश: पिज्जा का उदाहरण",
        "title_gu": "નવા ભાગીદારનો પ્રવેશ: પિઝાનું ઉદાહરણ",
        "body": "Imagine you and your friend own a pizza (the firm's profit). You each get 50%. Suddenly, a third friend joins. To give the new friend a slice, you both have to sacrifice a piece of your pizza. This is exactly what happens when a new partner is admitted into an accounting firm. But it's not just profit—assets and liabilities also need to be revalued before the new partner steps in. Let's see how this looks in the books of accounts!",
        "body_hi": "कल्पना करें कि आप और आपका दोस्त एक पिज्जा (फर्म का लाभ) के मालिक हैं। आप प्रत्येक को 50% मिलता है। अचानक, एक तीसरा दोस्त शामिल हो जाता है। नए दोस्त को एक टुकड़ा देने के लिए, आप दोनों को अपने पिज्जा के एक टुकड़े का त्याग करना होगा। बिल्कुल ऐसा ही तब होता है जब एक नए साझेदार को अकाउंटिंग फर्म में प्रवेश दिया जाता है। लेकिन यह सिर्फ लाभ नहीं है - नए साझेदार के कदम रखने से पहले संपत्ति और देनदारियों का पुनर्मूल्यांकन भी किया जाना चाहिए। आइए देखें कि यह खातों की किताबों में कैसा दिखता है!",
        "body_gu": "કલ્પના કરો કે તમે અને તમારો મિત્ર પિઝા (પેઢીનો નફો) ની માલિકી ધરાવો છો. તમને દરેકને 50% મળે છે. અચાનક, ત્રીજો મિત્ર જોડાય છે. નવા મિત્રને એક ટુકડો આપવા માટે, તમારે બંનેએ તમારા પિઝાના ટુકડાનું બલિદાન આપવું પડશે. બરાબર આવું જ ત્યારે થાય છે જ્યારે નવા ભાગીદારને પેઢીમાં પ્રવેશ આપવામાં આવે છે. પરંતુ આ માત્ર નફો નથી - નવા ભાગીદાર આવે તે પહેલા મિલકતો અને દેવાઓનું પણ પુનઃમૂલ્યાંકન કરવાની જરૂર છે. ચાલો જોઈએ કે હિસાબી ચોપડામાં આ કેવું દેખાય છે!"
    },
    {
        "id": "KOBJ_LEAC102_PROB_1",
        "type": "theory",
        "title": "Comprehensive Illustration: Admission of a Partner",
        "title_hi": "व्यापक चित्रण: साझेदार का प्रवेश",
        "title_gu": "વ્યાપક ઉદાહરણ: ભાગીદારનો પ્રવેશ",
        "body": "A and B are partners sharing profits in the ratio of 3:2. Their Balance Sheet as on 31st March 2023 was as follows:\n\n**Balance Sheet of A and B**\n\n| Liabilities | Amount (₹) | Assets | Amount (₹) |\n| :--- | :--- | :--- | :--- |\n| Creditors | 40,000 | Cash at Bank | 20,000 |\n| General Reserve | 10,000 | Debtors | 30,000 |\n| Capital: A | 60,000 | Stock | 40,000 |\n| Capital: B | 40,000 | Machinery | 60,000 |\n| **Total** | **1,50,000** | **Total** | **1,50,000** |\n\nThey admitted C as a new partner on 1st April 2023 for 1/5th share in future profits on the following terms:\n1. C will bring ₹40,000 as his capital and ₹15,000 for his share of Goodwill in cash.\n2. Machinery is to be depreciated by 10%.\n3. Stock is revalued at ₹45,000.\n4. A provision for doubtful debts is to be created @ 5% on Debtors.\n\n**Prepare Revaluation Account, Partners' Capital Accounts, and the Balance Sheet of the new firm.**",
        "body_hi": "A और B 3:2 के अनुपात में लाभ बांटने वाले साझेदार हैं। 31 मार्च 2023 को उनका बैलेंस शीट इस प्रकार था:\n\n(अंग्रेजी तालिका देखें)\n\nउन्होंने 1 अप्रैल 2023 को भविष्य के लाभ में 1/5 हिस्से के लिए C को नए साझेदार के रूप में भर्ती किया:\n1. C अपनी पूंजी के रूप में ₹40,000 और अपनी ख्याति (Goodwill) के लिए ₹15,000 नकद लाएगा।\n2. मशीनरी का 10% मूल्यह्रास किया जाना है।\n3. स्टॉक का पुनर्मूल्यांकन ₹45,000 पर किया गया है।\n4. देनदारों (Debtors) पर 5% की दर से संदिग्ध ऋणों के लिए प्रावधान किया जाना है।\n\n**पुनर्मूल्यांकन खाता, पार्टनर्स के पूंजी खाते और नई फर्म की बैलेंस शीट तैयार करें।**",
        "body_gu": "A અને B 3:2 ના પ્રમાણમાં નફો વહેંચતા ભાગીદારો છે. 31 માર્ચ 2023 ના રોજ તેમનું પાકું સરવૈયું નીચે મુજબ હતું:\n\n(અંગ્રેજી કોષ્ટક જુઓ)\n\nતેમણે 1 એપ્રિલ 2023 ના રોજ ભવિષ્યના નફામાં 1/5 ભાગ માટે C ને નવા ભાગીદાર તરીકે પ્રવેશ આપ્યો:\n1. C તેની મૂડી તરીકે ₹40,000 અને તેની પાઘડી (Goodwill) ના ભાગ માટે ₹15,000 રોકડમાં લાવશે.\n2. મશીનરી પર 10% ઘસારો ગણવાનો છે.\n3. સ્ટોકનું પુનઃમૂલ્યાંકન ₹45,000 કરવામાં આવ્યું છે.\n4. દેવાદારો (Debtors) પર 5% ના દરે શકમંદ લેણા અનામત ઊભી કરવાની છે.\n\n**પુનઃમૂલ્યાંકન ખાતું, ભાગીદારોના મૂડી ખાતા અને નવી પેઢીનું પાકું સરવૈયું તૈયાર કરો.**"
    },
    {
        "id": "KOBJ_LEAC102_SOL_1_REV",
        "type": "markdown_table",
        "title": "Solution: Revaluation Account",
        "title_hi": "समाधान: पुनर्मूल्यांकन खाता",
        "title_gu": "ઉકેલ: પુનઃમૂલ્યાંકન ખાતું",
        "table_markdown": "| Particulars (Dr.) | Amount (₹) | Particulars (Cr.) | Amount (₹) |\n| :--- | :--- | :--- | :--- |\n| To Machinery A/c (10% of 60k) | 6,000 | By Stock A/c (45k - 40k) | 5,000 |\n| To Provision for Bad Debts (5% of 30k) | 1,500 | By Loss trf to Capital A/cs: | |\n| | | A (3/5) : 1,500 | |\n| | | B (2/5) : 1,000 | 2,500 |\n| **Total** | **7,500** | **Total** | **7,500** |"
    },
    {
        "id": "KOBJ_LEAC102_SOL_1_CAP",
        "type": "markdown_table",
        "title": "Solution: Partners' Capital Accounts",
        "title_hi": "समाधान: पार्टनर्स के पूंजी खाते",
        "title_gu": "ઉકેલ: ભાગીદારોના મૂડી ખાતા",
        "table_markdown": "| Particulars (Dr.) | A (₹) | B (₹) | C (₹) | Particulars (Cr.) | A (₹) | B (₹) | C (₹) |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n| To Revaluation A/c (Loss) | 1,500 | 1,000 | - | By Balance b/d | 60,000 | 40,000 | - |\n| To Balance c/d | 73,500 | 49,000 | 40,000 | By General Reserve (3:2) | 6,000 | 4,000 | - |\n| | | | | By Cash A/c (Capital) | - | - | 40,000 |\n| | | | | By Premium for Goodwill | 9,000 | 6,000 | - |\n| **Total** | **75,000** | **50,000** | **40,000** | **Total** | **75,000** | **50,000** | **40,000** |"
    },
    {
        "id": "KOBJ_LEAC102_SOL_1_BS",
        "type": "markdown_table",
        "title": "Solution: Balance Sheet of the New Firm",
        "title_hi": "समाधान: नई फर्म की बैलेंस शीट",
        "title_gu": "ઉકેલ: નવી પેઢીનું પાકું સરવૈયું",
        "table_markdown": "| Liabilities | Amount (₹) | Assets | Amount (₹) |\n| :--- | :--- | :--- | :--- |\n| Creditors | 40,000 | Cash at Bank (20k+40k+15k) | 75,000 |\n| **Capital Accounts:** | | Debtors (30k - 1,500) | 28,500 |\n| A : 73,500 | | Stock (Revalued) | 45,000 |\n| B : 49,000 | | Machinery (60k - 6k) | 54,000 |\n| C : 40,000 | 1,62,500 | | |\n| **Total** | **2,02,500** | **Total** | **2,02,500** |"
    },
    {
        "id": "KOBJ_LEAC102_MCQ_1",
        "type": "mcq",
        "question": "In the above problem, why was the Premium for Goodwill (₹15,000) divided as A: ₹9,000 and B: ₹6,000?",
        "question_hi": "उपरोक्त समस्या में, ख्याति के लिए प्रीमियम (₹15,000) को A: ₹9,000 और B: ₹6,000 के रूप में क्यों विभाजित किया गया था?",
        "question_gu": "ઉપરોક્ત સમસ્યામાં, પાઘડી માટેના પ્રીમિયમ (₹15,000) ને A: ₹9,000 અને B: ₹6,000 તરીકે શા માટે વહેંચવામાં આવ્યું?",
        "options": [
            "It is divided in the sacrificing ratio, which is equal to their old ratio (3:2) since no other information is given.",
            "It is divided equally among old partners.",
            "It is given to the partner with the highest capital.",
            "It is kept in the bank and not distributed."
        ],
        "options_hi": [
            "इसे त्याग अनुपात में विभाजित किया जाता है, जो उनके पुराने अनुपात (3:2) के बराबर है क्योंकि कोई अन्य जानकारी नहीं दी गई है।",
            "इसे पुराने भागीदारों के बीच समान रूप से विभाजित किया जाता है।",
            "यह उच्चतम पूंजी वाले भागीदार को दिया जाता है।",
            "इसे बैंक में रखा जाता है और वितरित नहीं किया जाता है।"
        ],
        "options_gu": [
            "તે ત્યાગના પ્રમાણમાં વહેંચવામાં આવે છે, જે તેમના જૂના પ્રમાણ (3:2) જેટલું છે કારણ કે અન્ય કોઈ માહિતી આપવામાં આવી નથી.",
            "તે જૂના ભાગીદારો વચ્ચે સમાન રીતે વહેંચવામાં આવે છે.",
            "તે સૌથી વધુ મૂડી ધરાવતા ભાગીદારને આપવામાં આવે છે.",
            "તે બેંકમાં રાખવામાં આવે છે અને વહેંચવામાં આવતું નથી."
        ],
        "correct_index": 0,
        "explanation": "When new profit sharing ratio is not given, the old ratio becomes the sacrificing ratio. Thus, 15,000 is distributed in 3:2.",
        "explanation_hi": "जब नया लाभ विभाजन अनुपात नहीं दिया जाता है, तो पुराना अनुपात ही त्याग अनुपात बन जाता है। इस प्रकार, 15,000 को 3:2 में वितरित किया जाता है।",
        "explanation_gu": "જ્યારે નવો નફા નુકસાનનું પ્રમાણ આપવામાં આવતું નથી, ત્યારે જૂનું પ્રમાણ જ ત્યાગનું પ્રમાણ બની જાય છે. આમ, 15,000 ને 3:2 માં વહેંચવામાં આવે છે."
    }
]

full_json = {
    "metadata": {
        "id": "ncert_class12_accounts_leac102",
        "title": "Accountancy - Admission of a Partner",
        "subject": "Accountancy",
        "grade": "12",
        "curriculum": ["NCERT", "CBSE"],
        "difficulty": "Advanced",
        "estimated_minutes": 60
    },
    "blocks": blocks
}

with open(FILE_PATH, "w", encoding="utf-8") as f:
    json.dump(full_json, f, indent=2, ensure_ascii=False)
    f.write("\n")
print(f"Generated {FILE_PATH} with numerical solution and markdown_table!")
