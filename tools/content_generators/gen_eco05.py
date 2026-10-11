"""CBSE Class 10 Economics Ch 5: Consumer Rights (project work only in 2025-26; not in the board exam)."""
import sys
from ss_common import make, header, path, SQP, SHINE, CB

ROOT = sys.argv[1]
SUBJ, N = "economics", 5
PATH = path(SUBJ, "ch05_consumer_rights")
C = make(SUBJ, N, "eco10ch05")
blk, M, W = C.blk, C.m, C.w
MKT, MOV, RIGHTS, REDRESS = ["consumers_in_market"], ["consumer_movement"], ["consumer_rights"], ["redressal_and_standards"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 5 exercises", "question": n}

RIGHTSTAB = ("| Right | Meaning | Example |\n|---|---|---|\n| **Right to safety** | protection against goods and services that are hazardous to life and property | a pressure cooker with a faulty safety valve can cause a serious accident |\n"
             "| **Right to be informed** | information about ingredients, price (MRP), batch number, date of manufacture, expiry date and address of the maker | checking the expiry date on medicines |\n"
             "| **Right to choose** | freedom to choose among goods and services; no forced purchase | a gas dealer cannot insist that you buy a stove with a new connection |\n"
             "| **Right to seek redressal** | compensation for unfair trade practices and exploitation | getting a refund or replacement for a defective product |\n"
             "| **Right to represent** | to be heard in consumer protection bodies | consumer representatives in consumer protection councils |\n"
             "| **Right to consumer education** | to learn about rights and how to use them | consumer clubs in schools |")
COMMS = ("| Level | Called | Value of claims it hears (2021 rules) |\n|---|---|---|\n| **District level** | District Consumer Disputes Redressal Commission | up to Rs 50 lakh |\n"
         "| **State level** | State Commission | above Rs 50 lakh up to Rs 2 crore |\n| **National level** | National Commission (New Delhi) | above Rs 2 crore |")

sections = [
 {"id": "s1", "title": "Consumers in the marketplace", "blocks": [
  blk("s1.hook", "hook", title="An expired packet",
    body="You buy a packet of biscuits and find, at home, that it is past its expiry date. Another time, a shopkeeper charges you more than the printed price, or a new scooter's brakes fail. What can you do?\n\n"
         "Every one of us is a **consumer**. This chapter explains how consumers can be exploited, how the consumer movement grew in India, what our rights are, and where we can go for justice. **Note:** in 2025-26 this chapter is for the **project work** (Consumer Rights), not for the board examination."),
  blk("s1.inspiration", "inspiration", title="Consumers have rights", person="John F. Kennedy", years="1917–1963",
    body="On **15 March 1962**, US President **John F. Kennedy** told the US Congress that consumers have basic rights, including the right to safety, the right to be informed, the right to choose and the right to be heard. This idea spread around the world.\n\n"
         "Today, **15 March** is observed as **World Consumer Rights Day**. In India, **24 December** is **National Consumers' Day**, the day the Consumer Protection Act was passed in **1986**.",
    future="This chapter leads to careers in consumer law, quality control, standards testing, journalism and public administration."),
  C.socratic("s1.socratic", "Why might a consumer be cheated more easily by a big company than by a neighbour who sells goods?",
    ["Because big companies have more information, power and money than an individual consumer", "Because big companies always sell bad goods", "Because consumers never complain"], 0,
    "When producers are few and powerful, and consumers lack information, exploitation becomes easier."),
 ]},
 {"id": "s2", "title": "Exploitation and the consumer movement", "blocks": [
  blk("s2.thm", "theory", title="Why rules are needed and how the consumer movement grew", revision=True,
    body="**Consumers in the marketplace:** we participate in the market both as **producers** and as **consumers**. As consumers, we buy goods and services for final use. Individual consumers often find themselves in a **weak position**: whenever there is a complaint about a good or service, the seller tries to shift the responsibility to the buyer, as if the seller has no responsibility once the sale is complete.\n\n"
         "**Ways in which consumers are exploited:**\n"
         "- **Weighing less** than they should, or **adding extra charges**.\n- **Adulteration** (for example, of edible oil, butter and ghee) and **defective goods**.\n"
         "- **Selling expired goods** or charging more than the **maximum retail price (MRP)**.\n- **False or incomplete information** in advertisements, and **poor after-sales service**.\n\n"
         "**Factors that cause exploitation:** **limited information** with consumers; **limited supplies**, which lead to hoarding and black marketing; **limited competition**, when one or a few producers control the market; and **low literacy**, which makes consumers unaware of their rights.\n\n"
         "**Why rules and regulations are needed:** markets do not always work in a fair manner. Large companies with huge wealth, power and reach can manipulate the market in various ways, and false information is passed on through the media to attract consumers. Rules and regulations are required to **protect consumers**. For example, a company may sell a product for years even when it is known to be harmful; rules make companies take responsibility.\n\n"
         "**The consumer movement in India:** it arose out of **dissatisfaction** of consumers, as many unfair practices were being indulged in by sellers.\n"
         "- In the **1960s**, there was rampant **food shortage, hoarding, black marketing and adulteration** of food and edible oil. This gave birth to the consumer movement in an **organised form**.\n"
         "- Till the 1970s, consumer organisations were largely engaged in **writing articles** and holding **exhibitions**. They formed **consumer groups** to look into the malpractices in ration shops and overcrowding in road passenger transport.\n"
         "- In **1986**, the Indian government enacted the **Consumer Protection Act (COPRA)**. This was a major step. It has now been replaced by the **Consumer Protection Act, 2019**.\n"
         "- **Consumers International:** in **1985**, the United Nations adopted the **UN Guidelines for Consumer Protection**. Consumers International (earlier the International Organisation of Consumers Unions) has become an umbrella body of over **200 member organisations** from more than **100 countries**, including India."),
  C.kc("s2.check", "Which is NOT a factor that causes exploitation of consumers?",
    [("full and correct information with consumers", ""), ("limited information", "This causes exploitation."), ("limited competition", "This causes exploitation."), ("low literacy", "This causes exploitation.")],
    "Well-informed consumers are harder to cheat."),
  C.kc("s2.check2", "In which year did India enact the Consumer Protection Act (COPRA)?",
    [("1986", ""), ("1947", "That is independence."), ("2005", "That is the RTI Act."), ("1962", "That is Kennedy's speech on consumer rights.")],
    "It has been replaced by the Consumer Protection Act, 2019."),
 ]},
 {"id": "s3", "title": "Consumer rights", "blocks": [
  blk("s3.thm", "theory", title="The rights of consumers", revision=True,
    body="**1. Right to safety:** consumers have the right to be protected against the marketing of goods and delivery of services that are **hazardous to life and property**. Many goods and services, such as pressure cookers, electrical appliances, cars and medicines, need special attention to safety. Producers must follow **safety rules and regulations**.\n\n"
         "**2. Right to be informed:** when we buy a commodity, we find details given on the packing: **ingredients, price, batch number, date of manufacture, expiry date and address** of the manufacturer. When we buy medicines, we find 'directions for proper use' and information on side effects. Consumers have the right to be informed about the particulars of the goods and services they buy, so that they can **complain and ask for compensation** if the product proves defective. If a seller charges more than the **MRP** printed on the packet, consumers can protest and complain.\n"
         "- The **Right to Information (RTI) Act**, passed in **October 2005**, ensures citizens all the information about the functions of **government departments**.\n\n"
         "**3. Right to choose:** any consumer who receives a service, in whatever capacity, regardless of age, gender and nature of service, has the right to **choose** whether to continue to receive the service. Sometimes we are **forced** to buy things we do not want: for example, a gas supply dealer may insist that you buy a **gas stove** from him when you take a new connection. This denies the right to choose.\n\n"
         "**4. Right to seek redressal:** consumers have the right to seek redressal against **unfair trade practices and exploitation**. If any damage is done to a consumer, she has the right to get **compensation** depending on the degree of damage.\n\n"
         "**5. Right to represent:** consumers have the right to be represented in the **consumer protection councils** and to be heard. The Act has enabled consumers to have this right.\n\n"
         "**6. Right to consumer education:** consumers should know their rights and be able to use them. Schools have **consumer clubs**, and the government uses media campaigns such as **'Jago Grahak Jago'** to spread awareness.\n\n"
         "**Duties of consumers (taking part):** check the **quality and price**, look for **standard marks**, ask for a **bill** (cash memo) for every purchase, read the **expiry date**, and **complain** about genuine grievances. Consumers can also express **solidarity** by forming **consumer groups and voluntary organisations**."),
  blk("s3.table", "markdown_table", title="Rights of consumers", revision=True, body=RIGHTSTAB),
  C.kc("s3.check", "A dealer insists that you buy a gas stove from him to get a new gas connection. Which right is denied?",
    [("right to choose", ""), ("right to safety", "This is about forced purchase, not danger."), ("right to represent", "This is about being heard in councils."), ("right to education", "This is about awareness.")],
    "Consumers must be free to choose what they buy.")
  ,C.kc("s3.check2", "Information printed on a packet such as MRP, ingredients and expiry date relates to the:",
    [("right to be informed", ""), ("right to seek redressal", "That is about compensation."), ("right to choose", "That is about free choice."), ("right to represent", "That is about being heard.")],
    "Consumers can complain if the seller charges more than the MRP.")
 ]},
 {"id": "s4", "title": "Where to go for justice, and standard marks", "blocks": [
  blk("s4.thm", "theory", title="Consumer commissions and standardisation", revision=True,
    body="**Consumer commissions:** under the Consumer Protection Act, a **three-tier quasi-judicial machinery** has been set up at the **district, state and national levels** to settle consumer disputes. These bodies are popularly called **consumer courts**.\n"
         "- The **District Consumer Disputes Redressal Commission** deals with cases involving claims up to **Rs 50 lakh** (as per the 2021 rules under the 2019 Act).\n"
         "- The **State Commission** deals with claims above Rs 50 lakh and up to **Rs 2 crore**.\n"
         "- The **National Commission** in New Delhi deals with claims above **Rs 2 crore**.\n"
         "- If a case is dismissed at the district level, the consumer can **appeal** in the State Commission and then in the National Commission.\n"
         "- Consumers can file complaints themselves; they do not always need a lawyer. Consumer groups also **guide consumers** on how to file cases and often **represent** them.\n\n"
         "**Standardisation of products:** standard marks help consumers be assured of quality while buying goods.\n"
         "- **ISI mark:** given by the **Bureau of Indian Standards (BIS)** for industrial and consumer goods.\n"
         "- **Agmark:** for **agricultural products** such as edible oil, cereals and honey.\n"
         "- **Hallmark:** for **gold and silver jewellery**, certified by BIS.\n"
         "- **ISO:** international standards for quality.\n"
         "- For some products that affect the **health and safety** of consumers, such as **LPG cylinders, food colours and additives, cement and packaged drinking water**, it is **mandatory** for producers to get certified by these organisations.\n\n"
         "**Progress of the consumer movement:** **24 December** is observed as **National Consumers' Day** in India, as COPRA was passed on this day in 1986. India has hundreds of consumer groups, but only a few are well organised. The redressal process is often **cumbersome, expensive and time-consuming**; many consumers do not keep bills, and laws are not always enforced. So consumers need to be **aware and active**, and the movement needs voluntary effort and participation of all."),
  blk("s4.table", "markdown_table", title="Three-tier consumer commissions", revision=True, body=COMMS),
  C.kc("s4.check", "Which mark would you look for on a bottle of honey?",
    [("Agmark", ""), ("Hallmark", "Hallmark is for jewellery."), ("ISO", "ISO is an international quality standard, but Agmark certifies agricultural produce like honey."), ("no mark is needed", "Standard marks assure quality.")],
    "Agmark certifies agricultural products such as honey, edible oil and cereals.")
  ,C.kc("s4.check2", "A consumer court at the district level is called the:",
    [("District Consumer Disputes Redressal Commission", ""), ("District Court for Crimes", "Consumer cases go to consumer commissions."), ("Panchayat Samiti", "That is local government."), ("Election Commission", "That conducts elections.")],
    "It is the first level of the three-tier system.")
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Six rights \"S-I-C-R-R-E\"**: Safety, Information, Choice, Redressal, Representation, Education.\n- **Exploitation factors \"Info, Supply, Competition, Literacy\"** (all limited/low).\n"
         "- **Dates: COPRA 1986 (24 December = National Consumers' Day); CPA 2019; RTI 2005; 15 March = World Consumer Rights Day.**\n"
         "- **Marks: ISI = industry, Agmark = agriculture, Hallmark = jewellery.**\n- **Three tiers: District → State → National.**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Using Hallmark for honey: honey and edible oil carry **Agmark**; Hallmark is for **jewellery**.\n2. Saying consumer courts are ordinary criminal courts: they are **quasi-judicial consumer commissions**.\n"
         "3. Mixing up National Consumers' Day (**24 December**, India) with World Consumer Rights Day (**15 March**).\n4. Thinking a consumer must pay more than MRP: charging **above MRP** is unfair and can be challenged.\n"
         "5. Forgetting that this chapter is for the **project**, not the board exam, in 2025-26."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Ask students to bring five empty packets (food, medicine, cosmetics). In groups, list the MRP, date of manufacture, expiry date, standard mark and customer care number on each. Discuss which right each item of information supports. This can start the consumer rights project."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Have you or your family ever been overcharged or sold a defective product? What did you do? Which consumer right could you have used?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Chapter 3 (Money and Credit):** fair terms of credit for consumers.\n- **Chapter 4 (Globalisation):** many brands and choices in the market.\n"
         "- **Political Science Chapter 5 (Outcomes of Democracy):** the Right to Information and accountability."),
  blk("s5.mastery", "mastery", title="Mastery challenge (project starter)",
    body="'An aware consumer is a protected consumer.' Explain in about 120 words.\n\n"
         "**Model answer:** Consumers are exploited through under-weighing, adulteration, defective goods, charging above MRP and misleading advertisements, mainly because of limited information, limited supplies, limited competition and low literacy. "
         "An aware consumer checks the MRP, ingredients, date of manufacture and expiry date, looks for standard marks such as ISI, Agmark and Hallmark, and asks for a bill. "
         "Such a consumer knows the rights to safety, information, choice, redressal, representation and education, and can approach the district, state or national consumer commission under the Consumer Protection Act, 2019. Consumer groups help by guiding and representing consumers. Awareness therefore turns rights on paper into real protection."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Consumers are often in a weak position and can be exploited through under-weighing, adulteration, defective goods, charging above MRP and false information.\n"
         "- Exploitation is caused by limited information, limited supplies, limited competition and low literacy; rules are needed to protect consumers.\n"
         "- The consumer movement grew from the 1960s; COPRA was enacted in 1986 and replaced by the Consumer Protection Act, 2019.\n"
         "- Consumers have rights to safety, information, choice, redressal, representation and education; the RTI Act 2005 gives information about government work.\n"
         "- Three-tier consumer commissions (district, state, national) settle disputes; ISI, Agmark and Hallmark assure quality.\n"
         "- In 2025-26, this chapter is for project work, not the board exam."),
  blk("s5.examtips", "exam_tips", title="Project tips",
    body="- In 2025-26, Consumer Rights is one of the **project** options (internally assessed); it is **not** in the board examination.\n"
         "- A good project includes a survey of packets and bills, a case study of a real consumer complaint, the six consumer rights with examples, and the three-tier redressal system.\n"
         "- Keep the bills and photos of labels you collect as evidence in your project file."),
  blk("s5.flash1", "flashcard", front="Name the six consumer rights.", back="Right to safety, to be informed, to choose, to seek redressal, to represent, and to consumer education."),
  blk("s5.flash2", "flashcard", front="When is National Consumers' Day in India?", back="24 December, the day the Consumer Protection Act was passed in 1986."),
  blk("s5.flash3", "flashcard", front="What do ISI, Agmark and Hallmark certify?", back="ISI: industrial and consumer goods (BIS). Agmark: agricultural products. Hallmark: gold and silver jewellery."),
  blk("s5.flash4", "flashcard", front="What are the three tiers of consumer commissions?", back="District Commission, State Commission and National Commission."),
 ]},
]

