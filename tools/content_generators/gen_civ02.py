"""CBSE Class 10 Political Science Ch 2: Federalism (fully in the 2025-26 board syllabus)."""
import sys
from ss_common import make, header, path, SQP, SHINE, CB

ROOT = sys.argv[1]
SUBJ, N = "civics", 2
PATH = path(SUBJ, "ch02_federalism")
C = make(SUBJ, N, "civ10ch02")
blk, M, W = C.blk, C.m, C.w
WHAT, IND, PRAC, DEC = ["what_is_federalism"], ["india_federal_country"], ["federalism_in_practice"], ["decentralisation"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 2 exercises", "question": n}

UNITAB = ("| | Federal government | Unitary government |\n|---|---|---|\n| **Levels** | two or more levels, each with its own powers | only one level, or sub-units subordinate to the centre |\n"
          "| **Powers of units** | guaranteed by the constitution; the centre cannot order the state government | given and taken back by the central government |\n"
          "| **Changing the division of power** | needs the consent of both levels | the central government can do it alone |\n| **Examples** | India, USA, Switzerland, Australia, Belgium (since 1993) | Sri Lanka, UK, France |")
ROUTES = ("| | Coming together federation | Holding together federation |\n|---|---|---|\n| **How formed** | independent states come together on their own to form a bigger unit | a large country decides to divide its power between the national government and constituent states |\n"
          "| **Powers of states** | constituent states usually have **equal** power and are strong | the central government tends to be more powerful; states may have **unequal** powers |\n"
          "| **Examples** | USA, Switzerland, Australia | India, Spain, Belgium |")
LISTS = ("| List | Who makes laws | Examples of subjects |\n|---|---|---|\n| **Union List** | Union Government | defence, foreign affairs, banking, communications, currency |\n"
         "| **State List** | State Governments | police, trade, commerce, agriculture, irrigation |\n| **Concurrent List** | both; if laws conflict, the Union law prevails | education, forest, trade unions, marriage, adoption, succession |\n"
         "| **Residuary subjects** | Union Government | subjects not in any list, such as computer software |")
LOCAL = ("| Level | Rural (Panchayati Raj) | Urban |\n|---|---|---|\n| **Village / town** | gram panchayat: ward members (panch) and a president (sarpanch), directly elected; supervised by the gram sabha | municipality, headed by a municipal chairperson |\n"
         "| **Block** | panchayat samiti (block or mandal), elected by the panchayat members of the area | big cities: municipal corporation, headed by a mayor |\n"
         "| **District** | zilla parishad, with elected members, Lok Sabha MPs and MLAs of the district; headed by a chairperson | |")

sections = [
 {"id": "s1", "title": "Who governs what?", "blocks": [
  blk("s1.hook", "hook", title="Who fixes your street light?",
    body="The army that guards the border is run from New Delhi. The police station in your area is run by your state government. The broken street light outside your house is the job of your municipality or panchayat.\n\n"
         "India has more than one level of government, and each has its own work. This is **federalism**. In this chapter you will see what makes a country federal, how India shares power between the Union, the states and local governments, and why this has kept a very diverse country united."),
  blk("s1.inspiration", "inspiration", title="Unity through diversity", person="Dr B.R. Ambedkar", years="1891–1956",
    body="As Chairman of the Drafting Committee of the Constitution, **Dr B.R. Ambedkar** helped design India as a **'Union of States'**. He explained that the Indian federation was not the result of an agreement among states, so no state had the right to leave it.\n\n"
         "At the same time, the Constitution gave states their own powers and lists of subjects. This balance of a strong Union with real powers for the states has helped India hold together through languages, regions and cultures.",
    future="This chapter leads to careers in law, civil services, public administration, panchayat and municipal work, and policy research."),
  C.socratic("s1.socratic", "Why might a huge, diverse country like India need more than one level of government?",
    ["Different regions have different needs, and local governments know local problems better", "Because one government is always enough", "Because states want to leave the country"], 0,
    "Federalism accommodates regional diversity while keeping the country united."),
 ]},
 {"id": "s2", "title": "What is federalism?", "blocks": [
  blk("s2.thm", "theory", title="Meaning, features and two routes", revision=True,
    body="**Belgium and Sri Lanka:** in **1993**, Belgium shifted from a unitary to a federal form of government: its regional governments were given constitutional powers that were no longer dependent on the central government. Sri Lanka continues to be, for all practical purposes, a **unitary** system.\n\n"
         "**Federalism** is a system of government in which the power is divided between a **central authority** and various **constituent units** of the country. Usually a federation has two levels of government: one for the **entire country**, responsible for subjects of common national interest, and others at the level of **provinces or states**, which look after much of the day-to-day administration of their state.\n\n"
         "**Unitary system:** there is either only one level of government, or the sub-units are subordinate to the central government. The central government can pass on orders to the provincial or local government. In a federal system, the central government **cannot order** the state government to do something; the state government has powers of its own for which it is not answerable to the central government.\n\n"
         "**Key features of federalism:**\n"
         "1. There are **two or more levels (tiers)** of government.\n"
         "2. Different tiers govern the **same citizens**, but each tier has its **own jurisdiction** in specific matters of legislation, taxation and administration.\n"
         "3. The jurisdictions of the tiers are **specified in the constitution**, so the existence and authority of each tier is constitutionally guaranteed.\n"
         "4. The fundamental provisions of the constitution **cannot be unilaterally changed** by one level of government; such changes require the **consent of both levels**.\n"
         "5. **Courts** have the power to interpret the constitution and the powers of different levels. The highest court acts as an **umpire** if disputes arise between levels.\n"
         "6. **Sources of revenue** for each level are clearly specified to ensure its **financial autonomy**.\n"
         "7. The federal system has **dual objectives**: to safeguard and promote the **unity** of the country, while accommodating **regional diversity**. So two aspects are crucial: governments at different levels should **agree to some rules** of power sharing, and should **trust** that each will abide by its part. An ideal federal system has both: **mutual trust and agreement to live together**.\n\n"
         "**Two routes to federations:**\n"
         "- **Coming together federations:** independent states come together on their own to form a bigger unit, so that by pooling sovereignty and retaining identity they can increase their security. The constituent states usually have **equal power** and are strong vis-à-vis the federal government. Examples: the **USA, Switzerland and Australia**.\n"
         "- **Holding together federations:** a large country decides to divide its power between the constituent states and the national government. The central government tends to be **more powerful**, and very often the constituent units have **unequal powers**; some units are granted special powers. Examples: **India, Spain and Belgium**."),
  blk("s2.table", "markdown_table", title="Federal and unitary governments", revision=True, body=UNITAB),
  blk("s2.table2", "markdown_table", title="Two routes to federation", revision=True, body=ROUTES),
  C.kc("s2.check", "In a federal system, the powers of each level of government are guaranteed by:",
    [("the constitution", ""), ("the central government", "In a unitary system, the centre gives and takes powers."), ("the President alone", "No single office guarantees them."), ("the local government", "Local governments are one of the levels.")],
    "The jurisdictions of each tier are specified in the constitution."),
  C.kc("s2.check2", "India is an example of which type of federation?",
    [("holding together federation", ""), ("coming together federation", "That is the USA, Switzerland and Australia."), ("unitary federation", "There is no such type."), ("confederation", "India is a federation, not a loose confederation.")],
    "In India, a large country divided its power between the Union and the states."),
 ]},
 {"id": "s3", "title": "What makes India a federal country?", "blocks": [
  blk("s3.thm", "theory", title="The Constitution, the three lists and the role of courts", revision=True,
    body="The Constitution declared India as a **Union of States**. Although it did not use the word federation, the Indian Union is based on the principles of federalism.\n\n"
         "The Constitution originally provided for a **two-tier** system: the **Union Government** (Central Government) for the entire Union of India, and the **State Governments** for each unit or state. Later, a **third tier** of federalism was added in the form of **Panchayats and Municipalities**. Each tier enjoys separate jurisdiction.\n\n"
         "**Three-fold distribution of legislative powers:**\n"
         "- **Union List:** subjects of national importance such as **defence, foreign affairs, banking, communications and currency**. A uniform policy is needed on these matters throughout the country, so only the Union Government can make laws on them.\n"
         "- **State List:** subjects of state and local importance such as **police, trade, commerce, agriculture and irrigation**. Only the State Governments can make laws on them.\n"
         "- **Concurrent List:** subjects of common interest to both, such as **education, forest, trade unions, marriage, adoption and succession**. Both can make laws; if their laws **conflict**, the law made by the **Union Government prevails**.\n"
         "- **Residuary subjects:** subjects that came up after the Constitution was made and are not in any list, such as **computer software**. The Union Government has the power to legislate on them.\n\n"
         "**Unequal powers:** most federations that are formed by holding together do not give equal power to their constituent units. In India, some states enjoy a special status: states such as **Assam, Nagaland, Arunachal Pradesh and Mizoram** enjoy special powers under certain provisions of the Constitution (**Article 371**) due to their peculiar social and historical circumstances. These special powers relate especially to the **protection of land rights of indigenous peoples**, their culture, and preferential employment in government service.\n\n"
         "**Union Territories:** some units are too small to become independent states and cannot be merged with existing states, such as **Chandigarh, Lakshadweep** or the capital city of **Delhi**. They do not have the powers of a state; the Central Government has special powers in running them.\n\n"
         "**Changing the division of power is not easy:** the Parliament cannot on its own change this arrangement. Any change has to be first passed by **both the Houses of Parliament with at least two-thirds majority**, and then **ratified by the legislatures of at least half of the total states**.\n\n"
         "**Role of the judiciary:** the **High Courts and the Supreme Court** oversee the implementation of constitutional provisions and procedures. In case of any dispute about the division of powers, the courts make the decision.\n\n"
         "**Revenue:** the Union and State governments have the power to **raise resources by levying taxes** to carry on the government and the responsibilities assigned to each of them."),
  blk("s3.table", "markdown_table", title="The three lists", revision=True, body=LISTS),
  C.kc("s3.check", "On which list is 'currency'?",
    [("Union List", ""), ("State List", "The State List has police, trade, agriculture and irrigation."), ("Concurrent List", "The Concurrent List has education, forest and marriage."), ("Residuary subjects", "Residuary subjects are not in any list.")],
    "Currency needs a uniform policy for the whole country, so it is on the Union List."),
  C.kc("s3.check2", "A change in the division of powers between the Union and the states needs:",
    [("two-thirds majority in both Houses of Parliament and ratification by at least half of the state legislatures", ""), ("a simple majority in the Lok Sabha only", "Parliament cannot do it alone."),
     ("an order of the Prime Minister", "No single office can change it."), ("approval of the Supreme Court only", "Courts interpret the constitution; they do not amend it.")],
    "The consent of both levels is needed."),
 ]},
 {"id": "s4", "title": "How is federalism practised?", "blocks": [
  blk("s4.thm", "theory", title="Linguistic states, language policy and Centre-State relations", revision=True,
    body="Constitutional provisions are necessary, but the real success of federalism in India comes from the nature of **democratic politics**. The spirit of federalism, respect for diversity and the desire for living together became shared ideals. Three examples:\n\n"
         "**1. Linguistic States:** the creation of linguistic states was the first and a major test for democratic politics in India. After independence, the boundaries of several old states were changed to create new states, so that people who spoke the same language lived in the same state. Some states were created not on the basis of language but to recognise differences based on **culture, ethnicity or geography**, such as **Nagaland, Uttarakhand and Jharkhand**.\n"
         "- When the demand for states on the basis of language was raised, some national leaders **feared** it would lead to the disintegration of the country, and the Central Government **resisted** linguistic states for some time.\n"
         "- Experience has shown that the formation of linguistic states has actually made the country **more united**, and has also made **administration easier**.\n\n"
         "**2. Language policy:** the Constitution did **not give the status of national language** to any one language.\n"
         "- **Hindi** was identified as the **official language**, but Hindi is the mother tongue of only about **40 per cent** of Indians, so there were many safeguards to protect other languages.\n"
         "- Besides Hindi, there are **21 other languages** recognised as **Scheduled Languages** by the Constitution. A candidate in an examination for a Central Government position may opt to take the examination in any of these languages. States too have their own official languages, and much government work takes place in the official language of the concerned state.\n"
         "- According to the Constitution, the use of **English** for official purposes was to stop in **1965**. Many non-Hindi speaking states demanded that the use of English continue. In **Tamil Nadu**, this movement took a violent form. The Central Government responded by agreeing to **continue the use of English along with Hindi** for official purposes.\n"
         "- Promotion of Hindi continues to be the official policy, but this means that the Central Government cannot **impose** Hindi on states where people speak a different language. This flexibility helped India avoid the kind of situation that Sri Lanka found itself in.\n\n"
         "**3. Centre-State relations:** restructuring Centre-State relations is another way in which federalism has been strengthened in practice.\n"
         "- For a long time, the **same party** ruled both at the Centre and in most states, so state governments did not exercise their rights as autonomous federal units. When the ruling party at the state level was different, the Centre often **misused** the Constitution to **dismiss** state governments controlled by rival parties.\n"
         "- All this changed significantly after **1990**, with the **rise of regional political parties** in many states and the beginning of the era of **coalition governments** at the Centre. Since no single party got a clear majority in the Lok Sabha, the major national parties had to enter into alliances with many parties, including regional parties. This led to a **new culture of power sharing** and respect for the autonomy of state governments.\n"
         "- This trend was supported by a major judgement of the **Supreme Court** (**S.R. Bommai case, 1994**) that made it difficult for the Central Government to dismiss state governments in an arbitrary manner."),
  C.kc("s4.check", "Which states were created on the basis of culture, ethnicity or geography rather than language?",
    [("Nagaland, Uttarakhand and Jharkhand", ""), ("Tamil Nadu, Kerala and Karnataka", "These are linguistic states."), ("Gujarat and Maharashtra", "These were formed on the basis of language."), ("Delhi and Chandigarh", "These are Union Territories.")],
    "Some states recognised differences of culture, ethnicity or geography."),
  C.kc("s4.check2", "What happened to the use of English for official purposes after 1965?",
    [("It continued along with Hindi", ""), ("It stopped completely", "Non-Hindi states protested, so it continued."), ("It replaced Hindi", "Hindi remained the official language."), ("It became the national language", "India has no national language.")],
    "The Centre agreed to continue English along with Hindi after protests, especially in Tamil Nadu."),
 ]},
 {"id": "s5", "title": "Decentralisation in India", "blocks": [
  blk("s5.thm", "theory", title="The third tier: panchayats and municipalities", revision=True,
    body="A vast country like India cannot be run only through two tiers. States in India are as large as independent countries of Europe, and are internally very diverse. So federal power sharing in India needs **another tier** of government, below the state governments.\n\n"
         "**Decentralisation:** when power is taken away from Central and State governments and given to **local government**. The basic idea is that a large number of problems and issues are best settled at the **local level**: people have better knowledge of problems in their localities, and know better where to spend money and how to manage things efficiently. Local people can also **participate directly** in decision making. This helps inculcate a habit of democratic participation; local government is the best way to realise one important principle of democracy, namely **local self-government**.\n\n"
         "**Before 1992:** panchayats in villages and municipalities in urban areas existed, but they were under the **direct control of state governments**. Elections were **not held regularly**, and local governments did not have any **powers or resources** of their own.\n\n"
         "**The 1992 constitutional amendment** (73rd and 74th amendments) made the third tier more powerful and effective:\n"
         "- It is **constitutionally mandatory** to hold **regular elections** to local government bodies.\n"
         "- Seats are **reserved** in the elected bodies and the executive heads of these institutions for the **Scheduled Castes, Scheduled Tribes and Other Backward Classes**.\n"
         "- At least **one-third** of all positions are reserved for **women**.\n"
         "- An independent institution called the **State Election Commission** has been created in each state to conduct panchayat and municipal elections.\n"
         "- The state governments are required to **share some powers and revenue** with local government bodies. The nature of sharing varies from state to state.\n\n"
         "**Rural local government (Panchayati Raj):**\n"
         "- Each village, or a group of villages in some states, has a **gram panchayat**: a council of several ward members, often called **panch**, and a president or **sarpanch**. They are directly elected by all the adult population living in that ward or village. It is the decision-making body for the entire village.\n"
         "- The panchayat works under the overall supervision of the **gram sabha**. All the voters in the village are its members. It has to meet at least twice or thrice a year to approve the annual budget of the gram panchayat and to review its performance.\n"
         "- A few gram panchayats are grouped together to form a **panchayat samiti** (block or **mandal**). Its members are elected by all the panchayat members in that area.\n"
         "- All the panchayat samitis or mandals in a district together constitute the **zilla (district) parishad**. Most members are elected; **Members of the Lok Sabha and MLAs** of that district and some other officials are also its members. The **zilla parishad chairperson** is its political head.\n\n"
         "**Urban local government:** **municipalities** are set up in towns; big cities are constituted into **municipal corporations**. Both are controlled by elected bodies of people's representatives. The **municipal chairperson** is the political head of the municipality; in a municipal corporation, this officer is called the **mayor**.\n\n"
         "**Achievement and limits:** this new system of local government is the **largest experiment in democracy** conducted anywhere in the world. Constitutional status has helped deepen democracy, and the reservation for women has increased their representation and voice. But **gram sabhas are not held regularly**, and most state governments have **not transferred significant powers and adequate resources** to local governments. So we are still a long way from realising the ideal of self-government."),
  blk("s5.table", "markdown_table", title="Local government in India", revision=True, body=LOCAL),
  C.kc("s5.check", "What fraction of positions in local bodies is reserved for women?",
    [("at least one-third", ""), ("one-half in the Constitution", "The 1992 amendment says at least one-third (some states give more)."), ("one-fourth", "It is at least one-third."), ("none", "Seats are reserved for women.")],
    "At least one-third of all positions are reserved for women."),
  C.kc("s5.check2", "Who supervises the work of the gram panchayat?",
    [("the gram sabha", ""), ("the zilla parishad chairperson", "The zilla parishad is the district level."), ("the mayor", "A mayor heads a municipal corporation."), ("the Governor", "The Governor heads the state.")],
    "All the voters of the village are members of the gram sabha, which supervises the panchayat."),
 ]},
 {"id": "s6", "title": "Remember, avoid, practise", "blocks": [
  blk("s6.memory", "memory_trick", title="Memory tricks",
    body="- **Union List \"DFBCC\"**: Defence, Foreign affairs, Banking, Communications, Currency.\n- **State List \"PTCAI\"**: Police, Trade, Commerce, Agriculture, Irrigation.\n"
         "- **Concurrent List \"EFT MAS\"**: Education, Forest, Trade unions, Marriage, Adoption, Succession.\n- **Residuary = Recent** (computer software): goes to the Union.\n"
         "- **Coming together = USA** (\"US come together\", also Switzerland, Australia); **Holding together = I-S-B** (India, Spain, Belgium).\n"
         "- **1992 amendment \"RRWSS\"**: Regular elections, Reservation for SC/ST/OBC, Women one-third, State Election Commission, Sharing powers and revenue.\n"
         "- **Amendment rule \"2/3 + half\"**: two-thirds of both Houses, then half the states."),
  blk("s6.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying Hindi is India's **national** language: the Constitution gave no language that status; Hindi is the **official** language.\n2. Putting education on the State List: it is on the **Concurrent List**.\n"
         "3. Calling India a coming together federation: India is a **holding together** federation.\n4. Saying residuary powers belong to states: they belong to the **Union**.\n"
         "5. Saying Parliament alone can change the division of powers: it also needs ratification by **at least half of the states**.\n6. Writing that one-half of local seats are reserved for women by the Constitution: the amendment says **at least one-third**."),
  blk("s6.tip", "teacher_tip", title="Try this in class",
    body="Give pairs of students a pile of cards (defence, police, education, currency, irrigation, marriage, banking, trade, computer software) and ask them to sort the cards into Union, State, Concurrent and Residuary. Then ask: why should defence be decided in Delhi, but police in each state?"),
  blk("s6.reflection", "reflection", title="Think and explain",
    body="Find out the name of your sarpanch or municipal councillor, and one work done by your local body. Is this work better done locally or by the state government? Why?"),
  blk("s6.connection", "connection", title="Where this leads",
    body="- **Chapter 1 (Power-sharing):** federalism is the vertical division of power.\n- **Chapter 4 (Political Parties):** regional parties and coalition governments.\n"
         "- **Chapter 5 (Outcomes of Democracy):** accommodation of social diversity."),
  blk("s6.mastery", "mastery", title="Mastery challenge",
    body="'Federalism has been strengthened in India by democratic politics.' Justify in about 120 words.\n\n"
         "**Model answer:** The Constitution set up a three-fold division of powers, but democratic politics made it work. Linguistic states were created so that people speaking the same language lived in one state; this made the country more united and administration easier. "
         "The language policy gave no language the status of national language; 21 other languages were scheduled besides Hindi, and English continued along with Hindi after protests in non-Hindi states. "
         "After 1990, regional parties grew and coalition governments at the Centre led to a new culture of power sharing and respect for state autonomy, supported by a Supreme Court judgement that stopped arbitrary dismissal of state governments. "
         "The 1992 amendment gave local governments regular elections, reservation and resources. Together, these deepened federalism."),
  blk("s6.summary", "summary", title="Chapter summary",
    body="- Federalism divides power between a central authority and constituent units; each level's powers are guaranteed by the constitution.\n"
         "- Federations are formed by coming together (USA, Switzerland, Australia) or holding together (India, Spain, Belgium).\n"
         "- India has a Union List, State List, Concurrent List and residuary subjects; Union law prevails on concurrent conflicts.\n"
         "- Changing the division needs a two-thirds majority in both Houses and ratification by half the states; courts act as umpire.\n"
         "- Linguistic states, a flexible language policy and better Centre-State relations after 1990 strengthened federalism.\n"
         "- The 1992 amendment created a strong third tier: regular elections, reservations, one-third seats for women, State Election Commissions and shared powers."),
  blk("s6.examtips", "exam_tips", title="Board exam tips",
    body="- The 2025-26 sample paper asked whether a state can stop the Union from issuing new currency notes (no, because currency is on the Union List) and asked for any two key features of federalism (2 marks).\n"
         "- 3/5-mark favourites: features of federalism, the three lists, coming together and holding together, how federalism is practised, the 1992 amendment, and the structure of panchayati raj.\n"
         "- Always give an example subject when you name a list."),
  blk("s6.flash1", "flashcard", front="What is federalism?", back="A system of government in which power is divided between a central authority and various constituent units of the country."),
  blk("s6.flash2", "flashcard", front="Name three subjects on each list.", back="Union: defence, foreign affairs, currency. State: police, agriculture, irrigation. Concurrent: education, forest, marriage."),
  blk("s6.flash3", "flashcard", front="What is decentralisation?", back="Taking power away from the Central and State governments and giving it to local government."),
  blk("s6.flash4", "flashcard", front="How can the division of powers in India be changed?", back="By a two-thirds majority in both Houses of Parliament, then ratification by the legislatures of at least half of the states."),
 ]},
]

# ---------------- Sample paper ----------------
M("sqp22", IND, "Suppose the Government of India plans to issue new currency notes of different denominations in order to curb the influence of black money. The Government of one state is opposed to this policy of the Central Government. Can the state government stop the union government from implementing this policy?",
  [("Yes, because Currency is the subject of State List", "Currency is on the Union List."), ("No, because Currency is a subject of Union List", ""),
   ("Yes, because the approval of both the governments is necessary to implement this change.", "Only the Union can make laws on Union List subjects."), ("No, because any such change must be approved by the local government also.", "Local governments have no role in currency.")],
  "Only the Union Government can make laws on Union List subjects such as currency (CBSE marking scheme: B).", "medium", SQP(22), correct=1)
W("sqp24", "very_short_answer", WHAT, "Highlight any two key features of federalism.",
  ["Any two: there are two or more levels of government; each level governs the same citizens but has its own jurisdiction in legislation, taxation and administration; the jurisdictions are specified in the constitution, so each level's existence and authority is guaranteed.",
   "Or: fundamental provisions cannot be changed unilaterally by one level; courts interpret the constitution and act as umpire in disputes; sources of revenue of each level are clearly specified for financial autonomy."], source=SQP(24))

# ---------------- NCERT exercises ----------------
W("ex3", "very_short_answer", IND, "Point out one feature in the practice of federalism in India that is similar to and one feature that is different from that of Belgium.",
  ["Similar: both India and Belgium are holding together federations, where power is divided between the central government and the states, and both accommodate linguistic diversity.",
   "Different: Belgium has a community government for each language community and an equal Brussels government; India has no community government, but has a constitutionally recognised third tier of panchayats and municipalities."], source=ex("3"))
W("ex4", "short_answer", WHAT, "What is the main difference between a federal form of government and a unitary one? Explain with an example.",
  ["In a federal government, power is divided between two or more levels, each with its own powers guaranteed by the constitution; the centre cannot order the states.",
   "In a unitary government, there is either one level, or the sub-units are subordinate to the central government, which can give orders to them.",
   "Example: India is federal, with the Union and states having separate lists of subjects; Sri Lanka is, for practical purposes, unitary, where the national government has all the power."], source=ex("4"))
W("ex5", "short_answer", DEC, "State any two differences between the local government before and after the constitutional amendment in 1992.",
  ["Before 1992, elections to local bodies were not held regularly; after 1992, it became constitutionally mandatory to hold regular elections, conducted by the State Election Commission.",
   "Before 1992, local bodies had no powers or resources of their own and were under the direct control of state governments; after 1992, states must share some powers and revenue with them.",
   "After 1992, seats are also reserved for SC, ST and OBC, and at least one-third of all positions for women."], source=ex("5"))
W("ex7", "short_answer", PRAC, "Here are three reactions to the language policy followed in India. Give an argument or an example to support any of these positions. Sangeeta: The policy of accommodation has strengthened national unity. Arman: Language-based States have divided us by making everyone conscious of their language. Harish: This policy has only helped to consolidate the dominance of English over all other languages.",
  ["Supporting Sangeeta: India did not impose one language; Hindi is the official language, but 21 other languages are Scheduled Languages.",
   "Candidates may take Central Government examinations in any of these languages, and English continued along with Hindi after protests in non-Hindi states.",
   "This flexibility, along with linguistic states, made the country more united and helped India avoid a Sri Lanka-like conflict."], source=ex("7"))
M("ex6", WHAT, "Fill in the blanks: Since the United States is a ___ type of federation, all the constituent States have equal powers and States are ___ vis-à-vis the federal government. But India is a ___ type of federation and some States have more power than others. In India, the ___ government has more powers.",
  [("coming together; strong; holding together; central", ""), ("holding together; weak; coming together; state", "The USA is a coming together federation; India is holding together."),
   ("coming together; weak; holding together; state", "States in the USA are strong, and India's central government has more powers."), ("unitary; strong; federal; local", "Both are federations.")],
  "In a coming together federation states are equal and strong; in a holding together federation the centre is more powerful.", "medium", ex("6"), correct=0)
M("ex8", WHAT, "The distinguishing feature of a federal government is:",
  [("Governmental power is divided between different levels of government.", ""), ("National government gives some powers to the provincial governments.", "In a federation, powers are guaranteed by the constitution, not given by the centre."),
   ("Power is distributed among the legislature, executive and judiciary.", "That is horizontal sharing, found in unitary systems too."), ("Elected officials exercise supreme power in the government.", "That is a feature of democracy, not federalism.")],
  "Federalism means division of power between levels of government.", "easy", ex("8"), correct=0)
M("ex9", IND, "Group these subjects: Defence, Police, Agriculture, Education, Banking, Forests, Communications, Trade, Marriages. Which grouping is correct?",
  [("Union: Defence, Banking, Communications; State: Police, Agriculture, Trade; Concurrent: Education, Forests, Marriages", ""),
   ("Union: Defence, Police, Agriculture; State: Education, Banking, Forests; Concurrent: Communications, Trade, Marriages", "Police and agriculture are State subjects; banking and communications are Union subjects."),
   ("Union: Defence, Education, Banking; State: Police, Agriculture, Trade; Concurrent: Forests, Communications, Marriages", "Education is Concurrent; communications is Union."),
   ("Union: Banking, Trade, Marriages; State: Police, Agriculture, Forests; Concurrent: Defence, Education, Communications", "Defence and communications are Union subjects.")],
  "Union: defence, banking, communications; State: police, agriculture, trade; Concurrent: education, forests, marriages.", "medium", ex("9"), correct=0)
M("ex10", IND, "Which pair of a level of government and its law-making power is NOT correctly matched?",
  [("Local governments: Residuary powers", ""), ("State government: State List", "This is correct."), ("Central government: Union List", "This is correct."), ("Central and State governments: Concurrent List", "This is correct.")],
  "Residuary powers belong to the Union Government.", "medium", ex("10"), correct=0)
M("ex11", DEC, "Match: (1) Union of India, (2) State, (3) Municipal Corporation, (4) Gram Panchayat with (A) Prime Minister, (B) Sarpanch, (C) Governor, (D) Mayor. The correct order for 1, 2, 3, 4 is:",
  [("A C D B", ""), ("D A B C", "The Union is headed (in government) by the Prime Minister."), ("A B C D", "A State has a Governor, not a sarpanch."), ("C A D B", "The Governor heads a State, not the Union.")],
  "1-A, 2-C, 3-D, 4-B.", "easy", ex("11"), correct=0)
M("ex12", WHAT, "Consider: a. In a federation, the powers of the federal and provincial governments are clearly demarcated. b. India is a federation because the powers of the Union and State Governments are specified in the Constitution and they have exclusive jurisdiction on their respective subjects. c. Sri Lanka is a federation because the country is divided into provinces. d. India is no longer a federation because some powers of the states have been devolved to the local government bodies. Which statements are correct?",
  [("a and b", ""), ("a, b and c", "Sri Lanka is, for practical purposes, unitary."), ("a, c and d", "c and d are wrong."), ("b and d", "Decentralisation strengthens federalism; d is wrong.")],
  "Only a and b are correct.", "medium", ex("12"), correct=0)

# ---------------- MCQs ----------------
M("mcq01", WHAT, "In which year did Belgium shift from a unitary to a federal form of government?",
  [("1993", ""), ("1970", "1970 was the first of four amendments."), ("1948", "1948 is Sri Lanka's independence."), ("1992", "1992 is India's local government amendment.")], "Regional governments were given constitutional powers in 1993.")
M("mcq02", WHAT, "Which country is, for all practical purposes, a unitary system?",
  [("Sri Lanka", ""), ("India", "India is federal."), ("Belgium", "Belgium became federal in 1993."), ("USA", "The USA is federal.")], "The national government of Sri Lanka has all the power.")
M("mcq03", WHAT, "In a federation, the highest court acts as:",
  [("an umpire in disputes between levels of government", ""), ("the law-maker for both levels", "Legislatures make laws."), ("the head of the state governments", "Courts do not head governments."), ("the collector of taxes", "Governments collect taxes.")], "Courts interpret the constitution and the powers of each level.")
M("mcq04", WHAT, "Which is NOT a feature of federalism?",
  [("The central government can change the powers of states on its own", ""), ("Two or more levels of government", "This is a feature."), ("Each level's jurisdiction is in the constitution", "This is a feature."), ("Sources of revenue are clearly specified", "This is a feature.")], "Fundamental provisions need the consent of both levels.")
M("mcq05", WHAT, "The dual objectives of a federal system are:",
  [("to safeguard unity and accommodate regional diversity", ""), ("to make the centre powerful and states weak", "Both levels have powers."), ("to divide the country and weaken unity", "It promotes unity."), ("to abolish states", "States are a key level.")], "An ideal federation has mutual trust and agreement to live together.")
M("mcq06", WHAT, "Which is a 'coming together' federation?",
  [("Switzerland", ""), ("India", "India is holding together."), ("Spain", "Spain is holding together."), ("Belgium", "Belgium is holding together.")], "The USA, Switzerland and Australia are coming together federations.")
M("mcq07", WHAT, "In a 'holding together' federation:",
  [("the central government tends to be more powerful", ""), ("all states always have equal powers", "Units often have unequal powers."), ("independent states join on their own", "That is coming together."), ("there is only one level of government", "That is unitary.")], "A large country divides its power between the centre and states.")
M("mcq08", IND, "The Constitution declared India as:",
  [("a Union of States", ""), ("a confederation", "It did not use that word."), ("a unitary state", "India follows federal principles."), ("a federation of independent countries", "India is a holding together federation.")], "Though it did not use the word federation, India follows federal principles.")
M("mcq09", IND, "Which subject is on the State List?",
  [("Police", ""), ("Defence", "Union List."), ("Banking", "Union List."), ("Education", "Concurrent List.")], "The State List includes police, trade, commerce, agriculture and irrigation.")
M("mcq10", IND, "Which subject is on the Concurrent List?",
  [("Marriage", ""), ("Foreign affairs", "Union List."), ("Irrigation", "State List."), ("Currency", "Union List.")], "The Concurrent List includes education, forest, trade unions, marriage, adoption and succession.")
M("mcq11", IND, "If a Union law and a State law on a Concurrent List subject conflict:",
  [("the Union law prevails", ""), ("the State law prevails", "The Union law prevails."), ("both laws are cancelled", "The Union law prevails."), ("the local government decides", "Local governments do not decide this.")], "This is laid down in the Constitution.")
M("mcq12", IND, "Who can make laws on 'computer software'?",
  [("the Union Government", ""), ("the State Governments", "Residuary subjects go to the Union."), ("both equally", "It is a residuary subject."), ("panchayats", "Panchayats do not.")], "Computer software is a residuary subject.")
M("mcq13", IND, "Which states enjoy special powers under Article 371?",
  [("Assam, Nagaland, Arunachal Pradesh and Mizoram", ""), ("Punjab, Haryana and Rajasthan", "These are not the NCERT examples."), ("Delhi and Chandigarh", "These are Union Territories."), ("Goa and Kerala", "These are not the NCERT examples.")], "The powers relate to land rights of indigenous peoples, culture and jobs.")
M("mcq14", IND, "Which of these is a Union Territory?",
  [("Lakshadweep", ""), ("Nagaland", "Nagaland is a state."), ("Jharkhand", "Jharkhand is a state."), ("Mizoram", "Mizoram is a state.")], "Chandigarh, Lakshadweep and Delhi are NCERT examples.")
M("mcq15", IND, "To change the division of power between Union and states, the change must be ratified by:",
  [("the legislatures of at least half of the total states", ""), ("all the states", "Half is enough."), ("one-third of the states", "At least half are needed."), ("the Supreme Court", "Courts do not ratify amendments.")], "First a two-thirds majority in both Houses is needed.")
M("mcq16", IND, "Who settles disputes over the division of powers in India?",
  [("the High Courts and the Supreme Court", ""), ("the Prime Minister", "The judiciary decides."), ("the Election Commission", "It conducts elections."), ("the gram sabha", "It is a village body.")], "The courts oversee constitutional provisions.")
M("mcq17", PRAC, "The first major test for democratic politics in India was:",
  [("the creation of linguistic states", ""), ("the 1992 amendment", "That came much later."), ("the coalition era", "That began after 1990."), ("the Bommai judgement", "That was in 1994.")], "Old state boundaries were changed after independence.")
M("mcq18", PRAC, "The formation of linguistic states has:",
  [("made the country more united and administration easier", ""), ("broken up the country", "Fears of disintegration proved wrong."), ("ended all regional demands", "It accommodated them."), ("made Hindi the national language", "India has no national language.")], "Experience showed the fears were wrong.")
M("mcq19", PRAC, "Hindi is the mother tongue of about what share of Indians?",
  [("40 per cent", ""), ("80 per cent", "It is about 40 per cent."), ("25 per cent", "It is about 40 per cent."), ("60 per cent", "It is about 40 per cent.")], "So many safeguards protect other languages.")
M("mcq20", PRAC, "Besides Hindi, how many other languages are Scheduled Languages?",
  [("21", ""), ("14", "That was the original number at independence; now there are 21 besides Hindi."), ("18", "There are 21 besides Hindi."), ("30", "There are 21 besides Hindi.")], "There are 22 Scheduled Languages in all.")
M("mcq21", PRAC, "In which state did the movement for continuing English take a violent form?",
  [("Tamil Nadu", ""), ("Punjab", "It was Tamil Nadu."), ("Gujarat", "It was Tamil Nadu."), ("Assam", "It was Tamil Nadu.")], "The Centre then agreed to continue English along with Hindi.")
M("mcq22", PRAC, "Centre-State relations changed significantly after:",
  [("1990", ""), ("1947", "For long after 1947, one party ruled in most places."), ("1965", "1965 was about English."), ("2009", "The change came after 1990.")], "Regional parties rose and coalition governments began at the Centre.")
M("mcq23", PRAC, "The Supreme Court judgement that made arbitrary dismissal of state governments difficult was in:",
  [("the S.R. Bommai case (1994)", ""), ("the Kesavananda Bharati case (1973)", "That was about the basic structure of the Constitution."), ("the Indira Sawhney case (1992)", "That was about reservations."), ("the Maneka Gandhi case (1978)", "That was about personal liberty.")], "It supported the new culture of respect for state autonomy.")
M("mcq24", DEC, "Decentralisation means:",
  [("taking power from Central and State governments and giving it to local government", ""), ("giving all power to the Centre", "That is centralisation."), ("dividing power among organs of government", "That is horizontal sharing."), ("creating new states", "That is reorganisation.")], "Local government is the third tier.")
M("mcq25", DEC, "Who conducts panchayat and municipal elections?",
  [("the State Election Commission", ""), ("the Election Commission of India", "It conducts Lok Sabha and Assembly elections."), ("the District Collector alone", "An independent commission does it."), ("the gram sabha", "It supervises the panchayat.")], "It was created by the 1992 amendment.")
M("mcq26", DEC, "The members of a gram sabha are:",
  [("all the voters in the village", ""), ("only the ward members", "They form the gram panchayat."), ("the MLAs of the district", "They sit in the zilla parishad."), ("only the sarpanch and officials", "All voters are members.")], "It meets at least twice or thrice a year.")
M("mcq27", DEC, "A group of gram panchayats together forms a:",
  [("panchayat samiti (block or mandal)", ""), ("zilla parishad", "That is all samitis in a district."), ("municipal corporation", "That is urban."), ("gram sabha", "That is all voters of a village.")], "Its members are elected by the panchayat members of the area.")
M("mcq28", DEC, "The political head of a municipal corporation is the:",
  [("mayor", ""), ("sarpanch", "A sarpanch heads a gram panchayat."), ("municipal chairperson", "That is for a municipality."), ("Governor", "The Governor heads the state.")], "Big cities have municipal corporations.")
M("mcq29", DEC, "Which members sit in the zilla parishad besides elected members?",
  [("Lok Sabha MPs and MLAs of that district", ""), ("Supreme Court judges", "They do not."), ("the Prime Minister", "He does not."), ("all the voters of the district", "Only representatives sit in it.")], "Some other officials of district-level bodies are also members.")
M("mcq30", DEC, "A major weakness of local government in India is that:",
  [("gram sabhas are not held regularly and states have not transferred enough powers and resources", ""), ("there is no reservation for women", "At least one-third is reserved."),
   ("elections are not required", "They are mandatory since 1992."), ("there is no election commission", "Each state has a State Election Commission.")], "We are still far from the ideal of self-government.")
# ---------------- True / false ----------------
C.tf("tf1", PRAC, "Hindi is the national language of India.", False, "The Constitution gave no language the status of national language; Hindi is the official language.")
C.tf("tf2", IND, "Residuary subjects are under the jurisdiction of the Union Government.", True, "Computer software is an example.")
C.tf("tf3", WHAT, "In a unitary system, the sub-units are subordinate to the central government.", True, "The centre can pass orders to them.")
C.tf("tf4", DEC, "The 1992 amendment reserved at least one-half of all local government positions for women.", False, "It reserved at least one-third.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", WHAT, "Distinguish between 'coming together' and 'holding together' federations.",
  ["Coming together: independent states come together on their own to form a bigger unit, and the states usually have equal power (USA, Switzerland, Australia).",
   "Holding together: a large country divides its power between the centre and the states; the centre tends to be more powerful and units may have unequal powers (India, Spain, Belgium)."])
W("vsa2", "very_short_answer", IND, "What are residuary subjects? Who legislates on them?",
  ["Subjects that came up after the Constitution was made and are not in the Union, State or Concurrent Lists, such as computer software.", "The Union Government has the power to legislate on them."])
W("vsa3", "very_short_answer", DEC, "What is the gram sabha? What does it do?",
  ["The gram sabha is the body of all the voters in a village.", "It meets at least twice or thrice a year to approve the annual budget of the gram panchayat and review its performance."])
W("sa1", "short_answer", IND, "Describe the three-fold distribution of legislative powers in India.",
  ["Union List: subjects of national importance, such as defence, foreign affairs, banking, communications and currency; only the Union Government makes laws on them.",
   "State List: subjects of state and local importance, such as police, trade, commerce, agriculture and irrigation; only the State Governments make laws on them.",
   "Concurrent List: subjects of common interest, such as education, forest, trade unions, marriage, adoption and succession; both make laws, and the Union law prevails in a conflict. Residuary subjects go to the Union."])
W("sa2", "short_answer", PRAC, "How has India's language policy strengthened federalism?",
  ["The Constitution did not give any one language the status of national language; Hindi is the official language, the mother tongue of about 40 per cent of Indians.",
   "Besides Hindi, 21 other languages are Scheduled Languages; candidates may take Central Government examinations in any of them, and states have their own official languages.",
   "When non-Hindi states protested, especially in Tamil Nadu, English continued along with Hindi after 1965; Hindi is promoted but not imposed, which helped India avoid a Sri Lanka-like situation."])
W("sa3", "short_answer", PRAC, "How did Centre-State relations change after 1990?",
  ["Earlier, the same party ruled at the Centre and in most states, and the Centre often misused the Constitution to dismiss state governments of rival parties.",
   "After 1990, regional parties rose and coalition governments began at the Centre; national parties had to ally with regional parties, creating a new culture of power sharing and respect for state autonomy.",
   "A Supreme Court judgement (S.R. Bommai case, 1994) made it difficult for the Centre to dismiss state governments arbitrarily."])
W("la1", "long_answer", WHAT, "Explain any five key features of federalism.",
  ["There are two or more levels (tiers) of government.",
   "Different tiers govern the same citizens, but each has its own jurisdiction in specific matters of legislation, taxation and administration.",
   "The jurisdictions are specified in the constitution, so the existence and authority of each tier is guaranteed; fundamental provisions cannot be changed unilaterally and need the consent of both levels.",
   "Courts interpret the constitution and the powers of different levels; the highest court acts as an umpire in disputes between levels.",
   "Sources of revenue for each level are clearly specified to ensure financial autonomy; the system aims at both unity and accommodation of regional diversity, through mutual trust and agreement to live together."])
W("la2", "long_answer", DEC, "Describe the steps taken through the 1992 constitutional amendment to strengthen local government, and the structure of panchayati raj.",
  ["It is now constitutionally mandatory to hold regular elections to local bodies, conducted by an independent State Election Commission in each state.",
   "Seats are reserved for SC, ST and OBC, and at least one-third of all positions are reserved for women; state governments must share some powers and revenue with local bodies.",
   "Each village or group of villages has a gram panchayat of ward members (panch) and a sarpanch, directly elected, working under the supervision of the gram sabha of all voters.",
   "A few gram panchayats form a panchayat samiti (block or mandal), whose members are elected by the panchayat members of the area.",
   "All panchayat samitis in a district form the zilla parishad, with elected members, Lok Sabha MPs and MLAs of the district; its chairperson is the political head. In towns there are municipalities, and in big cities municipal corporations headed by a mayor."])
W("cb1", "case_based", DEC, "Read the source and answer the questions.\n\n*\"When power is taken away from Central and State governments and given to local government, it is called decentralisation. The basic idea behind decentralisation is that there are a large number of problems and issues which are best settled at the local level. People have better knowledge of problems in their localities. They also have better ideas on where to spend money and how to manage things more efficiently.\"* (NCERT)\n\n"
  "(i) Define decentralisation. (1)\n\n(ii) Give one reason why problems are best settled at the local level. (1)\n\n(iii) State any two provisions of the 1992 amendment that strengthened local government. (2)",
  ["(i) Taking power away from Central and State governments and giving it to local government.", "(ii) People have better knowledge of problems in their localities and better ideas on where to spend money.",
   "(iii) Any two: regular elections are mandatory; reservation for SC, ST and OBC; at least one-third positions for women; State Election Commission; sharing of powers and revenue by states."])
W("cb2", "case_based", IND, "Read the source and answer the questions.\n\n*\"The Constitution clearly provided a three-fold distribution of legislative powers between the Union Government and the State Governments. Thus, it contains three lists. Union List includes subjects of national importance... State List contains subjects of State and local importance... Concurrent List includes subjects of common interest to both the Union Government as well as the State Governments.\"* (NCERT)\n\n"
  "(i) Name any one subject of the Union List. (1)\n\n(ii) What happens if Union and State laws on a Concurrent List subject conflict? (1)\n\n(iii) How is the division of power between the Union and states protected from easy change? (2)",
  ["(i) Any one: defence, foreign affairs, banking, communications, currency.", "(ii) The law made by the Union Government prevails.",
   "(iii) Parliament cannot change it alone: any change must be passed by both Houses with at least a two-thirds majority and ratified by the legislatures of at least half of the states; courts settle disputes."])
# ---------------- Assertion-reason ----------------
C.arq("ar1", IND, "A state government cannot stop the Union Government from issuing new currency notes.", "Currency is a subject of the Union List.", 0,
      "R explains A.", "only the Union legislates on currency.", "the Union List has subjects of national importance.")
C.arq("ar2", PRAC, "The formation of linguistic states made India more united.", "People who spoke the same language came to live in the same state, making administration easier.", 0,
      "R explains A.", "the fears of disintegration proved wrong.", "this was the basis of linguistic states.")
C.arq("ar3", WHAT, "India is a coming together federation.", "In India, the central government tends to be more powerful than the states.", 3,
      "A is false: India is a holding together federation. R is true.", "India is holding together.", "this is a feature of holding together federations.")
C.arq("ar4", PRAC, "A new culture of power sharing emerged in Indian federalism after 1990.", "Coalition governments at the Centre needed the support of regional parties.", 0,
      "R explains A.", "states gained respect for their autonomy.", "no single party had a majority in the Lok Sabha.")
C.arq("ar5", DEC, "Local government in India has a constitutional status.", "Gram sabhas are not held regularly in many places.", 1,
      "Both are true, but R is a weakness, not the reason for constitutional status.", "the 1992 amendment gave it status.", "this is a real weakness.")
C.arq("ar6", PRAC, "The use of English for official purposes stopped in 1965.", "Many non-Hindi speaking states demanded that the use of English continue.", 3,
      "A is false: English continued along with Hindi. R is true.", "the Centre agreed to continue English.", "this was the demand, especially in Tamil Nadu.")

chapter = header(SUBJ, N, "Federalism", ["what_is_federalism", "india_federal_country", "federalism_in_practice", "decentralisation"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: this chapter is fully in the board examination (Political Science: 20 marks). There is no map item from this chapter; the NCERT map activities (locating states, shading federal countries) are not examined and are left out.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
