"""CBSE Class 10 Geography Ch 3: Water Resources (fully in the 2025-26 board syllabus; map: dams)."""
import sys
from ss_common import make, header, path, SQP, SHINE, CB

ROOT = sys.argv[1]
SUBJ, N = "geography", 3
PATH = path(SUBJ, "ch03_water_resources")
C = make(SUBJ, N, "geo10ch03")
blk, M, W = C.blk, C.m, C.w
SCAR, HIST, DAMS, HARV, MAP = ["water_scarcity"], ["ancient_hydraulics"], ["multipurpose_projects"], ["rainwater_harvesting"], ["dams_map"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 3 exercises", "question": n}

DAMLIST = ("| Dam | River | State |\n|---|---|---|\n| **Salal** | Chenab | Jammu and Kashmir |\n| **Bhakra Nangal** | Sutlej | Himachal Pradesh / Punjab |\n| **Tehri** | Bhagirathi | Uttarakhand |\n"
           "| **Rana Pratap Sagar** | Chambal | Rajasthan |\n| **Sardar Sarovar** | Narmada | Gujarat |\n| **Hirakud** | Mahanadi | Odisha |\n| **Nagarjuna Sagar** | Krishna | Telangana / Andhra Pradesh |\n| **Tungabhadra** | Tungabhadra | Karnataka |")
PROSCONS = ("| Benefits of multipurpose projects | Problems they cause |\n|---|---|\n| irrigation for agriculture | natural flow of rivers affected; poor sediment flow downstream |\n"
            "| hydroelectricity | excessive sedimentation at the reservoir bottom; rockier stream beds, poorer aquatic habitats |\n| water for homes and industries | rivers fragmented; aquatic fauna cannot migrate to spawn |\n"
            "| flood control | submerged vegetation and soil decompose; floods triggered by sedimentation and sudden releases |\n| recreation, inland navigation, fish breeding | displacement of local people; inter-state disputes; salinisation; widening gap between rich and poor |")
HARVEST = ("| Region | Traditional method |\n|---|---|\n| Western Himalayas (hills) | **guls or kuls**: diversion channels for agriculture |\n| Rajasthan (houses) | **rooftop rainwater harvesting** for drinking water |\n"
           "| Floodplains of Bengal | **inundation channels** to irrigate fields |\n| Arid Rajasthan (Jaisalmer and other parts) | **khadins** and **johads**: fields turned into rain-fed storage |\n"
           "| Bikaner, Phalodi, Barmer | **tankas**: underground tanks storing **palar pani** |\n| Meghalaya | **bamboo drip irrigation**, about 200 years old |")

sections = [
 {"id": "s1", "title": "Water everywhere, not a drop to drink?", "blocks": [
  blk("s1.hook", "hook", title="Why is a rainy city short of water?",
    body="Shillong in Meghalaya is only about **55 km** from Cherrapunji and Mawsynram, among the wettest places on Earth. Yet nearly every house in Shillong collects rain from its roof, because the city still runs short of water.\n\n"
         "Water is renewable, yet India faces scarcity. How can that be? This chapter explains why water becomes scarce, how big dams try to solve the problem and create new ones, and how people across India have harvested rain for centuries."),
  blk("s1.inspiration", "inspiration", title="The waterman of India", person="Rajendra Singh", years="born 1959",
    body="In the 1980s, Rajendra Singh began helping villagers in the dry Alwar district of Rajasthan to revive old **johads**, small earthen check dams that catch rainwater. Wells filled again, and rivers that had dried up, like the **Arvari**, began to flow.\n\n"
         "His organisation, Tarun Bharat Sangh, helped build thousands of johads. In 2015 he received the Stockholm Water Prize. His work shows that traditional wisdom can solve modern water problems.",
    future="This chapter leads to careers in hydrology, civil and water engineering, environmental planning and rural development."),
  C.socratic("s1.socratic", "Water is renewed by the water cycle. Why, then, does India face water scarcity?",
    ["Over-use and unequal access by a large population, plus pollution", "Because it never rains in India", "Because water is a non-renewable resource"], 0,
    "Scarcity is mostly caused by over-exploitation, excessive use and unequal access, not by a lack of rain alone."),
 ]},
 {"id": "s2", "title": "Water scarcity", "blocks": [
  blk("s2.thm", "theory", title="Why water becomes scarce", revision=True,
    body="Three-fourths of the Earth's surface is covered with water, but only a small proportion is **freshwater** that can be used. Freshwater comes mainly from **surface runoff and groundwater**, continually renewed and recharged through the **hydrological cycle**. "
         "About **96.5 per cent** of the world's water is in the oceans and only **2.5 per cent** is freshwater; nearly **70 per cent** of this freshwater is locked in ice sheets and glaciers, and a little less than **30 per cent** is stored as groundwater.\n\n"
         "Water is a renewable resource, but **water scarcity** can arise even in areas with plenty of rain or rivers. Its causes:\n"
         "- **Large and growing population:** more water for domestic use and more food grown.\n- **Irrigated agriculture:** to grow more food, water resources are over-exploited for irrigation and for **dry-season agriculture**.\n"
         "- **Over-use of groundwater:** many farmers have their own wells and tube-wells, which leads to falling groundwater levels.\n"
         "- **Industrialisation and urbanisation:** industries need water and also electricity, much of it from **hydroelectric power**; cities with large populations and urban lifestyles add to the demand, and housing societies often have their own groundwater pumps.\n"
         "- **Unequal access** among social groups.\n- **Poor quality of water:** even where water is available, it may be **polluted** by domestic and industrial wastes, chemicals, pesticides and fertilisers, making it unfit for use.\n\n"
         "So we need to **conserve and manage** water: to safeguard ourselves from health hazards, ensure food security, continue our livelihoods and productive activities, and prevent the degradation of natural ecosystems. Over-exploitation and mismanagement may impoverish this resource and cause ecological crisis."),
  C.kc("s2.check", "What share of the world's water is freshwater?",
    [("About 2.5 per cent", ""), ("About 96.5 per cent", "That is ocean water."), ("About 70 per cent", "70 per cent of freshwater is ice."), ("About 30 per cent", "Under 30 per cent of freshwater is groundwater.")],
    "Only about 2.5 per cent of the Earth's water is freshwater."),
  C.kc("s2.check2", "Which is NOT a cause of water scarcity in India?",
    [("Lack of any rainfall in the country", ""), ("Over-exploitation for irrigation", "This is a real cause."), ("Pollution of water", "This is a real cause."), ("Growing urban population", "This is a real cause.")],
    "Scarcity is caused by over-use, unequal access and pollution, even in areas that get rain."),
 ]},
 {"id": "s3", "title": "Dams: old and new", "blocks": [
  blk("s3.thm", "theory", title="Ancient hydraulic works and multipurpose projects", revision=True,
    body="**Hydraulic structures in ancient India:**\n- In the **1st century BC**, **Sringaverapura near Prayagraj (Allahabad)** had a sophisticated water harvesting system channelling the flood water of the **Ganga**.\n"
         "- During **Chandragupta Maurya's** time, dams, lakes and irrigation systems were extensively built.\n- Evidence of sophisticated irrigation works has been found in **Kalinga (Odisha), Nagarjunakonda (Andhra Pradesh), Bennur (Karnataka) and Kolhapur (Maharashtra)**.\n"
         "- In the **11th century**, **Bhopal Lake**, one of the largest artificial lakes of its time, was built.\n- In the **14th century**, the tank in **Hauz Khas, Delhi**, was constructed by **Iltutmish** to supply water to the **Siri Fort** area.\n\n"
         "**Dams:** a dam is a **barrier across flowing water** that obstructs, directs or retards the flow, often creating a **reservoir, lake or impoundment**. 'Dam' usually refers to the reservoir rather than the structure. Most dams have a section called a **spillway or weir** over which, or through which, water flows. "
         "Dams are classified by **structure and materials** (timber dams, embankment dams, masonry dams) and by **height** (large or major dams; low, medium and high dams).\n\n"
         "**Multipurpose river projects:** dams today are built not just for irrigation but for **electricity generation, water supply for domestic and industrial uses, flood control, recreation, inland navigation and fish breeding**. "
         "For example, in the **Sutlej-Beas** basin, the **Bhakra-Nangal** project water is used both for **hydel power and irrigation**; the **Hirakud** project in the **Mahanadi** basin integrates **conservation of water with flood control**. "
         "Jawaharlal Nehru proudly called dams the **'temples of modern India'**, because they would integrate agriculture, the village economy, rapid industrialisation and growth of the urban economy.\n\n"
         "**Why dams are opposed:**\n"
         "- Regulating and damming rivers affects their **natural flow**, causing **poor sediment flow** and **excessive sedimentation** at the bottom of the reservoir, resulting in **rockier stream beds** and poorer habitats for aquatic life.\n"
         "- Dams **fragment rivers**, making it difficult for aquatic fauna to migrate, especially for **spawning**.\n- Reservoirs on floodplains **submerge** the existing vegetation and soil, leading to their decomposition.\n"
         "- They caused **social movements** like the **Narmada Bachao Andolan** and the **Tehri Dam Andolan**, mainly due to the large-scale **displacement** of local communities, who often gave up their land and livelihood for the greater good of the nation.\n"
         "- **Inter-state water disputes:** the **Krishna-Godavari dispute** arose from objections by **Karnataka and Andhra Pradesh** to the diversion of more water at **Koyna** by **Maharashtra** for a multipurpose project, which would reduce downstream flow in their states.\n"
         "- Dams built to control floods have **triggered floods** due to sedimentation in the reservoir; big dams have often failed to control floods during excessive rainfall, and **release of water** from dams during heavy rain has worsened floods.\n"
         "- Irrigation changed the **cropping pattern** to water-intensive commercial crops, leading to **salinisation** of the soil; and it widened the **social gap** between rich landowners and the landless poor.\n"
         "- Other problems: earthquakes, water-borne diseases and pests, and pollution from excessive use of water."),
  blk("s3.proscons", "markdown_table", title="Multipurpose projects: benefits and problems", revision=True, body=PROSCONS),
  blk("s3.dams", "markdown_table", title="Dams to locate on the map (2025-26)", revision=True, body=DAMLIST),
  C.kc("s3.check", "Which project in the Mahanadi basin integrates conservation of water with flood control?",
    [("Hirakud", ""), ("Bhakra Nangal", "That is in the Sutlej-Beas basin, for hydel power and irrigation."), ("Sardar Sarovar", "That is on the Narmada."), ("Tehri", "That is on the Bhagirathi.")],
    "Hirakud, Odisha, on the Mahanadi."),
  C.kc("s3.check2", "Who built the tank in Hauz Khas, Delhi, in the 14th century?",
    [("Iltutmish", ""), ("Chandragupta Maurya", "His time saw dams and lakes, but not this tank."), ("Jawaharlal Nehru", "Nehru called dams temples of modern India."), ("Raja Bhoj", "The chapter credits Hauz Khas to Iltutmish.")],
    "Iltutmish built it to supply water to the Siri Fort area."),
 ]},
 {"id": "s4", "title": "Rainwater harvesting", "blocks": [
  blk("s4.thm", "theory", title="Traditional wisdom and modern revival", revision=True,
    body="Many thought that, given the disadvantages of multipurpose projects, **rainwater harvesting** is a viable alternative, both socio-economically and environmentally. In ancient India, people had in-depth knowledge of rainfall regimes and soil types and developed many techniques to harvest **rainwater, groundwater, river water and flood water**, keeping with local ecological conditions.\n\n"
         "- In **hill and mountainous regions**, people built diversion channels like the **'guls' or 'kuls'** of the **Western Himalayas** for agriculture.\n"
         "- **Rooftop rainwater harvesting** was commonly practised to store drinking water, particularly in **Rajasthan**.\n"
         "- In the **floodplains of Bengal**, people developed **inundation channels** to irrigate their fields.\n"
         "- In **arid and semi-arid regions**, agricultural fields were converted into rain-fed storage structures that allowed the water to stand and moisten the soil, like the **'khadins' in Jaisalmer** and **'johads'** in other parts of Rajasthan.\n\n"
         "**Tankas of Rajasthan:** in the semi-arid and arid regions of Rajasthan, particularly in **Bikaner, Phalodi and Barmer**, almost all houses traditionally had **underground tanks or 'tankas'** for storing drinking water. The tanks could be as large as a big room; one household in **Phalodi** had a tank **6.1 m deep, 4.27 m long and 2.44 m wide**. "
         "The tankas were part of a well-developed rooftop rainwater harvesting system, built inside the main house or the courtyard, and connected to the **sloping roofs** by a pipe. Rain falling on the roofs travelled down the pipe and was stored in the tanka. The **first spell of rain** was usually **not collected**, as it would clean the roofs and pipes. "
         "The rainwater stored in tankas is an extremely reliable source of drinking water when all other sources are dried up, and is considered the purest form of natural water, called **'palar pani'**. Many houses built underground rooms adjoining the tanka to beat the summer heat, since it kept the room **cool**. "
         "Today the practice is declining in western Rajasthan as perennial water from the **Indira Gandhi Canal** has become available, though some households still maintain tankas because they do not like the taste of tap water.\n\n"
         "**Modern revival:**\n"
         "- **Gendathur**, a remote village in **Mysuru, Karnataka**: villagers have installed rooftop rainwater harvesting in nearly **200 households**, and the village is known for being rich in rainwater.\n"
         "- **Shillong, Meghalaya**: though Cherrapunji and Mawsynram, about 55 km away, receive the highest rainfall in the world, the city faces acute water shortage; nearly every household has rooftop harvesting, meeting about **15-25 per cent** of its total water requirement.\n"
         "- **Tamil Nadu** is the **first state in India** to make **rooftop rainwater harvesting compulsory** for all houses across the state, with legal provisions to punish defaulters.\n"
         "- **Bamboo drip irrigation in Meghalaya:** a **200-year-old** system in which water from streams and springs is tapped by **bamboo pipes**. About **18-20 litres** of water enter the bamboo pipe system per minute and are carried over hundreds of metres, finally reduced to **20-80 drops per minute** at the site of the plant.\n"
         "- **Pradhan Mantri Krishi Sinchayee Yojana (2015):** a central scheme to extend irrigation to every farm ('**Har Khet Ko Pani**') and improve water-use efficiency ('**More crop per drop**') through better irrigation and water conservation."),
  blk("s4.table", "markdown_table", title="Traditional water harvesting across India", revision=True, body=HARVEST),
  C.kc("s4.check", "Which state first made rooftop rainwater harvesting compulsory for all houses?",
    [("Tamil Nadu", ""), ("Rajasthan", "Rajasthan has the traditional tankas."), ("Meghalaya", "Meghalaya has bamboo drip irrigation and Shillong's rooftop harvesting."), ("Karnataka", "Gendathur village is in Karnataka, but the law is Tamil Nadu's.")],
    "Tamil Nadu made it compulsory with penalties for defaulters (2025-26 sample paper)."),
  C.kc("s4.check2", "What is 'palar pani'?",
    [("Rainwater stored in tankas, considered the purest form of natural water", ""), ("Water from the Indira Gandhi Canal", "Canal water is replacing tankas."),
     ("Water from guls and kuls", "Those are Himalayan diversion channels."), ("Polluted river water", "Palar pani is pure.")],
    "Palar pani is stored in the underground tankas of Rajasthan."),
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **Water shares: \"96.5 sea, 2.5 sweet\"**; of the sweet water, 70% ice, under 30% groundwater.\n- **Two model projects: \"Bhakra = Bijli + Bhumi (power + irrigation); Hirakud = Holds floods\"**.\n"
         "- **Dams on the map, north to south: \"Sally Bought Ten Red Shirts, Her Nephew Took\"** = Salal, Bhakra Nangal, Tehri, Rana Pratap Sagar, Sardar Sarovar, Hirakud, Nagarjuna Sagar, Tungabhadra.\n"
         "- **Harvesting by region:** Himalaya = guls/kuls; Bengal = inundation channels; Rajasthan = khadins, johads, tankas; Meghalaya = bamboo drip.\n- **Tamil Nadu = first to make rooftop harvesting compulsory.**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying water scarcity happens only where there is no rain: it also comes from **over-use, unequal access and pollution**.\n2. Mixing up Bhakra Nangal (**Sutlej**, power and irrigation) and Hirakud (**Mahanadi**, flood control).\n"
         "3. Saying the first spell of rain is stored in tankas: it is **not collected**; it cleans the roofs and pipes.\n4. Placing Sardar Sarovar on the Mahanadi: it is on the **Narmada** in Gujarat.\n"
         "5. Saying Rajasthan made rooftop harvesting compulsory: it was **Tamil Nadu**.\n6. Saying the Krishna-Godavari dispute was about the Narmada: it was about **Maharashtra's diversion at Koyna**, opposed by Karnataka and Andhra Pradesh."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Measure the school roof area and the yearly rainfall of your town, and calculate how many litres the roof could harvest (area in sq m × rainfall in mm = litres). "
         "Then let students mark the eight dams on an outline map of India with their rivers."),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="Nehru called dams the 'temples of modern India', while people displaced by them protested. Write one argument for big dams and one for rainwater harvesting, and say which suits your region better."),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Chapter 1:** over-irrigation causes waterlogging and salinity.\n- **Chapter 2:** dams like Narmada Sagar submerge forests.\n"
         "- **Chapter 4 (Agriculture):** irrigation and cropping patterns.\n- **Chapter 5 (Energy):** hydroelectricity from multipurpose projects."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="'Multipurpose river projects are both a boon and a curse.' Explain in about 120 words.\n\n"
         "**Model answer:** Multipurpose projects like Bhakra Nangal and Hirakud provide irrigation, hydroelectricity, water for homes and industries, flood control, navigation, fish breeding and recreation, so Nehru called dams the temples of modern India. "
         "But they also block the natural flow of rivers, cause sedimentation and rockier stream beds, fragment rivers so fish cannot migrate to spawn, and submerge forests and soil. "
         "They displace local people, as protested by the Narmada Bachao Andolan, and cause inter-state disputes like the Krishna-Godavari one. Sometimes they even trigger floods through sedimentation and sudden releases, and water-intensive crops lead to salinisation. "
         "So we must weigh their benefits against their costs and combine them with rainwater harvesting."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Only about 2.5% of the world's water is freshwater; scarcity is caused by population, irrigation, groundwater over-use, industry, cities, unequal access and pollution.\n"
         "- India had ancient hydraulic structures: Sringaverapura (1st century BC), Bhopal Lake (11th century) and Hauz Khas tank (14th century, Iltutmish).\n"
         "- Multipurpose projects (Bhakra Nangal, Hirakud) serve many uses but cause ecological damage, displacement, disputes and floods.\n"
         "- Traditional rainwater harvesting: guls/kuls, rooftop harvesting, inundation channels, khadins, johads, tankas; bamboo drip irrigation in Meghalaya.\n"
         "- Modern efforts: Gendathur, Shillong, Tamil Nadu's compulsory rooftop harvesting and PMKSY (2015)."),
  blk("s5.examtips", "exam_tips", title="Board exam tips",
    body="- The 2025-26 sample paper asked which state made rooftop harvesting compulsory (Tamil Nadu), the goal of PMKSY (better irrigation and sustainable water conservation for farmers), and to locate Bhakra Nangal or Hirakud on the map.\n"
         "- 3/5-mark favourites: causes of water scarcity, benefits and problems of multipurpose projects, rainwater harvesting in Rajasthan and Meghalaya.\n"
         "- **Map work:** locate Salal, Bhakra Nangal, Tehri, Rana Pratap Sagar, Sardar Sarovar, Hirakud, Nagarjuna Sagar and Tungabhadra."),
  blk("s5.flash1", "flashcard", front="What are tankas?", back="Underground tanks in Rajasthan (Bikaner, Phalodi, Barmer) storing rooftop rainwater (palar pani)."),
  blk("s5.flash2", "flashcard", front="Name two uses each of Bhakra Nangal and Hirakud.", back="Bhakra Nangal: hydel power and irrigation. Hirakud: water conservation and flood control."),
  blk("s5.flash3", "flashcard", front="What did the Narmada Bachao Andolan oppose?", back="The Sardar Sarovar dam: first its environmental damage, later the poor rehabilitation of displaced people."),
  blk("s5.flash4", "flashcard", front="How does bamboo drip irrigation work?", back="Bamboo pipes carry 18-20 litres a minute from springs; it is reduced to 20-80 drops a minute at the plant."),
 ]},
]

