"""CBSE Class 10 English, First Flight Ch 8: The Sermon at Benares (Betty Renshaw)."""
import sys
from lit_common import make, header, path, ex

ROOT = sys.argv[1]
PATH = path("ch08_the_sermon_at_benares")
C = make("ff10ch08")
blk = C.blk
LIFE, KISA, SERMON, LANG = ["buddhas_life_and_enlightenment"], ["kisa_gotami"], ["the_sermon_on_death_and_grief"], ["vocabulary_and_style"]
OCC = lambda n: ex(n, "Oral Comprehension Check")

TIMELINE = ("| Stage | What happened |\n|---|---|\n"
            "| **Birth** | born Prince Siddhartha Gautama in northern India (563 B.C.) |\n"
            "| **Age 12** | sent away to study the Hindu sacred scriptures |\n"
            "| **Four years later** | returned home, married a princess, had a son; lived ten years as a royal prince |\n"
            "| **About 25** | saw a sick man, an aged man, a funeral procession and a monk begging for alms |\n"
            "| **Seven years** | wandered in search of enlightenment |\n"
            "| **Under the peepal tree** | sat until enlightened after seven days; named it the **Bodhi Tree** (Tree of Wisdom); became the **Buddha** (the Awakened or Enlightened) |\n"
            "| **Benares** | preached his first sermon at Benares, the holiest dipping place on the Ganges |")

