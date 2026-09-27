import json
import os

blocks = []

def add_subtopic(id_prefix, title_en, title_hi, title_gu, content_en, content_hi, content_gu):
    # Step 1: Hook
    blocks.append({
        "id": f"{id_prefix}_STEP1_HOOK",
        "type": "theory",
        "title": "Step 1: Hook",
        "title_hi": "कदम 1: हुक (Step 1: Hook)",
        "title_gu": "પગલું 1: હૂક",
        "body": f"Have you ever wondered about: {title_en}?",
        "body_hi": f"क्या आपने कभी इसके बारे में सोचा है: {title_hi}?",
        "body_gu": f"શું તમે ક્યારેય આના વિશે વિચાર્યું છે: {title_gu}?"
    })
    # Step 2: Socratic Thinking
    blocks.append({
        "id": f"{id_prefix}_STEP2_SOCRATIC",
        "type": "socratic",
        "title": "Step 2: Socratic Thinking",
        "title_hi": "कदम 2: सुकराती सोच (Step 2: Socratic Thinking)",
        "title_gu": "પગલું 2: સોક્રેટીસ વિચાર",
        "question": f"Why do you think {title_en} affects unemployment?",
        "question_hi": f"आपको क्यों लगता है कि {title_hi} बेरोजगारी को प्रभावित करता है?",
        "question_gu": f"તમને કેમ લાગે છે કે {title_gu} બેરોજગારીને અસર કરે છે?",
        "options": ["It increases jobs", "It decreases jobs", "No effect", "Depends on factors"],
        "options_hi": ["यह नौकरियां बढ़ाता है", "यह नौकरियां कम करता है", "कोई प्रभाव नहीं", "कारकों पर निर्भर करता है"],
        "options_gu": ["તે નોકરીઓ વધારે છે", "તે નોકરીઓ ઘટાડે છે", "કોઈ અસર નથી", "પરિબળો પર આધાર રાખે છે"],
        "correct_index": 1,
        "explanation": "Let us explore why this happens.",
        "explanation_hi": "आइए जानें कि ऐसा क्यों होता है।",
        "explanation_gu": "ચાલો જોઈએ કે આવું કેમ થાય છે."
    })
    # Step 3: Discovery
    blocks.append({
        "id": f"{id_prefix}_STEP3_DISCOVERY",
        "type": "theory",
        "title": "Step 3: Discovery",
        "title_hi": "कदम 3: खोज (Step 3: Discovery)",
        "title_gu": "પગલું 3: શોધ",
        "body": f"Imagine a scenario where {title_en} is present. The resources are limited but demands are high.",
        "body_hi": f"एक ऐसे परिदृश्य की कल्पना करें जहाँ {title_hi} मौजूद है। संसाधन सीमित हैं लेकिन मांग अधिक है।",
        "body_gu": f"એવી પરિસ્થિતિની કલ્પના કરો જ્યાં {title_gu} હાજર હોય. સંસાધનો મર્યાદિત છે પરંતુ માંગ વધારે છે."
    })
    # Step 4: Reveal
    blocks.append({
        "id": f"{id_prefix}_STEP4_REVEAL",
        "type": "theory",
        "title": "Step 4: Reveal - " + title_en,
        "title_hi": "कदम 4: प्रकट - " + title_hi,
        "title_gu": "પગલું 4: પ્રગટ - " + title_gu,
        "body": content_en,
        "body_hi": content_hi,
        "body_gu": content_gu
    })
    # Step 5: Knowledge Check
    blocks.append({
        "id": f"{id_prefix}_STEP5_CHECK",
        "type": "mcq",
        "title": "Step 5: Knowledge Check",
        "title_hi": "कदम 5: ज्ञान की जांच (Step 5: Knowledge Check)",
        "title_gu": "પગલું 5: જ્ઞાન તપાસ",
        "question": f"According to the text, what is the main issue with {title_en}?",
        "question_hi": f"पाठ के अनुसार, {title_hi} के साथ मुख्य समस्या क्या है?",
        "question_gu": f"પાઠ મુજબ, {title_gu} ની મુખ્ય સમસ્યા શું છે?",
        "options": ["It increases labor supply beyond job opportunities", "It decreases labor supply", "It creates more capital", "None of the above"],
        "options_hi": ["यह नौकरी के अवसरों से परे श्रम आपूर्ति को बढ़ाता है", "यह श्रम आपूर्ति को कम करता है", "यह अधिक पूंजी बनाता है", "इनमें से कोई नहीं"],
        "options_gu": ["તે નોકરીની તકો કરતાં શ્રમ પુરવઠો વધારે છે", "તે શ્રમ પુરવઠો ઘટાડે છે", "તે વધુ મૂડી બનાવે છે", "ઉપરનામાંથી કોઈ નહીં"],
        "correct_index": 0,
        "explanation": "The main issue is the mismatch between supply and demand.",
        "explanation_hi": "मुख्य मुद्दा आपूर्ति और मांग के बीच बेमेल है।",
        "explanation_gu": "મુખ્ય મુદ્દો પુરવઠા અને માંગ વચ્ચેની અસમાનતા છે."
    })
    # Step 6: Reflection
    blocks.append({
        "id": f"{id_prefix}_STEP6_REFLECTION",
        "type": "reflection",
        "title": "Step 6: Reflection",
        "title_hi": "कदम 6: प्रतिबिंब (Step 6: Reflection)",
        "title_gu": "પગલું 6: પ્રતિબિંબ",
        "body": f"Reflect on how {title_en} affects your local community.",
        "body_hi": f"विचार करें कि {title_hi} आपके स्थानीय समुदाय को कैसे प्रभावित करता है।",
        "body_gu": f"{title_gu} તમારા સ્થાનિક સમુદાયને કેવી રીતે અસર કરે છે તે વિશે વિચારો."
    })
    # Step 7: Connection
    blocks.append({
        "id": f"{id_prefix}_STEP7_CONNECTION",
        "type": "theory",
        "title": "Step 7: Connection",
        "title_hi": "कदम 7: संबंध (Step 7: Connection)",
        "title_gu": "પગલું 7: જોડાણ",
        "body": f"This concept of {title_en} connects to broader macroeconomic principles like national income.",
        "body_hi": f"{title_hi} की यह अवधारणा राष्ट्रीय आय जैसे व्यापक मैक्रोइकॉनॉमिक सिद्धांतों से जुड़ती है।",
        "body_gu": f"{title_gu} નો આ ખ્યાલ રાષ્ટ્રીય આવક જેવા વ્યાપક મેક્રોઇકોનોમિક સિદ્ધાંતો સાથે જોડાય છે."
    })
    # Step 8: Mastery
    blocks.append({
        "id": f"{id_prefix}_STEP8_MASTERY",
        "type": "mcq",
        "title": "Step 8: Mastery",
        "title_hi": "कदम 8: महारत (Step 8: Mastery)",
        "title_gu": "પગલું 8: નિપુણતા",
        "question": f"Can you apply your understanding of {title_en} to suggest a policy change?",
        "question_hi": f"क्या आप नीतिगत बदलाव का सुझाव देने के लिए {title_hi} की अपनी समझ को लागू कर सकते हैं?",
        "question_gu": f"શું તમે નીતિમાં ફેરફાર સૂચવવા માટે {title_gu} ની તમારી સમજને લાગુ કરી શકો છો?",
        "options": ["Yes, by reducing supply or increasing demand", "No, it's impossible", "Only the government can think about it", "None"],
        "options_hi": ["हां, आपूर्ति कम करके या मांग बढ़ाकर", "नहीं, यह असंभव है", "केवल सरकार इसके बारे में सोच सकती है", "कोई नहीं"],
        "options_gu": ["હા, પુરવઠો ઘટાડીને અથવા માંગ વધારીને", "ના, તે અશક્ય છે", "માત્ર સરકાર આના વિશે વિચારી શકે છે", "કોઈ નહીં"],
        "correct_index": 0,
        "explanation": "Applying economic concepts helps in policy making.",
        "explanation_hi": "आर्थिक अवधारणाओं को लागू करने से नीति निर्माण में मदद मिलती है।",
        "explanation_gu": "આર્થિક ખ્યાલો લાગુ કરવાથી નીતિ ઘડવામાં મદદ મળે છે."
    })

