"""CBSE Class 10 English Grammar Ch 3: Subject-Verb Concord. Every item lists the right answer first (see grammar_common)."""
import sys
from grammar_common import Grammar, header

ROOT = sys.argv[1]
PATH = "app_core/content/cbse/class10/english/grammar/ch03_subject_verb_concord"
C = Grammar("gram10ch03")
blk, kc, M = C.blk, C.check_block, C.mcq
BASIC, JOIN, INDEF, NOUNS, SPECIAL = ["basic_agreement"], ["joined_subjects"], ["indefinite_pronouns"], ["tricky_nouns"], ["special_patterns"]

JOINED = ("| Subject pattern | Verb agrees with | Example |\n|---|---|---|\n"
          "| A **and** B | plural | *Ravi and Sita **are** friends.* |\n"
          "| A and B = one person / one idea | singular | *Bread and butter **is** my breakfast.* *The poet and painter **has** arrived.* |\n"
          "| **Each / Every** A and B | singular | *Every boy and girl **has** a locker.* |\n"
          "| A **as well as / along with / with / together with / besides / in addition to** B | A (the first) | *The captain, along with his players, **was** honoured.* |\n"
          "| **Either** A **or** B / **Neither** A **nor** B | B (the nearer) | *Neither the teacher nor the students **were** late.* |\n"
          "| **Not only** A **but also** B | B (the nearer) | *Not only the students but also the principal **was** present.* |\n"
          "| A **of** B (a phrase between) | A (the real subject) | *The quality of these mangoes **is** excellent.* |")
NOUNS_T = ("| Always singular in meaning | Always plural | Singular or plural by meaning |\n|---|---|---|\n"
           "| news, mathematics, physics, economics, politics (as a subject), measles, mumps, billiards, ethics | scissors, trousers, spectacles, jeans, pliers, tongs, cattle, police, people, clergy | team, family, jury, committee, class, audience, staff, crowd |\n"
           "| *The news **is** good.* | *The police **have** arrested him.* *My trousers **are** torn.* | *The jury **has** given its verdict.* (one unit) / *The jury **are** divided in their opinions.* (individuals) |\n"
           "| Amounts as one total: *Ten kilometres **is** a long walk.* *Five hundred rupees **is** too much.* | *A pair of* → singular: *This pair of shoes **is** new.* | Titles of books/films: *\"Gulliver's Travels\" **is** a classic.* |")

