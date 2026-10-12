"""CBSE Class 10 Hindi Course B, Sparsh Part 2, Ch 4: पर्वत प्रदेश में पावस (Sumitranandan Pant).
The poem is in copyright, so the lesson summarises it stanza by stanza and quotes only short phrases; students read it in NCERT."""
import sys
from hindi_common import make, header, path, ex
from lit_common import closing

ROOT = sys.argv[1]
PATH = path("sparsh", "ch04_parvat_pradesh_mein_pavas")
C = make("hsp10ch04")
blk = C.blk
CHANGE, MOUNT, CLOUD, CRAFT = ["changing_nature"], ["mountain_lake_falls"], ["clouds_illusion"], ["pant_imagery"]
PE = lambda n: ex(n)
BH = lambda n: ex(n, "भाव स्पष्ट कीजिए")
KS = lambda n: ex(n, "कविता का सौंदर्य")

STANZAS = ("| Part of the poem | What the poet shows |\n|---|---|\n"
           "| **Opening** (*'पावस ऋतु थी, पर्वत प्रदेश'*) | It is the rainy season in the hills, and nature's dress changes every moment (*पल-पल परिवर्तित प्रकृति-वेश*). |\n"
           "| **The mountain** (*'मेखलाकार पर्वत अपार'*) | A huge, girdle-shaped range seems to open its thousands of flower-eyes and look again and again at its own giant reflection in the water below. |\n"
           "| **The lake** | The lake that lies at the mountain's feet spreads out like a vast **mirror** (*दर्पण-सा*). |\n"
           "| **The waterfalls** | Foaming falls rush down singing the glory of the mountain; they look like **strings of pearls** (*मोती की लड़ियों-से*). |\n"
           "| **The tall trees** | Trees rise from the mountain's heart and gaze at the silent sky, unblinking and steady, as if full of high ambition and a little worried. |\n"
           "| **Sudden clouds** | Suddenly the mountain seems to fly away on shining wings of mercury (*पारद के पर*); only the sound of the falls is left; the sky seems to crash down on the earth. |\n"
           "| **Fear and mist** | The sal trees seem to sink into the earth in fear; mist rises from the lake as if it is on fire (*जल गया ताल*). |\n"
           "| **Closing image** | In this way Indra, travelling in his cloud-chariot, seems to be playing a magic show (*इंद्रजाल*). |")

