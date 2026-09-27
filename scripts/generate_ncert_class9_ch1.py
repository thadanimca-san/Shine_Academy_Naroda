import json
import os

def create_block(b_type, b_id, content, content_hi, content_gu, **kwargs):
    block = {
        "type": b_type,
        "id": b_id,
    }
    
    # Adding root-level fields depending on block type
    # For standard text blocks (theory, definition, etc.)
    if b_type in ["theory", "hook", "definition", "discovery", "reflection", "connection", "real_world_example"]:
        block["body"] = content
        block["body_hi"] = content_hi
        block["body_gu"] = content_gu
    
    # For questions (mcq)
    elif b_type == "mcq" or b_type == "knowledge_check" or b_type == "socratic_question":
        # Usually mcq type is what's rendered, sometimes 'socratic_question' is used. Let's use 'mcq'
        block["type"] = b_type if b_type in ["mcq", "knowledge_check"] else "socratic_question"
        block["question"] = kwargs.get("question", "")
        block["question_hi"] = kwargs.get("question_hi", "")
        block["question_gu"] = kwargs.get("question_gu", "")
        
        block["options"] = kwargs.get("options", [])
        block["options_hi"] = kwargs.get("options_hi", [])
        block["options_gu"] = kwargs.get("options_gu", [])
        
        block["correct_index"] = kwargs.get("correct_index", 0)
        
        block["explanation"] = kwargs.get("explanation", "")
        block["explanation_hi"] = kwargs.get("explanation_hi", "")
        block["explanation_gu"] = kwargs.get("explanation_gu", "")
    
    # Merge any other kwargs at root level
    for k, v in kwargs.items():
        if k not in block and not k.endswith('_hi') and not k.endswith('_gu') and k not in ['question', 'options', 'correct_index', 'explanation']:
            block[k] = v

    return block

