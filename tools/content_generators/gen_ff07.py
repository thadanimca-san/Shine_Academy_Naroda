"""CBSE Class 10 English, First Flight Ch 7: Madam Rides the Bus (Vallikkannan)."""
import sys
from lit_common import make, header, path, ex

ROOT = sys.argv[1]
PATH = path("ch07_madam_rides_the_bus")
C = make("ff10ch07")
blk = C.blk
PLAN, RIDE, VALLI, DEATH, LANG = ["vallis_plan"], ["the_bus_ride"], ["valli_as_a_person"], ["first_encounter_with_death"], ["vocabulary_and_style"]
OCC = lambda n: ex(n, "Oral Comprehension Check")

PLANTAB = ("| What Valli did | Why |\n|---|---|\n"
           "| listened to neighbours' talk about the bus and asked questions | to learn how the journey works |\n"
           "| found out the fare: **thirty paise** one way, so **sixty paise** for both | to know how much to save |\n"
           "| found out the time: **forty-five minutes** to the town | so she could be back before anyone noticed |\n"
           "| saved every coin, resisting peppermints, toys, balloons and rides | to collect sixty paise |\n"
           "| chose the hours when her mother took her **afternoon nap** | to go and return without being missed |")

sections = [
 {"id": "s1", "title": "An eight-year-old's adventure", "blocks": [
  blk("s1.hook", "hook", title="The bus at the door",
    body="Every day a bus passed the door of eight-year-old **Valli**'s house. Every day she watched it and longed to ride it to the town, just for the joy of the ride.\n\n"
         "This is the story of how she planned, saved and finally took that ride on her own, and how the journey taught her about the beauty and the sadness of the world."),
  blk("s1.inspiration", "inspiration", title="The writer", person="Vallikkannan", years="1920–2006",
    body="**Vallikkannan** (R. S. Krishnaswamy) was a well-known **Tamil** writer of short stories, novels and essays. This story, translated from Tamil by the writer himself, sees the world through the eyes of a curious, independent village girl.",
    future="Good stories notice small details of everyday life; writers, film-makers and teachers learn to see like children."),
  C.socratic("s1.socratic", "Valli refused the elderly woman's friendship and the conductor's offer of a drink. What does this tell us about her?",
    ["She was independent and proud, and wanted to be treated as a grown-up", "She was rude to everyone", "She was very shy and afraid of people"], 0,
    "She wanted to do everything on her own, like an adult."),
 ]},
 {"id": "s2", "title": "The plan and the ride", "blocks": [
  blk("s2.thm", "theory", title="What happens in the story", revision=True,
    body="**The longing:** Valli (Valliammai), eight years old, stood at the front doorway of her house watching the street. Her favourite pastime was watching the **bus** that travelled between her village and the nearest town. Her deepest desire was to ride on it.\n\n"
         "**The plan:** by listening to neighbours and asking a few discreet questions, she learnt that the town was six miles away, the fare was **thirty paise one way**, and the trip took **forty-five minutes**. She saved every coin, resisting the temptation to buy **peppermints, toys, balloons** and a ride on the merry-go-round, until she had **sixty paise**. She chose a day when her mother took her **afternoon nap** (from about one to four).\n\n"
         "**Boarding:** at about one o'clock she caught the bus. The **conductor** joked with her, calling her **'Madam'**, and when he tried to help her up she said she could manage herself. She paid her fare like a grown-up and sat by the window, standing on the seat to see outside.\n\n"
         "**The elderly woman:** a woman with big **earrings** stretching her ear lobes asked her where she was going alone. Valli found her **ugly** and her questions annoying, and refused to make friends: 'I can take care of myself.'\n\n"
         "**The views:** she saw a **canal**, palm trees, grassland, distant mountains and the blue sky. A young **cow** ran in front of the bus with its tail high, and Valli **laughed** till tears came to her eyes.\n\n"
         "**At the town:** she did not get off. She stayed in the bus to return by the same bus, since she had money only for the return fare. The conductor offered to buy her a **drink**; she refused, saying she had no money and would not accept charity.\n\n"
         "**The return:** on the way back she saw the **same young cow lying dead** by the road, hit by a vehicle. The sight frightened and saddened her: the joy of the window view was gone. She reached home in time, and kept her adventure a **secret**."),
  blk("s2.table", "markdown_table", title="How Valli planned her trip", revision=True, body=PLANTAB),
  C.kc("s2.check", "How much did Valli need for the round trip?",
    [("sixty paise", ""), ("thirty paise", "That was one way."), ("one rupee", "Sixty paise."), ("ten paise", "Sixty paise.")],
    "The fare was thirty paise each way.")
  ,C.kc("s2.check2", "Why did Valli laugh during the journey?",
    [("a young cow ran in front of the bus with its tail up", ""), ("the conductor told a joke", "It was the cow."),
     ("the elderly woman fell", "It was the cow."), ("she saw a monkey", "It was the cow.")],
    "She laughed until tears came to her eyes.")
 ]},
 {"id": "s3", "title": "Valli as a person; the turning point", "blocks": [
  blk("s3.thm", "theory", title="Character and theme", revision=True,
    body="**Curious:** she watches the street and the bus every day and asks questions.\n\n"
         "**Determined and patient:** she saves for a long time, giving up sweets and toys.\n\n"
         "**Independent and proud:** she climbs in herself, pays her own fare, tells the conductor she is not a child, and refuses the drink: she will not accept **charity**.\n\n"
         "**Practical and mature:** she stays in the bus at the town because she has only the return fare, and returns in time.\n\n"
         "**Sensitive:** the dead cow upsets her deeply. It is her **first encounter with death**: the story moves from the **joy** of the outward journey to the **sorrow** of the return. Valli grows up a little: she learns that life has both beauty and loss.\n\n"
         "**Humour:** the conductor's teasing 'Madam' and Valli's serious replies make the story gently funny."),
  C.kc("s3.check", "Why did Valli refuse the conductor's offer of a drink?",
    [("she did not want to accept charity and had no extra money", ""), ("she did not like drinks", "She refused out of pride."),
     ("her mother had forbidden it", "Her mother did not know she was out."), ("the drink was cold", "She refused out of self-respect.")],
    "She wanted to be independent.")
  ,C.kc("s3.check2", "What changed Valli's mood on the return journey?",
    [("she saw the young cow lying dead by the road", ""), ("the bus broke down", "It was the dead cow."), ("she lost her money", "It was the dead cow."), ("it began to rain", "It was the dead cow.")],
    "Her joy turned to sorrow.")
 ]},
 {"id": "s4", "title": "Language of the story", "blocks": [
  blk("s4.thm", "theory", title="Words and expressions to know", revision=True,
    body="| Word or phrase | Meaning |\n|---|---|\n| **discreet** | careful, without drawing attention |\n| **fare** | the price of a journey |\n"
         "| **pastime** | something done for enjoyment |\n| **intently** | with close attention |\n| **mature** | grown-up in thinking |\n"
         "| **charity** | help given to someone who needs it |\n| **'Madam'** | the conductor's playful way of treating Valli as a lady |\n\n"
         "**Style:** a third-person narrator shows Valli's thoughts; humour (Madam) and contrast (living cow / dead cow) carry the theme."),
  C.kc("s4.check", "'Discreet questions' are questions asked:",
    [("carefully, without drawing attention", ""), ("loudly", "It means carefully."), ("rudely", "It means carefully."), ("in writing", "It means carefully.")],
    "Valli did not want anyone to guess her plan.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Numbers: age 8; 6 miles; 30 paise one way; 60 paise return; 45 minutes; mother's nap 1 to 4.**\n- **Journey: canal → palms → grassland → mountains → cow running (laugh) → town → cow dead (sad).**\n"
         "- **Valli says no three times: to help climbing in, to the old woman's friendship, to the free drink.**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying Valli explored the town: she **stayed in the bus** and came back.\n2. Saying her mother knew: Valli went during her mother's **nap** and kept it **secret**.\n"
         "3. Calling Valli rude: she was **proud and independent**, not deliberately rude.\n4. Forgetting the dead cow: it is the **turning point** of the story."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Draw two columns: 'Going' and 'Returning'. Students list Valli's feelings and sights in each. The contrast shows the theme of joy and death."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Have you ever saved for something you wanted very much? How did it feel when you finally got it? Was it exactly what you expected?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **The Ball Poem:** a boy's first lesson in loss.\n- **The Sermon at Benares:** accepting death as part of life.\n- **Anne Frank:** another independent young girl."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="'Valli was mature for her age.' Do you agree? Answer in about 120 words.\n\n"
         "**Model answer:** Yes, eight-year-old Valli shows a maturity beyond her years. She plans her trip like an adult: through discreet questions she learns the distance, the fare of thirty paise each way and the time of forty-five minutes. She saves sixty paise patiently, giving up sweets, toys and rides. She chooses her mother's nap time so she will not be missed. On the bus she pays her own fare and politely but firmly refuses help, friendship and a free drink, unwilling to accept charity. At the town she wisely stays in the bus, as she has only her return fare. Her deep sadness at the dead cow shows sensitivity too. Yet her delight at the running cow reminds us she is still a child."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Valli, 8, longs to ride the bus that passes her village to the town.\n- She learns the fare (30 paise each way) and time (45 minutes), saves 60 paise and goes during her mother's nap.\n"
         "- On the bus she is independent: refuses help, the elderly woman's friendship and the conductor's drink.\n"
         "- She enjoys the views and laughs at a cow running before the bus; on the return she sees the cow dead and is saddened.\n"
         "- She returns home safely and keeps her adventure secret."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- For character questions, choose three qualities and prove each with an action.\n- Quote numbers exactly (30 paise, 60 paise, 45 minutes); they show careful reading.\n"
         "- For the theme, contrast the outward and return journeys."),
  blk("s5.flash1", "flashcard", front="What was Valli's deepest desire?", back="To ride on the bus from her village to the town."),
  blk("s5.flash2", "flashcard", front="How did Valli raise the money?", back="She saved every coin and resisted buying peppermints, toys and balloons until she had sixty paise."),
  blk("s5.flash3", "flashcard", front="Why did Valli not get off at the town?", back="She had money only for the return fare, so she stayed in the bus."),
  blk("s5.flash4", "flashcard", front="What saddened Valli on the way back?", back="The young cow she had laughed at was lying dead by the road."),
 ]},
]

