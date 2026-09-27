import json

file_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_accounts_ch3.json"

new_mcqs = [
    {
        "type": "mcq",
        "question": "Goodwill is defined as:",
        "question_hi": "ख्याति को इस प्रकार परिभाषित किया गया है:",
        "question_gu": "પાઘડીની વ્યાખ્યા આ મુજબ આપવામાં આવે છે:",
        "options": ["A tangible asset", "An intangible asset", "A fictitious asset", "A current asset"],
        "options_hi": ["एक मूर्त संपत्ति", "एक अमूर्त संपत्ति", "एक काल्पनिक संपत्ति", "एक वर्तमान संपत्ति"],
        "options_gu": ["દ્રશ્ય મિલકત", "અદ્રશ્ય મિલકત", "અવાસ્તવિક મિલકત", "ચાલુ મિલકત"],
        "correct_index": 1,
        "explanation": "Goodwill is an intangible asset as it cannot be physically touched or seen.",
        "explanation_hi": "ख्याति एक अमूर्त संपत्ति है क्योंकि इसे भौतिक रूप से छुआ या देखा नहीं जा सकता है।",
        "explanation_gu": "પાઘડી એ એક અદ્રશ્ય મિલકત છે કારણ કે તેને ભૌતિક રીતે સ્પર્શ અથવા જોઈ શકાતી નથી."
    },
    {
        "type": "mcq",
        "question": "Which of the following is NOT a method of valuation of goodwill?",
        "question_hi": "निम्नलिखित में से कौन सा ख्याति के मूल्यांकन की विधि नहीं है?",
        "question_gu": "નીચેનામાંથી કઈ પાઘડીના મૂલ્યાંકનની પદ્ધતિ નથી?",
        "options": ["Average Profit Method", "Super Profit Method", "Capitalization Method", "Straight Line Method"],
        "options_hi": ["औसत लाभ विधि", "अधिमान लाभ विधि", "पूंजीकरण विधि", "सीधी रेखा विधि"],
        "options_gu": ["સરેરાશ નફાની પદ્ધતિ", "અધિક નફાની પદ્ધતિ", "મૂડીકરણની પદ્ધતિ", "સીધી લીટીની પદ્ધતિ"],
        "correct_index": 3,
        "explanation": "Straight Line Method is used for depreciation, not for goodwill valuation.",
        "explanation_hi": "सीधी रेखा विधि का उपयोग मूल्यह्रास के लिए किया जाता है, न कि ख्याति मूल्यांकन के लिए।",
        "explanation_gu": "સીધી લીટી પદ્ધતિનો ઉપયોગ ઘસારા માટે થાય છે, પાઘડીના મૂલ્યાંકન માટે નહીં."
    },
    {
        "type": "mcq",
        "question": "Super profit is the difference between:",
        "question_hi": "अधिमान लाभ किसके बीच का अंतर है:",
        "question_gu": "અધિક નફો એ કોની વચ્ચેનો તફાવત છે:",
        "options": ["Average Profit and Expected Profit", "Expected Profit and Normal Profit", "Average Profit and Normal Profit", "Capital Employed and Expected Profit"],
        "options_hi": ["औसत लाभ और अपेक्षित लाभ", "अपेक्षित लाभ और सामान्य लाभ", "औसत लाभ और सामान्य लाभ", "नियोजित पूंजी और अपेक्षित लाभ"],
        "options_gu": ["સરેરાશ નફો અને અપેક્ષિત નફો", "અપેક્ષિત નફો અને સામાન્ય નફો", "સરેરાશ નફો અને સામાન્ય નફો", "રોકાયેલી મૂડી અને અપેક્ષિત નફો"],
        "correct_index": 0,
        "explanation": "Super profit = Average Profit - Expected (Normal) Profit.",
        "explanation_hi": "अधिमान लाभ = औसत लाभ - अपेक्षित (सामान्य) लाभ।",
        "explanation_gu": "અધિક નફો = સરેરાશ નફો - અપેક્ષિત (સામાન્ય) નફો."
    },
    {
        "type": "mcq",
        "question": "Capital employed is equal to:",
        "question_hi": "नियोजित पूंजी किसके बराबर है:",
        "question_gu": "રોકાયેલી મૂડી કોની બરાબર છે:",
        "options": ["Total Assets - Total Liabilities", "Total Assets - Current Liabilities", "Total Tangible Assets - Total External Liabilities", "Total Current Assets - Total Current Liabilities"],
        "options_hi": ["कुल संपत्ति - कुल देनदारियां", "कुल संपत्ति - वर्तमान देनदारियां", "कुल मूर्त संपत्ति - कुल बाहरी देनदारियां", "कुल वर्तमान संपत्ति - कुल वर्तमान देनदारियां"],
        "options_gu": ["કુલ મિલકતો - કુલ જવાબદારીઓ", "કુલ મિલકતો - ચાલુ જવાબદારીઓ", "કુલ દ્રશ્ય મિલકતો - કુલ બાહ્ય જવાબદારીઓ", "કુલ ચાલુ મિલકતો - કુલ ચાલુ જવાબદારીઓ"],
        "correct_index": 2,
        "explanation": "Capital employed is calculated as Total Tangible Assets minus Total External Liabilities.",
        "explanation_hi": "नियोजित पूंजी की गणना कुल मूर्त संपत्ति से कुल बाहरी देनदारियों को घटाकर की जाती है।",
        "explanation_gu": "રોકાયેલી મૂડીની ગણતરી કુલ દ્રશ્ય મિલકતોમાંથી કુલ બાહ્ય જવાબદારીઓ બાદ કરીને કરવામાં આવે છે."
    },
    {
        "type": "mcq",
        "question": "Under which method are profits assigned weights?",
        "question_hi": "किस विधि के अंतर्गत लाभ को भार सौंपा जाता है?",
        "question_gu": "કઈ પદ્ધતિ હેઠળ નફાને ભાર આપવામાં આવે છે?",
        "options": ["Simple Average Method", "Weighted Average Method", "Super Profit Method", "Capitalization Method"],
        "options_hi": ["सरल औसत विधि", "भारित औसत विधि", "अधिमान लाभ विधि", "पूंजीकरण विधि"],
        "options_gu": ["સાદી સરેરાશ પદ્ધતિ", "ભારિત સરેરાશ પદ્ધતિ", "અધિક નફાની પદ્ધતિ", "મૂડીકરણની પદ્ધતિ"],
        "correct_index": 1,
        "explanation": "In the Weighted Average Method, different weights are assigned to the profits of different years.",
        "explanation_hi": "भारित औसत विधि में, विभिन्न वर्षों के लाभ को अलग-अलग भार सौंपा जाता है।",
        "explanation_gu": "ભારિત સરેરાશ પદ્ધતિમાં, જુદા જુદા વર્ષોના નફાને અલગ-અલગ ભાર આપવામાં આવે છે."
    },
    {
        "type": "mcq",
        "question": "If average profit is less than expected profit, what is the value of super profit?",
        "question_hi": "यदि औसत लाभ अपेक्षित लाभ से कम है, तो अधिमान लाभ का मूल्य क्या है?",
        "question_gu": "જો સરેરાશ નફો અપેક્ષિત નફા કરતા ઓછો હોય, તો અધિક નફાનું મૂલ્ય શું છે?",
        "options": ["Positive", "Zero", "Negative (No Goodwill)", "Equal to Average Profit"],
        "options_hi": ["सकारात्मक", "शून्य", "नकारात्मक (कोई ख्याति नहीं)", "औसत लाभ के बराबर"],
        "options_gu": ["ધન", "શૂન્ય", "ઋણ (કોઈ પાઘડી નથી)", "સરેરાશ નફા જેટલું"],
        "correct_index": 2,
        "explanation": "If average profit is less than expected, super profit is negative, meaning there is no goodwill.",
        "explanation_hi": "यदि औसत लाभ अपेक्षित से कम है, तो अधिमान लाभ नकारात्मक होता है, जिसका अर्थ है कोई ख्याति नहीं।",
        "explanation_gu": "જો સરેરાશ નફો અપેક્ષિત કરતાં ઓછો હોય, તો અધિક નફો ઋણ છે, જેનો અર્થ છે કે કોઈ પાઘડી નથી."
    },
    {
        "type": "mcq",
        "question": "Goodwill is an asset because:",
        "question_hi": "ख्याति एक संपत्ति है क्योंकि:",
        "question_gu": "પાઘડી એક મિલકત છે કારણ કે:",
        "options": ["It can be seen", "It helps in earning more profit", "It is fictitious", "It can be worn out"],
        "options_hi": ["इसे देखा जा सकता है", "यह अधिक लाभ कमाने में मदद करती है", "यह काल्पनिक है", "यह घिस सकती है"],
        "options_gu": ["તેને જોઈ શકાય છે", "તે વધુ નફો કમાવવામાં મદદ કરે છે", "તે અવાસ્તવિક છે", "તે ઘસાઈ શકે છે"],
        "correct_index": 1,
        "explanation": "Goodwill has real value as it helps the business earn more than normal profits.",
        "explanation_hi": "ख्याति का वास्तविक मूल्य होता है क्योंकि यह व्यवसाय को सामान्य लाभ से अधिक कमाने में मदद करती है।",
        "explanation_gu": "પાઘડીનું વાસ્તવિક મૂલ્ય હોય છે કારણ કે તે વ્યવસાયને સામાન્ય નફા કરતાં વધુ કમાવવામાં મદદ કરે છે."
    },
    {
        "type": "mcq",
        "question": "The need for valuation of goodwill arises during:",
        "question_hi": "ख्याति के मूल्यांकन की आवश्यकता कब होती है:",
        "question_gu": "પાઘડીના મૂલ્યાંકનની જરૂરિયાત ક્યારે ઊભી થાય છે:",
        "options": ["Admission of a partner", "Retirement of a partner", "Change in profit sharing ratio", "All of the above"],
        "options_hi": ["साझेदार का प्रवेश", "साझेदार की सेवानिवृत्ति", "लाभ विभाजन अनुपात में परिवर्तन", "ऊपर के सभी"],
        "options_gu": ["ભાગીદારનો પ્રવેશ", "ભાગીદારની નિવૃત્તિ", "નફા-નુકસાન વહેંચણીના પ્રમાણમાં ફેરફાર", "ઉપરોક્ત તમામ"],
        "correct_index": 3,
        "explanation": "Goodwill must be valued whenever there is a reconstitution of the partnership firm.",
        "explanation_hi": "साझेदारी फर्म के पुनर्गठन होने पर ख्याति का मूल्यांकन किया जाना चाहिए।",
        "explanation_gu": "જ્યારે પણ ભાગીદારી પેઢીનું પુનર્ગઠન થાય ત્યારે પાઘડીનું મૂલ્યાંકન થવું જોઈએ."
    },
    {
        "type": "mcq",
        "question": "Expected profit is calculated by:",
        "question_hi": "अपेक्षित लाभ की गणना कैसे की जाती है:",
        "question_gu": "અપેક્ષિત નફાની ગણતરી કઈ રીતે થાય છે:",
        "options": ["Capital Employed x Expected Rate of Return", "Average Profit x Expected Rate of Return", "Capital Employed / Expected Rate of Return", "Super Profit x Expected Rate of Return"],
        "options_hi": ["नियोजित पूंजी x अपेक्षित रिटर्न दर", "औसत लाभ x अपेक्षित रिटर्न दर", "नियोजित पूंजी / अपेक्षित रिटर्न दर", "अधिमान लाभ x अपेक्षित रिटर्न दर"],
        "options_gu": ["રોકાયેલી મૂડી x અપેક્ષિત વળતરનો દર", "સરેરાશ નફો x અપેક્ષિત વળતરનો દર", "રોકાયેલી મૂડી / અપેક્ષિત વળતરનો દર", "અધિક નફો x અપેક્ષિત વળતરનો દર"],
        "correct_index": 0,
        "explanation": "Expected profit = Capital employed × (Expected rate of return / 100).",
        "explanation_hi": "अपेक्षित लाभ = नियोजित पूंजी × (अपेक्षित रिटर्न दर / 100)।",
        "explanation_gu": "અપેક્ષિત નફો = રોકાયેલી મૂડી × (અપેક્ષિત વળતરનો દર / 100)."
    },
    {
        "type": "mcq",
        "question": "Location of business affects the value of goodwill.",
        "question_hi": "व्यवसाय का स्थान ख्याति के मूल्य को प्रभावित करता है।",
        "question_gu": "વ્યવસાયનું સ્થાન પાઘડીના મૂલ્યને અસર કરે છે.",
        "options": ["True", "False", "Partially True", "None of the above"],
        "options_hi": ["सत्य", "असत्य", "आंशिक रूप से सत्य", "इनमें से कोई नहीं"],
        "options_gu": ["સાચું", "ખોટું", "અંશતઃ સાચું", "આમાંથી કોઈ નહીં"],
        "correct_index": 0,
        "explanation": "A central or prime location usually generates more sales, increasing goodwill.",
        "explanation_hi": "एक केंद्रीय या मुख्य स्थान आमतौर पर अधिक बिक्री उत्पन्न करता है, जिससे ख्याति बढ़ती है।",
        "explanation_gu": "મુખ્ય સ્થાન સામાન્ય રીતે વધુ વેચાણ ઉત્પન્ન કરે છે, જેથી પાઘડી વધે છે."
    },
    {
        "type": "mcq",
        "question": "When profits show a continuously increasing trend, which method is best?",
        "question_hi": "जब लाभ लगातार बढ़ने की प्रवृत्ति दिखाते हैं, तो कौन सी विधि सबसे अच्छी है?",
        "question_gu": "જ્યારે નફો સતત વધતો હોય, ત્યારે કઈ પદ્ધતિ શ્રેષ્ઠ છે?",
        "options": ["Simple Average Method", "Weighted Average Method", "Super Profit Method", "Capitalization Method"],
        "options_hi": ["सरल औसत विधि", "भारित औसत विधि", "अधिमान लाभ विधि", "पूंजीकरण विधि"],
        "options_gu": ["સાદી સરેરાશ પદ્ધતિ", "ભારિત સરેરાશ પદ્ધતિ", "અધિક નફાની પદ્ધતિ", "મૂડીકરણની પદ્ધતિ"],
        "correct_index": 1,
        "explanation": "Weighted average method gives more weight to recent profits, accurately reflecting growth.",
        "explanation_hi": "भारित औसत विधि हाल के लाभ को अधिक भार देती है, जो वृद्धि को सटीक रूप से दर्शाती है।",
        "explanation_gu": "ભારિત સરેરાશ પદ્ધતિ તાજેતરના નફાને વધુ ભાર આપે છે, જે વૃદ્ધિને ચોક્કસપણે દર્શાવે છે."
    },
    {
        "type": "mcq",
        "question": "Valuation of goodwill is necessary for a sole proprietorship when:",
        "question_hi": "एकल स्वामित्व के लिए ख्याति का मूल्यांकन आवश्यक है जब:",
        "question_gu": "એકાકી વેપારી માટે પાઘડીનું મૂલ્યાંકન જરૂરી છે જ્યારે:",
        "options": ["Business is started", "Business is expanded", "Business is sold", "None of the above"],
        "options_hi": ["व्यवसाय शुरू किया जाता है", "व्यवसाय का विस्तार किया जाता है", "व्यवसाय बेचा जाता है", "इनमें से कोई नहीं"],
        "options_gu": ["વ્યવસાય શરૂ થાય છે", "વ્યવસાયનું વિસ્તરણ થાય છે", "વ્યવસાય વેચાય છે", "આમાંથી કોઈ નહીં"],
        "correct_index": 2,
        "explanation": "Goodwill is valued when a business is sold so the owner gets paid for their reputation.",
        "explanation_hi": "जब कोई व्यवसाय बेचा जाता है तो ख्याति का मूल्यांकन किया जाता है ताकि मालिक को उसकी प्रतिष्ठा के लिए भुगतान मिल सके।",
        "explanation_gu": "જ્યારે વ્યવસાય વેચાય છે ત્યારે પાઘડીનું મૂલ્યાંકન કરવામાં આવે છે જેથી માલિકને તેની પ્રતિષ્ઠા માટે ચૂકવણી મળે."
    },
    {
        "type": "mcq",
        "question": "Capitalized value of profit = ",
        "question_hi": "लाभ का पूंजीकृत मूल्य = ",
        "question_gu": "નફાનું મૂડીકૃત મૂલ્ય = ",
        "options": ["(Average Profit / Expected Rate of Return) * 100", "(Super Profit / Expected Rate of Return) * 100", "Capital Employed - Average Profit", "Average Profit - Expected Profit"],
        "options_hi": ["(औसत लाभ / अपेक्षित रिटर्न दर) * 100", "(अधिमान लाभ / अपेक्षित रिटर्न दर) * 100", "नियोजित पूंजी - औसत लाभ", "औसत लाभ - अपेक्षित लाभ"],
        "options_gu": ["(સરેરાશ નફો / અપેક્ષિત વળતરનો દર) * 100", "(અધિક નફો / અપેક્ષિત વળતરનો દર) * 100", "રોકાયેલી મૂડી - સરેરાશ નફો", "સરેરાશ નફો - અપેક્ષિત નફો"],
        "correct_index": 0,
        "explanation": "Capitalized value is found by capitalizing the average profit at the expected rate of return.",
        "explanation_hi": "पूंजीकृत मूल्य अपेक्षित रिटर्न दर पर औसत लाभ का पूंजीकरण करके पाया जाता है।",
        "explanation_gu": "મૂડીકૃત મૂલ્ય સરેરાશ નફાને અપેક્ષિત વળતરના દર પર મૂડીકૃત કરીને મેળવવામાં આવે છે."
    },
    {
        "type": "mcq",
        "question": "Goodwill = Capitalized Value of Profit minus:",
        "question_hi": "ख्याति = लाभ का पूंजीकृत मूल्य घटाव:",
        "question_gu": "પાઘડી = નફાનું મૂડીકૃત મૂલ્ય માઈનસ:",
        "options": ["Average Profit", "Capital Employed", "Super Profit", "Current Liabilities"],
        "options_hi": ["औसत लाभ", "नियोजित पूंजी", "अधिमान लाभ", "वर्तमान देनदारियां"],
        "options_gu": ["સરેરાશ નફો", "રોકાયેલી મૂડી", "અધિક નફો", "ચાલુ જવાબદારીઓ"],
        "correct_index": 1,
        "explanation": "Under Capitalization of Average Profit Method, Goodwill = Capitalized Value - Capital Employed.",
        "explanation_hi": "औसत लाभ के पूंजीकरण विधि के तहत, ख्याति = पूंजीकृत मूल्य - नियोजित पूंजी।",
        "explanation_gu": "સરેરાશ નફાના મૂડીકરણની પદ્ધતિ હેઠળ, પાઘડી = મૂડીકૃત મૂલ્ય - રોકાયેલી મૂડી."
    },
    {
        "type": "mcq",
        "question": "If super profit is capitalized, what is the formula for Goodwill?",
        "question_hi": "यदि अधिमान लाभ का पूंजीकरण किया जाता है, तो ख्याति का सूत्र क्या है?",
        "question_gu": "જો અધિક નફાનું મૂડીકરણ કરવામાં આવે, તો પાઘડીનું સૂત્ર શું છે?",
        "options": ["Super Profit * Number of Years Purchase", "(Super Profit / Expected Rate of Return) * 100", "Capital Employed - Super Profit", "Average Profit - Super Profit"],
        "options_hi": ["अधिमान लाभ * खरीद के वर्षों की संख्या", "(अधिमान लाभ / अपेक्षित रिटर्न दर) * 100", "नियोजित पूंजी - अधिमान लाभ", "औसत लाभ - अधिमान लाभ"],
        "options_gu": ["અધિક નફો * ખરીદીના વર્ષોની સંખ્યા", "(અધિક નફો / અપેક્ષિત વળતરનો દર) * 100", "રોકાયેલી મૂડી - અધિક નફો", "સરેરાશ નફો - અધિક નફો"],
        "correct_index": 1,
        "explanation": "Under capitalization of super profit method, Goodwill = (Super Profit / Expected Rate of Return) * 100.",
        "explanation_hi": "अधिमान लाभ के पूंजीकरण विधि के तहत, ख्याति = (अधिमान लाभ / अपेक्षित रिटर्न दर) * 100।",
        "explanation_gu": "અધિક નફાના મૂડીકરણની પદ્ધતિ હેઠળ, પાઘડી = (અધિક નફો / અપેક્ષિત વળતરનો દર) * 100."
    },
    {
        "type": "mcq",
        "question": "An older business usually has:",
        "question_hi": "एक पुराने व्यवसाय में आमतौर पर होता है:",
        "question_gu": "જૂના વ્યવસાયમાં સામાન્ય રીતે હોય છે:",
        "options": ["Less goodwill", "More goodwill", "Zero goodwill", "Negative goodwill"],
        "options_hi": ["कम ख्याति", "अधिक ख्याति", "शून्य ख्याति", "नकारात्मक ख्याति"],
        "options_gu": ["ઓછી પાઘડી", "વધુ પાઘડી", "શૂન્ય પાઘડી", "ઋણ પાઘડી"],
        "correct_index": 1,
        "explanation": "An older business is more known to customers, generating higher reputation and goodwill.",
        "explanation_hi": "एक पुराना व्यवसाय ग्राहकों के लिए अधिक जाना जाता है, जो उच्च प्रतिष्ठा और ख्याति उत्पन्न करता है।",
        "explanation_gu": "જૂનો વ્યવસાય ગ્રાહકો માટે વધુ જાણીતો છે, જે ઉચ્ચ પ્રતિષ્ઠા અને પાઘડી ઉત્પન્ન કરે છે."
    },
    {
        "type": "mcq",
        "question": "Is goodwill amortized?",
        "question_hi": "क्या ख्याति का परिशोधन किया जाता है?",
        "question_gu": "શું પાઘડીને માંડી વાળવામાં આવે છે?",
        "options": ["Yes, it is amortized over its useful life", "No, it is depreciated", "No, it is kept forever", "Yes, it is depreciated over 1 year"],
        "options_hi": ["हाँ, इसके उपयोगी जीवन में इसका परिशोधन किया जाता है", "नहीं, इसका मूल्यह्रास किया जाता है", "नहीं, इसे हमेशा के लिए रखा जाता है", "हाँ, इसका 1 वर्ष में मूल्यह्रास किया जाता है"],
        "options_gu": ["હા, તેના ઉપયોગી જીવનકાળ દરમિયાન તેને માંડી વાળવામાં આવે છે", "ના, તેના પર ઘસારો ગણાય છે", "ના, તે કાયમ માટે રાખવામાં આવે છે", "હા, તેના પર 1 વર્ષમાં ઘસારો ગણાય છે"],
        "correct_index": 0,
        "explanation": "Goodwill is an intangible asset and is amortized (written off) over its estimated useful economic life.",
        "explanation_hi": "ख्याति एक अमूर्त संपत्ति है और इसके अनुमानित उपयोगी आर्थिक जीवन पर इसका परिशोधन (लिखित) किया जाता है।",
        "explanation_gu": "પાઘડી એક અદ્રશ્ય મિલકત છે અને તેના અંદાજિત ઉપયોગી આર્થિક જીવનકાળ દરમિયાન તેને માંડી વાળવામાં આવે છે."
    },
    {
        "type": "mcq",
        "question": "Abnormal loss should be __________ to past profits to calculate average profit.",
        "question_hi": "औसत लाभ की गणना के लिए पिछले लाभों में असामान्य हानि को __________ किया जाना चाहिए।",
        "question_gu": "સરેરાશ નફાની ગણતરી કરવા માટે ભૂતકાળના નફામાં અસામાન્ય નુકસાનને __________ કરવું જોઈએ.",
        "options": ["Added back", "Deducted", "Ignored", "Multiplied"],
        "options_hi": ["वापस जोड़ा", "काटा", "अनदेखा", "गुणा"],
        "options_gu": ["ઉમેરવું", "બાદ કરવું", "અવગણવું", "ગુણાકાર કરવો"],
        "correct_index": 0,
        "explanation": "Abnormal losses are not regular, so they are added back to find the normal business profit.",
        "explanation_hi": "असामान्य नुकसान नियमित नहीं हैं, इसलिए सामान्य व्यावसायिक लाभ खोजने के लिए उन्हें वापस जोड़ा जाता है।",
        "explanation_gu": "અસામાન્ય નુકસાન નિયમિત નથી, તેથી સામાન્ય વ્યવસાયિક નફો શોધવા માટે તેને પાછો ઉમેરવામાં આવે છે."
    },
    {
        "type": "mcq",
        "question": "Abnormal income should be __________ from past profits.",
        "question_hi": "पिछले लाभों में से असामान्य आय को __________ किया जाना चाहिए।",
        "question_gu": "ભૂતકાળના નફામાંથી અસામાન્ય આવકને __________ કરવી જોઈએ.",
        "options": ["Added", "Deducted", "Ignored", "Doubled"],
        "options_hi": ["जोड़ा", "काटा", "अनदेखा", "दोगुना"],
        "options_gu": ["ઉમેરવી", "બાદ કરવી", "અવગણવી", "બમણી કરવી"],
        "correct_index": 1,
        "explanation": "Abnormal income is a one-time gain and must be deducted to find the normal operating profit.",
        "explanation_hi": "असामान्य आय एक बार का लाभ है और सामान्य परिचालन लाभ खोजने के लिए इसे काटा जाना चाहिए।",
        "explanation_gu": "અસામાન્ય આવક એક વખતનો લાભ છે અને સામાન્ય કામગીરીનો નફો શોધવા માટે તેને બાદ કરવી જોઈએ."
    },
    {
        "type": "mcq",
        "question": "If average profit is Rs. 50,000 and expected profit is Rs. 30,000, Super profit is:",
        "question_hi": "यदि औसत लाभ 50,000 रुपये है और अपेक्षित लाभ 30,000 रुपये है, तो अधिमान लाभ है:",
        "question_gu": "જો સરેરાશ નફો 50,000 રૂપિયા છે અને અપેક્ષિત નફો 30,000 રૂપિયા છે, તો અધિક નફો છે:",
        "options": ["Rs. 80,000", "Rs. 20,000", "Rs. 50,000", "Rs. 30,000"],
        "options_hi": ["80,000 रुपये", "20,000 रुपये", "50,000 रुपये", "30,000 रुपये"],
        "options_gu": ["80,000 રૂપિયા", "20,000 રૂપિયા", "50,000 રૂપિયા", "30,000 રૂપિયા"],
        "correct_index": 1,
        "explanation": "Super Profit = Average Profit - Expected Profit = 50,000 - 30,000 = 20,000.",
        "explanation_hi": "अधिमान लाभ = औसत लाभ - अपेक्षित लाभ = 50,000 - 30,000 = 20,000।",
        "explanation_gu": "અધિક નફો = સરેરાશ નફો - અપેક્ષિત નફો = 50,000 - 30,000 = 20,000."
    },
    {
        "type": "mcq",
        "question": "A business having a monopoly will usually have:",
        "question_hi": "एकाधिकार वाले व्यवसाय में आमतौर पर होता है:",
        "question_gu": "ઈજારો ધરાવતા વ્યવસાયમાં સામાન્ય રીતે હોય છે:",
        "options": ["High goodwill", "Low goodwill", "No goodwill", "Negative goodwill"],
        "options_hi": ["उच्च ख्याति", "कम ख्याति", "कोई ख्याति नहीं", "नकारात्मक ख्याति"],
        "options_gu": ["ઉચ્ચ પાઘડી", "ઓછી પાઘડી", "કોઈ પાઘડી નહીં", "ઋણ પાઘડી"],
        "correct_index": 0,
        "explanation": "Monopoly allows a business to earn higher profits due to lack of competition, increasing its goodwill.",
        "explanation_hi": "एकाधिकार एक व्यवसाय को प्रतिस्पर्धा की कमी के कारण अधिक लाभ कमाने की अनुमति देता है, जिससे उसकी ख्याति बढ़ती है।",
        "explanation_gu": "ઈજારો વ્યવસાયને હરીફાઈના અભાવને કારણે વધુ નફો કમાવવાની મંજૂરી આપે છે, જેથી તેની પાઘડી વધે છે."
    },
    {
        "type": "mcq",
        "question": "Which factor does NOT affect the valuation of goodwill?",
        "question_hi": "कौन सा कारक ख्याति के मूल्यांकन को प्रभावित नहीं करता है?",
        "question_gu": "કયું પરિબળ પાઘડીના મૂલ્યાંકનને અસર કરતું નથી?",
        "options": ["Efficiency of Management", "Market Situation", "Location of Business", "Number of Employees"],
        "options_hi": ["प्रबंधन की दक्षता", "बाजार की स्थिति", "व्यवसाय का स्थान", "कर्मचारियों की संख्या"],
        "options_gu": ["સંચાલનની કાર્યક્ષમતા", "બજારની સ્થિતિ", "વ્યવસાયનું સ્થાન", "કર્મચારીઓની સંખ્યા"],
        "correct_index": 3,
        "explanation": "The number of employees alone does not dictate profitability or reputation directly.",
        "explanation_hi": "अकेले कर्मचारियों की संख्या सीधे लाभप्रदता या प्रतिष्ठा को निर्धारित नहीं करती है।",
        "explanation_gu": "ફક્ત કર્મચારીઓની સંખ્યા સીધી નફાકારકતા અથવા પ્રતિષ્ઠા નક્કી કરતી નથી."
    },
    {
        "type": "mcq",
        "question": "The value of goodwill is subjective.",
        "question_hi": "ख्याति का मूल्य व्यक्तिपरक है।",
        "question_gu": "પાઘડીનું મૂલ્ય વ્યક્તિલક્ષી છે.",
        "options": ["True", "False", "Only in partnerships", "Only for companies"],
        "options_hi": ["सत्य", "असत्य", "केवल साझेदारी में", "केवल कंपनियों के लिए"],
        "options_gu": ["સાચું", "ખોટું", "માત્ર ભાગીદારીમાં", "માત્ર કંપનીઓ માટે"],
        "correct_index": 0,
        "explanation": "Since goodwill is intangible and based on estimation of future profits, its valuation involves personal judgment.",
        "explanation_hi": "चूंकि ख्याति अमूर्त है और भविष्य के लाभों के अनुमान पर आधारित है, इसके मूल्यांकन में व्यक्तिगत निर्णय शामिल है।",
        "explanation_gu": "કારણ કે પાઘડી અદ્રશ્ય છે અને ભવિષ્યના નફાના અંદાજ પર આધારિત છે, તેના મૂલ્યાંકનમાં વ્યક્તિગત નિર્ણય શામેલ છે."
    },
    {
        "type": "mcq",
        "question": "Self-generated goodwill is:",
        "question_hi": "स्व-निर्मित ख्याति है:",
        "question_gu": "સ્વ-ઉત્પન્ન પાઘડી છે:",
        "options": ["Recorded in books", "Not recorded in books", "Amortized immediately", "Treated as a liability"],
        "options_hi": ["पुस्तकों में दर्ज की जाती है", "पुस्तकों में दर्ज नहीं की जाती है", "तुरंत परिशोधित की जाती है", "एक दायित्व के रूप में माना जाता है"],
        "options_gu": ["ચોપડે નોંધાયેલ છે", "ચોપડે નોંધાયેલ નથી", "તરત જ માંડી વાળવામાં આવે છે", "જવાબદારી તરીકે ગણવામાં આવે છે"],
        "correct_index": 1,
        "explanation": "As per accounting standards, only purchased goodwill is recorded in the books of accounts.",
        "explanation_hi": "लेखांकन मानकों के अनुसार, केवल खरीदी गई ख्याति को खातों की पुस्तकों में दर्ज किया जाता है।",
        "explanation_gu": "હિસાબી ધોરણો મુજબ, માત્ર ખરીદેલી પાઘડી જ હિસાબી ચોપડાઓમાં નોંધવામાં આવે છે."
    },
    {
        "type": "mcq",
        "question": "Purchased goodwill is recorded in the books because:",
        "question_hi": "खरीदी गई ख्याति को पुस्तकों में दर्ज किया जाता है क्योंकि:",
        "question_gu": "ખરીદેલી પાઘડી ચોપડે નોંધવામાં આવે છે કારણ કે:",
        "options": ["It is free", "Consideration in money or money's worth has been paid for it", "It is fictitious", "It is self-generated"],
        "options_hi": ["यह मुफ्त है", "इसके लिए पैसे या पैसे के मूल्य में प्रतिफल का भुगतान किया गया है", "यह काल्पनिक है", "यह स्व-निर्मित है"],
        "options_gu": ["તે મફત છે", "તેના માટે નાણાં અથવા નાણાંના મૂલ્યમાં અવેજ ચૂકવવામાં આવેલ છે", "તે અવાસ્તવિક છે", "તે સ્વ-ઉત્પન્ન છે"],
        "correct_index": 1,
        "explanation": "Only assets for which a financial value has been paid can be recorded as assets.",
        "explanation_hi": "केवल उन्हीं संपत्तियों को संपत्ति के रूप में दर्ज किया जा सकता है जिनके लिए वित्तीय मूल्य का भुगतान किया गया है।",
        "explanation_gu": "જે મિલકતો માટે નાણાકીય મૂલ્ય ચૂકવવામાં આવ્યું હોય તેને જ મિલકત તરીકે નોંધી શકાય છે."
    },
    {
        "type": "mcq",
        "question": "Goodwill shown in the old balance sheet at the time of admission of a partner is:",
        "question_hi": "साझेदार के प्रवेश के समय पुरानी बैलेंस शीट में दिखाई गई ख्याति है:",
        "question_gu": "ભાગીદારના પ્રવેશ સમયે જૂના પાકા સરવૈયામાં દર્શાવેલ પાઘડી છે:",
        "options": ["Distributed among old partners", "Written off among old partners in old ratio", "Kept as it is", "Given to the new partner"],
        "options_hi": ["पुराने भागीदारों के बीच वितरित", "पुराने अनुपात में पुराने भागीदारों के बीच बट्टे खाते में डाल दी गई", "जैसी है वैसी ही रखी गई", "नए भागीदार को दी गई"],
        "options_gu": ["જૂના ભાગીદારો વચ્ચે વહેંચવામાં આવેલ", "જૂના પ્રમાણમાં જૂના ભાગીદારો વચ્ચે માંડી વાળેલ", "તેમ જ રાખવામાં આવેલ", "નવા ભાગીદારને આપેલ"],
        "correct_index": 1,
        "explanation": "Existing goodwill is typically written off to old partners' capital accounts in their old profit sharing ratio.",
        "explanation_hi": "मौजूदा ख्याति को आमतौर पर पुराने लाभ साझाकरण अनुपात में पुराने भागीदारों के पूंजी खातों में बट्टे खाते में डाल दिया जाता है।",
        "explanation_gu": "હાલની પાઘડી સામાન્ય રીતે જૂના નફા-નુકસાન વહેંચણીના પ્રમાણમાં જૂના ભાગીદારોના મૂડી ખાતે માંડી વાળવામાં આવે છે."
    },
    {
        "type": "mcq",
        "question": "Under Super Profit method, goodwill is valued by multiplying Super Profit by:",
        "question_hi": "अधिमान लाभ विधि के अंतर्गत, ख्याति का मूल्यांकन अधिमान लाभ को गुणा करके किया जाता है:",
        "question_gu": "અધિક નફાની પદ્ધતિ હેઠળ, પાઘડીનું મૂલ્યાંકન અધિક નફાને ગુણીને કરવામાં આવે છે:",
        "options": ["Expected Rate of Return", "Number of years of purchase", "Capital Employed", "Average Profit"],
        "options_hi": ["अपेक्षित रिटर्न दर", "खरीद के वर्षों की संख्या", "नियोजित पूंजी", "औसत लाभ"],
        "options_gu": ["અપેક્ષિત વળતરનો દર", "ખરીદીના વર્ષોની સંખ્યા", "રોકાયેલી મૂડી", "સરેરાશ નફો"],
        "correct_index": 1,
        "explanation": "Goodwill = Super Profit × Number of years of purchase.",
        "explanation_hi": "ख्याति = अधिमान लाभ × खरीद के वर्षों की संख्या।",
        "explanation_gu": "પાઘડી = અધિક નફો × ખરીદીના વર્ષોની સંખ્યા."
    },
    {
        "type": "mcq",
        "question": "Which of these businesses is likely to have higher goodwill?",
        "question_hi": "इनमें से किस व्यवसाय में उच्च ख्याति होने की संभावना है?",
        "question_gu": "આમાંથી કયા વ્યવસાયમાં ઉચ્ચ પાઘડી હોવાની સંભાવના છે?",
        "options": ["A business selling essential daily goods", "A risky business", "A new start-up", "A loss-making company"],
        "options_hi": ["आवश्यक दैनिक सामान बेचने वाला व्यवसाय", "एक जोखिम भरा व्यवसाय", "एक नया स्टार्ट-अप", "एक नुकसान कमाने वाली कंपनी"],
        "options_gu": ["રોજબરોજની જરૂરી વસ્તુઓ વેચતો વ્યવસાય", "જોખમી વ્યવસાય", "નવો સ્ટાર્ટ-અપ", "નુકસાન કરતી કંપની"],
        "correct_index": 0,
        "explanation": "Businesses with stable and continuous demand (like daily essentials) tend to have more consistent profits and higher goodwill.",
        "explanation_hi": "स्थिर और निरंतर मांग वाले व्यवसायों (जैसे दैनिक आवश्यक वस्तुएं) में अधिक सुसंगत लाभ और उच्च ख्याति होती है।",
        "explanation_gu": "સ્થિર અને સતત માંગવાળા વ્યવસાયો (જેમ કે રોજબરોજની વસ્તુઓ) સામાન્ય રીતે વધુ સુસંગત નફો અને ઉચ્ચ પાઘડી ધરાવે છે."
    },
    {
        "type": "mcq",
        "question": "If capital employed is Rs. 10,00,000 and Expected rate of return is 10%, the expected profit is:",
        "question_hi": "यदि नियोजित पूंजी 10,00,000 रुपये है और अपेक्षित रिटर्न दर 10% है, तो अपेक्षित लाभ है:",
        "question_gu": "જો રોકાયેલી મૂડી 10,00,000 રૂપિયા છે અને અપેક્ષિત વળતરનો દર 10% છે, તો અપેક્ષિત નફો છે:",
        "options": ["Rs. 1,00,000", "Rs. 10,00,000", "Rs. 10,000", "Rs. 1,10,000"],
        "options_hi": ["1,00,000 रुपये", "10,00,000 रुपये", "10,000 रुपये", "1,10,000 रुपये"],
        "options_gu": ["1,00,000 રૂપિયા", "10,00,000 રૂપિયા", "10,000 રૂપિયા", "1,10,000 રૂપિયા"],
        "correct_index": 0,
        "explanation": "Expected profit = 10,00,000 * 10% = 1,00,000.",
        "explanation_hi": "अपेक्षित लाभ = 10,00,000 * 10% = 1,00,000।",
        "explanation_gu": "અપેક્ષિત નફો = 10,00,000 * 10% = 1,00,000."
    },
    {
        "type": "mcq",
        "question": "The total of weights in Weighted Average Method is calculated to:",
        "question_hi": "भारित औसत विधि में भार का कुल योग की गणना की जाती है:",
        "question_gu": "ભારિત સરેરાશ પદ્ધતિમાં ભારના કુલ સરવાળાની ગણતરી કરવામાં આવે છે:",
        "options": ["Divide total weighted profit", "Multiply total profit", "Add to capital employed", "Subtract from super profit"],
        "options_hi": ["कुल भारित लाभ को विभाजित करने के लिए", "कुल लाभ को गुणा करने के लिए", "नियोजित पूंजी में जोड़ने के लिए", "अधिमान लाभ से घटाने के लिए"],
        "options_gu": ["કુલ ભારિત નફાને ભાગવા માટે", "કુલ નફાને ગુણવા માટે", "રોકાયેલી મૂડીમાં ઉમેરવા માટે", "અધિક નફામાંથી બાદ કરવા માટે"],
        "correct_index": 0,
        "explanation": "Weighted Average Profit = Total Weighted Profit / Total of Weights.",
        "explanation_hi": "भारित औसत लाभ = कुल भारित लाभ / भार का कुल योग।",
        "explanation_gu": "ભારિત સરેરાશ નફો = કુલ ભારિત નફો / ભારનો કુલ સરવાળો."
    }
]

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Find highest existing MCQ index to append safely
# (In the block IDs we just generate new ones like BLK_CH3_NEW_MCQ_01 etc)

for idx, mcq in enumerate(new_mcqs):
    mcq["id"] = f"BLK_CH3_NEW_MCQ_{idx+1:03d}"
    
    # We must format to fit the block schema in Shine Academy (No content wrapper as per Rule 2)
    # The fields are already flat as per my dictionary.
    data["blocks"].append(mcq)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_mcqs)} MCQs to {file_path}")
