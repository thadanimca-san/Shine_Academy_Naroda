"""CBSE Class 10 English, First Flight Ch 9: The Proposal (Anton Chekhov), a one-act play."""
import sys
from lit_common import make, header, path, ex

ROOT = sys.argv[1]
PATH = path("ch09_the_proposal")
C = make("ff10ch09")
blk = C.blk
PLOT, CHARS, QUARREL, HUMOUR, LANG = ["plot_of_the_play"], ["characters"], ["the_two_quarrels"], ["humour_and_satire"], ["vocabulary_and_style"]

CHARTAB = ("| Character | Who | Traits |\n|---|---|---|\n"
           "| **Ivan Vassilevitch Lomov** | a neighbour of Chubukov, a large and hearty but very suspicious landowner, 35 | nervous, a hypochondriac (palpitations, numb foot, twitching eyebrow), quarrelsome |\n"
           "| **Stepan Stepanovitch Chubukov** | a landowner | hypocritical and greedy: welcomes Lomov warmly, then insults him; wants his daughter married off |\n"
           "| **Natalya Stepanovna** | Chubukov's daughter, 25 | sharp-tongued, quarrelsome, possessive about property; desperate to marry when she learns of the proposal |")
QUARRELS = ("| | First quarrel | Second quarrel |\n|---|---|---|\n"
            "| **About** | **Oxen Meadows** | the dogs **Guess** (Lomov's) and **Squeezer** (Chubukov's) |\n"
            "| **Lomov says** | the meadows are his; his aunt's grandmother gave the peasants of Natalya's grandfather free use of them | Guess is the better dog; he paid **125 roubles** for him |\n"
            "| **Natalya says** | the meadows have always belonged to her family | Squeezer is better; Guess is **overshot** (lower jaw shorter than the upper) |\n"
            "| **Result** | Chubukov joins in, insults Lomov, who leaves; then Natalya learns he came to propose and demands he be brought back | Lomov collapses; Chubukov makes them kiss and agree to marry, and they start quarrelling again |")

