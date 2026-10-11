"""CBSE Class 10 Geography Ch 1: Resources and Development (fully in the 2025-26 board syllabus; map: major soil types)."""
import sys
from ss_common import make, header, path, SQP, SHINE, CB

ROOT = sys.argv[1]
SUBJ, N = "geography", 1
PATH = path(SUBJ, "ch01_resources_and_development")
C = make(SUBJ, N, "geo10ch01")
blk, M, W = C.blk, C.m, C.w
RES, DEV, LAND, SOIL, EROS = ["resource_types"], ["resource_planning"], ["land_resources"], ["soil_types"], ["soil_conservation"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 1 exercises", "question": n}

CLASSIFY = ("| Basis | Types | Examples |\n|---|---|---|\n| **Origin** | biotic (from the biosphere, have life) / abiotic (non-living) | human beings, flora, fauna, fisheries, livestock / rocks, metals |\n"
            "| **Exhaustibility** | renewable (replenishable) / non-renewable | solar and wind energy, water, forests, wildlife / fossil fuels, minerals |\n"
            "| **Ownership** | individual / community / national / international | a farmer's land, a house / grazing grounds, village ponds, public parks / roads, canals, railways, minerals / oceanic resources beyond 200 nautical miles |\n"
            "| **Status of development** | potential / developed / stock / reserves | wind and solar energy in Rajasthan and Gujarat / resources surveyed and in use / hydrogen in water (no technology yet) / water in dams for future hydel power |")
TIMELINE = ("| Year | Event |\n|---|---|\n| 1951 | First Five Year Plan: resource planning becomes part of national planning |\n| 1952 | National Forest Policy: 33 per cent of the area should be under forest |\n"
            "| 1968 | Club of Rome advocates resource conservation in a systematic way |\n| 1974 | Schumacher's book *Small is Beautiful* repeats Gandhi's philosophy |\n"
            "| 1987 | Brundtland Commission Report, *Our Common Future*, introduces 'sustainable development' |\n| June 1992 | Earth Summit at Rio de Janeiro; Agenda 21 adopted |")
LANDUSE = ("| Category | What it includes |\n|---|---|\n| 1. Forests | land under forest cover |\n| 2. Land not available for cultivation | (a) barren and wasteland; (b) land put to non-agricultural uses: buildings, roads, factories |\n"
           "| 3. Other uncultivated land (excluding fallow) | (a) permanent pastures and grazing land; (b) land under miscellaneous tree crops and groves; (c) culturable wasteland left uncultivated for more than 5 agricultural years |\n"
           "| 4. Fallow lands | (a) current fallow: left uncultivated for one agricultural year or less; (b) other than current fallow: left uncultivated for 1 to 5 agricultural years |\n"
           "| 5. Net sown area | area sown with crops in a year; **gross cropped area** = net sown area + area sown more than once |")
SOILS = ("| Soil | Formed by / found in | Features | Crops |\n|---|---|---|---|\n"
         "| **Alluvial** | deposited by the Indus, Ganga and Brahmaputra; northern plains, Rajasthan and Gujarat, eastern coast deltas (Mahanadi, Godavari, Krishna, Kaveri) | sand, silt, clay; rich in potash, phosphoric acid and lime; bangar (old) and khadar (new) | sugarcane, paddy, wheat, cereals, pulses |\n"
         "| **Black (regur)** | basalt lava of the Deccan trap; Maharashtra, Saurashtra, Malwa, Madhya Pradesh, Chhattisgarh, Godavari and Krishna valleys | clayey, holds moisture, rich in calcium carbonate, magnesium, potash, lime; poor in phosphorus; deep cracks in summer | cotton |\n"
         "| **Red and yellow** | crystalline igneous rocks in low-rainfall eastern and southern Deccan; Odisha, Chhattisgarh, southern middle Ganga plain, piedmont of Western Ghats | red from iron; yellow when hydrated | (with manure) many crops |\n"
         "| **Laterite** | high temperature and heavy rainfall; Karnataka, Kerala, Tamil Nadu, Madhya Pradesh, hilly Odisha and Assam | intense leaching; poor in humus | cashew nut (red laterite), tea, coffee with manure |\n"
         "| **Arid** | dry areas, western Rajasthan | sandy, saline; little humus and moisture; kankar in lower layers | cultivable with irrigation |\n"
         "| **Forest** | hilly and mountainous areas with enough rainforest | loamy and silty on valley sides, coarse on upper slopes; acidic, low humus in snow-covered areas | fertile in river terraces and alluvial fans |")

sections = [
 {"id": "s1", "title": "Everything around us", "blocks": [
  blk("s1.hook", "hook", title="Is a waterfall a resource?",
    body="A waterfall in a forest is just a beautiful sight until people build a turbine and turn its water into electricity. Coal lay under the ground for millions of years, but became a resource only when humans learnt to burn it for energy.\n\n"
         "So nature alone does not make a resource: **human beings, technology and institutions** do. In this chapter you will learn what resources are, why India must plan their use, and how the land and soil that feed us are being used, and wasted."),
  blk("s1.inspiration", "inspiration", title="Ecology is permanent economy", person="Sunderlal Bahuguna", years="1927–2021",
    body="Sunderlal Bahuguna, a Gandhian from the hills of present-day Uttarakhand, saw forests being cut, hill slopes washing away and springs drying up. He became a leader of the **Chipko movement**, in which villagers hugged trees to save them.\n\n"
         "He walked thousands of kilometres across the Himalayas to spread one message: ***'Ecology is permanent economy.'*** Without healthy forests, soil and water, no development can last.",
    future="Resource geography leads to careers in environmental science, soil science, agriculture, urban planning, remote sensing and GIS."),
  C.socratic("s1.socratic", "When does something in nature become a resource?",
    ["When it is technologically accessible, economically feasible and culturally acceptable", "As soon as it exists in nature", "Only when the government owns it"], 0,
    "Everything that can be used to satisfy our needs, provided it is technologically accessible, economically feasible and culturally acceptable, is a resource."),
 ]},
 {"id": "s2", "title": "Resources and their types", "blocks": [
  blk("s2.thm", "theory", title="What is a resource?", revision=True,
    body="Everything available in our environment which can be used to satisfy our needs, provided it is **technologically accessible, economically feasible and culturally acceptable**, can be termed a **resource**.\n\n"
         "Resources are a **function of human activities**. Human beings are themselves essential components of resources: they transform materials in the environment into resources and use them. There is an **interdependent relationship between nature, technology and institutions**.\n\n"
         "**Classification of resources:**\n"
         "1. **On the basis of origin:** **biotic** resources are obtained from the biosphere and have life: human beings, flora and fauna, fisheries, livestock. **Abiotic** resources are composed of non-living things: rocks and metals.\n"
         "2. **On the basis of exhaustibility:** **renewable** (replenishable) resources can be renewed or reproduced by physical, chemical or mechanical processes: solar and wind energy, water, forests and wildlife. They may be **continuous or flow** (water, wind) or **biological**. "
         "**Non-renewable** resources develop over a very long geological time; minerals and fossil fuels take millions of years to form. Some, like metals, are **recyclable**; others, like fossil fuels, cannot be recycled and get exhausted with use.\n"
         "3. **On the basis of ownership:** **individual** (a farmer's land, plots, houses); **community-owned** (grazing grounds, burial grounds, village ponds, public parks, picnic spots, playgrounds); "
         "**national** (all minerals, water resources, forests, wildlife, land within political boundaries and oceanic area **up to 12 nautical miles (22.2 km)** from the coast, called **territorial water**); and **international** resources, regulated by international institutions: **oceanic resources beyond 200 nautical miles** of the **Exclusive Economic Zone** belong to the open ocean, and no country can use them without the agreement of international institutions.\n"
         "4. **On the basis of the status of development:** **potential** resources are found in a region but not yet used (Rajasthan and Gujarat have enormous potential for wind and solar energy); **developed** resources are surveyed, with their quality and quantity determined, and in use; "
         "**stock** is material that can satisfy needs but humans lack the technology to use it (water is a compound of hydrogen and oxygen, which could be a rich source of energy, but we lack the advanced technology); **reserves** are a **subset of stock** that can be used with existing technology but whose use has not started, kept for the future (river water used later for hydroelectric power)."),
  blk("s2.table", "markdown_table", title="Classification of resources at a glance", revision=True, body=CLASSIFY),
  C.kc("s2.check", "Water contains hydrogen, a rich source of energy, but we lack the technology to use it. What type of resource is this?",
    [("Stock", ""), ("Reserve", "Reserves can be used with existing technology."), ("Developed resource", "A developed resource is already in use."), ("Community resource", "That is a type based on ownership.")],
    "Stock: the material is there but technology to use it is not."),
  C.kc("s2.check2", "Up to how far from the coast does the territorial water of India extend?",
    [("12 nautical miles (22.2 km)", ""), ("200 nautical miles", "That is the limit of the Exclusive Economic Zone."), ("2 nautical miles", "It is 12 nautical miles."), ("100 km", "It is 22.2 km.")],
    "Territorial water extends 12 nautical miles (22.2 km) from the coast; the resources there are national resources."),
 ]},
 {"id": "s3", "title": "Using resources wisely", "blocks": [
  blk("s3.thm", "theory", title="Development, planning and conservation", revision=True,
    body="Resources are vital for human survival. But humans used them **indiscriminately**, leading to major problems:\n"
         "- **depletion** of resources to satisfy the greed of a few individuals;\n- **accumulation** of resources in a few hands, dividing society into **haves and have-nots** (rich and poor);\n"
         "- **global ecological crises** such as global warming, ozone layer depletion, environmental pollution and land degradation.\n\n"
         "**Sustainable development** means development should take place **without damaging the environment**, and development in the present should **not compromise the needs of future generations**.\n\n"
         "**Rio de Janeiro Earth Summit, 1992:** in **June 1992**, more than **100 heads of state** met in Rio de Janeiro, Brazil, at the first International Earth Summit, to address environmental protection and socio-economic development at the global level. They signed the **Declaration on Global Climatic Change and Biological Diversity**, and endorsed the global Forest Principles. "
         "The summit adopted **Agenda 21**: an agenda to **combat environmental damage, poverty and disease through global co-operation** on common interests, mutual needs and shared responsibilities. Its major objective is that **every local government should draw up its own local Agenda 21**.\n\n"
         "**Resource planning** is essential in India because of the enormous **diversity** in the availability of resources:\n"
         "- **Jharkhand, Madhya Pradesh and Chhattisgarh** are rich in minerals and coal deposits.\n- **Arunachal Pradesh** has abundant water resources but lacks infrastructural development.\n"
         "- **Rajasthan** is very well endowed with solar and wind energy but lacks water resources.\n- **Ladakh** is a cold desert, relatively isolated, with a very rich cultural heritage but deficient in water, infrastructure and some vital minerals.\n\n"
         "**Steps in resource planning:**\n1. **Identification and inventory** of resources across the country: surveying, mapping, and qualitative and quantitative estimation and measurement.\n"
         "2. Evolving a **planning structure** with appropriate technology, skill and institutional set-up for implementing the plans.\n3. **Matching** the resource development plans with overall **national development plans**.\n\n"
         "India has made concerted efforts since the **First Five Year Plan**. But the availability of resources alone is not enough: development needs **technology, quality of human resources and historical experiences**, and resources contribute to development only when there are **technological development and institutional changes**. "
         "Colonies rich in resources attracted foreign invaders, and the higher technological level of the colonisers helped them exploit those resources.\n\n"
         "**Conservation of resources:** **Gandhiji** said: ***'There is enough for everybody's need and not for anybody's greed.'*** He blamed greedy and selfish individuals and the exploitative nature of modern technology, and favoured production **by the masses** rather than mass production. "
         "The **Club of Rome** (1968) advocated resource conservation in a systematic way; **Schumacher's *Small is Beautiful*** (1974) repeated Gandhi's philosophy; and the **Brundtland Commission Report** (1987), ***Our Common Future***, introduced the concept of **sustainable development**."),
  blk("s3.timeline", "markdown_table", title="Milestones in resource conservation", revision=True, body=TIMELINE),
  C.kc("s3.check", "What is the main objective of Agenda 21?",
    [("To combat environmental damage, poverty and disease through global co-operation", ""), ("To increase mining in developing countries", "It aims at sustainable development, not more exploitation."),
     ("To divide resources among rich countries", "It is about shared responsibilities."), ("To ban all use of fossil fuels", "It does not ban resources; it seeks sustainable use.")],
    "Agenda 21, adopted at Rio in 1992, also says every local government should draw up its own local Agenda 21."),
  C.kc("s3.check2", "Which state is rich in solar and wind energy but lacks water resources?",
    [("Rajasthan", ""), ("Arunachal Pradesh", "It has abundant water but lacks infrastructure."), ("Jharkhand", "It is rich in minerals and coal."), ("Kerala", "It receives heavy rainfall.")],
    "Rajasthan: solar and wind energy, but little water."),
 ]},
 {"id": "s4", "title": "Land resources", "blocks": [
  blk("s4.thm", "theory", title="Land utilisation and land degradation", revision=True,
    body="Land is a **natural resource of utmost importance**: it supports natural vegetation, wildlife, human life, economic activities, transport and communication. Since it is **limited**, it must be used with careful planning.\n\n"
         "India has a variety of relief features: about **43 per cent** of the land area is **plains**, providing facilities for agriculture and industry; **mountains** account for **30 per cent**, ensuring the perennial flow of some rivers, tourism and ecological aspects; about **27 per cent** is **plateau**, with rich reserves of minerals, fossil fuels and forests.\n\n"
         "**Land use pattern in India:** land use is determined by **physical factors** (topography, climate, soil types) and **human factors** (population density, technological capability, culture and traditions). "
         "India's total geographical area is **3.28 million sq km**, but land use data is available for only about **93 per cent**, because land use reporting for most of the north-east states except Assam has not been done fully, and some areas of Jammu and Kashmir occupied by Pakistan and China have not been surveyed.\n"
         "- The net sown area varies greatly: **over 80 per cent** of the total area in **Punjab and Haryana**, but **less than 10 per cent** in **Arunachal Pradesh, Mizoram, Manipur and the Andaman and Nicobar Islands**.\n"
         "- Forest area is far below the **33 per cent** of geographical area outlined in the **National Forest Policy (1952)**, considered essential for maintaining the ecological balance. Many people living in and around forests depend on them for their livelihood.\n"
         "- Land under **permanent pasture** has decreased; land left **fallow** for long periods can be degraded; and land put to non-agricultural uses has increased with the growth of cities and industries.\n\n"
         "**Land degradation:** human activities have caused degradation, and natural forces have aggravated it. India has about **130 million hectares** of degraded land: about **28 per cent** is degraded forest, **56 per cent** is water-eroded, and the rest is affected by **saline and alkaline deposits**.\n"
         "- **Mining:** in **Jharkhand, Chhattisgarh, Madhya Pradesh and Odisha**, deforestation due to mining has caused severe degradation; mining sites are abandoned after excavation, leaving deep scars and traces of over-burdening.\n"
         "- **Overgrazing:** in **Gujarat, Rajasthan, Madhya Pradesh and Maharashtra**, overgrazing is one of the main causes.\n"
         "- **Over-irrigation:** in **Punjab, Haryana and western Uttar Pradesh**, over-irrigation causes **waterlogging**, increasing **salinity and alkalinity** in the soil.\n"
         "- **Mineral processing:** grinding limestone for the cement industry and calcite and soapstone for the ceramic industry generates huge dust, which settles on land and slows the infiltration of water.\n"
         "- **Industrial effluents** have become a major source of land and water pollution.\n\n"
         "**Ways to solve land degradation:** afforestation and proper management of grazing; planting **shelter belts** of plants; control on overgrazing; **stabilisation of sand dunes** by growing thorny bushes; proper management of wastelands; control of mining activities; and proper discharge and disposal of industrial effluents and wastes after treatment."),
  blk("s4.landuse", "markdown_table", title="Categories of land use", revision=True, body=LANDUSE),
  C.kc("s4.check", "Which is the main cause of land degradation in Punjab and Haryana?",
    [("Over-irrigation", ""), ("Mining", "Mining degrades land in Jharkhand, Chhattisgarh, Madhya Pradesh and Odisha."), ("Overgrazing", "Overgrazing is the main cause in Gujarat, Rajasthan, Madhya Pradesh and Maharashtra."), ("Deforestation by shifting cultivation", "That is not the cause given for Punjab.")],
    "Over-irrigation causes waterlogging, which raises salinity and alkalinity."),
  C.kc("s4.check2", "Land left uncultivated for one agricultural year or less is called:",
    [("Current fallow", ""), ("Culturable wasteland", "That is left uncultivated for more than 5 years."), ("Other than current fallow", "That is left uncultivated for 1 to 5 years."), ("Barren land", "Barren land cannot be cultivated.")],
    "Current fallow: one agricultural year or less."),
 ]},
 {"id": "s5", "title": "Soil as a resource", "blocks": [
  blk("s5.thm", "theory", title="How soil forms and the soils of India", revision=True,
    body="Soil is the most important **renewable natural resource**: the medium of plant growth that supports different types of living organisms. It is a living system. It takes **millions of years to form soil up to a few centimetres in depth**.\n\n"
         "**Factors of soil formation:** **relief, parent rock or bedrock, climate, vegetation and other forms of life, and time**. Natural forces like change in temperature, actions of running water, wind and glaciers, and activities of decomposers contribute to it. Chemical and organic changes in the soil are equally important. Soil also consists of organic (humus) and inorganic materials.\n\n"
         "**1. Alluvial soil:** the **most widely spread** and important soil. The entire **northern plains** are made of it, deposited by three Himalayan river systems: the **Indus, the Ganga and the Brahmaputra**. It also extends to **Rajasthan and Gujarat** through a narrow corridor, and is found in the eastern coastal plains, particularly the **deltas of the Mahanadi, Godavari, Krishna and Kaveri**.\n"
         "- It consists of various proportions of **sand, silt and clay**. Soil particles are bigger in the upper reaches of the river valley, near the place of the break of slope; coarse soils are common in piedmont plains such as the **Duars, Chos and Terai**.\n"
         "- By age it is **old alluvial (bangar)**, with a higher concentration of **kanker nodules**, and **new alluvial (khadar)**, with more fine particles, which is **more fertile** than bangar.\n"
         "- It is very fertile, containing adequate **potash, phosphoric acid and lime**, ideal for **sugarcane, paddy, wheat and other cereal and pulse crops**. So these regions are **intensively cultivated and densely populated**. Soils in drier areas are more alkaline and can be productive after proper treatment and irrigation.\n\n"
         "**2. Black soil (regur soil):** black in colour, ideal for growing **cotton**, hence also called **black cotton soil**. Climatic conditions and **parent rock material** are important for its formation: it is made of **lava flows (basalt)** and is typical of the **Deccan trap region** spread over the north-west Deccan plateau.\n"
         "- It covers the plateaus of **Maharashtra, Saurashtra, Malwa, Madhya Pradesh and Chhattisgarh**, and extends south-east along the **Godavari and Krishna valleys**.\n"
         "- It is made of extremely fine **clayey** material, known for its capacity to **hold moisture**; rich in **calcium carbonate, magnesium, potash and lime**, but **poor in phosphoric content**.\n"
         "- It develops **deep cracks during hot weather**, which helps in the proper **aeration** of the soil; it becomes **sticky when wet** and is difficult to work on unless tilled immediately after the first shower or during the pre-monsoon period.\n\n"
         "**3. Red and yellow soils:** develop on **crystalline igneous rocks** in areas of low rainfall in the eastern and southern parts of the Deccan plateau; also in parts of **Odisha, Chhattisgarh, southern parts of the middle Ganga plain** and along the **piedmont zone of the Western Ghats**. "
         "They are **reddish** due to the **diffusion of iron** in crystalline and metamorphic rocks, and look **yellow when hydrated**.\n\n"
         "**4. Laterite soil:** from the Latin word **'later' meaning brick**. It develops under **high temperature and heavy rainfall**, the result of **intense leaching** due to heavy rain. **Humus content is low** because decomposers like bacteria are destroyed by high temperature. "
         "Found mainly in **Karnataka, Kerala, Tamil Nadu, Madhya Pradesh** and the hilly areas of **Odisha and Assam**. After adopting appropriate soil conservation techniques, particularly in hilly areas, these soils are very useful for **tea and coffee**; red laterite soils in **Tamil Nadu, Andhra Pradesh and Kerala** are more suitable for crops like **cashew nut**.\n\n"
         "**5. Arid soil:** ranges from **red to brown**; generally **sandy** in texture and **saline** in nature; in some areas salt content is so high that common salt is obtained by evaporating water. Due to the dry climate and high temperature, evaporation is faster and the soil **lacks humus and moisture**. "
         "The lower horizons are occupied by **kankar** because of increasing calcium content downwards, which restricts the infiltration of water. After proper **irrigation** these soils become cultivable, as in **western Rajasthan**.\n\n"
         "**6. Forest soil:** found in **hilly and mountainous areas** where sufficient rainforests are available. Texture varies with the mountain environment: **loamy and silty** on valley sides and **coarse-grained** on the upper slopes. In the snow-covered areas of the Himalayas they experience denudation and are **acidic with low humus**; soils in the lower parts of the valleys, particularly on **river terraces and alluvial fans**, are fertile."),
  blk("s5.table", "markdown_table", title="The six soils compared", revision=True, body=SOILS),
  C.kc("s5.check", "Why is black soil good for cotton?",
    [("It is clayey and holds moisture well", ""), ("It is sandy and drains quickly", "That describes arid soil."), ("It is poor in calcium", "It is rich in calcium carbonate."), ("It is formed by intense leaching", "That describes laterite soil.")],
    "Black soil holds moisture and is rich in calcium carbonate, magnesium, potash and lime."),
  C.kc("s5.check2", "Which soil gets its name from the Latin word for brick?",
    [("Laterite soil", ""), ("Regur soil", "Regur is another name for black soil."), ("Khadar", "Khadar is new alluvial soil."), ("Arid soil", "Arid soil is found in dry areas.")],
    "'Later' means brick; laterite forms under high temperature and heavy rain."),
 ]},
 {"id": "s6", "title": "Soil erosion and conservation", "blocks": [
  blk("s6.thm", "theory", title="How soil is lost, and how to save it", revision=True,
    body="The denudation of the soil cover and its subsequent washing down is called **soil erosion**. Soil formation and erosion go on simultaneously and are generally in balance, but human activities disturb this balance.\n\n"
         "**Causes:** **deforestation, overgrazing, construction and mining**, and natural forces like **wind, glaciers and water**.\n"
         "- **Gullies:** running water cuts through clayey soils and makes deep channels called gullies. The land becomes unfit for cultivation and is known as **bad land**. In the **Chambal basin**, such lands are called **ravines**.\n"
         "- **Sheet erosion:** water flows as a sheet over large areas down a slope, and the topsoil is washed away.\n"
         "- **Wind erosion:** wind blows loose soil off flat or sloping land.\n"
         "- **Defective methods of farming:** ploughing **up and down the slope** forms channels for the quick flow of water, leading to erosion.\n\n"
         "**Soil conservation:**\n"
         "- **Contour ploughing:** ploughing **along the contour lines** decelerates the flow of water down the slopes.\n"
         "- **Terrace cultivation:** **steps** cut out on the slopes make terraces, which restrict erosion. The **western and central Himalayas** have well-developed terrace farming.\n"
         "- **Strip cropping:** large fields are divided into strips, and **strips of grass are left to grow between the crops**; this breaks the force of the wind.\n"
         "- **Shelter belts:** planting **lines of trees** to create shelter works in a similar way. Rows of such trees have contributed significantly to the **stabilisation of sand dunes** and the desert in **western India**.\n\n"
         "Villages like **Sukhomajri** (Haryana) and the **Jhabua** district (Madhya Pradesh) have shown that land degradation can be reversed through community management of watersheds and forests."),
  C.kc("s6.check", "Which method of soil conservation is well developed in the western and central Himalayas?",
    [("Terrace cultivation", ""), ("Shelter belts", "Shelter belts stabilise sand dunes in western India."), ("Strip cropping", "Strip cropping breaks the force of the wind on large fields."), ("Ploughing up and down the slope", "That causes erosion.")],
    "Steps cut on the slopes form terraces that slow down water and check erosion."),
 ]},
 {"id": "s7", "title": "Remember, avoid, practise", "blocks": [
  blk("s7.memory", "memory_trick", title="Memory tricks",
    body="- **Four bases of classification: \"O-E-O-S\"** = Origin, Exhaustibility, Ownership, Status of development.\n- **Status ladder: Potential → Developed; Stock ⊃ Reserves** (reserves are a part of stock).\n"
         "- **12 and 200:** 12 nautical miles = territorial water (national); beyond 200 nautical miles = international.\n- **Land of India 43-30-27:** plains, mountains, plateaus.\n"
         "- **Degradation map: \"Mines in the east, grazing in the west, water in the north-west\":** mining (Jharkhand, Chhattisgarh, MP, Odisha), overgrazing (Gujarat, Rajasthan, MP, Maharashtra), over-irrigation (Punjab, Haryana, western UP).\n"
         "- **Soils: \"All Big Rivers Leave A Footprint\"** = Alluvial, Black, Red-yellow, Laterite, Arid, Forest."),
  blk("s7.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying reserves and stock are the same: **reserves are a subset of stock** that can be used with existing technology.\n2. Calling khadar 'old alluvium': **khadar is new** and more fertile; **bangar is old** and has kanker nodules.\n"
         "3. Saying black soil is rich in phosphorus: it is **poor in phosphoric content**.\n4. Saying laterite is rich in humus: humus is **low** because high temperature destroys bacteria.\n"
         "5. Mixing up the 1987 Brundtland Report (sustainable development) with the 1992 Rio Summit (Agenda 21).\n6. Saying gross cropped area = net sown area: gross cropped area also counts land sown **more than once** in a year."),
  blk("s7.tip", "teacher_tip", title="Try this in class",
    body="Bring soil samples from a garden, a river bank and a red-earth area. Let students compare colour, texture and how fast water drains through each. "
         "Then tilt a tray of soil and pour water: once with straight furrows down the slope and once with furrows across it, to show why contour ploughing works."),
  blk("s7.reflection", "reflection", title="Think and explain",
    body="Gandhiji said, 'There is enough for everybody's need and not for anybody's greed.' List two things in your own home or school that waste a resource, and suggest how to fix each."),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 2 (Forest and Wildlife Resources):** conservation of biotic resources.\n- **Chapter 3 (Water Resources):** dams, rainwater harvesting and water conservation.\n"
         "- **Chapter 4 (Agriculture):** which soils suit which crops, and Indian cropping seasons.\n- **Chapter 5 (Minerals and Energy Resources):** non-renewable resources and their conservation."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="'Resources can contribute to development only when they are accompanied by appropriate technological development and institutional changes.' Explain with examples in about 120 words.\n\n"
         "**Model answer:** Resources alone do not create development; people need technology to use them and institutions to manage them. Rajasthan has huge potential for solar and wind energy, but it becomes useful only with solar parks and wind farms. Hydrogen in water is a stock because we lack the technology to use it. "
         "Arunachal Pradesh has abundant water but lacks infrastructure, so its water is not fully used. History shows that colonies rich in resources were exploited by colonisers with higher technology. "
         "India, therefore, plans its resources through surveys, planning structures and Five Year Plans, matching them with national development, so that resources lead to development."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- A resource is anything that satisfies our needs and is technologically accessible, economically feasible and culturally acceptable.\n"
         "- Resources are classified by origin, exhaustibility, ownership and status of development.\n"
         "- Indiscriminate use causes depletion, inequality and ecological crises; sustainable development, the Rio Summit (1992) and Agenda 21 aim to fix this.\n"
         "- Resource planning in India involves inventory, a planning structure and matching with national plans; Gandhiji stressed conservation.\n"
         "- Land: 43% plains, 30% mountains, 27% plateaus; land degradation comes from mining, overgrazing, over-irrigation, dust and effluents.\n"
         "- Six soil types: alluvial, black, red and yellow, laterite, arid and forest; soil erosion is checked by contour ploughing, terracing, strip cropping and shelter belts."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- The 2025-26 sample paper asked what makes resource development lead to overall development (technology and institutional changes) and to fill a soil classification chart (black soil for cotton, laterite for cashew nut).\n"
         "- 3/5-mark favourites: classification of resources, resource planning steps, land degradation and its solutions, features of alluvial and black soils, methods of soil conservation.\n"
         "- **Map work:** be ready to locate and label the major soil types on the map of India."),
  blk("s7.flash1", "flashcard", front="What are the three conditions for something to be a resource?", back="Technologically accessible, economically feasible and culturally acceptable."),
  blk("s7.flash2", "flashcard", front="What is Agenda 21?", back="An agenda adopted at the Rio Earth Summit (1992) to combat environmental damage, poverty and disease through global co-operation."),
  blk("s7.flash3", "flashcard", front="What is the difference between bangar and khadar?", back="Bangar is old alluvium with kanker nodules; khadar is new, finer and more fertile."),
  blk("s7.flash4", "flashcard", front="Name four methods of soil conservation.", back="Contour ploughing, terrace cultivation, strip cropping and shelter belts."),
 ]},
]

