import json
import os

def generate_full_english_ch5():
    chapter_id = "ncert_class10_english_ch5"
    title = "Chapter 5: The Hundred Dresses - I (First Flight)"
    
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
        "tags": ["english", "first_flight", "hundred_dresses_1", "full_text", "bilingual"],
        "learning_outcomes": [
            "Read and comprehend the original NCERT text of 'The Hundred Dresses - I'.",
            "Explore themes of discrimination, bullying, peer pressure, and empathy.",
            "Master complex English vocabulary with inline Hindi and Gujarati translations.",
            "Analyze character dynamics (Wanda, Peggy, Maddie) for CBSE and GSEB Board Exams."
        ],
        "ai_context": {
            "learning_goal": "Provide the exact NCERT text broken into passages, with inline translations using backticks for the Smart Translation Filter.",
        }
    }
    
    blocks = [
        {
            "type": "hook",
            "content": "Imagine sitting in the darkest corner of your classroom every single day, wearing the same faded blue dress, while the most popular kids mock you about how many clothes you own. Wanda Petronski always replied calmly: *'A hundred dresses, all lined up in my closet.'*\n\nWas she lying, or did she possess a secret world of unimaginable brilliance? Let's read the *complete original story* by **Eleanor Estes** to discover the poignant truth.",
            "difficulty": "Beginner",
            "bloom": "Understand"
        },
        {
            "type": "diagram",
            "content": "Wanda Petronski sitting quietly in the back corner of Room Thirteen.",
            "image_url": "assets/images/eng_ch5_wanda_corner.jpg",
            "alt_text": "A quiet young girl sitting alone in the last row of a classroom."
        },
        {
            "type": "theory",
            "title": "Passage 1: Wanda in Room Thirteen",
            "content": "Today, Monday, Wanda Petronski was not in her seat. But nobody, not even Peggy and Madeline, the girls who started all the fun, noticed her absence `(अनुपस्थिति / ગેરહાજરી)`.\n\nUsually Wanda sat in the seat next to the last seat in the last row in Room Thirteen. She sat in the corner of the room where the rough boys who did not make good marks sat, the corner of the room where there was most scuffling of feet `(पैरों को घसीटने की आवाज़ / પગ ઘસડવાનો અવાજ)`, most roars of laughter when anything funny was said, and most mud and dirt on the floor.\n\nWanda did not sit there because she was rough `(उद्दंड / તોફાની)` and noisy. On the contrary `(इसके विपरीत / તેનાથી વિપરીત)`, she was very quiet and rarely said anything at all. And nobody had ever heard her laugh out loud. Sometimes she twisted her mouth into a crooked sort of smile `(कुटिल या टेढ़ी मुस्कान / વાંકી મુસ્કાન)`, but that was all.\n\nNobody knew exactly why Wanda sat in that seat, unless it was because she came all the way from Boggins Heights `(बोगिन्स हाइट्स - एक गरीब बस्ती / બોગિન્સ હાઇટ્સ - એક ગરીબ વિસ્તાર)` and her feet were usually caked with dry mud `(सूखी मिट्टी से सने हुए / સૂકા કાદવથી ખરડાયેલા)`. But no one really thought much about Wanda Petronski, once she sat in the corner of the room.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Teacher's Insight:** Notice the subtle social segregation in Room Thirteen. Wanda sits in the corner not because of bad behavior, but because her poverty (evidenced by the caked mud from Boggins Heights) pushes her to the margins of the classroom."
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Where did Wanda Petronski usually sit in Room Thirteen?",
                "options": [
                    "In the first row next to the teacher's desk",
                    "In the seat next to the last seat in the last row",
                    "In the middle row beside Peggy",
                    "Near the front window next to Madeline"
                ],
                "correct_answer": "In the seat next to the last seat in the last row",
                "explanation": "Wanda sat in the corner of Room Thirteen, in the seat next to the last seat in the last row, where rough boys sat and where there was mud and scuffling of feet."
            },
            "difficulty": "Beginner",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 2: Waiting for Wanda and Her Unfamiliar Name",
            "content": "The time they thought about Wanda was outside of school hours — at noon-time when they were coming back to school or in the morning early before school began, when groups of two or three, or even more, would be talking and laughing on their way to the school yard. Then, sometimes, they waited for Wanda — to have fun with her `(उसका मज़ाक उड़ाने के लिए / તેની મજાક ઉડાવવા માટે)`.\n\nThe next day, Tuesday, Wanda was not in school, either. And nobody noticed her absence again.\n\nBut on Wednesday, Peggy and Maddie did think about Wanda. Peggy and Maddie sat down in front with other children who got good marks and who didn’t track in a whole lot of mud. Peggy was the most popular girl in school. She was pretty, she had many pretty clothes and her hair was curly. Maddie was her closest friend.\n\nThe reason Peggy and Maddie noticed Wanda’s absence was that Wanda had made them late for school. They had waited and waited for Wanda, to have some 'fun' with her, and she just hadn’t come. They often waited for Wanda Petronski to have fun with her.\n\nWanda Petronski. Most of the children in Room Thirteen didn’t have names like that. They had names easy to say, like Thomas, Smith or Allen. There was one boy named Bounce, Willie Bounce, and people thought that was funny, but not funny in the same way that Petronski was.\n\nWanda didn’t have any friends. She came to school alone and went home alone. She always wore a faded `(रंग उड़ा हुआ / ઝાંખો પડી ગયેલો)` blue dress that didn’t hang right `(ठीक से फिट नहीं बैठता था / યોગ્ય રીતે બંધબેસતો નહોતો)`. It was clean, but it looked as though it had never been ironed properly `(ठीक से इस्त्री नहीं किया गया / સરખી રીતે ઇસ્ત્રી ન કરેલો)`.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Why did Peggy and Maddie notice Wanda's absence on Wednesday?",
                "options": [
                    "They were worried about her health",
                    "Wanda was supposed to submit her homework to them",
                    "They had waited for her to tease her and ended up being late for school",
                    "Miss Mason asked them to find Wanda"
                ],
                "correct_answer": "They had waited for her to tease her and ended up being late for school",
                "explanation": "Peggy and Maddie noticed Wanda was missing because they had waited on Oliver Street to have 'fun' teasing her, which made them late for school."
            },
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "theory",
            "title": "Passage 3: The Hundred Dresses Game",
            "content": "As soon as Wanda would arrive in the schoolyard, someone would call out to her. Peggy would say in a most courteous `(अत्यंत विनम्र / અત્યંત નમ્ર)` manner, as though she were talking to Miss Mason, \"Wanda,\" she’d say, giving one of her friends a nudge `(कोहनी से हल्का धक्का / કોણીથી હળવો ધક્કો)`, \"tell us. How many dresses did you say you had hanging up in your closet `(अलमारी / કબાટ)`?\"\n\n\"A hundred,\" Wanda would say.\n\n\"A hundred!\" exclaimed all the little girls incredulously `(अविश्वास से / અવિશ્વાસપૂર્વક)`, and the little ones would stop playing hopscotch `(किकिली/टिप्पी का खेल / પગથિયાંની રમત)` and listen.\n\n\"Yeah, a hundred, all lined up `(कतार में लगी हुई / હારબંધ ગોઠવેલી)`,\" said Wanda. Then her thin lips drew together in silence `(होंठ खामोशी में भिंच गए / હોઠ મૌનમાં બીડાઈ ગયા)`.\n\n\"What are they like? All silk, I bet `(शर्त लगाती हूँ / શરત લગાવું છું)`?\" said Peggy.\n\n\"Yeah, all silk, all colours.\"\n\n\"Velvet `(मखमल / મખમલ)`, too?\"\n\n\"Yeah, velvet too. A hundred dresses,\" Wanda would repeat stolidly `(बिना किसी भाव के / ભાવવિહીન થઈને)`, \"all lined up in my closet.\"\n\nThen they’d let her go. And then before she’d gone very far, they couldn’t help bursting into shriek after shriek of laughter `(हंसी के ठहाकों में फूट पड़ना / ખડખડાટ હાસ્યની ચીસો પાડવી)`. A hundred dresses! Obviously, the only dress Wanda had was the blue one she wore every day. So why did she say she had a hundred? What a story!\n\n\"How many pairs of shoes did you say you had?\"\n\n\"Sixty pairs. All lined up in my closet.\"\n\nCries of exaggerated `(अतिशयोक्तिपूर्ण / અતિશયોક્તિપૂર્ણ)` politeness greeted this. \"All alike?\"\n\n\"Oh, no. Every pair is different. All colours. All lined up.\"",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Teacher's Insight on Bullying:** Notice how Peggy couches her mockery in 'exaggerated politeness'. She never shouts or uses abusive words, which makes the psychological cruelty even harder for outside observers to catch."
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "How did Wanda describe her shoes when questioned by Peggy?",
                "options": [
                    "Ten pairs, all black leather",
                    "Sixty pairs, all different, all colours, all lined up",
                    "A single pair covered with mud",
                    "A hundred pairs made of pure velvet"
                ],
                "correct_answer": "Sixty pairs, all different, all colours, all lined up",
                "explanation": "Wanda claimed to have sixty pairs of shoes, all different in colour and design, and all lined up in her closet."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 4: Peggy's Perspective and Maddie's Unease",
            "content": "Peggy was not really cruel. She protected small children from bullies `(धौंस जमाने वाले / ગુંડાગીરી કરનારા)`. And she cried for hours if she saw an animal mistreated `(दुर्व्यवહાર / ગેરવર્તણૂક)`. If anybody had said to her, \"Don’t you think that is a cruel way to treat Wanda?\" she would have been very surprised. Cruel? Why did the girl say she had a hundred dresses? Anybody could tell that that was a lie. Why did she want to lie? And she wasn’t just an ordinary person, else why did she have a name like that? Anyway, they never made her cry.\n\nAs for Maddie, this business of asking Wanda every day how many dresses and how many hats and how many this and that she had was bothering `(परेशान कर रहा था / પરેશાન કરતું હતું)` her. Maddie was poor herself. She usually wore somebody’s hand-me-down `(पुराने उतारे हुए कपड़े / કોઈના જૂના આપેલા કપડાં)` clothes. Thank goodness, she didn’t live up on Boggins Heights or have a funny name.\n\nSometimes, when Peggy was asking Wanda those questions in that mocking polite voice, Maddie embarrassed `(शर्मिंदा / શરમ અનુભવતી)` herself and studied the marbles in the palm of her hand, rolling them around and saying nothing herself. Not that she felt sorry for Wanda, exactly. She would never have paid any attention to Wanda if Peggy hadn’t invented the dresses game. But suppose Peggy and all the others started in on her next `(अगला निशाना बनाना / હવે પછી તેને નિશાન બનાવવું)`? She wasn’t as poor as Wanda, perhaps, but she was poor. Of course she would have more sense than to say she had a hundred dresses. Still she would not like for them to begin on her. She wished Peggy would stop teasing Wanda Petronski.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "🔥 **Board Exam Concept - Character Contrast:**\n- **Peggy:** Popular, wealthy, genuinely believes Wanda is a liar, lacks self-awareness of her own cruelty.\n- **Maddie:** Poor, wears hand-me-downs, empathetic, but paralyzed by fear of social exclusion and losing Peggy's friendship."
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Why did Maddie feel uneasy when Peggy teased Wanda?",
                "options": [
                    "She hated Peggy and wanted to fight her",
                    "She was poor herself and feared becoming the next target of teasing",
                    "She was Wanda's secret cousin",
                    "Miss Mason had strictly warned her"
                ],
                "correct_answer": "She was poor herself and feared becoming the next target of teasing",
                "explanation": "Maddie wore hand-me-down clothes herself and was terrified that if Peggy stopped teasing Wanda, the girls might turn their attention to her."
            },
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "theory",
            "title": "Passage 5: Maddie's Dilemma and The Torn Note",
            "content": "Today, even though they had been late to school, Maddie was glad she had not had to make fun of Wanda. She worked her arithmetic problems absent-mindedly `(अनमने ढंग से / બેધ્યાનપણે)`. \"Eight times eight let’s see...\" She wished she had the nerve `(हिम्मत / હિંમત)` to write Peggy a note, because she knew she never would have the courage to speak right out to Peggy, to say, \"Hey, Peg, let’s stop asking Wanda how many dresses she has.\"\n\nWhen she finished her arithmetic she did start a note to Peggy. She wrote, \"Dear Peg, Let’s stop asking Wanda Petronski how many dresses she has.\"\n\nSuddenly she paused and shuddered `(कांप उठी / ધ્રૂજી ઊઠી)`. She pictured herself in the schoolyard, a new target `(नया निशाना / નવો લક્ષ્ય)` for Peggy and the girls. Peggy might ask her where she got the dress that she had on, and Maddie would have to say it was one of Peggy’s old ones that Maddie’s mother had tried to disguise `(छिपाना / છુપાવવું)` with new trimmings `(सजावट / શણગાર)` so no one in Room Thirteen would recognize it.\n\nIf only Peggy would decide of her own accord `(अपनी मर्ज़ी से / પોતાની મેળે)` to stop having fun with Wanda. Oh, well! Maddie ran her hand through her short blonde hair as though to push the uncomfortable thoughts away. What difference did it make? Slowly Maddie tore into bits `(टुकड़े-टुकड़े कर दिए / ટુકડે-ટુકડા કરી નાખ્યા)` the note she had started. She was Peggy’s best friend, and Peggy was the best-liked girl in the whole room. Peggy could not possibly do anything that was really wrong, she thought.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Deep Literary Analysis:** The tearing of the note represents the tragic triumph of cowardice and peer pressure over moral conscience. Maddie rationalizes Peggy's behavior ('Peggy could not possibly do anything really wrong') to suppress her own guilt."
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Why did Maddie tear up the note she wrote to Peggy?",
                "options": [
                    "Her mother told her not to write notes in class",
                    "She feared Peggy would mock her own altered hand-me-down dresses",
                    "She ran out of ink before completing it",
                    "Wanda walked into the room at that moment"
                ],
                "correct_answer": "She feared Peggy would mock her own altered hand-me-down dresses",
                "explanation": "Maddie tore up the note because she pictured herself as the new target of teasing, fearing Peggy would point out that Maddie was wearing Peggy's old hand-me-down dress."
            },
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "theory",
            "title": "Passage 6: Wanda's Descriptions and The Drawing Contest",
            "content": "As for Wanda, she was just some girl who lived up on Boggins Heights and stood alone in the schoolyard. She scarcely ever said anything to anybody. The only time she talked was in the schoolyard about the hundred dresses. Maddie remembered her telling about one of her dresses, pale blue with cerise `(चमकीला लाल-गुलाबी रंग / તેજસ્વી લાલ-ગુલાબી રંગ)` coloured trimmings. And she remembered another that was brilliant jungle green with a red sash `(कमरबंद / કમરપટ્ટો)`. \"You’d look like a Christmas tree in that,\" the girls had said in pretended admiration `(झूठी प्रशंसा / બનાવટી પ્રશંસા)`.\n\nThinking about Wanda and her hundred dresses all lined up in the closet, Maddie began to wonder who was going to win the drawing and colouring contest `(चित्रकला और रंग प्रतियोगिता / ચિત્રકામ અને રંગ સ્પર્ધા)`.\n\nFor girls, this contest consisted of designing dresses and for boys, of designing motorboats. Probably Peggy would win the girls’ medal. Peggy drew better than anyone else in the room. At least, that’s what everybody thought. She could copy a picture in a magazine or some film star’s head so that you could almost tell who it was. Oh, Maddie was sure Peggy would win. Well, tomorrow the teacher was going to announce the winners. Then they’d know.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "diagram",
            "content": "A beautiful sketch of a brilliant jungle green dress with a red sash.",
            "image_url": "assets/images/eng_ch5_green_dress.jpg",
            "alt_text": "A vibrant green dress design with a bright red sash."
        },
        {
            "type": "theory",
            "title": "Passage 7: The Drizzling Morning and Room Thirteen Exhibition",
            "content": "The next day it was drizzling `(बूंदाबांदी हो रही थी / ઝરમર વરસાદ પડી રહ્યો હતો)`. Maddie and Peggy hurried to school under Peggy’s umbrella. Naturally, on a day like this, they didn’t wait for Wanda Petronski on the corner of Oliver Street, the street that far down, under the railroad tracks and up the hill, led to Boggins Heights. Anyway, they weren’t taking chances on being late today, because today was important.\n\n\"Do you think Miss Mason will announce the winners today?\" asked Peggy.\n\n\"Oh, I hope so, the minute we get in,\" said Maddie. \"Of course, you’ll win, Peg.\"\n\n\"Hope so,\" said Peggy eagerly.\n\nThe minute they entered the classroom, they stopped short and gasped `(हैरानी से सांस थाम लेना / આશ્ચર્યથી દંગ રહી જવું)`. There were drawings all over the room, on every ledge and windowsill, tacking up on the walls, great sheets of wrapping paper, on which were drawn the most lavish `(भव्य / ભવ્ય)` designs, all of dazzling `(आंखें चौंधिया देने वाले / આંખો અંજાઈ જાય તેવા)` colours and brilliant, lavish designs.\n\nThey must have been the drawings for the contest. They were! Everybody stopped and whistled or murmured admiringly `(प्रशंसा से फुसफुसाना / વખાણ કરતાં ગણગણવું)`.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "What spectacle greeted Peggy and Maddie as they stepped inside Room Thirteen?",
                "options": [
                    "A hundred empty desks arranged in a circle",
                    "A lavish exhibition of dazzling, colourful dress designs displayed all over the room",
                    "Miss Mason scolding the boys for making noise",
                    "Wanda Petronski wearing a silk gown"
                ],
                "correct_answer": "A lavish exhibition of dazzling, colourful dress designs displayed all over the room",
                "explanation": "Upon entering, they saw Room Thirteen filled with great sheets of wrapping paper showcasing lavish, dazzling dress designs all over the ledges, windowsills, and walls."
            },
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "theory",
            "title": "Passage 8: The Winner Revealed",
            "content": "As soon as the class had assembled, Miss Mason announced the winners. Jack Beggles had won for the boys, she said, and his design for an outboard motor was on exhibition in Room Twelve, along with the sketches by all the other boys.\n\n\"As for the girls,\" she said, \"although just one or two sketches were submitted by most, one girl — and Room Thirteen should be proud of her — this one girl designed one hundred designs — all different and all beautiful. In the opinion of the judges, any one of the drawings is worthy of winning the prize. I am very happy to say that Wanda Petronski is the winner of the girls’ medal.\"\n\nUnfortunately, Wanda had been absent from school for some days and was not there to receive the applause `(तालियों की गड़गड़ाहट / તાળીઓનો ગડગડાટ)` that was due to her.\n\n\"Let us hope she will be back tomorrow. Now class, you may file around `(पंक्तिबद्ध होकर घूमना / હારબંધ થઈને ફરવું)` the room quietly and look at her exquisite `(अति सुंदर / અત્યંત સુંદર)` drawings.\"\n\nThe children burst into applause, and even the boys were glad to have a chance to stamp on the floor, put their fingers in their mouths and whistle, though they were not interested in dresses.\n\n\"Look, Peg,\" whispered Maddie. \"There’s that blue one she told us about. Isn’t it beautiful?\"\n\n\"Yes,\" said Peggy, \"and here’s that green one. Boy, and I thought I could draw!\"",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "exam_tips",
            "content": "🔥 **BOARD EXAM SPECIAL: High Order Thinking Skills (HOTS) & Key Themes**\n\n### 1. The Climax & Irony\n- **What was Wanda's 'hundred dresses'?** They were not fabric dresses in a wooden wardrobe, but a hundred brilliant artistic masterworks born from her fertile imagination and creative genius.\n- **The Poignant Irony:** While her classmates judged her poverty based on her single faded blue dress, Wanda possessed a wealth of creativity far surpassing everyone else in Room Thirteen.\n\n### 2. Character Analysis\n- **Wanda Petronski:** Quiet, dignified, extremely gifted artist. She never reacted with anger to bullying, maintaining her self-respect.\n- **Peggy:** Popular and artistic, but thoughtless and oblivious to how her teasing hurt others. When she sees Wanda's designs, she genuinely acknowledges Wanda's superior talent (*'Boy, and I thought I could draw!'*).\n- **Maddie:** The moral center torn by fear. She realizes that standing by silently while someone is bullied makes one an accomplice.\n\n### 3. Common 5-Mark Board Questions\n1. *How does the author portray the subtle dynamics of school bullying in 'The Hundred Dresses - I'?*\n2. *Why did Maddie feel guilty even though she never directly teased Wanda? Explain her psychological conflict.*",
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        }
    ]

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ch5.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch5.json"
    final_json["metadata"]["id"] = "gseb_class10_english_ch5"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Full-Text English Chapter 5 Generated Successfully!")

if __name__ == "__main__":
    generate_full_english_ch5()