# ---------------- NCERT exercises ----------------
W("ex1", "short_answer", MKT, "Why are rules and regulations required in the marketplace? Illustrate with a few examples.",
  ["Individual consumers are in a weak position, while large companies with wealth and power can manipulate the market.",
   "Without rules, sellers may under-weigh goods, adulterate food, sell expired or defective products, or charge more than the MRP.",
   "Rules such as safety standards and the Consumer Protection Act make producers responsible and give consumers a way to seek redressal."], source=ex("1"))
W("ex2", "short_answer", MOV, "What factors gave birth to the consumer movement in India? Trace its evolution.",
  ["The movement arose from consumer dissatisfaction with unfair practices; in the 1960s there was food shortage, hoarding, black marketing and adulteration of food and edible oil.",
   "Till the 1970s, consumer organisations mainly wrote articles and held exhibitions, and formed consumer groups to check malpractices in ration shops and road transport.",
   "In 1986 the government enacted COPRA, now replaced by the Consumer Protection Act, 2019, which set up consumer commissions; India is also part of Consumers International."], source=ex("2"))
W("ex3", "very_short_answer", RIGHTS, "Explain the need for consumer consciousness by giving two examples.",
  ["A conscious consumer checks the expiry date and MRP, so cannot be sold expired medicine or charged above the printed price.",
   "A conscious consumer looks for standard marks like ISI or Agmark and keeps the bill, so can claim a replacement or compensation for a defective product."], source=ex("3"))
