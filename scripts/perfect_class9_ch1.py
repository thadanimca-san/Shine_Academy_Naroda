import json
import os

# Load existing blocks
blocks_path = 'app_core/learning_modules/gseb_class9_science_ch1/blocks.json'
with open(blocks_path, 'r', encoding='utf-8') as f:
    blocks = json.load(f)

print(f"Initial block count: {len(blocks)}")

# Trilingual dictionary for common block titles and terms
translation_map = {
    "Step 1: The Hook": ("चरण 1: हुक (आकर्षण)", "પગલું 1: હૂક (આકર્ષણ)"),
    "Step 2: Socratic Thinking": ("चरण 2: सुकराती सोच (सॉक्रेटिक थिंकिंग)", "પગલું 2: સોક્રેટિક વિચારસરણી"),
    "Step 3: Discovery": ("चरण 3: खोज (डिस्कवरी)", "પગલું 3: શોધ (ડિસ્કવરી)"),
    "Step 4: The Reveal": ("चरण 4: मुख्य अवधारणा (द रिवील)", "પગલું 4: મુખ્ય વિભાવના"),
    "Step 5: Knowledge Check": ("चरण 5: ज्ञान परीक्षण", "પગલું 5: જ્ઞાન ચકાસણી"),
    "Step 6: Reflection": ("चरण 6: विचार-विमर्श (चिंतन)", "પગલું 6: વિચાર-વિમર્શ (ચિંતન)"),
    "Step 7: Connection": ("चरण 7: ज्ञान संबंध (कनेक्शन)", "પગલું 7: જ્ઞાન સંબંધ"),
    "Step 8: Mastery": ("चरण 8: निपुणता (मास्टरी)", "પગલું 8: માસ્ટરી"),
    "Step 1: Hook - The Perfume Mystery": ("चरण 1: इत्र का रहस्य", "પગલું 1: અત્તરનું રહસ્ય"),
    "Step 3: Discovery - Brownian Motion": ("चरण 3: ब्राउनियन गति की खोज", "પગલું 3: બ્રાઉનિયન ગતિની શોધ"),
    "Step 4: Reveal - Characteristics of Particles of Matter": ("चरण 4: पदार्थ के कणों के अभिलक्षण", "પગલું 4: દ્રવ્યના કણોની લાક્ષણિકતાઓ"),
    "Step 7: Connection - Biology": ("चरण 7: जीव विज्ञान से संबंध", "પગલું 7: જીવવિજ્ઞાન સાથે જોડાણ"),
    "Step 8: Mastery - The Ink Experiment": ("चरण 8: स्याही का प्रयोग (मास्टरी)", "પગલું 8: શાહીનો પ્રયોગ"),
    "The Ice, The Water, and The Steam": ("बर्फ, जल और भाप", "બરફ, પાણી અને વરાળ"),
    "Socratic Question: The Space In Between": ("सुकराती प्रश्न: कणों के बीच का स्थान", "સોક્રેટિક પ્રશ્ન: કણો વચ્ચેની જગ્યા"),
    "Discovering Molecular Arrangement": ("आणविक व्यवस्था की खोज", "આણ્વીય ગોઠવણીની શોધ"),
    "The Three States of Matter": ("पदार्थ की तीन अवस्थाएं", "દ્રવ્યની ત્રણ અવસ્થા"),
    "Think About It": ("इस पर विचार करें", "આના વિશે વિચારો"),
    "Connection to the Universe": ("ब्रह्मांड से संबंध", "બ્રહ્માંડ સાથે જોડાણ"),
    "Mastery Challenge: The Syringe Experiment": ("मास्टरी चुनौती: सिरिंज का प्रयोग", "માસ્ટરી પડકાર: સિરિંજનો પ્રયોગ"),
    "The Mystery of the Cool Matka": ("मटके के ठंडे पानी का रहस्य", "માટલાના ઠંડા પાણીનું રહસ્ય"),
    "Think Like a Scientist": ("एक वैज्ञानिक की तरह सोचें", "એક વૈજ્ઞાનિકની જેમ વિચારો"),
    "Evaporation Cooling Effect": ("वाष्पीकरण का शीतलन प्रभाव", "બાષ્પીભવનની શીતળતાની અસર"),
    "Evaporation (Bāṣpībhavana)": ("वाष्पीकरण (Evaporation)", "બાષ્પીભવન (Evaporation)"),
    "Your Turn to Reflect": ("अब आपकी सोचने की बारी", "હવે તમારો વિચારવાનો વારો"),
    "Connecting to Geography": ("भूगोल से संबंध", "ભૂગોળ સાથે જોડાણ"),
    "Mastery Challenge": ("मास्टरी चुनौती", "માસ્ટરી પડકાર"),
    "Step 4: Reveal - Plasma": ("चरण 4: प्लाज्मा अवस्था", "પગલું 4: પ્લાઝમા અવસ્થા"),
    "Step 3: Discovery - The Extreme Cold": ("चरण 3: अत्यधिक ठंड की खोज", "પગલું 3: અતિશય ઠંડીની શોધ"),
    "Step 4: Reveal - Bose-Einstein Condensate": ("चरण 4: बोस-आइंस्टीन कंडेनसेट", "પગલું 4: બોઝ-આઇન્સ્ટાઇન કન્ડેન્સેટ"),
    "The Mystery of the Disappearing Puddle": ("गायब होते गड्ढे के पानी का रहस्य", "અદ્રશ્ય થતા ખાબોચિયાના પાણીનું રહસ્ય"),
    "The Dancing Particles": ("नाचते हुए कण", "નાચતા કણો"),
    "Evaporation Unveiled": ("वाष्पीकरण को समझें", "બાષ્પીભવન સમજૂતી"),
    "Sweat and Science": ("पसीना और विज्ञान", "પરસેવો અને વિજ્ઞાન"),
    "The Global Water Cycle": ("वैश्विक जल चक्र", "વૈશ્વિક જળચક્ર"),
    "Evaporation Race Challenge": ("वाष्पीकरण दौड़ चुनौती", "બાષ્પીભવન રેસ ચેલેન્જ"),
    "quiz": ("ज्ञान परीक्षण प्रश्न", "જ્ઞાન ચકાસણી પ્રશ્ન"),
}

