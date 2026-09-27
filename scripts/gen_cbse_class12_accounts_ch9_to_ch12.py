import json
import os

def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Generated {file_path} successfully!")

def gen_ch9():
    data = {
        "metadata": {
            "id": "cbse_class12_accounts_ch9",
            "title": "Financial Statements of a Company",
            "title_hi": "एक कंपनी के वित्तीय विवरण",
            "title_gu": "કંપનીના નાણાકીય પત્રકો",
            "subject": "Accountancy",
            "grade": "12",
            "board": "CBSE",
            "curriculum": ["CBSE"],
            "difficulty": "Intermediate",
            "estimated_minutes": 60,
            "learning_outcomes": [
                "Understand the meaning and nature of Financial Statements of a company.",
                "Learn the format of Balance Sheet as per Schedule III of Companies Act, 2013.",
                "Learn the format of Statement of Profit and Loss as per Schedule III."
            ]
        },
        "blocks": [
            {
                "type": "theory",
                "content": "Unlike a Partnership Firm where the partners can prepare their Balance Sheet in any format they like (T-shape), a Joint Stock Company MUST prepare its Financial Statements in a strict, legally mandated format.\nThis format is given in **Schedule III of the Companies Act, 2013**. It is a vertical format, not a horizontal one.",
                "content_hi": "एक साझेदारी फर्म के विपरीत जहां भागीदार किसी भी प्रारूप (टी-आकार) में अपनी बैलेंस शीट तैयार कर सकते हैं, एक संयुक्त स्टॉक कंपनी को सख्त, कानूनी रूप से अनिवार्य प्रारूप में अपने वित्तीय विवरण तैयार करने होंगे।\nयह प्रारूप **कंपनी अधिनियम, 2013 की अनुसूची III (Schedule III)** में दिया गया है। यह एक लंबवत (Vertical) प्रारूप है, क्षैतिज नहीं।",
                "content_gu": "ભાગીદારી પેઢીથી વિપરીત જ્યાં ભાગીદારો તેમને ગમે તેવા ફોર્મેટમાં (ટી-આકારમાં) તેમનું પાકું સરવૈયું તૈયાર કરી શકે છે, સંયુક્ત સ્ટોક કંપનીએ તેના નાણાકીય પત્રકો કડક, કાયદેસર રીતે ફરજિયાત ફોર્મેટમાં તૈયાર કરવા જ જોઈએ.\nઆ ફોર્મેટ **કંપની ધારા, 2013 ના પરિશિષ્ટ III (Schedule III)** માં આપવામાં આવ્યું છે. તે ઊભું (Vertical) ફોર્મેટ છે, આડું નહીં.",
                "id": "KOBJ_CBSE_ACC12_CH9_THEO_001"
            }
        ]
    }
    save_json('app_core/chapters/cbse_class12_accounts_ch9.json', data)

