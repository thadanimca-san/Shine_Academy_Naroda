"""CBSE Class 10 Economics Ch 3: Money and Credit (fully in the 2025-26 board syllabus)."""
import sys
from ss_common import make, header, path, SQP, SHINE, CB

ROOT = sys.argv[1]
SUBJ, N = "economics", 3
PATH = path(SUBJ, "ch03_money_and_credit")
C = make(SUBJ, N, "eco10ch03")
blk, M, W = C.blk, C.m, C.w
MON, BANK, CRED, FORM, SHG = ["money_as_exchange"], ["banks_and_deposits"], ["credit_and_terms"], ["formal_informal_credit"], ["self_help_groups"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 3 exercises", "question": n}

FORMTAB = ("| | Formal sources | Informal sources |\n|---|---|---|\n| **Who** | banks and cooperatives | moneylenders, traders, employers, relatives and friends |\n"
           "| **Supervision** | supervised by the **Reserve Bank of India** | **no organisation** supervises them |\n| **Interest** | lower | much higher; can lead to a debt trap |\n"
           "| **Collateral and papers** | usually need collateral and documents | often lend without collateral, but on unfair terms |\n| **Who uses them more** | richer households | poor households |")
TERMS = ("| Term of credit | Meaning |\n|---|---|\n| **Interest rate** | the extra amount the borrower pays the lender along with the principal |\n"
         "| **Collateral** | an asset the borrower owns (land, building, vehicle, livestock, deposits) and uses as a guarantee until the loan is repaid |\n"
         "| **Documentation** | papers the lender needs, such as proof of identity, income and ownership |\n| **Mode of repayment** | how and when the loan is to be paid back, such as monthly instalments |")

sections = [
 {"id": "s1", "title": "Why do we need money and credit?", "blocks": [
  blk("s1.hook", "hook", title="A shoe-maker who wants wheat",
    body="A shoe-maker wants to sell shoes and buy wheat. Without money, he must find a farmer who has wheat to sell and also wants shoes. That could take days!\n\n"
         "Money solves this problem. And when people need money they do not have, they borrow: this is **credit**. Credit can help a business grow, or it can trap a poor family in debt. This chapter explains how money works, how banks lend, and how to make cheap credit reach everyone."),
  blk("s1.inspiration", "inspiration", title="Banker to the poor", person="Muhammad Yunus", years="born 1940",
    body="In the 1970s, economist **Muhammad Yunus** lent a small amount of his own money to poor women in a village in Bangladesh, who were trapped by moneylenders. They repaid him. This grew into the **Grameen Bank**, which gives small loans to the poor without collateral; almost all its borrowers are **women**.\n\n"
         "In **2006**, Yunus and the Grameen Bank won the **Nobel Peace Prize**. Their work shows that the poor are creditworthy and that cheap credit can fight poverty.",
    future="This chapter leads to careers in banking, finance, microfinance, rural development and economics."),
  C.socratic("s1.socratic", "Why can borrowing make one person richer and another person poorer?",
    ["Because it depends on the terms of credit and whether the money earns enough to repay the loan", "Because borrowing is always harmful", "Because only rich people are allowed to borrow"], 0,
    "Credit at reasonable terms helps; credit at high interest with failed crops can lead to a debt trap."),
 ]},
 {"id": "s2", "title": "Money as a medium of exchange", "blocks": [
  blk("s2.thm", "theory", title="Double coincidence of wants, forms of money and bank deposits", revision=True,
    body="**Money as a medium of exchange:** a person holding money can easily exchange it for any commodity or service that he or she might want. Everyone prefers to receive payments in money and then use it to buy what they need.\n"
         "- **Barter system:** goods are directly exchanged without the use of money. Here, both parties have to agree to sell and buy each other's commodities. This is called the **double coincidence of wants**: what a person desires to sell is exactly what the other wishes to buy.\n"
         "- **Example:** a shoe manufacturer wants to sell shoes and buy wheat. In barter, he has to look for a wheat-growing farmer who not only wants to sell wheat but also wants to buy shoes in exchange. With money, he first exchanges shoes for money and then exchanges money for wheat.\n"
         "- Money **eliminates the need for double coincidence of wants**. Since money acts as an intermediate in the exchange process, it is called a **medium of exchange**.\n\n"
         "**Modern forms of money:** before coins, people used **grains and cattle** as money. Then came **metallic coins** of gold, silver and copper. Today, money includes **paper notes and coins**.\n"
         "- **Currency:** in India, the **Reserve Bank of India (RBI)** issues currency notes **on behalf of the central government**. The rupee is widely accepted as a medium of exchange because the currency is **authorised by the government** of the country. As per Indian law, no other individual or organisation is allowed to issue currency, and the law legalises the use of the rupee as a medium of payment that **cannot be refused** in settling transactions in India.\n"
         "- **Deposits with banks:** people deposit extra cash in **bank accounts** and get interest on it. Since the deposits can be withdrawn **on demand**, they are called **demand deposits**. These deposits share the essential features of money, so in a modern economy they are also considered money.\n"
         "- **Cheque:** a paper instructing the bank to pay a specific amount from the person's account to the person in whose name the cheque has been issued. Payments by cheque settle transactions without using cash. Today, payments also move between bank accounts through **digital means** such as debit cards and UPI, which also use demand deposits.\n\n"
         "**Loan activities of banks:** banks keep only a **small proportion** of their deposits as cash with themselves (in India, about **15 per cent**) to pay depositors who may come to withdraw money on any given day. Banks use the **major portion of the deposits to extend loans**. In this way, banks **mediate** between those who have **surplus funds** (depositors) and those who are **in need** of these funds (borrowers). Banks charge a **higher interest rate on loans** than what they offer on deposits; the **difference** is the main source of income for banks."),
  C.kc("s2.check", "Double coincidence of wants means:",
    [("what one person wants to sell is exactly what the other wishes to buy", ""), ("both people want money", "Money removes the need for it."),
     ("one person gives a loan to another", "That is credit."), ("two banks exchange deposits", "That is not the meaning.")],
    "It is needed in a barter system and removed by money."),
  C.kc("s2.check2", "Who issues currency notes in India?",
    [("the Reserve Bank of India, on behalf of the central government", ""), ("the State Bank of India", "It is a commercial bank."), ("the Finance Ministry directly", "The RBI issues notes on behalf of the government."), ("every commercial bank", "Only the RBI issues notes.")],
    "This was asked in the 2025-26 sample paper (answer: RBI).")
 ]},
 {"id": "s3", "title": "Credit and its terms", "blocks": [
  blk("s3.thm", "theory", title="Two credit situations and the terms of credit", revision=True,
    body="**Credit** (loan) refers to an **agreement** in which the lender supplies the borrower with money, goods or services in return for the **promise of future payment**.\n\n"
         "**Two different credit situations:**\n"
         "- **Salim**, a shoe manufacturer, gets an order for 3,000 pairs of shoes for the festival season. He takes **credit** (advance payment from the trader, and raw materials on credit from suppliers), completes the order in time and makes a **good profit**. Here credit plays a vital and **positive role**: it helps him meet ongoing expenses, complete production on time and **increase earnings**.\n"
         "- **Swapna**, a small farmer, borrows from a **moneylender** to meet the expenses of cultivation, hoping the harvest will help her repay. But the crop is hit by **pests** and fails. She cannot repay, the debt grows, and she has to **sell part of her land** to repay it. Here credit pushes her into a **debt trap**: a situation where the borrower cannot repay and is left worse off than before.\n"
         "- Whether credit is useful depends on the **risks** in the situation and whether there is some **support in case of loss**.\n\n"
         "**Terms of credit:** every loan agreement specifies an **interest rate** which the borrower must pay to the lender along with the repayment of the principal. In addition, lenders may demand **collateral** (security) against loans.\n"
         "- **Collateral** is an asset that the borrower owns (such as **land, building, vehicle, livestock, deposits with banks**) and uses as a **guarantee** to a lender until the loan is repaid. If the borrower fails to repay, the lender has the right to **sell the asset or collateral** to obtain payment.\n"
         "- **Interest rate, collateral and documentation requirement, and the mode of repayment** together comprise the **terms of credit**. These may vary substantially from one credit arrangement to another, and depend on the nature of the lender and the borrower.\n"
         "- **Example:** Megha took a loan of **Rs 5 lakh** from a bank to buy a house, at an annual interest rate of **12 per cent**, repayable in **10 years** in monthly instalments. The bank kept the **papers of the new house** as collateral; they are returned only when the whole loan with interest is repaid."),
  blk("s3.table", "markdown_table", title="Terms of credit", revision=True, body=TERMS),
  C.kc("s3.check", "What is collateral?",
    [("an asset the borrower owns and uses as a guarantee until the loan is repaid", ""), ("the interest charged on a loan", "That is the interest rate."), ("the money deposited in a bank", "Deposits can be collateral, but collateral is any pledged asset."), ("the papers that prove identity", "That is documentation.")],
    "If the loan is not repaid, the lender can sell the collateral.")
  ,C.kc("s3.check2", "Swapna's crop failed and she sold part of her land to repay the moneylender. This is an example of:",
    [("a debt trap", ""), ("a profitable use of credit", "Salim's case was profitable."), ("collateral being returned", "She lost part of her land."), ("a demand deposit", "That is a bank deposit.")],
    "High-interest credit plus crop failure left her worse off.")
 ]},
 {"id": "s4", "title": "Formal and informal sources of credit", "blocks": [
  blk("s4.thm", "theory", title="Who lends, on what terms, and to whom", revision=True,
    body="**Variety of credit arrangements (Sonpur village):**\n"
         "- **Shyamal**, a small farmer, borrows from the village **moneylender** at **5 per cent per month** (that is, **60 per cent per year**) for cultivation.\n"
         "- **Rama**, an agricultural labourer, borrows from her **employer**, a landowner, at 5 per cent per month and repays by **working for him** for low wages; she is stuck in debt.\n"
         "- **Arun**, who owns more land, gets a **bank loan** at **8.5 per cent per year**, repayable in **three years**, by giving his land as collateral.\n"
         "- Farmers can also get loans from the **Krishak Cooperative**, which accepts deposits from members and lends to them at reasonable rates.\n\n"
         "**Formal sector credit:** loans from **banks and cooperatives**. The **Reserve Bank of India supervises** the functioning of formal sources of loans: it sees that banks **maintain a minimum cash balance** out of the deposits they receive, and that they give loans not just to profit-making businesses and traders but also to **small cultivators, small-scale industries and small borrowers**. Banks have to submit information to the RBI on how much they are lending, to whom and at what interest rate.\n\n"
         "**Informal sector credit:** loans from **moneylenders, traders, employers, relatives and friends**. There is **no organisation** which supervises their credit activities. They can lend at whatever interest rate they choose, and there is no one to stop them from using **unfair means** to get their money back. Since informal lenders charge **much higher interest rates**, a larger part of the borrower's earnings is used to repay the loan, and the borrower may fall into a **debt trap**.\n\n"
         "**Why we need to expand formal credit:** cheap and affordable credit is crucial for the country's development.\n"
         "- **Higher cost of borrowing** from informal sources means that more of the borrower's income goes to repaying the loan, leaving less for themselves (as for Shyamal).\n"
         "- The high interest rate can mean that the amount to be repaid is **greater than the income** of the borrower, leading to **increasing debt** (as for Rama).\n"
         "- People who wish to **start an enterprise** may not do so because of the high cost of borrowing.\n"
         "- So banks and cooperatives need to **lend more**, especially in rural areas, so that dependence on informal sources reduces. Formal sector loans also need to reach the **poor**, not only the rich. The formal sector still meets only about **half** of the total credit needs of the rural people.\n\n"
         "**Who gets what?** **Rich households** get most of their credit from **formal sources**, while **poor households** depend largely on **informal sources**. The poor often lack **collateral** and the **documents** banks require, and banks find it costly to make many small loans."),
  blk("s4.table", "markdown_table", title="Formal and informal sources of credit", revision=True, body=FORMTAB),
  C.kc("s4.check", "Which of these is an informal source of credit?",
    [("a village moneylender", ""), ("a commercial bank", "Banks are formal."), ("a cooperative society", "Cooperatives are formal."), ("a regional rural bank", "This is formal.")],
    "Informal lenders are not supervised by any organisation.")
  ,C.kc("s4.check2", "Who supervises the formal sources of credit in India?",
    [("the Reserve Bank of India", ""), ("the village panchayat", "It does not supervise banks."), ("the Supreme Court", "Courts do not supervise lending."), ("the moneylenders' association", "There is no such supervisor.")],
    "The RBI checks cash balances and lending to small borrowers.")
 ]},
 {"id": "s5", "title": "Self-Help Groups for the poor", "blocks": [
  blk("s5.thm", "theory", title="How SHGs bring credit to the poor", revision=True,
    body="The poor, especially in rural areas, find it difficult to get bank loans because they lack **collateral** and documents. **Self-Help Groups (SHGs)** are a newer way of meeting their credit needs, based on the idea of **organising rural poor, in particular women**, into small groups and pooling their savings.\n"
         "- A typical SHG has **15–20 members**, usually belonging to one neighbourhood, who **meet and save regularly**. Saving per member varies from **Rs 25 to Rs 100** or more, depending on the ability of the people to save.\n"
         "- Members can take **small loans from the group itself** to meet their needs. The group charges interest on these loans, but this is still **less than what the moneylender charges**.\n"
         "- After a year or two, if the group is regular in savings, it becomes **eligible for availing a loan from the bank**. The loan is sanctioned **in the name of the group** and is meant to create **self-employment** opportunities for the members: for example, small loans to release mortgaged land, to meet working capital needs (seeds, fertilisers, raw materials like bamboo and cloth), for housing, or to buy assets like sewing machines, handlooms and cattle.\n"
         "- **Most of the important decisions regarding savings and loan activities are taken by the group members.** The group decides the loans to be granted, the purpose, amount, interest to be charged and repayment schedule. The **group is responsible for repayment**: any case of non-repayment is followed up seriously by other members. Because of this, banks are willing to lend to the poor women when they are organised in SHGs, **even though they have no collateral**.\n\n"
         "**Benefits of SHGs:**\n"
         "- They help borrowers **overcome the problem of lack of collateral**.\n"
         "- They get **timely loans** for a variety of purposes at a **reasonable interest rate**.\n"
         "- They are the building blocks of organisation of the rural poor: they help women become **financially self-reliant**.\n"
         "- Regular meetings give a **platform to discuss** a variety of social issues such as **health, nutrition and domestic violence**.\n\n"
         "**Grameen Bank of Bangladesh:** started in the **1970s** by **Professor Muhammad Yunus** as a small project, it gives small loans to poor people without collateral. **Almost all of its borrowers are women** who belong to the poorest sections of society. It has shown that the poor are reliable borrowers. Professor Yunus and the Grameen Bank received the **Nobel Peace Prize in 2006**."),
  C.kc("s5.check", "In an SHG, most decisions about savings and loans are taken by:",
    [("the members of the group", ""), ("the bank", "The bank lends to the group but does not decide its internal loans."), ("a moneylender", "SHGs reduce dependence on moneylenders."), ("the RBI", "The RBI supervises banks, not SHG decisions.")],
    "The group is also responsible for repayment.")
  ,C.kc("s5.check2", "Why are banks willing to lend to SHGs without collateral?",
    [("Because the whole group is responsible for repayment", ""), ("Because the members are rich", "Members are usually poor."), ("Because the RBI repays the loan", "The group repays."), ("Because the loans are free", "Loans carry interest.")],
    "Group pressure ensures repayment.")
 ]},
 {"id": "s6", "title": "Remember, avoid, practise", "blocks": [
  blk("s6.memory", "memory_trick", title="Memory tricks",
    body="- **Barter needs \"DCW\"** (Double Coincidence of Wants); **money removes it** = medium of exchange.\n- **RBI issues notes on behalf of the Centre; rupee cannot be refused.**\n"
         "- **Banks keep ~15% as cash; lend the rest; income = loan interest − deposit interest.**\n- **Terms of credit \"I-C-D-R\"**: Interest, Collateral, Documentation, Repayment mode.\n"
         "- **Formal = Banks + Cooperatives (RBI watches); Informal = Moneylenders, Traders, Employers, Relatives, Friends (no one watches).**\n"
         "- **SHG \"15-20, save, loan, bank, group repays\"**; Grameen Bank, Yunus, Nobel Peace Prize 2006."),
  blk("s6.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying the State Bank of India or the Finance Ministry issues notes: the **RBI** issues them on behalf of the central government.\n2. Calling demand deposits 'not money': they share the essential features of money and are counted as money.\n"
         "3. Calling employers and relatives formal lenders: they are **informal**.\n4. Saying banks keep all deposits as cash: they keep only about **15 per cent** and lend the rest.\n"
         "5. Saying SHG decisions are taken by the bank: they are taken by the **members**.\n6. Mixing up collateral and interest: collateral is an **asset pledged**; interest is the **price** of the loan."),
  blk("s6.tip", "teacher_tip", title="Try this in class",
    body="Play a quick barter game: give each student a picture card of a good, and ask them to trade for what they want without money. Then introduce paper 'money' and repeat. Discuss how money removed the need for double coincidence of wants."),
  blk("s6.reflection", "reflection", title="Think and explain",
    body="If a small shopkeeper in your area needed Rs 20,000 to expand the shop, where could she borrow from? Compare a bank, a moneylender and an SHG on interest, collateral and risk."),
  blk("s6.connection", "connection", title="Where this leads",
    body="- **Chapter 2 (Sectors of the Indian Economy):** credit for farmers and small producers creates jobs.\n- **Chapter 4 (Globalisation):** finance and investment across countries.\n"
         "- **History Chapter 3 (The Making of a Global World):** money, trade and the world economy."),
  blk("s6.mastery", "mastery", title="Mastery challenge",
    body="'Cheap and affordable credit is crucial for the country's development.' Justify in about 120 words.\n\n"
         "**Model answer:** Credit helps people meet the expenses of production and earn more, as Salim did by completing his festival order. But informal credit is costly: moneylenders charge very high interest, such as 5 per cent per month, so a large part of the borrower's earnings goes to repaying the loan. "
         "If the crop fails, as with Swapna, the borrower falls into a debt trap and may lose land. High interest also discourages people from starting new enterprises. "
         "Banks and cooperatives lend at lower rates and are supervised by the RBI, so expanding formal credit, especially to the rural poor, raises incomes. Self-Help Groups help the poor get such loans without collateral. Cheap credit thus supports farming, small industry and employment."),
  blk("s6.summary", "summary", title="Chapter summary",
    body="- Money is a medium of exchange that removes the double coincidence of wants; modern money includes currency and demand deposits.\n"
         "- The RBI issues currency on behalf of the government; the rupee is legal tender that cannot be refused.\n"
         "- Banks keep about 15 per cent of deposits as cash and lend the rest; interest on loans minus interest on deposits is their main income.\n"
         "- Credit can raise earnings or cause a debt trap; terms of credit include interest, collateral, documentation and repayment.\n"
         "- Formal credit (banks, cooperatives) is supervised by the RBI and cheaper; informal credit is costly and unregulated; the poor depend more on informal credit.\n"
         "- Self-Help Groups help the poor, especially women, get loans without collateral and become self-reliant."),
  blk("s6.examtips", "exam_tips", title="Board exam tips",
    body="- The 2025-26 sample paper asked who issues currency notes in India (RBI; answer B), why double coincidence of wants limits barter trade (answer A), and a 3-mark question on why formal credit must expand and reach all people.\n"
         "- 3/5-mark favourites: money solving double coincidence, banks as mediators, terms of credit, formal vs informal credit, role of the RBI, SHGs.\n"
         "- Use the textbook examples (Salim, Swapna, Shyamal, Rama, Arun) to support your answers."),
  blk("s6.flash1", "flashcard", front="What is double coincidence of wants?", back="A situation in barter where what one person wants to sell is exactly what the other wishes to buy."),
  blk("s6.flash2", "flashcard", front="What is collateral?", back="An asset the borrower owns (land, building, vehicle, livestock, deposits) and pledges as a guarantee until the loan is repaid."),
  blk("s6.flash3", "flashcard", front="What is a debt trap?", back="A situation where the borrower cannot repay the loan, the debt grows, and the borrower is left worse off than before."),
  blk("s6.flash4", "flashcard", front="What are demand deposits?", back="Deposits in bank accounts that can be withdrawn on demand; they are treated as money and can be used through cheques."),
 ]},
]

# ---------------- Sample paper ----------------
M("sqp32", MON, "Which one of the following issues currency notes in India?",
  [("Finance Ministry.", "The RBI issues notes on behalf of the central government."), ("Reserve Bank of India.", ""), ("State Bank of India.", "It is a commercial bank."), ("Central Bank of India.", "It is a commercial bank, despite its name.")],
  "The Reserve Bank of India issues currency notes on behalf of the central government (CBSE marking scheme: B).", "easy", SQP(32), correct=1)
M("sqp33", MON, "Person Z tries to explain how the requirement of a double coincidence of wants in a barter system limits trade and exchange. Which of the following justifications do you think will be used by him/her?",
  [("It makes trade more complicated, as each person must have what the other person wants, limiting the pool of potential trade partners.", ""),
   ("The barter system allows trade to be conducted more efficiently since both parties already know what they need from the transaction.", "Barter is less efficient, not more."),
   ("It increases the number of exchanges because each person can trade for exactly what they want.", "It reduces the number of possible exchanges."),
   ("The system creates value for goods by ensuring that both parties have a direct need for each other's goods.", "This does not explain the limitation.")],
  "Double coincidence of wants narrows the number of people one can trade with (CBSE marking scheme: A).", "medium", SQP(33), correct=0)
W("sqp36", "short_answer", FORM, "'Expanding access to loans in the formal sector is important, yet it is equally critical that these loans are accessible to all people for national development.' Justify the statement.",
  ["Borrowing from informal sources costs more, so a larger part of the borrower's earnings goes to repaying the loan, leaving less income (as for Shyamal); high interest can make repayment greater than income and push borrowers into a debt trap (as for Rama).",
   "People who wish to start an enterprise may not do so because of the high cost of borrowing, so banks and cooperatives need to lend more, especially to the poor.",
   "Cheap and affordable credit lets people grow crops, do business and set up small industries, raising incomes; so formal credit must reach everyone, not just the rich, for the country's development."], source=SQP(36))

# ---------------- NCERT exercises ----------------
W("ex1", "very_short_answer", CRED, "Why are risks for borrowers higher in situations of high interest rate?",
  ["With high interest, a large part of the borrower's earnings goes to repaying the loan, and the amount to repay may become greater than the income.",
   "If the borrower cannot repay (for example, if a crop fails), the debt keeps growing and the borrower may lose collateral such as land: a debt trap."], source=ex("1"))
W("ex2", "short_answer", MON, "How does money solve the problem of double coincidence of wants? Explain with an example of your own.",
  ["In barter, both parties must want what the other has: this is the double coincidence of wants, which makes trade difficult.",
   "Money acts as a medium of exchange: a person can sell goods for money and use the money to buy what they want from anyone.",
   "Example: a potter who wants rice need not find a rice farmer who wants pots; he sells pots for money and buys rice with it."], source=ex("2"))
W("ex3", "short_answer", BANK, "How do banks mediate between those who have surplus money and those who need money?",
  ["People with surplus money deposit it in banks and earn interest on it.",
   "Banks keep only a small part (about 15 per cent) of deposits as cash and use the major portion to give loans to people who need money.",
   "Banks charge a higher interest on loans than they pay on deposits; the difference is their main income."], source=ex("3"))
W("ex4", "short_answer", MON, "Look at a 10 rupee note. What is written on top? Can you explain this statement?",
  ["It says 'Reserve Bank of India', 'Guaranteed by the Central Government', and the Governor's promise: 'I promise to pay the bearer the sum of ten rupees'.",
   "This means the RBI issues the currency note on behalf of the central government, which guarantees its value.",
   "Because the currency is authorised by the government, the rupee is legal tender and cannot be refused as payment in India."], source=ex("4"))
W("ex5", "short_answer", FORM, "Why do we need to expand formal sources of credit in India?",
  ["Informal lenders charge very high interest and are not supervised, so borrowers can fall into a debt trap.",
   "Cheap credit from banks and cooperatives lets people grow crops, run businesses and set up small industries, raising incomes.",
   "The poor depend largely on informal credit, and the formal sector meets only about half of rural credit needs, so it must expand and reach the poor."], source=ex("5"))
W("ex6", "short_answer", SHG, "What is the basic idea behind the SHGs for the poor? Explain in your own words.",
  ["SHGs organise the rural poor, especially women, into small groups of 15–20 members who save regularly and pool their savings.",
   "Members take small loans from the group at lower interest than moneylenders; after regular saving, the group gets bank loans in its name without collateral.",
   "The group decides on loans and is responsible for repayment, which helps members become financially self-reliant and discuss social issues."], source=ex("6"))
W("ex7", "short_answer", FORM, "What are the reasons why the banks might not be willing to lend to certain borrowers?",
  ["The borrower may not have collateral, such as land or a building, to guarantee the loan.",
   "The borrower may not have proper documents, such as proof of income or a regular job.",
   "The borrower may have failed to repay earlier loans, or the bank may find the loan too small and risky to be worth the cost."], source=ex("7"))
W("ex8", "short_answer", FORM, "In what ways does the Reserve Bank of India supervise the functioning of banks? Why is this necessary?",
  ["The RBI sees that banks maintain a minimum cash balance out of the deposits they receive.",
   "It sees that banks give loans not just to profit-making businesses and traders but also to small cultivators, small-scale industries and small borrowers; banks must report how much they lend, to whom and at what interest.",
   "This is necessary to protect depositors' money and to make sure cheap credit reaches those who need it, reducing dependence on moneylenders."], source=ex("8"))
W("ex9", "short_answer", CRED, "Analyse the role of credit for development.",
  ["Credit helps people meet the costs of production and complete work on time, raising earnings, as in Salim's case.",
   "Cheap credit lets farmers grow crops and people start businesses and small industries, creating jobs and incomes.",
   "But credit at high interest can push people into a debt trap, as with Swapna; so cheap and affordable formal credit is crucial for development."], source=ex("9"))
W("ex10", "short_answer", CRED, "Manav needs a loan to set up a small business. On what basis will Manav decide whether to borrow from the bank or the moneylender? Discuss.",
  ["He will compare the terms of credit: the bank charges a much lower interest rate than the moneylender.",
   "He will check whether he has the collateral and documents the bank needs; the moneylender may lend without them but on unfair terms.",
   "He will consider the mode of repayment and the risk of a debt trap; if he can meet the bank's conditions, a bank loan is safer and cheaper."], source=ex("10"))
M("ex12a", MON, "______ issues currency notes on behalf of the central government.",
  [("The Reserve Bank of India", ""), ("The State Bank of India", "It is a commercial bank."), ("The Finance Commission", "It deals with sharing taxes."), ("NABARD", "It is a development bank for agriculture.")],
  "The RBI is India's central bank.", "easy", ex("12"), correct=0)
M("ex12b", CRED, "______ is an asset that the borrower owns and uses as a guarantee until the loan is repaid to the lender.",
  [("Collateral", ""), ("Interest", "Interest is the price of the loan."), ("Deposit", "A deposit can be collateral, but the term is collateral."), ("Cheque", "A cheque is an instruction to pay.")],
  "The lender can sell the collateral if the loan is not repaid.", "easy", ex("12"), correct=0)
M("ex12c", FORM, "The majority of the credit needs of the ______ households are met from informal sources.",
  [("poor", ""), ("rich", "Rich households use formal sources more."), ("urban rich", "They use formal sources more."), ("government employee", "They usually have access to banks.")],
  "The poor lack collateral and documents.", "easy", ex("12"), correct=0)
M("ex13a", SHG, "In an SHG, most of the decisions regarding savings and loan activities are taken by:",
  [("Members", ""), ("Bank", "The bank lends to the group but members decide."), ("Non-government organisation", "NGOs may help form groups, but members decide."), ("Moneylender", "SHGs reduce dependence on moneylenders.")],
  "The group decides the loans, purpose, amount, interest and repayment.", "easy", ex("13"), correct=0)
M("ex13b", FORM, "Formal sources of credit do not include:",
  [("Employers", ""), ("Banks", "Banks are formal."), ("Cooperatives", "Cooperatives are formal."), ("Regional rural banks", "These are formal.")],
  "Employers, moneylenders, traders, relatives and friends are informal sources.", "easy", ex("13"), correct=0)

# ---------------- MCQs ----------------
M("mcq01", MON, "In a barter system, goods are exchanged:",
  [("directly, without the use of money", ""), ("only through banks", "Barter does not use banks."), ("using paper currency", "That is money exchange."), ("using cheques", "That uses demand deposits.")], "It needs double coincidence of wants.")
M("mcq02", MON, "Money is called a medium of exchange because it:",
  [("acts as an intermediate in the exchange process", ""), ("is always made of gold", "Money takes many forms."), ("can only be used by banks", "Everyone uses it."), ("is issued by moneylenders", "The RBI issues currency.")], "It removes the need for double coincidence of wants.")
M("mcq03", MON, "Before coins came into use, which were used as money?",
  [("grains and cattle", ""), ("paper notes", "These came much later."), ("cheques", "These came much later."), ("credit cards", "These are modern.")], "Then came metallic coins.")
M("mcq04", MON, "Why is the rupee widely accepted as a medium of exchange in India?",
  [("because it is authorised by the government", ""), ("because it is made of gold", "It is not."), ("because banks print it freely", "Only the RBI issues it."), ("because it earns interest", "Currency does not earn interest.")], "No one can refuse payment in rupees in India.")
M("mcq05", BANK, "Deposits in bank accounts that can be withdrawn on demand are called:",
  [("demand deposits", ""), ("fixed collateral", "Collateral is a pledged asset."), ("informal loans", "These are loans."), ("terms of credit", "These are loan conditions.")], "They are treated as money.")
M("mcq06", BANK, "A cheque is:",
  [("a paper instructing the bank to pay a specific amount from a person's account to another person", ""), ("a type of loan", "It is a payment instruction."), ("a currency note", "It is not currency."), ("a certificate of collateral", "It is a payment instruction.")], "It uses demand deposits.")
M("mcq07", BANK, "About what share of their deposits do banks in India keep as cash?",
  [("about 15 per cent", ""), ("about 85 per cent", "They lend most of it."), ("100 per cent", "They lend most deposits."), ("about 50 per cent", "It is about 15 per cent.")], "They lend the major portion.")
M("mcq08", BANK, "What is the main source of income of banks?",
  [("the difference between interest on loans and interest on deposits", ""), ("selling currency notes", "Banks do not sell notes."), ("fees from the RBI", "That is not the main income."), ("collateral sold every day", "Collateral is sold only if loans are not repaid.")], "Banks charge more on loans than they pay on deposits.")
M("mcq09", CRED, "Credit refers to an agreement in which:",
  [("the lender supplies money, goods or services in return for a promise of future payment", ""), ("goods are exchanged without money", "That is barter."), ("money is given as a gift", "Credit must be repaid."), ("the government prints money", "That is not credit.")], "It is also called a loan.")
M("mcq10", CRED, "In Salim's case, credit:",
  [("helped him complete the order in time and earn a profit", ""), ("pushed him into a debt trap", "That was Swapna's case."), ("made him sell his land", "That was Swapna."), ("was refused by all lenders", "He got credit.")], "Credit played a positive role.")
M("mcq11", CRED, "Why did Swapna fall into a debt trap?",
  [("Her crop failed, so she could not repay the moneylender's loan", ""), ("She got a bank loan at low interest", "She borrowed from a moneylender."), ("She had too much income", "She could not repay."), ("She joined an SHG", "That is not the reason.")], "She had to sell part of her land.")
M("mcq12", CRED, "Which is NOT one of the terms of credit?",
  [("the colour of the currency note", ""), ("interest rate", "This is a term."), ("collateral", "This is a term."), ("mode of repayment", "This is a term.")], "Terms are interest, collateral, documentation and repayment.")
M("mcq13", CRED, "If a borrower fails to repay a loan, the lender has the right to:",
  [("sell the collateral to obtain payment", ""), ("print new money", "Only the RBI issues currency."), ("cancel the borrower's vote", "This is not allowed."), ("close the bank", "This is not the remedy.")], "Collateral is a guarantee.")
M("mcq14", CRED, "Megha took a housing loan of Rs 5 lakh at 12 per cent per year for 10 years. What did the bank keep as collateral?",
  [("the papers of the new house", ""), ("her salary slips only", "These are documents, not collateral."), ("her bank passbook", "That is not the collateral given."), ("nothing", "The house papers were kept.")], "They are returned after full repayment.")
M("mcq15", FORM, "Shyamal borrowed from a moneylender at 5 per cent per month. What is this per year?",
  [("60 per cent", ""), ("5 per cent", "That is per month."), ("12 per cent", "That is Megha's bank rate."), ("8.5 per cent", "That is Arun's bank rate.")], "5 × 12 months = 60 per cent per year.")
M("mcq16", FORM, "Rama repays her loan by working for her employer at low wages. This shows that:",
  [("informal credit can trap borrowers in debt", ""), ("formal credit is always costly", "Formal credit is cheaper."), ("employers are formal lenders", "Employers are informal lenders."), ("Rama has a lot of collateral", "She has no land.")], "Her debt keeps growing.")
M("mcq17", FORM, "Arun got a bank loan at 8.5 per cent per year because he:",
  [("could give his land as collateral", ""), ("was an agricultural labourer", "Rama was the labourer."), ("borrowed from a moneylender", "He borrowed from a bank."), ("had no documents", "He met the bank's conditions.")], "Formal credit needs collateral.")
M("mcq18", FORM, "Which is a formal source of credit?",
  [("a cooperative society", ""), ("a trader", "Traders are informal."), ("a relative", "Relatives are informal."), ("a moneylender", "Moneylenders are informal.")], "Banks and cooperatives are formal.")
M("mcq19", FORM, "The RBI makes sure that banks give loans to:",
  [("small cultivators, small-scale industries and small borrowers", ""), ("only big companies", "It wants small borrowers to get loans too."), ("only the government", "That is not the aim."), ("only foreign banks", "That is not the aim.")], "Banks must report whom they lend to.")
M("mcq20", FORM, "Why is informal credit costlier?",
  [("Because no one supervises informal lenders, so they charge high interest", ""), ("Because the RBI fixes high rates for moneylenders", "The RBI does not supervise moneylenders."), ("Because informal lenders always ask for collateral", "They often do not."), ("Because informal loans are free", "They charge high interest.")], "They may also use unfair means to recover money.")
M("mcq21", FORM, "Most of the credit needs of rich households are met by:",
  [("formal sources", ""), ("moneylenders", "The poor depend more on moneylenders."), ("employers", "These are informal."), ("relatives only", "These are informal.")], "The poor depend more on informal sources.")
M("mcq22", FORM, "Why do poor households depend on informal credit?",
  [("They lack collateral and the documents banks need", ""), ("Informal credit is cheaper", "It is costlier."), ("Banks are not allowed in villages", "Banks work in villages."), ("They prefer high interest", "No one prefers high interest.")], "Banks also find small loans costly.")
M("mcq23", FORM, "About what share of the total credit needs of rural people is met by the formal sector?",
  [("about half", ""), ("all of it", "Much is still informal."), ("about one-tenth", "It is about half."), ("none", "Banks and cooperatives do lend.")], "Formal credit must expand.")
M("mcq24", SHG, "A typical Self-Help Group has how many members?",
  [("15–20", ""), ("2–3", "It is usually 15–20."), ("100–200", "It is usually 15–20."), ("only one", "It is a group.")], "They usually belong to one neighbourhood.")
M("mcq25", SHG, "After how long can a regular SHG usually get a bank loan?",
  [("after a year or two of regular savings", ""), ("on the first day", "It must save regularly first."), ("after twenty years", "It is usually a year or two."), ("never", "SHGs do get bank loans.")], "The loan is in the name of the group.")
M("mcq26", SHG, "SHGs help borrowers overcome the problem of:",
  [("lack of collateral", ""), ("too much income", "That is not a problem they solve."), ("too many banks", "That is not the issue."), ("double coincidence of wants", "Money solves that.")], "The group guarantees repayment.")
M("mcq27", SHG, "Besides credit, SHG meetings provide a platform to discuss:",
  [("health, nutrition and domestic violence", ""), ("only cricket scores", "They discuss social issues."), ("printing currency", "That is the RBI's work."), ("election results only", "They discuss social issues.")], "They help women become self-reliant.")
M("mcq28", SHG, "Who started the Grameen Bank of Bangladesh?",
  [("Professor Muhammad Yunus", ""), ("Amartya Sen", "He is an economist known for development studies."), ("Ela Bhatt", "She founded SEWA in India."), ("Kanshi Ram", "He founded the BSP.")], "He won the Nobel Peace Prize in 2006.")
M("mcq29", SHG, "Almost all the borrowers of the Grameen Bank are:",
  [("women from the poorest sections", ""), ("big landowners", "It lends to the poor."), ("foreign companies", "It lends to the poor."), ("government officers", "It lends to the poor.")], "It shows the poor are reliable borrowers.")
M("mcq30", BANK, "Banks mediate between:",
  [("depositors with surplus funds and borrowers who need funds", ""), ("buyers and sellers in barter", "That is not the banks' role."), ("the RBI and the courts", "That is not the role."), ("moneylenders and traders", "That is not the role.")], "They take deposits and give loans.")
# ---------------- True / false ----------------
C.tf("tf1", MON, "The State Bank of India issues currency notes in India.", False, "The Reserve Bank of India issues them on behalf of the central government.")
C.tf("tf2", BANK, "Demand deposits are considered money in a modern economy.", True, "They share the essential features of money.")
C.tf("tf3", FORM, "Moneylenders are supervised by the Reserve Bank of India.", False, "No organisation supervises informal lenders.")
C.tf("tf4", SHG, "In an SHG, the group as a whole is responsible for repaying the loan.", True, "This is why banks lend to SHGs without collateral.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", MON, "Why is the rupee accepted as a medium of exchange in India?",
  ["The currency is issued by the RBI on behalf of the central government and is authorised by the government.", "By law, no one in India can refuse payment made in rupees."])
W("vsa2", "very_short_answer", CRED, "What are the terms of credit?",
  ["Interest rate, collateral and documentation requirement, and the mode of repayment.", "They differ from one credit arrangement to another, depending on the lender and the borrower."])
W("vsa3", "very_short_answer", FORM, "Distinguish between formal and informal sources of credit.",
  ["Formal: banks and cooperatives, supervised by the RBI, with lower interest.", "Informal: moneylenders, traders, employers, relatives and friends, not supervised, with much higher interest."])
W("sa1", "short_answer", CRED, "'Credit can play a positive role or push people into a debt trap.' Explain with examples.",
  ["Positive: Salim took credit to complete a festival order of shoes, finished on time and made a profit.",
   "Debt trap: Swapna borrowed from a moneylender for her crop; the crop failed, she could not repay, and she had to sell part of her land.",
   "Whether credit helps depends on the risks involved and whether there is support in case of loss."])
W("sa2", "short_answer", FORM, "What is the role of the Reserve Bank of India in the formal credit system?",
  ["It issues currency notes on behalf of the central government.",
   "It supervises banks: they must keep a minimum cash balance out of deposits and report how much they lend, to whom and at what interest.",
   "It makes sure banks lend to small cultivators, small-scale industries and small borrowers, not just to big businesses."])
W("sa3", "short_answer", SHG, "Explain the benefits of Self-Help Groups.",
  ["SHGs help the poor overcome the lack of collateral, as the group guarantees repayment.",
   "Members get timely loans for many purposes at reasonable interest, lower than moneylenders.",
   "They help women become financially self-reliant, and meetings give a platform to discuss health, nutrition and domestic violence."])
W("la1", "long_answer", FORM, "'Formal sources of credit need to be expanded and made accessible to the poor.' Explain.",
  ["Informal lenders charge very high interest, such as 5 per cent per month, so a large part of the borrower's earnings goes to repaying loans.",
   "When the amount to be repaid is more than income, borrowers fall into a debt trap, as with Rama, and may lose land.",
   "High interest also discourages people from starting enterprises, which slows development.",
   "Banks and cooperatives lend at lower interest and are supervised by the RBI, but they meet only about half of rural credit needs, and mostly serve richer households.",
   "So formal credit must expand, especially in rural areas, and reach the poor through means like Self-Help Groups that overcome the lack of collateral."])
W("la2", "long_answer", SHG, "Explain how a Self-Help Group works.",
  ["A typical SHG has 15–20 members, usually women from one neighbourhood, who meet and save regularly, from Rs 25 to Rs 100 or more each.",
   "Members can take small loans from the group's savings at interest lower than the moneylender's.",
   "After a year or two of regular savings, the group can get a bank loan in its name, used for self-employment such as buying seeds, sewing machines, handlooms or cattle.",
   "The members take most decisions on savings and loans: the purpose, amount, interest and repayment schedule.",
   "The group is responsible for repayment, so banks lend without collateral; SHGs also make women self-reliant and give a platform to discuss social issues."])
W("cb1", "case_based", CRED, "Read the source and answer the questions.\n\n*\"Every loan agreement specifies an interest rate which the borrower must pay to the lender along with the repayment of the principal. In addition, lenders may demand a collateral (security) against loans. Collateral is an asset that the borrower owns (such as land, building, vehicle, livestock, deposits with banks) and uses this as a guarantee to a lender until the loan is repaid.\"* (NCERT)\n\n"
  "(i) What is collateral? (1)\n\n(ii) What happens if the borrower fails to repay the loan? (1)\n\n(iii) Name the four terms of credit. (2)",
  ["(i) An asset the borrower owns and uses as a guarantee to the lender until the loan is repaid.", "(ii) The lender has the right to sell the collateral to obtain payment.",
   "(iii) Interest rate, collateral, documentation requirement and mode of repayment."])
W("cb2", "case_based", SHG, "Read the source and answer the questions.\n\n*\"A typical SHG has 15–20 members, usually belonging to one neighbourhood, who meet and save regularly... Members can take small loans from the group itself to meet their needs. The group charges interest on these loans but this is still less than what the moneylender charges. After a year or two, if the group is regular in savings, it becomes eligible for availing loan from the bank.\"* (NCERT)\n\n"
  "(i) How many members does a typical SHG have? (1)\n\n(ii) Why do members prefer loans from the group? (1)\n\n(iii) How do SHGs help the poor get bank loans? (2)",
  ["(i) 15–20 members.", "(ii) Because the group charges less interest than the moneylender.",
   "(iii) After regular savings, the group gets a bank loan in its name without collateral, because the whole group is responsible for repayment."])
# ---------------- Assertion-reason ----------------
C.arq("ar1", MON, "Money acts as a medium of exchange.", "Money eliminates the need for double coincidence of wants.", 0,
      "R explains A.", "it is an intermediate in exchange.", "this is why it is a medium of exchange.")
C.arq("ar2", BANK, "Banks keep only a small part of their deposits as cash.", "Banks use the major portion of deposits to extend loans.", 0,
      "R explains A.", "they keep about 15 per cent.", "lending is how they earn.")
C.arq("ar3", FORM, "Poor households depend largely on informal sources of credit.", "Banks require collateral and documents that the poor often lack.", 0,
      "R explains A.", "their credit comes mostly from moneylenders and others.", "this keeps them away from banks.")
C.arq("ar4", FORM, "Informal lenders charge low interest rates.", "No organisation supervises the credit activities of informal lenders.", 3,
      "A is false: informal lenders charge much higher interest. R is true.", "their rates are high.", "they are unregulated.")
C.arq("ar5", SHG, "Banks lend to SHGs even without collateral.", "The group as a whole is responsible for repayment of the loan.", 0,
      "R explains A.", "group pressure ensures repayment.", "this is the SHG principle.")
C.arq("ar6", MON, "The rupee can be refused as payment in India.", "The Reserve Bank of India issues currency notes on behalf of the central government.", 3,
      "A is false: by law the rupee cannot be refused. R is true.", "it is legal tender.", "the RBI issues currency.")

chapter = header(SUBJ, N, "Money and Credit", ["money_as_exchange", "banks_and_deposits", "credit_and_terms", "formal_informal_credit", "self_help_groups"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: this chapter is fully in the board examination (Economics: 20 marks). There is no map item from this chapter. NCERT exercise 11 (a long case on small farmers) is covered by the formal and informal credit questions; data graphs are summarised in words.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
