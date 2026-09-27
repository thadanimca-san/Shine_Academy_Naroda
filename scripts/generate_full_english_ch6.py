import json
import os

def generate_full_english_ch6():
    chapter_id = "ncert_class10_english_ch6"
    title = "Chapter 6: The Hundred Dresses - II (First Flight)"
    
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
        "tags": ["english", "first_flight", "hundred_dresses_2", "full_text"],
        "learning_outcomes": [
            "Read and comprehend the original NCERT text line-by-line.",
            "Analyze the themes of bullying, bystander guilt, remorse, and unconditional forgiveness.",
            "Master complex vocabulary contextually using bilingual translations.",
            "Compare and contrast the character growth of Maddie and Peggy for Board Exam HOTS questions."
        ],
        "ai_context": {
            "learning_goal": "Provide the exact NCERT text broken into passages, with inline translations using backticks for the Smart Translation Filter."
        }
    }
    
    blocks = [
        {
            "type": "hook",
            "content": "Have you ever realized your mistake too late, when the person you hurt has already walked away forever? In Part 1, Wanda Petronski was teased by Peggy and Maddie about having 'a hundred dresses'. But now, a sudden, heartbreaking letter from Wanda's father arrives in Room Thirteen.\n\nWill Maddie ever be able to clear her guilty conscience `(अंतरात्मा / અંતરાત્મા)` and make amends `(गलती सुधारना / ભૂલ સુધારવી)`?\n\nLet's read the *original, complete story* line-by-line to experience this touching lesson on empathy, remorse, and forgiveness.",
            "difficulty": "Beginner",
            "bloom": "Understand"
        },
        {
            "type": "diagram",
            "content": "Miss Mason reading Mr. Petronski's letter to the silent and tense classroom.",
            "image_url": "assets/images/eng_ch6_miss_mason_letter.jpg",
            "alt_text": "A teacher reading a letter to silent, attentive students in a classroom."
        },
        {
            "type": "theory",
            "title": "Passage 1: The Letter from Wanda's Father",
            "content": "While the class was circling the room `(कक्षा का चक्कर लगा रही थी / વર્ગખંડમાં ગોળ ફરી રહી હતી)`, admiring the drawings `(चित्रों की प्रशंसा करते हुए / ચિત્રોની પ્રશંસા કરતા)`, the monitor from the principal's office brought Miss Mason a note. Miss Mason read it several times and studied it thoughtfully `(विचारपूर्वक / વિચારપૂર્વક)` for a while. Then she clapped her hands.\n\n\"Attention, class. Everyone back to their seat.\"\n\nWhen the shuffling of feet `(पैरों की घिसटने की आवाज / પગ ઘસડવાનો અવાજ)` had stopped and the room was still and quiet `(शांत और स्थिर / શાંત અને સ્થિર)`, Miss Mason said, \"I have a letter from Wanda's father that I want to read to you.\"\n\nMiss Mason stood there a moment and the silence in the room grew tense and expectant `(तनावपूर्ण और उत्सुक / તણાવપૂર્ણ અને આતુર)`. The teacher adjusted her glasses slowly and deliberately `(जानबूझकर / જાણીજોઈને)`. Her manner indicated that what was coming — this letter from Wanda's father — was a matter of great importance. Everybody listened closely as Miss Mason read the brief note:\n\n*\"Dear teacher: My Wanda will not come to your school any more. Jake also. Now we move away to big city. No more holler 'Pollack' `('पोलाक' कहकर चिल्लाना / 'પોલાક' કહીને બૂમ પાડવી)`. No more ask why funny name. Plenty of funny names in the big city. Yours truly, Jan Petronski.\"*",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Teacher's Insight:** Notice the tone of Jan Petronski's letter. It is ungrammatical yet profoundly painful. It highlights how immigrant children faced prejudice `(पूर्वाग्रह / પૂર્વગ્રહ)` and discrimination simply because of their ethnic background and unfamiliar names."
        },
        {
            "type": "theory",
            "title": "Passage 2: Miss Mason's Reaction and Classroom Silence",
            "content": "A deep silence met the reading of this letter. Miss Mason took off her glasses, blew on them and wiped them on her soft white handkerchief `(रुमाल / રૂમાલ)`. Then she put them on again and looked at the class. When she spoke her voice was very low.\n\n\"I am sure that none of the boys and girls in Room Thirteen would purposely and deliberately `(जानबूझकर / જાણીજોઈને)` hurt anyone’s feelings because his name happened to be a long, unfamiliar one. I prefer to think that what was said was said in thoughtlessness `(लापरवाही / બેદરકારી)`. It is a very unfortunate thing to have happened — unfortunate and sad, both. And I want you all to think about it `(इस पर विचार करें / આ બાબતે વિચારો)`.\"",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Why did Wanda's father decide to move his children to the big city?",
                "options": [
                    "To find a better paying job",
                    "Because in the big city, there were plenty of funny names and no one would mock them as 'Pollack'",
                    "Because Wanda wanted to attend a dedicated art school",
                    "Because the school in town was closing down"
                ],
                "correct_answer": "Because in the big city, there were plenty of funny names and no one would mock them as 'Pollack'",
                "explanation": "Mr. Petronski wrote that in the big city, there are plenty of unfamiliar names, so nobody would mock them or shout discriminatory slurs at them."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 3: Maddie's Sickening Guilt",
            "content": "The first period was a study period. Maddie tried to prepare her lessons, but she could not put her mind on her work. She had a very sick feeling `(बेचैनी और ग्लानि की भावना / અસ્વસ્થતા અને અપરાધભાવ)` in the bottom of her stomach.\n\nTrue, she had not herself said anything to Wanda, but she had stood by silently `(मूक दर्शक बनकर खड़ी रही / ચુપચાપ ઊભી રહી)`, and that was just as bad as what Peggy had done. Worse. She was a coward `(कायर / કાયર)`. At least Peggy hadn't considered they were being mean, but she, Maddie, had thought they were doing wrong. She had known how Wanda felt, and she had put herself in Wanda's shoes `(खुद को वांडा की जगह रखकर देखा / પોતાને વાન્ડાની જગ્યાએ મૂકીને જોયું)`.\n\nGoodness! Wasn't there anything she could do? If only she could tell Wanda she hadn't meant to hurt her feelings. She turned around and stole a glance `(चोरी-छिपे देखा / ચોરીછૂપીથી જોયું)` at Peggy, but Peggy did not look up. She seemed to be studying hard. Well, whether Peggy felt badly or not, she, Maddie, had to do something. She had to find Wanda Petronski. Maybe she had not yet moved away. Maybe Peggy would climb the Heights with her, and they would tell Wanda she had won the contest, that they thought she was smart and the hundred dresses were beautiful.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "🔥 **Board Exam Focus (Theme of Bystander Guilt):** Why did Maddie consider herself a coward and worse than Peggy?\nBecause while Peggy teased Wanda out of ignorance and didn't think she was being cruel, Maddie was conscious that it was wrong yet remained silent out of fear of becoming the next target of ridicule."
        },
        {
            "type": "theory",
            "title": "Passage 4: The Journey to Boggins Heights",
            "content": "When school was dismissed in the afternoon, Peggy said, with pretended casualness `(दिखावटी बेपरवाही / દેખાતી બેપરવાઈ)`, \"Hey, let's go and see if that kid has left town or not.\"\n\nSo Peggy had had the same idea! Maddie glowed `(प्रसन्न हो उठी / ખુશ થઈ ગઈ)`. Peg was really all right.\n\nThe two girls hurried out of the building, up the trenches `(रास्तों की पगडंडियों / રસ્તાની કેડીઓ)` toward Boggins Heights, the part of town that wore such a forbidding air `(डरावना और उदास माहौल / ભયાનક અને ઉદાસ વાતાવરણ)`. It was a cold, drizzly `(बूंदाबांदी वाली / ઝરમર વરસાદવાળી)` afternoon. \n\n\"At least,\" said Peggy gruffly `(रूखे स्वर में / કઠોર અવાજે)`, \"I never did call her a foreigner or make fun of her name. I never thought she had the sense to know we were making fun of her anyway. I thought she was too dumb. And gee, look how she can draw!\"\n\nMaddie could say nothing. All she hoped was that they would find Wanda. She wanted to tell her that they were sorry they had picked on her `(उसे तंग किया था / તેને હેરાન કરી હતી)`, and how wonderful the whole school thought she was, and please not to move away and everybody would be nice. She and Peggy would fight anybody who was not nice.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "What kind of atmosphere did Boggins Heights have on that afternoon?",
                "options": [
                    "Bright and cheerful with blooming flowers",
                    "A forbidding air with cold, drizzly weather",
                    "Noisy and crowded with festival celebrations",
                    "Warm and sunny with dry autumn leaves"
                ],
                "correct_answer": "A forbidding air with cold, drizzly weather",
                "explanation": "NCERT text states: 'the part of town that wore such a forbidding air. It was a cold, drizzly afternoon.'"
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 5: The Empty House and Maddie's Resolution",
            "content": "The two girls hurried on. They hoped to get to the top of the hill before dark.\n\n\"I think that's where the Petronskis live,\" said Maddie, pointing to a little white house. Wisps of old grass stuck up here and there along the pathway like thin kittens `(कमज़ोर बिल्ली के बच्चों की तरह / પાતળા બિલાડીના બચ્ચાં જેવા)`. The house and its sparse little yard looked shabby but clean `(जीर्ण-शीर्ण लेकिन साफ / જૂનું-પુરાણું પણ સ્વચ્છ)`. It reminded Maddie of Wanda's one dress, her faded blue cotton dress, shabby but clean.\n\nThere was not a sign of life about the house. Peggy walked firmly up to the door and knocked, but there was no answer. She and Maddie went around to the backyard and knocked there. Still there was no answer. There was no doubt about it. The Petronskis were gone. How could they ever make amends `(गलती सुधारना / ભૂલ સુધારવી)`?\n\nThey turned and made their way slowly down the hill. \"Well, anyway,\" said Peggy, \"she's gone now, so what can we do? Besides, when I was asking her about all her dresses, she probably was getting good ideas for her drawings. She might not even have won the contest, otherwise.\"\n\nMaddie turned this idea carefully over in her head, for if there were anything in it she would not have to feel so bad. But that night she could not get to sleep. She thought about Wanda and her faded blue dress and the little house she had lived in. And she thought of the glowing picture those hundred dresses made — all lined up in the classroom. \n\nAt last Maddie sat up in bed and pressed her forehead tight in her hands and really thought. This was the hardest thinking she had ever done. After a long, long time, she reached an important conclusion `(महत्वपूर्ण निष्कर्ष / મહત્વપૂર્ણ તારણ)`:\n\nShe was never going to stand by and say nothing again `(वह कभी मूक दर्शक बनकर चुप नहीं रहेगी / તે ક્યારેય ચુપચાપ સહન નહીં કરે)`. If she ever heard anybody picking on someone because they were funny looking or because they had strange names, she'd speak up. Even if it meant losing Peggy's friendship. She had no way of making things right with Wanda, but from now on she would never make anybody else that unhappy again.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Key Character Turning Point:** Maddie makes a firm moral vow: 'She was never going to stand by and say nothing again.' This reflects the growth from passive conformity to active moral courage."
        },
        {
            "type": "theory",
            "title": "Passage 6: Writing the Letter to Wanda",
            "content": "On Saturday Maddie spent the afternoon with Peggy. They were writing a letter to Wanda Petronski.\n\nIt was just a friendly letter `(एक मित्रतापूर्ण पत्र / એક મૈત્રીપૂર્ણ પત્ર)`, the kind they would write to any good friend, telling about the contest and telling Wanda she had won. They told her how pretty her drawings were. And they asked her if she liked where she was living and if she liked her new teacher. They had meant to say they were sorry `(माफी मांगना चाहते थे / માફી માંગવા માંગતા હતા)`, but it ended up with their just writing a friendly letter, the kind they would have written to any good friend, and they signed it with lots of X's for love.\n\nThey mailed the letter to Boggins Heights, writing 'Please Forward' on the envelope.\n\nDays passed and there was no answer, but the letter did not come back, so maybe Wanda had received it. Perhaps she was so hurt and angry she was not going to answer. You could not blame her `(आप उसे दोष नहीं दे सकते / તમે તેનો વાંક ન કાઢી શકો)`.\n\nWeeks went by and still Wanda did not answer. Peggy had begun to forget the whole business, and Maddie put herself to sleep at night making speeches about Wanda, defending her from great crowds of girls who were trying to tease her with, \"How many dresses have you got?\" and before Wanda could press her lips together in a tight line `(होंठ भींचना / હોઠ દબાવવા)` the way she did before answering, Maddie would shout, \"Stop!\" and everybody would feel ashamed the way she used to feel.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "theory",
            "title": "Passage 7: The Christmas Letter from Wanda",
            "content": "Now it was Christmas time and there was snow on the ground. Christmas bells and a little tree decorated the classroom. On the last day of school before the holidays, the teacher showed the class a letter she had received that morning.\n\n\"Class, you remember Wanda Petronski, the gifted little artist `(प्रतिभाशाली छोटी कलाकार / પ્રતિભાશાળી નાની કલાકાર)` who won the drawing contest? Well, she has written me a letter, and I am glad to know where she lives, because now I can send her the medal. I want to read her letter to you.\"\n\nThe class sat up with a sudden interest and listened intently `(ध्यानपूर्वक सुना / ધ્યાનપૂર્વક સાંભળ્યું)`.\n\n*\"Dear Miss Mason: How are you and Room Thirteen? Please tell the girls they can keep those hundred dresses, because in my new house I have a hundred new ones, all lined up in my closet. I’d like that girl Peggy to have the drawing of the green dress with the red trimming `(लाल किनारी वाली हरी पोशाक / લાલ કિનારીવાળો લીલો ડ્રેસ)`, and her friend Maddie to have the blue one. For Christmas, I miss that school and my new teacher does not equalize `(बराबरी नहीं कर सकती / બરાબરી કરી શકતી નથી)` with you. Merry Christmas to you and everybody. Yours truly, Wanda Petronski.\"*",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Which specific drawings did Wanda offer as Christmas gifts to Peggy and Maddie?",
                "options": [
                    "Peggy: the blue dress; Maddie: the green dress with red trimming",
                    "Peggy: the green dress with red trimming; Maddie: the blue dress",
                    "Peggy: the velvet dress; Maddie: the dotted yellow silk dress",
                    "Both girls received identical white dresses"
                ],
                "correct_answer": "Peggy: the green dress with red trimming; Maddie: the blue dress",
                "explanation": "Wanda wrote: 'I'd like that girl Peggy to have the drawing of the green dress with the red trimming, and her friend Maddie to have the blue one.'"
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 8: The Discovery of Wanda's Secret Forgiveness",
            "content": "On the way home from school Maddie and Peggy held their drawings very carefully. All the houses had wreaths `(फूलों के छल्ले / ફૂલોના હાર/ચક્રો)` and holly in the windows. Outside the grocery store, hundreds of Christmas trees were stacked, and in the window, candy peppermint canes `(पुदीने की मीठी छड़ियाँ / ફુદીનાની મીઠી લાકડીઓ)` and cornucopias of shiny transparent paper `(चमकीले सजावटी शंकु / ચમકદાર સુશોભિત શંકુઓ)` were strung. The air smelled like Christmas and light shining everywhere reflected different colors on the snow.\n\n\"The colors are so bright,\" said Peggy. \"This shows she really liked us, and that she got our letter, and that this is her way of saying that everything’s all right. And that’s that.\"\n\n\"I hope so,\" said Maddie sadly. She felt sad because she knew she would never see the little Polish girl again and would never really be able to make things right between them.\n\nShe went home and she pinned her drawing over a torn place `(फटी हुई जगह / ફાટેલી જગ્યા)` in the pink-flowered wallpaper in the bedroom. The shabby room came alive from the brilliancy of the colors `(रंगों की चमक / રંગોની ચમક)`. Maddie sat down on her bed and looked at the drawing. She had stood by and said nothing, but Wanda had been nice to her, anyway.\n\nTears blurred her eyes and she gazed for a long time at the picture. Then hastily she rubbed her eyes and studied it intently `(गहराई से अध्ययन किया / ઊંડાણપૂર્વક જોયું)`. The colors in the dress were so vivid `(सजीव और चटकीले / જીવંત અને આબેહૂબ)` that she had scarcely noticed the face and head of the drawing. But it looked like her, Maddie! It really looked like her own mouth and eyes. Why, it really looked like herself! Wanda had really drawn this for her. Excitedly, she ran over to Peggy's.\n\n\"Peg!\" she said, \"let me see your picture.\"\n\n\"What's the matter?\" asked Peggy, as they clattered up to her room where Wanda's drawing was lying face down on the bed. Maddie carefully lifted it up.\n\n\"Look! She drew you. That's you!\" she exclaimed. And the head and face of this picture really did look like Peggy.\n\n\"What did I say!\" said Peggy. \"She must have really liked us, anyway.\"\n\n\"Yes, she must have,\" agreed Maddie, and she blinked away the tears `(आँसू पोंछ लिए / આંસુ લૂછી નાખ્યા)` that came every time she thought of Wanda standing alone in that sunny spot in the school yard, looking stolidly `(बिना किसी भाव के / ભાવહીન રીતે)` over at the group of laughing girls, after she had walked off, after she had said, \"Sure, a hundred of them, all lined up.\"",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "diagram",
            "content": "Maddie realizing with tears in her eyes that Wanda had drawn Maddie's face inside the blue dress portrait.",
            "image_url": "assets/images/eng_ch6_maddie_drawing.jpg",
            "alt_text": "Maddie closely observing the drawing of a blue dress and discovering her own face."
        },
        {
            "type": "exam_tips",
            "content": "🔥 **BOARD EXAM HOT TOPICS & CHARACTER ANALYSIS**\n\n**1. Character Sketch of Wanda Petronski:**\n- **Dignified & Forgiving:** Wanda never harbored hatred against Peggy and Maddie despite being mocked daily. She had genuine affection for them, secretly drawing their faces into the designs and gifting them the drawings for Christmas.\n- **Highly Creative & Artistic:** Her 100 exquisite designs won the contest unanimously.\n\n**2. Contrast between Maddie and Peggy's Reactions:**\n- **Peggy:** Rationalizes her bullying by believing that teasing Wanda inspired her drawings. She lacks deep introspection.\n- **Maddie:** Undergoes intense emotional suffering and guilt. She takes moral accountability and makes a lifelong resolution never to remain a silent spectator to cruelty again.\n\n**3. Central Message of the Story:**\n- Teasing and discrimination based on race, appearance, or economic background cause deep emotional scars. Forgiveness and moral courage are the true antidotes to cruelty.",
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        }
    ]

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ch6.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch6.json"
    final_json["metadata"]["id"] = "gseb_class10_english_ch6"
    with open(gseb_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    print("Full-Text English Chapter 6 Generated Successfully!")

if __name__ == "__main__":
    generate_full_english_ch6()
