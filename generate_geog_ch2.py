import json

blocks = [
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH2_001",
        "type": "hook",
        "title": "A Web of Life",
        "title_hi": "जीवन का जाल",
        "title_gu": "જીવનની જાળ",
        "body": "Imagine a world without birds singing in the morning, without the majestic roar of a tiger, or without the colourful flowers in a forest. We share this planet with millions of other living beings, from micro-organisms and bacteria to banyan trees, elephants, and blue whales. This entire habitat that we live in has immense biodiversity. But human beings are cutting the branches they sit on. Forests are vanishing and animals are disappearing. Can we survive alone on this planet without them?",
        "body_hi": "एक ऐसी दुनिया की कल्पना करें जहां सुबह पक्षियों के चहचहाने की आवाज न हो, बाघ की राजसी दहाड़ न हो, या जंगल में रंग-बिरंगे फूल न हों। हम इस ग्रह को सूक्ष्म जीवों (micro-organisms) और बैक्टीरिया से लेकर बरगद के पेड़ों, हाथियों और नीली व्हेल तक लाखों अन्य जीवित प्राणियों के साथ साझा करते हैं। हम जिस पूरे आवास में रहते हैं, उसमें अपार जैव विविधता (biodiversity) है। लेकिन इंसान उसी डाल को काट रहे हैं जिस पर वे बैठे हैं। जंगल गायब हो रहे हैं और जानवर लुप्त हो रहे हैं। क्या हम उनके बिना इस ग्रह पर अकेले जीवित रह सकते हैं?",
        "body_gu": "સવારે પક્ષીઓના કલરવ વિના, વાઘની ભવ્ય ગર્જના વિના, અથવા જંગલમાં રંગબેરંગી ફૂલો વિનાની દુનિયાની કલ્પના કરો. આપણે આ ગ્રહને સૂક્ષ્મ જીવો (micro-organisms) અને બેક્ટેરિયાથી લઈને વડના વૃક્ષો, હાથીઓ અને બ્લુ વ્હેલ સુધી લાખો અન્ય જીવંત પ્રાણીઓ સાથે વહેંચીએ છીએ. આ સમગ્ર નિવાસસ્થાન કે જેમાં આપણે રહીએ છીએ તેમાં અપાર જૈવવિવિધતા (biodiversity) છે. પરંતુ મનુષ્યો જે ડાળી પર બેઠા છે તેને જ કાપી રહ્યા છે. જંગલો ગાયબ થઈ રહ્યા છે અને પ્રાણીઓ અદૃશ્ય થઈ રહ્યા છે. શું આપણે તેમના વિના આ ગ્રહ પર એકલા જીવી શકીએ?"
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH2_002",
        "type": "theory",
        "title": "Flora and Fauna in India",
        "title_hi": "भारत में वनस्पति और जीव (Flora and Fauna)",
        "title_gu": "ભારતમાં વનસ્પતિ અને પ્રાણીસૃષ્ટિ (Flora and Fauna)",
        "body": "India is one of the world's richest countries in terms of its vast array of biological diversity. However, at least 10 per cent of India’s recorded wild flora and 20 per cent of its mammals are on the threatened list.\nThe International Union for Conservation of Nature and Natural Resources (IUCN) classifies species as:\n1. Normal Species: Population levels are considered normal (e.g., cattle, sal, pine).\n2. Endangered Species: In danger of extinction (e.g., black buck, crocodile, Indian rhino).\n3. Vulnerable Species: Population has declined to levels where it is likely to become endangered (e.g., Asiatic elephant, Gangetic dolphin).\n4. Rare Species: Small population that may move into the endangered category.\n5. Endemic Species: Found only in some particular areas usually isolated by natural barriers (e.g., Andaman teal, Nicobar pigeon).\n6. Extinct Species: Not found after searches of known or likely areas (e.g., Asiatic cheetah, pink head duck).",
        "body_hi": "जैविक विविधता की विशाल श्रृंखला के संदर्भ में भारत दुनिया के सबसे अमीर देशों में से एक है। हालाँकि, भारत की कम से कम 10 प्रतिशत दर्ज जंगली वनस्पति और 20 प्रतिशत स्तनधारी खतरे की सूची में हैं।\nअंतर्राष्ट्रीय प्रकृति संरक्षण संघ (IUCN) प्रजातियों को इस प्रकार वर्गीकृत करता है:\n1. सामान्य प्रजातियाँ: जनसंख्या का स्तर सामान्य माना जाता है (जैसे, मवेशी, साल, देवदार)।\n2. लुप्तप्राय (Endangered) प्रजातियाँ: विलुप्त होने के खतरे में (जैसे, काला हिरण, मगरमच्छ, भारतीय गैंडा)।\n3. सुभेद्य (Vulnerable) प्रजातियाँ: जनसंख्या उस स्तर तक गिर गई है जहाँ इसके लुप्तप्राय होने की संभावना है (जैसे, एशियाई हाथी, गंगा डॉल्फिन)।\n4. दुर्लभ (Rare) प्रजातियाँ: छोटी आबादी जो लुप्तप्राय श्रेणी में जा सकती है।\n5. स्थानिक (Endemic) प्रजातियाँ: केवल कुछ विशेष क्षेत्रों में पाई जाती हैं जो प्राकृतिक बाधाओं से अलग होते हैं (जैसे, अंडमान टील, निकोबार कबूतर)।\n6. विलुप्त (Extinct) प्रजातियाँ: जो अब नहीं पाई जाती हैं (जैसे, एशियाई चीता, गुलाबी सिर वाली बत्तख)।",
        "body_gu": "જૈવિક વિવિધતાની વિશાળ શ્રેણીના સંદર્ભમાં ભારત વિશ્વના સૌથી સમૃદ્ધ દેશોમાંનો એક છે. જો કે, ભારતની ઓછામાં ઓછી 10 ટકા નોંધાયેલ જંગલી વનસ્પતિ અને 20 ટકા સસ્તન પ્રાણીઓ જોખમની યાદીમાં છે.\nઇન્ટરનેશનલ યુનિયન ફોર કન્ઝર્વેશન ઓફ નેચર એન્ડ નેચરલ રિસોર્સિસ (IUCN) પ્રજાતિઓને નીચે મુજબ વર્ગીકૃત કરે છે:\n1. સામાન્ય પ્રજાતિઓ: વસ્તીનું સ્તર સામાન્ય માનવામાં આવે છે (દા.ત., ઢોર, સાલ, પાઈન).\n2. લુપ્તપ્રાય (Endangered) પ્રજાતિઓ: લુપ્ત થવાના જોખમમાં (દા.ત., કાળિયાર, મગર, ભારતીય ગેંડો).\n3. સંવેદનશીલ (Vulnerable) પ્રજાતિઓ: વસ્તી એ સ્તરે ઘટી ગઈ છે જ્યાં તે લુપ્તપ્રાય થવાની સંભાવના છે (દા.ત., એશિયાટિક હાથી, ગંગાની ડોલ્ફિન).\n4. દુર્લભ (Rare) પ્રજાતિઓ: નાની વસ્તી જે લુપ્તપ્રાય શ્રેણીમાં જઈ શકે છે.\n5. સ્થાનિક (Endemic) પ્રજાતિઓ: કુદરતી અવરોધો દ્વારા અલગ થયેલા કેટલાક ચોક્કસ વિસ્તારોમાં જ જોવા મળે છે (દા.ત., આંદામાન ટીલ, નિકોબાર કબૂતર).\n6. લુપ્ત (Extinct) પ્રજાતિઓ: જે હવે જોવા મળતી નથી (દા.ત., એશિયાટિક ચિત્તો, ગુલાબી માથાવાળી બતક)."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH2_003",
        "type": "theory",
        "title": "Causes of Depletion",
        "title_hi": "कमी के कारण",
        "title_gu": "ઘટાડાના કારણો",
        "body": "What has caused such a rapid decline in India's biodiversity?\n1. Colonial Rule: The greatest damage inflicted on Indian forests was during the colonial period due to the expansion of the railways, agriculture, commercial and scientific forestry and mining activities.\n2. Agricultural Expansion: Between 1951 and 1980, over 26,200 sq. km. of forest area was converted into agricultural land.\n3. Large-scale Development Projects: Since 1951, over 5,000 sq km of forest was cleared for river valley projects (e.g., Narmada Sagar Project in MP).\n4. Mining: The Buxa Tiger Reserve in West Bengal is seriously threatened by dolomite mining.\n5. Poaching and Hunting: Illegal hunting for skin, horns, and bones has endangered many species like the tiger and rhino.",
        "body_hi": "भारत की जैव विविधता में इतनी तेजी से गिरावट का कारण क्या है?\n1. औपनिवेशिक शासन (Colonial Rule): रेलवे, कृषि, वाणिज्यिक और वैज्ञानिक वानिकी और खनन गतिविधियों के विस्तार के कारण औपनिवेशिक काल के दौरान भारतीय जंगलों को सबसे ज्यादा नुकसान पहुंचा।\n2. कृषि विस्तार: 1951 और 1980 के बीच, 26,200 वर्ग किमी से अधिक वन क्षेत्र को कृषि भूमि में बदल दिया गया।\n3. बड़े पैमाने पर विकास परियोजनाएं: 1951 के बाद से, नदी घाटी परियोजनाओं (जैसे मध्य प्रदेश में नर्मदा सागर परियोजना) के लिए 5,000 वर्ग किमी से अधिक जंगल साफ कर दिए गए।\n4. खनन: पश्चिम बंगाल में बक्सा टाइगर रिजर्व को डोलोमाइट खनन से गंभीर खतरा है।\n5. अवैध शिकार (Poaching) और शिकार: त्वचा, सींग और हड्डियों के लिए अवैध शिकार ने बाघ और गैंडे जैसी कई प्रजातियों को खतरे में डाल दिया है।",
        "body_gu": "ભારતની જૈવવિવિધતામાં આટલા ઝડપી ઘટાડાનું કારણ શું છે?\n1. વસાહતી શાસન (Colonial Rule): રેલ્વે, કૃષિ, વ્યાપારી અને વૈજ્ઞાનિક વનસંવર્ધન અને ખાણકામ પ્રવૃત્તિઓના વિસ્તરણને કારણે વસાહતી સમયગાળા દરમિયાન ભારતીય જંગલોને સૌથી વધુ નુકસાન થયું હતું.\n2. કૃષિ વિસ્તરણ: 1951 અને 1980 ની વચ્ચે, 26,200 ચોરસ કિમીથી વધુ જંગલ વિસ્તારને ખેતીલાયક જમીનમાં ફેરવવામાં આવ્યો હતો.\n3. મોટા પાયે વિકાસ પ્રોજેક્ટ્સ: 1951 થી, નદી ખીણ પ્રોજેક્ટ્સ (દા.ત., એમપીમાં નર્મદા સાગર પ્રોજેક્ટ) માટે 5,000 ચોરસ કિમીથી વધુ જંગલ સાફ કરવામાં આવ્યા હતા.\n4. ખાણકામ: પશ્ચિમ બંગાળમાં બક્સા ટાઇગર રિઝર્વને ડોલોમાઇટ ખાણકામથી ગંભીર ખતરો છે.\n5. શિકાર (Poaching) અને શિકાર: ચામડી, શિંગડા અને હાડકાં માટે ગેરકાયદેસર શિકારને કારણે વાઘ અને ગેંડા જેવી ઘણી પ્રજાતિઓ જોખમમાં મુકાઈ છે."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH2_004",
        "type": "theory",
        "title": "Conservation of Forest and Wildlife",
        "title_hi": "वन और वन्य जीवन का संरक्षण",
        "title_gu": "જંગલ અને વન્યજીવનનું સંરક્ષણ",
        "body": "Conservation preserves the ecological diversity and our life support systems – water, air, and soil. \nIn response to demands from conservationists, the Indian Wildlife (Protection) Act was implemented in 1972. The thrust of the programme was towards protecting the remaining population of certain endangered species by banning hunting, giving legal protection to their habitats, and restricting trade in wildlife.\nProject Tiger: Launched in 1973, it is one of the most well-publicised wildlife campaigns in the world. The tiger population had dwindled from an estimated 55,000 at the turn of the century to 1,827 in 1973 due to poaching, shrinking habitats, and depletion of prey base. Corbett National Park (Uttarakhand) and Sundarbans (West Bengal) are important tiger reserves.",
        "body_hi": "संरक्षण से पारिस्थितिक (ecological) विविधता और हमारे जीवन समर्थन प्रणालियों - पानी, हवा और मिट्टी का संरक्षण होता है।\nसंरक्षणवादियों की मांगों के जवाब में, भारतीय वन्यजीव (संरक्षण) अधिनियम 1972 में लागू किया गया था। इस कार्यक्रम का मुख्य जोर शिकार पर प्रतिबंध लगाकर, उनके आवासों को कानूनी सुरक्षा देकर और वन्यजीवों के व्यापार को प्रतिबंधित करके कुछ लुप्तप्राय प्रजातियों की शेष आबादी की रक्षा करना था।\nप्रोजेक्ट टाइगर: 1973 में शुरू किया गया, यह दुनिया में सबसे प्रसिद्ध वन्यजीव अभियानों में से एक है। सदी के अंत में बाघों की अनुमानित संख्या 55,000 से घटकर 1973 में 1,827 रह गई थी, जिसका कारण अवैध शिकार, सिकुड़ते आवास और शिकार के आधार में कमी थी। कॉर्बेट नेशनल पार्क (उत्तराखंड) और सुंदरबन (पश्चिम बंगाल) महत्वपूर्ण बाघ अभयारण्य (tiger reserves) हैं।",
        "body_gu": "સંરક્ષણ ઇકોલોજીકલ વિવિધતા અને આપણી જીવન આધાર પ્રણાલીઓ - પાણી, હવા અને જમીનને જાળવી રાખે છે.\nસંરક્ષણવાદીઓની માંગના પ્રતિભાવમાં, ભારતીય વન્યજીવ (સંરક્ષણ) અધિનિયમ 1972 માં લાગુ કરવામાં આવ્યો હતો. આ કાર્યક્રમનો મુખ્ય ઉદ્દેશ્ય શિકાર પર પ્રતિબંધ મૂકીને, તેમના રહેઠાણોને કાનૂની રક્ષણ આપીને અને વન્યજીવોના વેપારને પ્રતિબંધિત કરીને કેટલીક લુપ્તપ્રાય પ્રજાતિઓની બાકી રહેલી વસ્તીનું રક્ષણ કરવાનો હતો.\nપ્રોજેક્ટ ટાઇગર: 1973 માં શરૂ કરાયેલ, તે વિશ્વમાં સૌથી વધુ પ્રસિદ્ધ વન્યજીવન ઝુંબેશમાંની એક છે. ગેરકાયદેસર શિકાર, સંકોચાઈ રહેલા રહેઠાણો અને શિકારના આધારમાં ઘટાડો થવાને કારણે સદીના વળાંક પર વાઘની અંદાજિત વસ્તી 55,000 થી ઘટીને 1973 માં 1,827 થઈ ગઈ હતી. કોર્બેટ નેશનલ પાર્ક (ઉત્તરાખંડ) અને સુંદરવન (પશ્ચિમ બંગાળ) એ વાઘ અનામત (tiger reserves) ક્ષેત્રો છે."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH2_005",
        "type": "theory",
        "title": "Community and Conservation",
        "title_hi": "समुदाय और संरक्षण",
        "title_gu": "સમુદાય અને સંરક્ષણ",
        "body": "Forests are not just trees; they are home to traditional communities. \n1. Sacred Groves: Nature worship is an age-old tribal belief. Certain patches of forest or parts of large forests have been left untouched by the local people and any interference with them is banned. These are called sacred groves.\n2. Chipko Movement: In the Himalayas, the famous Chipko movement successfully resisted deforestation in several areas. Villagers hugged the trees to prevent them from being cut down.\n3. Beej Bachao Andolan: Farmers and citizen's groups like the Beej Bachao Andolan in Tehri and Navdanya have shown that adequate levels of diversified crop production without the use of synthetic chemicals are possible and economically viable.\n4. Joint Forest Management (JFM): Introduced in India in 1988 (Odisha), it involves local communities in the management and restoration of degraded forests.",
        "body_hi": "जंगल केवल पेड़ नहीं हैं; वे पारंपरिक समुदायों के घर हैं।\n1. पवित्र उपवन (Sacred Groves): प्रकृति पूजा एक सदियों पुरानी आदिवासी मान्यता है। जंगल के कुछ पैच या बड़े जंगलों के कुछ हिस्सों को स्थानीय लोगों द्वारा अछूता छोड़ दिया गया है और उनके साथ कोई भी हस्तक्षेप प्रतिबंधित है। इन्हें पवित्र उपवन कहा जाता है।\n2. चिपको आंदोलन: हिमालय में, प्रसिद्ध चिपको आंदोलन ने कई क्षेत्रों में वनों की कटाई का सफलतापूर्वक विरोध किया। ग्रामीणों ने पेड़ों को कटने से बचाने के लिए उन्हें गले लगा लिया।\n3. बीज बचाओ आंदोलन: टिहरी में बीज बचाओ आंदोलन और नवदान्या (Navdanya) जैसे किसानों और नागरिकों के समूहों ने दिखाया है कि सिंथेटिक रसायनों के उपयोग के बिना विविध फसल उत्पादन के पर्याप्त स्तर संभव और आर्थिक रूप से व्यवहार्य हैं।\n4. संयुक्त वन प्रबंधन (JFM): 1988 (ओडिशा) में भारत में पेश किया गया, यह खराब जंगलों के प्रबंधन और बहाली में स्थानीय समुदायों को शामिल करता है।",
        "body_gu": "જંગલો માત્ર વૃક્ષો નથી; તેઓ પરંપરાગત સમુદાયોનું ઘર છે.\n1. પવિત્ર ઉપવન (Sacred Groves): પ્રકૃતિ પૂજા એ સદીઓ જૂની આદિવાસી માન્યતા છે. જંગલના કેટલાક ભાગો અથવા મોટા જંગલોના ભાગોને સ્થાનિક લોકો દ્વારા અસ્પૃશ્ય છોડી દેવામાં આવ્યા છે અને તેમની સાથે કોઈપણ દખલગીરી પર પ્રતિબંધ છે. આને પવિત્ર ઉપવન કહેવામાં આવે છે.\n2. ચિપકો આંદોલન: હિમાલયમાં, પ્રખ્યાત ચિપકો આંદોલને ઘણા વિસ્તારોમાં જંગલો કાપવાનો સફળતાપૂર્વક પ્રતિકાર કર્યો. ગ્રામવાસીઓએ વૃક્ષોને કપાતા અટકાવવા માટે તેમને ભેટી લીધા.\n3. બીજ બચાવો આંદોલન: ટિહરીમાં બીજ બચાવો આંદોલન અને નવદન્યા જેવા ખેડૂતો અને નાગરિકોના જૂથોએ દર્શાવ્યું છે કે કૃત્રિમ રસાયણોના ઉપયોગ વિના વૈવિધ્યસભર પાક ઉત્પાદનનું પર્યાપ્ત સ્તર શક્ય અને આર્થિક રીતે સક્ષમ છે.\n4. સંયુક્ત વન વ્યવસ્થાપન (JFM): 1988 (ઓડિશા) માં ભારતમાં રજૂ કરવામાં આવ્યું, તે જંગલોના સંચાલન અને પુનઃસ્થાપનમાં સ્થાનિક સમુદાયોને સામેલ કરે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH2_006",
        "type": "mcq",
        "title": "NCERT Exercise Q1_i",
        "title_hi": "NCERT अभ्यास Q1_i",
        "title_gu": "NCERT સ્વાધ્યાય Q1_i",
        "question": "Which of these statements is not a valid reason for the depletion of flora and fauna?",
        "question_hi": "इनमें से कौन सा कथन वनस्पति और जीवों की कमी का वैध कारण नहीं है?",
        "question_gu": "આમાંથી કયું વિધાન વનસ્પति અને પ્રાણીસૃષ્ટિના ઘટાડા માટેનું માન્ય કારણ નથી?",
        "options": [
            "Agricultural expansion",
            "Large scale developmental projects",
            "Grazing and fuel wood collection",
            "Rapid industrialisation and urbanisation"
        ],
        "options_hi": [
            "कृषि विस्तार",
            "बड़े पैमाने पर विकासात्मक परियोजनाएं",
            "चराई और जलाऊ लकड़ी संग्रह (Grazing and fuel wood collection)",
            "तेजी से औद्योगीकरण और शहरीकरण"
        ],
        "options_gu": [
            "કૃષિ વિસ્તરણ",
            "મોટા પાયે વિકાસ પ્રોજેક્ટ્સ",
            "ચરાઈ અને બળતણ લાકડાનો સંગ્રહ (Grazing and fuel wood collection)",
            "ઝડપી ઔદ્યોગિકીકરણ અને શહેરીકરણ"
        ],
        "correct_index": 2,
        "explanation": "While agricultural expansion, developmental projects, and industrialisation cause massive clearance of forests, grazing and fuelwood collection generally only lop a few branches and do not result in the large-scale wiping out of entire forests.",
        "explanation_hi": "जबकि कृषि विस्तार, विकासात्मक परियोजनाएं और औद्योगीकरण बड़े पैमाने पर जंगलों की कटाई का कारण बनते हैं, चराई और जलाऊ लकड़ी के संग्रह से आम तौर पर केवल कुछ शाखाएं कटती हैं और इसके परिणामस्वरूप बड़े पैमाने पर पूरे जंगलों का सफाया नहीं होता है।",
        "explanation_gu": "જ્યારે કૃષિ વિસ્તરણ, વિકાસ પ્રોજેક્ટ્સ અને ઔદ્યોગિકીકરણ જંગલોના મોટા પાયે સફાઇનું કારણ બને છે, ત્યારે ચરાઈ અને બળતણ લાકડાના સંગ્રહથી સામાન્ય રીતે માત્ર થોડી ડાળીઓ જ કપાય છે અને તેના પરિણામે મોટા પાયે આખા જંગલોનો નાશ થતો નથી."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH2_007",
        "type": "mcq",
        "title": "NCERT Exercise Q1_ii",
        "title_hi": "NCERT अभ्यास Q1_ii",
        "title_gu": "NCERT સ્વાધ્યાય Q1_ii",
        "question": "Which of the following conservation strategies do not directly involve community participation?",
        "question_hi": "निम्नलिखित में से किस संरक्षण रणनीति में सीधे तौर पर सामुदायिक भागीदारी (community participation) शामिल नहीं है?",
        "question_gu": "નીચેનામાંથી કઈ સંરક્ષણ વ્યૂહરચનામાં સીધી રીતે સમુદાયની ભાગીદારી (community participation) સામેલ નથી?",
        "options": [
            "Joint forest management",
            "Beej Bachao Andolan",
            "Chipko Movement",
            "Demarcation of Wildlife sanctuaries"
        ],
        "options_hi": [
            "संयुक्त वन प्रबंधन (Joint forest management)",
            "बीज बचाओ आंदोलन",
            "चिपको आंदोलन",
            "वन्यजीव अभयारण्यों का सीमांकन (Demarcation of Wildlife sanctuaries)"
        ],
        "options_gu": [
            "સંયુક્ત વન વ્યવસ્થાપન (Joint forest management)",
            "બીજ બચાવો આંદોલન",
            "ચિપકો આંદોલન",
            "વન્યજીવ અભયારણ્યોનું સીમાંકન (Demarcation of Wildlife sanctuaries)"
        ],
        "correct_index": 3,
        "explanation": "The demarcation (setting boundaries) of wildlife sanctuaries is done directly by the state or central government using administrative power, without directly requiring the local community's participation, unlike the Chipko movement or JFM where people actively take part.",
        "explanation_hi": "वन्यजीव अभयारण्यों का सीमांकन (सीमाएं तय करना) सीधे राज्य या केंद्र सरकार द्वारा प्रशासनिक शक्ति का उपयोग करके किया जाता है, जिसमें चिपको आंदोलन या JFM के विपरीत सीधे स्थानीय समुदाय की भागीदारी की आवश्यकता नहीं होती है जहां लोग सक्रिय रूप से भाग लेते हैं।",
        "explanation_gu": "વન્યજીવ અભયારણ્યોનું સીમાંકન (સીમાઓ નક્કી કરવી) સીધા રાજ્ય અથવા કેન્દ્ર સરકાર દ્વારા વહીવટી સત્તાનો ઉપયોગ કરીને કરવામાં આવે છે, જેમાં ચિપકો આંદોલન અથવા JFM થી વિપરીત સ્થાનિક સમુદાયની સીધી ભાગીદારીની જરૂર હોતી નથી જ્યાં લોકો સક્રિયપણે ભાગ લે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH2_008",
        "type": "mcq",
        "title": "NCERT Exercise Q2 (Match the following)",
        "title_hi": "NCERT अभ्यास Q2",
        "title_gu": "NCERT સ્વાધ્યાય Q2",
        "question": "Which of the following animals is correctly matched with its IUCN category of existence?",
        "question_hi": "अस्तित्व की IUCN श्रेणी के साथ निम्नलिखित में से किस जानवर का सही मिलान किया गया है?",
        "question_gu": "નીચેનામાંથી કયું પ્રાણી તેની અસ્તિત્વની IUCN શ્રેણી સાથે યોગ્ય રીતે મેળ ખાતું છે?",
        "options": [
            "Black buck - Extinct",
            "Asiatic elephant - Vulnerable",
            "Andaman wild pig - Normal",
            "Pink head duck - Endemic"
        ],
        "options_hi": [
            "काला हिरण (Black buck) - विलुप्त",
            "एशियाई हाथी (Asiatic elephant) - सुभेद्य (Vulnerable)",
            "अंडमान जंगली सुअर (Andaman wild pig) - सामान्य",
            "गुलाबी सिर वाली बत्तख (Pink head duck) - स्थानिक"
        ],
        "options_gu": [
            "કાળિયાર (Black buck) - લુપ્ત",
            "એશિયાટિક હાથી (Asiatic elephant) - સંવેદનશીલ (Vulnerable)",
            "આંદામાન જંગલી ડુક્કર (Andaman wild pig) - સામાન્ય",
            "ગુલાબી માથાવાળી બતક (Pink head duck) - સ્થાનિક"
        ],
        "correct_index": 1,
        "explanation": "The Asiatic elephant is Vulnerable (population has declined to levels from where it is likely to move into the endangered category). Black buck is Endangered, Andaman wild pig is Endemic, and Pink head duck is Extinct.",
        "explanation_hi": "एशियाई हाथी सुभेद्य (Vulnerable) है (जनसंख्या उस स्तर तक गिर गई है जहां से इसके लुप्तप्राय श्रेणी में जाने की संभावना है)। काला हिरण (Black buck) लुप्तप्राय (Endangered) है, अंडमान जंगली सुअर स्थानिक (Endemic) है, और गुलाबी सिर वाली बत्तख विलुप्त (Extinct) है।",
        "explanation_gu": "એશિયાટિક હાથી સંવેદનશીલ (Vulnerable) છે (વસ્તી એ સ્તરે ઘટી ગઈ છે જ્યાંથી તે લુપ્તપ્રાય શ્રેણીમાં જવાની સંભાવના છે). કાળિયાર લુપ્તપ્રાય (Endangered) છે, આંદામાન જંગલી ડુક્કર સ્થાનિક (Endemic) છે, અને ગુલાબી માથાવાળી બતક લુપ્ત (Extinct) છે."
    },
    {
        "id": "KOBJ_NCERT_C10_GEOG_CH2_009",
        "type": "mcq",
        "title": "NCERT Exercise Q3a",
        "title_hi": "NCERT अभ्यास Q3a",
        "title_gu": "NCERT સ્વાધ્યાય Q3a",
        "question": "What is biodiversity?",
        "question_hi": "जैव विविधता (biodiversity) क्या है?",
        "question_gu": "જૈવવિવિધતા (biodiversity) એટલે શું?",
        "options": [
            "The study of the solar system.",
            "The variety of life forms, including plants, animals, and micro-organisms, closely integrated in a system through multiple networks of interdependencies.",
            "The process of planting new trees in empty lands.",
            "The division of a country into different geographical zones."
        ],
        "options_hi": [
            "सौर मंडल का अध्ययन।",
            "परस्पर निर्भरता के कई नेटवर्क के माध्यम से एक प्रणाली में निकटता से एकीकृत पौधों, जानवरों और सूक्ष्म जीवों सहित जीवन रूपों की विविधता।",
            "खाली भूमि में नए पेड़ लगाने की प्रक्रिया।",
            "एक देश का विभिन्न भौगोलिक क्षेत्रों में विभाजन।"
        ],
        "options_gu": [
            "સૂર્યમંડળનો અભ્યાસ.",
            "પરસ્પર નિર્ભરતાના બહુવિધ નેટવર્ક દ્વારા સિસ્ટમમાં નજીકથી સંકલિત છોડ, પ્રાણીઓ અને સુક્ષ્મજીવો સહિત જીવન સ્વરૂપોની વિવિધતા.",
            "ખાલી જમીનમાં નવા વૃક્ષો વાવવાની પ્રક્રિયા.",
            "દેશનું વિવિધ ભૌગોલિક વિસ્તારોમાં વિભાજન."
        ],
        "correct_index": 1,
        "explanation": "Biodiversity is the immense variety of life on Earth, from the smallest bacteria to the largest whales. All these organisms interact with each other and their environment, creating a complex web of life essential for ecological balance.",
        "explanation_hi": "जैव विविधता पृथ्वी पर जीवन की विशाल विविधता है, सबसे छोटे बैक्टीरिया से लेकर सबसे बड़ी व्हेल तक। ये सभी जीव एक-दूसरे और अपने पर्यावरण के साथ बातचीत करते हैं, जिससे पारिस्थितिक संतुलन के लिए आवश्यक जीवन का एक जटिल जाल बनता है।",
        "explanation_gu": "જૈવવિવિધતા એ પૃથ્વી પરના જીવનની વિશાળ વિવિધતા છે, નાનામાં નાના બેક્ટેરિયાથી લઈને સૌથી મોટી વ્હેલ સુધી. આ તમામ સજીવો એકબીજા સાથે અને તેમના પર્યાવરણ સાથે ક્રિયાપ્રતિક્રિયા કરે છે, જે ઇકોલોજીકલ સંતુલન માટે જરૂરી જીવનની જટિલ જાળ બનાવે છે."
    }
]

data = {
    "metadata": {
        "id": "ncert_class10_geography_ch2",
        "title": "Geography Chapter 2: Forest and Wildlife Resources",
        "subject": "Social Science",
        "grade": "10"
    },
    "blocks": blocks
}

output_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_geography_ch2.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {len(blocks)} blocks to {output_path}")
