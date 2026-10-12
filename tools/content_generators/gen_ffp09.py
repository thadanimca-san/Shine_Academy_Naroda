"""CBSE Class 10 English, First Flight Poem 9: The Tale of Custard the Dragon (Ogden Nash). Short quotes only."""
import sys
from lit_common import make, header, path, ex, closing

ROOT = sys.argv[1]
PATH = path("p09_the_tale_of_custard_the_dragon")
C = make("ff10p09")
blk = C.blk
CHARS, STORY, DEV = ["characters"], ["story_and_irony"], ["poetic_devices"]
TP = lambda n: ex(n, "Thinking about the Poem")

TAB = ("| Character | Who | Before the pirate | During the pirate's attack |\n|---|---|---|---|\n"
       "| **Belinda** | a little girl | 'as brave as a barrel full of bears' | turned pale and cried 'Help! Help!' |\n"
       "| **Ink** | a little black kitten | brave, chased lions down the stairs | 'trickled down to the bottom of the household' |\n"
       "| **Blink** | a little grey mouse | brave, chased lions down the stairs | 'strategically mouseholed' |\n"
       "| **Mustard** | a little yellow dog | 'as brave as a tiger in a rage' | fled with a terrified yelp |\n"
       "| **Custard** | a little pet dragon | cowardly; cried for 'a nice safe cage' | jumped on the pirate and gobbled him up |")