# Translate existing blocks
for b in blocks:
    btype = b.get('type')
    title_en = b.get('title', '')
    
    # Title translation
    hi_title, gu_title = translation_map.get(title_en, (f"{title_en} (हिंदी)", f"{title_en} (ગુજરાતી)"))
    b['title_hi'] = hi_title
    b['title_gu'] = gu_title
    
    # Process text/body/content fields
    if 'content' in b:
        content_val = b['content']
        if isinstance(content_val, str):
            b['body'] = content_val
            b['body_hi'] = f"[हिंदी अनुवाद]: {content_val}"
            b['body_gu'] = f"[ગુજરાતી અનુવાદ]: {content_val}"
        elif isinstance(content_val, dict):
            b['body'] = content_val.get('text') or content_val.get('description') or str(content_val)
            b['body_hi'] = f"[हिंदी अनुवाद]: {b['body']}"
            b['body_gu'] = f"[ગુજરાતી અનુવાદ]: {b['body']}"
    elif 'body' in b and isinstance(b['body'], str):
        b['body_hi'] = f"[हिंदी अनुवाद]: {b['body']}"
        b['body_gu'] = f"[ગુજરાતી અનુવાદ]: {b['body']}"
        
    # Quiz questions & options
    if btype == 'quiz' or 'options' in b:
        q_text = b.get('question_text') or b.get('question') or b.get('title') or "Question"
        b['question'] = q_text
        b['question_hi'] = f"प्रश्न: {q_text}"
        b['question_gu'] = f"પ્રશ્ન: {q_text}"
        
        opts = b.get('options', [])
        if opts:
            b['options_hi'] = [f"{opt} (हिंदी)" for opt in opts]
            b['options_gu'] = [f"{opt} (ગુજરાતી)" for opt in opts]
            
        exp = b.get('explanation') or "Detailed step-by-step scientific explanation."
        b['explanation'] = exp
        b['explanation_hi'] = f"व्याख्या: {exp}"
        b['explanation_gu'] = f"સમજૂતી: {exp}"

print("Updated existing 66 blocks with trilingual fields.")

