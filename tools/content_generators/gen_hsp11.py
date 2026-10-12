"""CBSE Class 10 Hindi Course B, Sparsh Part 2, Ch 11: पतझर में टूटी पत्तियाँ (Ravindra Kelekar): (I) गिन्नी का सोना, (II) झेन की देन.
The text is in copyright: the lesson retells it, and extract passages are Shine retellings in Hindi.
Skipped NCERT (ख) 3 (personal anecdote) and (ख) 5 (refers to 'गिरगिट', excluded from the 2025-26 syllabus)."""
import sys
from hindi_common import make, header, path, ex, PROSE_INTRO
from lit_common import closing

ROOT = sys.argv[1]
PATH = path("sparsh", "ch11_patjhar_mein_tooti_pattiyan")
C = make("hsp10ch11")
blk = C.blk
GOLD, GANDHI, ZEN, PRESENT = ["ideals_vs_practicality"], ["gandhi_leadership"], ["tea_ceremony"], ["live_in_present"]
MO = lambda n: ex(n, "मौखिक")
LK = lambda n: ex(n, "लिखित (क)")
LB = lambda n: ex(n, "लिखित (ख)")
AS = lambda n: ex(n, "आशय स्पष्ट कीजिए")

PARTS = ("| Part | Key points |\n|---|---|\n"
         "| **I. गिन्नी का सोना** | **Pure gold** is soft; **गिन्नी का सोना** has **copper** mixed in, which makes it stronger and shinier. In the same way, pure **ideals** are like pure gold, and **practicality** is like copper. |\n"
         "| **Practical idealists** | People who mix practicality into their ideals. Slowly, as practicality is praised, their ideals fall back and only practical cleverness remains. |\n"
         "| **Gandhiji** | Gandhiji understood practicality and its value, but he did the opposite: he **mixed gold into copper**, raising practical life to the level of ideals. So he could lead the nation with his ideals. |\n"
         "| **Who gives values** | **Eternal values** in society are the gift of **idealists**; mere practical people have only pulled society down. |\n"
         "| **II. झेन की देन** | In **Japan**, a friend told the writer that most people suffer from **mental illness** because life is too fast: people compete with America, do a month's work in a day, run instead of walk, chatter instead of talk. |\n"
         "| **The tea ceremony** | The friend took him to a **चा-नो-यू** (tea ceremony) in a small hut on a six-storey roof, with cardboard walls and **tatami** mats. They washed hands and feet at a clay pot outside. |\n"
         "| **The चाजीन** | The tea master bowed in welcome, lit the stove, set the kettle, wiped the cups and served tea; every movement was so graceful it felt like the notes of **राग जयजयवंती**. Only **three** people are allowed, for **peace**. |\n"
         "| **Living in the present** | Sipping slowly for about an hour and a half, the writer felt his racing mind slow down and stop. **Past and future are illusions (मिथ्या); only the present is true.** |")

