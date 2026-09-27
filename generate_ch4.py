import json
import os

def tr(en, hi, gu):
    return {"en": en, "hi": hi, "gu": gu}

# --- LEARN CONTENT ---
learn_blocks = []

learn_blocks.append({
    "id": "KOBJ_CLASS10_ENG_CH4_HOOK",
    "type": "theory",
    "title": "Hook: The Power of a Diary",
    "title_hi": "हुक: डायरी की शक्ति",
    "title_gu": "હૂક: ડાયરીની શક્તિ",
    "body": "Have you ever felt like you have so much to say, but no one to truly listen? Imagine being completely alone with your thoughts in a crowded world. What if a simple paper notebook could become your best friend?",
    "body_hi": "क्या आपने कभी महसूस किया है कि आपके पास कहने को बहुत कुछ है, लेकिन सच में सुनने वाला कोई नहीं है? भीड़ भरी दुनिया में अपने विचारों के साथ पूरी तरह से अकेले होने की कल्पना करें। क्या होगा अगर एक साधारण कागज की नोटबुक आपका सबसे अच्छा दोस्त बन जाए?",
    "body_gu": "શું તમે ક્યારેય એવું અનુભવ્યું છે કે તમારી પાસે કહેવા માટે ઘણું બધું છે, પણ ખરેખર સાંભળવા વાળું કોઈ નથી? ભીડવાળી દુનિયામાં તમારા વિચારો સાથે સંપૂર્ણપણે એકલા હોવાની કલ્પના કરો. જો એક સામાન્ય કાગળની નોટબુક તમારી શ્રેષ્ઠ મિત્ર બની જાય તો શું?"
})

learn_blocks.append({
    "id": "KOBJ_CLASS10_ENG_CH4_SOCRATIC",
    "type": "theory",
    "title": "Socratic Thinking",
    "title_hi": "सुकराती सोच",
    "title_gu": "સોક્રેટીક વિચારસરણી",
    "body": "Why do you think people write diaries? Is it just to record events, or does it serve a deeper psychological purpose? Can a piece of paper have more patience than a human being?",
    "body_hi": "आपको क्यों लगता है कि लोग डायरी लिखते हैं? क्या यह केवल घटनाओं को रिकॉर्ड करने के लिए है, या यह किसी गहरे मनोवैज्ञानिक उद्देश्य को पूरा करता है? क्या कागज के एक टुकड़े में इंसान से ज्यादा धैर्य हो सकता है?",
    "body_gu": "તમને કેમ લાગે છે કે લોકો ડાયરી લખે છે? શું તે માત્ર ઘટનાઓ નોંધવા માટે છે, કે પછી તેનો કોઈ ઊંડો મનોવૈજ્ઞાનિક હેતુ છે? શું કાગળના ટુકડામાં માણસ કરતાં વધુ ધીરજ હોઈ શકે?"
})

learn_blocks.append({
    "id": "KOBJ_CLASS10_ENG_CH4_DISCOVERY",
    "type": "theory",
    "title": "Discovery: Anne Frank's World",
    "title_hi": "खोज: ऐनी फ्रैंक की दुनिया",
    "title_gu": "શોધ: એની ફ્રેન્કની દુનિયા",
    "body": "Let's discover the world of Anne Frank, a 13-year-old Jewish girl hiding from the Nazis in World War II. She had a loving family and friends, yet she felt lonely. She decided to confide in a diary she named 'Kitty'.",
    "body_hi": "आइए ऐनी फ्रैंक की दुनिया की खोज करें, जो द्वितीय विश्व युद्ध में नाजियों से छिपकर रह रही एक 13 वर्षीय यहूदी लड़की थी। उसका एक प्यारा परिवार और दोस्त थे, फिर भी वह अकेलापन महसूस करती थी। उसने 'किट्टी' नाम की एक डायरी से अपने दिल की बात कहने का फैसला किया।",
    "body_gu": "ચાલો એની ફ્રેન્કની દુનિયાની શોધ કરીએ, એક 13 વર્ષની યહૂદી છોકરી જે બીજા વિશ્વયુદ્ધમાં નાઝીઓથી છુપાઈને રહેતી હતી. તેનો એક પ્રેમાળ પરિવાર અને મિત્રો હતા, છતાં તે એકલતા અનુભવતી હતી. તેણે 'કિટ્ટી' નામની ડાયરીમાં પોતાના મનની વાત કહેવાનું નક્કી કર્યું."
})

learn_blocks.append({
    "id": "KOBJ_CLASS10_ENG_CH4_REVEAL",
    "type": "theory",
    "title": "Reveal: The Diary Entries",
    "title_hi": "प्रकटीकरण: डायरी प्रविष्टियाँ",
    "title_gu": "પ્રકટીકરણ: ડાયરીની નોંધો",
    "body": "Anne starts her diary by giving a brief sketch of her life, explaining that 'paper has more patience than people'. She writes about her class 'quaking in its boots' over upcoming results, and her amusing conflict with her math teacher, Mr. Keesing, who punishes her for talking by assigning essays on being a 'Chatterbox'. Through clever arguments and poetry, she outsmarts him.",
    "body_hi": "ऐनी अपने जीवन का एक संक्षिप्त रेखाचित्र देकर अपनी डायरी शुरू करती है, और बताती है कि 'कागज में लोगों की तुलना में अधिक धैर्य होता है'। वह अपनी कक्षा के बारे में लिखती है जो आगामी परिणामों को लेकर 'डर से कांप' रही है, और अपने गणित शिक्षक, मिस्टर कीसिंग के साथ अपने मनोरंजक संघर्ष के बारे में लिखती है, जो उसे बात करने के लिए 'चैटरबॉक्स' (बातूनी) पर निबंध लिखने की सजा देते हैं। चतुर तर्कों और कविता के माध्यम से, वह उन्हें मात देती है।",
    "body_gu": "એની તેના જીવનનું સંક્ષિપ્ત ચિત્ર આપીને તેની ડાયરી શરૂ કરે છે, અને સમજાવે છે કે 'કાગળમાં લોકો કરતા વધુ ધીરજ હોય છે'. તે તેના વર્ગ વિશે લખે છે જે આવનારા પરિણામોને કારણે 'ડરથી ધ્રૂજી' રહ્યો છે, અને તેના ગણિત શિક્ષક, મિસ્ટર કીસિંગ સાથેના તેના રમુજી સંઘર્ષ વિશે લખે છે, જે તેને વાતો કરવા બદલ 'ચેટરબોક્સ' (વાતોડિયું) પર નિબંધ લખવાની સજા આપે છે. ચતુર દલીલો અને કવિતા દ્વારા, તે તેમને મ્હાત આપે છે."
})

