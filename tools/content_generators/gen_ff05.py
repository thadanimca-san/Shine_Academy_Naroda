"""CBSE Class 10 English, First Flight Ch 5: Glimpses of India
(I. A Baker from Goa, Lucio Rodrigues; II. Coorg, Lokesh Abrol; III. Tea from Assam, Arup Kumar Datta)."""
import sys
from lit_common import make, header, path, ex

ROOT = sys.argv[1]
PATH = path("ch05_glimpses_of_india")
C = make("ff10ch05")
blk = C.blk
GOA, COORG, TEA, LANG = ["baker_from_goa"], ["coorg"], ["tea_from_assam"], ["vocabulary_and_style"]
E1 = lambda n: ex(n, "Thinking about the Text (A Baker from Goa)")
E2 = lambda n: ex(n, "Thinking about the Text (Coorg)")
E3 = lambda n: ex(n, "Thinking about the Text (Tea from Assam)")

THREE = ("| | A Baker from Goa | Coorg | Tea from Assam |\n|---|---|---|---|\n"
         "| **Writer** | Lucio Rodrigues | Lokesh Abrol | Arup Kumar Datta |\n"
         "| **Region** | Goa, west coast | Kodagu, Karnataka | Assam, north-east |\n"
         "| **Focus** | the traditional baker (pader) and Portuguese bread | land, people, wildlife and adventure | tea plantations and legends of tea |\n"
         "| **Key details** | jingle of the bamboo staff; kabai; bol; bolinhas; bills on the wall | Kodavus; Coorg Regiment; General Cariappa; Kaveri; mahaseer; Bylakuppe | Pranjol and Rajvir; Dhekiabari; Chinese and Indian legends; second flush |\n"
         "| **Mood** | nostalgic and warm | admiring, like a travel guide | curious and informative |")