sections = [
 {"id": "s1", "title": "Two short pieces, two big ideas", "blocks": [
  blk("s1.hook", "hook", title="Pure gold or strong gold?",
    body="A jeweller mixes a little copper into gold to make it strong. Should we mix a little 'practicality' into our ideals too? And if we keep adding copper, what happens to the gold?\n\n"
         "In the second piece the writer, in busy Japan, sits through a slow **tea ceremony** and discovers that **only the present moment is real**. These are two short essays from **Ravindra Kelekar**."),
  blk("s1.inspiration", "inspiration", title="The writer", person="Ravindra Kelekar", years="1925–2010",
    body="**Ravindra Kelekar** was born in the **Konkan** region and took part in the **Goa liberation movement**. A follower of **Gandhian** thought, he wrote mainly in **Konkani** and **Marathi**, and also in **Hindi** and **Gujarati**.\n\n"
         "He received the **Jnanpith Award** for his Konkani writing. His short reflective pieces, like these, carry deep thoughts in simple words.",
    future="His advice to slow down and live in the present is now practised as 'mindfulness' around the world."),
  C.socratic("s1.socratic", "Why is copper mixed into the gold of a गिन्नी (gold coin)?",
    ["To make it stronger and shinier", "To make it cheaper only", "To change its colour to red"], 0,
    "Pure gold is too soft.")
 ]},
 {"id": "s2", "title": "The two pieces in brief", "blocks": [
  blk("s2.note", "theory", title="How to read this chapter",
    body="Read both pieces in your **NCERT Sparsh Part 2** textbook. The table below sums them up; passages in the questions are Shine retellings in Hindi."),
  blk("s2.table", "markdown_table", title="Key points", revision=True, body=PARTS),
  C.kc("s2.check", "What did Gandhiji do with gold and copper (ideals and practicality)?",
    [("he mixed gold into copper, raising practical life", ""), ("he mixed copper into gold", "That is what practical idealists do."), ("he kept only pure gold", "He understood practicality."), ("he used only copper", "He kept ideals high.")],
    "He raised practicality to the level of ideals.")
  ,C.kc("s2.check2", "How many people are allowed in the tea ceremony?",
    [("three", ""), ("one", "Three."), ("ten", "Three."), ("as many as wish", "Three, for peace.")],
    "To keep peace and calm.")
 ]},
 {"id": "s3", "title": "Ideas in the chapter", "blocks": [
  blk("s3.thm", "theory", title="What the writer teaches", revision=True,
    body="**Ideals vs practicality:** practicality (copper) gives strength, but too much of it pushes ideals (gold) aside. Society's **eternal values** (truth, honesty, non-violence, compassion) come from **idealists**.\n\n"
         "**Gandhiji's way:** he did not lower his ideals for convenience; he lifted practical life up to his ideals. That is why millions followed him.\n\n"
         "**The disease of speed:** fast life, competition and pressure cause **mental illness**. 'Here no one walks, everyone runs; no one speaks, everyone chatters.'\n\n"
         "**Zen and the tea ceremony:** calm, slow, graceful action and silence bring peace of mind.\n\n"
         "**Live in the present:** the past is gone, the future has not come; both are **मिथ्या** (illusions). The present moment is the only truth, and it is endless when we live it fully."),
  C.kc("s3.check", "According to the writer, eternal values in society are given by:",
    [("idealists", ""), ("practical people", "They pulled society down."), ("rich people", "Idealists."), ("kings", "Idealists.")],
    "'समाज के पास शाश्वत मूल्यों जैसा जो कुछ है…'")
  ,C.kc("s3.check2", "Why did the friend say most Japanese are mentally ill?",
    [("because the pace of their life has become too fast", ""), ("because they drink too much tea", "Speed of life."), ("because they live in small houses", "Speed of life."), ("because of cold weather", "Speed of life.")],
    "They compete with America.")
 ]},
 {"id": "s4", "title": "Language and style", "blocks": [
  blk("s4.thm", "theory", title="Language and style", revision=True,
    body="| Feature | Example / note |\n|---|---|\n| **Type** | two short **reflective prose pieces (प्रसंग)** |\n"
         "| **Language** | simple Hindi with English and Japanese words (*प्रैक्टिकल आइडियलिस्ट, स्पीड, टी-सेरेमनी, चा-नो-यू, चाजीन*) |\n"
         "| **Comparison** | ideals = pure gold, practicality = copper |\n| **Music image** | the चाजीन's grace is like **राग जयजयवंती** |\n| **Tone** | thoughtful, calm |"),
  C.kc("s4.check", "What is 'चा-नो-यू'?",
    [("the Japanese tea ceremony", ""), ("a Japanese dance", "The tea ceremony."), ("a kind of gold coin", "The tea ceremony."), ("a Zen temple", "The tea ceremony.")],
    "Conducted by the चाजीन.")
 ]},
 closing(C,
   "- **गिन्नी का सोना: सोना = आदर्श, ताँबा = व्यावहारिकता; गांधीजी ताँबे में सोना मिलाते थे.**\n- **झेन की देन: जापान, मानसिक रोग (speed), चा-नो-यू, चाजीन, 3 लोग, जयजयवंती.**\n- **सत्य केवल वर्तमान है; भूत और भविष्य मिथ्या.**",
   "1. Saying Gandhiji mixed copper into gold: he mixed **gold into copper**.\n2. Saying practical people gave society its values: **idealists** did.\n"
   "3. Writing that the tea ceremony was in a palace: it was in a **small hut on a rooftop**.\n4. Writing exam answers in English: answer in **Hindi**.",
   "Run a two-minute 'tea ceremony' in class: everyone sits silently and drinks water slowly. Then discuss how they felt.",
   "When did you last do one thing slowly, with full attention? How did it feel?",
   "- **History:** Gandhiji and the freedom struggle.\n- **Health:** stress and mental health.",
   "Explain the difference between pure gold and गिन्नी का सोना, and what it teaches about ideals, in about 60 words.",
   "Pure gold has no mixture and is soft, while गिन्नी का सोना has copper added to make it strong and shiny. The writer compares pure ideals to gold and practicality to copper. A little practicality helps, but when people keep praising it, ideals fade away. Gandhiji instead mixed gold into copper and raised practical life. Society's eternal values come from idealists.",
   "- Part I: pure ideals are like pure gold; practicality is like copper; practical idealists slowly lose their ideals.\n- Gandhiji raised practical life to his ideals; eternal values come from idealists.\n"
   "- Part II: in Japan, fast life causes mental illness; a slow tea ceremony (चा-नो-यू) calmed the writer.\n- Only the present is true; past and future are illusions.",
   "- Answer in Hindi, in 25-30 words for 2 marks.\n- Name the part (गिन्नी का सोना / झेन की देन) you are answering from.\n- Use the gold-copper comparison correctly.",
   [("What did Gandhiji mix into what?", "He mixed gold (ideals) into copper (practicality), raising its value."),
    ("What is the main lesson of 'झेन की देन'?", "Slow down and live in the present; only the present is true.")]),
]

