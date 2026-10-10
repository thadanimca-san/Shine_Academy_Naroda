"""CBSE Class 10 English Grammar Ch 2: Modals. Every item lists the right answer first (see grammar_common)."""
import sys
from grammar_common import Grammar, header

ROOT = sys.argv[1]
PATH = "app_core/content/cbse/class10/english/grammar/ch02_modals"
C = Grammar("gram10ch02")
blk, kc, M = C.blk, C.check_block, C.mcq
RULES, ABIL, POSS, OBLIG, ADV, PASTM = ["modal_rules"], ["ability_permission"], ["possibility"], ["obligation_necessity"], ["advice_requests"], ["past_modals"]

MEANINGS = ("| Meaning | Modals | Example |\n|---|---|---|\n"
            "| Ability | can, could, be able to | *She **can** speak three languages.* *I **could** swim at five.* |\n"
            "| Permission | may (formal), can, could | ***May** I come in, sir?* *You **can** use my pen.* |\n"
            "| Possibility | may, might, could | *It **may** rain today.* (fairly likely) *It **might** rain.* (less likely) |\n"
            "| Certainty (deduction) | must (sure yes), can't (sure no) | *He **must** be tired after the trek.* *That **can't** be Riya; she is in London.* |\n"
            "| Obligation / necessity | must, have to, need to | *You **must** wear a helmet.* *I **have to** catch the 7 o'clock bus.* |\n"
            "| No necessity | needn't, don't have to | *You **needn't** bring lunch; it is provided.* |\n"
            "| Prohibition | mustn't, can't | *You **mustn't** use phones in the exam hall.* |\n"
            "| Advice / duty | should, ought to, had better | *You **should** see a doctor.* *We **ought to** respect elders.* |\n"
            "| Polite request | could, would, will, can | ***Could** you open the window, please?* ***Would** you mind waiting?* |\n"
            "| Offer / suggestion | shall (with I/we), will | ***Shall** I carry your bag?* ***Shall** we start?* |\n"
            "| Past habit | used to, would | *We **used to** live in Rajkot.* *Grandpa **would** tell us stories every night.* |\n"
            "| Wish / prayer | may | ***May** you live long!* |")
PASTMODALS = ("| Pattern | Meaning | Example |\n|---|---|---|\n"
              "| must have + V3 | sure it happened | *The ground is wet; it **must have rained**.* |\n"
              "| can't / couldn't have + V3 | sure it did not happen | *He **can't have stolen** it; he was with me.* |\n"
              "| may / might have + V3 | perhaps it happened | *She **might have missed** the bus.* |\n"
              "| should / ought to have + V3 | it was right, but it was not done (regret, criticism) | *You **should have told** me earlier.* |\n"
              "| could have + V3 | it was possible, but it did not happen | *We **could have won** the match.* |\n"
              "| needn't have + V3 | it was done, but it was not necessary | *You **needn't have bought** milk; we had plenty.* |\n"
              "| would have + V3 | imagined past result | *I **would have helped** you if you had asked.* |")

