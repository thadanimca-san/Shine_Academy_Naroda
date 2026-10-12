"""CBSE Class 10 Hindi Course B, Sparsh Part 2, Ch 6: आत्मत्राण (Rabindranath Tagore, Hindi translation by Hazari Prasad Dwivedi).
The Hindi translation is in copyright, so the lesson summarises it and quotes only short lines; students read it in NCERT."""
import sys
from hindi_common import make, header, path, ex
from lit_common import closing

ROOT = sys.argv[1]
PATH = path("sparsh", "ch06_atmatran")
C = make("hsp10ch06")
blk = C.blk
COURAGE, SELF, FAITH, CRAFT = ["fearless_courage"], ["self_reliance"], ["faith_in_god"], ["prayer_craft"]
PE = lambda n: ex(n)
BH = lambda n: ex(n, "भाव स्पष्ट कीजिए")

PARTS = ("| Part of the prayer | What the poet asks for |\n|---|---|\n"
         "| **Opening** (*'विपदाओं से मुझे बचाओ, यह मेरी प्रार्थना नहीं'*) | I do not pray to be saved from troubles; I only ask that I may **never be afraid** of them. |\n"
         "| **Sorrow** | If you do not comfort my pained heart, that is fine; but let me always be able to **conquer sorrow**. |\n"
         "| **No helper** | If I find no helper anywhere, let my **own strength and courage (बल-पौरुष)** not shake. |\n"
         "| **Loss and deceit** | If I suffer loss in the world and get only **deceit (वंचना)** instead of gain, let my mind still **not accept defeat (क्षय)**. |\n"
         "| **Saving** | I do not ask you to save me every day; give me the **healthy strength to cross over (तरने की शक्ति अनामय)** myself. |\n"
         "| **Burden** | Even if you do not lighten my burden or console me, let me **carry it without fear**. |\n"
         "| **Happy days** | In days of happiness, let me bow my head and **recognise your face every moment**. |\n"
         "| **Night of sorrow** | On the day the whole world deceives me in my night of sorrow, let me **never doubt you**. |")

