"""CBSE Class 10 English Grammar Ch 7: Gap Filling (integrated board practice). Every item lists the right answer first."""
import sys
from grammar_common import Grammar, header

ROOT = sys.argv[1]
PATH = "app_core/content/cbse/class10/english/grammar/ch07_gap_filling"
C = Grammar("gram10ch07")
blk, kc, M = C.blk, C.check_block, C.mcq
STRAT, PREP, LINK, MIXED, PASS = ["gap_strategy"], ["prepositions"], ["connectors"], ["mixed_gaps"], ["passage_gaps"]

CLUES = ("| Look at… | It tells you… | Example |\n|---|---|---|\n| the word **before** the gap | *a/the/my* → a noun or adjective comes next; *will/can* → V1; *has/have* → V3; *is/are* → V-ing or V3 | *She has ____ (write) a poem* → **written** |\n"
         "| the word **after** the gap | a noun after the gap → you may need a determiner or adjective | *____ honest man* → **an** |\n"
         "| **time words** | the tense | *since 2010* → present perfect |\n| the **subject** | singular or plural verb | *Each of them ____* → **has** |\n"
         "| the **meaning** of the two parts | the connector | *He was ill, ____ he came* → **but / yet** |")
TIME = ("| at | on | in |\n|---|---|---|\n| clock times: *at 6 o'clock, at noon, at night* | days and dates: *on Monday, on 26 January, on my birthday* | months, years, seasons, parts of the day: *in May, in 2025, in winter, in the morning* |\n"
        "| exact points/places: *at the door, at the station, at school* | surfaces and lines: *on the table, on the wall, on the road* | enclosed spaces, cities, countries: *in the box, in Surat, in India* |\n"
        "| festivals as a period: *at Diwali* | *on time* (punctual) | *in time* (early enough) |")
CONN = ("| Purpose | Connectors | Example |\n|---|---|---|\n| addition | and, also, besides, moreover, in addition | *She sings; **moreover**, she dances.* |\n"
        "| contrast | but, yet, although/though, however, whereas, despite/in spite of (+ noun/-ing) | ***Although** it rained, we played.* ***Despite** the rain, we played.* |\n"
        "| reason | because, as, since, because of / due to (+ noun) | *We stayed in **because of** the rain.* |\n"
        "| result | so, therefore, hence, as a result, so … that | *It was **so** hot **that** we stayed in.* |\n"
        "| purpose | so that, in order to, to | *He works hard **so that** he can succeed.* |\n"
        "| condition | if, unless (= if not), provided that, in case | ***Unless** you hurry, you'll miss the bus.* |\n"
        "| time | when, while, before, after, until, as soon as | *Wait here **until** I come.* |")

