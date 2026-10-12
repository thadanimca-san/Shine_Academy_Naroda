"""CBSE Class 10 Hindi Course B, Sparsh Part 2, Ch 3: मनुष्यता (Maithilisharan Gupt, d. 1964; public domain in India from 2025)."""
import sys
from hindi_common import make, header, path, ex
from lit_common import closing

ROOT = sys.argv[1]
PATH = path("sparsh", "ch03_manushyata")
C = make("hsp10ch03")
blk = C.blk
SAC, GEN, HUM, UNI = ["noble_death_sacrifice"], ["generosity"], ["humility"], ["unity_brotherhood"]
PE = lambda n: ex(n)
BH = lambda n: ex(n, "भाव स्पष्ट कीजिए")

POEM = ("*विचार लो कि मर्त्य हो न मृत्यु से डरो कभी,*\n*मरो परंतु यों मरो कि याद जो करें सभी।*\n*हुई न यों सुमृत्यु तो वृथा मरे, वृथा जिए,*\n*मरा नहीं वही कि जो जिया न आपके लिए।*\n*यही पशु-प्रवृत्ति है कि आप आप ही चरे,*\n*वही मनुष्य है कि जो मनुष्य के लिए मरे॥ 1॥*\n\n"
        "*उसी उदार की कथा सरस्वती बखानती,*\n*उसी उदार से धरा कृतार्थ भाव मानती।*\n*उसी उदार की सदा सजीव कीर्ति कूजती;*\n*तथा उसी उदार को समस्त सृष्टि पूजती।*\n*अखंड आत्म भाव जो असीम विश्व में भरे,*\n*वही मनुष्य है कि जो मनुष्य के लिए मरे॥ 2॥*\n\n"
        "*क्षुधार्त रंतिदेव ने दिया करस्थ थाल भी,*\n*तथा दधीचि ने दिया परार्थ अस्थिजाल भी।*\n*उशीनर क्षितीश ने स्वमांस दान भी किया,*\n*सहर्ष वीर कर्ण ने शरीर-चर्म भी दिया।*\n*अनित्य देह के लिए अनादि जीव क्या डरे?*\n*वही मनुष्य है कि जो मनुष्य के लिए मरे॥ 3॥*\n\n"
        "*सहानुभूति चाहिए, महाविभूति है यही;*\n*वशीकृता सदैव है बनी हुई स्वयं मही।*\n*विरुद्धवाद बुद्ध का दया-प्रवाह में बहा,*\n*विनीत लोकवर्ग क्या न सामने झुका रहा?*\n*अहा! वही उदार है परोपकार जो करे,*\n*वही मनुष्य है कि जो मनुष्य के लिए मरे॥ 4॥*\n\n"
        "*रहो न भूल के कभी मदांध तुच्छ वित्त में,*\n*सनाथ जान आपको करो न गर्व चित्त में।*\n*अनाथ कौन है यहाँ? त्रिलोकनाथ साथ हैं,*\n*दयालु दीनबंधु के बड़े विशाल हाथ हैं।*\n*अतीव भाग्यहीन है अधीर भाव जो करे,*\n*वही मनुष्य है कि जो मनुष्य के लिए मरे॥ 5॥*\n\n"
        "*अनंत अंतरिक्ष में अनंत देव हैं खड़े,*\n*समक्ष ही स्वबाहु जो बढ़ा रहे बड़े-बड़े।*\n*परस्परावलंब से उठो तथा बढ़ो सभी,*\n*अभी अमर्त्य-अंक में अपंक हो चढ़ो सभी।*\n*रहो न यों कि एक से न काम और का सरे,*\n*वही मनुष्य है कि जो मनुष्य के लिए मरे॥ 6॥*\n\n"
        "*'मनुष्य मात्र बंधु है' यही बड़ा विवेक है,*\n*पुराणपुरुष स्वयंभू पिता प्रसिद्ध एक है।*\n*फलानुसार कर्म के अवश्य बाह्य भेद हैं,*\n*परंतु अंतरैक्य में प्रमाणभूत वेद हैं।*\n*अनर्थ है कि बंधु ही न बंधु की व्यथा हरे,*\n*वही मनुष्य है कि जो मनुष्य के लिए मरे॥ 7॥*\n\n"
        "*चलो अभीष्ट मार्ग में सहर्ष खेलते हुए,*\n*विपत्ति, विघ्न जो पड़ें उन्हें ढकेलते हुए।*\n*घटे न हेलमेल हाँ, बढ़े न भिन्नता कभी,*\n*अतर्क एक पंथ के सतर्क पंथ हों सभी।*\n*तभी समर्थ भाव है कि तारता हुआ तरे,*\n*वही मनुष्य है कि जो मनुष्य के लिए मरे॥ 8॥*")