sections = [
 {"id": "s1", "title": "A prayer for strength, not rescue", "blocks": [
  blk("s1.hook", "hook", title="A different kind of prayer",
    body="Most prayers ask God to remove our troubles. This prayer says the opposite: **'Do not save me from troubles; just make me fearless in them.'**\n\n"
         "The poet does not want God to do his work for him. He wants the **courage, strength and faith** to face life himself. That is why the poem is called **आत्मत्राण**, 'saving oneself'."),
  blk("s1.inspiration", "inspiration", title="The poet", person="Rabindranath Tagore", years="1861–1941",
    body="**Rabindranath Tagore** was born in **Kolkata**. In **1913** he became the **first Asian to win the Nobel Prize for Literature**, for **Gitanjali**. He wrote India's national anthem **'जन गण मन'** and Bangladesh's **'आमार सोनार बांग्ला'**, and founded **Shantiniketan** (Visva-Bharati).\n\n"
         "He wrote mainly in **Bengali**. This prayer-song was translated into Hindi by the scholar **Acharya Hazari Prasad Dwivedi**.",
    future="Tagore's call for inner strength is useful before every exam, interview or hard choice."),
  C.socratic("s1.socratic", "What does the poet really ask God for?",
    ["Courage and strength to face troubles himself", "Freedom from all troubles", "Wealth and success"], 0,
    "He does not ask to be rescued.")
 ]},
 {"id": "s2", "title": "The prayer and its meaning", "blocks": [
  blk("s2.note", "theory", title="How to read this chapter",
    body="Read the full poem in your **NCERT Sparsh Part 2** textbook. The table below explains each part, with key lines quoted so you can find them."),
  blk("s2.table", "markdown_table", title="What the poet asks", revision=True, body=PARTS),
  C.kc("s2.check", "What does the poet ask for in place of being saved from troubles?",
    [("that he should never be afraid of troubles", ""), ("that troubles never come", "He does not ask that."), ("that God fights for him", "He wants to fight himself."), ("that others help him", "He relies on himself.")],
    "'केवल इतना हो, कभी न विपदा में पाऊँ भय'.")
  ,C.kc("s2.check2", "What does the poet want if he finds no helper?",
    [("that his own strength and courage do not shake", ""), ("that God sends a helper", "He relies on himself."), ("that he gives up", "The opposite."), ("that he runs away", "The opposite.")],
    "'तो अपना बल पौरुष न हिले'.")
 ]},
 {"id": "s3", "title": "The message of the prayer", "blocks": [
  blk("s3.thm", "theory", title="Ideas in the poem", revision=True,
    body="**Fearlessness, not escape:** the poet accepts that troubles will come; he asks only to be unafraid.\n\n"
         "**Self-reliance:** he wants to win over sorrow, keep his own strength when no one helps, and **cross the ocean of life himself**.\n\n"
         "**Strong mind:** even in loss and deceit, he will not accept defeat in his heart.\n\n"
         "**Carrying the burden:** he does not ask for a lighter load, only the courage to carry it without fear.\n\n"
         "**Faith in good times and bad:** in happy days he will remember God with humility; in the darkest night, even if the whole world deceives him, he will **not doubt God**.\n\n"
         "**Title:** **आत्मत्राण** = आत्म (self) + त्राण (protection, rescue): saving oneself through one's own strength, with faith in God."),
  C.kc("s3.check", "'आत्मत्राण' means:",
    [("saving oneself", ""), ("praying to God", "It means self-rescue."), ("fear of death", "Self-rescue."), ("a holy song", "Self-rescue.")],
    "आत्म + त्राण.")
  ,C.kc("s3.check2", "What does the poet promise in the night of sorrow?",
    [("never to doubt God", ""), ("to stop praying", "The opposite."), ("to blame the world", "He keeps faith."), ("to hide from people", "He keeps faith.")],
    "'तुम पर करूँ नहीं कुछ संशय'.")
 ]},
 {"id": "s4", "title": "Language and style", "blocks": [
  blk("s4.thm", "theory", title="Language and devices", revision=True,
    body="| Feature | Example / note |\n|---|---|\n| **Language** | **तत्सम**-rich **खड़ी बोली** (translation): *विपदा, त्राण, अनामय, वंचना, क्षय, अनुनय, निखिल, मही, संशय* |\n"
         "| **Form** | a **prayer-song (प्रार्थना-गीत)** with a gentle, musical flow |\n| **Repeated phrase** | *'करुणामय'*, addressing God as the merciful one |\n"
         "| **Contrast** | *सुख के दिन* vs *दुःख-रात्रि* |\n| **अनुप्रास (alliteration)** | *'बल पौरुष'*, *'छिन-छिन'* |\n| **पुनरुक्ति प्रकाश** | *'छिन-छिन'* |\n\n"
         "**How it differs from other prayers:** others ask God to remove troubles; this one asks for **courage, self-reliance and unshaken faith**."),
  C.kc("s4.check", "Who translated this poem into Hindi?",
    [("Acharya Hazari Prasad Dwivedi", ""), ("Maithilisharan Gupt", "Dwivedi."), ("Sumitranandan Pant", "Dwivedi."), ("Tagore himself", "Dwivedi.")],
    "Tagore wrote it in Bengali.")
 ]},
 closing(C,
   "- **Not 'save me', but 'make me fearless'.**\n- **Asks: निर्भय, दुख पर जय, अपना बल-पौरुष, क्षय न मानूँ, तरने की शक्ति, भार निर्भय वहन, सुख में स्मरण, दुख में संशय नहीं.**\n- **Tagore (Bengali, Nobel 1913) → Hindi by Hazari Prasad Dwivedi.**",
   "1. Writing that the poet asks to be saved from troubles: he asks for **courage** in them.\n2. Writing that he loses faith in sorrow: he says he will **not doubt** God.\n"
   "3. Saying Tagore wrote it in Hindi: he wrote in **Bengali**; it was translated.\n4. Writing exam answers in English: answer in **Hindi**.",
   "Ask students to compare this prayer with their school prayer: what does each ask for?",
   "Think of a difficult moment you faced alone. What helped you more: help from others, or your own courage?",
   "- **Manushyata (Ch 3):** courage and service.\n- **Moral science:** self-reliance (स्वावलंबन).",
   "How is 'आत्मत्राण' different from usual prayers? Answer in about 60 words.",
   "Usual prayers ask God to remove troubles, give comfort and fulfil wishes. In 'आत्मत्राण', Tagore does not ask to be saved from troubles. He asks for courage to face them, strength to conquer sorrow, the power to cross life's ocean himself and to carry his burden without fear. He also asks never to doubt God, even when the whole world deceives him. It is a prayer for self-reliance.",
   "- Tagore's prayer, translated by Hazari Prasad Dwivedi, asks for fearlessness, not rescue.\n- He wants to conquer sorrow, keep his strength when no one helps, and not accept defeat in loss.\n"
   "- He asks for strength to cross over himself and carry his burden without fear.\n- He will remember God humbly in happy days and never doubt Him in sorrow.",
   "- Answer in Hindi, in 25-30 words for 2 marks.\n- Show the contrast: 'not ... but ...'.\n- Explain the title as आत्म + त्राण.",
   [("What does the poet not pray for?", "To be saved from troubles, or to be consoled."),
    ("What does 'तरने की हो शक्ति अनामय' ask for?", "Healthy, unbroken strength to cross life's troubles himself.")]),
]