sections = [
 {"id": "s1", "title": "A proposal that turns into a fight", "blocks": [
  blk("s1.hook", "hook", title="He came to propose, and argued about a meadow",
    body="A nervous young landowner puts on his evening dress and goes to his neighbour's house to ask for the daughter's hand. But before he can say the words, the two of them are shouting about who owns a meadow, and then whose dog is better!\n\n"
         "**The Proposal** is a comic one-act play by **Anton Chekhov** that laughs at people who care more about property and pride than about love."),
  blk("s1.inspiration", "inspiration", title="The playwright", person="Anton Chekhov", years="1860–1904",
    body="**Anton Pavlovich Chekhov** was a Russian doctor and one of the greatest writers of short stories and plays. He wrote with gentle humour about ordinary people. The Proposal (1888–89) is a **farce**, a comedy built on exaggerated characters and ridiculous situations, which satirises the 19th-century Russian landowning class and marriages made for property.",
    future="Playwrights, actors and screenwriters study Chekhov to learn how to build comedy from character."),
  C.socratic("s1.socratic", "Why does Lomov want to marry Natalya, according to his own words?",
    ["She is a good housekeeper, not bad-looking, well educated, and he needs to marry at 35", "He is deeply in love with her", "Her father forces him"], 0,
    "His reasons are practical, not romantic, which is part of the satire.")
 ]},
 {"id": "s2", "title": "The play, scene by scene", "blocks": [
  blk("s2.thm", "theory", title="What happens", revision=True,
    body="**Lomov arrives:** Lomov comes to Chubukov's house in **evening dress**. Chubukov, suspicious at first that he has come to borrow money, is overjoyed when Lomov says he wants to ask for Natalya's hand: 'I've always loved you, my angel, as if you were my own son.' He goes to call Natalya.\n\n"
         "**Lomov's nerves:** alone, Lomov worries: he is **35**, a 'critical age'; Natalya is an excellent housekeeper, not bad-looking and well educated. He suffers from **palpitations**, his **foot goes numb**, his **eyebrow twitches** and he cannot sleep.\n\n"
         "**The first quarrel, Oxen Meadows:** Natalya enters in an apron, thinking he has come on business. Lomov starts to explain his family's connection with hers and mentions that his **Oxen Meadows** touch her birchwoods. Natalya says the Meadows are **hers**. They argue hotly; Chubukov joins in, and they hurl insults at each other ('intriguer', 'pettifogger', grandfathers who drank and played cards). Lomov leaves, clutching his heart.\n\n"
         "**The truth comes out:** Chubukov tells Natalya that Lomov had come to **propose**. Natalya becomes hysterical: 'Bring him back! Back!' Chubukov fetches him.\n\n"
         "**The second quarrel, the dogs:** Natalya, now careful, changes the subject to hunting, but they soon quarrel over whose dog is better: Lomov's **Guess** or Chubukov's **Squeezer**. Lomov says Squeezer is **overshot**; Natalya says Guess is old and ugly. Chubukov joins in again. Lomov collapses into an armchair; Chubukov thinks he is **dead**.\n\n"
         "**The 'happy' ending:** Lomov revives. Chubukov makes them kiss and declares, 'She's willing!' and calls for **champagne**. But within moments they are arguing about the dogs again, and Chubukov shouts, 'Champagne!' to drown them out. The marriage is fixed, but the quarrels will clearly continue."),
  blk("s2.table", "markdown_table", title="The characters", revision=True, body=CHARTAB),
  C.kc("s2.check", "What did Chubukov first suspect Lomov had come for?",
    [("to borrow money", ""), ("to propose", "He did not guess at first."), ("to buy his dog", "He suspected a loan."), ("to sell the meadows", "He suspected a loan.")],
    "He resolved not to give it.")
  ,C.kc("s2.check2", "What is Lomov's complaint about his health?",
    [("palpitations, a numb foot, a twitching eyebrow and sleeplessness", ""), ("a broken leg", "His complaints are nervous ones."),
     ("a bad cough only", "He lists many nervous symptoms."), ("he is perfectly healthy", "He is a hypochondriac.")],
    "He is very nervous and easily excited.")
 ]},
 {"id": "s3", "title": "The quarrels and the comedy", "blocks": [
  blk("s3.thm", "theory", title="Why the play is funny", revision=True,
    body="**Satire:** the play mocks the **landowning class** of 19th-century Russia, for whom marriage was a matter of **property** and convenience. Lomov proposes for practical reasons; Chubukov wants to marry off his daughter; Natalya wants a husband, but not at the cost of losing a meadow.\n\n"
         "**Farce:** exaggerated characters and situations: a man fainting over a dog, a father who swings from 'my angel' to 'intriguer' in minutes, a woman who screams 'Bring him back!'\n\n"
         "**Irony:** a proposal, meant to bring two families together, makes them fight; the 'happy ending' is followed at once by another quarrel.\n\n"
         "**Character contrast:** all three are **quarrelsome**, proud and stubborn, which is why Chubukov says, 'Here begins the period of conjugal bliss!' The joke is that their marriage will be one long argument."),
  blk("s3.table", "markdown_table", title="The two quarrels", revision=True, body=QUARRELS),
  C.kc("s3.check", "What are the two quarrels about?",
    [("Oxen Meadows and the dogs Guess and Squeezer", ""), ("money and a horse", "Meadows and dogs."), ("a wedding date and a dowry", "Meadows and dogs."), ("a house and a carriage", "Meadows and dogs.")],
    "Both show their pride and possessiveness.")
  ,C.kc("s3.check2", "The Proposal is best described as:",
    [("a farce that satirises marriage for property", ""), ("a tragedy", "It is a comedy."), ("a romantic love story", "Love is the last thing on their minds."), ("a detective play", "It is a comedy.")],
    "Exaggeration and quarrels drive the humour.")
 ]},
 {"id": "s4", "title": "Language of the play", "blocks": [
  blk("s4.thm", "theory", title="Words and expressions to know", revision=True,
    body="| Word or phrase | Meaning |\n|---|---|\n| **hypochondriac** | a person who always worries about being ill |\n| **palpitations** | a fast, strong heartbeat |\n"
         "| **overshot** | (of a dog) with the lower jaw shorter than the upper |\n| **intriguer** | a person who plots secretly |\n| **pettifogger** | a person who argues over trivial things |\n"
         "| **conjugal bliss** | married happiness (said ironically) |\n| **evening dress** | formal clothes for a special occasion |\n\n"
         "**Stage directions** in brackets (for example *[Kisses him]*, *[Faints]*) show actions and add to the comedy."),
  C.kc("s4.check", "'Here begins the period of conjugal bliss!' is said:",
    [("ironically, as the couple starts quarrelling again", ""), ("sincerely, as they are very happy", "They are fighting."), ("by Lomov", "Chubukov says it."), ("at the start of the play", "At the end.")],
    "Their married life will be full of quarrels.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Three characters: Lomov (35, nervous), Chubukov (father), Natalya (25).**\n- **Two quarrels: Meadows, then Dogs (Guess vs Squeezer).**\n"
         "- **Lomov's body: heart (palpitations), foot (numb), eyebrow (twitch).**\n- **Guess cost 125 roubles; Squeezer is 'overshot'.**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying Lomov proposed at once: he never gets to propose properly; the meadows come first.\n2. Mixing up the dogs: **Guess** is Lomov's, **Squeezer** is Chubukov's.\n"
         "3. Calling it a love story: it is a **farce** and **satire** on marriages for property.\n4. Forgetting the ending: they are engaged but quarrelling again."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Perform the second quarrel as a three-person reading. Students mark every stage direction and act it out; then discuss how the actions make the scene funny."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Have you seen people argue over something small and forget what really matters? What does the play suggest about pride?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Footprints without Feet:** another comic look at human behaviour.\n- **History (Rise of Nationalism in Europe):** 19th-century landed aristocracy in Europe."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="'The Proposal is a satire on the landowning class of Russia.' Explain in about 120 words.\n\n"
         "**Model answer:** Chekhov uses The Proposal to laugh at rich landowners who value property above feelings. Lomov wants to marry Natalya not out of love but because, at 35, he needs a wife, and she is a good housekeeper and not bad-looking. Chubukov is eager to get his daughter married and is friendly only while it suits him. Yet as soon as Lomov mentions Oxen Meadows, all three forget the proposal and fight bitterly over a small piece of land, and then over which dog is better. Insults about grandfathers and family follow. Even after the engagement they quarrel again. The play shows that pride and possessiveness make these people ridiculous, and that marriages based on property are unlikely to be happy."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Lomov, a nervous 35-year-old landowner, comes in evening dress to propose to Natalya, his neighbour Chubukov's daughter.\n"
         "- Before proposing he quarrels with Natalya over Oxen Meadows; Chubukov joins in and Lomov leaves.\n"
         "- Learning he came to propose, Natalya demands he be brought back; they then quarrel over the dogs Guess and Squeezer.\n"
         "- Lomov faints; on reviving he is made to kiss Natalya; they are engaged but begin quarrelling again.\n"
         "- The play is a farce satirising marriage for property and the pride of landowners."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- Keep the order of events: arrival, nerves, meadows quarrel, truth, dogs quarrel, faint, engagement, new quarrel.\n- Use the words farce, satire and irony in long answers.\n"
         "- Character sketches: two traits each with an example from the play."),
  blk("s5.flash1", "flashcard", front="Who are the three characters?", back="Lomov, Chubukov and Chubukov's daughter Natalya."),
  blk("s5.flash2", "flashcard", front="What are the two quarrels about?", back="Oxen Meadows, and whether Guess or Squeezer is the better dog."),
  blk("s5.flash3", "flashcard", front="What does 'overshot' mean?", back="Having the lower jaw shorter than the upper; Lomov says this of Squeezer."),
  blk("s5.flash4", "flashcard", front="How does the play end?", back="Lomov and Natalya are engaged, but start quarrelling again; Chubukov calls for champagne."),
 ]},
]