sections = [
 {"id": "s1", "title": "A magic show in the hills", "blocks": [
  blk("s1.hook", "hook", title="Now you see it, now you don't",
    body="Stand in the hills during the monsoon. One moment a mountain is reflected in a lake; the next, clouds swallow it and it seems to have **flown away**. Then heavy rain makes it look as if **the sky has fallen on the earth**.\n\n"
         "**Sumitranandan Pant** paints this changing scene in words, giving feelings to mountains, trees and lakes. He ends by calling it a **magic show of Indra**, the god of rain."),
  blk("s1.inspiration", "inspiration", title="The poet", person="Sumitranandan Pant", years="1900–1977",
    body="**Sumitranandan Pant** was born in **Kausani** in the Almora district of the Kumaon hills (now Uttarakhand). He was one of the four pillars of **छायावाद** (Chhayavad), along with Prasad, Nirala and Mahadevi Verma, and is called the **'प्रकृति का सुकुमार कवि'** (tender poet of nature).\n\n"
         "His works include **वीणा**, **पल्लव**, **गुंजन**, **ग्राम्या** and **चिदंबरा**. He received the **Jnanpith Award** for चिदंबरा and the **Padma Bhushan**.",
    future="Pant shows how close observation of nature can become poetry; try describing a rainy day you have seen in the same way."),
  C.socratic("s1.socratic", "Why does the poet call the scene 'इंद्रजाल' (Indra's magic)?",
    ["Because the scene keeps changing suddenly, like a magic show", "Because Indra appears in person", "Because it is a dream"], 0,
    "Clouds make mountains vanish and reappear.")
 ]},
 {"id": "s2", "title": "The poem, part by part", "blocks": [
  blk("s2.note", "theory", title="How to read this chapter",
    body="Read the full poem in your **NCERT Sparsh Part 2** textbook. The table below explains each part of the poem, with key phrases quoted so you can find them."),
  blk("s2.table", "markdown_table", title="What happens in the poem", revision=True, body=STANZAS),
  C.kc("s2.check", "To what has the poet compared the lake?",
    [("a mirror", ""), ("a sea", "A mirror."), ("a pearl", "The falls are like pearls."), ("a cloud", "A mirror.")],
    "'दर्पण-सा फैला है विशाल'.")
  ,C.kc("s2.check2", "Why does the mountain seem to fly away?",
    [("dense clouds cover it completely", ""), ("an earthquake moves it", "It is the clouds."), ("it is a dream", "It is the clouds."), ("the wind blows it", "Clouds hide it.")],
    "'उड़ गया, अचानक लो, भूधर'.")
 ]},
 {"id": "s3", "title": "Nature with human feelings", "blocks": [
  blk("s3.thm", "theory", title="Ideas in the poem", revision=True,
    body="**Ever-changing nature:** in the rainy season the hills change every moment: sun, cloud, rain and mist follow each other.\n\n"
         "**The mountain admires itself:** its flowers are like thousands of eyes (**सहस्र दृग-सुमन**) looking at its reflection in the lake, as a person looks into a mirror.\n\n"
         "**The falls sing:** the waterfalls sing the mountain's glory, filling every vein with excitement; their foam looks like strings of pearls.\n\n"
         "**The trees dream:** tall trees look at the sky **unblinking (अनिमेष)**, **steady (अटल)** and **thoughtful (चिंतापर)**; they reflect **high ambitions (उच्चाकांक्षाएँ)** of human beings.\n\n"
         "**The sudden storm:** clouds hide the mountain; only the sound of the falls remains; heavy rain makes it seem the sky has fallen; the sal trees seem to sink in fear; mist rises like smoke from the lake.\n\n"
         "**Indra's magic:** the whole changing scene is like Indra playing a magic trick from his chariot of clouds (**जलद-यान**)."),
  C.kc("s3.check", "What do the tall trees looking at the sky reflect?",
    [("human beings' high ambitions", ""), ("fear of the storm", "Ambition."), ("the poet's sadness", "Ambition."), ("love for the lake", "Ambition.")],
    "'उच्चाकांक्षाओं से तरुवर'.")
  ,C.kc("s3.check2", "Why do the sal trees seem to sink into the earth?",
    [("they are hidden by dense clouds and appear to vanish in fear", ""), ("they are cut down", "It is an image."), ("an earthquake swallows them", "It is the clouds."), ("they are very old", "The clouds hide them.")],
    "'धँस गए धरा में सभय शाल'.")
 ]},
 {"id": "s4", "title": "Language and style", "blocks": [
  blk("s4.thm", "theory", title="Language and devices", revision=True,
    body="| Feature | Example / note |\n|---|---|\n| **Language** | **खड़ी बोली**, rich in **तत्सम** words: *मेखलाकार, सहस्र, दृग, अनिमेष, भूधर, पारद, जलद* |\n"
         "| **मानवीकरण (personification)** | the mountain looks at itself; falls sing; trees gaze with ambition; sal trees are afraid |\n"
         "| **उपमा (simile)** | *दर्पण-सा* (lake like a mirror), *मोती की लड़ियों-से* (falls like strings of pearls) |\n"
         "| **रूपक (metaphor)** | *दृग-सुमन* (flower-eyes), *जलद-यान* (cloud-chariot) |\n"
         "| **अनुप्रास (alliteration)** | *पावस ऋतु थी, पर्वत प्रदेश, पल-पल परिवर्तित प्रकृति-वेश* |\n"
         "| **पुनरुक्ति प्रकाश** | *पल-पल, बार-बार, झर-झर, उठ-उठ, विचर-विचर* |\n| **अतिशयोक्ति (hyperbole)** | *है टूट पड़ा भू पर अंबर* |\n\n"
         "**Style:** **चित्रात्मक** (picture-like) and **संगीतात्मक** (musical); a typical **छायावादी** nature poem."),
  C.kc("s4.check", "Which device is used most in this poem?",
    [("मानवीकरण (personification)", ""), ("यमक", "Personification."), ("श्लेष", "Personification."), ("दृष्टांत", "Personification.")],
    "Nature is given human actions and feelings.")
 ]},
 closing(C,
   "- **Order: पर्वत (दर्पण में) → ताल (दर्पण) → झरने (मोती) → तरुवर (उच्चाकांक्षा) → बादल (भूधर उड़ा) → शाल (सभय) → इंद्रजाल.**\n- **Devices: मानवीकरण, उपमा, रूपक, अनुप्रास, पुनरुक्ति, अतिशयोक्ति.**\n- **Pant = प्रकृति का सुकुमार कवि, छायावाद.**",
   "1. Writing that the mountain really flew: it is **hidden by clouds**.\n2. Writing that the lake caught fire: **mist rising** looks like smoke.\n"
   "3. Calling the falls a mirror: the **lake** is the mirror; the falls are like **pearls**.\n4. Writing exam answers in English: answer in **Hindi**.",
   "Show a time-lapse video of clouds over hills, then ask students to match each scene to a line of the poem.",
   "Recall a rainy day you saw. Which line of this poem describes what you saw best?",
   "- **Geography:** monsoon and relief rainfall in the Himalayas.\n- **Chhayavad:** Prasad, Nirala and Mahadevi Verma also wrote on nature.",
   "How has Pant given human feelings to nature in 'पर्वत प्रदेश में पावस'? Answer in about 60 words.",
   "Pant uses personification throughout. The mountain looks at its own reflection in the lake through thousands of flower-eyes. The waterfalls sing the mountain's glory. Tall trees gaze at the sky with high ambitions, steady and thoughtful. When clouds come, the sal trees seem to sink into the earth in fear. In this way nature appears alive, with eyes, voice, hopes and fear.",
   "- Sumitranandan Pant, the Chhayavad poet of nature, describes the hills in the rainy season.\n- The mountain sees itself in the mirror-like lake; falls like pearls sing its glory; trees look up with ambition.\n"
   "- Suddenly clouds hide the mountain, rain pours as if the sky fell, sal trees seem to sink in fear, mist rises from the lake.\n- The changing scene is Indra's magic show from his cloud-chariot.",
   "- Answer in Hindi, in 25-30 words for 2 marks.\n- Name the device and quote the phrase as proof.\n- Explain images (दर्पण, मोती, इंद्रजाल) in plain words.",
   [("To what are the lake and the falls compared?", "The lake to a mirror; the falls to strings of pearls."),
    ("What is 'इंद्रजाल' here?", "The magic-like changing scene created by Indra in his cloud-chariot.")]),
]

