"""CBSE Class 10 Hindi Course B, Sparsh Part 2, Ch 10: अब कहाँ दूसरे के दुख से दुखी होने वाले (Nida Fazli).
The text is in copyright: the lesson retells it, and extract passages are Shine retellings in Hindi."""
import sys
from hindi_common import make, header, path, ex, PROSE_INTRO
from lit_common import closing

ROOT = sys.argv[1]
PATH = path("sparsh", "ch10_ab_kahan_doosre_ke_dukh_se")
C = make("hsp10ch10")
blk = C.blk
SHARE, MOTHER, NATURE, CITY = ["earth_belongs_to_all"], ["compassion_stories"], ["nature_imbalance"], ["city_life_change"]
MO = lambda n: ex(n, "मौखिक")
LK = lambda n: ex(n, "लिखित (क)")
LB = lambda n: ex(n, "लिखित (ख)")
AS = lambda n: ex(n, "आशय स्पष्ट कीजिए")

PARTS = ("| Part of the essay | What it says |\n|---|---|\n"
         "| **Solomon and the ants** | King **Solomon (सुलेमान)**, who knew the language of birds and animals, passed with his army. The ants feared being crushed. Solomon said: 'Do not fear; God made Solomon the protector of all; I am love for all, not trouble.' The ants prayed for him. |\n"
         "| **Noah and the dog** | In Arabia a man named **Lashkar** once called a wounded dog 'dirty'. The dog replied that neither was it a dog by choice nor he a man by choice; the Maker is the same. Lashkar wept all his life, so he is remembered as **Nuh (नूह)**. |\n"
         "| **Sheikh Ayaz's father** | The Sindhi poet **Sheikh Ayaz's** father saw a black ant (**च्योंटा**) on his arm while eating. He left his food to take it back to the well: 'I have made a householder homeless.' |\n"
         "| **The earth is for all** | God made the earth for all living beings. Humans built walls; growing **population** cut forests, pushed back the **sea** and drove birds and animals from their homes. |\n"
         "| **The sea's anger** | In **Bombay**, builders reclaimed land from the sea. The sea, patient for long, threw **three ships** onto the shore at **Worli**, **Bandra (Carter Road)** and the **Gateway of India**, so broken that they could never sail again. |\n"
         "| **The mother's lessons** | The writer's mother said: don't pluck leaves after sunset (trees weep); don't pick flowers at lamp-lighting time; greet the river; don't trouble pigeons or the rooster. |\n"
         "| **The pigeon's eggs** | In **Gwalior**, a cat broke one of a pigeon pair's eggs; the mother tried to save the other, but it slipped from her hand and broke. She **fasted the whole day** to seek God's forgiveness. |\n"
         "| **Now, in Bombay** | In his flat, pigeons nested near the kitchen; his wife put a **net (जाली)** on the window. The pigeons now sit outside, sad. The writer asks: where are the people who feel sad at others' sorrow? |")