# ---------------- Sample paper ----------------
M("sqp10", DEV, "What is essential for resource development to contribute to overall development?",
  [("The availability of resources alone is enough.", "Availability alone is not enough; many resource-rich regions remain undeveloped."),
   ("The presence of foreign invaders and their governance.", "Colonisers exploited resources; this did not develop the colonies."),
   ("Technological development and institutional changes.", ""),
   ("Only human resources can contribute to development.", "Natural resources, technology and institutions all matter.")],
  "Resources contribute to development only when accompanied by appropriate technological development and institutional changes.", "medium", SQP(10), correct=2)
M("sqp11", SOIL, "Identify the appropriate option to fill in the empty boxes of the chart 'Classification of Soils': Alluvial: ideal for sugarcane, paddy, wheat and other cereal and pulse crops; (?): ideal for growing cotton; (?): suitable for crops like cashew nut.",
  [("Black soil, Red and Yellow soils", "Red and yellow soils are not the cashew nut soil."), ("Laterite soil, Black soil.", "The order is reversed: cotton is grown on black soil."),
   ("Red & Yellow soils & Black soil.", "Cotton is grown on black soil, cashew nut on red laterite soil."), ("Black soil & Laterite soil.", "")],
  "Black (regur) soil is ideal for cotton; red laterite soil suits cashew nut.", "medium", SQP(11), correct=3)

