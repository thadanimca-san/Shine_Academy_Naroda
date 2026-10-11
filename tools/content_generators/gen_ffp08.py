"""CBSE Class 10 English, First Flight Poem 8: Fog (Carl Sandburg, 1916; public domain)."""
import sys
from lit_common import make, header, path, ex, closing

ROOT = sys.argv[1]
PATH = path("p08_fog")
C = make("ff10p08")
blk = C.blk
MEAN, MET, DEV = ["meaning_of_the_poem"], ["fog_as_a_cat"], ["form_and_devices"]
TP = lambda n: ex(n, "Thinking about the Poem")

POEM = ("*The fog comes*\n*on little cat feet.*\n\n*It sits looking*\n*over harbor and city*\n*on silent haunches*\n*and then moves on.*")

sections = [
 {"id": "s1", "title": "A cat made of fog", "blocks": [
  blk("s1.hook", "hook", title="Silent arrival, silent exit",
    body="Fog comes without a sound, settles over everything for a while, and then slips away. What does that remind you of? For **Carl Sandburg**, it is a **cat**."),
  blk("s1.inspiration", "inspiration", title="The poet", person="Carl Sandburg", years="1878–1967",
    body="**Carl Sandburg** was an American poet who won three Pulitzer Prizes. He wrote about cities, workers and the American land in plain words and **free verse**. Fog (1916) is one of the shortest and most famous poems in English.",
    future="Short poems teach precision: designers, advertisers and journalists also say a lot in few words."),
  C.socratic("s1.socratic", "Why is a cat a good comparison for fog?",
    ["Both move silently, sit still for a while and leave quietly", "Both are noisy", "Both are dangerous"], 0,
    "This is an extended metaphor."),
 ]},
 {"id": "s2", "title": "The poem and its meaning", "blocks": [
  blk("s2.poem", "theory", title="Fog", body=POEM),
  blk("s2.thm", "theory", title="What the poem says", revision=True,
    body="**Lines 1-2:** the fog comes **on little cat feet**: silently and softly, like a cat walking.\n\n"
         "**Lines 3-6:** **'It'** (the fog) sits looking over the **harbour and city** on **silent haunches**, like a cat sitting quietly on its back legs, watching. **Then it moves on**, just as a cat leaves without warning.\n\n"
         "**Extended metaphor:** the poet never says the fog is 'like' a cat; he describes the fog **as** a cat throughout the poem. Three things show this: it comes on little cat feet, it sits on silent haunches looking around, and it moves on quietly."),
  blk("s2.table", "markdown_table", title="Fog and cat", revision=True,
    body="| The fog | The cat |\n|---|---|\n| arrives silently | walks on soft, little feet |\n| hangs over harbour and city | sits on its haunches, looking around |\n| lifts and disappears | moves on without a sound |"),
  C.kc("s2.check", "What does 'It' in the third line refer to?",
    [("the fog", ""), ("the cat", "It refers to the fog, described as a cat."), ("the harbour", "The fog."), ("the city", "The fog.")],
    "The fog sits looking over the harbour and city.")
  ,C.kc("s2.check2", "Does the poet say the fog is 'like' a cat?",
    [("No; he describes the fog as a cat (extended metaphor)", ""), ("Yes, he uses 'like'", "There is no 'like' or 'as'."), ("He compares it to a dog", "A cat."), ("He does not compare it at all", "It is an extended metaphor.")],
    "A metaphor carried through the whole poem.")
 ]},
 {"id": "s3", "title": "Form and devices", "blocks": [
  blk("s3.thm", "theory", title="How the poem works", revision=True,
    body="- **Extended metaphor:** fog = cat, from the first line to the last.\n- **Free verse:** no rhyme scheme and no regular metre; the lines are short and uneven, like the fog's drifting.\n"
         "- **Imagery:** 'little cat feet', 'silent haunches' (sight and silence).\n- **Personification:** the fog 'sits looking' and 'moves on'.\n- **Two stanzas:** arrival (2 lines) and stay-and-leave (4 lines)."),
  C.kc("s3.check", "Does the poem have a rhyme scheme?",
    [("No, it is in free verse", ""), ("Yes, aabb", "It has no rhyme."), ("Yes, abab", "It has no rhyme."), ("Yes, abcb", "It has no rhyme.")],
    "Free verse has no fixed rhyme or metre.")
 ]},
 closing(C,
   "- **6 lines, 2 stanzas, free verse.**\n- **Three cat clues: little cat feet; sits on silent haunches looking; moves on.**",
   "1. Calling it a simile: there is no 'like' or 'as'; it is an **extended metaphor**.\n2. Saying the poem rhymes: it is **free verse**.\n3. Saying 'it' refers to the cat: 'it' is the **fog**.",
   "Students write a three-line poem describing rain, wind or the sun as an animal, using an extended metaphor.",
   "Which animal would you compare a thunderstorm to? Why?",
   "- **Dust of Snow and The Trees:** nature in poetry.\n- **A Tiger in the Zoo:** another cat, very different in mood.",
   "How does Sandburg use an extended metaphor in 'Fog'? Answer in about 120 words.",
   "In just six lines, Carl Sandburg describes fog as a cat without ever using 'like' or 'as'. The fog 'comes on little cat feet', arriving softly and silently as a cat walks. It 'sits looking over harbor and city on silent haunches', just as a cat sits still on its back legs, quietly watching everything. Then it 'moves on', leaving suddenly and silently as a cat does. Because the comparison runs through the whole poem, it is an extended metaphor. The short, unrhymed lines of free verse match the fog's quiet, drifting movement. The poem makes us see an ordinary weather event with fresh eyes.",
   "- Fog arrives silently, like a cat on little feet.\n- It sits over the harbour and city on silent haunches, then moves on.\n- The whole poem is one extended metaphor; it is written in free verse.",
   "- Name the device: extended metaphor, not simile.\n- Give the three cat-like actions.\n- Mention free verse and the short lines.",
   [("What is an extended metaphor?", "A metaphor continued through a whole poem, like fog described as a cat in every line."),
    ("Name three ways the fog is like a cat.", "It comes on little cat feet, sits on silent haunches looking, and then moves on.")]),
]