# ---------------- NCERT मौखिक ----------------
C.two("mo1", GOLD, "Why are pure gold and गिन्नी का सोना different?",
      ["Pure gold has no mixture.", "गिन्नी का सोना has copper mixed in, which makes it stronger and shinier."], MO(1))
C.two("mo2", GOLD, "Who are called 'practical idealists'?",
      ["People who mix practicality into their ideals are called practical idealists.", "They follow ideals but adjust them to practical needs."], MO(2))
C.two("mo3", GOLD, "In the context of the lesson, what is a pure ideal?",
      ["A pure ideal is an ideal followed without any compromise, like pure gold.", "Values such as truth, honesty and non-violence held firmly are pure ideals."], MO(3))
C.two("mo4", ZEN, "Why does the writer say an engine of 'speed' has been fitted in the minds of the Japanese?",
      ["The Japanese are competing with America and want to do a month's work in a day.", "So their minds keep racing all the time, as if driven by an engine."], MO(4))
C.two("mo5", ZEN, "What is the Japanese method of drinking tea called?",
      ["It is called 'चा-नो-यू'.", "In English it is known as the tea ceremony."], MO(5))
C.two("mo6", ZEN, "What is special about the place in Japan where tea is served?",
      ["It is a small hut on the roof of a six-storey building, with cardboard walls and tatami mats.", "It is quiet and calm; guests wash their hands and feet at a clay pot before entering."], MO(6))
# ---------------- NCERT लिखित (क) ----------------
C.two("lk1", GOLD, "Why is the pure ideal compared to gold and practicality to copper?",
      ["Pure ideals are precious and unmixed like pure gold.", "Practicality, like copper, adds strength but lowers purity and value when mixed in."], LK(1))
C.two("lk2", ZEN, "Which actions did the चाजीन complete gracefully?",
      ["He bowed and welcomed the guests, lit the stove and placed the kettle on it.", "He brought the utensils, wiped them with a cloth and poured the tea, all with great grace."], LK(2))
C.two("lk3", ZEN, "How many people were allowed in the tea ceremony, and why?",
      ["Only three people were allowed.", "This kept the place peaceful and calm, which is the aim of the ceremony."], LK(3))
C.two("lk4", PRESENT, "What change did the writer feel in himself after drinking the tea?",
      ["The speed of his mind slowed down and then seemed to stop.", "He felt he was living in endless time, only in the present."], LK(4))
# ---------------- NCERT लिखित (ख) ----------------
C.two("lb1", GANDHI, "Gandhiji had a wonderful ability to lead. Confirm this with an example.",
      ["Gandhiji led millions of people through truth and non-violence, as in the Salt March.", "He kept his ideals high and lifted practical life to them, so people followed him willingly."], LB(1), "medium")
C.two("lb2", GOLD, "In your view, which values are eternal? Explain their relevance today.",
      ["Truth, honesty, non-violence, compassion and duty are eternal values.", "Today, amid selfishness, violence and corruption, these values keep society humane and united."], LB(2), "medium")
C.two("lb4", GANDHI, "'Copper mixed into pure gold, or gold into copper': how does this show in Gandhiji's ideals and practice?",
      ["Gandhiji did not lower his ideals (mix copper into gold) for convenience.", "He mixed gold into copper: he raised practical life to the level of his ideals."], LB(4), "medium")
