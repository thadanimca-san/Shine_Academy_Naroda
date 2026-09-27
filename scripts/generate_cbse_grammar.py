import os
import json

CHAPTERS_DIR = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
os.makedirs(CHAPTERS_DIR, exist_ok=True)

def create_mcq(id_str, q, q_hi, q_gu, opts, opts_hi, opts_gu, ans_idx, expl, expl_hi, expl_gu):
    return {
        "id": id_str,
        "type": "mcq",
        "question": q,
        "question_hi": q_hi,
        "question_gu": q_gu,
        "options": opts,
        "options_hi": opts_hi,
        "options_gu": opts_gu,
        "correct_index": ans_idx,
        "explanation": expl,
        "explanation_hi": expl_hi,
        "explanation_gu": expl_gu
    }

# 30 high-quality MCQs for Tenses with full translations
tenses_base = [
    # 1-5 Simple Present
    (
        "He _______ (go) to the gym every morning.", "वह हर सुबह जिम _______ (go) है।", "તે દરરોજ સવારે જિમ _______ (go) છે.",
        "goes", "is going", "went", "has gone",
        "goes", "is going", "went", "has gone",
        "goes", "is going", "went", "has gone",
        0,
        "Daily habit uses simple present.", "दैनिक आदत में सामान्य वर्तमान (Simple Present) का प्रयोग होता है।", "રોજિંદી આદતમાં સાદા વર્તમાનકાળનો ઉપયોગ થાય છે."
    ),
    (
        "The sun _______ (rise) in the east.", "सूर्य पूर्व में _______ (rise) है।", "સૂર્ય પૂર્વમાં _______ (rise) છે.",
        "rises", "is rising", "rose", "has risen",
        "rises", "is rising", "rose", "has risen",
        "rises", "is rising", "rose", "has risen",
        0,
        "Universal truth uses simple present.", "सार्वभौमिक सत्य में सामान्य वर्तमान का प्रयोग होता है।", "સાર્વત્રિક સત્યમાં સાદા વર્તમાનકાળનો ઉપયોગ થાય છે."
    ),
    (
        "Water _______ (boil) at 100 degrees Celsius.", "पानी 100 डिग्री सेल्सियस पर _______ (boil) है।", "પાણી 100 ડિગ્રી સેલ્સિયસ પર _______ (boil) છે.",
        "boils", "is boiling", "boiled", "will boil",
        "boils", "is boiling", "boiled", "will boil",
        "boils", "is boiling", "boiled", "will boil",
        0,
        "Scientific fact uses simple present.", "वैज्ञानिक तथ्य के लिए सामान्य वर्तमान का प्रयोग होता है।", "વૈજ્ઞાનિક તથ્ય માટે સાદા વર્તમાનકાળનો ઉપયોગ થાય છે."
    ),
    (
        "She always _______ (forget) her keys.", "वह हमेशा अपनी चाबियाँ _______ (forget) है।", "તે હંમેશા તેની ચાવીઓ _______ (forget) છે.",
        "forgets", "is forgetting", "forgot", "has forgotten",
        "forgets", "is forgetting", "forgot", "has forgotten",
        "forgets", "is forgetting", "forgot", "has forgotten",
        0,
        "Habitual action uses simple present.", "आदतन क्रिया के लिए सामान्य वर्तमान का प्रयोग होता है।", "આદત મુજબની ક્રિયા માટે સાદા વર્તમાનકાળનો ઉપયોગ થાય છે."
    ),
    (
        "I usually _______ (wake) up at 6 AM.", "मैं आमतौर पर सुबह 6 बजे _______ (wake) हूँ।", "હું સામાન્ય રીતે સવારે 6 વાગ્યે _______ (wake) છું.",
        "wake", "wakes", "woke", "am waking",
        "wake", "wakes", "woke", "am waking",
        "wake", "wakes", "woke", "am waking",
        0,
        "Routine uses simple present base form for 'I'.", "'I' के साथ दिनचर्या के लिए क्रिया के मूल रूप (base form) का उपयोग होता है।", "'I' સાથે દિનચર્યા માટે ક્રિયાપદના મૂળ સ્વરૂપનો ઉપયોગ થાય છે."
    ),
    
    # 6-10 Present Continuous
    (
        "Look! The bus _______ (come).", "देखो! बस _______ (come)।", "જુઓ! બસ _______ (come).",
        "is coming", "comes", "came", "has come",
        "is coming", "comes", "came", "has come",
        "is coming", "comes", "came", "has come",
        0,
        "Happening right now uses present continuous.", "अभी हो रही क्रिया के लिए वर्तमान निरंतर (Present Continuous) का प्रयोग होता है।", "અત્યારે થઈ રહેલી ક્રિયા માટે ચાલુ વર્તમાનકાળનો ઉપયોગ થાય છે."
    ),
    (
        "Please be quiet; the baby _______ (sleep).", "कृपया शांत रहें; बच्चा _______ (sleep)।", "કૃપા કરીને શાંત રહો; બાળક _______ (sleep).",
        "is sleeping", "sleeps", "slept", "has slept",
        "is sleeping", "sleeps", "slept", "has slept",
        "is sleeping", "sleeps", "slept", "has slept",
        0,
        "Ongoing action in the present.", "वर्तमान में जारी क्रिया।", "વર્તમાનમાં ચાલુ ક્રિયા."
    ),
    (
        "They _______ (play) football at the moment.", "वे इस समय फुटबॉल _______ (play)।", "તેઓ આ ક્ષણે ફૂટબોલ _______ (play).",
        "are playing", "play", "played", "were playing",
        "are playing", "play", "played", "were playing",
        "are playing", "play", "played", "were playing",
        0,
        "Action happening at the time of speaking.", "बोलते समय हो रही क्रिया।", "બોલતી વખતે થઈ રહેલી ક્રિયા."
    ),
    (
        "I _______ (read) a really interesting book these days.", "मैं इन दिनों एक बहुत ही दिलचस्प किताब _______ (read)।", "હું આ દિવસોમાં એક ખૂબ જ રસપ્રદ પુસ્તક _______ (read).",
        "am reading", "read", "have read", "was reading",
        "am reading", "read", "have read", "was reading",
        "am reading", "read", "have read", "was reading",
        0,
        "Temporary ongoing action.", "अस्थायी रूप से जारी क्रिया।", "અસ્થાયી રૂપે ચાલુ ક્રિયા."
    ),
    (
        "Why _______ you _______ (cry)?", "तुम क्यों _______ (cry)?", "તમે શા માટે _______ (cry)?",
        "are / crying", "do / cry", "did / cry", "have / cried",
        "are / crying", "do / cry", "did / cry", "have / cried",
        "are / crying", "do / cry", "did / cry", "have / cried",
        0,
        "Present continuous for current state.", "वर्तमान स्थिति के लिए वर्तमान निरंतर।", "વર્તમાન સ્થિતિ માટે ચાલુ વર્તમાનકાળ."
    ),

    # 11-15 Present Perfect
    (
        "I _______ (just / finish) my homework.", "मैंने _______ (just / finish) अपना होमवर्क।", "મેં _______ (just / finish) મારું હોમવર્ક.",
        "have just finished", "just finished", "am just finishing", "had just finished",
        "have just finished", "just finished", "am just finishing", "had just finished",
        "have just finished", "just finished", "am just finishing", "had just finished",
        0,
        "Action recently completed with 'just'.", "'just' के साथ हाल ही में पूरी हुई क्रिया।", "'just' સાથે તાજેતરમાં પૂર્ણ થયેલ ક્રિયા."
    ),
    (
        "She _______ (never / visit) Paris.", "उसने _______ (never / visit) पेरिस।", "તેણે _______ (never / visit) પેરિસ.",
        "has never visited", "never visits", "never visited", "had never visited",
        "has never visited", "never visits", "never visited", "had never visited",
        "has never visited", "never visits", "never visited", "had never visited",
        0,
        "Life experience up to now uses present perfect.", "अब तक के जीवन के अनुभव के लिए पूर्ण वर्तमान (Present Perfect) का प्रयोग होता है।", "અત્યાર સુધીના જીવનના અનુભવ માટે પૂર્ણ વર્તમાનકાળનો ઉપયોગ થાય છે."
    ),
    (
        "We _______ (live) in this city for ten years.", "हम दस साल से इस शहर में _______ (live)।", "અમે દસ વર્ષથી આ શહેરમાં _______ (live).",
        "have lived", "live", "are living", "were living",
        "have lived", "live", "are living", "were living",
        "have lived", "live", "are living", "were living",
        0,
        "Action started in past and continuing to present.", "अतीत में शुरू हुई और वर्तमान तक जारी क्रिया।", "ભૂતકાળમાં શરૂ થયેલી અને વર્તમાન સુધી ચાલુ ક્રિયા."
    ),
    (
        "_______ you ever _______ (eat) sushi?", "क्या तुमने कभी सुशी _______ (eat)?", "શું તમે ક્યારેય સુશી _______ (eat)?",
        "Have / eaten", "Did / eat", "Do / eat", "Are / eating",
        "Have / eaten", "Did / eat", "Do / eat", "Are / eating",
        "Have / eaten", "Did / eat", "Do / eat", "Are / eating",
        0,
        "Asking about life experience.", "जीवन के अनुभव के बारे में पूछना।", "જીવનના અનુભવ વિશે પૂછવું."
    ),
    (
        "The train _______ (already / leave).", "ट्रेन _______ (already / leave)।", "ટ્રેન _______ (already / leave).",
        "has already left", "already left", "is already leaving", "had already left",
        "has already left", "already left", "is already leaving", "had already left",
        "has already left", "already left", "is already leaving", "had already left",
        0,
        "Completed action with present relevance.", "वर्तमान प्रासंगिकता के साथ पूरी हुई क्रिया।", "વર્તમાન સુસંગતતા સાથે પૂર્ણ થયેલ ક્રિયા."
    ),

    # 16-20 Simple Past
    (
        "I _______ (visit) my grandparents last weekend.", "मैंने पिछले सप्ताहांत अपने दादा-दादी से _______ (visit)।", "મેં ગયા સપ્તાહમાં મારા દાદા-દાદીની _______ (visit).",
        "visited", "visit", "have visited", "was visiting",
        "visited", "visit", "have visited", "was visiting",
        "visited", "visit", "have visited", "was visiting",
        0,
        "Completed action in the past with specific time.", "विशिष्ट समय के साथ अतीत में पूरी हुई क्रिया।", "ચોક્કસ સમય સાથે ભૂતકાળમાં પૂર્ણ થયેલ ક્રિયા."
    ),
    (
        "She _______ (buy) a new car yesterday.", "उसने कल एक नई कार _______ (buy)।", "તેણે ગઈકાલે એક નવી કાર _______ (buy).",
        "bought", "buys", "has bought", "is buying",
        "bought", "buys", "has bought", "is buying",
        "bought", "buys", "has bought", "is buying",
        0,
        "'Yesterday' indicates simple past.", "'Yesterday' सामान्य भूतकाल (Simple Past) को दर्शाता है।", "'Yesterday' સાદો ભૂતકાળ દર્શાવે છે."
    ),
    (
        "World War II _______ (end) in 1945.", "द्वितीय विश्व युद्ध 1945 में _______ (end)।", "બીજું વિશ્વ યુદ્ધ 1945 માં _______ (end).",
        "ended", "ends", "has ended", "was ending",
        "ended", "ends", "has ended", "was ending",
        "ended", "ends", "has ended", "was ending",
        0,
        "Historical event in the past.", "अतीत की ऐतिहासिक घटना।", "ભૂતકાળની ઐતિહાસિક ઘટના."
    ),
    (
        "When I was a child, I _______ (love) ice cream.", "जब मैं बच्चा था, मुझे आइसक्रीम _______ (love)।", "જ્યારે હું બાળક હતો, ત્યારે મને આઈસ્ક્રીમ _______ (love).",
        "loved", "love", "have loved", "am loving",
        "loved", "love", "have loved", "am loving",
        "loved", "love", "have loved", "am loving",
        0,
        "Past state or habit.", "पिछली स्थिति या आदत।", "ભૂતકાળની સ્થિતિ અથવા આદત."
    ),
    (
        "He _______ (not / see) the movie last night.", "उसने कल रात फिल्म _______ (not / see)।", "તેણે ગઈકાલે રાત્રે ફિલ્મ _______ (not / see).",
        "did not see", "has not seen", "does not see", "had not seen",
        "did not see", "has not seen", "does not see", "had not seen",
        "did not see", "has not seen", "does not see", "had not seen",
        0,
        "Negative simple past uses 'did not' + base verb.", "नकारात्मक सामान्य भूतकाल में 'did not' + मूल क्रिया का उपयोग होता है।", "નકારાત્મક સાદા ભૂતકાળમાં 'did not' + મૂળ ક્રિયાપદનો ઉપયોગ થાય છે."
    ),

    # 21-25 Past Continuous
    (
        "They _______ (play) soccer when it started raining.", "वे सॉकर _______ (play) जब बारिश शुरू हुई।", "તેઓ સોકર _______ (play) જ્યારે વરસાદ શરૂ થયો.",
        "were playing", "played", "are playing", "have played",
        "were playing", "played", "are playing", "have played",
        "were playing", "played", "are playing", "have played",
        0,
        "Past continuous interrupted by simple past.", "सामान्य भूतकाल द्वारा बाधित निरंतर भूतकाल।", "સાદા ભૂતકાળ દ્વારા વિક્ષેપિત ચાલુ ભૂતકાળ."
    ),
    (
        "I _______ (watch) TV at 8 PM last night.", "मैं कल रात 8 बजे टीवी _______ (watch)।", "હું ગઈકાલે રાત્રે 8 વાગ્યે ટીવી _______ (watch).",
        "was watching", "watched", "am watching", "have watched",
        "was watching", "watched", "am watching", "have watched",
        "was watching", "watched", "am watching", "have watched",
        0,
        "Ongoing action at a specific time in the past.", "अतीत में एक विशिष्ट समय पर चल रही क्रिया।", "ભૂતકાળમાં ચોક્કસ સમયે ચાલુ ક્રિયા."
    ),
    (
        "While she _______ (read), her phone rang.", "जब वह _______ (read), उसका फोन बजा।", "જ્યારે તે _______ (read), ત્યારે તેનો ફોન વાગ્યો.",
        "was reading", "reads", "read", "is reading",
        "was reading", "reads", "read", "is reading",
        "was reading", "reads", "read", "is reading",
        0,
        "Ongoing action in the past with 'while'.", "'while' के साथ अतीत में चल रही क्रिया।", "'while' સાથે ભૂતકાળમાં ચાલુ ક્રિયા."
    ),
    (
        "We _______ (sleep) when the earthquake happened.", "हम _______ (sleep) जब भूकंप आया।", "અમે _______ (sleep) જ્યારે ભૂકંપ આવ્યો.",
        "were sleeping", "slept", "are sleeping", "have slept",
        "were sleeping", "slept", "are sleeping", "have slept",
        "were sleeping", "slept", "are sleeping", "have slept",
        0,
        "Interrupted past action.", "बाधित पिछली क्रिया।", "વિક્ષેપિત ભૂતકાળની ક્રિયા."
    ),
    (
        "What _______ you _______ (do) when I called you?", "तुम क्या _______ (do) जब मैंने तुम्हें बुलाया?", "તમે શું _______ (do) જ્યારે મેં તમને બોલાવ્યા?",
        "were / doing", "did / do", "are / doing", "have / done",
        "were / doing", "did / do", "are / doing", "have / done",
        "were / doing", "did / do", "are / doing", "have / done",
        0,
        "Question about past ongoing action.", "अतीत में चल रही क्रिया के बारे में प्रश्न।", "ભૂતકાળમાં ચાલુ ક્રિયા વિશે પ્રશ્ન."
    ),

    # 26-30 Past Perfect & Future
    (
        "I _______ (finish) my homework before the power went out.", "मैंने बिजली जाने से पहले अपना होमवर्क _______ (finish)।", "મેં લાઈટ જતાં પહેલાં મારું હોમવર્ક _______ (finish).",
        "had finished", "finished", "have finished", "was finishing",
        "had finished", "finished", "have finished", "was finishing",
        "had finished", "finished", "have finished", "was finishing",
        0,
        "Action completed before another past action.", "दूसरी पिछली क्रिया से पहले पूरी हुई क्रिया।", "બીજી ભૂતકાળની ક્રિયા પહેલાં પૂર્ણ થયેલ ક્રિયા."
    ),
    (
        "By the time we arrived, the movie _______ (already / start).", "जब तक हम पहुँचे, फिल्म _______ (already / start)।", "જ્યાં સુધી અમે પહોંચ્યા, ત્યાં સુધીમાં ફિલ્મ _______ (already / start).",
        "had already started", "already started", "has already started", "was already starting",
        "had already started", "already started", "has already started", "was already starting",
        "had already started", "already started", "has already started", "was already starting",
        0,
        "Past perfect for earlier past action.", "पहले की पिछली क्रिया के लिए पूर्ण भूतकाल (Past Perfect)।", "અગાઉની ભૂતકાળની ક્રિયા માટે પૂર્ણ ભૂતકાળ."
    ),
    (
        "I think it _______ (rain) tomorrow.", "मुझे लगता है कल बारिश _______ (rain)।", "મને લાગે છે કે આવતીકાલે વરસાદ _______ (rain).",
        "will rain", "rains", "is raining", "has rained",
        "will rain", "rains", "is raining", "has rained",
        "will rain", "rains", "is raining", "has rained",
        0,
        "Prediction about the future uses 'will'.", "भविष्य के बारे में भविष्यवाणी 'will' का उपयोग करती है।", "ભવિષ્ય વિશેની આગાહી 'will' નો ઉપયોગ કરે છે."
    ),
    (
        "By next year, I _______ (graduate) from university.", "अगले साल तक, मैं विश्वविद्यालय से _______ (graduate)।", "આવતા વર્ષ સુધીમાં, હું યુનિવર્સિટીમાંથી _______ (graduate).",
        "will have graduated", "will graduate", "am graduating", "graduate",
        "will have graduated", "will graduate", "am graduating", "graduate",
        "will have graduated", "will graduate", "am graduating", "graduate",
        0,
        "Action completed by a certain future time uses future perfect.", "भविष्य के एक निश्चित समय तक पूरी होने वाली क्रिया में पूर्ण भविष्य (Future Perfect) का उपयोग होता है।", "ભવિષ્યના ચોક્કસ સમય સુધીમાં પૂર્ણ થનારી ક્રિયામાં પૂર્ણ ભવિષ્યકાળનો ઉપયોગ થાય છે."
    ),
    (
        "Don't call me at 8 PM; I _______ (eat) dinner.", "मुझे रात 8 बजे कॉल मत करना; मैं रात का खाना _______ (eat)।", "મને રાત્રે 8 વાગ્યે કૉલ કરશો નહીં; હું રાત્રિભોજન _______ (eat).",
        "will be eating", "will eat", "eat", "am eating",
        "will be eating", "will eat", "eat", "am eating",
        "will be eating", "will eat", "eat", "am eating",
        0,
        "Ongoing future action uses future continuous.", "चल रही भविष्य की क्रिया में निरंतर भविष्य (Future Continuous) का उपयोग होता है।", "ચાલુ ભવિષ્યની ક્રિયામાં ચાલુ ભવિષ્યકાળનો ઉપયોગ થાય છે."
    )
]