# ---------------- Sample paper ----------------
M("sqp14", HARV, "Which one of the following states has made roof top water harvesting compulsory in India?",
  [("Haryana", "Haryana has not been named for this."), ("Punjab", "Punjab has not been named for this."), ("Assam", "Assam has not been named for this."), ("Tamil Nadu.", "")],
  "Tamil Nadu is the first state to make rooftop rainwater harvesting compulsory for all houses.", "easy", SQP(14), correct=3)
M("sqp15", HARV, "Which of the following statements best evaluates the overall goal of the Pradhan Mantri Krishi Sinchaee Yojana?",
  [("Addressing the negative ecological effects of large dams by reducing water usage.", "The scheme is about irrigation for farmers, not dams."),
   ("To provide better irrigation systems and sustainable water conservation practices for farmers.", ""),
   ("Shifting farmers from traditional crops to more commercial, water-intensive crops.", "It aims at efficient water use, not water-intensive crops."),
   ("Preserve the natural river flow and prevent the fragmentation of aquatic ecosystems.", "That is a criticism of dams, not the scheme's goal.")],
  "'Har Khet Ko Pani' and 'More crop per drop'.", "medium", SQP(15), correct=1)
M("sqp19p", MAP, "Map work (sample paper): the dam in the Sutlej-Beas river basin, which is used both for hydel power production and irrigation, is:",
  [("Bhakra Nangal", ""), ("Hirakud", "Hirakud is in the Mahanadi basin."), ("Tehri", "Tehri is on the Bhagirathi."), ("Salal", "Salal is on the Chenab.")],
  "Bhakra Nangal, on the Sutlej, in Himachal Pradesh and Punjab.", "easy", SQP(19), correct=0)