# ---------------- NCERT ----------------
C.vsa("occ1", PLAN, "What was Valli's favourite pastime?",
      ["Standing at the front door watching the street.", "Above all, watching the bus that went between her village and the town."], OCC(1))
C.vsa("occ2", PLAN, "What was a source of unending joy for Valli? What was her deepest desire?",
      ["Watching the bus and the new set of passengers each time.", "Her deepest desire was to ride on that bus."], OCC(2))
C.vsa("occ3", PLAN, "What did Valli find out about the bus journey? How did she find out these details?",
      ["The town was six miles away, the fare was thirty paise one way and the trip took forty-five minutes.", "She listened to neighbours and asked discreet questions."], OCC(3))
C.vsa("occ4", RIDE, "Why did the conductor call Valli 'Madam'?",
      ["She spoke and behaved like a grown-up lady.", "She insisted on doing everything herself, so he teased her playfully."], OCC(4))
C.sa("ex1", VALLI, "Why didn't Valli want to make friends with the elderly woman?",
     ["She found the woman ugly, with ear lobes stretched by heavy earrings, and chewing betel.", "She disliked being treated as a child; she said she could take care of herself."], ex(1))
C.sa("ex2", RIDE, "Why didn't Valli get off the bus at the bus station in the town?",
     ["She had money only for the return fare.", "So she stayed in the bus and returned by it."], ex(2))