# ---------------- NCERT exercises ----------------
M("ex1i", RES, "Which one of the following type of resource is iron ore?",
  [("Renewable", "Iron ore cannot be renewed in a human lifetime."), ("Biotic", "Iron ore has no life."), ("Flow", "Flow resources are like water and wind."), ("Non-renewable", "")],
  "Iron ore is a mineral formed over millions of years: non-renewable (but recyclable as metal).", "easy", ex("1(i)"), correct=3)
M("ex1ii", RES, "Under which of the following type of resource can tidal energy be put?",
  [("Replenishable", ""), ("Human-made", "Tides are natural."), ("Abiotic", "This misses the key point: tidal energy keeps renewing."), ("Non-recyclable", "Tidal energy is renewed continuously.")],
  "Tidal energy is renewed continuously, so it is a replenishable (renewable) resource.", "easy", ex("1(ii)"))
M("ex1iii", LAND, "Which one of the following is the main cause of land degradation in Punjab?",
  [("Intensive cultivation", "The cause the book gives for Punjab is over-irrigation."), ("Deforestation", "Deforestation by mining affects Jharkhand, Odisha and others."), ("Over-irrigation", ""), ("Overgrazing", "Overgrazing affects Gujarat, Rajasthan, MP and Maharashtra.")],
  "Over-irrigation causes waterlogging and raises salinity and alkalinity in Punjab.", "easy", ex("1(iii)"), correct=2)
