"""CBSE Class 10 English Writing Ch 9: Formal Letter Writing (CBSE 184, Section B Writing, 5 marks). Objective items list the right answer first."""
import sys
from grammar_common import Grammar, header

ROOT = sys.argv[1]
PATH = "app_core/content/cbse/class10/english/grammar/ch09_formal_letter"
C = Grammar("gram10ch09")
blk, kc, M = C.blk, C.check_block, C.mcq
FORMAT, COMPLAINT, ORDER, EDITOR, STYLE = ["letter_format"], ["complaint_and_enquiry"], ["order_and_supply"], ["letter_to_the_editor"], ["tone_and_language"]
MS = ["1 mark: format (addresses, date, subject, salutation, closing)", "1 mark: organisation of ideas (clear paragraphs)", "1 mark: content (all points of the situation covered)",
      "1 mark: accuracy (grammar and spelling)", "1 mark: fluency (formal, clear expression in 100-120 words)"]

FORMAT_TAB = ("| Part | Example | Tip |\n|---|---|---|\n"
              "| **1. Sender's address** | Examination Hall / 14, Shanti Nagar, Ahmedabad | Use the name and address given in the question; otherwise 'Examination Hall' |\n"
              "| **2. Date** | 12 October 2026 | Write the month in words |\n"
              "| **3. Receiver's address** | The Municipal Commissioner, Ahmedabad Municipal Corporation, Ahmedabad | Designation first, then office and city |\n"
              "| **4. Subject** | Subject: Overflowing garbage bins in Shanti Nagar | One line, 6-10 words, tells the purpose |\n"
              "| **5. Salutation** | Sir / Madam | Never 'Dear friend' or 'Respected sir' in an editor's letter |\n"
              "| **6. Body** | three short paragraphs | (1) who you are and why you write; (2) details: problem, effects, facts; (3) request / action and thanks |\n"
              "| **7. Complimentary close** | Yours faithfully | 'faithfully' to an unknown official |\n"
              "| **8. Signature and name** | (signature) Rohan Mehta / Secretary, RWA | Use the name given in the question |")

COMPLAINT_MODEL = ("**Model letter of complaint (about 120 words, body)**\n\n"
                   "Examination Hall  \nABC Nagar, Ahmedabad\n\n12 October 2026\n\nThe Municipal Commissioner  \nAhmedabad Municipal Corporation  \nAhmedabad\n\n"
                   "**Subject: Overflowing garbage bins in Shanti Nagar**\n\nSir\n\n"
                   "I am a resident of Shanti Nagar and wish to draw your attention to the overflowing garbage bins in our colony.\n\n"
                   "For the past three weeks the bins near the community park have not been cleared. Garbage is scattered on the road, stray animals tear the bags, and the foul smell has made walking unbearable. Mosquitoes are breeding, and several children have fallen ill with fever.\n\n"
                   "I request you to ensure that the bins are cleared daily and that more bins are placed in the area. I hope you will take prompt action.\n\n"
                   "Yours faithfully  \n(signature)  \nRohan Mehta")

EDITOR_MODEL = ("**Model letter to the editor (about 120 words, body)**\n\n"
                "14, Lake View Society  \nVadodara\n\n12 October 2026\n\nThe Editor  \nThe Times of India  \nVadodara\n\n"
                "**Subject: Need to control noise pollution during festivals**\n\nSir\n\n"
                "Through the columns of your esteemed newspaper, I wish to highlight the growing problem of noise pollution in our city during festivals.\n\n"
                "Loudspeakers play at full volume till late at night, and firecrackers burst well beyond permitted hours. Students preparing for examinations cannot study, and elderly and sick people suffer greatly. Such noise can also damage hearing and cause stress.\n\n"
                "The authorities should strictly enforce time limits and sound levels, and citizens must celebrate responsibly. I hope this letter will draw the attention of those concerned.\n\n"
                "Yours truly  \n(signature)  \nAnanya Shah")

