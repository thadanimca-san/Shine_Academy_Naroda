"""CBSE Class 10 Hindi Course B, Sparsh Part 2, Ch 2: पद (Meera). The pads are 16th-century public-domain verse."""
import sys
from hindi_common import make, header, path, ex
from lit_common import closing

ROOT = sys.argv[1]
PATH = path("sparsh", "ch02_meera_pad")
C = make("hsp10ch02")
blk = C.blk
PLEA, SERVE, BEAUTY, LANG = ["plea_to_hari"], ["servant_devotion"], ["krishna_beauty"], ["meera_language"]
PE = lambda n: ex(n)
KS = lambda n: ex(n, "काव्य-सौंदर्य स्पष्ट कीजिए")

PAD1 = ("*हरि आप हरो जन री भीर।*\n*द्रोपदी री लाज राखी, आप बढ़ायो चीर।*\n*भगत कारण रूप नरहरि, धर्यो आप सरीर।*\n"
        "*बूढ़तो गजराज राख्यो, काटी कुण्जर पीर।*\n*दासी मीराँ लाल गिरधर, हरो म्हारी भीर॥*")
PAD2 = ("*स्याम म्हाने चाकर राखो जी,*\n*गिरधारी लाला म्हाँने चाकर राखोजी।*\n*चाकर रहस्यूँ बाग लगास्यूँ नित उठ दरसण पास्यूँ।*\n"
        "*बिन्दरावन री कुंज गली में, गोविन्द लीला गास्यूँ।*\n*चाकरी में दरसण पास्यूँ, सुमरण पास्यूँ खरची।*\n*भाव भगती जागीरी पास्यूँ, तीनूं बाताँ सरसी।*\n"
        "*मोर मुगट पीताम्बर सौहे, गल वैजन्ती माला।*\n*बिन्दरावन में धेनु चरावे, मोहन मुरली वाला।*\n*ऊँचा ऊँचा महल बणावं बिच बिच राखूँ बारी।*\n"
        "*साँवरिया रा दरसण पास्यूँ, पहर कुसुम्बी साड़ी।*\n*आधी रात प्रभु दरसण, दीज्यो जमनाजी रे तीर।*\n*मीराँ रा प्रभु गिरधर नागर, हिवड़ो घणो अधीर॥*")

MEANING = ("| Lines | Meaning |\n|---|---|\n"
           "| **हरि आप हरो जन री भीर** | O Hari, you remove the suffering of your devotees. |\n"
           "| **द्रोपदी री लाज राखी** | You saved Draupadi's honour by lengthening her sari in the Kaurava court. |\n"
           "| **भगत कारण रूप नरहरि** | For your devotee Prahlad you took the form of Narsingh (half man, half lion). |\n"
           "| **बूढ़तो गजराज राख्यो** | You saved the drowning king of elephants (Gajraj) from the crocodile and ended his pain. |\n"
           "| **दासी मीराँ लाल गिरधर** | Meera, your servant, prays: O Giridhar, remove my suffering too. |\n"
           "| **स्याम म्हाने चाकर राखो जी** | O Shyam, keep me as your servant. |\n"
           "| **चाकर रहस्यूँ बाग लगास्यूँ** | As your servant I will plant a garden, rise daily for your darshan, and sing your leela in the lanes of Vrindavan. |\n"
           "| **चाकरी में दरसण पास्यूँ** | In this service I will get three things: darshan (as salary), remembrance (as pocket money) and devotion (as an estate, jagir). |\n"
           "| **मोर मुगट पीताम्बर सौहे** | Krishna wears a peacock-feather crown, a yellow garment and a Vaijayanti garland; he grazes cows in Vrindavan and plays the flute. |\n"
           "| **ऊँचा ऊँचा महल बणावं** | I will build tall palaces with windows in between, and wearing a saffron (kusumbi) sari I will see my dark lord. |\n"
           "| **आधी रात प्रभु दरसण** | O Lord, give me darshan at midnight on the bank of the Yamuna; Meera's heart is very restless. |")