def gen_ch10():
    data = {
        "metadata": {
            "id": "cbse_class12_accounts_ch10",
            "title": "Financial Statement Analysis",
            "title_hi": "वित्तीय विवरण विश्लेषण",
            "title_gu": "નાણાકીય પત્રકોનું વિશ્લેષણ",
            "subject": "Accountancy",
            "grade": "12",
            "board": "CBSE",
            "curriculum": ["CBSE"],
            "difficulty": "Intermediate",
            "estimated_minutes": 60,
            "learning_outcomes": [
                "Understand the meaning, significance, and limitations of Financial Analysis.",
                "Prepare Comparative Statements.",
                "Prepare Common-size Statements."
            ]
        },
        "blocks": [
            {
                "type": "theory",
                "content": "Just looking at a company's Net Profit (say, ₹10 Crores) doesn't tell the full story. Is ₹10 Crores good or bad? If they earned ₹20 Crores last year, then ₹10 Crores is terrible!\nTo truly understand a company's health, we must compare its data across different years (Trend Analysis) or with other companies (Cross-sectional Analysis). This process is called **Financial Statement Analysis**.",
                "content_hi": "केवल किसी कंपनी के शुद्ध लाभ (मान लीजिए, ₹10 करोड़) को देखने से पूरी कहानी बयां नहीं होती। क्या ₹10 करोड़ अच्छा है या बुरा? यदि उन्होंने पिछले साल ₹20 करोड़ कमाए, तो ₹10 करोड़ बहुत बुरा है!\nकिसी कंपनी के स्वास्थ्य को वास्तव में समझने के लिए, हमें विभिन्न वर्षों (Trend Analysis) या अन्य कंपनियों (Cross-sectional Analysis) के साथ उसके डेटा की तुलना करनी चाहिए। इस प्रक्रिया को **वित्तीय विवरण विश्लेषण (Financial Statement Analysis)** कहा जाता है।",
                "content_gu": "માત્ર કંપનીના ચોખ્ખા નફા (ધારો કે, ₹10 કરોડ) ને જોવાથી સંપૂર્ણ વાર્તા જણાતી નથી. શું ₹10 કરોડ સારા છે કે ખરાબ? જો તેઓએ ગયા વર્ષે ₹20 કરોડ કમાવ્યા હોય, તો ₹10 કરોડ ભયાનક છે!\nકંપનીના સ્વાસ્થ્યને ખરેખર સમજવા માટે, આપણે તેના ડેટાની વિવિધ વર્ષો (Trend Analysis) અથવા અન્ય કંપનીઓ (Cross-sectional Analysis) સાથે સરખામણી કરવી જોઈએ. આ પ્રક્રિયાને **નાણાકીય પત્રકોનું વિશ્લેષણ (Financial Statement Analysis)** કહેવામાં આવે છે.",
                "id": "KOBJ_CBSE_ACC12_CH10_THEO_001"
            }
        ]
    }
    save_json('app_core/chapters/cbse_class12_accounts_ch10.json', data)

