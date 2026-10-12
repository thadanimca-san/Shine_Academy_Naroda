"""CBSE Class 10 Hindi Course B, Sparsh Part 2, Ch 5: कर चले हम फ़िदा (Kaifi Azmi).
The song is in copyright, so the lesson summarises it and quotes only short lines; students read it in NCERT."""
import sys
from hindi_common import make, header, path, ex
from lit_common import closing

ROOT = sys.argv[1]
PATH = path("sparsh", "ch05_kar_chale_hum_fida")
C = make("hsp10ch05")
blk = C.blk
DUTY, SAC, CALL, CRAFT = ["soldiers_duty"], ["sacrifice_for_nation"], ["call_to_youth"], ["song_craft"]
PE = lambda n: ex(n)
BH = lambda n: ex(n, "भाव स्पष्ट कीजिए")

PARTS = ("| Part of the song | What the soldiers say |\n|---|---|\n"
         "| **Refrain** (*'कर चले हम फ़िदा जानो-तन साथियो'*) | We have sacrificed our life and body; now the nation is in your hands, friends. |\n"
         "| **Stanza 1** | Our breath was stopping and our pulse was freezing, yet we did not let our steps stop. We did not let the head of the **Himalaya** bow; even while dying, our **pride and spirit (बाँकपन)** remained. |\n"
         "| **Stanza 2** | There are many seasons to live, but the **season to give one's life** does not come every day. Youth that is not ready to shed blood for the country shames both beauty and love. Today the **earth has become a bride**. |\n"
         "| **Stanza 3** | Let the road of sacrifice never become empty; keep forming **new caravans** of brave people. The celebration of victory comes after this celebration of sacrifice; life is embracing death. **Tie a shroud on your heads (सर पर कफ़न)**. |\n"
         "| **Stanza 4** | Draw a **line on the ground with your blood** so that no **Ravana** can cross it. Break any hand raised to touch **Sita's** honour (the motherland). **You are Rama, you are Lakshmana**, friends. |")

