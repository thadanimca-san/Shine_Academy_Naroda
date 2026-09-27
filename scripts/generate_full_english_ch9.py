import json
import os

def generate_full_english_ch9():
    chapter_id = "ncert_class10_english_ch9"
    title = "Chapter 9: Madam Rides the Bus (First Flight)"
    
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
        "tags": ["english", "first_flight", "madam_rides_the_bus", "full_text", "bilingual", "cbse", "gseb"],
        "learning_outcomes": [
            "Read and comprehend the original NCERT full text of 'Madam Rides the Bus'.",
            "Understand Valli's meticulous planning, courage, independence, and innocent curiosity.",
            "Master difficult vocabulary with contextual bilingual translations (Hindi/Gujarati).",
            "Analyze the deeper philosophical theme of life and death through Valli's journey.",
            "Excel in CBSE/GSEB Board Examination questions (RTCs, Character Sketches, and HOTS)."
        ],
        "ai_context": {
            "learning_goal": "Provide the exact NCERT text broken into passages, with inline translations using backticks for the Smart Translation Filter."
        }
    }
    
    blocks = [
        {
            "type": "hook",
            "content": "Have you ever nurtured a secret dream so intensely that you planned every single detail on your own to make it come true? \n\nMeet **Valliammai (Valli) `(वल्ली / વલ્લી)`**, an extraordinary eight-year-old girl from a small village. While other children played ordinary games, Valli harboured an overwhelming passion—to ride the passenger bus to the town all by herself! \n\nLet's read the *complete, original story* line-by-line to experience her courage, self-discipline, humor, and her profound discovery of the mystery of life and death.",
            "difficulty": "Beginner",
            "bloom": "Understand"
        },
        {
            "type": "diagram",
            "content": "Valli standing at the doorway of her house, watching the bus pass by.",
            "image_url": "assets/images/eng_ch9_valli_doorway.jpg",
            "alt_text": "An eight-year-old girl standing by her doorway watching a bus on the street."
        },
        {
            "type": "theory",
            "title": "Passage 1: Valli and Her Overwhelming Desire",
            "content": "There was a girl named Valliammai who was called Valli for short. She was eight years old and very curious `(जिज्ञासु / જિજ્ઞાસુ)` about things. Her favourite pastime `(मनपसंद शगल या शौक / મનપસંદ શોખ)` was standing in the front doorway of her house, watching what was happening in the street outside.\n\nThere were no playmates of her own age on her street, and this was about all she had to do. But for Valli, standing at the front door was every bit as enjoyable as any of the elaborate `(विस्तृत और जटिल / વિસ્તૃત અને જટિલ)` games other children played. Watching the street gave her many new unusual experiences.\n\nThe most fascinating `(अत्यधिक आकर्षक / અત્યંત આકર્ષક)` thing of all was the bus that travelled between her village and the nearest town. It passed through her street each hour, once going to the town and once coming back. The sight of the bus, filled each time with a new set of passengers, was a source of unending joy `(अनंत आनंद / અનંત આનંદ)` for Valli.\n\nDay after day she watched the bus, and gradually a tiny wish crept into her head and grew there: she wanted to ride on that bus, even if just once. This wish became stronger and stronger, until it was an overwhelming desire `(अत्यधिक तीव्र इच्छा / ખૂબ જ તીવ્ર ઇચ્છા)`. Valli would stare wistfully `(उदासी और ललक से / ઝંખનાપૂર્વક)` at the people who got on or off the bus when it stopped at the street corner. Their faces would kindle `(जगाना या प्रज्वलित करना / પ્રજ્વલિત કરવું)` in her longings, dreams, and hopes. If one of her friends happened to ride the bus and tried to describe the sights of the town to her, Valli would be too jealous `(ईर्ष्यालु / ઈર્ષાળુ)` to listen and would shout, in English: 'Proud! proud!' Neither she nor her friends really understood the meaning of the word, but they used it often as a slang expression of disapproval `(अस्वीकृति जताने वाला मुहावरा / અસ્વીકૃતિ દર્શાવતો શબ્દ)`.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Teacher's Insight:** Notice how Valli's dream is not born out of boredom or greed, but out of pure, aesthetic curiosity. Standing at her doorway wasn't loneliness to her—it was a rich window to observe human life. Her reaction of saying 'Proud! proud!' shows how children invent expressive language to mask their longing."
        },
        {
            "type": "theory",
            "title": "Passage 2: Calculating and Planning the Journey",
            "content": "Over many days and months Valli listened carefully to conversations between her neighbours and people who regularly used the bus, and she also asked a few discreet questions `(सावधानीपूर्वक पूछे गए सवाल / સાવચેતીપૂર્વક પૂછેલા પ્રશ્નો)` here and there. This way she picked up various small details about the journey.\n\nThe town was six miles from her village. The fare was thirty paise one way—'which is almost nothing at all,' she heard one well-dressed man say, but to Valli, who scarcely saw that much money from one month to the next, it seemed a fortune `(बड़ी रकम या दौलत / મોટી રકમ કે સંપત્તિ)`.\n\nThe trip to the town took forty-five minutes. On reaching town, if she stayed in her seat and paid another thirty paise, she could return home on the same bus. This meant that she could take the one-o'clock afternoon bus, reach the town at one forty-five, and be back home by about two forty-five...\n\nOn and on went her calculations and recalculations, plans and replans. She had painstakingly `(अत्यधिक मेहनत और सावधानी से / ખૂબ જ મહેનત અને સાવચેતીથી)` saved whatever stray coins came her way, resisting every temptation `(प्रलोभन / લાલચ)` to buy peppermints `(पुदीने की गोलियां / પીપરમિન્ટ)`, toys, balloons, and the like, and finally she had saved a total of sixty paise. How difficult it had been, particularly that day at the village fair! She had had a strong desire to ride the merry-go-round `(झूला / ચકડોળ)`, even though she had the money, but she had resolutely stifled `(दृढ़तापूर्वक दबा दिया / દૃઢતાપૂર્વક દબાવી દીધી)` her strong desire in order to save the bus fare.\n\nAfter she had enough money saved, her next problem was how to slip out of the house without her mother's knowledge. But she managed this without too much difficulty. Every day after lunch her mother would nap from about one to four or so. Valli always used these hours for her 'excursions' `(छोटी यात्राएं / નાનકડા પ્રવાસો)` as she stood looking from the doorway of her house or sometimes even ventured out `(साहस करके बाहर निकलना / સાહસ કરીને બહાર જવું)` into the village; today, these same hours could be used for her first excursion outside the village.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "How did eight-year-old Valli manage to accumulate the sixty paise required for the bus fare?",
                "options": [
                    "She asked her mother for advance pocket money",
                    "She earned it by doing chores for the neighbours",
                    "She thriftily saved stray coins and resisted temptations like buying toys, balloons, or riding the merry-go-round",
                    "She borrowed the coins secretly from her aunt"
                ],
                "correct_answer": "She thriftily saved stray coins and resisted temptations like buying toys, balloons, or riding the merry-go-round",
                "explanation": "Valli exhibited incredible self-control and maturity for an eight-year-old by suppressing her desire for peppermints, toys, and the village fair's merry-go-round to save sixty paise."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 3: Boarding the Bus and Meeting the Jolly Conductor",
            "content": "One fine spring day the afternoon bus was just on the point of leaving the village and turning into the main highway when a small voice was heard shouting: 'Stop the bus! Stop the bus!' And a tiny hand was raised commandingly `(अधिकारपूर्वक / હુકમભર્યા અંદાજમાં)`.\n\nThe bus slowed down to a crawl `(रेंगने जैसी धीमी गति / અત્યંત ધીમી ગતિ)`, and the conductor, sticking his head out the door, said, 'Hurry then! Tell whoever it is to come quickly.'\n\n'It's me,' shouted Valli. 'I'm the one who has to get on.'\n\nBy now the bus had come to a stop, and the conductor said, 'Oh, really! You don't say so!'\n\n'Yes, I simply have to go to town,' said Valli, still standing outside the bus, 'and here's my money.' She showed him some coins.\n\n'Okay, okay, but first you must get on the bus,' said the conductor, and he stretched out a hand to help her up.\n\n'Never mind,' she said, 'I can get on by myself. You don't have to help me.'\n\nThe conductor was a jolly `(हंसमुख / ખુશમિજાજી)` sort, fond of joking. 'Oh, please don't be angry with me, my fine madam,' he said. 'Right this way, everybody make way `(रास्ता दीजिए / રસ્તો આપો)` for the madam!'\n\nIt was the slack time `(कम भीड़भाड़ वाला समय / ઓછી ભીડ વાળો સમય)` of day, and there were only six or seven passengers on the bus. They were all looking at Valli and laughing with the conductor. Valli was overcome with shyness `(शर्म / શરમ-સંકોચ)`. Avoiding everyone's eyes, she walked quickly to an empty seat and sat down.\n\nThe bus was new, its outside painted a gleaming white `(चमकदार सफेद / ચમકતો સફેદ)` with some green stripes along the sides. Inside, the overhead bars shone like silver. Directly in front of Valli, above the windshield `(हवा रोकने वाला शीशा / વિન્ડશિલ્ડ)`, there was a beautiful clock. The seats were soft and luxurious `(आरामदायक / આરામદાયક)`.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Character Trait - Self-Reliance & Dignity:** Notice Valli's proud declaration: *'I can get on by myself. You don't have to help me.'* Even at age eight, she commands respect and refuses to be patronized as a helpless toddler. The conductor playfully calls her 'Madam', which captures her adult-like self-possession."
        },
        {
            "type": "theory",
            "title": "Passage 4: The Scenic Canal and the Elderly Passenger",
            "content": "Valli devoured `(उत्सुकता से देखना / ઉત્સુકતાથી જોવું)` everything with her eyes. But when she began to look outside, she found her view cut off by a canvas blind `(कैनवास का मोटा पर्दा / કેનવાસનો પડદો)` that covered the lower part of her window. So she stood up on the seat and peered over `(ऊपर से झांकना / ઉપરથી ડોકિયું કરવું)` the blind.\n\nThe bus was now going along the bank of a canal. The road was very narrow `(संकरा / સાંકડો)`. On one side was the canal and, beyond it, palm trees, grassland, distant mountains, and the blue, blue sky. On the other side was a deep ditch `(गहरी खाई / ઊંડી ખાઈ)` and then acres and acres of green fields—green, green, green, as far as the eye could see. Oh, it was all so wonderful!\n\nSuddenly she was startled `(चौंक गई / ચોંકી ગઈ)` by a voice. 'Listen, child,' said the voice, 'you shouldn't stand like that. Sit down.'\n\nSitting down, she looked to see who had spoken. It was an elderly man who had honestly been concerned for her, but she was annoyed `(नाराज / નારાજ)` by his attention.\n\n'There's nobody here who's a child,' she said haughtily `(घमंड और गर्व से / ગર્વ અને અભિમાનથી)`. 'I've paid my thirty paise like everyone else.'\n\nThe conductor chimed in `(बीच में बोलना / વચ્ચે બોલ્યો)`. 'Oh, sir, but this is a very grown-up madam. Do you think a mere girl could pay her own fare and travel to the city all alone?'\n\nValli shot an angry glance at the conductor and said, 'I am not a madam. Please remember that. And you've not yet given me my ticket.'\n\n'I'll remember,' the conductor said, mimicking `(नकल उतारते हुए / નકલ કરતા)` her tone. Everyone laughed, and gradually Valli too joined in the laughter.\n\nThe conductor punched a ticket and handed it to her. 'Just sit back and make yourself comfortable. Why should you stand when you've paid for a seat?'\n\n'Because I want to,' she answered, standing up again.\n\n'If you stand on the seat, you may fall and hurt yourself when the bus makes a sharp turn or hits a bump. That's why we want you to sit down, child.'\n\n'I'm not a child, I tell you,' she said, irritated `(चिढ़कर / ચીડાઈને)`. 'I'm eight years old.'\n\n'Of course, of course. How stupid of me! Eight years—my!'",
            "difficulty": "Intermediate",
            "bloom": "Analyze"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Why did Valli react with annoyance when the elderly passenger told her to sit down?",
                "options": [
                    "Because she wanted to jump out of the bus window",
                    "Because she resented being treated as an incompetent child when she had paid the full fare like everyone else",
                    "Because the seats were dirty and stained",
                    "Because the elderly passenger took her seat"
                ],
                "correct_answer": "Because she resented being treated as an incompetent child when she had paid the full fare like everyone else",
                "explanation": "Valli took immense pride in paying her own fare and viewed herself as an independent passenger with equal rights, making her dislike being addressed patronizingly as a 'child'."
            },
            "difficulty": "Intermediate",
            "bloom": "Analyze"
        },
        {
            "type": "theory",
            "title": "Passage 5: The Repulsive Elderly Woman",
            "content": "The bus stopped, some new passengers got on, and the conductor got busy for a time. Afraid of losing her seat, Valli finally sat down.\n\nAn elderly woman came and sat beside her. 'Are you all alone, dear?' she asked Valli as the bus started again.\n\nValli found the woman absolutely repulsive `(घिनौनी या अरुचिकर / અણગમતી કે ઘૃણાસ્પદ)`—such big holes she had in her earlobes `(कान के निचले हिस्से / કાનની બૂટ)`, and such ugly earrings in them! And she could smell the betel nut `(सुपारी / સોપારી)` the woman was chewing and see the betel juice `(पान का रस / પાનનો રસ)` that was threatening to spill over her lips at any moment. Who could be sociable `(मिलनसार / મળતાવડા)` with such a person?\n\n'Yes, I'm travelling alone,' she answered curtly `(रूखेपन से / ટૂંકા અને તીખા અવાજમાં)`. 'And I've got a ticket too.'\n\n'Yes, she's on her way to town,' said the conductor. 'With a thirty-paise ticket.'\n\n'Oh, why don't you mind your own business,' said Valli. But she laughed all the same, and the conductor laughed too.\n\nThe old woman continued with her drivel `(निरर्थक बकवास / નકામી બકવાસ)`: 'Is it proper for such a young person to travel alone? Do you know exactly where you're going in town? What's the street? What's the house number?'\n\n'You needn't bother about me. I can take care of myself,' Valli said, turning her face towards the window and staring out.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Board Exam Focus - Safety & Street Smartness:** Why does Valli cut off the elderly woman? Although the woman might have had good intentions, she represents inquisitive, intrusive strangers. Valli is street-smart and protects herself by refusing to disclose personal details like her destination or house address."
        },
        {
            "type": "theory",
            "title": "Passage 6: The Galloping Cow and Arrival at Town",
            "content": "The bus rolled on now cutting across a bare landscape, now rushing through a tiny hamlet `(छोटा गाँव या बस्ती / નાનું ગામડું કે વસ્તી)` or past an odd wayside shop. Sometimes the bus seemed on the point of gobbling up `(निगल लेना / ગળી જવું)` another vehicle that was coming towards them or a pedestrian crossing the road. But lo! somehow it passed on smoothly, leaving all obstacles safely behind.\n\nTrees came running towards them but then stopped as the bus reached them and simply stood there helpless for a moment by the side of the road before rushing away in the other direction.\n\nSuddenly Valli clapped her hands with glee `(अत्यधिक खुशी और उल्लास / અતિશય આનંદ અને ઉલ્લાસ)`. A young cow, tail high in the air, was running very fast, right in the middle of the road, right in front of the bus. The bus slowed to a crawl, and the driver sounded his horn loudly again and again. But the more he honked, the more frightened the animal became and the faster it galloped `(तेजी से दौड़ना / ઝડપથી દોડવું)`—always right in front of the bus.\n\nSomehow this was very funny to Valli. She laughed and laughed until there were tears in her eyes.\n\n'Hey, lady, haven't you laughed enough?' called the conductor. 'Better save some for tomorrow.'\n\nAt last the cow moved off the road. And soon the bus came to a railroad crossing `(रेलवे फाटक / રેલવે ફાટક)`. A speck of a train could be seen in the distance, growing bigger and bigger as it drew near. Then it rushed past the crossing gate with a tremendous roar `(भीषण गर्जना / ભયંકર ગર્જના)` and rattle `(खड़खड़ाहट / ખડખડાટ)`, shaking the bus. Then the bus went on and passed the train station.\n\nFrom there it traversed a busy, well-laid-out shopping street and, turning, entered a wider thoroughfare `(चौड़ा मुख्य मार्ग / મુખ્ય માર્ગ)`. Such big, bright-looking shops! What glittering displays `(चमकदार प्रदर्शन / ઝગમગતું પ્રદર્શન)` of clothes and other merchandise `(व्यापार का सामान / વેપારનો સામાન)`! Such big crowds! Struck dumb with wonder `(आश्चर्य से अवाक / આશ્ચર્યથી સ્તબ્ધ)`, Valli gaped at everything.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "What sight made Valli clap her hands in sheer glee and laugh until tears came into her eyes?",
                "options": [
                    "The conductor dropping his ticket punch",
                    "A young cow with its tail high in the air running frantically in front of the honking bus",
                    "The glittering mannequins and clothes displayed in the town's shopping street",
                    "The elderly woman spilling her betel juice"
                ],
                "correct_answer": "A young cow with its tail high in the air running frantically in front of the honking bus",
                "explanation": "The comical sight of the frightened young cow galloping faster and faster right in front of the bus as the driver honked his horn caused Valli uncontrollable laughter."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 7: The Conductor's Offer and Valli's Firm Integrity",
            "content": "Then the bus stopped and everyone got off except Valli.\n\n'Hey, lady,' said the conductor, 'aren't you ready to get off? This is as far as your thirty paise takes you.'\n\n'No,' Valli said, 'I'm going back on this same bus.' She took another thirty paise from her pocket and handed the coins to the conductor.\n\n'Why, is something the matter?'\n\n'No, nothing's the matter. I just felt like having a bus ride, that's all.'\n\n'Don't you want to have a look at the sights, now that you're here?'\n\n'All by myself? Oh, I'd be much too afraid.'\n\nGreatly amused by the girl's way of speaking, the conductor said, 'But you weren't afraid to come in the bus.'\n\n'Nothing to be afraid of about that,' she answered.\n\n'Well, then, why not go to that stall over there and have something to drink? Nothing to be afraid of about that either.'\n\n'Oh, no, I couldn't do that.'\n\n'Well, then, let me bring you a cold drink.'\n\n'No, I don't have enough money. Just give me my ticket, that's all.'\n\n'It'll be my treat `(मेरी तरफ से दावत / મારી તરફથી ટ્રીટ)` and not cost you anything.'\n\n'No, no,' she said firmly `(दृढ़तापूर्वक / દૃઢતાપૂર્વક)`, 'please, no.'\n\nThe conductor shrugged `(कंधे उचकाए / ખભા ઉંચક્યા)`, and they waited until it was time for the bus to begin the return journey. Again there weren't many passengers.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Character Trait - Self-Control and Moral Dignity:** Despite being tempted by a refreshing cold drink on a hot day, Valli firmly turns down the conductor's offer because she has no money to pay for it. She refuses to accept charity or favors from a stranger, exemplifying extraordinary self-respect and boundaries."
        },
        {
            "type": "theory",
            "title": "Passage 8: The Tragedy of the Dead Cow and Silent Realization",
            "content": "'Won't your mother be looking for you?' the conductor asked when he gave the girl her ticket.\n\n'No, no one will be looking for me,' she said.\n\nThe bus started, and again there were the same wonderful sights. Valli wasn't bored in the slightest and greeted everything with the same excitement she'd felt the first time.\n\nBut suddenly she saw a young cow lying dead by the roadside, just where it had been struck by some fast-moving vehicle.\n\n'Isn't that the same cow that ran in front of the bus on our trip to town?' she asked the conductor.\n\nThe conductor nodded, and she was overcome with sadness `(उदासी से घिर जाना / ઉદાસીથી ઘેરાઈ જવું)`. What had been a lovable, beautiful creature just a little while ago had now suddenly lost its charm and its life and looked so horrible, so frightening as it lay there, legs spread-eagled `(हाथ-पैर फैले हुए / હાથ-પગ ફેલાયેલી હાલતમાં)`, a fixed stare in its lifeless eyes, blood all over...\n\nThe bus moved on. The memory of the dead cow haunted `(बार-बार सताना / વારંવાર યાદ આવીને સતાવવું)` her, dampening her enthusiasm `(उसके उत्साह को धीमा कर दिया / તેના ઉત્સાહને ઓસારી નાખ્યો)`. She no longer wanted to look out the window.\n\nShe sat thus, glued to her seat `(सीट से चिपकी हुई / સીટ પર ચોંટીને)`, until the bus reached her village at three forty. She stood up and stretched herself. Then she turned to the conductor and said, 'Well, sir, I hope to see you again.'\n\n'Okay, madam,' he answered her, smiling. 'Whenever you feel like a bus ride, come and join us. And don't forget to bring your fare!'\n\nShe laughed and jumped down from the bus. Then away she went, running straight for home.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "What philosophical transformation did Valli undergo after seeing the dead cow on the roadside?",
                "options": [
                    "She decided never to travel on a bus again",
                    "She realized that animals should not be allowed on paved roads",
                    "Her innocent excitement was subdued as she confronted the harsh, fragile, and sudden nature of death",
                    "She became terrified that the bus driver was unsafe"
                ],
                "correct_answer": "Her innocent excitement was subdued as she confronted the harsh, fragile, and sudden nature of death",
                "explanation": "The contrast between the playful cow galloping earlier and its blood-stained, lifeless body shattered Valli's naive joy, introducing her to the profound and sober reality of mortality."
            },
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        },
        {
            "type": "theory",
            "title": "Passage 9: Back Home and the Unspoken Secret",
            "content": "When she entered her house she found her mother awake and talking to one of Valli's aunts, the one from South Street. This aunt was a real chatterbox `(बहुत बातूनी / બહુ બોલકી)`, never closing her mouth once she started talking.\n\n'And where have you been?' asked her aunt when Valli came in. She spoke casually, not expecting a real reply. So Valli just smiled, and her mother and aunt went on with their conversation.\n\n'Yes, you're right,' her mother said. 'So many things in our midst `(हमारे बीच / આપણી વચ્ચે)` and in the world outside. How can we possibly know about everything? And even when we do know about something, we often can't understand it completely, can we?'\n\n'Oh, yes!' breathed Valli.\n\n'What?' asked her mother. 'What is that you say?'\n\n'Oh,' said Valli, 'I was just agreeing with what you said about things happening without our knowledge.'\n\n'Just look at that chit of a girl `(नासमझ या छोटी सी लड़की / નાની એવી છોકરી)`!' exclaimed her aunt. 'Watch how she pokes her nose `(टांग अड़ाना या दखल देना / દખલ દેવી)` into our conversation, just as though she were a grown lady.'\n\nValli smiled to herself. She didn't want them to understand her smile. But, then, there wasn't much chance of that, was there?",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "diagram",
            "content": "Valli smiling knowingly at home as her mother and aunt talk about the world outside.",
            "image_url": "assets/images/eng_ch9_valli_secret_smile.jpg",
            "alt_text": "An eight-year-old girl smiling thoughtfully to herself at home."
        },
        {
            "type": "exam_tips",
            "content": "🔥 **BOARD EXAM MASTERY GUIDE: Key Themes & Character Analysis**\n\n"
                       "**1. Character Sketch of Valli (5 Marks High-Yield Question):**\n"
                       "- **Meticulous Planner:** Gathered every minute detail (distance = 6 miles, fare = 30 paise, duration = 45 mins) and timed her trip with her mother's nap (1:00 PM to 2:45 PM).\n"
                       "- **Tremendous Self-Discipline:** Resisted temptations like candies, toys, and the village fair's merry-go-round to save 60 paise.\n"
                       "- **Dignified & Self-Reliant:** Refused help boarding the bus, declined a free drink from the conductor, and asserted her independence.\n"
                       "- **Mature & Sensitive:** Understood the profound lesson of life and death when she saw the dead cow.\n\n"
                       "**2. Central Theme - The Initiation into Life & Death:**\n"
                       "The story represents a transition from innocent childhood into deeper worldly awareness. The cow that represented comical joy on the outward journey becomes a symbol of mortality on the return, teaching Valli that life and death are intertwined.\n\n"
                       "**3. Irony in the Climax:**\n"
                       "Valli's mother remarks that no one can know everything happening in the outside world. Ironically, Valli had just returned from a solo journey into that very world without her mother having the slightest clue!",
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        }
    ]

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ch9.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch9.json"
    final_json["metadata"]["id"] = "gseb_class10_english_ch9"
    with open(gseb_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    print("Full-Text English Chapter 9 Generated Successfully!")

if __name__ == "__main__":
    generate_full_english_ch9()
