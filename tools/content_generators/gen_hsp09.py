"""CBSE Class 10 Hindi Course B, Sparsh Part 2, Ch 9: तीसरी कसम के शिल्पकार शैलेंद्र (Prahlad Agrawal).
The text is in copyright: the lesson retells it, and extract passages are Shine retellings in Hindi."""
import sys
from hindi_common import make, header, path, ex, PROSE_INTRO
from lit_common import closing

ROOT = sys.argv[1]
PATH = path("sparsh", "ch09_teesri_kasam_shailendra")
C = make("hsp10ch09")
blk = C.blk
FILM, SHAIL, RAJ, ART = ["teesri_kasam_film"], ["shailendra_poet_producer"], ["raj_kapoor_actor"], ["art_vs_commerce"]
MO = lambda n: ex(n, "मौखिक")
LK = lambda n: ex(n, "लिखित (क)")
LB = lambda n: ex(n, "लिखित (ख)")
AS = lambda n: ex(n, "आशय स्पष्ट कीजिए")

FACTS = ("| Topic | Key points |\n|---|---|\n"
         "| **The film** | **तीसरी कसम** (1966), based on **Phanishwar Nath Renu's** story **'मारे गए गुलफ़ाम'**. Produced by the lyricist **Shailendra**, his only film. |\n"
         "| **Cast** | **Raj Kapoor** as **Hiraman** (a simple village cart-driver) and **Waheeda Rehman** as **Hirabai** (a nautanki dancer). |\n"
         "| **Awards** | **President's Gold Medal** for the best feature film, the **Bengal Film Journalists' Association** award and other honours; it was also shown at the **Moscow** film festival. |\n"
         "| **Raj Kapoor's help** | Raj Kapoor, Shailendra's close friend, warned him of the risks, then asked for his fee 'in advance'. Shailendra's face fell; Raj laughed and asked for **just one rupee**. |\n"
         "| **No buyers** | Distributors, who think only of profit, could not understand the film's deep feeling, so it found few buyers and failed at the box office. |\n"
         "| **Celluloid poem** | Critics call it **'सैल्यूलाइड पर लिखी कविता'**: it stayed true to Renu's story and showed sorrow without glorifying it. |\n"
         "| **Shailendra the artist** | An idealist, emotional poet who wanted **self-satisfaction more than wealth or fame**. He believed an artist must **refine** people's taste, not feed them shallowness. |\n"
         "| **'दसों दिशाएँ'** | In the *श्री 420* song *'रातें दसों दिशाओं से कहेंगी अपनी कहानियाँ'*, composer **Jaikishan** objected that audiences know only four directions; Shailendra refused to change it. |")

