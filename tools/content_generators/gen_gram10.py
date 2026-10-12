"""CBSE Class 10 English Writing Ch 10: Analytical Paragraph Writing (CBSE 184, Section B Writing, 5 marks). Objective items list the right answer first."""
import sys
from grammar_common import Grammar, header

ROOT = sys.argv[1]
PATH = "app_core/content/cbse/class10/english/grammar/ch10_analytical_paragraph"
C = Grammar("gram10ch10")
blk, kc, M = C.blk, C.check_block, C.mcq
STRUCT, VOCAB, TABLE, GRAPH, CUES = ["paragraph_structure"], ["trend_vocabulary"], ["tables_and_bar_charts"], ["line_and_pie_charts"], ["cues_and_comparison"]
MS = ["1 mark: format (title, introduction, body, conclusion)", "1 mark: organisation of ideas", "1 mark: content (key data, comparisons, trend)",
      "1 mark: accuracy (grammar and spelling)", "1 mark: fluency (clear analytical language in 100-120 words)"]
VS = ["1 mark: first point", "1 mark: second point"]

VOCAB_TAB = ("| Movement | Verbs | Nouns / adverbs |\n|---|---|---|\n"
             "| **up** | rose, increased, grew, climbed, doubled | a rise, an increase, sharply, steadily, gradually |\n"
             "| **down** | fell, declined, dropped, decreased, halved | a fall, a decline, slightly, dramatically |\n"
             "| **no change** | remained steady, stayed constant, levelled off | stability |\n"
             "| **highest / lowest** | peaked at, reached a high of, hit a low of | the peak, the lowest point |\n"
             "| **up and down** | fluctuated | fluctuations |\n"
             "| **comparison** | whereas, while, in contrast, compared with, twice as many as | the majority, a quarter, nearly half |")

MODEL_DATA = ("| Year | Students using smartphones for study (%) |\n|---|---|\n| 2019 | 20 |\n| 2020 | 45 |\n| 2021 | 70 |\n| 2022 | 75 |\n| 2023 | 80 |")
MODEL_PARA = ("**Title: Smartphones in Study, 2019-2023**\n\n"
              "The table shows the percentage of students in a city school who used smartphones for study between 2019 and 2023. "
              "In 2019, only one in five students (20%) used a smartphone for learning. The figure more than doubled to 45% in 2020, when schools shifted online during the pandemic, "
              "and rose sharply again to 70% in 2021. After this, the growth slowed: usage increased slightly to 75% in 2022 and reached a peak of 80% in 2023. "
              "Overall, smartphone use for study quadrupled in five years, with the steepest rise between 2019 and 2021. "
              "It can be concluded that digital learning has become a regular part of students' lives, though its growth is now levelling off.")