MEANING = ("| Stanza | Meaning |\n|---|---|\n"
           "| **1. विचार लो कि मर्त्य हो** | We are mortal, so do not fear death; die in a way that everyone remembers. One who lives only for himself lives and dies in vain; grazing only for oneself is animal nature. A true human lives and dies for others. |\n"
           "| **2. उसी उदार की कथा** | Saraswati (books) sings the story of the generous; the earth feels grateful to them; their fame echoes for ever; all creation worships them. One who spreads oneness through the whole world is a true human. |\n"
           "| **3. क्षुधार्त रंतिदेव** | Hungry Rantidev gave away his plate of food; Dadhichi gave his bones; King Shivi of Ushinar gave his own flesh; brave Karna gladly gave his skin-armour. Why should the eternal soul fear for the mortal body? |\n"
           "| **4. सहानुभूति चाहिए** | Sympathy is the greatest wealth; it wins the whole earth. The Buddha's kindness washed away opposition and the world bowed before him. One who helps others is truly generous. |\n"
           "| **5. रहो न भूल के कभी** | Never be blinded by pride in petty wealth, or proud that you have protectors. No one is an orphan: God, the lord of the three worlds and friend of the poor, is with all, with very large hands. Only the impatient one is truly unlucky. |\n"
           "| **6. अनंत अंतरिक्ष में** | Countless gods stand in the endless sky, holding out their arms to help. Rise and progress together with mutual support, and reach the lap of the gods, free of stain. Do not live so that no one benefits from you. |\n"
           "| **7. 'मनुष्य मात्र बंधु है'** | 'All humans are brothers' is the highest wisdom; we all have one Father, God. Our outer differences come from our deeds, but the Vedas prove that we are one inside. It is wrong if a brother does not remove a brother's pain. |\n"
           "| **8. चलो अभीष्ट मार्ग में** | Walk your chosen path happily, pushing aside troubles and obstacles. Let friendship never fall and differences never grow; let all paths become one. True strength lies in crossing over while helping others cross too. |")

