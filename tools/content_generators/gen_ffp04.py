"""CBSE Class 10 English, First Flight Poem 4: How to Tell Wild Animals (Carolyn Wells)."""
import sys
from lit_common import make, header, path, ex, closing

ROOT = sys.argv[1]
PATH = path("p04_how_to_tell_wild_animals")
C = make("ff10p04")
blk = C.blk
ANIMALS, HUMOUR, DEV = ["animals_and_their_signs"], ["humour_in_the_poem"], ["poetic_devices"]
TP = lambda n: ex(n, "Thinking about the Poem")

TAB = ("| Animal | How to 'tell' it, according to the poem |\n|---|---|\n"
       "| **Asian Lion** | a large, tawny beast in the jungles of the East; it roars at you as you are dying |\n"
       "| **Bengal Tiger** | a noble wild beast with black stripes on a yellow ground; notice if he eats you |\n"
       "| **Leopard** | a beast whose hide is peppered with spots; you know it as soon as it has leapt on you |\n"
       "| **Bear** | a creature that hugs you very, very hard; if in doubt, it gives one more 'caress' |\n"
       "| **Hyena and Crocodile** | hyenas come with merry smiles; if they weep, they are crocodiles |\n"
       "| **Chameleon** | small, like a lizard, no ears or wings; if you see nothing on the tree, it is the chameleon |")

sections = [
 {"id": "s1", "title": "A guide you should not follow", "blocks": [
  blk("s1.hook", "hook", title="How do you recognise a lion? Wait until it roars at you as you die!",
    body="This poem pretends to be a helpful guide for identifying wild animals. But every 'test' works only when it is **too late**. **Carolyn Wells** uses this trick to make us laugh."),
  blk("s1.inspiration", "inspiration", title="The poet", person="Carolyn Wells", years="1862–1942",
    body="**Carolyn Wells** was an American writer of humorous verse, nonsense poems and mystery novels. Her playful poems are full of puns, odd spellings and twists.",
    future="Comic writing, advertising and cartooning use the same tricks: surprise, exaggeration and wordplay."),
  C.socratic("s1.socratic", "Why is the advice in this poem useless in real life?",
    ["You can identify each animal only after it has attacked you", "The animals are not real", "The poem gives too many facts"], 0,
    "That is the joke of the poem."),
 ]},
 {"id": "s2", "title": "Animal by animal", "blocks": [
  blk("s2.thm", "theory", title="What the poem says", revision=True,
    body="The poet tells us how to recognise six wild animals, each in its own stanza, and every time the 'clue' comes too late:\n\n" + TAB + "\n\n"
         "**The joke:** each identification comes only when the animal is attacking you. The tone is light and comic; the poem is meant to entertain, not to teach zoology."),
  C.kc("s2.check", "How can you identify the Bengal Tiger, according to the poem?",
    [("by noticing whether it eats you", ""), ("by its spots", "That is the leopard."), ("by its hug", "That is the bear."), ("by its tears", "That is the crocodile.")],
    "It has black stripes on a yellow ground.")
  ,C.kc("s2.check2", "How can you tell a hyena from a crocodile?",
    [("hyenas come with merry smiles; crocodiles weep", ""), ("by their colour", "By smiles and tears."), ("by their size", "By smiles and tears."), ("by their roar", "By smiles and tears.")],
    "'Crocodile tears' are false tears.")
 ]},
 {"id": "s3", "title": "Humour and devices", "blocks": [
  blk("s3.thm", "theory", title="How the poet makes us laugh", revision=True,
    body="| Device | Example | Effect |\n|---|---|---|\n| **Humour / irony** | 'Just notice if he eats you' | the test comes too late |\n"
         "| **Poetic licence** | 'dyin'' (dying), 'lept' / 'lep' (leapt, leap) | changes spelling to keep rhyme and rhythm |\n"
         "| **Rhyme scheme** | ababcc in each stanza | a neat, sing-song rhythm |\n| **Alliteration** | 'who **h**ugs you very, very **h**ard'; '**B**e sure it is a **B**ear' | music and fun |\n"
         "| **Pun** | 'caress' for a deadly hug | a gentle word for a dangerous act |\n| **Inversion** | 'if there should to you advance a large and tawny beast' | an old-fashioned order that sounds grand |\n"
         "| **Idiom** | crocodile tears | false tears; the hyena smiles, the crocodile weeps |"),
  C.kc("s3.check", "Why does the poet write 'dyin'' instead of 'dying'?",
    [("to rhyme with 'Lion' (poetic licence)", ""), ("it is a spelling mistake", "It is deliberate."), ("it is the American spelling", "It is poetic licence."), ("to sound sad", "To rhyme.")],
    "Poets may bend rules for rhyme and rhythm.")
 ]},
 closing(C,
   "- **Six animals in order: Lion, Tiger, Leopard, Bear, Hyena/Crocodile, Chameleon.**\n- **Every clue comes too late: roar, eat, leap, hug, weep, invisible.**\n- **Rhyme: ababcc; poetic licence: dyin', lept, lep.**",
   "1. Taking the poem as serious advice: it is **humorous**.\n2. Saying the tiger has spots: the **leopard** has spots; the tiger has black stripes on yellow.\n3. Calling 'dyin'' a mistake: it is **poetic licence**.",
   "Students add a new stanza in the same style for another animal (for example, a snake or an elephant), with a clue that comes too late.",
   "Which line in the poem made you laugh the most? Why?",
   "- **The Tale of Custard the Dragon:** another comic poem.\n- **A Tiger in the Zoo:** a serious poem about a tiger.",
   "How does Carolyn Wells use humour in 'How to Tell Wild Animals'? Answer in about 120 words.",
   "The poem pretends to be a guide to recognising wild animals, but each clue comes too late to help. You will know the Asian Lion when it roars at you as you are dying, and the Bengal Tiger if it eats you. The leopard is known once it has leapt on you, and the bear by its deadly hug, gently called a 'caress'. Hyenas smile while crocodiles weep their famous tears, and the chameleon is recognised when you see nothing at all. The poet also bends spellings ('dyin'', 'lep') to keep the rhyme and rhythm, which adds to the fun. Through irony, wordplay and a light tone, the poem entertains us rather than teaching zoology.",
   "- The poem 'teaches' how to identify six wild animals.\n- Each clue is useful only when the animal attacks, which is the joke.\n- Humour comes from irony, puns, poetic licence and a sing-song rhyme.",
   "- In answers, name the animal and its 'clue'.\n- Explain poetic licence with 'dyin'' and 'lep'.\n- State clearly that the tone is humorous.",
   [("How do you identify a leopard, according to the poem?", "By its spotted hide, as soon as it has leapt on you."),
    ("What is poetic licence?", "A poet's freedom to bend spelling or grammar, as in 'dyin'' and 'lep', for rhyme and rhythm.")]),
]

