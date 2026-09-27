import json
import os

chapter_data = {
    "id": "GSEB_CLASS12_ACC_CH13",
    "title": "Cash Flow Statement",
    "title_hi": "नकद प्रवाह विवरण",
    "title_gu": "રોકડ પ્રવાહ પત્રક",
    "subtitle": "Chapter 13",
    "subject": "Accounts",
    "grade": 12,
    "board": "GSEB",
    "curriculum": ["GSEB"],
    "language": "English",
    "difficulty": "Intermediate",
    "estimated_minutes": 180,
    "version": "2.0.0",
    "blocks": []
}

def add_block(block):
    chapter_data["blocks"].append(block)

# ==========================================
# 1. SOCRATIC DISCOVERY ARC - THEORY CONCEPT
# ==========================================
# Step 1: Hook
add_block({
    "id": "GSEB_CLASS12_ACC_CH13_HOOK",
    "type": "teacher_tip",
    "title": "A Missing Piece of the Puzzle",
    "title_hi": "पहेली का एक गायब टुकड़ा",
    "title_gu": "કોયડાનો એક ખૂટતો ટુકડો",
    "body": "Imagine a company making Rs 10 Lakhs in profit, but when the owner goes to pay salaries, the bank account is empty! How is this possible? Profit doesn't always equal cash. Let's find out where the cash went.",
    "body_hi": "कल्पना करें कि एक कंपनी 10 लाख रुपये का मुनाफा कमा रही है, लेकिन जब मालिक वेतन का भुगतान करने जाता है, तो बैंक खाता खाली होता है! यह कैसे संभव है? लाभ हमेशा नकद के बराबर नहीं होता। आइए पता करें कि नकद कहाँ गया।",
    "body_gu": "કલ્પના કરો કે એક કંપની 10 લાખ રૂપિયાનો નફો કરી રહી છે, પરંતુ જ્યારે માલિક પગાર ચૂકવવા જાય છે, ત્યારે બેંક ખાતું ખાલી હોય છે! આ કેવી રીતે શક્ય છે? નફો હંમેશા રોકડ સમાન હોતો નથી. ચાલો શોધીએ કે રોકડ ક્યાં ગઈ.",
    "difficulty": "Beginner",
    "estimated_minutes": 2,
    "bloom": "Understand"
})

# Step 2: Socratic Thinking
add_block({
    "id": "GSEB_CLASS12_ACC_CH13_SOCRATIC",
    "type": "theory",
    "title": "Why isn't Profit = Cash?",
    "title_hi": "लाभ = नकद क्यों नहीं है?",
    "title_gu": "નફો = રોકડ શા માટે નથી?",
    "body": "Think about it: If you sell goods on credit, it shows as revenue (and profit) in your P&L statement, but have you actually received the cash yet? What happens when you buy a large machine for cash? It reduces your bank balance, but does it reduce your profit immediately?",
    "body_hi": "इसके बारे में सोचें: यदि आप क्रेडिट पर माल बेचते हैं, तो यह आपके पी एंड एल विवरण में राजस्व (और लाभ) के रूप में दिखाता है, लेकिन क्या आपको वास्तव में अभी तक नकद प्राप्त हुआ है? क्या होता है जब आप नकद के लिए एक बड़ी मशीन खरीदते हैं? यह आपके बैंक बैलेंस को कम करता है, लेकिन क्या यह आपके लाभ को तुरंत कम करता है?",
    "body_gu": "તેના વિશે વિચારો: જો તમે ક્રેડિટ પર માલ વેચો છો, તો તે તમારા P&L સ્ટેટમેન્ટમાં આવક (અને નફો) તરીકે દર્શાવે છે, પરંતુ શું તમને ખરેખર રોકડ મળી છે? જ્યારે તમે રોકડ માટે એક મોટું મશીન ખરીદો છો ત્યારે શું થાય છે? તે તમારું બેંક બેલેન્સ ઘટાડે છે, પરંતુ શું તે તમારા નફાને તરત જ ઘટાડે છે?",
    "difficulty": "Intermediate",
    "estimated_minutes": 3,
    "bloom": "Analyze"
})

