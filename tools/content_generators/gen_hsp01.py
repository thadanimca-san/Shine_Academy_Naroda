"""CBSE Class 10 Hindi Course B, Sparsh Part 2, Ch 1: साखी (Kabir). The sakhis are 15th-century public-domain verse."""
import sys
from hindi_common import make, header, path, ex
from lit_common import closing

ROOT = sys.argv[1]
PATH = path("sparsh", "ch01_sakhi")
C = make("hsp10ch01")
blk = C.blk
SPEECH, GOD, EGO, CRITIC = ["sweet_speech"], ["god_within"], ["ego_and_knowledge"], ["critic_and_love"]
PE = lambda n: ex(n)
BH = lambda n: ex(n, "भाव स्पष्ट कीजिए")

SAKHI = ("*ऐसी बाँणी बोलिये, मन का आपा खोइ।*\n*अपना तन सीतल करै, औरन कौं सुख होइ॥ 1॥*\n\n"
         "*कस्तूरी कुंडलि बसै, मृग ढूँढै बन माँहि।*\n*ऐसैं घटि घटि राँम है, दुनियाँ देखै नाँहिं॥ 2॥*\n\n"
         "*जब मैं था तब हरि नहीं, अब हरि हैं मैं नाँहि।*\n*सब अँधियारा मिटि गया, जब दीपक देख्या माँहि॥ 3॥*\n\n"
         "*सुखिया सब संसार है, खायै अरू सोवै।*\n*दुखिया दास कबीर है, जागै अरू रोवै॥ 4॥*\n\n"
         "*बिरह भुवंगम तन बसै, मंत्र न लागै कोइ।*\n*राम बियोगी ना जिवै, जिवै तो बौरा होइ॥ 5॥*\n\n"
         "*निंदक नेड़ा राखिये, आँगणि कुटी बँधाइ।*\n*बिन साबण पाँणीं बिना, निरमल करै सुभाइ॥ 6॥*\n\n"
         "*पोथी पढ़ि पढ़ि जग मुवा, पंडित भया न कोइ।*\n*ऐकै अषिर पीव का, पढ़ै सु पंडित होइ॥ 7॥*\n\n"
         "*हम घर जाल्या आपणाँ, लिया मुराड़ा हाथि।*\n*अब घर जालौं तास का, जे चलै हमारे साथि॥ 8॥*")

MEANING = ("| Sakhi | Meaning |\n|---|---|\n"
           "| **1. ऐसी बाँणी बोलिये** | Speak words that come after giving up ego; they cool your own body (mind) and give happiness to others. |\n"
           "| **2. कस्तूरी कुंडलि बसै** | The musk is in the deer's own navel, yet it searches the forest; God lives in every heart, but people do not see Him. |\n"
           "| **3. जब मैं था तब हरि नहीं** | While 'I' (ego) existed, God was not found; when ego went, God was found, as darkness ends when the lamp of knowledge is seen within. |\n"
           "| **4. सुखिया सब संसार है** | The world is 'happy' eating and sleeping (lost in worldly pleasures); Kabir is 'unhappy', awake and weeping for God. |\n"
           "| **5. बिरह भुवंगम तन बसै** | The snake of separation lives in the body; no charm cures it; one separated from Ram cannot live, or lives like a madman. |\n"
           "| **6. निंदक नेड़ा राखिये** | Keep your critic near, build him a hut in your courtyard; without soap or water he cleans your nature. |\n"
           "| **7. पोथी पढ़ि पढ़ि जग मुवा** | The world died reading books, yet no one became wise; one who reads the single word of love (for God) becomes wise. |\n"
           "| **8. हम घर जाल्या आपणाँ** | I burnt my own house (worldly attachment) with a torch in hand; now I will burn the house of whoever walks with me. |")