sections = [
 {"id": "s1", "title": "Facing loss", "blocks": [
  blk("s1.hook", "hook", title="A handful of mustard seed",
    body="A young mother's only son dies. Mad with grief, she goes from house to house begging for medicine to bring him back. A wise man says he can help, if she brings him a handful of **mustard seed** from a house where **no one has ever died**.\n\n"
         "In this chapter we learn about the life of **Gautama Buddha** and how he taught Kisa Gotami, and all of us, to understand death and grief."),
  blk("s1.inspiration", "inspiration", title="The writer", person="Betty Renshaw",
    body="The chapter, retold by **Betty Renshaw**, presents the life of the Buddha and his first sermon at **Benares** (Varanasi). The story of **Kisa Gotami** is one of the best-known Buddhist parables about accepting death.",
    future="Counsellors, doctors and teachers help people cope with grief; understanding loss is part of growing up."),
  C.socratic("s1.socratic", "Why did the Buddha send Kisa Gotami for mustard seed instead of simply telling her that death is certain?",
    ["So that she would discover for herself that every family has suffered death", "Because he needed mustard seed", "To keep her busy and forget her son"], 0,
    "Truth we discover ourselves stays with us longer.")
 ]},
 {"id": "s2", "title": "The life of the Buddha", "blocks": [
  blk("s2.thm", "theory", title="From prince to the Enlightened One", revision=True,
    body="**Gautama Buddha (563 B.C. – 483 B.C.)** began life as **Prince Siddhartha Gautama** in northern India. At **twelve** he was sent away for schooling in the Hindu sacred scriptures, and four years later he returned home to **marry a princess**. They had a son and lived for **ten years** as befitted royalty.\n\n"
         "At about the age of **twenty-five**, the prince, who had been shielded from the sufferings of the world, while out hunting saw a **sick man**, then an **aged man**, then a **funeral procession**, and finally a **monk begging for alms**. These sights moved him so much that he went out into the world to seek **enlightenment** concerning the sorrows he had witnessed.\n\n"
         "He wandered for **seven years** and finally sat down under a **peepal tree**, vowing to stay there until enlightenment came. Enlightened after **seven days**, he renamed the tree the **Bodhi Tree** (Tree of Wisdom) and began to teach and share his new understanding. He became known as **the Buddha** (the Awakened or the Enlightened). He preached his **first sermon** at the city of **Benares**, most holy of the dipping places on the river Ganges."),
  blk("s2.table", "markdown_table", title="The Buddha's life at a glance", revision=True, body=TIMELINE),
  C.kc("s2.check", "Which sights changed Prince Siddhartha's life?",
    [("a sick man, an aged man, a funeral procession and a monk begging for alms", ""), ("a battle and a palace", "He saw sorrows of life."),
     ("a river and a tree", "He saw human suffering."), ("a wedding and a feast", "He saw suffering.")],
    "He had been shielded from the world's sufferings until then.")
  ,C.kc("s2.check2", "What does 'Buddha' mean?",
    [("the Awakened or the Enlightened", ""), ("the Prince", "It means the Enlightened."), ("the Wanderer", "It means the Enlightened."), ("the Teacher of Benares", "It means the Enlightened.")],
    "He gained enlightenment under the Bodhi Tree.")
 ]},
 {"id": "s3", "title": "Kisa Gotami and the sermon", "blocks": [
  blk("s3.thm", "theory", title="The mustard seed and the lesson", revision=True,
    body="**Kisa Gotami's grief:** Kisa Gotami had an only son, and he died. In her grief she carried the dead child to all her neighbours, asking them for **medicine**. People said, 'She has lost her senses. The boy is dead.' At last a man said, 'I cannot give thee medicine for thy child, but I know a physician who can,' and directed her to **Sakyamuni, the Buddha**.\n\n"
         "**The test:** the Buddha asked for **a handful of mustard seed**, but it must be taken from a house where **no one had lost a child, husband, parent or friend**. Kisa Gotami went from house to house. Everyone pitied her and was ready to give seed, but in every house someone had died: 'The living are few, but the dead are many.'\n\n"
         "**Understanding:** weary and hopeless, she sat down at the wayside, watching the lights of the city as they **flickered up and were extinguished** again. She thought, 'How selfish am I in my grief! **Death is common to all**; yet in this valley of desolation there is a path that leads him to immortality who has surrendered all selfishness.'\n\n"
         "**The sermon:** the Buddha said: the life of mortals is **troubled and brief and combined with pain**. As **ripe fruits** are early in danger of falling, so mortals when born are always in danger of death. As all **earthen vessels** made by the potter end in being broken, so is the life of mortals. Not from weeping nor from grieving will anyone obtain peace of mind; it only brings more pain. He who has **drawn out the arrow** of lamentation and grief will obtain peace of mind; he who has overcome all sorrow will become **free from sorrow, and be blessed**."),
  C.kc("s3.check", "What condition did the Buddha put on the mustard seed?",
    [("it must come from a house where no one had lost a child, husband, parent or friend", ""), ("it must be very fresh", "The condition was about death."),
     ("it must be bought with money", "It was about death in the house."), ("it must come from a temple", "It was about death in the house.")],
    "No such house existed.")
  ,C.kc("s3.check2", "What did Kisa Gotami understand at last?",
    [("death is common to all, and she was selfish in her grief", ""), ("her son would come back", "She accepted his death."),
     ("the Buddha had cheated her", "She understood his lesson."), ("mustard seed cures death", "She understood death is certain.")],
    "She watched the city lights flicker and go out.")
 ]},
 {"id": "s4", "title": "Language of the chapter", "blocks": [
  blk("s4.thm", "theory", title="Words, images and comparisons", revision=True,
    body="| Word or phrase | Meaning |\n|---|---|\n| **enlightenment** | spiritual wisdom and understanding |\n| **alms** | money or food given to the poor |\n"
         "| **sermon** | a religious talk |\n| **mortals** | human beings, who must die |\n| **desolation** | great sadness and emptiness |\n"
         "| **lamentation** | crying aloud in grief |\n| **Sakyamuni** | 'sage of the Sakyas', a name of the Buddha |\n\n"
         "**Similes in the sermon:** life is like **ripe fruit** that may fall early; like **earthen vessels** that end in being broken. **Image:** the city lights flickering up and going out show that lives begin and end. **Metaphor:** grief is an **arrow** to be drawn out."),
  C.kc("s4.check", "What do the flickering city lights symbolise?",
    [("human lives that begin and end", ""), ("a festival", "They symbolise life and death."), ("the Buddha's wisdom", "They show lives ending."), ("Kisa Gotami's home", "They symbolise life and death.")],
    "This image helps Kisa Gotami understand.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Four sights: Sick, Old, Dead, Monk (\"SODM\").**\n- **Numbers: 12 school, +4 married, 10 royal years, ~25 sights, 7 years wandering, 7 days under the tree.**\n"
         "- **Sermon images: ripe fruit, earthen pots, arrow of grief.**\n- **Kisa's realisation: 'The living are few, but the dead are many.'**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying the Buddha brought the child back to life: he taught Kisa to **accept** death.\n2. Writing that the first sermon was at Bodh Gaya: enlightenment was under the Bodhi Tree; the first sermon was at **Benares**.\n"
         "3. Saying Kisa got mustard seed: she could not find a house without death, which was the lesson.\n4. Mixing up 'alms' (charity) and 'arms'."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Compare Kisa Gotami's first and second searches: what she wanted, whom she met, what she learnt. Students fill a two-column chart."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="How can we comfort a friend who has lost someone dear? What would the Buddha's lesson suggest?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Madam Rides the Bus (Ch 7) and The Ball Poem:** first lessons in loss.\n- **History:** Buddhism spread across Asia; India's state emblem comes from Ashoka's pillar at Sarnath, near Benares, where the first sermon was given."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="How did the Buddha help Kisa Gotami overcome her grief? Answer in about 120 words.\n\n"
         "**Model answer:** When Kisa Gotami's only son died, she was so lost in grief that she carried his body from house to house asking for medicine. The Buddha did not lecture her. Instead he asked her to bring a handful of mustard seed from a house where no one had lost a child, husband, parent or friend. In every house she found that someone had died, and she realised that 'the living are few, but the dead are many'. Watching the city lights flicker and go out, she understood that death is common to all and that her grief had been selfish. The Buddha then taught that grieving only brings more pain, and that one who overcomes sorrow finds peace. By letting her discover the truth herself, he healed her."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Prince Siddhartha, moved by the sight of sickness, old age, death and a monk, left his royal life to seek enlightenment.\n"
         "- After seven years of wandering he was enlightened under the Bodhi Tree and became the Buddha; he preached his first sermon at Benares.\n"
         "- Kisa Gotami, grieving for her dead son, was asked to bring mustard seed from a house untouched by death; she found none and understood that death is universal.\n"
         "- The Buddha taught that weeping brings no peace; overcoming sorrow brings peace and blessing."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- Use the two comparisons from the sermon (ripe fruit, earthen vessels) in answers on the nature of life.\n- Compare Kisa's two searches when asked how she changed.\n"
         "- Value-based long answers: link the lesson to coping with loss today."),
  blk("s5.flash1", "flashcard", front="What four sights moved Prince Siddhartha?", back="A sick man, an aged man, a funeral procession and a monk begging for alms."),
  blk("s5.flash2", "flashcard", front="Where did the Buddha preach his first sermon?", back="At Benares, the holiest dipping place on the Ganges."),
  blk("s5.flash3", "flashcard", front="What did the Buddha ask Kisa Gotami to bring?", back="A handful of mustard seed from a house where no one had lost a child, husband, parent or friend."),
  blk("s5.flash4", "flashcard", front="Name the two comparisons the Buddha uses for human life.", back="Ripe fruits in danger of falling; earthen vessels that end in being broken."),
 ]},
]