# ---------------- NCERT प्रश्न-अभ्यास (क) ----------------
C.two("pa1", FAITH, "To whom is the poet praying, and what is he praying for?",
      ["The poet is praying to God (the merciful one).", "He asks not to be freed from troubles, but for courage, strength and self-confidence to face them."], PE(1))
C.two("pa2", COURAGE, "What does the poet want to say through 'विपदाओं से मुझे बचाओ, यह मेरी प्रार्थना नहीं'?",
      ["He does not want God to save him from troubles.", "He wants the strength to face them without fear, through his own effort."], PE(2))
C.two("pa3", SELF, "What does the poet pray for if he finds no helper?",
      ["He prays that even if no one helps him, his own strength and courage should not shake.", "He wants to face difficulties with self-confidence."], PE(3))
C.two("pa4", FAITH, "What does the poet plead for at the end?",
      ["He pleads that on the day the whole world deceives him in his night of sorrow,", "he should not have any doubt about God."], PE(4))
C.two("pa5", SELF, "Explain how the title 'आत्मत्राण' suits the poem.",
      ["आत्मत्राण means saving oneself by one's own strength.", "The poet asks God not for rescue but for courage to save himself, so the title is fitting."], PE(5), "medium")
C.two("pa6", SELF, "Besides praying, what efforts do you make to fulfil your wishes? Write.",
      ["Besides praying, I work hard, plan carefully and practise regularly.", "I take advice from elders and teachers and keep trying even after failure."], PE(6))
C.two("pa7", FAITH, "Does this prayer seem different from other prayer songs to you? If yes, how?",
      ["Yes; other prayers ask God to remove troubles and grant wishes.", "This prayer asks for courage, self-reliance and faith to face troubles oneself."], PE(7), "medium")
# ---------------- NCERT (ख) भाव ----------------
C.two("bh1", FAITH, "Explain the idea: 'नत शिर होकर सुख के दिन में तव मुख पहचानूँ छिन-छिन में'.",
      ["In days of happiness the poet wants to stay humble and bow his head before God.", "He wants to remember God every moment, not only in sorrow."], BH(1))
C.two("bh2", COURAGE, "Explain the idea: 'हानि उठानी पड़े जगत में लाभ अगर वंचना रही तो भी मन में ना मानूँ क्षय'.",
      ["Even if he suffers loss in the world and gets only deceit instead of gain,", "the poet does not want to accept defeat in his mind; his spirit should stay strong."], BH(2))
C.two("bh3", SELF, "Explain the idea: 'तरने की हो शक्ति अनामय, मेरा भार अगर लघु करके न दो सांत्वना नहीं सही'.",
      ["The poet asks for healthy strength to cross life's troubles himself.", "Even if God does not lighten his burden or console him, he will carry it without complaint."], BH(3), "medium")

