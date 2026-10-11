"""CBSE Class 10 English Grammar: Determiners (new chapter, alias ncert_class10_grammar_ch11). Every item lists the right answer first."""
import sys
from grammar_common import Grammar, header

ROOT = sys.argv[1]
PATH = "app_core/content/cbse/class10/english/grammar/ch11_determiners"
C = Grammar("gram10ch11")
blk, kc, M = C.blk, C.check_block, C.mcq
ART, DEM, QUANT, DIST, MIX = ["articles"], ["demonstratives_possessives"], ["quantifiers"], ["distributives_numbers"], ["determiners_in_context"]

KINDS = ("| Kind | Determiners | Example |\n|---|---|---|\n| Articles | a, an, the | ***an** honest man, **the** Ganga* |\n"
         "| Demonstratives | this, that, these, those | ***these** books* |\n| Possessives | my, your, his, her, its, our, their | ***their** house* |\n"
         "| Quantifiers | some, any, much, many, little, a little, few, a few, a lot of, enough, several, no, all, most | ***a few** friends* |\n"
         "| Distributives | each, every, either, neither, both | ***each** student* |\n| Numbers | one, two, first, second, last | ***the first** prize* |\n"
         "| Question words | which, what, whose | ***Whose** bag is this?* |")
FEW = ("| Countable (plural) | Uncountable | Meaning |\n|---|---|---|\n| **few** | **little** | almost none (negative feeling) |\n"
       "| **a few** | **a little** | some, a small number/amount (positive feeling) |\n| **the few** | **the little** | the small number/amount that there is, all of it |\n"
       "| **many** | **much** | a large number / amount (mostly in questions and negatives) |\n| **a lot of / lots of / plenty of** | **a lot of / lots of / plenty of** | a large number / amount (both) |\n"
       "| **number of** | **amount of** | *a large number of people*, *a large amount of money* |")
THE = ("| Use **the** | Use **no article** |\n|---|---|\n| something already mentioned or known: *the book I lent you* | general plural or uncountable nouns: *Books are friends.* *Milk is good for health.* |\n"
       "| unique things: *the sun, the moon, the sky, the earth* | names of people, cities, countries (most): *Ravi, Delhi, India* |\n"
       "| superlatives and ordinals: *the best, the tallest, the first, the last* | meals: *We have lunch at one.* |\n"
       "| rivers, seas, oceans, mountain ranges, deserts, groups of islands: *the Ganga, the Arabian Sea, the Himalayas, the Thar* | single mountains and lakes: *Mount Everest, Lake Dal* |\n"
       "| newspapers, holy books, famous buildings: *the Times of India, the Gita, the Taj Mahal* | languages and subjects: *She speaks Gujarati.* *I love history.* |\n"
       "| musical instruments: *She plays the sitar.* | games and sports: *He plays cricket.* |\n"
       "| countries with Republic/Kingdom/States, or plural names: *the USA, the UK, the Netherlands* | *go to school/church/bed/hospital* for their main purpose |\n"
       "| *the* + adjective = group: *the poor, the rich, the blind* | days, months, festivals: *on Monday, in May, at Diwali* |")

