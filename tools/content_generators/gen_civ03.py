"""CBSE Class 10 Political Science Ch 3: Gender, Religion and Caste (fully in the 2025-26 board syllabus)."""
import sys
from ss_common import make, header, path, SQP, SHINE, CB

ROOT = sys.argv[1]
SUBJ, N = "civics", 3
PATH = path(SUBJ, "ch03_gender_religion_and_caste")
C = make(SUBJ, N, "civ10ch03")
blk, M, W = C.blk, C.m, C.w
GEN, REL, SEC, CASTE = ["gender_and_politics"], ["communalism"], ["secular_state"], ["caste_and_politics"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 3 exercises", "question": n}

WOMEN = ("| Area | What the facts show |\n|---|---|\n| **Education** | literacy rate of women 54% against 76% for men in the NCERT figures (Census 2001); Census 2011: about 65% against 82%. Fewer girls go for higher studies, as parents prefer to spend on sons |\n"
         "| **Jobs and pay** | very few women in highly paid and valued jobs; an average woman works about one hour more than a man every day, but much of her work is unpaid and not valued; women are paid less despite the **Equal Remuneration Act, 1976** |\n"
         "| **Son preference** | sex-selective abortion; child sex ratio fell to **919** girls per 1000 boys (Census 2011; it was 927 in 2001) |\n"
         "| **Safety** | harassment, exploitation and domestic violence; public spaces are often unsafe for women |\n"
         "| **Politics** | women were about **14 per cent** of Lok Sabha members in 2019 (78) and about 13.6 per cent in 2024 (74); less than 5 per cent in many state assemblies; one-third of seats in local bodies are reserved for women |")
COMMUNAL = ("| Form of communal politics | Example |\n|---|---|\n| **Everyday beliefs**: religious prejudices, stereotypes and belief in the superiority of one's religion | thinking that people of another religion are all alike or inferior |\n"
            "| **Quest for political dominance**: majoritarian dominance by the majority, or a separate political unit for a minority | demanding that the state follow one religion; demand for a separate state on religious lines |\n"
            "| **Political mobilisation on religious lines**: sacred symbols, religious leaders, emotional appeal and fear | using religious slogans and fear of another community to win votes |\n"
            "| **Communal violence, riots and massacres** | the riots at the time of Partition in 1947 |")

sections = [
 {"id": "s1", "title": "Differences in a democracy", "blocks": [
  blk("s1.hook", "hook", title="Do differences divide us?",
    body="Every society has differences: between women and men, between people of different religions, and between castes. In a democracy, these differences often show up in politics.\n\n"
         "Is that good or bad? It can be both. When a group that was left out raises its voice, democracy becomes fairer. But when one group is turned against another, democracy is harmed. This chapter looks at three social differences: **gender, religion and caste**, and asks which expressions of them are healthy in a democracy."),
  blk("s1.inspiration", "inspiration", title="Educate, and change society", person="Savitribai Phule", years="1831–1897",
    body="With her husband **Jotiba Phule**, **Savitribai Phule** opened one of the first schools for girls in India in Pune in **1848**. She became one of the country's first women teachers. People threw mud and stones at her on the way to school, but she carried a spare sari and kept teaching.\n\n"
         "The Phules also fought against untouchability and caste discrimination. Their work shows how education can challenge both gender and caste inequality.",
    future="This chapter leads to careers in law, social work, journalism, public policy, teaching and gender and human rights studies."),
  C.socratic("s1.socratic", "When is it healthy for a social group to raise its demands in politics?",
    ["When a group that faces discrimination demands equal rights through democratic means", "When one group demands that another group be kept out of power", "Never: differences should not be expressed in politics"], 0,
    "Expressing demands for equality is healthy; using differences to dominate or attack others is not."),
 ]},
 {"id": "s2", "title": "Gender and politics", "blocks": [
  blk("s2.thm", "theory", title="Gender division, feminist movements and women's representation", revision=True,
    body="**Public/private division:** gender division is a form of hierarchical social division seen everywhere, but it is rarely recognised in the study of politics. It is understood as natural and unchangeable, but it is based not on biology but on **social expectations and stereotypes**.\n"
         "- **Sexual division of labour:** a system in which all work inside the home is either done by the women of the family or organised by them through domestic helpers. Boys and girls are brought up to believe that the main responsibility of women is housework and bringing up children.\n"
         "- Women do all the work inside the home, such as cooking, cleaning, washing clothes, tailoring and looking after children. Men do these jobs too when they are paid for it outside the home: most tailors or cooks in hotels are men.\n"
         "- Many women also work outside: in villages they fetch water, collect fuel and work in the fields; in cities, poor women work as domestic helpers and middle-class women work in offices. But their work is **not valued** and does not get recognition.\n"
         "- The result is that although women are about half of humanity, their role in **public life**, especially politics, is minimal in most societies.\n\n"
         "**Feminist movements:** women in different parts of the world organised and agitated for equal rights. There were agitations in different countries for the extension of **voting rights** to women. These agitations demanded enhancing the political and legal status of women and improving their educational and career opportunities. More radical women's movements aimed at equality in **personal and family life** as well.\n"
         "- A **feminist** is a woman or a man who believes in equal rights and opportunities for women and men.\n"
         "- In some parts of the world, for example in **Scandinavian countries such as Sweden, Norway and Finland**, the participation of women in public life is very high.\n\n"
         "**India: a patriarchal society.** **Patriarchy** literally means rule by father; it refers to a system that values men more and gives them power over women. Women in India face disadvantage, discrimination and oppression in many ways:\n"
         "- **Literacy:** the literacy rate among women is only **54 per cent**, compared with **76 per cent** among men (NCERT figures, Census 2001; Census 2011 showed about 65 and 82 per cent). A smaller proportion of girls go for higher studies, because parents prefer to spend their resources on their sons' education.\n"
         "- **Jobs:** the proportion of women among the highly paid and valued jobs is still very small. On average, an Indian woman works **one hour more** than an average man every day, yet much of her work is not paid and therefore often not valued.\n"
         "- **Wages:** the **Equal Remuneration Act, 1976** provides that equal wages should be paid for equal work. However, in almost all areas of work, from sports and cinema to factories and fields, women are paid less than men, even when both do exactly the same work.\n"
         "- **Son preference:** in many parts of India, parents prefer to have sons and find ways to have the girl child aborted before she is born. This sex-selective abortion led to a decline in the **child sex ratio** (number of girl children per thousand boys) to merely **919** (Census 2011). In some states, it fell below 850 or even 800.\n"
         "- **Violence:** there are reports of harassment, exploitation and violence against women. Urban areas have become particularly unsafe for women, and even at home women face beating and other forms of **domestic violence**.\n\n"
         "**Women's political representation:** issues of women's well-being do not get adequate attention because women's representation in legislatures is low.\n"
         "- The percentage of elected women members in the **Lok Sabha** touched **14.36 per cent** for the first time in **2019** (78 women); in **2024**, 74 women were elected (about 13.6 per cent). Their share in many state assemblies is **less than 5 per cent**. India is among the bottom group of nations in the world in this respect.\n"
         "- One way to solve this problem is to make it legally binding to have a fair proportion of women in elected bodies. This is what the **Panchayati Raj** has done: **one-third** of seats in local government bodies, in panchayats and municipalities, are reserved for women. There are now more than **10 lakh** elected women representatives in rural and urban local bodies.\n"
         "- Women's organisations long demanded at least one-third of seats in the **Lok Sabha and State Assemblies** for women. In **September 2023**, Parliament passed the **Constitution (106th Amendment) Act (Nari Shakti Vandan Adhiniyam)**, which reserves one-third of these seats for women; it will come into effect after the next census and delimitation.\n\n"
         "Gender division is an example that some form of social division needs to be expressed in politics: disadvantaged groups benefit when social divisions become a political issue. In countries where women's political participation increased, their role in public life improved."),
  blk("s2.table", "markdown_table", title="How women are disadvantaged in India", revision=True, body=WOMEN),
  C.kc("s2.check", "Who is a feminist?",
    [("A woman or a man who believes in equal rights and opportunities for women and men", ""), ("Only a woman who works outside the home", "Men can be feminists too."),
     ("A person who believes men are superior", "That is the opposite."), ("A person who wants women to stay at home", "That is a patriarchal view.")],
    "Feminism is about equal rights and opportunities."),
  C.kc("s2.check2", "In India, one-third of seats are already reserved for women in:",
    [("panchayats and municipalities", ""), ("the Rajya Sabha", "There is no reservation there."), ("the Union Cabinet", "There is no reservation in the Cabinet."), ("the Supreme Court", "Courts have no such reservation.")],
    "Reservation in the Lok Sabha and assemblies was passed in 2023 but comes into effect after the next census and delimitation."),
 ]},
 {"id": "s3", "title": "Religion, communalism and politics", "blocks": [
  blk("s3.thm", "theory", title="Communalism and the secular state", revision=True,
    body="Religious differences are often expressed in politics. Is that always wrong? Not necessarily:\n"
         "- **Gandhiji** used to say that religion can never be separated from politics. By religion he meant not any particular religion, but the **moral values** that inform all religions. He believed politics must be guided by ethics drawn from religion.\n"
         "- Human rights groups have argued that most of the victims of communal riots in our country are people from **religious minorities**, and have demanded that the government take special steps to protect them.\n"
         "- Women's movements have argued that **family laws** of all religions discriminate against women, and have demanded that they be changed to make them more equitable.\n\n"
         "These involve a relationship between religion and politics, and they are not wrong. Every person should be able to express in politics their needs, interests and demands as a member of a religious community. Those with political power should be able to **regulate the practice of religion** to prevent discrimination and oppression. These acts are fine as long as they treat every religion **equally**.\n\n"
         "**Communalism:** the problem begins when religion is seen as the **basis of the nation**. It becomes acute when religion is expressed in politics in exclusive and partisan terms, when one religion and its followers are pitted against another, when beliefs of one religion are presented as superior, when demands of one religious group are formed in opposition to another, and when **state power** is used to establish the domination of one religious group over the rest. This manner of using religion in politics is **communal politics**.\n"
         "- Communal politics is based on the idea that **religion is the principal basis of social community**. It believes that followers of a particular religion must belong to one community, that their fundamental interests are the same, and that people who follow different religions cannot belong to the same social community.\n"
         "- This is a false belief: people of one religion do not have the same interests and aspirations in every context. Everyone has several other roles, positions and identities. There are many voices inside every community.\n\n"
         "**Forms of communalism in politics:**\n"
         "1. **Everyday beliefs:** routinely involve religious prejudices, stereotypes of religious communities and belief in the superiority of one's religion over others. This is so common that we often fail to notice it.\n"
         "2. **Quest for political dominance:** a communal mind often leads to a quest for the political dominance of one's own religious community. For those belonging to the majority community, this takes the form of **majoritarian dominance**; for those belonging to a minority community, it can take the form of a desire to form a **separate political unit**.\n"
         "3. **Political mobilisation on religious lines:** this involves the use of sacred symbols, religious leaders, emotional appeal and plain fear to bring the followers of one religion together in the political arena. In electoral politics, this often involves special appeal to the interests or emotions of voters of one religion in preference to others.\n"
         "4. **Communal violence, riots and massacres:** sometimes communalism takes its most ugly form. **India and Pakistan** suffered some of the worst communal riots at the time of **Partition**, and the post-independence period has also seen large-scale communal violence.\n\n"
         "**Secular state:** communalism was and continues to be one of the major challenges to democracy in our country. The makers of our Constitution chose the model of a **secular state**:\n"
         "- There is **no official religion** for the Indian state. Unlike the status of **Buddhism in Sri Lanka**, that of **Islam in Pakistan** and that of **Christianity in England**, our Constitution does not give a special status to any religion.\n"
         "- The Constitution provides to all individuals and communities **freedom to profess, practise and propagate any religion**, or not to follow any.\n"
         "- The Constitution **prohibits discrimination** on grounds of religion.\n"
         "- At the same time, the Constitution allows the state to **intervene in the matters of religion** in order to ensure **equality within religious communities**. For example, it bans **untouchability**.\n\n"
         "Secularism is not just an ideology of some parties or persons; it is one of the **foundations of our country**. Communalism should be combated in everyday beliefs and in religion-based mobilisation in politics."),
  blk("s3.table", "markdown_table", title="Forms of communal politics", revision=True, body=COMMUNAL),
  C.kc("s3.check", "Communal politics is based on the belief that:",
    [("religion is the principal basis of social community", ""), ("all religions are equal", "That is a secular idea."), ("religion should guide politics through moral values", "That was Gandhiji's view, which is not communal."),
     ("the state should protect religious minorities", "That is a demand of human rights groups, not communalism.")],
    "Communal politics sees followers of one religion as one community with the same interests."),
  C.kc("s3.check2", "Which feature makes India a secular state?",
    [("There is no official religion for the Indian state", ""), ("Hinduism is the state religion", "India has no state religion."), ("The state never intervenes in religion", "It can intervene to ensure equality, such as banning untouchability."),
     ("Only the majority religion can be practised", "Everyone has freedom of religion.")],
    "The Constitution gives no special status to any religion."),
 ]},
 {"id": "s4", "title": "Caste and politics", "blocks": [
  blk("s4.thm", "theory", title="Caste inequalities, caste in politics and politics in caste", revision=True,
    body="**Caste inequalities:** unlike gender and religion, caste division is special to India. All societies have some social inequality and some form of division of labour, but in most societies occupations are not passed on from one generation to another. The caste system is an extreme form of this: it is based on **hereditary occupational division** sanctioned by rituals.\n"
         "- Members of the same caste group were supposed to form a social community that practised the same or similar occupation, married within the caste group and did not eat with members of other caste groups.\n"
         "- The caste system was based on exclusion of and discrimination against the 'outcaste' groups, who were subjected to the inhuman practice of **untouchability**.\n"
         "- Political leaders and social reformers like **Jotiba Phule, Gandhiji, B.R. Ambedkar and Periyar Ramaswami Naicker** advocated and worked to establish a society in which caste inequalities are absent.\n\n"
         "**Changes in modern India:** partly due to their efforts and partly due to other socio-economic changes, castes and the caste system have undergone great changes. With **economic development, large-scale urbanisation, growth of literacy and education, occupational mobility** and the weakening of the position of landlords in villages, the old notions of caste hierarchy are breaking down. In urban areas, it does not matter much who is walking along next to us on a street or eating at the next table in a restaurant. The **Constitution prohibited any caste-based discrimination** and laid the foundations of policies to reverse the injustices of the caste system.\n\n"
         "**But caste has not disappeared:**\n"
         "- Even now most people **marry within their own caste** or tribe.\n"
         "- **Untouchability** has not ended completely, despite constitutional prohibition.\n"
         "- The effects of centuries of advantages and disadvantages continue to be felt today. The caste groups that had access to education under the old system have done very well in acquiring modern education. Those groups that did not have access to education or were prohibited from acquiring it have naturally lagged behind. That is why there is a disproportionately large presence of **'upper caste'** among the urban middle classes. Caste continues to be closely linked to **economic status**.\n\n"
         "**Caste in politics:** caste can take various forms in politics:\n"
         "- When parties choose candidates in elections, they keep in mind the **caste composition of the electorate** and nominate candidates from different castes so as to muster the support needed to win.\n"
         "- Political parties and candidates in elections make appeals to **caste sentiment** to muster support. Some political parties are known to favour some castes and are seen as their representatives.\n"
         "- **Universal adult franchise** and the principle of **one-person-one-vote** compelled political leaders to gear up to the task of mobilising and securing political support. It also brought new consciousness among the people of castes that were hitherto treated as inferior and low.\n\n"
         "**Caste alone does not decide elections:**\n"
         "- **No parliamentary constituency** in the country has a clear majority of one single caste. So every candidate and party needs to win the confidence of more than one caste and community.\n"
         "- **No party wins the votes of all the voters** of a caste or community. When people say a caste is a 'vote bank' of one party, it usually means that a large proportion of the voters from that caste vote for that party.\n"
         "- Many political parties may put up candidates from the **same caste**, so some voters have more than one candidate from their caste while many voters have none.\n"
         "- The ruling party and the sitting MP or MLA frequently **lose elections** in our country. That could not have happened if all castes and communities were frozen in their political preferences.\n"
         "- Voters have strong attachment to political parties, which is often stronger than their attachment to their caste. People within the same caste or community have different interests depending on their **economic condition**. Rich and poor, or men and women from the same caste often vote very differently. People's assessment of the **performance of the government** and the **popularity rating of leaders** matter and are often decisive in elections.\n\n"
         "**Politics in caste:** it is not politics that gets caste-ridden; it is caste that gets politicised:\n"
         "- Each caste group tries to become bigger by incorporating within it neighbouring castes or sub-castes that were earlier excluded from it.\n"
         "- Various caste groups are required to enter into a **coalition** with other castes or communities, and thus enter into a dialogue and negotiation.\n"
         "- New kinds of caste groups have come up in the political arena, like **'backward' and 'forward'** caste groups.\n\n"
         "**Effects:** caste politics has helped people from **Dalit and OBC** castes to gain better access to decision making. But **exclusive attention to caste can produce negative results**: it can divert attention from other pressing issues like **poverty, development and corruption**, and in some cases caste division leads to **tensions, conflict and even violence**."),
  C.kc("s4.check", "Which of these shows that caste alone does not decide elections in India?",
    [("No parliamentary constituency has a clear majority of one single caste", ""), ("Parties choose candidates keeping caste in mind", "This shows caste matters in politics."),
     ("Some parties are known to favour some castes", "This shows caste matters in politics."), ("Caste sentiment is used in campaigns", "This shows caste matters in politics.")],
    "Every candidate must win support from more than one caste."),
  C.kc("s4.check2", "Exclusive attention to caste in politics can:",
    [("divert attention from issues like poverty, development and corruption", ""), ("end untouchability at once", "Untouchability needs social and legal action."),
     ("make every election peaceful", "It can lead to tension and violence."), ("remove all economic inequality", "It does not do this.")],
    "This was the point of the 2025-26 sample paper assertion-reason question."),
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Women's disadvantages \"LJWSV\"**: Literacy, Jobs, Wages, Son preference, Violence.\n- **Women's numbers \"54-76, 919, 1976\"**: literacy 54% vs 76% (NCERT), child sex ratio 919, Equal Remuneration Act 1976.\n"
         "- **Four forms of communalism \"Beliefs, Dominance, Mobilisation, Violence\"** (B-D-M-V: \"Bad Deeds Mean Violence\").\n"
         "- **Secular state \"No-Free-No-Fix\"**: No official religion, Freedom of religion, No discrimination, can Fix inequality within religions (untouchability ban).\n"
         "- **Caste alone does not decide: \"No majority, No full vote, Same-caste rivals, Sitting MPs lose\".**\n- **Politics in caste: \"Bigger, Coalition, Backward-Forward\".**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying gender division is biological: it is based on **social expectations and stereotypes**.\n2. Thinking only women can be feminists: a feminist is **a woman or a man** who believes in equal rights.\n"
         "3. Calling every link between religion and politics communal: Gandhiji's moral values, protection of minorities and reform of family laws are **not** communal.\n"
         "4. Saying a secular state has nothing to do with religion: it can **intervene** to ensure equality, such as banning untouchability.\n"
         "5. Saying caste alone decides elections: no constituency has one caste majority, and sitting MPs often lose.\n"
         "6. Writing that one-third reservation for women is already in force in the Lok Sabha: the 2023 Act will apply only after the next census and delimitation; it is in force in **panchayats and municipalities**."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Ask students to note who does each household task at home for one week (cooking, cleaning, shopping, paying bills, helping with homework). Pool the results anonymously and discuss: are these roles based on biology or on social expectations?"),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Think of an election advertisement or speech you have seen. Did it appeal to gender, religion or caste? Was the appeal for equality (healthy) or against another group (unhealthy)?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Chapter 1 (Power-sharing):** sharing power with social groups.\n- **Chapter 4 (Political Parties):** how parties mobilise voters.\n"
         "- **Chapter 5 (Outcomes of Democracy):** dignity and freedom of citizens, especially women and disadvantaged castes."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="'Caste cannot alone determine election results in India.' Justify in about 120 words.\n\n"
         "**Model answer:** Caste does play a role in politics: parties choose candidates keeping the caste composition of the electorate in mind and appeal to caste sentiment. But caste alone cannot decide results. "
         "No parliamentary constituency has a clear majority of one single caste, so every candidate must win the support of several castes and communities. No party gets the votes of all the voters of a caste. "
         "Many parties put up candidates from the same caste, so voters of that caste have to choose between them. Ruling parties and sitting MPs and MLAs frequently lose elections, which could not happen if caste preferences were fixed. "
         "Voters also judge the performance of the government and the popularity of leaders, and rich and poor members of the same caste often vote differently."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Gender division is based on social expectations, not biology; the sexual division of labour keeps women's work unrecognised.\n"
         "- Feminist movements demanded voting rights and equality; India is still patriarchal: low literacy, low pay, son preference and violence.\n"
         "- Women's share in the Lok Sabha was about 14% in 2019; one-third of local body seats are reserved for women; a 2023 Act will reserve one-third in the Lok Sabha and assemblies.\n"
         "- Communalism treats religion as the basis of the nation; its forms are everyday beliefs, quest for dominance, mobilisation on religious lines and violence.\n"
         "- India is a secular state: no official religion, freedom of religion, no discrimination, and state intervention for equality.\n"
         "- Caste still matters, but caste alone does not decide elections; politics has also changed caste, and exclusive attention to caste can be harmful."),
  blk("s5.examtips", "exam_tips", title="Board exam tips",
    body="- The 2025-26 sample paper had an assertion-reason item: exclusive attention to caste can produce negative results (answer: both true, R explains A), and a 2-mark question on two aspects of life where women face inequality (education, jobs, wages, son preference, violence).\n"
         "- 3/5-mark favourites: forms of communalism, features of the secular state, caste inequalities today, why caste alone does not decide elections, women's representation.\n"
         "- Use one fact or example in each point (54% literacy, Equal Remuneration Act 1976, child sex ratio 919)."),
  blk("s5.flash1", "flashcard", front="What is patriarchy?", back="Literally rule by father; a system that values men more and gives them power over women."),
  blk("s5.flash2", "flashcard", front="What is communalism?", back="Politics based on the belief that religion is the principal basis of social community, using religion in exclusive and partisan terms."),
  blk("s5.flash3", "flashcard", front="Name four features of India's secular state.", back="No official religion; freedom to profess, practise and propagate any religion; no discrimination on grounds of religion; state can intervene to ensure equality within religions."),
  blk("s5.flash4", "flashcard", front="What is the sexual division of labour?", back="A system in which all work inside the home is done by women or organised by them through domestic helpers."),
 ]},
]

