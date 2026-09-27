import json

file_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class7_social_science_ch16.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# ID starts from 9
start_id = 9

def get_id():
    global start_id
    id_str = f"KOBJ_GSEB_CLASS7_SOCIAL_SCIENCE_CH16_{start_id:02d}"
    start_id += 1
    return id_str

new_blocks = [
    {
        "id": get_id(),
        "type": "mcq",
        "question": "The number of members in the Gujarat Legislative Assembly is ........ ;",
        "question_hi": "गुजरात विधानसभा में सदस्यों की संख्या ........ है।",
        "question_gu": "ગુજરાત વિધાનસભામાં સભ્યોની સંખ્યા ........ છે.",
        "options": ["182", "160", "200", "150"],
        "options_hi": ["182", "160", "200", "150"],
        "options_gu": ["182", "160", "200", "150"],
        "correct_index": 0,
        "hint": "Think about the total number of assembly seats in Gujarat.",
        "hint_hi": "गुजरात में विधानसभा सीटों की कुल संख्या के बारे में सोचें।",
        "hint_gu": "ગુજરાતમાં વિધાનસભા બેઠકોની કુલ સંખ્યા વિશે વિચારો."
    },
    {
        "id": get_id(),
        "type": "mcq",
        "question": "The upper house of the State Legislature is called ........ .",
        "question_hi": "राज्य विधानमंडल के उच्च सदन को ........ कहा जाता है।",
        "question_gu": "રાજ્ય વિધાનસભાના ઉપલા ગૃહને ........ કહેવામાં આવે છે.",
        "options": ["Legislative Council", "Legislative Assembly", "Rajya Sabha", "Lok Sabha"],
        "options_hi": ["विधान परिषद", "विधानसभा", "राज्यसभा", "लोकसभा"],
        "options_gu": ["વિધાન પરિષદ", "વિધાનસભા", "રાજ્યસભા", "લોકસભા"],
        "correct_index": 0,
        "hint": "It is not present in all states, and Gujarat doesn't have one.",
        "hint_hi": "यह सभी राज्यों में मौजूद नहीं है, और गुजरात में यह नहीं है।",
        "hint_gu": "તે બધા રાજ્યોમાં હાજર નથી, અને ગુજરાતમાં તે નથી."
    },
    {
        "id": get_id(),
        "type": "mcq",
        "question": "The name of the Legislative Assembly building of Gujarat is ........ ;",
        "question_hi": "गुजरात के विधानसभा भवन का नाम ........ है।",
        "question_gu": "ગુજરાતના વિધાનસભા ભવનનું નામ ........ છે.",
        "options": ["Vitthalbhai Patel Vidhan Sabha Bhavan", "Sardar Patel Bhavan", "Mahatma Mandir", "Swarnim Sankul"],
        "options_hi": ["विट्ठलभाई पटेल विधानसभा भवन", "सरदार पटेल भवन", "महात्मा मंदिर", "स्वर्णिम संकुल"],
        "options_gu": ["વિઠ્ઠલભાઈ પટેલ વિધાનસભા ભવન", "સરદાર પટેલ ભવન", "મહાત્મા મંદિર", "સ્વર્ણિમ સંકુલ"],
        "correct_index": 0,
        "hint": "It is named after a prominent political leader from Gujarat.",
        "hint_hi": "इसका नाम गुजरात के एक प्रमुख राजनीतिक नेता के नाम पर रखा गया है।",
        "hint_gu": "તેનું નામ ગુજરાતના એક અગ્રણી રાજકીય નેતાના નામ પરથી રાખવામાં આવ્યું છે."
    },
    {
        "id": get_id(),
        "type": "mcq",
        "question": "Assembly elections are held every ........ years.",
        "question_hi": "विधानसभा चुनाव हर ........ साल में होते हैं।",
        "question_gu": "વિધાનસભાની ચૂંટણીઓ દર ........ વર્ષે યોજાય છે.",
        "options": ["5", "4", "6", "3"],
        "options_hi": ["5", "4", "6", "3"],
        "options_gu": ["5", "4", "6", "3"],
        "correct_index": 0,
        "hint": "The term of the Legislative Assembly is typically this many years.",
        "hint_hi": "विधानसभा का कार्यकाल आमतौर पर इतने वर्षों का होता है।",
        "hint_gu": "વિધાનસભાની મુદત સામાન્ય રીતે આટલા વર્ષોની હોય છે."
    },
    {
        "id": get_id(),
        "type": "mcq",
        "question": "There is a ........ scheme in Gujarat for the patient to get immediate service.",
        "question_hi": "मरीज़ों को तत्काल सेवा पाने के लिए गुजरात में ........ योजना है।",
        "question_gu": "દર્દીઓને તાત્કાલિક સેવા મેળવવા માટે ગુજરાતમાં ........ યોજના છે.",
        "options": ["108", "104", "100", "101"],
        "options_hi": ["108", "104", "100", "101"],
        "options_gu": ["108", "104", "100", "101"],
        "correct_index": 0,
        "hint": "It is a toll-free emergency medical service number.",
        "hint_hi": "यह एक टोल-फ्री आपातकालीन चिकित्सा सेवा नंबर है।",
        "hint_gu": "તે ટોલ-ફ્રી ઇમરજન્સી મેડિકલ સર્વિસ નંબર છે."
    },
    {
        "id": get_id(),
        "type": "mcq",
        "question": "State whether true or false: Mukhyamantri Amrutam (Ma) Yojana is run by the Central Government.",
        "question_hi": "बताएं कि क्या यह सच है या गलत: मुख्यमंत्री अमृतम (मा) योजना केंद्र सरकार द्वारा चलाई जाती है।",
        "question_gu": "સાચું કે ખોટું તે જણાવો: મુખ્યમંત્રી અમૃતમ (મા) યોજના કેન્દ્ર સરકાર દ્વારા ચલાવવામાં આવે છે.",
        "options": ["True", "False"],
        "options_hi": ["सत्य", "असत्य"],
        "options_gu": ["સાચું", "ખોટું"],
        "correct_index": 1,
        "hint": "Look at the name 'Mukhyamantri' (Chief Minister), which indicates state level.",
        "hint_hi": "नाम 'मुख्यमंत्री' देखें, जो राज्य स्तर को दर्शाता है।",
        "hint_gu": "નામ 'મુખ્યમંત્રી' જુઓ, જે રાજ્ય સ્તર દર્શાવે છે."
    },
    {
        "id": get_id(),
        "type": "mcq",
        "question": "State whether true or false: The state of Delhi is a National Capital Region (NCR).",
        "question_hi": "बताएं कि क्या यह सच है या गलत: दिल्ली राज्य एक राष्ट्रीय राजधानी क्षेत्र (NCR) है।",
        "question_gu": "સાચું કે ખોટું તે જણાવો: દિલ્હી રાજ્ય એક રાષ્ટ્રીય રાજધાની ક્ષેત્ર (NCR) છે.",
        "options": ["True", "False"],
        "options_hi": ["सत्य", "असत्य"],
        "options_gu": ["સાચું", "ખોટું"],
        "correct_index": 0,
        "hint": "Delhi is indeed a special state and forms the NCR.",
        "hint_hi": "दिल्ली वास्तव में एक विशेष राज्य है और NCR का हिस्सा है।",
        "hint_gu": "દિલ્હી ખરેખર એક વિશેષ રાજ્ય છે અને NCR ની રચના કરે છે."
    },
    {
        "id": get_id(),
        "type": "mcq",
        "question": "State whether true or false: The Legislative Assembly is also called the lower house.",
        "question_hi": "बताएं कि क्या यह सच है या गलत: विधानसभा को निचला सदन भी कहा जाता है।",
        "question_gu": "સાચું કે ખોટું તે જણાવો: વિધાનસભાને નીચલું ગૃહ પણ કહેવામાં આવે છે.",
        "options": ["True", "False"],
        "options_hi": ["सत्य", "असत्य"],
        "options_gu": ["સાચું", "ખોટું"],
        "correct_index": 0,
        "hint": "The Legislative Council is the upper house.",
        "hint_hi": "विधान परिषद उच्च सदन है।",
        "hint_gu": "વિધાન પરિષદ ઉપલું ગૃહ છે."
    },
    {
        "id": get_id(),
        "type": "mcq",
        "question": "State whether true or false: Uttar Pradesh has a Legislative Council.",
        "question_hi": "बताएं कि क्या यह सच है या गलत: उत्तर प्रदेश में विधान परिषद है।",
        "question_gu": "સાચું કે ખોટું તે જણાવો: ઉત્તર પ્રદેશમાં વિધાન પરિષદ છે.",
        "options": ["True", "False"],
        "options_hi": ["सत्य", "असत्य"],
        "options_gu": ["સાચું", "ખોટું"],
        "correct_index": 0,
        "hint": "UP is one of the few states in India with a bicameral legislature.",
        "hint_hi": "यूपी भारत के उन कुछ राज्यों में से एक है जहां द्विसदनीय विधायिका है।",
        "hint_gu": "યુપી ભારતના એવા થોડા રાજ્યોમાંનું એક છે જ્યાં દ્વિગૃહી ધારાસભા છે."
    },
    {
        "id": get_id(),
        "type": "mcq",
        "question": "State whether true or false: The Legislative Assembly is a permanent house.",
        "question_hi": "बताएं कि क्या यह सच है या गलत: विधानसभा एक स्थायी सदन है।",
        "question_gu": "સાચું કે ખોટું તે જણાવો: વિધાનસભા એ કાયમી ગૃહ છે.",
        "options": ["True", "False"],
        "options_hi": ["सत्य", "असत्य"],
        "options_gu": ["સાચું", "ખોટું"],
        "correct_index": 1,
        "hint": "It dissolves every 5 years for elections.",
        "hint_hi": "यह चुनावों के लिए हर 5 साल में भंग हो जाता है।",
        "hint_gu": "તે ચૂંટણીઓ માટે દર 5 વર્ષે વિસર્જન થાય છે."
    },
    {
        "id": get_id(),
        "type": "flashcard",
        "front": "When does the bill become an act?",
        "front_hi": "विधेयक अधिनियम कब बन जाता है?",
        "front_gu": "બિલ કાયદો ક્યારે બને છે?",
        "back": "A bill becomes an act after passing through various stages in the Legislative Assembly and getting the approval (signature) of the Governor.",
        "back_hi": "विधानसभा में विभिन्न चरणों से गुजरने और राज्यपाल की स्वीकृति (हस्ताक्षर) प्राप्त करने के बाद एक विधेयक अधिनियम बन जाता है।",
        "back_gu": "વિધાનસભામાં વિવિધ તબક્કાઓમાંથી પસાર થયા પછી અને રાજ્યપાલની મંજૂરી (સહી) મેળવ્યા પછી બિલ કાયદો બને છે."
    },
    {
        "id": get_id(),
        "type": "flashcard",
        "front": "Mention the organs of the state government.",
        "front_hi": "राज्य सरकार के अंगों का उल्लेख करें।",
        "front_gu": "રાજ્ય સરકારના અંગોનો ઉલ્લેખ કરો.",
        "back": "The three main organs of the state government are the Legislature, the Executive, and the Judiciary.",
        "back_hi": "राज्य सरकार के तीन मुख्य अंग विधायिका, कार्यपालिका और न्यायपालिका हैं।",
        "back_gu": "રાજ્ય સરકારના ત્રણ મુખ્ય અંગો ધારાસભા, કારોબારી અને ન્યાયતંત્ર છે."
    },
    {
        "id": get_id(),
        "type": "flashcard",
        "front": "Who appoints the Chief Minister?",
        "front_hi": "मुख्यमंत्री की नियुक्ति कौन करता है?",
        "front_gu": "મુખ્યમંત્રીની નિમણૂક કોણ કરે છે?",
        "back": "The Governor appoints the leader of the party having a majority in the state legislature as the Chief Minister.",
        "back_hi": "राज्यपाल राज्य विधानमंडल में बहुमत वाले दल के नेता को मुख्यमंत्री नियुक्त करते हैं।",
        "back_gu": "રાજ્યપાલ રાજ્ય વિધાનસભામાં બહુમતી ધરાવતા પક્ષના નેતાની મુખ્યમંત્રી તરીકે નિમણૂક કરે છે."
    },
    {
        "id": get_id(),
        "type": "flashcard",
        "front": "Through whom are questions asked in the assembly?",
        "front_hi": "विधानसभा में किसके माध्यम से प्रश्न पूछे जाते हैं?",
        "front_gu": "વિધાનસભામાં કોના દ્વારા પ્રશ્નો પૂછવામાં આવે છે?",
        "back": "Legislators ask questions to ministers or the Chief Minister through the Speaker of the Legislative Assembly.",
        "back_hi": "विधायक विधानसभा के अध्यक्ष (स्पीकर) के माध्यम से मंत्रियों या मुख्यमंत्री से प्रश्न पूछते हैं।",
        "back_gu": "ધારાસભ્યો વિધાનસભાના અધ્યક્ષ (સ્પીકર) દ્વારા મંત્રીઓ અથવા મુખ્યમંત્રીને પ્રશ્નો પૂછે છે."
    },
    {
        "id": get_id(),
        "type": "flashcard",
        "front": "Who takes care of the state when there is Presidential Rule in the state?",
        "front_hi": "जब राज्य में राष्ट्रपति शासन होता है तो राज्य की देखभाल कौन करता है?",
        "front_gu": "જ્યારે રાજ્યમાં રાષ્ટ્રપતિ શાસન હોય ત્યારે રાજ્યની સંભાળ કોણ રાખે છે?",
        "back": "When there is Presidential Rule in the state, the Governor takes care of the state administration on behalf of the President.",
        "back_hi": "जब राज्य में राष्ट्रपति शासन होता है, तो राज्यपाल राष्ट्रपति की ओर से राज्य प्रशासन की देखभाल करते हैं।",
        "back_gu": "જ્યારે રાજ્યમાં રાષ્ટ્રપતિ શાસન હોય છે, ત્યારે રાજ્યપાલ રાષ્ટ્રપતિ વતી રાજ્યના વહીવટની સંભાળ રાખે છે."
    },
    {
        "id": get_id(),
        "type": "flashcard",
        "front": "Write a short note on: Functions of the Governor",
        "front_hi": "संक्षिप्त टिप्पणी लिखें: राज्यपाल के कार्य",
        "front_gu": "ટૂંક નોંધ લખો: રાજ્યપાલના કાર્યો",
        "back": "1. Appoints the Chief Minister and cabinet ministers.\n2. Convenes or dissolves the Legislative Assembly.\n3. Makes law by signing bills.\n4. Imposes an ordinance if needed.\n5. Takes care of administration neutrally.",
        "back_hi": "1. मुख्यमंत्री और कैबिनेट मंत्रियों की नियुक्ति करते हैं।\n2. विधानसभा बुलाते या भंग करते हैं।\n3. विधेयकों पर हस्ताक्षर करके कानून बनाते हैं।\n4. आवश्यकता पड़ने पर अध्यादेश लागू करते हैं।\n5. तटस्थ रूप से प्रशासन की देखभाल करते हैं।",
        "back_gu": "1. મુખ્યમંત્રી અને કેબિનેટ મંત્રીઓની નિમણૂક કરે છે.\n2. વિધાનસભા બોલાવે છે અથવા વિસર્જન કરે છે.\n3. બિલ પર સહી કરીને કાયદો બનાવે છે.\n4. જરૂર પડે તો વટહુકમ બહાર પાડે છે.\n5. તટસ્થ રીતે વહીવટની સંભાળ રાખે છે."
    },
    {
        "id": get_id(),
        "type": "flashcard",
        "front": "Write a short note on: Public Health Services",
        "front_hi": "संक्षिप्त टिप्पणी लिखें: सार्वजनिक स्वास्थ्य सेवाएं",
        "front_gu": "ટૂંક નોંધ લખો: જાહેર આરોગ્ય સેવાઓ",
        "back": "Public health services are provided by the government through PHCs, civil hospitals, and sub-centers. They run vaccination, family welfare, and environmental protection programs. 108 emergency service and generic medicine distribution help citizens maintain well-being.",
        "back_hi": "सार्वजनिक स्वास्थ्य सेवाएं सरकार द्वारा पीएचसी, सिविल अस्पताल और उप-केंद्रों के माध्यम से प्रदान की जाती हैं। वे टीकाकरण, परिवार कल्याण और पर्यावरण संरक्षण कार्यक्रम चलाते हैं। 108 आपातकालीन सेवा और जेनेरिक दवा वितरण नागरिकों को भलाई बनाए रखने में मदद करते हैं।",
        "back_gu": "સરકાર દ્વારા પીએચસી, સિવિલ હોસ્પિટલ અને પેટા-કેન્દ્રો દ્વારા જાહેર આરોગ્ય સેવાઓ પૂરી પાડવામાં આવે છે. તેઓ રસીકરણ, કુટુંબ કલ્યાણ અને પર્યાવરણ સંરક્ષણ કાર્યક્રમો ચલાવે છે. 108 ઇમરજન્સી સેવા અને જેનરિક દવા વિતરણ નાગરિકોને સુખાકારી જાળવવામાં મદદ કરે છે."
    },
    {
        "id": get_id(),
        "type": "flashcard",
        "front": "Write a short note on: Functions of the Chief-Minister",
        "front_hi": "संक्षिप्त टिप्पणी लिखें: मुख्यमंत्री के कार्य",
        "front_gu": "ટૂંક નોંધ લખો: મુખ્યમંત્રીના કાર્યો",
        "back": "1. Convenes cabinet meetings and assigns portfolios to ministers.\n2. Supervises and guides ministers.\n3. Informs the Governor about cabinet decisions.\n4. Continually works for the state's development and citizen's welfare.\n5. Serves as the captain of government policies.",
        "back_hi": "1. कैबिनेट की बैठकें बुलाते हैं और मंत्रियों को विभाग सौंपते हैं।\n2. मंत्रियों का पर्यवेक्षण और मार्गदर्शन करते हैं।\n3. कैबिनेट के फैसलों के बारे में राज्यपाल को सूचित करते हैं।\n4. राज्य के विकास और नागरिक कल्याण के लिए लगातार काम करते हैं।\n5. सरकारी नीतियों के कप्तान के रूप में कार्य करते हैं।",
        "back_gu": "1. કેબિનેટની બેઠકો બોલાવે છે અને મંત્રીઓને ખાતા સોંપે છે.\n2. મંત્રીઓનું નિરીક્ષણ અને માર્ગદર્શન કરે છે.\n3. કેબિનેટના નિર્ણયો વિશે રાજ્યપાલને જાણ કરે છે.\n4. રાજ્યના વિકાસ અને નાગરિકોના કલ્યાણ માટે સતત કામ કરે છે.\n5. સરકારી નીતિઓના કેપ્ટન તરીકે સેવા આપે છે."
    },
    {
        "id": get_id(),
        "type": "flashcard",
        "front": "Write a short note on: Formation of the Legislative Assembly",
        "front_hi": "संक्षिप्त टिप्पणी लिखें: विधानसभा का गठन",
        "front_gu": "ટૂંક નોંધ લખો: વિધાનસભાની રચના",
        "back": "The lower house of the state legislature is the Legislative Assembly. Members (MLAs) are elected directly by citizens every 5 years based on population constituencies. It has a minimum of 60 and maximum of 500 members. Gujarat has 182 seats.",
        "back_hi": "राज्य विधानमंडल का निचला सदन विधानसभा है। सदस्य (विधायक) हर 5 साल में जनसंख्या निर्वाचन क्षेत्रों के आधार पर सीधे नागरिकों द्वारा चुने जाते हैं। इसमें न्यूनतम 60 और अधिकतम 500 सदस्य होते हैं। गुजरात में 182 सीटें हैं।",
        "back_gu": "રાજ્ય વિધાનસભાનું નીચલું ગૃહ વિધાનસભા છે. સભ્યો (ધારાસભ્યો) દર 5 વર્ષે વસ્તી મતવિસ્તારોના આધારે સીધા નાગરિકો દ્વારા ચૂંટાય છે. તેમાં ઓછામાં ઓછા 60 અને વધુમાં વધુ 500 સભ્યો હોય છે. ગુજરાતમાં 182 બેઠકો છે."
    },
    {
        "id": get_id(),
        "type": "flashcard",
        "front": "Mention functions of the State Government.",
        "front_hi": "राज्य सरकार के कार्यों का उल्लेख करें।",
        "front_gu": "રાજ્ય સરકારના કાર્યોનો ઉલ્લેખ કરો.",
        "back": "The state government works for people's welfare by providing electricity, roads, clean water, health services, and education. It distributes food through ration shops, helps during natural calamities, and maintains peace and law & order.",
        "back_hi": "राज्य सरकार बिजली, सड़क, स्वच्छ पानी, स्वास्थ्य सेवा और शिक्षा प्रदान करके लोगों के कल्याण के लिए काम करती है। यह राशन की दुकानों के माध्यम से भोजन वितरित करता है, प्राकृतिक आपदाओं के दौरान मदद करता है, और शांति और कानून व्यवस्था बनाए रखता है।",
        "back_gu": "રાજ્ય સરકાર વીજળી, રસ્તાઓ, શુદ્ધ પાણી, આરોગ્ય સેવાઓ અને શિક્ષણ આપીને લોકોના કલ્યાણ માટે કામ કરે છે. તે રાશનની દુકાનો દ્વારા અનાજનું વિતરણ કરે છે, કુદરતી આફતો દરમિયાન મદદ કરે છે અને શાંતિ અને કાયદો અને વ્યવસ્થા જાળવી રાખે છે."
    },
    {
        "id": get_id(),
        "type": "flashcard",
        "front": "What functions does the State Government perform for the health of the citizens?",
        "front_hi": "राज्य सरकार नागरिकों के स्वास्थ्य के लिए कौन से कार्य करती है?",
        "front_gu": "રાજ્ય સરકાર નાગરિકોના આરોગ્ય માટે કયા કાર્યો કરે છે?",
        "back": "It plans and funds health schemes like Mukhyamantri Amrutam Yojana. It runs vaccination drives, generic medicine stores, controls food adulteration, and provides 108 emergency services and disease eradication programs (e.g., Malaria, Polio).",
        "back_hi": "यह मुख्यमंत्री अमृतम योजना जैसी स्वास्थ्य योजनाओं की योजना और वित्तपोषण करता है। यह टीकाकरण अभियान, जेनेरिक दवा स्टोर चलाता है, खाद्य मिलावट को नियंत्रित करता है, और 108 आपातकालीन सेवाएं और रोग उन्मूलन कार्यक्रम प्रदान करता है।",
        "back_gu": "તે મુખ્યમંત્રી અમૃતમ યોજના જેવી આરોગ્ય યોજનાઓનું આયોજન અને ભંડોળ પૂરું પાડે છે. તે રસીકરણ ઝુંબેશ, જેનરિક મેડિકલ સ્ટોર્સ ચલાવે છે, ખાદ્ય ભેળસેળને નિયંત્રિત કરે છે અને 108 ઇમરજન્સી સેવાઓ અને રોગ નાબૂદી કાર્યક્રમો પૂરા પાડે છે."
    },
    {
        "id": get_id(),
        "type": "flashcard",
        "front": "State the eligibility to become a member of the Legislative Assembly.",
        "front_hi": "विधानसभा का सदस्य बनने के लिए योग्यता बताएं।",
        "front_gu": "વિધાનસભાના સભ્ય બનવા માટેની લાયકાત જણાવો.",
        "back": "The person must be an Indian citizen, at least 25 years old. They must not hold a paid government position, and should not be a bankrupt, a convicted offender, or of an unstable mind.",
        "back_hi": "व्यक्ति एक भारतीय नागरिक होना चाहिए, कम से कम 25 वर्ष का होना चाहिए। उनके पास सरकारी पद नहीं होना चाहिए, और वे दिवालिया, दोषी अपराधी या अस्थिर दिमाग के नहीं होने चाहिए।",
        "back_gu": "વ્યક્તિ ભારતીય નાગરિક હોવો જોઈએ, ઓછામાં ઓછો 25 વર્ષનો હોવો જોઈએ. તેમની પાસે ચૂકવણીવાળી સરકારી નોકરી ન હોવી જોઈએ, અને તે નાદાર, દોષિત ગુનેગાર અથવા અસ્થિર મગજનો ન હોવો જોઈએ."
    },
    {
        "id": get_id(),
        "type": "flashcard",
        "front": "How is the State Executive formed?",
        "front_hi": "राज्य कार्यपालिका का गठन कैसे होता है?",
        "front_gu": "રાજ્ય કારોબારીની રચના કેવી રીતે થાય છે?",
        "back": "The State Executive consists of the Governor, the Chief Minister, and the Cabinet of Ministers (Political Executive), along with administrative officers (Administrative Executive). The Governor appoints the CM from the majority party, who forms the Cabinet.",
        "back_hi": "राज्य कार्यपालिका में राज्यपाल, मुख्यमंत्री और कैबिनेट मंत्री (राजनीतिक कार्यपालिका), और प्रशासनिक अधिकारी (प्रशासनिक कार्यपालिका) शामिल होते हैं। राज्यपाल बहुमत वाले दल से मुख्यमंत्री नियुक्त करते हैं, जो कैबिनेट बनाते हैं।",
        "back_gu": "રાજ્ય કારોબારીમાં રાજ્યપાલ, મુખ્યમંત્રી અને કેબિનેટ મંત્રીઓ (રાજકીય કારોબારી), વહીવટી અધિકારીઓ (વહીવટી કારોબારી) સાથે હોય છે. રાજ્યપાલ બહુમતીવાળા પક્ષમાંથી મુખ્યમંત્રીની નિમણૂક કરે છે, જે કેબિનેટની રચના કરે છે."
    },
    {
        "id": get_id(),
        "type": "flashcard",
        "front": "Write the duties of the State Executive.",
        "front_hi": "राज्य कार्यपालिका के कर्तव्य लिखिए।",
        "front_gu": "રાજ્ય કારોબારીની ફરજો લખો.",
        "back": "The State Executive enforces laws made by the Assembly, maintains law and order, works to remove poverty and unemployment, and provides basic services like health, education, transport, and electricity for people's welfare.",
        "back_hi": "राज्य कार्यपालिका विधानसभा द्वारा बनाए गए कानूनों को लागू करती है, कानून और व्यवस्था बनाए रखती है, गरीबी और बेरोजगारी को दूर करने के लिए काम करती है, और लोगों के कल्याण के लिए स्वास्थ्य, शिक्षा और बिजली जैसी बुनियादी सेवाएं प्रदान करती है।",
        "back_gu": "રાજ્ય કારોબારી વિધાનસભા દ્વારા બનાવેલા કાયદાઓનો અમલ કરે છે, કાયદો અને વ્યવસ્થા જાળવી રાખે છે, ગરીબી અને બેરોજગારી દૂર કરવા માટે કામ કરે છે અને લોકોના કલ્યાણ માટે આરોગ્ય, શિક્ષણ અને વીજળી જેવી મૂળભૂત સેવાઓ પૂરી પાડે છે."
    },
    {
        "id": get_id(),
        "type": "flashcard",
        "front": "The village Sarpanch wants to make a law for the development of the village. How will he make it?",
        "front_hi": "ग्राम सरपंच गांव के विकास के लिए कानून बनाना चाहते हैं। वह इसे कैसे बनाएंगे?",
        "front_gu": "ગામના સરપંચ ગામના વિકાસ માટે કાયદો બનાવવા માંગે છે. તે કેવી રીતે બનાવશે?",
        "back": "A Sarpanch operates at the local self-government level (Gram Panchayat) and can pass resolutions for village development with the Panchayat members. However, formal state laws are made only by the Legislative Assembly.",
        "back_hi": "एक सरपंच स्थानीय स्वशासन स्तर (ग्राम पंचायत) पर काम करता है और पंचायत सदस्यों के साथ गांव के विकास के लिए प्रस्ताव पारित कर सकता है। हालांकि, औपचारिक राज्य कानून केवल विधानसभा द्वारा बनाए जाते हैं।",
        "back_gu": "સરપંચ સ્થાનિક સ્વરાજ્યના સ્તરે (ગ્રામ પંચાયત) કામ કરે છે અને પંચાયતના સભ્યો સાથે ગામના વિકાસ માટે ઠરાવો પસાર કરી શકે છે. જોકે, ઔપચારિક રાજ્ય કાયદાઓ ફક્ત વિધાનસભા દ્વારા જ બનાવવામાં આવે છે."
    },
    {
        "id": get_id(),
        "type": "flashcard",
        "front": "Vijay Bhai is 24 years old. He has registered his candidature for the Assembly elections. Will his candidature be valid or not? Why?",
        "front_hi": "विजय भाई 24 वर्ष के हैं। उन्होंने विधानसभा चुनाव के लिए अपना नामांकन दर्ज कराया है। उनकी उम्मीदवारी वैध होगी या नहीं? क्यों?",
        "front_gu": "વિજય ભાઈ 24 વર્ષના છે. તેમણે વિધાનસભાની ચૂંટણી માટે ઉમેદવારી નોંધાવી છે. તેમની ઉમેદવારી માન્ય ગણાશે કે નહીં? શા માટે?",
        "back": "His candidature will not be valid. To become a member of the Legislative Assembly (MLA), the minimum age requirement according to the constitution is 25 years.",
        "back_hi": "उनकी उम्मीदवारी वैध नहीं होगी। विधानसभा सदस्य (विधायक) बनने के लिए संविधान के अनुसार न्यूनतम आयु 25 वर्ष होनी चाहिए।",
        "back_gu": "તેમની ઉમેદવારી માન્ય ગણાશે નહીં. વિધાનસભાના સભ્ય (ધારાસભ્ય) બનવા માટે, બંધારણ મુજબ લઘુત્તમ વય 25 વર્ષ હોવી જોઈએ."
    },
    {
        "id": get_id(),
        "type": "flashcard",
        "front": "Explain the difference between a bill and a law.",
        "front_hi": "विधेयक और कानून में अंतर स्पष्ट करें।",
        "front_gu": "બિલ અને કાયદા વચ્ચેનો તફાવત સમજાવો.",
        "back": "A bill is a proposed legislation presented in the assembly for discussion and voting. Once it is passed by the legislature and gets the Governor's approval (signature), it becomes a binding law (Act).",
        "back_hi": "विधेयक एक प्रस्तावित विधान है जिसे चर्चा और मतदान के लिए विधानसभा में प्रस्तुत किया जाता है। एक बार जब यह विधायिका द्वारा पारित हो जाता है और राज्यपाल की मंजूरी (हस्ताक्षर) प्राप्त कर लेता है, तो यह एक बाध्यकारी कानून (अधिनियम) बन जाता है।",
        "back_gu": "બિલ એ ચર્ચા અને મતદાન માટે વિધાનસભામાં રજૂ કરવામાં આવેલો સૂચિત કાયદો છે. એકવાર તે ધારાસભા દ્વારા પસાર થઈ જાય અને રાજ્યપાલની મંજૂરી (સહી) મેળવી લે, તો તે બંધનકર્તા કાયદો (અધિનિયમ) બની જાય છે."
    },
    {
        "id": get_id(),
        "type": "flashcard",
        "front": "What happens if Meenakshi, who is registered as a voter in Gujarat's Kutch district, registers her candidature in the Delhi Assembly elections?",
        "front_hi": "यदि मीनाक्षी, जो गुजरात के कच्छ जिले में मतदाता के रूप में पंजीकृत हैं, दिल्ली विधानसभा चुनाव में अपनी उम्मीदवारी दर्ज कराती हैं, तो क्या होगा?",
        "front_gu": "જો મીનાક્ષી, જે ગુજરાતના કચ્છ જિલ્લામાં મતદાર તરીકે નોંધાયેલ છે, તે દિલ્હી વિધાનસભાની ચૂંટણીમાં પોતાની ઉમેદવારી નોંધાવે તો શું થાય?",
        "back": "Generally, to contest state assembly elections, a person must be an elector for any assembly constituency in that particular state. Thus, her candidature in Delhi might be rejected unless she is registered as a voter in Delhi.",
        "back_hi": "आमतौर पर, राज्य विधानसभा चुनाव लड़ने के लिए, व्यक्ति को उस विशेष राज्य के किसी भी विधानसभा क्षेत्र के लिए मतदाता होना चाहिए। इस प्रकार, दिल्ली में उनकी उम्मीदवारी खारिज हो सकती है जब तक कि वह दिल्ली में मतदाता के रूप में पंजीकृत न हों।",
        "back_gu": "સામાન્ય રીતે, રાજ્ય વિધાનસભાની ચૂંટણી લડવા માટે, વ્યક્તિ તે ચોક્કસ રાજ્યના કોઈપણ વિધાનસભા મતવિસ્તાર માટે મતદાર હોવો જોઈએ. આમ, જ્યાં સુધી તેણી દિલ્હીમાં મતદાર તરીકે નોંધાયેલ ન હોય ત્યાં સુધી દિલ્હીમાં તેણીની ઉમેદવારી નકારી શકાય છે."
    }
]

data['blocks'].extend(new_blocks)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Blocks successfully added!")
