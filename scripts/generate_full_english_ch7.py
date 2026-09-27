import json
import os

def generate_full_english_ch7():
    chapter_id = "ncert_class10_english_ch7"
    title = "Chapter 7: Glimpses of India (First Flight)"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "Interactive Full-Text Reading",
        "subject": "English",
        "grade": "10",
        "board": "NCERT/CBSE",
        "curriculum": ["Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 120,
        "version": "4.0.0-FULL-TEXT",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": [
            "english",
            "first_flight",
            "glimpses_of_india",
            "full_text",
            "baker_from_goa",
            "coorg",
            "tea_from_assam"
        ],
        "learning_outcomes": [
            "Read and comprehend the full original NCERT text for all three parts of Glimpses of India.",
            "Understand Goan traditions, the Portuguese baking heritage, and the socio-economic role of the pader.",
            "Explore Coorg's unique geography, martial ancestry (Greek/Arab descent), and bravery traditions.",
            "Examine Assam's world-famous tea gardens, cultivation seasons, and historical legends.",
            "Master complex vocabulary contextually with trilingual (English-Hindi-Gujarati) annotations.",
            "Formulate high-scoring analytical answers for CBSE and State Board Examination questions."
        ],
        "ai_context": {
            "learning_goal": "Provide the exact NCERT text broken into passages, with inline translations using backticks for the Smart Translation Filter."
        }
    }
    
    blocks = [
        {
            "type": "hook",
            "content": "From the fragrant bakeries of **Goa `(गोवा / ગોવા)`** to the misty rainforest hills of **Coorg `(कूर्ग / કુર્ગ)`**, and into the sprawling emerald tea estates of **Assam `(असम / અસમ)`**—India's rich tapestry of cultures, stories, and people comes alive in three distinct glimpses.\n\nHave you ever wondered why traditional bread is irreplaceable in a Goan wedding, why the people of Coorg are the only Indians permitted to carry firearms without a licence, or how an ancient Buddhist monk accidentally discovered tea? Let's read the *complete, original text* line-by-line!",
            "difficulty": "Beginner",
            "bloom": "Understand"
        },
        {
            "type": "diagram",
            "content": "A traditional Goan baker carrying a basket on his head and holding a bamboo staff.",
            "image_url": "assets/images/eng_ch7_goan_baker.jpg",
            "alt_text": "A traditional Goan baker with fresh loaves of bread."
        },
        {
            "type": "theory",
            "title": "Passage 1: Part I – A Baker from Goa: Nostalgia and the Baker's Arrival",
            "content": "Our elders are often heard reminiscing nostalgically `(पुरानी यादों को प्यार से याद करना / ભૂતકાળની મીઠી યાદો તાજી કરવી)` about those good old Portuguese days, the Portuguese and their famous loaves of bread. Those eaters of loaves might have vanished `(गायब हो गए / અદ્રશ્ય થઈ ગયા)`, but the makers are still there. We still have amongst us the mixers, the moulders and those who bake the loaves.\n\nThose age-old, time-tested furnaces `(समय की कसौटी पर खरी उतरीं भट्ठियाँ / સમયની કસોટી પર ખરી ઉતરેલી ભઠ્ઠીઓ)` still exist. The fire in the furnaces has not yet been extinguished `(बुझाई गई / ઓલવાયેલી)`. The thud and jingle `(धम-धम और झंकार की आवाज / ધબકારો અને ઝણકાર)` of the traditional baker's bamboo, heralding `(आगमन की घोषणा करते हुए / આગમનની જાહેરાત કરતો)` his arrival in the morning, can still be heard in some places.\n\nMaybe the father is not alive, but the son still carries on the family profession. These bakers are, even today, known as pader `(गोवा में पारंपरिक बेकर / ગોવામાં પરંપરાગત બેકર)` in Goa.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Teacher's Insight:** Notice the historical link! Goa was under Portuguese rule for over 450 years. Although the Portuguese left, their traditional culture of bread-making remained deeply rooted. Even today, bakers are called by their Portuguese name, **'Pader'**."
        },
        {
            "type": "theory",
            "title": "Passage 2: Part I – A Baker from Goa: Childhood Memories and Bread-Bangles",
            "content": "During our childhood in Goa, the baker used to be our friend, companion and guide `(साथी और मार्गदर्शक / સાથી અને માર્ગદર્શક)`. He used to come at least twice a day. Once, when he set out in the morning on his selling round, and then again, when he returned after emptying his huge basket.\n\nThe jingling thud of his bamboo woke us up from sleep and we ran to meet and greet him. Why was it so? Was it for the love of the loaf? Not at all. The loaves were bought by some Paskine or Bastine, the maid-servant of the house! What we longed for `(तीव्र इच्छा रखते थे / આતુરતાથી ઝંખતા હતા)` were those bread-bangles `(चूड़ी के आकार की मीठी ब्रेड / બંગડી આકારની મીઠી બ્રેડ)` which we chose carefully. Sometimes it was sweet bread of special make.\n\nThe baker made his musical entry on the scene with the 'jhang, jhang' sound of his specially made bamboo staff `(बांस की लाठी / વાંસની લાકડી)`. One hand supported the basket on his head and the other banged the bamboo on the ground. He would greet the lady of the house with \"Good morning\" and then place his basket on the vertical bamboo.\n\nWe kids would be pushed aside with a mild rebuke `(हल्की सी डांट / હળવો ઠપકો)` and the loaves would be delivered to the servant. But we would not give up. We would climb a bench or the parapet `(मुंडेर या रेलिंग / છતની પાળી)` and peep into the basket, somehow. I can still recall the typical fragrance `(विशिष्ट सुगंध / વિશિષ્ટ સુગંધ)` of those loaves. Loaves for the elders and the bangles for the children. Then we did not even care to brush our teeth or wash our mouths properly. And why should we? Who would take the trouble of plucking the mango-leaf for the toothbrush? And why was it necessary at all? The tiger never brushed his teeth. Hot tea could wash and clean up everything so nicely, after all!",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Why did the children in Goa rush to meet the baker every morning?",
                "options": [
                    "To collect the daily newspaper",
                    "For the special bread-bangles they longed for",
                    "To brush their teeth with mango leaves",
                    "To buy loaves for the household servants"
                ],
                "correct_answer": "For the special bread-bangles they longed for",
                "explanation": "The children did not run for the loaves (which were bought by maid-servants like Paskine or Bastine), but specifically for the sweet bread-bangles that they carefully chose."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 3: Part I – A Baker from Goa: Marriage Gifts, Kabai, and Prosperity",
            "content": "Marriage gifts are meaningless without the sweet bread known as the bol `(शादी में दी जाने वाली मीठी ब्रेड / લગ્નમાં અપાતી મીઠી બ્રેડ)`, just as a party or a feast loses its charm `(आकर्षण / આકર્ષણ)` without bread. Not enough can be said to show how important a baker can be for a village. The lady of the house must prepare sandwiches on the occasion of her daughter's engagement. Cakes and bolinhas `(नारियल की स्वादिष्ट कुकीज़ / નાળિયેરની કૂકીઝ કે બિસ્કિટ)` are a must for Christmas as well as other festivals. Thus, the presence of the baker's furnace in the village is absolutely essential `(अति आवश्यक / અત્યંત જરૂરી)`.\n\nThe baker or bread-seller of those days had a peculiar dress known as the kabai `(पारंपरिक लंबा चोगा / પરંપરાગત લાંબો ઝભ્ભો)`. It was a single-piece long frock reaching down to the knees. In our childhood we saw bakers wearing a shirt and trousers which were shorter than full-length ones and longer than half pants. Even today, anyone who wears a half pant which reaches just below the knees invites the comment that he is dressed like a pader!\n\nThe baker usually collected his bills at the end of the month. Monthly accounts used to be recorded on some wall in pencil. Baking was indeed a profitable profession in the old days. The baker and his family never starved `(भूखों मरना / ભૂખે મરવું)`. He, his family and his servants always looked happy and prosperous `(समृद्ध / સમૃદ્ધ)`. Their plump physique `(मोटा-ताजा शरीर / ભરાવદાર શરીર)` was an open testimony `(प्रत्यक्ष प्रमाण / જીવંત પુરાવો)` to this. Even today any person with a jackfruit-like physical appearance `(कटहल जैसा भारी-भरकम शरीर / ફણસ જેવો સ્થૂળ દેખાવ)` is easily compared to a baker.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Exam Fact Alert:** Remember these three traditional bakery items for short-answer questions:\n1. **Bol:** Sweet bread essential for wedding gifts.\n2. **Sandwiches:** Prepared by the lady of the house for her daughter's engagement.\n3. **Bolinhas & Cakes:** Mandatory for Christmas and festive occasions."
        },
        {
            "type": "diagram",
            "content": "Lush coffee plantations and rolling hills of Coorg with colonial bungalows.",
            "image_url": "assets/images/eng_ch7_coorg_hills.jpg",
            "alt_text": "The misty rolling hills and coffee estates of Coorg."
        },
        {
            "type": "theory",
            "title": "Passage 4: Part II – Coorg: The Land of Rainforests, Coffee, and Spices",
            "content": "Coorg, or Kodagu, the smallest district of Karnataka, is home to evergreen rainforests `(सदाबहार वर्षावन / નિત્યલીલા વર્ષાવનો)`, spices and coffee plantations. Evergreen rainforests cover thirty per cent of this district. During the monsoons, it pours enough to keep many visitors away. The season of joy commences `(शुरू होता है / શરૂ થાય છે)` from September and continues till March.\n\nThe weather is perfect, with some showers thrown in for good measure. The air breathes of invigorating coffee `(ऊर्जा और ताजगी देने वाली कॉफी / તાજગી અને સ્ફૂર્તિ આપતી કોફી)`. Coffee estates and colonial bungalows stand tucked under tree canopies `(वृक्षों की छत्रछाया / વૃક્ષોની છત્રછાયા)` in prime corners.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "What percentage of Coorg is covered with evergreen rainforests, and when does the tourist season begin?",
                "options": [
                    "50% rainforests; starts in May",
                    "30% rainforests; starts in September",
                    "20% rainforests; starts in November",
                    "70% rainforests; starts in July"
                ],
                "correct_answer": "30% rainforests; starts in September",
                "explanation": "Evergreen rainforests cover 30 percent of Coorg, and the season of joy commences in September and continues till March."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 5: Part II – Coorg: Descent, Martial Traditions, and Valour",
            "content": "The fiercely independent people of Coorg are possibly of Greek or Arabic descent `(यूनानी या अरबी वंशज / ગ્રીક કે અરબી વંશજ)`. As one story goes, a part of Alexander's army moved south along the coast and settled here when return became impractical. These people married amongst the locals and their culture is apparent in the martial traditions `(युद्ध और वीरता की परंपराएं / યુદ્ધ અને વીરતાની પરંપરાઓ)`, marriage and religious rites, which are distinct from the Hindu mainstream.\n\nThe theory of Arab origin draws support from the long, black coat with an embroidered waist-belt worn by the Kodavus. Known as kuppia `(कोडावू लोगों का लंबा काला कोट / કોડાગુ લોકોનો લાંબો કાળો કોટ)`, it resembles the kuffia `(अरबों और कुर्दों द्वारा पहना जाने वाला पारंपरिक वस्त्र / આરબો અને કુર્દો દ્વારા પહેરાતો પરંપરાગત પોશાક)` worn by the Arabs and the Kurds.\n\nCoorgi homes have a tradition of hospitality `(अतिथि सत्कार / આતિથ્ય સત્કાર)`, and they are more than willing to recount numerous tales of valour `(शौर्य और वीरता की कहानियाँ / શૌર્ય અને બહાદુરીની વાર્તાઓ)` related to their sons and fathers. The Coorg Regiment is one of the most decorated `(सर्वाधिक सैन्य पदकों से सम्मानित / સૌથી વધુ લશ્કરી ચંદ્રકો મેળવનાર)` in the Indian Army, and the first Chief of the Indian Army, General Cariappa, was a Coorgi. Even now, Kodavus are the only people in India permitted to carry firearms `(हथियार या बंदूकें / બંદૂકો કે હથિયારો)` without a licence.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Teacher's Secret:** Compare **Kuppia** and **Kuffia**:\n• **Kuppia:** Long black coat with an embroidered waist-belt worn by Kodavus (Coorgis).\n• **Kuffia:** Traditional coat worn by Arabs and Kurds.\nThis striking similarity supports the theory of Arab origin!"
        },
        {
            "type": "theory",
            "title": "Passage 6: Part II – Coorg: Wildlife, River Kaveri, and Adventure Trails",
            "content": "The river, Kaveri, obtains its water from the hills and forests of Coorg. Mahaseer `(बड़ी ताजे पानी की मछली / મીઠા પાણીની મોટી માછલી)`—a large freshwater fish—abound in these waters. Kingfishers dive for their catch, while squirrels and langurs drop partially eaten fruit for the mischief of enjoying the splash and the ripple effect `(तरंगों का प्रभाव / પાણીના વમળોની અસર)` in the clear water. Elephants enjoy being bathed and scrubbed in the river by their mahouts `(महावत / મહાવત)`.\n\nThe most laidback individuals become converts to the life of high-energy adventure with river rafting, canoeing, rappelling `(रस्सी के सहारे नीचे उतरना / દોરડા વડે ખડક પરથી ઉતરવું)`, rock climbing and mountain biking. Numerous walking trails in this region are a favourite with trekkers.\n\nBirds, bees and butterflies are there to give you company. Macaques, Malabar squirrels, langurs and slender loris keep a watchful eye from the tree canopy. I do, however, prefer to step aside for wild elephants.\n\nThe climb to the Brahmagiri hills brings you into a panoramic view `(विहंगम और विस्तृत दृश्य / વિશાળ અને નયનરમ્ય દ્રશ્ય)` of the entire misty landscape of Coorg. A walk across the rope bridge leads to the sixty-four-acre island of Nisargadhama. Running into Buddhist monks from India's largest Tibetan settlement, at nearby Bylakuppe, is a bonus. The monks, in red, ochre `(गेरुआ / ગેરુઆ/કાષાય)` and yellow robes, are amongst the many surprises that wait to be discovered by visitors searching for the heart and soul of India, right here in Coorg.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Which large freshwater fish abounds in the waters of the river Kaveri in Coorg?",
                "options": [
                    "Salmon",
                    "Mahaseer",
                    "Catfish",
                    "Rohu"
                ],
                "correct_answer": "Mahaseer",
                "explanation": "Mahaseer is the large freshwater fish that abounds in the Kaveri river flowing through the hills and forests of Coorg."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "diagram",
            "content": "Tea gardens of Assam stretching into the horizon with tea-pluckers carrying bamboo baskets.",
            "image_url": "assets/images/eng_ch7_assam_tea.jpg",
            "alt_text": "Tea plantations in Assam with workers plucking young tea shoots."
        },
        {
            "type": "theory",
            "title": "Passage 7: Part III – Tea from Assam: The Train Journey to the Greenery",
            "content": "\"Chai-garam... garam-chai,\" a vendor called out in a high-pitched voice `(तीखी और ऊंची आवाज / તીણો અને ઊંચો અવાજ)`. He came up to their window and asked, \"Chai, sa'ab?\" \"Give us two cups,\" Pranjol said. They sipped the steaming hot liquid `(खौलता हुआ गर्म तरल / વરાળ નીકળતું ગરમ પ્રવાહી)`. Almost everyone in their compartment was drinking tea too.\n\n\"Do you know that over eighty crore `(अस्सी करोड़ / એંસી કરોડ)` cups of tea are drunk every day throughout the world?\" Rajvir said. \"Whew!\" exclaimed Pranjol. \"Tea really is very popular.\"\n\nThe train pulled out of the station. Pranjol buried his nose in his detective book again. Rajvir too was an ardent fan `(कट्टर प्रशंसक / ઉત્સાહી ચાહક)` of detective stories, but at the moment he was keener on looking at the beautiful scenery. It was green, green everywhere. Rajvir had never seen so much greenery before. Then the soft green paddy fields gave way to tea bushes.\n\nIt was a magnificent view. Against the backdrop of densely wooded hills `(घने जंगलों से ढकी पहाड़ियाँ / ગાઢ જંગલોવાળી ટેકરીઓ)` a sea of tea bushes stretched as far as the eye could see. Dwarfing `(छोटा या बौना दिखाना / નાનું કે વામન દર્શાવવું)` the tiny tea plants were tall sturdy shade-trees `(मजबूत छायादार पेड़ / મજબૂત છાંયડો આપતાં વૃક્ષો)` and amidst the orderly rows of bushes busily moved doll-like figures `(गुड़िया जैसी आकृतियाँ / ઢીંગલી જેવી આકૃતિઓ)`. In the distance was an ugly building with smoke billowing out `(धुएं का उमड़ते हुए निकलना / ધુમાડાના ગોટા નીકળવા)` of tall chimneys.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Character Contrast:** Observe the contrast between **Rajvir** and **Pranjol**. Pranjol was born and brought up on a tea estate, so tea bushes were ordinary to him. Rajvir, visiting Assam for the first time, was fascinated by the breathtaking greenery and prepared himself with extensive knowledge about tea history!"
        },
        {
            "type": "theory",
            "title": "Passage 8: Part III – Tea from Assam: Legends of Tea (Chinese Emperor & Bodhidharma)",
            "content": "\"Hey, a tea garden!\" Rajvir cried excitedly. Pranjol, who had been born and brought up on a plantation, didn't share Rajvir's excitement. \"Oh, this is tea country now,\" he said. \"Assam has the largest concentration of plantations in the world. You will see enough gardens to last you a lifetime!\"\n\n\"I have been reading as much as I could about tea,\" Rajvir said. \"No one really knows who discovered tea but there are many legends `(पौराणिक कथाएं / દંતકથાઓ)`.\"\n\n\"What legends?\"\n\n\"Well, there's the one about the Chinese emperor who always boiled water before drinking it. One day a few leaves of the twigs burning under the pot fell into the water giving it a delicious flavour `(स्वादिष्ट स्वाद / સ્વાદિષ્ટ સુગંધ અને સ્વાદ)`. It is said they were tea leaves.\"\n\n\"Tell me another!\" scoffed Pranjol.\n\n\"We have an Indian legend too. Bodhidharma, an ancient Buddhist ascetic `(तपस्वी या संन्यासी / પ્રાચીન બૌદ્ધ તપસ્વી કે સાધુ)`, cut off his eyelids because he felt sleepy during meditations. Ten tea plants grew out of the eyelids. The leaves of these plants when put in hot water and drunk banished sleep `(नींद को भगा दिया / ઊંઘ ભગાડી દીધી)`.\"\n\n\"Tea was first drunk in China,\" Rajvir added, \"as far back as 2700 B.C.! In fact words such as tea, 'chai' and 'chini' are from Chinese. Tea came to Europe only in the sixteenth century and was drunk more as a medicine than as a beverage `(पेय पदार्थ / પીણું)`.\"",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "According to the Indian legend, why did Bodhidharma cut off his eyelids?",
                "options": [
                    "To cure an eye disease",
                    "Because he felt sleepy during meditations",
                    "As a ritual sacrifice for tea plants",
                    "To improve his eyesight"
                ],
                "correct_answer": "Because he felt sleepy during meditations",
                "explanation": "Bodhidharma cut off his eyelids because he felt sleepy during meditations; ten tea plants then grew out of his discarded eyelids."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 9: Part III – Tea from Assam: Dhekiabari Estate and the Second-Flush",
            "content": "The train clattered into Mariani junction. The boys collected their luggage and pushed their way to the crowded platform. Pranjol's parents were waiting for them. Soon they were driving towards Dhekiabari, the tea-garden managed by Pranjol's father.\n\nAn hour later the car veered sharply `(अचानक तेजी से मुड़ी / અચાનક ઝડપથી વળી)` off the main road. They crossed a cattle-guard `(मवेशी-रोधी फाटक / પશુ-અવરોધક જાળી)` and entered Dhekiabari Tea Estate. On both sides of the gravel-road were acre upon acre of tea bushes, all neatly pruned `(समान ऊंचाई पर छांटी गई / સમાન ઊંચાઈએ કાપેલી)` to the same height. Groups of tea-pluckers, with bamboo baskets on their backs, wearing plastic aprons, were plucking the newly sprouted leaves `(नई फूटी हुई पत्तियां / નવી ફૂટેલી કૂંપળો)`.\n\nPranjol's father slowed down to allow a tractor, pulling a trailer-load of tea leaves, to pass.\n\n\"This is the second-flush `(दूसरी बार अंकुरण का समय / ચાની બીજી મોસમ)` or sprouting period, isn't it, Mr. Barua?\" Rajvir asked. \"It lasts from May to July and yields the best tea.\"\n\n\"You seem to have done your homework before coming,\" Pranjol's father said in surprise.\n\n\"Yes, Mr. Barua,\" Rajvir admitted. \"But I hope to learn much more while I'm here.\"",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Board Exam Key Point:** The second-flush or sprouting period lasts from **May to July** and yields the best quality tea. Rajvir's prior research impressed Mr. Barua, demonstrating the value of curiosity and preparation before visiting a new place."
        },
        {
            "type": "exam_tips",
            "content": "🔥 **BOARD EXAM HIGH-YIELD QUESTIONS & ANSWERS**\n\n**Q1: How did the baker make his entry in a Goan village, and what was his significance?**\n**A:** The baker arrived with the musical 'jhang-jhang' sound of his bamboo staff. He was a friend, companion, and guide. Village life revolved around his bakery—marriages required sweet bread (*bol*), engagements demanded sandwiches, and Christmas was incomplete without *bolinhas* and cakes.\n\n**Q2: What is the story regarding the descent of the people of Coorg?**\n**A:** Coorgis are believed to be of Greek or Arabic descent. The Greek theory states that a part of Alexander's army settled in Coorg and married locals. The Arabic theory is supported by their traditional embroidered black coat called *kuppia*, which closely resembles the Arab *kuffia*.\n\n**Q3: Describe the two legends regarding the discovery of tea.**\n**A:**\n1. **Chinese Legend:** A Chinese emperor was boiling water when leaves from burning twigs blew into the pot, giving the water a refreshing flavour.\n2. **Indian Legend:** Buddhist monk Bodhidharma cut off his eyelids to stay awake during meditation; ten tea plants sprouted from them whose leaves banished sleep.",
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        }
    ]

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ch7.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch7.json"
    final_json["metadata"]["id"] = "gseb_class10_english_ch7"
    with open(gseb_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    print("Full-Text English Chapter 7 Generated Successfully!")

if __name__ == "__main__":
    generate_full_english_ch7()
