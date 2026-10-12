"""CBSE Class 10 Hindi Course B, Sparsh Part 2, Ch 8: तताँरा-वामीरो कथा (Leeladhar Mandloi).
The text is in copyright: the lesson retells it, and extract passages are Shine retellings in Hindi."""
import sys
from hindi_common import make, header, path, ex, PROSE_INTRO
from lit_common import closing

ROOT = sys.argv[1]
PATH = path("sparsh", "ch08_tatara_vamiro_katha")
C = make("hsp10ch08")
blk = C.blk
TAT, VAM, CUSTOM, LEGEND = ["tataanra_character"], ["vamiro_love"], ["custom_and_sacrifice"], ["nicobar_legend"]
MO = lambda n: ex(n, "मौखिक")
LK = lambda n: ex(n, "लिखित (क)")
LB = lambda n: ex(n, "लिखित (ख)")
AS = lambda n: ex(n, "आशय स्पष्ट कीजिए")

STORY = ("| Part of the story | What happens |\n|---|---|\n"
         "| **The legend** | Long ago **Little Andaman** and **Car Nicobar** were one island. The Nicobarese believe a love story split them apart. |\n"
         "| **Tataanra** | A handsome, strong and kind young man of **Pasa** village. He always carried a **wooden sword**; people believed it had **magical power**. He helped everyone. |\n"
         "| **Vamiro** | A beautiful girl of **Lapati** village with a very sweet voice. One evening Tataanra hears her singing on the seashore. A big wave drenches her and she stops; he begs her to finish the song and tell her name. |\n"
         "| **The custom** | Vamiro answers coldly: by custom, marriage is allowed **only within one's own village**. Still both feel drawn to each other and keep meeting at the shore. |\n"
         "| **पशु-पर्व** | At the animal festival in Pasa, Vamiro comes to see Tataanra. Her **mother** sees them together, insults Tataanra, and villagers gather. Vamiro weeps. |\n"
         "| **The sword** | Helpless and angry, Tataanra **thrusts his sword into the earth** and drags it. The land **splits**; one part drifts away with him. He cries 'वामीरो!' and is lost. Vamiro, mad with grief, also disappears. |\n"
         "| **The change** | After their **sacrifice**, the Nicobarese began to **marry outside their village**; the harmful custom ended. |")