# ---------------- NCERT प्रश्न-अभ्यास (क) ----------------
C.two("pa1", CHANGE, "What changes come in nature during the rainy season? Explain on the basis of the poem.",
      ["Nature changes every moment: the mountain shows in the lake, falls rush down and trees stand tall.", "Suddenly clouds hide the mountain, heavy rain falls as if the sky has dropped, and mist rises from the lake."], PE(1))
C.two("pa2", MOUNT, "What does 'मेखलाकार' mean? Why has the poet used this word here?",
      ["मेखलाकार means shaped like a girdle (करधनी), circling round.", "The poet uses it because the mountain range stretches in a curve around the land like a girdle."], PE(2))
C.two("pa3", MOUNT, "What is meant by 'सहस्र दृग-सुमन'? For what has the poet used this phrase?",
      ["It means thousands of flowers like eyes.", "The poet uses it for the flowers blooming on the mountain, through which it seems to look at its own reflection."], PE(3))
C.two("pa4", MOUNT, "With what has the poet compared the lake, and why?",
      ["The poet has compared the lake to a mirror.", "Its water is clear and still, and the mountain sees its huge form reflected in it."], PE(4))
C.two("pa5", MOUNT, "Why were the tall trees rising from the mountain's heart looking at the sky, and what do they reflect?",
      ["They look up at the silent sky, steady and thoughtful, as if they want to reach it.", "They reflect the high ambitions of human beings, who also want to rise higher."], PE(5), "medium")
C.two("pa6", CLOUD, "Why did the sal trees sink into the earth in fear?",
      ["Dense clouds came down and covered the sal trees, so they could not be seen.", "It looked as if they had sunk into the earth in fear of the sudden storm."], PE(6))
C.two("pa7", MOUNT, "Whose glory are the waterfalls singing? With what has the flowing waterfall been compared?",
      ["The waterfalls are singing the glory of the mountain.", "The foaming waterfall has been compared to strings of pearls."], PE(7))
# ---------------- NCERT (ख) भाव ----------------
C.two("bh1", CLOUD, "Explain the idea: 'है टूट पड़ा भू पर अंबर'.",
      ["The rain is so heavy and the clouds so low that it seems the sky has broken and fallen on the earth.", "It shows the force of the sudden rain in the hills."], BH(1))
C.two("bh2", CLOUD, "Explain the idea: '—यों जलद-यान में विचर-विचर था इंद्र खेलता इंद्रजाल'.",
      ["The rapidly changing scene of cloud, rain and mist looks like magic.", "It seems Indra, the rain god, is moving in his cloud-chariot and playing a magic show."], BH(2))
C.two("bh3", MOUNT, "Explain the idea: 'गिरिवर के उर से उठ-उठ कर उच्चाकांक्षाओं से तरुवर हैं झाँक रहे नीरव नभ पर अनिमेष, अटल, कुछ चिंतापर'.",
      ["Tall trees rising from the mountain look at the silent sky without blinking, steady and a little worried.", "They seem full of high ambitions, like people who wish to reach great heights."], BH(3), "medium")
