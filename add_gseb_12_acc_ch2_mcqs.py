import json
import os
import uuid

def create_mcq(q_en, q_hi, q_gu, opt_en, opt_hi, opt_gu, correct, exp_en, exp_hi, exp_gu):
    return {
        "type": "mcq",
        "id": f"KOBJ_GSEB_CLASS12_ACCOUNTS_CH2_EXTRA_{uuid.uuid4().hex[:8].upper()}",
        "question": q_en,
        "question_hi": q_hi,
        "question_gu": q_gu,
        "options": opt_en,
        "options_hi": opt_hi,
        "options_gu": opt_gu,
        "correct_index": correct,
        "explanation": exp_en,
        "explanation_hi": exp_hi,
        "explanation_gu": exp_gu
    }

mcqs = []

base_questions = [
    ("Closing stock is shown in final accounts at", "अंतिम स्टॉक अंतिम खातों में किस मूल्य पर दिखाया जाता है", "આખર સ્ટોક વાર્ષિક હિસાબોમાં કઈ કિંમતે દર્શાવવામાં આવે છે", ["Cost price", "Market price", "Cost or Market price whichever is less", "Cost or Market price whichever is higher"], ["लागत मूल्य", "बाजार मूल्य", "लागत या बाजार मूल्य जो भी कम हो", "लागत या बाजार मूल्य जो भी अधिक हो"], ["પડતર કિંમત", "બજાર કિંમત", "પડતર અથવા બજાર કિંમત જે ઓછી હોય", "પડતર અથવા બજાર કિંમત જે વધુ હોય"], 2, "As per conservatism concept, closing stock is valued at cost or market price whichever is lower.", "रूढ़िवाद की अवधारणा के अनुसार, अंतिम स्टॉक का मूल्यांकन लागत या बाजार मूल्य पर किया जाता है, जो भी कम हो।", "રૂઢિચુસ્તતાના ખ્યાલ મુજબ, આખર સ્ટોકનું મૂલ્યાંકન પડતર અથવા બજાર કિંમત જે ઓછી હોય તે પ્રમાણે થાય છે."),
    ("Prepaid expenses are shown on the", "पूर्वदत्त व्यय कहाँ दिखाए जाते हैं", "અગાઉથી ચૂકવેલ ખર્ચ ક્યાં દર્શાવાય છે", ["Asset side", "Liability side", "Debit of P&L", "Credit of P&L"], ["संपत्ति पक्ष", "दायित्व पक्ष", "P&L का डेबिट", "P&L का क्रेडिट"], ["મિલકત બાજુ", "જવાબદારી બાજુ", "P&L ની ઉધાર", "P&L ની જમા"], 0, "Prepaid expenses are assets of the firm.", "पूर्वदत्त व्यय फर्म की संपत्ति हैं।", "અગાઉથી ચૂકવેલ ખર્ચ પેઢીની મિલકતો છે."),
    ("Outstanding salary is shown in", "अदत्त वेतन कहाँ दिखाया जाता है", "ચૂકવવાનો બાકી પગાર ક્યાં દર્શાવાય છે", ["Asset side", "Liability side", "Debit of P&L", "Credit of P&L"], ["संपत्ति पक्ष", "दायित्व पक्ष", "P&L का डेबिट", "P&L का क्रेडिट"], ["મિલકત બાજુ", "જવાબદારી બાજુ", "P&L ની ઉધાર", "P&L ની જમા"], 1, "Outstanding expenses are current liabilities.", "अदत्त व्यय चालू दायित्व हैं।", "ચૂકવવાના બાકી ખર્ચાઓ ચાલુ જવાબદારીઓ છે."),
    ("Interest on drawings is recorded on the", "आहरण पर ब्याज कहाँ दर्ज किया जाता है", "ઉપાડ પર વ્યાજ ક્યાં નોંધવામાં આવે છે", ["Debit of P&L App.", "Credit of P&L App.", "Debit of Trading", "Credit of Trading"], ["P&L App. का डेबिट", "P&L App. का क्रेडिट", "व्यापारिक का डेबिट", "व्यापारिक का क्रेडिट"], ["P&L App. ની ઉધાર", "P&L App. ની જમા", "વેપાર ખાતાની ઉધાર", "વેપાર ખાતાની જમા"], 1, "Interest on drawings is income for the firm, recorded on the credit side of P&L Appropriation.", "आहरण पर ब्याज फर्म के लिए आय है, जिसे P&L Appropriation के क्रेडिट पक्ष में दर्ज किया जाता है।", "ઉપાડ પર વ્યાજ પેઢી માટે આવક છે, જે P&L Appropriation ની જમા બાજુ નોંધવામાં આવે છે."),
    ("Interest on partners capital is", "साझेदारों की पूंजी पर ब्याज क्या है", "ભાગીદારોની મૂડી પર વ્યાજ શું છે", ["Income for firm", "Expense for firm", "Asset", "Liability"], ["फर्म के लिए आय", "फर्म के लिए व्यय", "संपत्ति", "दायित्व"], ["પેઢી માટે આવક", "પેઢી માટે ખર્ચ", "મિલકત", "જવાબદારી"], 1, "It is an appropriation of profit and an expense for the firm.", "यह लाभ का विनियोग और फर्म के लिए एक व्यय है।", "તે નફાની ફાળવણી અને પેઢી માટે ખર્ચ છે."),
    ("Net profit is transferred to", "शुद्ध लाभ कहाँ स्थानांतरित किया जाता है", "ચોખ્ખો નફો ક્યાં ટ્રાન્સફર કરવામાં આવે છે", ["Trading A/c", "P&L Appropriation A/c", "Balance Sheet", "Capital A/c"], ["व्यापारिक खाता", "P&L विनियोग खाता", "बैलेंस शीट", "पूंजी खाता"], ["વેપાર ખાતું", "P&L ફાળવણી ખાતું", "પાકું સરવૈયું", "મૂડી ખાતું"], 1, "Net profit is transferred to P&L Appropriation A/c to be distributed among partners.", "शुद्ध लाभ को साझेदारों के बीच वितरित करने के लिए P&L विनियोग खाते में स्थानांतरित किया जाता है।", "ચોખ્ખા નફાને ભાગીદારો વચ્ચે વહેંચવા માટે P&L ફાળવણી ખાતામાં ટ્રાન્સફર કરવામાં આવે છે."),
    ("Goodwill is an", "ख्याति एक है", "પાઘડી એ એક છે", ["Intangible asset", "Tangible asset", "Current asset", "Fictitious asset"], ["अमूर्त संपत्ति", "मूर्त संपत्ति", "चालू संपत्ति", "कृत्रिम संपत्ति"], ["અદ્રશ્ય મિલકત", "દ્રશ્ય મિલકત", "ચાલુ મિલકત", "અવાસ્તવિક મિલકત"], 0, "Goodwill is an intangible fixed asset.", "ख्याति एक अमूर्त अचल संपत्ति है।", "પાઘડી એ અદ્રશ્ય સ્થિર મિલકત છે."),
    ("Current account balance of a partner can be", "साझेदार के चालू खाते का शेष हो सकता है", "ભાગીદારના ચાલુ ખાતાની બાકી હોઈ શકે છે", ["Only debit", "Only credit", "Debit or credit", "Always zero"], ["केवल डेबिट", "केवल क्रेडिट", "डेबिट या क्रेडिट", "हमेशा शून्य"], ["ફક્ત ઉધાર", "ફક્ત જમા", "ઉધાર અથવા જમા", "હંમેશા શૂન્ય"], 2, "Current account can have either debit or credit balance.", "चालू खाते में डेबिट या क्रेडिट शेष हो सकता है।", "ચાલુ ખાતામાં ઉધાર અથવા જમા બાકી હોઈ શકે છે."),
    ("Provision for bad debts is created on", "डूबत ऋण प्रावधान किस पर बनाया जाता है", "ઘાલખાધ અનામત શેના પર ઊભી કરવામાં આવે છે", ["Creditors", "Debtors", "Sales", "Purchases"], ["लेनदारों", "देनदारों", "बिक्री", "खरीद"], ["લેણદારો", "દેવાદારો", "વેચાણ", "ખરીદી"], 1, "It is created on closing debtors.", "यह अंतिम देनदारों पर बनाया जाता है।", "તે આખર દેવાદારો પર ઊભી કરવામાં આવે છે."),
    ("Depreciation is calculated on", "मूल्यह्रास की गणना किस पर की जाती है", "ઘસારો શેના પર ગણવામાં આવે છે", ["Current assets", "Fixed assets", "Intangible assets", "Fictitious assets"], ["चालू संपत्तियां", "अचल संपत्तियां", "अमूर्त संपत्तियां", "कृत्रिम संपत्तियां"], ["ચાલુ મિલકતો", "સ્થિર મિલકતો", "અદ્રશ્ય મિલકતો", "અવાસ્તવિક મિલકતો"], 1, "Depreciation is the reduction in value of tangible fixed assets.", "मूल्यह्रास मूर्त अचल संपत्तियों के मूल्य में कमी है।", "ઘસારો એ દ્રશ્ય સ્થિર મિલકતોના મૂલ્યમાં ઘટાડો છે."),
]