# ---------------- Sample paper ----------------
C.arq("sqp23", CASTE, "Exclusive attention to caste can produce negative results in democracy.", "It can divert attention from other important issues thus leading to tensions, conflicts and even violence.", 0,
      "Both are true and R explains A (CBSE marking scheme: A).", "caste politics can harm democracy.", "this is how it causes harm.", source=SQP(23))
W("sqp25", "very_short_answer", GEN, "'Women in India face discrimination, disadvantages and oppression in many ways.' Highlight any two aspects of life where you witness this inequality.",
  ["Any one: education: the literacy rate among women is only 54% compared with 76% among men, and parents prefer to spend on sons' education; or jobs: few women hold highly paid and valued jobs, and their work is not valued.",
   "Any other one: women are paid less than men for the same work despite the Equal Wages Act; son preference and sex-selective abortion have lowered the child sex ratio; women face exploitation at work and domestic violence at home."], source=SQP(25))

# ---------------- NCERT exercises ----------------
W("ex1", "short_answer", GEN, "Mention different aspects of life in which women are discriminated or disadvantaged in India.",
  ["Education: the literacy rate among women is only 54% against 76% for men, and fewer girls go for higher studies.",
   "Work and pay: women are a small share of highly paid jobs, work about an hour more than men daily but their work is unpaid and unvalued, and they are paid less despite the Equal Remuneration Act, 1976.",
   "Son preference has lowered the child sex ratio to 919; women face harassment, exploitation and domestic violence, and their representation in legislatures is low."], source=ex("1"))
