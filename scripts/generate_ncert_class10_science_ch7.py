import json
import os

def build_ncert_class10_science_ch7():
    chapter_id = "ncert_class10_science_ch7"

    # =========================================================================
    # DIRECTIVE: EXTRACT EXISTING DATA AND TRANSLATIONS FROM EXISTING FILE
    # =========================================================================
    existing_file = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch7.json"
    existing_blocks_map = {}
    if os.path.exists(existing_file):
        try:
            with open(existing_file, "r", encoding="utf-8") as f:
                old_data = json.load(f)
                old_blocks = old_data.get("blocks", []) if isinstance(old_data, dict) else old_data
                for b in old_blocks:
                    bid = b.get("id")
                    if bid:
                        existing_blocks_map[bid] = b
            print(f"📖 Loaded {len(existing_blocks_map)} existing blocks from {existing_file}")
        except Exception as e:
            print(f"⚠️ Warning loading existing file: {e}")

    metadata = {
        "id": chapter_id,
        "title": "Chapter 7: How do Organisms Reproduce?",
        "title_hi": "अध्याय 7: जीव जनन कैसे करते हैं?",
        "title_gu": "પ્રકરણ 7: સજીવો કેવી રીતે પ્રજનન કરે છે?",
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
            "reproduction",
            "dna_copying",
            "variation",
            "asexual_reproduction",
            "binary_fission",
            "multiple_fission",
            "fragmentation",
            "regeneration",
            "budding",
            "vegetative_propagation",
            "spore_formation",
            "tissue_culture",
            "flower_structure",
            "pollination",
            "fertilization",
            "seed_germination",
            "puberty",
            "male_reproductive_system",
            "testosterone",
            "female_reproductive_system",
            "placenta",
            "menstruation",
            "contraception",
            "reproductive_health",
            "stds"
        ],
        "learning_outcomes": [
            "Explain why reproduction is essential for species continuity and how DNA copying produces variations necessary for survival.",
            "Compare and contrast all modes of asexual reproduction: binary fission, multiple fission, fragmentation, regeneration, budding, vegetative propagation, and spore formation.",
            "Describe the anatomy of a flower, differentiate unisexual and bisexual flowers, and trace pollination, pollen tube growth, fertilization, and seed/fruit formation.",
            "Analyze the changes during puberty and detail the structure and functions of male and female human reproductive systems.",
            "Explain the menstrual cycle, the site of fertilization, embryo nourishment through the placenta, and human gestation.",
            "Evaluate contraceptive methods (mechanical barriers, oral pills, IUCDs, surgical sterilization) and their role in family planning and STD prevention.",
            "Solve every NCERT in-text question and end-of-chapter textbook exercise with rigorous trilingual explanations."
        ],
        "ai_context": {
            "learning_goal": "Master NCERT Class 10 Chapter 7 (How do Organisms Reproduce?) through the 8-Step Gold Pedagogy Arc with 100% textbook syllabus and exercise coverage.",
            "common_misconceptions": [
                "Students think fertilization occurs in the uterus; fertilization occurs in the Fallopian tube (oviduct), while implantation occurs in the uterus.",
                "Students confuse regeneration with true reproduction; regeneration is accidental repair using specialized cells, not a planned mode of multiplication.",
                "Students believe vasectomy prevents fluid ejaculation; fluid from prostate and seminal vesicles is still ejaculated as semen, only sperm cells are absent.",
                "Students assume Copper-T protects against STDs; IUCDs only prevent pregnancy (implantation), while condoms protect against both pregnancy and STDs."
            ],
            "tutor_hint": "Always emphasize the dual role of variations in evolution and reinforce the exact sequence of events from pollination to seed formation."
        }
    }

    blocks = []
    block_counter = 1

    def next_id():
        nonlocal block_counter
        bid = f"KOBJ_NCERT_C10_SCI_CH7_{block_counter:03d}"
        block_counter += 1
        return bid

    # =========================================================================
    # MODULE 1: DNA COPYING & THE IMPORTANCE OF VARIATION (8-STEP PEDAGOGY)
    # =========================================================================

    # 1. Hook (Incorporating & Enhancing Existing Block 001)
    blocks.append({
        "id": next_id(),
        "type": "hook",
        "title": "The Purpose of Life: The Species Survival Imperative",
        "title_hi": "जीवन का उद्देश्य: प्रजाति के अस्तित्व की अनिवार्य आवश्यकता",
        "title_gu": "જીવનનો હેતુ: જાતિના અસ્તિત્વની અનિવાર્ય જરૂરિયાત",
        "body": "Before we ask how organisms reproduce, we must ask: WHY do they reproduce? Unlike nutrition, respiration, or excretion, reproduction is not necessary to maintain the life of an individual organism! An animal that never reproduces can live a full, healthy life. Yet creating a new individual consumes a massive amount of energy, nutrients, and biological risk. Why do all living creatures invest so heavily in a process they do not need to survive? Because if a species ceases to reproduce, every single member will die of age or predation, and that species will be erased from Earth forever!",
        "body_hi": "इससे पहले कि हम पूछें कि जीव कैसे प्रजनन करते हैं, हमें पूछना चाहिए: वे प्रजनन क्यों करते हैं? पोषण, श्वसन या उत्सर्जन के विपरीत, किसी व्यष्टि (individual) के जीवन को बनाए रखने के लिए प्रजनन आवश्यक नहीं है! जो जीव कभी प्रजनन नहीं करता, वह भी पूरा स्वस्थ जीवन जी सकता है। फिर भी नया जीव बनाने में भारी मात्रा में ऊर्जा और जैविक जोखिम लगता है। जीव उस प्रक्रिया में इतनी ऊर्जा क्यों लगाते हैं जिसकी उन्हें स्वयं जीवित रहने के लिए आवश्यकता नहीं है? क्योंकि यदि कोई प्रजाति प्रजनन बंद कर दे, तो उम्र या बीमारी से सभी सदस्य मर जाएंगे और वह प्रजाति हमेशा के लिए पृथ्वी से विलुप्त हो जाएगी!",
        "body_gu": "સજીવો પ્રજનન કેવી રીતે કરે છે તે પૂછતાં પહેલાં, આપણે પૂછવું જોઈએ: તેઓ પ્રજનન શા માટે કરે છે? પોષણ, શ્વસન કે ઉત્સર્જનથી વિપરીત, કોઈપણ સજીવને પોતાના વ્યક્તિગત જીવનને ટકાવી રાખવા માટે પ્રજનન જરૂરી નથી! જે સજીવ ક્યારેય પ્રજનન ન કરે તે પણ સંપૂર્ણ સ્વસ્થ જીવન જીવી શકે છે. તેમ છતાં નવો સજીવ ઉત્પન્ન કરવામાં પુષ્કળ ઊર્જા અને જૈવિક જોખમ રહેલું છે. સજીવો પોતાની જાતે જીવવા માટે જે પ્રક્રિયા જરૂરી નથી તેની પાછળ આટલી ઊર્જા શા માટે ખર્ચે છે? કારણ કે જો કોઈ જાતિ પ્રજનન બંધ કરે, તો તેના તમામ સભ્યો મૃત્યુ પામશે અને તે જાતિ પૃથ્વી પરથી સદાને માટે લુપ્ત થઈ જશે!"
    })

    # 2. Socratic Question (Incorporating & Enhancing Existing Block 002)
    blocks.append({
        "id": next_id(),
        "type": "socratic_question",
        "question": "When a single cell divides, it replicates its DNA blueprint to pass to the daughter cells. Is this biochemical copying mechanism 100% mathematically exact?",
        "question_hi": "जब कोई कोशिका विभाजित होती है, तो वह संतति कोशिकाओं को देने के लिए अपने डीएनए ब्लूप्रिंट की प्रतिलिपि बनाती है। क्या यह जैव रासायनिक नकल प्रक्रिया 100% गणितीय रूप से सटीक होती है?",
        "question_gu": "જ્યારે કોઈ કોષ વિભાજન પામે છે, ત્યારે તે બાળકોષોમાં વહન કરવા માટે પોતાના ડીએનએ બ્લૂપ્રિન્ટની નકલ બનાવે છે. શું આ જૈવરાસાયણિક નકલ પ્રક્રિયા 100% ગાણિતિક રીતે ભૂલરહિત હોય છે?",
        "options": [
            "No biochemical reaction is absolutely reliable; subtle copying errors inevitably occur, creating vital variations among offspring.",
            "Yes, DNA replication is an infallible mechanical process that always produces 100% identical atomic clones.",
            "DNA copying only occurs in complex mammals; bacteria and plants do not copy DNA.",
            "Cells do not copy DNA at all; they manufacture random new DNA from atmospheric gases."
        ],
        "options_hi": [
            "कोई भी जैव रासायनिक प्रक्रिया पूरी तरह से त्रुटिहीन नहीं होती; डीएनए की नकल में सूक्ष्म त्रुटियां स्वाभाविक रूप से होती हैं, जिससे संतति में महत्वपूर्ण विभिन्नताएं पैदा होती हैं।",
            "हाँ, डीएनए की नकल एक अचूक प्रक्रिया है जो हमेशा 100% सटीक क्लोन बनाती है।",
            "डीएनए की नकल केवल जटिल स्तनधारियों में होती है; बैक्टीरिया और पौधों में नहीं।",
            "कोशिकाएं डीएनए की नकल नहीं करतीं; वे वातावरण की गैसों से यादृच्छिक नया डीएनए बनाती हैं।"
        ],
        "options_gu": [
            "કોઈપણ જૈવરાસાયણિક પ્રક્રિયા સંપૂર્ણપણે વિશ્વસનીય હોતી નથી; ડીએનએ નકલ દરમિયાન સૂક્ષ્મ ભૂલો અનિવાર્યપણે થાય છે, જેનાથી સંતતિમાં મહત્વપૂર્ણ ભિન્નતાઓ સર્જાય છે.",
            "હા, ડીએનએ નકલ એ અચૂક પ્રક્રિયા છે જે હંમેશા 100% આબેહૂબ ક્લોન બનાવે છે.",
            "ડીએનએ નકલ માત્ર સસ્તન પ્રાણીઓમાં થાય છે; બેક્ટેરિયા કે વનસ્પતિમાં નહીં.",
            "કોષો ડીએનએ ની નકલ કરતા નથી; તેઓ હવામાંથી રેન્ડમ નવું ડીએનએ બનાવે છે."
        ],
        "correct_index": 0,
        "explanation": "No biochemical reaction is absolutely reliable. During DNA replication, subtle copying inaccuracies naturally occur. Consequently, the DNA copies generated are similar to the parent blueprint, but not absolutely identical. These built-in inaccuracies are called 'Variations'.",
        "explanation_hi": "कोई भी जैव रासायनिक प्रक्रिया पूर्णतः त्रुटिहीन नहीं होती। डीएनए प्रतिकृति के दौरान प्राकृतिक रूप से सूक्ष्म भिन्नताएं आती हैं। इसलिए बनी हुई डीएनए प्रतियां मूल डीएनए के समान तो होती हैं, परंतु हूबहू एक जैसी नहीं होतीं। इन अंतर्निहित परिवर्तनों को ही 'विभिन्नता (Variation)' कहा जाता है।",
        "explanation_gu": "કોઈપણ જૈવરાસાયણિક પ્રક્રિયા સંપૂર્ણપણે ભૂલરહિત હોતી નથી. ડીએનએ ની પ્રતિકૃતિ બનતી વખતે કુદરતી રીતે જ નાની ક્ષતિઓ થાય છે. પરિણામે ઉત્પન્ન થયેલ ડીએનએ નકલો મૂળ ડીએનએ જેવી હોય છે પરંતુ આબેહૂબ સરખી હોતી નથી. આ સૂક્ષ્મ ફેરફારોને 'ભિન્નતા (Variation)' કહેવામાં આવે છે."
    })

    # 3. Discovery
    blocks.append({
        "id": next_id(),
        "type": "discovery",
        "title": "The Dual Engines of Reproduction: DNA Blueprint & Cellular Apparatus",
        "title_hi": "प्रजनन के दोहरे इंजन: डीएनए ब्लूप्रिंट और कोशिकीय उपकरण",
        "title_gu": "પ્રજનનના બેવડા એન્જિન: ડીએનએ બ્લૂપ્રિન્ટ અને કોષીય સાધનસામગ્રી",
        "body": "Reproduction at its most fundamental molecular level involves two inseparable steps:\n\n1. Creating a DNA Copy: Chromosomes inside the nucleus contain information for inheritance of features from parents to next generation in the form of DNA (DeoxyriboNucleic Acid). DNA is the master information source for making proteins. If the information changes, different proteins will be made, leading to altered body designs.\n\n2. Creating Accompanying Cellular Machinery: A bare strand of copied DNA cannot survive on its own! It has no cytoplasm, no ribosomes, and no enzymes to sustain life. Therefore, DNA copying is always accompanied by the creation of an additional cellular apparatus. Only then does the cell divide to form two independent living units.",
        "body_hi": "आणविक स्तर पर प्रजनन में दो अनिवार्य चरण शामिल हैं:\n\n1. डीएनए की प्रतिलिपि बनाना: कोशिका के केंद्रक में मौजूद गुणसूत्रों (chromosomes) में माता-पिता से संतति में जाने वाली अनुवांशिक सूचना डीएनए (डीऑक्सीराइबोन्यूक्लिक अम्ल) के रूप में होती है। डीएनए प्रोटीन बनाने का मुख्य सूचना स्रोत है। यदि डीएनए बदलता है, तो बनने वाले प्रोटीन बदल जाएंगे, जिससे शारीरिक संरचना में बदलाव आएगा।\n\n2. अतिरिक्त कोशिकीय उपकरण का निर्माण: केवल अलग हुआ डीएनए का धागा अपने दम पर जीवित नहीं रह सकता! उसके पास कोशिकाद्रव्य, राइबोसोम या जीवन चलाने वाले एंजाइम नहीं होते। इसलिए डीएनए प्रतिलिपि के साथ-साथ पूरी कोशिकीय संरचना की भी दूसरी प्रति बनती है। तभी कोशिका विभाजित होकर दो स्वतंत्र जीवित कोशिकाएं बनाती है।",
        "body_gu": "આણ્વીય સ્તરે પ્રજનનમાં બે અનિવાર્ય પગલાંઓ સંકળાયેલા છે:\n\n1. ડીએનએ ની નકલ બનાવવી: કોષકેન્દ્રમાં રહેલા રંગસૂત્રોમાં પિતૃઓમાંથી પેઢીમાં વારસાગત લક્ષણો વહન કરતી માહિતી ડીએનએ (ડીઓક્સિરાઇબોન્યુક્લિક એસિડ) સ્વરૂપે હોય છે. ડીએનએ પ્રોટીન સંશ્લેષણ માટેનો મૂળભૂત સ્ત્રોત છે. જો માહિતી બદલાય, તો પ્રોટીન બદલાશે અને સજીવની શારીરિક રચના બદલાઈ જશે.\n\n2. કોષીય સંરચનાનું નિર્માણ: માત્ર છૂટો પડેલો ડીએનએ નો અણુ પોતાની જાતે જીવંત રહી શકતો નથી! તેની પાસે કોષરસ, રીબોઝોમ કે ચયાપચય માટેના ઉત્સેચકો હોતા નથી. તેથી ડીએનએ નકલની સાથે સાથે કોષીય સાધનસામગ્રીનું પણ સર્જન થાય છે. ત્યાર બાદ જ કોષ વિભાજિત થઈને બે સ્વતંત્ર સજીવ કોષો બનાવે છે."
    })

    # 4. Theory
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "The Importance of Variation for Species Survival",
        "title_hi": "प्रजातियों के अस्तित्व के लिए विभिन्नता का महत्व",
        "title_gu": "જાતિના અસ્તિત્વ માટે ભિન્નતાનું મહત્વ",
        "body": "Why are variations useful if they alter body design?\n\n• Populations of organisms live in well-defined places called niches in the ecosystem, using their specific body design.\n• However, niches can change drastically due to reasons beyond the organisms' control: temperatures may rise, water levels may drop, or a deadly new pathogen may strike.\n• If a population of reproducing organisms were suited to a particular niche and if that niche were drastically altered, the entire population could be wiped out completely!\n• But if some variations were present in a few individuals, there is a chance they might survive. \n\nClassic NCERT Example:\nIf there were a population of bacteria living in temperate water, and the water temperature increased drastically due to global warming, most of these bacteria would perish. But a few variants resistant to heat would survive and multiply, saving the species from total extinction!",
        "body_hi": "विभिन्नताएं प्रजाति के लिए क्यों उपयोगी हैं?\n\n• जीवों की आबादी अपने निश्चित शारीरिक डिजाइन का उपयोग करके पारिस्थितिकी तंत्र में विशेष स्थान (निकेत / Niche) में रहती है।\n• लेकिन निकेत में ऐसे भारी बदलाव आ सकते हैं जो जीवों के नियंत्रण से बाहर हों: जैसे वैश्विक तापमान बढ़ना, पानी का सूख जाना या किसी उल्कापिंड का प्रभाव।\n• यदि किसी प्रजाति के सभी सदस्य बिल्कुल एक जैसे हों और उनका निकेत बदल जाए, तो पूरी आबादी एक झटके में समाप्त हो जाएगी!\n• परंतु यदि आबादी के कुछ सदस्यों में थोड़ी विभिन्नता (variation) मौजूद हो, तो उनके जीवित बचने की संभावना होती है।\n\nNCERT का उत्कृष्ट उदाहरण:\nयदि शीतोष्ण जल में रहने वाले बैक्टीरिया की आबादी हो और ग्लोबल वार्मिंग के कारण पानी का तापमान अचानक बढ़ जाए, तो अधिकांश बैक्टीरिया मर जाएंगे। लेकिन गर्मी सहन करने की क्षमता वाले कुछ विभिन्नता युक्त बैक्टीरिया जीवित बच जाएंगे और आगे वंश चलाएंगे, जिससे प्रजाति विलुप्त होने से बच जाएगी!",
        "body_gu": "જો શારીરિક રચના બદલાય તો પણ ભિન્નતાઓ જાતિ માટે શા માટે ફાયદાકારક છે?\n\n• સજીવોની વસ્તી પોતાની વિશિષ્ટ શારીરિક રચના દ્વારા પરિસ્થિતિ તંત્રમાં ચોક્કસ વસવાટ (નિકેત / Niche) ધરાવે છે.\n• પરંતુ સજીવોના નિયંત્રણ બહારના કારણોસર વસવાટમાં મોટા ફેરફારો થઈ શકે છે: જેમ કે તાપમાનમાં વધારો, પાણીની અછત કે કોઈ ઘાતક વાયરસનો હુમલો.\n• જો સજીવોની વસ્તી સંપૂર્ણપણે એકસરખી હોય અને પર્યાવરણ બદલાય, તો સમગ્ર વસ્તી એકસાથે નાશ પામી શકે છે!\n• પરંતુ જો વસ્તીના અમુક સજીવોમાં ભિન્નતા રહેલી હોય, તો તેમના બચી જવાની શક્યતા રહે છે.\n\nNCERT નું ઉત્તમ ઉદાહરણ:\nજો સામાન્ય તાપમાનવાળા પાણીમાં રહેતા બેક્ટેરિયા હોય અને વૈશ્વિક તાપમાન વધવાથી પાણી ખૂબ ગરમ થઈ જાય, તો મોટાભાગના બેક્ટેરિયા મરી જશે. પરંતુ ગરમી સામે પ્રતિકારકતા ધરાવતા થોડા ભિન્નતાવાળા બેક્ટેરિયા જીવી જશે અને વૃદ્ધિ પામશે, જેથી બેક્ટેરિયાની જાતિ લુપ્ત થતી બચી જશે!"
    })

    # Teacher Tip
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Teacher Tip: Individual vs Species Perspective on Variation",
        "title_hi": "शिक्षक टिप: विभिन्नता का व्यक्तिगत बनाम प्रजाति परिप्रेक्ष्य",
        "title_gu": "શિક્ષક ટિપ: ભિન્નતાનો વ્યક્તિગત વિરુદ્ધ જાતિગત દ્રષ્ટિકોણ",
        "body": "Remember this critical exam distinction:\n• For an individual organism: A variation is often not necessary and can even be detrimental if it disrupts fine-tuned metabolic processes.\n• For the species as a whole: Variation is absolutely essential over evolutionary time! Without variation, a species has zero adaptive flexibility and will instantly go extinct during catastrophic ecological changes. Variation is the raw material for natural selection and evolution.",
        "body_hi": "परीक्षा के लिए यह महत्वपूर्ण अंतर हमेशा याद रखें:\n• किसी एक व्यष्टि (individual) के लिए: विभिन्नता आवश्यक नहीं है और कभी-कभी हानिकारक भी हो सकती है यदि वह शरीर के सामान्य कामकाज में बाधा डाले।\n• संपूर्ण प्रजाति (species) के लिए: विकासवादी समय में विभिन्नता अत्यंत आवश्यक है! बिना विभिन्नता के प्रजाति में अनुकूलन की कोई क्षमता नहीं होती और पर्यावरण बदलते ही वह विलुप्त हो जाती है। विभिन्नता ही प्राकृतिक चयन और जैव विकास का मूल आधार है।",
        "body_gu": "પરીક્ષા માટે આ મહત્ત્વનો તફાવત યાદ રાખો:\n• એક વ્યક્તિગત સજીવ માટે: ભિન્નતા હંમેશા જરૂરી હોતી નથી અને ક્યારેક નુકસાનકારક પણ હોઈ શકે છે.\n• સમગ્ર જાતિ માટે: લાંબા ગાળે ભિન્નતા અનિવાર્ય છે! ભિન્નતા વિના જાતિમાં પર્યાવરણ સાથે અનુકૂલન સાધવાની ક્ષમતા રહેતી નથી અને પર્યાવરણ બદલાતાં તે લુપ્ત થઈ જાય છે. ભિન્નતા એ કુદરતી પસંદગી અને ઉદવિકાસનો કાચો માલ છે."
    })

    # 5. Knowledge Check (MCQ)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "What is the primary reason why DNA copying in reproduction must be accompanied by the creation of an additional cellular apparatus?",
        "question_hi": "प्रजनन में डीएनए प्रतिलिपि के साथ-साथ अतिरिक्त कोशिकीय संरचना का निर्माण होना क्यों अनिवार्य है?",
        "question_gu": "પ્રજનનમાં ડીએનએ ની નકલની સાથે સાથે વધારાની કોષીય સાધનસામગ્રીનું સર્જન થવું શા માટે અનિવાર્ય છે?",
        "options": [
            "A bare DNA copy without cytoplasm, ribosomes, and metabolic machinery cannot independently survive and sustain life processes.",
            "DNA copying consumes all cellular nutrients and destroys the original nucleus.",
            "Cellular apparatus is needed only to increase the physical weight of the newly formed cell.",
            "DNA is made purely of water and will evaporate if not covered by a thick cell wall."
        ],
        "options_hi": [
            "कोशिकाद्रव्य, राइबोसोम और चयापचय तंत्र के बिना अकेला डीएनए स्वतंत्र रूप से जीवित नहीं रह सकता और जीवन प्रक्रियाओं को नहीं चला सकता।",
            "डीएनए की नकल से कोशिका के सारे पोषक तत्व नष्ट हो जाते हैं।",
            "कोशिकीय उपकरण केवल नए बने कोष्ठक का वजन बढ़ाने के लिए चाहिए।",
            "डीएनए केवल पानी का बना होता है और वाष्पीकृत हो सकता है।"
        ],
        "options_gu": [
            "કોષરસ, રીબોઝોમ અને ચયાપચય તંત્ર વિના માત્ર છૂટું ડીએનએ સ્વતંત્ર રીતે જીવંત રહી શકતું નથી અને જીવન ક્રિયાઓ ચલાવી શકતું નથી.",
            "ડીએનએ ની નકલ કોષના બધા પોષક તત્ત્વો વાપરી નાખે છે.",
            "કોષીય સાધનસામગ્રી માત્ર નવા કોષનું વજન વધારવા માટે જરૂરી છે.",
            "ડીએનએ માત્ર પાણીનું બનેલું હોવાથી બાષ્પીભવન પામી શકે છે."
        ],
        "correct_index": 0,
        "explanation": "DNA contains only the genetic code. It requires an organised cellular apparatus (cytoplasm, organelles, enzymes) to read that code, synthesize proteins, and perform metabolism. Hence, cell division always partitions both DNA and cellular machinery.",
        "explanation_hi": "डीएनए में केवल आनुवंशिक कूट (code) होता है। उस कूट को पढ़ने, प्रोटीन बनाने और उपापचय चलाने के लिए सुव्यवस्थित कोशिकीय उपकरण आवश्यक है। इसलिए कोशिका विभाजन में डीएनए और कोशिकीय मशीनरी दोनों का निर्माण होता है।",
        "explanation_gu": "ડીએનએ માત્ર જનીનિક સંકેતો ધરાવે છે. તે સંકેતોને વાંચવા, પ્રોટીન બનાવવા અને ચયાપચય ચલાવવા સુવ્યવસ્થિત કોષીય રચના જરૂરી છે. આથી કોષ વિભાજનમાં ડીએનએ અને કોષીય સાધનસામગ્રી બંનેનું વિભાજન થાય છે."
    })

    # 6. Reflection
    blocks.append({
        "id": next_id(),
        "type": "reflection",
        "title": "Why Pure Clones are at Risk in a Changing World",
        "title_hi": "बदलती दुनिया में शत-प्रतिशत क्लोन पर भारी खतरा क्यों होता है?",
        "title_gu": "બદલાતી દુનિયામાં શુદ્ધ ક્લોન પર મોટું જોખમ કેમ રહેલું છે?",
        "body": "Consider commercial Cavendish bananas grown worldwide: virtually every Cavendish banana plant is a sterile genetic clone reproduced by vegetative suckers. Because there is virtually zero genetic variation among millions of plants, a single fungal disease (Panama Tropical Race 4) threatens to wipe out global commercial banana production! This real-world crisis illustrates why sexual reproduction and variations are nature's insurance policy against global catastrophe.",
        "body_hi": "दुनिया भर में उगाए जाने वाले कैवेंडिश केलों पर विचार करें: लगभग हर कैवेंडिश केले का पौधा अलैंगिक रूप से तैयार किया गया एक समान क्लोन है। लाखों पौधों में आनुवंशिक विविधता शून्य होने के कारण, पनामा ट्रॉपिकल रेस 4 नामक एक अकेला कवक रोग पूरी दुनिया के केला उद्योग को समाप्त करने की कगार पर ला चुका है! यह वास्तविक संकट दिखाता है कि विभिन्नताएं प्रकृति द्वारा प्रजातियों को विनाश से बचाने की सबसे बड़ी बीमा पॉलिसी हैं।",
        "body_gu": "વિશ્વભરમાં વવાતા કેવેન્ડિશ કેળાં વિશે વિચારો: લગભગ દરેક કેળ એ વાનસ્પતિક રીતે ઉગાડવામાં આવેલો આબેહૂબ ક્લોન છે. લાખો છોડવાઓમાં જનીનિક ભિન્નતા શૂન્ય હોવાને કારણે, પનામા ટ્રોપિકલ રેસ 4 નામનો એક ફૂગજન્ય રોગ સમગ્ર વિશ્વના કેળાંના પાકને નષ્ટ કરી શકે તેમ છે! આ વાસ્તવિક ઘટના દર્શાવે છે કે લિંગી પ્રજનન અને ભિન્નતાઓ એ કુદરત દ્વારા જાતિને સામૂહિક વિનાશથી બચાવવા માટેની શ્રેષ્ઠ વીમા પોલિસી છે."
    })

    # 7. Connection
    blocks.append({
        "id": next_id(),
        "type": "connection",
        "title": "From Cellular Division to Evolution and Biotechnology",
        "title_hi": "कोशिका विभाजन से जैव विकास और जैव प्रौद्योगिकी तक का संबंध",
        "title_gu": "કોષ વિભાજનથી ઉદવિકાસ અને બાયોટેકનોલોજી સાથેનો સંબંધ",
        "body": "The subtle DNA copying variations introduced during reproduction form the fundamental bedrock for Charles Darwin's Theory of Natural Selection. In modern biotechnology, geneticists intentionally introduce targeted variations using CRISPR gene editing to create drought-resistant crops, disease-resistant livestock, and personalized gene therapies for human hereditary disorders.",
        "body_hi": "प्रजनन के दौरान डीएनए की नकल में होने वाली सूक्ष्म विभिन्नताएं ही चार्ल्स डार्विन के प्राकृतिक चयन द्वारा जैव विकास के सिद्धांत का मूल आधार हैं। आधुनिक जैव प्रौद्योगिकी में, वैज्ञानिक CRISPR जीन एडिटिंग तकनीक द्वारा जानबूझकर पौधों में सूखे और कीटों से लड़ने वाली विभिन्नताएं उत्पन्न कर रहे हैं।",
        "body_gu": "પ્રજનન દરમિયાન ડીએનએ નકલમાં થતી સૂક્ષ્મ ભિન્નતાઓ ચાર્લ્સ ડાર્વિનના કુદરતી પસંદગી દ્વારા ઉદવિકાસના સિદ્ધાંતનો પાયો છે. આધુનિક બાયોટેકનોલોજીમાં, વૈજ્ઞાનિકો CRISPR જનીન સંશોધન દ્વારા દુષ્કાળ-પ્રતિકારક પાક અને રોગ-પ્રતિકારક જાતો વિકસાવવા માટે નિયંત્રિત ભિન્નતાઓ દાખલ કરે છે."
    })

    # 8. Mastery Challenge (MCQ)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Which of the following statements best explains why variation is beneficial to the species, even if not necessarily for an individual?",
        "question_hi": "निम्नलिखित में से कौन सा कथन यह स्पष्ट करता है कि विभिन्नता व्यष्टि के लिए आवश्यक न होते हुए भी प्रजाति के लिए क्यों लाभकारी है?",
        "question_gu": "નીચેનામાંથી કયું વિધાન સ્પષ્ટ કરે છે કે ભિન્નતા વ્યક્તિગત સજીવ માટે જરૂરી ન હોવા છતાં જાતિ માટે શા માટે ફાયદાકારક છે?",
        "options": [
            "Variations give the entire population a buffer of genetic diversity so that unexpected environmental shifts do not cause total extinction.",
            "Variations ensure that every individual lives longer than its parents.",
            "Variations prevent any individual organism from ever getting sick.",
            "Variations guarantee that all offspring look completely different from the species."
        ],
        "options_hi": [
            "विभिन्नताएं पूरी आबादी को आनुवंशिक विविधता की सुरक्षा देती हैं ताकि अचानक आए पर्यावरणीय बदलाव से पूरी प्रजाति एक साथ विलुप्त न हो जाए।",
            "विभिन्नताएं यह सुनिश्चित करती हैं कि प्रत्येक व्यक्ति अपने माता-पिता से अधिक लंबा जीवन जिए।",
            "विभिन्नताएं किसी भी जीव को कभी बीमार नहीं पड़ने देतीं।",
            "विभिन्नताएं यह गारंटी देती हैं कि सभी बच्चे प्रजाति से पूरी तरह अलग दिखें।"
        ],
        "options_gu": [
            "ભિન્નતાઓ સમગ્ર વસ્તીને જનીનિક વિવિધતાનું સુરક્ષા કવચ પૂરું પાડે છે જેથી અચાનક પર્યાવરણીય પલટો આવતાં સમગ્ર જાતિ એકસાથે લુપ્ત ન થઈ જાય.",
            "ભિન્નતાઓ ખાતરી આપે છે કે દરેક વ્યક્તિ પોતાના પિતૃઓ કરતાં વધુ જીવે.",
            "ભિન્નતાઓ કોઈપણ સજીવને ક્યારેય બીમાર પડવા દેતી નથી.",
            "ભિન્નતાઓ ખાતરી આપે છે કે બધી સંતતિ મૂળ જાતિ કરતાં તદ્દન અલગ દેખાય."
        ],
        "correct_index": 0,
        "explanation": "A single individual might not benefit or may even struggle with a variation. But across thousands of individuals in a species, having diverse variants ensures that if climate, predators, or diseases alter the niche, some individuals will survive to propagate the species.",
        "explanation_hi": "किसी एक व्यक्ति को विभिन्नता से सीधा लाभ न भी मिले, परंतु हजारों जीवों की आबादी में विभिन्नताएं यह सुनिश्चित करती हैं कि विपरीत परिस्थितियों में भी कुछ सदस्य जीवित रहकर प्रजाति का अस्तित्व बनाए रखेंगे।",
        "explanation_gu": "કોઈ એક વ્યક્તિગત સજીવને ભિન્નતાથી સીધો ફાયદો ન પણ થાય, પરંતુ લાખો સજીવોની વસ્તીમાં વિવિધતા એ સુનિશ્ચિત કરે છે કે પ્રતિકૂળ સંજોગોમાં પણ કેટલાક સભ્યો બચી જઈને જાતિનું અસ્તિત્વ ટકાવી રાખશે."
    })

    # =========================================================================
    # MODULE 2: MODES OF ASEXUAL REPRODUCTION (8-STEP PEDAGOGY)
    # =========================================================================

    # 1. Hook
    blocks.append({
        "id": next_id(),
        "type": "hook",
        "title": "The Organism That Defies Death by Slicing",
        "title_hi": "वह जीव जो कटने पर भी मृत्यु को मात दे देता है",
        "title_gu": "એ સજીવ જે ટુકડા થવા છતાં મૃત્યુને માત આપે છે",
        "body": "If you cut an earthworm in half, only one end might survive. If you cut a mammal in half, it dies immediately. But if you take a tiny freshwater flatworm called Planaria and cut it horizontally, vertically, or into ten random pieces, something incredible happens: every single piece grows its own head, eyespots, brain, gut, and tail, transforming into ten complete, crawling flatworms! How do simple creatures perform such biological miracles without needing a partner?",
        "body_hi": "यदि आप केंचुए को दो टुकड़ों में काट दें, तो शायद केवल एक हिस्सा ही बचे। किसी स्तनपायी के दो टुकड़े करने पर उसकी तुरंत मृत्यु हो जाती है। लेकिन यदि आप मीठे पानी के चपटे कृमि 'प्लेनेरिया' (Planaria) को लें और उसे क्षैतिज, लंबवत या दस टुकड़ों में काट दें, तो एक अविश्वसनीय घटना घटती है: हर एक टुकड़ा अपना सिर, आंखें, मस्तिष्क और पूंछ फिर से उगाकर दस पूर्ण जीवित प्लेनेरिया में बदल जाता है! आखिर सरल जीव बिना किसी साथी के ऐसे चमत्कारी प्रजनन कैसे कर लेते हैं?",
        "body_gu": "જો તમે અળસિયાના બે ટુકડા કરો, તો કદાચ એક જ છેડો જીવી શકે. પરંતુ જો તમે પ્લેનેરિયા (Planaria) નામના ચપટા કૃમિના આડા, ઊભા કે દસ ટુકડા કરી નાખો, તો એક અદભુત ઘટના બને છે: દરેક ટુકડો પોતાનું નવું માથું, આંખો, મગજ અને પૂંછડી વિકસાવીને દસ સંપૂર્ણ પ્લેનેરિયા બની જાય છે! સરળ સજીવો કોઈ બીજા સાથી વગર આવા જૈવિક ચમત્કારો કેવી રીતે કરી શકે છે?"
    })

    # 2. Socratic Question
    blocks.append({
        "id": next_id(),
        "type": "socratic_question",
        "question": "Why can simple organisms like Spirogyra or Planaria reproduce by simply breaking or regenerating from fragments, while complex multicellular organisms like dogs and humans cannot?",
        "question_hi": "स्पाइरोगायरा या प्लेनेरिया जैसे सरल जीव टुकड़ों में टूटकर या पुनरुद्भवन द्वारा नया जीव बना सकते हैं, जबकि कुत्ते और मानव जैसे जटिल बहुकोशिकीय जीव ऐसा क्यों नहीं कर सकते?",
        "question_gu": "સ્પાયરોગાયરા કે પ્લેનેરિયા જેવા સરળ સજીવો ટુકડાઓમાં તૂટીને કે પુનઃસર્જન દ્વારા નવો સજીવ બનાવી શકે છે, જ્યારે કૂતરા કે માનવી જેવા જટિલ બહુકોષી સજીવો આવું કેમ કરી શકતા નથી?",
        "options": [
            "Complex organisms possess highly specialized organ systems arranged in precise hierarchical layers; skin or muscle cells cannot spontaneously reconstitute a missing heart, brain, or lungs.",
            "Complex organisms do not have DNA inside their cells.",
            "Complex organisms have bones which completely prevent any cell division.",
            "Simple organisms do not need oxygen or nutrition to stay alive."
        ],
        "options_hi": [
            "जटिल जीवों में अत्यधिक विशिष्ट अंग प्रणालियां होती हैं; त्वचा या मांसपेशी की कोशिकाएं हृदय, मस्तिष्क या फेफड़े जैसे जटिल अंग अपने आप नहीं बना सकतीं।",
            "जटिल जीवों की कोशिकाओं में डीएनए नहीं होता।",
            "जटिल जीवों में हड्डियां होती हैं जो कोशिका विभाजन को पूरी तरह रोक देती हैं।",
            "सरल जीवों को जीवित रहने के लिए ऑक्सीजन या पोषण की आवश्यकता नहीं होती।"
        ],
        "options_gu": [
            "જટિલ સજીવોમાં અત્યંત વિશિષ્ટ અંગતંત્રો ક્રમબદ્ધ રચના ધરાવે છે; ચામડી કે સ્નાયુના કોષો પોતાની મેળે હૃદય, મગજ કે ફેફસાં જેવા જટિલ અંગો પુનઃ બનાવી શકતા નથી.",
            "જટિલ સજીવોના કોષોમાં ડીએનએ હોતું નથી.",
            "જટિલ સજીવોમાં હાડકાં હોય છે જે કોષ વિભાજનને અટકાવે છે.",
            "સરલ સજીવોને જીવવા માટે ઓક્સિજન કે પોષણની જરૂર હોતી નથી."
        ],
        "correct_index": 0,
        "explanation": "In simple organisms, cells are not heavily differentiated; specialized regenerative cells can proliferate and form all cell types. In complex animals, extensive differentiation organizes tissues into specific organ systems. Cell-by-cell division cannot regenerate an entire integrated body.",
        "explanation_hi": "सरल जीवों में कोशिकाएं अत्यधिक विभेदित नहीं होतीं; विशेष पुनरुद्भवन कोशिकाएं विभाजित होकर सभी प्रकार की कोशिकाएं बना सकती हैं। जटिल जीवों में ऊतक विशिष्ट अंगों में व्यवस्थित होते हैं, अतः मात्र किसी एक ऊतक से पूरा जीव नहीं बन सकता।",
        "explanation_gu": "સરળ સજીવોમાં કોષોનું બહુ મોટું વિભેદન હોતું નથી; વિશિષ્ટ પુનઃસર્જન કોષો વિભાજિત થઈને કોઈપણ પેશી રચી શકે છે. જટિલ પ્રાણીઓમાં વિશિષ્ટ પેશીઓ અંગતંત્રોમાં ગોઠવાયેલી હોવાથી માત્ર કોઈ એક ભાગમાંથી આખો સજીવ બનવો અશક્ય છે."
    })

    # 3. Discovery
    blocks.append({
        "id": next_id(),
        "type": "discovery",
        "title": "The Master Taxonomy of Asexual Reproduction",
        "title_hi": "अलैंगिक प्रजनन का संपूर्ण वर्गीकरण",
        "title_gu": "અલિંગી પ્રજનનનું સંપૂર્ણ વર્ગીકરણ",
        "body": "Asexual reproduction involves only a SINGLE parent without the fusion of gametes, producing genetically identical offspring (clones). Here are all six textbook modes:\n\n1. Fission:\n   • Binary Fission: Organism splits into two halves. Amoeba splits in any plane. Leishmania (causes Kala-azar) has a whip-like flagellum at one end and splits longitudinally in a definite orientation.\n   • Multiple Fission: Single cell divides into many daughter cells simultaneously inside a protective cyst (e.g. Plasmodium, the malarial parasite).\n\n2. Fragmentation: In simple multicellular filamentous organisms like Spirogyra, mature filaments break into small fragments, and each fragment grows by cell division into a new filament.\n\n3. Regeneration: Organisms like Planaria and Hydra, when cut into pieces, use specialized regenerative cells to proliferate, mass-differentiate, and regrow missing organs.\n\n4. Budding: A small outgrowth (bud) develops due to repeated cell division at one specific site. It matures, develops miniature tentacles and mouth, and detaches (Hydra, Yeast).\n\n5. Vegetative Propagation: In plants, new individuals arise from vegetative parts (roots, stems, leaves) naturally (Bryophyllum leaf notches, potato eyes) or artificially (grafting, layering).\n\n6. Spore Formation: In fungi like Rhizopus (bread mould), thread-like structures called hyphae produce knob-like sporangia containing hundreds of microscopic spores covered by thick protective walls resistant to drought and heat.",
        "body_hi": "अलैंगिक प्रजनन में युग्मकों के संलयन के बिना केवल एक ही जनक भाग लेता है। इसके सभी 6 मुख्य तरीके निम्न हैं:\n\n1. विखंडन (Fission):\n   • द्विखंडन (Binary Fission): एक कोशिका दो में बंटती है। अमीबा किसी भी तल में विभाजित होता है। लीशमैनिया (कालाजार का कारक) में एक सिरे पर कोड़े जैसी संरचना होती है और वह निश्चित तल में विभाजित होता है।\n   • बहुखंडन (Multiple Fission): प्रतिकूल परिस्थितियों में सिस्ट के अंदर कोशिका एक साथ कई संतति कोशिकाओं में बंट जाती है (जैसे प्लाज्मोडियम)।\n\n2. खंडन (Fragmentation): स्पाइरोगायरा जैसे सरल तंतुमय शैवाल परिपक्व होने पर छोटे टुकड़ों में टूट जाते हैं और प्रत्येक टुकड़ा वृद्धि करके नया शैवाल बन जाता है।\n\n3. पुनरुद्भवन (Regeneration): प्लेनेरिया और हाइड्रा को काटने पर विशेष पुनरुद्भवन कोशिकाएं तेजी से विभाजित होकर छूटे हुए अंगों का पुनर्निर्माण कर देती हैं।\n\n4. मुकुलन (Budding): हाइड्रा या यीस्ट के शरीर पर एक उभार (मुकुल) बनता है जो विकसित होकर जनक से अलग हो जाता है।\n\n5. कायिक प्रवर्धन (Vegetative Propagation): पौधों में जड़, तना या पत्तियों से नया पौधा बनना (जैसे ब्रायोफिलम की पत्तियां, आलू की आंखें)।\n\n6. बीजाणु समासंघ (Spore Formation): राइजोपस (ब्रेड मोल्ड) में बीजाणुधानी के अंदर मोटी सुरक्षात्मक भित्ति वाले सैकड़ों बीजाणु बनते हैं जो अनुकूल परिस्थितियों में अंकुरित होते हैं।",
        "body_gu": "અલિંગી પ્રજનનમાં જન્યુઓના જોડાણ વિના માત્ર એક જ પિતૃ ભાગ લે છે. તેના 6 મુખ્ય પ્રકારો:\n\n1. ભાજન (Fission):\n   • દ્વિભાજન: અમીબા કોઈપણ સમતલમાં વિભાજિત થાય છે. લેશમાનિયા (કાલા-અઝાર રોગનો કારક) એક છેડે ચાબૂક જેવી રચના ધરાવે છે અને ચોક્કસ સપાટી પર વિભાજિત થાય છે.\n   • બહુભાજન: કોષ અનુકૂળ ન હોય ત્યારે કોથળીમાં એકસાથે અનેક બાળકોષોમાં વિભાજિત થાય છે (દા.ત. પ્લાઝમોડિયમ).\n\n2. અવખંડન (Fragmentation): સ્પાયરોગાયરા જેવા સરળ તંતુમય સજીવો પુખ્ત થતાં ટુકડાઓમાં તૂટે છે અને દરેક ટુકડો નવો સજીવ બને છે.\n\n3. પુનઃસર્જન (Regeneration): પ્લેનેરિયા અને હાઇડ્રા કપાઈ જતાં વિશિષ્ટ કોષોના વિભાજનથી ખૂટતા અંગો પુનઃ બનાવી લે છે.\n\n4. કલિકાસર્જન (Budding): હાઇડ્રા કે યીસ્ટમાં ઉપસેલો ભાગ (કલિકા) પુખ્ત થઈ પિતૃથી છૂટો પડે છે.\n\n5. વાનસ્પતિક પ્રજનન: મૂળ, પ્રકાંડ કે પર્ણોમાંથી નવા છોડનું સર્જન (દા.ત. પાનફૂટીના પર્ણો, બટાટાની આંખો).\n\n6. બીજાણુ નિર્માણ (Spore Formation): રાઇઝોપસ (બ્રેડ મોલ્ડ) ની બીજાણુધાનીમાં જાડી રક્ષણાત્મક દીવાલવાળા અસંખ્ય બીજાણુઓ બને છે જે હવામાં ફેલાય છે."
    })

    # 4. Theory: Deep-dive into Vegetative Propagation & Tissue Culture
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "Vegetative Propagation and Artificial Tissue Culture",
        "title_hi": "कायिक प्रवर्धन और कृत्रिम ऊतक संवर्धन",
        "title_gu": "વાનસ્પતિક પ્રજનન અને કૃત્રિમ પેશી સંવર્ધન",
        "body": "Vegetative propagation is widely exploited in agriculture and horticulture:\n\n1. Natural Vegetative Structures:\n   • Roots: Sweet potato, Dahlia.\n   • Stems: Potato tubers (germinating 'eyes' or buds), Ginger rhizome, Onion bulb, Strawberry runners.\n   • Leaves: Bryophyllum (sprout leaf plant) forms adventitious buds along the notches of its leaf margins. When leaves fall on moist soil, each bud develops roots and grows into an independent plant!\n\n2. Artificial Techniques:\n   • Cutting: Sugarcane, rose.\n   • Layering: Jasmine (bending a lower branch to touch moist soil until it roots).\n   • Grafting: Mango, apple, rose (joining scion of desired flower/fruit with sturdy rootstock).\n\n3. Tremendous Benefits of Vegetative Propagation:\n   • Plants raised this way bear flowers and fruits much earlier than those grown from seeds.\n   • Enables propagation of seedless varieties like banana, seedless grapes, orange, rose, and jasmine.\n   • All offspring are genetically identical clones, preserving desirable high-yield parent traits.\n\n4. Tissue Culture (Micropropagation):\n   • Growing plant cells/tissues in an artificial nutrient medium under sterile conditions.\n   • A small piece from the growing tip (shoot apex) is placed on nutrient medium containing plant hormones, forming an unorganized dividing cell mass called a Callus.\n   • Callus is transferred to differentiation hormone medium, producing tiny plantlets which are potted in soil.\n   • Advantage: Thousands of disease-free plants can be grown from a single parent in very short time.",
        "body_hi": "कृषि और बागवानी में कायिक प्रवर्धन का व्यापक उपयोग किया जाता है:\n\n1. प्राकृतिक कायिक अंग:\n   • जड़ें: शकरकंद, डहलिया।\n   • तना: आलू के कंद (आलू की कलिकाएं या 'आंखें'), अदरक का प्रकंद, प्याज, स्ट्रॉबेरी।\n   • पत्तियां: ब्रायोफिलम (अजूबा/पत्थरचट्टा) की पत्तियों के किनारों के खांचों में कलिकाएं होती हैं। पत्ती के गीली मिट्टी पर गिरते ही ये कलिकाएं नए पौधे बना लेती हैं!\n\n2. कृत्रिम तकनीकें: कलम लगाना (गुलाब), दाब लगाना (चमेली), और रोपण/ग्राफ्टिंग (आम, सेब)।\n\n3. कायिक प्रवर्धन के मुख्य लाभ:\n   • बीज से उगने वाले पौधों की तुलना में इनमें फूल और फल बहुत पहले आ जाते हैं।\n   • केला, संतरा, गुलाब और चमेली जैसे बीजहीन पौधों को उगाने का यह एकमात्र तरीका है।\n   • सभी पौधे आनुवंशिक रूप से बिल्कुल जनक के समान होते हैं, जिससे उत्तम गुण बरकरार रहते हैं।\n\n4. ऊतक संवर्धन (Tissue Culture):\n   • पौधे के बढ़ते अग्रभाग (meristem) से कोशिकाओं को निकालकर रोगाणुरहित पोषक माध्यम में रखा जाता है।\n   • कोशिकाएं विभाजित होकर 'कैलस' (Callus) नामक कोशिकाओं का समूह बनाती हैं।\n   • कैलस को हार्मोन युक्त माध्यम में रखकर छोटे पौधे (plantlets) तैयार किए जाते हैं।\n   • लाभ: अत्यंत कम समय में एक ही पौधे से हजारों रोगमुक्त पौधे उगाए जा सकते हैं।",
        "body_gu": "કૃષિ અને બાગાયતમાં વાનસ્પતિક પ્રજનનનો વ્યાપક ઉપયોગ થાય છે:\n\n1. કુદરતી વાનસ્પતિક અંગો:\n   • મૂળ: શક્કરિયાં, ડહાલિયા.\n   • પ્રકાંડ: બટાટા (કલિકાઓ કે 'આંખો'), આદુ, ડુંગળી, સ્ટ્રોબેરી.\n   • પર્ણો: પાનફૂટી (બ્રાયોફિલમ) ના પર્ણની કિનારીની ખાંચોમાં કલિકાઓ હોય છે. પર્ણ ભીની જમીન પર પડતાં જ તેમાંથી નવો છોડ ઊગી નીકળે છે!\n\n2. કૃત્રિમ પદ્ધતિઓ: કલમ કરવી (ગુલાબ), દાબકલમ (ચમેલી), આરોપણ (કેરી, સફરજન).\n\n3. વાનસ્પતિક પ્રજનનના ફાયદા:\n   • બીજમાંથી ઊગતા છોડ કરતાં આ પદ્ધતિથી ફૂલો અને ફળો ખૂબ ઝડપથી આવે છે.\n   • કેળાં, ગુલાબ, દ્રાક્ષ અને મોગરા જેવી બીજવિહીન જાતોનું વાવેતર શક્ય બને છે.\n   • બધા છોડ પિતૃ જેવા જ ઉત્તમ લક્ષણો ધરાવતા આબેહૂબ ક્લોન હોય છે.\n\n4. પેશી સંવર્ધન (Tissue Culture):\n   • વનસ્પતિના વધતા અગ્રભાગમાંથી પેશી લઈને જંતુરહિત પોષક માધ્યમમાં ઉછેરવામાં આવે છે.\n   • કોષો વિભાજિત થઈને 'કેલસ' (Callus) નામનો અસંગઠિત કોષસમૂહ રચે છે.\n   • કેલસને અંતઃસ્ત્રાવોવાળા માધ્યમમાં મૂકી નાના રોપાઓ તૈયાર કરી કૂંડામાં રોપાય છે.\n   • ફાયદો: ખૂબ ઓછા સમયમાં એક જ છોડમાંથી હજારો રોગમુક્ત છોડવાઓ મેળવી શકાય છે."
    })

    # Teacher Tip
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Teacher Tip: Binary Fission Differences - Amoeba vs Leishmania",
        "title_hi": "शिक्षक टिप: द्विखंडन में अंतर - अमीबा बनाम लीशमैनिया",
        "title_gu": "શિક્ષક ટિપ: દ્વિભાજનમાં તફાવત - અમીબા વિરુદ્ધ લેશમાનિયા",
        "body": "In board examinations, examiners frequently ask how binary fission in Amoeba differs from that in Leishmania:\n• Amoeba has no fixed shape, so splitting can happen along ANY plane.\n• Leishmania has a definite body shape with a whip-like flagellum at one end. Splitting happens strictly in a definite longitudinal orientation relative to this structure.\nAlways include this structural difference for full marks!",
        "body_hi": "बोर्ड परीक्षाओं में परीक्षक अक्सर पूछते हैं कि अमीबा और लीशमैनिया के द्विखंडन में क्या अंतर है:\n• अमीबा का कोई निश्चित आकार नहीं होता, इसलिए कोशिका विभाजन किसी भी तल में हो सकता है।\n• लीशमैनिया का निश्चित आकार होता है और एक सिरे पर कोड़े जैसी कशाभिका (flagellum) होती है। इसमें विभाजन केवल एक विशिष्ट अनुदैर्ध्य (longitudinal) तल में ही होता है।\nपूरे अंक प्राप्त करने के लिए यह अंतर अवश्य लिखें!",
        "body_gu": "બોર્ડ પરીક્ષામાં અવારનવાર પૂછાતો પ્રશ્ન: અમીબા અને લેશમાનિયાના દ્વિભાજન વચ્ચેનો તફાવત:\n• અમીબા અનિયમિત આકાર ધરાવે છે, તેથી તેનું વિભાજન કોઈપણ સમતલમાં થઈ શકે છે.\n• લેશમાનિયા ચોક્કસ આકાર અને એક છેડે ચાબૂક જેવી કશા ધરાવે છે. તેનું વિભાજન આ કશાના સંદર્ભમાં ચોક્કસ આયામ સમતલમાં જ થાય છે.\nપૂરા ગુણ મેળવવા આ વિગત અવશ્ય લખવી!"
    })

    # 5. Knowledge Check (MCQ)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Which of the following organisms reproduces by multiple fission inside a protective cyst under unfavorable conditions?",
        "question_hi": "निम्नलिखित में से कौन सा जीव प्रतिकूल परिस्थितियों में सुरक्षात्मक सिस्ट के अंदर बहुखंडन द्वारा प्रजनन करता है?",
        "question_gu": "નીચેનામાંથી કયો સજીવ પ્રતિકૂળ સંજોગોમાં રક્ષણાત્મક કોથળીની અંદર બહુભાજન દ્વારા પ્રજનન કરે છે?",
        "options": [
            "Plasmodium (the malarial parasite)",
            "Amoeba proteus",
            "Planaria torva",
            "Hydra vulgaris"
        ],
        "options_hi": [
            "प्लाज्मोडियम (मलेरिया परजीवी)",
            "अमीबा",
            "प्लेनेरिया",
            "हाइड्रा"
        ],
        "options_gu": [
            "પ્લાઝમોડિયમ (મેલેરિયા પરજીવી)",
            "અમીબા",
            "પ્લેનેરિયા",
            "હાઇડ્રા"
        ],
        "correct_index": 0,
        "explanation": "Plasmodium, a single-celled protozoan parasite, divides into many daughter cells simultaneously inside a protective wall (cyst) through multiple fission. When the cyst ruptures, numerous parasites are released at once.",
        "explanation_hi": "प्लाज्मोडियम बहुखंडन (Multiple Fission) द्वारा एक सुरक्षात्मक सिस्ट के अंदर एक साथ कई संतति कोशिकाओं में विभाजित होता है। सिस्ट के फटने पर कई परजीवी एक साथ बाहर निकलते हैं।",
        "explanation_gu": "પ્લાઝમોડિયમ બહુભાજન પદ્ધતિ દ્વારા રક્ષણાત્મક કોથળીની અંદર એકસાથે અસંખ્ય બાળકોષોમાં વિભાજિત થાય છે. કોથળી તૂટતાં જ ઘણા બધા પરજીવીઓ એકસાથે મુક્ત થાય છે."
    })

    # 6. Reflection
    blocks.append({
        "id": next_id(),
        "type": "reflection",
        "title": "Why Spores Survived for Millions of Years",
        "title_hi": "बीजाणु करोड़ों वर्षों तक कैसे जीवित रहे?",
        "title_gu": "બીજાણુઓ કરોડો વર્ષો સુધી કેવી રીતે જીવંત રહ્યા?",
        "body": "Rhizopus spores are microscopic, yet they possess a virtually impenetrable outer wall made of complex chitin and melanin. These spore coats can endure freezing sub-zero temperatures, intense ultraviolet radiation, boiling desert heat, and decades of complete dehydration! When you leave a fresh slice of moist bread on a kitchen counter, invisible spores floating in room air settle, germinate within hours, and produce a thriving colony of bread mould.",
        "body_hi": "राइजोपस के बीजाणु सूक्ष्म होते हैं, फिर भी उनकी बाहरी भित्ति काइटिन और मेलानिन से बनी अत्यंत मजबूत होती है। यह भित्ति अत्यधिक ठंड, तेज पराबैंगनी किरणों, रेगिस्तानी गर्मी और दशकों के सूखे को झेल सकती है! जब आप रसोई में ब्रेड का नम टुकड़ा खुला छोड़ते हैं, तो हवा में तैरते ये अदृश्य बीजाणु उस पर बैठकर कुछ ही घंटों में अंकुरित हो जाते हैं।",
        "body_gu": "રાઇઝોપસના બીજાણુઓ અતિ સૂક્ષ્મ હોવા છતાં તેમની બહાર કાઇટિનની બનેલી અત્યંત મજબૂત રક્ષણાત્મક દીવાલ હોય છે. આ દીવાલ અતિશય ઠંડી, સૂર્યના પારજાંબલી કિરણો, રણની ગરમી અને વર્ષો સુધીનો દુષ્કાળ સહન કરી શકે છે! જ્યારે તમે ભેજવાળી બ્રેડ ખુલ્લી મૂકો છો, ત્યારે હવામાં તરતા આ અદ્રશ્ય બીજાણુઓ તેના પર બેસી કલાકોમાં અંકુરિત થઈ ફૂગનું સામ્રાજ્ય રચે છે."
    })

    # 7. Connection
    blocks.append({
        "id": next_id(),
        "type": "connection",
        "title": "Vegetative Cloning and the Global Orchid Industry",
        "title_hi": "कायिक क्लोनिंग और वैश्विक आर्किड पुष्प उद्योग",
        "title_gu": "વાનસ્પતિક ક્લોનિંગ અને વૈશ્વિક ઓર્કિડ પુષ્પ ઉદ્યોગ",
        "body": "Before tissue culture, exotic orchids were harvested from wild rainforests, pushing species to extinction because orchid seeds lack food reserves and rarely germinate in nature. Through plant tissue culture (micropropagation), commercial laboratories now produce over 100 million identical, disease-free, flowering orchid plantlets every year in test tubes, transforming global floriculture without damaging wild ecosystems.",
        "body_hi": "ऊतक संवर्धन से पहले, दुर्लभ आर्किड के पौधों को वर्षावनों से काटा जाता था क्योंकि प्राकृतिक रूप से इनके बीज बिना भोजन के अंकुरित नहीं हो पाते थे। आज पादप ऊतक संवर्धन की बदौलत प्रयोगशालाओं में परखनली के अंदर हर साल 10 करोड़ से अधिक रोगमुक्त और सुंदर आर्किड के पौधे तैयार किए जाते हैं, जिससे वनों का विनाश रुक गया है।",
        "body_gu": "પેશી સંવર્ધન ટેકનોલોજી પહેલાં, જંગલી ઓર્કિડના ફૂલોને જંગલોમાંથી લૂંટવામાં આવતા હતા કારણ કે કુદરતમાં તેના બીજમાં ખોરાક ન હોવાથી તે સરળતાથી ઊગતા નહોતા. આજે પેશી સંવર્ધન દ્વારા પ્રયોગશાળામાં ટેસ્ટ ટ્યુબમાં દર વર્ષે કરોડો રોગમુક્ત ઓર્કિડના રોપાઓ ઉછેરવામાં આવે છે, જેનાથી જંગલોનો વિનાશ અટક્યો છે."
    })

    # 8. Mastery Challenge (MCQ)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "A student cuts a Planaria horizontally into three pieces (head, middle, tail) and places them in water. What will be the observed result after two weeks?",
        "question_hi": "एक छात्र प्लेनेरिया को क्षैतिज रूप से तीन टुकड़ों (सिर, मध्य, पूंछ) में काटता है और उन्हें पानी में रखता है। दो सप्ताह बाद क्या परिणाम दिखेगा?",
        "question_gu": "એક વિદ્યાર્થી પ્લેનેરિયાના આડા ત્રણ ટુકડા (માથું, મધ્ય ભાગ, પૂંછડી) કરીને પાણીમાં મૂકે છે. બે અઠવાડિયા પછી શું પરિણામ જોવા મળશે?",
        "options": [
            "All three pieces will regenerate missing parts and grow into three complete, healthy Planaria.",
            "Only the head piece will survive because the brain is located there; the other pieces will rot.",
            "All three pieces will decay and die immediately.",
            "The three pieces will fuse back together to form the single original worm."
        ],
        "options_hi": [
            "तीनों टुकड़े अपने छूटे हुए अंगों का पुनर्निर्माण करेंगे और तीन पूर्ण, स्वस्थ प्लेनेरिया बन जाएंगे।",
            "केवल सिर वाला भाग बचेगा क्योंकि मस्तिष्क वहीं होता है; अन्य टुकड़े सड़ जाएंगे।",
            "तीनों टुकड़े तुरंत सड़कर मर जाएंगे।",
            "तीनों टुकड़े आपस में जुड़कर फिर से एक ही कीड़ा बना लेंगे।"
        ],
        "options_gu": [
            "ત્રણેય ટુકડાઓ પોતાના ખૂટતા અંગોનું પુનઃસર્જન કરશે અને ત્રણ સંપૂર્ણ સ્વસ્થ પ્લેનેરિયા બની જશે.",
            "માત્ર માથાવાળો ભાગ જીવશે કારણ કે મગજ ત્યાં છે; બાકીના ટુકડા સડી જશે.",
            "ત્રણેય ટુકડાઓ તરત જ સડીને નાશ પામશે.",
            "ત્રણેય ટુકડાઓ ફરી જોડાઈને એક જ કૃમિ બની જશે."
        ],
        "correct_index": 0,
        "explanation": "Planaria possesses specialized stem-like regenerative cells throughout its body. When sliced, these cells proliferate and differentiate according to positional gradients, regenerating a head on the tail piece, a tail on the head piece, and both on the middle piece.",
        "explanation_hi": "प्लेनेरिया के पूरे शरीर में विशेष पुनरुद्भवन कोशिकाएं होती हैं। कटने पर ये कोशिकाएं तेजी से विभाजित होकर सिर, मध्य और पूंछ वाले सभी टुकड़ों को पूर्ण प्लेनेरिया में बदल देती हैं।",
        "explanation_gu": "પ્લેનેરિયાના સમગ્ર શરીરમાં વિશિષ્ટ પુનઃસર્જન કોષો આવેલા હોય છે. ટુકડા થતાં આ કોષો ઝડપથી વિભાજિત થઈને ખૂટતા તમામ ભાગો રચી દે છે અને ત્રણેય ટુકડા સંપૂર્ણ સજીવ બને છે."
    })

    # =========================================================================
    # MODULE 3: SEXUAL REPRODUCTION IN FLOWERING PLANTS (8-STEP PEDAGOGY)
    # =========================================================================

    # 1. Hook
    blocks.append({
        "id": next_id(),
        "type": "hook",
        "title": "The Seduction Architecture of Flowers",
        "title_hi": "फूलों की मनमोहક बनावट और परागण का रहस्य",
        "title_gu": "પુષ્પોની મોહક રચના અને પરાગનયનનું રહસ્ય",
        "body": "Have you ever wondered why roses are intensely fragrant, why sunflowers are radiant golden yellow, and why nocturnal jasmine blossoms release intoxicating perfumes into the dark midnight air? Plants cannot walk, speak, or seek out partners. To reproduce sexually, they engineered the most magnificent matchmaking structure on Earth: the Flower! The flower hires flying insect couriers with bribes of sweet nectar and nutritious pollen to transport male sperm cells to waiting female egg cells.",
        "body_hi": "क्या आपने कभी सोचा है कि गुलाब में इतनी मादक सुगंध क्यों होती है, सूरजमुखी चमकीला पीला क्यों होता है, और रात की रानी आधी रात में तेज खुशबू क्यों बिखेरती है? पौधे चल नहीं सकते, बोल नहीं सकते और न ही साथी की तलाश कर सकते हैं। लैंगिक प्रजनन के लिए उन्होंने पृथ्वी की सबसे सुंदर व्यवस्था बनाई है: फूल! फूल मीठे मकरंद (nectar) का लालच देकर कीड़ों को अपने पास बुलाते हैं ताकि वे नर परागकणों को मादा अंडकोष तक पहुंचा सकें।",
        "body_gu": "શું તમે ક્યારેય વિચાર્યું છે કે ગુલાબમાં આટલી મીઠી સુગંધ કેમ હોય છે, સૂર્યમુખી આટલું તેજસ્વી પીળું કેમ હોય છે અને રાતરાણી અંધારી રાતે જ કેમ સુગંધ પ્રસરાવે છે? વનસ્પતિઓ ચાલી શકતી નથી કે પોતાના સાથીને શોધી શકતી નથી. લિંગી પ્રજનન કરવા માટે તેમણે પૃથ્વી પરની સૌથી સુંદર રચના બનાવી છે: પુષ્પ! પુષ્પો મીઠા મધ જેવા રસ (મકરંદ) ની લાલચ આપી કીટકોને બોલાવે છે જેથી તેઓ નર પરાગરજને માદા અંડકોષ સુધી પહોંચાડી શકે."
    })

    # 2. Socratic Question
    blocks.append({
        "id": next_id(),
        "type": "socratic_question",
        "question": "A papaya farmer plants twenty papaya trees in an orchard. All trees grow tall and flower profusely, but five of the trees NEVER bear a single fruit! Why did this happen?",
        "question_hi": "एक किसान अपने बगीचे में पपीते के 20 पौधे लगाता है। सभी पौधे बड़े होकर खूब फूल देते हैं, लेकिन 5 पौधों पर कभी एक भी पपीता नहीं लगता! ऐसा क्यों हुआ?",
        "question_gu": "એક ખેડૂત પોતાના બગીચામાં પપૈયાના 20 છોડ વાવે છે. બધા જ છોડ મોટા થાય છે અને પુષ્કળ ફૂલો આવે છે, પરંતુ તેમાંથી 5 છોડ પર ક્યારેય એક પણ પપૈયું બેસતું નથી! આવું કેમ બન્યું?",
        "options": [
            "Papaya flowers are unisexual; the barren trees bear ONLY male flowers (staminate), which produce pollen but lack ovaries to form fruit.",
            "The farmer did not supply enough chemical fertilizer to those five trees.",
            "Birds ate the fruit buds before they could develop.",
            "Papaya trees require moonlight to produce fruits."
        ],
        "options_hi": [
            "पपीते के फूल एकलिंगी (unisexual) होते हैं; फल न देने वाले पौधे केवल नर फूल वाले थे, जिनमें परागकण तो बनते हैं पर फल बनाने वाला अंडाशय नहीं होता।",
            "किसान ने उन 5 पौधों में पर्याप्त खाद नहीं डाली थी।",
            "पक्षियों ने फल बनने से पहले ही कलियां खा ली थीं।",
            "पपीते के फल बनने के लिए चांदनी रात की आवश्यकता होती है।"
        ],
        "options_gu": [
            "પપૈયાના પુષ્પો એકલિંગી હોય છે; ફળ ન આપતા છોડ માત્ર નર પુષ્પો (પુંકેસરીય) ધરાવતા હતા, જેમાં પરાગરજ બને છે પરંતુ ફળ બનાવતું બીજાશય હોતું નથી.",
            "ખેડૂતે તે પાંચ છોડમાં ખાતર ઓછું નાખ્યું હતું.",
            "પક્ષીઓ કળીઓ ખાઈ ગયા હતા.",
            "પપૈયા પર ફળ આવવા ચાંદની રાત જરૂરી છે."
        ],
        "options_gu": [
            "પપૈયાના પુષ્પો એકલિંગી હોય છે; ફળ ન આપતા છોડ માત્ર નર પુષ્પો ધરાવતા હતા, જેમાં બીજાશય હોતું નથી.",
            "ખેડૂતે ખાતર ઓછું નાખ્યું હતું.",
            "પક્ષીઓ કળીઓ ખાઈ ગયા હતા.",
            "પપૈયાને ફળ માટે ચાંદનીની જરૂર હોય છે."
        ],
        "correct_index": 0,
        "explanation": "Papaya and watermelon produce unisexual flowers containing either stamens (male) or carpels (female). In flowering plants, ONLY the female ovary develops into the fruit after fertilization. Male trees produce only pollen and never bear fruit.",
        "explanation_hi": "पपीता और तरबूज एकलिंगी फूल पैदा करते हैं जिनमें केवल पुंकेसर या केवल स्त्रीकेसर होता है। निषेचन के बाद केवल मादा भाग का अंडाशय (ovary) ही फल बनता है। अतः केवल नर फूल वाले पौधों पर कभी फल नहीं लगते।",
        "explanation_gu": "પપૈયા અને તરબૂચમાં એકલિંગી પુષ્પો હોય છે જેમાં માત્ર પુંકેસર અથવા માત્ર સ્ત્રીકેસર હોય છે. ફલન પછી માત્ર સ્ત્રીકેસરનું બીજાશય જ ફળમાં પરિણમે છે. તેથી માત્ર નર પુષ્પોવાળા છોડ પર ક્યારેય ફળ લાગતા નથી."
    })

    # 3. Discovery
    blocks.append({
        "id": next_id(),
        "type": "discovery",
        "title": "Anatomy of a Flower: The Four Concentric Whorls",
        "title_hi": "फूल की आंतरिक संरचना: चार संकेंद्री चक्र",
        "title_gu": "પુષ્પની આંતરિક રચના: ચાર કેન્દ્રીય ચક્રો",
        "body": "A typical flower has four concentric whorls arranged on the swollen receptacle:\n\n1. Calyx (Sepals): The outermost green, leaf-like structures that protect the delicate inner floral parts during the bud stage.\n\n2. Corolla (Petals): Brightly colored, scented petals that attract insect, bird, or bat pollinators.\n\n3. Androecium (Stamen - Male Reproductive Part):\n   • Filament: The slender stalk.\n   • Anther: Swollen bilobed head containing pollen sacs that produce millions of powdery, yellow Pollen Grains (contain male germ cells).\n\n4. Gynoecium / Pistil (Carpel - Female Reproductive Part):\n   • Stigma: Sticky top platform designed to trap landing pollen grains.\n   • Style: Elongated slender neck through which the pollen tube grows.\n   • Ovary: Swollen basal part containing one or more Ovules. Each ovule contains an embryo sac with a Female Germ Cell (Egg cell).",
        "body_hi": "एक प्रारूपिक फूल में चार मुख्य चक्र होते हैं:\n\n1. बाह्यदलपुंज (Sepals / बाह्यदल): सबसे बाहरी हरी पत्तियों जैसी संरचनाएं जो कली की अवस्था में फूल की रक्षा करती हैं।\n\n2. दलपुंज (Petals / पंखुड़ियां): चमकीली, रंगीन और सुगंधित पंखुड़ियां जो परागण के लिए कीटों को आकर्षित करती हैं।\n\n3. पुमंग (Stamen / पुंकेसर - नर जनन अंग):\n   • तंतु (Filament): पतला डंठल।\n   • परागकोश (Anther): ऊपरी फूला हुआ भाग जिसमें परागकण (Pollen grains) बनते हैं। परागकण में नर युग्मक होते हैं।\n\n4. जायाંગ (Carpel / स्त्रीकेसर - मादा जनन अंग):\n   • वर्तिकाग्र (Stigma): चिपचिपा ऊपरी भाग जो परागकणों को ग्रहण करता है।\n   • वर्तिका (Style): लंबी पतली नली जिससे होकर पराग नलिका नीचे जाती है।\n   • अंडाशय (Ovary): फूला हुआ निचला भाग जिसमें बीजांड (Ovules) होते हैं। बीजांड में मादा युग्मक (अंडकोशिका) होती है।",
        "body_gu": "લાક્ષણિક પુષ્પમાં ચાર મુખ્ય ચક્રો આવેલા હોય છે:\n\n1. વજ્રચક્ર (Sepals / વજ્રપત્રો): સૌથી બહારનું લીલું ચક્ર જે કળી અવસ્થામાં પુષ્પનું રક્ષણ કરે છે.\n\n2. દલચક્ર (Petals / દલપત્રો): તેજસ્વી રંગીન પાંખડીઓ જે કીટકોને પરાગનયન માટે આકર્ષે છે.\n\n3. પુંકેસર ચક્ર (Stamen / પુંકેસર - નર પ્રજનન અંગ):\n   • તંતુ (Filament): પાતળો દંડ.\n   • પરાગાશય (Anther): ઉપરનો ફૂલેલો ભાગ જેમાં પરાગરજ બને છે. પરાગરજમાં નર જન્યુઓ હોય છે.\n\n4. સ્ત્રીકેસર ચક્ર (Carpel / સ્ત્રીકેસર - માદા પ્રજનન અંગ):\n   • પરાગાસન (Stigma): ચીકણું મથાળું જે પરાગરજને ચોંટાડે છે.\n   • પરાગવાહિની (Style): પાતળી નળી જેમાંથી પરાગનલિકા પસાર થાય છે.\n   • બીજાશય (Ovary): નીચેનો ફૂલેલો ભાગ જેમાં અંડકો (Ovules) આવેલા હોય છે. અંડકમાં માદા જન્યુ (અંડકોષ) હોય છે."
    })

    # 4. Theory
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "Pollination, Fertilization, and Post-Fertilization Metamorphosis",
        "title_hi": "परागण, निषेचन और निषेचनोत्तर कायापलट",
        "title_gu": "પરાગનયન, ફલન અને ફલન પછીના ફેરફારો",
        "body": "The journey from flower to fruit follows a precise biological choreography:\n\n1. Pollination: Transfer of pollen grains from the anther to the stigma.\n   • Self-pollination: Transfer occurs within the same flower or between flowers of the same plant.\n   • Cross-pollination: Transfer from the anther of one flower to the stigma of a different plant's flower via wind, water, or animal vectors (bees, butterflies).\n\n2. Pollen Tube Germination & Fertilization:\n   • After landing on the compatible sticky stigma, the pollen grain absorbs sugary fluid and germinates.\n   • A Pollen Tube emerges and grows down through the entire length of the style into the ovary.\n   • The tube enters the ovule through a tiny pore (micropyle) and releases two male gametes.\n   • Fertilization: One male gamete fuses with the female egg cell to form a diploid Zygote (2n).\n\n3. Post-Fertilization Transformations (BOARD ESSENTIAL):\n   • Zygote divides repeatedly by mitosis to become an Embryo.\n   • Ovule develops a tough protective coat and converts into a SEED.\n   • Ovary grows rapidly, ripens, and transforms into the FRUIT.\n   • Petals, sepals, stamens, style, and stigma shrivel and fall off completely.\n\n4. Seed Germination: The seed contains the future plant (embryo):\n   • Cotyledon(s): Store starch and nutrients for the seedling.\n   • Plumule: The future shoot system (stems and leaves).\n   • Radicle: The future root system.",
        "body_hi": "फूल से फल बनने की संपूर्ण प्रक्रिया:\n\n1. परागण (Pollination): परागकणों का परागकोश से वर्तिकाग्र पर स्थानांतरण।\n   • स्व-परागण: एक ही फूल में या एक ही पौधे के फूलों के बीच परागण।\n   • पर-परागण: हवा, पानी या कीटों द्वारा एक पौधे के फूल से दूसरे पौधे के फूल के वर्तिकाग्र पर पराग जाना।\n\n2. परागनली और निषेचन (Fertilization):\n   • वर्तिकाग्र पर पहुंचकर परागकण अंकुरित होता है और एक परागनली निकलती है।\n   • परागनली वर्तिका से होती हुई अंडाशय में बीजांड तक पहुंचती है।\n   • नर युग्मक परागनली से निकलकर बीजांड में मादा अंडकोशिका से संलयित होकर युग्मनज (Zygote) बनाता है। इसे निषेचन कहते हैं।\n\n3. निषेचन के बाद होने वाले परिवर्तन (बोर्ड परीक्षा के लिए अति महत्वपूर्ण):\n   • युग्मनज विभाजित होकर भ्रूण (Embryo) बनता है।\n   • बीजांड (Ovule) कठोर आवरण विकसित करके बीज (SEED) में बदल जाता है।\n   • अंडाशय (Ovary) तेजी से पककर फल (FRUIT) में बदल जाता है।\n   • बाह्यदल, पंखुड़ियां, पुंकेसर और वर्तिका सूखकर गिर जाते हैं।\n\n4. बीज का अंकुरण:\n   • बीजपत्र (Cotyledon): अंकुर के लिए भोजन का भंडारण।\n   • प्रांकुर (Plumule): भावी प्ररोહ (तना और पत्तियां)।\n   • मूलांकुर (Radicle): भावी जड़।",
        "body_gu": "પુષ્પમાંથી ફળ બનવાની સમગ્ર પ્રક્રિયા:\n\n1. પરાગનયન (Pollination): પરાગાશયમાંથી પરાગરજનું પરાગાસન પર સ્થળાંતર.\n   • સ્વ-પરાગનયન: તે જ પુષ્પમાં કે તે જ છોડના પુષ્પો વચ્ચે પરાગરજનું વહન.\n   • પર-પરાગનયન: પવન, પાણી કે કીટકો દ્વારા એક છોડના પુષ્પ પરથી બીજા છોડના પુષ્પના પરાગાસન પર પરાગરજ જવી.\n\n2. પરાગનલિકાનો વિકાસ અને ફલન (Fertilization):\n   • પરાગાસન પર પરાગરજ અંકુરિત થઈ પરાગનલિકા બનાવે છે.\n   • પરાગનલિકા પરાગવાહિનીમાંથી પસાર થઈ બીજાશયમાં અંડક સુધી પહોંચે છે.\n   • નર જન્યુ અંડકોષ સાથે જોડાઈને યુગ્મનજ (Zygote) રચે છે, જેને ફલન કહેવાય છે.\n\n3. ફલન પછી થતા ફેરફારો (બોર્ડ પરીક્ષા માટે ખાસ):\n   • યુગ્મનજ વિભાજન પામી ભ્રૂણ (Embryo) બને છે.\n   • અંડક (Ovule) મજબૂત આવરણ બનાવી બીજ (SEED) માં ફેરવાય છે.\n   • બીજાશય (Ovary) ઝડપથી વિકાસ પામીને ફળ (FRUIT) બને છે.\n   • વજ્રપત્રો, દલપત્રો, પુંકેસર અને પરાગવાહિની ખરી પડે છે.\n\n4. બીજ અંકુરણ:\n   • બીજપત્ર (Cotyledons): ભ્રૂણ માટે ખોરાકનો સંગ્રહ.\n   • ભ્રૂણાગ્ર / પ્રરોહાગ્ર (Plumule): ભવિષ્યનું પ્રકાંડ.\n   • ભ્રૂણમૂળ (Radicle): ભવિષ્યનું મૂળ."
    })

    # Teacher Tip
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Teacher Tip: The Golden Mnemonic for Flower Parts to Fruit",
        "title_hi": "शिक्षक टिप: फूल के भागों से फल बनने का गोल्डन नियम",
        "title_gu": "શિક્ષક ટિપ: પુષ્પના ભાગોમાંથી ફળ બનવાનો સુવર્ણ નિયમ",
        "body": "Never confuse Ovule and Ovary in the exam!\n• OVULE becomes the SEED (Inside the fruit).\n• OVARY becomes the FRUIT (The fleshy outer part you eat).\nRemember: 'Ovary is Ordinary fruit, Ovule is Under the seed'!",
        "body_hi": "परीक्षा में बीजांड और अंडाशय में कभी भ्रमित न हों!\n• बीजांड (Ovule) -> बीज (Seed) बनता है (अंदर रहता है)।\n• अंडाशय (Ovary) -> फल (Fruit) बनता है (बाहर का गूदेदार भाग जो हम खाते हैं)।",
        "body_gu": "પરીક્ષામાં અંડક અને બીજાશય વચ્ચે ક્યારેય ભૂલ ન કરો!\n• અંડક (Ovule) -> બીજ (Seed) બને છે (અંદર રહે છે).\n• બીજાશય (Ovary) -> ફળ (Fruit) બને છે (ફળનો ગર્ભ જે આપણે ખાઈએ છીએ)."
    })

    # 5. Knowledge Check (MCQ)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Which part of the embryonic seed develops into the future root system during seed germination?",
        "question_hi": "बीज अंकुरण के दौरान भ्रूण का कौन सा भाग भावी जड़ (root system) के रूप में विकसित होता है?",
        "question_gu": "બીજ અંકુરણ દરમિયાન ભ્રૂણનો કયો ભાગ ભવિષ્યના મૂળ તંત્ર તરીકે વિકાસ પામે છે?",
        "options": [
            "Radicle",
            "Plumule",
            "Cotyledon",
            "Seed coat"
        ],
        "options_hi": [
            "मूलांकुर (Radicle)",
            "प्रांकुर (Plumule)",
            "बीजपत्र (Cotyledon)",
            "बीजावरण (Seed coat)"
        ],
        "options_gu": [
            "ભ્રૂણમૂળ / મૂલાંકુર (Radicle)",
            "ભ્રૂણાગ્ર / પ્રાંકુર (Plumule)",
            "બીજપત્ર (Cotyledon)",
            "બીજાવરણ (Seed coat)"
        ],
        "correct_index": 0,
        "explanation": "Remember 'R for Radicle = Root' and 'P for Plumule = Plant Shoot'. The radicle grows downwards into soil to establish roots, while plumule grows upward into sunlight.",
        "explanation_hi": "'मूलांकुर (Radicle)' से 'मूल' यानी जड़ बनती है, जबकि 'प्रांकुर (Plumule)' से प्ररोह यानी तना और पत्तियां बनती हैं।",
        "explanation_gu": "'મૂલાંકુર (Radicle)' જમીનમાં નીચે ઊતરીને મૂળ બનાવે છે, જ્યારે 'પ્રાંકોર (Plumule)' સૂર્યપ્રકાશ તરફ વધીને પ્રકાંડ બનાવે છે."
    })

    # 6. Reflection
    blocks.append({
        "id": next_id(),
        "type": "reflection",
        "title": "Why Cross-Pollination Demands Such Heavy Investment",
        "title_hi": "पर-परागण के लिए पौधे इतना भारी निवेश क्यों करते हैं?",
        "title_gu": "પર-પરાગનયન માટે વનસ્પતિઓ આટલું મોટું રોકાણ કેમ કરે છે?",
        "body": "Making sweet nectar, radiant pigments, and billions of pollen grains consumes immense photosynthetic energy. Why didn't all plants evolve simple, cheap self-pollination? Because self-pollination results in continuous inbreeding, reducing genetic variation and accumulating harmful recessive mutations. Cross-pollination introduces novel genetic combinations from unrelated plants, conferring vigor, disease resistance, and evolutionary resilience.",
        "body_hi": "मीठा मकरंद, रंगीन पंखुड़ियां और करोड़ों परागकण बनाने में पौधे की बहुत सारी प्रकाश-संश्लेषण ऊर्जा खर्च होती है। पौधों ने केवल सरल स्व-परागण ही क्यों नहीं अपनाया? क्योंकि स्व-परागण से आनुवंशिक विविधता समाप्त हो जाती है और हानिकारक उत्परिवर्तन जमा होने लगते हैं। पर-परागण नए जीन संयोजनों को लाता है जिससे पौधे अधिक स्वस्थ, रोग-प्रतिरोधी और मजबूत बनते हैं।",
        "body_gu": "મીઠો મકરંદ, રંગીન પાંખડીઓ અને અબજો પરાગરજ બનાવવામાં વનસ્પતિની પુષ્કળ ઊર્જા વપરાય છે. બધા છોડ સાદું સ્વ-પરાગનયન જ કેમ નથી અપનાવતા? કારણ કે સતત સ્વ-પરાગનયનથી જનીનિક ભિન્નતા નાશ પામે છે અને નુકસાનકારક રોગો સામે પ્રતિકારકતા ઘટે છે. પર-પરાગનયન નવા જનીનોનું મિશ્રણ લાવે છે જે પાકને વધુ મજબૂત અને રોગમુક્ત બનાવે છે."
    })

    # 7. Connection
    blocks.append({
        "id": next_id(),
        "type": "connection",
        "title": "The Global Pollinator Crisis and Food Security",
        "title_hi": "वैश्विक परागणकर्ता संकट और खाद्य सुरक्षा",
        "title_gu": "વૈશ્વિક પરાગનયન સંકટ અને વૈશ્વિક ખાદ્ય સુરક્ષા",
        "body": "Over 75% of global food crop types—including almonds, apples, coffee, tomatoes, and cocoa—depend directly on insect pollinators. Due to indiscriminate pesticide spraying, habitat destruction, and climate disruption, bee populations are crashing worldwide. Agricultural scientists estimate that without insect pollination, global food yields would collapse by 30%, triggering catastrophic food shortages.",
        "body_hi": "बादाम, सेब, कॉफी, टमाटर और कोको जैसी 75% से अधिक वैश्विक खाद्य फसलें परागणकारी कीटों (विशेषकर मधुमक्खियों) पर निर्भर हैं। कीटनाशकों के अत्यधिक छिड़काव और पर्यावरण विनाश से मधुमक्खियों की आबादी तेजी से घट रही है। यदि परागणकर्ता समाप्त हो गए, तो विश्व में अनाज और फलों का उत्पादन 30% तक गिर जाएगा, जिससे भीषण अकाल पड़ सकता है।",
        "body_gu": "બદામ, સફરજન, કૉફી અને ટામેટાં જેવા વિશ્વના 75% થી વધુ ખાદ્ય પાકો મધમાખી જેવા પરાગવાહક કીટકો પર નિર્ભર છે. જંતુનાશકોના આડેધડ વપરાશથી મધમાખીઓ મરી રહી છે. વૈજ્ઞાનિકો ચેતવણી આપે છે કે જો પરાગવાહકો નાશ પામશે, તો વિશ્વનું ખાદ્ય ઉત્પાદન 30% ઘટી જશે અને ભયંકર ભૂખમરો સર્જાશે."
    })

    # 8. Mastery Challenge (MCQ)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Which of the following represents the correct sequential path of a male gamete from the surface of the flower until fertilization?",
        "question_hi": "निषेचन तक पहुंचने के लिए नर युग्मक के सही अनुक्रमिक मार्ग को कौन सा विकल्प दर्शाता है?",
        "question_gu": "ફલન સુધી પહોંચવા માટે નર જન્યુના સાચા ક્રમિક માર્ગને કયો વિકલ્પ દર્શાવે છે?",
        "options": [
            "Stigma -> Pollen tube through Style -> Ovary -> Micropyle of Ovule -> Female egg cell",
            "Anther -> Sepal -> Petal -> Ovary -> Style",
            "Stigma -> Filament -> Anther -> Seed -> Fruit",
            "Radicle -> Cotyledon -> Plumule -> Ovule"
        ],
        "options_hi": [
            "वर्तिकाग्र -> वर्तिका से होती हुई परागनली -> अंडाशय -> बीजांडद्वार (Micropyle) -> अंड कोशिका",
            "परागकोश -> बाह्यदल -> पंखुड़ी -> अंडाशय -> वर्तिका",
            "वर्तिकाग्र -> तंतु -> परागकोश -> बीज -> फल",
            "मूलांकुर -> बीजपत्र -> प्रांकुर -> बीजांड"
        ],
        "options_gu": [
            "પરાગાસન -> પરાગવાહિનીમાંથી પરાગનલિકા -> બીજાશય -> અંડકનું છિદ્ર -> અંડકોષ",
            "પરાગાશય -> વજ્રપત્ર -> દલપત્ર -> બીજાશય -> પરાગવાહિની",
            "પરાગાસન -> તંતુ -> પરાગાશય -> બીજ -> ફળ",
            "ભ્રૂણમૂળ -> બીજપત્ર -> ભ્રૂણાગ્ર -> અંડક"
        ],
        "correct_index": 0,
        "explanation": "Pollen lands on stigma -> germinates into pollen tube -> grows down style into ovary -> enters micropyle of ovule -> male gamete fuses with egg cell to form zygote.",
        "explanation_hi": "परागकण वर्तिकाग्र पर चिपकता है -> परागनली निकलती है जो वर्तिका से अंडाशय में जाती है -> बीजांडद्वार से प्रवेश कर अंड कोशिका से संलयन करती है।",
        "explanation_gu": "પરાગરજ પરાગાસન પર ચોંટે છે -> પરાગનલિકા પરાગવાહિનીમાંથી બીજાશયમાં ઊતરે છે -> અંડકના છિદ્રમાંથી પ્રવેશી અંડકોષ સાથે ફલન કરે છે."
    })

    # =========================================================================
    # MODULE 4: HUMAN REPRODUCTION - PUBERTY & MALE SYSTEM (8-STEP PEDAGOGY)
    # =========================================================================

    # 1. Hook
    blocks.append({
        "id": next_id(),
        "type": "hook",
        "title": "The Teenage Metamorphosis: Why Our Bodies Transform",
        "title_hi": "किशोरावस्था का कायाकल्प: हमारा शरीर अचानक क्यों बदलता है?",
        "title_gu": "કિશોરાવસ્થાનો કાયાકલ્પ: આપણું શરીર અચાનક શા માટે બદલાય છે?",
        "body": "Between the ages of 10 and 14, every human experiences a sudden, dramatic biological revolution: boys find their voices cracking into a deep bass, shoulders broadening, and facial hair sprouting; girls experience breast development, hip widening, and the onset of menstruation. Why does this drastic bodily remodeling occur at this exact stage of life? Because the rapid childhood body growth slows down, and the body redirects its resources to activate reproductive maturity—a transition known as Puberty!",
        "body_hi": "10 से 14 वर्ष की आयु के बीच हर मनुष्य के शरीर में एक नाटकीय जैविक क्रांति होती है: लड़कों की आवाज भारी होने लगती है, कंधे चौड़े होते हैं और चेहरे पर दाढ़ी-मूंछ आने लगती है; लड़कियों में स्तनों का विकास, कूल्हों का चौड़ा होना और मासिक धर्म शुरू हो जाता है। जीवन के इसी पड़ाव पर यह जबरदस्त शारीरिक बदलाव क्यों आता है? क्योंकि बचपन की तीव्र सामान्य शारीरिक वृद्धि धीमी हो जाती है और शरीर अपनी ऊर्जा जनन ऊतकों को परिपक्व करने में लगाता है—इस परिवर्तन काल को यौवनारंभ (Puberty) कहते हैं!",
        "body_gu": "10 થી 14 વર્ષની વય વચ્ચે દરેક બાળકના શરીરમાં એક નાટકીય જૈવિક ક્રાંતિ થાય છે: છોકરાઓનો અવાજ ઘેરો બને છે, ખભા પહોળા થાય છે અને દાઢી-મૂંછ ઊગવા લાગે છે; છોકરીઓમાં સ્તનનો વિકાસ, નિતંબ પહોળા થવા અને માસિક સ્ત્રાવ શરૂ થાય છે. જીવનના આ તબક્કે જ આવો મોટો શારીરિક બદલાવ કેમ આવે છે? કારણ કે બાળપણની સામાન્ય શારીરિક વૃદ્ધિ ધીમી પડે છે અને શરીર પોતાની ઊર્જા પ્રજનન અંગોને પુખ્ત કરવામાં વાપરે છે—આ તબક્કાને યૌવનારંભ (Puberty) કહે છે!"
    })

    # 2. Socratic Question
    blocks.append({
        "id": next_id(),
        "type": "socratic_question",
        "question": "The human core body temperature is strictly regulated at 37°C (98.6°F). Yet in males, the testes are placed outside the abdominal cavity in a hanging sac called the scrotum. Why did human evolution place such vital organs outside the protective body cavity?",
        "question_hi": "मानव शरीर का आंतरिक तापमान 37°C पर नियंत्रित रहता है। फिर भी पुरुषों में वृषण (Testes) उदर गुहा के बाहर एक लटकती थैली 'वृषण कोष' (Scrotum) में स्थित होते हैं। विकास ने इतने महत्वपूर्ण अंगों को शरीर के बाहर क्यों रखा?",
        "question_gu": "માનવ શરીરનું સામાન્ય તાપમાન 37°C જળવાઈ રહે છે. તેમ છતાં પુરુષોમાં શુક્રપિંડ (Testes) ઉદરગુહાની બહાર લટકતી વૃષણકોથળી (Scrotum) માં આવેલા છે. ઉત્ક્રાંતિએ આટલા મહત્વના અંગોને શરીરની બહાર શા માટે રાખ્યા?",
        "options": [
            "Sperm formation (spermatogenesis) strictly requires a temperature 2 to 2.5°C lower than normal internal body temperature.",
            "The testes are too large to fit inside the human abdominal cavity.",
            "The scrotum allows direct absorption of atmospheric oxygen through the skin.",
            "Testes migrate outside to prevent sperm from mixing with digestive acids in the stomach."
        ],
        "options_hi": [
            "शुक्राणु निर्माण (Spermatogenesis) के लिए शरीर के सामान्य तापमान से 2 से 2.5°C कम तापमान की सख्त आवश्यकता होती है।",
            "वृषण इतने बड़े होते हैं कि पेट के अंदर नहीं समा सकते।",
            "वृषण कोष सीधे हवा से ऑक्सीजन लेने के लिए बाहर होता है।",
            "ताकि शुक्राणु पेट के पाचक अम्लों में न मिल जाएं।"
        ],
        "options_gu": [
            "શુક્રકોષોના નિર્માણ માટે શરીરના સામાન્ય તાપમાન કરતાં 2 થી 2.5°C નીચા તાપમાનની સખત જરૂર હોય છે.",
            "શુક્રપિંડ કદમાં ખૂબ મોટા હોવાથી પેટમાં સમાઈ શકતા નથી.",
            "વૃષણકોથળી હવામાંથી સીધો ઓક્સિજન મેળવવા બહાર આવેલી છે.",
            "શુક્રકોષો જઠરના એસિડ સાથે ભળી ન જાય તે માટે."
        ],
        "correct_index": 0,
        "explanation": "Human core temperature (37°C) is lethal to developing sperms and halts spermatogenesis. The external scrotum functions as a biological thermostat, maintaining testes 2 - 2.5°C cooler than internal body temperature, ensuring healthy sperm production.",
        "explanation_hi": "शरीर का सामान्य तापमान (37°C) शुक्राणुओं के निर्माण के लिए बहुत अधिक होता है। वृषण कोष शरीर के बाहर रहकर तापमान को 2 से 2.5°C कम बनाए रखता है, जिससे शुक्राणु स्वस्थ रूप से बन सकें।",
        "explanation_gu": "શરીરનું 37°C તાપમાન શુક્રકોષ નિર્માણ માટે ખૂબ વધારે છે. વૃષણકોથળી શરીરની બહાર રહીને તાપમાન 2 થી 2.5°C નીચું જાળવે છે, જેથી તંદુરસ્ત શુક્રકોષો ઉત્પન્ન થઈ શકે."
    })

    # 3. Discovery
    blocks.append({
        "id": next_id(),
        "type": "discovery",
        "title": "Architecture of the Male Reproductive System",
        "title_hi": "नर जनन तंत्र की विस्तृत शारीरिक रचना",
        "title_gu": "નર પ્રજનન તંત્રની વિસ્તૃત શારીરિક રચના",
        "body": "The male reproductive system is engineered to produce, nourish, and deliver male germ cells:\n\n1. Testes (Paired): Located in the scrotum. Dual function:\n   • Production of male germ cells: Millions of microscopic, motile Sperms.\n   • Endocrine hormone secretion: Produces Testosterone, which regulates sperm production and stimulates puberty changes (facial hair, deeper voice, muscle mass).\n\n2. Vas Deferens (Sperm Duct): Long muscular tubes that transport sperms upward from the testes, looping over the urinary bladder.\n\n3. Accessory Glands (Seminal Vesicles & Prostate Gland):\n   • Add alkaline secretions along the path of the vas deferens.\n   • Function of glandular fluid: 1) Provides liquid medium for smooth sperm mobility. 2) Provides nutrition (fructose, enzymes). 3) Neutralizes acidity of female genital tract.\n   • The mixture of sperm cells + glandular fluid is called SEMEN.\n\n4. Urethra: A common muscular tube in males serving as the exit pathway for both urine and semen (never simultaneously due to nervous sphincter control).\n\n5. Penis: Muscular copulatory organ that transfers semen into the female vagina during sexual intercourse.\n\n6. Sperm Anatomy: Tiny specialized cells consisting of a Head (containing the nucleus with DNA) and a long, whip-like Tail that propels the sperm forward through fluid towards the female egg.",
        "body_hi": "नर जनन तंत्र की मुख्य संरचनाएं और कार्य:\n\n1. वृषण (Testes): वृषण कोष में स्थित एक जोड़ी अंडाकार अंग। दो मुख्य कार्य:\n   • शुक्राणुओं (Sperms) का निर्माण करना।\n   • टेस्टोस्टेरोन (Testosterone) हार्मोन का स्राव करना, जो शुक्राणु निर्माण को नियंत्रित करता है और लड़कों में यौवनारंभ के शारीरिक लक्षणों को प्रेरित करता है।\n\n2. शुक्रवाहिका (Vas Deferens): वृषण से शुक्राणुओं को ऊपर मूत्रमार्ग तक ले जाने वाली पेशीय नली।\n\n3. सहायक ग्रंथियां (शुक्राशय / Seminal Vesicles और प्रोस्टेट ग्रंथि / Prostate Gland):\n   • ये ग्रंथियां शुक्रवाहिका में अपना तरल स्राव मिलाती हैं।\n   • तरल के कार्य: 1) शुक्राणुओं को तैरने के लिए तरल माध्यम देना। 2) शुक्राणुओं को पोषण (फ्रुक्टोज) प्रदान करना।\n   • शुक्राणुओं और इन ग्रंथियों के तरल के मिश्रण को वीर्य (SEMEN) कहा जाता है।\n\n4. मूत्रमार्ग (Urethra): पुरुषों में मूत्र और वीर्य दोनों के निकास के लिए एक ही साझा मार्ग है।\n\n5. शिश्न (Penis): बाह્ય जननांग जो संभोग के दौरान वीर्य को मादा जनन पथ में पहुंचाता है।\n\n6. शुक्राणु की संरचना: सिर (जिसमें डीएनए युक्त केंद्रक होता है) और एक लंबी पूंछ (जो तैरने में मदद करती है)।",
        "body_gu": "નર પ્રજનન તંત્રના મુખ્ય ભાગો અને તેમના કાર્યો:\n\n1. શુક્રપિંડ (Testes): વૃષણકોથળીમાં આવેલી એક જોડ. બે મુખ્ય કાર્યો:\n   • શુક્રકોષો (Sperms) નું ઉત્પાદન કરવું.\n   • ટેસ્ટોસ્ટેરોન (Testosterone) અંતઃસ્ત્રાવ મુક્ત કરવો, જે શુક્રકોષ ઉત્પાદનનું નિયમન કરે છે અને છોકરાઓમાં યૌવનારંભના લક્ષણો લાવે છે.\n\n2. શુક્રવાહિની (Vas Deferens): શુક્રકોષોનું શુક્રપિંડમાંથી મૂત્રમાર્ગ તરફ વહન કરતી નળી.\n\n3. સહાયક ગ્રંથિઓ (શુક્રાશય અને પ્રોસ્ટેટ ગ્રંથિ):\n   • શુક્રવાહિનીમાં પોતાનો પ્રવાહી સ્ત્રાવ ઉમેરે છે.\n   • પ્રવાહીના કાર્યો: 1) શુક્રકોષોને તરવા માટે પ્રવાહી માધ્યમ પૂરું પાડવું. 2) શુક્રકોષોને પોષણ આપવું.\n   • શુક્રકોષો અને ગ્રંથિઓના પ્રવાહીના મિશ્રણને વીર્ય (SEMEN) કહે છે.\n\n4. મૂત્રમાર્ગ (Urethra): પુરુષોમાં મૂત્ર અને વીર્ય બંનેના નિકાલ માટેનો એક સામાન્ય માર્ગ.\n\n5. શિશ્ન (Penis): નળાકાર અંગ જે વીર્યને માદાના પ્રજનન માર્ગમાં દાખલ કરે છે.\n\n6. શુક્રકોષની રચના: શીર્ષ (જેમાં જનીનિક દ્રવ્ય ડીએનએ હોય છે) અને લાંબી પૂંછડી (જે શુક્રકોષને તરવામાં મદદ કરે છે)."
    })

    # 4. Theory
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "Master Summary: Glandular Fluid and the Miracle of Sperm Motility",
        "title_hi": "मास्टर सारांश: ग्रंथियों का तरल स्राव और शुक्राणु गतिशीलता का रहस्य",
        "title_gu": "માસ્ટર સારાંશ: ગ્રંથિઓનો સ્ત્રાવ અને શુક્રકોષ ગતિશીલતાનું મહત્વ",
        "body": "Why don't sperms travel alone? A single ejaculation contains 200 to 300 million microscopic sperm cells suspended in approximately 3 to 5 mL of fluid.\n\n• Prostate Secretion: Thin, milky alkaline fluid containing calcium and enzymes that neutralizes the naturally acidic environment of the male urethra and female vagina (acid is lethal to sperms).\n• Seminal Vesicle Secretion: Thick, yellowish fluid rich in fructose sugar. Sperms consume this fructose as their cellular fuel inside their midpiece mitochondria to generate ATP, powering the vigorous lashing motion of their tail to swim toward the Fallopian tube!\n\nWithout these secretions, sperms would instantly perish from acidity and starvation before ever reaching the egg.",
        "body_hi": "शुक्राणु अकेले यात्रा क्यों नहीं कर सकते? एक बार के स्खलन में लगभग 20 से 30 करोड़ शुक्राणु 3 से 5 मिलीलीटर वीर्य में तैरते हैं।\n\n• प्रोस्टेट ग्रंथि का स्राव: हल्का क्षारीय तरल जो मूत्रमार्ग और योनि के अम्लीय वातावरण को उदासीन करता है (क्योंकि अम्ल शुक्राणुओं को मार देता है)।\n• शुक्राशय का स्राव: फ्रुक्टोज शर्करा से भरपूर गाढ़ा तरल। शुक्राणु इस फ्रुक्टोज को ऊर्जा के रूप में उपयोग करते हैं जिससे उनकी पूंछ तेजी से चलती है और वे तैरकर आगे बढ़ पाते हैं।\n\nइन ग्रंथियों के स्राव के बिना शुक्राणु मादा जनन मार्ग में पहुंचते ही नष्ट हो जाएंगे।",
        "body_gu": "શુક્રકોષો એકલા કેમ મુસાફરી કરી શકતા નથી? એક વખતના સ્ખલનમાં 20 થી 30 કરોડ શુક્રકોષો 3 થી 5 મિલી વીર્યમાં વહે છે.\n\n• પ્રોસ્ટેટ ગ્રંથિનો સ્ત્રાવ: આલ્કલાઇન પ્રવાહી જે મૂત્રમાર્ગ અને યોનિમાર્ગના એસિડિક વાતાવરણને તટસ્થ કરે છે (એસિડ શુક્રકોષોને મારી નાખે છે).\n• શુક્રાશયનો સ્ત્રાવ: ફ્રુક્ટોઝ શર્કરાથી ભરપૂર પ્રવાહી. શુક્રકોષો આ ફ્રુક્ટોઝમાંથી ઊર્જા મેળવીને પોતાની પૂંછડી હલાવીને અંડવાહિની તરફ ઝડપથી તરી શકે છે.\n\nઆ સહાયક ગ્રંથિઓના સ્ત્રાવ વિના શુક્રકોષો એસિડિટી અને ભૂખમરાથી અધવચ્ચે જ નાશ પામે."
    })

    # Teacher Tip
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Teacher Tip: Dual Function of Testes and Vasectomy Clarity",
        "title_hi": "शिक्षक टिप: वृषण के दोहरे कार्य और नसबंदी की स्पष्टता",
        "title_gu": "શિક્ષક ટિપ: શુક્રપિંડના બેવડા કાર્યો અને વાસેક્ટોમીની સ્પષ્ટતા",
        "body": "NCERT frequently tests: 'What are the two functions performed by the testis?'\n1. Production of male germ cells (sperms) - Exocrine/Gametic function.\n2. Secretion of the male sex hormone (testosterone) - Endocrine function.\n\nAlso remember: When a male undergoes a vasectomy (surgical sterilization), only the vas deferens tubes are cut and tied. Semen is still ejaculated normally because the prostate and seminal vesicles are completely untouched! The only difference is that the semen contains zero sperms.",
        "body_hi": "NCERT में बार-बार पूछा जाने वाला प्रश्न: 'वृषण के दो कार्य क्या हैं?'\n1. नर जनन कोशिकाओं (शुक्राणुओं) का उत्पादन।\n2. नर सेक्स हार्मोन (टेस्टोस्टेरोन) का स्राव।\n\nयह भी याद रखें: जब किसी पुरुष की नसबंदी (Vasectomy) की जाती है, तो केवल शुक्रवाहिका काटी जाती है। वीर्य का निकलना बंद नहीं होता क्योंकि प्रोस्टेट और शुक्राशय ग्रंथियां सामान्य रूप से तरल बनाती रहती हैं! बस उस वीर्य में शुक्राणु नहीं होते।",
        "body_gu": "પરીક્ષામાં વારંવાર પૂછાતો પ્રશ્ન: 'શુક્રપિંડના બે કાર્યો કયા છે?'\n1. નર પ્રજનન કોષો (શુક્રકોષો) ઉત્પન્ન કરવા.\n2. નર જાતીય અંતઃસ્ત્રાવ (ટેસ્ટોસ્ટેરોન) મુક્ત કરવો.\n\nયાદ રાખો: પુરુષ નસબંધી (વાસેક્ટોમી) માં માત્ર શુક્રવાહિની કાપીને બાંધવામાં આવે છે. વીર્યનું સ્ખલન બંધ થતું નથી કારણ કે પ્રોસ્ટેટ અને શુક્રાશય પ્રવાહી બનાવવાનું ચાલુ રાખે છે, માત્ર તે વીર્યમાં શુક્રકોષો હોતા નથી."
    })

    # 5. Knowledge Check (MCQ)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Which hormone is secreted by the testes to regulate the production of sperms and bring about secondary sexual changes in boys during puberty?",
        "question_hi": "किशोरावस्था के दौरान लड़कों में शुक्राणु उत्पादन को नियंत्रित करने और द्वितीयक लैंगिक लक्षण लाने के लिए वृषण द्वारा कौन सा हार्मोन स्रावित होता है?",
        "question_gu": "યૌવનારંભ દરમિયાન છોકરાઓમાં શુક્રકોષ ઉત્પાદનનું નિયમન કરવા અને ગૌણ જાતીય લક્ષણો લાવવા માટે શુક્રપિંડ દ્વારા કયો અંતઃસ્ત્રાવ મુક્ત થાય છે?",
        "options": [
            "Testosterone",
            "Oestrogen",
            "Progesterone",
            "Insulin"
        ],
        "options_hi": [
            "टेस्टोस्टेरोन (Testosterone)",
            "एस्ट्रोजन (Oestrogen)",
            "प्रोजेस्टेरोन (Progesterone)",
            "इंसुलिन (Insulin)"
        ],
        "options_gu": [
            "ટેસ્ટોસ્ટેરોન (Testosterone)",
            "ઇસ્ટ્રોજન (Oestrogen)",
            "પ્રોજેસ્ટેરોન (Progesterone)",
            "ઇન્સ્યુલિન (Insulin)"
        ],
        "correct_index": 0,
        "explanation": "Testosterone is the primary male sex hormone produced by Leydig cells in the testes. It stimulates spermatogenesis and develops secondary sexual characteristics (deep voice, facial hair, muscular development).",
        "explanation_hi": "टेस्टोस्टेरोन मुख्य नर सेक्स हार्मोन है जो वृषण द्वारा स्रावित होता है। यह शुक्राणु उत्पादन को उत्तेजित करता है और लड़कों में दाढ़ी-मूंछ और भारी आवाज जैसे लक्षणों को विकसित करता है।",
        "explanation_gu": "ટેસ્ટોસ્ટેરોન એ શુક્રપિંડ દ્વારા મુક્ત થતો મુખ્ય નર જાતીય અંતઃસ્ત્રાવ છે, જે શુક્રકોષોના નિર્માણનું નિયમન કરે છે અને દાઢી-મૂંછ તથા ઘેરા અવાજ જેવા લક્ષણો વિકસાવે છે."
    })

    # 6. Reflection
    blocks.append({
        "id": next_id(),
        "type": "reflection",
        "title": "Why Millions of Sperms Compete for a Single Egg",
        "title_hi": "एक अकेले अंडे के लिए करोड़ों शुक्राणुओं की दौड़ क्यों?",
        "title_gu": "માત્ર એક અંડકોષ માટે કરોડો શુક્રકોષો વચ્ચેની સ્પર્ધા શા માટે?",
        "body": "In every human ejaculation, nearly 300 million sperms are released, yet only ONE will fertilize the egg! Why such colossal overproduction? Because the journey is extraordinarily perilous: millions are killed by acidic vaginal fluids, millions get trapped in cervical mucus, half swim up the wrong Fallopian tube (only one tube contains an egg each month), and thousands exhaust their energy reserves before swimming the 15-centimeter distance. Extreme numbers guarantee that only the healthiest, most motile sperm achieves fertilization.",
        "body_hi": "हर स्खलन में लगभग 30 करोड़ शुक्राणु निकलते हैं, फिर भी केवल एक ही शुक्राणु अंडे को निषेचित करता है! प्रकृति इतना बड़ा निर्माण क्यों करती है? क्योंकि यह यात्रा अत्यंत कठिन है: लाखों शुक्राणु योनि के अम्ल से मर जाते हैं, आधे गलत डिंबवाहिनी में चले जाते हैं, और हजारों तैरते-तैरते थक जाते हैं। अत्यधिक संख्या यह सुनिश्चित करती है कि केवल सबसे स्वस्थ और तेज शुक्राणु ही जीवन की शुरुआत करे।",
        "body_gu": "દરેક સ્ખલનમાં 30 કરોડ જેટલા શુક્રકોષો મુક્ત થાય છે, છતાં માત્ર એક જ શુક્રકોષ અંડકોષનું ફલન કરે છે! આટલી મોટી સંખ્યા કેમ? કારણ કે માર્ગ ખૂબ જોખમી છે: લાખો શુક્રકોષો એસિડિક વાતાવરણમાં નાશ પામે છે, અડધા ખોટી અંડવાહિની તરફ જતા રહે છે અને હજારો રસ્તામાં જ થાકી જાય છે. આ વિશાળ સંખ્યા સુનિશ્ચિત કરે છે કે સૌથી તંદુરસ્ત અને શ્રેષ્ઠ શુક્રકોષ જ ફલન કરી શકે."
    })

    # 7. Connection
    blocks.append({
        "id": next_id(),
        "type": "connection",
        "title": "Male Infertility and Modern Assisted Reproductive Technologies",
        "title_hi": "पुरुष बांझपन और आधुनिक सहायक जनन तकनीकें",
        "title_gu": "પુરુષ વંધ્યત્વ અને આધુનિક આસિસ્ટેડ રિપ્રોડક્ટિવ ટેકનોલોજી",
        "body": "When a man produces fewer than 15 million sperms per mL (oligospermia) or when sperm motility is poor, natural fertilization becomes difficult. Medical science overcomes this using Intra-Cytoplasmic Sperm Injection (ICSI), where embryologists use microscopic needles to inject a single healthy sperm directly into an egg cell in a petri dish, enabling couples to have biological children.",
        "body_hi": "यदि किसी पुरुष में शुक्राणुओं की संख्या 1.5 करोड़ प्रति मिलीलीटर से कम हो जाए या उनकी गतिशीलता कम हो, तो प्राकृतिक गर्भधारण कठिन हो जाता है। चिकित्सा विज्ञान में 'आईसीएसआई' (ICSI) तकनीक द्वारा माइक्रोस्कोप के नीचे एक अकेले स्वस्थ शुक्राणु को सीधे अंडे के अंदर इंजेक्ट करके परखनली में भ्रूण तैयार कर लिया जाता है।",
        "body_gu": "જો કોઈ પુરુષમાં શુક્રકોષોની સંખ્યા ઓછી હોય કે તેમની ગતિશીલતા નબળી હોય, તો કુદરતી ગર્ભાધાન મુશ્કેલ બને છે. આધુનિક ચિકિત્સા વિજ્ઞાનમાં ICSI પદ્ધતિ દ્વારા માઇક્રોસ્કોપ હેઠળ એક જ તંદુરસ્ત શુક્રકોષને ઇન્જેક્શન વડે સીધો અંડકોષમાં દાખલ કરી સફળતાપૂર્વક ગર્ભ સ્થાપિત કરાય છે."
    })

    # 8. Mastery Challenge (MCQ)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Which of the following structures in the male human body acts as a common conduit for both urine and semen, though never at the same time?",
        "question_hi": "मानव नर शरीर में कौन सी संरचना मूत्र और वीर्य दोनों के लिए एक सामान्य मार्ग के रूप में कार्य करती है?",
        "question_gu": "માનવ નર શરીરમાં કઈ રચના મૂત્ર અને વીર્ય બંને માટે સામાન્ય વહન માર્ગ તરીકે કાર્ય કરે છે?",
        "options": [
            "Urethra",
            "Ureter",
            "Vas deferens",
            "Scrotum"
        ],
        "options_hi": [
            "मूत्रमार्ग (Urethra)",
            "मूત્રવાહિની (Ureter)",
            "शुक्रवाहिका (Vas deferens)",
            "वृषण कोष (Scrotum)"
        ],
        "options_gu": [
            "મૂત્રમાર્ગ (Urethra)",
            "મૂત્રવાહિની (Ureter)",
            "શુક્રવાહિની (Vas deferens)",
            "વૃષણકોથળી (Scrotum)"
        ],
        "correct_index": 0,
        "explanation": "In human males, the urethra passes through the penis and carries urine from the bladder as well as semen from the vas deferens and accessory glands. In females, the urethra is entirely separate from the reproductive tract.",
        "explanation_hi": "पुरुषों में मूत्रमार्ग (Urethra) मूत्राशय से मूत्र और शुक्रवाहिका से वीर्य दोनों को शरीर से बाहर ले जाने वाला एक ही साझा मार्ग है। (जबकि मूत्रवाहिनी / Ureter केवल गुर्दे से मूत्राशय तक पेशाब लाती है)।",
        "explanation_gu": "પુરુષોમાં મૂત્રમાર્ગ (Urethra) શિશ્નમાંથી પસાર થાય છે અને તે મૂત્ર તેમજ વીર્ય બંનેના નિકાલ માટેનો એકમાત્ર સામાન્ય માર્ગ છે. (જ્યારે મૂત્રવાહિની / Ureter માત્ર કિડનીમાંથી મૂત્રાશય સુધી પેશાબ લાવે છે)."
    })

    # =========================================================================
    # MODULE 5: FEMALE SYSTEM, FERTILIZATION, EMBRYO & MENSTRUATION (8-STEP)
    # =========================================================================

    # 1. Hook
    blocks.append({
        "id": next_id(),
        "type": "hook",
        "title": "The 28-Day Architectural Cycle of the Human Womb",
        "title_hi": "मानव गर्भाशय का 28 दिवसीय चमत्कारी चक्र",
        "title_gu": "માનવ ગર્ભાશયનું 28 દિવસનું અદભુત ચક્ર",
        "body": "Every single month, the female human body performs a silent architectural marvel: the inner wall of the uterus thickens, weaves thousands of new microscopic blood vessels, and cushions itself with spongy, nutrient-rich tissues to prepare a luxurious biological nursery for a potential new human life. If no fertilized egg arrives, this entire biological cradle is gently dismantled, shed, and rebuilt from scratch in a rhythmic cycle known as Menstruation. Why does nature rebuild this room every month rather than keeping it permanently ready?",
        "body_hi": "हर महीने स्त्री का शरीर एक अद्भुत जैविक निर्माण कार्य करता है: गर्भाशय की आंतरिक दीवार मोटी हो जाती है, हजारों नई सूक्ष्म रक्त वाहिकाएं बनती हैं और संभावित नए जीवन के स्वागत के लिए एक नरम, स्पंजी गद्देदार आवरण तैयार किया जाता है। यदि निषेचित अंडा नहीं पहुंचता, तो इस पूरे आवरण को धीरे-धीरे तोड़कर रक्त और श्लेष्म के रूप में बहा दिया जाता है और फिर से नया बनाया जाता है—इसे मासिक धर्म (Menstruation) कहते हैं। प्रकृति इसे हमेशा तैयार रखने के बजाय हर महीने नया क्यों बनाती है?",
        "body_gu": "દર મહિને સ્ત્રીનું શરીર એક અદભુત જૈવિક નિર્માણ કરે છે: ગર્ભાશયની અંદરની દીવાલ જાડી બને છે, હજારો નવી રુધિરકેશિકાઓ વિકસે છે અને સંભવિત નવા બાળકના સ્વાગત માટે પોષક તત્ત્વોથી સભર નરમ, સ્પંજી ગાદી જેવું સ્તર તૈયાર થાય છે. જો ફલિત અંડકોષ ન આવે, તો આ આખું સ્તર તૂટીને રુધિર અને શ્લેષ્મ સ્વરૂપે બહાર નીકળી જાય છે અને ફરીથી નવું બને છે—જેને માસિક સ્ત્રાવ (Menstruation) કહે છે. કુદરત આ સ્તર કાયમ રાખવાને બદલે દર મહિને નવું કેમ બનાવે છે?"
    })

    # 2. Socratic Question
    blocks.append({
        "id": next_id(),
        "type": "socratic_question",
        "question": "A developing human embryo inside the mother's womb does not breathe air with its lungs, nor does it eat food with its mouth. How does it obtain oxygen, glucose, and eliminate carbon dioxide and nitrogenous wastes?",
        "question_hi": "मां के गर्भ में पल रहा भ्रूण न तो फेफड़ों से सांस लेता है और न ही मुंह से खाना खाता है। फिर उसे ऑक्सीजन और ग्लूकोज कैसे मिलते हैं, और वह कार्बन डाइऑक्साइड तथा अपशिष्ट कैसे बाहर निकालता है?",
        "question_gu": "માતાના ગર્ભાશયમાં વિકાસ પામતો ભ્રૂણ પોતાના ફેફસાંથી શ્વાસ લેતો નથી કે મોં વડે ખોરાક ખાતો નથી. તો તેને ઓક્સિજન અને ગ્લુકોઝ કેવી રીતે મળે છે, અને તે કચરાનો નિકાલ કેવી રીતે કરે છે?",
        "options": [
            "Through a specialized disc-like vascular organ called the Placenta, where maternal and fetal blood vessels exchange nutrients and wastes across villi.",
            "The embryo absorbs nutrients directly from the mother's stomach acids.",
            "The embryo does not require any oxygen or nutrients until the moment of birth.",
            "Nutrients are absorbed through the mother's skin by osmosis."
        ],
        "options_hi": [
            "अपरा (Placenta) नामक एक विशेष तश्तरीनुमा संवहनी अंग के माध्यम से, जहां विली की सहायता से मां और भ्रूण के रक्त के बीच पोषक तत्वों और अपशिष्टों का आदान-प्रदान होता है।",
            "भ्रूण सीधे मां के पेट के अम्ल से पोषक तत्व सोखता है।",
            "जन्म के समय तक भ्रूण को किसी ऑक्सीजन या पोषक तत्व की आवश्यकता नहीं होती।",
            "पोषक तत्व मां की त्वचा से परासरण द्वारा अवशोषित होते हैं।"
        ],
        "options_gu": [
            "જરાયુ (Placenta) નામના વિશિષ્ટ રકાબી જેવા અંગ દ્વારા, જ્યાં પ્રવર્ધો (villi) ની મદદથી માતાના રુધિર અને ભ્રૂણ વચ્ચે પોષક દ્રવ્યો અને કચરાની આપ-લે થાય છે.",
            "ભ્રૂણ સીધો માતાના જઠરના એસિડમાંથી પોષણ મેળવે છે.",
            "જન્મ સુધી ભ્રૂણને ઓક્સિજન કે ખોરાકની કોઈ જરૂર હોતી નથી.",
            "પોષક તત્ત્વો માતાની ચામડી દ્વારા આસૃતિથી શોષાય છે."
        ],
        "correct_index": 0,
        "explanation": "The Placenta is a disc embedded in the uterine wall. It contains finger-like villi on the embryo's side and open blood spaces on the mother's side. This provides a vast surface area for glucose and oxygen to pass from mother to embryo, and metabolic wastes from embryo to mother.",
        "explanation_hi": "अपरा (Placenta) गर्भाशय की दीवार में धंसा एक तश्तरीनुमा अंग है। इसमें भ्रूण की ओर प्रवर्ध (villi) और मां की ओर रक्त से भरे स्थान होते हैं। यह मां से भ्रूण तक ग्लूकोज और ऑक्सीजन पहुंचाने तथा भ्रूण के अपशिष्ट मां के रक्त में भेजने के लिए विशाल सतह प्रदान करता है।",
        "explanation_gu": "જરાયુ (Placenta) ગર્ભાશયની દીવાલમાં જોડાયેલું રકાબી જેવું અંગ છે. તેમાં ભ્રૂણ તરફ પ્રવર્ધો (villi) અને માતા તરફ રુધિર કોટરો હોય છે. આ વિશાળ સપાટી દ્વારા ગ્લુકોઝ અને ઓક્સિજન માતામાંથી ગર્ભમાં જાય છે અને ગર્ભનો ઉત્સર્ગ કચરો માતાના લોહીમાં નિકાલ પામે છે."
    })

    # 3. Discovery
    blocks.append({
        "id": next_id(),
        "type": "discovery",
        "title": "Architecture of the Female Reproductive System",
        "title_hi": "मादा जनन तंत्र की विस्तृत शारीरिक रचना",
        "title_gu": "માદા પ્રજનન તંત્રની વિસ્તૃત શારીરિક રચના",
        "body": "The female reproductive system is designed to produce eggs, host fertilization, nourish the growing fetus, and give birth:\n\n1. Ovaries (Paired): Oval organs in the abdominal cavity.\n   • Contain thousands of immature eggs (follicles) since birth.\n   • At puberty, one mature Ovum (egg) is released alternately every month (Ovulation).\n   • Endocrine hormone secretion: Oestrogen (puberty traits, uterine lining thickening) and Progesterone (maintains pregnancy).\n\n2. Fallopian Tubes / Oviducts (Paired):\n   • Ciliated funnel-like tubes picking up the released ovum.\n   • CRITICAL BOARD FACT: The Fallopian tube is the EXACT SITE OF FERTILIZATION! Sperm meets and fertilizes the egg here.\n\n3. Uterus (Womb):\n   • A hollow, pear-shaped muscular elastic organ.\n   • Site of IMPLANTATION: The fertilized embryo attaches to the vascular inner lining (endometrium) to grow for 9 months.\n\n4. Cervix: The narrow muscular neck connecting uterus to vagina.\n\n5. Vagina: Elastic muscular canal that receives semen during intercourse and serves as the birth canal during parturition.",
        "body_hi": "मादा जनन तंत्र की मुख्य संरचनाएं और कार्य:\n\n1. अंडाशय (Ovaries): उदर गुहा में स्थित एक जोड़ी अंग।\n   • जन्म से ही इनमें हजारों अपरिपक्व अंडे होते हैं।\n   • यौवनारंभ पर हर महीने दोनों अंडाशयों में से किसी एक से एक परिपक्व अंडाणु निकलता है (अंडोत्सर्ग / Ovulation)।\n   • हार्मोन स्राव: एस्ट्रोजन और प्रोजेस्टेरोन।\n\n2. डिंबवाहिनी / फैलोपियन ट्यूब (Fallopian Tubes):\n   • अंडोत्सर्ग के बाद अंडे को पकड़कर गर्भाशय की ओर ले जाने वाली नलिकाएं।\n   • अति महत्वपूर्ण तथ्य: फैलोपियन ट्यूब ही निषेचन (FERTILIZATION) का वास्तविक स्थान है! यहीं शुक्राणु अंडे से मिलता है।\n\n3. गर्भाशय (Uterus / Womb):\n   • नाशपाती के आकार का लोचदार पेशीय अंग।\n   • आरोपण (Implantation) का स्थान: निषेचित भ्रूण गर्भाशय की आंतरिक परत में स्थापित होकर 9 महीने तक विकसित होता है।\n\n4. गर्भाशय ग्रीवा (Cervix): गर्भाशय का निचला संकरा सिरा जो योनि में खुलता है।\n\n5. योनि (Vagina): जन्म नलिका और मैथुन के समय वीर्य ग्रहण करने वाला पेशीय मार्ग।",
        "body_gu": "માદા પ્રજનન તંત્રના મુખ્ય ભાગો અને કાર્યો:\n\n1. અંડપિંડ (Ovaries): ઉદરગુહામાં આવેલી એક જોડ.\n   • જન્મથી જ તેમાં હજારો અપરિપક્વ અંડકોષો હોય છે.\n   • યૌવનારંભે વારાફરતી દર મહિને એક અંડપિંડમાંથી એક પરિપક્વ અંડકોષ મુક્ત થાય છે (અંડપાત / Ovulation).\n   • અંતઃસ્ત્રાવો: ઇસ્ટ્રોજન અને પ્રોજેસ્ટેરોન મુક્ત કરે છે.\n\n2. અંડવાહિની / ફેલોપિયન નળી (Fallopian Tubes):\n   • અંડકોષને અંડપિંડમાંથી ગર્ભાશય તરફ લઈ જતી નળી.\n   • બોર્ડ પરીક્ષાનો મહત્વનો પ્રશ્ન: અંડવાહિની એ ફલન (FERTILIZATION) થવાનું મૂળ સ્થાન છે! શુક્રકોષ અહીં જ અંડકોષને ફલિત કરે છે.\n\n3. ગર્ભાશય (Uterus):\n   • નાસપતી આકારની સ્થિતિસ્થાપક સ્નાયુમય કોથળી.\n   • ગર્ભસ્થાપન (Implantation) નું સ્થાન: ફલિત ભ્રૂણ ગર્ભાશયની દીવાલમાં ચોંટીને 9 મહિના સુધી બાળક તરીકે વિકાસ પામે છે.\n\n4. ગ્રીવા (Cervix): ગર્ભાશયનું સાંકડું મુખ જે યોનિમાર્ગમાં ખૂલે છે.\n\n5. યોનિમાર્ગ (Vagina): પ્રસૂતિ નળી અને શુક્રકોષ મેળવવાનો માર્ગ."
    })

    # 4. Theory
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "Gestation, Placenta, and What Happens When the Egg is NOT Fertilized",
        "title_hi": "गर्भकाल, अपरा और जब अंडे का निषेचन नहीं होता तो क्या होता है",
        "title_gu": "ગર્ભાવસ્થા, જરાયુ અને જ્યારે અંડકોષનું ફલન ન થાય ત્યારે શું બને છે",
        "body": "Here are the two possible outcomes of every monthly ovulation:\n\nSCENARIO A: FERTILIZATION OCCURS\n• Sperm fertilizes egg in Fallopian tube -> Zygote.\n• Zygote divides repeatedly by mitosis into a ball of cells while traveling down to the uterus.\n• Implantation: The young embryo embeds itself into the thick, vascular lining of the uterus.\n• Placenta Development: Disc-like vascular organ forms between embryo and uterine wall. Finger-like villi maximize surface area for nutrient/gas exchange with maternal blood.\n• Gestation: Embryo develops inside uterus for roughly 9 months (~280 days).\n• Parturition (Birth): Strong, rhythmic muscular contractions of the uterine wall push the baby out through the cervix and vagina.\n\nSCENARIO B: NO FERTILIZATION OCCURS (MENSTRUATION)\n• The released unfertilized egg survives for about 24 hours.\n• Since the egg is not fertilized, the thick, spongy, vascular uterine lining is no longer needed.\n• The lining slowly breaks down, and along with unfertilized egg, blood, and mucus, it exits the body through the vagina.\n• This monthly bleeding cycle is called Menstruation. It occurs roughly every 28 days and typically lasts for 2 to 8 days.",
        "body_hi": "हर महीने अंडोत्सर्ग के दो संभावित परिणाम:\n\nस्थिति 1: जब निषेचन होता है\n• डिंबवाहिनी में शुक्राणु अंडे को निषेचित करता है -> युग्मनज (Zygote) बनता है।\n• युग्मनज बार-बार विभाजित होकर कोशिकाओं का गोला बनता है और गर्भाशय में पहुंचता है।\n• आरोपण (Implantation): भ्रूण गर्भाशय की स्पंजी रक्तयुक्त दीवार में धंस जाता है।\n• अपरा (Placenta): मां और भ्रूण के बीच पोषक तत्वों और गैसों के आदान-प्रदान के लिए अपरा विकसित होती है।\n• गर्भकाल (Gestation): लगभग 9 महीने (280 दिन) तक भ्रूण का विकास होता है।\n• प्रसव (Parturition): गर्भाशय की पेशियों के तेज संकुचन से शिशु का जन्म होता है।\n\nस्थिति 2: जब निषेचन नहीं होता (ऋतुस्राव / Menstruation)\n• बिना निषेचित अंडा केवल 24 घंटे जीवित रहता है।\n• गर्भाशय की मोटी और स्पंजी रक्तयुक्त परत की अब कोई आवश्यकता नहीं रहती।\n• यह परत धीरे-धीरे टूटती है और रक्त तथा श्लेष्म के रूप में योनि से बाहर बह जाती है।\n• इस चक्र को ऋतुस्राव (मासिक धर्म / रजोधर्म) कहते हैं। यह लगभग हर 28 दिन में होता है और 2 से 8 दिन तक रहता है।",
        "body_gu": "દર મહિને મુક્ત થતા અંડકોષના બે સંભવિત પરિણામો:\n\nપરિસ્થિતિ 1: જ્યારે ફલન થાય છે\n• અંડવાહિનીમાં શુક્રકોષ અંડકોષને ફલિત કરે છે -> યુગ્મનજ (Zygote) બને છે.\n• યુગ્મનજ વિભાજન પામતો પામતો ગર્ભાશય તરફ આગળ વધે છે.\n• ગર્ભસ્થાપન (Implantation): ભ્રૂણ ગર્ભાશયની જાડી, રુધિરવાળી દીવાલમાં સ્થાપિત થાય છે.\n• જરાયુ (Placenta): માતા અને ભ્રૂણ વચ્ચે પોષક દ્રવ્યો અને શ્વસન વાયુઓની આપ-લે માટે જરાયુ અંગ રચાય છે.\n• ગર્ભધારણ કાળ: આશરે 9 મહિના (280 દિવસ) સુધી બાળક વિકસે છે.\n• પ્રસૂતિ (Parturition): ગર્ભાશયની દીવાલના લયબદ્ધ સ્નાયુ સંકોચનથી બાળકનો જન્મ થાય છે.\n\nપરિસ્થિતિ 2: જ્યારે ફલન થતું નથી (ઋતુસ્ત્રાવ / Menstruation)\n• અફલિત અંડકોષ માત્ર 24 કલાક જીવે છે.\n• ફલન ન થવાથી ગર્ભાશયની જાડી, રુધિરકેશિકાઓવાળી સ્પંજી દીવાલની હવે કોઈ જરૂર રહેતી નથી.\n• આ દીવાલ ધીમે ધીમે તૂટે છે અને રક્ત તથા શ્લેષ્મ સ્વરૂપે યોનિમાર્ગ દ્વારા બહાર વહી જાય છે.\n• આ માસિક ચક્રને ઋતુસ્ત્રાવ (રજોધર્મ) કહે છે. તે આશરે દર 28 દિવસે થાય છે અને 2 થી 8 દિવસ ચાલે છે."
    })

    # Teacher Tip
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Teacher Tip: Site of Fertilization vs Site of Implantation",
        "title_hi": "शिक्षक टिप: निषेचन का स्थान बनाम आरोपण का स्थान",
        "title_gu": "શિક્ષક ટિપ: ફલનનું સ્થાન વિરુદ્ધ ગર્ભસ્થાપનનું સ્થાન",
        "body": "This is the single most common trick question in Class 10 Science:\n• WHERE DOES FERTILIZATION OCCUR? -> In the Fallopian Tube (Oviduct).\n• WHERE DOES IMPLANTATION / EMBRYO DEVELOPMENT OCCUR? -> In the Uterus (Womb).\nNever write Uterus for fertilization!",
        "body_hi": "कक्षा 10 की परीक्षा का सबसे आम भ्रामक प्रश्न:\n• निषेचन (Fertilization) कहाँ होता है? -> डिंबवाहिनी / फैलोपियन ट्यूब (Fallopian tube) में।\n• आरोपण (Implantation) और भ्रूण का विकास कहाँ होता है? -> गर्भाशय (Uterus) में।\nनिषेचन के उत्तर में कभी गर्भाशय न लिखें!",
        "body_gu": "ધોરણ 10 ની બોર્ડ પરીક્ષાનો સૌથી સામાન્ય પ્રશ્ન:\n• ફલન (Fertilization) ક્યાં થાય છે? -> અંડવાહિની / ફેલોપિયન નળી (Fallopian tube) માં.\n• ગર્ભસ્થાપન (Implantation) અને શિશુનો વિકાસ ક્યાં થાય છે? -> ગર્ભાશય (Uterus) માં.\nફલન માટે ક્યારેય ગર્ભાશય ન લખવું!"
    })

    # 5. Knowledge Check (MCQ)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "In the human female reproductive tract, where does fertilization of the egg by sperm normally take place?",
        "question_hi": "मानव मादा जनन तंत्र में शुक्राणु द्वारा अंडे का निषेचन सामान्यतः किस स्थान पर होता है?",
        "question_gu": "માનવ માદા પ્રજનન તંત્રમાં શુક્રકોષ દ્વારા અંડકોષનું ફલન સામાન્ય રીતે ક્યાં થાય છે?",
        "options": [
            "Fallopian tube (Oviduct)",
            "Uterus (Womb)",
            "Ovary",
            "Cervix"
        ],
        "options_hi": [
            "डिंबवाहिनी / फैलोपियन ट्यूब (Fallopian tube)",
            "गर्भाशय (Uterus)",
            "अंडाशय (Ovary)",
            "ग्रीवा (Cervix)"
        ],
        "options_gu": [
            "અંડવાહિની / ફેલોપિયન નળી (Fallopian tube)",
            "ગર્ભાશય (Uterus)",
            "અંડપિંડ (Ovary)",
            "ગ્રીવા (Cervix)"
        ],
        "correct_index": 0,
        "explanation": "Fertilization occurs in the ampullary region of the Fallopian tube. Once fertilized, the resulting zygote divides as it travels towards the uterus for implantation.",
        "explanation_hi": "निषेचन डिंबवाहिनी (फैलोपियन ट्यूब) में होता है। निषेचित होने के बाद युग्मनज विभाजित होते हुए गर्भाशय में आरोपण के लिए आगे बढ़ता है।",
        "explanation_gu": "ફલન અંડવાહિનીમાં થાય છે. ફલિત થયા પછી યુગ્મનજ કોષવિભાજન પામતાં પામતાં ગર્ભાશય તરફ આગળ વધી ત્યાં સ્થાપિત થાય છે."
    })

    # 6. Reflection
    blocks.append({
        "id": next_id(),
        "type": "reflection",
        "title": "Why the Placenta is a Biological Masterpiece",
        "title_hi": "अपरा (Placenta) प्रकृति की एक बेमिसाल इंजीनियरिंग क्यों है?",
        "title_gu": "જરાયુ (Placenta) કુદરતની અજોડ બાયોલોજીકલ માસ્ટરપીસ કેમ છે?",
        "body": "The developing fetus has its own distinct blood type which may differ from the mother's (e.g. fetus is type A+ while mother is O-). If maternal and fetal blood directly mixed, the mother's immune antibodies would attack and destroy the fetus! The placenta is a selective semi-permeable barrier: maternal blood pools in open spaces surrounding fetal villi, allowing oxygen, amino acids, and glucose to diffuse across cell membranes without letting maternal blood cells or lethal immune killer cells physically mix.",
        "body_hi": "गर्भ में पल रहे भ्रूण का रक्त समूह मां से अलग हो सकता है (जैसे मां O- और भ्रूण A+)। यदि मां और बच्चे का खून सीधे मिल जाए, तो मां का प्रतिरक्षा तंत्र बच्चे के रक्त को विदेशी मानकर नष्ट कर देगा! अपरा (Placenta) एक चयनात्मक अवरोधक की तरह काम करती है: मां और बच्चे का रक्त कभी सीधे नहीं मिलता, केवल झिल्ली के आर-पार पोषक तत्वों और ऑक्सीजन का विसरण होता है।",
        "body_gu": "ગર્ભમાં રહેલા બાળકનું બ્લડ ગ્રૂપ માતા કરતાં અલગ હોઈ શકે છે (દા.ત. માતાનું O- અને બાળકનું A+). જો માતા અને બાળકનું લોહી સીધું ભળી જાય, તો માતાના એન્ટિબોડી બાળકના લોહીના કણોનો નાશ કરી દે! જરાયુ (Placenta) એક વિશિષ્ટ ફિલ્ટર જેવું કામ કરે છે: માતા અને બાળકનું રુધિર ક્યારેય સીધું ભળતું નથી, માત્ર દીવાલ દ્વારા પોષક દ્રવ્યો અને ઓક્સિજનનું પ્રસરણ થાય છે."
    })

    # 7. Connection
    blocks.append({
        "id": next_id(),
        "type": "connection",
        "title": "Menstrual Hygiene and Female Health Rights",
        "title_hi": "मासिक धर्म स्वच्छता और महिला स्वास्थ्य अधिकार",
        "title_gu": "માસિક સ્ત્રાવ સ્વચ્છતા અને મહિલા સ્વાસ્થ્ય અધિકાર",
        "body": "Menstruation is a completely natural, healthy biological cycle, yet social stigmas and lack of sanitary hygiene products cause thousands of girls in developing nations to drop out of school. Poor menstrual hygiene using unsterilized cloths leads to severe Pelvic Inflammatory Disease (PID) and cervical infections. Modern public health initiatives focus on breaking superstitions and providing biodegradable sanitary napkins across schools.",
        "body_hi": "मासिक धर्म पूरी तरह से प्राकृतिक और स्वस्थ जैविक प्रक्रिया है, फिर भी सामाजिक भ्रांतियों और सैनिटरी पैड की कमी के कारण लाखों लड़कियां पढ़ाई छोड़ने को मजबूर होती हैं। अस्वच्छ कपड़ों के उपयोग से गर्भाशय और जननांगों में गंभीर संक्रमण हो सकता है। आज सार्वजनिक स्वास्थ्य अभियान अंधविश्वासों को तोड़ने और विद्यालयों में स्वच्छ पैड उपलब्ध कराने पर जोर दे रहे हैं।",
        "body_gu": "માસિક સ્ત્રાવ એ સંપૂર્ણપણે કુદરતી અને તંદુરસ્ત જૈવિક પ્રક્રિયા છે, તેમ છતાં સામાજિક કુરિવાજો અને સેનિટરી પેડના અભાવે ઘણી દીકરીઓ શાળા છોડી દેતી હતી. અસ્વચ્છ કાપડ વાપરવાથી ગર્ભાશયમાં ગંભીર ચેપ લાગી શકે છે. આજે સરકારી જાગૃતિ અભિયાનો દ્વારા અંધશ્રદ્ધા દૂર કરી શાળાઓમાં સ્વચ્છ સેનિટરી નેપકિન પૂરા પાડવામાં આવે છે."
    })

    # 8. Mastery Challenge (MCQ)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "What is the primary physiological cause of menstruation in human females?",
        "question_hi": "मानव मादा में मासिक धर्म (ऋतुस्राव) का मुख्य शारीरिक कारण क्या है?",
        "question_gu": "માનવ સ્ત્રીઓમાં માસિક સ્ત્રાવ (ઋતુસ્ત્રાવ) થવાનું મુખ્ય શારીરિક કારણ શું છે?",
        "options": [
            "The unfertilized egg causes degeneration of the progesterone-supported vascular uterine lining, which breaks down and sheds as blood and mucus.",
            "The ovaries permanently run out of all egg cells.",
            "The urinary bladder contracts vigorously to clean out the uterus.",
            "Excessive physical exercise breaks the fallopian tubes."
        ],
        "options_hi": [
            "अंडे का निषेचन न होने के कारण गर्भाशय की मोटी और स्पंजी रक्तयुक्त परत टूट जाती है और रक्त तथा श्लेष्म के रूप में बाहर निकलती है।",
            "अंडाशय में सभी अंड कोशिकाएं हमेशा के लिए समाप्त हो जाती हैं।",
            "मूत्राशय गर्भाशय को साफ करने के लिए संकुचित होता है।",
            "अधिक व्यायाम से डिंबवाहिनी टूट जाती है।"
        ],
        "options_gu": [
            "અંડકોષનું ફલન ન થવાને કારણે ગર્ભાશયની જાડી, રુધિરકેશિકાઓવાળી સ્પંજી દીવાલ તૂટી જાય છે અને રુધિર તથા શ્લેષ્મ સ્વરૂપે વહી જાય છે.",
            "અંડપિંડમાં અંડકોષો કાયમ માટે ખૂટી જાય છે.",
            "મૂત્રાશય ગર્ભાશયને સાફ કરવા સંકોચાય છે.",
            "વધુ પડતી કસરતથી અંડવાહિની તૂટી જાય છે."
        ],
        "correct_index": 0,
        "explanation": "If fertilization does not happen, the unfertilized egg perishes, progesterone levels drop, and the prepared spongy endometrial lining of the uterus sheds via the vagina.",
        "explanation_hi": "निषेचन न होने पर प्रोजेस्टेरोन हार्मोन गिर जाता है, जिससे गर्भाशय की तैयार स्पंजी परत टूटकर योनि मार्ग से बाहर बह जाती है।",
        "explanation_gu": "ફલન ન થતાં અંતઃસ્ત્રાવો ઘટતાં ગર્ભાશયની તૈયાર થયેલી સ્પંજી દીવાલ તૂટીને યોનિમાર્ગ દ્વારા ઋતુસ્ત્રાવ તરીકે બહાર વહી જાય છે."
    })

    # =========================================================================
    # MODULE 6: REPRODUCTIVE HEALTH & CONTRACEPTION (8-STEP PEDAGOGY)
    # =========================================================================

    # 1. Hook
    blocks.append({
        "id": next_id(),
        "type": "hook",
        "title": "The Balance of Life: Population, Well-Being, and Intimacy",
        "title_hi": "जीवन का संतुलन: जनसंख्या, स्वास्थ्य और सुरक्षित संबंध",
        "title_gu": "જીવનનું સંતુલન: વસ્તી, સુખાકારી અને સુરક્ષિત સંબંધો",
        "body": "Human sexual reproduction involves deep physical, emotional, and social dimensions. Having children is a tremendous responsibility requiring mature emotional stability, financial independence, and maternal physical strength. Unplanned, frequent pregnancies severely deplete a mother's nutritional reserves, leading to high maternal and infant mortality. Furthermore, sexual acts can transmit deadly microscopic pathogens directly between bloodstreams. How has modern science empowered humanity to protect health, choose family size, and prevent deadly infections?",
        "body_hi": "मानव लैंगिक प्रजनन के गहरे शारीरिक, भावनात्मक और सामाजिक आयाम होते हैं। बच्चे को जन्म देना और पालना एक भारी जिम्मेदारी है जिसके लिए मानसिक परिपक्वતા, वित्तीय स्थिरता और मां के अच्छे स्वास्थ्य की आवश्यकता होती है। बार-बार और अनियोजित गर्भधारण से मां का स्वास्थ्य बुरी तरह बिगड़ जाता है। इसके अलावा, यौन क्रियाओं से घातक सूक्ष्म रोगाणु एक व्यक्ति से दूसरे में फैल सकते हैं। आधुनिक विज्ञान ने स्वास्थ्य की रक्षा करने, परिवार नियोजन करने और घातक संक्रमणों से बचने के लिए क्या उपाय खोजे हैं?",
        "body_gu": "માનવ લિંગી પ્રજનન શારીરિક, ભાવનાત્મક અને સામાજિક પરિમાણો ધરાવે છે. બાળકને જન્મ આપવો અને ઉછેરવો એ ખૂબ મોટી જવાબદારી છે જેના માટે માતાનું સારું સ્વાસ્થ્ય અને આર્થિક સ્થિરતા જરૂરી છે. વારંવાર અને અનિચ્છનીય ગર્ભાવસ્થાથી માતાનું સ્વાસ્થ્ય જોખમાય છે. ઉપરાંત, જાતીય સંબંધોથી ઘાતક રોગોનો ફેલાવો થઈ શકે છે. આધુનિક વિજ્ઞાને સ્વાસ્થ્યની સુરક્ષા કરવા, કુટુંબ નિયોજન કરવા અને રોગોથી બચવા માટે કઈ પદ્ધતિઓ શોધી છે?"
    })

    # 2. Socratic Question
    blocks.append({
        "id": next_id(),
        "type": "socratic_question",
        "question": "A woman has a Copper-T Intrauterine Device (IUCD) fitted inside her uterus by a doctor. Will this Copper-T device protect her from sexually transmitted diseases (STDs) like HIV-AIDS or Syphilis?",
        "question_hi": "एक महिला के गर्भाशय में डॉक्टर द्वारा कॉपर-टी (Copper-T) उपकरण लगाया गया है। क्या यह कॉपर-टी उसे एचआईवी-एड्स या सिफलिस जैसे यौन संचारित रोगों (STDs) से बचाएगी?",
        "question_gu": "એક મહિલાએ પોતાના ગર્ભાશયમાં ડૉક્ટર પાસે કૉપર-ટી (Copper-T) મુકાવી છે. શું આ કૉપર-ટી તેને HIV-AIDS કે સિફિલિસ જેવા જાતીય સંક્રમિત રોગો (STDs) સામે રક્ષણ આપશે?",
        "options": [
            "No; Copper-T only prevents embryo implantation inside the uterus; it does not block fluid contact or pathogen transmission between partners.",
            "Yes; Copper metal actively kills all viruses and bacteria present in body fluids.",
            "Yes; any contraceptive method provides 100% immunity against all infectious diseases.",
            "No; Copper-T accelerates the transmission of all bacterial diseases."
        ],
        "options_hi": [
            "नहीं; कॉपर-टी केवल गर्भाशय में भ्रूण के आरोपण को रोकती है; यह शरीर के तरल पदार्थों या रोगाणुओं के आदान-प्रदान को नहीं रोकती।",
            "हाँ; तांबा धातु शरीर के सभी वायरस और बैक्टीरिया को तुरंत मार देती है।",
            "हाँ; कोई भी गर्भनिरोधक तरीका सभी संक्रामक रोगों से 100% सुरक्षा देता है।",
            "नहीं; कॉपर-टी से बीमारियां और तेजी से फैलती हैं।"
        ],
        "options_gu": [
            "ના; કૉપર-ટી માત્ર ગર્ભાશયમાં ભ્રૂણ સ્થાપનને અટકાવે છે; તે પ્રવાહીના સંપર્ક કે રોગના વાયરસ-બેક્ટેરિયાના વહનને રોકી શકતી નથી.",
            "હા; તાંબુ ધાતુ બધા જ વાયરસ અને બેક્ટેરિયાને મારી નાખે છે.",
            "હા; કોઈપણ ગર્ભનિરોધક પદ્ધતિ તમામ ચેપી રોગો સામે રક્ષણ આપે છે.",
            "ના; કૉપર-ટી રોગોનો ફેલાવો વધારે છે."
        ],
        "correct_index": 0,
        "explanation": "Copper-T is an Intrauterine Device that prevents pregnancy by releasing copper ions that irritate the uterine lining and suppress sperm motility. It provides ZERO physical barrier against mucosal contact; hence, it cannot prevent STDs. Only barrier methods like condoms prevent STDs.",
        "explanation_hi": "कॉपर-टी केवल गर्भधारण को रोकने के लिए गर्भाशय में लगाई जाती है। यह जननांगों के शारीरिक संपर्क या तरल पदार्थों के आदान-प्रदान को नहीं रोकती, इसलिए यह एचआईवी-एड्स या सिफलिस जैसे एसटीडी से कोई सुरक्षा नहीं देती। केवल कंडोम ही एसटीडी से बचा सकता है।",
        "explanation_gu": "કૉપર-ટી માત્ર ગર્ભાશયમાં ગર્ભસ્થાપન રોકવા માટે છે. તે શારીરિક પ્રવાહીના સીધા સંપર્કને રોકતી નથી, તેથી HIV-AIDS કે સિફિલિસ જેવા રોગો સામે કોઈ રક્ષણ આપતી નથી. માત્ર કૉન્ડોમ જ STDs સામે રક્ષણ આપે છે."
    })

    # 3. Discovery
    blocks.append({
        "id": next_id(),
        "type": "discovery",
        "title": "Classification of Sexually Transmitted Diseases (STDs)",
        "title_hi": "यौन संचारित रोगों (STDs) का वैज्ञानिक वर्गीकरण",
        "title_gu": "જાતીય સંક્રમિત રોગો (STDs) નું વૈજ્ઞાનિક વર્ગીકરણ",
        "body": "Sexually Transmitted Diseases (STDs / STIs) are infections transmitted through sexual contact:\n\n1. Bacterial Infections:\n   • Gonorrhoea: Caused by bacterium Neisseria gonorrhoeae. Symptoms include burning sensation during urination and purulent discharge.\n   • Syphilis: Caused by bacterium Treponema pallidum. Characterized by genital sores (chancres), skin rashes, and eventual neurological/cardiac damage if untreated. Can be treated with antibiotics.\n\n2. Viral Infections:\n   • Genital Warts: Caused by Human Papillomavirus (HPV). Causes fleshy growths in the genital area.\n   • HIV-AIDS (Human Immunodeficiency Virus): Attacks CD4+ T-helper immune cells, collapsing the body's immune defense system. Incurable; leaves the patient vulnerable to fatal secondary infections.\n\nPrevention: Using mechanical barriers (condoms) during sexual acts provides the only effective protection against transmission of both bacterial and viral STDs.",
        "body_hi": "यौन संचारित रोग (STDs) और उनके प्रकार:\n\n1. जीवाणु जनित (Bacterial) संक्रमण:\n   • गोनोरिया (Gonorrhoea): नीसेरिया गोनोरिया बैक्टीरिया द्वारा होता है। पेशाब में जलन और मवाद आना।\n   • सिफलिस (Syphilis): ट्रेपोनेमा पैलिडम बैक्टीरिया द्वारा होता है। जननांगों पर घाव और चकत्ते। एंटीबायोटिक दवाओं से इलाज संभव है।\n\n2. विषाणु जनित (Viral) संक्रमण:\n   • मस्से (Warts): ह्यूमन पेपिलोमावायरस (HPV) द्वारा।\n   • एचआईवी-एड्स (HIV-AIDS): ह्यूमन इम्यूनोडेफिशिएंसी वायरस द्वारा। यह शरीर की रोग प्रतिरोधક क्षमता को पूरी तरह नष्ट कर देता है। यह असाध्य (incurable) है।\n\nरोकथाम: कंडोम (यांत्रिक अवरोध) का उपयोग एसटीडी और अनचाहे गर्भ दोनों से बचने का सबसे प्रभावी उपाय है।",
        "body_gu": "જાતીય સંક્રમિત રોગો (STDs) અને તેના પ્રકારો:\n\n1. બેક્ટેરિયાજન્ય ચેપ:\n   • ગોનોરિયા (Gonorrhoea): પેશાબમાં બળતરા અને રસી થવી.\n   • સિફિલિસ (Syphilis): જનનાંગો પર ચાંદા પડવા અને ચકામા થવા. એન્ટિબાયોટિક્સથી સારવાર શક્ય છે.\n\n2. વાયરસજન્ય ચેપ:\n   • મસા (Warts): હ્યુમન પેપિલોમા વાયરસ દ્વારા.\n   • HIV-AIDS: વાયરસ શરીરના રોગપ્રતિકારક તંત્રનો નાશ કરે છે. આ રોગ અસાધ્ય છે.\n\nઅટકાવવાના ઉપાયો: કૉન્ડોમ (યાંત્રિક અંતરાય) નો ઉપયોગ STDs અને અનિચ્છનીય ગર્ભ બંને સામે શ્રેષ્ઠ સુરક્ષા આપે છે."
    })

    # 4. Theory
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "Comprehensive Guide to Contraceptive Methods",
        "title_hi": "गर्भनिरोधक विधियों की संपूर्ण वैज्ञानिक मार्गदर्शिका",
        "title_gu": "ગર્ભનિરોધક પદ્ધતિઓની સંપૂર્ણ વૈજ્ઞાનિક માર્ગદર્શિકા",
        "body": "Contraception is the prevention of pregnancy. Contraceptive methods are grouped into four categories:\n\n1. Mechanical / Barrier Methods:\n   • Condoms (worn over the penis) or cervical caps/diaphragms (fitted into the vagina).\n   • Mechanism: Creates a physical barrier preventing sperms from reaching the egg.\n   • UNIQUE ADVANTAGE: Condoms are the ONLY contraceptive method that also protects against Sexually Transmitted Diseases (STDs/HIV)!\n\n2. Chemical / Hormonal Methods (Oral Contraceptive Pills):\n   • Pills taken orally containing synthetic hormones (progestins/estrogens).\n   • Mechanism: Alters hormonal balance so that the ovaries stop releasing eggs (prevents ovulation).\n   • Disadvantage: Does not protect against STDs; can cause side effects due to altered hormone levels.\n\n3. Intrauterine Contraceptive Devices (IUCDs):\n   • Copper-T or Loop inserted into the uterus by a trained doctor or nurse.\n   • Mechanism: Releases copper ions that suppress sperm motility and prevents embryo implantation in the uterine wall.\n   • Disadvantage: Can cause uterine irritation, bleeding, or pelvic discomfort; does NOT protect against STDs.\n\n4. Surgical Methods (Sterilization - Permanent):\n   • Vasectomy in Males: A small portion of both Vas Deferens tubes is cut and tied. Sperms cannot travel from testes to urethra.\n   • Tubectomy in Females: A small portion of both Fallopian Tubes is cut and tied. The egg cannot reach the uterus, and sperms cannot reach the egg.\n   • Advantage: Highly effective and permanent. Disadvantage: Difficult to reverse.",
        "body_hi": "गर्भनिरोधक की चार प्रमुख श्रेणियां:\n\n1. यांत्रिक अवरोध विधियां (Mechanical Barriers):\n   • कंडोम (पुरुषों के लिए) या डायाफ्राम/कैप (महिलाओं के लिए)।\n   • कार्यप्रणाली: शुक्राणुओं को अंडे तक पहुंचने से भौतिक रूप से रोकना।\n   • सबसे बड़ा लाभ: कंडोम एकमात्र ऐसा तरीका है जो गर्भधारण के साथ-साथ एसटीडी (एचआईवी) से भी बचाता है!\n\n2. रासायनिक विधियां (गर्भनिरोधक गोलियां):\n   • महिलाओं द्वारा खाई जाने वाली मौखिक गोलियां।\n   • कार्यप्रणाली: शरीर के हार्मोनल संतुलन को बदल देती हैं जिससे अंडाशय से अंडा निकलना बंद हो जाता है (अंडोत्सर्ग रुकता है)।\n   • नुकसान: एसटीडी से बचाव नहीं करतीं; हार्मोन असंतुलन से दुष्प्रभाव हो सकते हैं।\n\n3. अंतर्गर्भाशयी उपकरण (IUCDs - जैसे कॉपर-टी):\n   • डॉक्टर द्वारा गर्भाशय में स्थापित कॉपर-टी।\n   • कार्यप्रणाली: तांबे के आयन शुक्राणुओं की गतिशीलता रोकते हैं और गर्भाशय में भ्रूण का आरोपण नहीं होने देते।\n   • नुकसान: रक्तस्राव या दर्द हो सकता है; एसटीडी से कोई बचाव नहीं।\n\n4. शल्य चिकित्सा विधियां (Surgical / नसबंदी - स्थायी):\n   • पुरुष नसबंदी (Vasectomy): शुक्रवाहिका (Vas deferens) को काटकर बांध दिया जाता है।\n   • महिला नसबंदी (Tubectomy): डिंबवाहिनी (Fallopian tube) को काटकर बांध दिया जाता है।\n   • लाभ: हमेशा के लिए अत्यंत प्रभावी।",
        "body_gu": "ગર્ભનિરોધક પદ્ધતિઓના ચાર મુખ્ય પ્રકારો:\n\n1. યાંત્રિક અંતરાય પદ્ધતિઓ (Mechanical Barriers):\n   • કૉન્ડોમ (પુરુષો માટે) અથવા ડાયાફ્રામ (સ્ત્રીઓ માટે).\n   • કાર્યપદ્ધતિ: શુક્રકોષોને અંડકોષ સુધી પહોંચતા ભૌતિક રીતે રોકે છે.\n   • સૌથી મોટો ફાયદો: કૉન્ડોમ એકમાત્ર પદ્ધતિ છે જે ગર્ભધારણની સાથે સાથે STDs (HIV) સામે પણ રક્ષણ આપે છે!\n\n2. રાસાયણિક પદ્ધતિઓ (ગર્ભનિરોધક ગોળીઓ):\n   • સ્ત્રીઓ દ્વારા લેવાતી મૌખિક ગોળીઓ.\n   • કાર્યપદ્ધતિ: અંતઃસ્ત્રાવી સંતુલન બદલીને અંડપિંડમાંથી અંડકોષ મુક્ત થતો (અંડપાત) અટકાવે છે.\n   • નુકસાન: STDs સામે રક્ષણ નથી; આડઅસરો થઈ શકે.\n\n3. આઇયુસીડી (IUCDs - કૉપર-ટી):\n   • ડૉક્ટર દ્વારા ગર્ભાશયમાં કૉપર-ટી મૂકવી.\n   • કાર્યપદ્ધતિ: કૉપર આયનો શુક્રકોષોની ગતિશીલતા રોકે છે અને ગર્ભાશયમાં ભ્રૂણ સ્થાપન અટકાવે છે.\n   • નુકસાન: STDs સામે કોઈ રક્ષણ નથી.\n\n4. શસ્ત્રક્રિયા (સર્જિકલ પદ્ધતિઓ - કાયમી):\n   • વાસેક્ટોમી (પુરુષ નસબંધી): શુક્રવાહિની કાપીને બાંધી દેવી.\n   • ટ્યુબેક્ટોમી (સ્ત્રી નસબંધી): અંડવાહિની કાપીને બાંધી દેવી.\n   • ફાયદો: અત્યંત અસરકારક અને કાયમી ઉકેલ."
    })

    # Teacher Tip
    blocks.append({
        "id": next_id(),
        "type": "teacher_tip",
        "title": "Teacher Tip: Female Foeticide and the PCPNDT Act",
        "title_hi": "शिक्षक टिप: कन्या भ्रूण हत्या और पीसीपीएनडीटी अधिनियम",
        "title_gu": "શિક્ષક ટિપ: કન્યા ભ્રૂણ હત્યા અને પીસીપીએનડીટી કાયદો",
        "body": "Reproductive health also encompasses social justice:\nBecause of reckless cultural preference for male children, prenatal diagnostic techniques (ultrasound) were historically abused to determine fetal sex and illegally abort female fetuses (female foeticide).\nTo protect girls and restore a healthy child sex ratio, the Government of India enacted the Pre-Conception and Pre-Natal Diagnostic Techniques (PCPNDT) Act, strictly banning prenatal sex determination under heavy criminal penalties.",
        "body_hi": "प्रजनन स्वास्थ्य में सामाजिक न्याय भी शामिल है:\nबेटे की चाहत में कुछ लोग अल्ट्रासाउंड तकनीक का दुरुपयोग करके गर्भ में पल रहे बच्चे का लिंग पता कर कन्या भ्रूण हत्या करते थे।\nबाल लिंगानुपात को सुधारने और बेटियों की रक्षा के लिए भारत सरकार ने PCPNDT अधिनियम लागू किया है, जिसके तहत प्रसव पूर्व लिंग निर्धारण करना कानूनन गैरकानूनी और दंडनीय अपराध है।",
        "body_gu": "પ્રજનન સ્વાસ્થ્યમાં સામાજિક સંતુલન પણ સંકળાયેલું છે:\nદીકરાની ઘેલછામાં અલ્ટ્રાસાઉન્ડ તકનીકનો દુરુપયોગ કરીને કન્યા ભ્રૂણ હત્યા કરવામાં આવતી હતી, જેનાથી જાતિ પ્રમાણ ખોરવાયું હતું.\nઆ અટકાવવા ભારત સરકારે PCPNDT કાયદો બનાવ્યો છે, જેના હેઠળ ગર્ભનું લિંગ પરીક્ષણ કરાવવું કે કરવું એ કાયદાકીય ગુનો અને સજાપાત્ર છે."
    })

    # 5. Knowledge Check (MCQ)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "Which of the following contraceptive methods provides dual protection by preventing unwanted pregnancy as well as transmission of Sexually Transmitted Diseases (STDs)?",
        "question_hi": "निम्नलिखित में से कौन सी गर्भनिरोधक विधि अवांछित गर्भधारण के साथ-साथ यौन संचारित रोगों (एसटीडी) से भी दोहरा बचाव प्रदान करती है?",
        "question_gu": "નીચેનામાંથી કઈ ગર્ભનિરોધક પદ્ધતિ અનિચ્છનીય ગર્ભાવસ્થા તેમજ જાતીય સંક્રમિત રોગો (STDs) બંને સામે બેવડું રક્ષણ પૂરું પાડે છે?",
        "options": [
            "Condom (Mechanical barrier)",
            "Oral contraceptive hormonal pills",
            "Copper-T (Intrauterine device)",
            "Tubectomy (Surgical sterilization)"
        ],
        "options_hi": [
            "कंडोम (यांत्रिक अवरोधक)",
            "मौखिक गर्भनिरोधक गोलियां",
            "कॉपर-टी (आईयूसीडी)",
            "महिला नसबंदी (ट्यूબેક્ટોમી)"
        ],
        "options_gu": [
            "કૉન્ડોમ (યાંત્રિક અંતરાય)",
            "મૌખિક ગર્ભનિરોધક ગોળીઓ",
            "કૉપર-ટી (IUCD)",
            "ટ્યુબેક્ટોમી (સ્ત્રી નસબંધી)"
        ],
        "correct_index": 0,
        "explanation": "Only condoms prevent direct contact between mucous membranes and body fluids, providing dual protection against both fertilization and sexually transmitted pathogens like HIV and syphilis.",
        "explanation_hi": "केवल कंडोम ही जननांगों और तरल पदार्थों के सीधे संपर्क को रोकता है, जिससे अनचाहे गर्भ और एचआईवी जैसे रोगों दोनों से सुरक्षा मिलती है।",
        "explanation_gu": "માત્ર કૉન્ડોમ જ શારીરિક પ્રવાહીના સીધા સંપર્કને અટકાવે છે, જેથી ગર્ભધારણ અને HIV જેવા રોગો બંને સામે સુરક્ષા મળે છે."
    })

    # 6. Reflection
    blocks.append({
        "id": next_id(),
        "type": "reflection",
        "title": "Why Healthy Maternal Spacing Benefits Entire Nations",
        "title_hi": "बच्चों के जन्म में अंतर पूरे देश के लिए क्यों वरदान है?",
        "title_gu": "બાળકોના જન્મ વચ્ચે અંતર સમગ્ર દેશ માટે કેમ આશીર્વાદરૂપ છે?",
        "body": "When parents adopt modern family planning methods to space births by 3 to 4 years, maternal mortality drops by over 50%. A mother has time to replenish her iron, calcium, and bone density reserves, breastfeed her toddler, and pursue personal career aspirations. Healthy mothers raise well-nourished, educated children, directly breaking the intergenerational cycle of poverty.",
        "body_hi": "जब माता-पिता दो बच्चों के जन्म के बीच 3 से 4 साल का अंतर रखते हैं, तो मातृ मृत्यु दर में 50% से अधिक की गिरावट आती है। मां के शरीर को फिर से पोषण, हीमोग्लोबिन और कैल्शियम जुटाने का समय मिलता है। स्वस्थ माताएं स्वस्थ बच्चों का पालन-पोषण करती हैं जिससे पूरे परिवार और देश की गरीबी दूर होती है।",
        "body_gu": "જ્યારે માતા-પિતા બે બાળકો વચ્ચે 3 થી 4 વર્ષનું અંતર રાખે છે, ત્યારે માતાનું મૃત્યુદર 50% ઘટી જાય છે. માતાને પોતાના શરીરમાં પોષક તત્ત્વો અને લોહીની પુનઃપૂર્તિ કરવાનો પૂરતો સમય મળે છે. સ્વસ્થ માતાઓ તંદુરસ્ત અને સુશિક્ષિત બાળકોનો ઉછેર કરી શકે છે જે ગરીબી નાબૂદીમાં મદદરૂપ બને છે."
    })

    # 7. Connection
    blocks.append({
        "id": next_id(),
        "type": "connection",
        "title": "Demographic Dividend and Sustainable Global Development",
        "title_hi": "जनसांख्यिकीय लाभांश और सतत विकास लक्ष्य",
        "title_gu": "વસ્તી વિષયક લાભ અને ટકાઉ વિકાસ લક્ષ્યાંકો",
        "body": "The United Nations Sustainable Development Goals (SDG 3: Good Health and Well-Being, SDG 5: Gender Equality) identify universal access to sexual and reproductive healthcare as fundamental human rights. Countries with accessible reproductive healthcare empower women into the formal economic workforce, accelerating GDP growth and eradicating malnutrition.",
        "body_hi": "संयुक्त राष्ट्र के सतत विकास लक्ष्य (SDG 3 और 5) प्रजनन स्वास्थ्य सेवाओं को मौलिक मानवाधिकार मानते हैं। जिन देशों में महिलाओं को परिवार नियोजन और स्वास्थ्य सुविधाएं मिलती हैं, वहां महिलाएं कार्यबल में शामिल होकर देश की अर्थव्यवस्था को नई ऊंचाइयों पर ले जाती हैं।",
        "body_gu": "સંયુક્ત રાષ્ટ્રના ટકાઉ વિકાસ લક્ષ્યાંકો (SDG 3 અને 5) પ્રજનન સ્વાસ્થ્ય સેવાઓને મૂળભૂત માનવ અધિકાર ગણે છે. જે દેશોમાં મહિલાઓને કુટુંબ નિયોજન અને આરોગ્ય સુવિધાઓ મળે છે, ત્યાં મહિલાઓ આર્થિક રીતે સક્ષમ બની દેશના વિકાસમાં મોટું યોગદાન આપે છે."
    })

    # 8. Mastery Challenge (MCQ)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "What is the primary surgical step performed during a male vasectomy?",
        "question_hi": "पुरुष नसबंदी (Vasectomy) के दौरान मुख्य शल्य क्रिया क्या की जाती है?",
        "question_gu": "પુરુષ નસબંધી (વાસેક્ટોમી) દરમિયાન મુખ્ય કઈ શસ્ત્રક્રિયા કરવામાં આવે છે?",
        "options": [
            "A small section of both Vas Deferens tubes is cut and tied off to prevent sperms from reaching the semen.",
            "The testes are surgically excised from the scrotum.",
            "The prostate gland is removed entirely.",
            "The urethra is blocked permanently."
        ],
        "options_hi": [
            "शुक्रवाहिकाओं (Vas Deferens) के एक छोटे टुकड़े को काटकर बांध दिया जाता है ताकि शुक्राणु वीर्य तक न पहुंच सकें।",
            "वृषण को काटकर शरीर से अलग कर दिया जाता है।",
            "प्रोस्टेट ग्रंथि को पूरी तरह निकाल दिया जाता है।",
            "मूत्रमार्ग को बंद कर दिया जाता है।"
        ],
        "options_gu": [
            "બંને શુક્રવાહિનીઓ (Vas deferens) નો નાનો ભાગ કાપીને બાંધી દેવામાં આવે છે જેથી શુક્રકોષો વીર્યમાં ભળી ન શકે.",
            "શુક્રપિંડને શરીરમાંથી કાઢી નાખવામાં આવે છે.",
            "પ્રોસ્ટેટ ગ્રંથિ કાઢી નાખવામાં આવે છે.",
            "મૂત્રમાર્ગ કાયમ માટે બંધ કરવામાં આવે છે."
        ],
        "correct_index": 0,
        "explanation": "In a vasectomy, the vas deferens tubes that carry sperms from the testes are cut and tied. Testes continue producing testosterone and sperms (which are harmlessly reabsorbed by the body), but sperms cannot enter the ejaculated semen.",
        "explanation_hi": "पुरुष नसबंदी में केवल शुक्रवाहिका को काटा और बांधा जाता है। वृषण सामान्य रूप से हार्मोन और शुक्राणु बनाते रहते हैं, परंतु शुक्राणु बाहर निकलने वाले वीर्य में नहीं पहुंच पाते।",
        "explanation_gu": "પુરુષ નસબંધીમાં માત્ર શુક્રવાહિનીને કાપીને બાંધવામાં આવે છે. શુક્રપિંડ ટેસ્ટોસ્ટેરોન અને શુક્રકોષ બનાવવાનું ચાલુ રાખે છે, પરંતુ શુક્રકોષો સ્ખલન પામતા વીર્ય સુધી પહોંચી શકતા નથી."
    })

    # =========================================================================
    # MODULE 7: COMPLETE NCERT IN-TEXT QUESTIONS (ALL 3 SETS)
    # =========================================================================

    # In-Text Set 1 (Page ~128) - Q1
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT In-Text 7.1 Q1: What is the importance of DNA copying in reproduction?",
        "question_hi": "NCERT पाठ्य-निहित 7.1 Q1: जनन में डीएनए (DNA) प्रतिकृति की क्या भूमिका है?",
        "question_gu": "NCERT પાઠ્ય-નિહિત 7.1 Q1: પ્રજનનમાં ડીએનએ (DNA) પ્રતિકૃતિનું શું મહત્વ છે?",
        "options": [
            "DNA copying transmits genetic information from parents to offspring and introduces subtle variations essential for survival of the species.",
            "DNA copying only increases the physical size of the cell without affecting genetics.",
            "DNA copying prevents the cell from ever dividing.",
            "DNA copying turns animal cells into plant cells."
        ],
        "options_hi": [
            "डीएनए प्रतिकृति माता-पिता से संतति में आनुवंशिक जानकारी पहुंचाती है और सूक्ष्म विभिन्नताएं लाती है जो प्रजाति के अस्तित्व के लिए आवश्यक हैं।",
            "डीएनए प्रतिकृति केवल कोशिका का आकार बढ़ाती है।",
            "डीएनए प्रतिकृति कोशिका को विभाजित होने से रोकती है।",
            "डीएनए प्रतिकृति जंतु कोशिका को पादप कोशिका बना देती है।"
        ],
        "options_gu": [
            "ડીએનએ પ્રતિકૃતિ પિતૃઓમાંથી સંતતિમાં જનીનિક માહિતીનું વહન કરે છે અને સૂક્ષ્મ ભિન્નતાઓ લાવે છે જે જાતિના અસ્તિત્વ માટે અનિવાર્ય છે.",
            "ડીએનએ પ્રતિકૃતિ માત્ર કોષનું કદ વધારે છે.",
            "ડીએનએ પ્રતિકૃતિ કોષવિભાજન અટકાવે છે.",
            "ડીએનએ પ્રતિકૃતિ પ્રાણીકોષને વનસ્પતિકોષમાં ફેરવે છે."
        ],
        "correct_index": 0,
        "explanation": "DNA contains the master instructions for cell structure and function. Copying ensures that daughter cells receive the necessary blueprints, while minor replication errors generate genetic variations needed for adaptation.",
        "explanation_hi": "डीएनए में शारीरिक बनावट और कार्यों की संपूर्ण जानकारी होती है। प्रतिकृति बनने से संतति को समान लक्षण मिलते हैं और साथ ही विकास के लिए उपयोगी विभिन्नताएं भी उत्पन्न होती हैं।",
        "explanation_gu": "ડીએનએ કોષની રચના અને કાર્યોની તમામ માહિતી ધરાવે છે. પ્રતિકૃતિ બનવાથી સંતતિને લક્ષણો વારસામાં મળે છે અને અનુકૂલન માટે જરૂરી ભિન્નતાઓ પેદા થાય છે."
    })

    # In-Text Set 1 (Page ~128) - Q2
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "NCERT In-Text 7.1 Q2: Why Variation is Beneficial to Species but Not for Individual",
        "title_hi": "NCERT पाठ्य-निहित 7.1 Q2: विभिन्नता व्यष्टि के लिए आवश्यक नहीं पर प्रजाति के लिए क्यों लाभकारी है?",
        "title_gu": "NCERT પાઠ્ય-નિહિત 7.1 Q2: ભિન્નતા વ્યક્તિગત સજીવ માટે જરૂરી ન હોવા છતાં જાતિ માટે કેમ લાભદાયી છે?",
        "body": "• Scientific Explanation:\n1. For an Individual: An organism's body design is finely tuned to its specific ecological niche. A sudden drastic variation might disrupt physiological balance or make the individual ill-adapted, potentially causing early death. Hence, it is not essential for the individual's day-to-day survival.\n\n2. For the Species: Niches are not static; global climate, temperatures, water levels, or pathogens can change drastically. If all members of a species are identical clones, an adverse shift could exterminate the entire population overnight! However, if some individuals possess variations (such as heat tolerance in bacteria), those few will survive the catastrophe and propagate, saving the species from total extinction.",
        "body_hi": "• वैज्ञानिक व्याख्या:\n1. व्यष्टि (Individual) के लिए: जीव का शरीर अपने विशिष्ट पर्यावरण (निकेत) के पूर्णतः अनुकूल होता है। अचानक आई कोई विभिन्नता उसके सामान्य कार्यों में बाधा डाल सकती है जिससे उसका जीवन कठिन हो सकता है। अतः व्यक्तिगत जीवन के लिए विभिन्नता जरूरी नहीं है।\n\n2. प्रजाति (Species) के लिए: पर्यावरण कभी भी बदल सकता है (जैसे अचानक तापमान बढ़ना या कोई नई बीमारी फैलना)। यदि प्रजाति के सभी सदस्य एक समान हों, तो पूरी आबादी एक साथ नष्ट हो जाएगी। परंतु यदि कुछ सदस्यों में विभिन्नता हो, तो वे विषम परिस्थितियों में भी जीवित बच जाएंगे और प्रजाति का अस्तित्व बना रहेगा।",
        "body_gu": "• વૈજ્ઞાનિક સમજૂતી:\n1. વ્યક્તિગત સજીવ માટે: સજીવનું શરીર પોતાના વસવાટ સાથે સુમેળ સાધીને જીવવા ટેવાયેલું હોય છે. અચાનક આવેલો કોઈ મોટો ફેરફાર તેની જૈવિક ક્રિયાઓ ખોરવી શકે છે. તેથી વ્યક્તિગત અસ્તિત્વ માટે ભિન્નતા જરૂરી નથી.\n\n2. જાતિ માટે: પર્યાવરણ કાયમ માટે સ્થિર રહેતું નથી (દા.ત. અચાનક તાપમાન વધવું કે રોગચાળો ફેલાવો). જો બધા જ સજીવો એકસરખા હોય તો સમગ્ર વસ્તી નાશ પામે. પરંતુ જો કેટલાક સજીવોમાં ભિન્નતા હોય, તો તેઓ વિપરીત સંજોગોમાં પણ બચી જશે અને જાતિનું અસ્તિત્વ લુપ્ત થતું અટકશે."
    })

    # In-Text Set 2 (Page ~133) - Q1
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT In-Text 7.2 Q1: How does binary fission differ from multiple fission?",
        "question_hi": "NCERT पाठ्य-निहित 7.2 Q1: द्विखंडन बहुखंडन से किस प्रकार भिन्न है?",
        "question_gu": "NCERT પાઠ્ય-નિહિત 7.2 Q1: દ્વિભાજન એ બહુભાજનથી કઈ રીતે અલગ પડે છે?",
        "options": [
            "In binary fission, a parent cell divides into two equal daughter cells (e.g. Amoeba); in multiple fission, it divides into many daughter cells simultaneously inside a cyst (e.g. Plasmodium).",
            "Binary fission occurs only in plants, while multiple fission occurs only in mammals.",
            "Binary fission requires two parents, while multiple fission requires one parent.",
            "There is no difference; both produce exactly three daughter cells."
        ],
        "options_hi": [
            "द्विखंडन में जनक कोशिका दो समान संतति कोशिकाओं में विभाजित होती है (अमीबा); बहुखंडन में वह एक साथ कई संतति कोशिकाओं में विभाजित होती है (प्लाज्मोडियम)।",
            "द्विखंडन केवल पौधों में होता है और बहुखंडन केवल स्तनधारियों में।",
            "द्विखंडन में दो जनक चाहिए और बहुखंडन में एक।",
            "दोनों में कोई अंतर नहीं है।"
        ],
        "options_gu": [
            "દ્વિભાજનમાં પિતૃકોષ બે સમાન બાળકોષોમાં વિભાજિત થાય છે (અમીબા); બહુભાજનમાં તે કોથળીની અંદર એકસાથે અનેક બાળકોષોમાં વિભાજિત થાય છે (પ્લાઝમોડિયમ).",
            "દ્વિભાજન માત્ર વનસ્પતિમાં અને બહુભાજન માત્ર પ્રાણીઓમાં થાય છે.",
            "દ્વિભાજનમાં બે પિતૃ અને બહુભાજનમાં એક પિતૃ જોઈએ.",
            "બંને વચ્ચે કોઈ તફાવત નથી."
        ],
        "correct_index": 0,
        "explanation": "Binary fission divides the mother cell into two daughter cells (Amoeba, Leishmania). Multiple fission divides the nucleus repeatedly within a cyst, releasing dozens of offspring simultaneously (Plasmodium).",
        "explanation_hi": "द्विखंडन में एक कोशिका से दो कोशिकाएं बनती हैं (अमीबा)। बहुखंडन में सुरक्षात्मक आवरण के अंदर एक साथ कई संतति कोशिकाएं बनती हैं (प्लाज्मोडियम)।",
        "explanation_gu": "દ્વિભાજનમાં એક કોષમાંથી બે બાળકોષો બને છે (અમીબા). બહુભાજનમાં રક્ષણાત્મક કોથળીની અંદર એકસાથે અનેક કોષો બને છે (પ્લાઝમોડિયમ)."
    })

    # In-Text Set 2 (Page ~133) - Q2
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT In-Text 7.2 Q2: How will an organism be benefited if it reproduces through spores?",
        "question_hi": "NCERT पाठ्य-निहित 7.2 Q2: बीजाणुओं द्वारा जनन करने से किसी जीव को क्या लाभ होता है?",
        "question_gu": "NCERT પાઠ્ય-નિહિત 7.2 Q2: બીજાણુઓ દ્વારા પ્રજનન કરવાથી સજીવને કયા ફાયદા થાય છે?",
        "options": [
            "Spores have thick, protective walls that withstand adverse conditions (heat, drought) and are light enough to disperse over wide geographical areas via air.",
            "Spores allow organisms to fly like birds.",
            "Spores eliminate the need for food and water forever.",
            "Spores prevent any other competitor species from growing."
        ],
        "options_hi": [
            "बीजाणुओं की बाहरी भित्ति मोटी और सुरक्षात्मक होती है जो प्रतिकूल परिस्थितियों (गर्मी, सूखे) को झेल सकती है और वे हवा द्वारा दूर-दूर तक फैल सकते हैं।",
            "बीजाणु जीवों को पक्षियों की तरह उड़ने की शक्ति देते हैं।",
            "बीजाणुओं से भोजन और पानी की आवश्यकता हमेशा के लिए समाप्त हो जाती है।",
            "बीजाणु अन्य प्रजातियों को उगने से रोकते हैं।"
        ],
        "options_gu": [
            "બીજાણુઓ જાડી રક્ષણાત્મક દીવાલ ધરાવે છે જે પ્રતિકૂળ સંજોગો (ગરમી, દુષ્કાળ) સામે રક્ષણ આપે છે અને હલકા હોવાથી હવામાં દૂર દૂર સુધી ફેલાઈ શકે છે.",
            "બીજાણુઓ સજીવોને પક્ષીઓની જેમ ઊડવાની ક્ષમતા આપે છે.",
            "બીજાણુઓ ખોરાક અને પાણીની જરૂરિયાત કાયમ માટે દૂર કરે છે.",
            "બીજાણુઓ અન્ય સજીવોને ઊગવા દેતા નથી."
        ],
        "correct_index": 0,
        "explanation": "Spores are covered by tough chitinous walls that protect them from desiccation and extreme temperatures. Because millions are produced and carried easily by breezes, fungal species rapidly colonize new food sources.",
        "explanation_hi": "बीजाणुओं पर मोटी सुरक्षात्मक परत होती है जो सूखे और तापमान से रक्षा करती है। हल्के होने के कारण वे हवा से आसानी से दूर-दूर बिखर जाते हैं और नए स्थानों पर अंकुरित होते हैं।",
        "explanation_gu": "બીજાણુઓ પર મજબૂત રક્ષણાત્મક પડ હોવાથી તેઓ પ્રતિકૂળ વાતાવરણ સહન કરી શકે છે અને વજનમાં હલકા હોવાથી પવન દ્વારા સરળતાથી દૂર સુધી ફેલાઈ શકે છે."
    })

    # In-Text Set 2 (Page ~133) - Q3
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "NCERT In-Text 7.2 Q3: Why Complex Organisms Cannot Reproduce Through Regeneration",
        "title_hi": "NCERT पाठ्य-निहित 7.2 Q3: जटिल बहुकोशिकीय जीव पुनरुद्भवन द्वारा नई संतति क्यों नहीं बना सकते?",
        "title_gu": "NCERT પાઠ્ય-નિહિત 7.2 Q3: જટિલ બહુકોષી સજીવો પુનઃસર્જન દ્વારા નવો સજીવ કેમ બનાવી શકતા નથી?",
        "body": "• Scientific Reason:\n1. Simple organisms (like Hydra or Planaria) are composed of relatively unspecialized tissues with abundant stem-like regenerative cells that can divide and differentiate into any missing cell type.\n\n2. Complex organisms (like birds, dogs, or humans) exhibit advanced structural hierarchy: cells form specialized tissues, tissues form intricate organs, and organs are organized into integrated organ systems located at precise anatomical positions.\n\n3. In such complex organisms, highly differentiated tissues (like nervous tissue, heart muscle, or skeletal bone) lose the pluripotency required to rebuild an entire living organism from a severed fragment.",
        "body_hi": "• वैज्ञानिक कारण:\n1. हाइड्रा या प्लेनेरिया जैसे सरल जीवों में कोशिकाएं अत्यधिक विशिष्टीकृत नहीं होती हैं; उनके पास विशेष पुनरुद्भवन कोशिकाएं होती हैं जो तेजी से विभाजित होकर सभी अंगों को बना सकती हैं।\n\n2. जटिल जीवों (जैसे मनुष्य या कुत्ते) में अत्यधिक संगठित अंग प्रणाली होती है: कोशिकाएं ऊतक बनाती हैं, ऊतक अंग बनाते हैं और अंग मिलकर जटिल अंग तंत्र बनाते हैं।\n\n3. जटिल जीवों के विभेदित अंग (जैसे मस्तिष्क, हृदय या हड्डियां) कटे हुए किसी एक टुकड़े से दोबारा नहीं बन सकते। अतः वे पुनरुद्भवन द्वारा नया जीव नहीं बना सकते।",
        "body_gu": "• વૈજ્ઞાનિક કારણ:\n1. હાઇડ્રા કે પ્લેનેરિયા જેવા સાદા સજીવોમાં કોષોનું વધુ પડતું વિભેદન હોતું નથી; તેમની પાસે વિશિષ્ટ પુનઃસર્જન કોષો હોય છે જે કોઈપણ ખૂટતો ભાગ બનાવી શકે છે.\n\n2. જટિલ સજીવો (જેમ કે મનુષ્ય કે પક્ષીઓ) માં ઊંચી કક્ષાનું શારીરિક આયોજન હોય છે: કોષોમાંથી પેશી, પેશીમાંથી અંગો અને અંગોમાંથી જટિલ અંગતંત્રો બનેલા હોય છે.\n\n3. આ જટિલ વિશિષ્ટ અંગો (જેમ કે મગજ, હૃદય કે ફેફસાં) માત્ર કોઈ કપાયેલા ટુકડામાંથી આપમેળે પુનઃ નિર્માણ પામી શકતા નથી. તેથી જટિલ સજીવો પુનઃસર્જન દ્વારા પ્રજનન કરી શકતા નથી."
    })

    # In-Text Set 2 (Page ~133) - Q4
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT In-Text 7.2 Q4: Why is vegetative propagation practiced for growing some types of plants?",
        "question_hi": "NCERT पाठ्य-निहित 7.2 Q4: कुछ पौधों को उगाने के लिए कायिक प्रवर्धन का उपयोग क्यों किया जाता है?",
        "question_gu": "NCERT પાઠ્ય-નિહિત 7.2 Q4: કેટલાક પ્રકારની વનસ્પતિઓને ઉગાડવા માટે વાનસ્પતિક પ્રજનનનો ઉપયોગ શા માટે થાય છે?",
        "options": [
            "It allows propagation of seedless plants (banana, rose, jasmine), bears flowers and fruits faster than seed plants, and preserves exact parental genetic traits.",
            "It makes plants produce toxic chemicals that repel all animals.",
            "It guarantees that plants do not require sunlight for photosynthesis.",
            "It is the only method to grow heavy oak trees."
        ],
        "options_hi": [
            "यह बीजहीन पौधों (केला, गुलाब, चमेली) को उगाने की अनुमति देता है, बीज वाले पौधों की तुलना में तेजी से फल-फूल देता है और जनक के उत्तम गुणों को सुरक्षित रखता है।",
            "यह पौधों को ऐसा जहरीला रसायन बनाने में मदद करता है जिससे जानवर दूर रहें।",
            "इससे पौधों को प्रकाश संश्लेषण के लिए धूप की जरूरत नहीं रहती।",
            "यह भारी बलूत के पेड़ उगाने का एकमात्र तरीका है।"
        ],
        "options_gu": [
            "તે બીજવિહીન વનસ્પતિઓ (કેળાં, ગુલાબ, મોગરો) ઉગાડવાની તક આપે છે, બીજ કરતાં ઝડપથી ફૂલો-ફળો આપે છે અને પિતૃ છોડના ઉત્તમ લક્ષણો જાળવી રાખે છે.",
            "તે વનસ્પતિને ઝેરી રસાયણો બનાવવામાં મદદ કરે છે.",
            "તેનાથી વનસ્પતિને સૂર્યપ્રકાશની જરૂર રહેતી નથી.",
            "તે મોટા ઓક વૃક્ષો ઉગાડવાની એકમાત્ર પદ્ધતિ છે."
        ],
        "correct_index": 0,
        "explanation": "Vegetative propagation is economically essential because: 1) Seedless varieties (banana, orange) can only be propagated this way. 2) Plants mature faster. 3) Genetic uniformity of high-yield crops is maintained.",
        "explanation_hi": "कायिक प्रवर्धन के तीन बड़े लाभ: बीजहीन किस्मों को उगाना, फल-फूल का जल्दी आना और उच्च गुणवत्ता वाले मूल गुणों को शत-प्रतिशत बनाए रखना।",
        "explanation_gu": "વાનસ્પતિક પ્રજનનના મુખ્ય ફાયદા: બીજવિહીન પાક ઉગાડી શકાય છે, ઝડપથી ઉત્પાદન મળે છે અને પિતૃ છોડના તમામ સારા ગુણો જળવાઈ રહે છે."
    })

    # In-Text Set 2 (Page ~133) - Q5
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT In-Text 7.2 Q5: Why is DNA copying an essential part of the process of reproduction?",
        "question_hi": "NCERT पाठ्य-निहित 7.2 Q5: डीएनए प्रतिकृति बनाना जनन की प्रक्रिया का अनिवार्य भाग क्यों है?",
        "question_gu": "NCERT પાઠ્ય-નિહિત 7.2 Q5: ડીએનએ પ્રતિકૃતિ બનાવવી એ પ્રજનન પ્રક્રિયાનો અનિવાર્ય ભાગ કેમ છે?",
        "options": [
            "Because DNA carries the genetic code that determines body design, protein synthesis, and inherited traits from parent to offspring.",
            "Because DNA is required to digest food in newly born babies.",
            "Because without DNA, cells cannot absorb atmospheric nitrogen.",
            "Because DNA creates physical bones in all living organisms."
        ],
        "options_hi": [
            "क्योंकि डीएनए में वह आनुवंशिक कोड होता है जो शारीरिक बनावट, प्रोटीन संश्लेषण और माता-पिता से मिलने वाले लक्षणों को तय करता है।",
            "क्योंकि नवजात शिशुओं में भोजन पचाने के लिए डीएनए चाहिए।",
            "क्योंकि डीएनए के बिना कोशिकाएं नाइट्रोजन नहीं सोख सकतीं।",
            "क्योंकि डीएनए सभी जीवों में हड्डियां बनाता है।"
        ],
        "options_gu": [
            "કારણ કે ડીએનએ એ જનીનિક સંકેતો ધરાવે છે જે શારીરિક બંધારણ, પ્રોટીન સંશ્લેષણ અને વારસાગત લક્ષણોનું નિયમન કરે છે.",
            "કારણ કે નવજાત શિશુમાં ખોરાક પચાવવા ડીએનએ જરૂરી છે.",
            "કારણ કે ડીએનએ વગર કોષો નાઇટ્રોજન શોષી શકતા નથી.",
            "કારણ કે ડીએનએ તમામ સજીવોમાં હાડકાં બનાવે છે."
        ],
        "correct_index": 0,
        "explanation": "DNA contains all the coded hereditary information for building cellular proteins and establishing characteristic species morphology. Copying ensures daughter cells receive this vital genetic manual.",
        "explanation_hi": "डीएनए में जीव की शारीरिक संरचना और प्रोटीन निर्माण की पूरी जानकारी होती है। प्रतिकृति बनने से ही अगली पीढ़ी में जीवन के आवश्यक लक्षण पहुंचते हैं।",
        "explanation_gu": "ડીએનએ માં સજીવની શારીરિક રચના અને પ્રોટીન સંશ્લેષણ માટેના તમામ જનીનિક સંકેતો હોય છે. પ્રતિકૃતિ બનવાથી જ સંતતિમાં લક્ષણોનું સાચું વહન થાય છે."
    })

    # In-Text Set 3 (Page ~140) - Q1
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT In-Text 7.3 Q1: How is the process of pollination different from fertilization?",
        "question_hi": "NCERT पाठ्य-निहित 7.3 Q1: परागण की क्रिया निषेचन से किस प्रकार भिन्न है?",
        "question_gu": "NCERT પાઠ્ય-નિહિત 7.3 Q1: પરાગનયનની ક્રિયા એ ફલનથી કઈ રીતે અલગ છે?",
        "options": [
            "Pollination is the physical transfer of pollen from anther to stigma; Fertilization is the chemical/biological fusion of male and female gametes to form a zygote.",
            "Pollination occurs only in animals, while fertilization occurs only in plants.",
            "Pollination produces fruit directly, while fertilization produces flowers.",
            "There is no difference; pollination and fertilization are synonymous terms."
        ],
        "options_hi": [
            "परागण परागकोश से वर्तिकाग्र तक परागकणों का भौतिक स्थानांतरण है; जबकि निषेचन नर और मादा युग्मकों का संलयन होकर युग्मनज (Zygote) बनने की प्रक्रिया है।",
            "परागण केवल जंतुओं में होता है और निषेचन केवल पौधों में।",
            "परागण से सीधे फल बनता है और निषेचन से फूल।",
            "दोनों में कोई अंतर नहीं है।"
        ],
        "options_gu": [
            "પરાગનયન એ પરાગાશયમાંથી પરાગાસન પર પરાગરજનું ભૌતિક સ્થળાંતર છે; જ્યારે ફલન એ નર અને માદા જન્યુઓ જોડાઈને યુગ્મનજ (Zygote) બનવાની પ્રક્રિયા છે.",
            "પરાગનયન માત્ર પ્રાણીઓમાં અને ફલન માત્ર વનસ્પતિમાં થાય છે.",
            "પરાગનયનથી સીધું ફળ બને છે અને ફલનથી પુષ્પ.",
            "બંને એક જ પ્રક્રિયાના સમાનાર્થી શબ્દો છે."
        ],
        "correct_index": 0,
        "explanation": "Pollination is an external physical process bringing pollen to stigma (by wind/insects). Fertilization is the internal cellular fusion of gamete nuclei inside the ovule to produce a 2n zygote.",
        "explanation_hi": "परागण केवल परागकणों का वर्तिकाग्र तक पहुंचना है (बाह्य प्रक्रिया)। निषेचन बीजांड के अंदर नर और मादा जनन कोशिकाओं का आपस में जुड़ना है (आंतरિક प्रक्रिया)।",
        "explanation_gu": "પરાગનયન એ પરાગરજનું પરાગાસન પર પહોંચવું છે (બાહ્ય પ્રક્રિયા). ફલન એ અંડકની અંદર નર અને માદા જન્યુઓનું એકબીજા સાથે જોડાવું છે (આંતરિક પ્રક્રિયા)."
    })

    # In-Text Set 3 (Page ~140) - Q2
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT In-Text 7.3 Q2: What is the role of the seminal vesicles and the prostate gland?",
        "question_hi": "NCERT पाठ्य-निहित 7.3 Q2: शुक्राशय और प्रोस्टेट ग्रंथि की क्या भूमिका है?",
        "question_gu": "NCERT પાઠ્ય-નિહિત 7.3 Q2: શુક્રાશય અને પ્રોસ્ટેટ ગ્રંથિની શી ભૂમિકા છે?",
        "options": [
            "They secrete alkaline fluid that provides nutrition (fructose) and a liquid transport medium that enhances sperm motility and survival.",
            "They filter metabolic wastes from the blood to produce urine.",
            "They produce and store testosterone hormone.",
            "They pump blood directly to the testes."
        ],
        "options_hi": [
            "वे क्षारीय तरल स्रावित करते हैं जो शुक्राणुओं को पोषण (फ्रुक्टोज) और एक तरल माध्यम प्रदान करता है जिससे उनकी गतिशीलता और जीवन क्षमता बढ़ती है।",
            "वे रक्त से अपशिष्ट छानकर मूत्र बनाते हैं।",
            "वे टेस्टोस्टेरोन हार्मोन का उत्पादन और भंडारण करते हैं।",
            "वे वृषण में सीधे रक्त पंप करते हैं।"
        ],
        "options_gu": [
            "તેઓ આલ્કલાઇન પ્રવાહી મુક્ત કરે છે જે શુક્રકોષોને પોષણ (ફ્રુક્ટોઝ) અને પ્રવાહી માધ્યમ પૂરું પાડે છે જેથી શુક્રકોષો સરળતાથી તરી શકે.",
            "તેઓ રુધિરમાંથી કચરો ગાળીને પેશાબ બનાવે છે.",
            "તેઓ ટેસ્ટોસ્ટેરોન અંતઃસ્ત્રાવ બનાવે છે.",
            "તેઓ શુક્રપિંડમાં લોહી પંપ કરે છે."
        ],
        "correct_index": 0,
        "explanation": "The secretions of the seminal vesicles and prostate gland: 1) Neutralize urethral and vaginal acidity, 2) Provide fructose for sperm ATP production, 3) Form the liquid vehicle (semen) for easy transport.",
        "explanation_hi": "शुक्राशय और प्रोस्टेट ग्रंथि का तरल शुक्राणुओं को पोषण देता है, अम्लीयता को खत्म करता है और उन्हें तैरने के लिए तरल माध्यम प्रदान करता है।",
        "explanation_gu": "શુક્રાશય અને પ્રોસ્ટેટ ગ્રંથિનો સ્ત્રાવ શુક્રકોષોને પોષણ આપે છે, એસિડિટી તટસ્થ કરે છે અને તેમને તરવા માટે પ્રવાહી માધ્યમ આપે છે."
    })

    # In-Text Set 3 (Page ~140) - Q3
    blocks.append({
        "id": next_id(),
        "type": "theory",
        "title": "NCERT In-Text 7.3 Q3: Changes Seen in Girls at the Time of Puberty",
        "title_hi": "NCERT पाठ्य-निहित 7.3 Q3: यौवनारंभ के समय लड़कियों में होने वाले परिवर्तन",
        "title_gu": "NCERT પાઠ્ય-નિહિત 7.3 Q3: યૌવનારંભ સમયે છોકરીઓમાં જોવા મળતા ફેરફારો",
        "body": "• Secondary Sexual Characteristics in Girls during Puberty:\n1. Breast Development: Mammary glands enlarge and nipples darken.\n2. Body Hair: Growth of hair in armpits and the pubic region.\n3. Body Contours: Pelvis and hips broaden; fat deposits accumulate on thighs and buttocks.\n4. Skin Changes: Skin becomes oilier, often leading to acne/pimples.\n5. Onset of Menstruation (Menarche): Ovaries mature and begin releasing one mature ovum every month, initiating the 28-day menstrual cycle.\n6. Deepening of Emotional and Psychological Maturity.",
        "body_hi": "• यौवनारंभ (Puberty) पर लड़कियों में होने वाले शारीरिक परिवर्तन:\n1. स्तनों के आकार में वृद्धि और चूचुक (nipples) की त्वचा का रंग गहरा होना।\n2. कांख (armpits) और जांघों के मध्य जननांग क्षेत्र में बालों का उगना।\n3. कूल्हों (hips) का चौड़ा होना और नितंबों पर वसा का जमाव।\n4. त्वचा का तैलीय होना और चेहरे पर मुंहासे (pimples) निकलना।\n5. मासिक धर्म (ऋतुस्राव / Menstruation) का प्रारंभ होना (रजोदर्शन)।\n6. जनन अंगों की परिपक्वता और हार्मोनल बदलाव।",
        "body_gu": "• યૌવનારંભ (Puberty) સમયે છોકરીઓમાં થતા શારીરિક ફેરફારો:\n1. સ્તન ગ્રંથિઓના કદમાં વધારો થવો.\n2. કાખમાં અને જનનાંગોની આસપાસ વાળ ઊગવા.\n3. નિતંબનો ભાગ પહોળો થવો.\n4. ત્વચા તૈલીય બનવી અને ચહેરા પર ખીલ થવા.\n5. માસિક સ્ત્રાવ (ઋતુસ્ત્રાવ / રજોધર્મ) ની શરૂઆત થવી.\n6. પ્રજનન અંગોનો વિકાસ થવો અને અંતઃસ્ત્રાવોમાં ફેરફાર થવો."
    })

    # In-Text Set 3 (Page ~140) - Q4
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT In-Text 7.3 Q4: How does the embryo get nourishment inside the mother's body?",
        "question_hi": "NCERT पाठ्य-निहित 7.3 Q4: मां के शरीर में गर्भस्थ भ्रूण को पोषण कैसे प्राप्त होता है?",
        "question_gu": "NCERT પાઠ્ય-નિહિત 7.3 Q4: માતાના શરીરમાં ગર્ભસ્થ ભ્રૂણને પોષણ કેવી રીતે પ્રાપ્ત થાય છે?",
        "options": [
            "Through a specialized disc-like tissue called the Placenta, where chorionic villi provide a large surface area for glucose and oxygen to diffuse from mother to embryo.",
            "The embryo drinks amniotic fluid directly through its mouth.",
            "The embryo absorbs nutrition directly from the mother's spinal cord.",
            "Nutrients are transmitted through radio waves inside the uterus."
        ],
        "options_hi": [
            "प्लेसेंटा (अपरा) नामक एक विशेष तश्तरीनुमा ऊतक के माध्यम से, जहां विली मां के रक्त से ग्लूकोज और ऑक्सीजन को भ्रूण में विसरित होने के लिए बड़ी सतह प्रदान करते हैं।",
            "भ्रूण मुंह से सीधे एमनियोटिक द्रव पीता है।",
            "भ्रूण मां की रीढ़ की हड्डी से पोषण लेता है।",
            "गर्भाशय में रेडियो तरंगों द्वारा पोषण पहुंचता है।"
        ],
        "options_gu": [
            "જરાયુ (Placenta) નામની વિશિષ્ટ પેશી દ્વારા, જ્યાં પ્રવર્ધો માતાના લોહીમાંથી ગ્લુકોઝ અને ઓક્સિજન ભ્રૂણમાં પહોંચાડવા વિશાળ સપાટી આપે છે.",
            "ભ્રૂણ મોં વડે સીધું પ્રવાહી પીએ છે.",
            "ભ્રૂણ માતાના કરોડરજ્જુમાંથી પોષણ મેળવે છે.",
            "ગર્ભાશયમાં તરંગો દ્વારા પોષણ પહોંચે છે."
        ],
        "correct_index": 0,
        "explanation": "The placenta contains villi on the fetal side bathed in maternal blood spaces. Glucose, amino acids, and oxygen diffuse across this thin placental membrane from mother to fetus, while fetal wastes diffuse back into maternal blood for excretion.",
        "explanation_hi": "अपरा (Placenta) गर्भाशय की भित्ति से जुड़ा होता है। इसके प्रवर्ध मां के रक्त से ग्लूकोज और ऑक्सीजन सोखकर भ्रूण तक पहुंचाते हैं और अपशिष्ट पदार्थों को बाहर निकालते हैं।",
        "explanation_gu": "જરાયુ (Placenta) ગર્ભાશયની દીવાલ સાથે જોડાયેલું હોય છે. તેના પ્રવર્ધો માતાના રુધિરમાંથી ગ્લુકોઝ અને ઓક્સિજન મેળવી ભ્રૂણને આપે છે અને કચરો બહાર મોકલે છે."
    })

    # In-Text Set 3 (Page ~140) - Q5
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT In-Text 7.3 Q5: If a woman is using a Copper-T, will it help in protecting her from sexually transmitted diseases?",
        "question_hi": "NCERT पाठ्य-निहित 7.3 Q5: यदि कोई महिला कॉपर-टी का उपयोग कर रही है, तो क्या यह उसे यौन संचरित रोगों से बचाने में मदद करेगा?",
        "question_gu": "NCERT પાઠ્ય-નિહિત 7.3 Q5: જો કોઈ મહિલા કૉપર-ટીનો ઉપયોગ કરી રહી હોય, તો શું તે તેને જાતીય સંક્રમિત રોગોથી બચાવવામાં મદદ કરશે?",
        "options": [
            "No, Copper-T only prevents pregnancy by hindering implantation; it does not prevent mucosal contact or transmission of STDs (HIV, syphilis).",
            "Yes, Copper-T kills all bacteria and viruses in the reproductive tract.",
            "Yes, Copper-T creates an airtight shield blocking all fluids.",
            "No, because Copper-T is made of plastic."
        ],
        "options_hi": [
            "नहीं, कॉपर-टी केवल गर्भधारण को रोकती है; यह जननांगों के संपर्क या एसटीडी (एचआईवी, सिफलिस) के संचरण को नहीं रोक सकती।",
            "हाँ, कॉपर-टी सभी बैक्टीरिया और वायरस को मार देती है।",
            "हाँ, कॉपर-टी सभी तरल पदार्थों को रोक देती है।",
            "नहीं, क्योंकि कॉपर-टी प्लास्टिक की होती है।"
        ],
        "options_gu": [
            "ના, કૉપર-ટી માત્ર ગર્ભધારણ અટકાવે છે; તે પ્રવાહીના સંપર્ક કે STDs (HIV, સિફિલિસ) ના ચેપને અટકાવી શકતી નથી.",
            "હા, કૉપર-ટી બધા બેક્ટેરિયા અને વાયરસને મારી નાખે છે.",
            "હા, કૉપર-ટી બધા પ્રવાહીને રોકી દે છે.",
            "ના, કારણ કે કૉપર-ટી પ્લાસ્ટિકની છે."
        ],
        "correct_index": 0,
        "explanation": "Copper-T is an Intrauterine Device placed inside the uterus to prevent implantation. It does not provide any barrier against fluid exchange or mucosal contact. Hence, it offers zero protection against STDs.",
        "explanation_hi": "कॉपर-टी केवल गर्भाशय में भ्रूण का आरोपण रोकती है। यह शारीरिक द्रवों के आदान-प्रदान को नहीं रोकती, इसलिए एसटीडी से कोई सुरक्षा नहीं देती।",
        "explanation_gu": "કૉપર-ટી માત્ર ગર્ભાશયમાં ભ્રૂણ સ્થાપન અટકાવે છે. તે જાતીય પ્રવાહીના વહનને રોકતી નથી, તેથી STDs સામે કોઈ રક્ષણ મળતું નથી."
    })

    # =========================================================================
    # MODULE 8: COMPLETE NCERT TEXTBOOK EXERCISES (QUESTIONS 1 TO 11)
    # Reusing & Enhancing All Existing Blocks from ncert_class10_science_ch7.json
    # =========================================================================

    # NCERT Exercise Q1 (Existing Block 009)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q1: Asexual reproduction takes place through budding in",
        "question_hi": "NCERT अभ्यास Q1: अलैंगिक जनन मुकुलन (Budding) द्वारा किसमें होता है?",
        "question_gu": "NCERT સ્વાધ્યાય Q1: અલિંગી પ્રજનન કલિકાસર્જન (Budding) દ્વારા શેમાં થાય છે?",
        "options": [
            "Amoeba",
            "Yeast",
            "Plasmodium",
            "Leishmania"
        ],
        "options_hi": [
            "अमीबा",
            "यीस्ट (खमीर)",
            "प्लाज्मोडियम",
            "लीशमैनिया"
        ],
        "options_gu": [
            "અમીબા",
            "યીસ્ટ",
            "પ્લાઝમોડિયમ",
            "લેશમાનિયા"
        ],
        "correct_index": 1,
        "explanation": "Amoeba and Leishmania reproduce by binary fission. Plasmodium reproduces by multiple fission. Yeast (and Hydra) reproduces asexually by budding, where a small outgrowth develops into a new individual.",
        "explanation_hi": "अमीबा और लीशमैनिया द्विखंडन द्वारा प्रजनन करते हैं। प्लाज्मोडियम बहुखंडन द्वारा प्रजनन करता है। यीस्ट (और हाइड्रा) मुकुलन द्वारा अलैंगिक रूप से प्रजनन करते हैं, जहां एक छोटा उभार नए जीव में विकसित होता है।",
        "explanation_gu": "અમીબા અને લેશમાનિયા દ્વિભાજન દ્વારા પ્રજનન કરે છે. પ્લાઝમોડિયમ બહુભાજન દ્વારા પ્રજનન કરે છે. યીસ્ટ (અને હાઇડ્રા) કલિકાસર્જન દ્વારા અલિંગી પ્રજનન કરે છે, જ્યાં એક નાનો ઉપસેલો ભાગ નવા સજીવમાં વિકાસ પામે છે."
    })

    # NCERT Exercise Q2 (Existing Block 010)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q2: Which of the following is not a part of the female reproductive system in human beings?",
        "question_hi": "NCERT अभ्यास Q2: निम्न में से कौन मानव में मादा जनन तंत्र का भाग नहीं है?",
        "question_gu": "NCERT સ્વાધ્યાય Q2: નીચેનામાંથી કયો મનુષ્યમાં માદા પ્રજનન તંત્રનો ભાગ નથી?",
        "options": [
            "Ovary",
            "Uterus",
            "Vas deferens",
            "Fallopian tube"
        ],
        "options_hi": [
            "अंडाशय",
            "गर्भाशय",
            "शुक्रवाहिका (Vas deferens)",
            "डिंबवाहिनी (Fallopian tube)"
        ],
        "options_gu": [
            "અંડપિંડ",
            "ગર્ભાશય",
            "શુક્રવાહિની (Vas deferens)",
            "અંડવાહિની (Fallopian tube)"
        ],
        "correct_index": 2,
        "explanation": "Ovary, Uterus, and Fallopian tube are parts of the female reproductive system. Vas deferens is a duct in the MALE reproductive system that carries sperm from the testes.",
        "explanation_hi": "अंडाशय, गर्भाशय और डिंबवाहिनी मादा जनन तंत्र के भाग हैं। शुक्रवाहिका नर जनन तंत्र में एक वाहिनी है जो वृषण से शुक्राणु ले जाती है।",
        "explanation_gu": "અંડપિંડ, ગર્ભાશય અને અંડવાહિની એ માદા પ્રજનન તંત્રના ભાગો છે. શુક્રવાહિની એ નર પ્રજનન તંત્રની નળી છે જે શુક્રપિંડમાંથી શુક્રકોષોનું વહન કરે છે."
    })

    # NCERT Exercise Q3 (Existing Block 011)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q3: The anther contains",
        "question_hi": "NCERT अभ्यास Q3: परागकोश (Anther) में क्या होते हैं?",
        "question_gu": "NCERT સ્વાધ્યાય Q3: પરાગાશય (Anther) માં શું હોય છે?",
        "options": [
            "sepals",
            "ovules",
            "carpel",
            "pollen grains"
        ],
        "options_hi": [
            "बाह्यदल (Sepals)",
            "बीजांड (Ovules)",
            "स्त्रीकेसर (Carpel)",
            "परागकण (Pollen grains)"
        ],
        "options_gu": [
            "વજ્રપત્રો (Sepals)",
            "અંડકો (Ovules)",
            "સ્ત્રીકેસર (Carpel)",
            "પરાગરજ (Pollen grains)"
        ],
        "correct_index": 3,
        "explanation": "The anther is the swollen top part of the stamen (the male reproductive organ of a flower). It produces and contains yellowish powder called pollen grains, which carry the male germ cells.",
        "explanation_hi": "परागकोश पुंकेसर (फूल का नर प्रजनन अंग) का फूला हुआ ऊपरी भाग है। यह परागकण नामक पीला पाउडर पैदा करता है और उसमें रखता है, जो नर जनन कोशिकाओं को ले जाते हैं।",
        "explanation_gu": "પરાગાશય એ પુંકેસર (પુષ્પનું નર પ્રજનન અંગ) નો ફૂલેલો ઉપરનો ભાગ છે. તે પરાગરજ નામનો પીળો પાવડર ઉત્પન્ન કરે છે અને ધરાવે છે, જેમાં નર જન્યુઓ હોય છે."
    })

    # NCERT Exercise Q4 (Existing Block 012)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q4: What are the advantages of sexual reproduction over asexual reproduction?",
        "question_hi": "NCERT अभ्यास Q4: अलैंगिक प्रजनन की तुलना में लैंगिक प्रजनन के क्या लाभ हैं?",
        "question_gu": "NCERT સ્વાધ્યાય Q4: અલિંગી પ્રજનનની સરખામણીમાં લિંગી પ્રજનનના ફાયદાઓ કયા છે?",
        "options": [
            "Sexual reproduction requires less energy and time.",
            "Sexual reproduction allows only one parent to produce exact clones.",
            "Sexual reproduction mixes DNA from two individuals, creating genetic variations that help the species survive changing environments and promotes evolution.",
            "Sexual reproduction guarantees that all offspring will survive forever."
        ],
        "options_hi": [
            "लैंगिक प्रजनन में कम ऊर्जा और समय लगता है।",
            "लैंगिक प्रजनन केवल एक माता-पिता को सटीक क्लोन बनाने की अनुमति देता है।",
            "लैंगिक प्रजनन दो व्यक्तियों के डीएनए को मिलाता है, आनुवंशिक विभिन्नताएं पैदा करता है जो प्रजातियों को बदलते वातावरण में जीवित रहने में मदद करता है और विकास को बढ़ावा देता है।",
            "लैंगिक प्रजनन गारंटी देता है कि सभी संततियां हमेशा के लिए जीवित रहेंगी।"
        ],
        "options_gu": [
            "લિંગી પ્રજનન માટે ઓછી ઊર્જા અને સમયની જરૂર પડે છે.",
            "લિંગી પ્રજનન માત્ર એક જ પિતૃને આબેહૂબ ક્લોન (નકલ) બનાવવાની મંજૂરી આપે છે.",
            "લિંગી પ્રજનન બે સજીવોના ડીએનએ ને મિશ્રિત કરે છે, જે જનીનિક ભિન્નતાઓ પેદા કરે છે જે જાતિને બદલાતા પર્યાવરણમાં ટકી રહેવામાં મદદ કરે છે અને ઉદવિકાસને પ્રોત્સાહન આપે છે.",
            "લિંગી પ્રજનન ખાતરી આપે છે કે તમામ સંતતિ હંમેશા માટે જીવંત રહેશે."
        ],
        "correct_index": 2,
        "explanation": "Asexual reproduction creates nearly exact clones. Sexual reproduction combines DNA from two different parents, introducing large variations in offspring. This diversity gives the species a better chance of surviving environmental changes.",
        "explanation_hi": "अलैंगिक प्रजनन लगभग सटीक क्लोन बनाता है। लैंगिक प्रजनन दो अलग-अलग जनकों से डीएनए को जोड़ता है, जिससे संतानों में बड़े पैमाने पर विभिन्नताएं आती हैं। यह विविधता प्रजातियों को पर्यावरणीय परिवर्तनों से बचने का बेहतर मौका देती है।",
        "explanation_gu": "અલિંગી પ્રજનન લગભગ આબેહૂબ ક્લોન બનાવે છે. લિંગી પ્રજનન બે અલગ અલગ પિતૃઓના ડીએનએ જોડે છે, જેથી સંતતિમાં મોટી ભિન્નતાઓ આવે છે. આ વિવિધતા જાતિને પર્યાવરણીય ફેરફારો સામે ટકી રહેવાની સારી તક આપે છે."
    })

    # NCERT Exercise Q5 (Existing Block 013)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q5: What are the functions performed by the testis in human beings?",
        "question_hi": "NCERT अभ्यास Q5: मानवों में वृषण (Testis) के क्या कार्य हैं?",
        "question_gu": "NCERT સ્વાધ્યાય Q5: મનુષ્યમાં શુક્રપિંડ (Testis) દ્વારા કયા કાર્યો થાય છે?",
        "options": [
            "To produce urine and filter the blood.",
            "To produce the male germ cells (sperms) and secrete the male sex hormone (testosterone).",
            "To store food and produce gastric juices.",
            "To produce eggs and secrete oestrogen."
        ],
        "options_hi": [
            "मूत्र का उत्पादन करना और रक्त को छानना।",
            "नर जनन कोशिकाओं (शुक्राणुओं) का उत्पादन करना और नर सेक्स हार्मोन (टेस्टोस्टेरोन) का स्राव करना।",
            "भोजन का भंडारण करना और गैस्ट्रिक रस का उत्पादन करना।",
            "अंडे का उत्पादन करना और एस्ट्रोजन का स्राव करना।"
        ],
        "options_gu": [
            "મૂત્ર ઉત્પન્ન કરવું અને લોહીનું ગાળણ કરવું.",
            "નર જન્યુઓ (શુક્રકોષો) ઉત્પન્ન કરવા અને નર જાતીય અંતઃસ્ત્રાવ (ટેસ્ટોસ્ટેરોન) મુક્ત કરવો.",
            "ખોરાકનો સંગ્રહ કરવો અને જઠરરસ ઉત્પન્ન કરવો.",
            "અંડકોષો ઉત્પન્ન કરવા અને ઇસ્ટ્રોજન મુક્ત કરવો."
        ],
        "correct_index": 1,
        "explanation": "Testes have a dual role: 1) Spermatogenesis: Producing millions of male gametes called sperms. 2) Endocrine function: Secreting testosterone, which regulates sperm production and brings about puberty changes in boys.",
        "explanation_hi": "वृषण की दोहरी भूमिका होती है: 1) शुक्राणुजनन: शुक्राणु नामक लाखों नर युग्मकों का उत्पादन करना। 2) अंतःस्रावी कार्य: टेस्टोस्टेरोन स्रावित करना, जो शुक्राणु उत्पादन को नियंत्रित करता है और लड़कों में यौवन (puberty) परिवर्तन लाता है।",
        "explanation_gu": "શુક્રપિંડ બેવડી ભૂમિકા ધરાવે છે: 1) શુક્રકોષ જનન: શુક્રકોષો નામના લાખો નર જન્યુઓ ઉત્પન્ન કરવા. 2) અંતઃસ્ત્રાવી કાર્ય: ટેસ્ટોસ્ટેરોન મુક્ત કરવો, જે શુક્રકોષ ઉત્પાદનનું નિયમન કરે છે અને છોકરાઓમાં યૌવનારંભના ફેરફારો લાવે છે."
    })

    # NCERT Exercise Q6 (Existing Block 014)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q6: Why does menstruation occur?",
        "question_hi": "NCERT अभ्यास Q6: ऋतुस्राव (Menstruation) क्यों होता है?",
        "question_gu": "NCERT સ્વાધ્યાય Q6: ઋતુસ્ત્રાવ (Menstruation) શા માટે થાય છે?",
        "options": [
            "Because the ovary completely stops producing eggs.",
            "Because when the egg is NOT fertilized, the thick, spongy lining of the uterus breaks down and comes out as blood and mucus.",
            "Because the fertilized egg needs to be flushed out of the body.",
            "Because it is a way to excrete urine from the uterus."
        ],
        "options_hi": [
            "क्योंकि अंडाशय पूरी तरह से अंडे देना बंद कर देता है।",
            "क्योंकि जब अंडे का निषेचन नहीं होता है, तो गर्भाशय की मोटी, स्पंजी परत टूट जाती है और रक्त तथा श्लेष्म के रूप में बाहर आती है।",
            "क्योंकि निषेचित अंडे को शरीर से बाहर निकालने की आवश्यकता होती है।",
            "क्योंकि यह गर्भाशय से मूत्र उत्सर्जित करने का एक तरीका है।"
        ],
        "options_gu": [
            "કારણ કે અંડપિંડ અંડકોષો ઉત્પન્ન કરવાનું સંપૂર્ણપણે બંધ કરે છે.",
            "કારણ કે જ્યારે અંડકોષનું ફલન થતું નથી, ત્યારે ગર્ભાશયની જાડી, સ્પંજી દીવાલ તૂટી જાય છે અને રુધિર તથા શ્લેષ્મ સ્વરૂપે બહાર આવે છે.",
            "કારણ કે ફલિત અંડકોષને શરીરમાંથી બહાર કાઢવાની જરૂર હોય છે.",
            "કારણ કે તે ગર્ભાશયમાંથી મૂત્ર ઉત્સર્જન કરવાનો એક માર્ગ છે."
        ],
        "correct_index": 1,
        "explanation": "Every month, the uterus prepares a thick blood-rich lining to nourish a potential embryo. If fertilization does not happen, this lining is no longer needed. It sheds and exits the body via the vagina as menstrual blood.",
        "explanation_hi": "हर महीने, गर्भाशय एक संभावित भ्रूण को पोषण देने के लिए रक्त से भरपूर एक मोटी परत तैयार करता है। यदि निषेचन नहीं होता है, तो इस अस्तर की कोई आवश्यकता नहीं होती है। यह झड़ जाती है और मासिक धर्म के रक्त के रूप में योनि के माध्यम से शरीर से बाहर निकल जाती है।",
        "explanation_gu": "દર મહિને, ગર્ભાશય સંભવિત ભ્રૂણને પોષણ આપવા માટે રુધિરથી સભર જાડું સ્તર તૈયાર કરે છે. જો ફલન ન થાય, તો આ સ્તરની હવે જરૂર રહેતી નથી. તે તૂટે છે અને માસિક રુધિર તરીકે યોનિમાર્ગ દ્વારા શરીરમાંથી બહાર આવે છે."
    })

    # NCERT Exercise Q7 (Existing Block 015)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q7: When drawing a labelled diagram of the longitudinal section of a flower, which parts must be labeled to show the male and female reproductive organs?",
        "question_hi": "NCERT अभ्यास Q7: फूल के अनुदैर्ध्य काट (Longitudinal Section) का नामांकित चित्र बनाते समय, नर और मादा प्रजनन अंगों को दर्शाने के लिए किन भागों को लेबल किया जाना चाहिए?",
        "question_gu": "NCERT સ્વાધ્યાય Q7: પુષ્પના આયામ છેદ (Longitudinal section) ની નામનિર્દેશન વાળી આકૃતિ દોરતી વખતે, નર અને માદા પ્રજનન અંગો દર્શાવવા માટે કયા ભાગો દર્શાવવા જોઈએ?",
        "options": [
            "Only sepals and petals.",
            "Male: Stamen (Anther, Filament); Female: Carpel (Stigma, Style, Ovary).",
            "Male: Ovary; Female: Anther.",
            "Only leaves, roots, and stem."
        ],
        "options_hi": [
            "केवल बाह्यदल और पंखुड़ियां।",
            "नर: पुंकेसर (परागकोश, तंतु); मादा: स्त्रीकेसर (वर्तिकाग्र, वर्तिका, अंडाशय)।",
            "नर: अंडाशय; मादा: परागकोश।",
            "केवल पत्तियां, जड़ें और तना।"
        ],
        "options_gu": [
            "માત્ર વજ્રપત્રો અને દલપત્રો.",
            "નર: પુંકેસર (પરાગાશય, તંતુ); માદા: સ્ત્રીકેસર (પરાગાસન, પરાગવાહિની, બીજાશય).",
            "નર: બીજાશય; માદા: પરાગાશય.",
            "માત્ર પર્ણો, મૂળ અને પ્રકાંડ."
        ],
        "correct_index": 1,
        "explanation": "A complete diagram of a flower shows: Sepals (protect bud), Petals (attract insects), Stamen (Male part: Anther and Filament), and Carpel/Pistil (Female part: Stigma, Style, and Ovary at the base).",
        "explanation_hi": "एक फूल का पूरा आरेख (diagram) दिखाता है: बाह्यदल (कली की रक्षा), पंखुड़ियाँ (कीड़ों को आकर्षित करती हैं), पुंकेसर (नर भाग: परागकोश और तंतु), और स्त्रीकेसर (मादा भाग: वर्तिकाग्र, वर्तिका और आधार पर अंडाशय)।",
        "explanation_gu": "પુષ્પની સંપૂર્ણ આકૃતિ આ દર્શાવે છે: વજ્રપત્રો (કળીનું રક્ષણ), દલપત્રો (કીટકોને આકર્ષવા), પુંકેસર (નર ભાગ: પરાગાશય અને તંતુ), અને સ્ત્રીકેસર (માદા ભાગ: પરાગાસન, પરાગવાહિની અને તળિયે બીજાશય)."
    })

    # NCERT Exercise Q8 (Existing Block 016)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q8: What are the different methods of contraception?",
        "question_hi": "NCERT अभ्यास Q8: गर्भनिरोधक की विभिन्न विधियाँ क्या हैं?",
        "question_gu": "NCERT સ્વાધ્યાય Q8: ગર્ભનિરોધની વિવિધ પદ્ધતિઓ કઈ છે?",
        "options": [
            "Mechanical barriers (Condoms), Chemical methods (Oral pills), Intrauterine Devices (Copper-T), and Surgical methods (Vasectomy/Tubectomy).",
            "Eating hot foods, exercising rigorously, and drinking excessive water.",
            "Antibiotics, painkillers, and vitamin supplements.",
            "Breathing techniques and meditation."
        ],
        "options_hi": [
            "यांत्रिक अवरोध (कंडोम), रासायनिक विधियाँ (मौखिक गोलियाँ), अंतर्गर्भाशयी उपकरण (कॉपर-टी), और शल्य चिकित्सा विधियाँ (पुरुष नसबंदी/महिला नसबंदी)।",
            "गर्म खाना खाना, कठोर व्यायाम करना और अत्यधिक पानी पीना।",
            "एंटीबायोटिक्स, दर्द निवारक और विटामिन की खुराक।",
            "श्वास तकनीक और ध्यान।"
        ],
        "options_gu": [
            "યાંત્રિક અંતરાય (કૉન્ડોમ), રાસાયણિક પદ્ધતિઓ (મૌખિક ગોળીઓ), આઇયુસીડી (કૉપર-ટી), અને શસ્ત્રક્રિયા પદ્ધતિઓ (વાસેક્ટોમી/ટ્યુબેક્ટોમી).",
            "ગરમ ખોરાક ખાવો, સખત કસરત કરવી અને વધુ પડતું પાણી પીવું.",
            "એન્ટિબાયોટિક્સ, પેઇનકિલર્સ અને વિટામિન સપ્લીમેન્ટ્સ.",
            "શ્વાસ લેવાની તકનીકો અને ધ્યાન."
        ],
        "correct_index": 0,
        "explanation": "Contraception (preventing pregnancy) is achieved via: Barrier methods (stop sperm meeting egg), Oral pills (stop egg release), IUCDs like Copper-T (prevent implantation), and Surgery (permanent block of ducts).",
        "explanation_hi": "गर्भनिरोधक (गर्भावस्था को रोकना) निम्न द्वारा प्राप्त किया जाता है: अवरोध विधियाँ (शुक्राणु को अंडे से मिलने से रोकना), मौखिक गोलियाँ (अंडा जारी होने से रोकना), कॉपर-टी जैसे IUCD (आरोपण को रोकना), और सर्जरी (नलिकाओं का स्थायी ब्लॉक)।",
        "explanation_gu": "ગર્ભનિરોધ (ગર્ભાવસ્થા અટકાવવી) આના દ્વારા પ્રાપ્ત થાય છે: અંતરાય પદ્ધતિઓ (શુક્રકોષને અંડકોષ સુધી પહોંચતા રોકવા), મૌખિક ગોળીઓ (અંડકોષ મુક્ત થતો રોકવા), Copper-T જેવા IUCD (સ્થાપન અટકાવવા), અને સર્જરી (નળીઓ કાયમ માટે બંધ કરવી)."
    })

    # NCERT Exercise Q9 (Existing Block 017)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q9: How are the modes for reproduction different in unicellular and multicellular organisms?",
        "question_hi": "NCERT अभ्यास Q9: एककोशिकीय एवं बहुकोशिकीय जीवों की जनन पद्धति में क्या अंतर है?",
        "question_gu": "NCERT સ્વાધ્યાય Q9: એકકોષી અને બહુકોષી સજીવોમાં પ્રજનનની પદ્ધતિઓ કેવી રીતે અલગ છે?",
        "options": [
            "Unicellular organisms only reproduce sexually, whereas multicellular organisms reproduce only by cell division.",
            "Unicellular organisms mostly reproduce by asexual methods like simple cell division (fission) or budding. Complex multicellular organisms often use specialized reproductive organs and sexual reproduction.",
            "Both use exactly the same method of simple cell splitting.",
            "Unicellular organisms do not reproduce at all; they just live forever."
        ],
        "options_hi": [
            "एककोशिकीय जीव केवल लैंगिक रूप से प्रजनन करते हैं, जबकि बहुकोशिकीय जीव केवल कोशिका विभाजन द्वारा प्रजनन करते हैं।",
            "एककोशिकीय जीव ज्यादातर सरल कोशिका विभाजन (विखंडन) या मुकुलन जैसे अलैंगिक तरीकों से प्रजनन करते हैं। जटिल बहुकोशिकीय जीव अक्सर विशेष प्रजनन अंगों और लैंगिक प्रजनन का उपयोग करते हैं।",
            "दोनों साधारण सेल स्प्लिटिंग की बिल्कुल उसी विधि का उपयोग करते हैं।",
            "एककोशिकीय जीव बिल्कुल प्रजनन नहीं करते हैं; वे बस हमेशा के लिए जीते हैं।"
        ],
        "options_gu": [
            "એકકોષી સજીવો માત્ર લિંગી પ્રજનન કરે છે, જ્યારે બહુકોષી સજીવો માત્ર કોષવિભાજન દ્વારા પ્રજનન કરે છે.",
            "એકકોષી સજીવો મોટાભાગે સાદા કોષવિભાજન (ભાજન) અથવા કલિકાસર્જન જેવી અલિંગી પદ્ધતિઓ દ્વારા પ્રજનન કરે છે. જટિલ બહુકોષી સજીવો ઘણીવાર વિશિષ્ટ પ્રજનન અંગો અને લિંગી પ્રજનનનો ઉપયોગ કરે છે.",
            "બંને સાદા કોષ વિભાજનની બરાબર સમાન પદ્ધતિનો ઉપયોગ કરે છે.",
            "એકકોષી સજીવો બિલકુલ પ્રજનન કરતા નથી; તેઓ માત્ર કાયમ માટે જીવે છે."
        ],
        "correct_index": 1,
        "explanation": "In unicellular organisms (Amoeba), the entire cell splits to form offspring. In complex multicellular organisms (humans, trees), specific reproductive cells (gametes) and complex reproductive organs are required.",
        "explanation_hi": "एककोशिकीय जीवों (अमीबा) में, संतान पैदा करने के लिए पूरी कोशिका विभाजित हो जाती है। जटिल बहुकोशिकीय जीवों (मनुष्य, पेड़) में, विशिष्ट प्रजनन कोशिकाओं (युग्मकों) और जटिल प्रजनन अंगों की आवश्यकता होती है।",
        "explanation_gu": "એકકોષી સજીવો (અમીબા) માં, સંતતિ બનાવવા માટે આખો કોષ વિભાજિત થાય છે. જટિલ બહુકોષી સજીવો (માણસ, વૃક્ષો) માં, વિશિષ્ટ પ્રજનન કોષો (જન્યુઓ) અને જટિલ પ્રજનન અંગો જરૂરી છે."
    })

    # NCERT Exercise Q10 (Existing Block 018)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q10: How does reproduction help in providing stability to populations of species?",
        "question_hi": "NCERT अभ्यास Q10: प्रजनन किसी प्रजाति की समष्टि (population) को स्थायित्व प्रदान करने में किस प्रकार सहायक है?",
        "question_gu": "NCERT સ્વાધ્યાય Q10: પ્રજનન કોઈપણ જાતિની વસ્તીને સ્થિરતા જાળવી રાખવામાં કેવી રીતે મદદ કરે છે?",
        "options": [
            "By making the individuals live forever so the population never dies.",
            "By producing new individuals to replace those that die due to age or disease, ensuring the species does not go extinct. Also, variations help the species adapt to changes.",
            "By preventing predators from hunting them.",
            "By changing the physical size of the organisms to make them stronger."
        ],
        "options_hi": [
            "व्यक्तियों को हमेशा के लिए जीवित बनाकर ताकि आबादी कभी न मरे।",
            "उम्र या बीमारी के कारण मरने वालों को बदलने के लिए नए व्यक्तियों का उत्पादन करके, यह सुनिश्चित करना कि प्रजाति विलुप्त न हो। इसके अलावा, विभिन्नताएं प्रजातियों को बदलावों के अनुकूल होने में मदद करती हैं।",
            "शिकारियों को उनका शिकार करने से रोककर।",
            "जीवों को मजबूत बनाने के लिए उनके भौतिक आकार को बदलकर।"
        ],
        "options_gu": [
            "વ્યક્તિઓને હંમેશ માટે જીવંત બનાવીને જેથી વસ્તી ક્યારેય નાશ ન પામે.",
            "ઉંમર કે રોગને કારણે મૃત્યુ પામતા સજીવોનું સ્થાન લેવા નવા સજીવો ઉત્પન્ન કરીને, એ સુનિશ્ચિત કરે છે કે જાતિ લુપ્ત ન થાય. ઉપરાંત, ભિન્નતાઓ જાતિને ફેરફારો સામે અનુકૂલન સાધવામાં મદદ કરે છે.",
            "શિકારીઓને તેમનો શિકાર કરતા અટકાવીને.",
            "સજીવોને મજબૂત બનાવવા માટે તેમના શારીરિક કદમાં ફેરફાર કરીને."
        ],
        "correct_index": 1,
        "explanation": "Death is inevitable for every individual. Reproduction continually adds new individuals to the population, maintaining its numbers. Furthermore, DNA variations generated during reproduction allow the population to adapt to slowly changing environmental niches.",
        "explanation_hi": "प्रत्येक व्यक्ति के लिए मृत्यु निश्चित है। प्रजनन लगातार आबादी में नए व्यक्तियों को जोड़ता है, जिससे इसकी संख्या बनी रहती है। इसके अलावा, प्रजनन के दौरान उत्पन्न डीएनए विविधताएं आबादी को बदलते वातावरण के अनुकूल होने में मदद करती हैं।",
        "explanation_gu": "દરેક સજીવ માટે મૃત્યુ નિશ્ચિત છે. પ્રજનન સતત વસ્તીમાં નવા સજીવો ઉમેરે છે, અને તેની સંખ્યા જાળવી રાખે છે. વધુમાં, પ્રજનન દરમિયાન ઉત્પન્ન થતી ડીએનએ ભિન્નતાઓ વસ્તીને બદલાતા પર્યાવરણ સાથે અનુકૂલન સાધવામાં મદદ કરે છે."
    })

    # NCERT Exercise Q11 (Existing Block 019)
    blocks.append({
        "id": next_id(),
        "type": "mcq",
        "question": "NCERT Exercise Q11: What could be the reasons for adopting contraceptive methods?",
        "question_hi": "NCERT अभ्यास Q11: गर्भनिरोधक युक्तियां अपनाने के क्या कारण हो सकते हैं?",
        "question_gu": "NCERT સ્વાધ્યાય Q11: ગર્ભનિરોધક પદ્ધતિઓ અપનાવવાના કારણો કયા હોઈ શકે?",
        "options": [
            "To increase the population of the country rapidly.",
            "To cure a genetic disease.",
            "To prevent unwanted pregnancies, space out children for better health of the mother, and (using condoms) to prevent sexually transmitted diseases (STDs).",
            "To improve digestion and breathing rates."
        ],
        "options_hi": [
            "देश की जनसंख्या में तेजी से वृद्धि करने के लिए।",
            "एक आनुवंशिक बीमारी को ठीक करने के लिए।",
            "अवांछित गर्भधारण को रोकने के लिए, मां के बेहतर स्वास्थ्य के लिए बच्चों के बीच अंतर रखने के लिए, और (कंडोम का उपयोग करके) यौन संचारित रोगों (एसटीडी) को रोकने के लिए।",
            "पाचन और सांस लेने की दर में सुधार करने के लिए।"
        ],
        "options_gu": [
            "દેશની વસ્તી ઝડપથી વધારવા માટે.",
            "જનીનિક રોગનો ઇલાજ કરવા માટે.",
            "અનિચ્છનીય ગર્ભાવસ્થા અટકાવવા, માતાના સારા સ્વાસ્થ્ય માટે બાળકો વચ્ચે અંતર રાખવા અને (કૉન્ડોમનો ઉપયોગ કરીને) જાતીય સંક્રમિત રોગો (STDs) અટકાવવા માટે.",
            "પાચન અને શ્વાસ લેવાના દરમાં સુધારો કરવા માટે."
        ],
        "correct_index": 2,
        "explanation": "Contraceptives are adopted mainly for family planning (preventing unwanted pregnancy), ensuring the physical and mental health of the mother by keeping a gap between children, and preventing deadly STDs like HIV-AIDS.",
        "explanation_hi": "गर्भनिरोधक मुख्य रूप से परिवार नियोजन (अवांछित गर्भावस्था को रोकना), बच्चों के बीच अंतर रखकर मां के शारीरिक और मानसिक स्वास्थ्य को सुनिश्चित करने और एचआईवी-एड्स जैसे घातक एसटीडी को रोकने के लिए अपनाए जाते हैं।",
        "explanation_gu": "ગર્ભનિરોધક મુખ્યત્વે કુટુંબ નિયોજન (અનિચ્છનીય ગર્ભાવસ્થા અટકાવવા), બાળકો વચ્ચે અંતર રાખીને માતાના શારીરિક અને માનસિક સ્વાસ્થ્યની ખાતરી કરવા અને HIV-AIDS જેવા ઘાતક STDs અટકાવવા માટે અપનાવવામાં આવે છે."
    })

    # =========================================================================
    # PAYLOAD COMPOSITION & FILE OUTPUT
    # =========================================================================
    final_payload = {
        "metadata": metadata,
        "blocks": blocks
    }

    output_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch7.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(final_payload, f, ensure_ascii=False, indent=2)

    print(f"✅ Generated {len(blocks)} blocks successfully in {output_path}")

    # Also generate gseb version for syllabus parity
    gseb_output_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_science_ch7.json"
    gseb_payload = dict(final_payload)
    gseb_payload["metadata"] = dict(metadata)
    gseb_payload["metadata"]["id"] = "gseb_class10_science_ch7"
    gseb_payload["metadata"]["board"] = "GSEB"
    with open(gseb_output_path, "w", encoding="utf-8") as f:
        json.dump(gseb_payload, f, ensure_ascii=False, indent=2)
    print(f"✅ Generated GSEB copy in {gseb_output_path}")

if __name__ == "__main__":
    build_ncert_class10_science_ch7()