sections = [
 {"id": "s1", "title": "The princess who chose Krishna", "blocks": [
  blk("s1.hook", "hook", title="A queen who wanted to be a servant",
    body="Meera was born into a royal family and married into another, yet she said she wanted only one job: to be **Krishna's servant**. In return she asked for no money, only the chance to see him, remember him and love him.\n\n"
         "In this chapter you read **two pads** (devotional songs). In the first she begs Hari to remove her pain, as he did for his other devotees. In the second she asks to serve him in Vrindavan."),
  blk("s1.inspiration", "inspiration", title="The poet", person="Meera", years="16th century",
    body="**Meerabai** is one of the best-loved poets of the **Bhakti movement**. According to tradition she was born in **Rajasthan** (Kudki, near Merta) and was married into the royal family of **Mewar**. She lost her husband early, left palace life against family opposition, and gave her whole life to **Krishna (Giridhar Gopal)**, whom she saw as her beloved and husband.\n\n"
         "Tradition calls **Sant Raidas** her guru. She spent her later years in **Vrindavan** and **Dwarka**. Her pads are written in **Rajasthani mixed with Braj and Gujarati**, and are still sung across India.",
    future="Meera's courage to follow her faith against social pressure inspires people even today."),
  C.socratic("s1.socratic", "Why does Meera want to be Krishna's servant (चाकर)?",
    ["Service lets her see him daily, remember him and love him", "She needs a salary", "Her family asked her to"], 0,
    "She gets darshan, remembrance and devotion in return."),
 ]},
 {"id": "s2", "title": "The two pads and their meaning", "blocks": [
  blk("s2.poem", "theory", title="पद 1", body=PAD1),
  blk("s2.poem2", "theory", title="पद 2", body=PAD2),
  blk("s2.table", "markdown_table", title="Meaning, line by line", revision=True, body=MEANING),
  C.kc("s2.check", "In the first pad, how did Hari save Draupadi?",
    [("by lengthening her sari", ""), ("by killing Duryodhana", "He protected her honour."), ("by taking the form of Narsingh", "That was for Prahlad."), ("by saving her from a crocodile", "That was Gajraj.")],
    "'आप बढ़ायो चीर'.")
  ,C.kc("s2.check2", "What three things will Meera 'earn' as Krishna's servant?",
    [("darshan, remembrance and devotion", ""), ("money, land and jewels", "She wants spiritual rewards."), ("a palace, a garden and cows", "These are things she will do or see."), ("fame, power and respect", "Spiritual rewards.")],
    "'तीनूं बाताँ सरसी'.")
 ]},
 {"id": "s3", "title": "Meera's devotion", "blocks": [
  blk("s3.thm", "theory", title="What the pads show", revision=True,
    body="**Faith through examples:** in the first pad Meera recalls three times Hari rescued devotees: he lengthened **Draupadi's** sari, became **Narsingh** to save **Prahlad**, and saved the drowning **Gajraj** from a crocodile. Since he saved them, she asks him to remove her pain too.\n\n"
         "**Servant-devotion (दास्य भक्ति):** in the second pad she asks to be his **चाकर** (servant). She will plant a garden, rise daily to see him and sing his leela in Vrindavan's lanes.\n\n"
         "**Three rewards:** her salary will be **darshan**, her pocket money (**खरची**) will be **remembrance (सुमरण)**, and her estate (**जागीरी**) will be **devotion (भाव-भगती)**.\n\n"
         "**Krishna's beauty:** peacock-feather crown (**मोर मुकुट**), yellow garment (**पीतांबर**), **Vaijayanti** garland, grazing cows in Vrindavan, playing the **flute**.\n\n"
         "**Longing:** she will build tall palaces with windows, wear a **kusumbi** (saffron-red) sari, and wait at midnight on the **Yamuna** bank; her heart is **very restless (घणो अधीर)**.\n\n"
         "**Type of devotion:** **सगुण भक्ति** (God with form) towards Krishna, with the feeling of a servant and a beloved."),
  C.kc("s3.check", "'सुमरण पास्यूँ खरची' means Meera will get:",
    [("remembrance of God as her pocket money", ""), ("money to spend", "It is a metaphor."), ("food for the journey", "It is remembrance."), ("a salary in gold", "It is remembrance.")],
    "खरची = pocket money.")
  ,C.kc("s3.check2", "Where does Meera ask Krishna to give her darshan at midnight?",
    [("on the bank of the Yamuna", ""), ("in the palace", "On the Yamuna bank."), ("in Dwarka", "On the Yamuna bank."), ("in a temple", "On the Yamuna bank.")],
    "'दीज्यो जमनाजी रे तीर'.")
 ]},
 {"id": "s4", "title": "Language and style", "blocks": [
  blk("s4.thm", "theory", title="Language, form and devices", revision=True,
    body="| Feature | Example / note |\n|---|---|\n| **Language** | **राजस्थानी** mixed with **ब्रज** and **गुजराती**; simple and sweet (*री* = की, *म्हाने* = मुझे, *पास्यूँ* = पाऊँगी) |\n"
         "| **Form** | **गेय पद** (songs meant to be sung), with rhyme (*भीर, चीर, सरीर, पीर*) |\n| **Quality** | **माधुर्य गुण** (sweetness) and **दास्य भाव** |\n"
         "| **दृष्टांत (illustration)** | Draupadi, Narsingh, Gajraj as proof of Hari's kindness |\n| **रूपक (metaphor)** | 'भाव भगती जागीरी' = devotion as an estate |\n"
         "| **अनुप्रास (alliteration)** | 'हरि आप हरो', 'मोर मुगट', 'मोहन मुरली' |\n| **पुनरुक्ति प्रकाश (repetition)** | 'ऊँचा ऊँचा', 'बिच बिच' |\n\n"
         "**Common forms:** *भीर* = पीड़ा, *चीर* = वस्त्र, *बूढ़ता* = डूबता, *धर्यो* = धारण किया, *कुण्जर* = हाथी, *घणा* = बहुत, *बिन्दरावन* = वृंदावन, *सरसी* = अच्छी, *रहस्यूँ* = रहूँगी, *हिवड़ा* = हृदय, *राखो* = रखो, *कुसुम्बी* = केसरिया।"),
  C.kc("s4.check", "Meera's pads are mainly in:",
    [("Rajasthani mixed with Braj and Gujarati", ""), ("pure Sanskrit", "Rajasthani mix."), ("Awadhi only", "Rajasthani mix."), ("Khari Boli", "Rajasthani mix.")],
    "Simple and sweet.")
 ]},
 closing(C,
   "- **Pad 1 = three rescues: Draupadi (चीर), Prahlad (नरहरि), Gajraj (कुण्जर पीर).**\n- **Pad 2 = चाकर: दरसण (salary), सुमरण (खरची), भाव-भगती (जागीरी).**\n- **Krishna: मोर मुकुट, पीतांबर, वैजंती माला, मुरली.**",
   "1. Writing that Narsingh saved Draupadi: Narsingh saved **Prahlad**; Draupadi's sari was lengthened.\n2. Taking 'चाकर' as a paid servant: Meera wants **spiritual rewards**, not money.\n"
   "3. Mixing up 'भीर' (pain) with 'भीड़' (crowd).\n4. Writing exam answers in English: answer in **Hindi**.",
   "Students sing one pad, then each picks one Rajasthani word and gives its common Hindi form.",
   "Is there something you love so much that you would do it without any reward? How is it like Meera's devotion?",
   "- **Kabir's sakhis (Ch 1):** Kabir's God is formless and within; Meera's Krishna has form and beauty.\n- **Mahabharata and Bhagavata stories:** Draupadi, Prahlad and Gajendra.",
   "Compare the request Meera makes in the first pad with the one in the second pad, in about 60 words.",
   "In the first pad Meera asks Hari to remove her suffering, reminding him that he saved Draupadi, Prahlad and the elephant Gajraj. In the second pad she asks to become Krishna's servant, so that she can see him every day, remember him and love him. The first is a plea for rescue; the second is a wish for lifelong service and nearness to her Lord.",
   "- Meera, a Bhakti poet devoted to Krishna, wrote singable pads in Rajasthani mixed with Braj and Gujarati.\n- Pad 1: she asks Hari to remove her pain, recalling how he saved Draupadi, Prahlad and Gajraj.\n"
   "- Pad 2: she asks to be his servant, earning darshan, remembrance and devotion; she describes his beauty and longs to meet him at the Yamuna.\n- Her devotion is saguna, with the feeling of a servant (दास्य).",
   "- Answer in Hindi, in 25-30 words for 2 marks.\n- Name all three rescues for Pad 1.\n- For काव्य-सौंदर्य, write both भाव-पक्ष (idea) and शिल्प-पक्ष (language, device).",
   [("Whom did Hari save in Pad 1?", "Draupadi (lengthened her sari), Prahlad (as Narsingh), and the drowning Gajraj."),
    ("What are Meera's three rewards for service?", "Darshan, remembrance (सुमरण) and devotion (भाव-भगती).")]),
]