W("ex2", "short_answer", REL, "State different forms of communal politics with one example each.",
  ["Everyday beliefs: religious prejudices and stereotypes, such as believing one's religion is superior; and the quest for political dominance, such as majoritarian dominance or the demand for a separate state for a minority.",
   "Political mobilisation on religious lines: use of sacred symbols, religious leaders, emotional appeal and fear, for example appeals to voters of one religion at election time.",
   "Communal violence, riots and massacres: for example the riots at the time of Partition in 1947."], source=ex("2"))
W("ex3", "short_answer", CASTE, "State how caste inequalities are still continuing in India.",
  ["Most people still marry within their own caste or tribe.", "Untouchability has not ended completely, despite constitutional prohibition.",
   "Castes that had access to education did well, while others lagged behind; so upper castes are over-represented in the urban middle class, and caste is still linked to economic status."], source=ex("3"))
W("ex4", "very_short_answer", CASTE, "State two reasons to say that caste alone cannot determine election results in India.",
  ["No parliamentary constituency has a clear majority of one single caste, so candidates need the support of many castes; and no party wins the votes of all voters of a caste.",
   "Ruling parties and sitting MPs often lose elections, and voters judge the government's performance and the popularity of leaders."], source=ex("4"))
W("ex5", "very_short_answer", GEN, "What is the status of women's representation in India's legislative bodies?",
  ["It is low: women were about 14 per cent of the Lok Sabha in 2019 (about 13.6 per cent in 2024), and less than 5 per cent in many state assemblies.",
   "In panchayats and municipalities one-third of seats are reserved for women, giving more than 10 lakh women representatives; a 2023 Act will reserve one-third of Lok Sabha and assembly seats after the next census and delimitation."], source=ex("5"))