learn_blocks.append({
    "id": "KOBJ_CLASS10_ENG_CH4_POEM",
    "type": "theory",
    "title": "Amanda! (Poem)",
    "title_hi": "अमांडा! (कविता)",
    "title_gu": "અમાન્ડા! (કવિતા)",
    "body": "The poem 'Amanda!' by Robin Klein explores a child's desire for freedom. Amanda is constantly instructed by her parents (don't bite nails, sit up straight, do homework). In response, she escapes into her imagination, dreaming of being a mermaid, an orphan, or Rapunzel, just to find peace and silence.",
    "body_hi": "रॉबिन क्लेन की कविता 'अमांडा!' एक बच्चे की स्वतंत्रता की इच्छा का पड़ताल करती है। अमांडा को उसके माता-पिता द्वारा लगातार निर्देश दिए जाते हैं (नाखून मत काटो, सीधे बैठो, होमवर्क करो)। इसके जवाब में, वह अपनी कल्पना में भाग जाती है, केवल शांति और मौन पाने के लिए एक जलपरी, एक अनाथ या रॅपन्ज़ेल होने का सपना देखती है।",
    "body_gu": "રોબિન ક્લેઇનની કવિતા 'અમાન્ડા!' બાળકની સ્વતંત્રતાની ઇચ્છાની તપાસ કરે છે. અમાન્ડાને તેના માતાપિતા દ્વારા સતત સૂચના આપવામાં આવે છે (નખ ન કરડવા, સીધા બેસવું, હોમવર્ક કરવું). તેના જવાબમાં, તે તેની કલ્પનામાં ભાગી જાય છે, માત્ર શાંતિ અને મૌન શોધવા માટે મરમેઇડ, અનાથ અથવા રાપુન્ઝેલ બનવાનું સ્વપ્ન જુએ છે."
})

learn_blocks.append({
    "id": "KOBJ_CLASS10_ENG_CH4_REFLECTION",
    "type": "theory",
    "title": "Reflection",
    "title_hi": "प्रतिबिंब",
    "title_gu": "પ્રતિબિંબ",
    "body": "Think about Anne's situation and Amanda's situation. Anne lacks a true friend to confide in, while Amanda feels suffocated by constant instructions. How do both use writing or imagination as an escape?",
    "body_hi": "ऐनी की स्थिति और अमांडा की स्थिति के बारे में सोचें। ऐनी के पास अपने दिल की बात कहने के लिए कोई सच्चा दोस्त नहीं है, जबकि अमांडा लगातार निर्देशों से घुटन महसूस करती है। दोनों लिखने या कल्पना को एक बचाव के रूप में कैसे उपयोग करते हैं?",
    "body_gu": "એનીની પરિસ્થિતિ અને અમાન્ડાની પરિસ્થિતિ વિશે વિચારો. એની પાસે મનની વાત કહેવા માટે સાચો મિત્ર નથી, જ્યારે અમાન્ડા સતત સૂચનાઓથી ગૂંગળામણ અનુભવે છે. બંને લખવા કે કલ્પનાનો બચાવ તરીકે કેવી રીતે ઉપયોગ કરે છે?"
})


# --- PRACTICE CONTENT ---
questions = []
q_id_counter = 1

def add_subj(q_en, q_hi, q_gu, a_en, a_hi, a_gu):
    global q_id_counter
    questions.append({
        "id": f"KOBJ_CLASS10_ENG_CH4_Q{q_id_counter}",
        "type": "subjective",
        "question": q_en,
        "question_hi": q_hi,
        "question_gu": q_gu,
        "answer": a_en,
        "answer_hi": a_hi,
        "answer_gu": a_gu
    })
    q_id_counter += 1

def add_mcq(q_en, q_hi, q_gu, opts_en, opts_hi, opts_gu, correct_idx, exp_en, exp_hi, exp_gu):
    global q_id_counter
    questions.append({
        "id": f"KOBJ_CLASS10_ENG_CH4_Q{q_id_counter}",
        "type": "mcq",
        "question": q_en,
        "question_hi": q_hi,
        "question_gu": q_gu,
        "options": opts_en,
        "options_hi": opts_hi,
        "options_gu": opts_gu,
        "correct_index": correct_idx,
        "explanation": exp_en,
        "explanation_hi": exp_hi,
        "explanation_gu": exp_gu
    })
    q_id_counter += 1

# -- Oral Comprehension 1 --
add_subj("What makes writing in a diary a strange experience for Anne Frank?",
         "ऐनी फ्रैंक के लिए डायरी लिखना एक अजीब अनुभव क्यों है?",
         "એની ફ્રેન્ક માટે ડાયરી લખવી એ વિચિત્ર અનુભવ કેમ છે?",
         "Because she had never written anything before, and she doubted anyone would be interested in the musings of a thirteen-year-old.",
         "क्योंकि उसने पहले कभी कुछ नहीं लिखा था, और उसे संदेह था कि किसी को तेरह साल की लड़की के विचारों में दिलचस्पी होगी।",
         "કારણ કે તેણે પહેલાં ક્યારેય કંઈ લખ્યું ન હતું, અને તેને શંકા હતી કે કોઈને તેર વર્ષની છોકરીના વિચારોમાં રસ હશે.")

add_subj("Why does Anne want to keep a diary?",
         "ऐनी डायरी क्यों रखना चाहती है?",
         "એની ડાયરી કેમ રાખવા માંગે છે?",
         "She wants to keep a diary because she feels she has no true friend to whom she can confide her deepest feelings.",
         "वह डायरी रखना चाहती है क्योंकि उसे लगता है कि उसका कोई सच्चा दोस्त नहीं है जिससे वह अपनी गहरी भावनाओं को साझा कर सके।",
         "તે ડાયરી રાખવા માંગે છે કારણ કે તેને લાગે છે કે તેનો કોઈ સાચો મિત્ર નથી કે જેને તે પોતાની ઊંડી લાગણીઓ કહી શકે.")

add_mcq("Why did Anne think she could confide more in her diary than in people?",
        "ऐनी ने ऐसा क्यों सोचा कि वह लोगों की तुलना में अपनी डायरी पर अधिक भरोसा कर सकती है?",
        "એનીને કેમ લાગ્યું કે તે લોકો કરતાં તેની ડાયરીમાં વધુ વિશ્વાસ મૂકી શકે છે?",
        ["Paper is cheaper", "Paper has more patience than people", "She was deaf", "She had no family"],
        ["कागज सस्ता है", "कागज में लोगों से ज्यादा धैर्य होता है", "वह बहरी थी", "उसका कोई परिवार नहीं था"],
        ["કાગળ સસ્તો છે", "કાગળમાં લોકો કરતાં વધુ ધીરજ હોય છે", "તે બહેરી હતી", "તેનો કોઈ પરિવાર ન હતો"],
        1,
        "She believed the saying 'Paper has more patience than people.'",
        "वह कहावत में विश्वास करती थी 'कागज में लोगों की तुलना में अधिक धैर्य होता है।'",
        "તે કહેવતમાં માનતી હતી 'કાગળમાં લોકો કરતાં વધુ ધીરજ હોય છે.'")

