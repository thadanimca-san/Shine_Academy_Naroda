import json
import os

def generate_full_english_ch2():
    chapter_id = "ncert_class10_english_ch2"
    title = "Chapter 2: Nelson Mandela: Long Walk to Freedom (First Flight)"
    
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
        "estimated_minutes": 150,
        "version": "4.0.0-FULL-TEXT",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": ["english", "first_flight", "nelson_mandela", "long_walk_to_freedom", "full_text"],
        "learning_outcomes": [
            "Read and comprehend the original NCERT autobiographical excerpt by Nelson Mandela.",
            "Understand the historical struggle against the brutal system of Apartheid in South Africa.",
            "Analyze Mandela's philosophical concepts of courage, freedom, and twin obligations.",
            "Master rich vocabulary and rhetorical devices contextually.",
            "Formulate high-scoring analytical answers for Board Examinations."
        ],
        "ai_context": {
            "learning_goal": "Provide the exact NCERT text broken into passages, with inline translations using backticks for the Smart Translation Filter.",
        }
    }
    
    blocks = [
        {
            "type": "hook",
            "content": "Imagine being locked behind prison bars for **27 years `(27 साल / 27 વર્ષ)`** simply because you wanted equal rights and dignity for your people. When you finally walk out free, not only do you forgive your oppressors, but you become the first Black President of your nation in a historic **rainbow gathering `(इंद्रधनुषी जमावड़ा / મેઘધનુષી મેળાવડો)`**.\n\nThis is the extraordinary story of **Nelson Rolihlahla Mandela**. Let us read the *original, complete autobiographical text* line-by-line to understand his unbreakable spirit, his definition of true courage, and the long walk to freedom!",
            "difficulty": "Beginner",
            "bloom": "Understand"
        },
        {
            "type": "diagram",
            "content": "Nelson Mandela at the historic inauguration ceremony in Pretoria, South Africa.",
            "image_url": "assets/images/eng_ch2_mandela_inauguration.jpg",
            "alt_text": "Nelson Mandela waving to the crowd at Union Buildings amphitheatre."
        },
        {
            "type": "theory",
            "title": "Passage 1: The Dawn of Freedom and The Gathering of Nations",
            "content": "10th May dawned `(उदित हुआ / ઉગ્યો)` bright and clear. For the past few days I had been pleasantly besieged `(घिरा हुआ / ઘેરાયેલો)` by dignitaries `(उच्च पदस्थ व्यक्ति / મહાનુભાવો)` and world leaders who were coming to pay their respects before the inauguration `(उद्घाटन समारोह / ઉદ્ઘાટન સમારોહ)`. The inauguration would be the largest gathering ever of international leaders on South African soil.\n\nThe ceremonies took place in the lovely sandstone amphitheatre `(खुला रंगमंच / ખુલ્લું નાટ્યગૃહ)` formed by the Union Buildings in Pretoria. For decades this had been the seat of white supremacy `(श्वेत प्रभुत्व / શ્વેત સર્વોચ્ચતા)`, and now it was the site of a rainbow gathering `(इंद्रधनुषी जमावड़ा / મેઘધનુષી મેળાવડો)` of different colours and nations for the installation `(स्थापना / સ્થાપના)` of South Africa's first democratic `(लोकतांत्रिक / લોકશાહી)`, non-racial `(गैर-नस्लीय / બિન-વંશીય)` government.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Teacher's Insight:** Why was 10th May called an 'autumn day' in South Africa? \nBecause South Africa is in the Southern Hemisphere, where the seasons are reversed compared to India (Northern Hemisphere). In May, while India experiences peak summer, South Africa experiences pleasant autumn. Metaphorically, it also represents the 'autumn' of the old apartheid regime and the harvest of new freedom!"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Where did the inauguration ceremonies take place on 10th May?",
                "options": [
                    "The Parliament House in Cape Town",
                    "The Union Buildings amphitheatre in Pretoria",
                    "The National Stadium in Johannesburg",
                    "The Supreme Court in Durban"
                ],
                "correct_answer": "The Union Buildings amphitheatre in Pretoria",
                "explanation": "The historic inauguration took place in the sandstone amphitheatre formed by the Union Buildings in Pretoria, which had previously been the seat of white supremacy."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 2: The Swearing-In and The Historic Address",
            "content": "On that lovely autumn `(पतझड़ / પાનખર)` day I was accompanied by my daughter Zenani. On the podium `(मंच / સ્ટેજ)`, Mr de Klerk was first sworn in `(शपथ दिलाई गई / શપથ લેવડાવ્યા)` as second deputy president. Then Thabo Mbeki was sworn in as first deputy president. When it was my turn, I pledged `(प्रतिज्ञा ली / પ્રતિજ્ઞા લીધી)` to obey and uphold `(बनाए रखना / સમર્થન કરવું)` the Constitution and to devote `(समर्पित करना / સમર્પિત કરવું)` myself to the wellbeing of the Republic and its people.\n\nTo the assembled guests and the watching world, I said:\n\n\"Today, all of us do, by our presence here... confer `(प्रदान करना / અર્પણ કરવું)` glory and hope to newborn liberty `(आज़ादी / સ્વતંત્રતા)`. Out of the experience of an extraordinary `(असाधारण / અસાધારણ)` human disaster that lasted too long, must be born a society of which all humanity will be proud.\n\nWe, who were outlaws `(कानून द्वारा बहिष्कृत / બહિષ્કૃત)` not so long ago, have today been given the rare privilege `(दुर्लभ विशेषाधिकार / દુર્લભ વિશેષાધિકાર)` to be host to the nations of the world on our own soil. We thank all of our distinguished `(प्रतिष्ठित / પ્રતિષ્ઠિત)` international guests for having come to take possession with the people of our country of what is, after all, a common victory for justice `(न्याय / ન્યાય)`, for peace `(शांति / શાંતિ)`, for human dignity `(मानव गरिमा / માનવ ગૌરવ)`.\n\nWe have, at last, achieved our political emancipation `(राजनीतिक मुक्ति / રાજકીય મુક્તિ)`. We pledge ourselves to liberate `(मुक्त करना / મુક્ત કરવા)` all our people from the continuing bondage `(बंधन / બંધન)` of poverty `(गरीबी / ગરીબી)`, deprivation `(वंचितता / વંચિતતા)`, suffering `(पीड़ा / પીડા)`, gender and other discrimination `(भेदभाव / ભેદભાવ)`.\n\nNever, never, and never again shall it be that this beautiful land will again experience the oppression `(दमन / અત્યાચાર)` of one by another. The sun shall never set on so glorious `(शानदार / ભવ્ય)` a human achievement.\n\nLet freedom reign `(शासन करना / રાજ કરવું)`. God bless Africa!\"",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "🔥 **Board Exam Analysis - The 'Extraordinary Human Disaster':**\nWhen Mandela speaks of an 'extraordinary human disaster', he refers to the decades of **Apartheid**—a state-sponsored policy of brutal racial discrimination and dehumanization where millions of Black citizens were denied basic human rights and dignity."
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Why does Mandela refer to his people as having been 'outlaws not so long ago'?",
                "options": [
                    "They had broken traffic rules",
                    "Because of the policy of apartheid, many nations had severed diplomatic relations with South Africa",
                    "They were exiled to other continents",
                    "They refused to participate in the Olympics"
                ],
                "correct_answer": "Because of the policy of apartheid, many nations had severed diplomatic relations with South Africa",
                "explanation": "Under Apartheid, South Africa was internationally boycotted and isolated. Now, international leaders recognized and celebrated the new democratic government."
            },
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "theory",
            "title": "Passage 3: The Military Salute and The Two National Anthems",
            "content": "A few moments later we all lifted our eyes in awe `(विस्मय / આશ્ચર્ય)` as a spectacular array `(शानदार प्रदर्शन / ભવ્ય પ્રદર્શન)` of South African jets, helicopters and troop carriers roared `(गरजे / ગર્જના કરી)` in perfect formation over the Union Buildings.\n\nIt was not only a display of pinpoint precision `(सटीकता / અચૂક ચોકસાઈ)` and military force, but a demonstration of the military's loyalty `(वफादारी / વફાદારી)` to democracy, to a new government that had been freely and fairly elected. Only moments before, the highest generals of the South African defence force and police, their chests bedecked `(सजे हुए / શણગારેલા)` with ribbons and medals from days gone by, saluted me and pledged their loyalty. I was not unmindful `(अनजान नहीं / સભાન)` of the fact that not so many years before they would not have saluted but arrested me.\n\nFinally a chevron `(V-आकार का पैटर्न / V-આકારની ભાત)` of Impala jets left a smoke trail of the black, red, green, blue and gold of the new South African flag.\n\nThe day was symbolised `(प्रतीक बन गया / પ્રતીક બન્યું)` for me by the playing of our two national anthems, and the vision of whites singing 'Nkosi Sikelel' iAfrika' and blacks singing 'Die Stem', the old anthem of the Republic. Although that day neither group knew the lyrics `(गीत के बोल / ગીતના બોલ)` of the anthem they once despised `(घृणा करते थे / ધિક્કારતા હતા)`, they would soon know the words by heart.",
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Symbol of Reconciliation:** Notice the profound symbolism of singing **both** national anthems—'Nkosi Sikelel' iAfrika' (the African anthem) and 'Die Stem' (the old white anthem). Instead of erasing the past, Mandela united both cultures under one nation."
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "What did the spectacular smoke trail left by the Impala jets represent?",
                "options": [
                    "A sign of military aggression",
                    "The new five-colored South African flag",
                    "A rainbow weather phenomenon",
                    "The victory of a particular political party"
                ],
                "correct_answer": "The new five-colored South African flag",
                "explanation": "The Impala jets left a smoke trail showing the black, red, green, blue, and gold colors of the new democratic South African flag."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 4: A Sense of History and The Roots of Apartheid",
            "content": "On the day of the inauguration, I was overwhelmed `(अभिभूत / અભિભૂત)` with a sense of history. In the first decade of the twentieth century, a few years after the bitter Anglo-Boer war `(एंग्लो-बोअर युद्ध / એંગ્લો-બોઅર યુદ્ધ)` and before my own birth, the white-skinned peoples of South Africa patched up their differences and erected `(खड़ा किया / ઊભી કરી)` a system of racial domination `(नस्लीय वर्चस्व / વંશીય વર્ચસ્વ)` against the dark-skinned peoples of their own land.\n\nThe structure they created formed the basis of one of the harshest `(सबसे कठोर / સૌથી કઠોર)`, most inhumane `(अमानवीय / અમાનવીય)` societies the world has ever known. Now, in the last decade of the twentieth century, and my own eighth decade as a man, that system had been overturned `(उलट दिया गया / ઉથલાવી દેવામાં આવ્યું)` forever and replaced by one that recognised the rights and freedoms of all peoples, regardless of the colour of their skin.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Historical Context:** Notice the timeframe Mandela mentions:\n- **First decade of 20th century:** Apartheid was created after the Anglo-Boer War.\n- **Last decade of 20th century (1994):** Apartheid was officially overturned and replaced with democracy."
        },
        {
            "type": "theory",
            "title": "Passage 5: The Unintended Effect of Oppression and The Comrades of Struggle",
            "content": "That day had come about through the unimaginable `(अकल्पनीय / અકલ્પ્ય)` sacrifices of thousands of my people, people whose suffering and courage can never be counted or repaid. I felt that day, as I have on so many other days, that I was simply the sum `(योग / સરવાળો)` of all those African patriots `(देशभक्तों / દેશભક્તો)` who had gone before me. That long and noble line ended and now began again with me. I was pained `(दुखी / દુઃખી)` that I was not able to thank them and that they were not able to see what their sacrifices had wrought `(हासिल किया / સર્જાયેલ)`.\n\nThe policy of apartheid `(रंगभेद की नीति / રંગભેદ નીતિ)` created a deep and lasting wound `(घाव / ઘા)` in my country and my people. All of us will spend many years, if not generations, recovering from that profound `(गहरे / ઊંડા)` hurt. But the decades of oppression and brutality `(बर्बरता / ક્રૂરતા)` had another, unintended `(अनपेक्षित / અનપેક્ષિત)` effect, and that was that it produced the Oliver Tambos, the Walter Sisulus, the Chief Luthulis, the Yusuf Dadoos, the Bram Fischers, the Robert Sobukwes of our time—men of such extraordinary courage, wisdom `(बुद्धिमत्ता / શાણપણ)` and generosity `(उदारता / ઉદારતા)` that their like may never be known again.\n\nPerhaps it requires such depths of oppression to create such heights of character `(चरित्र की ऊंचाइयां / ચારિત્ર્યની ઊંચાઈઓ)`. My country is rich in the minerals and gems that lie beneath its soil, but I have always known that its greatest wealth is its people, finer and truer than the purest diamonds `(हीरे / હીરા)`.",
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        },
        {
            "type": "diagram",
            "content": "The great heroes and comrades of the South African freedom struggle.",
            "image_url": "assets/images/eng_ch2_struggle_heroes.jpg",
            "alt_text": "Portraits of Oliver Tambo, Walter Sisulu, and other freedom fighters."
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "According to Nelson Mandela, what is the greatest wealth of South Africa?",
                "options": [
                    "Its rich gold and diamond mines",
                    "Its lush forests and wildlife",
                    "Its people, finer and truer than the purest diamonds",
                    "Its powerful military and air force"
                ],
                "correct_answer": "Its people, finer and truer than the purest diamonds",
                "explanation": "Mandela states that while South Africa is rich in minerals and gems beneath its soil, its greatest wealth is its people."
            },
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "theory",
            "title": "Passage 6: The True Meaning of Courage and The Flame of Humanity",
            "content": "It is from these comrades `(साथियों / સાથીઓ)` in the struggle that I learned the meaning of courage. Time and again, I have seen men and women risk and give their lives for an idea. I have seen men stand up to attacks and torture `(यातना / ત્રાસ)` without breaking, showing a strength and resilience `(कठिनाइयों से उबरने की क्षमता / સ્થિતિસ્થાપકતા અને સહનશક્તિ)` that defies `(चुनौती देती है / પડકારે છે)` the imagination.\n\nI learned that courage was not the absence of fear, but the triumph `(विजय / વિજય)` over it. The brave man is not he who does not feel afraid, but he who conquers `(जीत लेता है / જીતે છે)` that fear.\n\nNo one is born hating another person because of the colour of his skin, or his background, or his religion. People must learn to hate, and if they can learn to hate, they can be taught to love, for love comes more naturally to the human heart than its opposite. Even in the grimmest `(सबसे कठिन / સૌથી કઠોર)` times in prison, when my comrades and I were pushed to our limits, I would see a glimmer `(झलक / ઝાંખી)` of humanity in one of the guards, perhaps just for a second, but it was enough to reassure `(आश्वस्त करना / આશ્વાસન આપવું)` me and keep me going. Man's goodness is a flame that can be hidden but never extinguished `(बुझाई / ઓલવી)`.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "🔥 **Mandela's Golden Quotation for Board Exams:**\n*\"Courage is not the absence of fear, but the triumph over it. The brave man is not he who does not feel afraid, but he who conquers that fear.\"*\nMemorize this line! It is one of the most frequently asked questions in CBSE/GSEB Class 10 exams."
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "How does Nelson Mandela define 'courage'?",
                "options": [
                    "Having no fear at all",
                    "The triumph over fear rather than the absence of fear",
                    "Physical strength and aggressive fighting",
                    "Escaping dangerous situations safely"
                ],
                "correct_answer": "The triumph over fear rather than the absence of fear",
                "explanation": "Mandela clarifies that being brave doesn't mean never feeling afraid; it means conquering and overcoming that fear."
            },
            "difficulty": "Intermediate",
            "bloom": "Remember"
        },
        {
            "type": "theory",
            "title": "Passage 7: The Twin Obligations of Every Man",
            "content": "In life, every man has twin obligations `(दोहरे कर्तव्य / બેવડી ફરજો)`—obligations to his family, to his parents, to his wife and children; and he has an obligation to his people, his community, his country. In a civil `(सभ्य / સભ્ય)` and humane society, each man is able to fulfil those obligations according to his own inclinations `(रुझानों / વલણો)` and abilities.\n\nBut in a country like South Africa, it was almost impossible for a man of my birth and colour to fulfil both of those obligations. In South Africa, a man of colour who attempted to live as a human being was punished and isolated `(अलग-थलग कर दिया गया / અલગ પાડી દેવાયો)`.\n\nIn South Africa, a man who tried to fulfil his duty to his people was inevitably `(अनिवार्य रूप से / અનિવાર્યપણે)` ripped from his family and his home and was forced to live a life apart, a twilight existence `(अंधेरे और रहस्य का जीवन / અંધકારમય અસ્તિત્વ)` of secrecy and rebellion `(विद्रोह / વિદ્રોહ)`. I did not in the beginning choose to place my people above my family, but in attempting to serve my people, I found that I was prevented from fulfilling my obligations as a son, a brother, a father and a husband.",
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Concept Breakdown - Twin Obligations:**\n1. **Personal Obligation:** Towards family, parents, wife, and children.\n2. **Social / National Obligation:** Towards community, people, and the nation.\nUnder Apartheid, any Black person who tried to fulfill their duty to their nation was branded a rebel, torn from their family, and thrown into prison."
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "What happens to a man of colour in South Africa when he attempts to fulfill his obligation to his people?",
                "options": [
                    "He is awarded national honours",
                    "He is promoted in his government job",
                    "He is ripped from his family and forced into a twilight existence of secrecy and rebellion",
                    "He is allowed dual citizenship"
                ],
                "correct_answer": "He is ripped from his family and forced into a twilight existence of secrecy and rebellion",
                "explanation": "Apartheid punished anyone who fought for their community, forcing them away from family into hiding, rebellion, and imprisonment."
            },
            "difficulty": "Intermediate",
            "bloom": "Understand"
        },
        {
            "type": "theory",
            "title": "Passage 8: The Meaning of Freedom & The Boyhood Illusion",
            "content": "I was not born with a hunger to be free. I was born free—free in every way that I could know. Free to run in the fields near my mother's hut, free to swim in the clear stream that ran through my village, free to roast mealies `(मक्के के भुट्टे / મકાઈના ડોડા)` under the stars and ride the broad backs of slow-moving bulls. As long as I obeyed my father and abided `(पालन किया / પાલન કર્યું)` by the customs of my tribe, I was not troubled by the laws of man or God.\n\nIt was only when I began to learn that my boyhood freedom was an illusion `(भ्रम / ભ્રમ)`, when I discovered as a young man that my freedom had already been taken from me, that I began to hunger for it.\n\nAt first, as a student, I wanted freedom only for myself, the transitory `(अस्थायी / ક્ષણિક)` freedoms of being able to stay out at night, read what I pleased and go where I chose. Later, as a young man in Johannesburg, I yearned `(तीव्र इच्छा की / તીવ્ર ઝંખના કરી)` for the basic and honourable freedoms of achieving my potential, of earning my keep, of marrying and having a family—the freedom not to be obstructed `(बाधित / અવરોધાયેલ)` in a lawful life.",
            "difficulty": "Advanced",
            "bloom": "Analyze"
        },
        {
            "type": "teacher_tip",
            "content": "💡 **Evolution of Mandela's Perception of Freedom:**\n- **Childhood:** Physical freedom (running in fields, swimming in streams, roasting mealies).\n- **Student:** Transitory freedom (staying out at night, reading books of choice).\n- **Young Man:** Basic & honourable freedom (earning livelihood, marrying, family life).\n- **Mature Leader:** Universal freedom (freedom and dignity for all his brothers and sisters)."
        },
        {
            "type": "theory",
            "title": "Passage 9: The Transformation into a Freedom Fighter & The Liberation of the Oppressor",
            "content": "But then I slowly saw that not only was I not free, but my brothers and sisters were not free. I saw that it was not just my freedom that was curtailed `(कम किया गया / ઘટાડી દેવામાં આવી)`, but the freedom of everyone who looked like I did. That is when I joined the African National Congress, and that is when the hunger for my own freedom became the greater hunger for the freedom of my people.\n\nIt was this desire for the freedom of my people to live their lives with dignity `(गरिमा / ગૌરવ)` and self-respect that animated `(ऊर्जा भर दी / પ્રેરિત કર્યું)` my life, that transformed a frightened young man into a bold one, that drove a law-abiding attorney `(वकील / વકીલ)` to become a criminal, that turned a family-loving husband into a man without a home, that forced a life-loving man to live like a monk `(संन्यासी / સાધુ)`.\n\nI am no more virtuous `(सदाचारी / સદ્ગુણી)` or self-sacrificing than the next man, but I found that I could not even enjoy the poor and limited freedoms I was allowed when I knew my people were not free. Freedom is indivisible `(अविभाज्य / અવિભાજ્ય)`; the chains on any one of my people were the chains on all of them, the chains on all of my people were the chains on me.\n\nI knew that the oppressor `(दमनकारी / અત્યાચારી)` must be liberated just as surely as the oppressed `(पीड़ित / પીડિત)`. A man who takes away another man's freedom is a prisoner of hatred `(नफ़रत का कैदी / નફરતનો કેદી)`; he is locked behind the bars of prejudice `(पूर्वाग्रह / પૂર્વગ્રહ)` and narrow-mindedness `(संकीर्ण मानसिकता / સંકુચિતતા)`. I am not truly free if I am taking away someone else's freedom, just as surely as I am not free when my freedom is taken from me. The oppressed and the oppressor alike are robbed `(वंचित / વંચિત)` of their humanity.",
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        },
        {
            "type": "knowledge_check",
            "content": {
                "question": "Why does Nelson Mandela say that the oppressor must be liberated just as surely as the oppressed?",
                "options": [
                    "Because oppressors also want to retire early",
                    "Because a person who robs another of freedom is himself a prisoner of hatred, prejudice, and narrow-mindedness",
                    "Because oppressors pay higher taxes",
                    "Because oppressors belong to the African National Congress"
                ],
                "correct_answer": "Because a person who robs another of freedom is himself a prisoner of hatred, prejudice, and narrow-mindedness",
                "explanation": "Mandela explains that both the oppressor and the oppressed are robbed of their humanity; the oppressor is trapped behind the bars of prejudice and hatred."
            },
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        },
        {
            "type": "exam_tips",
            "content": "🔥 **BOARD EXAM MASTER CHEAT SHEET: High-Yield Themes & 5-Mark Questions**\n\n1. **The Twin Obligations:**\n   - Obligation to Family (parents, wife, children).\n   - Obligation to Country and Community.\n   - In an apartheid state, a Black man fulfilling duty to country was isolated and treated as an outlaw.\n\n2. **Meaning of Courage:**\n   - Courage is NOT the absence of fear, but the triumph over it.\n   - A brave man is one who conquers fear.\n\n3. **Evolution of Freedom:**\n   - Boyhood (illusion of freedom: swimming, running) ➔ Youth (transitory personal freedom) ➔ Manhood (honourable livelihood & family) ➔ Freedom Fighter (hunger for freedom of all his people).\n\n4. **Transformation of Mandela:**\n   - Frightened young man ➔ Bold leader.\n   - Law-abiding lawyer ➔ Branded criminal.\n   - Family-loving husband ➔ Homeless wanderer.\n   - Life-loving man ➔ Living like a monk.\n\n5. **Liberation of Oppressor and Oppressed:**\n   - An oppressor is a prisoner of hatred, prejudice, and narrow-mindedness.\n   - Both the oppressor and oppressed are equally robbed of their humanity!",
            "difficulty": "Advanced",
            "bloom": "Evaluate"
        }
    ]

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ch2.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch2.json"
    final_json["metadata"]["id"] = "gseb_class10_english_ch2"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Full-Text English Chapter 2 Generated Successfully!")

if __name__ == "__main__":
    generate_full_english_ch2()

