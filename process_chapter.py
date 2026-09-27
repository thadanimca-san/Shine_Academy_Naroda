import json
import os
from datetime import datetime

# Destination file
OUTPUT_PATH = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_accounts_ch10.json"

# Translations for Universal Strings
def translate_hi(text):
    # Dummy translation for demonstration of concept when API is unavailable.
    # We provide real translations for hardcoded parts below.
    return text + " (Hindi)"

def translate_gu(text):
    return text + " (Gujarati)"

def main():
    chapter_data = {
        "id": "ACC_GSEB_12_CH10",
        "title": "Company Final Accounts",
        "title_hi": "कंपनी के अंतिम खाते",
        "title_gu": "કંપનીના અંતિમ હિસાબો",
        "subtitle": "Financial Statements of a Company as per Schedule III",
        "subtitle_hi": "अनुसूची III के अनुसार कंपनी के वित्तीय विवरण",
        "subtitle_gu": "શેડ્યૂલ III મુજબ કંપનીના નાણાકીય નિવેદનો",
        "subject": "Accounts",
        "grade": 12,
        "board": "GSEB",
        "curriculum": ["GSEB", "CBSE"],
        "language": "English",
        "difficulty": "Intermediate",
        "estimated_minutes": 180,
        "version": "1.0",
        "author": "Shine Academy",
        "reviewed_by": "System",
        "last_updated": datetime.utcnow().isoformat() + "Z",
        "tags": ["Company", "Final Accounts", "Balance Sheet", "Profit and Loss"],
        "learning_outcomes": [
            "Understand financial statements",
            "Prepare Balance Sheet",
            "Prepare Statement of Profit and Loss"
        ],
        "ai_context": {
            "learning_goal": "Master the preparation of company final accounts as per Companies Act, 2013.",
            "common_misconceptions": [
                "Treating provisions as reserves",
                "Incorrect classification of current vs non-current liabilities"
            ],
            "tutor_hint": "Remind students that Schedule III format is mandatory and strictly vertical.",
            "next_topics": []
        },
        "blocks": []
    }

    # Helper function to generate IDs
    def make_id(index, block_type):
        return f"KOBJ_ACC_12_CH10_{block_type.upper()}_{index:03d}"

    blocks = []
    
    # ---------------------------------------------------------
    # EDUOS 8-STEP SOCRATIC DISCOVERY ARC - CONCEPT 1
    # ---------------------------------------------------------
    # STEP 1: HOOK
    blocks.append({
        "id": make_id(1, "hook"),
        "type": "teacher_tip",
        "difficulty": "Beginner",
        "estimated_minutes": 2,
        "bloom": "Understand",
        "title": "A CEO's Nightmare",
        "title_hi": "एक सीईओ का बुरा सपना",
        "title_gu": "સીઇઓનું ખરાબ સપનું",
        "body": "Imagine you are the CEO of a huge company. At the end of the year, investors ask you: 'Are we making money or losing it? What do we own?' How do you prove your company is doing well? You can't just show them your bank passbook!",
        "body_hi": "कल्पना करें कि आप एक बड़ी कंपनी के सीईओ हैं। साल के अंत में, निवेशक आपसे पूछते हैं: 'क्या हम पैसा कमा रहे हैं या खो रहे हैं? हमारे पास क्या है?' आप कैसे साबित करेंगे कि आपकी कंपनी अच्छा कर रही है? आप केवल अपनी बैंक पासबुक नहीं दिखा सकते!",
        "body_gu": "કલ્પના કરો કે તમે મોટી કંપનીના સીઇઓ છો. વર્ષના અંતે, રોકાણકારો તમને પૂછે છે: 'શું આપણે પૈસા કમાઈએ છીએ કે ગુમાવીએ છીએ? આપણી પાસે શું છે?' તમે કેવી રીતે સાબિત કરશો કે તમારી કંપની સારું કરી રહી છે? તમે તેમને માત્ર તમારી બેંક પાસબુક બતાવી શકતા નથી!"
    })

    # STEP 2: SOCRATIC THINKING
    blocks.append({
        "id": make_id(2, "socratic"),
        "type": "ai_tutor_prompt",
        "difficulty": "Beginner",
        "estimated_minutes": 3,
        "bloom": "Analyze",
        "title": "What would you do?",
        "title_hi": "आप क्या करेंगे?",
        "title_gu": "તમે શું કરશો?",
        "body": "Why do you think companies need to follow a strict, common format for showing their accounts instead of creating their own personal formats?",
        "body_hi": "आपको क्या लगता है कि कंपनियों को अपने खाते दिखाने के लिए एक सख्त, सामान्य प्रारूप का पालन करने की आवश्यकता क्यों है, बजाय इसके कि वे अपना स्वयं का व्यक्तिगत प्रारूप बनाएं?",
        "body_gu": "તમને કેમ લાગે છે કે કંપનીઓએ તેમના હિસાબો બતાવવા માટે કડક, સામાન્ય ફોર્મેટનું પાલન કરવું જોઈએ, તેના બદલે તેઓ પોતાનું વ્યક્તિગત ફોર્મેટ બનાવે?"
    })

    # STEP 3: DISCOVERY
    blocks.append({
        "id": make_id(3, "discovery"),
        "type": "real_world_example",
        "difficulty": "Beginner",
        "estimated_minutes": 3,
        "bloom": "Understand",
        "title": "The Language of Business",
        "title_hi": "व्यापार की भाषा",
        "title_gu": "વ્યાપારની ભાષા",
        "body": "Think of it like languages. If a Japanese company writes reports in Japanese, and an Indian company writes in Hindi, an American investor won't understand either! Similarly, in accounting, we need a universal format. This format is provided by the Companies Act, 2013.",
        "body_hi": "इसे भाषाओं की तरह सोचें। यदि कोई जापानी कंपनी जापानी में रिपोर्ट लिखती है, और एक भारतीय कंपनी हिंदी में लिखती है, तो एक अमेरिकी निवेशक को कुछ भी समझ नहीं आएगा! इसी तरह, अकाउंटिंग में, हमें एक सार्वभौमिक प्रारूप की आवश्यकता होती है। यह प्रारूप कंपनी अधिनियम, 2013 द्वारा प्रदान किया गया है।",
        "body_gu": "તેને ભાષાઓની જેમ વિચારો. જો જાપાની કંપની જાપાનીઝમાં અહેવાલો લખે છે, અને ભારતીય કંપની હિન્દીમાં લખે છે, તો અમેરિકન રોકાણકારને કંઈ સમજમાં આવશે નહીં! તેવી જ રીતે, એકાઉન્ટિંગમાં, અમને સાર્વત્રિક ફોર્મેટની જરૂર છે. આ ફોર્મેટ કંપની અધિનિયમ, 2013 દ્વારા પ્રદાન કરવામાં આવ્યું છે."
    })

    # STEP 4: REVEAL
    blocks.append({
        "id": make_id(4, "reveal"),
        "type": "theory",
        "difficulty": "Intermediate",
        "estimated_minutes": 5,
        "bloom": "Remember",
        "title": "Meaning of Financial Statements",
        "title_hi": "वित्तीय विवरणों का अर्थ",
        "title_gu": "નાણાકીય નિવેદનોનો અર્થ",
        "body": "Financial statements are statements presenting accounting information in brief at the end of the accounting process. As per section 2(40) of the Companies Act, 2013, they include:\n1. A Balance Sheet\n2. A Statement of Profit and Loss\n3. Cash Flow Statement\n4. Statement of Changes in Equity\n5. Notes to Accounts",
        "body_hi": "वित्तीय विवरण वे विवरण हैं जो लेखांकन प्रक्रिया के अंत में संक्षिप्त रूप में लेखांकन जानकारी प्रस्तुत करते हैं। कंपनी अधिनियम, 2013 की धारा 2(40) के अनुसार, इनमें शामिल हैं:\n1. एक बैलेंस शीट\n2. लाभ और हानि का विवरण\n3. कैश फ्लो स्टेटमेंट\n4. इक्विटी में बदलाव का विवरण\n5. खातों के नोट्स",
        "body_gu": "નાણાકીય નિવેદનો એવા નિવેદનો છે જે હિસાબી પ્રક્રિયાના અંતે ટૂંકમાં એકાઉન્ટિંગ માહિતી રજૂ કરે છે. કંપની અધિનિયમ, 2013 ની કલમ 2(40) મુજબ, તેમાં શામેલ છે:\n1. સરવૈયું\n2. નફા-નુકસાનનું નિવેદન\n3. કેશ ફ્લો સ્ટેટમેન્ટ\n4. ઇક્વિટીમાં ફેરફારનું નિવેદન\n5. ખાતાઓની નોંધો"
    })

    # STEP 5: KNOWLEDGE CHECK
    blocks.append({
        "id": make_id(5, "check"),
        "type": "mcq",
        "difficulty": "Beginner",
        "estimated_minutes": 2,
        "bloom": "Remember",
        "question": "Which section of the Companies Act, 2013 defines 'Financial statements'?",
        "question_hi": "कंपनी अधिनियम, 2013 की कौन सी धारा 'वित्तीय विवरण' को परिभाषित करती है?",
        "question_gu": "કંપની અધિનિયમ, 2013 ની કઈ કલમ 'નાણાકીય નિવેદનો' ને વ્યાખ્યાયિત કરે છે?",
        "options": ["Section 129", "Section 133", "Section 2(40)", "Section 2(41)"],
        "options_hi": ["धारा 129", "धारा 133", "धारा 2(40)", "धारा 2(41)"],
        "options_gu": ["કલમ 129", "કલમ 133", "કલમ 2(40)", "કલમ 2(41)"],
        "correct_index": 2,
        "explanation": "Section 2(40) of the Companies Act, 2013 provides the legal definition of what is included in a financial statement.",
        "explanation_hi": "कंपनी अधिनियम, 2013 की धारा 2(40) यह परिभाषित करती है कि वित्तीय विवरण में क्या शामिल है।",
        "explanation_gu": "કંપની અધિનિયમ, 2013 ની કલમ 2(40) નાણાકીય નિવેદનમાં શું સામેલ છે તે વ્યાખ્યાયિત કરે છે."
    })

    # STEP 6: REFLECTION
    blocks.append({
        "id": make_id(6, "reflection"),
        "type": "reflection",
        "difficulty": "Beginner",
        "estimated_minutes": 2,
        "bloom": "Evaluate",
        "title": "Reflect and Explain",
        "title_hi": "विचार करें और समझाएं",
        "title_gu": "વિચારો અને સમજાવો",
        "body": "Explain in your own words why a 'Cash Flow Statement' is considered a vital part of the financial statements alongside the Balance Sheet.",
        "body_hi": "अपने शब्दों में समझाएं कि बैलेंस शीट के साथ-साथ 'कैश फ्लो स्टेटमेंट' को वित्तीय विवरणों का एक महत्वपूर्ण हिस्सा क्यों माना जाता है।",
        "body_gu": "તમારા પોતાના શબ્દોમાં સમજાવો કે શા માટે બેલેન્સ શીટની સાથે 'કેશ ફ્લો સ્ટેટમેન્ટ'ને નાણાકીય નિવેદનોનો મહત્વપૂર્ણ ભાગ માનવામાં આવે છે."
    })

    # STEP 7: CONNECTION
    blocks.append({
        "id": make_id(7, "connection"),
        "type": "cross_subject_link",
        "difficulty": "Intermediate",
        "estimated_minutes": 2,
        "bloom": "Apply",
        "title": "Connection to Business Studies",
        "title_hi": "बिजनेस स्टडीज से संबंध",
        "title_gu": "બિઝનેસ સ્ટડીઝ સાથે જોડાણ",
        "body": "In Business Studies, you learned about 'Financial Management'. The financial statements we prepare here are the raw data used by Financial Managers to make investment and dividend decisions.",
        "body_hi": "बिजनेस स्टडीज में, आपने 'वित्तीय प्रबंधन' के बारे में सीखा। हम यहाँ जो वित्तीय विवरण तैयार करते हैं, वे कच्चे डेटा हैं जिनका उपयोग वित्तीय प्रबंधकों द्वारा निवेश और लाभांश निर्णय लेने के लिए किया जाता है।",
        "body_gu": "બિઝનેસ સ્ટડીઝમાં, તમે 'ફાઇનાન્સિયલ મેનેજમેન્ટ' વિશે શીખ્યા. અમે અહીં જે નાણાકીય નિવેદનો તૈયાર કરીએ છીએ તે કાચો ડેટા છે જેનો ઉપયોગ ફાઇનાન્સિયલ મેનેજરો દ્વારા રોકાણ અને ડિવિડન્ડ નિર્ણયો લેવા માટે થાય છે."
    })

    # STEP 8: MASTERY
    blocks.append({
        "id": make_id(8, "mastery"),
        "type": "challenge_question",
        "difficulty": "Advanced",
        "estimated_minutes": 4,
        "bloom": "Create",
        "title": "Mastery Challenge",
        "title_hi": "मास्टरी चुनौती",
        "title_gu": "માસ્ટરી ચેલેન્જ",
        "body": "A company claims it has a massive profit but cannot pay its employees' salaries this month. Using your knowledge of the components of financial statements, which specific statement would you check to find out why?",
        "body_hi": "एक कंपनी का दावा है कि उसे भारी लाभ हुआ है लेकिन वह इस महीने अपने कर्मचारियों का वेतन नहीं दे सकती। वित्तीय विवरणों के घटकों के अपने ज्ञान का उपयोग करते हुए, आप यह पता लगाने के लिए कौन सा विशिष्ट विवरण जांचेंगे कि ऐसा क्यों है?",
        "body_gu": "એક કંપની દાવો કરે છે કે તેને મોટો નફો થયો છે પરંતુ તે આ મહિને તેના કર્મચારીઓનો પગાર ચૂકવી શકતી નથી. નાણાકીય નિવેદનોના ઘટકોના તમારા જ્ઞાનનો ઉપયોગ કરીને, તમે આવું કેમ છે તે શોધવા માટે કયું ચોક્કસ નિવેદન તપાસશો?"
    })

    # ---------------------------------------------------------
    # EXERCISES - NUMERICAL PROBLEMS
    # ---------------------------------------------------------
    # Problem 6
    blocks.append({
        "id": make_id(106, "exercise"),
        "type": "worked_example",
        "difficulty": "Advanced",
        "estimated_minutes": 15,
        "bloom": "Apply",
        "title": "Exercise Problem 6: Moon Ltd. Balance Sheet",
        "title_hi": "व्यायाम समस्या 6: मून लिमिटेड की बैलेंस शीट",
        "title_gu": "વ્યાયામ સમસ્યા 6: મૂન લિમિટેડની બેલેન્સ શીટ",
        "body": "Following balances are taken from the books of Moon Ltd. Prepare balance sheet as at 31-3-2017 as per schedule-III of Companies Act, 2013.\n\n| Balance | Amt. (₹) |\n|---|---|\n| (1) Interest accrued | 30,000 |\n| (2) Plant-machinery | 15,00,000 |\n| (3) Equity share capital | 15,00,000 |\n| (4) Bank balance and cash | 67,500 |\n| (5) General reserve | 30,000 |\n| (6) Closing stock | 2,70,000 |\n| (7) Creditors | 6,00,000 |\n| (8) Debtors | 3,45,000 |\n| (9) Provision for tax | 90,000 |\n| (10) 12 % bank loan | 1,95,000 |\n| (11) Non-current investments | 45,000 |\n| (12) Electricity deposit | 1,87,500 |\n| (13) Provident fund | 30,000 |",
        "body_hi": "मून लिमिटेड की पुस्तकों से निम्नलिखित शेष लिए गए हैं। कंपनी अधिनियम, 2013 की अनुसूची-III के अनुसार 31-3-2017 को बैलेंस शीट तैयार करें।\n\n| शेष | राशि (₹) |\n|---|---|\n| (1) उपार्जित ब्याज | 30,000 |\n| (2) प्लांट-मशीनरी | 15,00,000 |\n| (3) इक्विटी शेयर पूंजी | 15,00,000 |\n| (4) बैंक बैलेंस और नकद | 67,500 |\n| (5) सामान्य संचय | 30,000 |\n| (6) अंतिम स्टॉक | 2,70,000 |\n| (7) लेनदार | 6,00,000 |\n| (8) देनदार | 3,45,000 |\n| (9) कर के लिए प्रावधान | 90,000 |\n| (10) 12 % बैंक ऋण | 1,95,000 |\n| (11) गैर-वर्तमान निवेश | 45,000 |\n| (12) बिजली जमा | 1,87,500 |\n| (13) भविष्य निधि | 30,000 |",
        "body_gu": "નીચેની બાકી મૂન લિમિટેડના પુસ્તકોમાંથી લેવામાં આવી છે. કંપની અધિનિયમ, 2013 ના શેડ્યૂલ-III મુજબ 31-3-2017 ના રોજ બેલેન્સ શીટ તૈયાર કરો.\n\n| બાકી | રકમ (₹) |\n|---|---|\n| (1) ઉપાર્જિત વ્યાજ | 30,000 |\n| (2) પ્લાન્ટ-મશીનરી | 15,00,000 |\n| (3) ઇક્વિટી શેર મૂડી | 15,00,000 |\n| (4) બેંક બેલેન્સ અને રોકડ | 67,500 |\n| (5) સામાન્ય અનામત | 30,000 |\n| (6) આખરનો સ્ટોક | 2,70,000 |\n| (7) લેણદારો | 6,00,000 |\n| (8) દેવાદારો | 3,45,000 |\n| (9) કર માટે જોગવાઈ | 90,000 |\n| (10) 12 % બેંક લોન | 1,95,000 |\n| (11) બિન-વર્તમાન રોકાણો | 45,000 |\n| (12) વીજળી થાપણ | 1,87,500 |\n| (13) પ્રોવિડન્ટ ફંડ | 30,000 |"
    })

    # Problem 9
    blocks.append({
        "id": make_id(109, "exercise"),
        "type": "practice_question",
        "difficulty": "Advanced",
        "estimated_minutes": 20,
        "bloom": "Create",
        "title": "Exercise Problem 9: Keyur Ltd. Final Accounts",
        "title_hi": "व्यायाम समस्या 9: केयूर लिमिटेड अंतिम खाते",
        "title_gu": "વ્યાયામ સમસ્યા 9: કેયુર લિમિટેડ અંતિમ હિસાબો",
        "body": "Following is the balance sheet of Keyur Ltd. as on 31-3-2017:\n\n| Particulars | Debit (₹) | Credit (₹) |\n|---|---|---|\n| Equity share capital | | 2,40,000 |\n| Office and sales expenses | 24,000 | |\n| Purchase | 4,26,000 | |\n| 10 % Debenture | | 1,20,000 |\n| Sales | | 9,60,000 |\n| Software | 1,20,000 | |\n| Wages | 24,000 | |\n| Debenture interest | 12,000 | |\n| Salary | 3,00,000 | |\n| Bank overdraft | | 14,400 |\n| Land-building | 2,28,000 | |\n| Opening stock | 36,000 | |\n| Discount received | | 15,600 |\n| Debtors | 1,80,000 | |\n| **Total** | **13,50,000** | **13,50,000** |\n\n**Other information:**\n(1) Closing stock = 42,000\n(2) Make provision for tax at 50 % of net profit.\nFrom the above information, prepare final accounts of the company for the year ending on 31st March, 2017 as per schedule-III and Companies Act, 2013. Notes to the accounts are not required.",
        "body_hi": "केयूर लिमिटेड का 31-3-2017 का बैलेंस शीट निम्नलिखित है:\n\n| विवरण | डेबिट (₹) | क्रेडिट (₹) |\n|---|---|---|\n| इक्विटी शेयर पूंजी | | 2,40,000 |\n| कार्यालय और बिक्री खर्च | 24,000 | |\n| खरीद | 4,26,000 | |\n| 10 % डिबेंचर | | 1,20,000 |\n| बिक्री | | 9,60,000 |\n| सॉफ्टवेयर | 1,20,000 | |\n| वेतन | 24,000 | |\n| डिबेंचर ब्याज | 12,000 | |\n| वेतन | 3,00,000 | |\n| बैंक ओवरड्राफ्ट | | 14,400 |\n| भूमि-भवन | 2,28,000 | |\n| प्रारंभिक स्टॉक | 36,000 | |\n| छूट प्राप्त | | 15,600 |\n| देनदार | 1,80,000 | |\n| **कुल** | **13,50,000** | **13,50,000** |\n\n**अन्य जानकारी:**\n(1) अंतिम स्टॉक = 42,000\n(2) शुद्ध लाभ के 50% पर कर का प्रावधान करें।\nउपरोक्त जानकारी से, कंपनी अधिनियम, 2013 की अनुसूची-III के अनुसार 31 मार्च, 2017 को समाप्त होने वाले वर्ष के लिए कंपनी के अंतिम खाते तैयार करें। खातों के नोट्स आवश्यक नहीं हैं।",
        "body_gu": "કેયુર લિમિટેડની 31-3-2017 ના રોજની બેલેન્સ શીટ નીચે મુજબ છે:\n\n| વિગતો | ડેબિટ (₹) | ક્રેડિટ (₹) |\n|---|---|---|\n| ઇક્વિટી શેર મૂડી | | 2,40,000 |\n| ઓફિસ અને વેચાણ ખર્ચ | 24,000 | |\n| ખરીદી | 4,26,000 | |\n| 10 % ડિબેન્ચર | | 1,20,000 |\n| વેચાણ | | 9,60,000 |\n| સોફ્ટવેર | 1,20,000 | |\n| વેતન | 24,000 | |\n| ડિબેન્ચર વ્યાજ | 12,000 | |\n| પગાર | 3,00,000 | |\n| બેંક ઓવરડ્રાફ્ટ | | 14,400 |\n| જમીન-મકાન | 2,28,000 | |\n| શરૂઆતનો સ્ટોક | 36,000 | |\n| મળેલ વળતર | | 15,600 |\n| દેવાદારો | 1,80,000 | |\n| **કુલ** | **13,50,000** | **13,50,000** |\n\n**અન્ય માહિતી:**\n(1) આખરનો સ્ટોક = 42,000\n(2) ચોખ્ખા નફાના 50% પર કર માટે જોગવાઈ કરો.\nઉપરોક્ત માહિતી પરથી, કંપની અધિનિયમ, 2013 ના શેડ્યૂલ-III મુજબ 31 માર્ચ, 2017 ના રોજ પૂરા થતા વર્ષ માટે કંપનીના અંતિમ હિસાબો તૈયાર કરો. ખાતાઓની નોંધો જરૂરી નથી."
    })

    # Problem 10
    blocks.append({
        "id": make_id(110, "exercise"),
        "type": "practice_question",
        "difficulty": "Advanced",
        "estimated_minutes": 20,
        "bloom": "Create",
        "title": "Exercise Problem 10: Parth Ltd. Trial Balance",
        "title_hi": "व्यायाम समस्या 10: पार्थ लिमिटेड ट्रायल बैलेंस",
        "title_gu": "વ્યાયામ સમસ્યા 10: પાર્થ લિમિટેડ ટ્રાયલ બેલેન્સ",
        "body": "Following is the trial balance of Parth Ltd. as on 31-3-2017:\n\n| Particulars | Debit (₹) | Credit (₹) |\n|---|---|---|\n| Sales | | 11,25,000 |\n| Employee benefit expenses | 1,95,000 | |\n| Inventories | 1,65,000 | |\n| Finance costs | 26,250 | |\n| Security premium | | 60,000 |\n| Fixed assets - tangible | 12,00,000 | |\n| Trade payables | | 90,000 |\n| Equity share capital | | 7,50,000 |\n| Trade receivables | 60,000 | |\n| Other income | | 30,000 |\n| Long-term borrowings | | 5,25,000 |\n| Cash and bank balance | 90,000 | |\n| Depreciation | 33,750 | |\n| Cost of goods sold | 6,00,000 | |\n| Non-current investments | 2,10,000 | |\n| **Total** | **25,80,000** | **25,80,000** |\n\nFrom the above information, prepare final accounts of the company for the year ended on 31-3-2017 as per schedule-III of Companies Act, 2013. Notes to the accounts are not required.",
        "body_hi": "पार्थ लिमिटेड का 31-3-2017 का ट्रायल बैलेंस निम्नलिखित है:\n\n| विवरण | डेबिट (₹) | क्रेडिट (₹) |\n|---|---|---|\n| बिक्री | | 11,25,000 |\n| कर्मचारी लाभ व्यय | 1,95,000 | |\n| इन्वेंटरी | 1,65,000 | |\n| वित्त लागत | 26,250 | |\n| सुरक्षा प्रीमियम | | 60,000 |\n| अचल संपत्तियां - मूर्त | 12,00,000 | |\n| व्यापार देय | | 90,000 |\n| इक्विटी शेयर पूंजी | | 7,50,000 |\n| व्यापार प्राप्य | 60,000 | |\n| अन्य आय | | 30,000 |\n| दीर्घकालिक उधार | | 5,25,000 |\n| नकद और बैंक बैलेंस | 90,000 | |\n| मूल्यह्रास | 33,750 | |\n| बेचे गए माल की लागत | 6,00,000 | |\n| गैर-वर्तमान निवेश | 2,10,000 | |\n| **कुल** | **25,80,000** | **25,80,000** |\n\nउपरोक्त जानकारी से, कंपनी अधिनियम, 2013 की अनुसूची-III के अनुसार 31-3-2017 को समाप्त होने वाले वर्ष के लिए कंपनी के अंतिम खाते तैयार करें। खातों के नोट्स आवश्यक नहीं हैं।",
        "body_gu": "પાર્થ લિમિટેડનું 31-3-2017 ના રોજનું ટ્રાયલ બેલેન્સ નીચે મુજબ છે:\n\n| વિગતો | ડેબિટ (₹) | ક્રેડિટ (₹) |\n|---|---|---|\n| વેચાણ | | 11,25,000 |\n| કર્મચારી લાભ ખર્ચ | 1,95,000 | |\n| ઇન્વેન્ટરીઝ | 1,65,000 | |\n| ફાઇનાન્સ ખર્ચ | 26,250 | |\n| સુરક્ષા પ્રીમિયમ | | 60,000 |\n| સ્થિર સંપત્તિ - મૂર્ત | 12,00,000 | |\n| વેપાર ચૂકવવાપાત્ર | | 90,000 |\n| ઇક્વિટી શેર મૂડી | | 7,50,000 |\n| વેપાર મળવાપાત્ર | 60,000 | |\n| અન્ય આવક | | 30,000 |\n| લાંબા ગાળાના ઉધાર | | 5,25,000 |\n| રોકડ અને બેંક બેલેન્સ | 90,000 | |\n| ઘસારો | 33,750 | |\n| વેચાયેલા માલની કિંમત | 6,00,000 | |\n| બિન-વર્તમાન રોકાણો | 2,10,000 | |\n| **કુલ** | **25,80,000** | **25,80,000** |\n\nઉપરોક્ત માહિતી પરથી, કંપની અધિનિયમ, 2013 ના શેડ્યૂલ-III મુજબ 31-3-2017 ના રોજ પૂરા થતા વર્ષ માટે કંપનીના અંતિમ હિસાબો તૈયાર કરો. ખાતાઓની નોંધો જરૂરી નથી."
    })

    chapter_data["blocks"] = blocks
    
    # Save the JSON file
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(chapter_data, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated chapter JSON at {OUTPUT_PATH}")
    print(f"Total blocks generated: {len(blocks)}")

if __name__ == "__main__":
    main()