# -- Oral Comprehension 2 --
add_subj("Why does Anne provide a brief sketch of her life?",
         "ऐनी अपने जीवन का संक्षिप्त विवरण क्यों देती है?",
         "એની તેના જીવનનો સંક્ષિપ્ત પરિચય કેમ આપે છે?",
         "To provide context, so no one would be confused if they read her diary entries abruptly.",
         "संदर्भ प्रदान करने के लिए, ताकि यदि कोई अचानक उसकी डायरी प्रविष्टियाँ पढ़े तो भ्रमित न हो।",
         "સંદર્ભ પ્રદાન કરવા માટે, જેથી જો કોઈ અચાનક તેની ડાયરીની નોંધો વાંચે તો મૂંઝવણમાં ન આવે.")

add_subj("What tells you that Anne loved her grandmother?",
         "आपको कैसे पता चलता है कि ऐनी अपनी दादी से प्यार करती थी?",
         "તમને કેવી રીતે ખબર પડે છે કે એની તેની દાદીને પ્રેમ કરતી હતી?",
         "She often thought of her after she died and even lit a special candle for her on her own birthday.",
         "उनके निधन के बाद भी वह अक्सर उनके बारे में सोचती थी और अपने जन्मदिन पर उनके लिए एक विशेष मोमबत्ती भी जलाई।",
         "તેમના અવસાન પછી પણ તે વારંવાર તેમના વિશે વિચારતી હતી અને પોતાના જન્મદિવસે તેમના માટે ખાસ મીણબત્તી પણ પ્રગટાવી હતી.")

# -- Oral Comprehension 3 --
add_subj("Why was Mr Keesing annoyed with Anne? What did he ask her to do?",
         "श्री कीसिंग ऐनी से नाराज़ क्यों थे? उन्होंने उसे क्या करने के लिए कहा?",
         "શ્રી કીસિંગ એનીથી કેમ નારાજ હતા? તેમણે તેને શું કરવાનું કહ્યું?",
         "He was annoyed because she talked too much. He asked her to write an essay on 'A Chatterbox'.",
         "वे इसलिए नाराज़ थे क्योंकि वह बहुत बात करती थी। उन्होंने उसे 'ए चैटरबॉक्स' पर निबंध लिखने को कहा।",
         "તેઓ નારાજ હતા કારણ કે તે ખૂબ વાતો કરતી હતી. તેમણે તેને 'એ ચેટરબોક્સ' પર નિબંધ લખવાનું કહ્યું.")

add_subj("How did Anne justify her being a chatterbox in her essay?",
         "ऐनी ने अपने निबंध में बातूनी होने को कैसे सही ठहराया?",
         "એનીએ તેના નિબંધમાં વાતોડિયું હોવાને કેવી રીતે વ્યાજબી ઠેરવ્યું?",
         "She argued it was a student's trait and an inherited trait from her mother.",
         "उसने तर्क दिया कि यह एक छात्र का लक्षण है और उसकी माँ से विरासत में मिला लक्षण है।",
         "તેણે દલીલ કરી કે તે એક વિદ્યાર્થીનું લક્ષણ છે અને તેની માતા તરફથી વારસામાં મળેલું લક્ષણ છે.")

add_mcq("Do you think Mr Keesing was a strict teacher?",
        "क्या आपको लगता है कि श्री कीसिंग एक सख्त शिक्षक थे?",
        "શું તમને લાગે છે કે શ્રી કીસિંગ કડક શિક્ષક હતા?",
        ["Yes, completely without humor", "He was strict but had a good sense of humor", "No, he never punished anyone", "He only taught poetry"],
        ["हां, पूरी तरह से बिना हास्य के", "वह सख्त थे लेकिन उनमें हास्य की अच्छी भावना थी", "नहीं, उन्होंने कभी किसी को सजा नहीं दी", "उन्होंने केवल कविता पढ़ाई"],
        ["હા, સંપૂર્ણપણે રમૂજ વિના", "તે કડક હતા પરંતુ તેમનામાં રમૂજની સારી ભાવના હતી", "ના, તેમણે ક્યારેય કોઈને સજા નથી કરી", "તેઓ માત્ર કવિતા ભણાવતા"],
        1,
        "He punished her, but laughed at her clever essays.",
        "उन्होंने उसे सजा दी, लेकिन उसके चतुर निबंधों पर हंसे भी।",
        "તેમણે તેને સજા કરી, પરંતુ તેના ચતુર નિબંધો પર હસ્યા પણ ખરા.")

add_subj("What made Mr Keesing allow Anne to talk in class?",
         "किस बात ने श्री कीसिंग को ऐनी को कक्षा में बात करने की अनुमति दी?",
         "કઈ બાબતે શ્રી કીસિંગને એનીને વર્ગમાં વાત કરવાની મંજૂરી આપી?",
         "Her poem about a father swan biting ducklings to death for quacking too much made him laugh.",
         "एक पिता हंस द्वारा अपने बत्तख के बच्चों को ज्यादा क्वैक करने पर मार डालने की उसकी कविता ने उन्हें हंसाया।",
         "વધુ ક્વેક કરવા બદલ પિતા હંસ દ્વારા પોતાના બતકના બચ્ચાને મારી નાખવાની તેની કવિતાએ તેમને હસાવ્યા.")

# -- Thinking about the Text --
add_subj("Was Anne right when she said that the world would not be interested in the musings of a thirteen-year-old girl?",
         "क्या ऐनी सही थी जब उसने कहा कि दुनिया को तेरह साल की लड़की के विचारों में दिलचस्पी नहीं होगी?",
         "શું એની સાચી હતી જ્યારે તેણે કહ્યું કે દુનિયાને તેર વર્ષની છોકરીના વિચારોમાં રસ નહીં હોય?",
         "No, she was completely wrong. Her diary became world-famous.",
         "नहीं, वह पूरी तरह से गलत थी। उसकी डायरी विश्व प्रसिद्ध हो गई।",
         "ના, તે સંપૂર્ણપણે ખોટી હતી. તેની ડાયરી વિશ્વ પ્રસિદ્ધ બની ગઈ.")