sections = [
 {"id": "s1", "title": "Three corners of India", "blocks": [
  blk("s1.hook", "hook", title="Bread, coffee and tea",
    body="Wake up to the **jingle** of a baker's bamboo staff in a Goan village. Walk through misty **coffee estates** in Coorg. Ride a train through a 'sea of **tea bushes**' in Assam.\n\n"
         "Glimpses of India is three short pieces about three regions of our country: their food, people, history and nature."),
  blk("s1.inspiration", "inspiration", title="The writers", person="Lucio Rodrigues, Lokesh Abrol, Arup Kumar Datta",
    body="**Lucio Rodrigues** writes with nostalgia about the traditions of Goa. **Lokesh Abrol** describes Coorg (Kodagu) like a travel writer. **Arup Kumar Datta**, a writer from Assam known for children's adventure books, tells the story of tea through two schoolboys.",
    future="Travel writing, tourism, food history and journalism all begin with close observation of places and people."),
  C.socratic("s1.socratic", "Why do the elders in Goa still miss the Portuguese loaves and the old baker?",
    ["They are part of happy childhood memories and Goan culture", "The bread is cheaper now", "They dislike modern bakeries for no reason"], 0,
    "Food often carries memories of home and tradition.")
 ]},
 {"id": "s2", "title": "A Baker from Goa", "blocks": [
  blk("s2.thm", "theory", title="The pader and his bread", revision=True,
    body="**Old memories:** elders in Goa often recall the good old **Portuguese days**, the Portuguese and their famous **loaves of bread**. Though the Portuguese have left, the bakers, the **mixers, moulders** and **furnaces** remain; the age-old, time-tested furnaces still exist and 'the fire in the furnaces has not yet been extinguished'. In some places the sons still carry on the family profession. The bakers are known as **paders**.\n\n"
         "**The baker's arrival:** in the narrator's childhood, the baker came at least twice a day: in the morning on his selling round, and again when he returned after emptying his basket. The **jingling thud of his bamboo staff** woke them. He greeted the house with 'Good morning!' and the children ran to him. The servant took the loaves; the children, without brushing their teeth, looked for the **bread-bangles** chosen specially for them. They would not even care to wash their mouths: 'tigers' teeth' would take care of that!\n\n"
         "**His dress:** the baker wore a **kabai**, a single-piece long frock reaching down to the knees. In the narrator's childhood he wore a shirt and **trousers** shorter than full-length and longer than half pants. Even today, anyone wearing a half pant that reaches just below the knees is told he is dressed **like a pader**!\n\n"
         "**Bread in Goan life:** marriage gifts are meaningless without the sweet bread called the **bol**; a party or feast loses its charm without bread; **cakes and bolinhas** are a must for **Christmas**; the lady of the house prepares **sandwiches** for her daughter's engagement.\n\n"
         "**A good living:** the baker collected his bills at the end of the month; they were recorded on a wall in **pencil**. Baking was a profitable profession: the baker and his family never starved, and his **plump physique** was an open testimony to this. Even today any person with a jackfruit-like physique is compared to a baker."),
  C.kc("s2.check", "What is a 'kabai'?",
    [("a single-piece long frock reaching down to the knees, worn by the baker", ""), ("a kind of bread", "The bol and bolinhas are breads."),
     ("the baker's bamboo staff", "The kabai is a dress."), ("a basket", "It is a dress.")],
    "It was the baker's dress in the Portuguese days.")
  ,C.kc("s2.check2", "Which bread is a must at Goan marriages?",
    [("the bol (sweet bread)", ""), ("bolinhas", "Bolinhas are for Christmas."), ("sandwiches", "Those are for engagements."), ("bread-bangles", "Those were for children.")],
    "Marriage gifts are meaningless without the bol.")
 ]},
 {"id": "s3", "title": "Coorg", "blocks": [
  blk("s3.thm", "theory", title="The land and the people", revision=True,
    body="**Where:** midway between **Mysore** and the coastal town of **Mangalore**, Coorg or **Kodagu** is the smallest district of **Karnataka**. It is a land of rolling hills, **evergreen rainforests**, spices and **coffee plantations**. Rainforests cover 30% of the district. The writer calls it 'a piece of heaven that must have drifted from the kingdom of god'.\n\n"
         "**Weather:** the monsoon pours enough to keep many visitors away; the season of joy begins in **September** and continues till **March**, when the weather is perfect, with some showers thrown in. The air breathes of invigorating coffee.\n\n"
         "**The people:** the fiercely independent people of Coorg, the **Kodavus**, are possibly of **Greek or Arabic descent**. One story says part of **Alexander's army** moved south along the coast and settled here. Another theory traces Arab origin: the **kuppia**, a long black coat with an embroidered waist-belt worn by Kodavu men, resembles the **kuffia** worn by Arabs and Kurds. Coorgi homes have a tradition of **hospitality**, and they love to tell tales of **valour**.\n\n"
         "**Martial pride:** the **Coorg Regiment** is one of the most decorated in the Indian Army, and the first Chief of the Indian Army, **General Cariappa**, was a Coorgi. The Kodavus are the only people in India permitted to **carry firearms without a licence**.\n\n"
         "**River and wildlife:** the river **Kaveri** obtains its water from the hills and forests of Coorg. **Mahaseer**, a large freshwater fish, abound in its waters. Kingfishers dive for their catch, squirrels and langurs drop fruit for the mischief of it, and elephants enjoy being bathed in the river. The wildlife includes Malabar squirrels, langurs and **slender loris**.\n\n"
         "**Adventure and places:** river rafting, canoeing, rappelling, rock climbing and mountain biking; climb the **Brahmagiri hills** for a view; walk to the island of **Nisargadhama** across a rope bridge; nearby **Bylakuppe**, India's largest **Tibetan** settlement, with Buddhist monks in red, ochre and yellow robes."),
  C.kc("s3.check", "Which people in India may carry firearms without a licence?",
    [("the Kodavus of Coorg", ""), ("the Gorkhas", "The text names the Kodavus."), ("the Sikhs", "The text names the Kodavus."), ("the people of Goa", "The text names the Kodavus.")],
    "This reflects their martial tradition.")
  ,C.kc("s3.check2", "Why are the Kodavus thought to be of Arab descent?",
    [("their kuppia resembles the kuffia worn by Arabs and Kurds", ""), ("they speak Arabic", "The evidence is the dress."),
     ("they live in a desert", "Coorg is green and hilly."), ("they came by ship from Arabia in 1947", "The theory is ancient, based on the dress.")],
    "Another theory links them to Alexander's army.")
 ]},
 {"id": "s4", "title": "Tea from Assam", "blocks": [
  blk("s4.thm", "theory", title="Two friends and the story of tea", revision=True,
    body="**The journey:** **Pranjol**, a youngster from Assam, and his classmate **Rajvir** are going to Assam for the summer vacation. Pranjol's father is the **manager of a tea garden**. At a station, a vendor calls 'Chai-garam... garam-chai'; the boys buy two cups. Rajvir says **over eighty crore cups** of tea are drunk every day throughout the world.\n\n"
         "**The landscape:** from the train, Rajvir gazes at a **'sea of tea bushes'**, densely wooded hills, and tall shade-trees. Pranjol, who has grown up on a plantation, is not impressed. Rajvir says Assam has the **largest concentration of plantations in the world**.\n\n"
         "**Legends of tea:**\n- **Chinese legend:** a Chinese emperor always boiled water before drinking it. One day a few leaves of the twigs burning under the pot fell into the water, giving it a delicious flavour. They were **tea leaves**.\n"
         "- **Indian legend:** **Bodhidharma**, an ancient Buddhist ascetic, **cut off his eyelids** because he felt sleepy during meditations. **Ten tea plants** grew out of the eyelids; the leaves, put in hot water and drunk, banished sleep.\n\n"
         "**History:** tea was first drunk in **China** as far back as **2700 B.C.** Words such as *tea*, *chai* and *chini* come from Chinese. Tea came to **Europe** only in the **sixteenth century** and was drunk more as **medicine** than as a beverage.\n\n"
         "**The tea garden:** they reach **Mariani junction**, where Pranjol's parents meet them, and drive to **Dhekiabari Tea Estate**. Women with **bamboo baskets** on their backs, in plastic aprons, are plucking the newly sprouted leaves. It is the **second-flush** or sprouting period, from **May to July**, which yields the **best tea**. Mr Barua is impressed that Rajvir has 'done his homework'."),
  blk("s4.table", "markdown_table", title="The three pieces side by side", revision=True, body=THREE),
  C.kc("s4.check", "According to the Indian legend, how did tea plants first grow?",
    [("from the eyelids Bodhidharma cut off", ""), ("from leaves that fell into boiling water", "That is the Chinese legend."),
     ("from seeds brought from Europe", "Tea came to Europe much later."), ("from a gift by a king", "It grew from Bodhidharma's eyelids.")],
    "Ten tea plants grew from his eyelids.")
  ,C.kc("s4.check2", "Which period yields the best tea?",
    [("the second flush, from May to July", ""), ("the winter months", "The second flush is May to July."), ("the first week of January", "The second flush."), ("the monsoon only", "May to July, the second flush.")],
    "This is the sprouting period.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Goa words: pader (baker), kabai (dress), bol (marriage), bolinhas (Christmas), bills in pencil on the wall.**\n"
         "- **Coorg: Kodagu; smallest district of Karnataka; Kodavus; kuppia; Cariappa; Kaveri; mahaseer; Brahmagiri; Nisargadhama; Bylakuppe.**\n"
         "- **Tea: 2700 B.C. China; 16th century Europe (medicine); 80 crore cups a day; Dhekiabari; second flush May to July.**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying bolinhas are for marriages: **bol** is for marriages; **bolinhas** for Christmas.\n2. Saying Coorg is in Kerala: it is in **Karnataka**, between Mysore and Mangalore.\n"
         "3. Mixing up the legends: leaves in boiling water = **Chinese** legend; eyelids = **Indian** legend (Bodhidharma).\n4. Calling Pranjol the curious one: **Rajvir** read about tea; Pranjol grew up there."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Make three groups: Goa, Coorg and Assam. Each designs a one-page travel poster using five facts from the text. Display and compare."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Which food or drink in your home carries a family memory or tradition? Write three sentences about it, like the narrator of A Baker from Goa."),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Geography (Agriculture):** coffee and tea are plantation crops; Assam and Karnataka are leading producers.\n- **History:** the Portuguese in Goa until 1961.\n"
         "- **Analytical paragraph:** use tea production data to practise writing about charts."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="Which of the three places would you most like to visit, and why? Answer in about 120 words using details from the text.\n\n"
         "**Model answer:** I would most like to visit Coorg. Lying between Mysore and Mangalore, this smallest district of Karnataka is full of rolling hills, evergreen rainforests and coffee estates, so the air itself smells of coffee. I would go between September and March, when the weather is perfect. I could try river rafting and rock climbing, climb the Brahmagiri hills, and cross the rope bridge to Nisargadhama. I would love to see elephants being bathed in the Kaveri and kingfishers diving for fish, and to visit the Tibetan settlement at Bylakuppe. Above all, I would like to meet the brave and hospitable Kodavus, whose regiment is among the most decorated in the Indian Army."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- A Baker from Goa: the narrator remembers the pader with his jingling bamboo staff, kabai and loaves; bread is part of every Goan celebration; baking was profitable.\n"
         "- Coorg: a beautiful, misty land of coffee and forests, home to the martial, hospitable Kodavus, the Kaveri, wildlife and adventure sports.\n"
         "- Tea from Assam: Rajvir and Pranjol travel to a tea estate; Rajvir shares the Chinese and Indian legends and the history of tea."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- Always say which of the three parts you are answering from.\n- Use the local words (pader, kabai, bol, Kodavus, kuppia, second flush); they show close reading.\n"
         "- 'What do you learn about...?' questions need at least two specific facts from the text."),
  blk("s5.flash1", "flashcard", front="What were bakers called in Goa?", back="Paders."),
  blk("s5.flash2", "flashcard", front="Name two reasons the Kodavus are thought to have foreign origins.", back="A story says part of Alexander's army settled there (Greek); their kuppia resembles the Arab kuffia."),
  blk("s5.flash3", "flashcard", front="What is the Chinese legend about tea?", back="Leaves from burning twigs fell into an emperor's boiling water and gave it a delicious flavour."),
  blk("s5.flash4", "flashcard", front="Which period gives the best tea?", back="The second flush, from May to July."),
 ]},
]

