"""CBSE Class 10 English, Footprints without Feet Ch 5: Footprints without Feet (H. G. Wells)."""
import sys
from lit_common import make, header, path, ex

ROOT = sys.argv[1]
PATH = path("ch05_footprints_without_feet", "footprints")
C = make("fwf10ch05")
blk = C.blk
LONDON, IPING, GRIFFIN, SCIENCE = ["griffin_in_london"], ["griffin_at_iping"], ["griffins_character"], ["science_and_responsibility"]
RF = lambda n: ex(n, "Read and Find Out")
TA = lambda n: ex(n, "Think about It")

TIMELINE = ("| Where | What Griffin does |\n|---|---|\n"
            "| **His lodgings, London** | becomes invisible with rare drugs; sets fire to the house to take revenge on his landlord |\n"
            "| **London streets** | walks naked in mid-winter; leaves muddy footprints that two boys follow |\n"
            "| **A big London store** | hides after closing, eats, sleeps in blankets and wears clothes; escapes naked when found in the morning |\n"
            "| **A theatrical shop, Drury Lane** | takes bandages, dark glasses, a false nose, whiskers and a hat; robs the shopkeeper |\n"
            "| **Iping village** | stays at the inn; is short of money, robs the clergyman; frightens Mrs Hall; fights Jaffers the constable and escapes |")