sections = [
 {"id": "s1", "title": "A love story that split an island", "blocks": [
  blk("s1.hook", "hook", title="Why are there two islands?",
    body="Look at a map of the Andaman and Nicobar Islands. **Little Andaman** and **Car Nicobar** are separated by sea. A folk tale says they were once one island, and that a young man's **sword** split them in two.\n\n"
         "This chapter retells that legend. It is a story of love, of a **custom (रूढ़ि)** that became a burden, and of a sacrifice that changed society."),
  blk("s1.inspiration", "inspiration", title="The writer", person="Leeladhar Mandloi", years="born 1954",
    body="**Leeladhar Mandloi** was born in **Chhindwara** district, **Madhya Pradesh**. He is a poet and prose writer who worked for many years in **broadcasting** and headed **Doordarshan**. Having lived in the Andaman and Nicobar Islands, he collected and retold their **folk tales**.\n\n"
         "This story comes from that tradition of Nicobari folklore.",
    future="Folk tales carry a community's memory; collecting them keeps that memory alive."),
  C.socratic("s1.socratic", "Why could Tataanra and Vamiro not marry?",
    ["By custom, marriage was allowed only within one's own village", "Their parents were enemies", "Tataanra was poor"], 0,
    "They were from different villages.")
 ]},
 {"id": "s2", "title": "The story", "blocks": [
  blk("s2.note", "theory", title="How to read this chapter",
    body="Read the full story in your **NCERT Sparsh Part 2** textbook. The table below retells it in order; passages in the questions are Shine retellings in Hindi."),
  blk("s2.table", "markdown_table", title="The story in order", revision=True, body=STORY),
  C.kc("s2.check", "What did people believe about Tataanra's wooden sword?",
    [("it had magical power", ""), ("it was made of gold", "It was wooden."), ("it belonged to a king", "Magical power."), ("it was useless", "Magical power.")],
    "He never parted with it.")
  ,C.kc("s2.check2", "Which two islands were once one, according to the legend?",
    [("Little Andaman and Car Nicobar", ""), ("Great Nicobar and Sri Lanka", "Little Andaman and Car Nicobar."), ("Andaman and Lakshadweep", "Little Andaman and Car Nicobar."), ("Port Blair and Havelock", "Little Andaman and Car Nicobar.")],
    "Split by Tataanra's sword.")
 ]},
 {"id": "s3", "title": "Characters and message", "blocks": [
  blk("s3.thm", "theory", title="What the story shows", revision=True,
    body="**Tataanra:** handsome, strong, kind and helpful; loved by the whole island. In love he becomes restless; insulted in public, he cannot bear it, and his anger splits the island.\n\n"
         "**Vamiro:** beautiful, with a sweet voice; at first cold because of custom, but sincere in love; she weeps when he is insulted and is lost in grief after him.\n\n"
         "**Custom as a burden:** the rule of marrying only within the village stood against true love. When customs become chains, **breaking them is good** for society.\n\n"
         "**Sacrifice brings change:** Tataanra and Vamiro lost their lives, but after them the Nicobarese started marrying outside their villages.\n\n"
         "**Nature:** the sunset sea, waves, cool breeze and birds returning home form a beautiful background to the love story.\n\n"
         "**Old festivals:** the **पशु-पर्व** had music, dance, food and shows of strength in which young men tested their power against animals."),
  C.kc("s3.check", "What change came in Nicobar after their death?",
    [("people began marrying outside their village", ""), ("the sword was worshipped", "The custom changed."), ("the festival stopped", "The custom changed."), ("the villages united into one", "The custom changed.")],
    "Their sacrifice ended the custom.")
  ,C.kc("s3.check2", "What was the 'पशु-पर्व'?",
    [("a festival with shows of strength, music and dance", ""), ("a market for selling animals", "A festival."), ("a hunting trip", "A festival."), ("a religious fast", "A festival.")],
    "Young men showed their strength.")
 ]},
 {"id": "s4", "title": "Language and style", "blocks": [
  blk("s4.thm", "theory", title="Language and style", revision=True,
    body="| Feature | Example / note |\n|---|---|\n| **Type** | **लोककथा** (folk tale) retold in literary Hindi |\n"
         "| **Language** | simple Hindi with **tatsam** words (*शमन, असंगत, याचना, विभक्त*) |\n| **Description** | rich nature pictures: sunset, waves, breeze, birds |\n"
         "| **मुहावरे (idioms)** | *आस की किरण, सुध-बुध खोना, आग बबूला होना* |\n| **Structure** | the legend frames the story: it begins and ends with the split island |"),
  C.kc("s4.check", "This chapter is best described as a:",
    [("folk tale", ""), ("poem", "Folk tale."), ("diary", "Folk tale."), ("play", "Folk tale.")],
    "From Nicobari folklore.")
 ]},
 closing(C,
   "- **Tataanra (Pasa, wooden sword) + Vamiro (Lapati, sweet song).**\n- **Custom: marry only in your own village → insult at पशु-पर्व → sword splits the island.**\n- **Result: Little Andaman and Car Nicobar; custom ends.**",
   "1. Swapping villages: Tataanra is from **Pasa**, Vamiro from **Lapati**.\n2. Writing the sword was metal: it was **wooden**.\n"
   "3. Missing the message: harmful **customs should be broken**.\n4. Writing exam answers in English: answer in **Hindi**.",
   "Show Little Andaman and Car Nicobar on a map, then ask students to retell the legend in five sentences.",
   "Is there any custom around you that has become a burden? How could it change without anyone getting hurt?",
   "- **Geography:** the Andaman and Nicobar Islands.\n- **Civics:** social reform and changing customs.",
   "'When customs become chains, breaking them is good.' Explain with reference to the story in about 60 words.",
   "In Nicobar, custom allowed marriage only within one's own village. Because of this rule, Tataanra and Vamiro could not marry, though they loved each other truly. Vamiro's mother insulted Tataanra, and in the end both lost their lives. After their sacrifice, people began to marry outside their village. The story shows that a custom which blocks love and humanity becomes a burden and should be broken.",
   "- A Nicobari folk tale explains how Little Andaman and Car Nicobar separated.\n- Tataanra of Pasa and Vamiro of Lapati fell in love, but custom allowed marriage only within the village.\n"
   "- Insulted at the पशु-पर्व, Tataanra drove his wooden sword into the earth and split the island; both were lost.\n- Their sacrifice ended the custom; people began marrying outside their villages.",
   "- Answer in Hindi, in 25-30 words for 2 marks.\n- Name the villages and the custom correctly.\n- For 'message' questions, link the custom to the sacrifice and the change.",
   [("Which villages did Tataanra and Vamiro belong to?", "Tataanra to Pasa; Vamiro to Lapati."),
    ("What did Tataanra do in anger?", "He drove his wooden sword into the earth and dragged it, splitting the island.")]),
]

