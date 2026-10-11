"""CBSE Class 10 English, First Flight Ch 2: Nelson Mandela: Long Walk to Freedom."""
import sys
from lit_common import make, header, path, ex

ROOT = sys.argv[1]
PATH = path("ch02_nelson_mandela_long_walk_to_freedom")
C = make("ff10ch02")
blk = C.blk
DAY, APART, COURAGE, FREE, LANG = ["inauguration_day"], ["apartheid_and_its_legacy"], ["courage_and_character"], ["meaning_of_freedom"], ["vocabulary_and_style"]
OCC = lambda n: ex(n, "Oral Comprehension Check")

TIMELINE = ("| Time | What happened |\n|---|---|\n"
            "| **First decade of the 20th century** | after the Anglo-Boer war, white South Africans patched up their differences and set up a system of racial domination over dark-skinned people: the basis of **apartheid** |\n"
            "| **Mandela's boyhood** | felt 'born free': ran in the fields, swam in streams, roasted mealies under the stars |\n"
            "| **As a young man** | realised his freedom was an illusion; joined the African National Congress to fight for his people's freedom |\n"
            "| **Nearly three decades in prison (27 years)** | kept his belief in human goodness alive |\n"
            "| **10 May 1994** | sworn in as South Africa's first Black President at the Union Buildings, Pretoria |")
FREEDOM = ("| Stage of life | What freedom meant |\n|---|---|\n"
           "| **Boyhood** | to run, swim, roast mealies and ride bulls; freedom as long as he obeyed his father and tribal customs |\n"
           "| **Student** | 'transitory freedoms': to stay out at night, read what he pleased and go where he chose |\n"
           "| **Young man in Johannesburg** | the basic, honourable freedoms: to earn a living, marry and have a family, live a lawful life |\n"
           "| **Freedom fighter** | freedom of all his people; 'the chains on any one of my people were the chains on all of them' |\n"
           "| **President** | liberating the oppressor as well as the oppressed |")

