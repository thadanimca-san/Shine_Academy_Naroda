"""CBSE Class 10 English Grammar Ch 1: Tenses. Every item lists the right answer first (see grammar_common)."""
import sys
from grammar_common import Grammar, header

ROOT = sys.argv[1]
PATH = "app_core/content/cbse/class10/english/grammar/ch01_tenses"
C = Grammar("gram10ch01")
blk, kc = C.blk, C.check_block
FORMS, PRES, PAST, FUT, SEQ = ["tense_forms"], ["present_tenses"], ["past_tenses"], ["future_forms"], ["sequence_of_tenses"]

MAP = ("| Time ↓ / Aspect → | Simple | Continuous | Perfect | Perfect continuous |\n|---|---|---|---|---|\n"
       "| **Present** | V1 / V1+s: *She writes.* | am/is/are + V-ing: *She is writing.* | has/have + V3: *She has written.* | has/have been + V-ing: *She has been writing.* |\n"
       "| **Past** | V2: *She wrote.* | was/were + V-ing: *She was writing.* | had + V3: *She had written.* | had been + V-ing: *She had been writing.* |\n"
       "| **Future** | will + V1: *She will write.* | will be + V-ing: *She will be writing.* | will have + V3: *She will have written.* | will have been + V-ing: *She will have been writing.* |")
SIGNALS = ("| Signal words | Usual tense | Example |\n|---|---|---|\n"
           "| always, usually, often, every day, never (habit) | simple present | *He **walks** to school every day.* |\n"
           "| now, at present, at the moment, Look!, Listen! | present continuous | *Look! The baby **is sleeping**.* |\n"
           "| just, already, yet, ever, so far, recently, since, for (up to now) | present perfect | *I **have** just **finished** my homework.* |\n"
           "| since / for + an action still going on | present perfect continuous | *It **has been raining** since morning.* |\n"
           "| yesterday, last week, ago, in 2015, when (finished time) | simple past | *We **visited** Delhi two years ago.* |\n"
           "| while, when (something interrupted) | past continuous | *I **was reading** when the lights went out.* |\n"
           "| before, after, by the time, already (earlier past) | past perfect | *The train **had left** before we reached.* |\n"
           "| tomorrow, next week, soon, in 2030 | will / going to | *The results **will be** out tomorrow.* |\n"
           "| by (a future time), by the time | future perfect | *By 2030 they **will have built** the bridge.* |")

