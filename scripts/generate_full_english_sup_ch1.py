import json
import os

def generate_full_english_sup_ch1():
    chapter_id = "ncert_class10_english_sup_ch1"
    title = "Supplementary Chapter 1: A Triumph of Surgery (Footprints without Feet)"
    
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
        "tags": ["english", "footprints_without_feet", "a_triumph_of_surgery", "full_text", "james_herriot"],
        "learning_outcomes": [
            "Read and comprehend the original NCERT short story 'A Triumph of Surgery' by James Herriot.",
            "Analyze the destructive effects of over-pampering and improper pet care versus natural lifestyle and diet.",
            "Master rich vocabulary and literary devices (irony, humor, satire) with bilingual contextual translations.",
            "Examine character traits of Mrs. Pumphrey and Dr. James Herriot for Board Examination questions."
        ],
        "ai_context": {
            "learning_goal": "Provide the exact NCERT text broken into passages, with inline translations using backticks for the Smart Translation Filter."
        }
    }
    
    blocks = [
        {
            "type": "hook",
            "content": "Imagine loving your pet so much that you feed it cream cakes, chocolates, Horlicks, and wine, until it becomes so fat it looks like a **bloated sausage `(फूला हुआ कबाब / ફૂલેલો સોસેજ)`** unable to walk!\n\nThis is the heartwarming and humorous story of **Tricki**, a pampered dog, and his wealthy, emotional mistress **Mrs. Pumphrey**. When Tricki falls deathly ill from overfeeding, a clever veterinary doctor named **Dr. James Herriot** saves his life without giving him a single dose of medicine!\n\nLet us read the *original, complete NCERT story* line-by-line with rich bilingual translations to discover the true meaning behind 'A Triumph of Surgery'!",
            "difficulty": "Beginner",
            "bloom": "Understand"
        },
        {
            "type": "diagram",
            "content": "Dr. Herriot shocked by Tricki's bloated appearance on the street.",
            "image_url": "assets/images/eng_sup_ch1_fat_tricki.jpg",
            "alt_text": "A very obese dog with bloodshot eyes being walked by a wealthy lady."
        },
        {
            "type": "theory",
            "title": "Passage 1: Tricki's Alarming Condition & Mrs. Pumphrey's Overfeeding",
            "content": "I was really worried about Tricki this time. I had pulled up my car when I saw him in the street with his mistress and I was shocked at his appearance. He had become hugely fat, like a bloated sausage `(फूला हुआ कबाब / ફૂલેલો સોસેજ)` with a leg at each corner. His eyes, bloodshot `(खून जैसी लाल / લોહી જેવી લાલ)` and rheumy `(पानीदार, आंखों से पानी बहता हुआ / પાણી ઝરતી)`, stared straight ahead and his tongue lolled `(लटक रही थी / બહાર લટકતી હતી)` from his jaws.\n\nMrs Pumphrey hastened `(जल्दी से कहा / ઉતાવળે કહ્યું)` to explain: \"He was so listless `(सुस्त, ऊर्जाहीन / અશક્ત, સુસ્ત)`, Mr Herriot. He seemed to have no energy. I thought he must be suffering from malnutrition `(कुपोषण / કુપોષણ)`, so I have been giving him some little extras between meals to build him up, some malt `(जौ का सत्त / જવનો અર્ક)` and cod-liver oil `(मछली का तेल / માછલીનું તેલ)` and a bowl of Horlicks at night to make him sleep — nothing much really.\"\n\n\"And did you cut down on the sweet things as I told you?\"\n\n\"Oh, I did for a bit, but he seemed to be so weak I had to relent `(पिघल जाना, नरम पड़ना / નરમ પડવું)`. He does love cream cakes and chocolates so. I can't bear to refuse him.\"",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Teacher's Insight (Characterization of Mrs. Pumphrey):** Notice the dramatic irony here. Mrs. Pumphrey believes Tricki is suffering from *malnutrition* (lack of nutrition), when in reality he is suffering from severe *over-nutrition*! Her excessive, blind love and pampering are pushing her beloved pet towards fatal illness. Note Herriot's vivid description: 'a bloated sausage with a leg at each corner'."
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Why did Mrs. Pumphrey give Tricki malt, cod-liver oil, and Horlicks between meals?",
                "options": [
                    "Because the vet had prescribed them as daily medicine",
                    "Because she thought he was suffering from malnutrition and lacked energy",
                    "Because Tricki was participating in a dog racing tournament",
                    "Because Tricki refused to drink normal water"
                ],
                "correct_answer": "Because she thought he was suffering from malnutrition and lacked energy",
                "explanation": "Mrs. Pumphrey mistakenly diagnosed Tricki's lethargy as malnutrition and fed him rich extra nutrients to build up his energy."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 2: The Doctor's Stern Warning & The Unheeded Diet",
            "content": "I looked down again at the little dog. That was the trouble. Tricki's only fault was greed `(लालच / લાલચ)`. He had never been known to refuse food; he would tackle a meal at any hour of the day or night. And I wondered about all the things Mrs Pumphrey hadn't mentioned.\n\n\"Are you giving him plenty of exercise?\"\n\n\"Well, he has his little walks with me as you can see, but Hodgkin the gardener has been down with lumbago `(कमर का तेज दर्द / કમરનો સખત દુખાવો)`, so there has been no ring-throwing `(रिंग फेंकने का खेल / રિંગ ફેંકવાની રમત)` lately.\"\n\nI tried to sound severe `(कठोर / કડક)`: \"Now I really mean this. If you don't cut his food right down and give him more exercise he is going to be really ill. You must harden your heart `(दिल कड़ा करना / દિલ કઠણ કરવું)` and keep him on a very strict diet `(सख्त आहार / કડક આહાર)`.\"\n\nMrs Pumphrey wrung `(हाथ मलना, बेचैनी में हाथ मरोड़ना / હાથ મસળવા)` her hands. \"Oh I will, Mr Herriot. I'm sure you are right, but it is so difficult, so very difficult.\" She set off, head down, along the road, as if determined to put the new regime `(नया नियम / નવો નિયમ)` into practice immediately.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Board Exam Insight:** Tricki's main flaw was his uncontrollable **greed** for food. He never refused a meal at any hour. But the primary culprit was Mrs. Pumphrey's inability to say 'no'. Even though Dr. Herriot gave a stern warning, she found it emotionally 'too difficult' to enforce a strict diet."
        },
        {
            "type": "theory",
            "title": "Passage 3: The Crisis & The Decision for Hospitalisation",
            "content": "I watched their progress with growing concern `(चिंता / ચિંતા)`. Tricki was tottering along `(लड़खड़ाते हुए चलना / લથડતાં ચાલવું)` in his little tweed coat `(ऊनी कोट / ઊનનો કોટ)`; he had a whole wardrobe `(अलमारी / કબાટ)` of these coats — for the cold weather and a raincoat for the wet days. He struggled on, drooping `(झुकते हुए / લટકતો)` in his harness `(पट्टा / પટ્ટો)`. I thought it wouldn't be long before I heard from Mrs Pumphrey.\n\nThe expected call came within a few days. Mrs Pumphrey was distraught `(अत्यंत व्याकुल, परेशान / ખૂબ જ વ્યાકુળ)`. Tricki would eat nothing. Refused even his favourite dishes; and besides, he had bouts of vomiting `(उल्टी के दौरे / ઊલટીના હુમલા)`. He spent all his time lying on a rug, panting `(हांफते हुए / હાંફતો)`. Didn't want to go for walks, didn't want to do anything.\n\nI had made my plans in advance. The only way was to get Tricki out of the house for a period. I suggested that he be hospitalised `(अस्पताल में भर्ती / હોસ્પિટલમાં દાખલ)` for about a fortnight `(दो सप्ताह, चौदह दिन / પખવાડિયું, ૧૪ દિવસ)` to be kept under observation `(निगरानी / દેખરેખ)`.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Why did Dr. Herriot decide that Tricki must be hospitalised for a fortnight?",
                "options": [
                    "To perform a dangerous surgical operation on the dog",
                    "Because Tricki could only be cured if separated from Mrs. Pumphrey's constant overfeeding",
                    "To sell Tricki to another wealthy family",
                    "Because his clinic needed more boarding patients"
                ],
                "correct_answer": "Because Tricki could only be cured if separated from Mrs. Pumphrey's constant overfeeding",
                "explanation": "Dr. Herriot knew that as long as Tricki stayed with Mrs. Pumphrey, she would never stop pampering him. Hospitalisation was the only way to control his diet."
            },
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "theory",
            "title": "Passage 4: The Departure & The Mountain of Pet Luxuries",
            "content": "The poor lady almost swooned `(बेहोश हो गई / બેભાન જેવી થઈ ગઈ)`. She was sure he would pine `(तड़पना, विरह में दुखी होना / ઝૂરવું)` and die if he did not see her every day.\n\nBut I took a firm line `(कड़ा रुख अपनाया / કડક વલણ અપનાવ્યું)`. Tricki was very ill and this was the only way to save him; in fact, I thought it best to take him without delay and, followed by Mrs Pumphrey's wailings `(विलाप, रोना-धोना / રુદન, વિલાપ)`, I marched out to the car carrying the little dog wrapped in a blanket.\n\nThe entire staff was roused `(सक्रिय हो गया / દોડધામમાં લાગી ગયો)` and maids rushed in and out bringing his day bed, his night bed, favourite cushions, toys and rubber rings, breakfast bowl, lunch bowl, supper bowl. Realising that my car would never hold all the stuff, I started to drive away. As I moved off, Mrs Pumphrey, with a despairing cry `(निराशा भरी चीख / નિરાશાભરી ચીસ)`, threw an armful of the little coats through the window. I looked in the mirror before I turned the corner of the drive; everybody was in tears `(सबकी आंखों में आंसू थे / બધાની આંખોમાં આંસુ હતા)`.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "diagram",
            "content": "Mrs. Pumphrey and her servants loading Dr. Herriot's car with Tricki's luxurious possessions.",
            "image_url": "assets/images/eng_sup_ch1_car_departure.jpg",
            "alt_text": "A veterinary doctor driving away with a small dog wrapped in a blanket while servants carry beds and bowls."
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Humour and Satire in Herriot's Style:** Observe the gentle British humor and social satire in this scene! The household treats the dog like royalty: day beds, night beds, distinct bowls for every meal, dozens of tweed coats, and rubber toys. The maids and servants are in utter distress as if a prince is leaving for war!"
        },
        {
            "type": "theory",
            "title": "Passage 5: Arrival at the Surgery & The First Days of Fasting",
            "content": "Out on the road, I looked down at the pathetic `(दयनीय / દયનીય)` little animal gasping `(हांफता हुआ / શ્વાસ માટે તરફડતો)` on the seat by my side. I patted the head and Tricki made a brave effort to wag his tail. \"Poor old lad,\" I said, \"you haven't a kick in you `(शरीर में कोई ताकत नहीं बची / શરીરમાં કોઈ જોમ કે શક્તિ નથી)`, but I think I know a cure for you.\"\n\nAt the surgery `(पशु चिकित्सालय / પ્રાણીઓનું દવાખાનું)`, the household dogs surged `(उमड़ पड़े / ધસી આવ્યા)` round me. Tricki looked down at the noisy pack with dull eyes `(उदास, बेजान आंखें / નિસ્તેજ આંખો)` and, when put down, lay motionless `(गतिहीन / સ્થિર, નિશ્ચેષ્ટ)` on the carpet. The other dogs, after sniffing round him for a few seconds, decided he was an uninteresting object `(नीरस वस्तु / રસહીન વસ્તુ)` and ignored him.\n\nI made up a bed for him in a warm loose box next to the one where the other dogs slept. For two days I kept an eye on him, giving him no food but plenty of water `(भरपूर पानी / પુષ્કળ પાણી)`. At the end of the second day he started to show some interest in his surroundings and on the third he began to whimper `(धीमी आवाज में कराहना / ધીમા અવાજે રડવું)` when he heard the dogs in the yard.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "What medical treatment did Dr. Herriot administer to Tricki during his first two days at the surgery?",
                "options": [
                    "Heavy antibiotics and daily surgical injections",
                    "No food at all, but plenty of water and rest",
                    "A liquid diet of warm milk, eggs, and brandy",
                    "Strict electric massage therapy"
                ],
                "correct_answer": "No food at all, but plenty of water and rest",
                "explanation": "Dr. Herriot did not administer any pharmaceutical medicines or perform surgery. He simply gave Tricki zero food and plenty of water for two days to let his bloated digestive system recover."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 6: Joining the Pack & The Joy of Dog Life",
            "content": "When I opened the door, Tricki trotted out `(धीमी चाल से निकला / ધીમી ચાલે બહાર નીકળ્યો)` and was immediately engulfed `(घिर गया / ઘેરાઈ ગયો)` by Joe, the greyhound `(शिकारी कुत्ता / શિકારી કૂતરો)`, and his friends. After rolling him over and thoroughly inspecting him, the dogs moved off down the garden. Tricki followed them, rolling slightly with his surplus fat `(अतिरिक्त चर्बी / વધારાની ચરબી)`.\n\nLater that day, I was present at feeding time. I watched while Tristan slopped `(जल्दी-जल्दी डाला / ઉતાવળે પીરસ્યું)` the food into the bowls. There was the usual headlong rush followed by the sounds of high-speed eating; every dog knew that if he fell behind the others he was liable `(संभावना होना / જોખમ રહેવું)` to have some competition for the last part of his meal.\n\nWhen they had finished, Tricki took a walk round the shining bowls, licking casually `(लापरवाही से चाटना / સહજતાથી ચાટવું)` inside one or two of them. Next day, an extra bowl was put out for him and I was pleased to see him jostling `(धक्का-मुक्की करते हुए / ધક્કામુક્કી કરતો)` his way towards it.\n\nFrom then on, his progress was rapid `(तेज / ઝડપી)`. He had no medicinal treatment of any kind, but all day he ran about with the dogs, joining in their friendly scrimmages `(दोस्ताना छीना-झपटी / મિત્રતાપૂર્ણ ખેંચતાણ)`. He discovered the joys of being bowled over, tramped on `(पैरों तले रौंदे जाना / કચડાવું)` and squashed every few minutes. He became an accepted member of the gang, an unlikely, silky `(रेशमी बालों वाला / રેશમી વાળવાળો)` little object among the shaggy `(झबरे बालों वाला / રુવાંટીવાળો)` crew, fighting like a tiger for his share at mealtimes and hunting rats in the old hen-house at night. He had never had such a time in his life.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Psychological Transformation:** Notice Tricki's lifestyle before and after:\n- **Before:** Lying on a silk cushion, fed cakes and Horlicks, completely inactive, lonely and sick.\n- **After:** Running in the dirt, competing for food, wrestling in friendly scrimmages, hunting rats with the pack, vigorous and full of life!\nPhysical exercise and social play with his peers were the true medicine Tricki needed."
        },
        {
            "type": "theory",
            "title": "Passage 7: The Lavish Gifts & The Doctor's Temptation",
            "content": "All the while, Mrs Pumphrey hovered anxiously `(चिंता में चक्कर काटना / ચિંતામાં આંટા મારવા)` in the background, ringing a dozen times a day for the latest bulletins `(समाचार / સમાચાર)`. I dodged `(टालमटोल करना / ટાળવું)` the questions about whether his cushions were being turned regularly or his correct coat worn according to the weather; but I was able to tell her that the little fellow was out of danger and convalescing `(स्वास्थ्य लाभ कर रहा / સાજો થઈ રહ્યો છે)` rapidly.\n\nThe word 'convalescing' seemed to do something to Mrs Pumphrey. She started to bring round fresh eggs, two dozen at a time, to build up Tricki's strength. For a happy period my partners and I had two eggs each for breakfast. Then the bottles of wine `(शराब / વાઇન)` began to arrive to enrich Tricki's blood. It was then that the real possibilities of the situation began to dawn `(समझ में आना / સમજાવા લાગ્યું)` on the household.\n\nLunch became a ceremonial occasion `(उत्सव जैसा अवसर / ભવ્ય ઉત્સવ પ્રસંગ)` with two glasses of wine before and several during the meal. We could hardly believe it when the brandy `(ब्रांडी / બ્રાન્ડી)` came to put a final edge on Tricki's constitution `(शारीरिक गठन, स्वास्थ्य / શારીરિક બાંધો)`. For a few nights the fine spirit was rolled around, inhaled and reverently `(श्रद्धापूर्वक / આદરપૂર્વક)` drunk.\n\nThey were days of deep content `(परम संतोष / પરમ સંતોષ)`, starting well with the extra egg in the morning, improved and sustained by the midday wine and finishing luxuriously round the fire with the brandy. It was a temptation `(प्रलोभन, लालच / લાલચ)` to keep Tricki on as a permanent guest `(स्थायी मेहमान / કાયમી મહેમાન)`!",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Why was Dr. Herriot tempted to keep Tricki at the surgery as a permanent guest?",
                "options": [
                    "Because Tricki had become his best watch-dog",
                    "Because the surgery staff enjoyed the lavish fresh eggs, wine, and brandy sent by Mrs. Pumphrey",
                    "Because Mrs. Pumphrey refused to pay the veterinary bill",
                    "Because Tricki was suffering from a chronic contagious disease"
                ],
                "correct_answer": "Because the surgery staff enjoyed the lavish fresh eggs, wine, and brandy sent by Mrs. Pumphrey",
                "explanation": "Mrs. Pumphrey sent fresh eggs, fine wine, and brandy to build up Tricki's health. Since Tricki didn't need them, the doctor and his partners enjoyed these luxurious treats every day!"
            },
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "theory",
            "title": "Passage 8: The Grand Reunion & 'A Triumph of Surgery'",
            "content": "But I knew Mrs Pumphrey was suffering and after a fortnight, felt compelled `(विवश होकर / મજબૂર થઈને)` to phone and tell her that the little dog had recovered and was awaiting collection.\n\nWithin minutes, about thirty feet of gleaming `(चमकती हुई / ચમકતી)` black metal drew up outside the surgery. The chauffeur `(कार चालक / ડ્રાઈવર)` opened the door and I could just make out the figure of Mrs Pumphrey almost lost in the interior. Her hands were tightly clasped `(भींचे हुए / દબાયેલા)` in front of her; her lips trembled `(कांप रहे थे / ધ્રૂજતા હતા)`. \"Oh, Mr Herriot, do tell me the truth. Is he really better?\"\n\n\"Yes, he's fine,\" I said. \"There's no need for you to get out of the car — I'll go and fetch him.\"\n\nI walked through the house into the garden. A mass of dogs was hurtling `(तेजी से दौड़ना / પૂરઝડપે દોડવું)` round and round the lawn and in their midst, ears flapping, tail waving, was the little golden figure of Tricki. In two weeks he had been transformed into a lithe `(फुर्तीला और लचीला / ચપળ અને લચીલો)`, hard-muscled animal; he was keeping up well with the pack, stretching out in great bounds, his chest almost brushing the ground.\n\nI carried him back along the passage to the front of the house. The chauffeur was still holding open the car door and when Tricki saw his mistress he took off from my arms in a tremendous leap `(ज़बरदस्त छलांग / જબરદસ્ત કૂદકો)` and sailed into Mrs Pumphrey's lap. She gave a startled \"Ooh!\" and then had to defend herself as he swarmed over her, licking her face and barking.\n\nDuring the excitement, I helped the chauffeur to bring out the beds, toys, cushions, coats and bowls, none of which had been used. As the car moved away, Mrs Pumphrey leaned out of the window. Tears shone in her eyes. Her lips trembled. \"Oh, Mr Herriot,\" she cried, \"how can I ever thank you? This is a **triumph of surgery `(शल्य चिकित्सा की विजय / શસ્ત્રક્રિયાની જીત)`**!\"",
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        },
        {
            "type": "diagram",
            "content": "Tricki leaping joyfully into Mrs. Pumphrey's lap inside the luxury car.",
            "image_url": "assets/images/eng_sup_ch1_tricki_reunion.jpg",
            "alt_text": "A fit and energetic dog jumping excitedly into the lap of his crying, joyful mistress inside a limousine."
        },
        {
            "type": "teacher_tip",
            "content": "💡 **The Master Irony of the Title:**\nWhy is the chapter titled *'A Triumph of Surgery'*?\nIn British English, a 'surgery' is a doctor's clinic/consultation room. But Mrs. Pumphrey thought Tricki was cured through complex medical surgery and advanced treatment! The deep irony is that **no surgery or medicine was ever used**—Tricki was cured purely through disciplined diet, fasting, water, and outdoor exercise with other dogs."
        },
        {
            "type": "exam_tips",
            "content": "🔥 **BOARD EXAM MASTER CHEAT SHEET: High-Yield Themes & 5-Mark Questions**\n\n1. **Significance & Irony of the Title ('A Triumph of Surgery'):**\n   - Mrs. Pumphrey exclaims that Tricki's miraculous recovery is a 'triumph of surgery'.\n   - **Irony:** Tricki underwent no surgical operation or medicinal treatment. Dr. Herriot simply cut his diet, gave him plenty of water for two days, and let him run freely with the pack. Mrs. Pumphrey's blind belief in medical miracles blinds her to the simple truth of healthy living.\n\n2. **Character Sketch of Mrs. Pumphrey:**\n   - **Fabulously Rich & Over-Indulgent:** Possesses separate day/night beds, designer tweed coats, dedicated servants, and feeds luxurious treats (malt, Horlicks, chocolates, wine, brandy).\n   - **Foolishly Loving:** Mistook Tricki's lethargy for malnutrition. Her excessive pampering almost killed her beloved pet.\n   - **Emotional & Grateful:** Weeps with gratitude upon seeing Tricki transformed and thanks Dr. Herriot profusely.\n\n3. **Character Sketch of Dr. James Herriot:**\n   - **Pragmatic & Observant:** Diagnoses the root cause instantly — overfeeding and lack of exercise.\n   - **Tactful & Compassionate:** Avoids insulting Mrs. Pumphrey; tactfully removes Tricki to the clinic for 14 days.\n   - **Realistic & Resourceful:** Relies on nature cure (portion control, water, pack play) rather than unnecessary medications.\n   - **Good-Humoured:** Enjoys the luxury eggs, wine, and brandy sent by Mrs. Pumphrey with his clinic colleagues.\n\n4. **Key Lesson / Moral for Students:**\n   - Over-indulgence and unconditional pampering can become toxic and harmful.\n   - Physical activity, disciplined diet, and peer socialization are essential for physical and mental well-being, whether for animals or humans!",
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        }
    ]

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_sup_ch1.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_sup_ch1.json"
    final_json["metadata"]["id"] = "gseb_class10_english_sup_ch1"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Full-Text English Supplementary Chapter 1 Generated Successfully!")

if __name__ == "__main__":
    generate_full_english_sup_ch1()