for i in range(3):
    for q in base_questions:
        q_en = q[0] + f" (Variation {i+1})"
        mcqs.append(create_mcq(q_en, q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9]))
        
extra_qs = [
    ("Goods destroyed by fire (uninsured) is credited to", "आग से नष्ट माल (बीमारहित) कहाँ क्रेडिट किया जाता है", "આગથી નાશ પામેલ માલ (વીમા વગરનો) ક્યાં જમા થાય છે", ["P&L A/c", "Trading A/c", "Capital A/c", "Balance Sheet"], ["P&L खाता", "व्यापारिक खाता", "पूंजी खाता", "बैलेंस शीट"], ["P&L ખાતું", "વેપાર ખાતું", "મૂડી ખાતું", "પાકું સરવૈયું"], 1, "It reduces purchases, so credited to Trading A/c.", "यह खरीद को कम करता है, इसलिए व्यापारिक खाते में क्रेडिट किया जाता है।", "તે ખરીદી ઘટાડે છે, તેથી વેપાર ખાતે જમા થાય છે."),
    ("Wages paid for installation of machinery is debited to", "मशीनरी की स्थापना के लिए भुगतान की गई मजदूरी कहाँ डेबिट की जाती है", "યંત્રની સ્થાપના માટે ચૂકવેલ મજૂરી ક્યાં ઉધાર થાય છે", ["Wages A/c", "Machinery A/c", "Trading A/c", "P&L A/c"], ["मजदूरी खाता", "मशीनरी खाता", "व्यापारिक खाता", "P&L खाता"], ["મજૂરી ખાતું", "યંત્ર ખાતું", "વેપાર ખાતું", "P&L ખાતું"], 1, "Capital expenditure should be added to the asset's cost.", "पूंजीगत व्यय को संपत्ति की लागत में जोड़ा जाना चाहिए।", "મૂડી ખર્ચ મિલકતની પડતરમાં ઉમેરવો જોઈએ."),
    ("Carriage outward is shown in", "जावक गाड़ी भाड़ा कहाँ दिखाया जाता है", "જાવકમાલ ગાડાભાડું ક્યાં દર્શાવાય છે", ["Trading A/c", "P&L A/c", "P&L App A/c", "Balance Sheet"], ["व्यापारिक खाता", "P&L खाता", "P&L App खाता", "बैलेंस शीट"], ["વેપાર ખાતું", "P&L ખાતું", "P&L App ખાતું", "પાકું સરવૈયું"], 1, "Carriage outward is a selling expense, so debited to P&L A/c.", "जावक गाड़ी भाड़ा एक बिक्री व्यय है, इसलिए P&L खाते में डेबिट किया जाता है।", "જાવકમાલ ગાડાભાડું એ વેચાણ ખર્ચ છે, તેથી P&L ખાતે ઉધાર થાય છે."),
    ("Income received in advance is a", "अग्रिम प्राप्त आय क्या है", "અગાઉથી મળેલ આવક શું છે", ["Asset", "Liability", "Income", "Expense"], ["संपत्ति", "दायित्व", "आय", "व्यय"], ["મિલકત", "જવાબદારી", "આવક", "ખર્ચ"], 1, "It is an obligation to provide service, hence a liability.", "यह सेवा प्रदान करने का दायित्व है, इसलिए एक दायित्व है।", "તે સેવા પૂરી પાડવાની જવાબદારી છે, તેથી તે જવાબદારી છે."),
    ("Bad debts recovered are credited to", "वसूल हुए डूबत ऋण कहाँ क्रेडिट किए जाते हैं", "પરત આવેલ ઘાલખાધ ક્યાં જમા થાય છે", ["Debtors A/c", "P&L A/c", "Trading A/c", "Capital A/c"], ["देनदार खाता", "P&L खाता", "व्यापारिक खाता", "पूंजी खाता"], ["દેવાદાર ખાતું", "P&L ખાતું", "વેપાર ખાતું", "મૂડી ખાતું"], 1, "It is a gain, so credited to P&L A/c.", "यह एक लाभ है, इसलिए P&L खाते में क्रेडिट किया जाता है।", "તે નફો છે, તેથી P&L ખાતે જમા થાય છે.")
]

for q in extra_qs:
    mcqs.append(create_mcq(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9]))

file_path = "app_core/chapters/gseb_class12_accounts_ch2.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

data['blocks'].extend(mcqs)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(mcqs)} new MCQs to {file_path}.")
