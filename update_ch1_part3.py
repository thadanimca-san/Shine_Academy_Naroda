import json

filepath = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch1.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

blocks = data.get('blocks', [])

new_blocks = [
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_EX06",
      "type": "theory",
      "title": "Exercise Q6",
      "title_hi": "अभ्यास प्रश्न 6",
      "title_gu": "સ્વાધ્યાય પ્રશ્ન 6",
      "body": "**Question:** Balance the following chemical equations.\n(a) HNO3 + Ca(OH)2 → Ca(NO3)2 + H2O\n(b) NaOH + H2SO4 → Na2SO4 + H2O\n(c) NaCl + AgNO3 → AgCl + NaNO3\n(d) BaCl2 + H2SO4 → BaSO4 + HCl\n\n**Answer:**\n(a) 2HNO3 + Ca(OH)2 → Ca(NO3)2 + 2H2O\n(b) 2NaOH + H2SO4 → Na2SO4 + 2H2O\n(c) NaCl + AgNO3 → AgCl + NaNO3 (Already balanced)\n(d) BaCl2 + H2SO4 → BaSO4 + 2HCl",
      "body_hi": "**प्रश्न:** निम्न रासायनिक समीकरणों को संतुलित कीजिए।\n(a) HNO3 + Ca(OH)2 → Ca(NO3)2 + H2O\n(b) NaOH + H2SO4 → Na2SO4 + H2O\n(c) NaCl + AgNO3 → AgCl + NaNO3\n(d) BaCl2 + H2SO4 → BaSO4 + HCl\n\n**उत्तर:**\n(a) 2HNO3 + Ca(OH)2 → Ca(NO3)2 + 2H2O\n(b) 2NaOH + H2SO4 → Na2SO4 + 2H2O\n(c) NaCl + AgNO3 → AgCl + NaNO3 (पहले से संतुलित है)\n(d) BaCl2 + H2SO4 → BaSO4 + 2HCl",
      "body_gu": "**પ્રશ્ન:** નીચેના રાસાયણિક સમીકરણોને સંતુલિત કરો.\n(a) HNO3 + Ca(OH)2 → Ca(NO3)2 + H2O\n(b) NaOH + H2SO4 → Na2SO4 + H2O\n(c) NaCl + AgNO3 → AgCl + NaNO3\n(d) BaCl2 + H2SO4 → BaSO4 + HCl\n\n**જવાબ:**\n(a) 2HNO3 + Ca(OH)2 → Ca(NO3)2 + 2H2O\n(b) 2NaOH + H2SO4 → Na2SO4 + 2H2O\n(c) NaCl + AgNO3 → AgCl + NaNO3 (પહેલાથી જ સંતુલિત છે)\n(d) BaCl2 + H2SO4 → BaSO4 + 2HCl"
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_EX07",
      "type": "theory",
      "title": "Exercise Q7",
      "title_hi": "अभ्यास प्रश्न 7",
      "title_gu": "સ્વાધ્યાય પ્રશ્ન 7",
      "body": "**Question:** Write the balanced chemical equations for the following reactions.\n(a) Calcium hydroxide + Carbon dioxide → Calcium carbonate + Water\n(b) Zinc + Silver nitrate → Zinc nitrate + Silver\n(c) Aluminium + Copper chloride → Aluminium chloride + Copper\n(d) Barium chloride + Potassium sulphate → Barium sulphate + Potassium chloride\n\n**Answer:**\n(a) Ca(OH)2 + CO2 → CaCO3 + H2O\n(b) Zn + 2AgNO3 → Zn(NO3)2 + 2Ag\n(c) 2Al + 3CuCl2 → 2AlCl3 + 3Cu\n(d) BaCl2 + K2SO4 → BaSO4 + 2KCl",
      "body_hi": "**प्रश्न:** निम्न अभिक्रियाओं के लिए संतुलित रासायनिक समीकरण लिखिए।\n(a) कैल्शियम हाइड्रॉक्साइड + कार्बन डाइऑक्साइड → कैल्शियम कार्बोनेट + जल\n(b) जिंक + सिल्वर नाइट्रेट → जिंक नाइट्रेट + सिल्वर\n(c) एल्युमिनियम + कॉपर क्लोराइड → एल्युमिनियम क्लोराइड + कॉपर\n(d) बेरियम क्लोराइड + पोटैशियम सल्फेट → बेरियम सल्फेट + पोटैशियम क्लोराइड\n\n**उत्तर:**\n(a) Ca(OH)2 + CO2 → CaCO3 + H2O\n(b) Zn + 2AgNO3 → Zn(NO3)2 + 2Ag\n(c) 2Al + 3CuCl2 → 2AlCl3 + 3Cu\n(d) BaCl2 + K2SO4 → BaSO4 + 2KCl",
      "body_gu": "**પ્રશ્ન:** નીચેની પ્રક્રિયાઓ માટે સંતુલિત રાસાયણિક સમીકરણો લખો.\n(a) કેલ્શિયમ હાઇડ્રોક્સાઇડ + કાર્બન ડાયોક્સાઇડ → કેલ્શિયમ કાર્બોનેટ + પાણી\n(b) ઝીંક + સિલ્વર નાઇટ્રેટ → ઝીંક નાઇટ્રેટ + સિલ્વર\n(c) એલ્યુમિનિયમ + કોપર ક્લોરાઇડ → એલ્યુમિનિયમ ક્લોરાઇડ + કોપર\n(d) બેરિયમ ક્લોરાઇડ + પોટેશિયમ સલ્ફેટ → બેરિયમ સલ્ફેટ + પોટેશિયમ ક્લોરાઇડ\n\n**જવાબ:**\n(a) Ca(OH)2 + CO2 → CaCO3 + H2O\n(b) Zn + 2AgNO3 → Zn(NO3)2 + 2Ag\n(c) 2Al + 3CuCl2 → 2AlCl3 + 3Cu\n(d) BaCl2 + K2SO4 → BaSO4 + 2KCl"
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_EX08",
      "type": "theory",
      "title": "Exercise Q8",
      "title_hi": "अभ्यास प्रश्न 8",
      "title_gu": "સ્વાધ્યાય પ્રશ્ન 8",
      "body": "**Question:** Write the balanced chemical equation for the following and identify the type of reaction in each case.\n(a) Potassium bromide (aq) + Barium iodide (aq) → Potassium iodide (aq) + Barium bromide (s)\n(b) Zinc carbonate (s) → Zinc oxide (s) + Carbon dioxide (g)\n(c) Hydrogen (g) + Chlorine (g) → Hydrogen chloride (g)\n(d) Magnesium (s) + Hydrochloric acid (aq) → Magnesium chloride (aq) + Hydrogen (g)\n\n**Answer:**\n(a) 2KBr(aq) + BaI2(aq) → 2KI(aq) + BaBr2(s) (Double displacement reaction)\n(b) ZnCO3(s) → ZnO(s) + CO2(g) (Decomposition reaction)\n(c) H2(g) + Cl2(g) → 2HCl(g) (Combination reaction)\n(d) Mg(s) + 2HCl(aq) → MgCl2(aq) + H2(g) (Displacement reaction)",
      "body_hi": "**प्रश्न:** निम्न के लिए संतुलित रासायनिक समीकरण लिखिए एवं प्रत्येक अभिक्रिया का प्रकार बताइए।\n(a) पोटैशियम ब्रोमाइड (aq) + बेरियम आयोडाइड (aq) → पोटैशियम आयोडाइड (aq) + बेरियम ब्रोमाइड (s)\n(b) जिंक कार्बोनेट (s) → जिंक ऑक्साइड (s) + कार्बन डाइऑक्साइड (g)\n(c) हाइड्रोजन (g) + क्लोरीन (g) → हाइड्रोजन क्लोराइड (g)\n(d) मैग्नीशियम (s) + हाइड्रोक्लोरिक अम्ल (aq) → मैग्नीशियम क्लोराइड (aq) + हाइड्रोजन (g)\n\n**उत्तर:**\n(a) 2KBr(aq) + BaI2(aq) → 2KI(aq) + BaBr2(s) (द्विविस्थापन अभिक्रिया)\n(b) ZnCO3(s) → ZnO(s) + CO2(g) (वियोजन अभिक्रिया)\n(c) H2(g) + Cl2(g) → 2HCl(g) (संयोजन अभिक्रिया)\n(d) Mg(s) + 2HCl(aq) → MgCl2(aq) + H2(g) (विस्थापन अभिक्रिया)",
      "body_gu": "**પ્રશ્ન:** નીચેના માટે સંતુલિત રાસાયણિક સમીકરણ લખો અને દરેક કિસ્સામાં પ્રક્રિયાનો પ્રકાર ઓળખો.\n(a) પોટેશિયમ બ્રોમાઇડ (aq) + બેરિયમ આયોડાઇડ (aq) → પોટેશિયમ આયોડાઇડ (aq) + બેરિયમ બ્રોમાઇડ (s)\n(b) ઝીંક કાર્બોનેટ (s) → ઝીંક ઓક્સાઇડ (s) + કાર્બન ડાયોક્સાઇડ (g)\n(c) હાઇડ્રોજન (g) + ક્લોરિન (g) → હાઇડ્રોજન ક્લોરાઇડ (g)\n(d) મેગ્નેશિયમ (s) + હાઇડ્રોક્લોરિક એસિડ (aq) → મેગ્નેશિયમ ક્લોરાઇડ (aq) + હાઇડ્રોજન (g)\n\n**જવાબ:**\n(a) 2KBr(aq) + BaI2(aq) → 2KI(aq) + BaBr2(s) (દ્વિવિસ્થાપન પ્રક્રિયા)\n(b) ZnCO3(s) → ZnO(s) + CO2(g) (વિઘટન પ્રક્રિયા)\n(c) H2(g) + Cl2(g) → 2HCl(g) (સંયોગીકરણ પ્રક્રિયા)\n(d) Mg(s) + 2HCl(aq) → MgCl2(aq) + H2(g) (વિસ્થાપન પ્રક્રિયા)"
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_EX09",
      "type": "theory",
      "title": "Exercise Q9",
      "title_hi": "अभ्यास प्रश्न 9",
      "title_gu": "સ્વાધ્યાય પ્રશ્ન 9",
      "body": "**Question:** What does one mean by exothermic and endothermic reactions? Give examples.\n\n**Answer:** \n**Exothermic reactions:** Reactions in which heat is released along with the formation of products are called exothermic reactions. Example: Respiration, burning of natural gas (CH4 + 2O2 → CO2 + 2H2O + Heat).\n**Endothermic reactions:** Reactions in which energy is absorbed are known as endothermic reactions. Example: Decomposition of calcium carbonate (CaCO3 + Heat → CaO + CO2).",
      "body_hi": "**प्रश्न:** ऊष्माक्षेपी एवं ऊष्माशोषी अभिक्रिया का क्या अर्थ है? उदाहरण दीजिए।\n\n**उत्तर:** \n**ऊष्माक्षेपी अभिक्रियाएँ:** जिन अभिक्रियाओं में उत्पाद के निर्माण के साथ-साथ ऊष्मा भी उत्पन्न होती है, उन्हें ऊष्माक्षेपी अभिक्रियाएँ कहते हैं। उदाहरण: श्वसन, प्राकृतिक गैस का दहन (CH4 + 2O2 → CO2 + 2H2O + ऊष्मा)।\n**ऊष्माशोषी अभिक्रियाएँ:** जिन अभिक्रियाओं में ऊर्जा अवशोषित होती है, उन्हें ऊष्माशोषी अभिक्रियाएँ कहते हैं। उदाहरण: कैल्शियम कार्बोनेट का वियोजन (CaCO3 + ऊष्मा → CaO + CO2)।",
      "body_gu": "**પ્રશ્ન:** ઉષ્માક્ષેપક અને ઉષ્માશોષક પ્રક્રિયાઓનો અર્થ શું છે? ઉદાહરણ આપો.\n\n**જવાબ:** \n**ઉષ્માક્ષેપક પ્રક્રિયાઓ:** જે પ્રક્રિયાઓમાં નીપજોના નિર્માણની સાથે ઉષ્મા પણ મુક્ત થાય છે તેને ઉષ્માક્ષેપક પ્રક્રિયાઓ કહેવાય છે. ઉદાહરણ: શ્વસન, કુદરતી વાયુનું દહન (CH4 + 2O2 → CO2 + 2H2O + ઉષ્મા).\n**ઉષ્માશોષક પ્રક્રિયાઓ:** જે પ્રક્રિયાઓમાં ઉર્જા શોષાય છે તેને ઉષ્માશોષક પ્રક્રિયાઓ કહેવામાં આવે છે. ઉદાહરણ: કેલ્શિયમ કાર્બોનેટનું વિઘટન (CaCO3 + ઉષ્મા → CaO + CO2)."
    },
    {
      "id": "KOBJ_NCERT_C10_SCI_CH1_EX10",
      "type": "theory",
      "title": "Exercise Q10",
      "title_hi": "अभ्यास प्रश्न 10",
      "title_gu": "સ્વાધ્યાય પ્રશ્ન 10",
      "body": "**Question:** Why is respiration considered an exothermic reaction? Explain.\n\n**Answer:** During respiration, the glucose in our body combines with oxygen in the cells to form carbon dioxide and water, and energy is released. Since energy (heat) is released during this process, respiration is considered an exothermic reaction. \nC6H12O6(aq) + 6O2(aq) → 6CO2(aq) + 6H2O(l) + Energy.",
      "body_hi": "**प्रश्न:** श्वसन को ऊष्माक्षेपी अभिक्रिया क्यों कहा जाता है? वर्णन कीजिए।\n\n**उत्तर:** श्वसन के दौरान, हमारे शरीर में ग्लूकोज कोशिकाओं में ऑक्सीजन के साथ मिलकर कार्बन डाइऑक्साइड और पानी बनाता है, और ऊर्जा मुक्त होती है। चूंकि इस प्रक्रिया के दौरान ऊर्जा (ऊष्मा) मुक्त होती है, इसलिए श्वसन को ऊष्माक्षेपी अभिक्रिया माना जाता है।\nC6H12O6(aq) + 6O2(aq) → 6CO2(aq) + 6H2O(l) + ऊर्जा।",
      "body_gu": "**પ્રશ્ન:** શ્વસનને ઉષ્માક્ષેપક પ્રક્રિયા શા માટે ગણવામાં આવે છે? સમજાવો.\n\n**જવાબ:** શ્વસન દરમિયાન, આપણા શરીરમાં રહેલું ગ્લુકોઝ કોષોમાં ઓક્સિજન સાથે જોડાઈને કાર્બન ડાયોક્સાઇડ અને પાણી બનાવે છે, અને ઉર્જા મુક્ત થાય છે. આ પ્રક્રિયા દરમિયાન ઉર્જા (ઉષ્મા) મુક્ત થતી હોવાથી, શ્વસનને ઉષ્માક્ષેપક પ્રક્રિયા ગણવામાં આવે છે.\nC6H12O6(aq) + 6O2(aq) → 6CO2(aq) + 6H2O(l) + ઉર્જા."
    }
]

blocks.extend(new_blocks)
data['blocks'] = blocks

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Part 3 (Ex 6-10) updated!")