M("ex1iv", EROS, "In which one of the following states is terrace cultivation practised?",
  [("Punjab", "Punjab is a plain."), ("Plains of Uttar Pradesh", "Terraces are made on slopes."), ("Haryana", "Haryana is mostly plain."), ("Uttarakhand", "")],
  "Terraces are cut on hill slopes, as in Uttarakhand in the western and central Himalayas.", "easy", ex("1(iv)"), correct=3)
W("ex2i", "very_short_answer", SOIL, "Name three states having black soil and the crop which is mainly grown in it.",
  ["States: Maharashtra, Gujarat (Saurashtra), Madhya Pradesh (Malwa) and Chhattisgarh.", "The main crop is cotton, so black soil is also called black cotton soil."], source=ex("2(i)"))
W("ex2ii", "short_answer", SOIL, "What type of soil is found in the river deltas of the eastern coast? Give three main features of this type of soil.",
  ["Alluvial soil is found in the deltas of the Mahanadi, Godavari, Krishna and Kaveri.",
   "It consists of sand, silt and clay, and is very fertile, with adequate potash, phosphoric acid and lime.",
   "It is ideal for paddy, sugarcane, wheat, cereals and pulses, so these areas are intensively cultivated and densely populated."], source=ex("2(ii)"))
W("ex2iii", "short_answer", EROS, "What steps can be taken to control soil erosion in the hilly areas?",
  ["Contour ploughing: ploughing along the contour lines slows the flow of water down the slopes.",
   "Terrace cultivation: steps cut on the slopes check erosion, as in the western and central Himalayas.",
   "Afforestation and controlled grazing; strip cropping and rows of trees reduce the force of water and wind."], source=ex("2(iii)"))