sections = [
 {"id": "s1", "title": "What makes us human?", "blocks": [
  blk("s1.hook", "hook", title="One line, eight times",
    body="Every stanza of this poem ends with the same line: **'वही मनुष्य है कि जो मनुष्य के लिए मरे'** (a true human is one who lives and dies for other humans).\n\n"
         "The poet says eating, sleeping and caring only for ourselves is what animals do. To be truly human we must **share, sacrifice, stay humble and stand together**."),
  blk("s1.inspiration", "inspiration", title="The poet", person="Maithilisharan Gupt", years="1886–1964",
    body="**Maithilisharan Gupt** was born in **Chirgaon** near **Jhansi** (Uttar Pradesh). He was a major poet of the **Dwivedi age** and helped make **Khari Boli** the language of Hindi poetry. For the patriotism and Indian values in his poems he was honoured as **'राष्ट्रकवि'** (national poet).\n\n"
         "His famous works include **भारत-भारती**, **साकेत**, **यशोधरा**, **जयद्रथ-वध** and **पंचवटी**. He received the **Padma Bhushan** and was a member of the **Rajya Sabha**.",
    future="Gupt's call for kindness and unity is as needed today as it was a hundred years ago."),
  C.socratic("s1.socratic", "According to the poet, what is 'पशु-प्रवृत्ति' (animal nature)?",
    ["Caring only for oneself", "Working hard all day", "Living in the forest"], 0,
    "'आप आप ही चरे': grazing only for oneself.")
 ]},
 {"id": "s2", "title": "The poem and its meaning", "blocks": [
  blk("s2.poem", "theory", title="मनुष्यता", body=POEM),
  blk("s2.table", "markdown_table", title="Meaning of each stanza", revision=True, body=MEANING),
  C.kc("s2.check", "What kind of death does the poet call 'सुमृत्यु' (a good death)?",
    [("a death after which everyone remembers you for your good deeds", ""), ("a peaceful death in old age", "It is about being remembered."), ("a death in battle only", "It is about service to others."), ("a death without pain", "It is about being remembered.")],
    "'मरो परंतु यों मरो कि याद जो करें सभी'.")
  ,C.kc("s2.check2", "Which great giver donated his bones?",
    [("Dadhichi", ""), ("Karna", "Karna gave his skin-armour."), ("Rantidev", "Rantidev gave his plate of food."), ("King Shivi", "Shivi gave his flesh.")],
    "'दधीचि ने दिया परार्थ अस्थिजाल भी'.")
 ]},
 {"id": "s3", "title": "The poet's message", "blocks": [
  blk("s3.thm", "theory", title="What the poem teaches", revision=True,
    body="**Do not fear death; make it meaningful:** we are mortal, so live and die in a way that people remember (**सुमृत्यु**). Living only for oneself is **पशु-प्रवृत्ति**.\n\n"
         "**The generous are honoured:** books praise them, the earth is grateful, and their fame lives on.\n\n"
         "**Great givers:** **रंतिदेव** (gave his plate of food while starving), **दधीचि** (gave his bones to make the thunderbolt), **उशीनर के राजा शिवि** (gave his own flesh to save a dove), **कर्ण** (gave his kavach, armour joined to his skin). The body is temporary; the soul is eternal.\n\n"
         "**Sympathy is the greatest wealth:** the **Buddha** won the world through compassion.\n\n"
         "**No pride in wealth:** never be blinded by petty wealth; no one is helpless, for God (**दीनबंधु**) is with everyone.\n\n"
         "**Mutual support:** rise together (**परस्परावलंब**); live so that others benefit from you.\n\n"
         "**Brotherhood:** **'मनुष्य मात्र बंधु है'**; God is the one father of all; outer differences come from deeds, but inside we are one.\n\n"
         "**Walk together:** face obstacles cheerfully, keep friendship, reduce differences, and **help others across as you cross (तारता हुआ तरे)**."),
  C.kc("s3.check", "Why did the Buddha's opponents bow before him?",
    [("his compassion washed away their opposition", ""), ("he defeated them in war", "Compassion, not war."), ("he gave them money", "Compassion."), ("he was a king", "Compassion.")],
    "'विरुद्धवाद बुद्ध का दया-प्रवाह में बहा'.")
  ,C.kc("s3.check2", "'तारता हुआ तरे' means:",
    [("to cross over while helping others cross", ""), ("to swim across a river", "It is a metaphor for life."), ("to defeat others", "It means helping others."), ("to travel alone", "Together, helping others.")],
    "True strength is rising along with others.")
 ]},
 {"id": "s4", "title": "Language and style", "blocks": [
  blk("s4.thm", "theory", title="Language and devices", revision=True,
    body="| Feature | Example / note |\n|---|---|\n| **Language** | **खड़ी बोली** rich in **तत्सम** (Sanskrit) words: *मर्त्य, क्षुधार्त, करस्थ, क्षितीश, अमर्त्य, परस्परावलंब* |\n"
         "| **Refrain (टेक)** | 'वही मनुष्य है कि जो मनुष्य के लिए मरे' ends every stanza |\n| **Mythological examples** | रंतिदेव, दधीचि, शिवि, कर्ण, बुद्ध |\n"
         "| **अनुप्रास (alliteration)** | 'मरो परंतु यों मरो', 'वृथा मरे, वृथा जिए' |\n| **पुनरुक्ति प्रकाश** | 'आप आप', 'बड़े-बड़े' |\n| **प्रश्न अलंकार (question)** | 'अनाथ कौन है यहाँ?', 'अनित्य देह के लिए अनादि जीव क्या डरे?' |\n\n"
         "**Tone:** motivational (उद्बोधन); simple message in elevated language."),
  C.kc("s4.check", "The language of 'मनुष्यता' is:",
    [("Khari Boli rich in tatsam words", ""), ("Braj", "Gupt wrote in Khari Boli."), ("Awadhi", "Khari Boli."), ("Rajasthani", "Khari Boli.")],
    "With many Sanskrit words.")
 ]},
 closing(C,
   "- **Refrain: 'वही मनुष्य है कि जो मनुष्य के लिए मरे'.**\n- **Four givers: रंतिदेव (थाल), दधीचि (अस्थि), शिवि (मांस), कर्ण (चर्म/कवच).**\n- **Message: सुमृत्यु, उदारता, सहानुभूति, गर्व नहीं, परस्परावलंब, भाईचारा, साथ चलना.**",
   "1. Mixing up the givers: Dadhichi gave **bones**, Karna gave **skin-armour**, Rantidev gave his **plate of food**, Shivi gave his **flesh**.\n"
   "2. Taking 'मरे' literally only: it means **living and giving one's life for others**.\n3. Writing that the poet praises wealth: he warns against **pride in wealth**.\n4. Writing exam answers in English: answer in **Hindi**.",
   "Students tell one of the four giver stories in a minute each, then link it to a modern example of sacrifice (soldiers, doctors, organ donors).",
   "When did you last do something only for someone else? How did it feel?",
   "- **Kar Chale Hum Fida (Ch 5):** soldiers who give their lives for the nation.\n- **Civics:** fraternity in the Preamble of the Constitution.",
   "'वही मनुष्य है कि जो मनुष्य के लिए मरे.' Explain the poet's idea of a true human in about 60 words.",
   "The poet says a true human does not live only for himself, which is animal nature, but lives and even dies for others. He gives the examples of Rantidev, Dadhichi, Shivi and Karna, who sacrificed everything. A true human shows sympathy, avoids pride in wealth, treats all as brothers and helps others rise along with himself. Such a person is remembered for ever.",
   "- Maithilisharan Gupt, the 'Rashtrakavi', wrote this poem in tatsam-rich Khari Boli.\n- Live and die for others; living for oneself is animal nature.\n"
   "- Givers like Rantidev, Dadhichi, Shivi and Karna are examples; sympathy is the greatest wealth.\n- Avoid pride, support each other, see all humans as brothers, and walk together.",
   "- Answer in Hindi, in 25-30 words for 2 marks.\n- Name the givers and what each gave.\n- Quote the refrain where it fits.",
   [("What did Dadhichi and Karna give?", "Dadhichi gave his bones; Karna gave his skin-armour (kavach)."),
    ("What is 'सुमृत्यु'?", "A death after a life of service, for which everyone remembers you.")]),
]