# ---------------- NCERT मौखिक ----------------
C.two("mo1", LEGEND, "Where is the story of Tataanra-Vamiro from?",
      ["It is a folk tale of the Andaman and Nicobar Islands.", "It explains how Little Andaman and Car Nicobar became separate."], MO(1))
C.two("mo2", VAM, "Why did Vamiro forget her song?",
      ["While she was singing by the sea, a high wave suddenly drenched her.", "Startled, she stopped and forgot her song; then she saw Tataanra watching her."], MO(2))
C.two("mo3", TAT, "What did Tataanra plead with Vamiro for?",
      ["He begged her to complete her sweet song and tell him her name.", "He also asked her to come to the shore again the next day."], MO(3))
C.two("mo4", CUSTOM, "What was the custom of Tataanra's and Vamiro's villages?",
      ["Marriage was allowed only between a young man and woman of the same village.", "So a youth of one village could not marry a girl of another."], MO(4))
C.two("mo5", TAT, "What did Tataanra do in anger?",
      ["He thrust his wooden sword into the earth with all his strength.", "He dragged it, and the land split into two parts."], MO(5))
# ---------------- NCERT लिखित (क) ----------------
C.two("lk1", TAT, "What did people think about Tataanra's sword?",
      ["Though it was wooden, people believed it had magical, divine power.", "He always kept it with him and never used it before others."], LK(1))
C.two("lk2", VAM, "What curt reply did Vamiro give Tataanra?",
      ["She asked who he was and why he was staring at her and asking such an odd question.", "She said she was not bound to answer a young man of another village."], LK(2))
C.two("lk3", CUSTOM, "What change came in Nicobar after the sacrificial death of Tataanra and Vamiro?",
      ["After their death, the Nicobarese gave up the custom of marrying only within the village.", "People began to marry youths of other villages too."], LK(3))
C.two("lk4", TAT, "Why did the people of Nicobar like Tataanra?",
      ["He was handsome, strong, kind and very helpful.", "He was always ready to help anyone in trouble, so the whole island loved him."], LK(4))
# ---------------- NCERT लिखित (ख) ----------------
C.two("lb1", LEGEND, "What do the Nicobarese believe about the division of the Nicobar islands?",
      ["They believe Little Andaman and Car Nicobar were once one island.", "Tataanra's sword split the land in anger, separating them."], LB(1))
C.two("lb2", TAT, "Where did Tataanra go after a day of hard work? Describe the natural beauty there in your own words.",
      ["He went to the seashore at sunset to rest.", "The setting sun coloured the sky and sea, a cool breeze blew, waves played and birds returned home."], LB(2), "medium")
C.two("lb3", TAT, "What change came in Tataanra's life after meeting Vamiro?",
      ["He became restless and lost in thoughts of Vamiro.", "He waited for her at the shore every evening; each moment seemed very long."], LB(3))
C.two("lb4", CUSTOM, "What kind of events were held in ancient times for entertainment and display of strength?",
      ["Festivals like the पशु-पर्व were held, with music, dance and feasts.", "Young men showed their strength by fighting strong animals."], LB(4))