# ---------------- NCERT कविता का सौंदर्य ----------------
C.two("ks1", CRAFT, "How has personification (मानवीकरण) been used in this poem? Explain.",
      ["The mountain looks at its reflection, the falls sing its glory, and the trees gaze at the sky with ambition.", "The sal trees sink in fear; thus nature is shown with human actions and feelings."], KS(1))
C.two("ks2", CRAFT, "In your view, on what does the beauty of this poem depend: repetition of words, picture-like language, or musicality?",
      ["Mainly on the picture-like language, which paints a living scene of the hills in the rain.", "Repetition (पल-पल, झर-झर) and musical rhythm add to that beauty."], KS(2), "medium")
C.two("ks3", CRAFT, "Pick out places where the poet has used the picture-like style to paint the rainy season.",
      ["'मेखलाकार पर्वत अपार' looking at itself in the lake, and 'दर्पण-सा फैला है विशाल'.", "'मोती की लड़ियों-से सुंदर' falls, and 'उठ रहा धुआँ, जल गया ताल'."], KS(3))

# ---------------- Extracts (short quotations) ----------------
C.extract("ext1", CHANGE + CRAFT, "पावस ऋतु थी, पर्वत प्रदेश,\nपल-पल परिवर्तित प्रकृति-वेश।",
  [("Which season is described?", "The rainy season (पावस)."), ("Where is the scene set?", "In the hills (पर्वत प्रदेश)."),
   ("What happens to nature every moment?", "Its appearance (dress) keeps changing."), ("What does 'वेश' mean?", "Dress, appearance."), ("Name the device in these lines.", "Alliteration (अनुप्रास) of 'प'; repetition in 'पल-पल'.")])
C.extract("ext2", CLOUD, "है टूट पड़ा भू पर अंबर!\nधँस गए धरा में सभय शाल!",
  [("What does 'अंबर' mean?", "The sky."), ("Why does the sky seem to fall on the earth?", "Because of very heavy rain and low clouds."),
   ("What happened to the sal trees?", "They seemed to sink into the earth."), ("What does 'सभय' mean?", "Afraid, full of fear."), ("Name a device used here.", "Hyperbole (अतिशयोक्ति) / personification (मानवीकरण).")])

