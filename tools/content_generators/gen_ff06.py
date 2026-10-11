"""CBSE Class 10 English, First Flight Ch 6: Mijbil the Otter (Gavin Maxwell)."""
import sys
from lit_common import make, header, path, ex

ROOT = sys.argv[1]
PATH = path("ch06_mijbil_the_otter")
C = make("ff10ch06")
blk = C.blk
GET, HABITS, JOURNEY, LONDON, LANG = ["getting_mijbil"], ["mijs_habits_and_intelligence"], ["journey_to_london"], ["mij_in_london"], ["vocabulary_and_style"]

TRAITS = ("| What Mij does | What it shows |\n|---|---|\n"
          "| stays aloof at first, then comes to sleep in Maxwell's bed | he slowly learns to trust |\n"
          "| plays wildly in the bathtub, splashing and rolling | otters are water creatures who love to play |\n"
          "| learns to **turn on the tap** by himself | curiosity and intelligence |\n"
          "| invents a game with a rubber ball on a sloping suitcase lid | he can entertain himself and solve problems |\n"
          "| tears the lining of his travel box | he panics in a closed, strange place |\n"
          "| Londoners mistake him for a seal, a squirrel, a walrus and more | otters were unfamiliar to people in England |")

sections = [
 {"id": "s1", "title": "An unusual pet", "blocks": [
  blk("s1.hook", "hook", title="A pet that plays with taps",
    body="Most people keep a dog or a cat. **Gavin Maxwell** decided to keep an **otter**, brought it from the marshes of Iraq, and flew it all the way to London. On the way, the otter escaped inside the aeroplane!\n\n"
         "This true story shows how a wild animal and a man came to trust each other, and how clever and funny an otter can be."),
  blk("s1.inspiration", "inspiration", title="The writer", person="Gavin Maxwell", years="1914–1969",
    body="**Gavin Maxwell** was a Scottish naturalist and writer who lived at **Camusfeàrna** on the west coast of Scotland. In 1956 he travelled to southern **Iraq** and brought back an otter, Mijbil, which belonged to a species unknown to science. It was named **Maxwell's otter** after him.\n\n"
         "His book Ring of Bright Water, from which this story is taken, made otters famous around the world.",
    future="Wildlife biologists, zoologists and vets study animal behaviour the way Maxwell watched Mij."),
  C.socratic("s1.socratic", "Mij was aloof at first but later followed Maxwell everywhere. What changed?",
    ["Mij slowly learnt to trust Maxwell, who was patient and caring", "Mij was punished until he obeyed", "Mij was drugged"], 0,
    "Trust between an animal and a person grows with patience and kindness."),
 ]},
 {"id": "s2", "title": "Getting Mij and his habits", "blocks": [
  blk("s2.thm", "theory", title="From the marshes of Iraq", revision=True,
    body="**The idea:** early in 1956 Maxwell travelled to southern Iraq. By then it had occurred to him that he would like to keep an otter instead of a dog, and that **Camusfeàrna**, his home in Scotland ringed by water, would be a suitable place for the experiment. A friend suggested that he get one from the **Tigris marshes**, where otters were as common as mosquitoes.\n\n"
         "**Mij arrives:** Maxwell went to **Basra**, to the Consulate-General, to collect and answer his mail. There, two Arabs brought him a sack: inside was the otter he named **Mijbil** (Mij). It resembled 'a very small, medieval dragon'. Mij belonged to a race unknown to science; zoologists named it **Maxwell's otter**.\n\n"
         "**Learning to trust:** for the first 24 hours Mij was neither hostile nor friendly, simply **aloof and indifferent**, choosing to sleep on the floor as far from Maxwell's bed as possible. On the second night he came onto the bed and slept in the crook of Maxwell's knees. Soon he followed him everywhere.\n\n"
         "**Water and play:** Mij went wild with joy in the **bathtub**, plunging and rolling and splashing 'like a child'. Within a few days he learnt to **turn on the tap** by himself, though it took him a little longer to turn it fully on. Indoors he played for hours with a rubber ball, and invented a game of rolling it down the sloping lid of a suitcase and catching it at the bottom. Maxwell concludes that otters are like human beings: they need **company and play**."),
  blk("s2.table", "markdown_table", title="What Mij's behaviour tells us", revision=True, body=TRAITS),
  C.kc("s2.check", "How did Mij behave during his first 24 hours with Maxwell?",
    [("aloof and indifferent, sleeping far from Maxwell's bed", ""), ("very friendly and playful", "That came later."),
     ("angry and biting", "He was neither hostile nor friendly."), ("sick and silent", "He was simply aloof.")],
    "On the second night he came to Maxwell's bed.")
  ,C.kc("s2.check2", "Why was the otter named 'Maxwell's otter'?",
    [("it belonged to a species unknown to science, named after Maxwell", ""), ("Maxwell bought it in a shop", "It was a new species."),
     ("all otters are called that", "Only this new species."), ("Mij was Maxwell's surname", "It was named after its discoverer.")],
    "Zoologists named the new race after him.")
 ]},
 {"id": "s3", "title": "The journey and London", "blocks": [
  blk("s3.thm", "theory", title="Basra to London", revision=True,
    body="**No animals allowed:** the airline flying to England would not carry animals, so Maxwell had to book a flight to **Paris** and on to **London**, and he had to keep Mij in a **box** about eighteen inches square, placed at his feet.\n\n"
         "**Panic in the box:** an hour before the flight, Maxwell put Mij in the box and went for a meal. When he returned, there was blood: Mij had torn at the **metal lining** of the box until his mouth and paws were bleeding. Maxwell had to rush to the airport with the otter barely calmed.\n\n"
         "**Chaos on the plane:** on board, Maxwell opened the box to calm Mij, who escaped and ran down the aisle. There was chaos among the passengers; a woman stood on her seat screaming, 'A rat! A rat!' The **air hostess** stayed calm and kind and helped him; Mij was caught at last and returned to Maxwell's knees.\n\n"
         "**Mij in London:** Maxwell took Mij for walks on a lead in London. People could not guess what animal he was: they suggested a baby **seal**, a **squirrel**, a **walrus**, a **hippo**, a **beaver**, a **bear cub**, a **leopard**, and even a brontosaurus. Otters were unfamiliar to Londoners."),
  C.kc("s3.check", "Why did Maxwell have to fly to Paris first?",
    [("the airline flying to England would not carry animals", ""), ("Mij liked Paris", "It was an airline rule."),
     ("he had work in Paris", "The reason was the rule on animals."), ("the tickets were cheaper", "The reason was the rule.")],
    "So he flew via Paris to London.")
  ,C.kc("s3.check2", "What did a woman passenger shout when Mij escaped?",
    [("'A rat! A rat!'", ""), ("'A cat!'", "She thought it was a rat."), ("'A snake!'", "She thought it was a rat."), ("'An otter!'", "She did not know what it was.")],
    "She stood on her seat in fear.")
 ]},
 {"id": "s4", "title": "Language of the story", "blocks": [
  blk("s4.thm", "theory", title="Words and expressions to know", revision=True,
    body="| Word or phrase | Meaning |\n|---|---|\n| **aloof** | distant, not friendly |\n| **indifferent** | not interested |\n"
         "| **marshes** | low, wet land |\n| **crook of the knees** | the bend behind the knees |\n| **pandemonium / chaos** | wild confusion |\n"
         "| **sodden** | completely wet |\n| **aisle** | the passage between seats |\n| **ethnologist / zoologist** | scientists who study peoples / animals |\n\n"
         "**Style:** the story is told in the **first person** with humour; Maxwell compares Mij to a child to show his playful nature."),
  C.kc("s4.check", "'Aloof' means:",
    [("distant and not friendly", ""), ("very playful", "It means distant."), ("hungry", "It means distant."), ("very wet", "That is sodden.")],
    "Mij was aloof at first.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Mij's route: Tigris marshes → Basra → Paris → London → (home: Camusfeàrna, Scotland).**\n"
         "- **Trust timeline: day 1 aloof → night 2 in bed → follows everywhere.**\n- **Clever Mij: tap, ball, suitcase lid.**\n- **London guesses: seal, squirrel, walrus, hippo, beaver, bear cub, leopard.**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying Mij was friendly from the start: he was **aloof** for the first 24 hours.\n2. Saying the airline allowed pets: it did **not**, so Maxwell flew via Paris.\n"
         "3. Calling Mij an ordinary otter: he was of a **species new to science**, Maxwell's otter.\n4. Writing that Maxwell was a zoo-keeper: he was a **writer and naturalist**."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Ask students to retell the plane journey as a news report: 'Otter causes chaos on Paris flight'. They must use five facts in the right order."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Should wild animals be kept as pets? Give one reason for and one against, using Mij's story."),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Geography (Forest and Wildlife Resources):** protecting wild animals in their habitats.\n- **A Tiger in the Zoo (poem):** another view of a wild animal kept by people.\n- **Science (Our Environment):** wetlands like the Tigris marshes support many species."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="'Mij was an intelligent and playful animal.' Prove this with examples from the story in about 120 words.\n\n"
         "**Model answer:** Mij showed intelligence and playfulness in many ways. Though aloof at first, he quickly understood that Maxwell meant him no harm and by the second night slept in the crook of his knees. In the bathroom he went wild with joy, splashing like a child, and within a few days he learnt to turn on the tap by himself. Indoors he could play alone for hours: he shuffled a rubber ball round the room and invented a game of rolling it down the sloping lid of a suitcase and catching it at the bottom. Even his escape on the plane showed how quick and curious he was. Maxwell rightly concludes that otters, like humans, need company and play."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- In 1956 Gavin Maxwell went to southern Iraq and decided to keep an otter at his Scottish home, Camusfeàrna.\n"
         "- At Basra he received Mijbil, of a species new to science, later named Maxwell's otter.\n- Mij was aloof at first but soon became attached, loved water, learnt to turn on the tap and invented games.\n"
         "- Airlines would not carry animals to England, so they flew via Paris; Mij tore his box and escaped on the plane, causing chaos.\n"
         "- In London, people could not guess what animal Mij was."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- For 'intelligence' questions, give two actions (tap, ball game) and explain what each shows.\n- Narrate the journey in order: box, blood, airport, escape, chaos, air hostess, London.\n"
         "- Use words like aloof, indifferent and pandemonium; they score in short answers."),
  blk("s5.flash1", "flashcard", front="Where did Maxwell get Mij?", back="At Basra, in southern Iraq; Mij came from the Tigris marshes."),
  blk("s5.flash2", "flashcard", front="How did Mij behave in the first 24 hours?", back="Aloof and indifferent; he slept on the floor far from Maxwell's bed."),
  blk("s5.flash3", "flashcard", front="What clever thing did Mij learn in the bathroom?", back="To turn on the tap by himself."),
  blk("s5.flash4", "flashcard", front="Why did Maxwell fly via Paris?", back="The airline flying to England did not allow animals."),
 ]},
]