M("sqp19q", MAP, "Map work (sample paper): the dam in the Mahanadi basin that integrates conservation of water with flood control is:",
  [("Hirakud", ""), ("Nagarjuna Sagar", "That is on the Krishna."), ("Sardar Sarovar", "That is on the Narmada."), ("Rana Pratap Sagar", "That is on the Chambal.")],
  "Hirakud, in Odisha.", "easy", SQP(19), correct=0)

# ---------------- NCERT exercises ----------------
M("ex1ii", DAMS, "Which one of the following statements is not an argument in favour of multi-purpose river projects?",
  [("Multi-purpose projects bring water to those areas which suffer from water scarcity.", "This is an argument in favour."),
   ("Multi-purpose projects by regulating water flow helps to control floods.", "This is an argument in favour."),
   ("Multi-purpose projects lead to large scale displacements and loss of livelihood.", ""),
   ("Multi-purpose projects generate electricity for our industries and our homes.", "This is an argument in favour.")],
  "Displacement and loss of livelihood are arguments against such projects.", "easy", ex("1(ii)"), correct=2)
W("ex2i", "short_answer", HARV, "Explain how water becomes a renewable resource.",
  ["Water is continually renewed and recharged through the hydrological cycle: evaporation, condensation and precipitation.",
   "Rain refills rivers, lakes and ponds (surface runoff) and seeps into the ground to recharge groundwater.",
   "So the freshwater we use is replaced naturally, as long as we do not over-use or pollute it."], source=ex("2(i)"))
