"""CBSE Class 10 English, Footprints without Feet Ch 3: The Midnight Visitor (Robert Arthur)."""
import sys
from lit_common import make, header, path, ex

ROOT = sys.argv[1]
PATH = path("ch03_the_midnight_visitor", "footprints")
C = make("fwf10ch03")
blk = C.blk
SPY, MAX, TRICK, CHARS = ["ausable_the_secret_agent"], ["max_and_the_report"], ["the_balcony_trick"], ["characters"]
RF = lambda n: ex(n, "Read and Find Out")
TA = lambda n: ex(n, "Think about It")

TRICKS = ("| Ausable's invention | Why Max believes it | The truth |\n|---|---|---|\n"
          "| a **balcony** under the window, used by an intruder before | Ausable says it calmly and complains about it | there is **no balcony** |\n"
          "| the **police** are coming, because he asked them to check on him | there is a knock at the door at that very moment | the knock is **Henry, the waiter**, with the drinks Ausable had ordered |")

sections = [
 {"id": "s1", "title": "Not what a spy should look like", "blocks": [
  blk("s1.hook", "hook", title="A fat, wheezing secret agent?",
    body="Fowler, a young writer, expects a secret agent to be tall, handsome and mysterious, with dark-eyed beauties and secret notes. Instead he meets **Ausable**: fat, wheezing, living in a small room at the top of a shabby hotel.\n\n"
         "But when a rival spy points a pistol at them in the middle of the night, Ausable shows that a sharp mind is a better weapon than good looks."),
  blk("s1.inspiration", "inspiration", title="The writer", person="Robert Arthur", years="1909–1969",
    body="**Robert Arthur** was an American writer of mystery and suspense stories for magazines, radio and television, and of the 'Three Investigators' books for young readers. His stories often end with a clever twist.",
    future="Detectives, negotiators and crisis managers rely on the calm, quick thinking that Ausable shows."),
  C.socratic("s1.socratic", "Ausable had no weapon, yet he defeated an armed man. What was his weapon?",
    ["His presence of mind and quick, convincing lies", "A hidden pistol", "The police, who were waiting outside"], 0,
    "Brains, not muscles."),
 ]},
 {"id": "s2", "title": "The story", "blocks": [
  blk("s2.thm", "theory", title="What happens", revision=True,
    body="**Fowler's disappointment:** **Fowler**, a young writer, has come to meet **Ausable**, a secret agent, hoping for romance and adventure. Ausable is **fat**, speaks with an accent, and lives in a **small room on the sixth (top) floor** of an old French hotel. There are no beautiful women, no secret messages, no gunfire. Ausable says that his work is mostly dull, but that tonight he expects an important **paper** about **new missiles**.\n\n"
         "**The visitor:** when they enter the room and switch on the light, they find **Max**, a rival agent, with a **pistol**. Max has come for the same report. Fowler is thrilled at last.\n\n"
         "**The balcony:** Ausable stays calm. He complains, as if annoyed, that this is the second time someone has got into his room through **the balcony** under the window, which belongs to the next room. Max listens.\n\n"
         "**The knock:** then comes a knock at the door. Ausable tells Max it must be **the police**: he had asked them to check on him, as he was carrying an important paper. Max, afraid of being caught, decides to hide on 'the balcony'. He climbs out of the window and drops, and there is a **scream**: there is **no balcony**.\n\n"
         "**The twist:** Ausable opens the door. It is **Henry, the waiter**, with the drinks Ausable had ordered earlier. Fowler asks, 'But the balcony?' and Ausable replies, 'No, there is no balcony.' The police, too, were Ausable's invention."),
  blk("s2.table", "markdown_table", title="Ausable's two inventions", revision=True, body=TRICKS),
  C.kc("s2.check", "What had Max come for?",
    [("a paper about new missiles", ""), ("money", "A report about missiles."), ("to kill Fowler", "He wanted the paper."), ("to rent the room", "He wanted the paper.")],
    "Ausable expected to receive it that night.")
  ,C.kc("s2.check2", "Who was really knocking at the door?",
    [("Henry, the waiter, with drinks", ""), ("the police", "Ausable invented the police."), ("another spy", "It was the waiter."), ("Fowler's friend", "It was the waiter.")],
    "Ausable had ordered the drinks earlier.")
 ]},
 {"id": "s3", "title": "Characters and twist", "blocks": [
  blk("s3.thm", "theory", title="How Ausable wins", revision=True,
    body="**Ausable:** fat and ordinary-looking, but **calm, clever and resourceful**, with great **presence of mind**. He never panics; he invents two believable stories on the spot and lets Max defeat himself. His appearance hides his sharp mind.\n\n"
         "**Max:** a rival agent, **armed but gullible** and nervous. He believes the stories because they come with convincing detail (a complaint to the management, an actual knock).\n\n"
         "**Fowler:** a young writer with **romantic, bookish ideas** about spies; he learns that real spying is different.\n\n"
         "**Twist ending:** the 'police' were a waiter and the 'balcony' never existed. The surprise ending is typical of a **suspense story**.\n\n"
         "**Theme:** **intelligence and presence of mind** are stronger than weapons; appearances can be misleading."),
  C.kc("s3.check", "Which quality helped Ausable most?",
    [("presence of mind", ""), ("physical strength", "He was fat and unfit."), ("a hidden gun", "He had no weapon."), ("good looks", "He was not glamorous.")],
    "He thought fast and stayed calm.")
  ,C.kc("s3.check2", "Why did Max believe Ausable's story?",
    [("Ausable told it calmly with convincing detail, and a knock came at the right moment", ""), ("Max had seen the balcony before", "There was no balcony."),
     ("Fowler confirmed it", "Fowler said nothing."), ("Max trusted Ausable as a friend", "They were rivals.")],
    "Timing and confidence made the lie work.")
 ]},
 {"id": "s4", "title": "Language of the story", "blocks": [
  blk("s4.thm", "theory", title="Words and expressions to know", revision=True,
    body="| Word or phrase | Meaning |\n|---|---|\n| **secret agent** | a spy who gathers information secretly |\n| **romantic figure** | a glamorous, exciting person, as in films |\n"
         "| **presence of mind** | the ability to think and act calmly in danger |\n| **missiles** | rockets that carry weapons |\n| **gullible** | easily fooled |\n| **wheeze** | breathe noisily |\n\n"
         "**Style:** third-person narration, short dialogue, building suspense and a twist at the end."),
  C.kc("s4.check", "'Presence of mind' means:",
    [("the ability to think quickly and calmly in a difficult situation", ""), ("being present in a room", "It means calm, quick thinking."), ("a good memory", "Calm, quick thinking."), ("being polite", "Calm, quick thinking.")],
    "Ausable shows it throughout.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Characters: Ausable (fat agent), Fowler (young writer), Max (rival with pistol), Henry (waiter).**\n- **Room: sixth floor, small. Paper: new missiles.**\n"
         "- **Two lies: balcony + police. Truth: no balcony + waiter with drinks.**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying the police arrived: it was **Henry, the waiter**.\n2. Saying there was a balcony: there was **none**.\n"
         "3. Saying Ausable fought Max: he used only **words and wit**.\n4. Mixing up Fowler and Max: Fowler is the **writer**, Max the **rival spy**."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Act out the scene in the room with three students. Stop at the knock and ask the class: what would you say if you were Ausable?"),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Have you ever solved a problem by staying calm while others panicked? What happened?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **A Question of Trust:** another thief outwitted by a clever lie.\n- **The Thief's Story:** a surprise ending of a different kind."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="'Ausable is not a typical secret agent, yet he is very good at his job.' Discuss in about 120 words.\n\n"
         "**Model answer:** Ausable does not look like the glamorous spy of films. He is fat, speaks with an accent and lives in a small room on the sixth floor of a shabby hotel, which disappoints the young writer Fowler. Yet when the rival agent Max surprises them with a pistol, Ausable stays perfectly calm. He invents a balcony under the window, complaining that intruders have used it before, and when a knock comes he says it is the police he had asked to check on him. Max panics, climbs out to hide on the 'balcony' and falls, because there is none. The knock was only the waiter. Ausable wins without a weapon, using presence of mind and quick thinking."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Fowler, a writer, is disappointed that the secret agent Ausable is fat and ordinary.\n- In Ausable's room, the rival agent Max waits with a pistol for a report on new missiles.\n"
         "- Ausable invents a balcony and says the police are coming; a knock seems to confirm it.\n- Max jumps out of the window to hide and falls: there is no balcony.\n"
         "- The knock was the waiter with drinks. Theme: presence of mind beats force."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- In character questions about Ausable, contrast his appearance with his intelligence.\n- Always explain both lies (balcony and police) and the twist.\n"
         "- Use the phrase 'presence of mind' with examples."),
  blk("s5.flash1", "flashcard", front="Why was Fowler disappointed?", back="Ausable was fat and ordinary, not a glamorous, romantic secret agent."),
  blk("s5.flash2", "flashcard", front="What two lies did Ausable tell?", back="That there was a balcony below the window, and that the police were coming."),
  blk("s5.flash3", "flashcard", front="Who knocked at the door?", back="Henry, the waiter, bringing the drinks Ausable had ordered."),
  blk("s5.flash4", "flashcard", front="What happened to Max?", back="He climbed out of the window to hide on the balcony and fell, because there was no balcony."),
 ]},
]