# ---------------- NCERT: Thinking about the Text ----------------
C.sa("ex1", GOA, "What are the elders in Goa nostalgic about?",
     ["They miss the good old Portuguese days.", "They remember the Portuguese and their famous loaves of bread, and the traditional bakers."], E1(1))
C.sa("ex2", GOA, "Is bread-making still popular in Goa? How do you know?",
     ["Yes. The mixers, moulders and furnaces still exist and the fire has not been extinguished.", "The thud and jingle of the baker's staff can still be heard, and sons carry on the family profession."], E1(2))
C.sa("ex3", GOA, "What is the baker called? When would the baker come every day? Why did the children run to meet him?",
     ["He was called the pader; he came twice a day, in the morning and again on his return.", "The children ran to meet him for the bread-bangles he had for them."], E1(3))
C.sa("ex4", GOA, "Match the following: when were these bread items eaten? (marriage gifts; a party or feast; a daughter's engagement; Christmas)",
     ["Marriage gifts: the sweet bread bol; a party or feast: bread of all kinds.", "Daughter's engagement: sandwiches; Christmas: cakes and bolinhas."], E1(4))
C.sa("ex5", GOA, "What did the bakers wear in Portuguese days and later? How did a baker live and collect his bills?",
     ["In Portuguese days a kabai, a single-piece frock to the knees; later a shirt and trousers between half and full length.", "He collected his bills at the month's end from records in pencil on the wall; the business was profitable, as his plump body showed."], E1(5))
