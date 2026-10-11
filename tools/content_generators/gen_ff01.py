"""CBSE Class 10 English, First Flight Ch 1: A Letter to God (G. L. Fuentes)."""
import sys
from lit_common import make, header, path, ex, SHINE

ROOT = sys.argv[1]
PATH = path("ch01_a_letter_to_god")
C = make("ff10ch01")
blk = C.blk
PLOT, LENCHO, POST, IRONY, LANG = ["plot_and_setting"], ["lencho_faith"], ["postmaster_kindness"], ["irony_and_conflict"], ["vocabulary_and_style"]
OCC = lambda n: ex(n, "Oral Comprehension Check")

CHARS = ("| Character | Who he is | What he shows |\n|---|---|---|\n"
         "| **Lencho** | a hard-working farmer; his house is the only one in the valley, on the crest of a low hill | complete, unquestioning faith in God; simple and naive; ungrateful at the end |\n"
         "| **Lencho's wife** | runs the house and prepares supper | shares the family's hope and later its sorrow |\n"
         "| **The postman** | delivers letters | laughs heartily at a letter addressed to God |\n"
         "| **The postmaster** | 'a fat, amiable fellow' who runs the post office | kindness and goodwill; does not want to shake a man's faith |")
CONFLICT = ("| Conflict | Between | Shown by |\n|---|---|---|\n"
            "| **Human vs nature** | Lencho and the hailstorm | the hail destroys the ripe corn; 'a plague of locusts would have left more than this' |\n"
            "| **Human vs human** | Lencho and the post-office employees | Lencho calls the people who helped him 'a bunch of crooks' |")

