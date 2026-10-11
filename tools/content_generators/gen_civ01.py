"""CBSE Class 10 Political Science Ch 1: Power-sharing (fully in the 2025-26 board syllabus)."""
import sys
from ss_common import make, header, path, SQP, SHINE, CB

ROOT = sys.argv[1]
SUBJ, N = "civics", 1
PATH = path(SUBJ, "ch01_power_sharing")
C = make(SUBJ, N, "civ10ch01")
blk, M, W = C.blk, C.m, C.w
BEL, SL, WHY, FORMS = ["belgium_model"], ["sri_lanka_majoritarianism"], ["why_power_sharing"], ["forms_of_power_sharing"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 1 exercises", "question": n}

COMPARE = ("| | Belgium | Sri Lanka |\n|---|---|---|\n| **Population mix** | 59% Dutch-speaking (Flemish region), 40% French-speaking (Wallonia), 1% German; Brussels 80% French, 20% Dutch | 74% Sinhala-speakers, 18% Tamil-speakers (13% Sri Lankan Tamils, rest Indian Tamils) |\n"
           "| **Approach** | **accommodation**: four constitutional amendments (1970–1993) | **majoritarianism**: 1956 Act made Sinhala the only official language |\n"
           "| **Key measures** | equal Dutch and French ministers; powers to states; equal representation in Brussels; community governments | preferential policies for Sinhala in universities and jobs; the state to protect and foster Buddhism |\n"
           "| **Result** | unity kept; Brussels chosen as the headquarters of the European Union | alienation of Tamils, demand for Tamil Eelam, civil war (ended 2009) |")
FORMSTAB = ("| Form of power sharing | Meaning | Example |\n|---|---|---|\n| **Horizontal**: among organs of government | legislature, executive and judiciary at the same level; checks and balances | judges check laws made by legislatures |\n"
            "| **Vertical**: among governments at different levels | union, state and local governments | federal government; panchayats and municipalities |\n"
            "| **Among social groups** | religious and linguistic groups, weaker sections, women | 'community government' in Belgium; reserved constituencies in India |\n"
            "| **Among parties, pressure groups and movements** | competition and alliances; influence of interest groups | coalition government; traders, farmers and workers' groups |")

sections = [
 {"id": "s1", "title": "Who should hold power?", "blocks": [
  blk("s1.hook", "hook", title="Two countries, two choices",
    body="Belgium and Sri Lanka are both democracies, and both have people who speak different languages. In the 20th century, both faced tension between their communities.\n\n"
         "Belgium chose to **share power** with all its groups and stayed united. Sri Lanka chose to let the **majority rule over** the minority, and slid into a long civil war. This chapter asks why sharing power is wise and right, and what forms it takes in modern democracies."),
  blk("s1.inspiration", "inspiration", title="Power shared, not grabbed", person="Nelson Mandela", years="1918–2013",
    body="After decades of apartheid, Nelson Mandela became South Africa's first democratically elected president in **1994**. Instead of taking revenge on the white minority that had imprisoned him for 27 years, he formed a **Government of National Unity** that included leaders of the former ruling party.\n\n"
         "By sharing power, he helped a deeply divided country move to democracy without a civil war. He showed that sharing power can protect both the minority and the majority.",
    future="This chapter leads to careers in law, public administration, diplomacy, journalism and conflict resolution."),
  C.socratic("s1.socratic", "Why might a majority community be wise to share power with a minority?",
    ["Sharing power reduces conflict and keeps the country stable and united", "Because the majority is always wrong", "Because power sharing means no one rules"], 0,
    "Imposing the majority's will may look attractive in the short run, but it undermines the unity of the nation in the long run."),
 ]},
 {"id": "s2", "title": "Belgium and Sri Lanka", "blocks": [
  blk("s2.thm", "theory", title="Two stories of ethnic diversity", revision=True,
    body="**Belgium:** a small country in Europe, smaller in area than the state of Haryana. It has borders with **France, the Netherlands, Germany and Luxembourg**. It has a population of a little over one crore, about half the population of Haryana.\n"
         "- **Ethnic composition:** of the country's total population, **59 per cent** lives in the **Flemish region** and speaks **Dutch**; another **40 per cent** lives in the **Wallonia region** and speaks **French**; the remaining **one per cent** speaks **German**.\n"
         "- In the capital city **Brussels**, **80 per cent** speak **French**, while **20 per cent** are **Dutch**-speaking.\n"
         "- The minority **French-speaking** community was relatively **rich and powerful**. This was resented by the Dutch-speaking community, who got the benefit of economic development and education much later. This led to **tensions** between the communities during the **1950s and 1960s**.\n"
         "- The tension was more acute in **Brussels**: the Dutch-speaking people were a majority in the country but a **minority in the capital**.\n\n"
         "**Sri Lanka:** an island nation, just a few kilometres off the southern coast of Tamil Nadu, with about **2 crore** people, about the same as Haryana. It has a diverse population:\n"
         "- The major social groups are the **Sinhala-speakers (74 per cent)** and the **Tamil-speakers (18 per cent)**.\n"
         "- Among Tamils there are two sub-groups: Tamil natives of the country, called **'Sri Lankan Tamils' (13 per cent)**; and the rest, whose forefathers came from India as **plantation workers** during the colonial period, called **'Indian Tamils'**. Sri Lankan Tamils are concentrated in the **north and east** of the country.\n"
         "- Most Sinhala-speaking people are **Buddhist**, while most Tamils are **Hindus or Muslims**. There are about **7 per cent Christians**, who are both Tamil and Sinhala.\n\n"
         "**Majoritarianism in Sri Lanka:** Sri Lanka became independent in **1948**. The leaders of the Sinhala community sought to secure dominance over the government by virtue of their majority, and the democratically elected government adopted a series of **majoritarian measures** to establish **Sinhala supremacy**:\n"
         "- In **1956**, an Act was passed to recognise **Sinhala as the only official language**, disregarding Tamil.\n"
         "- Governments followed **preferential policies** that favoured Sinhala applicants for **university positions and government jobs**.\n"
         "- A new constitution stipulated that the state shall **protect and foster Buddhism**.\n\n"
         "All these measures gradually increased the feeling of **alienation** among the Sri Lankan Tamils. They felt that none of the major political parties led by the Buddhist Sinhala leaders was sensitive to their language and culture, and that the constitution and government policies denied them equal political rights and discriminated against them in jobs and other opportunities.\n"
         "- The Sri Lankan Tamils launched parties and struggles demanding **recognition of Tamil as an official language, regional autonomy, and equality of opportunity in securing education and jobs**. But their demand for more autonomy to provinces populated by Tamils was repeatedly denied.\n"
         "- By the **1980s**, several political organisations were formed demanding an **independent Tamil Eelam (state)** in the northern and eastern parts of Sri Lanka.\n"
         "- The distrust between the two communities turned into widespread conflict and soon into a **civil war**. Thousands of people of both communities were killed, many families were forced to leave the country as **refugees**, and many more lost their livelihoods. The civil war ended in **2009**."),
  blk("s2.table", "markdown_table", title="Belgium and Sri Lanka compared", revision=True, body=COMPARE),
  C.kc("s2.check", "In Belgium, which language do 59 per cent of the people speak?",
    [("Dutch", ""), ("French", "40 per cent speak French."), ("German", "One per cent speak German."), ("English", "English is not one of the three groups.")],
    "59 per cent live in the Flemish region and speak Dutch."),
  C.kc("s2.check2", "Which 1956 measure in Sri Lanka alienated the Tamils?",
    [("An Act recognising Sinhala as the only official language", ""), ("An Act making Tamil the only official language", "It was the reverse."),
     ("Creation of community governments", "That was in Belgium."), ("Equal numbers of ministers from both groups", "That was in Belgium.")],
    "It disregarded Tamil and was part of a series of majoritarian measures."),
 ]},
 {"id": "s3", "title": "Accommodation in Belgium and why power sharing is desirable", "blocks": [
  blk("s3.thm", "theory", title="The Belgian model and the case for sharing power", revision=True,
    body="**Accommodation in Belgium:** the Belgian leaders took a different path. They recognised the existence of **regional differences and cultural diversities**. Between **1970 and 1993**, they **amended their constitution four times** to work out an arrangement that would enable everyone to live together within the same country. The Belgian model:\n"
         "1. The constitution prescribes that the number of **Dutch and French-speaking ministers shall be equal** in the central government. Some special laws require the support of a **majority of members from each linguistic group**. Thus, no single community can make decisions unilaterally.\n"
         "2. Many powers of the central government have been given to **state governments** of the two regions. The state governments are **not subordinate** to the central government.\n"
         "3. **Brussels** has a **separate government** in which both communities have **equal representation**. The French-speaking people accepted equal representation in Brussels because the Dutch-speaking community accepted equal representation in the central government.\n"
         "4. Apart from the central and state governments, there is a **third kind of government**, the **'community government'**, elected by people belonging to one language community (Dutch, French or German-speaking), no matter where they live. It has power over **cultural, educational and language-related issues**.\n\n"
         "The Belgian model is complicated, but it has worked well. It helped **avoid civic strife** and a possible **division of the country on linguistic lines**. When many countries of Europe came together to form the **European Union**, **Brussels** was chosen as its **headquarters**.\n\n"
         "**Lessons:** both are democracies, but they dealt with the question of power sharing differently. In Belgium, the leaders realised that the unity of the country is possible only by **respecting the feelings and interests** of different communities. Sri Lanka shows that if a majority community wants to force its dominance over others and refuses to share power, it can **undermine the unity** of the country.\n\n"
         "**Why power sharing is desirable:**\n"
         "- **Prudential reasons** (based on careful calculation of gains and losses): power sharing is good because it helps to **reduce the possibility of conflict** between social groups. Since social conflict often leads to violence and political instability, power sharing is a good way to **ensure the stability of the political order**. Imposing the will of the majority over others may look attractive in the short run, but in the long run it undermines the unity of the nation. **Tyranny of the majority** is not just oppressive for the minority; it often brings ruin to the majority as well.\n"
         "- **Moral reasons** (the intrinsic worth of power sharing): power sharing is the **very spirit of democracy**. A democratic rule involves sharing power with those affected by its exercise, and who have to live with its effects. People have a **right to be consulted** on how they are to be governed. A **legitimate government** is one where citizens, through participation, acquire a stake in the system.\n"
         "Prudential reasons stress that power sharing brings **better outcomes**; moral reasons emphasise the very act of power sharing as **valuable in itself**."),
  C.kc("s3.check", "What is a 'community government' in Belgium?",
    [("A government elected by people of one language community, with power over culture, education and language", ""), ("The government of Brussels only", "Brussels has a separate government with equal representation."),
     ("A government run by village elders", "That is not the Belgian model."), ("The central government of Belgium", "The community government is a third kind of government.")],
    "It is elected by Dutch, French or German-speaking people, no matter where they live."),
  C.kc("s3.check2", "'Power sharing reduces conflict between social groups and ensures political stability.' This is a:",
    [("prudential reason", ""), ("moral reason", "Moral reasons stress the intrinsic value of power sharing."), ("majoritarian reason", "Majoritarianism opposes power sharing."), ("religious reason", "This is not about religion.")],
    "Prudential reasons are based on careful calculation of gains and losses."),
 ]},
 {"id": "s4", "title": "Forms of power sharing", "blocks": [
  blk("s4.thm", "theory", title="Four ways power is shared", revision=True,
    body="The idea of power sharing has emerged in opposition to the notion of **undivided political power**. For a long time it was believed that all power of a government must reside in one person or group located at one place. Modern democracies share power in many ways:\n\n"
         "1. **Horizontal distribution of power (among different organs of government):** power is shared among the **legislature, executive and judiciary**, placed at the same level to exercise different powers. Such separation ensures that none of the organs can exercise **unlimited power**; each organ **checks** the others. This is called a system of **checks and balances**. "
         "For example, in India the executive (ministers and officials) exercises power but is **responsible to Parliament or State Assemblies**; similarly, although judges are appointed by the executive, they can **check the functioning of the executive or laws made by legislatures**.\n"
         "2. **Vertical division of power (among governments at different levels):** a general government for the entire country (the **central or Union government**) and governments at the provincial or regional level (**state governments** in India). Such a general government for the entire country is usually called a **federal government**. The same principle can be extended to levels **lower than the state**, such as the **municipality and panchayat**.\n"
         "3. **Power shared among different social groups**, such as religious and linguistic groups. **'Community government'** in Belgium is a good example. In some countries there are constitutional and legal arrangements whereby **socially weaker sections and women** are represented in legislatures and administration, like the **reserved constituencies** in India. This gives space to minority communities in the government.\n"
         "4. **Power shared among political parties, pressure groups and movements:** in a democracy, citizens must have freedom to choose among various contenders for power. **Competition among parties** ensures that power does not remain in one hand; in the long run power is shared among parties that represent different ideologies and social groups. "
         "Sometimes this sharing is direct, when two or more parties form an alliance to contest elections and form a **coalition government**. Interest groups such as **traders, businessmen, industrialists, farmers and industrial workers** also share governmental power, through participation in governmental committees or by influencing decision-making."),
  blk("s4.table", "markdown_table", title="Forms of power sharing", revision=True, body=FORMSTAB),
  C.kc("s4.check", "Power shared among the legislature, executive and judiciary is called:",
    [("horizontal distribution of power", ""), ("vertical division of power", "Vertical is among levels of government."), ("community government", "That is sharing among social groups."), ("coalition government", "That is sharing among parties.")],
    "It creates a system of checks and balances."),
  C.kc("s4.check2", "When two or more parties form an alliance and run the government, it is a:",
    [("coalition government", ""), ("federal government", "Federal refers to levels of government."), ("community government", "That is for language communities in Belgium."), ("unitary government", "Unitary means one main level of government.")],
    "Germany's grand coalition of 2005 is an example."),
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Belgium numbers: \"59-40-1 and 80-20\"**: 59% Dutch (Flemish), 40% French (Wallonia), 1% German; Brussels 80% French, 20% Dutch.\n"
         "- **Sri Lanka numbers: \"74-18-13\"**: 74% Sinhala, 18% Tamil, 13% Sri Lankan Tamils.\n- **Sri Lanka timeline: 1948 independence → 1956 Sinhala only → 1980s Tamil Eelam demand → civil war ends 2009.**\n"
         "- **Belgian model: \"Equal, States, Brussels, Community\"** (equal ministers, powers to states, equal Brussels government, community government).\n"
         "- **Two reasons: Prudential = Peace (better outcomes); Moral = Meaning of democracy (intrinsic value).**\n- **Four forms: \"Here Visit Some Parties\"** = Horizontal, Vertical, Social groups, Parties."),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Swapping the Belgian figures: **59% speak Dutch** (Flemish region), **40% speak French** (Wallonia); in Brussels **80% speak French**.\n2. Saying the French speakers were the majority in Belgium: they were the **minority**, but richer and more powerful.\n"
         "3. Calling the 1956 Act a Tamil language Act: it made **Sinhala the only official language**.\n4. Mixing up prudential (better outcomes) and moral (intrinsic value) reasons.\n"
         "5. Saying horizontal sharing is among levels of government: horizontal is among **organs**; vertical is among **levels**.\n6. Saying the Sri Lankan civil war ended in 1983: it ended in **2009**."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Divide the class into a 'majority' and a 'minority' group and let them decide the class picnic spot twice: once by a simple majority vote, and once by a rule that needs both groups to agree. "
         "Discuss which decision the whole class accepted more happily, and link it to Belgium and Sri Lanka."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Think of your school or housing society. Give one example each of horizontal sharing, vertical sharing and sharing among groups that you can see there."),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Chapter 2 (Federalism):** vertical division of power in India.\n- **Chapter 3 (Gender, Religion and Caste):** sharing power with social groups and women.\n"
         "- **Chapter 4 (Political Parties):** competition and coalitions.\n- **Chapter 5 (Outcomes of Democracy):** accommodation of social diversity."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="'Belgium and Sri Lanka show two different ways of dealing with diversity.' Compare them in about 120 words.\n\n"
         "**Model answer:** Belgium recognised regional and cultural differences and amended its constitution four times between 1970 and 1993. It made the number of Dutch and French-speaking ministers equal, gave powers to state governments, set up a separate Brussels government with equal representation, and created community governments for culture, education and language. "
         "This accommodation avoided civic strife, kept the country united, and Brussels became the headquarters of the European Union. Sri Lanka followed majoritarianism: the 1956 Act made Sinhala the only official language, Sinhala applicants were favoured for jobs and universities, and the state was to protect Buddhism. "
         "Tamils felt alienated, demanded Tamil Eelam, and a civil war followed. Power sharing builds unity; majoritarianism destroys it."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Belgium (59% Dutch, 40% French, 1% German) faced tension because the French-speaking minority was richer and more powerful.\n"
         "- Sri Lanka (74% Sinhala, 18% Tamil) adopted majoritarian measures after 1948, alienating Tamils and leading to civil war (ended 2009).\n"
         "- Belgium accommodated diversity through equal ministers, powers to states, an equal Brussels government and community governments.\n"
         "- Power sharing is desirable for prudential reasons (less conflict, stability) and moral reasons (the spirit of democracy).\n"
         "- Forms: horizontal (organs), vertical (levels), among social groups, and among parties, pressure groups and movements."),
  blk("s5.examtips", "exam_tips", title="Board exam tips",
    body="- The 2025-26 sample paper asked which statements about Belgium's ethnic composition are true (1% German; Brussels 80% French, 20% Dutch), identified Germany's 2005 government as a coalition government, and had a 4-mark case study on Sri Lanka and Belgium (Tamil demands, results of majoritarianism, Belgian provisions).\n"
         "- 3/5-mark favourites: the Belgian model, majoritarianism in Sri Lanka, prudential and moral reasons, forms of power sharing with examples.\n"
         "- Memorise the exact percentages; options often swap them."),
  blk("s5.flash1", "flashcard", front="What is majoritarianism?", back="A belief that the majority community should rule a country in whatever way it wants, disregarding the wishes and needs of the minority."),
  blk("s5.flash2", "flashcard", front="Name the four elements of the Belgian model.", back="Equal Dutch and French ministers; powers to state governments; an equal Brussels government; community governments."),
  blk("s5.flash3", "flashcard", front="What is the difference between prudential and moral reasons for power sharing?", back="Prudential: it brings better outcomes (less conflict, stability). Moral: it is the very spirit of democracy and valuable in itself."),
  blk("s5.flash4", "flashcard", front="What are checks and balances?", back="A system in which each organ of government (legislature, executive, judiciary) checks the others, so none has unlimited power."),
 ]},
]