C.sa("ex1", CHARS, "What does Chubukov at first suspect that Lomov has come for? Is he sincere when he later says, 'And I've always loved you, my angel, as if you were my own son'?",
     ["He suspects Lomov has come to borrow money and resolves not to give it.", "He is not sincere: he flatters Lomov because he wants Natalya married, and soon insults him."], ex(1))
C.sa("ex2", CHARS, "Chubukov says of Natalya: '... as if she won't consent! She's in love; egad, she's like a lovesick cat...' Would you agree? Find reasons for your answer.",
     ["Not exactly: she quarrels fiercely with Lomov over the meadows and the dogs.", "But she is eager to marry: when she learns he came to propose she cries, 'Bring him back!'"], ex(2))
C.sa("ex3", QUARREL, "Find all the words and expressions in the play that the characters use to speak about each other, and the accusations and insults they hurl at each other.",
     ["Chubukov calls Lomov an 'intriguer', 'pettifogger', 'malicious' and 'a puppy'; Lomov calls Chubukov 'a land-grabber'.", "They insult each other's families: grandfathers who drank or played cards, a 'hunchbacked' aunt."], ex(3))
C.sa("ex4", HUMOUR, "Why does Lomov say he must marry, and what are his feelings about Natalya?",
     ["He is 35, a critical age, and needs a quiet, regular life; he is nervous and cannot sleep.", "He thinks Natalya is an excellent housekeeper, not bad-looking and well educated, not that he loves her."])