sections = [
 {"id": "s1", "title": "Faith in hard times", "blocks": [
  blk("s1.hook", "hook", title="If you lost everything overnight",
    body="Imagine a farmer who has worked all year. His corn is ripe, the rain he prayed for has come, and then, in one hour, a storm of ice destroys everything. Where would he turn?\n\n"
         "In **A Letter to God**, the farmer Lencho turns to God, and writes Him a letter. What happens next is funny, touching and full of **irony**: the people who help him are the very people he ends up blaming."),
  blk("s1.inspiration", "inspiration", title="The writer", person="G. L. Fuentes", years="1897–1966",
    body="**Gregorio López y Fuentes** was a Mexican novelist, poet and journalist. He wrote about the lives of ordinary country people of Mexico, especially farmers who depend on rain and land.\n\n"
         "A Letter to God is set in the countryside, among people whose lives depend on one good harvest. It shows how faith, kindness and misunderstanding can sit side by side.",
    future="Reading stories closely builds the skills of journalists, lawyers, teachers, writers and anyone who must understand people."),
  C.socratic("s1.socratic", "The post-office employees help Lencho, yet he calls them crooks. What does this tell us?",
    ["Lencho's faith in God is so complete that he cannot imagine God making a mistake", "The employees really stole the money", "Lencho knew the employees had sent it"], 0,
    "Lencho is sure God sent 100 pesos, so he blames people. This is the central irony of the story."),
 ]},
 {"id": "s2", "title": "The story", "blocks": [
  blk("s2.thm", "theory", title="What happens in the story", revision=True,
    body="**1. Hope for rain.** Lencho's house is the only one in the valley, on the crest of a low hill. From there he can see the river and the field of **ripe corn** dotted with flowers, which always promises a good harvest. The earth needs only a downpour, or at least a shower. All morning he scans the sky towards the north-east.\n\n"
         "**2. The rain becomes hail.** At dinner time large drops of rain begin to fall. Lencho says they are like **new coins**: 'the big drops are ten cent pieces and the little ones are fives.' Then a strong wind begins to blow and very large **hailstones** fall. For an hour the hail falls on the house, the garden, the hillside, the cornfield and the whole valley. The field turns white, **'as if covered with salt'**. Not a leaf is left on the trees; the corn is totally destroyed. Lencho says, **'A plague of locusts would have left more than this.'**\n\n"
         "**3. Faith and the letter.** That night is sorrowful, but the family has one hope: help from God, because **'no one dies of hunger'**. Lencho, who believes God's eyes 'see everything, even what is deep in one's conscience', writes a letter to God asking for **a hundred pesos** to sow his field again and to live until the new crop comes. He addresses it 'To God' and posts it.\n\n"
         "**4. The postmaster's kindness.** The postman laughs at the letter and takes it to the **postmaster**, a fat, amiable fellow, who also laughs but then becomes serious. Admiring Lencho's faith, he decides to reply, so as **not to shake the writer's faith in God**. He collects money from his employees and friends and gives part of his own salary, but he can collect only a **little more than seventy pesos**. He puts the money in an envelope and signs the letter **'God'**.\n\n"
         "**5. The twist.** The next Sunday Lencho comes for his letter. He is **not surprised** to find money, so great is his confidence, but he becomes **angry** when he counts it: only seventy pesos. He writes again: God should send the rest, but not through the mail, **'because the post office employees are a bunch of crooks.'**"),
  blk("s2.table", "markdown_table", title="Characters at a glance", revision=True, body=CHARS),
  C.kc("s2.check", "Why did Lencho compare the raindrops to new coins?",
    [("He hoped the rain would bring a good harvest and money", ""), ("The raindrops were made of silver", "This is a comparison, not a fact."),
     ("He wanted to buy new coins", "He is thinking of his crop."), ("He was counting his savings", "He is watching the rain.")],
    "Rain meant a rich crop, so each drop seemed like money to him.")
  ,C.kc("s2.check2", "How much money did the postmaster manage to send?",
    [("a little more than seventy pesos", ""), ("exactly one hundred pesos", "He could not collect that much."),
     ("fifty pesos", "It was more than seventy."), ("nothing", "He did send money.")],
    "He collected from employees and friends and gave part of his salary.")
 ]},
 {"id": "s3", "title": "Themes, irony and conflict", "blocks": [
  blk("s3.thm", "theory", title="What the story means", revision=True,
    body="**Unquestioning faith:** Lencho's faith in God is complete. He writes to God as if to a friend, he is not surprised to get money, and he never doubts that God sent the full amount.\n\n"
         "**Kindness and goodwill:** the postmaster and his employees give their own money to a stranger, only to keep his faith alive. They act out of pure **goodwill** and sign as 'God', expecting no thanks.\n\n"
         "**Irony:** the people who help Lencho are the ones he calls **'a bunch of crooks'**. The reader knows the truth; Lencho does not. This is **dramatic irony**.\n\n"
         "**Two conflicts:** the story shows a conflict between **humans and nature** (the hailstorm destroys the crop) and between **humans and humans** (Lencho distrusts the post-office employees).\n\n"
         "**What kind of person is Lencho?** hard-working and simple; **naive** and **unquestioning** in faith; and, at the end, **ungrateful** without knowing it."),
  blk("s3.table", "markdown_table", title="Two kinds of conflict", revision=True, body=CONFLICT),
  C.kc("s3.check", "What is the main irony in the story?",
    [("Lencho calls the people who helped him crooks", ""), ("The hail looked like salt", "That is a comparison, not the irony."),
     ("Lencho's house was on a hill", "That is the setting."), ("The postman laughed", "That is a reaction, not the irony.")],
    "His helpers are blamed for 'stealing' money they gave out of kindness.")
  ,C.kc("s3.check2", "Why did the postmaster sign the letter 'God'?",
    [("so as not to shake Lencho's faith in God", ""), ("to make fun of Lencho", "He admired Lencho's faith."),
     ("because God told him to", "It was his own idea."), ("to avoid paying postage", "That has nothing to do with it.")],
    "He wanted Lencho to believe God had answered him.")
 ]},
 {"id": "s4", "title": "Language of the story", "blocks": [
  blk("s4.thm", "theory", title="Words and expressions to know", revision=True,
    body="| Word or phrase | Meaning in the story |\n|---|---|\n"
         "| **crest** | the top of a hill |\n| **downpour** | heavy rain |\n| **hailstones** | small balls of ice that fall like rain |\n"
         "| **plague of locusts** | a huge swarm of insects that eats crops; used to show the damage was even worse |\n"
         "| **'as if covered with salt'** | a simile: the white hail covered the field |\n| **an ox of a man** | a man who works as hard as an ox |\n"
         "| **amiable** | friendly and pleasant |\n| **conscience** | the inner sense of right and wrong |\n"
         "| **goodwill** | kindness and a wish to help |\n| **crooks** | dishonest people, cheats |\n\n"
         "**Figures of speech:** 'the big drops are ten cent pieces' (**metaphor**); 'as if covered with salt' (**simile**); the whole ending is **irony**."),
  C.kc("s4.check", "'An ox of a man' means a man who:",
    [("works very hard", ""), ("is very angry", "It is about hard work."), ("owns many oxen", "It is a comparison."), ("is very lazy", "It means the opposite.")],
    "Lencho worked like an animal in the fields.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Story in five words: Rain → Hail → Letter → Money → Crooks.**\n- **Numbers:** asked for **100** pesos, received **70**.\n"
         "- **Coins:** big drops = **ten-cent** pieces, little drops = **fives**.\n- **Simile:** field 'white, as if covered with **salt**'."),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Writing that the postmaster sent 100 pesos: he sent **a little more than seventy**.\n2. Saying the postmaster mocked Lencho: he laughed at first, but then **admired his faith**.\n"
         "3. Calling Lencho greedy: he is **naive and unquestioning**, not greedy; he asks only for what he needs to sow again.\n"
         "4. Missing the irony: the helpers are called crooks, which is the point of the ending."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Ask students to write the postmaster's diary entry for the day he read Lencho's letter, and then Lencho's diary for the day he received the money. Compare the two: this shows the irony clearly."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Have you ever helped someone who did not know it was you? How would you feel if that person blamed you? What would you do?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **The Sermon at Benares (Ch 8):** another story about how people face loss and grief.\n- **Footprints without Feet:** compare the honest postmaster with selfish Griffin.\n"
         "- **Analytical writing:** use the two conflicts as an example of how stories build tension."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="'Faith can move mountains.' How does this apply to Lencho? Answer in about 120 words.\n\n"
         "**Model answer:** Lencho's faith in God is complete. When the hailstorm destroys his corn, he does not lose hope; he writes a letter to God asking for a hundred pesos. His faith 'moves' the postmaster, who first laughs but then admires the farmer's belief. Not wanting to shake that faith, the postmaster collects money from his staff and friends and gives part of his own salary. So Lencho's belief makes strangers act with kindness. Yet the same faith blinds him: sure that God cannot make a mistake, he decides the post-office employees stole thirty pesos. Faith brings him help, but unquestioning faith also makes him ungrateful."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Lencho, a hard-working farmer, hopes for rain for his ripe corn; the rain turns into a hailstorm that destroys the crop.\n"
         "- With complete faith, he writes to God for 100 pesos.\n- The kind postmaster collects a little more than 70 pesos and signs the reply 'God' to keep Lencho's faith alive.\n"
         "- Lencho, angry at receiving less, asks God for the rest and calls the post-office employees 'a bunch of crooks'.\n"
         "- Themes: faith, goodwill, irony, and conflicts between humans and nature and among humans."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- **Short answers (3 marks, 40-50 words):** give two clear points from the story and one quotation or detail (for example 'as if covered with salt').\n"
         "- **Long answers (6 marks, 100-120 words):** state your view, support it with three or four events in order, and end with the irony or the lesson.\n"
         "- In extracts, read the question words carefully: 'who', 'why', 'which word means' and 'what does this show' need different kinds of answers."),
  blk("s5.flash1", "flashcard", front="How much did Lencho ask for, and how much did he get?", back="He asked for 100 pesos and got a little more than 70."),
  blk("s5.flash2", "flashcard", front="What did Lencho compare the raindrops to?", back="New coins: big drops were ten-cent pieces, little ones were fives."),
  blk("s5.flash3", "flashcard", front="Why did the postmaster sign the reply 'God'?", back="So as not to shake Lencho's faith in God."),
  blk("s5.flash4", "flashcard", front="What is the irony of the ending?", back="Lencho calls the people who helped him 'a bunch of crooks'."),
 ]},
]

