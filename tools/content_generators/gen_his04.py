"""CBSE Class 10 History Ch 4: The Age of Industrialisation (2025-26: periodic assessment only, not in the board examination)."""
import sys
from ss_common import make, header, path, SHINE

ROOT = sys.argv[1]
SUBJ, N = "history", 4
PATH = path(SUBJ, "ch04_age_of_industrialisation")
C = make(SUBJ, N, "his10ch04")
blk, M, W = C.blk, C.m, C.w
PROTO, BRIT, WORK, COL, IND = ["proto_industrialisation"], ["industrial_britain"], ["hand_labour_workers"], ["colonies_weavers"], ["indian_factories_market"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 4 exercises", "question": n}

TIMELINE = ("| Year | Event |\n|---|---|\n| 1730s | Earliest factories in England |\n| 1760 → 1787 | Britain's raw cotton imports rise from 2.5 million to 22 million pounds |\n"
            "| 1764 | James Hargreaves' Spinning Jenny |\n| 1781 | James Watt patents his improved steam engine |\n| 1772 | Henry Patullo claims demand for Indian textiles can never fall |\n"
            "| 1811–12 → 1850–51 | Piece-goods fall from 33% to 3% of India's exports |\n| 1854 | First cotton mill in Bombay (production from 1856) |\n| 1855 | First jute mill in Bengal |\n"
            "| 1860s | American Civil War: raw cotton exports from India rise; Elgin Mill in Kanpur |\n| 1861 | First cotton mill in Ahmedabad |\n| 1874 | First spinning and weaving mill in Madras |\n"
            "| 1917 | Seth Hukumchand sets up the first Indian jute mill in Calcutta |\n| 1914–18 | First World War: Indian industries expand |")
HANDvsMACH = ("| Why some industrialists preferred hand labour | Example |\n|---|---|\n| Plenty of cheap labour; no labour shortage | poor peasants and vagrants moved to the cities in search of work |\n"
              "| Machines were costly and broke down | merchants were cautious about expensive new technology |\n| Seasonal demand | gasworks and breweries were busy in winter; printers and bookbinders before Christmas |\n"
              "| Variety and design | 500 varieties of hammers and 45 kinds of axes in mid-19th-century Britain |\n| Taste of the rich | aristocrats and the bourgeoisie preferred hand-made, refined, individually designed goods |")
WEAVERS = ("| Company step | Effect on weavers |\n|---|---|\n| Removed existing traders and brokers | weavers lost their old networks |\n| Appointed **gomasthas** (paid servants) to supervise weavers, collect supplies and check quality | outsiders who acted arrogantly; weavers were often beaten and flogged for delays |\n"
           "| **System of advances**: loans to buy raw material, cloth to be handed to the gomastha | weavers could not sell to other buyers or bargain over prices; prices paid were miserably low |\n"
           "| Result | many weavers deserted villages, revolted, refused loans or became agricultural labourers |")

sections = [
 {"id": "s1", "title": "Before the factories", "blocks": [
  blk("s1.hook", "hook", title="What does 'industry' bring to mind?",
    body="Smoke from tall chimneys, roaring machines, rows of workers? That picture is only part of the story. For many decades after the first factories came up, most goods in Britain were still made by hand: by craftspeople, women and children in homes and small workshops.\n\n"
         "This chapter looks at how industrialisation really happened in Britain, why many industrialists preferred hand labour to machines, what happened to India's famous weavers under the East India Company, and how Indian factories finally came up and found buyers for their goods."),
  blk("s1.inspiration", "inspiration", title="The industrialist who dreamt for India", person="Jamsetji Nusserwanji Tata", years="1839–1904",
    body="Jamsetji Tata began in trade with China and England. In 1877 he opened the **Empress Mill** in Nagpur, one of India's most modern cotton mills, with good working conditions for its time.\n\n"
         "He dreamt of three things India needed: a steel plant, a hydroelectric power plant and a world-class institute of science. All three came true after his death: Tata Steel at Jamshedpur (1907), the hydroelectric project in the Western Ghats, and the Indian Institute of Science in Bengaluru (1909).",
    future="Understanding industry helps in careers in engineering, management, economics, labour law and entrepreneurship."),
  C.socratic("s1.socratic", "Before factories, were goods produced for the international market?",
    ["Yes, by peasants and artisans in the countryside, financed by merchants", "No, nothing was traded internationally", "Only in China"], 0,
    "Even before factories, large-scale production for international markets took place in villages. Historians call this proto-industrialisation."),
 ]},
 {"id": "s2", "title": "Proto-industrialisation and the coming of the factory", "blocks": [
  blk("s2.thm", "theory", title="Industry before factories", revision=True,
    body="Even before factories began to dot the landscape in England and Europe, there was **large-scale industrial production for an international market**. It was not based in factories. Many historians call this phase **proto-industrialisation**.\n\n"
         "- In the 17th and 18th centuries, **merchants from the towns** in Europe moved to the **countryside**, supplying money to peasants and artisans and persuading them to produce for an international market.\n"
         "- They could not expand production within towns because powerful **urban crafts and trade guilds** controlled production, regulated competition and prices, and restricted the entry of new people. Rulers granted guilds the monopoly right to produce and trade in specific products.\n"
         "- In the countryside, poor peasants and artisans happily agreed: open fields were disappearing and the **commons** were being **enclosed**, so they needed new sources of income.\n"
         "- **Example:** a merchant clothier in England bought wool from a wool stapler and carried it to spinners; the yarn went to weavers, fullers and dyers. Finishing was done in **London** before the cloth was sold in international markets.\n"
         "- The proto-industrial system was part of a network of commercial exchanges controlled by merchants, with a close relationship between the town and the countryside."),
  blk("s2.factory", "theory", title="The coming up of the factory", revision=True,
    body="- The earliest factories in England came up by the **1730s**, and their number multiplied in the late 18th century.\n"
         "- **Cotton** was the first symbol of the new era. In **1760** Britain imported **2.5 million pounds** of raw cotton; by **1787** this had soared to **22 million pounds**.\n"
         "- A series of inventions increased the efficiency of each step of production (carding, twisting and spinning, and rolling). **Richard Arkwright** created the **cotton mill**, bringing all the processes under one roof and management, which allowed careful supervision, quality control and regulation of labour.\n\n"
         "**The pace of change was slow:**\n- Cotton was the leading sector until the 1840s; then **iron and steel** led, with railway expansion (in England from the 1840s, in the colonies from the 1860s). By **1873** Britain's iron and steel exports were worth about **£77 million**, double its cotton exports.\n"
         "- Even at the end of the 19th century, **less than 20 per cent** of the total workforce was employed in technologically advanced industrial sectors.\n"
         "- **James Watt** improved Newcomen's steam engine and patented it in **1781**; Matthew Boulton manufactured it. Yet by the beginning of the 19th century there were **no more than 321 steam engines** in all of England (80 in cotton, 9 in wool, the rest in mining, canal works and ironworks).\n"
         "- New technology was expensive, machines broke down and repairs were costly, so industrialists were cautious. The typical worker in the mid-19th century was not a machine operator but a traditional craftsperson or labourer."),
  C.kc("s2.check", "Why did merchants in the 17th and 18th centuries turn to the countryside?",
    [("Powerful guilds in the towns restricted new producers", ""), ("Towns had no workers at all", "Towns had artisans, but guilds controlled who could produce."),
     ("Factories were cheaper in villages", "There were no factories yet."), ("The government banned trade in towns", "It was the guilds, not a ban.")],
    "Urban guilds controlled production and restricted entry, so merchants turned to rural peasants and artisans."),
  C.kc("s2.check2", "Who created the cotton mill?",
    [("Richard Arkwright", ""), ("James Watt", "Watt improved the steam engine."), ("James Hargreaves", "Hargreaves invented the Spinning Jenny."), ("Matthew Boulton", "Boulton manufactured Watt's engine.")],
    "Richard Arkwright brought all the processes under one roof."),
 ]},
 {"id": "s3", "title": "Hand labour, steam power and the life of workers", "blocks": [
  blk("s3.thm", "theory", title="Why not machines everywhere?", revision=True,
    body="In Victorian Britain there was **no shortage of human labour**. Poor peasants and vagrants moved to the cities in large numbers in search of jobs. Industrialists had no problem of labour shortage or high wage costs, so they did not want machines that needed large capital investment.\n\n"
         "- In many industries the demand for labour was **seasonal**: gasworks and breweries were busy through the cold months; bookbinders and printers needed extra hands before Christmas; ship repairing and spring cleaning took place in summer. Industrialists preferred hand labour, employing workers for the season.\n"
         "- Many products could be made only by hand. In mid-19th-century Britain, **500 varieties of hammers** and **45 kinds of axes** were produced; this needed human skill, not mechanical technology.\n"
         "- The **upper classes** (aristocrats and the bourgeoisie) preferred things produced by hand. Hand-made products symbolised refinement and class; they were better finished and individually designed. Machine-made goods were for export to the colonies.\n"
         "- In countries with a labour shortage, like **America**, industrialists were keen on mechanical power."),
  blk("s3.table", "markdown_table", title="Hand labour vs machines in 19th-century Britain", revision=True, body=HANDvsMACH),
  blk("s3.workers", "theory", title="The life of the workers", revision=True,
    body="- The abundance of labour meant that **jobs were hard to get**. Getting a job depended on existing networks of friendship and kin relations.\n"
         "- The **seasonality** of work meant prolonged periods without work. After the busy season, workers were back on the streets.\n"
         "- Wages increased somewhat in the early 19th century, but prices rose too, so real income fell. In bad times about 10 per cent of the urban population was extremely poor; during the economic slump of the **1830s**, **35 to 75 per cent** were unemployed in different regions.\n"
         "- **Fear of unemployment** made workers hostile to new technology. When the **Spinning Jenny** was introduced in the woollen industry, **women** who survived on hand spinning **attacked the new machines**, because a worker could now turn many spindles with one wheel, reducing the need for labour.\n"
         "- After the 1840s, building activity in the cities and **railway construction** opened new opportunities: the number of workers in transport industries doubled in the 1840s and doubled again in the next 30 years."),
  C.kc("s3.check", "Why did women in the woollen industry attack the Spinning Jenny?",
    [("It reduced the need for labour and threatened their jobs", ""), ("It was too heavy to use", "The machine was meant to speed up spinning."),
     ("It produced poor cloth", "The issue was unemployment."), ("It was very noisy", "The fear was of losing work.")],
    "One worker could turn several spindles at once, so hand spinners feared unemployment."),
 ]},
 {"id": "s4", "title": "Industrialisation in the colonies: India's weavers", "blocks": [
  blk("s4.thm", "theory", title="The age of Indian textiles", revision=True,
    body="Before the age of machine industries, **silk and cotton goods from India dominated the international market** in textiles. Coarse cotton was produced in many countries, but the **finer varieties** came from India.\n\n"
         "- **Armenian and Persian merchants** took goods from Punjab to Afghanistan, eastern Persia and Central Asia.\n- Pre-colonial ports: **Surat** on the Gujarat coast connected India to the Gulf and Red Sea ports; **Masulipatam** on the Coromandel coast and **Hoogly** in Bengal had trade links with Southeast Asian ports.\n"
         "- Indian merchants and bankers financed production, carried goods and supplied exporters; supply merchants linked the port towns to the inland regions.\n\n"
         "**Breakdown:** by the **1750s** this network was breaking down as the European companies gained power, securing local concessions and monopoly rights. **Surat and Hoogly decayed**; exports from them fell dramatically, credit dried up and local bankers went bankrupt. "
         "In the last years of the 17th century, the gross value of trade through Surat had been **Rs 16 million**; by the 1740s it had slumped. New ports, **Bombay and Calcutta**, grew under colonial power, and trade passed into the hands of European companies and European ships."),
  blk("s4.weavers", "theory", title="What happened to the weavers?", revision=True,
    body="After the East India Company established political power in Bengal and the Carnatic in the 1760s and 1770s, it tried to **eliminate competition, control costs and ensure regular supplies** of cotton and silk goods:\n\n"
         "- It tried to eliminate the existing traders and brokers connected with the cloth trade and to establish more direct control over the weaver.\n"
         "- It appointed a paid servant called the **gomastha** to supervise weavers, collect supplies and examine the quality of cloth.\n"
         "- It prevented Company weavers from dealing with other buyers through a **system of advances**: once an order was placed, the weavers were given loans to buy raw material, and those who took loans had to hand over the cloth to the gomastha.\n\n"
         "The gomasthas were outsiders with no long-term social link with the village. They acted arrogantly, marched into villages with sepoys and peons, and punished weavers for delays, often beating and flogging them. Weavers lost the space to bargain for prices, and the price they received from the Company was miserably low. "
         "In many places in the Carnatic and Bengal, weavers **deserted their villages**, some **revolted** with the village traders, and many refused loans, closed their workshops and took to **agricultural labour**."),
  blk("s4.table", "markdown_table", title="The Company's control over weavers", revision=True, body=WEAVERS),
  blk("s4.manchester", "theory", title="Manchester comes to India", revision=True,
    body="In **1772**, Henry Patullo, a Company official, said the demand for Indian textiles could never fall. Yet by the beginning of the 19th century Indian textile exports began a long decline: in **1811–12**, piece-goods were **33 per cent** of India's exports; by **1850–51**, no more than **3 per cent**.\n\n"
         "- **Manchester** industrialists pressured the government to impose import duties on cotton textiles in Britain, so their goods faced no competition there, and persuaded the Company to sell British manufactures in Indian markets.\n"
         "- At the end of the 18th century there was virtually no import of cotton piece-goods into India; by **1850** they were over **31 per cent** of the value of Indian imports, and by the **1870s** over **50 per cent**.\n\n"
         "**Weavers faced two problems:** their **export market collapsed** and the **local market shrank**, flooded with cheaper machine-made Manchester goods. And they could not get **raw cotton** of good quality: when the **American Civil War** broke out in the **1860s** and cotton supplies from the US were cut off, Britain turned to India. Raw cotton exports from India rose, prices shot up, and Indian weavers were starved of supplies and forced to buy raw cotton at exorbitant prices. "
         "By the end of the 19th century, factories in India too began production, flooding the market with machine goods."),
  C.kc("s4.check", "Who was a gomastha?",
    [("A paid servant of the Company who supervised weavers, collected supplies and checked quality", ""), ("A weaver who owned a factory", "Gomasthas were Company servants."),
     ("A Manchester industrialist", "Gomasthas worked in Indian villages."), ("A jobber in a Bombay mill", "Jobbers recruited mill workers in the 20th century.")],
    "The gomastha was the Company's paid agent over the weavers."),
  C.kc("s4.check2", "What effect did the American Civil War of the 1860s have on Indian weavers?",
    [("Raw cotton exports from India rose and weavers had to buy raw cotton at very high prices", ""), ("Weavers got cheap raw cotton from America", "Supplies from the US were cut off."),
     ("Manchester stopped exporting to India", "Manchester goods kept flooding India."), ("Weavers began exporting to America", "The war reduced, not increased, Indian weavers' opportunities.")],
    "Britain turned to India for raw cotton, so prices shot up and weavers were starved of supplies."),
 ]},
 {"id": "s5", "title": "Factories come up in India", "blocks": [
  blk("s5.thm", "theory", title="The first mills and the first entrepreneurs", revision=True,
    body="- The **first cotton mill in Bombay** came up in **1854** and went into production two years later. By 1862 four mills were at work with 94,000 spindles and 2,150 looms.\n"
         "- The **first jute mill in Bengal** came up in **1855**, and another in 1862. In north India, the **Elgin Mill** started in **Kanpur** in the 1860s, and a year later the **first cotton mill of Ahmedabad** was set up. By **1874** the first spinning and weaving mill of **Madras** began production.\n\n"
         "**Early entrepreneurs** had made money in trade, especially with China:\n- **Dwarkanath Tagore** made his fortune in the China trade and set up **six joint-stock companies** in the 1830s and 1840s.\n"
         "- In Bombay, **Parsis like Dinshaw Petit and Jamsetjee Nusserwanjee Tata** built huge industrial empires, with wealth partly from exports to China and partly from raw cotton shipments to England.\n"
         "- **Seth Hukumchand**, a Marwari businessman who set up the **first Indian jute mill in Calcutta in 1917**, also traded with China, as did the father and grandfather of the industrialist **G. D. Birla**.\n"
         "- As colonial control tightened, Indian businessmen were barred from trading in many goods. Until the First World War, **European Managing Agencies** (such as Bird Heiglers & Co., Andrew Yule and Jardine Skinner & Co.) controlled a large sector of Indian industry.\n\n"
         "**Where did the workers come from?** Mostly from neighbouring districts. In **1911**, half the workers in Bombay's cotton industries came from the neighbouring district of **Ratnagiri**; Kanpur's mills got most of their hands from villages in Kanpur district. "
         "Getting a job was difficult; industrialists used a **jobber**, usually an old and trusted worker, to recruit people from his village, help them settle and lend money in a crisis. Over time jobbers began demanding money and gifts and controlling workers' lives. "
         "Factory workers grew from **584,000 in 1901** to over **2,436,000 by 1946**."),
  blk("s5.growth", "theory", title="Peculiarities of industrial growth", revision=True,
    body="- European Managing Agencies invested in **tea and coffee plantations, mining, indigo and jute**, mostly for export, not for sale in India.\n"
         "- Indian businessmen avoided competing with Manchester goods. Since yarn was not an important part of British imports, early Indian cotton mills produced **coarse cotton yarn** rather than fabric, and much of it was **exported to China**.\n"
         "- In the first decade of the 20th century the **Swadeshi movement** boycotted foreign cloth, and industrial groups pressed for tariff protection. From **1906**, Indian yarn exports to China declined as Chinese and Japanese mills flooded that market, so Indian industrialists shifted from yarn to **cloth**. Cotton piece-goods production in India **doubled between 1900 and 1912**.\n"
         "- **The First World War** created a dramatically new situation. British mills were busy with war production, so Manchester imports into India declined. Indian mills suddenly had a vast home market and also supplied war needs: **jute bags, cloth for army uniforms, tents, leather boots, horse and mule saddles**. After the war, **Manchester could never recapture its old position** in India.\n\n"
         "**Small-scale industries predominate:** large factories were only a small segment; most production took place in small workshops and households. Handloom production actually **expanded** in the 20th century, helped by technology like the **fly shuttle**, a mechanical device moved by ropes and pulleys that places the weft threads into the warp, increasing productivity per worker. "
         "By **1941**, over **35 per cent** of handlooms in India were fitted with fly shuttles (70–80 per cent in Travancore, Madras, Mysore, Cochin and Bengal). Weavers of coarse cloth suffered when harvests failed; weavers of fine cloth had steadier demand from the well-to-do. Whole families, including women and children, worked long hours."),
  blk("s5.market", "theory", title="Market for goods: advertisements", revision=True,
    body="New consumers had to be created. **Advertisements** made products appear desirable and necessary.\n\n- Manchester cloth bundles carried labels **'MADE IN MANCHESTER'**, a mark of quality.\n"
         "- Labels carried images of **Indian gods and goddesses** like Krishna or Saraswati, to make the product seem familiar and divinely approved.\n- Manufacturers printed **calendars** to popularise their products; calendars hung in tea shops and homes for a whole year. Images of important personages, emperors and nawabs also adorned advertisements.\n"
         "- When Indian manufacturers advertised, the nationalist message was clear: **'Be Indian, Buy Indian'** (Swadeshi). Taking care of the nation meant buying products produced by Indians."),
  blk("s5.timeline", "markdown_table", title="Timeline of the chapter", revision=True, body=TIMELINE),
  C.kc("s5.check", "Who set up the first Indian jute mill in Calcutta in 1917?",
    [("Seth Hukumchand", ""), ("Dwarkanath Tagore", "He set up six joint-stock companies in the 1830s–40s."), ("Dinshaw Petit", "He was a Parsi industrialist in Bombay."), ("Henry Patullo", "He was a Company official in 1772.")],
    "Seth Hukumchand, a Marwari businessman."),
  C.kc("s5.check2", "How did the First World War help Indian industries?",
    [("Manchester imports fell and Indian mills supplied a vast home market and war needs", ""), ("Britain built many mills in India during the war", "British mills were busy at home with war production."),
     ("Indian yarn exports to China doubled", "Exports to China had declined from 1906."), ("The fly shuttle was banned", "The fly shuttle spread in the 20th century.")],
    "With Manchester busy with war production, Indian mills grew; Manchester never regained its old position."),
 ]},
 {"id": "s6", "title": "Remember, avoid, practise", "blocks": [
  blk("s6.memory", "memory_trick", title="Memory tricks",
    body="- **Proto = before:** merchants + villages + no factories.\n- **Why hand labour? \"C-S-V-T\":** **C**heap labour, **S**easonal demand, **V**ariety of designs, **T**aste of the rich.\n"
         "- **Company control = \"G-A\":** **G**omastha + **A**dvances.\n- **Indian exports 33% → 3%; Manchester imports 0 → 31% → 50%.**\n- **First mills: Bombay 1854, Bengal jute 1855, Ahmedabad 1861, Madras 1874.**"),
  blk("s6.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Thinking machines replaced hand labour quickly in Britain: change was slow; less than 20% worked in advanced sectors by the end of the 19th century.\n2. Confusing Arkwright (cotton mill), Hargreaves (Spinning Jenny) and Watt (steam engine).\n"
         "3. Writing that the American Civil War reduced cotton exports from India: it **increased** them.\n4. Calling the gomastha a weaver: he was the Company's paid servant.\n5. Saying early Indian mills made fine cloth for India: they made **coarse yarn**, much of it for China.\n"
         "6. Remember: this chapter is for periodic assessment only in 2025-26, not the board paper."),
  blk("s6.tip", "teacher_tip", title="Try this in class",
    body="Collect old product labels, calendar art and advertisements (or images of them). Students identify the techniques used: gods and goddesses, famous personalities, 'Made in Manchester', 'Be Indian, Buy Indian'. Then each group designs an advertisement for a 1920s Indian mill product."),
  blk("s6.reflection", "reflection", title="Think and explain",
    body="If you were a Victorian industrialist with plenty of cheap workers, would you buy expensive machines? Give two reasons for your answer."),
  blk("s6.connection", "connection", title="Where this leads",
    body="- **Chapter 2, Nationalism in India:** the Swadeshi movement and the boycott of foreign cloth helped Indian mills.\n- **Geography, Manufacturing Industries:** today's cotton textile, jute and iron and steel industries.\n"
         "- **Economics, Sectors of the Indian Economy:** organised and unorganised sectors, like factories and household units."),
  blk("s6.mastery", "mastery", title="Mastery challenge",
    body="Explain in about 100 words how the East India Company's policies affected Indian weavers.\n\n"
         "**Model answer:** The Company removed existing traders and brokers and appointed gomasthas to supervise weavers, collect cloth and check quality. Through a system of advances, weavers took loans to buy raw material and had to sell their cloth only to the gomastha, so they lost the freedom to bargain and sell to others, and received very low prices. "
         "Gomasthas were outsiders who punished weavers for delays. Many weavers deserted their villages, revolted or became labourers. Later, Manchester imports destroyed their markets, and the American Civil War made raw cotton scarce and costly."),
  blk("s6.summary", "summary", title="Chapter summary",
    body="- Proto-industrialisation: merchants financed rural producers for international markets before factories.\n- Factories came up from the 1730s; cotton and then iron and steel led; but change was slow and most workers remained craftspeople and labourers.\n"
         "- Cheap labour, seasonal demand, variety and the taste of the rich made many industrialists prefer hand labour; workers faced unemployment and feared machines like the Spinning Jenny.\n"
         "- India dominated the fine textile trade; the Company's gomasthas and advances, Manchester imports and the cotton shortage of the 1860s ruined many weavers.\n"
         "- Indian factories (Bombay 1854 onwards) were set up by traders enriched by the China trade; workers came through jobbers; the Swadeshi movement and the First World War helped Indian industry; small-scale and handloom production still predominated.\n- Advertisements created markets: gods on labels, calendars, and 'Be Indian, Buy Indian'."),
  blk("s6.examtips", "exam_tips", title="Exam tips",
    body="- In 2025-26 this chapter is assessed in **periodic tests** only, not in the board paper.\n- Typical questions: proto-industrialisation, why hand labour was preferred, gomasthas and the system of advances, effects of the First World War, the role of advertisements.\n"
         "- Use the numbers: 33% → 3%, 31% → 50%, 321 steam engines, 1854 Bombay mill."),
  blk("s6.flash1", "flashcard", front="What is proto-industrialisation?", back="Large-scale production for international markets in villages, financed by merchants, before factories."),
  blk("s6.flash2", "flashcard", front="What was the system of advances?", back="Company loans to weavers for raw material; the cloth then had to be handed over to the gomastha."),
  blk("s6.flash3", "flashcard", front="What was the fly shuttle?", back="A device moved by ropes and pulleys that puts the weft into the warp, raising a weaver's productivity."),
  blk("s6.flash4", "flashcard", front="When and where did the first cotton mill in India come up?", back="Bombay, 1854 (production from 1856)."),
 ]},
]

# ---------------- NCERT exercises ----------------
W("ex1a", "very_short_answer", WORK, "Explain why women workers in Britain attacked the Spinning Jenny.",
  ["The Spinning Jenny allowed one worker to turn a number of spindles with one wheel, so fewer hands were needed to spin yarn.", "Women who survived on hand spinning feared losing their jobs, so they attacked the new machines."], source=ex("1(a)"))
W("ex1b", "very_short_answer", PROTO, "Explain why, in the seventeenth century, merchants from towns in Europe began employing peasants and artisans within the villages.",
  ["Powerful urban crafts and trade guilds controlled production, regulated prices and competition and restricted new producers, so merchants could not expand in the towns.",
   "In the countryside, poor peasants and artisans needed new income as open fields disappeared and commons were enclosed, so they agreed to produce for the merchants."], source=ex("1(b)"))
W("ex1c", "very_short_answer", COL, "Explain why the port of Surat declined by the end of the eighteenth century.",
  ["European companies gained power, securing concessions and monopoly rights, and the network of Indian merchants broke down; exports fell, credit dried up and local bankers went bankrupt.",
   "Trade shifted to new colonial ports like Bombay and Calcutta, controlled by European companies and carried on European ships."], source=ex("1(c)"))
W("ex1d", "very_short_answer", COL, "Explain why the East India Company appointed gomasthas to supervise weavers in India.",
  ["The Company wanted to eliminate competition from other traders, control costs and ensure regular supplies of cotton and silk goods.",
   "Gomasthas supervised the weavers, collected supplies and examined the quality of the cloth, establishing direct Company control."], source=ex("1(d)"))
C.tf("ex2a", BRIT, "At the end of the nineteenth century, 80 per cent of the total workforce in Europe was employed in the technologically advanced industrial sector.", False,
     "Less than 20 per cent was employed in technologically advanced sectors; traditional industries still employed most workers.", source=ex("2(a)"))
C.tf("ex2b", COL, "The international market for fine textiles was dominated by India till the eighteenth century.", True,
     "Fine Indian cotton and silk goods dominated international textile markets before machine industries.", source=ex("2(b)"))
C.tf("ex2c", COL, "The American Civil War resulted in the reduction of cotton exports from India.", False,
     "When American supplies were cut off, Britain turned to India and raw cotton exports from India increased.", source=ex("2(c)"))
C.tf("ex2d", IND, "The introduction of the fly shuttle enabled handloom workers to improve their productivity.", True,
     "The fly shuttle increased productivity per worker and speeded up production.", source=ex("2(d)"))
W("ex3", "short_answer", PROTO, "Explain what is meant by proto-industrialisation.",
  ["Proto-industrialisation was the phase of large-scale industrial production for an international market before factories, not based in factories.",
   "Merchants from the towns supplied money and raw material to peasants and artisans in the countryside and persuaded them to produce for the international market.",
   "It was part of a network of commercial exchanges controlled by merchants, with a close link between town and countryside (e.g. wool to spinners, weavers, fullers, dyers, finished in London)."], source=ex(3))
W("ex4", "long_answer", WORK, "Why did some industrialists in nineteenth-century Europe prefer hand labour over machines?",
  ["There was no shortage of human labour; poor peasants and vagrants crowded the cities, so labour was cheap and plentiful.",
   "Machines needed large capital, often broke down and were costly to repair, so industrialists were cautious.",
   "Demand in many industries was seasonal (gasworks, breweries, printers, bookbinders), so seasonal workers were preferred to costly machines that would lie idle.",
   "Many products with intricate designs and shapes (500 varieties of hammers, 45 kinds of axes) needed human skill.",
   "The upper classes preferred hand-made goods as a symbol of refinement and class; machine-made goods were for the colonies."], source=ex("discuss 1"))
W("ex5", "long_answer", COL, "How did the East India Company procure regular supplies of cotton and silk textiles from Indian weavers?",
  ["After gaining political power, the Company tried to eliminate competition, control costs and ensure regular supplies.",
   "It removed the existing traders and brokers connected with the cloth trade to get direct control over the weavers.",
   "It appointed paid servants called gomasthas to supervise weavers, collect supplies and examine the quality of cloth.",
   "Through the system of advances, weavers took loans to buy raw material and had to hand over their cloth to the gomastha, so they could not sell to other buyers.",
   "Gomasthas often used force, beating and flogging weavers for delays; weavers lost bargaining power and received very low prices."], source=ex("discuss 2"))
W("ex6", "long_answer", IND, "Explain the impact of the First World War on industrial production in India.",
  ["Before the war, industrial growth was slow; the war created a dramatically new situation.",
   "British mills were busy with war production to meet army needs, so Manchester imports into India declined.",
   "Indian mills suddenly had a vast home market to supply.",
   "As the war went on, Indian factories also supplied war needs: jute bags, cloth for army uniforms, tents, leather boots, and horse and mule saddles; new factories were set up and old ones ran multiple shifts.",
   "After the war Manchester could never recapture its old position in the Indian market, and local industrialists consolidated their position."], source=ex("discuss 4"))

# ---------------- MCQs ----------------
M("mcq01", PROTO, "Which term do historians use for industrial production for international markets before factories?", [("Proto-industrialisation", ""), ("Globalisation", "That is a modern process."), ("Imperialism", "That is political domination."), ("Swadeshi", "Swadeshi was a nationalist movement.")], "Proto-industrialisation.")
M("mcq02", PROTO, "Who controlled production, prices and entry of new people in European towns?", [("Crafts and trade guilds", ""), ("Factory owners", "There were no factories yet."), ("Gomasthas", "Gomasthas were Company servants in India."), ("Jobbers", "Jobbers recruited mill workers in India.")], "Guilds, often with monopoly rights from rulers.")
M("mcq03", PROTO, "In England, where was cloth finished before export?", [("London", ""), ("Manchester", "Manchester rose later as a factory centre."), ("Surat", "Surat is in India."), ("Ahmedabad", "Ahmedabad is in India.")], "London was the finishing centre.", "medium")
M("mcq04", PROTO, "Why did poor peasants in the countryside agree to work for merchants?", [("Open fields were disappearing and commons were being enclosed", ""), ("They were forced by the guilds", "Guilds were in towns."), ("Factories paid more", "There were no factories."), ("The king ordered it", "It was their need for income.")], "They needed new sources of income.", "medium")
M("mcq05", BRIT, "By when had the earliest factories come up in England?", [("The 1730s", ""), ("The 1830s", "That is a century later."), ("The 1630s", "That is too early."), ("The 1930s", "That is far too late.")], "By the 1730s.")
M("mcq06", BRIT, "Britain's raw cotton imports rose from 2.5 million pounds in 1760 to how much by 1787?", [("22 million pounds", ""), ("5 million pounds", "The rise was much bigger."), ("100 million pounds", "The figure was 22 million."), ("2.5 million pounds", "It rose sharply.")], "22 million pounds.", "medium")
M("mcq07", BRIT, "Who improved Newcomen's steam engine and patented it in 1781?", [("James Watt", ""), ("Richard Arkwright", "Arkwright created the cotton mill."), ("Matthew Boulton", "Boulton manufactured the engine."), ("James Hargreaves", "Hargreaves invented the Spinning Jenny.")], "James Watt.")
M("mcq08", BRIT, "How many steam engines were there in all of England at the beginning of the 19th century?", [("No more than 321", ""), ("About 32,000", "There were very few."), ("Exactly 80", "80 were in the cotton industry."), ("About 3 million", "There were very few.")], "No more than 321, showing how slow the change was.", "medium")
M("mcq09", BRIT, "Which became the leading industrial sector after the 1840s in Britain?", [("Iron and steel", ""), ("Cotton", "Cotton led until the 1840s."), ("Wool", "Wool was a traditional industry."), ("Jute", "Jute was important in Bengal.")], "Iron and steel, with railway expansion.")
M("mcq10", BRIT, "At the end of the 19th century, what share of the total workforce worked in technologically advanced sectors?", [("Less than 20 per cent", ""), ("About 80 per cent", "Most workers were still in traditional industries."), ("About 50 per cent", "The share was below 20 per cent."), ("Over 90 per cent", "The share was below 20 per cent.")], "Less than 20 per cent.")
M("mcq11", WORK, "In mid-19th-century Britain, how many varieties of hammers were produced?", [("500", ""), ("45", "45 was the number of kinds of axes."), ("50", "The figure was 500."), ("5", "The figure was 500.")], "500 varieties of hammers and 45 kinds of axes.", "medium")
M("mcq12", WORK, "Why did the upper classes prefer hand-made goods?", [("They symbolised refinement and class and were individually designed", ""), ("They were cheaper", "Hand-made goods were usually costlier."), ("Machines were banned", "Machines were not banned."), ("They were made in factories", "Hand-made goods were not factory-made.")], "Hand-made goods were seen as better finished and refined.")
M("mcq13", WORK, "Which country, facing a labour shortage, was keen on mechanical power?", [("America", ""), ("Britain", "Britain had plenty of labour."), ("India", "India had plenty of labour."), ("China", "The chapter names America.")], "America.")
M("mcq14", WORK, "Who invented the Spinning Jenny in 1764?", [("James Hargreaves", ""), ("James Watt", "Watt improved the steam engine."), ("Richard Arkwright", "Arkwright created the cotton mill."), ("Henry Patullo", "Patullo was a Company official.")], "James Hargreaves.", "medium")
M("mcq15", WORK, "During the economic slump of the 1830s, what share of people were unemployed in different regions of Britain?", [("35 to 75 per cent", ""), ("5 to 10 per cent", "Unemployment was much higher."), ("90 per cent everywhere", "It varied from 35 to 75 per cent."), ("None", "Unemployment was very high.")], "35 to 75 per cent.", "medium")
M("mcq16", WORK, "Which development after the 1840s opened new job opportunities for workers in Britain?", [("Building activity and railway construction", ""), ("The Spinning Jenny", "It reduced jobs."), ("The guild system", "Guilds were older institutions."), ("The system of advances", "That was in India.")], "Workers in transport industries doubled in the 1840s.")
M("mcq17", COL, "Which port on the Gujarat coast connected India to the Gulf and Red Sea ports?", [("Surat", ""), ("Masulipatam", "Masulipatam was on the Coromandel coast."), ("Hoogly", "Hoogly was in Bengal."), ("Calcutta", "Calcutta grew later under colonial rule.")], "Surat.")
M("mcq18", COL, "Which merchants took goods from Punjab to Afghanistan, Persia and Central Asia?", [("Armenian and Persian merchants", ""), ("Manchester merchants", "They sold British goods in India later."), ("Chinese merchants", "The chapter names Armenian and Persian merchants."), ("Marwari merchants", "The chapter names Armenian and Persian merchants.")], "Armenian and Persian merchants.", "medium")
M("mcq19", COL, "Which new ports grew under colonial power as Surat and Hoogly decayed?", [("Bombay and Calcutta", ""), ("Masulipatam and Surat", "These were old ports."), ("Delhi and Agra", "These are inland cities."), ("Madras and Hoogly", "Hoogly decayed.")], "Bombay and Calcutta.")
M("mcq20", COL, "What was the 'system of advances'?", [("Loans to weavers for raw material, with the cloth handed over to the gomastha", ""), ("Advance payments by weavers to the Company", "The Company gave the loans."), ("Advance booking of trains", "It was about weavers."), ("A tax on cloth exports", "It was a system of loans.")], "It tied weavers to the Company.")
M("mcq21", COL, "Why were weavers often in conflict with gomasthas?", [("Gomasthas were arrogant outsiders who punished weavers for delays", ""), ("Gomasthas paid very high prices", "They paid very low prices."), ("Gomasthas were village elders", "They were outsiders."), ("Gomasthas helped weavers sell to other buyers", "They prevented that.")], "Weavers were often beaten and flogged for delays.", "medium")
M("mcq22", COL, "In 1811–12 piece-goods were 33 per cent of India's exports. What was the share by 1850–51?", [("No more than 3 per cent", ""), ("50 per cent", "Exports fell sharply."), ("33 per cent", "Exports fell sharply."), ("31 per cent", "31 per cent was the share of cotton piece-goods in imports by 1850.")], "No more than 3 per cent.", "medium")
M("mcq23", COL, "By the 1870s, what share of the value of Indian imports was cotton piece-goods?", [("Over 50 per cent", ""), ("3 per cent", "That was the share of piece-goods in exports by 1850–51."), ("Nil", "Imports were huge."), ("10 per cent", "It was over 50 per cent.")], "Over 50 per cent.", "medium")
M("mcq24", COL, "Who said in 1772 that the demand for Indian textiles could never reduce?", [("Henry Patullo", ""), ("James Watt", "He improved the steam engine."), ("Dwarkanath Tagore", "He was an Indian entrepreneur."), ("Richard Arkwright", "He created the cotton mill.")], "Henry Patullo, a Company official.", "medium")
M("mcq25", IND, "When did the first cotton mill in Bombay come up?", [("1854", ""), ("1874", "1874 was Madras."), ("1917", "1917 was Hukumchand's jute mill."), ("1906", "1906 is when yarn exports to China declined.")], "1854, with production from 1856.")
M("mcq26", IND, "The Elgin Mill was started in which city?", [("Kanpur", ""), ("Ahmedabad", "Ahmedabad's first mill came a year later."), ("Madras", "Madras's first mill came in 1874."), ("Calcutta", "Calcutta had jute mills.")], "Kanpur, in the 1860s.", "medium")
M("mcq27", IND, "Who set up six joint-stock companies in the 1830s and 1840s?", [("Dwarkanath Tagore", ""), ("Seth Hukumchand", "He set up a jute mill in 1917."), ("Dinshaw Petit", "He was a Bombay Parsi industrialist."), ("G. D. Birla", "Birla was a 20th-century industrialist.")], "Dwarkanath Tagore.")
M("mcq28", IND, "Who was a 'jobber'?", [("A trusted worker who recruited people from his village for the mills", ""), ("A Company official over weavers", "That was the gomastha."), ("A Manchester industrialist", "Jobbers worked in Indian mills."), ("A machine for weaving", "The fly shuttle was a device.")], "The jobber recruited and controlled mill workers.")
M("mcq29", IND, "In 1911, half the workers in Bombay's cotton mills came from which district?", [("Ratnagiri", ""), ("Kanpur", "Kanpur supplied Kanpur's mills."), ("Surat", "The chapter names Ratnagiri."), ("Nagpur", "The chapter names Ratnagiri.")], "The neighbouring district of Ratnagiri.", "medium")
M("mcq30", IND, "Early Indian cotton mills mainly produced:", [("coarse cotton yarn, much of it exported to China", ""), ("fine cloth for Britain", "They avoided competing with Manchester."), ("jute bags for Manchester", "Jute mills made bags; cotton mills made yarn."), ("steel", "They were cotton mills.")], "Yarn was not an important British import, so Indian mills made yarn.", "medium")
M("mcq31", IND, "Why did Indian industrialists shift from yarn to cloth production from 1906?", [("Yarn exports to China declined as Chinese and Japanese mills flooded China", ""), ("The British banned yarn", "There was no ban."), ("Cloth was cheaper to make", "The reason was the loss of the China market."), ("The fly shuttle was invented", "That was not the reason.")], "They also benefited from the Swadeshi boycott of foreign cloth.", "medium")
M("mcq32", IND, "Which of these did Indian factories supply for the First World War?", [("Jute bags, army uniforms, tents and leather boots", ""), ("Steam engines for Britain", "They supplied textiles and leather goods."), ("Spinning Jennies", "That was an 18th-century machine."), ("Silk for Manchester", "They supplied war needs.")], "War needs boosted Indian industry.")
M("mcq33", IND, "By 1941, what share of handlooms in India were fitted with fly shuttles?", [("Over 35 per cent", ""), ("Over 90 per cent", "It was over 35 per cent nationally."), ("Less than 5 per cent", "It was over 35 per cent."), ("Exactly 50 per cent", "It was over 35 per cent.")], "Over 35 per cent (70–80% in some regions).", "hard")
M("mcq34", IND, "What nationalist message did Indian manufacturers use in advertisements?", [("Be Indian, Buy Indian", ""), ("Made in Manchester", "That was on British cloth."), ("Go back Simon", "That was a protest slogan."), ("Vande Mataram only", "The advertising message was 'Be Indian, Buy Indian'.")], "Swadeshi in advertising.")
M("mcq35", IND, "Why did Manchester labels show images of Indian gods and goddesses?", [("To make the product seem familiar and divinely approved to Indian buyers", ""), ("Because the cloth was made in temples", "It was made in Manchester."), ("Because the British worshipped them", "It was a marketing technique."), ("To avoid taxes", "It was about attracting buyers.")], "Familiar images helped sell foreign goods.", "medium")
# ---------------- Assertion-reason ----------------
C.arq("ar1", WORK, "Many industrialists in Victorian Britain preferred hand labour.", "There was no shortage of human labour and wages were low.", 0,
      "R explains A.", "they did not want costly machines.", "cheap, plentiful labour explains it.")
C.arq("ar2", COL, "Indian weavers suffered after the East India Company established power.", "The Company paid weavers high prices through the gomasthas.", 2,
      "A is true; R is false: the Company paid miserably low prices.", "they lost bargaining power and markets.", "the prices were very low.")
C.arq("ar3", COL, "Indian weavers faced a shortage of raw cotton in the 1860s.", "The American Civil War cut off cotton supplies from the US, so Britain turned to India.", 0,
      "R explains A.", "they had to buy raw cotton at exorbitant prices.", "raw cotton exports from India rose.")
C.arq("ar4", IND, "Manchester could never recapture its old position in India after the First World War.", "During the war Indian mills captured the home market and supplied war needs.", 0,
      "R explains A.", "Indian industries consolidated their position.", "the war gave Indian mills the home market.")
C.arq("ar5", BRIT, "Technological change in 19th-century Britain was slow.", "New machines were expensive and often broke down.", 0,
      "R explains A.", "less than 20% worked in advanced sectors.", "cost and unreliability slowed adoption.")
C.arq("ar6", IND, "Handloom production in India expanded in the 20th century.", "The fly shuttle reduced the productivity of weavers.", 2,
      "A is true; R is false: the fly shuttle increased productivity.", "handlooms adopted new technology.", "the fly shuttle raised productivity.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", COL, "Name two pre-colonial ports and the regions they traded with.",
  ["Surat on the Gujarat coast traded with the Gulf and Red Sea ports.", "Masulipatam on the Coromandel coast and Hoogly in Bengal traded with Southeast Asian ports."], difficulty="easy")
W("vsa2", "very_short_answer", IND, "Who were the early Indian entrepreneurs, and where did their wealth come from?",
  ["Dwarkanath Tagore, Parsis like Dinshaw Petit and Jamsetjee Nusserwanjee Tata, Seth Hukumchand and the Birla family.", "Much of their wealth came from trade, especially with China, and raw cotton shipments to England."])
W("vsa3", "very_short_answer", IND, "How did advertisements help create a market for goods? Give two ways.",
  ["Labels with images of Indian gods and goddesses, or 'Made in Manchester', made products seem familiar and of good quality.", "Calendars hung in homes and shops for a whole year, and nationalist messages like 'Be Indian, Buy Indian' appealed to patriotism."])
W("sa1", "short_answer", WORK, "Describe the life of workers in 19th-century Britain.",
  ["Labour was abundant, so jobs were hard to get and depended on networks of friends and relatives.",
   "Work was seasonal, leaving workers unemployed for long periods; real wages fell as prices rose, and in the 1830s slump 35–75% were unemployed in different regions.",
   "Fear of unemployment made them hostile to machines like the Spinning Jenny; only after the 1840s did building and railway work open new opportunities."])
W("sa2", "short_answer", COL, "Why did the export of Indian textiles decline in the 19th century?",
  ["Manchester industrialists got import duties imposed on Indian cotton textiles in Britain, removing competition there.",
   "Cheap machine-made Manchester goods flooded the Indian market, so weavers lost both their export market and their local market.",
   "Weavers could not get good raw cotton, especially after the American Civil War raised prices; exports of piece-goods fell from 33% (1811–12) to 3% (1850–51)."])
W("la1", "long_answer", IND, "Describe the peculiarities of industrial growth in India in the early 20th century.",
  ["European Managing Agencies invested in tea, coffee, mining, indigo and jute, mostly for export rather than the Indian market.",
   "Indian mills avoided competing with Manchester and produced coarse yarn, much of it for China.",
   "From 1906, as China's market was lost to Chinese and Japanese mills, and with the Swadeshi boycott of foreign cloth, Indian mills shifted to cloth; piece-goods production doubled between 1900 and 1912.",
   "The First World War cut Manchester imports and gave Indian mills a vast home market and war orders.",
   "Small-scale and handloom production still predominated and even expanded, helped by the fly shuttle."])
# ---------------- Case based ----------------
W("cb1", "case_based", COL, "Read the source and answer the questions.\n\n*\"Once an order was placed, the weavers were given loans to purchase the raw material for their production. Those who took loans had to hand over the cloth they produced to the gomastha. They could not take it to any other trader.\"* (NCERT)\n\n"
  "(i) Who was the gomastha? (1)\n\n(ii) What was this system of loans called? (1)\n\n(iii) How did this system harm the weavers? (2)",
  ["(i) A paid servant of the East India Company who supervised weavers, collected supplies and examined the quality of cloth.", "(ii) The system of advances.",
   "(iii) Weavers could not sell to other buyers or bargain for better prices, and received miserably low prices; gomasthas punished them for delays, so many deserted their villages or gave up weaving."])
W("cb2", "case_based", WORK, "Read the source and answer the questions.\n\n*\"In Victorian Britain there was no shortage of human labour. Poor peasants and vagrants moved to the cities in large numbers in search of jobs, waiting for work. So industrialists had no problem of labour shortage or high wage costs.\"* (NCERT)\n\n"
  "(i) Who moved to the cities in search of jobs? (1)\n\n(ii) Why did industrialists not face high wage costs? (1)\n\n(iii) Give two other reasons why industrialists preferred hand labour. (2)",
  ["(i) Poor peasants and vagrants.", "(ii) Because labour was plentiful, so wages stayed low.",
   "(iii) Any two: machines were costly and broke down; demand was seasonal; products needed intricate designs that only skilled hands could make; the upper classes preferred hand-made goods."])
W("cb3", "case_based", IND, "Read the source and answer the questions.\n\n*\"Till the First World War, industrial growth was slow. The war created a dramatically new situation. With British mills busy with war production to meet the needs of the army, Manchester imports into India declined. Suddenly, Indian mills had a vast home market to supply.\"* (NCERT)\n\n"
  "(i) Why did Manchester imports into India decline during the war? (1)\n\n(ii) What new opportunity did Indian mills get? (1)\n\n(iii) Name two war needs supplied by Indian factories. (2)",
  ["(i) British mills were busy with war production to meet the needs of the army.", "(ii) A vast home market to supply.",
   "(iii) Any two: jute bags, cloth for army uniforms, tents, leather boots, horse and mule saddles."])

chapter = header(SUBJ, N, "The Age of Industrialisation", ["proto_industrialisation", "industrial_britain", "hand_labour_workers", "colonies_weavers", "indian_factories_market"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: this chapter is assessed only as part of Periodic Assessment (school tests) and is NOT evaluated in the board examination.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
