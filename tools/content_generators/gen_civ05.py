"""CBSE Class 10 Political Science Ch 5: Outcomes of Democracy (fully in the 2025-26 board syllabus)."""
import sys
from ss_common import make, header, path, SQP, SHINE, CB

ROOT = sys.argv[1]
SUBJ, N = "civics", 5
PATH = path(SUBJ, "ch05_outcomes_of_democracy")
C = make(SUBJ, N, "civ10ch05")
blk, M, W = C.blk, C.m, C.w
GOV, ECO, SOC, DIG = ["accountable_government"], ["economic_outcomes"], ["social_diversity"], ["dignity_and_freedom"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 5 exercises", "question": n}

GROWTH = ("| Type of regime | Average rate of economic growth, 1950–2000 (%) |\n|---|---|\n| All democracies | 3.95 |\n| All dictatorships | 4.42 |\n| Poor countries under dictatorship | 4.34 |\n| Poor countries under democracy | 4.28 |")
SCORE = ("| Outcome | How democracy does | Main point |\n|---|---|---|\n| **Accountable, responsive, legitimate government** | very good on accountability and legitimacy; weaker on responsiveness and corruption | it is people's own government |\n"
         "| **Economic growth and development** | slightly lower growth than dictatorships, but the difference is negligible | growth depends on many factors |\n"
         "| **Reduction of inequality and poverty** | weak: economic inequality is growing | political equality does not ensure economic equality |\n"
         "| **Accommodation of social diversity** | good: it handles differences peacefully | majority must work with minority |\n"
         "| **Dignity and freedom of citizens** | far superior to other regimes | women and disadvantaged castes gained equal status |")

sections = [
 {"id": "s1", "title": "How good is democracy?", "blocks": [
  blk("s1.hook", "hook", title="A report card for democracy",
    body="Most countries in the world today call themselves democracies. But is democracy really better than other forms of government? Does it make people richer, more equal, freer and safer?\n\n"
         "This chapter gives democracy a fair report card. It looks at five outcomes: whether democracy gives accountable government, economic growth, less inequality, peaceful handling of social differences, and dignity and freedom for citizens."),
  blk("s1.inspiration", "inspiration", title="The right to know", person="Aruna Roy", years="born 1946",
    body="**Aruna Roy** left the Indian Administrative Service in 1975 to work with poor villagers in Rajasthan. In 1990 she helped found the **Mazdoor Kisan Shakti Sangathan (MKSS)**, which held public hearings where villagers checked official records of wages and public works.\n\n"
         "Their campaign for the right to know helped bring about India's **Right to Information Act, 2005**. It shows how citizens can make a democratic government more transparent and accountable.",
    future="This chapter leads to careers in public administration, law, journalism, development work and policy analysis."),
  C.socratic("s1.socratic", "Why do people complain more about governments in democracies than in dictatorships?",
    ["Because in a democracy citizens are free to examine and criticise the government", "Because democracies always perform worse", "Because dictatorships solve every problem"], 0,
    "Complaints are themselves a sign that people expect more and are free to say so."),
 ]},
 {"id": "s2", "title": "Accountable, responsive and legitimate government", "blocks": [
  blk("s2.thm", "theory", title="How do we assess democracy's outcomes?", revision=True,
    body="**Why democracy is better:** compared with other forms of government, democracy:\n"
         "- promotes **equality** among citizens;\n- enhances the **dignity** of the individual;\n- improves the **quality of decision making**;\n- provides a method to **resolve conflicts**; and\n- allows room to **correct mistakes**.\n\n"
         "But we must be careful: democracy is only a **form of government**. It can only create **conditions** for achieving something. The citizens have to take advantage of those conditions and achieve those goals.\n\n"
         "**Accountable government:** the most basic outcome of democracy is that it produces a government that is **accountable to the citizens**, and **responsive** to the needs and expectations of the citizens.\n"
         "- In a democracy, people have the right to **choose their rulers** and have **control over the rulers**. Whenever possible and necessary, citizens should be able to participate in decision making that affects them all.\n"
         "- **Slower but better decisions:** democracy is based on the idea of **deliberation and negotiation**, so some delay is bound to take place. A non-democratic government may be very quick and efficient in decision making, but its decisions may not be accepted by the people and may face problems. A democratic government takes more time, but because it follows procedures, its decisions may be **more acceptable** to the people and **more effective**. The cost of time that democracy pays is perhaps worth it.\n"
         "- **Transparency:** a citizen who wants to know if a decision was taken through the correct procedures can find this out. She has the **right and the means to examine the process** of decision making. This is missing from a non-democratic government. India's **Right to Information Act, 2005** gives citizens a legal right to ask for government information.\n\n"
         "**How democracy does on these points:**\n"
         "- Democracies have developed mechanisms for citizens to take part: **regular, free and fair elections**; **open public debate** on major policies and legislation; and citizens' **right to information** about the government and its functioning.\n"
         "- But democracies often **frustrate the needs** of the people and often **ignore the demands of a majority** of their population. The routine tales of **corruption** are enough to show that democracy is not free of this evil, though nothing shows that non-democracies are less corrupt.\n\n"
         "**Legitimate government:** there is one respect in which democratic government is certainly better than its alternatives: it is a **legitimate government**. It may be slow, less efficient, not always very responsive or clean, but a democratic government is **people's own government**. That is why there is an overwhelming support for the idea of democracy all over the world; people in South Asia, for example, strongly prefer democracy, and they want to be ruled by representatives elected by them."),
  C.kc("s2.check", "Why may a democratic government take more time to decide?",
    [("Because it is based on deliberation and negotiation", ""), ("Because it has no rules", "It follows procedures."), ("Because it never takes decisions", "It does take decisions."), ("Because citizens cannot participate", "Citizens can participate.")],
    "Its decisions may be slower but more acceptable and effective."),
  C.kc("s2.check2", "The most basic outcome of democracy is a government that is:",
    [("accountable to the citizens and responsive to their needs", ""), ("always the fastest in taking decisions", "Dictatorships may be faster."), ("free of all corruption", "Democracies are not free of corruption."), ("run by one leader for life", "That is not democracy.")],
    "Citizens choose and control their rulers."),
 ]},
 {"id": "s3", "title": "Economic growth, inequality and poverty", "blocks": [
  blk("s3.thm", "theory", title="Does democracy make people richer and more equal?", revision=True,
    body="**Economic growth and development:** if we consider all democracies and all dictatorships for the fifty years between **1950 and 2000**, dictatorships have a **slightly higher rate of economic growth**. The inability of democracy to achieve higher economic development worries us, but this alone cannot be the reason to reject democracy.\n"
         "- **Economic development depends on several factors**: the country's **population size**, the **global situation**, **cooperation from other countries**, the **economic priorities** adopted by the country, and so on.\n"
         "- The difference in the rates of economic development between less developed countries with dictatorships and democracies is **negligible**. Overall, we cannot say that democracy is a guarantee of economic development. But we can expect democracy not to lag far behind dictatorships in this respect. When there is such a small difference, it is better to prefer democracy, as it has several other positive outcomes.\n\n"
         "**Economic outcomes and inequality:** can we expect democracy to reduce economic inequality? Democracies are based on **political equality**: all individuals have **equal weight** in electing representatives. But we find growing **economic inequalities**:\n"
         "- A small number of **ultra-rich** enjoy a highly disproportionate share of wealth and incomes. Not only that, their share in the total income of the country has been increasing.\n"
         "- Those at the **bottom of the society** have very little to depend upon. Their incomes have been declining. Sometimes they find it difficult to meet their basic needs of life, such as food, clothing, house, education and health.\n"
         "- In actual life, democracies do not appear to be very successful in reducing economic inequalities. The **poor constitute a large proportion of voters**, and no party will like to lose their votes. Yet democratically elected governments do not appear to be as keen to address the question of poverty as you would expect them to.\n"
         "- The situation is much worse in some other countries. In **Bangladesh**, more than half of the population lived in poverty (NCERT). People in several poor countries are now dependent on the rich countries even for food supplies."),
  blk("s3.table", "markdown_table", title="Rates of economic growth for different regimes, 1950–2000 (NCERT)", revision=True, body=GROWTH),
  C.kc("s3.check", "Between 1950 and 2000, which had a slightly higher average rate of economic growth?",
    [("dictatorships", ""), ("democracies", "Democracies were slightly lower (3.95% against 4.42%)."), ("both were exactly equal", "Dictatorships were slightly higher."), ("monarchies only", "The comparison was between democracies and dictatorships.")],
    "But the difference among poor countries was negligible."),
  C.kc("s3.check2", "Democracy is based on political equality, which means:",
    [("every individual has equal weight in electing representatives", ""), ("every individual has equal income", "That is economic equality, which democracy has not achieved."),
     ("only the rich can vote", "Every adult has one vote."), ("there is no poverty", "Poverty still exists in democracies.")],
    "Political equality does not ensure economic equality."),
 ]},
 {"id": "s4", "title": "Social diversity, dignity and freedom", "blocks": [
  blk("s4.thm", "theory", title="Accommodating differences and respecting every citizen", revision=True,
    body="**Accommodation of social diversity:** democracies usually develop a procedure to conduct their **competition**. This **reduces the possibility of tensions** becoming explosive or violent.\n"
         "- No society can fully and permanently resolve conflicts among different groups. But we can certainly learn to **respect these differences**, and we can also evolve mechanisms to negotiate the differences. Democracy is best suited to produce this outcome. **Belgium** successfully negotiated differences among ethnic groups.\n"
         "- Non-democratic regimes often turn a blind eye to or **suppress** internal social differences. The ability to handle social differences, divisions and conflicts is thus a **definite plus point** of democratic regimes. But the example of **Sri Lanka** reminds us that a democracy must fulfil two conditions to achieve this outcome:\n"
         "  1. **Democracy is not simply rule by majority opinion.** The majority always needs to work with the minority so that governments function to represent the general view. Majority and minority opinions are not permanent.\n"
         "  2. **Rule by majority must not become rule by majority community** in terms of religion, race or linguistic group. Rule by majority means that in case of every decision or every election, **different persons and groups may form a majority**. Democracy remains democracy only as long as **every citizen has a chance of being in majority** at some point of time. If someone is barred from being in majority on the basis of birth, the democratic rule ceases to be accommodative for that person or group.\n\n"
         "**Dignity and freedom of the citizens:** democracy stands much **superior** to any other form of government in promoting the **dignity and freedom of the individual**. Every individual wants to receive respect from fellow beings. Often conflicts arise among individuals because some feel that they are not treated with due respect.\n"
         "- **Dignity of women:** most societies across the world were historically male-dominated. Long struggles by women have created some sensitivity today that respect and equal treatment of women are necessary ingredients of a democratic society. This does not mean that women are always treated with respect, but once the principle is recognised, it becomes easier for women to wage a struggle against what is now unacceptable legally and morally. In a non-democratic set-up, this unacceptability would not have had legal basis, because the principle of individual freedom and dignity would not have had the legal and moral force there.\n"
         "- **Caste inequalities:** democracy in India has **strengthened the claims of the disadvantaged and discriminated castes** for equal status and equal opportunity. There are instances still of caste-based inequalities and atrocities, but these lack the **moral and legal foundations**.\n\n"
         "**Expectations from democracy:** democracy is not a magic solution for all problems. As people get some benefits of democracy, they ask for more and want to make democracy even better. That is why, when we ask people about the way democracy functions, they will always come up with more expectations and many complaints. The fact that people are complaining is itself a **testimony to the success of democracy**: it shows that people have developed awareness and the ability to expect and to look critically at power holders and the high and mighty. A public expression of dissatisfaction with democracy shows the success of the democratic project: it transforms people from the status of a **subject** into that of a **citizen**. Most individuals today believe that their **vote makes a difference** to the way the government is run and to their own self-interest."),
  blk("s4.table", "markdown_table", title="Democracy's report card", revision=True, body=SCORE),
  C.kc("s4.check", "For a democracy to accommodate social diversity, it is necessary that:",
    [("every citizen has a chance of being in majority at some point of time", ""), ("one community always forms the majority", "That makes democracy non-accommodative."),
     ("the minority has no say", "The majority must work with the minority."), ("differences are suppressed", "Suppression is what non-democracies do.")],
    "Rule by majority must not become rule by a majority community."),
  C.kc("s4.check2", "Why are people's complaints about democracy a sign of its success?",
    [("They show that people have become citizens who expect more and look critically at power holders", ""), ("They show that democracy has failed", "Complaints show awareness, not failure."),
     ("They show that people want a dictatorship", "Support for democracy remains overwhelming."), ("They show that elections are not held", "Elections are held regularly.")],
    "Democracy transforms people from subjects into citizens."),
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Why democracy is better: \"E-D-Q-C-C\"**: Equality, Dignity, Quality of decisions, Conflict resolution, Correct mistakes.\n- **Government: \"A-R-L\"**: Accountable, Responsive, Legitimate (legitimacy is democracy's surest strength).\n"
         "- **Growth numbers: \"Dictator 4.42 > Democracy 3.95\"** (1950–2000), but the gap among poor countries is tiny (4.34 against 4.28).\n"
         "- **Growth factors: \"P-G-C-P\"**: Population, Global situation, Cooperation, Priorities.\n"
         "- **Diversity conditions: \"Not just majority; Not majority community\".**\n- **Subjects to citizens**: complaints mean success."),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying democracies always have higher economic growth: dictatorships had **slightly higher** growth from 1950 to 2000.\n2. Saying democracy removed economic inequality: economic inequality is **growing**; democracy ensures **political** equality.\n"
         "3. Saying a democratic government is the fastest decision maker: it is **slower**, but its decisions are more acceptable and effective.\n"
         "4. Saying democracy means majority rule only: the majority must **work with the minority**, and the majority must not be a fixed community.\n"
         "5. Saying democracies are free of corruption: they are not, but their governments are **legitimate**.\n6. Treating complaints as failure: complaints show people have become **citizens**."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Make a five-row 'report card' on the board for democracy in India (accountability, economic growth, inequality, social diversity, dignity). Let groups give a grade with one piece of evidence for each, then compare grades and discuss why they differ."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Think of one public problem in your area (roads, water, school). Which democratic tool could a citizen use to get it solved: voting, RTI, a petition, the media, or a local representative?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Chapter 1 (Power-sharing):** Belgium and Sri Lanka and the accommodation of diversity.\n- **Chapter 3 (Gender, Religion and Caste):** dignity of women and disadvantaged castes.\n"
         "- **Economics Chapter 1 (Development):** growth, income and other goals of development."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="'Democracy is better than any other form of government.' Evaluate this statement in about 120 words, using the outcomes of democracy.\n\n"
         "**Model answer:** Democracy produces an accountable, responsive and legitimate government: citizens choose and control their rulers through regular, free and fair elections, open debate and the right to information. Its decisions may be slower, but they are more acceptable and effective. "
         "It accommodates social diversity by letting groups compete peacefully, as in Belgium, and it promotes the dignity and freedom of individuals, including women and disadvantaged castes. "
         "However, democracy has not done well on reducing economic inequality and poverty, and dictatorships had slightly higher growth between 1950 and 2000, though the difference among poor countries is negligible. "
         "On balance, democracy is better because it is people's own government and allows mistakes to be corrected."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Democracy promotes equality and dignity, improves decision making, resolves conflicts and allows mistakes to be corrected; it creates conditions, which citizens must use.\n"
         "- It produces accountable, responsive and legitimate government; decisions are slower but more acceptable, and transparency is built in.\n"
         "- Dictatorships grew slightly faster (1950–2000), but growth depends on many factors and the gap is small.\n"
         "- Democracy ensures political equality, but economic inequality and poverty remain serious problems.\n"
         "- It accommodates social diversity if the majority works with the minority and no community is a permanent majority.\n"
         "- It is far superior in promoting dignity and freedom; complaints about democracy show its success, as people become citizens."),
  blk("s5.examtips", "exam_tips", title="Board exam tips",
    body="- The 2025-26 sample paper asked for three arguments that democracy leads to a peaceful and harmonious life (accommodating social divisions, conducting competition, respecting differences, majority working with minority, no permanent majority community).\n"
         "- 3/5-mark favourites: accountable, responsive and legitimate government; economic outcomes; conditions for accommodating diversity; dignity and freedom.\n"
         "- Use the Belgium and Sri Lanka examples from Chapter 1 when writing about social diversity."),
  blk("s5.flash1", "flashcard", front="What is a legitimate government?", back="A government that is people's own government, chosen by them; democracy may be slow or less efficient, but it is legitimate."),
  blk("s5.flash2", "flashcard", front="What is transparency in a democracy?", back="The right and the means of citizens to examine the process of decision making, for example through the Right to Information."),
  blk("s5.flash3", "flashcard", front="On what factors does economic development depend?", back="Population size, the global situation, cooperation from other countries and the economic priorities adopted by the country."),
  blk("s5.flash4", "flashcard", front="What are the two conditions for democracy to accommodate social diversity?", back="It is not simply rule by majority opinion (the majority works with the minority), and rule by majority does not become rule by a majority community."),
 ]},
]

