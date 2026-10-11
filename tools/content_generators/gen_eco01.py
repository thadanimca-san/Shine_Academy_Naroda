"""CBSE Class 10 Economics Ch 1: Development (fully in the 2025-26 board syllabus)."""
import sys
from ss_common import make, header, path, SQP, SHINE, CB

ROOT = sys.argv[1]
SUBJ, N = "economics", 1
PATH = path(SUBJ, "ch01_development")
C = make(SUBJ, N, "eco10ch01")
blk, M, W = C.blk, C.m, C.w
GOAL, INC, HUM, SUS = ["development_goals"], ["income_and_comparison"], ["human_development"], ["sustainability"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 1 exercises", "question": n}

GOALS = ("| Category of person | Developmental goals / aspirations |\n|---|---|\n| Landless rural labourers | more days of work and better wages; local school for children; no social discrimination |\n"
         "| Prosperous farmers from Punjab | higher family income through higher support prices and hardworking, cheap labourers; settling children abroad |\n"
         "| Farmers who depend only on rain | assured irrigation, so that crops do not fail |\n| A rural woman from a land-owning family | freedom, security, respect and equal treatment |\n"
         "| Urban unemployed youth | a job with good pay |\n| A boy from a rich urban family | good education and a chance to study abroad |\n"
         "| A girl from a rich urban family | as much freedom as her brother to decide what she wants to do |\n| An adivasi from the Narmada valley | no displacement by a big dam; protection of land, forests and livelihood |")
STATES = ("| State | Per capita income 2018–19 (Rs) | Infant mortality rate per 1000 live births (2018) | Literacy rate % (2017–18) | Net attendance ratio, age 14–15 (2017–18) |\n|---|---|---|---|---|\n"
          "| Haryana | 2,36,147 | 30 | 82 | 61 |\n| Kerala | 2,04,105 | 7 | 94 | 83 |\n| Bihar | 40,982 | 32 | 62 | 43 |")

sections = [
 {"id": "s1", "title": "What does development mean?", "blocks": [
  blk("s1.hook", "hook", title="One dam, two stories",
    body="A big dam brings electricity and irrigation to towns and farms far away. For an industrialist it is development. But for an adivasi family whose village and forest will be drowned by the dam, it means losing home and livelihood.\n\n"
         "So what is development, and for whom? This chapter asks how different people see development, how we compare countries and states, why income alone is not enough, and why development must be sustainable."),
  blk("s1.inspiration", "inspiration", title="Development as freedom", person="Amartya Sen", years="born 1933",
    body="Indian economist **Amartya Sen** won the **Nobel Prize in Economics in 1998**. He argued that development is not only about rising income, but about expanding the real **freedoms and capabilities** of people: to be healthy, educated, free and able to take part in society.\n\n"
         "His ideas helped shape the **Human Development Index** used by the United Nations Development Programme, which compares countries on health, education and income, not income alone.",
    future="This chapter leads to careers in economics, development studies, public policy, statistics and environmental management."),
  C.socratic("s1.socratic", "Why can the same project be development for one person and harmful for another?",
    ["Because people have different goals, and what helps one group can hurt another", "Because development is always harmful", "Because only the government decides what development means"], 0,
    "Different people can have different as well as conflicting notions of development."),
 ]},
 {"id": "s2", "title": "Different goals, income and other goals", "blocks": [
  blk("s2.thm", "theory", title="What development promises to different people", revision=True,
    body="**Different people, different goals:** people seek things that are most important for them, that can fulfil their aspirations or desires. Different persons can have **different developmental goals**, and these goals can even be **conflicting**: what may be development for one may not be development for another, and may even be destructive for the other.\n"
         "- For example, an industrialist may want more dams to get more electricity, but this may submerge the land and disrupt the lives of people who are displaced, such as **tribals**.\n\n"
         "**Income and other goals:** what people desire are **regular work, better wages and a decent price** for their crops or products. In other words, they want **more income**. But besides seeking more income, people also seek things like **equal treatment, freedom, security and respect** of others. They resent discrimination.\n"
         "- In some cases, non-material things may be more important than more income or more consumption, because material goods are not all that you need to live. For example, if women are engaged in paid work, their dignity in the household and society increases; but there must also be **respect** for women and a **safe and secure environment** for them to take up jobs or run a business.\n"
         "- Money, or material things that one can buy with it, is one factor on which our life depends. But the quality of our life also depends on **non-material things**, which are often not easy to measure but mean a lot to our lives. So, for development, people look at a **mix of goals**.\n\n"
         "**National development:** if individuals seek different goals, their notion of national development is also likely to be different. Even the idea of what constitutes national development may differ. We need to think about whether there may be a **better way of doing things**, and whether a particular way of development is **fair and just** for most people."),
  blk("s2.table", "markdown_table", title="Developmental goals of different categories of persons (NCERT)", revision=True, body=GOALS),
  C.kc("s2.check", "Which is a non-material goal of development?",
    [("respect and equal treatment", ""), ("a higher wage", "This is a material (income) goal."), ("a better price for crops", "This is a material goal."), ("a bigger house", "This is a material goal.")],
    "Non-material goals are hard to measure but very important."),
  C.kc("s2.check2", "Why might a big dam not be development for everyone?",
    [("It may displace people such as tribals from their land and livelihood", ""), ("It never produces electricity", "Dams do produce electricity."),
     ("Everyone has the same goals", "People have different goals."), ("It always increases forest cover", "It often submerges forests.")],
    "Development for one may be destructive for another."),
 ]},
 {"id": "s3", "title": "Comparing countries and states", "blocks": [
  blk("s3.thm", "theory", title="Average income and its limits", revision=True,
    body="**How to compare countries:** for comparing countries, their **income** is considered one of the most important attributes. Countries with higher income are more developed than others with less income. But the total income of a country does not tell us what an average person is likely to earn, as populations differ. So we compare the **average income**:\n"
         "- **Average income = total income of the country ÷ total population.** It is also called **per capita income**.\n"
         "- The **World Bank**, in its **World Development Report**, uses per capita income as the criterion for classifying countries. In the **World Development Report 2019** (as given in NCERT), countries with a per capita income of **USD 12,056 per annum and above in 2017** are called **rich countries**, and those with **USD 955 or less** are called **low-income countries**. **India** comes in the category of **low middle income countries** because its per capita income in 2017 was just **USD 1,820** per annum. The rich countries, excluding countries of the Middle East and certain other small countries, are generally called **developed countries**.\n\n"
         "**Limitation of averages:** while averages are useful for comparison, they **hide disparities**. Imagine two countries, each with an average income of Rs 10,000. In country A, all five citizens earn close to Rs 10,000; in country B, one citizen earns Rs 48,000 and four earn Rs 500 each. Both have the same average, but country A is more equitable: people are neither very rich nor extremely poor. In country B, most people are poor.\n\n"
         "**Income and other criteria:** is income enough? Compare three states (NCERT table below). **Haryana** has the highest per capita income and **Bihar** the lowest. But **Kerala**, with a lower per capita income than Haryana, has a much **lower infant mortality rate** and higher literacy and attendance.\n"
         "- **Infant mortality rate (IMR):** the number of children that die **before the age of one year** as a proportion of **1000 live children** born in that particular year.\n"
         "- **Literacy rate:** the proportion of literate population in the **7 years and above** age group.\n"
         "- **Net attendance ratio:** the total number of children of age group **14 and 15 years** attending school as a percentage of the total number of children in the same age group.\n\n"
         "**Public facilities:** money in your pocket cannot buy all the goods and services you need to live well. Income by itself is not an adequate indicator of the material goods and services that citizens are able to use. Money cannot buy a **pollution-free environment** or ensure that you get **unadulterated medicines**, unless you can afford to shift to a community that already has all these. Money may also not be able to protect you from **infectious diseases**, unless the whole community takes preventive steps.\n"
         "- Many important things are best provided **collectively**: it is cheaper to have collective security for the whole locality than for each house to pay for its own; schools, health centres and other facilities work only when the government and community provide them.\n"
         "- **Kerala** has a low infant mortality rate because it has adequate provision of **basic health and educational facilities**. In some states, the **Public Distribution System (PDS)** functions well, so the health and nutritional status of people there is likely to be better."),
  blk("s3.table", "markdown_table", title="Some comparative data on Haryana, Kerala and Bihar (NCERT)", revision=True, body=STATES),
  C.kc("s3.check", "Per capita income is calculated as:",
    [("total income of the country divided by its total population", ""), ("total income multiplied by population", "It is a division."), ("income of the richest person", "That is not an average."), ("total population divided by total income", "It is income divided by population.")],
    "It is also called average income."),
  C.kc("s3.check2", "Why does Kerala have a lower infant mortality rate than Haryana despite a lower per capita income?",
    [("Because it has adequate basic health and educational facilities", ""), ("Because it has the highest per capita income", "Haryana has a higher per capita income."),
     ("Because it has more factories", "That is not the reason given."), ("Because it has fewer schools", "It has better educational facilities.")],
    "Public facilities matter as much as income."),
 ]},
 {"id": "s4", "title": "Human development and sustainability", "blocks": [
  blk("s4.thm", "theory", title="The Human Development Report and sustainable development", revision=True,
    body="**Human Development Report:** once we realise that even though income is important, it is not an adequate criterion, we look for other criteria. The **Human Development Report** published by the **UNDP (United Nations Development Programme)** compares countries based on the **educational levels** of the people, their **health status** and **per capita income**.\n"
         "- **Life expectancy at birth** denotes, as the name suggests, the average expected length of life of a person at the time of birth.\n"
         "- **Gross enrolment ratio** for three levels means the enrolment ratio for primary school, secondary school and higher education beyond secondary school.\n"
         "- **Per capita income** in the HDR is calculated in **dollars** for all countries so that it can be compared, and in a way that every dollar buys the same amount of goods and services in any country (**purchasing power parity**).\n"
         "- In the Human Development Report 2019 (as in NCERT), **Sri Lanka** (rank **71**) was far ahead of **India** (rank **129**) in human development, even though Sri Lanka is a much smaller country. India's neighbours Bangladesh, Nepal, Myanmar and Pakistan ranked below or near India.\n\n"
         "**Sustainability of development:** development must not come at the cost of future generations. Scientists have been warning that the present type and levels of development are **not sustainable**.\n"
         "- **Groundwater:** recent evidence suggests that the groundwater in the country is under serious threat of **overuse**. Groundwater is an example of a **renewable resource**: it is replenished by nature, as in the case of crops and plants. But even these resources may be overused: in the case of groundwater, if we use more than what is being replenished by rain, we would be overusing it.\n"
         "- **Non-renewable resources** are those which will get exhausted after years of use. We have a fixed stock on earth which cannot be replenished. We do discover new resources, which increases the available stock, but over time even these will be exhausted. **Crude oil** is an example: if the world continues to extract it at the present rate, the reserves will last only for a limited number of years. India has to import much of its oil, which makes it vulnerable.\n"
         "- **Environmental degradation** is not confined to a nation or state. Issues like this are **no longer regional or national**; our future is linked together. **Sustainability of development** is a comparatively new area of knowledge in which scientists, economists, philosophers and other social scientists are working together.\n"
         "- In general, the question of development or progress is perennial. At all times, as members of society and as individuals, we need to ask **where we want to go, what we wish to become and what our goals are**."),
  C.kc("s4.check", "The Human Development Report compares countries on:",
    [("educational levels, health status and per capita income", ""), ("per capita income only", "That is the World Bank's main criterion."), ("military strength", "This is not used."), ("population size only", "This is not used.")],
    "It is published by the UNDP."),
  C.kc("s4.check2", "Which is a renewable resource that can still be overused?",
    [("groundwater", ""), ("crude oil", "Crude oil is non-renewable."), ("coal", "Coal is non-renewable."), ("natural gas", "Natural gas is non-renewable.")],
    "If we use more groundwater than rain replenishes, we overuse it."),
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Per capita income = Total income ÷ Population.**\n- **World Bank (WDR 2019): Rich ≥ USD 12,056; Low ≤ USD 955; India = USD 1,820 (low middle).**\n"
         "- **UNDP HDI = \"HEI\"**: Health (life expectancy), Education (literacy, enrolment), Income (per capita, in PPP dollars).\n"
         "- **IMR = deaths before age 1 per 1000 live births; Literacy = age 7+; Attendance = age 14–15.**\n"
         "- **Kerala vs Haryana: \"Kerala Keeps Kids alive\"**: lower income, but IMR 7 against 30.\n- **Renewable = Replenished (groundwater); Non-renewable = Not replenished (crude oil).**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying everyone has the same development goals: goals are **different and can conflict**.\n2. Thinking total income is the best comparison: we use **average (per capita) income** because populations differ.\n"
         "3. Forgetting that averages **hide disparities**.\n4. Saying Kerala has the highest per capita income: **Haryana** has the highest of the three; Kerala does best on health and education.\n"
         "5. Mixing up the World Bank and UNDP: the World Bank uses **per capita income**; the UNDP uses **health, education and income**.\n6. Calling groundwater non-renewable: it is **renewable**, but can be overused."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Give five students imaginary incomes (for example Rs 500, 500, 500, 500 and 48,000). Ask the class to find the average and then ask: does the average describe these five people well? Repeat with five nearly equal incomes with the same average."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Write down three development goals for yourself and three for your locality. Which of them are about income, and which are about non-material things like safety, respect or clean air?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Chapter 2 (Sectors of the Indian Economy):** jobs, income and employment.\n- **Geography Chapter 1 (Resources and Development):** sustainable use of resources.\n"
         "- **Political Science Chapter 5 (Outcomes of Democracy):** economic growth and inequality."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="'Per capita income is not a useful criterion at all.' Do you agree? Answer in about 120 words.\n\n"
         "**Model answer:** I do not fully agree. Per capita income is useful: dividing total income by population lets us compare countries of different sizes, and the World Bank uses it to classify countries as rich, middle-income or low-income. "
         "But it has limitations. Being an average, it hides disparities: two countries with the same average may have very different distributions of income. It also ignores non-material goals and public facilities. "
         "Kerala has a lower per capita income than Haryana, yet its infant mortality rate is much lower and its literacy and school attendance are higher, because of good health and educational facilities. "
         "So per capita income should be used along with other indicators, such as those in the UNDP's Human Development Index."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Different people have different, and sometimes conflicting, development goals; people want income and also equality, freedom, security and respect.\n"
         "- Countries are compared by per capita (average) income; the World Bank classifies countries this way, with India in the low middle income group.\n"
         "- Averages hide disparities, and income does not show access to public facilities.\n"
         "- Kerala, with a lower per capita income than Haryana, does far better on infant mortality, literacy and attendance.\n"
         "- The UNDP's Human Development Report compares countries on education, health and income; Sri Lanka ranks well above India.\n"
         "- Development must be sustainable: groundwater is overused and crude oil is running out."),
  blk("s5.examtips", "exam_tips", title="Board exam tips",
    body="- The 2025-26 sample paper asked about the limitation of per capita income (it gives a basic idea of well-being but hides income inequality; answer C) and the utility of public services (health, education, sanitation and clean water, infrastructure) for well-being (3 marks).\n"
         "- 3/5-mark favourites: different goals, limitations of per capita income, Kerala and Haryana comparison, World Bank vs UNDP criteria, sustainability.\n"
         "- Learn the definitions of IMR, literacy rate and net attendance ratio exactly."),
  blk("s5.flash1", "flashcard", front="What is per capita income?", back="The total income of a country divided by its total population; also called average income."),
  blk("s5.flash2", "flashcard", front="What is the infant mortality rate?", back="The number of children that die before the age of one year as a proportion of 1000 live children born in that year."),
  blk("s5.flash3", "flashcard", front="On what does the UNDP's Human Development Report compare countries?", back="Educational levels, health status and per capita income."),
  blk("s5.flash4", "flashcard", front="What is sustainable development?", back="Development that meets present needs without using up resources or damaging the environment for future generations."),
 ]},
]