sections = [
 {"id": "s1", "title": "Filling the gaps like a pro", "blocks": [
  blk("s1.hook", "hook", title="Every gap has a clue",
    body="*The Statue of Unity ____ (a) the tallest statue in ____ (b) world. It was built ____ (c) honour of Sardar Vallabhbhai Patel ____ (d) stands on an island in the Narmada.*\n\n"
         "Each blank tells you what it needs: (a) a verb that agrees with *statue* → **is**; (b) a determiner before a unique thing → **the**; (c) a preposition in a fixed phrase → **in** honour of; (d) a joining word → **and**.\n\n"
         "Gap filling is a puzzle where the sentence always hides the clue. In this chapter you'll learn to read those clues, master prepositions and connectors, and practise with many board-style passages."),
  blk("s1.inspiration", "inspiration", title="A love of the right word", person="Shashi Tharoor", years="born 1956",
    body="Shashi Tharoor worked for nearly 30 years at the United Nations, rising to Under-Secretary-General, and has written more than twenty books. He is famous for his rich vocabulary, "
         "but in his writing he always chooses the *right* word for the place: the exact preposition, the exact connector, the exact tense.\n\n"
         "He received the Sahitya Akademi Award in 2019 for *An Era of Darkness*. Choosing the right word for a gap is the same skill, used every day by writers and speakers.",
    future="Precise word choice matters in diplomacy, law, public speaking, advertising and journalism."),
  C.socratic("s1.socratic", "*He was ill; ____, he went to school.* Which word fits?",
    ["however", "therefore", "because"], 0,
    "The two ideas contrast (ill, yet went to school), so we need a contrast word: *however*. *therefore* shows a result; *because* gives a reason."),
 ]},
 {"id": "s2", "title": "The gap-filling method", "blocks": [
  blk("s2.thm", "theory", title="Four questions for every gap", revision=True,
    body="1. **What part of speech is needed?** verb, noun, determiner, preposition, connector, pronoun, adjective or adverb?\n"
         "2. **If it is a verb, what form?** Check the subject (singular/plural), the time words, and the helper before it.\n"
         "3. **What does the meaning need?** contrast, reason, result, condition, time?\n4. **Does it fit a fixed phrase?** *in spite of, according to, look forward to, depend on, interested in*.\n\n"
         "Read the **whole passage once** before filling anything, because the tense is set by the passage, not by one line. After filling, read the passage again: it should flow without a bump."),
  blk("s2.table", "markdown_table", title="Where the clues hide", revision=True, body=CLUES),
  kc("s2.check", "Fill in the blank: The scientists ____ working on the vaccine for two years now.",
    [("have been", ""), ("are", "*for two years now* needs the present perfect continuous."), ("has been", "*scientists* is plural."), ("were", "*now* points to the present.")],
    "Plural subject + *for two years now* → *have been*."),
 ]},
 {"id": "s3", "title": "Prepositions of time and place", "blocks": [
  blk("s3.time", "markdown_table", title="at, on, in", revision=True, body=TIME),
  blk("s3.thm", "theory", title="More prepositions that board papers test", revision=True,
    body="- **since / for / from**: *since 2010* (point), *for ten years* (length), *from Monday to Friday* (start–end).\n- **by / until (till)**: *Finish it **by** Friday* (deadline); *Wait **until** Friday* (continuing up to then).\n"
         "- **between / among**: *between two*, *among many*.\n- **beside / besides**: *beside* = next to; *besides* = in addition to.\n- **in / into**: *in* = position; *into* = movement inside: *He jumped **into** the pool.*\n"
         "- **across / through / along**: *across the road* (side to side), *through the forest* (inside), *along the river* (beside its length).\n"
         "- **by / with**: *written **by** Tagore* (doer), *cut **with** a knife* (instrument).\n"
         "- **Fixed phrases:** *according to, in spite of, on behalf of, in front of, instead of, in charge of, by mistake, on purpose, at present, in fact*."),
  kc("s3.check", "Fill in the blank: The train will arrive ____ 5:30 p.m. ____ Sunday.",
    [("at, on", ""), ("on, at", "Clock times take *at*; days take *on*."), ("in, on", "*in* is not used with a clock time."), ("at, in", "Days take *on*.")],
    "*at* + clock time; *on* + day."),
  kc("s3.check2", "Fill in the blank: You must submit the form ____ Monday; the office closes after that.",
    [("by", ""), ("until", "*until* means the action continues up to then; a deadline needs *by*."), ("since", "*since* is used with the perfect tenses for a starting point."), ("for", "*for* is used with a length of time.")],
    "Deadline → *by*."),
 ]},
 {"id": "s4", "title": "Connectors", "blocks": [
  blk("s4.conn", "markdown_table", title="Joining ideas", revision=True, body=CONN),
  blk("s4.thm", "theory", title="Traps with connectors", revision=True,
    body="- **although + clause; despite / in spite of + noun or -ing:** *Although it was raining…* / *Despite the rain…* / *In spite of being ill…* (✗ *Despite it was raining*; ✗ *despite of*)\n"
         "- **because + clause; because of / due to + noun:** *because he was ill* / *because of his illness*\n- **unless = if … not**: never add another *not*: ✗ *Unless you do not study, you will fail.* ✓ *Unless you study, you will fail.*\n"
         "- **so … that / such … that:** *so* + adjective/adverb; *such (a)* + noun: *It was **so** cold **that**…* / *It was **such a** cold day **that**…*\n"
         "- **Don't double conjunctions:** ✗ *Although … but*, ✗ *Because … so*.\n- **however / therefore** join two sentences, usually after a semicolon or full stop, with a comma after them."),
  kc("s4.check", "Fill in the blank: ____ his injury, he completed the marathon.",
    [("Despite", ""), ("Although", "*Although* needs a clause (subject + verb), not just a noun."), ("Because of", "The meaning is contrast, not reason."), ("Despite of", "There is no *of* after *despite*.")],
    "Contrast + noun → *Despite* (or *In spite of*)."),
  kc("s4.check2", "Fill in the blank: You will not pass ____ you work regularly.",
    [("unless", ""), ("if", "*will not pass if you work* gives the opposite meaning."), ("because", "The meaning is a condition, not a reason."), ("although", "The meaning is a condition, not contrast.")],
    "*unless* = *if … not*."),
 ]},
 {"id": "s5", "title": "Board skills: passages", "blocks": [
  blk("s5.worked", "worked_example", title="Solving a board-style passage",
    problem="Fill in the blanks:\n\n*Chandrayaan-3 (a) ____ (land) near the south pole of the moon (b) ____ 23 August 2023. India became (c) ____ first country to land there. The mission was successful (d) ____ the scientists had learnt from the earlier attempt. Since then, (e) ____ students (f) ____ (show) interest in space science.*",
    steps=["(a) A completed event with a date → simple past: **landed**.", "(b) A date → **on**.", "(c) An ordinal → **the** first.",
           "(d) Reason joining two clauses → **because** (or *as*).", "(e) Countable plural, a positive idea → **many** (or *a large number of*).",
           "(f) *Since then* + plural subject → present perfect: **have shown**."],
    answer="landed, on, the, because, many, have shown"),
  blk("s5.worked2", "worked_example", title="Choosing between close options",
    problem="Choose the right word:\n\n1. She was ____ (so / such) tired that she slept at once.\n2. We reached the station ____ (in / on) time to buy tickets.\n3. He walked ____ (along / across) the bridge to the other side.\n4. ____ (Beside / Besides) English, she speaks Japanese.",
    steps=["1. *so* + adjective (*tired*): **so**.", "2. Early enough to do something: **in** time.", "3. From one side to the other: **across**.", "4. In addition to: **Besides**."],
    answer="so; in; across; Besides"),
  kc("s5.check", "Fill in the blank: It was ____ interesting book that I finished it in one night.",
    [("such an", ""), ("so", "*so* goes before an adjective alone; with *a/an* + noun use *such*."), ("such a", "*interesting* starts with a vowel sound: *an*."), ("so an", "*so an* is not English.")],
    "*such* + *a/an* + adjective + noun + *that*."),
 ]},
 {"id": "s6", "title": "Remember, avoid, practise", "blocks": [
  blk("s6.memory", "memory_trick", title="Gap-filling memory aids",
    body="- **AT a point, ON a surface/day, IN a space/period.** \"AT 5, ON Monday, IN May.\"\n- **BY = deadline; UNTIL = keep going.**\n"
         "- **Although + sentence; Despite + thing.** (\"Despite is shy, it only takes a noun.\")\n- **Unless already has *not* inside it.**\n- **SO + adjective; SUCH + a noun.**"),
  blk("s6.mistakes", "common_mistakes", title="Common mistakes",
    body="1. ✗ *in Monday* ✓ *on Monday*; ✗ *at 2020* ✓ *in 2020*\n2. ✗ *despite of the rain* ✓ *despite the rain / in spite of the rain*\n3. ✗ *Unless you don't hurry* ✓ *Unless you hurry*\n"
         "4. ✗ *because of he was late* ✓ *because he was late*\n5. ✗ *such hot day* ✓ *such a hot day*\n6. ✗ *wait till Friday to submit* (deadline) ✓ *submit by Friday*\n"
         "7. ✗ *divide among two* ✓ *divide between two*\n8. ✗ *He entered into the room* ✓ *He entered the room*\n9. Filling a blank without reading the next sentence, which often shows the tense."),
  blk("s6.tip", "teacher_tip", title="Try this in class",
    body="Take a short news story from today's newspaper and blank out ten words: two verbs, two determiners, two prepositions, two connectors and two pronouns. "
         "Students fill them in pairs and must say which **clue** they used for each answer. Discussing the clue matters more than the answer itself."),
  blk("s6.reflection", "reflection", title="Say it in your own words",
    body="Explain the difference between *Although it rained, we went out* and *Despite the rain, we went out*. Why can't you say *Despite it rained*?"),
  blk("s6.connection", "connection", title="Where this leads",
    body="- **All grammar chapters:** gap filling tests tenses, modals, concord, determiners and reported speech together.\n- **Chapter 6, Editing:** the same rules, applied to spotting errors.\n"
         "- **Writing:** connectors (*however, therefore, moreover*) make letters and analytical paragraphs flow and earn marks for coherence."),
  blk("s6.mastery", "mastery", title="Mastery challenge",
    body="Fill in the blanks:\n\n*Yoga (a) ____ (practise) in India for thousands of years. Today people (b) ____ over the world do it (c) ____ it keeps both body and mind healthy. (d) ____ you start early in the morning, you (e) ____ (feel) fresh all day. (f) ____ its popularity, some people still think it is only for the old.*\n\n"
         "**Answer:** (a) **has been practised** (b) **all** (c) **because** (d) **If** (e) **will feel** (f) **Despite** / *In spite of*."),
  blk("s6.summary", "summary", title="Chapter summary",
    body="- Every gap has a clue: the word before, the word after, the subject, the time words, the meaning.\n- Decide the part of speech first, then the exact form.\n"
         "- *at* (point/clock), *on* (day/date/surface), *in* (month/year/space).\n- *by* = deadline; *until* = up to; *since* = from a point; *for* = a length.\n"
         "- *although* + clause; *despite / in spite of* + noun; *because* + clause; *because of* + noun; *unless* = if not.\n- Read the whole passage before and after filling."),
  blk("s6.examtips", "exam_tips", title="Board exam tips",
    body="- Write only the missing word(s) with the blank number: *(a) has been practised*.\n- If the verb is given in brackets, use that verb; don't change it for a synonym.\n"
         "- Check spelling of verb forms: *occurred, began, written, lying, studied*.\n- Never leave a blank empty."),
  blk("s6.flash1", "flashcard", front="at / on / in: ___ 26 January, ___ 2026, ___ 7 a.m.", back="*on* 26 January, *in* 2026, *at* 7 a.m."),
  blk("s6.flash2", "flashcard", front="although vs despite?", back="*although* + clause (*although it rained*); *despite* + noun/-ing (*despite the rain*)."),
  blk("s6.flash3", "flashcard", front="*Unless you don't study…*: what's wrong?", back="*unless* already means *if not*: *Unless you study…*"),
  blk("s6.flash4", "flashcard", front="so or such: ___ a lovely day / ___ lovely?", back="*such* a lovely day; *so* lovely."),
 ]},
]