sections = [
 {"id": "s1", "title": "A poet who made one film", "blocks": [
  blk("s1.hook", "hook", title="A film that lost money and won hearts",
    body="In 1966 a famous song-writer put all his savings into one film. It won the top national award, yet distributors did not want it, and it failed at the box office. Today it is called **a poem written on celluloid**.\n\n"
         "This chapter, by **Prahlad Agrawal**, is about **Shailendra** and his film **'तीसरी कसम'**: a story of art against money, and of honesty in creative work."),
  blk("s1.inspiration", "inspiration", title="The writer", person="Prahlad Agrawal", years="born 1947",
    body="**Prahlad Agrawal** was born in **Jabalpur**, Madhya Pradesh. He taught Hindi and is known as a writer on **Hindi cinema**, with books on **Raj Kapoor**, **Shailendra**, **Guru Dutt** and other film-makers.\n\n"
         "**Shailendra** (1923–1966), the subject of this chapter, was one of Hindi cinema's best-loved lyricists, writing simple, deep songs for Raj Kapoor's films.",
    future="This chapter shows that creative work done honestly can last longer than commercial success."),
  C.socratic("s1.socratic", "Why did Shailendra make 'तीसरी कसम' despite the risks?",
    ["He wanted self-satisfaction more than money or fame", "He wanted to become rich", "Raj Kapoor forced him"], 0,
    "He was an idealist poet.")
 ]},
 {"id": "s2", "title": "The chapter in brief", "blocks": [
  blk("s2.note", "theory", title="How to read this chapter",
    body="Read the full chapter in your **NCERT Sparsh Part 2** textbook. The table below sums up its key points; passages in the questions are Shine retellings in Hindi."),
  blk("s2.table", "markdown_table", title="Key points", revision=True, body=FACTS),
  C.kc("s2.check", "On whose story is 'तीसरी कसम' based?",
    [("Phanishwar Nath Renu", ""), ("Premchand", "Renu."), ("Shailendra", "He produced it."), ("Raj Kapoor", "He acted in it.")],
    "'मारे गए गुलफ़ाम'.")
  ,C.kc("s2.check2", "What fee did Raj Kapoor finally take?",
    [("one rupee", ""), ("one lakh rupees", "One rupee."), ("nothing at all", "He asked for one rupee."), ("a share of profits", "One rupee.")],
    "As a joke between friends.")
 ]},
 {"id": "s3", "title": "Ideas in the chapter", "blocks": [
  blk("s3.thm", "theory", title="What the chapter says", revision=True,
    body="**Art vs commerce:** the film was made with feeling, not for profit. Distributors want 'masala' and quick returns, so they could not value it.\n\n"
         "**The artist's duty:** Shailendra believed an artist should **refine** the audience's taste, not push shallow content on them in the name of 'what people want'.\n\n"
         "**Showing sorrow honestly:** many films **glorify** tragedy to make audiences cry and earn money. 'तीसरी कसम' showed sorrow as it is in life; **'व्यथा आदमी को पराजित नहीं करती, उसे आगे बढ़ने का संदेश देती है'**.\n\n"
         "**Faithful to literature:** the film did full justice to Renu's story, keeping its village life and feelings.\n\n"
         "**Raj Kapoor:** called **Asia's greatest showman**; an actor who 'talks with his eyes'. In this film he became Hiraman so fully that we do not see the star at all.\n\n"
         "**Shailendra's songs:** simple, full of feeling (**भाव-प्रवण**), never difficult (**दुरूह**); they gave words to Raj Kapoor's emotions.\n\n"
         "**Shailendra's life in the film:** his simplicity, honesty and pain show in Hiraman's innocence and the film's sensitivity. He died soon after the film's release."),
  C.kc("s3.check", "According to Shailendra, what is an artist's duty?",
    [("to refine the audience's taste", ""), ("to give people whatever sells", "The opposite."), ("to win awards", "Refine taste."), ("to copy hit films", "Refine taste.")],
    "Not to impose shallowness.")
  ,C.kc("s3.check2", "Why did Jaikishan object to 'दसों दिशाओं'?",
    [("he felt audiences know only four directions", ""), ("the word was too long", "Four directions."), ("it did not rhyme", "Four directions."), ("Raj Kapoor disliked it", "Jaikishan's objection.")],
    "Shailendra did not change it.")
 ]},
 {"id": "s4", "title": "Language and style", "blocks": [
  blk("s4.thm", "theory", title="Language and style", revision=True,
    body="| Feature | Example / note |\n|---|---|\n| **Type** | **संस्मरणात्मक लेख / फ़िल्म-समीक्षा** (memoir-style essay on cinema) |\n"
         "| **Language** | Hindi mixed with **Urdu** and **English** film words (*सैल्यूलाइड, शोमैन, ग्लोरीफ़ाई, एडवांस*) |\n"
         "| **Tone** | admiring, thoughtful, sometimes sad |\n| **Key phrases** | *सैल्यूलाइड पर लिखी कविता*, *एशिया के सबसे बड़े शोमैन*, *दो से चार बनाने वाले* (profit-seekers) |"),
  C.kc("s4.check", "'दो से चार बनाने वाले' refers to:",
    [("people who only want to multiply their money", ""), ("mathematics teachers", "Profit-seekers."), ("song-writers", "Profit-seekers."), ("actors", "Profit-seekers.")],
    "They could not understand the film's feeling.")
 ]},
 closing(C,
   "- **तीसरी कसम (1966) ← Renu's 'मारे गए गुलफ़ाम'; producer Shailendra (only film).**\n- **Raj Kapoor = हीरामन, Waheeda Rehman = हीराबाई; fee ₹1.**\n- **President's Gold Medal; 'सैल्यूलाइड पर लिखी कविता'; artist must refine taste.**",
   "1. Writing that Raj Kapoor produced the film: **Shailendra** produced it.\n2. Saying it was a box-office hit: it **won awards but failed commercially**.\n"
   "3. Mixing up Hiraman (the cart-driver) and Hirabai (the dancer).\n4. Writing exam answers in English: answer in **Hindi**.",
   "Play one song from 'तीसरी कसम' and ask students to say what feeling it shows and how simple words carry it.",
   "Would you choose work that makes you happy or work that makes more money? Why?",
   "- **Phanishwar Nath Renu:** the writer of the original story.\n- **Media studies:** art films vs commercial films.",
   "Why is 'तीसरी कसम' called 'a poem written on celluloid'? Answer in about 60 words.",
   "'तीसरी कसम' is called a poem on celluloid because it is full of delicate feelings, like a poem. Shailendra, a sensitive poet, made it with honesty, keeping Renu's story intact. It shows village life, innocent love and real sorrow without exaggeration. Raj Kapoor became Hiraman completely, and the simple songs touch the heart. Its beauty lies in feeling, not in commercial 'masala'.",
   "- Prahlad Agrawal writes about Shailendra's only film, 'तीसरी कसम', based on Renu's story.\n- Raj Kapoor (Hiraman) and Waheeda Rehman (Hirabai) acted; Raj took a fee of one rupee.\n"
   "- The film won the President's Gold Medal but found few buyers and failed commercially.\n- Shailendra, an idealist poet, valued self-satisfaction and believed artists must refine public taste.",
   "- Answer in Hindi, in 25-30 words for 2 marks.\n- Keep names right: Shailendra (producer), Raj Kapoor (Hiraman), Waheeda Rehman (Hirabai), Renu (story).\n- Use key phrases like 'सैल्यूलाइड पर लिखी कविता'.",
   [("Who played Hiraman and Hirabai?", "Raj Kapoor played Hiraman; Waheeda Rehman played Hirabai."),
    ("Which award did 'तीसरी कसम' win?", "The President's Gold Medal for best feature film (and others).")]),
]

