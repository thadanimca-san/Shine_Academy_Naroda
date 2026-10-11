"""CBSE Class 10 English, First Flight Poem 5: The Ball Poem (John Berryman). Short quotes only."""
import sys
from lit_common import make, header, path, ex, closing

ROOT = sys.argv[1]
PATH = path("p05_the_ball_poem")
C = make("ff10p05")
blk = C.blk
LOSS, LESSON, DEV = ["the_boy_and_his_loss"], ["learning_to_bear_loss"], ["poetic_devices"]
TP = lambda n: ex(n, "Thinking about the Poem")

sections = [
 {"id": "s1", "title": "A small loss, a big lesson", "blocks": [
  blk("s1.hook", "hook", title="It was only a ball, or was it?",
    body="A boy's ball bounces down the street and falls into the harbour. An adult watching could easily buy him another one. But the poet chooses **not to**. Why? Because the boy is learning one of life's hardest lessons: **how to bear loss**."),
  blk("s1.inspiration", "inspiration", title="The poet", person="John Berryman", years="1914–1972",
    body="**John Berryman** was an American poet, a Pulitzer Prize winner, known for poems about inner feelings and suffering. The Ball Poem shows how a small event in childhood can hold a big truth.",
    future="Psychologists, teachers and parents help children deal with loss; this poem shows why that matters."),
  C.socratic("s1.socratic", "Why does the poet not offer to buy the boy a new ball?",
    ["The boy must learn to accept loss; a new ball cannot replace what he has lost", "The poet has no money", "The poet dislikes the boy"], 0,
    "'Money is external.'"),
 ]},
 {"id": "s2", "title": "The poem and its meaning", "blocks": [
  blk("s2.thm", "theory", title="What the poem says", revision=True,
    body="**The loss:** the poet asks, 'What is the boy now, who has lost his ball, / What, what is he to do?' He saw the ball go **merrily bouncing** down the street and then **merrily over**, into the water.\n\n"
         "**The boy's grief:** the boy stands **rigid, trembling**, staring down **'all his young days'** into the harbour where his ball went. The ball is linked with the memories of his childhood days.\n\n"
         "**No intrusion:** the poet says 'No use to say \"O there are other balls\"'. He **would not intrude** on the boy. He will not offer him **a dime** for another ball: it is worthless. The boy must learn, for the first time, the **responsibility** of possessing things in 'the world of possessions'.\n\n"
         "**The lesson:** **'Balls will be lost always, little boy'**. Money is **external**: it cannot buy back what is truly lost. The boy is learning **'the epistemology of loss'**, that is, the nature of loss and how to stand up after it. Everyone has to learn this some day."),
  blk("s2.table", "markdown_table", title="Key phrases", revision=True,
    body="| Phrase | Meaning |\n|---|---|\n| **'merrily bouncing... merrily over'** | the ball's happy movement contrasts with the boy's sadness |\n"
         "| **'staring down / All his young days'** | the ball holds the memories of his childhood |\n| **'I would not intrude on him'** | the poet will not interfere; the boy must face this alone |\n"
         "| **'the world of possessions'** | a world where we own things and must accept losing them |\n| **'Money is external'** | money cannot replace feelings or memories |\n"
         "| **'the epistemology of loss'** | knowing what loss means and how to bear it |"),
  C.kc("s2.check", "What does 'the epistemology of loss' mean?",
    [("understanding the nature of loss and how to cope with it", ""), ("a science of balls", "It is about understanding loss."), ("the price of a ball", "It is about loss."), ("a game", "It is about loss.")],
    "Epistemology is the study of knowledge.")
  ,C.kc("s2.check2", "Where did the boy's ball go?",
    [("into the harbour", ""), ("onto a roof", "Into the water of the harbour."), ("into a shop", "Into the harbour."), ("down a well", "Into the harbour.")],
    "It bounced down the street and then over into the water.")
 ]},
 {"id": "s3", "title": "Devices and theme", "blocks": [
  blk("s3.thm", "theory", title="How the poem works", revision=True,
    body="| Device | Example |\n|---|---|\n| **Repetition** | 'What, what is he to do?'; 'merrily... merrily' |\n| **Enjambment** | lines run on, like the boy's flowing thoughts |\n"
         "| **Free verse** | no regular rhyme scheme |\n| **Symbolism** | the ball stands for childhood, and for everything we will lose in life |\n| **Contrast** | 'merrily' bouncing ball vs the 'rigid, trembling' boy |\n\n"
         "**Theme:** loss is part of life. We grow up when we learn to accept it and stand up again; no money can buy back what we have truly lost."),
  C.kc("s3.check", "The ball in the poem symbolises:",
    [("childhood and the things we lose in life", ""), ("sport", "It is a symbol of loss."), ("money", "Money is external."), ("the harbour", "The ball is the symbol.")],
    "The boy is learning about loss.")
 ]},
 closing(C,
   "- **Ball → harbour; boy rigid, trembling; poet won't intrude; money is external; balls will be lost always; epistemology of loss.**\n- **Form: free verse.**",
   "1. Thinking the poet is unkind: he lets the boy **learn** to bear loss.\n2. Saying the boy will get another ball: the poet refuses to give money for one.\n3. Thinking the poem is only about a ball: it is about **all loss**.",
   "Ask students to describe something they lost and how they got over it, in five sentences.",
   "Have you ever lost something you liked very much? How did you feel, and how did you get over it?",
   "- **Madam Rides the Bus and The Sermon at Benares:** first lessons in loss and death.",
   "'Balls will be lost always, little boy.' What lesson does the boy learn? Answer in about 120 words.",
   "The boy's ball, which he has had for a long time, bounces into the harbour. He stands rigid and trembling, staring at the water as if all his young days had gone with it, because the ball carried his childhood memories. The poet could buy him another ball, but he chooses not to intrude: a new ball would not replace what is lost, since 'money is external'. The boy is learning, for the first time, the responsibility of owning things in a world of possessions, where things will always be lost. He is learning 'the epistemology of loss', that is, how to understand loss and stand up again. This is a lesson every person must learn to grow up.",
   "- A boy loses his ball in the harbour and is deeply upset.\n- The poet does not intrude or offer money for a new ball.\n- The boy is learning that loss is part of life and must be borne: 'the epistemology of loss'.",
   "- Explain 'money is external' and 'epistemology of loss' in simple words.\n- Show why the poet does not intrude.\n- Link the ball to childhood and to life's other losses.",
   [("Why doesn't the poet buy the boy another ball?", "The boy must learn to accept loss; money is external and cannot replace what is lost."),
    ("What is 'the epistemology of loss'?", "Understanding what loss is and how to stand up after it.")]),
]

