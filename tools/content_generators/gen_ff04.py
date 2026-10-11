"""CBSE Class 10 English, First Flight Ch 4: From the Diary of Anne Frank."""
import sys
from lit_common import make, header, path, ex

ROOT = sys.argv[1]
PATH = path("ch04_from_the_diary_of_anne_frank")
C = make("ff10ch04")
blk = C.blk
DIARY, FAMILY, SCHOOL, ANNE, LANG = ["why_a_diary"], ["family_background"], ["mr_keesing_and_the_essays"], ["anne_as_a_person"], ["vocabulary_and_style"]
OCC = lambda n: ex(n, "Oral Comprehension Check")

FAMTAB = ("| Person | What Anne tells Kitty |\n|---|---|\n"
          "| **Father (Otto Frank)** | 'the most adorable father I've ever seen'; married at 36; became Managing Director of the Dutch Opekta Company |\n"
          "| **Mother (Edith)** | married at 25; Anne says she inherited her talkativeness from her mother |\n"
          "| **Margot** | her elder sister, born in 1926 in Frankfurt; brilliant report card |\n"
          "| **Grandmother** | came to live with them; died in January 1942; Anne lit a candle for her on her birthday |\n"
          "| **Mrs Kuperus** | headmistress of her Montessori school; their parting was tearful |\n"
          "| **Mr Keesing** | old-fogey maths teacher; set essays on 'chatterbox' as punishment, then laughed at her poem |")
ESSAYS = ("| Punishment | Anne's answer |\n|---|---|\n"
          "| **'A Chatterbox'** | talking is a student's trait; she will try, but may never be cured, as her mother talks as much |\n"
          "| **'An Incorrigible Chatterbox'** | she wrote it and handed it in; Mr Keesing had no complaints for two lessons |\n"
          "| **'Quack, Quack, Quack, Said Mistress Chatterback'** | a poem (with her friend Sanne) about a mother duck and a father swan, who bit his three quacking ducklings to death; Mr Keesing took the joke well |")