# ---------------- Sample paper ----------------
M("sqp30", INC, "What can be inferred about the limitations of using per capita income (average income) to compare well-being across countries? Choose the correct option.",
  [("It shows how equally or unequally income is distributed among the people in a country.", "Averages hide how income is distributed."),
   ("The only measure needed to understand a country's development is Per capita income.", "Many other measures, like health and education, are needed."),
   ("It gives a basic idea of economic well-being but hides the income inequality.", ""),
   ("It only reflects the industrial growth of a country and does not consider other important factors.", "It reflects total income, not only industry.")],
  "Per capita income gives a basic idea of well-being but hides inequality, cost of living and access to services (CBSE marking scheme: C).", "medium", SQP(30), correct=2)
W("sqp35", "short_answer", HUM, "Evaluate the utility of public services in contributing to the overall well-being of individuals and society.",
  ["Healthcare: accessible and quality public healthcare keeps the population healthy and productive, reduces mortality and lets people contribute to the economy; poor healthcare leads to disease and lower life expectancy.",
   "Education and skill development: public education gives equal learning opportunities to all, raising literacy, skills and innovation, which reduce inequality and support growth.",
   "Sanitation, clean water and infrastructure: these prevent diseases like cholera and dysentery, raise life expectancy and productivity, and roads, transport and energy give easy access to goods and services."], source=SQP(35))