# ---------------- NCERT: Oral Comprehension Check ----------------
C.vsa("occ1", PLOT, "What did Lencho hope for?", ["He hoped for rain, a downpour or at least a shower.", "His field of ripe corn needed rain for a good harvest."], OCC(1))
C.vsa("occ2", LANG, "Why did Lencho say the raindrops were like 'new coins'?",
      ["The rain promised a good harvest, which meant money.", "So the big drops seemed like ten-cent pieces and the little ones like fives."], OCC(2))
C.vsa("occ3", PLOT, "How did the rain change? What happened to Lencho's fields?",
      ["A strong wind began to blow and very large hailstones fell with the rain.", "The hail destroyed the corn completely; the field was white, as if covered with salt."], OCC(3))
C.vsa("occ4", LENCHO, "What were Lencho's feelings when the hail stopped?",
      ["His soul was filled with sadness: his crop was totally destroyed.", "He said a plague of locusts would have left more, and the family feared hunger."], OCC(4))
C.vsa("occ5", LENCHO, "Who or what did Lencho have faith in? What did he do?",
      ["He had complete faith in God.", "He wrote a letter to God asking for a hundred pesos and posted it."], OCC(5))
C.vsa("occ6", POST, "Who read the letter? What did the postmaster do then?",
      ["The postman found it and took it to the postmaster, who read it.", "Moved by Lencho's faith, the postmaster collected money from employees and friends and sent it, signed 'God'."], OCC(6))