sections = [
 {"id": "s1", "title": "A day of hope", "blocks": [
  blk("s1.hook", "hook", title="From prisoner to President",
    body="On **10 May 1994**, a man who had spent nearly three decades in prison took the oath as **President** of his country, and generals who once would have arrested him saluted him.\n\n"
         "This chapter is taken from **Long Walk to Freedom**, the autobiography of **Nelson Mandela**. It tells of that day, of the system called **apartheid**, and of what Mandela learnt about **courage** and **freedom**."),
  blk("s1.inspiration", "inspiration", title="The writer", person="Nelson Rolihlahla Mandela", years="1918–2013",
    body="Nelson Mandela led the struggle against **apartheid**, the system of racial discrimination in South Africa. He was imprisoned for 27 years, released in 1990, and in 1994 became the country's **first Black President** after the first democratic elections.\n\n"
         "He shared the **Nobel Peace Prize (1993)** with F. W. de Klerk and is remembered across the world as a symbol of forgiveness and freedom.",
    future="Leaders in law, public service and human rights study Mandela to learn how courage and forgiveness can change a nation."),
  C.socratic("s1.socratic", "Mandela says 'the oppressor must be liberated just as surely as the oppressed'. Why might the oppressor not be free?",
    ["Hatred and prejudice imprison the mind of the one who oppresses others", "The oppressor is locked in a real jail", "The oppressor has no money"], 0,
    "A man who takes away another man's freedom is a 'prisoner of hatred'."),
 ]},
 {"id": "s2", "title": "10 May 1994: the inauguration", "blocks": [
  blk("s2.thm", "theory", title="The day of the inauguration", revision=True,
    body="**The setting:** the ceremony took place in the lovely sandstone amphitheatre of the **Union Buildings in Pretoria**, for decades the seat of white supremacy. 10 May was 'bright and clear', an autumn day in the southern hemisphere. Politicians and dignitaries from **more than 140 countries** attended: the largest gathering of international leaders on South African soil.\n\n"
         "**The oath:** first **Mr de Klerk** was sworn in as second deputy president, then **Thabo Mbeki** as first deputy president, and then Mandela as President.\n\n"
         "**The speech:** Mandela called the end of apartheid a 'glorious ... human victory' after 'an extraordinary human disaster' that had lasted too long. He thanked the international leaders for coming to take possession, with the people of South Africa, of 'a common victory for justice, for peace, for human dignity'. He promised to liberate all the people from the continuing bondage of **poverty, deprivation, suffering, gender and other discrimination**: 'Never, never and never again shall it be that this beautiful land will again experience the oppression of one by another... Let freedom reign. God bless Africa!'\n\n"
         "**The military:** a spectacular array of South African **jets, helicopters and troop carriers** flew in perfect formation over the Union Buildings. The highest generals saluted Mandela and pledged their loyalty. Mandela notes that 'not so many years before' they would have **arrested** him instead. The display showed the military's loyalty to democracy.\n\n"
         "**Two anthems:** the whites sang **'Nkosi Sikelel–iAfrika'** and the blacks sang **'Die Stem'**, the old anthem of the Republic. Each group sang the other's song: a sign of a new, united nation."),
  blk("s2.table", "markdown_table", title="Mandela's journey at a glance", revision=True, body=TIMELINE),
  C.kc("s2.check", "Why were two national anthems sung at the ceremony?",
    [("to show that the whites and the blacks now belonged to one nation", ""), ("because one anthem was too short", "It was a symbol of unity."),
     ("because the guests asked for it", "It was the new nation's choice."), ("to please only the white people", "Both groups sang.")],
    "The whites sang 'Nkosi Sikelel–iAfrika' and the blacks sang 'Die Stem'.")
  ,C.kc("s2.check2", "What did the military generals do on 10 May 1994?",
    [("saluted Mandela and pledged their loyalty", ""), ("arrested Mandela", "That is what they might have done years before."),
     ("refused to attend", "They took part."), ("left the country", "They stayed and pledged loyalty.")],
    "Their change shows the power of the struggle and of democracy.")
 ]},
 {"id": "s3", "title": "Apartheid, courage and character", "blocks": [
  blk("s3.thm", "theory", title="What oppression taught Mandela", revision=True,
    body="**Apartheid:** in the first decade of the twentieth century, a few years after the bitter **Anglo-Boer war**, the white-skinned peoples of South Africa patched up their differences and set up a system of racial domination against the dark-skinned peoples. It became 'one of the harshest, most inhumane societies the world has ever known'. In the last decade of the century, that system was overturned and replaced by one that recognised the **rights and freedoms of all**, whatever the colour of their skin.\n\n"
         "**Depths of oppression create heights of character:** apartheid created 'a deep and lasting wound', but it also produced men of extraordinary courage, wisdom and generosity: **Oliver Tambo, Walter Sisulu, Chief Luthuli, Yusuf Dadoo, Bram Fischer, Robert Sobukwe**. Mandela says South Africa is rich in minerals and gems, but **its greatest wealth is its people**, 'finer and truer than the purest diamonds'.\n\n"
         "**Courage:** 'I learned that courage was not the absence of fear, but the **triumph over it**. The brave man is not he who does not feel afraid, but he who conquers that fear.'\n\n"
         "**Love and hate:** 'No one is born hating another person because of the colour of his skin... People must learn to hate, and if they can learn to hate, they can be taught to love, for **love comes more naturally** to the human heart than its opposite.' Even in prison, a glimpse of humanity in a guard reassured him that 'man's goodness is a flame that can be hidden but never extinguished'.\n\n"
         "**Twin obligations:** every man has obligations to his **family** (parents, wife, children) and to his **people, community and country**. In apartheid South Africa, a man of colour who tried to fulfil his duty to his people was torn from his family and forced into 'a twilight existence of secrecy and rebellion'."),
  C.kc("s3.check", "According to Mandela, courage is:",
    [("the triumph over fear", ""), ("the absence of fear", "He says it is not the absence of fear."), ("never feeling afraid", "The brave man does feel afraid."), ("anger against enemies", "It is about conquering fear.")],
    "'The brave man is not he who does not feel afraid, but he who conquers that fear.'")
  ,C.kc("s3.check2", "What does Mandela call his country's greatest wealth?",
    [("its people", ""), ("its diamonds", "He says people are finer than diamonds."), ("its gold mines", "He says people are its greatest wealth."), ("its army", "He praises the people.")],
    "They are 'finer and truer than the purest diamonds'.")
 ]},
 {"id": "s4", "title": "Freedom: how Mandela's idea grew", "blocks": [
  blk("s4.thm", "theory", title="From personal freedom to freedom for all", revision=True,
    body="**As a boy** Mandela felt 'born free', free to run in the fields near his mother's hut, swim in the clear stream, roast **mealies** under the stars and ride the broad backs of slow-moving bulls, as long as he obeyed his father and the customs of his tribe.\n\n"
         "**As a student** he wanted 'transitory freedoms': to stay out at night, read what he pleased and go where he chose.\n\n"
         "**As a young man** in Johannesburg he yearned for the 'basic and honourable freedoms' of achieving his potential, earning his keep, marrying and having a family. He then saw that **his brothers and sisters were not free** either. 'The chains on any one of my people were the chains on all of them.' His **hunger for his own freedom became the greater hunger for the freedom of his people**: it turned a frightened young man into a bold one, a law-abiding attorney into a 'criminal', and a family-loving husband into a man without a home.\n\n"
         "**The oppressor is not free:** 'A man who takes away another man's freedom is a **prisoner of hatred**, he is locked behind the bars of prejudice and narrow-mindedness.' So the oppressor must be liberated as surely as the oppressed."),
  blk("s4.table", "markdown_table", title="Freedom at different stages of life", revision=True, body=FREEDOM),
  C.kc("s4.check", "Why does Mandela say the oppressor is not free?",
    [("he is a prisoner of hatred, prejudice and narrow-mindedness", ""), ("he is kept in jail", "It is a mental prison."),
     ("he has no rights", "He holds power, but is ruled by hate."), ("he is poor", "It is about hatred, not money.")],
    "Both the oppressor and the oppressed are robbed of their humanity.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Date and place: 10 May 1994, Union Buildings, Pretoria; 140+ countries.**\n- **Deputies: de Klerk (second), Thabo Mbeki (first).**\n"
         "- **Anthems swapped: whites sang Nkosi Sikelel–iAfrika, blacks sang Die Stem.**\n- **Courage = triumph over fear. Wealth = people. Oppressor = prisoner of hatred.**\n"
         "- **Freedom ladder: boy → student → young man → his people → everyone.**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Mixing up the anthems: each group sang the **other** group's anthem.\n2. Saying Mandela had no fear: he says courage is **conquering** fear, not having none.\n"
         "3. Saying de Klerk was first deputy: **Thabo Mbeki** was first deputy president, de Klerk second.\n4. Writing 'apartheid' as a place or a person: it is a **system of racial segregation**."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Draw a 'freedom ladder' on the board with five steps (boy, student, young man, freedom fighter, President). Students fill each step with one quotation from the chapter. It makes Thinking about the Text Q4 easy."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Mandela says people learn to hate, so they can be taught to love. Think of one way schools can teach people to respect those who are different from them."),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **History (Nationalism in India):** compare Mandela's struggle with India's freedom movement and Gandhiji, who also began his work in South Africa.\n"
         "- **Civics (Power-sharing, Outcomes of Democracy):** how a democracy treats all its people with dignity.\n- **The Sermon at Benares:** another lesson on facing suffering."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="'Depths of oppression create heights of character.' Explain with reference to the chapter in about 120 words.\n\n"
         "**Model answer:** Mandela believes that great suffering brings out great qualities in people. Apartheid was one of the harshest systems in the world: dark-skinned people lost their rights, and those who fought for freedom were jailed or separated from their families. Yet this cruelty produced leaders of extraordinary courage, wisdom and generosity, such as Oliver Tambo, Walter Sisulu, Chief Luthuli and Robert Sobukwe. Their sacrifices taught Mandela what courage means: not the absence of fear, but the triumph over it. He concludes that South Africa's greatest wealth is not its diamonds but its people. In India too, the freedom struggle produced leaders like Gandhiji and Bhagat Singh, showing that oppression can create heights of character."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- On 10 May 1994 Mandela became South Africa's first Black President at the Union Buildings, Pretoria, before leaders from over 140 countries.\n"
         "- Jets flew past, generals saluted him, and the two groups sang each other's anthems: signs of a new, united nation.\n"
         "- Apartheid, set up after the Anglo-Boer war, was a cruel system of racial domination; it also created heroes of great character.\n"
         "- Courage is the triumph over fear; love comes more naturally than hate; a country's greatest wealth is its people.\n"
         "- Mandela's idea of freedom grew from his own freedom to the freedom of all; the oppressor too must be freed from hatred."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- Learn four key quotations (courage, love and hate, greatest wealth, prisoner of hatred): one quotation lifts any answer.\n"
         "- For 'How did his idea of freedom change?', write the stages in order (boy, student, young man, freedom fighter).\n"
         "- In long answers on character or values, link the text to India's freedom struggle or present-day examples for 'beyond the text' marks."),
  blk("s5.flash1", "flashcard", front="When and where was Mandela sworn in as President?", back="10 May 1994, in the amphitheatre of the Union Buildings, Pretoria."),
  blk("s5.flash2", "flashcard", front="What is courage, according to Mandela?", back="Not the absence of fear, but the triumph over it."),
  blk("s5.flash3", "flashcard", front="What are Mandela's 'twin obligations'?", back="To his family, and to his people, community and country."),
  blk("s5.flash4", "flashcard", front="Why must the oppressor also be liberated?", back="He is a prisoner of hatred, locked behind bars of prejudice and narrow-mindedness."),
 ]},
]

