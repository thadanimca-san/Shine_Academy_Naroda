"""CBSE Class 10 English, First Flight Poem 10: For Anne Gregory (W. B. Yeats). Short quotes only."""
import sys
from lit_common import make, header, path, ex, closing

ROOT = sys.argv[1]
PATH = path("p10_for_anne_gregory")
C = make("ff10p10")
blk = C.blk
BEAUTY, LOVE, DEV = ["outer_and_inner_beauty"], ["true_love"], ["form_and_devices"]
TP = lambda n: ex(n, "Thinking about the Poem")

sections = [
 {"id": "s1", "title": "Loved for yourself alone?", "blocks": [
  blk("s1.hook", "hook", title="Would they still love you without your golden hair?",
    body="A beautiful young woman wants to be loved for who she is, not for her lovely yellow hair. An older man tells her that only **God** can love a person for herself alone. This short conversation-poem asks: **what do we really love in people?**"),
  blk("s1.inspiration", "inspiration", title="The poet", person="W. B. Yeats", years="1865–1939",
    body="**William Butler Yeats** was an Irish poet and dramatist who won the **Nobel Prize in Literature in 1923**. He wrote For Anne Gregory for the granddaughter of his friend **Lady Augusta Gregory**.",
    future="Psychologists and writers study how appearance affects the way people are treated."),
  C.socratic("s1.socratic", "Why does the young woman want to dye her hair?",
    ["So that men will love her for herself, not her looks", "Because yellow hair is unfashionable", "Because her mother tells her to"], 0,
    "She wants to be valued for her inner self."),
 ]},
 {"id": "s2", "title": "The conversation", "blocks": [
  blk("s2.thm", "theory", title="What the poem says", revision=True,
    body="**Stanza 1, the poet (an older man):** young men, 'thrown into despair' by her **'great honey-coloured ramparts'** at her ear (her beautiful yellow hair), can never love her **for herself alone**, but only for her **yellow hair**.\n\n"
         "**Stanza 2, Anne Gregory:** she replies that she can get **hair dye** and set such colour there, **brown, or black, or carrot**, so that young men in despair may love her for herself alone and not her yellow hair.\n\n"
         "**Stanza 3, the poet:** he says he heard an **old religious man** declare 'but yesternight' that he had found a **text** to prove that **only God**, my dear, could love you for yourself alone and not your yellow hair.\n\n"
         "**Message:** human beings are attracted by **outer beauty**; only God loves a person for their **inner self**. Anne wants pure love, but the poet suggests that this is beyond human nature."),
  blk("s2.table", "markdown_table", title="Key phrases", revision=True,
    body="| Phrase | Meaning |\n|---|---|\n| **'great honey-coloured ramparts at your ear'** | her thick, yellow hair falling over her ears like a protective wall |\n"
         "| **'thrown into despair'** | young men are hopelessly in love because of her beauty |\n| **'for yourself alone'** | for her inner qualities, her real self |\n"
         "| **'brown, or black, or carrot'** | the colours she could dye her hair |\n| **'an old religious man'** | a wise, spiritual person who quotes a holy text |\n| **'only God... could love you for yourself alone'** | only divine love sees beyond appearance |"),
  C.kc("s2.check", "What are 'honey-coloured ramparts'?",
    [("her thick yellow hair, like a wall around her ears", ""), ("the walls of her house", "Her hair."), ("her earrings", "Her hair."), ("a city's walls", "Her hair.")],
    "A rampart is a protective wall.")
  ,C.kc("s2.check2", "Who, according to the old religious man, can love her for herself alone?",
    [("only God", ""), ("young men", "They love her hair."), ("her parents", "Only God."), ("the poet", "Only God.")],
    "Human love is drawn to appearance.")
 ]},
 {"id": "s3", "title": "Form and devices", "blocks": [
  blk("s3.thm", "theory", title="How the poem works", revision=True,
    body="- **Dialogue form:** stanza 1 the poet, stanza 2 Anne, stanza 3 the poet.\n- **Metaphor:** 'honey-coloured ramparts' for hair.\n- **Repetition:** 'for yourself alone' and 'yellow hair' end each stanza, stressing the contrast between self and looks.\n"
         "- **Rhyme scheme:** abcbdefe (lines 2 and 4, 6 and 8 rhyme).\n- **Tone:** gentle, teasing, wise.\n- **Opposites of 'young' in the poem:** 'old' (old religious man) and 'yesternight' points to the past, too."),
  C.kc("s3.check", "The poem is written as:",
    [("a conversation between the poet and Anne", ""), ("a letter", "A dialogue."), ("a prayer", "A dialogue."), ("a story told by Anne alone", "A dialogue.")],
    "Three stanzas, two speakers.")
 ]},
 closing(C,
   "- **3 stanzas: poet → Anne → poet.**\n- **Hair: yellow; dye options: brown, black, carrot.**\n- **Only God loves 'for yourself alone'.**",
   "1. Saying Anne has brown hair: her hair is **yellow** (golden); she offers to dye it brown, black or carrot.\n2. Thinking the poet wants her to dye it: he says it would not help; only God loves for the self.\n3. Missing the dialogue form.",
   "Discuss: list five things people notice first about others, and five things that matter more. Link to the poem.",
   "Do people today judge others by appearance? Give one example from school or social media.",
   "- **The Proposal:** marriage based on property, not the person.\n- **Amanda!:** a young person who wants to be understood.",
   "'Only God could love you for yourself alone.' Discuss the poem's view of love and beauty in about 120 words.",
   "In For Anne Gregory, a young woman with beautiful yellow hair wants to be loved for her real self. The poet tells her that the young men who are thrown into despair by her 'honey-coloured ramparts' love only her hair. She replies that she will dye it brown, black or carrot, so that she may be loved for herself alone. The poet answers that an old religious man has found a text proving that only God can love a person for herself alone and not for her yellow hair. The poem suggests that human love is always drawn first to outer beauty, while pure love for the inner self belongs to God. It asks us to look beyond appearance.",
   "- The poet says young men will love Anne only for her beautiful yellow hair.\n- Anne says she will dye her hair so she is loved for herself.\n- The poet replies that only God can love a person for herself alone.",
   "- Name the speaker of each stanza.\n- Explain 'honey-coloured ramparts' and 'for yourself alone'.\n- State the theme: outer versus inner beauty.",
   [("What colour is Anne's hair, and what could she change it to?", "Yellow; she says she could dye it brown, black or carrot."),
    ("Who can love her 'for herself alone'?", "Only God, according to the old religious man.")]),
]

