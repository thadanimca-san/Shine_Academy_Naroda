"""CBSE Class 10 English Grammar Ch 6: Editing and Omission (integrated board practice). Every item lists the right answer first."""
import sys
from grammar_common import Grammar, header

ROOT = sys.argv[1]
PATH = "app_core/content/cbse/class10/english/grammar/ch06_editing_omission"
C = Grammar("gram10ch06")
blk, kc, M = C.blk, C.check_block, C.mcq
STRAT, ED_V, ED_O, OMIT, MIXED = ["editing_strategy"], ["verb_errors"], ["other_errors"], ["omission"], ["integrated_practice"]

CHECK = ("| Step | Look at | Typical error | Correction |\n|---|---|---|---|\n"
         "| 1 | **Verb tense** | *Yesterday he **goes** home.* | goes → went |\n| 2 | **Subject-verb agreement** | *The list of names **are** long.* | are → is |\n"
         "| 3 | **Verb form after a helper** | *She **can sings**; he **did not came**.* | sings → sing; came → come |\n"
         "| 4 | **Articles / determiners** | *He is **a** honest man; **less** students.* | a → an; less → fewer |\n"
         "| 5 | **Prepositions** | *He is good **in** maths; married **with** her.* | in → at; with → to |\n"
         "| 6 | **Pronouns** | *Between you and **I**; everyone did **their** best* (formal) | I → me |\n"
         "| 7 | **Conjunctions** | *Although he was ill, **but** he came.* | remove *but* / but → (none) |\n"
         "| 8 | **Word form** | *She sings **beautiful**.* | beautiful → beautifully |\n"
         "| 9 | **Singular / plural** | *one of my **friend**; two **childs*** | friend → friends; childs → children |\n"
         "| 10 | **Comparatives** | ***more better**; the **most tallest*** | more better → better |")
MISSING = ("| Word that often goes missing | Example with the gap (^) | Correct |\n|---|---|---|\n"
           "| article | *She is ^ best player.* | the |\n| helping verb | *They ^ playing in the park.* | are |\n| preposition | *He was born ^ 2010.* | in |\n"
           "| *to* (infinitive) | *I want ^ learn music.* | to |\n| pronoun | *Ravi told ^ that he was busy.* | me |\n| conjunction | *She was tired ^ she kept working.* | but |\n"
           "| *of / for / with* after nouns | *a cup ^ tea* | of |\n| *have / has* in perfect tenses | *I ^ finished my work.* | have |")
PREP = ("| Phrase | Correct preposition |\n|---|---|\n| good / bad / expert ___ (a skill) | **at**: *good at maths* |\n| interested ___ | **in** |\n| afraid / proud / fond / tired ___ | **of** |\n"
        "| married / similar / addicted / prefer A ___ B | **to** |\n| different ___ | **from** |\n| angry ___ a person / ___ a thing | **with** a person / **at** or **about** a thing |\n"
        "| depend / rely ___ | **on** |\n| congratulate ___ | **on** |\n| responsible ___ | **for** |\n| born ___ (year/month) / ___ (date) | **in** 2010 / **on** 5 May |\n"
        "| arrive ___ (city) / ___ (place) | **in** Delhi / **at** the station |\n| discuss / enter / reach / attend ___ | **no preposition**: *discuss the plan*, *reach home* |")