# ---------------- NCERT: Oral Comprehension Check ----------------
C.vsa("occ1", DAY, "Where did the ceremonies take place? Can you name any public buildings in India that are made of sandstone?",
      ["In the sandstone amphitheatre of the Union Buildings in Pretoria.", "Sandstone buildings in India: the Red Fort, Rashtrapati Bhavan, Parliament House (Sansad Bhavan)."], OCC(1))
C.vsa("occ2", DAY, "Can you say how 10 May is an 'autumn day' in South Africa?",
      ["South Africa is in the southern hemisphere, where the seasons are opposite to India's.", "So May, which is summer in India, falls in autumn there."], OCC(2))
C.vsa("occ3", APART, "At the beginning of his speech, Mandela mentions 'an extraordinary human disaster'. What does he mean by this?",
      ["He means apartheid, the system of racial discrimination.", "Black people were denied rights and dignity for a very long time."], OCC(3))
C.vsa("occ4", DAY, "What is the 'glorious... human achievement' he speaks of at the end?",
      ["The end of apartheid and the setting up of a democratic, non-racial government.", "A Black man becoming President of a country that once denied Black people their rights."], OCC(4))
C.vsa("occ5", DAY, "What does Mandela thank the international leaders for?",
      ["For coming to the inauguration and sharing the victory for justice, peace and human dignity.", "For their support to the people of South Africa during the struggle."], OCC(5))
