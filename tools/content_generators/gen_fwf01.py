"""CBSE Class 10 English, Footprints without Feet Ch 1: A Triumph of Surgery (James Herriot)."""
import sys
from lit_common import make, header, path, ex

ROOT = sys.argv[1]
PATH = path("ch01_a_triumph_of_surgery", "footprints")
C = make("fwf10ch01")
blk = C.blk
SICK, CURE, CHARS, THEME = ["tricki_falls_ill"], ["herriots_treatment"], ["characters"], ["love_and_good_sense"]
RF = lambda n: ex(n, "Read and Find Out")
TA = lambda n: ex(n, "Think about It")

STAGES = ("| Stage | What happens to Tricki |\n|---|---|\n"
          "| **At home** | over-fed with cream cakes, chocolates, malt, cod-liver oil and Horlicks; no exercise; becomes hugely fat, lazy and ill |\n"
          "| **In the street** | Herriot sees him 'hideously bloated, like a distended sausage', eyes bloodshot, tongue lolling |\n"
          "| **At the surgery, days 1-2** | no food at all, only plenty of water; lies listless |\n"
          "| **At the surgery, later** | runs with the other dogs, joins the rough-and-tumble, fights for his food; grows lean and lively |\n"
          "| **Back home (two weeks)** | leaps from the car into Mrs Pumphrey's arms, fit and happy |")