# ---------------- NCERT ----------------
C.vsa("occ1", LIFE, "When her son dies, Kisa Gotami goes from house to house. What does she ask for? Does she get it? Why not?",
      ["She asks for medicine to cure her dead son.", "She does not get it, because the boy is dead and no medicine can help."], OCC(1))
C.vsa("occ2", KISA, "Kisa Gotami again goes from house to house after she speaks with the Buddha. What does she ask for the second time? Does she get it? Why not?",
      ["She asks for a handful of mustard seed from a house where no one has died.", "She cannot get it, because every house has lost someone."], OCC(2))
C.sa("ex1", KISA, "What did Kisa Gotami understand the second time that she failed to understand the first time? Was this what the Buddha wanted her to understand?",
     ["The first time she thought her son could be cured; the second time she saw that death is common to all.", "Yes, the Buddha wanted her to find this truth for herself and stop her selfish grief."], ex(1))
C.sa("ex2", KISA, "Why do you think Kisa Gotami understood this only the second time? In what way did the Buddha change her understanding?",
     ["At first grief had blinded her; she only wanted her son back.", "The Buddha's task made her meet many grieving families, so she saw that everyone suffers loss."], ex(2))
C.sa("ex3", KISA, "How do you usually understand the idea of 'selfishness'? Do you agree with Kisa Gotami that she was being 'selfish in her grief'?",
     ["Selfishness usually means thinking only of oneself.", "Yes: she saw only her own sorrow and forgot that death touches everyone; realising this freed her."], ex(3))