# ---------------- Sample paper ----------------
M("sqp20", BEL, "Which of the following statement(s) are true with respect to the ethnic composition of Belgium? I. 59 percent of the total population of Belgium lives in the Wallonia region and speaks French. II. 40 percent live in the Flemish region and speak Dutch. III. One percent of the Belgians speak German. IV. In the capital city Brussels, 80 percent people speak French while 20 per cent are Dutch speaking.",
  [("I and II", "Both are wrong: 59% live in the Flemish region and speak Dutch; 40% live in Wallonia and speak French."), ("III and IV", ""),
   ("I, II and III", "I and II swap the regions and languages."), ("I and IV", "Statement I is wrong.")],
  "Statements I and II swap the figures; III and IV are correct (CBSE marking scheme: B).", "hard", SQP(20), correct=1)
M("sqp21", FORMS, "Germany's government formed after the 2005 elections included the two major parties of the country, the Christian Democratic Union and the Social Democratic Party, which historically compete with each other. Which of the following options best explains this arrangement (shown in a cartoon in the NCERT book)?",
  [("Coalition Government.", ""), ("Two Party System.", "A two-party system means two parties compete; here they governed together."), ("Democratic government.", "True but too general."), ("Bi-party system.", "This means the same as a two-party system.")],
  "Two or more parties sharing power in an alliance form a coalition government.", "medium", SQP(21), correct=0)