W("ex6", "very_short_answer", SEC, "Mention any two constitutional provisions that make India a secular state.",
  ["There is no official religion for the Indian state; and the Constitution gives everyone freedom to profess, practise and propagate any religion, or not follow any.",
   "The Constitution prohibits discrimination on grounds of religion, and allows the state to intervene to ensure equality within religious communities, for example by banning untouchability."], source=ex("6"))
M("ex7", GEN, "When we speak of gender divisions, we usually refer to:",
  [("Unequal roles assigned by the society to men and women", ""), ("Biological difference between men and women", "Gender division is social, not biological."),
   ("Unequal child sex ratio", "That is one result of gender division."), ("Absence of voting rights for women in democracies", "Women have voting rights in democracies.")],
  "Gender division is based on social expectations and stereotypes.", "easy", ex("7"), correct=0)
M("ex8", GEN, "In India, seats are reserved for women in (as given in the NCERT exercise):",
  [("Panchayati Raj bodies", ""), ("Lok Sabha", "The 2023 Act reserving Lok Sabha seats comes into effect only after the next census and delimitation."),
   ("State legislative assemblies", "Reservation here also waits for the next census and delimitation."), ("Cabinets", "There is no reservation in Cabinets.")],
  "One-third of seats in panchayats and municipalities are reserved for women.", "easy", ex("8"), correct=0)