# ---------------- NCERT: Thinking about the Text ----------------
C.sa("ex1", GET, "What 'experiment' did Maxwell think Camusfeàrna would be suitable for?",
     ["Keeping an otter as a pet instead of a dog.", "Camusfeàrna, ringed by water, would be a good home for an otter."], ex(1))
C.sa("ex2", GET, "Why was Maxwell in Basra?",
     ["He had gone to the Consulate-General at Basra.", "There he was to collect and answer his mail from Europe."], ex(2))
C.sa("ex3", GET, "How did Maxwell get the otter? Did he like it?",
     ["Two Arabs brought the otter to him in a sack at Basra.", "Yes; he was charmed by it and found it like a small medieval dragon, and he soon became deeply attached to it."], ex(3))
C.sa("ex4", GET, "Why was the otter named 'Maxwell's otter'?",
     ["Mij belonged to a race of otter unknown to science.", "Zoologists named this new species after Maxwell."], ex(4))
C.sa("ex5", HABITS, "Tell the story of Mij's adventures with water in your own words.",
     ["Mij went wild with joy in the bathtub, plunging, rolling and splashing like a child.", "Within a few days he learnt to turn on the tap himself, though at first not fully."], ex(5))
C.sa("ex6", HABITS, "What are some of the things Mij does that tell you he is intelligent?",
     ["He learnt to turn on the tap by himself.", "He invented a game with a rubber ball on the sloping lid of a suitcase and played alone for hours."], ex(6))