C.sa("ex1", MEAN, "What does Sandburg think the fog is like?", ["He thinks the fog is like a cat.", "It arrives silently, sits watching, and leaves quietly, as a cat does."], TP(1))
C.sa("ex2", MET, "How does the fog come? What does 'it' in the third line refer to? Does the poet actually say that the fog is like a cat? Find three things that tell us that it is like a cat.",
     ["It comes silently on little cat feet; 'it' refers to the fog; the poet does not say 'like a cat'.", "Cat-like: it comes on little cat feet, sits on silent haunches looking, and then moves on."], TP(2))
C.sa("ex3", DEV, "Does the poem have a rhyme scheme? Is it in free verse?",
     ["The poem has no rhyme scheme.", "Yes, it is in free verse: short, uneven lines with no regular rhyme or metre."], TP(3))

C.extract("ext1", MET, "The fog comes\non little cat feet.\n\nIt sits looking\nover harbor and city\non silent haunches\nand then moves on.",
  [("Name the poem and the poet.", "Fog, Carl Sandburg."), ("To what is the fog compared?", "A cat."), ("What does 'haunches' mean?", "The back legs and hips of an animal, on which it sits."),
   ("Name the device used throughout.", "Extended metaphor."), ("What does 'moves on' suggest?", "The fog lifts and disappears silently.")])

C.m("mcq01", MEAN, "Fog was written by:", [("Carl Sandburg", ""), ("Robert Frost", "Carl Sandburg."), ("W. B. Yeats", "Carl Sandburg."), ("Ogden Nash", "Carl Sandburg.")], "An American poet.")
C.m("mcq02", MET, "How does the fog come?", [("on little cat feet", ""), ("with a loud roar", "Silently."), ("like a storm", "Silently."), ("on big paws", "Little cat feet.")], "Softly and silently.")
C.m("mcq03", MET, "The fog sits looking over:", [("harbour and city", ""), ("mountains and rivers", "Harbour and city."), ("fields and forests", "Harbour and city."), ("deserts", "Harbour and city.")], "Like a cat watching.")
C.m("mcq04", DEV, "The main device in the poem is:", [("extended metaphor", ""), ("simile", "No 'like' or 'as'."), ("rhyme", "It does not rhyme."), ("alliteration", "Extended metaphor.")], "Fog is a cat throughout.")
C.m("mcq05", DEV, "How many lines does the poem have?", [("six", ""), ("eight", "Six."), ("nine", "Six."), ("four", "Six.")], "Two short stanzas.")
C.m("mcq06", MET, "'Silent haunches' suggests that the fog:", [("sits quietly over the place, like a cat", ""), ("makes noise", "It is silent."), ("is moving fast", "It sits still."), ("is very high", "It sits quietly.")], "A watchful, still presence.")
C.m("mcq07", DEV, "Fog is written in:", [("free verse", ""), ("rhyming couplets", "Free verse."), ("abab quatrains", "Free verse."), ("a sonnet", "Free verse.")], "No fixed rhyme or metre.")
C.tf("tf1", DEV, "The poet uses the word 'like' to compare fog to a cat.", False, "He uses an extended metaphor, not a simile.")
C.tf("tf2", MET, "At the end of the poem, the fog moves on.", True, "It leaves quietly, like a cat.")
C.sa("sa1", MET, "Why is a cat a suitable comparison for fog?",
     ["Both move silently and softly.", "Both settle and watch for a while, then leave without warning."])

C.m("mcq08", MET, "What does the fog do after sitting over the city?", [("it moves on", ""), ("it turns into rain", "It moves on."), ("it stays forever", "It moves on."), ("it roars", "It moves on silently.")], "Like a cat, it leaves quietly.")
C.m("mcq09", DEV, "The poem has how many stanzas?", [("two", ""), ("one", "Two."), ("three", "Two."), ("four", "Two.")], "Arrival; then sitting and leaving.")
C.tf("tf3", MET, "The fog arrives with a loud noise.", False, "It comes silently, on little cat feet.")

chapter = header("poem08", 17, "Fog", "Carl Sandburg", "poem", ["meaning_of_the_poem", "fog_as_a_cat", "form_and_devices"],
                 "CBSE 2025-26 English Language and Literature (184): First Flight poem 8. Assessed through poetry extracts (5 marks) and short answers (3 marks).")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