ORDER_MODEL = ("**Model letter placing an order (body)**\n\nThe Librarian of a school writes to a bookseller:\n\n"
               "I am writing to place an order for the following books for our school library:\n\n"
               "| S. No. | Title | Author / Publisher | Copies |\n|---|---|---|---|\n| 1 | Wings of Fire | A. P. J. Abdul Kalam | 10 |\n| 2 | The Story of My Experiments with Truth | M. K. Gandhi | 5 |\n| 3 | Oxford Student's Dictionary | OUP | 15 |\n\n"
               "Kindly send the books by 30 October 2026 and allow the usual discount for schools. Please ensure that the books are new and not damaged. Payment will be made by cheque on delivery.")

sections = [
 {"id": "s1", "title": "Why letters still matter", "blocks": [
  blk("s1.hook", "hook", title="Five marks for one page",
    body="In the board exam, a formal letter of about **100-120 words** carries **5 marks**. One mark is for **format** alone. Students lose easy marks by forgetting the date, writing 'Respected Sir' in the wrong place, or missing a subject line.\n\n"
         "This chapter gives you a fixed format, model letters for every type in the syllabus, and plenty of practice so the format becomes automatic."),
  blk("s1.inspiration", "inspiration", title="A letter that changed history", person="Mahatma Gandhi", years="1869–1948",
    body="Gandhi wrote thousands of letters, to viceroys, newspapers and ordinary people. His letters were **polite, clear and firm**: he stated the problem, gave facts and asked for specific action. That is exactly what a good formal letter does.",
    future="Clear formal writing is needed for job applications, complaints to companies, emails to officials and letters to newspapers."),
  C.socratic("s1.socratic", "Why does a formal letter need a subject line?",
    ["It tells the reader the purpose at once, so the letter reaches the right action quickly", "It decorates the letter", "It replaces the salutation"], 0,
    "Busy officials read the subject first."),
 ]},
 {"id": "s2", "title": "The format", "blocks": [
  blk("s2.thm", "theory", title="The CBSE formal letter", revision=True,
    body="**Types in the CBSE 2025-26 syllabus:** a **letter of complaint**, **letter of enquiry**, **letter placing an order** (and its reply, supply), and a **letter to the editor** on a social issue. You answer **one of two** choices, in about **100-120 words** (body), for **5 marks**.\n\n"
         "**Layout:** use the **block format**: every line starts at the left margin; leave a line between parts.\n\n"
         "**Marking:** format 1, organisation 1, content 1, accuracy 1, fluency 1.\n\n"
         "**Language:** formal and polite. No contractions (*don't* → *do not*), no slang, no SMS language. Short, clear sentences. Use the names and addresses given in the question."),
  blk("s2.table", "markdown_table", title="The eight parts of a formal letter", revision=True, body=FORMAT_TAB),
  kc("s2.check", "Which complimentary close is correct for a letter to a government official?",
    [("Yours faithfully", ""), ("Your loving son", "That is informal."), ("Bye", "Far too informal."), ("Yours affectionately", "That is for family.")],
    "Use 'faithfully' when writing to an official you do not know personally.")
  ,kc("s2.check2", "Where does the subject line go?",
    [("after the receiver's address and before the salutation", ""), ("at the very top", "After the receiver's address."), ("after the signature", "Before the salutation."), ("in the last paragraph", "Before the salutation.")],
    "Subject, then Sir/Madam.")
 ]},
 {"id": "s3", "title": "Model letters", "blocks": [
  blk("s3.complaint", "theory", title="Letter of complaint", revision=True, body=COMPLAINT_MODEL),
  blk("s3.editor", "theory", title="Letter to the editor", revision=True, body=EDITOR_MODEL),
  blk("s3.order", "theory", title="Letter placing an order", revision=True, body=ORDER_MODEL),
  blk("s3.tips", "theory", title="How to plan the body in 2 minutes", revision=True,
    body="**Paragraph 1, purpose:** introduce yourself (if needed) and state why you are writing: *I wish to draw your attention to...*, *I am writing to enquire about...*, *I would like to place an order for...*, *Through the columns of your esteemed newspaper...*\n\n"
         "**Paragraph 2, details:** facts, effects and examples: when, where, how long, who is affected, what has been tried. For an enquiry, list your questions; for an order, give a table with titles and quantities.\n\n"
         "**Paragraph 3, action:** what you want done and by when; a polite closing line: *I hope you will take prompt action.*, *I look forward to an early reply.*"),
  kc("s3.check", "Which opening suits a letter to the editor?",
    [("Through the columns of your esteemed newspaper, I wish to highlight...", ""), ("Hi! How are you?", "Too informal."), ("I am writing to order ten books.", "That is an order letter."), ("Please refund my money.", "That suits a complaint.")],
    "Editors publish letters on public issues.")
 ]},
 {"id": "s4", "title": "Tone and language", "blocks": [
  blk("s4.thm", "theory", title="Useful formal expressions", revision=True,
    body="| Purpose | Expression |\n|---|---|\n| complaint | I wish to draw your attention to... / I regret to inform you that... |\n| enquiry | I would be grateful if you could provide information about... |\n"
         "| order | Kindly supply the following items at the earliest. |\n| editor | Through the columns of your esteemed newspaper... |\n| request | I request you to take immediate action. |\n| closing | I hope you will look into the matter. / I look forward to your reply. |\n\n"
         "**Avoid:** *Respected Sir* is acceptable to a principal, but use *Sir/Madam* for officials and editors in CBSE; never *Dear Editor friend*, *Thanking you* on its own line without a closing, emotional exaggeration, or very long paragraphs."),
  kc("s4.check", "Which sentence is most suitable in a formal letter?",
    [("I would be grateful if you could look into the matter.", ""), ("Fix this ASAP!", "Too rude and informal."), ("U must do something.", "SMS language."), ("This is soooo bad.", "Too informal.")],
    "Formal letters are polite and clear.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Order of parts: S-D-R-S-S-B-C-S: Sender, Date, Receiver, Subject, Salutation, Body, Close, Signature.**\n- **Body = 3 Ps: Purpose, Particulars, Plea (request).**\n- **To officials: 'Sir/Madam' ... 'Yours faithfully'.**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Forgetting the **date** or the **subject**: you lose the format mark.\n2. Writing **'Yours faithfully'** with a capital F or a comma error is minor, but writing **'Your faithfully'** is wrong.\n"
         "3. Inventing your own name when the question gives one: **use the given name**.\n4. Writing 250 words: stay within **100-120 words** in the body.\n5. Using contractions and slang."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Give students a jumbled letter (eight parts on cards). In pairs, they arrange them in order in one minute, then write the body for a given situation."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Which problem in your area deserves a letter to the editor? Plan the three paragraphs."),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Analytical Paragraph:** the other writing task in the paper.\n- **Real life:** job applications, complaints to companies, emails to schools and offices."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="You are Kavya / Kunal of 22, Green Park, Surat. Write a letter to the Station House Officer complaining about frequent chain-snatching in your area. (100-120 words)\n\n"
         "**Model answer (outline):** Sender's address and date; The Station House Officer, Adajan Police Station, Surat; Subject: Frequent chain-snatching in Green Park; Sir. Para 1: resident of Green Park, writing to report rising chain-snatching. Para 2: four incidents in two weeks near the market road in the evening; women afraid to walk; poor street lighting. Para 3: request regular police patrolling, CCTV cameras and better lighting; hope for prompt action. Yours faithfully, signature, Kavya."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Formal letters: complaint, enquiry, order/supply, letter to the editor; 100-120 words; 5 marks.\n- Eight parts in block format; subject before salutation; 'Yours faithfully' to officials.\n"
         "- Body in three paragraphs: purpose, details, request.\n- Formal, polite, clear language; use the given names."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- Write the format first, then the body: it secures the format mark.\n- Underline the key words in the question (who writes, to whom, about what).\n- Count roughly 10-12 lines of body; do not exceed the limit."),
  blk("s5.flash1", "flashcard", front="What are the eight parts of a formal letter?", back="Sender's address, date, receiver's address, subject, salutation, body, complimentary close, signature and name."),
  blk("s5.flash2", "flashcard", front="How should the body be organised?", back="Three paragraphs: purpose, details (facts and effects), request or action with a polite close."),
  blk("s5.flash3", "flashcard", front="Which close is used for officials and editors?", back="Yours faithfully (or Yours truly for an editor)."),
  blk("s5.flash4", "flashcard", front="How long should the letter be?", back="About 100-120 words in the body."),
 ]},
]

