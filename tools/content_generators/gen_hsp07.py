"""CBSE Class 10 Hindi Course B, Sparsh Part 2, Ch 7: बड़े भाई साहब (Premchand, d. 1936; public domain).
The lesson retells the story; passages for extract questions are Shine retellings in Hindi."""
import sys
from hindi_common import make, header, path, ex, PROSE_INTRO
from lit_common import closing

ROOT = sys.argv[1]
PATH = path("sparsh", "ch07_bade_bhai_sahab")
C = make("hsp10ch07")
blk = C.blk
ELDER, YOUNGER, EDU, BOND = ["elder_brother_character"], ["younger_brother_play"], ["education_satire"], ["experience_and_care"]
MO = lambda n: ex(n, "मौखिक")
LI = lambda n: ex(n, "लिखित (ख)")
LG = lambda n: ex(n, "लिखित (ग)")
BH = lambda n: ex(n, "भाव स्पष्ट कीजिए")

STORY = ("| Part of the story | What happens |\n|---|---|\n"
         "| **Two brothers** | The narrator's elder brother is **five years older but only three classes ahead**. They live in a hostel. The elder studies all the time, by rote; the younger loves games. |\n"
         "| **'कहाँ थे?'** | Whenever the younger brother comes back from playing, the elder asks the same first question, **'Where were you?'**, and then gives a long lecture on how hard studies are. |\n"
         "| **The time-table** | Scared, the younger brother makes a strict time-table, but he cannot follow it: green fields, fresh air and games like **गुल्ली-डंडा** pull him outside. |\n"
         "| **First result** | The younger brother **passes first in class**; the elder **fails**. The elder still lectures him not to be proud. |\n"
         "| **Second result** | Again the younger passes first and the elder fails; now there is **only one class** between them. The elder becomes softer, and the younger **takes advantage**, playing and flying kites more. |\n"
         "| **The elder's speech** | Catching him with kites, the elder says **experience matters more than books**: parents and the headmaster's old mother manage life better than degree-holders. He suppresses his own wishes to set an example and protect his brother. |\n"
         "| **The kite** | A cut kite floats past. The tall elder brother **jumps, catches its string and runs to the hostel**, with the younger running behind. The child inside him shows; the younger brother's respect grows. |")