def gen_ch11():
    data = {
        "metadata": {
            "id": "cbse_class12_accounts_ch11",
            "title": "Accounting Ratios",
            "title_hi": "लेखांकन अनुपात",
            "title_gu": "હિસાબી ગુણોત્તર",
            "subject": "Accountancy",
            "grade": "12",
            "board": "CBSE",
            "curriculum": ["CBSE"],
            "difficulty": "Master",
            "estimated_minutes": 150,
            "learning_outcomes": [
                "Calculate and interpret Liquidity Ratios (Current Ratio, Liquid Ratio).",
                "Calculate and interpret Solvency Ratios (Debt-Equity, Proprietary, Interest Coverage).",
                "Calculate and interpret Activity/Turnover Ratios (Inventory Turnover, Trade Receivables Turnover).",
                "Calculate and interpret Profitability Ratios (Gross Profit, Net Profit, Operating Profit)."
            ]
        },
        "blocks": [
            {
                "type": "theory",
                "content": "A ratio is a mathematical relationship between two numbers. In accounting, we use Ratios to simplify complex financial data. \nFor example, if a company has Current Assets of ₹2,00,000 and Current Liabilities of ₹1,00,000, the **Current Ratio** is 2:1. This simply means for every ₹1 of short-term debt, the company has ₹2 of short-term assets to pay it off. The company is safe!",
                "content_hi": "अनुपात (Ratio) दो संख्याओं के बीच एक गणितीय संबंध है। लेखांकन में, हम जटिल वित्तीय डेटा को सरल बनाने के लिए अनुपात का उपयोग करते हैं।\nउदाहरण के लिए, यदि किसी कंपनी की वर्तमान संपत्ति ₹2,00,000 है और वर्तमान देनदारियां ₹1,00,000 हैं, तो **चालू अनुपात (Current Ratio)** 2:1 है। इसका सीधा सा मतलब है कि प्रत्येक ₹1 के अल्पकालिक ऋण के लिए, कंपनी के पास इसका भुगतान करने के लिए ₹2 की अल्पकालिक संपत्ति है। कंपनी सुरक्षित है!",
                "content_gu": "ગુણોત્તર (Ratio) એ બે સંખ્યાઓ વચ્ચેનો ગાણિતિક સંબંધ છે. એકાઉન્ટિંગમાં, અમે જટિલ નાણાકીય ડેટાને સરળ બનાવવા માટે ગુણોત્તરનો ઉપયોગ કરીએ છીએ.\nઉદાહરણ તરીકે, જો કંપનીની ચાલુ મિલકતો ₹2,00,000 હોય અને ચાલુ દેવા ₹1,00,000 હોય, તો **ચાલુ ગુણોત્તર (Current Ratio)** 2:1 છે. આનો સીધો અર્થ એ છે કે દરેક ₹1 ના ટૂંકા ગાળાના દેવા માટે, કંપની પાસે તેને ચૂકવવા માટે ₹2 ની ટૂંકા ગાળાની મિલકતો છે. કંપની સુરક્ષિત છે!",
                "id": "KOBJ_CBSE_ACC12_CH11_THEO_001"
            },
            {
                "type": "numerical",
                "question": "A company has Current Assets of ₹5,00,000, Inventory of ₹1,00,000, Prepaid Expenses of ₹20,000, and Current Liabilities of ₹2,00,000. \nCalculate the Quick Ratio (Liquid Ratio).",
                "question_hi": "एक कंपनी के पास ₹5,00,000 की चालू संपत्ति (Current Assets), ₹1,00,000 की इन्वेंटरी, ₹20,000 का प्रीपेड खर्च और ₹2,00,000 की चालू देनदारियां (Current Liabilities) हैं।\nत्वरित अनुपात (Quick Ratio) की गणना करें।",
                "question_gu": "કંપની પાસે ₹5,00,000 ની ચાલુ મિલકતો (Current Assets), ₹1,00,000 નો સ્ટોક (Inventory), ₹20,000 ના અગાઉથી ચૂકવેલ ખર્ચા (Prepaid Expenses) અને ₹2,00,000 ના ચાલુ દેવા (Current Liabilities) છે.\nપ્રવાહી ગુણોત્તર (Quick/Liquid Ratio) ની ગણતરી કરો.",
                "solution": "Step 1: Calculate Quick (Liquid) Assets\nQuick Assets = Current Assets - Inventory - Prepaid Expenses\nQuick Assets = 5,00,000 - 1,00,000 - 20,000 = **₹3,80,000**\n*(Why? Because inventory takes time to sell, and prepaid expenses cannot be converted back into cash quickly. They are not 'liquid'.)*\n\nStep 2: Note the Current Liabilities\nCurrent Liabilities = **₹2,00,000**\n\nStep 3: Calculate Quick Ratio\nQuick Ratio = Quick Assets / Current Liabilities\nQuick Ratio = 3,80,000 / 2,00,000 = **1.9 : 1**",
                "solution_hi": "(गणितीय गणना के लिए अंग्रेजी समाधान देखें। त्वरित संपत्ति (Quick Assets) की गणना इन्वेंट्री और प्रीपेड खर्चों को घटाकर की जाती है क्योंकि उन्हें तुरंत नकदी में नहीं बदला जा सकता है।)",
                "solution_gu": "(ગાણિતિક ગણતરી માટે અંગ્રેજી ઉકેલ જુઓ. પ્રવાહી મિલકતોની (Quick Assets) ગણતરી સ્ટોક અને અગાઉથી ચૂકવેલ ખર્ચને બાદ કરીને કરવામાં આવે છે કારણ કે તેને તરત રોકડમાં રૂપાંતરિત કરી શકાતા નથી.)",
                "id": "KOBJ_CBSE_ACC12_CH11_NUME_002"
            }
        ]
    }
    save_json('app_core/chapters/cbse_class12_accounts_ch11.json', data)

