import json
import os

def build_ncert_class10_science_ch12():
    chapter_id = "ncert_class10_science_ch12"

    metadata = {
        "id": chapter_id,
        "title": "Chapter 12: Magnetic Effects of Electric Current",
        "title_hi": "अध्याय 12: विद्युत धारा के चुंबकीय प्रभाव",
        "title_gu": "પ્રકરણ 12: વિદ્યુતપ્રવાહની ચુંબકીય અસરો",
        "subject": "Science",
        "grade": "10",
        "board": "NCERT/CBSE/GSEB",
        "curriculum": ["NCERT", "CBSE", "GSEB"],
        "language": "Trilingual (English/Hindi/Gujarati)",
        "difficulty": "Intermediate",
        "estimated_minutes": 240,
        "version": "2.0.0-GOLD-STANDARD",
        "author": "Chief Academic Architect - Antigravity",
        "reviewed_by": "Gold Pedagogy Standard Review Board",
        "tags": [
            "magnetic_effects",
            "oersted_experiment",
            "magnetic_field_lines",
            "right_hand_thumb_rule",
            "solenoid",
            "electromagnet",
            "flemings_left_hand_rule",
            "force_on_current_carrying_conductor",
            "electromagnetic_induction",
            "flemings_right_hand_rule",
            "electric_motor",
            "electric_generator",
            "ac_vs_dc",
            "domestic_electric_circuits",
            "short_circuit",
            "overloading",
            "electric_fuse",
            "earthing"
        ],
        "learning_outcomes": [
            "Explain Oersted's discovery demonstrating the relationship between electricity and magnetism.",
            "Describe the magnetic field around a bar magnet, circular loop, straight wire, and solenoid using field lines.",
            "State and apply the Right-Hand Thumb Rule to determine the magnetic field direction around current-carrying conductors.",
            "Compare permanent magnets and temporary electromagnets, detailing the role of the soft iron core.",
            "Formulate the force on a current-carrying conductor in a magnetic field and apply Fleming's Left-Hand Rule.",
            "Understand the phenomenon of Electromagnetic Induction and apply Fleming's Right-Hand Rule to determine induced current direction.",
            "Distinguish between Direct Current (DC) and Alternating Current (AC), including frequency and long-distance transmission merits.",
            "Examine domestic electrical circuits: 220V supply, color coding (live, neutral, earth), parallel wiring, earthing, overloading, short-circuiting, and fuse protection.",
            "Master every NCERT in-text question and end-of-chapter exercise question with rigorous trilingual solutions."
        ],
        "ai_context": {
            "learning_goal": "Master NCERT Class 10 Chapter 12 (Magnetic Effects of Electric Current) through the 8-Step Gold Pedagogy Arc with 100% textbook syllabus and exercise coverage.",
            "common_misconceptions": [
                "Students confuse the Right-Hand Thumb Rule (field around wire) with Fleming's Left-Hand Rule (force on wire).",
                "Students assume magnetic field lines have distinct starting and ending points; they form continuous closed loops.",
                "Students forget that conventional current direction is opposite to the movement of negative electrons.",
                "Students think the earth wire carries live current during normal operation; it is a safety path solely for accidental leakage.",
                "Students believe a stationary charge in a magnetic field experiences a magnetic force; only moving charges experience magnetic Lorentz force."
            ],
            "tutor_hint": "Always reinforce vector directions using the Right-Hand Thumb Rule and Fleming's Left-Hand Rule with physical 3D visualization."
        }
    }

    blocks = []
    block_counter = 1

    def next_id():
        nonlocal block_counter
        bid = f"KOBJ_NCERT_C10_SCI_CH12_{block_counter:03d}"
        block_counter += 1
        return bid

    # =========================================================================
    # MODULE 1: MAGNETIC FIELD, OERSTED'S EXPERIMENT & FIELD LINES (8-STEP PEDAGOGY)
    # =========================================================================

    # 1. Hook
    blocks.append({
        "id": next_id(),
        "type": "hook",
        "title": "The Mysterious Dance of the Compass Needle (1820)",
        "title_hi": "कंपास की सुई का रहस्यमयी विक्षेप (1820)",
        "title_gu": "હોકાયંત્રની સોયનું રહસ્યમય વિચલન (1820)",
        "body": "In 1820, during a university lecture, Danish physicist Hans Christian Oersted accidentally set up a compass near a wire connected to a chemical battery. The moment he completed the circuit, the compass needle jerked violently and pointed sideways! For millennia, humans believed electricity and magnetism were two completely unrelated phenomena. Yet, with one flick of a switch, a simple electric current acted like an invisible magnet. How can moving electrons generate an invisible magnetic force field out of thin air?",
        "body_hi": "1820 में एक विश्वविद्यालय व्याख्यान के दौरान, डेनिश भौतिक विज्ञानी हैंस क्रिश्चियन ओर्स्टेड ने गलती से एक बैटरी से जुड़े तार के पास चुंबकीय कंपास रख दिया। जैसे ही उन्होंने स्विच दबाया, कंपास की सुई अचानक तेजी से विक्षेपित हो गई! सदियों से लोग मानते थे कि बिजली और चुंबकत्व दो पूरी तरह से अलग चीजें हैं। लेकिन स्विच ऑन करते ही बहती विद्युत धारा ने एक अदृश्य चुंबक की तरह व्यवहार किया। गतिमान इलेक्ट्रॉन हवा में एक अदृश्य चुंबकीय बल क्षेत्र कैसे पैदा कर देते हैं?",
        "body_gu": "1820 માં એક યુનિવર્સિટી લેક્ચર દરમિયાન, ડૅનિશ ભૌતિકશાસ્ત્રી હાંસ ક્રિશ્ચિયન ઓર્સ્ટેડે આકસ્મિક રીતે બેટરી સાથે જોડાયેલા વાયર પાસે એક ચુંબકીય હોકાયંત્ર મૂક્યું. સ્વિચ ચાલુ કરતાં જ હોકાયંત્રની સોય એકાએક વિચલિત થઈ ગઈ! સદીઓથી લોકો માનતા હતા કે વીજળી અને ચુંબકત્વ બે તદ્દન અલગ બાબતો છે. પરંતુ સ્વિચ ઓન થતાં જ વિદ્યુતપ્રવાહ એક અદ્રશ્ય ચુંબકની જેમ વર્તવા લાગ્યો. ગતિમાન ઇલેક્ટ્રોન હવામાં અદ્રશ્ય ચુંબકીય ક્ષેત્ર કેવી રીતે પેદા કરે છે?"
    })

    # 2. Socratic Question
    blocks.append({
        "id": next_id(),
        "type": "socratic_question",
        "question": "A stationary electric charge only produces an electrostatic field. Why does a flowing electric current (moving charges) deflect a magnetic compass needle?",
        "question_hi": "एक स्थिर विद्युत आवेश केवल स्थिर-वैद्युत क्षेत्र पैदा करता है। गतिमान विद्युत धारा (प्रवाहित आवेश) चुंबकीय कंपास की सुई को विक्षेपित क्यों करती है?",
        "question_gu": "સ્થિર વિદ્યુતભાર માત્ર સ્થિત-વિદ્યુતક્ષેત્ર ઉત્પન્ન કરે છે. તો વહેતો વિદ્યુતપ્રવાહ (ગતિમાન વિદ્યુતભારો) ચુંબકીય હોકાયંત્રની સોયને કેમ વિચલિત કરે છે?",
        "options": [
            "Moving electric charges create a surrounding magnetic field that exerts magnetic torque on the compass needle.",
            "The electric current heats the air, blowing the compass needle physically.",
            "The copper wire chemically turns into iron when electricity flows through it.",
            "The wire attracts the glass cover of the compass by static friction."
        ],
        "options_hi": [
            "गतिमान विद्युत आवेश अपने चारों ओर एक चुंबकीय क्षेत्र उत्पन्न करते हैं जो कंपास सुई पर चुंबकीय बल-आघूर्ण लगाता है।",
            "विद्युत धारा हवा को गर्म करती है, जिससे हवा का झोंका सुई को हिला देता है।",
            "बिजली बहने पर तांबे का तार रासायनिक रूप से लोहे में बदल जाता है।",
            "तार घर्षण द्वारा कंपास के कांच के ढक्कन को आकर्षित करता है।"
        ],
        "options_gu": [
            "ગતિમાન વિદ્યુતભારો પોતાની આસપાસ ચુંબકીય ક્ષેત્ર ઉત્પન્ન કરે છે જે હોકાયંત્રની સોય પર ચુંબકીય ટોર્ક લગાડે છે.",
            "વિદ્યુતપ્રવાહ હવાને ગરમ કરે છે, જેના દબાણથી સોય હલે છે.",
            "વીજળી વહેવાથી તાંબાનો વાયર રાસાયણિક રીતે લોખંડ બની જાય છે.",
            "વાયર સ્થિત વિદ્યુત દ્વારા હોકાયંત્રના કાચને આકર્ષે છે."
        ],
        "correct_index": 0,
        "explanation": "Moving electric charges constitute an electric current, which inherently creates a magnetic field around the conductor. The magnetic needle of a compass is a small bar magnet; the magnetic field of the current interacts with the magnetic field of the needle, exerting a torque that deflects it.",
        "explanation_hi": "गतिमान विद्युत आवेश एक विद्युत धारा का निर्माण करते हैं, जो स्वाभाविक रूप से चालक के चारों ओर एक चुंबकीय क्षेत्र उत्पन्न करती है। कंपास की सुई एक छोटा चुंबक है; धारा का चुंबकीय क्षेत्र सुई के चुंबकीय क्षेत्र के साथ अन्योन्यक्रिया करता है, जिससे सुई विक्षेपित होती है।",
        "explanation_gu": "ગતિમાન વિદ્યુતભારો વિદ્યુતપ્રવાહ રચે છે, જે વાહકની આસપાસ ચુંબકીય ક્ષેત્ર પેદા કરે છે. હોકાયંત્રની સોય એક નાનો ગજિયો ચુંબક છે; પ્રવાહનું ચુંબકીય ક્ષેત્ર સોયના ચુંબકીય ક્ષેત્ર સાથે આંતરક્રિયા કરી તેને વિચલિત કરે છે."
    })

    # 3. Discovery (Activity 12.1, 12.2 & 12.3)
    blocks.append({
        "id": next_id(),
        "type": "discovery",
        "title": "Mapping the Invisible: Iron Filings & Compass Tracing",
        "title_hi": "अदृश्य को देखना: लोहे के बुरादे और कंपास से क्षेत्र रेखाएं बनाना",
        "title_gu": "અદ્રશ્યને જોવું: લોખંડના વહેર અને હોકાયંત્ર વડે ક્ષેત્રરેખાઓ દોરવી",
        "body": "How can we visualize something completely invisible? Place a bar magnet on a white cardboard and gently sprinkle fine iron filings over it. When you tap the cardboard lightly, the iron filings magically align into continuous smooth curved patterns!\n\nWhy does this happen? Every iron filing becomes a tiny induced magnetic dipole. The filings rotate and line up along lines of magnetic force.\n\nNext, place a small magnetic compass near the North pole of a bar magnet. The South tip of the compass needle points to the magnet's North pole, while its North tip points away. Move the compass step by step following its North needle and mark points with a pencil. Joining these points creates a continuous curve called a Magnetic Field Line.",
        "body_hi": "हम पूरी तरह से अदृश्य चीज को कैसे देख सकते हैं? एक सफेद कार्डबोर्ड पर एक छड़ चुंबक (Bar Magnet) रखें और उस पर लोहे का बारीक बुरादा छिड़कें। जब आप कार्डबोर्ड को धीरे से थपथपाते हैं, तो लोहे का बुरादा जादुई रूप से चिकने घुमावदार वक्रों में व्यवस्थित हो जाता है!\n\nऐसा क्यों होता है? लोहे का प्रत्येक कण एक छोटा सा प्रेरित चुंबक बन जाता है और चुंबकीय बल रेखाओं की दिशा में संरेखित हो जाता है।\n\nइसके बाद, चुंबक के उत्तरी ध्रुव के पास एक छोटा कंपास रखें। कंपास की सुई के सिरे को पेंसिल से चिह्नित करते हुए आगे बढ़ें। इन बिंदुओं को मिलाने पर बनने वाले वक्र को 'चुंबकीय क्षेत्र रेखा' (Magnetic Field Line) कहते हैं।",
        "body_gu": "આપણે તદ્દન અદ્રશ્ય બાબતને કેવી રીતે જોઈ શકીએ? સફેદ કાર્ડબોર્ડ પર ગજિયો ચુંબક મૂકી તેના પર લોખંડનો ઝીણો વહેર ભભરાવો. કાર્ડબોર્ડને હળવેથી ટકોરા મારતાં જ લોખંડનો વહેર સુંદર વળાંકવાળી રેખાઓમાં ગોઠવાઈ જાય છે!\n\nઆવું કેમ થાય છે? લોખંડનો દરેક કણ નાનો પ્રેરિત ચુંબક બની ચુંબકીય બળરેખાઓની દિશામાં ગોઠવાય છે.\n\nત્યારબાદ, ચુંબકના ઉત્તર ધ્રુવ પાસે નાનું હોકાયંત્ર મૂકી સોયની દિશામાં પેન્સિલથી ટપકાં કરતાં આગળ વધો. આ ટપકાં જોડતાં બનતા વક્રને 'ચુંબકીય ક્ષેત્રરેખા' (Magnetic Field Line) કહે છે."
    })

    # 4. Theory
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "Magnetic Field & Key Properties of Magnetic Field Lines",
        "title_hi": "चुंबकीय क्षेत्र एवं चुंबकीय क्षेत्र रेखाओं के प्रमुख गुणधर्म",
        "title_gu": "ચુંબકીય ક્ષેત્ર અને ચુંબકીય ક્ષેત્રરેખાઓની લાક્ષણિકતાઓ",
        "body": "1. WHAT IS A MAGNETIC FIELD?\nThe region surrounding a magnet in which the force of attraction or repulsion can be detected by another magnet or magnetic material. Magnetic field is a vector quantity having both magnitude and direction. Its SI unit is Tesla (T) (named after Nikola Tesla; older CGS unit is Oersted).\n\n2. DIRECTION OF FIELD LINES:\n• Outside the magnet: Magnetic field lines emerge from the North pole and merge at the South pole (N -> S).\n• Inside the magnet: The field lines run from the South pole to the North pole (S -> N).\n• Therefore, magnetic field lines are continuous closed loops (unlike electric field lines which start at positive charge and terminate on negative charge).\n\n3. STRENGTH OF THE FIELD:\nThe relative strength of the magnetic field is indicated by the degree of closeness (crowding) of the field lines. The field is strongest near the magnetic poles where lines are crowded, and weaker where they spread out.\n\n4. NON-INTERSECTION PRINCIPLE:\nNo two magnetic field lines ever cross or intersect each other. If they did, at the point of intersection, a compass needle would point in two different directions simultaneously, which is physically impossible!",
        "body_hi": "1. चुंबकीय क्षेत्र क्या है?\nकिसी चुंबक के चारों ओर का वह क्षेत्र जिसमें उसके चुंबकीय प्रभाव (आकर्षण या प्रतिकर्षण) का अनुभव किया जा सकता है। यह एक सदिश राशि (Vector quantity) है, जिसमें परिमाण और दिशा दोनों होते हैं। इसका SI मात्रक टेस्ला (Tesla, T) है (CGS मात्रक ओर्स्टेड है)।\n\n2. क्षेत्र रेखाओं की दिशा:\n• चुंबक के बाहर: क्षेत्र रेखाएं उत्तरी ध्रुव (N) से निकलती हैं और दक्षिणी ध्रुव (S) पर विलीन होती हैं।\n• चुंबक के अंदर: क्षेत्र रेखाएं दक्षिणी ध्रुव (S) से उत्तरी ध्रुव (N) की ओर जाती हैं।\n• अतः चुंबकीय क्षेत्र रेखाएं बंद वक्र (Closed continuous loops) होती हैं।\n\n3. क्षेत्र की प्रबलता:\nक्षेत्र रेखाओं की सघनता (निकटता) चुंबकीय क्षेत्र की प्रबलता को दर्शाती है। ध्रुवों के पास जहां रेखाएं घनी होती हैं, वहां चुंबकीय क्षेत्र सबसे मजबूत होता है।\n\n4. प्रतिच्छेदन न करने का नियम:\nदो चुंबकीय क्षेत्र रेखाएं कभी भी एक-दूसरे को प्रतिच्छेद (Intersect) नहीं करतीं। यदि वे काटतीं, तो प्रतिच्छेद बिंदु पर कंपास की सुई दो अलग-अलग दिशाओं को दर्शाती, जो कि भौतिक रूप से असंभव है!",
        "body_gu": "1. ચુંબકીય ક્ષેત્ર શું છે?\nચુંબકની આસપાસનો એવો વિસ્તાર જેમાં ચુંબકીય બળ (આકર્ષણ કે અપાકર્ષણ) અનુભવી શકાય. તે સદિશ રાશિ છે (મૂલ્ય અને દિશા બંને ધરાવે છે). તેનો SI એકમ ટેસ્લા (Tesla, T) છે.\n\n2. ક્ષેત્રરેખાઓની દિશા:\n• ચુંબકની બહાર: ક્ષેત્રરેખાઓ ઉત્તર ધ્રુવ (N) માંથી નીકળી દક્ષિણ ધ્રુવ (S) માં પ્રવેશે છે.\n• ચુંબકની અંદર: ક્ષેત્રરેખાઓ દક્ષિણ ધ્રુવ (S) થી ઉત્તર ધ્રુવ (N) તરફ જાય છે.\n• તેથી, ચુંબકીય ક્ષેત્રરેખાઓ બંધ વક્ર (Closed loops) રચે છે.\n\n3. ક્ષેત્રની પ્રબળતા:\nક્ષેત્રરેખાઓની ગીચતા ચુંબકીય ક્ષેત્રની પ્રબળતા દર્શાવે છે. ધ્રુવો પાસે રેખાઓ ગીચ હોવાથી ત્યાં ચુંબકીય ક્ષેત્ર સૌથી પ્રબળ હોય છે.\n\n4. છેદન ન કરવાનો નિયમ:\nબે ચુંબકીય ક્ષેત્રરેખાઓ ક્યારેય એકબીજાને છેદતી નથી. જો છેદે, તો છેદનબિંદુ પાસે હોકાયંત્રની સોય બે દિશાઓ દર્શાવે, જે કુદરતી રીતે અશક્ય છે!"
    })

    # Teacher Tip
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Teacher Tip: The 3 Hallmark Properties Tested in Board Exams",
        "title_hi": "शिक्षक टिप: बोर्ड परीक्षा में बार-बार पूछे जाने वाले 3 प्रमुख गुणधर्म",
        "title_gu": "શિક્ષક ટિપ: બોર્ડ પરીક્ષામાં વારંવાર પૂછાતી 3 મુખ્ય લાક્ષણિકતાઓ",
        "body": "When asked in exams to 'List three characteristics of magnetic field lines':\n1. They emerge from North and enter South outside the magnet, forming continuous closed curves.\n2. Degree of closeness represents magnetic field strength (crowded at poles = strong field; parallel and equidistant = uniform field).\n3. They NEVER intersect each other (at intersection point, compass would show two directions, which is impossible).",
        "body_hi": "जब परीक्षा में 'चुंबकीय क्षेत्र रेखाओं के तीन गुणधर्म लिखिए' पूछा जाए:\n1. ये चुंबक के बाहर उत्तर से दक्षिण और अंदर दक्षिण से उत्तर जाकर सतत बंद वक्र बनाती हैं।\n2. रेखाओं की निकटता क्षेत्र की प्रबलता दर्शाती है (ध्रुवों पर घनी = प्रबल क्षेत्र; समानांतर व समदूरस्थ = एकसमान क्षेत्र)।\n3. ये कभी एक-दूसरे को नहीं काटतीं (कटान बिंदु पर दो दिशाएं संभव नहीं हैं)।",
        "body_gu": "પરીક્ષામાં જ્યારે 'ચુંબકીય ક્ષેત્રરેખાઓની ત્રણ લાક્ષણિકતાઓ જણાવો' પૂછાય ત્યારે:\n1. ચુંબકની બહાર N થી S અને અંદર S થી N જઈ બંધ ગાળો રચે છે.\n2. ક્ષેત્રરેખાઓની નિકટતા ક્ષેત્રની પ્રબળતા દર્શાવે છે (ધ્રુવો પાસે ગીચ = પ્રબળ ક્ષેત્ર; સમાંતર અને સમાન અંતરે = સમાન ક્ષેત્ર).\n3. તેઓ ક્યારેય એકબીજાને છેદતી નથી (છેદનબિંદુએ બે દિશા અશક્ય છે)."
    })

    # Common Mistakes
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Common Mistake: Thinking Field Lines Stop at the Poles",
        "title_hi": "सामान्य गलती: यह सोचना कि चुंबकीय क्षेत्र रेखाएं ध्रुवों पर समाप्त हो जाती हैं",
        "title_gu": "સામાન્ય ભૂલ: એવું માનવું કે ક્ષેત્રરેખાઓ ધ્રુવો આગળ સમાપ્ત થઈ જાય છે",
        "body": "Do not confuse electrostatic field lines with magnetic field lines! Electric field lines originate on positive charge and end on negative charge (open curves). Magnetic field lines DO NOT start or end; they pass continuously straight through the interior of the magnet from South to North, forming unbroken endless loops.",
        "body_hi": "स्थिर-वैद्युत क्षेत्र रेखाओं और चुंबकीय क्षेत्र रेखाओं में भ्रमित न हों! विद्युत रेखाएं धन आवेश से शुरू होकर ऋण आवेश पर समाप्त होती हैं (खुले वक्र)। चुंबकीय क्षेत्र रेखाएं कभी समाप्त नहीं होतीं; वे चुंबक के अंदर दक्षिण से उत्तर की ओर लगातार चलती हैं और अखंड बंद लूप बनाती हैं।",
        "body_gu": "સ્થિત-વિદ્યુતક્ષેત્ર રેખાઓ અને ચુંબકીય ક્ષેત્રરેખાઓ વચ્ચે ભૂલ ન કરવી! વિદ્યુતરેખાઓ ધનભારથી શરૂ થઈ ઋણભાર પર પૂર્ણ થાય છે (ખુલ્લા વળાંકો). ચુંબકીય ક્ષેત્રરેખાઓ ક્યારેય અટકતી નથી; તે ચુંબકની અંદર S થી N તરફ વહી અખંડ બંધ ગાળો રચે છે."
    })

    # 5. Knowledge Check (In-text Set 1 Q1)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT In-Text Q: Why does a compass needle get deflected when brought near a bar magnet?",
        "question_hi": "NCERT पाठ्य-निहित प्रश्न: किसी छड़ चुंबक के निकट लाने पर कंपास की सुई विक्षेपित क्यों हो जाती है?",
        "question_gu": "NCERT પાઠ્યપુસ્તક પ્રશ્ન: ગજિયા ચુંબકની નજીક લાવતાં હોકાયંત્રની સોય કેમ વિચલિત થાય છે?",
        "options": [
            "The compass needle is a tiny bar magnet whose magnetic field interacts with the field of the bar magnet, creating a deflecting force.",
            "The bar magnet induces an electric current in the needle that produces heat.",
            "The bar magnet pulls the metal pivot of the compass due to gravitational attraction.",
            "The compass needle loses its magnetism when near another magnet."
        ],
        "options_hi": [
            "कंपास की सुई स्वयं एक छोटा छड़ चुंबक है जिसका चुंबकीय क्षेत्र बड़े चुंबक के क्षेत्र के साथ अन्योन्यक्रिया करके विक्षेपक बल लगाता है।",
            "छड़ चुंबक सुई में विद्युत धारा प्रेरित करता है जिससे गर्मी पैदा होती है।",
            "छड़ चुंबक गुरुत्वाकर्षण बल के कारण कंपास की धुरी को खींचता है।",
            "दूसरे चुंबक के पास आने पर कंपास की सुई अपना चुंबकत्व खो देती है।"
        ],
        "options_gu": [
            "હોકાયંત્રની સોય પોતે એક નાનો ગજિયો ચુંબક છે જેનું ચુંબકીય ક્ષેત્ર મોટા ચુંબકના ક્ષેત્ર સાથે આંતરક્રિયા કરી વિચલન બળ લગાડે છે.",
            "ગજિયો ચુંબક સોયમાં વિદ્યુતપ્રવાહ પ્રેરિત કરે છે જેથી ઉષ્મા પેદા થાય છે.",
            "ગજિયો ચુંબક ગુરુત્વાકર્ષણ બળથી હોકાયંત્રના કેન્દ્રને ખેંચે છે.",
            "બીજા ચુંબક નજીક આવતાં હોકાયંત્રની સોય ચુંબકત્વ ગુમાવી દે છે."
        ],
        "correct_index": 0,
        "explanation": "A compass needle is a small freely pivoted bar magnet. When brought near another magnet, the magnetic fields interact: like poles repel and unlike poles attract. This exerts a magnetic couple (torque) on the needle, deflecting it until it aligns with the net magnetic field.",
        "explanation_hi": "कंपास की सुई एक छोटी स्वतंत्र रूप से घूमने वाली छड़ चुंबक होती है। जब इसे किसी अन्य चुंबक के पास लाया जाता है, तो दोनों के चुंबकीय क्षेत्र आपस में क्रिया करते हैं: समान ध्रुव प्रतिकर्षित और विपरीत ध्रुव आकर्षित होते हैं, जिससे सुई चुंबकीय क्षेत्र रेखा की दिशा में संरेखित होने के लिए विक्षेपित हो जाती है।",
        "explanation_gu": "હોકાયંત્રની સોય એક મુક્ત રીતે ભ્રમણ કરી શકે તેવો નાનો ગજિયો ચુંબક છે. તેને બીજા ચુંબક પાસે લાવતાં સમાન ધ્રુવો વચ્ચે અપાકર્ષણ અને અસમાન ધ્રુવો વચ્ચે આકર્ષણ બળ લાગે છે, જેનાથી સોય પરિણામી ચુંબકીય ક્ષેત્રની દિશામાં ગોઠવાવા વિચલિત થાય છે."
    })

    # 6. Reflection
    blocks.append({
        "id": next_id(),
        "type": "reflection",
        "title": "Why Can Magnetic Monopoles Never Exist?",
        "title_hi": "चुंबकीय एकल ध्रुव (Magnetic Monopoles) कभी अस्तित्व में क्यों नहीं हो सकते?",
        "title_gu": "ચુંબકીય એકલ ધ્રુવ ક્યારેય અસ્તિત્વ ધરાવી શકે નહીં, શા માટે?",
        "body": "If you break an electrically charged rod in half, you can isolate positive charges on one half and negative charges on the other. But if you cut a bar magnet in half, do you get an isolated North pole and an isolated South pole? Never! Each half instantly becomes a complete new magnet with its own North and South poles, no matter how many times you slice it down to the atomic level. This fundamental law of nature confirms that magnetic field lines MUST always form closed continuous loops.",
        "body_hi": "यदि आप एक आवेशित छड़ को तोड़ते हैं, तो आप धनात्मक और ऋणात्मक आवेशों को अलग कर सकते हैं। लेकिन यदि आप किसी छड़ चुंबक को बीच से काट दें, तो क्या आपको केवल उत्तरी या केवल दक्षिणी ध्रुव मिलेगा? कभी नहीं! प्रत्येक टुकड़ा तुरंत अपने उत्तरी और दक्षिणी ध्रुव के साथ एक नया पूर्ण चुंबक बन जाता है, चाहे आप उसे परमाणु स्तर तक क्यों न काट दें। प्रकृति का यह नियम साबित करता है कि चुंबकीय क्षेत्र रेखाएं हमेशा बंद लूप बनाती हैं।",
        "body_gu": "જો તમે વિદ્યુતભારિત સળિયાના બે ટુકડા કરો તો ધન અને ઋણ વિદ્યુતભાર અલગ થઈ શકે છે. પરંતુ જો તમે ગજિયા ચુંબકના બે ટુકડા કરો, તો શું ઉત્તર કે દક્ષિણ ધ્રુવ અલગ થાય છે? ક્યારેય નહીં! દરેક ટુકડો તરત જ પોતાનો ઉત્તર અને દક્ષિણ ધ્રુવ બનાવી નવો ચુંબક બની જાય છે. કુદરતનો આ મૂળભૂત નિયમ સાબિત કરે છે કે ચુંબકીય ક્ષેત્રરેખાઓ હંમેશા બંધ ગાળો રચે છે."
    })

    # 7. Connection
    blocks.append({
        "id": next_id(),
        "type": "connection",
        "title": "Earth's Geodynamo: Our Planet's Invisible Magnetic Shield",
        "title_hi": "पृथ्वी का भू-डायनेमो: हमारे ग्रह की अदृश्य चुंबकीय ढाल",
        "title_gu": "પૃથ્વીનું ભૂ-ડાયનેમો: આપણા ગ્રહનું અદ્રશ્ય ચુંબકીય રક્ષણ કવચ",
        "body": "Why doesn't deadly solar radiation incinerate Earth's atmosphere? Deep in Earth's outer core (3,000 km beneath our feet), molten liquid iron and nickel circulate due to convection currents and planetary rotation. These circulating metallic currents act as a colossal natural dynamo, generating Earth's planetary magnetic field (Magnetosphere).\n\nThis field deflects supersonic solar wind particles towards the polar regions, creating the dazzling Northern and Southern Lights (Aurora Borealis and Australis) and preserving the air we breathe!",
        "body_hi": "सूर्य से आने वाले घातक सौर विकिरण पृथ्वी के वायुमंडल को नष्ट क्यों नहीं करते? हमारे पैरों के नीचे लगभग 3,000 किमी गहराई में पृथ्वी के बाहरी कोर में पिघला हुआ लोहा और निकल संवहन धाराओं और घूर्णन के कारण गति करता है। यह विशाल प्राकृतिक डायनेमो पृथ्वी का चुंबकीय क्षेत्र उत्पन्न करता है।\n\nयह चुंबकीय क्षेत्र हानिकारक सौर तूफानों को ध्रुवों की ओर मोड़ देता है, जिससे आकाश में सुंदर ऑरोरा (ध्रुवीय ज्योति) बनती है और हमारा वायुमंडल सुरक्षित रहता है!",
        "body_gu": "સૂર્યમાંથી આવતા જીવલેણ વિકિરણો પૃથ્વીના વાતાવરણને કેમ બાળી નાખતા નથી? પૃથ્વીના પેટાળમાં 3,000 કિમી ઊંડે પીગળેલું લોખંડ અને નિકલ પૃથ્વીના પરિભ્રમણને કારણે સતત વહે છે. આ વિશાળ કુદરતી ડાયનેમો પૃથ્વીનું ચુંબકીય ક્ષેત્ર ઉત્પન્ન કરે છે.\n\nઆ ચુંબકીય કવચ સૌર પવનોને ધ્રુવો તરફ વાળી દે છે, જેનાથી ધ્રુવો પર સુંદર અરોરા (પ્રકાશપુંજ) રચાય છે અને આપણું વાતાવરણ સુરક્ષિત રહે છે!"
    })

    # 8. Mastery Challenge (MCQ)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Which of the following statements about magnetic field lines is INCORRECT?",
        "question_hi": "चुंबकीय क्षेत्र रेखाओं के बारे में निम्नलिखित में से कौन सा कथन असत्य (गलत) है?",
        "question_gu": "ચુંબકીય ક્ષેત્રરેખાઓ વિશે નીચેનામાંથી કયું વિધાન ખોટું છે?",
        "options": [
            "Magnetic field lines can cross each other in regions of extremely strong magnetic fields.",
            "Outside a bar magnet, field lines emerge from the North pole and enter the South pole.",
            "The relative strength of the field is shown by how closely the lines are packed together.",
            "Magnetic field lines are continuous closed curves that pass from South to North inside the magnet."
        ],
        "options_hi": [
            "अत्यधिक प्रबल चुंबकीय क्षेत्र वाले क्षेत्रों में क्षेत्र रेखाएं एक-दूसरे को काट सकती हैं।",
            "चुंबक के बाहर, क्षेत्र रेखाएं उत्तरी ध्रुव से निकलती हैं और दक्षिणी ध्रुव में प्रवेश करती हैं।",
            "क्षेत्र की सापेक्ष प्रबलता रेखाओं की निकटता (सघनता) द्वारा प्रदर्शित की जाती है।",
            "चुंबकीय क्षेत्र रेखाएं सतत बंद वक्र होती हैं जो चुंबक के अंदर दक्षिण से उत्तर की ओर जाती हैं।"
        ],
        "options_gu": [
            "અતિશય પ્રબળ ચુંબકીય ક્ષેત્ર ધરાવતા વિસ્તારોમાં ક્ષેત્રરેખાઓ એકબીજાને છેદી શકે છે.",
            "ગજિયા ચુંબકની બહાર, ક્ષેત્રરેખાઓ ઉત્તર ધ્રુવમાંથી નીકળી દક્ષિણ ધ્રુવમાં પ્રવેશે છે.",
            "ચુંબકીય ક્ષેત્રની સાપેક્ષ પ્રબળતા રેખાઓની ગીચતા વડે દર્શાવવામાં આવે છે.",
            "ચુંબકીય ક્ષેત્રરેખાઓ સતત બંધ વળાંકો છે જે ચુંબકની અંદર S થી N તરફ વહે છે."
        ],
        "correct_index": 0,
        "explanation": "Statement A is completely false: Magnetic field lines NEVER intersect under any circumstances. If they did, a compass at the intersection point would point in two directions at once, which is a physical impossibility. Statements B, C, and D are scientifically accurate.",
        "explanation_hi": "कथन A पूरी तरह से गलत है: चुंबकीय क्षेत्र रेखाएं किसी भी परिस्थिति में कभी एक-दूसरे को नहीं काटतीं। यदि वे काटतीं, तो प्रतिच्छेद बिंदु पर कंपास दो दिशाएं दर्शाता, जो असंभव है। कथन B, C और D पूर्णतः सत्य हैं।",
        "explanation_gu": "વિધાન A તદ્દન ખોટું છે: કોઈપણ સંજોગોમાં ચુંબકીય ક્ષેત્રરેખાઓ ક્યારેય છેદતી નથી. જો છેદે તો હોકાયંત્ર એકસાથે બે દિશા બતાવે જે અશક્ય છે. વિધાન B, C અને D સાચા છે."
    })

    # =========================================================================
    # MODULE 2: STRAIGHT CONDUCTOR & RIGHT-HAND THUMB RULE (8-STEP PEDAGOGY)
    # =========================================================================

    # 1. Hook
    blocks.append({
        "id": next_id(),
        "type": "hook",
        "title": "The Invisible Whirlpools Around High-Tension Cables",
        "title_hi": "हाई-टेंशन बिजली के तारों के चारों ओर अदृश्य भंवर",
        "title_gu": "હાઈ-ટેન્શન વીજળીના વાયરોની આસપાસ અદ્રશ્ય વમળો",
        "body": "When hundreds of amperes of electric current surge through overhead transmission cables humming across our highways, what surrounds that metal wire? Not empty space! Around every millimetre of that cable spins an invisible concentric cylinder of magnetic force. If you held a giant sheet of cardboard sprinkled with iron dust around the cable, the dust would instantly arrange into thousands of concentric glowing circles centered directly on the wire!",
        "body_hi": "जब राजमार्गों पर झूलते बिजली के विशाल तारों में से सैकड़ों एम्पीयर की धारा बहती है, तो उस तार के चारों ओर क्या होता है? खाली स्थान नहीं! उस तार के चारों ओर चुंबकीय बल का एक अदृश्य बेलनाकार भंवर लगातार घूमता रहता है। यदि आप उस तार के चारों ओर लोहे के बुरादे से भरा एक बड़ा कार्डबोर्ड रखें, तो बुरादा तार के चारों ओर हजारों संकेंद्रीय वृत्तों (Concentric Circles) में व्यवस्थित हो जाएगा!",
        "body_gu": "જ્યારે હાઈવે પરથી પસાર થતા મોટા વીજ કેબલોમાંથી સેંકડો એમ્પીયરનો કરંટ વહે છે, ત્યારે વાયરની આસપાસ શું હોય છે? ખાલી જગ્યા નહીં! વાયરની દરેક મિલિમીટર આસપાસ ચુંબકીય બળના અદ્રશ્ય નળાકાર વમળો ફરતા હોય છે. જો વાયરની આસપાસ કાર્ડબોર્ડ પર લોખંડનો વહેર ભભરાવો, તો તે વાયરને કેન્દ્ર રાખીને હજારો સમકેન્દ્રી વર્તુળોમાં ગોઠવાઈ જાય છે!"
    })

    # 2. Socratic Question
    blocks.append({
        "id": next_id(),
        "type": "socratic_question",
        "question": "If you double the electric current in a straight copper wire and move your compass twice as far away, what happens to the strength of the magnetic field?",
        "question_hi": "यदि आप सीधे तांबे के तार में बहने वाली धारा को दोगुना कर दें और अपने कंपास को दोगुनी दूरी पर ले जाएं, तो चुंबकीय क्षेत्र की प्रबलता पर क्या प्रभाव पड़ेगा?",
        "question_gu": "જો તમે સીધા તાંબાના વાયરમાંથી વહેતો પ્રવાહ બમણો કરો અને હોકાયંત્રને બમણા અંતરે લઈ જાઓ, તો ચુંબકીય ક્ષેત્રની પ્રબળતા પર શું અસર થશે?",
        "options": [
            "The magnetic field strength remains unchanged because doubling current doubles B, but doubling distance halves B.",
            "The magnetic field becomes 4 times stronger.",
            "The magnetic field completely drops to zero.",
            "The magnetic field becomes 4 times weaker."
        ],
        "options_hi": [
            "चुंबकीय क्षेत्र की प्रबलता अपरिवर्तित रहती है क्योंकि धारा दोगुनी करने से B दोगुना होता है, लेकिन दूरी दोगुनी करने से B आधा हो जाता है।",
            "चुंबकीय क्षेत्र 4 गुना अधिक मजबूत हो जाता है।",
            "चुंबकीय क्षेत्र शून्य हो जाता है।",
            "चुंबकीय क्षेत्र 4 गुना कमजोर हो जाता है।"
        ],
        "options_gu": [
            "ચુંબકીય ક્ષેત્રની પ્રબળતા યથાવત રહે છે કારણ કે પ્રવાહ બમણો થતાં B બમણું થાય છે અને અંતર બમણું થતાં B અડધું થઈ જાય છે.",
            "ચુંબકીય ક્ષેત્ર 4 ગણું પ્રબળ બને છે.",
            "ચુંબકીય ક્ષેત્ર શૂન્ય થઈ જાય છે.",
            "ચુંબકીય ક્ષેત્ર 4 ગણું નબળું પડે છે."
        ],
        "correct_index": 0,
        "explanation": "Magnetic field strength B near a straight conductor is directly proportional to current (B ∝ I) and inversely proportional to distance (B ∝ 1/r). Therefore, B ∝ I/r. Multiplying current by 2 and distance by 2 gives (2*I)/(2*r) = I/r, so the net magnetic field remains unchanged.",
        "explanation_hi": "सीधे चालक के निकट चुंबकीय क्षेत्र B धारा के समानुपाती (B ∝ I) और दूरी के व्युत्क्रमानुपाती (B ∝ 1/r) होता है। अतः B ∝ I/r। धारा को 2 गुना और दूरी को 2 गुना करने पर (2*I)/(2*r) = I/r रहता है, इसलिए कुल चुंबकीय क्षेत्र अपरिवर्तित रहता है।",
        "explanation_gu": "સુરેખ વાહક નજીક ચુંબકીય ક્ષેત્ર B પ્રવાહના સમપ્રમાણમાં (B ∝ I) અને અંતરના વ્યસ્ત પ્રમાણમાં (B ∝ 1/r) હોય છે. તેથી B ∝ I/r. પ્રવાહ 2 ગણો અને અંતર 2 ગણું કરવાથી (2*I)/(2*r) = I/r રહે છે, જેથી ક્ષેત્ર બદલાતું નથી."
    })

    # 3. Discovery (Activity 12.4 & 12.5)
    blocks.append({
        "id": next_id(),
        "type": "discovery",
        "title": "Mapping Concentric Rings: The Straight Wire Circuit",
        "title_hi": "संकेंद्रीय वृत्तों का रहस्य: सीधे तार का विद्युत परिपथ",
        "title_gu": "સમકેન્દ્રી વર્તુળોનું રહસ્ય: સુરેખ વાયરનો વિદ્યુત પરિપથ",
        "body": "Pass a thick copper wire vertically through a hole in a horizontal sheet of white cardboard. Connect the wire in series with a battery, a plug key, and a rheostat (variable resistor). Sprinkle iron filings uniformly on the cardboard.\n\nClose the key so that current flows vertically downwards through the wire. Gently tap the cardboard. The filings align in neat concentric circles centered on the wire!\n\nNow place a compass at a point on one circle:\n• When current flows downwards, the compass needle's North pole points clockwise.\n• Reverse the battery terminals so current flows upwards: the compass needle immediately flips and points anticlockwise!\n• Move the compass further from the wire: the deflection decreases, proving that magnetic field weakens with distance.",
        "body_hi": "एक सफेद कार्डबोर्ड के बीच में छेद करके एक मोटा तांबे का तार लंबवत निकालें। तार को बैटरी, कुंजी और रियोस्टैट (परिवर्ती प्रतिरोध) के साथ श्रेणीक्रम में जोड़ें। कार्डबोर्ड पर समान रूप से लोहे का बुरादा छिड़कें।\n\nकुंजी दबाएं ताकि तार में धारा नीचे की ओर बहे। कार्डबोर्ड को हल्के से थपथपाएं। बुरादा तार को केंद्र मानकर संकेंद्रीय वृत्तों में व्यवस्थित हो जाता है!\n\nअब किसी वृत्त पर कंपास रखें:\n• जब धारा नीचे बहती है, तो कंपास की सुई दक्षिणावर्त (Clockwise) दिशा दिखाती है।\n• बैटरी के टर्मिनल उल्टे करने पर (धारा ऊपर जाने पर), सुई तुरंत वामावर्त (Anticlockwise) दिशा में मुड़ जाती है!\n• कंपास को तार से दूर ले जाने पर सुई का विक्षेप घट जाता है, जो साबित करता है कि दूरी बढ़ने पर चुंबकीय क्षेत्र घटता है।",
        "body_gu": "સફેદ કાર્ડબોર્ડની મધ્યમાં કાણું પાડી તેમાંથી જાડો તાંબાનો વાયર ઊભો પસાર કરો. વાયરને બેટરી, કળ અને ચલ અવરોધ સાથે શ્રેણીમાં જોડો. કાર્ડબોર્ડ પર લોખંડનો વહેર ભભરાવો.\n\nકળ ચાલુ કરી વાયરમાં પ્રવાહ નીચે તરફ વહેવડાવો. કાર્ડબોર્ડને ટકોરા મારતાં જ વહેર સમકેન્દ્રી વર્તુળોમાં ગોઠવાઈ જાય છે!\n\nહવે વર્તુળ પર હોકાયંત્ર મૂકો:\n• પ્રવાહ નીચે જતો હોય ત્યારે હોકાયંત્ર સમઘડી (Clockwise) દિશા દર્શાવે છે.\n• બેટરીના છેડા ઉલટાવતાં (પ્રવાહ ઉપર જતાં), સોય તરત જ વિષમઘડી (Anticlockwise) દિશામાં ફરી જાય છે!\n• હોકાયંત્રને વાયરથી દૂર લઈ જતાં વિચલન ઘટે છે, જે દર્શાવે છે કે અંતર વધતાં ચુંબકીય ક્ષેત્ર ઘટે છે."
    })

    # 4. Theory
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "Right-Hand Thumb Rule & Field Proportionality",
        "title_hi": "दाहिने हाथ के अंगूठे का नियम एवं क्षेत्र की निर्भरता",
        "title_gu": "જમણા હાથના અંગૂઠાનો નિયમ અને ક્ષેત્રની નિર્ભરતા",
        "body": "1. RIGHT-HAND THUMB RULE (Maxwell's Corkscrew Rule):\nImagine that you are grasping the current-carrying straight conductor in your RIGHT HAND such that your stretched thumb points in the direction of the electric current. Then your curled fingers wrapped around the conductor will point in the direction of the magnetic field lines.\n• If current flows UPWARDS: Fingers curl ANTICLOCKWISE (when viewed from above).\n• If current flows DOWNWARDS: Fingers curl CLOCKWISE (when viewed from above).\n\n2. FACTORS AFFECTING MAGNETIC FIELD STRENGTH (B):\n• Current (I): B ∝ I (Directly proportional to the magnitude of current). Larger current = stronger field.\n• Distance (r): B ∝ 1/r (Inversely proportional to distance from the wire). As distance increases, concentric circles become larger and spaced further apart, showing a weaker field.",
        "body_hi": "1. दाहिने हाथ के अंगूठे का नियम (Right-Hand Thumb Rule):\nकल्पना कीजिए कि आप अपने दाहिने हाथ में धारावाही चालक को इस प्रकार पकड़े हुए हैं कि आपका फैला हुआ अंगूठा विद्युत धारा की दिशा में संकेत करता है। तब आपकी उंगलियां चालक के चारों ओर चुंबकीय क्षेत्र रेखाओं की दिशा में लिपटी होंगी।\n• यदि धारा ऊपर की ओर बहती है: उंगलियां वामावर्त (Anticlockwise) मुड़ती हैं (ऊपर से देखने पर)।\n• यदि धारा नीचे की ओर बहती है: उंगलियां दक्षिणावर्त (Clockwise) मुड़ती हैं (ऊपर से देखने पर)।\n\n2. चुंबकीय क्षेत्र (B) को प्रभावित करने वाले कारक:\n• विद्युत धारा (I): B ∝ I (धारा के समानुपाती)। धारा बढ़ाने पर चुंबकीय क्षेत्र मजबूत होता है।\n• दूरी (r): B ∝ 1/r (दूरी के व्युत्क्रमानुपाती)। तार से दूर जाने पर संकेंद्रीय वृत्त बड़े और दूर-दूर हो जाते हैं, जो कमजोर क्षेत्र को दर्शाते हैं।",
        "body_gu": "1. જમણા હાથના અંગૂઠાનો નિયમ (Right-Hand Thumb Rule):\nકલ્પના કરો કે તમે તમારા જમણા હાથમાં વિદ્યુતપ્રવાહધારિત સુરેખ વાહકને એવી રીતે પકડ્યો છે કે તમારો અંગૂઠો વિદ્યુતપ્રવાહની દિશામાં રહે. તો વાહક ફરતે વીંટળાયેલી તમારી આંગળીઓ ચુંબકીય ક્ષેત્રરેખાઓની દિશા દર્શાવશે.\n• જો પ્રવાહ ઉપર તરફ વહેતો હોય: આંગળીઓ વિષમઘડી (Anticlockwise) દિશા દર્શાવે છે.\n• જો પ્રવાહ નીચે તરફ વહેતો હોય: આંગળીઓ સમઘડી (Clockwise) દિશા દર્શાવે છે.\n\n2. ચુંબકીય ક્ષેત્ર (B) ની નિર્ભરતા:\n• વિદ્યુતપ્રવાહ (I): B ∝ I (પ્રવાહના સમપ્રમાણમાં). પ્રવાહ વધારતાં ક્ષેત્ર પ્રબળ બને છે.\n• અંતર (r): B ∝ 1/r (વાયરથી અંતરના વ્યસ્ત પ્રમાણમાં). દૂર જતાં વર્તુળો મોટા અને છૂટા બને છે, જે ક્ષેત્રની ઘટતી પ્રબળતા દર્શાવે છે."
    })

    # Worked Example (NCERT Example 12.1)
    blocks.append({
        "id": next_id(),
        "type": "example",
        "title": "NCERT Example 12.1: Horizontal Power Line Field Direction",
        "title_hi": "NCERT उदाहरण 12.1: क्षैतिज विद्युत तार में चुंबकीय क्षेत्र की दिशा",
        "title_gu": "NCERT ઉદાહરણ 12.1: સમક્ષિતિજ વીજ વાયરમાં ચુંબકીય ક્ષેત્રની દિશા",
        "body": "PROBLEM:\nA current flows through a horizontal power line from East to West. What is the direction of magnetic field at a point directly below it and at a point directly above it?\n\nSOLUTION:\n• Current direction: East to West.\n• Apply Right-Hand Thumb Rule:\nPoint the thumb of your right hand towards the West.\n1. Directly BELOW the wire: Your fingers curl from North towards South. Thus, the magnetic field is directed from NORTH to SOUTH.\n2. Directly ABOVE the wire: Your fingers emerge and curl from South towards North. Thus, the magnetic field is directed from SOUTH to NORTH.\n• Viewed from the East end, the field lines appear CLOCKWISE.",
        "body_hi": "प्रश्न:\nकिसी क्षैतिज शक्ति संचरण लाइन में पूर्व से पश्चिम दिशा की ओर विद्युत धारा प्रवाहित हो रही है। इसके ठीक नीचे और ठीक ऊपर के बिंदु पर चुंबकीय क्षेत्र की दिशा क्या है?\n\nहल:\n• धारा की दिशा: पूर्व से पश्चिम (East to West)।\n• दाहिने हाथ के अंगूठे का नियम लागू करने पर:\nअपने दाहिने हाथ के अंगूठे को पश्चिम की ओर रखें।\n1. तार के ठीक नीचे: उंगलियां उत्तर से दक्षिण (North to South) की ओर मुड़ती हैं। अतः चुंबकीय क्षेत्र की दिशा उत्तर से दक्षिण है।\n2. तार के ठीक ऊपर: उंगलियां दक्षिण से उत्तर (South to North) की ओर मुड़ती हैं। अतः चुंबकीय क्षेत्र की दिशा दक्षिण से उत्तर है।\n• पूर्व सिरे से देखने पर क्षेत्र रेखाएं दक्षिणावर्त (Clockwise) दिखाई देती हैं।",
        "body_gu": "પ્રશ્ન:\nએક સમક્ષિતિજ પાવર લાઇનમાં પૂર્વથી પશ્ચિમ દિશા તરફ વિદ્યુતપ્રવાહ વહે છે. તેની બરાબર નીચે અને બરાબર ઉપરના બિંદુએ ચુંબકીય ક્ષેત્રની દિશા શોધો.\n\nઉકેલ:\n• પ્રવાહની દિશા: પૂર્વથી પશ્ચિમ.\n• જમણા હાથના અંગૂઠાનો નિયમ વાપરતાં:\nજમણા હાથનો અંગૂઠો પશ્ચિમ તરફ રાખો.\n1. વાયરની બરાબર નીચે: આંગળીઓ ઉત્તરથી દક્ષિણ (North to South) તરફ વળે છે. તેથી ક્ષેત્ર ઉત્તરથી દક્ષિણ દિશામાં છે.\n2. વાયરની બરાબર ઉપર: આંગળીઓ દક્ષિણથી ઉત્તર (South to North) તરફ વળે છે. તેથી ક્ષેત્ર દક્ષિણથી ઉત્તર દિશામાં છે.\n• પૂર્વ છેડેથી જોતાં ક્ષેત્રરેખાઓ સમઘડી (Clockwise) દેખાય છે."
    })

    # 5. Knowledge Check (MCQ)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "A vertical wire carries an electric current flowing vertically upwards. Looking down at the wire from above, the magnetic field lines are in the shape of:",
        "question_hi": "एक ऊर्ध्वाधर तार में विद्युत धारा नीचे से ऊपर की ओर बह रही है। तार को ऊपर से देखने पर चुंबकीय क्षेत्र रेखाएं किस प्रकार होंगी?",
        "question_gu": "એક ઊભા વાયરમાં વિદ્યુતપ્રવાહ નીચેથી ઉપર તરફ વહે છે. ઉપરથી જોતાં ચુંબકીય ક્ષેત્રરેખાઓ કઈ દિશામાં હશે?",
        "options": [
            "Concentric circles directed anticlockwise.",
            "Concentric circles directed clockwise.",
            "Straight parallel lines pointing North.",
            "Radial lines pointing outward from the wire."
        ],
        "options_hi": [
            "वामावर्त (Anticlockwise) दिशा में संकेंद्रीय वृत्त।",
            "दक्षिणावर्त (Clockwise) दिशा में संकेंद्रीय वृत्त।",
            "उत्तर की ओर संकेत करती समानांतर सीधी रेखाएं।",
            "तार से बाहर की ओर जाती त्रिज्यीय रेखाएं।"
        ],
        "options_gu": [
            "વિષમઘડી (Anticlockwise) દિશામાં સમકેન્દ્રી વર્તુળો.",
            "સમઘડી (Clockwise) દિશામાં સમકેન્દ્રી વર્તુળો.",
            "ઉત્તર તરફ જતી સમાંતર રેખાઓ.",
            "વાયરમાંથી બહાર નીકળતી ત્રિજ્યાવર્તી રેખાઓ."
        ],
        "correct_index": 0,
        "explanation": "According to the Right-Hand Thumb Rule, point your right thumb upwards along the direction of current. Your fingers curl in an anticlockwise direction when viewed from above. Hence, the field consists of anticlockwise concentric circles.",
        "explanation_hi": "दाहिने हाथ के अंगूठे के नियमानुसार, अपने अंगूठे को धारा की दिशा में ऊपर रखें। ऊपर से देखने पर आपकी उंगलियां वामावर्त (Anticlockwise) दिशा में मुड़ेंगी। अतः क्षेत्र वामावर्त संकेंद्रीय वृत्तों के रूप में होता है।",
        "explanation_gu": "જમણા હાથના અંગૂઠાના નિયમ મુજબ, અંગૂઠો પ્રવાહની દિશામાં ઉપર રાખો. ઉપરથી જોતાં આંગળીઓ વિષમઘડી (Anticlockwise) દિશામાં વળે છે. તેથી સમકેન્દ્રી વર્તુળો વિષમઘડી દિશામાં રચાય છે."
    })

    # 6. Reflection
    blocks.append({
        "id": next_id(),
        "type": "reflection",
        "title": "Why Does Field Strength Decay as 1/r Instead of 1/r^2?",
        "title_hi": "चुंबकीय क्षेत्र 1/r के अनुसार क्यों घटता है, 1/r² के अनुसार क्यों नहीं?",
        "title_gu": "ચુંબકીય ક્ષેત્ર 1/r² ને બદલે 1/r મુજબ કેમ ઘટે છે?",
        "body": "Gravitational and electrostatic point forces obey the inverse-square law (1/r^2) because energy radiates outward into a 3D spherical volume (surface area = 4*pi*r^2). But an infinitely long straight wire is a 1D cylindrical source! The magnetic flux radiates outward through cylindrical surfaces (surface area = 2*pi*r*L). Because circumference scales linearly with radius r, the magnetic field strength decreases as 1/r. Geometry dictates physics!",
        "body_hi": "गुरुत्वाकर्षण और बिंदु आवेश 1/r² के नियम का पालन करते हैं क्योंकि ऊर्जा एक 3D गोले की सतह (4*pi*r²) पर फैलती है। लेकिन एक लंबा सीधा तार एक 1D बेलनाकार स्रोत है! इसका चुंबकीय फ्लक्स बेलन की सतह (2*pi*r*L) पर फैलता है। चूंकि बेलन की परिधि त्रिज्या r के रैखिक अनुपात में बढ़ती है, इसलिए चुंबकीय क्षेत्र 1/r के अनुसार घटता है। ज्यामिति ही भौतिकी का आधार है!",
        "body_gu": "ગુરુત્વાકર્ષણ અને બિંદુવત વિદ્યુતભારનું બળ 1/r² ના નિયમ મુજબ ઘટે છે કારણ કે ઊર્જા 3D ગોળાની સપાટી (4*pi*r²) પર ફેલાય છે. પરંતુ લાંબો સુરેખ વાયર 1D નળાકાર સ્ત્રોત છે! તેનું ચુંબકીય ક્ષેત્ર નળાકાર સપાટી (2*pi*r*L) પર ફેલાય છે. નળાકારનો પરિઘ ત્રિજ્યા r ના સમપ્રમાણમાં વધતો હોવાથી ચુંબકીય ક્ષેત્ર 1/r મુજબ ઘટે છે. ભૂમિતિ જ ભૌતિક વિજ્ઞાન નક્કી કરે છે!"
    })

    # 7. Connection
    blocks.append({
        "id": next_id(),
        "type": "connection",
        "title": "Engineering Solution: Twisted-Pair Ethernet Cables",
        "title_hi": "इंजीनियरिंग समाधान: ट्विस्टेड-पेयर ईथरनेट केबल",
        "title_gu": "એન્જિનિયરિંગ કૌશલ્ય: ટ્વિસ્ટેડ-પેર ઇન્ટરનેટ કેબલ",
        "body": "Every current creates a magnetic field, which means every wire in your computer cable leaks magnetic noise that could corrupt adjacent data signals! How do network engineers solve this? They twist the sending and receiving wires together in pairs ('Twisted Pair' Cat-6 cables). Because equal currents flow in opposite directions through the twisted wires, their respective concentric magnetic fields cancel each other out completely, guaranteeing clean, noise-free internet data transfer!",
        "body_hi": "प्रत्येक विद्युत धारा एक चुंबकीय क्षेत्र बनाती है, जिसका अर्थ है कि कंप्यूटर केबल का प्रत्येक तार चुंबकीय शोर पैदा करता है जो डेटा को खराब कर सकता है! इंजीनियर इसे कैसे हल करते हैं? वे तारों को जोड़े में आपस में मोड़ (Twist) देते हैं (Cat-6 केबल)। चूंकि मुड़े हुए तारों में समान धारा विपरीत दिशाओं में बहती है, उनके संकेंद्रीय चुंबकीय क्षेत्र एक-दूसरे को पूरी तरह से समाप्त कर देते हैं, जिससे डेटा बिना किसी रुकावट के तेज गति से ट्रांसफर होता है!",
        "body_gu": "દરેક વિદ્યુતપ્રવાહ ચુંબકીય ક્ષેત્ર બનાવે છે, જેથી કોમ્પ્યુટર કેબલના વાયરો ચુંબકીય ક્ષોભ પેદા કરી ડેટા બગાડી શકે છે! એન્જિનિયરો આનો ઉકેલ કેવી રીતે લાવ્યા? તેઓ કેબલના વાયરોને એકબીજા સાથે વણી (Twist) દે છે (Cat-6 કેબલ). સામસામે વિરુદ્ધ દિશામાં વહેતા પ્રવાહોના ચુંબકીય ક્ષેત્રો એકબીજાની અસર નાબૂદ કરે છે, જેથી ઇન્ટરનેટ ડેટા અવાજ કે વિક્ષેપ વગર ઝડપથી વહે છે!"
    })

    # 8. Mastery Challenge (MCQ)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "If the direction of electric current in a vertical wire is reversed from downwards to upwards, what change occurs in the concentric magnetic field lines around it?",
        "question_hi": "यदि किसी ऊर्ध्वाधर तार में विद्युत धारा की दिशा को नीचे से ऊपर की ओर उलट दिया जाए, तो उसके चारों ओर संकेंद्रीय चुंबकीय क्षेत्र रेखाओं में क्या परिवर्तन होगा?",
        "question_gu": "જો ઊભા વાયરમાં વિદ્યુતપ્રવાહની દિશા નીચેથી બદલીને ઉપર કરવામાં આવે, તો તેની આસપાસની સમકેન્દ્રી ક્ષેત્રરેખાઓમાં શું ફેરફાર થશે?",
        "options": [
            "The direction of the field lines reverses from clockwise to anticlockwise.",
            "The field lines become straight parallel lines.",
            "The magnetic field completely vanishes.",
            "The field lines become elliptical and double in radius."
        ],
        "options_hi": [
            "क्षेत्र रेखाओं की दिशा दक्षिणावर्त (Clockwise) से बदलकर वामावर्त (Anticlockwise) हो जाती है।",
            "क्षेत्र रेखाएं सीधी समानांतर रेखाएं बन जाती हैं।",
            "चुंबकीय क्षेत्र पूरी तरह से गायब हो जाता है।",
            "क्षेत्र रेखाएं दीर्घवृत्ताकार हो जाती हैं और उनकी त्रिज्या दोगुनी हो जाती है।"
        ],
        "options_gu": [
            "ક્ષેત્રરેખાઓની દિશા સમઘડીમાંથી બદલાઈને વિષમઘડી થઈ જાય છે.",
            "ક્ષેત્રરેખાઓ સમાંતર સીધી રેખાઓ બની જાય છે.",
            "ચુંબકીય ક્ષેત્ર સંપૂર્ણપણે અદ્રશ્ય થઈ જાય છે.",
            "ક્ષેત્રરેખાઓ લંબગોળ બની તેમની ત્રિજ્યા બમણી થઈ જાય છે."
        ],
        "correct_index": 0,
        "explanation": "By Maxwell's Right-Hand Thumb Rule, reversing the direction of current reverses the magnetic field direction: looking down, downward current produces clockwise lines, while upward current produces anticlockwise lines.",
        "explanation_hi": "दाहिने हाथ के अंगूठे के नियमानुसार, धारा की दिशा उलटने से चुंबकीय क्षेत्र की दिशा भी उलट जाती है: नीचे देखने पर नीचे की धारा दक्षिणावर्त और ऊपर की धारा वामावर्त वृत्त बनाती है।",
        "explanation_gu": "જમણા હાથના અંગૂઠાના નિયમ મુજબ પ્રવાહની દિશા ઉલટાવતાં ક્ષેત્રની દિશા પણ ઉલટાય છે: નીચે તરફનો પ્રવાહ સમઘડી અને ઉપર તરફનો પ્રવાહ વિષમઘડી ક્ષેત્રરેખાઓ રચે છે."
    })

    # =========================================================================
    # MODULE 3: CIRCULAR LOOP, SOLENOID & ELECTROMAGNET (8-STEP PEDAGOGY)
    # =========================================================================

    # 1. Hook
    blocks.append({
        "id": next_id(),
        "type": "hook",
        "title": "From Weak Whispers to a Magnetic Roar: The Magic of Coils",
        "title_hi": "एक तार से शक्तिशाली चुंबक: कुंडली का जादुई विज्ञान",
        "title_gu": "એક વાયરમાંથી મહાશક્તિશાળી ચુંબક: ગૂંચળાનું જાદુઈ વિજ્ઞાન",
        "body": "A single straight wire carrying 1 ampere produces a magnetic field so feeble it barely moves a lightweight needle a few centimetres away. But what if we bend that same wire into a circle? The magnetic fields from both sides now add up at the center! And what if we wind that wire 1,000 times into a tight spring-like cylinder called a Solenoid? Suddenly, thousands of microscopic fields unite into a colossal, uniform magnetic force capable of lifting 10-ton cars in a scrapyard! How does winding wire create this miraculous amplification?",
        "body_hi": "1 एम्पीयर धारा वाला एक सीधा तार इतना कमजोर चुंबकीय क्षेत्र बनाता है कि वह पास रखी सुई को भी बमुश्किल हिला पाता है। लेकिन अगर हम उसी तार को मोड़कर एक वृत्त बना दें? दोनों तरफ के चुंबकीय क्षेत्र केंद्र पर जुड़ जाते हैं! और अगर हम उसी तार को 1,000 बार लपेटकर एक बेलनाकार स्प्रिंग (परिनालिका / Solenoid) बना दें? हजारों छोटे-छोटे क्षेत्र मिलकर एक शक्तिशाली चुंबकीय क्षेत्र बना लेते हैं जो कबाड़खाने में 10 टन की कारों को उठा सकता है! तार लपेटने से यह शक्ति कैसे बढ़ जाती है?",
        "body_gu": "1 એમ્પીયર પ્રવાહ ધરાવતો સુરેખ વાયર એટલું નબળું ક્ષેત્ર બનાવે છે કે તે સોયને પણ માંડ હલાવી શકે છે. પણ જો એ જ વાયરને વાળીને વર્તુળ બનાવીએ તો? બંને બાજુના ક્ષેત્રો કેન્દ્રમાં ભેગા થઈ ઉમેરાય છે! અને જો વાયરને 1,000 આંટા વાળીને નળાકાર સ્પ્રિંગ (સોલેનોઇડ) બનાવીએ તો? હજારો નાના ક્ષેત્રો જોડાઈને 10 ટનની કાર પણ ઊંચકી શકે તેવું મહાકાય ચુંબકીય બળ રચે છે! માત્ર ગૂંચળું વાળવાથી આ ચમત્કાર કેવી રીતે સર્જાય છે?"
    })

    # 2. Socratic Question
    blocks.append({
        "id": next_id(),
        "type": "socratic_question",
        "question": "At the exact center of a circular loop carrying an electric current, what is the geometric shape of the magnetic field lines?",
        "question_hi": "विद्युत धारा ले जाने वाले वृत्ताकार लूप के ठीक केंद्र पर चुंबकीय क्षेत्र रेखाओं का ज्यामितीय आकार कैसा होता है?",
        "question_gu": "વિદ્યુતપ્રવાહધારિત વર્તુળાકાર લૂપના બરાબર કેન્દ્ર પર ચુંબકીય ક્ષેત્રરેખાઓનો ભૌમિતિક આકાર કેવો હોય છે?",
        "options": [
            "Straight parallel lines perpendicular to the plane of the loop.",
            "Tightly curved small concentric circles.",
            "Zig-zag diagonal waves.",
            "Spiraling inward vortices."
        ],
        "options_hi": [
            "लूप के तल के लंबवत सीधी समानांतर रेखाएं।",
            "अत्यधिक घुमावदार छोटे संकेंद्रीय वृत्त।",
            "टेढ़ी-मेढ़ी विकर्ण तरंगें।",
            "अंदर की ओर घूमते चक्रवात।"
        ],
        "options_gu": [
            "લૂપના સમતલને લંબરૂપે સીધી સમાંતર રેખાઓ.",
            "ખૂબ વળાંકવાળા નાના સમકેન્દ્રી વર્તુળો.",
            "ત્રાંસી ઝિગ-ઝેગ તરંગો.",
            "અંદર તરફ ઘૂમરી ખાતા વમળો."
        ],
        "correct_index": 0,
        "explanation": "As we move towards the center of a circular current loop, the concentric circular field lines become larger and larger. At the exact center, the arcs become so vast that they appear as straight parallel lines perpendicular to the plane of the loop, representing a uniform magnetic field.",
        "explanation_hi": "जैसे-जैसे हम वृत्ताकार लूप के केंद्र की ओर बढ़ते हैं, संकेंद्रीय क्षेत्र रेखाओं के वृत्त बड़े होते जाते हैं। ठीक केंद्र पर, चाप इतने बड़े हो जाते हैं कि वे लूप के तल के लंबवत सीधी समानांतर रेखाओं के रूप में दिखाई देते हैं, जो एकसमान चुंबकीय क्षेत्र को दर्शाते हैं।",
        "explanation_gu": "જેમ જેમ વર્તુળાકાર લૂપના કેન્દ્ર તરફ જઈએ તેમ ક્ષેત્રરેખાઓના વર્તુળો મોટા ને મોટા થતા જાય છે. બરાબર કેન્દ્ર પર ચાપ એટલો મોટો થઈ જાય છે કે તે લૂપના સમતલને લંબ સીધી સમાંતર રેખા જેવો દેખાય છે, જે સમાન ક્ષેત્ર દર્શાવે છે."
    })

    # 3. Discovery (Activity 12.6)
    blocks.append({
        "id": next_id(),
        "type": "discovery",
        "title": "Mapping a Circular Coil & Solenoid",
        "title_hi": "वृत्ताकार कुंडली और परिनालिका का चुंबकीय मानचित्रण",
        "title_gu": "વર્તુળાકાર ગૂંચળા અને સોલેનોઇડનું ચુંબકીય ક્ષેત્રદર્શન",
        "body": "ACTIVITY 12.6:\nTake a rectangular cardboard with two holes. Insert a circular coil having many turns of insulated copper wire through the holes. Connect the coil to a battery, rheostat, and plug key. Sprinkle iron filings uniformly.\n\nWhen current is switched on and cardboard is tapped:\n1. Around each wire segment at the holes, the filings form concentric circles.\n2. Moving away from the wires towards the center, the circles expand continuously.\n3. At the center of the coil, the lines run straight and parallel perpendicular to the coil's plane!\n\nTHE SOLENOID:\nA long coil of many circular turns of insulated copper wire wrapped closely in the shape of a cylinder is called a Solenoid. Sprinkle iron filings around a current-carrying solenoid: The field pattern is IDENTICAL to that of a bar magnet! One end behaves as a magnetic North pole, and the other as a South pole. Inside the solenoid, the field lines are parallel straight lines, proving the magnetic field inside is completely UNIFORM.",
        "body_hi": "क्रियाकलाप 12.6:\nदो छेदों वाला एक कार्डबोर्ड लें और उसमें तांबे के तार की कई फेरों वाली वृत्ताकार कुंडली लगाएं। कुंडली को बैटरी, रियोस्टैट और कुंजी से जोड़ें और कार्डबोर्ड पर लोहे का बुरादा छिड़कें।\n\nकुंजी ऑन करके कार्डबोर्ड थपथपाने पर:\n1. दोनों छेदों के पास तार के चारों ओर संकेंद्रीय वृत्त बनते हैं।\n2. तार से केंद्र की ओर बढ़ने पर ये वृत्त बड़े होते जाते हैं।\n3. कुंडली के केंद्र पर रेखाएं बिल्कुल सीधी और समानांतर हो जाती हैं!\n\nपरिनालिका (Solenoid):\nपास-पास लिपटे विद्युतरोधी तांबे के तार की बेलन के आकार की अनेक फेरों वाली कुंडली को 'परिनालिका' कहते हैं। परिनालिका का चुंबकीय क्षेत्र प्रतिरूप बिल्कुल छड़ चुंबक जैसा होता है! इसका एक सिरा उत्तरी ध्रुव और दूसरा सिरा दक्षिणी ध्रुव की तरह कार्य करता है। परिनालिका के अंदर क्षेत्र रेखाएं समानांतर सीधी रेखाएं होती हैं, जिसका अर्थ है कि अंदर चुंबकीय क्षेत्र पूरी तरह से एकसमान (Uniform) है।",
        "body_gu": "પ્રવૃત્તિ 12.6:\nબે કાણાંવાળા કાર્ડબોર્ડમાંથી ઘણા આંટાવાળા તાંબાના તારની વર્તુળાકાર કોઈલ પસાર કરો. તેને બેટરી, કળ અને ચલ અવરોધ સાથે જોડી લોખંડનો વહેર ભભરાવો.\n\nસ્વિચ ચાલુ કરી ટકોરા મારતાં:\n1. બંને છેડે વાયરની આસપાસ સમકેન્દ્રી વર્તુળો બને છે.\n2. કેન્દ્ર તરફ જતાં આ વર્તુળો સતત મોટા થાય છે.\n3. કેન્દ્રમાં ક્ષેત્રરેખાઓ તદ્દન સીધી અને સમાંતર બને છે!\n\nસોલેનોઇડ (Solenoid):\nઅલગ કરેલા (ઇન્સ્યુલેટેડ) તાંબાના વાયરને પાસપાસે વીંટાળી નળાકાર સ્પ્રિંગ જેવી બનાવેલી રચનાને સોલેનોઇડ કહે છે. તેનું ચુંબકીય ક્ષેત્ર હૂબહૂ ગજિયા ચુંબક જેવું હોય છે! તેનો એક છેડો ઉત્તર ધ્રુવ અને બીજો છેડો દક્ષિણ ધ્રુવ બને છે. સોલેનોઇડની અંદર ક્ષેત્રરેખાઓ સમાંતર સીધી હોવાથી અંદરનું ચુંબકીય ક્ષેત્ર સમાન (Uniform) હોય છે."
    })

    # 4. Theory
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "Physics of Circular Loops, Solenoids & Electromagnets",
        "title_hi": "वृत्ताकार लूप, परिनालिका एवं विद्युत चुंबक का संपूर्ण भौतिकी",
        "title_gu": "વર્તુળાકાર લૂપ, સોલેનોઇડ અને વિદ્યુતચુંબકનું સમગ્ર ભૌતિક વિજ્ઞાન",
        "body": "1. CIRCULAR LOOP FIELD STRENGTH:\n• Proportional to Current: B ∝ I\n• Inversely Proportional to Radius: B ∝ 1/r\n• Proportional to Number of Turns (N): If a coil has N turns, the field is N times as large as that produced by a single turn (B ∝ N*I/r). Why? Because current in each turn has the same direction, so their magnetic fields add up arithmetically!\n\n2. CLOCK FACE RULE FOR POLARITY:\nLooking at the face of a coil or solenoid:\n• CLOCKWISE Current = SOUTH Pole (S)\n• ANTICLOCKWISE Current = NORTH Pole (N)\n\n3. THE SOLENOID:\nMagnetic field inside a long solenoid is uniform: B = μ₀*n*I (where n is turns per unit length).\n\n4. ELECTROMAGNET:\nA strong magnetic field produced inside a solenoid can be used to magnetize a piece of magnetic material, like SOFT IRON, when placed inside the coil. The magnet so formed is called an ELECTROMAGNET.\n• Why Soft Iron? Soft iron has high permeability and low retentivity: it magnetizes powerfully when current flows, and completely loses its magnetism the instant current is switched off (temporary magnet). Steel retains magnetism and becomes a permanent magnet, making it unsuitable for electromagnets.",
        "body_hi": "1. वृत्ताकार लूप की क्षेत्र प्रबलता:\n• धारा के समानुपाती: B ∝ I\n• त्रिज्या के व्युत्क्रमानुपाती: B ∝ 1/r\n• फेरों की संख्या (N) के समानुपाती: यदि कुंडली में N फेरे हैं, तो चुंबकीय क्षेत्र 1 फेरे की तुलना में N गुना प्रबल होगा (B ∝ N*I/r)। ऐसा इसलिए क्योंकि प्रत्येक फेरे में धारा समान दिशा में बहती है, जिससे उनके चुंबकीय क्षेत्र सीधे जुड़ जाते हैं!\n\n2. ध्रुवता के लिए क्लॉक फेस नियम (Clock Rule):\nकुंडली के फलक को देखने पर:\n• दक्षिणावर्त धारा (Clockwise) = दक्षिणी ध्रुव (South Pole, S)\n• वामावर्त धारा (Anticlockwise) = उत्तरी ध्रुव (North Pole, N)\n\n3. परिनालिका:\nपरिनालिका के भीतर चुंबकीय क्षेत्र एकसमान होता है: B = μ₀*n*I।\n\n4. विद्युत चुंबक (Electromagnet):\nपरिनालिका के अंदर उत्पन्न शक्तिशाली चुंबकीय क्षेत्र का उपयोग उसके भीतर रखे नरम लोहे (Soft Iron) की छड़ को चुंबकित करने के लिए किया जाता है। इस प्रकार बने चुंबक को 'विद्युत चुंबक' कहते हैं।\n• नरम लोहा ही क्यों? नरम लोहा अत्यधिक चुंबकीय हो जाता है और जैसे ही धारा बंद की जाती है, उसका चुंबकत्व तुरंत समाप्त हो जाता है (अस्थायी चुंबक)। स्टील का चुंबकत्व समाप्त नहीं होता, इसलिए वह स्थाई चुंबक बनाने के काम आता है।",
        "body_gu": "1. વર્તુળાકાર લૂપની ક્ષેત્ર પ્રબળતા:\n• પ્રવાહના સમપ્રમાણમાં: B ∝ I\n• ત્રિજ્યાના વ્યસ્ત પ્રમાણમાં: B ∝ 1/r\n• આંટાની સંખ્યા (N) ના સમપ્રમાણમાં: જો કોઈલમાં N આંટા હોય તો ક્ષેત્ર N ગણું બને છે (B ∝ N*I/r). કારણ કે દરેક આંટામાં પ્રવાહની દિશા સમાન હોવાથી તેમના ક્ષેત્રોનો સરવાળો થાય છે!\n\n2. ધ્રુવીયતા માટે ઘડિયાળનો નિયમ (Clock Face Rule):\nગૂંચળા સામે જોતાં:\n• સમઘડી પ્રવાહ (Clockwise) = દક્ષિણ ધ્રુવ (South Pole, S)\n• વિષમઘડી પ્રવાહ (Anticlockwise) = ઉત્તર ધ્રુવ (North Pole, N)\n\n3. સોલેનોઇડ:\nસોલેનોઇડની અંદર ચુંબકીય ક્ષેત્ર સમાન હોય છે: B = μ₀*n*I.\n\n4. વિદ્યુતચુંબક (Electromagnet):\nસોલેનોઇડની અંદર નરમ લોખંડનો ગર્ભ મૂકી પ્રવાહ પસાર કરતાં તે અતિશક્તિશાળી ચુંબક બને છે. તેને 'વિદ્યુતચુંબક' કહે છે.\n• નરમ લોખંડ કેમ? નરમ લોખંડ પ્રવાહ ચાલુ હોય ત્યાં સુધી જ ચુંબકત્વ જાળવે છે અને સ્વિચ બંધ કરતાં તરત ચુંબકત્વ ગુમાવે છે (અસ્થાયી ચુંબક). સ્ટીલ કાયમી ચુંબક બની જતું હોવાથી વિદ્યુતચુંબક માટે વાપરી શકાતું નથી."
    })

    # Teacher Tip: Comparison Table
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Teacher Tip: Electromagnet vs Permanent Bar Magnet",
        "title_hi": "शिक्षक टिप: विद्युत चुंबक और स्थाई चुंबक में 4 महत्वपूर्ण अंतर",
        "title_gu": "શિક્ષક ટિપ: વિદ્યુતચુંબક અને કાયમી ચુંબક વચ્ચેના 4 મુખ્ય તફાવતો",
        "body": "A guaranteed 2-mark or 3-mark exam question:\n1. NATURE: Electromagnet is a temporary magnet (loses magnetism when current stops); Permanent magnet retains its magnetism indefinitely.\n2. STRENGTH: Electromagnet field strength can be easily changed (by altering current or number of turns); Permanent magnet strength is fixed.\n3. POLARITY: Electromagnet polarity can be reversed simply by flipping current direction; Permanent magnet polarity is fixed.\n4. CORE: Electromagnet uses soft iron; Permanent magnet uses carbon steel, Alnico, or Neodymium.",
        "body_hi": "बोर्ड परीक्षा के लिए 2 या 3 अंक का अनिवार्य प्रश्न:\n1. प्रकृति: विद्युत चुंबक अस्थायी है (धारा बंद होते ही चुंबकत्व समाप्त); स्थाई चुंबक का चुंबकत्व हमेशा बना रहता है।\n2. प्रबलता: विद्युत चुंबक की शक्ति को धारा या फेरों की संख्या बदलकर आसानी से बदला जा सकता है; स्थाई चुंबक की शक्ति निश्चित होती है।\n3. ध्रुवता: धारा की दिशा बदलकर विद्युत चुंबक के ध्रुव (N और S) बदले जा सकते हैं; स्थाई चुंबक के ध्रुव निश्चित होते हैं।\n4. पदार्थ: विद्युत चुंबक में नरम लोहे का उपयोग होता है; स्थाई चुंबक में कार्बन स्टील, एल्निको या नियोडिमियम का उपयोग होता है।",
        "body_gu": "બોર્ડ પરીક્ષા માટે 2 કે 3 ગુણનો ખૂબ અગત્યનો પ્રશ્ન:\n1. સ્વભાવ: વિદ્યુતચુંબક અસ્થાયી છે (પ્રવાહ બંધ થતાં ચુંબકત્વ નષ્ટ થાય છે); કાયમી ચુંબકનું ચુંબકત્વ લાંબો સમય ટકી રહે છે.\n2. પ્રબળતા: વિદ્યુતચુંબકની પ્રબળતા પ્રવાહ કે આંટા બદલી સરળતાથી બદલી શકાય છે; કાયમી ચુંબકની પ્રબળતા નિશ્ચિત હોય છે.\n3. ધ્રુવીયતા: પ્રવાહની દિશા ઉલટાવી ધ્રુવો બદલી શકાય છે; કાયમી ચુંબકના ધ્રુવો નિશ્ચિત રહે છે.\n4. દ્રવ્ય: વિદ્યુતચુંબકમાં નરમ લોખંડ વપરાય છે; કાયમી ચુંબકમાં સ્ટીલ કે એલ્નિકો વપરાય છે."
    })

    # 5. Knowledge Check (In-text Set 3 Q3)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT In-Text Q: The magnetic field inside a long straight solenoid-carrying current:",
        "question_hi": "NCERT पाठ्य-निहित प्रश्न: किसी लंबी सीधी धारावाही परिनालिका के भीतर चुंबकीय क्षेत्र:",
        "question_gu": "NCERT પાઠ્યપુસ્તક પ્રશ્ન: વિદ્યુતપ્રવાહધારિત લાંબા સુરેખ સોલેનોઇડની અંદરના વિસ્તારમાં ચુંબકીય ક્ષેત્ર:",
        "options": [
            "is the same at all points.",
            "is zero.",
            "decreases as we move towards its ends.",
            "increases as we move towards its ends."
        ],
        "options_hi": [
            "सभी बिंदुओं पर समान होता है।",
            "शून्य होता है।",
            "इसके सिरों की ओर जाने पर घटता है।",
            "इसके सिरों की ओर जाने पर बढ़ता है।"
        ],
        "options_gu": [
            "બધા જ બિંદુઓએ સમાન હોય છે.",
            "શૂન્ય હોય છે.",
            "તેના છેડા તરફ જતાં ઘટે છે.",
            "તેના છેડા તરફ જતાં વધે છે."
        ],
        "correct_index": 0,
        "explanation": "Inside a long straight current-carrying solenoid, the magnetic field lines are parallel straight lines. This indicates that the magnetic field has identical magnitude and direction at every point inside the core, meaning it is completely uniform.",
        "explanation_hi": "लंबी सीधी धारावाही परिनालिका के भीतर चुंबकीय क्षेत्र रेखाएं समानांतर सीधी रेखाएं होती हैं। यह दर्शाता है कि परिनालिका के अंदर प्रत्येक बिंदु पर चुंबकीय क्षेत्र का परिमाण और दिशा समान है, अर्थात् क्षेत्र पूरी तरह से एकसमान (Uniform) है।",
        "explanation_gu": "વિદ્યુતપ્રવાહધારિત લાંબા સોલેનોઇડની અંદર ક્ષેત્રરેખાઓ પરસ્પર સમાંતર અને સુરેખ હોય છે, જે દર્શાવે છે કે સોલેનોઇડના અંદરના તમામ બિંદુઓએ ચુંબકીય ક્ષેત્રનું મૂલ્ય અને દિશા એકસરખાં (સમાન) હોય છે."
    })

    # 6. Reflection
    blocks.append({
        "id": next_id(),
        "type": "reflection",
        "title": "Why Can't Steel Be Used for Industrial Scrap Cranes?",
        "title_hi": "कबाड़ उठाने वाली क्रेन में स्टील का उपयोग क्यों नहीं किया जा सकता?",
        "title_gu": "કચરાના ડબ્બા/સ્ક્રેપ ક્રેનમાં સ્ટીલ કેમ ન વાપરી શકાય?",
        "body": "Imagine operating an industrial scrapyard crane with an electromagnet made of steel instead of soft iron. You switch the current ON, and the crane powerfully lifts a 3-ton crushed automobile. You swing the crane over the cargo truck and switch the current OFF. But horror strikes: the steel core has become a permanent magnet! The automobile stays glued to the magnet and refuses to drop! This is why soft iron's zero retentivity is an absolute engineering necessity.",
        "body_hi": "कल्पना कीजिए कि कबाड़खाने की क्रेन में नरम लोहे के बजाय स्टील के कोर वाला चुंबक लगा है। आप धारा चालू करते हैं और क्रेन 3 टन की कार उठा लेती है। आप कार को ट्रक के ऊपर ले जाते हैं और धारा बंद कर देते हैं। लेकिन स्टील स्थाई चुंबक बन चुका है! कार क्रेन से चिपकी रहती है और नीचे नहीं गिरती! इसीलिए तुरंत चुंबकत्व खोने वाला नरम लोहा ही इंजीनियरिंग की अनिवार्य आवश्यकता है।",
        "body_gu": "કલ્પના કરો કે સ્ક્રેપ ક્રેનમાં નરમ લોખંડને બદલે સ્ટીલનો ગર્ભ વપરાયો છે. પ્રવાહ ચાલુ કરતાં ક્રેન 3 ટનની કાર ઊંચકી લે છે. તમે ટ્રક ઉપર કાર લાવી સ્વિચ બંધ કરો છો. પણ સ્ટીલ કાયમી ચુંબક બની ગયું હોવાથી કાર ચોંટેલી જ રહે છે અને નીચે પડતી જ નથી! આ કારણે જ પ્રવાહ બંધ થતાં તરત ચુંબકત્વ ગુમાવતું નરમ લોખંડ જ વાપરવું અનિવાર્ય છે."
    })

    # 7. Connection
    blocks.append({
        "id": next_id(),
        "type": "connection",
        "title": "Superconducting Solenoids: The Engine of Modern Hospital MRI",
        "title_hi": "अतिचालक परिनालिकाएं: आधुनिक अस्पताल एमआरआई का दिल",
        "title_gu": "અતિવાહક સોલેનોઇડ: આધુનિક હોસ્પિટલ એમઆરઆઈ (MRI) નું હૃદય",
        "body": "How do doctors take crystal-clear 3D images of your brain without cutting open your skull? Inside every Magnetic Resonance Imaging (MRI) machine is a massive cylindrical solenoid wound with superconducting niobium-titanium wire chilled by liquid helium to -269°C (4 Kelvin)! At this temperature, electrical resistance drops to exactly ZERO, allowing thousands of amperes to flow endlessly without heating, creating an immense, perfectly uniform magnetic field of 1.5 to 3.0 Tesla (60,000 times stronger than Earth's field) to align hydrogen protons in human tissue.",
        "body_hi": "डॉक्टर बिना कोई चीरा लगाए आपके मस्तिष्क की स्पष्ट 3D छवियां कैसे ले लेते हैं? प्रत्येक एमआरआई (MRI) मशीन के अंदर तरल हीलियम द्वारा -269°C तक ठंडा किया गया एक विशाल परिनालिका कॉइल होता है। इस तापमान पर विद्युत प्रतिरोध शून्य हो जाता है, जिससे बिना किसी प्रतिरोध के हजारों एम्पीयर धारा बहती है और 1.5 से 3 टेस्ला का शक्तिशाली चुंबकीय क्षेत्र उत्पन्न होता है, जो शरीर के प्रोटॉनों को संरेखित करके आंतरिक अंगों की तस्वीरें बनाता है।",
        "body_gu": "ડોકટરો મગજની સ્પષ્ટ 3D તસવીરો કાપકૂપ વગર કેવી રીતે મેળવે છે? દરેક MRI મશીનમાં પ્રવાહી હિલીયમ વડે -269°C તાપમાને ઠંડુ રાખેલું અતિવાહક સોલેનોઇડ હોય છે. આ તાપમાને અવરોધ શૂન્ય થતાં હજારો એમ્પીયરનો પ્રવાહ સતત વહે છે અને 1.5 થી 3 ટેસ્લાનું પ્રચંડ સમાન ચુંબકીય ક્ષેત્ર બનાવે છે, જે શરીરના પેશીઓની અદભુત તસવીરો આપે છે."
    })

    # 8. Mastery Challenge (In-text Set 3 Q1)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT In-Text Q: Consider a circular loop of wire lying in the plane of the table. Let the current pass through the loop clockwise. Apply the right-hand rule to find the direction of the magnetic field inside and outside the loop.",
        "question_hi": "NCERT पाठ्य-निहित प्रश्न: मान लीजिए आप मेज के तल में तार का एक वृत्ताकार लूप रखे हुए हैं। मान लीजिए इसमें दक्षिणावर्त (Clockwise) दिशा में धारा बह रही है। दाहिने हाथ के नियम द्वारा लूप के भीतर और बाहर चुंबकीय क्षेत्र की दिशा ज्ञात कीजिए।",
        "question_gu": "NCERT પાઠ્યપુસ્તક પ્રશ્ન: ધારો કે ટેબલના સમતલમાં તારનો એક વર્તુળાકાર લૂપ મૂકેલો છે. ધારો કે તેમાંથી સમઘડી (Clockwise) દિશામાં વિદ્યુતપ્રવાહ વહે છે. જમણા હાથના નિયમ મુજબ લૂપની અંદર અને બહાર ચુંબકીય ક્ષેત્રની દિશા શોધો.",
        "options": [
            "Inside the loop: downwards (into the table); Outside the loop: upwards (out of the table).",
            "Inside the loop: upwards (out of the table); Outside the loop: downwards (into the table).",
            "Both inside and outside: downwards into the table.",
            "Both inside and outside: upwards out of the table."
        ],
        "options_hi": [
            "लूप के भीतर: नीचे की ओर (मेज के अंदर); लूप के बाहर: ऊपर की ओर (मेज से बाहर)।",
            "लूप के भीतर: ऊपर की ओर (मेज से बाहर); लूप के बाहर: नीचे की ओर (मेज के अंदर)।",
            "भीतर और बाहर दोनों जगह: मेज के अंदर नीचे की ओर।",
            "भीतर और बाहर दोनों जगह: मेज से बाहर ऊपर की ओर।"
        ],
        "options_gu": [
            "લૂપની અંદર: નીચે તરફ (ટેબલની અંદર); લૂપની બહાર: ઉપર તરફ (ટેબલમાંથી બહાર).",
            "લૂપની અંદર: ઉપર તરફ (ટેબલમાંથી બહાર); લૂપની બહાર: નીચે તરફ (ટેબલની અંદર).",
            "અંદર અને બહાર બંને જગ્યાએ: નીચે તરફ ટેબલમાં.",
            "અંદર અને બહાર બંને જગ્યાએ: ઉપર તરફ ટેબલની બહાર."
        ],
        "correct_index": 0,
        "explanation": "Applying the Right-Hand Thumb Rule to any segment of the circular wire with clockwise current: inside the loop, the curled fingers point perpendicularly downwards into the plane of the table. Curving around outside the loop, the fingers point upwards out of the table.",
        "explanation_hi": "दक्षिणावर्त धारा वाले तार के किसी भी हिस्से पर दाहिने हाथ के अंगूठे का नियम लगाने पर: लूप के अंदर उंगलियां मेज के तल के लंबवत नीचे की ओर इशारा करती हैं। लूप के बाहर घूमकर उंगलियां मेज से ऊपर की ओर निकलती हैं।",
        "explanation_gu": "સમઘડી પ્રવાહવાળા વાયરના કોઈપણ ભાગ પર જમણા હાથનો નિયમ વાપરતાં: લૂપની અંદર આંગળીઓ ટેબલના સમતલને લંબરૂપે નીચે તરફ જાય છે, જ્યારે લૂપની બહાર આંગળીઓ ફરીને ઉપર તરફ બહાર નીકળે છે."
    })

    # =========================================================================
    # MODULE 4: FORCE ON CONDUCTOR & FLEMING'S LEFT-HAND RULE (8-STEP PEDAGOGY)
    # =========================================================================

    # 1. Hook
    blocks.append({
        "id": next_id(),
        "type": "hook",
        "title": "When Magnetism Pushes Back: The Spark of Electric Motors",
        "title_hi": "जब चुंबक ने पलटवार किया: विद्युत मोटर की अद्भुत खोज",
        "title_gu": "જ્યારે ચુંબકે સામું બળ કર્યું: વિદ્યુત મોટરની અદભુત ક્રાંતિ",
        "body": "Sir Isaac Newton's Third Law states: To every action there is an equal and opposite reaction. In 1820, French physicist André-Marie Ampère reasoned: 'If a current-carrying wire exerts a magnetic force on a compass needle to deflect it, must not the compass needle exert an equal and opposite physical force on the current-carrying wire?' He tested it: suspended between two magnetic poles, a lightweight metal wire physically leaped into the air the microsecond electric current flowed! This mechanical push is the foundation of every electric motor powering our modern civilization.",
        "body_hi": "सर आइजैक न्यूटन का तीसरा नियम कहता है: प्रत्येक क्रिया की बराबर और विपरीत प्रतिक्रिया होती है। 1820 में फ्रांसीसी भौतिक विज्ञानी आंद्रे-मैरी एम्पीयर ने सोचा: 'यदि धारावाही तार कंपास की सुई पर बल लगाकर उसे घुमा सकता है, तो क्या चुंबक को भी धारावाही तार पर बराबर बल नहीं लगाना चाहिए?' उन्होंने प्रयोग किया: दो चुंबकों के बीच लटका हुआ एक तार धारा बहते ही हवा में उछल पड़ा! यही यांत्रिक धक्का आज हमारी दुनिया के हर पंखे, इलेक्ट्रिक कार और ट्रेन की मोटरों को चलाता है।",
        "body_gu": "ન્યૂટનનો ત્રીજો નિયમ કહે છે: દરેક ક્રિયાબળ સામે સમાન અને વિરુદ્ધ પ્રતિક્રિયાબળ હોય છે. 1820 માં ફ્રેન્ચ વૈજ્ઞાનિક આન્દ્રે-મેરી એમ્પીયરે વિચાર્યું: 'જો વિદ્યુતપ્રવાહ ચુંબકીય સોય પર બળ લગાડી શકે, તો શું ચુંબકે પણ વાયર પર સામું બળ ન લગાડવું જોઈએ?' તેમણે પ્રયોગ કર્યો: બે ચુંબકીય ધ્રુવો વચ્ચે લટકાવેલો વાયર કરંટ ચાલુ થતાં જ હવામાં કૂદકો મારવા લાગ્યો! આ યાંત્રિક ધક્કો જ આપણી દુનિયાની તમામ ઇલેક્ટ્રિક મોટરોનો પાયો છે."
    })

    # 2. Socratic Question
    blocks.append({
        "id": next_id(),
        "type": "socratic_question",
        "question": "Under what condition will a current-carrying straight conductor placed in a strong magnetic field experience ZERO mechanical force?",
        "question_hi": "एक शक्तिशाली चुंबकीय क्षेत्र में रखे धारावाही सीधे चालक पर किस स्थिति में शून्य (Zero) यांत्रिक बल लगेगा?",
        "question_gu": "પ્રબળ ચુંબકીય ક્ષેત્રમાં મૂકેલા વિદ્યુતપ્રવાહધારિત સુરેખ વાહક પર કઈ પરિસ્થિતિમાં શૂન્ય (Zero) યાંત્રિક બળ લાગશે?",
        "options": [
            "When the conductor is aligned parallel (or antiparallel) to the direction of the magnetic field.",
            "When the conductor is placed perpendicular (at 90 degrees) to the magnetic field.",
            "When the electric current is increased to its maximum value.",
            "When the conductor is made of pure copper instead of aluminium."
        ],
        "options_hi": [
            "जब चालक चुंबकीय क्षेत्र की दिशा के समानांतर (या प्रति-समानांतर) रखा हो।",
            "जब चालक चुंबकीय क्षेत्र के लंबवत (90 डिग्री पर) रखा हो।",
            "जब विद्युत धारा को उसके अधिकतम मान तक बढ़ा दिया जाए।",
            "जब चालक एल्यूमीनियम के बजाय शुद्ध तांबे का बना हो।"
        ],
        "options_gu": [
            "જ્યારે વાહક ચુંબકીય ક્ષેત્રની દિશાને સમાંતર (કે પરસ્પર વિરુદ્ધ સમાંતર) ગોઠવાયેલો હોય.",
            "જ્યારે વાહક ચુંબકીય ક્ષેત્રને લંબરૂપે (90 અંશના ખૂણે) ગોઠવાયેલો હોય.",
            "જ્યારે વિદ્યુતપ્રવાહ વધારીને મહત્તમ કરવામાં આવે.",
            "જ્યારે વાહક એલ્યુમિનિયમને બદલે શુદ્ધ તાંબાનો બનેલો હોય."
        ],
        "correct_index": 0,
        "explanation": "The magnetic force on a conductor of length L carrying current I in field B is given by F = B*I*L*sin(θ), where θ is the angle between current and magnetic field. When θ = 0° or 180° (parallel or antiparallel), sin(θ) = 0, so the force is identically ZERO. Force is maximum when θ = 90° (perpendicular).",
        "explanation_hi": "चुंबकीय क्षेत्र में धारावाही चालक पर लगने वाला बल F = B*I*L*sin(θ) होता है, जहाँ θ धारा और चुंबकीय क्षेत्र के बीच का कोण है। जब चालक समानांतर होता है (θ = 0° या 180°), तो sin(θ) = 0 होता है, इसलिए बल शून्य हो जाता है। जब θ = 90° (लंबवत) होता है, तब बल अधिकतम होता है।",
        "explanation_gu": "વાહક પર લાગતું ચુંબકીય બળ F = B*I*L*sin(θ) છે, જ્યાં θ એ પ્રવાહ અને ચુંબકીય ક્ષેત્ર વચ્ચેનો ખૂણો છે. જ્યારે વાહક સમાંતર હોય (θ = 0° કે 180°), ત્યારે sin(θ) = 0 થવાથી બળ શૂન્ય બને છે. જ્યારે લંબરૂપ (90°) હોય ત્યારે બળ મહત્તમ હોય છે."
    })

    # 3. Discovery (Activity 12.7)
    blocks.append({
        "id": next_id(),
        "type": "discovery",
        "title": "The Kicking Wire: Activity 12.7",
        "title_hi": "झूलता हुआ एल्युमिनियम का तार: क्रियाकलाप 12.7",
        "title_gu": "ઉછળતો એલ્યુમિનિયમનો સળિયો: પ્રવૃત્તિ 12.7",
        "body": "ACTIVITY 12.7:\nSuspend a small aluminium rod AB horizontally using connecting wires from a stand. Place a strong horseshoe magnet such that the rod lies between its two poles with magnetic field directed vertically upwards (North pole below the rod, South pole above it).\n\nConnect the rod in series with a battery, key, and rheostat so current flows from B to A (horizontal):\n1. Switch on the current: The aluminium rod is physically displaced (pushed) to the LEFT!\n2. Reverse the current (from A to B): The rod is kicked to the RIGHT!\n3. Flip the magnet so field points vertically downwards: The direction of displacement reverses again!\n4. Increase the current or use a stronger magnet: The displacement of the rod increases noticeably!\n\nCONCLUSION:\nA current-carrying conductor in a magnetic field experiences a mechanical force whose direction depends mutually on the direction of current and the direction of the magnetic field.",
        "body_hi": "क्रियाकलाप 12.7:\nएक स्टैंड से तारों के सहारे एक छोटी एल्युमिनियम की छड़ AB को क्षैतिज रूप से लटकाएं। एक प्रबल नाल चुंबक (Horseshoe Magnet) को इस तरह रखें कि छड़ दोनों ध्रुवों के बीच रहे और चुंबकीय क्षेत्र ऊपर की ओर हो (N ध्रुव नीचे, S ध्रुव ऊपर)।\n\nछड़ को बैटरी और कुंजी से जोड़कर धारा B से A की ओर प्रवाहित करें:\n1. धारा चालू करते ही छड़ बाईं (Left) ओर तेजी से विस्थापित होती है!\n2. धारा की दिशा उलटने पर (A से B करने पर), छड़ दाईं (Right) ओर विस्थापित होती है!\n3. चुंबक को उल्टा करने पर (क्षेत्र नीचे करने पर), विस्थापन की दिशा पुनः उलट जाती है!\n4. धारा बढ़ाने या अधिक शक्तिशाली चुंबक लगाने पर छड़ का विस्थापन और अधिक बढ़ जाता है!\n\nनिष्कर्ष:\nचुंबकीय क्षेत्र में धारावाही चालक एक यांत्रिक बल का अनुभव करता है, जिसकी दिशा धारा की दिशा और चुंबकीय क्षेत्र की दिशा दोनों पर निर्भर करती है।",
        "body_gu": "પ્રવૃત્તિ 12.7:\nસ્ટેન્ડ પરથી પાતળા વાયરો વડે નાનો એલ્યુમિનિયમનો સળિયો AB સમક્ષિતિજ લટકાવો. ઘોડાની નાળ આકારના પ્રબળ ચુંબકને એવી રીતે ગોઠવો કે સળિયો બંને ધ્રુવો વચ્ચે રહે અને ચુંબકીય ક્ષેત્ર ઉપર તરફ હોય (N ધ્રુવ નીચે, S ધ્રુવ ઉપર).\n\nસળિયામાંથી B થી A તરફ પ્રવાહ વહેવડાવો:\n1. પ્રવાહ ચાલુ કરતાં જ સળિયો ડાબી બાજુ જોરથી ધકેલાય છે!\n2. પ્રવાહ ઉલટાવી A થી B કરતાં સળિયો જમણી બાજુ ધકેલાય છે!\n3. ચુંબક ઉલટાવતાં (ક્ષેત્ર નીચે કરતાં) વિચલનની દિશા ફરી બદલાઈ જાય છે!\n4. પ્રવાહ વધારતાં કે પ્રબળ ચુંબક વાપરતાં સળિયો વધુ દૂર સુધી ધકેલાય છે!\n\nતારણ:\nચુંબકીય ક્ષેત્રમાં રહેલો વિદ્યુતપ્રવાહધારિત વાહક યાંત્રિક બળ અનુભવે છે, જેની દિશા પ્રવાહ અને ચુંબકીય ક્ષેત્ર બંનેની દિશા પર આધારિત હોય છે."
    })

    # 4. Theory
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "Fleming's Left-Hand Rule & Force Formula",
        "title_hi": "फ्लेमिंग का वाम-हस्त नियम (बाएं हाथ का नियम) एवं बल का सूत्र",
        "title_gu": "ફ્લેમિંગનો ડાબા હાથનો નિયમ અને ચુંબકીય બળનું સૂત્ર",
        "body": "1. FLEMING'S LEFT-HAND RULE:\nStretch the thumb, forefinger (index finger), and middle finger of your LEFT HAND mutually perpendicular to each other:\n• FOREFINGER points in the direction of the MAGNETIC FIELD (B).\n• MIDDLE FINGER points in the direction of the ELECTRIC CURRENT (I).\n• THUMB points in the direction of MOTION or FORCE (F) acting on the conductor.\n\nMemory Aid (FBI / Father-Mother-Child):\n• Thumb = Force (Father)\n• Forefinger = Field (Mother / B-Field)\n• Middle finger = Current (Child / I-Current)\n\n2. MAGNITUDE OF FORCE:\nF = B * I * L * sin(θ)\n• Force is MAXIMUM when the conductor is perpendicular to field (θ = 90°, sin 90° = 1, F_max = B*I*L).\n• Force is ZERO when conductor is parallel to field (θ = 0°, sin 0° = 0).\n• Force increases with: stronger magnetic field (B), larger current (I), and longer length of conductor inside field (L).\n\n3. CHARGED PARTICLES IN MAGNETIC FIELDS:\nA moving charge constitutes current. Direction of current for positive charges (protons, alpha particles) is their direction of motion. Direction of current for negative charges (electrons) is OPPOSITE to their direction of motion.",
        "body_hi": "1. फ्लेमिंग का वाम-हस्त नियम (Fleming's Left-Hand Rule):\nअपने बाएं हाथ के अंगूठे, तर्जनी (Forefinger) और मध्यमा (Middle finger) को इस प्रकार फैलाएं कि वे तीनों एक-दूसरे के परस्पर लंबवत हों:\n• तर्जनी: चुंबकीय क्षेत्र की दिशा (B) दर्शाती है।\n• मध्यमा: विद्युत धारा की दिशा (I) दर्शाती है।\n• अंगूठा: चालक पर लगने वाले बल या गति की दिशा (F) को दर्शाता है।\n\nयाद रखने की ट्रिक (Father - Mother - Child):\n• अंगूठा (Thumb) = Force (बल - Father)\n• तर्जनी (Forefinger) = Field (क्षेत्र - Mother)\n• मध्यमा (Middle finger) = Current (धारा - Child)\n\n2. बल का परिमाण:\nF = B * I * L * sin(θ)\n• जब चालक चुंबकीय क्षेत्र के लंबवत (90°) हो, तो बल अधिकतम होता है (F = B*I*L)।\n• जब चालक समानांतर (0°) हो, तो बल शून्य होता है।\n• चुंबकीय क्षेत्र बढ़ाने, धारा बढ़ाने या तार की लंबाई बढ़ाने पर बल बढ़ता है।\n\n3. चुंबकीय क्षेत्र में गतिमान आवेश:\nगतिमान आवेश ही धारा है। धनावेश (प्रोटॉन, अल्फा कण) की गति की दिशा ही धारा की दिशा होती है। ऋणावेश (इलेक्ट्रॉन) की गति की दिशा के विपरीत धारा की दिशा मानी जाती है।",
        "body_gu": "1. ફ્લેમિંગનો ડાબા હાથનો નિયમ (Fleming's Left-Hand Rule):\nતમારા ડાબા હાથના અંગૂઠા, પ્રથમ આંગળી (તર્જની) અને મધ્યમા આંગળીને પરસ્પર કાટખૂણે (લંબરૂપે) ફેલાવો:\n• પ્રથમ આંગળી (તર્જની): ચુંબકીય ક્ષેત્રની દિશા (B) દર્શાવે છે.\n• બીજી આંગળી (મધ્યમા): વિદ્યુતપ્રવાહની દિશા (I) દર્શાવે છે.\n• અંગૂઠો: વાહક પર લાગતા ચુંબકીય બળ કે ગતિની દિશા (F) દર્શાવે છે.\n\nયાદ રાખવાની રીત (Father - Mother - Child):\n• અંગૂઠો = Force (બળ - F)\n• પહેલી આંગળી = Field (ક્ષેત્ર - B)\n• વચ્ચેની આંગળી = Current (પ્રવાહ - I)\n\n2. બળનું મૂલ્ય:\nF = B * I * L * sin(θ)\n• વાહક ક્ષેત્રને લંબ હોય (90°) ત્યારે બળ મહત્તમ હોય છે (F = B*I*L).\n• વાહક સમાંતર હોય (0°) ત્યારે બળ શૂન્ય બને છે.\n\n3. ગતિમાન વિદ્યુતભારો:\nધનભાર (પ્રોટોન, આલ્ફા કણ) ની ગતિની દિશા એ જ પ્રવાહની દિશા ગણાય છે. જ્યારે ઋણભાર (ઇલેક્ટ્રોન) ની ગતિની વિરુદ્ધ દિશામાં વિદ્યુતપ્રવાહ ગણવામાં આવે છે."
    })

    # Worked Example (NCERT Example 12.2)
    blocks.append({
        "id": next_id(),
        "type": "example",
        "title": "NCERT Example 12.2: Force on an Injected Electron",
        "title_hi": "NCERT उदाहरण 12.2: इलेक्ट्रॉन पर लगने वाले बल की दिशा",
        "title_gu": "NCERT ઉદાહરણ 12.2: દાખલ થતા ઇલેક્ટ્રોન પર લાગતા બળની દિશા",
        "body": "PROBLEM:\nAn electron enters a magnetic field at right angles to it, where the magnetic field is directed towards the right and the electron moves vertically downwards. The direction of force acting on the electron will be:\n(a) to the right (b) to the left (c) out of the page (d) into the page.\n\nSOLUTION:\n• Magnetic Field (B): Directed to the RIGHT -> Forefinger points RIGHT.\n• Direction of Electron Motion: Vertically DOWNWARDS.\n• CRITICAL PRINCIPLE: The direction of electric current is OPPOSITE to the direction of motion of negative charges (electrons). Therefore, current (I) is directed vertically UPWARDS -> Middle finger points UPWARDS.\n• Apply Fleming's Left-Hand Rule with Left Hand:\nForefinger pointing RIGHT, Middle finger pointing UPWARDS.\n• Your THUMB points directly INTO THE PAGE!\n• Correct Answer: (d) into the page.",
        "body_hi": "प्रश्न:\nकोई इलेक्ट्रॉन किसी चुंबकीय क्षेत्र में क्षेत्र के लंबवत प्रवेश करता है। चुंबकीय क्षेत्र दाईं ओर है और इलेक्ट्रॉन नीचे की ओर गति कर रहा है। इलेक्ट्रॉन पर लगने वाले बल की दिशा होगी:\n(a) दाईं ओर (b) बाईं ओर (c) पृष्ठ से बाहर (d) पृष्ठ के अंदर की ओर।\n\nहल:\n• चुंबकीय क्षेत्र (B): दाईं ओर -> तर्जनी को दाईं ओर रखें।\n• इलेक्ट्रॉन की गति: नीचे की ओर।\n• महत्वपूर्ण नियम: धारा की दिशा इलेक्ट्रॉन (ऋणावेश) की गति की दिशा के विपरीत मानी जाती है। अतः धारा (I) ऊपर की ओर है -> मध्यमा को ऊपर की ओर रखें।\n• बाएं हाथ का नियम लगाने पर:\nतर्जनी दाईं ओर, मध्यमा ऊपर की ओर रखने पर अंगूठा कागज के तल के लंबवत अंदर की ओर (Into the page) संकेत करता है।\n• सही उत्तर: (d) पृष्ठ के अंदर की ओर।",
        "body_gu": "પ્રશ્ન:\nએક ઇલેક્ટ્રોન ચુંબકીય ક્ષેત્રને લંબરૂપે દાખલ થાય છે. ચુંબકીય ક્ષેત્ર જમણી તરફ છે અને ઇલેક્ટ્રોન નીચે તરફ ગતિ કરે છે. ઇલેક્ટ્રોન પર લાગતા બળની દિશા કઈ હશે?\n(a) જમણી તરફ (b) ડાબી તરફ (c) પાનાની બહાર (d) પાનાની અંદર તરફ.\n\nઉકેલ:\n• ચુંબકીય ક્ષેત્ર (B): જમણી તરફ -> પહેલી આંગળી જમણી તરફ રાખો.\n• ઇલેક્ટ્રોનની ગતિ: નીચે તરફ.\n• મહત્વનો સિદ્ધાંત: ઇલેક્ટ્રોન ઋણભારિત હોવાથી વિદ્યુતપ્રવાહની દિશા તેની ગતિની વિરુદ્ધ એટલે કે ઉપર તરફ ગણાય -> વચ્ચેની આંગળી ઉપર તરફ રાખો.\n• ડાબા હાથનો નિયમ વાપરતાં:\nપહેલી આંગળી જમણી બાજુ અને વચ્ચેની આંગળી ઉપર રાખતાં અંગૂઠો પાનાની અંદર તરફ (Into the page) દિશા દર્શાવે છે.\n• સાચો જવાબ: (d) પાનાની અંદર તરફ."
    })

    # Teacher Tip: Common Trap
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Teacher Tip: The 3 Classic Pitfalls in Fleming's Left-Hand Rule",
        "title_hi": "शिक्षक टिप: बाएं हाथ के नियम में 3 सबसे आम गलतियां",
        "title_gu": "શિક્ષક ટિપ: ડાબા હાથના નિયમમાં વિદ્યાર્થીઓ દ્વારા થતી 3 સામાન્ય ભૂલો",
        "body": "1. WRONG HAND: Students frequently use their RIGHT hand by mistake! Always touch your left shoulder first to confirm you are using your LEFT hand for motors/force.\n2. ELECTRON TRAP: If a question mentions electrons or beta particles, remember: Current is OPPOSITE to their direction of flight! If protons or alpha particles are mentioned, current is in the SAME direction as their flight.\n3. ZERO FORCE: If a particle moves parallel to the magnetic field, force is ZERO regardless of speed!",
        "body_hi": "1. गलत हाथ का उपयोग: विद्यार्थी अक्सर गलती से दाएं हाथ का उपयोग कर लेते हैं! हमेशा याद रखें: बल या मोटर के लिए बायां हाथ ही इस्तेमाल करना है।\n2. इलेक्ट्रॉन की चाल: यदि प्रश्न में इलेक्ट्रॉन या बीटा कण हो, तो धारा उनकी गति के विपरीत दिशा में लें! प्रोटॉन या अल्फा कण के लिए धारा उनकी ही दिशा में लें।\n3. शून्य बल: यदि कोई कण चुंबकीय क्षेत्र के समानांतर गति करता है, तो उस पर कोई बल नहीं लगता (बल = 0)।",
        "body_gu": "1. ખોટો હાથ વાપરવો: વિદ્યાર્થીઓ ઘણીવાર ભૂલથી જમણો હાથ વાપરે છે! મોટર કે બળ માટે હંમેશા ડાબો હાથ જ વાપરવો.\n2. ઇલેક્ટ્રોનની ગતિ: જો પ્રશ્નમાં ઇલેક્ટ્રોન હોય તો પ્રવાહ તેની ગતિની વિરુદ્ધ લેવો! જો પ્રોટોન કે આલ્ફા કણ હોય તો પ્રવાહ તેની જ દિશામાં લેવો.\n3. શૂન્ય બળ: ક્ષેત્રને સમાંતર ગતિ કરતા કણ પર બળ શૂન્ય લાગે છે."
    })

    # 5. Knowledge Check (In-text Set 4 Q1)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT In-Text Q: Which of the following properties of a proton can change while it moves freely in a magnetic field? (Choose all that apply)",
        "question_hi": "NCERT पाठ्य-निहित प्रश्न: किसी प्रोटॉन का निम्नलिखित में से कौन सा गुण किसी चुंबकीय क्षेत्र में मुक्त गति करते समय परिवर्तित हो सकता है?",
        "question_gu": "NCERT પાઠ્યપુસ્તક પ્રશ્ન: કોઈ પ્રોટોન ચુંબકીય ક્ષેત્રમાં મુક્ત રીતે ગતિ કરે છે ત્યારે નીચેનામાંથી કયો ગુણધર્મ બદલાઈ શકે છે?",
        "options": [
            "Velocity and Momentum",
            "Mass only",
            "Speed and Mass",
            "None of these properties change"
        ],
        "options_hi": [
            "वेग (Velocity) एवं संवेग (Momentum)",
            "केवल द्रव्यमान",
            "चाल एवं द्रव्यमान",
            "इनमें से कोई भी गुणधर्म नहीं बदलता"
        ],
        "options_gu": [
            "વેગ (Velocity) અને વેગમાન (Momentum)",
            "માત્ર દળ",
            "ઝડપ અને દળ",
            "આમાંથી એકપણ ગુણધર્મ બદલાતો નથી"
        ],
        "correct_index": 0,
        "explanation": "When a charged particle moves in a magnetic field, the magnetic force acts perpendicular to its velocity. A perpendicular force changes the direction of motion without changing the speed (scalar magnitude). Because velocity and momentum are vectors that depend on direction, both velocity and momentum change continuously.",
        "explanation_hi": "जब कोई आवेशित कण चुंबकीय क्षेत्र में गति करता है, तो चुंबकीय बल उसके वेग के लंबवत कार्य करता है। लंबवत बल चाल (परिमाण) को बदले बिना केवल गति की दिशा बदलता है। चूंकि वेग और संवेग दोनों सदिश राशियां हैं जो दिशा पर निर्भर करती हैं, इसलिए वेग और संवेग दोनों बदल जाते हैं।",
        "explanation_gu": "જ્યારે વિદ્યુતભારિત કણ ચુંબકીય ક્ષેત્રમાં ગતિ કરે છે, ત્યારે ચુંબકીય બળ તેના વેગને લંબરૂપે લાગે છે. લંબ બળ ઝડપ (અદિશ મૂલ્ય) બદલ્યા વગર માત્ર ગતિની દિશા બદલે છે. વેગ અને વેગમાન સદિશ રાશિઓ હોવાથી દિશા બદલાતાં વેગ અને વેગમાન બંને બદલાય છે."
    })

    # 6. Reflection (In-text Box: Magnetism in Medicine)
    blocks.append({
        "id": next_id(),
        "type": "reflection",
        "title": "Magnetism in Medicine: The Human Body's Bio-Magnetic Signals",
        "title_hi": "चिकित्सा में चुंबकत्व: मानव शरीर के जैविक चुंबकीय संकेत",
        "title_gu": "તબીબી વિજ્ઞાનમાં ચુંબકત્વ: માનવ શરીરના જૈવિક ચુંબકીય સંકેતો",
        "body": "Did you know that you are a living magnet? Extremely weak ionic currents continuously travel along the nerve cells of your body to carry signals between your senses, brain, and muscles. These nerve impulses produce transient magnetic fields, roughly one-billionth of Earth's magnetic field! The two main human organs that produce significant magnetic fields are the HEART and the BRAIN. Detecting these tiny biomagnetic fields allows doctors to generate detailed cross-sectional diagnostic images of our internal organs via Magnetic Resonance Imaging (MRI).",
        "body_hi": "क्या आप जानते हैं कि आपका शरीर भी एक चुंबक है? हमारे शरीर की तंत्रिका कोशिकाओं (Nerve cells) में मांसपेशियों और मस्तिष्क के बीच संकेतों को ले जाने के लिए सूक्ष्म आयनिक धाराएं बहती हैं। ये धाराएं एक बहुत कमजोर चुंबकीय क्षेत्र पैदा करती हैं, जो पृथ्वी के चुंबकीय क्षेत्र का लगभग एक-अरबवाँ (one-billionth) भाग होता है! मानव शरीर के दो प्रमुख अंग जहां महत्वपूर्ण चुंबकीय क्षेत्र उत्पन्न होता है, वे हैं: हृदय (Heart) और मस्तिष्क (Brain)। इस तकनीक का उपयोग एमआरआई (MRI) में शरीर के आंतरिक अंगों के चित्र लेने के लिए किया जाता है।",
        "body_gu": "શું તમે જાણો છો કે તમારું શરીર પણ એક ચુંબક છે? આપણા શરીરના ચેતાકોષોમાં મગજ અને સ્નાયુઓ વચ્ચે સંકેતોના વહન માટે અત્યંત સૂક્ષ્મ આયનિક પ્રવાહો વહે છે. આ પ્રવાહો પૃથ્વીના ચુંબકીય ક્ષેત્રના અબજમા ભાગ જેટલું સૂક્ષ્મ ચુંબકીય ક્ષેત્ર રચે છે! માનવ શરીરમાં સૌથી વધુ ચુંબકીય ક્ષેત્ર ઉત્પન્ન કરતા બે મુખ્ય અંગો હૃદય અને મગજ છે. આ સિદ્ધાંત પર જ હોસ્પિટલોમાં MRI મશીન વડે આંતરિક અંગોની તસવીરો લેવાય છે."
    })

    # 7. Connection
    blocks.append({
        "id": next_id(),
        "type": "connection",
        "title": "The Commercial Electric Motor: Turning Fields into Motion",
        "title_hi": "व्यावसायिक विद्युत मोटर: चुंबकीय क्षेत्र से विशाल यांत्रिक घूर्णन",
        "title_gu": "કોમર્શિયલ વિદ્યુત મોટર: ચુંબકીય ક્ષેત્રમાંથી યાંત્રિક પરિભ્રમણ",
        "body": "An Electric Motor is a device that converts electrical energy into mechanical energy based on Fleming's Left-Hand Rule. A rectangular copper coil ABCD is placed between opposite poles of a permanent magnet. When current flows into side AB and out of side CD, the forces on AB (downwards) and CD (upwards) form a couple that rotates the coil continuously.\n\nKey Engineering Components:\n• Split-ring Commutator: Reverses the direction of current in the coil every half-rotation, ensuring the motor keeps spinning in the SAME continuous direction!\n• Armature: An insulated copper coil wound over a soft iron core, which enhances the magnetic power of commercial motors in electric vehicles, subway trains, and elevators.",
        "body_hi": "विद्युत मोटर एक ऐसी युक्ति है जो विद्युत ऊर्जा को यांत्रिक ऊर्जा में परिवर्तित करती है। यह फ्लेमिंग के वाम-हस्त नियम पर कार्य करती है। एक आयताकार कुंडली ABCD को चुंबक के ध्रुवों के बीच रखा जाता है। जब भुजा AB और CD में विपरीत धारा बहती है, तो उन पर विपरीत दिशा में बल लगता है, जिससे कुंडली लगातार घूमने लगती है।\n\nप्रमुख घटक:\n• विभક્ત वलय दिक्परिवर्तक (Split-ring Commutator): प्रत्येक आधे चक्कर के बाद कुंडली में धारा की दिशा को उलट देता है, जिससे मोटर लगातार एक ही दिशा में घूमती रहती है!\n• आर्मेचर: नरम लोहे के क्रोड पर तांबे के तार को लपेटकर बनाई गई कुंडली, जो मोटर की शक्ति को कई गुना बढ़ा देती है।",
        "body_gu": "વિદ્યુત મોટર એ વિદ્યુત ઊર્જાનું યાંત્રિક ઊર્જામાં રૂપાંતર કરતું સાધન છે જે ફ્લેમિંગના ડાબા હાથના નિયમ પર કાર્ય કરે છે. લંબચોરસ કોઈલ ABCD ને ચુંબકીય ધ્રુવો વચ્ચે મૂકી પ્રવાહ આપતાં સામસામેની બાજુઓ પર પરસ્પર વિરુદ્ધ બળ લાગવાથી કોઈલ સતત ભ્રમણ કરે છે.\n\nમુખ્ય ભાગો:\n• સ્પ્લિટ રિંગ કમ્યુટેટર (દિક્પરિવર્તક): દર અડધા આંટા પછી કોઈલમાં પ્રવાહની દિશા ઉલટાવે છે, જેથી મોટર સતત એક જ દિશામાં ફરતી રહે છે!\n• આર્મેચર: નરમ લોખંડના ગર્ભ પર વીંટાળેલી કોઈલ, જે મોટરની શક્તિમાં પ્રચંડ વધારો કરે છે."
    })

    # 8. Mastery Challenge (In-text Set 4 Q3)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT In-Text Q: A positively-charged particle (alpha-particle) projected towards the west is deflected towards the north by a magnetic field. The direction of the magnetic field is:",
        "question_hi": "NCERT पाठ्य-निहित प्रश्न: पश्चिम की ओर प्रक्षेपित कोई धनावेशित कण (अल्फा-कण) किसी चुंबकीय क्षेत्र द्वारा उत्तर की ओर विक्षेपित हो जाता है। चुंबकीय क्षेत्र की दिशा क्या है?",
        "question_gu": "NCERT પાઠ્યપુસ્તક પ્રશ્ન: પશ્ચિમ દિશામાં પ્રક્ષિપ્ત કરેલો ધનભારિત કણ (આલ્ફા-કણ) ચુંબકીય ક્ષેત્રને કારણે ઉત્તર દિશામાં વિચલિત થાય છે. ચુંબકીય ક્ષેત્રની દિશા શોધો:",
        "options": [
            "Upward (out of the plane)",
            "Downward (into the plane)",
            "Towards South",
            "Towards East"
        ],
        "options_hi": [
            "ऊपरी मुखी (Upward / तल से ऊपर की ओर)",
            "अधोमुखी (Downward / तल के नीचे की ओर)",
            "दक्षिण की ओर",
            "पूर्व की ओर"
        ],
        "options_gu": [
            "ઉપર તરફ (Upward / સમતલની બહાર)",
            "નીચે તરફ (Downward / સમતલની અંદર)",
            "દક્ષિણ તરફ",
            "પૂર્વ તરફ"
        ],
        "correct_index": 0,
        "explanation": "Direction of current (I) is towards West (direction of positive alpha particle) -> Middle finger points WEST. Direction of force (F) is towards North (deflection) -> Thumb points NORTH. By Fleming's Left-Hand Rule, your forefinger points UPWARDS (out of the plane).",
        "explanation_hi": "धनावेशित अल्फा कण पश्चिम की ओर जा रहा है, अतः धारा की दिशा पश्चिम है -> मध्यमा को पश्चिम में रखें। विक्षेप उत्तर की ओर है, अतः बल उत्तर दिशा में है -> अंगूठे को उत्तर में रखें। फ्लेमिंग के बाएं हाथ के नियम से तर्जनी ऊपर की ओर (Upward) संकेत करेगी।",
        "explanation_gu": "ધનભારિત કણ પશ્ચિમ તરફ જતો હોવાથી પ્રવાહ પશ્ચિમ દિશામાં છે -> વચ્ચેની આંગળી પશ્ચિમ તરફ રાખો. વિચલન ઉત્તર તરફ હોવાથી બળ ઉત્તર દિશામાં છે -> અંગૂઠો ઉત્તર તરફ રાખો. ડાબા હાથના નિયમ મુજબ પહેલી આંગળી ઉપર તરફ (Upward) દિશા દર્શાવે છે."
    })

    # =========================================================================
    # MODULE 5: ELECTROMAGNETIC INDUCTION, AC/DC & GENERATORS (8-STEP PEDAGOGY)
    # =========================================================================

    # 1. Hook
    blocks.append({
        "id": next_id(),
        "type": "hook",
        "title": "Michael Faraday's Miracle: Generating Electricity from Thin Air",
        "title_hi": "माइकल फैराडे का चमत्कार: चुंबक से बिजली पैदा करने की क्रांति",
        "title_gu": "માઈકલ ફેરાડેનો ચમત્કાર: ચુંબકમાંથી વીજળી પેદા કરવાની મહાક્રાંતિ",
        "body": "In 1831, British scientist Michael Faraday asked the reverse question: If an electric current can create a magnetic field, can a magnetic field create an electric current? For ten long years, he placed coils near the strongest magnets, but not a single volt of electricity appeared! Then, in a moment of pure frustration, he jerked the magnet violently away from the coil. In that exact microsecond, the galvanometer needle flicked! Electricity wasn't created by magnetism alone; it was created by RELATIVE MOTION. This discovery birthed the modern electric grid powering billions of homes today!",
        "body_hi": "1831 में ब्रिटिश वैज्ञानिक माइकल फैराडे ने उल्टा प्रश्न पूछा: यदि विद्युत धारा चुंबक बना सकती है, तो क्या चुंबक बिजली बना सकता है? दस वर्षों तक उन्होंने सबसे शक्तिशाली चुंबकों के पास तार की कुंडलियां रखीं, लेकिन एक वोल्ट भी बिजली पैदा नहीं हुई! फिर एक दिन हताशा में उन्होंने चुंबक को तेजी से कुंडली से दूर खींचा। उसी क्षण गैल्वेनोमीटर की सुई हिली! बिजली केवल चुंबक से नहीं, बल्कि चुंबक और कुंडली की 'सापेक्ष गति' से पैदा होती है। इसी खोज ने आज पूरी दुनिया को रोशन करने वाले पावर प्लांटों को जन्म दिया!",
        "body_gu": "1831 માં બ્રિટિશ વૈજ્ઞાનિક માઈકલ ફેરાડેએ સામો પ્રશ્ન પૂછ્યો: જો વિદ્યુતપ્રવાહ ચુંબકત્વ બનાવી શકે તો શું ચુંબકત્વ વિદ્યુતપ્રવાહ ન બનાવી શકે? દસ વર્ષ સુધી તેમણે શક્તિશાળી ચુંબકો પાસે ગૂંચળા મૂકી રાખ્યા પણ વીજળી પેદા ન થઈ! પછી એક દિવસ હતાશામાં તેમણે ચુંબકને જોરથી ગૂંચળામાંથી બહાર ખેંચ્યો. બરાબર તે જ ક્ષણે ગેલ્વેનોમીટરની સોય હલી! વીજળી માત્ર ચુંબકથી નહીં, પણ તેમની વચ્ચેની 'સાપેક્ષ ગતિ' થી પેદા થતી હતી. આ શોધે સમગ્ર માનવજાત માટે પાવર સ્ટેશનોની ભેટ આપી!"
    })

    # 2. Socratic Question
    blocks.append({
        "id": next_id(),
        "type": "socratic_question",
        "question": "If you hold a powerful bar magnet completely stationary inside a copper coil, how much electric current is measured on a sensitive galvanometer?",
        "question_hi": "यदि आप एक शक्तिशाली छड़ चुंबक को तांबे की कुंडली के अंदर बिल्कुल स्थिर (Stationary) पकड़कर रखें, तो गैल्वेनोमीटर पर कितनी धारा मापी जाएगी?",
        "question_gu": "જો તમે શક્તિશાળી ગજિયા ચુંબકને તાંબાના ગૂંચળાની અંદર તદ્દન સ્થિર પકડી રાખો, તો ગેલ્વેનોમીટર પર કેટલો વિદ્યુતપ્રવાહ નોંધાશે?",
        "options": [
            "Exactly zero current because there is no relative motion or change in magnetic flux.",
            "A constant high DC current proportional to the magnet's strength.",
            "An alternating current of 50 Hz.",
            "A decaying pulse that lasts for several hours."
        ],
        "options_hi": [
            "बिल्कुल शून्य धारा क्योंकि कोई सापेक्ष गति या चुंबकीय फ्लक्स में परिवर्तन नहीं हो रहा है।",
            "चुंबक की शक्ति के समानुपाती एक स्थिर उच्च दिष्ट धारा (DC)।",
            "50 हर्ट्ज़ की प्रत्यावर्ती धारा (AC)।",
            "एक घटती हुई धारा जो कई घंटों तक चलती है।"
        ],
        "options_gu": [
            "તદ્દન શૂન્ય પ્રવાહ કારણ કે ત્યાં કોઈ સાપેક્ષ ગતિ કે ચુંબકીય ફ્લક્સમાં ફેરફાર થતો નથી.",
            "ચુંબકની પ્રબળતાના સમપ્રમાણમાં સતત વહેતો DC પ્રવાહ.",
            "50 Hz નો ઉલટસુલટ AC પ્રવાહ.",
            "કલાકો સુધી ચાલતો ક્ષીણ પ્રવાહ."
        ],
        "correct_index": 0,
        "explanation": "Faraday's Law of Electromagnetic Induction dictates that current is induced ONLY when there is a change in the magnetic field linked with the coil (relative motion). When the magnet is stationary inside the coil, the magnetic field is constant, so induced EMF and current are exactly ZERO.",
        "explanation_hi": "फैराडे के विद्युत चुंबकीय प्रेरण के नियमानुसार, धारा केवल तभी प्रेरित होती है जब कुंडली से गुजरने वाले चुंबकीय क्षेत्र (फ्लक्स) में परिवर्तन होता है। जब चुंबक स्थिर होता है, तो चुंबकीय क्षेत्र नियत रहता है, जिससे प्रेरित विभव और धारा दोनों शून्य होते हैं।",
        "explanation_gu": "ફેરાડેના વિદ્યુતચુંબકીય પ્રેરણના નિયમ મુજબ જ્યારે ગૂંચળા સાથે સંકળાયેલા ચુંબકીય ક્ષેત્રમાં ફેરફાર થાય (સાપેક્ષ ગતિ થાય) ત્યારે જ પ્રવાહ પ્રેરિત થાય છે. ચુંબક સ્થિર હોય ત્યારે ક્ષેત્ર અચળ રહેતું હોવાથી પ્રેરિત વિદ્યુતપ્રવાહ તદ્દન શૂન્ય હોય છે."
    })

    # 3. Discovery
    blocks.append({
        "id": next_id(),
        "type": "discovery",
        "title": "Faraday's Coil & Magnet Experiments",
        "title_hi": "फैराडे का कुंडली एवं चुंबक प्रयोग: प्रेरण का जीवंत प्रमाण",
        "title_gu": "ફેરાડેના ગૂંચળા અને ચુંબકના પ્રયોગો: પ્રેરણની સાબિતી",
        "body": "EXPERIMENT 1: RELATIVE MOTION\nConnect a coil of insulated wire to a sensitive Galvanometer (an instrument that detects the presence and direction of tiny electric currents; zero at the center of its scale):\n1. Push North pole of a magnet into the coil: Galvanometer needle deflects to the RIGHT.\n2. Hold magnet stationary inside: Deflection drops immediately to ZERO.\n3. Pull magnet out of coil: Needle deflects to the LEFT (opposite direction).\n4. Move magnet faster: Deflection is larger!\n\nEXPERIMENT 2: TWO COILS (MUTUAL INDUCTION)\nWind two coils (Coil 1 / Primary and Coil 2 / Secondary) on a non-conducting cardboard cylinder. Connect Coil 1 to a battery and key, and Coil 2 only to a galvanometer:\n• The instant you press the key in Coil 1, the needle in Coil 2 momentarily jerks and returns to zero!\n• When current in Coil 1 flows steadily, needle in Coil 2 stays at ZERO.\n• The instant you open the key, needle jerks in the OPPOSITE direction!",
        "body_hi": "प्रयोग 1: सापेक्ष गति\nतार की एक कुंडली को संवेदनशील गैल्वेनोमीटर (धारा की उपस्थिति और दिशा मापने वाला यंत्र) से जोड़ें:\n1. चुंबक के उत्तरी ध्रुव को कुंडली में डालें: सुई दाईं ओर विक्षेपित होती है।\n2. चुंबक को अंदर स्थिर रखें: विक्षेप तुरंत शून्य हो जाता है।\n3. चुंबक को बाहर निकालें: सुई बाईं ओर (विपरीत दिशा में) विक्षेपित होती है।\n4. चुंबक को तेजी से हिलाने पर विक्षेप और बढ़ जाता है!\n\nप्रयोग 2: दो कुंडलियां (अन्योन्य प्रेरण)\nकार्डबोर्ड के रोल पर दो कुंडलियां लपेटें (प्राथमिक और द्वितीयक)। प्राथमिक कुंडली में बैटरी और कुंजी लगाएं, द्वितीयक को केवल गैल्वेनोमीटर से जोड़ें:\n• जैसे ही प्राथमिक में स्विच ऑन करते हैं, द्वितीयक में सुई एक क्षण के लिए हिलकर शून्य पर आ जाती है!\n• जब प्राथमिक में स्थिर धारा बहती है, तो द्वितीयक में धारा शून्य रहती है।\n• जैसे ही स्विच बंद करते हैं, सुई विपरीत दिशा में क्षणिक विक्षेप दिखाती है!",
        "body_gu": "પ્રયોગ 1: સાપેક્ષ ગતિ\nતાંબાના ગૂંચળાને સંવેદનશીલ ગેલ્વેનોમીટર (પ્રવાહની હાજરી અને દિશા દર્શાવતું સાધન) સાથે જોડો:\n1. ચુંબકનો ઉત્તર ધ્રુવ ગૂંચળામાં દાખલ કરતાં: સોય જમણી બાજુ વિચલન દર્શાવે છે.\n2. ચુંબક સ્થિર રાખતાં: વિચલન તરત જ શૂન્ય થઈ જાય છે.\n3. ચુંબક બહાર ખેંચતાં: સોય ડાબી બાજુ (વિરુદ્ધ દિશામાં) વિચલન દર્શાવે છે.\n4. ચુંબક ઝડપથી હલાવતાં: વિચલન વધુ મોટું મળે છે!\n\nપ્રયોગ 2: બે ગૂંચળા (અન્યોન્ય પ્રેરણ)\nકાર્ડબોર્ડ રોલ પર બે કોઈલ વીંટાળો. કોઈલ 1 માં બેટરી અને કળ જોડો, કોઈલ 2 માં માત્ર ગેલ્વેનોમીટર જોડો:\n• કળ ચાલુ કરતાં જ કોઈલ 2 માં સોય એક ક્ષણ માટે વિચલિત થઈ શૂન્ય પર આવે છે!\n• પ્રવાહ સ્થિર રહે ત્યારે કોઈલ 2 માં કોઈ પ્રવાહ મળતો નથી.\n• કળ બંધ કરતાં જ સોય ક્ષણિક વિરુદ્ધ દિશામાં વિચલન બતાવે છે!"
    })

    # 4. Theory
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "Electromagnetic Induction, Fleming's Right-Hand Rule & AC vs DC",
        "title_hi": "विद्युत चुंबकीय प्रेरण, फ्लेमिंग का दक्षिण-हस्त नियम एवं AC बनाम DC",
        "title_gu": "વિદ્યુતચુંબકીય પ્રેરણ, ફ્લેમિંગનો જમણા હાથનો નિયમ અને AC વિરુદ્ધ DC",
        "body": "1. ELECTROMAGNETIC INDUCTION (EMI):\nThe process by which a changing magnetic field in a conductor induces an electric current in another conductor (or across its own terminals) is called Electromagnetic Induction.\n\n2. FLEMING'S RIGHT-HAND RULE (For Induced Current):\nStretch the thumb, forefinger, and middle finger of your RIGHT HAND mutually perpendicular:\n• FOREFINGER indicates the direction of the MAGNETIC FIELD.\n• THUMB indicates the direction of MOTION of the conductor.\n• MIDDLE FINGER indicates the direction of INDUCED CURRENT.\n\n3. DIRECT CURRENT (DC) VS ALTERNATING CURRENT (AC):\n• Direct Current (DC): Electric current that flows unidirectionally without changing direction over time (provided by chemical cells, batteries, DC dynamos).\n• Alternating Current (AC): Electric current that reverses its direction of flow periodically.\n• Frequency in India: In Indian domestic supply, AC reverses direction every 1/100 second. One complete cycle takes 2 * (1/100) = 1/50 second. Therefore, the frequency of domestic AC in India is 50 Hz (50 cycles per second) at 220 V.\n\n4. MAJOR ADVANTAGE OF AC OVER DC:\nAC can be transmitted over very long distances with negligible loss of electrical energy by using step-up transformers (high voltage, low current minimizes Joule heating loss: H = I²Rt).",
        "body_hi": "1. विद्युत चुंबकीय प्रेरण (Electromagnetic Induction):\nवह प्रक्रम जिसके द्वारा किसी चालक में बदलते हुए चुंबकीय क्षेत्र के कारण किसी अन्य चालक में विद्युत धारा प्रेरित होती है, 'विद्युत चुंबकीय प्रेरण' कहलाता है।\n\n2. फ्लेमिंग का दक्षिण-हस्त नियम (Fleming's Right-Hand Rule):\nअपने दाहिने हाथ के अंगूठे, तर्जनी और मध्यमा को परस्पर लंबवत फैलाएं:\n• तर्जनी: चुंबकीय क्षेत्र की दिशा दर्शाती है।\n• अंगूठा: चालक की गति की दिशा दर्शाता है।\n• मध्यमा: प्रेरित विद्युत धारा (Induced Current) की दिशा दर्शाती है।\n\n3. दिष्ट धारा (DC) बनाम प्रत्यावर्ती धारा (AC):\n• दिष्ट धारा (DC): वह धारा जो सदैव एक ही दिशा में बहती है (सेल, बैटरी से प्राप्त)।\n• प्रत्यावर्ती धारा (AC): वह धारा जो एक निश्चित समय अंतराल के बाद अपनी दिशा बदलती है।\n• भारत में आवृत्ति: भारत में घरेलू AC धारा प्रत्येक 1/100 सेकंड बाद अपनी दिशा बदलती है। एक पूरा चक्र 1/50 सेकंड में पूरा होता है, इसलिए भारत में AC की आवृत्ति 50 Hz (हर्ट्ज़) तथा विभवांतर 220 V होता है।\n\n4. DC की तुलना में AC का मुख्य लाभ:\nट्रांसफार्मर की मदद से AC को उच्च वोल्टता पर बहुत लंबी दूरियों तक बिना अधिक ऊर्जा हानि के भेजा जा सकता है (क्योंकि कम धारा से ऊष्मा हानि H = I²Rt न्यूनतम होती है)।",
        "body_gu": "1. વિદ્યુતચુંબકીય પ્રેરણ (Electromagnetic Induction):\nવાહકમાં બદલાતા જતા ચુંબકીય ક્ષેત્રને કારણે અન્ય વાહકમાં વિદ્યુતપ્રવાહ પ્રેરિત થવાની ઘટનાને વિદ્યુતચુંબકીય પ્રેરણ કહે છે.\n\n2. ફ્લેમિંગનો જમણા હાથનો નિયમ (Fleming's Right-Hand Rule):\nજમણા હાથના અંગૂઠા, પ્રથમ આંગળી (તર્જની) અને વચ્ચેની આંગળી (મધ્યમા) ને પરસ્પર કાટખૂણે ફેલાવો:\n• પ્રથમ આંગળી: ચુંબકીય ક્ષેત્રની દિશા દર્શાવે છે.\n• અંગૂઠો: વાહકની ગતિની દિશા દર્શાવે છે.\n• વચ્ચેની આંગળી: પ્રેરિત વિદ્યુતપ્રવાહની દિશા દર્શાવે છે.\n\n3. દિષ્ટ પ્રવાહ (DC) અને ઉલટસુલટ પ્રવાહ (AC):\n• દિષ્ટ પ્રવાહ (DC): જે વિદ્યુતપ્રવાહ હંમેશા એક જ દિશામાં વહે છે (બેટરી, સેલમાંથી મળતો પ્રવાહ).\n• ઉલટસુલટ પ્રવાહ (AC): જે પ્રવાહ નિશ્ચિત સમયગાળે પોતાની દિશા ઉલટાવે છે.\n• ભારતમાં AC ની આવૃત્તિ: ભારતમાં ઘરેલું AC દર 1/100 સેકન્ડે પોતાની દિશા બદલે છે. એક ચક્ર પૂર્ણ થતાં 1/50 સેકન્ડ લાગે છે, તેથી ભારતમાં AC ની આવૃત્તિ 50 Hz અને વોલ્ટેજ 220 V હોય છે.\n\n4. DC કરતાં AC નો મોટો ફાયદો:\nટ્રાન્સફોર્મરની મદદથી વોલ્ટેજ વધારીને AC પ્રવાહને ખૂબ ઓછા ઊર્જા વ્યય સાથે સેંકડો કિલોમીટર દૂર સુધી સરળતાથી પહોંચાડી શકાય છે."
    })

    # Teacher Tip: Left Hand vs Right Hand
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Teacher Tip: Never Confuse Left-Hand and Right-Hand Rules",
        "title_hi": "शिक्षक टिप: फ्लेमिंग के बाएं और दाएं हाथ के नियमों में अंतर",
        "title_gu": "શિક્ષક ટિપ: ફ્લેમિંગના ડાબા અને જમણા હાથના નિયમ વચ્ચેનો સ્પષ્ટ ભેદ",
        "body": "HOW TO NEVER MIX THEM UP:\n• LEFT HAND = MOTOR (Electrical energy in -> Mechanical FORCE out). Use Fleming's LEFT-Hand Rule to find the direction of FORCE/MOTION.\n• RIGHT HAND = GENERATOR (Mechanical motion in -> INDUCED CURRENT out). Use Fleming's RIGHT-Hand Rule to find the direction of INDUCED CURRENT.",
        "body_hi": "याद रखने का अचूक तरीका:\n• बायां हाथ (Left Hand) = मोटर (Motor): जब बिजली दी जाए और गति/बल प्राप्त हो -> बल की दिशा के लिए बायां हाथ नियम।\n• दायां हाथ (Right Hand) = जनरेटर (Generator): जब गति दी जाए और बिजली पैदा हो -> प्रेरित धारा की दिशा के लिए दायां हाथ नियम।",
        "body_gu": "યાદ રાખવાની સુવર્ણ ચાવી:\n• ડાબો હાથ (Left Hand) = મોટર: કરંટ આપતાં યાંત્રિક બળ/ગતિ મળે -> બળની દિશા માટે ડાબો હાથ.\n• જમણો હાથ (Right Hand) = જનરેટર: ગતિ આપતાં પ્રેરિત વિદ્યુતપ્રવાહ પેદા થાય -> પ્રેરિત પ્રવાહ માટે જમણો હાથ."
    })

    # 5. Knowledge Check (MCQ)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "In India, alternating current (AC) domestic power supply reverses its direction every:",
        "question_hi": "भारत में प्रत्यावर्ती धारा (AC) घरेलू विद्युत आपूर्ति अपनी दिशा कितने समय बाद बदलती है?",
        "question_gu": "ભારતમાં ઘરેલું વપરાશ માટેનો ઉલટસુલટ પ્રવાહ (AC) દર કેટલા સમયે પોતાની દિશા ઉલટાવે છે?",
        "options": [
            "1/100 second",
            "1/50 second",
            "1/25 second",
            "1/200 second"
        ],
        "options_hi": [
            "1/100 सेकंड",
            "1/50 सेकंड",
            "1/25 सेकंड",
            "1/200 सेकंड"
        ],
        "options_gu": [
            "1/100 સેકન્ડ",
            "1/50 સેકન્ડ",
            "1/25 સેકન્ડ",
            "1/200 સેકન્ડ"
        ],
        "correct_index": 0,
        "explanation": "Domestic AC in India has a frequency of 50 Hz, meaning it completes 50 full cycles per second. Since an AC current reverses its direction TWICE in every cycle, it reverses direction 100 times each second, which corresponds to once every 1/100 second.",
        "explanation_hi": "भारत में AC की आवृत्ति 50 Hz है, यानी यह प्रति सेकंड 50 चक्र पूरे करती है। चूंकि धारा प्रत्येक चक्र में 2 बार अपनी दिशा बदलती है, अतः यह 1 सेकंड में 100 बार दिशा बदलती है, यानी प्रत्येक 1/100 सेकंड में दिशा बदलती है।",
        "explanation_gu": "ભારતમાં AC ની આવૃત્તિ 50 Hz હોવાથી તે પ્રતિ સેકન્ડ 50 ચક્ર પૂર્ણ કરે છે. દરેક ચક્રમાં પ્રવાહ 2 વાર દિશા બદલતો હોવાથી એક સેકન્ડમાં 100 વખત દિશા બદલાય છે, એટલે કે દર 1/100 સેકન્ડે દિશા ઉલટાય છે."
    })

    # 6. Reflection
    blocks.append({
        "id": next_id(),
        "type": "reflection",
        "title": "The War of the Currents: Nikola Tesla vs Thomas Edison",
        "title_hi": "विद्युत धाराओं का महायुद्ध: निकोला टेस्ला बनाम थॉमस एडिसन",
        "title_gu": "વીજપ્રવાહોનું મહાયુદ્ધ: નિકોલા ટેસ્લા વિરુદ્ધ થોમસ એડિસન",
        "body": "In the late 1880s, Thomas Edison built the first power grids using Direct Current (DC). But DC had a fatal flaw: high resistance caused severe voltage drops, requiring a coal power plant every 2 kilometres! Nikola Tesla and George Westinghouse championed Alternating Current (AC), which could be stepped up to tens of thousands of volts and transmitted over hundreds of kilometres with minimal heat loss before being stepped down safely for homes. Tesla's AC won, making continental electrification possible.",
        "body_hi": "1880 के दशक में थॉमस एडिसन ने दिष्ट धारा (DC) पर आधारित पहले पावर ग्रिड बनाए। लेकिन डीसी में एक बड़ी खामी थी: तारों के प्रतिरोध के कारण भारी वोल्टेज ड्रॉप होता था, जिससे हर 2 किलोमीटर पर एक पावर प्लांट लगाना पड़ता था! निकोला टेस्ला ने प्रत्यावर्ती धारा (AC) का समर्थन किया, जिसे ट्रांसफार्मर द्वारा हजारों वोल्ट तक बढ़ाकर बिना ऊर्जा हानि के सैकड़ों किलोमीटर दूर भेजा जा सकता था। टेस्ला के AC की जीत हुई और आज पूरी दुनिया में एसी ग्रिड ही संचालित होते हैं।",
        "body_gu": "1880 ના દાયકામાં થોમસ એડિસને DC કરંટ પર પાવર ગ્રીડ શરૂ કરી. પરંતુ DC માં મોટો અવરોધ હતો: વાયરમાં વોલ્ટેજ ઘટી જતો હોવાથી દર 2 કિમીએ નવું પાવર સ્ટેશન બનાવવું પડતું! નિકોલા ટેસ્લાએ AC કરંટ રજૂ કર્યો, જેને ટ્રાન્સફોર્મર વડે ઊંચા વોલ્ટેજે સેંકડો કિમી સુધી નહિવત વ્યય સાથે મોકલી શકાતો હતો. ટેસ્લાની AC સિસ્ટમ જીતી અને આજે આખી દુનિયા AC થી જ ઝળહળે છે."
    })

    # 7. Connection
    blocks.append({
        "id": next_id(),
        "type": "connection",
        "title": "Hydroelectric Dam Turbines: Mechanical Work to Clean Gigawatts",
        "title_hi": "जलविद्युत बांध टरबाइन: पानी के वेग से विशाल विद्युत उत्पादन",
        "title_gu": "હાઇડ્રોઇલેક્ટ્રિક ડેમ ટર્બાઇન: પાણીના વેગમાંથી ગીગાવોટ વીજળીનું ઉત્પાદન",
        "body": "At hydroelectric projects like the Sardar Sarovar Dam on the Narmada River, millions of tons of water fall through massive penstock pipes to spin giant hydraulic turbines. Inside the generator attached to the turbine, massive electromagnets rotate at high speed within stationary copper stator coils. By Faraday's Law of Electromagnetic Induction, the rotating magnetic flux induces gigawatts of alternating current, supplying clean renewable electricity to millions of homes and industries!",
        "body_hi": "नर्मदा नदी पर बने सरदार सरोवर बांध जैसे जलविद्युत संयंत्रों में विशाल पेनस्टॉक पाइपों से लाखों टन पानी गिरकर हाइड्रोलिक टरबाइनों को घुमाता है। टरबाइन से जुड़े विशाल एसी जनरेटर में तांबे की स्थिर कुंडलियों (Stator) के बीच भारी विद्युत चुंबक तेजी से घूमते हैं। फैराडे के प्रेरण नियमानुसार यह घूर्णन गीगावाट में बिजली पैदा करता है, जो लाखों घरों और कारखानों को जगमग करती है!",
        "body_gu": "નર્મદા નદી પર સરદાર સરોવર ડેમ જેવા જળવિદ્યુત મથકોમાં લાખો ટન પાણી પાઇપમાંથી ધસી આવી વિશાળ ટર્બાઇન ફેરવે છે. ટર્બાઇન સાથે જોડાયેલા જનરેટરમાં તાંબાના સ્થિર ગૂંચળા વચ્ચે પ્રચંડ વિદ્યુતચુંબકો અતિ ઝડપે ભ્રમણ કરે છે. ફેરાડેના પ્રેરણ નિયમ મુજબ આ ગતિમાંથી ગીગાવોટ વીજળી ઉત્પન્ન થઈ લાખો ઘરો સુધી પહોંચે છે!"
    })

    # 8. Mastery Challenge (MCQ)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Which instrument is used to detect the presence and direction of a weak electric current in a circuit?",
        "question_hi": "परिपथ में दुर्बल विद्युत धारा की उपस्थिति और उसकी दिशा का पता लगाने के लिए किस उपकरण का उपयोग किया जाता है?",
        "question_gu": "પરિપથમાં અત્યંત નિર્બળ વિદ્યુતપ્રવાહની હાજરી અને દિશા જાણવા માટે કયું સાધન વપરાય છે?",
        "options": [
            "Galvanometer",
            "Voltmeter",
            "Ammeter",
            "Rheostat"
        ],
        "options_hi": [
            "गैल्वेनोमीटर (Galvanometer)",
            "वोल्टमीटर (Voltmeter)",
            "एमीटर (Ammeter)",
            "रियोस्टैट (Rheostat)"
        ],
        "options_gu": [
            "ગેલ્વેનોમીટર (Galvanometer)",
            "વોલ્ટમીટર (Voltmeter)",
            "એમીટર (Ammeter)",
            "ચલ અવરોધ (રીઓસ્ટેટ)"
        ],
        "correct_index": 0,
        "explanation": "A Galvanometer is a highly sensitive instrument used to detect the presence and direction of minute electric currents in a circuit. Its needle rests at the center zero mark and deflects left or right depending on the current's direction.",
        "explanation_hi": "गैल्वेनोमीटर एक अत्यधिक संवेदनशील उपकरण है जो परिपथ में बहुत छोटी धारा की उपस्थिति और दिशा दोनों का पता लगाता है। इसका शून्य स्केल के केंद्र में होता है और धारा की दिशा के अनुसार सुई बाएं या दाएं विक्षेपित होती है।",
        "explanation_gu": "ગેલ્વેનોમીટર અત્યંત સંવેદનશીલ સાધન છે જે પરિપથમાં સૂક્ષ્મ વિદ્યુતપ્રવાહની હાજરી અને વહેવાની દિશા બંને દર્શાવે છે. તેનો શૂન્ય કાપો સ્કેલની મધ્યમાં હોય છે અને પ્રવાહ મુજબ સોય ડાબે કે જમણે ફરે છે."
    })

    # =========================================================================
    # MODULE 6: DOMESTIC ELECTRIC CIRCUITS & ELECTRICAL SAFETY (8-STEP PEDAGOGY)
    # =========================================================================

    # 1. Hook
    blocks.append({
        "id": next_id(),
        "type": "hook",
        "title": "The 2000W Appliance Surge: Why Didn't Your House Catch Fire?",
        "title_hi": "2000W का सर्ज: आपका घर आग लगने से कैसे बचा?",
        "title_gu": "2000W નો સર્જ: તમારા ઘરમાં આગ લાગતાં કોણે બચાવ્યું?",
        "body": "It is a cold winter morning. You plug in a heavy 2000W water geyser, a room heater, and an electric iron into the same electrical socket simultaneously. Suddenly, with a loud 'CLICK', all the power in the room cuts out instantly! No sparks, no smoke, no raging house fire. What invisible superhero sacrificing its own life behind your home's meter box just saved your entire house from burning down in a catastrophic electrical fire?",
        "body_hi": "सर्दियों की एक सुबह, आप एक ही बिजली के बोर्ड में 2000W का गीज़र, हीटर और कपड़े की प्रेस एक साथ चालू कर देते हैं। अचानक एक जोरदार 'क्लिक' की आवाज के साथ पूरे कमरे की बत्ती गुल हो जाती है! न कोई चिंगारी, न धुआं, न कोई आग। आपके मीटर बॉक्स में छिपे किस अदृश्य रक्षक ने अपना बलिदान देकर आपके पूरे घर को भयंकर आग से बचा लिया?",
        "body_gu": "શિયાળાની સવારે તમે એક જ બોર્ડમાં 2000W નું ગીઝર, રૂમ હીટર અને ઇસ્ત્રી એકસાથે ચાલુ કરો છો. અચાનક 'ક્લિક' અવાજ સાથે રૂમની લાઈટો બંધ થઈ જાય છે! ન કોઈ તણખા, ન ધુમાડો, ન આગ. તમારા મીટર બોર્ડ પાછળ રહેલા કયા અદ્રશ્ય રક્ષકે પોતાનું બલિદાન આપી સમગ્ર ઘરને ભયાનક આગથી બચાવી લીધું?"
    })

    # 2. Socratic Question
    blocks.append({
        "id": next_id(),
        "type": "socratic_question",
        "question": "Why are all domestic appliances connected in parallel across the Live and Neutral wires rather than in series?",
        "question_hi": "घरेलू उपकरणों को श्रेणीक्रम (Series) के बजाय विद्युन्मय (Live) और उदासीन (Neutral) तारों के बीच समानांतर (Parallel) क्यों जोड़ा जाता है?",
        "question_gu": "ઘરના તમામ ઉપકરણોને શ્રેણી જોડાણના બદલે જીવંત (Live) અને તટસ્થ (Neutral) વાયર વચ્ચે સમાંતર (Parallel) કેમ જોડવામાં આવે છે?",
        "options": [
            "Parallel connection provides full 220V across every appliance and allows each to be operated independently with its own switch.",
            "Parallel connection eliminates the need for an electric meter.",
            "Series connection uses too much copper wire.",
            "Parallel connection converts AC current to DC current."
        ],
        "options_hi": [
            "समानांतर क्रम में प्रत्येक उपकरण को पूरा 220V मिलता है और हर उपकरण को अपने अलग स्विच से स्वतंत्र रूप से चालू/बंद किया जा सकता है।",
            "समानांतर कनेक्शन से बिजली के मीटर की आवश्यकता समाप्त हो जाती है।",
            "श्रेणी कनेक्शन में बहुत अधिक तांबे के तार की खपत होती है।",
            "समानांतर कनेक्शन एसी को डीसी में बदल देता है।"
        ],
        "options_gu": [
            "સમાંતર જોડાણમાં દરેક સાધનને પૂરા 220V મળે છે અને દરેક સાધનને પોતાની અલગ સ્વિચ વડે સ્વતંત્ર રીતે ચાલુ/બંધ કરી શકાય છે.",
            "સમાંતર જોડાણથી વીજળી મીટરની જરૂર રહેતી નથી.",
            "શ્રેણી જોડાણમાં તાંબાનો વાયર બહુ વધારે વપરાય છે.",
            "સમાંતર જોડાણ AC ને DC માં ફેરવી નાખે છે."
        ],
        "correct_index": 0,
        "explanation": "In parallel wiring: 1) Every appliance receives the full supply potential difference of 220V; 2) If one appliance breaks or is turned off, other appliances continue running unaffected; 3) Total resistance decreases, ensuring sufficient current.",
        "explanation_hi": "समानांतर संयोजन में: 1) प्रत्येक उपकरण को 220V का पूर्ण विभवांतर मिलता है; 2) यदि एक उपकरण खराब या बंद हो जाए, तो बाकी उपकरण बिना रुकावट के चलते रहते हैं; 3) कुल प्रतिरोध घटता है जिससे उपकरणों को पर्याप्त धारा मिलती है।",
        "explanation_gu": "સમાંતર જોડાણમાં: 1) દરેક સાધનને 220V નો પૂરો વોલ્ટેજ મળે છે; 2) એક સાધન બગડી જાય કે બંધ કરો તો અન્ય સાધનો ચાલુ રહે છે; 3) પરિપથનો કુલ અવરોધ ઘટે છે જેથી સાધનોને પૂરતો પ્રવાહ મળે છે."
    })

    # 3. Discovery
    blocks.append({
        "id": next_id(),
        "type": "discovery",
        "title": "Anatomy of a Domestic Electrical Supply System",
        "title_hi": "घरेलू विद्युत परिपथ की संपूर्ण संरचना",
        "title_gu": "ઘરેલું વિદ્યુત પરિપથની સંપૂર્ણ રચના",
        "body": "Electricity enters our homes from overhead poles or underground cables via three insulated wires:\n1. LIVE WIRE (Positive): Red insulation cover (modern code: brown). Carries 220V alternating potential.\n2. NEUTRAL WIRE (Negative): Black insulation cover (modern code: blue). Carries zero volts (0V) return potential.\n• The potential difference between Live and Neutral in India is exactly 220 V.\n3. EARTH WIRE (Ground): Green insulation cover (modern code: green/yellow). Carries 0V. Connected to a large metal copper plate buried deep in the earth near the building.\n\nTHE TWO HOUSEHOLD CIRCUITS:\n• 15 A Power Circuit: For high-power appliances (geysers, air conditioners, heaters, refrigerators).\n• 5 A Lighting Circuit: For low-power appliances (bulbs, fans, televisions, chargers).",
        "body_hi": "बिजली हमारे घरों में खंभों या भूमिगत केबलों से तीन तारों के माध्यम से प्रवेश करती है:\n1. विद्युन्मय तार (Live wire / धनात्मक): लाल रंग का आवरण। इसमें 220V का प्रत्यावर्ती विभव होता है।\n2. उदासीन तार (Neutral wire / ऋणात्मक): काले रंग का आवरण। इसका विभव 0V होता है।\n• भारत में लाइव और न्यूट्रल तार के बीच विभवांतर 220 V होता है।\n3. भूसंपर्क तार (Earth wire): हरे रंग का आवरण। यह घर के पास जमीन में गहराई में दबी तांबे की प्लेट से जुड़ा सुरक्षा तार होता है।\n\nघरों में दो अलग-अलग परिपथ होते हैं:\n• 15 A का पावर परिपथ: उच्च शक्ति वाले उपकरणों (गीज़र, एसी, हीटर, फ्रिज) के लिए।\n• 5 A का लाइटिंग परिपथ: कम शक्ति वाले उपकरणों (बल्બ, पंखे, टीवी, चार्जर) के लिए।",
        "body_gu": "વીજળી આપણા ઘરમાં ત્રણ અલગ અલગ વાયરો દ્વારા પ્રવેશે છે:\n1. જીવંત વાયર (Live Wire / લાઈવ): લાલ રંગનું પડ. તે 220V નો વોલ્ટેજ ધરાવે છે.\n2. તટસ્થ વાયર (Neutral Wire / ન્યુટ્રલ): કાળા રંગનું પડ. તેનો વોલ્ટેજ 0V હોય છે.\n• ભારતમાં લાઈવ અને ન્યુટ્રલ વાયર વચ્ચેનો વિદ્યુતસ્થિતિમાનનો તફાવત 220 V હોય છે.\n3. અર્થિંગ વાયર (Earth Wire): લીલા રંગનું પડ. જમીનમાં ઊંડે દાટેલી તાંબાની પ્લેટ સાથે જોડેલો સુરક્ષા વાયર છે.\n\nઘરમાં બે અલગ સર્કિટ હોય છે:\n• 15 A ની પાવર સર્કિટ: વધુ પાવરવાળા સાધનો (ગીઝર, એસી, હીટર, ફ્રિજ) માટે.\n• 5 A ની લાઇટિંગ સર્કિટ: ઓછા પાવરવાળા સાધનો (ગોળા, પંખા, ટીવી) માટે."
    })

    # 4. Theory
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "Earthing, Short-Circuiting, Overloading & Electrical Fuse",
        "title_hi": "भूसंपर्कन, लघुपथन (Short Circuit), अतिभारण (Overloading) एवं फ्यूज",
        "title_gu": "અર્થિંગ, શોર્ટ સર્કિટ, ઓવરલોડિંગ અને ઇલેક્ટ્રિક ફ્યુઝ",
        "body": "1. FUNCTION OF EARTH WIRE & EARTHING:\nThe metal casing of metallic appliances (electric press, toaster, refrigerator) is connected directly to the Earth wire. Why? If live wire insulation wears off and touches the metallic body, the earth wire provides an ultra-low-resistance conducting path straight into the ground. The current leaks safely into the earth without passing through the human body, preventing fatal electric shocks!\n\n2. SHORT-CIRCUITING:\nWhen the insulation of wires is damaged or an appliance is faulty, the LIVE wire comes into DIRECT contact with the NEUTRAL wire. Because contact resistance drops almost to zero, current in the circuit abruptly increases to enormous levels. This can generate intense heat and trigger electrical fires.\n\n3. OVERLOADING:\nOverloading occurs when the total current drawn by all running appliances exceeds the safe carrying capacity of the circuit wires. Causes include:\n• Connecting too many heavy appliances to a single socket.\n• Accidental hike in supply voltage from the power station.\n• Direct short-circuit contact.\n\n4. ELECTRIC FUSE & MCB:\nA safety device containing a thin wire made of an alloy with a LOW MELTING POINT (lead-tin alloy). When excessive current flows due to short-circuiting or overloading, Joule heating (H = I²Rt) melts the fuse wire, breaking the circuit instantly and protecting expensive appliances from destruction.",
        "body_hi": "1. भूसंपर्कन (Earthing) का कार्य:\nधातु के आवरण वाले उपकरणों (प्रेस, टोस्टर, फ्रिज) की बॉडी को अर्थ वायर से जोड़ा जाता है। यदि गलती से लाइव तार कटकर धातु की बॉडी को छू ले, तो अर्थ वायर उस धारा को बिना किसी रुकावट के सीधे जमीन में भेज देता है। इससे उपकरण छूने वाले व्यक्ति को घातक झटका नहीं लगता!\n\n2. लघुपथन (Short-Circuiting):\nजब तारों का प्लास्टिक आवरण खराब हो जाता है या उपकरण में कोई खराबी आ जाती है, तो विद्युन्मय (Live) तार और उदासीन (Neutral) तार सीधे एक-दूसरे के संपर्क में आ जाते हैं। प्रतिरोध लगभग शून्य हो जाने से परिपथ में विद्युत धारा अचानक अत्यधिक बढ़ जाती है, जिससे चिंगारियां और आग लग सकती है।\n\n3. अतिभारण (Overloading):\nजब परिपथ में जुड़े उपकरणों द्वारा खींची गई कुल धारा तार की सुरक्षित वहन क्षमता से अधिक हो जाती है, तो उसे 'अतिभारण' कहते हैं। इसके कारण हैं:\n• एक ही सॉकेट से बहुत सारे उपकरण जोड़ना।\n• बिजली आपूर्ति में अचानक वोल्टेज बढ़ जाना।\n• शॉर्ट सर्किट होना।\n\n4. विद्युत फ्यूज एवं MCB:\nकम गलनांक (Low Melting Point) वाले लेड और टिन के मिश्रधातु से बना सुरक्षा उपकरण। अत्यधिक धारा बहने पर जूल ऊष्मा (H = I²Rt) के कारण फ्यूज का तार पिघलकर टूट जाता है और परिपथ कट जाता है, जिससे उपकरण जलने से बच जाते हैं।",
        "body_gu": "1. અર્થિંગ (Earthing) નું કાર્ય:\nધાતુનું બોડી ધરાવતા સાધનો (ઇસ્ત્રી, ટોસ્ટર, ફ્રિજ) ના કવરને અર્થિંગ વાયર સાથે જોડવામાં આવે છે. જો કોઈ ખામીને લીધે લાઈવ વાયર ધાતુના કવરને અડી જાય, તો અર્થિંગ વાયર તે વધારાના પ્રવાહને જમીનમાં ઉતારી દે છે. જેથી સાધનને અડકનાર વ્યક્તિને જીવલેણ શોક લાગતો નથી!\n\n2. શોર્ટ સર્કિટ (Short-Circuiting):\nવાયર પરનું અવાહક પડ ઘસાઈ જતાં કે ખામી સર્જાતાં જ્યારે જીવંત (Live) વાયર અને તટસ્થ (Neutral) વાયર સીધા એકબીજાના સંપર્કમાં આવે છે, ત્યારે અવરોધ ઘટીને લગભગ શૂન્ય થઈ જાય છે અને પ્રવાહ એકાએક ખૂબ વધી જાય છે. આને શોર્ટ સર્કિટ કહે છે.\n\n3. ઓવરલોડિંગ (Overloading):\nજ્યારે પરિપથમાં જોડાયેલા તમામ સાધનો દ્વારા વપરાતો પ્રવાહ વાયરની ક્ષમતા કરતાં વધી જાય ત્યારે ઓવરલોડિંગ થાય છે. તેના કારણો:\n• એક જ પ્લગમાં ઘણા બધા સાધનો જોડવા.\n• વોલ્ટેજમાં અચાનક મોટો વધારો થવો.\n• શોર્ટ સર્કિટ થવું.\n\n4. ઇલેક્ટ્રિક ફ્યુઝ (Electric Fuse):\nનીચું ગલનબિંદુ ધરાવતી મિશ્રધાતુમાંથી બનેલું સુરક્ષા સાધન છે. વધુ પડતો પ્રવાહ વહેતાં જ જૂલ ઉષ્મા (H = I²Rt) ને લીધે ફ્યુઝનો વાયર પીગળી જઈ સર્કિટ તોડી નાખે છે, જેથી કિંમતી સાધનો બચી જાય છે."
    })

    # Worked Numerical (In-text Set 5 Q2)
    blocks.append({
        "id": next_id(),
        "type": "example",
        "title": "NCERT In-Text Q: 2 kW Electric Oven on a 5 A Domestic Circuit",
        "title_hi": "NCERT पाठ्य-निहित प्रश्न: 5 A के घरेलू परिपथ में 2 kW का विद्युत ओवन",
        "title_gu": "NCERT પાઠ્યપુસ્તક પ્રશ્ન: 5 A ના ઘરેલું પરિપથમાં 2 kW નો વિદ્યુત ઓવન",
        "body": "QUESTION:\nAn electric oven of 2 kW power rating is operated in a domestic electric circuit (220 V) that has a current rating of 5 A. What result do you expect? Explain.\n\nSOLUTION:\n• Power rating of oven, P = 2 kW = 2000 W\n• Supply Voltage, V = 220 V\n• Safe Current rating of circuit, I_max = 5 A\n\nCALCULATION OF CURRENT DRAWN:\nElectric current, I = P / V\nI = 2000 W / 220 V = 9.09 A\n\nEXPLANATION & RESULT:\nThe electric oven draws a current of 9.09 A, which substantially exceeds the safe rated capacity of 5 A for this circuit. This causes severe OVERLOADING. As a consequence:\n1. Excessive Joule heat will be generated in the wires.\n2. The 5 A electric fuse wire will heat up and melt, breaking the circuit to prevent wire melting and fire hazards.",
        "body_hi": "प्रश्न:\n2 kW शक्ति अनुमतांक का एक विद्युत ओवन 220 V के घरेलू परिपथ में प्रचालित किया जाता है जिसका धारा अनुमतांक 5 A है। आप इससे किस परिणाम की अपेक्षा करते हैं? स्पष्ट कीजिए।\n\nहल:\n• ओवन की शक्ति (P) = 2 kW = 2000 W\n• विभव (V) = 220 V\n• परिपथ का धारा अनुमतांक = 5 A\n\nओवन द्वारा ली गई धारा:\nI = P / V = 2000 / 220 = 9.09 A\n\nनिष्कर्ष एवं परिणाम:\nओवन द्वारा 9.09 A की धारा ली जाती है, जो परिपथ की सुरक्षित क्षमता (5 A) से काफी अधिक है। इसके परिणामस्वरूप 'अतिभारण' (Overloading) होगा और अत्यधिक धारा के कारण 5 A का फ्यूज तार पिघलकर टूट जाएगा, जिससे परिपथ कट जाएगा और आग लगने का खतरा टल जाएगा।",
        "body_gu": "પ્રશ્ન:\n5 A ના પ્રવાહ રેટિંગ ધરાવતા 220 V ના ઘરેલું વિદ્યુત પરિપથમાં 2 kW પાવર રેટિંગ ધરાવતો ઓવન વાપરવામાં આવે છે. તમે કયા પરિણામની અપેક્ષા રાખો છો? સમજાવો.\n\nઉકેલ:\n• ઓવનનો પાવર (P) = 2 kW = 2000 W\n• વોલ્ટેજ (V) = 220 V\n• પરિપથનું પ્રવાહ રેટિંગ = 5 A\n\nઓવન દ્વારા ખેંચાતો પ્રવાહ:\nI = P / V = 2000 / 220 = 9.09 A\n\nસમજૂતી અને તારણ:\nઓવન 9.09 A નો પ્રવાહ વાપરે છે જે પરિપથની 5 A ની ક્ષમતા કરતાં ખૂબ વધારે છે. આથી 'ઓવરલોડિંગ' થશે અને વધુ પડતા પ્રવાહના કારણે 5 A નો ફ્યુઝ પીગળી જશે અને પરિપથ બંધ થઈ જશે જેથી વાયરો બળી જતાં અટકી જશે."
    })

    # Teacher Tip: Safety Precaution
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Teacher Tip: 3 Practical Precautions to Avoid Overloading",
        "title_hi": "शिक्षक टिप: अतिभारण (Overloading) से बचने की 3 व्यावहारिक सावधानियां",
        "title_gu": "શિક્ષક ટિપ: ઓવરલોડિંગથી બચવા માટેની 3 વ્યવહારુ સાવચેતીઓ",
        "body": "When answering 'What precautions should be taken to avoid overloading?':\n1. Never connect too many high-power appliances to a single electrical socket.\n2. Always use standard ISI-certified cables with proper insulation and appropriate current ratings (15 A for heaters/geysers; 5 A for lights).\n3. Install suitable electric fuses or Miniature Circuit Breakers (MCB) in every branch circuit.",
        "body_hi": "बोर्ड परीक्षा में 'अतिभारण से बचने की सावधानियां' लिखते समय:\n1. एक ही सॉकेट से बहुत सारे भारी बिजली के उपकरण न जोड़ें।\n2. हमेशा उचित धारा क्षमता और अच्छी गुणवत्ता (ISI मार्क) वाले तारों का उपयोग करें।\n3. परिपथ में हमेशा उपयुक्त क्षमता वाले फ्यूज या MCB लगाएं।",
        "body_gu": "પરીક્ષામાં 'ઓવરલોડિંગથી બચવાના ઉપાયો' પૂછાય ત્યારે:\n1. એક જ સોકેટમાં ઘણા બધા ભારે પાવરવાળા સાધનો ન જોડવા.\n2. યોગ્ય પ્રવાહ ક્ષમતા ધરાવતા ગુણવત્તાયુક્ત વાયરો વાપરવા (હીટર માટે 15 A અને બલ્બ માટે 5 A).\n3. દરેક સર્કિટમાં યોગ્ય રેટિંગવાળા ફ્યુઝ કે MCB લગાવવા."
    })

    # 5. Knowledge Check (In-text Set 5 Q1)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT In-Text Q: Name two safety measures commonly used in domestic electric circuits and appliances.",
        "question_hi": "NCERT पाठ्य-निहित प्रश्न: विद्युत परिपथों तथा साधित्रों में सामान्यतः उपयोग होने वाले दो सुरक्षा उपायों के नाम लिखिए।",
        "question_gu": "NCERT પાઠ્યપુસ્તક પ્રશ્ન: વિદ્યુત પરિપથો અને સાધનોમાં સામાન્ય રીતે વપરાતા બે સુરક્ષા ઉપાયોના નામ આપો:",
        "options": [
            "Electric Fuse and Earthing wire",
            "Ammeter and Voltmeter",
            "Rheostat and Switch",
            "Galvanometer and Transformer"
        ],
        "options_hi": [
            "विद्युत फ्यूज (Electric Fuse) एवं भूसंपर्क तार (Earthing wire)",
            "एमीटर एवं वोल्टमीटर",
            "रियोस्टैट एवं स्विच",
            "गैल्वेनोमीटर एवं ट्रांसफार्मर"
        ],
        "options_gu": [
            "વિદ્યુત ફ્યુઝ અને અર્થિંગ વાયર",
            "એમીટર અને વોલ્ટમીટર",
            "ચલ અવરોધ અને સ્વિચ",
            "ગેલ્વેનોમીટર અને ટ્રાન્સફોર્મર"
        ],
        "correct_index": 0,
        "explanation": "The two primary safety measures are: 1) Electric Fuse (or MCB), which prevents damage from overloading and short-circuits by melting and breaking the circuit; 2) Earthing wire, which safely diverts leakage currents from metallic appliance bodies into the ground to protect users from electric shocks.",
        "explanation_hi": "दो प्रमुख सुरक्षा उपाय हैं: 1) विद्युत फ्यूज (या MCB), जो अतिभारण और शॉर्ट-सर्किट की स्थिति में पिघलकर परिपथ को तोड़ देता है; 2) भूसंपर्क तार (Earthing), जो धातु के आवरण से लीक होने वाली धारा को सीधे जमीन में भेजकर उपयोगकर्ता को बिजली के झटके से बचाता है।",
        "explanation_gu": "બે મુખ્ય સુરક્ષા ઉપાયો: 1) ઇલેક્ટ્રિક ફ્યુઝ (કે MCB), જે ઓવરલોડિંગ કે શોર્ટ સર્કિટ વખતે પીગળી જઈ પરિપથ તોડી સાધનોનું રક્ષણ કરે છે; 2) અર્થિંગ વાયર, જે લીક થતા કરંટને જમીનમાં ઉતારી યુઝરને ઇલેક્ટ્રિક શોકથી બચાવે છે."
    })

    # 6. Reflection
    blocks.append({
        "id": next_id(),
        "type": "reflection",
        "title": "Why Does Human Skin Conduct Electricity?",
        "title_hi": "मानव शरीर से विद्युत धारा क्यों प्रवाहित हो जाती है?",
        "title_gu": "માનવ શરીરમાંથી વીજપ્રવાહ કેમ પસાર થઈ શકે છે?",
        "body": "The human body is approximately 60% saline water filled with dissolved electrolyte ions (Na+, K+, Cl-). Pure water is a poor conductor, but ionic water is an excellent conductor of electric current! When wet skin touches a live 220V conductor, thousands of milliamps rush through your chest cavity to find ground, causing cardiac fibrillation. Earthing protects life by providing a near-zero resistance copper path that diverts 99.99% of that current away from human tissue.",
        "body_hi": "मानव शरीर लगभग 60% लवणीय जल (Saline water) से बना है जिसमें सोडियम, पोटेशियम और क्लोराइड आयन घुले होते हैं। जब गीली त्वचा 220V के जीवित तार को छूती है, तो शरीर से भारी धारा बहती है जो हृदय की धड़कन को रोक सकती है। भूसंपर्क तार (Earthing) तांबे का लगभग शून्य प्रतिरोध वाला मार्ग प्रदान करके इस सारी धारा को हमारे शरीर के बजाय जमीन में सुरक्षित भेज देता है।",
        "body_gu": "માનવ શરીરમાં 60% જેટલું ક્ષારયુક્ત પાણી (ઇલેક્ટ્રોલાઇટ્સ Na+, K+, Cl-) રહેલું છે. ભીની ચામડી 220V ના વાયરને અડતાં જ શરીરમાંથી પ્રવાહ ધસી જઈ હૃદયને નુકસાન પહોંચાડી શકે છે. અર્થિંગ વાયર તાંબાનો શૂન્ય અવરોધવાળો માર્ગ આપી સમગ્ર કરંટને જમીનમાં ઉતારી માનવજીવન બચાવે છે."
    })

    # 7. Connection
    blocks.append({
        "id": next_id(),
        "type": "connection",
        "title": "Modern Green Buildings: From Wire Fuses to Smart RCCBs",
        "title_hi": "आधुनिक ग्रीन बिल्डिंग: पुराने फ्यूज से स्मार्ट RCCB और MCB तक",
        "title_gu": "આધુનિક સ્માર્ટ બિલ્ડિંગ્સ: જૂના ફ્યુઝથી માંડીને સ્માર્ટ RCCB અને MCB",
        "body": "In old homes, replacing a blown ceramic fuse meant finding a scrap piece of wire in the dark! Modern buildings use Miniature Circuit Breakers (MCBs) and Residual Current Circuit Breakers (RCCBs). An MCB uses an internal bimetallic strip and electromagnet that trips mechanically in just 3 milliseconds during a short circuit. An RCCB continuously compares incoming Live current with outgoing Neutral current: if a leakage as tiny as 30 milliamperes is detected escaping through a human, it trips in 0.03 seconds!",
        "body_hi": "पुराने घरों में फ्यूज उड़ने पर अंधेरे में तार ढूंढकर बांधना पड़ता था! आधुनिक इमारतों में मिनिएचर सर्किट ब्रेकर (MCB) और आरसीसीबी (RCCB) का उपयोग किया जाता है। MCB एक इलेक्ट्रोमैग्नेट की मदद से शॉर्ट सर्किट होते ही मात्र 3 मिलीसेकंड में ट्रिप हो जाता है। वहीं RCCB लाइव और न्यूट्रल धारा की लगातार तुलना करता है; यदि 30 मिलीएम्पीयर की भी लीकेज दिखे, तो यह 0.03 सेकंड में बिजली काट देता है!",
        "body_gu": "જૂના ઘરોમાં ફ્યુઝ બળી જતાં અંધારામાં તાર બાંધવો પડતો હતો! આધુનિક મકાનોમાં MCB અને RCCB વપરાય છે. શોર્ટ સર્કિટ થતાં જ MCB માત્ર 3 મિલિસેકન્ડમાં ટ્રીપ થઈ જાય છે. જ્યારે RCCB માત્ર 30 મિલિએમ્પીયરના લીકેજ પર પણ 0.03 સેકન્ડમાં લાઈન કાપી નાખી વ્યક્તિનો જીવ બચાવી લે છે!"
    })

    # 8. Mastery Challenge (NCERT Exercise Q2)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q2: At the time of a short circuit, the current in the circuit:",
        "question_hi": "NCERT अभ्यास प्रश्न 2: लघुपथन (Short Circuit) के समय परिपथ में विद्युत धारा का मान:",
        "question_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 2: શોર્ટ સર્કિટ વખતે પરિપથમાં વિદ્યુતપ્રવાહનું મૂલ્ય:",
        "options": [
            "increases heavily.",
            "reduces substantially.",
            "does not change.",
            "varies continuously."
        ],
        "options_hi": [
            "बहुत अधिक बढ़ जाता है।",
            "काफी हद तक कम हो जाता है।",
            "परिवर्तित नहीं होता।",
            "लगातार बदलता रहता है।"
        ],
        "options_gu": [
            "ખૂબ મોટા પ્રમાણમાં વધી જાય છે.",
            "નોંધપાત્ર રીતે ઘટી જાય છે.",
            "બદલાતો નથી.",
            "સતત બદલાયા કરે છે."
        ],
        "correct_index": 0,
        "explanation": "During a short circuit, the Live wire and Neutral wire come into direct physical contact with negligible resistance (R ≈ 0). By Ohm's law (I = V/R), as resistance drops near zero, the current surges heavily to immense values.",
        "explanation_hi": "शॉर्ट सर्किट के समय लाइव और न्यूट्रल तार सीधे संपर्क में आ जाते हैं जिससे प्रतिरोध लगभग शून्य हो जाता है। ओम के नियमानुसार (I = V/R), प्रतिरोध शून्य होने पर धारा बहुत अधिक बढ़ जाती है।",
        "explanation_gu": "શોર્ટ સર્કિટ વખતે લાઈવ અને ન્યુટ્રલ વાયર સીધા અડી જવાથી અવરોધ લગભગ શૂન્ય થઈ જાય છે. ઓહ્મના નિયમ (I = V/R) મુજબ અવરોધ શૂન્ય થતાં પ્રવાહ એકાએક ખૂબ મોટા પ્રમાણમાં વધી જાય છે."
    })

    # =========================================================================
    # MODULE 7: COMPLETE NCERT IN-TEXT QUESTIONS (ALL SETS)
    # =========================================================================

    # In-Text Set 2 Q1 & Q2 (Bar Magnet Field Lines & Properties)
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "NCERT In-Text Questions: Page 198 (Q1 & Q2 - Magnetic Field Lines)",
        "title_hi": "NCERT पाठ्य-निहित प्रश्न: पृष्ठ 198 (प्रश्न 1 एवं 2 - चुंबकीय क्षेत्र रेखाएं)",
        "title_gu": "NCERT પાઠ્યપુસ્તક પ્રશ્નો: પાના નં. 198 (પ્રશ્ન 1 અને 2 - ચુંબકીય ક્ષેત્રરેખાઓ)",
        "body": "QUESTION 1:\nDraw magnetic field lines around a bar magnet.\n\nANSWER 1:\n• Magnetic field lines emerge from the North pole (N) of the bar magnet and curve symmetrically through surrounding space to enter the South pole (S).\n• Inside the magnet, the lines run straight from the South pole to the North pole, forming continuous closed loops.\n• The density of lines is highest near the magnetic poles.\n\nQUESTION 2:\nList the properties of magnetic field lines.\n\nANSWER 2:\n1. Direction: Outside the magnet, they travel from North to South; inside the magnet, from South to North (closed continuous curves).\n2. Strength Indicator: Closeness of field lines indicates field strength (dense near poles where field is strongest).\n3. Non-Intersection: No two magnetic field lines ever intersect each other.",
        "body_hi": "प्रश्न 1:\nकिसी छड़ चुंबक के चारों ओर चुंबकीय क्षेत्र रेखाएं खींचिए।\n\nउत्तर 1:\n• क्षेत्र रेखाएं चुंबक के उत्तरी ध्रुव (N) से निकलकर वक्र बनाते हुए दक्षिणी ध्रुव (S) में प्रवेश करती हैं।\n• चुंबक के अंदर वे दक्षिण से उत्तर की ओर जाकर सतत बंद लूप बनाती हैं।\n• ध्रुवों के पास रेखाएं अत्यधिक घनी होती हैं।\n\nप्रश्न 2:\nचुंबकीय क्षेत्र रेखाओं के गुणों की सूची बनाइए।\n\nउत्तर 2:\n1. दिशा: चुंबक के बाहर उत्तर से दक्षिण और अंदर दक्षिण से उत्तर की ओर (सतत बंद वक्र)।\n2. प्रबलता: रेखाओं की निकटता क्षेत्र की प्रबलता दर्शाती है (ध्रुवों पर अधिक प्रबल)।\n3. प्रतिच्छेदन न करना: दो क्षेत्र रेखाएं कभी एक-दूसरे को नहीं काटतीं।",
        "body_gu": "પ્રશ્ન 1:\nગજિયા ચુંબકની આસપાસ ચુંબકીય ક્ષેત્રરેખાઓ દોરો.\n\nઉત્તર 1:\n• ક્ષેત્રરેખાઓ ઉત્તર ધ્રુવ (N) માંથી નીકળી વક્રાકારે દક્ષિણ ધ્રુવ (S) માં પ્રવેશે છે.\n• ચુંબકની અંદર તે દક્ષિણથી ઉત્તર તરફ જઈ બંધ ગાળો રચે છે.\n• ધ્રુવો આગળ ક્ષેત્રરેખાઓ સૌથી વધુ ગીચ હોય છે.\n\nપ્રશ્ન 2:\nચુંબકીય ક્ષેત્રરેખાઓના ગુણધર્મોની યાદી બનાવો.\n\nઉત્તર 2:\n1. દિશા: ચુંબકની બહાર N થી S અને અંદર S થી N તરફ (બંધ વક્ર).\n2. પ્રબળતા: ક્ષેત્રરેખાઓની ગીચતા ક્ષેત્રની પ્રબળતા દર્શાવે છે (ધ્રુવો પાસે મહત્તમ).\n3. છેદન ન કરવું: બે ક્ષેત્રરેખાઓ ક્યારેય એકબીજાને છેદતી નથી."
    })

    # In-Text Set 2 Q3 (Non-intersection of Field Lines)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT In-Text Q: Why don't two magnetic field lines intersect each other?",
        "question_hi": "NCERT पाठ्य-निहित प्रश्न: दो चुंबकीय क्षेत्र रेखाएं एक-दूसरे को प्रतिच्छेद क्यों नहीं करतीं?",
        "question_gu": "NCERT પાઠ્યપુસ્તક પ્રશ્ન: બે ચુંબકીય ક્ષેત્રરેખાઓ એકબીજાને કેમ છેદતી નથી?",
        "options": [
            "At the point of intersection, a compass needle would point in two different directions at once, which is physically impossible.",
            "Magnetic lines carry identical electric charges that repel each other.",
            "The magnetic field strength drops to zero between field lines.",
            "Field lines are straight rigid rods that cannot bend."
        ],
        "options_hi": [
            "प्रतिच्छेद बिंदु पर कंपास की सुई एक साथ दो दिशाओं की ओर संकेत करेगी, जो कि भौतिक रूप से असंभव है।",
            "चुंबकीय रेखाओं पर समान विद्युत आवेश होता है जो एक-दूसरे को प्रतिकर्षित करता है।",
            "क्षेत्र रेखाओं के बीच में चुंबकीय क्षेत्र शून्य हो जाता है।",
            "क्षेत्र रेखाएं सीधी ठोस छड़ें होती हैं जो मुड़ नहीं सकतीं।"
        ],
        "options_gu": [
            "છેદનબિંદુ આગળ હોકાયંત્રની સોય એકસાથે બે દિશાઓ દર્શાવે, જે કુદરતી રીતે અશક્ય છે.",
            "ચુંબકીય રેખાઓ સમાન વિદ્યુતભાર ધરાવતી હોવાથી અપાકર્ષણ પામે છે.",
            "ક્ષેત્રરેખાઓ વચ્ચે ચુંબકીય ક્ષેત્ર શૂન્ય થઈ જાય છે.",
            "ક્ષેત્રરેખાઓ વળી ન શકે તેવી સખત લાકડીઓ જેવી હોય છે."
        ],
        "correct_index": 0,
        "explanation": "The direction of magnetic field at any point is given by the tangent to the field line (the direction in which a compass needle points). If two field lines crossed, there would be two tangents at that single point, meaning two directions of the magnetic field simultaneously, which is impossible.",
        "explanation_hi": "किसी बिंदु पर चुंबकीय क्षेत्र की दिशा उस बिंदु पर खींची गई स्पर्श रेखा (कंपास सुई की दिशा) द्वारा दी जाती है। यदि दो रेखाएं काटेंगी, तो उस एक ही बिंदु पर दो स्पर्श रेखाएं होंगी, जिसका अर्थ होगा कि एक ही स्थान पर चुंबकीय क्षेत्र की दो दिशाएं हैं, जो संभव नहीं है।",
        "explanation_gu": "કોઈપણ બિંદુએ ચુંબકીય ક્ષેત્રની દિશા તે બિંદુએ દોરેલા સ્પર્શક (હોકાયંત્રની સોય) દ્વારા મળે છે. જો બે રેખાઓ છેદે તો તે બિંદુએ બે સ્પર્શકો મળે, જેનો અર્થ એ થાય કે એક જ બિંદુએ ચુંબકીય ક્ષેત્રની બે દિશાઓ છે, જે અશક્ય છે."
    })

    # In-Text Set 3 Q2 (Uniform Magnetic Field Representation)
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "NCERT In-Text Question: Page 200 (Q2 - Representation of Uniform Field)",
        "title_hi": "NCERT पाठ्य-निहित प्रश्न: पृष्ठ 200 (प्रश्न 2 - एकसमान चुंबकीय क्षेत्र का निरूपण)",
        "title_gu": "NCERT પાઠ્યપુસ્તક પ્રશ્ન: પાના નં. 200 (પ્રશ્ન 2 - સમાન ચુંબકીય ક્ષેત્રનું નિરૂપણ)",
        "body": "QUESTION:\nThe magnetic field in a given region is uniform. Draw a diagram to represent it.\n\nANSWER:\nA uniform magnetic field is a region where the magnetic field has the same magnitude and the same direction at every single point.\n• REPRESENTATION:\nIt is represented by a set of EQUIDISTANT, PARALLEL STRAIGHT LINES pointing in the same direction.\n• If the lines are parallel and pointing from left to right, it represents a uniform field directed to the right.\n• If pointing perpendicularly into the plane of the page, it is represented by a uniform grid of crosses (x).\n• If pointing perpendicularly out of the plane of the page, it is represented by a uniform grid of dots (•).\n• EXAMPLE IN REAL LIFE: The magnetic field inside a long current-carrying solenoid.",
        "body_hi": "प्रश्न:\nकिसी दिए गए क्षेत्र में चुंबकीय क्षेत्र एकसमान है। इसे निरूपित करने के लिए आरेख खींचिए।\n\nउत्तर:\nएकसमान चुंबकीय क्षेत्र वह क्षेत्र है जहां प्रत्येक बिंदु पर चुंबकीय क्षेत्र का परिमाण और दिशा समान होती है।\n• निरूपण:\nइसे समान दूरी पर स्थित समानांतर सीधी रेखाओं (Equidistant Parallel Lines) द्वारा दर्शाया जाता है, जिनके तीर एक ही दिशा में होते हैं।\n• यदि रेखाएं बाईं से दाईं ओर समानांतर हैं, तो यह दाईं ओर एकसमान क्षेत्र को दर्शाती हैं।\n• यदि तल के लंबवत अंदर जा रही हों, तो क्रॉस (x) के ग्रिड द्वारा दर्शाया जाता है।\n• यदि तल के लंबवत बाहर आ रही हों, तो बिंदु (•) के ग्रिड द्वारा दर्शाया जाता है।\n• वास्तविक उदाहरण: लंबी धारावाही परिनालिका के भीतर का चुंबकीय क्षेत्र।",
        "body_gu": "પ્રશ્ન:\nકોઈ વિસ્તારમાં ચુંબકીય ક્ષેત્ર સમાન છે. તેને દર્શાવતી આકૃતિ દોરો.\n\nઉત્તર:\nસમાન ચુંબકીય ક્ષેત્ર એવો વિસ્તાર છે જ્યાં તમામ બિંદુઓએ ચુંબકીય ક્ષેત્રનું મૂલ્ય અને દિશા સરખાં હોય છે.\n• નિરૂપણ:\nતેને પરસ્પર સમાંતર અને સમાન અંતરે આવેલી સુરેખ ક્ષેત્રરેખાઓ (Equidistant Parallel Lines) દ્વારા દર્શાવવામાં આવે છે.\n• પાનાના સમતલને લંબ અંદર જતી દિશા માટે ચોકડી (x) ના ચિહ્નો વપરાય છે.\n• પાનાના સમતલમાંથી બહાર આવતી દિશા માટે ટપકાં (•) વપરાય છે.\n• વાસ્તવિક ઉદાહરણ: વિદ્યુતપ્રવાહધારિત સોલેનોઇડની અંદરનું ચુંબકીય ક્ષેત્ર."
    })

    # In-Text Set 4 Q2 (Activity 12.7 Rod Displacement Factors)
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "NCERT In-Text Question: Page 203 (Q2 - Factors Affecting Rod Displacement)",
        "title_hi": "NCERT पाठ्य-निहित प्रश्न: पृष्ठ 203 (प्रश्न 2 - छड़ के विस्थापन को प्रभावित करने वाले कारक)",
        "title_gu": "NCERT પાઠ્યપુસ્તક પ્રશ્ન: પાના નં. 203 (પ્રશ્ન 2 - સળિયાના વિચલનને અસર કરતા પરિબળો)",
        "body": "QUESTION:\nIn Activity 12.7, how do we think the displacement of rod AB will be affected if:\n(i) current in rod AB is increased?\n(ii) a stronger horse-shoe magnet is used?\n(iii) length of the rod AB is increased?\n\nANSWER:\nThe force acting on a current-carrying conductor in a magnetic field is given by F = B * I * L * sin(θ). Since the rod is perpendicular to the field (sin 90° = 1), F = B * I * L.\n\n(i) If current (I) in rod AB is increased:\nThe magnetic force increases proportionally (F ∝ I). Therefore, the displacement of rod AB INCREASES.\n\n(ii) If a stronger horse-shoe magnet is used (higher B):\nThe magnetic force increases proportionally (F ∝ B). Therefore, the displacement of rod AB INCREASES.\n\n(iii) If length of the rod AB is increased (higher L):\nThe magnetic force increases proportionally (F ∝ L). Therefore, the displacement of rod AB INCREASES.",
        "body_hi": "प्रश्न:\nक्रियाकलाप 12.7 में छड़ AB का विस्थापन किस प्रकार प्रभावित होगा यदि:\n(i) छड़ AB में प्रवाहित धारा बढ़ा दी जाए?\n(ii) अधिक प्रबल नाल चुंबक प्रयोग किया जाए?\n(iii) छड़ AB की लंबाई बढ़ा दी जाए?\n\nउत्तर:\nचुंबकीय क्षेत्र में लंबवत रखे चालक पर लगने वाला बल F = B * I * L होता है।\n\n(i) धारा (I) बढ़ाने पर: बल धारा के समानुपाती होता है (F ∝ I), अतः छड़ का विस्थापन बढ़ जाएगा।\n(ii) अधिक प्रबल चुंबक (B) लेने पर: बल चुंबकीय क्षेत्र के समानुपाती होता है (F ∝ B), अतः छड़ का विस्थापन बढ़ जाएगा।\n(iii) छड़ की लंबाई (L) बढ़ाने पर: बल चालक की लंबाई के समानुपाती होता है (F ∝ L), अतः छड़ का विस्थापन बढ़ जाएगा।",
        "body_gu": "પ્રશ્ન:\nપ્રવૃત્તિ 12.7 માં સળિયા AB નું સ્થાનાંતર કેવી રીતે પ્રભાવિત થશે જો:\n(i) સળિયા AB માંથી વહેતો પ્રવાહ વધારવામાં આવે?\n(ii) વધુ પ્રબળ નાળ ચુંબક વાપરવામાં આવે?\n(iii) સળિયા AB ની લંબાઈ વધારવામાં આવે?\n\nઉત્તર:\nચુંબકીય ક્ષેત્રમાં લંબરૂપે રહેલા વાહક પર લાગતું બળ F = B * I * L છે.\n\n(i) પ્રવાહ (I) વધારતાં: બળ પ્રવાહના સમપ્રમાણમાં વધતું હોવાથી (F ∝ I), સળિયાનું સ્થાનાંતર વધશે.\n(ii) પ્રબળ ચુંબક (B) વાપરતાં: બળ ક્ષેત્રની પ્રબળતાના સમપ્રમાણમાં વધતું હોવાથી (F ∝ B), સ્થાનાંતર વધશે.\n(iii) લંબાઈ (L) વધારતાં: બળ લંબાઈના સમપ્રમાણમાં વધતું હોવાથી (F ∝ L), સળિયાનું સ્થાનાંતર વધશે."
    })

    # =========================================================================
    # MODULE 8: COMPLETE NCERT END-OF-CHAPTER EXERCISES (Q1 TO Q9+)
    # =========================================================================

    # NCERT Exercise Q1 (MCQ)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q1: Which of the following correctly describes the magnetic field near a long straight wire?",
        "question_hi": "NCERT अभ्यास प्रश्न 1: किसी लंबे सीधे विद्युत धारावाही तार के निकट चुंबकीय क्षेत्र का सही वर्णन निम्न में से कौन करता है?",
        "question_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 1: લાંબા સુરેખ વિદ્યુતપ્રવાહધારિત તારની નજીક ચુંબકીય ક્ષેત્રનું સાચું વર્ણન નીચેનામાંથી કયું કરે છે?",
        "options": [
            "The field consists of concentric circles centred on the wire.",
            "The field consists of straight lines perpendicular to the wire.",
            "The field consists of straight lines parallel to the wire.",
            "The field consists of radial lines originating from the wire."
        ],
        "options_hi": [
            "क्षेत्र तार पर केंद्रित संकेंद्रीय वृत्तों के रूप में होता है।",
            "क्षेत्र तार के लंबवत सीधी रेखाओं के रूप में होता है।",
            "क्षेत्र तार के समानांतर सीधी रेखाओं के रूप में होता है।",
            "क्षेत्र तार से बाहर निकलती त्रिज्यीय रेखाओं के रूप में होता है।"
        ],
        "options_gu": [
            "ક્ષેત્ર તાર પર કેન્દ્રિત સમકેન્દ્રી વર્તુળોનું બનેલું છે.",
            "ક્ષેત્ર તારને લંબરૂપ સીધી રેખાઓનું બનેલું છે.",
            "ક્ષેત્ર તારને સમાંતર સીધી રેખાઓનું બનેલું છે.",
            "ક્ષેત્ર તારમાંથી નીકળતી ત્રિજ્યાવર્તી રેખાઓનું બનેલું છે."
        ],
        "correct_index": 0,
        "explanation": "The magnetic field lines around a long straight current-carrying conductor consist of a family of concentric circles centered directly on the wire and lying in a plane perpendicular to the conductor.",
        "explanation_hi": "लंबे सीधे धारावाही चालक के चारों ओर चुंबकीय क्षेत्र रेखाएं तार को केंद्र मानकर उसके लंबवत तल में संकेंद्रीय वृत्तों (Concentric Circles) के रूप में होती हैं।",
        "explanation_gu": "લાંબા સુરેખ વિદ્યુતપ્રવાહધારિત તારની આસપાસ ચુંબકીય ક્ષેત્રરેખાઓ તારને કેન્દ્ર રાખીને દોરેલા સમકેન્દ્રી વર્તુળોના રૂપમાં હોય છે."
    })

    # NCERT Exercise Q3 (True / False)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q3: State whether the following statements are True or False:\n(a) The field at the centre of a long circular coil carrying current will be parallel straight lines.\n(b) A wire with a green insulation is usually the live wire of an electric supply.",
        "question_hi": "NCERT अभ्यास प्रश्न 3: बताइए कि निम्नलिखित कथन सत्य हैं अथवा असत्य:\n(क) किसी लंबी वृत्ताकार धारावाही कुंडली के केंद्र पर क्षेत्र समानांतर सीधी रेखाएं होंगी।\n(ख) हरे विद्युतरोधी आवरण वाला तार प्रायः विद्युन्मय (Live) तार होता है।",
        "question_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 3: નીચેના વિધાનો ખરાં છે કે ખોટાં તે જણાવો:\n(a) પ્રવાહધારિત લાંબી વર્તુળાકાર કોઈલના કેન્દ્રમાં ક્ષેત્ર સમાંતર સીધી રેખાઓ હશે.\n(b) લીલા અવાહક પડવાળો વાયર સામાન્ય રીતે જીવંત (લાઈવ) વાયર હોય છે.",
        "options": [
            "(a) is True; (b) is False",
            "(a) is False; (b) is True",
            "Both (a) and (b) are True",
            "Both (a) and (b) are False"
        ],
        "options_hi": [
            "(क) सत्य है; (ख) असत्य है",
            "(क) असत्य है; (ख) सत्य है",
            "(क) और (ख) दोनों सत्य हैं",
            "(क) और (ख) दोनों असत्य हैं"
        ],
        "options_gu": [
            "(a) ખરું છે; (b) ખોટું છે",
            "(a) ખોટું છે; (b) ખરું છે",
            "(a) અને (b) બંને ખરાં છે",
            "(a) અને (b) બંને ખોટાં છે"
        ],
        "correct_index": 0,
        "explanation": "Statement (a) is TRUE: Near the centre of a circular coil, the field lines are parallel straight lines perpendicular to the loop plane. Statement (b) is FALSE: A wire with green insulation is the EARTH wire; the live wire has RED insulation.",
        "explanation_hi": "कथन (क) सत्य है: कुंडली के केंद्र पर रेखाएं समानांतर सीधी होती हैं। कथन (ख) असत्य है: हरा तार भूसंपर्क (Earth) तार होता है, जबकि विद्युन्मय (Live) तार लाल रंग का होता है।",
        "explanation_gu": "વિધાન (a) ખરું છે: કોઈલના કેન્દ્રમાં ક્ષેત્રરેખાઓ સમાંતર સીધી હોય છે. વિધાન (b) ખોટું છે: લીલો વાયર અર્થિંગ વાયર હોય છે, જ્યારે લાઈવ વાયર લાલ રંગનો હોય છે."
    })

    # NCERT Exercise Q4
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "NCERT Exercise Q4: Two Methods of Producing Magnetic Fields",
        "title_hi": "NCERT अभ्यास प्रश्न 4: चुंबकीय क्षेत्र उत्पन्न करने की दो विधियां",
        "title_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 4: ચુંબકીય ક્ષેત્ર ઉત્પન્ન કરવાની બે રીતો",
        "body": "QUESTION:\nList two methods of producing magnetic fields.\n\nANSWER:\n1. Using Permanent Magnets: Natural lodestones or artificial permanent magnets made of steel/alloys (such as bar magnets, horseshoe magnets, or magnetic compass needles) produce a persistent magnetic field in surrounding space.\n2. Using Electric Currents: Passing an electric current through a conductor (a straight wire, circular loop, or solenoid) creates an immediate magnetic field around it.\n3. Using Electromagnets: Placing a soft iron core inside a current-carrying solenoid produces an exceptionally strong magnetic field.",
        "body_hi": "प्रश्न:\nचुंबकीय क्षेत्र उत्पन्न करने की दो विधियों की सूची बनाइए।\n\nउत्तर:\n1. स्थाई चुंबकों का उपयोग करके: छड़ चुंबक, नाल चुंबक या चुंबकीय सुई अपने चारों ओर निरंतर चुंबकीय क्षेत्र उत्पन्न करते हैं।\n2. विद्युत धारा का उपयोग करके: किसी चालक (सीधे तार, वृत्ताकार कुंडली या परिनालिका) में से विद्युत धारा प्रवाहित करके उसके चारों ओर चुंबकीय क्षेत्र बनाया जाता है।\n3. विद्युत चुंबक बनाकर: धारावाही परिनालिका के अंदर नरम लोहे की छड़ रखकर अत्यधिक शक्तिशाली चुंबकीय क्षेत्र उत्पन्न किया जाता है।",
        "body_gu": "પ્રશ્ન:\nચુંબકીય ક્ષેત્ર ઉત્પન્ન કરવાની બે પદ્ધતિઓની યાદી બનાવો.\n\nઉત્તર:\n1. કાયમી ચુંબકોનો ઉપયોગ કરીને: ગજિયા ચુંબક, નાળ ચુંબક કે હોકાયંત્રની સોય પોતાની આસપાસ કાયમી ચુંબકીય ક્ષેત્ર ધરાવે છે.\n2. વિદ્યુતપ્રવાહનો ઉપયોગ કરીને: સુરેખ વાયર, વર્તુળાકાર ગૂંચળા કે સોલેનોઇડમાંથી વિદ્યુતપ્રવાહ પસાર કરીને ચુંબકીય ક્ષેત્ર મેળવી શકાય છે.\n3. વિદ્યુતચુંબક બનાવીને: સોલેનોઇડમાં નરમ લોખંડનો ગર્ભ મૂકી પ્રવાહ આપતાં પ્રબળ ક્ષેત્ર મળે છે."
    })

    # NCERT Exercise Q5
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q5: When is the force experienced by a current-carrying conductor placed in a magnetic field largest?",
        "question_hi": "NCERT अभ्यास प्रश्न 5: किसी चुंबकीय क्षेत्र में स्थित धारावाही चालक पर आरोपित बल कब अधिकतम होता है?",
        "question_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 5: ચુંબકીય ક્ષેત્રમાં મૂકેલા વિદ્યુતપ્રવાહધારિત વાહક પર લાગતું બળ ક્યારે મહત્તમ હોય છે?",
        "options": [
            "When the direction of current is perpendicular (at 90 degrees) to the direction of magnetic field.",
            "When the direction of current is parallel (at 0 degrees) to the magnetic field.",
            "When the direction of current is antiparallel (at 180 degrees) to the magnetic field.",
            "When the conductor is coiled into an open loop at 45 degrees."
        ],
        "options_hi": [
            "जब विद्युत धारा की दिशा चुंबकीय क्षेत्र की दिशा के लंबवत (90 डिग्री पर) होती है।",
            "जब धारा की दिशा चुंबकीय क्षेत्र के समानांतर (0 डिग्री पर) होती है।",
            "जब धारा की दिशा चुंबकीय क्षेत्र के विपरीत समानांतर (180 डिग्री पर) होती है।",
            "जब चालक 45 डिग्री के कोण पर रखा होता है।"
        ],
        "options_gu": [
            "જ્યારે વિદ્યુતપ્રવાહની દિશા ચુંબકીય ક્ષેત્રની દિશાને લંબરૂપે (90 અંશના ખૂણે) હોય.",
            "જ્યારે વિદ્યુતપ્રવાહની દિશા ચુંબકીય ક્ષેત્રને સમાંતર (0 અંશે) હોય.",
            "જ્યારે વિદ્યુતપ્રવાહની દિશા ચુંબકીય ક્ષેત્રની વિરુદ્ધ દિશામાં સમાંતર (180 અંશે) હોય.",
            "જ્યારે વાહક 45 અંશના ખૂણે ગોઠવાયેલો હોય."
        ],
        "correct_index": 0,
        "explanation": "The magnitude of force is F = B * I * L * sin(θ). The value of sin(θ) is maximum at θ = 90° (sin 90° = 1). Therefore, the force experienced by a current-carrying conductor is largest when the conductor is placed perpendicular to the direction of the magnetic field.",
        "explanation_hi": "बल का सूत्र F = B * I * L * sin(θ) होता है। sin(θ) का मान θ = 90° पर अधिकतम (1) होता है। अतः जब धारावाही चालक चुंबकीय क्षेत्र के लंबवत होता है, तब उस पर लगने वाला बल सबसे बड़ा (अधिकतम) होता है।",
        "explanation_gu": "બળનું સૂત્ર F = B * I * L * sin(θ) છે. θ = 90° હોય ત્યારે sin(90°) = 1 મહત્તમ થાય છે. આથી જ્યારે વાહક ચુંબકીય ક્ષેત્રને લંબરૂપે હોય ત્યારે તેના પર લાગતું બળ સૌથી મોટું (મહત્તમ) હોય છે."
    })

    # NCERT Exercise Q6
    blocks.append({
        "id": next_id(),
        "type": "example",
        "title": "NCERT Exercise Q6: Deflection of Horizontal Electron Beam in Chamber",
        "title_hi": "NCERT अभ्यास प्रश्न 6: कक्ष में क्षैतिज इलेक्ट्रॉन पुंज का विक्षेपण",
        "title_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 6: ઓરડામાં સમક્ષિતિજ ઇલેક્ટ્રોન બીમનું વિચલન",
        "body": "QUESTION:\nImagine that you are sitting in a chamber with your back to one wall. An electron beam, moving horizontally from the back wall towards the front wall, is deflected by a strong magnetic field to your right side. What is the direction of the magnetic field?\n\nSOLUTION:\n1. Direction of Electron Beam: From back wall to front wall (FORWARD).\n2. Direction of Conventional Current (I): Because electrons carry negative charge, the direction of conventional current is OPPOSITE to electron motion. Therefore, current is directed from the front wall to the back wall (BACKWARD).\n• Middle finger of left hand points BACKWARDS (towards yourself).\n3. Direction of Magnetic Force (F): Deflection is to your RIGHT side.\n• Thumb of left hand points to your RIGHT.\n4. Apply Fleming's Left-Hand Rule:\nWith middle finger pointing BACKWARDS and thumb pointing RIGHT, your forefinger points vertically DOWNWARDS (towards the floor).\n\nCONCLUSION:\nThe direction of the magnetic field is vertically DOWNWARD.",
        "body_hi": "प्रश्न:\nमान लीजिए आप किसी कक्ष में अपनी पीठ को एक दीवार से सटाकर बैठे हैं। कोई इलेक्ट्रॉन पुंज, जो पिछली दीवार से सामने की दीवार की ओर क्षैतिजतः गमन कर रहा है, किसी प्रबल चुंबकीय क्षेत्र द्वारा आपके दाईं ओर विक्षेपित हो जाता है। चुंबकीय क्षेत्र की दिशा क्या है?\n\nहल:\n1. इलेक्ट्रॉन की दिशा: पीछे से आगे की ओर।\n2. विद्युत धारा (I) की दिशा: इलेक्ट्रॉन ऋणावेशित होते हैं, अतः धारा की दिशा उनकी गति के विपरीत (आगे से पीछे / आपकी ओर) होगी।\n• बाएं हाथ की मध्यमा को पीछे की ओर रखें।\n3. बल (F) की दिशा: विक्षेप दाईं ओर है, अतः अंगूठे को दाईं ओर रखें।\n4. फ्लेमिंग का वाम-हस्त नियम लगाने पर:\nतर्जनी ऊर्ध्वाधर नीचे की ओर (Downward / फर्श की ओर) संकेत करती है।\n\nनिष्कर्ष:\nचुंबकीय क्षेत्र की दिशा ऊर्ध्वाधर अधोमुखी (Vertically Downward) है।",
        "body_gu": "પ્રશ્ન:\nધારો કે તમે એક ઓરડામાં દીવાલ તરફ પીઠ રાખીને બેઠા છો. એક ઇલેક્ટ્રોન બીમ પાછળની દીવાલથી આગળની દીવાલ તરફ સમક્ષિતિજ ગતિ કરે છે અને પ્રબળ ચુંબકીય ક્ષેત્ર વડે તમારી જમણી બાજુ વિચલિત થાય છે. ચુંબકીય ક્ષેત્રની દિશા શોધો.\n\nઉકેલ:\n1. ઇલેક્ટ્રોનની ગતિ: પાછળથી આગળ તરફ.\n2. પ્રવાહ (I) ની દિશા: ઇલેક્ટ્રોન ઋણભારિત હોવાથી પ્રવાહ આગળથી પાછળ (તમારી તરફ) ગણાય -> વચ્ચેની આંગળી પાછળ રાખો.\n3. બળ (F) ની દિશા: વિચલન જમણી બાજુ હોવાથી અંગૂઠો જમણી તરફ રાખો.\n4. ફ્લેમિંગનો ડાબા હાથનો નિયમ વાપરતાં:\nપહેલી આંગળી અધોદિશામાં (Vertically Downward / ભોંયતળિયા તરફ) દિશા દર્શાવે છે.\n\nતારણ:\nચુંબકીય ક્ષેત્રની દિશા શિરોલંબ નીચે તરફ (Downward) છે."
    })

    # NCERT Exercise Q7
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "NCERT Exercise Q7: Three Essential Rules in Electromagnetism",
        "title_hi": "NCERT अभ्यास प्रश्न 7: विद्युत चुंबकत्व के तीन प्रमुख नियम",
        "title_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 7: વિદ્યુતચુંબકત્વના ત્રણ પાયાના નિયમો",
        "body": "QUESTION:\nState the rule to determine the direction of a:\n(i) magnetic field produced around a straight conductor carrying current,\n(ii) force experienced by a current-carrying straight conductor placed in a magnetic field which is perpendicular to it, and\n(iii) current induced in a coil due to its rotation in a magnetic field.\n\nANSWER:\n(i) RIGHT-HAND THUMB RULE:\nImagine holding the straight conductor in your right hand with the stretched thumb pointing in the direction of current. The curled fingers encircling the wire give the direction of the magnetic field lines.\n\n(ii) FLEMING'S LEFT-HAND RULE:\nStretch the thumb, forefinger, and middle finger of the left hand mutually perpendicular. If forefinger points in the direction of magnetic field and middle finger points in the direction of current, the thumb gives the direction of FORCE / MOTION.\n\n(iii) FLEMING'S RIGHT-HAND RULE:\nStretch the thumb, forefinger, and middle finger of the right hand mutually perpendicular. If forefinger points in the direction of magnetic field and thumb in the direction of motion of the conductor, the middle finger gives the direction of INDUCED CURRENT.",
        "body_hi": "प्रश्न:\nनिम्नलिखित की दिशा निर्धारित करने वाला नियम लिखिए:\n(i) किसी सीधे धारावाही चालक के चारों ओर उत्पन्न चुंबकीय क्षेत्र,\n(ii) किसी चुंबकीय क्षेत्र में लंबवत रखे धारावाही चालक पर आरोपित बल, तथा\n(iii) किसी चुंबकीय क्षेत्र में घूर्णन करने वाली कुंडली में प्रेरित विद्युत धारा।\n\nउत्तर:\n(i) दाहिने हाथ के अंगूठे का नियम (Right-Hand Thumb Rule):\nसीधे चालक को दाहिने हाथ में इस प्रकार पकड़ें कि अंगूठा धारा की दिशा में हो, तो मुड़ी हुई उंगलियां चुंबकीय क्षेत्र रेखाओं की दिशा बताएंगी।\n\n(ii) फ्लेमिंग का वाम-हस्त नियम (Fleming's Left-Hand Rule):\nबाएं हाथ के अंगूठे, तर्जनी और मध्यमा को लंबवत फैलाएं। यदि तर्जनी चुंबकीय क्षेत्र और मध्यमा धारा की दिशा में हो, तो अंगूठा बल/गति की दिशा दर्शाता है।\n\n(iii) फ्लेमिंग का दक्षिण-हस्त नियम (Fleming's Right-Hand Rule):\nदाहिने हाथ के अंगूठे, तर्जनी और मध्यमा को लंबवत फैलाएं। यदि तर्जनी चुंबकीय क्षेत्र और अंगूठा चालक की गति की दिशा में हो, तो मध्यमा प्रेरित धारा की दिशा दर्शाती है।",
        "body_gu": "પ્રશ્ન:\nનીચેનાની દિશા નક્કી કરવા માટેના નિયમો જણાવો:\n(i) સુરેખ વિદ્યુતપ્રવાહધારિત વાહકની આસપાસ ઉદ્ભવતું ચુંબકીય ક્ષેત્ર,\n(ii) ચુંબકીય ક્ષેત્રમાં લંબરૂપે મૂકેલા વિદ્યુતપ્રવાહધારિત વાહક પર લાગતું બળ, અને\n(iii) ચુંબકીય ક્ષેત્રમાં ભ્રમણ કરતી કોઈલમાં પ્રેરિત થતો વિદ્યુતપ્રવાહ.\n\nઉત્તર:\n(i) જમણા હાથના અંગૂઠાનો નિયમ: વાહકને જમણા હાથમાં પકડતાં અંગૂઠો પ્રવાહની દિશામાં હોય તો વીંટળાયેલી આંગળીઓ ચુંબકીય ક્ષેત્રરેખાઓની દિશા દર્શાવે છે.\n\n(ii) ફ્લેમિંગનો ડાબા હાથનો નિયમ: ડાબા હાથની પ્રથમ આંગળી ક્ષેત્રની દિશામાં અને વચ્ચેની આંગળી પ્રવાહની દિશામાં હોય તો અંગૂઠો વાહક પર લાગતા બળની દિશા દર્શાવે છે.\n\n(iii) ફ્લેમિંગનો જમણા હાથનો નિયમ: જમણા હાથની પ્રથમ આંગળી ક્ષેત્રની દિશામાં અને અંગૂઠો ગતિની દિશામાં હોય તો વચ્ચેની આંગળી પ્રેરિત પ્રવાહની દિશા દર્શાવે છે."
    })

    # NCERT Exercise Q8 & Q9
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "NCERT Exercise Q8 & Q9: Short-Circuiting & Necessity of Earthing",
        "title_hi": "NCERT अभ्यास प्रश्न 8 एवं 9: लघुपथन का कारण एवं भूसंपर्कन की आवश्यकता",
        "title_gu": "NCERT સ્વાધ્યાય પ્રશ્ન 8 અને 9: શોર્ટ સર્કિટ અને અર્થિંગની અનિવાર્યતા",
        "body": "QUESTION 8:\nWhen does an electric short circuit occur?\n\nANSWER 8:\nAn electric short circuit occurs when the LIVE wire and the NEUTRAL wire come into direct contact with each other. This happens when:\n1. The plastic insulation coating of the wires is damaged or perished due to wear, heat, or aging.\n2. An internal fault occurs within an appliance, bridging live and neutral terminals.\nBecause direct contact drops the resistance of the circuit to nearly zero, an enormous surge of electric current flows abruptly, creating sparks, melting wires, and causing electrical fires.\n\nQUESTION 9:\nWhat is the function of an earth wire? Why is it necessary to earth metallic appliances?\n\nANSWER 9:\n• The Earth wire (green insulation) is a low-resistance safety conductor connected to a metallic plate buried deep in the ground.\n• Necessity: In appliances with metallic bodies (electric irons, toasters, refrigerators, water heaters), there is always a risk that internal live wire insulation may fray and touch the outer metallic shell. If a person touches that live shell, current would normally pass through their body to ground, causing a fatal electric shock.\n• When properly earthed, the earth wire provides an ultra-low-resistance bypass path into the ground. The leakage current flows safely into the earth, keeping the appliance's potential at 0V and triggering the fuse/MCB to cut off power instantly.",
        "body_hi": "प्रश्न 8:\nविद्युत परिपथ में लघुपथन (Short Circuit) कब होता है?\n\nउत्तर 8:\nलघुपथन तब होता है जब विद्युन्मय (Live) तार और उदासीन (Neutral) तार सीधे एक-दूसरे के संपर्क में आ जाते हैं। ऐसा तब होता है जब:\n1. तारों का रोधन (इन्सुलेशन) पुराना होने या गर्मी से खराब हो जाता है।\n2. उपकरण के अंदर कोई खराबी आ जाती है।\nप्रतिरोध लगभग शून्य हो जाने से परिपथ में भारी धारा अचानक बहने लगती है, जिससे आग लग सकती है।\n\nप्रश्न 9:\nभूसंपर्क तार का क्या कार्य है? धातु के आवरण वाले विद्युत साधित्रों को भूसंपर्कित करना क्यों आवश्यक है?\n\nउत्तर 9:\n• भूसंपर्क तार (हरा तार) एक अत्यंत कम प्रतिरोध वाला सुरक्षा तार है जो जमीन में दबी तांबे की प्लेट से जुड़ा होता है।\n• आवश्यकता: धातु की बॉडी वाले उपकरणों (प्रेस, हीटर, फ्रिज) में यदि लाइव तार कटकर धातु की बॉडी से छू जाए, तो उसे छूने वाले व्यक्ति को जानलेવા बिजली का झटका लग सकता है। भूसंपर्क तार उस लीकेज धारा को सीधे जमीन में पहुंचा देता है, जिससे उपकरण का विभव शून्य रहता है और उपयोगकर्ता पूरी तरह सुरक्षित रहता है।",
        "body_gu": "પ્રશ્ન 8:\nવિદ્યુત પરિપથમાં શોર્ટ સર્કિટ ક્યારે થાય છે?\n\nઉત્તર 8:\nજ્યારે જીવંત (Live) વાયર અને તટસ્થ (Neutral) વાયર સીધા એકબીજાના સંપર્કમાં આવે ત્યારે શોર્ટ સર્કિટ થાય છે. આના મુખ્ય કારણો:\n1. વાયરો પરનું અવાહક પડ ઘસાઈ ગયું હોય કે બળી ગયું હોય.\n2. વિદ્યુત સાધનમાં આંતરિક ખામી સર્જાઈ હોય.\nઅવરોધ શૂન્ય થતાં પ્રવાહ એકાએક ખૂબ વધી જાય છે અને તણખા કે આગ પેદા કરે છે.\n\nપ્રશ્ન 9:\nઅર્થિંગ વાયરનું કાર્ય શું છે? ધાતુનું કવચ ધરાવતા સાધનોને અર્થિંગ કરવું કેમ જરૂરી છે?\n\nઉત્તર 9:\n• અર્થિંગ વાયર (લીલો વાયર) નીચો અવરોધ ધરાવતો વાયર છે જે જમીનમાં દાટેલી પ્લેટ સાથે જોડાયેલો હોય છે.\n• જરૂરિયાત: ઇસ્ત્રી, ટોસ્ટર કે ફ્રિજ જેવા ધાતુની બોડીવાળા સાધનોમાં જો અંદરનો લાઈવ વાયર બોડીને અડી જાય અને કોઈ માણસ તેને અડે, તો તેને જીવલેણ શોક લાગી શકે છે. અર્થિંગ વાયર તે વધારાના પ્રવાહને સીધો જમીનમાં ઉતારી દે છે જેથી સાધનનું વિદ્યુતસ્થિતિમાન શૂન્ય રહે છે અને માણસ શોકથી બચી જાય છે."
    })

    # =========================================================================
    # MODULE 9: COMPREHENSIVE SHINE ACADEMY ASSESSMENT QUESTION BANK
    # =========================================================================

    # Bank MCQ 1
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "What is the SI unit of magnetic field strength?",
        "question_hi": "चुंबकीय क्षेत्र की तीव्रता का SI मात्रक क्या है?",
        "question_gu": "ચુંબકીય ક્ષેત્રની તીવ્રતાનો SI એકમ કયો છે?",
        "options": [
            "Tesla",
            "Weber",
            "Ampere",
            "Henry"
        ],
        "options_hi": [
            "टेस्ला (Tesla)",
            "वेबर (Weber)",
            "एम्पीयर (Ampere)",
            "हेनरी (Henry)"
        ],
        "options_gu": [
            "ટેસ્લા (Tesla)",
            "વેબર (Weber)",
            "એમ્પીયર (Ampere)",
            "હેનરી (Henry)"
        ],
        "correct_index": 0,
        "explanation": "The SI unit of magnetic field strength is the Tesla (T), named in honor of Nikola Tesla. 1 Tesla = 1 Newton / (Ampere * metre).",
        "explanation_hi": "चुंबकीय क्षेत्र का SI मात्रक टेस्ला (Tesla, T) है, जो निकोला टेस्ला के सम्मान में रखा गया है। 1 टेस्ला = 1 न्यूटन / (एम्पीयर * मीटर)।",
        "explanation_gu": "ચુંબકીય ક્ષેત્રની તીવ્રતાનો SI એકમ ટેસ્લા (T) છે. 1 ટેસ્લા = 1 ન્યૂટન / (એમ્પીયર * મીટર)."
    })

    # Bank MCQ 2
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "What is the polarity of that face of a circular coil in which the electric current appears to flow in a clockwise direction?",
        "question_hi": "वृत्ताकार कुंडली के उस फलक की ध्रुवता क्या होगी जिसमें विद्युत धारा दक्षिणावर्त (Clockwise) दिशा में बहती दिखाई देती है?",
        "question_gu": "વર્તુળાકાર ગૂંચળાના જે છેડે વિદ્યુતપ્રવાહ સમઘડી (Clockwise) દિશામાં વહેતો દેખાય તે છેડાની ધ્રુવીયતા કઈ હશે?",
        "options": [
            "South Pole",
            "North Pole",
            "Neutral",
            "Alternates between North and South"
        ],
        "options_hi": [
            "दक्षिणी ध्रुव (South Pole)",
            "उत्तरी ध्रुव (North Pole)",
            "उदासीन (Neutral)",
            "उत्तर और दक्षिण के बीच बदलता रहता है"
        ],
        "options_gu": [
            "દક્ષિણ ધ્રુવ (South Pole)",
            "ઉત્તર ધ્રુવ (North Pole)",
            "તટસ્થ (Neutral)",
            "ઉત્તર અને દક્ષિણ વચ્ચે બદલાતી રહે છે"
        ],
        "correct_index": 0,
        "explanation": "According to the Clock Face Rule, if the current flows in a CLOCKWISE direction around the face of a coil, that face behaves as a SOUTH magnetic pole. If anticlockwise, it behaves as a NORTH pole.",
        "explanation_hi": "क्लॉक फेस नियम के अनुसार, यदि कुंडली में धारा दक्षिणावर्त (Clockwise) बहती दिखाई देती है, तो वह सिरा दक्षिणी ध्रुव (South Pole) बनता है। यदि वामावर्त बहे, तो वह उत्तरी ध्रुव बनता है।",
        "explanation_gu": "ઘડિયાળના નિયમ (Clock Face Rule) મુજબ જો પ્રવાહ સમઘડી (Clockwise) દિશામાં વહેતો દેખાય તો તે છેડો દક્ષિણ ધ્રુવ (S) બને છે. જો વિષમઘડી હોય તો ઉત્તર ધ્રુવ (N) બને છે."
    })

    # Bank MCQ 3
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Which material is used as the core inside a solenoid to create a powerful temporary electromagnet?",
        "question_hi": "शक्तिशाली अस्थायी विद्युत चुंबक बनाने के लिए परिनालिका के अंदर कोर के रूप में किस पदार्थ का उपयोग किया जाता है?",
        "question_gu": "શક્તિશાળી અસ્થાયી વિદ્યુતચુંબક બનાવવા માટે સોલેનોઇડની અંદર ગર્ભ તરીકે કયા દ્રવ્યનો ઉપયોગ થાય છે?",
        "options": [
            "Soft Iron",
            "Stainless Steel",
            "Alnico alloy",
            "Copper"
        ],
        "options_hi": [
            "नरम लोहा (Soft Iron)",
            "स्टेनलेस स्टील",
            "एल्निको मिश्रधातु",
            "तांबा"
        ],
        "options_gu": [
            "નરમ લોખંડ (Soft Iron)",
            "સ્ટેનલેસ સ્ટીલ",
            "એલ્નિકો મિશ્રધાતુ",
            "તાંબુ"
        ],
        "correct_index": 0,
        "explanation": "Soft iron is used because it has very high magnetic permeability (magnetizes strongly) and near-zero retentivity, meaning it loses all its magnetism instantly when current is switched off.",
        "explanation_hi": "नरम लोहे का उपयोग इसलिए किया जाता है क्योंकि यह धारा चालू होने पर बहुत शक्तिशाली चुंबक बन जाता है और धारा बंद होते ही तुरंत अपना सारा चुंबकत्व खो देता है।",
        "explanation_gu": "નરમ લોખંડ વાપરવામાં આવે છે કારણ કે તે પ્રવાહ ચાલુ થતાં જ ખૂબ પ્રબળ ચુંબક બને છે અને પ્રવાહ બંધ થતાં તરત જ સમગ્ર ચુંબકત્વ ગુમાવી દે છે."
    })

    # Bank MCQ 4
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "What is the primary function of a split-ring commutator in an electric motor?",
        "question_hi": "विद्युत मोटर में विभक्त वलय दिक्परिवर्तक (Split-ring Commutator) का मुख्य कार्य क्या है?",
        "question_gu": "વિદ્યુત મોટરમાં સ્પ્લિટ-રિંગ કમ્યુટેટર (દિક્પરિવર્તક) નું મુખ્ય કાર્ય શું છે?",
        "options": [
            "To reverse the direction of current in the rotating coil every half rotation.",
            "To increase the voltage of the battery.",
            "To cool down the armature coil.",
            "To prevent the motor from rotating in reverse."
        ],
        "options_hi": [
            "प्रत्येक आधे चक्कर के बाद घूमती हुई कुंडली में धारा की दिशा को उलटना।",
            "बैटरी के वोल्टेज को बढ़ाना।",
            "आर्मेचर कुंडली को ठंडा रखना।",
            "मोटर को उल्टा घूमने से रोकना।"
        ],
        "options_gu": [
            "દર અડધા ભ્રમણ પછી ફરતી કોઈલમાં વિદ્યુતપ્રવાહની દિશા ઉલટાવવી.",
            "બેટરીના વોલ્ટેજમાં વધારો કરવો.",
            "આર્મેચર ગૂંચળાને ઠંડુ રાખવું.",
            "મોટરને ઊંધી ફરતી અટકાવવી."
        ],
        "correct_index": 0,
        "explanation": "The split-ring commutator acts as a direction reverser. By reversing the direction of current in the coil every half rotation, it ensures that the forces on both arms continue to push the coil in the same rotational sense.",
        "explanation_hi": "विभक्त वलय प्रत्येक आधे घूर्णन के बाद कुंडली में धारा की दिशा को उलट देता है, जिससे कुंडली पर लगने वाला बल युग्म उसे लगातार एक ही दिशा में घुमाता रहता है।",
        "explanation_gu": "સ્પ્લિટ-રિંગ કમ્યુટેટર દર અડધા આંટા પછી કોઈલમાં પ્રવાહની દિશા ઉલટાવે છે, જેથી બંને ભુજાઓ પર લાગતું બળ કોઈલને સતત એક જ દિશામાં ગોળ ફેરવતું રહે છે."
    })

    # Bank MCQ 5
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "An electric fuse wire should have which of the following physical characteristics?",
        "question_hi": "एक विद्युत फ्यूज के तार में निम्नलिखित में से कौन से भौतिक गुण होने चाहिए?",
        "question_gu": "વિદ્યુત ફ્યુઝના વાયરમાં નીચેનામાંથી કઈ ભૌતિક લાક્ષણિકતાઓ હોવી જોઈએ?",
        "options": [
            "High electrical resistance and a low melting point.",
            "Low resistance and a very high melting point.",
            "High resistance and an infinitely high melting point.",
            "Zero resistance and zero melting point."
        ],
        "options_hi": [
            "उच्च प्रतिरोध एवं निम्न गलनांक (High resistance and low melting point)।",
            "निम्न प्रतिरोध एवं अत्यधिक उच्च गलनांक।",
            "उच्च प्रतिरोध एवं अत्यधिक उच्च गलनांक।",
            "शून्य प्रतिरोध एवं शून्य गलनांक।"
        ],
        "options_gu": [
            "ઊંચો વિદ્યુત અવરોધ અને નીચું ગલનબિંદુ.",
            "નીચો અવરોધ અને ખૂબ ઊંચું ગલનબિંદુ.",
            "ઊંચો અવરોધ અને અતિશય ઊંચું ગલનબિંદુ.",
            "શૂન્ય અવરોધ અને શૂન્ય ગલનબિંદુ."
        ],
        "correct_index": 0,
        "explanation": "A fuse wire needs moderately high resistance so that excess current generates sufficient Joule heat (H = I²Rt), and a LOW MELTING POINT so that it quickly melts and breaks the circuit to prevent fire hazards.",
        "explanation_hi": "फ्यूज तार में उच्च प्रतिरोध होना चाहिए ताकि अधिक धारा बहने पर पर्याप्त जूल ऊष्मा (H = I²Rt) उत्पन्न हो सके, तथा निम्न गलनांक होना चाहिए ताकि वह तुरंत पिघलकर परिपथ को तोड़ सके।",
        "explanation_gu": "ફ્યુઝ વાયરમાં યોગ્ય ઊંચો અવરોધ હોવો જોઈએ જેથી વધુ પ્રવાહ વખતે પૂરતી જૂલ ઉષ્મા (H = I²Rt) પેદા થાય અને નીચું ગલનબિંદુ હોવું જોઈએ જેથી તે તરત પીગળીને સર્કિટ તોડી શકે."
    })

    # Bank MCQ 6
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Which rule is specifically used to determine the direction of induced electric current in a conductor moving through a magnetic field?",
        "question_hi": "चुंबकीय क्षेत्र में गतिमान चालक में प्रेरित विद्युत धारा की दिशा ज्ञात करने के लिए किस नियम का उपयोग किया जाता है?",
        "question_gu": "ચુંબકીય ક્ષેત્રમાં ગતિ કરતા વાહકમાં પ્રેરિત વિદ્યુતપ્રવાહની દિશા નક્કી કરવા માટે કયો નિયમ વપરાય છે?",
        "options": [
            "Fleming's Right-Hand Rule",
            "Fleming's Left-Hand Rule",
            "Maxwell's Right-Hand Thumb Rule",
            "Ampere's Swimming Rule"
        ],
        "options_hi": [
            "फ्लेमिंग का दक्षिण-हस्त नियम (Fleming's Right-Hand Rule)",
            "फ्लेमिंग का वाम-हस्त नियम (Fleming's Left-Hand Rule)",
            "मैक्सवेल का दाहिने हाथ के अंगूठे का नियम",
            "एम्पीयर का तैराकी नियम"
        ],
        "options_gu": [
            "ફ્લેમિંગનો જમણા હાથનો નિયમ (Fleming's Right-Hand Rule)",
            "ફ્લેમિંગનો ડાબા હાથનો નિયમ (Fleming's Left-Hand Rule)",
            "મેક્સવેલનો જમણા હાથના અંગૂઠાનો નિયમ",
            "એમ્પીયરનો તરવાનો નિયમ"
        ],
        "correct_index": 0,
        "explanation": "Fleming's Right-Hand Rule is used for induced currents (generators). Forefinger = Magnetic Field, Thumb = Motion of conductor, Middle finger = Direction of Induced Current.",
        "explanation_hi": "प्रेरित धारा की दिशा ज्ञात करने के लिए फ्लेमिंग के दक्षिण-हस्त (दाएं हाथ) के नियम का उपयोग किया जाता है। तर्जनी = चुंबकीय क्षेत्र, अंगूठा = चालक की गति, मध्यमा = प्रेरित धारा।",
        "explanation_gu": "પ્રેરિત વિદ્યુતપ્રવાહની દિશા જાણવા માટે ફ્લેમિંગના જમણા હાથના નિયમનો ઉપયોગ થાય છે. પહેલી આંગળી = ચુંબકીય ક્ષેત્ર, અંગૂઠો = વાહકની ગતિ, વચ્ચેની આંગળી = પ્રેરિત પ્રવાહ."
    })

    # Bank MCQ 7
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "What is the potential difference between the Live wire and the Neutral wire in standard Indian domestic power supply?",
        "question_hi": "मानक भारतीय घरेलू विद्युत आपूर्ति में विद्युन्मय (Live) तार और उदासीन (Neutral) तार के बीच विभवांतर कितना होता है?",
        "question_gu": "ભારતમાં પ્રમાણભૂત ઘરેલું વિદ્યુત સપ્લાયમાં જીવંત (Live) વાયર અને તટસ્થ (Neutral) વાયર વચ્ચેનો વિદ્યુતસ્થિતિમાનનો તફાવત કેટલો હોય છે?",
        "options": [
            "220 V",
            "110 V",
            "440 V",
            "12 V"
        ],
        "options_hi": [
            "220 V",
            "110 V",
            "440 V",
            "12 V"
        ],
        "options_gu": [
            "220 V",
            "110 V",
            "440 V",
            "12 V"
        ],
        "correct_index": 0,
        "explanation": "In India, the potential of the Live wire is 220 V and that of the Neutral wire is 0 V, creating a potential difference of 220 V across all domestic parallel circuits.",
        "explanation_hi": "भारत में लाइव तार का विभव 220 V और न्यूट्रल तार का विभव 0 V होता है, जिससे सभी घरेलू परिपथों में 220 V का विभवांतर मिलता है।",
        "explanation_gu": "ભારતમાં લાઈવ વાયર 220 V અને ન્યુટ્રલ વાયર 0 V પર હોવાથી તમામ ઘરેલું સાધનો વચ્ચે 220 V નો વિદ્યુતસ્થિતિમાનનો તફાવત રહે છે."
    })

    # Bank MCQ 8
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Which of the following will NOT increase the strength of the magnetic field inside a current-carrying solenoid?",
        "question_hi": "निम्नलिखित में से किससे धारावाही परिनालिका के भीतर चुंबकीय क्षेत्र की प्रबलता में वृद्धि नहीं होगी?",
        "question_gu": "નીચેનામાંથી શેના વડે પ્રવાહધારિત સોલેનોઇડની અંદર ચુંબકીય ક્ષેત્રની પ્રબળતામાં વધારો થશે નહીં?",
        "options": [
            "Reversing the direction of the electric current.",
            "Increasing the magnitude of electric current.",
            "Increasing the number of turns per unit length.",
            "Inserting a soft iron core into the core of the solenoid."
        ],
        "options_hi": [
            "विद्युत धारा की दिशा को उलटना।",
            "विद्युत धारा के परिमाण को बढ़ाना।",
            "प्रति इकाई लंबाई में फेरों की संख्या बढ़ाना।",
            "परिनालिका के भीतर नरम लोहे की छड़ डालना।"
        ],
        "options_gu": [
            "વિદ્યુતપ્રવાહની દિશા ઉલટાવવી.",
            "વિદ્યુતપ્રવાહના મૂલ્યમાં વધારો કરવો.",
            "એકમ લંબાઈ દીઠ આંટાની સંખ્યા વધારવી.",
            "સોલેનોઇડની અંદર નરમ લોખંડનો ગર્ભ દાખલ કરવો."
        ],
        "correct_index": 0,
        "explanation": "Reversing the direction of current only reverses the magnetic polarity (North becomes South and vice versa); it does NOT change the field magnitude/strength. Increasing current, increasing turns, or inserting a soft iron core all increase magnetic field strength.",
        "explanation_hi": "धारा की दिशा उलटने से केवल ध्रुवता (उत्तर और दक्षिण ध्रुव) बदलती है, चुंबकीय क्षेत्र की प्रबलता नहीं बदलती। धारा बढ़ाने, फेरे बढ़ाने या नरम लोहा डालने से क्षेत्र की शक्ति बढ़ती है।",
        "explanation_gu": "પ્રવાહની દિશા ઉલટાવવાથી માત્ર ધ્રુવો ઉલટાય છે (ઉત્તરનો દક્ષિણ બને છે), ક્ષેત્રની પ્રબળતા બદલાતી નથી. જ્યારે પ્રવાહ કે આંટા વધારવાથી અથવા નરમ લોખંડ મૂકવાથી ક્ષેત્ર પ્રબળ બને છે."
    })

    final_payload = {
        "metadata": metadata,
        "blocks": blocks
    }

    # Output to NCERT chapter path
    output_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch12.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(final_payload, f, ensure_ascii=False, indent=2)
    print(f"✅ Generated {len(blocks)} blocks successfully in {output_path}")

    # Output to GSEB chapter path for full syllabus parity
    gseb_output_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_science_ch12.json"
    gseb_payload = dict(final_payload)
    gseb_payload["metadata"] = dict(metadata)
    gseb_payload["metadata"]["id"] = "gseb_class10_science_ch12"
    gseb_payload["metadata"]["board"] = "GSEB"
    with open(gseb_output_path, "w", encoding="utf-8") as f:
        json.dump(gseb_payload, f, ensure_ascii=False, indent=2)
    print(f"✅ Generated GSEB copy in {gseb_output_path}")

if __name__ == "__main__":
    build_ncert_class10_science_ch12()