C.sa("ex1", LESSON, "Why does the poet say, 'I would not intrude on him'? Why doesn't he offer him money to buy another ball?",
     ["He wants the boy to learn on his own how to face loss.", "Money is external; a new ball cannot replace the lost one and its memories."], TP(1))
C.sa("ex2", LOSS, "'... staring down / All his young days into the harbour where / His ball went...' Do you think the boy has had the ball for a long time? Is it linked to memories of days when he played with it?",
     ["Yes, he seems to have had it for a long time.", "The ball holds memories of his childhood days of play, so losing it feels like losing those days."], TP(2))
C.sa("ex3", LESSON, "What does 'in the world of possessions' mean?",
     ["It means the world in which we own things.", "Owning things carries the responsibility of accepting that they can be lost."], TP(3))
C.sa("ex4", LOSS, "Do you think the boy has lost anything earlier? Pick out the words that suggest the answer.",
     ["No, this seems to be his first loss.", "'He senses first responsibility in a world of possessions' shows it is his first experience of loss."], TP(4))
C.sa("ex5", LESSON, "What does the poet say the boy is learning from the loss of the ball? Try to explain this in your own words.",
     ["He is learning the 'epistemology of loss': what loss means.", "He learns that loss is part of life, that money cannot bring back what is lost, and that he must stand up again."], TP(5))