sections = [
 {"id": "s1", "title": "Partners that must match", "blocks": [
  blk("s1.hook", "hook", title="Spot what sounds wrong",
    body="- *The box of chocolates **are** on the table.*\n- *Neither of my friends **know** the answer.*\n- *Mathematics **are** my favourite subject.*\n\n"
         "All three sound almost right, and all three are wrong. The verb must agree with its **real subject** in number (singular or plural) and person. "
         "This is called **subject-verb concord** (concord = agreement). It looks simple, but board examiners hide the real subject behind long phrases, *either/or*, *each*, *news*, *the number of*... "
         "In this chapter you will learn a short set of rules that cracks every one of these traps."),
  blk("s1.inspiration", "inspiration", title="The missile man who wrote for students", person="Dr A. P. J. Abdul Kalam", years="1931–2015",
    body="The son of a boat owner in Rameswaram, Abdul Kalam sold newspapers as a boy, studied in Tamil, and learnt English with great effort. "
         "He became India's leading rocket scientist and the 11th President of India.\n\n"
         "His autobiography *Wings of Fire*, written in plain, correct English, has inspired millions of young readers. He believed that language should be clear enough for every child to understand.",
    future="Accurate English is valued in science, defence research, administration, journalism and public speaking."),
  C.socratic("s1.socratic", "Which is correct: *The list of items ____ long.*",
    ["is", "are", "were"], 0,
    "The subject is *list* (singular), not *items*. The phrase *of items* only describes the list, so *The list ... is long.*"),
 ]},
 {"id": "s2", "title": "The basic rule and the real subject", "blocks": [
  blk("s2.thm", "theory", title="Find the real subject first", revision=True,
    body="**Rule 1:** A singular subject takes a singular verb; a plural subject takes a plural verb.\n\n"
         "| | Singular verb | Plural verb |\n|---|---|---|\n| be (present) | is | are |\n| be (past) | was | were |\n| have | has | have |\n| do | does | do |\n| other verbs (present) | V1 + s: *plays, goes* | V1: *play, go* |\n\n"
         "Remember: in the simple present, the **-s goes on the verb when the subject is singular**: *The dog bark**s**. The dogs bark.*\n\n"
         "**Rule 2: Ignore the words between the subject and the verb.** Phrases with *of, in, with, near, of which* do not change the subject:\n"
         "- *The **colour** of the flowers **is** bright.*\n- *One **of my friends** **lives** in Pune.* (subject = *one*)\n- *The **students** in the corner room **are** noisy.*\n\n"
         "**Rule 3: In questions and in sentences beginning with *There* or *Here*, the subject comes after the verb.** Look ahead to find it:\n"
         "- *There **is** a **book** on the table.* / *There **are** two **books** on the table.*\n- *Here **comes** the **bus**.* / *Here **are** your **keys**.*\n- *Where **are** my **shoes**?*"),
  kc("s2.check", "Fill in the blank: The leader of the protesters ____ been arrested.",
    [("has", ""), ("have", "The subject is *leader* (singular); *of the protesters* is only a phrase."),
     ("are", "*are been arrested* is not a correct form."), ("were", "*were been* is not a correct form.")],
    "Real subject = *leader* → *has been arrested*."),
  kc("s2.check2", "Fill in the blank: There ____ many reasons for his success.",
    [("are", ""), ("is", "The subject comes after *There*: *many reasons* is plural."),
     ("was", "*many reasons* is plural; *was* is singular."), ("has", "*There has* does not fit; we need a form of *be*.")],
    "*There* + verb + subject: *There are many reasons*."),
 ]},
 {"id": "s3", "title": "Joined subjects", "blocks": [
  blk("s3.table", "markdown_table", title="When two subjects are joined", revision=True, body=JOINED),
  blk("s3.thm", "theory", title="And, or, as well as", revision=True,
    body="- **and** usually makes the subject plural: *Gold and silver **are** precious metals.*\n"
         "- But if the two nouns name **one** person or idea, the verb is singular. Watch the article: *The secretary and treasurer **is** here.* (one person, one *the*) vs *The secretary and **the** treasurer **are** here.* (two people)\n"
         "- **as well as, along with, with, together with, besides, in addition to, accompanied by, like** do NOT add to the subject. The verb agrees with the first noun: *The teacher, as well as the students, **was** excited.*\n"
         "- **or / nor / either…or / neither…nor / not only…but also**: the verb agrees with the noun **nearer** to it: *Either you or **he is** responsible.* *Neither he nor **you are** responsible.*\n"
         "  - Tip: put the plural noun last; it sounds more natural: *Neither the coach nor the players **were** happy.*"),
  kc("s3.check", "Fill in the blank: The Prime Minister, along with his ministers, ____ expected tomorrow.",
    [("is", ""), ("are", "*along with his ministers* does not add to the subject; *the Prime Minister* is singular."),
     ("were", "The subject is singular and the time is the future."), ("have", "*have expected* changes the meaning; we need *is expected*.")],
    "*along with* → the verb agrees with the first subject."),
  kc("s3.check2", "Fill in the blank: Neither the manager nor his assistants ____ aware of the problem.",
    [("were", ""), ("was", "With *neither…nor*, the verb agrees with the nearer subject, *assistants* (plural)."),
     ("is", "*assistants* is plural."), ("has been", "*assistants* is plural; and *has been aware* changes the tense.")],
    "*neither…nor* → nearer subject: *assistants were*."),
 ]},
 {"id": "s4", "title": "Each, every, none and other pronouns", "blocks": [
  blk("s4.thm", "theory", title="Singular words that look plural", revision=True,
    body="**Always singular:** *each, every, either, neither, everyone, everybody, everything, someone, somebody, anyone, anybody, no one, nobody, nothing, one, each of, either of, neither of, many a*.\n"
         "- *Each of the girls **has** a prize.*\n- *Everyone **wants** to win.*\n- *Neither of the answers **is** correct.*\n- ***Many a** student **has** made this mistake.* (*many a* + singular noun + singular verb)\n\n"
         "**Always plural:** *both, few, many, several, a few*: *Both of them **are** absent.* *Few **were** saved.*\n\n"
         "**Singular or plural by the noun after *of*:** *some, all, most, none, any, half, a lot of, part of, a percentage/fraction of*:\n"
         "- *Most of the **cake** **is** gone.* / *Most of the **cakes** **are** gone.*\n- *Half of the **class** **is** absent.* / *Half of the **students** **are** absent.*\n"
         "- *None of the work **was** done.* With a plural noun, *none* takes a singular verb in formal writing (*None of the boys **was** there*), though *were* is common in everyday English.\n\n"
         "**the number of vs a number of**\n- ***The number of** accidents **is** rising.* (the number = one figure → singular)\n- ***A number of** students **were** absent.* (= many → plural)"),
  kc("s4.check", "Fill in the blank: Each of the players ____ given a medal.",
    [("was", ""), ("were", "*Each of* is singular, whatever noun follows."), ("have", "*Each* is singular: *has*."), ("are", "*Each* is singular.")],
    "*Each of* + plural noun + **singular** verb."),
  kc("s4.check2", "Fill in the blank: A number of trees ____ uprooted in the storm.",
    [("were", ""), ("was", "*A number of* means *many*, so the verb is plural."), ("is", "*A number of trees* is plural and the time is past."), ("has", "*has uprooted* changes the meaning, and the subject is plural.")],
    "*A number of* + plural noun → plural verb."),
 ]},
 {"id": "s5", "title": "Tricky nouns", "blocks": [
  blk("s5.table", "markdown_table", title="Nouns that break the -s rule", revision=True, body=NOUNS_T),
  blk("s5.thm", "theory", title="More special patterns", revision=True,
    body="- **The + adjective** means a group of people and is plural: *The rich **are** not always happy.* *The young **need** guidance.*\n"
         "- **Relative clauses:** *who/which/that* take the number of the noun they refer to: *She is one of those **students who work** hard.* (many students work hard; she is one of them) "
         "but *She is the only one of the students **who works** hard.*\n- **One of the + plural noun + singular verb:** *One of the **windows is** broken.*\n"
         "- **Subject = a clause or -ing form** → singular: *Swimming **is** good exercise.* *What he says **is** true.*\n"
         "- **Distances, money, time and weight as one amount** → singular: *Two hours **is** enough.* *Fifty kilograms **is** heavy.*\n"
         "- **I** takes *am/was/have*; **you** always takes the plural form: *You **are**, you **were**, you **have***, even for one person."),
  kc("s5.check", "Fill in the blank: Economics ____ my brother's favourite subject.",
    [("is", ""), ("are", "*Economics* ends in -s but is a single subject: singular."), ("were", "The subject is singular, and it is a present fact."), ("have been", "The subject is singular, and *have been* changes the meaning.")],
    "Subjects of study ending in -ics are singular."),
  kc("s5.check2", "Fill in the blank: The police ____ searching for the missing child.",
    [("are", ""), ("is", "*police* is always plural in English."), ("was", "*police* is plural: *were*, not *was*."), ("has", "*police* is plural, and *has searching* is wrong.")],
    "*police, cattle, people* are always plural."),
 ]},
 {"id": "s6", "title": "Board skills: editing and gap filling", "blocks": [
  blk("s6.worked", "worked_example", title="Editing a passage for concord",
    problem="Each line of this passage has one error. Write the incorrect word and the correction.\n\n1. The news of the floods have shocked everyone.\n2. Many villages in the district is under water.\n"
            "3. Each of the families have been given shelter.\n4. The army, along with volunteers, are helping them.\n5. A number of doctors has reached the camps.",
    steps=["Line 1: *news* is singular: **have → has**.",
           "Line 2: the subject is *villages* (plural); *in the district* is only a phrase: **is → are**.",
           "Line 3: *Each of* is singular: **have → has**.",
           "Line 4: *along with volunteers* does not add to the subject *army*: **are → is**.",
           "Line 5: *A number of* = many → plural: **has → have**."],
    answer="have → has; is → are; have → has; are → is; has → have"),
  blk("s6.worked2", "worked_example", title="Gap filling with concord",
    problem="Fill in the blanks with *is/are/was/were/has/have*:\n\n*Physics (a) ____ my favourite subject. My spectacles (b) ____ broken yesterday, so neither my notes nor my textbook (c) ____ been readable since then. Everyone in my class (d) ____ offered to help.*",
    steps=["(a) *Physics* is a single subject → **is**.", "(b) *spectacles* is always plural, and *yesterday* is past → **were**.",
           "(c) *neither…nor* → nearer subject *textbook* (singular) → **has**.", "(d) *Everyone* is singular → **has**."],
    answer="is, were, has, has"),
  kc("s6.check", "Find the error: *One of my cousins live in Australia.*",
    [("live → lives", ""), ("cousins → cousin", "*One of my cousins* needs the plural noun."), ("in → at", "*in Australia* is correct."), ("One → Ones", "*One* is correct.")],
    "The subject is *One* (singular): *lives*."),
 ]},
 {"id": "s7", "title": "Remember, avoid, practise", "blocks": [
  blk("s7.memory", "memory_trick", title="Concord in five quick checks",
    body="1. **Cross out the phrase** (*of…, with…, along with…*): what is left is the real subject.\n2. **And = add** (plural), but **as well as = ignore**.\n"
         "3. **Or / nor → nearest neighbour wins.**\n4. **Each, every, -one, -body, -thing → ONE → singular.**\n5. **\"A number\" = many (plural); \"the number\" = a figure (singular).**\n\n"
         "Remember the word **NEWS**: **N**ews, **E**conomics, **W**hat-clauses, **S**ubjects of study → all singular."),
  blk("s7.mistakes", "common_mistakes", title="Common mistakes",
    body="1. ✗ *The quality of the apples are poor.* ✓ *... is poor.*\n2. ✗ *Everyone have arrived.* ✓ *Everyone has arrived.*\n3. ✗ *Mathematics are difficult.* ✓ *Mathematics is difficult.*\n"
         "4. ✗ *The cattle is grazing.* ✓ *The cattle are grazing.*\n5. ✗ *Ram as well as his friends were there.* ✓ *... was there.*\n6. ✗ *There is many books.* ✓ *There are many books.*\n"
         "7. ✗ *The number of students are increasing.* ✓ *... is increasing.*\n8. ✗ *My scissors is blunt.* ✓ *My scissors are blunt.* (but *This pair of scissors is blunt.*)\n"
         "9. ✗ *Many a man have tried.* ✓ *Many a man has tried.*\n10. ✗ *The rich is getting richer.* ✓ *The rich are getting richer.*"),
  blk("s7.tip", "teacher_tip", title="Try this in class",
    body="Play **\"Find the boss\"**: write long sentences on the board (*The box of old letters from my grandparents ___ in the attic*). "
         "Students come up and cross out every phrase until only the \"boss\" (the real subject) and the verb remain. Then they choose *is* or *are*. "
         "Follow up with a 10-sentence editing race in pairs."),
  blk("s7.reflection", "reflection", title="Say it in your own words",
    body="Explain why we say *The teacher as well as the students was happy* but *The teacher and the students were happy*."),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 1, Tenses:** -s agreement is part of the simple present.\n- **Editing and omission:** concord errors are the second most common board error after tenses.\n"
         "- **Writing:** analytical paragraphs often use *the number of ... is*, *a majority of ... are*, *the percentage of ... has*."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="Choose the correct verb:\n\n(a) The committee (has / have) announced its decision.\n(b) Twenty kilometres (is / are) too far to walk.\n(c) Not only the boys but also the girl (was / were) praised.\n"
         "(d) She is one of the singers who (has / have) won national awards.\n(e) The bread and butter (is / are) on the plate.\n\n"
         "**Answer:** (a) **has** (one unit, *its*) (b) **is** (one distance) (c) **was** (nearer subject *girl*) (d) **have** (*who* refers to *singers*) (e) **is** (one dish)."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- The verb agrees with its real subject; ignore phrases in between.\n- *and* → plural (unless one idea); *as well as / with / along with* → first subject.\n"
         "- *or, nor, either…or, neither…nor, not only…but also* → nearer subject.\n- *each, every, either, neither, -one, -body, many a* → singular; *both, few, many, several* → plural.\n"
         "- *some/all/most/half/none of* → depends on the noun after *of*.\n- *news, -ics subjects, amounts, titles, -ing subjects* → singular; *police, cattle, people, scissors, trousers* → plural.\n"
         "- *A number of* → plural; *the number of* → singular."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- In editing, when a line has *is/are, was/were, has/have* or a verb + s, check concord first.\n- Underline the real subject before choosing an option.\n"
         "- Be careful with *there is/are*: look at the noun that comes after the verb.\n- When the subject is far from the verb, read the sentence again without the middle phrase."),
  blk("s7.flash1", "flashcard", front="*The teacher as well as the students ___ present.*", back="**was**: *as well as* does not add to the subject."),
  blk("s7.flash2", "flashcard", front="*Neither the boys nor the girl ___ come.*", back="**has**: the nearer subject *girl* is singular."),
  blk("s7.flash3", "flashcard", front="*A number of* vs *The number of*?", back="*A number of* (many) → plural; *The number of* (a figure) → singular."),
  blk("s7.flash4", "flashcard", front="*Mathematics ___ easy for her.*", back="**is**: subjects ending in -ics are singular."),
 ]},
]