W("ex2ii", "short_answer", SCAR, "What is water scarcity and what are its main causes?",
  ["Water scarcity is the shortage of water to meet the needs of people, even in areas where water is available.",
   "Causes: a large and growing population needs more water for homes and food; over-exploitation for irrigation and groundwater use; industries and cities increase demand.",
   "Unequal access among social groups and pollution by domestic and industrial wastes, chemicals, pesticides and fertilisers also cause scarcity."], source=ex("2(ii)"))
W("ex2iii", "short_answer", DAMS, "Compare the advantages and disadvantages of multi-purpose river projects.",
  ["Advantages: irrigation, hydroelectricity, water for homes and industries, flood control, recreation, inland navigation and fish breeding.",
   "Disadvantages: they affect natural river flow, cause sedimentation, fragment rivers, submerge vegetation and soil, and displace local people.",
   "They also cause inter-state disputes, sometimes trigger floods, and lead to salinisation and a widening gap between rich and poor."], source=ex("2(iii)"))
W("ex3i", "long_answer", HARV, "Discuss how rainwater harvesting in semi-arid regions of Rajasthan is carried out.",
  ["In Bikaner, Phalodi and Barmer, almost all houses traditionally had underground tanks called tankas for storing drinking water.",
   "Tankas were part of a rooftop rainwater harvesting system, built in the main house or courtyard and connected to the sloping roofs by a pipe.",
   "Rain falling on the roof flowed down the pipe into the tanka; the first spell of rain was not collected, as it cleaned the roofs and pipes.",
   "The stored rainwater, palar pani, is the purest natural water and a reliable source when other sources dry up; tankas also kept adjoining rooms cool.",
   "Agricultural fields were also turned into rain-fed storage like khadins in Jaisalmer and johads; the practice is now declining as Indira Gandhi Canal water is available."], source=ex("3(i)"))