W("ex4", "very_short_answer", MKT, "Mention a few factors which cause exploitation of consumers.",
  ["Limited information about products, and low literacy and awareness among consumers.", "Limited supplies (leading to hoarding and black marketing) and limited competition, where a few producers control the market."], source=ex("4"))
W("ex5", "short_answer", MOV, "What is the rationale behind the enactment of the Consumer Protection Act 1986?",
  ["Consumers were being exploited through adulteration, defective goods, high prices and false information, and had no easy way to get justice.",
   "The Act aimed to protect consumers' rights and make producers and sellers responsible for their goods and services.",
   "It set up a three-tier quasi-judicial machinery (district, state and national) for simple, quick and inexpensive redressal of consumer disputes."], source=ex("5"))
W("ex6", "very_short_answer", RIGHTS, "Describe some of your duties as consumers if you visit a shopping complex in your locality.",
  ["Check the quality, MRP, expiry date and standard mark (ISI, Agmark) of products before buying.", "Ask for a proper bill for every purchase and complain to the right authority about genuine grievances."], source=ex("6"))
W("ex7", "very_short_answer", REDRESS, "Suppose you buy a bottle of honey and a biscuit packet. Which logo or mark will you have to look for and why?",
  ["For honey (an agricultural product), look for the Agmark; for biscuits (a processed food product), look for the ISI or FSSAI food safety mark.",
   "These marks assure that the products meet quality and safety standards."], source=ex("7"))
