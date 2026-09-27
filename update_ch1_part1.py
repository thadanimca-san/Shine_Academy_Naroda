import json

filepath = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch1.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

blocks = data.get('blocks', [])

new_blocks = [
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_021",
      "type": "theory",
      "title": "Types of Chemical Reactions",
      "title_hi": "रासायनिक अभिक्रियाओं के प्रकार",
      "title_gu": "રાસાયણિક પ્રક્રિયાઓના પ્રકાર",
      "body": "Chemical reactions involve the breaking and making of bonds between atoms to produce new substances. There are several types of chemical reactions, such as Combination, Decomposition, Displacement, Double Displacement, and Oxidation-Reduction reactions.",
      "body_hi": "रासायनिक अभिक्रियाओं में नए पदार्थ बनाने के लिए परमाणुओं के बीच बंधों का टूटना और बनना शामिल होता है। रासायनिक अभिक्रियाओं के कई प्रकार होते हैं, जैसे संयोजन, वियोजन, विस्थापन, द्विविस्थापन, और उपचयन-अपचयन अभिक्रियाएं।",
      "body_gu": "રાસાયણિક પ્રક્રિયાઓમાં નવા પદાર્થો ઉત્પન્ન કરવા માટે અણુઓ વચ્ચેના બંધ તોડવા અને બનાવવાનો સમાવેશ થાય છે. રાસાયણિક પ્રક્રિયાઓના ઘણા પ્રકારો છે, જેમ કે સંયોગીકરણ, વિઘટન, વિસ્થાપન, દ્વિવિસ્થાપન અને ઓક્સિડેશન-રિડક્શન પ્રક્રિયાઓ."
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_022",
      "type": "theory",
      "title": "1. Combination Reaction",
      "title_hi": "1. संयोजन अभिक्रिया",
      "title_gu": "1. સંયોગીકરણ પ્રક્રિયા",
      "body": "A reaction in which a single product is formed from two or more reactants is known as a combination reaction. \nFor example: CaO(s) + H2O(l) → Ca(OH)2(aq) (Slaked lime) + Heat.\nAnother example is burning of coal: C(s) + O2(g) → CO2(g).",
      "body_hi": "ऐसी अभिक्रिया जिसमें दो या दो से अधिक अभिकारकों से एकल उत्पाद का निर्माण होता है, उसे संयोजन अभिक्रिया कहते हैं।\nउदाहरण के लिए: CaO(s) + H2O(l) → Ca(OH)2(aq) (बुझा हुआ चूना) + ऊष्मा।\nएक अन्य उदाहरण कोयले का जलना है: C(s) + O2(g) → CO2(g)।",
      "body_gu": "જે પ્રક્રિયામાં બે કે તેથી વધુ પ્રક્રિયકોમાંથી એક જ નીપજ બને છે તેને સંયોગીકરણ પ્રક્રિયા કહેવાય છે.\nઉદાહરણ તરીકે: CaO(s) + H2O(l) → Ca(OH)2(aq) (ફોડેલો ચૂનો) + ઉષ્મા.\nબીજું ઉદાહરણ કોલસાનું સળગવું છે: C(s) + O2(g) → CO2(g)."
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_023",
      "type": "mcq",
      "title": "Combination Reaction Test",
      "title_hi": "संयोजन अभिक्रिया परीक्षण",
      "title_gu": "સંયોગીકરણ પ્રક્રિયા કસોટી",
      "question": "Which of the following is a combination reaction?",
      "question_hi": "निम्नलिखित में से कौन सी एक संयोजन अभिक्रिया है?",
      "question_gu": "નીચેનામાંથી કઈ સંયોગીકરણ પ્રક્રિયા છે?",
      "options": [
        "CaCO3 → CaO + CO2",
        "2H2 + O2 → 2H2O",
        "Zn + CuSO4 → ZnSO4 + Cu",
        "NaOH + HCl → NaCl + H2O"
      ],
      "options_hi": [
        "CaCO3 → CaO + CO2",
        "2H2 + O2 → 2H2O",
        "Zn + CuSO4 → ZnSO4 + Cu",
        "NaOH + HCl → NaCl + H2O"
      ],
      "options_gu": [
        "CaCO3 → CaO + CO2",
        "2H2 + O2 → 2H2O",
        "Zn + CuSO4 → ZnSO4 + Cu",
        "NaOH + HCl → NaCl + H2O"
      ],
      "correct_index": 1,
      "explanation": "In 2H2 + O2 → 2H2O, two reactants combine to form a single product. Hence, it is a combination reaction.",
      "explanation_hi": "2H2 + O2 → 2H2O में, दो अभिकारक मिलकर एक एकल उत्पाद बनाते हैं। इसलिए, यह एक संयोजन अभिक्रिया है।",
      "explanation_gu": "2H2 + O2 → 2H2O માં, બે પ્રક્રિયકો જોડાઈને એક જ નીપજ બનાવે છે. તેથી, તે સંયોગીકરણ પ્રક્રિયા છે."
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_024",
      "type": "theory",
      "title": "2. Decomposition Reaction",
      "title_hi": "2. वियोजन (अपघटन) अभिक्रिया",
      "title_gu": "2. વિઘટન પ્રક્રિયા",
      "body": "A reaction in which a single reactant breaks down to give simpler products is called a decomposition reaction. Decomposition reactions require energy either in the form of heat, light or electricity.\nExample: 2FeSO4(s) + Heat → Fe2O3(s) + SO2(g) + SO3(g).",
      "body_hi": "ऐसी अभिक्रिया जिसमें एकल अभिकारक टूटकर छोटे-छोटे उत्पाद प्रदान करता है, वियोजन अभिक्रिया कहलाती है। वियोजन अभिक्रियाओं में ऊर्जा की आवश्यकता होती है, जो ऊष्मा, प्रकाश या विद्युत के रूप में हो सकती है।\nउदाहरण: 2FeSO4(s) + ऊष्मा → Fe2O3(s) + SO2(g) + SO3(g)।",
      "body_gu": "એવી પ્રક્રિયા કે જેમાં એક જ પ્રક્રિયક તૂટીને સરળ નીપજો આપે છે તેને વિઘટન પ્રક્રિયા કહેવાય છે. વિઘટન પ્રક્રિયાઓમાં ઉષ્મા, પ્રકાશ અથવા વિદ્યુત સ્વરૂપે ઉર્જાની જરૂર પડે છે.\nઉદાહરણ: 2FeSO4(s) + ઉષ્મા → Fe2O3(s) + SO2(g) + SO3(g)."
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_025",
      "type": "theory",
      "title": "3. Displacement Reaction",
      "title_hi": "3. विस्थापन अभिक्रिया",
      "title_gu": "3. વિસ્થાપન પ્રક્રિયા",
      "body": "A reaction in which a more reactive element displaces a less reactive element from its compound is called a displacement reaction.\nExample: Fe(s) + CuSO4(aq) → FeSO4(aq) + Cu(s). Here, Iron displaces Copper from copper sulphate.",
      "body_hi": "ऐसी अभिक्रिया जिसमें अधिक अभिक्रियाशील तत्व कम अभिक्रियाशील तत्व को उसके यौगिक से विस्थापित कर देता है, विस्थापन अभिक्रिया कहलाती है।\nउदाहरण: Fe(s) + CuSO4(aq) → FeSO4(aq) + Cu(s)। यहाँ, लोहा तांबे को कॉपर सल्फेट से विस्थापित करता है।",
      "body_gu": "એવી પ્રક્રિયા જેમાં વધુ સક્રિય તત્વ ઓછા સક્રિય તત્વને તેના સંયોજનમાંથી વિસ્થાપિત કરે છે તેને વિસ્થાપન પ્રક્રિયા કહેવાય છે.\nઉદાહરણ: Fe(s) + CuSO4(aq) → FeSO4(aq) + Cu(s). અહીં, લોખંડ કોપર સલ્ફેટમાંથી તાંબાને વિસ્થાપિત કરે છે."
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_026",
      "type": "theory",
      "title": "4. Double Displacement Reaction",
      "title_hi": "4. द्विविस्थापन अभिक्रिया",
      "title_gu": "4. દ્વિવિસ્થાપન પ્રક્રિયા",
      "body": "Reactions in which there is an exchange of ions between the reactants are called double displacement reactions. Often, these result in the formation of a precipitate.\nExample: Na2SO4(aq) + BaCl2(aq) → BaSO4(s) + 2NaCl(aq).",
      "body_hi": "वे अभिक्रियाएँ जिनमें अभिकारकों के बीच आयनों का आदान-प्रदान होता है, द्विविस्थापन अभिक्रियाएँ कहलाती हैं। अक्सर, इसके परिणामस्वरूप एक अवक्षेप (precipitate) बनता है।\nउदाहरण: Na2SO4(aq) + BaCl2(aq) → BaSO4(s) + 2NaCl(aq)।",
      "body_gu": "જે પ્રક્રિયાઓમાં પ્રક્રિયકો વચ્ચે આયનોની આપ-લે થાય છે તેને દ્વિવિસ્થાપન પ્રક્રિયાઓ કહેવામાં આવે છે. ઘણીવાર, આના પરિણામે અવક્ષેપ (precipitate) બને છે.\nઉદાહરણ: Na2SO4(aq) + BaCl2(aq) → BaSO4(s) + 2NaCl(aq)."
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_027",
      "type": "theory",
      "title": "5. Oxidation and Reduction",
      "title_hi": "5. उपचयन एवं अपचयन",
      "title_gu": "5. ઓક્સિડેશન અને રિડક્શન",
      "body": "Oxidation is the gain of oxygen or loss of hydrogen. Reduction is the loss of oxygen or gain of hydrogen. If one reactant gets oxidized while the other gets reduced, such reactions are called oxidation-reduction reactions or redox reactions.\nExample: CuO + H2 → Cu + H2O (CuO is reduced to Cu, H2 is oxidized to H2O).",
      "body_hi": "ऑक्सीजन की वृद्धि या हाइड्रोजन का ह्रास उपचयन (ऑक्सीकरण) कहलाता है। ऑक्सीजन का ह्रास या हाइड्रोजन की वृद्धि अपचयन कहलाता है। यदि एक अभिकारक उपचयित होता है और दूसरा अपचयित, तो ऐसी अभिक्रियाओं को उपचयन-अपचयन या रेडॉक्स अभिक्रियाएँ कहते हैं।\nउदाहरण: CuO + H2 → Cu + H2O (CuO अपचयित होकर Cu बनता है, H2 उपचयित होकर H2O बनता है)।",
      "body_gu": "ઓક્સિજનનો ઉમેરો અથવા હાઇડ્રોજન દૂર થવાની ક્રિયાને ઓક્સિડેશન કહે છે. ઓક્સિજન દૂર થવાની અથવા હાઇડ્રોજન ઉમેરાવાની ક્રિયાને રિડક્શન કહે છે. જો એક પ્રક્રિયકનું ઓક્સિડેશન થાય અને બીજાનું રિડક્શન થાય, તો આવી પ્રક્રિયાઓને રેડોક્ષ પ્રક્રિયાઓ કહેવાય છે.\nઉદાહરણ: CuO + H2 → Cu + H2O (CuO નું રિડક્શન થઈ Cu બને છે, H2 નું ઓક્સિડેશન થઈ H2O બને છે)."
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_028",
      "type": "theory",
      "title": "Effects of Oxidation in Everyday Life",
      "title_hi": "दैनिक जीवन में उपचयन के प्रभाव",
      "title_gu": "રોજિંદા જીવનમાં ઓક્સિડેશનની અસરો",
      "body": "Corrosion: When a metal is attacked by substances around it such as moisture, acids, etc., it is said to corrode. Example: Rusting of iron.\nRancidity: When fats and oils are oxidized, they become rancid and their smell and taste change. Antioxidants are usually added to foods to prevent oxidation.",
      "body_hi": "संक्षारण (Corrosion): जब कोई धातु अपने आस-पास के पदार्थों जैसे नमी, अम्ल आदि के संपर्क में आती है, तो वह संक्षारित होने लगती है। उदाहरण: लोहे पर जंग लगना।\nविकृतगंधिता (Rancidity): जब वसा और तेल उपचयित होते हैं, तो वे विकृतगंधी हो जाते हैं और उनकी गंध व स्वाद बदल जाते हैं। ऑक्सीकरण को रोकने के लिए आमतौर पर खाद्य पदार्थों में एंटीऑक्सीडेंट मिलाए जाते हैं।",
      "body_gu": "ક્ષારણ (Corrosion): જ્યારે કોઈ ધાતુ તેની આસપાસના પદાર્થો જેવા કે ભેજ, એસિડ વગેરેના સંપર્કમાં આવે છે, ત્યારે તેનું ક્ષારણ થાય છે. ઉદાહરણ: લોખંડને કાટ લાગવો.\nખોરાપણું (Rancidity): જ્યારે ચરબી અને તેલનું ઓક્સિડેશન થાય છે, ત્યારે તે ખોરા થઈ જાય છે અને તેમની ગંધ અને સ્વાદ બદલાઈ જાય છે. ખોરાકને ઓક્સિડેશનથી બચાવવા માટે સામાન્ય રીતે તેમાં એન્ટિઓક્સિડન્ટ્સ ઉમેરવામાં આવે છે."
    }
]

blocks.extend(new_blocks)
data['blocks'] = blocks

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Part 1 updated!")