# ---------------- Sample paper ----------------
W("sqp26", "short_answer", SOC, "'Democracy leads to peaceful and harmonious life among citizens in every sphere.' Support this statement with suitable arguments.",
  ["Democracies accommodate various social divisions; for example, Belgium peacefully solved its ethnic problems. Democracies develop a procedure to conduct competition (elections, power sharing), which reduces the chance of tensions turning violent.",
   "Democracy teaches people to respect differences and resolve conflicts among groups peacefully, while non-democratic rulers ignore or suppress differences, as in Sri Lanka.",
   "Democracy is not just rule by majority opinion: the majority works with the minority, and rule by majority does not become rule by one religious, racial or linguistic community, so every citizen has a chance to be in the majority."], source=SQP(26))

# ---------------- NCERT exercises ----------------
W("ex1", "long_answer", GOV, "How does democracy produce an accountable, responsive and legitimate government?",
  ["Accountable: people have the right to choose their rulers and control over them through regular, free and fair elections.",
   "Open public debate on major policies and legislation, and citizens' right to information about the government, make the government answerable.",
   "Transparency: citizens have the right and the means to examine the process of decision making, for example through the Right to Information Act, 2005.",
   "Responsive: decisions are based on deliberation and negotiation, so they may be slower but more acceptable and effective; elected governments must respond to people's needs to win again.",
   "Legitimate: even if it is slow or less efficient, a democratic government is people's own government, which is why support for democracy is overwhelming."], source=ex("1"))
