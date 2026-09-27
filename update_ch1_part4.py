import json

filepath = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch1.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

blocks = data.get('blocks', [])

new_blocks = [
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_EX11",
      "type": "theory",
      "title": "Exercise Q11",
      "title_hi": "अभ्यास प्रश्न 11",
      "title_gu": "સ્વાધ્યાય પ્રશ્ન 11",
      "body": "**Question:** Why are decomposition reactions called the opposite of combination reactions? Write equations for these reactions.\n\n**Answer:** In a combination reaction, two or more substances combine to form a single product. In a decomposition reaction, a single reactant breaks down into two or more simpler products. Hence, they are opposite to each other.\nCombination: C + O2 → CO2\nDecomposition: CaCO3 → CaO + CO2",
      "body_hi": "**प्रश्न:** वियोजन अभिक्रिया को संयोजन अभिक्रिया के विपरीत क्यों कहा जाता है? इन अभिक्रियाओं के लिए समीकरण लिखिए।\n\n**उत्तर:** संयोजन अभिक्रिया में, दो या दो से अधिक पदार्थ मिलकर एक एकल उत्पाद बनाते हैं। जबकि वियोजन अभिक्रिया में, एक एकल अभिकारक टूटकर दो या दो से अधिक सरल उत्पाद बनाता है। इसलिए, ये एक दूसरे के विपरीत हैं।\nसंयोजन: C + O2 → CO2\nवियोजन: CaCO3 → CaO + CO2",
      "body_gu": "**પ્રશ્ન:** વિઘટન પ્રક્રિયાઓને સંયોગીકરણ પ્રક્રિયાઓની વિરુદ્ધ શા માટે કહેવામાં આવે છે? આ પ્રક્રિયાઓ માટે સમીકરણો લખો.\n\n**જવાબ:** સંયોગીકરણ પ્રક્રિયામાં, બે કે તેથી વધુ પદાર્થો જોડાઈને એક જ નીપજ બનાવે છે. જ્યારે વિઘટન પ્રક્રિયામાં, એક જ પ્રક્રિયક તૂટીને બે કે તેથી વધુ સરળ નીપજો બનાવે છે. તેથી, તેઓ એકબીજાથી વિરુદ્ધ છે.\nસંયોગીકરણ: C + O2 → CO2\nવિઘટન: CaCO3 → CaO + CO2"
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_EX12",
      "type": "theory",
      "title": "Exercise Q12",
      "title_hi": "अभ्यास प्रश्न 12",
      "title_gu": "સ્વાધ્યાય પ્રશ્ન 12",
      "body": "**Question:** Write one equation each for decomposition reactions where energy is supplied in the form of heat, light or electricity.\n\n**Answer:**\n(a) Heat (Thermal decomposition): CaCO3(s) + Heat → CaO(s) + CO2(g)\n(b) Light (Photochemical decomposition): 2AgCl(s) + Light → 2Ag(s) + Cl2(g)\n(c) Electricity (Electrolytic decomposition): 2H2O(l) + Electricity → 2H2(g) + O2(g)",
      "body_hi": "**प्रश्न:** उन वियोजन अभिक्रियाओं के एक-एक समीकरण लिखिए जिनमें ऊष्मा, प्रकाश एवं विद्युत के रूप में ऊर्जा प्रदान की जाती है।\n\n**उत्तर:**\n(a) ऊष्मा (ऊष्मीय वियोजन): CaCO3(s) + ऊष्मा → CaO(s) + CO2(g)\n(b) प्रकाश (प्रकाशीय वियोजन): 2AgCl(s) + प्रकाश → 2Ag(s) + Cl2(g)\n(c) विद्युत (विद्युत अपघटन): 2H2O(l) + विद्युत → 2H2(g) + O2(g)",
      "body_gu": "**પ્રશ્ન:** એવી વિઘટન પ્રક્રિયાઓનું એક-એક સમીકરણ લખો જેમાં ઉષ્મા, પ્રકાશ અને વિદ્યુત સ્વરૂપે ઉર્જા પૂરી પાડવામાં આવે છે.\n\n**જવાબ:**\n(a) ઉષ્મા (ઉષ્મીય વિઘટન): CaCO3(s) + ઉષ્મા → CaO(s) + CO2(g)\n(b) પ્રકાશ (પ્રકાશ રાસાયણિક વિઘટન): 2AgCl(s) + પ્રકાશ → 2Ag(s) + Cl2(g)\n(c) વિદ્યુત (વિદ્યુત વિભાજન): 2H2O(l) + વિદ્યુત → 2H2(g) + O2(g)"
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_EX13",
      "type": "theory",
      "title": "Exercise Q13",
      "title_hi": "अभ्यास प्रश्न 13",
      "title_gu": "સ્વાધ્યાય પ્રશ્ન 13",
      "body": "**Question:** What is the difference between displacement and double displacement reactions? Write equations for these reactions.\n\n**Answer:** In a displacement reaction, a more reactive element replaces a less reactive element from its compound (e.g., Fe + CuSO4 → FeSO4 + Cu). In a double displacement reaction, two compounds react by an exchange of ions to form two new compounds (e.g., Na2SO4 + BaCl2 → BaSO4 + 2NaCl).",
      "body_hi": "**प्रश्न:** विस्थापन एवं द्विविस्थापन अभिक्रियाओं में क्या अंतर है? इन अभिक्रियाओं के समीकरण लिखिए।\n\n**उत्तर:** विस्थापन अभिक्रिया में, एक अधिक अभिक्रियाशील तत्व किसी कम अभिक्रियाशील तत्व को उसके यौगिक से विस्थापित कर देता है (उदाहरण: Fe + CuSO4 → FeSO4 + Cu)। द्विविस्थापन अभिक्रिया में, दो यौगिक आयनों के आदान-प्रदान द्वारा अभिक्रिया करके दो नए यौगिक बनाते हैं (उदाहरण: Na2SO4 + BaCl2 → BaSO4 + 2NaCl)।",
      "body_gu": "**પ્રશ્ન:** વિસ્થાપન અને દ્વિવિસ્થાપન પ્રક્રિયાઓ વચ્ચે શું તફાવત છે? આ પ્રક્રિયાઓ માટે સમીકરણો લખો.\n\n**જવાબ:** વિસ્થાપન પ્રક્રિયામાં, વધુ સક્રિય તત્વ ઓછા સક્રિય તત્વને તેના સંયોજનમાંથી વિસ્થાપિત કરે છે (દા.ત., Fe + CuSO4 → FeSO4 + Cu). દ્વિવિસ્થાપન પ્રક્રિયામાં, બે સંયોજનો આયનોની આપ-લે દ્વારા પ્રક્રિયા કરી બે નવા સંયોજનો બનાવે છે (દા.ત., Na2SO4 + BaCl2 → BaSO4 + 2NaCl)."
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_EX14",
      "type": "theory",
      "title": "Exercise Q14",
      "title_hi": "अभ्यास प्रश्न 14",
      "title_gu": "સ્વાધ્યાય પ્રશ્ન 14",
      "body": "**Question:** In the refining of silver, the recovery of silver from silver nitrate solution involved displacement by copper metal. Write down the reaction involved.\n\n**Answer:** When copper metal is added to silver nitrate solution, copper (being more reactive) displaces silver from silver nitrate. The equation is:\nCu(s) + 2AgNO3(aq) → Cu(NO3)2(aq) + 2Ag(s)",
      "body_hi": "**प्रश्न:** सिल्वर के शोधन में, सिल्वर नाइट्रेट के विलयन से सिल्वर प्राप्त करने के लिए कॉपर धातु द्वारा विस्थापन किया जाता है। इस प्रक्रिया के लिए अभिक्रिया लिखिए।\n\n**उत्तर:** जब सिल्वर नाइट्रेट विलयन में कॉपर धातु मिलाई जाती है, तो कॉपर (अधिक अभिक्रियाशील होने के कारण) सिल्वर नाइट्रेट से सिल्वर को विस्थापित कर देता है। समीकरण है:\nCu(s) + 2AgNO3(aq) → Cu(NO3)2(aq) + 2Ag(s)",
      "body_gu": "**પ્રશ્ન:** સિલ્વરના શુદ્ધિકરણમાં, સિલ્વર નાઇટ્રેટના દ્રાવણમાંથી સિલ્વર મેળવવા માટે કોપર ધાતુ દ્વારા વિસ્થાપન કરવામાં આવે છે. આ પ્રક્રિયા માટે સમીકરણ લખો.\n\n**જવાબ:** જ્યારે સિલ્વર નાઇટ્રેટના દ્રાવણમાં કોપર ધાતુ ઉમેરવામાં આવે છે, ત્યારે કોપર (વધુ સક્રિય હોવાથી) સિલ્વર નાઇટ્રેટમાંથી સિલ્વરને વિસ્થાપિત કરે છે. સમીકરણ છે:\nCu(s) + 2AgNO3(aq) → Cu(NO3)2(aq) + 2Ag(s)"
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_EX15",
      "type": "theory",
      "title": "Exercise Q15",
      "title_hi": "अभ्यास प्रश्न 15",
      "title_gu": "સ્વાધ્યાય પ્રશ્ન 15",
      "body": "**Question:** What do you mean by a precipitation reaction? Explain by giving examples.\n\n**Answer:** A reaction that produces an insoluble solid (precipitate) in an aqueous solution is called a precipitation reaction. When two solutions containing soluble salts are mixed, an insoluble salt is formed which settles down. \nExample: AgNO3(aq) + NaCl(aq) → AgCl(s) (white precipitate) + NaNO3(aq).",
      "body_hi": "**प्रश्न:** अवक्षेपण अभिक्रिया से आप क्या समझते हैं? उदाहरण देकर समझाइए।\n\n**उत्तर:** ऐसी अभिक्रिया जिसमें जलीय विलयन में एक अघुलनशील ठोस (अवक्षेप) बनता है, अवक्षेपण अभिक्रिया कहलाती है। जब घुलनशील लवण वाले दो विलयनों को मिलाया जाता है, तो एक अघुलनशील लवण बनता है जो नीचे बैठ जाता है।\nउदाहरण: AgNO3(aq) + NaCl(aq) → AgCl(s) (सफेद अवक्षेप) + NaNO3(aq)।",
      "body_gu": "**પ્રશ્ન:** અવક્ષેપન પ્રક્રિયા એટલે શું? ઉદાહરણ આપીને સમજાવો.\n\n**જવાબ:** એવી પ્રક્રિયા જેમાં જલીય દ્રાવણમાં અદ્રાવ્ય ઘન (અવક્ષેપ) ઉત્પન્ન થાય છે તેને અવક્ષેપન પ્રક્રિયા કહેવાય છે. જ્યારે દ્રાવ્ય ક્ષાર ધરાવતા બે દ્રાવણોને મિશ્ર કરવામાં આવે છે, ત્યારે એક અદ્રાવ્ય ક્ષાર બને છે જે નીચે બેસી જાય છે.\nઉદાહરણ: AgNO3(aq) + NaCl(aq) → AgCl(s) (સફેદ અવક્ષેપ) + NaNO3(aq)."
    }
]

blocks.extend(new_blocks)
data['blocks'] = blocks

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Part 4 (Ex 11-15) updated!")