sections = [
 {"id": "s1", "title": "Turning numbers into words", "blocks": [
  blk("s1.hook", "hook", title="What does this chart say?",
    body="A bar rises, another falls, a pie has one huge slice. An **analytical paragraph** turns such data into clear sentences: what the chart shows, the main trends, and what we can conclude.\n\n"
         "In the board exam it carries **5 marks** for about **100-120 words**. With a fixed plan and the right words, it is one of the easiest places to score."),
  blk("s1.inspiration", "inspiration", title="A statistician who changed health care", person="Florence Nightingale", years="1820–1910",
    body="Florence Nightingale, famous as a nurse, was also a pioneer of statistics. She drew a new kind of chart to show that most soldiers in the Crimean War died from disease, not wounds, and used it to persuade the government to improve hospitals. Data, explained clearly, changed policy.",
    future="Data analysts, journalists, economists and scientists describe charts every day."),
  C.socratic("s1.socratic", "Why should an analytical paragraph not list every number?",
    ["The reader needs the main trends and comparisons, not a copy of the table", "Numbers are always wrong", "The word limit is 20 words"], 0,
    "Select and compare; do not copy."),
 ]},
 {"id": "s2", "title": "Structure and language", "blocks": [
  blk("s2.thm", "theory", title="The four-part plan", revision=True,
    body="**What the exam asks:** describe and analyse a **table, bar chart, line graph, pie chart** or a set of **cues/data** in about **100-120 words** (one of two choices). Marks: format 1, organisation 1, content 1, accuracy 1, fluency 1.\n\n"
         "**1. Title:** a short heading (optional but useful).\n\n"
         "**2. Introduction (1-2 sentences):** what the data shows: topic, place, time period, units. *The bar chart compares... between 2019 and 2023.*\n\n"
         "**3. Body (3-4 sentences):** the **main trend**, the **highest and lowest** values, important **changes** with figures, and **comparisons**. Group similar items; do not describe every number.\n\n"
         "**4. Conclusion (1-2 sentences):** the overall picture and a sensible **inference**: *Overall, ... It can be concluded that...*\n\n"
         "**Language:** use the **past tense** for past data and the **present tense** for what the chart shows (*The chart shows...*). Be objective: no 'I think'. Quote figures exactly."),
  blk("s2.table", "markdown_table", title="Words for trends", revision=True, body=VOCAB_TAB),
  kc("s2.check", "Which sentence makes the best introduction?",
    [("The line graph shows the sale of electric scooters in India from 2018 to 2023.", ""), ("Scooters are good.", "Say what the data shows."), ("In 2020 sales were 5,000.", "That is a detail for the body."), ("I like electric scooters.", "Stay objective.")],
    "Topic, place and period.")
  ,kc("s2.check2", "Which verb describes values going up and down repeatedly?",
    [("fluctuated", ""), ("peaked", "That is the highest point."), ("doubled", "That is a rise to twice."), ("levelled off", "That means no change.")],
    "Fluctuate = rise and fall.")
 ]},
 {"id": "s3", "title": "A model analytical paragraph", "blocks": [
  blk("s3.data", "markdown_table", title="Data: smartphones for study", revision=True, body=MODEL_DATA),
  blk("s3.model", "theory", title="Model answer (about 120 words)", revision=True, body=MODEL_PARA),
  blk("s3.notes", "theory", title="Why this answer scores well", revision=True,
    body="- **Introduction** names the data, place and period.\n- **Body** gives the main trend with exact figures and the phases: sharp rise (2019-2021), slow rise (2021-2023).\n"
         "- **Comparison words**: *more than doubled, rose sharply, increased slightly, reached a peak, quadrupled*.\n- **Conclusion** gives an inference without personal opinion.\n- About 120 words, in clear, formal English."),
  kc("s3.check", "In the model, which phrase shows a comparison over the whole period?",
    [("quadrupled in five years", ""), ("in 2019", "That is one point."), ("the table shows", "That is the introduction."), ("in a city school", "That is the setting.")],
    "From 20% to 80% is four times.")
 ]},
 {"id": "s4", "title": "Different kinds of data", "blocks": [
  blk("s4.thm", "theory", title="Tips for each chart type", revision=True,
    body="| Data | What to focus on |\n|---|---|\n| **Table** | highest and lowest values, biggest changes, groups that behave alike |\n| **Bar chart** | compare categories; rank them; note large gaps |\n"
         "| **Line graph** | overall trend over time; peaks, dips, periods of sharp change or stability |\n| **Pie chart** | largest and smallest shares; express as fractions (nearly half, one quarter) |\n"
         "| **Cues / notes** | link the given points logically; add connectives (moreover, however, as a result) |\n\n"
         "**Useful link words:** *whereas, while, in contrast, similarly, on the other hand, as a result, overall, in conclusion.*"),
  kc("s4.check", "For a pie chart, it is best to:",
    [("describe the largest and smallest shares, using fractions and percentages", ""), ("describe the trend over years", "That suits a line graph."), ("list every slice in order", "Group and compare."), ("give your opinion", "Stay objective.")],
    "Shares of a whole.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **T-I-B-C: Title, Introduction, Body, Conclusion.**\n- **Body = Trend + Top/Bottom + Turning points + Comparison.**\n- **Never 'I think'; always figures + trend words.**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. **Copying every number** from the table: select and compare.\n2. **No introduction or conclusion**: you lose format and organisation marks.\n"
         "3. **Wrong figures or units**: check percentages, years and units.\n4. **Personal opinions** ('I feel it is bad'): give a data-based inference instead.\n5. **Tense errors**: past data in the past tense."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Show a simple class survey chart (favourite sport). In pairs, students write one introduction sentence, two trend sentences and one conclusion, then read aloud."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Find a chart in a newspaper. What is its main message in one sentence?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Maths (Statistics):** reading mean, mode and graphs.\n- **Economics:** describing data on income, employment and development."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="The table shows the number of visitors (in lakhs) to a national park: 2019: 4; 2020: 1; 2021: 2; 2022: 5; 2023: 6. Write an analytical paragraph (100-120 words).\n\n"
         "**Model answer (outline):** Introduction: visitors to the park from 2019 to 2023, in lakhs. Body: 4 lakh in 2019; fell sharply to 1 lakh in 2020 (pandemic restrictions); recovered to 2 lakh in 2021; rose to 5 lakh in 2022, above the 2019 level; reached a peak of 6 lakh in 2023. Conclusion: after a steep fall, tourism recovered strongly and grew by 50% over the 2019 figure, showing renewed interest in wildlife tourism."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- An analytical paragraph describes data in 100-120 words for 5 marks.\n- Plan: title, introduction, body (trend, extremes, changes, comparison), conclusion.\n"
         "- Use trend vocabulary and exact figures; stay objective; use the correct tense."),
  blk("s5.examtips", "exam_tips", title="Exam tips",
    body="- Spend one minute marking the highest, lowest and biggest change on the chart before writing.\n- Begin with 'The table/chart/graph shows...'.\n- End with 'Overall...' or 'It can be concluded that...'."),
  blk("s5.flash1", "flashcard", front="What are the four parts of an analytical paragraph?", back="Title, introduction, body (analysis), conclusion."),
  blk("s5.flash2", "flashcard", front="Give three verbs for an upward trend.", back="rose, increased, climbed (also doubled, soared)."),
  blk("s5.flash3", "flashcard", front="What should the conclusion contain?", back="The overall trend and a data-based inference, without personal opinion."),
  blk("s5.flash4", "flashcard", front="What is the word limit?", back="About 100-120 words."),
 ]},
]

