"""CBSE Class 10 English, Footprints without Feet Ch 4: A Question of Trust (Victor Canning)."""
import sys
from lit_common import make, header, path, ex

ROOT = sys.argv[1]
PATH = path("ch04_a_question_of_trust", "footprints")
C = make("fwf10ch04")
blk = C.blk
HORACE, ROBBERY, LADY, IRONY = ["horace_danby"], ["the_robbery_plan"], ["the_lady_in_red"], ["irony_and_trust"]
RF = lambda n: ex(n, "Read and Find Out")
TA = lambda n: ex(n, "Think about It")

TWIST = ("| What Horace believed | What was true |\n|---|---|\n"
         "| the young woman was the lady of the house | she was a **clever thief** pretending |\n"
         "| she was letting him go out of kindness | she wanted him to **open the safe for her** |\n"
         "| he was the one robbing the house | he was **robbed of the jewels** and left his **fingerprints** |\n"
         "| he could trust her | the 'question of trust' ends with **Horace in prison** |")

sections = [
 {"id": "s1", "title": "An honest thief?", "blocks": [
  blk("s1.hook", "hook", title="Robbed by a robber",
    body="Horace Danby is a respectable man who steals only once a year, very carefully, to buy rare books. This year he plans the perfect robbery. Everything goes smoothly, until a charming young woman in red walks in.\n\n"
         "By the end, the thief has been tricked by a cleverer thief. Can a thief trust a thief?"),
  blk("s1.inspiration", "inspiration", title="The writer", person="Victor Canning", years="1911–1986",
    body="**Victor Canning** was a popular English writer of thrillers, mysteries and children's books. His stories are known for clever plots and surprise endings.",
    future="Lawyers, police and security experts study how criminals are tricked by their own over-confidence."),
  C.socratic("s1.socratic", "Horace thought he could trust the young woman. Why is it ironic that a thief trusts a stranger?",
    ["He made his living by deceiving others, yet he himself was deceived", "Thieves never trust anyone", "She was his relative"], 0,
    "The title asks whether trust exists among thieves."),
 ]},
 {"id": "s2", "title": "The story", "blocks": [
  blk("s2.thm", "theory", title="What happens", revision=True,
    body="**Horace Danby:** about **fifty**, **unmarried**, a good and respectable citizen. He makes **locks** and is a skilled locksmith. But once a year he robs a house, carefully planned, to buy **rare and expensive books**, which he loves. He has done this for years without being caught.\n\n"
         "**The plan:** this year he plans to rob **Shotover Grange**, where a **safe** holds jewels. He has studied the house, knows the family is away and the servants are out, and has made friends with the family dog, **Sherry**. He gets into the house easily and finds the safe behind a painting.\n\n"
         "**The lady in red:** as he works, a **young, pretty woman dressed in red** appears at the door. She behaves as if she is the **lady of the house**. Instead of calling the police, she says she will let him go if he does something for her: she has forgotten the combination and wants her jewels, so would he open the safe? Horace suffers from **hay fever**, and the flowers make him sneeze, which adds to his nervousness.\n\n"
         "**The trick:** charmed and relieved, Horace opens the safe **with his bare hands** and gives her the jewels. She thanks him and he leaves.\n\n"
         "**The end:** two days later Horace is **arrested**. His **fingerprints** are all over the safe; the jewels are gone. The woman was not the lady of the house but **another thief**, who used him. No one believes his story. In prison he works as assistant **librarian**, and thinks bitterly of the charming woman who **cheated** him."),
  blk("s2.table", "markdown_table", title="Belief and truth", revision=True, body=TWIST),
  C.kc("s2.check", "Why did Horace steal once a year?",
    [("to buy rare and expensive books", ""), ("to pay his debts", "To buy rare books."), ("to help the poor", "To buy rare books."), ("for excitement only", "To buy rare books.")],
    "He loved books.")
  ,C.kc("s2.check2", "Who was the young woman in red really?",
    [("a clever thief who tricked Horace", ""), ("the lady of the house", "She only pretended."), ("a police officer", "She was a thief."), ("Horace's niece", "She was a thief.")],
    "She used Horace to open the safe.")
 ]},
 {"id": "s3", "title": "Characters and irony", "blocks": [
  blk("s3.thm", "theory", title="Why the title fits", revision=True,
    body="**Horace Danby:** careful, skilled and proud of his planning; lives a respectable life apart from his yearly theft. His weakness is **over-confidence** and **trusting** a stranger. He thinks of himself as an honest man in all other ways.\n\n"
         "**The lady in red:** young, charming and **cunning**; a better actor than Horace is a thief. She keeps calm, plays the role of the owner and lets Horace do the work and leave the evidence.\n\n"
         "**Irony:** a thief who cheats others is himself cheated; the man who plans every detail ends in prison because of one moment of trust. He is caught for a theft he did not profit from.\n\n"
         "**Title:** 'A Question of Trust' asks: can a thief trust anyone? Horace trusted the woman and lost. The story also shows that **crime does not pay**: careful planning cannot protect a wrongdoer for ever."),
  C.kc("s3.check", "What is the main irony of the story?",
    [("a thief is cheated by another thief", ""), ("Horace becomes rich", "He goes to prison."), ("the police are fooled", "Horace is arrested."), ("the dog steals the jewels", "The woman takes them.")],
    "The deceiver is deceived.")
  ,C.kc("s3.check2", "Why was Horace caught?",
    [("his fingerprints were on the safe", ""), ("the dog barked", "The dog was friendly."), ("the woman called the police at once", "His fingerprints betrayed him."), ("a servant saw him", "His fingerprints.")],
    "He had opened the safe with bare hands.")
 ]},
 {"id": "s4", "title": "Language of the story", "blocks": [
  blk("s4.thm", "theory", title="Words and expressions to know", revision=True,
    body="| Word or phrase | Meaning |\n|---|---|\n| **respectable** | regarded as honest and decent |\n| **safe** | a strong locked box for valuables |\n"
         "| **combination** | the secret number that opens a safe |\n| **hay fever** | an allergy to pollen or flowers that causes sneezing |\n| **fingerprints** | marks left by fingers, used as evidence |\n"
         "| **honour among thieves** | the idea that criminals are loyal to each other (shown false here) |\n\n**Style:** third-person narration, a light, ironic tone and a surprise ending."),
  C.kc("s4.check", "'Hay fever' is:",
    [("an allergy causing sneezing", ""), ("a high temperature from hard work", "It is an allergy."), ("a kind of farm", "It is an allergy."), ("fear of the police", "It is an allergy.")],
    "Flowers made Horace sneeze.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Horace: ~50, unmarried, locksmith, steals once a year for rare books.**\n- **Target: Shotover Grange; safe behind a painting; dog Sherry.**\n"
         "- **Lady in red → 'open the safe' → bare hands → fingerprints → prison librarian.**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying the woman owned the house: she was **another thief**.\n2. Saying Horace kept the jewels: **she** took them.\n"
         "3. Saying Horace was caught on the spot: he was **arrested two days later** through fingerprints.\n4. Forgetting why he stole: to buy **rare books**."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Ask students to retell the story from the woman's point of view: how did she plan to use Horace?"),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Can a good purpose (like buying books) justify a wrong act (like stealing)? Give your view."),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **The Thief's Story:** a thief changed by trust.\n- **The Midnight Visitor:** a criminal outwitted by a quick mind."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="Explain the irony in 'A Question of Trust' in about 120 words.\n\n"
         "**Model answer:** Horace Danby is a respectable locksmith who steals once a year to buy rare books. He plans every detail of the robbery at Shotover Grange: the family is away, the servants are out, and he has befriended the dog. Yet his careful plan is ruined by a charming young woman in red who pretends to be the lady of the house. She persuades him to open the safe for her, and he does so with bare hands. She takes the jewels; he is arrested two days later because his fingerprints are on the safe. The irony is that a thief who deceives others is deceived by another thief, and goes to prison for jewels he never kept. The story shows that there is no honour among thieves and that crime does not pay."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Horace Danby, a respectable locksmith, steals once a year to buy rare books.\n- He plans to rob the safe at Shotover Grange while the family is away.\n"
         "- A young woman in red, pretending to be the owner, makes him open the safe and takes the jewels.\n- Horace's fingerprints lead to his arrest; no one believes his story.\n"
         "- Theme: a thief cheated by a thief; crime does not pay."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- Explain the title and the irony together.\n- In character sketches, show both sides of Horace: respectable and dishonest.\n- Mention the fingerprints as the reason for his arrest."),
  blk("s5.flash1", "flashcard", front="Why did Horace steal?", back="To buy rare and expensive books, once a year."),
  blk("s5.flash2", "flashcard", front="How was Horace caught?", back="His fingerprints were on the safe he opened with bare hands."),
  blk("s5.flash3", "flashcard", front="Who was the lady in red?", back="A clever thief who pretended to be the lady of the house."),
  blk("s5.flash4", "flashcard", front="What is the irony of the story?", back="A thief is cheated by another thief and goes to prison for jewels he never kept."),
 ]},
]

# ---------------- NCERT ----------------
C.vsa("rf1", HORACE, "Who was Horace Danby? Was he a typical thief?", ["Horace Danby was a respectable, unmarried locksmith of about fifty.", "No; he stole only once a year, with great care, to buy rare books."], RF(1))
C.sa("rf2", ROBBERY, "Where did Horace get the money to buy rare books? Why did he plan his robberies so carefully?",
     ["He got it by robbing one house a year.", "He planned carefully so that he would never be caught and could keep his respectable life."], RF(2))
C.sa("rf3", ROBBERY, "Who saw Horace enter the house? Who was Sherry?",
     ["No one saw him enter; he thought the family and servants were away.", "Sherry was the family dog, whom Horace had made friends with so that she would not bark."], RF(3))
C.sa("rf4", LADY, "Who was the lady in red? What did she ask Horace to do?",
     ["She was a young, charming woman who pretended to be the lady of the house.", "She asked him to open the safe, saying she had forgotten the combination."], RF(4))
C.sa("rf5", IRONY, "How was Horace caught? Why did no one believe him?",
     ["His fingerprints were found on the safe and he was arrested.", "His story about the lady in red seemed impossible to prove; she had disappeared with the jewels."], RF(5))
C.la("ta1", IRONY, "Horace Danby was a thief. Was he a respectable man too? Explain the double life he led, and how it ended.",
     ["Horace was a respectable locksmith who lived quietly, employed men and was liked by people.", "But once a year he robbed a house to buy rare books he loved.",
      "He planned each theft carefully and was never caught for many years.", "His downfall came when he trusted a woman who was a cleverer thief than he.",
      "He ended in prison as assistant librarian, showing that a double life cannot last."], TA(1))
C.la("ta2", LADY, "Did you suspect that the lady was not the person she said she was? When did you realise the truth? What clues are there?",
     ["The woman was too calm on finding a thief in her house.", "She did not call the police but asked him to open the safe for her.",
      "It was strange that the owner had forgotten her own combination.", "The truth is clear only when Horace is arrested and the jewels are gone.",
      "Like Horace, readers are charmed and fooled, which makes the ending a surprise."], TA(2))
C.sa("ta3", IRONY, "Why is the story called 'A Question of Trust'?",
     ["Horace, a thief, trusted a stranger who seemed to be the owner.", "She betrayed that trust; the title asks whether trust is possible among thieves."], TA(3))

# ---------------- Objective practice ----------------
C.m("mcq01", HORACE, "Horace Danby was by profession a:", [("locksmith", ""), ("librarian", "That was in prison."), ("policeman", "A locksmith."), ("bookseller", "He bought books.")], "He made locks.")
C.m("mcq02", HORACE, "Horace stole once a year to:", [("buy rare books", ""), ("pay his workers", "To buy rare books."), ("go on holiday", "To buy rare books."), ("buy jewels", "To buy rare books.")], "He loved books.")
C.m("mcq03", HORACE, "Horace was about:", [("fifty years old", ""), ("twenty", "About fifty."), ("thirty", "About fifty."), ("seventy", "About fifty.")], "Unmarried and respectable.")
C.m("mcq04", ROBBERY, "Which house did Horace plan to rob?", [("Shotover Grange", ""), ("Camusfeàrna", "That is Maxwell's home."), ("Mrs Pumphrey's house", "Shotover Grange."), ("a bank", "Shotover Grange.")], "The family was away.")
C.m("mcq05", ROBBERY, "Where was the safe?", [("behind a painting", ""), ("under the bed", "Behind a painting."), ("in the kitchen", "Behind a painting."), ("in the garden", "Behind a painting.")], "In the drawing room.")
C.m("mcq06", ROBBERY, "Who was Sherry?", [("the family dog", ""), ("the lady in red", "She was a thief."), ("a servant", "The dog."), ("Horace's sister", "The dog.")], "Horace had made friends with her.")
C.m("mcq07", LADY, "The young woman was dressed in:", [("red", ""), ("black", "Red."), ("white", "Red."), ("blue", "Red.")], "The 'lady in red'.")
C.m("mcq08", LADY, "What did the woman ask Horace to do?", [("open the safe", ""), ("leave at once", "She asked him to open the safe."), ("call the police", "She wanted the safe opened."), ("feed the dog", "Open the safe.")], "She said she had forgotten the combination.")
C.m("mcq09", IRONY, "Horace was caught because of:", [("his fingerprints", ""), ("the dog's barking", "His fingerprints."), ("a camera", "His fingerprints."), ("his sneezing", "His fingerprints.")], "He used bare hands.")
C.m("mcq10", HORACE, "Horace suffered from:", [("hay fever", ""), ("a weak heart", "Hay fever."), ("poor eyesight", "Hay fever."), ("deafness", "Hay fever.")], "Flowers made him sneeze.")
C.m("mcq11", IRONY, "In prison Horace worked as:", [("assistant librarian", ""), ("a cook", "Assistant librarian."), ("a locksmith", "Assistant librarian."), ("a guard", "Assistant librarian.")], "Near the books he loved.")
C.m("mcq12", IRONY, "The theme of the story is that:", [("crime does not pay; a thief can be cheated by a thief", ""), ("books are expensive", "Crime does not pay."), ("dogs are friendly", "Crime does not pay."), ("women are honest", "Crime does not pay.")], "There is no honour among thieves.")
C.m("mcq13", LADY, "The lady in red was:", [("a clever thief", ""), ("the owner of the house", "She only pretended."), ("a policewoman", "A thief."), ("Horace's friend", "A thief.")], "She fooled Horace.")
C.m("mcq14", HORACE, "Horace's main weakness was:", [("over-confidence and trusting a stranger", ""), ("laziness", "Over-confidence."), ("anger", "Over-confidence."), ("greed for jewels", "He wanted books.")], "He trusted the woman.")
C.m("mcq15", IRONY, "When was Horace arrested?", [("two days later", ""), ("immediately", "Two days later."), ("after a year", "Two days later."), ("never", "He was arrested.")], "Through fingerprints.")
C.m("mcq16", HORACE, "Horace was:", [("unmarried", ""), ("married with children", "Unmarried."), ("a widower", "Unmarried."), ("engaged to the lady", "Unmarried.")], "He lived a quiet life.")
C.tf("tf1", LADY, "The lady in red was the owner of Shotover Grange.", False, "She was another thief.")
C.tf("tf2", HORACE, "Horace stole only once a year.", True, "To buy rare books.")
C.tf("tf3", IRONY, "Horace kept the jewels he stole.", False, "The woman took them.")
C.tf("tf4", IRONY, "Horace's fingerprints led to his arrest.", True, "He opened the safe with bare hands.")
C.tf("tf5", ROBBERY, "The family was at home when Horace entered.", False, "They were away.")
C.tf("tf6", IRONY, "Horace became a librarian's assistant in prison.", True, "He still loved books.")

# ---------------- More ----------------
C.vsa("vsa1", HORACE, "Give two facts about Horace's respectable life.", ["He was a skilled locksmith with a business.", "He was liked and lived a quiet, decent life."])
C.vsa("vsa2", LADY, "Give two clues that the lady in red was not the owner.", ["She was too calm and did not call the police.", "She 'forgot' the combination of her own safe."])
C.sa("sa1", ROBBERY, "How had Horace prepared for the robbery?",
     ["He studied the house and knew the family was away and the servants were out.", "He made friends with the dog Sherry and found the safe behind a painting."])
C.sa("sa2", LADY, "How did the woman make Horace open the safe?",
     ["She pretended to be the lady of the house and said she would not call the police.", "She charmingly asked for help, saying she had forgotten the combination."])
C.sa("sa3", IRONY, "Why did no one believe Horace's story?",
     ["The woman had vanished with the jewels, leaving no trace.", "Only his fingerprints were on the safe, so the story sounded like an excuse."])
C.sa("sa4", HORACE, "Do you think Horace was a good man? Give reasons.",
     ["He was respectable, hardworking and loved books, which shows some good qualities.", "But stealing, even for books, is wrong; his good side cannot excuse his crime."])
C.vsa("vsa3", ROBBERY, "Why did Horace make friends with Sherry?", ["So that the dog would not bark when he entered.", "It was part of his careful planning."])
C.sa("sa5", IRONY, "'There is no honour among thieves.' How does the story prove this?",
     ["The lady in red, a thief, used Horace, another thief, to open the safe.", "She took the jewels and let him take the blame and go to prison."])
C.sa("sa6", HORACE, "Why did Horace take off his gloves, and what did it cost him?",
     ["He opened the safe with bare hands, relaxed because he believed the woman was the owner.", "This left his fingerprints on the safe, which led to his arrest."])
C.la("la1", HORACE, "Write a character sketch of Horace Danby.",
     ["Horace is about fifty, unmarried, a respected locksmith.", "He loves rare books and steals once a year to buy them.",
      "He is careful and methodical, planning each theft in detail.", "But he is over-confident and too trusting: a charming woman fools him easily.",
      "He ends in prison, a victim of his own double life."])
C.la("la2", LADY, "Describe the role of the lady in red in Horace's downfall.",
     ["She appears while Horace is at the safe, dressed in red and calm.", "She pretends to be the owner and promises not to call the police.",
      "She asks him to open the safe, as she has 'forgotten' the combination.", "He opens it with bare hands; she takes the jewels and disappears.",
      "His fingerprints remain; he is arrested while she escapes, a cleverer thief."])
C.la("la3", IRONY, "Imagine you are Horace in prison. Write a diary entry about the lady in red.",
     ["Date and first person; describe your careful plan for Shotover Grange.", "Meeting the charming lady in red and believing she was the owner.",
      "Opening the safe for her and your arrest two days later.", "Your bitterness at being cheated, and your thoughts about trust and crime."])

chapter = header("ch04", 23, "A Question of Trust", "Victor Canning", "prose",
                 ["horace_danby", "the_robbery_plan", "the_lady_in_red", "irony_and_trust"],
                 "CBSE 2025-26 English Language and Literature (184): Footprints without Feet, Chapter 4. Assessed through short answers in 40-50 words (3 marks) and a long answer in 100-120 words (6 marks); no extracts from this book.",
                 book="footprints")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