M("sqp21vi", WHY, "Consider the following statements on Power Sharing and choose the correct statement(s): I. Imposing the will of the majority community over others. II. It helps in reducing the possibility of conflict between the social groups. III. Power Sharing is a good way to ensure the stability of political order. IV. It brings socio-political opposition among parties.",
  [("I and II", "Statement I describes majoritarianism, not power sharing."), ("I and III", "Statement I is wrong."), ("II and IV", "Power sharing does not aim at socio-political opposition."), ("II and III", "")],
  "Power sharing reduces conflict and ensures stability (sample paper, version for visually impaired candidates: D).", "medium", SQP("21 (VI)"), correct=3)
W("sqp28", "case_based", SL, "Read the given text and answer the questions.\n\n*\"Sri Lanka emerged as an independent country in 1948. The leaders of the Sinhala community sought to secure dominance over government by virtue of their majority. As a result, the democratically elected government adopted a series of MAJORITARIAN measures to establish Sinhala supremacy. Over the years, it created feelings of alienation among the Sri Lankan Tamils... On the other hand, the Belgian leaders took a different path. They recognised the existence of regional differences and cultural diversities. Between 1970 and 1993, they amended their constitution four times to work out an arrangement that would enable everyone to live together within the same country.\"* (Adapted from Power Sharing, NCERT)\n\n"
  "(i) State any one demand of the Tamils in Sri Lanka. (1)\n\n(ii) State the result of the majoritarian government in Sri Lanka. (1)\n\n(iii) Explain any two provisions of the Belgian model of power sharing. (2)",
  ["(i) Any one: recognition of Tamil as an official language; regional autonomy; equality of opportunity in securing education and jobs.",
   "(ii) It created distrust between the Tamil and Sinhala communities, which turned into a civil war; thousands were killed and many families became refugees.",
   "(iii) Any two: equal numbers of Dutch and French-speaking ministers in the central government; many powers given to state governments, which are not subordinate to the centre; a separate Brussels government with equal representation; community governments for cultural, educational and language issues."],
  source=SQP(28))