grammar_ch1 = {
    "file": "cbse_class10_english_grammar_ch1.json",
    "blocks": [
        {
            "id": "KOBJ_GR10_CH1_HEADING",
            "type": "heading",
            "title": "Tenses: The Master Clock of English",
            "title_hi": "काल (Tenses): अंग्रेजी की मुख्य घड़ी",
            "title_gu": "કાળ (Tenses): અંગ્રેજીની મુખ્ય ઘડિયાળ"
        },
        {
            "id": "KOBJ_GR10_CH1_HOOK",
            "type": "hook",
            "title": "Time Travelers",
            "title_hi": "समय यात्री",
            "title_gu": "સમય યાત્રીઓ",
            "body": "Imagine watching a movie where the beginning, middle, and end all play at exactly the same time. It would be pure chaos! In English, verbs act as time travelers. They change their clothes (forms) to tell us exactly when an action happened. Without tenses, we wouldn't know if you are eating pizza right now, ate it yesterday, or will eat it tomorrow.",
            "body_hi": "कल्पना करें कि आप एक ऐसी फिल्म देख रहे हैं जहां शुरुआत, मध्य और अंत बिल्कुल एक ही समय पर चल रहे हों। यह पूरी तरह से अराजकता होगी! अंग्रेजी में, क्रियाएं (verbs) समय यात्रियों के रूप में कार्य करती हैं। वे हमें यह बताने के लिए अपने कपड़े (रूप) बदलते हैं कि कोई क्रिया ठीक कब हुई थी। काल (tenses) के बिना, हमें नहीं पता चलेगा कि आप अभी पिज्जा खा रहे हैं, कल खाया था, या कल खाएंगे।",
            "body_gu": "કલ્પના કરો કે તમે એવી ફિલ્મ જોઈ રહ્યા છો જ્યાં શરૂઆત, મધ્ય અને અંત બરાબર એક જ સમયે ચાલી રહ્યા હોય. તે સંપૂર્ણ અરાજકતા હશે! અંગ્રેજીમાં, ક્રિયાપદો (verbs) સમય યાત્રીઓ તરીકે કાર્ય કરે છે. તેઓ અમને બરાબર ક્યારે ક્રિયા થઈ તે જણાવવા માટે તેમના કપડાં (સ્વરૂપ) બદલે છે. કાળ (tenses) વિના, અમને ખબર નહીં પડે કે તમે અત્યારે પિઝા ખાઈ રહ્યા છો, ગઈકાલે ખાધો હતો, કે આવતીકાલે ખાશો."
        },
        {
            "id": "KOBJ_GR10_CH1_THEORY_1",
            "type": "theory",
            "title": "Present Tense Family",
            "title_hi": "वर्तमान काल परिवार",
            "title_gu": "વર્તમાન કાળ પરિવાર",
            "body": "1. Simple Present: Habits, routines, facts. (I play)\n2. Present Continuous: Happening right now. (I am playing)\n3. Present Perfect: Completed recently, or past experience connected to present. (I have played)\n4. Present Perfect Continuous: Started in past, still continuing. (I have been playing)",
            "body_hi": "1. सामान्य वर्तमान: आदतें, दिनचर्या, तथ्य। (I play)\n2. वर्तमान निरंतर: अभी हो रहा है। (I am playing)\n3. पूर्ण वर्तमान: हाल ही में पूरा हुआ, या वर्तमान से जुड़ा पिछला अनुभव। (I have played)\n4. पूर्ण निरंतर वर्तमान: अतीत में शुरू हुआ, अभी भी जारी है। (I have been playing)",
            "body_gu": "1. સાદો વર્તમાન: આદતો, દિનચર્યા, તથ્યો. (I play)\n2. ચાલુ વર્તમાન: અત્યારે થઈ રહ્યું છે. (I am playing)\n3. પૂર્ણ વર્તમાન: તાજેતરમાં પૂર્ણ થયું, અથવા વર્તમાન સાથે જોડાયેલો ભૂતકાળનો અનુભવ. (I have played)\n4. પૂર્ણ ચાલુ વર્તમાન: ભૂતકાળમાં શરૂ થયું, હજુ પણ ચાલુ છે. (I have been playing)"
        },
        {
            "id": "KOBJ_GR10_CH1_THEORY_2",
            "type": "theory",
            "title": "Past Tense Family",
            "title_hi": "भूतकाल परिवार",
            "title_gu": "ભૂતકાળ પરિવાર",
            "body": "1. Simple Past: Finished action at a specific time. (I played)\n2. Past Continuous: Ongoing action in the past. (I was playing)\n3. Past Perfect: The 'past of the past'. Completed before another past action. (I had played)\n4. Past Perfect Continuous: Ongoing action that ended before another past action. (I had been playing)",
            "body_hi": "1. सामान्य भूतकाल: एक विशिष्ट समय पर समाप्त क्रिया। (I played)\n2. निरंतर भूतकाल: अतीत में चल रही क्रिया। (I was playing)\n3. पूर्ण भूतकाल: 'अतीत का अतीत'। दूसरी पिछली क्रिया से पहले पूरा हुआ। (I had played)\n4. पूर्ण निरंतर भूतकाल: चल रही क्रिया जो दूसरी पिछली क्रिया से पहले समाप्त हो गई। (I had been playing)",
            "body_gu": "1. સાદો ભૂતકાળ: ચોક્કસ સમયે પૂર્ણ થયેલ ક્રિયા. (I played)\n2. ચાલુ ભૂતકાળ: ભૂતકાળમાં ચાલુ ક્રિયા. (I was playing)\n3. પૂર્ણ ભૂતકાળ: 'ભૂતકાળનો ભૂતકાળ'. બીજી ભૂતકાળની ક્રિયા પહેલાં પૂર્ણ. (I had played)\n4. પૂર્ણ ચાલુ ભૂતકાળ: ચાલુ ક્રિયા જે બીજી ભૂતકાળની ક્રિયા પહેલાં સમાપ્ત થઈ. (I had been playing)"
        },
        {
            "id": "KOBJ_GR10_CH1_THEORY_3",
            "type": "theory",
            "title": "Future Tense Family",
            "title_hi": "भविष्य काल परिवार",
            "title_gu": "ભવિષ્ય કાળ પરિવાર",
            "body": "1. Simple Future: Predictions, promises, instant decisions. (I will play)\n2. Future Continuous: Action that will be ongoing in the future. (I will be playing)\n3. Future Perfect: Action that will be completed by a certain future time. (I will have played)\n4. Future Perfect Continuous: Ongoing action up to a future point. (I will have been playing)",
            "body_hi": "1. सामान्य भविष्य: भविष्यवाणियां, वादे, तत्काल निर्णय। (I will play)\n2. निरंतर भविष्य: वह क्रिया जो भविष्य में जारी रहेगी। (I will be playing)\n3. पूर्ण भविष्य: वह क्रिया जो भविष्य के एक निश्चित समय तक पूरी हो जाएगी। (I will have played)\n4. पूर्ण निरंतर भविष्य: भविष्य के एक बिंदु तक चल रही क्रिया। (I will have been playing)",
            "body_gu": "1. સાદો ભવિષ્ય: આગાહીઓ, વચનો, ત્વરિત નિર્ણયો. (I will play)\n2. ચાલુ ભવિષ્ય: ભવિષ્યમાં ચાલુ રહેનારી ક્રિયા. (I will be playing)\n3. પૂર્ણ ભવિષ્ય: ચોક્કસ ભવિષ્યના સમય સુધીમાં પૂર્ણ થનારી ક્રિયા. (I will have played)\n4. પૂર્ણ ચાલુ ભવિષ્ય: ભવિષ્યના બિંદુ સુધી ચાલુ રહેતી ક્રિયા. (I will have been playing)"
        }
    ]
}

