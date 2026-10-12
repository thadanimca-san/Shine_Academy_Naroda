"""CBSE Class 10 English, Footprints without Feet Ch 2: The Thief's Story (Ruskin Bond)."""
import sys
from lit_common import make, header, path, ex

ROOT = sys.argv[1]
PATH = path("ch02_the_thiefs_story", "footprints")
C = make("fwf10ch02")
blk = C.blk
MEET, THEFT, CHANGE, CHARS = ["hari_meets_anil"], ["the_theft"], ["the_change_of_heart"], ["characters"]
RF = lambda n: ex(n, "Read and Find Out")
TA = lambda n: ex(n, "Think about It")

REACT = ("| Kind of person robbed | Reaction, according to Hari |\n|---|---|\n"
         "| **a greedy man** | fear |\n| **a rich man** | anger |\n| **a poor man** | acceptance |\n"
         "| **Anil (a trusting man)** | only a touch of sadness, not for the money but for the loss of trust |")

sections = [
 {"id": "s1", "title": "A thief and a trusting man", "blocks": [
  blk("s1.hook", "hook", title="What would you do with six hundred rupees?",
    body="A fifteen-year-old thief gets a job with a young writer who trusts him completely. One night he steals the writer's money and runs to catch a train. But the train leaves without him. Why?\n\n"
         "**Ruskin Bond** tells this story through the thief's own eyes, and shows how trust and education can change a person."),
  blk("s1.inspiration", "inspiration", title="The writer", person="Ruskin Bond", years="born 1934",
    body="**Ruskin Bond** is one of India's best-loved writers of stories, novels and essays, many set in the hills of Mussoorie and Dehradun. He won the **Sahitya Akademi Award** and the **Padma Bhushan**. His stories are simple, warm and full of ordinary people.",
    future="Teachers, social workers and mentors know that trusting someone can change their life, as Anil's trust changes Hari's."),
  C.socratic("s1.socratic", "Anil knew Hari had stolen the money but said nothing. Why might silence work better than punishment?",
    ["It let Hari feel ashamed and choose to change by himself", "Anil was afraid of Hari", "Anil did not care about money at all"], 0,
    "Trust can reform where punishment only hardens."),
 ]},
 {"id": "s2", "title": "The story", "blocks": [
  blk("s2.thm", "theory", title="What happens", revision=True,
    body="**The meeting:** the narrator, **Hari Singh**, is a **fifteen-year-old thief**, 'a fairly successful hand'. He changes his name every month to stay ahead of the police and former employers. He watches **Anil**, a writer of about **twenty-five**, at a **wrestling match**, flatters him and asks for work. Anil says he cannot pay him but can **feed him if he can cook**.\n\n"
         "**Working for Anil:** Hari's first meal is so bad that Anil gives it to a stray dog, but Anil **teaches him to cook**. He also teaches him to **write his name** and promises to teach him to **write whole sentences and add figures**. Hari makes a small profit, about a rupee a day, on the shopping. Anil makes money **'by fits and starts'**, writing for magazines.\n\n"
         "**The theft:** one day Anil brings home a bundle of notes (**six hundred rupees**) from a publisher and puts it **under his mattress**. That night Hari takes the money and goes to the station to catch the **Lucknow Express**.\n\n"
         "**The change of heart:** as the train starts, Hari **does not board**. He thinks of how Anil would react: only a touch of **sadness**, for the loss of trust. He realises that being able to **write whole sentences** would one day bring him far more than a few hundred rupees, and that he would be a **'big man'** only through education. He sits in the rain at the **maidan**, then **returns and puts the damp notes back** under the mattress.\n\n"
         "**The next morning:** Anil gives him a **fifty-rupee note**, saying he made some money yesterday and will now pay him regularly. Hari notices the notes are **still wet** from the rain: Anil knows, but says nothing. 'We'll start writing sentences today,' says Anil."),
  blk("s2.table", "markdown_table", title="How people react when robbed, according to Hari", revision=True, body=REACT),
  C.kc("s2.check", "What did Anil offer Hari instead of wages?",
    [("food, if Hari could cook", ""), ("a room and a salary", "He could not pay him at first."), ("a free train ticket", "Food in return for cooking."), ("nothing at all", "He offered food.")],
    "Later he also taught him to read and write.")
  ,C.kc("s2.check2", "Where did Hari go after stealing the money?",
    [("to the railway station, to catch the Lucknow Express", ""), ("to the police station", "He went to catch a train."), ("to the wrestling ground", "To the station."), ("to Anil's publisher", "To the station.")],
    "But he did not board the train.")
 ]},
 {"id": "s3", "title": "Hari, Anil and the message", "blocks": [
  blk("s3.thm", "theory", title="Characters and theme", revision=True,
    body="**Hari Singh:** clever, cunning and a good judge of people, but at heart he wants to become **somebody**. His wish to learn to read and write grows stronger than his greed. He has a **conscience**: he cannot betray a man who trusts him.\n\n"
         "**Anil:** a young writer, **kind, simple and trusting**, careless with money ('fits and starts'). He teaches Hari without being asked to pay. He discovers the theft (the wet notes) but forgives silently and gives Hari wages and education instead of punishment.\n\n"
         "**Turning point:** at the station Hari realises that **education** is worth more than stolen money, and that Anil's **trust** is precious.\n\n"
         "**Theme:** **trust, kindness and education** can reform a person. A thief becomes honest not through fear of the police, but through being trusted and given a chance."),
  C.kc("s3.check", "Why did Hari return the money?",
    [("he valued Anil's trust and the chance to learn more than the money", ""), ("he was caught by the police", "No one caught him."), ("he missed the train by accident and was afraid", "He chose not to board."), ("the money was fake", "It was real money.")],
    "Education promised a better future.")
  ,C.kc("s3.check2", "How did Hari know that Anil had discovered the theft?",
    [("the fifty-rupee note was still wet from the rain", ""), ("Anil scolded him", "Anil said nothing."), ("the police came", "No police came."), ("Anil counted the money in front of him", "He noticed the wet notes.")],
    "Anil chose to forgive silently.")
 ]},
 {"id": "s4", "title": "Language of the story", "blocks": [
  blk("s4.thm", "theory", title="Words and expressions to know", revision=True,
    body="| Word or phrase | Meaning |\n|---|---|\n| **a fairly successful hand** | quite skilled (here, at stealing) |\n| **by fits and starts** | irregularly, now and then |\n"
         "| **to be one step ahead of** | to keep away from (the police, former employers) |\n| **maidan** | an open ground in a town |\n| **a big man** | a respected, successful person |\n"
         "| **ingratiating smile** | a smile meant to win favour |\n\n**Style:** first-person narration by the thief; we see his clever thinking and slowly changing feelings."),
  C.kc("s4.check", "'Anil made money by fits and starts' means he:",
    [("earned money irregularly", ""), ("earned money by fighting", "Irregularly."), ("was very rich", "His income was irregular."), ("never earned money", "Irregularly.")],
    "He borrowed one week and lent the next.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Hari 15 (thief) + Anil 25 (writer); met at a wrestling match.**\n- **Deal: cook for food → learns cooking, writing his name, sentences and figures promised.**\n"
         "- **Theft: ₹600 under the mattress → Lucknow Express → does not board → returns damp notes.**\n- **Morning: ₹50 note, wet notes, 'We'll start writing sentences today.'**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying Hari boarded the train: he **let it go**.\n2. Saying Anil handed Hari to the police: he **forgave silently**.\n"
         "3. Mixing up who is the narrator: 'I' is **Hari Singh**, the thief.\n4. Thinking Hari returned out of fear: he returned for **trust and education**."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Freeze the story at the platform: students write Hari's thoughts in two columns, 'Reasons to go' and 'Reasons to return', then discuss which side wins and why."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Has someone's trust ever made you want to behave better? What happened?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **The Midnight Visitor:** another story with a surprise in the end.\n- **A Question of Trust:** a thief who is himself tricked.\n- **Nelson Mandela:** how people can change for the better."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="How does Anil's trust change Hari Singh? Answer in about 120 words.\n\n"
         "**Model answer:** Hari Singh is a fifteen-year-old thief who befriends Anil only to rob him. Anil, a simple and trusting young writer, gives him food, teaches him to cook and to write his name, and promises to teach him sentences and figures. When Anil leaves six hundred rupees under his mattress, Hari steals it and goes to catch the Lucknow Express. But on the platform he imagines Anil's sad face at the loss of trust, and realises that education will make him 'a big man' far more than stolen money. He returns and replaces the notes. The next morning Anil gives him fifty rupees with the notes still wet, showing he knows and forgives. Trust, not punishment, turns the thief towards honesty."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Hari Singh, a 15-year-old thief, gets work with Anil, a 25-year-old writer, in return for food.\n- Anil teaches him to cook and write, and promises more lessons.\n"
         "- Hari steals Anil's ₹600 and goes to catch a train, but cannot leave.\n- Valuing trust and education, he returns the money.\n"
         "- Anil gives him ₹50 with the wet notes, silently forgiving him, and starts teaching him sentences."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- Write 3-mark answers in 40-50 words and 6-mark answers in 100-120 words.\n- For 'Why did Hari return?', give two reasons: trust and education.\n"
         "- Use the clue of the wet notes to show that Anil knew."),
  blk("s5.flash1", "flashcard", front="How did Hari know Anil had found out?", back="The fifty-rupee note Anil gave him was still wet from the rain."),
  blk("s5.flash2", "flashcard", front="What did Anil teach Hari?", back="To cook, to write his name, and he promised to teach whole sentences and figures."),
  blk("s5.flash3", "flashcard", front="How much did Hari steal?", back="Six hundred rupees, hidden under Anil's mattress."),
  blk("s5.flash4", "flashcard", front="Why did Hari not board the train?", back="He valued Anil's trust and realised education would make him a big man."),
 ]},
]