sections = [
 {"id": "s1", "title": "Too much love", "blocks": [
  blk("s1.hook", "hook", title="A dog that was loved too much",
    body="Tricki is a little dog whose rich owner loves him so much that she feeds him cream cakes, chocolates and tonics all day. The result? He becomes so fat and ill that he can hardly walk.\n\n"
         "In this funny, warm story, a sensible country vet finds a simple cure, and his rich client calls it **'a triumph of surgery'**."),
  blk("s1.inspiration", "inspiration", title="The writer", person="James Herriot", years="1916–1995",
    body="**James Herriot** was the pen name of **James Alfred Wight**, a veterinary surgeon who worked for more than fifty years in the Yorkshire countryside of England. His books about his patients and their owners, such as **All Creatures Great and Small**, are loved for their gentle humour. This story comes from those books.",
    future="Vets, doctors and dieticians often have to tell caring families, tactfully, that too much food or comfort is harming the one they love."),
  C.socratic("s1.socratic", "Mrs Pumphrey loved Tricki dearly, yet he fell ill. How can love harm someone?",
    ["When love is not guided by good sense, as in over-feeding and pampering", "Love can never harm anyone", "Only when the pet is unkind"], 0,
    "Loving and being sensible are not the same thing."),
 ]},
 {"id": "s2", "title": "The story", "blocks": [
  blk("s2.thm", "theory", title="What happens", revision=True,
    body="**The worry:** the narrator, a vet (Herriot), sees **Mrs Pumphrey**, a rich widow, walking her dog **Tricki** in the street. Tricki is **hideously bloated, like a distended hairy sausage**, his eyes bloodshot and rheumy, his tongue lolling. Mrs Pumphrey says he is listless and has no energy; she thinks he has **malnutrition**, so she gives him **malt and cod-liver oil** between meals and **Horlicks** at night to help him sleep.\n\n"
         "**The real cause:** she also feeds him **cream cakes and chocolates**, 'little extras', and he gets no proper exercise. Herriot advises her to **cut down his food**, give no cakes or chocolates, and take him for long walks. But Mrs Pumphrey cannot resist Tricki's pleading eyes, and Tricki grows worse: he has bouts of **vomiting**, will not eat, and starts **'flop-bot'** (his hind legs go weak).\n\n"
         "**The surgery:** Herriot persuades her to send Tricki to his **surgery** for **two weeks**. Tricki arrives in a car with his bed, toys, cushions and coats. For the **first two days** Herriot gives him **no food, only plenty of water**. Then Tricki begins to **play with the other dogs**, gets knocked about in their games, and soon fights for his share of food. He grows lean and lively.\n\n"
         "**The gifts:** meanwhile Mrs Pumphrey sends **fresh eggs** (to build up Tricki's strength) and then **bottles of wine and brandy**. Herriot and his partners enjoy them, which tempts Herriot to keep Tricki as a **permanent guest**.\n\n"
         "**The return:** after two weeks Mrs Pumphrey arrives in her **chauffeur-driven car**. Tricki **leaps** out of Herriot's arms into hers and licks her face. With tears in her eyes she cries, 'Oh, Mr Herriot, how can I ever thank you? This is **a triumph of surgery**!'"),
  blk("s2.table", "markdown_table", title="Tricki from sick to fit", revision=True, body=STAGES),
  C.kc("s2.check", "Why did Mrs Pumphrey give Tricki malt, cod-liver oil and Horlicks?",
    [("she wrongly thought he was suffering from malnutrition", ""), ("Herriot prescribed them", "Herriot told her to cut down his food."),
     ("Tricki liked their taste only", "She thought he was undernourished."), ("to make him lose weight", "They made him fatter.")],
    "In fact he was over-fed.")
  ,C.kc("s2.check2", "What did Herriot give Tricki for the first two days at the surgery?",
    [("no food, only plenty of water", ""), ("cream cakes", "That caused the problem."), ("medicine injections", "No surgery or medicine was needed."), ("eggs and brandy", "Herriot enjoyed those himself.")],
    "Starving the excess away was the cure.")
 ]},
 {"id": "s3", "title": "The people and the message", "blocks": [
  blk("s3.thm", "theory", title="Characters and theme", revision=True,
    body="**Mrs Pumphrey:** rich, warm-hearted and generous, but **foolish and over-indulgent**. She cannot say no to Tricki and mistakes over-feeding for love. She is also **anxious**: she phones for news and sends gifts.\n\n"
         "**The narrator (Herriot):** a **sensible, tactful and practical** vet. He knows the cure is simple diet and exercise, but explains it gently so as not to hurt her. He is honest enough to admit that the eggs and wine tempted him, which adds humour.\n\n"
         "**Tricki:** a pampered little dog who, given a chance, becomes a normal, playful dog.\n\n"
         "**Humour and irony:** no surgery is done at all; the 'triumph' is just starvation and exercise, yet Mrs Pumphrey calls it 'a triumph of surgery'. Herriot does not correct her.\n\n"
         "**Theme:** love must be guided by **good sense**. Over-indulgence can harm children and pets; discipline, exercise and simple food keep them healthy."),
  C.kc("s3.check", "Why is the title ironic?",
    [("no surgery was performed; the cure was only diet and exercise", ""), ("Herriot operated on Tricki", "No operation took place."), ("Tricki died", "He recovered."), ("Mrs Pumphrey was a surgeon", "Herriot is a vet.")],
    "Mrs Pumphrey did not understand what had cured Tricki.")
  ,C.kc("s3.check2", "Which word best describes Herriot?",
    [("sensible and tactful", ""), ("greedy", "He enjoyed the gifts but put Tricki first."), ("careless", "He cured Tricki carefully."), ("rude", "He handled Mrs Pumphrey gently.")],
    "He cured the dog without offending the owner.")
 ]},
 {"id": "s4", "title": "Language of the story", "blocks": [
  blk("s4.thm", "theory", title="Words and expressions to know", revision=True,
    body="| Word or phrase | Meaning |\n|---|---|\n| **bloated / distended** | swollen, puffed up |\n| **rheumy** | watery (of the eyes) |\n| **listless** | without energy or interest |\n"
         "| **malnutrition** | illness from not eating the right food |\n| **flop-bot** | Herriot's comic word for Tricki's weak, dragging hind legs |\n| **convalescence** | the period of getting well again |\n"
         "| **surgery** | here, the vet's clinic (and an operation) |\n| **a triumph of surgery** | a great success of medical skill (said ironically) |\n\n"
         "**Style:** first-person narration with gentle humour; the vet laughs at himself and at Mrs Pumphrey without being unkind."),
  C.kc("s4.check", "'Listless' means:",
    [("lacking energy", ""), ("without a list", "It means lacking energy."), ("very active", "The opposite."), ("hungry", "Lacking energy.")],
    "Tricki was listless because he was over-fed and unexercised.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Problem: cakes + chocolates + tonics + no walks = fat, sick Tricki.**\n- **Cure: 2 days water only → play with dogs → lean and lively, in 2 weeks.**\n- **Gifts: eggs, then wine and brandy.**\n- **End: 'a triumph of surgery' (but no surgery!).**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying Herriot operated on Tricki: he only used **diet and exercise**.\n2. Saying Tricki had malnutrition: he was **over-fed**; Mrs Pumphrey only thought so.\n"
         "3. Calling Herriot greedy: he enjoyed the gifts but **cured the dog** and sent him home.\n4. Forgetting that Mrs Pumphrey is kind: she is **loving but unwise**."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Role-play the phone calls: a student as Mrs Pumphrey asks anxious questions; another as Herriot gives tactful replies without revealing that Tricki is simply being starved."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Have you seen children or pets being given too many sweets or gadgets out of love? What would be a sensible way to show love?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Science (Life Processes):** balanced diet and nutrition.\n- **Mijbil the Otter:** another loving relationship between a person and an animal.\n- **Amanda!:** a different way in which adults can harm children while meaning well."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="'Love without good sense can be harmful.' Explain with reference to A Triumph of Surgery, in about 120 words.\n\n"
         "**Model answer:** Mrs Pumphrey loves her dog Tricki dearly, but her love has no good sense. She feeds him cream cakes and chocolates, gives him malt, cod-liver oil and Horlicks, and lets him lie about without exercise. As a result Tricki becomes hugely fat, listless and ill, and even begins to vomit and drag his hind legs. When the sensible vet, Herriot, takes him to his surgery, he gives him only water for two days and then lets him run and play with other dogs. In two weeks Tricki is lean and lively. Mrs Pumphrey thinks it is a triumph of surgery, but the real lesson is that true love sometimes means saying no. Whether with pets or children, care must be wise."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Mrs Pumphrey, a rich widow, over-feeds her dog Tricki and he becomes fat and ill.\n- The vet, Herriot, advises less food and more exercise, but she cannot follow it.\n"
         "- He takes Tricki to his surgery for two weeks: water only at first, then play with other dogs.\n- Mrs Pumphrey sends eggs, wine and brandy, which the vets enjoy.\n"
         "- Tricki returns fit and happy; Mrs Pumphrey calls it 'a triumph of surgery'. Theme: love must be sensible."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- Footprints questions are short answers (3 marks, 40-50 words) and long answers (6 marks, 100-120 words); there are no extracts.\n"
         "- In character sketches, give two qualities with evidence from the story.\n- Explain the irony of the title in value-based answers."),
  blk("s5.flash1", "flashcard", front="What was wrong with Tricki?", back="He was over-fed and under-exercised, so he became hugely fat, listless and ill."),
  blk("s5.flash2", "flashcard", front="How did Herriot cure Tricki?", back="No food for two days, only water; then exercise and play with other dogs for two weeks."),
  blk("s5.flash3", "flashcard", front="What did Mrs Pumphrey send to the surgery?", back="Fresh eggs, then bottles of wine and brandy."),
  blk("s5.flash4", "flashcard", front="Why is the title ironic?", back="No surgery was done; the dog was cured only by diet and exercise."),
 ]},
]