W("ex3ii", "long_answer", HARV, "Describe how modern adaptations of traditional rainwater harvesting methods are being carried out to conserve and store water.",
  ["Rooftop rainwater harvesting is being revived in cities and villages to store water and recharge groundwater.",
   "In Gendathur, Mysuru (Karnataka), about 200 households have installed rooftop harvesting, making the village rich in rainwater.",
   "In Shillong, Meghalaya, nearly every household harvests rooftop rain, meeting 15-25 per cent of its water needs.",
   "Tamil Nadu has made rooftop rainwater harvesting compulsory for all houses, with penalties for defaulters.",
   "Traditional johads have been revived in Rajasthan, and the bamboo drip irrigation of Meghalaya continues; schemes like PMKSY promote efficient irrigation."], source=ex("3(ii)"))

# ---------------- MCQs ----------------
M("mcq01", SCAR, "About what percentage of the world's water is in the oceans?",
  [("96.5 per cent", ""), ("2.5 per cent", "That is freshwater."), ("70 per cent", "70 per cent of freshwater is ice."), ("50 per cent", "Most water is in the oceans.")], "Only about 2.5 per cent is freshwater.")
M("mcq02", SCAR, "Most of the world's freshwater is found as:",
  [("ice sheets and glaciers", ""), ("rivers", "Rivers hold a tiny share."), ("lakes", "Lakes hold a small share."), ("water vapour", "The atmosphere holds very little.")], "Nearly 70 per cent of freshwater is ice.")
M("mcq03", SCAR, "Freshwater is continually renewed through the:",
  [("hydrological cycle", ""), ("carbon cycle", "That cycles carbon."), ("rock cycle", "That forms rocks."), ("nitrogen cycle", "That cycles nitrogen.")], "Evaporation, condensation and precipitation renew water.")
M("mcq04", SCAR, "Which is a cause of falling groundwater levels?",
  [("Many farmers using their own wells and tube-wells for irrigation", ""), ("Rooftop rainwater harvesting", "Harvesting recharges groundwater."), ("Afforestation", "Forests help recharge."), ("Johads", "Johads recharge groundwater.")], "Over-use of groundwater lowers water tables.")
M("mcq05", SCAR, "Why do industries increase pressure on water?",
  [("They use water and also need electricity, much of it from hydel power", ""), ("They produce rainfall", "They do not."), ("They reduce population", "They attract people to cities."), ("They clean rivers", "They often pollute rivers.")], "Industries are heavy users of water and energy.")
M("mcq06", SCAR, "Water may be available but unfit for use because of:",
  [("pollution by domestic and industrial wastes, chemicals and fertilisers", ""), ("too much rain", "Rain is not the problem here."), ("rooftop harvesting", "Harvesting stores clean water."), ("bamboo pipes", "Bamboo drip irrigation saves water.")], "Poor quality of water is a form of scarcity.")
M("mcq07", HIST, "In the 1st century BC, which place had a sophisticated system channelling the flood water of the Ganga?",
  [("Sringaverapura near Prayagraj", ""), ("Hauz Khas", "That was a 14th-century tank in Delhi."), ("Bhopal", "Bhopal Lake was built in the 11th century."), ("Bennur", "Bennur in Karnataka had irrigation works.")], "It is one of India's oldest known water harvesting systems.")
