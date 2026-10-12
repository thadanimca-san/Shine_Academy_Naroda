"""CBSE Class 10 English, Footprints without Feet Ch 6: The Making of a Scientist (Robert W. Peterson)."""
import sys
from lit_common import make, header, path, ex

ROOT = sys.argv[1]
PATH = path("ch06_the_making_of_a_scientist", "footprints")
C = make("fwf10ch06")
blk = C.blk
CHILD, PROJECTS, QUAL, MOTHER = ["ebrights_childhood"], ["science_projects"], ["qualities_of_a_scientist"], ["role_of_mother_and_teachers"]
RF = lambda n: ex(n, "Read and Find Out")
TA = lambda n: ex(n, "Think about It")

PROJ = ("| When | Project | Result |\n|---|---|---|\n"
        "| **Childhood** | collected butterflies (all 25 species around his hometown) and tagged monarchs for Dr Urquhart | the start of his interest |\n"
        "| **Seventh grade** | county science fair: slides of frog tissues | **lost**: winners had done real experiments |\n"
        "| **Eighth grade** | looked for the cause of a viral disease that kills monarch caterpillars | could not prove his idea, but learnt to experiment |\n"
        "| **Next year** | tested the theory that **viceroy butterflies copy monarchs** | entered county fair |\n"
        "| **High school** | found the purpose of the **twelve tiny gold spots** on a monarch pupa: they make a hormone needed for full development | **first prize** in the county fair and a place at the **International Science and Engineering Fair** |\n"
        "| **College** | with his room-mate, a new theory on **how cells read their DNA** | a major scientific paper |")