C.vsa("occ6", DAY, "What ideals does he set out for the future of South Africa?",
      ["To free all people from poverty, deprivation, suffering, gender and other discrimination.", "That the land should never again know the oppression of one by another: 'Let freedom reign.'"], OCC(6))
C.vsa("occ7", DAY, "What did the military generals do? How did their attitude change, and why?",
      ["They saluted Mandela and pledged their loyalty.", "Years before they would have arrested him; the long struggle and many sacrifices brought democracy and changed their attitude."], OCC(7))
C.vsa("occ8", DAY, "Why were two national anthems sung?",
      ["To show respect for both the white and the Black communities.", "The whites sang 'Nkosi Sikelel–iAfrika' and the blacks sang 'Die Stem', a sign of unity."], OCC(8))
C.vsa("occ9", APART, "How does Mandela describe the systems of government in his country (i) in the first decade, and (ii) in the final decade, of the twentieth century?",
      ["(i) A system of racial domination by white people over dark-skinned people.", "(ii) A system that recognised the rights and freedoms of all, whatever the colour of their skin."], OCC(9))
C.vsa("occ10", COURAGE, "What does courage mean to Mandela? Which does he think is natural, to love or to hate?",
      ["Courage is not the absence of fear but the triumph over it.", "He thinks love comes more naturally to the human heart than hate."], OCC(10))