# ---------------- Writing tasks (5 marks each) ----------------
TASKS = [
 ("w1", TABLE, "The table shows the number of books borrowed from a school library per month (Jan 120, Feb 150, Mar 90, Apr 60, May 30, Jun 140). Write an analytical paragraph. (100-120 words)",
  ["Introduction: monthly library borrowing in a school, January to June.", "Body: rise from 120 to a peak of 150 in February; steady fall through March (90) and April (60) to a low of 30 in May.",
   "Body: sharp recovery to 140 in June when the new session began.", "Comparison: February borrowing was five times that of May.", "Conclusion: borrowing falls during exams and vacations and rises when classes resume."]),
 ("w2", TABLE, "The bar chart shows the favourite sports of 200 students: cricket 80, football 50, badminton 40, kabaddi 20, chess 10. Write an analytical paragraph. (100-120 words)",
  ["Introduction: survey of 200 students on favourite sports.", "Body: cricket most popular (80, two-fifths of students).", "Body: football (50) and badminton (40) next; kabaddi (20) and chess (10) least.",
   "Comparison: cricket is preferred by eight times as many students as chess.", "Conclusion: outdoor team sports dominate; indoor games need more promotion."]),
 ("w3", GRAPH, "The line graph shows the average monthly temperature (°C) in Ahmedabad: Jan 20, Mar 28, May 41, Jul 31, Sep 30, Nov 24. Write an analytical paragraph. (100-120 words)",
  ["Introduction: average temperature in Ahmedabad across the year.", "Body: rises steadily from 20°C in January to a peak of 41°C in May.",
   "Body: falls to 31°C in July with the monsoon, remains steady in September (30°C), drops to 24°C by November.", "Comparison: May is about twice as hot as January.",
   "Conclusion: hot summers, milder monsoon and pleasant winters."]),
 ("w4", GRAPH, "The pie chart shows how a family spends its monthly income: food 40%, rent 25%, education 15%, transport 10%, savings 10%. Write an analytical paragraph. (100-120 words)",
  ["Introduction: distribution of a family's monthly income.", "Body: food takes the largest share, two-fifths (40%).", "Body: rent a quarter (25%); education 15%; transport and savings 10% each.",
   "Comparison: food and rent together use about two-thirds of income.", "Conclusion: basic needs dominate; savings are low and could be increased."]),
 ("w5", TABLE, "The table shows the number of electric vehicles sold in a city (2019: 500; 2020: 400; 2021: 1,200; 2022: 3,000; 2023: 5,500). Write an analytical paragraph. (100-120 words)",
  ["Introduction: electric vehicle sales in a city, 2019-2023.", "Body: slight fall from 500 to 400 in 2020.", "Body: sharp rise to 1,200 in 2021, 3,000 in 2022 and a peak of 5,500 in 2023.",
   "Comparison: 2023 sales were eleven times those of 2019.", "Conclusion: rapid growth shows rising acceptance of clean transport."]),
 ("w6", CUES, "Using the cues, write an analytical paragraph on 'Screen time among teenagers': average 2 hours in 2018 → 5 hours in 2023; 60% use phones after 10 p.m.; sleep reduced by 1 hour; 30% report eye strain. (100-120 words)",
  ["Introduction: changes in teenagers' screen time, 2018-2023.", "Body: daily screen time rose from 2 to 5 hours (2.5 times).",
   "Body: 60% use phones late at night; sleep cut by an hour; 30% report eye strain.", "Link words: as a result, moreover.",
   "Conclusion: screen time is rising sharply and affecting health; balance is needed."]),
 ("w7", TABLE, "The bar chart compares the literacy rate (%) of men and women in a state: 2001 M 75, W 50; 2011 M 82, W 62; 2021 M 88, W 75. Write an analytical paragraph. (100-120 words)",
  ["Introduction: male and female literacy rates, 2001-2021.", "Body: male literacy rose from 75% to 88%; female literacy from 50% to 75%.",
   "Body: the gender gap narrowed from 25 to 13 percentage points.", "Comparison: female literacy grew faster (25 points) than male (13 points).",
   "Conclusion: steady progress, especially for women, though a gap remains."]),
 ("w8", GRAPH, "The line graph shows the water level (in metres) of a reservoir: Jan 30, Mar 22, May 12, Jul 25, Sep 38, Nov 35. Write an analytical paragraph. (100-120 words)",
  ["Introduction: reservoir water level through the year.", "Body: falls steadily from 30 m in January to a low of 12 m in May.",
   "Body: rises with the monsoon to 25 m in July and a peak of 38 m in September; slight fall to 35 m in November.", "Comparison: the September level is three times the May level.",
   "Conclusion: water storage depends on the monsoon; summer conservation is needed."]),
 ("w9", TABLE, "The table shows how 100 students travel to school: bus 40, bicycle 25, walk 15, car 12, two-wheeler with parents 8. Write an analytical paragraph. (100-120 words)",
  ["Introduction: modes of travel of 100 students.", "Body: bus most common (40%).", "Body: bicycle 25%, walking 15%, car 12%, two-wheeler 8%.",
   "Comparison: eco-friendly modes (bus, bicycle, walking) account for 80%.", "Conclusion: most students use sustainable transport; car use is limited."]),
 ("w10", CUES, "Using the data, write an analytical paragraph on 'Plastic waste collected by a city' (tonnes per month): 2020: 800; 2021: 700; 2022: 550; 2023: 400. Reason: ban on single-use plastic in 2021. (100-120 words)",
  ["Introduction: monthly plastic waste collected, 2020-2023.", "Body: steady decline from 800 to 400 tonnes.", "Body: sharpest fall after the 2021 ban (700 to 550).",
   "Comparison: waste halved in three years.", "Conclusion: the ban and awareness are working; continued efforts can reduce it further."]),
 ("w11", GRAPH, "The bar chart shows the number of trees planted by a school eco-club: 2019: 50; 2020: 30; 2021: 80; 2022: 120; 2023: 150. Write an analytical paragraph. (100-120 words)",
  ["Introduction: trees planted by the eco-club, 2019-2023.", "Body: dip from 50 to 30 in 2020.", "Body: steady rise to 80, 120 and a peak of 150 in 2023.",
   "Comparison: 2023 planting was five times the 2020 figure.", "Conclusion: growing environmental awareness among students."]),
 ("w12", TABLE, "The table shows the hours students spend daily on activities: study 6, sleep 7, play 1, screens 4, others 6. Write an analytical paragraph. (100-120 words)",
  ["Introduction: average daily time use of students.", "Body: sleep (7 h) and study (6 h) take the most time.", "Body: screens 4 h, play only 1 h, other activities 6 h.",
   "Comparison: screen time is four times play time.", "Conclusion: students need more physical activity and less screen time."]),
]
for id_, concepts, question, steps in TASKS:
    C.q(id_, "long_answer", 5, concepts, question, "medium", answer_steps=steps, marking_scheme=MS)

