"""CBSE Class 10 English, First Flight Poem 1: Dust of Snow (Robert Frost, 1923; public domain)."""
import sys
from lit_common import make, header, path, ex

ROOT = sys.argv[1]
PATH = path("p01_dust_of_snow")
C = make("ff10p01")
blk = C.blk
MEAN, SYMB, DEV = ["meaning_of_the_poem"], ["symbols_crow_and_hemlock"], ["poetic_devices"]

POEM = ("*The way a crow*\n*Shook down on me*\n*The dust of snow*\n*From a hemlock tree*\n\n"
        "*Has given my heart*\n*A change of mood*\n*And saved some part*\n*Of a day I had rued.*")

sections = [
 {"id": "s1", "title": "A small moment, a big change", "blocks": [
  blk("s1.hook", "hook", title="When a tiny thing lifts your mood",
    body="Have you ever been in a bad mood when something small, a joke, a song, a cool breeze, suddenly cheered you up?\n\n"
         "In just eight lines, **Robert Frost** describes such a moment: a crow shakes snow from a tree onto him, and a day he regretted is partly saved."),
  blk("s1.inspiration", "inspiration", title="The poet", person="Robert Frost", years="1874–1963",
    body="**Robert Frost** was an American poet who won the **Pulitzer Prize four times**. He wrote about the countryside of New England using simple words and everyday scenes that carry deep meaning. Dust of Snow appeared in his collection **New Hampshire (1923)**.",
    future="Learning to notice small moments is the first step in writing poetry, and in looking after our own mental health."),
  C.socratic("s1.socratic", "Crows and hemlock trees are usually linked with gloom. Why does Frost use them for a happy moment?",
    ["To show that even things linked with sorrow can bring joy", "Because he could not see any other bird", "To make the poem sad"], 0,
    "Joy can come from unexpected places."),
 ]},
 {"id": "s2", "title": "The poem and its meaning", "blocks": [
  blk("s2.poem", "theory", title="Dust of Snow", body=POEM),
  blk("s2.thm", "theory", title="What the poem says", revision=True,
    body="**Stanza 1:** the poet is standing under a **hemlock tree**. A **crow** sitting on it moves and shakes down fine snow, the 'dust of snow', onto him.\n\n"
         "**Stanza 2:** this small, unexpected touch of nature **changes his mood**. He had been sad and had **rued** (regretted) the day, but now **some part** of the day is saved.\n\n"
         "**The whole poem is one sentence:** the event and its effect flow together, just as the mood changes in a moment.\n\n"
         "**Message:** small moments in nature can heal us; even things we think of as gloomy can bring joy."),
  blk("s2.table", "markdown_table", title="Poetic devices", revision=True,
    body="| Device | Example | Effect |\n|---|---|---|\n| **Symbolism** | crow, hemlock tree | usually symbols of gloom and death; here they bring cheer |\n"
         "| **Metaphor** | 'dust of snow' | fine snowflakes compared to dust |\n| **Alliteration** | '**h**as given my **h**eart'; '**s**aved **s**ome' | music in the lines |\n"
         "| **Enjambment** | lines run on without a pause | the poem reads as one breath, one moment |\n| **Rhyme scheme** | abab cdcd | crow/snow, me/tree; heart/part, mood/rued |"),
  C.kc("s2.check", "What does 'rued' mean?",
    [("regretted", ""), ("enjoyed", "It means the opposite."), ("forgot", "It means regretted."), ("planned", "It means regretted.")],
    "He had regretted the day until the snow fell on him.")
  ,C.kc("s2.check2", "What is the rhyme scheme of each stanza?",
    [("abab", ""), ("aabb", "Lines 1 and 3 rhyme, 2 and 4 rhyme."), ("abcd", "There is rhyme."), ("aaaa", "Only alternate lines rhyme.")],
    "crow/snow and me/tree.")
 ]},
 {"id": "s3", "title": "Symbols and theme", "blocks": [
  blk("s3.thm", "theory", title="Crow, hemlock and snow", revision=True,
    body="**The crow** is often seen as a bird of ill omen, linked with sorrow or death, unlike nightingales or skylarks in poems.\n\n"
         "**The hemlock tree** is poisonous (the Greek thinker Socrates died by drinking hemlock), so it too suggests sadness or death.\n\n"
         "**The dust of snow** stands for a small, fresh, cheerful touch of nature, a **moment of hope**.\n\n"
         "**Theme:** nature has the power to heal. Frost shows that joy can come from unexpected sources, and that one small moment can change the rest of the day."),
  C.kc("s3.check", "What do the crow and the hemlock usually represent?",
    [("sorrow and gloom", ""), ("joy and peace", "They usually suggest gloom."), ("wealth", "Gloom."), ("love", "Gloom.")],
    "Here they become a source of joy.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **8 lines, 2 stanzas, 1 sentence.**\n- **Crow + hemlock (gloom) → snow (cheer) → mood changed, part of day saved.**\n- **Rhyme: abab cdcd.**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying the whole day was saved: only **'some part'** of it.\n2. Calling the hemlock a beautiful tree: it is **poisonous**, chosen deliberately.\n3. Thinking the poet is happy from the start: he had **rued** the day."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Ask students to write two lines about a small thing that changed their mood, using an unexpected source of joy, as Frost does."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Have you had a day that changed because of a tiny moment? What was it?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Fire and Ice:** another short Frost poem with deep meaning.\n- **The Trees, Fog:** more poems where nature has a life of its own."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="How does Frost show that nature can heal a sad heart? Answer in about 120 words.\n\n"
         "**Model answer:** In Dust of Snow, the poet is in a dull, regretful mood. As he stands under a hemlock tree, a crow shakes fine snow onto him. This tiny, unplanned touch of nature lifts his spirits and saves the rest of a day he had rued. Frost deliberately uses a crow and a hemlock, which are usually linked with gloom and death, to show that even such things can bring joy. The poem, written as one sentence of eight lines, moves as quickly as the change of mood. Its message is that nature can heal us in small ways, and that we should stay open to such moments, because one of them can change how we feel."),
  blk("s5.summary", "summary", title="Summary",
    body="- A crow shakes snow from a hemlock tree onto the poet.\n- His mood changes and part of a day he regretted is saved.\n- Symbols of gloom (crow, hemlock) bring joy: nature heals in small ways."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- Always explain the irony of the crow and hemlock.\n- Quote 'some part of a day I had rued' to show the change is partial but real.\n- Name devices with examples: metaphor, alliteration, rhyme abab."),
  blk("s5.flash1", "flashcard", front="What is 'dust of snow'?", back="Fine particles of snow, like dust, shaken down from a tree."),
  blk("s5.flash2", "flashcard", front="What does the crow's action do for the poet?", back="It changes his mood and saves part of a day he had regretted."),
 ]},
]

C.sa("ex1", MEAN, "What is a 'dust of snow'? What does the poet say has changed his mood? How has the poet's mood changed?",
     ["'Dust of snow' means fine particles of snow.", "The snow shaken down on him by a crow changed his mood from regret and sadness to cheerfulness."], ex(1, "Thinking about the Poem"))
C.sa("ex2", SYMB, "How does Frost present nature in this poem? What images come to mind when you think of a crow?",
     ["He shows nature as healing: a small natural event lifts his mood.", "A crow usually suggests a black, harsh, ill-omened bird, linked with gloom."], ex(2, "Thinking about the Poem"))
C.sa("ex3", SYMB, "What is 'a hemlock tree'? Why doesn't the poet write about a more 'beautiful' tree such as a maple, an oak or a pine?",
     ["A hemlock is a poisonous tree, linked with death.", "He chooses it to show that even something associated with sorrow can bring joy."], ex(3, "Thinking about the Poem"))
C.sa("ex4", SYMB, "What do the 'crow' and 'hemlock' represent, joy or sorrow? What does the dust of snow stand for?",
     ["They usually represent sorrow and gloom.", "The dust of snow stands for a small, cheerful moment of hope that lifts the poet's spirits."], ex(4, "Thinking about the Poem"))
C.sa("ex5", MEAN, "Have there been times when you felt depressed or hopeless? Have you experienced a moment that changed your mood that day?",
     ["Yes, for example after doing badly in a test.", "A friend's joke or a sudden rain shower cheered me up and changed the rest of the day."], ex(5, "Thinking about the Poem"))

C.extract("ext1", MEAN + SYMB, "The way a crow\nShook down on me\nThe dust of snow\nFrom a hemlock tree",
  [("Who is 'me'?", "The poet, Robert Frost."), ("What did the crow do?", "It shook down snow onto the poet."),
   ("What is 'a hemlock tree'?", "A poisonous tree."), ("What does the crow usually symbolise?", "Gloom or bad luck."),
   ("Give the rhyming words in the extract.", "crow/snow, me/tree.")])
C.extract("ext2", MEAN, "Has given my heart\nA change of mood\nAnd saved some part\nOf a day I had rued.",
  [("What has given the poet's heart a change of mood?", "The dust of snow shaken down by the crow."),
   ("What was his mood before?", "Sad and regretful."), ("What does 'rued' mean?", "Regretted."),
   ("Was the whole day saved?", "No, only some part of it."), ("Name the device in 'has given my heart'.", "Alliteration (h sound).")])

C.m("mcq01", MEAN, "Who wrote 'Dust of Snow'?", [("Robert Frost", ""), ("Carl Sandburg", "He wrote Fog."), ("W. B. Yeats", "He wrote For Anne Gregory."), ("Leslie Norris", "He wrote A Tiger in the Zoo.")], "Frost also wrote Fire and Ice.")
C.m("mcq02", MEAN, "The poem has:", [("two stanzas of four lines", ""), ("one long stanza", "Two quatrains."), ("three stanzas", "Two."), ("fourteen lines", "Eight lines.")], "It is one sentence.")
C.m("mcq03", SYMB, "Why is the hemlock significant?", [("it is a poisonous tree linked with death", ""), ("it is a fruit tree", "It is poisonous."), ("it is the poet's favourite", "It suggests gloom."), ("it flowers in winter", "It is poisonous.")], "Its use is deliberate.")
C.m("mcq04", MEAN, "The poet's mood changes from:", [("sad to cheerful", ""), ("happy to sad", "The opposite."), ("angry to sad", "Sad to cheerful."), ("calm to angry", "Sad to cheerful.")], "The snow lifted his spirits.")
C.m("mcq05", DEV, "'Dust of snow' is an example of:", [("metaphor", ""), ("simile", "No 'like' or 'as'."), ("personification", "It compares snow to dust."), ("onomatopoeia", "It compares snow to dust.")], "Snowflakes are compared to dust.")
C.m("mcq06", DEV, "The rhyme scheme of the poem is:", [("abab cdcd", ""), ("aabb ccdd", "Alternate lines rhyme."), ("abcd abcd", "There is rhyme."), ("abba cddc", "Alternate lines rhyme.")], "crow/snow, me/tree; heart/part, mood/rued.")
C.m("mcq07", MEAN, "The central message of the poem is that:", [("small moments in nature can change our mood", ""), ("crows are harmful", "The crow brings cheer."), ("winter is sad", "Nature heals."), ("we should avoid trees", "Nature heals.")], "Joy can come from unexpected sources.")
C.m("mcq08", DEV, "How many sentences make up the poem?", [("one", ""), ("two", "One."), ("four", "One."), ("eight", "One.")], "The lines run on to the end.")
C.tf("tf1", MEAN, "The poet says the whole day was saved.", False, "Only some part of the day was saved.")
C.tf("tf2", SYMB, "Frost chose the crow and hemlock because they are usually linked with joy.", False, "They are usually linked with gloom; he uses them to show unexpected joy.")
C.la("la1", SYMB + MEAN, "Explain how Frost uses ordinary symbols in an unusual way in 'Dust of Snow'.",
     ["The crow is usually a bird of ill omen and the hemlock a poisonous tree linked with death.", "In the poem, the crow shakes snow from the hemlock onto the poet.",
      "This unlikely pair brings him joy and changes his mood.", "Frost thus shows that happiness can come from unexpected, even gloomy, sources.",
      "The message: stay open to small moments in nature; they can heal us."])

chapter = header("poem01", 10, "Dust of Snow", "Robert Frost", "poem", ["meaning_of_the_poem", "symbols_crow_and_hemlock", "poetic_devices"],
                 "CBSE 2025-26 English Language and Literature (184): First Flight poem 1. Assessed through poetry extracts (5 marks) and short answers (3 marks); can appear in long answers.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