W("ex8", "short_answer", REDRESS, "What legal measures were taken by the government to empower the consumers in India?",
  ["The Consumer Protection Act, 1986 (COPRA), now replaced by the Consumer Protection Act, 2019, protects consumer rights.",
   "A three-tier system of consumer commissions at the district, state and national levels was set up to settle disputes.",
   "The Right to Information Act, 2005 gives citizens information about government departments, and standardisation bodies like BIS certify products."], source=ex("8"))
W("ex9", "long_answer", RIGHTS, "Mention some of the rights of consumers and write a few sentences on each.",
  ["Right to safety: protection against goods and services hazardous to life and property, such as faulty electrical appliances or pressure cookers.",
   "Right to be informed: information on ingredients, price, date of manufacture, expiry date and address of the maker, so consumers can complain about defective products.",
   "Right to choose: freedom to choose goods and services without forced purchase, for example a gas dealer cannot force you to buy a stove.",
   "Right to seek redressal: compensation for unfair trade practices and exploitation, depending on the degree of damage.",
   "Right to represent and right to consumer education: to be heard in consumer protection councils, and to learn about rights through consumer clubs and campaigns."], source=ex("9"))
W("ex10", "very_short_answer", MOV, "By what means can the consumers express their solidarity?",
  ["By forming consumer groups and voluntary consumer organisations.", "By joining consumer clubs and campaigns, and by supporting each other in filing complaints in consumer commissions."], source=ex("10"))
