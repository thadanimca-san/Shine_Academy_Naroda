import json
import os

def generate_supreme_science_ch5():
    blocks = [
        {
            "id": "KOBJ_CLASS10_SCI_CH5_01_HOOK",
            "type": "theory",
            "title": "The Machine That Never Stops",
            "title_hi": "वह मशीन जो कभी नहीं रुकती",
            "body": "• Imagine a factory that works 24/7 without a break.\n• Even when you are sleeping, sitting, or resting, your body is doing intense maintenance work!\n• Your heart is pumping, lungs are breathing, and cells are being repaired.\n• What keeps this biological factory running?",
            "body_hi": "• एक ऐसे कारखाने की कल्पना करें जो बिना रुके 24/7 काम करता है।\n• यहां तक ​​कि जब आप सो रहे होते हैं, बैठे होते हैं, या आराम कर रहे होते हैं, तब भी आपका शरीर रखरखाव का गहन काम कर रहा होता है!\n• आपका हृदय धड़क रहा है, फेफड़े सांस ले रहे हैं, और कोशिकाओं की मरम्मत की जा रही है।\n• इस जैविक कारखाने को क्या चलाता है?"
        },
        {
            "id": "KOBJ_CLASS10_SCI_CH5_02_SOCRATIC",
            "type": "socratic_question",
            "question": "If a dog is asleep, how do we know it is alive?",
            "question_hi": "अगर कोई कुत्ता सो रहा है, तो हमें कैसे पता चलेगा कि वह जीवित है?",
            "options": [
                "Because it barks.",
                "Because it is moving.",
                "Because we can see it breathing.",
                "Because it has a heartbeat."
            ],
            "options_hi": [
                "क्योंकि यह भौंकता है।",
                "क्योंकि यह चल रहा है।",
                "क्योंकि हम उसे सांस लेते हुए देख सकते हैं।",
                "क्योंकि इसमें दिल की धड़कन है।"
            ],
            "correct_index": 2,
            "explanation": "• While a sleeping animal isn't moving or barking, breathing is a visible life process that indicates it is alive.",
            "explanation_hi": "• जबकि सोया हुआ जानवर हिल या भौंक नहीं रहा है, सांस लेना एक दृश्य जीवन प्रक्रिया है जो इंगित करती है कि वह जीवित है।"
        },
        {
            "id": "KOBJ_CLASS10_SCI_CH5_03_REVEAL",
            "type": "definition",
            "title": "Life Processes",
            "title_hi": "जैव प्रक्रम",
            "body": "• The basic functions performed by living organisms to maintain their life on earth are called life processes.\n• The essential life processes are: Nutrition, Respiration, Transportation, and Excretion.\n• Without these, an organism cannot survive.",
            "body_hi": "• जीवित जीवों द्वारा पृथ्वी पर अपना जीवन बनाए रखने के लिए किए जाने वाले बुनियादी कार्यों को जैव प्रक्रम कहा जाता है।\n• आवश्यक जैव प्रक्रम हैं: पोषण, श्वसन, वहन, और उत्सर्जन।\n• इनके बिना कोई भी जीव जीवित नहीं रह सकता।"
        },
        {
            "id": "KOBJ_CLASS10_SCI_CH5_04_NUTRITION_HOOK",
            "type": "theory",
            "title": "The Ultimate Fuel",
            "title_hi": "अंतिम ईंधन",
            "body": "• To do any work, we need energy. \n• Even when we are not doing any apparent activity, energy is needed to maintain a state of order in our body.\n• Where does this energy come from? Food!\n• The process of taking in food and utilizing it is called Nutrition.",
            "body_hi": "• कोई भी काम करने के लिए हमें ऊर्जा की आवश्यकता होती है।\n• यहां तक ​​कि जब हम कोई स्पष्ट गतिविधि नहीं कर रहे होते हैं, तब भी हमारे शरीर में व्यवस्था की स्थिति बनाए रखने के लिए ऊर्जा की आवश्यकता होती है।\n• यह ऊर्जा कहाँ से आती है? भोजन से!\n• भोजन ग्रहण करने और उसका उपयोग करने की प्रक्रिया को पोषण कहा जाता है।"
        },
        {
            "id": "KOBJ_CLASS10_SCI_CH5_05_NUTRITION_DEF",
            "type": "definition",
            "title": "Modes of Nutrition",
            "title_hi": "पोषण के प्रकार",
            "body": "• **Autotrophic Nutrition (स्वपोषी पोषण):** Organisms synthesize their own food using inorganic raw materials (CO2, water) in the presence of sunlight. Examples: Green plants.\n• **Heterotrophic Nutrition (विषमपोषी पोषण):** Organisms cannot prepare their own food and depend directly or indirectly on autotrophs. Examples: Animals, fungi.",
            "body_hi": "• **स्वपोषी पोषण:** जीव सूर्य के प्रकाश की उपस्थिति में अकार्बनिक कच्चे माल (CO2, पानी) का उपयोग करके अपना भोजन स्वयं बनाते हैं। उदाहरण: हरे पौधे।\n• **विषमपोषी पोषण:** जीव अपना भोजन स्वयं नहीं बना सकते हैं और प्रत्यक्ष या अप्रत्यक्ष रूप से स्वपोषियों पर निर्भर होते हैं। उदाहरण: जानवर, कवक।"
        },
        {
            "id": "KOBJ_CLASS10_SCI_CH5_06_TEACHER_TIP",
            "type": "teacher_tip",
            "body": "• Remember: Autotrophs use 'Photosynthesis' to make food.\n• The raw materials for photosynthesis are Carbon dioxide, Water, Sunlight, and Chlorophyll.",
            "body_hi": "• याद रखें: स्वपोषी भोजन बनाने के लिए 'प्रकाश संश्लेषण' का उपयोग करते हैं।\n• प्रकाश संश्लेषण के लिए कच्चे माल हैं कार्बन डाइऑक्साइड, पानी, सूर्य का प्रकाश, और क्लोरोफिल।"
        },
        {
            "id": "KOBJ_CLASS10_SCI_CH5_07_PHOTOSYNTHESIS_EQ",
            "type": "worked_example",
            "title": "The Magic Equation: Photosynthesis",
            "title_hi": "जादुई समीकरण: प्रकाश संश्लेषण",
            "body": "**Equation:**\n6CO₂ + 12H₂O ⟶ C₆H₁₂O₆ + 6O₂ + 6H₂O\n(In presence of sunlight and chlorophyll)\n\n**Steps:**\n1. Absorption of light energy by chlorophyll.\n2. Conversion of light energy to chemical energy & splitting of water molecules into hydrogen and oxygen.\n3. Reduction of carbon dioxide to carbohydrates.",
            "body_hi": "**समीकरण:**\n6CO₂ + 12H₂O ⟶ C₆H₁₂O₆ + 6O₂ + 6H₂O\n(सूर्य के प्रकाश और क्लोरोफिल की उपस्थिति में)\n\n**चरण:**\n1. क्लोरोफिल द्वारा प्रकाश ऊर्जा का अवशोषण।\n2. प्रकाश ऊर्जा का रासायनिक ऊर्जा में रूपांतरण और पानी के अणुओं का हाइड्रोजन और ऑक्सीजन में विभाजन।\n3. कार्बन डाइऑक्साइड का कार्बोहाइड्रेट में अपचयन।"
        },
        {
            "id": "KOBJ_CLASS10_SCI_CH5_08_RESPIRATION",
            "type": "theory",
            "title": "Respiration: Releasing the Energy",
            "title_hi": "श्वसन: ऊर्जा मुक्त करना",
            "body": "• Nutrition gives us glucose (food). But glucose is useless until we break it down!\n• Respiration is the process of breaking down food to release energy in the form of ATP.\n• It can happen with oxygen (Aerobic) or without oxygen (Anaerobic).",
            "body_hi": "• पोषण हमें ग्लूकोज (भोजन) देता है। लेकिन जब तक हम इसे तोड़ नहीं देते, ग्लूकोज बेकार है!\n• श्वसन भोजन को तोड़ने की प्रक्रिया है जिससे ATP के रूप में ऊर्जा मुक्त होती है।\n• यह ऑक्सीजन के साथ (वायवीय) या ऑक्सीजन के बिना (अवायवीय) हो सकता है।"
        }
    ]

    # Add 10 MCQs
    mcqs = [
        {
            "id": f"KOBJ_CLASS10_SCI_CH5_MCQ_{i+1}",
            "type": "mcq",
            "question": q,
            "question_hi": q_hi,
            "options": opt,
            "options_hi": opt_hi,
            "correct_index": ans_idx,
            "explanation": exp,
            "explanation_hi": exp_hi
        }
        for i, (q, q_hi, opt, opt_hi, ans_idx, exp, exp_hi) in enumerate([
            (
                "Which of the following are energy foods?",
                "निम्नलिखित में से कौन ऊर्जा देने वाले भोजन हैं?",
                ["Carbohydrates and fats", "Proteins and mineral salts", "Vitamins and minerals", "Water and roughage"],
                ["कार्बोहाइड्रेट और वसा", "प्रोटीन और खनिज लवण", "विटामिन और खनिज", "पानी और रुक्षांश"],
                0,
                "Carbohydrates and fats provide energy to the body.",
                "कार्बोहाइड्रेट और वसा शरीर को ऊर्जा प्रदान करते हैं।"
            ),
            (
                "In which mode of nutrition does an organism derive its food from the body of another living organism without killing it?",
                "पोषण के किस तरीके में कोई जीव दूसरे जीवित जीव के शरीर से उसे मारे बिना अपना भोजन प्राप्त करता है?",
                ["Saprotropic nutrition", "Parasitic nutrition", "Holozoic nutrition", "Autotrophic nutrition"],
                ["मृतजीवी पोषण", "परजीवी पोषण", "प्राणिसम पोषण", "स्वपोषी पोषण"],
                1,
                "Parasites feed on a host organism without killing it.",
                "परजीवी किसी परपोषी जीव को मारे बिना उस पर भोजन करते हैं।"
            ),
            (
                "The site of photosynthesis in the cells of a leaf is",
                "पत्ती की कोशिकाओं में प्रकाश संश्लेषण का स्थान है",
                ["chloroplast", "mitochondria", "cytoplasm", "protoplasm"],
                ["क्लोरोप्लास्ट", "माइटोकॉन्ड्रिया", "कोशिका द्रव्य", "प्रोटोप्लाज्म"],
                0,
                "Chloroplasts contain chlorophyll where photosynthesis occurs.",
                "क्लोरोप्लास्ट में क्लोरोफिल होता है जहाँ प्रकाश संश्लेषण होता है।"
            ),
            (
                "In amoeba, food is digested in the:",
                "अमीबा में भोजन पचता है:",
                ["food vacuole", "mitochondria", "pseudopodia", "chloroplast"],
                ["खाद्य रिक्तिका", "माइटोकॉन्ड्रिया", "कूटपाद", "क्लोरोप्लास्ट"],
                0,
                "Amoeba digests its food within the food vacuole using digestive enzymes.",
                "अमीबा पाचक एंजाइमों का उपयोग करके खाद्य रिक्तिका के भीतर अपना भोजन पचाता है।"
            ),
            (
                "Which of the following events in the mouth cavity will be affected if salivary amylase is lacking in the saliva?",
                "यदि लार में लार एमाइलेज की कमी है, तो मुंह की गुहा में निम्नलिखित में से कौन सी घटना प्रभावित होगी?",
                ["Proteins breaking down into amino acids", "Starch breaking down into sugars", "Fats breaking down into fatty acids and glycerol", "Absorption of vitamins"],
                ["प्रोटीन का अमीनो एसिड में टूटना", "स्टार्च का शर्करा में टूटना", "वसा का फैटी एसिड और ग्लिसरॉल में टूटना", "विटामिन का अवशोषण"],
                1,
                "Salivary amylase digests starch into complex sugars in the mouth.",
                "लार एमाइलेज मुंह में स्टार्च को जटिल शर्करा में पचाता है।"
            ),
            (
                "Which region of the alimentary canal absorbs the digested food?",
                "आहार नाल का कौन सा भाग पचे हुए भोजन को अवशोषित करता है?",
                ["Stomach", "Small intestine", "Large intestine", "Liver"],
                ["आमाशय", "छोटी आंत", "बड़ी आंत", "यकृत"],
                1,
                "The small intestine has villi which increase the surface area for absorption.",
                "छोटी आंत में विली होते हैं जो अवशोषण के लिए सतह क्षेत्र को बढ़ाते हैं।"
            ),
            (
                "The contraction and expansion movement of the walls of the food pipe is called:",
                "भोजन नली की दीवारों के सिकुड़ने और फैलने की गति को क्या कहा जाता है?",
                ["translocation", "transpiration", "peristaltic movement", "digestion"],
                ["स्थानांतरण", "वाष्पोत्सर्जन", "क्रमाकुंचन गति", "पाचन"],
                2,
                "Peristalsis is the wave-like muscle contraction that moves food down the digestive tract.",
                "पेरिस्टलसिस लहर जैसी मांसपेशियों का संकुचन है जो भोजन को पाचन तंत्र में नीचे ले जाता है।"
            ),
            (
                "When a few drops of iodine solution are added to rice water, the solution turns blue-black in colour. This indicates that rice water contains:",
                "जब चावल के पानी में आयोडीन के घोल की कुछ बूँदें मिलाई जाती हैं, तो घोल का रंग नीला-काला हो जाता है। यह इंगित करता है कि चावल के पानी में शामिल हैं:",
                ["fats", "complex proteins", "starch", "simple proteins"],
                ["वसा", "जटिल प्रोटीन", "स्टार्च", "सरल प्रोटीन"],
                2,
                "Iodine turns blue-black in the presence of starch.",
                "स्टार्च की उपस्थिति में आयोडीन नीला-काला हो जाता है।"
            ),
            (
                "The exit of unabsorbed food material is regulated by",
                "अनअवशोषित खाद्य सामग्री की निकासी किसके द्वारा नियंत्रित होती है",
                ["liver", "anus", "small intestine", "anal sphincter"],
                ["यकृत", "गुदा", "छोटी आंत", "गुदा अवरोधिनी"],
                3,
                "The anal sphincter muscle controls the release of undigested waste.",
                "गुदा अवरोधिनी पेशी अपचे अपशिष्ट की रिहाई को नियंत्रित करती है।"
            ),
            (
                "What are the products obtained by anaerobic respiration in plants?",
                "पौधों में अवायवीय श्वसन से प्राप्त उत्पाद क्या हैं?",
                ["Lactic acid + Energy", "Carbon dioxide + Water + Energy", "Ethanol + Carbon dioxide + Energy", "Pyruvate"],
                ["लैक्टिक अम्ल + ऊर्जा", "कार्बन डाइऑक्साइड + पानी + ऊर्जा", "इथेनॉल + कार्बन डाइऑक्साइड + ऊर्जा", "पाइरूवेट"],
                2,
                "In the absence of oxygen, yeast (a fungus, functionally similar in this aspect to plant anaerobic pathways) converts pyruvate to ethanol, carbon dioxide, and energy.",
                "ऑक्सीजन की अनुपस्थिति में, खमीर पाइरूवेट को इथेनॉल, कार्बन डाइऑक्साइड और ऊर्जा में परिवर्तित करता है।"
            )
        ])
    ]

    blocks.extend(mcqs)

    for prefix in ["cbse", "gseb", "ncert"]:
        chapter_id = f"{prefix}_class10_science_ch5"
        metadata = {
            "id": chapter_id,
            "title": "Chapter 5: Life Processes",
            "subtitle": "The Ultimate Board Exam Mastery Guide",
            "subject": "Science",
            "grade": "10",
            "board": "NCERT/CBSE/GSEB",
            "curriculum": ["Universal"],
            "language": "English/Hindi (Bilingual)",
            "difficulty": "Intermediate",
            "estimated_minutes": 180,
            "version": "4.0.0-SUPREME-SCIENCE",
            "author": "Antigravity Supreme Intelligence",
            "reviewed_by": "Chief Academic Architect",
            "tags": [
                "science",
                "life_processes",
                "nutrition",
                "respiration",
                "board_special",
                "bilingual"
            ],
            "learning_outcomes": [
                "Understand the meaning of life processes.",
                "Differentiate between autotrophic and heterotrophic nutrition.",
                "Explain the process of photosynthesis.",
                "Describe human digestion and respiration."
            ],
            "ai_context": {
                "learning_goal": "Make abstract biological concepts visual. Relate human body processes to everyday machines.",
                "common_misconceptions": [
                    "Students confuse breathing with respiration.",
                    "Students think plants only respire at night."
                ]
            }
        }
        
        # Write to file
        file_path = f"app_core/chapters/{chapter_id}.json"
        
        # Ensure blocks have proper IDs based on current prefix (optional but cleaner)
        clean_blocks = []
        for b in blocks:
            b_copy = b.copy()
            # KOBJ_CLASS10_SCI_CH5_...
            # The ID doesn't strict require prefix, but let's keep it uniform.
            b_copy['id'] = b_copy['id'].replace("KOBJ_CLASS10_SCI_CH5", f"KOBJ_{prefix.upper()}_10_SCI_5")
            clean_blocks.append(b_copy)

        final_json = {
            "metadata": metadata,
            "blocks": clean_blocks
        }
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(final_json, f, indent=2, ensure_ascii=False)
            
        print(f"✅ Generated {file_path}")

if __name__ == '__main__':
    generate_supreme_science_ch5()
