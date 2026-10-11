"""CBSE Class 10 English, First Flight Poem 2: Fire and Ice (Robert Frost, 1920; public domain)."""
import sys
from lit_common import make, header, path, ex

ROOT = sys.argv[1]
PATH = path("p02_fire_and_ice")
C = make("ff10p02")
blk = C.blk
MEAN, SYMB, DEV = ["meaning_of_the_poem"], ["fire_and_ice_as_symbols"], ["poetic_devices"]

POEM = ("*Some say the world will end in fire,*\n*Some say in ice.*\n*From what I've tasted of desire*\n*I hold with those who favour fire.*\n"
        "*But if it had to perish twice,*\n*I think I know enough of hate*\n*To say that for destruction ice*\n*Is also great*\n*And would suffice.*")

sections = [
 {"id": "s1", "title": "How will the world end?", "blocks": [
  blk("s1.hook", "hook", title="Fire or ice?",
    body="Scientists have argued about whether the world will end in a great **fire** or in a frozen **ice** age. In nine short lines, **Robert Frost** turns this question inward: the real fire and ice are **inside us**: desire and hatred."),
  blk("s1.inspiration", "inspiration", title="The poet", person="Robert Frost", years="1874–1963",
    body="**Robert Frost**, four-time Pulitzer Prize winner, published Fire and Ice in **1920**. The poem is short, but each word is chosen with care.",
    future="Poems like this train us to read symbols, a skill used in literature, advertising, film and law."),
  C.socratic("s1.socratic", "Why might hatred be compared to ice rather than to fire?",
    ["Hatred is cold, rigid and slowly destroys relationships", "Hatred is warm", "Ice is more beautiful"], 0,
    "Ice suggests coldness, indifference and rigidity."),
 ]},
 {"id": "s2", "title": "The poem and its meaning", "blocks": [
  blk("s2.poem", "theory", title="Fire and Ice", body=POEM),
  blk("s2.thm", "theory", title="What the poem says", revision=True,
    body="**Lines 1-2:** some people believe the world will end in **fire**, others in **ice**.\n\n"
         "**Lines 3-4:** from his experience of **desire**, the poet agrees with those who favour fire. Fire stands for **desire**: greed, lust, ambition and fury, which spread quickly and burn out of control.\n\n"
         "**Lines 5-9:** but if the world had to be destroyed **twice**, he knows enough about **hate** to say that ice would also be great for destruction and 'would **suffice**' (be enough). Ice stands for **hatred**: coldness, indifference, rigidity and intolerance, which destroy slowly.\n\n"
         "**Message:** human emotions such as uncontrolled desire and hatred can destroy the world."),
  blk("s2.table", "markdown_table", title="Fire and ice as symbols", revision=True,
    body="| Symbol | Stands for | How it destroys |\n|---|---|---|\n| **Fire** | desire: greed, avarice, lust, conflict, fury | spreads quickly and burns everything |\n"
         "| **Ice** | hatred: cruelty, intolerance, rigidity, insensitivity, coldness, indifference | slowly freezes relationships and kills feeling |"),
  C.kc("s2.check", "What does 'fire' stand for in the poem?",
    [("desire, greed and lust", ""), ("hatred", "Ice stands for hatred."), ("knowledge", "Fire is desire."), ("peace", "Fire is desire.")],
    "From what he has tasted of desire, he favours fire.")
  ,C.kc("s2.check2", "What does 'suffice' mean?",
    [("be enough", ""), ("be too little", "It means be enough."), ("be beautiful", "Be enough."), ("be slow", "Be enough.")],
    "Ice would be enough to destroy the world.")
 ]},
 {"id": "s3", "title": "Form and devices", "blocks": [
  blk("s3.thm", "theory", title="How the form supports the idea", revision=True,
    body="**Rhyme scheme:** **aba abc bcb** (fire/desire/fire; ice/twice/ice/suffice; hate/great). The rhymes link the two opposite ideas, fire and ice, and the poem swings between them.\n\n"
         "**Short last lines:** 'Is also great / And would suffice' are very short, ending the poem with a cold, quiet, chilling force.\n\n"
         "**Symbolism and irony:** simple words carry deep meaning; the casual tone ('Some say... I think I know enough...') makes the warning more powerful.\n\n"
         "**Contrast:** fire (hot, fast) against ice (cold, slow): both destroy."),
  C.kc("s3.check", "What is the rhyme scheme of Fire and Ice?",
    [("aba abc bcb", ""), ("abab cdcd e", "It is aba abc bcb."), ("aabb ccdd e", "It is aba abc bcb."), ("there is no rhyme", "It rhymes.")],
    "It links the opposite ideas.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Fire = Desire (both end in -ire!). Ice = hate (cold).**\n- **9 lines; rhyme aba abc bcb; perish twice.**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Reading the poem as only about science: it is about **human emotions**.\n2. Saying the poet favours ice: he **holds with fire**, but says ice is also great.\n3. Mixing the symbols: fire = desire, ice = hate."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="List twelve words (greed, avarice, cruelty, lust, conflict, fury, intolerance, rigidity, insensitivity, coldness, indifference, hatred). Students sort them into Fire or Ice and explain."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Which do you think harms the world more today, greed or hatred? Give one example."),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Dust of Snow:** another short Frost poem.\n- **Nelson Mandela:** how hatred is learnt and can be unlearnt."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="'Fire and Ice' is a warning about human nature. Explain in about 120 words.\n\n"
         "**Model answer:** On the surface Frost repeats a debate about whether the world will end in fire or in ice. But he uses these as symbols of human emotions. Fire stands for desire: greed, lust and ambition that spread quickly and burn everything. From his own experience of desire, he agrees the world could end in fire. Ice stands for hatred: cold, rigid indifference that slowly destroys relationships. He says that if the world had to perish twice, ice would 'suffice' too. The calm tone and short final lines make the warning chilling. The poem tells us that if we do not control our desires and our hatred, we ourselves may destroy the world."),
  blk("s5.summary", "summary", title="Summary",
    body="- Some say the world will end in fire, some in ice.\n- Fire symbolises desire; ice symbolises hatred.\n- Either is powerful enough to destroy the world; the poem warns us to control both."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- Always explain both symbols.\n- Mention the rhyme scheme and how it links the contrasting ideas.\n- Quote 'would suffice' for the power of hatred."),
  blk("s5.flash1", "flashcard", front="What do fire and ice symbolise?", back="Fire: desire (greed, lust). Ice: hatred (coldness, indifference)."),
  blk("s5.flash2", "flashcard", front="What is the rhyme scheme?", back="aba abc bcb."),
 ]},
]

TP = lambda n: ex(n, "Thinking about the Poem")
C.sa("ex1", MEAN, "There are many ideas about how the world will 'end'. Do you think the world will end some day? Have you ever thought what would happen if the sun got so hot that it 'burnt' the earth, or so cold that the earth became frozen?",
     ["Many scientists believe the world could end through heat from the sun or a frozen ice age.", "Frost uses these ideas to talk about human emotions that can destroy the world."], TP(1))
C.sa("ex2", SYMB, "For Frost, what do 'fire' and 'ice' stand for? Choose from: greed, avarice, cruelty, lust, conflict, fury, intolerance, rigidity, insensitivity, coldness, indifference, hatred.",
     ["Fire: greed, avarice, lust, conflict, fury (desire).", "Ice: cruelty, intolerance, rigidity, insensitivity, coldness, indifference, hatred."], TP(2))
C.sa("ex3", DEV, "What is the rhyme scheme of the poem? How does it help in bringing out the contrasting ideas in the poem?",
     ["The rhyme scheme is aba abc bcb.", "The rhymes tie 'fire' and 'ice' words together, so the poem swings between the two opposite ideas, both leading to destruction."], TP(3))

C.extract("ext1", SYMB, "Some say the world will end in fire,\nSome say in ice.\nFrom what I've tasted of desire\nI hold with those who favour fire.",
  [("Name the poem and the poet.", "Fire and Ice, Robert Frost."), ("What does 'fire' symbolise?", "Desire: greed and lust."),
   ("Why does the poet favour fire?", "From his own experience of desire."), ("What does 'I hold with' mean?", "I agree with."),
   ("Find the rhyming words.", "fire/desire/fire.")])
C.extract("ext2", SYMB, "But if it had to perish twice,\nI think I know enough of hate\nTo say that for destruction ice\nIs also great\nAnd would suffice.",
  [("What does 'it' refer to?", "The world."), ("What does 'ice' stand for?", "Hatred."), ("What does 'perish' mean?", "Be destroyed, die."),
   ("What does 'suffice' mean?", "Be enough."), ("What is the poet's view of hatred?", "It is powerful enough to destroy the world.")])

C.m("mcq01", MEAN, "Fire and Ice was written by:", [("Robert Frost", ""), ("John Berryman", "Frost."), ("Ogden Nash", "Frost."), ("Robin Klein", "Frost.")], "He also wrote Dust of Snow.")
C.m("mcq02", SYMB, "In the poem, 'ice' symbolises:", [("hatred", ""), ("desire", "That is fire."), ("love", "Ice is hatred."), ("wisdom", "Ice is hatred.")], "Cold, rigid, indifferent.")
C.m("mcq03", MEAN, "The poet says he holds with those who favour:", [("fire", ""), ("ice", "He favours fire, but says ice is also great."), ("water", "Fire."), ("neither", "Fire.")], "From what he has tasted of desire.")
C.m("mcq04", MEAN, "'If it had to perish twice' means:", [("if the world had to be destroyed a second time", ""), ("if the poet had to die twice", "It refers to the world."), ("if it rained twice", "The world."), ("if fire burned twice", "The world being destroyed.")], "Then ice would also do.")
C.m("mcq05", DEV, "The poem has how many lines?", [("nine", ""), ("eight", "That is Dust of Snow."), ("fourteen", "Nine."), ("twelve", "Nine.")], "It is very short.")
C.m("mcq06", DEV, "The tone of the poem is:", [("calm but warning", ""), ("joyful", "It is a warning."), ("angry", "Calm, even casual."), ("romantic", "A warning.")], "The calmness makes it chilling.")
C.m("mcq07", SYMB, "Which of these belongs with 'fire'?", [("greed", ""), ("indifference", "That is ice."), ("rigidity", "That is ice."), ("coldness", "That is ice.")], "Desire, greed and lust.")
C.m("mcq08", DEV, "The poem's main device is:", [("symbolism", ""), ("onomatopoeia", "Symbolism."), ("a refrain", "Symbolism."), ("a dialogue", "Symbolism.")], "Fire and ice are symbols.")
C.tf("tf1", SYMB, "In Fire and Ice, fire stands for hatred.", False, "Fire stands for desire; ice stands for hatred.")
C.tf("tf2", MEAN, "The poet believes ice would be enough to destroy the world.", True, "'For destruction ice is also great and would suffice.'")
C.la("la1", SYMB, "How are 'fire' and 'ice' used to talk about human emotions? Which do you think is more dangerous today?",
     ["Fire stands for desire: greed, lust and ambition that spread fast and destroy.", "Ice stands for hatred: coldness and indifference that destroy slowly.",
      "Frost says either would be enough to end the world.", "Today, greed harms nature through over-use of resources, while hatred causes wars and divides people.",
      "Both must be controlled; the poem is a warning to humanity."])

chapter = header("poem02", 11, "Fire and Ice", "Robert Frost", "poem", ["meaning_of_the_poem", "fire_and_ice_as_symbols", "poetic_devices"],
                 "CBSE 2025-26 English Language and Literature (184): First Flight poem 2. Assessed through poetry extracts (5 marks) and short answers (3 marks); can appear in long answers.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