C.sa("ex6", COORG, "Where is Coorg?",
     ["Coorg or Kodagu is the smallest district of Karnataka.", "It lies midway between Mysore and the coastal town of Mangalore."], E2(1))
C.sa("ex7", COORG, "What is the story about the Kodavus' descent?",
     ["One story says part of Alexander's army settled in Coorg after moving south along the coast.", "Another theory points to Arab origin: the kuppia worn by Kodavu men resembles the kuffia of Arabs and Kurds."], E2(2))
C.sa("ex8", COORG, "What are some of the things you now know about (i) the Coorg Regiment, (ii) General Cariappa, (iii) the Kodavus' right to firearms?",
     ["(i) It is one of the most decorated regiments of the Indian Army; (ii) General Cariappa, the first Chief of the Indian Army, was a Coorgi.", "(iii) The Kodavus are the only people in India allowed to carry firearms without a licence."], E2(3))
C.sa("ex9", COORG, "Name the river and the famous fish of Coorg, and three adventure sports you can enjoy there.",
     ["The river Kaveri; the mahaseer, a large freshwater fish.", "River rafting, canoeing, rappelling, rock climbing and mountain biking."])
C.sa("ex10", TEA, "Look at these words: upright, downpour, undergrowth, sunrise. They are compound words. Explain 'a sea of tea bushes'.",
     ["'A sea of tea bushes' is a metaphor.", "It means the tea bushes stretched as far as the eye could see, like the vast sea."])