# ---------------- NCERT प्रश्न-अभ्यास (क) ----------------
C.two("pa1", PLEA, "How has Meera asked Hari to remove her suffering in the first pad?",
      ["She reminds Hari that he saved Draupadi's honour, took the Narsingh form for Prahlad, and saved the drowning Gajraj.", "In the same way, as his servant, she begs him to remove her pain."], PE(1))
C.two("pa2", SERVE, "Why does Meerabai want to serve Shyam in the second pad? Explain.",
      ["As his servant she can see him every day and sing his leela in Vrindavan.", "In return she will get darshan, remembrance and devotion, which are dearer to her than anything."], PE(2))
C.two("pa3", BEAUTY, "How has Meerabai described Shri Krishna's beauty?",
      ["Krishna wears a peacock-feather crown, a yellow garment and a Vaijayanti garland around his neck.", "He grazes cows in Vrindavan and plays the flute, looking very charming."], PE(3))
C.two("pa4", LANG, "Throw light on Meerabai's language and style.",
      ["Her language is Rajasthani mixed with Braj and Gujarati; it is simple, sweet and full of feeling.", "Her pads are singable, use rhyme and devices such as illustration, metaphor and alliteration."], PE(4))
C.two("pa5", SERVE, "What is Meera ready to do to attain Shri Krishna?",
      ["She is ready to be his servant, plant gardens, rise daily for darshan and sing his leela in Vrindavan.", "She will build tall palaces with windows, wear a kusumbi sari and wait for him at midnight on the Yamuna bank."], PE(5))