C.sa("ex4", LIFE, "What made Prince Siddhartha leave his royal life?",
     ["At about 25 he saw a sick man, an aged man, a funeral procession and a monk begging for alms.", "These sights of suffering made him seek enlightenment about the sorrows of life."], ex(4))

# ---------------- Extracts ----------------
C.extract("ext1", LIFE,
  "Enlightened after seven days, he renamed the tree the Bodhi Tree (Tree of Wisdom)\nand began to teach and to share his new understandings.",
  [("Who is 'he'?", "Gautama Buddha (Prince Siddhartha)."),
   ("What was the tree before he renamed it?", "A peepal tree."),
   ("What does 'Bodhi Tree' mean?", "Tree of Wisdom."),
   ("How long did he sit before he was enlightened?", "Seven days."),
   ("Where did he preach his first sermon?", "At Benares.")])
C.extract("ext2", KISA,
  "Kisa Gotami had an only son, and he died. In her grief she carried the dead child to all her neighbours,\nasking them for medicine, and the people said, 'She has lost her senses. The boy is dead.'",
  [("What happened to Kisa Gotami's son?", "He died."),
   ("What did she ask her neighbours for?", "Medicine for her dead child."),
   ("What did the people think of her?", "That she had lost her senses."),
   ("Find a word that means 'deep sorrow'.", "Grief."),
   ("Who finally helped her?", "The Buddha (Sakyamuni).")])
C.extract("ext3", SERMON,
  "The life of mortals in this world is troubled and brief and combined with pain.\nAs ripe fruits are early in danger of falling, so mortals when born are always in danger of death.",
  [("Who speaks these words?", "The Buddha."),
   ("How does he describe human life?", "Troubled, brief and full of pain."),
   ("To what are mortals compared?", "Ripe fruits in danger of falling."),
   ("Name the figure of speech.", "Simile."),
   ("What does 'mortals' mean?", "Human beings, who must die.")])

# ---------------- Objective practice ----------------
C.m("mcq01", LIFE, "At what age was Siddhartha sent away for schooling?",
    [("twelve", ""), ("twenty-five", "That is when he saw the four sights."), ("seven", "Twelve."), ("sixteen", "He returned four years later.")],
    "He studied the Hindu sacred scriptures.")
C.m("mcq02", LIFE, "For how long did Siddhartha wander seeking enlightenment?",
    [("seven years", ""), ("seven days", "That was under the tree."), ("ten years", "He lived ten royal years."), ("twelve years", "Seven years.")],
    "Then he sat under the peepal tree.")
C.m("mcq03", LIFE, "Siddhartha had been shielded from:",
    [("the sufferings of the world", ""), ("his family", "He lived with them."), ("education", "He was educated."), ("religion", "He studied scriptures.")],
    "So the four sights shocked him.")
C.m("mcq04", LIFE, "Benares is described as:",
    [("the holiest of the dipping places on the Ganges", ""), ("the Buddha's birthplace", "He was born in northern India."), ("the place of the Bodhi Tree", "That is elsewhere."), ("a desert town", "It is on the Ganges.")],
    "He preached his first sermon there.")
C.m("mcq05", KISA, "Who directed Kisa Gotami to the Buddha?",
    [("a man who said he knew a physician who could help", ""), ("her husband", "A man she met."), ("a monk", "A man she met."), ("the king", "A man she met.")],
    "He called the Buddha a physician.")