# Step 3: Discovery
add_block({
    "id": "GSEB_CLASS12_ACC_CH13_DISCOVERY",
    "type": "real_world_example",
    "title": "Tracing the Flow of Money",
    "title_hi": "पैसे के प्रवाह का पता लगाना",
    "title_gu": "પૈસાના પ્રવાહને ટ્રેક કરવું",
    "body": "In business, money flows in three main ways: from daily operations (selling goods), from investments (buying/selling assets), and from financing (taking loans or issuing shares). Understanding these three streams is essential for survival.",
    "body_hi": "व्यापार में, पैसा तीन मुख्य तरीकों से बहता है: दैनिक संचालन (माल बेचना) से, निवेश (संपत्ति खरीदना/बेचना) से, और वित्तपोषण (ऋण लेना या शेयर जारी करना) से। जीवित रहने के लिए इन तीन धाराओं को समझना आवश्यक है।",
    "body_gu": "વ્યવસાયમાં, પૈસા ત્રણ મુખ્ય રીતે વહે છે: દૈનિક કામગીરી (માલ વેચવા) થી, રોકાણ (સંપત્તિ ખરીદવા/વેચવા) થી, અને ધિરાણ (લોન લેવા અથવા શેર બહાર પાડવા) થી. અસ્તિત્વ માટે આ ત્રણ પ્રવાહોને સમજવું આવશ્યક છે.",
    "difficulty": "Intermediate",
    "estimated_minutes": 4,
    "bloom": "Understand"
})

# Step 4: Reveal
add_block({
    "id": "GSEB_CLASS12_ACC_CH13_REVEAL",
    "type": "definition",
    "title": "The Cash Flow Statement",
    "title_hi": "नकद प्रवाह विवरण",
    "title_gu": "રોકડ પ્રવાહ પત્રક",
    "body": "A Cash Flow Statement is a financial statement that shows the changes in cash and cash equivalents of an enterprise during a specified period. It classifies cash flows into Operating, Investing, and Financing activities as per Accounting Standard 3.",
    "body_hi": "नकद प्रवाह विवरण एक वित्तीय विवरण है जो किसी निर्दिष्ट अवधि के दौरान किसी उद्यम की नकदी और नकद समकक्षों में परिवर्तन दिखाता है। यह लेखा मानक 3 के अनुसार नकद प्रवाह को संचालन, निवेश और वित्तपोषण गतिविधियों में वर्गीकृत करता है।",
    "body_gu": "કેશ ફ્લો સ્ટેટમેન્ટ એ એક નાણાકીય નિવેદન છે જે નિર્દિષ્ટ સમયગાળા દરમિયાન એન્ટરપ્રાઇઝના રોકડ અને રોકડ સમકક્ષોમાં ફેરફાર દર્શાવે છે. તે એકાઉન્ટિંગ સ્ટાન્ડર્ડ 3 મુજબ ઓપરેટિંગ, રોકાણ અને ધિરાણ પ્રવૃત્તિઓમાં રોકડ પ્રવાહનું વર્ગીકરણ કરે છે.",
    "difficulty": "Beginner",
    "estimated_minutes": 5,
    "bloom": "Remember"
})

# Step 5: Knowledge Check
add_block({
    "id": "GSEB_CLASS12_ACC_CH13_CHECK1",
    "type": "mcq",
    "question": "Which accounting standard governs the preparation of the Cash Flow Statement in India?",
    "question_hi": "भारत में नकद प्रवाह विवरण तैयार करने को कौन सा लेखा मानक नियंत्रित करता है?",
    "question_gu": "ભારતમાં કેશ ફ્લો સ્ટેટમેન્ટની તૈયારીને કયું એકાઉન્ટિંગ સ્ટાન્ડર્ડ સંચાલિત કરે છે?",
    "options": ["Accounting Standard 1", "Accounting Standard 2", "Accounting Standard 3", "Accounting Standard 9"],
    "options_hi": ["लेखा मानक 1", "लेखा मानक 2", "लेखा मानक 3", "लेखा मानक 9"],
    "options_gu": ["એકાઉન્ટિંગ સ્ટાન્ડર્ડ 1", "એકાઉન્ટિંગ સ્ટાન્ડર્ડ 2", "એકાઉન્ટિંગ સ્ટાન્ડર્ડ 3", "એકાઉન્ટિંગ સ્ટાન્ડર્ડ 9"],
    "correct_index": 2,
    "explanation": "Accounting Standard 3 (AS-3) governs the preparation and presentation of the Cash Flow Statement.",
    "explanation_hi": "लेखा मानक 3 (AS-3) नकद प्रवाह विवरण की तैयारी और प्रस्तुति को नियंत्रित करता है।",
    "explanation_gu": "એકાઉન્ટિંગ સ્ટાન્ડર્ડ 3 (AS-3) રોકડ પ્રવાહ નિવેદનની તૈયારી અને પ્રસ્તુતિને સંચાલિત કરે છે.",
    "difficulty": "Beginner",
    "estimated_minutes": 1,
    "bloom": "Remember"
})