# ---------------- NCERT: Read and Find Out ----------------
C.vsa("rf1", CHARS, "Who does 'I' refer to in this story?", ["'I' refers to Hari Singh, the narrator.", "He is a fifteen-year-old thief."], RF(1))
C.vsa("rf2", MEET, "What is he 'a fairly successful hand' at?", ["He is a fairly successful hand at stealing.", "He is an experienced thief."], RF(2))
C.sa("rf3", MEET, "What does he get from Anil in return for his work?", ["He gets food, a place to stay and later some wages.", "He also learns to cook, to write his name, and is promised lessons in writing sentences and adding figures."], RF(3))
C.sa("rf4", THEFT, "How does the thief think Anil will react to the theft?", ["He thinks Anil will show only a touch of sadness.", "Anil will be sad not for the money but for the loss of trust."], RF(4))
C.sa("rf5", THEFT, "What does he say about the different reactions of people when they are robbed?", ["A greedy man shows fear and a rich man shows anger.", "A poor man shows acceptance; a trusting man like Anil would show only sadness."], RF(5))
C.sa("rf6", CHANGE, "Does Hari Singh return to Anil? Why?", ["Yes, he returns and puts the money back.", "He realises that education and Anil's trust are worth more than the stolen money."], RF(6))

# ---------------- NCERT: Think about It ----------------
C.la("ta1", CHANGE, "What are Hari Singh's reactions to the prospect of receiving an education? Do they change over time? What makes the difference?",
     ["At first Hari values education only as a way to make Anil trust him and to earn more.", "He agrees to learn to cook and write mainly to stay with Anil, whom he plans to rob.",
      "At the station he realises that being able to write whole sentences could make him a 'big man'.", "He sees education as worth more than a few hundred rupees.",
      "Anil's trust and kindness make the difference, and he returns to learn."], TA(1))
