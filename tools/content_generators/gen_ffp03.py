"""CBSE Class 10 English, First Flight Poem 3: A Tiger in the Zoo (Leslie Norris). Quotes are short extracts only."""
import sys
from lit_common import make, header, path, ex, closing

ROOT = sys.argv[1]
PATH = path("p03_a_tiger_in_the_zoo")
C = make("ff10p03")
blk = C.blk
CAGE, WILD, DEV = ["tiger_in_the_cage"], ["tiger_in_the_wild"], ["poetic_devices"]
TP = lambda n: ex(n, "Thinking about the Poem")

sections = [
 {"id": "s1", "title": "A wild animal behind bars", "blocks": [
  blk("s1.hook", "hook", title="Pacing, pacing, pacing",
    body="Watch a tiger in a zoo: it walks the same few steps again and again. In **A Tiger in the Zoo**, **Leslie Norris** contrasts this caged tiger with the free tiger it should be, hunting in the forest, and shows its silent anger."),
  blk("s1.inspiration", "inspiration", title="The poet", person="Leslie Norris", years="1921–2006",
    body="**Leslie Norris** was a Welsh poet and short-story writer who loved nature and wrote often about animals and the countryside.",
    future="Wildlife conservation, zoo design and animal welfare all ask the question this poem raises: where do wild animals belong?"),
  C.socratic("s1.socratic", "The tiger 'ignores visitors'. Why might it do that?",
    ["It is angry and unhappy at being caged; the visitors mean nothing to it", "It cannot see them", "It is asleep"], 0,
    "Its 'quiet rage' shows its feelings."),
 ]},
 {"id": "s2", "title": "The poem stanza by stanza", "blocks": [
  blk("s2.thm", "theory", title="What the poem says", revision=True,
    body="**Stanza 1, in the cage:** the tiger stalks in his **vivid stripes** the **few steps of his cage**, on **'pads of velvet quiet'**, in his **'quiet rage'**.\n\n"
         "**Stanza 2, where he should be:** he should be **lurking in shadow**, sliding through **long grass** near the **water hole** where plump **deer** pass.\n\n"
         "**Stanza 3, in the wild:** he should be **snarling** around houses at the **jungle's edge**, baring his white fangs and claws, **terrorising the village**.\n\n"
         "**Stanza 4, back in the cage:** but he is **locked in a concrete cell**, his strength **behind bars**, stalking the length of his cage and **ignoring visitors**.\n\n"
         "**Stanza 5, at night:** he hears the last voice at night, the **patrolling cars**, and stares with his **brilliant eyes** at the **brilliant stars**: longing for freedom.\n\n"
         "**Theme:** wild animals lose their dignity and freedom in captivity; they belong in their natural habitat."),
  blk("s2.table", "markdown_table", title="Cage versus wild", revision=True,
    body="| In the cage | In the wild |\n|---|---|\n| stalks a few steps | slides through long grass |\n| in a concrete cell, behind bars | lurking in shadow near the water hole |\n"
         "| ignores visitors | terrorises the village at the jungle's edge |\n| hears patrolling cars at night | hunts plump deer |\n| quiet rage, helpless | free, powerful, feared |"),
  C.kc("s2.check", "Where should the tiger be, according to the poet?",
    [("in the jungle, lurking near a water hole", ""), ("in a bigger cage", "In the wild."), ("in a circus", "In the wild."), ("in a museum", "In the wild.")],
    "He should be free to hunt deer.")
  ,C.kc("s2.check2", "What does the tiger stare at during the night?",
    [("the brilliant stars", ""), ("the visitors", "He ignores visitors."), ("the patrolling cars", "He hears them, but stares at the stars."), ("the moon", "The stars.")],
    "He longs for freedom.")
 ]},
 {"id": "s3", "title": "Poetic devices", "blocks": [
  blk("s3.thm", "theory", title="How the poet creates the picture", revision=True,
    body="| Device | Example | Effect |\n|---|---|---|\n| **Alliteration** | 'He **s**talks in his vivid **s**tripes'; 'He **s**hould be lurking in **s**hadow, / **S**liding through long grass' | the soft 's' sounds echo his silent movement |\n"
         "| **Oxymoron / contrast** | 'quiet rage' | silent but deep anger |\n| **Repetition** | 'quiet... quiet'; 'brilliant... brilliant' | links the tiger's eyes with the free stars |\n"
         "| **Imagery** | 'vivid stripes', 'pads of velvet' | we see and feel the tiger |\n| **Personification** | the tiger 'ignores visitors' | gives him human feelings |\n"
         "| **Contrast** | stanzas 1, 4, 5 (cage) vs 2, 3 (wild) | shows what captivity takes away |\n| **Rhyme scheme** | abcb | lines 2 and 4 of each stanza rhyme |"),
  C.kc("s3.check", "'Quiet rage' is an example of:",
    [("oxymoron (contradictory words together)", ""), ("simile", "No 'like' or 'as'."), ("onomatopoeia", "Contradiction."), ("rhyme", "Contradiction.")],
    "Rage is usually loud; his is silent.")
 ]},
 closing(C,
   "- **5 stanzas: cage, wild, wild, cage, night.**\n- **Key phrases: vivid stripes; pads of velvet quiet; quiet rage; concrete cell; brilliant eyes/brilliant stars.**\n- **Rhyme: abcb.**",
   "1. Saying the tiger is happy: he is in **quiet rage**.\n2. Mixing which stanzas describe the wild (2 and 3).\n3. Calling 'quiet rage' a simile: it is an **oxymoron**.",
   "Draw two columns 'Cage' and 'Wild'; students fill them from the poem, then write a 3-line poem from the tiger's point of view.",
   "Should zoos exist? What could make them better for animals like this tiger?",
   "- **Mijbil the Otter:** a wild animal taken from its home.\n- **Geography (Forest and Wildlife):** Project Tiger (1973) protects tigers in reserves.",
   "Compare the tiger in the zoo with the tiger in the wild. Answer in about 120 words.",
   "In the zoo, the tiger stalks the few steps of his cage in 'quiet rage'. He is locked in a concrete cell, his great strength wasted behind bars. He ignores the visitors, and at night, hearing only patrolling cars, he stares at the brilliant stars, longing for freedom. In the wild, he would be lurking in the shadows, sliding through long grass near a water hole to hunt plump deer, or snarling at the jungle's edge, baring his fangs and terrorising the villagers. There he is powerful, free and feared; here he is helpless and humiliated. The contrast shows that wild animals belong in their natural homes, not in cages.",
   "- The caged tiger paces in silent anger.\n- In the wild he would hunt and be feared.\n- Locked in a cell, he ignores visitors and gazes at the stars at night, longing for freedom.\n- Theme: captivity robs wild animals of freedom and dignity.",
   "- Always use the cage/wild contrast.\n- Explain 'quiet rage' and 'brilliant eyes / brilliant stars'.\n- Value-based answers: zoos versus wildlife sanctuaries and Project Tiger.",
   [("What does 'quiet rage' show?", "The tiger's silent but deep anger at being caged."),
    ("Where should the tiger be?", "In the jungle: lurking in shadow near the water hole, hunting deer.")]),
]