M("ex9", REL, "Communal politics is based on the belief that: A. One religion is superior to that of others. B. Followers of different religions can live together happily as equal citizens. C. Followers of a particular religion constitute one community. D. State power cannot be used to establish the domination of one religious group over others. Which statements are correct?",
  [("A and C", ""), ("A, B, C and D", "B and D are secular ideas."), ("A, B and D", "B and D are secular ideas."), ("B and D", "These are the opposite of communal politics.")],
  "Communal politics believes in the superiority of one religion and treats its followers as one community.", "medium", ex("9"), correct=0)
M("ex10", SEC, "Which among the following statements about India's Constitution is wrong? It:",
  [("gives official status to one religion", ""), ("prohibits discrimination on grounds of religion", "This is true."), ("provides to all individuals freedom to profess any religion", "This is true."), ("ensures equality of citizens within religious communities", "This is true.")],
  "India has no official religion.", "easy", ex("10"), correct=0)
M("ex11", CASTE, "Social divisions based on ______ are peculiar to India.",
  [("caste", ""), ("gender", "Gender division is found everywhere."), ("religion", "Religious divisions exist in many countries."), ("language", "Linguistic divisions exist in many countries.")],
  "Caste division is special to India.", "easy", ex("11"), correct=0)
M("ex12", GEN, "Match: (1) a person who believes in equal rights and opportunities for women and men, (2) a person who says that religion is the principal basis of community, (3) a person who thinks that caste is the principal basis of community, (4) a person who does not discriminate others on the basis of religious beliefs, with (A) Communalist, (B) Feminist, (C) Secularist, (D) Casteist. The correct order for 1, 2, 3, 4 is:",
  [("B A D C", ""), ("B C A D", "2 is communalist, not secularist."), ("D C A B", "1 is feminist."), ("C D B A", "1 is feminist and 4 is secularist.")],
  "1-B, 2-A, 3-D, 4-C.", "easy", ex("12"), correct=0)

# ---------------- MCQs ----------------
M("mcq01", GEN, "The sexual division of labour means that:",
  [("all work inside the home is done by women or organised by them through domestic helpers", ""), ("men and women share housework equally", "That is the ideal, not the system."),
   ("women do only paid work", "Women's housework is unpaid."), ("only men work outside the home", "Many women work outside too.")], "Boys and girls are brought up to believe this.")