C.m("mcq06", KISA, "What did Kisa Gotami find in every house?",
    [("someone had died there", ""), ("no mustard seed", "They had seed, but also death."), ("no one at home", "People were home and pitied her."), ("medicine", "They had none for death.")],
    "'The living are few, but the dead are many.'")
C.m("mcq07", KISA, "While sitting at the wayside, Kisa Gotami watched:",
    [("the lights of the city flicker up and be extinguished", ""), ("the sun rise", "She watched the lights."), ("birds flying", "The lights."), ("the river flow", "The lights.")],
    "The lights reminded her of lives beginning and ending.")
C.m("mcq08", SERMON, "According to the Buddha, weeping and grieving:",
    [("bring more pain and no peace of mind", ""), ("bring the dead back", "They do not."), ("are the path to wisdom", "They bring pain."), ("make the body strong", "They harm the body.")],
    "His body will become sick and pale.")
C.m("mcq09", SERMON, "'Earthen vessels made by the potter end in being broken' means:",
    [("all life ends in death", ""), ("pots are badly made", "It is a comparison for life."), ("potters are careless", "It is about mortality."), ("we should not use pots", "It is about mortality.")],
    "Every created thing must end.")
C.m("mcq10", SERMON, "Who will obtain peace of mind, according to the Buddha?",
    [("one who has drawn out the arrow of lamentation and grief", ""), ("one who weeps the most", "Weeping brings pain."), ("one who is rich", "Peace comes from overcoming grief."), ("one who lives alone", "Peace comes from overcoming grief.")],
    "He becomes free from sorrow and is blessed.")
C.m("mcq11", LANG, "'Alms' means:",
    [("money or food given to the poor", ""), ("weapons", "That is arms."), ("prayers", "Alms are charity."), ("sorrows", "Alms are charity.")],
    "The monk was begging for alms.")
C.m("mcq12", LANG, "'Desolation' means:",
    [("great sadness and emptiness", ""), ("great joy", "The opposite."), ("a city", "It means emptiness."), ("a festival", "It means emptiness.")],
    "This 'valley of desolation' is the world of sorrow.")
C.m("mcq13", KISA, "Kisa Gotami realised she had been:",
    [("selfish in her grief", ""), ("cheated by the Buddha", "She understood his lesson."), ("too generous", "Selfish in grief."), ("lazy", "Selfish in grief.")],
    "Death is common to all.")
C.tf("tf1", LIFE, "Siddhartha preached his first sermon under the Bodhi Tree.", False, "He was enlightened there; the first sermon was at Benares.")
C.tf("tf2", KISA, "Kisa Gotami found a house where no one had died.", False, "Every house had lost someone.")
C.tf("tf3", LIFE, "Siddhartha lived for ten years as a royal prince after marriage.", True, "He married, had a son and lived as befitted royalty.")
C.tf("tf4", SERMON, "The Buddha compares mortals to ripe fruits in danger of falling.", True, "So mortals are always in danger of death.")

C.sa("sa1", SERMON, "What does the Buddha say about the nature of life and death?",
     ["Life is troubled, brief and full of pain; like ripe fruit or earthen pots, all mortals end in death.", "Weeping brings no peace; overcoming sorrow brings peace and blessing."])
C.sa("sa2", LIFE, "How did the Buddha get his name and what does it mean?",
     ["After seven days under the peepal tree he gained enlightenment.", "He was then called the Buddha, the Awakened or the Enlightened."])
C.la("la1", KISA, "Compare Kisa Gotami's two journeys from house to house. What did she learn?",
     ["First journey: mad with grief, she begged for medicine to cure her dead son; people thought she had lost her senses.",
      "Second journey: she sought mustard seed from a house where no one had died, at the Buddha's request.", "In every house someone had died: 'the living are few, but the dead are many.'",
      "Watching the city lights flicker out, she understood that death is common to all and that her grief was selfish.", "She learnt to accept death and find peace, as the Buddha intended."])