C.sa("ex3", VALLI, "Why didn't Valli want to go to the stall and have a drink? What does this tell you about her?",
     ["She had no money for it and would not accept a free drink.", "It shows she was proud and independent and did not want charity."], ex(3))
C.sa("ex4", DEATH, "What happened on the return journey that saddened Valli?",
     ["She saw the young cow, which had run before the bus earlier, lying dead by the roadside.", "It had been hit by a vehicle; the sight took away all her joy."], ex(4))

# ---------------- Extracts ----------------
C.extract("ext1", PLAN,
  "Valli stood at the front doorway of her house, looking out at what was happening in the street.\nThere were no playmates of her age on her street, and this was about all she had to do.",
  [("How old was Valli?", "Eight."),
   ("Where was she standing?", "At the front doorway of her house."),
   ("Why did she spend time watching the street?", "She had no playmates of her age there."),
   ("What on the street interested her most?", "The bus to the town."),
   ("Give a word from the story meaning 'hobby'.", "Pastime.")])
C.extract("ext2", RIDE,
  "'Stand back, stand back,' said the conductor. 'Here comes a madam.'\nValli did not like being called 'madam' by him, and she said, 'I'm not a madam.'",
  [("Who calls Valli 'madam'?", "The bus conductor."),
   ("Why does he call her that?", "She acts like a grown-up lady; he is teasing her."),
   ("What tone does he use?", "Playful, joking."),
   ("What does Valli's reply show?", "She is independent and self-respecting."),
   ("Who is the 'madam' in the title of the story?", "Valli.")])
C.extract("ext3", DEATH,
  "It was the same young cow, lying dead by the roadside, just where it had been struck by some passing vehicle.\nValli no longer wanted to look out of the window.",
  [("Which cow is meant?", "The young cow that had run in front of the bus earlier."),
   ("How had it died?", "It was hit by a passing vehicle."),
   ("How did Valli feel?", "Sad and frightened."),
   ("Why did she not want to look out now?", "The sight of death took away her joy."),
   ("What contrast does this create?", "Joy on the way to town, sorrow on the way back.")])

