import json
import os

blocks = [
    {
        "id": "ACC_CH12_01_HOOK",
        "type": "theory",
        "title": "Introduction to Ratios",
        "title_hi": "अनुपातों का परिचय",
        "title_gu": "ગુણોત્તરનો પરિચય",
        "body": "Have you ever wondered how investors decide whether a company is doing well? Looking at raw numbers like profit can be confusing. That's why we use 'Ratios'. A ratio is a mathematical relationship between two accounting figures.",
        "body_hi": "क्या आपने कभी सोचा है कि निवेशक कैसे तय करते हैं कि कोई कंपनी अच्छा कर रही है? मुनाफे जैसे कच्चे नंबरों को देखना भ्रमित करने वाला हो सकता है। इसलिए हम 'अनुपात' का उपयोग करते हैं। अनुपात दो लेखांकन आंकड़ों के बीच एक गणितीय संबंध है।",
        "body_gu": "શું તમે ક્યારેય વિચાર્યું છે કે રોકાણકારો કેવી રીતે નક્કી કરે છે કે કંપની સારું કામ કરી રહી છે? નફા જેવા કાચા નંબરો જોવું મૂંઝવણભર્યું હોઈ શકે છે. તેથી જ આપણે 'ગુણોત્તર' નો ઉપયોગ કરીએ છીએ. ગુણોત્તર એ બે એકાઉન્ટિંગ આંકડા વચ્ચેનો ગાણિતિક સંબંધ છે."
    },
    {
        "id": "ACC_CH12_02_SOCRATIC",
        "type": "theory",
        "title": "Think About It!",
        "title_hi": "इसके बारे में सोचो!",
        "title_gu": "આના વિશે વિચારો!",
        "body": "If Company A makes ₹90,000 profit and Company B makes ₹90,000 profit, are they equally successful? What if Company A had sales of ₹3,00,000 and Company B had sales of ₹9,00,000? Clearly, Company A is more efficient. This relative comparison is the essence of Ratio Analysis.",
        "body_hi": "यदि कंपनी A ₹90,000 का लाभ कमाती है और कंपनी B ₹90,000 का लाभ कमाती है, तो क्या वे समान रूप से सफल हैं? क्या होगा यदि कंपनी A की बिक्री ₹3,00,000 थी और कंपनी B की बिक्री ₹9,00,000 थी? स्पष्ट रूप से, कंपनी A अधिक कुशल है। यह सापेक्ष तुलना अनुपात विश्लेषण का सार है।",
        "body_gu": "જો કંપની A ₹90,000 નો નફો કરે છે અને કંપની B ₹90,000 નો નફો કરે છે, તો શું તેઓ સમાન રીતે સફળ છે? જો કંપની A નું વેચાણ ₹3,00,000 હોય અને કંપની B નું વેચાણ ₹9,00,000 હોય તો શું? સ્પષ્ટ છે કે, કંપની A વધુ કાર્યક્ષમ છે. આ સાપેક્ષ સરખામણી એ ગુણોત્તર વિશ્લેષણનો સાર છે."
    },
    {
        "id": "ACC_CH12_03_REVEAL",
        "type": "definition",
        "title": "Peculiarity of Ratios",
        "title_hi": "अनुपातों की विशिष्टता",
        "title_gu": "ગુણોત્તરની વિશિષ્ટતા",
        "body": "An individual ratio does not indicate any favourable or adverse situation on its own. It must be compared with a standard (like past results, industry averages, or competitors' ratios) to be meaningful.",
        "body_hi": "एक व्यक्तिगत अनुपात अपने आप में किसी अनुकूल या प्रतिकूल स्थिति का संकेत नहीं देता है। सार्थक होने के लिए इसकी तुलना एक मानक (जैसे पिछले परिणाम, उद्योग के औसत या प्रतिस्पर्धियों के अनुपात) से की जानी चाहिए।",
        "body_gu": "એક વ્યક્તિગત ગુણોત્તર તેના પોતાના પર કોઈપણ અનુકૂળ અથવા પ્રતિકૂળ પરિસ્થિતિનો સંકેત આપતો નથી. અર્થપૂર્ણ બનવા માટે તેની સરખામણી પ્રમાણભૂત (જેમ કે ભૂતકાળના પરિણામો, ઉદ્યોગની સરેરાશ અથવા સ્પર્ધકોના ગુણોત્તર) સાથે થવી જોઈએ."
    },
    {
        "id": "ACC_CH12_04_CHECK",
        "type": "mcq",
        "question": "An individual ratio without comparison is:",
        "question_hi": "तुलना के बिना एक व्यक्तिगत अनुपात है:",
        "question_gu": "સરખામણી વિના એક વ્યક્તિગત ગુણોત્તર છે:",
        "options": [
            "Always highly useful",
            "Meaningless on its own",
            "A guarantee of profit",
            "A complete financial statement"
        ],
        "options_hi": [
            "हमेशा अत्यधिक उपयोगी",
            "अपने आप में अर्थहीन",
            "लाभ की गारंटी",
            "एक पूर्ण वित्तीय विवरण"
        ],
        "options_gu": [
            "હંમેશા અત્યંત ઉપયોગી",
            "પોતાની જાતે અર્થહીન",
            "નફાની ગેરંટી",
            "સંપૂર્ણ નાણાકીય નિવેદન"
        ],
        "correct_index": 1,
        "explanation": "A ratio must be compared against standards (past performance, competitors, industry) to provide a meaningful interpretation.",
        "explanation_hi": "सार्थक व्याख्या प्रदान करने के लिए अनुपात की तुलना मानकों (पिछले प्रदर्शन, प्रतिस्पर्धियों, उद्योग) से की जानी चाहिए।",
        "explanation_gu": "અર્થપૂર્ણ અર્થઘટન પ્રદાન કરવા માટે ગુણોત્તરની સરખામણી ધોરણો (ભૂતકાળની કામગીરી, સ્પર્ધકો, ઉદ્યોગ) સામે કરવી જોઈએ."
    },
    {
        "id": "ACC_CH12_05_THEORY",
        "type": "theory",
        "title": "Objectives & Limitations",
        "title_hi": "उद्देश्य और सीमाएँ",
        "title_gu": "ઉદ્દેશ્યો અને મર્યાદાઓ",
        "body": "Objectives of Ratio Analysis: Simplifies financial statements, helps know profitability, liquidity, solvency, operating efficiency, and aids in forecasting and inter-firm comparison. Limitations: Relies on historical data, ignores qualitative factors (like employee honesty), and ignores price changes (inflation).",
        "body_hi": "अनुपात विश्लेषण के उद्देश्य: वित्तीय विवरणों को सरल बनाता है, लाभप्रदता, तरलता, शोधनक्षमता, परिचालन दक्षता जानने में मदद करता है, और पूर्वानुमान और अंतर-फर्म तुलना में सहायता करता है। सीमाएँ: ऐतिहासिक डेटा पर निर्भर करता है, गुणात्मक कारकों (जैसे कर्मचारी की ईमानदारी) को नज़रअंदाज़ करता है, और मूल्य परिवर्तन (मुद्रास्फीति) को अनदेखा करता है।",
        "body_gu": "ગુણોત્તર વિશ્લેષણના ઉદ્દેશ્યો: નાણાકીય નિવેદનોને સરળ બનાવે છે, નફાકારકતા, પ્રવાહિતા, સદ્ધરતા, કાર્યકારી કાર્યક્ષમતા જાણવામાં મદદ કરે છે અને આગાહી અને આંતર-પેઢી સરખામણીમાં મદદ કરે છે. મર્યાદાઓ: ઐતિહાસિક ડેટા પર આધાર રાખે છે, ગુણાત્મક પરિબળો (જેમ કે કર્મચારીની પ્રામાણિકતા) ને અવગણે છે, અને ભાવ ફેરફારો (ફુગાવો) ને અવગણે છે."
    },
    {
        "id": "ACC_CH12_06_PRESENTATION",
        "type": "theory",
        "title": "Presentation and Classification of Ratios",
        "title_hi": "अनुपातों की प्रस्तुति और वर्गीकरण",
        "title_gu": "ગુણોત્તરની રજૂઆત અને વર્ગીકરણ",
        "body": "Ratios can be presented in 5 ways: Proportion (e.g., 2:1), Percentage (e.g., 20%), Times (e.g., 3 times), Fraction (e.g., 1/2), and Days/Weeks/Months (e.g., 37 days). Classification is Traditional (Trading A/c, Balance Sheet, Composite) or Functional (Profitability, Liquidity, Solvency, Efficiency).",
        "body_hi": "अनुपातों को 5 तरीकों से प्रस्तुत किया जा सकता है: अनुपात (उदा., 2:1), प्रतिशत (उदा., 20%), गुना (उदा., 3 गुना), भिन्न (उदा., 1/2), और दिन/सप्ताह/महीने (उदा., 37 दिन)। वर्गीकरण पारंपरिक (व्यापार खाता, बैलेंस शीट, मिश्रित) या कार्यात्मक (लाभप्रदता, तरलता, शोधनक्षमता, दक्षता) है।",
        "body_gu": "ગુણોત્તર 5 રીતે રજૂ કરી શકાય છે: પ્રમાણ (દા.ત., 2:1), ટકાવારી (દા.ત., 20%), વખત (દા.ત., 3 વખત), અપૂર્ણાંક (દા.ત., 1/2), અને દિવસો/અઠવાડિયા/મહિના (દા.ત., 37 દિવસ). વર્ગીકરણ પરંપરાગત (ટ્રેડિંગ એકાઉન્ટ, બેલેન્સ શીટ, સંયુક્ત) અથવા કાર્યાત્મક (નફાકારકતા, પ્રવાહિતા, સદ્ધરતા, કાર્યક્ષમતા) છે."
    },
    {
        "id": "ACC_CH12_07_PROFITABILITY",
        "type": "theory",
        "title": "Profitability Ratios",
        "title_hi": "लाभप्रदता अनुपात",
        "title_gu": "નફાકારકતા ગુણોત્તર",
        "body": "Profitability ratios measure the earning capacity of the business. The main ones are: \n1. Gross Profit Ratio = (Gross Profit / Net Sales) × 100\n2. Operating Ratio = (Operating Cost / Net Sales) × 100\n3. Operating Profit Ratio = (Operating Profit / Net Sales) × 100\n4. Net Profit Ratio = (Net Profit After Tax / Net Sales) × 100",
        "body_hi": "लाभप्रदता अनुपात व्यवसाय की कमाई क्षमता को मापते हैं। मुख्य हैं: \n1. सकल लाभ अनुपात = (सकल लाभ / शुद्ध बिक्री) × 100\n2. परिचालन अनुपात = (परिचालन लागत / शुद्ध बिक्री) × 100\n3. परिचालन लाभ अनुपात = (परिचालन लाभ / शुद्ध बिक्री) × 100\n4. शुद्ध लाभ अनुपात = (कर के बाद शुद्ध लाभ / शुद्ध बिक्री) × 100",
        "body_gu": "નફાકારકતા ગુણોત્તર વ્યવસાયની કમાણી કરવાની ક્ષમતાને માપે છે. મુખ્ય આ છે: \n1. કુલ નફાનો ગુણોત્તર = (કુલ નફો / ચોખ્ખું વેચાણ) × 100\n2. ઓપરેટિંગ ગુણોત્તર = (ઓપરેટિંગ ખર્ચ / ચોખ્ખું વેચાણ) × 100\n3. ઓપરેટિંગ નફાનો ગુણોત્તર = (ઓપરેટિંગ નફો / ચોખ્ખું વેચાણ) × 100\n4. ચોખ્ખા નફાનો ગુણોત્તર = (કર પછી ચોખ્ખો નફો / ચોખ્ખું વેચાણ) × 100"
    },
    {
        "id": "ACC_CH12_08_MASTERY",
        "type": "mcq",
        "question": "If Sales = ₹5,00,000 and Gross Profit = ₹1,00,000, what is the Gross Profit Ratio?",
        "question_hi": "यदि बिक्री = ₹5,00,000 और सकल लाभ = ₹1,00,000 है, तो सकल लाभ अनुपात क्या है?",
        "question_gu": "જો વેચાણ = ₹5,00,000 અને કુલ નફો = ₹1,00,000 હોય, તો કુલ નફાનો ગુણોત્તર શું છે?",
        "options": [
            "10%",
            "20%",
            "25%",
            "50%"
        ],
        "options_hi": [
            "10%",
            "20%",
            "25%",
            "50%"
        ],
        "options_gu": [
            "10%",
            "20%",
            "25%",
            "50%"
        ],
        "correct_index": 1,
        "explanation": "Gross Profit Ratio = (1,00,000 / 5,00,000) × 100 = 20%",
        "explanation_hi": "सकल लाभ अनुपात = (1,00,000 / 5,00,000) × 100 = 20%",
        "explanation_gu": "કુલ નફાનો ગુણોત્તર = (1,00,000 / 5,00,000) × 100 = 20%"
    }
]

os.makedirs("/home/ubuntu/Shine_Academy_Naroda/app_core/chapters", exist_ok=True)
with open("/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/tmp_ch12_part1.json", "w", encoding="utf-8") as f:
    json.dump(blocks, f, indent=4, ensure_ascii=False)

print("JSON file generated successfully.")