# Add topics
add_subtopic("KOBJ_CH6_3_1", 
             "High Rate of Population Growth", 
             "जनसंख्या वृद्धि की उच्च दर (High Rate of Population Growth)", 
             "વસ્તી વૃદ્ધિનો ઉચ્ચ દર",
             "In India, size of population and high rate of population growth is noticed. Each year there is an increase in population by 1.70 crores.",
             "भारत में जनसंख्या का आकार और जनसंख्या वृद्धि की उच्च दर देखी गई है। हर साल जनसंख्या में 1.70 करोड़ की वृद्धि होती है।",
             "ભારતમાં વસ્તીનું કદ અને વસ્તી વૃદ્ધિનો ઊંચો દર જોવા મળે છે. દર વર્ષે વસ્તીમાં ૧.૭૦ કરોડનો વધારો થાય છે.")

add_subtopic("KOBJ_CH6_3_2",
             "Slow Rise in Employment Opportunities",
             "रोजगार के अवसरों में धीमी वृद्धि (Slow Rise in Employment Opportunities)",
             "રોજગારીની તકોમાં ધીમો વધારો",
             "Even after planned economic growth, opportunities cannot be created for old and new entrants. Economic growth has remained jobless growth.",
             "नियोजित आर्थिक विकास के बाद भी, रोजगार के अवसर पैदा नहीं किए जा सकते। आर्थिक विकास रोजगार विहीन विकास बना हुआ है।",
             "આયોજિત આર્થિક વિકાસ પછી પણ રોજગારીની તકો ઉભી થઈ શકતી નથી. આર્થિક વિકાસ રોજગાર વિહીન વિકાસ રહ્યો છે.")

