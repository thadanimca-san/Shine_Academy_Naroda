"""CBSE Class 10 English, First Flight Poem 6: Amanda! (Robin Klein). Short quotes only."""
import sys
from lit_common import make, header, path, ex, closing

ROOT = sys.argv[1]
PATH = path("p06_amanda")
C = make("ff10p06")
blk = C.blk
NAG, DREAM, DEV = ["the_nagging_voice"], ["amandas_daydreams"], ["structure_and_devices"]
TP = lambda n: ex(n, "Thinking about the Poem")

TAB = ("| Stanzas | Speaker | What is said |\n|---|---|---|\n"
       "| **1, 3, 5, 7** | an adult, probably her mother | constant instructions: don't bite your nails, don't hunch your shoulders, sit up straight, finish your homework, tidy your room, clean your shoes, don't eat chocolate (remember your acne), look at me when I'm speaking, stop sulking |\n"
       "| **2, 4, 6** (in brackets) | Amanda, in her mind | daydreams: a **mermaid** drifting in a languid emerald sea; an **orphan** roaming the streets, patterning soft dust with bare feet; **Rapunzel** in a tower, never letting down her hair |")

sections = [
 {"id": "s1", "title": "Too many instructions", "blocks": [
  blk("s1.hook", "hook", title="'Don't do this, Amanda! Do that, Amanda!'",
    body="Imagine being told every minute how to sit, what to eat and when to do your homework. **Amanda** hears it all, but her mind has escaped: she is a **mermaid**, an **orphan**, and **Rapunzel** in a tower."),
  blk("s1.inspiration", "inspiration", title="The poet", person="Robin Klein", years="1936–2025",
    body="**Robin Klein** was an Australian writer of children's books, known for understanding young people's feelings. Amanda! shows the gap between what adults demand and what a child longs for.",
    future="Teachers, counsellors and parents learn from such poems how nagging can push children away."),
  C.socratic("s1.socratic", "Why does Amanda escape into daydreams?",
    ["She feels suffocated by constant nagging and wants freedom", "She is bored by the sea", "She is very ill"], 0,
    "Her dreams are all about freedom and peace."),
 ]},
 {"id": "s2", "title": "Two voices", "blocks": [
  blk("s2.thm", "theory", title="How the poem is built", revision=True,
    body="The poem has **two voices** that never meet:\n\n" + TAB + "\n\n"
         "**Amanda's dreams:**\n- As a **mermaid**, she would drift blissfully in a languid **emerald sea**, the sole inhabitant: alone and free.\n"
         "- As an **orphan**, she would roam the streets, patterning soft dust with her bare feet; she thinks silence is 'golden' and freedom is sweet. She is **not** really an orphan; she imagines it to be free of instructions.\n"
         "- As **Rapunzel**, she would live in a tower in peace and would **never let down her bright hair**, so no one could climb up to disturb her.\n\n"
         "**The ending:** 'Stop that sulking at once, Amanda! You're always so moody, Amanda!' and anyone would think she is nagged. The adult does not see that the nagging itself makes her moody."),
  C.kc("s2.check", "Why are stanzas 2, 4 and 6 in brackets?",
    [("they are Amanda's private thoughts and daydreams", ""), ("they are less important", "They show her inner world."), ("they are spoken loudly", "They are silent thoughts."), ("the poet forgot to remove them", "They show her inner world.")],
    "They show what she imagines while she is being scolded.")
  ,C.kc("s2.check2", "Why does Amanda want to be Rapunzel?",
    [("to live alone in a tower in peace, and not let anyone up", ""), ("to have long hair", "For the peace of the tower."), ("to marry a prince", "She would not let down her hair."), ("to be famous", "For peace and solitude.")],
    "She would never let down her bright hair.")
 ]},
 {"id": "s3", "title": "Amanda and the speaker", "blocks": [
  blk("s3.thm", "theory", title="Who is Amanda? What does she want?", revision=True,
    body="**Amanda's age:** about **nine to twelve**: she has homework, must tidy her room, and is warned about acne, which suggests early adolescence.\n\n"
         "**The speaker:** probably her **mother**, who corrects every small thing.\n\n"
         "**Is Amanda listening?** No. She seems lost in her own world; she does not answer at all.\n\n"
         "**What she yearns for:** **freedom, peace and solitude**: no rules, no nagging.\n\n"
         "**Is she moody?** She may seem sulky, but she is reacting to constant criticism. The poem asks adults to **listen** to children rather than only instruct them.\n\n"
         "**Devices:** **repetition** of 'Amanda!'; **contrast** between nagging and dreaming; **allusion** to the fairy tale of **Rapunzel**; **imagery** ('languid emerald sea', 'soft dust')."),
  C.kc("s3.check", "What does Amanda yearn for?",
    [("freedom and peace", ""), ("chocolate", "She dreams of freedom."), ("more homework", "Freedom."), ("a new dress", "Freedom.")],
    "Each daydream is about being free and alone.")
 ]},
 closing(C,
   "- **Stanzas 1, 3, 5, 7: adult nagging. Stanzas 2, 4, 6 (brackets): mermaid, orphan, Rapunzel.**\n- **Last line: 'You're always so moody, Amanda!'**",
   "1. Saying Amanda is really an orphan: she only **imagines** it.\n2. Saying she listens carefully: she is lost in **daydreams**.\n3. Forgetting the purpose of the brackets: they hold her **thoughts**.",
   "Two students read the poem aloud: one as the adult (stanzas 1, 3, 5, 7), one as Amanda (2, 4, 6) in a dreamy voice. Discuss how it feels to be Amanda.",
   "Do you think instructions help children or push them away? How would you speak to Amanda?",
   "- **From the Diary of Anne Frank:** another young girl who feels unheard.\n- **The Ball Poem:** childhood feelings that adults should respect.",
   "What does the poem tell us about the way adults treat children? Answer in about 120 words.",
   "In Amanda!, an adult, probably her mother, gives a stream of instructions: don't bite your nails, don't hunch your shoulders, finish your homework, tidy your room, don't eat chocolate. The adult never asks how Amanda feels. Amanda does not answer; instead she escapes into daydreams, shown in brackets. She imagines being a mermaid alone in an emerald sea, an orphan free to roam the streets, and Rapunzel in a tower who will never let her hair down. All her dreams are about freedom and peace. At the end the adult calls her moody, without seeing that the nagging has made her so. The poem tells adults to guide children gently and to listen to them.",
   "- An adult keeps instructing Amanda in stanzas 1, 3, 5 and 7.\n- In brackets, Amanda dreams of being a mermaid, an orphan and Rapunzel: free and at peace.\n- She is called moody, but she is reacting to constant nagging.",
   "- Explain the brackets and the two speakers.\n- Name all three daydreams and what each means.\n- In long answers, discuss the effect of nagging on children.",
   [("Who speaks in stanzas 2, 4 and 6?", "Amanda, in her thoughts; that is why they are in brackets."),
    ("What are Amanda's three daydreams?", "A mermaid in an emerald sea, an orphan roaming free, and Rapunzel in a tower.")]),
]