C.sa("ex7", JOURNEY, "Why was Mij put in a box, and what did he do to it?",
     ["Airlines would not carry animals loose, so he had to travel in a box.", "He tore at its metal lining in panic until his mouth and paws bled."], ex(7))
C.sa("ex8", LONDON, "What are some of the things that Londoners thought Mij was?",
     ["A baby seal, a squirrel or a walrus.", "A hippo, a beaver, a bear cub, a leopard and even a brontosaurus."], ex(8))

# ---------------- Extracts ----------------
C.extract("ext1", HABITS,
  "For the first twenty-four hours Mijbil was neither hostile nor friendly; he was simply aloof and indifferent,\nchoosing to sleep on the floor as far from my bed as possible.",
  [("Who is 'my' in the extract?", "Gavin Maxwell."),
   ("What does 'aloof' mean?", "Distant, not friendly."),
   ("Where did Mij choose to sleep at first?", "On the floor, as far from the bed as possible."),
   ("What changed on the second night?", "He came onto the bed and slept in the crook of Maxwell's knees."),
   ("Give the opposite of 'hostile'.", "Friendly.")])
C.extract("ext2", HABITS,
  "He would spend hours shuffling a rubber ball round the room like a soccer player\nusing all four feet to dribble the ball.",
  [("Who is 'he'?", "Mij, the otter."),
   ("What did he play with?", "A rubber ball."),
   ("Name the figure of speech in 'like a soccer player'.", "Simile."),
   ("What does this show about Mij?", "He was playful and clever; he could amuse himself."),
   ("Which word means 'moving the ball forward with small kicks'?", "Dribble.")])