sections = [
 {"id": "s1", "title": "Becoming a grammar detective", "blocks": [
  blk("s1.hook", "hook", title="Can you spot it in ten seconds?",
    body="*My brother and me goes to the same school since 2020.*\n\nThis short sentence has **two** errors: the subject pronoun must be *I* (*My brother and **I***), and *since 2020* with two subjects needs *have been going* instead of *goes*. "
         "In the board exam you get one line at a time, and you must find the error and write the correction quickly and neatly.\n\n"
         "Editing and omission bring together everything you have learnt: tenses, modals, concord, determiners, reported speech, plus prepositions and word forms. "
         "This chapter gives you a step-by-step detective method and a large set of board-style lines to practise until spotting errors becomes automatic."),
  blk("s1.inspiration", "inspiration", title="The editor who loved clear English", person="Khushwant Singh", years="1915–2014",
    body="Khushwant Singh edited *The Illustrated Weekly of India* and later the *Hindustan Times*, and wrote the novel *Train to Pakistan*. As an editor, his job every day was to read other people's writing and fix errors before millions of readers saw them.\n\n"
         "He wrote his famous column *With Malice towards One and All* for decades, and received the Padma Vibhushan in 2007. Every good editor starts as a careful detective of small mistakes.",
    future="Editing skills lead to careers in publishing, journalism, content strategy, law (drafting) and translation, and help in every exam you write."),
  C.socratic("s1.socratic", "Which word is wrong? *She is good in drawing.*",
    ["in", "good", "drawing"], 0,
    "We are *good at* a skill: *She is good at drawing.* Preposition errors are a favourite in board editing."),
 ]},
 {"id": "s2", "title": "The detective method", "blocks": [
  blk("s2.thm", "theory", title="How to edit a line", revision=True,
    body="**Board format:** each sentence or line has **one** error. You must write the **incorrect word** and the **correction**, usually in a table or as *incorrect → correct*.\n\n"
         "**Method:**\n1. Read the whole line (and the line before it, if it is a passage) for meaning.\n2. **Find the subject and the verb first.** Most errors are in the verb: tense, agreement, or form after a helper.\n"
         "3. Then check, in order: **articles/determiners → prepositions → pronouns → conjunctions → word forms → plurals → comparatives**.\n"
         "4. Change **only one word** (or the smallest group) and keep the meaning.\n5. Read the corrected line again; it must now be perfect.\n\n"
         "**Spelling and punctuation:** copy your correction exactly; a misspelt correction loses the mark."),
  blk("s2.table", "markdown_table", title="The 10-point error checklist", revision=True, body=CHECK),
  kc("s2.check", "Edit the line: *The children was playing in the garden.*",
    [("was → were", ""), ("playing → played", "*were playing* is fine; the problem is agreement."), ("in → on", "*in the garden* is correct."), ("children → child", "Changing the subject changes the meaning; correct the verb.")],
    "*children* is plural → *were*."),
 ]},
 {"id": "s3", "title": "Prepositions and word forms", "blocks": [
  blk("s3.prep", "markdown_table", title="Fixed prepositions examiners test", revision=True, body=PREP),
  blk("s3.thm", "theory", title="Word forms: noun, verb, adjective, adverb", revision=True,
    body="Many editing errors use the right word in the wrong form:\n\n- **Adjective vs adverb:** an adjective describes a noun (*a **careful** driver*); an adverb describes a verb (*He drives **carefully***). ✗ *She speaks fluent.* ✓ *She speaks fluently.*\n"
         "- **Noun vs verb:** *advice* (noun) / *advise* (verb); *practice* (noun) / *practise* (verb); *success* (noun) / *succeed* (verb) / *successful* (adjective).\n"
         "  ✗ *He gave me good advise.* ✓ *He gave me good advice.*\n- **Comparatives:** never double them. ✗ *more taller, most best* ✓ *taller, best*. Use *than* after a comparative: ✗ *superior than* ✓ *superior **to***.\n"
         "- **Irregular plurals:** *child → children, man → men, mouse → mice, criterion → criteria, phenomenon → phenomena*.\n"
         "- **Pronoun case:** after a preposition use the object form: *between you and **me***, *for **him** and **me***."),
  kc("s3.check", "Edit the line: *She danced so graceful that everyone clapped.*",
    [("graceful → gracefully", ""), ("danced → dances", "The past tense matches *clapped*."), ("so → such", "*so* + adverb is correct."), ("everyone → every one", "*everyone* (all people) is correct.")],
    "*danced* (verb) needs an adverb: *gracefully*."),
  kc("s3.check2", "Edit the line: *My grandfather is fond in gardening.*",
    [("in → of", ""), ("is → was", "The present is fine for a hobby he still has."), ("fond → fondly", "*fond of* uses the adjective."), ("gardening → garden", "*fond of* + V-ing is correct.")],
    "*fond of*."),
 ]},
 {"id": "s4", "title": "Omission: finding the missing word", "blocks": [
  blk("s4.thm", "theory", title="Where words go missing", revision=True,
    body="In an **omission** task, one word has been left out of each line. You must say **which word is missing and where**, usually by writing the word before, the missing word, and the word after.\n\n"
         "**Method:**\n1. Read the line aloud in your head; you will feel a \"bump\" where the word is missing.\n2. Check the grammar skeleton: every finite verb needs its helper (*is/are/have/has/will*); every singular countable noun needs a determiner; every verb + infinitive needs *to*.\n"
         "3. The missing word is usually small: an **article, preposition, helping verb, pronoun, conjunction or *to***."),
  blk("s4.table", "markdown_table", title="The usual missing words", revision=True, body=MISSING),
  kc("s4.check", "Which word is missing? *We have been waiting the bus for an hour.*",
    [("*for* after *waiting*", ""), ("*a* before *bus*", "*the bus* already has a determiner."), ("*the* before *hour*", "*an hour* already has a determiner."), ("*are* after *We*", "*have been waiting* is a complete verb.")],
    "*wait for* someone or something: *waiting for the bus*."),
 ]},
 {"id": "s5", "title": "Board skills: worked lines", "blocks": [
  blk("s5.worked", "worked_example", title="Editing a passage line by line",
    problem="The following passage has one error in each line. Write the incorrect word and the correction.\n\n1. Exercise is very important for a healthy life. It keep\n2. our body fit and our mind fresh. Doctors advices that\n3. we should walk atleast thirty minutes every day. Many\n4. people does not exercise because they think they have no time.",
    steps=["Line 1: *It* is singular → **keep → keeps**.", "Line 2: *Doctors* is plural, and *advice* is a noun; the verb is *advise* → **advices → advise**.",
           "Line 3: *at least* is two words → **atleast → at least**.", "Line 4: *people* is plural → **does → do**."],
    answer="keep → keeps; advices → advise; atleast → at least; does → do"),
  blk("s5.worked2", "worked_example", title="Omission line by line",
    problem="One word is missing in each line. Write the word before, the missing word and the word after.\n\n1. Rani is one of best dancers in our school.\n2. She has been learning Kathak the age of six.\n3. Last year she won first prize at a national festival.\n4. She wants become a dance teacher.",
    steps=["1. Superlative needs *the*: *of **the** best*.", "2. A point of time with the perfect continuous → *since*: *Kathak **since** the*.",
           "3. Ordinal *first* needs *the*: *won **the** first*.", "4. *want* + infinitive: *wants **to** become*."],
    answer="of the best; Kathak since the; won the first; wants to become"),
  kc("s5.check", "Edit the line: *Neither of the answers are correct, so try again.*",
    [("are → is", ""), ("answers → answer", "*Neither of the* needs a plural noun."), ("so → but", "*so* (result) fits the meaning."), ("try → tried", "*try again* is an instruction.")],
    "*Neither of* → singular verb."),
 ]},
 {"id": "s6", "title": "Remember, avoid, practise", "blocks": [
  blk("s6.memory", "memory_trick", title="The VAPPCW scan",
    body="Scan every line in this order:\n\n- **V**erb (tense, agreement, form after helper)\n- **A**rticle / determiner\n- **P**reposition\n- **P**ronoun\n- **C**onjunction (double conjunctions: *although … but*, *though … yet* is fine)\n- **W**ord form (adjective/adverb, noun/verb, plurals, comparatives)\n\n"
         "\"**V**ery **A**ngry **P**eople **P**ick **C**orrect **W**ords.\""),
  blk("s6.mistakes", "common_mistakes", title="Mistakes students make in editing answers",
    body="1. Changing two words when only one is wrong.\n2. Writing the correction with a new error (wrong spelling).\n3. Changing the meaning of the sentence instead of correcting the grammar.\n"
         "4. Not copying the incorrect word exactly as it appears.\n5. In omission, writing only the missing word and not showing where it goes (write the words before and after).\n"
         "6. Ignoring the line before: in a passage, the tense is often set by the earlier line.\n7. Leaving a blank: always write your best guess; there is no negative marking."),
  blk("s6.tip", "teacher_tip", title="Try this in class",
    body="Run an **\"Error auction\"**: put ten sentences on the board, some correct and some with one error. Teams get 100 points to \"bid\" on sentences they think are correct. "
         "Then reveal the answers; teams win points for correct bids and lose them for wrong ones. Students quickly learn to check verbs, articles and prepositions before betting."),
  blk("s6.reflection", "reflection", title="Say it in your own words",
    body="Which grammar area gives you the most errors in your own writing: verbs, articles or prepositions? Write two sentences you often get wrong, and correct them."),
  blk("s6.connection", "connection", title="Where this leads",
    body="- **Chapters 1–4 and Determiners:** every rule you learnt there is tested here.\n- **Chapter 7, Gap Filling:** the same rules, but you supply the word instead of correcting it.\n"
         "- **Your own writing:** use the VAPPCW scan to proofread your letters and paragraphs before the exam ends."),
  blk("s6.mastery", "mastery", title="Mastery challenge",
    body="Edit each line (one error per line):\n\n(a) The news are not good today.\n(b) She is more cleverer than her sister.\n(c) He has gone to Mumbai last week.\n(d) Each of the boys have a bicycle.\n(e) I am looking forward to meet you.\n\n"
         "**Answer:** (a) **are → is** (b) **more cleverer → cleverer** (c) **has gone → went** (d) **have → has** (e) **meet → meeting** (*look forward to* + V-ing)."),
  blk("s6.summary", "summary", title="Chapter summary",
    body="- Each board line has one error (editing) or one missing word (omission).\n- Check the verb first, then determiners, prepositions, pronouns, conjunctions and word forms.\n"
         "- Write the incorrect word and the correction exactly; for omission, show where the word goes.\n- Missing words are usually articles, prepositions, helping verbs, *to*, pronouns or conjunctions.\n"
         "- Learn the fixed prepositions (*good at, fond of, married to, different from, depend on*)."),
  blk("s6.examtips", "exam_tips", title="Board exam tips",
    body="- Spend about one minute per line; come back to difficult lines later.\n- If a line looks correct, check prepositions and articles again; there is always one error.\n"
         "- Answer in the format asked: usually *incorrect word → correct word*.\n- Never rewrite the whole sentence unless asked."),
  blk("s6.flash1", "flashcard", front="Correct: *He is good in maths.*", back="*He is good **at** maths.*"),
  blk("s6.flash2", "flashcard", front="Correct: *Although it rained, but we played.*", back="Remove *but*: *Although it rained, we played.*"),
  blk("s6.flash3", "flashcard", front="Correct: *I look forward to see you.*", back="*look forward to* + V-ing: *to seeing you*."),
  blk("s6.flash4", "flashcard", front="What usually goes missing in omission?", back="Articles, prepositions, helping verbs, *to*, pronouns, conjunctions."),
 ]},
]