C.sa("ex11", TEA, "Mention the two legends about the discovery of tea.",
     ["Chinese: leaves from burning twigs fell into an emperor's boiling water and gave it a delicious flavour.", "Indian: Bodhidharma cut off his eyelids to stay awake; ten tea plants grew from them."], E3(2))
C.sa("ex12", TEA, "Where is the tea garden Pranjol's father manages, and what do Rajvir and Pranjol see there?",
     ["Dhekiabari Tea Estate in Assam.", "They see a sea of tea bushes and women with bamboo baskets on their backs plucking newly sprouted leaves in the second-flush period."])

# ---------------- Extracts ----------------
C.extract("ext1", GOA,
  "Our elders are often heard reminiscing nostalgically about those good old Portuguese days,\nthe Portuguese and their famous loaves of bread.\nThose eaters of loaves might have vanished but the makers are still there.",
  [("Who are 'our elders'?", "The older people of Goa."),
   ("What are they nostalgic about?", "The Portuguese days and their loaves of bread."),
   ("Who are 'the makers'?", "The bakers (paders)."),
   ("Find a word that means 'thinking of the past with longing'.", "Nostalgically (reminiscing)."),
   ("Who are 'those eaters of loaves'?", "The Portuguese.")])
C.extract("ext2", COORG,
  "Midway between Mysore and the coastal town of Mangalore sits a piece of heaven that must have drifted from the kingdom of god.\nThis land of rolling hills is inhabited by a proud race of martial men, beautiful women and wild creatures.",
  [("Which place is described?", "Coorg (Kodagu)."),
   ("Where is it situated?", "Midway between Mysore and Mangalore."),
   ("Why is it called 'a piece of heaven'?", "Because of its great natural beauty."),
   ("Who are the 'martial men'?", "The Kodavus."),
   ("Give a word from the extract meaning 'warlike'.", "Martial.")])