C.extract("ext3", JOURNEY,
  "I had been told that the box must be eighteen inches square, and that it would be placed at my feet.\nI put Mijbil into the box an hour before we started, so that he would become accustomed to it.",
  [("Why was a box needed?", "The airline did not allow animals to travel loose."),
   ("How big was the box?", "Eighteen inches square."),
   ("Why did Maxwell put Mij in it an hour early?", "So that he would get used to it."),
   ("What did Mij do inside the box?", "He tore the lining and bled."),
   ("Give a word from the extract meaning 'used to'.", "Accustomed.")])

# ---------------- Objective practice ----------------
C.m("mcq01", GET, "In which year did Maxwell travel to southern Iraq?",
    [("1956", ""), ("1947", "It was early in 1956."), ("1969", "That is when he died."), ("1914", "That is when he was born.")],
    "He travelled there early in 1956.")
C.m("mcq02", GET, "Where did Maxwell's friend suggest he could get an otter?",
    [("in the Tigris marshes", ""), ("in a London zoo", "In the Tigris marshes."), ("in Scotland", "In the Tigris marshes."), ("in Paris", "In the Tigris marshes.")],
    "Otters were common there.")
C.m("mcq03", GET, "Mij looked like:",
    [("a very small medieval dragon", ""), ("a big dog", "He compared him to a small dragon."), ("a cat", "A small dragon."), ("a rabbit", "A small dragon.")],
    "Covered in mud-coloured fur in spikes.")
