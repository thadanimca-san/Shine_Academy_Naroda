"""CBSE Class 10 English, First Flight Ch 3: Two Stories about Flying
(I. His First Flight, Liam O'Flaherty; II. The Black Aeroplane, Frederick Forsyth)."""
import sys
from lit_common import make, header, path, ex

ROOT = sys.argv[1]
PATH = path("ch03_two_stories_about_flying")
C = make("ff10ch03")
blk = C.blk
GULL, FAMILY, PILOT, MYST, LANG = ["seagull_first_flight"], ["family_and_encouragement"], ["pilot_in_the_storm"], ["mystery_of_the_black_aeroplane"], ["vocabulary_and_style"]
EX1 = lambda n: ex(n, "Thinking about the Text (His First Flight)")
EX2 = lambda n: ex(n, "Thinking about the Text (The Black Aeroplane)")

COMPARE = ("| | His First Flight | The Black Aeroplane |\n|---|---|---|\n"
           "| **Who flies** | a young seagull | an experienced pilot in an old Dakota |\n"
           "| **The problem** | fear of the first flight | a storm, dead instruments and almost no fuel |\n"
           "| **Who helps** | his mother, by tempting him with a piece of fish | a mysterious black aeroplane with no lights |\n"
           "| **Turning point** | hunger makes him dive at the fish | he follows the black aeroplane through the clouds |\n"
           "| **Ending** | he flies, lands on the sea, and is praised by his family | he lands safely, but control says no other plane was flying |\n"
           "| **Message** | courage comes from facing fear; we sometimes need a push | help may come when we least expect it; mystery remains |")