# ---------------- Writing tasks (5 marks each) ----------------
TASKS = [
 ("w1", COMPLAINT, "You are Riya / Rahul of 12, Navrangpura, Ahmedabad. Write a letter to the Municipal Commissioner complaining about potholes on the main road of your area. (100-120 words)",
  ["Format: sender's address, date, The Municipal Commissioner, AMC, Ahmedabad; Subject: Dangerous potholes on the main road of Navrangpura; Sir/Madam.",
   "Para 1: introduce yourself as a resident; state the purpose.", "Para 2: deep potholes after the monsoon; accidents to two-wheelers; traffic jams; water logging and mosquitoes.",
   "Para 3: request urgent repair before the festival season; thank and hope for prompt action.", "Close: Yours faithfully, signature, Riya."]),
 ("w2", COMPLAINT, "You are Neha / Nikhil of 5, Alkapuri, Vadodara. You bought a mixer-grinder that stopped working within a week. Write a letter to the Customer Care Manager of the company seeking a replacement. (100-120 words)",
  ["Format: addresses, date; Subject: Replacement of defective mixer-grinder; Sir/Madam.", "Para 1: purchase details: model, date, shop, bill number.",
   "Para 2: the defect: motor stops, burning smell; under warranty.", "Para 3: request replacement within a week; enclose copy of bill and warranty card.", "Close: Yours faithfully, signature, name."]),
 ("w3", COMPLAINT, "Write a letter to the Principal of a summer camp enquiring about the courses, fees, timings and facilities. You are Isha / Ishaan of 9, Satellite, Ahmedabad. (100-120 words)",
  ["Format: addresses, date; Subject: Enquiry about summer camp courses; Sir/Madam.", "Para 1: saw the advertisement; interested in joining.",
   "Para 2: questions: courses offered, duration and timings, fees and concessions, transport, safety and qualified trainers.", "Para 3: request a brochure and admission form; look forward to an early reply.",
   "Close: Yours faithfully, signature, Isha."]),
 ("w4", ORDER, "You are the Sports In-charge of Shine Public School, Naroda. Write a letter to M/s Sports House, Ahmedabad, placing an order for sports equipment. (100-120 words)",
  ["Format: school address, date, The Manager, M/s Sports House, Ahmedabad; Subject: Order for sports equipment; Sir.", "Para 1: purpose: placing an order for the school.",
   "Para 2: table of items: 10 cricket bats, 20 footballs, 5 volleyball nets, 30 skipping ropes, with brands.", "Para 3: delivery by a date, school discount, quality check, payment by cheque on delivery.",
   "Close: Yours faithfully, signature, name, Sports In-charge."]),
 ("w5", ORDER, "You are the Librarian of Shine Academy, Naroda. Write a letter to a bookseller placing an order for books for the school library. (100-120 words)",
  ["Format: addresses, date; Subject: Order for library books; Sir/Madam.", "Para 1: purpose: ordering books for the library.",
   "Para 2: table with titles, authors and copies (e.g. Wings of Fire, a dictionary, NCERT exemplars).", "Para 3: delivery date, discount, new and undamaged copies, mode of payment.",
   "Close: Yours faithfully, signature, Librarian."]),
 ("w6", EDITOR, "Write a letter to the editor of a newspaper about the increasing use of plastic bags in your city and its harmful effects. You are Meera / Manav of 21, Maninagar, Ahmedabad. (100-120 words)",
  ["Format: addresses, date, The Editor, newspaper, city; Subject: Harmful effects of plastic bags; Sir.", "Para 1: through the columns of your newspaper; the problem.",
   "Para 2: effects: blocked drains, cattle deaths, soil and water pollution; plastic does not decompose.", "Para 3: suggestions: strict ban, cloth bags, awareness drives, fines.",
   "Close: Yours truly / faithfully, signature, Meera."]),
 ("w7", EDITOR, "Write a letter to the editor about the problem of stray dogs in your locality. You are Tanvi / Tarun of 7, Bopal, Ahmedabad. (100-120 words)",
  ["Format: addresses, date, The Editor; Subject: Menace of stray dogs in Bopal; Sir.", "Para 1: purpose: draw attention of authorities.",
   "Para 2: dogs chase children and two-wheelers; bite cases; fear at night.", "Para 3: humane solutions: sterilisation, shelters, vaccination drives; request the corporation to act.",
   "Close: Yours truly, signature, Tanvi."]),
 ("w8", EDITOR, "Write a letter to the editor about the need for more public libraries in your city. You are Aarav / Aarohi of 3, Vastrapur, Ahmedabad. (100-120 words)",
  ["Format: addresses, date, The Editor; Subject: Need for more public libraries; Sir/Madam.", "Para 1: purpose: lack of public libraries.",
   "Para 2: students cannot afford books; quiet study space is rare; reading habit is declining.", "Para 3: suggest libraries in every ward with digital sections and long hours.",
   "Close: Yours faithfully, signature, Aarav."]),
 ("w9", COMPLAINT, "You are Sneha / Sahil of 15, Gandhinagar. Write a letter to the Electricity Board complaining about frequent power cuts in your area during examinations. (100-120 words)",
  ["Format: addresses, date, The Executive Engineer, Electricity Board, Gandhinagar; Subject: Frequent power cuts during examinations; Sir.",
   "Para 1: resident; purpose.", "Para 2: power cuts of 3-4 hours daily, often in the evening; students cannot study; elderly suffer in heat.",
   "Para 3: request a regular supply, especially during exam season; announce scheduled cuts in advance.", "Close: Yours faithfully, signature, Sneha."]),
 ("w10", COMPLAINT, "Write a letter to the Manager of a travel agency enquiring about a five-day educational tour to Delhi for 40 students. You are the Class Teacher of Class 10, Shine Academy, Naroda. (100-120 words)",
  ["Format: addresses, date; Subject: Enquiry about an educational tour to Delhi; Sir/Madam.", "Para 1: purpose: planning a five-day tour for 40 students.",
   "Para 2: questions: itinerary, places of educational value, travel mode, stay, food, safety, cost per student.", "Para 3: request a detailed quotation; look forward to an early reply.",
   "Close: Yours faithfully, signature, Class Teacher."]),
]
TASKS += [
 ("w11", ORDER, "You are the Manager of M/s Sports House, Ahmedabad. Reply to Shine Public School's order, confirming supply of the sports equipment and the delivery date. (100-120 words)",
  ["Format: addresses, date; Subject: Supply of sports equipment against your order; Sir/Madam.", "Para 1: thank the school for its order.",
   "Para 2: confirm items and quantities; one item out of stock, to follow in a week; school discount allowed.", "Para 3: delivery date, invoice enclosed, payment terms; assure quality.",
   "Close: Yours faithfully, signature, Manager."]),
 ("w12", COMPLAINT, "You are Pooja / Prakash of 30, Chandkheda, Ahmedabad. Write a letter to the Regional Transport Officer complaining about rash driving by school vans near your school. (100-120 words)",
  ["Format: addresses, date; Subject: Rash driving by school vans; Sir.", "Para 1: resident and parent; purpose.",
   "Para 2: overloaded vans, over-speeding near the school gate, no attendants; a near-accident last week.", "Para 3: request checks on vans, speed limits and penalties; hope for prompt action.",
   "Close: Yours faithfully, signature, Pooja."]),
]
for id_, concepts, question, steps in TASKS:
    C.q(id_, "long_answer", 5, concepts, question, "medium", answer_steps=steps, marking_scheme=MS)