add_subj("There are some examples of diary or journal entries in the 'Before You Read' section. Compare these with what Anne writes in her diary. What language was the diary originally written in? In what way is Anne's diary different?",
         "ऐनी की डायरी मूल रूप से किस भाषा में लिखी गई थी? ऐनी की डायरी किस तरह से अलग है?",
         "એનીની ડાયરી મૂળ કઈ ભાષામાં લખાઈ હતી? એનીની ડાયરી કઈ રીતે અલગ છે?",
         "Originally in Dutch. Her diary is different because it's deeply personal and treats the diary as a real friend ('Kitty').",
         "मूल रूप से डच में। उसकी डायरी अलग है क्योंकि यह गहराई से व्यक्तिगत है और डायरी को एक असली दोस्त ('किट्टी') के रूप में मानती है।",
         "મૂળ ડચમાં. તેની ડાયરી અલગ છે કારણ કે તે ઊંડી વ્યક્તિગત છે અને ડાયરીને એક સાચા મિત્ર ('કિટ્ટી') તરીકે માને છે.")

add_subj("Why does Anne need to give a brief sketch about her family? Does she treat 'Kitty' as an insider or an outsider?",
         "ऐनी को अपने परिवार के बारे में एक संक्षिप्त रेखाचित्र देने की आवश्यकता क्यों है? क्या वह 'किट्टी' के साथ अंदरूनी सूत्र या बाहरी व्यक्ति के रूप में व्यवहार करती है?",
         "એનીએ તેના પરિવાર વિશે સંક્ષિપ્ત ચિત્ર આપવાની જરૂર શા માટે છે? શું તે 'કિટ્ટી'ને અંદરની કે બહારની વ્યક્તિ તરીકે ગણે છે?",
         "To give readers context. She treats 'Kitty' as an insider.",
         "पाठकों को संदर्भ देने के लिए। वह 'किट्टी' को एक अंदरूनी सूत्र मानती है।",
         "વાંચકોને સંદર્ભ આપવા માટે. તે 'કિટ્ટી' ને અંદરની વ્યક્તિ માને છે.")

add_subj("How does Anne feel about her father, her grandmother, Mrs Kuperus and Mr Keesing? What do these tell you about her?",
         "ऐनी अपने पिता, दादी, मिसेज कुपेरस और मिस्टर कीसिंग के बारे में कैसा महसूस करती है?",
         "એની તેના પિતા, દાદી, શ્રીમતી કુપેરસ અને શ્રી કીસિંગ વિશે કેવું અનુભવે છે?",
         "She loved her adorable father and grandmother. She was emotionally attached to Mrs Kuperus. She saw Mr Keesing as unpredictable but ultimately human. This shows she is observant and affectionate.",
         "वह अपने प्यारे पिता और दादी से प्यार करती थी। वह मिसेज कुपेरस से भावनात्मक रूप से जुड़ी हुई थी। वह मिस्टर कीसिंग को अप्रत्याशित लेकिन अंततः इंसान मानती थी। यह दर्शाता है कि वह चौकस और स्नेही है।",
         "તે તેના પ્રેમાળ પિતા અને દાદીને પ્રેમ કરતી હતી. તે શ્રીમતી કુપેરસ સાથે ભાવનાત્મક રીતે જોડાયેલી હતી. તે શ્રી કીસિંગને અણધારી પરંતુ છેવટે માનવ માનતી હતી. આ દર્શાવે છે કે તે સચેત અને પ્રેમાળ છે.")

add_subj("What does Anne write in her first essay?",
         "ऐनी अपने पहले निबंध में क्या लिखती है?",
         "એની તેના પહેલા નિબંધમાં શું લખે છે?",
         "She argues that talking is a student's trait and that she inherited it from her mother.",
         "वह तर्क देती है कि बात करना एक छात्र का लक्षण है और उसने इसे अपनी माँ से विरासत में पाया है।",
         "તે દલીલ કરે છે કે વાત કરવી એ વિદ્યાર્થીનું લક્ષણ છે અને તેણે તે તેની માતા પાસેથી વારસામાં મેળવ્યું છે.")

add_subj("Anne says teachers are most unpredictable. Is Mr Keesing unpredictable? How?",
         "ऐनी कहती है कि शिक्षक सबसे अप्रत्याशित होते हैं। क्या मिस्टर कीसिंग अप्रत्याशित हैं? कैसे?",
         "એની કહે છે કે શિક્ષકો સૌથી અણધાર્યા હોય છે. શું શ્રી કીસિંગ અણધાર્યા છે? કેવી રીતે?",
         "Yes. First, he punished her, but later accepted her joke and stopped punishing her, which she didn't expect.",
         "हाँ। पहले उन्होंने उसे सज़ा दी, लेकिन बाद में उसके मज़ाक को स्वीकार कर लिया और सज़ा देना बंद कर दिया, जिसकी उसे उम्मीद नहीं थी।",
         "હા. પહેલા તેમણે તેને સજા આપી, પરંતુ પછીથી તેની મજાક સ્વીકારી લીધી અને સજા આપવાનું બંધ કર્યું, જેની તેને અપેક્ષા નહોતી.")

add_subj("What do these statements tell you about Anne Frank as a person? (i) We don't seem to be able to get any closer...",
         "ये कथन ऐनी फ्रैंक के बारे में एक व्यक्ति के रूप में क्या बताते हैं? (i) हम करीब नहीं आ पा रहे हैं...",
         "આ વિધાનો એની ફ્રેન્ક વિશે વ્યક્તિ તરીકે શું કહે છે? (i) અમે નજીક આવી શકતા નથી...",
         "It shows she felt lonely and lacked a true confidant despite having friends.",
         "यह दर्शाता है कि दोस्त होने के बावजूद वह अकेलापन महसूस करती थी और उसके पास एक सच्चा हमराज़ नहीं था।",
         "તે દર્શાવે છે કે મિત્રો હોવા છતાં તે એકલતા અનુભવતી હતી અને તેનો કોઈ સાચો વિશ્વાસુ ન હતો.")

add_subj("What do these statements tell you about Anne Frank? (ii) I don't want to jot down facts... I want the diary to be my friend.",
         "(ii) मैं केवल तथ्य नहीं लिखना चाहती... मैं चाहती हूं कि डायरी मेरी दोस्त बने।",
         "(ii) હું માત્ર તથ્યો લખવા નથી માંગતી... હું ઈચ્છું છું કે ડાયરી મારી મિત્ર બને.",
         "It shows she is imaginative and values emotional connection over just recording events.",
         "यह दर्शाता है कि वह कल्पनाशील है और केवल घटनाओं को रिकॉर्ड करने के बजाय भावनात्मक जुड़ाव को महत्व देती है।",
         "તે દર્શાવે છે કે તે કલ્પનાશીલ છે અને માત્ર ઘટનાઓ નોંધવાને બદલે ભાવનાત્મક જોડાણને મહત્વ આપે છે.")