C.extract("ext1", LOSS, "What is the boy now, who has lost his ball,\nWhat, what is he to do? I saw it go\nMerrily bouncing, down the street, and then\nMerrily over — there it is in the water!",
  [("Name the poem and the poet.", "The Ball Poem, John Berryman."), ("Where has the ball gone?", "Into the water of the harbour."),
   ("Name the device in 'What, what'.", "Repetition."), ("What is the contrast in 'merrily'?", "The ball moves happily while the boy is sad."), ("How does the boy react?", "He stands rigid and trembling, staring at the water.")])
C.extract("ext2", LESSON, "Balls will be lost always, little boy,\nAnd no one buys a ball back. Money is external.",
  [("Who speaks these words?", "The poet."), ("What does 'Money is external' mean?", "Money cannot replace feelings or what is truly lost."),
   ("What truth does the first line state?", "Losing things is a part of life."), ("Why will no one 'buy a ball back'?", "The lost thing, with its memories, cannot be replaced."), ("What is the boy learning?", "To accept and bear loss.")])

C.m("mcq01", LOSS, "The Ball Poem was written by:", [("John Berryman", ""), ("Robert Frost", "John Berryman."), ("Robin Klein", "John Berryman."), ("Leslie Norris", "John Berryman.")], "An American poet.")
C.m("mcq02", LOSS, "How does the boy react to the loss?", [("he stands rigid and trembling, staring into the harbour", ""), ("he laughs", "He is shocked and sad."), ("he dives in", "He stares."), ("he runs home", "He stares.")], "He seems frozen in grief.")
C.m("mcq03", LESSON, "Why does the poet not intrude?", [("the boy must learn to bear loss himself", ""), ("he is busy", "So the boy can learn."), ("he is afraid of the boy", "So the boy can learn."), ("he did not see the loss", "He saw it.")], "This is an important lesson.")
C.m("mcq04", LESSON, "'Money is external' means:", [("money cannot replace what is lost inside us", ""), ("money is kept outside", "It cannot replace feelings."), ("money is useful", "It cannot replace the loss."), ("money grows", "It cannot replace the loss.")], "Feelings and memories cannot be bought.")
C.m("mcq05", DEV, "The poem is written in:", [("free verse", ""), ("rhyming couplets", "No regular rhyme."), ("sonnet form", "Free verse."), ("abab quatrains", "Free verse.")], "It reads like natural thought.")
C.m("mcq06", LOSS, "The ball goes 'merrily bouncing'. 'Merrily' creates a:", [("contrast with the boy's sorrow", ""), ("sad mood", "It contrasts with sorrow."), ("rhyme", "A contrast."), ("question", "A contrast.")], "The world goes on while the boy grieves.")
C.m("mcq07", LESSON, "The boy is learning 'the epistemology of loss'. 'Epistemology' means:", [("the study of knowledge, how we know things", ""), ("a disease", "The study of knowledge."), ("a kind of ball", "The study of knowledge."), ("a harbour", "The study of knowledge.")], "Here, knowing what loss means.")
C.m("mcq08", LESSON, "What will the poet NOT offer the boy?", [("a dime to buy another ball", ""), ("sympathy", "He feels for him."), ("silence", "He stays silent."), ("understanding", "He understands.")], "He knows it would be worthless.")
C.tf("tf1", LESSON, "The poet buys the boy a new ball.", False, "He would not intrude or offer money.")
C.tf("tf2", LOSS, "The ball fell into the harbour.", True, "It bounced down the street and over into the water.")
C.la("la1", LESSON, "Have you ever lost something you liked very much? Describe how you felt and how you got over it, linking your experience to The Ball Poem.",
     ["Describe the lost thing and why it mattered to you (memories).", "Your feelings: shock and sadness, like the boy standing rigid and trembling.",
      "How you got over it: time, accepting it, focusing on other things; a replacement did not fully help, as 'money is external'.",
      "Link: like the boy, you learnt 'the epistemology of loss': loss is part of life, and we grow by bearing it."], TP(6))

chapter = header("poem05", 14, "The Ball Poem", "John Berryman", "poem", ["the_boy_and_his_loss", "learning_to_bear_loss", "poetic_devices"],
                 "CBSE 2025-26 English Language and Literature (184): First Flight poem 5. Assessed through poetry extracts (5 marks) and short answers (3 marks). Only short lines are quoted here; read the full poem in the NCERT textbook.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