# ---------------- NCERT: Read and Find Out ----------------
C.vsa("rf1", SPY, "How is Ausable different from other secret agents?", ["He is fat and does not look glamorous or romantic.", "He lives in a small room on the top floor of an ordinary hotel and his work seems dull."], RF(1))
C.vsa("rf2", SPY, "Who is Fowler and what are his expectations about Ausable?", ["Fowler is a young writer.", "He expects a romantic, mysterious spy with beautiful women, secret notes and gunfire."], RF(2))
C.vsa("rf3", MAX, "Who is Max? Who does he say he is?", ["Max is another secret agent, a rival of Ausable.", "He has come with a pistol to take the report on new missiles."], RF(3))
C.sa("rf4", TRICK, "How does Ausable say Max must have got into the room?", ["Ausable says Max came in through the balcony under the window.", "He claims the balcony belongs to the next room and that intruders have used it before."], RF(4))
C.sa("rf5", TRICK, "Who is at the door? Why is Max frightened? What does he do?", ["It is Henry, the waiter, with drinks, but Ausable says it is the police.", "Max fears arrest, so he jumps out of the window to hide on the balcony and falls."], RF(5))

# ---------------- NCERT: Think about It ----------------
C.sa("ta1", SPY, "How is Ausable different from the popular image of a secret agent? What things does he say that show his presence of mind and ability to think quickly?",
     ["He is fat, unglamorous and lives in a shabby room, unlike the romantic spy of films.", "He invents the balcony and says the police are coming when there is a knock, showing quick thinking and calm."], TA(1))