W("ex2", "short_answer", SOC, "What are the conditions under which democracies accommodate social diversities?",
  ["Democracy is not simply rule by majority opinion: the majority always needs to work with the minority so that the government represents the general view.",
   "Rule by majority must not become rule by a majority community in terms of religion, race or linguistic group.",
   "Every citizen must have a chance of being in the majority at some point of time; if anyone is barred from it on the basis of birth, democracy stops being accommodative."], source=ex("2"))
W("ex3", "short_answer", ECO, "Give arguments to refute the assertion: 'Industrialised countries can afford democracy but the poor need dictatorship to become rich.'",
  ["Between 1950 and 2000, dictatorships grew only slightly faster than democracies, and among poor countries the difference (4.34% against 4.28%) is negligible.",
   "Economic development depends on several factors such as population size, the global situation, cooperation from other countries and economic priorities, not on dictatorship.",
   "Democracy also gives other benefits, such as accountable and legitimate government, dignity and freedom, so it is better to prefer democracy."], source=ex("3"))
M("ex5", ECO, "In the context of democracies, which of the following ideas is correct? Democracies have successfully eliminated:",
  [("the idea of political inequality", ""), ("conflicts among people", "Democracies handle conflicts but do not eliminate them."), ("economic inequalities among people", "Economic inequality is growing."), ("differences of opinion about how marginalised sections are to be treated", "Such differences remain.")],
  "Every citizen has one vote and equal weight in electing representatives.", "medium", ex("5"), correct=0)