C.sa("ex1", NAG, "How old do you think Amanda is? How do you know this?",
     ["She is probably between nine and twelve.", "She has homework and must tidy her room, and is warned about acne, which begins at that age."], TP(1))
C.sa("ex2", NAG, "Who do you think is speaking to her?",
     ["Probably her mother.", "She gives constant instructions about manners, homework, food and behaviour."], TP(2))
C.sa("ex3", DEV, "Why are stanzas 2, 4 and 6 given in parentheses?",
     ["They are Amanda's private thoughts and daydreams.", "They show her inner world, which the speaker cannot hear."], TP(3))
C.sa("ex4", DEV, "Who is the speaker in stanzas 2, 4 and 6? Do you think this speaker is listening to the speaker in stanzas 1, 3, 5 and 7?",
     ["Amanda is the speaker.", "No, she is not listening; she is lost in her own dreams of freedom."], TP(4))
C.sa("ex5", DREAM, "What could Amanda do if she were a mermaid?",
     ["She could drift blissfully in a languid emerald sea.", "She would be the sole inhabitant, alone and free of instructions."], TP(5))
C.sa("ex6", DREAM, "Is Amanda an orphan? Why does she say so?",
     ["No, she is not an orphan.", "She imagines being one so that she could be free of her parents' nagging and roam the streets."], TP(6))
C.sa("ex7", DREAM, "Do you know the story of Rapunzel? Why does Amanda want to be Rapunzel?",
     ["Rapunzel was locked in a tower and let down her long hair for visitors to climb.", "Amanda wants to live alone in peace in the tower and would never let down her hair, so no one could disturb her."], TP(7))