C.extract("ext3", TEA,
  "'Over eighty crore cups of tea are drunk every day throughout the world,' said Rajvir.\n'Whew!' said Pranjol. 'Do you know, the first tea was drunk in China,' Rajvir added. 'As far back as 2700 B.C.!'",
  [("Who are Rajvir and Pranjol?", "Classmates travelling to Assam."),
   ("How many cups of tea are drunk every day?", "Over eighty crore."),
   ("Where was tea first drunk?", "In China."),
   ("How long ago?", "As far back as 2700 B.C."),
   ("What does 'Whew!' show about Pranjol?", "His surprise at the huge number.")])

# ---------------- Objective practice ----------------
C.m("mcq01", GOA, "What woke the narrator's family in the morning?",
    [("the jingling thud of the baker's bamboo staff", ""), ("church bells", "It was the baker's staff."), ("the cock crowing", "It was the baker's staff."), ("the milkman", "It was the baker.")],
    "The baker announced his arrival with his staff.")
C.m("mcq02", GOA, "What did the children look for in the baker's basket?",
    [("bread-bangles", ""), ("cakes", "They wanted bread-bangles."), ("sweets", "Bread-bangles."), ("toys", "Bread-bangles.")],
    "Specially chosen for them.")
C.m("mcq03", GOA, "Where were the baker's monthly accounts recorded?",
    [("on a wall, in pencil", ""), ("in a notebook", "On the wall."), ("on a slate", "In pencil on a wall."), ("in a bank", "On the wall.")],
    "He collected his bills at the end of the month.")
C.m("mcq04", GOA, "'Bolinhas' are a must for:",
    [("Christmas", ""), ("marriages", "The bol is for marriages."), ("birthdays", "Bolinhas are for Christmas."), ("engagements", "Sandwiches are for engagements.")],
    "Cakes and bolinhas are Christmas treats.")
C.m("mcq05", GOA, "How do we know the baker was well off?",
    [("his plump physique was an open testimony", ""), ("he owned many houses", "His body showed it."), ("he had a car", "His physique showed it."), ("he never worked", "He worked twice a day.")],
    "The family never starved.")
C.m("mcq06", COORG, "Coorg is the smallest district of:",
    [("Karnataka", ""), ("Kerala", "It is in Karnataka."), ("Tamil Nadu", "It is in Karnataka."), ("Goa", "It is in Karnataka.")],
    "It lies between Mysore and Mangalore.")
C.m("mcq07", COORG, "The best season to visit Coorg is:",
    [("September to March", ""), ("June to August", "That is the monsoon."), ("only in May", "September to March."), ("December only", "September to March.")],
    "The weather is perfect then.")
C.m("mcq08", COORG, "Who was the first Chief of the Indian Army from Coorg?",
    [("General Cariappa", ""), ("General Manekshaw", "He was not from Coorg."), ("General Thimayya", "The text names Cariappa."), ("Field Marshal Roberts", "He was British.")],
    "The Coorg Regiment is highly decorated.")
C.m("mcq09", COORG, "Mahaseer is a:",
    [("large freshwater fish", ""), ("bird", "It is a fish."), ("type of coffee", "It is a fish."), ("Coorgi dress", "That is the kuppia.")],
    "It is found in the Kaveri.")
C.m("mcq10", COORG, "Bylakuppe is known for:",
    [("India's largest Tibetan settlement", ""), ("its coffee factory", "It is a Tibetan settlement."), ("the source of the Kaveri", "It is a Tibetan settlement."), ("a fort", "It is a Tibetan settlement.")],
    "Buddhist monks in red, ochre and yellow robes live there.")
C.m("mcq11", TEA, "Where was Pranjol's father the manager?",
    [("Dhekiabari Tea Estate", ""), ("a coffee estate in Coorg", "He managed a tea estate in Assam."), ("a bakery in Goa", "A tea estate."), ("Mariani junction", "That is the station.")],
    "Pranjol had grown up on a tea garden.")