# ---------------- NCERT exercises ----------------
M("ex1", INC, "Development of a country can generally be determined by:",
  [("its per capita income", ""), ("its average literacy level", "This is one indicator, but per capita income is the general criterion."), ("health status of its people", "This is one indicator, but per capita income is the general criterion."), ("none of these", "Per capita income is the general criterion.")],
  "Per capita income is the most common criterion, though not adequate on its own.", "easy", ex("1"), correct=0)
M("ex2", HUM, "Which neighbouring country has better performance in terms of human development than India?",
  [("Sri Lanka", ""), ("Bangladesh", "Bangladesh ranks below India."), ("Nepal", "Nepal ranks below India."), ("Pakistan", "Pakistan ranks below India.")],
  "Sri Lanka ranked 71 against India's 129 (HDR 2019).", "easy", ex("2"), correct=0)
M("ex3", INC, "Assume there are four families in a country. The average per capita income of these families is Rs 15,000. If the income of three families is Rs 10,000, Rs 20,000 and Rs 12,000, what is the income of the fourth family?",
  [("Rs 18,000", ""), ("Rs 7,500", "Total must be 4 × 15,000 = 60,000; 60,000 − 42,000 = 18,000."), ("Rs 12,000", "Check: 60,000 − 42,000 = 18,000."), ("Rs 15,000", "That is the average, not the fourth income.")],
  "Total = 4 × 15,000 = 60,000; the three families earn 42,000; the fourth earns 18,000 (the options printed in some NCERT editions do not include this answer).", "medium", ex("3"), correct=0)