C.la("ta2", TRICK, "Ausable stays calm when he sees Max with a pistol. How does he use words, not weapons, to defeat Max?",
     ["Ausable does not panic or argue; he talks calmly and even complains.", "He tells Max that intruders have entered through a balcony under the window, planting the idea of the balcony.",
      "When a knock comes, he claims it is the police he had asked to check on him.", "Max, afraid of arrest, climbs out to hide on the balcony and falls, because there is no balcony.",
      "So Ausable wins with presence of mind and clever lies, without firing a shot."], TA(2))
C.sa("ta3", CHARS, "Is Max a gullible person? Give reasons for your answer.",
     ["Yes, Max believes Ausable's stories without checking them.", "He trusts the story of the balcony and the police so quickly that he jumps from the window."])

# ---------------- Objective practice ----------------
C.m("mcq01", SPY, "Ausable was:", [("a fat secret agent", ""), ("a young writer", "That is Fowler."), ("a waiter", "That is Henry."), ("a police officer", "A secret agent.")], "He did not look like a spy.")
C.m("mcq02", SPY, "Fowler was:", [("a young writer", ""), ("a rival spy", "That is Max."), ("a waiter", "That is Henry."), ("a policeman", "A writer.")], "He expected a romantic adventure.")
C.m("mcq03", SPY, "Ausable's room was on the:", [("sixth floor", ""), ("ground floor", "The sixth (top) floor."), ("second floor", "The sixth floor."), ("basement", "The sixth floor.")], "This matters for the twist.")
C.m("mcq04", MAX, "What did Max have in his hand?", [("a pistol", ""), ("a knife", "A pistol."), ("the report", "He wanted the report."), ("a tray", "Henry had a tray.")], "He threatened them.")
C.m("mcq05", MAX, "The paper Max wanted was about:", [("new missiles", ""), ("a bank robbery", "Missiles."), ("Fowler's book", "Missiles."), ("the hotel", "Missiles.")], "A secret military report.")
C.m("mcq06", TRICK, "Ausable said the intruder came in through:", [("the balcony under the window", ""), ("the main door", "Through the 'balcony'."), ("the chimney", "The 'balcony'."), ("a secret tunnel", "The 'balcony'.")], "There was no balcony.")
C.m("mcq07", TRICK, "Whom did Ausable say was knocking?", [("the police", ""), ("the waiter", "That was the truth, not what he said."), ("Fowler's friend", "The police."), ("the manager", "The police.")], "He said he had asked them to check on him.")
C.m("mcq08", TRICK, "What happened to Max in the end?", [("he jumped out of the window and fell", ""), ("he was arrested", "No police came."), ("he shot Ausable", "No shot was fired."), ("he ran down the stairs", "He went out of the window.")], "He expected a balcony.")
C.m("mcq09", CHARS, "Ausable's main quality is:", [("presence of mind", ""), ("cruelty", "He used wit."), ("laziness", "He acted quickly."), ("strength", "He was fat and unfit.")], "He stayed calm under a gun.")
C.m("mcq10", CHARS, "Max can be described as:", [("gullible and nervous", ""), ("very clever", "He was fooled."), ("brave and calm", "He panicked."), ("honest", "He was a rival spy.")], "He believed every word.")
C.m("mcq11", SPY, "Fowler was disappointed because:", [("Ausable did not look like a romantic spy", ""), ("Ausable was rude", "He was unglamorous."), ("the hotel was far away", "Ausable was unglamorous."), ("Max was late", "Ausable was unglamorous.")], "No beautiful women, no gunfire.")
C.m("mcq12", TRICK, "The story ends with:", [("a twist: no police and no balcony", ""), ("a gunfight", "A twist."), ("Max getting the report", "He failed."), ("Ausable's arrest", "A twist.")], "Typical of suspense stories.")
C.m("mcq13", TRICK, "Henry, the waiter, brought:", [("drinks Ausable had ordered", ""), ("the police", "Drinks."), ("the report", "Drinks."), ("a letter", "Drinks.")], "His knock frightened Max.")
C.m("mcq14", CHARS, "The theme of the story is that:", [("intelligence beats force", ""), ("spies are always handsome", "Appearances mislead."), ("guns solve problems", "Wit wins."), ("hotels are dangerous", "Wit wins.")], "Ausable wins without a weapon.")
C.m("mcq15", SPY, "'Romantic figure' here means:", [("a glamorous, exciting person", ""), ("a person in love", "Glamorous and exciting."), ("a poet", "Glamorous and exciting."), ("an old man", "Glamorous and exciting.")], "Fowler's idea of a spy.")
C.m("mcq16", TRICK, "Why was the 'balcony' story so dangerous for Max?", [("the room was on the sixth floor, with nothing below the window", ""), ("the balcony was weak", "There was no balcony at all."), ("the police were on the balcony", "There was no balcony."), ("Fowler was hiding there", "There was no balcony.")], "He dropped from a great height.")
C.tf("tf1", TRICK, "There really was a balcony under Ausable's window.", False, "Ausable invented it.")
C.tf("tf2", TRICK, "The police came to Ausable's room.", False, "It was Henry, the waiter.")
C.tf("tf3", SPY, "Ausable was fat and unglamorous.", True, "This disappointed Fowler.")
C.tf("tf4", MAX, "Max wanted a report about new missiles.", True, "Ausable was to receive it that night.")
C.tf("tf5", CHARS, "Ausable panicked when he saw Max's pistol.", False, "He stayed perfectly calm.")
C.tf("tf6", SPY, "Fowler was a young writer.", True, "He hoped to write about romantic spying.")