M("mcq02", GEN, "Gender division is based on:",
  [("social expectations and stereotypes", ""), ("biology", "It is not based on biology."), ("religion", "It exists across religions."), ("law", "Laws in India promote equality.")], "It is wrongly seen as natural and unchangeable.")
M("mcq03", GEN, "In which countries is the participation of women in public life very high?",
  [("Sweden, Norway and Finland", ""), ("India, Pakistan and Bangladesh", "Women's participation here is low."), ("Saudi Arabia and Iran", "Women's participation here is low."), ("Sri Lanka and Nepal", "These are not the NCERT examples.")], "These are the Scandinavian countries.")
M("mcq04", GEN, "Patriarchy refers to a system that:",
  [("values men more and gives them power over women", ""), ("values women more than men", "That is the opposite."), ("treats men and women equally", "That is gender equality."), ("is ruled by elected women", "Patriarchy means rule by father.")], "Literally, rule by father.")
M("mcq05", GEN, "According to NCERT, the literacy rate among women in India is:",
  [("54 per cent, compared with 76 per cent among men", ""), ("76 per cent, compared with 54 per cent among men", "The figures are reversed."),
   ("equal to men", "There is a large gap."), ("90 per cent", "It is much lower.")], "These are Census 2001 figures used in the CBSE marking scheme.")
M("mcq06", GEN, "The Equal Remuneration Act was passed in:",
  [("1976", ""), ("1956", "1956 is not correct."), ("1992", "1992 was the local government amendment."), ("2023", "2023 was the women's reservation Act.")], "It provides equal wages for equal work.")
M("mcq07", GEN, "The child sex ratio is:",
  [("the number of girl children per thousand boys", ""), ("the number of boys per thousand girls", "It is girls per thousand boys."),
   ("the literacy rate of girls", "That is literacy."), ("the number of women in Parliament", "That is representation.")], "It fell to 919 in Census 2011.")
M("mcq08", GEN, "Why do issues of women's well-being not get adequate attention in India?",
  [("because women's representation in legislatures is low", ""), ("because women do not vote", "Women vote in large numbers."), ("because there are no laws for women", "There are many laws."), ("because women do no work", "Women do a great deal of work.")], "Women were about 14% of the Lok Sabha in 2019.")
M("mcq09", GEN, "In 2019, the share of women in the Lok Sabha touched:",
  [("about 14 per cent", ""), ("about 33 per cent", "That is the reservation target."), ("about 50 per cent", "It is far lower."), ("about 5 per cent", "That is the share in many state assemblies.")], "It was 14.36%, the highest so far.")
M("mcq10", GEN, "The Act passed in 2023 to reserve one-third of Lok Sabha and state assembly seats for women is:",
  [("the Nari Shakti Vandan Adhiniyam (106th Amendment)", ""), ("the Equal Remuneration Act", "That is about equal wages (1976)."), ("the 73rd Amendment", "That was about panchayats (1992)."), ("the Right to Education Act", "That is about schooling.")], "It applies after the next census and delimitation.")
M("mcq11", GEN, "There are now more than how many elected women representatives in rural and urban local bodies?",
  [("10 lakh", ""), ("1 lakh", "There are many more."), ("10,000", "There are many more."), ("1 crore", "That is too many.")], "One-third of seats in local bodies are reserved for women.")
M("mcq12", REL, "By religion, Gandhiji meant:",
  [("the moral values that inform all religions", ""), ("the beliefs of one particular religion", "He did not mean any particular religion."), ("religious rituals only", "He meant moral values."), ("the rule of priests", "He did not mean that.")], "He believed politics must be guided by ethics.")
M("mcq13", REL, "Which is NOT an example of communal politics?",
  [("Women's movements demanding fair family laws in all religions", ""), ("Using fear of another religion to win votes", "This is communal mobilisation."),
   ("Demanding that one religion dominate the state", "This is majoritarian dominance."), ("Spreading stereotypes about another community", "This is a communal everyday belief.")], "Asking for equality within religions is not communal.")
M("mcq14", REL, "The use of sacred symbols, religious leaders and emotional appeal to bring followers of one religion together in politics is:",
  [("political mobilisation on religious lines", ""), ("secularism", "Secularism opposes this."), ("feminism", "Feminism is about gender equality."), ("decentralisation", "That is about local government.")], "It is one form of communal politics.")
M("mcq15", REL, "For a minority community, a communal quest for dominance can take the form of:",
  [("a desire to form a separate political unit", ""), ("majoritarian dominance", "That is for the majority."), ("feminist movements", "They are about gender."), ("caste coalitions", "Those are about caste.")], "For the majority, it takes the form of majoritarian dominance.")
M("mcq16", REL, "Some of the worst communal riots in India and Pakistan took place:",
  [("at the time of Partition", ""), ("in 1993 in Belgium", "Belgium is not relevant here."), ("during the 1857 revolt", "That was not the NCERT example."), ("in 2009", "2009 was the end of Sri Lanka's civil war.")], "Post-independence India has also seen communal violence.")
M("mcq17", SEC, "Which country gives a special status to Buddhism?",
  [("Sri Lanka", ""), ("India", "India has no official religion."), ("Pakistan", "Pakistan gives special status to Islam."), ("England", "England gives special status to Christianity.")], "NCERT compares India with these countries.")
M("mcq18", SEC, "The Indian Constitution allows the state to intervene in religion in order to:",
  [("ensure equality within religious communities", ""), ("make one religion official", "There is no official religion."), ("ban all religions", "Freedom of religion is guaranteed."), ("help the majority religion", "The state treats all religions equally.")], "For example, it bans untouchability.")
M("mcq19", SEC, "Secularism in India is:",
  [("one of the foundations of the country", ""), ("an ideology of only some parties", "It is a constitutional foundation."), ("a ban on religion", "It protects freedom of religion."), ("a foreign idea not in the Constitution", "It is built into the Constitution.")], "The makers of the Constitution chose a secular state.")