sections = [
 {"id": "s1", "title": "Why time matters in English", "blocks": [
  blk("s1.hook", "hook", title="One verb, many times",
    body="Read these three sentences:\n\n- *Riya **plays** the sitar.*\n- *Riya **is playing** the sitar.*\n- *Riya **has played** the sitar.*\n\n"
         "The same verb tells three different stories. The first says it is her habit, the second says it is happening right now, and the third says it is done and the result is with us. "
         "That small change in the verb is called **tense**, and it is the single most tested grammar topic in the CBSE board paper. Gap filling, editing and reported speech all depend on it.\n\n"
         "In this chapter you will learn all twelve tenses through one simple map, the signal words that give the answer away, and the traps examiners set again and again."),
  blk("s1.inspiration", "inspiration", title="Writing that anyone can read", person="Ruskin Bond", years="born 1934",
    body="Ruskin Bond has written more than 500 stories, essays and novels from his home in the hills of Mussoorie. His sentences are short and clear, and his verbs always tell you exactly *when* something happens: "
         "a boy **was walking** through the forest, the rain **had stopped**, the leopard **will come back** tonight.\n\n"
         "He was awarded the Sahitya Akademi Award in 1992 and the Padma Bhushan in 2014. His secret is not difficult words; it is correct, simple grammar used with care.",
    future="Strong English grammar opens doors to journalism, law, teaching, content writing, civil services, international business and every competitive exam."),
  C.socratic("s1.socratic", "Which sentence means that the keys are still missing now?",
    ["I have lost my keys.", "I lost my keys yesterday.", "I was losing my keys."], 0,
    "*Have lost* (present perfect) connects a past action to the present: the keys are still lost. *Lost yesterday* only tells us about the past; they may have been found."),
 ]},
 {"id": "s2", "title": "The tense map: 3 times × 4 aspects", "blocks": [
  blk("s2.thm", "theory", title="Time and aspect", revision=True,
    body="Every tense answers two questions:\n\n1. **When?** Present, past or future: this is the **time**.\n2. **How?** This is the **aspect**:\n"
         "   - **Simple:** the plain fact or habit.\n   - **Continuous (progressive):** in progress, unfinished: *be* + V-ing.\n"
         "   - **Perfect:** completed before a point of time: *have* + V3.\n   - **Perfect continuous:** started earlier and still going on, or just stopped: *have been* + V-ing.\n\n"
         "3 times × 4 aspects = **12 tenses**. Learn the helping verbs in the map below, and every tense becomes a simple formula.\n\n"
         "**Verb forms:** V1 = base (*go*), V2 = past (*went*), V3 = past participle (*gone*), V-ing = present participle (*going*)."),
  blk("s2.map", "markdown_table", title="The twelve tenses", revision=True, body=MAP),
  kc("s2.check", "Which tense is used in: *They had been waiting for an hour.*?",
    [("Past perfect continuous", ""), ("Past perfect", "Past perfect is *had* + V3 (*had waited*); here we have *had been* + V-ing."),
     ("Present perfect continuous", "That would be *have been waiting*; *had* shows the past."), ("Past continuous", "That would be *were waiting*, without *had been*.")],
    "*had been* + V-ing = past perfect continuous: the waiting went on for a time before a past moment."),
 ]},
 {"id": "s3", "title": "The present tenses", "blocks": [
  blk("s3.thm", "theory", title="Four ways to talk about now", revision=True,
    body="**1. Simple present (V1 / V1+s or es)**\n- Habits and routines: *She **reads** the newspaper every morning.*\n- Universal truths: *Water **boils** at 100 °C.* *The sun **rises** in the east.*\n"
         "- Timetables and fixed schedules: *The train **leaves** at 6 p.m. tomorrow.*\n- Headlines, quotations and commentary: *Kohli **hits** a six!*\n"
         "- Rule: add **-s/-es** with *he, she, it* and singular nouns: *he goes, she watches, it flies*. Negatives and questions use *do/does* + V1: *She **does not like** tea.* (never *does not likes*)\n\n"
         "**2. Present continuous (am/is/are + V-ing)**\n- Action happening now: *The children **are playing** outside.*\n- Temporary situations: *I **am staying** with my uncle this month.*\n"
         "- Fixed future plans: *We **are meeting** the principal tomorrow.*\n\n"
         "**3. Present perfect (has/have + V3)**\n- Past action with a result now: *She **has broken** her arm.* (it is still broken)\n- Experience up to now: *Have you ever **seen** snow?*\n"
         "- With *just, already, yet, ever, never, so far, recently, since, for*.\n- ✗ Never with a finished time: *I have seen him **yesterday*** is wrong. Say *I **saw** him yesterday.*\n\n"
         "**4. Present perfect continuous (has/have been + V-ing)**\n- Action that began in the past and is still going on: *He **has been studying** since 7 o'clock.* *They **have been living** here for ten years.*\n\n"
         "**Stative verbs** (feelings, thoughts, senses, possession: *know, believe, like, love, want, belong, own, seem, understand*) are not normally used in the continuous: "
         "*I **know** the answer*, not *I am knowing the answer*."),
  blk("s3.sincefor", "markdown_table", title="Since or for?", revision=True,
    body="| **since** + a point of time | **for** + a length of time |\n|---|---|\n| since Monday, since 2019, since morning, since I was a child | for two hours, for three days, for a long time, for ages |\n"
         "| *She has worked here **since 2019**.* | *She has worked here **for six years**.* |"),
  kc("s3.check", "Fill in the blank: My grandmother ____ yoga every morning for the last twenty years.",
    [("has been doing", ""), ("is doing", "*is doing* tells only about now; *for the last twenty years* needs an action that started long ago and still continues."),
     ("does", "The simple present gives the habit, but *for the last twenty years* asks for the perfect continuous."),
     ("did", "*did* puts the action fully in the past; she still does yoga.")],
    "*for the last twenty years* + an action still going on = present perfect continuous: *has been doing*."),
  kc("s3.check2", "Choose the correct sentence.",
    [("I finished the project last night.", ""), ("I have finished the project last night.", "*last night* is a finished time, so the present perfect cannot be used."),
     ("I have finish the project last night.", "After *have* we need V3 (*finished*), and *last night* still needs the simple past."),
     ("I had finishing the project last night.", "*had* is never followed by V-ing; and one past action does not need the past perfect.")],
    "A definite past time (*last night, yesterday, ago*) always takes the simple past."),
 ]},
 {"id": "s4", "title": "The past tenses", "blocks": [
  blk("s4.thm", "theory", title="Telling a story in the past", revision=True,
    body="**1. Simple past (V2)**\n- A completed action at a definite time: *Gandhiji **returned** to India in 1915.*\n- A series of actions in a story: *He **opened** the door, **looked** around and **left**.*\n"
         "- Negatives and questions use *did* + **V1**: *He **did not go**.* *Did she **call**?* (✗ *did not went*, ✗ *did she called*)\n\n"
         "**2. Past continuous (was/were + V-ing)**\n- An action in progress at a past moment: *At 8 p.m. we **were having** dinner.*\n"
         "- A longer action interrupted by a shorter one: *I **was crossing** the road **when** I **saw** the accident.* (long action = past continuous; short action = simple past)\n"
         "- Two actions going on together: ***While** mother **was cooking**, father **was reading**.*\n\n"
         "**3. Past perfect (had + V3)**: the *earlier* of two past actions.\n- *The patient **had died** before the doctor **arrived**.* (first died, then arrived)\n"
         "- *When we reached the station, the train **had** already **left**.*\n- Only use it when there are two past actions and you need to show which came first.\n\n"
         "**4. Past perfect continuous (had been + V-ing)**: an action that went on for some time before another past action.\n- *She **had been waiting** for two hours when the bus finally **came**.*"),
  blk("s4.timeline", "markdown_table", title="Which happened first?", revision=True,
    body="| Sentence | First action (earlier) | Second action (later) |\n|---|---|---|\n| *The match **had started** when we **reached** the stadium.* | match started (past perfect) | we reached (simple past) |\n"
         "| *After he **had finished** his work, he **went** home.* | finished work | went home |\n| *I **was sleeping** when the phone **rang**.* | sleeping (going on) | phone rang (interrupted) |"),
  kc("s4.check", "Fill in the blank: When the firemen arrived, the house ____ to ashes.",
    [("had burnt", ""), ("burnt", "Both actions would then seem to happen together; the burning finished *before* the firemen came, so use the past perfect."),
     ("has burnt", "*has burnt* is present perfect; the story is in the past."), ("was burning", "This means it was still burning; *to ashes* shows it was already completely burnt.")],
    "The burning was completed before the firemen arrived: the earlier past action takes the past perfect, *had burnt*."),
  kc("s4.check2", "Fill in the blank: She ____ a novel when the guests knocked at the door.",
    [("was reading", ""), ("read", "The reading was going on and was interrupted, so it needs the continuous: *was reading*."),
     ("had read", "*had read* means she had finished before they knocked; *when ... knocked* shows an interrupted action."),
     ("is reading", "The knock is in the past (*knocked*), so the reading must be in the past too.")],
    "A longer action in progress (*was reading*) is interrupted by a short one (*knocked*)."),
 ]},
 {"id": "s5", "title": "Talking about the future", "blocks": [
  blk("s5.thm", "theory", title="Will, going to and more", revision=True,
    body="English has no single future tense; it has several ways to talk about the future.\n\n"
         "- **will + V1**: decisions made now, predictions, promises: *I **will help** you with the bags.* *It **will rain** tonight, I think.*\n"
         "- **be going to + V1**: plans already made, and predictions from present evidence: *We **are going to buy** a car.* *Look at those clouds! It **is going to rain**.*\n"
         "- **Present continuous**: fixed arrangements: *I **am flying** to Mumbai on Friday.*\n- **Simple present**: timetables: *The exam **begins** on 15 February.*\n"
         "- **Future continuous (will be + V-ing)**: in progress at a future time: *This time tomorrow I **will be travelling** to Shimla.*\n"
         "- **Future perfect (will have + V3)**: completed before a future time: *By next March we **will have finished** the syllabus.*\n"
         "- **Future perfect continuous (will have been + V-ing)**: duration up to a future time: *By June she **will have been teaching** for 25 years.*\n\n"
         "**Golden rule for time clauses:** after *when, as soon as, before, after, until, if, unless*, use the **present**, not *will*:\n"
         "*I will call you **when I reach** home.* (✗ *when I will reach*) *If it **rains**, the match will be cancelled.* (✗ *If it will rain*)"),
  kc("s5.check", "Fill in the blank: I will give him your message as soon as he ____.",
    [("arrives", ""), ("will arrive", "After *as soon as* (a time clause) we use the present, not *will*."),
     ("arrived", "The main clause is in the future (*will give*), so the time clause takes the simple present."), ("has been arriving", "Arriving is a single short action, not one that continues.")],
    "Time clauses (*as soon as, when, before, until, if*) take the simple present even when the meaning is future."),
  kc("s5.check2", "Fill in the blank: By the time you get there, the meeting ____.",
    [("will have ended", ""), ("will end", "*will end* does not show that the ending happens *before* you get there."),
     ("ended", "*By the time you get there* is in the future; *ended* is past."), ("has ended", "Present perfect cannot point to a future time.")],
    "*By the time* + a future moment → future perfect: completed before that moment."),
 ]},
 {"id": "s6", "title": "Board skills: signal words, sequence of tenses and traps", "blocks": [
  blk("s6.signals", "markdown_table", title="Signal words give the answer away", revision=True, body=SIGNALS),
  blk("s6.seq", "theory", title="Sequence of tenses", revision=True,
    body="When the main verb is in the **past**, the verb in the joined (subordinate) clause normally goes into a past form too:\n\n"
         "- *He **said** that he **was** tired.* (not *is*)\n- *I **thought** you **would** come.* (not *will*)\n- *She **knew** that the bus **had left**.*\n\n"
         "**Exceptions:** a universal truth or habitual fact stays in the present: *The teacher **said** that the earth **revolves** round the sun.*\n\n"
         "A clause with *than* or *as* can take any tense the meaning needs: *She **liked** you more than she **likes** me.*\n\n"
         "This rule is the heart of **reported speech** (Chapter 4), so master it here."),
  blk("s6.worked", "worked_example", title="Solving a gap-filling passage, step by step",
    problem="Fill in the blanks with the correct form of the verbs given in brackets:\n\n"
            "Last Sunday our class (a) ____ (visit) the science museum. When we (b) ____ (reach), the guide (c) ____ (already, start) the tour, so we (d) ____ (join) the group quietly. "
            "Since then I (e) ____ (read) three books on space, and next year I (f) ____ (take) part in the science olympiad.",
    steps=["(a) *Last Sunday* is a finished time → simple past: **visited**.",
           "(b) A completed short action in the past story → simple past: **reached**.",
           "(c) The tour started *before* we reached, and *already* confirms it → past perfect: **had already started**.",
           "(d) The next action in the story → simple past: **joined**.",
           "(e) *Since then* links the past to now → present perfect: **have read**.",
           "(f) *next year* is the future → **will take** (or *am going to take*, a plan)."],
    answer="visited, reached, had already started, joined, have read, will take"),
  blk("s6.worked2", "worked_example", title="Editing: find the error, write the correction",
    problem="Each line has one error. Write the incorrect word and the correction.\n\n1. Yesterday I have met my old teacher in the market.\n2. She did not knew that the shop was closed.\n"
            "3. The earth moved round the sun, our teacher explained.\n4. I am knowing him since my childhood.",
    steps=["Line 1: *Yesterday* is a finished time; the present perfect cannot be used. **have met → met**.",
           "Line 2: After *did* we always use V1. **knew → know**.",
           "Line 3: A universal truth stays in the simple present. **moved → moves**.",
           "Line 4: *know* is a stative verb, and *since my childhood* needs the present perfect. **am knowing → have known**."],
    answer="have met → met; knew → know; moved → moves; am knowing → have known"),
  kc("s6.check", "Find the error: *The guests have arrived an hour ago.*",
    [("have arrived → arrived", ""), ("arrived → arrive", "*have arrive* is not a correct form; and the real problem is *ago*."),
     ("an → a", "*an hour* is correct, because *hour* begins with a vowel sound."), ("ago → before", "*an hour ago* is correct; the verb is the problem.")],
    "*ago* marks a finished past time, so the simple past is needed: *The guests arrived an hour ago.*"),
 ]},
 {"id": "s7", "title": "Remember, avoid, practise", "blocks": [
  blk("s7.memory", "memory_trick", title="Three keys to every tense",
    body="- **Be + ing = going on** (am/is/are/was/were/will be + V-ing).\n- **Have + V3 = done** (has/have/had/will have + V3).\n- **Have been + ing = going on for a while** (since / for).\n\n"
         "**Did, does, do → always V1 after them.** \"Did went\" is a crime!\n\n**Two past actions?** The one that happened **first** gets **had**.\n\n**After when, if, as soon as → no *will*.**"),
  blk("s7.mistakes", "common_mistakes", title="The ten traps examiners love",
    body="1. Present perfect with a past time: ✗ *I have seen it yesterday.* ✓ *I saw it yesterday.*\n2. V2 after *did*: ✗ *He did not came.* ✓ *He did not come.*\n"
         "3. Missing -s: ✗ *She go to school.* ✓ *She goes to school.*\n4. Stative verbs in the continuous: ✗ *I am understanding.* ✓ *I understand.*\n"
         "5. *Since* with a length of time: ✗ *since two years* ✓ *for two years*\n6. *Will* in a time clause: ✗ *when he will come* ✓ *when he comes*\n"
         "7. Wrong sequence: ✗ *He said that he is ill.* ✓ *He said that he was ill.*\n8. Changing a universal truth: ✗ *She said the sun rose in the east.* ✓ *... rises in the east.*\n"
         "9. Wrong V3: ✗ *has wrote, had went, have drank* ✓ *has written, had gone, have drunk*\n10. Simple present for an action going on now: ✗ *Look! It rains.* ✓ *Look! It is raining.*"),
  blk("s7.tip", "teacher_tip", title="Try this in class",
    body="Make a \"tense ladder\" on the board: one sentence, *Ravi eats lunch*, changed into all twelve tenses by the class, one student per step. "
         "Then play **Signal-word cricket**: the teacher calls out a signal word (*since, yesterday, Look!, by next year*), and each team must make a correct sentence in the right tense to score a run."),
  blk("s7.reflection", "reflection", title="Say it in your own words",
    body="Explain to a friend the difference between *I have lived in Ahmedabad for ten years* and *I lived in Ahmedabad for ten years*. Who still lives there?"),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 4, Reported Speech:** the sequence of tenses is used in every reported sentence.\n- **Chapter 6–7, Editing and Gap Filling:** most board errors are tense errors.\n"
         "- **Writing (letters and analytical paragraphs):** a data paragraph uses the past and present perfect; a letter of complaint uses the present perfect for problems still going on."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="Fill in the blanks with the correct form of the verbs in brackets:\n\n"
         "The bell (a) ____ (ring) just now, but the teacher (b) ____ (not come) yet. The students (c) ____ (talk) loudly. Rohan (d) ____ (sit) quietly in the corner because he (e) ____ (forget) his homework at home. "
         "He hopes the teacher (f) ____ (not check) it today.\n\n"
         "**Answer:** (a) **rang** (*just now* = a moment in the past) (b) **has not come** (*yet* → present perfect) (c) **are talking** (going on now) (d) **is sitting** (e) **has forgotten** / **forgot** (f) **will not check**."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- 3 times × 4 aspects = 12 tenses; learn their helping verbs from the map.\n- Simple = fact/habit; continuous = going on; perfect = completed; perfect continuous = continuing for a period.\n"
         "- Present perfect links the past to now; never use it with a finished past time.\n- Past perfect marks the earlier of two past actions.\n"
         "- In time and *if* clauses, use the present for the future.\n- After a past reporting verb, shift the tense back, except for universal truths.\n- *do/does/did* are always followed by V1."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- Read the **whole** sentence or passage before filling a blank; the signal word may come later.\n- In editing, check the verb first: tense, -s agreement, and V1 after *did*.\n"
         "- Write only the required answer in the format asked (for editing: *incorrect word → correction*).\n- Spelling counts: *occurred, stopped, written, began, lying*."),
  blk("s7.flash1", "flashcard", front="Formula of the present perfect continuous?", back="has/have + been + V-ing: *She has been working since morning.*"),
  blk("s7.flash2", "flashcard", front="Which tense for the earlier of two past actions?", back="Past perfect (had + V3): *The film had started before we arrived.*"),
  blk("s7.flash3", "flashcard", front="Since or for: ___ 2020, ___ five years?", back="since 2020 (point of time), for five years (length of time)."),
  blk("s7.flash4", "flashcard", front="Correct: *If it will rain, we will stay home*?", back="*If it rains, we will stay home.* No *will* in an *if* or time clause."),
 ]},
]