add_subj("What do these statements tell you about Anne Frank? (iii) Margot went to Holland in December... plunked down on the table.",
         "(iii) मार्गोट दिसंबर में हॉलैंड गई... मेज पर रख दी गई।",
         "(iii) માર્ગોટ ડિસેમ્બરમાં હોલેન્ડ ગઈ... ટેબલ પર મૂકવામાં આવી.",
         "It shows her sense of humor and slightly self-deprecating wit.",
         "यह उसकी हास्य की भावना और थोड़ा आत्म-हीनता वाला मज़ाक दर्शाता है।",
         "તે તેની રમૂજની ભાવના અને થોડી આત્મ-અવમૂલ્યનવાળી બુદ્ધિ દર્શાવે છે.")

add_subj("What do these statements tell you about Anne? (iv) If you ask me, there are so many dummies...",
         "(iv) अगर आप मुझसे पूछें, तो बहुत से डमी (बेवकूफ) हैं...",
         "(iv) જો તમે મને પૂછો, તો ઘણા બધા ડમી (મૂર્ખ) છે...",
         "It shows she is opinionated, confident, and observant of her classmates.",
         "यह दर्शाता है कि वह मुखर, आत्मविश्वासी और अपने सहपाठियों को ध्यान से देखने वाली है।",
         "તે દર્શાવે છે કે તે મક્કમ, આત્મવિશ્વાસુ અને તેના સહપાઠીઓનું નિરીક્ષણ કરનારી છે.")

add_subj("What do these statements tell you about Anne? (v) Anyone could ramble on... but the trick was to come up with convincing arguments.",
         "(v) कोई भी बकवास कर सकता है... लेकिन असली चाल आश्वस्त करने वाले तर्क देना था।",
         "(v) કોઈ પણ બકવાસ કરી શકે છે... પરંતુ સાચી યુક્તિ પ્રતીતિકર દલીલો આપવી હતી.",
         "It shows she is intelligent, takes assignments seriously, and wants to prove a point rather than just fill pages.",
         "यह दर्शाता है कि वह बुद्धिमान है, असाइनमेंट को गंभीरता से लेती है, और केवल पन्ने भरने के बजाय एक बात साबित करना चाहती है।",
         "તે દર્શાવે છે કે તે બુદ્ધિશાળી છે, અસાઇનમેન્ટને ગંભીરતાથી લે છે અને માત્ર પાના ભરવાને બદલે કંઈક સાબિત કરવા માંગે છે.")

# -- Thinking about Language --
# Compound Words (Matchings as MCQs)
add_mcq("Match the meaning for 'Heartbreaking':",
        "'Heartbreaking' के लिए अर्थ मिलाएँ:",
        "'Heartbreaking' માટે અર્થ મેળવો:",
        ["producing great sadness", "obeying the law", "stupid person", "excessive degree"],
        ["बहुत दुःख पैदा करने वाला", "कानून का पालन", "मूर्ख व्यक्ति", "अत्यधिक सीमा"],
        ["ખૂબ ઉદાસી પેદા કરનાર", "કાયદાનું પાલન", "મૂર્ખ વ્યક્તિ", "વધુ પડતી મર્યાદા"],
        0, "", "", "")

add_mcq("Match the meaning for 'Homesick':",
        "'Homesick' के लिए अर्थ मिलाएँ:",
        "'Homesick' માટે અર્થ મેળવો:",
        ["missing home and family very much", "produced by a machine", "respecting the law", "vehicles stop working"],
        ["घर और परिवार को बहुत याद करना", "मशीन द्वारा निर्मित", "कानून का सम्मान", "वाहन काम करना बंद कर देते हैं"],
        ["ઘર અને પરિવારને ખૂબ યાદ કરવું", "મશીન દ્વારા ઉત્પાદિત", "કાયદાનું સન્માન", "વાહનો કામ કરતા બંધ થાય છે"],
        0, "", "", "")

add_mcq("Match the meaning for 'Blockhead':",
        "'Blockhead' के लिए अर्थ मिलाएँ:",
        "'Blockhead' માટે અર્થ મેળવો:",
        ["missing home", "very stupid person", "great sadness", "output"],
        ["घर की याद", "बहुत बेवकूफ व्यक्ति", "बड़ा दुख", "उत्पादन"],
        ["ઘરની યાદ", "ખૂબ મૂર્ખ વ્યક્તિ", "મોટું દુઃખ", "ઉત્પાદન"],
        1, "", "", "")

add_mcq("Match the meaning for 'Law-abiding':",
        "'Law-abiding' के लिए अर्थ मिलाएँ:",
        "'Law-abiding' માટે અર્થ મેળવો:",
        ["producing great sadness", "obeying and respecting the law", "excessive degree", "forgetting the present"],
        ["बड़ा दुख पैदा करना", "कानून का पालन करना और सम्मान करना", "अत्यधिक सीमा", "वर्तमान को भूल जाना"],
        ["મોટું દુઃખ પેદા કરવું", "કાયદાનું પાલન અને સન્માન કરવું", "વધુ પડતી મર્યાદા", "વર્તમાનને ભૂલી જવું"],
        1, "", "", "")

add_mcq("Match the meaning for 'Overdo':",
        "'Overdo' के लिए अर्थ मिलाएँ:",
        "'Overdo' માટે અર્થ મેળવો:",
        ["vehicles stop working", "do something to an excessive degree", "stupid person", "obeying the law"],
        ["वाहन काम करना बंद कर देते हैं", "किसी काम को अत्यधिक करना", "मूर्ख व्यक्ति", "कानून का पालन"],
        ["વાહનો કામ કરતા બંધ થાય છે", "કોઈ કામને વધુ પડતું કરવું", "મૂર્ખ વ્યક્તિ", "કાયદાનું પાલન"],
        1, "", "", "")

add_mcq("Match the meaning for 'Daydream':",
        "'Daydream' के लिए अर्थ मिलाएँ:",
        "'Daydream' માટે અર્થ મેળવો:",
        ["missing home", "obeying law", "think about pleasant things, forgetting the present", "producing sadness"],
        ["घर की याद", "कानून का पालन", "मनभावन चीजों के बारे में सोचना, वर्तमान को भूल जाना", "दुख पैदा करना"],
        ["ઘરની યાદ", "કાયદાનું પાલન", "આનંદદાયક વસ્તુઓ વિશે વિચારવું, વર્તમાનને ભૂલી જવું", "દુઃખ પેદા કરવું"],
        2, "", "", "")

