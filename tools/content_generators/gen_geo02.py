"""CBSE Class 10 Geography Ch 2: Forest and Wildlife Resources (fully in the 2025-26 board syllabus; no map item)."""
import sys
from ss_common import make, header, path, SQP, SHINE, CB

ROOT = sys.argv[1]
SUBJ, N = "geography", 2
PATH = path(SUBJ, "ch02_forest_and_wildlife_resources")
C = make(SUBJ, N, "geo10ch02")
blk, M, W = C.blk, C.m, C.w
BIO, CAT, LOSS, CONS, COMM = ["biodiversity"], ["species_categories"], ["depletion_causes"], ["conservation_policy"], ["community_conservation"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 2 exercises", "question": n}

IUCN = ("| Category (IUCN) | Meaning | Examples |\n|---|---|---|\n| **Normal species** | population considered normal for survival | cattle, sal, pine, rodents |\n"
        "| **Endangered** | in danger of extinction if negative factors continue | black buck, crocodile, Indian wild ass, Indian rhino, lion-tailed macaque, sangai (brow antler deer, Manipur) |\n"
        "| **Vulnerable** | population has declined to levels where it is likely to become endangered soon | blue sheep, Asiatic elephant, Gangetic dolphin |\n"
        "| **Rare** | small population; may become endangered or vulnerable | Himalayan brown bear, wild Asiatic buffalo, desert fox, hornbill |\n"
        "| **Endemic** | found only in particular areas, usually isolated by natural barriers | Andaman teal, Nicobar pigeon, Andaman wild pig, mithun (Arunachal Pradesh) |\n"
        "| **Extinct** | not found after searches of known or likely areas | Asiatic cheetah, pink head duck |")
FORESTS = ("| Type | Share of forest land | Notes |\n|---|---|---|\n| **Reserved forests** | more than half | most valuable for conservation; large shares in J&K, Andhra Pradesh, Uttarakhand, Kerala, Tamil Nadu, West Bengal, Maharashtra |\n"
           "| **Protected forests** | about one-third | protected from further depletion; bulk of forests in Bihar, Haryana, Punjab, Himachal Pradesh, Odisha, Rajasthan |\n"
           "| **Unclassed forests** | the rest | other forests and wastelands owned by government, private individuals and communities; high share in the north-eastern states and parts of Gujarat, managed by local communities |")
TIMELINE = ("| Year | Event |\n|---|---|\n| 1952 | Asiatic cheetah declared extinct in India |\n| 1951–1980 | over 26,200 sq km of forest converted to farmland |\n| 1972 | Indian Wildlife (Protection) Act |\n"
            "| 1973 | Project Tiger launched |\n| 1970s | Chipko movement in the Himalayas |\n| 1980 and 1986 | insects (butterflies, moths, beetles, a dragonfly) added to the protected list |\n"
            "| 1988 | Joint Forest Management: Odisha passes the first resolution |\n| 1991 | plants added to the protected list, starting with six species |")

sections = [
 {"id": "s1", "title": "Living together", "blocks": [
  blk("s1.hook", "hook", title="Who gives us the medicine for cancer?",
    body="High in the forests of Himachal Pradesh and Arunachal Pradesh grows a slow, quiet tree: the **Himalayan yew**. From its bark, needles, twigs and roots, scientists extract a chemical called **taxol**, used in one of the world's most widely sold anti-cancer drugs.\n\n"
         "But because so much was stripped from it, thousands of yew trees have dried up. One tree, one forest, one species can matter to millions of people. This chapter asks: why are India's forests and wildlife disappearing, and who is saving them?"),
  blk("s1.inspiration", "inspiration", title="Hug the trees", person="Gaura Devi", years="1925–1991",
    body="In March **1974**, contractors came to cut trees near Reni village in the Garhwal Himalayas while the men were away. **Gaura Devi** led the village women into the forest and hugged the trees, refusing to move.\n\n"
         "The loggers left. Her act became a symbol of the **Chipko movement**, which showed that ordinary villagers, especially women, could protect forests better than any law alone.",
    future="This chapter leads to careers in forestry, wildlife biology, conservation, ecotourism and environmental law."),
  C.socratic("s1.socratic", "Why should we care if a species of insect or grass disappears?",
    ["Every species is part of an ecosystem on which all life, including ours, depends", "Only large animals matter", "It makes no difference to humans"], 0,
    "Plants, animals and micro-organisms recreate the air we breathe, the water we drink and the soil that produces our food; each species has a role."),
 ]},
 {"id": "s2", "title": "Biodiversity in India", "blocks": [
  blk("s2.thm", "theory", title="Flora, fauna and the threat to them", revision=True,
    body="We share this planet with millions of other living beings, from micro-organisms and bacteria to lichens and banyan trees, and from elephants to blue whales. This whole habitat has immense **biodiversity**. Humans and other living organisms form a complex web of an **ecological system** of which we are only a part. "
         "Plants, animals and micro-organisms re-create the quality of the air we breathe, the water we drink and the soil that produces our food. Forests play a key role as **primary producers** on which all other living beings depend.\n\n"
         "**Flora and fauna in India:** India is one of the world's richest countries in biological diversity, with nearly **8 per cent** of the total number of species in the world (estimated at **1.6 million**). This is possibly twice or thrice the number yet to be discovered. "
         "But much of this diversity is under great threat, mainly due to our insensitivity to the environment. **At least 10 per cent** of India's recorded wild flora and **20 per cent** of its mammals are on the **threatened** list. Many would now be categorised as **'critical'**, on the verge of extinction, such as the cheetah, pink-headed duck, mountain quail, forest spotted owlet, and plants like *Madhuca insignis* (a wild variety of mahua) and *Hubbardia heptaneuron* (a species of grass).\n\n"
         "**Vanishing forests:** the forest and tree cover in the country is estimated at **80.9 million hectares**, which is **24.62 per cent** of the total geographical area (forest cover 21.71% + tree cover 2.91%, State of Forest Report 2021). "
         "This remains below the 33 per cent recommended by the National Forest Policy.\n\n"
         "**Categories of species (International Union for Conservation of Nature, IUCN):** normal, endangered, vulnerable, rare, endemic and extinct (see the table). The **Asiatic cheetah**, the world's fastest land mammal, was declared **extinct in India in 1952**. Its last population was in Iran."),
  blk("s2.table", "markdown_table", title="IUCN categories of species", revision=True, body=IUCN),
  C.kc("s2.check", "About what share of the world's species is found in India?",
    [("Nearly 8 per cent", ""), ("About 33 per cent", "33 per cent is the forest target."), ("About 24.62 per cent", "That is India's forest and tree cover."), ("About 1 per cent", "India is far richer than that.")],
    "India has nearly 8 per cent of the world's estimated 1.6 million species."),
  C.kc("s2.check2", "The Andaman teal and Nicobar pigeon are found only in particular areas. Which category are they in?",
    [("Endemic", ""), ("Extinct", "They still exist."), ("Normal", "Their range is very limited."), ("Vulnerable", "Vulnerable species are declining, like the Asiatic elephant.")],
    "Endemic species are found only in particular areas, usually isolated by natural barriers."),
 ]},
 {"id": "s3", "title": "Why flora and fauna are disappearing", "blocks": [
  blk("s3.thm", "theory", title="The causes of depletion", revision=True,
    body="**Colonial period:** the greatest damage to Indian forests came during colonial rule, due to the expansion of the **railways, agriculture, commercial and scientific forestry, and mining**.\n\n"
         "**Agricultural expansion:** even after Independence it remains a major cause. According to the Forest Survey of India, between **1951 and 1980**, over **26,200 sq km** of forest area was converted into agricultural land. Large parts of tribal belts, especially in the north-eastern and central India, have been deforested or degraded by **shifting cultivation (jhumming)**, a type of 'slash and burn' agriculture.\n\n"
         "**Enrichment plantations:** in many parts of India, large areas of natural forest were cleared for single commercial species (**monoculture**), such as **teak in South India** and **chir pine in the Himalayas**. This destroyed other species.\n\n"
         "**Large-scale development projects:** since **1951**, over **5,000 sq km** of forest was cleared for **river valley projects**. Clearing continues with projects like the **Narmada Sagar Project** in Madhya Pradesh, which would inundate **40,000 hectares** of forest.\n\n"
         "**Mining:** the **Buxa Tiger Reserve** in West Bengal is seriously threatened by ongoing **dolomite mining**, which has disturbed the natural habitat of many species and blocked the migration route of the great Indian elephant.\n\n"
         "**Other causes:** **grazing and fuel wood collection** (often blamed, though the larger causes are those above), **habitat destruction, hunting, poaching, over-exploitation, environmental pollution, poisoning and forest fires**. "
         "**Unequal access, inequitable consumption** and differential sharing of responsibility for environmental well-being also matter: the richest people consume far more resources.\n\n"
         "**Effects:** loss of forests and wildlife is linked to the **loss of cultural diversity**. Many indigenous communities depend on forests for food, drink, medicine, culture and spirituality. "
         "Among the poor, **women** are affected more than men: they collect fuel, fodder, water and other basic needs, so as these deplete, their drudgery increases and they walk long distances, causing health problems and neglect of home and children. "
         "Deforestation also leads to severe **droughts and floods**, which further hit the poor."),
  C.kc("s3.check", "Which mining activity threatens the Buxa Tiger Reserve?",
    [("Dolomite mining", ""), ("Coal mining", "The chapter names dolomite."), ("Iron ore mining", "The chapter names dolomite."), ("Bauxite mining", "The chapter names dolomite.")],
    "Dolomite mining in West Bengal has disturbed habitats and blocked the elephant's migration route."),
  C.kc("s3.check2", "Chir pine plantations in the Himalayas are an example of:",
    [("Enrichment plantations of a single commercial species", ""), ("Shifting cultivation", "Shifting cultivation is slash-and-burn farming."), ("Sacred groves", "Sacred groves are protected for religious reasons."), ("Joint Forest Management", "JFM involves communities in restoring degraded forests.")],
    "Monoculture plantations (teak in South India, chir pine in the Himalayas) destroy other species."),
 ]},
 {"id": "s4", "title": "Conservation by the state", "blocks": [
  blk("s4.thm", "theory", title="Laws, projects and types of forests", revision=True,
    body="Conservation preserves the **ecological diversity** and our life support systems: **water, air and soil**. It also preserves the **genetic diversity** of plants and animals for better growth of species and breeding; in agriculture we still depend on traditional crop varieties, and fisheries depend heavily on aquatic biodiversity.\n\n"
         "**Indian Wildlife (Protection) Act, 1972:** in the 1960s and 1970s conservationists demanded a national wildlife protection programme. The Act was implemented with various provisions for protecting habitats:\n"
         "- an all-India list of **protected species** was published;\n- **hunting was banned**, giving legal protection to their habitats, and **trade in wildlife** was restricted;\n"
         "- central and many state governments established **national parks and wildlife sanctuaries**;\n"
         "- the central government announced projects for protecting specific animals: the **tiger, the one-horned rhinoceros, the Kashmir stag (hangul), three types of crocodiles (freshwater crocodile, saltwater crocodile and the gharial), the Asiatic lion** and others;\n"
         "- the **Indian elephant, black buck (chinkara), the great Indian bustard (godawan) and the snow leopard** were given full or partial legal protection against hunting and trade.\n\n"
         "Conservation projects now focus on **biodiversity** rather than a few components. In **1980 and 1986**, several hundred **butterflies, moths, beetles and one dragonfly** were added to the protected list. In **1991**, for the first time, **plants** were added, starting with **six species**.\n\n"
         "**Project Tiger (1973):** tigers are a key wildlife species. Their population had dwindled from an estimated **55,000** at the turn of the 20th century to **1,827 in 1973**. Threats included poaching for trade, shrinking habitat, depletion of prey species and growing human population. "
         "Tiger reserves include **Corbett** National Park (Uttarakhand), **Sunderbans** (West Bengal), **Bandhavgarh** (Madhya Pradesh), **Sariska** (Rajasthan), **Manas** (Assam) and **Periyar** (Kerala). Project Tiger is not only about saving an endangered species but about preserving **biotypes of sizeable magnitude**.\n\n"
         "**Types and distribution of forests:** in India, much of the forest and wildlife is owned or managed by the government through the **Forest Department** and other departments. Forests are classified as:\n"
         "1. **Reserved forests:** more than **half** of the total forest land; regarded as the **most valuable** for the conservation of forest and wildlife resources.\n"
         "2. **Protected forests:** almost **one-third** of the total forest area; protected from any further depletion.\n"
         "3. **Unclassed forests:** other forests and wastelands belonging to both **government and private individuals and communities**.\n\n"
         "Reserved and protected forests are also called **permanent forest estates**, maintained for timber, other forest produce and protection. **Madhya Pradesh** has the **largest area under permanent forests**, about **75 per cent** of its total forest area. "
         "**Jammu and Kashmir, Andhra Pradesh, Uttarakhand, Kerala, Tamil Nadu, West Bengal and Maharashtra** have large percentages of reserved forests, while **Bihar, Haryana, Punjab, Himachal Pradesh, Odisha and Rajasthan** have a bulk of protected forests. "
         "All **north-eastern states and parts of Gujarat** have a very high percentage of **unclassed forests managed by local communities**."),
  blk("s4.forests", "markdown_table", title="Reserved, protected and unclassed forests", revision=True, body=FORESTS),
  blk("s4.timeline", "markdown_table", title="Timeline of conservation", revision=True, body=TIMELINE),
  C.kc("s4.check", "Which state has the largest area under permanent forests?",
    [("Madhya Pradesh", ""), ("Kerala", "Kerala has a large share of reserved forests, but MP has the largest permanent forest area."), ("Rajasthan", "Rajasthan has mostly protected forests."), ("Arunachal Pradesh", "North-eastern states have mostly unclassed forests.")],
    "Permanent forests make up about 75 per cent of Madhya Pradesh's forest area."),
  C.kc("s4.check2", "In which year was Project Tiger launched?",
    [("1973", ""), ("1972", "1972 is the Wildlife (Protection) Act."), ("1988", "1988 is Joint Forest Management."), ("1952", "1952 is when the cheetah was declared extinct in India.")],
    "Tiger numbers had fallen to 1,827 by 1973."),
 ]},
 {"id": "s5", "title": "Community and conservation", "blocks": [
  blk("s5.thm", "theory", title="People who protect forests", revision=True,
    body="Conservation strategies are not new: in India, forests are also **home to traditional communities**, who have worked with the state to protect their habitats.\n\n"
         "- **Sariska Tiger Reserve, Rajasthan:** villagers have fought against **mining** by citing the **Wildlife Protection Act**.\n"
         "- **Alwar district, Rajasthan:** inhabitants of **5 villages** have declared **1,200 hectares** of forest as the **Bhairodev Dakav 'Sonchuri'**, with their own rules that **do not allow hunting** and protect the wildlife against outside encroachment.\n"
         "- **Chipko movement** in the Himalayas: successfully resisted deforestation in several areas and showed that community afforestation with indigenous species can be very successful.\n"
         "- **Beej Bachao Andolan** in **Tehri** and **Navdanya**: farmers and citizens' groups have shown that adequate levels of diversified crop production **without synthetic chemicals** are possible and economically viable.\n\n"
         "**Joint Forest Management (JFM):** a good example of involving local communities in the management and restoration of **degraded forests**. It has existed formally since **1988**, when **Odisha** passed the **first resolution**. "
         "JFM depends on forming **local (village) institutions** that undertake protection activities mostly on degraded forest land managed by the Forest Department. In return, members are entitled to **intermediary benefits like non-timber forest produce** and a **share in the timber** harvested by successful protection.\n\n"
         "**Sacred groves (nature worship):** nature worship is an age-old tribal belief that all creations of nature have to be protected. Such beliefs have preserved several virgin forests in pristine form, called **sacred groves** (forests of God and Goddesses), where no one may touch the trees.\n"
         "- The **Mundas and the Santhals** of Chota Nagpur worship **mahua** (*Bassia latifolia*) and **kadamba** (*Anthocephalus cadamba*) trees; the tribals of Odisha and Bihar worship **tamarind** (*Tamarindus indica*) and **mango** (*Mangifera indica*) trees during weddings.\n"
         "- Many of us consider **peepal and banyan** trees sacred.\n"
         "- Indian society has many cultures, each with its own traditional methods of conserving nature. Springs, mountain peaks, plants and animals are considered sacred and protected. Troops of **macaques and langurs** are found around many temples, fed by devotees.\n"
         "- In and around **Bishnoi villages in Rajasthan**, herds of **blackbuck (chinkara), nilgai and peacocks** can be seen as an integral part of the community, and nobody harms them."),
  C.kc("s5.check", "Which state passed the first resolution for Joint Forest Management, in 1988?",
    [("Odisha", ""), ("Rajasthan", "Rajasthan is known for the Alwar sonchuri and Bishnoi villages."), ("Uttarakhand", "The Chipko movement began in the Himalayas."), ("Madhya Pradesh", "MP has the largest permanent forest area.")],
    "Odisha passed the first JFM resolution in 1988."),
  C.kc("s5.check2", "What is the Bhairodev Dakav 'Sonchuri'?",
    [("1,200 hectares of forest declared protected by five villages of Alwar district", ""), ("A national park in Madhya Pradesh", "It is a community-protected forest in Rajasthan."),
     ("A tiger reserve in West Bengal", "That would be Buxa or Sunderbans."), ("A seed-saving movement", "That is Beej Bachao Andolan.")],
    "The villagers made their own rules banning hunting."),
 ]},
 {"id": "s6", "title": "Remember, avoid, practise", "blocks": [
  blk("s6.memory", "memory_trick", title="Memory tricks",
    body="- **IUCN six: \"No Endangered Vulture Remains Ever Extinct\"** = Normal, Endangered, Vulnerable, Rare, Endemic, Extinct.\n- **Numbers: 8% species, 24.62% forest and tree cover, 26,200 sq km to farms (1951–80), 5,000 sq km to dams.**\n"
         "- **Forest shares: \"Reserved > half, Protected ≈ third, Unclassed = rest\".**\n- **Dates: 1972 Act → 1973 Tiger → 1988 JFM (Odisha) → 1991 plants protected.**\n"
         "- **Endemic = \"islands\":** Andaman teal, Nicobar pigeon, Andaman wild pig, plus mithun in Arunachal."),
  blk("s6.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Calling the Asiatic elephant 'endangered': in the chapter it is **vulnerable**; the Indian rhino and black buck are **endangered**.\n2. Saying unclassed forests belong only to the government: they belong to **government, private individuals and communities**.\n"
         "3. Mixing up the **Wildlife Act (1972)** and **Project Tiger (1973)**.\n4. Saying Madhya Pradesh has the most unclassed forest: it has the **largest permanent forest** area.\n"
         "5. Blaming only grazing and fuelwood for depletion: agricultural expansion, development projects, mining and monoculture plantations are major causes.\n6. Saying JFM gives forests to communities: the Forest Department still manages the land; communities protect it and **share benefits**."),
  blk("s6.tip", "teacher_tip", title="Try this in class",
    body="Give each group one IUCN category and ask them to make a 'missing poster' for a species in it, with where it lives and why it is in danger. "
         "Then run a mock village meeting: one side wants a mine near the forest, the other wants a sonchuri like Alwar. Each side must use facts from the chapter."),
  blk("s6.reflection", "reflection", title="Think and explain",
    body="Women in poor rural families are hurt more than men when forests disappear. Explain why, and suggest one way your community could reduce this burden."),
  blk("s6.connection", "connection", title="Where this leads",
    body="- **Chapter 1:** land degradation and soil erosion are linked to deforestation.\n- **Chapter 3 (Water Resources):** large dams submerge forests; the Narmada project.\n"
         "- **Chapter 5 (Minerals):** mining in forest areas like Buxa and Sariska.\n- **Political Science:** movements like Chipko show the power of popular struggles."),
  blk("s6.mastery", "mastery", title="Mastery challenge",
    body="'Conservation of forests and wildlife cannot succeed without local communities.' Do you agree? Answer in about 120 words.\n\n"
         "**Model answer:** Yes. Government laws like the Wildlife (Protection) Act, 1972 and Project Tiger (1973) created protected areas, but laws alone cannot watch every tree. "
         "Communities live in and around forests and depend on them, so they have the strongest reason to protect them. In Sariska, villagers fought mining using the Wildlife Act; in Alwar, five villages declared 1,200 hectares as the Bhairodev Dakav Sonchuri and banned hunting; the Chipko movement stopped tree felling in the Himalayas. "
         "Joint Forest Management since 1988 gives villagers a share in forest produce for protecting degraded forests. Sacred groves and Bishnoi traditions show conservation built into culture. So the best results come when the state and communities work together."),
  blk("s6.summary", "summary", title="Chapter summary",
    body="- India has nearly 8 per cent of the world's species, but at least 10% of its wild flora and 20% of its mammals are threatened.\n"
         "- IUCN categories: normal, endangered, vulnerable, rare, endemic, extinct (the Asiatic cheetah was declared extinct in India in 1952).\n"
         "- Causes of depletion: colonial railways and forestry, agricultural expansion, shifting cultivation, monoculture plantations, dams, mining, grazing, poaching, pollution and fires.\n"
         "- The state: Wildlife (Protection) Act 1972, Project Tiger 1973, national parks and sanctuaries; reserved, protected and unclassed forests.\n"
         "- Communities: Sariska, Alwar's sonchuri, Chipko, Beej Bachao Andolan, Joint Forest Management (Odisha, 1988), sacred groves and Bishnoi villages."),
  blk("s6.examtips", "exam_tips", title="Board exam tips",
    body="- The 2025-26 sample paper asked about an indirect consequence of poaching on tigers (fewer prey species) and about forest types in J&K, Andhra Pradesh and Kerala (mostly reserved or protected forests).\n"
         "- 3/5-mark favourites: causes of depletion, the Wildlife Act 1972, types of forests, community conservation, JFM, why biodiversity matters.\n"
         "- There is no map item from this chapter in 2025-26."),
  blk("s6.flash1", "flashcard", front="What does IUCN call a species found only in particular areas?", back="Endemic, e.g. the Andaman teal and Nicobar pigeon."),
  blk("s6.flash2", "flashcard", front="What is Joint Forest Management?", back="Since 1988 (first in Odisha), village institutions protect degraded forests and share forest produce and timber."),
  blk("s6.flash3", "flashcard", front="What are permanent forest estates?", back="Reserved and protected forests, kept for timber, forest produce and protection."),
  blk("s6.flash4", "flashcard", front="What was Project Tiger?", back="A 1973 project to save tigers, whose numbers had fallen to 1,827; reserves include Corbett, Sunderbans, Sariska and Manas."),
 ]},
]

# ---------------- Sample paper ----------------
M("sqp12", LOSS, "A total of 628 tigers died in India during the past five years due to natural causes and other reasons, including poaching, according to government data. Meanwhile, 349 people were killed in tiger attacks during this period, with one state alone recording 200 deaths. Which of the following is the most significant indirect consequence of poaching on the tiger population?",
  [("Reduction in the prey species, dwindling tiger's food supply.", ""), ("Increase in human-wildlife conflicts in protected areas", "Conflict is a related issue, but the official answer is the loss of prey species."),
   ("Rise in the tiger population.", "Poaching reduces, not raises, numbers."), ("Decrease in tourism revenue in national parks", "That is an economic effect on people, not on the tiger population.")],
  "Poaching of animals depletes the prey base, so tigers lose their food supply (CBSE marking scheme: A).", "hard", SQP(12), correct=0)
M("sqp13", CONS, "Based on the classification of forests, which of the following statements would most likely apply to places like Jammu and Kashmir, Andhra Pradesh, and Kerala etc.?",
  [("These places mostly have forests managed as reserved or protected forests for conservation.", ""),
   ("They rely on unclassed forests and local community management for forest conservation.", "That describes the north-eastern states and parts of Gujarat."),
   ("They have forest resources and primarily focus on industrial development.", "The classification is about conservation, not industry."),
   ("There are no classified forests and forest management is entirely left to private ownership.", "These states have large reserved forests.")],
  "J&K, Andhra Pradesh, Uttarakhand, Kerala, Tamil Nadu, West Bengal and Maharashtra have large percentages of reserved forests.", "medium", SQP(13), correct=0)

# ---------------- NCERT exercises ----------------
M("ex1i", LOSS, "Which of these statements is not a valid reason for the depletion of flora and fauna?",
  [("Agricultural expansion", "This is a major cause: 26,200 sq km converted between 1951 and 1980."), ("Large scale developmental projects", "Dams and projects cleared over 5,000 sq km."),
   ("Grazing and fuel wood collection", ""), ("Rapid industrialisation and urbanisation", "These also destroy habitats.")],
  "The textbook argues grazing and fuel wood collection are not the main causes; the larger damage comes from agriculture, development projects, mining and plantations.", "medium", ex("1(i)"), correct=2)
M("ex1ii", COMM, "Which of the following conservation strategies do not directly involve community participation?",
  [("Joint forest management", "JFM is based on village institutions."), ("Beej Bachao Andolan", "This is a farmers' movement."), ("Chipko Movement", "Villagers hugged trees."), ("Demarcation of Wildlife sanctuaries", "")],
  "Wildlife sanctuaries are demarcated by the government.", "easy", ex("1(ii)"), correct=3)
W("ex3i", "short_answer", BIO, "What is biodiversity? Why is biodiversity important for human lives?",
  ["Biodiversity is the variety of life forms, plants, animals and micro-organisms, that live in a habitat and are interdependent.",
   "Plants, animals and micro-organisms recreate the quality of the air we breathe, the water we drink and the soil that produces our food.",
   "Forests are primary producers; biodiversity gives us food, medicine (like taxol from the Himalayan yew), timber and genetic diversity for crops and fisheries, and keeps the ecosystem balanced."], source=ex("3(i)"))
W("ex3ii", "short_answer", LOSS, "How have human activities affected the depletion of flora and fauna? Explain.",
  ["Colonial railways, agriculture, commercial forestry and mining destroyed forests; between 1951 and 1980 over 26,200 sq km of forest was converted to farmland.",
   "Monoculture plantations (teak, chir pine), river valley projects (over 5,000 sq km cleared since 1951) and mining (dolomite in Buxa) destroyed habitats.",
   "Hunting, poaching, over-exploitation, pollution and forest fires have pushed many species to the threatened list."], source=ex("3(ii)"))
W("ex4i", "long_answer", COMM, "Describe how communities have conserved and protected forests and wildlife in India.",
  ["In Sariska Tiger Reserve, Rajasthan, villagers fought against mining by citing the Wildlife Protection Act.",
   "In Alwar district, five villages declared 1,200 hectares as the Bhairodev Dakav 'Sonchuri', with their own rules banning hunting and keeping out encroachers.",
   "The Chipko movement in the Himalayas resisted deforestation and showed the success of community afforestation with indigenous species.",
   "Through Joint Forest Management (from 1988, first in Odisha), village institutions protect degraded forests and share non-timber produce and timber.",
   "Sacred groves, worship of trees like mahua, kadamba, peepal and banyan, and Bishnoi villages protecting blackbuck, nilgai and peacocks preserve nature through tradition."], source=ex("4(i)"))
W("ex4ii", "long_answer", CONS, "Write a note on good practices towards conserving forest and wildlife.",
  ["The Indian Wildlife (Protection) Act, 1972 banned hunting, restricted wildlife trade and set up national parks and sanctuaries.",
   "Special projects protect the tiger (Project Tiger, 1973), one-horned rhino, Kashmir stag, three types of crocodiles and the Asiatic lion; insects (1980, 1986) and plants (1991) were added to the protected list.",
   "Joint Forest Management involves villagers in restoring degraded forests in return for a share of produce.",
   "Beej Bachao Andolan and Navdanya show diversified farming without synthetic chemicals is possible.",
   "Community efforts like Chipko, the Alwar sonchuri and sacred groves protect forests; conservation now focuses on whole biodiversity rather than a few species."], source=ex("4(ii)"))

# ---------------- MCQs ----------------
M("mcq01", BIO, "India's share of the world's estimated 1.6 million species is nearly:",
  [("8 per cent", ""), ("20 per cent", "20 per cent of India's mammals are threatened."), ("33 per cent", "33 per cent is the forest target."), ("2 per cent", "India is much richer.")], "India is one of the world's most biodiverse countries.")
M("mcq02", BIO, "What share of India's mammals are on the threatened list?",
  [("20 per cent", ""), ("10 per cent", "10 per cent refers to wild flora."), ("50 per cent", "The figure is 20 per cent."), ("8 per cent", "8 per cent is India's share of world species.")], "At least 10% of wild flora and 20% of mammals are threatened.")
M("mcq03", BIO, "Forests play a key role in the ecological system because they are:",
  [("primary producers on which all other living beings depend", ""), ("consumers of oxygen", "Forests produce oxygen."), ("only a source of timber", "They do much more."), ("not connected to soil or water", "They protect soil and water.")], "Forests are primary producers.")
M("mcq04", BIO, "India's forest and tree cover (State of Forest Report 2021) is about:",
  [("24.62 per cent of the geographical area", ""), ("33 per cent", "33 per cent is the recommended target."), ("43 per cent", "43 per cent of India is plains."), ("8 per cent", "8 per cent is India's share of world species.")],
  "80.9 million hectares: forest cover 21.71% + tree cover 2.91%.")
M("mcq05", CAT, "Species whose population is considered normal for survival, like cattle, sal and pine, are:",
  [("normal species", ""), ("rare species", "Rare species have small populations."), ("endemic species", "Endemic species live only in particular areas."), ("vulnerable species", "Vulnerable species are declining.")], "These are normal species.")
M("mcq06", CAT, "The black buck, Indian rhino and lion-tailed macaque are:",
  [("endangered", ""), ("extinct", "They still survive."), ("normal", "They are in danger."), ("endemic", "They are classed as endangered.")], "They are in danger of extinction.")
M("mcq07", CAT, "The blue sheep, Asiatic elephant and Gangetic dolphin are:",
  [("vulnerable", ""), ("extinct", "They still survive."), ("rare", "The Himalayan brown bear is an example of rare."), ("normal", "Their numbers are falling.")], "Their populations have declined to levels where they may soon become endangered.")
M("mcq08", CAT, "The Himalayan brown bear, desert fox and hornbill are:",
  [("rare", ""), ("endemic", "Endemic examples are the Andaman teal and Nicobar pigeon."), ("extinct", "They still survive."), ("vulnerable", "Vulnerable examples are the blue sheep and Asiatic elephant.")], "Rare species have small populations.")
M("mcq09", CAT, "Which animal is endemic to Arunachal Pradesh?",
  [("Mithun", ""), ("Sangai", "The sangai is an endangered deer of Manipur."), ("Hangul", "The hangul is the Kashmir stag."), ("Nilgai", "Nilgai are common in Rajasthan.")], "The mithun is endemic to Arunachal Pradesh.")
M("mcq10", CAT, "Which of these is extinct?",
  [("Pink head duck", ""), ("Gangetic dolphin", "It is vulnerable."), ("Hornbill", "It is rare."), ("Andaman teal", "It is endemic.")], "The Asiatic cheetah and pink head duck are extinct.")
M("mcq11", CAT, "The Asiatic cheetah was declared extinct in India in:",
  [("1952", ""), ("1972", "1972 is the Wildlife Act."), ("1973", "1973 is Project Tiger."), ("1988", "1988 is JFM.")], "The world's fastest land mammal vanished from India.")
M("mcq12", CAT, "The 'sangai', an endangered deer, is found in:",
  [("Manipur", ""), ("Kashmir", "The Kashmir stag is the hangul."), ("Rajasthan", "Rajasthan has blackbuck and nilgai."), ("Kerala", "The lion-tailed macaque lives in the Western Ghats.")], "The brow antler deer of Manipur.")
M("mcq13", LOSS, "The greatest damage to Indian forests happened during the colonial period because of:",
  [("expansion of railways, agriculture, commercial forestry and mining", ""), ("Project Tiger", "That protected tigers."), ("Joint Forest Management", "JFM began in 1988 to restore forests."), ("sacred groves", "Sacred groves protected forests.")], "Railways needed timber; agriculture and mining cleared forests.")
M("mcq14", LOSS, "Between 1951 and 1980, how much forest area was converted into agricultural land?",
  [("Over 26,200 sq km", ""), ("Over 5,000 sq km", "That was cleared for river valley projects."), ("40,000 hectares", "That is the Narmada Sagar submergence."), ("1,200 hectares", "That is the Alwar sonchuri.")], "According to the Forest Survey of India.")
M("mcq15", LOSS, "'Slash and burn' agriculture that has degraded forests in the north-east is called:",
  [("shifting cultivation (jhumming)", ""), ("terrace cultivation", "Terracing conserves soil."), ("strip cropping", "Strip cropping conserves soil."), ("plantation farming", "Plantations are permanent estates.")], "It has deforested large tribal belts.")
M("mcq16", LOSS, "Teak monoculture in South India is an example of:",
  [("enrichment plantation", ""), ("sacred grove", "A sacred grove is untouched forest."), ("unclassed forest", "That is a forest category by ownership."), ("joint forest management", "JFM restores degraded forests with villagers.")], "Single commercial species replaced natural forests.")
M("mcq17", LOSS, "Which project in Madhya Pradesh would inundate 40,000 hectares of forest?",
  [("Narmada Sagar Project", ""), ("Bhakra Nangal", "That is in Punjab and Himachal."), ("Hirakud", "That is in Odisha."), ("Tehri Dam", "That is in Uttarakhand.")], "Development projects keep clearing forests.")
M("mcq18", LOSS, "The Buxa Tiger Reserve is located in:",
  [("West Bengal", ""), ("Assam", "Manas is in Assam."), ("Rajasthan", "Sariska is in Rajasthan."), ("Kerala", "Periyar is in Kerala.")], "It is threatened by dolomite mining.")
M("mcq19", LOSS, "Which plant gives taxol, used in an anti-cancer drug?",
  [("Himalayan yew", ""), ("Mahua", "Mahua is worshipped by the Mundas and Santhals."), ("Chir pine", "Chir pine is a plantation species."), ("Teak", "Teak is valued for timber.")], "Thousands of yew trees have dried up from over-exploitation.")
M("mcq20", LOSS, "Why are poor women most affected by the depletion of forests?",
  [("They collect fuel, fodder and water and must walk longer distances", ""), ("They own most forests", "They do not."), ("They work in mines", "The chapter stresses collection work."), ("They live in cities", "The chapter refers to rural women.")],
  "Their drudgery increases, causing health problems and neglect of home and children.")
M("mcq21", CONS, "The Indian Wildlife (Protection) Act was passed in:",
  [("1972", ""), ("1973", "1973 is Project Tiger."), ("1988", "1988 is JFM."), ("1991", "In 1991 plants were added to the protected list.")], "It banned hunting and set up protected areas.")
M("mcq22", CONS, "Which is NOT a provision of the Wildlife (Protection) Act, 1972?",
  [("Giving forests to private companies for mining", ""), ("Publishing a list of protected species", "This is a provision."), ("Banning hunting", "This is a provision."), ("Setting up national parks and sanctuaries", "This is a provision.")], "The Act protects habitats.")
M("mcq23", CONS, "The hangul, protected under a special project, is the:",
  [("Kashmir stag", ""), ("Indian rhino", "The rhino is one-horned."), ("great Indian bustard", "That bird is the godawan."), ("snow leopard", "It lives in the high Himalayas.")], "The hangul is the Kashmir stag.")
M("mcq24", CONS, "Which three crocodiles are protected under special projects?",
  [("Freshwater crocodile, saltwater crocodile and the gharial", ""), ("Alligator, caiman and gharial", "Alligators and caimans are not Indian."), ("Only the gharial", "Three types are protected."), ("Nile crocodile and gharial", "The Nile crocodile is African.")], "All three Indian crocodiles.")
M("mcq25", CONS, "The great Indian bustard is also known as:",
  [("godawan", ""), ("chinkara", "Chinkara refers to the black buck in the chapter."), ("mithun", "Mithun is endemic to Arunachal."), ("sangai", "Sangai is a deer in Manipur.")], "It got legal protection against hunting.")
M("mcq26", CONS, "In which year were plants first added to the protected list?",
  [("1991", ""), ("1980", "In 1980 insects were added."), ("1972", "1972 is the Wildlife Act."), ("1986", "In 1986 more insects were added.")], "Starting with six species.")
M("mcq27", CONS, "In 1973 the tiger population of India was:",
  [("1,827", ""), ("55,000", "That was the estimate at the turn of the century."), ("628", "628 tigers died in five years (sample paper)."), ("8,000", "The figure was 1,827.")], "This led to Project Tiger.")
M("mcq28", CONS, "Which is NOT a tiger reserve?",
  [("Bhairodev Dakav Sonchuri", ""), ("Corbett", "Corbett in Uttarakhand is a tiger reserve."), ("Sunderbans", "Sunderbans in West Bengal is a tiger reserve."), ("Bandhavgarh", "Bandhavgarh in Madhya Pradesh is a tiger reserve.")], "The sonchuri is a community forest in Alwar.")
M("mcq29", CONS, "Manas Tiger Reserve is in:",
  [("Assam", ""), ("Kerala", "Periyar is in Kerala."), ("West Bengal", "Buxa and Sunderbans are in West Bengal."), ("Uttarakhand", "Corbett is in Uttarakhand.")], "Manas is in Assam.")
M("mcq30", CONS, "Reserved forests make up:",
  [("more than half of the total forest land", ""), ("about one-third", "That is protected forests."), ("less than 10 per cent", "They are the largest category."), ("all forest land", "There are three types.")], "They are the most valuable for conservation.")
M("mcq31", CONS, "Forests and wastelands owned by government, private individuals and communities are:",
  [("unclassed forests", ""), ("reserved forests", "Reserved forests are state-managed."), ("protected forests", "Protected forests are state-managed."), ("sacred groves", "Sacred groves are community religious forests.")], "Unclassed forests.")
M("mcq32", CONS, "Reserved and protected forests together are called:",
  [("permanent forest estates", ""), ("sacred groves", "Sacred groves are community forests."), ("unclassed forests", "That is the third category."), ("tiger reserves", "Tiger reserves are a separate category.")], "They are maintained for timber, produce and protection.")
M("mcq33", CONS, "Where is a very high percentage of forests unclassed and managed by local communities?",
  [("North-eastern states and parts of Gujarat", ""), ("Madhya Pradesh", "MP has the largest permanent forests."), ("Punjab and Haryana", "These have mostly protected forests."), ("Kerala and Tamil Nadu", "These have large reserved forests.")], "Local communities manage them.")
M("mcq34", COMM, "Villagers in Sariska fought against mining by citing:",
  [("the Wildlife Protection Act", ""), ("Agenda 21", "That is an international agenda."), ("the Vernacular Press Act", "That is a History topic."), ("the Forest Survey of India", "That is a survey body.")], "Communities used the law to protect forests.")
M("mcq35", COMM, "Beej Bachao Andolan began in:",
  [("Tehri", ""), ("Alwar", "Alwar has the Bhairodev Dakav sonchuri."), ("Odisha", "Odisha began JFM."), ("Sariska", "Sariska villagers fought mining.")], "It promotes diversified farming without synthetic chemicals.")
M("mcq36", COMM, "Under JFM, members of village institutions get:",
  [("non-timber forest produce and a share in timber", ""), ("ownership of the forest land", "The land stays with the Forest Department."), ("hunting rights", "Hunting is banned."), ("mining licences", "JFM is about protection.")], "Benefits come from successful protection.")
M("mcq37", COMM, "The Mundas and Santhals of Chota Nagpur worship:",
  [("mahua and kadamba trees", ""), ("tamarind and mango trees", "Tribals of Odisha and Bihar worship these during weddings."), ("teak and sal", "These are timber species."), ("chir pine", "Chir pine is a plantation species.")], "Nature worship preserves sacred groves.")
M("mcq38", COMM, "Around Bishnoi villages in Rajasthan, which animals are protected by the community?",
  [("Blackbuck, nilgai and peacocks", ""), ("Tigers and elephants", "These are not named for Bishnoi villages."), ("Macaques and langurs", "These live around temples."), ("Gharials", "Gharials are river crocodiles.")], "They are an integral part of the community.")

# ---------------- True / false ----------------
C.tf("tf1", CAT, "The Asiatic elephant is a vulnerable species.", True, "Its population has declined to levels where it is likely to become endangered.")
C.tf("tf2", CONS, "Protected forests make up more than half of India's forest land.", False, "Reserved forests are more than half; protected forests are about one-third.")
C.tf("tf3", COMM, "Joint Forest Management began formally in Odisha in 1988.", True, "Odisha passed the first resolution.")
C.tf("tf4", LOSS, "Grazing and fuel wood collection are the main causes of forest depletion in India.", False, "Agricultural expansion, development projects, mining and plantations are bigger causes.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", CAT, "Distinguish between endangered and endemic species, with one example each.",
  ["Endangered species are in danger of extinction if the negative factors continue, e.g. the black buck or Indian rhino.", "Endemic species are found only in particular areas, usually isolated by natural barriers, e.g. the Andaman teal or Nicobar pigeon."])
W("vsa2", "very_short_answer", LOSS, "Why is the Himalayan yew in trouble?",
  ["Taxol, extracted from its bark, needles, twigs and roots, is used in a widely sold anti-cancer drug.", "Over-exploitation has dried up thousands of yew trees in Himachal Pradesh and Arunachal Pradesh."])
W("vsa3", "very_short_answer", COMM, "What are sacred groves?",
  ["Virgin forests preserved in pristine form because of the tribal belief that all creations of nature must be protected.", "They are 'forests of God and Goddesses', where no one is allowed to touch the trees."])
W("sa1", "short_answer", CONS, "Describe the three types of forests in India.",
  ["Reserved forests: more than half of the forest land, the most valuable for conservation.", "Protected forests: about one-third of the forest area, protected from further depletion.",
   "Unclassed forests: other forests and wastelands belonging to government, private individuals and communities."])
W("sa2", "short_answer", BIO, "How does the loss of forests and wildlife affect people?",
  ["It causes a loss of cultural diversity, since many indigenous communities depend on forests for food, medicine, culture and spirituality.",
   "Women, who collect fuel, fodder and water, must walk longer distances, leading to health problems and neglect of home and children.",
   "Deforestation leads to droughts and floods, which hurt the poor most."])
W("sa3", "short_answer", CONS, "What were the main features of Project Tiger?",
  ["It was launched in 1973 when tiger numbers had fallen from about 55,000 to 1,827.", "It aimed to protect tigers from poaching, loss of habitat and depletion of prey.",
   "Tiger reserves like Corbett, Sunderbans, Bandhavgarh, Sariska, Manas and Periyar were set up; it preserves whole biotypes, not just one species."])
W("la1", "long_answer", LOSS, "Explain the major causes of the depletion of forests and wildlife in India.",
  ["Colonial expansion of railways, agriculture, commercial and scientific forestry, and mining caused the greatest damage.",
   "Agricultural expansion converted over 26,200 sq km of forest between 1951 and 1980; shifting cultivation degraded tribal belts.",
   "Enrichment plantations of single species like teak and chir pine replaced natural forests.",
   "Development projects (over 5,000 sq km for river valley projects; Narmada Sagar would drown 40,000 ha) and mining (dolomite in Buxa) destroyed habitats.",
   "Hunting, poaching, over-exploitation, pollution, poisoning, forest fires, and unequal consumption by the rich add to the damage."])
W("cb1", "case_based", COMM, "Read the source and answer the questions.\n\n*\"In India joint forest management (JFM) programme furnishes a good example for involving local communities in the management and restoration of degraded forests. The programme has been in formal existence since 1988 when the state of Odisha passed the first resolution for joint forest management.\"* (NCERT)\n\n"
  "(i) Which state passed the first resolution for JFM? (1)\n\n(ii) What kind of forest land does JFM mostly work on? (1)\n\n(iii) How do local communities benefit from JFM, and why does this help conservation? (2)",
  ["(i) Odisha, in 1988.", "(ii) Degraded forest land managed by the Forest Department.",
   "(iii) Members get intermediary benefits like non-timber forest produce and a share in the timber harvested; since they gain from healthy forests, they protect them."])
W("cb2", "case_based", CAT, "Read the source and answer the questions.\n\n*\"The Asiatic cheetah, the world's fastest land mammal, was a unique and specialised member of the cat family and could move at the speed of 112 km/hr. It was declared extinct in India in 1952.\"* (NCERT)\n\n"
  "(i) In which IUCN category is the Asiatic cheetah placed for India? (1)\n\n(ii) In which year was it declared extinct in India? (1)\n\n(iii) Name two other IUCN categories with one example each. (2)",
  ["(i) Extinct.", "(ii) 1952.", "(iii) Endangered: black buck or Indian rhino; vulnerable: Asiatic elephant or Gangetic dolphin (any two categories with examples)."])
# ---------------- Assertion-reason ----------------
C.arq("ar1", LOSS, "The Buxa Tiger Reserve is seriously threatened.", "Ongoing dolomite mining has disturbed the habitat and blocked the migration route of the great Indian elephant.", 0,
      "R explains A.", "it is in West Bengal.", "mining destroys habitat.")
C.arq("ar2", CONS, "Madhya Pradesh has the largest area under permanent forests.", "Unclassed forests are managed by local communities in the north-east.", 1,
      "Both are true, but R is about the north-east and does not explain A.", "about 75 per cent of MP's forest is permanent.", "the north-east has unclassed forests.")
C.arq("ar3", CAT, "The Gangetic dolphin is an endemic species.", "Vulnerable species have populations declining towards the endangered level.", 3,
      "A is false: the Gangetic dolphin is vulnerable. R is true.", "it is listed as vulnerable.", "this defines vulnerable.")
C.arq("ar4", COMM, "Joint Forest Management helps restore degraded forests.", "Village institutions protect the forest in return for a share of its produce.", 0,
      "R explains A.", "it began in 1988.", "benefit-sharing motivates protection.")
C.arq("ar5", LOSS, "Enrichment plantations harm biodiversity.", "A single commercial species replaces many natural species.", 0,
      "R explains A.", "teak and chir pine are examples.", "monoculture destroys other species.")
C.arq("ar6", CONS, "Project Tiger aims only to save one species.", "Tiger reserves preserve whole biotypes of sizeable magnitude.", 3,
      "A is false: Project Tiger preserves whole biotypes, not only tigers. R is true.", "it protects ecosystems too.", "reserves cover large biotypes.")

chapter = header(SUBJ, N, "Forest and Wildlife Resources", ["biodiversity", "species_categories", "depletion_causes", "conservation_policy", "community_conservation"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: this chapter is fully in the board examination (Geography: 17 marks + 3 map marks). There is no map item from this chapter.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