C.sa("ta2", CHARS, "Why does Anil not hand the thief over to the police? Do you think most people would have done so? In what ways is Anil different from such employers?",
     ["Anil is kind and trusting; he sees that Hari has returned the money and wants to change.", "Most employers would have punished him; Anil instead pays him and continues teaching him."], TA(2))
C.la("ta3", CHARS, "Do you think people like Anil and Hari Singh are found only in fiction, or are there such people in real life?",
     ["People like Hari exist: poor children often turn to petty crime for survival.", "People like Anil also exist: teachers and kind employers who help others.",
      "Real life has examples of people reformed by trust and education.", "Such stories inspire us to give others a second chance.",
      "So Anil and Hari, though fictional, reflect real people."], TA(3))

# ---------------- Objective practice ----------------
C.m("mcq01", MEET, "How old was Hari Singh?", [("fifteen", ""), ("twenty-five", "That is Anil."), ("ten", "Fifteen."), ("eighteen", "Fifteen.")], "He was already an experienced thief.")
C.m("mcq02", MEET, "Where did Hari first see Anil?", [("at a wrestling match", ""), ("at the railway station", "At a wrestling match."), ("in a market", "At a wrestling match."), ("at school", "At a wrestling match.")], "He decided Anil was easy-going.")
C.m("mcq03", MEET, "Why did Hari change his name every month?", [("to stay ahead of the police and former employers", ""), ("for fun", "To avoid being caught."), ("because Anil asked", "To avoid being caught."), ("for a new job", "To avoid being caught.")], "He was a thief.")
C.m("mcq04", MEET, "What happened to Hari's first meal for Anil?", [("Anil gave it to a stray dog", ""), ("Anil loved it", "It was terrible."), ("Hari ate it himself", "It went to a dog."), ("it was sold", "It went to a dog.")], "Then Anil taught him to cook.")
C.m("mcq05", MEET, "How did Anil earn money?", [("by writing for magazines, by fits and starts", ""), ("by wrestling", "By writing."), ("as a shopkeeper", "By writing."), ("as a teacher in a school", "By writing.")], "His income was irregular.")
C.m("mcq06", THEFT, "Where did Anil keep the money?", [("under his mattress", ""), ("in a bank", "Under the mattress."), ("in a locked box", "Under the mattress."), ("in his pocket", "Under the mattress.")], "Hari took it at night.")
C.m("mcq07", THEFT, "How much money did Hari steal?", [("six hundred rupees", ""), ("fifty rupees", "That is what Anil gave him later."), ("one rupee", "His daily profit on shopping."), ("one thousand rupees", "Six hundred.")], "Anil had got it from a publisher.")
C.m("mcq08", THEFT, "Which train did Hari plan to take?", [("the Lucknow Express", ""), ("the Delhi Mail", "The Lucknow Express."), ("a goods train", "The Lucknow Express."), ("the Bombay train", "The Lucknow Express.")], "But he let it go.")
C.m("mcq09", CHANGE, "What made Hari return?", [("the value of Anil's trust and education", ""), ("fear of the police", "He was not caught."), ("he had no money for a ticket", "He had ₹600."), ("the rain", "Trust and education.")], "He wanted to be a 'big man'.")
C.m("mcq10", CHANGE, "What did Anil give Hari the next morning?", [("a fifty-rupee note", ""), ("a scolding", "He said nothing about the theft."), ("a train ticket", "Fifty rupees."), ("a new book", "Fifty rupees.")], "The note was still wet.")
C.m("mcq11", CHARS, "Anil can best be described as:", [("kind and trusting", ""), ("cruel", "Kind."), ("greedy", "Kind."), ("suspicious", "Trusting.")], "He forgave Hari silently.")
C.m("mcq12", THEFT, "According to Hari, a rich man who is robbed shows:", [("anger", ""), ("fear", "That is the greedy man."), ("acceptance", "That is the poor man."), ("sadness", "That would be Anil.")], "Hari has watched many victims.")
C.m("mcq13", CHANGE, "Where did Hari sit after leaving the station?", [("in the maidan, in the rain", ""), ("in a hotel", "In the maidan."), ("on the train", "He did not board."), ("in a temple", "In the maidan.")], "The notes got damp.")
C.m("mcq14", CHANGE, "What did Anil say at the end?", [("'We'll start writing sentences today.'", ""), ("'Go to the police.'", "He forgave."), ("'Leave my house.'", "He forgave."), ("'Where is my money?'", "He said nothing about it.")], "Education continues.")
C.m("mcq15", MEET, "Hari's profit on the shopping was about:", [("a rupee a day", ""), ("ten rupees a day", "About a rupee."), ("nothing", "About a rupee."), ("a hundred rupees", "About a rupee.")], "Anil never checked.")
C.m("mcq16", CHARS, "The theme of the story is:", [("trust and education can reform a person", ""), ("crime always pays", "Trust reforms."), ("writers are rich", "Trust reforms."), ("trains are dangerous", "Trust reforms.")], "Hari chooses honesty.")
C.tf("tf1", THEFT, "Hari boarded the Lucknow Express.", False, "He let the train leave without him.")
C.tf("tf2", CHANGE, "Anil reported the theft to the police.", False, "He forgave Hari silently.")
C.tf("tf3", MEET, "Anil taught Hari to write his name.", True, "He also promised sentences and figures.")
C.tf("tf4", CHANGE, "The notes Anil gave Hari were wet.", True, "This showed Anil knew about the theft.")
C.tf("tf5", MEET, "Anil was an older, rich businessman.", False, "He was a young writer of about twenty-five, with irregular income.")
C.tf("tf6", CHARS, "The story is narrated by Anil.", False, "It is narrated by Hari Singh, the thief.")