# ---------------- NCERT मौखिक ----------------
C.two("mo1", FILM, "Which awards was the film 'तीसरी कसम' honoured with?",
      ["It received the President's Gold Medal as the best feature film.", "It also won the Bengal Film Journalists' Association award and other honours, and was shown at the Moscow film festival."], MO(1))
C.two("mo2", SHAIL, "How many films did Shailendra make?",
      ["Shailendra made only one film.", "That film was 'तीसरी कसम'."], MO(2))
C.two("mo3", RAJ, "Name some films directed by Raj Kapoor.",
      ["आवारा, श्री 420, बरसात and संगम.", "मेरा नाम जोकर, बॉबी and सत्यम शिवम सुंदरम."], MO(3))
C.two("mo4", FILM, "Name the hero and heroine of 'तीसरी कसम' and the characters they played.",
      ["The hero was Raj Kapoor, who played Hiraman, a village cart-driver.", "The heroine was Waheeda Rehman, who played Hirabai, a nautanki dancer."], MO(4))
C.two("mo5", SHAIL, "Who produced the film 'तीसरी कसम'?",
      ["The film was produced by the lyricist Shailendra.", "It was the only film he ever produced."], MO(5))
C.two("mo6", RAJ, "What had Raj Kapoor not even imagined while making 'मेरा नाम जोकर'?",
      ["He had not imagined that making even one part of the film would take six years.", "The film took far longer than he expected."], MO(6))
C.two("mo7", RAJ, "At what did Shailendra's face fall?",
      ["When Raj Kapoor asked for his fee in advance, Shailendra's face fell.", "Then Raj Kapoor laughed and asked for only one rupee."], MO(7))
C.two("mo8", RAJ, "What kind of artist did film critics consider Raj Kapoor?",
      ["They considered him a master of the art of acting.", "They said he was an actor who could speak with his eyes."], MO(8))
# ---------------- NCERT लिखित (क) ----------------
C.two("lk1", FILM, "Why has 'तीसरी कसम' been called 'a poem written on celluloid'?",
      ["The film is full of delicate feelings and sensitivity, like a poem.", "It was made by a poet with honesty and shows life's emotions beautifully on film."], LK(1))
C.two("lk2", ART, "Why was 'तीसरी कसम' not finding buyers?",
      ["The film had deep feeling and no commercial 'masala'.", "Profit-minded distributors could not understand its sensitivity, so they did not buy it."], LK(2))
C.two("lk3", ART, "According to Shailendra, what is an artist's duty?",
      ["An artist should not impose shallowness on audiences in the name of their taste.", "The artist's duty is to try to refine the audience's taste."], LK(3))
C.two("lk4", ART, "Why are tragic situations glorified in films?",
      ["Film-makers glorify tragedy to move audiences and attract them.", "They do it to earn more money at the box office."], LK(4))
C.two("lk5", SHAIL, "'Shailendra gave words to Raj Kapoor's feelings.' What do you understand by this? Explain.",
      ["Raj Kapoor expressed emotions through his acting and eyes.", "Shailendra's songs put those very emotions into simple, touching words."], LK(5))
C.two("lk6", RAJ, "The writer calls Raj Kapoor Asia's greatest showman. What do you understand by 'showman'?",
      ["A showman is an artist who presents entertainment grandly and attractively.", "He knows how to hold the audience and make his work popular."], LK(6))