M("ex6", GOV, "In the context of assessing democracy, which among the following is the odd one out? Democracies need to ensure:",
  [("majority rule", ""), ("free and fair elections", "This is needed."), ("dignity of the individual", "This is needed."), ("equal treatment before law", "This is needed.")],
  "Democracy is not simply majority rule; the majority must work with the minority.", "medium", ex("6"), correct=0)
M("ex7", ECO, "Studies on political and social inequalities in democracy show that:",
  [("inequalities exist in democracies", ""), ("democracy and development go together", "Democracy does not guarantee development."), ("inequalities do not exist under dictatorship", "They exist there too."), ("dictatorship is better than democracy", "This is not what the studies show.")],
  "Economic inequality is growing even in democracies.", "medium", ex("7"), correct=0)
W("ex8", "case_based", GOV, "Read the passage and answer the questions.\n\n*Nannu is a daily wage earner. He lives in Welcome Mazdoor Colony, a slum habitation in East Delhi. He lost his ration card and applied for a duplicate one. He made several rounds to the local Food and Civil Supplies office for the next three months. But the clerks and officials would not even look at him, leave alone do his job or bother to tell him the status of his application. Ultimately, he filed an application under the Right to Information Act asking for the daily progress made on his application, names of the officials who were supposed to act on his application and what action would be taken against these officials for their inaction. Within a week of filing the application under the Right to Information Act, he was visited by an inspector from the Food Department, who informed him that the card had been made and he could collect it from the office.* (NCERT)\n\n"
  "(i) What does Nannu's example show about democracy? (1)\n\n(ii) Which right did Nannu use? (1)\n\n(iii) How does this right make the government accountable? (2)",
  ["(i) Ordinary citizens in a democracy can make the government work and respond to their needs.", "(ii) The Right to Information (Right to Information Act, 2005).",
   "(iii) It gives citizens the right and the means to examine the process of decision making and ask officials about delays, so officials know they can be questioned and act faster."], source=ex("8"))