# ---------------- More short and long answers ----------------
C.vsa("vsa1", MEET, "Give two things Anil taught Hari.", ["To cook.", "To write his name (and he promised sentences and figures)."])
C.vsa("vsa2", CHANGE, "Give two reasons why Hari returned the money.", ["He valued Anil's trust.", "He wanted to be educated and become a 'big man'."])
C.sa("sa1", MEET, "How did Hari get the job with Anil?",
     ["He met Anil at a wrestling match, flattered him with an ingratiating smile, and asked for work.", "Anil said he could not pay, but would feed him if he could cook, so Hari agreed."])
C.sa("sa2", THEFT, "Describe Hari's thoughts on the railway platform.",
     ["He imagined Anil's sad face at the loss of trust.", "He realised he would lose the chance of education, which could make him a big man, so he let the train go."])
C.sa("sa3", CHARS, "What shows that Anil was careless about money?",
     ["He made money by fits and starts and borrowed one week, lent the next.", "He kept six hundred rupees under his mattress and never checked Hari's shopping profit."])
C.sa("sa4", CHANGE, "Why did Anil not mention the theft?",
     ["He saw that Hari had returned the money and wanted to change.", "By forgiving silently, he kept Hari's dignity and trust alive."])
C.vsa("vsa3", THEFT, "Why did Hari think Anil would be easy to rob?", ["Anil was simple and trusting.", "He was careless with money and never checked accounts."])
C.sa("sa5", CHANGE, "'I would be a big man.' What did Hari mean, and how did he hope to become one?",
     ["He meant a respected, successful person, not a thief.", "He hoped to become one through education: learning to write whole sentences and add figures."])