sections = [
 {"id": "s1", "title": "From butterflies to DNA", "blocks": [
  blk("s1.hook", "hook", title="It started with a butterfly collection",
    body="A boy in a small American town collects butterflies, rocks and fossils. A children's book about a monarch butterfly opens a door, and years later he helps explain how the cells of our body read their genetic instructions.\n\n"
         "This is the story of **Richard Ebright**, and of what really makes a scientist."),
  blk("s1.inspiration", "inspiration", title="The writer and the scientist", person="Robert W. Peterson",
    body="**Robert W. Peterson** wrote this account of **Richard H. Ebright**, an American scientist who began as a curious child in **Reading, Pennsylvania**. Ebright went on to graduate from **Harvard** with highest honours and became a leading researcher in molecular biology.",
    future="Every science fair, school project or nature club can be the first step towards a life in science."),
  C.socratic("s1.socratic", "Ebright lost his first science fair. Why did that loss help him?",
    ["It taught him that real experiments, not just displays, win in science", "It made him give up science", "It showed his teachers were unfair"], 0,
    "Failure can teach more than success."),
 ]},
 {"id": "s2", "title": "Ebright's journey", "blocks": [
  blk("s2.thm", "theory", title="What happens", revision=True,
    body="**Childhood:** Richard Ebright was the **only child** of his mother; his father died when he was in the third grade. He collected **butterflies**, rocks, fossils and coins. By the time he was in second grade, he had collected **all twenty-five species** of butterflies found around his hometown.\n\n"
         "**His mother:** she was his companion and guide. She took him on trips, bought him **telescopes, microscopes and cameras**, and helped him in every way. When he had collected all the local butterflies, she got him a children's book, **'The Travels of Monarch X'**, which told how monarch butterflies migrate to Central America. This book **opened the world of science** to him.\n\n"
         "**Tagging monarchs:** the book invited readers to help study the migration by **tagging butterflies** for **Dr Frederick Urquhart** of the University of Toronto. Ebright tagged and raised monarchs, but tagging was slow and few were recaptured, so he lost interest.\n\n"
         "**The lost science fair:** in **seventh grade** he entered the county science fair with **slides of frog tissues**, and **lost**. The winners had done **real experiments**. He realised that a science project needs experimenting, not just display.\n\n"
         "**Real experiments:** with Dr Urquhart's suggestions, he studied a viral disease of monarch caterpillars, tested the idea that **viceroy butterflies copy monarchs**, and then discovered the purpose of the **twelve tiny gold spots** on a monarch **pupa**: they produce a **hormone** needed for the butterfly's full development. This won **first prize** at the county fair and took him to the **International Science and Engineering Fair**.\n\n"
         "**The scientist:** at college he and his room-mate developed a new theory of **how cells read their DNA blueprint**, which was published as an important paper. Ebright also enjoyed **debate, public speaking, canoeing and photography**."),
  blk("s2.table", "markdown_table", title="Ebright's projects", revision=True, body=PROJ),
  C.kc("s2.check", "Which book opened the world of science to Ebright?",
    [("The Travels of Monarch X", ""), ("The Invisible Man", "That is fiction by H. G. Wells."), ("a school textbook", "The Travels of Monarch X."), ("a book on frogs", "The Travels of Monarch X.")],
    "His mother gave it to him.")
  ,C.kc("s2.check2", "Why did Ebright lose his first science fair?",
    [("his project only showed slides; the winners had done real experiments", ""), ("he arrived late", "Real experiments won."), ("his slides were broken", "Real experiments won."), ("he did not enter", "He entered and lost.")],
    "He learnt the value of experimenting.")
 ]},
 {"id": "s3", "title": "What makes a scientist", "blocks": [
  blk("s3.thm", "theory", title="Qualities and influences", revision=True,
    body="**Three qualities of a scientist** shown by Ebright:\n1. **A first-rate mind:** intelligence and curiosity, always asking why.\n2. **Hard work and persistence:** years of collecting, tagging, rearing and experimenting.\n3. **Wanting to win for the right reasons:** he was **competitive**, not to beat others, but to do his best and learn.\n\n"
         "**Influences:** his **mother**, who gave him books, equipment and her time; **Dr Urquhart**, who suggested projects; and his teachers, such as his social studies teacher, who praised his curiosity and his healthy competitiveness.\n\n"
         "**Wide interests:** debate, public speaking, canoeing, photography of nature and science, which show a well-rounded person.\n\n"
         "**Theme:** scientists are **made**, through curiosity, encouragement, failure and steady effort, not simply by reading books."),
  C.kc("s3.check", "Which is one quality of a scientist mentioned in the chapter?",
    [("wanting to win for the right reasons", ""), ("being rich", "Not a quality listed."), ("being famous", "Not listed."), ("avoiding failure", "He learnt from failure.")],
    "Ebright competed to do his best.")
  ,C.kc("s3.check2", "Who was Ebright's greatest support in childhood?",
    [("his mother", ""), ("his father", "His father died when he was young."), ("his brother", "He was an only child."), ("a neighbour", "His mother.")],
    "She bought him books and equipment.")
 ]},
 {"id": "s4", "title": "Language of the chapter", "blocks": [
  blk("s4.thm", "theory", title="Words to know", revision=True,
    body="| Word | Meaning |\n|---|---|\n| **species** | a group of similar living things |\n| **migration** | seasonal movement of animals from one region to another |\n"
         "| **pupa** | the resting stage between caterpillar and butterfly |\n| **hormone** | a chemical in the body that controls growth or activity |\n| **tagging** | putting a label on an animal to track it |\n| **DNA blueprint** | the genetic instructions in a cell |\n\n"
         "**Style:** a biographical account written in the third person, with quotations from Ebright and his teachers."),
  C.kc("s4.check", "A 'pupa' is:",
    [("the stage between caterpillar and butterfly", ""), ("an adult butterfly", "Before that."), ("an egg", "After the caterpillar."), ("a flower", "A stage of the butterfly.")],
    "Ebright studied the gold spots on it.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Mother → 'The Travels of Monarch X' → tagging for Dr Urquhart.**\n- **7th grade: frog slides, lost → lesson: experiment!**\n"
         "- **Projects: caterpillar virus, viceroy copies monarch, 12 gold spots = hormone (1st prize).**\n- **College: how cells read DNA.**\n- **Qualities: mind + hard work + win for the right reasons.**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying Ebright won his first science fair: he **lost** in seventh grade.\n2. Saying his father guided him: his **mother** did; his father died early.\n"
         "3. Forgetting the gold spots discovery: they make a **hormone**.\n4. Thinking science is only reading books: Ebright did **experiments**."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Students plan a small science fair project: a question, a simple experiment, and how they would record results, as Ebright learnt to do."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="What hobby or interest of yours could grow into a career? Who encourages you in it?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Science (Heredity, Life Processes):** DNA and hormones.\n- **Footprints without Feet:** a scientist who misused his gifts, in contrast."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="'Scientists are made, not born.' Discuss with reference to Richard Ebright, in about 120 words.\n\n"
         "**Model answer:** Richard Ebright's story shows how a scientist is made. As a child he collected butterflies, rocks and fossils, and his mother encouraged him with trips, books, telescopes and microscopes. A book, The Travels of Monarch X, opened the world of science to him, and he began tagging monarchs for Dr Urquhart. When he lost a science fair in seventh grade because he had only displayed slides, he learnt that science needs real experiments. He went on to test ideas, discover the hormone made by the gold spots on a monarch pupa, and later explain how cells read their DNA. His curiosity, hard work and wish to win for the right reasons, supported by his mother and teachers, made him a scientist."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Richard Ebright, an only child, collected butterflies and was encouraged by his mother.\n- 'The Travels of Monarch X' led him to tag monarchs for Dr Urquhart.\n"
         "- He lost his first science fair and learnt the value of real experiments.\n- His projects led to discoveries about monarch pupae and, later, how cells read DNA.\n"
         "- A scientist needs a good mind, hard work and the wish to win for the right reasons."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- Name the three qualities of a scientist with examples.\n- Explain the role of his mother clearly.\n- Use the science fair failure as a turning point."),
  blk("s5.flash1", "flashcard", front="What did Ebright learn from his first science fair?", back="That real experiments, not just displays, are needed to win."),
  blk("s5.flash2", "flashcard", front="What did the gold spots on a monarch pupa do?", back="They produce a hormone needed for the butterfly's full development."),
  blk("s5.flash3", "flashcard", front="Who was Dr Urquhart?", back="A scientist at the University of Toronto who studied monarch migration and suggested projects to Ebright."),
  blk("s5.flash4", "flashcard", front="Name three qualities of a scientist.", back="A first-rate mind, hard work and persistence, and wanting to win for the right reasons."),
 ]},
]

# ---------------- NCERT ----------------
C.vsa("rf1", CHILD, "How did a book become a turning point in Richard Ebright's life?", ["His mother gave him 'The Travels of Monarch X'.", "It opened the world of science and led him to tag monarchs for Dr Urquhart."], RF(1))
C.sa("rf2", MOTHER, "How did his mother help him?", ["She took him on trips and bought him telescopes, microscopes, cameras and books.", "She spent time with him and encouraged his interest in learning and science."], RF(2))
C.sa("rf3", PROJECTS, "What lesson does Ebright learn when he does not win anything at a science fair?", ["He learns that the winners had done real experiments.", "A science project needs experiments, not just neat displays like his frog slides."], RF(3))
C.sa("rf4", PROJECTS, "What experiments and projects does he then undertake?", ["He tested the idea that viceroy butterflies copy monarchs and studied a caterpillar disease.", "He found that the gold spots on monarch pupae make a growth hormone."], RF(4))
C.la("rf5", QUAL, "What are the qualities that go into the making of a scientist?",
     ["A first-rate mind: Ebright was intelligent and curious.", "Hard work: he spent years collecting, tagging and experimenting.",
      "Wanting to win for the right reasons: he competed to do his best and to learn.", "Persistence after failure: he learnt from losing a science fair.",
      "Support from family and teachers also helps, as his mother and Dr Urquhart helped him."], RF(5))
C.la("ta1", QUAL, "How can one become a scientist, an economist, a historian...? Does it simply involve reading many books? Does it involve observing and thinking?",
     ["Reading books gives knowledge, but it is not enough.", "One must observe carefully, ask questions and think for oneself.",
      "One must test ideas through experiments or research, as Ebright did with butterflies.", "Learning from failure, like his lost science fair, is important.",
      "Curiosity, hard work and guidance together make a scientist or scholar."], TA(1))
C.sa("ta2", MOTHER, "What role did Ebright's mother play in his success?",
     ["She was his companion after his father's death and encouraged every interest.", "She gave him books, equipment and trips, which opened the world of science to him."], TA(2))
C.sa("ta3", QUAL, "How did Ebright's competitive spirit help him?",
     ["He wanted to win, but in the right way: by doing his best.", "It pushed him to improve after losing, leading to prize-winning experiments."], TA(3))

# ---------------- Objective practice ----------------
C.m("mcq01", CHILD, "Richard Ebright grew up in:", [("Reading, Pennsylvania", ""), ("London", "Reading, Pennsylvania."), ("Toronto", "That is Dr Urquhart's university."), ("Iping", "Reading, Pennsylvania.")], "A small American town.")
C.m("mcq02", CHILD, "By second grade Ebright had collected:", [("all 25 species of butterflies around his town", ""), ("100 coins", "Butterflies."), ("all local birds", "Butterflies."), ("rare stamps", "Butterflies.")], "Then his mother gave him a book.")
C.m("mcq03", MOTHER, "When did Ebright's father die?", [("when he was in the third grade", ""), ("before he was born", "In third grade."), ("when he was in college", "In third grade."), ("he did not die", "He died early.")], "His mother brought him up.")
C.m("mcq04", CHILD, "'The Travels of Monarch X' is about:", [("the migration of monarch butterflies", ""), ("a king's journey", "Butterflies."), ("frogs", "Butterflies."), ("DNA", "Butterflies.")], "To Central America.")
C.m("mcq05", PROJECTS, "Ebright tagged butterflies for:", [("Dr Frederick Urquhart", ""), ("his mother", "For Dr Urquhart."), ("his school", "For Dr Urquhart."), ("a museum", "For Dr Urquhart.")], "To study migration.")
C.m("mcq06", PROJECTS, "His seventh-grade project was on:", [("slides of frog tissues", ""), ("monarch gold spots", "That came later."), ("DNA", "Much later."), ("viceroy butterflies", "Later.")], "It lost.")
C.m("mcq07", PROJECTS, "The gold spots on a monarch pupa produce:", [("a hormone needed for full development", ""), ("poison", "A hormone."), ("colour only", "A hormone."), ("food", "A hormone.")], "His prize-winning discovery.")
C.m("mcq08", PROJECTS, "Ebright tested the theory that viceroy butterflies:", [("copy monarchs", ""), ("eat monarchs", "They mimic them."), ("migrate to Canada", "They mimic monarchs."), ("cannot fly", "They mimic monarchs.")], "Birds avoid monarchs.")
C.m("mcq09", QUAL, "Which is NOT one of the three qualities of a scientist in the chapter?", [("great wealth", ""), ("a first-rate mind", "This is one."), ("hard work", "This is one."), ("wanting to win for the right reasons", "This is one.")], "Money is not mentioned.")
C.m("mcq10", PROJECTS, "At college, Ebright and his room-mate developed a theory about:", [("how cells read their DNA", ""), ("butterfly migration", "That was earlier."), ("frog tissues", "How cells read DNA."), ("invisibility", "How cells read DNA.")], "An important scientific paper.")
C.m("mcq11", QUAL, "Ebright graduated from:", [("Harvard, with highest honours", ""), ("Toronto", "Harvard."), ("Oxford", "Harvard."), ("he did not graduate", "Harvard.")], "He was a brilliant student.")
C.m("mcq12", QUAL, "Besides science, Ebright enjoyed:", [("debate, public speaking, canoeing and photography", ""), ("only science", "He had many interests."), ("wrestling", "Debate and photography."), ("cooking", "Debate and photography.")], "He was well-rounded.")
C.m("mcq13", PROJECTS, "Why did Ebright lose interest in tagging?", [("it was slow and few tagged butterflies were recaptured", ""), ("his mother stopped him", "Few were recaptured."), ("he was bored of science", "He moved to experiments."), ("butterflies disappeared", "Few were recaptured.")], "He turned to experiments.")
C.m("mcq14", MOTHER, "Ebright's mother bought him:", [("telescopes, microscopes and cameras", ""), ("toys only", "Scientific equipment."), ("a car", "Scientific equipment."), ("a pet dog", "Scientific equipment.")], "She supported his curiosity.")
C.m("mcq15", QUAL, "The main idea of the chapter is that:", [("curiosity, effort and encouragement make a scientist", ""), ("scientists are born geniuses", "They are made."), ("only rich children become scientists", "Effort matters."), ("failure ends a career", "Failure teaches.")], "Scientists are made.")
C.m("mcq16", CHILD, "Ebright was:", [("an only child", ""), ("the eldest of three", "An only child."), ("a twin", "An only child."), ("adopted", "An only child.")], "His mother was his companion.")
C.tf("tf1", PROJECTS, "Ebright won the county science fair in seventh grade.", False, "He lost; the winners did real experiments.")
C.tf("tf2", MOTHER, "Ebright's mother encouraged his interest in science.", True, "She gave him books and equipment.")
C.tf("tf3", PROJECTS, "The gold spots on monarch pupae produce a hormone.", True, "This was his key discovery.")
C.tf("tf4", CHILD, "Ebright's father guided all his projects.", False, "His father died when he was in third grade.")
C.tf("tf5", QUAL, "Ebright had no interests apart from science.", False, "He enjoyed debate, canoeing and photography.")
C.tf("tf6", CHILD, "A children's book led Ebright to tag monarch butterflies.", True, "The Travels of Monarch X.")

# ---------------- More ----------------
C.vsa("vsa1", MOTHER, "Name two things Ebright's mother did for him.", ["She took him on trips.", "She bought him telescopes, microscopes, cameras and books."])
C.vsa("vsa2", PROJECTS, "Name two of Ebright's science projects.", ["Testing whether viceroy butterflies copy monarchs.", "Finding the purpose of the gold spots on monarch pupae."])
C.sa("sa1", PROJECTS, "How did Dr Urquhart help Ebright?",
     ["He welcomed Ebright's help in tagging monarchs to study migration.", "He suggested ideas for experiments that led to Ebright's prize-winning projects."])
C.sa("sa2", QUAL, "'Wanting to win for the right reasons.' What does this mean in Ebright's case?",
     ["He was competitive, but he wanted to win by doing his best, not by beating others unfairly.", "Winning meant learning and improving, which pushed him to real experiments."])
C.sa("sa3", PROJECTS, "Why is the seventh-grade science fair a turning point?",
     ["Losing showed him that display was not enough; real experiments were needed.", "After this he chose experimental projects that won prizes."])
C.sa("sa4", CHILD, "How did Ebright's childhood hobbies prepare him for science?",
     ["Collecting butterflies, rocks and fossils taught him to observe and classify.", "Rearing and tagging monarchs taught patience and careful record-keeping."])
C.vsa("vsa3", CHILD, "What did Ebright collect as a child?", ["Butterflies, all twenty-five local species.", "Rocks, fossils and coins too."])
C.sa("sa5", PROJECTS, "What did Ebright find out about the twelve gold spots on a monarch pupa?",
     ["He found that they are not just decoration.", "They produce a hormone necessary for the butterfly's full development."])
C.sa("sa6", QUAL, "Why is curiosity important for a scientist? Answer with reference to Ebright.",
     ["Curiosity makes a scientist ask questions and look for answers.", "Ebright's curiosity about butterflies led him from collecting to experiments and new discoveries."])
C.la("la1", QUAL, "Write a character sketch of Richard Ebright.",
     ["Ebright was curious from childhood, collecting butterflies, rocks and fossils.", "He was hardworking and persistent, rearing and tagging monarchs for years.",
      "He learnt from failure: losing a science fair taught him to do real experiments.", "He was competitive in the right way, always trying to do his best.",
      "He was well-rounded, enjoying debate, canoeing and photography, and became a leading scientist."])
C.la("la2", MOTHER, "'Behind every successful child is an encouraging parent.' Discuss with reference to Ebright and his mother.",
     ["After his father's death, Ebright's mother became his companion.", "She took him on trips and bought telescopes, microscopes and cameras.",
      "She gave him 'The Travels of Monarch X', which opened the world of science.", "She spent her evenings with him and supported his projects.",
      "Her encouragement helped turn his curiosity into a scientific career."])
C.la("la3", PROJECTS, "Imagine you are Richard Ebright. Write a diary entry on the day you lost your first science fair.",
     ["Date and first person; describe your project of frog tissue slides.", "Your disappointment at not winning anything.",
      "What you noticed about the winners: they had done real experiments.", "Your resolve to do real experiments next time, and your hope for the future."])

chapter = header("ch06", 25, "The Making of a Scientist", "Robert W. Peterson", "prose",
                 ["ebrights_childhood", "science_projects", "qualities_of_a_scientist", "role_of_mother_and_teachers"],
                 "CBSE 2025-26 English Language and Literature (184): Footprints without Feet, Chapter 6. Assessed through short answers in 40-50 words (3 marks) and a long answer in 100-120 words (6 marks); no extracts from this book.",
                 book="footprints")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