add_subtopic("KOBJ_CH6_3_3",
             "Low rate of Savings and Investments",
             "बचत और निवेश की कम दर (Low rate of Savings and Investments)",
             "બચત અને રોકાણનો નીચો દર",
             "Due to low per capita income and expenses in satisfying basic needs, savings and investments are at a lower rate, leading to fewer jobs.",
             "कम प्रति व्यक्ति आय और बुनियादी जरूरतों को पूरा करने में खर्च के कारण, बचत और निवेश कम दर पर हैं, जिससे कम नौकरियां पैदा होती हैं।",
             "માથાદીઠ આવક ઓછી હોવાને કારણે અને પાયાની જરૂરિયાતો સંતોષવામાં થતા ખર્ચને કારણે, બચત અને રોકાણ નીચા દરે છે, જેનાથી ઓછી નોકરીઓ ઊભી થાય છે.")

add_subtopic("KOBJ_CH6_3_4",
             "Capital Intensive Production Technique",
             "पूंजी गहन उत्पादन तकनीक (Capital Intensive Production Technique)",
             "મૂડી પ્રધાન ઉત્પાદન પદ્ધતિ",
             "There is scarcity of capital and abundance of labour, but India adopted capital intensive techniques, saving labour and increasing unemployment.",
             "भारत में पूंजी की कमी और श्रम की प्रचुरता है, लेकिन भारत ने पूंजी गहन तकनीकों को अपनाया, जिससे श्रम की बचत हुई और बेरोजगारी बढ़ी।",
             "ભારતમાં મૂડીની અછત છે અને શ્રમ વિપુલ પ્રમાણમાં છે, પરંતુ ભારતે મૂડી પ્રધાન પદ્ધતિ અપનાવી છે, જે શ્રમ બચાવે છે અને બેરોજગારી વધારે છે.")

add_subtopic("KOBJ_CH6_3_5",
             "Lack of Vocational Education",
             "व्यावसायिक शिक्षा का अभाव (Lack of Vocational Education)",
             "વ્યાવસાયિક શિક્ષણનો અભાવ",
             "Present education system does not create skilled labourers required by modern technology, leading to high educational unemployment.",
             "वर्तमान शिक्षा प्रणाली आधुनिक तकनीक के लिए आवश्यक कुशल मजदूर नहीं बनाती है, जिससे शैक्षिक बेरोजगारी बढ़ती है।",
             "વર્તમાન શિક્ષણ પ્રણાલી આધુનિક ટેકનોલોજી માટે જરૂરી કુશળ શ્રમિકો તૈયાર કરતી નથી, જેના કારણે શૈક્ષણિક બેરોજગારી વધે છે.")

add_subtopic("KOBJ_CH6_3_6",
             "Lack of Manpower Planning",
             "जनशक्ति नियोजन का अभाव (Lack of Manpower Planning)",
             "માનવશક્તિ આયોજનનો અભાવ",
             "Education is widespread without estimating the kind and number of labour requirements, resulting in educated but unemployed youth and brain drain.",
             "श्रम आवश्यकताओं के प्रकार और संख्या का अनुमान लगाए बिना शिक्षा व्यापक है, जिसके परिणामस्वरूप शिक्षित लेकिन बेरोजगार युवा और ब्रेन ड्रेन होता है।",
             "શ્રમની જરૂરિયાતોના પ્રકાર અને સંખ્યાનો અંદાજ લગાવ્યા વિના શિક્ષણ વ્યાપક છે, જેના પરિણામે શિક્ષિત પરંતુ બેરોજગાર યુવાનો અને બ્રેન ડ્રેઇન થાય છે.")