add_mcq("Match the meaning for 'Breakdown':",
        "'Breakdown' के लिए अर्थ मिलाएँ:",
        "'Breakdown' માટે અર્થ મેળવો:",
        ["an occasion when vehicles/machines stop working", "missing home", "stupid person", "pleasant thoughts"],
        ["एक अवसर जब वाहन/मशीन काम करना बंद कर देते हैं", "घर की याद", "मूर्ख व्यक्ति", "सुखद विचार"],
        ["એક પ્રસંગ જ્યારે વાહનો/મશીનો કામ કરવાનું બંધ કરે છે", "ઘરની યાદ", "મૂર્ખ વ્યક્તિ", "સુખદ વિચારો"],
        0, "", "", "")

add_mcq("Match the meaning for 'Output':",
        "'Output' के लिए अर्थ मिलाएँ:",
        "'Output' માટે અર્થ મેળવો:",
        ["excessive work", "sadness", "something produced by a person, machine or organisation", "forgetting the present"],
        ["अत्यधिक काम", "उदासी", "किसी व्यक्ति, मशीन या संगठन द्वारा उत्पादित कुछ", "वर्तमान को भूल जाना"],
        ["વધુ પડતું કામ", "ઉદાસી", "કોઈ વ્યક્તિ, મશીન અથવા સંસ્થા દ્વારા ઉત્પાદિત કંઈક", "વર્તમાનને ભૂલી જવું"],
        2, "", "", "")

# Phrasal Verbs
add_mcq("What is the meaning of the phrasal verb 'plunge in'?",
        "Phrasal verb 'plunge in' का क्या अर्थ है?",
        "Phrasal verb 'plunge in' નો અર્થ શું છે?",
        ["go straight to the topic", "stay indoors", "make quiet", "not promoted"],
        ["सीधे विषय पर जाना", "घर के अंदर रहना", "चुप करना", "प्रमोशन नहीं हुआ"],
        ["સીધા વિષય પર જવું", "ઘરની અંદર રહેવું", "ચુપ કરવું", "પ્રમોશન નથી થયું"],
        0, "", "", "")

add_mcq("What is the meaning of the phrasal verb 'kept back'?",
        "Phrasal verb 'kept back' का क्या अर्थ है?",
        "Phrasal verb 'kept back' નો અર્થ શું છે?",
        ["compensate", "not promoted", "have a good relationship", "stay indoors"],
        ["क्षतिपूर्ति करना", "प्रमोशन नहीं हुआ", "अच्छा रिश्ता होना", "घर के अंदर रहना"],
        ["વળતર આપવું", "પ્રમોશન નથી થયું", "સારો સંબંધ હોવો", "ઘરની અંદર રહેવું"],
        1, "", "", "")

add_mcq("What is the meaning of the phrasal verb 'move up'?",
        "Phrasal verb 'move up' का क्या अर्थ है?",
        "Phrasal verb 'move up' નો અર્થ શું છે?",
        ["go to the next grade", "compensate", "stay indoors", "speak without focus"],
        ["अगली कक्षा में जाना", "क्षतिपूर्ति करना", "घर के अंदर रहना", "बिना फोकस के बोलना"],
        ["આગલા ધોરણમાં જવું", "વળતર આપવું", "ઘરની અંદર રહેવું", "ધ્યાન વગર બોલવું"],
        0, "", "", "")

add_mcq("What is the meaning of the phrasal verb 'ramble on'?",
        "Phrasal verb 'ramble on' का क्या अर्थ है?",
        "Phrasal verb 'ramble on' નો અર્થ શું છે?",
        ["give an assignment", "speak or write without focus", "make them remain quiet", "compensate"],
        ["असाइनमेंट देना", "बिना फोकस के बोलना या लिखना", "उन्हें चुप रहने देना", "क्षतिपूर्ति करना"],
        ["અસાઇનમેન્ટ આપવું", "ધ્યાન વગર બોલવું કે લખવું", "તેમને શાંત રાખવા", "વળતર આપવું"],
        1, "", "", "")

add_mcq("What is the meaning of the phrasal verb 'get along with'?",
        "Phrasal verb 'get along with' का क्या अर्थ है?",
        "Phrasal verb 'get along with' નો અર્થ શું છે?",
        ["go straight to the topic", "have a good relationship with", "not promoted", "compensate"],
        ["सीधे विषय पर जाना", "के साथ अच्छे संबंध होना", "प्रमोशन नहीं हुआ", "क्षतिपूर्ति करना"],
        ["સીધા વિષય પર જવું", "સાથે સારો સંબંધ હોવો", "પ્રમોશન નથી થયું", "વળતર આપવું"],
        1, "", "", "")

add_mcq("What is the meaning of the phrasal verb 'calm down'?",
        "Phrasal verb 'calm down' का क्या अर्थ है?",
        "Phrasal verb 'calm down' નો અર્થ શું છે?",
        ["make (them) remain quiet", "go to the next grade", "stay indoors", "speak without focus"],
        ["(उन्हें) शांत करना", "अगली कक्षा में जाना", "घर के अंदर रहना", "बिना फोकस के बोलना"],
        ["(તેમને) શાંત કરવા", "આગલા ધોરણમાં જવું", "ઘરની અંદર રહેવું", "ધ્યાન વગર બોલવું"],
        0, "", "", "")

add_mcq("What is the meaning of the phrasal verb 'stay in'?",
        "Phrasal verb 'stay in' का क्या अर्थ है?",
        "Phrasal verb 'stay in' નો અર્થ શું છે?",
        ["stay indoors", "not promoted", "have a good relationship", "give an assignment"],
        ["घर के अंदर रहना", "प्रमोशन नहीं हुआ", "अच्छा रिश्ता होना", "असाइनमेंट देना"],
        ["ઘરની અંદર રહેવું", "પ્રમોશન નથી થયું", "સારો સંબંધ હોવો", "અસાઇનમેન્ટ આપવું"],
        0, "", "", "")

add_mcq("What is the meaning of the phrasal verb 'make up for'?",
        "Phrasal verb 'make up for' का क्या अर्थ है?",
        "Phrasal verb 'make up for' નો અર્થ શું છે?",
        ["compensate", "not promoted", "go straight to the topic", "speak without focus"],
        ["क्षतिपूर्ति करना", "प्रमोशन नहीं हुआ", "सीधे विषय पर जाना", "बिना फोकस के बोलना"],
        ["વળતર આપવું", "પ્રમોશન નથી થયું", "સીધા વિષય પર જવું", "ધ્યાન વગર બોલવું"],
        0, "", "", "")

add_mcq("What is the meaning of the phrasal verb 'hand in'?",
        "Phrasal verb 'hand in' का क्या अर्थ है?",
        "Phrasal verb 'hand in' નો અર્થ શું છે?",
        ["give an assignment (homework) to a person in authority", "make them remain quiet", "stay indoors", "compensate"],
        ["अधिकारी को असाइनमेंट (होमवर्क) देना", "उन्हें शांत रखना", "घर के अंदर रहना", "क्षतिपूर्ति करना"],
        ["અધિકારીને અસાઇનમેન્ટ (હોમવર્ક) આપવું", "તેમને શાંત રાખવા", "ઘરની અંદર રહેવું", "વળતર આપવું"],
        0, "", "", "")