M("mcq08", HIST, "One of the largest artificial lakes of its time, built in the 11th century, was:",
  [("Bhopal Lake", ""), ("Hauz Khas tank", "That was built in the 14th century."), ("Dal Lake", "Dal Lake is natural."), ("Sardar Sarovar", "That is a modern dam.")], "Bhopal Lake.")
M("mcq09", HIST, "The tank in Hauz Khas, Delhi, supplied water to:",
  [("the Siri Fort area", ""), ("the Red Fort", "The chapter names Siri Fort."), ("Fatehpur Sikri", "That is near Agra."), ("Bhopal", "Bhopal had its own lake.")], "Built by Iltutmish in the 14th century.")
M("mcq10", HIST, "Extensive dams, lakes and irrigation systems were built during the time of:",
  [("Chandragupta Maurya", ""), ("Iltutmish", "He built the Hauz Khas tank."), ("Akbar", "The chapter names Chandragupta Maurya."), ("Ashoka only", "The chapter names Chandragupta Maurya.")], "Ancient India had sophisticated hydraulic engineering.")
M("mcq11", DAMS, "A dam is:",
  [("a barrier across flowing water that obstructs, directs or retards the flow", ""), ("a natural lake", "Dams are built structures."), ("an underground tank", "That is a tanka."), ("a canal", "A canal carries water away.")], "It often creates a reservoir.")
M("mcq12", DAMS, "The section of a dam over or through which water flows is called the:",
  [("spillway or weir", ""), ("reservoir", "The reservoir stores water."), ("tanka", "A tanka is a household tank."), ("kul", "A kul is a Himalayan channel.")], "Most dams have a spillway.")
M("mcq13", DAMS, "Who called dams the 'temples of modern India'?",
  [("Jawaharlal Nehru", ""), ("Mahatma Gandhi", "Gandhi warned against greed."), ("Medha Patkar", "She led the Narmada Bachao Andolan."), ("Iltutmish", "He built the Hauz Khas tank.")], "Dams would integrate agriculture, industry and urban growth.")
M("mcq14", DAMS, "Which is NOT a purpose of multipurpose river projects?",
  [("Increasing sedimentation downstream", ""), ("Irrigation", "This is a purpose."), ("Electricity generation", "This is a purpose."), ("Flood control", "This is a purpose.")], "Sedimentation is a problem, not a purpose.")
M("mcq15", DAMS, "Dams make it difficult for aquatic fauna to migrate because they:",
  [("fragment rivers", ""), ("increase the flow", "They reduce natural flow."), ("clean the water", "They do not."), ("raise the temperature", "The chapter names fragmentation.")], "Fish cannot reach spawning grounds.")
M("mcq16", DAMS, "The Narmada Bachao Andolan opposed:",
  [("the Sardar Sarovar dam", ""), ("the Bhakra Nangal dam", "That is on the Sutlej."), ("the Hirakud dam", "That is on the Mahanadi."), ("rooftop harvesting", "The movement opposed a big dam.")], "It raised environmental issues and the rehabilitation of displaced people.")
M("mcq17", DAMS, "The Krishna-Godavari dispute arose because of diversion of water at Koyna by:",
  [("Maharashtra", ""), ("Karnataka", "Karnataka objected."), ("Andhra Pradesh", "Andhra Pradesh objected."), ("Tamil Nadu", "Tamil Nadu was not part of this dispute.")], "Downstream states feared reduced flow.")
M("mcq18", DAMS, "How can dams built for flood control trigger floods?",
  [("Sedimentation in the reservoir and sudden release of water during heavy rain", ""), ("By reducing rainfall", "Dams do not change rainfall."), ("By recharging groundwater", "That does not cause floods."), ("By stopping irrigation", "That does not cause floods.")], "Big dams have often failed to control floods.")
M("mcq19", DAMS, "Irrigation from dams has led to salinisation of soil because:",
  [("cropping shifted to water-intensive commercial crops", ""), ("farmers stopped irrigating", "Over-irrigation is the issue."), ("forests increased", "Not related."), ("rainfall fell", "The issue is excess irrigation.")], "Water-intensive crops cause salinity.")
M("mcq20", DAMS, "Social effects of big dams include:",
  [("displacement of local people and a widening gap between rich and poor", ""), ("more land for the landless", "The rich gain most."), ("lower food production", "Not the main effect."), ("end of inter-state disputes", "They cause disputes.")], "Rich landowners benefit more than the landless.")
M("mcq21", HARV, "'Guls' or 'kuls' are:",
  [("diversion channels in the Western Himalayas", ""), ("underground tanks in Rajasthan", "Those are tankas."), ("inundation channels in Bengal", "Those are in the floodplains."), ("bamboo pipes in Meghalaya", "That is drip irrigation.")], "They carry water for agriculture.")
M("mcq22", HARV, "Inundation channels to irrigate fields were developed in:",
  [("the floodplains of Bengal", ""), ("Jaisalmer", "Jaisalmer has khadins."), ("the Western Himalayas", "There people used guls and kuls."), ("Meghalaya", "Meghalaya has bamboo drip irrigation.")], "Flood water was used for irrigation.")
M("mcq23", HARV, "'Khadins' are found in:",
  [("Jaisalmer", ""), ("Shillong", "Shillong uses rooftop harvesting."), ("Bengal", "Bengal has inundation channels."), ("Mysuru", "Gendathur is near Mysuru.")], "Fields are turned into rain-fed storage.")
M("mcq24", HARV, "Tankas were traditionally found in houses of:",
  [("Bikaner, Phalodi and Barmer", ""), ("Shillong and Cherrapunji", "These are in Meghalaya."), ("Kolkata and Howrah", "These are in Bengal."), ("Chennai and Madurai", "These are in Tamil Nadu.")], "Underground tanks stored drinking water.")
