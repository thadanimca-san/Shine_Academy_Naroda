"""CBSE Class 10 History Ch 5: Print Culture and the Modern World (fully in the 2025-26 board syllabus)."""
import sys
from ss_common import make, header, path, SQP, SHINE, CB

ROOT = sys.argv[1]
SUBJ, N = "history", 5
PATH = path(SUBJ, "ch05_print_culture_and_the_modern_world")
C = make(SUBJ, N, "his10ch05")
blk, M, W = C.blk, C.m, C.w
EAST, EUR, IMPACT, C19, INDIA = ["print_east_asia"], ["print_europe_gutenberg"], ["print_revolution_impact"], ["nineteenth_century_print"], ["print_in_india"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 5 exercises", "question": n}

TIMELINE = ("| Year | Event |\n|---|---|\n| AD 594 | Books printed from woodblocks in China |\n| AD 768–770 | Buddhist missionaries bring hand-printing to Japan |\n| AD 868 | *Diamond Sutra*, the oldest Japanese printed book |\n"
            "| 1295 | Marco Polo returns to Italy with knowledge of woodblock printing |\n| 1448 | Gutenberg perfects his printing press; prints the Bible |\n| 1517 | Martin Luther's Ninety Five Theses |\n| 1558 | Roman Church's Index of Prohibited Books |\n"
            "| Mid-16th century | First printing press in India, at Goa (Portuguese missionaries) |\n| 1579 / 1713 | First Tamil book (Cochin) / first Malayalam book |\n| 1780 | James Augustus Hickey's *Bengal Gazette* |\n"
            "| 1821 | Rammohun Roy's *Sambad Kaumudi* |\n| 1822 | *Bombay Samachar* (Gujarati); Persian papers *Jam-i-Jahan Nama* and *Shamsul Akhbar* |\n| 1835 | Bentinck and Macaulay restore press freedom |\n"
            "| 1867 | Deoband Seminary founded |\n| 1876 | Rashsundari Debi's *Amar Jiban* |\n| 1878 | Vernacular Press Act |\n| 1908 | Tilak imprisoned for writing in *Kesari* |")
HAND_PRINT = ("| Handwritten manuscripts | Printed books |\n|---|---|\n| copied by scribes; slow, laborious and expensive | many copies made quickly and cheaply |\n| fragile and awkward to handle | sturdier and easy to circulate |\n"
              "| few copies; only for the rich and religious institutions | a new reading public: artisans, peasants, women, workers |\n| knowledge passed mainly by word of mouth | ideas spread widely, creating debate and dissent |")
LAWS = ("| Year | Press policy in colonial India |\n|---|---|\n| Before 1798 | little censorship; early controls aimed at Englishmen who criticised the Company |\n| 1820s | Calcutta Supreme Court regulations control press freedom; pro-British papers encouraged |\n"
        "| 1835 | Bentinck agrees to revise press laws; Macaulay's rules restore earlier freedoms |\n| After 1857 | demand to clamp down on the 'native' press |\n"
        "| 1878 | **Vernacular Press Act** (modelled on the Irish Press Laws): extensive rights to censor vernacular papers; presses could be seized |\n| 1908 | Tilak jailed for writing in *Kesari* in sympathy with Punjab revolutionaries |")

sections = [
 {"id": "s1", "title": "The power of the printed word", "blocks": [
  blk("s1.hook", "hook", title="Could a book start a revolution?",
    body="Before printing, a single book had to be copied by hand, letter by letter, for months. Only kings, priests and the very rich owned books. Then came the printing press, and a book could be made in hundreds of copies in days.\n\n"
         "Within a few decades, ideas that would once have stayed in one room spread across a continent: a monk's criticism split the Church, novels taught women to think for themselves, and newspapers made kings and colonial rulers afraid. "
         "This chapter follows print from East Asia to Europe and to India, and shows how it changed the way people thought, argued and dreamt of freedom."),
  blk("s1.inspiration", "inspiration", title="The reformer who used the press", person="Raja Rammohun Roy", years="1772–1833",
    body="Rammohun Roy knew many languages and believed that people should judge customs by reason. He campaigned against the cruel practice of widow immolation (sati) and for women's rights and modern education.\n\n"
         "He used print as his weapon: from **1821** he published the Bengali newspaper ***Sambad Kaumudi***, carrying his arguments to thousands of readers. His opponents replied through their own paper, and the debate itself, fought in print, helped bring about social reform.",
    future="Print culture leads to careers in journalism, publishing, editing, media, library science and communication."),
  C.socratic("s1.socratic", "Why were many rulers and priests afraid of the printing press?",
    ["It could spread rebellious and irreligious ideas they could not control", "It was too expensive to buy", "It made books harder to read"], 0,
    "Easy access to print meant ideas could spread widely without control; authorities feared dissent, as the Church did after Luther."),
 ]},
 {"id": "s2", "title": "The first printed books", "blocks": [
  blk("s2.thm", "theory", title="Print in China and Japan", revision=True,
    body="The earliest kind of print technology was developed in **China, Japan and Korea**: a system of **hand printing**.\n\n"
         "**China:**\n- From **AD 594**, books in China were printed by rubbing paper against the inked surface of **woodblocks**. Both sides of the thin, porous sheet could not be printed, so the traditional Chinese **'accordion book'** was folded and stitched at the side.\n"
         "- For a long time the **imperial state** was the major producer of printed material. China had a huge bureaucratic system that recruited its personnel through **civil service examinations**, and textbooks for these were printed in vast numbers.\n"
         "- By the 17th century, as urban culture bloomed, uses of print diversified: merchants used print in trade, reading became a leisure activity, and readers enjoyed fiction, poetry, autobiographies and romantic plays. Rich women began to read, and many published their own poetry and plays.\n"
         "- In the late 19th century, Western printing techniques and mechanical presses were imported as Western powers set up outposts in China. **Shanghai** became the hub of the new print culture.\n\n"
         "**Japan:**\n- **Buddhist missionaries from China** introduced hand-printing technology into Japan around **AD 768–770**.\n"
         "- The oldest Japanese book, printed in **AD 868**, is the Buddhist ***Diamond Sutra***, with six sheets of text and woodcut illustrations.\n"
         "- Pictures were printed on textiles, playing cards and paper money. In the late 18th century, in **Edo** (later Tokyo), illustrated collections of paintings showed an elegant urban culture; the artist **Kitagawa Utamaro**, born in Edo in 1753, was famous for his *ukiyo* ('pictures of the floating world')."),
  C.kc("s2.check", "What was the oldest Japanese printed book?",
    [("The Diamond Sutra, AD 868", ""), ("The Gutenberg Bible", "That was printed in Germany in the 15th century."),
     ("The Ninety Five Theses", "Luther wrote them in 1517."), ("Amar Jiban", "That was Rashsundari Debi's autobiography (1876).")],
    "The Buddhist Diamond Sutra, printed in AD 868, with six sheets of text and woodcut illustrations."),
 ]},
 {"id": "s3", "title": "Print comes to Europe", "blocks": [
  blk("s3.thm", "theory", title="From manuscripts to Gutenberg", revision=True,
    body="- In the **11th century**, Chinese **paper** reached Europe via the silk routes, making it possible to produce manuscripts carefully written by scribes.\n"
         "- In **1295**, **Marco Polo**, the great explorer, returned to Italy after many years in China and brought back the knowledge of **woodblock printing**. Italians began producing books with woodblocks, and the technology spread across Europe.\n"
         "- Luxury editions were still handwritten on very expensive **vellum** for aristocrats and rich monasteries; merchants and students in university towns bought cheaper printed copies.\n"
         "- Demand for books rose; booksellers exported books and organised book fairs. More than **50 scribes** often worked for one bookseller, but handwritten manuscripts could not meet the demand: copying was **expensive, laborious and time-consuming**, and manuscripts were **fragile and awkward to handle**.\n\n"
         "**Gutenberg and the printing press:** **Johann Gutenberg**, the son of a merchant, grew up on a large agricultural estate where he saw **wine and olive presses**. He learnt to polish stones, became a **master goldsmith**, and learnt to make **lead moulds** for trinkets. "
         "Using this knowledge, he adapted existing technology: the **olive press** became the model for the printing press, and moulds were used to cast **metal types** for the letters of the alphabet. By **1448** he had perfected the system. "
         "The first book he printed was the **Bible**: about **180 copies**, which took **three years** to produce, very fast for the time.\n\n"
         "At first, printed books closely resembled handwritten manuscripts: the metal letters imitated ornamental handwriting, and borders were illuminated by hand. Between **1450 and 1550** printing presses were set up in most countries of Europe. "
         "In the second half of the 15th century, **20 million** copies of printed books flowed into European markets; in the 16th century the number rose to about **200 million**. This shift from hand printing to mechanical printing led to the **print revolution**."),
  blk("s3.table", "markdown_table", title="Manuscripts vs printed books", revision=True, body=HAND_PRINT),
  C.kc("s3.check", "Which machine gave Gutenberg the model for his printing press?",
    [("The olive press", ""), ("The steam engine", "The steam engine came much later."), ("The spinning wheel", "That was used for spinning yarn."), ("The woodblock", "Woodblocks were an older printing method, not the press model.")],
    "The olive press served as the model; moulds cast the metal types."),
  C.kc("s3.check2", "Who brought the knowledge of woodblock printing from China to Italy?",
    [("Marco Polo, in 1295", ""), ("Johann Gutenberg", "Gutenberg developed the printing press in Germany."), ("Martin Luther", "Luther was a religious reformer."), ("Kitagawa Utamaro", "Utamaro was a Japanese artist.")],
    "Marco Polo returned to Italy in 1295 with knowledge of woodblock printing."),
 ]},
 {"id": "s4", "title": "The print revolution and its impact", "blocks": [
  blk("s4.thm", "theory", title="A new reading public, and the fear of print", revision=True,
    body="**A new reading public:** printing reduced the cost of books, and the time and labour needed to produce each book; multiple copies could be made with ease. Earlier, reading was restricted to the elites; common people lived in an **oral culture**, hearing sacred texts read out, ballads recited and folk tales narrated. "
         "Now a new reading public emerged. But literacy rates were low, so printers published popular ballads and folk tales with many illustrations, which were sung and recited at gatherings. **Oral culture entered print, and printed material was transmitted orally**: the hearing public and the reading public intermingled.\n\n"
         "**Religious debates and the fear of print:** print created the possibility of wide circulation of ideas and introduced a new world of debate. Many feared that if there was no control over what was printed and read, rebellious and irreligious thoughts might spread. The Latin scholar and Catholic reformer **Erasmus** complained that 'swarms of new books' were flying everywhere, most of them scandalous, irreligious and seditious.\n"
         "- In **1517**, the religious reformer **Martin Luther** wrote the ***Ninety Five Theses***, criticising many practices and rituals of the Roman Catholic Church. A printed copy was posted on a church door in **Wittenberg**. His writings were reproduced in vast numbers and read widely, leading to a division within the Church and the beginning of the **Protestant Reformation**. "
         "Luther's translation of the New Testament sold **5,000 copies within a few weeks**. He said: ***'Printing is the ultimate gift of God and the greatest one.'***\n"
         "- **Print and dissent:** in the 16th century **Menocchio**, a miller in Italy, read books available in his locality and reinterpreted the Bible, forming a view of God and Creation that enraged the Roman Catholic Church. He was hauled up twice during the Church's **inquisition** and ultimately executed. "
         "The Church imposed severe controls on publishers and booksellers and began to maintain an **Index of Prohibited Books from 1558**."),
  blk("s4.mania", "theory", title="The reading mania and the French Revolution", revision=True,
    body="**Reading mania:** in the 17th and 18th centuries literacy rose across Europe as churches set up schools in villages; by the end of the 18th century literacy in some parts of Europe was **60 to 80 per cent**.\n"
         "- Booksellers employed **pedlars** who roamed villages selling little books: almanacs, ballads, folk tales. In England, **penny chapbooks** were sold by pedlars called **chapmen** for a penny. In France, the ***Bibliotheque Bleue*** were cheap small books on poor paper, bound in **blue covers**.\n"
         "- From the early 18th century the **periodical press** combined news of wars and trade with entertainment. The ideas of scientists and philosophers became accessible: **Isaac Newton's** discoveries were published, and the writings of **Thomas Paine, Voltaire and Jean Jacques Rousseau** were widely printed and read.\n\n"
         "**'Tremble, therefore, tyrants of the world!'** By the mid-18th century people believed books could spread progress and enlightenment, and free society from despotism. **Louise-Sebastien Mercier**, an 18th-century French novelist, declared: *'The printing press is the most powerful engine of progress and public opinion is the force that will sweep despotism away.'* "
         "He wrote: ***'Tremble, therefore, tyrants of the world! Tremble before the virtual writer!'*** (the tyrants being absolutist institutions like the monarchy and the Church).\n\n"
         "**Print culture and the French Revolution:** historians give three arguments:\n1. Print **popularised the ideas of Enlightenment thinkers** (Voltaire, Rousseau), who criticised tradition, superstition and despotism and argued for the rule of reason; they attacked the sacred authority of the Church and the despotic power of the state.\n"
         "2. Print created a **new culture of dialogue and debate**: all values, norms and institutions were re-evaluated by a public that had become aware of the power of reason.\n"
         "3. By the **1780s**, an outpouring of literature, **cartoons and caricatures** mocked the royalty and their morality, suggesting the monarchy was absorbed in pleasure while common people suffered; this spread hostility against the monarchy.\n\n"
         "But print does not directly shape minds: people also read royal and Church propaganda, and accepted some ideas while rejecting others. Print did, however, **open up the possibility of thinking differently**."),
  C.kc("s4.check", "Who were the 'tyrants' in Mercier's line 'Tremble, therefore, tyrants of the world'?",
    [("Absolutist institutions like the monarchy and the Church", ""), ("Printers and booksellers", "Mercier praised the power of print."), ("Pedlars and chapmen", "They sold cheap books."), ("Readers of novels", "Mercier's heroes were transformed by reading.")],
    "He meant the despotic monarchy and Church, whose authority print would sweep away."),
  C.kc("s4.check2", "What were 'chapbooks' in England?",
    [("Cheap pocket-size books sold by pedlars called chapmen for a penny", ""), ("Expensive vellum manuscripts", "Those were for aristocrats."), ("Books banned by the Church", "Banned books were listed in the Index."), ("Blue-covered books in France", "Those were the Bibliotheque Bleue.")],
    "Penny chapbooks were sold by chapmen."),
 ]},
 {"id": "s5", "title": "The nineteenth century", "blocks": [
  blk("s5.thm", "theory", title="Children, women, workers and new technology", revision=True,
    body="The 19th century saw **mass literacy** in Europe, bringing many new readers among **children, women and workers**.\n\n"
         "- **Children:** primary education became compulsory from the late 19th century, and school textbooks became important for publishers. A **children's press** was set up in **France in 1857**. The **Grimm Brothers** in Germany compiled traditional folk tales from peasants and published them in **1812**, leaving out anything thought unsuitable for children or vulgar to the elites.\n"
         "- **Women:** penny magazines and manuals on behaviour and housekeeping were meant for women. Some of the best-known novelists were women, **Jane Austen, the Bronte sisters and George Eliot**, whose writings defined a new type of woman with will, strength of personality and the power to think.\n"
         "- **Workers:** **lending libraries**, existing from the 17th century, became instruments for educating white-collar workers, artisans and the lower middle class. As the working day shortened from the mid-19th century, workers wrote political tracts and autobiographies.\n\n"
         "**Further innovations:** by the late 18th century presses were made of metal. By the mid-19th century **Richard M. Hoe** of New York had perfected the **power-driven cylindrical press**, printing **8,000 sheets per hour**, ideal for newspapers. In the late 19th century the **offset press** could print up to **six colours** at a time; from the turn of the 20th century **electrically operated presses** speeded up printing.\n\n"
         "**Selling books:** periodicals **serialised novels**; in the 1920s England sold popular works in the cheap **Shilling Series**; the **dust cover (book jacket)** was a 20th-century innovation; and with the **Great Depression of the 1930s**, publishers brought out cheap **paperback** editions."),
  C.kc("s5.check", "Who perfected the power-driven cylindrical press?",
    [("Richard M. Hoe of New York", ""), ("Johann Gutenberg", "Gutenberg's press of 1448 was hand-operated."), ("James Augustus Hickey", "Hickey edited the Bengal Gazette."), ("Marco Polo", "Marco Polo brought woodblock printing to Italy.")],
    "By the mid-19th century, Hoe's press printed 8,000 sheets an hour."),
 ]},
 {"id": "s6", "title": "India and the world of print", "blocks": [
  blk("s6.thm", "theory", title="Manuscripts, the first presses and newspapers", revision=True,
    body="**Before print:** India had a very rich and old tradition of **handwritten manuscripts** in Sanskrit, Arabic, Persian and various vernacular languages, copied on **palm leaves** or handmade paper, sometimes beautifully illustrated. But manuscripts were expensive and fragile, written in different scripts, and not widely used in everyday life. "
         "In pre-colonial Bengal, village primary schools taught students to write from the teacher's dictation; many became literate without ever reading a text.\n\n"
         "**Print comes to India:**\n- The printing press first came to **Goa** with **Portuguese missionaries** in the **mid-16th century**. Jesuit priests learnt **Konkani** and printed tracts; by **1674** about **50 books** had been printed in Konkani and Kanara.\n"
         "- **Catholic priests** printed the **first Tamil book in 1579 at Cochin**, and the **first Malayalam book in 1713**. By **1710**, **Dutch Protestant missionaries** had printed **32 Tamil texts**.\n"
         "- The English East India Company imported presses from the late 17th century, but the English press grew slowly. From **1780**, **James Augustus Hickey** edited the ***Bengal Gazette***, a weekly calling itself *'a commercial paper open to all, but influenced by none'*. He published advertisements (including for the import and sale of slaves) and gossip about senior Company officials. "
         "Enraged, Governor-General **Warren Hastings** persecuted Hickey and encouraged officially sanctioned newspapers.\n"
         "- The first Indian newspaper was the weekly ***Bengal Gazette*** brought out by **Gangadhar Bhattacharya**, who was close to Rammohun Roy."),
  blk("s6.reform", "theory", title="Religious reform and public debates", revision=True,
    body="From the early 19th century there were intense debates around religious issues, carried out in public and **in print**. Printed tracts and newspapers spread new ideas and let a wider public take part in the debates.\n\n"
         "- In Bengal, reformers and Hindu orthodoxy debated **widow immolation, monotheism, Brahmanical priesthood and idolatry**, printing their ideas in the everyday spoken language of ordinary people. **Rammohun Roy** published ***Sambad Kaumudi*** from **1821**; the Hindu orthodoxy commissioned ***Samachar Chandrika*** to oppose him.\n"
         "- From **1822**, two Persian newspapers, ***Jam-i-Jahan Nama*** and ***Shamsul Akhbar***, were published; the same year, the Gujarati newspaper ***Bombay Samachar*** appeared.\n"
         "- In north India, the **ulama**, anxious about the collapse of Muslim dynasties and fearing conversion and changes to Muslim personal laws, used cheap **lithographic presses** to publish Persian and Urdu translations of holy scriptures and religious newspapers. The **Deoband Seminary**, founded in **1867**, published thousands of **fatwas** guiding Muslim readers in everyday life.\n"
         "- Among Hindus, print encouraged reading religious texts in vernacular languages. The first printed edition of **Tulsidas's *Ramcharitmanas*** came out from **Calcutta in 1810**. From the 1880s, the **Naval Kishore Press** at Lucknow and the **Shri Venkateshwar Press** in Bombay published numerous religious texts in vernaculars.\n\n"
         "Print **connected communities** across India: newspapers carried news from one place to another, creating **pan-Indian identities**."),
  blk("s6.forms", "theory", title="New forms of publication, women and the poor", revision=True,
    body="**New forms:** the **novel**, lyrics, short stories and essays on social and political matters; **visual images**: **Raja Ravi Varma** produced images for mass circulation, cheap prints and calendars decorated even poor homes, and by the **1870s** **caricatures and cartoons** in journals commented on social and political issues.\n\n"
         "**Women and print:** women's reading increased in middle-class homes; liberal fathers and husbands educated women at home and sent them to schools. Conservative Hindus feared a literate girl would be widowed, and Muslims feared educated women would be corrupted by Urdu romances.\n"
         "- **Rashsundari Debi**, a young married girl in an orthodox household, learnt to read secretly in her kitchen and later wrote ***Amar Jiban***, published in **1876**, the first full-length autobiography in Bengali.\n"
         "- From the 1860s **Kailashbashini Debi** wrote about how women were imprisoned at home and treated unjustly. In the 1880s, in Maharashtra, **Tarabai Shinde and Pandita Ramabai** wrote with passionate anger about the miserable lives of upper-caste Hindu women, especially widows.\n"
         "- In Punjab, **Ram Chaddha** published ***Istri Dharm Vichar*** to teach women to be obedient wives. In Calcutta, an area called **Battala** printed cheap popular books, and pedlars took them into homes, letting women read in their leisure time.\n\n"
         "**Print and the poor:** cheap small books were sold at crossroads in 19th-century Madras towns, and **public libraries** came up from the early 20th century. Caste discrimination became a subject of print: **Jyotiba Phule** wrote about the injustices of the caste system in ***Gulamgiri*** (1871); in the 20th century **B. R. Ambedkar** in Maharashtra and **E. V. Ramaswamy Naicker (Periyar)** in Madras wrote powerfully on caste. "
         "**Kashibaba**, a Kanpur millworker, wrote ***Chhote Aur Bade Ka Sawal*** (1938) showing the links between caste and class exploitation, and another Kanpur millworker writing as **Sudarshan Chakr** produced poems collected as ***Sacchi Kavitayan***. By the 1930s, **Bangalore** cotton millworkers set up libraries, following the example of Bombay workers."),
  blk("s6.censor", "theory", title="Print and censorship", revision=True,
    body="- Before **1798**, the Company was not much concerned with censorship; its early controls were aimed at **Englishmen** in India who criticised Company misrule, because such criticism might be used in England to attack its trade monopoly.\n"
         "- By the **1820s** the Calcutta Supreme Court passed regulations to control press freedom, and the Company encouraged newspapers celebrating British rule.\n"
         "- In **1835**, after petitions by editors, Governor-General **Bentinck** agreed to revise the press laws, and **Thomas Macaulay** formulated rules that restored earlier freedoms.\n"
         "- After the **revolt of 1857**, the attitude changed. Enraged Englishmen demanded a clamp-down on the 'native' press. As vernacular newspapers became assertively nationalist, the government passed the **Vernacular Press Act in 1878**, **modelled on the Irish Press Laws**. It gave the government extensive rights to **censor** reports and editorials in the vernacular press. If a report was judged **seditious**, the newspaper was warned; if the warning was ignored, the press could be **seized** and the printing machinery **confiscated**.\n"
         "- Despite this, nationalist newspapers grew in all parts of India. When Punjab revolutionaries were deported in **1907**, **Balgangadhar Tilak** wrote about them with great sympathy in his paper ***Kesari***. This led to his **imprisonment in 1908**, provoking widespread protests across India."),
  blk("s6.laws", "markdown_table", title="How press policy changed in colonial India", revision=True, body=LAWS),
  blk("s6.timeline", "markdown_table", title="Timeline of the chapter", revision=True, body=TIMELINE),
  C.kc("s6.check", "Where did the printing press first come to India?",
    [("Goa, with Portuguese missionaries", ""), ("Calcutta, with the East India Company", "The Company's presses came later."), ("Bombay, with Parsi merchants", "The first press came to Goa."), ("Cochin, with Dutch traders", "Catholic priests printed the first Tamil book at Cochin in 1579, but the first press came to Goa.")],
    "Portuguese missionaries brought the first press to Goa in the mid-16th century."),
  C.kc("s6.check2", "What did the Vernacular Press Act of 1878 do?",
    [("Gave the government extensive rights to censor vernacular newspapers and seize presses", ""), ("Restored press freedom", "That was done by Macaulay in 1835."),
     ("Banned all English newspapers", "It targeted the vernacular press."), ("Set up the first Indian newspaper", "The first Indian newspaper came much earlier.")],
    "Modelled on the Irish Press Laws, it allowed censorship and seizure of presses."),
 ]},
 {"id": "s7", "title": "Remember, avoid, practise", "blocks": [
  blk("s7.memory", "memory_trick", title="Memory tricks",
    body="- **East Asia: China 594, Japan 768–770, Diamond Sutra 868.**\n- **Europe: \"Paper → Polo → Gutenberg → Luther\":** paper in the 11th century, Marco Polo 1295, Gutenberg's Bible 1448, Luther's Theses 1517.\n"
         "- **Gutenberg's three skills = 3 tools:** olive press (press), goldsmith (precision), lead moulds (metal type).\n- **India firsts: Goa press → Tamil 1579 → Malayalam 1713 → Hickey 1780 → Sambad Kaumudi 1821 → Bombay Samachar 1822.**\n"
         "- **Censorship: 1835 free (Macaulay), 1878 gagged (Vernacular Press Act), 1908 Tilak jailed.**"),
  blk("s7.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying print began in Europe: it began in **China, Japan and Korea**.\n2. Saying Gutenberg's first book was a novel: it was the **Bible** (about 180 copies in three years).\n"
         "3. Mixing up the Bengal Gazette of **Hickey** (English, 1780) and that of **Gangadhar Bhattacharya** (the first Indian newspaper).\n4. Saying the Vernacular Press Act was modelled on British laws: it was modelled on the **Irish** Press Laws.\n"
         "5. Saying Macaulay restricted the press: he **restored** freedoms in 1835.\n6. Confusing *Sambad Kaumudi* (Rammohun Roy) with *Samachar Chandrika* (his orthodox opponents)."),
  blk("s7.tip", "teacher_tip", title="Try this in class",
    body="Make a 'woodblock print' using a potato or eraser stamp, then ask students to copy one page by hand. Compare the time taken. "
         "Then stage a mock 1820s debate: one group writes a pamphlet for *Sambad Kaumudi*, the other for *Samachar Chandrika*, and the class sees how print turned an argument into a public debate."),
  blk("s7.reflection", "reflection", title="Think and explain",
    body="Mercier believed the printing press would sweep despotism away. Do you think social media today plays a similar role? Give one way it does and one way it does not."),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 1:** print spread the ideas of nationalism and liberalism in Europe.\n- **Chapter 2:** nationalist newspapers, songs and images built a sense of collective belonging in India.\n"
         "- **Political Science, Outcomes of Democracy:** a free press is essential for an accountable government."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="'Print opened up the possibility of thinking differently.' Explain with reference to Europe and India in about 120 words.\n\n"
         "**Model answer:** In Europe, Luther's Ninety Five Theses (1517), printed and read widely, split the Church and began the Reformation; Menocchio reinterpreted the Bible from books he read; Voltaire and Rousseau's writings spread the rule of reason, and cartoons mocked the monarchy before the French Revolution. "
         "In India, Rammohun Roy's Sambad Kaumudi and the orthodox Samachar Chandrika turned social reform into a public debate; women like Rashsundari Debi and Pandita Ramabai wrote about women's suffering; Phule and Ambedkar attacked caste; nationalist papers like Tilak's Kesari criticised colonial rule. "
         "Print did not decide what people thought, but it let them question and debate."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- Print began in China (woodblocks from AD 594), spread to Japan (AD 768–770; Diamond Sutra, 868) and reached Europe through paper and Marco Polo (1295).\n"
         "- Gutenberg perfected the printing press by 1448 (the Bible); presses spread across Europe, causing a print revolution.\n"
         "- Print created a new reading public, religious debate and dissent (Luther, Menocchio), the reading mania, and the ideas behind the French Revolution.\n"
         "- In the 19th century, children, women and workers became readers; new presses (Hoe's cylinder press, offset press) and new selling strategies appeared.\n"
         "- In India, print came to Goa in the mid-16th century; newspapers and tracts spread religious reform debates, connected communities, gave women and lower castes a voice, and drew colonial censorship (Vernacular Press Act, 1878)."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- The 2025-26 sample paper asked about Mercier's 'tyrants' (MCQ) and a case study on why newspapers were published and became popular in the 19th century.\n"
         "- 3/5-mark questions: Gutenberg's press, Luther and the Reformation, print and the French Revolution, the Vernacular Press Act, women and print, print and religious reform in India.\n"
         "- Quote short lines accurately: Luther's 'ultimate gift of God', Hickey's 'open to all, but influenced by none'."),
  blk("s7.flash1", "flashcard", front="When and what did Gutenberg first print?", back="The Bible: about 180 copies, perfected by 1448, taking three years."),
  blk("s7.flash2", "flashcard", front="What did the Vernacular Press Act (1878) allow?", back="Censorship of vernacular papers; seizure of presses if a warning about seditious reports was ignored."),
  blk("s7.flash3", "flashcard", front="Who wrote 'Amar Jiban' and why is it important?", back="Rashsundari Debi (1876): the first full-length autobiography in Bengali."),
  blk("s7.flash4", "flashcard", front="What was the Index of Prohibited Books?", back="A list of banned books kept by the Roman Catholic Church from 1558."),
 ]},
]