W("ex4", "short_answer", INC, "What is the main criterion used by the World Bank in classifying different countries? What are the limitations of this criterion, if any?",
  ["The World Bank uses per capita (average) income to classify countries as rich, middle-income or low-income.",
   "Limitation: as an average, it hides disparities in how income is distributed among people.",
   "It also ignores non-material goals and public facilities such as health and education; Kerala, with lower income than Haryana, has much better health indicators."], source=ex("4"))
W("ex5", "short_answer", HUM, "In what respects is the criterion used by the UNDP for measuring development different from the one used by the World Bank?",
  ["The World Bank uses only per capita income to compare countries.",
   "The UNDP's Human Development Report compares countries on educational levels, health status and per capita income together.",
   "So the UNDP gives a broader picture: a country like Sri Lanka ranks above India in human development though both are developing countries."], source=ex("5"))
W("ex6", "short_answer", INC, "Why do we use averages? Are there any limitations to their use? Illustrate with your own examples related to development.",
  ["We use averages because countries have different populations, so total income cannot be compared directly.",
   "Limitation: averages hide disparities in distribution.",
   "Example: two villages each have an average monthly income of Rs 10,000; in one everyone earns about Rs 10,000, in the other one person earns Rs 48,000 and the rest Rs 500, so most people are poor."], source=ex("6"))