C.m("mcq04", HABITS, "Where did Mij sleep on the second night?",
    [("on Maxwell's bed, in the crook of his knees", ""), ("in the bathtub", "On the bed."), ("in his box", "On the bed."), ("on the floor", "That was the first night.")],
    "He had begun to trust Maxwell.")
C.m("mcq05", HABITS, "What did Mij learn to do in the bathroom?",
    [("turn on the tap", ""), ("open the door", "He learnt to turn on the tap."), ("switch on the light", "The tap."), ("swim in the sink", "The tap.")],
    "At first he could not turn it fully on.")
C.m("mcq06", JOURNEY, "What did Mij do in his travel box?",
    [("tore at the lining until he bled", ""), ("slept peacefully", "He panicked."), ("ate his food", "He tore the lining."), ("played with a ball", "He tore the lining.")],
    "There was blood on his mouth and paws.")
C.m("mcq07", JOURNEY, "Who helped Maxwell calmly on the plane?",
    [("the air hostess", ""), ("the pilot", "The air hostess."), ("a passenger who was a vet", "The air hostess."), ("no one", "The air hostess helped.")],
    "Maxwell praised her kindness.")
C.m("mcq08", LONDON, "What did Londoners NOT guess Mij was?",
    [("an otter", ""), ("a seal", "Some guessed seal."), ("a walrus", "Some guessed walrus."), ("a beaver", "Some guessed beaver.")],
    "Otters were unfamiliar to them.")
C.m("mcq09", GET, "Camusfeàrna is:",
    [("Maxwell's home in Scotland", ""), ("a town in Iraq", "It is in Scotland."), ("an airline", "It is his home."), ("Mij's mother", "It is his home.")],
    "It is ringed by water.")
C.m("mcq10", LANG, "'Pandemonium' means:",
    [("wild confusion", ""), ("deep silence", "It means the opposite."), ("great joy", "It means chaos."), ("a kind of otter", "It means chaos.")],
    "There was pandemonium on the plane.")
C.m("mcq11", HABITS, "Maxwell concludes that otters, like humans, need:",
    [("company and play", ""), ("only food", "They need company and play."), ("cages", "They need company and play."), ("silence", "They need company and play.")],
    "Mij was unhappy when alone.")
C.m("mcq12", JOURNEY, "Why did Maxwell open the box on the plane?",
    [("to calm Mij, who was struggling and bleeding", ""), ("to show Mij to passengers", "To calm him."), ("to feed the passengers", "To calm Mij."), ("because the hostess asked", "To calm Mij.")],
    "Mij then escaped.")
C.tf("tf1", GET, "Mij belonged to a species already well known to science.", False, "It was unknown to science and named Maxwell's otter.")
C.tf("tf2", HABITS, "Mij was friendly from the first moment.", False, "He was aloof for the first 24 hours.")
C.tf("tf3", JOURNEY, "The airline flying to England did not allow animals.", True, "So Maxwell flew via Paris.")
C.tf("tf4", HABITS, "Mij loved water and played in the bathtub.", True, "He splashed and rolled like a child.")

# ---------------- More written practice ----------------
C.sa("sa1", JOURNEY, "Describe the scene on the plane when Mij escaped.",
     ["Mij ran down the aisle; passengers were alarmed and a woman stood on her seat screaming 'A rat!'.", "The air hostess helped calmly and Mij was caught and returned to Maxwell."])
C.sa("sa2", HABITS, "How did Mij show that he trusted Maxwell?",
     ["From the second night he slept in the crook of Maxwell's knees.", "He followed Maxwell everywhere and played with him."])
C.la("la1", JOURNEY, "Narrate Mij's journey from Basra to London.",
     ["Airlines to England did not carry animals, so Maxwell booked a flight via Paris and put Mij in a small box.",
      "Mij tore the box's lining in panic and bled; Maxwell hurried to the airport with him.", "On the plane Maxwell opened the box to calm him, and Mij escaped down the aisle.",
      "There was chaos; a woman screamed 'A rat!' The kind air hostess helped and Mij was caught.", "They reached London, where people could not guess what animal Mij was."])