# ---------------- MCQs ----------------
M("mcq01", GOV, "Which is NOT a reason why democracy is better than other forms of government?",
  [("It guarantees the fastest economic growth", ""), ("It promotes equality among citizens", "This is a reason."), ("It enhances the dignity of the individual", "This is a reason."), ("It allows room to correct mistakes", "This is a reason.")], "Democracy does not guarantee faster growth.")
M("mcq02", GOV, "Democracy can only create conditions for achieving goals; achieving them depends on:",
  [("citizens taking advantage of those conditions", ""), ("the army", "It depends on citizens."), ("foreign countries", "It depends on citizens."), ("one strong leader", "It depends on citizens.")], "Democracy is only a form of government.")
M("mcq03", GOV, "The most basic outcome of democracy is a government that is:",
  [("accountable to citizens and responsive to their needs", ""), ("free of all mistakes", "Democracies make mistakes but can correct them."), ("always the richest", "Democracy does not guarantee wealth."), ("run without elections", "Elections are essential.")], "Citizens choose and control their rulers.")
M("mcq04", GOV, "A non-democratic government may be quicker in decisions, but its decisions:",
  [("may not be accepted by the people and may face problems", ""), ("are always better", "Not necessarily."), ("are always more transparent", "Non-democracies lack transparency."), ("are made after public debate", "Public debate is a feature of democracy.")], "Democratic decisions are slower but more acceptable.")
M("mcq05", GOV, "Transparency in a democracy means that citizens:",
  [("have the right and means to examine the process of decision making", ""), ("can make laws themselves", "Legislatures make laws."), ("can ignore government decisions", "That is not transparency."), ("are not told about decisions", "That is the opposite.")], "It is missing in non-democratic governments.")
M("mcq06", GOV, "India's Right to Information Act was passed in:",
  [("2005", ""), ("1950", "That is when the Constitution came into force."), ("1976", "That is the Equal Remuneration Act."), ("1992", "That is the local government amendment.")], "It gives citizens a legal right to government information.")
M("mcq07", GOV, "Which is a mechanism through which citizens take part in decision making in democracies?",
  [("regular, free and fair elections", ""), ("secret decisions by rulers", "This is not democratic."), ("ban on public debate", "Democracies have open debate."), ("censorship of the press", "This is not democratic.")], "Open public debate and the right to information are others.")
M("mcq08", GOV, "Democracies often fall short of expectations because they:",
  [("frustrate the needs of people and ignore demands of the majority at times", ""), ("never hold elections", "They hold elections."), ("have no laws", "They have laws."), ("cannot correct mistakes", "They can correct mistakes.")], "Corruption also remains a problem.")