W("ex2iv", "short_answer", RES, "What are the biotic and abiotic resources? Give some examples.",
  ["Biotic resources are obtained from the biosphere and have life.", "Examples: human beings, flora and fauna, fisheries and livestock.",
   "Abiotic resources are composed of non-living things, for example rocks and metals."], source=ex("2(iv)"))
W("ex3i", "long_answer", LAND, "Explain the land use pattern in India and why the land under forest has not increased much since 1960-61.",
  ["Land use depends on physical factors (relief, climate, soil) and human factors (population, technology, culture); India's area is 3.28 million sq km, with land use data for about 93 per cent.",
   "Land is classed as forests, land not available for cultivation, other uncultivated land, fallow land and net sown area; net sown area is over 80 per cent in Punjab and Haryana but under 10 per cent in Arunachal Pradesh, Mizoram, Manipur and Andaman and Nicobar.",
   "Land under permanent pasture has fallen, and land under non-agricultural uses has grown with cities and industries.",
   "Forest cover has not increased much and remains far below the 33 per cent recommended by the National Forest Policy (1952).",
   "Reasons: the growing population needs land for farming, housing, industries, roads and mining (as in Jharkhand, Chhattisgarh, MP and Odisha), and large development projects; so forests keep being cleared even as afforestation goes on."],
  source=ex("3(i)"))
W("ex3ii", "long_answer", DEV, "How have technical and economic development led to more consumption of resources?",
  ["New technology made it possible to extract and use resources such as minerals, fossil fuels and water on a large scale.",
   "Industrialisation and mass production created demand for ever more raw materials and energy.",
   "Rising incomes increased consumption of goods, vehicles and electricity, using up resources faster.",
   "Colonisers with better technology exploited the resources of colonies; today resources gather in a few hands, dividing society into haves and have-nots.",
   "This indiscriminate use has caused depletion, global warming, ozone depletion, pollution and land degradation, which is why sustainable development is needed."],
  source=ex("3(ii)"))

# ---------------- MCQs ----------------
M("mcq01", RES, "Which of these is NOT a condition for something to be called a resource?",
  [("It must be found in every country", ""), ("It must be technologically accessible", "This is one of the three conditions."), ("It must be economically feasible", "This is one of the three conditions."), ("It must be culturally acceptable", "This is one of the three conditions.")],
  "A resource must be technologically accessible, economically feasible and culturally acceptable; it need not be found everywhere.")
M("mcq02", RES, "Resources are a function of:",
  [("human activities", ""), ("only nature", "Nature provides materials; humans make them resources."), ("only the government", "Government is one institution among many."), ("only money", "Money alone cannot create resources.")],
  "Human beings transform materials in the environment into resources.")