# ---------------- Sample paper ----------------
M("sqp4", IMPACT, "Louise-Sebastien Mercier proclaimed \"Tremble, therefore, tyrants of the world! Tremble before the virtual writer!\" Who are referred to as the tyrants in this context?",
  [("Educated classes who wanted to change the society", "The educated classes were the readers Mercier hoped would change society."), ("Absolutist institutions like monarchy and church", ""),
   ("Authors of the new books", "Mercier praised writers; they were not the tyrants."), ("Printing press", "Mercier called the press the engine of progress.")],
  "Mercier believed print and public opinion would sweep away despotism: the tyrants were the absolutist monarchy and Church.", "medium", SQP(4), correct=1)
W("sqp8", "case_based", INDIA, "Read the given text and answer the questions.\n\n*Why Newspapers?* \"Krishnaji Trimbuck Ranade inhabitant of Poona intends to publish a Newspaper in the Marathi Language with a view of affording useful information on every topic of local interest. It will be open for free discussion on subjects of general utility, scientific investigation and the speculations connected with the antiquities, statistics, curiosities, history and geography of the country and of the Deccan especially...\" (Bombay Telegraph and Courier, 6 January 1849)\n\n"
  "\"The task of the native newspapers and political associations is identical to the role of the Opposition in the House of Commons in Parliament in England. That is to critically examine government policy to suggest improvements, by removing those parts that will not be to the benefit of the people, and also by ensuring speedy implementation.\" (Native Opinion, 3 April 1870)\n\n"
  "(i) Explain the main reason for publishing newspapers by Krishnaji. (1)\n\n(ii) How was the task of native newspapers and political associations seen as identical to the role of the opposition? (1)\n\n(iii) Analyse the reasons for the popularity of newspapers during the 19th century. (2)",
  ["(i) To provide useful information on every topic of local interest in Marathi and to be open for free discussion on subjects of general utility, science, history and geography.",
   "(ii) Like the Opposition in Parliament, they would critically examine government policy, suggest improvements, remove what was not for the people's benefit and press for speedy implementation.",
   "(iii) Newspapers were cheap and in the vernacular languages people understood; they carried news across regions and connected communities, spread ideas of social reform and nationalism, and let people debate public issues and criticise colonial rule."],
  CB, source=SQP(8))

