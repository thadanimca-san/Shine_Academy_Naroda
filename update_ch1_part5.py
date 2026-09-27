import json

filepath = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch1.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

blocks = data.get('blocks', [])

new_blocks = [
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_EX16",
      "type": "theory",
      "title": "Exercise Q16",
      "title_hi": "अभ्यास प्रश्न 16",
      "title_gu": "સ્વાધ્યાય પ્રશ્ન 16",
      "body": "**Question:** Explain the following in terms of gain or loss of oxygen with two examples each.\n(a) Oxidation\n(b) Reduction\n\n**Answer:**\n(a) **Oxidation:** It is the gain of oxygen in a chemical reaction. \nExamples: \n1. 2Mg + O2 → 2MgO (Magnesium gains oxygen)\n2. C + O2 → CO2 (Carbon gains oxygen)\n\n(b) **Reduction:** It is the loss of oxygen in a chemical reaction. \nExamples:\n1. CuO + H2 → Cu + H2O (Copper oxide loses oxygen)\n2. ZnO + C → Zn + CO (Zinc oxide loses oxygen)",
      "body_hi": "**प्रश्न:** ऑक्सीजन के योग या ह्रास के आधार पर निम्न पदों की व्याख्या कीजिए। प्रत्येक के लिए दो उदाहरण दीजिए।\n(a) उपचयन (Oxidation)\n(b) अपचयन (Reduction)\n\n**उत्तर:**\n(a) **उपचयन:** रासायनिक अभिक्रिया में ऑक्सीजन की वृद्धि को उपचयन कहते हैं।\nउदाहरण:\n1. 2Mg + O2 → 2MgO (मैग्नीशियम में ऑक्सीजन की वृद्धि)\n2. C + O2 → CO2 (कार्बन में ऑक्सीजन की वृद्धि)\n\n(b) **अपचयन:** रासायनिक अभिक्रिया में ऑक्सीजन के ह्रास को अपचयन कहते हैं।\nउदाहरण:\n1. CuO + H2 → Cu + H2O (कॉपर ऑक्साइड से ऑक्सीजन का ह्रास)\n2. ZnO + C → Zn + CO (जिंक ऑक्साइड से ऑक्सीजन का ह्रास)",
      "body_gu": "**પ્રશ્ન:** ઓક્સિજનના ઉમેરાવા અથવા દૂર થવાના આધારે નીચેના પદો સમજાવો. દરેક માટે બે ઉદાહરણ આપો.\n(a) ઓક્સિડેશન\n(b) રિડક્શન\n\n**જવાબ:**\n(a) **ઓક્સિડેશન:** રાસાયણિક પ્રક્રિયામાં ઓક્સિજનના ઉમેરાવાની ક્રિયાને ઓક્સિડેશન કહે છે.\nઉદાહરણો:\n1. 2Mg + O2 → 2MgO (મેગ્નેશિયમમાં ઓક્સિજન ઉમેરાય છે)\n2. C + O2 → CO2 (કાર્બનમાં ઓક્સિજન ઉમેરાય છે)\n\n(b) **રિડક્શન:** રાસાયણિક પ્રક્રિયામાં ઓક્સિજન દૂર થવાની ક્રિયાને રિડક્શન કહે છે.\nઉદાહરણો:\n1. CuO + H2 → Cu + H2O (કોપર ઓક્સાઇડમાંથી ઓક્સિજન દૂર થાય છે)\n2. ZnO + C → Zn + CO (ઝીંક ઓક્સાઇડમાંથી ઓક્સિજન દૂર થાય છે)"
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_EX17",
      "type": "theory",
      "title": "Exercise Q17",
      "title_hi": "अभ्यास प्रश्न 17",
      "title_gu": "સ્વાધ્યાય પ્રશ્ન 17",
      "body": "**Question:** A shiny brown coloured element 'X' on heating in air becomes black in colour. Name the element 'X' and the black coloured compound formed.\n\n**Answer:** \nThe shiny brown element 'X' is Copper (Cu).\nWhen copper is heated in air, it reacts with oxygen to form a black compound called Copper(II) oxide (CuO).\nEquation: 2Cu + O2 → 2CuO",
      "body_hi": "**प्रश्न:** एक भूरे रंग का चमकदार तत्व 'X' वायु की उपस्थिति में गर्म करने पर काले रंग का हो जाता है। तत्व 'X' एवं बनने वाले काले रंग के यौगिक का नाम बताइए।\n\n**उत्तर:**\nभूरे रंग का चमकदार तत्व 'X' कॉपर (Cu) है।\nजब कॉपर को हवा में गर्म किया जाता है, तो यह ऑक्सीजन के साथ अभिक्रिया करके कॉपर(II) ऑक्साइड (CuO) नामक काले रंग का यौगिक बनाता है।\nसमीकरण: 2Cu + O2 → 2CuO",
      "body_gu": "**પ્રશ્ન:** એક ચળકતા બદામી રંગના તત્વ 'X' ને હવામાં ગરમ કરતાં તે કાળા રંગનું બને છે. તત્વ 'X' અને બનતા કાળા રંગના સંયોજનનું નામ આપો.\n\n**જવાબ:**\nચળકતું બદામી તત્વ 'X' કોપર (Cu) છે.\nજ્યારે કોપરને હવામાં ગરમ કરવામાં આવે છે, ત્યારે તે ઓક્સિજન સાથે પ્રક્રિયા કરી કોપર(II) ઓક્સાઇડ (CuO) નામનું કાળું સંયોજન બનાવે છે.\nસમીકરણ: 2Cu + O2 → 2CuO"
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_EX18",
      "type": "theory",
      "title": "Exercise Q18",
      "title_hi": "अभ्यास प्रश्न 18",
      "title_gu": "સ્વાધ્યાય પ્રશ્ન 18",
      "body": "**Question:** Why do we apply paint on iron articles?\n\n**Answer:** We apply paint on iron articles to protect them from rusting. Paint acts as a barrier and prevents the iron surface from coming into contact with moisture and oxygen present in the air, which are necessary for rusting.",
      "body_hi": "**प्रश्न:** लोहे की वस्तुओं को हम पेंट क्यों करते हैं?\n\n**उत्तर:** हम लोहे की वस्तुओं को जंग (rusting) से बचाने के लिए पेंट करते हैं। पेंट एक आवरण का कार्य करता है और लोहे की सतह को हवा में मौजूद नमी और ऑक्सीजन के संपर्क में आने से रोकता है, जो जंग लगने के लिए आवश्यक होते हैं।",
      "body_gu": "**પ્રશ્ન:** લોખંડની વસ્તુઓ પર આપણે રંગ શા માટે લગાવીએ છીએ?\n\n**જવાબ:** લોખંડની વસ્તુઓને કાટ લાગતો અટકાવવા માટે આપણે તેના પર રંગ લગાવીએ છીએ. રંગ એક પડ તરીકે કામ કરે છે અને લોખંડની સપાટીને હવામાં રહેલા ભેજ અને ઓક્સિજનના સંપર્કમાં આવતા અટકાવે છે, જે કાટ લાગવા માટે જરૂરી છે."
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_EX19",
      "type": "theory",
      "title": "Exercise Q19",
      "title_hi": "अभ्यास प्रश्न 19",
      "title_gu": "સ્વાધ્યાય પ્રશ્ન 19",
      "body": "**Question:** Oil and fat containing food items are flushed with nitrogen. Why?\n\n**Answer:** Oil and fat containing food items are flushed with nitrogen gas to prevent them from getting oxidized. Nitrogen is an unreactive gas that displaces oxygen, thus preventing the food from becoming rancid and spoiling its taste and smell.",
      "body_hi": "**प्रश्न:** तेल एवं वसा युक्त खाद्य पदार्थों को नाइट्रोजन से प्रभावित (flush) क्यों किया जाता है?\n\n**उत्तर:** तेल एवं वसा युक्त खाद्य पदार्थों को उपचयित (oxidized) होने से बचाने के लिए नाइट्रोजन गैस से प्रवाहित किया जाता है। नाइट्रोजन एक अक्रिय गैस है जो ऑक्सीजन को विस्थापित कर देती है, जिससे खाद्य पदार्थ विकृतगंधी (rancid) होने से बच जाते हैं और उनका स्वाद व गंध खराब नहीं होता।",
      "body_gu": "**પ્રશ્ન:** તેલ અને ચરબી ધરાવતા ખાદ્ય પદાર્થોને નાઇટ્રોજનથી ફ્લશ શા માટે કરવામાં આવે છે?\n\n**જવાબ:** તેલ અને ચરબી ધરાવતા ખાદ્ય પદાર્થોનું ઓક્સિડેશન થતું અટકાવવા માટે તેમને નાઇટ્રોજન વાયુથી ફ્લશ કરવામાં આવે છે. નાઇટ્રોજન નિષ્ક્રિય વાયુ છે જે ઓક્સિજનને દૂર કરે છે, આમ ખોરાકને ખોરો થતો અટકાવે છે અને તેનો સ્વાદ તથા ગંધ બગડતા બચાવે છે."
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_EX20",
      "type": "theory",
      "title": "Exercise Q20",
      "title_hi": "अभ्यास प्रश्न 20",
      "title_gu": "સ્વાધ્યાય પ્રશ્ન 20",
      "body": "**Question:** Explain the following terms with one example each.\n(a) Corrosion\n(b) Rancidity\n\n**Answer:**\n(a) **Corrosion:** It is the slow process of eating away of metals when exposed to moisture, acids, or air. \nExample: Rusting of iron, tarnishing of silver.\n(b) **Rancidity:** It is the oxidation of fats and oils present in food items, resulting in a bad smell and foul taste.\nExample: Butter kept in the open for a long time smells bad and tastes sour.",
      "body_hi": "**प्रश्न:** निम्न पदों का वर्णन कीजिए तथा प्रत्येक का एक उदाहरण दीजिए।\n(a) संक्षारण (Corrosion)\n(b) विकृतगंधिता (Rancidity)\n\n**उत्तर:**\n(a) **संक्षारण:** नमी, अम्ल या हवा के संपर्क में आने पर धातुओं के धीरे-धीरे नष्ट होने की प्रक्रिया को संक्षारण कहते हैं।\nउदाहरण: लोहे पर जंग लगना, चांदी का काला पड़ना।\n(b) **विकृतगंधिता:** खाद्य पदार्थों में मौजूद वसा और तेल के ऑक्सीकरण की प्रक्रिया को विकृतगंधिता कहते हैं, जिसके परिणामस्वरूप दुर्गंध और खराब स्वाद पैदा होता है।\nउदाहरण: लंबे समय तक खुले में रखा हुआ मक्खन दुर्गंध देता है और उसका स्वाद खट्टा हो जाता है।",
      "body_gu": "**પ્રશ્ન:** નીચેના પદો એક ઉદાહરણ આપીને સમજાવો.\n(a) ક્ષારણ (Corrosion)\n(b) ખોરાપણું (Rancidity)\n\n**જવાબ:**\n(a) **ક્ષારણ:** જ્યારે ધાતુ ભેજ, એસિડ અથવા હવાના સંપર્કમાં આવે છે ત્યારે તેના ધીમે ધીમે ખવાઈ જવાની પ્રક્રિયાને ક્ષારણ કહે છે.\nઉદાહરણ: લોખંડને કાટ લાગવો, ચાંદીનું ઝાંખું પડવું.\n(b) **ખોરાપણું:** ખાદ્ય પદાર્થોમાં રહેલી ચરબી અને તેલના ઓક્સિડેશનની પ્રક્રિયાને ખોરાપણું કહે છે, જેના પરિણામે ખરાબ ગંધ અને સ્વાદ ઉત્પન્ન થાય છે.\nઉદાહરણ: લાંબા સમય સુધી ખુલ્લું રાખેલું માખણ ખરાબ ગંધ મારે છે અને સ્વાદમાં ખાટું થઈ જાય છે."
    }
]

blocks.extend(new_blocks)
data['blocks'] = blocks

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Part 5 (Ex 16-20) updated!")