def generate_chapter():
    chapter_id = "ncert_class9_science_ch1"
    blocks = []
    
    # Concept 1: Scientific Models
    blocks.append(create_block("hook", f"{chapter_id}_HOOK_01",
        "Have you ever wondered how scientists study complex things like a whole galaxy or a tiny atom? They cannot bring a star into a lab! How do they do it?",
        "क्या आपने कभी सोचा है कि वैज्ञानिक पूरी आकाशगंगा या एक छोटे से परमाणु जैसी जटिल चीजों का अध्ययन कैसे करते हैं? वे किसी तारे को प्रयोगशाला में नहीं ला सकते! वे ऐसा कैसे करते हैं?",
        "શું તમે ક્યારેય વિચાર્યું છે કે વૈજ્ઞાનિકો આખી આકાશગંગા કે નાના અણુ જેવી જટિલ વસ્તુઓનો અભ્યાસ કેવી રીતે કરે છે? તેઓ તારાને પ્રયોગશાળામાં લાવી શકતા નથી! તેઓ આ કેવી રીતે કરે છે?"
    ))
    
    blocks.append(create_block("socratic_question", f"{chapter_id}_SOC_01",
        content="", content_hi="", content_gu="",
        question="If you were to explain a car's motion to someone, what detail is NOT important?",
        question_hi="यदि आपको किसी को कार की गति समझानी हो, तो कौन सा विवरण महत्वपूर्ण नहीं है?",
        question_gu="જો તમારે કોઈને કારની ગતિ સમજાવવી હોય, તો કઈ વિગત મહત્વપૂર્ણ નથી?",
        options=["Speed of the car", "Color of the car", "Direction of the car", "Time taken"],
        options_hi=["कार की गति", "कार का रंग", "कार की दिशा", "लिया गया समय"],
        options_gu=["કારની ઝડપ", "કારનો રંગ", "કારની દિશા", "લીધેલો સમય"],
        correct_index=1,
        explanation="The color of the car does not affect its motion. Ignoring such details helps us focus on the physics.",
        explanation_hi="कार का रंग उसकी गति को प्रभावित नहीं करता है। ऐसे विवरणों को अनदेखा करने से हमें भौतिकी पर ध्यान केंद्रित करने में मदद मिलती है।",
        explanation_gu="કારનો રંગ તેની ગતિને અસર કરતો નથી. આવી વિગતોને અવગણવાથી અમને ભૌતિકશાસ્ત્ર પર ધ્યાન કેન્દ્રિત કરવામાં મદદ મળે છે."
    ))
    
    blocks.append(create_block("theory", f"{chapter_id}_THEORY_01",
        "The natural world is complex. To make sense of it, science uses **models**. These are simplified ways of looking at real systems that focus only on what is most important for a given question.",
        "प्राकृतिक दुनिया जटिल है। इसे समझने के लिए, विज्ञान **मॉडल (प्रतिरूप)** का उपयोग करता है। ये वास्तविक प्रणालियों को देखने के सरल तरीके हैं जो केवल उसी पर ध्यान केंद्रित करते हैं जो किसी दिए गए प्रश्न के लिए सबसे महत्वपूर्ण है।",
        "કુદરતી વિશ્વ જટિલ છે. તેને સમજવા માટે, વિજ્ઞાન **મોડેલ** નો ઉપયોગ કરે છે. આ વાસ્તવિક સિસ્ટમોને જોવાની સરળ રીતો છે જે માત્ર આપેલ પ્રશ્ન માટે જે સૌથી મહત્વપૂર્ણ છે તેના પર ધ્યાન કેન્દ્રિત કરે છે."
    ))
    
    blocks.append(create_block("definition", f"{chapter_id}_DEF_01",
        "**Scientific Model**: A representation of an idea, object, process, or system that is used to describe and explain phenomena that cannot be experienced directly.",
        "**वैज्ञानिक मॉडल**: एक विचार, वस्तु, प्रक्रिया या प्रणाली का प्रतिनिधित्व जिसका उपयोग उन घटनाओं का वर्णन और व्याख्या करने के लिए किया जाता है जिन्हें सीधे अनुभव नहीं किया जा सकता है।",
        "**વૈજ્ઞાનિક મોડેલ**: એક વિચાર, વસ્તુ, પ્રક્રિયા અથવા સિસ્ટમનું પ્રતિનિધિત્વ જેનો ઉપયોગ એવી ઘટનાઓનું વર્ણન અને સમજાવવા માટે થાય છે જેનો સીધો અનુભવ કરી શકાતો નથી."
    ))
    
    # Activity 1.1: Let us model
    blocks.append(create_block("real_world_example", f"{chapter_id}_EX_01",
        "**Activity 1.1: Let us model.** Suppose you ride a bicycle from your school to your home. You want to model the time it takes to go home from school. What details would you keep? (Distance, average speed). What details could you ignore? (Brand of the bicycle, color of your bag).",
        "**गतिविधि 1.1: आइए मॉडल बनाएं।** मान लीजिए कि आप अपने स्कूल से अपने घर तक साइकिल चलाते हैं। आप स्कूल से घर जाने में लगने वाले समय का मॉडल बनाना चाहते हैं। आप किन विवरणों को रखेंगे? (दूरी, औसत गति)। आप किन विवरणों को अनदेखा कर सकते हैं? (साइकिल का ब्रांड, आपके बैग का रंग)।",
        "**પ્રવૃત્તિ 1.1: ચાલો મોડેલ બનાવીએ.** ધારો કે તમે તમારી શાળાથી તમારા ઘર સુધી સાયકલ ચલાવો છો. તમે શાળાએથી ઘરે જવામાં લાગતા સમયનું મોડેલ બનાવવા માંગો છો. તમે કઈ વિગતો રાખશો? (અંતર, સરેરાશ ઝડપ). તમે કઈ વિગતોને અવગણી શકો છો? (સાયકલની બ્રાન્ડ, તમારી બેગનો રંગ)."
    ))

    # Concept 2: Mathematics, Symbols and Standard Units
    blocks.append(create_block("hook", f"{chapter_id}_HOOK_02",
        "Imagine if every shopkeeper used a different stone to measure 1 kg of rice. It would be chaos! How does science solve this?",
        "कल्पना कीजिए कि अगर हर दुकानदार 1 किलो चावल मापने के लिए एक अलग पत्थर का इस्तेमाल करता। यह बहुत बड़ी उलझन होगी! विज्ञान इसे कैसे हल करता है?",
        "કલ્પના કરો કે જો દરેક દુકાનદાર 1 કિલો ચોખા માપવા માટે અલગ પથ્થરનો ઉપયોગ કરે. આ ખૂબ મોટી મૂંઝવણ હશે! વિજ્ઞાન આને કેવી રીતે હલ કરે છે?"
    ))
    
    blocks.append(create_block("theory", f"{chapter_id}_THEORY_02",
        "Science uses a shared language of specific terms, symbols, and units. Standard units allow scientific results to be compared globally and ensure fairness in daily life and trade.",
        "विज्ञान विशिष्ट शब्दों, प्रतीकों और इकाइयों की एक साझा भाषा का उपयोग करता है। मानक इकाइयाँ वैज्ञानिक परिणामों की विश्व स्तर पर तुलना करने की अनुमति देती हैं और दैनिक जीवन और व्यापार में निष्पक्षता सुनिश्चित करती हैं।",
        "વિજ્ઞાન ચોક્કસ શબ્દો, પ્રતીકો અને એકમોની વહેંચાયેલ ભાષાનો ઉપયોગ કરે છે. પ્રમાણભૂત એકમો વૈજ્ઞાનિક પરિણામોની વૈશ્વિક સ્તરે તુલના કરવાની મંજૂરી આપે છે અને દૈનિક જીવન અને વેપારમાં નિષ્પક્ષતા સુનિશ્ચિત કરે છે."
    ))

    blocks.append(create_block("theory", f"{chapter_id}_THEORY_03",
        "Science often turns to mathematics. An equation is not just a calculation tool; it is a compact statement about how certain things are related. Mathematics becomes a powerful language for thinking.",
        "विज्ञान अक्सर गणित की ओर मुड़ता है। एक समीकरण केवल एक गणना उपकरण नहीं है; यह एक संक्षिप्त कथन है कि कुछ चीजें कैसे संबंधित हैं। गणित सोचने के लिए एक शक्तिशाली भाषा बन जाता है।",
        "વિજ્ઞાન ઘણીવાર ગણિત તરફ વળે છે. સમીકરણ એ માત્ર ગણતરીનું સાધન નથી; અમુક બાબતો કેવી રીતે સંબંધિત છે તે વિશે તે એક કોમ્પેક્ટ નિવેદન છે. ગણિત વિચારવા માટે એક શક્તિશાળી ભાષા બની જાય છે."
    ))

    # Concept 3: Laws, Theories, and Predictions
    blocks.append(create_block("theory", f"{chapter_id}_THEORY_04",
        "As observations are repeated and tested, we form Laws, Theories, and Principles.\n- **Law**: Describes a regular pattern observed in nature (e.g., Newton's laws of motion).\n- **Theory**: Explains *why* those patterns occur (e.g., Atomic theory).\n- **Principle**: Broad ideas that help make sense of a situation (e.g., Conservation of energy).",
        "जैसे-जैसे अवलोकनों को दोहराया जाता है और परीक्षण किया जाता है, हम नियम, सिद्धांत और सिद्धांत बनाते हैं।\n- **नियम**: प्रकृति में देखे गए एक नियमित पैटर्न का वर्णन करता है (उदा. न्यूटन के गति के नियम)।\n- **सिद्धांत**: यह बताता है कि वे पैटर्न *क्यों* होते हैं (उदा. परमाणु सिद्धांत)।\n- **सिद्धांत (प्रिंसिपल)**: व्यापक विचार जो किसी स्थिति को समझने में मदद करते हैं (उदा. ऊर्जा संरक्षण)।",
        "જેમ જેમ અવલોકનોનું પુનરાવર્તન થાય છે અને પરીક્ષણ કરવામાં આવે છે, તેમ આપણે નિયમો, સિદ્ધાંતો અને સિદ્ધાંતો (પ્રિન્સિપલ) બનાવીએ છીએ.\n- **નિયમ**: પ્રકૃતિમાં જોવા મળતી નિયમિત પેટર્નનું વર્ણન કરે છે (દા.ત. ન્યૂટનના ગતિના નિયમો).\n- **સિદ્ધાંત (થિયરી)**: સમજાવે છે કે શા માટે તે પેટર્ન થાય છે (દા.ત. અણુ સિદ્ધાંત).\n- **સિદ્ધાંત (પ્રિન્સિપલ)**: વ્યાપક વિચારો જે પરિસ્થિતિને સમજવામાં મદદ કરે છે (દા.ત. ઊર્જાનું સંરક્ષણ)."
    ))

    blocks.append(create_block("theory", f"{chapter_id}_THEORY_05",
        "One of the most remarkable strengths of science is its ability to make **predictions**. These are reasoned expectations based on evidence, not just guesses.",
        "विज्ञान की सबसे उल्लेखनीय ताकतों में से एक **भविष्यवाणियां** करने की क्षमता है। ये केवल अनुमान नहीं हैं, बल्कि सबूतों पर आधारित तर्कसंगत अपेक्षाएं हैं।",
        "વિજ્ઞાનની સૌથી નોંધપાત્ર શક્તિઓમાંની એક **આગાહી** કરવાની ક્ષમતા છે. આ માત્ર અનુમાન નથી, પરંતુ પુરાવા પર આધારિત તર્કબદ્ધ અપેક્ષાઓ છે."
    ))

    # Concept 4: Estimations
    blocks.append(create_block("hook", f"{chapter_id}_HOOK_03",
        "Can you calculate exactly how many liters of air you breathe in a day? Probably not exactly, but you can definitely estimate it!",
        "क्या आप ठीक-ठीक गणना कर सकते हैं कि आप एक दिन में कितने लीटर हवा में सांस लेते हैं? शायद बिल्कुल ठीक नहीं, लेकिन आप निश्चित रूप से इसका अनुमान लगा सकते हैं!",
        "શું તમે ચોક્કસ ગણતરી કરી શકો છો કે તમે એક દિવસમાં કેટલા લિટર હવાનો શ્વાસ લો છો? કદાચ બરાબર નથી, પરંતુ તમે ચોક્કસપણે તેનો અંદાજ લગાવી શકો છો!"
    ))

    blocks.append(create_block("theory", f"{chapter_id}_THEORY_06",
        "Exact values are not always necessary. An **approximate estimate** is often enough to tell us whether a result is reasonable or impossible. Estimation builds intuition and detects errors.",
        "सटीक मूल्यों की हमेशा आवश्यकता नहीं होती है। यह बताने के लिए अक्सर एक **अनुमान** ही काफी होता है कि कोई परिणाम उचित है या असंभव। अनुमान अंतर्ज्ञान का निर्माण करता है और त्रुटियों का पता लगाता है।",
        "ચોક્કસ મૂલ્યો હંમેશા જરૂરી નથી. કોઈ પરિણામ વાજબી છે કે અશક્ય તે કહેવા માટે **આશરે અંદાજ** વારંવાર પૂરતો હોય છે. અંદાજ અંતર્જ્ઞાન બનાવે છે અને ભૂલો શોધી કાઢે છે."
    ))

    # Pause and Ponder / Exercises
    blocks.append(create_block("reflection", f"{chapter_id}_REFL_01",
        "**Pause and Ponder 1**: Think of a prediction you or your family made recently. Was it based on evidence and reasoning, or mainly on guesswork? How can scientific thinking improve such predictions?",
        "**रुकें और विचार करें 1**: उस भविष्यवाणी के बारे में सोचें जो आपने या आपके परिवार ने हाल ही में की थी। क्या यह साक्ष्य और तर्क पर आधारित था, या मुख्य रूप से अनुमान पर? वैज्ञानिक सोच ऐसी भविष्यवाणियों को कैसे सुधार सकती है?",
        "**થોભો અને વિચાર કરો 1**: એવી આગાહી વિશે વિચારો જે તમે અથવા તમારા પરિવારે તાજેતરમાં કરી હતી. શું તે પુરાવા અને તર્ક પર આધારિત હતું, અથવા મુખ્યત્વે અનુમાન પર? વૈજ્ઞાનિક વિચારસરણી આવી આગાહીઓને કેવી રીતે સુધારી શકે?"
    ))

    blocks.append(create_block("reflection", f"{chapter_id}_REFL_02",
        "**Pause and Ponder 2**: Describe one situation where an approximate answer is good enough (like estimating food for a party), and one where you would need a very exact value (like designing airplane parts).",
        "**रुकें और विचार करें 2**: एक ऐसी स्थिति का वर्णन करें जहां एक अनुमानित उत्तर काफी अच्छा हो (जैसे पार्टी के लिए भोजन का अनुमान लगाना), और एक जहां आपको बहुत सटीक मूल्य की आवश्यकता होगी (जैसे हवाई जहाज के हिस्से डिजाइन करना)।",
        "**થોભો અને વિચાર કરો 2**: એવી પરિસ્થિતિનું વર્ણન કરો કે જ્યાં આશરે જવાબ પૂરતો સારો હોય (જેમ કે પાર્ટી માટે ખોરાકનો અંદાજ કાઢવો), અને જ્યાં તમને ખૂબ જ ચોક્કસ મૂલ્યની જરૂર હોય (જેમ કે એરોપ્લેનના ભાગો ડિઝાઇન કરવા)."
    ))

    blocks.append(create_block("reflection", f"{chapter_id}_REFL_03",
        "**Pause and Ponder 3**: Choose a real-life object (like a mobile phone). Notice how physics (battery, screen), chemistry (materials), and mathematics (software logic) all connect to make it work! Science has no boundaries.",
        "**रुकें और विचार करें 3**: कोई वास्तविक जीवन की वस्तु (जैसे मोबाइल फोन) चुनें। ध्यान दें कि भौतिकी (बैटरी, स्क्रीन), रसायन विज्ञान (सामग्री), और गणित (सॉफ्टवेयर लॉजिक) इसे काम करने के लिए कैसे जुड़ते हैं! विज्ञान की कोई सीमा नहीं है।",
        "**થોભો અને વિચાર કરો 3**: કોઈ વાસ્તવિક જીવનની વસ્તુ (જેમ કે મોબાઈલ ફોન) પસંદ કરો. નોંધ કરો કે ભૌતિકશાસ્ત્ર (બેટરી, સ્ક્રીન), રસાયણશાસ્ત્ર (સામગ્રી), અને ગણિત (સોફ્ટવેર લોજિક) તેને કામ કરવા માટે કેવી રીતે જોડાય છે! વિજ્ઞાનની કોઈ સીમા હોતી નથી."
    ))

    # MCQ Knowledge Checks
    blocks.append(create_block("knowledge_check", f"{chapter_id}_MCQ_01",
        content="", content_hi="", content_gu="",
        question="Which of the following describes a regular pattern observed in nature?",
        question_hi="निम्नलिखित में से कौन प्रकृति में देखे गए एक नियमित पैटर्न का वर्णन करता है?",
        question_gu="નીચેનામાંથી કયું પ્રકૃતિમાં જોવા મળતી નિયમિત પેટર્નનું વર્ણન કરે છે?",
        options=["Scientific Theory", "Scientific Law", "Scientific Model", "Scientific Guess"],
        options_hi=["वैज्ञानिक सिद्धांत", "वैज्ञानिक नियम", "वैज्ञानिक मॉडल", "वैज्ञानिक अनुमान"],
        options_gu=["વૈજ્ઞાનિક સિદ્ધાંત", "વૈજ્ઞાનિક નિયમ", "વૈજ્ઞાનિક મોડેલ", "વૈજ્ઞાનિક અનુમાન"],
        correct_index=1,
        explanation="A Scientific Law describes a regular pattern observed in nature, such as Newton's Laws of Motion.",
        explanation_hi="एक वैज्ञानिक नियम प्रकृति में देखे गए एक नियमित पैटर्न का वर्णन करता है, जैसे न्यूटन के गति के नियम।",
        explanation_gu="વૈજ્ઞાનિક નિયમ પ્રકૃતિમાં જોવા મળતી નિયમિત પેટર્નનું વર્ણન કરે છે, જેમ કે ન્યૂટનના ગતિના નિયમો."
    ))

    blocks.append(create_block("knowledge_check", f"{chapter_id}_MCQ_02",
        content="", content_hi="", content_gu="",
        question="Why do scientists use models?",
        question_hi="वैज्ञानिक मॉडल का उपयोग क्यों करते हैं?",
        question_gu="વૈજ્ઞાનિકો મોડેલનો ઉપયોગ શા માટે કરે છે?",
        options=[
            "To make things more complicated",
            "Because real objects are not available",
            "To simplify complex systems by ignoring less important details",
            "To draw beautiful pictures"
        ],
        options_hi=[
            "चीजों को और अधिक जटिल बनाने के लिए",
            "क्योंकि वास्तविक वस्तुएं उपलब्ध नहीं हैं",
            "कम महत्वपूर्ण विवरणों को अनदेखा करके जटिल प्रणालियों को सरल बनाने के लिए",
            "सुंदर चित्र बनाने के लिए"
        ],
        options_gu=[
            "વસ્તુઓને વધુ જટિલ બનાવવા માટે",
            "કારણ કે વાસ્તવિક વસ્તુઓ ઉપલબ્ધ નથી",
            "ઓછી મહત્વની વિગતોને અવગણીને જટિલ સિસ્ટમોને સરળ બનાવવા માટે",
            "સુંદર ચિત્રો દોરવા માટે"
        ],
        correct_index=2,
        explanation="Models are simplified ways of looking at real systems that focus only on what is most important for a given question.",
        explanation_hi="मॉडल वास्तविक प्रणालियों को देखने के सरल तरीके हैं जो केवल उसी पर ध्यान केंद्रित करते हैं जो किसी दिए गए प्रश्न के लिए सबसे महत्वपूर्ण है।",
        explanation_gu="મોડેલ્સ વાસ્તવિક સિસ્ટમોને જોવાની સરળ રીતો છે જે આપેલ પ્રશ્ન માટે જે સૌથી મહત્વપૂર્ણ છે તેના પર જ ધ્યાન કેન્દ્રિત કરે છે."
    ))

    chapter = {
        "metadata": {
            "title": "Exploration: Entering the World of Secondary Science",
            "subject": "Science",
            "grade": "9",
            "curriculum": ["NCERT", "CBSE"],
            "difficulty": "Beginner",
            "version": "4.0.0",
            "id": chapter_id
        },
        "blocks": blocks
    }

    with open('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class9_science_ch1.json', 'w', encoding='utf-8') as f:
        json.dump(chapter, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_chapter()
    print("Successfully generated ncert_class9_science_ch1.json")