sections = [
 {"id": "s1", "title": "Whose earth is it?", "blocks": [
  blk("s1.hook", "hook", title="A net on the window",
    body="Two pigeons have built a nest in a flat in Mumbai. They make a mess, so a net is fixed on the window. The pigeons now sit outside all night, sad. It seems a small thing, but it raises a big question: **does the earth belong only to humans?**\n\n"
         "In this essay **Nida Fazli** moves from old stories of kindness to today's crowded cities, and asks where the people have gone who **felt sad at the sorrow of others**."),
  blk("s1.inspiration", "inspiration", title="The writer", person="Nida Fazli", years="1938–2016",
    body="**Nida Fazli** was born in **Delhi** and grew up in **Gwalior**. He was a much-loved **Urdu-Hindi poet**, prose writer and film lyricist, known for simple words and deep feeling.\n\n"
         "His works include **लफ़्ज़ों का पुल** and **खोया हुआ सा कुछ**; this chapter is from his prose collection **तमाशा मेरे आगे**. He received the **Sahitya Akademi Award** and the **Padma Shri**.",
    future="His question about sharing the earth is now a question of climate and survival."),
  C.socratic("s1.socratic", "Why did the writer's mother fast for a whole day?",
    ["To ask God's forgiveness after a pigeon's egg broke in her hand", "Because it was a festival", "Because she was ill"], 0,
    "She felt she had sinned.")
 ]},
 {"id": "s2", "title": "The essay in brief", "blocks": [
  blk("s2.note", "theory", title="How to read this chapter",
    body="Read the full chapter in your **NCERT Sparsh Part 2** textbook. The table below retells it in order; passages in the questions are Shine retellings in Hindi."),
  blk("s2.table", "markdown_table", title="The essay in order", revision=True, body=PARTS),
  C.kc("s2.check", "Why is Lashkar remembered as Nuh?",
    [("he wept all his life after the dog's reply", ""), ("he built a ship", "He wept all his life."), ("he was a king", "He wept."), ("he spoke to ants", "That was Solomon.")],
    "The dog's words changed him.")
  ,C.kc("s2.check2", "How did the sea show its anger in Bombay?",
    [("it threw three ships onto the shore", ""), ("it flooded the whole city", "Three ships."), ("it dried up", "Three ships."), ("it swallowed buildings", "Three ships.")],
    "At Worli, Bandra and the Gateway of India.")
 ]},
 {"id": "s3", "title": "Ideas in the essay", "blocks": [
  blk("s3.thm", "theory", title="What the writer wants us to see", revision=True,
    body="**The earth belongs to all:** God created it for humans, birds, animals, insects, rivers and trees alike. Humans have built walls and claimed it alone.\n\n"
         "**Old compassion:** Solomon, Lashkar (Nuh), Sheikh Ayaz's father and the writer's mother felt the pain of even the smallest creatures.\n\n"
         "**Population and greed:** growing population and builders cut forests and push back the sea; birds and animals lose homes and **'डेरा डाल लेते हैं'** (settle wherever they can).\n\n"
         "**Nature's patience has a limit:** the sea's anger in Bombay shows that nature strikes back. **'जो जितना बड़ा होता है उसे उतना ही कम गुस्सा आता है'**, but when it does come, it is huge.\n\n"
         "**Imbalance:** more heat, untimely rain, earthquakes, floods, storms and new diseases are results of disturbing nature.\n\n"
         "**From Gwalior to Bombay:** from a big house with a courtyard and a caring mother to small box-like flats where people shut out pigeons with nets. Life has **shrunk into boxes**, and so has kindness.\n\n"
         "**Oneness:** *'मट्टी से मट्टी मिले…'*: all beings are made of the same soil; in the end no one can tell who is who."),
  C.kc("s3.check", "What does 'डेरा डाल लेना' mean in the essay?",
    [("to settle wherever one can for the time being", ""), ("to fight", "To settle."), ("to build a palace", "To settle temporarily."), ("to run away", "To settle somewhere.")],
    "Homeless birds and animals did this.")
  ,C.kc("s3.check2", "What message does the essay mainly give?",
    [("all creatures have an equal right to the earth", ""), ("cities are better than villages", "Equal right to the earth."), ("pigeons are a nuisance", "The opposite."), ("the sea is dangerous", "Equal right to the earth.")],
    "Compassion for all life.")
 ]},
 {"id": "s4", "title": "Language and style", "blocks": [
  blk("s4.thm", "theory", title="Language and style", revision=True,
    body="| Feature | Example / note |\n|---|---|\n| **Type** | **निबंध** (reflective essay) mixing memories and stories |\n"
         "| **Language** | simple **Hindustani** with Urdu and English words (*नेचर, बिल्डर, खुदा, रोज़ा, फ़्लैट*) |\n"
         "| **Stories within** | Solomon, Nuh, Sheikh Ayaz's father, the mother's tales |\n| **Tone** | gentle, sad, thoughtful |\n"
         "| **Doha** | *'मट्टी से मट्टी मिले, खो के सभी निशान…'* sums up the theme |"),
  C.kc("s4.check", "This chapter is best described as a:",
    [("reflective essay", ""), ("poem", "Essay."), ("play", "Essay."), ("diary", "Essay.")],
    "With small stories inside.")
 ]},
 closing(C,
   "- **Stories: सुलेमान (चींटियाँ), लशकर → नूह (कुत्ता), शेख अयाज़ के पिता (च्योंटा), माँ (कबूतर के अंडे, रोज़ा).**\n- **Bombay: builders → sea throws 3 ships (Worli, Bandra, Gateway).**\n- **Message: धरती सबकी; जाली लगी खिड़की = सिमटती करुणा.**",
   "1. Mixing up stories: the **dog** story is about Lashkar (Nuh); the **ant** stories are Solomon and Sheikh Ayaz's father.\n"
   "2. Writing the mother fasted for a festival: she fasted to seek **forgiveness** for the broken egg.\n3. Missing the title's question: **people who share others' pain are now rare**.\n4. Writing exam answers in English: answer in **Hindi**.",
   "Ask students to list three ways their city has taken homes from birds or animals, and one thing they can do about each.",
   "When did you last feel sad for an animal or bird? What did you do?",
   "- **Science:** ecosystems and biodiversity.\n- **Geography:** urbanisation and land reclamation in Mumbai.",
   "'अब कहाँ दूसरे के दुख से दुखी होने वाले' — explain the title in about 60 words.",
   "The title asks where the people have gone who felt sad at others' sorrow. In the past, Solomon protected ants, Sheikh Ayaz's father returned an ant to its home, and the writer's mother fasted after a pigeon's egg broke. Today people cut forests, push back the sea and put nets on windows to keep pigeons out. Compassion for other creatures has become rare, so the title is fitting.",
   "- Nida Fazli says the earth belongs to all creatures, not only humans.\n- Old stories (Solomon, Nuh, Sheikh Ayaz's father, the writer's mother) show compassion for small creatures.\n"
   "- Growing population and builders destroy nature; the sea in Bombay struck back by throwing three ships ashore.\n- In today's flats even pigeons are shut out; people who share others' pain are now rare.",
   "- Answer in Hindi, in 25-30 words for 2 marks.\n- Name the right person for each story.\n- Link examples to the theme of compassion and nature.",
   [("Why did Sheikh Ayaz's father leave his food?", "To take a black ant back to its home at the well: 'I have made a householder homeless.'"),
    ("Where did the sea throw the three ships?", "Worli, Bandra (Carter Road) and the Gateway of India.")]),
]