def gen_ch12():
    data = {
        "metadata": {
            "id": "cbse_class12_accounts_ch12",
            "title": "Cash Flow Statement",
            "title_hi": "नकदी प्रवाह विवरण",
            "title_gu": "રોકડ પ્રવાહ પત્રક",
            "subject": "Accountancy",
            "grade": "12",
            "board": "CBSE",
            "curriculum": ["CBSE"],
            "difficulty": "Master",
            "estimated_minutes": 180,
            "learning_outcomes": [
                "Understand the meaning and objectives of a Cash Flow Statement.",
                "Classify activities into Operating, Investing, and Financing.",
                "Prepare Cash Flow Statement as per AS-3 (Revised)."
            ]
        },
        "blocks": [
            {
                "type": "theory",
                "content": "A company can show ₹50 Crores in Net Profit on paper, but still go bankrupt because it has absolutely NO CASH in the bank! How is that possible? Because accounting is done on an 'Accrual Basis' (recording income even if cash isn't received yet).\nTo prevent this deadly illusion, Accounting Standard 3 (AS-3) forces large companies to prepare a **Cash Flow Statement**. It tracks the actual physical movement of Cash Inflows and Cash Outflows.",
                "content_hi": "एक कंपनी कागज पर ₹50 करोड़ का शुद्ध लाभ दिखा सकती है, लेकिन फिर भी दिवालिया हो सकती है क्योंकि उसके बैंक में बिल्कुल नकद (NO CASH) नहीं है! यह कैसे संभव है? क्योंकि लेखांकन 'उपार्जन आधार' (Accrual Basis) पर किया जाता है (आय दर्ज करना भले ही नकद अभी तक प्राप्त न हुआ हो)।\nइस घातक भ्रम को रोकने के लिए, लेखांकन मानक 3 (AS-3) बड़ी कंपनियों को **नकदी प्रवाह विवरण (Cash Flow Statement)** तैयार करने के लिए मजबूर करता है। यह कैश इनफ्लो और कैश आउटफ्लो के वास्तविक भौतिक आंदोलन को ट्रैक करता है।",
                "content_gu": "કંપની કાગળ પર ₹50 કરોડનો ચોખ્ખો નફો બતાવી શકે છે, પરંતુ તેમ છતાં નાદાર થઈ શકે છે કારણ કે તેની બેંકમાં બિલકુલ રોકડ (NO CASH) નથી! આ કેવી રીતે શક્ય છે? કારણ કે એકાઉન્ટિંગ 'ઉપાર્જિત ધોરણે' (Accrual Basis) કરવામાં આવે છે (જો રોકડ હજી સુધી પ્રાપ્ત ન થઈ હોય તો પણ આવક નોંધવી).\nઆ ઘાતક ભ્રમને રોકવા માટે, એકાઉન્ટિંગ સ્ટાન્ડર્ડ 3 (AS-3) મોટી કંપનીઓને **રોકડ પ્રવાહ પત્રક (Cash Flow Statement)** તૈયાર કરવાની ફરજ પાડે છે. તે રોકડ આવક (Inflow) અને રોકડ જાવક (Outflow) ની વાસ્તવિક હિલચાલને ટ્રેક કરે છે.",
                "id": "KOBJ_CBSE_ACC12_CH12_THEO_001"
            },
            {
                "type": "teacher_tip",
                "content": "The statement divides ALL cash movements into 3 simple activities:\n1. **Operating Activities:** Day-to-day main business (buying/selling goods).\n2. **Investing Activities:** Buying/selling long-term Assets (Land, Machinery, Investments).\n3. **Financing Activities:** Changing the Capital or Borrowings (Issuing shares, taking loans, paying dividends).",
                "content_hi": "विवरण सभी नकद आंदोलनों को 3 सरल गतिविधियों में विभाजित करता है:\n1. **परिचालन गतिविधियां (Operating):** दिन-प्रतिदिन का मुख्य व्यवसाय (माल खरीदना/बेचना)।\n2. **निवेश गतिविधियां (Investing):** लंबी अवधि की संपत्ति (भूमि, मशीनरी, निवेश) खरीदना/बेचना।\n3. **वित्तीय गतिविधियां (Financing):** पूंजी या उधार (शेयर जारी करना, ऋण लेना, लाभांश का भुगतान) को बदलना।",
                "content_gu": "આ પત્રક તમામ રોકડ હિલચાલને 3 સરળ પ્રવૃત્તિઓમાં વહેંચે છે:\n1. **કામગીરીની પ્રવૃત્તિઓ (Operating):** રોજિંદો મુખ્ય વ્યવસાય (માલની ખરીદી/વેચાણ).\n2. **રોકાણની પ્રવૃત્તિઓ (Investing):** લાંબા ગાળાની મિલકતો (જમીન, મશીનરી, રોકાણ) ખરીદવી/વેચવી.\n3. **નાણાકીય પ્રવૃત્તિઓ (Financing):** મૂડી અથવા ઉછીના નાણાંમાં ફેરફાર (શેર બહાર પાડવા, લોન લેવી, ડિવિડન્ડ ચૂકવવું).",
                "id": "KOBJ_CBSE_ACC12_CH12_TEAC_002"
            }
        ]
    }
    save_json('app_core/chapters/cbse_class12_accounts_ch12.json', data)

if __name__ == "__main__":
    gen_ch9()
    gen_ch10()
    gen_ch11()
    gen_ch12()