sections = [
 {"id": "s1", "title": "A song from the battlefield", "blocks": [
  blk("s1.hook", "hook", title="The last words of soldiers",
    body="Imagine soldiers lying wounded on a snowy mountain border, knowing they will not survive. What would they say to the people they leave behind?\n\n"
         "This song gives their answer: **'We have given our lives; now the country is in your hands.'** It was written by **Kaifi Azmi** for the film **'हकीकत' (1964)**, based on the **India-China war of 1962**."),
  blk("s1.inspiration", "inspiration", title="The poet", person="Kaifi Azmi", years="1919–2002",
    body="**Kaifi Azmi** (real name **Athar Husain Rizvi**) was born in **Majwan** village in **Azamgarh** district (Uttar Pradesh). He was a leading **progressive** Urdu poet and a famous film lyricist, writing about ordinary people, justice and patriotism.\n\n"
         "His collections include **झंकार**, **आख़िर-ए-शब** and **आवारा सिज्दे** (which won the **Sahitya Akademi Award**). He received the **Padma Shri**. The actor **Shabana Azmi** is his daughter.",
    future="Every Independence Day and Republic Day this song is played to remember soldiers' sacrifice."),
  C.socratic("s1.socratic", "Whom do the dying soldiers call 'साथियो' (friends)?",
    ["The people of the country, especially the young", "Only other soldiers of the enemy", "Their officers alone"], 0,
    "They hand the country over to all citizens.")
 ]},
 {"id": "s2", "title": "The song and its meaning", "blocks": [
  blk("s2.note", "theory", title="How to read this chapter",
    body="Read the full song in your **NCERT Sparsh Part 2** textbook. The table below explains each part, with key lines quoted so you can find them."),
  blk("s2.table", "markdown_table", title="What the song says", revision=True, body=PARTS),
  C.kc("s2.check", "What does the Himalaya stand for in 'सर हिमालय का हमने न झुकने दिया'?",
    [("the pride and honour of India", ""), ("only a mountain", "It is a symbol."), ("the enemy", "It is India's pride."), ("snow and cold", "It is a symbol.")],
    "The soldiers did not let India's pride bow.")
  ,C.kc("s2.check2", "Why is the earth called a bride?",
    [("it is red with the blood of martyrs, like a bride in red", ""), ("it is decorated with flowers", "Red with blood."), ("it is getting married", "It is a metaphor."), ("it is covered with snow", "Red with blood.")],
    "'आज धरती बनी है दुलहन साथियो'.")
 ]},
 {"id": "s3", "title": "The message of the song", "blocks": [
  blk("s3.thm", "theory", title="Ideas in the song", revision=True,
    body="**Historical background:** the song comes from the film **हकीकत (1964)**, about the **1962 India-China war**, when Indian soldiers fought bravely on the Himalayan border.\n\n"
         "**Duty to the end:** even as breath stopped and pulse froze, the soldiers kept moving forward and did not let the **Himalaya**, the symbol of India's honour, bow.\n\n"
         "**A rare chance:** many days come for living, but the chance to die for the nation is rare; youth that does not offer itself for the country is wasted.\n\n"
         "**The earth as a bride:** the land is red with the blood of martyrs, like a bride in red.\n\n"
         "**Keep the caravan going:** the soldiers ask the young to keep forming **caravans** of the brave, so that the path of sacrifice is never empty, and to **tie a shroud on their heads**, that is, be ready to die.\n\n"
         "**Protect the motherland:** draw a line with your blood so no **Ravana** (enemy) can cross; protect **Sita** (the motherland's honour); **you are Rama and Lakshmana** now."),
  C.kc("s3.check", "'सर पर कफ़न बाँधना' means:",
    [("being ready to die for the nation", ""), ("wearing a turban", "It is an idiom."), ("being sad", "Readiness to die."), ("going to a funeral", "Readiness to die.")],
    "An idiom of fearless readiness.")
  ,C.kc("s3.check2", "In the last stanza, 'रावण' stands for:",
    [("the enemy who attacks the country", ""), ("a character in a film", "It is a symbol."), ("a king of Lanka only", "The enemy."), ("a soldier", "The enemy.")],
    "Sita stands for the motherland's honour.")
 ]},
 {"id": "s4", "title": "Language and style", "blocks": [
  blk("s4.thm", "theory", title="Language and devices", revision=True,
    body="| Feature | Example / note |\n|---|---|\n| **Language** | simple **Hindustani** with **Urdu** words: *फ़िदा, जानो-तन, नब्ज़, रुत, रुस्वा, काफ़िले, फतह, जश्न, कफ़न* |\n"
         "| **Form** | **गीत** (song) with a **refrain** ending in *'साथियो'*; musical and easy to remember |\n"
         "| **Tone** | **वीर रस** (heroic), with an **उद्बोधन** (call) to the young |\n| **मुहावरे (idioms)** | *सर पर कफ़न बाँधना, गले मिलना, सर न झुकने देना* |\n"
         "| **प्रतीक (symbols)** | हिमालय = national honour; राम-लक्ष्मण = protectors; सीता = motherland's honour; रावण = enemy |\n"
         "| **रूपक (metaphor)** | *धरती बनी है दुलहन* |\n| **मानवीकरण** | *ज़िंदगी मौत से मिल रही है गले* |\n\n"
         "**Why such songs are remembered:** simple words, a catchy tune, deep feeling, and a link to a real event."),
  C.kc("s4.check", "The main रस (mood) of this song is:",
    [("वीर रस (heroic)", ""), ("शृंगार रस", "Heroic."), ("हास्य रस", "Heroic."), ("शांत रस", "Heroic.")],
    "It inspires courage and sacrifice.")
 ]},
 closing(C,
   "- **Film: हकीकत (1964); war: India-China 1962.**\n- **Symbols: हिमालय = सम्मान, धरती = दुलहन, रावण = शत्रु, सीता = मातृभूमि, राम-लक्ष्मण = रक्षक.**\n- **Idiom: सर पर कफ़न बाँधना = मरने को तैयार.**",
   "1. Saying the song is about the 1947 or 1971 war: it is about **1962 (India-China)**.\n2. Writing that the earth is a bride because of flowers: it is red with **martyrs' blood**.\n"
   "3. Taking Ravana and Sita literally: they are **symbols** of the enemy and the motherland.\n4. Writing exam answers in English: answer in **Hindi**.",
   "Play the song (film audio) in class, then ask students to list each symbol and what it stands for.",
   "What can you do for your country in daily life, without being a soldier?",
   "- **Manushyata (Ch 3):** 'वही मनुष्य है कि जो मनुष्य के लिए मरे'.\n- **History:** the 1962 war and the defence of India's borders.",
   "Why do the soldiers say 'अब तुम्हारे हवाले वतन साथियो'? Explain in about 60 words.",
   "The soldiers have fought till their last breath and are about to die. They know the country will still need protection after them. So they hand over the responsibility of the nation to the young people. They ask them to keep the path of sacrifice alive, to be ready to die, and to draw a line with their blood that no enemy can cross. Now the youth must be Rama and Lakshmana.",
   "- Kaifi Azmi wrote this song for the film 'हकीकत', about the 1962 India-China war.\n- The dying soldiers say they kept moving and did not let the Himalaya (India's pride) bow.\n"
   "- The chance to die for the nation is rare; the earth is a bride red with blood.\n- They ask the young to keep the caravan of sacrifice going, tie a shroud on their heads and protect the motherland like Rama and Lakshmana.",
   "- Answer in Hindi, in 25-30 words for 2 marks.\n- Mention the 1962 war for background questions.\n- Explain each symbol in plain words.",
   [("What is the background of this song?", "The 1962 India-China war; written for the film 'हकीकत' (1964)."),
    ("What does 'सर पर कफ़न बाँधना' mean?", "To be ready to die for the country.")]),
]