W("ex7", "long_answer", HUM, "Kerala, with lower per capita income, has a better human development ranking than Haryana. Hence, per capita income is not a useful criterion at all and should not be used to compare states. Do you agree? Discuss.",
  ["I do not fully agree: per capita income is a useful starting point for comparing the economic condition of states of different sizes.",
   "But it is not enough on its own: Kerala's per capita income is lower than Haryana's, yet its infant mortality rate is 7 against 30.",
   "Kerala also has higher literacy (94% against 82%) and net attendance ratio (83 against 61), because of good basic health and educational facilities.",
   "Per capita income is an average, so it hides disparities and does not show access to public facilities like the PDS, health and schools.",
   "So per capita income should be used along with other indicators such as health and education, as in the Human Development Index."], source=ex("7"))
W("ex9", "short_answer", SUS, "Why is the issue of sustainability important for development?",
  ["Present levels of development use resources faster than they can be replenished; groundwater is being overused.",
   "Non-renewable resources like crude oil have a fixed stock and will be exhausted, harming future generations.",
   "Environmental degradation crosses national boundaries, so development must meet present needs without damaging the future."], source=ex("9"))
W("ex10", "short_answer", SUS, "'The Earth has enough resources to meet the needs of all but not enough to satisfy the greed of even one person.' How is this statement relevant to the discussion of development? Discuss.",
  ["The statement (by Gandhiji) means that resources are enough for everyone's needs if used wisely.",
   "Greed leads to overuse of resources like groundwater and crude oil and to environmental degradation.",
   "Development must therefore be sustainable and fair, sharing resources so that present and future generations can meet their needs."], source=ex("10"))
W("ex11", "very_short_answer", SUS, "List a few examples of environmental degradation that you may have observed around you.",
  ["Any two: falling groundwater levels; air pollution from vehicles and factories; dumping of waste and plastic; polluted rivers and lakes.",
   "Any other: cutting of trees and loss of green cover; soil erosion; noise pollution in cities."], source=ex("11"))

# ---------------- MCQs ----------------
M("mcq01", GOAL, "Which statement about development goals is correct?",
  [("Different people can have different and even conflicting development goals", ""), ("All people have the same development goals", "Goals differ."), ("Development goals are only about income", "Non-material goals matter too."), ("Development is the same for every country", "Notions differ.")], "What is development for one may be destructive for another.")
M("mcq02", GOAL, "What would most likely be a development goal of landless rural labourers?",
  [("more days of work and better wages", ""), ("settling children abroad", "That is a goal of prosperous farmers."), ("more electricity for industry", "That is an industrialist's goal."), ("higher support prices for crops", "That is a goal of farmers who own land.")], "They also want local schools and no discrimination.")
M("mcq03", GOAL, "An adivasi from the Narmada valley would most likely want:",
  [("no displacement and protection of land, forests and livelihood", ""), ("more big dams", "Big dams can displace adivasis."), ("a job abroad", "That is not the typical goal."), ("higher factory output", "That is not their main goal.")], "Development for some can be destructive for others.")
M("mcq04", GOAL, "Besides more income, people also seek:",
  [("equal treatment, freedom, security and respect", ""), ("only more consumption", "They seek non-material goals too."), ("only bigger houses", "They seek non-material goals too."), ("only more cars", "They seek non-material goals too.")], "People resent discrimination.")
M("mcq05", GOAL, "Why does the dignity of women increase when they do paid work?",
  [("Because their contribution is recognised in the household and society", ""), ("Because they stop doing housework", "Not necessarily."), ("Because they earn more than men", "Not necessarily."), ("Because they need no safety", "A safe environment is still needed.")], "Respect and safety are also needed.")
M("mcq06", INC, "For comparing countries, which is considered one of the most important attributes?",
  [("income", ""), ("area", "Area is not used for development."), ("number of rivers", "Not used."), ("number of cities", "Not used.")], "Countries with higher income are seen as more developed.")
