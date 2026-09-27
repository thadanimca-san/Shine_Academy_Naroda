import json
import os

def generate_full_english_sup_ch2():
    chapter_id = "ncert_class10_english_sup_ch2"
    title = "Chapter 2: The Thief's Story (Footprints without Feet)"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "Interactive Full-Text Reading",
        "subject": "English Supplementary",
        "grade": "10",
        "board": "NCERT/CBSE",
        "curriculum": ["Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 120,
        "version": "4.0.0-FULL-TEXT",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": ["english", "footprints_without_feet", "thiefs_story", "full_text", "ruskin_bond", "bilingual"],
        "learning_outcomes": [
            "Read and comprehend the original unabridged NCERT text by Ruskin Bond.",
            "Understand the profound psychological themes of trust, guilt, compassion, and transformation.",
            "Master difficult vocabulary contextually with inline Hindi and Gujarati translations.",
            "Analyze character dynamics between Hari Singh and Anil for Board Exam long-answer questions."
        ],
        "ai_context": {
            "learning_goal": "Provide the exact NCERT text broken into passages, with inline translations using backticks for the Smart Translation Filter."
        }
    }
    
    blocks = [
        {
            "type": "hook",
            "content": "Can unconditional trust and kindness reform a thief more effectively than police and prison? Imagine you are a 15-year-old seasoned thief whose entire survival depends on lies and deception. You meet a struggling writer named Anil who has no wealth, but offers you his complete trust, shelter, and education. When you steal all his hard-earned savings and have a chance to escape forever, something stops you at the train station.\n\nLet's read Ruskin Bond's *original, unabridged masterpiece* line-by-line with inline translations `(हिंदी / ગુજરાતી અનુવાદ)` to experience this unforgettable journey of human conscience.",
            "difficulty": "Beginner",
            "bloom": "Understand"
        },
        {
            "type": "diagram",
            "content": "Hari Singh watching Anil at a wrestling match, planning how to win his trust.",
            "image_url": "assets/images/eng_sup_ch2_wrestling_match.jpg",
            "alt_text": "A 15-year-old boy observing a young man at a wrestling match."
        },
        {
            "type": "theory",
            "title": "Passage 1: Meeting Anil and The Approach",
            "content": "I was still a thief when I met Anil. And though only 15, I was an experienced `(अनुभवी / અનુભવી)` and fairly successful hand. Anil was watching a wrestling match when I approached him. He was about 25—a tall, lean fellow—and he looked easy-going `(शांत स्वभाव का / શાંત અને નિરાંતવાળો)`, kind and simple enough for my purpose. I hadn't had much luck of late and thought I might be able to get into the young man's confidence.\n\n\"You look a bit of a wrestler yourself,\" I said. A little flattery `(चापलूसी / ખુશામત)` helps in making friends.\n\n\"So do you,\" he replied, which put me off for a moment because at that time I was rather thin.\n\n\"Well,\" I said modestly `(विनम्रता से / નમ્રતાપૂર્વક)`, \"I do wrestle a bit.\"\n\n\"What's your name?\"\n\n\"Hari Singh,\" I lied. I took a new name every month. That kept me ahead of the police and my former employers `(पुराने मालिक / ભૂતપૂર્વ નોકરીદાતાઓ)`.\n\nAfter this introduction, Anil talked about the well-oiled wrestlers who were grunting `(गुर्रा रहे थे / ઘૂરકિયાં કરતા હતા)`, lifting and throwing each other about. I didn't have much to say. Anil walked away. I followed casually `(लापरवाही से / સહજતાથી)`.\n\n\"Hello again,\" he said.\n\nI gave him my most appealing `(आकर्षक / આકર્ષક)` smile. \"I want to work for you,\" I said.\n\n\"But I can't pay you.\"\n\nI thought that over for a minute. Perhaps I had misjudged `(गलत आंकलन किया / ખોટો અંદાજ લગાવ્યો)` my man. I asked, \"Can you feed me?\"\n\n\"Can you cook?\"\n\n\"I can cook,\" I lied again.\n\n\"If you can cook, then maybe I can feed you.\"",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Teacher's Insight:** Notice Hari Singh's survival tactics: he changes his name every month to dodge the police, uses deliberate flattery to disarm strangers, and lies about knowing how to cook. At 15, he is street-smart and calculating, viewing every person as a potential mark."
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Why did the narrator take a new name every month?",
                "options": [
                    "Because he forgot his real name",
                    "To stay ahead of the police and former employers",
                    "Because he liked trying out different names",
                    "To impress his new friends"
                ],
                "correct_answer": "To stay ahead of the police and former employers",
                "explanation": "Hari Singh was a seasoned thief who changed his identity every month to prevent the police and past victims from tracking him down."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 2: Life with Anil and The Gift of Education",
            "content": "He took me to his room over the Jumna Sweet Shop and told me I could sleep on the balcony `(बालकनी / બાલ્કની)`. But the meal I cooked that night must have been terrible `(भयानक / ભયાનક)` because Anil gave it to a stray dog `(आवारा कुत्ता / રખડતો કૂતરો)` and told me to be off, but I just hung around, smiling in my most appealing `(आकर्षक / આકર્ષક)` way, and he couldn't help laughing.\n\nLater, he patted `(थपथपाया / પીઠ થાબડી)` me on the head and said never mind, he'd teach me to cook. He also taught me to write my name and said he would soon teach me to write whole sentences `(पूरे वाक्य / આખા વાક્યો)` and to add numbers.\n\nI was grateful `(कृतज्ञ / આભારી)`. I knew that once I could write like an educated `(शिक्षित / શિક્ષિત)` man there would be no limit to what I could achieve.\n\nIt was quite pleasant `(सुखद / સુખદ)` working for Anil. I made the tea in the morning and then would take my time buying the day's supplies `(दैनिक राशन / રોજિંદો સામાન)`, usually making a profit of about a rupee a day. I think he knew I made a little money this way but he did not seem to mind.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Literary Significance:** Anil's promise to teach Hari to write whole sentences is the turning point of Hari's life. Hari recognizes that literacy and education can offer him respect and endless possibilities, unlike the risky, temporary gains of petty theft."
        },
        {
            "type": "theory",
            "title": "Passage 3: Anil's Carefree Income and The Temptation",
            "content": "Anil made money by fits and starts `(अनियमित रूप से / અનિયમિત રીતે)`. He would borrow one week, lend the next. He kept worrying about his next cheque, but as soon as it arrived he would go out and celebrate `(जश्न मनाना / ઉજવણી કરવી)`. It seemed he wrote for magazines—a queer `(अजीब / વિચિત્ર)` way to make a living!\n\nOne evening he came home with a small bundle of notes, saying he had just sold a book to a publisher `(प्रकाशक / પ્રકાશક)`. At night, I saw him tuck `(दबाकर रखना / સરકાવીને મૂકવું)` the money under the mattress `(गद्दा / ગાદલું)`.\n\nI had been working for Anil for almost a month and, apart from cheating on the shopping, had not done anything in my line of work. I had every opportunity for doing so. Anil had given me a key to the door, and I could come and go as I pleased. He was the most trusting `(भरोसेमंद / વિશ્વાસુ)` person I had ever met.\n\nAnd that is why it was so difficult to rob him. It's easy to rob a greedy `(लालची / લાલચુ)` man, because he can afford to be robbed; but it's difficult to rob a careless `(लापरवाह / બેદરકાર)` man—sometimes he doesn't even notice he's been robbed and that takes all the pleasure out of the work.\n\n\"Well, it's time I did some real work,\" I told myself; \"I'm out of practice `(अभ्यास छूट गया है / પ્રેક્ટિસ છૂટી ગઈ છે)`. And if I don't take the money, he'll only waste it on his friends. After all, he doesn't even pay me.\"",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Why did Hari Singh find it difficult to rob a careless and trusting person like Anil?",
                "options": [
                    "Because careless men keep their money in heavy safes",
                    "Because they might not even notice the theft, taking away the satisfaction and thrill of the crime",
                    "Because Anil had a watchdog guarding the room",
                    "Because Hari was afraid of Anil's physical strength"
                ],
                "correct_answer": "Because they might not even notice the theft, taking away the satisfaction and thrill of the crime",
                "explanation": "Hari explains that robbing a greedy man is easy because he deserves it and feels the loss, but a trusting, careless man may not even notice, which robs the thief of any pleasure."
            },
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "theory",
            "title": "Passage 4: The Midnight Theft",
            "content": "Anil was asleep. A beam of moonlight `(चांदनी की किरण / ચંદ્રપ્રકાશનું કિરણ)` stepped over the balcony and fell on the bed. I sat up on the floor, considering `(विचार करते हुए / વિચારતાં)` the situation. If I took the money, I could catch the 10.30 Express to Lucknow.\n\nSlipping out of the blanket, I crept `(रेंगते हुए आगे बढ़ा / ધીમેથી સરક્યો)` up to the bed. Anil was sleeping peacefully `(शांतिपूर्वक / શાંતિથી)`. His face was clear and unlined `(बिना झुर्रियों वाला / કરચલીઓ વગરનું)`; even I had more marks on my face, though mine were mostly scars `(घाव के निशान / ઘાના ડાઘ)`.\n\nMy hand slid under the mattress, searching for the notes. When I found them, I drew them out without a sound `(बिना किसी आवाज़ के / અવાજ કર્યા વગર)`. Anil sighed `(आह भरी / નિસાસો નાખ્યો)` in his sleep and turned on his side, towards me.\n\nI was startled `(चौंक गया / ચોંકી ગયો)` and quickly crawled `(घिसटते हुए / પેટે સરકીને)` out of the room.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "diagram",
            "content": "Hari Singh drawing the bundle of notes from under the mattress as moonlight enters the room.",
            "image_url": "assets/images/eng_sup_ch2_theft_moonlight.jpg",
            "alt_text": "A boy taking money from under a sleeping man's mattress."
        },
        {
            "type": "theory",
            "title": "Passage 5: The Railway Station and The Unexplained Hesitation",
            "content": "When I was on the road, I began to run. I had the notes at my waist, held there by the string of my pyjamas. I slowed down to a walk and counted the notes: 600 rupees in fifties! I could live like an oil-rich Arab `(तेल का अमीर अरब व्यापारी / તેલનો અમીર આરબ વેપારી)` for a week or two.\n\nWhen I reached the station, I did not stop at the ticket office (I had never bought a ticket in my life) but dashed straight to the platform. The Lucknow Express was just moving out. The train had still to pick up speed and I should have been able to jump into one of the carriages `(डिब्बे / ડબ્બા)`, but I hesitated `(हिचकिचाया / અચકાયો)`—for some reason I can't explain—and I lost the chance to get away.\n\nWhen the train had gone, I found myself standing alone on the deserted `(सूनसान / નિર્જન)` platform. I had no idea where to spend the night. I had no friends, believing that friends were more trouble than help. And I did not want to make anyone curious `(उत्सुक / જિજ્ઞાસુ)` by staying at one of the small hotels near the station. The only person I knew really well was the man I had robbed.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Psychological Nuance:** Why did Hari hesitate to board the moving train? His subconscious conscience was already awakening. Anil's pure trust had planted a moral anchor in Hari's heart that held him back from running away."
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "How much money did Hari Singh steal from under Anil's mattress?",
                "options": [
                    "100 rupees in tens",
                    "600 rupees in fifties",
                    "500 rupees in hundreds",
                    "1000 rupees in twenties"
                ],
                "correct_answer": "600 rupees in fifties",
                "explanation": "Hari counted the notes on the road and found there were 600 rupees in fifty-rupee notes."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 6: A Study of Men's Faces",
            "content": "Leaving the station, I walked slowly through the bazaar `(बाजार / બજાર)`.\n\nIn my short career as a thief, I had made a study of men's faces when they had lost their goods. The greedy man showed fear `(डर / ડર)`; the rich man showed anger `(क्रोध / ગુસ્સો)`; the poor man showed acceptance `(स्वीकृति / સ્વીકાર)`.\n\nBut I knew that Anil's face, when he discovered the theft, would show only a touch of sadness `(उदासी / ઉદાસી)`. Not for the loss of money, but for the loss of trust `(विश्वास का टूटना / વિશ્વાસનો ભંગ)`.\n\nI found myself in the maidan `(खुला मैदान / ખુલ્લું મેદાન)` and sat down on a bench. The night was chilly `(ठंडी / ઠંડી)`—it was early November—and a light drizzle `(बूंदाबांदी / ઝરમર વરસાદ)` added to my discomfort `(असुविधा / અગવડતા)`.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "🔥 **Board Exam Key Point:** Memorize the four reactions to loss of goods:\n1. Greedy man → Fear\n2. Rich man → Anger\n3. Poor man → Acceptance\n4. Anil (trusting man) → Sadness for loss of trust (NOT for money)."
        },
        {
            "type": "theory",
            "title": "Passage 7: The Drizzle, The Clock Tower, and The Epiphany",
            "content": "Soon it was pouring heavily. My shirt and pyjamas stuck `(चिपक गए / ચોંટી ગયા)` to my skin, and a cold wind brought the rain across my face.\n\nI went back to the bazaar and sat down in the shelter `(ओट / આશરો)` of the clock tower. The clock showed midnight. I felt for the notes. They were damp `(गीले / ભીના)` from the rain.\n\nAnil's money. In the morning he would probably have given me two or three rupees to go to the cinema, but now I had it all. No more cooking his meals, running to the bazaar or learning to write whole sentences any more!\n\nI had forgotten about them in the excitement `(उत्तेजना / ઉત્તેજના)` of the theft. Whole sentences, I knew, could one day bring me more than a few hundred rupees. It was a simple matter to steal—and sometimes just as simple to be caught. But to be a really big man, a clever and respected `(सम्मानित / પ્રતિષ્ઠિત)` man, was something else.\n\nI should go back to Anil, I told myself, if only to learn to read and write.",
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "What ultimate realization convinced Hari Singh to return to Anil?",
                "options": [
                    "He was afraid of catching pneumonia in the cold rain",
                    "He feared the police would catch him at the clock tower",
                    "He realized that education and learning to write whole sentences could make him a truly respected man",
                    "He wanted to steal even more money from Anil later"
                ],
                "correct_answer": "He realized that education and learning to write whole sentences could make him a truly respected man",
                "explanation": "Hari realized that stealing offers petty, temporary cash, but literacy and education have the power to bring genuine respect, status, and infinite opportunities."
            },
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        },
        {
            "type": "theory",
            "title": "Passage 8: Returning Undetected and The Silent Redemption",
            "content": "I hurried back to the room feeling very nervous `(घबराया हुआ / ગભરાયેલો)`, for it is much easier to steal something than to return it undetected `(बिना पकड़े गए / પકડાયા વિના)`.\n\nI opened the door quietly, then stood in the doorway, in clouded moonlight. Anil was still asleep. I crept to the head of the bed, and my hand came up with the notes. I felt his breath on my hand. I remained still for a minute. Then my hand found the edge of the mattress, and slipped under it with the notes.\n\nI woke late next morning to find that Anil had already made the tea. He stretched out his hand towards me. There was a fifty-rupee note between his fingers. My heart sank `(दिल बैठ गया / હિંમત હારી ગયો)`.\n\n\"I made some money yesterday,\" he explained. \"Now you'll be paid regularly.\"\n\nMy spirits rose `(उत्साह बढ़ गया / ઉત્સાહ વધ્યો)`. But when I took the note, I saw it was still wet from the night's rain.\n\n\"Today we'll start writing sentences,\" he said.\n\nHe knew. But neither his lips nor his eyes showed anything. I smiled at Anil in my most appealing `(आकर्षक / આકર્ષક)` way. And the smile came by itself, without any effort `(प्रयास / પ્રયાસ)`.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "diagram",
            "content": "Anil handing Hari Singh the wet fifty-rupee note with a warm, knowing expression.",
            "image_url": "assets/images/eng_sup_ch2_wet_note.jpg",
            "alt_text": "Anil handing a wet fifty rupee note to Hari Singh in the morning."
        },
        {
            "type": "teacher_tip",
            "content": "💡 **The Climax & The Natural Smile:** At the beginning of the story, Hari Singh's appealing smile was a calculated, artificial mask used to manipulate people. At the end, his smile came *'by itself, without any effort'*—symbolizing authentic redemption, gratitude, and moral rebirth."
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "How did Hari Singh know that Anil was aware of the previous night's theft?",
                "options": [
                    "Anil scolded him and called the police",
                    "The fifty-rupee note Anil handed him in the morning was still damp from the rain",
                    "Anil refused to give him breakfast",
                    "Anil asked him why his pyjamas were soaked"
                ],
                "correct_answer": "The fifty-rupee note Anil handed him in the morning was still damp from the rain",
                "explanation": "The note was wet from the rain of the previous night, showing Anil knew Hari had taken the money out into the storm and returned it, yet chose silent forgiveness."
            },
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "exam_tips",
            "content": "🔥 **BOARD EXAM HIGHEST-WEIGHTAGE QUESTIONS & ANSWERS**\n\n**Q1. Give a character sketch of Anil. What made him different from other employers? (5 Marks)**\n*   **Simple & Easy-going:** Anil is a 25-year-old struggling writer who lives carefree and earns by 'fits and starts'.\n*   **Compassionate & Patient:** When Hari cooks a disastrous meal on day one, Anil feeds it to stray dogs and patiently teaches him how to cook and write.\n*   **Magnanimous & Forgiving:** When he discovers Hari stole and returned the 600 rupees, he does not rebuke or report him. He hands him a wet ₹50 note and promises regular pay, using unconditional love to transform a criminal.\n\n---\n\n**Q2. How did education play a transformative role in Hari Singh's life? (5 Marks)**\n*   Hari realized that stealing is easy and temporary, but learning to read, write, and calculate could make him a respected, big man.\n*   The desire for literacy overpowered his instinct to steal, causing him to miss the Lucknow Express and return the stolen money under the mattress.\n\n---\n\n**Q3. Explain the significance of the title 'The Thief's Story'. (3 Marks)**\n*   The story is narrated directly from the perspective of a 15-year-old thief.\n*   It chronicles not a story of robbery, but the psychological metamorphosis of a thief into an honest human being through trust and kindness.",
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        }
    ]

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_sup_ch2.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_sup_ch2.json"
    final_json["metadata"]["id"] = "gseb_class10_english_sup_ch2"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Full-Text English Supplementary Chapter 2 Generated Successfully!")

if __name__ == "__main__":
    generate_full_english_sup_ch2()