M("mcq09", GOV, "In which respect is democratic government certainly better than its alternatives?",
  [("it is a legitimate government", ""), ("it is always the most efficient", "It may be slow or less efficient."), ("it is always free of corruption", "Democracies face corruption."), ("it never makes mistakes", "It makes mistakes but can correct them.")], "It is people's own government.")
M("mcq10", ECO, "According to NCERT, the average rate of economic growth of all democracies from 1950 to 2000 was:",
  [("3.95%", ""), ("4.42%", "That was all dictatorships."), ("4.34%", "That was poor countries under dictatorship."), ("4.28%", "That was poor countries under democracy.")], "Dictatorships grew slightly faster.")
M("mcq11", ECO, "Economic development of a country depends on:",
  [("population size, global situation, cooperation from other countries and economic priorities", ""), ("only the type of government", "It depends on several factors."),
   ("only the number of political parties", "It depends on several factors."), ("only the size of the army", "It depends on several factors.")], "Democracy alone does not decide growth.")
M("mcq12", ECO, "Why should we prefer democracy even if its growth is slightly lower?",
  [("because the difference is small and democracy has several other positive outcomes", ""), ("because democracies always grow faster", "They grew slightly slower."),
   ("because dictatorships never grow", "Dictatorships did grow."), ("because growth does not matter at all", "Growth matters, but it is not the only outcome.")], "Accountability, dignity and freedom matter too.")
M("mcq13", ECO, "Political equality in a democracy means that:",
  [("all individuals have equal weight in electing representatives", ""), ("everyone earns the same", "That is economic equality."), ("everyone holds a government job", "That is not political equality."), ("only educated people vote", "Every adult has one vote.")], "One person, one vote, one value.")
M("mcq14", ECO, "What has been happening to the share of the ultra-rich in total income?",
  [("it has been increasing", ""), ("it has been decreasing", "It has been increasing."), ("it has stayed exactly the same", "It has been increasing."), ("it has become zero", "That is not true.")], "Economic inequality is growing.")
M("mcq15", ECO, "Why is it surprising that democracies do not do more about poverty?",
  [("because the poor form a large proportion of voters", ""), ("because the poor cannot vote", "They can vote."), ("because there is no poverty in democracies", "Poverty exists."), ("because only the rich vote", "Everyone votes.")], "No party wants to lose the votes of the poor.")
M("mcq16", ECO, "Which country is given in NCERT as an example where more than half the population lived in poverty?",
  [("Bangladesh", ""), ("Belgium", "Belgium is a rich country."), ("USA", "That is not the example."), ("Switzerland", "That is not the example.")], "People in some poor countries depend on rich countries even for food.")
M("mcq17", SOC, "Democracies reduce the chance of social tensions becoming violent because they:",
  [("develop procedures to conduct competition", ""), ("suppress all differences", "That is what non-democracies do."), ("ban all groups", "They do not."), ("allow only one community to rule", "That is not democratic.")], "Elections and power sharing are such procedures.")
M("mcq18", SOC, "Which country successfully negotiated differences among ethnic groups?",
  [("Belgium", ""), ("Sri Lanka", "Sri Lanka faced civil war."), ("Pakistan", "That is not the NCERT example."), ("Myanmar", "That is not the NCERT example.")], "This is from Chapter 1.")
M("mcq19", SOC, "Non-democratic regimes usually deal with social differences by:",
  [("turning a blind eye to them or suppressing them", ""), ("negotiating them openly", "That is democracy."), ("holding free elections", "That is democracy."), ("sharing power with all groups", "That is democracy.")], "Handling differences is a plus point of democracy.")
M("mcq20", SOC, "Democracy is not simply rule by majority opinion; the majority always needs to:",
  [("work with the minority", ""), ("ignore the minority", "That is majoritarianism."), ("rule permanently", "Majorities change."), ("ban minority parties", "That is not democratic.")], "Governments must represent the general view.")
M("mcq21", SOC, "Democracy stops being accommodative for a person or group when:",
  [("they are barred from being in the majority on the basis of birth", ""), ("they lose one election", "Losing an election is normal."), ("they form a new party", "That is part of democracy."), ("they criticise the government", "Criticism is part of democracy.")], "Every citizen must have a chance of being in the majority.")
M("mcq22", SOC, "Which country's example shows that a democracy must meet conditions to accommodate diversity?",
  [("Sri Lanka", ""), ("Belgium", "Belgium shows success."), ("Switzerland", "That is not the NCERT example."), ("Canada", "That is not the NCERT example.")], "Majoritarian measures there led to civil war.")
M("mcq23", DIG, "In promoting the dignity and freedom of the individual, democracy is:",
  [("far superior to any other form of government", ""), ("worse than dictatorship", "It is superior."), ("equal to monarchy", "It is superior."), ("not concerned with dignity", "Dignity is central to democracy.")], "Everyone wants to be treated with respect.")
M("mcq24", DIG, "Once respect and equal treatment of women are accepted as principles in a democracy:",
  [("it becomes easier for women to struggle against what is legally and morally unacceptable", ""), ("women are always treated with respect", "Not always, but the struggle becomes easier."),
   ("women no longer need laws", "Laws are needed."), ("men lose the right to vote", "That is not true.")], "These principles have legal and moral force in a democracy.")