C.two("lk7", SHAIL, "Why did composer Jaikishan object to the song 'रातें दसों दिशाओं से कहेंगी अपनी कहानियाँ' in 'श्री 420'?",
      ["Jaikishan felt audiences know only four directions, not ten.", "He wanted 'दसों दिशाएँ' changed to 'चारों दिशाएँ', but Shailendra refused."], LK(7))
# ---------------- NCERT लिखित (ख) ----------------
C.two("lb1", SHAIL, "Why did Shailendra make this film even after Raj Kapoor warned him of the risks of failure?",
      ["Shailendra was an idealist, emotional poet.", "He wanted the joy of self-satisfaction more than wealth or fame."], LB(1))
C.two("lb2", RAJ, "How did Raj Kapoor's grand personality enter Hiraman's soul in 'तीसरी कसम'? Explain.",
      ["Raj Kapoor set aside his star image and became the simple, innocent village cart-driver.", "On screen we see only Hiraman, not the famous Raj Kapoor."], LB(2), "medium")
C.two("lb3", FILM, "Why does the writer say that 'तीसरी कसम' did full justice to the literary work?",
      ["The film kept Renu's story, its village life and its feelings without change.", "It did not distort the story for commercial gain."], LB(3))
C.two("lb4", SHAIL, "What are the features of Shailendra's songs? Write in your own words.",
      ["His songs are simple, easy to understand and full of feeling.", "They carry deep meaning and touch the heart of ordinary people."], LB(4))
C.two("lb5", SHAIL, "Throw light on Shailendra's qualities as a film producer.",
      ["He was an idealist who made the film for art, not profit.", "He stayed honest to the story and did not compromise for box-office success."], LB(5))
C.two("lb6", SHAIL, "The impression of Shailendra's personal life shows in his film. How? Explain.",
      ["Shailendra was simple, honest and sensitive.", "The same simplicity and sensitivity appear in Hiraman's innocence and the film's emotions."], LB(6), "medium")
C.two("lb7", FILM, "How far do you agree that only a true poet's heart could make 'तीसरी कसम'?",
      ["I agree; the film's delicate emotions and honesty need a sensitive heart.", "Only a poet like Shailendra, who cared for feeling over profit, could make it."], LB(7), "medium")
# ---------------- NCERT आशय ----------------
C.two("as1", SHAIL, "Explain the meaning: 'वह तो एक आदर्शवादी भावुक कवि था, जिसे अपार संपत्ति और यश तक की इतनी कामना नहीं थी जितनी आत्म-संतुष्टि के सुख की अभिलाषा थी।'",
      ["Shailendra was an idealist, emotional poet.", "He did not long for great wealth or fame as much as for the joy of self-satisfaction."], AS(1))
C.two("as2", ART, "Explain the meaning: 'दर्शकों की रुचि की आड़ में हमें उथलेपन को उन पर नहीं थोपना चाहिए। कलाकार का यह कर्तव्य भी है कि वह उपभोक्ता की रुचियों का परिष्कार करने का प्रयत्न करे।'",
      ["We should not force shallow content on audiences claiming that it is what they like.", "An artist must try to improve and refine the taste of the audience."], AS(2), "medium")
C.two("as3", ART, "Explain the meaning: 'व्यथा आदमी को पराजित नहीं करती, उसे आगे बढ़ने का संदेश देती है।'",
      ["Sorrow does not defeat a person.", "Instead it gives him strength and the message to move forward in life."], AS(3))
C.two("as4", ART, "Explain the meaning: 'दरअसल इस फ़िल्म की संवेदना किसी दो से चार बनाने वाले की समझ से परे है।'",
      ["The film's deep sensitivity is beyond the understanding of people who only want profit.", "Those who think only of multiplying money cannot value such feeling."], AS(4))
C.two("as5", SHAIL, "Explain the meaning: 'उनके गीत भाव-प्रवण थे—दुरूह नहीं।'",
      ["Shailendra's songs were full of feeling.", "They were not difficult; ordinary people could easily understand them."], AS(5))

# ---------------- Extracts (Shine retellings) ----------------
C.extract("ext1", RAJ + FILM, "राजकपूर शैलेंद्र के गहरे मित्र थे। उन्होंने शैलेंद्र को फ़िल्म की असफलता के खतरों से सावधान किया, फिर मुस्कुराकर पूरा पारिश्रमिक पहले माँगा। शैलेंद्र का चेहरा मुरझा गया। तब राजकपूर ने हँसकर कहा—'निकालो एक रुपया, मेरा पारिश्रमिक।'",
  [("What was the relation between Raj Kapoor and Shailendra?", "They were close friends."), ("What did Raj Kapoor warn Shailendra about?", "The risks of the film failing."),
   ("Why did Shailendra's face fall?", "Because Raj Kapoor asked for his full fee in advance."), ("What fee did Raj Kapoor finally ask for?", "One rupee."), ("What does this show about Raj Kapoor?", "His friendship and generosity.")],
  intro=PROSE_INTRO)