sections = [
 {"id": "s1", "title": "The words that point", "blocks": [
  blk("s1.hook", "hook", title="A, the or nothing?",
    body="Compare:\n\n- *I saw **a** tiger.* (some tiger, any one)\n- *I saw **the** tiger.* (the one we were talking about)\n- *I saw **few** tigers.* (hardly any, a disappointing trip)\n- *I saw **a few** tigers.* (some, a happy trip!)\n\n"
         "The small words before a noun tell us *which* one and *how much*. They are called **determiners**. A tiny change (*few* → *a few*) can turn a sad sentence into a happy one.\n\n"
         "Determiners are part of the CBSE grammar syllabus and appear in almost every gap-filling and editing question. Let's master them."),
  blk("s1.inspiration", "inspiration", title="The storyteller of Malgudi", person="R. K. Narayan", years="1906–2001",
    body="R. K. Narayan created the imaginary town of Malgudi and filled it with unforgettable people: Swami and his friends, the guide Raju, the sweet-vendor Jagan. "
         "His English was simple and exact. Every *a*, *the* and *some* in his sentences was in the right place, so his stories read as smoothly as talk.\n\n"
         "He won the Sahitya Akademi Award in 1958 for *The Guide* and the Padma Vibhushan in 2000. His *Malgudi Days* was made into a much-loved television series.",
    future="Precise English opens careers in writing, publishing, film scripts, editing and translation."),
  C.socratic("s1.socratic", "Which sentence shows that the speaker is *pleased* with the number of friends who came?",
    ["A few friends came to my party.", "Few friends came to my party.", "No friends came to my party."], 0,
    "*A few* = some (a positive idea). *Few* = hardly any (a disappointing idea)."),
 ]},
 {"id": "s2", "title": "What determiners are", "blocks": [
  blk("s2.thm", "theory", title="Words that come before a noun", revision=True,
    body="A **determiner** comes before a noun (and before any adjective) and tells us **which**, **whose** or **how many/how much**: *the* old *house*, *my* new *phone*, *three* red *apples*.\n\n"
         "Two things decide which determiner to use:\n1. **Countable or uncountable?** Countable nouns have a plural (*book → books*); uncountable nouns don't (*water, advice, information, furniture, luggage, news, money, knowledge*).\n"
         "2. **Specific or general?** Do the speaker and listener know which one?\n\n"
         "**Watch out:** *advice, information, furniture, luggage, equipment, homework, news* are uncountable in English: *some advice* (✗ *an advice*), *a piece of information* (✗ *informations*)."),
  blk("s2.kinds", "markdown_table", title="Kinds of determiners", revision=True, body=KINDS),
  kc("s2.check", "Which of these nouns is uncountable?",
    [("Furniture", ""), ("Chair", "*chair* has a plural (*chairs*), so it is countable."), ("Table", "*table → tables*: countable."), ("Bed", "*bed → beds*: countable.")],
    "*furniture* has no plural: *some furniture, a piece of furniture*."),
 ]},
 {"id": "s3", "title": "Articles: a, an, the", "blocks": [
  blk("s3.thm", "theory", title="a / an: the sound decides", revision=True,
    body="**a** and **an** are used with **singular countable** nouns when we mean *any one* or mention something for the first time.\n\n"
         "The choice depends on the **sound**, not the letter:\n- **an** before a vowel **sound**: *an apple, an hour (h is silent), an honest man, an MLA (em-el-ay), an FIR, an X-ray*\n"
         "- **a** before a consonant **sound**: *a book, a university (yoo-), a European (yoo-), a one-rupee coin (wun-), a uniform, a useful tip*\n\n"
         "Other uses of *a/an*: jobs (*She is **a** doctor*), *per* (*fifty km **an** hour*, *twice **a** week*), exclamations (*What **a** beautiful day!*), and with *such* (*such **a** good boy*)."),
  blk("s3.the", "markdown_table", title="When to use the — and when to leave it out", revision=True, body=THE),
  kc("s3.check", "Fill in the blank: He is ____ honest and hard-working officer.",
    [("an", ""), ("a", "*honest* begins with a vowel sound (the *h* is silent), so *an*."), ("the", "We are not talking about a particular officer already known."), ("no article", "A singular countable noun (*officer*) needs an article.")],
    "Silent *h* → vowel sound → *an honest*."),
  kc("s3.check2", "Fill in the blank: ____ Himalayas protect India from cold winds.",
    [("The", ""), ("A", "A mountain range takes *the*."), ("An", "*An* is wrong; mountain ranges take *the*."), ("No article", "Mountain ranges take *the*; only single peaks (*Mount Everest*) take none.")],
    "Mountain ranges → *the*."),
  kc("s3.check3", "Fill in the blank: She studied at ____ university in Ahmedabad.",
    [("a", ""), ("an", "*university* begins with a *yoo* sound (a consonant sound): *a*."), ("the", "Nothing tells us which university, so it is general."), ("no article", "A singular countable noun needs an article.")],
    "*university* sounds like *yoo* → *a*."),
 ]},
 {"id": "s4", "title": "Quantifiers: how many, how much", "blocks": [
  blk("s4.few", "markdown_table", title="few, a few, little, a little, much, many", revision=True, body=FEW),
  blk("s4.thm", "theory", title="some / any / no, much / many, enough", revision=True,
    body="**some**: positive sentences, and offers/requests: *I have **some** money.* *Would you like **some** tea?* *Can I have **some** water?*\n"
         "**any**: negatives and most questions: *I don't have **any** money.* *Do you have **any** questions?* Also *any* = it doesn't matter which: *Take **any** book.*\n"
         "**no** = not any: *There is **no** milk.* (✗ *There is not no milk*)\n\n"
         "**much** (uncountable) and **many** (countable): *How **much** sugar? How **many** eggs?* In positive sentences we usually say *a lot of*: *She has **a lot of** friends.*\n\n"
         "**enough** goes before a noun: *We have **enough** chairs.* (but after an adjective: *old enough*)\n\n"
         "**several** (countable, more than two): *several times*. **all, most, some, none of the** + noun: *Most of the students passed.*"),
  kc("s4.check", "Fill in the blank: There is ____ hope of finding survivors now; the rescue team is losing heart.",
    [("little", ""), ("a little", "*a little* hope is positive; the team is losing heart, so the meaning is negative."), ("few", "*hope* is uncountable: *little*, not *few*."), ("many", "*many* is for countable nouns.")],
    "Uncountable + negative meaning → *little*."),
  kc("s4.check2", "Fill in the blank: Could you give me ____ information about the timings?",
    [("some", ""), ("any", "In requests we normally use *some*."), ("an", "*information* is uncountable: no *an*."), ("many", "*information* is uncountable: *many* is for countable nouns.")],
    "Request + uncountable noun → *some information*."),
 ]},
 {"id": "s5", "title": "Each, every, either, neither, this, that", "blocks": [
  blk("s5.thm", "theory", title="Distributives, demonstratives and possessives", revision=True,
    body="**each**: every one taken separately (two or more): *Each child got a gift.*\n**every**: all of a group (three or more), seen together: *Every student must wear a badge.* *every day, every week.* (Never *every of*; say *each of* or *every one of*.)\n"
         "**either**: one or the other of two: *You can sit on either side.*\n**neither**: not one and not the other of two: *Neither answer is correct.*\n**both**: the two together: *Both answers are correct.*\n"
         "All of *each, every, either, neither* take a **singular noun and verb**.\n\n"
         "**this / these** (near), **that / those** (far): *this book, these books, that house, those houses*. They must agree with the noun: ✗ *this books*.\n\n"
         "**Possessives** (*my, your, his, her, its, our, their*) replace an article: ✗ *the my book*. And *its* (belonging to it) ≠ *it's* (it is): *The dog wagged **its** tail.*"),
  kc("s5.check", "Fill in the blank: There are shops on ____ side of the road.",
    [("either", ""), ("both", "*both* needs a plural noun: *both sides*."), ("every", "A road has two sides; *every* is for three or more."), ("all", "*all* needs a plural noun: *all sides*.")],
    "*either side* = both sides of two (singular noun)."),
  kc("s5.check2", "Fill in the blank: The company has changed ____ logo.",
    [("its", ""), ("it's", "*it's* means *it is*."), ("their", "*The company* here is treated as one unit (singular)."), ("his", "A company is not *he*.")],
    "Possessive of *it* → *its* (no apostrophe)."),
 ]},
 {"id": "s6", "title": "Board skills", "blocks": [
  blk("s6.worked", "worked_example", title="Gap filling with determiners",
    problem="Fill in the blanks with suitable determiners:\n\n*(a) ____ Ganga is (b) ____ longest river in India. It rises in (c) ____ Himalayas. (d) ____ year, millions of pilgrims take (e) ____ dip in its water, but (f) ____ of them think about keeping it clean.*",
    steps=["(a) A river → **The** Ganga.", "(b) A superlative → **the** longest.", "(c) A mountain range → **the** Himalayas.",
           "(d) A repeated time → **Every** year (or *Each* year).", "(e) One single dip, first mention → **a** dip.",
           "(f) The meaning is negative (*but*), countable *them* → **few**."],
    answer="The, the, the, Every, a, few"),
  blk("s6.worked2", "worked_example", title="Editing determiner errors",
    problem="Each line has one error. Correct it.\n\n1. He gave me an useful advice.\n2. I have less friends than my brother.\n3. Mount Everest is a highest peak in the world.\n4. Each students received a certificate.",
    steps=["1. *useful* starts with a *yoo* sound, and *advice* is uncountable: **an useful advice → some useful advice / a useful piece of advice**.",
           "2. *friends* is countable: **less → fewer**.", "3. Superlative needs *the*: **a highest → the highest**.", "4. *each* + singular noun: **students → student**."],
    answer="some useful advice; fewer; the highest; student"),
  kc("s6.check", "Find the error: *I need an information about the trains.*",
    [("an information → some information", ""), ("about → for", "*information about* is correct."), ("the trains → trains", "*the trains* (the specific trains) is fine."), ("need → needs", "*I need* is correct.")],
    "*information* is uncountable: no *an*."),
 ]},
 {"id": "s7", "title": "Remember, avoid, practise", "blocks": [
  blk("s7.memory", "memory_trick", title="Remember determiners the easy way",
    body="- **A/an: listen, don't look.** *an hour, a university, an MBA, a one-way street.*\n- **\"A\" makes it positive:** *a few, a little* = some. Without *a*: *few, little* = almost none.\n"
         "- **Few/many/fewer = count** (people, books). **Little/much/less = amount** (water, time).\n- **THE for the ONE:** one sun, one best, one first, one Ganga, one Himalayas.\n"
         "- **Each, every, either, neither → singular noun.**"),
  blk("s7.mistakes", "common_mistakes", title="Common mistakes",
    body="1. ✗ *a hour* ✓ *an hour*; ✗ *an university* ✓ *a university*\n2. ✗ *an advice / informations / furnitures* ✓ *some advice, information, furniture*\n3. ✗ *less people* ✓ *fewer people*\n"
         "4. ✗ *He is best student.* ✓ *He is the best student.*\n5. ✗ *She plays the cricket.* ✓ *She plays cricket.* (but *plays the violin*)\n6. ✗ *Every students* ✓ *Every student*\n"
         "7. ✗ *the Mount Everest* ✓ *Mount Everest*; ✗ *Himalayas* ✓ *the Himalayas*\n8. ✗ *this books* ✓ *these books*\n9. ✗ *I don't have some money.* ✓ *I don't have any money.*\n10. ✗ *it's own way* ✓ *its own way*"),
  blk("s7.tip", "teacher_tip", title="Try this in class",
    body="Read out a short news report with every determiner removed and ask students to restore them. Then play **\"few or a few?\"**: the teacher says a situation "
         "(*Only two people came to the free concert*), and students hold up a card *FEW* or *A FEW* to show the feeling. Finish with an *a/an* sound race: *hour, union, MLA, one-day match, honour, European*."),
  blk("s7.reflection", "reflection", title="Say it in your own words",
    body="Explain the difference between *He has little knowledge of computers* and *He has a little knowledge of computers*. Which one would help him get a job?"),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 3, Concord:** *each/every/either/neither* take singular verbs; *a number of / the number of*.\n- **Editing and gap filling:** article errors are among the commonest in the board paper.\n"
         "- **Analytical paragraph writing:** *a large number of, a small amount of, the majority of, few, several* describe data precisely."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="Fill in the blanks:\n\n*There was (a) ____ old man in our village who owned (b) ____ elephant. (c) ____ children loved (d) ____ elephant, but (e) ____ adults were afraid of it. Every morning (f) ____ man took it to (g) ____ river for (h) ____ bath.*\n\n"
         "**Answer:** (a) **an** (b) **an** (c) **The** / *All the* (d) **the** (now known) (e) **some/many** (or *a few*) (f) **the** (g) **the** (h) **a**."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- Determiners come before nouns and tell which, whose, how many or how much.\n- *a/an* by sound; *the* for specific or unique things, superlatives, rivers, ranges, oceans, instruments.\n"
         "- No article with general plurals, uncountables, names, meals, languages, games.\n- *few/a few/many/fewer* with countables; *little/a little/much/less* with uncountables.\n"
         "- *some* in positives, offers and requests; *any* in negatives and questions.\n- *each, every, either, neither* + singular noun."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- Decide countable/uncountable first, then positive/negative meaning.\n- Say the next word aloud in your head before choosing *a* or *an*.\n"
         "- In editing, look for a missing *the* before superlatives, and for *a/an* before uncountable nouns.\n- Remember the uncountables: *advice, information, furniture, luggage, equipment, news, knowledge*."),
  blk("s7.flash1", "flashcard", front="a or an: ___ hour, ___ university, ___ MLA?", back="*an hour*, *a university*, *an MLA*: the sound decides."),
  blk("s7.flash2", "flashcard", front="few vs a few?", back="*few* = almost none (negative); *a few* = some (positive). Both with countable nouns."),
  blk("s7.flash3", "flashcard", front="fewer or less: ___ students, ___ water?", back="*fewer students* (countable), *less water* (uncountable)."),
  blk("s7.flash4", "flashcard", front="*the* with rivers or single mountains?", back="Rivers: *the Ganga*. Single mountains: no article: *Mount Abu*."),
 ]},
]