sections = [
 {"id": "s1", "title": "A girl and her diary", "blocks": [
  blk("s1.hook", "hook", title="'Paper has more patience than people'",
    body="On her **thirteenth birthday** a girl in Amsterdam received a diary. She named it **Kitty** and wrote to it as her closest friend.\n\n"
         "Two years later she was dead, a victim of the Nazi persecution of Jews. Her diary survived and is now read in more than 70 languages. In this chapter we read the opening pages: why she writes, her family, and a funny battle with a maths teacher."),
  blk("s1.inspiration", "inspiration", title="The writer", person="Anne Frank", years="1929–1945",
    body="**Anne Frank** was born in Frankfurt, Germany, on **12 June 1929**. Her Jewish family moved to Amsterdam in Holland in 1933 to escape the Nazis. From 1942 they hid in a secret annexe; in 1944 they were discovered. Anne died in the **Bergen-Belsen** concentration camp in 1945.\n\n"
         "Her father **Otto Frank**, the only survivor of the family, published her diary, written in **Dutch**. It is one of the most widely read books in the world.",
    future="Writing a journal builds clear thinking and honest expression, skills used by writers, journalists and historians."),
  C.socratic("s1.socratic", "Anne had loving parents, a sister and about thirty friends, yet she felt alone. How is that possible?",
    ["She could not share her deepest feelings with any of them", "She had no family", "She did not like her friends at all"], 0,
    "She lacked one true friend to confide in, so she turned to her diary."),
 ]},
 {"id": "s2", "title": "Why Anne keeps a diary", "blocks": [
  blk("s2.thm", "theory", title="Saturday, 20 June 1942", revision=True,
    body="**A strange experience:** Anne says writing a diary is strange for someone like her: she has never written anything before, and she thinks neither she nor anyone else will be interested in 'the musings of a thirteen-year-old schoolgirl'.\n\n"
         "**'Paper has more patience than people.'** She remembers this saying from a day when she sat at home, bored and low, unsure whether to stay in or go out. Paper will listen without getting tired.\n\n"
         "**No real friend:** she has loving parents, a sixteen-year-old sister and about thirty people she can call friends, and admirers too, but she cannot get close to anyone. With friends she talks only of ordinary things. 'That's the root of the problem.' So the diary will be her friend, and she names it **Kitty**.\n\n"
         "**Not a list of facts:** she does not want to jot down facts in a diary 'the way most people would do'; she wants the diary itself to be her friend. So she first gives Kitty a **brief sketch of her life**."),
  C.kc("s2.check", "Why did Anne name her diary 'Kitty'?",
    [("she wanted the diary to be her close friend", ""), ("Kitty was her sister's name", "Her sister was Margot."),
     ("her teacher told her to", "It was her own idea."), ("it was the name of the shop", "She wanted a friend.")],
    "She wanted to confide in it as in a friend.")
  ,C.kc("s2.check2", "What does 'paper has more patience than people' mean?",
    [("you can write anything on paper and it will not get tired of listening", ""), ("paper lasts longer than people", "It is about listening, not time."),
     ("people should use more paper", "It is about confiding."), ("paper is expensive", "It is about patience.")],
    "Anne remembered this saying on a day she felt bored and low.")
 ]},
 {"id": "s3", "title": "Anne's family and Mr Keesing", "blocks": [
  blk("s3.thm", "theory", title="Family sketch and the chatterbox essays", revision=True,
    body="**Family:** her father married at 36, her mother at 25. Her sister **Margot** was born in **Frankfurt** in 1926; Anne on **12 June 1929**. Being **Jewish**, the family emigrated to **Holland in 1933**, where her father became Managing Director of the **Dutch Opekta Company**, which made products used in making jam. Her **grandmother** came to live with them and died in **January 1942**; no one knows how often Anne thinks of her. Her birthday in 1942 was celebrated to make up for the one in 1941, and a candle was lit for her grandmother.\n\n"
         "**School:** she went to a **Montessori nursery school** and stayed there until the sixth form, when her teacher was the headmistress **Mrs Kuperus**; they had a tearful farewell. Later she went to the **Jewish Lyceum**.\n\n"
         "**Mr Keesing:** her old maths teacher was annoyed because she talked so much. As punishment he gave her an essay, **'A Chatterbox'**. Anne argued that talking is a student's trait and that she had inherited it from her mother, so she could never be cured. Mr Keesing laughed, but when she went on talking he assigned **'An Incorrigible Chatterbox'**, and then **'Quack, Quack, Quack, Said Mistress Chatterback'**. With her friend **Sanne**, good at poetry, she wrote a poem about a mother duck and a father swan with three baby ducklings who were bitten to death by their father because they quacked too much. Mr Keesing took the joke the right way, read the poem aloud to the class, and from then on **allowed her to talk** and gave her no more extra homework."),
  blk("s3.table", "markdown_table", title="The people in Anne's sketch", revision=True, body=FAMTAB),
  blk("s3.table2", "markdown_table", title="Three punishments, three clever replies", revision=True, body=ESSAYS),
  C.kc("s3.check", "Why was Mr Keesing annoyed with Anne?",
    [("she talked too much in class", ""), ("she failed in maths", "He was annoyed by her talking."), ("she was late every day", "She talked too much."), ("she did not do homework", "She did every essay.")],
    "So he gave her essays on being a chatterbox.")
  ,C.kc("s3.check2", "How did Anne justify talking in her first essay?",
    [("talking is a student's trait, and she had inherited it from her mother", ""), ("talking helps her learn maths", "She argued it was inherited."),
     ("Mr Keesing talks too", "She blamed her mother's talkativeness."), ("everyone else was talking", "She gave reasons about herself.")],
    "Her argument was clever and amusing.")
 ]},
 {"id": "s4", "title": "Anne as a person; language", "blocks": [
  blk("s4.thm", "theory", title="What the diary shows about Anne", revision=True,
    body="- **Thoughtful and honest:** she looks into her own feelings ('We don't seem to be able to get any closer, and that's the problem').\n- **Lonely:** many friends but no confidant.\n"
         "- **Loving:** she adores her father and misses her grandmother.\n- **Witty and confident:** she turns punishment into clever essays and a poem.\n- **Mature beyond her age:** she sees through people and writes with insight.\n\n"
         "| Word or phrase | Meaning |\n|---|---|\n| **musings** | thoughts, reflections |\n| **confide** | to share secrets with someone you trust |\n| **listless** | without energy |\n"
         "| **brooding** | thinking deeply, often sadly |\n| **incorrigible** | that cannot be corrected or changed |\n| **old fogey** | an old-fashioned person |\n| **chatterbox** | someone who talks too much |\n| **ingenious** | very clever |"),
  C.kc("s4.check", "'Incorrigible' means:",
    [("that cannot be corrected", ""), ("very intelligent", "It means beyond correction."), ("very quiet", "It means the opposite of improving."), ("polite", "It means beyond correction.")],
    "'An Incorrigible Chatterbox' was the second essay.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Dates: born 12 June 1929; diary entry 20 June 1942; moved to Holland 1933; grandmother died January 1942.**\n"
         "- **Essays: Chatterbox → Incorrigible Chatterbox → Quack, Quack, Quack (poem with Sanne).**\n- **Teachers: Mrs Kuperus (kind, tearful farewell); Mr Keesing (maths, punishments, then a good sport).**\n"
         "- **Diary = Kitty; language = Dutch.**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Writing that Anne had no friends: she had about **thirty friends**, but no one to confide in.\n2. Calling Mr Keesing cruel: he was annoyed, but he **took the poem as a joke** and let her talk.\n"
         "3. Saying the diary was written in English: it was written in **Dutch**.\n4. Mixing up Margot (sister) and Kitty (the diary)."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Ask each student to write a four-line diary entry about one school day, addressed to a named diary. Then discuss: how is writing to 'a friend' different from listing facts?"),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Is a diary a good substitute for a friend? What can a diary give you that a friend cannot, and what can a friend give that a diary cannot?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **History (The Rise of Nationalism in Europe):** extreme nationalism later led to the Nazi persecution that Anne's family fled.\n- **Nelson Mandela (Ch 2):** another life story of resisting injustice.\n- **Writing:** diary entries are a common creative task."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="'Anne was right that no one would be interested in the musings of a thirteen-year-old schoolgirl.' Do you agree? Answer in about 120 words.\n\n"
         "**Model answer:** No, Anne was wrong, though she could not have known it. She thought a schoolgirl's thoughts would interest no one, so she wrote mainly for herself and for 'Kitty'. But her honest, lively diary became one of the most widely read books in the world. Readers value it because it shows the everyday feelings of a teenager, such as loneliness, love for her father and fun with a strict teacher, against the dark background of the Nazi persecution of Jews. Her wit, as in the 'Quack, Quack, Quack' poem, and her insight into people make her real to us. Her diary turned a private voice into a lasting record of history."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Anne Frank, given a diary on her 13th birthday, names it Kitty and makes it her friend because she cannot confide in anyone.\n"
         "- 'Paper has more patience than people.'\n- She sketches her family: German Jews who moved to Holland in 1933; her father, mother, sister Margot and beloved grandmother.\n"
         "- At school, Mr Keesing punishes her talkativeness with three essays; her clever poem wins him over and he lets her talk.\n"
         "- The diary shows Anne as honest, lonely, loving, witty and mature."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- For questions on Anne's character, pair each quality with an example (witty: the duck poem; loving: candle for grandmother).\n"
         "- Remember the order and titles of the three essays; questions often ask about them.\n- For 'Is Mr Keesing unpredictable?', show his change: punishment → laughter → acceptance."),
  blk("s5.flash1", "flashcard", front="Why did Anne feel lonely though she had many friends?", back="She could not confide her deepest feelings in any of them; they talked only of ordinary things."),
  blk("s5.flash2", "flashcard", front="What were the three essays Mr Keesing set?", back="'A Chatterbox', 'An Incorrigible Chatterbox' and 'Quack, Quack, Quack, Said Mistress Chatterback'."),
  blk("s5.flash3", "flashcard", front="In what language was the diary written?", back="Dutch."),
  blk("s5.flash4", "flashcard", front="How did Mr Keesing react to the duck poem?", back="He took it as a joke, read it to the class and allowed Anne to talk from then on."),
 ]},
]

