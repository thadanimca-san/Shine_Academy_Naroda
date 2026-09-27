import json
import os

def generate_full_english_ch4():
    chapter_id = "ncert_class10_english_ch4"
    title = "Chapter 4: From the Diary of Anne Frank (First Flight)"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "Interactive Full-Text Reading & Master Analysis",
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
        "tags": ["english", "first_flight", "anne_frank", "full_text", "bilingual", "board_mastery"],
        "learning_outcomes": [
            "Read and comprehend the original NCERT text of Anne Frank's diary.",
            "Master key vocabulary with contextual Hindi and Gujarati translations.",
            "Analyze Anne Frank's wit, emotional maturity, and character traits.",
            "Understand the dynamic relationship between Anne and Mr. Keesing.",
            "Ace Board Exam 3-mark and 5-mark subjective and objective questions."
        ],
        "ai_context": {
            "learning_goal": "Provide the exact NCERT text broken into passages, with inline translations using backticks for the Smart Translation Filter.",
            "common_misconceptions": [
                "Students mistakenly assume Anne Frank had no friends at all in real life (she had ~30 friends, but lacked a true confidante).",
                "Students view Mr. Keesing as a cruel enemy rather than a strict teacher who appreciated Anne's wit and creativity."
            ]
        }
    }
    
    blocks = [
        {
            "type": "hook",
            "content": "Imagine being a 13-year-old girl living during World War II, surrounded by friends and a loving family, yet feeling completely alone inside because you have no one in whom you can confide your innermost feelings. Anne Frank made a life-changing decision: she turned a red-and-white checked notebook into her dearest confidante, naming her **'Kitty' `(किट्टी / કિટી)`**.\n\nLet us read the *original, complete text* of her world-famous diary line-by-line to experience her razor-sharp wit, her poignant reflections, and her hilarious classroom battles with her maths teacher, Mr. Keesing!",
            "difficulty": "Beginner",
            "bloom": "Understand"
        },
        {
            "type": "diagram",
            "content": "Anne Frank writing in her diary 'Kitty' in the Secret Annex.",
            "image_url": "assets/images/eng_ch4_anne_writing.jpg",
            "alt_text": "A thoughtful young girl writing in a diary with a fountain pen."
        },
        {
            "type": "theory",
            "title": "Passage 1: Paper Has More Patience Than People",
            "content": "Writing in a diary is a really strange experience for someone like me. Not only because I've never written anything before, but also because it seems to me that later on neither I nor anyone else will be interested in the musings `(गहन विचार / ઊંડા વિચારો)` of a thirteen-year-old schoolgirl. Oh well, it doesn't matter. I feel like writing, and I have an even greater need to get all kinds of things off my chest `(मन की बात खुलकर कहना / મનની વાત હળવી કરવી)`.\n\n'Paper has more patience than people `(कागज में लोगों की तुलना में अधिक धैर्य होता है / કાગળમાં લોકો કરતાં વધુ ધીરજ હોય છે)`.' I thought of this saying on one of those days when I was feeling a little depressed and was sitting at home with my chin in my hands, bored and listless `(उत्साहहीन / ઉત્સાહ વગરનું)`, wondering whether to stay in or go out. I finally stayed where I was, brooding `(गंभीर सोच में डूबा / ઊંડા વિચારમાં ડૂબેલું)`: Yes, paper does have more patience, and since I'm not planning to let anyone else read this stiff-backed notebook grandly referred to as a 'diary', unless I should ever find a real friend, it probably won't make a bit of difference.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Teacher's Insight: The Philosophy of 'Paper has more patience than people'**\n\nHumans get bored, judgmental, impatient, or break confidences when you share your deepest secrets. Paper, on the other hand, listens silently without interrupting, judging, or betraying trust. This profound observation by a 13-year-old girl is a frequent theme in Board Exam questions!"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Why did Anne Frank believe that 'paper has more patience than people'?",
                "options": [
                    "Because paper never gets bored, never judges, and can listen to anything without losing patience",
                    "Because books are cheaper than having human friends",
                    "Because she wanted to publish a best-selling novel",
                    "Because her teachers told her to write diaries"
                ],
                "correct_answer": "Because paper never gets bored, never judges, and can listen to anything without losing patience",
                "explanation": "Anne felt that human beings lack the patience to listen to someone's inner musings without interruption or judgment, whereas paper absorbs thoughts silently and patiently."
            },
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "theory",
            "title": "Passage 2: Why I Started a Diary (The Search for a True Friend)",
            "content": "Now I'm back to the point that prompted me to keep a diary in the first place: I don't have a friend.\n\nLet me put it more clearly, since no one will believe that a thirteen-year-old girl is completely alone in the world. And I'm not. I have loving parents and a sixteen-year-old sister, and there are about thirty people I can call friends. I have a family, loving aunts and a good home. No, on the surface I seem to have everything, except my one true friend `(एक सच्चा दोस्त / એક સાચો મિત્ર)`.\n\nAll I think about when I'm with friends is having a good time. I can't bring myself to talk about anything but ordinary everyday things. We don't seem to be able to get any closer, and that's the problem. Maybe it's my fault that we don't confide `(विश्वास करके गुप्त बात बताना / વિશ્વાસ રાખીને ખાનગી વાત કહેવી)` in each other. In any case, that's just how things are, and unfortunately they're not liable `(संभावित / સંભાવના હોવી)` to change. This is why I've started the diary.\n\nTo enhance `(बढ़ाना या निखारना / વધારવું કે સુધારવું)` the image of this long-awaited friend in my imagination, I don't want to jot down the facts in this diary the way most people would do, but I want the diary to be my friend, and I'm going to call this friend 'Kitty'.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Board Exam Distinction: Casual Friends vs. A True Confidante**\n\nNotice that Anne was NOT an outcast or anti-social. She had ~30 casual friends and a warm family. However, she lacked intimacy—someone to whom she could open her heart completely. That is why she personalized her diary as an imaginary companion named **Kitty**."
        },
        {
            "type": "theory",
            "title": "Passage 3: A Brief Sketch of My Life",
            "content": "Since no one would understand a word of my stories to Kitty if I were to plunge `(सीधे कूद पड़ना / સીધા કૂદી પડવું)` right in, I'd better provide a brief sketch of my life, much as I dislike doing so.\n\nMy father, the most adorable `(प्यारे और आदरणीय / વહાલા અને આદરણીય)` father I've ever seen, didn't marry my mother until he was thirty-six and she was twenty-five. My sister, Margot, was born in Frankfurt in Germany in 1926. I was born on 12 June 1929. I lived in Frankfurt until I was four. My father emigrated `(देश छोड़कर दूसरे देश में बसना / દેશ છોડી બીજા દેશમાં સ્થળાંતર કરવું)` to Holland in 1933. My mother, Edith Hollander Frank, went with him to Holland in September, while Margot and I were sent to Aachen to stay with our grandmother. Margot went to Holland in December, and I followed in February, when I was plunked down `(अचानक रख दिया गया / અચાનક મૂકી દેવામાં આવ્યું)` on the table as a birthday present for Margot.\n\nI started right away at the Montessori nursery school. I stayed there until I was six, at which time I started in the first form. In the sixth form my teacher was Mrs Kuperus, the headmistress. At the end of the year we were both in tears as we said a heartbreaking farewell `(दर्दनाक विदाई / હૃદયદ્રાવક વિદાય)`.\n\nIn the summer of 1941 Grandma fell ill and had to have an operation, so my birthday passed with little celebration. Grandma died in January 1942. No one knows how often I think of her and still love her. This birthday celebration in 1942 was intended to make up for the other, and Grandma's candle was lit along with the rest.\n\nThe four of us are still doing well, and that brings me to the present date of 20 June 1942, and the solemn `(गंभीर और निष्ठावान / ગંભીર અને નિષ્ઠાવાન)` dedication of my diary.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "How did Anne honor her deceased grandmother during her 1942 birthday celebration?",
                "options": [
                    "By lighting Grandma's candle along with the rest",
                    "By writing a long poem in her memory",
                    "By planting a tree in her garden",
                    "By refusing to celebrate her birthday"
                ],
                "correct_answer": "By lighting Grandma's candle along with the rest",
                "explanation": "Anne deeply loved her grandmother, and in her 1942 birthday celebration, a special candle was lit for Grandma alongside her birthday candles."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 4: Saturday, 20 June 1942 - Class Quaking in Its Boots",
            "content": "Dearest Kitty,\n\nOur entire class is quaking in its boots `(डर और घबराहट से कांपना / ડર અને ચિંતાથી ધ્રૂજવું)`. The reason, of course, is the forthcoming `(आगामी / આવનારું)` meeting in which the teachers decide who'll move up to the next form and who'll be kept back. Half the class is making bets. G.N. and I laugh ourselves silly at the two boys behind us, C.N. and Jacques, who have staked `(दांव पर लगा दिया / દાવ પર લગાવી દીધું)` their entire holiday savings on their bet.\n\n'From morning to night, it's \"You're going to pass\", \"No, I'm not\", \"Yes, you are\", \"No, I'm not\".' Even G.'s pleading glances and my angry outbursts can't calm them down. If you ask me, there are so many dummies `(मूर्ख या कमजोर छात्र / નબળા વિદ્યાર્થીઓ)` that about a quarter of the class should be kept back, but teachers are the most unpredictable `(अनपेक्षित / જેની આગાહી ન કરી શકાય તેવું)` creatures on earth.\n\nI'm not so worried about my girlfriends and myself. We'll make it. The only subject I'm not sure about is maths. Anyway, all we can do is wait. Until then, we keep telling each other not to lose heart `(हिम्मत न हारना / હિંમત ન હારવી)`.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Exam Hot Question:** Why does Anne describe teachers as 'the most unpredictable creatures on earth'?\nBecause no one can ever guess what criteria teachers will use in their meetings to promote or detain students. Even students who seem completely dull might pass, while confident ones might fail!"
        },
        {
            "type": "theory",
            "title": "Passage 5: The Math Teacher - Mr. Keesing",
            "content": "I get along pretty well with all my teachers. There are nine of them, seven men and two women. Mr Keesing, the old fogey `(पुराने ख्यालात का व्यक्ति / જૂના વિચારોવાળી વ્યક્તિ)` who teaches maths, was annoyed with me for ages because I talked so much. After several warnings, he assigned me extra homework. An essay on the subject, 'A Chatterbox `(बातूनी व्यक्ति / વાતોડિયું માણસ)`'.\n\nA chatterbox — what can you write about that? I'd worry about that later, I decided. I jotted down the title in my notebook, tucked it in my bag and tried to keep quiet.\n\nThat evening, after I'd finished the rest of my homework, the note about the essay caught my eye. I began thinking about the subject while chewing the tip of my fountain pen. Anyone could ramble on `(बिना मतलब लंबी-चौड़ी बातें करना / અર્થ વગર લાંબી વાતો કરવી)` and leave big spaces between the words, but the trick was to come up with convincing arguments `(ठोस और प्रभावशाली तर्क / પ્રભાવશાળી દલીલો)` to prove the necessity of talking.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "What was the initial punishment given to Anne by Mr. Keesing for talking in class?",
                "options": [
                    "Writing an essay on 'A Chatterbox'",
                    "Standing outside the classroom for two hours",
                    "Doing 50 extra mathematics problems",
                    "Writing an apology letter to the principal"
                ],
                "correct_answer": "Writing an essay on 'A Chatterbox'",
                "explanation": "Mr. Keesing assigned her an extra essay titled 'A Chatterbox' to teach her a lesson about excessive talking."
            },
            "difficulty": "Beginner",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 6: The Argument for Talking",
            "content": "I thought and thought, and suddenly I had an idea. I wrote the three pages Mr Keesing had assigned me and was satisfied. I argued that talking is a student's trait `(विद्यार्थी का स्वाभाविक लक्षण / વિદ્યાર્થીનું સ્વાભાવિક લક્ષણ)` and that I would do my best to keep it under control, but that I would never be able to cure myself of the habit since my mother talked as much as I did if not more, and that there's not much you can do about inherited traits `(विरासत में मिले आनुवंशिक गुण / વારસામાં મળેલા લક્ષણો)`.\n\nMr Keesing had a good laugh at my arguments, but when I proceeded to talk my way through the next lesson, he assigned me a second essay. This time it was supposed to be on 'An Incorrigible Chatterbox `(एक ऐसा बातूनी जिसे कभी सुधारा न जा सके / ન સુધારી શકાય તેવું વાતોડિયું)`'. I handed it in, and Mr Keesing had nothing to complain about for two whole lessons.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Anne's Wit & Clever Logic:**\nNotice Anne's defense: She doesn't just say 'Sorry, I won't do it again.' She brilliantly argues that:\n1. Talking is an inherent student trait.\n2. She inherited it genetically from her talkative mother, so it is incurable!\nThis clever psychological reasoning made even the strict Mr. Keesing laugh out loud."
        },
        {
            "type": "theory",
            "title": "Passage 7: The Third Assignment - 'Quack, Quack, Quack'",
            "content": "However, during the third lesson he'd finally had enough. 'Anne Frank, as punishment for talking in class, write an essay entitled — \"Quack, Quack, Quack, Said Mistress Chatterbox\".'\n\nThe class roared `(पूरी कक्षा ठहाके मारकर हंस पड़ी / આખો વર્ગ ખડખડાટ હસી પડ્યો)`. I had to laugh too, though I'd nearly exhausted my ingenuity `(रचनात्मक प्रतिभा और बुद्धिमानी / સર્જનાત્મક બુદ્ધિ અને ચતુરાઈ)` on the topic of chatterboxes. It was time to come up with something else, something original.\n\nMy friend, Sanne, who's good at poetry, offered to help me write the essay from beginning to end in verse `(कविता या पद्य के रूप में / કવિતાના રૂપમાં)` and I jumped for joy. Mr Keesing was trying to play a joke on me with this ridiculous `(हास्यास्पद / હાસ્યાસ્પદ)` subject, but I'd make sure the joke was on him.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "theory",
            "title": "Passage 8: The Poem of the Father Swan and The Happy Ending",
            "content": "I finished my poem, and it was beautiful! It was about a mother duck and a father swan with three baby ducklings who were bitten to death by the father because they quacked too much.\n\nLuckily, Mr Keesing took the joke the right way `(मजाक को सकारात्मक और सही तरीके से लिया / મજાકને હકારાત્મક રીતે લીધી)`. He read the poem to the class, adding his own comments, and to several other classes as well. Since then I've been allowed to talk and haven't been assigned any extra homework. On the contrary `(इसके विपरीत / તેનાથી ઉલટું)`, Mr Keesing's always making jokes these days.\n\nYours,\nAnne",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "diagram",
            "content": "Mr. Keesing enjoying Anne's verse in class and sharing the joke with the students.",
            "image_url": "assets/images/eng_ch4_mr_keesing_reading.jpg",
            "alt_text": "A cheerful math teacher reading a poem to his students in class."
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "What happened to the three baby ducklings in Anne's satirical poem?",
                "options": [
                    "They were bitten to death by their father swan because they quacked too much",
                    "They flew away to another lake to escape punishment",
                    "They learned how to swim silently without making any noise",
                    "They became friends with the math teacher"
                ],
                "correct_answer": "They were bitten to death by their father swan because they quacked too much",
                "explanation": "In her satirical poem, the father swan bit the baby ducklings to death due to their excessive quacking. Mr. Keesing got the gentle, witty hint that silencing natural chatter is absurdly harsh."
            },
            "difficulty": "Intermediate",
            "bloom": "Analyze"
        },
        {
            "type": "exam_tips",
            "content": "🔥 **BOARD EXAM HIGH-PROBABILITY QUESTIONS & MODEL ANSWERS**\n\n---\n\n### Q1. Give a character sketch of Anne Frank. (5 Marks)\n**Answer Model:**\n1. **Intelligent and Witty:** Anne possessed sharp intellectual prowess. When punished for talking, she did not grumble or copy generic essays; instead, she used clever arguments (inherited traits) and poetry to win over her teacher.\n2. **Emotionally Mature & Deep Thinker:** At just 13, she observed that *'paper has more patience than people'* and recognized that true friendship requires deep emotional intimacy.\n3. **Loving & Sensitive:** She had profound love for her grandmother (lighting a candle in her memory) and her former teacher Mrs. Kuperus.\n4. **Humorous & Lively:** Despite the strictness of Mr. Keesing, she turned punishments into creative masterpieces and entertained the entire classroom.\n\n---\n\n### Q2. How did Mr. Keesing react to Anne's third essay? What does it reveal about his personality? (3 Marks)\n**Answer Model:**\nMr. Keesing took the satirical joke in the right spirit. He read Anne's verse aloud to her class with his own remarks, and even shared it with other classes. He stopped penalizing Anne and began cracking jokes in class. This reveals that despite being an 'old fogey' and strict disciplinarian, Mr. Keesing was sporting, possessed a good sense of humor, and genuinely appreciated creativity and wit in his students.\n\n---\n\n### Q3. Why did Anne decide to write a diary and name it 'Kitty'? (3 Marks)\n**Answer Model:**\nAnne felt that despite having loving parents, a sister, and about thirty acquaintances, she lacked a true friend in whom she could confide her deepest feelings. She believed paper has more patience than humans. To make the diary feel like a genuine, long-awaited confidante rather than a factual logbook, she affectionately christened it 'Kitty'.",
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        }
    ]

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ch4.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch4.json"
    final_json["metadata"]["id"] = "gseb_class10_english_ch4"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Full-Text English Chapter 4 Generated Successfully!")

if __name__ == "__main__":
    generate_full_english_ch4()