E = "Identify the error and choose the correct correction: "
# ---------- Verb errors ----------
M("v01", ED_V, E + "*She go to the temple every Tuesday.*", [("go → goes", ""), ("to → at", "*go to the temple* is correct."), ("every → each", "*every Tuesday* is correct."), ("the temple → temple", "*the temple* is fine.")], "Third person singular → *goes*.")
M("v02", ED_V, E + "*I have visited Jaipur in 2019.*", [("have visited → visited", ""), ("in → on", "*in 2019* is correct for a year."), ("Jaipur → the Jaipur", "City names take no article."), ("visited → visit", "*have visit* is wrong.")], "Definite past time → simple past.")
M("v03", ED_V, E + "*They did not attended the meeting.*", [("attended → attend", ""), ("did → does", "*did* is right for the past."), ("the meeting → meeting", "*the meeting* is fine."), ("not → no", "*did not* is correct.")], "*did* + V1.")
M("v04", ED_V, E + "*The quality of these mangoes are excellent.*", [("are → is", ""), ("these → this", "*these mangoes* is correct."), ("mangoes → mango", "*of these mangoes* is fine."), ("excellent → excellently", "After *is* we need an adjective.")], "Real subject *quality* → *is*.")
M("v05", ED_V, E + "*He could not came on time.*", [("came → come", ""), ("could → can", "*could* fits the past."), ("on → in", "*on time* (punctual) is correct here."), ("not → no", "*could not* is correct.")], "Modal + V1.")
M("v06", ED_V, E + "*By the time we reached, the film already started.*", [("already started → had already started", ""), ("reached → had reached", "The later action stays simple past."), ("By → On", "*By the time* is correct."), ("the film → film", "*the film* is fine.")], "Earlier past action → past perfect.")
M("v07", ED_V, E + "*Everybody in the class like the new teacher.*", [("like → likes", ""), ("Everybody → Every body", "*Everybody* is one word."), ("new → newly", "*new* (adjective) describes *teacher*."), ("in → of", "*in the class* is correct.")], "*Everybody* → singular.")
M("v08", ED_V, E + "*I will call you when I will reach home.*", [("will reach → reach", ""), ("will call → call", "The main clause keeps *will*."), ("when → while", "*when* is right for a single event."), ("home → to home", "*reach home* takes no preposition.")], "Time clause → present.")
M("v09", ED_V, E + "*He has been living here since five years.*", [("since → for", ""), ("has been → have been", "*He* takes *has*."), ("living → lived", "*has been living* is correct."), ("here → there", "*here* is fine.")], "Length of time → *for*.")
M("v10", ED_V, E + "*The teacher said that the earth moved round the sun.*", [("moved → moves", ""), ("said → says", "*said* is fine; the truth stays present."), ("round → around of", "*round the sun* is correct."), ("that → if", "A statement takes *that*.")], "Universal truths keep the present.")
M("v11", ED_V, E + "*We was waiting for the bus when it started raining.*", [("was → were", ""), ("waiting → waited", "*were waiting* is right for the longer action."), ("when → while", "*when* introduces the short action."), ("raining → rain", "*started raining* is correct.")], "*We* → *were*.")
M("v12", ED_V, E + "*You should to apologise to your friend.*", [("should to → should", ""), ("apologise → apologised", "Modal + V1."), ("to your → for your", "*apologise to* a person is correct."), ("friend → friends", "The singular is fine.")], "No *to* after *should*.")
# ---------- Other errors ----------
M("o01", ED_O, E + "*He is an university student.*", [("an → a", ""), ("is → was", "The tense is fine."), ("university → universities", "*a/an* needs a singular noun."), ("student → students", "*a* needs a singular noun.")], "*university* (*yoo*) → *a*.")
M("o02", ED_O, E + "*She is married with a doctor.*", [("with → to", ""), ("is → was", "*is married* (her state now) is fine."), ("a → an", "*doctor* starts with a consonant sound."), ("married → marry", "*is married* is correct.")], "*married to*.")
M("o03", ED_O, E + "*This book is different than that one.*", [("than → from", ""), ("This → These", "*book* is singular."), ("different → differ", "*is different* is correct."), ("one → ones", "*that one* refers to one book.")], "*different from*.")
M("o04", ED_O, E + "*Between you and I, the plan will fail.*", [("I → me", ""), ("Between → Among", "*Between* is right for two people."), ("will → would", "*will fail* is fine."), ("the plan → plan", "*the plan* is fine.")], "After a preposition → object pronoun *me*.")
M("o05", ED_O, E + "*Although he worked hard, but he failed.*", [("but → (remove it)", ""), ("Although → Despite", "*Despite* needs a noun or V-ing, not a clause."), ("hard → hardly", "*hardly* means almost not."), ("failed → fail", "The past matches *worked*.")], "*Although* and *but* cannot both join the same two clauses.", "medium")
M("o06", ED_O, E + "*She sings very sweet.*", [("sweet → sweetly", ""), ("sings → sing", "*She* takes *sings*."), ("very → much", "*very* + adverb is correct."), ("She → Her", "*She* is the subject.")], "Verb → adverb *sweetly*.")
M("o07", ED_O, E + "*Ravi is more taller than his father.*", [("more taller → taller", ""), ("than → then", "*than* is for comparison."), ("his → him", "*his father* is correct."), ("is → was", "The tense is fine.")], "No double comparative.")
M("o08", ED_O, E + "*He gave me a good advise.*", [("a good advise → good advice", ""), ("gave → given", "*gave* is correct."), ("me → to me", "*gave me* is correct."), ("good → well", "*good* (adjective) describes the noun.")], "*advice* is the (uncountable) noun; *advise* is the verb.", "medium")
M("o09", ED_O, E + "*One of my friend lives in London.*", [("friend → friends", ""), ("lives → live", "*One* takes *lives*."), ("in → at", "*in London* is correct."), ("my → mine", "*my friends* is correct.")], "*one of* + plural noun.")
M("o10", ED_O, E + "*I am looking forward to meet you.*", [("meet → meeting", ""), ("forward → forwards", "*look forward to* is fixed."), ("to → for", "*look forward to* is fixed."), ("am looking → look", "*am looking forward* is correct.")], "*look forward to* + V-ing.", "medium")
M("o11", ED_O, E + "*We discussed about the problem for an hour.*", [("discussed about → discussed", ""), ("for → since", "*an hour* is a length of time."), ("an → a", "*hour* starts with a vowel sound."), ("the problem → problem", "*the problem* is fine.")], "*discuss* takes no preposition.", "medium")
M("o13", ED_O, E + "*He is senior than me in the office.*", [("than → to", ""), ("senior → seniors", "*senior* is an adjective here."), ("me → I", "After *to* we use *me*."), ("in → at", "*in the office* is acceptable.")], "*senior to, junior to, superior to, inferior to*.", "medium")
M("o14", ED_O, E + "*The childs are playing in the park.*", [("childs → children", ""), ("are → is", "The plural subject needs *are*."), ("in → at", "*in the park* is correct."), ("playing → play", "*are playing* is correct.")], "*child → children*.")
M("o15", ED_O, E + "*She is angry on her brother.*", [("on → with", ""), ("angry → angrily", "*is angry* uses the adjective."), ("her → hers", "*her brother* is correct."), ("is → was", "The tense is fine.")], "*angry with* a person.")
M("o16", ED_O, E + "*I prefer tea than coffee.*", [("than → to", ""), ("prefer → prefers", "*I* takes *prefer*."), ("tea → the tea", "General drinks need no article."), ("coffee → coffees", "*coffee* is uncountable here.")], "*prefer A to B*.")
# ---------- Omission ----------
O = "Which word is missing from this line, and where? "
M("m01", OMIT, O + "*She is best athlete in our school.*", [("*the* before *best*", ""), ("*a* before *athlete*", "A superlative takes *the*, before *best*."), ("*of* after *athlete*", "*athlete in our school* is correct."), ("*very* before *best*", "*very best* is possible but not a grammatical need.")], "Superlative → *the best*.")
M("m02", OMIT, O + "*The children playing in the rain.*", [("*are* before *playing*", ""), ("*were* after *rain*", "The helper must come before *playing*."), ("*the* before *children*", "*The children* already has *the*."), ("*to* before *playing*", "*to playing* is wrong here.")], "Continuous tense needs a helping verb.")
M("m03", OMIT, O + "*I want learn French.*", [("*to* after *want*", ""), ("*the* before *French*", "Languages take no article."), ("*am* after *I*", "*I am want* is wrong."), ("*a* before *French*", "Languages take no article.")], "*want* + *to* + V1.")
M("m04", OMIT, O + "*He was born 2009.*", [("*in* after *born*", ""), ("*on* after *born*", "Years take *in*."), ("*at* after *born*", "Years take *in*."), ("*the* before *2009*", "Years take no article.")], "*born in* + year.")
M("m05", OMIT, O + "*Rahul told that he was ill.*", [("*me* (or another object) after *told*", ""), ("*to* after *told*", "*told to that* is wrong."), ("*him* after *that*", "*that him was* is wrong."), ("*was* after *Rahul*", "*Rahul was told* changes the meaning.")], "*told* needs an object.")
M("m06", OMIT, O + "*I have living in this city for ten years.*", [("*been* after *have*", ""), ("*am* after *I*", "*I am have* is wrong."), ("*since* after *city*", "*for ten years* is correct already."), ("*the* before *ten*", "*for ten years* takes no article.")], "Present perfect continuous: *have been living*.")
M("m07", OMIT, O + "*Please give me cup of tea.*", [("*a* before *cup*", ""), ("*the* before *tea*", "General *tea* takes no article."), ("*of* after *tea*", "*of* is already there after *cup*."), ("*to* after *give*", "*give me* needs no *to*.")], "Singular countable noun *cup* needs *a*.")
M("m08", OMIT, O + "*She was tired she continued working.*", [("*but* after *tired*", ""), ("*and* after *working*", "The conjunction must join the two clauses."), ("*so* after *continued*", "*so* would be in the wrong place and give the wrong meaning."), ("*was* after *she* (second)", "*she was continued* is wrong.")], "Contrast → *but*.")
M("m09", OMIT, O + "*We are waiting our results.*", [("*for* after *waiting*", ""), ("*to* after *waiting*", "*wait for* something."), ("*the* before *our*", "*the our* is wrong."), ("*on* after *waiting*", "*wait on* means to serve.")], "*wait for*.")
M("m10", OMIT, O + "*Neither Ravi Sita was present.*", [("*nor* after *Ravi*", ""), ("*or* after *Ravi*", "*Neither* pairs with *nor*."), ("*and* after *Ravi*", "*Neither* pairs with *nor*."), ("*not* after *was*", "*Neither* already makes it negative.")], "*neither … nor*.")
M("m11", OMIT, O + "*She asked me I had finished my work.*", [("*if* (or *whether*) after *me*", ""), ("*that* after *me*", "A reported yes/no question takes *if/whether*."), ("*what* after *me*", "*what* changes the meaning."), ("*did* after *me*", "Reported questions do not use *did*.")], "Reported yes/no question → *if/whether*.", "medium")
M("m12", OMIT, O + "*The doctor advised him take rest.*", [("*to* after *him*", ""), ("*that* after *advised*", "*advised that take* is wrong."), ("*should* after *rest*", "The modal cannot come after the verb."), ("*a* before *rest*", "*take rest* / *take a rest* is not the missing grammar.")], "*advised + object + to + V1*.")
# ---------- Integrated passages ----------
P1 = ("The passage below has one error in each numbered line. Choose the correct correction for the given line.\n\n"
      "*(1) Last week our school organise a cleanliness drive. (2) All the student came with brooms and bags. (3) We cleaned the park near our school and plant twenty trees. (4) The principal was very proud on us.*\n\n")