C.two("lb5", CUSTOM, "'When customs become chains and burdens, it is good that they break.' Why? Explain.",
      ["Customs that stop love, freedom and humanity cause suffering, as with Tataanra and Vamiro.", "Breaking such customs brings progress and happiness, as Nicobar changed after their sacrifice."], LB(5), "medium")
# ---------------- NCERT आशय ----------------
C.two("as1", TAT, "Explain the meaning: 'जब कोई राह न सूझी तो क्रोध का शमन करने के लिए उसमें शक्ति भर उसे धरती में घोंप दिया और ताकत से उसे खींचने लगा।'",
      ["Insulted and helpless, Tataanra found no way out.", "To calm his anger he drove his sword into the earth with full strength and dragged it."], AS(1))
C.two("as2", VAM, "Explain the meaning: 'बस आस की एक किरण थी जो समुद्र की देह पर डूबती किरणों की तरह कभी भी डूब सकती थी।'",
      ["Tataanra had only a small hope that Vamiro would come.", "That hope was as weak as the last rays of the setting sun on the sea, ready to vanish any moment."], AS(2), "medium")

# ---------------- Extracts (Shine retellings) ----------------
C.extract("ext1", TAT + LEGEND, "तताँरा पासा गाँव का एक सुंदर और शक्तिशाली युवक था। वह सबकी मदद को सदा तैयार रहता था, इसलिए पूरा द्वीप उससे प्रेम करता था। उसकी कमर में हमेशा एक लकड़ी की तलवार बँधी रहती थी। लोगों का विश्वास था कि उस तलवार में अद्भुत दैवीय शक्ति है।",
  [("Which village was Tataanra from?", "Pasa (पासा)."), ("Why did the whole island love him?", "He was always ready to help everyone."),
   ("What did he always carry?", "A wooden sword."), ("What did people believe about it?", "That it had divine, magical power."), ("Give one quality of Tataanra.", "Helpful / strong / kind.")],
  intro=PROSE_INTRO)
C.extract("ext2", CUSTOM + VAM, "पशु-पर्व में वामीरो तताँरा से मिलने आई। उसकी माँ ने दोनों को साथ देखा तो आग बबूला हो गई और तताँरा को अपमानित करने लगी। गाँव के लोग इकट्ठा हो गए। वामीरो रोने लगी। तताँरा अपमान सह न सका।",
  [("Where did Vamiro come to meet Tataanra?", "At the पशु-पर्व (animal festival)."), ("Who saw them together?", "Vamiro's mother."),
   ("What did she do?", "She became furious and insulted Tataanra."), ("What does 'आग बबूला होना' mean?", "To become very angry."), ("How did Vamiro react?", "She began to cry.")],
  intro=PROSE_INTRO)

