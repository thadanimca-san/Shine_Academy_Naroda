import json
import os

# POEM 1: Dust of Snow
poem1_blocks = [
    {
        "id": "KOBJ_NCERT_C10_ENG_FFP_P1_001",
        "type": "hook",
        "title": "Finding Joy in Small Things",
        "title_hi": "छोटी चीज़ों में खुशी ढूँढना",
        "title_gu": "નાની વસ્તુઓમાં આનંદ શોધવો",
        "body": "Have you ever had a terrible day where everything seemed to go wrong, and you were in a very bad mood? Then, suddenly, a small, unexpected thing—like a cool breeze, a smiling child, or a beautiful bird—completely changed your mood and made you happy? Robert Frost's short poem 'Dust of Snow' is about exactly this. It shows how even things we usually consider 'bad omens' or negative can bring unexpected joy and save our day from being ruined.",
        "body_hi": "क्या आपका कभी कोई ऐसा भयानक दिन बीता है जब ऐसा लग रहा हो कि सब कुछ गलत हो रहा है, और आपका मूड बहुत खराब था? फिर, अचानक, एक छोटी, अप्रत्याशित (unexpected) चीज़-जैसे ठंडी हवा, एक मुस्कुराता हुआ बच्चा, या एक सुंदर पक्षी-ने आपका मूड पूरी तरह बदल दिया और आपको खुश कर दिया? रॉबर्ट फ्रॉस्ट (Robert Frost) की छोटी कविता 'डस्ट ऑफ स्नो' (Dust of Snow) बिल्कुल इसी के बारे में है। यह दर्शाता है कि कैसे जिन चीजों को हम आमतौर पर 'अशुभ संकेत' (bad omens) या नकारात्मक (negative) मानते हैं, वे भी अप्रत्याशित खुशी ला सकती हैं और हमारे दिन को बर्बाद होने से बचा सकती हैं।",
        "body_gu": "શું તમારી પાસે ક્યારેય એવો ભયંકર દિવસ હતો જ્યાં બધું ખોટું થતું હોય તેવું લાગતું હતું, અને તમે ખૂબ જ ખરાબ મૂડમાં હતા? પછી, અચાનક, એક નાની, અણધારી (unexpected) વસ્તુ - જેમ કે ઠંડી પવન, હસતું બાળક અથવા એક સુંદર પક્ષી - એ તમારો મૂડ સંપૂર્ણપણે બદલી નાખ્યો અને તમને ખુશ કરી દીધા? રોબર્ટ ફ્રોસ્ટની (Robert Frost) ટૂંકી કવિતા 'ડસ્ટ ઓફ સ્નો' (Dust of Snow) બરાબર આ વિશે છે. તે બતાવે છે કે કેવી રીતે જે વસ્તુઓને આપણે સામાન્ય રીતે 'ખરાબ શુકન' (bad omens) અથવા નકારાત્મક (negative) માનીએ છીએ તે પણ અણધારી ખુશી લાવી શકે છે અને આપણા દિવસને બરબાદ થવાથી બચાવી શકે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_ENG_FFP_P1_002",
        "type": "theory",
        "title": "The Poem: Dust of Snow",
        "title_hi": "कविता: डस्ट ऑफ स्नो (Dust of Snow)",
        "title_gu": "કવિતા: ડસ્ટ ઓફ સ્નો (Dust of Snow)",
        "body": "The way a crow\nShook down on me\nThe dust of snow\nFrom a hemlock tree\n\nHas given my heart\nA change of mood\nAnd saved some part\nOf a day I had rued.\n\n— Robert Frost",
        "body_hi": "एक कौवे (crow) ने जिस तरह\nमुझ पर झाड़ दी (Shook down)\nबर्फ की धूल (dust of snow)\nएक हेमलॉक पेड़ (hemlock tree) से\n\nउसने मेरे दिल को दे दिया है\nमूड (mood) में बदलाव\nऔर बचा लिया है कुछ हिस्सा\nउस दिन का जिस पर मुझे पछतावा (rued) था।\n\n— रॉबर्ट फ्रॉस्ट (Robert Frost)",
        "body_gu": "જે રીતે એક કાગડાએ (crow)\nમારા પર ખંખેરી (Shook down)\nબરફની ધૂળ (dust of snow)\nહેમલોક વૃક્ષ (hemlock tree) પરથી\n\nતેણે મારા હૃદયને આપી દીધો છે\nમૂડમાં (mood) ફેરફાર\nઅને બચાવી લીધો છે કેટલોક ભાગ\nએક દિવસનો જેનો મને પસ્તાવો (rued) હતો.\n\n- રોબર્ટ ફ્રોસ્ટ (Robert Frost)"
    },
    {
        "id": "KOBJ_NCERT_C10_ENG_FFP_P1_003",
        "type": "theory",
        "title": "Understanding the Irony",
        "title_hi": "विडंबना को समझना (Understanding the Irony)",
        "title_gu": "વક્રોક્તિ સમજવી (Understanding the Irony)",
        "body": "In poetry, birds like peacocks, parrots, or nightingales are often used to represent beauty and joy. Trees like oak, pine, or maple are celebrated. \nBut Robert Frost chose a crow (often associated with sorrow or doom) and a hemlock tree (a poisonous plant). By using these 'negative' symbols, the poet is showing that joy and healing do not always come from beautiful or positive things. Nature can bless us and change our mood using the most unexpected and ordinary things.",
        "body_hi": "कविता में, अक्सर सुंदरता और खुशी का प्रतिनिधित्व करने के लिए मोर, तोते या बुलबुल जैसे पक्षियों का उपयोग किया जाता है। ओक, देवदार, या मेपल (maple) जैसे पेड़ों का जश्न मनाया जाता है।\nलेकिन रॉबर्ट फ्रॉस्ट ने एक कौवा (अक्सर दुःख या कयामत से जुड़ा) और एक हेमलॉक पेड़ (एक जहरीला पौधा) चुना। इन 'नकारात्मक' प्रतीकों (negative symbols) का उपयोग करके, कवि यह दिखा रहा है कि खुशी और उपचार हमेशा सुंदर या सकारात्मक चीजों से नहीं आते हैं। प्रकृति हमें आशीर्वाद दे सकती है और सबसे अप्रत्याशित (unexpected) और साधारण चीजों का उपयोग करके हमारा मूड बदल सकती है।",
        "body_gu": "કવિતામાં, મોર, પોપટ અથવા નાઇટિંગેલ જેવા પક્ષીઓનો ઉપયોગ ઘણીવાર સુંદરતા અને આનંદને દર્શાવવા માટે થાય છે. ઓક, પાઈન અથવા મેપલ (maple) જેવા વૃક્ષો ઉજવવામાં આવે છે.\nપરંતુ રોબર્ટ ફ્રોસ્ટે કાગડો (ઘણીવાર દુઃખ કે વિનાશ સાથે સંકળાયેલો) અને હેમલોક વૃક્ષ (ઝેરી છોડ) પસંદ કર્યું. આ 'નકારાત્મક' પ્રતીકોનો (negative symbols) ઉપયોગ કરીને, કવિ દર્શાવે છે કે આનંદ અને ઉપચાર હંમેશા સુંદર અથવા સકારાત્મક વસ્તુઓમાંથી આવતા નથી. પ્રકૃતિ આપણને આશીર્વાદ આપી શકે છે અને સૌથી અણધારી (unexpected) અને સામાન્ય વસ્તુઓનો ઉપયોગ કરીને આપણો મૂડ બદલી શકે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_ENG_FFP_P1_004",
        "type": "mcq",
        "title": "NCERT Exercise Q: Mood Change",
        "title_hi": "NCERT अभ्यास Q: मूड में बदलाव",
        "title_gu": "NCERT સ્વાધ્યાય Q: મૂડ ચેન્જ",
        "question": "What does the poet mean when he says, 'And saved some part / Of a day I had rued'?",
        "question_hi": "कवि का क्या अर्थ है जब वह कहता है, 'और मेरे उस दिन का कुछ हिस्सा बचा लिया जिस पर मुझे पछतावा था (rued)'?",
        "question_gu": "કવિનો અર્થ શું છે જ્યારે તે કહે છે, 'અને મારા એ દિવસનો કેટલોક ભાગ બચાવ્યો જેનો મને પસ્તાવો (rued) હતો'?",
        "options": [
            "He was having a great day, but the snow made it worse.",
            "He was having a regretful, sad day, but the snow falling on him changed his mood and made the rest of the day better.",
            "He regretted going out into the snow and wished he stayed inside.",
            "He was happy to see the crow but angry at the hemlock tree."
        ],
        "options_hi": [
            "उसका दिन बहुत अच्छा जा रहा था, लेकिन बर्फबारी ने इसे और खराब कर दिया।",
            "उसका दिन पछतावे भरा (regretful) और उदास था, लेकिन उस पर गिरी बर्फ ने उसका मूड बदल दिया और बाकी के दिन को बेहतर बना दिया।",
            "उसे बर्फ में बाहर जाने का पछतावा हुआ और उसने चाहा कि वह अंदर ही रहे।",
            "वह कौवे को देखकर खुश हुआ लेकिन हेमलॉक के पेड़ पर क्रोधित हुआ।"
        ],
        "options_gu": [
            "તેનો દિવસ ઘણો સારો હતો, પરંતુ બરફથી તે ખરાબ થઈ ગયો.",
            "તેનો દિવસ પસ્તાવાભર્યો (regretful) અને ઉદાસી હતો, પરંતુ તેના પર પડતા બરફથી તેનો મૂડ બદલાઈ ગયો અને બાકીનો દિવસ સારો બન્યો.",
            "તેને બરફમાં બહાર જવાનો પસ્તાવો થયો અને ઈચ્છા વ્યક્ત કરી કે તે અંદર જ રહે.",
            "તે કાગડાને જોઈને ખુશ હતો પણ હેમલોક વૃક્ષ પર ગુસ્સે હતો."
        ],
        "correct_index": 1,
        "explanation": "The word 'rued' means 'held in regret'. The poet was depressed and regretting the day. The simple act of the snow falling on him broke his chain of sad thoughts, refreshed him, and 'saved' the remaining part of his day from being wasted in sadness.",
        "explanation_hi": "'rued' शब्द का अर्थ है 'पछतावा करना' (regret)। कवि निराश था और उस दिन पर पछता रहा था। उस पर बर्फ गिरने की साधारण सी घटना ने उसके दुखद विचारों की श्रृंखला को तोड़ दिया, उसे तरोताजा कर दिया, और उसके दिन के शेष भाग को दुख में बर्बाद होने से 'बचा लिया' (saved)।",
        "explanation_gu": "'rued' શબ્દનો અર્થ થાય છે 'પસ્તાવો' (regret). કવિ નિરાશ હતો અને દિવસનો પસ્તાવો કરતો હતો. તેના પર પડતા બરફની સાદી ક્રિયાએ તેના ઉદાસી વિચારોની સાંકળ તોડી નાખી, તેને તાજું કર્યું અને તેના દિવસના બાકીના ભાગને ઉદાસીમાં વેડફાઈ જવાથી 'બચાવી' (saved)."
    }
]