# ---------------- NCERT exercises ----------------
W("ex1", "short_answer", FORMS, "What are the different forms of power sharing in modern democracies? Give an example of each of these.",
  ["Horizontal: among the legislature, executive and judiciary (e.g. judges can check laws made by legislatures); vertical: among levels of government (e.g. union, state and local governments in India).",
   "Among social groups: e.g. community government in Belgium, reserved constituencies in India.",
   "Among political parties, pressure groups and movements: e.g. coalition governments; farmers' and traders' groups influencing decisions."], source=ex("1"))
W("ex2", "short_answer", WHY, "State one prudential reason and one moral reason for power sharing with an example from the Indian context.",
  ["Prudential reason: power sharing reduces conflict between social groups and ensures political stability.",
   "Example: reserved constituencies for Scheduled Castes and Tribes give them a share in power and reduce social tension.",
   "Moral reason: power sharing is the spirit of democracy; people have a right to be consulted, as in panchayati raj where people govern their own villages."], source=ex("2"))
W("ex3", "short_answer", WHY, "After reading this chapter, three students drew different conclusions. Thomman: power sharing is necessary only in societies which have religious, linguistic or ethnic divisions. Mathayi: power sharing is suitable only for big countries that have regional divisions. Ouseph: every society needs some form of power sharing even if it is small or does not have social divisions. Which of these do you agree with and why?",
  ["I agree with Ouseph.", "Power sharing is the very spirit of democracy: people affected by decisions have a right to be consulted, whatever the size or diversity of the society.",
   "Power sharing also prevents the concentration of power and the tyranny of the majority, so even small or uniform societies need it."], source=ex("3"))