# ---------------- More short and long answers ----------------
C.vsa("vsa1", TRICK, "What two stories did Ausable invent?", ["A balcony under his window.", "The police coming to check on him."])
C.vsa("vsa2", SPY, "Give two reasons for Fowler's disappointment.", ["Ausable was fat and unglamorous.", "His room and work were dull, with no romance or excitement."])
C.sa("sa1", TRICK, "Why did Ausable mention the balcony before the knock came?",
     ["He planted the idea of an escape route in Max's mind.", "So when the 'police' knocked, Max would try to escape by the balcony, which did not exist."])
C.sa("sa2", MAX, "Describe Max.",
     ["Max was a rival secret agent who came armed with a pistol for the missile report.", "He was nervous and gullible, believing Ausable's lies and jumping from the window."])
C.sa("sa3", SPY, "How did Fowler's view of secret agents change?",
     ["At first he thought spies were glamorous, with beautiful women and gunfire.", "After seeing Ausable defeat Max with wit, he learnt that real spies rely on intelligence."])
C.sa("sa4", TRICK, "Why is the ending of the story surprising?",
     ["We, like Max, believe that the police are at the door and that there is a balcony.", "We discover that it was only the waiter and that there was no balcony at all."])
C.vsa("vsa3", CHARS, "Name the four characters in the story.", ["Ausable, the secret agent, and Fowler, the young writer.", "Max, the rival agent, and Henry, the waiter."])
C.sa("sa5", SPY, "What did Ausable say about the real life of a secret agent?",
     ["He said it was mostly dull, ordinary work, not glamour and adventure.", "That night, however, he expected an important paper about new missiles."])