C.sa("ex1", CAGE + WILD, "Read the poem again, and work in pairs or groups to contrast the tiger in the zoo with the tiger in the wild.",
     ["In the zoo: he stalks a few steps in a concrete cell, ignores visitors and stares at the stars at night.", "In the wild: he lurks in shadow near a water hole, hunts deer and terrorises villages at the jungle's edge."], TP(1))
C.sa("ex2", DEV, "Notice the use of a word repeated in lines such as 'On pads of velvet quiet, / In his quiet rage.' What do you think is the effect of this repetition?",
     ["Repeating 'quiet' stresses that his movement is soft and silent.", "It also shows that his anger is held in silently, which makes it more powerful and sad."], TP(2))
C.sa("ex3", DEV, "Notice the lines in the poem where the poet uses repetition: 'brilliant eyes' and 'brilliant stars'. What is the effect?",
     ["The tiger's shining eyes are linked with the shining, free stars.", "It shows his longing for the freedom of the open sky."], TP(3))
C.sa("ex4", CAGE, "Why does the tiger ignore the visitors?",
     ["He is angry and helpless at being caged.", "The visitors mean nothing to him; his mind is on the freedom he has lost."])

C.extract("ext1", CAGE, "He stalks in his vivid stripes\nThe few steps of his cage,\nOn pads of velvet quiet,\nIn his quiet rage.",
  [("Who is 'he'?", "The tiger in the zoo."), ("What does 'stalks' mean here?", "Walks stiffly, angrily, to and fro."),
   ("What are 'pads of velvet'?", "The soft paws of the tiger."), ("Name the device in 'quiet rage'.", "Oxymoron."), ("Find the rhyming words.", "cage/rage.")])