W("ex4", "short_answer", BEL, "The Mayor of Merchtem, a town near Brussels in Belgium, has defended a ban on speaking French in the town's schools. He said that the ban would help all non-Dutch speakers integrate in this Flemish town. Do you think that this measure is in keeping with the spirit of Belgium's power sharing arrangements? Give your reasons.",
  ["No, the measure is against the spirit of Belgium's power sharing arrangements.",
   "Belgium's model is based on respecting all linguistic communities, with equal representation and community governments for language and education.",
   "Banning French imposes one community's language on others, which could revive the tensions that Belgium's accommodation was designed to remove."], source=ex("4"))
W("ex5", "very_short_answer", WHY, "Read the passage and pick out any one of the prudential reasons for power sharing offered in it: 'We want to give more power to the panchayats to realise the dream of Mahatma Gandhi... Giving power to panchayats is also a way to reduce corruption and increase administrative efficiency. When people participate in the planning and implementation of developmental schemes, they would naturally exercise greater control over these schemes. This would eliminate the corrupt middlemen...'",
  ["Prudential reason: giving power to panchayats reduces corruption and increases administrative efficiency.", "When people plan and implement schemes, they control them and eliminate corrupt middlemen."], source=ex("5"))
M("ex6", WHY, "Arguments in favour of power sharing are: A. reduces conflict among different communities; B. decreases the possibility of arbitrariness; C. delays decision making process; D. accommodates diversities; E. increases instability and divisiveness; F. promotes people's participation in government; G. undermines the unity of a country. Select the answer:",
  [("A B D F", ""), ("A C E F", "C and E are arguments against power sharing."), ("A B D G", "G is an argument against."), ("B C D G", "C and G are arguments against.")],
  "Power sharing reduces conflict, checks arbitrariness, accommodates diversity and promotes participation.", "medium", ex("6"), correct=0)
M("ex7", SL, "Consider: A. In Belgium, the Dutch-speaking majority people tried to impose their domination on the minority French-speaking community. B. In Sri Lanka, the policies of the government sought to ensure the dominance of the Sinhala-speaking majority. C. The Tamils in Sri Lanka demanded a federal arrangement of power sharing to protect their culture, language and equality of opportunity in education and jobs. D. The transformation of Belgium from unitary government to a federal one prevented a possible division of the country on linguistic lines. Which statements are correct?",
  [("A, B, C and D", "A is wrong: in Belgium the French-speaking minority was richer; the Dutch did not impose domination."), ("A, B and D", "A is wrong."), ("C and D", "B is also correct."), ("B, C and D", "")],
  "Belgium's leaders accommodated both communities instead of imposing majority rule.", "medium", ex("7"), correct=3)
M("ex8", FORMS, "Match: (1) power shared among different organs of government, (2) among governments at different levels, (3) by different social groups, (4) by two or more political parties, with (A) community government, (B) separation of powers, (C) coalition government, (D) federal government. The correct order for 1, 2, 3, 4 is:",
  [("D A B C", "1 is separation of powers, not federal government."), ("B C D A", "2 is federal government."), ("B D A C", ""), ("C D A B", "1 is separation of powers.")],
  "1-B, 2-D, 3-A, 4-C.", "medium", ex("8"), correct=2)
M("ex9", WHY, "Consider the two statements: A. Power sharing is good for democracy. B. It helps to reduce the possibility of conflict between social groups. Which of these statements are true and false?",
  [("A is true but B is false", "B is also true."), ("Both A and B are true", ""), ("Both A and B are false", "Both are true."), ("A is false but B is true", "A is true.")],
  "Power sharing is the spirit of democracy and reduces conflict.", "easy", ex("9"), correct=1)

# ---------------- MCQs ----------------
M("mcq01", BEL, "Belgium shares its borders with:",
  [("France, the Netherlands, Germany and Luxembourg", ""), ("Spain, Italy and Austria", "These do not border Belgium."), ("India and Sri Lanka", "Belgium is in Europe."), ("Switzerland and Poland only", "These do not border Belgium.")], "Belgium is a small country in Europe.")