W("ex11", "short_answer", MOV, "Critically examine the progress of the consumer movement in India.",
  ["Progress: COPRA (1986) and the Consumer Protection Act, 2019 set up consumer commissions, and 24 December is observed as National Consumers' Day; many consumer groups guide and represent consumers.",
   "Limitations: the redressal process is often cumbersome, expensive and time-consuming, and many consumers do not keep bills or know their rights.",
   "Only a few consumer groups are well organised, and laws are not always enforced; so awareness and voluntary participation must increase."], source=ex("11"))
M("ex12a", REDRESS, "Agmark certifies:",
  [("agricultural products such as edible oil and cereals", ""), ("gold jewellery", "That is Hallmark."), ("electrical appliances", "That is ISI."), ("cement", "That is under BIS (ISI).")],
  "Agmark is the mark for agricultural produce.", "easy", ex("12"), correct=0)
M("ex12b", RIGHTS, "Availing details of the ingredients of a product relates to the:",
  [("right to information", ""), ("right to safety", "Safety is about protection from hazards."), ("right to choose", "Choice is about free selection."), ("right to represent", "That is about being heard.")],
  "Consumers have the right to know what they buy.", "easy", ex("12"), correct=0)
M("ex12c", RIGHTS, "An accident due to a faulty engine in a scooter relates to the:",
  [("right to safety", ""), ("right to choose", "This is about danger, not choice."), ("right to education", "This is about danger."), ("right to represent", "This is about danger.")],
  "Products must not be hazardous to life and property.", "easy", ex("12"), correct=0)
M("ex12d", MOV, "Consumers International is:",
  [("a global-level institution of consumer welfare organisations", ""), ("an Indian consumer court", "It is international."), ("a government department of India", "It is an international body."), ("a company that sells goods worldwide", "It is a consumer body.")],
  "It is an umbrella body of over 200 member organisations from more than 100 countries.", "medium", ex("12"), correct=0)
M("ex12e", REDRESS, "The Bureau of Indian Standards (BIS) is responsible for:",
  [("certification of standards for goods", ""), ("collecting taxes", "That is the tax department."), ("issuing currency", "That is the RBI."), ("conducting elections", "That is the Election Commission.")],
  "It gives the ISI mark and the Hallmark.", "easy", ex("12"), correct=0)

# ---------------- MCQs ----------------
M("mcq01", MKT, "When there is a complaint about a product, sellers often:",
  [("try to shift the responsibility to the buyer", ""), ("always give a refund at once", "Many sellers avoid responsibility."), ("call the consumer court themselves", "They do not."), ("double the warranty", "That is not common.")], "Consumers are often in a weak position.")
M("mcq02", MKT, "Mixing a cheaper substance into edible oil or ghee is called:",
  [("adulteration", ""), ("standardisation", "That is ensuring quality."), ("redressal", "That is getting justice."), ("hallmarking", "That certifies jewellery.")], "It harms consumers' health and pockets.")
M("mcq03", MKT, "Charging more than the price printed on a packet means charging above the:",
  [("maximum retail price (MRP)", ""), ("minimum support price", "That is a price for farmers."), ("cost price", "That is the seller's cost."), ("wholesale price", "That is the bulk price.")], "Consumers can complain about it.")
M("mcq04", MKT, "Limited supplies of a product often lead to:",
  [("hoarding and black marketing", ""), ("lower prices for everyone", "Shortages raise prices."), ("better quality", "Not necessarily."), ("more competition", "Supplies are limited.")], "This was common in the 1960s.")
M("mcq05", MKT, "When one or a few producers control the market, consumers face:",
  [("limited competition", ""), ("perfect competition", "There are few producers."), ("free goods", "Goods are not free."), ("more information", "They often get less.")], "This makes exploitation easier.")
M("mcq06", MOV, "The consumer movement in India took an organised form in the 1960s because of:",
  [("food shortage, hoarding, black marketing and adulteration", ""), ("too many consumer courts", "Courts came later."), ("the RTI Act", "That came in 2005."), ("globalisation", "That came later.")], "Consumers were dissatisfied.")