M("p01", MIXED, P1 + "Line (1):", [("organise → organised", ""), ("Last → The last", "*Last week* takes no article."), ("our → ours", "*our school* is correct."), ("a → the", "First mention → *a* is fine.")], "*Last week* → past tense.", "medium")
M("p02", MIXED, P1 + "Line (2):", [("student → students", ""), ("came → come", "The story is past."), ("with → by", "*came with brooms* is correct."), ("All → Each", "*All the students* is the natural meaning.")], "*All the* + plural noun.", "medium")
M("p03", MIXED, P1 + "Line (3):", [("plant → planted", ""), ("cleaned → clean", "The story is past."), ("near → nearby", "*near our school* is correct."), ("twenty → twentieth", "We need the number of trees.")], "Parallel past verbs: *cleaned … planted*.", "medium")
M("p04", MIXED, P1 + "Line (4):", [("on → of", ""), ("was → were", "*The principal* is singular."), ("very → much", "*very proud* is correct."), ("us → we", "After a preposition use *us*.")], "*proud of*.", "medium")
P2 = ("The passage below has one error in each numbered line. Choose the correct correction for the given line.\n\n"
      "*(1) Water is one of the most precious resource on earth. (2) Yet many people wastes it carelessly. (3) If we does not save water now, (4) our children will suffered in the future.*\n\n")