# ---------------- NCERT exercises ----------------
W("ex1a", "very_short_answer", EAST, "Give reasons for the following: woodblock print only came to Europe after 1295.",
  ["Woodblock printing was developed in China, and Europe had no regular contact with this technology.", "In 1295 Marco Polo returned to Italy after many years in China and brought back the knowledge of woodblock printing."], source=ex("1(a)"))
W("ex1b", "very_short_answer", IMPACT, "Give reasons for the following: Martin Luther was in favour of print and spoke out in praise of it.",
  ["Print helped Luther's Ninety Five Theses (1517) and his translation of the New Testament to be reproduced in vast numbers and read widely, spreading his criticism of the Church.", "This began the Protestant Reformation; so he said, 'Printing is the ultimate gift of God and the greatest one.'"], source=ex("1(b)"))
W("ex1c", "very_short_answer", IMPACT, "Give reasons for the following: the Roman Catholic Church began keeping an Index of Prohibited Books from the mid-sixteenth century.",
  ["Popular reading led people like the miller Menocchio to reinterpret the Bible and question the Church's teachings.", "Troubled by such heretical ideas, the Church imposed controls on publishers and booksellers and kept an Index of Prohibited Books from 1558."], source=ex("1(c)"))
W("ex1d", "very_short_answer", INDIA, "Give reasons for the following: Gandhi said the fight for Swaraj is a fight for liberty of speech, liberty of the press, and freedom of association.",
  ["The colonial government repressed these freedoms through laws like the Vernacular Press Act and by jailing writers like Tilak.", "Without freedom of speech, press and association, Indians could not express opinions, organise or oppose colonial rule, so these freedoms were the basis of Swaraj."], source=ex("1(d)"))