sections = [
 {"id": "s1", "title": "The weaver-poet who spoke plainly", "blocks": [
  blk("s1.hook", "hook", title="Two lines that last six hundred years",
    body="A deer runs through the forest searching for a lovely smell, not knowing that the musk is in its own body. **Kabir** uses this picture to say that God is inside us, yet we search for Him outside.\n\n"
         "His **sakhis** (couplets) are short, simple and sharp. In two lines each, they teach about sweet speech, ego, love, criticism and true knowledge."),
  blk("s1.inspiration", "inspiration", title="The poet", person="Kabir", years="c. 1398–1518",
    body="**Kabir** was a saint-poet of the **Bhakti movement**, believed to have lived in **Kashi (Varanasi)** and to have earned his living as a **weaver**. He opposed blind ritual, caste pride and religious hypocrisy, and taught love of one formless God. His sayings were collected in works such as the **Bijak**.\n\n"
         "His language is a mix of many dialects (Awadhi, Braj, Rajasthani, Punjabi, Khari Boli), called **'सधुक्कड़ी'** or **'पंचमेल खिचड़ी'**.",
    future="Kabir's couplets are quoted in speeches, songs and everyday conversation; learning them gives you ready wisdom for life."),
  C.socratic("s1.socratic", "Why does Kabir advise keeping a critic close to you?",
    ["A critic points out our faults, so we can improve our nature", "Critics are our best friends always", "So that we can argue with them"], 0,
    "He cleans our nature without soap or water."),
 ]},
 {"id": "s2", "title": "The sakhis and their meaning", "blocks": [
  blk("s2.poem", "theory", title="साखी", body=SAKHI),
  blk("s2.table", "markdown_table", title="Meaning of each sakhi", revision=True, body=MEANING),
  C.kc("s2.check", "In the second sakhi, what does the musk deer stand for?",
    [("people who search for God outside, though He is within", ""), ("a hunter", "It stands for seekers who look outside."), ("a rich man", "It stands for seekers."), ("a saint who has found God", "It has not found the musk.")],
    "God lives in every heart.")
  ,C.kc("s2.check2", "What does 'दीपक' (lamp) mean in the third sakhi?",
    [("the light of knowledge within", ""), ("an oil lamp in a temple", "It is a symbol."), ("the sun", "It is inner knowledge."), ("fire", "It is inner knowledge.")],
    "Knowledge removes the darkness of ego.")
 ]},
 {"id": "s3", "title": "Kabir's teachings", "blocks": [
  blk("s3.thm", "theory", title="What Kabir teaches", revision=True,
    body="**Sweet speech:** words spoken without ego bring peace to the speaker and joy to the listener.\n\n"
         "**God within:** God is present in every heart (*घटि घटि राँम*), as musk is in the deer; we need not search temples or forests.\n\n"
         "**Ego blocks God:** 'मैं' (I) and 'हरि' cannot live together; when ego goes, the lamp of knowledge removes all darkness.\n\n"
         "**Worldly vs spiritual:** the world 'sleeps' in pleasure (ignorance); the devotee 'wakes' (is aware) and weeps for God. **सोना** = ignorance, **जागना** = awareness.\n\n"
         "**Love for God:** separation from God is like a snakebite no charm can cure.\n\n"
         "**Value of criticism:** a critic cleans our nature without soap or water.\n\n"
         "**True knowledge:** reading many books does not make one wise; the one word of love ('पीव' = beloved God) does.\n\n"
         "**Renunciation:** Kabir burnt his own house of attachment and invites those who follow him to do the same."),
  C.kc("s3.check", "In the fourth sakhi, 'सोना' (sleeping) is a symbol of:",
    [("ignorance and being lost in worldly pleasure", ""), ("rest after work", "It is a symbol."), ("death", "It is ignorance."), ("wealth (gold)", "Here it means sleeping, i.e. ignorance.")],
    "जागना = awareness of God.")
  ,C.kc("s3.check2", "According to Kabir, who is truly wise (पंडित)?",
    [("one who reads the single word of love", ""), ("one who reads many books", "The world died reading books."), ("one who is rich", "Love, not wealth."), ("one who performs rituals", "Love, not ritual.")],
    "'ऐकै अषिर पीव का'.")
 ]},
 {"id": "s4", "title": "Language and style", "blocks": [
  blk("s4.thm", "theory", title="Form, language and devices", revision=True,
    body="| Feature | Example / note |\n|---|---|\n| **Form** | **साखी / दोहा**: two lines, 13 + 11 matras in each half |\n| **Language** | **सधुक्कड़ी (पंचमेल खिचड़ी)**: a mix of dialects; simple, direct and forceful |\n"
         "| **रूपक (metaphor)** | 'बिरह भुवंगम' = separation as a snake |\n| **दृष्टांत (illustration)** | the musk deer explains God within |\n| **अनुप्रास (alliteration)** | 'पोथी पढ़ि पढ़ि' |\n"
         "| **पुनरुक्ति (repetition)** | 'घटि घटि', 'पढ़ि पढ़ि' |\n| **प्रतीक (symbol)** | सोना = ignorance, जागना = awareness, दीपक = knowledge, घर = attachment |\n\n"
         "**Spelling:** old forms like *बाँणी* (वाणी), *सीतल* (शीतल), *अषिर* (अक्षर), *पाँणीं* (पानी)."),
  C.kc("s4.check", "Kabir's language is called:",
    [("सधुक्कड़ी", ""), ("शुद्ध संस्कृत", "It is a mixed dialect."), ("अवधी only", "It mixes many dialects."), ("अंग्रेज़ी", "It is Hindi of his time.")],
    "Also called पंचमेल खिचड़ी.")
 ]},
 closing(C,
   "- **8 sakhis: वाणी, कस्तूरी, मैं-हरि, सुखिया-दुखिया, बिरह, निंदक, पोथी, घर जाल्या.**\n- **Symbols: दीपक = knowledge, सोना/जागना = ignorance/awareness, भुवंगम = snake of separation.**\n- **Language: सधुक्कड़ी; form: दोहा/साखी.**",
   "1. Taking 'सोना' to mean gold: here it means **sleeping** (ignorance).\n2. Saying Kabir rejects all learning: he rejects **bookish learning without love**.\n"
   "3. Explaining 'निंदक' as an enemy to avoid: Kabir says **keep him near**.\n4. Writing exam answers in English: answer in **Hindi**.",
   "Students recite one sakhi each, explain it in their own words, and give a real-life example (for example, a critic who helped them improve).",
   "Which of Kabir's sakhis can you use in your own life this week? How?",
   "- **Meera's pads (Ch 2):** another Bhakti poet, with a different kind of devotion.\n- **History:** the Bhakti movement and its message of equality.",
   "'Kabir's sakhis teach us how to live.' Explain with reference to any three sakhis in about 60 words.",
   "Kabir teaches us to speak sweetly after giving up ego, because such words calm us and please others. He tells us that God lives in every heart, like musk in the deer's navel, so we need not search outside. He advises keeping a critic close, since criticism cleans our nature without soap or water. Together these sakhis guide us towards humility, inner faith and self-improvement.",
   "- Kabir, a Bhakti saint-poet and weaver, wrote sakhis (dohas) in sadhukkadi language.\n- He teaches sweet, ego-free speech; God within every heart; ego as the barrier to God.\n"
   "- The world sleeps in pleasure while the devotee wakes and weeps for God.\n- Critics purify us; love, not bookish learning, makes one wise; renounce attachment.",
   "- Answer in Hindi, in 25-30 words for 2 marks.\n- Quote the relevant line of the sakhi.\n- Explain symbols (दीपक, सोना, निंदक) clearly.",
   [("What does 'कस्तूरी कुंडलि बसै' teach?", "God lives within us, as musk lives in the deer's navel, but we search outside."),
    ("Why keep a critic near?", "He points out our faults and cleans our nature without soap or water.")]),
]

