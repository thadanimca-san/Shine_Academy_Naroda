import json
import os

blocks = [
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_001",
        "type": "hook",
        "title": "Is It Alive?",
        "title_hi": "क्या यह जीवित है?",
        "title_gu": "શું તે જીવંત છે?",
        "body": "How do we tell the difference between what is alive and what is not alive? If we see a dog running, a cow chewing cud, or a human shouting, we know they are living. But what about plants? They don't shout or run. Yet, invisible molecular movements are happening inside them every second. Life is not just about visible movement; it is about continuous maintenance!",
        "body_hi": "हम जीवित और निर्जीव के बीच अंतर कैसे बताते हैं? यदि हम किसी कुत्ते को दौड़ते, गाय को जुगाली करते या मनुष्य को चिल्लाते हुए देखते हैं, तो हम जानते हैं कि वे जीवित हैं। लेकिन पौधों के बारे में क्या? वे चिल्लाते या दौड़ते नहीं हैं। फिर भी, उनके अंदर हर सेकंड अदृश्य आणविक गतिविधियां हो रही हैं। जीवन केवल दृश्य गति के बारे में नहीं है; यह निरंतर रखरखाव के बारे में है!",
        "body_gu": "આપણે જીવંત અને નિર્જીવ વચ્ચેનો તફાવત કેવી રીતે જાણી શકીએ? જો આપણે કૂતરાને દોડતો, ગાયને વાગોળતી કે માણસને બૂમો પાડતો જોઈએ, તો આપણે જાણીએ છીએ કે તેઓ જીવંત છે. પરંતુ વનસ્પતિઓ વિશે શું? તેઓ બૂમો પાડતા નથી કે દોડતા નથી. છતાં, તેમની અંદર દર સેકન્ડે અદ્રશ્ય આણ્વીય ગતિવિધિઓ થઈ રહી હોય છે. જીવન માત્ર દેખીતી હિલચાલ નથી; તે સતત જાળવણી છે!"
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_002",
        "type": "socratic_question",
        "title": "The Virus Dilemma",
        "title_hi": "वायरस की दुविधा",
        "title_gu": "વાયરસની દ્વિધા",
        "question": "Viruses do not show any molecular movement in them until they infect a cell. Based on this, do you think viruses are truly alive?",
        "question_hi": "वायरस जब तक किसी कोशिका को संक्रमित नहीं करते, तब तक उनमें कोई आणविक गति नहीं होती है। इसके आधार पर, क्या आपको लगता है कि वायरस वास्तव में जीवित हैं?",
        "question_gu": "વાયરસ જ્યાં સુધી કોઈ કોષમાં દાખલ ન થાય ત્યાં સુધી તેમાં કોઈ આણ્વીય હિલચાલ જોવા મળતી નથી. આના આધારે, શું તમને લાગે છે કે વાયરસ ખરેખર જીવંત છે?",
        "options": [
            "Yes, because they have DNA or RNA.",
            "No, they are completely non-living.",
            "They are on the borderline of living and non-living.",
            "Yes, because they can cause diseases."
        ],
        "options_hi": [
            "हाँ, क्योंकि उनके पास डीएनए या आरएनए होता है।",
            "नहीं, वे पूरी तरह से निर्जीव हैं।",
            "वे सजीव और निर्जीव की सीमा रेखा पर हैं।",
            "हाँ, क्योंकि वे रोग पैदा कर सकते हैं।"
        ],
        "options_gu": [
            "હા, કારણ કે તેમની પાસે ડીએનએ અથવા આરએનએ છે.",
            "ના, તેઓ સંપૂર્ણપણે નિર્જીવ છે.",
            "તેઓ સજીવ અને નિર્જીવની સીમારેખા પર છે.",
            "હા, કારણ કે તેઓ રોગ પેદા કરી શકે છે."
        ],
        "correct_index": 2,
        "explanation": "Viruses remain inactive (non-living) outside a host body. They only show signs of life (reproduction and molecular movement) when they enter a host cell, making them a biological puzzle.",
        "explanation_hi": "वायरस मेजबान शरीर के बाहर निष्क्रिय (निर्जीव) रहते हैं। वे जीवन के लक्षण (प्रजनन और आणविक गति) तभी दिखाते हैं जब वे किसी मेजबान कोशिका में प्रवेश करते हैं, जिससे वे एक जैविक पहेली बन जाते हैं।",
        "explanation_gu": "વાયરસ યજમાનના શરીરની બહાર નિષ્ક્રિય (નિર્જીવ) રહે છે. જ્યારે તેઓ યજમાન કોષમાં પ્રવેશે છે ત્યારે જ તેઓ જીવનના લક્ષણો (પ્રજનન અને આણ્વીય ગતિ) દર્શાવે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_003",
        "type": "discovery",
        "title": "What are Life Processes?",
        "title_hi": "जैव प्रक्रम क्या हैं?",
        "title_gu": "જૈવિક પ્રક્રિયાઓ શું છે?",
        "body": "Since living organisms are highly organized structures, they tend to break down over time due to environmental effects. To prevent this, they need continuous repair and maintenance. The basic processes in living organisms which are essential for maintaining their life are called Life Processes. The major ones are: Nutrition, Respiration, Transportation, and Excretion.",
        "body_hi": "चूंकि जीव अत्यधिक संगठित संरचनाएं हैं, इसलिए पर्यावरणीय प्रभावों के कारण वे समय के साथ टूट सकते हैं। इसे रोकने के लिए, उन्हें निरंतर मरम्मत और रखरखाव की आवश्यकता होती है। जीवों में वे बुनियादी प्रक्रियाएं जो उनके जीवन को बनाए रखने के लिए आवश्यक हैं, जैव प्रक्रम कहलाती हैं। प्रमुख जैव प्रक्रम हैं: पोषण, श्वसन, वहन और उत्सर्जन।",
        "body_gu": "સજીવો ખૂબ જ સંગઠિત રચનાઓ હોવાથી, પર્યાવરણની અસરોને કારણે સમય જતાં તેઓ તૂટી શકે છે. આને રોકવા માટે, તેમને સતત સમારકામ અને જાળવણીની જરૂર છે. સજીવોમાં થતી એવી બધી જ ક્રિયાઓ જે સામૂહિક રીતે સજીવના અસ્તિત્વને જાળવી રાખવાનું કાર્ય કરે છે, તેને જૈવિક પ્રક્રિયાઓ કહે છે. મુખ્ય પ્રક્રિયાઓ છે: પોષણ, શ્વસન, વહન અને ઉત્સર્જન."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_004",
        "type": "theory",
        "title": "Nutrition: The Energy Source",
        "title_hi": "पोषण: ऊर्जा का स्रोत",
        "title_gu": "પોષણ: ઊર્જાનો સ્ત્રોત",
        "body": "Nutrition is the process of taking in food and utilizing it to generate energy and build the body. There are two main modes:\n1. Autotrophic Nutrition: Organisms (like green plants) use simple inorganic materials (CO2 and H2O) to synthesize their own food using sunlight.\n2. Heterotrophic Nutrition: Organisms (like animals and fungi) depend on other organisms for complex organic food.",
        "body_hi": "पोषण भोजन ग्रहण करने और शरीर के निर्माण तथा ऊर्जा उत्पन्न करने के लिए इसका उपयोग करने की प्रक्रिया है। इसके दो मुख्य तरीके हैं:\n1. स्वपोषी पोषण: जीव (जैसे हरे पौधे) सूर्य के प्रकाश का उपयोग करके सरल अकार्बनिक पदार्थों (CO2 और H2O) से अपना भोजन स्वयं बनाते हैं।\n2. विषमपोषी पोषण: जीव (जैसे जानवर और कवक) जटिल कार्बनिक भोजन के लिए अन्य जीवों पर निर्भर करते हैं।",
        "body_gu": "ખોરાક ગ્રહણ કરવાની અને ઊર્જા ઉત્પન્ન કરવા તથા શરીરના નિર્માણ માટે તેનો ઉપયોગ કરવાની પ્રક્રિયા એટલે પોષણ. તેના બે મુખ્ય પ્રકાર છે:\n1. સ્વયંપોષી પોષણ: સજીવો (જેમ કે લીલી વનસ્પતિ) સૂર્યપ્રકાશનો ઉપયોગ કરીને સરળ અકાર્બનિક પદાર્થો (CO2 અને H2O) માંથી પોતાનો ખોરાક જાતે બનાવે છે.\n2. વિષમપોષી પોષણ: સજીવો (જેમ કે પ્રાણીઓ અને ફૂગ) જટિલ કાર્બનિક ખોરાક માટે અન્ય સજીવો પર આધાર રાખે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_005",
        "type": "theory",
        "title": "Photosynthesis: The Green Factory",
        "title_hi": "प्रकाश संश्लेषण: हरी फैक्ट्री",
        "title_gu": "પ્રકાશસંશ્લેષણ: લીલી ફેક્ટરી",
        "body": "Photosynthesis is the process by which autotrophs take in CO2 and H2O and convert them into carbohydrates (glucose) in the presence of sunlight and chlorophyll. \nEquation: 6CO2 + 12H2O + Sunlight -> C6H12O6 (Glucose) + 6O2 + 6H2O.\nThe three main events are:\n(i) Absorption of light energy by chlorophyll.\n(ii) Conversion of light energy to chemical energy and splitting of water into hydrogen and oxygen.\n(iii) Reduction of carbon dioxide to carbohydrates.",
        "body_hi": "प्रकाश संश्लेषण वह प्रक्रिया है जिसके द्वारा स्वपोषी CO2 और H2O ग्रहण करते हैं और उन्हें सूर्य के प्रकाश तथा क्लोरोफिल की उपस्थिति में कार्बोहाइड्रेट (ग्लूकोज) में परिवर्तित करते हैं।\nसमीकरण: 6CO2 + 12H2O + सूर्य का प्रकाश -> C6H12O6 (ग्लूकोज) + 6O2 + 6H2O.\nतीन मुख्य घटनाएं हैं:\n(i) क्लोरोफिल द्वारा प्रकाश ऊर्जा का अवशोषण।\n(ii) प्रकाश ऊर्जा का रासायनिक ऊर्जा में रूपांतरण और जल का हाइड्रोजन तथा ऑक्सीजन में टूटना।\n(iii) कार्बन डाइऑक्साइड का कार्बोहाइड्रेट में अपचयन।",
        "body_gu": "પ્રકાશસંશ્લેષણ એ એક એવી પ્રક્રિયા છે જેમાં સ્વયંપોષીઓ સૂર્યપ્રકાશ અને ક્લોરોફિલની હાજરીમાં CO2 અને H2O નો ઉપયોગ કરીને કાર્બોદિત (ગ્લુકોઝ) બનાવે છે.\nસમીકરણ: 6CO2 + 12H2O + સૂર્યપ્રકાશ -> C6H12O6 (ગ્લુકોઝ) + 6O2 + 6H2O.\nતેમાં ત્રણ મુખ્ય ઘટનાઓ બને છે:\n(i) ક્લોરોફિલ દ્વારા પ્રકાશ-ઊર્જાનું શોષણ.\n(ii) પ્રકાશ-ઊર્જાનું રાસાયણિક ઊર્જામાં રૂપાંતર અને પાણીના અણુઓનું હાઇડ્રોજન અને ઓક્સિજનમાં વિઘટન.\n(iii) કાર્બન ડાયોક્સાઇડનું કાર્બોદિતમાં રિડક્શન."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_006",
        "type": "socratic_question",
        "title": "Desert Plants Mystery",
        "title_hi": "रेगिस्तानी पौधों का रहस्य",
        "title_gu": "રણની વનસ્પતિઓનું રહસ્ય",
        "question": "If stomata open during the day to take in CO2, plants lose a lot of water. How do desert plants survive this water loss while still performing photosynthesis?",
        "question_hi": "यदि CO2 लेने के लिए दिन के दौरान रंध्र (stomata) खुलते हैं, तो पौधों से बहुत सारा पानी वाष्पित हो जाता है। रेगिस्तानी पौधे इस पानी के नुकसान से कैसे बचते हैं और फिर भी प्रकाश संश्लेषण कैसे करते हैं?",
        "question_gu": "જો CO2 મેળવવા માટે દિવસ દરમિયાન પર્ણરંધ્રો ખુલ્લા રહે, તો વનસ્પતિમાંથી ઘણું પાણી બાષ્પીભવન પામે છે. રણપ્રદેશની વનસ્પતિઓ આ પાણીનો વ્યય અટકાવીને પ્રકાશસંશ્લેષણ કેવી રીતે કરે છે?",
        "options": [
            "They don't need CO2 for photosynthesis.",
            "They take up CO2 at night and prepare an intermediate compound, which is acted upon by sunlight during the day.",
            "They keep their stomata completely closed forever and use oxygen instead.",
            "They absorb water directly from the hot desert air."
        ],
        "options_hi": [
            "उन्हें प्रकाश संश्लेषण के लिए CO2 की आवश्यकता नहीं होती है।",
            "वे रात में CO2 ग्रहण करते हैं और एक मध्यवर्ती यौगिक तैयार करते हैं, जिस पर दिन के दौरान सूर्य का प्रकाश कार्य करता है।",
            "वे अपने रंध्रों को हमेशा के लिए पूरी तरह से बंद रखते हैं और इसके बजाय ऑक्सीजन का उपयोग करते हैं।",
            "वे सीधे गर्म रेगिस्तानी हवा से पानी सोखते हैं।"
        ],
        "options_gu": [
            "તેમને પ્રકાશસંશ્લેષણ માટે CO2 ની જરૂર હોતી નથી.",
            "તેઓ રાત્રિ દરમિયાન CO2 મેળવે છે અને એક મધ્યવર્તી નીપજ બનાવે છે, જેના પર દિવસ દરમિયાન સૂર્યપ્રકાશ કાર્ય કરે છે.",
            "તેઓ તેમના પર્ણરંધ્રો હંમેશા માટે સંપૂર્ણપણે બંધ રાખે છે અને તેના બદલે ઓક્સિજનનો ઉપયોગ કરે છે.",
            "તેઓ ગરમ રણની હવામાંથી સીધું પાણી શોષી લે છે."
        ],
        "correct_index": 1,
        "explanation": "Desert plants take up CO2 at night (when it's cool and water loss is minimal) and form an intermediate acid. During the day, when stomata are closed to save water, the sunlight acts on this stored compound to complete photosynthesis.",
        "explanation_hi": "रेगिस्तानी पौधे रात में CO2 ग्रहण करते हैं (जब मौसम ठंडा होता है और पानी का नुकसान कम होता है) और एक मध्यवर्ती अम्ल बनाते हैं। दिन के दौरान, जब पानी बचाने के लिए रंध्र बंद होते हैं, तो प्रकाश संश्लेषण को पूरा करने के लिए सूर्य का प्रकाश इस संग्रहीत यौगिक पर कार्य करता है।",
        "explanation_gu": "રણની વનસ્પતિઓ રાત્રિ દરમિયાન CO2 મેળવે છે (જ્યારે વાતાવરણ ઠંડુ હોય છે અને પાણીનો વ્યય ઓછો થાય છે) અને એક મધ્યવર્તી એસિડ બનાવે છે. દિવસ દરમિયાન, જ્યારે પાણી બચાવવા માટે રંધ્રો બંધ હોય છે, ત્યારે પ્રકાશસંશ્લેષણ પૂર્ણ કરવા માટે સૂર્યપ્રકાશ આ સંગ્રહિત સંયોજન પર કાર્ય કરે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_007",
        "type": "theory",
        "title": "Nutrition in Human Beings",
        "title_hi": "मानव में पोषण",
        "title_gu": "મનુષ્યમાં પોષણ",
        "body": "The human digestive system comprises the alimentary canal and associated glands. \n1. Mouth: Saliva contains salivary amylase which breaks down starch into sugar.\n2. Stomach: Gastric glands release HCl, Pepsin (protein digestion), and Mucus (protection).\n3. Small Intestine: The site of COMPLETE digestion. It receives bile from the liver (emulsifies fats) and pancreatic juice (trypsin for proteins, lipase for fats). Villi absorb the digested food.\n4. Large Intestine: Absorbs excess water and excretes solid waste.",
        "body_hi": "मानव पाचन तंत्र में आहार नली और संबंधित ग्रंथियां शामिल हैं।\n1. मुंह: लार में लार एमाइलेज होता है जो स्टार्च को शर्करा में तोड़ता है।\n2. आमाशय: जठर ग्रंथियां HCl, पेप्सिन (प्रोटीन पाचन), और श्लेष्मा (सुरक्षा) छोड़ती हैं।\n3. छोटी आंत: पूर्ण पाचन का स्थल। यह यकृत से पित्त (वसा का इमल्सीकरण) और अग्नाशयी रस (प्रोटीन के लिए ट्रिप्सिन, वसा के लिए लाइपेज) प्राप्त करता है। विली पचे हुए भोजन को अवशोषित करते हैं।\n4. बड़ी आंत: अतिरिक्त पानी को अवशोषित करती है और ठोस अपशिष्ट को बाहर निकालती है।",
        "body_gu": "માનવ પાચનતંત્રમાં પાચનમાર્ગ અને તેની સાથે સંકળાયેલી ગ્રંથિઓનો સમાવેશ થાય છે.\n1. મુખ: લાળમાં એમાયલેઝ ઉત્સેચક હોય છે જે સ્ટાર્ચનું શર્કરામાં પાચન કરે છે.\n2. જઠર: જઠર ગ્રંથિઓ HCl, પેપ્સિન (પ્રોટીનનું પાચન) અને શ્લેષ્મ (રક્ષણ) નો સ્ત્રાવ કરે છે.\n3. નાનું આંતરડું: સંપૂર્ણ પાચનનું સ્થાન. તે યકૃતમાંથી પિત્ત (ચરબીનું તૈલોદકીકરણ) અને સ્વાદુપિંડમાંથી સ્વાદુરસ (પ્રોટીન માટે ટ્રિપ્સિન, ચરબી માટે લાઇપેઝ) મેળવે છે. રસાંકુરો પચેલા ખોરાકનું શોષણ કરે છે.\n4. મોટું આંતરડું: વધારાના પાણીનું શોષણ કરે છે અને મળનો નિકાલ કરે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_008",
        "type": "theory",
        "title": "Respiration: Extracting Energy",
        "title_hi": "श्वसन: ऊर्जा निकालना",
        "title_gu": "શ્વસન: ઊર્જા મુક્ત કરવી",
        "body": "Respiration is the process of breaking down food (glucose) to release energy. The first step happens in the cytoplasm where 6-carbon glucose breaks into 3-carbon pyruvate.\nFrom here, there are three paths:\n1. Aerobic Respiration (Presence of O2, in Mitochondria): Produces CO2, Water, and a LOT of energy (38 ATP).\n2. Anaerobic Respiration in Yeast (Absence of O2): Produces Ethanol, CO2, and less energy (2 ATP).\n3. Lack of Oxygen in Human Muscles: Produces Lactic acid and energy. Accumulation of lactic acid causes muscle cramps.",
        "body_hi": "श्वसन ऊर्जा मुक्त करने के लिए भोजन (ग्लूकोज) को तोड़ने की प्रक्रिया है। पहला चरण कोशिकाद्रव्य में होता है जहां 6-कार्बन ग्लूकोज 3-कार्बन पाइरुवेट में टूट जाता है।\nयहाँ से, तीन रास्ते हैं:\n1. वायवीय श्वसन (O2 की उपस्थिति, माइटोकॉन्ड्रिया में): CO2, पानी और बहुत अधिक ऊर्जा (38 ATP) पैदा करता है।\n2. खमीर में अवायवीय श्वसन (O2 की अनुपस्थिति): इथेनॉल, CO2 और कम ऊर्जा (2 ATP) पैदा करता है।\n3. मानव मांसपेशियों में ऑक्सीजन की कमी: लैक्टिक अम्ल और ऊर्जा पैदा करता है। लैक्टिक अम्ल के जमा होने से मांसपेशियों में ऐंठन होती है।",
        "body_gu": "શ્વસન એ ઊર્જા મુક્ત કરવા માટે ખોરાક (ગ્લુકોઝ) ના વિઘટનની પ્રક્રિયા છે. પ્રથમ તબક્કો કોષરસમાં થાય છે જ્યાં 6-કાર્બન ગ્લુકોઝ 3-કાર્બન પાયરુવેટમાં તૂટી જાય છે.\nઅહીંથી, ત્રણ માર્ગો છે:\n1. જારક શ્વસન (O2 ની હાજરી, કણભસૂત્રમાં): CO2, પાણી અને વધુ માત્રામાં ઊર્જા ઉત્પન્ન કરે છે.\n2. યીસ્ટમાં અજારક શ્વસન (O2 ની ગેરહાજરી): ઇથેનોલ, CO2 અને ઓછી ઊર્જા ઉત્પન્ન કરે છે.\n3. માનવ સ્નાયુઓમાં ઓક્સિજનનો અભાવ: લેક્ટિક એસિડ અને ઊર્જા ઉત્પન્ન કરે છે. લેક્ટિક એસિડ જમા થવાથી સ્નાયુઓમાં ખેંચાણ થાય છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_009",
        "type": "theory",
        "title": "Transportation in Humans: The Heart",
        "title_hi": "मनुष्य में वहन: हृदय",
        "title_gu": "મનુષ્યમાં વહન: હૃદય",
        "body": "The human heart is a muscular organ with four chambers. The upper chambers (atria) receive blood, and the lower chambers (ventricles) pump it out. \n- Right side handles Deoxygenated blood (from body to lungs).\n- Left side handles Oxygenated blood (from lungs to body).\nThis complete separation ensures high-efficiency oxygen supply, which is critical for maintaining body temperature in mammals and birds. This process where blood passes through the heart twice during one cycle is called Double Circulation.",
        "body_hi": "मानव हृदय चार कक्षों वाला एक पेशीय अंग है। ऊपरी कक्ष (आलिंद) रक्त प्राप्त करते हैं, और निचले कक्ष (निलय) इसे बाहर पंप करते हैं।\n- दाहिना भाग विऑक्सीजनित रक्त (शरीर से फेफड़ों तक) को संभालता है।\n- बायां भाग ऑक्सीजनित रक्त (फेफड़ों से शरीर तक) को संभालता है।\nयह पूर्ण पृथक्करण उच्च दक्षता वाली ऑक्सीजन की आपूर्ति सुनिश्चित करता है, जो स्तनधारियों और पक्षियों में शरीर के तापमान को बनाए रखने के लिए महत्वपूर्ण है। यह प्रक्रिया जहां रक्त एक चक्र के दौरान दो बार हृदय से होकर गुजरता है, दोहरा परिसंचरण कहलाती है।",
        "body_gu": "માનવ હૃદય ચાર ખંડો ધરાવતું એક સ્નાયુલ અંગ છે. ઉપરના ખંડો (કર્ણકો) રુધિર મેળવે છે, અને નીચેના ખંડો (ક્ષેપકો) તેને પમ્પ કરે છે.\n- જમણો ભાગ ઓક્સિજનવિહીન રુધિર (શરીરથી ફેફસાં સુધી) નું વહન કરે છે.\n- ડાબો ભાગ ઓક્સિજનયુક્ત રુધિર (ફેફસાંથી શરીર સુધી) નું વહન કરે છે.\nઆ સંપૂર્ણ અલગીકરણ અત્યંત કાર્યક્ષમ ઓક્સિજનનો પુરવઠો સુનિશ્ચિત કરે છે, જે સસ્તન પ્રાણીઓ અને પક્ષીઓમાં શરીરનું તાપમાન જાળવી રાખવા માટે મહત્વપૂર્ણ છે. રુધિર એક ચક્ર દરમિયાન બે વાર હૃદયમાંથી પસાર થાય છે, જેને બેવડું પરિવહન કહેવાય છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_010",
        "type": "theory",
        "title": "Transportation in Plants",
        "title_hi": "पौधों में वहन",
        "title_gu": "વનસ્પતિમાં વહન",
        "body": "Plants need a transport system to move water from roots to leaves, and food from leaves to other parts.\n1. Xylem: Transports water and minerals upwards. This is mainly driven by Transpiration Pull—a suction force created when water evaporates from leaves through stomata.\n2. Phloem: Transports the soluble products of photosynthesis (food) to all parts of the plant. This process is called Translocation and it requires energy in the form of ATP.",
        "body_hi": "पौधों को जड़ों से पत्तियों तक पानी ले जाने और पत्तियों से अन्य भागों में भोजन ले जाने के लिए एक परिवहन प्रणाली की आवश्यकता होती है।\n1. जाइलम: पानी और खनिजों को ऊपर की ओर ले जाता है। यह मुख्य रूप से वाष्पोत्सर्जन खिंचाव द्वारा संचालित होता है - एक चूषण बल जो तब बनता है जब रंध्रों के माध्यम से पत्तियों से पानी वाष्पित होता है।\n2. फ्लोएम: प्रकाश संश्लेषण (भोजन) के घुलनशील उत्पादों को पौधे के सभी भागों में ले जाता है। इस प्रक्रिया को स्थानांतरण कहा जाता है और इसके लिए ATP के रूप में ऊर्जा की आवश्यकता होती है।",
        "body_gu": "વનસ્પતિઓને મૂળમાંથી પર્ણો સુધી પાણી અને પર્ણોમાંથી અન્ય ભાગોમાં ખોરાક પહોંચાડવા માટે વહનતંત્રની જરૂર હોય છે.\n1. જલવાહક પેશી (Xylem): પાણી અને ખનિજ ક્ષારોનું ઉપર તરફ વહન કરે છે. પર્ણરંધ્રોમાંથી પાણીનું બાષ્પીભવન થવાથી ઉત્પન્ન થતા બાષ્પોત્સર્જન ખેંચાણ દ્વારા આ વહન થાય છે.\n2. અન્નવાહક પેશી (Phloem): પ્રકાશસંશ્લેષણની નીપજો (ખોરાક) નું વનસ્પતિના તમામ ભાગોમાં વહન કરે છે. આ પ્રક્રિયાને સ્થાનાંતરણ (Translocation) કહેવાય છે અને તેના માટે ATP સ્વરૂપે ઊર્જાની જરૂર પડે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_011",
        "type": "theory",
        "title": "Excretion: Cleaning the System",
        "title_hi": "उत्सर्जन: प्रणाली की सफाई",
        "title_gu": "ઉત્સર્જન: તંત્રની સફાઈ",
        "body": "Excretion is the biological process of removing harmful metabolic wastes from the body. \nIn Humans: The kidneys contain million of filtration units called Nephrons. A nephron filters blood to remove urea and uric acid, reabsorbs useful substances (like glucose, amino acids, and water), and forms urine. Urine is stored in the urinary bladder before being passed out.\nIn Plants: Plants excrete waste by losing leaves, releasing oxygen through stomata, and storing waste products as resins and gums.",
        "body_hi": "उत्सर्जन शरीर से हानिकारक उपापचयी अपशिष्टों को निकालने की जैविक प्रक्रिया है।\nमनुष्यों में: गुर्दे (वृक्क) में लाखों निस्पंदन इकाइयां होती हैं जिन्हें वृक्काणु (नेफ्रॉन) कहा जाता है। एक नेफ्रॉन यूरिया और यूरिक एसिड को हटाने के लिए रक्त को छानता है, उपयोगी पदार्थों (जैसे ग्लूकोज, अमीनो एसिड और पानी) को पुनरावशोषित करता है, और मूत्र बनाता है। मूत्र को बाहर निकालने से पहले मूत्राशय में जमा किया जाता है।\nपौधों में: पौधे पत्तियों को गिराकर, रंध्रों के माध्यम से ऑक्सीजन जारी करके, और अपशिष्ट उत्पादों को रेजिन और गोंद के रूप में संग्रहीत करके अपशिष्ट का उत्सर्जन करते हैं।",
        "body_gu": "ઉત્સર્જન એ શરીરમાંથી હાનિકારક ચયાપચયી કચરો દૂર કરવાની જૈવિક પ્રક્રિયા છે.\nમનુષ્યમાં: મૂત્રપિંડમાં લાખો ગાળણ એકમો હોય છે જેને ઉત્સર્ગએકમ (નેફ્રોન) કહેવાય છે. નેફ્રોન લોહીમાંથી યુરિયા અને યુરિક એસિડ દૂર કરવા માટે ગાળણ કરે છે, ઉપયોગી પદાર્થો (જેમ કે ગ્લુકોઝ, એમિનો એસિડ અને પાણી) નું પુનઃશોષણ કરે છે અને મૂત્રનું નિર્માણ કરે છે. નિકાલ થતાં પહેલાં મૂત્રનો મૂત્રાશયમાં સંગ્રહ થાય છે.\nવનસ્પતિમાં: વનસ્પતિઓ પર્ણો ખેરવીને, પર્ણરંધ્રો દ્વારા ઓક્સિજન મુક્ત કરીને, અને રેઝિન તથા ગુંદર સ્વરૂપે નકામા પદાર્થોનો સંગ્રહ કરીને ઉત્સર્જન કરે છે."
    }
]

