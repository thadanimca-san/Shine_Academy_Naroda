"""CBSE Class 10 History Ch 3: The Making of a Global World.
Board exam 2025-26: subtopics 1 to 1.3 only (pre-modern world, silk routes, food travels, conquest-disease-trade).
Subtopics 2 to 4.4 (1815 to the end of Bretton Woods) are an interdisciplinary project, taught briefly and marked as such."""
import sys
from ss_common import make, header, path, SQP, SHINE

ROOT = sys.argv[1]
SUBJ, N = "history", 3
PATH = path(SUBJ, "ch03_making_of_a_global_world")
C = make(SUBJ, N, "his10ch03")
blk, M, W = C.blk, C.m, C.w
SILK, FOOD, CONQ, PROJ = ["silk_routes"], ["food_travels"], ["conquest_disease_trade"], ["project_19th_20th_century"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 3 exercises", "question": n}

FOODS = ("| Food | Where it came from | What happened |\n|---|---|---|\n| Noodles → spaghetti | China | travelled west; perhaps Arab traders took pasta to 5th-century Sicily |\n"
         "| Potatoes | the Americas | the poor in Europe ate better and lived longer; Ireland came to depend on them |\n| Maize, tomatoes, chillies, sweet potatoes, groundnuts, soya | the Americas | reached the rest of the world only after Columbus reached America |")
CONQ_T = ("| Factor | How it changed the world in the 16th century |\n|---|---|\n| Sea routes | European sailors found a sea route to Asia and crossed the western ocean to America |\n"
          "| Silver | silver from mines in present-day Peru and Mexico increased Europe's wealth and paid for trade with Asia |\n"
          "| Germs | smallpox carried by the Spanish killed the original inhabitants of America, who had no immunity: a weapon stronger than guns |\n"
          "| Push factors in Europe | poverty, hunger, crowded cities, deadly diseases and religious persecution made thousands flee to America |\n"
          "| Plantations | slaves captured in Africa grew cotton and sugar in America for European markets |\n| China's isolation | from the 15th century China restricted overseas contacts; the centre of world trade moved westwards to Europe |")
PROJECT = ("| Period (project topic) | Key facts |\n|---|---|\n| 1815–1914: the world economy takes shape | Three flows: trade, labour and capital. Britain abolished the Corn Laws; nearly 50 million people emigrated from Europe to America and Australia; railways, steamships, the telegraph and refrigerated ships connected markets |\n"
           "| Colonialism | Berlin conference (1885) carved up Africa; **rinderpest** (1890s) killed about 90% of Africa's cattle, forcing Africans into wage labour |\n"
           "| Indentured labour | Indian workers from eastern UP, Bihar, central India and Tamil Nadu went to the Caribbean (Trinidad, Guyana, Surinam), Mauritius and Fiji; Hosay festival, chutney music; indenture abolished in **1921** |\n"
           "| Indian entrepreneurs | Shikaripuri shroffs and Nattukottai Chettiars financed export agriculture in Central and Southeast Asia |\n"
           "| Inter-war economy | First World War (1914–18); the USA became an international creditor; the **Great Depression** began around 1929; in India wheat prices fell 50% between 1928 and 1934 |\n"
           "| Post-war | **Bretton Woods conference (July 1944)** set up the IMF and the World Bank; fixed exchange rates with the dollar tied to gold at 35 US dollars an ounce; later, decolonisation, G-77 and globalisation |")

sections = [
 {"id": "s1", "title": "A world connected long ago", "blocks": [
  blk("s1.hook", "hook", title="What's on your plate?",
    body="Look at a plate of pav bhaji or a samosa. Potatoes, tomatoes and green chillies are in almost every Indian kitchen today. But none of them grew in India five hundred years ago: they all came from the Americas.\n\n"
         "The world was connected long before mobile phones and the internet. Traders, travellers, priests and pilgrims carried goods, money, skills, ideas, inventions, and even germs and diseases across oceans and deserts. "
         "This chapter traces how the world came to be connected, starting in the **pre-modern world**: the silk routes, the journeys of foods, and the conquest of America."),
  blk("s1.inspiration", "inspiration", title="A pilgrim who walked the silk routes", person="Xuanzang (Hiuen Tsang)", years="602–664",
    body="The Chinese monk Xuanzang set out in 629 CE on the silk routes, crossing the deserts of Central Asia and the mountains of the Hindu Kush, to reach India and learn about Buddhism at its source. "
         "He studied at the great university of **Nalanda** and returned to China in 645 with hundreds of Buddhist texts, which he spent the rest of his life translating.\n\n"
         "His travel account is one of the most important records of 7th-century India. The silk routes carried not only silk and spices, but also ideas and learning like his.",
    future="Studying global connections leads to careers in international trade, diplomacy, economics, archaeology, tourism and the travel industry."),
  C.socratic("s1.socratic", "Which of these do you think travelled along the old trade routes?",
    ["Goods, people, ideas and even diseases", "Only goods", "Only soldiers"], 0,
    "Trade routes carried far more than goods: traders, travellers and pilgrims carried religions, skills, inventions and germs too."),
 ]},
 {"id": "s2", "title": "The silk routes", "blocks": [
  blk("s2.thm", "theory", title="Silk routes link the world", revision=True,
    body="The **silk routes** are a good example of vibrant pre-modern trade and cultural links between distant parts of the world. The name comes from the importance of west-bound **Chinese silk** cargoes along this route.\n\n"
         "- Historians have identified several silk routes, over land and by sea, knitting together vast regions of **Asia** and linking Asia with **Europe** and **northern Africa**.\n"
         "- They are known to have existed since **before the Christian Era** and thrived almost till the **fifteenth century**.\n"
         "- **Goods:** Chinese pottery, textiles and spices from India and Southeast Asia travelled west; in return, **precious metals, gold and silver**, flowed from Europe to Asia.\n"
         "- **Culture:** trade and cultural exchange went hand in hand. Early Christian missionaries almost certainly travelled this route to Asia, as did early Muslim preachers a few centuries later. "
         "Much before all this, **Buddhism** emerged from eastern India and spread in several directions through intersecting points on the silk routes."),
  C.kc("s2.check", "Which of these flowed from Europe to Asia along the silk routes?",
    [("Gold and silver", ""), ("Chinese silk", "Silk went west, from China towards Europe."), ("Indian spices", "Spices went west from India and Southeast Asia."), ("Chinese pottery", "Pottery went west from China.")],
    "Precious metals, gold and silver, flowed from Europe to Asia to pay for Asian goods."),
  C.kc("s2.check2", "Which religion spread from eastern India along the silk routes?",
    [("Buddhism", ""), ("Christianity", "Christian missionaries travelled to Asia along the routes; Christianity did not emerge from India."),
     ("Islam", "Muslim preachers travelled the routes later; Islam did not emerge from India."), ("Zoroastrianism", "The chapter mentions Buddhism spreading from eastern India.")],
    "Buddhism emerged from eastern India and spread through the silk routes."),
 ]},
 {"id": "s3", "title": "Food travels: spaghetti and potatoes", "blocks": [
  blk("s3.thm", "theory", title="How foods crossed the world", revision=True,
    body="Food offers many examples of long-distance cultural exchange. Traders and travellers introduced new crops to the lands they travelled.\n\n"
         "- Even 'ready' foods in distant parts of the world might share common origins. Take **spaghetti and noodles**: it is believed that noodles travelled **west from China** to become spaghetti. "
         "Or perhaps **Arab traders** took pasta to **fifth-century Sicily**, an island now in Italy. Similar foods were also known in India and Japan, so the truth about their origins may never be known.\n"
         "- Many of our common foods such as **potatoes, soya, groundnuts, maize, tomatoes, chillies and sweet potatoes** were not known to our ancestors until about five centuries ago. "
         "They came to Europe and Asia only after **Christopher Columbus** accidentally discovered the vast continent that would later become known as the **Americas**. Many of our common foods came from America's original inhabitants, the **American Indians**.\n"
         "- **New crops could make the difference between life and death.** Europe's poor began to eat better and live longer with the arrival of the humble **potato**. "
         "**Ireland's** poorest peasants became so dependent on potatoes that when disease destroyed the potato crop in the **mid-1840s**, hundreds of thousands died of starvation."),
  blk("s3.table", "markdown_table", title="Foods that travelled", revision=True, body=FOODS),
  C.kc("s3.check", "Which of these foods did NOT come to Asia and Europe from the Americas?",
    [("Noodles", ""), ("Potatoes", "Potatoes came from the Americas."), ("Tomatoes", "Tomatoes came from the Americas."), ("Maize", "Maize came from the Americas.")],
    "Noodles came from China; potatoes, tomatoes, maize, chillies, groundnuts and sweet potatoes came from the Americas."),
  C.kc("s3.check2", "What happened in Ireland in the mid-1840s?",
    [("Disease destroyed the potato crop and hundreds of thousands died of starvation", ""), ("Spaghetti was invented", "Pasta's origins are linked to China and Sicily."),
     ("Ireland discovered the silk routes", "The silk routes linked Asia with Europe and Africa."), ("Smallpox killed the American Indians", "That happened in America in the 16th century.")],
    "Ireland's poorest peasants depended on potatoes, so the potato famine was a disaster."),
 ]},
 {"id": "s4", "title": "Conquest, disease and trade", "blocks": [
  blk("s4.thm", "theory", title="The 16th century: the world shrinks", revision=True,
    body="The pre-modern world shrank greatly in the **sixteenth century** after **European sailors found a sea route to Asia** and also successfully crossed the western ocean to **America**.\n\n"
         "- For centuries the **Indian Ocean** had known bustling trade, with goods, people, knowledge and customs criss-crossing its waters. The **Indian subcontinent** was central to these flows and a crucial point in their networks. "
         "The entry of the Europeans helped expand or redirect some of these flows towards Europe.\n"
         "- Before its 'discovery', America had been cut off from regular contact with the rest of the world for millions of years. From the 16th century its vast lands and abundant crops and minerals began to transform trade and lives everywhere.\n"
         "- **Precious metals**, particularly **silver**, from mines in present-day **Peru and Mexico** enhanced Europe's wealth and financed its trade with Asia. Legends spread in 17th-century Europe about South America's fabled wealth, and many expeditions set off in search of **El Dorado**, the fabled city of gold.\n\n"
         "**Germs as weapons:** the **Portuguese and Spanish** conquest and colonisation of America was decisively under way by the mid-sixteenth century. European conquest was not just a result of superior firepower. "
         "The most powerful weapon of the Spanish conquerors was not a conventional military weapon at all: it was the **germs such as those of smallpox** that they carried on their persons. Because of their long isolation, America's original inhabitants had **no immunity** against these diseases. "
         "**Smallpox** in particular proved a deadly killer. Once introduced, it spread deep into the continent, ahead even of any Europeans reaching there. It killed and decimated whole communities, paving the way for conquest. Guns could be bought or captured; diseases such as smallpox could not be.\n\n"
         "**Europe's push factors:** until the nineteenth century, **poverty and hunger** were common in Europe. Cities were crowded and **deadly diseases** were widespread. Religious conflicts were common, and religious dissenters were persecuted. **Thousands therefore fled Europe for America.** "
         "Here, by the eighteenth century, **plantations** worked by **slaves captured in Africa** were growing **cotton and sugar** for European markets.\n\n"
         "**The centre of trade moves west:** until well into the eighteenth century, **China and India** were among the world's richest countries and pre-eminent in Asian trade. However, from the **fifteenth century**, China is said to have **restricted overseas contacts** and retreated into isolation. "
         "China's reduced role and the rising importance of the Americas gradually moved the centre of world trade westwards. **Europe now emerged as the centre of world trade.**"),
  blk("s4.table", "markdown_table", title="Why the 16th century changed everything", revision=True, body=CONQ_T),
  C.kc("s4.check", "What was the most powerful 'weapon' of the Spanish conquerors of America?",
    [("Germs such as smallpox", ""), ("Cannons", "Guns could be bought or captured; diseases could not."), ("Silk", "Silk was a trade good."), ("Silver coins", "Silver was taken from America, not used to conquer it.")],
    "The original inhabitants had no immunity, so smallpox destroyed whole communities and paved the way for conquest."),
  C.kc("s4.check2", "Why did thousands flee Europe for America before the nineteenth century?",
    [("Poverty, hunger, deadly diseases and religious persecution", ""), ("To join the silk routes", "The silk routes were in Asia."),
     ("Because China invited them", "China was retreating into isolation."), ("Because Europe was the richest place on earth", "Poverty and hunger were common in Europe.")],
    "Europe had widespread poverty and hunger, crowded cities, deadly diseases and religious conflict."),
 ]},
 {"id": "s5", "title": "Beyond the board exam: the project topics", "blocks": [
  blk("s5.note", "teacher_tip", title="For your interdisciplinary project, not the board paper",
    body="In the CBSE 2025-26 syllabus, only **subtopics 1 to 1.3** of this chapter are tested in the board examination. "
         "Subtopics **2 to 4.4** (the nineteenth century, 1815–1914, to the end of Bretton Woods and the beginning of 'globalisation') form an **interdisciplinary project** together with Geography Chapter 7 (Lifelines of National Economy) and Economics Chapter 4 (Globalisation), assessed internally for 5 marks. "
         "The summary below helps you with that project."),
  blk("s5.table", "markdown_table", title="The project topics at a glance", revision=True, body=PROJECT),
 ]},
 {"id": "s6", "title": "Remember, avoid, practise", "blocks": [
  blk("s6.memory", "memory_trick", title="Memory tricks",
    body="- **Silk routes = \"Silk goes west, silver goes east, Buddha goes everywhere.\"**\n- **Gifts of the Americas: \"PoToMaC GS\":** **Po**tatoes, **To**matoes, **Ma**ize, **C**hillies, **G**roundnuts, **S**weet potatoes (and soya).\n"
         "- **16th century = 3 S:** **S**ea route, **S**ilver from Peru and Mexico, **S**mallpox.\n- **Push from Europe = P-H-D-R:** **P**overty, **H**unger, **D**isease, **R**eligious persecution."),
  blk("s6.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying silk routes carried only silk: they carried pottery, textiles, spices, precious metals, religions and people.\n2. Writing that potatoes and chillies are native to India: they came from the Americas.\n"
         "3. Saying the Spanish conquered America mainly with guns: germs like smallpox were their most powerful weapon.\n4. Saying gold flowed from Asia to Europe on the silk routes: precious metals flowed **from Europe to Asia**.\n"
         "5. Writing that China expanded trade from the 15th century: it **restricted** overseas contacts.\n6. Learning Bretton Woods and the Great Depression for the board exam: they are **project** topics in 2025-26."),
  blk("s6.tip", "teacher_tip", title="Try this in class",
    body="Run a 'kitchen archaeology' activity: students list ten ingredients used at home and find out where each one first came from. Mark them on a world map with arrows. "
         "Then discuss: how would Indian food be different without the Americas?"),
  blk("s6.reflection", "reflection", title="Think and explain",
    body="Why do historians say that germs, not guns, conquered America? Explain in three sentences."),
  blk("s6.connection", "connection", title="Where this leads",
    body="- **Geography Chapter 7, Lifelines of National Economy** and **Economics Chapter 4, Globalisation:** these form the interdisciplinary project with this chapter.\n"
         "- **Science, Chapter 13 (Our Environment) and health:** diseases spreading across populations without immunity.\n- **Chapter 1:** European nation-states became the colonial powers that reshaped world trade."),
  blk("s6.mastery", "mastery", title="Mastery challenge",
    body="'The pre-modern world changed dramatically in the sixteenth century.' Explain with three points in about 60 words.\n\n"
         "**Model answer:** European sailors found a sea route to Asia and crossed the western ocean to America. Silver from mines in Peru and Mexico increased Europe's wealth and financed its trade with Asia. "
         "Germs such as smallpox wiped out America's original inhabitants, who had no immunity, paving the way for Portuguese and Spanish colonisation; plantations worked by African slaves grew cotton and sugar for Europe, and the centre of world trade moved westwards to Europe."),
  blk("s6.summary", "summary", title="Chapter summary",
    body="- The silk routes (from before the Christian Era to about the 15th century) linked Asia with Europe and northern Africa; silk, pottery, textiles and spices went west, gold and silver went east; Buddhism, Christianity and Islam spread along them.\n"
         "- Foods travelled: noodles from China (perhaps pasta to Sicily); potatoes, maize, tomatoes, chillies, groundnuts and sweet potatoes from the Americas; the potato saved Europe's poor but its failure caused famine in Ireland in the 1840s.\n"
         "- In the 16th century Europeans found sea routes to Asia and America; silver from Peru and Mexico enriched Europe; smallpox destroyed America's original inhabitants; poverty, disease and persecution pushed Europeans to America; African slaves worked plantations.\n"
         "- China's isolation and the rise of the Americas moved the centre of world trade to Europe.\n- 1815 to the end of Bretton Woods is an interdisciplinary project topic in 2025-26."),
  blk("s6.examtips", "exam_tips", title="Board exam tips",
    body="- Questions from this chapter are limited to the pre-modern world: silk routes, food travels, and conquest, disease and trade.\n- The 2025-26 sample paper asked: silk routes as an example of trade and cultural links (2 marks), and why new crops could make the difference between life and death (2 marks).\n"
         "- Give two concrete examples in each 2-mark answer (e.g. Chinese silk and pottery; Buddhism).\n- Remember the direction of flows: silk west, gold and silver east."),
  blk("s6.flash1", "flashcard", front="Why are they called 'silk routes'?", back="Because of the importance of west-bound Chinese silk cargoes along them."),
  blk("s6.flash2", "flashcard", front="Name four foods that came from the Americas.", back="Potatoes, maize, tomatoes, chillies (also groundnuts, soya, sweet potatoes)."),
  blk("s6.flash3", "flashcard", front="Where did the silver that enriched Europe come from?", back="Mines in present-day Peru and Mexico."),
  blk("s6.flash4", "flashcard", front="Why did smallpox kill so many American Indians?", back="They had been isolated for so long that they had no immunity to European diseases."),
 ]},
]

# ---------------- Sample paper ----------------
M("sqp3", CONQ, "Thousands of people fled Europe for America in the 19th century due to -",
  [("Widespread poverty and deadly diseases", ""), ("Frequent famines and poor living conditions", "Hunger was part of it, but the textbook stresses poverty, deadly diseases and religious persecution."),
   ("Continuous wars and political instability", "The textbook names poverty, hunger, disease and religious conflict, not continuous wars."), ("Harsh climate and repeated natural disasters", "Climate is not given as a reason.")],
  "Until the 19th century poverty and hunger were common in Europe, cities were crowded and deadly diseases were widespread, so thousands fled to America.", "medium", SQP(3))
W("sqp5a", "very_short_answer", SILK, "'The silk route was a good example of vibrant pre-modern trade and cultural links between distant parts of the world.' Explain the statement with any two examples.",
  ["Trade: Chinese silk and pottery, and textiles and spices from India and Southeast Asia, travelled west, while gold and silver flowed from Europe to Asia.",
   "Culture: early Christian missionaries and later Muslim preachers travelled these routes to Asia, and Buddhism spread from eastern India in several directions along them."], source=SQP("5A"))
W("sqp5b", "very_short_answer", FOOD, "'Sometimes the new crops could make the difference between life and death.' Explain the statement with any two examples.",
  ["Europe's poor began to eat better and live longer with the arrival of the humble potato from the Americas.",
   "Ireland's poorest peasants became so dependent on potatoes that when disease destroyed the crop in the mid-1840s, hundreds of thousands died of starvation."], source=SQP("5B"))

# ---------------- NCERT exercises (board part) ----------------
W("ex1", "short_answer", SILK, "Give two examples of different types of global exchanges which took place before the seventeenth century, choosing one example from Asia and one from the Americas.",
  ["Asia: the silk routes linked China and India with Europe and northern Africa; Chinese silk, pottery and Indian spices went west, while gold and silver came east; Buddhism spread from eastern India along these routes.",
   "Americas: after Columbus, foods such as potatoes, maize, tomatoes, chillies and groundnuts travelled from America to Europe and Asia.",
   "Also from the Americas: silver from mines in Peru and Mexico enhanced Europe's wealth and financed its trade with Asia."], source=ex(1))
W("ex2", "short_answer", CONQ, "Explain how the global transfer of disease in the pre-modern world helped in the colonisation of the Americas.",
  ["The Portuguese and Spanish conquerors carried germs such as smallpox on their persons.",
   "America's original inhabitants had been isolated for millions of years and had no immunity against these diseases, so smallpox spread deep into the continent, even ahead of the Europeans.",
   "It killed and decimated whole communities, weakening resistance and paving the way for conquest; unlike guns, disease could not be bought or captured."], source=ex(2))
W("ex3", "long_answer", CONQ, "Explain how the world shrank and changed in the sixteenth century.",
  ["European sailors found a sea route to Asia and crossed the western ocean to America; the Indian subcontinent, central to Indian Ocean trade, became linked to Europe.",
   "America's vast lands, crops and minerals transformed trade; silver from Peru and Mexico enhanced Europe's wealth and financed its trade with Asia.",
   "Smallpox and other germs carried by the Spanish and Portuguese killed America's original inhabitants, who had no immunity, and paved the way for colonisation.",
   "Poverty, hunger, disease and religious persecution in Europe made thousands flee to America, where plantations worked by African slaves grew cotton and sugar for Europe.",
   "As China restricted overseas contacts from the 15th century and the Americas grew in importance, the centre of world trade moved westwards to Europe."], source=SHINE)

# ---------------- Shine MCQs (board part) ----------------
M("mcq01", SILK, "The silk routes got their name because of:", [("the importance of west-bound Chinese silk cargoes", ""), ("silk being made in Europe", "Silk came from China and went west."), ("roads made of silk", "The name refers to the main cargo, not the roads."), ("a king named Silk", "There was no such king.")], "West-bound Chinese silk was the most important cargo.")
M("mcq02", SILK, "The silk routes linked Asia with:", [("Europe and northern Africa", ""), ("America and Australia", "America and Australia were not on these routes."), ("Antarctica", "Antarctica had no trade."), ("only India and China", "They linked Asia with Europe and northern Africa too.")], "Over land and sea, the silk routes knit Asia to Europe and northern Africa.")
M("mcq03", SILK, "The silk routes are known to have existed since:", [("before the Christian Era", ""), ("the 15th century", "They thrived almost till the 15th century; they began much earlier."), ("the 19th century", "That is far too late."), ("1945", "That is the modern period.")], "Before the Christian Era, thriving almost till the 15th century.")
M("mcq04", SILK, "Which goods travelled west from Asia along the silk routes?", [("Chinese pottery, textiles and Indian spices", ""), ("Gold and silver", "Gold and silver flowed east, from Europe to Asia."), ("Potatoes and maize", "These came from the Americas, much later."), ("Cars and machines", "These are modern goods.")], "Pottery, textiles and spices went west.")
M("mcq05", SILK, "Which religion emerged from eastern India and spread along the silk routes?", [("Buddhism", ""), ("Christianity", "Christian missionaries travelled the routes, but Christianity did not emerge from India."), ("Islam", "Muslim preachers travelled the routes later."), ("Shintoism", "Shintoism is Japanese.")], "Buddhism.")
M("mcq06", FOOD, "Noodles are believed to have travelled west from which country to become spaghetti?", [("China", ""), ("Italy", "Spaghetti is the Italian form; noodles came from China."), ("Peru", "Peru gave silver and potatoes."), ("Ireland", "Ireland depended on potatoes.")], "From China.")
M("mcq07", FOOD, "Who perhaps took pasta to fifth-century Sicily?", [("Arab traders", ""), ("Spanish conquerors", "The Spanish conquered America in the 16th century."), ("Christopher Columbus", "Columbus reached America in 1492."), ("Buddhist monks", "Monks carried Buddhism, not pasta.")], "Perhaps Arab traders.", "medium")
M("mcq08", FOOD, "Which of these foods came from the Americas?", [("Chillies", ""), ("Noodles", "Noodles came from China."), ("Rice", "Rice was grown in Asia long before."), ("Wheat", "Wheat was known in Asia and Europe long before.")], "Chillies, potatoes, maize, tomatoes, groundnuts, soya and sweet potatoes came from the Americas.")
M("mcq09", FOOD, "Many common foods came to Europe and Asia after whose voyage to the Americas?", [("Christopher Columbus", ""), ("Vasco da Gama", "Vasco da Gama reached India by sea."), ("Xuanzang", "Xuanzang travelled to India on the silk routes."), ("Marco Polo", "Marco Polo travelled to China.")], "After Columbus accidentally reached the Americas.")
M("mcq10", FOOD, "The Irish potato famine took place in the:", [("mid-1840s", ""), ("1520s", "That was the time of the Spanish conquest of America."), ("1929", "1929 marks the Great Depression."), ("5th century", "That was pasta in Sicily.")], "Disease destroyed the potato crop in the mid-1840s.")
M("mcq11", FOOD, "How did the potato change the lives of Europe's poor?", [("They ate better and lived longer", ""), ("They became rich traders", "The potato improved diet, not wealth."), ("They stopped farming", "They farmed potatoes."), ("They moved to China", "There was no such migration.")], "The humble potato improved the diet of the poor.")
M("mcq12", CONQ, "Silver that enhanced Europe's wealth came mainly from mines in present-day:", [("Peru and Mexico", ""), ("India and China", "India and China received silver from Europe."), ("Ireland and Scotland", "There were no such silver mines."), ("Egypt and Ethiopia", "The silver came from America.")], "Peru and Mexico.")
M("mcq13", CONQ, "'El Dorado' was:", [("a fabled city of gold in South America", ""), ("a silk route town", "It was a legend about South America."), ("a Spanish ship", "It was a legendary city."), ("a disease", "It was a legendary city of gold.")], "Many 17th-century expeditions set off in search of it.")
M("mcq14", CONQ, "Which two European powers conquered and colonised America by the mid-sixteenth century?", [("Portugal and Spain", ""), ("Britain and France", "Britain and France became important later."), ("Germany and Italy", "These were not yet nation-states."), ("Russia and Austria", "They were not involved.")], "The Portuguese and the Spanish.")
M("mcq15", CONQ, "Why did America's original inhabitants die in large numbers from smallpox?", [("They had no immunity because of their long isolation", ""), ("They refused medicine", "No medicine existed for smallpox then."), ("They were starving", "The main reason was lack of immunity."), ("They lived in cold climates", "Climate was not the cause.")], "Long isolation meant no immunity to European germs.")
M("mcq16", CONQ, "By the eighteenth century, plantations in America grew which crops for European markets?", [("Cotton and sugar", ""), ("Tea and coffee", "The chapter mentions cotton and sugar."), ("Wheat and rice", "The chapter mentions cotton and sugar."), ("Silk and spices", "Silk and spices came from Asia.")], "Cotton and sugar, worked by slaves captured in Africa.")
M("mcq17", CONQ, "Who worked on the plantations in America?", [("Slaves captured in Africa", ""), ("Chinese silk weavers", "They worked in China."), ("Irish potato farmers", "They farmed in Ireland."), ("Arab traders", "Arab traders traded across Asia.")], "African slaves.")
M("mcq18", CONQ, "From which century did China restrict its overseas contacts?", [("15th century", ""), ("19th century", "By then China had long been in isolation."), ("5th century", "The silk routes were active then."), ("20th century", "The restriction began much earlier.")], "From the 15th century, China retreated into isolation.")
M("mcq19", CONQ, "Which region emerged as the centre of world trade after the sixteenth century?", [("Europe", ""), ("China", "China restricted overseas contacts."), ("Africa", "Africa supplied slaves and was later colonised."), ("Australia", "Australia was not yet part of world trade.")], "China's isolation and the rise of the Americas moved the centre of trade westwards to Europe.")
M("mcq20", CONQ, "Until well into the eighteenth century, which two countries were among the richest in the world?", [("China and India", ""), ("Spain and Portugal", "They grew rich, but China and India were pre-eminent."), ("Britain and USA", "Britain rose later; the USA was not yet independent."), ("Peru and Mexico", "Their silver went to Europe.")], "China and India were pre-eminent in Asian trade.", "medium")
M("mcq21", CONQ, "Which ocean had bustling trade with the Indian subcontinent at its centre before the Europeans arrived?", [("Indian Ocean", ""), ("Atlantic Ocean", "The Atlantic linked Europe with America."), ("Pacific Ocean", "The chapter speaks of the Indian Ocean."), ("Arctic Ocean", "There was no such trade.")], "The Indian Ocean.")
M("mcq22", SILK, "Who travelled along the silk routes to Asia, according to the chapter?", [("Christian missionaries and later Muslim preachers", ""), ("Only Chinese soldiers", "Many types of travellers used the routes."), ("Spanish conquerors", "They went to America."), ("Irish farmers", "They migrated to America.")], "Missionaries and preachers travelled with traders.")
M("mcq23", CONQ, "Which statement about religious life in Europe before the 19th century is correct?", [("Religious dissenters were persecuted, so many fled to America", ""), ("Everyone was free to follow any religion", "Religious conflicts were common."), ("Buddhism was the main religion", "Buddhism spread in Asia."), ("Religion had no effect on migration", "Persecution was a push factor.")], "Religious persecution pushed people to America.")
M("mcq24", FOOD, "Which of these is NOT among the foods that came from America's original inhabitants?", [("Spaghetti", ""), ("Groundnuts", "Groundnuts came from the Americas."), ("Sweet potatoes", "Sweet potatoes came from the Americas."), ("Soya", "Soya is listed among foods unknown to our ancestors before Columbus.")], "Spaghetti developed from noodles and pasta, with roots in China.")
M("mcq25", SILK, "Until about which century did the silk routes thrive?", [("The fifteenth century", ""), ("The fifth century", "They thrived much longer."), ("The nineteenth century", "By then sea routes dominated."), ("The twentieth century", "That is far too late.")], "They thrived almost till the fifteenth century.")
M("mcq26", CONQ, "For how long had America been cut off from regular contact with the rest of the world before its 'discovery'?", [("Millions of years", ""), ("Fifty years", "It was isolated for millions of years."), ("Two centuries", "It was isolated for millions of years."), ("It was never cut off", "It was isolated until the 16th century.")], "This long isolation explains why its people had no immunity to European diseases.", "medium")
M("mcq27", FOOD, "Besides China and Italy, in which countries were foods similar to noodles also known?", [("India and Japan", ""), ("Peru and Mexico", "These gave silver and new crops."), ("Ireland and Britain", "Ireland is linked to potatoes."), ("Egypt and Ethiopia", "The chapter mentions India and Japan.")], "So the true origin of noodles and pasta may never be known.", "medium")
M("mcq28", CONQ, "Which of the following was NOT a reason why guns alone could not explain the conquest of America?", [("The Spanish had no guns", ""), ("Guns could be bought or captured by the inhabitants", "This is a reason given in the chapter."), ("Smallpox spread ahead of the conquerors", "This is a reason given in the chapter."), ("Diseases could not be bought or captured", "This is a reason given in the chapter.")], "The Spanish did have guns; the point is that germs were a more powerful weapon.", "hard")
M("mcq29", SILK, "What does the chapter say about trade and cultural exchange on the silk routes?", [("They went hand in hand", ""), ("They were always separate", "Missionaries and preachers travelled with traders."), ("Only culture travelled", "Goods travelled too."), ("Only trade travelled", "Religions travelled too.")], "Trade and cultural exchange always went hand in hand.")
M("mcq30", CONQ, "The entry of Europeans into Indian Ocean trade helped to:", [("expand or redirect some trade flows towards Europe", ""), ("end all trade in the Indian Ocean", "Trade continued and expanded."), ("make China the centre of world trade", "Europe became the centre."), ("stop the silver trade", "Silver financed Europe's trade with Asia.")], "Europeans expanded or redirected some flows towards Europe.", "medium")
# ---------------- Project-topic MCQs (internal assessment) ----------------
M("prj01", PROJ, "[Project topic] What were the Corn Laws in Britain?", [("Laws allowing the government to restrict the import of corn", ""), ("Laws forcing farmers to grow corn", "They restricted imports."), ("Laws banning potatoes", "They were about corn imports."), ("Laws on silk trade", "They were about corn.")], "When they were abolished, cheap food imports flooded Britain.", "medium")
M("prj02", PROJ, "[Project topic] Rinderpest, which arrived in Africa in the late 1880s, was:", [("a cattle disease that killed about 90% of Africa's cattle", ""), ("a type of silk", "It was a cattle plague."), ("a European treaty", "It was a disease."), ("a crop from America", "It was a disease.")], "It destroyed African livelihoods and forced people into wage labour.", "medium")
M("prj03", PROJ, "[Project topic] Indian indentured workers were taken mainly to:", [("the Caribbean islands, Mauritius and Fiji", ""), ("Germany and France", "They went to plantations in colonies."), ("China and Japan", "They went to plantation colonies."), ("Peru and Mexico", "These were Spanish silver-mining areas.")], "Trinidad, Guyana and Surinam in the Caribbean, Mauritius, Fiji, Ceylon and Malaya.", "medium")
M("prj04", PROJ, "[Project topic] In which year was Indian indentured migration abolished?", [("1921", ""), ("1815", "1815 is the start of the 19th-century world economy period."), ("1947", "It was abolished much earlier."), ("1885", "1885 was the Berlin conference.")], "1921.", "medium")
M("prj05", PROJ, "[Project topic] The Great Depression began around:", [("1929", ""), ("1919", "1919 was just after the First World War."), ("1944", "1944 was the Bretton Woods conference."), ("1885", "1885 was the Berlin conference.")], "Around 1929, lasting till the mid-1930s.", "medium")
M("prj06", PROJ, "[Project topic] The Bretton Woods conference of 1944 set up:", [("the IMF and the World Bank", ""), ("the League of Nations", "That was set up after the First World War."), ("the silk routes", "The silk routes were ancient."), ("the WTO in 1944", "The WTO came in 1995.")], "The IMF and the International Bank for Reconstruction and Development (World Bank).", "medium")
# ---------------- Assertion-reason ----------------
C.arq("ar1", SILK, "The silk routes were an example of vibrant pre-modern trade and cultural links.", "Goods as well as religions like Buddhism travelled along them.", 0,
      "R explains A: both trade and culture moved along the routes.", "they linked distant parts of the world.", "goods and religions travelled together.")
C.arq("ar2", FOOD, "Chillies and tomatoes were known in India before Columbus reached the Americas.", "Many common foods came to Asia from the Americas after Columbus.", 3,
      "A is false: they came from the Americas after Columbus. R is true.", "they arrived only after Columbus.", "foods like chillies and tomatoes came from America.")
C.arq("ar3", CONQ, "Smallpox helped the Spanish conquer America.", "America's original inhabitants had no immunity to it.", 0,
      "R explains A: without immunity, whole communities died.", "the disease spread ahead of the conquerors.", "lack of immunity made smallpox deadly.")
C.arq("ar4", CONQ, "Europe emerged as the centre of world trade after the sixteenth century.", "China expanded its overseas contacts from the fifteenth century.", 2,
      "A is true; R is false: China restricted its overseas contacts.", "trade moved westwards.", "China retreated into isolation.")
C.arq("ar5", FOOD, "The failure of the potato crop in the 1840s caused mass starvation in Ireland.", "Ireland's poorest peasants had become heavily dependent on potatoes.", 0,
      "R explains A.", "hundreds of thousands died of starvation.", "dependence on one crop made the failure deadly.")
C.arq("ar6", CONQ, "Silver from America financed Europe's trade with Asia.", "Gold and silver flowed from Asia to Europe on the silk routes.", 2,
      "A is true; R is false: precious metals flowed from Europe to Asia.", "silver from Peru and Mexico enriched Europe.", "precious metals flowed from Europe to Asia.")
# ---------------- True / false ----------------
C.tf("tf1", SILK, "Gold and silver flowed from Europe to Asia along the silk routes.", True, "Asia sold silk, pottery and spices, and was paid in precious metals.")
C.tf("tf2", FOOD, "Potatoes are native to India.", False, "Potatoes came from the Americas after Columbus.")
C.tf("tf3", CONQ, "The Spanish conquered America only through superior firepower.", False, "Their most powerful weapon was germs such as smallpox.")
C.tf("tf4", CONQ, "China restricted overseas contacts from the fifteenth century.", True, "This, together with the rise of the Americas, moved the centre of trade to Europe.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", SILK, "Name two goods that travelled west and one that travelled east along the silk routes.",
  ["West: Chinese silk and pottery (also textiles and spices from India and Southeast Asia).", "East: precious metals, gold and silver, from Europe to Asia."], difficulty="easy")
W("vsa2", "very_short_answer", CONQ, "What was El Dorado, and why did Europeans search for it?",
  ["El Dorado was the fabled city of gold believed to be in South America.", "Legends of South America's fabled wealth, spread in 17th-century Europe after silver was found in Peru and Mexico, sent many expeditions in search of it."])
W("vsa3", "very_short_answer", CONQ, "Give two reasons why thousands fled Europe for America before the nineteenth century.",
  ["Poverty and hunger were common, cities were crowded and deadly diseases were widespread.", "Religious conflicts were common, and religious dissenters were persecuted."])
W("sa1", "short_answer", FOOD, "'Food offers many examples of long-distance cultural exchange.' Explain with three examples.",
  ["Noodles are believed to have travelled west from China to become spaghetti; perhaps Arab traders took pasta to fifth-century Sicily.",
   "Potatoes, soya, groundnuts, maize, tomatoes, chillies and sweet potatoes came to Europe and Asia from the American Indians after Columbus reached the Americas.",
   "The potato helped Europe's poor eat better and live longer, while Ireland's dependence on it led to famine in the mid-1840s."])
W("sa2", "short_answer", CONQ, "Why did the centre of world trade shift westwards to Europe?",
  ["Until well into the 18th century China and India were among the richest countries and dominated Asian trade.",
   "From the 15th century China restricted overseas contacts and retreated into isolation, reducing its role.",
   "Meanwhile the Americas grew in importance as a source of silver, crops and plantation produce, so trade moved westwards and Europe became its centre."])
W("la1", "long_answer", SILK, "Describe the silk routes and their importance in the pre-modern world.",
  ["The silk routes were land and sea routes, named after west-bound Chinese silk, that linked vast regions of Asia with Europe and northern Africa.",
   "They existed since before the Christian Era and thrived almost till the 15th century.",
   "Chinese pottery, textiles and spices from India and Southeast Asia travelled west, while gold and silver flowed from Europe to Asia.",
   "Christian missionaries and later Muslim preachers travelled along them, and Buddhism spread from eastern India in several directions.",
   "They show that trade and cultural exchange went hand in hand, connecting distant peoples long before modern times."])
# ---------------- Case and source based ----------------
W("cb1", "case_based", CONQ, "Read the source and answer the questions.\n\n*\"The Portuguese and Spanish conquest and colonisation of America was decisively under way by the mid-sixteenth century. European conquest was not just a result of superior firepower. In fact, the most powerful weapon of the Spanish conquerors was not a conventional military weapon at all. It was the germs such as those of smallpox that they carried on their person.\"* (NCERT)\n\n"
  "(i) Which two European powers colonised America? (1)\n\n(ii) What was the most powerful weapon of the Spanish conquerors? (1)\n\n(iii) Why did this 'weapon' work so well? (2)",
  ["(i) Portugal and Spain.", "(ii) Germs such as those of smallpox.",
   "(iii) America's original inhabitants had been isolated for millions of years and had no immunity; smallpox spread deep into the continent, ahead of the Europeans, killing whole communities, and unlike guns it could not be bought or captured."])
W("cb2", "case_based", FOOD, "Read the source and answer the questions.\n\n*\"Many of our common foods such as potatoes, soya, groundnuts, maize, tomatoes, chillies, sweet potatoes, and so on were not known to our ancestors until about five centuries ago. These foods were only introduced in Europe and Asia after Christopher Columbus accidentally discovered the vast continent that would later become known as the Americas.\"* (NCERT)\n\n"
  "(i) Name two foods mentioned that came from the Americas. (1)\n\n(ii) Who were the original inhabitants of the Americas from whom these foods came? (1)\n\n(iii) How could a new crop make the difference between life and death? Give one example each way. (2)",
  ["(i) Any two: potatoes, soya, groundnuts, maize, tomatoes, chillies, sweet potatoes.", "(ii) The American Indians.",
   "(iii) Life: the potato let Europe's poor eat better and live longer. Death: Ireland's poor depended so much on potatoes that when disease destroyed the crop in the mid-1840s, hundreds of thousands starved."])
W("cb3", "case_based", SILK, "Read the source and answer the questions.\n\n*\"The silk routes are a good example of vibrant pre-modern trade and cultural links between distant parts of the world. The name 'silk routes' points to the importance of west-bound Chinese silk cargoes along this route. Historians have identified several silk routes, over land and by sea, knitting together vast regions of Asia, and linking Asia with Europe and northern Africa.\"* (NCERT)\n\n"
  "(i) Why were these routes called silk routes? (1)\n\n(ii) Which regions did the silk routes link? (1)\n\n(iii) How were the silk routes also routes of culture? (2)",
  ["(i) Because of the importance of west-bound Chinese silk cargoes along them.", "(ii) Vast regions of Asia, and Asia with Europe and northern Africa.",
   "(iii) Christian missionaries and later Muslim preachers travelled them to Asia, and Buddhism spread from eastern India in several directions through the routes."])

chapter = header(SUBJ, N, "The Making of a Global World", ["silk_routes", "food_travels", "conquest_disease_trade", "project_19th_20th_century"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: only subtopics 1 to 1.3 (the pre-modern world; silk routes; food travels; conquest, disease and trade) are evaluated in the board examination. "
  "Subtopics 2 to 4.4 (the nineteenth century, 1815-1914, to the end of Bretton Woods) are an interdisciplinary project assessed internally; they are summarised in section 5 and their practice items are marked [Project topic].")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
