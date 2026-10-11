"""CBSE Class 10 Economics Ch 4: Globalisation and the Indian Economy.

Only 'What is Globalisation?' and 'Factors that have enabled Globalisation' are examined in the 2025-26 board exam;
the other parts are an interdisciplinary project (internal assessment)."""
import sys
from ss_common import make, header, path, SQP, SHINE, CB

ROOT = sys.argv[1]
SUBJ, N = "economics", 4
PATH = path(SUBJ, "ch04_globalisation_and_the_indian_economy")
C = make(SUBJ, N, "eco10ch04")
blk, M, W = C.blk, C.m, C.w
GLO, MNC, TECH, LIB = ["what_is_globalisation"], ["mncs_and_investment"], ["technology"], ["liberalisation"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 4 exercises", "question": n}

FACTORS = ("| Factor | How it enabled globalisation | Examples |\n|---|---|---|\n| **Transportation technology** | faster delivery of goods across long distances at lower cost | **containers** loaded intact onto ships, railways, planes and trucks; cheaper air transport |\n"
           "| **Information and communication technology** | instant contact and information across the world | telephone, mobile phones, fax, **satellite** communication, **computers and the internet**, e-mail, internet banking |\n"
           "| **Liberalisation of foreign trade and investment** | removal of government barriers so goods and investment can move freely | India's new economic policy from **1991**; foreign companies allowed to set up factories and offices |")

sections = [
 {"id": "s1", "title": "A connected world", "blocks": [
  blk("s1.hook", "hook", title="One phone, many countries",
    body="Look at a mobile phone. It may be designed in one country, use chips made in another, be assembled in a third, and be sold in India by a company based in yet another country. You pay for it through a bank app linked to the internet.\n\n"
         "This tight connection between countries is **globalisation**. This chapter, for the board exam, answers two questions: **what is globalisation**, and **what made it possible?**"),
  blk("s1.inspiration", "inspiration", title="Opening up the economy", person="Manmohan Singh", years="1932–2024",
    body="In **1991**, India faced a serious economic crisis. As Finance Minister, economist **Dr Manmohan Singh** presented the budget that began India's **new economic policy** of liberalisation. Many barriers on foreign trade and foreign investment were removed, so that Indian producers could compete with producers around the world.\n\n"
         "He later served as Prime Minister from 2004 to 2014. The 1991 reforms were a major step in connecting India's economy with the world.",
    future="This chapter leads to careers in international business, trade, logistics, economics and information technology."),
  C.socratic("s1.socratic", "Why might a company produce goods in several countries instead of one?",
    ["To produce where costs are lower and to be close to markets", "Because one country cannot make anything", "Because governments force all companies to move"], 0,
    "MNCs look for locations where production is cheap and markets are near."),
 ]},
 {"id": "s2", "title": "What is globalisation?", "blocks": [
  blk("s2.thm", "theory", title="Integration of production and markets", revision=True,
    body="**Multinational corporations (MNCs):** a **multinational corporation (MNC)** is a company that **owns or controls production in more than one nation**. MNCs set up offices and factories for production in regions where they can get **cheap labour and other resources**, so that their costs of production are low and they can earn greater profits. They also look for places close to markets, with good infrastructure and favourable government policies.\n"
         "- **Investment** is the money spent to buy assets such as land, buildings, machines and other equipment. Investment made by MNCs is called **foreign investment**.\n\n"
         "**What is globalisation?** In the past few decades, more and more MNCs have been looking for locations around the world that would be cheap for their production. **Foreign investment** by MNCs in these countries has been rising. At the same time, **foreign trade** between countries has been rising rapidly, and a large part of it is also controlled by MNCs.\n"
         "- The result of greater foreign investment and greater foreign trade has been **greater integration of production and markets** across countries.\n"
         "- **Globalisation is this process of rapid integration or interconnection between countries.** MNCs are playing a **major role** in the globalisation process.\n"
         "- More and more **goods and services, investments and technology** are moving between countries. Most regions of the world are in closer contact with each other than a few decades back.\n"
         "- Besides the movements of goods, services, investments and technology, countries can also be connected through the **movement of people** between countries. People usually move from one country to another in search of better income, better jobs or better education. However, in the past few decades, there has **not been much increase in the movement of people** between countries, due to various **restrictions**.\n\n"
         "**Effects of globalisation (for understanding):** more foreign investment brings **expansion of markets and access to technology**; cultural exchange spreads **practices, ideas and values** across borders; and large **MNCs become dominant players** in global markets. At the same time, competition and automation can lead to the **loss of some traditional jobs**."),
  C.kc("s2.check", "A company that owns or controls production in more than one nation is called:",
    [("a multinational corporation", ""), ("a cooperative society", "A cooperative is a local member organisation."), ("a public sector enterprise", "That is government-owned."), ("a self-help group", "An SHG is a savings group.")],
    "MNCs play a major role in globalisation."),
  C.kc("s2.check2", "Globalisation is best described as:",
    [("the process of rapid integration or interconnection between countries", ""), ("the removal of all governments", "Governments remain."), ("trade only within one country", "It is about many countries."), ("the movement of people only", "Goods, services, investment and technology move most.")],
    "Greater foreign investment and trade integrate production and markets."),
 ]},
 {"id": "s3", "title": "Factors that have enabled globalisation", "blocks": [
  blk("s3.thm", "theory", title="Technology and liberalisation", revision=True,
    body="**1. Technology:** rapid improvement in technology has been one major factor that has stimulated the globalisation process.\n"
         "- **Transportation technology:** this has made much **faster delivery** of goods across long distances possible at **lower costs**. Of particular importance is the use of **containers** for the transport of goods: goods are placed in containers that can be loaded **intact** onto ships, railways, planes and trucks. Containers have led to huge reductions in **port handling costs** and increased the **speed** with which exports can reach markets. Similarly, the cost of **air transport** has fallen, enabling much greater volumes of goods to be transported by airlines.\n"
         "- **Information and communication technology (IT):** even more remarkable have been the developments in IT. **Telecommunication facilities** (telegraph, telephone including mobile phones, fax) are used to contact one another around the world, to access information instantly and to communicate from remote areas. This has been facilitated by **satellite communication** devices. **Computers** have entered almost every field of activity. Through the **internet**, one can obtain and share information on almost anything; it also allows us to send instant electronic mail (**e-mail**) and talk (voice-mail) across the world at negligible costs.\n"
         "- **Example:** a news magazine published for London readers is designed and printed in Delhi. The text is sent through the internet to the Delhi office; designers in Delhi take orders from the London office using telecommunication facilities; the design is printed in Delhi, and payment is made through a bank in London using **internet banking**. IT thus plays a major role in spreading out the **production of services** across countries.\n\n"
         "**2. Liberalisation of foreign trade and foreign investment policy:**\n"
         "- **Trade barrier:** a **tax on imports** is an example of a trade barrier. It is called a barrier because some restriction has been set up. Governments can use trade barriers to **increase or decrease (regulate) foreign trade** and to decide what kinds of goods, and how much of each, should come into the country.\n"
         "- **After independence**, the Indian government put **barriers to foreign trade and foreign investment**. This was considered necessary to **protect the producers within the country from foreign competition**. Industries were just coming up in the **1950s and 1960s**, and competition from imports at that stage would not have allowed them to come up. Thus, India allowed imports of only **essential items** such as machinery, fertilisers and petroleum.\n"
         "- Starting around **1991**, some far-reaching changes in policy were made in India. The government decided that the time had come for Indian producers to **compete with producers around the globe**. It felt that competition would **improve the performance** of producers within the country, which would have to improve their quality. This decision was supported by powerful international organisations.\n"
         "- Thus, **barriers on foreign trade and foreign investment were removed to a large extent**. Goods could be imported and exported easily, and foreign companies could set up factories and offices here.\n"
         "- **Liberalisation:** removing barriers or restrictions set by the government is what is known as liberalisation. With liberalisation of trade, businesses are allowed to make decisions **freely** about what they wish to import or export. The government imposes much fewer restrictions than before and is therefore said to be more liberal."),
  blk("s3.table", "markdown_table", title="Factors that have enabled globalisation", revision=True, body=FACTORS),
  C.kc("s3.check", "Why did the use of containers help globalisation?",
    [("They reduced port handling costs and increased the speed of exports", ""), ("They made goods heavier to carry", "They made transport easier."), ("They stopped air transport", "Air transport also grew."), ("They raised the cost of shipping", "They reduced costs.")],
    "Containers can be loaded intact onto ships, trains, planes and trucks."),
  C.kc("s3.check2", "Why did India put barriers on foreign trade and investment after independence?",
    [("To protect producers within the country from foreign competition", ""), ("To stop all exports", "The aim was to protect new industries."), ("Because foreign goods were banned by the UN", "There was no such ban."), ("To help MNCs enter India", "The barriers kept foreign competition out.")],
    "Industries were just coming up in the 1950s and 1960s."),
 ]},
 {"id": "s4", "title": "Remember, avoid, practise", "blocks": [
  blk("s4.memory", "memory_trick", title="Memory tricks",
    body="- **Globalisation = rapid integration of countries**, through goods, services, investment, technology (and a little movement of people).\n- **MNC = owns or controls production in more than one nation.**\n"
         "- **Factors: \"T-T-L\"**: Transport technology (containers), Telecom/IT (internet, satellites), Liberalisation (1991).\n"
         "- **Trade barrier example = tax on imports.**\n- **Before 1991: protect; after 1991: compete.**"),
  blk("s4.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying globalisation is mainly about people moving between countries: movement of people has **not increased much** due to restrictions.\n"
         "2. Defining MNC as any big company: an MNC **owns or controls production in more than one nation**.\n"
         "3. Saying India removed trade barriers right after independence: it **put** barriers after independence and **removed** them from **1991**.\n"
         "4. Forgetting containers when writing about transport technology.\n5. Calling liberalisation 'more government control': liberalisation means **removing** government barriers."),
  blk("s4.tip", "teacher_tip", title="Try this in class",
    body="Ask students to check the labels of five things at home (a phone, a toy, clothes, a packet of food, a bottle). Note the brand and the country of manufacture. Discuss how many involve MNCs and how technology and liberalisation made this possible. (The rest of the NCERT chapter, such as the WTO and fair globalisation, is done as a project.)"),
  blk("s4.reflection", "reflection", title="Think and explain",
    body="Think of one service you use that may be produced in another country, such as online customer care or a video app. How did information technology make this possible?"),
  blk("s4.connection", "connection", title="Where this leads",
    body="- **History Chapter 3 (The Making of a Global World):** the long history of trade and migration.\n- **Geography Chapter 7 (Lifelines of National Economy):** transport and communication.\n"
         "- **Chapter 2 (Sectors of the Indian Economy):** growth of IT-based services."),
  blk("s4.mastery", "mastery", title="Mastery challenge",
    body="'Technology and liberalisation together made globalisation possible.' Explain in about 120 words.\n\n"
         "**Model answer:** Globalisation is the rapid integration of countries through foreign trade and foreign investment, led largely by MNCs. Technology made it possible: containers cut port handling costs and sped up exports, and air transport became cheaper. "
         "Information and communication technology, including telephones, satellites, computers and the internet, allowed instant contact and let services, such as designing a magazine in Delhi for London readers, be produced across countries. "
         "Liberalisation removed government barriers: after independence India protected its new industries with trade barriers, but from 1991 it removed most barriers on foreign trade and investment so that Indian producers would compete globally. Together, these allowed goods, services, investment and technology to move freely."),
  blk("s4.summary", "summary", title="Chapter summary",
    body="- An MNC owns or controls production in more than one nation; money MNCs spend on assets abroad is foreign investment.\n"
         "- Rising foreign investment and foreign trade have integrated production and markets across countries: this is globalisation.\n"
         "- Goods, services, investments and technology move between countries; movement of people has not increased much because of restrictions.\n"
         "- Technology enabled globalisation: containers and cheaper air transport, and IT such as telecom, satellites, computers and the internet.\n"
         "- Liberalisation enabled it too: India protected its industries after independence, then removed most trade and investment barriers from 1991."),
  blk("s4.examtips", "exam_tips", title="Board exam tips",
    body="- Only two topics are examined: **What is Globalisation?** and **Factors that have enabled Globalisation**. The rest of the NCERT chapter is an internally assessed interdisciplinary project.\n"
         "- The 2025-26 sample paper had a 1-mark matching of effects and outcomes of globalisation (answer D) and a 3-mark question on factors that contributed to globalisation (movement of goods and services, ICT, transport technology, movement of people, liberalisation).\n"
         "- In 3-mark answers, name the factor and give one example for each."),
  blk("s4.flash1", "flashcard", front="What is globalisation?", back="The process of rapid integration or interconnection between countries, through foreign trade and foreign investment."),
  blk("s4.flash2", "flashcard", front="What is a multinational corporation?", back="A company that owns or controls production in more than one nation."),
  blk("s4.flash3", "flashcard", front="What is a trade barrier? Give an example.", back="A government restriction on foreign trade, such as a tax on imports."),
  blk("s4.flash4", "flashcard", front="What is liberalisation?", back="Removing barriers or restrictions set by the government on trade and investment."),
 ]},
]

# ---------------- Sample paper ----------------
M("sqp34", GLO, "Match the effects of globalisation with their outcomes: (1) Increased foreign investment, (2) Cultural exchange and awareness, (3) Technological exchange and awareness, (4) Growth of multinational corporations; with (i) Expansion of global markets and access to technology, (ii) Loss of traditional jobs due to automation and cheaper labour elsewhere, (iii) Spread of cultural practices, ideas and values across borders, (iv) Large companies becoming dominant players in global markets. Choose the correct option:",
  [("1-iii, 2-ii, 3-i, 4-iv", "Foreign investment expands markets (i), not cultural spread."), ("1-iv, 2-ii, 3-i, 4-iii", "Growth of MNCs makes large companies dominant (iv)."),
   ("1-ii, 2-iv, 3-iii, 4-i", "Cultural exchange spreads practices and ideas (iii)."), ("1-i, 2-iii, 3-ii, 4-iv", "")],
  "As per the CBSE marking scheme, the answer is D: 1-i, 2-iii, 3-ii, 4-iv.", "medium", SQP(34), correct=3)
W("sqp37", "short_answer", TECH, "Highlight the significant three factors that have contributed to the growth of globalisation.",
  ["Transportation technology: containers loaded intact onto ships, trains, planes and trucks cut port handling costs and sped up exports; air transport became cheaper.",
   "Information and communication technology: telephones, mobile phones, fax, satellite communication, computers and the internet allow instant contact and spread the production of services across countries.",
   "Liberalisation of foreign trade and foreign investment policy: from 1991 India removed most barriers, so goods could be imported and exported easily and foreign companies could set up factories and offices (movement of goods, services and people also grew)."], source=SQP(37))

# ---------------- NCERT exercises ----------------
W("ex1", "short_answer", GLO, "What do you understand by globalisation? Explain in your own words.",
  ["Globalisation is the process of rapid integration or interconnection between countries.",
   "It happens as more goods and services, investments and technology move between countries, mainly through MNCs that set up production in many countries and through rising foreign trade.",
   "As a result, production and markets in different countries become closely linked; people also move, though less, because of restrictions."], source=ex("1"))
W("ex2", "short_answer", LIB, "What was the reason for putting barriers to foreign trade and foreign investment by the Indian government? Why did it wish to remove these barriers?",
  ["After independence, the government put barriers to protect producers within the country from foreign competition, as industries were just coming up in the 1950s and 1960s; only essential items like machinery, fertilisers and petroleum were imported.",
   "Around 1991, the government felt Indian producers were ready to compete with producers around the globe.",
   "It believed competition would improve the performance and quality of Indian producers, so it removed barriers to a large extent (liberalisation)."], source=ex("2"))
W("ex7", "short_answer", LIB, "How has liberalisation of trade and investment policies helped the globalisation process?",
  ["Liberalisation removed government barriers such as taxes on imports, so goods could be imported and exported easily.",
   "Foreign companies were allowed to set up factories and offices, increasing foreign investment by MNCs.",
   "Businesses could freely decide what to import and export, which increased foreign trade and integrated production and markets across countries."], source=ex("7"))
M("ex13", GLO, "The past two decades of globalisation have seen rapid movements in:",
  [("goods, services and investments between countries", ""), ("goods, services and people between countries", "Movement of people has not increased much."), ("goods, investments and people between countries", "Movement of people has been restricted."), ("only people between countries", "People's movement has been limited.")],
  "Movement of people has not increased much because of restrictions.", "medium", ex("13"), correct=0)

# ---------------- MCQs ----------------
M("mcq01", GLO, "Globalisation is the process of:",
  [("rapid integration or interconnection between countries", ""), ("closing borders to trade", "That is the opposite."), ("growth of only local markets", "It links markets across countries."), ("government ownership of all firms", "That is not globalisation.")], "MNCs play a major role in it.")
M("mcq02", MNC, "Which is the main role of MNCs in globalisation?",
  [("spreading production and investment across countries", ""), ("collecting taxes", "Governments collect taxes."), ("printing currency", "Central banks issue currency."), ("making laws", "Legislatures make laws.")], "They control a large part of foreign trade too.")
M("mcq03", MNC, "Money spent to buy assets such as land, buildings and machines is called:",
  [("investment", ""), ("consumption", "That is spending on goods for use."), ("tax", "That is paid to the government."), ("barter", "That is direct exchange of goods.")], "Investment by MNCs is foreign investment.")
M("mcq04", MNC, "Investment made by MNCs in other countries is called:",
  [("foreign investment", ""), ("public investment", "That is by the government."), ("domestic saving", "That is saving within a country."), ("trade barrier", "That is a restriction.")], "It has been rising in the past few decades.")
M("mcq05", MNC, "MNCs set up production where they can get:",
  [("cheap labour and other resources, so costs are low", ""), ("the highest wages", "They look for cheaper labour."), ("no markets at all", "They look for nearness to markets."), ("the strictest trade barriers", "They prefer favourable policies.")], "This helps them earn greater profits.")
M("mcq06", GLO, "The result of greater foreign investment and foreign trade has been:",
  [("greater integration of production and markets across countries", ""), ("the end of all trade", "Trade has increased."), ("less contact between regions", "Regions are in closer contact."), ("the disappearance of MNCs", "MNCs have grown.")], "This is globalisation.")
M("mcq07", GLO, "Which has NOT increased much in the past few decades of globalisation?",
  [("movement of people between countries", ""), ("movement of goods", "This has increased."), ("movement of investments", "This has increased."), ("movement of technology", "This has increased.")], "Various restrictions limit the movement of people.")
M("mcq08", GLO, "People usually move from one country to another in search of:",
  [("better income, jobs or education", ""), ("higher taxes", "People do not seek higher taxes."), ("trade barriers", "These are restrictions."), ("containers", "These are for goods.")], "But restrictions limit migration.")
M("mcq09", TECH, "Which development in transport technology helped globalisation the most?",
  [("the use of containers", ""), ("the use of bullock carts", "These are local transport."), ("closing of ports", "That would stop trade."), ("higher cost of air transport", "Air transport became cheaper.")], "Containers are loaded intact onto ships, trains, planes and trucks.")
M("mcq10", TECH, "Containers led to:",
  [("huge reductions in port handling costs", ""), ("higher port handling costs", "Costs fell."), ("slower delivery of exports", "Delivery became faster."), ("the end of shipping", "Shipping grew.")], "Exports reach markets faster.")
M("mcq11", TECH, "What has happened to the cost of air transport?",
  [("it has fallen", ""), ("it has risen sharply", "It has fallen."), ("it has stayed the same", "It has fallen."), ("air transport has stopped", "It has grown.")], "Larger volumes of goods are now carried by air.")
M("mcq12", TECH, "Instant communication from remote areas has been made possible by:",
  [("satellite communication devices", ""), ("trade barriers", "These restrict trade."), ("containers", "These carry goods."), ("import taxes", "These are trade barriers.")], "Telephones, mobile phones and fax use them.")
M("mcq13", TECH, "The internet allows us to:",
  [("obtain and share information and send e-mail across the world at negligible cost", ""), ("only watch films", "It does much more."), ("avoid all trade", "It increases trade."), ("transport heavy goods", "It carries information, not goods.")], "It is a key part of IT.")
M("mcq14", TECH, "A news magazine for London readers is designed and printed in Delhi. This shows that IT has helped in:",
  [("spreading the production of services across countries", ""), ("stopping foreign trade", "It increases trade."), ("raising trade barriers", "It is about technology."), ("moving people to London", "The work moves, not the people.")], "Payment is made through internet banking.")
M("mcq15", TECH, "In the magazine example, payment is made through:",
  [("internet banking", ""), ("barter", "Barter is direct exchange of goods."), ("gold coins", "Not in this example."), ("cash sent by ship", "It is done online.")], "IT makes this instant.")
M("mcq16", LIB, "Which is an example of a trade barrier?",
  [("a tax on imports", ""), ("a container", "That is transport technology."), ("an e-mail", "That is IT."), ("a bank deposit", "That is not a trade barrier.")], "Governments use barriers to regulate foreign trade.")
M("mcq17", LIB, "Governments use trade barriers to:",
  [("increase or decrease (regulate) foreign trade", ""), ("print money", "That is the central bank's job."), ("build containers", "That is technology."), ("ban all exports forever", "They regulate, not ban forever.")], "They decide what goods and how much come in.")
M("mcq18", LIB, "After independence, India allowed imports mainly of:",
  [("essential items such as machinery, fertilisers and petroleum", ""), ("luxury cars", "Only essential items were allowed."), ("all goods freely", "There were barriers."), ("no goods at all", "Essential items were allowed.")], "This protected new industries.")
M("mcq19", LIB, "India's barriers on foreign trade after independence were meant to:",
  [("protect domestic producers from foreign competition", ""), ("attract MNCs", "They kept foreign competition out."), ("increase imports of luxury goods", "Imports were limited."), ("stop all industrial growth", "They protected new industries.")], "Industries were coming up in the 1950s and 1960s.")
M("mcq20", LIB, "In which year did India begin far-reaching changes to liberalise its economy?",
  [("1991", ""), ("1947", "Barriers were put after independence."), ("1965", "That is not the year of liberalisation."), ("2005", "Liberalisation began in 1991.")], "Barriers on trade and investment were removed to a large extent.")
M("mcq21", LIB, "Why did the Indian government decide to remove trade barriers around 1991?",
  [("It felt Indian producers should compete with producers around the globe", ""), ("It wanted to protect producers from competition", "That was the earlier policy."), ("It wanted to stop exports", "Exports became easier."), ("It wanted to ban foreign companies", "Foreign companies were allowed in.")], "Competition was expected to improve quality.")
M("mcq22", LIB, "Liberalisation means:",
  [("removing barriers or restrictions set by the government", ""), ("adding more taxes on imports", "That is a trade barrier."), ("nationalising all companies", "That is not liberalisation."), ("closing the economy", "That is the opposite.")], "Businesses can decide freely what to import or export.")
M("mcq23", LIB, "After liberalisation, foreign companies in India could:",
  [("set up factories and offices", ""), ("not enter at all", "They were allowed in."), ("only export from India", "They could produce and sell in India."), ("print Indian currency", "Only the RBI issues currency.")], "Foreign investment increased.")
M("mcq24", LIB, "With liberalisation of trade, businesses are allowed to:",
  [("make decisions freely about what to import or export", ""), ("ignore all laws", "Laws still apply."), ("stop paying wages", "That is not allowed."), ("avoid competition", "They face more competition.")], "The government imposes fewer restrictions.")
M("mcq25", LIB, "The government's decision to liberalise in 1991 was also supported by:",
  [("powerful international organisations", ""), ("all moneylenders", "This is not mentioned."), ("only farmers' unions", "This is not mentioned."), ("no one", "International organisations supported it.")], "Competition was expected to improve performance.")
M("mcq26", GLO, "Which outcome is linked with increased foreign investment?",
  [("expansion of global markets and access to technology", ""), ("spread of cultural practices", "That is linked with cultural exchange."), ("loss of all jobs", "Some traditional jobs may be lost, but not all."), ("closing of borders", "Investment opens markets.")], "This was part of the sample paper matching.")
M("mcq27", GLO, "Which outcome is linked with cultural exchange?",
  [("spread of cultural practices, ideas and values across borders", ""), ("large companies becoming dominant", "That is linked with growth of MNCs."), ("access to technology", "That is linked with investment."), ("higher import taxes", "That is a trade barrier.")], "Globalisation also connects cultures.")
M("mcq28", MNC, "The growth of MNCs can lead to:",
  [("large companies becoming dominant players in global markets", ""), ("small producers always gaining", "Many small producers face tough competition."), ("the end of foreign trade", "Trade grows."), ("no change in markets", "Markets change a lot.")], "MNCs control much of world trade.")
M("mcq29", TECH, "Which is part of information and communication technology?",
  [("mobile phones and fax", ""), ("containers", "These are transport technology."), ("ships", "These are transport."), ("import taxes", "These are trade barriers.")], "Telecommunication links people across the world.")
M("mcq30", TECH, "Computers and the internet have helped globalisation mainly by:",
  [("letting information and services move instantly across countries", ""), ("raising the cost of communication", "They reduced it."), ("stopping trade in services", "They increased it."), ("replacing all transport", "Goods still need transport.")], "They connect producers and buyers worldwide.")
M("mcq31", GLO, "Which statement about foreign trade in the globalisation period is correct?",
  [("Foreign trade has been rising rapidly, and a large part of it is controlled by MNCs", ""), ("Foreign trade has stopped", "It has risen rapidly."),
   ("Only governments carry out foreign trade", "MNCs control a large part."), ("Foreign trade has no link with globalisation", "It is central to globalisation.")], "Trade and investment together integrate markets.")
M("mcq32", LIB, "A government that imposes much fewer restrictions on trade than before is said to be:",
  [("more liberal", ""), ("more protective", "Protection means more barriers."), ("closed", "It is more open."), ("socialist only", "The term is liberal.")], "This is the meaning of liberalisation.")
M("mcq33", TECH, "Telecommunication facilities include:",
  [("telegraph, telephone including mobile phones, and fax", ""), ("containers and ships", "These are transport."), ("dams and canals", "These are irrigation works."), ("taxes and quotas", "These are trade barriers.")], "They help people contact each other worldwide.")
M("mcq34", MNC, "Besides cheap labour, MNCs choose locations that have:",
  [("nearness to markets, good infrastructure and favourable government policies", ""), ("no roads or electricity", "They need good infrastructure."), ("very high taxes", "They prefer favourable policies."), ("no skilled workers", "They look for available skills.")], "These keep costs low.")
# ---------------- True / false ----------------
C.tf("tf5", TECH, "The cost of air transport has fallen, allowing larger volumes of goods to be carried by air.", True, "Cheaper air transport helped globalisation.")
C.tf("tf6", LIB, "Liberalisation means adding more restrictions on foreign trade.", False, "Liberalisation means removing government barriers and restrictions.")
C.tf("tf1", MNC, "An MNC owns or controls production in more than one nation.", True, "This is the NCERT definition.")
C.tf("tf2", GLO, "Movement of people between countries has greatly increased in the past few decades.", False, "It has not increased much because of various restrictions.")
C.tf("tf3", LIB, "A tax on imports is an example of a trade barrier.", True, "It restricts imports.")
C.tf("tf4", LIB, "India removed most trade barriers immediately after independence in 1947.", False, "India put barriers after independence and removed them from 1991.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", MNC, "What is an MNC? Why does it set up production in other countries?",
  ["An MNC is a company that owns or controls production in more than one nation.", "It sets up production where it can get cheap labour and resources and be near markets, so its costs are low and profits high."])
W("vsa2", "very_short_answer", TECH, "How did containers help globalisation?",
  ["Goods are placed in containers that can be loaded intact onto ships, railways, planes and trucks.", "This reduced port handling costs and increased the speed with which exports reach markets."])
W("vsa3", "very_short_answer", LIB, "What is a trade barrier? Why do governments use it?",
  ["A trade barrier is a restriction on foreign trade, such as a tax on imports.", "Governments use it to regulate foreign trade, deciding what kinds of goods and how much of each come into the country."])
W("sa1", "short_answer", GLO, "Explain how MNCs, foreign investment and foreign trade together lead to globalisation.",
  ["MNCs look for locations around the world where production is cheap, so their foreign investment in these countries has been rising.",
   "At the same time, foreign trade between countries has been rising rapidly, and a large part of it is controlled by MNCs.",
   "Greater foreign investment and trade have integrated production and markets across countries; this rapid integration is globalisation."])
W("sa2", "short_answer", TECH, "How has information and communication technology helped globalisation?",
  ["Telecommunication facilities like telephones, mobile phones and fax, aided by satellites, let people contact each other and access information instantly, even from remote areas.",
   "Computers and the internet let people share information and send e-mail across the world at negligible cost.",
   "IT spreads the production of services across countries, for example a London magazine designed and printed in Delhi and paid for by internet banking."])
W("sa3", "short_answer", LIB, "Compare India's trade policy before and after 1991.",
  ["Before 1991: the government put barriers on foreign trade and investment to protect new domestic industries; only essential imports like machinery, fertilisers and petroleum were allowed.",
   "After 1991: the government decided Indian producers should compete globally, and removed barriers to a large extent.",
   "Goods could now be imported and exported easily, foreign companies could set up factories and offices, and businesses could decide freely what to trade."])
W("la1", "long_answer", GLO, "What is globalisation? Explain the different ways in which countries are connected through it.",
  ["Globalisation is the process of rapid integration or interconnection between countries.",
   "Goods and services move between countries through rising foreign trade, a large part of which is controlled by MNCs.",
   "Investment moves between countries as MNCs set up factories and offices abroad; this foreign investment has been rising.",
   "Technology moves across countries, and IT spreads the production of services, linking producers and markets worldwide.",
   "People also move in search of better income, jobs or education, but this movement has not increased much because of restrictions."])
W("la2", "long_answer", TECH, "Explain the factors that have enabled globalisation.",
  ["Transportation technology: containers loaded intact onto ships, trains, planes and trucks reduced port handling costs and sped up exports; air transport became cheaper.",
   "Information and communication technology: telephones, mobile phones, fax and satellite communication allow instant contact; computers and the internet let information and services move across the world at negligible cost.",
   "IT helps spread the production of services, such as designing and printing a London magazine in Delhi with payment by internet banking.",
   "Liberalisation of foreign trade and investment: after independence India used trade barriers to protect new industries, but from 1991 it removed most barriers so producers would compete globally.",
   "With liberalisation, goods could be imported and exported easily and foreign companies could set up factories and offices, increasing foreign trade and investment."])
W("cb1", "case_based", TECH, "Read the source and answer the questions.\n\n*\"Rapid improvement in technology has been one major factor that has stimulated the globalisation process. For instance, the past fifty years have seen several improvements in transportation technology. This has made much faster delivery of goods across long distances possible at lower costs.\"* (NCERT)\n\n"
  "(i) Name one improvement in transportation technology that helped globalisation. (1)\n\n(ii) How did it help? (1)\n\n(iii) Give two examples of information and communication technology that helped globalisation. (2)",
  ["(i) The use of containers (or cheaper air transport).", "(ii) Containers reduced port handling costs and increased the speed of exports.",
   "(iii) Any two: telephones and mobile phones; fax; satellite communication; computers; the internet and e-mail; internet banking."])
W("cb2", "case_based", LIB, "Read the source and answer the questions.\n\n*\"Starting around 1991, some far-reaching changes in policy were made in India. The government decided that the time had come for Indian producers to compete with producers around the globe. It felt that competition would improve the performance of producers within the country since they would have to improve their quality.\"* (NCERT)\n\n"
  "(i) What did the government decide around 1991? (1)\n\n(ii) Why did it expect competition to help? (1)\n\n(iii) What is liberalisation? How did it help globalisation? (2)",
  ["(i) That Indian producers should compete with producers around the globe, so trade and investment barriers were removed.", "(ii) Competition would force producers to improve their quality and performance.",
   "(iii) Liberalisation is removing government barriers on trade and investment; it let goods be imported and exported easily and foreign companies set up in India, increasing integration with other countries."])
# ---------------- Assertion-reason ----------------
C.arq("ar1", GLO, "Globalisation has led to greater integration of production and markets across countries.", "Foreign investment and foreign trade between countries have been rising rapidly.", 0,
      "R explains A.", "production and markets are closely linked.", "this is what integrates them.")
C.arq("ar2", MNC, "MNCs set up production in regions with cheap labour and resources.", "MNCs want to keep their costs of production low and earn greater profits.", 0,
      "R explains A.", "they look for cheap locations.", "this is their aim.")
C.arq("ar3", TECH, "Containers increased the speed of exports.", "Goods in containers can be loaded intact onto ships, railways, planes and trucks.", 0,
      "R explains A.", "port handling became faster and cheaper.", "this is how containers work.")
C.arq("ar4", LIB, "India removed trade barriers soon after independence.", "Barriers were needed to protect new industries from foreign competition.", 3,
      "A is false: India put barriers after independence and removed them from 1991. R is true.", "barriers were put, not removed.", "this was the reason for barriers.")
C.arq("ar5", GLO, "Movement of people between countries has not increased much in recent decades.", "Various restrictions limit the movement of people between countries.", 0,
      "R explains A.", "migration has stayed limited.", "restrictions are the reason.")
C.arq("ar6", LIB, "Liberalisation helped the globalisation process.", "A tax on imports is an example of a trade barrier.", 1,
      "Both are true, but R defines a trade barrier; it does not explain how liberalisation helped globalisation.", "removing barriers increased trade and investment.", "this is a definition.")

chapter = header(SUBJ, N, "Globalisation and the Indian Economy", ["what_is_globalisation", "mncs_and_investment", "technology", "liberalisation"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: only 'What is Globalisation?' and 'Factors that have enabled Globalisation' are evaluated in the board examination, and this lesson covers them (with the MNC and investment ideas they need). "
  "Production across countries, interlinking production, Chinese toys in India, the WTO, the impact of globalisation and the struggle for fair globalisation are an interdisciplinary project (internally assessed, 5 marks) and are left out here. There is no map item from this chapter.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