# POEM 2: Fire and Ice
poem2_blocks = [
    {
        "id": "KOBJ_NCERT_C10_ENG_FFP_P2_001",
        "type": "hook",
        "title": "How Will the World End?",
        "title_hi": "दुनिया का अंत कैसे होगा?",
        "title_gu": "વિશ્વનો અંત કેવી રીતે આવશે?",
        "body": "Scientists have many theories about how the Earth might eventually be destroyed. Some say the sun will get too hot and burn everything up. Others say we will enter a new ice age and everything will freeze. \nIn the poem 'Fire and Ice', Robert Frost uses these two ideas—fire and ice—not just as physical forces, but as symbols of human emotions. He compares 'Fire' to human desire, greed, and passion. He compares 'Ice' to human hatred, coldness, and indifference. Which emotion do you think is strong enough to destroy the world? Let's find out what the poet thinks.",
        "body_hi": "वैज्ञानिकों के पास इस बारे में कई सिद्धांत (theories) हैं कि अंततः पृथ्वी कैसे नष्ट हो सकती है। कुछ का कहना है कि सूरज बहुत गर्म हो जाएगा और सब कुछ जला देगा। दूसरों का कहना है कि हम एक नए हिमयुग (ice age) में प्रवेश करेंगे और सब कुछ जम जाएगा।\nकविता 'फायर एंड आइस' (Fire and Ice - आग और बर्फ) में, रॉबर्ट फ्रॉस्ट इन दो विचारों-आग और बर्फ-का उपयोग केवल भौतिक शक्तियों (physical forces) के रूप में नहीं, बल्कि मानवीय भावनाओं (human emotions) के प्रतीकों के रूप में करते हैं। वह 'अग्नि' की तुलना मानवीय इच्छा (desire), लालच (greed) और जुनून (passion) से करते हैं। वह 'बर्फ' की तुलना मानवीय घृणा (hatred), शीतलता और उदासीनता (indifference) से करते हैं। आपको क्या लगता है कि कौन सी भावना दुनिया को नष्ट करने के लिए काफी मजबूत है? आइए जानें कि कवि क्या सोचता है।",
        "body_gu": "વૈજ્ઞાનિકો પાસે પૃથ્વી કેવી રીતે નાશ પામી શકે છે તે વિશે ઘણી થિયરીઓ (theories) છે. કેટલાક કહે છે કે સૂર્ય ખૂબ ગરમ થશે અને બધું બાળી નાખશે. અન્ય લોકો કહે છે કે આપણે નવા હિમયુગમાં (ice age) પ્રવેશીશું અને બધું થીજી જશે.\n'ફાયર એન્ડ આઇસ' (Fire and Ice - અગ્નિ અને બરફ) કવિતામાં રોબર્ટ ફ્રોસ્ટ આ બે વિચારોનો ઉપયોગ કરે છે-અગ્નિ અને બરફ-માત્ર ભૌતિક શક્તિઓ (physical forces) તરીકે જ નહીં, પરંતુ માનવ લાગણીઓના (human emotions) પ્રતીકો તરીકે. તે 'અગ્નિ' ની સરખામણી માનવ ઈચ્છા (desire), લોભ (greed) અને જુસ્સા (passion) સાથે કરે છે. તે 'આઇસ'ની સરખામણી માનવ નફરત (hatred), ઠંડક અને ઉદાસીનતા (indifference) સાથે કરે છે. તમારા મતે કઈ લાગણી દુનિયાને નષ્ટ કરવા માટે પૂરતી મજબૂત છે? ચાલો જાણીએ કવિ શું વિચારે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_ENG_FFP_P2_002",
        "type": "theory",
        "title": "The Poem: Fire and Ice",
        "title_hi": "कविता: फायर एंड आइस (Fire and Ice)",
        "title_gu": "કવિતા: ફાયર એન્ડ આઈસ (Fire and Ice)",
        "body": "Some say the world will end in fire\nSome say in ice.\nFrom what I’ve tasted of desire\nI hold with those who favour fire.\n\nBut if it had to perish twice,\nI think I know enough of hate\nTo say that for destruction ice\nIs also great\nAnd would suffice.\n\n— Robert Frost",
        "body_hi": "कुछ का कहना है कि दुनिया आग में खत्म हो जाएगी\nकुछ कहते हैं बर्फ में।\nमैंने इच्छा (desire) का जो स्वाद चखा है, उससे\nमैं उनका साथ देता हूँ जो आग का पक्ष (favour) लेते हैं।\n\nलेकिन अगर इसे दो बार नष्ट (perish) होना पड़े,\nमुझे लगता है कि मैं नफरत (hate) को इतना जानता हूं\nयह कहने के लिए कि विनाश के लिए बर्फ भी\nमहान है\nऔर पर्याप्त (suffice) होगी।\n\n— रॉबर्ट फ्रॉस्ट (Robert Frost)",
        "body_gu": "કેટલાક કહે છે કે દુનિયા આગમાં ખતમ થઈ જશે\nકેટલાક કહે છે બરફમાં.\nમેં જે ઈચ્છા (desire) નો સ્વાદ ચાખ્યો છે તેમાંથી\nહું આગની તરફેણ (favour) કરનારાઓની સાથે છું.\n\nપરંતુ જો તેને બે વાર નાશ (perish) પામવો પડે,\nમને લાગે છે કે હું નફરતને (hate) પૂરતી જાણું છું\nએમ કહેવા માટે કે વિનાશ માટે બરફ પણ\nમહાન છે\nઅને પૂરતું (suffice) થશે.\n\n- રોબર્ટ ફ્રોસ્ટ (Robert Frost)"
    },
    {
        "id": "KOBJ_NCERT_C10_ENG_FFP_P2_003",
        "type": "theory",
        "title": "The Meaning of Fire and Ice",
        "title_hi": "आग और बर्फ का अर्थ (Meaning of Fire and Ice)",
        "title_gu": "અગ્નિ અને બરફનો અર્થ (Meaning of Fire and Ice)",
        "body": "In this poem, 'Fire' stands for greed, avarice, lust, conflict, and fury. These strong, uncontrolled desires spread rapidly like a forest fire and can easily consume and destroy the world. \n'Ice' stands for cruelty, intolerance, rigidity, insensitivity, coldness, indifference, and hatred. While fire destroys quickly, ice destroys slowly and silently. Hatred makes people numb to the feelings of others. The poet concludes that if the world had to be destroyed a second time (perish twice), the cold power of hatred (ice) would be just as effective as the burning heat of desire (fire).",
        "body_hi": "इस कविता में, 'अग्नि' (Fire) लालच, लोभ, वासना (lust), संघर्ष (conflict) और क्रोध का प्रतीक है। ये प्रबल, अनियंत्रित इच्छाएँ जंगल की आग की तरह तेजी से फैलती हैं और आसानी से दुनिया को निगल और नष्ट कर सकती हैं।\n'बर्फ' (Ice) क्रूरता, असहिष्णुता (intolerance), कठोरता, असंवेदनशीलता, शीतलता, उदासीनता और घृणा (hatred) का प्रतीक है। आग जहां जल्दी नष्ट करती है, वहीं बर्फ धीरे-धीरे और चुपचाप नष्ट करती है। नफ़रत लोगों को दूसरों की भावनाओं के प्रति सुन्न (numb) कर देती है। कवि का निष्कर्ष है कि यदि दुनिया को दूसरी बार नष्ट होना पड़े (दो बार नष्ट होना), तो नफरत की ठंडी शक्ति (बर्फ) इच्छा की जलती हुई गर्मी (आग) जितनी ही प्रभावी (effective) होगी।",
        "body_gu": "આ કવિતામાં, 'અગ્નિ' (Fire) લોભ, વાસના (lust), સંઘર્ષ (conflict) અને ક્રોધ માટે વપરાય છે. આ પ્રબળ, અનિયંત્રિત ઈચ્છાઓ જંગલની આગની જેમ ઝડપથી ફેલાય છે અને સરળતાથી વિશ્વને ખાઈ જાય છે અને નાશ કરી શકે છે.\n'આઇસ' (Ice) ક્રૂરતા, અસહિષ્ણુતા (intolerance), કઠોરતા, અસંવેદનશીલતા, ઠંડક, ઉદાસીનતા અને નફરત માટે (hatred) વપરાય છે. અગ્નિ જ્યાં ઝડપથી નાશ કરે છે ત્યાં બરફ ધીરે ધીરે અને શાંતિથી નાશ કરે છે. નફરત લોકોને અન્યની લાગણીઓ પ્રત્યે સુન્ન (numb) બનાવે છે. કવિ તારણ આપે છે કે જો દુનિયાનો બીજી વાર નાશ થવાનો હોય (બે વાર નાશ પામવો), તો દ્વેષની ઠંડી શક્તિ (બરફ) ઇચ્છાની બળતી ગરમી (અગ્નિ) જેટલી જ અસરકારક (effective) રહેશે."
    },
    {
        "id": "KOBJ_NCERT_C10_ENG_FFP_P2_004",
        "type": "mcq",
        "title": "NCERT Exercise Q: Suffice",
        "title_hi": "NCERT अभ्यास Q: पर्याप्त (Suffice)",
        "title_gu": "NCERT સ્વાધ્યાય Q: પૂરતું (Suffice)",
        "question": "What does the word 'suffice' mean in the context of the poem?",
        "question_hi": "कविता के संदर्भ में 'सफ़ाइस' (suffice) शब्द का क्या अर्थ है?",
        "question_gu": "કવિતાના સંદર્ભમાં 'સફાઇસ' (suffice) શબ્દનો અર્થ શું છે?",
        "options": [
            "To be completely destroyed",
            "To be sufficient or enough",
            "To suffer great pain",
            "To freeze solid"
        ],
        "options_hi": [
            "पूरी तरह नष्ट हो जाना (To be completely destroyed)",
            "पर्याप्त या काफी होना (To be sufficient or enough)",
            "अत्यधिक दर्द सहना (To suffer great pain)",
            "ठोस रूप में जम जाना (To freeze solid)"
        ],
        "options_gu": [
            "સંપૂર્ણપણે નાશ પામવા માટે (To be completely destroyed)",
            "પૂરતું કે પર્યાપ્ત હોવું (To be sufficient or enough)",
            "ખૂબ પીડા ભોગવવી (To suffer great pain)",
            "નક્કર સ્થિર થવા માટે (To freeze solid)"
        ],
        "correct_index": 1,
        "explanation": "The word 'suffice' means 'be enough or adequate'. The poet says that hatred (ice) would 'suffice' (be enough) to cause the destruction of the world.",
        "explanation_hi": "'suffice' शब्द का अर्थ है 'पर्याप्त या काफी होना' (be enough)। कवि कहता है कि दुनिया के विनाश का कारण बनने के लिए नफरत (बर्फ) 'पर्याप्त' (suffice) होगी।",
        "explanation_gu": "'suffice' શબ્દનો અર્થ થાય છે 'પૂરતું કે પર્યાપ્ત હોવું' (be enough). કવિ કહે છે કે નફરત (બરફ) વિશ્વના વિનાશનું કારણ બનવા માટે 'પૂરતું' (suffice) હશે."
    }
]

data1 = {
    "metadata": {
        "id": "ncert_class10_english_ff_poem1",
        "title": "First Flight Poetry 1: Dust of Snow",
        "subject": "English",
        "grade": "10"
    },
    "blocks": poem1_blocks
}

data2 = {
    "metadata": {
        "id": "ncert_class10_english_ff_poem2",
        "title": "First Flight Poetry 2: Fire and Ice",
        "subject": "English",
        "grade": "10"
    },
    "blocks": poem2_blocks
}

path1 = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ff_poem1.json'
path2 = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ff_poem2.json'

with open(path1, 'w', encoding='utf-8') as f:
    json.dump(data1, f, ensure_ascii=False, indent=2)
with open(path2, 'w', encoding='utf-8') as f:
    json.dump(data2, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {len(poem1_blocks)} blocks to {path1}")
print(f"Successfully wrote {len(poem2_blocks)} blocks to {path2}")