# ---------------- Extracts (short quotations) ----------------
C.extract("ext1", COURAGE, "विपदाओं से मुझे बचाओ, यह मेरी प्रार्थना नहीं\nकेवल इतना हो (करुणामय) कभी न विपदा में पाऊँ भय।",
  [("To whom is the prayer made?", "To God, the merciful one (करुणामय)."), ("What does the poet not ask for?", "To be saved from troubles."),
   ("What does he ask for instead?", "That he should never feel fear in troubles."), ("What does 'विपदा' mean?", "Trouble, calamity."), ("What quality does the poet want?", "Fearlessness and courage.")])
C.extract("ext2", SELF, "कोई कहीं सहायक न मिले\nतो अपना बल पौरुष न हिले",
  [("What situation does the poet imagine?", "Finding no helper anywhere."), ("What should not shake?", "His own strength and courage."),
   ("What does 'पौरुष' mean?", "Manliness, courage, effort."), ("Which value do these lines show?", "Self-reliance (आत्मनिर्भरता)."), ("What does 'सहायक' mean?", "Helper.")])

# ---------------- Objective practice ----------------
C.m("mcq01", COURAGE, "The poet does not pray to be:", [("saved from troubles", ""), ("made fearless", "He asks for that."), ("given strength", "He asks for that."), ("given faith", "He asks for that.")], "'यह मेरी प्रार्थना नहीं'.")
C.m("mcq02", COURAGE, "The poet wants never to feel:", [("fear in troubles", ""), ("happiness", "Fear."), ("faith", "Fear."), ("love", "Fear.")], "'कभी न विपदा में पाऊँ भय'.")
C.m("mcq03", COURAGE, "What does the poet want to do with sorrow?", [("conquer it", ""), ("avoid it", "Conquer."), ("hide it", "Conquer."), ("give it to others", "Conquer.")], "'दुख को मैं कर सकूँ सदा जय'.")
C.m("mcq04", SELF, "'पौरुष' means:", [("courage, effort", ""), ("wealth", "Courage."), ("fear", "Courage."), ("prayer", "Courage.")], "'बल पौरुष न हिले'.")
C.m("mcq05", COURAGE, "'वंचना' means:", [("deceit", ""), ("gain", "Deceit."), ("prayer", "Deceit."), ("help", "Deceit.")], "Instead of gain.")
C.m("mcq06", COURAGE, "'क्षय' in the poem means:", [("loss, defeat", ""), ("victory", "Loss."), ("peace", "Loss."), ("prayer", "Loss.")], "'मन में ना मानूँ क्षय'.")
C.m("mcq07", SELF, "'त्राण' means:", [("protection, rescue", ""), ("fear", "Rescue."), ("sorrow", "Rescue."), ("prayer", "Rescue.")], "आत्मत्राण = self-rescue.")
C.m("mcq08", SELF, "'अनामय' means:", [("healthy, free from illness", ""), ("nameless", "Healthy."), ("weak", "Healthy."), ("sad", "Healthy.")], "'तरने की हो शक्ति अनामय'.")
C.m("mcq09", SELF, "The poet wants the strength to:", [("cross life's troubles himself", ""), ("be carried across by God", "Himself."), ("avoid the river", "Himself."), ("stay where he is", "Cross over.")], "'तरने की हो शक्ति'.")
C.m("mcq10", SELF, "About his burden, the poet asks to:", [("carry it without fear", ""), ("have it removed", "He accepts it."), ("give it to others", "He carries it."), ("drop it", "He carries it.")], "'वहन कर सकूँ इसको निर्भय'.")
C.m("mcq11", FAITH, "In happy days, the poet wants to:", [("bow his head and remember God", ""), ("forget God", "Remember."), ("enjoy only", "Remember God."), ("ask for more", "Remember God.")], "'नत शिर होकर सुख के दिन में'.")
C.m("mcq12", FAITH, "'छिन-छिन' means:", [("every moment", ""), ("slowly", "Every moment."), ("sometimes", "Every moment."), ("never", "Every moment.")], "क्षण-क्षण.")
C.m("mcq13", FAITH, "'निखिल मही' means:", [("the whole earth (world)", ""), ("a small village", "Whole world."), ("the sky", "Earth."), ("the sea", "Earth.")], "When the whole world deceives.")
C.m("mcq14", FAITH, "In the night of sorrow, the poet will not:", [("doubt God", ""), ("pray", "He keeps faith."), ("cry", "He keeps faith."), ("sleep", "He keeps faith.")], "'तुम पर करूँ नहीं कुछ संशय'.")
C.m("mcq15", FAITH, "'करुणामय' is used for:", [("God", ""), ("the poet", "God."), ("the world", "God."), ("a friend", "God.")], "The merciful one.")
C.m("mcq16", CRAFT, "The original poem was written in:", [("Bengali", ""), ("Hindi", "Translated into Hindi."), ("Sanskrit", "Bengali."), ("English", "Bengali.")], "By Tagore.")
C.m("mcq17", CRAFT, "Tagore won the Nobel Prize in:", [("1913", ""), ("1931", "1913."), ("1947", "1913."), ("1901", "1913.")], "For Gitanjali.")
C.m("mcq18", CRAFT, "Tagore founded:", [("Shantiniketan", ""), ("Sabarmati Ashram", "That was Gandhi."), ("Banaras Hindu University", "That was Malaviya."), ("Aligarh Muslim University", "That was Sir Syed.")], "Visva-Bharati.")
C.m("mcq19", CRAFT, "This poem is mainly a:", [("prayer-song", ""), ("patriotic song", "Prayer."), ("love poem", "Prayer."), ("nature poem", "Prayer.")], "Addressed to God.")
C.m("mcq20", SELF, "The central value of the poem is:", [("self-reliance with faith", ""), ("dependence on others", "Self-reliance."), ("fear of God", "Faith without fear."), ("love of wealth", "Self-reliance.")], "आत्मत्राण.")
C.tf("tf1", COURAGE, "The poet prays that troubles never come to him.", False, "He asks only to be fearless in them.")
C.tf("tf2", SELF, "The poet wants to keep his own strength even when no one helps.", True, "'अपना बल पौरुष न हिले'.")
C.tf("tf3", SELF, "The poet asks God to carry his burden for him.", False, "He wants to carry it himself.")
C.tf("tf4", FAITH, "The poet will not doubt God even when the world deceives him.", True, "Last lines.")
C.tf("tf5", CRAFT, "Tagore wrote 'आत्मत्राण' in Hindi.", False, "Bengali; translated by Dwivedi.")
C.tf("tf6", FAITH, "In happy days, the poet wants to stay humble.", True, "'नत शिर होकर'.")
C.two("sa1", COURAGE, "Why does the poet not ask to be saved from troubles?",
      ["He believes troubles are part of life and make a person strong.", "He wants to face them with his own courage, not depend on God's help."], difficulty="medium")
C.two("sa2", SELF, "How can a student use the message of this poem?",
      ["A student can face exams and failures with courage instead of fear.", "He should rely on his own hard work while keeping faith in God."])
C.two("sa3", FAITH, "Why does the poet remember God even in days of happiness?",
      ["People often remember God only in sorrow and forget Him in happiness.", "The poet wants to stay humble and grateful in good times too."])
C.two("sa4", COURAGE, "What is meant by 'दुख को मैं कर सकूँ सदा जय'?",
      ["The poet wants to always win over sorrow.", "He does not want comfort; he wants the strength to overcome pain himself."])

chapter = header("sparsh", "ch06", 6, "आत्मत्राण", "रवींद्रनाथ ठाकुर (अनुवाद: हजारी प्रसाद द्विवेदी)", "poem", ["fearless_courage", "self_reliance", "faith_in_god", "prayer_craft"],
                 "CBSE 2025-26 Hindi Course B (085), Section C: Sparsh Part 2 poetry. Assessed through extract-based MCQs (1 mark each) and short answers in 25-30 words (2 marks); answers are written in Hindi. The Hindi translation is in copyright: read the full text in the NCERT textbook.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