M("mcq07", MOV, "Till the 1970s, consumer organisations in India mainly:",
  [("wrote articles and held exhibitions", ""), ("ran consumer courts", "Courts came after 1986."), ("issued standard marks", "That is BIS's work."), ("made laws", "Parliament makes laws.")], "They also formed consumer groups.")
M("mcq08", MOV, "COPRA has now been replaced by the:",
  [("Consumer Protection Act, 2019", ""), ("Right to Information Act, 2005", "That is about government information."), ("Factories Act", "That is about workplaces."), ("Essential Commodities Act only", "It is the Consumer Protection Act, 2019.")], "COPRA was enacted in 1986.")
M("mcq09", MOV, "National Consumers' Day in India is observed on:",
  [("24 December", ""), ("15 March", "That is World Consumer Rights Day."), ("26 January", "That is Republic Day."), ("5 June", "That is World Environment Day.")], "COPRA was passed on this day in 1986.")
M("mcq10", MOV, "World Consumer Rights Day is observed on:",
  [("15 March", ""), ("24 December", "That is India's National Consumers' Day."), ("1 May", "That is Labour Day."), ("10 December", "That is Human Rights Day.")], "It recalls Kennedy's speech of 15 March 1962.")
M("mcq11", MOV, "The UN Guidelines for Consumer Protection were adopted in:",
  [("1985", ""), ("1947", "The UN was new then."), ("2019", "That is India's new Act."), ("1962", "That was Kennedy's speech.")], "Consumers International grew as a global body.")
M("mcq12", RIGHTS, "Protection against goods hazardous to life and property is the:",
  [("right to safety", ""), ("right to choose", "That is about free choice."), ("right to represent", "That is about being heard."), ("right to education", "That is about awareness.")], "Producers must follow safety rules.")
M("mcq13", RIGHTS, "Which information must be printed on a packet so that consumers are informed?",
  [("ingredients, MRP, date of manufacture and expiry date", ""), ("the seller's personal phone number only", "Packaging gives product details."), ("the shopkeeper's profit", "This is not required."), ("the worker's salary", "This is not required.")], "This supports the right to be informed.")
M("mcq14", RIGHTS, "The RTI Act of 2005 ensures citizens information about:",
  [("the functions of government departments", ""), ("private companies' profits", "It covers government departments."), ("neighbours' incomes", "It covers government departments."), ("film releases", "It covers government departments.")], "It extends the right to be informed.")
M("mcq15", RIGHTS, "Getting compensation for a defective product is linked to the:",
  [("right to seek redressal", ""), ("right to safety", "Safety is about protection."), ("right to choose", "Choice is about selection."), ("right to be informed", "That is about details.")], "Compensation depends on the degree of damage.")
M("mcq16", RIGHTS, "Being heard in consumer protection councils is the:",
  [("right to represent", ""), ("right to safety", "Safety is about hazards."), ("right to choose", "Choice is about selection."), ("right to be informed", "That is about details.")], "The Act enables this right.")
M("mcq17", RIGHTS, "Which campaign spreads consumer awareness in India?",
  [("Jago Grahak Jago", ""), ("Swachh Bharat only", "That is about cleanliness."), ("Make in India only", "That is about manufacturing."), ("Beti Bachao only", "That is about girls.")], "This supports the right to consumer education.")
M("mcq18", RIGHTS, "Which is a duty of a consumer?",
  [("asking for a bill for every purchase", ""), ("never checking the expiry date", "Consumers should check it."), ("paying above MRP happily", "Consumers should not."), ("ignoring standard marks", "Consumers should look for them.")], "A bill helps when filing a complaint.")
M("mcq19", RIGHTS, "Consumers can express solidarity by:",
  [("forming consumer groups and voluntary organisations", ""), ("buying only expired goods", "That harms consumers."), ("avoiding complaints", "Complaints help."), ("paying extra charges", "That is exploitation.")], "Groups guide and represent consumers.")
M("mcq20", REDRESS, "The three-tier consumer redressal machinery works at:",
  [("district, state and national levels", ""), ("village, block and district levels", "It is district, state and national."), ("only the national level", "There are three levels."), ("panchayat and municipal levels", "These are local governments.")], "These are popularly called consumer courts.")
M("mcq21", REDRESS, "Under the 2021 rules, the District Commission hears claims up to:",
  [("Rs 50 lakh", ""), ("Rs 10 crore", "That was an older limit for the State Commission."), ("Rs 5,000", "It is much higher."), ("no limit", "There is a limit.")], "Above that, cases go to the State or National Commission.")
M("mcq22", REDRESS, "Under the 2021 rules, the National Commission hears claims above:",
  [("Rs 2 crore", ""), ("Rs 50 lakh", "That is the District Commission limit."), ("Rs 1,000", "It is much higher."), ("Rs 100 crore only", "It is above Rs 2 crore.")], "It sits in New Delhi.")
