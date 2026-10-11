"""CBSE Class 10 English, First Flight Poem 7: The Trees (Adrienne Rich). Short quotes only."""
import sys
from lit_common import make, header, path, ex, closing

ROOT = sys.argv[1]
PATH = path("p07_the_trees")
C = make("ff10p07")
blk = C.blk
MOVE, MEAN, DEV = ["trees_moving_out"], ["deeper_meaning"], ["poetic_devices"]
TP = lambda n: ex(n, "Thinking about the Poem")

sections = [
 {"id": "s1", "title": "Trees that walk out", "blocks": [
  blk("s1.hook", "hook", title="A house full of trees",
    body="Imagine potted trees kept inside a house, cramped for years. One night their roots pull free, their branches push against the glass, and they **walk out into the empty forest**. That is the strange, dream-like picture in **The Trees**."),
  blk("s1.inspiration", "inspiration", title="The poet", person="Adrienne Rich", years="1929–2012",
    body="**Adrienne Rich** was an American poet and essayist. Her poems speak about freedom, nature and the place of women in society. The Trees can be read both as a poem about nature reclaiming its place, and as a poem about anyone breaking free from confinement.",
    future="Environmental scientists, urban planners and writers ask the same question: how much space do we leave for nature?"),
  C.socratic("s1.socratic", "Why is the forest 'empty' at the start of the poem?",
    ["Its trees have been taken and kept inside houses by people", "It is winter", "The birds have flown south"], 0,
    "Without trees there is no shade, no birds, no insects."),
 ]},
 {"id": "s2", "title": "The poem stanza by stanza", "blocks": [
  blk("s2.thm", "theory", title="What the poem says", revision=True,
    body="**Stanza 1, an empty forest:** the trees inside the house are moving out into the forest, a forest that was empty all these days, where **no bird could sit, no insect hide, no sun bury its feet in shadow**. By morning, the forest will be full of trees again.\n\n"
         "**Stanza 2, breaking free:** all night the **roots** work to disengage themselves from the **cracks in the veranda floor**; the **leaves** strain toward the glass; small **twigs** are stiff with exertion; long-cramped **boughs** shuffle under the roof **'like newly discharged patients / half-dazed, moving / to the clinic doors'**.\n\n"
         "**Stanza 3, the poet ignores it:** the poet sits inside, doors open to the veranda, writing long letters in which she **scarcely mentions the departure of the forest from the house**. The night is fresh; the **whole moon** shines in a sky still open; the smell of leaves and lichen still reaches like a voice into the rooms. Her head is full of whispers which tomorrow will be silent.\n\n"
         "**Stanza 4, the trees are gone:** she hears the **glass breaking** as the trees **stumble forward** into the night. The winds rush to meet them, and **the moon is broken like a mirror**, its pieces flashing in the crown of the tallest oak."),
  C.kc("s2.check", "Which three things cannot happen in a treeless forest?",
    [("no bird can sit, no insect hide, no sun bury its feet in shadow", ""), ("no rain can fall, no wind blow, no river flow", "The poem names birds, insects and the sun's feet."),
     ("no deer, no tiger, no lion", "Birds, insects and the sun."), ("no house, no road, no car", "Birds, insects and the sun.")],
    "Trees give shelter and shade.")
  ,C.kc("s2.check2", "To what does the poet compare the long-cramped branches?",
    [("newly discharged patients, half-dazed, moving to the clinic doors", ""), ("soldiers marching", "To discharged patients."), ("birds flying", "To discharged patients."), ("children playing", "To discharged patients.")],
    "They are weak and dazed after long confinement.")
 ]},
 {"id": "s3", "title": "Images and meaning", "blocks": [
  blk("s3.thm", "theory", title="Devices and the deeper meaning", revision=True,
    body="| Device | Example | Effect |\n|---|---|---|\n| **Personification** | roots work, leaves strain, trees stumble forward | trees act like living people seeking freedom |\n"
         "| **Simile** | branches 'like newly discharged patients'; moon 'broken like a mirror' | weakness after confinement; a shattered, changed scene |\n"
         "| **Metaphor / image** | 'sun bury its feet in shadow' (the sun's rays are its feet) | sunlight resting in the shade of trees |\n| **Imagery** | smell of leaves and lichen 'like a voice' | nature calling from outside |\n| **Free verse** | no regular rhyme | a dream-like, flowing movement |\n\n"
         "**The moon:** at first the **whole moon shines** in an open sky; at the end it is **broken like a mirror**, its pieces flashing in the crown of the tallest oak, because the trees now stand between the poet and the moon.\n\n"
         "**Why doesn't the poet mention it in her letters?** She is absorbed in her own world and does not care, or does not want to admit, that nature is leaving: an image of human **indifference**.\n\n"
         "**Deeper meaning:** (1) humans have cut and confined nature for their own use; nature will take back its place. (2) The trees can also stand for **women** (or anyone) confined at home, breaking free to find their own identity."),
  C.kc("s3.check", "How does the moon change by the end of the poem?",
    [("from whole to 'broken like a mirror' among the trees' branches", ""), ("from new moon to full moon", "From whole to broken."), ("it disappears behind clouds", "It looks broken through the branches."), ("it turns red", "From whole to broken.")],
    "The trees now stand between the poet and the moon.")
 ]},
 closing(C,
   "- **Stanzas: empty forest → trees struggle out → poet writes letters, ignores it → glass breaks, moon broken.**\n- **Similes: discharged patients; moon like a broken mirror.**",
   "1. Taking the poem only literally: discuss the **deeper meaning** too.\n2. Saying the poet helps the trees: she **scarcely mentions** their departure.\n3. Forgetting 'the sun's feet' are its rays.",
   "Ask students to draw the four stages of the poem as a comic strip, labelling each with one phrase from the poem.",
   "What does nature lose when we cut forests to build homes? What do we lose?",
   "- **Geography (Forest and Wildlife Resources):** deforestation and its effects.\n- **Amanda! and Anne Frank:** the wish to be free.",
   "Explain the deeper meaning of 'The Trees'. Answer in about 120 words.",
   "Literally, the poem shows trees kept inside a house breaking free and moving back into an empty forest. Their roots tear loose from the floor, their leaves push at the glass, and their cramped branches stagger out like patients leaving hospital. On a deeper level, the poem shows how humans have confined nature for decoration and use, leaving forests empty of birds, insects and shade; nature now takes back its place. The poet's indifference, writing letters without mentioning the departure, shows how little we notice what we destroy. The poem can also be read as the story of women, long confined to the home, breaking out to find freedom and identity. Either way, it is a poem about freedom.",
   "- Trees kept indoors move out into the empty forest at night.\n- Roots, leaves, twigs and boughs struggle free like discharged patients.\n- The poet ignores it; the glass breaks and the moon seems broken among the branches.\n- Deeper meaning: nature reclaiming freedom; also women breaking free.",
   "- Give both the literal and the deeper meaning.\n- Quote the two similes.\n- Explain 'the sun bury its feet in shadow'.",
   [("What are the 'sun's feet'?", "Its rays; in a forest they rest in the shade of trees."),
    ("What is the deeper meaning of the poem?", "Nature reclaiming its freedom from human control; also women breaking free from confinement.")]),
]