# Idioms
add_mcq("What is the meaning of the idiom 'quaking in its boots'?",
        "मुहावरे 'quaking in its boots' का क्या अर्थ है?",
        "રૂઢિપ્રયોગ 'quaking in its boots' નો અર્થ શું છે?",
        ["very happy", "shaking with fear and nervousness", "walking fast", "feeling warm"],
        ["बहुत खुश", "डर और घबराहट से कांपना", "तेज चलना", "गर्म महसूस करना"],
        ["ખૂબ ખુશ", "ડર અને ગભરામણથી ધ્રૂજવું", "ઝડપથી ચાલવું", "ગરમ અનુભવવું"],
        1, "", "", "")

add_mcq("What is the meaning of the idiom 'not to lose heart'?",
        "मुहावरे 'not to lose heart' का क्या अर्थ है?",
        "રૂઢિપ્રયોગ 'not to lose heart' નો અર્થ શું છે?",
        ["to get heart disease", "not to lose hope", "to find someone", "to lose a game"],
        ["हृदय रोग होना", "उम्मीद नहीं खोना", "किसी को खोजना", "खेल हारना"],
        ["હૃદય રોગ થવો", "આશા ન ગુમાવવી", "કોઈને શોધવું", "રમત હારવી"],
        1, "", "", "")

add_mcq("What is the meaning of the idiom 'for ages'?",
        "मुहावरे 'for ages' का क्या अर्थ है?",
        "રૂઢિપ્રયોગ 'for ages' નો અર્થ શું છે?",
        ["for old people", "for a long time", "for the future", "for a short time"],
        ["बूढ़े लोगों के लिए", "लंबे समय के लिए", "भविष्य के लिए", "थोड़े समय के लिए"],
        ["વૃદ્ધ લોકો માટે", "લાંબા સમય માટે", "ભવિષ્ય માટે", "થોડા સમય માટે"],
        1, "", "", "")

add_mcq("What is the meaning of the idiom 'the joke was on him'?",
        "मुहावरे 'the joke was on him' का क्या अर्थ है?",
        "રૂઢિપ્રયોગ 'the joke was on him' નો અર્થ શું છે?",
        ["he made a joke", "he would be the one laughed at", "he liked jokes", "the joke was bad"],
        ["उसने मजाक किया", "वह वह होगा जिस पर हंसा जाएगा", "उसे चुटकुले पसंद थे", "मजाक बुरा था"],
        ["તેણે મજાક કરી", "તે એવો હશે જેના પર હસવામાં આવશે", "તેને ટુચકાઓ ગમતા", "મજાક ખરાબ હતી"],
        1, "", "", "")

# Contracted forms
add_subj("Make a list of the contracted forms in the text.",
         "पाठ में अनुबंधित रूपों (contracted forms) की एक सूची बनाएं।",
         "પાઠમાં ટૂંકા સ્વરૂપો (contracted forms) ની યાદી બનાવો.",
         "I've, doesn't, I'm, won't, don't, can't, that's, it's, they're, I'd, who'll, we'll, who's, you're.",
         "I've, doesn't, I'm, won't, don't, can't, that's, it's, they're, I'd, who'll, we'll, who's, you're.",
         "I've, doesn't, I'm, won't, don't, can't, that's, it's, they're, I'd, who'll, we'll, who's, you're.")

add_subj("Find contracted forms that stand for two different full forms.",
         "उन अनुबंधित रूपों को खोजें जो दो अलग-अलग पूर्ण रूपों के लिए हैं।",
         "એવા ટૂંકા સ્વરૂપો શોધો જે બે અલગ અલગ પૂર્ણ સ્વરૂપો માટે વપરાય છે.",
         "I'd (I had or I would), he'd (he had or he would).",
         "I'd (I had या I would), he'd (he had या he would).",
         "I'd (I had અથવા I would), he'd (he had અથવા he would).")

# Poem Amanda Questions
add_subj("How old do you think Amanda is? How do you know this?",
         "आपको क्या लगता है अमांडा की उम्र क्या होगी? आपको यह कैसे पता चला?",
         "તમને શું લાગે છે અમાન્ડાની ઉંમર કેટલી હશે? તમને આ કેવી રીતે ખબર પડી?",
         "Amanda is likely a pre-teen or teenager (10-14). We know this because of references to homework, acne, and her rebellious sulking.",
         "अमांडा संभवतः पूर्व-किशोर या किशोरी (10-14) है। हम यह जानते हैं क्योंकि होमवर्क, मुँहासे और उसके विद्रोही रूप से रूठने के संदर्भ हैं।",
         "અમાન્ડા સંભવતઃ પ્રી-ટીન અથવા કિશોરવયની (10-14) છે. આપણે આ જાણીએ છીએ કારણ કે હોમવર્ક, ખીલ અને તેના બળવાખોર રીતે રિસાવાના સંદર્ભો છે.")

add_subj("Who do you think is speaking to her?",
         "आपको क्या लगता है कि उससे कौन बात कर रहा है?",
         "તમને શું લાગે છે કે તેની સાથે કોણ વાત કરી રહ્યું છે?",
         "One of her parents, mostly likely her mother, is speaking to her.",
         "उसके माता-पिता में से कोई एक, संभवतः उसकी माँ, उससे बात कर रही है।",
         "તેના માતાપિતામાંથી એક, સંભવતઃ તેની માતા, તેની સાથે વાત કરી રહી છે.")

add_subj("Why are Stanzas 2, 4 and 6 given in parenthesis?",
         "श्लोक 2, 4 और 6 को कोष्ठक (parenthesis) में क्यों दिया गया है?",
         "પંક્તિઓ 2, 4 અને 6 ને કૌંસમાં શા માટે આપવામાં આવી છે?",
         "They represent Amanda's inner thoughts and daydreams, contrasting with the outer reality of her parent's instructions.",
         "वे अमांडा के आंतरिक विचारों और दिवास्वप्नों का प्रतिनिधित्व करते हैं, जो उसके माता-पिता के निर्देशों की बाहरी वास्तविकता के विपरीत हैं।",
         "તેઓ અમાન્ડાના આંતરિક વિચારો અને દિવાસ્વપ્નોનું પ્રતિનિધિત્વ કરે છે, જે તેના માતાપિતાની સૂચનાઓની બાહ્ય વાસ્તવિકતાથી વિપરીત છે.")

