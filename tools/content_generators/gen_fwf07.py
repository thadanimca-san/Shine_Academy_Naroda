"""CBSE Class 10 English, Footprints without Feet Ch 7: The Necklace (Guy de Maupassant)."""
import sys
from lit_common import make, header, path, ex

ROOT = sys.argv[1]
PATH = path("ch07_the_necklace", "footprints")
C = make("fwf10ch07")
blk = C.blk
MATILDA, BALL, LOSS, IRONY = ["matildas_discontent"], ["the_ball"], ["loss_and_repayment"], ["irony_and_pride"]
RF = lambda n: ex(n, "Read and Find Out")
TA = lambda n: ex(n, "Think about It")

MONEY = ("| Item | Amount |\n|---|---|\n| money M. Loisel had saved for a gun, spent on the dress | **400 francs** |\n"
         "| price of the replacement diamond necklace | **36,000 francs** |\n| inheritance from Loisel's father | **18,000 francs** |\n"
         "| the rest | **borrowed** at high interest |\n| time taken to repay | **ten years** |\n| real value of the lost necklace | at most **500 francs** (it was **paste**) |")

sections = [
 {"id": "s1", "title": "One night of glory, ten years of toil", "blocks": [
  blk("s1.hook", "hook", title="A borrowed necklace",
    body="Matilda dreams of luxury she cannot afford. For one glittering evening she looks like a rich lady in a borrowed diamond necklace. Then the necklace is lost, and she and her husband spend **ten years** paying for it.\n\n"
         "The last line of the story turns everything upside down."),
  blk("s1.inspiration", "inspiration", title="The writer", person="Guy de Maupassant", years="1850–1893",
    body="**Guy de Maupassant** was a French writer and one of the masters of the **short story**. His stories show ordinary people with realism and often end with a sharp **twist**. 'The Necklace' is his most famous.",
    future="Financial advisers warn against living beyond one's means; this story shows why."),
  C.socratic("s1.socratic", "Why did Matilda not tell her friend the truth at once?",
    ["Pride and fear of being thought a thief or careless", "She did not know her friend's address", "Her husband forbade her"], 0,
    "Her pride cost her ten years."),
 ]},
 {"id": "s2", "title": "The story", "blocks": [
  blk("s2.thm", "theory", title="What happens", revision=True,
    body="**Matilda's discontent:** **Matilda (Mme Loisel)** is pretty and charming but was born into a family of clerks. She marries a **petty clerk** in the Ministry of Public Instruction. She is always **unhappy**, dreaming of a rich, elegant life with fine furniture, dinners and admirers.\n\n"
         "**The invitation:** her husband, **M. Loisel**, proudly brings an **invitation to a ball** given by the Minister. Matilda cries: she has **no suitable dress**. He gives her the **400 francs** he had saved to buy a **gun** for shooting trips with friends.\n\n"
         "**The necklace:** then she worries that she has **no jewels**. On her husband's suggestion she visits her rich friend **Mme Forestier**, who lends her a beautiful **diamond necklace**.\n\n"
         "**The ball:** Matilda is the **most beautiful** woman there; all the men notice her, and she dances in delight until four in the morning.\n\n"
         "**The loss:** at home she finds the necklace is **gone**. Loisel searches the streets, the police and the cab companies, but it is not found. They write to Mme Forestier that the clasp is being mended, to gain time.\n\n"
         "**The replacement:** they find a similar diamond necklace at a jeweller's for **36,000 francs**. Loisel uses his **18,000-franc inheritance** and **borrows** the rest. They return the necklace without telling Mme Forestier.\n\n"
         "**Ten years of poverty:** they dismiss the servant and move to an attic. Matilda does all the heavy housework; Loisel works in the evenings copying documents. After **ten years** the debt is paid, but Matilda looks old, rough and worn.\n\n"
         "**The twist:** one Sunday she meets Mme Forestier, still young and beautiful, and tells her the whole story. Mme Forestier, deeply moved, says: **'Oh, my poor Matilda! But mine was false. It was not worth over five hundred francs!'**"),
  blk("s2.table", "markdown_table", title="The cost of the necklace", revision=True, body=MONEY),
  C.kc("s2.check", "What did Matilda borrow from Mme Forestier?",
    [("a diamond necklace", ""), ("a dress", "She bought the dress."), ("money", "A necklace."), ("a carriage", "A necklace.")],
    "She had no jewels for the ball.")
  ,C.kc("s2.check2", "How long did the Loisels take to repay the debt?",
    [("ten years", ""), ("one year", "Ten years."), ("five years", "Ten years."), ("twenty years", "Ten years.")],
    "It ruined Matilda's youth and beauty.")
 ]},
 {"id": "s3", "title": "Characters, irony and theme", "blocks": [
  blk("s3.thm", "theory", title="Why the ending hurts", revision=True,
    body="**Matilda:** beautiful but **discontented, proud and materialistic**; she longs for wealth and admiration. Later she shows **courage and honesty**: she works hard for ten years to repay the debt.\n\n"
         "**M. Loisel:** a simple, **loving and self-sacrificing** husband. He gives up his gun money and his inheritance and works day and night for her.\n\n"
         "**Mme Forestier:** a rich, generous friend who lends the necklace without hesitation.\n\n"
         "**Irony:** Matilda borrowed the necklace to look rich for one night; she spent ten years in poverty replacing a necklace that was **fake**. Had she told the truth, the whole suffering could have been avoided.\n\n"
         "**Theme:** **pride, vanity and false appearances** lead to ruin; **honesty** is the best policy; contentment matters more than show."),
  C.kc("s3.check", "What is the central irony of the story?",
    [("the lost necklace was fake, but they paid for a real one", ""), ("Matilda became rich", "She became poor."), ("the necklace was found", "It was never found."), ("Mme Forestier was poor", "She was rich.")],
    "Ten years wasted for a paste necklace.")
  ,C.kc("s3.check2", "Which quality led to the Loisels' ruin?",
    [("pride that stopped Matilda from telling the truth", ""), ("laziness", "They worked hard."), ("greed for money", "Pride, not greed."), ("bad luck alone", "Pride made it worse.")],
    "Honesty would have saved them.")
 ]},
 {"id": "s4", "title": "Language of the story", "blocks": [
  blk("s4.thm", "theory", title="Words and expressions to know", revision=True,
    body="| Word or phrase | Meaning |\n|---|---|\n| **petty clerk** | a junior, low-paid office worker |\n| **ball** | a grand dancing party |\n| **franc** | French unit of money |\n"
         "| **paste** | glass used to make imitation jewels |\n| **clasp** | the fastening of a necklace |\n| **attic** | a room just under the roof |\n| **ruinous** | causing complete loss |\n\n"
         "**Style:** realistic third-person narration and a famous **twist ending**."),
  C.kc("s4.check", "A 'paste' necklace is:",
    [("an imitation made of glass", ""), ("made of real diamonds", "It is imitation."), ("made of gold", "Imitation glass."), ("a necklace of flowers", "Imitation glass.")],
    "Mme Forestier's necklace was paste.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **400 francs (gun money) → dress. Borrowed necklace → ball → lost.**\n- **Replacement 36,000 francs = 18,000 inheritance + loans → 10 years of toil.**\n- **Twist: 'Mine was false… not worth over five hundred francs!'**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying the necklace was found: it was **never found**.\n2. Saying Mme Forestier knew about the loss: they **hid it** for ten years.\n"
         "3. Saying the lost necklace was real: it was **paste**.\n4. Forgetting Loisel's sacrifices: gun money, inheritance, night work."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Rewrite the ending: what if Matilda had told Mme Forestier the truth the next morning? Students write the new final paragraph."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Have you ever pretended to be something you are not? What did it cost you?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **A Question of Trust:** another story with a twist about deception.\n- **Economics (Money and Credit):** the burden of borrowing at high interest."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="'Matilda's pride and vanity ruined her life.' Discuss in about 120 words.\n\n"
         "**Model answer:** Matilda, a clerk's wife, was always unhappy because she longed for luxury. When invited to the Minister's ball, she wanted to look rich, so she spent her husband's 400 francs on a dress and borrowed a diamond necklace from Mme Forestier. She shone at the ball, but lost the necklace. Too proud to admit the loss, she and her husband bought a replacement for 36,000 francs, using his inheritance and heavy loans. For ten years they lived in poverty; Matilda did hard housework and lost her beauty. Finally she learnt that the original necklace was fake, worth only 500 francs. Her pride and vanity, not bad luck, cost her ten years of her life."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Matilda, wife of a petty clerk, longs for luxury.\n- Invited to a ball, she buys a dress and borrows a diamond necklace from Mme Forestier.\n"
         "- She shines at the ball but loses the necklace.\n- The Loisels replace it for 36,000 francs and spend ten years repaying the debt.\n"
         "- Mme Forestier reveals the necklace was fake. Theme: pride and false show lead to ruin; honesty matters."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- Quote the key amounts correctly (400, 36,000, 18,000, 500 francs; ten years).\n- Explain the irony of the ending.\n- In character sketches, show Matilda's change from vanity to hard work."),
  blk("s5.flash1", "flashcard", front="What did Matilda borrow for the ball?", back="A diamond necklace from her friend Mme Forestier."),
  blk("s5.flash2", "flashcard", front="How much did the replacement necklace cost?", back="36,000 francs."),
  blk("s5.flash3", "flashcard", front="What was the real value of the lost necklace?", back="At most 500 francs; it was paste (imitation)."),
  blk("s5.flash4", "flashcard", front="What sacrifice did M. Loisel make first?", back="He gave Matilda the 400 francs he had saved to buy a gun."),
 ]},
]

# ---------------- NCERT ----------------
C.sa("rf1", MATILDA, "What kind of a person is Mme Loisel? Why is she unhappy?", ["She is pretty and charming but discontented and materialistic.", "She is unhappy because she is married to a petty clerk and cannot have the luxury she dreams of."], RF(1))
C.sa("rf2", MATILDA, "What kind of a person is her husband?", ["M. Loisel is simple, content and loving.", "He sacrifices his gun money and later his inheritance for her."], RF(2))
C.sa("rf3", BALL, "What fresh problem now disturbs Mme Loisel? How is the problem solved?", ["After getting a dress, she is upset that she has no jewels.", "She borrows a diamond necklace from her friend Mme Forestier."], RF(3))
C.sa("rf4", LOSS, "What did the Loisels do after they lost the necklace?", ["Loisel searched the streets, the police and the cab companies.", "They wrote to Mme Forestier that the clasp was being mended and bought a replacement for 36,000 francs."], RF(4))
C.sa("rf5", LOSS, "How did the Loisels pay for the replacement necklace?", ["Loisel used his 18,000-franc inheritance and borrowed the rest.", "They lived in poverty for ten years, working hard to repay the loans."], RF(5))
C.la("ta1", IRONY, "The course of the Loisels' life changed because of the necklace. Comment.",
     ["The Loisels lived modestly but comfortably before the ball.", "Matilda borrowed a necklace to look rich for one evening and lost it.",
      "To replace it they spent 36,000 francs, using an inheritance and loans.", "For ten years they lived in an attic and worked hard, and Matilda lost her beauty.",
      "Ironically, the lost necklace was fake; one evening's vanity changed their whole life."], TA(1))
C.la("ta2", IRONY, "What would have happened to Matilda if she had confessed to her friend that she had lost her necklace?",
     ["Mme Forestier would have told her that the necklace was fake.", "Matilda would have had to pay at most 500 francs.",
      "The Loisels would not have borrowed 36,000 francs or lived in poverty for ten years.", "Matilda would have kept her youth and beauty.",
      "Honesty would have saved them; pride ruined them."], TA(2))
C.sa("ta3", MATILDA, "If you were caught in a situation like this, how would you have dealt with it?",
     ["I would tell my friend the truth at once and apologise.", "Together we could find a fair solution instead of hiding the loss for years."], TA(3))

# ---------------- Objective practice ----------------
C.m("mcq01", MATILDA, "Matilda's husband worked as:", [("a petty clerk in the Ministry of Public Instruction", ""), ("a jeweller", "A clerk."), ("a minister", "A clerk."), ("a doctor", "A clerk.")], "A modest job.")
C.m("mcq02", BALL, "The invitation was to a ball given by:", [("the Minister", ""), ("Mme Forestier", "The Minister."), ("the king", "The Minister."), ("a jeweller", "The Minister.")], "Loisel was proud of it.")
C.m("mcq03", BALL, "M. Loisel had saved 400 francs to buy:", [("a gun", ""), ("a horse", "A gun."), ("a necklace", "A gun."), ("a house", "A gun.")], "For shooting with friends.")
C.m("mcq04", BALL, "Matilda borrowed the necklace from:", [("Mme Forestier", ""), ("her mother", "Mme Forestier."), ("a jeweller", "She bought the replacement there."), ("the Minister's wife", "Mme Forestier.")], "Her rich friend.")
C.m("mcq05", BALL, "At the ball, Matilda:", [("was the most admired woman", ""), ("felt ignored", "She was admired."), ("left early", "She danced till four."), ("lost her dress", "She lost the necklace later.")], "Her night of glory.")
C.m("mcq06", LOSS, "The replacement necklace cost:", [("36,000 francs", ""), ("400 francs", "That was the dress."), ("500 francs", "That was the real value."), ("18,000 francs", "That was the inheritance.")], "They borrowed heavily.")
C.m("mcq07", LOSS, "How long did the Loisels work to repay their debts?", [("ten years", ""), ("two years", "Ten years."), ("five years", "Ten years."), ("their whole life", "Ten years.")], "Matilda grew old.")
C.m("mcq08", IRONY, "The lost necklace was actually:", [("made of paste, worth at most 500 francs", ""), ("made of real diamonds", "It was fake."), ("found later", "Never found."), ("stolen by Loisel", "It was lost.")], "The final twist.")
C.m("mcq09", LOSS, "What excuse did they give Mme Forestier while searching?", [("the clasp was being mended", ""), ("Matilda was ill", "The clasp."), ("they had moved house", "The clasp."), ("they were travelling", "The clasp.")], "To gain time.")
C.m("mcq10", LOSS, "After the loss, Matilda:", [("did all the hard housework herself", ""), ("hired more servants", "They dismissed the servant."), ("went to more balls", "She worked hard."), ("left her husband", "She worked with him.")], "She showed courage.")
C.m("mcq11", MATILDA, "Matilda can best be described as:", [("vain and discontented", ""), ("content and humble", "She was discontented."), ("dishonest and cruel", "She was vain, not cruel."), ("lazy throughout", "She worked hard later.")], "She longed for luxury.")
C.m("mcq12", MATILDA, "M. Loisel can best be described as:", [("loving and self-sacrificing", ""), ("selfish", "He sacrificed much."), ("rich", "He was a clerk."), ("cruel", "He was loving.")], "He gave up his gun money.")
C.m("mcq13", IRONY, "The theme of the story is:", [("pride and false show lead to ruin", ""), ("diamonds are beautiful", "Pride leads to ruin."), ("balls are fun", "Pride leads to ruin."), ("clerks are poor", "Pride leads to ruin.")], "Honesty is the best policy.")
C.m("mcq14", LOSS, "Loisel's inheritance from his father was:", [("18,000 francs", ""), ("36,000 francs", "The necklace cost that."), ("400 francs", "That was the gun money."), ("nothing", "18,000 francs.")], "He borrowed the rest.")
C.m("mcq15", IRONY, "Where did Matilda meet Mme Forestier after ten years?", [("on a walk on a Sunday", ""), ("at another ball", "On a Sunday walk."), ("at the jeweller's", "On a Sunday walk."), ("at the Ministry", "On a Sunday walk.")], "Mme Forestier hardly recognised her.")
C.m("mcq16", LOSS, "Where did the Loisels move after the loss?", [("to an attic", ""), ("to a palace", "An attic."), ("to the countryside", "An attic."), ("to Mme Forestier's house", "An attic.")], "They lived in poverty.")
C.tf("tf1", LOSS, "The Loisels found the lost necklace.", False, "It was never found.")
C.tf("tf2", IRONY, "The lost necklace was made of real diamonds.", False, "It was paste, worth at most 500 francs.")
C.tf("tf3", BALL, "Matilda was a great success at the ball.", True, "She was the most admired woman.")
C.tf("tf4", BALL, "M. Loisel gave up the money saved for a gun.", True, "He gave Matilda 400 francs for a dress.")
C.tf("tf5", LOSS, "Matilda told Mme Forestier the truth at once.", False, "She hid it for ten years.")
C.tf("tf6", LOSS, "The Loisels took ten years to repay their debts.", True, "Matilda grew old and worn.")

# ---------------- More ----------------
C.vsa("vsa1", BALL, "What two things did Matilda need for the ball?", ["A suitable dress.", "Jewels."])
C.vsa("vsa2", LOSS, "Name two changes in Matilda's life after the loss.", ["She moved to an attic and did hard housework.", "She lost her youth and beauty."])
C.vsa("vsa3", IRONY, "What did Mme Forestier say at the end?", ["'Oh, my poor Matilda! But mine was false.'", "It was not worth over five hundred francs."])
C.sa("sa1", MATILDA, "Why was Matilda always unhappy?",
     ["She felt she was born for luxury but married a petty clerk.", "She dreamt of rich furniture, fine dinners and admirers, and hated her simple home."])
C.sa("sa2", LOSS, "How did Matilda change during the ten years?",
     ["She worked hard at heavy housework, bargaining for every coin.", "She became strong but rough and old-looking, losing her beauty."])
C.sa("sa3", IRONY, "Why is the ending of the story ironic?",
     ["The Loisels spent ten years paying for a real diamond necklace.", "The one they lost was fake and worth very little."])
C.sa("sa4", MATILDA, "What lesson does the story teach?",
     ["We should be content with what we have and not live beyond our means.", "Honesty would have saved the Loisels years of hardship."])
C.sa("sa5", MATILDA, "What sacrifices did M. Loisel make for his wife?",
     ["He gave her the 400 francs he had saved for a gun.", "He used his inheritance, borrowed money and worked extra in the evenings for ten years."])
C.sa("sa6", BALL, "Describe Matilda at the ball.",
     ["She was the prettiest woman there, elegant and smiling.", "All the men noticed her, and she danced with joy until four in the morning."])
C.la("la1", MATILDA, "Write a character sketch of Matilda Loisel.",
     ["Matilda is pretty and charming, born into a family of clerks.", "She is discontented and vain, always dreaming of luxury.",
      "Her pride stops her from confessing the loss of the necklace.", "Yet she shows courage: she works hard for ten years to repay the debt.",
      "Her story shows how vanity can ruin life, though hardship also builds strength."])
C.la("la2", MATILDA, "Write a character sketch of M. Loisel.",
     ["M. Loisel is a simple petty clerk, content with his life.", "He loves his wife and tries to please her by getting the ball invitation.",
      "He sacrifices his gun money, and later his inheritance, for her.", "He works day and night for ten years to repay the debt.",
      "He is a model of patience, love and self-sacrifice."])
C.la("la3", LOSS, "Imagine you are Matilda. Write a diary entry on the day you learnt the necklace was fake.",
     ["Date and first person; meeting Mme Forestier on a Sunday walk.", "Telling her the story of the ball, the loss and the ten years of toil.",
      "Her words: the necklace was false, worth at most 500 francs.", "Your shock, regret at your pride, and the lesson of honesty."])

chapter = header("ch07", 26, "The Necklace", "Guy de Maupassant", "prose",
                 ["matildas_discontent", "the_ball", "loss_and_repayment", "irony_and_pride"],
                 "CBSE 2025-26 English Language and Literature (184): Footprints without Feet, Chapter 7. Assessed through short answers in 40-50 words (3 marks) and a long answer in 100-120 words (6 marks); no extracts from this book.",
                 book="footprints")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