# ---------------- Objective practice ----------------
C.m("mcq01", PLAN, "How old was Valli?",
    [("eight", ""), ("ten", "She was eight."), ("six", "She was eight."), ("twelve", "She was eight.")],
    "She was a young girl.")
C.m("mcq02", PLAN, "How long did the bus take to reach the town?",
    [("forty-five minutes", ""), ("two hours", "45 minutes."), ("ten minutes", "45 minutes."), ("one hour", "45 minutes.")],
    "The town was six miles away.")
C.m("mcq03", PLAN, "What did Valli give up to save money?",
    [("peppermints, toys, balloons and merry-go-round rides", ""), ("her school fees", "She saved small coins."), ("her meals", "She gave up treats."), ("nothing", "She gave up treats.")],
    "She saved sixty paise.")
C.m("mcq04", PLAN, "When did Valli go on her bus ride?",
    [("in the afternoon, while her mother napped", ""), ("early morning", "In the afternoon."), ("at night", "In the afternoon."), ("on a school holiday with her mother", "Her mother did not know.")],
    "Her mother usually slept from one to four.")
C.m("mcq05", RIDE, "Where did Valli stand on the bus to see outside?",
    [("on the seat", ""), ("near the driver", "On the seat."), ("on the roof", "On the seat."), ("at the door", "On the seat.")],
    "The window was too high for her.")
C.m("mcq06", VALLI, "Why did Valli dislike the elderly woman?",
    [("she found her ugly and her questions annoying", ""), ("the woman was rude to her", "Valli simply disliked her."), ("the woman took her seat", "She disliked her looks and questions."), ("she owed her money", "She disliked her looks and questions.")],
    "The woman's ear lobes were stretched by big earrings.")
C.m("mcq07", RIDE, "Which of these did Valli NOT see on the way?",
    [("a big railway station", ""), ("a canal", "She saw a canal."), ("palm trees", "She saw palm trees."), ("mountains", "She saw distant mountains.")],
    "She saw nature on the way.")
C.m("mcq08", DEATH, "The dead cow represents Valli's:",
    [("first encounter with death", ""), ("happiest moment", "It saddened her."), ("fear of buses", "It is about death."), ("dislike of animals", "She had laughed with joy at the cow.")],
    "It is the turning point of the story.")
C.m("mcq09", VALLI, "Which word best describes Valli?",
    [("independent", ""), ("timid", "She travelled alone."), ("careless", "She planned carefully."), ("greedy", "She saved carefully.")],
    "She did everything by herself.")
C.m("mcq10", LANG, "'Charity' means:",
    [("help given freely to someone in need", ""), ("a bus fare", "It means free help."), ("a joke", "It means free help."), ("a ticket", "It means free help.")],
    "Valli would not accept charity.")
C.tf("tf1", PLAN, "Valli's mother knew about her bus ride.", False, "Valli went during her mother's nap and kept it secret.")
C.tf("tf2", RIDE, "Valli got off the bus and explored the town.", False, "She stayed in the bus because she had only the return fare.")
C.tf("tf3", PLAN, "The fare was thirty paise one way.", True, "So she needed sixty paise for the round trip.")
C.tf("tf4", DEATH, "Valli saw the young cow lying dead on her return journey.", True, "It had been hit by a vehicle.")

C.sa("sa1", PLAN, "How did Valli plan her journey?",
     ["She found out the fare, distance and time by listening and asking discreet questions.", "She saved sixty paise and chose her mother's nap time so no one would miss her."])
C.la("la1", VALLI, "Write a character sketch of Valli.",
     ["Valli is curious: she watches the bus every day and asks questions.", "She is determined: she saves sixty paise by giving up treats.",
      "She is independent and proud: she pays her own fare and refuses help, friendship and charity.", "She is practical: she stays on the bus as she has only the return fare.",
      "She is sensitive: the dead cow saddens her; her trip teaches her about life and death."])
C.la("la2", DEATH, "How does the outward journey differ from the return journey? What does this teach Valli?",
     ["Going, Valli is thrilled: she enjoys the canal, palm trees, mountains and laughs at the running cow.", "Returning, she sees the same cow dead and loses all interest in the view.",
      "The contrast moves the story from joy to sorrow.", "Valli learns that life includes death and loss, and she grows up a little."])

chapter = header("ch07", 7, "Madam Rides the Bus", "Vallikkannan", "prose",
                 ["vallis_plan", "the_bus_ride", "valli_as_a_person", "first_encounter_with_death", "vocabulary_and_style"],
                 "CBSE 2025-26 English Language and Literature (184): First Flight prose, Chapter 7. Assessed through extracts (5 marks), short answers in 40-50 words (3 marks) and long answers in 100-120 words (6 marks).")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