# Add the 30 MCQs for Tenses
for idx, mcq in enumerate(tenses_base):
    q_str, q_hi, q_gu = mcq[0], mcq[1], mcq[2]
    opt1, opt2, opt3, opt4 = mcq[3], mcq[4], mcq[5], mcq[6]
    opt1_hi, opt2_hi, opt3_hi, opt4_hi = mcq[7], mcq[8], mcq[9], mcq[10]
    opt1_gu, opt2_gu, opt3_gu, opt4_gu = mcq[11], mcq[12], mcq[13], mcq[14]
    ans_idx = mcq[15]
    expl, expl_hi, expl_gu = mcq[16], mcq[17], mcq[18]
    
    grammar_ch1["blocks"].append(create_mcq(
        f"KOBJ_GR10_CH1_MCQ_{idx+1:03d}",
        q_str, q_hi, q_gu,
        [opt1, opt2, opt3, opt4],
        [opt1_hi, opt2_hi, opt3_hi, opt4_hi],
        [opt1_gu, opt2_gu, opt3_gu, opt4_gu],
        ans_idx,
        expl, expl_hi, expl_gu
    ))

file_path = os.path.join(CHAPTERS_DIR, grammar_ch1["file"])
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(grammar_ch1["blocks"], f, indent=2, ensure_ascii=False)
    f.write("\n")
print(f"Created {grammar_ch1['file']} with {len(grammar_ch1['blocks'])} blocks.")