# ---------------- NCERT: Oral Comprehension Check ----------------
C.vsa("occ1", DIARY, "What makes writing in a diary a strange experience for Anne Frank?",
      ["She had never written anything before.", "She felt no one would be interested in the musings of a thirteen-year-old schoolgirl."], OCC(1))
C.vsa("occ2", DIARY, "Why does Anne want to keep a diary?",
      ["She wanted to write and get things off her chest.", "She had no true friend to confide in, so the diary would be her friend."], OCC(2))
C.vsa("occ3", DIARY, "Why did Anne think she could confide more in her diary than in people?",
      ["Paper has more patience than people.", "With people she could talk only about everyday things, not her deep feelings."], OCC(3))
C.vsa("occ4", FAMILY, "Why does Anne provide a brief sketch about her family?",
      ["She treats Kitty as a friend who needs to know her.", "No one would understand her stories without knowing her background."], OCC(4))
C.vsa("occ5", FAMILY, "What tells you that Anne loved her grandmother?",
      ["She says no one knows how often she thinks of her and still loves her.", "On her birthday a candle was lit for her grandmother."], OCC(5))
C.vsa("occ6", SCHOOL, "Why was Mr Keesing annoyed with Anne? What did he ask her to do?",
      ["She talked too much in class.", "He asked her to write an essay titled 'A Chatterbox'."], OCC(6))