add_subtopic("KOBJ_CH6_3_7",
             "Inefficiency of Public Sector",
             "सार्वजनिक क्षेत्र की अकुशलता (Inefficiency of Public Sector)",
             "જાહેર ક્ષેત્રની બિનકાર્યક્ષમતા",
             "Public sector was given importance but had low productivity and generated less employment than estimated, while private sector was neglected.",
             "सार्वजनिक क्षेत्र को महत्व दिया गया लेकिन उत्पादकता कम थी और अनुमान से कम रोजगार पैदा हुआ, जबकि निजी क्षेत्र की उपेक्षा की गई।",
             "જાહેર ક્ષેત્રને મહત્વ આપવામાં આવ્યું હતું પરંતુ ઉત્પાદકતા ઓછી હતી અને અંદાજ કરતાં ઓછી રોજગારી ઊભી થઈ હતી, જ્યારે ખાનગી ક્ષેત્રની અવગણના કરવામાં આવી હતી.")

add_subtopic("KOBJ_CH6_3_8",
             "Negligence Towards Agriculture Sector",
             "कृषि क्षेत्र की ओर लापरवाही (Negligence Towards Agriculture Sector)",
             "કૃષિ ક્ષેત્ર તરફની ઉપેક્ષા",
             "Agriculture was given less importance despite most people depending on it. Lack of irrigation and finance led to seasonal and disguised unemployment.",
             "अधिकांश लोगों के इस पर निर्भर होने के बावजूद कृषि को कम महत्व दिया गया। सिंचाई और वित्त की कमी के कारण मौसमी और प्रच्छन्न बेरोजगारी हुई।",
             "મોટાભાગના લોકો તેના પર નિર્ભર હોવા છતાં કૃષિને ઓછું મહત્વ આપવામાં આવ્યું. સિંચાઈ અને નાણાંના અભાવે મોસમી અને પ્રચ્છન્ન બેરોજગારી સર્જી.")

add_subtopic("KOBJ_CH6_3_9",
             "Low Mobility of Workers",
             "श्रमिकों की कम गतिशीलता (Low Mobility of Workers)",
             "શ્રમિકોની ઓછી ગતિશીલતા",
             "Social reasons, language, casteism, and attraction to urban life restrain mobilization of laborers to rural or backward areas where jobs might exist.",
             "सामाजिक कारण, भाषा, जातिवाद और शहरी जीवन के प्रति आकर्षण मजदूरों को ग्रामीण या पिछड़े क्षेत्रों में जाने से रोकते हैं जहाँ नौकरियां हो सकती हैं।",
             "સામાજિક કારણો, ભાષા, જ્ઞાતિવાદ અને શહેરી જીવન પ્રત્યેનું આકર્ષણ શ્રમિકોને ગ્રામીણ અથવા પછાત વિસ્તારોમાં જતા રોકે છે જ્યાં નોકરીઓ હોઈ શકે છે.")

add_subtopic("KOBJ_CH6_3_10",
             "Lack of Infrastructural Facilities",
             "बुनियादी सुविधाओं का अभाव (Lack of Infrastructural Facilities)",
             "માળખાગત સુવિધાઓનો અભાવ",
             "Lack of transportation, proper roads, education, health, and continuous electricity in rural areas discourages industries, leading to unemployment.",
             "ग्रामीण क्षेत्रों में परिवहन, उचित सड़कों, शिक्षा, स्वास्थ्य और निरंतर बिजली की कमी उद्योगों को हतोत्साहित करती है, जिससे बेरोजगारी होती है।",
             "ગ્રામીણ વિસ્તારોમાં પરિવહન, યોગ્ય રસ્તાઓ, શિક્ષણ, આરોગ્ય અને સતત વીજળીનો અભાવ ઉદ્યોગોને નિરાશ કરે છે, જેનાથી બેરોજગારી વધે છે.")

os.makedirs("/home/ubuntu/.gemini/antigravity/brain/82ecb053-41c8-4fb0-b2e6-b70d6b65ebfd/scratch", exist_ok=True)
with open("/home/ubuntu/.gemini/antigravity/brain/82ecb053-41c8-4fb0-b2e6-b70d6b65ebfd/scratch/part2.json", "w", encoding="utf-8") as f:
    json.dump(blocks, f, ensure_ascii=False, indent=2)

print("Done")