sections = [
 {"id": "s1", "title": "Little words, big meanings", "blocks": [
  blk("s1.hook", "hook", title="Four sentences, four moods",
    body="- *You **can** leave now.* (you are allowed)\n- *You **should** leave now.* (it is a good idea)\n- *You **must** leave now.* (it is necessary)\n- *You **may** leave now.* (polite permission)\n\n"
         "Only one small word changed, yet the meaning moved from permission to advice to order. These small helping verbs are **modals**. They show the speaker's attitude: ability, permission, possibility, duty, advice, request.\n\n"
         "Every CBSE board paper has modal blanks in gap filling, and reported speech changes *can → could, may → might, will → would, shall → should*. Master them here once and for all."),
  blk("s1.inspiration", "inspiration", title="Kindness in simple words", person="Sudha Murty", years="born 1950",
    body="Sudha Murty was the first woman engineer hired by TELCO (now Tata Motors), after she wrote a bold postcard to J. R. D. Tata asking why the company wanted only men. "
         "She went on to write more than forty books in English and Kannada, loved by children and adults for their simple, warm language.\n\n"
         "Her writing is full of modals used with care: what we **can** do, what we **should** do, what we **must** never forget. She received the Padma Shri in 2006 and the Padma Bhushan in 2023.",
    future="Clear English helps in engineering, social work, writing, teaching and leadership, everywhere you need to persuade, request or advise."),
  C.socratic("s1.socratic", "Your friend has a high fever. Which sentence gives *advice*?",
    ["You should see a doctor.", "You can see a doctor.", "You might see a doctor."], 0,
    "*should* gives advice. *can* only says it is possible or allowed, and *might* says it is only a possibility."),
 ]},
 {"id": "s2", "title": "The rules every modal follows", "blocks": [
  blk("s2.thm", "theory", title="Five golden rules", revision=True,
    body="The main modals are *can, could, may, might, shall, should, will, would, must, ought to*. Semi-modals behave partly like them: *need, dare, used to, have to, be able to*.\n\n"
         "1. **Modal + V1 (base form).** *She can **sing**.* ✗ *She can sings / can singing / can to sing*.\n"
         "2. **No -s with he/she/it.** *He **must** go.* ✗ *He musts go*.\n"
         "3. **No *to* after modals**, except *ought to*, *have to*, *used to*, *be able to*. *You **should** rest*, but *You **ought to** rest*.\n"
         "4. **Negative: modal + not.** *cannot (can't), could not (couldn't), must not (mustn't), should not (shouldn't), will not (won't)*. No *do/does/did*: ✗ *He doesn't can swim*.\n"
         "5. **Questions: put the modal first.** ***Can** you help me?* ***Should** I wait?*\n\n"
         "**Modals have no -ing, -ed or *to* forms.** For other tenses use a substitute: *can → be able to* (*I will **be able to** come*), *must → have to* (*I **had to** leave early*)."),
  kc("s2.check", "Which sentence is correct?",
    [("She can play the guitar well.", ""), ("She can plays the guitar well.", "After a modal, use V1 with no -s."),
     ("She cans play the guitar well.", "Modals never take -s."), ("She can to play the guitar well.", "No *to* after *can*.")],
    "Modal + V1: *can play*."),
 ]},
 {"id": "s3", "title": "What each modal means", "blocks": [
  blk("s3.table", "markdown_table", title="Modals and their meanings", revision=True, body=MEANINGS),
  blk("s3.thm", "theory", title="Pairs that confuse everyone", revision=True,
    body="**can vs could**\n- *can*: present ability or informal permission: *I **can** solve this.*\n- *could*: past ability (*I **could** read at four*), or a more polite request (***Could** you help me?*), or a weak possibility (*It **could** be true*).\n\n"
         "**may vs might**\n- *may*: formal permission, or a fair possibility: ***May** I go out?* *She **may** be at home.*\n- *might*: a weaker possibility, and the past of *may* in reported speech.\n\n"
         "**must vs have to**\n- *must*: the speaker feels it is necessary: *I **must** call my mother.* Also rules and notices: *Visitors **must** sign in.*\n- *have to*: necessity from outside (rules, timetables): *We **have to** wear a uniform.* Past: *had to*.\n\n"
         "**mustn't vs needn't / don't have to**\n- *mustn't* = it is **not allowed**: *You **mustn't** cross on red.*\n- *needn't / don't have to* = it is **not necessary**: *You **needn't** hurry; we have time.*\n\n"
         "**should vs ought to**: both give advice or duty; *ought to* is a little stronger and always takes *to*. *You **ought to** obey traffic rules.*\n\n"
         "**shall vs will**: *shall* with *I/we* for offers and suggestions (***Shall** I open the door?*); *will* for promises, willingness and future (*I **will** help you*).\n\n"
         "**used to vs would**: both describe past habits; only *used to* can describe a past *state*: *I **used to** have long hair.* (✗ *would have long hair*)\n\n"
         "**need and dare** as modals: *You **need not** come.* *How **dare** you speak like that?* As ordinary verbs: *You **don't need to** come.*"),
  kc("s3.check", "Fill in the blank: You ____ smoke here. It is strictly prohibited.",
    [("mustn't", ""), ("needn't", "*needn't* means *it is not necessary*; here it is not allowed."),
     ("don't have to", "*don't have to* also means *not necessary*, not *forbidden*."), ("might not", "*might not* shows a weak possibility, not a rule.")],
    "Prohibition → *mustn't*."),
  kc("s3.check2", "Fill in the blank: ____ we go for a walk after dinner?",
    [("Shall", ""), ("Must", "*Must we ...?* asks if it is compulsory, not a suggestion."),
     ("Would", "*Would we ...?* is used for imagined situations, not suggestions."), ("Ought", "*ought* needs *to* and does not make suggestions.")],
    "A suggestion with *we* → *Shall we ...?*"),
 ]},
 {"id": "s4", "title": "Possibility and certainty", "blocks": [
  blk("s4.thm", "theory", title="How sure are you?", revision=True,
    body="Modals let us show how sure we are, from 100% yes to 100% no:\n\n"
         "| How sure | Modal | Example |\n|---|---|---|\n| 100% yes (deduction) | must | *The lights are on. They **must** be at home.* |\n| strong possibility | may / will (prediction) | *He **may** be in the library.* |\n"
         "| weak possibility | might / could | *It **might** snow, but I doubt it.* |\n| 100% no | can't / couldn't | *She **can't** be hungry; she just ate.* |\n\n"
         "Note: the opposite of *must* (sure yes) is **can't**, not *mustn't*. *He must be rich → He can't be rich.*"),
  kc("s4.check", "Fill in the blank: She has been working for ten hours. She ____ be exhausted.",
    [("must", ""), ("can't", "*can't* would mean you are sure she is NOT exhausted, the opposite of the evidence."),
     ("needn't", "*needn't* is about necessity, not deduction."), ("shall", "*shall* is for offers and suggestions.")],
    "Strong evidence → *must* (sure deduction)."),
 ]},
 {"id": "s5", "title": "Modals about the past", "blocks": [
  blk("s5.table", "markdown_table", title="Modal + have + V3", revision=True, body=PASTMODALS),
  blk("s5.thm", "theory", title="Regret, criticism and guessing about the past", revision=True,
    body="To talk about the past, most modals take **have + V3**:\n\n"
         "- **Guessing:** *must have*, *may/might have*, *can't have*. *The window is broken; someone **must have thrown** a ball.*\n"
         "- **Criticism and regret:** *should have / ought to have*. *I **should have studied** harder.* (I did not)\n"
         "- **Missed chances:** *could have*. *You **could have called** me.* (you didn't)\n"
         "- **Unnecessary actions:** *needn't have*. *You **needn't have cooked**; we ate outside.* (you cooked, for nothing)\n\n"
         "**needn't have done vs didn't need to do:** *I **needn't have taken** an umbrella* (I took it, but it didn't rain). *I **didn't need to take** an umbrella* (so I probably didn't)."),
  kc("s5.check", "Fill in the blank: You failed because you didn't study. You ____ harder.",
    [("should have worked", ""), ("must have worked", "*must have worked* means *I'm sure you worked*, which contradicts the sentence."),
     ("should work", "The failure is in the past; criticism about the past needs *should have* + V3."), ("needn't have worked", "That would mean the work was unnecessary.")],
    "Criticism about the past → *should have* + V3."),
  blk("s5.worked", "worked_example", title="Solving a modal gap-filling passage",
    problem="Fill in the blanks with suitable modals:\n\n*Doctor: You (a) ____ take these tablets twice a day. You (b) ____ eat oily food for a week. You (c) ____ come back for a check-up if you feel better. Patient: (d) ____ I go to school tomorrow?*",
    steps=["(a) The doctor gives a firm instruction → **must** (or *should*).",
           "(b) Something not allowed → **mustn't** (or *should not*).",
           "(c) Coming back is not necessary if the patient feels better → **needn't**.",
           "(d) Asking for permission → **May** (formal) or *Can*."],
    answer="must, mustn't, needn't, May"),
  blk("s5.worked2", "worked_example", title="Editing modal errors",
    problem="Each sentence has one error. Correct it.\n\n1. You should to respect your elders.\n2. She can speaks French fluently.\n3. He musts finish the work today.\n4. I could not came yesterday.",
    steps=["1. No *to* after *should*: **should to respect → should respect**.",
           "2. Modal + V1: **can speaks → can speak**.",
           "3. Modals take no -s: **musts → must**.",
           "4. Modal + V1: **could not came → could not come**."],
    answer="should respect; can speak; must; could not come"),
 ]},
 {"id": "s6", "title": "Remember, avoid, practise", "blocks": [
  blk("s6.memory", "memory_trick", title="Remember modals the easy way",
    body="- **\"Modal + V1, no -s, no to\"**: chant it before every gap-filling question.\n- **Only three love *to*:** *ought to, have to, used to*.\n"
         "- **mustn't = STOP sign** (forbidden); **needn't = relax** (not necessary).\n- **Past guess? Add *have* + V3:** *must have gone, might have forgotten, should have told*.\n"
         "- **Reported speech:** *can → could, may → might, will → would, shall → should*; *must* stays *must* or becomes *had to*."),
  blk("s6.mistakes", "common_mistakes", title="Common mistakes",
    body="1. ✗ *He can drives.* ✓ *He can drive.*\n2. ✗ *You must to go.* ✓ *You must go.*\n3. ✗ *You mustn't come if you are busy.* (forbidden) ✓ *You needn't come if you are busy.* (not necessary)\n"
         "4. ✗ *He must be not at home.* ✓ *He can't be at home.* (certainty about a negative)\n5. ✗ *I should went.* ✓ *I should have gone.*\n"
         "6. ✗ *I will can come tomorrow.* ✓ *I will be able to come tomorrow.* (two modals cannot sit together)\n7. ✗ *Did you could finish?* ✓ *Could you finish? / Were you able to finish?*\n"
         "8. ✗ *I would have long hair as a child.* ✓ *I used to have long hair.*"),
  blk("s6.tip", "teacher_tip", title="Try this in class",
    body="Play **\"Situation cards\"**: each card gives a situation (*Your friend left his bag on the bus*, *The road is wet*, *You want to borrow a pen from the principal*). "
         "Students reply with one sentence using the right modal (*He should have checked*, *It must have rained*, *May I borrow your pen, sir?*). The class decides if the modal fits the meaning."),
  blk("s6.reflection", "reflection", title="Say it in your own words",
    body="Explain the difference between *You mustn't tell anyone* and *You needn't tell anyone*. Which one would a friend say about a secret?"),
  blk("s6.connection", "connection", title="Where this leads",
    body="- **Chapter 4, Reported Speech:** modals shift back (*can → could, will → would*).\n- **Gap filling and editing:** a modal followed by a wrong verb form is one of the commonest board errors.\n"
         "- **Letter writing:** polite requests (*I would be grateful if you could ...*) and suggestions (*The authorities should ...*) need modals."),
  blk("s6.mastery", "mastery", title="Mastery challenge",
    body="Choose a modal for each blank and give the meaning:\n\n*It is 9 p.m. and Aarav isn't home yet. He (a) ____ be stuck in traffic, or he (b) ____ have forgotten the time. He (c) ____ have called us; he knows we worry. Next time he (d) ____ carry his phone.*\n\n"
         "**Answer:** (a) **may/might** (possibility) (b) **might/may** + have forgotten (guess about the past) (c) **should** have called (criticism) (d) **must/should** (necessity/advice)."),
  blk("s6.summary", "summary", title="Chapter summary",
    body="- Modals show ability, permission, possibility, necessity, advice, requests and offers.\n- Modal + V1; no -s, no *to* (except *ought to, have to, used to*); no *do/does/did*.\n"
         "- *must* (sure yes) ↔ *can't* (sure no); *mustn't* (forbidden) ↔ *needn't* (not necessary).\n- *Shall I/we* for offers and suggestions; *could/would* for polite requests.\n"
         "- Modal + *have* + V3 talks about the past: guess (*must/might have*), regret (*should have*), missed chance (*could have*), unnecessary action (*needn't have*)."),
  blk("s6.examtips", "exam_tips", title="Board exam tips",
    body="- Read the meaning of the sentence: is it advice, necessity, permission or possibility? Then choose.\n- In editing, check the verb after a modal: it must be V1 (or *have* + V3).\n"
         "- If the sentence says something did not happen (*but he didn't*), think of *should have / could have*.\n- Watch the time: *yesterday* with a modal usually needs *have* + V3 or *had to / could*."),
  blk("s6.flash1", "flashcard", front="mustn't vs needn't?", back="*mustn't* = not allowed; *needn't* = not necessary."),
  blk("s6.flash2", "flashcard", front="Opposite of *He must be at home* (sure)?", back="*He can't be at home.*"),
  blk("s6.flash3", "flashcard", front="Regret about the past with a modal?", back="*should have* + V3: *I should have listened.*"),
  blk("s6.flash4", "flashcard", front="Which modals take *to*?", back="*ought to*, plus the semi-modals *have to*, *used to*, *be able to*."),
 ]},
]