M("mcq02", BEL, "What percentage of Belgians live in the Wallonia region and speak French?",
  [("40 per cent", ""), ("59 per cent", "59 per cent speak Dutch in the Flemish region."), ("80 per cent", "80 per cent of Brussels speaks French."), ("1 per cent", "1 per cent speak German.")], "The French-speakers were a minority in the country.")
M("mcq03", BEL, "In Brussels, the French-speaking people are:",
  [("80 per cent", ""), ("20 per cent", "20 per cent are Dutch-speaking."), ("40 per cent", "That is the national share."), ("59 per cent", "That is the Dutch national share.")], "The Dutch were a majority in the country but a minority in Brussels.")
M("mcq04", BEL, "Why did the Dutch-speaking community resent the French-speaking community?",
  [("The French-speakers were richer and more powerful, and the Dutch got development and education later", ""), ("The French-speakers were the majority", "They were the minority."),
   ("The Dutch-speakers ruled Brussels alone", "The Dutch were a minority in Brussels."), ("The French spoke German", "Not the reason.")], "This led to tension in the 1950s and 1960s.")
M("mcq05", BEL, "Between 1970 and 1993, Belgium amended its constitution:",
  [("four times", ""), ("once", "It was amended four times."), ("ten times", "It was amended four times."), ("never", "It was amended four times.")], "The aim was to let everyone live together.")
M("mcq06", BEL, "Which is NOT a feature of the Belgian model?",
  [("Sinhala made the only official language", ""), ("Equal Dutch and French ministers", "This is a feature."), ("A separate Brussels government", "This is a feature."), ("Community governments", "This is a feature.")], "Sinhala relates to Sri Lanka.")
M("mcq07", BEL, "Why did French-speakers accept equal representation in Brussels?",
  [("Because the Dutch-speaking community accepted equal representation in the central government", ""), ("Because they were forced by the army", "It was a compromise."),
   ("Because they were a minority in Brussels", "They were a majority in Brussels."), ("Because the EU demanded it", "The EU came later.")], "Each side gave something to the other.")
M("mcq08", BEL, "Belgium's community government has power over:",
  [("cultural, educational and language-related issues", ""), ("defence and foreign affairs", "These are for the central government."), ("currency", "Not a community issue."), ("only Brussels' roads", "It covers language communities everywhere.")], "It is elected by people of one language community.")
M("mcq09", BEL, "Which city was chosen as the headquarters of the European Union?",
  [("Brussels", ""), ("Paris", "The headquarters is in Brussels."), ("Colombo", "Colombo is in Sri Lanka."), ("Berlin", "The headquarters is in Brussels.")], "The Belgian model avoided division of the country.")
M("mcq10", SL, "The Sinhala-speakers form what share of Sri Lanka's population?",
  [("74 per cent", ""), ("18 per cent", "That is Tamil-speakers."), ("13 per cent", "That is Sri Lankan Tamils."), ("7 per cent", "That is Christians.")], "Sinhala-speakers are the majority.")
M("mcq11", SL, "'Indian Tamils' in Sri Lanka are those:",
  [("whose forefathers came from India as plantation workers in the colonial period", ""), ("who are natives of Sri Lanka", "Those are Sri Lankan Tamils."), ("who live in Tamil Nadu", "They live in Sri Lanka."), ("who speak Sinhala", "They speak Tamil.")], "Sri Lankan Tamils are natives concentrated in the north and east.")
M("mcq12", SL, "Most Sinhala-speaking people in Sri Lanka are:",
  [("Buddhists", ""), ("Hindus", "Most Tamils are Hindus or Muslims."), ("Christians", "About 7 per cent are Christians."), ("Jews", "Not mentioned.")], "Most Tamils are Hindus or Muslims.")
M("mcq13", SL, "Sri Lanka became independent in:",
  [("1948", ""), ("1956", "1956 was the Sinhala-only Act."), ("1947", "That was India."), ("2009", "2009 was the end of the civil war.")], "Its leaders then sought Sinhala dominance.")
M("mcq14", SL, "Which was a majoritarian measure in Sri Lanka?",
  [("Preferential policies for Sinhala applicants in universities and government jobs", ""), ("Equal ministers from both communities", "That was in Belgium."),
   ("Recognising Tamil as an official language", "Tamils demanded this, but it was refused."), ("Regional autonomy to Tamil provinces", "This was denied.")], "The new constitution also had the state protect Buddhism.")
M("mcq15", SL, "Which was NOT a demand of the Sri Lankan Tamils?",
  [("Making Buddhism the state religion", ""), ("Recognition of Tamil as an official language", "This was a demand."), ("Regional autonomy", "This was a demand."), ("Equality of opportunity in education and jobs", "This was a demand.")], "The constitution's support for Buddhism alienated Tamils.")
M("mcq16", SL, "By the 1980s, Tamil organisations demanded:",
  [("an independent Tamil Eelam in the north and east", ""), ("union with India", "Not the demand."), ("Sinhala as the official language", "They opposed this."), ("a community government like Belgium", "They demanded an independent state.")], "Distrust turned into civil war.")
M("mcq17", SL, "The civil war in Sri Lanka ended in:",
  [("2009", ""), ("1983", "The war continued long after."), ("1956", "1956 was the language Act."), ("1993", "1993 was Belgium's last amendment.")], "Thousands were killed and many became refugees.")
M("mcq18", WHY, "Majoritarianism means:",
  [("the majority community rules in whatever way it wants, disregarding the minority", ""), ("sharing power equally", "That is power sharing."), ("rule by the minority", "It is rule by the majority."), ("rule by judges", "Not the meaning.")], "Sri Lanka followed majoritarianism.")
