import json
import os

data = {}

def create_module(subject, grade, chapter_num, title, blocks):
    module_id = f"ncert_class{grade}_{subject}_ch{chapter_num}_mock"
    return {
        "metadata": {
            "id": module_id,
            "title": f"Chapter {chapter_num}: {title}",
            "subtitle": f"Class {grade} {subject.capitalize()} (NCERT)",
            "subject": subject.capitalize(),
            "grade": grade,
            "board": "NCERT",
            "curriculum": ["NCERT"],
            "language": "English",
            "difficulty": "Beginner",
            "estimated_minutes": 30,
            "version": "1.0.0",
            "author": "EduOS Gold Standard Editor",
            "reviewed_by": "EduOS",
            "last_updated": "2026-08-10T00:00:00Z",
            "tags": [subject.capitalize(), f"Class {grade}", "NCERT"],
            "learning_outcomes": [f"Master concepts of {title}"],
            "ai_context": {}
        },
        "blocks": blocks
    }

content = {
    "evs": {
        1: {"title": "Going to School", "qs": [
            {"type": "quiz", "content": {"question": "Which bridge is made of cement, bricks and iron rods?", "options": ["Bamboo bridge", "Cement bridge", "Rope bridge", "Vallam"], "correct_index": 1}},
            {"type": "quiz", "content": {"question": "What is a 'Vallam' used in Kerala?", "options": ["A type of food", "A small wooden boat", "A big bus", "A train"], "correct_index": 1}},
            {"type": "true_false", "content": {"question": "In Rajasthan, children use camel carts to reach school.", "answer": "True"}},
            {"type": "true_false", "content": {"question": "Jugaad is a vehicle used in Gujarat that makes a phut-phut sound.", "answer": "True"}},
            {"type": "fill_blank", "content": {"question": "A trolley is an open box made of wood, attached with a ________ to cross rivers.", "answer": "rope"}},
            {"type": "fill_blank", "content": {"question": "In the mountains of Uttarakhand, the paths are rocky and ________.", "answer": "uneven"}},
            {"type": "short_note", "content": {"question": "How do children in the Northern Hills travel to school when there is a lot of snow?", "answer": "They hold hands and walk carefully. If the snow is soft, their feet sink into it. If it is frozen, they may slip and fall."}},
            {"type": "short_note", "content": {"question": "What is a pulley and how does it help in a trolley?", "answer": "A pulley is a simple machine that helps to pull the trolley across a river by moving the rope easily."}}
        ]},
        2: {"title": "Ear to Ear", "qs": [
            {"type": "quiz", "content": {"question": "Which animal has ears like fans?", "options": ["Elephant", "Mouse", "Rabbit", "Dog"], "correct_index": 0}},
            {"type": "quiz", "content": {"question": "Which of these animals does NOT have hair on its body?", "options": ["Cat", "Frog", "Cow", "Pig"], "correct_index": 1}},
            {"type": "true_false", "content": {"question": "Birds have tiny holes on both sides of their heads instead of visible ears.", "answer": "True"}},
            {"type": "true_false", "content": {"question": "Animals with visible ears and hair on their body lay eggs.", "answer": "False"}},
            {"type": "fill_blank", "content": {"question": "A crocodile has tiny holes for ________ but we cannot see them easily.", "answer": "ears"}},
            {"type": "fill_blank", "content": {"question": "Animals whose ears you cannot see from the outside generally lay ________.", "answer": "eggs"}},
            {"type": "short_note", "content": {"question": "Why do different animals have different patterns on their skin?", "answer": "The patterns on animals' skin are due to the hair on their skin."}},
            {"type": "short_note", "content": {"question": "Describe the ears of a rabbit.", "answer": "A rabbit has ears like leaves, situated on the top of its head."}}
        ]},
        3: {"title": "A Day with Nandu", "qs": [
            {"type": "quiz", "content": {"question": "Who is Nandu in the chapter?", "options": ["A baby elephant", "A baby monkey", "A human child", "A bird"], "correct_index": 0}},
            {"type": "quiz", "content": {"question": "What does a herd of elephants mainly consist of?", "options": ["Only male elephants", "Only females and baby elephants", "Equal males and females", "Only old elephants"], "correct_index": 1}},
            {"type": "true_false", "content": {"question": "An adult elephant can eat more than 100 kilograms of leaves and twigs in a day.", "answer": "True"}},
            {"type": "true_false", "content": {"question": "Elephants sleep for 8 to 10 hours a day.", "answer": "False"}},
            {"type": "fill_blank", "content": {"question": "The oldest ________ elephant is the leader of the herd.", "answer": "female"}},
            {"type": "fill_blank", "content": {"question": "Elephants use their big ears like ________ to keep themselves cool.", "answer": "fans"}},
            {"type": "short_note", "content": {"question": "Why do elephants love to play in mud and water?", "answer": "The mud keeps their skin cool and protects it."}},
            {"type": "short_note", "content": {"question": "When do male elephants leave their herd?", "answer": "Male elephants leave the herd when they are 14 or 15 years old and move around alone."}}
        ]},
        4: {"title": "The Story of Amrita", "qs": [
            {"type": "quiz", "content": {"question": "Where did Amrita live?", "options": ["Khejadli village", "Jaipur city", "Bhopal", "A village in Kerala"], "correct_index": 0}},
            {"type": "quiz", "content": {"question": "Why was the village named Khejadli?", "options": ["Because of a king", "Because of the Khejadi trees that grew there", "Because of a river", "Because of a mountain"], "correct_index": 1}},
            {"type": "true_false", "content": {"question": "The elders of Khejadli village used to say 'Agar ped hain to hum hain'.", "answer": "True"}},
            {"type": "true_false", "content": {"question": "The King ordered his men to cut trees to build a temple.", "answer": "False"}},
            {"type": "fill_blank", "content": {"question": "Amrita and the villagers hugged the ________ to protect them from being cut.", "answer": "trees"}},
            {"type": "fill_blank", "content": {"question": "The people of this area, known as ________, continue to protect plants and animals today.", "answer": "Bishnois"}},
            {"type": "short_note", "content": {"question": "Why did the king's men want to cut the trees?", "answer": "The king's men wanted wood to build a new palace for the king."}},
            {"type": "short_note", "content": {"question": "What is special about the Khejadi tree?", "answer": "It can grow without much water. Its bark is used for making medicines, its wood is not affected by insects, and animals eat its leaves."}}
        ]},
        5: {"title": "Anita and the Honeybees", "qs": [
            {"type": "quiz", "content": {"question": "Where does Anita Khushwaha live?", "options": ["Bochaha village in Bihar", "A village in Assam", "Delhi", "Khejadli village"], "correct_index": 0}},
            {"type": "quiz", "content": {"question": "When do honeybees lay their eggs?", "options": ["January to March", "October to December", "April to June", "July to September"], "correct_index": 1}},
            {"type": "true_false", "content": {"question": "Every beehive has one Queen Bee that lays eggs.", "answer": "True"}},
            {"type": "true_false", "content": {"question": "Worker bees do not play an important role in the hive.", "answer": "False"}},
            {"type": "fill_blank", "content": {"question": "Anita started ________ to collect money for her studies.", "answer": "teaching young children"}},
            {"type": "fill_blank", "content": {"question": "Bees are attracted to ________ flowers.", "answer": "Litchi"}},
            {"type": "short_note", "content": {"question": "What work do the worker bees do?", "answer": "Worker bees build the hive, look after the baby bees, and fly around flowers in search of nectar to make honey."}},
            {"type": "short_note", "content": {"question": "Why did Anita want to become a wholesaler?", "answer": "She wanted to become a wholesaler so she could help the villagers get the right price for their honey."}}
        ]}
    },
    "maths": {
        1: {"title": "Building with Bricks", "qs": [
            {"type": "quiz", "content": {"question": "How many faces does a normal brick have?", "options": ["4", "5", "6", "8"], "correct_index": 2}},
            {"type": "quiz", "content": {"question": "Which of these shapes is a face of a brick?", "options": ["Circle", "Triangle", "Rectangle", "Hexagon"], "correct_index": 2}},
            {"type": "true_false", "content": {"question": "A brick has curved edges.", "answer": "False"}},
            {"type": "true_false", "content": {"question": "One lakh has five zeros in it.", "answer": "True"}},
            {"type": "fill_blank", "content": {"question": "A normal brick is a ________ dimensional shape.", "answer": "three"}},
            {"type": "fill_blank", "content": {"question": "To make a strong wall, bricks should be placed so that their joints overlap. Such patterns are called brick ________.", "answer": "patterns"}},
            {"type": "short_note", "content": {"question": "If a brick costs Rs. 5, what will be the cost of 500 bricks?", "answer": "Cost of one brick = Rs. 5. Cost of 500 bricks = 500 * 5 = Rs. 2500."}},
            {"type": "short_note", "content": {"question": "Draw or describe the longest face of a brick.", "answer": "The longest face of a brick is a rectangle. It represents the top or bottom of the brick."}}
        ]},
        2: {"title": "Long and Short", "qs": [
            {"type": "quiz", "content": {"question": "How many centimetres make one metre?", "options": ["10", "100", "1000", "10000"], "correct_index": 1}},
            {"type": "quiz", "content": {"question": "Which unit is best for measuring the distance between two cities?", "options": ["Millimetre", "Centimetre", "Metre", "Kilometre"], "correct_index": 3}},
            {"type": "true_false", "content": {"question": "The length of a pencil is usually measured in kilometres.", "answer": "False"}},
            {"type": "true_false", "content": {"question": "1 km is equal to 1000 metres.", "answer": "True"}},
            {"type": "fill_blank", "content": {"question": "To measure the length of a classroom, you would use ________ as the unit.", "answer": "metres"}},
            {"type": "fill_blank", "content": {"question": "If someone is 1 m 50 cm tall, their height in centimetres is ________ cm.", "answer": "150"}},
            {"type": "short_note", "content": {"question": "Raju is 120 cm tall. His brother is 150 cm tall. Who is taller and by how much?", "answer": "Raju's brother is taller by 150 - 120 = 30 cm."}},
            {"type": "short_note", "content": {"question": "Explain how to convert metres into centimetres with an example.", "answer": "To convert metres to centimetres, multiply the number of metres by 100. For example, 3 metres = 3 x 100 = 300 cm."}}
        ]},
        3: {"title": "A Trip to Bhopal", "qs": [
            {"type": "quiz", "content": {"question": "If 1 bus can carry 50 children, how many children can 4 buses carry?", "options": ["150", "200", "250", "300"], "correct_index": 1}},
            {"type": "quiz", "content": {"question": "A boat ticket costs Rs 30. How much will it cost for 5 children?", "options": ["Rs 100", "Rs 150", "Rs 200", "Rs 250"], "correct_index": 1}},
            {"type": "true_false", "content": {"question": "Bhimbetka is famous for its cave paintings.", "answer": "True"}},
            {"type": "true_false", "content": {"question": "If you start at 9:00 AM and travel for 2 hours, you will reach at 10:00 AM.", "answer": "False"}},
            {"type": "fill_blank", "content": {"question": "If one litre of diesel costs Rs 100, then 50 litres will cost Rs ________.", "answer": "5000"}},
            {"type": "fill_blank", "content": {"question": "There are 210 children going on a trip. If each child gets 1 orange, ________ oranges are needed.", "answer": "210"}},
            {"type": "short_note", "content": {"question": "What is the total time spent if the students spend 1 hour in the caves and 45 minutes travelling back?", "answer": "Total time = 1 hour + 45 minutes = 1 hour 45 minutes."}},
            {"type": "short_note", "content": {"question": "Raman has Rs 100. He buys a toy for Rs 45 and a snack for Rs 20. How much money is left?", "answer": "Total spent = 45 + 20 = 65. Money left = 100 - 65 = Rs 35."}}
        ]},
        4: {"title": "Tick-Tick-Tick", "qs": [
            {"type": "quiz", "content": {"question": "How many minutes are there in one hour?", "options": ["24", "30", "60", "120"], "correct_index": 2}},
            {"type": "quiz", "content": {"question": "What time is it when the hour hand is on 3 and the minute hand is on 12?", "options": ["12:15", "3:00", "3:30", "12:03"], "correct_index": 1}},
            {"type": "true_false", "content": {"question": "A leap year has 366 days.", "answer": "True"}},
            {"type": "true_false", "content": {"question": "The minute hand moves faster than the second hand.", "answer": "False"}},
            {"type": "fill_blank", "content": {"question": "There are ________ hours in one day.", "answer": "24"}},
            {"type": "fill_blank", "content": {"question": "Half past four can be written as ________.", "answer": "4:30"}},
            {"type": "short_note", "content": {"question": "How do you calculate the number of days from 15th May to 25th May?", "answer": "Count the days: 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25. That is 11 days."}},
            {"type": "short_note", "content": {"question": "Explain the difference between a 12-hour clock and a 24-hour clock.", "answer": "A 12-hour clock uses AM and PM to distinguish between morning and night, while a 24-hour clock runs continuously from 00:00 to 23:59."}}
        ]},
        5: {"title": "The Way The World Looks", "qs": [
            {"type": "quiz", "content": {"question": "How does a railway track look from top down?", "options": ["Wider near you and narrower far away", "Parallel lines with sleepers", "Like a circle", "Like a triangle"], "correct_index": 1}},
            {"type": "quiz", "content": {"question": "What does a cube look like from the front?", "options": ["A square", "A circle", "A triangle", "A rectangle"], "correct_index": 0}},
            {"type": "true_false", "content": {"question": "Objects look smaller when viewed from far away.", "answer": "True"}},
            {"type": "true_false", "content": {"question": "A map of a room shows exactly how tall the walls are.", "answer": "False"}},
            {"type": "fill_blank", "content": {"question": "Looking down from above is called a ________ view.", "answer": "top"}},
            {"type": "fill_blank", "content": {"question": "A ball looks like a ________ from every angle.", "answer": "circle"}},
            {"type": "short_note", "content": {"question": "Why do things look different when viewed from the side compared to the top?", "answer": "Because we see different faces of a 3D object from different angles, which changes the outline and visible features."}},
            {"type": "short_note", "content": {"question": "Describe how Gappu the mouse saw the room differently from the ceiling.", "answer": "From the ceiling, Gappu saw the top of the fan, the bed, and the bowls, which looked flat and different from his usual view on the floor."}}
        ]}
    },
    "english": {
        1: {"title": "Wake Up!", "qs": [
            {"type": "quiz", "content": {"question": "Who is asking the child to wake up in the poem 'Wake Up!'?", "options": ["The poet", "The sun and birds", "The mother", "The teacher"], "correct_index": 1}},
            {"type": "quiz", "content": {"question": "In 'Neha's Alarm Clock', at what time does the alarm ring every morning?", "options": ["5 o'clock", "6 o'clock", "7 o'clock", "8 o'clock"], "correct_index": 1}},
            {"type": "true_false", "content": {"question": "The birds are singing in the trees in the poem 'Wake Up!'.", "answer": "True"}},
            {"type": "true_false", "content": {"question": "Neha loves waking up early in the morning.", "answer": "False"}},
            {"type": "fill_blank", "content": {"question": "According to the poem 'Wake Up!', it is too late to lie in ________.", "answer": "bed"}},
            {"type": "fill_blank", "content": {"question": "The big bright ________ fills Neha's room with light.", "answer": "Sun"}},
            {"type": "short_note", "content": {"question": "Why does Neha not want to wake up in the morning?", "answer": "Neha wants to sleep longer and finds it annoying when the alarm clock rings, birds chirp, or the sun shines brightly to wake her up."}},
            {"type": "short_note", "content": {"question": "Who finally wakes Neha up when her alarm, birds, and sun fail?", "answer": "Neha wakes up on her own because her body clock tells her it is time to wake up."}}
        ]},
        2: {"title": "Noses", "qs": [
            {"type": "quiz", "content": {"question": "In the poem 'Noses', what does the child think her nose is?", "options": ["Beautiful", "The funniest thing", "Ugly", "Too small"], "correct_index": 1}},
            {"type": "quiz", "content": {"question": "In 'The Little Fir Tree', who granted wishes to the fir tree?", "options": ["A fairy", "Shetty the magician", "A little boy", "The wind"], "correct_index": 1}},
            {"type": "true_false", "content": {"question": "The child in 'Noses' sees her nose in the mirror.", "answer": "True"}},
            {"type": "true_false", "content": {"question": "The little fir tree was happy with its needle-like leaves in the beginning.", "answer": "False"}},
            {"type": "fill_blank", "content": {"question": "The nose sticks right out where all of it ________.", "answer": "shows"}},
            {"type": "fill_blank", "content": {"question": "The little fir tree wanted ________ leaves like its friends.", "answer": "green"}},
            {"type": "short_note", "content": {"question": "What happened when the fir tree got glass leaves?", "answer": "The wind blew strongly at night, and all the glass leaves were broken."}},
            {"type": "short_note", "content": {"question": "Why did the fir tree finally want its old needle-like leaves back?", "answer": "Because goats ate green leaves, a thief stole gold leaves, and wind broke glass leaves. Its needle leaves were safe."}}
        ]},
        3: {"title": "Run!", "qs": [
            {"type": "quiz", "content": {"question": "Where does the poet want you to run in the poem 'Run!'?", "options": ["Away from the city", "To the school", "Into the house", "To the market"], "correct_index": 0}},
            {"type": "quiz", "content": {"question": "What was Nasruddin boasting about?", "options": ["His running", "His singing", "His skill in archery", "His dancing"], "correct_index": 2}},
            {"type": "true_false", "content": {"question": "The poet asks the child to run and be merry all through the day.", "answer": "True"}},
            {"type": "true_false", "content": {"question": "Nasruddin hit the target on his very first try.", "answer": "False"}},
            {"type": "fill_blank", "content": {"question": "Run down the hillside, run up the ________.", "answer": "lane"}},
            {"type": "fill_blank", "content": {"question": "When Nasruddin's arrow missed the target, he said it was ________'s aim.", "answer": "Azad"}},
            {"type": "short_note", "content": {"question": "Why did Nasruddin take someone else's name each time he missed the target?", "answer": "To hide his failure and save himself from embarrassment, he blamed the missed shots on others."}},
            {"type": "short_note", "content": {"question": "What does the poet mean by 'run in the raindrops'?", "answer": "The poet is asking children to enjoy playing freely outside even when it is raining slightly."}}
        ]},
        4: {"title": "Why?", "qs": [
            {"type": "quiz", "content": {"question": "What kind of a boy is described in the poem 'Why?'?", "options": ["Sleepy", "Curious", "Angry", "Sad"], "correct_index": 1}},
            {"type": "quiz", "content": {"question": "In 'Alice in Wonderland', what color were the rabbit's eyes?", "options": ["Black", "Blue", "Pink", "Red"], "correct_index": 2}},
            {"type": "true_false", "content": {"question": "The curious boy always asks 'Why?' for everything.", "answer": "True"}},
            {"type": "true_false", "content": {"question": "Alice followed a cat into a hole.", "answer": "False"}},
            {"type": "fill_blank", "content": {"question": "He wants to know why ________ and marble sink.", "answer": "lead"}},
            {"type": "fill_blank", "content": {"question": "The rabbit took a ________ out of his waistcoat pocket.", "answer": "watch"}},
            {"type": "short_note", "content": {"question": "What strange things did Alice see in Wonderland?", "answer": "She saw a very small door, a glass table with a golden key, and a beautiful garden with bright flowers."}},
            {"type": "short_note", "content": {"question": "Give an example of a question the boy asks in the poem 'Why?'.", "answer": "He asks why wood should swim and lead and marble sink."}}
        ]},
        5: {"title": "Don't be Afraid of the Dark", "qs": [
            {"type": "quiz", "content": {"question": "Who wrote the poem 'Don't be Afraid of the Dark'?", "options": ["Ruskin Bond", "Enid Blyton", "Roald Dahl", "Rabindranath Tagore"], "correct_index": 0}},
            {"type": "quiz", "content": {"question": "How did Helen Keller communicate later in life?", "options": ["By crying", "Through sign language", "By shouting", "She never communicated"], "correct_index": 1}},
            {"type": "true_false", "content": {"question": "The earth must rest when the day is done.", "answer": "True"}},
            {"type": "true_false", "content": {"question": "Helen Keller could hear but could not see.", "answer": "False"}},
            {"type": "fill_blank", "content": {"question": "The ________ is never harsh, but the sun can be.", "answer": "moonlight"}},
            {"type": "fill_blank", "content": {"question": "Helen Keller's teacher was Miss ________.", "answer": "Sullivan"}},
            {"type": "short_note", "content": {"question": "Why does the poet say we should not be afraid of the dark?", "answer": "Because the earth needs to rest, and the stars will shine forever in the night sky as friends."}},
            {"type": "short_note", "content": {"question": "How did Miss Sullivan help Helen Keller?", "answer": "She spelled words into Helen's hand to help her understand that every object had a name, teaching her how to communicate."}}
        ]}
    },
    "hindi": {
        1: {"title": "Man ke Bhole Bhale Badal", "qs": [
            {"type": "quiz", "content": {"question": "बादल कैसे बालों वाले हैं?", "options": ["सीधे", "झब्बर-झब्बर", "छोटे", "घुंघराले"], "correct_index": 1}},
            {"type": "quiz", "content": {"question": "बादल आसमान में क्या कर रहे हैं?", "options": ["सो रहे हैं", "दौड़ लगा रहे हैं", "रो रहे हैं", "गाना गा रहे हैं"], "correct_index": 1}},
            {"type": "true_false", "content": {"question": "कविता में बादलों को जोकर जैसा भी कहा गया है।", "answer": "True"}},
            {"type": "true_false", "content": {"question": "सारे बादल बहुत शांत और अच्छे हैं, वे कभी शैतानी नहीं करते।", "answer": "False"}},
            {"type": "fill_blank", "content": {"question": "कुछ बादल ________ से सूंड उठाए हुए हैं।", "answer": "हाथी"}},
            {"type": "fill_blank", "content": {"question": "रह-रह कर ________ पर आ जाते।", "answer": "छत"}},
            {"type": "short_note", "content": {"question": "बादल नदी-नालों में बाढ़ कैसे लाते हैं?", "answer": "जब बादल बहुत तेज़ और लगातार बारिश करते हैं, तो सारा पानी नदी-नालों में भर जाता है और बाढ़ आ जाती है।"}},
            {"type": "short_note", "content": {"question": "कवि ने बादलों को किन-किन रूपों में देखा है?", "answer": "कवि ने बादलों को जोकर, हाथी, ऊंट, और परियों जैसे रूपों में देखा है।"}}
        ]},
        2: {"title": "Jaisa Sawal Waisa Jawab", "qs": [
            {"type": "quiz", "content": {"question": "बादशाह अकबर के सबसे चतुर मंत्री कौन थे?", "options": ["बीरबल", "तानसेन", "टोडरमल", "ख्वाजा सरा"], "correct_index": 0}},
            {"type": "quiz", "content": {"question": "ख्वाजा सरा बीरबल को क्या समझते थे?", "options": ["अपना दोस्त", "सबसे बुद्धिमान", "मूर्ख और बच्चा", "गुरु"], "correct_index": 2}},
            {"type": "true_false", "content": {"question": "ख्वाजा सरा ने बीरबल से पाँच सवाल पूछे थे।", "answer": "False"}},
            {"type": "true_false", "content": {"question": "बीरबल ने हर सवाल का बहुत ही चतुराई से जवाब दिया।", "answer": "True"}},
            {"type": "fill_blank", "content": {"question": "आसमान में जितने ________ हैं, सिर पर उतने ही बाल हैं।", "answer": "तारे"}},
            {"type": "fill_blank", "content": {"question": "संसार की आबादी पल-पल ________ और घटती रहती है।", "answer": "बढ़ती"}},
            {"type": "short_note", "content": {"question": "ख्वाजा सरा का पहला सवाल क्या था?", "answer": "ख्वाजा सरा का पहला सवाल था कि संसार का केंद्र (बीच की जगह) कहाँ है?"}},
            {"type": "short_note", "content": {"question": "बीरबल ने संसार की आबादी के सवाल का क्या जवाब दिया?", "answer": "बीरबल ने कहा कि संसार की आबादी पल-पल घटती और बढ़ती रहती है। अगर सभी लोगों को एक जगह इकट्ठा किया जाए तभी गिन कर सही संख्या बताई जा सकती है।"}}
        ]},
        3: {"title": "Kirmich ki Gend", "qs": [
            {"type": "quiz", "content": {"question": "दिनेश को दोपहर में क्या मिला?", "options": ["किताब", "बल्ला", "किरमिच की गेंद", "खिलौना"], "correct_index": 2}},
            {"type": "quiz", "content": {"question": "किसने कहा कि वह गेंद उसकी है?", "options": ["सुधीर", "अनिल", "दीपक", "उपरोक्त सभी ने"], "correct_index": 3}},
            {"type": "true_false", "content": {"question": "गेंद एकदम नई थी।", "answer": "True"}},
            {"type": "true_false", "content": {"question": "दिनेश ने गेंद अपने पास छिपा कर रख ली।", "answer": "False"}},
            {"type": "fill_blank", "content": {"question": "गेंद आकर एक ________ के पेड़ के नीचे गिरी।", "answer": "सीताफल"}},
            {"type": "fill_blank", "content": {"question": "अंत में गेंद एक ________ वाले की टोकरी में जा गिरी।", "answer": "स्कूटर"}},
            {"type": "short_note", "content": {"question": "दीपक अपनी गेंद की पहचान क्या बता रहा था?", "answer": "दीपक कह रहा था कि उसकी गेंद पर लाल रंग का निशान था, जो हर गेंद पर होता है।"}},
            {"type": "short_note", "content": {"question": "गेंद का फैसला कैसे हुआ?", "answer": "जब सभी बच्चे गेंद के लिए लड़ रहे थे, तभी स्कूटर चला गया और गेंद स्कूटर के साथ चली गई।"}}
        ]},
        4: {"title": "Papa Jab Bachche The", "qs": [
            {"type": "quiz", "content": {"question": "पापा बचपन में सबसे पहले क्या बनना चाहते थे?", "options": ["आइसक्रीम वाला", "शंटिंग करने वाला", "चौकीदार", "कुत्ता"], "correct_index": 2}},
            {"type": "quiz", "content": {"question": "पापा आइसक्रीम वाला क्यों बनना चाहते थे?", "options": ["मुफ्त में आइसक्रीम खाने吃 के लिए", "पैसे कमाने के लिए", "घूमने के लिए", "दोस्तों को देने के लिए"], "correct_index": 0}},
            {"type": "true_false", "content": {"question": "पापा अंत में एक इंसान बनना चाहते थे।", "answer": "True"}},
            {"type": "true_false", "content": {"question": "पापा कुत्ता बनकर भौंकना सीख गए थे।", "answer": "True"}},
            {"type": "fill_blank", "content": {"question": "पापा ने तय किया कि वह स्टेशन पर ________ करेंगे।", "answer": "शंटिंग"}},
            {"type": "fill_blank", "content": {"question": "एक ________ अफसर ने पापा को इंसान बनने की सीख दी।", "answer": "फौजी"}},
            {"type": "short_note", "content": {"question": "पापा ने कुत्ता बनने के लिए क्या-क्या किया?", "answer": "पापा चारों पैरों पर चलने लगे, अजनबियों पर भौंकने लगे और कान खुजाना सीखने लगे।"}},
            {"type": "short_note", "content": {"question": "अंत में पापा ने क्या बनने का निश्चय किया और क्यों?", "answer": "अंत में पापा ने एक अच्छा इंसान बनने का निश्चय किया क्योंकि फौजी अफसर की बात से उन्हें समझ आ गया था कि सबसे जरूरी है एक अच्छा इंसान होना।"}}
        ]},
        5: {"title": "Dost ki Poshak", "qs": [
            {"type": "quiz", "content": {"question": "नसीरुद्दीन अपने किस दोस्त से मिले?", "options": ["जमाल साहब", "कमाल साहब", "रोशन साहब", "रहीम साहब"], "correct_index": 0}},
            {"type": "quiz", "content": {"question": "जमाल साहब बाहर क्यों नहीं जाना चाहते थे?", "options": ["क्योंकि वे बीमार थे", "क्योंकि उनकी पोशाक पुरानी थी", "क्योंकि उन्हें डर लग रहा था", "क्योंकि उन्हें नींद आ रही थी"], "correct_index": 1}},
            {"type": "true_false", "content": {"question": "नसीरुद्दीन ने जमाल साहब को अपनी एक भड़कीली अचकन दी।", "answer": "True"}},
            {"type": "true_false", "content": {"question": "पड़ोसी से मिलते समय नसीरुद्दीन ने कहा कि यह अचकन जमाल साहब की ही है।", "answer": "False"}},
            {"type": "fill_blank", "content": {"question": "जमाल साहब को अपनी साधारण सी ________ में बाहर जाने में शर्म आ रही थी।", "answer": "पोशाक"}},
            {"type": "fill_blank", "content": {"question": "नसीरुद्दीन की बातों से जमाल साहब बहुत ________ हुए।", "answer": "नाराज़"}},
            {"type": "short_note", "content": {"question": "पहले पड़ोसी से मिलकर नसीरुद्दीन ने अचकन के बारे में क्या कहा?", "answer": "उन्होंने कहा कि यह मेरे बहुत पुराने दोस्त हैं और इन्होंने जो अचकन पहनी है वह मेरी है।"}},
            {"type": "short_note", "content": {"question": "जमाल साहब क्यों नाराज़ हो रहे थे?", "answer": "क्योंकि नसीरुद्दीन बार-बार लोगों को बता रहे थे कि अचकन किसकी है, जिससे जमाल साहब का अपमान हो रहा था।"}}
        ]}
    }
}

for sub, chapters in content.items():
    for ch_num, ch_data in chapters.items():
        blocks = []
        for q in ch_data['qs']:
            blocks.append(q)
        
        module = create_module(sub, 4, ch_num, ch_data['title'], blocks)
        data[module['metadata']['id']] = module

out_path = '/home/ubuntu/.gemini/antigravity/brain/fec251e7-56c6-4b62-97ea-fb1fb0fb087d/scratch/class4_curriculum.json'
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"File successfully created at {out_path}!")