M("mcq20", CASTE, "The caste system is based on:",
  [("hereditary occupational division sanctioned by rituals", ""), ("free choice of occupation", "Occupations were inherited."), ("wealth alone", "It was based on birth."), ("education alone", "It was based on birth.")], "Members were expected to marry and eat only within the caste.")
M("mcq21", CASTE, "Who among these worked for a society free of caste inequalities?",
  [("Periyar Ramaswami Naicker", ""), ("Nelson Mandela", "He worked against apartheid in South Africa."), ("Otto von Bismarck", "He unified Germany."), ("Giuseppe Mazzini", "He was an Italian nationalist.")], "Jotiba Phule, Gandhiji and B.R. Ambedkar also did.")
M("mcq22", CASTE, "Which has helped break down old notions of caste hierarchy?",
  [("urbanisation, education and occupational mobility", ""), ("marrying within one's caste", "This keeps caste alive."), ("untouchability", "This is a caste practice."), ("hereditary occupations", "This is the caste system itself.")], "Economic development also weakened landlords in villages.")
M("mcq23", CASTE, "Why is there a large presence of 'upper caste' people among the urban middle classes?",
  [("because caste groups that had access to education did well in modern education", ""), ("because the Constitution favours them", "The Constitution prohibits caste discrimination."),
   ("because other castes refused education", "They were denied access."), ("because of reservation", "Reservation helps disadvantaged groups.")], "Centuries of advantage and disadvantage still have effects.")
M("mcq24", CASTE, "When parties choose candidates keeping in mind the caste composition of the electorate, this shows:",
  [("caste in politics", ""), ("politics in caste", "That is caste becoming politicised."), ("secularism", "This is about caste."), ("feminism", "This is about caste.")], "Parties try to win the support needed to win.")
M("mcq25", CASTE, "Which is a reason why caste alone cannot decide election results?",
  [("Ruling parties and sitting MPs frequently lose elections", ""), ("Parties appeal to caste sentiment", "This shows caste matters."),
   ("Some parties favour some castes", "This shows caste matters."), ("Caste groups form coalitions", "This is politics in caste.")], "Voters' preferences are not frozen.")
M("mcq26", CASTE, "When people call a caste a 'vote bank' of a party, it usually means:",
  [("a large proportion of voters from that caste vote for that party", ""), ("all voters of that caste vote for that party", "No party wins all the votes of a caste."),
   ("the caste keeps money in a bank", "It is a figure of speech."), ("the caste does not vote", "It does vote.")], "No party wins the votes of all voters of a caste.")
M("mcq27", CASTE, "The emergence of 'backward' and 'forward' caste groups in politics is an example of:",
  [("politics in caste", ""), ("caste in politics", "This is caste being changed by politics."), ("communalism", "This is about caste."), ("feminism", "This is about caste.")], "Caste gets politicised.")
M("mcq28", CASTE, "Caste politics has helped:",
  [("Dalit and OBC castes gain better access to decision making", ""), ("end all poverty", "It has not done this."), ("remove caste completely", "Caste still exists."), ("stop all violence", "It can sometimes cause tension.")], "It has given voice to disadvantaged groups.")
M("mcq29", CASTE, "Universal adult franchise and one-person-one-vote:",
  [("brought new consciousness among castes earlier treated as inferior", ""), ("ended caste completely", "Caste still exists."), ("gave more votes to upper castes", "Each person has one vote."), ("stopped parties from appealing to caste", "Parties still appeal to caste.")], "Leaders had to mobilise support from all groups.")
M("mcq30", GEN, "Which statement about gender division shows why it should be expressed in politics?",
  [("Disadvantaged groups benefit when social divisions become a political issue", ""), ("Women should stay out of politics", "This is a patriarchal view."),
   ("Gender roles are natural and fixed", "They are social and can change."), ("Only men's interests matter in politics", "Women are half of humanity.")], "Women's role in public life improved where their participation increased.")
# ---------------- True / false ----------------
C.tf("tf1", GEN, "A feminist can be a man.", True, "A feminist is a woman or a man who believes in equal rights and opportunities for women and men.")
C.tf("tf2", SEC, "The Indian Constitution gives a special status to Hinduism.", False, "India has no official religion.")
C.tf("tf3", CASTE, "At least one parliamentary constituency in India has a clear majority of one single caste.", False, "No parliamentary constituency has a clear majority of one single caste.")
C.tf("tf4", REL, "Communal politics believes that followers of a particular religion form one community with the same interests.", True, "This is a false belief: every community has many voices.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", GEN, "What were the demands of feminist movements?",
  ["Extension of voting rights to women, and enhancing their political and legal status.", "Improving educational and career opportunities; radical movements also demanded equality in personal and family life."])
W("vsa2", "very_short_answer", REL, "Give two examples of religion in politics that are NOT communal.",
  ["Gandhiji's view that politics should be guided by the moral values that inform all religions.", "Human rights groups demanding protection of religious minorities, or women's movements demanding fair family laws in all religions."])
W("vsa3", "very_short_answer", CASTE, "How has politics changed caste ('politics in caste')?",
  ["Each caste group tries to become bigger by incorporating neighbouring castes or sub-castes, and castes enter coalitions with other castes.", "New kinds of caste groups, such as 'backward' and 'forward' castes, have emerged in politics."])
W("sa1", "short_answer", SEC, "Explain the features of India's secular state.",
  ["There is no official religion for the Indian state, unlike Buddhism in Sri Lanka, Islam in Pakistan and Christianity in England.",
   "The Constitution gives all individuals and communities freedom to profess, practise and propagate any religion, or not to follow any, and prohibits discrimination on grounds of religion.",
   "The state can intervene in matters of religion to ensure equality within religious communities, for example by banning untouchability."])