M("mcq23", REDRESS, "If a case is dismissed at the district level, the consumer can:",
  [("appeal to the State Commission and then the National Commission", ""), ("never appeal", "Appeals are allowed."), ("go only to the police", "Consumer commissions handle appeals."), ("appeal to the panchayat", "Panchayats do not hear consumer appeals.")], "This is the benefit of the three-tier system.")
M("mcq24", REDRESS, "The ISI mark is given by:",
  [("the Bureau of Indian Standards", ""), ("the RBI", "The RBI is the central bank."), ("the Election Commission", "It conducts elections."), ("Consumers International", "It is a global consumer body.")], "It certifies industrial and consumer goods.")
M("mcq25", REDRESS, "Which mark is used for gold jewellery?",
  [("Hallmark", ""), ("Agmark", "That is for agricultural products."), ("ISI", "ISI is for industrial goods."), ("no mark", "Hallmark is used.")], "BIS certifies it.")
M("mcq26", REDRESS, "For which product is certification mandatory because it affects health and safety?",
  [("LPG cylinders", ""), ("notebooks", "Not mandatory in this list."), ("pencils", "Not mandatory in this list."), ("greeting cards", "Not mandatory in this list.")], "Others include food colours and additives, cement and packaged drinking water.")
M("mcq27", REDRESS, "ISO refers to:",
  [("international standards for quality", ""), ("an Indian consumer court", "It is an international standard."), ("a type of tax", "It is a standard."), ("a bank loan", "It is a standard.")], "It is used across countries.")
M("mcq28", MOV, "A major weakness of the consumer redressal process is that it is often:",
  [("cumbersome, expensive and time-consuming", ""), ("too fast", "It is often slow."), ("completely free and instant", "It can be costly and slow."), ("closed to all consumers", "It is open to consumers.")], "Awareness and simpler processes are needed.")
M("mcq29", MOV, "Why do many consumers fail to get justice?",
  [("They do not keep bills or know their rights", ""), ("Consumer courts do not exist", "They exist at three levels."), ("Complaints are illegal", "Complaints are allowed."), ("All sellers are honest", "Exploitation happens.")], "Awareness is the key.")
M("mcq30", RIGHTS, "A pressure cooker with a faulty safety valve violates the consumer's:",
  [("right to safety", ""), ("right to choose", "This is about danger."), ("right to represent", "This is about danger."), ("right to education", "This is about danger.")], "Such goods can cause serious accidents.")
# ---------------- True / false ----------------
C.tf("tf1", REDRESS, "Agmark is used for gold jewellery.", False, "Agmark is for agricultural products; Hallmark is for jewellery.")
C.tf("tf2", MOV, "National Consumers' Day is observed on 24 December in India.", True, "COPRA was passed on this day in 1986.")
C.tf("tf3", RIGHTS, "A seller may charge more than the MRP printed on a packet.", False, "Charging above MRP is unfair and consumers can complain.")
C.tf("tf4", REDRESS, "Consumer disputes are settled by a three-tier system of district, state and national commissions.", True, "These are popularly called consumer courts.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", MKT, "Give two ways in which consumers are exploited in the market.",
  ["Any one: under-weighing goods or adding extra charges; adulteration of food such as edible oil and ghee.", "Any other: selling expired or defective goods; charging above MRP; false advertisements; poor after-sales service."])
W("vsa2", "very_short_answer", REDRESS, "What are ISI, Agmark and Hallmark?",
  ["ISI is the BIS mark for industrial and consumer goods; Agmark is for agricultural products like edible oil, cereals and honey.", "Hallmark certifies the purity of gold and silver jewellery."])
W("vsa3", "very_short_answer", RIGHTS, "Why should consumers ask for a bill?",
  ["A bill is proof of purchase, showing the product, price and date.", "It is needed to claim a replacement, refund or compensation and to file a complaint in a consumer commission."])
W("sa1", "short_answer", RIGHTS, "Explain the right to be informed with examples.",
  ["Consumers have the right to know the ingredients, price (MRP), batch number, date of manufacture, expiry date and address of the maker of a product.",
   "Medicines must carry directions for use and information on side effects.",
   "This helps consumers choose wisely and complain if a product is defective or if they are charged above MRP; the RTI Act 2005 extends this right to government information."])
W("sa2", "short_answer", REDRESS, "Describe the three-tier consumer redressal system in India.",
  ["Under the Consumer Protection Act, consumer disputes are settled by quasi-judicial commissions at the district, state and national levels.",
   "Under the 2021 rules, the District Commission hears claims up to Rs 50 lakh, the State Commission above Rs 50 lakh up to Rs 2 crore, and the National Commission above Rs 2 crore.",
   "A consumer can appeal from the district to the state and then to the national level; consumer groups help consumers file cases."])
W("sa3", "short_answer", MKT, "What factors make consumers easy to exploit?",
  ["Limited information about products and their quality, and low literacy and awareness of rights.",
   "Limited supplies, which lead to hoarding and black marketing.",
   "Limited competition, when a few big producers control the market and use their wealth and power, including misleading advertisements."])
