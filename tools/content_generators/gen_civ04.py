"""CBSE Class 10 Political Science Ch 4: Political Parties (fully in the 2025-26 board syllabus)."""
import sys
from ss_common import make, header, path, SQP, SHINE, CB

ROOT = sys.argv[1]
SUBJ, N = "civics", 4
PATH = path(SUBJ, "ch04_political_parties")
C = make(SUBJ, N, "civ10ch04")
blk, M, W = C.blk, C.m, C.w
WHY, SYS, NAT, CHAL = ["why_parties"], ["party_systems"], ["national_and_state_parties"], ["challenges_and_reforms"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 4 exercises", "question": n}

SYSTAB = ("| Party system | Meaning | Example |\n|---|---|---|\n| **One-party system** | only one party is allowed to control and run the government; voters have no real choice, so it is not a democratic option | China (Communist Party) |\n"
          "| **Two-party system** | power usually changes between two main parties; others exist but rarely win more than a few seats | USA, United Kingdom |\n"
          "| **Multi-party system** | several parties compete, and more than two have a reasonable chance of coming to power, alone or in alliance | India |")
NATTAB = ("| National party | Founded | Key ideas |\n|---|---|---|\n| **Indian National Congress (INC)** | 1885 | centrist; secularism and welfare of weaker sections and minorities; led the UPA (2004–2014) |\n"
          "| **Bharatiya Janata Party (BJP)** | 1980 (from the Bharatiya Jana Sangh, 1951) | cultural nationalism; 'integral humanism'; leads the NDA; formed the government in 2014, 2019 and 2024 |\n"
          "| **Bahujan Samaj Party (BSP)** | 1984 (Kanshi Ram) | power for the bahujan samaj: dalits, adivasis, OBCs and religious minorities; inspired by Sahu Maharaj, Phule, Periyar and Ambedkar; main base in Uttar Pradesh |\n"
          "| **Communist Party of India (Marxist) (CPI-M)** | 1964 | Marxism-Leninism; socialism, secularism and democracy; opposes imperialism and communalism; strong in Kerala, West Bengal and Tripura |\n"
          "| **Aam Aadmi Party (AAP)** | 2012 | national party since 2023; anti-corruption and governance issues |\n"
          "| **National People's Party (NPP)** | 2013 (P.A. Sangma) | national party since 2019; first party from the North-East with national status; based in Meghalaya |")

sections = [
 {"id": "s1", "title": "Why do we need political parties?", "blocks": [
  blk("s1.hook", "hook", title="An election without parties",
    body="Imagine a Lok Sabha election with 543 seats and no parties. Every candidate is independent. After the result, who becomes Prime Minister? Who promises to bring in a new policy for farmers or students, and who is responsible if it fails?\n\n"
         "Parties solve this problem. They bring people with similar views together, put forward policies, form governments and act as the opposition. This chapter asks what parties do, how many we need, which parties India has, and what is wrong with them today."),
  blk("s1.inspiration", "inspiration", title="Building a party for the voiceless", person="Kanshi Ram", years="1934–2006",
    body="**Kanshi Ram** left a government job in Pune to organise dalit, adivasi and backward class employees. In **1984** he founded the **Bahujan Samaj Party**, which aimed to win political power for the 'bahujan samaj', the majority of people who had been kept away from power.\n\n"
         "Within a decade, the BSP became one of the main parties of Uttar Pradesh. His work shows how a political party can give a voice to people who were left out of decision making.",
    future="This chapter leads to careers in politics, public policy, election management, journalism, political research and law."),
  C.socratic("s1.socratic", "What would most likely happen in a large democracy without political parties?",
    ["No one could promise major policy changes, and no one would be responsible for running the country", "Elections would become more peaceful and simple", "The government would be stronger and more responsible"], 0,
    "Representative democracy cannot work without political parties."),
 ]},
 {"id": "s2", "title": "Meaning and functions of political parties", "blocks": [
  blk("s2.thm", "theory", title="What parties are, what they do and why we need them", revision=True,
    body="**Meaning:** a **political party** is a group of people who come together to **contest elections and hold power** in the government. They agree on some policies and programmes for the society with a view to promote the **collective good**. Since there can be different views on what is good for all, parties try to persuade people why their policies are better than others. They seek to implement these policies by winning popular support through elections.\n"
         "- Parties reflect fundamental political divisions in a society. A party is known by which **part** of society it stands for, which policies it supports and whose interests it upholds.\n"
         "- **Partisanship:** a party is about a part of society, and thus involves partisanship: an inclination to take a side and an inability to take a balanced view.\n"
         "- **Three components of a party:** the **leaders**, the **active members** and the **followers**.\n\n"
         "**Functions of political parties:**\n"
         "1. **Contest elections:** in most democracies, elections are fought mainly among candidates put up by political parties. In some countries such as the **USA**, members and supporters of a party choose its candidates; in **India**, top party leaders choose candidates.\n"
         "2. **Put forward policies and programmes:** parties put forward different policies and programmes, and voters choose from them. Parties reduce a vast number of opinions into a few basic positions that they support. A government is expected to base its policies on the line taken by the ruling party.\n"
         "3. **Make laws:** laws are debated and passed in the legislature. Since most members of the legislature belong to a party, they go by the direction of the party leadership, irrespective of their personal opinions.\n"
         "4. **Form and run governments:** parties recruit leaders, train them and then make them ministers to run the government in the way they want. The big policy decisions are taken by the political executive, which comes from the parties.\n"
         "5. **Play the role of opposition:** parties that lose elections play the role of opposition to the parties in power, by voicing different views and criticising the government for its failures or wrong policies. Opposition parties also mobilise opposition to the government.\n"
         "6. **Shape public opinion:** parties raise and highlight issues. They have lakhs of members and activists spread all over the country. Many of the pressure groups are extensions of political parties among different sections of society. Parties sometimes also launch movements for the resolution of problems faced by people.\n"
         "7. **Provide access to government machinery and welfare schemes:** for an ordinary citizen, it is easier to approach a local party leader than a government officer. Parties have to be responsive to people's needs and demands; otherwise people can reject them in the next election.\n\n"
         "**Necessity of political parties:** we need parties because they perform all these functions. Imagine a situation without parties:\n"
         "- Every candidate in the elections would be **independent**. No one would be able to make any promises to the people about major policy changes.\n"
         "- The government may be formed, but its utility would remain uncertain. Elected representatives would be accountable to their constituency for what they do in the locality, but **no one would be responsible for how the country is run**.\n"
         "- We can see this in the **non-party based elections to panchayats** in many states: although parties do not contest formally, the village often splits into factions, each putting up a 'panel' of candidates.\n"
         "- The rise of political parties is directly linked to the emergence of **representative democracies**. As societies became large and complex, they needed some agency to gather different views on various issues and present these to the government. That is why almost all countries of the world have political parties."),
  C.kc("s2.check", "What are the three components of a political party?",
    [("leaders, active members and followers", ""), ("voters, judges and ministers", "These are not party components."), ("President, Prime Minister and Speaker", "These are offices of state."), ("candidates, the Election Commission and the press", "The Election Commission is not part of a party.")],
    "A party has leaders, active members and followers."),
  C.kc("s2.check2", "In India, who chooses the candidates of a party for elections?",
    [("top party leaders", ""), ("all members and supporters of the party", "That happens in the USA."), ("the Election Commission", "It only conducts elections."), ("the President", "The President has no such role.")],
    "In the USA, members and supporters choose candidates; in India, top leaders do."),
 ]},
 {"id": "s3", "title": "How many parties should we have?", "blocks": [
  blk("s3.thm", "theory", title="Party systems and alliances", revision=True,
    body="In a democracy, any group of citizens is free to form a political party. In India, more than **750 parties** are registered with the Election Commission. But not all of these are serious contenders in elections. So the question is not how many parties exist, but how many are effective.\n\n"
         "**One-party system:** in some countries, only one party is allowed to control and run the government. In **China**, only the **Communist Party** is allowed to rule. Although, legally speaking, people are free to form political parties, the electoral system does not permit free competition for power. A one-party system is **not a good option** because it is not a democratic option: any democratic system must allow at least two parties to compete in elections and provide a fair chance for the competing parties to come to power.\n\n"
         "**Two-party system:** in some countries, power usually changes between two main parties. Several other parties may exist, contest elections and win a few seats, but only the two main parties have a serious chance of winning a majority and forming the government. The **United States of America** and the **United Kingdom** are examples.\n\n"
         "**Multi-party system:** when several parties compete for power, and more than two parties have a reasonable chance of coming to power either on their own strength or in alliance with others. **India** has a multi-party system.\n"
         "- **Alliance or front:** when several parties in a multi-party system join hands for the purpose of contesting elections and winning power. In India, there were three major alliances in the **2004** parliamentary elections: the **National Democratic Alliance (NDA)**, the **United Progressive Alliance (UPA)** and the **Left Front**.\n"
         "- A multi-party system often appears very messy and can lead to political instability, but it allows a variety of interests and opinions to enjoy political representation.\n\n"
         "**Which system is best?** There is no simple answer. A party system is not something a country can choose. It evolves over a long time, depending on the **nature of society**, its **social and regional divisions**, its **history of politics** and its **system of elections**. Each country develops a party system conditioned by its special circumstances. India evolved a multi-party system because its social and geographical diversity is not easily absorbed by two or even three parties."),
  blk("s3.table", "markdown_table", title="Party systems compared", revision=True, body=SYSTAB),
  C.kc("s3.check", "Why is a one-party system not a good option?",
    [("It is not a democratic option, as voters have no real choice", ""), ("It leads to too many coalitions", "Coalitions belong to multi-party systems."),
     ("It makes elections too expensive", "That is not the main reason."), ("It allows too many parties to win seats", "Only one party rules.")],
    "Democracy needs at least two parties competing fairly for power."),
  C.kc("s3.check2", "Why does India have a multi-party system?",
    [("Its social and geographical diversity is not easily absorbed by two or three parties", ""), ("The Constitution allows only many parties", "The Constitution does not fix the number."),
     ("The Election Commission chose it", "A party system evolves; it is not chosen."), ("Two-party systems are illegal in India", "There is no such law.")],
    "A party system evolves with a country's society, divisions, history and elections."),
 ]},
 {"id": "s4", "title": "National and state parties", "blocks": [
  blk("s4.thm", "theory", title="Recognised parties in India", revision=True,
    body="Democracies that follow a federal system all over the world tend to have two kinds of parties: parties present in only one of the federal units, and parties present in several or all units of the federation. India is no exception.\n\n"
         "**Recognition by the Election Commission:** every party in the country has to **register** with the Election Commission. While the Commission treats all parties equally, it offers some special facilities to large and established parties. These parties are given a **unique symbol**: only the official candidates of that party can use that election symbol. Parties that get this privilege and some other special facilities are **'recognised'** by the Election Commission.\n"
         "- **State party:** a party that secures at least **six per cent** of the total votes in an election to the **Legislative Assembly** of a state and wins at least **two seats**.\n"
         "- **National party:** a party that secures at least **six per cent** of the total votes in **Lok Sabha** elections or Assembly elections in **four states**, and wins at least **four seats** in the Lok Sabha.\n\n"
         "**National parties (as recognised by the Election Commission since 2023):** the NCERT book lists the parties recognised when it was printed; the Commission's list in 2023 had **six** national parties:\n"
         "- **Indian National Congress (INC):** founded in **1885**; it has split many times. It played a dominant role in Indian politics for several decades after independence. A **centrist** party in its ideological orientation, it espouses **secularism** and the **welfare of weaker sections and minorities**. It led the **United Progressive Alliance (UPA)** government from **2004 to 2014**.\n"
         "- **Bharatiya Janata Party (BJP):** founded in **1980** by reviving the **Bharatiya Jana Sangh**, formed by **Syama Prasad Mukherjee** in **1951**. It wants to build a strong and modern India by drawing inspiration from India's ancient culture and values; **cultural nationalism (Hindutva)** is an important element of its conception of Indian nationhood, and Deendayal Upadhyaya's ideas of **'integral humanism'** guide it. It leads the **National Democratic Alliance (NDA)** and formed the government at the Centre after the **2014, 2019 and 2024** elections.\n"
         "- **Bahujan Samaj Party (BSP):** formed in **1984** under the leadership of **Kanshi Ram**. It seeks to represent and secure power for the **bahujan samaj**, which includes the **dalits, adivasis, OBCs and religious minorities**. It draws inspiration from the ideas and teachings of **Sahu Maharaj, Mahatma Phule, Periyar Ramaswami Naicker and Babasaheb Ambedkar**. Its main base is in **Uttar Pradesh**.\n"
         "- **Communist Party of India (Marxist) (CPI-M):** founded in **1964**. It believes in **Marxism-Leninism**, supports **socialism, secularism and democracy**, and opposes **imperialism and communalism**. It enjoys strong support in **West Bengal, Kerala and Tripura**.\n"
         "- **Aam Aadmi Party (AAP):** founded in **2012**; recognised as a national party in **2023**.\n"
         "- **National People's Party (NPP):** founded in **2013** by **P.A. Sangma**; recognised as a national party in **2019**, the first party from the **North-East** to get this status.\n\n"
         "**State parties:** other than these, most of the major parties are classified as **'state parties'**, commonly called regional parties. Some of them are all-India parties that happen to have succeeded only in some states. Parties like the **Biju Janata Dal, Sikkim Democratic Front, Mizo National Front** and **Telugu Desam Party** are conscious about their state identity.\n"
         "- Over the last three decades, the number and strength of these parties has expanded. This made the **Parliament of India more diverse** politically.\n"
         "- No one national party was able to secure a majority in the Lok Sabha on its own from **1989 until 2014**. As a result, national parties were compelled to form alliances with state parties. Since 1996, nearly every one of the state parties has got an opportunity to be part of one or the other **national-level coalition government**. This has contributed to the **strengthening of federalism and democracy** in our country."),
  blk("s4.table", "markdown_table", title="National parties of India", revision=True, body=NATTAB),
  C.kc("s4.check", "To be recognised as a state party, a party must win at least:",
    [("6% of the votes in a state Assembly election and 2 seats", ""), ("6% of the votes in Lok Sabha elections and 4 Lok Sabha seats", "That is part of the condition for a national party."),
     ("50% of the votes in the state", "The threshold is much lower."), ("one seat in any election", "It needs 6% of votes and 2 seats.")],
    "Recognised parties get a unique election symbol."),
  C.kc("s4.check2", "Which party was founded by Kanshi Ram in 1984?",
    [("Bahujan Samaj Party", ""), ("Bharatiya Janata Party", "It was founded in 1980."), ("Communist Party of India (Marxist)", "It was founded in 1964."), ("National People's Party", "It was founded by P.A. Sangma in 2013.")],
    "The BSP represents the bahujan samaj."),
 ]},
 {"id": "s5", "title": "Challenges to political parties and reforms", "blocks": [
  blk("s5.thm", "theory", title="What is wrong with parties, and how can they be reformed?", revision=True,
    body="Since parties are the most visible face of democracy, people blame parties for whatever is wrong with the working of democracy. Popular dissatisfaction and criticism has focused on **four problem areas**:\n\n"
         "1. **Lack of internal democracy:** all over the world, there is a tendency for parties to concentrate power in **one or a few leaders** at the top. Parties do not keep **membership registers**, do not hold **organisational meetings**, and do not conduct **internal elections** regularly. Ordinary members do not get sufficient information about what happens inside the party, and do not have the means or connections needed to influence decisions. Leaders assume greater power to make decisions in the name of the party. Those who disagree with the leadership find it difficult to continue in the party. More than loyalty to party principles and policies, **personal loyalty to the leader** becomes more important.\n"
         "2. **Dynastic succession:** since most parties do not practise open and transparent procedures, there are very few ways for an ordinary worker to rise to the top. Those who happen to be the leaders are in a position of unfair advantage to favour people close to them or even their family members. In many parties, the **top positions are always controlled by members of one family**. This is unfair to other members and bad for democracy, since people who do not have adequate experience or popular support come to occupy positions of power. This tendency is present in some measure all over the world, including in some older democracies.\n"
         "3. **Money and muscle power:** since parties are focused only on winning elections, they tend to use short-cuts. They nominate candidates who have or can raise **lots of money**. Rich people and companies who give funds to parties tend to influence their policies and decisions. In some cases, parties support **criminals** who can win elections. Democrats all over the world are worried about the increasing role of rich people and big companies in democratic politics.\n"
         "4. **Lack of meaningful choice:** in order to offer meaningful choice, parties must be significantly different. In recent years, there has been a decline in the **ideological differences** among parties in most parts of the world. In our country too, the differences among major parties on economic issues have reduced. Those who want really different policies have no option available to them. Sometimes people cannot even elect very different leaders, because the same set of leaders keep shifting from one party to another.\n\n"
         "**Steps already taken to reform parties:**\n"
         "- **Anti-defection law:** **defection** means changing party allegiance from the party on which a person got elected to a different party. Many MLAs and MPs were indulging in defection to become ministers or for cash rewards. The Constitution was amended (**52nd Amendment, 1985**) so that if an MLA or MP changes parties, he or she will **lose the seat** in the legislature. This has helped bring defection down, but it has made dissent even more difficult: MPs and MLAs have to accept whatever the party leaders decide.\n"
         "- **Affidavit:** the **Supreme Court** passed an order (**2003**) to reduce the influence of money and criminals. Now it is mandatory for every candidate who contests elections to file an **affidavit** giving details of their **property and criminal cases** pending against them. This information is made public. But there is no system of check on whether the information is true.\n"
         "- **Election Commission order:** the Election Commission passed an order making it necessary for political parties to hold their **organisational elections** and file their **income tax returns**. Parties have started doing so, but sometimes it is a mere formality.\n\n"
         "**Suggestions for further reform:**\n"
         "- A **law to regulate the internal affairs** of political parties: to maintain a register of members, follow their own constitution, have an independent authority to act as a judge in case of party disputes, and hold open elections to the highest posts.\n"
         "- Make it mandatory for parties to give a minimum number of tickets, about **one-third, to women** candidates; similarly, there should be a quota for women in the decision-making bodies of the party.\n"
         "- **State funding of elections:** the government should give parties money to support their election expenses, in kind (petrol, paper, telephone and so on) or in cash, on the basis of votes secured in the last election.\n\n"
         "Legal reforms need care: over-regulation can be counter-productive, and parties may find ways to cheat the law. Two other ways are important: **people can put pressure** on parties through petitions, publicity and agitations, and through the media and movements; and **people who want reform can join parties** themselves, since the quality of democracy depends on the degree of public participation."),
  C.kc("s5.check", "A law that makes an MP or MLA lose the seat for changing parties is the:",
    [("anti-defection law", ""), ("affidavit rule", "The affidavit is about property and criminal cases."), ("state funding law", "That is a suggested reform about election expenses."), ("organisational election order", "That is an Election Commission order for internal elections.")],
    "The Constitution was amended in 1985 to stop defection."),
  C.kc("s5.check2", "Which is a challenge to political parties in India?",
    [("dynastic succession", ""), ("too many internal elections", "The problem is too few internal elections."), ("too much ideological difference", "The problem is a decline in ideological differences."), ("too much transparency", "The problem is lack of transparency.")],
    "Top positions are often controlled by members of one family."),
 ]},
 {"id": "s6", "title": "Remember, avoid, practise", "blocks": [
  blk("s6.memory", "memory_trick", title="Memory tricks",
    body="- **Functions: \"CPL-FOSA\"**: Contest elections, Policies, Laws, Form government, Opposition, Shape opinion, Access to schemes.\n- **Components: \"LAF\"**: Leaders, Active members, Followers.\n"
         "- **Party systems: China = 1, USA/UK = 2, India = many.**\n- **Recognition: \"6% + 2 seats\" (state); \"6% in Lok Sabha or 4 states + 4 Lok Sabha seats\" (national).**\n"
         "- **National parties and years: \"INC 1885, CPI-M 1964, BJP 1980, BSP 1984, AAP 2012, NPP 2013\".**\n- **Challenges: \"I-D-M-C\"**: Internal democracy, Dynastic succession, Money and muscle, Choice.\n"
         "- **Reforms already taken: \"Defection 1985, Affidavit 2003, Elections and tax returns (EC)\".**"),
  blk("s6.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying China has no parties: it has a **one-party** system (Communist Party).\n2. Saying India has a two-party system: India has a **multi-party** system.\n"
         "3. Saying the Election Commission decides which party system India has: party systems **evolve** with society, divisions, history and elections.\n"
         "4. Mixing up the recognition rules: a **state** party needs 6% of Assembly votes and **2 seats**; a **national** party needs 6% in Lok Sabha or 4 states and **4 Lok Sabha seats**.\n"
         "5. Saying the anti-defection law increased dissent: it reduced defection but made **dissent more difficult**.\n6. Writing that the affidavit order came from Parliament: it came from the **Supreme Court**."),
  blk("s6.tip", "teacher_tip", title="Try this in class",
    body="Collect the election symbols of the national parties and two state parties of your state. Ask groups to find out the party's founding year, its main ideas and whether it is national or state, and present a one-minute 'party profile'."),
  blk("s6.reflection", "reflection", title="Think and explain",
    body="If you joined a political party, which one challenge from this chapter would you most want to fix first, and how?"),
  blk("s6.connection", "connection", title="Where this leads",
    body="- **Chapter 1 (Power-sharing):** sharing power among parties and coalitions.\n- **Chapter 2 (Federalism):** regional parties and coalition governments after 1990.\n"
         "- **Chapter 5 (Outcomes of Democracy):** accountable and responsive government."),
  blk("s6.mastery", "mastery", title="Mastery challenge",
    body="'Lack of internal democracy and dynastic succession are major challenges to political parties.' Explain in about 120 words.\n\n"
         "**Model answer:** Political parties tend to concentrate power in one or a few leaders at the top. They do not keep membership registers, hold organisational meetings or conduct regular internal elections, so ordinary members have little information or influence, and those who disagree find it hard to stay. "
         "Personal loyalty to the leader becomes more important than loyalty to party principles. Because parties lack open and transparent procedures, there are very few ways for an ordinary worker to rise to the top. "
         "Leaders favour people close to them or their family members, and in many parties the top posts are always held by one family. This is unfair to other members and bad for democracy, as people without adequate experience or popular support come to occupy positions of power."),
  blk("s6.summary", "summary", title="Chapter summary",
    body="- A political party is a group of people who come together to contest elections and hold power; it has leaders, active members and followers.\n"
         "- Parties contest elections, put forward policies, make laws, form governments, act as opposition, shape opinion and give access to government schemes.\n"
         "- Party systems: one-party (China), two-party (USA, UK), multi-party (India); party systems evolve, they are not chosen.\n"
         "- The Election Commission recognises state and national parties (6% votes plus seats) and gives them unique symbols.\n"
         "- Challenges: lack of internal democracy, dynastic succession, money and muscle power, lack of meaningful choice.\n"
         "- Reforms: anti-defection law, affidavits on property and criminal cases, organisational elections and tax returns; suggestions include regulating internal affairs, tickets for women and state funding."),
  blk("s6.examtips", "exam_tips", title="Board exam tips",
    body="- The 2025-26 sample paper had a 5-mark question with a choice: explain the significant role of parties in democracy (functions), or analyse how leadership succession is a challenge to parties in India (dynastic succession).\n"
         "- 3/5-mark favourites: functions, necessity of parties, party systems, national party profiles, challenges and reforms.\n"
         "- In 5-mark answers, write five separate points with a heading for each."),
  blk("s6.flash1", "flashcard", front="What is a political party?", back="A group of people who come together to contest elections and hold power in the government, agreeing on policies to promote the collective good."),
  blk("s6.flash2", "flashcard", front="What is defection?", back="Changing party allegiance from the party on which a person got elected to a different party."),
  blk("s6.flash3", "flashcard", front="What is an alliance or front?", back="When several parties in a multi-party system join hands to contest elections and win power, such as the NDA and UPA."),
  blk("s6.flash4", "flashcard", front="Name the four challenges to political parties.", back="Lack of internal democracy; dynastic succession; growing role of money and muscle power; lack of meaningful choice."),
 ]},
]

# ---------------- Sample paper ----------------
W("sqp27a", "long_answer", WHY, "'Political parties play a significant role in the effective working of a democracy.' Explain.",
  ["Parties contest elections: elections are fought mainly among candidates put up by parties; in India, top party leaders choose the candidates.",
   "Parties put forward different policies and programmes, grouping similar opinions together to give a direction for government policies.",
   "Parties make laws: laws are debated and passed in the legislature, where most members follow their party's direction.",
   "Parties that lose elections play the role of opposition, criticising the government for its failures or wrong policies; parties also shape public opinion by raising issues, and many pressure groups are their extensions.",
   "Parties provide people access to government machinery and welfare schemes: it is easier for an ordinary citizen to approach a local party leader than a government officer."], source=SQP("27A"))
W("sqp27b", "long_answer", CHAL, "Analyse how the issue of leadership succession poses a challenge to political parties in India.",
  ["Most political parties do not practise open and transparent procedures for their functioning, so there are very few ways for an ordinary worker to rise to the top.",
   "Those who happen to be the leaders are in a position of unfair advantage to favour people close to them or even their family members.",
   "In many parties there is a trend of dynastic succession: top positions are always controlled by members of one family, which is unfair to other members and bad for democracy.",
   "People who do not have adequate experience or popular support come to occupy positions of power.",
   "Personal loyalty to the leader becomes more important than loyalty to party principles and policies; this tendency is seen all over the world, even in older democracies."], source=SQP("27B"))

# ---------------- NCERT exercises ----------------
W("ex1", "long_answer", WHY, "State the various functions political parties perform in a democracy.",
  ["Contest elections, with candidates chosen by party leaders (in India) or by members and supporters (in the USA).",
   "Put forward policies and programmes, reducing many opinions to a few basic positions for voters to choose from.",
   "Make laws in the legislature, and form and run governments by recruiting and training leaders who become ministers.",
   "Play the role of opposition by criticising the government and mobilising opposition, and shape public opinion by raising issues and launching movements.",
   "Provide access to government machinery and welfare schemes, since local party leaders are easier to approach than officials."], source=ex("1"))
W("ex2", "long_answer", CHAL, "What are the various challenges faced by political parties?",
  ["Lack of internal democracy: power is concentrated in one or a few leaders; parties do not keep membership registers, hold meetings or conduct internal elections.",
   "Ordinary members have little information or influence, and personal loyalty to the leader matters more than party principles.",
   "Dynastic succession: top positions are controlled by members of one family, so people without experience or popular support get power.",
   "Growing role of money and muscle power: parties nominate rich candidates, rich donors influence policies, and some parties support criminals who can win.",
   "Lack of meaningful choice: ideological differences among parties have declined, and the same leaders keep shifting from one party to another."], source=ex("2"))
W("ex3", "short_answer", CHAL, "Suggest some reforms to strengthen parties so that they perform their functions well.",
  ["A law to regulate the internal affairs of parties: a register of members, following the party constitution, an independent authority for disputes, and open elections to the highest posts.",
   "Make it mandatory for parties to give about one-third of tickets to women, with a quota for women in party decision-making bodies; and state funding of elections, in kind or cash, based on votes secured.",
   "People should put pressure on parties through petitions, publicity, agitations, the media and movements, and those who want reform should join parties themselves."], source=ex("3"))
W("ex4", "very_short_answer", WHY, "What is a political party?",
  ["A political party is a group of people who come together to contest elections and hold power in the government.",
   "They agree on some policies and programmes for the society with a view to promote the collective good, and try to win popular support for them."], source=ex("4"))
W("ex5", "short_answer", WHY, "What are the characteristics of a political party?",
  ["It is a group of people who come together to contest elections and hold power in the government.",
   "Its members agree on some policies and programmes to promote the collective good, and it tries to persuade people that its policies are better.",
   "It reflects a part of society and involves partisanship, and it has three components: leaders, active members and followers."], source=ex("5"))
M("ex6", WHY, "A group of people who come together to contest elections and hold power in the government is called a:",
  [("political party", ""), ("pressure group", "Pressure groups influence the government but do not contest elections to hold power."), ("movement", "Movements usually do not contest elections."), ("coalition government", "A coalition is an alliance of parties in government.")],
  "This is the NCERT definition of a political party.", "easy", ex("6"), correct=0)
M("ex7", SYS, "Match: (1) Congress Party, (2) Bharatiya Janata Party, (3) Communist Party of India (Marxist), (4) Telugu Desam Party, with (A) National Democratic Alliance, (B) State party, (C) United Progressive Alliance, (D) Left Front. The correct order for 1, 2, 3, 4 is:",
  [("C A D B", ""), ("C D A B", "The BJP leads the NDA, not the Left Front."), ("A C D B", "The Congress led the UPA."), ("D C A B", "The Congress led the UPA, and the CPI(M) is in the Left Front.")],
  "1-C, 2-A, 3-D, 4-B.", "medium", ex("7"), correct=0)
M("ex8", NAT, "Who among the following is the founder of the Bahujan Samaj Party?",
  [("Kanshi Ram", ""), ("Sahu Maharaj", "The BSP draws inspiration from him, but he did not found it."), ("B.R. Ambedkar", "The BSP draws inspiration from him, but he did not found it."), ("Jotiba Phule", "The BSP draws inspiration from him, but he did not found it.")],
  "Kanshi Ram founded the BSP in 1984.", "easy", ex("8"), correct=0)
M("ex9", NAT, "What is the guiding philosophy of the Bharatiya Janata Party?",
  [("Integral humanism", ""), ("Bahujan samaj", "That is the BSP."), ("Revolutionary democracy", "That is linked to communist parties."), ("Modernity", "This is not the BJP's stated philosophy.")],
  "Deendayal Upadhyaya's ideas of integral humanism guide the BJP.", "easy", ex("9"), correct=0)
M("ex10", CHAL, "Consider the statements: A. Political parties do not enjoy much trust among the people. B. Parties are often rocked by scandals involving top party leaders. C. Parties are not necessary to run governments. Which statements are correct?",
  [("A and B", ""), ("A, B and C", "C is wrong: parties are necessary to run governments."), ("B and C", "C is wrong."), ("A and C", "C is wrong.")],
  "Parties are necessary, even though people distrust them.", "medium", ex("10"), correct=0)

# ---------------- MCQs ----------------
M("mcq01", WHY, "'Partisanship' means:",
  [("an inclination to take a side and an inability to take a balanced view", ""), ("being a member of a party", "That is party membership."), ("sharing power between parties", "That is a coalition."), ("changing parties after an election", "That is defection.")], "A party stands for a part of society.")
M("mcq02", WHY, "In the USA, the candidates of a party are chosen by:",
  [("members and supporters of the party", ""), ("top party leaders", "That is the practice in India."), ("the President", "The President does not choose them."), ("the Supreme Court", "Courts do not choose candidates.")], "This makes the process more open.")
M("mcq03", WHY, "Which function of parties helps an ordinary citizen get a ration card or a pension?",
  [("providing access to government machinery and welfare schemes", ""), ("making laws", "That happens in the legislature."), ("playing the role of opposition", "That is criticising the government."), ("contesting elections", "That is about winning power.")], "A local party leader is easier to approach than an officer.")
M("mcq04", WHY, "Parties that lose elections:",
  [("play the role of opposition", ""), ("are dissolved", "They continue to exist."), ("join the judiciary", "Parties have no role in the judiciary."), ("must join the ruling party", "They are free to oppose.")], "They criticise the government for failures or wrong policies.")
M("mcq05", WHY, "Many pressure groups are:",
  [("extensions of political parties among different sections of society", ""), ("part of the Election Commission", "They are not."), ("government departments", "They are not."), ("courts", "They are not.")], "This is how parties shape public opinion.")
M("mcq06", WHY, "Without political parties:",
  [("no one would be responsible for how the country is run", ""), ("elections would not be needed", "Elections would still be held."), ("the Prime Minister would be stronger", "There would be no clear majority."), ("every voter would agree", "Opinions would still differ.")], "Every candidate would be independent.")
M("mcq07", WHY, "The rise of political parties is directly linked to the emergence of:",
  [("representative democracies", ""), ("monarchies", "Parties grew with representative democracy."), ("military rule", "Parties grew with representative democracy."), ("colonial empires", "Parties grew with representative democracy.")], "Large societies needed an agency to gather views.")
M("mcq08", WHY, "Elections are held without political parties in:",
  [("panchayats in many states", ""), ("the Lok Sabha", "Parties contest Lok Sabha elections."), ("state Assemblies", "Parties contest Assembly elections."), ("municipal corporations everywhere", "Parties often contest these.")], "Even there, villages split into factions with 'panels'.")
M("mcq09", SYS, "Which country has a one-party system?",
  [("China", ""), ("India", "India has a multi-party system."), ("USA", "The USA has a two-party system."), ("United Kingdom", "The UK has a two-party system.")], "Only the Communist Party is allowed to rule.")
M("mcq10", SYS, "Which countries are examples of a two-party system?",
  [("USA and United Kingdom", ""), ("India and Sri Lanka", "India is multi-party."), ("China and North Korea", "China is one-party."), ("Belgium and Switzerland", "These are multi-party.")], "Power usually changes between two main parties.")
M("mcq11", SYS, "Roughly how many parties are registered with the Election Commission of India?",
  [("more than 750", ""), ("about 10", "There are far more."), ("exactly 6", "6 is the number of national parties."), ("about 50", "There are far more.")], "But only a few are serious contenders.")
M("mcq12", SYS, "Which three alliances contested the 2004 Lok Sabha election?",
  [("NDA, UPA and Left Front", ""), ("NDA, BSP and AAP", "BSP and AAP are parties, not alliances."), ("UPA, INC and BJP", "INC and BJP are parties."), ("Left Front, CPI(M) and NPP", "CPI(M) and NPP are parties.")], "An alliance is formed when parties join hands to win power.")
M("mcq13", SYS, "A party system develops according to:",
  [("the nature of society, its divisions, history of politics and system of elections", ""), ("the order of the Election Commission", "It evolves; it is not ordered."),
   ("the choice of the Prime Minister", "It is not chosen."), ("the size of the army", "This has no link.")], "Each country develops a party system for its special circumstances.")
M("mcq14", SYS, "A multi-party system can lead to political instability, but it:",
  [("allows a variety of interests and opinions to be represented", ""), ("always produces one-party rule", "It does not."), ("removes the need for elections", "Elections remain."), ("stops all coalitions", "It often leads to coalitions.")], "India's diversity needs many parties.")
M("mcq15", NAT, "What does the Election Commission give to recognised parties?",
  [("a unique election symbol", ""), ("seats in Parliament", "Seats must be won in elections."), ("government funding for all expenses", "There is no such full funding."), ("the power to make laws", "Only legislatures make laws.")], "Only the party's official candidates can use that symbol.")
M("mcq16", NAT, "A national party must win at least how many Lok Sabha seats?",
  [("four", ""), ("two", "Two Assembly seats is for a state party."), ("ten", "It is four."), ("one", "It is four.")], "It also needs 6% of the votes in Lok Sabha or Assembly elections in four states.")
M("mcq17", NAT, "The Indian National Congress was founded in:",
  [("1885", ""), ("1947", "That is the year of independence."), ("1964", "That is the CPI(M)."), ("1980", "That is the BJP.")], "It is a centrist party.")
M("mcq18", NAT, "The Bharatiya Jana Sangh was formed in 1951 by:",
  [("Syama Prasad Mukherjee", ""), ("Kanshi Ram", "He founded the BSP."), ("P.A. Sangma", "He founded the NPP."), ("Deendayal Upadhyaya", "He gave the idea of integral humanism.")], "The BJP was formed in 1980 by reviving the Jana Sangh.")
M("mcq19", NAT, "The CPI(M) enjoys strong support in:",
  [("West Bengal, Kerala and Tripura", ""), ("Uttar Pradesh and Bihar", "That is not its main base."), ("Gujarat and Rajasthan", "That is not its main base."), ("Meghalaya and Nagaland", "That is the NPP's region.")], "It was founded in 1964.")
M("mcq20", NAT, "The Bahujan Samaj Party draws inspiration from:",
  [("Sahu Maharaj, Mahatma Phule, Periyar and Ambedkar", ""), ("Marx and Lenin", "That is the CPI(M)."), ("Syama Prasad Mukherjee", "That is linked to the BJP."), ("Dadabhai Naoroji", "He is not mentioned for the BSP.")], "It represents the bahujan samaj.")
M("mcq21", NAT, "The first party from the North-East to be recognised as a national party is the:",
  [("National People's Party", ""), ("Mizo National Front", "It is a state party."), ("Sikkim Democratic Front", "It is a state party."), ("Aam Aadmi Party", "It is based in Delhi and Punjab.")], "It was recognised in 2019.")
M("mcq22", NAT, "Which is a state party conscious of its state identity?",
  [("Biju Janata Dal", ""), ("Indian National Congress", "It is a national party."), ("Bharatiya Janata Party", "It is a national party."), ("Bahujan Samaj Party", "It is a national party.")], "Others include the Sikkim Democratic Front and the Mizo National Front.")
M("mcq23", NAT, "The growth of state parties has:",
  [("made Parliament more diverse and strengthened federalism", ""), ("ended coalition governments", "It increased coalitions."), ("weakened democracy", "It strengthened democracy."), ("reduced the number of parties", "It increased them.")], "State parties joined national coalitions.")
M("mcq24", CHAL, "Which is NOT a sign of lack of internal democracy in parties?",
  [("holding regular, open elections to party posts", ""), ("no membership registers", "This is a sign of it."), ("no organisational meetings", "This is a sign of it."), ("power concentrated in one leader", "This is a sign of it.")], "Regular internal elections are a sign of internal democracy.")
M("mcq25", CHAL, "When rich people and companies fund parties, they tend to:",
  [("influence the policies and decisions of the party", ""), ("reduce the role of money", "They increase it."), ("make parties more transparent", "Not necessarily."), ("stop criminals from contesting", "They do not.")], "This is the challenge of money and muscle power.")
M("mcq26", CHAL, "The lack of meaningful choice arises because:",
  [("ideological differences among parties have declined", ""), ("there are too few parties", "India has many parties."), ("voters do not vote", "Voters do vote."), ("parties have very different economic policies", "The differences have reduced.")], "The same leaders also shift between parties.")
M("mcq27", CHAL, "The anti-defection law has:",
  [("reduced defection but made dissent more difficult", ""), ("increased defection", "It reduced defection."), ("removed party leaders' power", "Leaders became more powerful."), ("banned all parties", "It did not.")], "MPs and MLAs must accept what party leaders decide.")
M("mcq28", CHAL, "Which body ordered that candidates file affidavits on their property and criminal cases?",
  [("the Supreme Court", ""), ("the Election Commission", "The Commission ordered internal elections and tax returns."), ("Parliament", "It came from a court order."), ("the President", "It came from a court order.")], "The information is made public.")
M("mcq29", CHAL, "The Election Commission has made it necessary for parties to:",
  [("hold organisational elections and file income tax returns", ""), ("give one-third tickets to women", "That is a suggestion, not yet a rule."), ("receive state funding", "That is a suggestion."), ("merge with national parties", "There is no such rule.")], "Sometimes this is a mere formality.")
M("mcq30", CHAL, "Which is a suggested reform for political parties?",
  [("state funding of elections", ""), ("abolishing elections", "That would end democracy."), ("allowing only one party", "That is not democratic."), ("banning women candidates", "The suggestion is to give women more tickets.")], "Money would be given in kind or cash based on votes secured.")
# ---------------- True / false ----------------
C.tf("tf1", SYS, "India has a two-party system.", False, "India has a multi-party system.")
C.tf("tf2", NAT, "Recognised parties are given a unique election symbol.", True, "Only the official candidates of that party can use it.")
C.tf("tf3", CHAL, "The anti-defection law makes an MP or MLA lose the seat for changing parties.", True, "It was brought in by a constitutional amendment in 1985.")
C.tf("tf4", WHY, "Political parties are not needed to run governments.", False, "Parties form and run governments; without them, no one would be responsible for running the country.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", SYS, "What is an alliance or front? Give an example.",
  ["When several parties in a multi-party system join hands to contest elections and win power, they form an alliance or front.", "Example: the NDA, the UPA and the Left Front in the 2004 elections."])
W("vsa2", "very_short_answer", NAT, "How does the Election Commission recognise a state party and a national party?",
  ["State party: at least 6% of the votes in a state Assembly election and at least 2 seats.", "National party: at least 6% of the votes in Lok Sabha elections or Assembly elections in four states, and at least 4 Lok Sabha seats."])
W("vsa3", "very_short_answer", CHAL, "What is defection? How was it checked?",
  ["Defection is changing party allegiance from the party on which a person got elected to a different party.", "A constitutional amendment (1985) made an MP or MLA lose the seat for changing parties."])
W("sa1", "short_answer", SYS, "Compare one-party, two-party and multi-party systems with examples.",
  ["One-party system: only one party is allowed to control and run the government, as in China; it is not democratic as voters have no real choice.",
   "Two-party system: power usually changes between two main parties, though others exist, as in the USA and the United Kingdom.",
   "Multi-party system: several parties compete and more than two have a reasonable chance of coming to power alone or in alliance, as in India."])
W("sa2", "short_answer", NAT, "Describe any three national parties of India.",
  ["Indian National Congress: founded in 1885; centrist; supports secularism and welfare of weaker sections and minorities; led the UPA from 2004 to 2014.",
   "Bharatiya Janata Party: founded in 1980 from the Bharatiya Jana Sangh (1951); cultural nationalism and integral humanism; leads the NDA and formed governments after 2014, 2019 and 2024.",
   "Bahujan Samaj Party: founded in 1984 by Kanshi Ram; represents dalits, adivasis, OBCs and religious minorities; inspired by Sahu Maharaj, Phule, Periyar and Ambedkar; main base in Uttar Pradesh."])
W("sa3", "short_answer", CHAL, "What steps have been taken to reform political parties in India?",
  ["Anti-defection law: a constitutional amendment (1985) makes an MP or MLA lose the seat for changing parties; it reduced defection but made dissent harder.",
   "Supreme Court order (2003): every candidate must file an affidavit giving details of property and pending criminal cases, which is made public.",
   "Election Commission order: parties must hold organisational elections and file income tax returns, though sometimes it is a formality."])
W("la1", "long_answer", SYS, "'India has a multi-party system.' Explain the reasons and the role of state parties.",
  ["In a multi-party system, several parties compete and more than two have a reasonable chance of coming to power, alone or in alliance.",
   "A party system evolves over a long time, depending on the nature of society, its social and regional divisions, its history of politics and its system of elections.",
   "India's social and geographical diversity is not easily absorbed by two or even three parties, so many parties represent different interests and regions.",
   "Over the last three decades, the number and strength of state parties has grown, making Parliament more diverse; from 1989 to 2014 no national party won a majority on its own.",
   "Since 1996, nearly every state party has been part of a national coalition government, which has strengthened federalism and democracy."])
W("la2", "long_answer", CHAL, "Suggest reforms to make political parties more democratic, and explain the role of citizens.",
  ["A law to regulate the internal affairs of parties: a register of members, following the party constitution, an independent authority to settle disputes, and open elections to the highest posts.",
   "Make it mandatory for parties to give about one-third of tickets to women and to have a quota for women in party decision-making bodies.",
   "State funding of elections: the government should give parties money or support in kind (petrol, paper, telephone) based on votes secured in the last election.",
   "Legal reforms need care, since over-regulation can be counter-productive and parties may find ways to cheat the law.",
   "Citizens can put pressure on parties through petitions, publicity, agitations, the media and movements, and those who want reform can join parties themselves."])
W("cb1", "case_based", WHY, "Read the source and answer the questions.\n\n*\"A political party is a group of people who come together to contest elections and hold power in the government. They agree on some policies and programmes for the society with a view to promote the collective good. Since there can be different views on what is good for all, parties try to persuade people why their policies are better than others.\"* (NCERT)\n\n"
  "(i) What is the main aim of a political party? (1)\n\n(ii) Name the three components of a political party. (1)\n\n(iii) Give two functions of a political party. (2)",
  ["(i) To contest elections and hold power in the government to implement its policies.", "(ii) Leaders, active members and followers.",
   "(iii) Any two: contest elections; put forward policies and programmes; make laws; form and run governments; act as opposition; shape public opinion; provide access to government schemes."])
W("cb2", "case_based", CHAL, "Read the source and answer the questions.\n\n*\"Since most political parties do not practise open and transparent procedures for their functioning, there are very few ways for an ordinary worker to rise to the top in a party. Those who happen to be the leaders are in a position of unfair advantage to favour people close to them or even their family members.\"* (NCERT)\n\n"
  "(i) Which challenge to political parties is described here? (1)\n\n(ii) Why is it bad for democracy? (1)\n\n(iii) Suggest two reforms to deal with such challenges. (2)",
  ["(i) Dynastic succession, linked to the lack of internal democracy.", "(ii) People without adequate experience or popular support come to occupy positions of power, which is unfair to other members.",
   "(iii) Any two: a law to regulate internal affairs and hold open elections to party posts; maintaining membership registers; an independent authority for party disputes; pressure from citizens and the media."])
# ---------------- Assertion-reason ----------------
C.arq("ar1", WHY, "Political parties are necessary in a representative democracy.", "Large societies need an agency to gather different views on various issues and present them to the government.", 0,
      "R explains A.", "almost every country has parties.", "this is why parties emerged.")
C.arq("ar2", SYS, "A one-party system is not a good option.", "It does not give voters a real choice, so it is not a democratic option.", 0,
      "R explains A.", "China is an example.", "democracy needs competition.")
C.arq("ar3", SYS, "India has a two-party system.", "India's social and geographical diversity is not easily absorbed by two or three parties.", 3,
      "A is false: India has a multi-party system. R is true and is the reason for it.", "India is multi-party.", "this explains the multi-party system.")
C.arq("ar4", NAT, "State parties have become important in national politics.", "From 1989 to 2014, no national party won a majority in the Lok Sabha on its own.", 0,
      "R explains A.", "they joined national coalition governments.", "national parties needed allies.")
C.arq("ar5", CHAL, "The anti-defection law has made dissent more difficult.", "Under it, MPs and MLAs must accept whatever the party leaders decide, or lose their seats.", 0,
      "R explains A.", "this is a side effect of the law.", "this is how the law works.")
C.arq("ar6", CHAL, "Ideological differences among parties have increased in recent years.", "In India, differences among major parties on economic issues have reduced.", 3,
      "A is false: ideological differences have declined. R is true.", "they have declined.", "this shows the decline.")

chapter = header(SUBJ, N, "Political Parties", ["why_parties", "party_systems", "national_and_state_parties", "challenges_and_reforms"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: this chapter is fully in the board examination (Political Science: 20 marks). There is no map item from this chapter. The list of national parties is updated to the Election Commission's 2023 recognition; the NCERT book prints an older list.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