C.m("mcq12", TEA, "When did tea reach Europe?",
    [("in the sixteenth century", ""), ("in 2700 B.C.", "That is China."), ("in the twentieth century", "Much earlier."), ("in Roman times", "In the sixteenth century.")],
    "It was drunk more as medicine than as a beverage.")
C.m("mcq13", TEA, "Who had read up about tea before the trip?",
    [("Rajvir", ""), ("Pranjol", "He grew up there and was not curious."), ("Mr Barua", "He praised Rajvir."), ("the vendor", "Rajvir.")],
    "Mr Barua said Rajvir had done his homework.")
C.m("mcq14", LANG, "'A sea of tea bushes' is an example of:",
    [("metaphor", ""), ("simile", "There is no 'like' or 'as'."), ("alliteration", "It is a comparison."), ("personification", "It is a comparison.")],
    "It shows the vast stretch of bushes.")
C.m("mcq15", COORG, "The kuppia is:",
    [("a long black coat with an embroidered waist-belt", ""), ("a type of gun", "It is a coat."), ("a dance", "It is a coat."), ("a river", "It is a coat.")],
    "Worn by Kodavu men.")
C.m("mcq16", GOA, "A person dressed in a half pant reaching just below the knees is said to be dressed like:",
    [("a pader", ""), ("a Kodavu", "The comment is about the baker."), ("a soldier", "Like a pader."), ("a tea planter", "Like a pader.")],
    "The baker wore such trousers.")
C.tf("tf1", COORG, "The Kodavus are permitted to carry firearms without a licence.", True, "They are the only people in India with this right.")
C.tf("tf2", TEA, "According to the Chinese legend, tea grew from a monk's eyelids.", False, "That is the Indian legend about Bodhidharma.")
C.tf("tf3", GOA, "The furnaces of the bakers in Goa have all gone cold.", False, "The fire in the furnaces has not yet been extinguished.")
C.tf("tf4", TEA, "Assam has the largest concentration of tea plantations in the world.", True, "Rajvir says so.")

# ---------------- More written practice ----------------
C.sa("sa1", COORG, "How does the writer show that Coorg is rich in wildlife?",
     ["Kingfishers dive for fish, squirrels and langurs drop fruit, and elephants enjoy being bathed in the Kaveri.", "Malabar squirrels, langurs, slender loris and many birds, bees and butterflies are found there."])
C.sa("sa2", TEA, "How are Rajvir and Pranjol different in their attitude to tea gardens?",
     ["Rajvir is curious and excited; he has read about tea and its history.", "Pranjol has grown up among tea gardens, so he is not impressed by them."])
C.la("la1", GOA, "How does the writer show that bread was an important part of Goan life and culture?",
     ["The pader visited twice a day and was welcomed by the whole family.", "Marriage gifts needed the bol; feasts needed bread; Christmas needed cakes and bolinhas.",
      "Daughters' engagements called for sandwiches.", "Baking was profitable, and the furnaces and the trade continue even today.",
      "So bread was linked to the daily routine and to every celebration."])
C.la("la2", COORG, "Write a short travel brochure entry for Coorg using details from the text.",
     ["Heading and location: between Mysore and Mangalore, Karnataka's smallest district.", "Best time: September to March; coffee estates, rainforests, rolling hills.",
      "Things to do: river rafting, canoeing, rock climbing, Brahmagiri hills, Nisargadhama, Bylakuppe.", "People: the brave, hospitable Kodavus; the Coorg Regiment and General Cariappa."])

chapter = header("ch05", 5, "Glimpses of India", "Lucio Rodrigues; Lokesh Abrol; Arup Kumar Datta", "prose",
                 ["baker_from_goa", "coorg", "tea_from_assam", "vocabulary_and_style"],
                 "CBSE 2025-26 English Language and Literature (184): First Flight prose, Chapter 5 (A Baker from Goa; Coorg; Tea from Assam). Assessed through extracts (5 marks), short answers in 40-50 words (3 marks) and long answers in 100-120 words (6 marks).")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