W("la1", "long_answer", MOV, "Trace the growth of the consumer movement in India.",
  ["The movement arose from consumer dissatisfaction with unfair trade practices by sellers.",
   "In the 1960s, food shortage, hoarding, black marketing and adulteration of food and edible oil gave birth to an organised consumer movement.",
   "Till the 1970s, consumer organisations wrote articles, held exhibitions and formed groups to check malpractices in ration shops and road transport.",
   "In 1986 the government enacted COPRA, setting up consumer courts; it has been replaced by the Consumer Protection Act, 2019, and 24 December is National Consumers' Day.",
   "India is part of Consumers International; but redressal is still often slow and costly, so more awareness and participation are needed."])
W("la2", "long_answer", RIGHTS, "Explain any five rights of consumers with examples.",
  ["Right to safety: protection from hazardous goods, such as a pressure cooker with a faulty valve.",
   "Right to be informed: details such as MRP, ingredients and expiry date on packets.",
   "Right to choose: freedom from forced purchase, such as a gas dealer insisting you buy his stove.",
   "Right to seek redressal: compensation for a defective product or unfair practice through consumer commissions.",
   "Right to represent: being heard in consumer protection councils; and right to consumer education through consumer clubs and campaigns like Jago Grahak Jago."])
W("cb1", "case_based", RIGHTS, "Read the source and answer the questions.\n\n*\"When we buy a commodity, we find certain details given on the packing. These details are about ingredients used, price, batch number, date of manufacture, expiry date and the address of the manufacturer... Consumers have the right to be informed about the particulars of goods and services that they purchase.\"* (NCERT)\n\n"
  "(i) Which consumer right is described here? (1)\n\n(ii) Name two details printed on a packet. (1)\n\n(iii) How does this right help consumers? (2)",
  ["(i) The right to be informed.", "(ii) Any two: ingredients; price (MRP); batch number; date of manufacture; expiry date; address of the manufacturer.",
   "(iii) It helps consumers choose wisely, avoid expired or harmful goods, and complain and seek compensation if the product is defective or overpriced."])
W("cb2", "case_based", REDRESS, "Read the source and answer the questions.\n\n*\"Under COPRA, a three-tier quasi-judicial machinery at the district, state and national levels was set up for redressal of consumer disputes. The district level court deals with cases involving claims up to a certain amount, the state level courts with higher claims, and the national level court with the largest claims.\"* (Adapted from NCERT)\n\n"
  "(i) Name the three levels of consumer commissions. (1)\n\n(ii) Under the 2021 rules, up to what amount can the District Commission hear claims? (1)\n\n(iii) How do consumer groups help consumers? (2)",
  ["(i) District, State and National Commissions.", "(ii) Up to Rs 50 lakh.",
   "(iii) They guide consumers on how to file cases in consumer commissions, often represent them, and spread awareness of consumer rights."])
# ---------------- Assertion-reason ----------------
C.arq("ar1", MKT, "Rules and regulations are needed in the marketplace.", "Large companies with wealth and power can manipulate the market and exploit consumers.", 0,
      "R explains A.", "consumers need protection.", "this is why rules are needed.")
C.arq("ar2", MOV, "The consumer movement in India took an organised form in the 1960s.", "There was food shortage, hoarding, black marketing and adulteration at that time.", 0,
      "R explains A.", "it became organised then.", "this caused dissatisfaction.")
C.arq("ar3", RIGHTS, "Consumers can complain if a seller charges more than the MRP.", "Consumers have the right to be informed about the price of goods.", 0,
      "R explains A.", "overcharging is unfair.", "the MRP is printed for them.")
C.arq("ar4", REDRESS, "Hallmark is used to certify honey.", "Agmark certifies agricultural products.", 3,
      "A is false: Hallmark certifies jewellery; honey carries Agmark. R is true.", "Hallmark is for jewellery.", "Agmark is for agricultural produce.")
C.arq("ar5", REDRESS, "Consumers can appeal against a District Commission's decision.", "There is a three-tier system of district, state and national commissions.", 0,
      "R explains A.", "appeals go to higher levels.", "the tiers make appeals possible.")
C.arq("ar6", MOV, "National Consumers' Day is observed on 24 December.", "World Consumer Rights Day is observed on 15 March.", 1,
      "Both are true, but R does not explain why 24 December is National Consumers' Day (COPRA was passed that day in 1986).", "COPRA was passed on 24 December 1986.", "this recalls Kennedy's 1962 speech.")

chapter = header(SUBJ, N, "Consumer Rights", ["consumers_in_market", "consumer_movement", "consumer_rights", "redressal_and_standards"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: Consumer Rights is project work only (internally assessed) and is not evaluated in the board examination. "
  "This lesson supports the project. The pecuniary limits of consumer commissions follow the 2021 rules under the Consumer Protection Act, 2019; the NCERT book may print older limits.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