C.vsa("occ11", FREE, "What 'twin obligations' does Mandela mention?",
      ["Obligations to his family: parents, wife and children.", "Obligations to his people, community and country."], OCC(11))
C.vsa("occ12", FREE, "What did being free mean to Mandela as a boy, and as a student?",
      ["As a boy: to run in the fields, swim in streams, roast mealies and ride bulls.", "As a student: to stay out at night, read what he pleased and go where he chose."], OCC(12))
C.vsa("occ13", FREE, "Does Mandela think the oppressor is free? Why/Why not?",
      ["No.", "The oppressor is a prisoner of hatred, locked behind the bars of prejudice and narrow-mindedness."], OCC(13))

# ---------------- NCERT: Thinking about the Text ----------------
C.sa("ex1", DAY, "Why did such a large number of international leaders attend the inauguration? What did it signify?",
     ["Leaders from more than 140 countries came to show support for the end of apartheid and the new democracy.",
      "It signified the world's recognition of the victory of justice, peace and human dignity in South Africa."], ex(1))
C.sa("ex2", COURAGE, "What does Mandela mean when he says he is 'simply the sum of all those African patriots' who had gone before him?",
     ["He gives credit to the many freedom fighters who struggled and sacrificed before him.", "His achievement rests on their courage; he sees himself as the continuation of their struggle."], ex(2))
C.sa("ex3", COURAGE, "Would you agree that the 'depths of oppression' create 'heights of character'? How does Mandela illustrate this? Can you add your own examples?",
     ["Yes: apartheid produced leaders of great courage and generosity such as Oliver Tambo, Walter Sisulu and Chief Luthuli.",
      "Indian examples: Mahatma Gandhi and Bhagat Singh grew great through the struggle against British rule."], ex(3))
C.sa("ex4", FREE, "How did Mandela's understanding of freedom change with age and experience?",
     ["As a boy, freedom meant playing freely; as a student, staying out late and reading what he liked.",
      "As a young man he wanted the basic freedoms of earning a living and raising a family; then he saw that his people were not free and fought for their freedom."], ex(4))
C.sa("ex5", FREE, "How did Mandela's 'hunger for freedom' change his life?",
     ["His hunger for his own freedom became a hunger for the freedom of his people.", "It made a frightened young man bold, a lawyer a 'criminal', and a family man homeless, leading to years in prison."], ex(5))

# ---------------- Extracts ----------------
C.extract("ext1", DAY,
  "Tenth May dawned bright and clear. For the past few days I had been pleasantly besieged by dignitaries and world leaders\nwho were coming to pay their respects before the inauguration.\nThe inauguration would be the largest gathering ever of international leaders on South African soil.",
  [("Who is 'I' in the extract?", "Nelson Mandela."),
   ("Why does he call 10 May a special day?", "It was the day of his inauguration as President."),
   ("Find a word that means 'surrounded'.", "Besieged."),
   ("Why does he say 'pleasantly' besieged?", "He was happy to meet the leaders who had come to honour him."),
   ("What did the large gathering show?", "The world's support for the new democracy.")])
