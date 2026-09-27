import json

filepath = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch1.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

blocks = data.get('blocks', [])

new_blocks = [
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_EX01",
      "type": "mcq",
      "title": "Exercise Q1",
      "title_hi": "अभ्यास प्रश्न 1",
      "title_gu": "સ્વાધ્યાય પ્રશ્ન 1",
      "question": "Which of the statements about the reaction below are incorrect?\n2PbO(s) + C(s) → 2Pb(s) + CO2(g)\n(a) Lead is getting reduced.\n(b) Carbon dioxide is getting oxidised.\n(c) Carbon is getting oxidised.\n(d) Lead oxide is getting reduced.",
      "question_hi": "नीचे दी गई अभिक्रिया के संबंध में कौन सा कथन असत्य है?\n2PbO(s) + C(s) → 2Pb(s) + CO2(g)\n(a) सीसा अपचयित हो रहा है।\n(b) कार्बन डाइऑक्साइड उपचयित हो रहा है।\n(c) कार्बन उपचयित हो रहा है।\n(d) लेड ऑक्साइड अपचयित हो रहा है।",
      "question_gu": "નીચે આપેલ પ્રક્રિયા માટે કયા વિધાનો ખોટા છે?\n2PbO(s) + C(s) → 2Pb(s) + CO2(g)\n(a) સીસું રિડક્શન પામે છે.\n(b) કાર્બન ડાયોક્સાઇડ ઓક્સિડેશન પામે છે.\n(c) કાર્બન ઓક્સિડેશન પામે છે.\n(d) લેડ ઓક્સાઇડ રિડક્શન પામે છે.",
      "options": [
        "(a) and (b)",
        "(a) and (c)",
        "(a), (b) and (c)",
        "All"
      ],
      "options_hi": [
        "(a) और (b)",
        "(a) और (c)",
        "(a), (b) और (c)",
        "सभी"
      ],
      "options_gu": [
        "(a) અને (b)",
        "(a) અને (c)",
        "(a), (b) અને (c)",
        "બધા"
      ],
      "correct_index": 0,
      "explanation": "Statements (a) and (b) are incorrect. Lead oxide (PbO) is getting reduced to Lead (Pb), not Lead. Carbon (C) is getting oxidized to Carbon dioxide (CO2), not CO2.",
      "explanation_hi": "कथन (a) और (b) असत्य हैं। लेड ऑक्साइड (PbO) लेड (Pb) में अपचयित हो रहा है, न कि सीसा। कार्बन (C) कार्बन डाइऑक्साइड (CO2) में उपचयित हो रहा है, न कि CO2।",
      "explanation_gu": "વિધાન (a) અને (b) ખોટા છે. લેડ ઓક્સાઇડ (PbO) નું લેડ (Pb) માં રિડક્શન થાય છે, સીસાનું નહીં. કાર્બન (C) નું કાર્બન ડાયોક્સાઇડ (CO2) માં ઓક્સિડેશન થાય છે, CO2 નું નહીં."
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_EX02",
      "type": "mcq",
      "title": "Exercise Q2",
      "title_hi": "अभ्यास प्रश्न 2",
      "title_gu": "સ્વાધ્યાય પ્રશ્ન 2",
      "question": "Fe2O3 + 2Al → Al2O3 + 2Fe\nThe above reaction is an example of a:",
      "question_hi": "Fe2O3 + 2Al → Al2O3 + 2Fe\nऊपर दी गई अभिक्रिया किस प्रकार की है?",
      "question_gu": "Fe2O3 + 2Al → Al2O3 + 2Fe\nઉપર આપેલી પ્રક્રિયા શેનું ઉદાહરણ છે?",
      "options": [
        "combination reaction",
        "double displacement reaction",
        "decomposition reaction",
        "displacement reaction"
      ],
      "options_hi": [
        "संयोजन अभिक्रिया",
        "द्विविस्थापन अभिक्रिया",
        "वियोजन अभिक्रिया",
        "विस्थापन अभिक्रिया"
      ],
      "options_gu": [
        "સંયોગીકરણ પ્રક્રિયા",
        "દ્વિવિસ્થાપન પ્રક્રિયા",
        "વિઘટન પ્રક્રિયા",
        "વિસ્થાપન પ્રક્રિયા"
      ],
      "correct_index": 3,
      "explanation": "It is a displacement reaction because Aluminium (Al), being more reactive, displaces Iron (Fe) from Iron oxide (Fe2O3).",
      "explanation_hi": "यह एक विस्थापन अभिक्रिया है क्योंकि एल्युमीनियम (Al) अधिक अभिक्रियाशील होने के कारण लोहे (Fe) को आयरन ऑक्साइड (Fe2O3) से विस्थापित कर देता है।",
      "explanation_gu": "આ એક વિસ્થાપન પ્રક્રિયા છે કારણ કે એલ્યુમિનિયમ (Al) વધુ સક્રિય હોવાથી તે લોખંડ (Fe) ને આયર્ન ઓક્સાઇડ (Fe2O3) માંથી વિસ્થાપિત કરે છે."
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_EX03",
      "type": "mcq",
      "title": "Exercise Q3",
      "title_hi": "अभ्यास प्रश्न 3",
      "title_gu": "સ્વાધ્યાય પ્રશ્ન 3",
      "question": "What happens when dilute hydrochloric acid is added to iron fillings? Tick the correct answer.",
      "question_hi": "लौह चूर्ण पर तनु हाइड्रोक्लोरिक अम्ल डालने से क्या होता है? सही उत्तर पर निशान लगाएँ।",
      "question_gu": "જ્યારે લોખંડના ભૂકા પર મંદ હાઇડ્રોક્લોરિક એસિડ ઉમેરવામાં આવે છે ત્યારે શું થાય છે? સાચા જવાબ પર નિશાની કરો.",
      "options": [
        "Hydrogen gas and iron chloride are produced.",
        "Chlorine gas and iron hydroxide are produced.",
        "No reaction takes place.",
        "Iron salt and water are produced."
      ],
      "options_hi": [
        "हाइड्रोजन गैस और आयरन क्लोराइड बनते हैं।",
        "क्लोरीन गैस और आयरन हाइड्रॉक्साइड बनते हैं।",
        "कोई अभिक्रिया नहीं होती है।",
        "आयरन लवण और जल बनते हैं।"
      ],
      "options_gu": [
        "હાઇડ્રોજન વાયુ અને આયર્ન ક્લોરાઇડ ઉત્પન્ન થાય છે.",
        "ક્લોરિન વાયુ અને આયર્ન હાઇડ્રોક્સાઇડ ઉત્પન્ન થાય છે.",
        "કોઈ પ્રક્રિયા થતી નથી.",
        "આયર્ન ક્ષાર અને પાણી ઉત્પન્ન થાય છે."
      ],
      "correct_index": 0,
      "explanation": "Iron reacts with dilute hydrochloric acid to produce iron(II) chloride and hydrogen gas: Fe + 2HCl → FeCl2 + H2.",
      "explanation_hi": "लोहा तनु हाइड्रोक्लोरिक अम्ल के साथ अभिक्रिया करके आयरन(II) क्लोराइड और हाइड्रोजन गैस बनाता है: Fe + 2HCl → FeCl2 + H2।",
      "explanation_gu": "લોખંડ મંદ હાઇડ્રોક્લોરિક એસિડ સાથે પ્રક્રિયા કરી આયર્ન(II) ક્લોરાઇડ અને હાઇડ્રોજન વાયુ ઉત્પન્ન કરે છે: Fe + 2HCl → FeCl2 + H2."
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_EX04",
      "type": "theory",
      "title": "Exercise Q4",
      "title_hi": "अभ्यास प्रश्न 4",
      "title_gu": "સ્વાધ્યાય પ્રશ્ન 4",
      "body": "**Question:** What is a balanced chemical equation? Why should chemical equations be balanced?\n\n**Answer:** A balanced chemical equation has an equal number of atoms of each element on both the reactant and product sides. Chemical equations must be balanced to satisfy the Law of Conservation of Mass, which states that mass can neither be created nor destroyed in a chemical reaction.",
      "body_hi": "**प्रश्न:** संतुलित रासायनिक समीकरण क्या है? रासायनिक समीकरण को संतुलित करना क्यों आवश्यक है?\n\n**उत्तर:** संतुलित रासायनिक समीकरण वह है जिसमें अभिकारक और उत्पाद दोनों तरफ प्रत्येक तत्व के परमाणुओं की संख्या समान होती है। रासायनिक समीकरण को संतुलित करना इसलिए आवश्यक है ताकि द्रव्यमान संरक्षण के नियम का पालन हो सके, जिसके अनुसार किसी रासायनिक अभिक्रिया में द्रव्यमान का न तो निर्माण होता है और न ही विनाश।",
      "body_gu": "**પ્રશ્ન:** સંતુલિત રાસાયણિક સમીકરણ એટલે શું? રાસાયણિક સમીકરણ શા માટે સંતુલિત હોવું જોઈએ?\n\n**જવાબ:** સંતુલિત રાસાયણિક સમીકરણ એ છે જેમાં પ્રક્રિયકો અને નીપજો બંને તરફ દરેક તત્વના અણુઓની સંખ્યા સમાન હોય છે. રાસાયણિક સમીકરણ દળ સંરક્ષણના નિયમને અનુસરવા માટે સંતુલિત હોવું જોઈએ, જે મુજબ રાસાયણિક પ્રક્રિયામાં દળનું નિર્માણ કે વિનાશ થઈ શકતો નથી."
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_EX05",
      "type": "theory",
      "title": "Exercise Q5",
      "title_hi": "अभ्यास प्रश्न 5",
      "title_gu": "સ્વાધ્યાય પ્રશ્ન 5",
      "body": "**Question:** Translate the following statements into chemical equations and then balance them.\n(a) Hydrogen gas combines with nitrogen to form ammonia.\n(b) Hydrogen sulphide gas burns in air to give water and sulphur dioxide.\n(c) Barium chloride reacts with aluminium sulphate to give aluminium chloride and a precipitate of barium sulphate.\n(d) Potassium metal reacts with water to give potassium hydroxide and hydrogen gas.\n\n**Answer:**\n(a) 3H2(g) + N2(g) → 2NH3(g)\n(b) 2H2S(g) + 3O2(g) → 2H2O(l) + 2SO2(g)\n(c) 3BaCl2(aq) + Al2(SO4)3(aq) → 2AlCl3(aq) + 3BaSO4(s)\n(d) 2K(s) + 2H2O(l) → 2KOH(aq) + H2(g)",
      "body_hi": "**प्रश्न:** निम्न कथनों को रासायनिक समीकरण के रूप में परिवर्तित कर उन्हें संतुलित कीजिए।\n(a) नाइट्रोजन हाइड्रोजन गैस से संयोग करके अमोनिया बनाता है।\n(b) हाइड्रोजन सल्फाइड गैस का वायु में दहन होने पर जल एवं सल्फर डाइऑक्साइड बनता है।\n(c) एल्युमिनियम सल्फेट के साथ अभिक्रिया कर बेरियम क्लोराइड, एल्युमिनियम क्लोराइड एवं बेरियम सल्फेट का अवक्षेप देता है।\n(d) पोटैशियम धातु जल के साथ अभिक्रिया करके पोटैशियम हाइड्रॉक्साइड एवं हाइड्रोजन गैस देती है।\n\n**उत्तर:**\n(a) 3H2(g) + N2(g) → 2NH3(g)\n(b) 2H2S(g) + 3O2(g) → 2H2O(l) + 2SO2(g)\n(c) 3BaCl2(aq) + Al2(SO4)3(aq) → 2AlCl3(aq) + 3BaSO4(s)\n(d) 2K(s) + 2H2O(l) → 2KOH(aq) + H2(g)",
      "body_gu": "**પ્રશ્ન:** નીચેના વિધાનોને રાસાયણિક સમીકરણમાં ફેરવી તેમને સંતુલિત કરો.\n(a) હાઇડ્રોજન વાયુ નાઇટ્રોજન સાથે જોડાઈને એમોનિયા બનાવે છે.\n(b) હાઇડ્રોજન સલ્ફાઇડ વાયુ હવામાં સળગીને પાણી અને સલ્ફર ડાયોક્સાઇડ આપે છે.\n(c) બેરિયમ ક્લોરાઇડ એલ્યુમિનિયમ સલ્ફેટ સાથે પ્રક્રિયા કરી એલ્યુમિનિયમ ક્લોરાઇડ અને બેરિયમ સલ્ફેટના અવક્ષેપ આપે છે.\n(d) પોટેશિયમ ધાતુ પાણી સાથે પ્રક્રિયા કરી પોટેશિયમ હાઇડ્રોક્સાઇડ અને હાઇડ્રોજન વાયુ આપે છે.\n\n**જવાબ:**\n(a) 3H2(g) + N2(g) → 2NH3(g)\n(b) 2H2S(g) + 3O2(g) → 2H2O(l) + 2SO2(g)\n(c) 3BaCl2(aq) + Al2(SO4)3(aq) → 2AlCl3(aq) + 3BaSO4(s)\n(d) 2K(s) + 2H2O(l) → 2KOH(aq) + H2(g)"
    }
]

blocks.extend(new_blocks)
data['blocks'] = blocks

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Part 2 (Ex 1-5) updated!")