# ---------------- NCERT: Read and Find Out ----------------
C.vsa("rf1", SICK, "Why is Mrs Pumphrey worried about Tricki?",
      ["Tricki has become very fat and listless and seems ill.", "He has no energy, vomits, and drags his hind legs."], RF(1))
C.vsa("rf2", SICK, "What does she do to help him? Is she wise in this?",
      ["She gives him malt and cod-liver oil between meals and Horlicks at night, besides cakes and chocolates.", "No, it is unwise: he is over-fed, and this only makes him worse."], RF(2))
C.vsa("rf3", CHARS, "Who does 'I' refer to in this story?",
      ["'I' is the narrator, James Herriot.", "He is a veterinary surgeon (vet)."], RF(3))
C.vsa("rf4", CHARS, "Is the narrator as rich as Tricki's mistress?",
      ["No, he is not as rich as Mrs Pumphrey.", "He enjoys her gifts of eggs, wine and brandy as luxuries."], RF(4))
C.sa("rf5", CURE, "How does he treat the dog?",
     ["He gives Tricki no food for two days, only plenty of water.", "Then he lets him play and run with the other dogs, so he grows lean and lively."], RF(5))
C.sa("rf6", CURE, "Why is he tempted to keep Tricki as a permanent guest?",
     ["Mrs Pumphrey keeps sending fresh eggs, wine and brandy for Tricki.", "Herriot and his partners enjoy these luxuries, so he is tempted to keep the dog."], RF(6))