M("mcq03", RES, "Fisheries and livestock are examples of:",
  [("biotic resources", ""), ("abiotic resources", "Abiotic resources are non-living."), ("non-renewable resources", "They can be reproduced."), ("international resources", "That is a type by ownership.")],
  "They are obtained from the biosphere and have life.")
M("mcq04", RES, "Which of the following is a non-renewable resource?",
  [("Coal", ""), ("Wind energy", "Wind is a flow resource."), ("Forests", "Forests can be regrown."), ("Solar energy", "Solar energy is renewable.")],
  "Fossil fuels like coal take millions of years to form and get exhausted with use.")
M("mcq05", RES, "Which non-renewable resource can be recycled?",
  [("Metals", ""), ("Petroleum", "Fossil fuels cannot be recycled."), ("Coal", "Fossil fuels cannot be recycled."), ("Natural gas", "Fossil fuels cannot be recycled.")],
  "Metals are non-renewable but recyclable.")
M("mcq06", RES, "Village ponds, public parks and grazing grounds are examples of:",
  [("community-owned resources", ""), ("individual resources", "They are not owned by one person."), ("national resources", "They belong to the village community."), ("international resources", "They are local.")],
  "These are accessible to all the people of the community.")
M("mcq07", RES, "Oceanic resources beyond 200 nautical miles of the Exclusive Economic Zone are:",
  [("international resources", ""), ("national resources", "National waters end at 12 nautical miles."), ("community resources", "No village or town owns them."), ("individual resources", "No individual owns them.")],
  "No country can use them without the agreement of international institutions.")
M("mcq08", RES, "Resources found in a region but not yet utilised are called:",
  [("potential resources", ""), ("developed resources", "Developed resources are surveyed and in use."), ("stock", "Stock cannot be used for lack of technology."), ("reserves", "Reserves are a part of stock kept for the future.")],
  "Example: wind and solar energy in Rajasthan and Gujarat.")
M("mcq09", RES, "Water in dams which may be used for hydroelectric power in the future is an example of:",
  [("reserves", ""), ("stock", "We already have the technology to use it."), ("potential resources", "It is already surveyed and kept for later."), ("biotic resources", "Water is abiotic.")],
  "Reserves are a subset of stock: usable with existing technology but kept for the future.")
M("mcq10", DEV, "Which is NOT a problem caused by the indiscriminate use of resources?",
  [("Equal distribution of resources among all people", ""), ("Depletion of resources", "This is a real problem."), ("Accumulation of resources in a few hands", "This is a real problem."), ("Global ecological crises", "This is a real problem.")],
  "Indiscriminate use leads to unequal, not equal, distribution: haves and have-nots.")
M("mcq11", DEV, "Sustainable development means:",
  [("development without damaging the environment and without compromising the needs of future generations", ""), ("development only in cities", "It is about the environment and the future."),
   ("using all resources quickly", "That is the opposite."), ("stopping all development", "It allows development, but sustainably.")],
  "The idea was introduced by the Brundtland Commission Report (1987).")
M("mcq12", DEV, "The first International Earth Summit was held in 1992 at:",
  [("Rio de Janeiro", ""), ("Kyoto", "That is linked to a later climate protocol."), ("Geneva", "The summit was in Brazil."), ("New Delhi", "The summit was in Brazil.")],
  "In June 1992, more than 100 heads of state met at Rio de Janeiro, Brazil.")
M("mcq13", DEV, "Which state is rich in minerals and coal deposits?",
  [("Jharkhand", ""), ("Rajasthan", "Rajasthan is rich in solar and wind energy."), ("Arunachal Pradesh", "It is rich in water resources."), ("Punjab", "Punjab is known for agriculture.")],
  "Jharkhand, Madhya Pradesh and Chhattisgarh are rich in minerals and coal.")
M("mcq14", DEV, "Ladakh is deficient in:",
  [("water, infrastructure and some vital minerals", ""), ("cultural heritage", "Ladakh has a very rich cultural heritage."), ("sunlight", "Ladakh gets plenty of sunshine."), ("land", "Ladakh has large land areas.")],
  "Ladakh is a cold desert, relatively isolated from the rest of the country.")
M("mcq15", DEV, "What is the first step of resource planning?",
  [("Identification and inventory of resources", ""), ("Matching with national plans", "That is the last step."), ("Setting up institutions", "That is the second step."), ("Exporting resources", "That is not a step of planning.")],
  "It involves surveying, mapping and qualitative and quantitative estimation of resources.")
M("mcq16", DEV, "Who said, 'There is enough for everybody's need and not for anybody's greed'?",
  [("Mahatma Gandhi", ""), ("Schumacher", "He wrote Small is Beautiful."), ("Jawaharlal Nehru", "The quote is Gandhiji's."), ("Sunderlal Bahuguna", "His slogan was 'Ecology is permanent economy'.")],
  "Gandhiji blamed greed and the exploitative nature of modern technology.")
M("mcq17", DEV, "Which report introduced the concept of sustainable development in 1987?",
  [("The Brundtland Commission Report, 'Our Common Future'", ""), ("Agenda 21", "Agenda 21 was adopted in 1992."), ("Small is Beautiful", "That book was published in 1974."), ("The Club of Rome", "The Club of Rome met in 1968.")],
  "'Our Common Future' (1987).")
M("mcq18", DEV, "Gandhiji favoured:",
  [("production by the masses", ""), ("mass production", "He was against mass production."), ("import of all goods", "He favoured self-reliance."), ("rapid mining", "He stressed conservation.")],
  "He wanted production by the masses rather than mass production.")
M("mcq19", LAND, "About what percentage of India's land area is plains?",
  [("43 per cent", ""), ("30 per cent", "That is the share of mountains."), ("27 per cent", "That is the share of plateaus."), ("60 per cent", "It is about 43 per cent.")],
  "Plains 43%, mountains 30%, plateaus 27%.")
M("mcq20", LAND, "Plateaus in India are important because they:",
  [("have rich reserves of minerals, fossil fuels and forests", ""), ("ensure the perennial flow of rivers", "That is the role of mountains."), ("are best for intensive farming", "That is true of plains."), ("are covered with snow", "That is true of high mountains.")],
  "About 27 per cent of India is plateau.")
M("mcq21", LAND, "Land left uncultivated for more than 5 agricultural years is:",
  [("culturable wasteland", ""), ("current fallow", "Current fallow is one year or less."), ("other than current fallow", "That is 1 to 5 years."), ("net sown area", "Net sown area is cultivated.")],
  "Culturable wasteland is grouped under other uncultivated land.")
M("mcq22", LAND, "Gross cropped area is:",
  [("net sown area plus area sown more than once in a year", ""), ("net sown area minus fallow land", "Fallow land is not part of it."), ("total geographical area", "It covers only cropped land."), ("forest area plus net sown area", "Forests are not cropped.")],
  "Area sown more than once in a year is added to the net sown area.")
M("mcq23", LAND, "In which state is the net sown area more than 80 per cent of the total area?",
  [("Punjab", ""), ("Arunachal Pradesh", "There it is less than 10 per cent."), ("Mizoram", "There it is less than 10 per cent."), ("Manipur", "There it is less than 10 per cent.")],
  "Punjab and Haryana have over 80 per cent net sown area.")
