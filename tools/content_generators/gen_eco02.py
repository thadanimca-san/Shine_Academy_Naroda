"""CBSE Class 10 Economics Ch 2: Sectors of the Indian Economy (fully in the 2025-26 board syllabus)."""
import sys
from ss_common import make, header, path, SQP, SHINE, CB

ROOT = sys.argv[1]
SUBJ, N = "economics", 2
PATH = path(SUBJ, "ch02_sectors_of_the_indian_economy")
C = make(SUBJ, N, "eco10ch02")
blk, M, W = C.blk, C.m, C.w
SEC, GDP, EMP, ORG, PUB = ["three_sectors"], ["gdp_and_sector_shares"], ["employment"], ["organised_unorganised"], ["public_private"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 2 exercises", "question": n}

SECTAB = ("| Sector | What it does | Examples | Also called |\n|---|---|---|---|\n| **Primary** | uses natural resources directly | agriculture, dairy, fishing, forestry, mining | agriculture and related sector |\n"
          "| **Secondary** | turns natural products into other forms through manufacturing | making cloth from cotton, sugar from sugarcane, bricks, steel | industrial sector |\n"
          "| **Tertiary** | provides services that support the other two sectors and people | transport, storage, communication, banking, trade, teaching, IT | service sector |")
ORGTAB = ("| Organised sector | Unorganised sector |\n|---|---|\n| enterprises **registered** by the government; follow rules such as the Factories Act, Minimum Wages Act, Payment of Gratuity Act and Shops and Establishments Act | small and scattered units, largely **outside government control**; rules exist but are not followed |\n"
          "| **regular** work and **job security** | jobs are **low-paid, irregular** and insecure; workers can be asked to leave without reason |\n"
          "| fixed working hours; **overtime** paid | long hours; no overtime |\n| **paid leave**, holidays, provident fund, gratuity, medical benefits, pension | no paid leave, holidays or sick leave |\n"
          "| safe working environment, drinking water | often unsafe conditions |")

sections = [
 {"id": "s1", "title": "Who does what in the economy?", "blocks": [
  blk("s1.hook", "hook", title="From cotton field to shirt",
    body="A farmer grows cotton. A mill spins it into yarn and weaves cloth. A truck carries the cloth to a tailor, a bank gives the tailor a loan, and a shopkeeper sells you the shirt.\n\n"
         "Every shirt passes through many hands. Economists group these activities into three **sectors**. This chapter shows how the sectors work together, which sector produces the most and which employs the most, and why many workers still lack secure jobs."),
  blk("s1.inspiration", "inspiration", title="Organising the unorganised", person="Ela Bhatt", years="1933–2022",
    body="In **1972**, **Ela Bhatt** founded the **Self-Employed Women's Association (SEWA)** in Ahmedabad. It organised women who worked in the unorganised sector: street vendors, head-loaders, home-based workers and garment makers.\n\n"
         "SEWA helped them get fair wages, savings, credit and a voice. Her work shows how workers in the unorganised sector can be protected and empowered.",
    future="This chapter leads to careers in economics, labour welfare, banking, rural development and entrepreneurship."),
  C.socratic("s1.socratic", "Can the primary, secondary and tertiary sectors grow independently of each other?",
    ["No: they are interdependent, as each needs the others' products and services", "Yes: each sector works completely alone", "Only the tertiary sector matters today"], 0,
    "A factory needs raw materials from the primary sector and transport and trade from the tertiary sector."),
 ]},
 {"id": "s2", "title": "The three sectors and GDP", "blocks": [
  blk("s2.thm", "theory", title="Sectors of economic activities and how we measure production", revision=True,
    body="**Primary sector:** when we produce a good by **exploiting natural resources**, it is an activity of the primary sector. Agriculture, dairy, fishing and forestry depend mainly on natural processes; **mining** of minerals also comes under it. Since most of the natural products we get are from agriculture, dairy, fishing and forestry, this sector is also called the **agriculture and related sector**.\n\n"
         "**Secondary sector:** activities in which natural products are **changed into other forms through ways of manufacturing**, in a factory, a workshop or at home. Making cloth from cotton fibre, sugar or gur from sugarcane, and bricks from earth are examples. Since this sector gradually became associated with the different kinds of industries that came up, it is also called the **industrial sector**.\n\n"
         "**Tertiary sector:** activities that **help in the development of the primary and secondary sectors**. These activities by themselves do not produce a good, but they are an aid or support for the production process. Goods need to be **transported** by trucks or trains, **stored** in godowns, and sold through **trade**; we need **communication** and **banking** services. Since these activities generate services rather than goods, the tertiary sector is also called the **service sector**. It also includes services that may not directly help production, such as teachers, doctors, washermen, barbers, cobblers and lawyers, and new services based on **information technology** such as internet cafes, ATM booths, call centres and software companies.\n\n"
         "**Interdependence:** the three sectors are **interdependent**. For example, if farmers refuse to sell sugarcane to a sugar mill, the mill will shut down; a factory needs transport and trade to sell its goods.\n\n"
         "**Comparing the sectors: GDP.** To find the total production of a sector, we cannot simply add the numbers of goods. We add the **values** of goods and services, but only of **final goods and services**:\n"
         "- **Final goods** reach the consumer. **Intermediate goods** are used up in producing final goods. A farmer sells wheat to a flour mill at Rs 8 per kg; the mill grinds it and sells flour to a biscuit company at Rs 10 per kg; the company makes biscuits and sells four packets for Rs 60. The value of the biscuits (Rs 60) already includes the value of the flour and wheat, so counting the wheat and flour separately would be **double counting**.\n"
         "- The value of final goods and services produced in each sector during a particular year gives the **total production of the sector** for that year. The sum of production in the three sectors gives the **Gross Domestic Product (GDP)** of a country: the value of **all final goods and services produced within a country during a particular year**.\n"
         "- In India, the task of measuring GDP is undertaken by a **central government ministry**, which collects information with the help of departments of all states and union territories."),
  blk("s2.table", "markdown_table", title="The three sectors", revision=True, body=SECTAB),
  C.kc("s2.check", "Making sugar from sugarcane is an activity of which sector?",
    [("secondary sector", ""), ("primary sector", "Growing sugarcane is primary; making sugar is manufacturing."), ("tertiary sector", "Tertiary activities provide services."), ("public sector", "That is a classification by ownership.")],
    "Natural products are changed into other forms through manufacturing."),
  C.kc("s2.check2", "Why do we count only final goods and services in GDP?",
    [("To avoid double counting, as their value already includes the intermediate goods", ""), ("Because intermediate goods have no value", "They have value, but it is included in final goods."),
     ("Because only services are counted", "Goods are counted too."), ("Because the government owns final goods", "Ownership is not the reason.")],
    "Counting wheat, flour and biscuits separately would count the wheat three times."),
 ]},
 {"id": "s3", "title": "Historical change and employment", "blocks": [
  blk("s3.thm", "theory", title="Rising importance of the tertiary sector and underemployment", revision=True,
    body="**Historical change in sectors:** in the initial stages of development, the **primary sector** was the most important sector of economic activity. Over a long time, as methods of farming changed and agriculture began to prosper, people began to take up other activities. When new methods of manufacturing were introduced, factories came up and the **secondary sector** gradually became the most important. In the past 100 years, there has been a further shift from the secondary to the **tertiary sector** in developed countries.\n\n"
         "**India:** over the forty years between **1973–74 and 2013–14**, production increased in all three sectors, but it increased the most in the tertiary sector. In **2013–14**, the tertiary sector emerged as the **largest producing sector** in India, replacing the primary sector.\n\n"
         "**Why the tertiary sector has become so important:**\n"
         "1. In any country, several services such as **hospitals, educational institutions, post and telegraph services, police stations, courts, village administrative offices, municipal corporations, defence, transport, banks and insurance companies** are required. These are basic services, and in a developing country the government has to take responsibility for providing them.\n"
         "2. The development of agriculture and industry leads to the development of services such as **transport, trade and storage**: the greater the development of the primary and secondary sectors, the greater the demand for such services.\n"
         "3. As income levels rise, certain sections of people start demanding many more services like **eating out, tourism, shopping, private hospitals, private schools and professional training**.\n"
         "4. Over the past decade or so, certain new services such as those based on **information and communication technology** have become important and essential.\n"
         "However, not all of the service sector is growing equally well. A large number of workers in this sector, such as **small shopkeepers, repair persons and transport persons**, barely manage to earn a living and have no alternative opportunities for work.\n\n"
         "**Where are most people employed?** Although the primary sector's share of GDP has fallen, it **continues to be the largest employer** in India: nearly half of the workers still work in it. The secondary and tertiary sectors produce most of the GDP but have not generated jobs in the same proportion. **Employment in the service sector has not increased to the same extent as production.**\n\n"
         "**Underemployment (disguised unemployment):** there are **more people in agriculture than necessary**. Consider Laxmi's family of five who work on their small plot of land all year round. Even if two of them move away to do other work, production on the plot will not fall: they are **underemployed**. Each person seems to be working, but no one is fully employed, and their labour effort is divided. This kind of underemployment is **hidden**, in contrast to someone who has no job and is clearly visible as unemployed (**open unemployment**). It is also called **disguised unemployment**. It exists in urban areas too, among **casual workers** such as painters, plumbers, repair persons and street vendors who search for daily work."),
  C.kc("s3.check", "In which year did the tertiary sector become the largest producing sector in India?",
    [("2013–14", ""), ("1973–74", "That was the starting point of the comparison."), ("1947–48", "The primary sector was largest then."), ("1991–92", "It happened in 2013–14.")],
    "It replaced the primary sector."),
  C.kc("s3.check2", "Disguised unemployment means:",
    [("more people work on a job than are needed, so some are not fully employed", ""), ("people have no work at all and are visibly unemployed", "That is open unemployment."),
     ("people work only in factories", "It is common in agriculture."), ("people work in two jobs", "That is not the meaning.")],
    "If some workers leave, production does not fall."),
 ]},
 {"id": "s4", "title": "Creating jobs, organised and unorganised sectors", "blocks": [
  blk("s4.thm", "theory", title="More employment and the conditions of work", revision=True,
    body="**How to create more employment:**\n"
         "- **Irrigation:** if the government builds a dam and canals to irrigate many farms like Laxmi's, a lot of employment can be generated within the agricultural sector itself.\n"
         "- **Transport and storage:** better roads and transport from villages to markets, and storage facilities, help farmers sell crops and create jobs for transporters and traders.\n"
         "- **Cheap credit:** if farmers get loans from banks at a reasonable rate of interest, they can buy seeds, fertilisers and equipment, and grow more.\n"
         "- **Industries and services in semi-rural areas:** setting up industries such as a **dal mill**, cold storage, honey collection and processing of vegetables and fruits can create jobs near villages.\n"
         "- **Education, health and tourism:** a study by the former **Planning Commission** (now **NITI Aayog**) estimated that nearly **20 lakh jobs** can be created in the **education sector** alone. If we improve health services, we need more doctors, nurses and health workers; tourism can also create jobs.\n\n"
         "**MGNREGA 2005:** the central government made a law implementing the **Right to Work** in 625 districts of India, called the **Mahatma Gandhi National Rural Employment Guarantee Act 2005 (MGNREGA 2005)**.\n"
         "- All those who are able to and in need of work in rural areas are **guaranteed 100 days of employment in a year** by the government.\n"
         "- If the government fails in its duty to provide employment, it will give **unemployment allowances** to the people.\n"
         "- **One-third** of the proposed jobs are **reserved for women**.\n"
         "- The types of work that would in future help to **increase production from land** are given preference.\n\n"
         "**Organised and unorganised sectors** (classification by **employment conditions**):\n"
         "- The **organised sector** covers enterprises or places of work where the terms of employment are **regular**, so people have **assured work**. They are **registered by the government** and have to follow its rules and regulations, given in laws such as the **Factories Act, Minimum Wages Act, Payment of Gratuity Act and Shops and Establishments Act**. Workers enjoy **security of employment**, fixed working hours, **overtime** pay, paid leave, payment during holidays, **provident fund, gratuity**, medical benefits and a **pension** after retirement.\n"
         "- The **unorganised sector** is characterised by **small and scattered units** which are largely **outside the control of the government**. There are rules and regulations, but these are not followed. Jobs are **low-paid and often not regular**. There is no provision for overtime, paid leave, holidays or leave due to sickness. Employment is **not secure**: people can be asked to leave without any reason, and work slackens in some seasons.\n"
         "- Since the 1990s, many workers have **lost their jobs in the organised sector** and have been forced to take up jobs in the unorganised sector, with low earnings.\n\n"
         "**Protecting workers in the unorganised sector:** in **rural areas**, the unorganised sector mostly comprises **landless agricultural labourers, small and marginal farmers, sharecroppers and artisans** (weavers, blacksmiths, carpenters and goldsmiths). In **urban areas**, it comprises **casual workers** in small-scale industry, construction, trade and transport, **street vendors, head-load workers, garment makers and rag pickers**. Workers from scheduled castes, tribes and backward communities are often in it. They need protection in terms of **wages, safety and health**, and small producers need support for buying raw materials and marketing output."),
  blk("s4.table", "markdown_table", title="Organised and unorganised sectors", revision=True, body=ORGTAB),
  C.kc("s4.check", "Under MGNREGA 2005, how many days of employment are guaranteed in a year?",
    [("100 days", ""), ("365 days", "It guarantees 100 days."), ("50 days", "It guarantees 100 days."), ("30 days", "It guarantees 100 days.")],
    "If work is not given, an unemployment allowance is paid."),
  C.kc("s4.check2", "Which is a feature of the unorganised sector?",
    [("low-paid and irregular jobs with no paid leave", ""), ("registration with the government and following the Factories Act", "That is the organised sector."),
     ("provident fund and pension", "These are organised sector benefits."), ("fixed hours with overtime pay", "That is the organised sector.")],
    "Workers have no job security."),
 ]},
 {"id": "s5", "title": "Public and private sectors", "blocks": [
  blk("s5.thm", "theory", title="Ownership of enterprises", revision=True,
    body="Another way of classifying economic activities is on the basis of **who owns assets and is responsible for the delivery of services**.\n"
         "- In the **public sector**, the **government owns most of the assets** and provides all the services. **Indian Railways** and the **post office** are examples.\n"
         "- In the **private sector**, ownership of assets and delivery of services is in the hands of **private individuals or companies**. Companies like **Tata Iron and Steel Company Limited (TISCO)** and **Reliance Industries Limited (RIL)** are privately owned.\n"
         "- Activities in the private sector are guided by the motive to **earn profits**. To get such services we have to pay money to these individuals and companies. The purpose of the public sector is **not just to earn profits**; governments raise money through **taxes** and other ways to meet expenses on the services rendered by them.\n\n"
         "**Why the government takes up some activities:**\n"
         "- There are several things needed by the society as a whole which the private sector will not provide at a reasonable cost. Some of these need **spending large sums of money**, which is beyond the capacity of the private sector, and it is not possible to collect money from thousands of people who use these facilities, such as **roads, bridges, railways, harbours, generating electricity and providing irrigation through dams**. Thus, governments take up such heavy spending and ensure that these facilities are available for everyone.\n"
         "- There are some activities which the government has to support. The private sector may not continue production unless the government encourages it: for example, selling **electricity at the cost of generation** may push up the costs of production of goods in many small-scale industries, so the government produces and supplies electricity at rates these industries can afford.\n"
         "- The government in India buys **wheat and rice** from farmers at a **fair price**, stores them in its godowns, and sells them at a **lower price to consumers through ration shops**. The government bears part of the cost. In this way it supports both farmers and consumers.\n"
         "- There are many activities that are the **primary responsibility of the government**: providing **health and education** facilities for all, running proper schools and providing quality education, and taking care of nutrition, especially for children and the poor."),
  C.kc("s5.check", "On what basis are sectors classified into public and private?",
    [("ownership of enterprises", ""), ("employment conditions", "That gives organised and unorganised."), ("nature of economic activity", "That gives primary, secondary and tertiary."), ("number of workers", "This is not the basis.")],
    "Who owns the assets and delivers the services decides it."),
  C.kc("s5.check2", "Why does the government build roads, bridges and dams?",
    [("They need very large spending, and the private sector would not provide them at a reasonable cost for everyone", ""), ("Because the government wants maximum profit", "Profit is not its main purpose."),
     ("Because the private sector is banned from construction", "It is not banned."), ("Because these are primary sector activities", "That is not the reason.")],
    "The government ensures these facilities are available for everyone."),
 ]},
 {"id": "s6", "title": "Remember, avoid, practise", "blocks": [
  blk("s6.memory", "memory_trick", title="Memory tricks",
    body="- **Three ways to classify: \"Nature–Conditions–Owner\"**: nature of activity (primary, secondary, tertiary); employment conditions (organised, unorganised); ownership (public, private).\n"
         "- **P-S-T = Plant, Shape, Transport**: primary grows/extracts, secondary shapes/manufactures, tertiary transports and serves.\n"
         "- **GDP = Final goods only** (biscuits, not flour and wheat).\n- **Tertiary rose because of \"B-D-I-N\"**: Basic services, Development of agriculture and industry, Income rise, New IT services.\n"
         "- **MGNREGA: \"2005, 100 days, 1/3 women, allowance\".**\n- **Organised laws: \"F-M-G-S\"**: Factories, Minimum Wages, Gratuity, Shops and Establishments."),
  blk("s6.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Calling mining a secondary activity: mining is **primary**.\n2. Adding intermediate goods to GDP: only **final goods and services** are counted.\n"
         "3. Saying the tertiary sector is the largest employer: it is the largest **producer**; the **primary** sector is the largest employer.\n"
         "4. Mixing up organised/unorganised with public/private: the first is about **employment conditions**, the second about **ownership**.\n"
         "5. Saying disguised unemployment is visible: it is **hidden**; open unemployment is visible.\n6. Writing that MGNREGA guarantees a job for the whole year: it guarantees **100 days**."),
  blk("s6.tip", "teacher_tip", title="Try this in class",
    body="Ask each student to list the jobs of five adults they know. Sort the list on the board three times: by sector (primary, secondary, tertiary), by employment conditions (organised, unorganised) and by ownership (public, private). Discuss which group is the largest each time."),
  blk("s6.reflection", "reflection", title="Think and explain",
    body="Think of a worker you see every day, such as a vegetable seller, a security guard or a delivery person. Which sector are they in? Do they have job security, paid leave and a pension?"),
  blk("s6.connection", "connection", title="Where this leads",
    body="- **Chapter 1 (Development):** income, jobs and well-being.\n- **Chapter 3 (Money and Credit):** loans for farmers and small producers.\n"
         "- **Geography Chapter 6 (Manufacturing Industries):** the secondary sector in detail."),
  blk("s6.mastery", "mastery", title="Mastery challenge",
    body="'The primary sector is the largest employer, but the tertiary sector is the largest producer.' Explain this situation and suggest two ways to create more jobs, in about 120 words.\n\n"
         "**Model answer:** Over 1973–74 to 2013–14, production rose most in the tertiary sector, which became the largest producing sector in 2013–14. But nearly half of India's workers still work in the primary sector, because the secondary and tertiary sectors did not create jobs in the same proportion as production. "
         "Agriculture therefore has disguised unemployment: more people work on farms than are needed, so removing some would not reduce output. "
         "More jobs can be created by building irrigation, roads and storage in rural areas, by giving farmers cheap credit, and by setting up agro-processing industries like dal mills in semi-rural areas. Expanding education, health and tourism, and schemes like MGNREGA, can also generate employment."),
  blk("s6.summary", "summary", title="Chapter summary",
    body="- Economic activities are primary (natural resources), secondary (manufacturing) and tertiary (services); the sectors are interdependent.\n"
         "- GDP is the value of all final goods and services produced within a country in a year; counting only final goods avoids double counting.\n"
         "- The tertiary sector became the largest producing sector in 2013–14, but the primary sector is still the largest employer, with disguised unemployment.\n"
         "- More jobs can come from irrigation, transport, cheap credit, rural industries, education, health and tourism; MGNREGA guarantees 100 days of work.\n"
         "- The organised sector gives regular, secure jobs with benefits; the unorganised sector has low-paid, insecure work and needs protection.\n"
         "- Public sector enterprises are owned by the government for public welfare; private ones are owned by individuals or companies for profit."),
  blk("s6.examtips", "exam_tips", title="Board exam tips",
    body="- The 2025-26 sample paper asked about the cause of underemployment (more workers than needed; answer A), an example of how the tertiary sector supports the other sectors (a shoe factory relying on transport and retail; answer B), and a 5-mark choice: differences between organised and unorganised sectors, or positive and negative effects of privatisation.\n"
         "- 3/5-mark favourites: three sectors with examples, GDP and final goods, rise of the tertiary sector, disguised unemployment, MGNREGA, organised vs unorganised, public vs private.\n"
         "- In comparison questions, write points in pairs (organised: ... / unorganised: ...)."),
  blk("s6.flash1", "flashcard", front="What is GDP?", back="The value of all final goods and services produced within a country during a particular year."),
  blk("s6.flash2", "flashcard", front="What is disguised unemployment?", back="A situation where more people are working than needed, so some are not fully employed; if they leave, production does not fall."),
  blk("s6.flash3", "flashcard", front="What does MGNREGA 2005 guarantee?", back="100 days of employment in a year to those able and in need of work in rural areas; an allowance if work is not given; one-third of jobs for women."),
  blk("s6.flash4", "flashcard", front="What is the difference between the public and private sector?", back="Public sector: the government owns assets and provides services for public welfare. Private sector: individuals or companies own assets and work for profit."),
 ]},
]

# ---------------- Sample paper ----------------
M("sqp29", EMP, "Underemployment is caused when:",
  [("More workers are employed than actually required", ""), ("Fewer workers are employed than actually required", "That would be a shortage of workers."),
   ("Workers are paid more than their actual output", "That is not underemployment."), ("Jobs are given only to highly educated workers", "That is not the cause.")],
  "When more people work than needed, their effort is divided and no one is fully employed (CBSE marking scheme: A).", "easy", SQP(29), correct=0)
M("sqp31", SEC, "Which of the following examples best demonstrates how the tertiary sector supports both the primary and secondary sectors?",
  [("Farmers grow vegetables and sell them directly to consumers, with no transportation or storage involved.", "No tertiary services are used here."),
   ("A factory makes shoes and uses raw materials like leather to create the product, relying on transport and retail stores to distribute the shoes.", ""),
   ("A bakery bakes bread and uses delivery services to send the bread to local shops for sale, without any direct involvement of raw materials.", "Raw materials from the primary sector are left out."),
   ("A company produces furniture from wood, but does not require any transport or retail services to sell the product.", "No tertiary services are used here.")],
  "Leather (primary) is made into shoes (secondary), and transport and retail (tertiary) support both (CBSE marking scheme: B).", "medium", SQP(31), correct=1)
W("sqp38a", "long_answer", ORG, "A research student spoke with two people, M and N, to learn about their work-related differences. The student concludes that while person M was working in an organised sector, person N was an employee of a workplace that was functioning in an unorganised way. Analyse the key differences between the two sectors that must have enabled the research student to come to this conclusion.",
  ["Regular vs irregular work: M has assured, regular work with fixed terms of employment; N's job is low-paid and often irregular, with no guarantee of continuous work.",
   "Government regulation: M's enterprise is registered and follows laws such as the Factories Act and Minimum Wages Act; N's workplace is largely outside government control, and rules are not followed.",
   "Job security: M has security of employment and clear working hours; N can be dismissed without notice or reason, and work may stop in some seasons.",
   "Benefits: M gets overtime pay, paid leave, holidays, provident fund, gratuity, medical benefits and a pension; N gets no overtime, paid leave or medical benefits.",
   "Working conditions: M's employer must provide a safe environment and facilities such as clean drinking water; N often works in unsafe conditions without legal protection."], source=SQP("38A"))
W("sqp38b", "long_answer", PUB, "Privatisation can have both positive and negative effects on the economy. Support the statement with arguments.",
  ["Positive: privatisation can increase efficiency and productivity, since private firms are driven by competition and profit.",
   "Positive: it can improve the quality of services and reduce the financial burden on the government.",
   "Negative: with profit as the only motive, public welfare may be ignored, and essential services may not reach poor or remote people.",
   "Negative: workers may lose employment security, and the gap between rich and poor may widen when basic facilities become costly.",
   "Negative: private firms are less accountable to the public than the government; so a balance between public and private sectors is needed."], source=SQP("38B"))

# ---------------- NCERT exercises ----------------
M("ex1", EMP, "Employment in the service sector ______ increased to the same extent as production.",
  [("has not", ""), ("has", "Employment has lagged behind production."), ("has more than", "Employment has lagged behind production."), ("has exactly", "Employment has lagged behind production.")],
  "The tertiary sector produces the most, but the primary sector employs the most.", "easy", ex("1"), correct=0)
M("ex2a", PUB, "The sectors are classified into public and private sector on the basis of:",
  [("ownership of enterprises", ""), ("employment conditions", "That gives organised and unorganised sectors."), ("the nature of economic activity", "That gives primary, secondary and tertiary sectors."), ("number of workers employed in the enterprise", "This is not the basis.")],
  "Public: government-owned; private: owned by individuals or companies.", "easy", ex("2"), correct=0)
M("ex2b", SEC, "Production of a commodity, mostly through the natural process, is an activity in the ______ sector.",
  [("primary", ""), ("secondary", "Secondary is manufacturing."), ("tertiary", "Tertiary provides services."), ("information technology", "IT is a tertiary service.")],
  "Agriculture, dairy, fishing and forestry depend on natural processes.", "easy", ex("2"), correct=0)
M("ex2c", GDP, "GDP is the total value of ______ produced during a particular year.",
  [("all final goods and services", ""), ("all goods and services", "Intermediate goods are not counted separately."), ("all intermediate goods and services", "Only final goods and services are counted."), ("all intermediate and final goods and services", "That would be double counting.")],
  "Counting only final goods avoids double counting.", "easy", ex("2"), correct=0)
M("ex3", EMP, "Match the problems faced by the farming sector with the right solutions: (a) unirrigated land, (b) low prices for crops, (c) debt burden, (d) no job in the off season, (e) compelled to sell grains to local traders soon after harvest; with (i) setting up agro-based mills, (ii) cooperative marketing societies, (iii) procurement of food grains by the government, (iv) construction of canals by the government, (v) banks to provide credit with low interest. The correct match is:",
  [("a-iv, b-iii, c-v, d-i, e-ii", ""), ("a-v, b-iii, c-iv, d-i, e-ii", "Unirrigated land needs canals, and debt needs cheap credit."),
   ("a-iv, b-ii, c-v, d-i, e-iii", "Low prices need government procurement; forced sale needs cooperative marketing."), ("a-i, b-iii, c-v, d-iv, e-ii", "Canals solve unirrigated land; mills give off-season jobs.")],
  "Canals for irrigation, procurement for prices, cheap credit for debt, mills for off-season jobs, cooperatives for marketing.", "medium", ex("3"), correct=0)
M("ex4a", SEC, "Find the odd one out: tourist guide, dhobi, tailor, potter.",
  [("potter", ""), ("tourist guide", "A guide provides a service (tertiary)."), ("dhobi", "A dhobi provides a service (tertiary)."), ("tailor", "A tailor provides a service here, unlike the potter who makes goods.")],
  "A potter makes goods (secondary); the others provide services.", "medium", ex("4"), correct=0)
M("ex4b", PUB, "Find the odd one out: postman, cobbler, soldier, police constable.",
  [("cobbler", ""), ("postman", "A postman works in the public sector."), ("soldier", "A soldier works in the public sector."), ("police constable", "A police constable works in the public sector.")],
  "A cobbler is in the private sector; the others work for the government.", "medium", ex("4"), correct=0)
W("ex6", "short_answer", SEC, "Explain the difference between primary, secondary and tertiary sectors using examples other than those mentioned in the text.",
  ["Primary sector: produces goods by using natural resources directly, for example growing tea, catching prawns, or collecting tendu leaves.",
   "Secondary sector: changes natural products into other forms through manufacturing, for example making tea powder in a factory, canning fish, or making furniture from timber.",
   "Tertiary sector: provides services that support production and people, for example a courier service, a mobile phone repair shop, or a tuition teacher."], source=ex("6"))
W("ex7", "very_short_answer", EMP, "Distinguish between open unemployment and disguised unemployment.",
  ["Open unemployment: a person who is able and willing to work has no job, and is clearly visible as unemployed.",
   "Disguised unemployment: people appear to be working, but more people are working than needed; if some leave, production does not fall, as on small family farms."], source=ex("7"))
W("ex8", "short_answer", GDP, "'Tertiary sector is not playing any significant role in the development of the Indian economy.' Do you agree? Give reasons in support of your answer.",
  ["No, I do not agree: in 2013–14 the tertiary sector became the largest producing sector in India, replacing the primary sector.",
   "It provides basic services such as hospitals, schools, banks, transport and communication, and supports agriculture and industry through transport, storage and trade.",
   "New services based on information technology have grown fast; however, employment in this sector has not grown as much as production, and many service workers earn very little."], source=ex("8"))
W("ex9", "very_short_answer", EMP, "Service sector in India employs two different kinds of people. Who are these?",
  ["Highly skilled and educated workers in well-paid services such as banking, IT, finance and professional services.",
   "Workers in small-scale, low-paid services such as small shopkeepers, repair persons, street vendors and transport workers, who barely earn a living."], source=ex("9"))
W("ex10", "short_answer", ORG, "Workers are exploited in the unorganised sector. Do you agree with this view? Give reasons in support of your answer.",
  ["Yes: jobs are low-paid and often irregular, and rules about wages and working conditions are not followed.",
   "There is no provision for overtime, paid leave, holidays or leave due to sickness, and no provident fund or pension.",
   "Employment is not secure: workers can be asked to leave without any reason, and work slackens in some seasons."], source=ex("10"))
W("ex12", "short_answer", ORG, "Compare the employment conditions prevailing in the organised and unorganised sectors.",
  ["Organised: enterprises are registered by the government and follow laws such as the Factories Act; unorganised: small and scattered units largely outside government control.",
   "Organised: regular work, job security, fixed hours and overtime pay; unorganised: low-paid, irregular and insecure work with long hours and no overtime.",
   "Organised: paid leave, provident fund, gratuity, medical benefits and pension; unorganised: none of these benefits."], source=ex("12"))
W("ex13", "short_answer", EMP, "Explain the objective of implementing the MGNREGA 2005.",
  ["MGNREGA 2005 implements the Right to Work in rural India by guaranteeing 100 days of employment in a year to all who are able and in need of work.",
   "If the government fails to give work, it pays an unemployment allowance; one-third of the jobs are reserved for women.",
   "It gives preference to work that increases production from land, such as water conservation, so it also reduces disguised unemployment in villages."], source=ex("13"))
W("ex16", "short_answer", PUB, "Give a few examples of public sector activities and explain why the government has taken them up.",
  ["Examples: railways, post offices, roads, bridges, dams for irrigation, electricity generation, schools and hospitals.",
   "Many of these need very large spending that the private sector cannot afford, and it is not possible to collect money from thousands of users.",
   "The government provides them at a reasonable cost so that they are available for everyone, and supports farmers and consumers, for example through the PDS."], source=ex("16"))
W("ex17", "short_answer", PUB, "Explain how the public sector contributes to the economic development of a nation.",
  ["It provides infrastructure such as roads, railways, harbours, electricity and irrigation that the private sector would not provide at a reasonable cost.",
   "It supplies electricity and other inputs at affordable rates to small industries and buys wheat and rice from farmers at a fair price, selling them cheaply through ration shops.",
   "It provides health, education and nutrition for all, which builds human capital and reduces poverty and inequality."], source=ex("17"))

# ---------------- MCQs ----------------
M("mcq01", SEC, "Which of these is a primary sector activity?",
  [("fishing", ""), ("making bricks", "This is secondary."), ("banking", "This is tertiary."), ("weaving cloth in a mill", "This is secondary.")], "It depends on natural resources.")
M("mcq02", SEC, "Why is the primary sector also called the agriculture and related sector?",
  [("Because most natural products come from agriculture, dairy, fishing and forestry", ""), ("Because it includes all factories", "Factories are secondary."), ("Because it gives services", "Services are tertiary."), ("Because the government owns it", "Ownership is a different classification.")], "Mining is also included.")
M("mcq03", SEC, "The secondary sector is also called the:",
  [("industrial sector", ""), ("service sector", "That is the tertiary sector."), ("agriculture sector", "That is the primary sector."), ("public sector", "That is a classification by ownership.")], "It became associated with industries.")
M("mcq04", SEC, "Which is a tertiary sector activity?",
  [("transporting goods by truck", ""), ("growing rice", "This is primary."), ("making steel", "This is secondary."), ("mining coal", "This is primary.")], "It supports production and generates services.")
M("mcq05", SEC, "If farmers refuse to sell sugarcane to a sugar mill, the mill will shut down. This shows that the sectors are:",
  [("interdependent", ""), ("independent", "They depend on each other."), ("unrelated", "They are closely related."), ("in competition only", "They support each other.")], "Each sector needs the others.")
M("mcq06", GDP, "A farmer sells wheat to a flour mill, which sells flour to a biscuit company, which sells biscuits. Which value is counted in GDP?",
  [("only the value of the biscuits", ""), ("the value of wheat, flour and biscuits added together", "That would be double counting."), ("only the value of the wheat", "Wheat is an intermediate good here."), ("only the value of the flour", "Flour is an intermediate good here.")], "Biscuits are the final good.")
M("mcq07", GDP, "Goods that are used up in producing final goods are called:",
  [("intermediate goods", ""), ("final goods", "Final goods reach the consumer."), ("capital goods only", "The term is intermediate goods."), ("public goods", "That is a different idea.")], "Their value is included in the final good.")
M("mcq08", GDP, "In India, the task of measuring GDP is undertaken by:",
  [("a central government ministry", ""), ("the Reserve Bank of India alone", "A central ministry does it."), ("each village panchayat", "A central ministry does it, with state departments."), ("private companies", "A central ministry does it.")], "It collects information with help from states and union territories.")
M("mcq09", GDP, "In the initial stages of development, the most important sector was the:",
  [("primary sector", ""), ("secondary sector", "It became important later with factories."), ("tertiary sector", "It became important in the last 100 years."), ("IT sector", "That is very recent.")], "Over time, the importance shifted.")
M("mcq10", GDP, "In the past 100 years, developed countries saw a shift from the secondary sector to the:",
  [("tertiary sector", ""), ("primary sector", "The shift was towards services."), ("public sector", "This is about the nature of activity."), ("unorganised sector", "This is about the nature of activity.")], "Services became the most important.")
M("mcq11", GDP, "Between 1973–74 and 2013–14, production in India increased the most in the:",
  [("tertiary sector", ""), ("primary sector", "It grew least."), ("secondary sector", "It grew, but less than tertiary."), ("all equally", "The tertiary sector grew most.")], "It became the largest producing sector in 2013–14.")
M("mcq12", GDP, "Which is NOT a reason for the rising importance of the tertiary sector in India?",
  [("A fall in the demand for services as incomes rise", ""), ("The need for basic services like hospitals and schools", "This is a reason."), ("Development of agriculture and industry needing transport and storage", "This is a reason."), ("Growth of IT-based services", "This is a reason.")], "As incomes rise, the demand for services increases.")
M("mcq13", EMP, "Which sector is the largest employer in India?",
  [("primary sector", ""), ("tertiary sector", "It is the largest producer, not employer."), ("secondary sector", "It employs fewer people."), ("public sector", "This is about ownership.")], "Nearly half the workers work in it.")
M("mcq14", EMP, "Laxmi's family of five works on a small plot. If two members leave for other work, production does not fall. This is an example of:",
  [("disguised unemployment", ""), ("open unemployment", "Here everyone seems to be working."), ("seasonal employment", "This is about too many workers, not seasons."), ("full employment", "Some workers are not needed.")], "It is also called underemployment.")
M("mcq15", EMP, "Disguised unemployment in urban areas is found among:",
  [("casual workers like painters, plumbers and street vendors", ""), ("permanent government officers", "They have regular jobs."), ("bank managers", "They have regular jobs."), ("factory owners", "They are employers.")], "They search for daily work.")
M("mcq16", EMP, "Which would create more jobs within agriculture itself?",
  [("building dams and canals to irrigate more farms", ""), ("closing rural banks", "This would reduce credit."), ("banning farm loans", "This would reduce jobs."), ("stopping road construction", "Roads help farmers.")], "Irrigation allows more crops and more work.")
M("mcq17", EMP, "According to a study by the former Planning Commission, how many jobs can be created in the education sector alone?",
  [("about 20 lakh", ""), ("about 2 lakh", "The estimate is about 20 lakh."), ("about 2 crore", "The estimate is about 20 lakh."), ("about 20,000", "The estimate is about 20 lakh.")], "The Planning Commission is now NITI Aayog.")
M("mcq18", EMP, "Setting up a dal mill in a semi-rural area helps by:",
  [("creating non-farm jobs near villages", ""), ("reducing crop output", "It processes crops."), ("ending the need for transport", "Transport is still needed."), ("replacing all farmers", "It adds jobs.")], "Agro-processing gives off-season work.")
M("mcq19", EMP, "Under MGNREGA, what share of jobs is reserved for women?",
  [("one-third", ""), ("one-half", "It is one-third."), ("one-fourth", "It is one-third."), ("none", "One-third is reserved.")], "It also guarantees 100 days of work.")
M("mcq20", EMP, "If the government fails to provide work under MGNREGA, it must:",
  [("give an unemployment allowance", ""), ("do nothing", "An allowance must be paid."), ("close the scheme", "It must pay an allowance."), ("give a permanent job", "It pays an allowance.")], "The law makes work a right.")
M("mcq21", ORG, "The organised and unorganised sectors are classified on the basis of:",
  [("employment conditions", ""), ("ownership", "That gives public and private."), ("nature of activity", "That gives the three sectors."), ("location", "This is not the basis.")], "Regular, secure work vs irregular, insecure work.")
M("mcq22", ORG, "Which law is followed by organised sector enterprises?",
  [("the Minimum Wages Act", ""), ("the Anti-defection Law", "That is about legislators."), ("the Right to Information Act", "That is about information."), ("the Panchayati Raj Act", "That is about local government.")], "Others are the Factories Act, Payment of Gratuity Act and Shops and Establishments Act.")
M("mcq23", ORG, "Which is NOT a benefit usually received by workers in the organised sector?",
  [("being asked to leave without any reason", ""), ("paid leave", "This is a benefit."), ("provident fund", "This is a benefit."), ("pension after retirement", "This is a benefit.")], "Insecurity is a feature of the unorganised sector.")
M("mcq24", ORG, "Since the 1990s, many workers who lost jobs in the organised sector:",
  [("took up jobs in the unorganised sector with low earnings", ""), ("became factory owners", "Most did not."), ("got government pensions at once", "Most did not."), ("moved to the public sector", "Most moved to the unorganised sector.")], "This increased insecurity.")
M("mcq25", ORG, "Who among these is in the urban unorganised sector?",
  [("a head-load worker", ""), ("a bank officer", "This is the organised sector."), ("a railway engineer", "This is the organised (public) sector."), ("a government teacher", "This is the organised (public) sector.")], "Others include street vendors, garment makers and rag pickers.")
M("mcq26", ORG, "Workers in the unorganised sector need protection mainly in terms of:",
  [("wages, safety and health", ""), ("higher taxes", "Taxes do not protect them."), ("fewer working days", "They need fair wages and safety."), ("more paperwork", "That does not protect them.")], "Small producers also need help with raw materials and marketing.")
M("mcq27", PUB, "Which is an example of a public sector enterprise?",
  [("Indian Railways", ""), ("Reliance Industries Limited", "This is private."), ("Tata Iron and Steel Company", "This is private."), ("a local grocery shop", "This is private.")], "The government owns most of its assets.")
M("mcq28", PUB, "Private sector activities are mainly guided by the motive of:",
  [("earning profits", ""), ("public welfare only", "That is the purpose of the public sector."), ("collecting taxes", "The government collects taxes."), ("giving free services", "Private firms charge money.")], "We pay money to get their services.")
M("mcq29", PUB, "Why does the government buy wheat and rice from farmers at a fair price and sell them cheaply in ration shops?",
  [("To support both farmers and poor consumers", ""), ("To earn large profits", "The government bears part of the cost."), ("To close ration shops", "It runs ration shops."), ("To reduce farm production", "It supports farmers.")], "The government pays part of the cost.")
M("mcq30", PUB, "Which is a primary responsibility of the government?",
  [("providing health and education facilities for all", ""), ("running all grocery shops", "That is not its responsibility."), ("making cars", "That is not its responsibility."), ("owning every factory", "That is not its responsibility.")], "It must also take care of nutrition, especially for children and the poor.")
# ---------------- True / false ----------------
C.tf("tf1", SEC, "Mining is an activity of the secondary sector.", False, "Mining uses natural resources directly, so it is primary.")
C.tf("tf2", GDP, "Only final goods and services are counted in GDP.", True, "This avoids double counting.")
C.tf("tf3", EMP, "The tertiary sector is the largest employer in India.", False, "The primary sector is the largest employer; the tertiary sector is the largest producer.")
C.tf("tf4", ORG, "Workers in the unorganised sector get provident fund and pension.", False, "These are benefits of the organised sector.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", GDP, "What are final goods and intermediate goods? Why are only final goods counted in GDP?",
  ["Final goods reach the consumer, like biscuits; intermediate goods are used up in making final goods, like wheat and flour.", "Only final goods are counted because their value already includes the intermediate goods; counting both would be double counting."])
W("vsa2", "very_short_answer", PUB, "Distinguish between the public sector and the private sector.",
  ["Public sector: the government owns most assets and provides services, for public welfare, like Indian Railways.", "Private sector: individuals or companies own assets and provide services, mainly for profit, like Reliance Industries."])
W("vsa3", "very_short_answer", EMP, "Why has employment not shifted out of the primary sector as much as production?",
  ["The secondary and tertiary sectors have not created enough jobs in proportion to their growth in production.", "So nearly half of the workers remain in agriculture, leading to disguised unemployment."])
W("sa1", "short_answer", GDP, "Why has the tertiary sector become the most important sector in India?",
  ["Basic services like hospitals, schools, post offices, police, courts, banks and transport are needed, and the government provides many of them.",
   "Development of agriculture and industry increases the demand for transport, trade and storage; and as incomes rise, people demand services like eating out, tourism and private schools.",
   "New services based on information and communication technology have become important and have grown fast."])
W("sa2", "short_answer", EMP, "Suggest ways to create more employment in rural areas.",
  ["Build dams and canals for irrigation, and improve roads, transport and storage, so that farmers can grow and sell more.",
   "Give farmers cheap credit from banks, and set up agro-processing industries such as dal mills, cold storage and honey collection in semi-rural areas.",
   "Expand education, health and tourism services, and implement schemes like MGNREGA, which guarantees 100 days of work."])
W("sa3", "short_answer", PUB, "Why does the government take up some economic activities itself?",
  ["Some activities need very large spending, like roads, bridges, railways, harbours, electricity and dams, which the private sector cannot afford or will not provide at a reasonable cost.",
   "The government supports small industries with affordable electricity, and supports farmers and consumers by buying grain at fair prices and selling it cheaply through ration shops.",
   "Health, education and nutrition for all are primary responsibilities of the government."])
W("la1", "long_answer", SEC, "Explain the three sectors of the economy with examples, and show how they are interdependent.",
  ["Primary sector: produces goods by exploiting natural resources, such as agriculture, dairy, fishing, forestry and mining; also called the agriculture and related sector.",
   "Secondary sector: changes natural products into other forms through manufacturing, such as making cloth from cotton or sugar from sugarcane; also called the industrial sector.",
   "Tertiary sector: provides services that support the other sectors and people, such as transport, storage, communication, banking, trade, teaching and IT; also called the service sector.",
   "Interdependence: a sugar mill needs sugarcane from farmers, and if farmers stop selling, the mill shuts down; farmers need fertilisers and tools made in factories.",
   "Both primary and secondary sectors need transport, storage, banking and trade from the tertiary sector to sell their products."])
W("la2", "long_answer", ORG, "Who are the workers in the unorganised sector, and why do they need protection? Suggest ways to protect them.",
  ["In rural areas, the unorganised sector includes landless agricultural labourers, small and marginal farmers, sharecroppers and artisans such as weavers, blacksmiths and carpenters.",
   "In urban areas, it includes casual workers in small industry, construction, trade and transport, street vendors, head-load workers, garment makers and rag pickers.",
   "They need protection because jobs are low-paid, irregular and insecure, with no paid leave, overtime, provident fund or pension, and rules are not followed.",
   "The government should ensure fair wages, safety and health for these workers, and enforce laws like the Minimum Wages Act.",
   "Small producers should get cheap credit and help in buying raw materials and marketing output, and schemes like MGNREGA can give rural workers assured work."])
W("cb1", "case_based", EMP, "Read the source and answer the questions.\n\n*\"Laxmi's family of five works on their small plot of land all through the year. Even if two members of the family move away to do some other work, the production on the plot will not be affected. In other words, more people are working than are actually needed. They are, in a sense, underemployed.\"* (Adapted from NCERT)\n\n"
  "(i) What type of unemployment is described here? (1)\n\n(ii) How is it different from open unemployment? (1)\n\n(iii) Suggest two ways to reduce such unemployment. (2)",
  ["(i) Disguised unemployment (underemployment).", "(ii) Here everyone appears to be working, but some are not needed; in open unemployment, a person clearly has no job.",
   "(iii) Any two: irrigation through dams and canals; cheap credit for farmers; agro-processing industries in semi-rural areas; better transport and storage; MGNREGA works."])
W("cb2", "case_based", ORG, "Read the source and answer the questions.\n\n*\"The organised sector covers those enterprises or places of work where the terms of employment are regular and therefore, people have assured work. They are registered by the government and have to follow its rules and regulations which are given in various laws such as the Factories Act, Minimum Wages Act, Payment of Gratuity Act, Shops and Establishments Act etc.\"* (NCERT)\n\n"
  "(i) Why do workers in the organised sector have assured work? (1)\n\n(ii) Name any one law that organised sector enterprises must follow. (1)\n\n(iii) State two features of the unorganised sector. (2)",
  ["(i) Because the terms of employment are regular and the enterprises are registered and regulated by the government.", "(ii) Any one: Factories Act; Minimum Wages Act; Payment of Gratuity Act; Shops and Establishments Act.",
   "(iii) Any two: small and scattered units outside government control; low-paid and irregular jobs; no paid leave, overtime or holidays; no job security."])
# ---------------- Assertion-reason ----------------
C.arq("ar1", GDP, "Only the value of final goods and services is counted in GDP.", "The value of final goods already includes the value of intermediate goods used to make them.", 0,
      "R explains A.", "this avoids double counting.", "this is why intermediate goods are not added again.")
C.arq("ar2", GDP, "The tertiary sector became the largest producing sector in India in 2013–14.", "The development of agriculture and industry increased the demand for transport, trade and storage.", 0,
      "R explains A (it is one of the reasons for the growth of the tertiary sector).", "it replaced the primary sector.", "this is one reason for its growth.")
C.arq("ar3", EMP, "There is disguised unemployment in Indian agriculture.", "More people work in agriculture than are actually needed.", 0,
      "R explains A.", "some workers are not fully employed.", "this is the definition of disguised unemployment.")
C.arq("ar4", EMP, "The tertiary sector is the largest employer in India.", "Employment in the service sector has not increased to the same extent as production.", 3,
      "A is false: the primary sector is the largest employer. R is true.", "the primary sector employs most people.", "employment has lagged behind production.")
C.arq("ar5", ORG, "Workers in the unorganised sector need protection.", "Their jobs are low-paid, irregular and insecure, with no paid leave or pension.", 0,
      "R explains A.", "they are easily exploited.", "these are the conditions of their work.")
C.arq("ar6", PUB, "The government provides electricity to small industries at affordable rates.", "Private sector activities are guided by the motive to earn profits.", 1,
      "Both are true, but R is a general feature of the private sector; it does not explain why the government supports small industries.", "this keeps their costs low.", "this is a feature of the private sector.")

chapter = header(SUBJ, N, "Sectors of the Indian Economy", ["three_sectors", "gdp_and_sector_shares", "employment", "organised_unorganised", "public_private"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: this chapter is fully in the board examination (Economics: 20 marks). There is no map item from this chapter. NCERT exercises built on local surveys or long data tables (Surat survey, Ahmedabad data, GDP table) are left out; privatisation (sample paper Q38B) is covered with the public and private sectors.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