C.extract("ext2", DAY,
  "A few moments later we all lifted our eyes in awe as a spectacular array of South African jets, helicopters and troop carriers\nroared in perfect formation over the Union Buildings.\nIt was not only a display of pinpoint precision and military force, but a demonstration of the military's loyalty to democracy.",
  [("Where did the planes fly?", "Over the Union Buildings in Pretoria."),
   ("Give a word from the extract that means 'wonder and respect'.", "Awe."),
   ("What did the display demonstrate?", "The military's loyalty to democracy."),
   ("Why was this significant?", "A few years earlier the army would have arrested Mandela."),
   ("Which phrase shows the flying was exact?", "'Pinpoint precision' / 'perfect formation'.")])
C.extract("ext3", COURAGE,
  "I learned that courage was not the absence of fear, but the triumph over it.\nThe brave man is not he who does not feel afraid, but he who conquers that fear.",
  [("Who learned this lesson?", "Nelson Mandela."),
   ("From whom did he learn it?", "From his comrades in the struggle."),
   ("What is courage, according to the extract?", "The triumph over fear."),
   ("Give the antonym of 'absence'.", "Presence."),
   ("Which word means 'defeats'?", "Conquers.")])
C.extract("ext4", FREE,
  "A man who takes away another man's freedom is a prisoner of hatred,\nhe is locked behind the bars of prejudice and narrow-mindedness.",
  [("Who is called 'a prisoner of hatred'?", "The oppressor, the man who takes away another's freedom."),
   ("What are 'the bars' he is locked behind?", "Prejudice and narrow-mindedness."),
   ("Name the figure of speech in 'bars of prejudice'.", "Metaphor."),
   ("What does Mandela conclude from this?", "The oppressor must be liberated just as surely as the oppressed."),
   ("Give a word from the extract meaning 'unfair opinion formed without reason'.", "Prejudice.")])

# ---------------- Objective practice ----------------
C.m("mcq01", DAY, "The inauguration ceremony took place in:",
    [("the Union Buildings, Pretoria", ""), ("Robben Island", "That was a prison."), ("Cape Town stadium", "It was in Pretoria."), ("Johannesburg city hall", "It was the Union Buildings.")],
    "A sandstone amphitheatre, once the seat of white supremacy.")
C.m("mcq02", DAY, "Who was sworn in as first deputy president?",
    [("Thabo Mbeki", ""), ("Mr de Klerk", "He was second deputy president."), ("Oliver Tambo", "He was a freedom fighter."), ("Walter Sisulu", "He was a freedom fighter.")],
    "De Klerk was sworn in first, as second deputy president.")
C.m("mcq03", DAY, "Leaders from about how many countries attended?",
    [("more than 140", ""), ("about 20", "It was the largest gathering ever."), ("exactly 50", "More than 140 countries came."), ("only African countries", "Leaders came from all over the world.")],
    "It was the largest gathering of international leaders on South African soil.")
C.m("mcq04", APART, "'Apartheid' means:",
    [("a system of racial segregation and discrimination", ""), ("a type of government building", "It is a political system."), ("a South African festival", "It is a system of oppression."), ("a freedom movement", "It was what the movement fought.")],
    "It separated people by the colour of their skin.")
C.m("mcq05", APART, "When was the system of racial domination set up?",
    [("in the first decade of the twentieth century, after the Anglo-Boer war", ""), ("in 1994", "That is when it ended."),
     ("in the 1800s, before any war", "It came after the Anglo-Boer war."), ("after the Second World War", "It was earlier, in the first decade.")],
    "The white-skinned peoples patched up their differences.")
C.m("mcq06", COURAGE, "Which of these is NOT named by Mandela as a hero of the struggle?",
    [("Thabo Mbeki", ""), ("Oliver Tambo", "He is named."), ("Walter Sisulu", "He is named."), ("Robert Sobukwe", "He is named.")],
    "Mbeki is mentioned as first deputy president, not in the list of heroes.")