C.vsa("occ7", LENCHO, "Was Lencho surprised to find a letter for him with money in it? What made him angry?",
      ["No, he was not surprised, so great was his confidence in God.", "He was angry because he got only seventy pesos instead of a hundred."], OCC(7))

# ---------------- NCERT: Thinking about the Text ----------------
C.sa("ex1", LENCHO, "Who does Lencho have complete faith in? Which sentences in the story tell you this?",
     ["Lencho has complete faith in God.", "'He had but one hope: help from God, whose eyes, as he had been instructed, see everything, even what is deep in one's conscience.'",
      "He was not surprised to see the money: 'Such was his confidence.'"], ex(1))
C.sa("ex2", POST, "Why does the postmaster send money to Lencho? Why does he sign the letter 'God'?",
     ["He admires Lencho's faith and wants to help a man in need.", "He signs it 'God' so as not to shake the writer's faith in God and to make Lencho believe God answered him."], ex(2))
C.sa("ex3", LENCHO, "Did Lencho try to find out who had sent the money to him? Why/Why not?",
     ["No, he did not.", "He was sure that God had sent it; he had no doubt at all, so it never occurred to him that people might have helped him."], ex(3))
C.sa("ex4", IRONY, "Who does Lencho think has taken the rest of the money? What is the irony in the situation?",
     ["He thinks the post-office employees took the rest and calls them 'a bunch of crooks'.",
      "The irony is that these very employees gave their own money to help him, and they are the ones he blames."], ex(4))
C.sa("ex5", LENCHO, "Are there people like Lencho in the real world? What kind of a person would you say he is? (Choose from: greedy, naive, stupid, ungrateful, selfish, comical, unquestioning.)",
     ["Yes, many simple people have such strong faith.", "Lencho is naive and unquestioning in his faith; he is also, without realising it, ungrateful to the people who helped him.",
      "He is hard-working, not greedy: he asks only for what he needs."], ex(5))
C.sa("ex6", IRONY, "There are two kinds of conflict in the story: between humans and nature, and between humans themselves. How are these conflicts illustrated?",
     ["Humans vs nature: the hailstorm destroys Lencho's ripe corn completely.", "Humans vs humans: Lencho distrusts the post-office employees and calls them crooks, though they helped him."], ex(6))

# ---------------- Extracts (board pattern: 5 marks) ----------------
C.extract("ext1", PLOT + LANG,
  "The air was fresh and sweet. The man went out for no other reason than to have the pleasure of feeling the rain on his body,\nand when he returned he exclaimed, \"These aren't raindrops falling from the sky, they are new coins.\nThe big drops are ten cent pieces and the little ones are fives.\"",
  [("Who is 'the man' in the extract?", "Lencho, the farmer."),
   ("Why did he go out?", "Just for the pleasure of feeling the rain on his body."),
   ("Why does he call the raindrops 'new coins'?", "Rain promised a good harvest, which meant money."),
   ("Name the figure of speech in 'they are new coins'.", "Metaphor."),
   ("What was his mood at this moment?", "Happy and hopeful.")])