M("mcq07", INC, "Why do we use average income instead of total income to compare countries?",
  [("Because populations of countries differ", ""), ("Because total income is secret", "It is not secret."), ("Because averages show inequality", "Averages hide inequality."), ("Because the World Bank does not know total income", "That is not the reason.")], "Average income = total income ÷ population.")
M("mcq08", INC, "Which organisation classifies countries mainly on the basis of per capita income?",
  [("the World Bank", ""), ("the UNDP", "The UNDP uses health, education and income."), ("the WTO", "The WTO deals with trade."), ("the RBI", "The RBI is India's central bank.")], "It publishes the World Development Report.")
M("mcq09", INC, "In the World Development Report 2019 (as given in NCERT), India was classified as a:",
  [("low middle income country", ""), ("rich country", "Rich countries had USD 12,056 or more."), ("low-income country", "Low-income was USD 955 or less."), ("developed country", "India is a developing country.")], "India's per capita income in 2017 was USD 1,820.")
M("mcq10", INC, "The main limitation of an average is that it:",
  [("hides disparities", ""), ("is hard to calculate", "It is easy to calculate."), ("always overstates income", "Not always."), ("cannot be used for comparison", "It is useful for comparison.")], "Two countries with the same average can have very different distributions.")
M("mcq11", INC, "Among Haryana, Kerala and Bihar (NCERT table), which state has the highest per capita income?",
  [("Haryana", ""), ("Kerala", "Kerala is second."), ("Bihar", "Bihar has the lowest."), ("All are equal", "They differ greatly.")], "But Kerala does best on health and education.")
M("mcq12", INC, "Among Haryana, Kerala and Bihar, which state has the lowest infant mortality rate?",
  [("Kerala", ""), ("Haryana", "Haryana's IMR is 30."), ("Bihar", "Bihar's IMR is 32."), ("All are equal", "They differ.")], "Kerala's IMR is 7 per 1000 live births.")
M("mcq13", INC, "Infant mortality rate indicates the number of children that die:",
  [("before the age of one year, per 1000 live births", ""), ("before the age of five years, per 100 births", "It is before one year, per 1000."), ("in hospitals only", "It covers all live births."), ("before the age of ten", "It is before one year.")], "It is a key health indicator.")
M("mcq14", INC, "Literacy rate measures the proportion of literate population in the age group of:",
  [("7 years and above", ""), ("14 and 15 years", "That is the net attendance ratio."), ("18 years and above", "It is 7 years and above."), ("5 to 10 years", "It is 7 years and above.")], "This is the NCERT definition.")
M("mcq15", INC, "Net attendance ratio refers to children of which age group attending school?",
  [("14 and 15 years", ""), ("7 years and above", "That is literacy rate."), ("below 1 year", "That relates to IMR."), ("18 to 25 years", "That is higher education.")], "It is a percentage of all children in that age group.")
M("mcq16", INC, "Which of these can money NOT easily buy for an individual?",
  [("a pollution-free environment", ""), ("a bicycle", "This can be bought."), ("a mobile phone", "This can be bought."), ("clothes", "These can be bought.")], "Some things are best provided collectively.")
M("mcq17", INC, "Why is it better to provide some facilities collectively?",
  [("Because it is cheaper and more effective for the whole community", ""), ("Because individuals cannot pay anything", "Not the reason."), ("Because the government owns all money", "Not the reason."), ("Because private goods are illegal", "They are not.")], "Collective security for a locality is cheaper than each house paying.")
M("mcq18", INC, "Kerala has a low infant mortality rate mainly because of:",
  [("adequate provision of basic health and educational facilities", ""), ("very high per capita income", "Its income is lower than Haryana's."), ("large industries", "That is not the reason."), ("cold climate", "That is not the reason.")], "Public facilities matter.")
M("mcq19", INC, "The PDS functions well in some states. PDS stands for:",
  [("Public Distribution System", ""), ("Private Development Scheme", "It is the Public Distribution System."), ("Per capita Data Survey", "It is the Public Distribution System."), ("Public Development Service", "It is the Public Distribution System.")], "It provides food grains at fair prices.")
M("mcq20", HUM, "The Human Development Report is published by:",
  [("the UNDP", ""), ("the World Bank", "The World Bank publishes the World Development Report."), ("the IMF", "The IMF does not publish it."), ("NITI Aayog", "It is an international report.")], "UNDP = United Nations Development Programme.")
M("mcq21", HUM, "Life expectancy at birth denotes:",
  [("the average expected length of life of a person at the time of birth", ""), ("the age at which people retire", "That is not life expectancy."), ("the number of births per year", "That is the birth rate."), ("the deaths of infants", "That is IMR.")], "It is an indicator of health.")
M("mcq22", HUM, "In the HDR, per capita income is calculated in:",
  [("dollars, using purchasing power parity", ""), ("rupees only", "It uses dollars for comparison."), ("gold", "It uses dollars."), ("euros only", "It uses dollars.")], "Every dollar buys the same amount of goods in any country.")
