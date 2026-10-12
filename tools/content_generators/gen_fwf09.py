"""CBSE Class 10 English, Footprints without Feet Ch 9: The Book That Saved the Earth (Claire Boiko), a play."""
import sys
from lit_common import make, header, path, ex

ROOT = sys.argv[1]
PATH = path("ch09_the_book_that_saved_the_earth", "footprints")
C = make("fwf10ch09")
blk = C.blk
PLOT, CHARS, BOOKS, HUMOUR = ["the_martian_invasion"], ["characters"], ["mother_goose"], ["humour_and_message"]
RF = lambda n: ex(n, "Read and Find Out")
TA = lambda n: ex(n, "Think about It")

CAST = ("| Character | Who | Traits |\n|---|---|---|\n"
        "| **Historian** | a speaker from the future | introduces the story of how a book saved the Earth |\n"
        "| **Think-Tank** | the ruler of Mars, with a huge, egg-shaped head | proud, conceited, foolish; wants to be called 'Great and Mighty' |\n"
        "| **Noodle** | Think-Tank's assistant | humble, polite and actually sensible |\n"
        "| **Captain Omega** | commander of the space probe to Earth | obedient, efficient |\n"
        "| **Lieutenant Iota and Sergeant Oop** | members of the crew | simple, comic followers |")

