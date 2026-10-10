"""CBSE Class 10 English Grammar Ch 4: Reported Speech. Every item lists the right answer first (see grammar_common)."""
import sys
from grammar_common import Grammar, header

ROOT = sys.argv[1]
PATH = "app_core/content/cbse/class10/english/grammar/ch04_reported_speech"
C = Grammar("gram10ch04")
blk, kc, M = C.blk, C.check_block, C.mcq
CHG, STAT, QUES, CMD, DIAL = ["reporting_changes"], ["statements"], ["questions"], ["commands_requests"], ["dialogue_reporting"]

TENSES = ("| Direct speech | Reported speech | Example (*He said, \"...\"* → *He said that ...*) |\n|---|---|---|\n"
          "| simple present | simple past | *\"I **like** tea.\"* → he **liked** tea |\n| present continuous | past continuous | *\"I **am reading**.\"* → he **was reading** |\n"
          "| present perfect | past perfect | *\"I **have finished**.\"* → he **had finished** |\n| present perfect continuous | past perfect continuous | *\"I **have been waiting**.\"* → he **had been waiting** |\n"
          "| simple past | past perfect | *\"I **saw** her.\"* → he **had seen** her |\n| past continuous | past perfect continuous | *\"I **was sleeping**.\"* → he **had been sleeping** |\n"
          "| will / shall | would / should | *\"I **will** come.\"* → he **would** come |\n| can / may | could / might | *\"I **can** swim.\"* → he **could** swim |\n"
          "| must | must / had to | *\"I **must** go.\"* → he **had to** go |\n| past perfect, would, could, should, might, ought to | no change | *\"You **should** rest.\"* → I **should** rest |")
WORDS = ("| Direct | Reported |\n|---|---|\n| now | then |\n| today | that day |\n| tonight | that night |\n| yesterday | the day before / the previous day |\n"
         "| tomorrow | the next day / the following day |\n| last week | the week before / the previous week |\n| next week | the following week |\n"
         "| ago | before |\n| this / these | that / those |\n| here | there |\n| come | go (often) |")
VERBS = ("| Type of sentence | Reporting verb | Joining word | Pattern |\n|---|---|---|---|\n"
         "| Statement | said, told + object, replied, informed, added, explained | that | *She told me **that** she was busy.* |\n"
         "| Yes/no question | asked, enquired, wanted to know, wondered | if / whether | *He asked **if** I was ready.* |\n"
         "| Wh- question | asked, enquired, wanted to know | the wh- word | *She asked **where** I lived.* |\n"
         "| Command | ordered, commanded, told, directed, instructed | to / not to + V1 | *The teacher told us **to** sit down.* |\n"
         "| Request | requested, begged, asked | to / not to + V1 | *He requested me **to** help him.* |\n"
         "| Advice | advised, warned, suggested | to + V1 / that … should | *The doctor advised him **to** rest.* |\n"
         "| Exclamation / wish | exclaimed with joy/sorrow, wished, prayed | that | *She exclaimed with joy that it was a beautiful view.* |")