M("mcq24", LAND, "How much land in India is degraded?",
  [("About 130 million hectares", ""), ("About 13 million hectares", "The figure is about ten times larger."), ("About 3.28 million sq km", "That is India's total area."), ("About 33 per cent", "33 per cent is the forest target.")],
  "About 28% is degraded forest, 56% water-eroded and the rest saline and alkaline.")
M("mcq25", LAND, "Overgrazing is the main cause of land degradation in:",
  [("Gujarat, Rajasthan, Madhya Pradesh and Maharashtra", ""), ("Punjab, Haryana and western Uttar Pradesh", "Over-irrigation is the cause there."),
   ("Jharkhand, Chhattisgarh and Odisha", "Mining is the main cause there."), ("Kerala and Karnataka", "These are not named for overgrazing.")],
  "These are the states named in the textbook.")
M("mcq26", LAND, "How does mineral processing degrade land?",
  [("Dust from grinding limestone, calcite and soapstone settles on land and slows infiltration of water", ""), ("It increases the humus content", "Dust does not add humus."),
   ("It causes waterlogging", "Waterlogging comes from over-irrigation."), ("It makes the soil more fertile", "It degrades land.")],
  "Limestone is ground for cement, and calcite and soapstone for ceramics.")
M("mcq27", SOIL, "Which is NOT a factor of soil formation?",
  [("Population density", ""), ("Parent rock", "Parent rock is a key factor."), ("Climate", "Climate is a key factor."), ("Time", "Time is a key factor.")],
  "The factors are relief, parent rock, climate, vegetation and other life forms, and time.")
M("mcq28", SOIL, "The most widely spread soil in India is:",
  [("alluvial soil", ""), ("black soil", "Black soil covers the Deccan trap region."), ("laterite soil", "Laterite is found in high-rainfall areas."), ("arid soil", "Arid soil is found in dry areas.")],
  "The entire northern plains are made of alluvial soil.")
M("mcq29", SOIL, "Coarse alluvial soils in piedmont plains such as the Duars, Chos and Terai are found:",
  [("near the place of the break of slope in the upper reaches", ""), ("in river deltas", "Deltas have finer soils."), ("in the Deccan trap", "That is black soil."), ("in deserts", "That is arid soil.")],
  "Soil particles are bigger in the upper reaches of river valleys.")
M("mcq30", SOIL, "Black soil is formed from:",
  [("lava flows (basalt) of the Deccan trap", ""), ("deposits of Himalayan rivers", "That forms alluvial soil."), ("crystalline igneous rocks in low rainfall", "That forms red soil."), ("intense leaching under heavy rain", "That forms laterite.")],
  "Climate and parent rock (basalt) are important for black soil.")
M("mcq31", SOIL, "Black soil is poor in:",
  [("phosphoric content", ""), ("calcium carbonate", "It is rich in calcium carbonate."), ("potash", "It is rich in potash."), ("lime", "It is rich in lime.")],
  "Black soil is rich in calcium carbonate, magnesium, potash and lime, but poor in phosphorus.")
M("mcq32", SOIL, "Red soil looks red because of:",
  [("diffusion of iron in crystalline and metamorphic rocks", ""), ("high humus", "Humus makes soil dark."), ("salt content", "Salt is typical of arid soil."), ("lava", "Lava forms black soil.")],
  "It looks yellow when hydrated.")
M("mcq33", SOIL, "Laterite soil has low humus because:",
  [("high temperature destroys decomposers like bacteria", ""), ("it is formed from basalt", "That is black soil."), ("it is found only in deserts", "Laterite forms in heavy rainfall areas."), ("it has too much salt", "That is arid soil.")],
  "Laterite forms under high temperature and heavy rainfall with intense leaching.")
M("mcq34", SOIL, "Kankar in the lower horizons of arid soil:",
  [("restricts the infiltration of water", ""), ("increases fertility", "It does not."), ("adds humus", "Arid soil lacks humus."), ("makes the soil sticky", "Stickiness is a feature of black soil.")],
  "Kankar forms because calcium content increases downwards.")
M("mcq35", EROS, "In the Chambal basin, land made unfit for cultivation by gullies is called:",
  [("ravines", ""), ("terraces", "Terraces are steps made to stop erosion."), ("shelter belts", "Shelter belts are rows of trees."), ("deltas", "Deltas are formed by deposition.")],
  "Such land is also known as bad land.")
M("mcq36", EROS, "Leaving strips of grass to grow between crops is called:",
  [("strip cropping", ""), ("contour ploughing", "Contour ploughing follows contour lines."), ("terrace cultivation", "Terraces are steps on slopes."), ("shelter belts", "Shelter belts are lines of trees.")],
  "It breaks the force of the wind.")
M("mcq37", EROS, "Shelter belts have helped to stabilise sand dunes in:",
  [("western India", ""), ("north-east India", "The textbook names western India."), ("the Ganga delta", "The textbook names western India."), ("the Western Ghats", "The textbook names western India.")],
  "Rows of trees break the force of wind in the desert.")
M("mcq38", EROS, "Water flowing as a sheet over large areas down a slope causes:",
  [("sheet erosion", ""), ("gully erosion", "Gullies are deep channels."), ("wind erosion", "That is caused by wind."), ("leaching", "Leaching washes nutrients down through soil.")],
  "The topsoil is washed away.")
# ---------------- Map work (major soil types) ----------------
M("map1", SOIL, "Map work: which soil would you mark over the Deccan trap region of Maharashtra and Malwa?",
  [("Black soil", ""), ("Alluvial soil", "Alluvial soil covers the northern plains."), ("Arid soil", "Arid soil is in western Rajasthan."), ("Forest soil", "Forest soil is in hilly areas.")],
  "Black (regur) soil covers the north-west Deccan plateau.", "medium")
M("map2", SOIL, "Map work: which soil would you mark over the entire northern plains from Punjab to West Bengal?",
  [("Alluvial soil", ""), ("Laterite soil", "Laterite is found in the south and hilly north-east."), ("Black soil", "Black soil is in the Deccan."), ("Red and yellow soil", "Red soil is in the eastern and southern Deccan.")],
  "Alluvial soil was deposited by the Indus, Ganga and Brahmaputra.", "medium")
M("map3", SOIL, "Map work: which soil would you mark over western Rajasthan?",
  [("Arid soil", ""), ("Black soil", "Black soil is further south-east."), ("Laterite soil", "Laterite needs heavy rain."), ("Forest soil", "Forest soil is in the mountains.")],
  "Arid soil: sandy and saline, cultivable with irrigation.", "medium")
W("map4", "very_short_answer", SOIL, "Map work: name the soil found (a) in Kerala and the hilly areas of Odisha and Assam, and (b) in the eastern parts of the Deccan plateau and Odisha.",
  ["(a) Laterite soil.", "(b) Red and yellow soil."])
# ---------------- True / false ----------------
C.tf("tf1", RES, "Reserves are a subset of stock.", True, "Reserves can be used with existing technology, but their use has not started.")
C.tf("tf2", SOIL, "Bangar is new alluvium and is more fertile than khadar.", False, "Bangar is old alluvium with kanker nodules; khadar is new and more fertile.")
C.tf("tf3", LAND, "The National Forest Policy (1952) recommends 33 per cent of the geographical area under forest.", True, "This is considered essential to maintain the ecological balance.")
C.tf("tf4", EROS, "Ploughing up and down the slope helps to conserve soil.", False, "It forms channels for the quick flow of water and causes erosion; ploughing along contours conserves soil.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", DEV, "State any two problems caused by the indiscriminate use of resources.",
  ["Depletion of resources to satisfy the greed of a few individuals.", "Accumulation of resources in a few hands, dividing society into haves and have-nots; and global ecological crises like global warming and pollution."])