M("mcq23", HUM, "In the Human Development Report 2019 (as in NCERT), India's rank was:",
  [("129", ""), ("71", "That was Sri Lanka."), ("1", "India was not first."), ("189", "India was far above that.")], "Sri Lanka ranked far above India.")
M("mcq24", HUM, "Gross enrolment ratio for three levels refers to enrolment in:",
  [("primary, secondary and higher education", ""), ("nursery, primary and middle", "It is primary, secondary and higher."), ("only colleges", "It covers three levels."), ("only primary", "It covers three levels.")], "It is used in the HDI.")
M("mcq25", SUS, "Groundwater is an example of a:",
  [("renewable resource that can be overused", ""), ("non-renewable resource", "It is renewable."), ("resource that can never run short", "It can be overused."), ("man-made resource", "It is natural.")], "Using more than rain replenishes is overuse.")
M("mcq26", SUS, "Crude oil is an example of a:",
  [("non-renewable resource", ""), ("renewable resource", "It is non-renewable."), ("resource replenished by rain", "That is groundwater."), ("human resource", "It is a natural resource.")], "Its stock is fixed and will be exhausted.")
M("mcq27", SUS, "Environmental degradation is:",
  [("not confined to a nation or state", ""), ("only a local problem", "It crosses borders."), ("only a problem of rich countries", "It affects all."), ("not related to development", "It is closely related.")], "Our future is linked together.")
M("mcq28", SUS, "Sustainable development means development that:",
  [("meets present needs without harming future generations", ""), ("uses all resources quickly", "That is unsustainable."), ("ignores the environment", "That is unsustainable."), ("stops all growth", "It does not stop growth.")], "Scientists warn present levels are not sustainable.")
M("mcq29", GOAL, "'A girl from a rich urban family' would most likely aspire to:",
  [("as much freedom as her brother to decide what she wants to do", ""), ("more days of work as a labourer", "That is a landless labourer's goal."), ("assured irrigation", "That is a rain-fed farmer's goal."), ("no displacement by a dam", "That is an adivasi's goal.")], "Freedom and equality are non-material goals.")
M("mcq30", INC, "Country A: five citizens each earn about Rs 10,000. Country B: one earns Rs 48,000 and four earn Rs 500 each. Which is true?",
  [("Both have the same average, but A is more equitable", ""), ("B is more equitable", "Most people in B are very poor."), ("A has a higher average", "Both averages are Rs 10,000."), ("Averages show B is fairer", "Averages hide the disparity.")], "This shows the limitation of averages.")
# ---------------- True / false ----------------
C.tf("tf1", GOAL, "Development for one person may be destructive for another.", True, "For example, a dam may displace tribals while giving electricity to others.")
C.tf("tf2", INC, "Averages show how equally income is distributed among people.", False, "Averages hide disparities in distribution.")
C.tf("tf3", INC, "Kerala has a higher per capita income than Haryana.", False, "Haryana's per capita income is higher, but Kerala does better on health and education.")
C.tf("tf4", SUS, "Crude oil is a renewable resource.", False, "Crude oil is non-renewable; groundwater is renewable.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", GOAL, "Why are development goals of different people different, and sometimes conflicting?",
  ["People seek what is most important for them, depending on their life situations, so goals differ.", "What is development for one may be destructive for another, such as a dam that gives electricity but displaces adivasis."])
W("vsa2", "very_short_answer", INC, "Define per capita income and state one limitation.",
  ["Per capita income is the total income of a country divided by its total population.", "Limitation: it is an average, so it hides disparities in income distribution."])
W("vsa3", "very_short_answer", HUM, "Name the three indicators used in the Human Development Index.",
  ["Health status (life expectancy at birth) and educational levels (literacy, gross enrolment ratio).", "Per capita income, calculated in dollars using purchasing power parity."])
W("sa1", "short_answer", GOAL, "'Besides income, people also seek other goals.' Explain with examples.",
  ["People want regular work, better wages and fair prices, that is, more income.",
   "They also seek non-material goals such as equal treatment, freedom, security and respect, and they resent discrimination.",
   "For example, women's dignity rises when they do paid work, but they also need respect and a safe environment to work."])
W("sa2", "short_answer", INC, "Why is income alone not an adequate indicator of development?",
  ["Income is an average and hides disparities in distribution.",
   "Money cannot buy many things like a pollution-free environment, unadulterated medicines or protection from infectious diseases, which need collective provision.",
   "Kerala, with lower income than Haryana, has a much lower infant mortality rate and higher literacy because of good public health and education facilities."])
W("sa3", "short_answer", SUS, "Distinguish between renewable and non-renewable resources with examples, and explain why sustainability matters.",
  ["Renewable resources are replenished by nature, like groundwater, but can still be overused if we use more than rain replenishes.",
   "Non-renewable resources have a fixed stock and get exhausted, like crude oil.",
   "Sustainability matters because overuse harms future generations and environmental damage crosses national boundaries."])