# Step 6: Reflection
add_block({
    "id": "GSEB_CLASS12_ACC_CH13_REFLECTION",
    "type": "reflection",
    "title": "Explain it in your own words",
    "title_hi": "इसे अपने शब्दों में समझाएं",
    "title_gu": "તેને તમારા પોતાના શબ્દોમાં સમજાવો",
    "body": "If you had to explain the difference between the Profit & Loss Statement and the Cash Flow Statement to a friend starting a business, what would you say? Think about it for a minute.",
    "body_hi": "यदि आपको किसी ऐसे मित्र को लाभ और हानि विवरण और नकद प्रवाह विवरण के बीच का अंतर समझाना पड़े जो व्यवसाय शुरू कर रहा है, तो आप क्या कहेंगे? एक मिनट इसके बारे में सोचें।",
    "body_gu": "જો તમારે વ્યવસાય શરૂ કરતા મિત્રને નફો અને નુકસાન નિવેદન અને રોકડ પ્રવાહ નિવેદન વચ્ચેનો તફાવત સમજાવવો હોય, તો તમે શું કહેશો? એક મિનિટ તેના વિશે વિચારો.",
    "difficulty": "Intermediate",
    "estimated_minutes": 3,
    "bloom": "Analyze"
})

# Step 7: Connection
add_block({
    "id": "GSEB_CLASS12_ACC_CH13_CONNECTION",
    "type": "theory",
    "title": "Connecting to the Balance Sheet",
    "title_hi": "बैलेंस शीट से जुड़ना",
    "title_gu": "બેલેન્સ શીટ સાથે જોડાઈ રહ્યું છે",
    "body": "The Cash Flow Statement acts as a bridge between two balance sheets. The opening cash balance plus the net cash flow generated during the year exactly equals the closing cash balance shown on the current year's balance sheet.",
    "body_hi": "नकद प्रवाह विवरण दो बैलेंस शीट के बीच एक पुल के रूप में कार्य करता है। शुरुआती नकद शेष और वर्ष के दौरान उत्पन्न शुद्ध नकद प्रवाह वर्तमान वर्ष की बैलेंस शीट पर दिखाए गए अंतिम नकद शेष के बिल्कुल बराबर होता है।",
    "body_gu": "રોકડ પ્રવાહ પત્રક બે બેલેન્સ શીટ વચ્ચેના સેતુ તરીકે કામ કરે છે. શરૂઆતની રોકડ બેલેન્સ વત્તા વર્ષ દરમિયાન જનરેટ થયેલ ચોખ્ખી રોકડ પ્રવાહ વર્તમાન વર્ષની બેલેન્સ શીટ પર દર્શાવેલ બંધ રોકડ બેલેન્સની બરાબર છે.",
    "difficulty": "Intermediate",
    "estimated_minutes": 4,
    "bloom": "Understand"
})

# Step 8: Mastery
add_block({
    "id": "GSEB_CLASS12_ACC_CH13_MASTERY",
    "type": "practice_question",
    "title": "Mastery Challenge",
    "title_hi": "महारत चुनौती",
    "title_gu": "નિપુણતા પડકાર",
    "body": "Classify the following into Operating, Investing, or Financing activities: 1. Paying salaries. 2. Buying a machine. 3. Issuing equity shares.",
    "body_hi": "निम्नलिखित को संचालन, निवेश या वित्तपोषण गतिविधियों में वर्गीकृत करें: 1. वेतन का भुगतान। 2. मशीन खरीदना। 3. इक्विटी शेयर जारी करना।",
    "body_gu": "નીચેનાને ઓપરેટિંગ, ઇન્વેસ્ટિંગ અથવા ફાઇનાન્સિંગ પ્રવૃત્તિઓમાં વર્ગીકૃત કરો: 1. પગાર ચૂકવવો. 2. મશીન ખરીદવું. 3. ઇક્વિટી શેર જારી કરવા.",
    "difficulty": "Intermediate",
    "estimated_minutes": 5,
    "bloom": "Apply"
})

# ==========================================
# EXERCISES SECTION
# ==========================================