sections = [
 {"id": "s1", "title": "Martians in the library", "blocks": [
  blk("s1.hook", "hook", title="Saved by nursery rhymes",
    body="Martians land in a small-town library on Earth, planning an invasion. Their leader studies a strange object, a book of **Mother Goose** nursery rhymes, and decides that Earth is far too dangerous to attack.\n\n"
         "This comic play shows how a simple book of rhymes 'saved the Earth'."),
  blk("s1.inspiration", "inspiration", title="The playwright", person="Claire Boiko",
    body="**Claire Boiko** was an American writer of short, lively plays for children. 'The Book That Saved the Earth' is a science-fiction comedy that laughs at pride and celebrates the value of books.",
    future="Writers of comedy and science fiction use misunderstanding, as Boiko does, to make audiences laugh and think."),
  C.socratic("s1.socratic", "Why did a book of nursery rhymes frighten the ruler of Mars?",
    ["He misread the rhymes literally, through his own pride and fear", "The book was magical", "Earth's army was hidden inside it"], 0,
    "Misunderstanding is the source of the comedy."),
 ]},
 {"id": "s2", "title": "The play", "blocks": [
  blk("s2.thm", "theory", title="What happens", revision=True,
    body="**The Historian:** a historian of the future explains that the **twentieth century** was called the **'Era of the Book'**, when books were used for everything. He then tells how a book once saved the Earth from a **Martian invasion** in the **twenty-first century**.\n\n"
         "**The Martians:** **Think-Tank**, the conceited ruler of Mars, with an enormous head, sends a space probe to Earth under **Captain Omega**, with **Lieutenant Iota** and **Sergeant Oop**. His assistant **Noodle** stays with him. The crew lands in the public **library** of a small town.\n\n"
         "**The mystery of books:** the Martians have never seen books. They guess they are **sandwiches** to eat or devices for communication. Noodle suggests they are for **reading**. Think-Tank tells them to read one.\n\n"
         "**Mother Goose:** they read nursery rhymes. **'Hey diddle diddle... the cow jumped over the moon'** makes Think-Tank believe that Earth people are so advanced that even their cows can travel in space. Then they read **'Humpty Dumpty sat on a wall... had a great fall'**. The picture of Humpty Dumpty looks just like Think-Tank's egg-shaped head, and he thinks the rhyme is a warning of a plot against him.\n\n"
         "**The retreat:** terrified, Think-Tank orders the probe to **leave Earth at once** and calls off the invasion, planning even to flee from Mars. So, the Historian concludes, a book of **Mother Goose** rhymes saved the Earth."),
  blk("s2.table", "markdown_table", title="The characters", revision=True, body=CAST),
  C.kc("s2.check", "Where did the Martians land on Earth?",
    [("in a public library", ""), ("in a school", "In a library."), ("in a market", "In a library."), ("in a forest", "In a library.")],
    "Full of the strange objects called books.")
  ,C.kc("s2.check2", "Why did Think-Tank order a retreat?",
    [("he thought the Humpty Dumpty rhyme threatened him", ""), ("Earth's army attacked", "No one attacked."), ("the probe broke down", "He was frightened by a rhyme."), ("Noodle asked to go home", "He was frightened.")],
    "Humpty Dumpty looked like him.")
 ]},
 {"id": "s3", "title": "Comedy and message", "blocks": [
  blk("s3.thm", "theory", title="Why the play is funny", revision=True,
    body="**Think-Tank:** proud and **conceited**; he insists on being called 'Great and Mighty', insults his followers, and claims to know everything, yet he understands nothing. His **huge ego** and **egg-shaped head** make him the object of the joke.\n\n"
         "**Noodle:** humble and **sensible**; he gives correct ideas but must pretend they are Think-Tank's, flattering him to avoid anger.\n\n"
         "**Humour:** comes from **misunderstanding** (books as sandwiches, nursery rhymes as scientific facts and threats), from Think-Tank's vanity, and from the silly obedience of the crew.\n\n"
         "**Message:** **pride and ignorance** lead to foolish decisions; a little knowledge used wisely (Noodle) is better than boastful 'genius'. The play also celebrates **books**, even simple rhymes, as powerful."),
  C.kc("s3.check", "Which word best describes Think-Tank?",
    [("conceited", ""), ("humble", "That is Noodle."), ("wise", "He misunderstood everything."), ("brave", "He fled in fear.")],
    "He wants to be called 'Great and Mighty'.")
  ,C.kc("s3.check2", "Why is Noodle important in the play?",
    [("he is the sensible one who suggests books are for reading", ""), ("he leads the probe", "That is Omega."), ("he eats the book", "He suggests reading."), ("he wants to attack Earth", "He is cautious.")],
    "Humble but wise.")
 ]},
 {"id": "s4", "title": "Language of the play", "blocks": [
  blk("s4.thm", "theory", title="Words to know", revision=True,
    body="| Word | Meaning |\n|---|---|\n| **invasion** | an attack to take over a place |\n| **probe** | a spacecraft sent to explore |\n| **conceited** | too proud of oneself |\n"
         "| **retreat** | to go back from danger |\n| **Mother Goose** | a famous collection of children's nursery rhymes |\n| **Era of the Book** | the twentieth century, when books were used widely |\n\n"
         "**Form:** a **play** with stage directions, a narrator (the Historian) and comic dialogue."),
  C.kc("s4.check", "'Mother Goose' is:",
    [("a collection of nursery rhymes", ""), ("a Martian ship", "Nursery rhymes."), ("a cookery book", "Nursery rhymes."), ("Think-Tank's mother", "Nursery rhymes.")],
    "Its rhymes 'saved the Earth'.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Historian: 20th century = Era of the Book; invasion in the 21st century.**\n- **Mars team: Think-Tank (big head), Noodle (assistant), Omega, Iota, Oop.**\n"
         "- **Library → books = sandwiches? → Mother Goose → cow over the moon → Humpty Dumpty → RETREAT.**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying the Martians fought a battle: they **retreated** without fighting.\n2. Mixing up Think-Tank and Noodle: Think-Tank is the **proud ruler**, Noodle the **sensible assistant**.\n"
         "3. Forgetting why Humpty Dumpty scared him: the picture looked like **his own head**."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Perform the library scene with five students. Then ask: which other nursery rhyme could fool the Martians, and how?"),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Have you ever misunderstood something because you took it too literally? What happened?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **The Proposal:** another comic play that laughs at human (and Martian!) pride.\n- **Footprints without Feet:** science fiction of a darker kind."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="How did a book of nursery rhymes save the Earth? Answer in about 120 words.\n\n"
         "**Model answer:** In the twenty-first century the Martians planned to invade Earth. Their proud ruler, Think-Tank, sent a probe that landed in a small-town library. The crew had never seen books and thought they might be sandwiches, until Noodle suggested they were for reading. They read Mother Goose rhymes. 'The cow jumped over the moon' convinced Think-Tank that Earth people were so advanced that even their cows could travel in space. Then the picture of Humpty Dumpty, an egg-shaped figure who has a great fall, looked exactly like Think-Tank, who took the rhyme as a threat against himself. Terrified, he ordered an immediate retreat. So, through Martian pride and misunderstanding, a simple book saved the Earth."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- A future Historian tells how a book saved Earth from a Martian invasion.\n- Think-Tank sends Captain Omega's probe, which lands in a library.\n"
         "- The Martians misunderstand books, then read Mother Goose rhymes.\n- Think-Tank takes 'Hey Diddle Diddle' and 'Humpty Dumpty' literally and orders a retreat.\n"
         "- Theme: pride and ignorance lead to folly; books have power."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- Name the two rhymes and explain how each was misread.\n- In character sketches, contrast Think-Tank and Noodle.\n- Mention the Historian's frame: 'Era of the Book'."),
  blk("s5.flash1", "flashcard", front="Why was the twentieth century called the 'Era of the Book'?", back="Because books were used everywhere, for learning, information and enjoyment."),
  blk("s5.flash2", "flashcard", front="What did Think-Tank conclude from 'the cow jumped over the moon'?", back="That Earth people were so advanced that even their cows could travel in space."),
  blk("s5.flash3", "flashcard", front="Why did Humpty Dumpty frighten Think-Tank?", back="The egg-shaped Humpty looked like him, so he thought the rhyme warned of his fall."),
  blk("s5.flash4", "flashcard", front="Who is Noodle?", back="Think-Tank's humble, sensible assistant, who suggests that books are for reading."),
 ]},
]

# ---------------- NCERT ----------------
C.vsa("rf1", PLOT, "Why is the twentieth century called the 'Era of the Book'?", ["Books were used for everything: learning, information and entertainment.", "There were books on every subject in libraries and homes."], RF(1))
C.vsa("rf2", PLOT, "Who tried to invade the Earth in the twenty-first century?", ["The Martians tried to invade the Earth.", "They were led by Think-Tank, the ruler of Mars."], RF(2))
C.sa("rf3", BOOKS, "What guesses are made by Think-Tank and the crew about the books found on Earth?", ["They guessed the books were sandwiches to eat, or devices for communication.", "Noodle suggested that they were for reading."], RF(3))
C.sa("rf4", BOOKS, "Why does Think-Tank believe that the people on Earth are very advanced?", ["He reads 'the cow jumped over the moon' literally.", "He thinks that if even cows can fly to the moon, Earth people must have advanced space technology."], RF(4))
C.sa("rf5", BOOKS, "Why does Think-Tank order his crew to retreat?", ["He sees a picture of egg-shaped Humpty Dumpty, who looks like him, having a great fall.", "He thinks it is a plot against him and fears for his life."], RF(5))
C.sa("rf6", PLOT, "How does the Historian end the story?", ["He says the Martians never came back.", "A simple book of Mother Goose rhymes had saved the Earth."], RF(6))
C.la("ta1", CHARS, "Noodle is shown as humble and sensible, Think-Tank as proud and foolish. Compare the two.",
     ["Think-Tank is the ruler of Mars, conceited, insisting on being called 'Great and Mighty'.", "He insults others and claims to know everything, yet he misunderstands books and rhymes.",
      "Noodle is his assistant, humble and polite, who gives correct ideas such as reading the books.", "Noodle must flatter Think-Tank and let him take credit to avoid his anger.",
      "The contrast shows that wisdom lies in humility, not in pride."], TA(1))
C.sa("ta2", HUMOUR, "What makes the play funny?",
     ["The Martians misunderstand books as sandwiches and nursery rhymes as facts.", "Think-Tank's vanity and egg-shaped head make his fear of Humpty Dumpty ridiculous."], TA(2))
C.sa("ta3", HUMOUR, "What is the message of the play?",
     ["Pride and ignorance lead to foolish decisions.", "Books, even simple ones, are powerful, and we should value them."], TA(3))

# ---------------- Objective practice ----------------
C.m("mcq01", PLOT, "The play was written by:", [("Claire Boiko", ""), ("Anton Chekhov", "He wrote The Proposal."), ("H. G. Wells", "Claire Boiko."), ("Ruskin Bond", "Claire Boiko.")], "A comic science-fiction play.")
C.m("mcq02", PLOT, "The twentieth century is called the:", [("Era of the Book", ""), ("Space Age", "Era of the Book."), ("Martian Age", "Era of the Book."), ("Stone Age", "Era of the Book.")], "Books were used everywhere.")
C.m("mcq03", CHARS, "Think-Tank is the:", [("ruler of Mars", ""), ("captain of the probe", "That is Omega."), ("Historian", "Ruler of Mars."), ("librarian", "Ruler of Mars.")], "With a huge head.")
C.m("mcq04", CHARS, "Who is Noodle?", [("Think-Tank's assistant", ""), ("a sergeant", "That is Oop."), ("an Earth child", "Think-Tank's assistant."), ("the Historian", "Think-Tank's assistant.")], "Humble and sensible.")
C.m("mcq05", PLOT, "Where did the Martians land?", [("in a library in a small town", ""), ("in a big city square", "A library."), ("in the desert", "A library."), ("on a ship", "A library.")], "Full of books.")
C.m("mcq06", BOOKS, "At first the Martians thought books were:", [("sandwiches", ""), ("weapons", "Sandwiches."), ("spaceships", "Sandwiches."), ("toys", "Sandwiches.")], "Or communication devices.")
C.m("mcq07", BOOKS, "The book the Martians read was:", [("Mother Goose nursery rhymes", ""), ("a science textbook", "Nursery rhymes."), ("a dictionary", "Nursery rhymes."), ("a newspaper", "Nursery rhymes.")], "Simple rhymes.")
C.m("mcq08", BOOKS, "Which rhyme made Think-Tank think Earth people were advanced?", [("'Hey diddle diddle... the cow jumped over the moon'", ""), ("'Twinkle, twinkle, little star'", "The cow and the moon."), ("'Baa, baa, black sheep'", "The cow and the moon."), ("'Jack and Jill'", "The cow and the moon.")], "He took it literally.")
C.m("mcq09", BOOKS, "Humpty Dumpty frightened Think-Tank because:", [("Humpty looked like him and had a great fall", ""), ("it was a war song", "Humpty looked like him."), ("Noodle laughed", "Humpty looked like him."), ("the book exploded", "Humpty looked like him.")], "He feared a plot.")
C.m("mcq10", PLOT, "What did Think-Tank finally order?", [("an immediate retreat from Earth", ""), ("an attack", "A retreat."), ("to read more books", "A retreat."), ("to capture the librarian", "A retreat.")], "The invasion was cancelled.")
C.m("mcq11", CHARS, "Think-Tank wanted to be addressed as:", [("Great and Mighty", ""), ("Captain", "Great and Mighty."), ("Little Brain", "That would insult him."), ("Doctor", "Great and Mighty.")], "His vanity shows.")
C.m("mcq12", HUMOUR, "The main source of humour in the play is:", [("misunderstanding and Think-Tank's pride", ""), ("a battle", "No battle."), ("sad events", "It is a comedy."), ("a love story", "It is a comedy.")], "Rhymes taken literally.")
C.m("mcq13", CHARS, "Captain Omega was:", [("commander of the space probe", ""), ("the ruler of Mars", "That is Think-Tank."), ("an Earth policeman", "Commander of the probe."), ("the Historian", "Commander of the probe.")], "With Iota and Oop.")
C.m("mcq14", HUMOUR, "The play shows that:", [("pride and ignorance lead to folly", ""), ("Martians are brave", "They fled."), ("books are useless", "A book saved Earth."), ("Earth is weak", "Earth was never attacked.")], "And books are powerful.")
C.m("mcq15", PLOT, "When did the Martian invasion attempt take place, according to the Historian?", [("in the twenty-first century", ""), ("in the tenth century", "The twenty-first."), ("in the twenty-fifth century", "That is near the Historian's time."), ("never", "It was attempted.")], "After the Era of the Book.")
C.m("mcq16", CHARS, "Think-Tank's head was:", [("huge and egg-shaped", ""), ("small and round", "Huge and egg-shaped."), ("square", "Egg-shaped."), ("covered with antennae", "Egg-shaped.")], "Like Humpty Dumpty.")
C.tf("tf1", PLOT, "The Martians fought a battle with Earth people.", False, "They retreated without fighting.")
C.tf("tf2", CHARS, "Noodle was humble and sensible.", True, "He suggested books were for reading.")
C.tf("tf3", BOOKS, "Think-Tank took the nursery rhymes literally.", True, "That led to his fear.")
C.tf("tf4", CHARS, "Think-Tank was modest about his intelligence.", False, "He was very conceited.")
C.tf("tf5", PLOT, "The Martians landed in a library.", True, "In a small town.")
C.tf("tf6", BOOKS, "The Martians knew at once what books were for.", False, "They guessed they were sandwiches.")

# ---------------- More ----------------
C.vsa("vsa1", BOOKS, "Name the two rhymes that frightened Think-Tank.", ["'Hey diddle diddle' (the cow jumped over the moon).", "'Humpty Dumpty'."])
C.vsa("vsa2", CHARS, "Name two members of the Martian crew.", ["Captain Omega and Lieutenant Iota.", "Sergeant Oop."])
C.vsa("vsa3", PLOT, "Who narrates the play's frame story?", ["A Historian from the future.", "He tells how a book saved the Earth."])
C.sa("sa1", CHARS, "How does Think-Tank treat his followers?",
     ["He insults them and calls them foolish names.", "He takes credit for Noodle's ideas and demands praise."])
C.sa("sa2", BOOKS, "How did Noodle help solve the mystery of books?",
     ["He politely suggested that books are meant to be read.", "He let Think-Tank take the credit, to avoid his anger."])
C.sa("sa3", HUMOUR, "Why is the title 'The Book That Saved the Earth' apt?",
     ["The Martian invasion was stopped only because of a book.", "Mother Goose rhymes frightened Think-Tank into retreating."])
C.sa("sa4", PLOT, "What role does the Historian play?",
     ["He introduces the play and explains the 'Era of the Book'.", "He links the events and gives the conclusion that a book saved the Earth."])
C.la("la1", CHARS, "Write a character sketch of Think-Tank.",
     ["Think-Tank is the ruler of Mars, with an enormous egg-shaped head.", "He is conceited and wants to be called 'Great and Mighty'.",
      "He is rude to his followers and takes credit for their ideas.", "He claims to know everything but misreads books and rhymes.",
      "His fear of Humpty Dumpty makes him flee, showing that pride and ignorance make him foolish."])
C.la("la2", BOOKS, "Describe how the Martians misunderstood the book of nursery rhymes.",
     ["The Martians first thought books were sandwiches or communication devices.", "Noodle suggested reading them, and they chose Mother Goose.",
      "'The cow jumped over the moon' made Think-Tank think Earth was highly advanced.", "'Humpty Dumpty' showed an egg-shaped figure falling, which he took as a threat to himself.",
      "In fear he ordered a retreat, so the misunderstanding saved the Earth."])
C.la("la3", HUMOUR, "Imagine you are Noodle. Write a diary entry about the day the Martians left Earth.",
     ["Date and first person; describe the landing in the library and the strange books.", "How you suggested reading them while letting Think-Tank take credit.",
      "Think-Tank's reaction to the cow over the moon and Humpty Dumpty.", "The sudden retreat, and your private thoughts about Think-Tank's pride."])

chapter = header("ch09", 28, "The Book That Saved the Earth", "Claire Boiko", "play",
                 ["the_martian_invasion", "characters", "mother_goose", "humour_and_message"],
                 "CBSE 2025-26 English Language and Literature (184): Footprints without Feet, Chapter 9 (play). Assessed through short answers in 40-50 words (3 marks) and a long answer in 100-120 words (6 marks); no extracts from this book.",
                 book="footprints")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