# ---------------- NCERT प्रश्न-अभ्यास (क) ----------------
C.two("pa1", SAC, "What kind of death has the poet called 'सुमृत्यु'?",
      ["A death after a life spent for others, so that everyone remembers the person.", "One who lives only for himself lives and dies in vain."], PE(1))
C.two("pa2", GEN, "How can a generous person be recognised?",
      ["A generous person helps others, spreads oneness and lives for others.", "Books praise him, the earth is grateful to him, and his fame lives for ever."], PE(2))
C.two("pa3", SAC, "What message has the poet given for 'humanity' through the examples of Dadhichi, Karna and others?",
      ["Dadhichi gave his bones and Karna his armour; Rantidev and Shivi also gave all they had.", "We too should be ready to sacrifice for others, without fearing for the temporary body."], PE(3), "medium")
C.two("pa4", HUM, "In which lines has the poet said that we should live without pride?",
      ["'रहो न भूल के कभी मदांध तुच्छ वित्त में, सनाथ जान आपको करो न गर्व चित्त में।'", "We should never be proud of petty wealth or of having powerful supporters."], PE(4))
C.two("pa5", UNI, "What do you understand by 'मनुष्य मात्र बंधु है'? Explain.",
      ["All human beings are brothers, because God is the one father of all.", "Outer differences come from our deeds, but inside we are one, so we must remove each other's pain."], PE(5))