exercises = [
    {
        "id": "GSEB_CLASS12_ACC_CH13_EX_MCQ_1",
        "type": "mcq",
        "question": "How many activities are there in cash flow statement?",
        "question_hi": "नकद प्रवाह विवरण में कितनी गतिविधियाँ हैं?",
        "question_gu": "રોકડ પ્રવાહ પત્રકમાં કેટલી પ્રવૃત્તિઓ છે?",
        "options": ["Five", "Four", "Three", "Two"],
        "options_hi": ["पाँच", "चार", "तीन", "दो"],
        "options_gu": ["પાંચ", "ચાર", "ત્રણ", "બે"],
        "correct_index": 2,
        "explanation": "There are three activities in a cash flow statement: Operating, Investing, and Financing.",
        "explanation_hi": "नकद प्रवाह विवरण में तीन गतिविधियाँ हैं: संचालन, निवेश, और वित्तपोषण।",
        "explanation_gu": "રોકડ પ્રવાહ પત્રકમાં ત્રણ પ્રવૃત્તિઓ છે: ઓપરેટિંગ, ઇન્વેસ્ટિંગ અને ફાઇનાન્સિંગ.",
        "difficulty": "Beginner",
        "estimated_minutes": 1,
        "bloom": "Remember"
    },
    {
        "id": "GSEB_CLASS12_ACC_CH13_EX_MCQ_2",
        "type": "mcq",
        "question": "Cash equivalent has ......... :",
        "question_hi": "नकद समकक्ष के पास ......... है:",
        "question_gu": "રોકડ સમકક્ષમાં ......... છે:",
        "options": ["higher liquidity", "higher solvency", "higher profitability", "all of the above"],
        "options_hi": ["उच्च तरलता", "उच्च शोधन क्षमता", "उच्च लाभप्रदता", "उपरोक्त सभी"],
        "options_gu": ["ઉચ્ચ પ્રવાહિતા", "ઉચ્ચ સદ્ધરતા", "ઉચ્ચ નફાકારકતા", "ઉપરોક્ત તમામ"],
        "correct_index": 0,
        "explanation": "Cash equivalents are highly liquid investments that are readily convertible to known amounts of cash.",
        "explanation_hi": "नकद समकक्ष अत्यधिक तरल निवेश हैं जो आसानी से नकद की ज्ञात मात्रा में परिवर्तनीय हैं।",
        "explanation_gu": "રોકડ સમકક્ષ એ અત્યંત પ્રવાહી રોકાણો છે જે રોકડની જાણીતી રકમમાં સરળતાથી રૂપાંતરિત થાય છે.",
        "difficulty": "Beginner",
        "estimated_minutes": 1,
        "bloom": "Remember"
    },
    {
        "id": "GSEB_CLASS12_ACC_CH13_EX_MCQ_3",
        "type": "mcq",
        "question": "Decrease in current assets and increase in current liabilities .......... :",
        "question_hi": "वर्तमान संपत्तियों में कमी और वर्तमान देनदारियों में वृद्धि .......... :",
        "question_gu": "વર્તમાન અસ્કયામતોમાં ઘટાડો અને વર્તમાન જવાબદારીઓમાં વધારો .......... :",
        "options": ["are cash inflow and cash outflow respectively", "are cash outflow and cash inflow respectively", "both are cash inflows", "both are cash outflows"],
        "options_hi": ["क्रमशः नकद प्रवाह और नकद बहिर्वाह हैं", "क्रमशः नकद बहिर्वाह और नकद प्रवाह हैं", "दोनों नकद प्रवाह हैं", "दोनों नकद बहिर्वाह हैं"],
        "options_gu": ["અનુક્રમે રોકડ પ્રવાહ અને રોકડ પ્રવાહ છે", "અનુક્રમે રોકડ આઉટફ્લો અને કેશ ઇનફ્લો છે", "બંને રોકડ પ્રવાહ છે", "બંને રોકડ પ્રવાહ છે"],
        "correct_index": 2,
        "explanation": "Both result in a positive adjustment (inflow) to operating cash flows under the indirect method.",
        "explanation_hi": "अप्रत्यक्ष विधि के तहत दोनों का परिणाम परिचालन नकद प्रवाह में सकारात्मक समायोजन (प्रवाह) होता है।",
        "explanation_gu": "પરોક્ષ પદ્ધતિ હેઠળ ઓપરેટિંગ રોકડ પ્રવાહમાં સકારાત્મક ગોઠવણ (ઇનફ્લો) બંને પરિણમે છે.",
        "difficulty": "Intermediate",
        "estimated_minutes": 1,
        "bloom": "Understand"
    },
    {
        "id": "GSEB_CLASS12_ACC_CH13_EX_MCQ_4",
        "type": "mcq",
        "question": "Increased in current assets and decrease in current liabilities ......... :",
        "question_hi": "वर्तमान संपत्तियों में वृद्धि और वर्तमान देनदारियों में कमी ......... :",
        "question_gu": "વર્તમાન અસ્કયામતોમાં વધારો અને વર્તમાન જવાબદારીઓમાં ઘટાડો ......... :",
        "options": ["both are cash outflows", "both are cash inflows", "are cash outflow and cash inflow respectively", "are cash inflow and cash outflow respectively"],
        "options_hi": ["दोनों नकद बहिर्वाह हैं", "दोनों नकद प्रवाह हैं", "क्रमशः नकद बहिर्वाह और नकद प्रवाह हैं", "क्रमशः नकद प्रवाह और नकद बहिर्वाह हैं"],
        "options_gu": ["બંને રોકડ આઉટફ્લો છે", "બંને રોકડ પ્રવાહ છે", "અનુક્રમે રોકડ આઉટફ્લો અને કેશ ઇનફ્લો છે", "અનુક્રમે રોકડ ઇનફ્લો અને રોકડ આઉટફ્લો છે"],
        "correct_index": 0,
        "explanation": "Both result in a negative adjustment (outflow) to operating cash flows under the indirect method.",
        "explanation_hi": "अप्रत्यक्ष विधि के तहत दोनों का परिणाम परिचालन नकद प्रवाह में नकारात्मक समायोजन (बहिर्वाह) होता है।",
        "explanation_gu": "પરોક્ષ પદ્ધતિ હેઠળ ઓપરેટિંગ રોકડ પ્રવાહમાં નકારાત્મક ગોઠવણ (આઉટફ્લો) બંને પરિણમે છે.",
        "difficulty": "Intermediate",
        "estimated_minutes": 1,
        "bloom": "Understand"
    },
    {
        "id": "GSEB_CLASS12_ACC_CH13_EX_MCQ_5",
        "type": "mcq",
        "question": "Collection of debtors and bills receivable is ......... :",
        "question_hi": "देनदारों और प्राप्य बिलों का संग्रह ......... है :",
        "question_gu": "દેવાદારો અને લેણાં બિલોનો સંગ્રહ ......... છે :",
        "options": ["cash inflow of operating activity", "cash outflow of operating activity", "cash inflow of financing activity", "cash inflow of investing activity"],
        "options_hi": ["परिचालन गतिविधि का नकद प्रवाह", "परिचालन गतिविधि का नकद बहिर्वाह", "वित्तपोषण गतिविधि का नकद प्रवाह", "निवेश गतिविधि का नकद प्रवाह"],
        "options_gu": ["ઓપરેટિંગ પ્રવૃત્તિનો રોકડ પ્રવાહ", "ઓપરેટિંગ પ્રવૃત્તિના રોકડ આઉટફ્લો", "ધિરાણ પ્રવૃત્તિનો રોકડ પ્રવાહ", "રોકાણ પ્રવૃત્તિનો રોકડ પ્રવાહ"],
        "correct_index": 0,
        "explanation": "Collecting money from customers (debtors) is a principal revenue-producing activity, hence an operating cash inflow.",
        "explanation_hi": "ग्राहकों (देनदारों) से धन एकत्र करना एक प्रमुख राजस्व-उत्पादक गतिविधि है, इसलिए यह एक परिचालन नकद प्रवाह है।",
        "explanation_gu": "ગ્રાહકો (દેવાદારો) પાસેથી નાણાં એકત્ર કરવા એ મુખ્ય આવક-ઉત્પાદક પ્રવૃત્તિ છે, તેથી તે ઓપરેટિંગ રોકડ પ્રવાહ છે.",
        "difficulty": "Intermediate",
        "estimated_minutes": 1,
        "bloom": "Understand"
    },
    {
        "id": "GSEB_CLASS12_ACC_CH13_EX_MCQ_6",
        "type": "mcq",
        "question": "Which of the following transaction is always transaction of operating activity?",
        "question_hi": "निम्नलिखित में से कौन सा लेनदेन हमेशा परिचालन गतिविधि का लेनदेन होता है?",
        "question_gu": "નીચેનામાંથી કયો વ્યવહાર હંમેશા ઓપરેટિંગ પ્રવૃત્તિનો વ્યવહાર છે?",
        "options": ["Interest paid on loan", "Dividend received", "Dividend paid", "Salary expense"],
        "options_hi": ["ऋण पर दिया गया ब्याज", "प्राप्त लाभांश", "भुगतान किया गया लाभांश", "वेतन व्यय"],
        "options_gu": ["લોન પર ચૂકવવામાં આવેલ વ્યાજ", "ડિવિડન્ડ મળ્યું", "ડિવિડન્ડ ચૂકવેલ", "પગાર ખર્ચ"],
        "correct_index": 3,
        "explanation": "Salary expense is a core day-to-day business operation, unlike interest or dividends which relate to financing/investing.",
        "explanation_hi": "वेतन व्यय एक मुख्य दैनिक व्यावसायिक संचालन है, ब्याज या लाभांश के विपरीत जो वित्तपोषण/निवेश से संबंधित हैं।",
        "explanation_gu": "પગાર ખર્ચ એ રોજિંદા વ્યવસાયિક કામગીરી છે, વ્યાજ અથવા ડિવિડન્ડથી વિપરીત જે ફાઇનાન્સિંગ/રોકાણ સાથે સંબંધિત છે.",
        "difficulty": "Beginner",
        "estimated_minutes": 1,
        "bloom": "Remember"
    },
    {
        "id": "GSEB_CLASS12_ACC_CH13_EX_MCQ_7",
        "type": "mcq",
        "question": "Dividend or interest received on investment is:",
        "question_hi": "निवेश पर प्राप्त लाभांश या ब्याज है:",
        "question_gu": "રોકાણ પર મળેલ ડિવિડન્ડ અથવા વ્યાજ છે:",
        "options": ["added to cash flow of operating activity", "deducted from cash flow of financing activity", "added to cash flow of investing activity", "deducted from cash flow of investing activity"],
        "options_hi": ["परिचालन गतिविधि के नकद प्रवाह में जोड़ा गया", "वित्तपोषण गतिविधि के नकद प्रवाह से घटाया गया", "निवेश गतिविधि के नकद प्रवाह में जोड़ा गया", "निवेश गतिविधि के नकद प्रवाह से घटाया गया"],
        "options_gu": ["ઓપરેટિંગ પ્રવૃત્તિના રોકડ પ્રવાહમાં ઉમેર્યું", "ફાઇનાન્સિંગ પ્રવૃત્તિના રોકડ પ્રવાહમાંથી બાદ કરવામાં આવે છે", "રોકાણ પ્રવૃત્તિના રોકડ પ્રવાહમાં ઉમેરવામાં આવે છે", "રોકાણ પ્રવૃત્તિના રોકડ પ્રવાહમાંથી બાદ કરવામાં આવે છે"],
        "correct_index": 2,
        "explanation": "Returns on investments (like dividends or interest) are inflows from investing activities for a non-financial enterprise.",
        "explanation_hi": "निवेश पर रिटर्न (जैसे लाभांश या ब्याज) एक गैर-वित्तीय उद्यम के लिए निवेश गतिविधियों से प्रवाह हैं।",
        "explanation_gu": "રોકાણો પર વળતર (જેમ કે ડિવિડન્ડ અથવા વ્યાજ) બિન-નાણાકીય એન્ટરપ્રાઇઝ માટે રોકાણ પ્રવૃત્તિઓમાંથી આવક છે.",
        "difficulty": "Intermediate",
        "estimated_minutes": 1,
        "bloom": "Understand"
    },
    {
        "id": "GSEB_CLASS12_ACC_CH13_EX_MCQ_8",
        "type": "mcq",
        "question": "Bank overdraft .........",
        "question_hi": "बैंक ओवरड्राफ्ट .........",
        "question_gu": "બેંક ઓવરડ્રાફ્ટ .........",
        "options": ["is current liability but considered as financing activity", "is current liability but considered as operating activity", "is current liability but considered as investing activity", "is not activity of cash flow statement"],
        "options_hi": ["वर्तमान देयता है लेकिन वित्तपोषण गतिविधि माना जाता है", "वर्तमान देयता है लेकिन परिचालन गतिविधि माना जाता है", "वर्तमान देयता है लेकिन निवेश गतिविधि माना जाता है", "नकद प्रवाह विवरण की गतिविधि नहीं है"],
        "options_gu": ["વર્તમાન જવાબદારી છે પરંતુ ફાઇનાન્સિંગ પ્રવૃત્તિ તરીકે ગણવામાં આવે છે", "વર્તમાન જવાબદારી છે પરંતુ ઓપરેટિંગ પ્રવૃત્તિ તરીકે ગણવામાં આવે છે", "વર્તમાન જવાબદારી છે પરંતુ રોકાણ પ્રવૃત્તિ તરીકે ગણવામાં આવે છે", "કેશ ફ્લો સ્ટેટમેન્ટની પ્રવૃત્તિ નથી"],
        "correct_index": 0,
        "explanation": "Bank overdraft is a short-term borrowing, hence it is part of financing activities despite being a current liability.",
        "explanation_hi": "बैंक ओवरड्राफ्ट एक अल्पकालिक उधार है, इसलिए वर्तमान देयता होने के बावजूद यह वित्तपोषण गतिविधियों का हिस्सा है।",
        "explanation_gu": "બેંક ઓવરડ્રાફ્ટ એ ટૂંકા ગાળાની ઉધાર છે, તેથી વર્તમાન જવાબદારી હોવા છતાં તે ધિરાણ પ્રવૃત્તિઓનો એક ભાગ છે.",
        "difficulty": "Intermediate",
        "estimated_minutes": 1,
        "bloom": "Understand"
    },
    {
        "id": "GSEB_CLASS12_ACC_CH13_EX_MCQ_9",
        "type": "mcq",
        "question": "Rent received ......... :",
        "question_hi": "प्राप्त किराया ......... :",
        "question_gu": "મળેલ ભાડું ......... :",
        "options": ["is added to operating activity and deducted from financing activity", "is added to operating activity and added to financing activity", "is added to operating activity and added to investing activity", "is deducted from operating activity and added to investing activity"],
        "options_hi": ["संचालन गतिविधि में जोड़ा जाता है और वित्तपोषण गतिविधि से काटा जाता है", "संचालन गतिविधि में जोड़ा जाता है और वित्तपोषण गतिविधि में जोड़ा जाता है", "संचालन गतिविधि में जोड़ा जाता है और निवेश गतिविधि में जोड़ा जाता है", "परिचालन गतिविधि से काटा जाता है और निवेश गतिविधि में जोड़ा जाता है"],
        "options_gu": ["ઓપરેટિંગ પ્રવૃત્તિમાં ઉમેરવામાં આવે છે અને ફાઇનાન્સિંગ પ્રવૃત્તિમાંથી કાપવામાં આવે છે", "ઓપરેટિંગ પ્રવૃત્તિમાં ઉમેરવામાં આવે છે અને ફાઇનાન્સિંગ પ્રવૃત્તિમાં ઉમેરવામાં આવે છે", "ઓપરેટિંગ પ્રવૃત્તિમાં ઉમેરવામાં આવે છે અને રોકાણ પ્રવૃત્તિમાં ઉમેરવામાં આવે છે", "ઓપરેટિંગ પ્રવૃત્તિમાંથી બાદ કરવામાં આવે છે અને રોકાણ પ્રવૃત્તિમાં ઉમેરવામાં આવે છે"],
        "correct_index": 3,
        "explanation": "Rent received is a non-operating income, so it is deducted from operating profits and shown as an inflow under investing activities.",
        "explanation_hi": "प्राप्त किराया एक गैर-परिचालन आय है, इसलिए इसे परिचालन लाभ से घटाया जाता है और निवेश गतिविधियों के तहत प्रवाह के रूप में दिखाया जाता है।",
        "explanation_gu": "મળેલ ભાડું એ બિન-ઓપરેટિંગ આવક છે, તેથી તે ઓપરેટિંગ નફામાંથી બાદ કરવામાં આવે છે અને રોકાણ પ્રવૃત્તિઓ હેઠળ પ્રવાહ તરીકે દર્શાવવામાં આવે છે.",
        "difficulty": "Advanced",
        "estimated_minutes": 2,
        "bloom": "Apply"
    },
    {
        "id": "GSEB_CLASS12_ACC_CH13_EX_MCQ_10",
        "type": "mcq",
        "question": "Reduction in goodwill in current year as compared to previous year is ......... :",
        "question_hi": "पिछले वर्ष की तुलना में चालू वर्ष में सद्भावना में कमी ......... है:",
        "question_gu": "અગાઉના વર્ષની સરખામણીમાં વર્તમાન વર્ષમાં ગુડવિલમાં ઘટાડો ......... :",
        "options": ["sale of goodwill", "purchase of goodwill", "written off goodwill", "all of the above"],
        "options_hi": ["सद्भावना की बिक्री", "सद्भावना की खरीद", "सद्भावना को बट्टे खाते में डालना", "उपरोक्त सभी"],
        "options_gu": ["ગુડવિલનું વેચાણ", "ગુડવિલની ખરીદી", "લેખિત ગુડવિલ", "ઉપરોક્ત તમામ"],
        "correct_index": 2,
        "explanation": "A decrease in goodwill is usually amortization (written off) unless it is explicitly sold.",
        "explanation_hi": "सद्भावना में कमी आमतौर पर परिशोधन (बट्टे खाते में डालना) होती है जब तक कि इसे स्पष्ट रूप से बेचा न जाए।",
        "explanation_gu": "ગુડવિલમાં ઘટાડો એ સામાન્ય રીતે ઋણમુક્તિ (રાઇટ ઓફ) છે સિવાય કે તે સ્પષ્ટપણે વેચાય.",
        "difficulty": "Intermediate",
        "estimated_minutes": 1,
        "bloom": "Understand"
    },
    {
        "id": "GSEB_CLASS12_ACC_CH13_EX_MCQ_11",
        "type": "mcq",
        "question": "Cash deposited in bank is ......... :",
        "question_hi": "बैंक में जमा की गई नकदी ......... है:",
        "question_gu": "બેંકમાં જમા થયેલ રોકડ ......... છે:",
        "options": ["cash outflow of operating activity", "cash outflow of financing activity", "cash outflow of investing activity", "not cash flow"],
        "options_hi": ["परिचालन गतिविधि का नकद बहिर्वाह", "वित्तपोषण गतिविधि का नकद बहिर्वाह", "निवेश गतिविधि का नकद बहिर्वाह", "नकद प्रवाह नहीं"],
        "options_gu": ["ઓપરેટિંગ પ્રવૃત્તિના રોકડ આઉટફ્લો", "ધિરાણ પ્રવૃત્તિનો રોકડ આઉટફ્લો", "રોકાણ પ્રવૃત્તિનો રોકડ આઉટફ્લો", "રોકડ પ્રવાહ નથી"],
        "correct_index": 3,
        "explanation": "Depositing cash into the bank just moves money between cash and cash equivalents; it does not change the total cash flow.",
        "explanation_hi": "बैंक में नकद जमा करने से केवल नकद और नकद समकक्षों के बीच पैसा चलता है; यह कुल नकद प्रवाह को नहीं बदलता है।",
        "explanation_gu": "બેંકમાં રોકડ જમા કરવાથી રોકડ અને રોકડ સમકક્ષ વચ્ચે નાણાં ખસે છે; તે કુલ રોકડ પ્રવાહમાં ફેરફાર કરતું નથી.",
        "difficulty": "Beginner",
        "estimated_minutes": 1,
        "bloom": "Remember"
    },
    {
        "id": "GSEB_CLASS12_ACC_CH13_EX_MCQ_12",
        "type": "mcq",
        "question": "Which of the following is included in financial expense?",
        "question_hi": "निम्नलिखित में से क्या वित्तीय व्यय में शामिल है?",
        "question_gu": "નીચેનામાંથી કોનો નાણાકીય ખર્ચમાં સમાવેશ થાય છે?",
        "options": ["Factory expenses", "Administrative expenses", "Sales expenses", "Interest expenses"],
        "options_hi": ["कारखाना व्यय", "प्रशासनिक व्यय", "बिक्री व्यय", "ब्याज व्यय"],
        "options_gu": ["ફેક્ટરી ખર્ચ", "વહીવટી ખર્ચ", "વેચાણ ખર્ચ", "વ્યાજ ખર્ચ"],
        "correct_index": 3,
        "explanation": "Interest paid on borrowed funds is a financial expense.",
        "explanation_hi": "उधार ली गई धनराशि पर दिया गया ब्याज एक वित्तीय व्यय है।",
        "explanation_gu": "ઉછીના ભંડોળ પર ચૂકવવામાં આવેલ વ્યાજ નાણાકીય ખર્ચ છે.",
        "difficulty": "Beginner",
        "estimated_minutes": 1,
        "bloom": "Remember"
    },
    {
        "id": "GSEB_CLASS12_ACC_CH13_EX_MCQ_13",
        "type": "mcq",
        "question": "Payment of interim dividend is ......... :",
        "question_hi": "अंतरिम लाभांश का भुगतान ......... है:",
        "question_gu": "વચગાળાના ડિવિડન્ડની ચુકવણી ......... છે:",
        "options": ["deducted from operating statement and added to financing activity", "deducted from operating statement and added to investing activity", "added to operating statement and deducted from financing activity", "none of the above"],
        "options_hi": ["परिचालन विवरण से घटाया गया और वित्तपोषण गतिविधि में जोड़ा गया", "परिचालन विवरण से घटाया गया और निवेश गतिविधि में जोड़ा गया", "परिचालन विवरण में जोड़ा गया और वित्तपोषण गतिविधि से काटा गया", "इनमें से कोई नहीं"],
        "options_gu": ["ઓપરેટિંગ સ્ટેટમેન્ટમાંથી બાદ કરવામાં આવે છે અને ફાઇનાન્સિંગ પ્રવૃત્તિમાં ઉમેરવામાં આવે છે", "ઓપરેટિંગ સ્ટેટમેન્ટમાંથી બાદ કરવામાં આવે છે અને રોકાણ પ્રવૃત્તિમાં ઉમેરવામાં આવે છે", "ઓપરેટિંગ સ્ટેટમેન્ટમાં ઉમેરવામાં આવે છે અને ફાઇનાન્સિંગ પ્રવૃત્તિમાંથી બાદ કરવામાં આવે છે", "ઉપરોક્તમાંથી કોઈ નહીં"],
        "correct_index": 2,
        "explanation": "Interim dividend paid is added back to net profit in operating activities (if previously deducted) and shown as an outflow under financing activities.",
        "explanation_hi": "भुगतान किया गया अंतरिम लाभांश परिचालन गतिविधियों में शुद्ध लाभ में वापस जोड़ा जाता है और वित्तपोषण गतिविधियों के तहत बहिर्वाह के रूप में दिखाया जाता है।",
        "explanation_gu": "ચૂકવેલ વચગાળાના ડિવિડન્ડ ઓપરેટિંગ પ્રવૃત્તિઓમાં ચોખ્ખા નફામાં પાછા ઉમેરવામાં આવે છે અને ફાઇનાન્સિંગ પ્રવૃત્તિઓ હેઠળ આઉટફ્લો તરીકે દર્શાવવામાં આવે છે.",
        "difficulty": "Advanced",
        "estimated_minutes": 2,
        "bloom": "Apply"
    }
]

# Write all exercises
for q in exercises:
    add_block(q)

# Write output to JSON
output_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_accounts_ch13.json'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(chapter_data, f, ensure_ascii=False, indent=2)

print(f"Generated successfully at {output_path}")