M("mcq19", WHY, "Which is a prudential reason for power sharing?",
  [("It reduces the possibility of conflict and ensures political stability", ""), ("It is the very spirit of democracy", "That is a moral reason."), ("People have a right to be consulted", "That is a moral reason."), ("It gives citizens a stake in the system", "That is a moral reason.")], "Prudential reasons stress better outcomes.")
M("mcq20", WHY, "Which is a moral reason for power sharing?",
  [("People have a right to be consulted on how they are governed", ""), ("It reduces social conflict", "That is prudential."), ("It ensures political stability", "That is prudential."), ("It prevents violence", "That is prudential.")], "Moral reasons stress the intrinsic value of power sharing.")
M("mcq21", WHY, "'Tyranny of the majority' is harmful because:",
  [("it oppresses the minority and often ruins the majority as well", ""), ("it helps the minority", "It oppresses the minority."), ("it creates equal rights", "It denies them."), ("it brings stability", "It brings instability.")], "Sri Lanka's civil war hurt both communities.")
M("mcq22", WHY, "A legitimate government is one where:",
  [("citizens, through participation, acquire a stake in the system", ""), ("one person holds all power", "That is undivided power."), ("only the majority is consulted", "That is majoritarianism."), ("there are no elections", "Participation is needed.")], "This is a moral argument.")
M("mcq23", FORMS, "The system in which each organ of government checks the others is called:",
  [("checks and balances", ""), ("federalism", "Federalism is about levels of government."), ("coalition", "Coalition is among parties."), ("community government", "That is among language groups.")], "It prevents any organ from having unlimited power.")
M("mcq24", FORMS, "In India, although judges are appointed by the executive, they can:",
  [("check the functioning of the executive and laws made by legislatures", ""), ("make laws", "Legislatures make laws."), ("remove ministers at will", "Not their power."), ("run elections", "Not their role.")], "This is horizontal sharing of power.")
M("mcq25", FORMS, "Sharing power between union, state and local governments is:",
  [("vertical division of power", ""), ("horizontal distribution of power", "Horizontal is among organs."), ("community government", "That is among language groups."), ("coalition government", "That is among parties.")], "Federal government is an example.")
M("mcq26", FORMS, "Reserved constituencies for weaker sections in India are an example of power sharing among:",
  [("social groups", ""), ("organs of government", "That is horizontal."), ("levels of government", "That is vertical."), ("pressure groups only", "They represent social groups.")], "They give space to weaker sections and minorities.")
M("mcq27", FORMS, "Competition among political parties ensures that:",
  [("power does not remain in one hand", ""), ("only one party rules forever", "It prevents this."), ("pressure groups disappear", "Not related."), ("elections are not needed", "Competition needs elections.")], "In the long run power is shared among parties.")
M("mcq28", FORMS, "Traders, farmers and industrial workers sharing in governmental power through committees are examples of:",
  [("interest (pressure) groups", ""), ("judiciary", "Not the judiciary."), ("community government", "That is for language groups."), ("local government", "That is a level of government.")], "They influence decision-making.")
M("mcq29", FORMS, "The idea of power sharing emerged in opposition to:",
  [("undivided political power", ""), ("democracy", "Power sharing is part of democracy."), ("elections", "Elections share power among parties."), ("federalism", "Federalism is a form of power sharing.")], "Earlier, all power was thought to reside in one person or group.")
M("mcq30", FORMS, "Municipalities and panchayats show power sharing:",
  [("below the state level", ""), ("among organs of government", "They are a level of government."), ("among parties", "They are a level of government."), ("among language communities", "That is Belgium's community government.")], "This extends the vertical division of power.")
# ---------------- True / false ----------------
C.tf("tf1", BEL, "The French-speaking community was the majority in Belgium as a whole.", False, "They were 40 per cent, a minority, though richer and more powerful; they were a majority in Brussels.")
C.tf("tf2", SL, "The 1956 Act in Sri Lanka recognised Sinhala as the only official language.", True, "It disregarded Tamil.")
C.tf("tf3", WHY, "Power sharing is the very spirit of democracy.", True, "This is a moral reason for power sharing.")
C.tf("tf4", FORMS, "Horizontal distribution of power is among governments at different levels.", False, "Horizontal is among organs (legislature, executive, judiciary); vertical is among levels.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", BEL, "Why was the tension between communities more acute in Brussels?",
  ["The Dutch-speaking people were a majority in Belgium as a whole.", "But in Brussels they were a minority, as 80 per cent spoke French."])
W("vsa2", "very_short_answer", SL, "Who are Sri Lankan Tamils and Indian Tamils?",
  ["Sri Lankan Tamils are Tamil natives of Sri Lanka (13 per cent), concentrated in the north and east.", "Indian Tamils are those whose forefathers came from India as plantation workers in the colonial period."])
W("vsa3", "very_short_answer", WHY, "Distinguish between prudential and moral reasons for power sharing.",
  ["Prudential reasons stress that power sharing brings better outcomes: less conflict and more stability.", "Moral reasons stress that power sharing is valuable in itself, as the very spirit of democracy."])
W("sa1", "short_answer", SL, "Describe the majoritarian measures adopted in Sri Lanka.",
  ["In 1956, an Act recognised Sinhala as the only official language, disregarding Tamil.",
   "Governments followed preferential policies that favoured Sinhala applicants for university positions and government jobs.",
   "A new constitution stipulated that the state shall protect and foster Buddhism."])