# ---------------- NCERT मौखिक ----------------
C.two("mo1", CITY, "Why were the big builders pushing the sea back?",
      ["Because of growing population, more land was needed for buildings.", "So builders filled the sea to make new land and earn money."], MO(1))
C.two("mo2", CITY, "In which city was the writer's house?",
      ["The writer's old house was in Gwalior.", "Now he lives in a flat in Bombay (Versova)."], MO(2))
C.two("mo3", CITY, "How has life begun to shrink into houses?",
      ["Earlier people lived in big houses with courtyards and open spaces.", "Now they live in small, box-like flats in crowded cities."], MO(3))
C.two("mo4", MOTHER, "Why were the pigeons fluttering here and there in distress?",
      ["A cat broke one of their eggs, and the other slipped from the mother's hand and broke.", "Losing both eggs, the pigeons were upset and fluttered about."], MO(4))
# ---------------- NCERT लिखित (क) ----------------
C.two("lk1", MOTHER, "Why is Lashkar remembered as Nuh in Arabia?",
      ["He once called a wounded dog 'dirty'; the dog said neither of them chose their form, and the Maker is one.", "Lashkar was so sorry that he wept all his life, so he is remembered as Nuh."], LK(1))
C.two("lk2", MOTHER, "At what time did the writer's mother forbid plucking leaves, and why?",
      ["She forbade plucking leaves after sunset.", "She said the trees would weep, because at that time they too rest."], LK(2))
C.two("lk3", NATURE, "What was the result of the imbalance in nature?",
      ["There is more heat, untimely rain, earthquakes, floods and storms.", "New diseases have also appeared."], LK(3))
C.two("lk4", MOTHER, "Why did the writer's mother keep a fast for the whole day?",
      ["A pigeon's egg slipped from her hand and broke while she was trying to save it.", "She felt she had sinned and fasted to seek God's forgiveness."], LK(4))
C.two("lk5", CITY, "What changes did the writer feel from Gwalior to Bombay? Explain.",
      ["In Gwalior there were big houses, courtyards and people like his mother who felt for every creature.", "In Bombay there are crowded flats, the sea and forests are pushed back, and people shut out even pigeons."], LK(5), "medium")
C.two("lk6", NATURE, "What do you understand by 'डेरा डाल लेने'?",
      ["It means settling somewhere temporarily.", "Birds and animals who lost their homes settled wherever they could find space."], LK(6))
C.two("lk7", SHARE, "Why did Sheikh Ayaz's father leave his food and get up on seeing a black ant on his arm?",
      ["He realised the ant had come with him from the well and was now away from its home.", "He left his food to take it back, saying he had made a householder homeless."], LK(7))
# ---------------- NCERT लिखित (ख) ----------------
C.two("lb1", NATURE, "What effect did the growing population have on the environment?",
      ["Forests were cut and the sea was pushed back to build houses; birds and animals lost their homes.", "Nature became unbalanced, causing heat, untimely rain, floods, storms and new diseases."], LB(1))
C.two("lb2", CITY, "Why did the writer's wife have to fix a net on the window?",
      ["Pigeons had nested near the kitchen; they kept coming and going and things fell and broke.", "To stop the trouble, she put a net on the window, and the pigeons were shut out."], LB(2))