FB = "Fill in the blank with the correct determiner: "
# ---------- Articles ----------
M("a01", ART, FB + "She waited for ____ hour at the bus stop.", [("an", ""), ("a", "*hour* begins with a vowel sound (silent h)."), ("the", "It is not a particular hour already known."), ("one", "*one hour* is possible in meaning, but the natural determiner here is *an*.")], "Silent *h* → *an hour*.")
M("a02", ART, FB + "My cousin is ____ European citizen.", [("a", ""), ("an", "*European* begins with a *yoo* sound (consonant)."), ("the", "Nothing makes it specific."), ("no article", "A singular countable noun needs an article.")], "*European* → *yoo* sound → *a*.")
M("a03", ART, FB + "He was elected ____ MLA last year.", [("an", ""), ("a", "*MLA* is read *em-el-ay*, starting with a vowel sound."), ("the", "Nothing shows a particular post known to both."), ("no article", "A singular countable noun needs an article here.")], "*MLA* starts with the sound *em* → *an*.", "medium")
M("a04", ART, FB + "____ sun gives us light and heat.", [("The", ""), ("A", "There is only one sun: *the*."), ("An", "There is only one sun."), ("No article", "Unique things take *the*.")], "Unique things → *the*.")
M("a05", ART, FB + "Mumbai is ____ largest city in India.", [("the", ""), ("a", "Superlatives take *the*."), ("an", "Superlatives take *the*."), ("no article", "Superlatives need *the*.")], "Superlative → *the*.")
M("a06", ART, FB + "My sister plays ____ violin beautifully.", [("the", ""), ("a", "Musical instruments take *the* when we talk about playing them."), ("an", "Instruments take *the*."), ("no article", "Instruments take *the*; only games take no article.")], "Musical instruments → *the*.")
M("a07", ART, FB + "We play ____ football every evening.", [("no article", ""), ("the", "Games and sports take no article."), ("a", "Games take no article."), ("an", "Games take no article.")], "Games → no article.")
M("a08", ART, FB + "____ Arabian Sea lies to the west of India.", [("The", ""), ("An", "Seas take *the*."), ("A", "Seas take *the*."), ("No article", "Seas and oceans take *the*.")], "Seas → *the*.")
M("a09", ART, FB + "This is ____ one-way road.", [("a", ""), ("an", "*one* is pronounced *wun* (a consonant sound)."), ("the", "Nothing makes it specific."), ("no article", "A singular countable noun needs an article.")], "*one* → *w* sound → *a*.", "medium")
M("a10", ART, FB + "The train was running at eighty kilometres ____ hour.", [("an", ""), ("a", "*hour* starts with a vowel sound."), ("the", "*per hour* is expressed with *an*."), ("each", "*each hour* is not the usual way to express speed.")], "*an hour* = per hour.")
M("a11", ART, FB + "____ rich should help the poor.", [("The", ""), ("A", "*the* + adjective names a group of people."), ("An", "*the* + adjective names a group."), ("No article", "*rich* alone cannot name the group; use *the rich*.")], "*the* + adjective = group.")
M("a12", ART, FB + "He goes to ____ school by bus.", [("no article", ""), ("the", "*go to school* (as a student) takes no article."), ("a", "*go to school* is a fixed expression without an article."), ("an", "*school* starts with a consonant, and no article is needed.")], "*go to school/bed/church* for its purpose → no article.", "medium")
M("a13", ART, FB + "What ____ wonderful surprise!", [("a", ""), ("the", "Exclamations with *What* + singular noun take *a/an*."), ("an", "*wonderful* begins with a consonant sound."), ("no article", "A singular countable noun needs *a*.")], "*What a …!*")
M("a14", ART, FB + "Mount Abu is ____ hill station in Rajasthan.", [("a", ""), ("the", "There are many hill stations; this is one of them."), ("an", "*hill* begins with a consonant sound."), ("no article", "A singular countable noun needs an article.")], "One of many → *a*.")
M("a15", ART, FB + "I read ____ Hindustan Times every morning.", [("the", ""), ("a", "Names of newspapers take *the*."), ("an", "Names of newspapers take *the*."), ("no article", "Newspapers take *the*.")], "Newspapers → *the*.")
M("a16", ART, FB + "I bought a pen and a notebook. ____ pen is blue.", [("The", ""), ("A", "The pen has already been mentioned."), ("An", "*pen* starts with a consonant, and it has been mentioned."), ("This", "*This* could fit in speech, but the second mention of a noun takes *the*.")], "Second mention → *the*.")
# ---------- Quantifiers ----------
M("q01", QUANT, FB + "There is ____ water in the bottle; please fill it.", [("little", ""), ("few", "*water* is uncountable: *little*."), ("a few", "*water* is uncountable."), ("many", "*many* is for countable nouns.")], "Uncountable + almost none → *little*.")
M("q02", QUANT, FB + "I have ____ friends in this city, so I never feel lonely.", [("a few", ""), ("few", "*few* means almost none; but you never feel lonely."), ("a little", "*friends* is countable."), ("little", "*friends* is countable.")], "Countable + positive meaning → *a few*.")
M("q03", QUANT, FB + "____ people can keep a secret; most tell somebody.", [("Few", ""), ("A few", "*A few* is positive; the sentence says hardly anyone can."), ("Little", "*people* is countable."), ("Much", "*people* is countable.")], "Countable + almost none → *Few*.")
M("q04", QUANT, FB + "Add ____ salt to the soup; it tastes bland.", [("a little", ""), ("a few", "*salt* is uncountable."), ("few", "*salt* is uncountable."), ("many", "*salt* is uncountable.")], "Uncountable + some → *a little*.")
M("q05", QUANT, FB + "How ____ money do you need for the trip?", [("much", ""), ("many", "*money* is uncountable."), ("few", "*How few* is not the usual question."), ("a lot", "*How a lot* is not English.")], "Uncountable → *How much*.")
M("q06", QUANT, FB + "How ____ students are there in your class?", [("many", ""), ("much", "*students* is countable."), ("little", "*students* is countable."), ("lot", "*How lot* is not English.")], "Countable → *How many*.")
M("q07", QUANT, FB + "Is there ____ milk left in the fridge?", [("any", ""), ("some", "In ordinary questions we use *any*."), ("many", "*milk* is uncountable."), ("a few", "*milk* is uncountable.")], "Questions → *any*.")
M("q08", QUANT, FB + "Would you like ____ biscuits with your tea?", [("some", ""), ("any", "In offers we use *some*."), ("much", "*biscuits* is countable."), ("a little", "*biscuits* is countable.")], "Offers → *some*.")
M("q09", QUANT, FB + "I didn't buy ____ vegetables yesterday.", [("any", ""), ("some", "In negatives we use *any*."), ("no", "*didn't* + *no* is a double negative."), ("much", "*vegetables* is countable.")], "Negatives → *any*.")
M("q10", QUANT, FB + "This year ____ students failed than last year.", [("fewer", ""), ("less", "*students* is countable: *fewer*."), ("little", "A comparison with *than* needs *fewer*."), ("lesser", "*lesser* is not used for numbers.")], "Countable comparison → *fewer*.", "medium")
M("q11", QUANT, FB + "We spent ____ time on the first question than on the second.", [("less", ""), ("fewer", "*time* is uncountable."), ("little", "A comparison with *than* needs *less*."), ("few", "*time* is uncountable.")], "Uncountable comparison → *less*.", "medium")
M("q12", QUANT, FB + "He spent ____ money he had on books.", [("the little", ""), ("a little", "*the little … he had* means all of the small amount."), ("little", "*little money he had* lacks *the*, which the clause *he had* needs."), ("few", "*money* is uncountable.")], "*the little* = the small amount, all of it.", "hard")
M("q13", QUANT, FB + "There are ____ chairs for everyone; nobody has to stand.", [("enough", ""), ("much", "*chairs* is countable."), ("little", "*little* would mean nearly none."), ("a little", "*chairs* is countable.")], "*enough* + plural noun.")
M("q14", QUANT, FB + "I have ____ homework today, so I can't come out.", [("a lot of", ""), ("many", "*homework* is uncountable."), ("a few", "*homework* is uncountable."), ("several", "*several* needs a plural countable noun.")], "Uncountable in a positive sentence → *a lot of*.")
M("q15", QUANT, FB + "There is ____ sugar in the tin. Let's buy some.", [("no", ""), ("not", "*not* cannot come directly before a noun like this."), ("any", "*There is any sugar* is not correct in a positive sentence."), ("none", "*none* is a pronoun; before a noun use *no*.")], "*no* + noun = not any.")
# ---------- Distributives, demonstratives, numbers ----------
M("d01", DIST, FB + "____ student was given a laptop.", [("Each", ""), ("All", "*All* needs a plural noun and verb."), ("Both", "*Both* needs a plural noun."), ("Many", "*Many* needs a plural noun.")], "*Each* + singular noun.")
M("d02", DIST, FB + "I like ____ of these two dresses; I can't decide.", [("both", ""), ("either", "*either of* means one or the other; *both* fits liking the two."), ("neither", "*neither* means you like none, which contradicts *can't decide*."), ("every", "*every of* is not English.")], "*both* = the two together.", "medium")
M("d03", DIST, FB + "____ of the two roads leads to the station; both go to the market.", [("Neither", ""), ("Either", "*Either* means one of the two does; the sentence says both go elsewhere."), ("Both", "*Both … leads* is wrong, and the meaning is negative."), ("Each", "*Each* would mean both lead to the station.")], "None of two → *Neither*.", "medium")
M("d04", DIST, FB + "The Olympics are held ____ four years.", [("every", ""), ("each", "*every four years* is the fixed expression for a regular interval."), ("all", "*all four years* changes the meaning."), ("either", "*either* is for one of two.")], "*every* + number + plural for intervals.", "medium")
M("d05", DEM, FB + "Look at ____ birds on the far wire.", [("those", ""), ("these", "The birds are far away: *those*."), ("that", "*birds* is plural."), ("this", "*birds* is plural and far.")], "Plural + far → *those*.")
M("d06", DEM, FB + "____ book in my hand is a gift from my aunt.", [("This", ""), ("That", "The book is near (in my hand)."), ("These", "*book* is singular."), ("Those", "*book* is singular and near.")], "Singular + near → *This*.")
M("d07", DEM, FB + "The dog hurt ____ leg.", [("its", ""), ("it's", "*it's* = *it is*."), ("his", "We usually refer to an animal of unknown sex as *it*."), ("their", "*The dog* is singular.")], "*its* = belonging to it.")
M("d08", DIST, FB + "He came ____ in the race and won the gold medal.", [("first", ""), ("one", "A position in a race is an ordinal: *first*."), ("a first", "*came first* has no article."), ("firstly", "*firstly* is used to begin a list of points.")], "Position → ordinal *first*.")
M("d09", DIST, FB + "____ answer is correct; you have to try again.", [("Neither", ""), ("Either", "*Either answer is correct* means one is right; but you must try again."), ("Both", "*Both* needs *answers are*."), ("Each", "*Each* would mean both are correct.")], "None of the two → *Neither*.", "medium")
M("d10", DIST, FB + "Whose umbrella is this? It is ____ umbrella.", [("my", ""), ("mine", "*mine* stands alone; before a noun use *my*."), ("me", "*me* is an object pronoun."), ("I", "*I* is a subject pronoun.")], "Possessive determiner before a noun → *my*.")
# ---------- Mixed passages ----------
P1 = ("Read the passage and choose the correct option for the blank.\n\n*Last summer we visited (a) ____ beautiful valley of Kashmir. We stayed in (b) ____ houseboat on Dal Lake. (c) ____ houseboat had (d) ____ beautiful carved ceiling. We spent (e) ____ days there, and they were (f) ____ best days of our holiday.*\n\n")
M("p01", ART, P1 + "Blank (a):", [("the", ""), ("a", "*of Kashmir* tells us exactly which valley, so it is specific."), ("an", "*beautiful* begins with a consonant sound, and the valley is specific."), ("no article", "A singular countable noun needs an article.")], "*the* + noun + *of* phrase that identifies it.", "medium")
M("p02", ART, P1 + "Blank (b):", [("a", ""), ("the", "First mention: one of many houseboats."), ("an", "*houseboat* begins with a consonant sound."), ("no article", "A singular countable noun needs an article.")], "First mention → *a*.", "medium")
M("p03", ART, P1 + "Blank (c):", [("The", ""), ("A", "The houseboat has already been mentioned."), ("An", "Already mentioned → *the*."), ("Every", "We stayed in one houseboat.")], "Second mention → *the*.", "medium")
M("p04", ART, P1 + "Blank (d):", [("a", ""), ("an", "*beautiful* begins with a consonant sound."), ("the", "First mention of the ceiling, described by its quality."), ("some", "*ceiling* is singular countable.")], "First mention, consonant sound → *a*.", "medium")
M("p05", QUANT, P1 + "Blank (e):", [("a few", ""), ("a little", "*days* is countable."), ("much", "*days* is countable."), ("few", "*few* would sound negative, but they were the best days.")], "Countable + positive → *a few*.", "medium")
M("p06", ART, P1 + "Blank (f):", [("the", ""), ("a", "Superlatives take *the*."), ("an", "Superlatives take *the*."), ("no article", "Superlatives take *the*.")], "Superlative → *the*.", "medium")
# ---------- Editing ----------
E = "Identify the error and choose the correct correction: "
M("e01", ART, E + "*She is a honest girl.*", [("a → an", ""), ("honest → honesty", "*honest* (adjective) is correct."), ("is → was", "The tense is fine."), ("girl → girls", "*a/an* needs a singular noun.")], "Silent *h* → *an honest*.")
M("e02", QUANT, E + "*He gave me many advices.*", [("many advices → a lot of advice", ""), ("gave → given", "*gave* is correct."), ("me → to me", "*gave me* is correct."), ("many → much", "*advices* is still wrong; *advice* has no plural.")], "*advice* is uncountable.", "medium")
M("e03", ART, E + "*Ganga is a holy river.*", [("Ganga → The Ganga", ""), ("a → the", "*a holy river* is correct."), ("holy → holiest", "No comparison is made."), ("is → was", "It is a present fact.")], "Rivers take *the*.")
M("e04", DIST, E + "*Every students must carry an ID card.*", [("students → student", ""), ("must → musts", "Modals take no -s."), ("an → a", "*ID* starts with a vowel sound: *an*."), ("carry → carries", "Modal + V1.")], "*Every* + singular noun.")
M("e05", QUANT, E + "*There were less people at the meeting than usual.*", [("less → fewer", ""), ("were → was", "*people* is plural."), ("than → then", "*than* is used for comparison."), ("usual → usually", "*than usual* is correct.")], "Countable → *fewer*.")
M("e06", ART, E + "*She is best singer in our school.*", [("best → the best", ""), ("singer → singers", "*the best singer* is singular."), ("in → of", "*in our school* is correct."), ("our → ours", "*our school* is correct.")], "Superlative → *the best*.")
M("e07", DEM, E + "*I bought this shoes yesterday.*", [("this → these", ""), ("bought → buy", "*yesterday* needs the past *bought*."), ("shoes → shoe", "Shoes come in pairs; change the determiner, not the noun."), ("yesterday → tomorrow", "The time fits the past tense.")], "Plural noun → *these*.")
M("e08", ART, E + "*He plays the cricket every Sunday.*", [("the cricket → cricket", ""), ("plays → play", "*He plays* is correct."), ("every → each", "*every Sunday* is correct."), ("Sunday → Sundays", "*every Sunday* takes the singular.")], "Games → no article.")
# ---------- Choose the correct sentence ----------
CS = "Choose the grammatically correct sentence."
M("c01", ART, CS, [("He is an honourable man.", ""), ("He is a honourable man.", "*honourable* has a silent *h*: *an*."), ("He is honourable man.", "A singular countable noun needs an article."), ("He is the honourable man.", "Nothing makes him a specific known man.")], "Silent *h* → *an*.")
M("c02", QUANT, CS, [("Can I have some water, please?", ""), ("Can I have any water, please?", "In requests we use *some*."), ("Can I have a water, please?", "*water* is uncountable (unless you mean a bottle)."), ("Can I have many water, please?", "*water* is uncountable.")], "Requests → *some*.")
M("c03", ART, CS, [("Mount Everest is in the Himalayas.", ""), ("The Mount Everest is in the Himalayas.", "Single peaks take no article."), ("Mount Everest is in Himalayas.", "Mountain ranges need *the*."), ("The Mount Everest is in Himalayas.", "Both articles are wrong.")], "Peak → no article; range → *the*.", "medium")
M("c04", QUANT, CS, [("We have little time left; let's hurry.", ""), ("We have few time left; let's hurry.", "*time* is uncountable: *little*."), ("We have a few time left; let's hurry.", "*time* is uncountable."), ("We have many time left; let's hurry.", "*time* is uncountable.")], "Uncountable + almost none → *little*.")
# ---------- True / false ----------
C.tf("t01", ART, "We say *a university* because *university* begins with a consonant sound.", True, "*university* is pronounced *yoo-*, a consonant sound.")
C.tf("t02", QUANT, "*Few* and *a few* mean the same thing.", False, "*few* = almost none (negative); *a few* = some (positive).")
C.tf("t03", QUANT, "*Information* and *furniture* can take the plural -s.", False, "They are uncountable: *some information*, *a piece of furniture*.")
C.tf("t04", ART, "Names of games, like *cricket* and *chess*, take no article.", True, "*He plays chess.* (but *She plays the flute*.)")
C.tf("t05", DIST, "*Each* and *every* are followed by a singular noun.", True, "*each boy, every girl*.")
C.tf("t06", QUANT, "*Less* is used with countable plural nouns, as in *less students*.", False, "With countable nouns use *fewer*: *fewer students*. *Less* is for uncountables: *less sugar*.")
# ---------- Assertion-reason ----------
C.ar("ar1", ART, "*An hour* is correct.", "The choice between *a* and *an* depends on the first sound, not the first letter.", 0,
     "R explains A: the *h* in *hour* is silent.", "*hour* starts with a vowel sound.", "sound, not spelling, decides.")
C.ar("ar2", QUANT, "*She has a little knowledge of French, so she can order food in Paris* is correct.", "*a little* means *some*, a small but useful amount.", 0,
     "R explains A.", "the meaning is positive.", "*a little* = some.")
C.ar("ar3", ART, "*The Mount Abu is a hill station* is correct.", "Single mountains take no article.", 3,
     "A is false (*Mount Abu is ...*); R is true and explains why.", "*the* is wrong before a single peak.", "single peaks take no article.")
C.ar("ar4", QUANT, "*Fewer people came this year* is correct.", "*fewer* is used with uncountable nouns.", 2,
     "A is true; R is false: *fewer* is used with countable nouns.", "*people* is countable, so *fewer*.", "*fewer* goes with countables, *less* with uncountables.")

chapter = header(11, "Determiners", ["articles", "demonstratives_possessives", "quantifiers", "distributives_numbers", "determiners_in_context"],
                 "Follows the CBSE 2025-26 English Language and Literature (184) syllabus, Section B Grammar: determiners, tested through gap filling, editing and transformation.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