FB = "Fill in the blank with the correct option: "
# ---------- Basic and real subject ----------
M("g01", BASIC, FB + "The boys ____ playing football.", [("are", ""), ("is", "*boys* is plural."), ("was", "*boys* is plural: *were*, not *was*."), ("has", "*has playing* is not a correct form.")], "Plural subject → *are*.")
M("g02", BASIC, FB + "The bunch of keys ____ on the table.", [("is", ""), ("are", "The subject is *bunch* (singular); *of keys* is a phrase."), ("were", "*bunch* is singular."), ("have", "*have on the table* has no main verb.")], "Real subject *bunch* → *is*.")
M("g03", BASIC, FB + "The houses on this street ____ very old.", [("are", ""), ("is", "The subject is *houses* (plural); *on this street* is a phrase."), ("was", "*houses* is plural."), ("has", "*has very old* is not correct.")], "Real subject *houses* → *are*.")
M("g04", BASIC, FB + "There ____ a lot of noise in the classroom.", [("was", ""), ("were", "*noise* is uncountable and singular."), ("are", "*noise* is singular."), ("have", "*There have* does not fit here.")], "*a lot of* + uncountable noun → singular.")
M("g05", BASIC, FB + "Here ____ the results of the examination.", [("are", ""), ("is", "The subject after the verb is *results* (plural)."), ("was", "*results* is plural."), ("has", "*Here has* is not a correct form.")], "*Here* + verb + plural subject → *are*.")
M("g06", BASIC, FB + "The cost of these phones ____ gone up.", [("has", ""), ("have", "The subject is *cost* (singular)."), ("are", "*are gone up* is not standard."), ("were", "*were gone* is not correct, and *cost* is singular.")], "Real subject *cost* → *has*.")
M("g07", BASIC, FB + "Where ____ my glasses?", [("are", ""), ("is", "*glasses* (spectacles) is plural."), ("was", "*glasses* is plural."), ("does", "*Where does my glasses* has no main verb.")], "Questions: find the subject after the verb.")
M("g08", BASIC, FB + "Walking in the morning ____ good for health.", [("is", ""), ("are", "An -ing subject (*Walking*) is singular."), ("were", "An -ing subject is singular, and it is a general truth."), ("have", "*have good* is not correct.")], "An -ing subject → singular.")
# ---------- Joined subjects ----------
M("g09", JOIN, FB + "My brother and my sister ____ in Canada.", [("live", ""), ("lives", "Two people joined by *and* → plural."), ("is living", "The subject is plural: *are living*."), ("has lived", "Plural subject: *have lived*.")], "A and B → plural.")
M("g10", JOIN, FB + "Rice and dal ____ my favourite meal.", [("is", ""), ("are", "*Rice and dal* here is one dish, one meal."), ("were", "It is one meal, and the time is present."), ("have", "*have my favourite meal* changes the meaning.")], "Two nouns forming one idea → singular.", "medium")
M("g11", JOIN, FB + "The principal, together with the teachers, ____ attending the function.", [("is", ""), ("are", "*together with the teachers* does not change the subject *principal*."), ("were", "The subject is singular."), ("have", "*have attending* is wrong.")], "*together with* → first subject.")
M("g12", JOIN, FB + "Either the students or the teacher ____ to blame.", [("is", ""), ("are", "With *either…or*, the nearer subject *teacher* decides."), ("were", "*teacher* is singular."), ("have", "*have to blame* changes the meaning.")], "*either…or* → nearer subject.")
M("g13", JOIN, FB + "Neither you nor I ____ responsible for this.", [("am", ""), ("are", "The nearer subject is *I*: *am*."), ("is", "*I* takes *am*."), ("were", "The sentence is in the present.")], "Nearer subject *I* → *am*.", "medium")
M("g14", JOIN, FB + "Not only the parents but also the child ____ happy.", [("was", ""), ("were", "*not only…but also* → the nearer subject *child* (singular)."), ("are", "*child* is singular."), ("have", "*have happy* is not correct.")], "*not only…but also* → nearer subject.")
M("g15", JOIN, FB + "Every man and woman ____ the right to vote.", [("has", ""), ("have", "*Every* makes each noun singular, even when joined by *and*."), ("are", "*are the right* is not correct."), ("were", "*were the right* is not correct.")], "*Every A and B* → singular.", "medium")
M("g16", JOIN, FB + "The singer and dancer ____ performing tonight.", [("is", ""), ("are", "One *The* = one person who sings and dances."), ("were", "One person, and *tonight* is future."), ("have", "*have performing* is wrong.")], "One article → one person → singular.", "hard")
M("g17", JOIN, FB + "The captain as well as the players ____ been praised.", [("has", ""), ("have", "*as well as the players* does not add to the subject *captain*."), ("are", "*are been* is not correct."), ("were", "*were been* is not correct.")], "*as well as* → first subject.")
# ---------- Indefinite pronouns and quantity words ----------
M("g18", INDEF, FB + "Everybody ____ to be appreciated.", [("wants", ""), ("want", "*Everybody* is singular."), ("are wanting", "*want* is stative, and *Everybody* is singular."), ("have wanted", "*Everybody* is singular: *has*.")], "*Everybody* → singular.")
M("g19", INDEF, FB + "Neither of the two answers ____ correct.", [("is", ""), ("are", "*Neither of* takes a singular verb in standard grammar."), ("were", "Singular subject, present time."), ("have", "*have correct* is wrong.")], "*Neither of* → singular.")
M("g20", INDEF, FB + "Both of my parents ____ doctors.", [("are", ""), ("is", "*Both* is always plural."), ("was", "*Both* is plural."), ("has", "*has doctors* changes the meaning.")], "*Both* → plural.")
M("g21", INDEF, FB + "Many a soldier ____ lost his life for the country.", [("has", ""), ("have", "*Many a* + singular noun takes a singular verb."), ("are", "*are lost* changes the meaning."), ("were", "*were lost his life* is wrong.")], "*Many a* → singular.", "medium")
M("g22", INDEF, FB + "Half of the apples ____ rotten.", [("are", ""), ("is", "*apples* (after *of*) is plural, so the verb is plural."), ("was", "*apples* is plural."), ("has", "*has rotten* is wrong.")], "*Half of* + plural noun → plural.")
M("g23", INDEF, FB + "Most of the milk ____ spilt.", [("was", ""), ("were", "*milk* is uncountable, so singular."), ("are", "*milk* is singular."), ("have", "*milk* is singular.")], "*Most of* + uncountable noun → singular.")
M("g24", INDEF, FB + "The number of road accidents ____ increasing every year.", [("is", ""), ("are", "*The number* is one figure → singular."), ("were", "*The number* is singular."), ("have", "*have increasing* is wrong.")], "*The number of* → singular.")
M("g25", INDEF, FB + "A large number of people ____ gathered outside the stadium.", [("have", ""), ("has", "*A number of* means *many* → plural."), ("is", "*is gathered* changes the meaning, and the subject is plural."), ("was", "The subject is plural.")], "*A number of* → plural.")
M("g26", INDEF, FB + "Sixty per cent of the students ____ passed with distinction.", [("have", ""), ("has", "The noun after *of* is *students* (plural)."), ("is", "*is passed* is wrong, and the subject is plural."), ("was", "The subject is plural.")], "Percentage + plural noun → plural.", "medium")
# ---------- Tricky nouns ----------
M("g27", NOUNS, FB + "The news ____ too good to be true.", [("was", ""), ("were", "*news* is always singular."), ("are", "*news* is singular."), ("have", "*have too good* is wrong.")], "*news* → singular.")
M("g28", NOUNS, FB + "The cattle ____ grazing in the field.", [("are", ""), ("is", "*cattle* is always plural."), ("was", "*cattle* is plural."), ("has", "*has grazing* is wrong.")], "*cattle* → plural.")
M("g29", NOUNS, FB + "My new trousers ____ too long.", [("are", ""), ("is", "*trousers* is always plural."), ("was", "*trousers* is plural, and it is present."), ("has", "*has too long* is wrong.")], "*trousers, scissors, spectacles* → plural.")
M("g30", NOUNS, FB + "This pair of shoes ____ very comfortable.", [("is", ""), ("are", "The subject is *pair* (singular)."), ("were", "*pair* is singular."), ("have", "*have very comfortable* is wrong.")], "*A/This pair of* → singular.")
M("g31", NOUNS, FB + "Five thousand rupees ____ a big amount for a student.", [("is", ""), ("are", "A sum of money taken as one amount is singular."), ("were", "One amount, present time."), ("have", "*have a big amount* changes the meaning.")], "Amounts as one total → singular.", "medium")
M("g32", NOUNS, FB + "The jury ____ given its verdict.", [("has", ""), ("have", "*its verdict* shows the jury is acting as one unit."), ("are", "*are given* changes the meaning."), ("were", "*were given its verdict* is wrong.")], "Collective noun as one unit → singular.", "medium")
M("g33", NOUNS, FB + "The family ____ quarrelling among themselves.", [("are", ""), ("is", "*among themselves* shows the members acting individually → plural."), ("was", "Members acting separately → plural."), ("has", "*has quarrelling* is wrong.")], "Collective noun as individuals → plural.", "hard")
M("g34", NOUNS, FB + "The poor ____ help from the government.", [("need", ""), ("needs", "*The poor* means poor people → plural."), ("is needing", "*The poor* is plural."), ("has needed", "*The poor* is plural.")], "*The + adjective* → plural.", "medium")
M("g35", NOUNS, FB + "\"The Arabian Nights\" ____ a famous collection of stories.", [("is", ""), ("are", "A book title is one thing → singular."), ("were", "One book, a present fact."), ("have", "*have a famous collection* is wrong.")], "Titles → singular.", "medium")
M("g36", SPECIAL, FB + "He is one of those boys who ____ always late.", [("are", ""), ("is", "*who* refers to *boys* (plural)."), ("was", "*who* refers to *boys*."), ("has", "*has always late* is wrong.")], "*one of those … who* + plural verb.", "hard")
M("g37", SPECIAL, FB + "She is the only one of the girls who ____ passed.", [("has", ""), ("have", "*the only one … who* → *who* refers to *one*."), ("are", "*are passed* is wrong."), ("were", "*were passed* is wrong.")], "*the only one … who* + singular verb.", "hard")
M("g38", SPECIAL, FB + "What you need ____ a good night's sleep.", [("is", ""), ("are", "A *what*-clause subject is singular."), ("were", "Singular, present."), ("have", "*have* changes the meaning.")], "Clause as subject → singular.", "medium")
# ---------- Board-style passage ----------
P1 = ("Read the passage and choose the correct option for the blank.\n\n*The Sundarbans (a) ____ home to the Royal Bengal tiger. The forest, along with its rivers, (b) ____ protected by law. Every year a number of tourists (c) ____ the area, but each of them (d) ____ to follow strict rules.*\n\n")
M("p01", NOUNS, P1 + "Blank (a):", [("is", ""), ("are", "*The Sundarbans* is the name of one place → singular."), ("were", "It is a present fact about one place."), ("have", "*have home* is wrong.")], "A place name with -s → singular.", "medium")
M("p02", JOIN, P1 + "Blank (b):", [("is", ""), ("are", "*along with its rivers* does not change the subject *forest*."), ("were", "Singular, present."), ("have", "*have protected* changes the meaning.")], "*along with* → first subject.", "medium")
M("p03", INDEF, P1 + "Blank (c):", [("visit", ""), ("visits", "*a number of tourists* = many tourists → plural."), ("visiting", "A finite verb is needed."), ("has visited", "The subject is plural.")], "*A number of* → plural.", "medium")
M("p04", INDEF, P1 + "Blank (d):", [("has", ""), ("have", "*each of them* is singular."), ("are", "*are to follow* changes the meaning, and *each* is singular."), ("were", "*each* is singular.")], "*each of* → singular.", "medium")
P2 = ("Read the passage and choose the correct option for the blank.\n\n*Mathematics (a) ____ not as difficult as it seems. Neither the formulas nor the method (b) ____ hard if you practise daily. Ten minutes (c) ____ enough to revise one topic, and the number of marks you can gain (d) ____ huge.*\n\n")
M("p05", NOUNS, P2 + "Blank (a):", [("is", ""), ("are", "*Mathematics* is a single subject → singular."), ("were", "It is a general present statement."), ("have", "*have not as difficult* is wrong.")], "-ics subjects → singular.", "medium")
M("p06", JOIN, P2 + "Blank (b):", [("is", ""), ("are", "*neither…nor* → nearer subject *method* (singular)."), ("were", "Singular, present."), ("have", "*have hard* is wrong.")], "Nearer subject → singular.", "medium")
M("p07", NOUNS, P2 + "Blank (c):", [("is", ""), ("are", "A period of time as one amount → singular."), ("were", "Singular, present."), ("have", "*have enough* changes the meaning.")], "Time as one amount → singular.", "medium")
M("p08", INDEF, P2 + "Blank (d):", [("is", ""), ("are", "*the number of …* is singular."), ("were", "Singular, present."), ("have", "*have huge* is wrong.")], "*The number of* → singular.", "medium")
# ---------- Editing ----------
E = "Identify the error and choose the correct correction: "
M("e01", BASIC, E + "*The colour of these curtains are fading.*", [("are → is", ""), ("curtains → curtain", "*these curtains* is correct; the verb is the problem."), ("fading → faded", "*is fading* is correct."), ("these → this", "*these curtains* is correct.")], "Real subject *colour* → *is*.")
M("e02", INDEF, E + "*Everyone in the room were silent.*", [("were → was", ""), ("Everyone → Every", "*Everyone* is correct as a pronoun."), ("room → rooms", "*the room* is correct."), ("silent → silence", "*silent* (adjective) is correct.")], "*Everyone* → singular.")
M("e03", NOUNS, E + "*Physics are taught by Mr Shah.*", [("are → is", ""), ("taught → teach", "*is taught* (passive) is correct."), ("by → from", "*taught by* is correct."), ("Physics → Physic", "*Physics* is the name of the subject.")], "*Physics* → singular.")
M("e04", JOIN, E + "*The teacher, with her students, are visiting the museum.*", [("are → is", ""), ("visiting → visit", "*is visiting* is correct."), ("with → and", "Changing the meaning is not needed; correct the verb."), ("her → their", "*her students* is correct.")], "*with* → first subject.")
M("e05", NOUNS, E + "*The police has caught the thief.*", [("has → have", ""), ("caught → catched", "*caught* is the correct V3."), ("the thief → thief", "*the thief* is correct."), ("police → polices", "*police* has no plural -s.")], "*police* → plural.")
M("e06", INDEF, E + "*Each of the students have submitted the form.*", [("have → has", ""), ("students → student", "*Each of the students* is correct."), ("submitted → submit", "*has submitted* is correct."), ("the form → form", "*the form* is correct.")], "*Each of* → singular.")
M("e07", BASIC, E + "*There is many problems in this plan.*", [("is → are", ""), ("many → much", "*problems* is countable: *many* is correct."), ("in → on", "*in this plan* is correct."), ("problems → problem", "*many* needs a plural noun.")], "*There* + verb + *many problems* → *are*.")
M("e08", INDEF, E + "*The number of students in the school have doubled.*", [("have → has", ""), ("number → numbers", "*The number of* is the correct phrase."), ("doubled → double", "*has doubled* is correct."), ("in → at", "*in the school* is correct.")], "*The number of* → singular.")
M("e09", JOIN, E + "*Neither the driver nor the passengers was injured.*", [("was → were", ""), ("Neither → Either", "*Neither…nor* is correct."), ("nor → or", "*nor* goes with *neither*."), ("injured → injure", "*were injured* is correct.")], "Nearer subject *passengers* → *were*.")
M("e10", INDEF, E + "*One of my friends have won a scholarship.*", [("have → has", ""), ("friends → friend", "*One of my friends* is correct."), ("won → win", "*has won* is correct."), ("a → an", "*a scholarship* is correct.")], "*One of* → singular.")
# ---------- Choose the correct sentence ----------
CS = "Choose the grammatically correct sentence."
M("c01", JOIN, CS, [("Ram, as well as his brothers, is coming.", ""), ("Ram, as well as his brothers, are coming.", "*as well as* does not add to the subject."), ("Ram, as well as his brothers, were coming.", "The subject is singular."), ("Ram, as well as his brothers, have coming.", "*have coming* is wrong.")], "*as well as* → first subject.")
M("c02", NOUNS, CS, [("The scissors are on the shelf.", ""), ("The scissors is on the shelf.", "*scissors* is plural."), ("The scissor are on the shelf.", "The noun is always *scissors*."), ("The scissors was on the shelf.", "*scissors* is plural.")], "*scissors* → plural.")
M("c03", INDEF, CS, [("Somebody has taken my pen.", ""), ("Somebody have taken my pen.", "*Somebody* is singular."), ("Somebody are taken my pen.", "*are taken* is wrong."), ("Somebody were taken my pen.", "*were taken* changes the meaning and is singular.")], "*Somebody* → singular.")
M("c04", NOUNS, CS, [("The rich are not always happy.", ""), ("The rich is not always happy.", "*The rich* = rich people → plural."), ("The riches is not always happy.", "*riches* means wealth, not people."), ("The rich was not always happy.", "Plural, and a general truth.")], "*The + adjective* → plural.", "medium")
M("c05", SPECIAL, CS, [("Gulliver's Travels is my favourite book.", ""), ("Gulliver's Travels are my favourite book.", "A title is singular."), ("Gulliver's Travels were my favourite book.", "A title is singular."), ("Gulliver's Travels have my favourite book.", "*have* changes the meaning.")], "Titles → singular.", "medium")
# ---------- True / false ----------
C.tf("t01", JOIN, "With *as well as*, the verb agrees with the first subject.", True, "*The captain as well as the players was praised.*")
C.tf("t02", INDEF, "*A number of* is followed by a singular verb.", False, "*A number of* means *many*, so the verb is plural: *A number of boys were absent.*")
C.tf("t03", NOUNS, "*News* is always singular.", True, "*The news is good.*")
C.tf("t04", JOIN, "With *neither…nor*, the verb always agrees with the first subject.", False, "It agrees with the nearer subject: *Neither he nor his friends were there.*")
C.tf("t05", NOUNS, "*Cattle* takes a plural verb.", True, "*The cattle are grazing.*")
C.tf("t06", INDEF, "*Each of the boys* takes a plural verb because *boys* is plural.", False, "The subject is *Each*, which is singular: *Each of the boys has a bag.*")
# ---------- Assertion-reason ----------
C.ar("ar1", BASIC, "*The box of pencils is on the desk* is correct.", "The verb agrees with the real subject, not with the noun in the phrase after it.", 0,
     "R explains A: the subject is *box*, so *is*.", "*box* is singular, so *is* is right.", "phrases between subject and verb are ignored.")
C.ar("ar2", NOUNS, "*Economics are a difficult subject* is correct.", "Names of subjects ending in -ics are singular.", 3,
     "A is false (*Economics is ...*); R is true and shows why.", "*Economics* needs *is*.", "-ics subjects take a singular verb.")
C.ar("ar3", INDEF, "*The number of cars on the road is increasing* is correct.", "*The number of* refers to a single figure.", 0,
     "R explains A: *the number* is one figure → singular.", "*The number of* takes *is*.", "*the number* is one figure.")
C.ar("ar4", JOIN, "*Bread and butter is a common breakfast* is correct.", "Two nouns joined by *and* always take a plural verb.", 2,
     "A is true; R is false: when two nouns form one idea, the verb is singular.", "*bread and butter* is one dish.", "*and* does not always make a plural.")

chapter = header(3, "Subject-Verb Concord", ["basic_agreement", "joined_subjects", "indefinite_pronouns", "tricky_nouns", "special_patterns"],
                 "Follows the CBSE 2025-26 English Language and Literature (184) syllabus, Section B Grammar: subject-verb concord, tested through gap filling, editing and transformation.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