C.sa("ex1", ANIMALS, "Which animal is described as 'a large and tawny beast'? How will you recognise it?",
     ["The Asian Lion.", "According to the poem, it roars at you as you are dying, so you recognise it only too late."], TP(1))
C.sa("ex2", HUMOUR, "Do you think the poet's advice on recognising animals is serious? Why or why not?",
     ["No, it is humorous.", "Every clue (roaring, eating, leaping, hugging) works only after the animal has attacked, which is useless as advice."])
C.sa("ex3", DEV, "Find examples of poetic licence in the poem and say why the poet uses them.",
     ["'Dyin'' instead of 'dying', and 'lep' / 'lept' instead of 'leap' / 'leapt'.", "She bends the spellings to keep the rhyme (dyin'/Lion) and the rhythm."])
C.sa("ex4", ANIMALS, "How can you distinguish a hyena from a crocodile, according to the poem?",
     ["Hyenas come with merry smiles.", "If they weep, they are crocodiles, a play on the idiom 'crocodile tears'."])

C.extract("ext1", ANIMALS, "If ever you should go by chance\nTo jungles in the East;\nAnd if there should to you advance\nA large and tawny beast,",
  [("Which animal is being described?", "The Asian Lion."), ("What does 'tawny' mean?", "Brownish-yellow."),
   ("How will you recognise it, according to the poem?", "It roars at you as you are dying."), ("Name the device in 'there should to you advance'.", "Inversion."),
   ("What is the tone of the poem?", "Humorous.")])
C.extract("ext2", ANIMALS, "If when you're walking round your yard\nYou meet a creature there,\nWho hugs you very, very hard,\nBe sure it is a Bear.",
  [("Which animal is described?", "The bear."), ("How does it greet you?", "It hugs you very, very hard."),
   ("Why is the hug dangerous?", "A bear's hug can crush and kill."), ("Find the repeated word.", "'very'."), ("What word does the poet later use for this hug?", "Caress.")])

C.m("mcq01", ANIMALS, "Which animal has 'black stripes on a yellow ground'?", [("the Bengal Tiger", ""), ("the leopard", "It has spots."), ("the lion", "It is tawny."), ("the bear", "It hugs.")], "Notice if he eats you!")
C.m("mcq02", ANIMALS, "The leopard's hide is:", [("peppered with spots", ""), ("striped", "That is the tiger."), ("plain tawny", "That is the lion."), ("green", "That is not in the poem.")], "You know it when it leaps on you.")
C.m("mcq03", ANIMALS, "The chameleon is described as:", [("small, like a lizard, with no ears or wings", ""), ("large and tawny", "That is the lion."), ("a noble wild beast", "That is the tiger."), ("a creature that hugs", "That is the bear.")], "If you see nothing on the tree, it is the chameleon.")
C.m("mcq04", HUMOUR, "The tone of the poem is:", [("humorous", ""), ("tragic", "It is comic."), ("scientific", "It is comic."), ("angry", "It is comic.")], "It makes fun of 'guides'.")
C.m("mcq05", DEV, "'He'll only lep and lep again' uses 'lep' instead of 'leap'. This is:", [("poetic licence", ""), ("a printing error", "It is deliberate."), ("a simile", "Poetic licence."), ("a metaphor", "Poetic licence.")], "For rhyme and rhythm.")
C.m("mcq06", DEV, "The rhyme scheme of each stanza is:", [("ababcc", ""), ("aabbcc", "ababcc."), ("abcabc", "ababcc."), ("abab", "Six lines: ababcc.")], "A sing-song pattern.")
C.m("mcq07", HUMOUR, "'Crocodile tears' means:", [("false tears", ""), ("tears of joy", "False tears."), ("tears of pain", "False tears."), ("rain", "False tears.")], "The poet plays on this idiom.")
C.m("mcq08", HUMOUR, "The bear's hug is called a:", [("caress", ""), ("greeting", "A caress."), ("blessing", "A caress."), ("game", "A caress.")], "A gentle word for a deadly act: irony.")
C.tf("tf1", HUMOUR, "The poem gives serious, practical advice for identifying animals.", False, "It is humorous; every clue comes too late.")
C.tf("tf2", ANIMALS, "Hyenas, according to the poem, come with merry smiles.", True, "If they weep, they are crocodiles.")

chapter = header("poem04", 13, "How to Tell Wild Animals", "Carolyn Wells", "poem", ["animals_and_their_signs", "humour_in_the_poem", "poetic_devices"],
                 "CBSE 2025-26 English Language and Literature (184): First Flight poem 4. Assessed through poetry extracts (5 marks) and short answers (3 marks).")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