sections = [
 {"id": "s1", "title": "Two brothers, two ways of studying", "blocks": [
  blk("s1.hook", "hook", title="Does more study always mean better marks?",
    body="One brother studies from morning to night and still fails. The other plays all day and comes first. Who is right?\n\n"
         "In **'बड़े भाई साहब'**, **Premchand** tells this funny and touching story. Behind the laughter he questions rote learning, and shows the love and responsibility of an elder brother."),
  blk("s1.inspiration", "inspiration", title="The writer", person="Premchand", years="1880–1936",
    body="**Premchand** (real name **Dhanpat Rai Srivastava**) was born in **Lamhi**, near **Varanasi**. He is called **'उपन्यास सम्राट'** (emperor of novels). He wrote about villagers, the poor, women and everyday family life in simple, lively Hindi-Urdu.\n\n"
         "His novels include **गोदान**, **गबन**, **निर्मला**, **सेवासदन** and **कर्मभूमि**; about 300 stories are collected in **मानसरोवर** (eight volumes), including **ईदगाह**, **पूस की रात** and **नमक का दारोगा**.",
    future="Premchand's stories are still read, filmed and staged because his characters feel like real people."),
  C.socratic("s1.socratic", "Why does the elder brother lecture the younger one so often?",
    ["He feels responsible for his younger brother's future", "He wants to show off", "He dislikes his brother"], 0,
    "He sees himself as the guardian.")
 ]},
 {"id": "s2", "title": "The story", "blocks": [
  blk("s2.note", "theory", title="How to read this chapter",
    body="Read the full story in your **NCERT Sparsh Part 2** textbook. The table below retells it in order; passages in the questions are Shine retellings in Hindi."),
  blk("s2.table", "markdown_table", title="The story in order", revision=True, body=STORY),
  C.kc("s2.check", "What was the elder brother's first question every time?",
    [("'कहाँ थे?' (Where were you?)", ""), ("'खाना खाया?'", "He asked where he had been."), ("'पढ़ाई हुई?'", "'Where were you?'"), ("'कौन जीता?'", "'Where were you?'")],
    "Then came the lecture.")
  ,C.kc("s2.check2", "What happened after the second result?",
    [("only one class was left between the brothers", ""), ("both failed", "The younger passed."), ("the elder came first", "The younger came first."), ("they left the hostel", "Only one class was left.")],
    "The elder failed again.")
 ]},
 {"id": "s3", "title": "Characters and message", "blocks": [
  blk("s3.thm", "theory", title="What the story shows", revision=True,
    body="**The elder brother:** serious, hard-working but learns by **rote (रटंत)**; strict and full of lectures; but also **caring and responsible**. He suppresses his own wish to play and fly kites so that he can set an example.\n\n"
         "**The younger brother:** playful and clever; he passes easily. At first he fears his brother; later he takes advantage of his soft behaviour; at the end he feels **respect (श्रद्धा)** when he understands his brother's sacrifice.\n\n"
         "**Satire on education:** Premchand mocks **rote learning**, **exam-centred** study, memorising kings' names and dates, and long **essays** written to fill pages. Passing exams is not real education; **'असल चीज़ है बुद्धि का विकास'**.\n\n"
         "**Experience vs bookish knowledge:** the elder says **life's experience** teaches more than books; parents without degrees run the house better.\n\n"
         "**The child inside:** when he catches the kite, the elder shows he is still a boy; his strictness came from duty, not from lack of feeling."),
  C.kc("s3.check", "According to the elder brother, what matters more than books?",
    [("experience of life", ""), ("good handwriting", "Experience."), ("money", "Experience."), ("games", "Experience.")],
    "Parents without degrees run life better.")
  ,C.kc("s3.check2", "Why did the elder brother suppress his wish to fly kites?",
    [("to set an example and protect his younger brother", ""), ("he did not like kites", "He did like them."), ("he was ill", "To set an example."), ("the warden stopped him", "His own sense of duty.")],
    "'खुद बेराह चलूँ तो तुम्हारी रक्षा कैसे करूँ?'")
 ]},
 {"id": "s4", "title": "Language and style", "blocks": [
  blk("s4.thm", "theory", title="Language and style", revision=True,
    body="| Feature | Example / note |\n|---|---|\n| **Narration** | **first person** (the younger brother tells the story) |\n"
         "| **Language** | simple **Hindi-Urdu** (*अव्वल, इम्तिहान, तालीम, फ़ज़ीहत, दरजा*) with English school words (*टाइम-टेबिल, जामेट्री, अलजबरा*) |\n"
         "| **Humour and satire (व्यंग्य)** | the elder's lectures on exams and essays make us laugh but also think |\n| **मुहावरे (idioms)** | *आँखें खुलना, हँसी-खेल नहीं, सिर पर नंगी तलवार लटकना, दाँतों पसीना आना* |\n"
         "| **Character drawing** | strict on the outside, loving inside |\n\n"
         "**Type:** **कहानी** (short story)."),
  C.kc("s4.check", "Who narrates the story?",
    [("the younger brother", ""), ("the elder brother", "The younger."), ("the writer as an outsider", "The younger brother, in first person."), ("their father", "The younger.")],
    "First-person narration.")
 ]},
 closing(C,
   "- **5 साल बड़े, 3 दरजे आगे → दो बार फेल → 1 दरजे का अंतर.**\n- **'कहाँ थे?' → lecture; टाइम-टेबिल टूटा; गुल्ली-डंडा, कनकौए.**\n- **End: elder catches the kite; अनुभव > किताबी ज्ञान; बुद्धि का विकास.**",
   "1. Writing that the elder brother passed: he **failed twice**.\n2. Calling the elder brother cruel: he is **strict but caring**.\n"
   "3. Missing the satire: Premchand mocks **rote learning and exam-centred education**.\n4. Writing exam answers in English: answer in **Hindi**.",
   "Role-play: one student is the elder brother giving the 'कहाँ थे?' lecture; another is the younger brother. Then discuss: who learns better?",
   "Do you study by understanding or by rote? Which does the story favour, and do you agree?",
   "- **Moral education:** family responsibility.\n- **NEP 2020:** focus on understanding and skills, not rote learning.",
   "Is the elder brother only a strict, failing student, or something more? Answer in about 60 words.",
   "The elder brother is not only strict and unsuccessful in exams. He studies very hard, though by rote, and lectures his brother because he feels responsible for him. He gives up his own wish to play and fly kites to set an example. He values experience over bookish knowledge. When he catches the kite, we see the child inside him. He is a loving guardian, which is why the younger brother respects him.",
   "- Premchand's story of two brothers: the elder studies by rote and fails; the younger plays and comes first.\n- The elder lectures ('कहाँ थे?'), but after failing twice he becomes softer and the younger takes advantage.\n"
   "- The elder explains that experience matters more than books and that he suppresses his wishes to set an example.\n- When he catches a kite, the younger sees the child in him and respects him; the story satirises rote learning.",
   "- Answer in Hindi, in 25-30 words for 2 marks.\n- Back your point with an event from the story.\n- For character questions give two qualities with examples.",
   [("How much older and how many classes ahead was the elder brother?", "Five years older, but only three classes ahead (he was in class 9)."),
    ("What does the story satirise?", "Rote learning and exam-centred education.")]),
]