# ---------------- NCERT प्रश्न-अभ्यास (क) ----------------
C.two("pa1", SPEECH, "How does speaking sweet words bring happiness to others and coolness to one's own body?",
      ["Sweet speech, free of ego, pleases the listener and makes them happy.", "It also calms the speaker's own mind, removing anger and pride."], PE(1))
C.two("pa2", EGO, "How does the darkness disappear when the lamp is seen? Explain with reference to the sakhi.",
      ["The lamp is the light of knowledge within; darkness is ignorance and ego.", "When inner knowledge comes, ego goes and one finds God, so all darkness ends."], PE(2))
C.two("pa3", GOD, "God is present in every particle, so why can we not see Him?",
      ["Like the musk deer searching the forest, we look for God outside in temples and forests.", "Because of ignorance and ego we do not look within our own heart."], PE(3))
C.two("pa4", GOD, "Who is happy and who is unhappy in the world? What do 'sleeping' and 'waking' symbolise here, and why are they used?",
      ["The world, lost in eating and sleeping, is 'happy'; Kabir, awake and weeping for God, is 'unhappy'.", "Sleeping symbolises ignorance; waking symbolises awareness of God; they contrast worldly and spiritual life."], PE(4))
C.two("pa5", CRITIC, "What means does Kabir suggest to keep one's nature pure?",
      ["He advises keeping a critic close, even building him a hut in one's courtyard.", "The critic shows our faults, cleaning our nature without soap or water."], PE(5))
C.two("pa6", EGO, "What does the poet want to say through the line 'ऐकै अषिर पीव का, पढ़ै सु पंडित होइ'?",
      ["Reading many books does not make one truly wise.", "One who reads the single word of love for God becomes truly learned."], PE(6))
C.two("pa7", SPEECH, "Explain the features of the language of Kabir's sakhis.",
      ["It is sadhukkadi (panchmel khichdi), a mix of many dialects, simple and direct.", "It uses symbols, metaphors and illustrations from everyday life, making it forceful."], PE(7))