# ---------------- Objective practice ----------------
C.m("mcq01", CHANGE, "'पावस' means:", [("the rainy season", ""), ("spring", "Rainy season."), ("winter", "Rainy season."), ("summer", "Rainy season.")], "The poem is set in the monsoon.")
C.m("mcq02", MOUNT, "'मेखलाकार' means:", [("shaped like a girdle", ""), ("very tall", "Girdle-shaped."), ("covered in snow", "Girdle-shaped."), ("full of trees", "Girdle-shaped.")], "मेखला = करधनी.")
C.m("mcq03", MOUNT, "'सहस्र दृग-सुमन' refers to:", [("thousands of flowers like eyes", ""), ("thousands of stars", "Flowers."), ("raindrops", "Flowers."), ("people's eyes", "The mountain's flowers.")], "The mountain looks through them.")
C.m("mcq04", MOUNT, "The lake has been compared to:", [("a mirror", ""), ("a pearl", "That is the falls."), ("a sea", "A mirror."), ("a sky", "A mirror.")], "'दर्पण-सा'.")
C.m("mcq05", MOUNT, "The waterfalls sing the glory of:", [("the mountain", ""), ("the lake", "The mountain."), ("Indra", "The mountain."), ("the clouds", "The mountain.")], "'गिरि का गौरव गाकर'.")
C.m("mcq06", MOUNT, "The foaming falls look like:", [("strings of pearls", ""), ("silver chains", "Pearls."), ("white clouds", "Pearls."), ("snakes", "Pearls.")], "'मोती की लड़ियों-से सुंदर'.")
C.m("mcq07", MOUNT, "The tall trees look at the sky with:", [("high ambitions", ""), ("anger", "Ambition."), ("joy", "Ambition."), ("sleepiness", "Ambition.")], "'उच्चाकांक्षाओं से तरुवर'.")
C.m("mcq08", MOUNT, "'अनिमेष' means:", [("without blinking", ""), ("without moving", "That is अटल."), ("without sound", "That is नीरव."), ("without fear", "Without blinking.")], "Steady gaze.")
C.m("mcq09", CLOUD, "'भूधर' means:", [("mountain", ""), ("earth", "Mountain."), ("cloud", "Mountain."), ("tree", "Mountain.")], "That which holds the earth.")
C.m("mcq10", CLOUD, "'पारद के पर' refers to:", [("shining wings of mercury (white clouds)", ""), ("bird feathers", "It is an image of clouds."), ("silver coins", "Clouds."), ("lightning", "Clouds.")], "Clouds look like shining wings.")
C.m("mcq11", CLOUD, "After the mountain 'flies away', what is left of the falls?", [("only their sound", ""), ("only their foam", "Only sound."), ("nothing at all", "Sound remains."), ("their colour", "Sound.")], "'रव-शेष रह गए हैं निर्झर'.")
C.m("mcq12", CLOUD, "'जल गया ताल' suggests:", [("mist rising from the lake like smoke", ""), ("the lake really caught fire", "It is an image."), ("the lake dried up", "Mist."), ("lightning hit the lake", "Mist rising.")], "'उठ रहा धुआँ'.")
C.m("mcq13", CLOUD, "'जलद-यान' means:", [("a chariot of clouds", ""), ("a boat on water", "Cloud-chariot."), ("an aeroplane", "Cloud-chariot."), ("a rainbow", "Cloud-chariot.")], "Indra travels in it.")
C.m("mcq14", CLOUD, "'इंद्रजाल' means:", [("magic", ""), ("Indra's net for fishing", "It means magic."), ("lightning", "Magic."), ("rain", "Magic.")], "The changing scene is like magic.")
C.m("mcq15", CRAFT, "Which trees seem to sink into the earth in fear?", [("sal", ""), ("pine", "Sal."), ("banyan", "Sal."), ("mango", "Sal.")], "'धँस गए धरा में सभय शाल'.")
C.m("mcq16", CRAFT, "Sumitranandan Pant belongs to which movement?", [("छायावाद", ""), ("प्रगतिवाद", "Chhayavad."), ("भक्ति काल", "Chhayavad."), ("रीति काल", "Chhayavad.")], "With Prasad, Nirala, Mahadevi.")
C.m("mcq17", CRAFT, "Pant is called:", [("प्रकृति का सुकुमार कवि", ""), ("राष्ट्रकवि", "That was Gupt."), ("महाप्राण", "That was Nirala."), ("आधुनिक मीरा", "That was Mahadevi.")], "Tender poet of nature.")
C.m("mcq18", CRAFT, "Pant was born in:", [("Kausani (Kumaon)", ""), ("Varanasi", "Kausani."), ("Allahabad", "Kausani."), ("Jhansi", "That was Gupt.")], "In the hills he loved.")
C.m("mcq19", CRAFT, "'पल-पल', 'झर-झर', 'उठ-उठ' are examples of:", [("पुनरुक्ति प्रकाश", ""), ("उपमा", "Repetition."), ("रूपक", "Repetition."), ("यमक", "Same meaning, so repetition.")], "Words repeated.")
C.m("mcq20", CRAFT, "'है टूट पड़ा भू पर अंबर' contains:", [("अतिशयोक्ति (hyperbole)", ""), ("उपमा", "Hyperbole."), ("श्लेष", "Hyperbole."), ("दृष्टांत", "Hyperbole.")], "The sky cannot really fall.")
C.tf("tf1", MOUNT, "The poet compares the lake to a mirror.", True, "'दर्पण-सा'.")
C.tf("tf2", CLOUD, "The mountain actually flies away in the storm.", False, "Clouds hide it.")
C.tf("tf3", MOUNT, "The waterfalls are compared to strings of pearls.", True, "'मोती की लड़ियों-से'.")
C.tf("tf4", CRAFT, "Personification is the main device of the poem.", True, "Nature acts and feels like people.")
C.tf("tf5", CLOUD, "The lake really catches fire at the end.", False, "Mist rises like smoke.")
C.tf("tf6", CRAFT, "Pant was a poet of the Bhakti period.", False, "He was a Chhayavad poet.")
C.two("sa1", CHANGE, "Why is 'पल-पल परिवर्तित प्रकृति-वेश' a fitting description of the hills in the rains?",
      ["In the hills, sunshine, clouds, rain and mist change within moments.", "So nature seems to change its dress every moment, as the poem shows."])

chapter = header("sparsh", "ch04", 4, "पर्वत प्रदेश में पावस", "सुमित्रानंदन पंत", "poem", ["changing_nature", "mountain_lake_falls", "clouds_illusion", "pant_imagery"],
                 "CBSE 2025-26 Hindi Course B (085), Section C: Sparsh Part 2 poetry. Assessed through extract-based MCQs (1 mark each) and short answers in 25-30 words (2 marks); answers are written in Hindi. The poem is in copyright: read the full text in the NCERT textbook.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