W("vsa2", "very_short_answer", DEV, "What were the two main decisions of the Rio de Janeiro Earth Summit (1992)?",
  ["Leaders signed the Declaration on Global Climatic Change and Biological Diversity and endorsed the global Forest Principles.", "They adopted Agenda 21 to achieve sustainable development, asking every local government to draw up its own local Agenda 21."])
W("vsa3", "very_short_answer", LAND, "Why is land use data available for only about 93 per cent of India's area?",
  ["Land use reporting for most north-east states except Assam has not been done fully.", "Some areas of Jammu and Kashmir occupied by Pakistan and China have not been surveyed."])
W("sa1", "short_answer", DEV, "Explain the three stages of resource planning in India.",
  ["Identification and inventory of resources across the regions of the country: surveying, mapping and qualitative and quantitative estimation.",
   "Evolving a planning structure endowed with appropriate technology, skill and institutional set-up for implementing the plans.",
   "Matching the resource development plans with the overall national development plans."])
W("sa2", "short_answer", LAND, "Suggest three ways to solve the problem of land degradation.",
  ["Afforestation, proper management of grazing and control on overgrazing.", "Planting shelter belts and stabilising sand dunes by growing thorny bushes.",
   "Proper management of wastelands, control of mining, and proper treatment and disposal of industrial effluents."])
W("sa3", "short_answer", SOIL, "Describe three features of laterite soil.",
  ["It develops under high temperature and heavy rainfall, as a result of intense leaching.", "It is low in humus because decomposers like bacteria are destroyed by high temperature.",
   "With manures and conservation methods it supports tea and coffee; red laterite in Tamil Nadu, Andhra Pradesh and Kerala suits cashew nut."])
W("la1", "long_answer", SOIL, "Describe the features and distribution of black soil and alluvial soil in India.",
  ["Alluvial soil covers the northern plains, deposited by the Indus, Ganga and Brahmaputra; it extends to Rajasthan and Gujarat and the eastern coast deltas.",
   "Alluvial soil consists of sand, silt and clay, is rich in potash, phosphoric acid and lime, and is divided into bangar (old) and khadar (new, more fertile); it suits sugarcane, paddy, wheat and pulses.",
   "Black (regur) soil is formed from the basalt lava of the Deccan trap and covers Maharashtra, Saurashtra, Malwa, Madhya Pradesh, Chhattisgarh and the Godavari and Krishna valleys.",
   "Black soil is clayey and holds moisture; it is rich in calcium carbonate, magnesium, potash and lime but poor in phosphorus; it is ideal for cotton.",
   "Black soil develops deep cracks in hot weather, which aerate it, and turns sticky when wet, so it must be tilled after the first shower or in the pre-monsoon period."])
W("la2", "long_answer", EROS, "What is soil erosion? Explain its causes and four methods of soil conservation.",
  ["Soil erosion is the denudation of the soil cover and its washing down; human activities upset the balance between soil formation and erosion.",
   "Causes: deforestation, overgrazing, construction, mining and defective farming such as ploughing up and down the slope; natural agents are water, wind and glaciers.",
   "Running water makes gullies and bad land (ravines in the Chambal basin); water also causes sheet erosion, and wind blows away loose soil.",
   "Contour ploughing and terrace cultivation (as in the western and central Himalayas) slow down water on slopes.",
   "Strip cropping and shelter belts break the force of wind; shelter belts have stabilised sand dunes in western India."])
W("cb1", "case_based", DEV, "Read the source and answer the questions.\n\n*\"In June 1992, more than 100 heads of states met in Rio de Janeiro in Brazil, for the first International Earth Summit. The Summit was convened for addressing urgent problems of environmental protection and socio-economic development at the global level.\"* (NCERT)\n\n"
  "(i) Why was the Earth Summit convened? (1)\n\n(ii) Name the agenda adopted at the summit. (1)\n\n(iii) Explain the main objective of this agenda and what it expects from local governments. (2)",
  ["(i) To address urgent problems of environmental protection and socio-economic development at the global level.", "(ii) Agenda 21.",
   "(iii) It aims to combat environmental damage, poverty and disease through global co-operation on common interests, mutual needs and shared responsibilities; every local government should draw up its own local Agenda 21."])
W("cb2", "case_based", SOIL, "Read the source and answer the questions.\n\n*\"Black soil is made up of extremely fine i.e. clayey material. It is well-known for its capacity to hold moisture. In addition, it is rich in soil nutrients, such as calcium carbonate, magnesium, potash and lime. This soil is generally poor in phosphoric contents. It develops deep cracks during hot weather, which helps in the proper aeration of the soil.\"* (NCERT)\n\n"
  "(i) Which crop is black soil best suited for? (1)\n\n(ii) Which nutrient is black soil poor in? (1)\n\n(iii) Why must black soil be tilled immediately after the first shower or during the pre-monsoon period? Give one more feature. (2)",
  ["(i) Cotton.", "(ii) Phosphoric content.",
   "(iii) It becomes sticky when wet and is difficult to work on, so it is tilled when just moist; it also develops deep cracks in hot weather, which help aeration."])
# ---------------- Assertion-reason ----------------
C.arq("ar1", RES, "Hydrogen in water is considered a stock.", "Humans do not yet have the advanced technology to use hydrogen as a source of energy.", 0,
      "R explains A.", "stock is material we cannot yet use.", "the technology is lacking.")
C.arq("ar2", DEV, "Resource planning is essential in India.", "India has enormous diversity in the availability of resources.", 0,
      "R explains A: some regions are rich in some resources and poor in others.", "planning ensures balanced use.", "Rajasthan, Arunachal and Ladakh differ greatly.")
C.arq("ar3", LAND, "Over-irrigation is a major cause of land degradation in Punjab and Haryana.", "Over-irrigation causes waterlogging, which increases salinity and alkalinity of the soil.", 0,
      "R explains A.", "the textbook names Punjab, Haryana and western UP.", "waterlogging leads to salinity.")
C.arq("ar4", SOIL, "Khadar is more fertile than bangar.", "Khadar has a higher concentration of kanker nodules.", 2,
      "A is true; R is false: bangar has more kanker nodules; khadar has more fine particles.", "khadar is new alluvium.", "kanker nodules are found in bangar.")
C.arq("ar5", SOIL, "Laterite soil is rich in humus.", "Laterite soil develops under high temperature and heavy rainfall.", 3,
      "A is false: laterite has low humus because heat destroys the decomposers. R is true.", "humus is low.", "it forms in hot, rainy areas.")
C.arq("ar6", EROS, "Contour ploughing helps to conserve soil on slopes.", "Ploughing along contour lines slows down the flow of water down the slope.", 0,
      "R explains A.", "it reduces erosion.", "slower water carries less soil.")

chapter = header(SUBJ, N, "Resources and Development", ["resource_types", "resource_planning", "land_resources", "soil_types", "soil_conservation"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: this chapter is fully in the board examination (Geography: 17 marks + 3 map marks). Map work from this chapter: major soil types (locating and labelling).")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