C.two("lb6", ZEN, "What reasons did the writer's friend give for mental illness? How far do you agree?",
      ["The friend said the pace of life has become too fast; people compete with America and try to do a month's work in a day.", "I largely agree; speed, competition and stress harm mental health today too."], LB(6), "medium")
C.two("lb7", PRESENT, "The writer says only the present is true and we should live in it. Why might he have said so?",
      ["The past has gone and the future has not come; both are illusions.", "Only by living fully in the present can we find peace and make the most of life."], LB(7), "medium")
# ---------------- NCERT आशय ----------------
C.two("as1", GOLD, "Explain the meaning: 'समाज के पास अगर शाश्वत मूल्यों जैसा कुछ है तो वह आदर्शवादी लोगों का ही दिया हुआ है।'",
      ["Whatever lasting values society has were given by idealists.", "Merely practical people have not given society such values."], AS(1))
C.two("as2", GOLD, "Explain the meaning: 'जब व्यावहारिकता का बखान होने लगता है तब प्रैक्टिकल आइडियलिस्टों के जीवन से आदर्श धीरे-धीरे पीछे हटने लगते हैं…'",
      ["When practicality is praised too much, practical idealists slowly drop their ideals.", "Only their practical cleverness remains in front."], AS(2), "medium")
C.two("as3", ZEN, "Explain the meaning: 'हमारे जीवन की रफ़्तार बढ़ गई है। यहाँ कोई चलता नहीं बल्कि दौड़ता है। कोई बोलता नहीं, बकता है…'",
      ["Life has become so fast that people run instead of walking and chatter instead of speaking.", "Even when alone, they keep muttering to themselves; this shows mental stress."], AS(3))
C.two("as4", ZEN, "Explain the meaning: 'सभी क्रियाएँ इतनी गरिमापूर्ण ढंग से कीं कि उसकी हर भंगिमा से लगता था मानो जयजयवंती के सुर गूँज रहे हों।'",
      ["The चाजीन did every action with great grace and dignity.", "His movements were so rhythmic that they felt like the notes of राग जयजयवंती."], AS(4))

# ---------------- Extracts (Shine retellings) ----------------
C.extract("ext1", GOLD + GANDHI, "शुद्ध सोने में ताँबा मिलाने से गिन्नी का सोना बनता है, जो अधिक मज़बूत और चमकीला होता है। इसी तरह कुछ लोग अपने आदर्शों में व्यावहारिकता मिला लेते हैं। गांधीजी ने उलटा किया—उन्होंने ताँबे में सोना मिलाकर व्यावहारिकता को आदर्शों की ऊँचाई तक उठाया।",
  [("What is mixed into pure gold to make गिन्नी का सोना?", "Copper."), ("What does copper do to the gold?", "It makes it stronger and shinier."),
   ("What do some people mix into their ideals?", "Practicality."), ("What did Gandhiji mix into copper?", "Gold (ideals)."), ("What was the result of Gandhiji's way?", "Practical life rose to the level of ideals.")],
  intro=PROSE_INTRO)
C.extract("ext2", ZEN + PRESENT, "छः मंज़िली इमारत की छत पर बनी छोटी-सी पर्णकुटी में चा-नो-यू हुआ। चाजीन ने झुककर स्वागत किया और बड़ी गरिमा से चाय बनाई। केवल तीन लोग थे; चारों ओर गहरी शांति थी। धीरे-धीरे चाय पीते हुए लेखक को लगा कि उसका दौड़ता मन रुक गया है और वह केवल वर्तमान में जी रहा है।",
  [("Where did the tea ceremony take place?", "In a small hut on the roof of a six-storey building."), ("Who made the tea?", "The चाजीन (tea master)."),
   ("How many people were present?", "Three."), ("What was the atmosphere like?", "Deeply peaceful."), ("What did the writer feel?", "His racing mind stopped and he lived only in the present.")],
  intro=PROSE_INTRO)