FB = "Fill in the blank with the correct option: "
# ---------- Prepositions ----------
M("r01", PREP, FB + "My birthday is ____ 14 November.", [("on", ""), ("in", "Dates take *on*."), ("at", "Dates take *on*."), ("by", "*by* shows a deadline.")], "Dates → *on*.")
M("r02", PREP, FB + "The shop opens ____ 9 a.m.", [("at", ""), ("on", "Clock times take *at*."), ("in", "Clock times take *at*."), ("since", "*since* needs a perfect tense.")], "Clock time → *at*.")
M("r03", PREP, FB + "It is very cold here ____ January.", [("in", ""), ("on", "Months take *in*."), ("at", "Months take *in*."), ("by", "*by January* means a deadline.")], "Months → *in*.")
M("r04", PREP, FB + "She has been working here ____ 2018.", [("since", ""), ("for", "*2018* is a point of time."), ("from", "*from 2018* needs an end point or a different tense."), ("in", "*has been working in 2018* does not fit.")], "Point of time + perfect → *since*.")
M("r05", PREP, FB + "The mango was divided ____ the two brothers.", [("between", ""), ("among", "*among* is for more than two."), ("with", "*divided with* is not the usual phrase."), ("into", "*into* tells the parts, not the people.")], "Two people → *between*.")
M("r06", PREP, FB + "The boy jumped ____ the river to save the puppy.", [("into", ""), ("in", "Movement from outside to inside → *into*."), ("on", "You cannot jump *on* a river."), ("at", "*at* does not show movement inside.")], "Movement inside → *into*.")
M("r07", PREP, FB + "We walked ____ the river bank for an hour.", [("along", ""), ("across", "*across* means from one side to the other."), ("through", "*through* means inside something."), ("into", "*into* means entering.")], "Beside the length of something → *along*.")
M("r08", PREP, FB + "This poem was written ____ Rabindranath Tagore.", [("by", ""), ("with", "*with* names an instrument, not the writer."), ("from", "*from* shows origin, not the doer."), ("of", "*of* does not show who did the action.")], "Doer in the passive → *by*.")
M("r09", PREP, FB + "He cut the cake ____ a knife.", [("with", ""), ("by", "*by* names the doer; an instrument takes *with*."), ("from", "*from* shows origin."), ("through", "*through* means passing inside.")], "Instrument → *with*.")
M("r10", PREP, FB + "Please reach the hall ____ time; the ceremony starts at ten sharp.", [("on", ""), ("in", "*in time* means early enough for something; punctual is *on time*."), ("at", "*at time* is not a fixed phrase."), ("by", "*by time* is not a fixed phrase.")], "Punctual → *on time*.", "medium")
M("r11", PREP, FB + "She is very interested ____ classical music.", [("in", ""), ("on", "*interested in*."), ("for", "*interested in*."), ("about", "*interested in*.")], "*interested in*.")
M("r12", PREP, FB + "The success of the event depends ____ the weather.", [("on", ""), ("of", "*depend on*."), ("in", "*depend on*."), ("from", "*depend on*.")], "*depend on*.")
M("r13", PREP, FB + "____ English, he knows French and German.", [("Besides", ""), ("Beside", "*beside* means next to; *besides* means in addition to."), ("Except", "*Except* would mean he does not know English."), ("Without", "*Without* changes the meaning.")], "In addition to → *Besides*.", "medium")
M("r14", PREP, FB + "He sat ____ his friend in the class.", [("beside", ""), ("besides", "*besides* means in addition to; *beside* means next to."), ("between", "*between* needs two people/things."), ("among", "*among* needs a group.")], "Next to → *beside*.", "medium")
M("r15", PREP, FB + "____ the doctor, he will be fine in a week.", [("According to", ""), ("Because of", "The meaning is *as the doctor says*."), ("In spite of", "There is no contrast."), ("Instead of", "*Instead of the doctor* changes the meaning.")], "*According to* = as said by.")
# ---------- Connectors ----------
M("k01", LINK, FB + "____ it was raining heavily, the match continued.", [("Although", ""), ("Because", "The ideas contrast, not cause and effect."), ("Despite", "*Despite* cannot take a full clause."), ("Unless", "*Unless* shows a condition.")], "Contrast + clause → *Although*.")
M("k02", LINK, FB + "The flight was delayed ____ the fog.", [("because of", ""), ("because", "*because* needs a clause; *the fog* is a noun phrase."), ("although", "There is no contrast."), ("so", "*so* shows a result, not a cause.")], "Reason + noun → *because of*.")
M("k03", LINK, FB + "She studied hard ____ she could get a scholarship.", [("so that", ""), ("because", "*because* gives a reason; *could get* shows purpose."), ("although", "There is no contrast."), ("unless", "*unless* shows a condition.")], "Purpose → *so that*.")
M("k04", LINK, FB + "It was ____ hot that we could not go out.", [("so", ""), ("such", "*such* needs a noun: *such a hot day*."), ("too", "*too* is not followed by *that* in this pattern."), ("very", "*very* is not followed by *that*.")], "*so* + adjective + *that*.")
M("k05", LINK, FB + "The roads were wet; ____, the race was postponed.", [("therefore", ""), ("however", "A wet road causes the delay: result, not contrast."), ("although", "*although* joins clauses, not sentences after a semicolon."), ("moreover", "*moreover* adds a point; here it is a result.")], "Result → *therefore*.")
M("k06", LINK, FB + "He is rich; ____, he lives a simple life.", [("however", ""), ("therefore", "Being rich does not cause a simple life: contrast."), ("so", "*so* shows result."), ("because", "*because* shows reason.")], "Contrast between sentences → *however*.")
M("k07", LINK, FB + "Take an umbrella ____ it rains.", [("in case", ""), ("unless", "*unless it rains* gives the wrong meaning."), ("so that", "You don't take an umbrella to make it rain."), ("although", "There is no contrast.")], "Precaution → *in case*.", "medium")
M("k08", LINK, FB + "____ being tired, she helped her mother.", [("In spite of", ""), ("Although", "*Although* needs a subject + verb clause."), ("Because of", "The meaning is contrast."), ("Despite of", "There is no *of* after *despite*.")], "Contrast + -ing → *In spite of*.")
M("k09", LINK, FB + "Wait here ____ I come back.", [("until", ""), ("by", "*by* is a deadline preposition, not a time clause joiner."), ("since", "*since* needs a perfect tense in the main clause."), ("unless", "*unless* is a condition.")], "Continuing up to a time → *until*.")
M("k10", LINK, FB + "You can borrow my bike ____ you return it by evening.", [("provided that", ""), ("unless", "*unless* would reverse the condition."), ("although", "There is no contrast."), ("so that", "Returning it is a condition, not a purpose.")], "Condition → *provided that*.", "medium")
M("k11", LINK, FB + "She not only sings ____ also plays the tabla.", [("but", ""), ("and", "*not only* pairs with *but also*."), ("or", "*not only* pairs with *but also*."), ("yet", "*not only* pairs with *but also*.")], "*not only … but also*.")
M("k12", LINK, FB + "It was ____ a beautiful sight that we took many photos.", [("such", ""), ("so", "*so* cannot come before *a* + noun."), ("very", "*very a* is wrong."), ("too", "*too a* is wrong.")], "*such* + a + adjective + noun + *that*.")
# ---------- Mixed single gaps ----------
M("x01", MIXED, FB + "Neither the principal nor the teachers ____ aware of the change.", [("were", ""), ("was", "Nearer subject *teachers* is plural."), ("is", "Plural nearer subject, and the context is past."), ("has", "*has aware* is wrong.")], "*neither … nor* → nearer subject.")
M("x02", MIXED, FB + "If I ____ you, I would accept the offer.", [("were", ""), ("am", "Imagined situations take *were*."), ("was", "In formal English, *If I were you* is the fixed form."), ("will be", "No *will* in the *if* clause.")], "Imaginary condition → *If I were you*.", "medium")
M("x03", MIXED, FB + "She ____ have reached home by now; she left two hours ago.", [("must", ""), ("can't", "The evidence suggests she has reached."), ("needn't", "*needn't* is about necessity."), ("ought", "*ought* needs *to*.")], "Deduction → *must have*.")
M("x04", MIXED, FB + "____ of the two candidates was selected; both were rejected.", [("Neither", ""), ("Either", "Both were rejected, so *neither*."), ("Both", "*Both … was* is wrong, and both were rejected."), ("Each", "*Each* means both were selected.")], "None of two → *Neither*.")
M("x05", MIXED, FB + "He asked me ____ I could lend him my notes.", [("whether", ""), ("that", "A reported yes/no question takes *if/whether*."), ("what", "*what* changes the meaning."), ("do", "Reported questions do not use *do*.")], "Reported yes/no → *whether/if*.")
M("x06", MIXED, FB + "I have ____ money left; I cannot buy the book.", [("little", ""), ("a little", "*a little* is positive; you cannot buy the book."), ("few", "*money* is uncountable."), ("many", "*money* is uncountable.")], "Uncountable + almost none → *little*.")
M("x07", MIXED, FB + "The doctor advised him ____ sweets.", [("not to eat", ""), ("don't eat", "*don't* → *not to* in reported speech."), ("to not eating", "*not to* + V1."), ("not eating", "*advised him* + *not to* + V1.")], "Advice → *advised + object + not to + V1*.")
M("x08", MIXED, FB + "By the time the police arrived, the robbers ____.", [("had escaped", ""), ("escaped", "The escape happened first: past perfect."), ("have escaped", "The story is in the past."), ("were escaping", "They were already gone.")], "Earlier past action → past perfect.")
M("x09", MIXED, FB + "The number of mobile users ____ increasing rapidly.", [("is", ""), ("are", "*The number of* → singular."), ("were", "*The number* is singular."), ("have", "*have increasing* is wrong.")], "*The number of* → singular.")
M("x10", MIXED, FB + "____ Ganga and the Yamuna meet at Prayagraj.", [("The", ""), ("A", "Rivers take *the*."), ("An", "Rivers take *the*."), ("No article", "Rivers take *the*.")], "Rivers → *the*.")
# ---------- Passages ----------
P1 = ("Read the passage and choose the correct option for the blank.\n\n*Dr Verghese Kurien (a) ____ known as the Father of the White Revolution. He came to Anand (b) ____ 1949 and helped farmers set up (c) ____ cooperative. (d) ____ his efforts, India became the largest producer of milk (e) ____ the world.*\n\n")
M("p01", PASS, P1 + "Blank (a):", [("is", ""), ("are", "*Dr Verghese Kurien* is one person."), ("has", "*has known* changes the meaning."), ("were", "One person, and his title is still used today.")], "He is still known by this title → *is*.", "medium")
M("p02", PASS, P1 + "Blank (b):", [("in", ""), ("on", "Years take *in*."), ("at", "Years take *in*."), ("since", "*came … since 1949* is wrong with the simple past.")], "Years → *in*.", "medium")
M("p03", PASS, P1 + "Blank (c):", [("a", ""), ("an", "*cooperative* begins with a consonant sound."), ("the", "First mention."), ("much", "*cooperative* is countable.")], "First mention + consonant sound → *a*.", "medium")
M("p04", PASS, P1 + "Blank (d):", [("Because of", ""), ("Because", "*his efforts* is a noun phrase: *because of*."), ("Despite", "The efforts caused the result; no contrast."), ("Although", "*Although* needs a clause and shows contrast.")], "Reason + noun → *Because of*.", "medium")
M("p05", PASS, P1 + "Blank (e):", [("in", ""), ("of", "The usual phrase is *the largest … in the world*."), ("on", "*in the world* is the fixed phrase."), ("at", "*in the world*.")], "*in the world*.", "medium")
P2 = ("Read the passage and choose the correct option for the blank.\n\n*Plastic bags (a) ____ banned in many states. (b) ____ they are cheap and useful, they harm animals and block drains. If everyone (c) ____ a cloth bag, we (d) ____ reduce plastic waste greatly. We (e) ____ wait for the government to act; we can start today.*\n\n")
M("p06", PASS, P2 + "Blank (a):", [("have been", ""), ("has been", "*Plastic bags* is plural."), ("was", "Plural subject."), ("are being", "The ban is already in place; *have been banned* fits best.")], "Plural + result now → *have been banned*.", "hard")
M("p07", PASS, P2 + "Blank (b):", [("Although", ""), ("Because", "The two ideas contrast."), ("Despite", "*Despite* cannot take a clause."), ("Unless", "*Unless* is a condition.")], "Contrast + clause → *Although*.", "medium")
M("p08", PASS, P2 + "Blank (c):", [("carries", ""), ("carry", "*everyone* is singular."), ("will carry", "No *will* in an *if* clause."), ("carrying", "A finite verb is needed.")], "*If* + present; *everyone* → *carries*.", "medium")
M("p09", PASS, P2 + "Blank (d):", [("can", ""), ("must", "The idea is possibility, not obligation."), ("needn't", "*needn't* is about necessity."), ("ought", "*ought* needs *to*.")], "Possibility/ability → *can*.", "medium")
M("p10", PASS, P2 + "Blank (e):", [("needn't", ""), ("mustn't", "*mustn't* means forbidden; the meaning is *not necessary*."), ("can't", "*can't* means unable."), ("should", "*should wait* contradicts *we can start today*.")], "Not necessary → *needn't*.", "hard")
P3 = ("Read the passage and choose the correct option for the blank.\n\n*Mary Kom (a) ____ born in a poor farming family in Manipur. She (b) ____ to box secretly (c) ____ her father did not approve. Later, she won (d) ____ Olympic bronze medal, and she (e) ____ an inspiration ever since.*\n\n")
M("p11", PASS, P3 + "Blank (a):", [("was", ""), ("is", "Her birth is a past event."), ("has", "*has born* is wrong."), ("were", "*Mary Kom* is singular.")], "*was born*.", "medium")
M("p12", PASS, P3 + "Blank (b):", [("learnt", ""), ("learns", "The story is past."), ("has learnt", "A past story uses the simple past."), ("had learn", "*had* + V3 would be *had learnt*.")], "Past story → *learnt*.", "medium")
M("p13", PASS, P3 + "Blank (c):", [("because", ""), ("although", "Boxing secretly was the result of his disapproval: reason."), ("so", "*so* would reverse cause and effect."), ("despite", "*despite* cannot take a clause.")], "Reason + clause → *because*.", "medium")
M("p14", PASS, P3 + "Blank (d):", [("an", ""), ("a", "*Olympic* begins with a vowel sound."), ("the", "First mention of one of many medals."), ("some", "*medal* is singular countable.")], "Vowel sound → *an*.", "medium")
M("p15", PASS, P3 + "Blank (e):", [("has been", ""), ("was", "*ever since* links the past to now: present perfect."), ("is", "*ever since* needs the present perfect."), ("had been", "The time is up to now, not up to a past moment.")], "*ever since* → present perfect.", "hard")
# ---------- True / false ----------
C.tf("t01", PREP, "We say *in Monday*.", False, "Days take *on*: *on Monday*.")
C.tf("t02", LINK, "*Despite* can be followed by a noun or an -ing form.", True, "*Despite the rain*, *despite being tired*.")
C.tf("t03", LINK, "*Unless* means *if … not*.", True, "*Unless you hurry* = *If you do not hurry*.")
C.tf("t04", PREP, "*by Friday* shows a deadline.", True, "*Submit it by Friday* = not later than Friday.")
C.tf("t05", LINK, "*Because of* is followed by a full clause.", False, "*because of* + noun: *because of the rain*; *because* + clause: *because it rained*.")
C.tf("t06", STRAT, "You should read the whole passage before filling the blanks.", True, "Later sentences often show the tense and meaning.")
# ---------- Assertion-reason ----------
C.ar("ar1", LINK, "*Despite it was late, we continued* is incorrect.", "*Despite* is followed by a noun or -ing form, not a clause.", 0,
     "R explains A: use *Although it was late* or *Despite the late hour*.", "*Despite* + clause is wrong.", "*despite* takes a noun/-ing.")
C.ar("ar2", PREP, "*The meeting is on 5 June at 10 a.m.* is correct.", "Dates take *on* and clock times take *at*.", 0,
     "R explains A.", "both prepositions are right.", "*on* + date, *at* + time.")
C.ar("ar3", LINK, "*Unless you don't practise, you won't improve* is correct.", "*Unless* already contains a negative meaning.", 3,
     "A is false (*Unless you practise…*); R is true and shows why.", "the double negative is wrong.", "*unless* = *if not*.")
C.ar("ar4", PREP, "*He was born in 2010* is correct.", "Years take *on*.", 2,
     "A is true; R is false: years take *in*.", "*in* + year is right.", "years take *in*, not *on*.")

chapter = header(7, "Gap Filling", ["gap_strategy", "prepositions", "connectors", "mixed_gaps", "passage_gaps"],
                 "Integrated board practice for the CBSE 2025-26 English Language and Literature (184) Section B Grammar: gap filling across tenses, modals, concord, determiners, reported speech, prepositions and connectors.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