# ---------------- NCERT (ख) काव्य-सौंदर्य ----------------
C.two("ks1", PLEA, "Explain the poetic beauty: 'हरि आप हरो जन री भीर। द्रोपदी री लाज राखी, आप बढ़ायो चीर। भगत कारण रूप नरहरि, धर्यो आप सरीर।'",
      ["Idea: Meera says Hari removes his devotees' pain; he lengthened Draupadi's sari and took the Narsingh form for Prahlad.", "Craft: Rajasthani-Braj language, illustration (दृष्टांत) device, alliteration in 'हरि आप हरो', and singable rhyme."], KS(1))
C.two("ks2", PLEA, "Explain the poetic beauty: 'बूढ़तो गजराज राख्यो, काटी कुण्जर पीर। दासी मीराँ लाल गिरधर, हरो म्हारी भीर।'",
      ["Idea: Hari saved the drowning elephant king and ended his pain; Meera, his servant, asks him to remove her pain too.", "Craft: Rajasthani language, servant-devotion (दास्य भाव), illustration device and rhyme (पीर-भीर)."], KS(2))
C.two("ks3", SERVE, "Explain the poetic beauty: 'चाकरी में दरसण पास्यूँ, सुमरण पास्यूँ खरची। भाव भगती जागीरी पास्यूँ, तीनूं बाताँ सरसी।'",
      ["Idea: as Krishna's servant Meera will get darshan, remembrance as pocket money and devotion as an estate; all three are good for her.", "Craft: metaphor (रूपक) in 'भाव भगती जागीरी', Rajasthani language and alliteration in 'पास्यूँ'."], KS(3))
C.two("bhasha", LANG, "Write the common Hindi forms of these words from the text: चीर, बूढ़ता, धर्यो, कुण्जर, बिन्दरावन, हिवड़ा.",
      ["चीर = वस्त्र, बूढ़ता = डूबता, धर्यो = धारण किया.", "कुण्जर = हाथी, बिन्दरावन = वृंदावन, हिवड़ा = हृदय."], ex(1, "भाषा-अध्ययन"))

C.two("bhasha2", LANG, "Write the common Hindi forms of these words from the text: लगास्यूँ, घणा, सरसी, रहस्यूँ, राखो, कुसुम्बी.",
      ["लगास्यूँ = लगाऊँगी, घणा = बहुत, सरसी = अच्छी.", "रहस्यूँ = रहूँगी, राखो = रखो, कुसुम्बी = केसरिया (लाल)."], ex(1, "भाषा-अध्ययन"))

# ---------------- Extracts ----------------
C.extract("ext1", PLEA, "हरि आप हरो जन री भीर।\nद्रोपदी री लाज राखी, आप बढ़ायो चीर।\nभगत कारण रूप नरहरि, धर्यो आप सरीर।",
  [("What does Meera ask Hari to do?", "To remove the suffering of his devotees."), ("How did Hari save Draupadi's honour?", "By lengthening her sari."),
   ("What does 'नरहरि' mean?", "Narsingh, the half-man half-lion form."), ("For whom did Hari take that form?", "For his devotee Prahlad."), ("What does 'भीर' mean?", "Suffering, pain.")])