sections = [
 {"id": "s1", "title": "Who is really brave?", "blocks": [
  blk("s1.hook", "hook", title="The cowardly dragon",
    body="Everyone in Belinda's little white house boasts of being brave, and everyone laughs at Custard, the dragon who keeps crying for a nice safe cage. Then a **pirate** climbs in through the window..."),
  blk("s1.inspiration", "inspiration", title="The poet", person="Ogden Nash", years="1902–1971",
    body="**Ogden Nash** was an American poet famous for funny verse with surprising rhymes and made-up words. The Tale of Custard the Dragon is a comic **ballad** that tells a story with a moral twist.",
    future="Humour writers, cartoonists and children's authors use rhythm, rhyme and surprise exactly as Nash does."),
  C.socratic("s1.socratic", "Why does everyone laugh at Custard at the start?",
    ["He seems cowardly, always asking for a safe cage", "He is very small", "He cannot breathe fire"], 0,
    "But he turns out to be the bravest of all."),
 ]},
 {"id": "s2", "title": "The story", "blocks": [
  blk("s2.thm", "theory", title="What happens in the poem", revision=True,
    body="**The household:** **Belinda** lives in a little white house with a little black kitten (**Ink**), a little grey mouse (**Blink**), a little yellow dog (**Mustard**) and a little pet dragon (**Custard**).\n\n"
         "**Custard:** he has big sharp **teeth**, **spikes** on top and **scales** underneath, a mouth like a **fireplace**, a nose like a **chimney** and toes like **daggers**, but he is a coward: he **cries for a nice safe cage**. Belinda, Ink, Blink and Mustard boast of their bravery and **laugh** at him; Belinda even **tickles him unmercifully**.\n\n"
         "**The pirate:** one day a **pirate** climbs in through the window, a pistol in his left hand, a pistol in his right, and a cutlass in his teeth. **Belinda** turns pale and cries for help; **Mustard** flees with a terrified yelp; **Ink** trickles down to the bottom of the household; **Blink** strategically mouseholes.\n\n"
         "**Custard's bravery:** Custard jumps up, snorting like an engine, clashing his tail like irons in a dungeon, and goes at the pirate **like a robin at a worm**. The pirate fires two bullets but misses, and Custard **gobbles him up**.\n\n"
         "**The ending:** Belinda embraces Custard and the others praise him, but soon they claim that **they would have been twice as brave** if they had not been flustered, and Custard again cries for **a nice safe cage**."),
  blk("s2.table", "markdown_table", title="The characters", revision=True, body=TAB),
  C.kc("s2.check", "What did Custard do when the pirate came?",
    [("he jumped on the pirate and gobbled him up", ""), ("he ran to his cage", "He fought bravely."), ("he cried for help", "Belinda cried for help."), ("he hid in a mousehole", "Blink did that.")],
    "He went at the pirate like a robin at a worm.")
  ,C.kc("s2.check2", "Why did Custard cry for a nice safe cage?",
    [("he seemed timid and wanted to feel safe", ""), ("he was hungry", "He wanted safety."), ("he wanted to sleep", "He wanted safety."), ("the pirate asked him", "He wanted safety.")],
    "This is why the others called him cowardly.")
 ]},
 {"id": "s3", "title": "Humour and devices", "blocks": [
  blk("s3.thm", "theory", title="How Nash makes it funny", revision=True,
    body="| Device | Example |\n|---|---|\n| **Simile** | brave as a barrel full of bears; brave as a tiger in a rage; mouth like a fireplace; nose like a chimney; toes like daggers; went at the pirate like a robin at a worm |\n"
         "| **Coined words** | 'realio, trulio' (really, truly), 'mouseholed' (hid in a mousehole) |\n| **Alliteration** | '**b**rave as a **b**arrel full of **b**ears'; 'little **b**lack kitten' |\n"
         "| **Onomatopoeia** | 'clatter', 'yelp' |\n| **Repetition** | 'little' before every character; 'a nice safe cage' |\n| **Rhyme scheme** | aabb (couplets) | \n| **Irony** | the 'coward' is the only one who is brave; the 'brave' ones run |\n\n"
         "**Theme:** true bravery is shown in action, not in boasting. People who look timid may be the bravest when it matters."),
  C.kc("s3.check", "'Realio, trulio' is an example of:",
    [("coined (made-up) words for humour", ""), ("a simile", "Made-up words."), ("a foreign language", "Made-up words."), ("a spelling mistake", "Deliberate.")],
    "They mean 'really, truly'.")
 ]},
 closing(C,
   "- **Pets: Ink (kitten, black), Blink (mouse, grey), Mustard (dog, yellow), Custard (dragon).**\n- **Pirate: two pistols + cutlass in teeth.**\n- **Irony: braggarts run, coward fights.**",
   "1. Mixing up Ink and Blink: Ink is the **kitten**, Blink the **mouse**.\n2. Saying Belinda fought the pirate: she **cried for help**.\n3. Thinking Custard changes his nature: after the fight he again cries for a **safe cage**.",
   "Act out the pirate scene with five students; others call out each simile as it appears.",
   "Have you met someone quiet who turned out to be very brave? What happened?",
   "- **How to Tell Wild Animals:** another comic poem.\n- **The Proposal:** comedy that mocks boasting and pride.",
   "Who is the real hero of the poem, and why? Answer in about 120 words.",
   "The real hero is Custard, the dragon everyone calls cowardly. Belinda, Ink, Blink and Mustard boast of their courage and laugh at Custard for crying for a nice safe cage. But when a pirate climbs in with two pistols and a cutlass, Belinda turns pale and cries for help, Mustard runs off yelping, Ink trickles away and Blink hides in a mousehole. Only Custard springs forward, snorting like an engine, and gobbles up the pirate. Afterwards the others claim they would have been twice as brave if they had not been flustered, while Custard modestly asks again for his cage. The poem's irony teaches that true bravery is shown in action, not in boasting.",
   "- Belinda and her pets boast of bravery and mock the dragon Custard.\n- A pirate attacks; all flee except Custard, who eats the pirate.\n- They still boast; Custard cries for a safe cage again.\n- Theme: actions, not words, show courage.",
   "- List the characters with their pet names.\n- Quote two similes.\n- Explain the irony of the ending.",
   [("Who are Ink, Blink and Mustard?", "A little black kitten, a little grey mouse and a little yellow dog."),
    ("What is ironic about the poem?", "The 'cowardly' dragon is the only one who fights; the boasters run away.")]),
]

C.sa("ex1", CHARS, "Who are the characters in this poem? List them with their pet names.",
     ["Belinda, a little girl; Ink, a little black kitten; Blink, a little grey mouse.", "Mustard, a little yellow dog; Custard, a little pet dragon; and the pirate."], TP(1))
C.sa("ex2", CHARS, "Why did Custard cry for a nice safe cage? Why is the dragon called 'cowardly dragon'?",
     ["He seemed timid and wanted to feel safe.", "Because of this the others thought he was a coward and laughed at him."], TP(2))
C.sa("ex3", CHARS, "'Belinda tickled him, she tickled him unmerciful...' Why?",
     ["She thought Custard was a coward.", "She teased him and made fun of him for crying for a safe cage."], TP(3))
C.sa("ex4", STORY, "The poet has employed many poetic devices. Find examples of simile and coined words.",
     ["Similes: brave as a barrel full of bears; mouth like a fireplace; went at the pirate like a robin at a worm.", "Coined words: 'realio, trulio' and 'mouseholed'."], TP(4))