M("mcq25", HARV, "Why was the first spell of rain not collected in tankas?",
  [("It cleaned the roofs and pipes", ""), ("It was too little", "It was used for cleaning."), ("It was salty", "Rainwater is not salty."), ("It was used for crops", "It was let go to clean surfaces.")], "Only later rain was stored.")
M("mcq26", HARV, "Why is the practice of tankas declining in western Rajasthan?",
  [("Perennial water from the Indira Gandhi Canal is available", ""), ("It stopped raining", "Rain still falls."), ("Tankas were banned", "They were not."), ("Palar pani is impure", "Palar pani is the purest water.")], "Some households keep tankas as they dislike tap water's taste.")
M("mcq27", HARV, "Underground rooms built next to tankas were used to:",
  [("beat the summer heat", ""), ("store grain", "The chapter mentions cooling."), ("hide treasure", "Not mentioned."), ("keep cattle", "Not mentioned.")], "The tanka kept the room cool.")
M("mcq28", HARV, "In Gendathur village, Mysuru, about how many households installed rooftop harvesting?",
  [("200", ""), ("20", "The figure is about 200."), ("2,000", "The figure is about 200."), ("50", "The figure is about 200.")], "The village is known as rich in rainwater.")
M("mcq29", HARV, "Shillong faces water shortage even though nearby Cherrapunji and Mawsynram:",
  [("receive the highest rainfall in the world", ""), ("are deserts", "They are among the wettest places."), ("have no rivers", "Not the point."), ("use bamboo drip irrigation", "That is a different practice.")], "Rooftop harvesting meets 15-25 per cent of Shillong's household needs.")
M("mcq30", HARV, "Rooftop harvesting meets about what share of a Shillong household's water requirement?",
  [("15-25 per cent", ""), ("80 per cent", "The figure is 15-25 per cent."), ("2-5 per cent", "The figure is 15-25 per cent."), ("100 per cent", "It is a partial source.")], "Nearly every house in Shillong has rooftop harvesting.")
M("mcq31", HARV, "How old is the bamboo drip irrigation system of Meghalaya?",
  [("About 200 years", ""), ("About 20 years", "It is much older."), ("About 2,000 years", "It is about 200 years old."), ("About 50 years", "It is about 200 years old.")], "Water from streams and springs is tapped by bamboo pipes.")
M("mcq32", HARV, "In bamboo drip irrigation, water reaching the plant is reduced to:",
  [("20-80 drops per minute", ""), ("18-20 litres per minute", "That is the amount entering the pipes."), ("one litre per hour", "The chapter gives drops per minute."), ("a full stream", "It reaches as drops.")], "18-20 litres a minute enter the system at the source.")
M("mcq33", HARV, "The motto 'Har Khet Ko Pani' belongs to:",
  [("Pradhan Mantri Krishi Sinchayee Yojana", ""), ("Narmada Bachao Andolan", "That is a protest movement."), ("Project Tiger", "That is about tigers."), ("Agenda 21", "That is an international agenda.")], "PMKSY was launched in 2015.")
# ---------------- Map work (dams) ----------------
M("map1", MAP, "Map work: the Salal dam is on which river?",
  [("Chenab", ""), ("Sutlej", "Bhakra Nangal is on the Sutlej."), ("Bhagirathi", "Tehri is on the Bhagirathi."), ("Chambal", "Rana Pratap Sagar is on the Chambal.")], "Salal is in Jammu and Kashmir.", "medium")
M("map2", MAP, "Map work: the Tehri dam is located in:",
  [("Uttarakhand", ""), ("Himachal Pradesh", "Bhakra is in Himachal Pradesh."), ("Odisha", "Hirakud is in Odisha."), ("Gujarat", "Sardar Sarovar is in Gujarat.")], "Tehri is on the Bhagirathi.", "medium")
M("map3", MAP, "Map work: the Rana Pratap Sagar dam is on the:",
  [("Chambal, in Rajasthan", ""), ("Narmada, in Gujarat", "That is Sardar Sarovar."), ("Krishna, in Telangana", "That is Nagarjuna Sagar."), ("Mahanadi, in Odisha", "That is Hirakud.")], "Rana Pratap Sagar is in Rajasthan.", "medium")
M("map4", MAP, "Map work: the Nagarjuna Sagar dam is on the:",
  [("Krishna", ""), ("Godavari", "The chapter's dam on the Krishna is Nagarjuna Sagar."), ("Kaveri", "Not this dam."), ("Tungabhadra", "The Tungabhadra dam is in Karnataka.")], "It is on the Telangana–Andhra Pradesh border.", "medium")
W("map5", "very_short_answer", MAP, "Map work: name the states in which (a) the Sardar Sarovar dam and (b) the Tungabhadra dam are located.",
  ["(a) Gujarat (on the Narmada).", "(b) Karnataka (on the Tungabhadra)."])
# ---------------- True / false ----------------
C.tf("tf1", SCAR, "Water scarcity happens only in areas of low rainfall.", False, "It also comes from over-use, unequal access and pollution, even in high-rainfall areas.")
C.tf("tf2", DAMS, "The Hirakud project integrates conservation of water with flood control.", True, "Hirakud is in the Mahanadi basin.")
C.tf("tf3", HARV, "Tamil Nadu was the first state to make rooftop rainwater harvesting compulsory.", True, "It has legal provisions to punish defaulters.")
C.tf("tf4", HIST, "Bhopal Lake was built in the 14th century by Iltutmish.", False, "Bhopal Lake is 11th century; Iltutmish built the Hauz Khas tank in the 14th century.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", SCAR, "Why is it necessary to conserve water? Give two reasons.",
  ["To safeguard ourselves from health hazards and to ensure food security.", "To continue our livelihoods and productive activities and prevent the degradation of natural ecosystems."])