C.vsa("occ7", SCHOOL, "How did Anne justify her being a chatterbox in her essay?",
      ["She said talking is a student's trait.", "She had inherited it from her mother, who talked as much, so it could not be cured."], OCC(7))
C.vsa("occ8", DIARY, "Do you think a diary is a good substitute for a friend? Why?",
      ["Partly: it listens patiently and keeps secrets, which helps to sort out feelings.", "But it cannot reply, advise or comfort the way a real friend can."], OCC(8))
C.vsa("occ9", SCHOOL, "What made Mr Keesing allow Anne to talk in class?",
      ["Her funny poem 'Quack, Quack, Quack, Said Mistress Chatterback'.", "He took the joke well, read it aloud and stopped punishing her."], OCC(9))

# ---------------- NCERT: Thinking about the Text ----------------
C.sa("ex1", DIARY, "Was Anne right when she said that the world would not be interested in the musings of a thirteen-year-old girl?",
     ["No, she was wrong.", "Her diary became one of the most widely read books, read in many languages, because it shows a teenager's honest feelings during the Nazi persecution."], ex(1))
C.sa("ex2", DIARY, "Compare Anne's diary with ordinary diary entries. What language was the diary originally written in?",
     ["Ordinary entries list events and facts; Anne writes to 'Kitty' as to a friend, sharing feelings and thoughts.", "The diary was originally written in Dutch."], ex(2))
C.sa("ex3", FAMILY, "Why does Anne provide a brief sketch about her family? Does she treat 'Kitty' as an insider or an outsider?",
     ["She wants Kitty to know her before she shares her stories.", "She treats Kitty as an insider, a close friend, though she begins by introducing herself."], ex(3))
C.sa("ex4", ANNE, "How does Anne feel about her father, her grandmother, Mrs Kuperus and Mr Keesing? What do these tell you about her?",
     ["She adores her father, loves and misses her grandmother, and is fond of Mrs Kuperus; she respects Mr Keesing after his change.", "This shows she is loving, sensitive and fair-minded."], ex(4))
C.sa("ex5", SCHOOL, "What does Anne write in her first essay?",
     ["That talking is a student's trait and she would try to control it.", "But she could never cure it, since she inherited it from her mother, who talked as much."], ex(5))
C.sa("ex6", SCHOOL, "Anne says teachers are most unpredictable. Is Mr Keesing unpredictable? How?",
     ["Yes. He punished her talkativeness with essays and seemed strict.", "Yet he laughed at her arguments, took her poem as a joke, read it aloud and then allowed her to talk."], ex(6))
C.sa("ex7", ANNE, "What do these statements tell you about Anne: (i) 'We don't seem to be able to get any closer, and that's the problem.' (ii) 'I don't want to jot down the facts in this diary the way most people would.'",
     ["(i) She is introspective and lonely; she wants a deep friendship.", "(ii) She is original and wants the diary to be a real friend, not a record of facts."], ex(7))

# ---------------- Extracts ----------------
C.extract("ext1", DIARY,
  "Writing in a diary is a really strange experience for someone like me.\nNot only because I've never written anything before, but also because it seems to me that later on\nneither I nor anyone else will be interested in the musings of a thirteen-year-old schoolgirl.",
  [("Who is 'me' in the extract?", "Anne Frank."),
   ("Why is writing a diary strange for her? (any one)", "She has never written anything before."),
   ("What does 'musings' mean?", "Thoughts or reflections."),
   ("How old was she?", "Thirteen."),
   ("Was she right that no one would be interested?", "No; her diary became world-famous.")])
C.extract("ext2", DIARY,
  "'Paper has more patience than people.' I thought of this saying on one of those days when I was feeling a little depressed\nand was sitting at home with my chin in my hands, bored and listless.",
  [("Who thought of this saying?", "Anne Frank."),
   ("What does the saying mean?", "Paper listens patiently to anything you write."),
   ("How was she feeling that day?", "A little depressed, bored and listless."),
   ("Find a word meaning 'without energy'.", "Listless."),
   ("What did this saying lead her to do?", "To keep a diary as her friend.")])