add_subj("Who is the speaker in Stanzas 2, 4 and 6? Do you think this speaker is listening to the speaker in Stanzas 1, 3, 5, and 7?",
         "श्लोक 2, 4 और 6 में वक्ता कौन है? क्या आपको लगता है कि यह वक्ता 1, 3, 5 और 7 में वक्ता को सुन रहा है?",
         "પંક્તિઓ 2, 4 અને 6 માં વક્તા કોણ છે? શું તમને લાગે છે કે આ વક્તા પંક્તિઓ 1, 3, 5 અને 7 માં વક્તાને સાંભળી રહ્યો છે?",
         "The speaker is Amanda herself in her imagination. She is not listening to the parent; she is lost in her daydreams.",
         "वक्ता अपनी कल्पना में स्वयं अमांडा है। वह माता-पिता की बात नहीं सुन रही है; वह अपने ख्यालों में खोई है।",
         "વક્તા પોતાની કલ્પનામાં સ્વયં અમાન્ડા છે. તે માતાપિતાની વાત સાંભળી રહી નથી; તે પોતાના દિવાસ્વપ્નોમાં ખોવાયેલી છે.")

add_mcq("What could Amanda do if she were a mermaid?",
        "अगर अमांडा जलपरी होती तो वह क्या कर सकती थी?",
        "જો અમાન્ડા મરમેઇડ હોત તો તે શું કરી શકત?",
        ["Fly in the sky", "Drift blissfully on a languid emerald sea", "Eat chocolate", "Play with friends"],
        ["आकाश में उड़ना", "शांत पन्ना समुद्र पर आनंदपूर्वक तैरना", "चॉकलेट खाना", "दोस्तों के साथ खेलना"],
        ["આકાશમાં ઉડવું", "શાંત નીલમણિ સમુદ્ર પર આનંદથી તરવું", "ચોકલેટ ખાવી", "મિત્રો સાથે રમવું"],
        1, "", "", "")

add_subj("Is Amanda an orphan? Why does she say so?",
         "क्या अमांडा अनाथ है? वह ऐसा क्यों कहती है?",
         "શું અમાન્ડા અનાથ છે? તે એવું શા માટે કહે છે?",
         "No, she is not an orphan. She says so because she wishes she were alone and free to roam the streets without constant nagging.",
         "नहीं, वह अनाथ नहीं है। वह ऐसा इसलिए कहती है क्योंकि वह चाहती है कि वह अकेली हो और बिना किसी लगातार रोक-टोक के सड़कों पर घूमने के लिए स्वतंत्र हो।",
         "ના, તે અનાથ નથી. તે એવું એટલા માટે કહે છે કારણ કે તે ઈચ્છે છે કે તે એકલી હોય અને સતત ટોક્યા વિના શેરીઓમાં ફરવા માટે મુક્ત હોય.")

add_subj("Do you know the story of Rapunzel? Why does she want to be Rapunzel?",
         "क्या आप रॅपन्ज़ेल की कहानी जानते हैं? वह रॅपन्ज़ेल क्यों बनना चाहती है?",
         "શું તમે રાપુન્ઝેલની વાર્તા જાણો છો? તે રાપુન્ઝેલ કેમ બનવા માંગે છે?",
         "Rapunzel lived alone in a tall tower. Amanda wants to be Rapunzel to live a peaceful, tranquil life in a tower away from everyone. Unlike Rapunzel, she would never let her hair down for anyone to climb up.",
         "रॅपन्ज़ेल एक ऊंची मीनार में अकेली रहती थी। अमांडा रॅपन्ज़ेल बनना चाहती है ताकि वह सबसे दूर एक मीनार में शांतिपूर्ण जीवन जी सके। रॅपन्ज़ेल के विपरीत, वह किसी को ऊपर चढ़ने के लिए अपने बाल कभी नीचे नहीं करेगी।",
         "રાપુન્ઝેલ એક ઊંચા ટાવરમાં એકલી રહેતી હતી. અમાન્ડા રાપુન્ઝેલ બનવા માંગે છે જેથી તે બધાથી દૂર ટાવરમાં શાંતિપૂર્ણ જીવન જીવી શકે. રાપુન્ઝેલથી વિપરીત, તે કોઈને ઉપર ચઢવા માટે ક્યારેય તેના વાળ નીચે નહીં કરે.")

add_subj("What does the girl yearn for? What does this poem tell you about Amanda?",
         "लड़की किस चीज की लालसा करती है? यह कविता आपको अमांडा के बारे में क्या बताती है?",
         "છોકરી શેની ઝંખના કરે છે? આ કવિતા તમને અમાન્ડા વિશે શું કહે છે?",
         "She yearns for freedom, peace, and silence. It tells us that Amanda feels suffocated by constant instructions and escapes into imagination.",
         "वह स्वतंत्रता, शांति और मौन के लिए तरसती है। यह हमें बताता है कि अमांडा लगातार निर्देशों से घुटन महसूस करती है और कल्पना में भाग जाती है।",
         "તે સ્વતંત્રતા, શાંતિ અને મૌન ઝંખે છે. તે આપણને કહે છે કે અમાન્ડા સતત સૂચનાઓથી ગૂંગળામણ અનુભવે છે અને કલ્પનામાં ભાગી જાય છે.")

add_subj("Read the last stanza. Do you think Amanda is sulking and is moody?",
         "अंतिम श्लोक पढ़ें। क्या आपको लगता है कि अमांडा रूठ रही है और मूडी है?",
         "છેલ્લી પંક્તિઓ વાંચો. શું તમને લાગે છે કે અમાન્ડા રિસાઈ ગઈ છે અને મૂડી છે?",
         "Amanda is likely just ignoring her parent and lost in thought, which the parent interprets as sulking and being moody.",
         "अमांडा संभवतः अपने माता-पिता को अनदेखा कर रही है और सोच में खोई हुई है, जिसे माता-पिता रूठना और मूडी होना मानते हैं।",
         "અમાન્ડા કદાચ તેના માતાપિતાની અવગણના કરી રહી છે અને વિચારમાં ખોવાઈ ગઈ છે, જેને માતાપિતા રિસાઈ જવું અને મૂડી હોવાનું માને છે.")

# Make sure to dump
os.makedirs("/home/ubuntu/Shine_Academy_Naroda/app_core/chapters", exist_ok=True)
os.makedirs("/home/ubuntu/Shine_Academy_Naroda/app_core/assessment", exist_ok=True)

with open("/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch4.json", "w", encoding="utf-8") as f:
    json.dump(learn_blocks, f, ensure_ascii=False, indent=2)

with open("/home/ubuntu/Shine_Academy_Naroda/app_core/assessment/gseb_class10_english_ch4_questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("All JSON files generated successfully with exhaustive question inclusion.")