C.extract("ext2", BEAUTY + SERVE, "मोर मुगट पीताम्बर सौहे, गल वैजन्ती माला।\nबिन्दरावन में धेनु चरावे, मोहन मुरली वाला।",
  [("What does Krishna wear on his head?", "A crown of peacock feathers."), ("What is 'पीताम्बर'?", "A yellow garment."),
   ("Which garland does he wear?", "The Vaijayanti garland."), ("What does he do in Vrindavan?", "He grazes cows."), ("Name the device in 'मोहन मुरली'.", "Alliteration (अनुप्रास).")])

# ---------------- Objective practice ----------------
C.m("mcq01", PLEA, "'भीर' in the first pad means:", [("suffering", ""), ("crowd", "That is भीड़."), ("fear", "Suffering."), ("devotee", "Suffering.")], "'हरो जन री भीर'.")
C.m("mcq02", PLEA, "Whose honour did Hari save by lengthening the sari?", [("Draupadi", ""), ("Sita", "Draupadi."), ("Radha", "Draupadi."), ("Meera", "Draupadi.")], "'द्रोपदी री लाज राखी'.")
C.m("mcq03", PLEA, "Hari took the Narsingh form to save:", [("Prahlad", ""), ("Draupadi", "Prahlad."), ("Gajraj", "Prahlad."), ("Sudama", "Prahlad.")], "'भगत कारण रूप नरहरि'.")
C.m("mcq04", PLEA, "'कुण्जर' means:", [("elephant", ""), ("crocodile", "Elephant."), ("lion", "Elephant."), ("garden", "Elephant.")], "Gajraj, the elephant king.")
C.m("mcq05", PLEA, "'बूढ़तो' means:", [("drowning", ""), ("old", "Here it means drowning."), ("running", "Drowning."), ("sleeping", "Drowning.")], "'बूढ़तो गजराज राख्यो'.")
C.m("mcq06", SERVE, "Meera asks Krishna to keep her as his:", [("servant (चाकर)", ""), ("queen", "Servant."), ("teacher", "Servant."), ("guard", "Servant.")], "'म्हाने चाकर राखो जी'.")
C.m("mcq07", SERVE, "Where will Meera sing Govind's leela?", [("in the lanes of Vrindavan", ""), ("in the royal court", "In Vrindavan."), ("in Dwarka", "In Vrindavan."), ("on the Ganga bank", "In Vrindavan.")], "'बिन्दरावन री कुंज गली में'.")
C.m("mcq08", SERVE, "In 'भाव भगती जागीरी', devotion is compared to:", [("an estate (jagir)", ""), ("a salary", "An estate."), ("pocket money", "That is remembrance."), ("a garden", "An estate.")], "Metaphor (रूपक).")
C.m("mcq09", SERVE, "'खरची' means:", [("pocket money", ""), ("expense on travel", "Pocket money."), ("debt", "Pocket money."), ("prize", "Pocket money.")], "Remembrance will be her pocket money.")
C.m("mcq10", BEAUTY, "Krishna's crown is made of:", [("peacock feathers", ""), ("gold", "Peacock feathers."), ("flowers", "Peacock feathers."), ("pearls", "Peacock feathers.")], "'मोर मुगट'.")
C.m("mcq11", BEAUTY, "'पीताम्बर' is a garment of which colour?", [("yellow", ""), ("blue", "Yellow."), ("red", "Yellow."), ("white", "Yellow.")], "पीत = yellow.")
C.m("mcq12", SERVE, "Which sari will Meera wear to see Krishna?", [("a kusumbi (saffron-red) sari", ""), ("a white sari", "Kusumbi."), ("a silk sari", "Kusumbi."), ("a blue sari", "Kusumbi.")], "'पहर कुसुम्बी साड़ी'.")
C.m("mcq13", SERVE, "When and where does Meera ask for darshan?", [("at midnight on the Yamuna bank", ""), ("at dawn in a temple", "Midnight, Yamuna."), ("at noon in Vrindavan", "Midnight, Yamuna."), ("in the evening in Dwarka", "Midnight, Yamuna.")], "'आधी रात ... जमनाजी रे तीर'.")
C.m("mcq14", LANG, "'हिवड़ो घणो अधीर' means:", [("the heart is very restless", ""), ("the body is very tired", "Heart, restless."), ("the mind is calm", "Opposite."), ("the eyes are full of tears", "Heart, restless.")], "हिवड़ो = heart, घणो = very.")
C.m("mcq15", LANG, "Meera's pads are mainly in:", [("Rajasthani", ""), ("Awadhi", "Rajasthani."), ("Bhojpuri", "Rajasthani."), ("Maithili", "Rajasthani.")], "Mixed with Braj and Gujarati.")
C.m("mcq16", LANG, "Meera's devotion is towards:", [("Krishna (Giridhar)", ""), ("Rama", "Krishna."), ("Shiva", "Krishna."), ("a formless God", "That is Kabir.")], "'मीराँ रा प्रभु गिरधर नागर'.")
C.m("mcq17", LANG, "The device in 'ऊँचा ऊँचा' and 'बिच बिच' is:", [("पुनरुक्ति प्रकाश", ""), ("उपमा", "Repetition of a word."), ("रूपक", "Repetition."), ("मानवीकरण", "Repetition.")], "A word is repeated.")
C.m("mcq18", LANG, "Meera's devotion is mainly:", [("दास्य भाव (as a servant)", ""), ("सख्य भाव (as a friend)", "As a servant (and beloved)."), ("वात्सल्य भाव (as a parent)", "As a servant."), ("निर्गुण भक्ति", "Krishna has form; saguna.")], "'दासी मीराँ'.")
C.m("mcq19", PLEA, "The device in the first pad, using three past rescues as proof, is:", [("दृष्टांत", ""), ("यमक", "Illustration."), ("श्लेष", "Illustration."), ("उत्प्रेक्षा", "Illustration.")], "Examples prove Hari's kindness.")
C.m("mcq20", LANG, "Meera's pads are best described as:", [("गेय पद (songs to be sung)", ""), ("दोहे", "They are pads."), ("चौपाई", "They are pads."), ("मुक्त छंद", "They are pads.")], "Sung across India.")
C.tf("tf1", PLEA, "In the first pad, Hari saved Gajraj from a lion.", False, "From a crocodile, in the water.")
C.tf("tf2", SERVE, "Meera wants money as a reward for serving Krishna.", False, "She wants darshan, remembrance and devotion.")
C.tf("tf3", BEAUTY, "Krishna wears a Vaijayanti garland around his neck.", True, "'गल वैजन्ती माला'.")
C.tf("tf4", SERVE, "Meera will build tall palaces with windows in between.", True, "'बिच बिच राखूँ बारी'.")
C.tf("tf5", LANG, "Meera's language is pure Sanskrit.", False, "Rajasthani mixed with Braj and Gujarati.")
C.tf("tf6", PLEA, "Meera calls herself Giridhar's servant (दासी).", True, "'दासी मीराँ लाल गिरधर'.")
C.two("sa1", SERVE, "Why does Meera say 'तीनूं बाताँ सरसी'?",
      ["As Krishna's servant she will get darshan, remembrance and devotion.", "All three are what she loves most, so service is profitable for her in every way."])
C.two("sa2", PLEA, "Why does Meera mention Draupadi, Prahlad and Gajraj in her prayer?",
      ["These examples show that Hari always helps his devotees in trouble.", "So she is confident he will remove her suffering as well."])

C.two("sa3", LANG, "How is Meera's devotion different from Kabir's?",
      ["Kabir worships a formless God who lives within every heart (निर्गुण भक्ति).", "Meera worships Krishna with form and beauty, as his servant and beloved (सगुण भक्ति)."], difficulty="medium")
C.two("sa4", SERVE, "Why does Meera want to see Krishna at midnight on the Yamuna bank?",
      ["Her heart is very restless with longing to meet her Lord.", "The Yamuna bank in Vrindavan is the place of Krishna's leela, and midnight is quiet for a private meeting."], difficulty="medium")

chapter = header("sparsh", "ch02", 2, "पद", "मीराबाई", "poem", ["plea_to_hari", "servant_devotion", "krishna_beauty", "meera_language"],
                 "CBSE 2025-26 Hindi Course B (085), Section C: Sparsh Part 2 poetry. Assessed through extract-based MCQs (1 mark each) and short answers in 25-30 words (2 marks); answers are written in Hindi.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