# ---------------- NCERT (ख) भाव ----------------
C.two("bh1", GOD, "Explain the idea: 'बिरह भुवंगम तन बसै, मंत्र न लागै कोइ'.",
      ["Separation from God is like a snake living in the body.", "No charm or cure works on it; the devotee suffers until united with God."], BH(1))
C.two("bh2", GOD, "Explain the idea: 'कस्तूरी कुंडलि बसै, मृग ढूँढै बन माँहि'.",
      ["The musk is in the deer's own navel, yet it searches the forest for it.", "Likewise God is within us, but we search for Him outside."], BH(2))
C.two("bh3", EGO, "Explain the idea: 'जब मैं था तब हरि नहीं, अब हरि हैं मैं नाँहि'.",
      ["As long as ego ('I') was there, God could not be found.", "When ego disappeared, God was realised; ego and God cannot live together."], BH(3))
C.two("bh4", EGO, "Explain the idea: 'पोथी पढ़ि पढ़ि जग मुवा, पंडित भया न कोइ'.",
      ["People spend their whole lives reading books, yet do not become truly wise.", "Bookish knowledge without love and experience is useless."], BH(4))

# ---------------- Extracts ----------------
C.extract("ext1", SPEECH + CRITIC, "ऐसी बाँणी बोलिये, मन का आपा खोइ।\nअपना तन सीतल करै, औरन कौं सुख होइ॥",
  [("What kind of speech does Kabir advise?", "Sweet speech, after giving up ego."), ("What is 'आपा'?", "Ego, pride."),
   ("What does such speech do for the speaker?", "It cools (calms) the speaker's own body and mind."), ("What does it do for others?", "It gives them happiness."),
   ("Name the form of this verse.", "Sakhi (doha).")])
C.extract("ext2", GOD, "कस्तूरी कुंडलि बसै, मृग ढूँढै बन माँहि।\nऐसैं घटि घटि राँम है, दुनियाँ देखै नाँहिं॥",
  [("Where is the musk?", "In the deer's own navel."), ("Where does the deer search for it?", "In the forest."),
   ("What does 'घटि घटि' mean?", "In every heart (body)."), ("What is the message?", "God lives within us, but people do not see Him."), ("Name the device used.", "Illustration (दृष्टांत) / repetition (पुनरुक्ति) in 'घटि घटि'.")])