W("ex2a", "short_answer", EAST, "Write a short note on the Gutenberg Press.",
  ["Johann Gutenberg, son of a merchant, saw wine and olive presses on his family estate, became a master goldsmith and learnt to make lead moulds.",
   "He used the olive press as a model for the printing press and moulds to cast metal types for letters; by 1448 he had perfected the system.",
   "The first book he printed was the Bible: about 180 copies in three years. Presses spread across Europe between 1450 and 1550, leading to the print revolution."], source=ex("2(a)"))
W("ex2b", "short_answer", IMPACT, "Write a short note on Erasmus's idea of the printed book.",
  ["Erasmus, a Latin scholar and Catholic reformer, was deeply anxious about printing.",
   "He felt that though some books might give something worthwhile, most of them were scandalous, seditious, irreligious and foolish, and they spread everywhere like swarms of flies.",
   "He feared that printers filled the world with books harmful to learning, showing the fear that easy print would spread dangerous ideas."], source=ex("2(b)"))
W("ex2c", "short_answer", INDIA, "Write a short note on the Vernacular Press Act.",
  ["After 1857 vernacular newspapers became assertively nationalist, and Englishmen demanded control of the 'native' press.",
   "The Vernacular Press Act of 1878, modelled on the Irish Press Laws, gave the government extensive rights to censor reports and editorials in the vernacular press.",
   "Newspapers publishing seditious reports were warned, and if they ignored the warning, their press could be seized and machinery confiscated; yet nationalist papers kept growing."], source=ex("2(c)"))