C.extract("ext3", SCHOOL,
  "Mr Keesing, the old fogey who teaches maths, was annoyed with me for ages because I talked so much.\nAfter several warnings, he assigned me extra homework.\nAn essay on the subject, 'A Chatterbox'.",
  [("What does 'old fogey' mean?", "An old-fashioned person."),
   ("Why was Mr Keesing annoyed?", "Anne talked too much in class."),
   ("What extra homework did he give?", "An essay titled 'A Chatterbox'."),
   ("What did Anne argue in it?", "Talking is a student's trait, inherited from her mother."),
   ("How did Mr Keesing finally react?", "He took her poem as a joke and let her talk.")])
C.extract("ext4", SCHOOL,
  "Mr Keesing was trying to play a joke on me with this ridiculous subject,\nbut I'd make sure the joke was on him.",
  [("Which 'ridiculous subject' is meant?", "'Quack, Quack, Quack, Said Mistress Chatterback'."),
   ("How did Anne make the joke 'on him'?", "She wrote a funny poem about ducks and a swan."),
   ("Who helped her write it?", "Her friend Sanne."),
   ("What does this show about Anne?", "She is witty and confident."),
   ("Give the opposite of 'ridiculous'.", "Sensible.")])

# ---------------- Objective practice ----------------
C.m("mcq01", DIARY, "Anne received the diary on:",
    [("her thirteenth birthday", ""), ("her twelfth birthday", "It was her thirteenth."), ("New Year's Day", "It was a birthday gift."), ("her first day at school", "It was a birthday gift.")],
    "She was born on 12 June 1929.")
C.m("mcq02", DIARY, "What name did Anne give her diary?",
    [("Kitty", ""), ("Margot", "That was her sister."), ("Sanne", "That was her friend."), ("Paper", "She called it Kitty.")],
    "She wanted it to be her friend.")
C.m("mcq03", FAMILY, "Where was Anne born?",
    [("Frankfurt, Germany", ""), ("Amsterdam, Holland", "The family moved there later."), ("London", "She was born in Germany."), ("Paris", "She was born in Frankfurt.")],
    "The family moved to Holland in 1933.")
C.m("mcq04", FAMILY, "Why did Anne's family emigrate to Holland?",
    [("because they were Jewish", ""), ("for a holiday", "They left to escape persecution."), ("because her father was a teacher there", "He worked at Opekta."), ("to join her grandmother", "Her grandmother joined them.")],
    "Anti-Jewish laws were starting in Germany in 1933.")
C.m("mcq05", FAMILY, "Anne's father became Managing Director of:",
    [("the Dutch Opekta Company", ""), ("a bank", "It was a company making jam products."), ("a school", "It was the Opekta Company."), ("a newspaper", "It was the Opekta Company.")],
    "The company made products used in making jam.")
C.m("mcq06", FAMILY, "When did Anne's grandmother die?",
    [("January 1942", ""), ("June 1942", "That was Anne's 13th birthday."), ("1933", "That was the move to Holland."), ("1945", "That is when Anne died.")],
    "A candle was lit for her on Anne's birthday.")
C.m("mcq07", SCHOOL, "Who was the headmistress of Anne's Montessori school?",
    [("Mrs Kuperus", ""), ("Mrs Keesing", "Mr Keesing was the maths teacher."), ("Mrs Frank", "That was her mother."), ("Mrs Sanne", "Sanne was a friend.")],
    "Their farewell was tearful.")
C.m("mcq08", SCHOOL, "What subject did Mr Keesing teach?",
    [("mathematics", ""), ("history", "He taught maths."), ("English", "He taught maths."), ("science", "He taught maths.")],
    "Anne calls him 'the old fogey who teaches maths'.")
C.m("mcq09", SCHOOL, "What was the title of the second essay?",
    [("An Incorrigible Chatterbox", ""), ("A Chatterbox", "That was the first."), ("Quack, Quack, Quack, Said Mistress Chatterback", "That was the third."), ("My Diary", "It was about chattering.")],
    "Each title was meant to tease her.")
C.m("mcq10", SCHOOL, "In the poem, what happened to the three baby ducklings?",
    [("their father bit them to death because they quacked too much", ""), ("they flew away", "Their father bit them."),
     ("they learnt to be quiet", "They were bitten to death."), ("they won a prize", "It is a comic poem about too much quacking.")],
    "The poem was a joke about chattering.")