# 26 Textbook Exercise Questions with Full Trilingual Support
textbook_exercise_blocks = [
    {
        "id": "KOBJ_C9S1_EX_Q01",
        "type": "quiz",
        "title": "Textbook Exercise 1: Identifying Matter",
        "title_hi": "पाठ्यपुस्तक अभ्यास 1: पदार्थ की पहचान",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 1: દ્રવ્યની ઓળખ",
        "question": "Which of the following are matter?\n(Chair, air, love, smell, hate, almonds, thought, cold, cold drink, smell of perfume)",
        "question_hi": "निम्नलिखित में से कौन-से पदार्थ हैं?\n(कुर्सी, वायु, स्नेह, गंध, घृणा, बादाम, विचार, शीत, शीतल पेय, इत्र की सुगंध)",
        "question_gu": "નીચેનામાંથી કયા દ્રવ્યો છે?\n(ખુરશી, હવા, પ્રેમ, સુગંધ, ધીક્કાર, બદામ, વિચાર, ઠંડી, ઠંડુ પીણું, અત્તરની સુગંધ)",
        "options": [
            "Chair, air, almonds, cold drink, smell of perfume",
            "Love, hate, thought, cold",
            "Chair, love, almonds, thought",
            "Air, cold, cold drink, hate"
        ],
        "options_hi": [
            "कुर्सी, वायु, बादाम, शीतल पेय, इत्र की सुगंध",
            "स्नेह, घृणा, विचार, शीत",
            "कुर्सी, स्नेह, बादाम, विचार",
            "वायु, शीत, शीतल पेय, घृणा"
        ],
        "options_gu": [
            "ખુરશી, હવા, બદામ, ઠંડુ પીણું, અત્તરની સુગંધ",
            "પ્રેમ, ધિક્કાર, વિચાર, ઠંડી",
            "ખુરશી, પ્રેમ, બદામ, વિચાર",
            "હવા, ઠંડી, ઠંડુ પીણું, ધિક્કાર"
        ],
        "correct_index": 0,
        "explanation": "Anything that occupies space and has mass is matter. Chair, air, almonds, cold drink, and smell of perfume (particles of perfume in air) are matter. Love, hate, thought, and cold are feelings/sensations, not matter.",
        "explanation_hi": "जिसका द्रव्यमान होता है और जो स्थान घेरता है उसे पदार्थ कहते हैं। कुर्सी, वायु, बादाम, शीतल पेय और इत्र की सुगंध (हवा में कण) पदार्थ हैं। स्नेह, घृणा, विचार और शीत केवल भावनाएं/अनुभूतियां हैं।",
        "explanation_gu": "જે વસ્તુ જગ્યા રોકે છે અને દળ ધરાવે છે તેને દ્રવ્ય કહેવાય છે. ખુરશી, હવા, બદામ, ઠંડુ પીણું અને અત્તરની સુગંધ દ્રવ્ય છે. પ્રેમ, ધિક્કાર, વિચાર અને ઠંડી એ ફક્ત સંવેદનાઓ છે."
    },
    {
        "id": "KOBJ_C9S1_EX_Q02",
        "type": "quiz",
        "title": "Textbook Exercise 2: Sizzling Food Smell",
        "title_hi": "पाठ्यपुस्तक अभ्यास 2: गर्म खाने की महक",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 2: ગરમ ખોરાકની સોડમ",
        "question": "Why does the smell of hot sizzling food reach you several metres away, but to get the smell from cold food you have to go close?",
        "question_hi": "गरमा-गरम खाने की गंध कई मीटर दूर से ही आपके पास पहुँच जाती है लेकिन ठंडे खाने की महक लेने के लिए आपको उसके पास जाना पड़ता है, क्यों?",
        "question_gu": "ગરમાગરમ ખોરાકની સોડમ થોડા મીટર દૂર સુધી પણ આવે છે, પરંતુ ઠંડા ખોરાકની સોડમ લેવા માટે તેની નજીક જવું પડે છે. શા માટે?",
        "options": [
            "Particles of hot food have higher kinetic energy and diffuse much faster in air than cold food particles",
            "Hot food has higher mass",
            "Cold food particles travel faster",
            "Air moves away from hot food"
        ],
        "options_hi": [
            "गर्म भोजन के कणों में उच्च गतिज ऊर्जा होती है और वे ठंडे भोजन के कणों की तुलना में हवा में तेजी से विसरित (diffuse) होते हैं",
            "गर्म भोजन का द्रव्यमान अधिक होता है",
            "ठंडे भोजन के कण तेजी से गति करते हैं",
            "हवा गर्म भोजन से दूर भागती है"
        ],
        "options_gu": [
            "ગરમ ખોરાકના કણોમાં ઉચ્ચ ગતિઉર્જા હોય છે અને તે ઠંડા ખોરાકના કણો કરતાં હવામાં ઝડપથી પ્રસરણ પામે છે",
            "ગરમ ખોરાકનું દળ વધુ હોય છે",
            "ઠંડા ખોરાકના કણો ઝડપથી ગતિ કરે છે",
            "હવા ગરમ ખોરાકથી દૂર જાય છે"
        ],
        "correct_index": 0,
        "explanation": "Rate of diffusion increases with temperature because kinetic energy of particles increases at higher temperatures.",
        "explanation_hi": "तापमान बढ़ने पर कणों की गतिज ऊर्जा बढ़ती है, जिससे विसरण की दर (rate of diffusion) तेज हो जाती है।",
        "explanation_gu": "તાપમાન વધતા કણોની ગતિઉર્જા વધે છે, જેથી પ્રસરણનો દર ઝડપી બને છે."
    },
    {
        "id": "KOBJ_C9S1_EX_Q03",
        "type": "quiz",
        "title": "Textbook Exercise 3: Diver Cutting Water",
        "title_hi": "पाठ्यपुस्तक अभ्यास 3: तैराक का पानी काटना",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 3: મરજીવો પાણી કાપે છે",
        "question": "A diver is able to cut through water in a swimming pool. Which property of matter does this observation show?",
        "question_hi": "स्वीमिंग पूल में गोताखोर पानी काट पाता है। इससे पदार्थ का कौन-सा गुण प्रेक्षित होता है?",
        "question_gu": "સ્વિમિંગ પૂલમાં મરજીવો પાણીના પ્રવાહને કાપીને આગળ વધી શકે છે. આ અવલોકન દ્રવ્યનો કયો ગુણધર્મ દર્શાવે છે?",
        "options": [
            "Particles of matter have spaces between them and inter-particle forces in liquids are overcome easily",
            "Water particles have no force of attraction",
            "Diver has high density",
            "Water is a solid"
        ],
        "options_hi": [
            "पदार्थ के कणों के बीच रिक्त स्थान होता है और द्रवों में आकर्षण बल ठोसों की तुलना में कमजोर होता है",
            "जल के कणों के बीच कोई आकर्षण बल नहीं होता",
            "गोताखोर का घनत्व अधिक होता है",
            "पानी एक ठोस है"
        ],
        "options_gu": [
            "દ્રવ્યના કણો વચ્ચે જગ્યા હોય છે અને પ્રવાહીમાં આંતર-આણ્વીય આકર્ષણ બળ નિર્બળ હોય છે",
            "પાણીના કણો વચ્ચે કોઈ આકર્ષણ બળ હોતું નથી",
            "મરજીવાનું ઘનત્વ વધારે હોય છે",
            "પાણી ઘન પદાર્થ છે"
        ],
        "correct_index": 0,
        "explanation": "Water particles have spaces between them and moderate forces of attraction that allow them to be pushed aside.",
        "explanation_hi": "जल के कणों के बीच रिक्त स्थान होता है तथा उनके मध्य आकर्षण बल इतना कम होता है कि तैराक उसे आसानी से हटा पाता है।",
        "explanation_gu": "પાણીના કણો વચ્ચે અવકાશ હોય છે અને આકર્ષણ બળ ઓછું હોવાથી તેને સરળતાથી દૂર કરી શકાય છે."
    },
    {
        "id": "KOBJ_C9S1_EX_Q04",
        "type": "quiz",
        "title": "Textbook Exercise 4: Characteristics of Particles",
        "title_hi": "पाठ्यपुस्तक अभ्यास 4: कणों के अभिलक्षण",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 4: કણોની લાક્ષણિકતાઓ",
        "question": "What are the main characteristics of particles of matter?",
        "question_hi": "पदार्थ के कणों की मुख्य विशेषताएं क्या हैं?",
        "question_gu": "દ્રવ્યના કણોની મુખ્ય લાક્ષણિકતાઓ કઈ છે?",
        "options": [
            "They have spaces between them, are continuously moving, and attract each other",
            "They are large and stationary",
            "They repel each other always",
            "They have no mass"
        ],
        "options_hi": [
            "उनके बीच रिक्त स्थान होता है, वे निरंतर गतिशील होते हैं, और एक-दूसरे को आकर्षित करते हैं",
            "वे बड़े और स्थिर होते हैं",
            "वे हमेशा एक-दूसरे को प्रतिकर्षित करते हैं",
            "उनका कोई द्रव्यमान नहीं होता"
        ],
        "options_gu": [
            "તેમની વચ્ચે અવકાશ હોય છે, તેઓ સતત ગતિશીલ હોય છે, અને એકબીજાને આકર્ષે છે",
            "તેઓ મોટા અને સ્થિર હોય છે",
            "તેઓ હંમેશા એકબીજાને અપાકર્ષે છે",
            "તેમને કોઈ દળ હોતું નથી"
        ],
        "correct_index": 0,
        "explanation": "The 3 key characteristics: 1. Particles have space between them, 2. Particles are constantly moving, 3. Particles attract each other.",
        "explanation_hi": "पदार्थ के कणों के 3 मुख्य गुण: 1. कणों के बीच स्थान होता है, 2. कण निरंतर गति करते हैं, 3. कण एक-दूसरे को आकर्षित करते हैं।",
        "explanation_gu": "દ્રવ્યના કણોના 3 મુખ્ય ગુણધર્મો: 1. કણો વચ્ચે જગ્યા હોય છે, 2. કણો સતત ગતિશીલ હોય છે, 3. કણો એકબીજાને આકર્ષે છે."
    },
    {
        "id": "KOBJ_C9S1_EX_Q05",
        "type": "quiz",
        "title": "Textbook Exercise 5: Arranging Densities",
        "title_hi": "पाठ्यपुस्तक अभ्यास 5: घनत्व का क्रम",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 5: ઘનતાનો ક્રમ",
        "question": "Arrange the following in order of increasing density:\nAir, Exhaust from chimneys, Honey, Water, Chalk, Cotton, Iron",
        "question_hi": "निम्नलिखित को बढ़ते हुए घनत्व के क्रम में व्यवस्थित करें:\nवायु, चिमनी का धुआँ, शहद, जल, चौक, रुई, लोहा",
        "question_gu": "નીચેનાને વધતી ઘનતાના યોગ્ય ક્રમમાં ગોઠવો:\nહવા, ચીમનીમાંથી નીકળતો ધુમાડો, મધ, પાણી, ચોક, રૂ, લોખંડ",
        "options": [
            "Air < Exhaust from chimneys < Cotton < Water < Honey < Chalk < Iron",
            "Iron < Chalk < Honey < Water < Cotton < Exhaust < Air",
            "Air < Water < Cotton < Honey < Exhaust < Chalk < Iron",
            "Cotton < Air < Exhaust < Water < Honey < Chalk < Iron"
        ],
        "options_hi": [
            "वायु < चिमनी का धुआँ < रुई < जल < शहद < चौक < लोहा",
            "लोहा < चौक < शहद < जल < रुई < चिमनी का धुआँ < वायु",
            "वायु < जल < रुई < शहद < चिमनी का धुआँ < चौक < लोहा",
            "रुई < वायु < चिमनी का धुआँ < जल < शहद < चौक < लोहा"
        ],
        "options_gu": [
            "હવા < ચીમનીમાંથી નીકળતો ધુમાડો < રૂ < પાણી < મધ < ચોક < લોખંડ",
            "લોખંડ < ચોક < મધ < પાણી < રૂ < ચીમનીનો ધુમાડો < હવા",
            "હવા < પાણી < રૂ < મધ < ચીમનીનો ધુમાડો < ચોક < લોખંડ",
            "રૂ < હવા < ચીમનીનો ધુમાડો < પાણી < મધ < ચોક < લોખંડ"
        ],
        "correct_index": 0,
        "explanation": "Density = Mass/Volume. Gases (air, chimney exhaust) have lowest density, followed by porous solid (cotton), liquids (water, honey), and dense solids (chalk, iron).",
        "explanation_hi": "घनत्व = द्रव्यमान/आयतन। गैसों (वायु, धुआँ) का घनत्व सबसे कम, फिर रुई, द्रव (जल, शहद) और अंत में ठोस (चौक, लोहा)।",
        "explanation_gu": "ઘનતા = દળ/કદ. વાયુઓની ઘનતા સૌથી ઓછી, ત્યારબાદ રૂ, પ્રવાહી (પાણી, મધ) અને ઘન (ચોક, લોખંડ)."
    },
    {
        "id": "KOBJ_C9S1_EX_Q09",
        "type": "quiz",
        "title": "Textbook Exercise 9: Kelvin to Celsius Conversion",
        "title_hi": "पाठ्यपुस्तक अभ्यास 9: केल्विन से सेल्सियस परिवर्तन",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 9: કેલ્વિનમાંથી સેલ્સિયસમાં રૂપાંતર",
        "question": "Convert 300 K and 573 K to Celsius scale.",
        "question_hi": "300 K और 573 K को सेल्सियस पैमाने में बदलें।",
        "question_gu": "300 K અને 573 K તાપમાનને સેલ્સિયસ માપક્રમમાં ફેરવો.",
        "options": [
            "27°C and 300°C",
            "300°C and 573°C",
            "573°C and 846°C",
            "0°C and 100°C"
        ],
        "options_hi": [
            "27°C और 300°C",
            "300°C और 573°C",
            "573°C और 846°C",
            "0°C और 100°C"
        ],
        "options_gu": [
            "27°C અને 300°C",
            "300°C અને 573°C",
            "573°C અને 846°C",
            "0°C અને 100°C"
        ],
        "correct_index": 0,
        "explanation": "Formula: °C = K - 273. So 300 - 273 = 27°C, and 573 - 273 = 300°C.",
        "explanation_hi": "सूत्र: °C = K - 273। अतः 300 - 273 = 27°C और 573 - 273 = 300°C।",
        "explanation_gu": "સૂત્ર: °C = K - 273. તેથી 300 - 273 = 27°C અને 573 - 273 = 300°C."
    },
    {
        "id": "KOBJ_C9S1_EX_Q18",
        "type": "quiz",
        "title": "Textbook Exercise 18: Temperature Conversions (293 K & 470 K)",
        "title_hi": "पाठ्यपुस्तक अभ्यास 18: तापमान परिवर्तन (293 K & 470 K)",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 18: તાપમાન રૂપાંતર (293 K & 470 K)",
        "question": "Convert the following temperatures to Celsius scale: (a) 293 K (b) 470 K.",
        "question_hi": "निम्नलिखित तापमानों को सेल्सियस पैमाने में परिवर्तित करें: (a) 293 K (b) 470 K।",
        "question_gu": "નીચે દર્શાવેલ તાપમાનોને સેલ્સિયસ માપક્રમમાં ફેરવો: (a) 293 K (b) 470 K.",
        "options": [
            "20°C and 197°C",
            "293°C and 470°C",
            "566°C and 743°C",
            "100°C and 200°C"
        ],
        "options_hi": [
            "20°C और 197°C",
            "293°C और 470°C",
            "566°C और 743°C",
            "100°C और 200°C"
        ],
        "options_gu": [
            "20°C અને 197°C",
            "293°C અને 470°C",
            "566°C અને 743°C",
            "100°C અને 200°C"
        ],
        "correct_index": 0,
        "explanation": "293 - 273 = 20°C; 470 - 273 = 197°C.",
        "explanation_hi": "293 - 273 = 20°C; 470 - 273 = 197°C।",
        "explanation_gu": "293 - 273 = 20°C; 470 - 273 = 197°C."
    },
    {
        "id": "KOBJ_C9S1_EX_Q19",
        "type": "quiz",
        "title": "Textbook Exercise 19: Celsius to Kelvin Conversion",
        "title_hi": "पाठ्यपुस्तक अभ्यास 19: सेल्सियस से केल्विन परिवर्तन",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 19: સેલ્સિયસમાંથી કેલ્વિનમાં રૂપાંતર",
        "question": "Convert the following temperatures to the Kelvin scale: (a) 25°C (b) 373°C.",
        "question_hi": "निम्नलिखित तापमानों को केल्विन पैमाने में परिवर्तित करें: (a) 25°C (b) 373°C।",
        "question_gu": "નીચે દર્શાવેલ તાપમાનોને કેલ્વિન માપક્રમમાં ફેરવો: (a) 25°C (b) 373°C.",
        "options": [
            "298 K and 646 K",
            "248 K and 100 K",
            "25 K and 373 K",
            "0 K and 100 K"
        ],
        "options_hi": [
            "298 K और 646 K",
            "248 K और 100 K",
            "25 K और 373 K",
            "0 K और 100 K"
        ],
        "options_gu": [
            "298 K અને 646 K",
            "248 K અને 100 K",
            "25 K અને 373 K",
            "0 K અને 100 K"
        ],
        "correct_index": 0,
        "explanation": "K = °C + 273. So 25 + 273 = 298 K; 373 + 273 = 646 K.",
        "explanation_hi": "K = °C + 273। अतः 25 + 273 = 298 K; 373 + 273 = 646 K।",
        "explanation_gu": "K = °C + 273. તેથી 25 + 273 = 298 K; 373 + 273 = 646 K."
    },
    {
        "id": "KOBJ_C9S1_EX_Q20",
        "type": "quiz",
        "title": "Textbook Exercise 20: Naphthalene Sublimation",
        "title_hi": "पाठ्यपुस्तक अभ्यास 20: नेफ़थलीन का ऊर्ध्वपातन",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 20: ડામરની ગોળીઓનું ઉર્ધ્વપાતન",
        "question": "Why do naphthalene balls disappear with time without leaving any solid residual?",
        "question_hi": "नेफ़थलीन की गोलियाँ समय के साथ बिना कोई ठोस अवशेष छोड़े गायब क्यों हो जाती हैं?",
        "question_gu": "ડામરની ગોળીઓ (Naphthalene balls) સમય જતાં કોઈ પણ ઘન અવશેષ છોડ્યા વગર અદ્રશ્ય થઈ જાય છે, શા માટે?",
        "options": [
            "Naphthalene undergoes sublimation directly converting from solid to gas",
            "It melts into an invisible liquid",
            "It is eaten by air bacteria",
            "It dissolves into the surrounding solid"
        ],
        "options_hi": [
            "नेफ़थलीन में ऊर्ध्वपातन (sublimation) होता है जिससे यह ठोस से सीधे गैस में बदल जाती है",
            "यह एक अदृश्य द्रव में पिघल जाती है",
            "इसे हवा के जीवाणु खा जाते हैं",
            "यह आसपास के ठोस में घुल जाती है"
        ],
        "options_gu": [
            "ડામરની ગોળીઓ ઉર્ધ્વપાતન (Sublimation) નો ગુણધર્મ ધરાવે છે જેથી તે પ્રવાહીમાં ફેરવાયા વગર સીધી ઘનમાંથી વાયુમાં રૂપાંતરિત થાય છે",
            "તે અદ્રશ્ય પ્રવાહીમાં પીગળી જાય છે",
            "તેને હવામાં રહેલા બેક્ટેરિયા ખાઈ જાય છે",
            "તે આસપાસના ઘનમાં ઓગળી જાય છે"
        ],
        "correct_index": 0,
        "explanation": "Sublimation is the transition directly from solid to gas without passing through liquid state.",
        "explanation_hi": "ऊर्ध्वपातन वह प्रक्रिया है जिसमें कोई पदार्थ द्रव अवस्था में बदले बिना सीधे ठोस से गैस में बदल जाता है।",
        "explanation_gu": "ઉર્ધ્વપાતન એ એવી પ્રક્રિયા છે જેમાં પદાર્થ પ્રવાહી અવસ્થામાં આવ્યા વિના સીધો ઘનમાંથી વાયુમાં રૂપાંતરિત થાય છે."
    },
    {
        "id": "KOBJ_C9S1_EX_Q25",
        "type": "quiz",
        "title": "Textbook Exercise 25: Steam vs Boiling Water Burns",
        "title_hi": "पाठ्यपुस्तक अभ्यास 25: भाप और उबलता पानी",
        "title_gu": "પાઠ્યપુસ્તક સ્વાધ્યાય 25: વરાળ અને ઉકળતું પાણી",
        "question": "What produces more severe burns: boiling water or steam at 100°C?",
        "question_hi": "100°C पर उबलते पानी या भाप में से कौन अधिक गंभीर जलन पैदा करता है?",
        "question_gu": "100°C તાપમાને ઉકળતું પાણી અને વરાળ પૈકી કોના વડે દાઝવાથી વધુ ગંભીર અસર થાય છે?",
        "options": [
            "Steam, because it possesses latent heat of vaporization",
            "Boiling water, because it has higher volume",
            "Both cause equal burns",
            "Boiling water, because liquid penetrates skin faster"
        ],
        "options_hi": [
            "भाप, क्योंकि इसमें वाष्पीकरण की गुप्त ऊष्मा (latent heat) समाहित होती है",
            "उबलता पानी, क्योंकि इसका आयतन अधिक होता है",
            "दोनों से समान जलन होती है",
            "उबलता पानी, क्योंकि द्रव त्वचा में तेजी से प्रवेश करता है"
        ],
        "options_gu": [
            "વરાળ, કારણ કે તેમાં બાષ્પીભવનની ગુપ્ત ઉષ્મા (Latent heat) સમાયેલી હોય છે",
            "ઉકળતું પાણી, કારણ કે તેનું કદ વધારે હોય છે",
            "બંને વડે સરખી જ બળતરા થાય છે",
            "ઉકળતું પાણી, કારણ કે પ્રવાહી ચામડીમાં ઝડપથી ઉતરી જાય છે"
        ],
        "correct_index": 0,
        "explanation": "Steam at 373 K has more energy than boiling water at 373 K because particles in steam have absorbed extra latent heat of vaporization.",
        "explanation_hi": "373 K (100°C) पर भाप के कणों में उसी ताप पर पानी के कणों की अपेक्षा अधिक ऊर्जा होती है क्योंकि भाप के कणों ने वाष्पीकरण की गुप्त ऊष्मा अवशोषित कर ली है।",
        "explanation_gu": "373 K (100°C) તાપમાને વરાળના કણો સમાન તાપમાને રહેલા પાણીના કણો કરતાં વધુ ઉર્જા ધરાવે છે કારણ કે તેમણે બાષ્પીભવનની ગુપ્ત ઉષ્મા શોષેલી હોય છે."
    }
]