C.extract("ext2", ART + FILM, "'तीसरी कसम' को राष्ट्रपति स्वर्ण पदक मिला, फिर भी वितरक इसे खरीदने को तैयार नहीं थे। इसमें न तो चमक-दमक थी, न मसाला। इसकी संवेदना मुनाफ़ा कमाने वालों की समझ से परे थी।",
  [("Which award did the film get?", "The President's Gold Medal."), ("Who were not ready to buy it?", "Distributors."),
   ("Why did they not buy it?", "It had no glamour or masala; its feeling was beyond them."), ("Who could not understand its sensitivity?", "Profit-seekers."), ("What does 'संवेदना' mean?", "Sensitivity, feeling.")],
  intro=PROSE_INTRO)

# ---------------- Objective practice ----------------
C.m("mcq01", FILM, "'तीसरी कसम' is based on a story by:", [("Phanishwar Nath Renu", ""), ("Premchand", "Renu."), ("Shailendra", "He produced it."), ("Prahlad Agrawal", "He wrote this chapter.")], "'मारे गए गुलफ़ाम'.")
C.m("mcq02", FILM, "Who played Hiraman?", [("Raj Kapoor", ""), ("Shailendra", "Raj Kapoor."), ("Dilip Kumar", "Raj Kapoor."), ("Dev Anand", "Raj Kapoor.")], "A village cart-driver.")
C.m("mcq03", FILM, "Who played Hirabai?", [("Waheeda Rehman", ""), ("Nargis", "Waheeda Rehman."), ("Madhubala", "Waheeda Rehman."), ("Meena Kumari", "Waheeda Rehman.")], "A nautanki dancer.")
C.m("mcq04", SHAIL, "Shailendra was mainly a:", [("lyricist and poet", ""), ("director", "Lyricist."), ("actor", "Lyricist."), ("music composer", "Lyricist.")], "He produced only one film.")
C.m("mcq05", RAJ, "Raj Kapoor is called:", [("Asia's greatest showman", ""), ("the tragedy king", "Showman."), ("the king of romance", "Showman."), ("the angry young man", "Showman.")], "शोमैन.")
C.m("mcq06", ART, "The film failed at the box office because:", [("distributors and profit-seekers could not value its feeling", ""), ("it had bad songs", "Its songs were loved."), ("it had no famous actors", "It had stars."), ("it was too short", "Its sensitivity was not understood.")], "No masala.")
C.m("mcq07", SHAIL, "Who objected to 'दसों दिशाओं'?", [("Jaikishan", ""), ("Raj Kapoor", "Jaikishan."), ("Mukesh", "Jaikishan."), ("Renu", "Jaikishan.")], "He was the composer.")
C.m("mcq08", ART, "'दुरूह' means:", [("difficult to understand", ""), ("full of feeling", "That is भाव-प्रवण."), ("very long", "Difficult."), ("sad", "Difficult.")], "Shailendra's songs were not दुरूह.")
C.m("mcq09", ART, "'परिष्कार' means:", [("refinement", ""), ("destruction", "Refinement."), ("copying", "Refinement."), ("payment", "Refinement.")], "Refining public taste.")
C.m("mcq10", FILM, "'तीसरी कसम' was released in:", [("1966", ""), ("1947", "1966."), ("1975", "1966."), ("1955", "1966.")], "Shailendra died the same year.")
C.tf("tf1", SHAIL, "Shailendra produced many films.", False, "Only one, 'तीसरी कसम'.")
C.tf("tf2", FILM, "'तीसरी कसम' won the President's Gold Medal.", True, "Best feature film.")
C.tf("tf3", ART, "Shailendra believed artists should give audiences whatever is shallow but popular.", False, "He believed they should refine taste.")

chapter = header("sparsh", "ch09", 9, "तीसरी कसम के शिल्पकार शैलेंद्र", "प्रहलाद अग्रवाल", "prose", ["teesri_kasam_film", "shailendra_poet_producer", "raj_kapoor_actor", "art_vs_commerce"],
                 "CBSE 2025-26 Hindi Course B (085), Section C: Sparsh Part 2 prose. Assessed through extract-based MCQs (1 mark each) and short answers in 25-30 words (2 marks); answers are written in Hindi. The text is in copyright: read it in the NCERT textbook.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