# ---------------- Short questions ----------------
C.q("v1", "very_short_answer", 2, STRUCT, "Write two things an introduction to an analytical paragraph must state.", "easy", answer_steps=["What the data is about (topic and place).", "The time period and units."], marking_scheme=VS)
C.q("v2", "very_short_answer", 2, VOCAB, "Rewrite with a trend word: 'Sales were 100, then 200.'", "easy", answer_steps=["Sales doubled from 100 to 200.", "(or) Sales rose sharply from 100 to 200."], marking_scheme=VS)
C.q("v3", "very_short_answer", 2, STRUCT, "Give two things a good conclusion does.", "easy", answer_steps=["States the overall trend.", "Gives a sensible inference without personal opinion."], marking_scheme=VS)
C.q("v4", "very_short_answer", 2, GRAPH, "Express as fractions: 50% and 25%.", "easy", answer_steps=["50% is half.", "25% is a quarter."], marking_scheme=VS)

# ---------------- Objective practice ----------------
M("m01", STRUCT, "The word limit for an analytical paragraph is about:", [("100-120 words", ""), ("20 words", "100-120 words."), ("300 words", "100-120 words."), ("500 words", "100-120 words.")], "As in the CBSE paper.")
M("m02", STRUCT, "Which part gives the overall trend and inference?", [("the conclusion", ""), ("the title", "The conclusion."), ("the introduction", "That names the data."), ("the first figure", "The conclusion.")], "Overall...")
M("m03", VOCAB, "'Reached a high of' means the same as:", [("peaked at", ""), ("fell to", "Opposite direction."), ("fluctuated", "Up and down."), ("levelled off", "No change.")], "The highest point.")
M("m04", VOCAB, "Which word shows a small change?", [("slightly", ""), ("sharply", "A big change."), ("dramatically", "A big change."), ("rapidly", "A big change.")], "Slightly = a little.")
M("m05", VOCAB, "From 40 to 20 is best described as:", [("halved", ""), ("doubled", "That is up."), ("tripled", "That is up."), ("remained steady", "It changed.")], "Half of 40 is 20.")
M("m06", STRUCT, "Which should you avoid in an analytical paragraph?", [("personal opinions like 'I think'", ""), ("exact figures", "Keep them."), ("comparison words", "Keep them."), ("a conclusion", "Keep it.")], "Stay objective.")
M("m07", GRAPH, "A line graph is best for showing:", [("change over time", ""), ("shares of a whole", "That is a pie chart."), ("a single number", "Change over time."), ("a map", "Change over time.")], "Trends across years or months.")
M("m08", GRAPH, "A pie chart is best for showing:", [("parts of a whole", ""), ("change over time", "That is a line graph."), ("a timeline", "Parts of a whole."), ("a story", "Parts of a whole.")], "Percentages add up to 100.")
M("m09", VOCAB, "'Whereas' is used to:", [("show contrast between two items", ""), ("show a rise", "It contrasts."), ("end the paragraph", "It contrasts."), ("introduce a title", "It contrasts.")], "Boys..., whereas girls...")
M("m10", STRUCT, "For data about 2019-2023, which tense describes the values?", [("simple past", ""), ("simple future", "Past data, past tense."), ("present continuous", "Past tense."), ("future perfect", "Past tense.")], "Sales rose in 2021.")
M("m11", TABLE, "In a table with many numbers, you should:", [("pick out the highest, lowest and biggest changes", ""), ("copy every number", "Select and compare."), ("ignore the numbers", "Use key figures."), ("describe only the first row", "Cover the whole table.")], "Selection shows analysis.")
M("m12", VOCAB, "'Remained steady' means:", [("did not change much", ""), ("rose sharply", "No change."), ("fell sharply", "No change."), ("went up and down", "That is fluctuated.")], "Stable.")
M("m13", VOCAB, "From 10 to 30 is best described as:", [("tripled", ""), ("doubled", "That would be 20."), ("halved", "That is down."), ("declined", "That is down.")], "Three times.")
M("m14", STRUCT, "Which is the best opening sentence?", [("The bar chart shows the number of visitors to a museum from 2019 to 2023.", ""), ("Museums are boring.", "Opinion."), ("In 2021 there were 300 visitors.", "A detail for the body."), ("I visited a museum.", "Personal.")], "Topic, place and period.")
M("m15", CUES, "Which link word adds a further point?", [("moreover", ""), ("however", "That contrasts."), ("whereas", "That contrasts."), ("in conclusion", "That ends.")], "Moreover = in addition.")
M("m16", GRAPH, "'Nearly half' is a good way to describe:", [("48%", ""), ("10%", "About a tenth."), ("90%", "Nearly all."), ("25%", "A quarter.")], "Close to 50%.")
C.tf("t01", STRUCT, "An analytical paragraph should include an introduction and a conclusion.", True, "They earn format and organisation marks.")
C.tf("t02", STRUCT, "You should give your personal opinion in the conclusion.", False, "Give a data-based inference.")
C.tf("t03", VOCAB, "'Fluctuated' means went up and down.", True, "Values changed irregularly.")
C.tf("t04", TABLE, "Every number in the table must be written in the paragraph.", False, "Select the important figures.")
C.tf("t05", GRAPH, "A pie chart shows percentages of a whole.", True, "They total 100%.")
C.tf("t06", VOCAB, "'Doubled' means increased to twice the earlier value.", True, "From 50 to 100 is doubling.")
C.tf("t07", CUES, "Link words like 'however' and 'moreover' make a paragraph flow better.", True, "They connect ideas logically.")
M("m17", TABLE, "In a bar chart of five categories, the body should mainly:", [("rank and compare the categories", ""), ("describe colours of the bars", "Compare values."), ("copy the title", "Compare values."), ("list unrelated facts", "Compare values.")], "Highest to lowest, with gaps.")
C.ar("ar1", STRUCT, "An analytical paragraph begins by stating what the data shows.", "The reader must know the topic and period before the details.", 0,
     "R explains A.", "the introduction names the data.", "context comes first.")
C.ar("ar2", VOCAB, "'Sales plummeted' describes a small rise.", "'Plummet' means to fall suddenly and steeply.", 3,
     "A is false; R is true.", "plummet is a steep fall.", "it means a sudden fall.")

chapter = header(10, "Analytical Paragraph Writing", ["paragraph_structure", "trend_vocabulary", "tables_and_bar_charts", "line_and_pie_charts", "cues_and_comparison"],
                 "CBSE 2025-26 English Language and Literature (184) Section B Writing: an analytical paragraph on a chart, graph, table, map or cues in 100-120 words, 5 marks, one of two choices.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