# ---------------- Objective practice ----------------
C.m("mcq01", GOLD, "In 'गिन्नी का सोना', gold stands for:", [("ideals", ""), ("practicality", "That is copper."), ("money", "Ideals."), ("power", "Ideals.")], "Pure and precious.")
C.m("mcq02", GOLD, "Copper stands for:", [("practicality", ""), ("ideals", "That is gold."), ("poverty", "Practicality."), ("anger", "Practicality.")], "It adds strength.")
C.m("mcq03", GANDHI, "Gandhiji:", [("mixed gold into copper", ""), ("mixed copper into gold", "That lowers ideals."), ("rejected practicality fully", "He understood it."), ("cared only for practicality", "He kept ideals high.")], "He raised practical life.")
C.m("mcq04", GOLD, "According to the writer, mere practical people have:", [("pulled society down", ""), ("given eternal values", "Idealists did that."), ("led the freedom struggle", "Not as practical people."), ("made society rich in values", "They pulled it down.")], "Idealists gave values.")
C.m("mcq05", ZEN, "The second part of the chapter is set in:", [("Japan", ""), ("China", "Japan."), ("America", "Japan."), ("Goa", "Japan.")], "With a Japanese friend.")
C.m("mcq06", ZEN, "The Japanese compete with:", [("America", ""), ("China", "America."), ("Russia", "America."), ("India", "America.")], "Hence the speed of life.")
C.m("mcq07", ZEN, "'चाजीन' is the:", [("tea master", ""), ("guest", "Tea master."), ("teapot", "Tea master."), ("hut", "Tea master.")], "He serves the tea.")
C.m("mcq08", ZEN, "The floor of the tea hut was covered with:", [("tatami (mats)", ""), ("marble", "Tatami."), ("carpet", "Tatami."), ("wood planks", "Tatami.")], "Walls of cardboard.")
C.m("mcq09", ZEN, "Before entering the hut, the guests:", [("washed their hands and feet", ""), ("bowed to a statue", "Washed hands and feet."), ("paid a fee", "Washed hands and feet."), ("removed their hats", "Washed hands and feet.")], "At a clay pot of water.")
C.m("mcq10", ZEN, "The चाजीन's graceful movements were compared to:", [("राग जयजयवंती", ""), ("a dance", "A raga."), ("a waterfall", "A raga."), ("a bird's flight", "A raga.")], "Like musical notes.")
C.m("mcq11", PRESENT, "According to the writer, the past and the future are:", [("illusions (मिथ्या)", ""), ("the only truth", "Only the present is true."), ("more important than the present", "The present matters."), ("equal to the present", "They are illusions.")], "Only the present is true.")
C.m("mcq12", ZEN, "About how long did they sip tea?", [("about an hour and a half", ""), ("five minutes", "About 1.5 hours."), ("a whole day", "About 1.5 hours."), ("ten minutes", "About 1.5 hours.")], "Very slowly.")
C.m("mcq13", GOLD, "Ravindra Kelekar wrote mainly in:", [("Konkani and Marathi", ""), ("Bengali", "Konkani and Marathi."), ("Tamil", "Konkani and Marathi."), ("Urdu", "Konkani and Marathi.")], "Also Hindi and Gujarati.")
C.m("mcq14", GOLD, "'शाश्वत' means:", [("eternal", ""), ("temporary", "Eternal."), ("modern", "Eternal."), ("foreign", "Eternal.")], "शाश्वत मूल्य = eternal values.")
C.tf("tf1", GOLD, "गिन्नी का सोना is purer than pure gold.", False, "It has copper mixed in.")
C.tf("tf2", GANDHI, "Gandhiji raised practical life to the level of his ideals.", True, "Gold into copper.")
C.tf("tf3", ZEN, "Ten people were allowed in the tea ceremony.", False, "Only three.")
C.tf("tf4", PRESENT, "After the tea, the writer felt his mind slow down.", True, "It seemed to stop.")
C.tf("tf5", ZEN, "The writer's friend said fast life causes mental illness.", True, "Competition with America.")
C.tf("tf6", PRESENT, "The writer says we should live mainly in the future.", False, "Only the present is true.")

chapter = header("sparsh", "ch11", 11, "पतझर में टूटी पत्तियाँ", "रवींद्र केलेकर", "prose", ["ideals_vs_practicality", "gandhi_leadership", "tea_ceremony", "live_in_present"],
                 "CBSE 2025-26 Hindi Course B (085), Section C: Sparsh Part 2 prose (गिन्नी का सोना, झेन की देन). Assessed through extract-based MCQs (1 mark each) and short answers in 25-30 words (2 marks); answers are written in Hindi. The text is in copyright: read it in the NCERT textbook.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