C.extract("ext1", CHARS,
  "LOMOV: It's cold... I'm trembling all over, just as if I'd got an examination before me.\nThe chief thing is, I must make up my mind. If I give myself time to think, to hesitate, to talk a lot, to look for an ideal, or for real love, then I'll never get married.",
  [("Why is Lomov trembling?", "He is nervous about proposing to Natalya."),
   ("To what does he compare his feeling?", "Taking an examination."),
   ("What does he think will happen if he waits for 'real love'?", "He will never get married."),
   ("What does this show about his reason for marrying?", "It is practical, not romantic."),
   ("Find a word that means 'to pause before deciding'.", "Hesitate.")])
C.extract("ext2", QUARREL,
  "NATALYA: Oxen Meadows are ours! ... You can't talk like that! I'm surprised at you...\nLOMOV: I'll prove to you that they're mine!",
  [("What are the two arguing about?", "Who owns Oxen Meadows."),
   ("Why had Lomov come to the house?", "To propose to Natalya."),
   ("What does the quarrel show about both?", "They are proud, stubborn and possessive."),
   ("Who joins the quarrel next?", "Chubukov, Natalya's father."),
   ("What is ironic here?", "A proposal visit turns into a fight.")])
C.extract("ext3", HUMOUR,
  "CHUBUKOV: She's willing! Kiss and be happy! ... Here begins the period of conjugal bliss! Champagne!",
  [("Who is willing?", "Natalya, to marry Lomov."),
   ("What does 'conjugal bliss' mean?", "Married happiness."),
   ("Why is the remark ironic?", "Lomov and Natalya start quarrelling again immediately."),
   ("Why does Chubukov call for champagne?", "To celebrate, and to drown out their quarrel."),
   ("What kind of play does this ending suit?", "A farce or comedy.")])

C.m("mcq01", CHARS, "How old is Lomov?",
    [("35", ""), ("25", "That is Natalya's age."), ("45", "He is 35."), ("30", "He is 35.")],
    "He calls it a critical age.")
C.m("mcq02", CHARS, "What is Lomov wearing when he arrives?",
    [("evening dress", ""), ("hunting clothes", "Evening dress, for the proposal."), ("an apron", "Natalya wears an apron."), ("a uniform", "Evening dress.")],
    "Chubukov is surprised by his formal clothes.")
C.m("mcq03", QUARREL, "Oxen Meadows lie between:",
    [("Lomov's land and Natalya's family's birchwoods", ""), ("two rivers", "Lomov's land and their birchwoods."), ("two towns", "They border the birchwoods."), ("Chubukov's house and the church", "They border the birchwoods.")],
    "Each side claims them.")