C.extract("ext2", PLOT + LANG,
  "The field was white, as if covered with salt.\nNot a leaf remained on the trees. The corn was totally destroyed.\nThe flowers were gone from the plants. Lencho's soul was filled with sadness.",
  [("What made the field white?", "Hailstones."),
   ("Name the figure of speech in 'as if covered with salt'.", "Simile."),
   ("What happened to the corn?", "It was totally destroyed."),
   ("How did Lencho feel?", "Full of sadness."),
   ("What did Lencho say a plague of locusts would have done?", "It would have left more than this.")])
C.extract("ext3", POST,
  "But later, struck by the faith of the man who wrote it, he decided to answer the letter.\nBut when he opened it, it was evident that to answer it he needed something more than goodwill, ink and paper.\nBut he stuck to his resolution: he asked for money from his employees, he himself gave part of his salary.",
  [("Who is 'he' in the extract?", "The postmaster."),
   ("What struck him about the letter?", "The faith of the man who wrote it."),
   ("What else did he need besides goodwill, ink and paper?", "Money."),
   ("Give a word from the extract that means 'firm decision'.", "Resolution."),
   ("What quality of the postmaster does this show?", "Kindness and generosity.")])
C.extract("ext4", IRONY,
  "\"God: Of the money that I asked for, only seventy pesos reached me. Send me the rest, since I need it very much.\nBut don't send it to me through the mail because the post office employees are a bunch of crooks. Lencho.\"",
  [("Who wrote this letter, and to whom?", "Lencho wrote it to God."),
   ("How much money had he asked for?", "A hundred pesos."),
   ("Whom does he call 'a bunch of crooks'?", "The post-office employees."),
   ("What does 'crooks' mean?", "Dishonest people, cheats."),
   ("What is ironic about this letter?", "The people he calls crooks are the ones who gave him the money.")])

# ---------------- Extract-based objective items ----------------
C.m("mcq01", LANG, "'The field was white, as if covered with salt.' The figure of speech is:",
    [("simile", ""), ("metaphor", "There is 'as if', so it is a direct comparison: a simile."), ("personification", "Nothing is given human qualities."), ("alliteration", "No repeated first sounds.")],
    "'As if' introduces a comparison.")
C.m("mcq02", LANG, "'They are new coins.' Here the raindrops are compared to coins. This is a:",
    [("metaphor", ""), ("simile", "There is no 'like' or 'as'."), ("hyperbole", "It is a comparison, not an exaggeration."), ("pun", "There is no play on words.")],
    "The drops are called coins directly.")
C.m("mcq03", PLOT, "Where was Lencho's house?",
    [("on the crest of a low hill in the valley", ""), ("in a big city", "He lived in the countryside."), ("next to the post office", "He went to town to post the letter."), ("on the bank of the sea", "He could see a river.")],
    "It was the only house in the entire valley.")
C.m("mcq04", PLOT, "What did Lencho's field of corn need, according to him?",
    [("a downpour or at least a shower", ""), ("more fertiliser", "He was waiting for rain."), ("more workers", "His sons were working in the field."), ("a new plough", "He needed rain.")],
    "The ripe corn promised a good harvest if it rained.")
C.m("mcq05", PLOT, "'A plague of locusts would have left more than this.' Lencho means that:",
    [("the hail caused more damage than locusts would have", ""), ("locusts had attacked his field", "There were no locusts."),
     ("locusts are better than rain", "He is comparing the damage."), ("he wanted locusts to come", "He is sad, not wishing.")],
    "Locusts eat crops; the hail was even worse.")
C.m("mcq06", LENCHO, "Why did Lencho write a letter to God?",
    [("to ask for a hundred pesos to sow his field again and live until the next crop", ""), ("to complain about the postman", "He wrote the second letter about the employees."),
     ("to thank God for the rain", "The rain destroyed his crop."), ("to ask for a new house", "He needed money for seed and food.")],
    "He believed God sees everything and would help.")
C.m("mcq07", POST, "How is the postmaster described?",
    [("a fat, amiable fellow", ""), ("a thin, angry man", "He is fat and friendly."), ("a strict officer", "He is kind."), ("a greedy man", "He gives his own salary.")],
    "'Amiable' means friendly.")