W("sa2", "short_answer", CASTE, "What are the positive and negative effects of caste in politics?",
  ["Positive: caste politics has given Dalit and OBC castes better access to decision making, and one-person-one-vote brought new consciousness among castes earlier treated as inferior.",
   "Negative: exclusive attention to caste can divert attention from pressing issues like poverty, development and corruption.",
   "Negative: caste division can lead to tensions, conflict and even violence."])
W("sa3", "short_answer", GEN, "Why is the representation of women in legislatures important? How has India tried to improve it?",
  ["When women are poorly represented, issues of their well-being do not get adequate attention; women were only about 14% of the Lok Sabha in 2019.",
   "One-third of seats in panchayats and municipalities are reserved for women, and there are now more than 10 lakh women representatives in local bodies.",
   "The Constitution (106th Amendment) Act, 2023 will reserve one-third of seats in the Lok Sabha and state assemblies for women after the next census and delimitation."])
W("la1", "long_answer", REL, "What is communalism? Explain the various forms that communalism can take in politics.",
  ["Communalism is the use of religion in politics in exclusive and partisan terms, based on the belief that religion is the principal basis of social community and that followers of one religion have the same interests.",
   "Everyday beliefs: religious prejudices, stereotypes of religious communities and belief in the superiority of one's religion.",
   "Quest for political dominance: majoritarian dominance for the majority community, or a desire for a separate political unit for a minority community.",
   "Political mobilisation on religious lines: use of sacred symbols, religious leaders, emotional appeal and plain fear, such as appeals to voters of one religion in elections.",
   "Communal violence, riots and massacres: India and Pakistan suffered some of the worst communal riots at the time of Partition, and there has also been communal violence after independence."])
W("la2", "long_answer", CASTE, "'Caste has not disappeared from contemporary India.' Explain. Also show why caste alone cannot decide election results.",
  ["Most people still marry within their own caste, and untouchability has not ended completely despite the constitutional ban.",
   "Groups that had access to education did well, so upper castes are over-represented in the urban middle class, and caste remains linked to economic status.",
   "But no parliamentary constituency has a clear majority of one single caste, so every candidate needs the support of many castes and communities.",
   "No party gets all the votes of a caste, and many parties put up candidates from the same caste.",
   "Ruling parties and sitting MPs often lose; voters judge the government's performance and the popularity of leaders, and people of the same caste vote differently depending on their economic condition."])
W("cb1", "case_based", GEN, "Read the source and answer the questions.\n\n*\"The result of this division of labour is that although women constitute half of the humanity, their role in public life, especially politics, is minimal in most societies. Earlier, only men were allowed to participate in public affairs, vote and contest for public offices. Gradually the gender issue was raised in politics. Women in different parts of the world organised and agitated for equal rights.\"* (NCERT)\n\n"
  "(i) Which division of labour is referred to here? (1)\n\n(ii) Who is a feminist? (1)\n\n(iii) Give two ways in which women are disadvantaged in India today. (2)",
  ["(i) The sexual division of labour, in which all work inside the home is done or organised by women.", "(ii) A woman or a man who believes in equal rights and opportunities for women and men.",
   "(iii) Any two: lower literacy (54% against 76%); few women in highly paid jobs; lower wages for the same work; son preference and a falling child sex ratio; harassment and domestic violence; low representation in legislatures."])
W("cb2", "case_based", SEC, "Read the source and answer the questions.\n\n*\"Communalism was and continues to be one of the major challenges to democracy in our country. The makers of our Constitution were aware of this challenge. That is why they chose the model of a secular state. This choice was reflected in several constitutional provisions.\"* (NCERT)\n\n"
  "(i) Why is communalism a challenge to democracy? (1)\n\n(ii) Name any one country that gives special status to a religion. (1)\n\n(iii) State two constitutional provisions that make India secular. (2)",
  ["(i) It treats religion as the basis of the nation and pits followers of one religion against another, which can lead to domination and violence.", "(ii) Any one: Sri Lanka (Buddhism), Pakistan (Islam), England (Christianity).",
   "(iii) Any two: no official religion; freedom to profess, practise and propagate any religion; no discrimination on grounds of religion; state intervention to ensure equality within religions, such as the ban on untouchability."])
# ---------------- Assertion-reason ----------------
C.arq("ar1", GEN, "Women's role in public life is minimal in most societies.", "The sexual division of labour assigns housework to women and does not value their work.", 0,
      "R explains A.", "this is true in most societies.", "this keeps women out of public life.")
C.arq("ar2", GEN, "The child sex ratio in India has declined.", "In many parts of India, parents prefer sons and resort to sex-selective abortion.", 0,
      "R explains A.", "it fell to 919 in Census 2011.", "this is the cause.")
C.arq("ar3", SEC, "India is a secular state.", "The Constitution bans untouchability.", 1,
      "Both are true, but the ban on untouchability is about equality within religions, not the main reason India is secular (which is that it has no official religion).", "India has no official religion.", "this is state intervention for equality.")
C.arq("ar4", REL, "Every expression of religion in politics is communal.", "Gandhiji believed politics must be guided by ethics drawn from religion.", 3,
      "A is false: expressions like Gandhiji's moral values are not communal. R is true.", "religion in politics is not always communal.", "this was Gandhiji's view.")
C.arq("ar5", CASTE, "Caste alone cannot determine election results in India.", "No parliamentary constituency has a clear majority of one single caste.", 0,
      "R explains A.", "candidates need support from many castes.", "this is a key reason.")
C.arq("ar6", CASTE, "Untouchability has ended completely in India.", "The Constitution prohibits untouchability.", 3,
      "A is false: untouchability has not ended completely despite the ban. R is true.", "it still exists in places.", "it is banned by the Constitution.")

chapter = header(SUBJ, N, "Gender, Religion and Caste", ["gender_and_politics", "communalism", "secular_state", "caste_and_politics"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: this chapter is fully in the board examination (Political Science: 20 marks). There is no map item from this chapter. NCERT figures (literacy 54% and 76%, Census 2001) are kept because the CBSE marking scheme uses them; newer Census 2011 and 2024 Lok Sabha figures are added for context.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