M("p05", MIXED, P2 + "Line (1):", [("resource → resources", ""), ("most → more", "*one of the most* is correct."), ("the → a", "Superlative takes *the*."), ("on → in", "*on earth* is correct.")], "*one of the most* + plural noun.", "medium")
M("p06", MIXED, P2 + "Line (2):", [("wastes → waste", ""), ("many → much", "*people* is countable."), ("carelessly → careless", "The verb needs an adverb."), ("Yet → So", "*Yet* (contrast) fits the meaning.")], "*people* is plural → *waste*.", "medium")
M("p07", MIXED, P2 + "Line (3):", [("does → do", ""), ("If → Unless", "*Unless we do not* would be a double negative."), ("save → saving", "*do not* + V1."), ("now → then", "*now* fits the meaning.")], "*we* → *do*.", "medium")
M("p08", MIXED, P2 + "Line (4):", [("suffered → suffer", ""), ("will → would", "First conditional uses *will*."), ("our → ours", "*our children* is correct."), ("in → at", "*in the future* is correct.")], "*will* + V1.", "medium")
# ---------- True / false ----------
C.tf("t01", STRAT, "In board editing, each line usually has exactly one error.", True, "That is the standard pattern, so look for one error and correct only that word.")
C.tf("t02", ED_O, "*Discuss about* is correct English.", False, "*discuss* takes a direct object: *discuss the plan*.")
C.tf("t03", ED_O, "*Although … but* can be used together in one sentence.", False, "Use only one: *Although it rained, we played* or *It rained, but we played*.")
C.tf("t04", OMIT, "Missing words in omission tasks are often articles, prepositions or helping verbs.", True, "These small words are easy to drop and easy to test.")
C.tf("t05", ED_O, "We say *superior than*.", False, "*superior, inferior, senior, junior, prefer* take *to*.")
C.tf("t06", STRAT, "When editing, you should rewrite the whole sentence in your own words.", False, "Write only the incorrect word and its correction, keeping the meaning.")
# ---------- Assertion-reason ----------
C.ar("ar1", ED_O, "*She is good at painting* is correct.", "We use *at* after *good* when talking about a skill.", 0,
     "R explains A.", "*good at* is the right phrase.", "skills take *good at*.")
C.ar("ar2", ED_V, "*He did not went* is correct.", "*did* is followed by the base form of the verb.", 3,
     "A is false (*did not go*); R is true and explains the correction.", "*went* after *did* is wrong.", "*did* + V1.")
C.ar("ar3", ED_O, "*She speaks English fluently* is correct.", "An adverb describes a verb.", 0,
     "R explains A: *fluently* describes *speaks*.", "*fluently* is the right form.", "adverbs describe verbs.")
C.ar("ar4", STRAT, "Reading the previous line helps in editing a passage.", "The tense of a passage is often set by an earlier line.", 0,
     "R explains A.", "context reveals the right tense.", "earlier lines set the time.")

chapter = header(6, "Editing and Omission", ["editing_strategy", "verb_errors", "other_errors", "omission", "integrated_practice"],
                 "Integrated board practice for the CBSE 2025-26 English Language and Literature (184) Section B Grammar: identifying and correcting errors and missing words across tenses, modals, concord, determiners and reported speech.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