# ---------------- NCERT मौखिक ----------------
C.two("mo1", YOUNGER, "What activities did the narrator enjoy?",
      ["The narrator enjoyed games such as गुल्ली-डंडा, throwing pebbles and flying paper butterflies.", "He also liked climbing walls, swinging on the gate and, later, flying kites."], MO(1))
C.two("mo2", ELDER, "What was the first question the elder brother always asked the younger one?",
      ["He always first asked, 'कहाँ थे?' (Where were you?).", "After that he began a long lecture on studies."], MO(2))
C.two("mo3", YOUNGER, "What change came in the younger brother's behaviour after passing the second time?",
      ["He became careless and overconfident, thinking he would pass anyway.", "He took advantage of his brother's soft behaviour and spent more time playing and flying kites."], MO(3))
C.two("mo4", ELDER, "How much older was the elder brother, and in which class did he study?",
      ["The elder brother was five years older than the younger brother.", "He studied in class nine (three classes ahead)."], MO(4))
C.two("mo5", ELDER, "What did the elder brother do to rest his mind?",
      ["He drew pictures of birds, dogs and cats in the margins of his books and notebooks.", "He also wrote a word or a sentence again and again, even meaningless lines."], MO(5))
# ---------------- NCERT लिखित (ख) ----------------
C.two("kh1", YOUNGER, "What did the younger brother think while making his study time-table, and why could he not follow it?",
      ["He planned to study from early morning till night, with fixed hours for every subject and no time for games.", "He could not follow it because green fields, fresh air and his friends' games pulled him outside."], LI(1))
C.two("kh2", ELDER, "One day, after playing गुल्ली-डंडा, the younger brother came before the elder. What was the elder's reaction?",
      ["The elder brother got angry and asked, 'कहाँ थे?'", "He scolded him and lectured that English and studies are not child's play, and that he was wasting their parents' hard-earned money."], LI(2))
C.two("kh3", BOND, "Why did the elder brother have to suppress his own wishes?",
      ["He was the elder brother and felt responsible for setting a good example.", "If he went astray himself, he could not guide and protect his younger brother."], LI(3))
C.two("kh4", ELDER, "What advice did the elder brother give the younger one, and why?",
      ["He advised him to study hard and not waste time in games.", "He wanted his brother's good and did not want their parents' hard-earned money wasted."], LI(4))
C.two("kh5", YOUNGER, "How did the younger brother take advantage of his elder brother's soft behaviour?",
      ["After the elder failed again, he became soft, so the younger stopped fearing him.", "He began to spend most of his time playing and flying kites and studied less."], LI(5))
# ---------------- NCERT लिखित (ग) ----------------
C.two("ga1", BOND, "If the younger brother had not been scolded, would he have come first in class? Give your view.",
      ["Probably not; the scolding kept some fear and discipline in him, so he studied a little.", "Without it he might have played all the time and fallen behind."], LG(1), "medium")
C.two("ga2", EDU, "Which methods of education has the writer satirised in this lesson? Do you agree with him?",
      ["He satirises rote learning, exam-centred study, memorising useless facts and long essays written to fill pages.", "Yes; education should develop understanding and intelligence, not only help pass exams."], LG(2), "medium")
C.two("ga3", BOND, "According to the elder brother, how does one gain an understanding of life?",
      ["Understanding of life comes from experience, not from books.", "Parents and elders without degrees understand and manage life better than educated people."], LG(3))
C.two("ga4", BOND, "Why did respect for the elder brother arise in the younger brother's mind?",
      ["He realised that his brother suppressed his own wishes for his sake.", "He understood that the scolding came from love and care, not from cruelty."], LG(4))