W("ex3a", "short_answer", INDIA, "What did the spread of print culture in nineteenth-century India mean to women?",
  ["Women's reading increased in middle-class homes; liberal men educated women at home and sent them to schools, and journals carried writings by women.",
   "Women wrote about their own lives: Rashsundari Debi learnt to read secretly and wrote Amar Jiban (1876); Kailashbashini Debi, Tarabai Shinde and Pandita Ramabai wrote about women's oppression and the plight of widows.",
   "Cheap Battala books reached women through pedlars, letting them read in leisure, though conservatives feared educated women and some books taught obedience."], source=ex("3(a)"))
W("ex3b", "short_answer", INDIA, "What did the spread of print culture in nineteenth-century India mean to the poor?",
  ["Very cheap small books sold at crossroads in Madras towns, and public libraries from the early 20th century, gave the poor access to reading.",
   "Writers like Jyotiba Phule (Gulamgiri), Ambedkar and Periyar wrote against caste discrimination, and their writings were read all over India.",
   "Workers wrote too: Kashibaba's Chhote Aur Bade Ka Sawal (1938) linked caste and class exploitation, and millworkers in Bombay and Bangalore set up libraries."], source=ex("3(b)"))
W("ex3c", "short_answer", INDIA, "What did the spread of print culture in nineteenth-century India mean to reformers?",
  ["Reformers used tracts and newspapers to spread their ideas in the everyday language of ordinary people and reach a wide public.",
   "Rammohun Roy's Sambad Kaumudi (1821) argued against widow immolation and idolatry, while the orthodox replied through Samachar Chandrika, making reform a public debate.",
   "Phule, Ambedkar and Periyar used print against caste, and Muslim ulama and Hindu groups used it to spread religious knowledge and connect communities."], source=ex("3(c)"))
W("ex4", "long_answer", IMPACT, "Why did some people in eighteenth-century Europe think that print culture would bring enlightenment and end despotism?",
  ["Print made books cheap and available, and literacy rose to 60–80 per cent in parts of Europe, creating a reading mania.",
   "The ideas of scientists and philosophers like Newton, Thomas Paine, Voltaire and Rousseau became accessible to ordinary readers.",
   "These writings criticised tradition, superstition and despotism and argued for the rule of reason, questioning the authority of the Church and the monarchy.",
   "Print created a culture of debate in which all values and institutions were re-examined by a public aware of the power of reason.",
   "So writers like Mercier believed the printing press was the most powerful engine of progress, and wrote, 'Tremble, therefore, tyrants of the world!'"], source=ex("discuss 1"))