C.sa("ex1", MOVE, "(a) Find, in the first stanza, three things that cannot happen in a treeless forest. (b) What picture do these words create: '...sun bury its feet in shadow...'? What are the sun's feet?",
     ["(a) No bird can sit, no insect hide, and no sun bury its feet in shadow.", "(b) Sunlight resting in the shade of trees; the sun's feet are its rays."], TP(1))
C.sa("ex2", MOVE, "(a) Where are the trees in the poem? What do their roots, their leaves and their twigs do? (b) What does the poet compare their branches to?",
     ["(a) Inside the house; roots work to free themselves from the veranda floor, leaves strain toward the glass, twigs grow stiff with exertion.", "(b) To newly discharged patients, half-dazed, moving to the clinic doors."], TP(2))
C.sa("ex3", DEV, "(a) How does the poet describe the moon at the beginning and at the end of the third and fourth stanzas? What causes this change? (b) What happens to the house when the trees move out of it?",
     ["(a) At first the whole moon shines in an open sky; later it is broken like a mirror, because the trees' branches now stand between her and the moon.", "(b) The glass breaks and the house is left empty of its trees."], TP(3))
C.sa("ex4", MEAN, "Why do you think the poet does not mention 'the departure of the forest from the house' in her letters?",
     ["She is absorbed in her own life and indifferent to nature.", "It shows how people ignore what happens to nature, or do not want to admit it."], TP(4))