M("mcq25", DIG, "Democracy in India has strengthened the claims of:",
  [("disadvantaged and discriminated castes for equal status and opportunity", ""), ("only the upper castes", "It strengthened disadvantaged castes."), ("kings and landlords", "It weakened their old power."), ("foreign companies", "That is not the point.")], "Caste atrocities still occur but lack moral and legal foundations.")
M("mcq26", DIG, "Caste-based inequalities and atrocities in a democracy:",
  [("lack moral and legal foundations", ""), ("are allowed by law", "They are illegal."), ("are approved by the Constitution", "The Constitution prohibits them."), ("no longer exist anywhere", "They still occur.")], "People can fight them legally.")
M("mcq27", DIG, "People's complaints about democracy show that:",
  [("democracy has transformed them from subjects into citizens", ""), ("democracy has completely failed", "Complaints are a sign of success."), ("people want to stop voting", "They believe their vote matters."), ("dictatorship is popular", "Support for democracy is overwhelming.")], "They expect more from power holders.")
M("mcq28", DIG, "Most individuals in democracies today believe that:",
  [("their vote makes a difference to the way government is run", ""), ("voting is useless", "They believe it matters."), ("only leaders matter", "They believe their vote matters."), ("elections should be stopped", "They support elections.")], "This is a sign of democratic success.")
M("mcq29", GOV, "Democracy is said to 'allow room to correct mistakes' because:",
  [("public debate and elections let wrong decisions be changed", ""), ("leaders never make mistakes", "They make mistakes."), ("decisions cannot be questioned", "They can be questioned."), ("there are no elections", "Elections are held.")], "Mistakes cannot be hidden for long in a democracy.")
M("mcq30", SOC, "Which statement about conflict in societies is correct?",
  [("No society can fully and permanently resolve conflicts, but democracy helps negotiate them", ""), ("Democracies have removed all conflicts", "Conflicts remain."),
   ("Dictatorships resolve conflicts better", "They suppress them."), ("Conflicts never arise in democracies", "They do arise.")], "Respecting differences is the key.")
# ---------------- True / false ----------------
C.tf("tf1", ECO, "From 1950 to 2000, democracies had a higher average rate of economic growth than dictatorships.", False, "Dictatorships had a slightly higher rate (4.42% against 3.95%).")
C.tf("tf2", GOV, "A democratic government is a legitimate government.", True, "It is people's own government, even if slow or less efficient.")
C.tf("tf3", ECO, "Democracies have been very successful in reducing economic inequalities.", False, "Economic inequality is growing in many democracies.")
C.tf("tf4", SOC, "Democracy is simply rule by majority opinion.", False, "The majority must work with the minority, and must not be a fixed community.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", GOV, "Why may democratic decisions take more time but be more effective?",
  ["Democracy is based on deliberation and negotiation, so decisions take time.", "Because they follow procedures and involve people, the decisions are more acceptable to the people and more effective."])
W("vsa2", "very_short_answer", ECO, "Why can we not say that democracy guarantees economic development?",
  ["Between 1950 and 2000, dictatorships had a slightly higher rate of growth than democracies.", "Economic development depends on several factors such as population size, the global situation, cooperation from other countries and economic priorities."])
W("vsa3", "very_short_answer", DIG, "How has democracy helped women and disadvantaged castes?",
  ["Long struggles in democracies made respect and equal treatment of women accepted principles, so women can fight what is legally and morally unacceptable.", "Democracy strengthened the claims of disadvantaged castes for equal status and opportunity; caste atrocities now lack moral and legal foundations."])
W("sa1", "short_answer", ECO, "'Democracies have not been very successful in reducing economic inequality.' Explain.",
  ["Democracies are based on political equality, giving every individual equal weight in electing representatives, but economic inequality is growing.",
   "A small number of ultra-rich enjoy a highly disproportionate and increasing share of wealth and income, while those at the bottom find it hard to meet basic needs.",
   "Though the poor form a large proportion of voters, elected governments are not as keen to address poverty as expected; in some countries like Bangladesh, more than half the people lived in poverty."])
W("sa2", "short_answer", GOV, "'Democracy is accountable but not always responsive.' Explain.",
  ["Democracies have mechanisms of accountability: regular, free and fair elections, open public debate and citizens' right to information.",
   "But democracies often frustrate the needs of the people and ignore the demands of a majority of the population.",
   "Corruption also remains, though there is no evidence that non-democracies are less corrupt; still, a democratic government is legitimate as it is people's own government."])
W("sa3", "short_answer", DIG, "Why are complaints about democracy a testimony to its success?",
  ["As people get some benefits of democracy, they ask for more and want to make democracy better.",
   "Complaints show that people have developed awareness and the ability to look critically at power holders.",
   "Democracy has transformed people from subjects into citizens, and most believe their vote makes a difference."])