W("sa2", "short_answer", SL, "How did majoritarianism affect Sri Lanka?",
  ["The Sri Lankan Tamils felt alienated and that their language, culture and equal rights were ignored.",
   "Their demands for Tamil as an official language, regional autonomy and equal opportunities were denied; by the 1980s they demanded Tamil Eelam.",
   "Distrust turned into a civil war: thousands were killed, many became refugees and lost livelihoods; the war ended only in 2009."])
W("sa3", "short_answer", FORMS, "Explain horizontal and vertical distribution of power with examples.",
  ["Horizontal distribution: power is shared among the legislature, executive and judiciary at the same level, creating checks and balances.",
   "Example: in India, ministers are responsible to Parliament, and judges can check the executive and laws made by legislatures.",
   "Vertical division: power is shared among governments at different levels, such as union, state and local (panchayat, municipality) governments."])
W("la1", "long_answer", BEL, "Explain the measures adopted by Belgium to accommodate its diversity.",
  ["Belgium amended its constitution four times between 1970 and 1993 to let everyone live together.",
   "The number of Dutch and French-speaking ministers in the central government is equal, and some special laws need a majority from each linguistic group.",
   "Many powers of the central government were given to state governments of the two regions, which are not subordinate to the centre.",
   "Brussels has a separate government in which both communities have equal representation.",
   "A third kind of government, the community government, elected by each language community, handles cultural, educational and language issues; this avoided civic strife, and Brussels became the EU headquarters."])
W("la2", "long_answer", FORMS, "Describe the four forms of power sharing in modern democracies.",
  ["Horizontal distribution: among the legislature, executive and judiciary, with checks and balances (judges can check the executive and legislatures).",
   "Vertical division: among governments at different levels, such as union and state (federal government), and local governments like panchayats and municipalities.",
   "Among social groups: community government in Belgium; reserved constituencies for weaker sections and women in India.",
   "Among political parties: competition ensures power does not stay in one hand; coalition governments share power directly.",
   "Among pressure groups and movements: traders, businessmen, farmers and industrial workers influence decisions or join government committees."])
W("cb1", "case_based", WHY, "Read the source and answer the questions.\n\n*\"Power sharing is good because it helps to reduce the possibility of conflict between social groups. Since social conflict often leads to violence and political instability, power sharing is a good way to ensure the stability of political order. Imposing the will of majority community over others may look like an attractive option in the short run, but in the long run it undermines the unity of the nation.\"* (NCERT)\n\n"
  "(i) What kind of reason for power sharing is given here? (1)\n\n(ii) What does imposing the will of the majority do in the long run? (1)\n\n(iii) Give one moral reason for power sharing and explain it. (2)",
  ["(i) A prudential reason.", "(ii) It undermines the unity of the nation.",
   "(iii) Power sharing is the very spirit of democracy: people affected by decisions have a right to be consulted on how they are governed, and a legitimate government is one where citizens participate and acquire a stake in the system."])
W("cb2", "case_based", BEL, "Read the source and answer the questions.\n\n*\"The ethnic composition of this small country is very complex. Of the country's total population, 59 per cent lives in the Flemish region and speaks Dutch language. Another 40 per cent people live in the Wallonia region and speak French. Remaining one per cent of the Belgians speak German. In the capital city Brussels, 80 per cent people speak French while 20 per cent are Dutch-speaking.\"* (NCERT)\n\n"
  "(i) Which community was the minority in Belgium but the majority in Brussels? (1)\n\n(ii) Why did the Dutch-speaking community resent the French-speakers? (1)\n\n(iii) How did Belgium solve this problem? Give two measures. (2)",
  ["(i) The French-speaking community.", "(ii) The French-speaking minority was richer and more powerful, and the Dutch got the benefits of development and education much later.",
   "(iii) Any two: equal Dutch and French ministers in the central government; powers to state governments; an equal Brussels government; community governments for culture, education and language."])
# ---------------- Assertion-reason ----------------
C.arq("ar1", BEL, "Belgium avoided civic strife and a division along linguistic lines.", "Belgium accommodated its communities through constitutional changes between 1970 and 1993.", 0,
      "R explains A.", "the Belgian model kept the country united.", "accommodation respected all groups.")
C.arq("ar2", SL, "The Sri Lankan Tamils felt alienated.", "The government adopted majoritarian measures to establish Sinhala supremacy.", 0,
      "R explains A.", "Tamils felt their rights were denied.", "majoritarian policies favoured Sinhala.")
C.arq("ar3", WHY, "Power sharing undermines the unity of a country.", "Power sharing reduces the possibility of conflict between social groups.", 3,
      "A is false: it is majoritarianism that undermines unity. R is true.", "power sharing strengthens unity.", "this is a prudential reason.")
C.arq("ar4", FORMS, "Judges in India can check laws made by legislatures.", "Horizontal distribution of power creates checks and balances.", 0,
      "R explains A.", "the judiciary checks other organs.", "each organ checks the others.")
C.arq("ar5", BEL, "Brussels has a separate government with equal representation for both communities.", "Brussels was chosen as the headquarters of the European Union.", 1,
      "Both are true, but R does not explain why Brussels has an equal government.", "this is part of the Belgian model.", "this followed Belgium's success.")
C.arq("ar6", SL, "Sinhala-speakers are a minority in Sri Lanka.", "Sri Lankan Tamils are concentrated in the north and east.", 3,
      "A is false: Sinhala-speakers are 74 per cent, the majority. R is true.", "they are the majority.", "this is where Sri Lankan Tamils live.")

chapter = header(SUBJ, N, "Power-sharing", ["belgium_model", "sri_lanka_majoritarianism", "why_power_sharing", "forms_of_power_sharing"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: this chapter is fully in the board examination (Political Science: 20 marks). There is no map item from this chapter.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