C.two("ga5", ELDER, "State the elder brother's natural qualities.",
      ["He was hard-working, serious, disciplined and responsible.", "He was caring and experienced, though strict on the outside, with a child still hidden inside him."], LG(5))
C.two("ga6", BOND, "Which did the elder brother consider more important, life's experience or bookish knowledge, and why?",
      ["He considered life's experience more important.", "Books give information, but experience teaches how to live and solve real problems."], LG(6))
C.two("ga7a", BOND, "Which parts of the lesson show that (a) the younger brother respects his elder brother and (b) the elder brother has good experience of life?",
      ["(a) The younger brother listens silently to every lecture and later feels deep respect.", "(b) The elder explains how parents and the headmaster's old mother run life better through experience."], LG(7), "medium")
C.two("ga7b", BOND, "Which parts of the lesson show that (c) there is a child inside the elder brother and (d) the elder brother wants his brother's good?",
      ["(c) He jumps up, catches the string of a cut kite and runs to the hostel.", "(d) He gives up his own wishes and keeps advising him so that he does not go astray."], LG(7), "medium")
# ---------------- NCERT भाव ----------------
C.two("bh1", EDU, "Explain the idea: 'इम्तिहान पास कर लेना कोई चीज़ नहीं, असल चीज़ है बुद्धि का विकास।'",
      ["Passing exams is not the real aim of education.", "The real aim is the development of intelligence and understanding."], BH(1))
C.two("bh2", YOUNGER, "Explain the idea: 'फिर भी जैसे मौत और विपत्ति के बीच भी आदमी मोह और माया के बंधन में जकड़ा रहता है, मैं फटकार और घुड़कियाँ खाकर भी खेल-कूद का तिरस्कार न कर सकता था।'",
      ["Just as a person stays attached to the world even in danger and death,", "the narrator could not give up games even after scolding and threats."], BH(2), "medium")
C.two("bh3", EDU, "Explain the idea: 'बुनियाद ही पुख्ता न हो, तो मकान कैसे पायेदार बने?'",
      ["If the foundation is weak, the building cannot be strong.", "Likewise, without a strong base in studies, higher learning cannot be firm."], BH(3))
C.two("bh4", YOUNGER, "Explain the idea about the kite: the narrator's eyes were on the sky and his mind on the slowly falling 'traveller of the sky'.",
      ["The narrator was so attracted to the cut kite that his whole attention was on it.", "The kite floating down slowly seemed like a soul leaving heaven to take a new birth."], BH(4), "medium")

# ---------------- Extracts (Shine retellings) ----------------
C.extract("ext1", ELDER + BOND, "बड़े भाई साहब छोटे भाई से पाँच साल बड़े थे, पर केवल तीन दरजे आगे थे। वे दिन-रात किताबें खोले बैठे रहते और हर पाठ रट डालते। छोटा भाई जब खेलकर लौटता, तो वे पहला सवाल यही पूछते—'कहाँ थे?' फिर उपदेश की लंबी झड़ी लग जाती।",
  [("How much older was the elder brother?", "Five years."), ("How many classes ahead was he?", "Three classes."),
   ("How did the elder brother study?", "By rote (रटकर), day and night."), ("What was his first question?", "'कहाँ थे?'"), ("What followed the question?", "A long lecture (उपदेश).")],
  intro=PROSE_INTRO)
C.extract("ext2", BOND, "एक दिन कटा हुआ कनकौआ हमारे ऊपर से गुज़रा। उसकी डोर नीचे लटक रही थी। बड़े भाई साहब लंबे थे; उन्होंने उछलकर डोर पकड़ ली और बेतहाशा होस्टल की ओर दौड़े। मैं उनके पीछे-पीछे दौड़ रहा था।",
  [("What passed overhead?", "A cut kite (कनकौआ)."), ("Why could the elder brother catch it?", "Because he was tall."),
   ("Where did he run?", "Towards the hostel."), ("What did the younger brother do?", "He ran behind him."), ("What does this event show about the elder brother?", "That a child still lived inside him.")],
  intro=PROSE_INTRO)