C.sa("rf7", THEME, "Why does Mrs Pumphrey think the dog's recovery is 'a triumph of surgery'?",
     ["Tricki comes back fit, lively and happy after two weeks at the surgery.", "She does not know he was cured only by diet and exercise, so she thinks Herriot performed a medical miracle."], RF(7))

# ---------------- NCERT: Think about It ----------------
C.sa("ta1", CHARS, "What kind of a person do you think the narrator, a veterinary surgeon, is? Would you say he is tactful as well as full of common sense?",
     ["He is kind, practical and honest about himself, with a sense of humour.", "Yes, he is tactful: he cures Tricki by common sense (diet and exercise) without hurting Mrs Pumphrey's feelings."], TA(1))
C.la("ta2", CHARS, "Do you think Mrs Pumphrey was a sensible woman? How would you have handled the situation if you were in her place?",
     ["Mrs Pumphrey was loving and generous, but not sensible.", "She over-fed Tricki with cakes, chocolates and tonics and gave him no exercise, and could not follow the vet's advice.",
      "In her place I would have followed the vet's advice at once: a measured diet and no sweets.", "I would take the dog for regular long walks and let him play with other dogs.",
      "I would show love through care and discipline, not through treats."], TA(2))
C.la("ta3", THEME, "Do you think this story would be equally enjoyable if it were told by Mrs Pumphrey, or the dog? Who would you say is the hero of the story? Explain.",
     ["Told by Herriot, the story has gentle humour and honesty: he laughs at himself and at Mrs Pumphrey.", "Mrs Pumphrey would tell it seriously and believe in the 'surgery', so the irony would be lost.",
      "Tricki could tell only of hunger and play, and would miss the human comedy.", "The hero is Herriot, whose tact and common sense save the dog.",
      "So the story is best told by the vet."], TA(3))