W("vsa2", "very_short_answer", DAMS, "Why did Nehru call dams the 'temples of modern India'?",
  ["He believed dams would integrate agriculture and the village economy.", "They would also support rapid industrialisation and the growth of the urban economy."])
W("vsa3", "very_short_answer", HARV, "Name two traditional rainwater harvesting methods and the regions where they are used.",
  ["Guls or kuls: diversion channels in the Western Himalayas.", "Khadins and johads: rain-fed storage fields in Rajasthan (also inundation channels in Bengal, tankas in Bikaner, Phalodi, Barmer)."])
W("sa1", "short_answer", DAMS, "Why have multipurpose projects faced resistance?",
  ["Large-scale displacement of local people, who lose land and livelihood, led to movements like the Narmada Bachao Andolan and the Tehri Dam Andolan.",
   "They damage ecosystems: affect river flow, cause sedimentation, fragment rivers and submerge vegetation and soil.",
   "They cause inter-state disputes, sometimes trigger floods, and benefit rich landowners more than the poor."])
W("sa2", "short_answer", HARV, "Describe the bamboo drip irrigation system of Meghalaya.",
  ["It is a 200-year-old system in which water from streams and springs is tapped using bamboo pipes.",
   "About 18-20 litres of water per minute enter the system and are carried over hundreds of metres.",
   "Smaller bamboo channels reduce the flow to 20-80 drops per minute at the site of the plant, saving water."])
W("la1", "long_answer", SCAR, "Explain the causes of water scarcity in India.",
  ["A large and growing population needs more water for domestic use and to produce more food.",
   "Over-exploitation for irrigation and dry-season agriculture, and over-use of groundwater by private wells and tube-wells, lower water tables.",
   "Industrialisation increases demand for water and for hydroelectric power; growing cities and urban lifestyles add to the demand.",
   "Unequal access to water among social groups leaves many without enough.",
   "Pollution by domestic and industrial wastes, chemicals, pesticides and fertilisers makes available water unfit for use."])
W("cb1", "case_based", HARV, "Read the source and answer the questions.\n\n*\"In the semi-arid and arid regions of Rajasthan, particularly in Bikaner, Phalodi and Barmer, almost all the houses traditionally had underground tanks or tankas for storing drinking water. The tanks could be as large as a big room; one household in Phalodi had a tank that was 6.1 metres deep, 4.27 metres long and 2.44 metres wide.\"* (NCERT)\n\n"
  "(i) What were tankas used for? (1)\n\n(ii) How were tankas connected to the rooftop? (1)\n\n(iii) Why was rainwater in tankas valued, and why is the practice declining? (2)",
  ["(i) Storing rainwater for drinking.", "(ii) By a pipe from the sloping roofs.",
   "(iii) It is palar pani, the purest form of natural water, and a reliable source when other sources dry up; the practice is declining because perennial Indira Gandhi Canal water is now available."])
W("cb2", "case_based", DAMS, "Read the source and answer the questions.\n\n*\"Regulating and damming of rivers affect their natural flow causing poor sediment flow and excessive sedimentation at the bottom of the reservoir, resulting in rockier stream beds and poorer habitats for the rivers' aquatic life.\"* (NCERT)\n\n"
  "(i) Name one multipurpose project used for hydel power and irrigation. (1)\n\n(ii) What happens to stream beds because of damming? (1)\n\n(iii) Give two other ecological problems caused by dams. (2)",
  ["(i) Bhakra Nangal (Sutlej-Beas basin).", "(ii) They become rockier.",
   "(iii) Dams fragment rivers so fish cannot migrate to spawn; reservoirs submerge vegetation and soil, which decompose (also triggered floods and salinisation)."])
# ---------------- Assertion-reason ----------------
C.arq("ar1", SCAR, "Water scarcity can occur even in areas with plenty of rainfall.", "Over-exploitation, unequal access and pollution reduce the water available for use.", 0,
      "R explains A.", "Shillong is an example.", "scarcity is not only about rain.")
C.arq("ar2", DAMS, "Dams fragment rivers.", "Aquatic fauna find it difficult to migrate for spawning.", 0,
      "R explains A: fragmentation blocks the migration of fish.", "dams cut a river into parts.", "fish cannot reach spawning grounds.")
C.arq("ar3", HARV, "The first spell of rain was stored in tankas.", "Rainwater in tankas is called palar pani.", 3,
      "A is false: the first rain was not collected, as it cleaned the roofs and pipes. R is true.", "the first rain cleaned surfaces.", "palar pani is the name for stored rainwater.")
C.arq("ar4", DAMS, "Big dams have sometimes triggered floods.", "Sedimentation in reservoirs and release of water during heavy rains worsen floods.", 0,
      "R explains A.", "they failed to control floods.", "sediment reduces capacity.")
C.arq("ar5", HARV, "Tamil Nadu made rooftop rainwater harvesting compulsory.", "Meghalaya practises bamboo drip irrigation.", 1,
      "Both are true, but R is about Meghalaya and does not explain A.", "it has penalties for defaulters.", "bamboo drip is about 200 years old.")
C.arq("ar6", DAMS, "Multipurpose projects have reduced the gap between rich and poor.", "Irrigation shifted cropping to water-intensive commercial crops.", 3,
      "A is false: they have widened the gap between rich landowners and the landless. R is true.", "the rich gained more.", "cropping patterns changed.")

chapter = header(SUBJ, N, "Water Resources", ["water_scarcity", "ancient_hydraulics", "multipurpose_projects", "rainwater_harvesting", "dams_map"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: this chapter is fully in the board examination (Geography: 17 marks + 3 map marks). Map work from this chapter: dams (Salal, Bhakra Nangal, Tehri, Rana Pratap Sagar, Sardar Sarovar, Hirakud, Nagarjuna Sagar, Tungabhadra). Map items are given here as text questions.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