C.two("pa6", UNI, "Why has the poet inspired everyone to move forward together?",
      ["Walking together increases friendship and removes differences.", "By supporting each other we can face obstacles and help everyone progress."], PE(6))
C.two("pa7", GEN, "What kind of life should a person live? Write on the basis of this poem.",
      ["One should live for others, with sympathy, generosity and without pride.", "One should treat everyone as a brother and help others rise along with oneself."], PE(7))
C.two("pa8", UNI, "What message does the poet want to give through the poem 'मनुष्यता'?",
      ["A true human lives and dies for others; selfishness is animal nature.", "We should be generous, kind, humble and united, helping each other progress."], PE(8))
# ---------------- NCERT (ख) भाव ----------------
C.two("bh1", GEN, "Explain the idea: 'सहानुभूति चाहिए, महाविभूति है यही; वशीकृता सदैव है बनी हुई स्वयं मही। विरुद्धवाद बुद्ध का दया-प्रवाह में बहा, विनीत लोकवर्ग क्या न सामने झुका रहा?'",
      ["Sympathy is the greatest wealth; through it one can win the whole earth.", "The Buddha's compassion washed away all opposition, and the world bowed humbly before him."], BH(1), "medium")
C.two("bh2", HUM, "Explain the idea: 'रहो न भूल के कभी मदांध तुच्छ वित्त में, सनाथ जान आपको करो न गर्व चित्त में। अनाथ कौन है यहाँ? त्रिलोकनाथ साथ हैं, दयालु दीनबंधु के बड़े विशाल हाथ हैं।'",
      ["Never be blinded by pride in petty wealth or proud that you have supporters.", "No one is helpless here, because kind God, the friend of the poor, is with everyone."], BH(2), "medium")
C.two("bh3", UNI, "Explain the idea: 'चलो अभीष्ट मार्ग में सहर्ष खेलते हुए, विपत्ति, विघ्न जो पड़ें उन्हें ढकेलते हुए। घटे न हेलमेल हाँ, बढ़े न भिन्नता कभी, अतर्क एक पंथ के सतर्क पंथ हों सभी।'",
      ["Walk your chosen path happily, pushing aside troubles and obstacles.", "Keep friendship, never let differences grow, and let everyone walk one shared path together."], BH(3), "medium")

# ---------------- Extracts ----------------
C.extract("ext1", SAC, "विचार लो कि मर्त्य हो न मृत्यु से डरो कभी,\nमरो परंतु यों मरो कि याद जो करें सभी।\nहुई न यों सुमृत्यु तो वृथा मरे, वृथा जिए,\nमरा नहीं वही कि जो जिया न आपके लिए।",
  [("What does 'मर्त्य' mean?", "Mortal, one who must die."), ("What does the poet tell us about death?", "Not to fear it, but to die in a way that everyone remembers."),
   ("When are life and death in vain?", "When there is no 'सुमृत्यु', a death remembered for good deeds."), ("Who is truly alive even after death?", "One who did not live only for himself."), ("Name the device in 'वृथा मरे, वृथा जिए'.", "Alliteration (अनुप्रास) / repetition.")])
C.extract("ext2", SAC, "क्षुधार्त रंतिदेव ने दिया करस्थ थाल भी,\nतथा दधीचि ने दिया परार्थ अस्थिजाल भी।\nउशीनर क्षितीश ने स्वमांस दान भी किया,\nसहर्ष वीर कर्ण ने शरीर-चर्म भी दिया।",
  [("What did Rantidev give?", "The plate of food in his hand, though he was hungry."), ("What did Dadhichi give?", "His bones, for the good of others."),
   ("Who is 'उशीनर क्षितीश'?", "King Shivi of Ushinar, who gave his own flesh."), ("What did Karna give?", "His skin-armour (kavach)."), ("What is 'क्षुधार्त'?", "Hungry, suffering from hunger.")])