C.m("mcq07", COURAGE, "'Depths of oppression create heights of character' means:",
    [("great suffering can bring out great qualities in people", ""), ("oppression makes people taller", "It is figurative."),
     ("oppressed people lose their character", "It means the opposite."), ("oppression should continue", "He opposes oppression.")],
    "Apartheid produced leaders of courage, wisdom and generosity.")
C.m("mcq08", COURAGE, "According to Mandela, which comes more naturally to the human heart?",
    [("love", ""), ("hate", "He says people must learn to hate."), ("fear", "He talks of love and hate."), ("anger", "He talks of love and hate.")],
    "'If they can learn to hate, they can be taught to love.'")
C.m("mcq09", COURAGE, "'Man's goodness is a flame that can be hidden but never extinguished.' Here 'extinguished' means:",
    [("put out completely", ""), ("made brighter", "It means the opposite."), ("hidden", "It can be hidden but not put out."), ("spread", "It means destroyed.")],
    "Mandela saw goodness even in prison guards.")
C.m("mcq10", FREE, "What did freedom mean to Mandela as a boy?",
    [("running in the fields, swimming and roasting mealies under the stars", ""), ("earning a living", "That was as a young man."),
     ("staying out at night", "That was as a student."), ("freedom for his people", "That came later.")],
    "He felt 'born free' as a boy.")
C.m("mcq11", FREE, "'Mealies' are:",
    [("maize or corn", ""), ("small animals", "They are roasted to eat."), ("songs", "They are food."), ("huts", "He roasted them.")],
    "A South African word for maize.")
C.m("mcq12", FREE, "'The chains on any one of my people were the chains on all of them' shows that freedom is:",
    [("indivisible", ""), ("unnecessary", "He gave his life for it."), ("only for a few", "He means freedom for all."), ("easy to get", "It took a long struggle.")],
    "No one is free while others are not.")
C.m("mcq13", FREE, "What did Mandela's hunger for freedom turn him into?",
    [("a bold man, a 'criminal' in the eyes of the law and a man without a home", ""), ("a rich lawyer", "He gave up a comfortable life."),
     ("a soldier", "He became a freedom fighter."), ("a teacher", "He became a freedom fighter.")],
    "It changed his whole life.")
C.m("mcq14", FREE, "Whom does Mandela call 'a prisoner of hatred'?",
    [("the oppressor", ""), ("the oppressed", "The oppressor is the one ruled by hate."), ("the prison guard only", "It is anyone who takes away freedom."), ("himself", "He is speaking of the oppressor.")],
    "He is locked behind bars of prejudice.")
C.m("mcq15", DAY, "Which anthem did the blacks sing?",
    [("Die Stem", ""), ("Nkosi Sikelel–iAfrika", "The whites sang this one."), ("God Save the Queen", "It was a South African anthem."), ("Jana Gana Mana", "That is India's anthem.")],
    "Each group sang the other's anthem.")
C.m("mcq16", DAY, "Mandela calls the end of apartheid:",
    [("a glorious human victory", ""), ("a human disaster", "That was apartheid itself."), ("a small change", "He calls it glorious."), ("a defeat", "It was a victory.")],
    "'Never, never and never again...'")
C.m("mcq17", COURAGE, "What is a country's greatest wealth, according to Mandela?",
    [("its people", ""), ("its minerals and gems", "People are finer than diamonds."), ("its army", "He says its people."), ("its land", "He says its people.")],
    "'Finer and truer than the purest diamonds.'")
C.m("mcq18", FREE, "'Transitory freedoms' are freedoms that:",
    [("last only a short time", ""), ("last forever", "Transitory means temporary."), ("belong to everyone", "They are personal and passing."), ("are given by law", "They are passing pleasures.")],
    "Staying out at night, reading what he pleased.")
C.m("mcq19", FREE, "Mandela's 'twin obligations' are to:",
    [("his family and his people", ""), ("his school and his job", "He speaks of family and nation."), ("God and the government", "He speaks of family and people."), ("his friends and enemies", "He speaks of family and people.")],
    "Apartheid made it impossible to fulfil both.")