C.two("lb3", NATURE, "What was the cause of the sea's anger? How did it show it?",
      ["Builders kept filling the sea to make land, pushing it back.", "In anger it threw three ships onto the shore at Worli, Bandra and the Gateway of India."], LB(3))
C.two("lb4", SHARE, "What does the writer want to say through 'मट्टी से मट्टी मिले, खो के सभी निशान, किसमें कितना कौन है, कैसे हो पहचान'?",
      ["All living beings are made of the same soil and return to it.", "After that no one can tell who is who, so all creatures are equal and one."], LB(4), "medium")
# ---------------- NCERT आशय ----------------
C.two("as1", NATURE, "Explain the meaning: 'नेचर की सहनशक्ति की एक सीमा होती है। नेचर के गुस्से का एक नमूना कुछ साल पहले बंबई में देखने को मिला था।'",
      ["Nature can bear human interference only up to a limit.", "When the sea was pushed back too far in Bombay, it showed its anger by throwing ships ashore."], AS(1))
C.two("as2", NATURE, "Explain the meaning: 'जो जितना बड़ा होता है उसे उतना ही कम गुस्सा आता है।'",
      ["Great beings like the sea are very patient and rarely get angry.", "But when their patience ends, their anger is terrible."], AS(2))
C.two("as3", NATURE, "Explain the meaning: 'इस बस्ती ने न जाने कितने परिंदों-चरिंदों से उनका घर छीन लिया है… जो नहीं जा सके हैं उन्होंने यहाँ-वहाँ डेरा डाल लिया है।'",
      ["Human settlements have taken away the homes of countless birds and animals.", "Some left the city; those who could not are living wherever they find a corner."], AS(3), "medium")
C.two("as4", SHARE, "Explain the feeling in Sheikh Ayaz's father's words: 'मैंने एक घरवाले को बेघर कर दिया है। उस बेघर को कुएँ पर उसके घर छोड़ने जा रहा हूँ।'",
      ["He felt deep compassion even for a tiny ant.", "He believed it was wrong to take any creature away from its home, so he returned it."], AS(4))

# ---------------- Extracts (Shine retellings) ----------------
C.extract("ext1", MOTHER, "ग्वालियर के हमारे घर के रोशनदान में कबूतरों ने घोंसला बनाया था। एक दिन बिल्ली ने एक अंडा तोड़ दिया। माँ ने दूसरा अंडा बचाना चाहा, पर वह उसके हाथ से गिरकर टूट गया। दुखी माँ ने खुदा से माफ़ी माँगने के लिए पूरे दिन रोज़ा रखा।",
  [("Where had the pigeons made their nest?", "In the ventilator of the house in Gwalior."), ("Who broke the first egg?", "A cat."),
   ("How did the second egg break?", "It slipped from the mother's hand."), ("What did the mother do then?", "She fasted the whole day."), ("Why did she do this?", "To seek God's forgiveness.")],
  intro=PROSE_INTRO)
C.extract("ext2", NATURE + CITY, "बढ़ती आबादी के कारण बिल्डर समुद्र को पीछे धकेलकर उसकी ज़मीन पर इमारतें बनाने लगे। सहनशील समुद्र को आख़िर गुस्सा आ गया। उसने तीन जहाज़ उठाकर किनारे पर फेंक दिए—एक वर्ली, एक बांद्रा और एक गेटवे ऑफ़ इंडिया पर।",
  [("Why were builders pushing back the sea?", "Because of growing population and the need for land."), ("What did they build?", "Buildings on land taken from the sea."),
   ("What did the sea do in anger?", "It threw three ships onto the shore."), ("Name one place where a ship was thrown.", "Worli / Bandra / Gateway of India."), ("What does this event show?", "That nature's patience has a limit.")],
  intro=PROSE_INTRO)