sections = [
 {"id": "s1", "title": "Telling what someone said", "blocks": [
  blk("s1.hook", "hook", title="How do you pass on a message?",
    body="Your friend says to you on the phone: *\"I am not well. I can't come to school today.\"* Your teacher asks why she is absent. You don't repeat her exact words; you say:\n\n"
         "*She said that she **was** not well and **couldn't** come to school **that day**.*\n\n"
         "Notice what changed: *I → she*, *am → was*, *can't → couldn't*, *today → that day*. That is **reported (indirect) speech**. "
         "Every CBSE board paper asks you to report a dialogue or complete a reported sentence, usually two or three marks' worth. Once you know the four changes, it becomes the easiest scoring question in the paper."),
  blk("s1.inspiration", "inspiration", title="The reporter of rural India", person="P. Sainath", years="born 1957",
    body="For decades, journalist P. Sainath travelled through India's villages, listening to farmers, labourers and women, and reported their words to the whole country. "
         "His book *Everybody Loves a Good Drought* became a classic of Indian journalism.\n\n"
         "He received the Ramon Magsaysay Award in 2007. A good reporter passes on people's words accurately, without changing their meaning; that is exactly what reported speech trains you to do.",
    future="Reporting skills are at the heart of journalism, law, police work, research interviews and business communication."),
  C.socratic("s1.socratic", "Riya said, \"I am tired.\" Which is the correct reported form?",
    ["Riya said that she was tired.", "Riya said that I am tired.", "Riya said that she is tired yesterday."], 0,
    "*I* becomes *she* (Riya), and *am* moves back to *was* because the reporting verb *said* is in the past."),
 ]},
 {"id": "s2", "title": "The four changes", "blocks": [
  blk("s2.thm", "theory", title="Pronouns, tense, time and place, and the joining word", revision=True,
    body="In *She said, \"I am busy today.\"*, *She said* is the **reporting verb** and *\"I am busy today\"* is the **reported speech**.\n\n"
         "When we change direct speech into indirect speech, check four things:\n\n"
         "1. **Reporting verb and joining word:** *said → said/told*; add *that*, *if/whether*, a wh- word, or *to*.\n"
         "2. **Pronouns** change to fit the new speaker: *\"I love **my** dog,\" said Ravi.* → *Ravi said that **he** loved **his** dog.* Use the **SON** rule: **S**ubject-pronoun (I, we) changes to match the **s**ubject of the reporting verb; "
         "**O**bject-pronoun (you) changes to match the **o**bject; **N**o change for third-person pronouns (he, she, they).\n"
         "3. **Tense moves one step back** when the reporting verb is in the past (*said, told, asked*).\n4. **Time and place words** change: *now → then, today → that day, here → there*.\n\n"
         "**When the tense does NOT change:**\n- The reporting verb is in the present or future: *He **says**, \"I **am** busy.\"* → *He **says** that he **is** busy.*\n"
         "- The reported speech is a universal truth, a habitual fact or a proverb: *The teacher said, \"The sun **rises** in the east.\"* → *... that the sun **rises** in the east.*\n"
         "- The direct speech already has *would, could, should, might, ought to, had (past perfect)*."),
  blk("s2.tenses", "markdown_table", title="Tense change (backshift)", revision=True, body=TENSES),
  blk("s2.words", "markdown_table", title="Time and place words", revision=True, body=WORDS),
  kc("s2.check", "He said, \"I will meet you tomorrow.\" → He said that he ____ me ____.",
    [("would meet, the next day", ""), ("will meet, tomorrow", "After *said*, *will → would* and *tomorrow → the next day*."),
     ("would meet, tomorrow", "*tomorrow* must change to *the next day*."), ("will meet, the next day", "*will* must change to *would*.")],
    "*will → would*; *tomorrow → the next day*."),
 ]},
 {"id": "s3", "title": "Reporting statements", "blocks": [
  blk("s3.thm", "theory", title="said or told?", revision=True,
    body="- **said** has no object, or *said to* + object: *He **said** (to me) that he was hungry.*\n- **told** must have an object: *He **told me** that he was hungry.* (✗ *He told that ...*, ✗ *He said me ...*)\n"
         "- In indirect speech, *said to me* usually becomes **told me**.\n\n"
         "Other useful reporting verbs for statements: *replied, answered, informed, added, explained, admitted, complained, promised, assured, remarked*. Board examiners reward a precise verb: "
         "*\"Yes, I broke the vase,\" said Raju.* → *Raju **admitted** that he **had broken** the vase.*\n\n"
         "**Worked steps:** *Meena said to me, \"I have lost my book here.\"*\n1. *said to me* → **told me**; add **that**.\n2. *I → she* (Meena); *my → her*.\n3. *have lost → had lost*.\n4. *here → there*.\n\n"
         "→ *Meena told me that she had lost her book there.*"),
  kc("s3.check", "Mother said to me, \"You must finish your homework now.\" → Mother told me that I ____ my homework ____.",
    [("had to finish, then", ""), ("must finish, now", "*now* must change to *then*, and *must* (obligation) usually becomes *had to*."),
     ("have to finish, then", "After *told*, the tense goes back: *had to*."), ("had finished, then", "That changes the meaning: she gave an instruction, not news of a finished action.")],
    "*must* (obligation) → *had to*; *now → then*; *You → I*."),
 ]},
 {"id": "s4", "title": "Reporting questions", "blocks": [
  blk("s4.thm", "theory", title="Questions become statements", revision=True,
    body="When we report a question, it **stops being a question**:\n- Use *asked, enquired, wanted to know, wondered*.\n- **Word order becomes subject + verb** (like a statement).\n"
         "- **No question mark** at the end, and **no *do/does/did***.\n\n"
         "**Yes/no questions** (starting with a helping verb: *Is, Are, Do, Did, Can, Will, Have ...*) → use **if** or **whether**:\n"
         "*He said to me, \"**Are you** coming?\"* → *He asked me **if I was** coming.*\n*She said, \"**Do you** like music?\"* → *She asked **whether I liked** music.*\n\n"
         "**Wh- questions** (*what, where, when, why, who, how, which*) → keep the wh- word, then subject + verb:\n"
         "*The teacher said, \"**Where do you live**?\"* → *The teacher asked me **where I lived**.*\n*He said, \"**Why did you come** late?\"* → *He asked me **why I had come** late.*\n\n"
         "✗ *He asked me where did I live.* ✓ *He asked me where I lived.*\n✗ *She asked me that if I was ready.* ✓ *She asked me if I was ready.*"),
  kc("s4.check", "Rohan said to Priya, \"Where are you going?\" → Rohan asked Priya ____.",
    [("where she was going", ""), ("where was she going", "Reported questions use statement order: subject + verb."),
     ("where she is going", "After *asked*, *is* moves back to *was*."), ("that where she was going", "No *that* before a wh- word.")],
    "wh- word + subject + verb, tense moved back."),
  kc("s4.check2", "The shopkeeper said to me, \"Do you want a bag?\" → The shopkeeper asked me ____.",
    [("if I wanted a bag", ""), ("do I want a bag", "Reported questions lose *do* and the question order."),
     ("if I want a bag", "After *asked*, *want → wanted*."), ("that I wanted a bag", "A yes/no question takes *if/whether*, not *that*.")],
    "Yes/no question → *if/whether* + subject + verb, tense moved back."),
 ]},
 {"id": "s5", "title": "Reporting commands and requests", "blocks": [
  blk("s5.verbs", "markdown_table", title="Choosing the reporting verb", revision=True, body=VERBS),
  blk("s5.thm", "theory", title="to + V1 and not to + V1", revision=True,
    body="Imperative sentences (orders, requests, advice) are reported with a verb that shows the **tone**, then **to + V1**:\n\n"
         "- Command: *The officer said to the soldiers, \"Stand still.\"* → *The officer **ordered** the soldiers **to stand** still.*\n"
         "- Request (*please*): *She said to me, \"Please lend me your pen.\"* → *She **requested** me **to lend** her my pen.* (*please* disappears; *requested* carries the politeness)\n"
         "- Negative command: *Mother said, \"Don't touch the stove.\"* → *Mother **told** me **not to touch** the stove.* (*Don't* → *not to*)\n"
         "- Advice: *The doctor said, \"You should rest.\"* → *The doctor **advised** him **to rest**.*\n- Warning: *\"Don't swim here,\" said the guard.* → *The guard **warned** us **not to swim** there.*\n"
         "- Suggestion with *Let's*: *He said, \"Let's play chess.\"* → *He **suggested that we should play** chess.* (or *suggested playing chess*). ✗ *suggested us to play*\n\n"
         "**Polite questions that are really requests** (*Could you…? Will you…? Would you…?*) are usually reported with *requested/asked + to*: "
         "*\"Could you open the window?\"* → *She **requested** me **to open** the window.*"),
  kc("s5.check", "The teacher said to the students, \"Don't make a noise.\" → The teacher ____ the students ____ a noise.",
    [("told, not to make", ""), ("told, don't make", "*Don't* changes to *not to* in reported speech."),
     ("said, not to make", "*said* cannot take a direct object like *the students*."), ("told, to not making", "The pattern is *not to* + V1.")],
    "Negative command → *told/ordered + object + not to + V1*."),
  kc("s5.check2", "He said, \"Let us go for a picnic.\" → He ____ go for a picnic.",
    [("suggested that we should", ""), ("suggested us to", "*suggest* is never followed by object + *to*."),
     ("ordered us to", "*Let us* is a suggestion, not an order."), ("said let us", "The words of the speaker must be reported, not repeated.")],
    "*Let us/Let's* → *suggested that we should* + V1 (or *suggested going*)."),
 ]},
 {"id": "s6", "title": "Board skills: reporting a dialogue", "blocks": [
  blk("s6.thm", "theory", title="How the board asks it", revision=True,
    body="The board usually gives a short dialogue and asks you to **complete** the reported version, or to choose the correct reported sentence. Example:\n\n"
         "*Customer: Can you show me a cheaper phone?*\n*Shopkeeper: I'm afraid this is the cheapest one we have.*\n\n"
         "Report: *The customer asked the shopkeeper **if he could show him a cheaper phone**. The shopkeeper replied **that he was afraid that was the cheapest one they had**.*\n\n"
         "**Checklist before you write:**\n1. What type of sentence is it? (statement / question / command / request)\n2. Which reporting verb and joining word?\n3. Pronouns: who is speaking to whom?\n"
         "4. Tense one step back.\n5. Time and place words.\n6. Question → statement order, no *?*, no *do/did*."),
  blk("s6.worked", "worked_example", title="Reporting a dialogue step by step",
    problem="Report the dialogue:\n\n*Teacher: Why didn't you submit your project yesterday, Aman?*\n*Aman: I was ill, Ma'am. I will submit it tomorrow.*\n*Teacher: Make sure you bring a medical certificate.*",
    steps=["Line 1 is a wh- question → *asked Aman why*; *didn't you submit* → *he had not submitted* (no *did*, past → past perfect); *yesterday → the day before*.",
           "→ *The teacher asked Aman why he had not submitted his project the day before.*",
           "Line 2 is a statement → *replied (respectfully) that*; *I was ill → he had been ill*; *I will submit → he would submit*; *tomorrow → the next day*.",
           "→ *Aman replied respectfully that he had been ill and that he would submit it the next day.*",
           "Line 3 is a command/advice → *told/instructed him to make sure he brought*.",
           "→ *The teacher told him to make sure that he brought a medical certificate.*"],
    answer="The teacher asked Aman why he had not submitted his project the day before. Aman replied respectfully that he had been ill and would submit it the next day. The teacher told him to make sure that he brought a medical certificate."),
  blk("s6.worked2", "worked_example", title="Editing a reported sentence",
    problem="Correct the errors:\n\n1. She asked me where did I live.\n2. He told that he was tired.\n3. The doctor advised me that take rest.\n4. I asked him whether is he ready.",
    steps=["1. Statement order, no *did*: **where I lived**.", "2. *told* needs an object: **told me that** (or *said that*).",
           "3. Advice → *to* + V1: **advised me to take rest**.", "4. Statement order: **whether he was ready**."],
    answer="where I lived; told me / said that; advised me to take rest; whether he was ready"),
  kc("s6.check", "Neha: \"Have you seen my keys?\" → Neha asked me ____.",
    [("whether I had seen her keys", ""), ("whether had I seen her keys", "Use statement order: *I had seen*."),
     ("whether I have seen my keys", "*have seen → had seen*, and *my → her* (Neha's keys)."), ("that I had seen her keys", "A yes/no question takes *if/whether*.")],
    "Yes/no question → *whether* + statement order; present perfect → past perfect; *my → her*."),
 ]},
 {"id": "s7", "title": "Remember, avoid, practise", "blocks": [
  blk("s7.memory", "memory_trick", title="The \"P-T-T-W\" check",
    body="Before writing any reported sentence, tick **P-T-T-W**:\n- **P**ronouns: who is speaking to whom?\n- **T**ense: one step back (*is → was, was → had been, will → would*).\n"
         "- **T**ime/place: *now → then, today → that day, here → there*.\n- **W**ord to join: *that* (statement), *if/whether* (yes/no), wh- (wh- question), *to / not to* (command).\n\n"
         "**Question → statement**: drop the *?*, drop *do/did*, put the subject before the verb.\n**Don't → not to.** **Please → requested.** **Let's → suggested that we should.**"),
  blk("s7.mistakes", "common_mistakes", title="Common mistakes",
    body="1. ✗ *He told that ...* ✓ *He told me that ... / He said that ...*\n2. ✗ *She asked me where was I going.* ✓ *She asked me where I was going.*\n"
         "3. ✗ *He asked me that if I was ready.* ✓ *He asked me if I was ready.*\n4. ✗ *Mother told me don't go out.* ✓ *Mother told me not to go out.*\n"
         "5. ✗ *She requested me please to help.* ✓ *She requested me to help her.*\n6. ✗ *He said that he will come tomorrow.* ✓ *He said that he would come the next day.*\n"
         "7. ✗ *The teacher said that the earth moved round the sun.* ✓ *... moves round the sun.*\n8. ✗ *He suggested us to go.* ✓ *He suggested that we should go.*\n"
         "9. ✗ *She asked did I like it.* ✓ *She asked if I liked it.*\n10. Forgetting the pronoun: ✗ *Ravi said that I was hungry* (when Ravi meant himself) ✓ *Ravi said that he was hungry.*"),
  blk("s7.tip", "teacher_tip", title="Try this in class",
    body="Play **\"Chinese whispers with grammar\"**: student A whispers a sentence to B (*\"I'll bring my guitar tomorrow\"*); B reports it aloud to the class (*\"Aditi said that she would bring her guitar the next day\"*). "
         "The class checks P-T-T-W. Then use real dialogues from the First Flight chapters (e.g. *The Proposal*) and report them line by line."),
  blk("s7.reflection", "reflection", title="Say it in your own words",
    body="Why does *\"Where do you live?\"* become *where I lived* and not *where did I live*? Explain the rule to a friend."),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 1, Tenses:** the sequence of tenses drives every backshift.\n- **Chapter 2, Modals:** *can → could, may → might, will → would, must → had to*.\n"
         "- **Literature:** questions on *The Proposal*, *Madam Rides the Bus* and *Two Gentlemen of Verona* often ask what a character said: answer in reported speech."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="Report the dialogue:\n\n*Passenger: Excuse me, does this bus go to the railway station?*\n*Conductor: Yes, it does. Please sit down; we are leaving now.*\n\n"
         "**Answer:** *The passenger politely asked the conductor whether that bus went to the railway station. The conductor replied that it did, and requested him to sit down as they were leaving then.*"),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- Reported speech passes on someone's words without quoting them.\n- Change pronouns, move the tense back (after a past reporting verb), change time/place words, and add the right joining word.\n"
         "- Statements → *said/told + that*; yes/no questions → *asked + if/whether*; wh- questions → *asked + wh-*; commands/requests → *told/ordered/requested + (not) to + V1*.\n"
         "- Reported questions use statement order, no *do/did*, no question mark.\n- No backshift when the reporting verb is present/future, or for universal truths."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- Use a precise reporting verb (*requested, ordered, advised, enquired, replied, exclaimed*); it shows understanding.\n- Never put a question mark at the end of a reported question.\n"
         "- When completing a reported sentence, copy the given beginning exactly and continue from it.\n- Check that your final sentence is grammatical on its own: read it aloud in your head."),
  blk("s7.flash1", "flashcard", front="\"Are you ready?\" he asked me. →", back="He asked me **if/whether I was** ready."),
  blk("s7.flash2", "flashcard", front="\"Don't run,\" the teacher said to us. →", back="The teacher **told us not to run**."),
  blk("s7.flash3", "flashcard", front="Reported form of *tomorrow*, *here*, *now*?", back="*the next day*, *there*, *then*."),
  blk("s7.flash4", "flashcard", front="\"I can swim,\" said Asha. →", back="Asha said that she **could** swim."),
 ]},
]