# ---------------- Objective practice ----------------
C.m("mcq01", SAC, "'मर्त्य' means:", [("mortal", ""), ("immortal", "That is अमर्त्य."), ("brave", "Mortal."), ("human", "Mortal.")], "One who must die.")
C.m("mcq02", SAC, "According to the poet, 'पशु-प्रवृत्ति' is:", [("living only for oneself", ""), ("hard work", "Selfishness."), ("eating grass", "It is a metaphor."), ("living in a forest", "Selfishness.")], "'आप आप ही चरे'.")
C.m("mcq03", SAC, "Who gave away his plate of food while hungry?", [("Rantidev", ""), ("Dadhichi", "Rantidev."), ("Karna", "Rantidev."), ("Shivi", "Rantidev.")], "'क्षुधार्त रंतिदेव ने दिया करस्थ थाल भी'.")
C.m("mcq04", SAC, "Dadhichi gave his:", [("bones", ""), ("flesh", "That was Shivi."), ("skin-armour", "That was Karna."), ("plate of food", "That was Rantidev.")], "'अस्थिजाल'.")
C.m("mcq05", SAC, "'उशीनर क्षितीश' refers to:", [("King Shivi", ""), ("King Karna", "Shivi."), ("King Rantidev", "Shivi."), ("King Dasharath", "Shivi.")], "He gave his own flesh.")
C.m("mcq06", SAC, "Karna gladly gave:", [("his skin-armour (शरीर-चर्म)", ""), ("his kingdom", "His armour."), ("his bones", "That was Dadhichi."), ("his food", "That was Rantidev.")], "'सहर्ष वीर कर्ण ने शरीर-चर्म भी दिया'.")
C.m("mcq07", GEN, "According to the poet, the greatest wealth (महाविभूति) is:", [("sympathy", ""), ("gold", "Sympathy."), ("land", "Sympathy."), ("knowledge of books", "Sympathy.")], "'सहानुभूति चाहिए, महाविभूति है यही'.")
C.m("mcq08", GEN, "Whose compassion washed away opposition?", [("the Buddha's", ""), ("Karna's", "The Buddha."), ("Rama's", "The Buddha."), ("Ashoka's", "The Buddha.")], "'विरुद्धवाद बुद्ध का दया-प्रवाह में बहा'.")
C.m("mcq09", HUM, "The poet warns us not to be blinded by pride in:", [("petty wealth", ""), ("knowledge", "Wealth."), ("friends", "Wealth."), ("strength", "Wealth.")], "'मदांध तुच्छ वित्त में'.")
C.m("mcq10", HUM, "'दीनबंधु' means:", [("friend of the poor (God)", ""), ("a poor brother", "Friend of the poor."), ("a rich man", "Friend of the poor."), ("a king", "Friend of the poor.")], "God with large, helping hands.")
C.m("mcq11", HUM, "According to the poet, who is truly unlucky?", [("one who becomes impatient", ""), ("one who is poor", "The impatient one."), ("one who is an orphan", "No one is an orphan."), ("one who has no friends", "The impatient one.")], "'अतीव भाग्यहीन है अधीर भाव जो करे'.")
C.m("mcq12", UNI, "'परस्परावलंब' means:", [("mutual support", ""), ("self-reliance", "Mutual support."), ("competition", "Mutual support."), ("separation", "Mutual support.")], "Rise together.")
C.m("mcq13", UNI, "'मनुष्य मात्र बंधु है' means:", [("all humans are brothers", ""), ("only some humans are brothers", "All."), ("brothers are human", "All humans are brothers."), ("humans have no brothers", "All are brothers.")], "The highest wisdom.")
C.m("mcq14", UNI, "Our outer differences come from:", [("our deeds (कर्म)", ""), ("our birth", "From deeds."), ("God's wish", "From deeds."), ("our wealth", "From deeds.")], "'फलानुसार कर्म के अवश्य बाह्य भेद हैं'.")
C.m("mcq15", UNI, "'तारता हुआ तरे' means:", [("rise while helping others rise", ""), ("swim alone", "Helping others."), ("defeat others", "Helping others."), ("float on water", "A metaphor.")], "True strength.")
C.m("mcq16", SAC, "The refrain of the poem is:", [("वही मनुष्य है कि जो मनुष्य के लिए मरे", ""), ("मरो परंतु यों मरो", "That is in stanza 1 only."), ("मनुष्य मात्र बंधु है", "That is in stanza 7."), ("सहानुभूति चाहिए", "That is in stanza 4.")], "It ends every stanza.")
C.m("mcq17", GEN, "The poet of 'मनुष्यता' is known as:", [("राष्ट्रकवि", ""), ("महाप्राण", "That was Nirala."), ("कविकुलगुरु", "Kalidas."), ("भारतेंदु", "Harishchandra.")], "Maithilisharan Gupt.")
C.m("mcq18", GEN, "Which is a famous work of Maithilisharan Gupt?", [("साकेत", ""), ("कामायनी", "By Jaishankar Prasad."), ("गोदान", "By Premchand."), ("मधुशाला", "By Bachchan.")], "Also भारत-भारती, यशोधरा.")
C.m("mcq19", SAC, "'अनित्य देह के लिए अनादि जीव क्या डरे?' means the soul should not fear because:", [("the body is temporary and the soul eternal", ""), ("the body is strong", "The body is temporary."), ("death never comes", "Death comes to the body."), ("God punishes fear", "The soul is eternal.")], "So give freely.")
C.m("mcq20", HUM, "'अनाथ कौन है यहाँ?' is an example of:", [("a rhetorical question", ""), ("a simile", "A question."), ("alliteration", "A question."), ("personification", "A question.")], "No one is helpless; God is with all.")
C.tf("tf1", SAC, "The poet says we should fear death.", False, "'न मृत्यु से डरो कभी'.")
C.tf("tf2", SAC, "Living only for oneself is called animal nature in the poem.", True, "'यही पशु-प्रवृत्ति है'.")
C.tf("tf3", SAC, "Karna gave his bones for the good of others.", False, "Dadhichi gave his bones; Karna gave his armour.")
C.tf("tf4", HUM, "The poet says that no one in this world is helpless.", True, "'अनाथ कौन है यहाँ? त्रिलोकनाथ साथ हैं'.")
C.tf("tf5", UNI, "The poet wants differences among people to grow.", False, "'बढ़े न भिन्नता कभी'.")
C.tf("tf6", GEN, "Maithilisharan Gupt wrote in Khari Boli.", True, "With many tatsam words.")
C.two("sa1", UNI, "Why does the poet call it 'अनर्थ' if a brother does not remove a brother's pain?",
      ["All humans are brothers, children of the same God.", "So ignoring another's suffering goes against humanity and is a great wrong."])
C.two("sa2", GEN, "How does a generous person become immortal according to the poem?",
      ["His story is told in books and the whole earth is grateful to him.", "His fame lives on for ever, and all creation honours him."])
C.two("sa3", SAC, "Give one modern example of the spirit of Dadhichi or Karna.",
      ["Organ donors and blood donors give parts of their body to save others.", "Like Dadhichi and Karna, they give selflessly for others' good."], difficulty="medium")

chapter = header("sparsh", "ch03", 3, "मनुष्यता", "मैथिलीशरण गुप्त", "poem", ["noble_death_sacrifice", "generosity", "humility", "unity_brotherhood"],
                 "CBSE 2025-26 Hindi Course B (085), Section C: Sparsh Part 2 poetry. Assessed through extract-based MCQs (1 mark each) and short answers in 25-30 words (2 marks); answers are written in Hindi.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