# ---------------- Objective practice ----------------
C.m("mcq01", SHARE, "Who understood the language of birds and animals?", [("King Solomon", ""), ("Lashkar", "Solomon."), ("Sheikh Ayaz", "Solomon."), ("the writer", "Solomon.")], "He reassured the ants.")
C.m("mcq02", MOTHER, "Lashkar is remembered as:", [("Nuh", ""), ("Solomon", "Nuh."), ("Ayaz", "Nuh."), ("Latif", "Nuh.")], "He wept all his life.")
C.m("mcq03", MOTHER, "Lashkar's life changed because of the words of a:", [("wounded dog", ""), ("king", "A dog."), ("pigeon", "A dog."), ("saint", "A dog.")], "The Maker is the same for all.")
C.m("mcq04", SHARE, "Sheikh Ayaz's father returned a black ant to:", [("the well", ""), ("the forest", "The well."), ("the garden", "The well."), ("the river", "The well.")], "Where it had come from.")
C.m("mcq05", MOTHER, "The writer's mother said not to pluck leaves:", [("after sunset", ""), ("in the morning", "After sunset."), ("at noon", "After sunset."), ("on Fridays", "After sunset.")], "The trees would weep.")
C.m("mcq06", MOTHER, "The mother asked to greet:", [("the river", ""), ("the sea", "The river."), ("the sun", "The river."), ("the moon", "The river.")], "'दरिया पर जाओ तो उसे सलाम किया करो'.")
C.m("mcq07", MOTHER, "Why did the mother say not to trouble the rooster?", [("it wakes everyone in the morning", ""), ("it is holy", "It wakes people."), ("it bites", "It wakes people."), ("it is expensive", "It wakes people.")], "Before the mullah's call.")
C.m("mcq08", CITY, "The writer's old house was in:", [("Gwalior", ""), ("Delhi", "Gwalior."), ("Lucknow", "Gwalior."), ("Bombay", "That is where he lives now.")], "He now lives in Bombay.")
C.m("mcq09", NATURE, "How many ships did the sea throw ashore?", [("three", ""), ("one", "Three."), ("two", "Three."), ("five", "Three.")], "Worli, Bandra, Gateway.")
C.m("mcq10", CITY, "Why did the writer's wife fix a net on the window?", [("to keep the pigeons out", ""), ("to keep mosquitoes out", "Pigeons."), ("for decoration", "Pigeons."), ("to stop thieves", "Pigeons.")], "Things fell and broke.")
C.m("mcq11", NATURE, "'परिंदे-चरिंदे' means:", [("birds and grazing animals", ""), ("fish and frogs", "Birds and animals."), ("trees and plants", "Birds and animals."), ("people", "Birds and animals.")], "They lost their homes.")
C.m("mcq12", NATURE, "'जो जितना बड़ा होता है उसे उतना ही कम गुस्सा आता है' refers here to:", [("the sea", ""), ("the king", "The sea."), ("the builder", "The sea."), ("the writer", "The sea.")], "Its patience is great, but limited.")
C.m("mcq13", SHARE, "The main theme of the essay is:", [("compassion for all creatures and respect for nature", ""), ("the beauty of Bombay", "Compassion."), ("the life of Solomon", "Compassion."), ("building flats", "Compassion.")], "The earth belongs to all.")
C.m("mcq14", CITY, "This chapter is taken from Nida Fazli's book:", [("तमाशा मेरे आगे", ""), ("गोदान", "That is Premchand's."), ("साकेत", "That is Gupt's."), ("मधुशाला", "That is Bachchan's.")], "A prose collection.")
C.tf("tf1", SHARE, "Solomon's army crushed the ants.", False, "He reassured and protected them.")
C.tf("tf2", MOTHER, "The writer's mother fasted to seek forgiveness after a pigeon's egg broke.", True, "In Gwalior.")
C.tf("tf3", NATURE, "The sea threw ships ashore because builders pushed it back.", True, "Nature's patience has a limit.")
C.tf("tf4", CITY, "The writer says life in Bombay flats has become more open and spacious.", False, "Life has shrunk into box-like flats.")
C.tf("tf5", SHARE, "The doha 'मट्टी से मट्टी मिले' teaches that all beings are one.", True, "Made of the same soil.")
C.two("sa1", NATURE, "Suggest two ways to give birds and animals their place back in cities.",
      ["Plant trees and keep parks and wetlands safe from construction.", "Keep water bowls and bird-houses on balconies instead of nets everywhere."])
C.two("sa2", MOTHER, "What does the mother's behaviour teach us?",
      ["She felt every creature's pain as her own, even a pigeon's.", "It teaches compassion and respect for all forms of life."])

chapter = header("sparsh", "ch10", 10, "अब कहाँ दूसरे के दुख से दुखी होने वाले", "निदा फ़ाज़ली", "prose", ["earth_belongs_to_all", "compassion_stories", "nature_imbalance", "city_life_change"],
                 "CBSE 2025-26 Hindi Course B (085), Section C: Sparsh Part 2 prose. Assessed through extract-based MCQs (1 mark each) and short answers in 25-30 words (2 marks); answers are written in Hindi. The text is in copyright: read it in the NCERT textbook.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
