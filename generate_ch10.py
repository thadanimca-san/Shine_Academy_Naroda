import json

blocks = [
    {
        "id": "KOBJ_NCERT_C10_SCI_CH10_001",
        "type": "hook",
        "title": "The Most Advanced Camera: The Human Eye",
        "title_hi": "सबसे उन्नत कैमरा: मानव नेत्र",
        "title_gu": "સૌથી આધુનિક કૅમેરો: માનવ આંખ",
        "body": "Imagine a camera that never needs to be manually focused, automatically adjusts to bright sunlight or pitch darkness, and captures images in full 3D colour. You already have two of these! The human eye uses light and enables us to see the colourful world around us. But how exactly does this biological lens work?",
        "body_hi": "एक ऐसे कैमरे की कल्पना करें जिसे कभी मैन्युअल रूप से फोकस करने की आवश्यकता नहीं होती, तेज धूप या घने अंधेरे में स्वचालित रूप से समायोजित हो जाता है, और पूर्ण 3D रंग में चित्र कैप्चर करता है। आपके पास पहले से ही इनमें से दो हैं! मानव नेत्र प्रकाश का उपयोग करता है और हमें हमारे आस-पास की रंगीन दुनिया को देखने में सक्षम बनाता है। लेकिन वास्तव में यह जैविक लेंस कैसे काम करता है?",
        "body_gu": "એવા કેમેરાની કલ્પના કરો કે જેને ક્યારેય જાતે ફોકસ કરવાની જરૂર પડતી નથી, તેજસ્વી સૂર્યપ્રકાશ અથવા ગાઢ અંધારામાં આપમેળે ગોઠવાઈ જાય છે, અને સંપૂર્ણ 3D રંગમાં ચિત્રો લે છે. તમારી પાસે પહેલેથી જ આવા બે છે! માનવ આંખ પ્રકાશનો ઉપયોગ કરે છે અને આપણને આપણી આસપાસની રંગીન દુનિયા જોવા માટે સક્ષમ બનાવે છે. પરંતુ આ જૈવિક લેન્સ ખરેખર કેવી રીતે કાર્ય કરે છે?"
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH10_002",
        "type": "theory",
        "title": "Structure of the Human Eye",
        "title_hi": "मानव नेत्र की संरचना",
        "title_gu": "માનવ આંખની રચના",
        "body": "1. Cornea: The clear front window where light enters. Most refraction happens here.\n2. Iris & Pupil: The iris (coloured part) controls the size of the pupil (the dark center) to regulate the amount of light entering.\n3. Eye Lens: A crystalline, flexible convex lens that fine-tunes the focus.\n4. Ciliary Muscles: Muscles that change the shape (and focal length) of the lens.\n5. Retina: The light-sensitive screen at the back containing rods and cones, where the real and inverted image is formed.",
        "body_hi": "1. कॉर्निया (स्वच्छ मंडल): साफ सामने की खिड़की जहां से प्रकाश प्रवेश करता है। अधिकांश अपवर्तन यहीं होता है।\n2. परितारिका (Iris) और पुतली (Pupil): परितारिका (रंगीन भाग) प्रवेश करने वाले प्रकाश की मात्रा को नियंत्रित करने के लिए पुतली (गहरा केंद्र) के आकार को नियंत्रित करती है।\n3. नेत्र लेंस: एक क्रिस्टलीय, लचीला उत्तल लेंस जो फोकस को ठीक करता है।\n4. पक्ष्माभी पेशियाँ (Ciliary Muscles): ऐसी मांसपेशियां जो लेंस के आकार (और फोकस दूरी) को बदलती हैं।\n5. दृष्टिपटल (Retina): पीछे की प्रकाश-संवेदनशील स्क्रीन जिसमें छड़ और शंकु (rods and cones) होते हैं, जहां वास्तविक और उल्टा प्रतिबिंब बनता है।",
        "body_gu": "1. પારદર્શક પટલ (Cornea): આગળની સ્પષ્ટ બારી જ્યાંથી પ્રકાશ પ્રવેશે છે. મોટાભાગનું વક્રીભવન અહીં થાય છે.\n2. કનીનિકા (Iris) અને કીકી (Pupil): કનીનિકા (રંગીન ભાગ) પ્રવેશતા પ્રકાશની માત્રાને નિયંત્રિત કરવા કીકીના કદને નિયંત્રિત કરે છે.\n3. નેત્રમણિ (Eye Lens): એક સ્ફટિકમય, લવચીક ઉત્તલ લેન્સ જે ફોકસને વ્યવસ્થિત કરે છે.\n4. સિલિયરી સ્નાયુઓ: સ્નાયુઓ જે લેન્સનો આકાર (અને કેન્દ્રલંબાઈ) બદલે છે.\n5. નેત્રપટલ (Retina): પાછળના ભાગમાં આવેલો પ્રકાશ-સંવેદનશીલ પડદો જેમાં દંડ કોષો અને શંકુ કોષો હોય છે, જ્યાં વાસ્તવિક અને ઉલટું પ્રતિબિંબ રચાય છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH10_003",
        "type": "socratic_question",
        "title": "Power of Accommodation",
        "title_hi": "समंजन क्षमता",
        "title_gu": "સમાવેશ ક્ષમતા",
        "question": "If you look at a distant mountain and then immediately look at the lines on your palm, your eye instantly refocuses. Which part of the eye is responsible for actively changing the focal length of the eye lens?",
        "question_hi": "यदि आप एक दूर के पहाड़ को देखते हैं और फिर तुरंत अपनी हथेली की रेखाओं को देखते हैं, तो आपकी आंख तुरंत फिर से फोकस कर लेती है। आंख का कौन सा भाग नेत्र लेंस की फोकस दूरी को सक्रिय रूप से बदलने के लिए जिम्मेदार है?",
        "question_gu": "જો તમે દૂરના પર્વત તરફ જુઓ અને પછી તરત જ તમારી હથેળીની રેખાઓ જુઓ, તો તમારી આંખ તરત જ ફરીથી ફોકસ કરે છે. આંખનો કયો ભાગ નેત્રમણિની કેન્દ્રલંબાઈને સક્રિય રીતે બદલવા માટે જવાબદાર છે?",
        "options": [
            "The Retina",
            "The Cornea",
            "The Ciliary Muscles",
            "The Optic Nerve"
        ],
        "options_hi": [
            "दृष्टिपटल (Retina)",
            "कॉर्निया (Cornea)",
            "पक्ष्माभी पेशियाँ (Ciliary Muscles)",
            "दृष्टि तंत्रिका (Optic Nerve)"
        ],
        "options_gu": [
            "નેત્રપટલ (Retina)",
            "પારદર્શક પટલ (Cornea)",
            "સિલિયરી સ્નાયુઓ",
            "દૃષ્ટિ ચેતા (Optic Nerve)"
        ],
        "correct_index": 2,
        "explanation": "The ciliary muscles modify the curvature of the eye lens. To see distant objects, they relax (lens becomes thin, high focal length). To see nearby objects, they contract (lens becomes thick, low focal length). This ability is called Accommodation.",
        "explanation_hi": "पक्ष्माभी पेशियाँ नेत्र लेंस की वक्रता को बदलती हैं। दूर की वस्तुओं को देखने के लिए, वे शिथिल (relax) हो जाती हैं (लेंस पतला हो जाता है, उच्च फोकस दूरी)। पास की वस्तुओं को देखने के लिए, वे सिकुड़ जाती हैं (लेंस मोटा हो जाता है, कम फोकस दूरी)। इस क्षमता को समंजन (Accommodation) कहा जाता है।",
        "explanation_gu": "સિલિયરી સ્નાયુઓ નેત્રમણિની વક્રતામાં ફેરફાર કરે છે. દૂરની વસ્તુઓ જોવા માટે, તેઓ આરામ કરે છે (લેન્સ પાતળો બને છે, વધુ કેન્દ્રલંબાઈ). નજીકની વસ્તુઓ જોવા માટે, તેઓ સંકોચાય છે (લેન્સ જાડો બને છે, ઓછી કેન્દ્રલંબાઈ). આ ક્ષમતાને સમાવેશ ક્ષમતા (Accommodation) કહે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH10_004",
        "type": "theory",
        "title": "Defects of Vision and Their Correction",
        "title_hi": "दृष्टि दोष और उनका सुधार",
        "title_gu": "દૃષ્ટિની ખામીઓ અને તેનું નિવારણ",
        "body": "1. Myopia (Near-sightedness): A person can see nearby objects clearly but cannot see distant objects. Image forms IN FRONT of the retina. Corrected with a Concave lens.\n2. Hypermetropia (Far-sightedness): A person can see distant objects clearly but cannot see nearby objects. Image forms BEHIND the retina. Corrected with a Convex lens.\n3. Presbyopia: Age-related loss of accommodation. Ciliary muscles weaken, making nearby vision blurry. Often corrected with Bifocal lenses.",
        "body_hi": "1. निकट-दृष्टि दोष (Myopia): एक व्यक्ति पास की वस्तुओं को स्पष्ट रूप से देख सकता है लेकिन दूर की वस्तुओं को नहीं देख सकता है। प्रतिबिंब रेटिना के सामने बनता है। अवतल (Concave) लेंस से सुधारा जाता है।\n2. दीर्घ-दृष्टि दोष (Hypermetropia): एक व्यक्ति दूर की वस्तुओं को स्पष्ट रूप से देख सकता है लेकिन पास की वस्तुओं को नहीं देख सकता है। प्रतिबिंब रेटिना के पीछे बनता है। उत्तल (Convex) लेंस से सुधारा जाता है।\n3. जरा-दूरदृष्टिता (Presbyopia): उम्र से संबंधित समंजन क्षमता की हानि। पक्ष्माभी पेशियां कमजोर हो जाती हैं, जिससे पास की दृष्टि धुंधली हो जाती है। अक्सर द्विफोकसी (Bifocal) लेंस से सुधारा जाता है।",
        "body_gu": "1. માયોપિયા (લઘુદૃષ્ટિની ખામી): વ્યક્તિ નજીકની વસ્તુઓ સ્પષ્ટ જોઈ શકે છે પરંતુ દૂરની વસ્તુઓ જોઈ શકતી નથી. પ્રતિબિંબ નેત્રપટલની આગળ રચાય છે. અવતલ લેન્સ વડે સુધારી શકાય છે.\n2. હાઇપરમેટ્રોપિયા (ગુરુદૃષ્ટિની ખામી): વ્યક્તિ દૂરની વસ્તુઓ સ્પષ્ટ જોઈ શકે છે પરંતુ નજીકની વસ્તુઓ જોઈ શકતી નથી. પ્રતિબિંબ નેત્રપટલની પાછળ રચાય છે. ઉત્તલ લેન્સ વડે સુધારી શકાય છે.\n3. પ્રેસબાયોપિયા: ઉંમર સંબંધિત સમાવેશ ક્ષમતામાં ઘટાડો. સિલિયરી સ્નાયુઓ નબળા પડે છે, જેનાથી નજીકની દૃષ્ટિ ઝાંખી બને છે. મોટેભાગે બાયફોકલ લેન્સ વડે સુધારવામાં આવે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH10_005",
        "type": "theory",
        "title": "Refraction Through a Prism & Dispersion",
        "title_hi": "प्रिज्म के माध्यम से अपवर्तन और विक्षेपण",
        "title_gu": "પ્રિઝમ વડે વક્રીભવન અને વિભાજન",
        "body": "When white light passes through a glass prism, it bends (refracts). Because different colours of light bend at different angles (red bends the least, violet bends the most), the white light splits into a band of seven colours (VIBGYOR). This splitting of light is called Dispersion. A rainbow is a natural spectrum caused by dispersion of sunlight by tiny water droplets in the atmosphere acting like small prisms.",
        "body_hi": "जब श्वेत प्रकाश कांच के प्रिज्म से होकर गुजरता है, तो यह मुड़ (अपवर्तित) जाता है। क्योंकि प्रकाश के अलग-अलग रंग अलग-अलग कोणों पर मुड़ते हैं (लाल सबसे कम मुड़ता है, बैंगनी सबसे अधिक मुड़ता है), श्वेत प्रकाश सात रंगों (VIBGYOR) के बैंड में विभाजित हो जाता है। प्रकाश के इस विभाजन को विक्षेपण (Dispersion) कहा जाता है। इंद्रधनुष एक प्राकृतिक स्पेक्ट्रम है जो वायुमंडल में छोटी पानी की बूंदों (जो छोटे प्रिज्म की तरह काम करती हैं) द्वारा सूर्य के प्रकाश के विक्षेपण के कारण होता है।",
        "body_gu": "જ્યારે શ્વેત પ્રકાશ કાચના પ્રિઝમમાંથી પસાર થાય છે, ત્યારે તે વળે (વક્રીભવન) છે. કારણ કે પ્રકાશના જુદા જુદા રંગો જુદા જુદા ખૂણાઓ પર વળે છે (લાલ સૌથી ઓછો વળે છે, જાંબલી સૌથી વધુ વળે છે), શ્વેત પ્રકાશ સાત રંગોના પટ્ટામાં (VIBGYOR) વિભાજિત થાય છે. પ્રકાશના આ છૂટા પડવાની ઘટનાને વિભાજન (Dispersion) કહે છે. મેઘધનુષ્ય એ વાતાવરણમાં રહેલા પાણીના નાના ટીપાં (જે નાના પ્રિઝમ તરીકે વર્તે છે) દ્વારા સૂર્યપ્રકાશના વિભાજનથી રચાતો કુદરતી વર્ણપટ છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH10_006",
        "type": "theory",
        "title": "Atmospheric Refraction & Scattering of Light",
        "title_hi": "वायुमंडलीय अपवर्तन और प्रकाश का प्रकीर्णन",
        "title_gu": "વાતાવરણીય વક્રીભવન અને પ્રકાશનું પ્રકીર્ણન",
        "body": "The Earth's atmosphere has layers of air with different densities. As starlight passes through these layers, it continuously refracts, causing the star's apparent position to fluctuate constantly—making the star 'twinkle'.\nScattering: Very fine particles in the atmosphere scatter short wavelengths (blue light) more effectively than long wavelengths (red). This scattered blue light makes the sky appear blue during the day. At sunset, light travels through more atmosphere, scattering away most of the blue and leaving the red light to reach our eyes.",
        "body_hi": "पृथ्वी के वायुमंडल में विभिन्न घनत्व वाली हवा की परतें हैं। जैसे ही तारों का प्रकाश इन परतों से गुजरता है, यह लगातार अपवर्तित होता है, जिससे तारे की स्पष्ट स्थिति में लगातार उतार-चढ़ाव होता है - जिससे तारा 'टिमटिमाता' है।\nप्रकीर्णन (Scattering): वायुमंडल में बहुत बारीक कण लंबी तरंग दैर्ध्य (लाल) की तुलना में छोटी तरंग दैर्ध्य (नीला प्रकाश) को अधिक प्रभावी ढंग से प्रकीर्णित करते हैं। यह बिखरा हुआ नीला प्रकाश दिन के दौरान आकाश को नीला दिखाता है। सूर्यास्त के समय, प्रकाश अधिक वायुमंडल से होकर यात्रा करता है, जिससे अधिकांश नीला रंग बिखर जाता है और लाल प्रकाश हमारी आंखों तक पहुंचता है।",
        "body_gu": "પૃથ્વીના વાતાવરણમાં જુદી જુદી ઘનતાવાળા હવાના સ્તરો છે. જ્યારે તારાનો પ્રકાશ આ સ્તરોમાંથી પસાર થાય છે, ત્યારે તેનું સતત વક્રીભવન થાય છે, જેના કારણે તારાનું આભાસી સ્થાન સતત બદલાય છે - જેનાથી તારો 'ટમટમે' છે.\nપ્રકીર્ણન (Scattering): વાતાવરણમાં રહેલા ખૂબ જ બારીક કણો લાંબી તરંગલંબાઈ (લાલ) કરતાં ટૂંકી તરંગલંબાઈ (વાદળી પ્રકાશ) નું વધુ અસરકારક રીતે પ્રકીર્ણન કરે છે. આ વિખરાયેલો વાદળી પ્રકાશ દિવસ દરમિયાન આકાશને વાદળી બનાવે છે. સૂર્યાસ્ત સમયે, પ્રકાશ વધુ વાતાવરણમાંથી પસાર થાય છે, જેમાં મોટાભાગનો વાદળી રંગ વિખેરાઈ જાય છે અને લાલ પ્રકાશ આપણી આંખો સુધી પહોંચે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH10_007",
        "type": "mcq",
        "title": "NCERT Exercise Q1",
        "title_hi": "NCERT अभ्यास Q1",
        "title_gu": "NCERT સ્વાધ્યાય Q1",
        "question": "The human eye can focus objects at different distances by adjusting the focal length of the eye lens. This is due to",
        "question_hi": "मानव नेत्र अभिनेत्र लेंस की फोकस दूरी को समायोजित करके विभिन्न दूरियों पर रखी वस्तुओं को फोकसित कर सकता है। ऐसा हो पाने का कारण है:",
        "question_gu": "માનવ આંખ નેત્રમણિની કેન્દ્રલંબાઈમાં ફેરફાર કરીને જુદા જુદા અંતરે રહેલી વસ્તુઓને સ્પષ્ટ જોઈ શકે છે. આવું શાના લીધે થાય છે?",
        "options": [
            "Presbyopia",
            "Accommodation",
            "Near-sightedness",
            "Far-sightedness"
        ],
        "options_hi": [
            "जरा-दूरदृष्टिता",
            "समंजन (Accommodation)",
            "निकट-दृष्टि दोष",
            "दीर्घ-दृष्टि दोष"
        ],
        "options_gu": [
            "પ્રેસબાયોપિયા",
            "સમાવેશ ક્ષમતા (Accommodation)",
            "લઘુદૃષ્ટિની ખામી",
            "ગુરુદૃષ્ટિની ખામી"
        ],
        "correct_index": 1,
        "explanation": "Accommodation is the active ability of the ciliary muscles to change the curvature and focal length of the eye lens to focus on objects at various distances.",
        "explanation_hi": "समंजन (Accommodation) विभिन्न दूरियों पर वस्तुओं को केंद्रित करने के लिए पक्ष्माभी पेशियों द्वारा नेत्र लेंस की वक्रता और फोकस दूरी को बदलने की सक्रिय क्षमता है।",
        "explanation_gu": "સમાવેશ ક્ષમતા (Accommodation) એ વિવિધ અંતરે રહેલી વસ્તુઓ પર ધ્યાન કેન્દ્રિત કરવા માટે સિલિયરી સ્નાયુઓ દ્વારા નેત્રમણિની વક્રતા અને કેન્દ્રલંબાઈ બદલવાની સક્રિય ક્ષમતા છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH10_008",
        "type": "mcq",
        "title": "NCERT Exercise Q2",
        "title_hi": "NCERT अभ्यास Q2",
        "title_gu": "NCERT સ્વાધ્યાય Q2",
        "question": "The human eye forms the image of an object at its",
        "question_hi": "मानव नेत्र जिस भाग पर किसी वस्तु का प्रतिबिंब बनाते हैं, वह है:",
        "question_gu": "માનવ આંખમાં વસ્તુનું પ્રતિબિંબ ક્યાં રચાય છે?",
        "options": [
            "cornea",
            "iris",
            "pupil",
            "retina"
        ],
        "options_hi": [
            "कॉर्निया",
            "परितारिका",
            "पुतली",
            "दृष्टिपटल (रेटिना)"
        ],
        "options_gu": [
            "પારદર્શક પટલ",
            "કનીનિકા",
            "કીકી",
            "નેત્રપટલ (રેટિના)"
        ],
        "correct_index": 3,
        "explanation": "The retina acts as a light-sensitive screen at the back of the eye where the real and inverted image is formed by the eye lens.",
        "explanation_hi": "रेटिना आंख के पीछे एक प्रकाश-संवेदनशील स्क्रीन के रूप में कार्य करता है जहां नेत्र लेंस द्वारा वास्तविक और उल्टा प्रतिबिंब बनता है।",
        "explanation_gu": "રેટિના આંખની પાછળના ભાગમાં પ્રકાશ-સંવેદનશીલ પડદા તરીકે કાર્ય કરે છે જ્યાં નેત્રમણિ દ્વારા વાસ્તવિક અને ઉલટું પ્રતિબિંબ રચાય છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH10_009",
        "type": "mcq",
        "title": "NCERT Exercise Q3",
        "title_hi": "NCERT अभ्यास Q3",
        "title_gu": "NCERT સ્વાધ્યાય Q3",
        "question": "The least distance of distinct vision for a young adult with normal vision is about",
        "question_hi": "सामान्य दृष्टि के तरुण वयस्क के लिए सुस्पष्ट दर्शन की अल्पतम दूरी होती है, लगभग:",
        "question_gu": "સામાન્ય દૃષ્ટિ ધરાવતા યુવાન પુખ્ત વયના વ્યક્તિ માટે સ્પષ્ટ દૃષ્ટિનું લઘુત્તમ અંતર આશરે કેટલું હોય છે?",
        "options": [
            "25 m",
            "2.5 cm",
            "25 cm",
            "2.5 m"
        ],
        "options_hi": [
            "25 मीटर",
            "2.5 सेमी",
            "25 सेमी",
            "2.5 मीटर"
        ],
        "options_gu": [
            "25 મીટર",
            "2.5 સેમી",
            "25 સેમી",
            "2.5 મીટર"
        ],
        "correct_index": 2,
        "explanation": "For a normal eye, the near point (least distance of distinct vision) is 25 cm. Objects placed closer than 25 cm cannot be focused clearly without strain.",
        "explanation_hi": "एक सामान्य आंख के लिए, निकट बिंदु (सुस्पष्ट दर्शन की अल्पतम दूरी) 25 सेमी है। 25 सेमी से अधिक करीब रखी वस्तुओं को बिना तनाव के स्पष्ट रूप से केंद्रित नहीं किया जा सकता है।",
        "explanation_gu": "સામાન્ય આંખ માટે, નજીકનું બિંદુ (સ્પષ્ટ દૃષ્ટિનું લઘુત્તમ અંતર) 25 સેમી છે. 25 સેમી કરતાં વધુ નજીક મૂકેલી વસ્તુઓને આંખ પર તાણ આપ્યા વિના સ્પષ્ટપણે ફોકસ કરી શકાતી નથી."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH10_010",
        "type": "mcq",
        "title": "NCERT Exercise Q4",
        "title_hi": "NCERT अभ्यास Q4",
        "title_gu": "NCERT સ્વાધ્યાય Q4",
        "question": "The change in focal length of an eye lens is caused by the action of the",
        "question_hi": "अभिनेत्र लेंस की फोकस दूरी में परिवर्तन किया जाता है:",
        "question_gu": "નેત્રમણિની કેન્દ્રલંબાઈમાં ફેરફાર કોની ક્રિયા દ્વારા થાય છે?",
        "options": [
            "pupil",
            "retina",
            "ciliary muscles",
            "iris"
        ],
        "options_hi": [
            "पुतली द्वारा",
            "दृष्टिपटल द्वारा",
            "पक्ष्माभी पेशियों द्वारा",
            "परितारिका द्वारा"
        ],
        "options_gu": [
            "કીકી દ્વારા",
            "નેત્રપટલ દ્વારા",
            "સિલિયરી સ્નાયુઓ દ્વારા",
            "કનીનિકા દ્વારા"
        ],
        "correct_index": 2,
        "explanation": "Ciliary muscles change the curvature of the eye lens. When they contract, the lens becomes thicker (shorter focal length). When they relax, the lens becomes thinner (longer focal length).",
        "explanation_hi": "पक्ष्माभी पेशियाँ नेत्र लेंस की वक्रता को बदलती हैं। जब वे सिकुड़ती हैं, तो लेंस मोटा हो जाता है (कम फोकस दूरी)। जब वे शिथिल होती हैं, तो लेंस पतला हो जाता है (लंबी फोकस दूरी)।",
        "explanation_gu": "સિલિયરી સ્નાયુઓ નેત્રમણિની વક્રતામાં ફેરફાર કરે છે. જ્યારે તેઓ સંકોચાય છે, ત્યારે લેન્સ જાડો બને છે (ઓછી કેન્દ્રલંબાઈ). જ્યારે તેઓ આરામ કરે છે, ત્યારે લેન્સ પાતળો બને છે (લાંબી કેન્દ્રલંબાઈ)."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH10_011",
        "type": "mcq",
        "title": "NCERT Exercise Q5",
        "title_hi": "NCERT अभ्यास Q5",
        "title_gu": "NCERT સ્વાધ્યાય Q5",
        "question": "A person needs a lens of power -5.5 dioptres for correcting his distant vision. For correcting his near vision he needs a lens of power +1.5 dioptre. What is the focal length of the lens required for correcting distant vision and near vision respectively?",
        "question_hi": "किसी व्यक्ति को अपनी दूर की दृष्टि को संशोधित करने के लिए -5.5 डायोप्टर क्षमता के लेंस की आवश्यकता है। अपनी निकट की दृष्टि को संशोधित करने के लिए उसे +1.5 डायोप्टर क्षमता के लेंस की आवश्यकता है। दूर की दृष्टि और निकट की दृष्टि को संशोधित करने के लिए आवश्यक लेंस की फोकस दूरी क्रमशः क्या है?",
        "question_gu": "કોઈ વ્યક્તિને તેની દૂરની દૃષ્ટિ સુધારવા માટે -5.5 ડાયોપ્ટર પાવરના લેન્સની જરૂર છે. તેની નજીકની દૃષ્ટિ સુધારવા માટે તેને +1.5 ડાયોપ્ટર પાવરના લેન્સની જરૂર છે. દૂરની દૃષ્ટિ અને નજીકની દૃષ્ટિ સુધારવા માટે જરૂરી લેન્સની કેન્દ્રલંબાઈ અનુક્રમે કેટલી છે?",
        "options": [
            "Distant: -0.18 m, Near: +0.67 m",
            "Distant: +0.18 m, Near: -0.67 m",
            "Distant: -5.5 m, Near: +1.5 m",
            "Distant: -18 cm, Near: +67 cm"
        ],
        "options_hi": [
            "दूर दृष्टि: -0.18 मीटर, निकट दृष्टि: +0.67 मीटर",
            "दूर दृष्टि: +0.18 मीटर, निकट दृष्टि: -0.67 मीटर",
            "दूर दृष्टि: -5.5 मीटर, निकट दृष्टि: +1.5 मीटर",
            "दूर दृष्टि: -18 सेमी, निकट दृष्टि: +67 सेमी"
        ],
        "options_gu": [
            "દૂરની દૃષ્ટિ: -0.18 મીટર, નજીકની દૃષ્ટિ: +0.67 મીટર",
            "દૂરની દૃષ્ટિ: +0.18 મીટર, નજીકની દૃષ્ટિ: -0.67 મીટર",
            "દૂરની દૃષ્ટિ: -5.5 મીટર, નજીકની દૃષ્ટિ: +1.5 મીટર",
            "દૂરની દૃષ્ટિ: -18 સેમી, નજીકની દૃષ્ટિ: +67 સેમી"
        ],
        "correct_index": 0,
        "explanation": "Formula: f = 1/P. For distant vision: P = -5.5 D, so f = 1 / -5.5 = -0.181 m (Concave lens). For near vision: P = +1.5 D, so f = 1 / 1.5 = +0.666 m (Convex lens).",
        "explanation_hi": "सूत्र: f = 1/P। दूर दृष्टि के लिए: P = -5.5 D, इसलिए f = 1 / -5.5 = -0.181 मीटर (अवतल लेंस)। निकट दृष्टि के लिए: P = +1.5 D, इसलिए f = 1 / 1.5 = +0.666 मीटर (उत्तल लेंस)।",
        "explanation_gu": "સૂત્ર: f = 1/P. દૂરની દૃષ્ટિ માટે: P = -5.5 D, તેથી f = 1 / -5.5 = -0.181 મીટર (અવતલ લેન્સ). નજીકની દૃષ્ટિ માટે: P = +1.5 D, તેથી f = 1 / 1.5 = +0.666 મીટર (ઉત્તલ લેન્સ)."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH10_012",
        "type": "mcq",
        "title": "NCERT Exercise Q6",
        "title_hi": "NCERT अभ्यास Q6",
        "title_gu": "NCERT સ્વાધ્યાય Q6",
        "question": "The far point of a myopic person is 80 cm in front of the eye. What is the nature and power of the lens required to correct the problem?",
        "question_hi": "किसी निकट-दृष्टि दोष (myopic) वाले व्यक्ति का दूर बिंदु नेत्र के सामने 80 सेमी पर है। इस समस्या को दूर करने के लिए आवश्यक लेंस की प्रकृति और क्षमता क्या है?",
        "question_gu": "માયોપિયા (લઘુદૃષ્ટિની ખામી) ધરાવતા વ્યક્તિનું દૂર બિંદુ આંખની સામે 80 સેમી છે. આ સમસ્યાને સુધારવા માટે જરૂરી લેન્સનો પ્રકાર અને પાવર શું છે?",
        "options": [
            "Convex lens, Power = +1.25 D",
            "Concave lens, Power = -1.25 D",
            "Concave lens, Power = -0.80 D",
            "Convex lens, Power = +0.80 D"
        ],
        "options_hi": [
            "उत्तल लेंस, क्षमता = +1.25 D",
            "अवतल लेंस, क्षमता = -1.25 D",
            "अवतल लेंस, क्षमता = -0.80 D",
            "उत्तल लेंस, क्षमता = +0.80 D"
        ],
        "options_gu": [
            "ઉત્તલ લેન્સ, પાવર = +1.25 D",
            "અવતલ લેન્સ, પાવર = -1.25 D",
            "અવતલ લેન્સ, પાવર = -0.80 D",
            "ઉત્તલ લેન્સ, પાવર = +0.80 D"
        ],
        "correct_index": 1,
        "explanation": "To correct myopia, the lens must make an object at infinity (u = -∞) appear at the far point (v = -80 cm). Using 1/f = 1/v - 1/u => 1/f = 1/-80 - 1/-∞ => f = -80 cm = -0.8 m. Power P = 1/f = 1 / -0.8 = -1.25 D. The negative sign indicates a Concave lens.",
        "explanation_hi": "मायोपिया को ठीक करने के लिए, लेंस को अनंत (u = -∞) पर रखी वस्तु को दूर बिंदु (v = -80 सेमी) पर दिखाना चाहिए। 1/f = 1/v - 1/u का उपयोग करके => 1/f = 1/-80 - 0 => f = -80 सेमी = -0.8 मीटर। क्षमता P = 1/f = 1 / -0.8 = -1.25 D। ऋणात्मक चिह्न अवतल लेंस को दर्शाता है।",
        "explanation_gu": "માયોપિયા સુધારવા માટે, લેન્સે અનંત અંતરે (u = -∞) રહેલી વસ્તુને દૂર બિંદુ (v = -80 સેમી) પર દર્શાવવી જોઈએ. 1/f = 1/v - 1/u નો ઉપયોગ કરતા => 1/f = 1/-80 - 0 => f = -80 સેમી = -0.8 મીટર. પાવર P = 1/f = 1 / -0.8 = -1.25 D. ઋણ નિશાની અવતલ લેન્સ દર્શાવે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH10_013",
        "type": "mcq",
        "title": "NCERT Exercise Q8",
        "title_hi": "NCERT अभ्यास Q8",
        "title_gu": "NCERT સ્વાધ્યાય Q8",
        "question": "Why is a normal eye not able to see clearly the objects placed closer than 25 cm?",
        "question_hi": "सामान्य नेत्र 25 सेमी से निकट रखी वस्तुओं को सुस्पष्ट क्यों नहीं देख पाते?",
        "question_gu": "સામાન્ય આંખ 25 સેમી કરતાં વધુ નજીક મૂકેલી વસ્તુઓને સ્પષ્ટ કેમ જોઈ શકતી નથી?",
        "options": [
            "Because the retina cannot detect objects that close.",
            "Because light rays from very close objects are scattered by the cornea.",
            "Because the ciliary muscles cannot contract any further to decrease the focal length below a certain minimum limit.",
            "Because the pupil becomes too small to let light in."
        ],
        "options_hi": [
            "क्योंकि रेटिना इतनी करीब की वस्तुओं का पता नहीं लगा सकता है।",
            "क्योंकि बहुत करीब की वस्तुओं से प्रकाश की किरणें कॉर्निया द्वारा बिखेर दी जाती हैं।",
            "क्योंकि पक्ष्माभी पेशियाँ फोकस दूरी को एक निश्चित न्यूनतम सीमा से नीचे कम करने के लिए और अधिक नहीं सिकुड़ सकती हैं।",
            "क्योंकि पुतली प्रकाश को अंदर आने देने के लिए बहुत छोटी हो जाती है।"
        ],
        "options_gu": [
            "કારણ કે નેત્રપટલ આટલી નજીકની વસ્તુઓને શોધી શકતું નથી.",
            "કારણ કે ખૂબ જ નજીકની વસ્તુઓમાંથી આવતા પ્રકાશના કિરણો પારદર્શક પટલ દ્વારા વિખેરાઈ જાય છે.",
            "કારણ કે કેન્દ્રલંબાઈને ચોક્કસ ન્યૂનતમ મર્યાદાથી નીચે ઘટાડવા માટે સિલિયરી સ્નાયુઓ વધુ સંકોચાઈ શકતા નથી.",
            "કારણ કે પ્રકાશને અંદર પ્રવેશવા દેવા માટે કીકી ખૂબ જ નાની થઈ જાય છે."
        ],
        "correct_index": 2,
        "explanation": "The ciliary muscles can only bulge the eye lens up to a certain maximum thickness, giving a minimum focal length. If an object is brought closer than 25 cm, the lens cannot become thick enough to focus the image exactly on the retina, causing blurriness.",
        "explanation_hi": "पक्ष्माभी पेशियाँ नेत्र लेंस को केवल एक निश्चित अधिकतम मोटाई तक ही फुला सकती हैं, जिससे न्यूनतम फोकस दूरी प्राप्त होती है। यदि कोई वस्तु 25 सेमी से अधिक निकट लाई जाती है, तो लेंस रेटिना पर प्रतिबिंब को ठीक से केंद्रित करने के लिए पर्याप्त मोटा नहीं हो पाता है, जिससे धुंधलापन होता है।",
        "explanation_gu": "સિલિયરી સ્નાયુઓ નેત્રમણિને માત્ર ચોક્કસ મહત્તમ જાડાઈ સુધી જ ઉપસાવી શકે છે, જે ન્યૂનતમ કેન્દ્રલંબાઈ આપે છે. જો વસ્તુને 25 સેમી કરતાં વધુ નજીક લાવવામાં આવે, તો લેન્સ પ્રતિબિંબને બરાબર નેત્રપટલ પર કેન્દ્રિત કરવા માટે પૂરતો જાડો બની શકતો નથી, જેનાથી ઝાંખપ આવે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH10_014",
        "type": "mcq",
        "title": "NCERT Exercise Q10",
        "title_hi": "NCERT अभ्यास Q10",
        "title_gu": "NCERT સ્વાધ્યાય Q10",
        "question": "Why do stars twinkle?",
        "question_hi": "तारे क्यों टिमटिमाते हैं?",
        "question_gu": "તારાઓ શા માટે ટમટમે છે?",
        "options": [
            "Due to their own fluctuating nuclear reactions.",
            "Due to the continuous refraction of starlight as it passes through the moving layers of Earth's atmosphere having different densities.",
            "Because planets pass in front of them repeatedly.",
            "Because they emit light in pulses."
        ],
        "options_hi": [
            "उनकी अपनी उतार-चढ़ाव वाली परमाणु प्रतिक्रियाओं के कारण।",
            "पृथ्वी के वायुमंडल (विभिन्न घनत्व वाले) की चलती परतों से गुजरने पर तारों के प्रकाश के निरंतर अपवर्तन के कारण।",
            "क्योंकि ग्रह बार-बार उनके सामने से गुजरते हैं।",
            "क्योंकि वे प्रकाश को स्पंदन (pulses) में उत्सर्जित करते हैं।"
        ],
        "options_gu": [
            "તેમની પોતાની બદલાતી પરમાણુ પ્રતિક્રિયાઓને કારણે.",
            "જુદી જુદી ઘનતાવાળા પૃથ્વીના વાતાવરણના ફરતા સ્તરોમાંથી પસાર થતાં તારાના પ્રકાશના સતત વક્રીભવનને કારણે.",
            "કારણ કે ગ્રહો વારંવાર તેમની સામેથી પસાર થાય છે.",
            "કારણ કે તેઓ પ્રકાશનું પલ્સ સ્વરૂપે ઉત્સર્જન કરે છે."
        ],
        "correct_index": 1,
        "explanation": "Atmospheric refraction occurs in a medium of gradually changing refractive index. Since the physical conditions of the earth's atmosphere are not stationary, the apparent position of the star fluctuates and the amount of starlight entering the eye flickers, causing the twinkling effect.",
        "explanation_hi": "वायुमंडलीय अपवर्तन धीरे-धीरे बदलते अपवर्तनांक के माध्यम में होता है। चूंकि पृथ्वी के वायुमंडल की भौतिक स्थितियां स्थिर नहीं हैं, इसलिए तारे की स्पष्ट स्थिति में उतार-चढ़ाव होता है और आंख में प्रवेश करने वाले तारों के प्रकाश की मात्रा टिमटिमाती है।",
        "explanation_gu": "ધીમે ધીમે બદલાતા વક્રીભવનાંકના માધ્યમમાં વાતાવરણીય વક્રીભવન થાય છે. પૃથ્વીના વાતાવરણની ભૌતિક પરિસ્થિતિઓ સ્થિર ન હોવાથી, તારાનું આભાસી સ્થાન બદલાય છે અને આંખમાં પ્રવેશતા તારાના પ્રકાશની માત્રામાં વધઘટ થાય છે, જે ટમટમવાની અસર પેદા કરે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH10_015",
        "type": "mcq",
        "title": "NCERT Exercise Q11",
        "title_hi": "NCERT अभ्यास Q11",
        "title_gu": "NCERT સ્વાધ્યાય Q11",
        "question": "Explain why the planets do not twinkle.",
        "question_hi": "व्याख्या कीजिए कि ग्रह क्यों नहीं टिमटिमाते।",
        "question_gu": "સમજાવો કે ગ્રહો કેમ ટમટમતા નથી.",
        "options": [
            "Planets do not emit their own light, so they cannot twinkle.",
            "Planets are much closer to Earth and thus act as extended sources of light (a collection of many point sources). The total variations in the amount of light entering our eye from all individual point sources average out to zero.",
            "Planets are surrounded by thick atmospheres that stop the twinkling effect.",
            "Planets move too fast across the sky for the twinkling to be noticed."
        ],
        "options_hi": [
            "ग्रह अपना प्रकाश उत्सर्जित नहीं करते हैं, इसलिए वे टिमटिमा नहीं सकते।",
            "ग्रह पृथ्वी के बहुत करीब हैं और इस प्रकार प्रकाश के विस्तारित स्रोतों (कई बिंदु स्रोतों का एक संग्रह) के रूप में कार्य करते हैं। सभी व्यक्तिगत बिंदु स्रोतों से हमारी आंख में प्रवेश करने वाले प्रकाश की मात्रा में कुल भिन्नता औसतन शून्य हो जाती है।",
            "ग्रह घने वायुमंडल से घिरे होते हैं जो टिमटिमाने वाले प्रभाव को रोकते हैं।",
            "ग्रह आकाश में बहुत तेज़ी से आगे बढ़ते हैं जिससे टिमटिमाना दिखाई नहीं देता।"
        ],
        "options_gu": [
            "ગ્રહો પોતાનો પ્રકાશ ઉત્સર્જિત કરતા નથી, તેથી તેઓ ટમટમી શકતા નથી.",
            "ગ્રહો પૃથ્વીની ખૂબ નજીક છે અને આથી પ્રકાશના વિસ્તૃત સ્ત્રોતો (ઘણા બિંદુ સ્ત્રોતોનો સંગ્રહ) તરીકે વર્તે છે. તમામ વ્યક્તિગત બિંદુ સ્ત્રોતોમાંથી આપણી આંખમાં પ્રવેશતા પ્રકાશની માત્રામાં થતો કુલ ફેરફાર સરેરાશ શૂન્ય થઈ જાય છે.",
            "ગ્રહો ગાઢ વાતાવરણથી ઘેરાયેલા હોય છે જે ટમટમવાની અસરને અટકાવે છે.",
            "આકાશમાં ગ્રહો ખૂબ ઝડપથી આગળ વધતા હોવાથી ટમટમવું દેખાતું નથી."
        ],
        "correct_index": 1,
        "explanation": "Stars are incredibly far away, acting like single points of light that can easily flicker when refracted. Planets are much closer and appear as larger discs of light. The dimming of one part of the planet's disc is canceled out by the brightening of another part, so the overall brightness remains steady.",
        "explanation_hi": "तारे अविश्वसनीय रूप से दूर हैं, जो प्रकाश के एकल बिंदुओं की तरह कार्य करते हैं जो अपवर्तित होने पर आसानी से टिमटिमा सकते हैं। ग्रह बहुत करीब हैं और प्रकाश की बड़ी डिस्क के रूप में दिखाई देते हैं। ग्रह की डिस्क के एक हिस्से के कम होने की भरपाई दूसरे हिस्से के चमकने से हो जाती है, इसलिए कुल चमक स्थिर रहती है।",
        "explanation_gu": "તારાઓ અવિશ્વસનીય રીતે દૂર છે, જે પ્રકાશના એકલ બિંદુઓ તરીકે વર્તે છે જે વક્રીભવન થવા પર સરળતાથી ટમટમી શકે છે. ગ્રહો ખૂબ નજીક છે અને પ્રકાશની મોટી ડિસ્ક તરીકે દેખાય છે. ગ્રહની ડિસ્કના એક ભાગમાં થતો ઘટાડો બીજા ભાગના પ્રકાશથી સરભર થઈ જાય છે, તેથી એકંદર તેજસ્વિતા સ્થિર રહે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH10_016",
        "type": "mcq",
        "title": "NCERT Exercise Q12",
        "title_hi": "NCERT अभ्यास Q12",
        "title_gu": "NCERT સ્વાધ્યાય Q12",
        "question": "Why does the Sun appear reddish early in the morning?",
        "question_hi": "सूर्योदय के समय सूर्य रक्ताभ (लाल) क्यों प्रतीत होता है?",
        "question_gu": "વહેલી સવારે સૂર્યોદય વખતે સૂર્ય લાલાશ પડતો શા માટે દેખાય છે?",
        "options": [
            "The Sun is cooler in the morning, making it glow red.",
            "Light from the Sun near the horizon passes through thicker layers of air. The shorter wavelengths (blue) are scattered away by particles, leaving mainly longer wavelengths (red) to reach our eyes.",
            "Morning mist absorbs all colors except red.",
            "The ozone layer shifts the light spectrum to the red side at dawn."
        ],
        "options_hi": [
            "सुबह के समय सूर्य अधिक ठंडा होता है, जिससे वह लाल चमकता है।",
            "क्षैतिज (horizon) के पास सूर्य का प्रकाश हवा की मोटी परतों से होकर गुजरता है। छोटी तरंग दैर्ध्य (नीला) कणों द्वारा बिखेर दी जाती है, जिससे मुख्य रूप से लंबी तरंग दैर्ध्य (लाल) हमारी आंखों तक पहुंचती है।",
            "सुबह की धुंध लाल को छोड़कर सभी रंगों को अवशोषित कर लेती है।",
            "ओजोन परत भोर में प्रकाश स्पेक्ट्रम को लाल पक्ष में बदल देती है।"
        ],
        "options_gu": [
            "સવારમાં સૂર્ય વધુ ઠંડો હોય છે, જેનાથી તે લાલ ચમકે છે.",
            "ક્ષિતિજ (horizon) પાસે સૂર્યનો પ્રકાશ હવાના જાડા સ્તરોમાંથી પસાર થાય છે. ટૂંકી તરંગલંબાઈ (વાદળી) કણો દ્વારા વિખેરાઈ જાય છે, જેનાથી મુખ્યત્વે લાંબી તરંગલંબાઈ (લાલ) આપણી આંખો સુધી પહોંચે છે.",
            "સવારનું ધુમ્મસ લાલ સિવાયના તમામ રંગોને શોષી લે છે.",
            "ઓઝોન સ્તર પરોઢિયે પ્રકાશના વર્ણપટને લાલ બાજુ તરફ ખસેડે છે."
        ],
        "correct_index": 1,
        "explanation": "At sunrise, the Sun is near the horizon. Its light travels a longer path through the Earth's atmosphere than at noon. The tiny air molecules scatter the short blue wavelengths out of our line of sight, allowing the least scattered red light to safely reach our eyes.",
        "explanation_hi": "सूर्योदय के समय सूर्य क्षैतिज के पास होता है। दोपहर की तुलना में इसका प्रकाश पृथ्वी के वायुमंडल के माध्यम से लंबा रास्ता तय करता है। छोटे वायु अणु हमारी दृष्टि की रेखा से छोटी नीली तरंग दैर्ध्य को बिखेर देते हैं, जिससे सबसे कम बिखरा हुआ लाल प्रकाश हमारी आंखों तक सुरक्षित रूप से पहुंच जाता है।",
        "explanation_gu": "સૂર્યોદય સમયે સૂર્ય ક્ષિતિજની નજીક હોય છે. બપોરની સરખામણીમાં તેનો પ્રકાશ પૃથ્વીના વાતાવરણમાંથી લાંબો માર્ગ કાપે છે. હવાના નાના અણુઓ આપણી દૃષ્ટિરેખામાંથી ટૂંકી વાદળી તરંગલંબાઈને વિખેરી નાખે છે, જેનાથી સૌથી ઓછો વિખેરાયેલો લાલ પ્રકાશ સુરક્ષિત રીતે આપણી આંખો સુધી પહોંચે છે."
    },
    {
        "id": "KOBJ_NCERT_C10_SCI_CH10_017",
        "type": "mcq",
        "title": "NCERT Exercise Q13",
        "title_hi": "NCERT अभ्यास Q13",
        "title_gu": "NCERT સ્વાધ્યાય Q13",
        "question": "Why does the sky appear dark instead of blue to an astronaut?",
        "question_hi": "किसी अंतरिक्ष यात्री को आकाश नीले की अपेक्षा काला क्यों प्रतीत होता है?",
        "question_gu": "અંતરિક્ષ યાત્રીને આકાશ વાદળીને બદલે કાળું શા માટે દેખાય છે?",
        "options": [
            "Because the space suit visor blocks blue light.",
            "Because there is no atmosphere in space to scatter sunlight in all directions.",
            "Because the sun doesn't shine in outer space.",
            "Because astronauts are colour-blind in zero gravity."
        ],
        "options_hi": [
            "क्योंकि स्पेस सूट का छज्जा नीली रोशनी को रोकता है।",
            "क्योंकि अंतरिक्ष में सूर्य के प्रकाश को सभी दिशाओं में बिखेरने के लिए कोई वायुमंडल नहीं है।",
            "क्योंकि सूर्य बाहरी अंतरिक्ष में नहीं चमकता है।",
            "क्योंकि शून्य गुरुत्वाकर्षण में अंतरिक्ष यात्री रंग-अंधे (colour-blind) हो जाते हैं।"
        ],
        "options_gu": [
            "કારણ કે સ્પેસ સૂટનો કાચ વાદળી પ્રકાશને રોકે છે.",
            "કારણ કે અવકાશમાં સૂર્યપ્રકાશને બધી દિશામાં વિખેરવા માટે કોઈ વાતાવરણ નથી.",
            "કારણ કે સૂર્ય બાહ્ય અવકાશમાં ચમકતો નથી.",
            "કારણ કે શૂન્ય ગુરુત્વાકર્ષણમાં અવકાશયાત્રીઓ કલર-બ્લાઈન્ડ થઈ જાય છે."
        ],
        "correct_index": 1,
        "explanation": "The sky on Earth is blue because our atmosphere scatters blue sunlight into our eyes. In space, there is a vacuum (no atmosphere and no fine particles). Without particles to scatter light, the sky remains completely dark.",
        "explanation_hi": "पृथ्वी पर आकाश नीला है क्योंकि हमारा वायुमंडल हमारी आंखों में नीले सूरज की रोशनी बिखेरता है। अंतरिक्ष में एक निर्वात (vacuum) है (कोई वायुमंडल और कोई महीन कण नहीं)। प्रकाश को बिखेरने वाले कणों के बिना, आकाश पूरी तरह से काला रहता है।",
        "explanation_gu": "પૃથ્વી પર આકાશ વાદળી છે કારણ કે આપણું વાતાવરણ આપણી આંખોમાં વાદળી સૂર્યપ્રકાશ વિખેરે છે. અવકાશમાં શૂન્યાવકાશ છે (કોઈ વાતાવરણ અને કોઈ બારીક કણો નથી). પ્રકાશને વિખેરવા માટે કણો ન હોવાથી, આકાશ સંપૂર્ણપણે કાળું રહે છે."
    }
]

data = {
    "metadata": {
        "id": "ncert_class10_science_ch10",
        "title": "Chapter 10: The Human Eye and the Colourful World",
        "subject": "Science",
        "grade": "10"
    },
    "blocks": blocks
}

output_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch10.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {len(blocks)} blocks to {output_path}")