C.m("mcq11", SCHOOL, "Who helped Anne write the poem?",
    [("her friend Sanne", ""), ("her sister Margot", "Sanne helped her."), ("her father", "Sanne helped."), ("Mrs Kuperus", "Sanne helped.")],
    "Sanne was good at poetry.")
C.m("mcq12", ANNE, "Which quality of Anne is shown by her reply to Mr Keesing's punishments?",
    [("wit and confidence", ""), ("fear", "She was not afraid."), ("laziness", "She did every task."), ("rudeness", "Her answers were clever, not rude.")],
    "She turned punishment into fun.")
C.m("mcq13", DIARY, "Anne's main problem with her friends was that:",
    [("she could not confide in them", ""), ("they were cruel", "They were friends, just not close."), ("she had none", "She had about thirty."), ("they lived far away", "She could not get close to them.")],
    "'That's the root of the problem.'")
C.m("mcq14", LANG, "'Musings' means:",
    [("thoughts and reflections", ""), ("songs", "It means thoughts."), ("complaints", "It means thoughts."), ("games", "It means thoughts.")],
    "The musings of a thirteen-year-old schoolgirl.")
C.m("mcq15", SCHOOL, "How did Mr Keesing finally react?",
    [("he read the poem to the class and allowed Anne to talk", ""), ("he gave her another essay", "He stopped punishing her."),
     ("he complained to her parents", "He took the joke well."), ("he failed her", "He let her talk.")],
    "He took the joke the right way.")
C.m("mcq16", FAMILY, "Who was Margot?",
    [("Anne's elder sister", ""), ("Anne's mother", "Her mother was Edith."), ("Anne's friend", "Margot was her sister."), ("Anne's teacher", "Margot was her sister.")],
    "She was born in 1926.")
C.tf("tf1", DIARY, "Anne wanted to list facts in her diary like most people.", False, "She wanted the diary to be her friend, not a list of facts.")
C.tf("tf2", FAMILY, "Anne's family was Jewish.", True, "That is why they left Germany in 1933.")
C.tf("tf3", SCHOOL, "Mr Keesing set Anne three essays as punishment for talking.", True, "A Chatterbox, An Incorrigible Chatterbox, and Quack, Quack, Quack.")
C.tf("tf4", DIARY, "Anne's diary was originally written in English.", False, "It was written in Dutch.")

# ---------------- More written practice ----------------
C.sa("sa1", ANNE, "Describe Anne's relationship with her father.",
     ["She calls him 'the most adorable father I've ever seen'.", "This shows her deep love and admiration for him."])
C.sa("sa2", SCHOOL, "How did Anne turn the third punishment into a victory?",
     ["She wrote a funny poem with Sanne about a mother duck, a father swan and three chattering ducklings.", "Mr Keesing laughed, read it aloud and never punished her again."])
C.la("la1", ANNE, "Write a character sketch of Anne Frank based on the chapter.",
     ["Anne is thoughtful and honest: she looks into her own loneliness.", "She is loving: she adores her father and lights a candle for her grandmother.",
      "She is witty and confident: she answers Mr Keesing's punishments with clever arguments and a comic poem.",
      "She is mature beyond her age: she writes with insight about people.", "Her diary shows a lively teenager in dark times, which is why the world still reads it."])
C.la("la2", SCHOOL, "'Teachers are most unpredictable.' Discuss with reference to Mr Keesing.",
     ["Mr Keesing seemed strict: he was annoyed at Anne's talking and set her extra essays.", "He kept raising the punishment with teasing titles.",
      "But he laughed at her argument in the first essay, and accepted the duck poem as a joke.", "He read it aloud and let her talk from then on.",
      "His change from strictness to good humour shows he was unpredictable, and also fair."])
C.la("la3", DIARY, "Imagine you are Anne. Write a diary entry to Kitty about the day Mr Keesing read your poem to the class.",
     ["Address: 'Dear Kitty' and the date.", "Describe how you and Sanne wrote the duck poem.", "Describe Mr Keesing reading it aloud and the class laughing.",
      "Your feelings: relief and pride; he will now let you talk."])

chapter = header("ch04", 4, "From the Diary of Anne Frank", "Anne Frank", "prose",
                 ["why_a_diary", "family_background", "mr_keesing_and_the_essays", "anne_as_a_person", "vocabulary_and_style"],
                 "CBSE 2025-26 English Language and Literature (184): First Flight prose, Chapter 4. Assessed through extracts (5 marks), short answers in 40-50 words (3 marks) and long answers in 100-120 words (6 marks).")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