R = "Choose the correct reported form: "
# ---------- Changes ----------
M("g01", CHG, R + "Amit said, \"I am hungry.\" → Amit said that ____.", [("he was hungry", ""), ("I was hungry", "*I* refers to Amit, so it becomes *he*."), ("he is hungry", "After *said*, *am → was*."), ("he had hungry", "*had hungry* is not a correct form.")], "Pronoun *I → he*; *am → was*.")
M("g02", CHG, R + "She said, \"I am writing a letter.\" → She said that she ____ a letter.", [("was writing", ""), ("is writing", "Present continuous → past continuous after *said*."), ("had written", "That changes the meaning to a finished action."), ("wrote", "The continuous aspect must be kept: *was writing*.")], "Present continuous → past continuous.")
M("g03", CHG, R + "He said, \"I have finished my work.\" → He said that he ____ his work.", [("had finished", ""), ("has finished", "Present perfect → past perfect."), ("finished", "The backshift of *have finished* is *had finished*."), ("have finished", "*he* takes *had* after the backshift.")], "Present perfect → past perfect.")
M("g04", CHG, R + "Ravi said, \"I met her yesterday.\" → Ravi said that he ____ her ____.", [("had met, the day before", ""), ("met, yesterday", "Simple past → past perfect, and *yesterday → the day before*."), ("had met, yesterday", "*yesterday* must change."), ("has met, the day before", "*has met* is present perfect.")], "Simple past → past perfect; *yesterday → the day before*.", "medium")
M("g05", CHG, R + "The girl said, \"I can dance.\" → The girl said that she ____ dance.", [("could", ""), ("can", "After *said*, *can → could*."), ("might", "*can* (ability) → *could*, not *might*."), ("would", "*can → could*.")], "*can → could*.")
M("g06", CHG, R + "He said, \"I may be late.\" → He said that he ____ be late.", [("might", ""), ("may", "After *said*, *may → might*."), ("could", "*may* (possibility) → *might*."), ("must", "*must* changes the meaning to certainty.")], "*may → might*.")
M("g07", CHG, R + "Father says, \"I am proud of you.\" → Father says that he ____ proud of me.", [("is", ""), ("was", "The reporting verb *says* is present, so the tense does not change."), ("had been", "No backshift after a present reporting verb."), ("were", "*he* takes *is/was*, and there is no backshift.")], "Present reporting verb → no tense change.", "medium")
M("g08", CHG, R + "The teacher said, \"Honesty is the best policy.\" → The teacher said that honesty ____ the best policy.", [("is", ""), ("was", "A proverb or universal truth keeps the present."), ("had been", "Universal truths do not change."), ("will be", "There is no future idea here.")], "Universal truths → no change.")
M("g09", CHG, R + "She said, \"I was reading when you called.\" → She said that she ____ when I had called.", [("had been reading", ""), ("was reading", "Past continuous → past perfect continuous in strict reported speech."), ("is reading", "The time is past."), ("had read", "The continuous meaning must be kept.")], "Past continuous → past perfect continuous.", "hard")
M("g10", CHG, R + "He said, \"I will leave this place now.\" → He said that he would leave ____ place ____.", [("that, then", ""), ("this, now", "*this → that*, *now → then*."), ("that, now", "*now → then*."), ("this, then", "*this → that*.")], "*this → that*; *now → then*.", "medium")
M("g11", CHG, R + "Mohan said to me, \"You should work hard.\" → Mohan told me that I ____ work hard.", [("should", ""), ("shall", "*should* does not change in reported speech."), ("would", "*should* stays *should*."), ("must have", "*must have* changes the meaning.")], "*should, would, could, might* do not change.", "medium")
# ---------- Statements ----------
M("s01", STAT, R + "Rina said to me, \"I like your dress.\" → Rina ____.", [("told me that she liked my dress", ""), ("said me that she liked my dress", "*said* cannot take *me* directly: use *told me*."), ("told me that I liked your dress", "*I → she* (Rina) and *your → my*."), ("told that she liked my dress", "*told* needs an object: *told me*.")], "*said to me → told me*; pronouns follow the speaker and listener.", "medium")
M("s02", STAT, R + "\"We are going to Goa next week,\" said the boys. → The boys said that they ____ to Goa ____.", [("were going, the following week", ""), ("are going, next week", "Tense and time words must change."), ("were going, next week", "*next week → the following week*."), ("had gone, the following week", "*are going* (plan) → *were going*, not *had gone*.")], "*are going → were going*; *next week → the following week*.", "medium")
M("s03", STAT, R + "\"Yes, I broke the window,\" said Raju. → Raju ____ that he had broken the window.", [("admitted", ""), ("ordered", "Raju is confessing, not giving an order."), ("requested", "Nothing is being requested."), ("asked", "It is a statement, not a question.")], "A confession → *admitted*.", "medium")
M("s04", STAT, R + "\"I'll help you with maths,\" my brother said to me. → My brother ____ me that he would help me with maths.", [("promised", ""), ("ordered", "An offer of help is a promise, not an order."), ("enquired", "*enquired* is for questions."), ("begged", "*begged* is for urgent requests.")], "An offer/assurance → *promised*.", "medium")
M("s05", STAT, R + "The guide said, \"The museum was built in 1890.\" → The guide said that the museum ____ built in 1890.", [("had been", ""), ("has been", "Simple past (passive) → past perfect (passive)."), ("is", "The building happened in the past."), ("will be", "There is no future meaning.")], "*was built → had been built* (a historical fact may also stay *was built*).", "hard")
# ---------- Questions ----------
M("q01", QUES, R + "He said to me, \"Are you happy?\" → He asked me ____.", [("if I was happy", ""), ("if was I happy", "Statement order: *I was*."), ("that I was happy", "A yes/no question takes *if/whether*."), ("if you were happy", "*you* (me) → *I*.")], "Yes/no → *if* + subject + verb.")
M("q02", QUES, R + "The teacher said to Tina, \"Why are you late?\" → The teacher asked Tina ____.", [("why she was late", ""), ("why was she late", "Statement order: *she was*."), ("why she is late", "*is → was* after *asked*."), ("that why she was late", "No *that* before a wh- word.")], "wh- word + statement order + backshift.")
M("q03", QUES, R + "She said to me, \"Do you know French?\" → She asked me ____ French.", [("whether I knew", ""), ("do I know", "Reported questions lose *do* and the question order."), ("whether I know", "*know → knew* after *asked*."), ("whether did I know", "No *did* in a reported question.")], "Yes/no with *do* → *whether* + past simple.")
M("q04", QUES, R + "He said, \"Where did you buy this?\" → He asked me where I ____ that.", [("had bought", ""), ("did buy", "*did* disappears in reported questions."), ("bought", "Simple past → past perfect: *had bought*."), ("have bought", "The backshift of *did buy* is *had bought*.")], "*did + V1 → had + V3*.", "medium")
M("q05", QUES, R + "\"How old are you?\" the doctor asked the boy. → The doctor asked the boy ____.", [("how old he was", ""), ("how old was he", "Statement order: *he was*."), ("how old he is", "*is → was*."), ("how old were you", "*you → he*, and statement order.")], "wh- question → statement order.")
M("q06", QUES, R + "\"Can you lend me a pen?\" Arjun asked Meera. → Arjun asked Meera ____ lend him a pen.", [("if she could", ""), ("can she", "Statement order: *she could*."), ("if she can", "*can → could*."), ("that she could", "A yes/no question takes *if/whether*.")], "*Can you …?* → *if she could*.", "medium")
M("q07", QUES, R + "\"Who broke this vase?\" Mother asked. → Mother asked ____ that vase.", [("who had broken", ""), ("who broke", "Simple past → past perfect: *had broken*."), ("who did break", "No *did* in reported questions."), ("who has broken", "The backshift is *had broken*.")], "*who* is the subject; *broke → had broken*.", "hard")
M("q08", QUES, R + "\"Will you come to my party?\" said Neha to Pooja. → Neha asked Pooja ____.", [("whether she would come to her party", ""), ("whether will she come to my party", "Statement order, and *my → her*."), ("whether she will come to her party", "*will → would*."), ("that she would come to her party", "Yes/no → *whether*.")], "*will → would*; *my → her* (Neha's).", "medium")
M("q09", QUES, R + "\"What are you doing here?\" the guard said to the boys. → The guard asked the boys what they ____.", [("were doing there", ""), ("were doing here", "*here → there*."), ("are doing there", "*are → were*."), ("was doing there", "*they* takes *were*.")], "*are doing → were doing*; *here → there*.", "medium")
M("q10", QUES, R + "\"Have you ever been to Shimla?\" my uncle asked me. → My uncle asked me if I ____ to Shimla.", [("had ever been", ""), ("have ever been", "Present perfect → past perfect."), ("ever had been", "*ever* comes after the helping verb: *had ever been*."), ("was ever", "The backshift of *have been* is *had been*.")], "Present perfect → past perfect.", "medium")
# ---------- Commands and requests ----------
M("c01", CMD, R + "The officer said to the soldiers, \"Fire!\" → The officer ____ the soldiers to fire.", [("ordered", ""), ("requested", "*Fire!* is a command, not a polite request."), ("advised", "It is an order, not advice."), ("suggested", "*suggest* never takes object + *to*.")], "A command → *ordered/commanded*.")
M("c02", CMD, R + "She said to me, \"Please help me.\" → She ____.", [("requested me to help her", ""), ("requested me please help her", "*please* is dropped; use *to* + V1."), ("ordered me to help her", "*Please* shows a request, not an order."), ("requested me to help me", "*me* (the speaker) → *her*.")], "Request → *requested + object + to + V1*.")
M("c03", CMD, R + "The doctor said to him, \"Don't eat junk food.\" → The doctor advised him ____ junk food.", [("not to eat", ""), ("don't eat", "*Don't* → *not to*."), ("to not eating", "Use *not to* + V1."), ("not eat", "*advised him not eat* misses *to*.")], "Negative advice → *not to* + V1.")
M("c04", CMD, R + "\"Let's watch a movie,\" said Kiran. → Kiran ____ watch a movie.", [("suggested that they should", ""), ("suggested them to", "*suggest* never takes object + *to*."), ("ordered them to", "*Let's* is a suggestion."), ("said let's", "Reported speech must not repeat the exact words.")], "*Let's* → *suggested that we/they should*.", "medium")
M("c05", CMD, R + "The teacher said, \"Open your books, children.\" → The teacher ____ the children to open their books.", [("told", ""), ("said", "*said* cannot take an object like *the children* + *to*."), ("asked that", "*asked that* + *to* is wrong."), ("enquired", "*enquired* is for questions.")], "*told + object + to + V1*.")
M("c06", CMD, R + "\"Could you please close the door?\" the old man said to me. → The old man ____ the door.", [("requested me to close", ""), ("asked me could I close", "A polite request is reported with *requested/asked + to*."), ("ordered me to close", "*Could you please* is polite, not an order."), ("requested me that close", "The pattern is *requested me to close*.")], "Polite question-request → *requested + to*.", "medium")
M("c07", CMD, R + "\"Don't swim in the lake,\" the guard said to us. → The guard ____ swim in the lake.", [("warned us not to", ""), ("warned us to not", "The standard pattern is *not to*."), ("told us don't", "*don't* → *not to*."), ("suggested us not to", "*suggest* never takes object + *to*.")], "Warning → *warned + object + not to + V1*.", "medium")
# ---------- Dialogue reporting (board style) ----------
D1 = ("Read the dialogue and choose the option that correctly completes the reported version.\n\n*Ravi: Mother, can I go to the cinema tonight?*\n*Mother: No, you have an exam tomorrow.*\n\n")
M("d01", DIAL, D1 + "Ravi asked his mother ____ to the cinema that night.", [("if he could go", ""), ("can I go", "Reported questions use statement order and backshift."), ("if he can go", "*can → could*."), ("that he could go", "A yes/no question takes *if*.")], "*can I → if he could*.", "medium")
M("d02", DIAL, D1 + "His mother refused and said that ____.", [("he had an exam the next day", ""), ("you have an exam tomorrow", "Pronoun, tense and time must change."), ("he has an exam tomorrow", "*has → had*; *tomorrow → the next day*."), ("he had an exam tomorrow", "*tomorrow* must change to *the next day*.")], "*you have → he had*; *tomorrow → the next day*.", "medium")
D2 = ("Read the dialogue and choose the option that correctly completes the reported version.\n\n*Customer: How much does this shirt cost?*\n*Shopkeeper: It costs five hundred rupees. Would you like to try it on?*\n\n")
M("d03", DIAL, D2 + "The customer asked the shopkeeper ____.", [("how much that shirt cost", ""), ("how much does this shirt cost", "No *does*, statement order, and *this → that*."), ("how much did that shirt cost", "No *did* in reported questions."), ("that how much that shirt cost", "No *that* before *how much*.")], "wh- question → statement order without *does*.", "hard")
M("d04", DIAL, D2 + "The shopkeeper replied that it cost five hundred rupees and asked ____.", [("if he would like to try it on", ""), ("would he like to try it on", "Statement order: *he would like*."), ("if you would like to try it on", "*you → he* (the customer)."), ("that he would like to try it on", "A yes/no question takes *if*.")], "*Would you like …?* → *if he would like …*.", "hard")
D3 = ("Read the dialogue and choose the option that correctly completes the reported version.\n\n*Coach: Run faster, Meera! Don't stop now.*\n*Meera: I am trying my best, sir.*\n\n")
M("d05", DIAL, D3 + "The coach urged Meera ____.", [("to run faster and not to stop then", ""), ("run faster and don't stop now", "Commands → *to* + V1; *Don't* → *not to*; *now → then*."), ("to run faster and not stop now", "*now → then*, and *not to stop*."), ("that she runs faster", "Commands are reported with *to* + V1.")], "Commands → *to / not to* + V1; *now → then*.", "hard")
M("d06", DIAL, D3 + "Meera replied respectfully that ____.", [("she was trying her best", ""), ("I am trying my best", "Pronouns and tense must change."), ("she is trying her best", "*am trying → was trying*."), ("she was trying my best", "*my → her*.")], "*I am trying my → she was trying her*.", "medium")
D4 = ("Read the dialogue and choose the option that correctly completes the reported version.\n\n*Principal: Who painted this beautiful poster?*\n*Sana: I did, ma'am. I made it for the science exhibition.*\n\n")
M("d07", DIAL, D4 + "The principal asked ____.", [("who had painted that beautiful poster", ""), ("who painted this beautiful poster?", "No question mark; *this → that*; *painted → had painted*."), ("who did paint that beautiful poster", "No *did* in reported questions."), ("that who had painted that poster", "No *that* before *who*.")], "*who painted → who had painted*; *this → that*.", "hard")
M("d08", DIAL, D4 + "Sana replied politely that ____ for the science exhibition.", [("she had painted it and had made it", ""), ("I did and I made it", "Pronouns and tense must change."), ("she did and she makes it", "Past → past perfect, not present."), ("she has painted it and made it", "*has* is present perfect; use *had*.")], "*I did / I made → she had painted / had made*.", "hard")
D5 = ("Read the dialogue and choose the option that correctly completes the reported version.\n\n*Grandfather: Switch off the fan when you leave the room.*\n*Kunal: Sorry, Dadaji, I forgot. I will remember next time.*\n\n")
M("d09", DIAL, D5 + "Grandfather told Kunal ____ the fan when he left the room.", [("to switch off", ""), ("switch off", "Commands → *to* + V1."), ("that switch off", "Commands are not reported with *that* + V1."), ("not to switch off", "Grandfather wants the fan switched off.")], "Command → *to* + V1.", "medium")
M("d10", DIAL, D5 + "Kunal apologised, saying that he ____ and that he ____ the next time.", [("had forgotten, would remember", ""), ("forgot, will remember", "Both verbs must move back."), ("has forgotten, would remember", "*forgot → had forgotten*."), ("had forgotten, will remember", "*will → would*.")], "*forgot → had forgotten*; *will → would*.", "hard")
D6 = ("Read the dialogue and choose the option that correctly completes the reported version.\n\n*Interviewer: How long have you been playing chess?*\n*Gukesh: Since I was seven. I practise for six hours every day.*\n\n")
M("d11", DIAL, D6 + "The interviewer asked Gukesh how long ____ chess.", [("he had been playing", ""), ("have you been playing", "Statement order and pronoun change are needed."), ("he has been playing", "Present perfect continuous → past perfect continuous."), ("had he been playing", "Statement order: *he had been playing*.")], "*have you been playing → he had been playing*.", "hard")
M("d12", DIAL, D6 + "Gukesh replied that he had been playing since he was seven and that he ____ for six hours every day.", [("practised", ""), ("practise", "*practise* is the base form; after *replied* it moves back to *practised*."), ("had been practise", "Not a correct form."), ("is practising", "*is* is present; and the habit is reported in the past.")], "*I practise → he practised*.", "medium")
D7 = ("Read the dialogue and choose the option that correctly completes the reported version.\n\n*Tourist: Excuse me, is there a good restaurant near here?*\n*Policeman: Yes, there is one at the end of this road.*\n\n")
M("d13", DIAL, D7 + "The tourist politely asked the policeman ____.", [("if there was a good restaurant near there", ""), ("is there a good restaurant near here", "Statement order, backshift, *here → there*."), ("if there is a good restaurant near here", "*is → was*; *here → there*."), ("if was there a good restaurant near there", "Statement order: *there was*.")], "*is there → if there was*; *here → there*.", "hard")
M("d14", DIAL, D7 + "The policeman replied that there was one at the end of ____ road.", [("that", ""), ("this", "*this → that* in reported speech."), ("these", "*road* is singular, and *this → that*."), ("those", "*road* is singular: *that*.")], "*this → that*.", "medium")
D8 = ("Read the dialogue and choose the option that correctly completes the reported version.\n\n*Sister: Please don't tell Mummy that I broke her cup.*\n*Brother: All right, but you must tell her yourself.*\n\n")
M("d15", DIAL, D8 + "The sister begged her brother ____ that she had broken her cup.", [("not to tell Mummy", ""), ("please don't tell Mummy", "*Please don't* → *not to*."), ("to not telling Mummy", "Use *not to* + V1."), ("that don't tell Mummy", "Requests are reported with *(not) to* + V1.")], "Negative request → *begged + object + not to + V1*.", "medium")
M("d16", DIAL, D8 + "The brother agreed, but said that she ____ tell her herself.", [("had to", ""), ("must to", "*must* takes no *to*."), ("has to", "*has to* is present; after *said*, *must → had to*."), ("can", "*must* (obligation) does not become *can*.")], "*must → had to* (obligation).", "medium")
# ---------- Editing ----------
E = "Identify the error and choose the correct correction: "
M("e01", QUES, E + "*She asked me where was I going.*", [("was I going → I was going", ""), ("asked → told", "*asked* is right for a question."), ("where → that", "Keep the wh- word."), ("me → to me", "*asked me* is correct.")], "Reported question → statement order.")
M("e02", STAT, E + "*He told that he was tired.*", [("told → told me", ""), ("was → is", "After *told*, *was* is correct."), ("that → if", "A statement takes *that*."), ("tired → tiring", "*tired* describes how he felt.")], "*told* needs an object.")
M("e03", CMD, E + "*Mother told me don't go out in the sun.*", [("don't go → not to go", ""), ("told → said", "*told me* is correct."), ("in → on", "*in the sun* is correct."), ("out → outside of", "*go out* is correct.")], "*Don't* → *not to* + V1.")
M("e04", QUES, E + "*He asked me that whether I could swim.*", [("that whether → whether", ""), ("could → can", "After *asked*, *could* is correct."), ("swim → swimming", "*could swim* is correct."), ("me → to me", "*asked me* is correct.")], "No *that* before *if/whether*.")
M("e05", CHG, E + "*She said that she will call me the next day.*", [("will → would", ""), ("call → called", "*would call* is correct."), ("the next day → tomorrow", "*the next day* is the correct reported form."), ("said → says", "With *the next day*, the report is in the past.")], "*will → would* after *said*.")
M("e06", CMD, E + "*The teacher suggested us to revise daily.*", [("suggested us to revise → suggested that we should revise", ""), ("revise → revising", "The main problem is *suggested us to*."), ("daily → everyday", "*daily* is correct."), ("teacher → teachers", "The subject is fine.")], "*suggest* takes *that … should* or V-ing, not object + *to*.", "medium")
M("e07", QUES, E + "*He asked me did I finish the work.*", [("did I finish → whether I had finished", ""), ("asked → said", "*asked* is right for a question."), ("the work → work", "*the work* is correct."), ("me → to me", "*asked me* is correct.")], "Yes/no → *whether* + statement order + backshift.", "medium")
M("e08", CHG, E + "*The teacher said that water boiled at 100 °C.*", [("boiled → boils", ""), ("said → says", "*said* is fine; the truth stays present."), ("at → on", "*at 100 °C* is correct."), ("that → if", "A statement takes *that*.")], "Scientific truths keep the present.")
# ---------- Choose the correct sentence ----------
CS = "Choose the correctly reported sentence."
M("x01", QUES, CS + " (\"Where is the post office?\" the tourist asked me.)", [("The tourist asked me where the post office was.", ""), ("The tourist asked me where was the post office.", "Statement order: *the post office was*."), ("The tourist asked me where the post office is?", "Backshift, and no question mark."), ("The tourist asked me that where the post office was.", "No *that* before *where*.")], "wh- + subject + verb, backshift, full stop.", "medium")
M("x02", CMD, CS + " (\"Please wait outside,\" the nurse said to us.)", [("The nurse requested us to wait outside.", ""), ("The nurse requested us please wait outside.", "*please* goes; use *to* + V1."), ("The nurse said us to wait outside.", "*said* cannot take *us* directly."), ("The nurse requested that wait outside.", "The pattern is *requested + object + to + V1*.")], "Request → *requested us to wait*.", "medium")
M("x03", STAT, CS + " (\"I have been working here for ten years,\" said Mr Rao.)", [("Mr Rao said that he had been working there for ten years.", ""), ("Mr Rao said that he has been working there for ten years.", "Present perfect continuous → past perfect continuous."), ("Mr Rao said that he had been working here for ten years.", "*here → there*."), ("Mr Rao said that I had been working there for ten years.", "*I* → *he*.")], "Backshift + *here → there*.", "medium")
# ---------- True / false ----------
C.tf("t01", QUES, "Reported questions end with a question mark.", False, "A reported question is a statement: *He asked me where I lived.* (full stop)")
C.tf("t02", CHG, "If the reporting verb is in the present tense, the tense of the reported speech does not change.", True, "*She says that she is busy.*")
C.tf("t03", CMD, "In reported commands, *Don't* changes to *not to*.", True, "*\"Don't shout\"* → *He told us not to shout.*")
C.tf("t04", STAT, "*He told that he was ill* is correct.", False, "*told* needs an object: *He told me that he was ill* (or *He said that he was ill*).")
C.tf("t05", CHG, "*tomorrow* becomes *the next day* in reported speech.", True, "After a past reporting verb, *tomorrow → the next day / the following day*.")
C.tf("t06", QUES, "Yes/no questions are reported with *if* or *whether*.", True, "*\"Are you ready?\"* → *He asked if I was ready.*")
# ---------- Assertion-reason ----------
C.ar("ar1", QUES, "*She asked me where I lived* is correct.", "Reported questions follow the statement word order.", 0,
     "R explains A: subject *I* comes before the verb *lived*.", "it uses statement order.", "reported questions use subject + verb.")
C.ar("ar2", CHG, "*He said that the sun rises in the east* is correct.", "After a past reporting verb, the tense never changes.", 2,
     "A is true; R is false: the tense usually moves back, but universal truths are an exception.", "universal truths keep the present.", "backshift is the normal rule, with exceptions.")
C.ar("ar3", CMD, "*The teacher told us not to talk* correctly reports *\"Don't talk.\"*", "Commands are reported with *to* / *not to* + V1.", 0,
     "R explains A.", "it uses *not to* + V1.", "commands take the infinitive.")
C.ar("ar4", STAT, "*She told me that she was busy* is correct.", "*told* is followed by a personal object when reporting a statement.", 0,
     "R explains A: *told* needs an object such as *me*; *said* does not take one directly.", "*told me that …* is the right pattern.", "*told* + object is required.")

chapter = header(4, "Reported Speech", ["reporting_changes", "statements", "questions", "commands_requests", "dialogue_reporting"],
                 "Follows the CBSE 2025-26 English Language and Literature (184) syllabus, Section B Grammar: reported speech (commands and requests, statements, questions), tested through gap filling, editing and transformation.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