W("ex5", "long_answer", IMPACT, "Why did some people fear the effect of easily available printed books? Choose one example from Europe and one from India.",
  ["Many feared that without control over what was printed and read, rebellious and irreligious thoughts would spread and the authority of 'valuable' literature would be destroyed.",
   "Europe: the Roman Catholic Church feared that popular readings would lead to questioning of faith; after Luther's Theses and the case of Menocchio, it kept an Index of Prohibited Books from 1558.",
   "Erasmus, too, felt most new books were scandalous, seditious and irreligious.",
   "India: the colonial government feared nationalist criticism and passed the Vernacular Press Act (1878) to censor the vernacular press, and jailed Tilak in 1908.",
   "Conservative Indians also feared that reading would corrupt women: Hindus believed a literate girl would be widowed, and Muslims feared Urdu romances."], source=ex("discuss 2"))
W("ex6", "long_answer", INDIA, "What were the effects of the spread of print culture for poor people in nineteenth-century India?",
  ["Cheap small books were sold at crossroads in Madras towns, so the poor too could buy books.",
   "Public libraries set up from the early 20th century expanded access to books, often by rich patrons seeking prestige.",
   "Issues of caste discrimination were written about: Phule's Gulamgiri (1871), and later Ambedkar and Periyar, whose writings were read across India.",
   "Workers wrote about their experiences: Kashibaba's Chhote Aur Bade Ka Sawal (1938) and Sudarshan Chakr's poems (Sacchi Kavitayan).",
   "Millworkers in Bombay and Bangalore set up libraries to educate themselves, supported by social reformers."], source=ex("discuss 3"))
W("ex7", "long_answer", INDIA, "Explain how print culture assisted the growth of nationalism in India.",
  ["Newspapers carried news from one place to another, connecting communities and creating pan-Indian identities.",
   "Vernacular and nationalist newspapers reported on colonial misrule and encouraged nationalist activities.",
   "Print spread debates on social and religious reform, making people question both tradition and colonial authority.",
   "Images, cartoons and calendars, and nationalist literature, spread national ideas even among people who could not read well.",
   "Repression like the Vernacular Press Act and Tilak's imprisonment for his writings in Kesari (1908) provoked widespread protests, strengthening nationalism further."], source=ex("discuss 4"))