# ---------------- Objective practice ----------------
C.m("mcq01", SICK, "Who was Tricki?", [("Mrs Pumphrey's pet dog", ""), ("Herriot's cat", "A dog."), ("a horse", "A dog."), ("Mrs Pumphrey's servant", "A dog.")], "A pampered little dog.")
C.m("mcq02", SICK, "Tricki looked 'like a distended hairy sausage' because he was:", [("hugely fat", ""), ("very thin", "The opposite."), ("dirty", "He was bloated."), ("injured", "He was bloated.")], "He was over-fed.")
C.m("mcq03", SICK, "What did Mrs Pumphrey give Tricki at night to help him sleep?", [("Horlicks", ""), ("brandy", "That came to the surgery."), ("milk and honey", "Horlicks."), ("a sleeping pill", "Horlicks.")], "Malt and cod-liver oil went between meals.")
C.m("mcq04", CURE, "How long did Tricki stay at the surgery?", [("about two weeks", ""), ("two days", "Two days was the fast."), ("two months", "Two weeks."), ("one year", "Two weeks.")], "Then he went home fit.")
C.m("mcq05", CURE, "What helped Tricki most at the surgery?", [("a strict diet and play with other dogs", ""), ("an operation", "No surgery was done."), ("special medicines", "Diet and exercise."), ("more cakes", "No cakes at all.")], "Common sense, not medicine.")
C.m("mcq06", CURE, "What did Mrs Pumphrey send to the surgery?", [("fresh eggs, wine and brandy", ""), ("cakes and chocolates", "Eggs, wine and brandy."), ("money", "Eggs, wine and brandy."), ("toys only", "His toys came with him.")], "To 'build up' Tricki's strength.")
C.m("mcq07", CHARS, "Who enjoyed Mrs Pumphrey's gifts?", [("Herriot and his partners", ""), ("Tricki", "Tricki was on a diet."), ("the other dogs", "The vets enjoyed them."), ("Mrs Pumphrey's maid", "The vets.")], "That is why Herriot was tempted to keep Tricki.")
C.m("mcq08", THEME, "Why did Mrs Pumphrey call it 'a triumph of surgery'?", [("she believed Herriot had worked a medical miracle", ""), ("Herriot operated on Tricki", "No operation was done."), ("Tricki died", "He recovered."), ("she was joking", "She was sincere.")], "The irony is lost on her.")
C.m("mcq09", CHARS, "Mrs Pumphrey can best be described as:", [("loving but over-indulgent", ""), ("cruel", "She loved Tricki."), ("sensible", "She could not follow advice."), ("poor", "She was rich.")], "She could not say no to Tricki.")
C.m("mcq10", CURE, "During the first two days at the surgery Tricki:", [("got no food, only water", ""), ("ate cream cakes", "No food at all."), ("played all day", "He lay listless at first."), ("went home", "He stayed.")], "Then he joined the other dogs.")
C.m("mcq11", SICK, "'Listless' means:", [("without energy", ""), ("cheerful", "Without energy."), ("angry", "Without energy."), ("hungry", "Without energy.")], "Tricki was listless at home.")
C.m("mcq12", SICK, "Mrs Pumphrey thought Tricki was suffering from:", [("malnutrition", ""), ("over-eating", "That was the truth, not her belief."), ("a broken leg", "Malnutrition."), ("old age", "Malnutrition.")], "She was wrong.")
C.m("mcq13", THEME, "The story's message is that:", [("love should be guided by good sense", ""), ("dogs should not be kept as pets", "Love must be sensible."), ("vets are greedy", "Love must be sensible."), ("rich people are happy", "Love must be sensible.")], "Over-indulgence harms.")
C.m("mcq14", CHARS, "Herriot is:", [("a veterinary surgeon", ""), ("a human surgeon", "A vet."), ("Mrs Pumphrey's chauffeur", "A vet."), ("a dog trainer", "A vet.")], "He wrote about his animal patients.")
C.m("mcq15", CURE, "How did Tricki return to Mrs Pumphrey?", [("he leapt into her arms", ""), ("he limped slowly", "He was lively."), ("he was carried asleep", "He leapt."), ("he refused to go", "He leapt into her arms.")], "He was fit and happy.")
C.m("mcq16", SICK, "Herriot first saw the sick Tricki:", [("in the street, with Mrs Pumphrey", ""), ("at the surgery", "In the street."), ("at a dog show", "In the street."), ("in a hospital", "In the street.")], "He was shocked by the dog's look.")
C.tf("tf1", CURE, "Herriot performed an operation on Tricki.", False, "He cured him with diet and exercise only.")
C.tf("tf2", CHARS, "Mrs Pumphrey was a rich widow.", True, "She had a chauffeur-driven car and servants.")
C.tf("tf3", CURE, "Tricki played with the other dogs at the surgery.", True, "This exercise helped him recover.")
C.tf("tf4", SICK, "Tricki was underweight when Herriot met him.", False, "He was hugely overweight.")
C.tf("tf5", CHARS, "Herriot refused to accept any of Mrs Pumphrey's gifts.", False, "He and his partners enjoyed the eggs, wine and brandy.")
C.tf("tf6", THEME, "The title of the story is ironic.", True, "No surgery was performed.")