# ---------------- Objective practice ----------------
C.m("mcq01", ELDER, "The elder brother was older than the narrator by:", [("five years", ""), ("three years", "Five years."), ("two years", "Five years."), ("seven years", "Five years.")], "But only three classes ahead.")
C.m("mcq02", ELDER, "The elder brother studied mainly by:", [("rote learning", ""), ("understanding", "By rote."), ("group study", "By rote."), ("asking teachers", "By rote.")], "He memorised everything.")
C.m("mcq03", YOUNGER, "Which game is named in the story?", [("गुल्ली-डंडा", ""), ("cricket", "गुल्ली-डंडा."), ("kabaddi", "गुल्ली-डंडा."), ("chess", "गुल्ली-डंडा.")], "Later he flies kites too.")
C.m("mcq04", YOUNGER, "Why could the younger brother not follow his time-table?", [("games and nature pulled him outside", ""), ("he was ill", "Games attracted him."), ("his brother stopped him", "Games attracted him."), ("he had no books", "Games attracted him.")], "Green fields and fresh air.")
C.m("mcq05", YOUNGER, "In the first result, the younger brother:", [("came first", ""), ("failed", "He came first."), ("passed with low marks", "He came first."), ("did not appear", "He came first.")], "The elder failed.")
C.m("mcq06", ELDER, "How many times did the elder brother fail in the story?", [("twice", ""), ("once", "Twice."), ("never", "Twice."), ("four times", "Twice.")], "Then only one class was left between them.")
C.m("mcq07", BOND, "The elder brother says real education is:", [("the development of intelligence", ""), ("passing exams", "Not just that."), ("getting degrees", "Intelligence."), ("memorising books", "Intelligence.")], "'असल चीज़ है बुद्धि का विकास'.")
C.m("mcq08", BOND, "Whose example does the elder give to show experience is better than degrees?", [("their parents and the headmaster's old mother", ""), ("the warden", "Parents and the old mother."), ("their teacher", "Parents and the old mother."), ("a king", "Parents and the old mother.")], "They run homes well without degrees.")
C.m("mcq09", YOUNGER, "What did the younger brother start doing after the elder failed again?", [("flying kites and playing more", ""), ("studying harder", "He played more."), ("helping his brother", "He played more."), ("leaving school", "He played more.")], "He took advantage of the soft behaviour.")
C.m("mcq10", BOND, "At the end, the elder brother:", [("catches a kite's string and runs to the hostel", ""), ("tears the kite", "He catches it."), ("complains to the warden", "He catches it."), ("beats the younger brother", "He catches it.")], "The child inside shows.")
C.m("mcq11", EDU, "The story mainly satirises:", [("rote learning and exam-centred education", ""), ("sports", "Education methods."), ("hostel food", "Education methods."), ("teachers' salaries", "Education methods.")], "व्यंग्य.")
C.m("mcq12", EDU, "'अव्वल' means:", [("first", ""), ("last", "First."), ("absent", "First."), ("average", "First.")], "He came first in class.")
C.m("mcq13", BOND, "The younger brother finally feels towards the elder:", [("respect", ""), ("anger", "Respect."), ("pity", "Respect."), ("fear only", "Respect.")], "श्रद्धा.")
C.m("mcq14", EDU, "Premchand is called:", [("उपन्यास सम्राट", ""), ("राष्ट्रकवि", "That was Gupt."), ("प्रकृति का सुकुमार कवि", "That was Pant."), ("महाप्राण", "That was Nirala.")], "Emperor of novels.")
C.tf("tf1", ELDER, "The elder brother was a quick learner who always came first.", False, "He failed twice.")
C.tf("tf2", YOUNGER, "The younger brother made a time-table but could not follow it.", True, "Games pulled him outside.")
C.tf("tf3", BOND, "The elder brother suppressed his own wishes to set an example.", True, "For his brother's sake.")
C.tf("tf4", EDU, "Premchand praises rote learning in this story.", False, "He satirises it.")
C.tf("tf5", BOND, "The story ends with the elder brother catching a kite.", True, "He runs to the hostel.")
C.tf("tf6", EDU, "Premchand's real name was Dhanpat Rai Srivastava.", True, "Born in Lamhi.")

chapter = header("sparsh", "ch07", 7, "बड़े भाई साहब", "प्रेमचंद", "prose", ["elder_brother_character", "younger_brother_play", "education_satire", "experience_and_care"],
                 "CBSE 2025-26 Hindi Course B (085), Section C: Sparsh Part 2 prose. Assessed through extract-based MCQs (1 mark each) and short answers in 25-30 words (2 marks); answers are written in Hindi.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