# ---------------- MCQs ----------------
M("mcq01", EAST, "The earliest print technology was developed in:", [("China, Japan and Korea", ""), ("Germany and Italy", "Print reached Europe much later."), ("India and Persia", "Print came to India in the 16th century."), ("England and France", "Print reached Europe later.")], "Hand printing began in East Asia.")
M("mcq02", EAST, "From which year were books printed in China by rubbing paper on inked woodblocks?", [("AD 594", ""), ("AD 868", "AD 868 is the Diamond Sutra in Japan."), ("1295", "1295 is Marco Polo's return."), ("1448", "1448 is Gutenberg's press.")], "AD 594.", "medium")
M("mcq03", EAST, "The traditional Chinese 'accordion book' was:", [("folded and stitched at the side", ""), ("printed on both sides of thick paper", "Thin porous paper could be printed on one side only."), ("bound in blue covers", "That was the Bibliotheque Bleue in France."), ("written on vellum", "Vellum was used for European luxury manuscripts.")], "Only one side could be printed, so sheets were folded.", "medium")
M("mcq04", EAST, "Who introduced hand-printing technology into Japan?", [("Buddhist missionaries from China", ""), ("Portuguese missionaries", "They brought the press to Goa."), ("Marco Polo", "He took woodblock printing to Italy."), ("Dutch traders", "They printed Tamil texts in India.")], "Around AD 768–770.")
M("mcq05", EAST, "Which city became the hub of the new print culture in late-19th-century China?", [("Shanghai", ""), ("Beijing", "The chapter names Shanghai."), ("Edo", "Edo is in Japan."), ("Canton", "The chapter names Shanghai.")], "Shanghai.", "medium")
M("mcq06", EAST, "Kitagawa Utamaro is known for:", [("ukiyo pictures of urban culture in Edo", ""), ("the first printing press", "That was Gutenberg."), ("the Diamond Sutra", "That was printed in AD 868."), ("the Ninety Five Theses", "That was Luther.")], "Ukiyo: 'pictures of the floating world'.", "medium")
M("mcq07", EUR, "Chinese paper reached Europe in the 11th century through:", [("the silk routes", ""), ("the Atlantic Ocean", "Paper came overland via the silk routes."), ("Gutenberg's press", "The press came much later."), ("Marco Polo", "Marco Polo brought woodblock printing, in 1295.")], "Via the silk routes.")
M("mcq08", EUR, "Expensive handwritten luxury editions in Europe were written on:", [("vellum", ""), ("palm leaves", "Palm leaves were used in India."), ("newsprint", "Newsprint is cheap paper."), ("silk", "The chapter mentions vellum.")], "Vellum, for aristocrats and monastic libraries.", "medium")
M("mcq09", EUR, "Which of these was NOT a problem with handwritten manuscripts?", [("They were cheap and quick to produce", ""), ("Copying was laborious and time-consuming", "This was a real problem."), ("They were fragile and awkward to handle", "This was a real problem."), ("They were expensive", "This was a real problem.")], "Manuscripts were slow and costly, not cheap and quick.")
M("mcq10", EUR, "Gutenberg had learnt which craft that helped him make metal types?", [("Goldsmithing and making lead moulds", ""), ("Weaving", "Weaving was not his craft."), ("Carpentry", "He was a goldsmith."), ("Pottery", "He was a goldsmith.")], "He was a master goldsmith skilled with lead moulds.")
M("mcq11", EUR, "By which year had Gutenberg perfected his printing system?", [("1448", ""), ("1295", "1295 is Marco Polo."), ("1517", "1517 is Luther."), ("1558", "1558 is the Index of Prohibited Books.")], "1448.")
M("mcq12", EUR, "How many copies of the Bible did Gutenberg print, and in how long?", [("About 180 copies in three years", ""), ("About 5,000 copies in a few weeks", "That was Luther's New Testament."), ("About 20 million copies", "That was all printed books in Europe in the late 15th century."), ("About 50 copies in one year", "The figure was about 180 in three years.")], "About 180 copies in three years.", "medium")
M("mcq13", EUR, "About how many printed books flowed into European markets in the 16th century?", [("About 200 million copies", ""), ("About 20 million copies", "That was the second half of the 15th century."), ("About 180 copies", "That was Gutenberg's Bible."), ("About 50 books", "That was Konkani and Kanara books by 1674.")], "About 200 million.", "medium")
M("mcq14", IMPACT, "Martin Luther's Ninety Five Theses (1517) criticised:", [("practices and rituals of the Roman Catholic Church", ""), ("the printing press", "Luther praised print."), ("the French monarchy", "That was later 18th-century literature."), ("the East India Company", "That is Indian history.")], "They led to the Protestant Reformation.")
M("mcq15", IMPACT, "Who said 'Printing is the ultimate gift of God and the greatest one'?", [("Martin Luther", ""), ("Erasmus", "Erasmus was anxious about print."), ("Mercier", "Mercier spoke of 'tyrants of the world'."), ("Gutenberg", "The words are Luther's.")], "Martin Luther.")
M("mcq16", IMPACT, "Menocchio was:", [("an Italian miller executed by the Church for reinterpreting the Bible", ""), ("the inventor of the printing press", "That was Gutenberg."), ("a French novelist", "That was Mercier."), ("a Japanese artist", "That was Utamaro.")], "He was hauled up during the inquisition and executed.", "medium")
M("mcq17", IMPACT, "From which year did the Roman Catholic Church maintain an Index of Prohibited Books?", [("1558", ""), ("1517", "1517 is Luther's Theses."), ("1448", "1448 is Gutenberg."), ("1878", "1878 is the Vernacular Press Act in India.")], "1558.")
M("mcq18", IMPACT, "By the end of the 18th century, literacy rates in some parts of Europe were as high as:", [("60 to 80 per cent", ""), ("10 to 20 per cent", "They were much higher."), ("100 per cent", "Not yet."), ("35 to 75 per cent", "That is a figure from the industrialisation chapter (unemployment).")], "60 to 80 per cent.", "medium")
M("mcq19", IMPACT, "In France, the 'Bibliotheque Bleue' were:", [("low-priced small books bound in cheap blue covers", ""), ("expensive manuscripts", "They were cheap."), ("banned books", "They were popular books."), ("newspapers", "They were small books.")], "Cheap books on poor paper with blue covers.")
M("mcq20", IMPACT, "Whose writings were widely printed and read in 18th-century Europe?", [("Thomas Paine, Voltaire and Rousseau", ""), ("Tulsidas and Kabir", "They wrote in India."), ("Jane Austen and George Eliot", "They were 19th-century novelists."), ("Phule and Ambedkar", "They wrote in India.")], "Enlightenment thinkers.")
M("mcq21", IMPACT, "Which of these is one of the arguments that print helped bring about the French Revolution?", [("Print popularised the ideas of Enlightenment thinkers", ""), ("Print was banned in France", "Print spread widely in France."), ("Only the king could read", "Literacy had spread."), ("Print supported the monarchy only", "Literature also mocked the monarchy.")], "Also: a culture of debate, and literature mocking the royalty.")
M("mcq22", C19, "A children's press devoted to literature for children was set up in France in:", [("1857", ""), ("1812", "1812 is the Grimm Brothers' collection."), ("1878", "1878 is the Vernacular Press Act."), ("1920", "The Shilling Series came in the 1920s.")], "1857.", "medium")
M("mcq23", C19, "The Grimm Brothers of Germany are known for:", [("compiling traditional folk tales from peasants", ""), ("inventing the offset press", "That was a late-19th-century technology."), ("writing the Ninety Five Theses", "That was Luther."), ("publishing Bombay Samachar", "That was in India.")], "Published in 1812.")
M("mcq24", C19, "Which of these was a famous 19th-century woman novelist?", [("Jane Austen", ""), ("Erasmus", "Erasmus was a Latin scholar."), ("Menocchio", "Menocchio was a miller."), ("Mercier", "Mercier was a male novelist.")], "Jane Austen, the Bronte sisters and George Eliot.")
M("mcq25", C19, "How many sheets per hour could Richard M. Hoe's cylindrical press print?", [("8,000", ""), ("180", "180 copies were Gutenberg's Bibles."), ("6", "Six was the number of colours on the offset press."), ("5,000", "5,000 were copies of Luther's New Testament.")], "8,000 sheets per hour.", "medium")
M("mcq26", C19, "Why did publishers bring out cheap paperback editions in the 1930s?", [("They feared a decline in book purchases during the Great Depression", ""), ("Paper became free", "Paper was not free."), ("The government ordered it", "It was a business strategy."), ("Hardbacks were banned", "There was no ban.")], "Paperbacks kept books affordable.", "medium")
M("mcq27", INDIA, "The printing press first came to India with:", [("Portuguese missionaries in Goa", ""), ("the English East India Company in Calcutta", "That came later."), ("Dutch traders in Cochin", "Dutch missionaries printed Tamil texts by 1710."), ("Persian merchants in Bombay", "The first press came to Goa.")], "In the mid-16th century.")
M("mcq28", INDIA, "The first Tamil book was printed in 1579 at:", [("Cochin", ""), ("Goa", "Konkani books were printed in Goa."), ("Calcutta", "Calcutta came later."), ("Madras", "The chapter names Cochin.")], "Cochin, by Catholic priests.", "medium")
M("mcq29", INDIA, "Who edited the Bengal Gazette from 1780, calling it 'a commercial paper open to all, but influenced by none'?", [("James Augustus Hickey", ""), ("Gangadhar Bhattacharya", "He brought out the first Indian newspaper."), ("Rammohun Roy", "He published Sambad Kaumudi."), ("Warren Hastings", "Hastings persecuted Hickey.")], "James Augustus Hickey.")
M("mcq30", INDIA, "Who brought out the first Indian newspaper, the weekly Bengal Gazette?", [("Gangadhar Bhattacharya", ""), ("James Augustus Hickey", "Hickey's was an English private paper."), ("Bal Gangadhar Tilak", "Tilak edited Kesari."), ("Raja Ravi Varma", "He was a painter.")], "Gangadhar Bhattacharya, close to Rammohun Roy.", "medium")
M("mcq31", INDIA, "Rammohun Roy published which newspaper from 1821?", [("Sambad Kaumudi", ""), ("Samachar Chandrika", "That was the orthodox paper opposing him."), ("Kesari", "Kesari was Tilak's."), ("Bombay Samachar", "That was a Gujarati paper of 1822.")], "Sambad Kaumudi.")
M("mcq32", INDIA, "Which Gujarati newspaper appeared in 1822?", [("Bombay Samachar", ""), ("Jam-i-Jahan Nama", "That was a Persian paper."), ("Sambad Kaumudi", "That was a Bengali paper."), ("Native Opinion", "That was a later paper.")], "Bombay Samachar.")
M("mcq33", INDIA, "The Deoband Seminary, founded in 1867, published:", [("thousands of fatwas guiding Muslims in everyday life", ""), ("the Ramcharitmanas", "That was printed in Calcutta in 1810."), ("Gulamgiri", "That was Phule's book."), ("Amar Jiban", "That was Rashsundari Debi's.")], "Fatwas explaining Islamic doctrines.", "medium")
M("mcq34", INDIA, "The first printed edition of Tulsidas's Ramcharitmanas came out from Calcutta in:", [("1810", ""), ("1867", "1867 is Deoband."), ("1876", "1876 is Amar Jiban."), ("1821", "1821 is Sambad Kaumudi.")], "1810.", "medium")
M("mcq35", INDIA, "Who wrote 'Amar Jiban', the first full-length autobiography in Bengali?", [("Rashsundari Debi", ""), ("Kailashbashini Debi", "She wrote about women's oppression from the 1860s."), ("Pandita Ramabai", "She wrote in Maharashtra."), ("Tarabai Shinde", "She wrote in Maharashtra.")], "Published in 1876.")
M("mcq36", INDIA, "Jyotiba Phule wrote about the injustices of the caste system in:", [("Gulamgiri", ""), ("Istri Dharm Vichar", "That was by Ram Chaddha."), ("Sacchi Kavitayan", "That was a millworker's poetry."), ("Chhote Aur Bade Ka Sawal", "That was by Kashibaba.")], "Gulamgiri (1871).")
M("mcq37", INDIA, "The Vernacular Press Act of 1878 was modelled on:", [("the Irish Press Laws", ""), ("the British Constitution", "It was modelled on the Irish Press Laws."), ("the Index of Prohibited Books", "That was the Church's list."), ("Macaulay's rules of 1835", "Macaulay's rules restored freedoms.")], "The Irish Press Laws.")
M("mcq38", INDIA, "Why was Bal Gangadhar Tilak imprisoned in 1908?", [("He wrote with sympathy about deported Punjab revolutionaries in Kesari", ""), ("He set up a printing press without permission", "The reason was his writing."), ("He opposed the Grimm Brothers", "Unrelated."), ("He published Sambad Kaumudi", "That was Rammohun Roy.")], "This provoked protests across India.")
M("mcq39", INDIA, "Which area of central Calcutta was devoted to printing cheap popular books?", [("Battala", ""), ("Edo", "Edo is in Japan."), ("Wittenberg", "Wittenberg is in Germany."), ("Deoband", "Deoband is a seminary in north India.")], "Battala.", "medium")
M("mcq40", INDIA, "Who restored press freedoms in 1835 by formulating new rules?", [("Thomas Macaulay", ""), ("Warren Hastings", "Hastings persecuted Hickey."), ("Lord Lytton", "The chapter credits Macaulay in 1835."), ("James Hickey", "Hickey was an editor.")], "With Governor-General Bentinck's agreement.", "medium")
# ---------------- Assertion-reason ----------------
C.arq("ar1", EUR, "Handwritten manuscripts could not satisfy the growing demand for books.", "Copying was expensive, laborious and time-consuming, and manuscripts were fragile.", 0,
      "R explains A.", "demand for books grew in the 15th century.", "copying by hand was slow and costly.")