C.m("mcq04", QUARREL, "Whose dog is Guess?",
    [("Lomov's", ""), ("Chubukov's", "Squeezer is Chubukov's."), ("Natalya's aunt's", "Lomov's."), ("a neighbour's", "Lomov's.")],
    "Lomov paid 125 roubles for him.")
C.m("mcq05", QUARREL, "Lomov says Squeezer is 'overshot'. This means:",
    [("its lower jaw is shorter than the upper jaw", ""), ("it runs too fast", "It is about its jaw."), ("it has been shot", "It is about its jaw."), ("it is very old", "It is about its jaw.")],
    "A defect in a hunting dog.")
C.m("mcq06", PLOT, "What does Natalya do when she learns why Lomov came?",
    [("she becomes hysterical and demands he be brought back", ""), ("she laughs", "She is desperate."), ("she refuses to see him", "She wants him back."), ("she faints", "Lomov faints later.")],
    "'Bring him back! Back!'")
C.m("mcq07", PLOT, "Why does Chubukov think Lomov is dead?",
    [("Lomov collapses into an armchair after the dog quarrel", ""), ("Lomov falls from a horse", "He collapses in the chair."), ("Lomov drinks poison", "He collapses."), ("Lomov leaves without a word", "He collapses.")],
    "He revives soon after.")
C.m("mcq08", HUMOUR, "A play with exaggerated characters and ridiculous situations is called a:",
    [("farce", ""), ("tragedy", "It is a comedy."), ("epic", "It is a short comedy."), ("biography", "It is a play.")],
    "The Proposal is a farce.")
C.m("mcq09", CHARS, "Which word best describes Lomov's health worries?",
    [("hypochondriac", ""), ("athletic", "He is always ill in his own mind."), ("optimistic", "He worries."), ("careless", "He worries constantly.")],
    "Palpitations, numb foot, twitching eyebrow.")
C.m("mcq10", HUMOUR, "The main target of Chekhov's satire is:",
    [("marriage for property and the pride of landowners", ""), ("the Russian army", "It is about landowners."), ("doctors", "Landowners."), ("hunting dogs", "The dogs are only the occasion.")],
    "Property matters more to them than love.")
C.tf("tf1", PLOT, "Lomov proposes to Natalya at the very beginning of their conversation.", False, "He starts talking of his land and they quarrel first.")
C.tf("tf2", QUARREL, "Squeezer is Chubukov's dog.", True, "Guess is Lomov's dog.")
C.tf("tf3", PLOT, "At the end of the play, Lomov and Natalya are engaged but quarrel again.", True, "Chubukov calls for champagne.")
C.tf("tf4", CHARS, "Natalya is 35 years old.", False, "Natalya is 25; Lomov is 35.")

C.la("la1", CHARS, "Write a character sketch of Lomov.",
     ["Lomov is a 35-year-old landowner who wants to marry for practical reasons: he needs a wife at a 'critical age'.", "He is a hypochondriac: palpitations, a numb foot, a twitching eyebrow, sleeplessness.",
      "He is nervous and indecisive, trembling as if before an examination.", "He is proud and quarrelsome: he fights over Oxen Meadows and the dogs even while proposing.",
      "His fainting and quick recovery make him a comic, almost ridiculous, figure."])
C.la("la2", HUMOUR, "How does Chekhov create humour in The Proposal?",
     ["Situation: a man comes to propose and ends up quarrelling over a meadow and a dog.", "Character: a hypochondriac hero, a fickle father and a sharp-tongued daughter.",
      "Irony: Chubukov's 'my angel' turns to 'intriguer'; 'conjugal bliss' begins with a quarrel.", "Exaggeration and stage action: fainting, shouting 'Bring him back!', champagne to drown the noise.",
      "The farce makes us laugh while showing the foolishness of pride and greed."])

chapter = header("ch09", 9, "The Proposal", "Anton Chekhov", "play",
                 ["plot_of_the_play", "characters", "the_two_quarrels", "humour_and_satire", "vocabulary_and_style"],
                 "CBSE 2025-26 English Language and Literature (184): First Flight, Chapter 9 (play). Assessed through extracts (5 marks), short answers in 40-50 words (3 marks) and long answers in 100-120 words (6 marks).")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