W("la1", "long_answer", SOC, "How does democracy accommodate social diversity? What conditions are necessary for it?",
  ["Democracies develop a procedure to conduct competition among groups, such as elections and power sharing, which reduces the chance of tensions becoming violent.",
   "No society can fully resolve conflicts, but democracy teaches people to respect differences and evolves ways to negotiate them; Belgium is an example.",
   "Non-democratic regimes ignore or suppress differences, so handling diversity is a plus point of democracy; Sri Lanka shows what happens when conditions are not met.",
   "Condition 1: democracy is not simply rule by majority opinion; the majority must work with the minority so that the government represents the general view.",
   "Condition 2: rule by majority must not become rule by a majority community of religion, race or language; every citizen must have a chance of being in the majority at some time."])
W("la2", "long_answer", GOV, "Assess democracy on the basis of its outcomes.",
  ["Government: democracy produces accountable and legitimate government through elections, open debate and the right to information, though it is not always responsive and corruption remains.",
   "Economic growth: dictatorships grew slightly faster from 1950 to 2000, but the difference is negligible and growth depends on many factors.",
   "Inequality and poverty: democracy ensures political equality, but economic inequality is growing and poverty remains a serious problem.",
   "Social diversity: democracy handles social differences peacefully if the majority works with the minority and no community is a permanent majority.",
   "Dignity and freedom: democracy is far superior in promoting the dignity of individuals, women and disadvantaged castes; overall it is better because it is people's own government."])
W("cb1", "case_based", ECO, "Read the source and answer the questions.\n\n*\"If you consider all democracies and all dictatorships for the fifty years between 1950 and 2000, dictatorships have slightly higher rate of economic growth. The inability of democracy to achieve higher economic development worries us. But this alone cannot be reason to reject democracy. Economic development depends on several factors.\"* (NCERT)\n\n"
  "(i) Which regime had a slightly higher growth rate between 1950 and 2000? (1)\n\n(ii) Name any two factors on which economic development depends. (1)\n\n(iii) Why should we still prefer democracy? (2)",
  ["(i) Dictatorships.", "(ii) Any two: population size; the global situation; cooperation from other countries; the economic priorities adopted by the country.",
   "(iii) The difference in growth rates, especially among poor countries, is negligible, and democracy has several other positive outcomes such as accountable and legitimate government, dignity and freedom."])
W("cb2", "case_based", DIG, "Read the source and answer the questions.\n\n*\"Democracy stands much superior to any other form of government in promoting dignity and freedom of the individual. Every individual wants to receive respect from fellow beings. Often conflicts arise among individuals because some feel that they are not treated with due respect.\"* (NCERT)\n\n"
  "(i) In which respect is democracy superior to other forms of government according to the source? (1)\n\n(ii) Why do conflicts often arise among individuals? (1)\n\n(iii) How has democracy helped women and disadvantaged castes? (2)",
  ["(i) In promoting the dignity and freedom of the individual.", "(ii) Because some feel that they are not treated with due respect.",
   "(iii) Respect and equal treatment of women became accepted principles, making it easier for women to struggle against injustice; democracy strengthened the claims of disadvantaged castes for equal status and opportunity, and caste atrocities lack moral and legal foundations."])
# ---------------- Assertion-reason ----------------
C.arq("ar1", GOV, "Democratic decisions may be slower than those of a dictatorship.", "Democracy is based on the idea of deliberation and negotiation.", 0,
      "R explains A.", "deliberation takes time.", "this is the basis of democracy.")
C.arq("ar2", GOV, "A democratic government is a legitimate government.", "It is people's own government, chosen by them.", 0,
      "R explains A.", "legitimacy is its surest strength.", "this is why it is legitimate.")
C.arq("ar3", ECO, "Democracy guarantees economic development.", "Economic development depends on several factors such as population size and the global situation.", 3,
      "A is false: democracy does not guarantee development. R is true.", "dictatorships grew slightly faster.", "growth depends on many factors.")
C.arq("ar4", ECO, "Economic inequality has been growing in many democracies.", "Democracies are based on political equality.", 1,
      "Both are true, but political equality does not explain growing economic inequality.", "the ultra-rich have an increasing share.", "every vote has equal weight.")
C.arq("ar5", SOC, "Democracy stops being accommodative for a group barred from being in the majority by birth.", "Democracy remains democracy only as long as every citizen has a chance of being in the majority at some time.", 0,
      "R explains A.", "permanent exclusion is undemocratic.", "this is the condition for accommodation.")
C.arq("ar6", DIG, "Complaints about democracy show that democracy has failed.", "Democracy transforms people from subjects into citizens who look critically at power holders.", 3,
      "A is false: complaints are a testimony to democracy's success. R is true.", "complaints show success.", "people have become aware citizens.")

chapter = header(SUBJ, N, "Outcomes of Democracy", ["accountable_government", "economic_outcomes", "social_diversity", "dignity_and_freedom"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: this chapter is fully in the board examination (Political Science: 20 marks). There is no map item from this chapter. NCERT exercise 4 (identifying challenges in short case descriptions) is left out as it is not a board-style item.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