W("la1", "long_answer", INC, "Compare Haryana, Kerala and Bihar using the NCERT data. What does the comparison show?",
  ["Per capita income: Haryana is highest (Rs 2,36,147), Kerala next (Rs 2,04,105) and Bihar lowest (Rs 40,982).",
   "Infant mortality rate: Kerala is lowest (7), much better than Haryana (30) and Bihar (32).",
   "Literacy rate: Kerala 94%, Haryana 82%, Bihar 62%; net attendance ratio (14–15 years): Kerala 83, Haryana 61, Bihar 43.",
   "So Kerala, though it has lower income than Haryana, does far better on health and education, because of adequate public health and educational facilities.",
   "The comparison shows that per capita income alone is not an adequate indicator of development; health, education and public facilities must also be considered."])
W("la2", "long_answer", HUM, "How is the UNDP's method of measuring development better than the World Bank's?",
  ["The World Bank classifies countries using only per capita income: in WDR 2019, rich countries had USD 12,056 or more and low-income countries USD 955 or less; India was low middle income at USD 1,820.",
   "Per capita income hides disparities and ignores health, education and public facilities.",
   "The UNDP's Human Development Report compares countries on educational levels, health status and per capita income together.",
   "It uses indicators like life expectancy at birth, gross enrolment ratio, and per capita income in PPP dollars, giving a fuller picture of people's lives.",
   "For example, Sri Lanka (rank 71) is far ahead of India (rank 129) in human development, showing that income alone does not show well-being."])
W("cb1", "case_based", INC, "Read the source and answer the questions.\n\n*\"For comparing countries, their income is considered to be one of the most important attributes. Countries with higher income are more developed than others with less income... Since countries have different populations, comparing total income will not tell us what an average person is likely to earn. Hence, we compare the average income which is the total income of the country divided by its total population.\"* (NCERT)\n\n"
  "(i) What is average income also called? (1)\n\n(ii) Which organisation uses this criterion to classify countries? (1)\n\n(iii) Give two limitations of this criterion. (2)",
  ["(i) Per capita income.", "(ii) The World Bank (in its World Development Report).",
   "(iii) Any two: it hides disparities in income distribution; it ignores non-material goals; it does not show access to public facilities such as health and education."])
W("cb2", "case_based", SUS, "Read the source and answer the questions.\n\n*\"Recent evidence suggests that the groundwater in the country is under serious threat of overuse... Groundwater is an example of renewable resources. These resources are replenished by nature as in the case of crops and plants. However, even these resources may be overused.\"* (NCERT)\n\n"
  "(i) Why is groundwater called a renewable resource? (1)\n\n(ii) When is groundwater said to be overused? (1)\n\n(iii) Why is sustainability important for development? (2)",
  ["(i) Because it is replenished by nature, through rain.", "(ii) When we use more than what is being replenished by rain.",
   "(iii) Because present levels of resource use harm future generations, non-renewable resources will be exhausted, and environmental damage crosses national boundaries."])
# ---------------- Assertion-reason ----------------
C.arq("ar1", GOAL, "Different people can have conflicting development goals.", "What is development for one may be destructive for another.", 0,
      "R explains A.", "goals differ and can conflict.", "for example, a dam displacing tribals.")
C.arq("ar2", INC, "Average income is used to compare countries.", "Countries have different populations, so total income cannot be compared directly.", 0,
      "R explains A.", "average = total income ÷ population.", "this is why averages are used.")
C.arq("ar3", INC, "Averages show how income is distributed among people.", "Two countries with the same average may have very different distributions.", 3,
      "A is false: averages hide disparities. R is true.", "averages hide distribution.", "this shows the limitation.")
C.arq("ar4", INC, "Kerala has a lower infant mortality rate than Haryana.", "Kerala has adequate provision of basic health and educational facilities.", 0,
      "R explains A.", "Kerala's IMR is 7 against 30.", "this is the reason given in NCERT.")
C.arq("ar5", HUM, "Sri Lanka ranks above India in human development.", "The Human Development Report compares countries on education, health and income.", 1,
      "Both are true, but R describes the method; it does not explain why Sri Lanka ranks higher.", "Sri Lanka ranked 71, India 129.", "this is the UNDP method.")
C.arq("ar6", SUS, "Groundwater can be overused.", "Groundwater is a non-renewable resource.", 2,
      "A is true but R is false: groundwater is renewable, but it can be overused when use exceeds replenishment.", "use can exceed replenishment.", "it is renewable, not non-renewable.")

chapter = header(SUBJ, N, "Development", ["development_goals", "income_and_comparison", "human_development", "sustainability"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: this chapter is fully in the board examination (Economics: 20 marks). There is no map item from this chapter. Data tables follow the current NCERT book (World Development Report 2019, HDR 2019, state data 2017–19). NCERT exercises that need personal surveys or long data tables are left out.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