# Now let's add the exactly 13 NCERT questions
ncert_questions = [
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_012",
        "type": "mcq",
        "title": "NCERT Exercise Q1",
        "title_hi": "NCERT अभ्यास Q1",
        "title_gu": "NCERT સ્વાધ્યાય Q1",
        "question": "The kidneys in human beings are a part of the system for:",
        "question_hi": "मनुष्यों में वृक्क (किडनी) किस तंत्र का एक भाग हैं?",
        "question_gu": "મનુષ્યમાં મૂત્રપિંડ એ શાનો એક ભાગ છે?",
        "options": ["Nutrition", "Respiration", "Excretion", "Transportation"],
        "options_hi": ["पोषण", "श्वसन", "उत्सर्जन", "परिवहन"],
        "options_gu": ["પોષણ", "શ્વસન", "ઉત્સર્જન", "પરિવહન"],
        "correct_index": 2,
        "explanation": "Kidneys are the primary organs of the excretory system, responsible for filtering nitrogenous wastes from the blood.",
        "explanation_hi": "वृक्क उत्सर्जन तंत्र के प्राथमिक अंग हैं, जो रक्त से नाइट्रोजनयुक्त अपशिष्टों को छानने के लिए जिम्मेदार हैं।",
        "explanation_gu": "મૂત્રપિંડ ઉત્સર્જન તંત્રના મુખ્ય અંગો છે, જે લોહીમાંથી નાઇટ્રોજનયુક્ત કચરાને ગાળવા માટે જવાબદાર છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_013",
        "type": "mcq",
        "title": "NCERT Exercise Q2",
        "title_hi": "NCERT अभ्यास Q2",
        "title_gu": "NCERT સ્વાધ્યાય Q2",
        "question": "The xylem in plants are responsible for:",
        "question_hi": "पौधों में जाइलम किसके लिए उत्तरदायी है?",
        "question_gu": "વનસ્પતિઓમાં જલવાહક પેશી શાના માટે જવાબદાર છે?",
        "options": [
            "transport of water",
            "transport of food",
            "transport of amino acids",
            "transport of oxygen"
        ],
        "options_hi": [
            "जल का वहन",
            "भोजन का वहन",
            "अमीनो अम्ल का वहन",
            "ऑक्सीजन का वहन"
        ],
        "options_gu": [
            "પાણીનું વહન",
            "ખોરાકનું વહન",
            "એમિનો એસિડનું વહન",
            "ઓક્સિજનનું વહન"
        ],
        "correct_index": 0,
        "explanation": "Xylem tissue transports water and dissolved minerals from the roots to the rest of the plant. Phloem transports food.",
        "explanation_hi": "जाइलम ऊतक जड़ों से पौधे के बाकी हिस्सों तक पानी और घुले हुए खनिजों को पहुंचाता है। फ्लोएम भोजन पहुंचाता है।",
        "explanation_gu": "જલવાહક પેશી મૂળમાંથી વનસ્પતિના બાકીના ભાગોમાં પાણી અને દ્રાવ્ય ખનિજોનું વહન કરે છે. અન્નવાહક ખોરાકનું વહન કરે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_014",
        "type": "mcq",
        "title": "NCERT Exercise Q3",
        "title_hi": "NCERT अभ्यास Q3",
        "title_gu": "NCERT સ્વાધ્યાય Q3",
        "question": "The autotrophic mode of nutrition requires:",
        "question_hi": "स्वपोषी पोषण के लिए क्या आवश्यक है?",
        "question_gu": "સ્વયંપોષી પોષણ માટે શું જરૂરી છે?",
        "options": [
            "carbon dioxide and water",
            "chlorophyll",
            "sunlight",
            "all of the above"
        ],
        "options_hi": [
            "कार्बन डाइऑक्साइड तथा जल",
            "क्लोरोफिल",
            "सूर्य का प्रकाश",
            "उपरोक्त सभी"
        ],
        "options_gu": [
            "કાર્બન ડાયોક્સાઇડ અને પાણી",
            "ક્લોરોફિલ",
            "સૂર્યપ્રકાશ",
            "આપેલ તમામ"
        ],
        "correct_index": 3,
        "explanation": "Autotrophic nutrition (photosynthesis) needs CO2, H2O, chlorophyll, and sunlight to synthesize carbohydrates.",
        "explanation_hi": "स्वपोषी पोषण (प्रकाश संश्लेषण) को कार्बोहाइड्रेट संश्लेषित करने के लिए CO2, H2O, क्लोरोफिल और सूर्य के प्रकाश की आवश्यकता होती है।",
        "explanation_gu": "સ્વયંપોષી પોષણ (પ્રકાશસંશ્લેષણ) ને કાર્બોદિત બનાવવા માટે CO2, H2O, ક્લોરોફિલ અને સૂર્યપ્રકાશની જરૂર પડે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_015",
        "type": "mcq",
        "title": "NCERT Exercise Q4",
        "title_hi": "NCERT अभ्यास Q4",
        "title_gu": "NCERT સ્વાધ્યાય Q4",
        "question": "The breakdown of pyruvate to give carbon dioxide, water and energy takes place in:",
        "question_hi": "पाइरुवेट के विखंडन से कार्बन डाइऑक्साइड, जल तथा ऊर्जा देने का कार्य कहां होता है?",
        "question_gu": "પાયરુવેટના વિઘટનથી કાર્બન ડાયોક્સાઇડ, પાણી અને ઊર્જા ઉત્પન્ન થવાની ક્રિયા ક્યાં થાય છે?",
        "options": [
            "cytoplasm",
            "mitochondria",
            "chloroplast",
            "nucleus"
        ],
        "options_hi": [
            "कोशिकाद्रव्य",
            "माइटोकॉन्ड्रिया",
            "हरितलवक",
            "केंद्रक"
        ],
        "options_gu": [
            "કોષરસ",
            "કણભસૂત્ર (માઇટોકોન્ડ્રિયા)",
            "હરિતકણ",
            "કોષકેન્દ્ર"
        ],
        "correct_index": 1,
        "explanation": "Complete aerobic breakdown of pyruvate into CO2, H2O, and a large amount of energy occurs in the mitochondria.",
        "explanation_hi": "माइटोकॉन्ड्रिया में पाइरुवेट का CO2, H2O और बड़ी मात्रा में ऊर्जा में पूर्ण वायवीय विखंडन होता है।",
        "explanation_gu": "કણભસૂત્રમાં પાયરુવેટનું CO2, H2O અને મોટી માત્રામાં ઊર્જામાં સંપૂર્ણ જારક વિઘટન થાય છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_016",
        "type": "mcq",
        "title": "NCERT Exercise Q5",
        "title_hi": "NCERT अभ्यास Q5",
        "title_gu": "NCERT સ્વાધ્યાય Q5",
        "question": "How are fats digested in our bodies? Where does this process take place?",
        "question_hi": "हमारे शरीर में वसा का पाचन कैसे होता है? यह प्रक्रम कहाँ होता है?",
        "question_gu": "આપણા શરીરમાં ચરબીનું પાચન કેવી રીતે થાય છે? આ પ્રક્રિયા ક્યાં થાય છે?",
        "options": [
            "In the stomach by pepsin enzyme.",
            "In the small intestine; bile salts emulsify large fat globules, and pancreatic lipase breaks them down into fatty acids and glycerol.",
            "In the large intestine by the action of water.",
            "In the mouth by salivary amylase."
        ],
        "options_hi": [
            "आमाशय में पेप्सिन एंजाइम द्वारा।",
            "छोटी आंत में; पित्त लवण बड़ी वसा गोलिकाओं को इमल्सीकृत करते हैं, और अग्नाशयी लाइपेज उन्हें फैटी एसिड और ग्लिसरॉल में तोड़ देता है।",
            "पानी की क्रिया द्वारा बड़ी आंत में।",
            "लार एमाइलेज द्वारा मुंह में।"
        ],
        "options_gu": [
            "જઠરમાં પેપ્સિન ઉત્સેચક દ્વારા.",
            "નાના આંતરડામાં; પિત્તક્ષારો ચરબીના મોટા ગોલકોનું તૈલોદકીકરણ કરે છે, અને સ્વાદુરસનો લાઇપેઝ તેને ફેટી એસિડ અને ગ્લિસરોલમાં વિઘટિત કરે છે.",
            "પાણીની ક્રિયા દ્વારા મોટા આંતરડામાં.",
            "લાળ એમાયલેઝ દ્વારા મોંમાં."
        ],
        "correct_index": 1,
        "explanation": "Fat is digested in the small intestine. Bile from the liver emulsifies large fat globules into smaller ones. Then, the enzyme lipase (from pancreatic juice) breaks them into fatty acids and glycerol.",
        "explanation_hi": "वसा का पाचन छोटी आंत में होता है। यकृत का पित्त बड़ी वसा गोलिकाओं को छोटी गोलिकाओं में इमल्सीकृत करता है। फिर, लाइपेज एंजाइम उन्हें फैटी एसिड और ग्लिसरॉल में तोड़ देता है।",
        "explanation_gu": "ચરબીનું પાચન નાના આંતરડામાં થાય છે. યકૃતનું પિત્ત ચરબીના મોટા ગોલકોને નાના ગોલકોમાં ફેરવે છે. પછી, લાઇપેઝ ઉત્સેચક તેમને ફેટી એસિડ અને ગ્લિસરોલમાં તોડે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_017",
        "type": "mcq",
        "title": "NCERT Exercise Q6",
        "title_hi": "NCERT अभ्यास Q6",
        "title_gu": "NCERT સ્વાધ્યાય Q6",
        "question": "What is the role of saliva in the digestion of food?",
        "question_hi": "भोजन के पाचन में लार की क्या भूमिका है?",
        "question_gu": "ખોરાકના પાચનમાં લાળની ભૂમિકા શું છે?",
        "options": [
            "It breaks down proteins into amino acids.",
            "It contains salivary amylase which breaks down complex starch into simple sugar. It also wets the food.",
            "It produces hydrochloric acid to kill bacteria.",
            "It absorbs excess water from the food."
        ],
        "options_hi": [
            "यह प्रोटीन को अमीनो एसिड में तोड़ता है।",
            "इसमें लार एमाइलेज होता है जो जटिल स्टार्च को सरल शर्करा में तोड़ता है। यह भोजन को गीला भी करता है।",
            "यह बैक्टीरिया को मारने के लिए हाइड्रोक्लोरिक एसिड पैदा करता है।",
            "यह भोजन से अतिरिक्त पानी को अवशोषित करता है।"
        ],
        "options_gu": [
            "તે પ્રોટીનને એમિનો એસિડમાં તોડે છે.",
            "તેમાં લાળ એમાયલેઝ હોય છે જે જટિલ સ્ટાર્ચને સરળ શર્કરામાં તોડે છે. તે ખોરાકને ભીનો પણ કરે છે.",
            "તે બેક્ટેરિયાને મારવા માટે હાઇડ્રોક્લોરિક એસિડ ઉત્પન્ન કરે છે.",
            "તે ખોરાકમાંથી વધારાનું પાણી શોષી લે છે."
        ],
        "correct_index": 1,
        "explanation": "Saliva contains an enzyme called salivary amylase that breaks down starch into simple sugar. It also lubricates the food for easy swallowing.",
        "explanation_hi": "लार में लार एमाइलेज नामक एंजाइम होता है जो स्टार्च को सरल शर्करा में तोड़ता है। यह निगलने में आसानी के लिए भोजन को चिकना भी करता है।",
        "explanation_gu": "લાળમાં લાળ એમાયલેઝ નામનો ઉત્સેચક હોય છે જે સ્ટાર્ચને સરળ શર્કરામાં તોડે છે. ગળવામાં સરળતા માટે તે ખોરાકને પોચો અને ચીકણો બનાવે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_018",
        "type": "mcq",
        "title": "NCERT Exercise Q7",
        "title_hi": "NCERT अभ्यास Q7",
        "title_gu": "NCERT સ્વાધ્યાય Q7",
        "question": "What are the necessary conditions for autotrophic nutrition and what are its byproducts?",
        "question_hi": "स्वपोषी पोषण के लिए आवश्यक परिस्थितियां कौन सी हैं और इसके उपोत्पाद क्या हैं?",
        "question_gu": "સ્વયંપોષી પોષણ માટે જરૂરી શરતો કઈ છે અને તેની આડપેદાશો કઈ છે?",
        "options": [
            "Conditions: Oxygen and water; Byproducts: Carbon dioxide and glucose.",
            "Conditions: Carbon dioxide, water, chlorophyll, and sunlight; Byproducts: Oxygen and water.",
            "Conditions: Nitrogen and sunlight; Byproducts: Amino acids.",
            "Conditions: Only sunlight; Byproducts: Energy."
        ],
        "options_hi": [
            "स्थितियां: ऑक्सीजन और पानी; उपोत्पाद: कार्बन डाइऑक्साइड और ग्लूकोज।",
            "स्थितियां: कार्बन डाइऑक्साइड, पानी, क्लोरोफिल और धूप; उपोत्पाद: ऑक्सीजन और पानी।",
            "स्थितियां: नाइट्रोजन और धूप; उपोत्पाद: अमीनो एसिड।",
            "स्थितियां: केवल धूप; उपोत्पाद: ऊर्जा।"
        ],
        "options_gu": [
            "શરતો: ઓક્સિજન અને પાણી; આડપેદાશો: કાર્બન ડાયોક્સાઇડ અને ગ્લુકોઝ.",
            "શરતો: કાર્બન ડાયોક્સાઇડ, પાણી, ક્લોરોફિલ અને સૂર્યપ્રકાશ; આડપેદાશો: ઓક્સિજન અને પાણી.",
            "શરતો: નાઇટ્રોજન અને સૂર્યપ્રકાશ; આડપેદાશો: એમિનો એસિડ.",
            "શરતો: માત્ર સૂર્યપ્રકાશ; આડપેદાશો: ઊર્જા."
        ],
        "correct_index": 1,
        "explanation": "Photosynthesis requires CO2, H2O, sunlight, and chlorophyll. Oxygen gas is released as the main byproduct along with water.",
        "explanation_hi": "प्रकाश संश्लेषण के लिए CO2, H2O, धूप और क्लोरोफिल की आवश्यकता होती है। पानी के साथ मुख्य उपोत्पाद के रूप में ऑक्सीजन गैस निकलती है।",
        "explanation_gu": "પ્રકાશસંશ્લેષણ માટે CO2, H2O, સૂર્યપ્રકાશ અને ક્લોરોફિલની જરૂર છે. ઓક્સિજન વાયુ પાણી સાથે મુખ્ય આડપેદાશ તરીકે મુક્ત થાય છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_019",
        "type": "mcq",
        "title": "NCERT Exercise Q8",
        "title_hi": "NCERT अभ्यास Q8",
        "title_gu": "NCERT સ્વાધ્યાય Q8",
        "question": "What are the differences between aerobic and anaerobic respiration?",
        "question_hi": "वायवीय और अवायवीय श्वसन के बीच क्या अंतर हैं?",
        "question_gu": "જારક અને અજારક શ્વસન વચ્ચે શું તફાવત છે?",
        "options": [
            "Aerobic needs oxygen and produces 38 ATP; Anaerobic does not need oxygen and produces 2 ATP.",
            "Aerobic occurs in absence of oxygen; Anaerobic needs oxygen.",
            "Aerobic produces lactic acid; Anaerobic produces carbon dioxide and water.",
            "There is no difference in energy production between the two."
        ],
        "options_hi": [
            "वायवीय को ऑक्सीजन की आवश्यकता होती है और 38 एटीपी पैदा करता है; अवायवीय को ऑक्सीजन की आवश्यकता नहीं होती है और 2 एटीपी पैदा करता है।",
            "वायवीय ऑक्सीजन की अनुपस्थिति में होता है; अवायवीय को ऑक्सीजन की आवश्यकता होती है।",
            "वायवीय लैक्टिक एसिड पैदा करता है; अवायवीय कार्बन डाइऑक्साइड और पानी पैदा करता है।",
            "दोनों के बीच ऊर्जा उत्पादन में कोई अंतर नहीं है।"
        ],
        "options_gu": [
            "જારક શ્વસનમાં ઓક્સિજનની જરૂર હોય છે અને 38 ATP ઉત્પન્ન કરે છે; અજારક શ્વસનમાં ઓક્સિજનની જરૂર નથી અને 2 ATP ઉત્પન્ન કરે છે.",
            "જારક ઓક્સિજનની ગેરહાજરીમાં થાય છે; અજારકને ઓક્સિજનની જરૂર છે.",
            "જારક લેક્ટિક એસિડ બનાવે છે; અજારક કાર્બન ડાયોક્સાઇડ અને પાણી બનાવે છે.",
            "બંને વચ્ચે ઊર્જા ઉત્પાદનમાં કોઈ તફાવત નથી."
        ],
        "correct_index": 0,
        "explanation": "Aerobic respiration requires oxygen, completely breaks down glucose, and generates a large amount of energy (38 ATP). Anaerobic respiration happens without oxygen and generates less energy (2 ATP).",
        "explanation_hi": "वायवीय श्वसन के लिए ऑक्सीजन की आवश्यकता होती है, ग्लूकोज को पूरी तरह से तोड़ देता है, और बड़ी मात्रा में ऊर्जा (38 एटीपी) उत्पन्न करता है। अवायवीय श्वसन ऑक्सीजन के बिना होता है और कम ऊर्जा (2 एटीपी) उत्पन्न करता है।",
        "explanation_gu": "જારક શ્વસનને ઓક્સિજનની જરૂર પડે છે, તે ગ્લુકોઝનું સંપૂર્ણ વિઘટન કરે છે અને મોટી માત્રામાં ઊર્જા (38 ATP) ઉત્પન્ન કરે છે. અજારક શ્વસન ઓક્સિજન વિના થાય છે અને ઓછી ઊર્જા (2 ATP) ઉત્પન્ન કરે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_020",
        "type": "mcq",
        "title": "NCERT Exercise Q9",
        "title_hi": "NCERT अभ्यास Q9",
        "title_gu": "NCERT સ્વાધ્યાય Q9",
        "question": "How are the alveoli designed to maximise the exchange of gases?",
        "question_hi": "गैसों के अधिकतम विनिमय के लिए कूपिकाएं (alveoli) किस प्रकार अभिकल्पित हैं?",
        "question_gu": "વાયુઓની મહત્તમ આપ-લે માટે વાયુકોષ્ઠોની રચના કેવી રીતે થયેલી છે?",
        "options": [
            "They have thick walls to prevent gas leakage.",
            "They form a balloon-like structure with very thin walls and an extensive network of blood vessels to provide a massive surface area.",
            "They contain chlorophyll to produce oxygen directly.",
            "They are large hollow tubes like the trachea."
        ],
        "options_hi": [
            "गैस रिसाव को रोकने के लिए उनकी दीवारें मोटी होती हैं।",
            "वे बहुत पतली दीवारों और रक्त वाहिकाओं के व्यापक नेटवर्क के साथ एक गुब्बारे जैसी संरचना बनाते हैं जो एक विशाल सतह क्षेत्र प्रदान करता है।",
            "सीधे ऑक्सीजन उत्पन्न करने के लिए उनमें क्लोरोफिल होता है।",
            "वे श्वासनली जैसी बड़ी खोखली नलियां हैं।"
        ],
        "options_gu": [
            "વાયુ લિકેજ અટકાવવા માટે તેમની દિવાલો જાડી હોય છે.",
            "તેઓ ખૂબ જ પાતળી દિવાલો અને રુધિરવાહિનીઓની વ્યાપક જાળ ધરાવતી ફુગ્ગા જેવી રચના ધરાવે છે જે વાયુવિનિમય માટે વિશાળ સપાટી પૂરી પાડે છે.",
            "સીધો ઓક્સિજન ઉત્પન્ન કરવા માટે તેમાં ક્લોરોફિલ હોય છે.",
            "તેઓ શ્વાસનળી જેવી મોટી પોલી નળીઓ છે."
        ],
        "correct_index": 1,
        "explanation": "Alveoli are tiny balloon-like structures in the lungs. They have extremely thin walls supplied with an extensive network of capillaries, providing a massive surface area for rapid gas exchange.",
        "explanation_hi": "कूपिकाएं फेफड़ों में गुब्बारे जैसी छोटी संरचनाएं हैं। उनकी दीवारें बेहद पतली होती हैं और उनमें केशिकाओं का एक व्यापक नेटवर्क होता है, जो तेजी से गैस विनिमय के लिए एक विशाल सतह क्षेत्र प्रदान करता है।",
        "explanation_gu": "વાયુકોષ્ઠો ફેફસામાં ફુગ્ગા જેવી નાની રચનાઓ છે. તેમની દિવાલો અત્યંત પાતળી હોય છે અને રુધિરકેશિકાઓની જાળ ધરાવે છે, જે વાયુઓની ઝડપી આપ-લે માટે વિશાળ સપાટી પૂરી પાડે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_021",
        "type": "mcq",
        "title": "NCERT Exercise Q10",
        "title_hi": "NCERT अभ्यास Q10",
        "title_gu": "NCERT સ્વાધ્યાય Q10",
        "question": "What would be the consequences of a deficiency of haemoglobin in our bodies?",
        "question_hi": "हमारे शरीर में हीमोग्लोबिन की कमी के क्या परिणाम होंगे?",
        "question_gu": "આપણા શરીરમાં હિમોગ્લોબિનની ઉણપના પરિણામો શું આવી શકે?",
        "options": [
            "Our blood will clot faster.",
            "Oxygen supply to body cells will be reduced, leading to fatigue, weakness, and a disease called anaemia.",
            "Our body will produce excess carbon dioxide.",
            "The heart will beat slower."
        ],
        "options_hi": [
            "हमारे खून का थक्का जल्दी जमेगा।",
            "शरीर की कोशिकाओं को ऑक्सीजन की आपूर्ति कम हो जाएगी, जिससे थकान, कमजोरी और एनीमिया नामक बीमारी हो जाएगी।",
            "हमारा शरीर अतिरिक्त कार्बन डाइऑक्साइड का उत्पादन करेगा।",
            "दिल की धड़कन धीमी हो जाएगी।"
        ],
        "options_gu": [
            "આપણું લોહી ઝડપથી જામી જશે.",
            "શરીરના કોષોને ઓક્સિજનનો પુરવઠો ઘટશે, જેનાથી થાક, નબળાઈ અને એનીમિયા (પાંડુરોગ) નામની બીમારી થશે.",
            "આપણું શરીર વધારાનો કાર્બન ડાયોક્સાઇડ ઉત્પન્ન કરશે.",
            "હૃદયના ધબકારા ધીમા પડશે."
        ],
        "correct_index": 1,
        "explanation": "Haemoglobin is the respiratory pigment in RBCs that carries oxygen. Its deficiency leads to a lack of oxygen in cells (Anaemia), causing severe fatigue and lack of energy.",
        "explanation_hi": "हीमोग्लोबिन आरबीसी में श्वसन वर्णक है जो ऑक्सीजन ले जाता है। इसकी कमी से कोशिकाओं में ऑक्सीजन की कमी (एनीमिया) हो जाती है, जिससे गंभीर थकान और ऊर्जा की कमी होती है।",
        "explanation_gu": "હિમોગ્લોબિન RBC માં રહેલું શ્વસન રંજકદ્રવ્ય છે જે ઓક્સિજનનું વહન કરે છે. તેની ઉણપથી કોષોમાં ઓક્સિજનની અછત (એનીમિયા) થાય છે, જેનાથી ભારે થાક અને ઊર્જાનો અભાવ થાય છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_022",
        "type": "mcq",
        "title": "NCERT Exercise Q11",
        "title_hi": "NCERT अभ्यास Q11",
        "title_gu": "NCERT સ્વાધ્યાય Q11",
        "question": "Describe double circulation of blood in human beings. Why is it necessary?",
        "question_hi": "मनुष्य में दोहरे परिसंचरण का वर्णन कीजिए। यह क्यों आवश्यक है?",
        "question_gu": "મનુષ્યમાં બેવડા પરિવહનનું વર્ણન કરો. તે શા માટે જરૂરી છે?",
        "options": [
            "Blood passes through the heart twice (Pulmonary and Systemic circulation). It strictly separates oxygenated and deoxygenated blood, vital for high energy needs of warm-blooded animals.",
            "Blood flows backward twice a minute to clean the heart.",
            "The heart has two chambers that pump blood twice.",
            "Blood passes through the kidneys twice to become perfectly pure."
        ],
        "options_hi": [
            "रक्त हृदय से दो बार होकर गुजरता है (फुफ्फुसीय और दैहिक परिसंचरण)। यह ऑक्सीजनित और विऑक्सीजनित रक्त को पूरी तरह अलग रखता है, जो समतापी प्राणियों की उच्च ऊर्जा आवश्यकताओं के लिए महत्वपूर्ण है।",
            "हृदय को साफ करने के लिए रक्त एक मिनट में दो बार पीछे की ओर बहता है।",
            "हृदय में दो कक्ष होते हैं जो दो बार रक्त पंप करते हैं।",
            "पूरी तरह से शुद्ध होने के लिए रक्त गुर्दे से दो बार होकर गुजरता है।"
        ],
        "options_gu": [
            "રુધિર હૃદયમાંથી બે વાર પસાર થાય છે (ફુપ્ફુસ અને દૈહિક પરિવહન). તે ઓક્સિજનયુક્ત અને ઓક્સિજનરહિત રુધિરને સંપૂર્ણપણે અલગ રાખે છે, જે ઉષ્ણ રક્ત ધરાવતા પ્રાણીઓની ઊંચી ઊર્જા જરૂરિયાતો માટે મહત્વપૂર્ણ છે.",
            "હૃદયને સાફ કરવા માટે રુધિર એક મિનિટમાં બે વાર પાછું વહે છે.",
            "હૃદયમાં બે ખંડો છે જે બે વાર રુધિર પમ્પ કરે છે.",
            "સંપૂર્ણ શુદ્ધ થવા માટે રુધિર મૂત્રપિંડમાંથી બે વાર પસાર થાય છે."
        ],
        "correct_index": 0,
        "explanation": "In humans, blood goes to the lungs, returns to the heart (Pulmonary), and is then pumped to the rest of the body, returning again to the heart (Systemic). This is double circulation.",
        "explanation_hi": "मनुष्यों में, रक्त फेफड़ों में जाता है, हृदय (फुफ्फुसीय) में लौटता है, और फिर शरीर के बाकी हिस्सों में पंप किया जाता है, फिर से हृदय (दैहिक) में लौटता है। यह दोहरा परिसंचरण है।",
        "explanation_gu": "મનુષ્યમાં, રુધિર ફેફસામાં જાય છે, હૃદયમાં પાછું ફરે છે (ફુપ્ફુસ પરિવહન), અને પછી બાકીના શરીરમાં પમ્પ થાય છે, અને ફરીથી હૃદયમાં પાછું ફરે છે (દૈહિક પરિવહન). આ બેવડું પરિવહન છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_023",
        "type": "mcq",
        "title": "NCERT Exercise Q12",
        "title_hi": "NCERT अभ्यास Q12",
        "title_gu": "NCERT સ્વાધ્યાય Q12",
        "question": "What are the differences between the transport of materials in xylem and phloem?",
        "question_hi": "जाइलम तथा फ्लोएम में पदार्थों के वहन में क्या अंतर हैं?",
        "question_gu": "જલવાહક અને અન્નવાહકમાં દ્રવ્યોના વહન વચ્ચે શું તફાવત છે?",
        "options": [
            "Xylem transports food bidirectionally using ATP; Phloem transports water upward passively.",
            "Xylem transports water and minerals upwards using transpiration pull; Phloem transports food bidirectionally using ATP.",
            "Both xylem and phloem transport water and food together.",
            "Xylem has living cells, while phloem is completely dead tissue."
        ],
        "options_hi": [
            "जाइलम एटीपी का उपयोग करके द्विदिश रूप से भोजन का परिवहन करता है; फ्लोएम निष्क्रिय रूप से पानी को ऊपर की ओर ले जाता है।",
            "जाइलम वाष्पोत्सर्जन खिंचाव का उपयोग करके पानी और खनिजों को ऊपर की ओर ले जाता है; फ्लोएम एटीपी का उपयोग करके द्विदिश रूप से भोजन का परिवहन करता है।",
            "जाइलम और फ्लोएम दोनों पानी और भोजन को एक साथ ले जाते हैं।",
            "जाइलम में जीवित कोशिकाएं होती हैं, जबकि फ्लोएम पूरी तरह से मृत ऊतक है।"
        ],
        "options_gu": [
            "જલવાહક એટીપીનો ઉપયોગ કરીને બંને દિશામાં ખોરાકનું વહન કરે છે; અન્નવાહક પાણીને ઉપર લઈ જાય છે.",
            "જલવાહક બાષ્પોત્સર્જન ખેંચાણનો ઉપયોગ કરીને પાણી અને ખનિજોને ઉપરની તરફ લઈ જાય છે; અન્નવાહક ATP નો ઉપયોગ કરીને બંને દિશામાં ખોરાકનું વહન કરે છે.",
            "જલવાહક અને અન્નવાહક બંને એકસાથે પાણી અને ખોરાકનું વહન કરે છે.",
            "જલવાહકમાં જીવંત કોષો હોય છે, જ્યારે અન્નવાહક સંપૂર્ણપણે મૃત પેશી છે."
        ],
        "correct_index": 1,
        "explanation": "Xylem transport is unidirectional (upward) for water, driven by physical forces. Phloem translocation is bidirectional for food, driven by biological metabolic energy (ATP).",
        "explanation_hi": "जाइलम वहन पानी के लिए एकदिशीय (ऊपर की ओर) होता है, जो भौतिक बलों द्वारा संचालित होता है। फ्लोएम स्थानांतरण भोजन के लिए द्विदिशीय है, जो जैविक चयापचय ऊर्जा (ATP) द्वारा संचालित होता है।",
        "explanation_gu": "પાણી માટે જલવાહક વહન એકદિશીય (ઉપરની તરફ) હોય છે, જે ભૌતિક બળો દ્વારા સંચાલિત થાય છે. ખોરાક માટે અન્નવાહક સ્થાનાંતરણ દ્વિ-દિશીય હોય છે, જે જૈવિક ઊર્જા (ATP) દ્વારા સંચાલિત થાય છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH5_024",
        "type": "mcq",
        "title": "NCERT Exercise Q13",
        "title_hi": "NCERT अभ्यास Q13",
        "title_gu": "NCERT સ્વાધ્યાય Q13",
        "question": "Compare the functioning of alveoli in the lungs and nephrons in the kidneys.",
        "question_hi": "फुफ्फुस में कूपिकाओं की तथा वृक्क में वृक्काणु (नेफ्रॉन) की रचना तथा क्रियाविधि की तुलना कीजिए।",
        "question_gu": "ફેફસામાં વાયુકોષ્ઠોની અને મૂત્રપિંડમાં ઉત્સર્ગએકમ (નેફ્રોન) ની રચના અને કાર્યકારી સરખામણી કરો.",
        "options": [
            "Alveoli filter blood to produce urine; Nephrons exchange oxygen and carbon dioxide.",
            "Alveoli exchange respiratory gases (O2 in, CO2 out); Nephrons filter blood to remove nitrogenous waste (urea, uric acid).",
            "Both are meant only for reabsorbing water back into the body.",
            "Alveoli are found in the heart, while nephrons are found in the stomach."
        ],
        "options_hi": [
            "कूपिकाएं मूत्र बनाने के लिए रक्त को छानती हैं; नेफ्रॉन ऑक्सीजन और कार्बन डाइऑक्साइड का विनिमय करते हैं।",
            "कूपिकाएं श्वसन गैसों (O2 अंदर, CO2 बाहर) का विनिमय करती हैं; नेफ्रॉन नाइट्रोजनयुक्त अपशिष्ट (यूरिया, यूरिक एसिड) को हटाने के लिए रक्त को छानते हैं।",
            "दोनों का उद्देश्य केवल पानी को शरीर में वापस अवशोषित करना है।",
            "कूपिकाएं हृदय में पाई जाती हैं, जबकि नेफ्रॉन आमाशय में पाए जाते हैं।"
        ],
        "options_gu": [
            "વાયુકોષ્ઠો મૂત્ર બનાવવા માટે લોહીને ગાળે છે; નેફ્રોન ઓક્સિજન અને કાર્બન ડાયોક્સાઇડની આપ-લે કરે છે.",
            "વાયુકોષ્ઠો શ્વસન વાયુઓની (O2 અંદર, CO2 બહાર) આપ-લે કરે છે; ઉત્સર્ગએકમ નાઇટ્રોજનયુક્ત કચરો (યુરિયા, યુરિક એસિડ) દૂર કરવા લોહીને ગાળે છે.",
            "બંનેનો હેતુ માત્ર શરીરમાં પાણીનું પુનઃશોષણ કરવાનો છે.",
            "વાયુકોષ્ઠો હૃદયમાં જોવા મળે છે, જ્યારે નેફ્રોન જઠરમાં જોવા મળે છે."
        ],
        "correct_index": 1,
        "explanation": "Alveoli act as the functional unit of lungs for gas exchange, whereas Nephrons act as the functional unit of kidneys for blood filtration and urine formation.",
        "explanation_hi": "कूपिकाएं गैस विनिमय के लिए फेफड़ों की कार्यात्मक इकाई के रूप में कार्य करती हैं, जबकि नेफ्रॉन रक्त निस्पंदन और मूत्र निर्माण के लिए गुर्दे की कार्यात्मक इकाई के रूप में कार्य करते हैं।",
        "explanation_gu": "વાયુકોષ્ઠો વાયુઓની આપ-લે માટે ફેફસાના કાર્યાત્મક એકમ તરીકે વર્તે છે, જ્યારે ઉત્સર્ગએકમ (નેફ્રોન) લોહીના ગાળણ અને મૂત્ર નિર્માણ માટે મૂત્રપિંડના કાર્યાત્મક એકમ તરીકે કામ કરે છે."
    }
]

blocks.extend(ncert_questions)

data = {
    "metadata": {
        "id": "ncert_class10_science_ch5",
        "title": "Chapter 5: Life Processes",
        "subject": "Science",
        "grade": "10"
    },
    "blocks": blocks
}

output_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch5.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {len(blocks)} blocks to {output_path}")