C.m("mcq08", POST, "What did the postmaster first do on reading the letter?",
    [("he laughed, but then became serious and admired the writer's faith", ""), ("he tore it up", "He kept it and answered it."),
     ("he sent it back to Lencho", "He answered it."), ("he reported Lencho to the police", "He wanted to help.")],
    "He was struck by the faith of the man who wrote it.")
C.m("mcq09", POST, "How did the postmaster collect money for Lencho?",
    [("from his employees, his friends and part of his own salary", ""), ("from the government", "He collected it himself."),
     ("from Lencho's neighbours", "Lencho's was the only house in the valley."), ("from a bank loan", "He asked people he knew.")],
    "It was an 'act of charity'.")
C.m("mcq10", LENCHO, "How did Lencho react when he saw the money?",
    [("he was not surprised but became angry after counting it", ""), ("he was shocked and thanked the postmaster", "He never knew who sent it."),
     ("he returned the money", "He kept it and asked for more."), ("he cried with joy", "He was angry.")],
    "His confidence in God was so great that he expected it.")
C.m("mcq11", IRONY, "Whom did Lencho call 'a bunch of crooks'?",
    [("the post-office employees", ""), ("his neighbours", "He had no neighbours in the valley."), ("his sons", "They worked with him."), ("the moneylenders", "They are not in the story.")],
    "He thought they had taken thirty pesos.")
C.m("mcq12", LANG, "The word 'amiable' means:",
    [("friendly and pleasant", ""), ("angry", "It means the opposite."), ("lazy", "It describes his nature, not his work."), ("rich", "It is about behaviour.")],
    "The postmaster was an amiable, kind man.")
C.m("mcq13", LANG, "'An ox of a man, working like an animal in the fields' describes Lencho as:",
    [("very hard-working", ""), ("very strong but lazy", "He worked hard."), ("very cruel", "It describes his work."), ("very rich", "He was a poor farmer.")],
    "He worked tirelessly on his land.")
C.m("mcq14", LENCHO, "Which word best describes Lencho's faith?",
    [("unquestioning", ""), ("weak", "His faith never wavers."), ("pretended", "It is real."), ("doubtful", "He never doubts God.")],
    "He never questions God, even when he gets less money.")
C.m("mcq15", PLOT, "What did Lencho write on the envelope?",
    [("To God", ""), ("To the Postmaster", "He addressed it to God."), ("To the Mayor", "He addressed it to God."), ("To my wife", "He addressed it to God.")],
    "This made the postman laugh.")
C.m("mcq16", PLOT, "On which day did Lencho go to the post office for his reply?",
    [("the following Sunday", ""), ("the next morning", "He came on Sunday."), ("after a month", "He came the next Sunday."), ("he never went", "He went to collect it.")],
    "He came a bit earlier than usual.")
C.m("mcq17", IRONY, "The ending of the story is an example of:",
    [("irony", ""), ("tragedy", "It is not a sad death."), ("mystery", "The reader knows everything."), ("adventure", "It is about faith and kindness.")],
    "The outcome is the opposite of what one would expect.")
C.m("mcq18", PLOT, "What helped the family on the sorrowful night after the storm?",
    [("their hope of help from God", ""), ("a loan from a neighbour", "They had no neighbours."), ("the postmaster's visit", "He never met them."), ("money saved earlier", "They had only hope.")],
    "'No one dies of hunger,' they said.")
C.m("mcq19", POST, "Why did the postmaster call the reply 'an act of charity'?",
    [("because the money was given freely to help someone in need", ""), ("because it was paid by the government", "People gave it themselves."),
     ("because Lencho repaid it", "He never did."), ("because it was a loan", "It was a gift.")],
    "It was given without expecting anything in return.")
C.m("mcq20", LENCHO, "What did Lencho do after counting the money?",
    [("he wrote another letter asking God for the rest", ""), ("he bought seed at once", "He first wrote again."), ("he went home happy", "He was angry."), ("he thanked the postmaster", "He did not know about him.")],
    "He licked the stamp and pasted it with a blow of his fist.")