# ---------------- NCERT प्रश्न-अभ्यास (क) ----------------
C.two("pa1", DUTY, "Does this song have a historical background?",
      ["Yes; it was written for the film 'हकीकत' (1964), based on the India-China war of 1962.", "In that war Indian soldiers fought bravely on the Himalayan border and many gave their lives."], PE(1))
C.two("pa2", DUTY, "In 'सर हिमालय का हमने न झुकने दिया', what does the Himalaya symbolise?",
      ["The Himalaya symbolises the pride, honour and self-respect of India.", "The soldiers did not let the nation's honour bow before the enemy."], PE(2))
C.two("pa3", SAC, "Why has the earth been called a bride in this song?",
      ["A bride wears red; the earth has become red with the blood of the martyrs.", "So, decorated with their sacrifice, the earth looks like a bride."], PE(3))
C.two("pa4", CRAFT, "What is special about songs that makes them remembered for a lifetime?",
      ["They have simple words, a sweet tune and rhythm, and deep feeling.", "They touch the heart and are often linked to real events, so they stay in memory."], PE(4))
C.two("pa5", CALL, "For whom has the poet used the address 'साथियो'?",
      ["The poet uses 'साथियो' for the people of the country, especially the youth.", "The dying soldiers hand over the protection of the nation to them."], PE(5))
C.two("pa6", CALL, "Which caravan has the poet asked to keep moving forward?",
      ["The caravan of brave people ready to sacrifice their lives for the country.", "The path of sacrifice should never become empty; new brave people should keep joining."], PE(6))
C.two("pa7", CALL, "What does 'सर पर कफ़न बाँधना' in this song point to?",
      ["It points to being ready to die for the nation.", "The soldiers ask the youth to fight the enemy fearlessly, without caring for their lives."], PE(7))
C.two("pa8", SAC, "Write the central idea of this poem in your own words.",
      ["The song gives the message of patriotism and sacrifice through the words of dying soldiers.", "They hand the country to the youth and ask them to protect its honour at any cost."], PE(8))
# ---------------- NCERT (ख) भाव ----------------
C.two("bh1", DUTY, "Explain the idea: 'साँस थमती गई, नब्ज़ जमती गई, फिर भी बढ़ते कदम को न रुकने दिया'.",
      ["Even when their breath was stopping and their pulse freezing in the cold, the soldiers did not stop.", "They kept moving forward and fought the enemy till their last breath."], BH(1))
C.two("bh2", CALL, "Explain the idea: 'खींच दो अपने खूँ से ज़मीं पर लकीर, इस तरफ़ आने पाए न रावन कोई'.",
      ["The soldiers ask the youth to guard the border with their blood, like a Lakshman-rekha.", "No enemy (Ravana) should be able to cross into our country."], BH(2))
