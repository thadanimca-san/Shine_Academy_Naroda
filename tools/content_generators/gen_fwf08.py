"""CBSE Class 10 English, Footprints without Feet Ch 8: Bholi (K. A. Abbas)."""
import sys
from lit_common import make, header, path, ex

ROOT = sys.argv[1]
PATH = path("ch08_bholi", "footprints")
C = make("fwf10ch08")
blk = C.blk
CHILD, SCHOOL, MARRIAGE, THEME = ["bholis_childhood"], ["school_and_teacher"], ["the_marriage"], ["education_and_dignity"]
RF = lambda n: ex(n, "Read and Find Out")
TA = lambda n: ex(n, "Think about It")

CHANGE = ("| Bholi before school | Bholi after education |\n|---|---|\n"
          "| pock-marked, slow-witted in others' eyes, called 'Bholi' (simpleton) | confident, educated young woman, really **Sulekha** |\n"
          "| stammered and hardly spoke | speaks clearly and firmly |\n| neglected and laughed at | respected; plans to teach in the school |\n"
          "| afraid, like a dumb cow | refuses a greedy bridegroom and stands up for her family's honour |")

sections = [
 {"id": "s1", "title": "From silence to a voice", "blocks": [
  blk("s1.hook", "hook", title="The girl everyone laughed at",
    body="She was called **Bholi**, the simpleton. Her face was scarred by smallpox and she stammered so badly that she hardly spoke. Her family expected nothing from her.\n\n"
         "Then a kind teacher gave her a book and a promise. Years later, on her wedding day, Bholi says the words that shock everyone."),
  blk("s1.inspiration", "inspiration", title="The writer", person="K. A. Abbas", years="1914–1987",
    body="**Khwaja Ahmad Abbas** was an Indian writer, journalist and film-maker. His stories and films deal with social problems such as poverty, the status of women and dowry. 'Bholi' shows how education can transform a girl's life.",
    future="Teachers, social workers and campaigners for girls' education change lives exactly as Bholi's teacher did."),
  C.socratic("s1.socratic", "What gave Bholi the courage to refuse the bridegroom?",
    ["Education and her teacher's encouragement gave her self-respect", "Her father told her to refuse", "She was afraid of marriage"], 0,
    "Education gave her a voice."),
 ]},
 {"id": "s2", "title": "The story", "blocks": [
  blk("s2.thm", "theory", title="What happens", revision=True,
    body="**Childhood:** **Ramlal**, a **numberdar** (village official), had seven children; the youngest daughter was **Sulekha**, called **Bholi**. When she was **ten months old** she fell off a cot and something in her brain was damaged. At **two** she had **smallpox**, which left her face **pock-marked**. She **stammered**, so other children made fun of her. Her parents worried: who would marry an ugly, slow-witted girl?\n\n"
         "**School:** a **primary school for girls** opened in the village. The **Tehsildar**, who came to open it, told Ramlal, as the numberdar, to set an example by sending his daughters. Ramlal sent **Bholi**, because no one would marry her anyway. Bholi was bathed and given clean clothes for the first time; she was frightened, thinking she was being sent away like **Lakshmi**, the family cow.\n\n"
         "**The teacher:** at school a **kind teacher** spoke softly to her and asked her name. Bholi stammered; the teacher encouraged her patiently until she said 'Bholi'. The teacher gave her a **picture book** and promised that if she came daily, she would soon speak without stammering and nobody would laugh at her. For the first time Bholi felt hope.\n\n"
         "**The proposal:** years later, a proposal came from **Bishamber Nath**, a well-to-do **grocer** from another village. He was **old and lame**, with grown-up children, but he did not ask for dowry, so Bholi's parents accepted.\n\n"
         "**The wedding:** at the ceremony, when Bishamber saw Bholi's pock-marked face, he demanded a dowry of **five thousand rupees**. Ramlal begged, then put the money at his feet. Then Bholi, now educated and confident, **refused to marry** 'such a mean, greedy and contemptible coward'. She said she would look after her parents in their old age and **teach in the school** where she had learnt so much. In the background her teacher watched, proud of her work."),
  blk("s2.table", "markdown_table", title="How education changed Bholi", revision=True, body=CHANGE),
  C.kc("s2.check", "Why did Ramlal send Bholi to school?",
    [("he thought no one would marry her, and the Tehsildar asked him to set an example", ""), ("she was the cleverest child", "She was thought slow-witted."),
     ("she begged to go", "She was afraid."), ("the school was free for her only", "To set an example; she was unlikely to marry.")],
    "His other daughters were to be married.")
  ,C.kc("s2.check2", "Why did Bholi refuse to marry Bishamber?",
    [("he was greedy and demanded dowry, which showed him to be mean", ""), ("he was too young", "He was old."), ("her teacher forbade it", "She decided herself."), ("he was poor", "He was well-to-do.")],
    "She chose self-respect.")
 ]},
 {"id": "s3", "title": "Bholi, her teacher and the message", "blocks": [
  blk("s3.thm", "theory", title="Characters and theme", revision=True,
    body="**Bholi:** at first a neglected, frightened girl who **stammers** and feels unwanted. Education and love turn her into a **confident, self-respecting woman** who speaks firmly. When she refuses the marriage, she is called **Sulekha** again: the 'simpleton' has found her real self.\n\n"
         "**The teacher:** gentle, patient and encouraging; she gives Bholi the first kind words she has ever heard and a picture book. She is the turning point of Bholi's life.\n\n"
         "**Ramlal and his wife:** not cruel, but trapped by social customs; they see a daughter as a burden to be married off.\n\n"
         "**Bishamber:** a greedy, heartless man who sees marriage as a bargain.\n\n"
         "**Social message:** the story attacks the **dowry system**, neglect of the girl child and judging people by looks; it shows that **education gives women dignity and independence**."),
  C.kc("s3.check", "Who changed the course of Bholi's life?",
    [("her teacher", ""), ("Bishamber Nath", "He only showed his greed."), ("the Tehsildar", "He opened the school, but the teacher changed her."), ("her brothers", "The teacher.")],
    "The teacher's kindness gave her confidence.")
  ,C.kc("s3.check2", "Which social evil does the story attack most strongly?",
    [("the dowry system", ""), ("child labour", "Dowry."), ("untouchability", "Dowry."), ("alcoholism", "Dowry.")],
    "Bishamber demanded dowry because of Bholi's looks.")
 ]},
 {"id": "s4", "title": "Language of the story", "blocks": [
  blk("s4.thm", "theory", title="Words to know", revision=True,
    body="| Word | Meaning |\n|---|---|\n| **numberdar** | a village official who collects revenue |\n| **Tehsildar** | an officer in charge of a tehsil (sub-district) |\n"
         "| **pock-marked** | scarred by smallpox |\n| **stammer** | to speak with pauses and repeated sounds |\n| **dowry** | money or goods given by the bride's family at marriage |\n| **contemptible** | deserving scorn |\n\n"
         "**Style:** simple third-person narration with Indian village setting and a strong social message."),
  C.kc("s4.check", "A 'numberdar' is:",
    [("a village official who collects revenue", ""), ("a teacher", "A village official."), ("a grocer", "A village official."), ("a doctor", "A village official.")],
    "Ramlal was the numberdar.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Sulekha = Bholi: fall at 10 months, smallpox at 2, stammer.**\n- **Tehsildar → school → kind teacher → picture book → confidence.**\n"
         "- **Bishamber (old, lame grocer) → demands ₹5000 → Bholi refuses → will teach.**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying Bholi married Bishamber: she **refused**.\n2. Saying Ramlal sent all his daughters to school: he sent only **Bholi**.\n"
         "3. Forgetting Bholi's real name: **Sulekha**.\n4. Calling Ramlal cruel: he was **worried and bound by custom**."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Students write the teacher's diary on the day Bholi refused the marriage: what did the teacher feel and remember?"),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Have you ever been judged by your looks or your speech? How can we make sure no child feels like Bholi did?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Civics (Gender, Religion and Caste):** the status of women and girls' education.\n- **The Making of a Scientist:** another child guided by a caring adult."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="'Education gave Bholi a voice.' Discuss in about 120 words.\n\n"
         "**Model answer:** Bholi grew up neglected and mocked. A fall in infancy and smallpox at two left her slow and pock-marked, and she stammered so badly that she hardly spoke. Her father sent her to the new village school only because no one was likely to marry her. There a kind teacher spoke gently, helped her say her name, and promised that with learning she would speak without fear. Years later, when the greedy, old Bishamber demanded five thousand rupees at the wedding because of her looks, Bholi, now educated and confident, refused to marry such a mean man. She chose to care for her parents and teach in the school. Education gave her self-respect and the courage to speak."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Sulekha, called Bholi, is scarred and stammers; her family neglects her.\n- She is sent to the new girls' school, where a kind teacher gives her confidence.\n"
         "- Her parents accept a proposal from Bishamber, an old, lame grocer.\n- At the wedding he demands dowry; Bholi refuses to marry him.\n"
         "- She will serve her parents and teach. Theme: education brings dignity; dowry is an evil."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- Explain the role of the teacher in every long answer on Bholi.\n- Mention the dowry demand and Bholi's exact refusal.\n- Use 'Sulekha' to show her transformation."),
  blk("s5.flash1", "flashcard", front="What is Bholi's real name?", back="Sulekha."),
  blk("s5.flash2", "flashcard", front="Why did Bholi stammer and look different?", back="A fall at ten months affected her brain, and smallpox at two left her face pock-marked."),
  blk("s5.flash3", "flashcard", front="What did Bishamber demand at the wedding?", back="A dowry of five thousand rupees, after seeing Bholi's pock-marked face."),
  blk("s5.flash4", "flashcard", front="What did Bholi decide to do after refusing the marriage?", back="Look after her parents and teach in the school where she studied."),
 ]},
]

# ---------------- NCERT ----------------
C.sa("rf1", CHILD, "Why is Bholi's father worried about her?", ["Bholi is pock-marked, slow-witted in others' eyes and stammers.", "He fears that no one will marry her."], RF(1))
C.sa("rf2", SCHOOL, "For what unusual reason is Bholi sent to school?", ["The Tehsildar asked Ramlal to set an example by sending his daughters.", "Ramlal sent Bholi, thinking no one would marry her anyway, so schooling would not spoil her chances."], RF(2))
C.sa("rf3", SCHOOL, "Does Bholi enjoy her first day at school?", ["At first she is frightened and cries.", "But the kind teacher and the picture book make her happy and hopeful."], RF(3))
C.sa("rf4", SCHOOL, "Does she find her teacher different from the people at home?", ["Yes; the teacher speaks to her softly and kindly.", "At home she was ignored or scolded; the teacher encourages her and believes in her."], RF(4))
C.sa("rf5", MARRIAGE, "Why do Bholi's parents accept Bishamber's marriage proposal?", ["Bishamber is well-to-do and does not ask for dowry.", "They fear that no one else will marry Bholi."], RF(5))
C.sa("rf6", MARRIAGE, "Why does the marriage not take place?", ["Bishamber demands five thousand rupees dowry after seeing Bholi's face.", "Bholi refuses to marry such a greedy, mean man."], RF(6))
C.la("ta1", THEME, "Bholi's teacher played a very important role in changing the course of her life. Discuss.",
     ["At home Bholi was neglected and laughed at; she stammered and was afraid.", "The teacher spoke kindly, helped her say her name and gave her a picture book.",
      "She promised Bholi that learning would make her speak without fear.", "This gave Bholi confidence and self-respect over the years.",
      "Because of this, Bholi could refuse a greedy bridegroom and choose to teach; the teacher changed her life."], TA(1))
C.la("ta2", MARRIAGE, "Why did Bholi at first agree to an unequal match? Why did she later reject the marriage? What does this tell us about her?",
     ["At first Bholi agreed because her parents wanted it and she did not wish to hurt them.", "She knew they feared no one else would marry her.",
      "When Bishamber demanded dowry and humiliated her father, she saw his greed and meanness.", "She rejected him to protect her family's honour and her self-respect.",
      "This shows she had become a confident, educated woman with dignity."], TA(2))
C.sa("ta3", THEME, "Bholi's real name is Sulekha. When is she called Sulekha again, and why?",
     ["She is called Sulekha when she refuses to marry Bishamber.", "It shows she is no longer a 'simpleton' but a confident, educated woman."], TA(3))

# ---------------- Objective practice ----------------
C.m("mcq01", CHILD, "Bholi's real name was:", [("Sulekha", ""), ("Lakshmi", "That was the cow."), ("Radha", "Sulekha."), ("Bholi", "Bholi was a nickname.")], "Bholi means 'simpleton'.")
C.m("mcq02", CHILD, "What happened to Bholi at ten months?", [("she fell off a cot and her brain was affected", ""), ("she got smallpox", "That was at two."), ("she went to school", "Much later."), ("she lost her mother", "She fell off a cot.")], "It made her slow.")
C.m("mcq03", CHILD, "Bholi's face was pock-marked because of:", [("smallpox", ""), ("a burn", "Smallpox."), ("a fall", "The fall affected her brain."), ("an insect bite", "Smallpox.")], "At the age of two.")
C.m("mcq04", CHILD, "Ramlal was the village:", [("numberdar", ""), ("Tehsildar", "The Tehsildar opened the school."), ("teacher", "Numberdar."), ("grocer", "Bishamber was a grocer.")], "A village official.")
C.m("mcq05", SCHOOL, "Who opened the girls' school?", [("the Tehsildar", ""), ("Ramlal", "The Tehsildar."), ("the teacher", "The Tehsildar."), ("Bishamber", "The Tehsildar.")], "He asked Ramlal to set an example.")
C.m("mcq06", SCHOOL, "Why was Bholi frightened on the way to school?", [("she thought she was being sent away like Lakshmi the cow", ""), ("she hated books", "She feared being sent away."), ("the teacher was harsh", "The teacher was kind."), ("she was ill", "She feared being sent away.")], "She was bathed and dressed for the first time.")
C.m("mcq07", SCHOOL, "What did the teacher give Bholi?", [("a picture book", ""), ("money", "A book."), ("sweets", "A book."), ("a doll", "A book.")], "And a promise of learning.")
C.m("mcq08", MARRIAGE, "Bishamber Nath was:", [("an old, lame grocer", ""), ("a young teacher", "An old grocer."), ("the Tehsildar", "A grocer."), ("Bholi's cousin", "A grocer.")], "He did not ask for dowry at first.")
C.m("mcq09", MARRIAGE, "How much dowry did Bishamber demand?", [("five thousand rupees", ""), ("five hundred rupees", "Five thousand."), ("fifty thousand rupees", "Five thousand."), ("nothing", "He demanded dowry.")], "After seeing her face.")
C.m("mcq10", MARRIAGE, "What did Bholi do at the wedding?", [("refused to marry Bishamber", ""), ("married him quietly", "She refused."), ("ran away", "She spoke firmly."), ("fainted", "She refused.")], "She called him greedy and mean.")
C.m("mcq11", MARRIAGE, "After refusing, Bholi planned to:", [("serve her parents and teach in the school", ""), ("marry someone rich", "She chose to teach."), ("leave the village", "She would stay."), ("open a shop", "She would teach.")], "Her teacher was proud.")
C.m("mcq12", THEME, "The main message of the story is:", [("education gives women dignity; dowry is an evil", ""), ("girls need not study", "Education empowers."), ("looks are everything", "Looks should not matter."), ("marriage is a business", "That is Bishamber's view.")], "A social comment.")
C.m("mcq13", CHILD, "How many children did Ramlal have?", [("seven", ""), ("four", "Seven."), ("two", "Seven."), ("ten", "Seven.")], "Bholi was the youngest daughter.")
C.m("mcq14", SCHOOL, "The teacher promised Bholi that:", [("she would speak without stammering and nobody would laugh at her", ""), ("she would become rich", "Confidence, not wealth."), ("she would marry a prince", "Confidence."), ("she would never study again", "She would learn.")], "Hope for the first time.")
C.m("mcq15", THEME, "When is Bholi called Sulekha again?", [("when she refuses the marriage", ""), ("on her first school day", "When she refuses."), ("when she was born", "That is the start."), ("never", "Once, at the end.")], "Her transformation.")
C.m("mcq16", MARRIAGE, "Why did Bholi's parents accept Bishamber's proposal?", [("he was well-to-do and asked no dowry", ""), ("Bholi loved him", "They accepted for practical reasons."), ("the teacher arranged it", "Her parents did."), ("he was young and handsome", "He was old and lame.")], "They feared no one else would marry her.")
C.tf("tf1", MARRIAGE, "Bholi married Bishamber in the end.", False, "She refused to marry him.")
C.tf("tf2", SCHOOL, "The teacher was kind to Bholi.", True, "She encouraged her patiently.")
C.tf("tf3", CHILD, "Bholi stammered as a child.", True, "Others laughed at her.")
C.tf("tf4", SCHOOL, "Ramlal sent all his daughters to school.", False, "He sent only Bholi.")
C.tf("tf5", MARRIAGE, "Bishamber asked for dowry before the wedding.", False, "He demanded it at the wedding, after seeing her face.")
C.tf("tf6", THEME, "The story criticises the dowry system.", True, "Bishamber's greed is exposed.")

# ---------------- More ----------------
C.vsa("vsa1", CHILD, "Give two reasons why Bholi was neglected.", ["She was pock-marked and thought to be slow.", "She stammered and others laughed at her."])
C.vsa("vsa2", SCHOOL, "Give two things the teacher did for Bholi.", ["She spoke kindly and helped her say her name.", "She gave her a picture book and a promise of learning."])
C.vsa("vsa3", MARRIAGE, "What two words did Bholi use for Bishamber?", ["Greedy and mean.", "A contemptible coward."])
C.sa("sa1", CHILD, "How was Bholi treated at home?",
     ["She was neglected; her parents worried she would never marry.", "Her brothers and sisters laughed at her, and she hardly spoke."])
C.sa("sa2", MARRIAGE, "How did Ramlal respond to Bishamber's demand?",
     ["He pleaded with Bishamber and placed his turban at his feet, begging him not to humiliate them.", "Then he brought the money, to avoid disgrace."])
C.sa("sa3", THEME, "How does the story show the importance of a good teacher?",
     ["The teacher's kindness and patience gave Bholi her first confidence.", "This confidence grew until Bholi could stand up for herself."])
C.sa("sa4", SCHOOL, "Why did Bholi think she was being sent away like Lakshmi the cow?",
     ["For the first time she was bathed, oiled and given clean clothes.", "She remembered that Lakshmi had been treated well before being sent away, so she was afraid."])
C.la("la1", THEME, "Write a character sketch of Bholi.",
     ["Bholi (Sulekha) was a neglected child, scarred by smallpox and stammering.", "She was timid and fearful, laughed at by others.",
      "At school, her teacher's kindness gave her hope and confidence.", "Education made her a self-respecting, articulate woman.",
      "She bravely refused a greedy bridegroom and chose to serve her parents and teach."])
C.la("la2", THEME, "'The dowry system is a curse.' Discuss with reference to Bholi.",
     ["Bholi's parents worried about her marriage because of her looks and their limited means.", "Bishamber, an old and lame man, agreed only because he expected advantage.",
      "At the wedding he demanded five thousand rupees after seeing her face.", "Ramlal was humiliated and forced to beg.",
      "Bholi's refusal shows that education and courage can fight this evil."])
C.la("la3", SCHOOL, "Imagine you are Bholi's teacher. Write a diary entry on the day Bholi refused the marriage.",
     ["Date and first person; recall the frightened, stammering girl who first came to school.", "How you encouraged her and gave her a picture book.",
      "Today: Bishamber's dowry demand and Bholi's firm refusal.", "Your pride that she will teach in the school, and your hope for other girls."])

chapter = header("ch08", 27, "Bholi", "K. A. Abbas", "prose",
                 ["bholis_childhood", "school_and_teacher", "the_marriage", "education_and_dignity"],
                 "CBSE 2025-26 English Language and Literature (184): Footprints without Feet, Chapter 8. Assessed through short answers in 40-50 words (3 marks) and a long answer in 100-120 words (6 marks); no extracts from this book.",
                 book="footprints")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