C.la("la2", SERMON, "'Not from weeping nor from grieving will anyone obtain peace of mind.' Explain with reference to the sermon and to life today.",
     ["The Buddha says grief only increases pain and makes the body sick.", "Death is natural: life is like ripe fruit and earthen pots.",
      "Peace comes from drawing out the 'arrow' of grief and accepting loss.", "Today too, people who share sorrow, support others and move on find strength, as Kisa Gotami did."])

# ---------------- Top-up practice ----------------
C.m("mcq14", LIFE, "Whom did Siddhartha marry after his schooling?",
    [("a princess", ""), ("a farmer's daughter", "A princess."), ("no one", "He married a princess."), ("Kisa Gotami", "Kisa Gotami is a later character.")],
    "They had a son.")
C.m("mcq15", LIFE, "Under which tree did Siddhartha sit for enlightenment?",
    [("a peepal tree", ""), ("a mango tree", "A peepal tree."), ("a banyan tree", "A peepal tree."), ("a neem tree", "A peepal tree.")],
    "He renamed it the Bodhi Tree.")
C.m("mcq16", LIFE, "The Buddha's dates are:",
    [("563 B.C. – 483 B.C.", ""), ("483 B.C. – 563 B.C.", "Birth comes first: 563 B.C."), ("A.D. 563 – 483", "B.C., not A.D."), ("2700 B.C.", "That is tea's history.")],
    "He lived about eighty years.")
C.m("mcq17", KISA, "Why did people say Kisa Gotami had lost her senses?",
    [("she asked for medicine for a child who was already dead", ""), ("she shouted at them", "She asked for medicine for a dead child."), ("she gave away her money", "She asked for medicine."), ("she sang in the street", "She asked for medicine.")],
    "Grief had blinded her.")
C.m("mcq18", KISA, "The phrase 'The living are few, but the dead are many' means:",
    [("death has touched every family", ""), ("the city was empty", "It is about death in every home."), ("people live long", "It is about death."), ("the dead come back", "It is about death in every home.")],
    "No house was free of death.")
C.m("mcq19", SERMON, "The Buddha compares grief to:",
    [("an arrow that must be drawn out", ""), ("a river", "An arrow."), ("a fire", "An arrow."), ("a flower", "An arrow.")],
    "Drawing it out brings peace.")
C.m("mcq20", LANG, "'Lamentation' means:",
    [("crying aloud in grief", ""), ("laughing", "The opposite."), ("singing", "Crying in grief."), ("praying", "Crying in grief.")],
    "The arrow of lamentation and grief.")
C.m("mcq21", LIFE, "What did Siddhartha see while out hunting?",
    [("signs of human suffering", ""), ("a tiger", "He saw suffering."), ("a battle", "He saw suffering."), ("a festival", "He saw suffering.")],
    "A sick man, an aged man, a funeral and a monk.")
C.tf("tf5", KISA, "The Buddha gave Kisa Gotami medicine to revive her son.", False, "He set her a task so she would understand death.")
C.tf("tf6", LIFE, "Siddhartha was enlightened after seven days under the tree.", True, "He then named it the Bodhi Tree.")
C.vsa("vsa1", SERMON, "Give the two comparisons the Buddha uses for human life.", ["Ripe fruits in danger of falling early.", "Earthen vessels that end in being broken."])
C.vsa("vsa2", KISA, "What did Kisa Gotami realise when she sat at the wayside?", ["Death is common to all.", "She had been selfish in her grief."])
C.sa("sa3", LIFE, "Why is Benares important in the Buddha's story?",
     ["It is the holiest dipping place on the Ganges.", "The Buddha preached his first sermon there after his enlightenment."])

chapter = header("ch08", 8, "The Sermon at Benares", "Betty Renshaw", "prose",
                 ["buddhas_life_and_enlightenment", "kisa_gotami", "the_sermon_on_death_and_grief", "vocabulary_and_style"],
                 "CBSE 2025-26 English Language and Literature (184): First Flight prose, Chapter 8. Assessed through extracts (5 marks), short answers in 40-50 words (3 marks) and long answers in 100-120 words (6 marks).")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