sections = [
 {"id": "s1", "title": "Two first-time fears", "blocks": [
  blk("s1.hook", "hook", title="The edge of a cliff, the edge of a storm",
    body="A young seagull stands on a cliff ledge, too afraid to jump. A pilot flies into black storm clouds, his compass spinning and his radio dead.\n\n"
         "Both stories are about **flying** and about **fear**. In one, a hungry bird finds its wings; in the other, a pilot is guided home by a plane that, it seems, was never there."),
  blk("s1.inspiration", "inspiration", title="The writers", person="Liam O'Flaherty and Frederick Forsyth", years="1896–1984; born 1938",
    body="**Liam O'Flaherty** was an Irish writer known for stories about animals and nature on the Aran Islands, where seagulls nest on high cliffs.\n\n"
         "**Frederick Forsyth** is a British novelist, once a pilot in the Royal Air Force, famous for thrillers such as The Day of the Jackal. The Black Aeroplane is a short mystery told in the first person.",
    future="Pilots, mountaineers and athletes all face 'first flights'. Learning to act in spite of fear is a life skill."),
  C.socratic("s1.socratic", "The young seagull flies only when he is very hungry. What does this suggest?",
    ["Sometimes a strong need pushes us past our fear", "Hunger makes birds lazy", "He never wanted to fly at all"], 0,
    "Hunger was stronger than fear, so he dived at the fish and found his wings."),
 ]},
 {"id": "s2", "title": "His First Flight", "blocks": [
  blk("s2.thm", "theory", title="What happens in the story", revision=True,
    body="**Alone on the ledge.** The young seagull is alone on his ledge. The day before, his **two brothers and his sister**, whose wings were far shorter than his own, had run to the brink, flapped their wings and flown away. He had tried, but the great expanse of sea below frightened him; he felt his wings would never support him, so he ran back to the little hole under the ledge.\n\n"
         "**Taunted and scolded.** His father and mother came round calling to him, **scolding** him and **threatening** to let him starve on the ledge unless he flew. Now his family is on the plateau opposite: brothers and sister lying down, his father preening his feathers, his mother looking at him. He has had nothing to eat since the previous nightfall and is **hungry**.\n\n"
         "**The trick with the fish.** His mother picks up a piece of fish and flies across towards him. She halts just opposite him, legs hanging limp, wings still, the fish almost within reach. Then, **maddened by hunger**, he dives at the fish with a scream.\n\n"
         "**Flying!** He falls, and a monstrous terror seizes him, but only for a minute. His wings spread outwards; the wind rushes against his breast; he is **flying**. His mother swoops past him, his father flies over him screaming, and his brothers and sister fly around him. He is no longer afraid.\n\n"
         "**The sea.** He lands on the **green sea**. His legs sink into it; he is frightened at first, but then his belly touches the water and he floats. His family lands around him, praising him and offering him scraps of dog-fish. **He had made his first flight.**"),
  C.kc("s2.check", "Why was the young seagull afraid to fly?",
    [("he thought his wings would not support him over the vast sea", ""), ("his wings were shorter than his brothers'", "His wings were longer than theirs."),
     ("he was injured", "He was only afraid."), ("his parents did not want him to fly", "They wanted him to fly.")],
    "Fear, not weakness, kept him on the ledge.")
  ,C.kc("s2.check2", "What finally made the young seagull fly?",
    [("hunger: he dived at the fish his mother held out", ""), ("his father pushed him", "No one pushed him."),
     ("a strong wind blew him off", "He dived for the food."), ("his brothers taught him", "Hunger drove him.")],
    "'The sight of the food maddened him.'")
 ]},
 {"id": "s3", "title": "The Black Aeroplane", "blocks": [
  blk("s3.thm", "theory", title="What happens in the story", revision=True,
    body="**Going home.** The narrator, a pilot, is flying his old **Dakota** aeroplane over France back to England, at about **1.30 in the morning**, dreaming of his holiday and an **English breakfast**. He calls **Paris Control**, which tells him to turn twelve degrees west.\n\n"
         "**'I'll take the risk.'** Ahead he sees huge **black storm clouds**. He could fly back to Paris, but he wants to get home, so he decides to take the risk and flies into the storm.\n\n"
         "**Lost in the storm.** Inside the clouds everything is black. The **compass** turns round and round and is dead; the **radio** is dead too. He can see nothing and cannot contact anyone. He is lost, with very little fuel left.\n\n"
         "**The black aeroplane.** Suddenly he sees another aeroplane with **no lights** on its wings, flying next to him. Its pilot waves, as if to say 'Follow me'. The narrator follows him through the storm with enough fuel for only a few minutes. Then the clouds clear, and he sees two lines of **runway lights**. He lands safely, and the black aeroplane is gone.\n\n"
         "**The mystery.** In the control centre he asks a woman who the other pilot was. She looks at him strangely: **'Black aeroplane? There are no other aeroplanes flying tonight. Yours was the only one I could see on the radar.'** So who helped him reach the airport without a compass, a radio or fuel? The story ends with this question."),
  blk("s3.table", "markdown_table", title="The two stories side by side", revision=True, body=COMPARE),
  C.kc("s3.check", "What was 'the risk' the narrator decided to take?",
    [("flying into the storm instead of returning to Paris", ""), ("flying without a licence", "He was a qualified pilot."),
     ("landing on the sea", "He landed on a runway."), ("flying a new aeroplane", "His Dakota was old.")],
    "He wanted to get home for breakfast.")
  ,C.kc("s3.check2", "Why did the woman in the control centre look at the narrator strangely?",
    [("no other aeroplane was flying that night; only his was on the radar", ""), ("he had landed at the wrong airport", "He landed safely."),
     ("he was very late", "She was puzzled by his question."), ("he was not a pilot", "He was the pilot of the Dakota.")],
    "His question about a black aeroplane made no sense to her.")
 ]},
 {"id": "s4", "title": "Language of the stories", "blocks": [
  blk("s4.thm", "theory", title="Words and expressions to know", revision=True,
    body="| Word or phrase | Meaning |\n|---|---|\n| **ledge** | a narrow shelf of rock on a cliff |\n| **brink** | the edge of a steep place |\n"
         "| **preening** | cleaning and arranging feathers with the beak |\n| **taunting** | mocking, teasing to provoke |\n| **cajole** | to persuade by coaxing |\n"
         "| **maddened by hunger** | driven wild by hunger |\n| **swoop** | to fly down quickly |\n| **plateau** | a flat, raised area of land |\n"
         "| **Dakota** | a type of old propeller aeroplane |\n| **Paris Control** | the air-traffic control centre in Paris |\n| **fuel gauge** | the instrument that shows how much fuel is left |\n\n"
         "**Style:** His First Flight is told in the **third person** and shows the bird's feelings closely. The Black Aeroplane is told in the **first person** in short, tense sentences, which build suspense and end in a **mystery**."),
  C.kc("s4.check", "'Preening' means:",
    [("cleaning feathers with the beak", ""), ("flying fast", "That is swooping."), ("screaming", "That is calling."), ("sleeping", "That is dozing.")],
    "The father was preening the feathers on his white back.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Seagull: Fear → Hunger → Fish → Fall → Fly → Float.**\n- **Pilot: Breakfast → Storm → Dead compass and radio → Black plane → Runway → 'No other plane'.**\n"
         "- **Brothers and sister: two brothers, one sister; wings shorter than his.**\n- **Time and plane: 1.30 a.m., old Dakota, Paris Control.**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying the seagull's wings were too short: his wings were **longer** than his siblings'; he lacked confidence.\n"
         "2. Saying his father pushed him: **hunger** made him dive at the fish.\n3. Saying the pilot crashed or landed on the sea: he landed safely on a runway.\n"
         "4. Explaining the black aeroplane as a fact: the story leaves it a **mystery**; give your view but call it a possibility."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Ask: 'Who flew the black aeroplane?' Let groups argue for four answers (a ghost pilot, a guardian angel, the pilot's imagination, a real plane missed by radar), each using details from the story."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Think of something you were afraid to try for the first time (swimming, cycling, speaking on stage). What or who helped you do it?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **A Letter to God (Ch 1):** help also comes from an unseen source.\n- **The Ball Poem:** learning to face loss on one's own.\n- **Physics:** how wings give lift; why pilots depend on the compass and radio."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="Compare the young seagull and the narrator of The Black Aeroplane. Answer in about 120 words.\n\n"
         "**Model answer:** Both face fear while flying, but in opposite ways. The young seagull is afraid of his very first flight: the vast sea below makes him think his wings will not hold him, and he stays on the ledge while his family taunts him. Only hunger, when his mother holds out a piece of fish, makes him dive and discover he can fly. The pilot, on the other hand, is experienced and confident, even too confident: he takes the risk of flying into a storm to reach home for breakfast. When his compass and radio fail, he is lost, and only a mysterious black aeroplane guides him to safety. One story shows that we grow by facing fear; the other that help can come from where we least expect it."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- His First Flight: a young seagull, afraid to fly, is left alone on a ledge; hungry, he dives at a fish held by his mother, falls, and finds he can fly. He lands on the sea and his family praises him.\n"
         "- The Black Aeroplane: a pilot flying a Dakota home to England at night flies into a storm; his compass and radio die. A black aeroplane with no lights guides him to a runway. Control says no other plane was flying.\n"
         "- Themes: fear and courage, family support, risk, and the mystery of unseen help."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- Name the story you are writing about in every answer; the chapter has two.\n- For 'Who helped the narrator?', give your opinion and support it with two details (no lights, waved, vanished, not on radar).\n"
         "- In long answers on the seagull, use the stages: fear, taunts, hunger, the dive, flight, landing on the sea."),
  blk("s5.flash1", "flashcard", front="Why could the young seagull not fly at first?", back="He was afraid; the vast sea below made him think his wings would not support him."),
  blk("s5.flash2", "flashcard", front="How did his mother get him to fly?", back="She flew towards him with a piece of fish and stopped just out of reach; maddened by hunger, he dived at it."),
  blk("s5.flash3", "flashcard", front="What failed in the pilot's aeroplane during the storm?", back="The compass and the radio; and his fuel was almost finished."),
  blk("s5.flash4", "flashcard", front="What did the woman at control say about the black aeroplane?", back="'There are no other aeroplanes flying tonight. Yours was the only one I could see on the radar.'"),
 ]},
]

# ---------------- NCERT: Thinking about the Text ----------------
C.sa("ex1", GULL, "Why was the young seagull afraid to fly? Do you think all young birds are afraid to make their first flight, or are some birds more timid than others?",
     ["He feared his wings would not support him over the great expanse of sea below.", "Some young birds are more timid than others; this one lacked confidence, while his brothers and sister flew easily."], EX1(1))
C.sa("ex2", GULL, "'The sight of the food maddened him.' What does this suggest? What compelled the young seagull to finally fly?",
     ["He was extremely hungry, having eaten nothing since the previous nightfall.", "Hunger made him forget his fear; he dived at the fish his mother held out and found himself flying."], EX1(2))
C.sa("ex3", FAMILY, "'They were beckoning to him, calling shrilly.' Why did the seagull's father and mother threaten him and cajole him to fly?",
     ["They knew he had to learn to fly to survive and find his own food.", "Scolding and tempting him were ways to push him past his fear."], EX1(3))
C.sa("ex4", FAMILY, "Have you ever had a similar experience, where your parents encouraged you to do something that you were too scared to do? Discuss this in pairs or in groups.",
     ["Yes, for example learning to swim or ride a cycle.", "My parents encouraged me, held me at first and then let go; once I tried, I found I could do it."], EX1(4))
C.sa("ex5", GULL, "In the case of a bird flying, it seems a natural action. Why does a human need special help?",
     ["For a bird, flying is instinctive, though it still needs courage the first time.", "Humans have no wings; they need machines and long training to fly, and help when instruments fail."], EX1(5))
C.sa("ex6", PILOT, "'I'll take the risk.' What is the risk? Why does the narrator take it?",
     ["The risk is to fly through the dangerous storm clouds instead of going back to Paris.", "He takes it because he wants to get home to England and have his English breakfast with his family."], EX2(1))
C.sa("ex7", PILOT, "Describe the narrator's experience as he flew the aeroplane into the storm.",
     ["Inside the clouds everything was black and he could see nothing outside.", "The compass turned round and round, the radio went dead, and he was lost with little fuel left."], EX2(2))
C.sa("ex8", MYST, "Why does the woman in the control centre look at the narrator strangely?",
     ["He asked her about the pilot of a black aeroplane.", "She said there were no other planes flying that night; only his was on the radar."], EX2(3))
C.sa("ex9", MYST, "Who do you think helped the narrator to reach safely? Discuss this among yourselves and give reasons for your answer.",
     ["It may have been a ghost pilot or a guardian angel, since the plane had no lights, was not on radar and vanished.", "Or it may have been his own instinct under stress; the story leaves it a mystery."], EX2(4))

# ---------------- Extracts ----------------
C.extract("ext1", GULL,
  "The day before, all his family had been on the ledge with him.\nHis two brothers and his sister, whose wings were far shorter than his own, had run to the brink, flapped their wings, and flown away.\nBut he became afraid to fly.",
  [("Who is 'he' in the extract?", "The young seagull."),
   ("How many brothers and sisters did he have?", "Two brothers and one sister."),
   ("How were their wings different from his?", "Their wings were shorter than his."),
   ("Find a word that means 'edge'.", "Brink."),
   ("What does this show about his problem?", "It was fear, not weak wings, that stopped him.")])
C.extract("ext2", GULL + FAMILY,
  "She was tearing at a piece of fish that lay at her feet.\nHe screamed and the mother looked across at him.\nThen she picked up a piece of the fish and flew across to him with it.",
  [("Who is 'she'?", "The young seagull's mother."),
   ("Why did he scream?", "He was very hungry and begged for food."),
   ("What did his mother do next?", "She flew towards him with a piece of fish."),
   ("Why did she stop just out of his reach?", "To tempt him to fly to get it."),
   ("What quality of the mother does this show?", "Wisdom and care: she encouraged him to fly.")])
C.extract("ext3", PILOT,
  "I knew that I had to take a risk. I didn't stop to think. I turned the old Dakota into the storm clouds.\nSuddenly, everything was black.\nIt was impossible to see anything outside the aeroplane.",
  [("Who is the speaker?", "The pilot, the narrator of The Black Aeroplane."),
   ("Name the aeroplane he was flying.", "An old Dakota."),
   ("What risk did he take?", "He flew into the storm clouds."),
   ("Why did he not go back to Paris?", "He wanted to get home to England for breakfast."),
   ("What happened inside the clouds?", "Everything turned black; he could see nothing.")])
C.extract("ext4", MYST,
  "'Black aeroplane? There are no other aeroplanes flying tonight.\nYours was the only one I could see on the radar.'",
  [("Who says these words?", "The woman in the control centre."),
   ("To whom are they said?", "To the narrator, the pilot."),
   ("What had the narrator asked her?", "Who the pilot of the black aeroplane was."),
   ("What does 'radar' do?", "It shows the position of aeroplanes in the sky."),
   ("What do her words make the story?", "A mystery.")])

# ---------------- Objective practice ----------------
C.m("mcq01", GULL, "Where was the young seagull standing?",
    [("on a ledge of a cliff", ""), ("on the sea", "He landed there at the end."), ("on a tree", "Seagulls nest on cliffs."), ("on a ship", "He was on the cliff.")],
    "He was alone on his ledge.")
C.m("mcq02", FAMILY, "What did his parents threaten to do?",
    [("let him starve on the ledge unless he flew", ""), ("push him into the sea", "They threatened starvation."), ("leave the island", "They stayed nearby."), ("beat him", "They scolded and threatened starvation.")],
    "They scolded and threatened him to make him fly.")
C.m("mcq03", FAMILY, "What was his father doing on the plateau?",
    [("preening his feathers", ""), ("sleeping", "His brothers and sister were dozing."), ("catching fish", "He was preening."), ("calling the mother", "He was preening.")],
    "Preening means cleaning feathers.")
C.m("mcq04", GULL, "Since when had the seagull not eaten?",
    [("the previous nightfall", ""), ("a week", "Only since the previous nightfall."), ("that morning", "Since the night before."), ("three days", "Since the previous nightfall.")],
    "He was very hungry.")
C.m("mcq05", GULL, "What happened when the seagull dived at the fish?",
    [("he fell, then his wings spread and he flew", ""), ("he caught the fish and went back", "He fell outwards and flew."), ("he drowned", "He flew and then floated."), ("his mother caught him", "He flew on his own.")],
    "Terror lasted only a minute.")
C.m("mcq06", GULL, "Where did the young seagull land after his first flight?",
    [("on the green sea", ""), ("back on the ledge", "He landed on the sea."), ("on the plateau", "He landed on the sea."), ("on a rock", "He landed on the sea.")],
    "At first he was frightened, then he floated.")
C.m("mcq07", FAMILY, "What did his family offer him after he landed?",
    [("scraps of dog-fish", ""), ("a herring", "They offered dog-fish."), ("bread", "They offered fish."), ("nothing", "They praised him and offered food.")],
    "They praised him.")
C.m("mcq08", LANG, "'He dived at the fish' shows that he acted:",
    [("on impulse, driven by hunger", ""), ("after careful thought", "Hunger made him act suddenly."), ("because he was ordered", "It was his own act."), ("out of anger", "It was hunger.")],
    "Hunger was stronger than fear.")
C.m("mcq09", PILOT, "What was the narrator flying?",
    [("an old Dakota aeroplane", ""), ("a jet fighter", "It was an old Dakota."), ("a helicopter", "It was a Dakota."), ("a glider", "It had engines and fuel.")],
    "He was flying from Paris to England.")
C.m("mcq10", PILOT, "What was the narrator looking forward to?",
    [("a big English breakfast at home", ""), ("a flight to Paris", "He was leaving Paris."), ("a holiday in France", "He was going home."), ("meeting the black pilot", "He did not know of him.")],
    "He thought of his family and breakfast.")
C.m("mcq11", PILOT, "Which instruments stopped working in the storm?",
    [("the compass and the radio", ""), ("the engines", "The engines kept running."), ("the lights only", "The compass and radio failed."), ("the wheels", "The compass and radio failed.")],
    "He could not find his way or call for help.")
C.m("mcq12", MYST, "What was strange about the black aeroplane?",
    [("it had no lights on its wings", ""), ("it was very large", "The point is that it had no lights."), ("it flew upside down", "It flew normally."), ("it was red", "It was black.")],
    "Its pilot waved to him to follow.")
C.m("mcq13", MYST, "How did the narrator know he was safe?",
    [("he saw two lines of runway lights", ""), ("the radio started working", "He saw the runway."), ("the fuel tank filled up", "He had little fuel."), ("the sun came out", "It was night.")],
    "He landed safely.")
C.m("mcq14", MYST, "The ending of The Black Aeroplane leaves the reader with:",
    [("a mystery", ""), ("a moral", "It ends with an unanswered question."), ("a tragedy", "He lands safely."), ("a joke", "It is serious.")],
    "Who helped him remains unknown.")
C.m("mcq15", PILOT, "At what time does the story of the pilot begin?",
    [("about one-thirty in the morning", ""), ("noon", "It was night."), ("evening", "It was 1.30 a.m."), ("dawn", "It was the middle of the night.")],
    "He was flying home at night.")
C.m("mcq16", PILOT, "Whom did the narrator call before the storm?",
    [("Paris Control", ""), ("London Control", "He called Paris."), ("his wife", "He used the radio to call Paris Control."), ("the black aeroplane", "He saw it later.")],
    "They told him to turn twelve degrees west.")
C.m("mcq17", LANG, "Which story is told in the first person?",
    [("The Black Aeroplane", ""), ("His First Flight", "It uses 'he'."), ("both", "Only The Black Aeroplane uses 'I'."), ("neither", "The Black Aeroplane uses 'I'.")],
    "The pilot tells his own story.")
C.m("mcq18", FAMILY, "The parents' behaviour towards the young seagull shows:",
    [("tough love, to make him independent", ""), ("cruelty without reason", "They wanted him to learn."), ("that they did not care", "They watched and helped."), ("favouritism", "They wanted all their young to fly.")],
    "They scolded and tempted him for his own good.")
C.tf("tf1", GULL, "The young seagull's wings were shorter than his siblings'.", False, "His siblings' wings were far shorter than his own.")
C.tf("tf2", GULL, "The young seagull was frightened when his feet sank into the sea.", True, "He was afraid at first, then he floated.")
C.tf("tf3", PILOT, "The narrator went back to Paris when he saw the storm.", False, "He took the risk and flew into the storm.")
C.tf("tf4", MYST, "The black aeroplane appeared on the control centre's radar.", False, "Only the narrator's plane was on the radar.")

# ---------------- More written practice ----------------
C.sa("sa1", GULL, "Describe the young seagull's feelings as he made his first flight.",
     ["He felt monstrous terror as he fell, but only for a minute.", "Then his wings spread, he felt the wind and the joy of flying, and his fear left him."])
C.sa("sa2", PILOT, "Why did the narrator feel that he would not reach England?",
     ["His compass and radio were dead and he could see nothing in the storm.", "He had very little fuel left and did not know where he was."])
C.sa("sa3", MYST, "Describe the role of the black aeroplane in the story.",
     ["It appeared beside the lost Dakota and its pilot waved to follow him.", "It guided the narrator through the storm to a runway and then disappeared."])
C.la("la1", GULL + FAMILY, "How did the young seagull's family help him overcome his fear? Do you think their method was right?",
     ["His brothers and sister flew first and set an example.", "His parents scolded and threatened to let him starve, so that he would not depend on them.",
      "His mother tempted him with a piece of fish held just out of reach; hunger made him dive.", "Once he flew, the family flew around him and praised him, building his confidence.",
      "Their method was tough but right: fear is overcome by doing, and they stayed near him all the time."])
C.la("la2", MYST, "Who do you think flew the black aeroplane? Give reasons for your answer.",
     ["The plane had no lights, was not seen on the radar, and vanished after the landing.", "Its pilot seemed to know the way through the storm and waved to guide the narrator.",
      "These details suggest a supernatural helper, perhaps a ghost pilot or a guardian angel.", "Another view is that, under great stress, the narrator imagined the plane while his instinct guided him.",
      "The writer leaves the question open, which makes the story a mystery."])
C.la("la3", PILOT, "Was the narrator of The Black Aeroplane wise to take the risk? Explain.",
     ["He was experienced and wanted to reach home for breakfast, so he flew into the storm.", "But the decision was unwise: storms can disable instruments and he had little fuel.",
      "He survived only because of the mysterious aeroplane.", "A good pilot should value safety over comfort; he could have returned to Paris."])

chapter = header("ch03", 3, "Two Stories about Flying", "Liam O'Flaherty; Frederick Forsyth", "prose",
                 ["seagull_first_flight", "family_and_encouragement", "pilot_in_the_storm", "mystery_of_the_black_aeroplane", "vocabulary_and_style"],
                 "CBSE 2025-26 English Language and Literature (184): First Flight prose, Chapter 3 (His First Flight; The Black Aeroplane). Assessed through extracts (5 marks), short answers in 40-50 words (3 marks) and long answers in 100-120 words (6 marks).")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