C.sa("ex1", BEAUTY, "What does the young man mean by 'great honey-coloured / Ramparts at your ear'? Why does he say that young men are 'thrown into despair' by them?",
     ["He means her thick, beautiful yellow hair falling over her ears like a wall.", "Young men fall hopelessly in love with her beauty, so they are thrown into despair."], TP(1))
C.sa("ex2", BEAUTY, "What colour is the young woman's hair? What does she say she can change it to? Why would she want to do so?",
     ["Her hair is yellow (golden); she can dye it brown, black or carrot.", "She wants to be loved for herself alone, not for her hair."], TP(2))
C.sa("ex3", LOVE, "Can you find the words in the poem that mean the opposite of 'young'? What does the old religious man say?",
     ["'Old' (an old religious man) is the opposite of young.", "He says he found a text proving that only God could love her for herself alone and not her yellow hair."], TP(3))

C.extract("ext1", BEAUTY, "'Never shall a young man,\nThrown into despair\nBy those great honey-coloured\nRamparts at your ear,'",
  [("Who speaks these lines?", "The poet."), ("To whom?", "Anne Gregory."), ("What are 'honey-coloured ramparts'?", "Her yellow hair."),
   ("Why are young men in despair?", "They are hopelessly in love with her beauty."), ("Name the device in 'honey-coloured ramparts'.", "Metaphor.")])
C.extract("ext2", LOVE, "That only God, my dear,\nCould love you for yourself alone\nAnd not your yellow hair.",
  [("Who had said that only God could love her for herself?", "An old religious man."), ("What does 'for yourself alone' mean?", "For her inner qualities, her real self."),
   ("What do people usually love her for?", "Her yellow hair, her outward beauty."), ("What is the theme of these lines?", "True love sees inner beauty; only God loves that way."), ("Name the poet.", "W. B. Yeats.")])

C.m("mcq01", BEAUTY, "For Anne Gregory was written by:", [("W. B. Yeats", ""), ("Robert Frost", "W. B. Yeats."), ("John Berryman", "W. B. Yeats."), ("Carolyn Wells", "W. B. Yeats.")], "An Irish Nobel laureate.")
C.m("mcq02", BEAUTY, "What colour is Anne's hair?", [("yellow", ""), ("black", "She could dye it black."), ("brown", "She could dye it brown."), ("carrot", "She could dye it carrot.")], "Honey-coloured.")
C.m("mcq03", BEAUTY, "Which colour does Anne NOT mention for dyeing her hair?", [("blonde", ""), ("brown", "She mentions brown."), ("black", "She mentions black."), ("carrot", "She mentions carrot.")], "Brown, black or carrot.")
C.m("mcq04", LOVE, "Who found a text about God's love?", [("an old religious man", ""), ("Anne", "An old religious man."), ("a young man", "An old religious man."), ("the poet's friend", "An old religious man.")], "He declared it 'but yesternight'.")
C.m("mcq05", DEV, "'Ramparts' are:", [("protective walls", ""), ("ribbons", "Walls."), ("earrings", "Walls."), ("rivers", "Walls.")], "Her hair is like a wall at her ear.")
C.m("mcq06", LOVE, "The theme of the poem is:", [("outer beauty versus inner beauty", ""), ("hair care", "Outer vs inner beauty."), ("religion only", "Outer vs inner beauty."), ("youth and old age only", "Outer vs inner beauty.")], "Only God loves the inner self.")
C.m("mcq07", DEV, "The poem is in the form of:", [("a dialogue", ""), ("a sonnet", "A dialogue."), ("a ballad about a battle", "A dialogue."), ("a list", "A dialogue.")], "Poet, Anne, poet.")
C.m("mcq08", DEV, "'Yesternight' means:", [("last night", ""), ("tomorrow night", "Last night."), ("every night", "Last night."), ("midnight", "Last night.")], "An old-fashioned word.")
C.tf("tf1", BEAUTY, "Anne Gregory wants to be loved for her yellow hair.", False, "She wants to be loved for herself alone.")
C.tf("tf2", LOVE, "The poet says only God can love a person for herself alone.", True, "He quotes an old religious man.")
C.la("la1", LOVE, "Do you agree that only God can love a person for 'herself alone'? Give reasons.",
     ["The poem says people are first attracted by outer beauty such as Anne's yellow hair.", "Anne wants to be loved for her inner self; the poet says only God's love is that pure.",
      "In life, appearance does draw attention, and media often judge people by looks.", "But parents, true friends and life partners can come to love a person's character over time.",
      "So human love can grow beyond looks, though only divine love begins there."])

chapter = header("poem10", 19, "For Anne Gregory", "W. B. Yeats", "poem", ["outer_and_inner_beauty", "true_love", "form_and_devices"],
                 "CBSE 2025-26 English Language and Literature (184): First Flight poem 10. Assessed through poetry extracts (5 marks) and short answers (3 marks). Only short lines are quoted here; read the full poem in the NCERT textbook.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