sections = [
 {"id": "s1", "title": "A man no one can see", "blocks": [
  blk("s1.hook", "hook", title="Fresh footprints, but no feet",
    body="Two boys in London see fresh, muddy footprints appearing on the steps of a house, one after another, but there is no one there!\n\n"
         "This is **Griffin**, a brilliant scientist who has made himself **invisible**. But being invisible is not as wonderful as it sounds: he is cold, hungry and hunted."),
  blk("s1.inspiration", "inspiration", title="The writer", person="H. G. Wells", years="1866–1946",
    body="**Herbert George Wells** was an English writer, often called a father of **science fiction**. His novels include The Time Machine, The War of the Worlds and **The Invisible Man** (1897), from which this chapter is taken.",
    future="Scientists and policy-makers today debate how to use powerful discoveries responsibly, the very question this story raises."),
  C.socratic("s1.socratic", "Griffin could have used his discovery for good. Why did invisibility make him a criminal instead?",
    ["He used it selfishly, to escape rules and take what he wanted", "Invisibility always makes people evil", "Other people forced him"], 0,
    "Science without values can be dangerous."),
 ]},
 {"id": "s2", "title": "The story", "blocks": [
  blk("s2.thm", "theory", title="What happens", revision=True,
    body="**The scientist:** **Griffin**, a brilliant but **lawless** scientist, discovers that by swallowing certain **rare drugs** his body can become as transparent as glass, that is, **invisible**.\n\n"
         "**In London:** his landlord dislikes him and tries to throw him out, so Griffin **sets fire to the house** in revenge. To escape unseen he takes off his clothes. Walking naked in the **cold of mid-winter**, he leaves **muddy footprints**; **two boys** are astonished to see footprints without feet.\n\n"
         "**The store and the shop:** he slips into a **big London store** at closing time, eats, sleeps and dresses in its clothes, but in the morning the assistants see him and he has to **undress and flee**. Then, in a **theatrical company's shop in Drury Lane**, he takes **bandages, dark glasses, a false nose, big bushy side-whiskers and a large hat**, and **robs the shopkeeper**, knocking him down from behind.\n\n"
         "**At Iping:** wrapped in bandages, he stays at the inn of the village of **Iping**, run by **Mrs Hall**. He keeps to himself and works with chemicals. Short of money, he **robs the house of the clergyman**, Mr Bunting, unseen. One morning Mrs Hall finds his room empty and his clothes lying about; the **furniture seems to fly at her**, and she thinks the room is haunted by **spirits**.\n\n"
         "**The escape:** the villagers grow suspicious. When **Mr Jaffers, the constable**, comes to arrest him, Griffin **takes off his bandages and clothes**, becomes invisible, fights off the crowd and **escapes**."),
  blk("s2.table", "markdown_table", title="Griffin's journey", revision=True, body=TIMELINE),
  C.kc("s2.check", "How did Griffin become invisible?",
    [("by swallowing certain rare drugs", ""), ("by wearing a magic coat", "By drugs."), ("by an accident in a fire", "By drugs."), ("by a spell", "By drugs.")],
    "He was a brilliant scientist.")
  ,C.kc("s2.check2", "Why did Griffin set fire to his landlord's house?",
    [("to take revenge, because the landlord wanted to evict him", ""), ("by accident", "It was revenge."), ("to keep warm", "It was revenge."), ("to test his drugs", "It was revenge.")],
    "It shows his lawless nature.")
 ]},
 {"id": "s3", "title": "Griffin and the message", "blocks": [
  blk("s3.thm", "theory", title="Character and theme", revision=True,
    body="**Griffin:** a **brilliant scientist**, but **lawless, selfish, short-tempered and violent**. He burns a house, robs shopkeepers and a clergyman, and attacks people. He has no respect for others or for the law.\n\n"
         "**The problems of invisibility:** he is **cold** without clothes, can be seen through **footprints**, mud and rain, and has to wear bandages and a false nose to appear in public. Invisibility brings him **loneliness and fear**, not happiness.\n\n"
         "**Humour:** Mrs Hall's belief in spirits, the clergyman's puzzled search, and the boys chasing footprints make the story amusing.\n\n"
         "**Theme:** **scientific power without moral values** is dangerous. A discovery should be used for the good of people, not for selfish, criminal ends."),
  C.kc("s3.check", "Which word best describes Griffin?",
    [("lawless", ""), ("kind", "He hurt people."), ("honest", "He stole."), ("patient", "He was short-tempered.")],
    "He broke every rule.")
  ,C.kc("s3.check2", "What problem did invisibility cause Griffin in winter?",
    [("he felt very cold, having to go without clothes", ""), ("he became visible again", "He stayed invisible."), ("he lost his memory", "He was cold."), ("he could not see", "He was cold.")],
    "Clothes would show him.")
 ]},
 {"id": "s4", "title": "Language of the story", "blocks": [
  blk("s4.thm", "theory", title="Words and expressions to know", revision=True,
    body="| Word or phrase | Meaning |\n|---|---|\n| **invisible** | cannot be seen |\n| **transparent** | clear, like glass |\n| **lawless** | not following any law |\n"
         "| **theatrical company** | a group that stages plays (its shop sells costumes and make-up) |\n| **side-whiskers** | hair grown on the sides of the face |\n| **constable** | a police officer |\n| **spirits** | ghosts |\n\n"
         "**Style:** third-person narration, fast action and gentle humour, typical of science fiction adventure."),
  C.kc("s4.check", "'Lawless' means:",
    [("not following any law", ""), ("a lawyer", "Without law."), ("very rich", "Without law."), ("living alone", "Without law.")],
    "Griffin broke the law again and again.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Griffin: drugs → invisible → burns landlord's house → naked footprints (2 boys).**\n- **Store (sleeps, dresses) → Drury Lane shop (bandages, glasses, nose, whiskers, hat) → robs shopkeeper.**\n"
         "- **Iping: inn (Mrs Hall) → robs clergyman → 'spirits' → Jaffers → escapes invisible.**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Calling Griffin a hero: he is a **lawless criminal**.\n2. Saying invisibility made him happy: it brought **cold, hunger and fear**.\n"
         "3. Mixing up places: London store, Drury Lane shop, then **Iping** village.\n4. Forgetting why he burnt the house: **revenge** on the landlord."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Make a 'wanted' poster for Griffin: list his crimes and describe how to recognise an invisible man (bandages, footprints, false nose)."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="If you could become invisible for one day, how would you use it responsibly?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **The Making of a Scientist:** a scientist who uses his gifts well.\n- **Science:** light, transparency and how we see objects."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="'Griffin was a brilliant scientist but a lawless man.' Discuss in about 120 words.\n\n"
         "**Model answer:** Griffin's discovery that rare drugs could make the human body invisible shows his brilliance as a scientist. But he uses this power only for selfish and criminal ends. When his landlord tries to evict him, he sets fire to the house. In London he steals food and clothes from a big store and robs a shopkeeper in Drury Lane, taking bandages, glasses and a false nose to disguise himself. At Iping he robs the clergyman and, when the constable comes to arrest him, he becomes invisible and fights his way out. He respects neither people nor the law. His story warns that science without moral values can make a genius dangerous to society."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Griffin, a scientist, becomes invisible by taking rare drugs.\n- He burns his landlord's house and wanders London naked, leaving footprints.\n"
         "- He hides in a store, then disguises himself with items stolen from a theatrical shop.\n- At Iping he robs a clergyman, frightens Mrs Hall and escapes arrest by becoming invisible.\n"
         "- Theme: science without morality is dangerous."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- Keep events in order: London house → streets → store → Drury Lane → Iping.\n- In character sketches use 'brilliant but lawless' with evidence.\n- Mention both the advantages and problems of invisibility."),
  blk("s5.flash1", "flashcard", front="Who was Griffin?", back="A brilliant but lawless scientist who made himself invisible with rare drugs."),
  blk("s5.flash2", "flashcard", front="What did Griffin take from the theatrical shop?", back="Bandages, dark glasses, a false nose, side-whiskers and a large hat."),
  blk("s5.flash3", "flashcard", front="Why did Mrs Hall think her inn was haunted?", back="Griffin's room was empty, clothes lay about, and furniture seemed to fly at her."),
  blk("s5.flash4", "flashcard", front="How did Griffin escape Jaffers?", back="He took off his bandages and clothes and became completely invisible."),
 ]},
]

# ---------------- NCERT ----------------
C.vsa("rf1", LONDON, "How did the invisible man first become visible?", ["He was seen through his muddy footprints in the London street.", "Two boys saw fresh footprints appearing without any feet."], RF(1))
C.sa("rf2", LONDON, "Why was he wandering the streets?", ["He had set fire to his landlord's house and had to escape unseen.", "He had taken off his clothes to stay invisible, so he wandered the cold streets."], RF(2))
C.sa("rf3", LONDON, "Why did Griffin set fire to his landlord's house?", ["The landlord disliked him and tried to evict him.", "In revenge Griffin set fire to the house, which also destroyed evidence of his work."], RF(3))
C.sa("rf4", LONDON, "What did he do in the big London store?", ["He hid there after closing, ate food and slept in blankets.", "He dressed in its clothes; in the morning he was seen and had to undress and escape."], RF(4))
C.sa("rf5", LONDON, "How did he get his disguise?", ["He went into a theatrical company's shop in Drury Lane.", "He took bandages, dark glasses, a false nose, whiskers and a hat, and robbed the shopkeeper."], RF(5))
C.sa("rf6", IPING, "Why did Mrs Hall think the furniture was haunted?", ["She found Griffin's room empty though his clothes and bandages lay about.", "The invisible Griffin made a chair and other things move, so she thought spirits were in the room."], RF(6))
C.sa("rf7", IPING, "What happened when Mr Jaffers came to arrest Griffin?", ["Griffin took off his bandages and clothes and became invisible.", "He fought Jaffers and the villagers and escaped."], RF(7))
C.la("ta1", GRIFFIN, "'Griffin was rather a lawless person.' Comment.",
     ["Griffin set fire to his landlord's house in revenge.", "He stole food and clothes from a London store.",
      "He knocked down and robbed a shopkeeper in Drury Lane.", "At Iping he robbed the clergyman and attacked the constable.",
      "He used his discovery only for selfish ends, with no respect for law or people."], TA(1))
C.la("ta2", SCIENCE, "How would you assess Griffin as a scientist?",
     ["Griffin was brilliant: he discovered how to make the human body invisible.", "But he did not think about the consequences or about others.",
      "He used his discovery for crime instead of for the good of society.", "A true scientist needs both knowledge and responsibility.",
      "So Griffin was a great scientist but a poor, even dangerous, human being."], TA(2))

# ---------------- Objective practice ----------------
C.m("mcq01", GRIFFIN, "Griffin was a:", [("scientist", ""), ("thief by profession", "A scientist who stole."), ("constable", "That is Jaffers."), ("clergyman", "That is Mr Bunting.")], "He made himself invisible.")
C.m("mcq02", GRIFFIN, "Griffin became invisible by:", [("swallowing rare drugs", ""), ("a magic ring", "Drugs."), ("an accident", "Deliberate drugs."), ("a coat", "Drugs.")], "His body became like glass.")
C.m("mcq03", LONDON, "Who saw Griffin's footprints?", [("two boys", ""), ("Mrs Hall", "Two boys in London."), ("the constable", "Two boys."), ("the clergyman", "Two boys.")], "Footprints without feet.")
C.m("mcq04", LONDON, "Why did Griffin feel cold?", [("it was mid-winter and he had no clothes", ""), ("he was ill", "No clothes in winter."), ("he lived in a cold country", "No clothes in winter."), ("the drugs made him cold", "No clothes in winter.")], "Clothes would make him visible.")
C.m("mcq05", LONDON, "Where did Griffin spend a night?", [("in a big London store", ""), ("in a hotel", "In a store."), ("in a church", "In a store."), ("in a police station", "In a store.")], "He ate and slept there.")
C.m("mcq06", LONDON, "Where did Griffin get his disguise?", [("a theatrical company's shop in Drury Lane", ""), ("Mrs Hall's inn", "In Drury Lane."), ("the big store", "In Drury Lane."), ("a hospital", "In Drury Lane.")], "Bandages, glasses, false nose.")
C.m("mcq07", IPING, "In which village did Griffin stay at an inn?", [("Iping", ""), ("Drury Lane", "That is in London."), ("Shotover", "Iping."), ("Lucknow", "Iping.")], "Mrs Hall ran the inn.")
C.m("mcq08", IPING, "Whose house did Griffin rob at Iping?", [("the clergyman's", ""), ("Mrs Hall's", "The clergyman's."), ("the constable's", "The clergyman's."), ("the landlord's", "The clergyman's.")], "He was short of money.")
C.m("mcq09", IPING, "Mrs Hall thought the furniture was moved by:", [("spirits", ""), ("the wind", "Spirits."), ("a thief", "She thought of spirits."), ("children", "Spirits.")], "It was really Griffin.")
C.m("mcq10", IPING, "Who came to arrest Griffin?", [("Mr Jaffers, the constable", ""), ("Mr Hall", "Jaffers."), ("the two boys", "Jaffers."), ("the clergyman", "Jaffers.")], "Griffin escaped.")
C.m("mcq11", GRIFFIN, "Griffin can best be described as:", [("brilliant but lawless", ""), ("kind and gentle", "Lawless."), ("honest and law-abiding", "Lawless."), ("lazy", "He was a brilliant scientist.")], "He misused science.")
C.m("mcq12", SCIENCE, "The theme of the story is:", [("science without moral values is dangerous", ""), ("invisibility is fun", "It brought him misery."), ("all scientists are criminals", "Only misuse is wrong."), ("winter is cold", "Science needs values.")], "Use discoveries responsibly.")
C.m("mcq13", LONDON, "Why did Griffin knock down the shopkeeper?", [("to rob him and escape with the disguise", ""), ("the shopkeeper attacked first", "Griffin attacked."), ("by mistake", "To rob him."), ("to save a child", "To rob him.")], "He took money too.")
C.m("mcq14", GRIFFIN, "Who wrote The Invisible Man?", [("H. G. Wells", ""), ("Ruskin Bond", "H. G. Wells."), ("James Herriot", "H. G. Wells."), ("Victor Canning", "H. G. Wells.")], "A father of science fiction.")
C.m("mcq15", LONDON, "What did Griffin do in the store in the morning?", [("he had to undress and escape when seen", ""), ("he paid for the clothes", "He fled."), ("he slept on", "He fled."), ("he surrendered", "He fled.")], "The assistants spotted him.")
C.m("mcq16", IPING, "How did Griffin escape the constable?", [("by taking off his clothes and becoming invisible", ""), ("by running into the forest", "He became invisible."), ("by bribing him", "He became invisible."), ("by hiding in the inn", "He became invisible.")], "No one could catch an invisible man.")
C.tf("tf1", GRIFFIN, "Griffin used his discovery to help people.", False, "He used it for crime.")
C.tf("tf2", LONDON, "Two boys saw Griffin's footprints in London.", True, "Footprints without feet.")
C.tf("tf3", IPING, "Mrs Hall ran the inn at Iping.", True, "Griffin stayed there.")
C.tf("tf4", LONDON, "Griffin felt warm and comfortable while invisible in winter.", False, "He suffered from the cold.")
C.tf("tf5", IPING, "Jaffers successfully arrested Griffin.", False, "Griffin became invisible and escaped.")
C.tf("tf6", LONDON, "Griffin burnt his landlord's house.", True, "In revenge.")

# ---------------- More ----------------
C.vsa("vsa1", GRIFFIN, "Name two problems Griffin faced because of invisibility.", ["He felt very cold without clothes.", "His footprints and any clothes he wore could give him away."])
C.vsa("vsa2", LONDON, "Name two items of Griffin's disguise.", ["Bandages and dark glasses.", "A false nose, whiskers and a large hat."])
C.vsa("vsa3", IPING, "Why did Griffin rob the clergyman?", ["He had run short of money at Iping.", "Being invisible, he could take money unseen."])
C.sa("sa1", IPING, "How did Griffin behave at the inn in Iping?",
     ["He kept to himself, wrapped in bandages, and worked with chemicals.", "He was rude and short-tempered with Mrs Hall and wanted to be left alone."])
C.sa("sa2", SCIENCE, "What are the advantages and disadvantages of being invisible, as shown in the story?",
     ["Advantage: Griffin could move and steal unseen, and escape arrest.", "Disadvantages: cold without clothes, footprints that betrayed him, and a lonely, hunted life."])
C.sa("sa3", IPING, "How did the people of Iping react to Griffin?",
     ["They were curious and suspicious of the bandaged stranger.", "After the robbery and Mrs Hall's fright, they tried to arrest him."])
C.sa("sa4", GRIFFIN, "Why is the story humorous though Griffin is a criminal?",
     ["Mrs Hall thinks spirits are moving her furniture.", "The clergyman and villagers search for a thief they cannot see, and boys chase footprints without feet."])
C.la("la1", GRIFFIN, "Write a character sketch of Griffin.",
     ["Griffin is a brilliant scientist who discovers how to become invisible.", "He is selfish and revengeful: he burns his landlord's house.",
      "He is a thief: he steals from a store, a theatrical shop and a clergyman.", "He is violent and short-tempered: he attacks a shopkeeper and the constable.",
      "He is lonely and hunted; he shows how genius without values becomes dangerous."])
C.la("la2", LONDON, "Describe Griffin's adventures in London.",
     ["After becoming invisible, Griffin burns his landlord's house in revenge.", "He walks naked through the cold streets; two boys follow his muddy footprints.",
      "He spends a night in a big store, eating and dressing, but must flee in the morning.", "In Drury Lane he steals a disguise from a theatrical shop and robs the shopkeeper.",
      "Disguised in bandages, glasses and a false nose, he leaves London for Iping."])
C.la("la3", SCIENCE, "Imagine you are Mrs Hall. Write a diary entry about the strange guest at your inn.",
     ["Date and first person; describe the bandaged stranger who wanted to be left alone.", "His rudeness, his chemicals and the robbery at the clergyman's house.",
      "The morning you found his room empty and the furniture flying at you.", "The day Jaffers came, the stranger vanished, and your fear and wonder."])

chapter = header("ch05", 24, "Footprints without Feet", "H. G. Wells", "prose",
                 ["griffin_in_london", "griffin_at_iping", "griffins_character", "science_and_responsibility"],
                 "CBSE 2025-26 English Language and Literature (184): Footprints without Feet, Chapter 5. Assessed through short answers in 40-50 words (3 marks) and a long answer in 100-120 words (6 marks); no extracts from this book.",
                 book="footprints")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