# ---------------- Objective practice ----------------
C.m("mcq01", SPEECH, "According to Kabir, sweet speech is possible after giving up:", [("ego (आपा)", ""), ("food", "Ego."), ("home", "Ego."), ("books", "Ego.")], "'मन का आपा खोइ'.")
C.m("mcq02", GOD, "Where does the musk deer search for the musk?", [("in the forest", ""), ("in its own navel", "That is where it actually is."), ("in the river", "In the forest."), ("in the village", "In the forest.")], "It does not know the musk is within.")
C.m("mcq03", EGO, "In 'जब मैं था तब हरि नहीं', 'मैं' means:", [("ego", ""), ("the poet's body", "It means ego."), ("the world", "Ego."), ("God", "God is 'हरि'.")], "Ego and God cannot coexist.")
C.m("mcq04", GOD, "Why is Kabir 'दुखिया' (unhappy)?", [("he is awake and weeps in longing for God", ""), ("he is poor", "Spiritual longing."), ("he is ill", "Spiritual longing."), ("he lost his house", "Spiritual longing.")], "'जागै अरू रोवै'.")
C.m("mcq05", GOD, "'बिरह भुवंगम' compares separation from God to:", [("a snake", ""), ("a lamp", "A snake."), ("a deer", "A snake."), ("a house", "A snake.")], "भुवंगम = snake.")
C.m("mcq06", CRITIC, "Kabir says the critic cleans our nature without:", [("soap and water", ""), ("books and teachers", "Soap and water."), ("money and gold", "Soap and water."), ("fire and air", "Soap and water.")], "'बिन साबण पाँणीं बिना'.")
C.m("mcq07", EGO, "'पीव' in the seventh sakhi refers to:", [("the beloved God", ""), ("a book", "The beloved God."), ("a pundit", "The beloved God."), ("water", "The beloved God.")], "The word of love for God.")
C.m("mcq08", EGO, "What did Kabir burn, according to the last sakhi?", [("his own house of worldly attachment", ""), ("his books", "His house (attachment)."), ("his enemy's house", "His own house."), ("a lamp", "His own house.")], "'हम घर जाल्या आपणाँ'.")
C.m("mcq09", SPEECH, "Kabir's language is also called:", [("पंचमेल खिचड़ी", ""), ("शुद्ध खड़ी बोली", "A mix of dialects."), ("संस्कृतनिष्ठ हिंदी", "A mix of dialects."), ("उर्दू", "A mix of dialects.")], "A mix of many dialects.")
C.m("mcq10", GOD, "'घटि घटि राँम है' means:", [("God is in every heart", ""), ("God is in every pot", "घट here means body/heart."), ("God is in temples", "In every heart."), ("God is far away", "In every heart.")], "So look within.")
C.m("mcq11", EGO, "In the third sakhi, 'अँधियारा' stands for:", [("ignorance", ""), ("night", "It is a symbol."), ("a dark room", "Ignorance."), ("sadness", "Ignorance.")], "Removed by the lamp of knowledge.")
C.m("mcq12", GOD, "The world is called 'सुखिया' because it:", [("eats and sleeps, lost in worldly pleasures", ""), ("prays all day", "It eats and sleeps."), ("works hard", "It eats and sleeps."), ("reads books", "It eats and sleeps.")], "'खायै अरू सोवै'.")
C.m("mcq13", CRITIC, "Where does Kabir suggest building the critic's hut?", [("in one's courtyard", ""), ("far away in the forest", "Near, in the courtyard."), ("on a hill", "In the courtyard."), ("in another village", "In the courtyard.")], "'आँगणि कुटी बँधाइ'.")
C.m("mcq14", SPEECH, "Kabir lived in:", [("Kashi (Varanasi)", ""), ("Mathura", "Kashi."), ("Delhi", "Kashi."), ("Ayodhya", "Kashi.")], "He was a weaver there.")
C.m("mcq15", SPEECH, "Kabir belonged to the:", [("Bhakti movement", ""), ("Riti period", "Bhakti."), ("modern period", "Bhakti."), ("Chhayavad", "Bhakti.")], "Saint-poet of devotion.")
C.m("mcq16", SPEECH, "A sakhi (doha) has:", [("two lines", ""), ("four lines", "Two lines."), ("six lines", "Two lines."), ("one line", "Two lines.")], "13 + 11 matras per half.")
C.m("mcq17", EGO, "Kabir's view of bookish learning is that it:", [("does not make one truly wise", ""), ("is the only path to God", "Love is the path."), ("makes one rich", "It does not make one wise."), ("should be done daily", "It does not make one wise.")], "Love makes one wise.")
C.m("mcq18", GOD, "'राम बियोगी ना जिवै' means one separated from God:", [("cannot live", ""), ("lives happily", "Cannot live."), ("becomes rich", "Cannot live."), ("forgets God", "Cannot live.")], "Or lives like a madman.")
C.m("mcq19", SPEECH, "'सीतल' in the first sakhi means:", [("cool, calm", ""), ("hot", "Opposite."), ("tired", "Cool."), ("strong", "Cool.")], "Sweet speech calms the speaker.")
C.m("mcq20", EGO, "In the last sakhi, 'मुराड़ा' is:", [("a burning torch", ""), ("a book", "A torch."), ("a house", "A torch."), ("a lamp of oil", "A burning stick (torch).")], "Taken in hand to burn attachment.")
C.tf("tf1", GOD, "Kabir says God is found only in temples.", False, "He says God is in every heart.")
C.tf("tf2", CRITIC, "Kabir advises keeping critics far away.", False, "He says keep them near.")
C.tf("tf3", SPEECH, "Sweet speech gives happiness to others and calms the speaker.", True, "First sakhi.")
C.tf("tf4", EGO, "According to Kabir, ego and God cannot live together.", True, "'जब मैं था तब हरि नहीं'.")
C.tf("tf5", EGO, "Kabir says reading many books makes one a true pundit.", False, "The word of love makes one wise.")
C.tf("tf6", SPEECH, "Kabir's language is a mix of many dialects.", True, "Sadhukkadi.")
C.two("sa1", GOD, "What is the difference between the 'happy' world and the 'unhappy' Kabir?",
      ["The world is happy in eating and sleeping, ignorant of God.", "Kabir is awake to the truth and suffers in longing for God."])
C.two("sa2", CRITIC, "Do you agree with Kabir that a critic is useful? Give a reason.",
      ["Yes; a critic shows faults we cannot see ourselves.", "This helps us correct them and improve our nature."])

chapter = header("sparsh", "ch01", 1, "साखी", "कबीर", "poem", ["sweet_speech", "god_within", "ego_and_knowledge", "critic_and_love"],
                 "CBSE 2025-26 Hindi Course B (085), Section C: Sparsh Part 2 poetry. Assessed through extract-based MCQs (1 mark each) and short answers in 25-30 words (2 marks); answers are written in Hindi.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