C.two("bh3", CALL, "Explain the idea: 'छू न पाए सीता का दामन कोई, राम भी तुम, तुम्हीं लक्ष्मण साथियो'.",
      ["The motherland's honour is like Sita's; no enemy should be able to touch it.", "The youth must protect it, as Rama and Lakshmana protected Sita."], BH(3))

# ---------------- Extracts (short quotations) ----------------
C.extract("ext1", DUTY, "साँस थमती गई, नब्ज़ जमती गई\nफिर भी बढ़ते कदम को न रुकने दिया",
  [("Who is speaking in these lines?", "Dying soldiers."), ("Why was their pulse freezing?", "Because of wounds and the extreme cold of the Himalayas."),
   ("What did they not let stop?", "Their steps moving forward."), ("What quality do these lines show?", "Courage and devotion to duty."), ("What does 'नब्ज़' mean?", "Pulse.")])
C.extract("ext2", CALL, "बाँध लो अपने सर से कफ़न साथियो\nअब तुम्हारे हवाले वतन साथियो",
  [("Whom are the soldiers addressing?", "The people, especially the youth of the country."), ("What does 'सर से कफ़न बाँधना' mean?", "To be ready to die."),
   ("What do the soldiers hand over?", "The country (वतन)."), ("Why are they handing it over?", "They are dying and cannot protect it any more."), ("What is the mood (रस)?", "वीर रस (heroic).")])