C.m("mcq21", LANG, "Which word in the story means 'the top of a hill'?",
    [("crest", ""), ("valley", "That is low land."), ("ridge", "Not the word used."), ("slope", "That is the side.")],
    "'The house was on the crest of a low hill.'")
C.m("mcq22", POST, "The postmaster's action shows:",
    [("goodwill and kindness", ""), ("selfishness", "He gave his own money."), ("anger", "He admired Lencho."), ("fear", "He acted freely.")],
    "He helped a stranger without any reward.")
C.tf("tf1", POST, "The postmaster managed to send a full hundred pesos to Lencho.", False, "He could send only a little more than seventy pesos.")
C.tf("tf2", LENCHO, "Lencho was surprised to receive the money.", False, "He was not surprised; such was his confidence in God.")
C.tf("tf3", PLOT, "The hailstorm lasted for about an hour.", True, "For an hour the hail rained on the house, garden, hillside and cornfield.")
C.tf("tf4", IRONY, "Lencho knew that the post-office employees had collected the money.", False, "He believed God sent it, and blamed the employees for the shortfall.")

# ---------------- More written practice ----------------
C.sa("sa1", PLOT, "Describe the hailstorm and its effect on Lencho's field.",
     ["A strong wind blew and very large hailstones fell for an hour on the house, garden, hillside and cornfield.",
      "The field became white, as if covered with salt; not a leaf was left and the corn was destroyed.", "Lencho was filled with sadness."])
C.sa("sa2", POST, "What kind of person was the postmaster? Give two reasons.",
     ["He was kind and generous: he gave part of his own salary.", "He respected faith: he signed the letter 'God' so as not to shake Lencho's belief."])
C.sa("sa3", LENCHO, "Why did Lencho think the post-office employees were crooks?",
     ["He was sure God had sent the full hundred pesos.", "When he got only seventy, he decided someone in the post office must have stolen the rest."])
C.sa("sa4", IRONY, "'Lencho was not surprised; such was his confidence.' Explain.",
     ["Lencho believed so completely in God that he expected the reply and the money.", "So he felt no surprise, only anger when the amount was less."])
C.sa("sa5", PLOT, "What did the family do on the night after the storm?",
     ["The night was sorrowful; they feared they would go hungry that year.", "Their only hope was help from God: 'no one dies of hunger'."])
C.la("la1", POST + IRONY, "The postmaster and his employees showed true humanity. Do you agree? Explain with reference to the story.",
     ["Yes. The postmaster first laughed at a letter to God but was soon struck by the writer's faith.",
      "Needing more than goodwill, ink and paper, he collected money from his employees and friends and gave part of his own salary.",
      "He signed the reply 'God' so that Lencho's faith would not be shaken, and expected no thanks.",
      "Even when Lencho called them crooks, their kindness remains: they helped a stranger out of pure goodwill.",
      "Their humanity makes the ending ironic and touching."])
C.la("la2", LENCHO + IRONY, "Write a character sketch of Lencho.",
     ["Lencho is a hard-working farmer, 'an ox of a man', who knows his fields and the weather.",
      "He is hopeful: he calls raindrops new coins.", "His faith in God is complete and unquestioning; after the hail he writes a letter to God for a hundred pesos.",
      "He is naive: he never wonders who sent the money.", "At the end he is unknowingly ungrateful, calling his helpers 'a bunch of crooks'."])
C.la("la3", IRONY, "Imagine you are the postmaster. Write a diary entry about the day you read Lencho's second letter.",
     ["Date and a heading; first-person voice.", "Describe opening the second letter and reading that only seventy pesos reached him.",
      "Feelings: hurt and amused at being called a crook, yet happy that Lencho's faith was not shaken.",
      "Reflection: the act of charity was worth it; goodness does not need thanks."])

chapter = header("ch01", 1, "A Letter to God", "G. L. Fuentes", "prose",
                 ["plot_and_setting", "lencho_faith", "postmaster_kindness", "irony_and_conflict", "vocabulary_and_style"],
                 "CBSE 2025-26 English Language and Literature (184): First Flight prose, Chapter 1. Assessed through extracts (5 marks), short answers in 40-50 words (3 marks) and long answers in 100-120 words (6 marks).")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