C.sa("ex5", STORY, "How is Custard's bravery different from the bravery of the others?",
     ["The others only boast and run when danger comes.", "Custard is quiet and modest but fights the pirate when it really matters."])

C.extract("ext1", CHARS, "Belinda lived in a little white house,\nWith a little black kitten and a little grey mouse,\nAnd a little yellow dog and a little pet dragon.",
  [("Name the poem.", "The Tale of Custard the Dragon."), ("What is the name of the kitten?", "Ink."), ("What is the name of the dragon?", "Custard."),
   ("Which word is repeated?", "'little'."), ("What is the rhyme scheme?", "aabb (couplets).")])
C.extract("ext2", STORY, "Custard jumped up, snorting like an engine,\nClashed his tail like irons in a dungeon,",
  [("Whom did Custard attack?", "The pirate."), ("Name the figure of speech in 'snorting like an engine'.", "Simile."),
   ("What does the extract show about Custard?", "He was brave in real danger."), ("What did the others do at this time?", "They ran away or hid."), ("What happened to the pirate?", "Custard gobbled him up.")])

C.m("mcq01", CHARS, "Who is Mustard?", [("a little yellow dog", ""), ("a little black kitten", "That is Ink."), ("a little grey mouse", "That is Blink."), ("the dragon", "That is Custard.")], "Brave as a tiger in a rage, he said.")
C.m("mcq02", CHARS, "Belinda was as brave as:", [("a barrel full of bears", ""), ("a tiger in a rage", "That is Mustard."), ("a robin at a worm", "That is Custard attacking."), ("an engine", "That is Custard snorting.")], "A boast she cannot live up to.")
C.m("mcq03", STORY, "What did the pirate carry?", [("a pistol in each hand and a cutlass in his teeth", ""), ("a sword only", "Two pistols and a cutlass."), ("a gun and a flag", "Two pistols and a cutlass."), ("a bag of gold", "Two pistols and a cutlass.")], "He climbed in through the window.")
C.m("mcq04", STORY, "What did Blink do when the pirate came?", [("strategically mouseholed", ""), ("fought him", "That was Custard."), ("cried for help", "That was Belinda."), ("fled with a yelp", "That was Mustard.")], "He hid in a mousehole.")
C.m("mcq05", DEV, "'Mouseholed' is a:", [("coined word", ""), ("simile", "A coined word."), ("rhyme", "A coined word."), ("misprint", "A coined word.")], "Nash invents words for fun.")
C.m("mcq06", DEV, "The rhyme scheme of the poem is:", [("aabb", ""), ("abab", "aabb."), ("abcb", "aabb."), ("free verse", "It rhymes in couplets.")], "Each pair of lines rhymes.")
C.m("mcq07", STORY, "After the fight, the others said:", [("they would have been twice as brave if not flustered", ""), ("Custard was a coward", "They praised him, then boasted."), ("they would leave the house", "They boasted."), ("nothing", "They boasted.")], "Boasting again.")
C.m("mcq08", STORY, "The central irony of the poem is that:", [("the 'cowardly' dragon is the bravest", ""), ("the pirate wins", "Custard wins."), ("Belinda is a dragon", "The coward is brave."), ("the house is black", "The coward is brave.")], "Actions, not words, show courage.")
C.tf("tf1", STORY, "Belinda fought the pirate bravely.", False, "She turned pale and cried 'Help! Help!'")
C.tf("tf2", CHARS, "Ink is a little black kitten.", True, "Blink is the mouse; Mustard the dog.")
C.la("la1", STORY, "'Actions speak louder than words.' Explain with reference to the poem.",
     ["Belinda, Ink, Blink and Mustard boast of being brave and laugh at Custard.", "When the pirate attacks, they all fail: Belinda cries for help, Mustard flees, Ink and Blink hide.",
      "Custard, who only asked for a safe cage, fights and eats the pirate.", "Even afterwards the others boast, while Custard stays modest.", "So his action, not their words, shows true courage."])

chapter = header("poem09", 18, "The Tale of Custard the Dragon", "Ogden Nash", "poem", ["characters", "story_and_irony", "poetic_devices"],
                 "CBSE 2025-26 English Language and Literature (184): First Flight poem 9. Assessed through poetry extracts (5 marks) and short answers (3 marks). Only short lines are quoted here; read the full poem in the NCERT textbook.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