C.la("la2", HABITS + GET, "Should wild animals like Mij be kept as pets? Give your view with reasons from the story.",
     ["Mij became loving and playful with Maxwell, showing that wild animals can bond with people.", "But he suffered in the box and panicked on the plane: travel and cities are stressful for wild animals.",
      "Otters need water, space and company, which most homes cannot provide.", "Maxwell lived by the sea and studied animals; ordinary people cannot do this.",
      "So wild animals are better protected in their natural homes."])

# ---------------- Top-up practice ----------------
C.m("mcq13", GET, "In which city did Maxwell receive Mij?",
    [("Basra", ""), ("Baghdad", "Basra."), ("London", "He received him in Iraq."), ("Paris", "Basra.")],
    "He was at the Consulate-General there.")
C.m("mcq14", GET, "Why did Maxwell want an otter rather than a dog?",
    [("he thought an otter would suit his water-ringed home at Camusfeàrna", ""), ("dogs were not allowed in Scotland", "His home suited an otter."),
     ("otters are cheaper", "His home suited an otter."), ("he disliked dogs", "His home suited an otter.")],
    "Camusfeàrna was ringed by water.")
C.m("mcq15", HABITS, "How did Mij behave in water?",
    [("he went wild with joy, plunging and rolling", ""), ("he was afraid", "He loved water."), ("he refused to enter", "He loved water."), ("he sat still", "He played wildly.")],
    "He splashed like a child.")
C.m("mcq16", HABITS, "What game did Mij invent with a suitcase lid?",
    [("rolling a ball down the sloping lid and catching it", ""), ("hiding inside the suitcase", "A ball game."), ("pushing the suitcase", "A ball game."), ("sleeping on it", "A ball game.")],
    "This shows his intelligence.")
C.m("mcq17", JOURNEY, "What was the box for Mij lined with?",
    [("metal", ""), ("cloth", "Metal, which he tore."), ("straw", "Metal."), ("paper", "Metal.")],
    "He tore it and bled.")
C.m("mcq18", LONDON, "Why couldn't Londoners recognise Mij?",
    [("otters were unfamiliar to them", ""), ("Mij was in disguise", "They had never seen an otter."), ("it was dark", "They had not seen otters."), ("Mij was very large", "Otters were unfamiliar.")],
    "They guessed many animals.")
C.m("mcq19", LANG, "'Indifferent' means:",
    [("not interested", ""), ("very excited", "The opposite."), ("angry", "Not interested."), ("hungry", "Not interested.")],
    "Mij was aloof and indifferent at first.")
C.m("mcq20", JOURNEY, "Where was Mij's box to be kept on the plane?",
    [("at Maxwell's feet", ""), ("in the cargo hold", "At his feet."), ("on the roof", "At his feet."), ("with the pilot", "At his feet.")],
    "So Maxwell could watch over him.")
C.tf("tf5", LONDON, "Some Londoners thought Mij was a baby seal.", True, "Others guessed a squirrel, a walrus and more.")
C.tf("tf6", JOURNEY, "Mij stayed calm in his box throughout the journey.", False, "He tore the lining in panic and later escaped.")
C.vsa("vsa1", HABITS, "Give two signs that Mij began to trust Maxwell.", ["He slept in the crook of Maxwell's knees.", "He followed Maxwell everywhere."])
C.sa("sa3", GET, "What does the name 'Maxwell's otter' tell us?",
     ["Mij belonged to a race of otter unknown to science.", "Zoologists named the new species after Gavin Maxwell."])

chapter = header("ch06", 6, "Mijbil the Otter", "Gavin Maxwell", "prose",
                 ["getting_mijbil", "mijs_habits_and_intelligence", "journey_to_london", "mij_in_london", "vocabulary_and_style"],
                 "CBSE 2025-26 English Language and Literature (184): First Flight prose, Chapter 6. Assessed through extracts (5 marks), short answers in 40-50 words (3 marks) and long answers in 100-120 words (6 marks).")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