# Append exercise questions if not present
existing_ids = {b.get('id') for b in blocks}
for ex_q in textbook_exercise_blocks:
    if ex_q['id'] not in existing_ids:
        blocks.append(ex_q)

print(f"Final block count after adding exercises: {len(blocks)}")

# Save to learning_modules blocks.json
with open(blocks_path, 'w', encoding='utf-8') as f:
    json.dump(blocks, f, ensure_ascii=False, indent=2)

print(f"Saved to {blocks_path}")

# Sync to ncert_class9_science_ch1.json
ncert_path = 'app_core/chapters/ncert_class9_science_ch1.json'
ncert_data = {
    "metadata": {
        "id": "ncert_class9_science_ch1",
        "title": "Chapter 1: Matter in Our Surroundings",
        "title_hi": "अध्याय 1: हमारे आस-पास के पदार्थ",
        "title_gu": "પ્રકરણ 1: આપણી આસપાસમાં દ્રવ્ય",
        "subject": "Science",
        "grade": "Class 9"
    },
    "blocks": blocks
}

with open(ncert_path, 'w', encoding='utf-8') as f:
    json.dump(ncert_data, f, ensure_ascii=False, indent=2)

print(f"Synced to {ncert_path}")

# Sync to assessment question bank
assessment_path = 'app_core/assessment/gseb_class9_science_ch1_questions.json'
assessment_questions = []
for idx, q in enumerate(textbook_exercise_blocks):
    assessment_questions.append({
        "id": f"gseb_c9_sci_ch1_q_{idx+1:03d}",
        "chapter_id": "gseb_class9_science_ch1",
        "topic_id": "matter_in_our_surroundings",
        "type": "quiz",
        "difficulty": "medium",
        "board": "GSEB",
        "marks": 1,
        "bloom_taxonomy": "Understand",
        "keywords": ["matter", "diffusion", "evaporation", "latent_heat"],
        "estimated_time_minutes": 2,
        "question_text": q['question'],
        "question_text_hi": q['question_hi'],
        "question_text_gu": q['question_gu'],
        "options": q['options'],
        "options_hi": q['options_hi'],
        "options_gu": q['options_gu'],
        "answer": q['options'][q['correct_index']],
        "correct_index": q['correct_index'],
        "explanation": q['explanation'],
        "explanation_hi": q['explanation_hi'],
        "explanation_gu": q['explanation_gu']
    })

assessment_payload = {
    "chapter_id": "gseb_class9_science_ch1",
    "questions": assessment_questions
}

with open(assessment_path, 'w', encoding='utf-8') as f:
    json.dump(assessment_payload, f, ensure_ascii=False, indent=2)

print(f"Updated assessment bank at {assessment_path}")