# ---------------- Objective practice ----------------
C.m("mcq01", LEGEND, "The story belongs to:", [("the Andaman and Nicobar Islands", ""), ("Lakshadweep", "Andaman-Nicobar."), ("Kerala", "Andaman-Nicobar."), ("Goa", "Andaman-Nicobar.")], "A Nicobari folk tale.")
C.m("mcq02", TAT, "Tataanra belonged to village:", [("Pasa", ""), ("Lapati", "That was Vamiro's."), ("Car Nicobar", "Pasa."), ("Port Blair", "Pasa.")], "पासा.")
C.m("mcq03", VAM, "Vamiro belonged to village:", [("Lapati", ""), ("Pasa", "That was Tataanra's."), ("Havelock", "Lapati."), ("Diglipur", "Lapati.")], "लपाती.")
C.m("mcq04", TAT, "Tataanra's sword was made of:", [("wood", ""), ("iron", "Wood."), ("gold", "Wood."), ("stone", "Wood.")], "People believed it had magical power.")
C.m("mcq05", VAM, "Vamiro was known for her:", [("sweet singing", ""), ("dancing", "Singing."), ("painting", "Singing."), ("wealth", "Singing.")], "Tataanra first heard her song.")
C.m("mcq06", VAM, "Why did Vamiro stop singing?", [("a high wave drenched her", ""), ("her mother called her", "A wave."), ("it started raining", "A wave."), ("she saw a snake", "A wave.")], "She was startled.")
C.m("mcq07", CUSTOM, "The custom said marriage was allowed:", [("only within one's own village", ""), ("only outside one's village", "The opposite."), ("only after age thirty", "Within the village."), ("only with the chief's permission", "Within the village.")], "This custom blocked their love.")
C.m("mcq08", CUSTOM, "Where did Vamiro's mother see the two together?", [("at the पशु-पर्व", ""), ("in the market", "At the festival."), ("at the temple", "At the festival."), ("in a boat", "At the festival.")], "In Pasa village.")
C.m("mcq09", TAT, "Tataanra drove his sword into the earth to:", [("calm his anger", ""), ("dig a well", "To calm his anger."), ("plant a tree", "Anger."), ("show a trick", "Anger.")], "'क्रोध का शमन करने के लिए'.")
C.m("mcq10", LEGEND, "The land split into:", [("Little Andaman and Car Nicobar", ""), ("Great Nicobar and Sri Lanka", "Little Andaman and Car Nicobar."), ("Port Blair and Havelock", "Little Andaman and Car Nicobar."), ("Andaman and Lakshadweep", "Little Andaman and Car Nicobar.")], "According to the legend.")
C.m("mcq11", CUSTOM, "After their death, the people of Nicobar:", [("began marrying outside their village", ""), ("banned all marriages", "They changed the custom."), ("left the island", "They changed the custom."), ("worshipped the sword", "They changed the custom.")], "Their sacrifice changed society.")
C.m("mcq12", TAT, "'शमन' means:", [("calming", ""), ("increasing", "Calming."), ("hiding", "Calming."), ("showing", "Calming.")], "क्रोध का शमन.")
C.m("mcq13", VAM, "'याचना' means:", [("pleading, request", ""), ("order", "Request."), ("anger", "Request."), ("song", "Request.")], "Tataanra pleaded with Vamiro.")
C.m("mcq14", LEGEND, "'विभक्त' means:", [("divided", ""), ("joined", "Divided."), ("worshipped", "Divided."), ("decorated", "Divided.")], "The island was divided.")
C.m("mcq15", CUSTOM, "The main message of the story is that:", [("harmful customs should be broken", ""), ("swords are dangerous", "Customs."), ("islands are beautiful", "Customs."), ("songs bring luck", "Customs.")], "Love and humanity above rigid rules.")
C.m("mcq16", LEGEND, "The writer of this chapter is:", [("Leeladhar Mandloi", ""), ("Premchand", "Mandloi."), ("Prahlad Agrawal", "He wrote about Shailendra."), ("Nida Fazli", "Mandloi.")], "A poet and broadcaster.")
C.tf("tf1", TAT, "Tataanra's sword was made of iron.", False, "It was wooden.")
C.tf("tf2", CUSTOM, "By custom, marriage was allowed only within one's own village.", True, "This blocked their love.")
C.tf("tf3", VAM, "Vamiro's father insulted Tataanra at the festival.", False, "Her mother did.")
C.tf("tf4", LEGEND, "According to the legend, the sword split the island.", True, "Little Andaman and Car Nicobar.")
C.tf("tf5", CUSTOM, "After their death, the old custom continued as before.", False, "People began marrying outside the village.")
C.tf("tf6", TAT, "Tataanra was loved by the whole island because he helped everyone.", True, "Kind and helpful.")
C.two("sa1", VAM, "Why did Vamiro first answer Tataanra coldly?",
      ["By custom she could not speak freely with a young man of another village.", "She was also startled by a stranger asking her name suddenly."])
C.two("sa2", CUSTOM, "Do you think Tataanra's reaction in anger was right? Give a reason.",
      ["His pain at the public insult is understandable.", "But anger caused destruction; patient effort to change the custom would have been better."], difficulty="medium")

chapter = header("sparsh", "ch08", 8, "तताँरा-वामीरो कथा", "लीलाधर मंडलोई", "prose", ["tataanra_character", "vamiro_love", "custom_and_sacrifice", "nicobar_legend"],
                 "CBSE 2025-26 Hindi Course B (085), Section C: Sparsh Part 2 prose. Assessed through extract-based MCQs (1 mark each) and short answers in 25-30 words (2 marks); answers are written in Hindi. The text is in copyright: read it in the NCERT textbook.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