# ---------------- Format practice (objective) ----------------
M("m01", FORMAT, "What comes first in a formal letter?", [("the sender's address", ""), ("the date", "Date comes after the sender's address."), ("the subject", "Subject comes later."), ("the salutation", "Salutation comes later.")], "Then the date.")
M("m02", FORMAT, "Which is the correct date format for a formal letter?", [("12 October 2026", ""), ("12/10", "Too short."), ("Oct 12th", "Write the full date."), ("twelve-ten-twenty-six", "Use 12 October 2026.")], "Month in words, no confusion.")
M("m03", FORMAT, "The subject line should be:", [("brief, stating the purpose in one line", ""), ("a full paragraph", "One line only."), ("written after the signature", "Before the salutation."), ("optional", "It is required.")], "6-10 words.")
M("m04", FORMAT, "Which salutation suits a letter to the editor?", [("Sir", ""), ("Dear friend", "Too informal."), ("Hi Editor", "Too informal."), ("My dear", "Too informal.")], "Sir/Madam.")
M("m05", FORMAT, "How many paragraphs should the body usually have?", [("three", ""), ("one long one", "Three short ones."), ("seven", "Three."), ("none", "Three.")], "Purpose, details, request.")
M("m06", STYLE, "Which is suitable in a formal letter?", [("I request you to take immediate action.", ""), ("Do it now or else!", "Rude."), ("Plz do the needful asap", "SMS language."), ("You are useless.", "Rude.")], "Polite and firm.")
M("m07", FORMAT, "Which complimentary close is used for an official you do not know?", [("Yours faithfully", ""), ("Yours lovingly", "Informal."), ("With love", "Informal."), ("Your friend", "Informal.")], "Faithfully.")
M("m08", EDITOR, "A letter to the editor is written mainly to:", [("raise a public issue through a newspaper", ""), ("order goods", "That is an order letter."), ("ask for leave", "That is an application."), ("invite a friend", "That is informal.")], "For public attention.")
M("m09", ORDER, "In a letter placing an order, the items are best shown in:", [("a table with names and quantities", ""), ("a poem", "A table."), ("the subject line", "A table in the body."), ("the signature", "A table in the body.")], "Clear and easy to check.")
M("m10", COMPLAINT, "A letter of enquiry mainly:", [("asks for information", ""), ("complains about service", "That is a complaint."), ("orders goods", "That is an order."), ("thanks someone", "It asks for information.")], "Courses, fees, timings, etc.")
M("m11", FORMAT, "The word limit for the body of the letter is about:", [("100-120 words", ""), ("50 words", "100-120 words."), ("300 words", "100-120 words."), ("20 words", "100-120 words.")], "As in the CBSE paper.")
M("m12", FORMAT, "Which layout is recommended?", [("block format, all lines from the left margin", ""), ("lines centred on the page", "Block format."), ("random alignment", "Block format."), ("right-aligned", "Block format.")], "Neat and modern.")
M("m13", STYLE, "Which should be avoided in formal letters?", [("contractions like 'don't' and 'can't'", ""), ("polite requests", "Keep them."), ("clear paragraphs", "Keep them."), ("a subject line", "Keep it.")], "Write 'do not', 'cannot'.")
M("m14", FORMAT, "If the question gives your name as 'Rohan', you should:", [("sign as Rohan", ""), ("use your real name", "Use the given name."), ("leave it blank", "Use the given name."), ("write 'XYZ'", "Use the given name.")], "Follow the question.")
M("m15", COMPLAINT, "Which detail strengthens a complaint letter?", [("specific facts: dates, duration, effects", ""), ("insults", "Stay polite."), ("jokes", "Stay serious."), ("unrelated stories", "Stay relevant.")], "Facts make it convincing.")
M("m16", EDITOR, "'Through the columns of your esteemed newspaper' is used in:", [("a letter to the editor", ""), ("an order letter", "Editor letter."), ("a leave application", "Editor letter."), ("an informal letter", "Editor letter.")], "A standard opening.")
C.tf("t01", FORMAT, "The subject line comes after the salutation.", False, "It comes before the salutation.")
C.tf("t02", FORMAT, "A formal letter must have a date.", True, "Missing it costs the format mark.")
C.tf("t03", STYLE, "SMS language is acceptable in formal letters.", False, "Use complete, formal English.")
C.tf("t04", FORMAT, "'Yours faithfully' is suitable for letters to officials.", True, "Use it when you do not know the person.")
C.tf("t05", ORDER, "An order letter should mention delivery time and payment mode.", True, "These are essential details.")
C.tf("t06", EDITOR, "A letter to the editor discusses a private family matter.", False, "It discusses a public issue.")
C.tf("t07", FORMAT, "The body of a formal letter should be one long paragraph.", False, "Use three short paragraphs.")
VS = ["1 mark: first point", "1 mark: second point"]
C.q("v1", "very_short_answer", 2, FORMAT, "Write two things that must appear in the subject line of a formal letter.", "easy", answer_steps=["It must begin with 'Subject:'.", "It must state the purpose briefly in one line."], marking_scheme=VS)
C.q("v2", "very_short_answer", 2, STYLE, "Rewrite in formal language: 'Pls fix the road fast, it's v bad.'", "easy", answer_steps=["I request you to repair the road at the earliest.", "Its condition is very poor and dangerous."], marking_scheme=VS)
C.q("v3", "very_short_answer", 2, ORDER, "Name two details a supplier needs in an order letter.", "easy", answer_steps=["The names and quantities of items.", "The delivery date and mode of payment."], marking_scheme=VS)
C.q("v4", "very_short_answer", 2, EDITOR, "Give two features of a good letter to the editor.", "easy", answer_steps=["It raises a public issue with facts and effects.", "It suggests practical solutions in a polite tone."], marking_scheme=VS)
C.q("v5", "very_short_answer", 2, FORMAT, "When do you use 'Yours sincerely' instead of 'Yours faithfully'?", "easy", answer_steps=["When the receiver is addressed by name (Dear Mr Shah).", "'Yours faithfully' is used with 'Sir/Madam'."], marking_scheme=VS)
C.ar("ar1", FORMAT, "The format of a letter carries one mark in CBSE.", "Correct format shows the writer knows formal conventions.", 0,
     "R explains why format is marked.", "format is 1 of 5 marks.", "conventions matter in formal writing.")
C.ar("ar2", STYLE, "'Respected Editor, how are you?' is a good opening.", "Formal letters avoid casual greetings.", 3,
     "A is false; R is true.", "the opening is casual.", "formal letters avoid it.")

chapter = header(9, "Formal Letter Writing", ["letter_format", "complaint_and_enquiry", "order_and_supply", "letter_to_the_editor", "tone_and_language"],
                 "CBSE 2025-26 English Language and Literature (184) Section B Writing: a formal letter (complaint, enquiry, placing an order, or letter to the editor) in 100-120 words, 5 marks, one of two choices.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