# ---------------- Objective practice ----------------
C.m("mcq01", DUTY, "The song 'कर चले हम फ़िदा' was written for the film:", [("हकीकत", ""), ("बॉर्डर", "Haqeeqat."), ("उपकार", "Haqeeqat."), ("लक्ष्य", "Haqeeqat.")], "Released in 1964.")
C.m("mcq02", DUTY, "The song is based on the war of:", [("1962 (India-China)", ""), ("1947", "1962."), ("1965", "1962."), ("1971", "1962.")], "Fought on the Himalayan border.")
C.m("mcq03", DUTY, "'फ़िदा' means:", [("sacrificed, devoted", ""), ("defeated", "Sacrificed."), ("tired", "Sacrificed."), ("happy", "Sacrificed.")], "'कर चले हम फ़िदा जानो-तन'.")
C.m("mcq04", DUTY, "In the song the Himalaya is a symbol of:", [("India's honour", ""), ("cold weather", "India's honour."), ("the enemy", "India's honour."), ("a holy place", "India's honour.")], "'सर हिमालय का हमने न झुकने दिया'.")
C.m("mcq05", DUTY, "'बाँकपन' means:", [("pride and spirit", ""), ("fear", "Pride."), ("tiredness", "Pride."), ("sadness", "Pride.")], "Even while dying.")
C.m("mcq06", SAC, "According to the song, what does not come every day?", [("the season to give one's life", ""), ("the season to live", "That comes often."), ("rain", "The chance to die for the nation."), ("victory", "The chance to die for the nation.")], "'जान देने की रुत रोज़ आती नहीं'.")
C.m("mcq07", SAC, "'रुत' means:", [("season", ""), ("road", "Season."), ("blood", "Season."), ("night", "Season.")], "ऋतु.")
C.m("mcq08", SAC, "The earth is called a bride because it is:", [("red with martyrs' blood", ""), ("covered in flowers", "Red with blood."), ("full of music", "Red with blood."), ("covered in snow", "Red with blood.")], "A bride wears red.")
C.m("mcq09", CALL, "'काफ़िले' means:", [("caravans, groups of travellers", ""), ("enemies", "Caravans."), ("weapons", "Caravans."), ("songs", "Caravans.")], "New groups of brave people.")
C.m("mcq10", CALL, "'फतह' means:", [("victory", ""), ("defeat", "Victory."), ("death", "Victory."), ("peace", "Victory.")], "'फतह का जश्न'.")
C.m("mcq11", SAC, "'ज़िंदगी मौत से मिल रही है गले' means:", [("life is embracing death in sacrifice", ""), ("life is afraid of death", "Embracing."), ("death has ended", "Embracing."), ("life is happy", "Embracing death.")], "Personification.")
C.m("mcq12", CALL, "'सर पर कफ़न बाँधना' means:", [("to be ready to die", ""), ("to wear a turban", "An idiom."), ("to be ill", "Ready to die."), ("to attend a funeral", "Ready to die.")], "Fearless readiness.")
C.m("mcq13", CALL, "With what should the line on the ground be drawn?", [("one's own blood", ""), ("chalk", "Blood."), ("a sword", "Blood."), ("a stick", "Blood.")], "'खींच दो अपने खूँ से ज़मीं पर लकीर'.")
C.m("mcq14", CALL, "In the song, 'रावण' stands for:", [("the enemy", ""), ("a demon king only", "A symbol."), ("a soldier", "The enemy."), ("a friend", "The enemy.")], "Who must not cross the line.")
C.m("mcq15", CALL, "'सीता का दामन' stands for:", [("the honour of the motherland", ""), ("a woman's dress", "A symbol."), ("the Himalaya", "Motherland's honour."), ("the army", "Motherland's honour.")], "No one should touch it.")
C.m("mcq16", CALL, "The youth are asked to be:", [("Rama and Lakshmana", ""), ("Ravana", "Protectors."), ("Hanuman only", "Rama and Lakshmana."), ("Bharata", "Rama and Lakshmana.")], "'राम भी तुम, तुम्हीं लक्ष्मण'.")
C.m("mcq17", CRAFT, "The poet of this song is:", [("Kaifi Azmi", ""), ("Sahir Ludhianvi", "Kaifi Azmi."), ("Gulzar", "Kaifi Azmi."), ("Pradeep", "Kaifi Azmi.")], "A progressive Urdu poet.")
C.m("mcq18", CRAFT, "Kaifi Azmi's real name was:", [("Athar Husain Rizvi", ""), ("Gosain Dutt", "That was Pant."), ("Gajanan Madhav", "Not him."), ("Sampooran Singh", "That is Gulzar.")], "Born in Azamgarh.")
C.m("mcq19", CRAFT, "The main mood of the song is:", [("वीर रस", ""), ("करुण रस only", "Heroic."), ("हास्य रस", "Heroic."), ("शृंगार रस", "Heroic.")], "Courage and sacrifice.")
C.m("mcq20", CRAFT, "'धरती बनी है दुलहन' is an example of:", [("रूपक (metaphor)", ""), ("यमक", "Metaphor."), ("अनुप्रास", "Metaphor."), ("श्लेष", "Metaphor.")], "The earth is called a bride.")
C.tf("tf1", DUTY, "The song is based on the 1962 India-China war.", True, "Film हकीकत.")
C.tf("tf2", DUTY, "The soldiers stopped moving when their pulse froze.", False, "'फिर भी बढ़ते कदम को न रुकने दिया'.")
C.tf("tf3", SAC, "The song says the chance to die for the nation comes every day.", False, "'जान देने की रुत रोज़ आती नहीं'.")
C.tf("tf4", CALL, "The soldiers hand over the country to the youth.", True, "'अब तुम्हारे हवाले वतन साथियो'.")
C.tf("tf5", CALL, "Ravana in the song means the enemy.", True, "A symbol.")
C.tf("tf6", CRAFT, "Kaifi Azmi was a poet of the Chhayavad movement.", False, "He was a progressive Urdu poet.")
C.two("sa1", SAC, "What do the soldiers mean by youth 'that does not bathe in blood'?",
      ["Youth that is not ready to shed blood for the nation is wasted.", "Such youth shames beauty and love; true youth serves the country."], difficulty="medium")

C.two("sa2", SAC, "What does 'फतह का जश्न इस जश्न के बाद है' mean?",
      ["The celebration of victory will come only after this 'celebration' of sacrifice.", "The soldiers' martyrdom today makes the nation's future victory possible."], difficulty="medium")
C.two("sa3", CALL, "Why is this song still relevant today?",
      ["Our borders still need brave soldiers, and the song reminds us of their sacrifice.", "It inspires young people to put the nation first and protect its honour."])

chapter = header("sparsh", "ch05", 5, "कर चले हम फ़िदा", "कैफ़ी आज़मी", "poem", ["soldiers_duty", "sacrifice_for_nation", "call_to_youth", "song_craft"],
                 "CBSE 2025-26 Hindi Course B (085), Section C: Sparsh Part 2 poetry. Assessed through extract-based MCQs (1 mark each) and short answers in 25-30 words (2 marks); answers are written in Hindi. The song is in copyright: read the full text in the NCERT textbook.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