FB = "Fill in the blank with the most suitable modal: "
# ---------- Ability and permission ----------
M("g01", ABIL, FB + "When I was five, I ____ ride a bicycle.", [("could", ""), ("can", "*When I was five* is past: use *could*."), ("may", "*may* is for permission or possibility, not ability."), ("must", "*must* shows necessity, not ability.")], "Past ability → *could*.")
M("g02", ABIL, FB + "____ I borrow your notes, Ma'am?", [("May", ""), ("Must", "*Must I ...?* asks about obligation, not permission."), ("Shall", "*Shall I* offers to do something; it does not ask permission to borrow."), ("Would", "*Would I borrow* is not a request form.")], "Formal permission → *May I ...?*")
M("g03", ABIL, FB + "After months of practice, she ____ to swim across the river last summer.", [("was able", ""), ("could", "*could* + *to* is wrong; and for one specific achievement we prefer *was able to*."), ("can", "*last summer* is past."), ("might", "*might* shows possibility, and needs no *to*.")], "A specific past achievement → *was able to*.", "medium")
M("g04", ABIL, FB + "I'm sorry, I ____ come to your party tomorrow; I have an exam.", [("can't", ""), ("mustn't", "*mustn't* means you are not allowed; this is about being unable."), ("needn't", "*needn't* means not necessary."), ("shouldn't", "*shouldn't* gives advice.")], "Inability → *can't*.")
M("g05", ABIL, FB + "Students ____ use calculators in the board exam; they are not allowed.", [("cannot", ""), ("need not", "*need not* means it is not necessary, not that it is forbidden."), ("might not", "*might not* is a possibility, not a rule."), ("would not", "*would not* is about willingness.")], "Not permitted → *cannot* (or *must not*).")
M("g06", ABIL, FB + "Next year I ____ drive, because I will be eighteen.", [("will be able to", ""), ("can", "*can* cannot show a future ability that depends on something; use *will be able to*."), ("will can", "Two modals cannot come together."), ("could", "*could* is past or a weak possibility.")], "Future ability → *will be able to*.", "medium")
# ---------- Possibility and certainty ----------
M("g07", POSS, FB + "Take an umbrella. It ____ rain later.", [("may", ""), ("must", "*must* would mean you are sure it will rain."), ("can't", "Then there would be no need for an umbrella."), ("should", "*should* gives advice, not possibility.")], "Possibility → *may/might*.")
M("g08", POSS, FB + "That ____ be Neha at the door; she has gone to Canada.", [("can't", ""), ("mustn't", "*mustn't* means forbidden, not certainty."), ("may", "*may* suggests it is possible, but she is in Canada."), ("must", "*must* would mean you are sure it is her.")], "Sure it is not true → *can't*.")
M("g09", POSS, FB + "Everyone is wearing a coat. It ____ be very cold outside.", [("must", ""), ("can't", "The evidence shows it is cold, not the opposite."), ("needn't", "*needn't* is about necessity."), ("shall", "*shall* is for offers and suggestions.")], "Deduction from evidence → *must*.")
M("g10", POSS, FB + "I'm not sure where Kabir is. He ____ be in the library, or perhaps in the canteen.", [("might", ""), ("must", "You are not sure, so *must* (certainty) is wrong."), ("ought to", "*ought to* gives advice or duty."), ("has to", "*has to* shows obligation.")], "Uncertain possibility → *might*.")
M("g11", POSS, FB + "The road is wet. It ____ rained last night.", [("must have", ""), ("should have", "*should have* criticises; here we are deducing."), ("can't have", "The wet road shows that it did rain."), ("needn't have", "*needn't have* is about unnecessary actions.")], "Past deduction → *must have* + V3.", "medium")
M("g12", POSS, FB + "He ____ stolen the money; he was with me the whole day.", [("can't have", ""), ("must have", "He was with you, so you are sure he did NOT."), ("should have", "*should have* means it was the right thing to do."), ("needn't have", "*needn't have* means an unnecessary action.")], "Sure something did not happen → *can't have* + V3.", "medium")
M("g13", POSS, FB + "She didn't reply. She ____ seen my message.", [("might not have", ""), ("mustn't have", "*mustn't have* is not used for deduction."), ("shouldn't have", "That would criticise her for seeing it."), ("needn't have", "That is about unnecessary actions.")], "Guess about the past → *might not have* + V3.", "hard")
# ---------- Obligation and necessity ----------
M("g14", OBLIG, FB + "All passengers ____ wear seat belts during take-off.", [("must", ""), ("may", "*may* gives permission, not a rule."), ("might", "*might* is possibility."), ("can", "*can* gives permission or ability.")], "Rules → *must*.")
M("g15", OBLIG, FB + "You ____ bring your own lunch; it will be served at the camp.", [("needn't", ""), ("mustn't", "It is not forbidden, just unnecessary."), ("shouldn't", "*shouldn't* is advice against something."), ("can't", "*can't* means not able or not allowed.")], "Not necessary → *needn't*.")
M("g16", OBLIG, FB + "Yesterday I ____ stay late at school to finish the project.", [("had to", ""), ("must", "*must* has no past form; use *had to*."), ("have to", "*Yesterday* needs the past *had to*."), ("ought", "*ought* needs *to* and gives advice.")], "Past obligation → *had to*.")
M("g17", OBLIG, FB + "In India we ____ drive on the left side of the road.", [("have to", ""), ("may", "Driving on the left is a rule, not a choice."), ("might", "*might* is only possibility."), ("would", "*would* is for habits or imagined situations.")], "External rule → *have to* (or *must*).")
M("g18", OBLIG, FB + "Do I ____ fill in this form again?", [("have to", ""), ("must", "*Do I must* is wrong; *must* never follows *do*."), ("ought", "*ought* needs *to*, and *Do I ought* is wrong."), ("should to", "*should* takes no *to*.")], "*Do I have to ...?* asks about necessity.")
M("g19", OBLIG, FB + "You ____ have bought vegetables. Mother had already bought them.", [("needn't", ""), ("mustn't", "*mustn't have* is not used here; the buying was simply unnecessary."), ("can't", "*can't have bought* would mean you are sure he did not buy."), ("couldn't", "*couldn't have bought* means it was impossible.")], "Done but unnecessary → *needn't have* + V3.", "medium")
# ---------- Advice, requests, offers ----------
M("g20", ADV, FB + "You look pale. You ____ see a doctor.", [("should", ""), ("can", "*can* only says it is possible; advice needs *should*."), ("may", "*may* gives permission."), ("would", "*would* is not used alone for advice.")], "Advice → *should*.")
M("g21", ADV, FB + "We ____ to respect our national flag.", [("ought", ""), ("should", "*should* takes no *to*; the blank is followed by *to*."), ("must", "*must* takes no *to*."), ("can", "*can* takes no *to*.")], "Moral duty followed by *to* → *ought to*.")
M("g22", ADV, FB + "____ you please pass me the salt?", [("Could", ""), ("Must", "*Must you* sounds like a complaint, not a request."), ("Should", "*Should you* is not a polite request form."), ("Ought", "*ought* needs *to*.")], "Polite request → *Could/Would you ...?*")
M("g23", ADV, FB + "____ I carry your bag for you, Grandma?", [("Shall", ""), ("Must", "*Must I* asks if it is compulsory."), ("Need", "*Need I* asks if it is necessary."), ("Ought", "*ought* needs *to*.")], "An offer with *I* → *Shall I ...?*")
M("g24", ADV, FB + "You'd ____ leave now or you will miss the train.", [("better", ""), ("rather", "*would rather* expresses preference, not advice."), ("best to", "*'d best to* is not a correct form."), ("should", "*'d should* is not a correct form.")], "*had better* + V1 = strong advice.")
M("g25", ADV, FB + "When we were children, we ____ play in the fields every evening.", [("used to", ""), ("use to", "In positive sentences the form is *used to*."), ("must", "*must* is not used for past habits."), ("ought to", "*ought to* is advice.")], "Past habit → *used to*.")
M("g26", ADV, FB + "____ you live long and be happy!", [("May", ""), ("Might", "Wishes and blessings begin with *May*."), ("Can", "*Can* is not used for wishes."), ("Shall", "*Shall* is not used for blessings.")], "Wishes and prayers → *May*.")
M("g27", ADV, FB + "____ you mind closing the door?", [("Would", ""), ("Should", "The fixed polite pattern is *Would you mind ...?*"), ("Must", "*Must you mind* is not a request."), ("Shall", "*Shall* is used with *I/we*.")], "*Would you mind + V-ing?* is a polite request.")
# ---------- Past modals: regret and criticism ----------
M("g28", PASTM, FB + "I failed the test. I ____ studied harder.", [("should have", ""), ("must have", "*must have studied* means you are sure you studied."), ("can have", "*can have* is not used this way."), ("needn't have", "*needn't have* means studying was unnecessary.")], "Regret → *should have* + V3.")
M("g29", PASTM, FB + "Why didn't you ask me? I ____ helped you.", [("could have", ""), ("must have", "*must have helped* means you are sure I helped."), ("should", "*should helped* is wrong; modal + V1 or *have* + V3."), ("can have", "*can have* is not used for missed chances.")], "Missed chance → *could have* + V3.", "medium")
M("g30", PASTM, FB + "He ____ driven so fast. That is why he had an accident.", [("shouldn't have", ""), ("mustn't have", "*mustn't have* is not used to criticise past actions."), ("can't have", "*can't have* means you are sure he did not drive fast."), ("needn't", "*needn't driven* is not a correct form.")], "Criticism of a past action → *shouldn't have* + V3.", "medium")
# ---------- Board-style passage ----------
P1 = ("Read the passage and choose the correct option for the blank.\n\n*Notice: All students (a) ____ report to the auditorium by 9 a.m. Students (b) ____ bring their mobile phones. Those who wish to participate in the quiz (c) ____ register with the class teacher. Parents (d) ____ attend the prize distribution if they wish.*\n\n")
M("p01", OBLIG, P1 + "Blank (a):", [("must", ""), ("may", "*may* would make reporting optional."), ("might", "*might* is only possibility."), ("would", "*would* is not used for rules.")], "Rules in a notice → *must*.", "medium")
M("p02", OBLIG, P1 + "Blank (b):", [("must not", ""), ("need not", "That would mean phones are optional; a notice like this forbids them."), ("may", "*may bring* allows phones."), ("ought", "*ought* needs *to*.")], "Prohibition → *must not*.", "medium")
M("p03", ADV, P1 + "Blank (c):", [("should", ""), ("can't", "*can't register* makes no sense for those who wish to take part."), ("mustn't", "That would forbid registering."), ("would have", "*would have register* is wrong.")], "Instruction/advice → *should*.", "medium")
M("p04", ABIL, P1 + "Blank (d):", [("may", ""), ("must", "*if they wish* shows it is optional, not compulsory."), ("have to", "*if they wish* shows it is optional."), ("ought to", "*ought to* is a duty, but it is optional.")], "Permission → *may*.", "medium")
# ---------- Editing ----------
E = "Identify the error and choose the correct correction: "
M("e01", RULES, E + "*She can speaks four languages.*", [("speaks → speak", ""), ("can → cans", "Modals never take -s."), ("four → fourth", "*four languages* is correct."), ("languages → language", "*four* needs the plural.")], "Modal + V1.")
M("e02", RULES, E + "*You should to drink more water.*", [("should to → should", ""), ("drink → drinking", "Modal + V1: *drink*."), ("more → much", "*more water* is correct."), ("You → Your", "*You* is the subject.")], "No *to* after *should*.")
M("e03", RULES, E + "*He musts complete the work by Monday.*", [("musts → must", ""), ("complete → completes", "Modal + V1."), ("by → till", "*by Monday* (deadline) is correct."), ("the work → work", "*the work* is correct.")], "Modals take no -s.")
M("e04", RULES, E + "*I will can meet you tomorrow.*", [("will can → will be able to", ""), ("meet → meeting", "Modal + V1 is correct here."), ("tomorrow → yesterday", "The time fits the future."), ("I → Me", "*I* is the subject.")], "Two modals cannot be used together.", "medium")
M("e05", PASTM, E + "*You should have went to the doctor.*", [("went → gone", ""), ("should → shall", "*should have* is correct for criticism."), ("have → has", "After a modal, *have* never changes to *has*."), ("the → a", "*the doctor* is fine.")], "Modal + *have* + V3: *gone*.")
M("e06", RULES, E + "*Does she can swim?*", [("Does she can → Can she", ""), ("swim → swims", "Modal + V1."), ("can → could", "The question form is the problem, not the modal."), ("she → her", "*she* is the subject.")], "Modals make questions themselves, without *do/does*.")
M("e07", OBLIG, E + "*We mustn't buy bread; there is plenty at home.*", [("mustn't → needn't", ""), ("buy → buying", "Modal + V1."), ("plenty → many", "*plenty* is correct."), ("at → in", "*at home* is correct.")], "Not necessary → *needn't*, not *mustn't* (forbidden).", "medium")
M("e08", ADV, E + "*We ought respect our teachers.*", [("ought → ought to", ""), ("respect → respects", "*ought to* + V1."), ("our → ours", "*our teachers* is correct."), ("teachers → teacher", "The plural is fine.")], "*ought* always takes *to*.")
M("e09", ABIL, E + "*Yesterday I can't finish my homework.*", [("can't → couldn't", ""), ("finish → finished", "Modal + V1."), ("my → mine", "*my homework* is correct."), ("Yesterday → Tomorrow", "The modal must fit the time, not the other way round.")], "Past inability → *couldn't*.")
M("e10", PASTM, E + "*He must have forget his keys.*", [("forget → forgotten", ""), ("must → musts", "Modals never take -s."), ("have → had", "*must have* + V3."), ("his → him", "*his keys* is correct.")], "*must have* + V3: *forgotten*.")
# ---------- Choose the correct sentence ----------
CS = "Choose the grammatically correct sentence."
M("c01", POSS, CS, [("She can't be at school; it's a holiday.", ""), ("She mustn't be at school; it's a holiday.", "Certainty that something is not true takes *can't*, not *mustn't*."), ("She can't to be at school; it's a holiday.", "No *to* after *can't*."), ("She doesn't can be at school; it's a holiday.", "*doesn't* is never used with modals.")], "Negative deduction → *can't*.", "medium")
M("c02", PASTM, CS, [("You could have told me earlier.", ""), ("You could told me earlier.", "Modal + V1 or *have* + V3."), ("You could have tell me earlier.", "*have* + V3: *told*."), ("You could has told me earlier.", "After a modal, *have*, never *has*.")], "*could have* + V3.", "medium")
M("c03", ADV, CS, [("We used to live in Bhavnagar.", ""), ("We use to live in Bhavnagar.", "Positive past habit: *used to*."), ("We used to lived in Bhavnagar.", "*used to* + V1."), ("We were used to live in Bhavnagar.", "*be used to* means *accustomed to* and takes V-ing.")], "*used to* + V1 for past habits/states.", "medium")
M("c04", OBLIG, CS, [("I had to wait for an hour.", ""), ("I must waited for an hour.", "*must* + V1, and *must* has no past."), ("I musted wait for an hour.", "*must* has no past form."), ("I had to waited for an hour.", "*had to* + V1.")], "Past obligation → *had to* + V1.")
M("c05", ADV, CS, [("Would you like some tea?", ""), ("Would you like to some tea?", "*like* + a noun needs no *to*."), ("Will you liked some tea?", "Modal + V1."), ("Would you likes some tea?", "Modal + V1, no -s.")], "Polite offer → *Would you like ...?*")
# ---------- Identify the meaning ----------
IM = "What does the modal in bold express? "
M("m01", ABIL, IM + "*My grandfather **can** still read without glasses.*", [("Ability", ""), ("Permission", "Nobody is allowing anything; it is about what he is able to do."), ("Possibility", "It is a fact about his ability."), ("Obligation", "Nothing is compulsory here.")], "*can* = ability.")
M("m02", POSS, IM + "*Don't call now; she **might** be sleeping.*", [("Possibility", ""), ("Permission", "No permission is given."), ("Obligation", "Sleeping is not a duty here."), ("Ability", "It is a guess, not about ability.")], "*might* = weak possibility.")
M("m03", POSS, IM + "*You have walked 20 km. You **must** be tired.*", [("Certainty (deduction)", ""), ("Obligation", "Being tired is not a rule; it is a logical conclusion."), ("Permission", "No permission is given."), ("Advice", "No advice is given.")], "*must* here = sure deduction.", "medium")
M("m04", ADV, IM + "*You **should** apologise to her.*", [("Advice", ""), ("Ability", "It is not about being able to."), ("Possibility", "It is a recommendation."), ("Prohibition", "It tells you to do something, not to avoid it.")], "*should* = advice.")
M("m05", OBLIG, IM + "*You **needn't** wear a tie on Saturdays.*", [("Absence of necessity", ""), ("Prohibition", "It is not forbidden; it is just not required."), ("Ability", "It is about requirement, not ability."), ("Possibility", "It is about requirement.")], "*needn't* = not necessary.")
M("m06", ADV, IM + "***Shall** we start the meeting now?*", [("Suggestion", ""), ("Obligation", "It does not ask whether it is compulsory."), ("Ability", "It is not about ability."), ("Certainty", "It is a question that proposes an idea.")], "*Shall we ...?* = suggestion.")
# ---------- True / false ----------
C.tf("t01", RULES, "Modals take -s with *he, she* and *it*.", False, "Modals never change: *he can, she must, it may*.")
C.tf("t02", OBLIG, "*mustn't* and *needn't* mean the same thing.", False, "*mustn't* = it is not allowed; *needn't* = it is not necessary.")
C.tf("t03", PASTM, "*should have* + V3 shows that something right was not done in the past.", True, "*You should have called* = you did not call, and that was wrong.")
C.tf("t04", RULES, "*ought* is always followed by *to*.", True, "*We ought to help the poor.*")
C.tf("t05", POSS, "The opposite of *He must be at home* (deduction) is *He mustn't be at home*.", False, "For deduction, the opposite of *must* is *can't*: *He can't be at home*.")
C.tf("t06", ABIL, "*be able to* can be used where *can* has no form, such as the future: *will be able to*.", True, "*can* has no future or perfect forms, so we use *be able to*.")
# ---------- Assertion-reason ----------
C.ar("ar1", RULES, "*She can sings well* is incorrect.", "A modal is always followed by the base form of the verb.", 0,
     "R explains A: after *can*, use V1, *sing*.", "*sings* after *can* is wrong.", "modal + V1 is the rule.")
C.ar("ar2", OBLIG, "*You mustn't come tomorrow if you are busy* is the best way to say coming is optional.", "*mustn't* expresses prohibition.", 3,
     "A is false: optional means *needn't*; R is true, which is why *mustn't* does not fit.", "optional needs *needn't*, not *mustn't*.", "*mustn't* means not allowed.")
C.ar("ar3", PASTM, "*The ground is wet; it must have rained* is correct.", "*must have* + V3 shows a sure guess about the past.", 0,
     "R explains A: the wet ground lets us deduce that it rained.", "it is a correct deduction about the past.", "*must have* + V3 is used for deductions about the past.")
C.ar("ar4", ADV, "*Shall I open the window?* is an offer.", "*shall* is used with all subjects in modern English.", 2,
     "A is true; R is false: in modern English *shall* is mainly used with *I* and *we*.", "*Shall I ...?* offers help.", "*shall* is mainly used with *I/we*.")

chapter = header(2, "Modals", ["modal_rules", "ability_permission", "possibility", "obligation_necessity", "advice_requests", "past_modals"],
                 "Follows the CBSE 2025-26 English Language and Literature (184) syllabus, Section B Grammar: modals, tested through gap filling, editing and transformation.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