C.extract("ext2", CAGE, "He should be lurking in shadow,\nSliding through long grass\nNear the water hole\nWhere plump deer pass.",
  [("Where should the tiger be?", "In the forest, near the water hole."), ("Why would he wait near the water hole?", "To hunt the deer that come to drink."),
   ("Find a word meaning 'waiting in hiding'.", "Lurking."), ("Find an example of alliteration.", "'Sliding... long grass' / 'should... shadow'."), ("What mood does this stanza show?", "The freedom and power of the wild.")])
C.extract("ext3", CAGE, "And stares with his brilliant eyes\nAt the brilliant stars.",
  [("When does the tiger stare at the stars?", "At night."), ("What does he hear before this?", "The patrolling cars."),
   ("Name the device in 'brilliant eyes / brilliant stars'.", "Repetition."), ("What does his staring suggest?", "Longing for freedom."),
   ("What does 'brilliant' mean?", "Shining brightly.")])

C.m("mcq01", CAGE, "A Tiger in the Zoo was written by:", [("Leslie Norris", ""), ("Robert Frost", "Leslie Norris."), ("Carolyn Wells", "Leslie Norris."), ("Ogden Nash", "Leslie Norris.")], "A Welsh poet.")
C.m("mcq02", CAGE, "The tiger's cage is made of:", [("concrete", ""), ("wood", "A concrete cell."), ("glass", "Concrete."), ("mud", "Concrete.")], "'Locked in a concrete cell.'")
C.m("mcq03", WILD, "In the wild, the tiger would terrorise:", [("the village at the jungle's edge", ""), ("the zoo keepers", "The village."), ("the city", "The village."), ("other tigers", "The village.")], "Baring his white fangs and claws.")
C.m("mcq04", CAGE, "What does the tiger hear at night?", [("patrolling cars", ""), ("deer", "Patrolling cars."), ("visitors", "Patrolling cars."), ("rain", "Patrolling cars.")], "The last voice of the night.")
C.m("mcq05", DEV, "The rhyme scheme of each stanza is:", [("abcb", ""), ("aabb", "abcb."), ("abab", "abcb."), ("none", "abcb.")], "Only lines 2 and 4 rhyme.")
C.m("mcq06", CAGE, "The poem's theme is:", [("wild animals suffer in captivity", ""), ("zoos are fun", "The opposite."), ("tigers are dangerous", "The theme is captivity."), ("deer are plump", "The theme is captivity.")], "They belong in the wild.")
C.m("mcq07", DEV, "Which stanzas describe the tiger in the wild?", [("the second and third", ""), ("the first and fourth", "Those are the cage."), ("the fifth", "That is night in the cage."), ("all", "Only 2 and 3.")], "The contrast is the structure of the poem.")
C.m("mcq08", DEV, "'Vivid stripes' appeals to our sense of:", [("sight", ""), ("hearing", "Sight."), ("smell", "Sight."), ("taste", "Sight.")], "It is visual imagery.")
C.tf("tf1", CAGE, "The tiger enjoys looking at the visitors.", False, "He ignores visitors.")
C.tf("tf2", WILD, "In the wild, the tiger would hunt plump deer near the water hole.", True, "Stanza 2.")
C.la("la1", CAGE, "Do you think animals should be kept in zoos? Answer with reference to 'A Tiger in the Zoo'.",
     ["The poem shows a tiger pacing a concrete cell in quiet rage.", "In the wild he would hunt, roam and be feared; in the zoo his strength is wasted.",
      "He ignores visitors and longs for the stars: freedom.", "Zoos may educate people and protect endangered species, but they should give space and natural habitat.",
      "Better still, sanctuaries and national parks let animals live freely."])

chapter = header("poem03", 12, "A Tiger in the Zoo", "Leslie Norris", "poem", ["tiger_in_the_cage", "tiger_in_the_wild", "poetic_devices"],
                 "CBSE 2025-26 English Language and Literature (184): First Flight poem 3. Assessed through poetry extracts (5 marks) and short answers (3 marks). Only short lines are quoted here; read the full poem in the NCERT textbook.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