# ---------------- More short and long answers ----------------
C.vsa("vsa1", SICK, "Name two things Mrs Pumphrey fed Tricki that made him fat.", ["Cream cakes.", "Chocolates (also malt, cod-liver oil and Horlicks)."])
C.vsa("vsa2", CURE, "What two things did Herriot's treatment involve?", ["A strict diet: no food at first, only water.", "Exercise: running and playing with other dogs."])
C.sa("sa1", SICK, "Describe Tricki's condition when Herriot saw him in the street.",
     ["He was hideously bloated, like a distended hairy sausage, with bloodshot, rheumy eyes.", "His tongue lolled from his jaws and he could barely walk; he was listless."])
C.sa("sa2", CHARS, "Why could Mrs Pumphrey not follow Herriot's advice?",
     ["She loved Tricki too much to refuse him anything.", "She could not resist his pleading eyes and kept giving him extra treats."])
C.sa("sa3", CURE, "How did Tricki change at the surgery?",
     ["At first he lay listless, getting only water.", "Soon he joined the other dogs, ran and played, fought for food, and became lean and lively."])
C.sa("sa4", CHARS, "How does Herriot show honesty and humour in telling the story?",
     ["He admits that the eggs, wine and brandy tempted him to keep Tricki longer.", "He gently laughs at himself and at Mrs Pumphrey without being unkind."])
C.sa("sa5", THEME, "What is the difference between being loving and being sensible, as shown in the story?",
     ["Mrs Pumphrey is loving: she gives Tricki whatever he wants.", "Herriot is sensible: he gives Tricki what is good for him, diet and exercise, which truly helps."], TA(4))
C.la("la1", CHARS, "Write a character sketch of Mrs Pumphrey.",
     ["Mrs Pumphrey is a rich, elderly widow who lives in comfort with servants and a chauffeur.", "She is warm-hearted and generous, and loves her dog Tricki dearly.",
      "But she is foolish and over-indulgent: she feeds him cakes, chocolates and tonics and gives him no exercise.", "She is anxious and emotional: she phones for news, sends eggs and wine, and weeps with joy at his return.",
      "Her innocent belief in 'a triumph of surgery' makes her a comic but likeable character."])
C.la("la2", CURE, "Describe how Herriot cured Tricki and how Tricki returned home.",
     ["Herriot took Tricki to his surgery for two weeks.", "For two days he gave him no food, only water; then he let him run and play with the other dogs.",
      "Tricki joined their games, fought for his food and became lean and lively.", "Meanwhile Mrs Pumphrey sent eggs, wine and brandy, which the vets enjoyed.",
      "When she came, Tricki leapt into her arms, and she called his recovery 'a triumph of surgery'."])
C.la("la3", THEME, "Imagine you are Herriot. Write a diary entry on the day Tricki went back home.",
     ["Date and first person; describe Mrs Pumphrey's arrival in her chauffeur-driven car.", "Tricki leaping into her arms, fit and lively after two weeks of diet and play.",
      "Her tears and her words, 'a triumph of surgery', and your amusement at the irony.", "Your mixed feelings: pleasure at the cure, and a little regret at losing the eggs and wine."])

chapter = header("ch01", 20, "A Triumph of Surgery", "James Herriot", "prose",
                 ["tricki_falls_ill", "herriots_treatment", "characters", "love_and_good_sense"],
                 "CBSE 2025-26 English Language and Literature (184): Footprints without Feet, Chapter 1. Assessed through short answers in 40-50 words (3 marks) and a long answer in 100-120 words (6 marks); no extracts from this book.",
                 book="footprints")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