C.m("mcq20", APART, "A man of colour who tried to serve his people under apartheid was:",
    [("torn from his family and forced into secrecy and rebellion", ""), ("rewarded by the government", "He was punished."), ("made a minister", "He was punished."), ("given land", "He was forced to live apart.")],
    "He lived 'a twilight existence of secrecy and rebellion'.")
C.tf("tf1", DAY, "The generals who saluted Mandela would once have arrested him.", True, "Not so many years before, they would have arrested him.")
C.tf("tf2", COURAGE, "Mandela says the brave man is one who never feels afraid.", False, "The brave man feels fear but conquers it.")
C.tf("tf3", FREE, "As a boy, Mandela felt he was born free.", True, "He was free to run, swim and play, as long as he obeyed his father and tribal customs.")
C.tf("tf4", DAY, "Mr de Klerk was sworn in as first deputy president.", False, "He was second deputy president; Thabo Mbeki was first deputy president.")

# ---------------- More written practice ----------------
C.sa("sa1", DAY, "What did the flypast of jets and helicopters symbolise?",
     ["It showed the military's precision and strength.", "Above all, it showed the army's loyalty to democracy and to the new, freely elected government."])
C.sa("sa2", COURAGE, "How did Mandela's comrades teach him the meaning of courage?",
     ["He saw them risk and give their lives for an idea again and again.", "From them he learned that courage is not the absence of fear but the triumph over it."])
C.sa("sa3", APART, "Why could a man of colour not fulfil both his obligations under apartheid?",
     ["If he served his people, he was punished and isolated.", "He was torn from his family and home and forced into a life of secrecy and rebellion."])
C.la("la1", FREE, "Trace Mandela's journey from a boy who felt 'born free' to a leader who fought for the freedom of all.",
     ["As a boy he enjoyed simple freedoms: running, swimming, roasting mealies, riding bulls.",
      "As a student he wanted to stay out at night and read what he pleased; as a young man he wanted to earn a living and raise a family.",
      "He then realised that his people were not free: 'the chains on any one of my people were the chains on all of them.'",
      "His hunger for freedom made him bold, a 'criminal' in the eyes of the law and a man without a home; he spent years in prison.",
      "Finally he understood that the oppressor too must be freed from hatred; in 1994 he became President to build freedom for all."])
C.la("la2", COURAGE + APART, "Mandela believes that love comes more naturally to the human heart than hate. Do you agree? Give reasons from the chapter and from life.",
     ["Mandela says no one is born hating; people learn to hate, so they can be taught to love.", "Even in prison, a glimpse of humanity in the guards gave him hope; goodness can be hidden but not extinguished.",
      "After 27 years in prison he chose forgiveness, not revenge: the new nation sang both anthems.",
      "In life, children of different backgrounds play together until they are taught prejudice.", "So love is natural; hatred is learnt and can be unlearnt."])
C.la("la3", DAY, "Imagine you attended Mandela's inauguration on 10 May 1994. Write a diary entry describing the day.",
     ["Date, place (Union Buildings, Pretoria) and the bright, clear autumn morning.", "The oath: de Klerk, Thabo Mbeki and then Mandela; leaders from 140+ countries.",
      "The jets in perfect formation, the generals' salute, and the two anthems sung by both communities.", "Your feelings: joy, hope and the sense of history after the end of apartheid."])

chapter = header("ch02", 2, "Nelson Mandela: Long Walk to Freedom", "Nelson Mandela", "prose",
                 ["inauguration_day", "apartheid_and_its_legacy", "courage_and_character", "meaning_of_freedom", "vocabulary_and_style"],
                 "CBSE 2025-26 English Language and Literature (184): First Flight prose, Chapter 2. Assessed through extracts (5 marks), short answers in 40-50 words (3 marks) and long answers in 100-120 words (6 marks).")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