C.sa("sa6", TRICK, "How did the knock at the door help Ausable?",
     ["It came just after he had mentioned the police and the balcony.", "It made his lie about the police seem true, so Max panicked and fled through the window."])
C.la("la1", CHARS, "Write a character sketch of Ausable.",
     ["Ausable is a secret agent who looks ordinary: fat, wheezing, with an accent.", "He lives simply in a small room on the sixth floor of an old hotel.",
      "But he is intelligent, calm and resourceful, with great presence of mind.", "Faced with Max's pistol, he invents a balcony and the police, and lets Max defeat himself.",
      "He shows that intelligence matters more than looks or weapons in his profession."])
C.la("la2", TRICK, "'Presence of mind can save us in danger.' Explain with reference to The Midnight Visitor.",
     ["When Ausable finds Max waiting with a pistol, he faces real danger.", "Instead of panicking, he calmly invents a balcony that intruders have used before.",
      "When a knock comes, he quickly says it is the police he had asked to check on him.", "Max, frightened, jumps out of the window to hide and falls, as there is no balcony.",
      "Ausable saves himself and the secret report by staying calm and thinking fast."])
C.la("la3", SPY, "Imagine you are Fowler. Write a diary entry about the night you spent with Ausable.",
     ["Date and first person; your disappointment at the fat, ordinary agent and his small room.", "The shock of finding Max with a pistol, waiting for the missile report.",
      "Ausable's calm stories about the balcony and the police, and the knock.", "The twist: Max's fall, the waiter with drinks, and your new respect for Ausable's wit."])

chapter = header("ch03", 22, "The Midnight Visitor", "Robert Arthur", "prose",
                 ["ausable_the_secret_agent", "max_and_the_report", "the_balcony_trick", "characters"],
                 "CBSE 2025-26 English Language and Literature (184): Footprints without Feet, Chapter 3. Assessed through short answers in 40-50 words (3 marks) and a long answer in 100-120 words (6 marks); no extracts from this book.",
                 book="footprints")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