C.la("la1", CHARS, "Write a character sketch of Hari Singh.",
     ["Hari Singh is a fifteen-year-old thief, clever and cunning, who changes his name to escape the police.", "He is a good judge of people: he chooses Anil because he is simple and trusting.",
      "He wants to be somebody, and slowly values learning to read and write.", "He has a conscience: he cannot bear to betray Anil's trust.",
      "Returning the money shows that he can change; he chooses education and honesty over theft."])
C.la("la2", CHARS, "Compare Anil and Hari Singh.",
     ["Anil is a young writer, kind, simple and trusting; Hari is a young thief, cunning and calculating.", "Anil is careless with money; Hari watches money closely and steals it.",
      "Anil offers education freely; Hari at first values it only for gain.", "Anil forgives silently; Hari learns from his kindness and returns the money.",
      "Together they show that trust can bring out the best in a person."])
C.la("la3", CHANGE, "Imagine you are Hari Singh. Write a diary entry on the night you returned the money.",
     ["Date and first person; describe stealing the ₹600 and running to the station.", "Your thoughts as the Lucknow Express left: Anil's trust, the lessons, becoming a 'big man'.",
      "Sitting in the rain at the maidan and deciding to return.", "Putting the damp notes back, and your hope for a new, honest life."])

chapter = header("ch02", 21, "The Thief's Story", "Ruskin Bond", "prose",
                 ["hari_meets_anil", "the_theft", "the_change_of_heart", "characters"],
                 "CBSE 2025-26 English Language and Literature (184): Footprints without Feet, Chapter 2. Assessed through short answers in 40-50 words (3 marks) and a long answer in 100-120 words (6 marks); no extracts from this book.",
                 book="footprints")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