C.sa("ex8", NAG, "What does Amanda yearn for? Do you think Amanda is sulking and is moody?",
     ["She yearns for freedom, peace and solitude.", "She may appear moody, but she is reacting to constant nagging; she is not naturally sulky."], TP(8))

C.extract("ext1", NAG, "Don't bite your nails, Amanda!\nDon't hunch your shoulders, Amanda!\nStop that slouching and sit up straight,\nAmanda!",
  [("Who is probably speaking?", "Amanda's mother."), ("What is the tone of the speaker?", "Nagging, commanding."), ("Name the device in the repeated 'Amanda!'.", "Repetition."),
   ("What does 'slouching' mean?", "Sitting or standing lazily with drooping shoulders."), ("How does Amanda react to such instructions?", "She escapes into daydreams.")])
C.extract("ext2", DREAM, "(I am Rapunzel, I have not a care;\nlife in a tower is tranquil and rare;\nI'll certainly never let down my bright hair!)",
  [("Who is 'I'?", "Amanda, imagining herself as Rapunzel."), ("Why is this stanza in brackets?", "It is her private daydream."),
   ("What does 'tranquil' mean?", "Calm and peaceful."), ("Why will she never let down her hair?", "So no one can climb up and disturb her peace."), ("What does she long for?", "Peace and freedom.")])

C.m("mcq01", NAG, "Amanda! was written by:", [("Robin Klein", ""), ("Carolyn Wells", "Robin Klein."), ("John Berryman", "Robin Klein."), ("Adrienne Rich", "Robin Klein.")], "An Australian writer.")
C.m("mcq02", DREAM, "Which is NOT one of Amanda's daydreams?", [("a pilot", ""), ("a mermaid", "She dreams of this."), ("an orphan", "She dreams of this."), ("Rapunzel", "She dreams of this.")], "Her dreams are about freedom.")
C.m("mcq03", DREAM, "The sea in Amanda's dream is:", [("languid and emerald", ""), ("stormy and grey", "Languid and emerald."), ("frozen", "Languid and emerald."), ("crowded", "She is the sole inhabitant.")], "Calm and green.")
C.m("mcq04", NAG, "Why is Amanda told not to eat chocolate?", [("because of her acne", ""), ("because it is expensive", "Her acne."), ("because she is a mermaid", "Her acne."), ("because it is dinner time", "Her acne.")], "'Remember your acne, Amanda!'")
C.m("mcq05", DEV, "The poem is built on a contrast between:", [("the adult's nagging and Amanda's daydreams", ""), ("day and night", "Nagging and dreams."), ("sea and land", "Nagging and dreams."), ("two sisters", "Nagging and dreams.")], "Two voices that never meet.")
C.m("mcq06", NAG, "At the end Amanda is called:", [("moody", ""), ("brave", "Moody."), ("lazy", "Moody."), ("clever", "Moody.")], "'You're always so moody, Amanda!'")
C.m("mcq07", DREAM, "As an orphan, Amanda imagines:", [("roaming the streets, patterning soft dust with her bare feet", ""), ("living in a castle", "Roaming free."), ("crying alone", "She imagines freedom."), ("going to school", "Roaming free.")], "Silence is golden and freedom is sweet.")
C.m("mcq08", DEV, "'Rapunzel' is an example of:", [("allusion (reference to a fairy tale)", ""), ("simile", "An allusion."), ("onomatopoeia", "An allusion."), ("rhyme", "An allusion.")], "The girl in the tower with long hair.")
C.tf("tf1", DREAM, "Amanda is really an orphan.", False, "She only imagines being one, to escape the nagging.")
C.tf("tf2", DEV, "Stanzas 2, 4 and 6 are in brackets because they are Amanda's thoughts.", True, "The adult cannot hear them.")
C.la("la1", NAG + DREAM, "Imagine you are Amanda. Write a diary entry about the day described in the poem.",
     ["Address and date; describe the stream of instructions: nails, shoulders, homework, room, shoes, chocolate.", "Your feelings: suffocated, unheard, misunderstood.",
      "Your escapes: mermaid in an emerald sea, orphan roaming free, Rapunzel in a tower.", "A wish that your mother would listen to you instead of only giving orders."])

chapter = header("poem06", 15, "Amanda!", "Robin Klein", "poem", ["the_nagging_voice", "amandas_daydreams", "structure_and_devices"],
                 "CBSE 2025-26 English Language and Literature (184): First Flight poem 6. Assessed through poetry extracts (5 marks) and short answers (3 marks). Only short lines are quoted here; read the full poem in the NCERT textbook.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