C.sa("ex5", MEAN, "Now that you have read the poem in detail, can you think of a deeper meaning?",
     ["Humans have cut and confined nature; nature will take back its place.", "It can also mean women, long confined to homes, breaking free to find their identity."], TP(5))

C.extract("ext1", MOVE, "The trees inside are moving out\ninto the forest,\nthe forest that was empty all these days\nwhere no bird could sit",
  [("Where are the trees?", "Inside the house."), ("Where are they moving?", "Out into the forest."), ("Why was the forest empty?", "Its trees had been taken into houses."),
   ("Name one more thing that could not happen in the empty forest.", "No insect could hide / no sun bury its feet in shadow."), ("Name the device in 'trees... are moving out'.", "Personification.")])
C.extract("ext2", DEV, "like newly discharged patients\nhalf-dazed, moving\nto the clinic doors.",
  [("What is compared to discharged patients?", "The long-cramped boughs (branches) of the trees."), ("Name the figure of speech.", "Simile."),
   ("Why 'half-dazed'?", "They are weak and confused after long confinement."), ("Where are they moving?", "Out of the house into the forest."), ("What do the trees seek?", "Freedom.")])

C.m("mcq01", MOVE, "The Trees was written by:", [("Adrienne Rich", ""), ("Robin Klein", "Adrienne Rich."), ("Carl Sandburg", "Adrienne Rich."), ("Robert Frost", "Adrienne Rich.")], "An American poet.")
C.m("mcq02", MOVE, "What do the roots do all night?", [("work to free themselves from the cracks in the veranda floor", ""), ("sleep", "They work to get free."), ("drink water", "They work to get free."), ("grow deeper", "They pull free.")], "The trees are breaking out.")
C.m("mcq03", DEV, "'The moon is broken like a mirror' is a:", [("simile", ""), ("metaphor", "There is 'like'."), ("pun", "A simile."), ("hyperbole", "A simile.")], "Its light is broken by the branches.")
C.m("mcq04", MEAN, "The poet, while the trees leave, is:", [("writing long letters", ""), ("helping the trees", "She writes letters."), ("sleeping", "She writes letters."), ("cutting the trees", "She writes letters.")], "She scarcely mentions the trees.")
C.m("mcq05", DEV, "The smell of leaves and lichen reaches the rooms:", [("like a voice", ""), ("like smoke", "Like a voice."), ("like music", "Like a voice."), ("like rain", "Like a voice.")], "Nature seems to call.")
C.m("mcq06", MEAN, "The poem can be read as a symbol of:", [("nature and women breaking free from confinement", ""), ("a storm", "Breaking free."), ("a festival", "Breaking free."), ("city life", "Breaking free.")], "Both readings are common.")
C.m("mcq07", DEV, "The poem is written in:", [("free verse", ""), ("rhyming couplets", "Free verse."), ("a sonnet", "Free verse."), ("limericks", "Free verse.")], "Its flow is dream-like.")
C.m("mcq08", MOVE, "What happens at the end of the poem?", [("the glass breaks and the trees stumble into the night", ""), ("the trees die", "They move out."), ("the poet plants new trees", "They move out."), ("it begins to snow", "They move out.")], "The winds rush to meet them.")
C.tf("tf1", MEAN, "The poet describes the trees' departure in detail in her letters.", False, "She scarcely mentions it.")
C.tf("tf2", MOVE, "The long-cramped boughs are compared to newly discharged patients.", True, "Half-dazed, moving to the clinic doors.")

chapter = header("poem07", 16, "The Trees", "Adrienne Rich", "poem", ["trees_moving_out", "deeper_meaning", "poetic_devices"],
                 "CBSE 2025-26 English Language and Literature (184): First Flight poem 7. Assessed through poetry extracts (5 marks) and short answers (3 marks). Only short lines are quoted here; read the full poem in the NCERT textbook.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