M = C.mcq
FB = "Fill in the blank with the correct option: "
# ---------- Gap filling: present ----------
M("g01", PRES, FB + "Water ____ at 0 °C.", [("freezes", ""), ("is freezing", "A scientific fact is always in the simple present, not the continuous."), ("froze", "Facts do not belong only to the past."), ("freeze", "*Water* is singular: add -s.")], "Universal truths take the simple present: *Water freezes at 0 °C.*")
M("g02", PRES, FB + "Listen! Someone ____ at the door.", [("is knocking", ""), ("knocks", "*Listen!* shows the action is happening right now: use the continuous."), ("knocked", "*Listen!* points to now, not the past."), ("has knocked", "The knocking is still going on as we listen.")], "*Listen!* / *Look!* signal an action in progress: present continuous.")
M("g03", PRES, FB + "My father ____ his car every Sunday.", [("washes", ""), ("wash", "*My father* is third person singular: *washes*."), ("is washing", "*every Sunday* shows a habit, so the simple present is used."), ("has washed", "A regular habit is not expressed with the present perfect.")], "A habit (*every Sunday*) + singular subject → *washes*.")
M("g04", PRES, FB + "I ____ this film three times already.", [("have seen", ""), ("saw", "*already* and *three times* (experience up to now) call for the present perfect."), ("have saw", "After *have* use V3: *seen*, not *saw*."), ("am seeing", "*see* in this sense is not used in the continuous.")], "*already* + experience up to now → present perfect: *have seen*.")
M("g05", PRES, FB + "She ____ in this school since 2018.", [("has been teaching", ""), ("is teaching", "*since 2018* needs a perfect tense, not the present continuous."), ("teaches", "*since* + a point of time takes the present perfect (continuous)."), ("taught", "She still teaches here; the simple past would mean she stopped.")], "*since 2018* + still going on → present perfect continuous.")
M("g06", PRES, FB + "The Ganga ____ into the Bay of Bengal.", [("flows", ""), ("is flowing", "A permanent geographical fact takes the simple present."), ("flowed", "The river still flows there; it is a permanent fact."), ("flow", "*The Ganga* is singular: *flows*.")], "Permanent facts → simple present.")
M("g07", PRES, FB + "We ____ for the bus for forty minutes, and it still hasn't come.", [("have been waiting", ""), ("are waiting", "*for forty minutes* (a length of time up to now) needs the perfect continuous."), ("waited", "*it still hasn't come* shows the waiting continues now."), ("wait", "The simple present does not show a period of time continuing up to now.")], "*for* + a period up to now, still continuing → present perfect continuous.")
M("g08", PRES, FB + "Do you ____ where Meena lives?", [("know", ""), ("knows", "After *do/does* we use V1 with no -s."), ("knew", "After *do* use V1, not V2."), ("knowing", "After *do* use V1, not the -ing form.")], "*do/does/did* + V1.")
M("g09", PRES, FB + "The train to Ahmedabad ____ at 6:45 tomorrow morning.", [("leaves", ""), ("left", "*tomorrow* is in the future."), ("has left", "*tomorrow* is future; the present perfect cannot refer to it."), ("had left", "Past perfect cannot point to tomorrow.")], "Timetables take the simple present even for the future.")
M("g10", PRES, FB + "This soup ____ delicious.", [("tastes", ""), ("is tasting", "*taste* meaning \"has a flavour\" is a stative verb, so no continuous."), ("taste", "*This soup* is singular: *tastes*."), ("has been tasting", "A stative meaning is not used in the continuous.")], "Stative use of *taste* → simple present: *tastes*.")
M("g11", PRES, FB + "Have you finished your homework ____?", [("yet", ""), ("already", "In questions and negatives about something expected, we normally use *yet*."), ("since", "*since* needs a point of time after it."), ("ago", "*ago* goes with the simple past, not the present perfect.")], "*yet* is used in questions and negatives with the present perfect.")
M("g12", PRES, FB + "Neither of the boys ____ the answer.", [("knows", ""), ("know", "*Neither of* + plural noun takes a singular verb in formal English."), ("are knowing", "*know* is stative, and the subject is singular."), ("have known", "The subject *neither* is singular, so *have* is wrong.")], "*Neither of the boys* is singular → *knows*.")
# ---------- Gap filling: past ----------
M("g13", PAST, FB + "Mahatma Gandhi ____ the Dandi March in 1930.", [("led", ""), ("has led", "*in 1930* is a finished time: no present perfect."), ("leads", "This is a historical fact in the past."), ("had led", "There is no second past action to make this the earlier one.")], "A definite past time → simple past.")
M("g14", PAST, FB + "While I ____ my bicycle, it started to rain.", [("was riding", ""), ("rode", "*While* introduces a longer action in progress: past continuous."), ("had ridden", "The riding was going on, not finished, when the rain started."), ("am riding", "*started* shows the story is in the past.")], "*While* + longer action in progress → past continuous.")
M("g15", PAST, FB + "The thief ____ before the police reached the spot.", [("had escaped", ""), ("escaped", "The escape happened first; to show that clearly, use the past perfect."), ("has escaped", "The story is in the past (*reached*)."), ("was escaping", "*before the police reached* shows the escape was complete.")], "Earlier of two past actions → past perfect.")
M("g16", PAST, FB + "She didn't ____ the bus yesterday.", [("miss", ""), ("missed", "After *did/didn't* always use V1."), ("missing", "After *didn't* use V1, not V-ing."), ("misses", "After *didn't*, V1 with no -s.")], "*didn't* + V1: *didn't miss*.")
M("g17", PAST, FB + "When I entered the hall, the chief guest ____ his speech.", [("was delivering", ""), ("delivers", "*entered* sets the time in the past."), ("has delivered", "The speech was in progress at that past moment."), ("deliver", "The subject is singular and the time is past.")], "Action in progress at a past moment → past continuous.")
M("g18", PAST, FB + "They ____ for three hours when the rescue team found them.", [("had been walking", ""), ("were walking", "*for three hours* before a past event needs the past perfect continuous."), ("have been walking", "The story is in the past (*found*)."), ("walked", "The simple past does not show the duration before *found*.")], "Duration up to a past moment → past perfect continuous.")
M("g19", PAST, FB + "After he ____ his breakfast, he went to the office.", [("had taken", ""), ("has taken", "The story is in the past (*went*)."), ("was taking", "*After* shows the breakfast was finished first."), ("takes", "Both actions are in the past.")], "*After* + earlier completed action → past perfect.")
M("g20", PAST, FB + "The old man ____ under the tree when the storm began.", [("was sleeping", ""), ("slept", "His sleeping was going on and the storm interrupted it."), ("had slept", "He was still asleep when the storm began."), ("sleeps", "The time is past (*began*).")], "Interrupted longer action → past continuous.")
M("g21", PAST, FB + "I ____ him a letter last month, but he hasn't replied yet.", [("wrote", ""), ("have written", "*last month* is a finished time."), ("had written", "No second past action is mentioned to need the past perfect."), ("write", "*last month* needs the past.")], "*last month* → simple past *wrote*.")
M("g22", PAST, FB + "The sun ____ when we reached the hilltop, so we missed the sunset.", [("had already set", ""), ("has already set", "*reached* puts the story in the past."), ("already set", "The setting happened before we reached; the past perfect makes the order clear."), ("was already setting", "*missed the sunset* means it was completely over.")], "Completed before the past moment → *had already set*.")
# ---------- Gap filling: future ----------
M("g23", FUT, FB + "Look at those dark clouds! It ____ rain.", [("is going to", ""), ("will", "When there is present evidence (*dark clouds*), we prefer *going to*."), ("rains", "The rain has not started yet."), ("has", "*has rain* is not a correct form.")], "Prediction from present evidence → *be going to*.")
M("g24", FUT, FB + "This time next week, we ____ on the beach in Goa.", [("will be relaxing", ""), ("will relax", "*This time next week* points to an action in progress at a future moment."), ("relax", "This is a future time, and the action is in progress."), ("will have relaxed", "We will be in the middle of relaxing, not finished.")], "In progress at a future time → future continuous.")
M("g25", FUT, FB + "By the end of this year, I ____ all twelve chapters.", [("will have revised", ""), ("will revise", "*By the end of this year* means completed before that time."), ("revised", "The time is in the future."), ("have revised", "Present perfect cannot point to the end of this year.")], "*By* + future time → future perfect.")
M("g26", FUT, FB + "If you ____ hard, you will surely pass.", [("work", ""), ("will work", "No *will* in an *if* clause."), ("worked", "The result clause *will pass* calls for the present in the *if* clause."), ("are working", "A general condition takes the simple present.")], "First conditional: *If* + simple present, *will* + V1.")
M("g27", FUT, FB + "Don't worry, I ____ you with your project.", [("will help", ""), ("am going to help", "A promise or decision made on the spot takes *will*."), ("help", "The help is a future promise, not a habit."), ("helped", "The help is still to come.")], "A promise made now → *will* + V1.")
M("g28", FUT, FB + "Please wait here until I ____ back.", [("come", ""), ("will come", "No *will* after *until* (a time clause)."), ("came", "The meaning is future; use the present in the time clause."), ("am coming", "A single future event in a time clause takes the simple present.")], "Time clause with *until* → simple present.")
M("g29", FUT, FB + "By next April, my grandfather ____ in this village for sixty years.", [("will have been living", ""), ("will live", "*for sixty years* up to *next April* shows a duration ending at a future point."), ("has been living", "*By next April* is a future point."), ("lived", "The time is future.")], "Duration up to a future point → future perfect continuous.")
# ---------- Sequence of tenses ----------
M("g30", SEQ, FB + "He told me that he ____ busy.", [("was", ""), ("is", "The main verb *told* is in the past, so the clause moves back: *was*."), ("will be", "After a past reporting verb, *will* changes to *would*."), ("has been", "Sequence of tenses: after *told*, use a past form.")], "Past main verb → past in the clause.")
M("g31", SEQ, FB + "Our teacher said that honesty ____ the best policy.", [("is", ""), ("was", "A universal truth or proverb stays in the present."), ("had been", "Universal truths do not change tense."), ("were", "*honesty* is singular, and the truth stays present.")], "Universal truths keep the present even after a past verb.")
M("g32", SEQ, FB + "I hoped that she ____ the competition.", [("would win", ""), ("will win", "After a past verb (*hoped*), *will* becomes *would*."), ("wins", "Sequence of tenses needs a past form."), ("has won", "After *hoped*, a past form is needed.")], "*hoped* (past) → *would win*.")
M("g33", SEQ, FB + "She worked hard so that she ____ get a scholarship.", [("might", ""), ("may", "After a past verb, *may* becomes *might*."), ("can", "The main verb is past; use *could* or *might*."), ("will", "*will* does not express purpose here, and the main verb is past.")], "Purpose clause after a past verb → *might/could*.")
M("g34", SEQ, FB + "We knew that the earth ____ round the sun.", [("moves", ""), ("moved", "A scientific truth stays in the simple present."), ("had moved", "Scientific truths do not shift into the past."), ("was moving", "The fact is permanent, so the simple present.")], "Exception to the sequence of tenses: universal truths.")
M("g35", SEQ, FB + "He ran fast lest he ____ the train.", [("should miss", ""), ("will miss", "*lest* is followed by *should* + V1."), ("would not miss", "*lest* already means *so that ... not*; a second *not* is wrong."), ("missed", "*lest* takes *should* + V1.")], "*lest* + *should* + V1.")
# ---------- Board-style passage gaps ----------
P1 = ("Read the passage and choose the correct option for the blank.\n\n*Rahul ____ (a) cricket since he was six. Last year he ____ (b) selected for the district team, and next month he ____ (c) in the state trials.*\n\n")
M("p01", PRES, P1 + "Blank (a):", [("has been playing", ""), ("is playing", "*since he was six* needs the present perfect continuous."), ("played", "He still plays; the simple past would mean he stopped."), ("plays", "*since* + point of time does not go with the simple present.")], "*since he was six* + still continuing → *has been playing*.", "medium")
M("p02", PAST, P1 + "Blank (b):", [("was", ""), ("has been", "*Last year* is a finished time."), ("is", "*Last year* needs the past."), ("had been", "There is no earlier past action here.")], "*Last year* → simple past passive: *was selected*.", "medium")
M("p03", FUT, P1 + "Blank (c):", [("will play", ""), ("played", "*next month* is in the future."), ("has played", "*next month* is in the future."), ("had played", "*next month* is in the future.")], "*next month* → *will play* (or *is playing*, an arrangement).", "medium")
P2 = ("Read the passage and choose the correct option for the blank.\n\n*The Taj Mahal ____ (a) by Shah Jahan in memory of his wife. Every year millions of tourists ____ (b) it. Recently, the government ____ (c) new rules to protect the marble from pollution.*\n\n")
M("p04", PAST, P2 + "Blank (a):", [("was built", ""), ("is built", "The building happened in the past (the 17th century)."), ("has built", "The Taj Mahal did not build anything; we need the passive *was built*."), ("built", "The Taj Mahal is the thing built; the passive is needed.")], "A past action done to the subject → *was built*.", "medium")
M("p05", PRES, P2 + "Blank (b):", [("visit", ""), ("visits", "*tourists* is plural: no -s."), ("visited", "*Every year* shows a repeated present habit."), ("are visited", "Tourists do the visiting: active voice.")], "*Every year* + plural subject → *visit*.", "medium")
M("p06", PRES, P2 + "Blank (c):", [("has made", ""), ("made", "*Recently* with a result that matters now is best in the present perfect."), ("had made", "There is no second past action."), ("makes", "*Recently* refers to a completed action.")], "*Recently* → present perfect: *has made*.", "hard")
P3 = ("Read the passage and choose the correct option for the blank.\n\n*When I ____ (a) the station, the train ____ (b) already. I ____ (c) for the next one for two hours before it finally arrived.*\n\n")
M("p07", PAST, P3 + "Blank (a):", [("reached", ""), ("had reached", "The reaching is the later action; the leaving of the train came first."), ("have reached", "The story is in the past."), ("was reaching", "Reaching a place is a short completed action.")], "Later of two past actions → simple past.", "medium")
M("p08", PAST, P3 + "Blank (b):", [("had left", ""), ("left", "*already* shows the train went before I reached: past perfect."), ("has left", "The story is in the past."), ("was leaving", "*already* shows the leaving was complete.")], "Earlier past action + *already* → *had left*.", "medium")
M("p09", PAST, P3 + "Blank (c):", [("had been waiting", ""), ("was waiting", "*for two hours before it finally arrived* shows duration up to a past moment."), ("have been waiting", "The story is in the past."), ("waited", "The duration before *arrived* is best shown by the past perfect continuous.")], "Duration before another past action → *had been waiting*.", "hard")
# ---------- Editing ----------
E = "Identify the error and choose the correct correction: "
M("e01", PAST, E + "*He did not went to school yesterday.*", [("went → go", ""), ("did → does", "*yesterday* needs the past *did*; the problem is the V2 after it."), ("yesterday → today", "The time is fine; the verb form is wrong."), ("not → no", "*did not* is correct.")], "*did* + V1: *He did not go to school yesterday.*")
M("e02", PRES, E + "*She have been working here for ten years.*", [("have → has", ""), ("been → being", "*has been working* is the correct present perfect continuous."), ("for → since", "*ten years* is a length of time: *for* is correct."), ("working → worked", "*been* + V-ing is correct here.")], "*She* takes *has*: *She has been working here for ten years.*")
M("e03", PRES, E + "*I am living in Surat since 2015.*", [("am living → have been living", ""), ("since → for", "*2015* is a point of time: *since* is correct."), ("in → at", "*in Surat* is correct for a city."), ("living → live", "*am live* is not a correct form.")], "*since 2015* needs the present perfect continuous.")
M("e04", PRES, E + "*The museum remain closed on Mondays.*", [("remain → remains", ""), ("closed → close", "*remains closed* is correct."), ("on → in", "We say *on Mondays*."), ("Mondays → Monday's", "*on Mondays* (every Monday) needs no apostrophe.")], "*The museum* is singular: *remains*.")
M("e05", PRES, E + "*We have visited Agra last summer.*", [("have visited → visited", ""), ("last → the", "*last summer* is correct."), ("visited → visit", "*have visit* is not a correct form."), ("Agra → to Agra", "*visit* takes no *to*.")], "A finished time (*last summer*) → simple past.")
M("e06", PAST, E + "*When I reached the cinema, the film already started.*", [("already started → had already started", ""), ("reached → had reached", "Reaching happened later; it stays in the simple past."), ("When → While", "*When* is fine for a short action."), ("the film → film", "*the film* is correct.")], "Earlier past action → past perfect.")
M("e07", FUT, E + "*I will tell her when she will come.*", [("will come → comes", ""), ("will tell → tell", "The main clause can keep *will*."), ("when → while", "*when* is right for a single event."), ("her → she", "*tell her* is correct.")], "No *will* in a time clause.")
M("e08", SEQ, E + "*The teacher said that the sun rose in the east.*", [("rose → rises", ""), ("said → says", "*said* is fine; the truth stays present."), ("in → from", "*rises in the east* is the standard phrase."), ("the east → east", "*in the east* is correct.")], "Universal truth → simple present.")
M("e09", PRES, E + "*I am knowing the answer to this question.*", [("am knowing → know", ""), ("the answer → answer", "*the answer* is correct."), ("to → of", "*the answer to a question* is correct."), ("this → that", "*this question* is correct.")], "*know* is stative: *I know the answer.*")
M("e10", PAST, E + "*She has wrote three poems for the school magazine.*", [("wrote → written", ""), ("has → have", "*She* takes *has*."), ("for → to", "*for the school magazine* is correct."), ("poems → poem", "*three* needs the plural.")], "*has* + V3: *has written*.")
M("e11", PAST, E + "*While we were playing, it begin to rain.*", [("begin → began", ""), ("were → was", "*we* takes *were*."), ("While → When", "*While* is right for the longer action."), ("to rain → raining", "*began to rain* is correct.")], "The short past action needs V2: *began*.")
M("e12", SEQ, E + "*He said that he will meet me the next day.*", [("will → would", ""), ("said → says", "With *the next day* the report is clearly in the past."), ("next → following", "*the next day* is acceptable."), ("me → I", "*meet me* is correct.")], "After a past reporting verb, *will* → *would*.")
M("e13", PRES, E + "*Look! The children plays in the garden.*", [("plays → are playing", ""), ("Look → Looks", "*Look!* is an imperative."), ("children → child", "The meaning needs the plural."), ("in → on", "*in the garden* is correct.")], "*Look!* → present continuous, and *children* is plural.")
M("e14", PAST, E + "*Did you saw the comet last night?*", [("saw → see", ""), ("Did → Do", "*last night* needs *Did*."), ("comet → a comet", "*the comet* is fine for a known comet."), ("last → the last", "*last night* is correct.")], "*Did* + V1: *Did you see ...?*")
M("e15", PRES, E + "*Mohan has gone to Delhi a week ago.*", [("has gone → went", ""), ("to → in", "*gone to Delhi* is correct."), ("a → one", "*a week ago* is correct."), ("ago → before", "*a week ago* is correct; the tense is wrong.")], "*ago* → simple past.")
# ---------- Choose the correct sentence ----------
CS = "Choose the grammatically correct sentence."
M("c01", PRES, CS, [("She has been ill since Monday.", ""), ("She is ill since Monday.", "*since Monday* needs the present perfect."), ("She has been ill for Monday.", "*Monday* is a point of time: *since*."), ("She was ill since Monday.", "*since* + still continuing → present perfect.")], "*since* + point of time → present perfect.", "medium")
M("c02", PAST, CS, [("I had finished my work before he came.", ""), ("I have finished my work before he came.", "*came* is past; use *had finished*."), ("I finished my work before he had come.", "The earlier action (finishing) should take *had*, not the later one."), ("I had finish my work before he came.", "*had* + V3: *finished*.")], "Earlier past action → past perfect.", "medium")
M("c03", FUT, CS, [("If it rains, the match will be cancelled.", ""), ("If it will rain, the match will be cancelled.", "No *will* in the *if* clause."), ("If it rains, the match is cancel.", "*will be cancelled* (passive) is needed."), ("If it rained, the match will be cancelled.", "Mixing *rained* with *will* is wrong in this condition.")], "*If* + present, *will* + V1.", "medium")
M("c04", PAST, CS, [("He did not come to the party.", ""), ("He did not came to the party.", "*did not* + V1."), ("He not came to the party.", "Negatives in the simple past need *did not*."), ("He does not came to the party.", "*does not* + V1, and the time is past.")], "*did not* + V1.")
M("c05", PRES, CS, [("I have known her for years.", ""), ("I am knowing her for years.", "*know* is stative and *for years* needs the perfect."), ("I know her since years.", "*years* is a length of time, and *since* needs a perfect tense."), ("I have know her for years.", "*have* + V3: *known*.")], "Stative verb + duration → present perfect.", "medium")
M("c06", SEQ, CS, [("She told me that she was leaving the next day.", ""), ("She told me that she is leaving the next day.", "After *told*, shift back: *was leaving*."), ("She told me that she will leave the next day.", "After *told*, *will* → *would*."), ("She told to me that she was leaving the next day.", "*tell* takes an object directly: *told me*.")], "Sequence of tenses after *told*.", "medium")
M("c07", FUT, CS, [("By 2030, India will have launched many more satellites.", ""), ("By 2030, India will launch many more satellites.", "*By 2030* shows completion before that time."), ("By 2030, India has launched many more satellites.", "2030 is in the future."), ("By 2030, India will have launch many more satellites.", "*will have* + V3: *launched*.")], "*By* + future time → future perfect.", "hard")
M("c08", PAST, CS, [("The phone rang while I was having a bath.", ""), ("The phone was ringing while I had a bath.", "The short action (*rang*) interrupts the longer one (*was having*)."), ("The phone rang while I have a bath.", "The story is in the past."), ("The phone had rang while I was having a bath.", "*had* + V3 is *had rung*, and no past perfect is needed.")], "Short action (simple past) + longer action (past continuous).", "medium")
# ---------- Identify the tense ----------
IT = "Identify the tense of the verb in bold: "
M("i01", FORMS, IT + "*The farmers **have been praying** for rain.*", [("Present perfect continuous", ""), ("Present perfect", "*have prayed* would be the present perfect; *have been* + V-ing is continuous."), ("Past perfect continuous", "That would be *had been praying*."), ("Present continuous", "That would be *are praying*.")], "*have been* + V-ing.")
M("i02", FORMS, IT + "*By evening, the workers **will have painted** the wall.*", [("Future perfect", ""), ("Future continuous", "That would be *will be painting*."), ("Simple future", "That would be *will paint*."), ("Present perfect", "*will* shows the future.")], "*will have* + V3.")
M("i03", FORMS, IT + "*The children **were singing** a song.*", [("Past continuous", ""), ("Present continuous", "*were* is past."), ("Past perfect", "That would be *had sung*."), ("Simple past", "That would be *sang*.")], "*was/were* + V-ing.")
M("i04", FORMS, IT + "*She **had already eaten** when we arrived.*", [("Past perfect", ""), ("Present perfect", "*had* is past; present perfect uses *has/have*."), ("Simple past", "Simple past would be *ate*."), ("Past perfect continuous", "That would be *had been eating*.")], "*had* + V3.")
M("i05", FORMS, IT + "*Ravi **is going to buy** a new phone.*", [("Future with *going to* (a plan)", ""), ("Present continuous", "*is going to* + V1 is a future form, not an action happening now."), ("Simple future", "The simple future uses *will*."), ("Simple present", "*is going to buy* is a future plan.")], "*be going to* + V1 = a future plan.", "medium")
# ---------- True / false ----------
C.tf("t01", PRES, "The present perfect can be used with *yesterday*.", False, "*yesterday* is a finished time, so it takes the simple past: *I met him yesterday*, never *I have met him yesterday*.")
C.tf("t02", PAST, "In *The train had left before we reached*, the train leaving happened first.", True, "The past perfect (*had left*) marks the earlier of the two past actions.")
C.tf("t03", FUT, "We should say *when he will come* in a time clause.", False, "Time clauses use the present for the future: *when he comes*.")
C.tf("t04", SEQ, "A universal truth stays in the present tense even after a past reporting verb.", True, "*He said that the earth is round.* Truths do not change tense.")
C.tf("t05", PRES, "*Since* is used with a length of time, such as *two hours*.", False, "*Since* goes with a point of time (*since 9 a.m.*); *for* goes with a length of time (*for two hours*).")
C.tf("t06", PRES, "Verbs like *know, believe* and *own* are not normally used in the continuous form.", True, "They are stative verbs: they describe states, not actions, so *I know*, not *I am knowing*.")
# ---------- Assertion-reason ----------
C.ar("ar1", PAST, "*I have seen him last week* is incorrect.", "The present perfect cannot be used with a definite past time.", 0,
     "R explains A: *last week* is a definite past time, so the simple past *saw* is needed.", "the sentence uses the present perfect with *last week*.", "definite past times need the simple past.")
C.ar("ar2", SEQ, "*He said that water boils at 100 °C* is correct.", "The sequence of tenses always changes the present into the past.", 2,
     "A is true but R is false: universal truths are an exception to the sequence of tenses.", "a scientific fact stays in the present.", "universal truths are an exception.")
C.ar("ar3", FUT, "*If it rains, we will stay indoors* is correct.", "In the *if* clause of a future condition, the simple present is used.", 0,
     "R explains A: the *if* clause takes the present, the main clause takes *will*.", "it follows the first-conditional pattern.", "*if* clauses take the present, not *will*.")
C.ar("ar4", PRES, "*She is having two brothers* is correct.", "*have* meaning possession is not used in the continuous.", 3,
     "A is false (correct form: *She has two brothers*); R is true and is the reason A is wrong.", "*have* for possession is stative, so *is having* is wrong here.", "possession is a state, not an action.")

chapter = header(1, "Tenses", ["tense_forms", "present_tenses", "past_tenses", "future_forms", "sequence_of_tenses"],
                 "Follows the CBSE 2025-26 English Language and Literature (184) syllabus, Section B Grammar: tenses, tested through gap filling, editing and transformation.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