C.arq("ar2", IMPACT, "The Roman Catholic Church began an Index of Prohibited Books.", "Popular reading led people like Menocchio to question the Church's teachings.", 0,
      "R explains A.", "it was kept from 1558.", "the Church feared heresy spread through print.")
C.arq("ar3", IMPACT, "Print directly shaped the minds of all people before the French Revolution.", "People also read royal and Church propaganda and accepted some ideas while rejecting others.", 3,
      "A is false: print did not directly shape minds; it opened up the possibility of thinking differently. R is true.", "print did not directly shape minds.", "readers chose what to accept.")
C.arq("ar4", INDIA, "Warren Hastings persecuted James Augustus Hickey.", "Hickey published gossip about senior Company officials.", 0,
      "R explains A.", "Hastings encouraged official newspapers instead.", "the gossip damaged the Company's image.")
C.arq("ar5", INDIA, "The Vernacular Press Act was passed in 1878.", "Vernacular newspapers had become assertively nationalist after 1857.", 0,
      "R explains A: the government wanted to control nationalist criticism.", "it allowed censorship of vernacular papers.", "nationalist papers alarmed the government.")
C.arq("ar6", INDIA, "Print helped create pan-Indian identities.", "Newspapers were printed only in English.", 2,
      "A is true; R is false: many newspapers were in vernacular languages.", "newspapers connected communities across India.", "vernacular papers were numerous.")
# ---------------- True / false ----------------
C.tf("tf1", EAST, "The first printed books were produced in Germany.", False, "Print began in China, Japan and Korea; China printed books from woodblocks from AD 594.")
C.tf("tf2", EUR, "The first book Gutenberg printed was the Bible.", True, "About 180 copies, which took three years.")
C.tf("tf3", INDIA, "Macaulay's rules of 1835 restricted press freedom in India.", False, "Macaulay's rules restored earlier press freedoms.")
C.tf("tf4", INDIA, "Rashsundari Debi learnt to read secretly in her kitchen.", True, "She later wrote Amar Jiban (1876).")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", IMPACT, "How did oral culture and print culture mix after the print revolution?",
  ["Printers published popular ballads and folk tales with many pictures, which were sung and recited at village gatherings and in town taverns.", "So oral culture entered print, and printed material was passed on orally; the hearing public and reading public intermingled."])
W("vsa2", "very_short_answer", INDIA, "Why did the East India Company begin to censor the press before 1857? Give two points.",
  ["Early controls were aimed at Englishmen in India who criticised Company misrule and the actions of particular officers.", "The Company worried that such criticism would be used in England to attack its trade monopoly in India."])
W("vsa3", "very_short_answer", INDIA, "How did the ulama use print in the 19th century?",
  ["Fearing that colonial rulers would encourage conversion and change Muslim personal laws, they used cheap lithographic presses to publish Persian and Urdu translations of holy scriptures and religious newspapers.", "The Deoband Seminary (1867) published thousands of fatwas guiding Muslims in everyday life."])
W("sa1", "short_answer", C19, "How did children, women and workers become new readers in 19th-century Europe?",
  ["Children: compulsory primary education created a demand for textbooks; a children's press began in France in 1857, and the Grimm Brothers published folk tales in 1812.",
   "Women: penny magazines and manuals were written for them, and novelists like Jane Austen, the Bronte sisters and George Eliot wrote about strong women.",
   "Workers: lending libraries educated workers and artisans, and as working hours shortened, workers wrote political tracts and autobiographies."])
W("sa2", "short_answer", INDIA, "How did print help the debates on social and religious reform in India?",
  ["Debates on widow immolation, monotheism, priesthood and idolatry were carried out in printed tracts and newspapers, allowing a wider public to take part.",
   "Ideas were printed in everyday spoken language; Rammohun Roy's Sambad Kaumudi (1821) was opposed by the orthodox Samachar Chandrika.",
   "Muslim ulama, Deoband's fatwas and cheap editions of Hindu scriptures like the Ramcharitmanas spread religious knowledge in vernaculars, connecting communities."])
W("la1", "long_answer", IMPACT, "Explain how print culture helped bring about the French Revolution.",
  ["Print popularised the ideas of Enlightenment thinkers like Voltaire and Rousseau, which criticised tradition, superstition and despotism.",
   "They argued for the rule of reason and attacked the sacred authority of the Church and the despotic power of the state, eroding the legitimacy of the old order.",
   "Print created a new culture of dialogue and debate in which all values and institutions were re-evaluated by a public aware of the power of reason.",
   "By the 1780s, literature, cartoons and caricatures mocked the royalty and showed the monarchy enjoying pleasures while common people suffered, spreading hostility.",
   "Yet print did not directly shape minds; it opened up the possibility of thinking differently."])
W("cb1", "case_based", EUR, "Read the source and answer the questions.\n\n*\"Johann Gutenberg was the son of a merchant and grew up on a large agricultural estate. From his childhood he had seen wine and olive presses. Subsequently, he learnt the art of polishing stones, became a master goldsmith, and also acquired the expertise to create lead moulds used for making trinkets.\"* (NCERT)\n\n"
  "(i) What did Gutenberg see on his family estate as a child? (1)\n\n(ii) What did the olive press provide the model for? (1)\n\n(iii) How did Gutenberg's press change the production of books? (2)",
  ["(i) Wine and olive presses.", "(ii) The printing press (moulds were used to cast metal types).",
   "(iii) By 1448 he perfected the system and printed about 180 Bibles in three years; presses spread across Europe, and by the 16th century about 200 million copies of books circulated, starting the print revolution."])
W("cb2", "case_based", INDIA, "Read the source and answer the questions.\n\n*\"In 1878, the Vernacular Press Act was passed, modelled on the Irish Press Laws. It provided the government with extensive rights to censor reports and editorials in the vernacular press. From now on the government kept regular track of the vernacular newspapers published in different provinces.\"* (NCERT)\n\n"
  "(i) On which laws was the Vernacular Press Act modelled? (1)\n\n(ii) What happened if a newspaper ignored a warning about seditious reports? (1)\n\n(iii) Why did the government pass this Act, and how did nationalists respond? (2)",
  ["(i) The Irish Press Laws.", "(ii) The press was liable to be seized and the printing machinery confiscated.",
   "(iii) After 1857 vernacular newspapers became assertively nationalist, so the government wanted to control their criticism; yet nationalist papers grew in number, and repression like Tilak's imprisonment (1908) provoked widespread protests."])

chapter = header(SUBJ, N, "Print Culture and the Modern World", ["print_east_asia", "print_europe_gutenberg", "print_revolution_impact", "nineteenth_century_print", "print_in_india"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: this chapter is fully in the board examination (History: 18 marks + 2 map marks; there is no map item from this chapter).")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
