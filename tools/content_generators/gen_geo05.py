"""CBSE Class 10 Geography Ch 5: Minerals and Energy Resources (fully in the 2025-26 board syllabus; map: mines, oil fields, power plants)."""
import sys
from ss_common import make, header, path, SQP, SHINE, CB

ROOT = sys.argv[1]
SUBJ, N = "geography", 5
PATH = path(SUBJ, "ch05_minerals_and_energy_resources")
C = make(SUBJ, N, "geo10ch05")
blk, M, W = C.blk, C.m, C.w
OCC, MET, CONS, CONV, NONC, MAP = ["mineral_occurrence"], ["metallic_nonmetallic"], ["mineral_conservation"], ["conventional_energy"], ["non_conventional_energy"], ["minerals_energy_map"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 5 exercises", "question": n}

IRON = ("| Iron ore belt | Key mines / facts |\n|---|---|\n| **Odisha-Jharkhand** | high-grade hematite at **Badampahar** (Mayurbhanj and Kendujhar, Odisha); Gua and Noamundi (Singhbhum, Jharkhand) |\n"
        "| **Durg-Bastar-Chandrapur** (Chhattisgarh, Maharashtra) | very high-grade hematite in the **Bailadila** hills of Bastar; 14 deposits; exported to Japan and South Korea via Visakhapatnam |\n"
        "| **Ballari-Chitradurga-Chikkamagaluru-Tumakuru** (Karnataka) | large reserves; **Kudremukh** in the Western Ghats is a 100% export unit; ore sent as slurry by pipeline to a port near Mangaluru |\n"
        "| **Maharashtra-Goa** | Goa and Ratnagiri; ore not of very high quality but efficiently exploited; exported through **Marmagao** |")
COAL = ("| Type of coal | Features |\n|---|---|\n| **Peat** | decaying plants in swamps; low carbon, high moisture, low heating capacity |\n"
        "| **Lignite** | low-grade brown coal, soft with high moisture; main reserves at **Neyveli** (Tamil Nadu), used for electricity |\n"
        "| **Bituminous** | buried deep and subjected to higher temperatures; most popular commercial coal; metallurgical coal is high-grade bituminous for smelting iron |\n"
        "| **Anthracite** | highest quality hard coal |")
MAPTAB = ("| Category | Places to locate |\n|---|---|\n| Iron ore mines | Mayurbhanj (Odisha), Durg and Bailadila (Chhattisgarh), Ballari and Kudremukh (Karnataka) |\n"
          "| Coal mines | Raniganj (West Bengal), Bokaro (Jharkhand), Talcher (Odisha), Neyveli (Tamil Nadu) |\n"
          "| Oil fields | Digboi and Naharkatia (Assam), Mumbai High and Bassien (offshore Maharashtra), Kalol and Ankaleshwar (Gujarat) |\n"
          "| Thermal power plants | Namrup (Assam), Singrauli (Uttar Pradesh–Madhya Pradesh border), Ramagundam (Telangana) |\n"
          "| Nuclear power plants | Narora (Uttar Pradesh), Kakrapara (Gujarat), Tarapur (Maharashtra), Kalpakkam (Tamil Nadu) |")

sections = [
 {"id": "s1", "title": "Treasures under our feet", "blocks": [
  blk("s1.hook", "hook", title="How many minerals did you use before breakfast?",
    body="Your toothpaste has calcium carbonate and fluoride. The steel spoon came from iron ore, the aluminium pan from bauxite, the wires in your house from copper, and the electricity from coal, water or the sun.\n\n"
         "Minerals are an indispensable part of our lives. But they take millions of years to form and we are using them up fast. This chapter explains how minerals occur, where India's main minerals are found, and how we get and save energy."),
  blk("s1.inspiration", "inspiration", title="The father of India's nuclear programme", person="Homi J. Bhabha", years="1909–1966",
    body="Physicist **Homi Jehangir Bhabha** saw that India had little uranium but large reserves of **thorium** in the monazite sands of Kerala. He planned a long-term programme to use thorium for nuclear power.\n\n"
         "He set up the Tata Institute of Fundamental Research and the Atomic Energy Establishment at Trombay (later renamed the Bhabha Atomic Research Centre). India's nuclear power stations, like **Tarapur**, grew from his vision.",
    future="This chapter leads to careers in geology, mining engineering, petroleum engineering, nuclear science and renewable energy."),
  C.socratic("s1.socratic", "Why must we conserve minerals even though India has large reserves of some of them?",
    ["They are finite and non-renewable, and take millions of years to form", "They grow back every year", "They are found only in India"], 0,
    "The rate of replenishment is infinitely small compared with our rate of consumption."),
 ]},
 {"id": "s2", "title": "What minerals are and how they occur", "blocks": [
  blk("s2.thm", "theory", title="Minerals and their modes of occurrence", revision=True,
    body="Geologists define a **mineral** as a **'homogenous, naturally occurring substance with a definable internal structure'**. Minerals are found in varied forms in nature, ranging from the **hardest diamond to the softest talc**. Rocks are combinations of homogenous substances called minerals.\n\n"
         "Minerals are usually found in **'ores'**: an accumulation of any mineral mixed with other elements. The mineral content of the ore must be in sufficient concentration to make its extraction commercially viable.\n\n"
         "**Modes of occurrence:**\n"
         "1. **In igneous and metamorphic rocks:** minerals occur in the **cracks, crevices, faults or joints**. Smaller occurrences are called **veins** and larger ones **lodes**. They form when minerals in liquid, molten or gaseous form are forced upward through cavities towards the surface, then cool and solidify. Major metallic minerals like **tin, copper, zinc and lead** are obtained from veins and lodes.\n"
         "2. **In sedimentary rocks:** minerals occur in **beds or layers**, formed by deposition, accumulation and concentration in horizontal strata. **Coal** and some forms of **iron ore** are concentrated after long periods under great heat and pressure. **Gypsum, potash salt and sodium salt** form as a result of **evaporation**, especially in arid regions.\n"
         "3. **By decomposition of surface rocks:** soluble constituents are removed, leaving a residual mass of weathered material containing ores. **Bauxite** is formed this way.\n"
         "4. **As alluvial deposits:** in the sands of valley floors and the base of hills; these are called **'placer deposits'** and generally contain minerals not corroded by water: **gold, silver, tin and platinum**.\n"
         "5. **In ocean waters:** most minerals in ocean water are too widely diffused to be of economic significance, but **common salt, magnesium and bromine** are largely derived from ocean waters. The ocean beds are rich in **manganese nodules**.\n\n"
         "**Rat-hole mining:** in parts of the north-east, like **Meghalaya** (Jowai and Cherrapunji), minerals are owned by individuals or communities. Coal is mined by family members in a **long, narrow tunnel** known as **'rat-hole' mining**."),
  C.kc("s2.check", "Gold, silver, tin and platinum found in the sands of valley floors are called:",
    [("Placer deposits", ""), ("Veins and lodes", "These occur in cracks of igneous and metamorphic rocks."), ("Manganese nodules", "These lie on the ocean bed."), ("Beds or layers", "These are in sedimentary rocks.")],
    "Placer deposits contain minerals not corroded by water."),
  C.kc("s2.check2", "Which mineral is formed by the decomposition of surface rocks?",
    [("Bauxite", ""), ("Coal", "Coal forms in sedimentary layers."), ("Copper", "Copper occurs in veins and lodes."), ("Gold", "Gold is found in placer deposits.")],
    "Soluble constituents are removed, leaving a residual mass rich in bauxite."),
 ]},
 {"id": "s3", "title": "India's minerals", "blocks": [
  blk("s3.thm", "theory", title="Ferrous, non-ferrous and non-metallic minerals", revision=True,
    body="**Ferrous minerals** account for about **three-fourths** of the total value of the production of metallic minerals, and provide a strong base for metallurgical industries.\n\n"
         "**Iron ore:** the basic mineral and the backbone of industrial development. India is rich in good-quality iron ores.\n"
         "- **Magnetite** is the **finest** iron ore, with a very high content of iron, **up to 70 per cent**; it has excellent magnetic qualities, especially valuable in the electrical industry.\n"
         "- **Hematite** is the most important industrial iron ore in terms of quantity used, with slightly lower iron content, **50 to 60 per cent**.\n"
         "- The major iron ore belts are listed in the table: Odisha-Jharkhand, Durg-Bastar-Chandrapur, Ballari-Chitradurga-Chikkamagaluru-Tumakuru and Maharashtra-Goa.\n\n"
         "**Manganese:** mainly used in the manufacture of **steel and ferro-manganese alloy**; nearly **10 kg of manganese** is required to make **one tonne of steel**. It is also used in bleaching powder, insecticides and paints.\n\n"
         "**Non-ferrous minerals:** India's reserves and production are not very satisfactory. These minerals, which include **copper, bauxite, lead, zinc and gold**, play a vital role in metallurgical, engineering and electrical industries.\n"
         "- **Copper:** India is **critically deficient** in copper. Being malleable, ductile and a good conductor, it is used in electrical cables, electronics and chemical industries. The **Balaghat** mines (Madhya Pradesh), the **Khetri** mines (Rajasthan) and **Singhbhum** (Jharkhand) are leading producers.\n"
         "- **Bauxite:** though several ores contain aluminium, it is from **bauxite**, a clay-like substance, that **alumina and later aluminium** are obtained. Bauxite deposits form by the decomposition of a wide variety of rocks rich in aluminium silicates. "
         "**Aluminium** combines the **strength** of metals such as iron with **extreme lightness**, and also has **good conductivity and great malleability**. India's bauxite deposits are mainly found in the **Amarkantak plateau, Maikal hills and the plateau region of Bilaspur-Katni**. "
         "**Odisha** was the **largest bauxite-producing state** in India (2016-17); the **Panchpatmali** deposits in **Koraput** district are the most important bauxite deposits in the state.\n\n"
         "**Non-metallic minerals:**\n"
         "- **Mica:** made up of a series of **plates or leaves**; it splits easily into thin sheets, which can be clear, black, green, red, yellow or brown. Due to its excellent **di-electric strength**, low power loss factor, **insulating properties** and resistance to high voltage, mica is one of the most indispensable minerals in **electric and electronic industries**. "
         "Mica deposits are found on the northern edge of the **Chota Nagpur plateau**; the **Koderma-Gaya-Hazaribagh** belt of Jharkhand is the leading producer. In Rajasthan, the major mica area is around **Ajmer**; the **Nellore** mica belt of Andhra Pradesh is also important.\n\n"
         "**Rock minerals:**\n"
         "- **Limestone:** found in association with rocks composed of **calcium carbonates or calcium and magnesium carbonates**, in sedimentary rocks of most geological formations. It is the **basic raw material for the cement industry** and essential for **smelting iron ore** in the blast furnace."),
  blk("s3.iron", "markdown_table", title="Iron ore belts of India", revision=True, body=IRON),
  C.kc("s3.check", "Which iron ore is the finest, with up to 70 per cent iron?",
    [("Magnetite", ""), ("Hematite", "Hematite has 50-60 per cent iron."), ("Bauxite", "Bauxite is the ore of aluminium."), ("Limonite", "The chapter names magnetite as the finest.")],
    "Magnetite also has excellent magnetic qualities."),
  C.kc("s3.check2", "Kudremukh iron ore mines are known for being:",
    [("a 100% export unit in the Western Ghats of Karnataka", ""), ("the main source of copper", "Copper comes from Balaghat and Khetri."), ("the largest coal field", "Kudremukh mines iron ore."), ("an oil field in Assam", "Kudremukh is in Karnataka.")],
    "The ore is sent as slurry through a pipeline to a port near Mangaluru."),
 ]},
 {"id": "s4", "title": "Mining hazards and conservation", "blocks": [
  blk("s4.thm", "theory", title="The cost of mining and how to save minerals", revision=True,
    body="**Hazards of mining:**\n- The **dust and noxious fumes** inhaled by miners make them vulnerable to **pulmonary (lung) diseases**.\n"
         "- The risk of **collapsing mine roofs, inundation and fires** in coal mines is a constant threat to miners.\n"
         "- **Water sources** in the region get **contaminated** due to mining.\n"
         "- **Dumping of waste and slurry** leads to **degradation of land and soil**, and an increase in **stream and river pollution**.\n"
         "Stricter safety regulations and implementation of environmental laws are essential to prevent mining from becoming a 'killer industry'.\n\n"
         "**Conservation of minerals:** all of us appreciate our strong dependence on minerals. Industry and agriculture depend upon mineral deposits and the substances made from them. But:\n"
         "- the total volume of workable mineral deposits is an **insignificant fraction (one per cent)** of the Earth's crust;\n"
         "- mineral resources are being consumed rapidly, while the geological processes of mineral formation are so **slow** that the rate of replenishment is **infinitely small** compared with present rates of consumption;\n"
         "- minerals are **finite and non-renewable**; continued extraction leads to **increasing costs** as mineral extraction comes from greater depths along with a **decrease in quality**.\n\n"
         "**How to conserve:** use mineral resources in a **planned and sustainable** manner; use **improved technologies** that allow low-grade ores to be used at low costs; **recycle metals**, use **scrap metals** and other **substitutes**."),
  C.kc("s4.check", "Which is a way to conserve minerals?",
    [("Recycling metals and using scrap and substitutes", ""), ("Mining from greater depths", "That raises costs and lowers quality."), ("Dumping slurry in rivers", "That pollutes rivers."), ("Using only high-grade ores", "Improved technology should let us use low-grade ores too.")],
    "Planned use, better technology for low-grade ores, recycling and substitutes conserve minerals."),
 ]},
 {"id": "s5", "title": "Conventional energy", "blocks": [
  blk("s5.thm", "theory", title="Coal, petroleum, natural gas and electricity", revision=True,
    body="Energy is needed to cook, to provide light and heat, to propel vehicles and to drive machinery in industries. It can be generated from fuel minerals like coal, petroleum, natural gas and uranium, and from electricity. "
         "Energy resources are classified as **conventional** (firewood, cattle dung cake, coal, petroleum, natural gas and electricity, both hydel and thermal) and **non-conventional** (solar, wind, tidal, geothermal, biogas and atomic energy). "
         "**Firewood and cattle dung cake** are most common in rural India; it is estimated that **more than 70 per cent** of the energy requirement in rural households is met by these two, but their use is becoming difficult due to decreasing forest area, and dung cake is better used as manure.\n\n"
         "**Coal:** the **most abundantly available fossil fuel** in India. It provides a substantial part of the nation's energy needs: for **power generation**, energy to **industry** and **domestic** needs. India is highly dependent on coal for meeting its **commercial energy** requirements. "
         "Coal is formed by the **compression of plant material** over millions of years, and is found in a variety of forms depending on the degree of compression and the depth and time of burial (see the table).\n"
         "- In India coal occurs in rock series of two main geological ages: **Gondwana**, a little over **200 million years** old, and **tertiary** deposits about **55 million years** old.\n"
         "- The major resources of **Gondwana coal** (metallurgical coal) are in the **Damodar valley** (West Bengal-Jharkhand); **Jharia, Raniganj and Bokaro** are important coalfields. The **Godavari, Mahanadi, Son and Wardha** valleys also contain coal deposits.\n"
         "- **Tertiary coals** occur in the north-eastern states of **Meghalaya, Assam, Arunachal Pradesh and Nagaland**.\n"
         "- Coal is a **bulky material**, which loses weight on use as it is reduced to ash. So heavy industries and thermal power stations are located **on or near the coalfields**.\n\n"
         "**Petroleum (mineral oil):** the next major energy source after coal. It provides fuel for heat and lighting, lubricants for machinery and raw materials for many manufacturing industries. **Petroleum refineries** act as a **'nodal industry'** for synthetic textile, fertiliser and numerous chemical industries.\n"
         "- Most petroleum occurrences in India are associated with **anticlines and fault traps** in rock formations of the **tertiary age**. In regions of folding, anticlines or domes, oil is trapped in the crest of the upfold. The oil-bearing layer is a **porous limestone or sandstone** through which oil may flow; it is prevented from rising or sinking by intervening **non-porous layers**. "
         "Petroleum is also found in **fault traps** between porous and non-porous rocks. **Gas**, being lighter, usually occurs **above the oil**.\n"
         "- **Mumbai High, Gujarat and Assam** are the major petroleum-producing areas. **Ankleshwar** is the most important field of Gujarat. **Assam** is the **oldest** oil-producing state; **Digboi, Naharkatia and Moran-Hugrijan** are its important oil fields.\n\n"
         "**Natural gas:** an important **clean energy** resource, found in association with or without petroleum. It is used as a source of energy and as an industrial raw material in the **petrochemical** industry. It is considered an **environment-friendly fuel** because of **low carbon dioxide emissions**. "
         "Large reserves have been discovered in the **Krishna-Godavari basin**; along the west coast, the reserves of **Mumbai High** and allied fields are supplemented by finds in the **Gulf of Cambay**; the **Andaman and Nicobar Islands** are also important. "
         "The **power and fertiliser** industries are the key users of natural gas; the use of **CNG (compressed natural gas)** for vehicles is gaining popularity.\n\n"
         "**Electricity:** generated mainly in two ways: by **running water** which drives hydro turbines (**hydroelectricity**), and by **burning fuels** such as coal, petroleum and natural gas to drive turbines (**thermal power**).\n"
         "- **Hydroelectricity** is generated by fast-flowing water, a **renewable** resource. India has a number of multipurpose projects like **Bhakra Nangal, Damodar Valley Corporation and the Kopili Hydel Project**.\n"
         "- **Thermal electricity** is generated using coal, petroleum and natural gas; thermal power stations use **non-renewable** fossil fuels."),
  blk("s5.coal", "markdown_table", title="Types of coal", revision=True, body=COAL),
  C.kc("s5.check", "Why are thermal power stations located on or near coalfields?",
    [("Coal is bulky and loses weight on use as it turns to ash", ""), ("Coal is very light", "Coal is bulky."), ("Coal cannot be transported at all", "It can, but it is costly to move."), ("Coalfields have the most rain", "Rain is not the reason.")],
    "Moving bulky coal is costly, so plants are built near the mines."),
  C.kc("s5.check2", "Which is the oldest oil-producing state of India?",
    [("Assam", ""), ("Gujarat", "Gujarat's main field is Ankleshwar."), ("Maharashtra", "Mumbai High is offshore Maharashtra but not the oldest."), ("Rajasthan", "The chapter names Assam.")],
    "Digboi, Naharkatia and Moran-Hugrijan are Assam's important fields."),
 ]},
 {"id": "s6", "title": "Non-conventional energy and conservation", "blocks": [
  blk("s6.thm", "theory", title="Nuclear, solar, wind, biogas, tidal and geothermal", revision=True,
    body="The growing consumption of energy has made India increasingly dependent on fossil fuels. Rising prices of oil and gas and their potential shortages have raised uncertainties about the security of energy supply, with serious repercussions on economic growth. Increasing use of fossil fuels also causes serious environmental problems. So there is a pressing need to use **renewable energy** sources.\n\n"
         "- **Nuclear or atomic energy:** obtained by **altering the structure of atoms**; when such an alteration is made, much energy is released as heat, which is used to generate electricity. **Uranium and thorium**, available in **Jharkhand** and the **Aravalli ranges of Rajasthan**, are used for generating atomic or nuclear power. The **monazite sands of Kerala** are also rich in **thorium**.\n"
         "- **Solar energy:** India is a tropical country with enormous possibilities of tapping solar energy. **Photovoltaic technology** converts sunlight directly into electricity. One of the largest solar plants is near **Bhuj** (at Madhapur), where solar energy is used to **sterilise milk cans**. Solar energy can reduce the dependence of rural households on firewood and dung cakes, leaving more manure for agriculture.\n"
         "- **Wind power:** India now ranks as a 'wind super power' in the world. The largest wind farm cluster is located in **Tamil Nadu from Nagarcoil to Madurai**; Andhra Pradesh, Karnataka, Gujarat, Kerala, Maharashtra and Lakshadweep also have important wind farms. **Nagarcoil and Jaisalmer** are well known for the effective use of wind energy.\n"
         "- **Biogas:** shrubs, farm waste, animal and human waste are used to produce biogas for domestic consumption in rural areas. Decomposition of organic matter yields gas with **higher thermal efficiency** than kerosene, dung cake and charcoal. Plants using cattle dung are known as **'Gobar gas plants'**. "
         "They provide **twin benefits** to the farmer: **energy** and **improved quality of manure**. Biogas is the most efficient use of cattle dung; it improves the quality of manure and prevents the loss of trees and manure due to burning of fuel wood and cow dung cakes.\n"
         "- **Tidal energy:** oceanic tides can be used to generate electricity. **Floodgate dams** are built across inlets. During high tide, water flows into the inlet and gets trapped when the gate is closed. After the tide falls outside the floodgate, the water retained flows back to the sea via a pipe that carries it through a **power-generating turbine**. "
         "In India, the **Gulf of Khambhat, the Gulf of Kachchh** in Gujarat on the western coast, and the **Gangetic delta in the Sunderban** region of West Bengal provide ideal conditions.\n"
         "- **Geothermal energy:** heat and electricity produced by using the **heat from the interior of the Earth**. Temperature increases with depth; where the geothermal gradient is high, high temperatures are found at shallow depths, and groundwater absorbs heat from the rocks and rises to the surface as **hot springs**. "
         "Two experimental projects have been set up: one in the **Parvati valley near Manikarn** in **Himachal Pradesh** and the other in the **Puga Valley, Ladakh**.\n\n"
         "**Conservation of energy:** energy is a basic requirement for economic development. We need a cautious approach to the judicious use of limited energy resources. As concerned citizens we can: use **public transport** instead of individual vehicles; **switch off** electricity when not in use; use **power-saving devices**; and use **non-conventional sources** of energy. "
         "After all, **'energy saved is energy produced'**."),
  blk("s6.map", "markdown_table", title="Map list: mines, oil fields and power plants (2025-26)", revision=True, body=MAPTAB),
  C.kc("s6.check", "Where are India's two experimental geothermal projects?",
    [("Parvati valley near Manikarn (Himachal Pradesh) and Puga Valley (Ladakh)", ""), ("Gulf of Khambhat and Gulf of Kachchh", "These are tidal energy sites."),
     ("Nagarcoil and Jaisalmer", "These are known for wind energy."), ("Bhuj and Madhapur", "These are linked to solar energy.")],
    "Geothermal energy uses heat from the Earth's interior."),
  C.kc("s6.check2", "What are the twin benefits of gobar gas plants to farmers?",
    [("Energy and improved quality of manure", ""), ("Timber and fodder", "Biogas does not produce these."), ("Petrol and diesel", "Biogas is not a petroleum product."), ("Electricity from tides and heat from rocks", "Those are tidal and geothermal energy.")],
    "Biogas is the most efficient use of cattle dung."),
 ]},
 {"id": "s7", "title": "Remember, avoid, practise", "blocks": [
  blk("s7.memory", "memory_trick", title="Memory tricks",
    body="- **Five modes of occurrence: \"Very Bright Diamonds Please Others\"** = Veins/lodes (igneous), Beds (sedimentary), Decomposition (bauxite), Placer (alluvial), Ocean (salt, magnesium, bromine).\n"
         "- **Iron ore: \"MAGnetite = MAGnificent, 70%\"; hematite 50-60%.**\n- **Coal ladder (worst to best): Peat → Lignite → Bituminous → Anthracite (\"Please Let Better Arrive\").**\n"
         "- **Oil in Assam: \"Digboi Never Misses\"** = Digboi, Naharkatia, Moran-Hugrijan.\n- **Geothermal = Parvati + Puga; Tidal = Khambhat, Kachchh, Sunderban.**\n"
         "- **Nuclear plants on the map: \"No Kid Taps Kettles\"** = Narora, Kakrapara, Tarapur, Kalpakkam."),
  blk("s7.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying hematite is the finest ore: **magnetite** is finest (up to 70%); hematite is the most used.\n2. Calling bauxite a placer deposit: it forms by **decomposition of surface rocks**.\n"
         "3. Saying lignite is the best coal: **anthracite** is the highest quality; lignite is low-grade brown coal.\n4. Saying gas lies below oil: gas, being lighter, usually occurs **above** the oil.\n"
         "5. Mixing up Gondwana coal (about 200 million years, Damodar valley) and tertiary coal (about 55 million years, north-east).\n6. Calling thermal power renewable: it uses **non-renewable** fossil fuels; hydel power is renewable."),
  blk("s7.tip", "teacher_tip", title="Try this in class",
    body="Make a 'mineral treasure hunt': students list ten objects at home and find the mineral in each (iron, aluminium, copper, mica, limestone). "
         "Then give outline maps and ask them to mark the five iron mines, four coal mines, six oil fields and seven power plants from the map list."),
  blk("s7.reflection", "reflection", title="Think and explain",
    body="'Energy saved is energy produced.' List three ways your family can save energy this week, and say which energy source each one saves."),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 1:** minerals are non-renewable resources; mining causes land degradation.\n- **Chapter 2:** mining threatens forests like Buxa.\n"
         "- **Chapter 6 (Manufacturing):** iron and steel, aluminium and cement industries use these minerals.\n- **Chapter 7 (Lifelines):** pipelines carry oil and gas; ports export iron ore."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="'Coal is the most important and abundant fossil fuel in India.' Justify with its uses and types (2025-26 sample paper idea), in about 120 words.\n\n"
         "**Model answer:** Coal is the most abundantly available fossil fuel in India and provides a substantial part of the nation's energy needs. It is used for power generation, to supply energy to industry and for domestic needs; India is highly dependent on coal for its commercial energy, for example in metallurgy. "
         "Coal is found in different forms depending on compression, depth and time of burial: peat has low carbon and high moisture with low heating capacity; lignite is a low-grade brown coal mined at Neyveli and used for electricity; bituminous coal is the most popular commercial coal, and its high-grade metallurgical form is used to smelt iron in blast furnaces; anthracite is the highest-quality hard coal. "
         "Major fields like Jharia, Raniganj and Bokaro support heavy industries and thermal power plants."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- A mineral is a homogenous, naturally occurring substance with a definable internal structure; minerals occur in veins and lodes, beds, residual deposits, placer deposits and ocean waters.\n"
         "- Ferrous minerals: iron ore (magnetite, hematite; four belts) and manganese. Non-ferrous: copper (Balaghat, Khetri), bauxite (Amarkantak, Maikal, Koraput). Non-metallic: mica (Koderma-Gaya-Hazaribagh). Rock minerals: limestone.\n"
         "- Mining harms miners' health and the environment; minerals must be conserved through planned use, technology, recycling and substitutes.\n"
         "- Conventional energy: coal (Gondwana, tertiary), petroleum (Mumbai High, Gujarat, Assam), natural gas (Krishna-Godavari, Mumbai High) and electricity (hydel, thermal).\n"
         "- Non-conventional energy: nuclear, solar, wind, biogas, tidal and geothermal; energy saved is energy produced."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- The 2025-26 sample paper asked why setting up a bauxite industry in Odisha is advisable (Panchpatmali in Koraput; aluminium's strength, lightness, conductivity and malleability) and, as an alternative, why coal is the most important fossil fuel (uses and types).\n"
         "- 3/5-mark favourites: modes of occurrence, iron ore belts, hazards of mining, conservation, coal, petroleum traps, non-conventional energy.\n"
         "- **Map work:** iron ore mines, coal mines, oil fields, thermal and nuclear power plants (see the map list table)."),
  blk("s7.flash1", "flashcard", front="What is a mineral?", back="A homogenous, naturally occurring substance with a definable internal structure."),
  blk("s7.flash2", "flashcard", front="Why does gas usually occur above oil?", back="Gas is lighter than oil, so it collects above it in anticlines and fault traps."),
  blk("s7.flash3", "flashcard", front="Name the four types of coal from lowest to highest quality.", back="Peat, lignite, bituminous, anthracite."),
  blk("s7.flash4", "flashcard", front="How does tidal energy work?", back="Floodgate dams trap water at high tide; when the tide falls, the water flows back through a turbine to generate electricity."),
 ]},
]

# ---------------- Sample paper ----------------
W("sqp17a", "long_answer", MET, "Person P is willing to establish a mineral based industry. He has been advised to set up a bauxite industry in Odisha as a suitable way to make a profitable venture. Analyse the possible reasons behind the advice given.",
  ["Odisha was the largest bauxite-producing state in India (2016-17), so raw material is readily available.",
   "The Panchpatmali deposits in Koraput district are the most important bauxite deposits in the state.",
   "Aluminium, made from bauxite, is an important metal because it combines the strength of metals such as iron,",
   "with extreme lightness, making it a good alternative to other metals,",
   "and it also has good conductivity and great malleability, so demand for it is high."], source=SQP("17A"))
W("sqp17b", "long_answer", CONV, "'Coal is the most important and abundant fossil fuel in India.' Justify the statement by evaluating the significant role it plays in the growth of the Indian economy in its different forms.",
  ["Coal is used for power generation and to supply energy to industry as well as for domestic needs; India is highly dependent on coal for commercial energy, e.g. in metallurgy.",
   "Peat: decaying plants in swamps; low carbon, high moisture and low heating capacity.",
   "Lignite: low-grade brown coal, soft with high moisture; main reserves at Neyveli (Tamil Nadu), used to generate electricity.",
   "Bituminous: coal buried deep and subjected to higher temperatures; the most popular commercial coal; metallurgical coal is high-grade bituminous used to smelt iron in blast furnaces.",
   "Anthracite: the highest quality hard coal."], ["Significance (at least two uses): 2 marks", "Types of coal: 3 marks"], source=SQP("17B"))

# ---------------- NCERT exercises ----------------
M("ex1i", OCC, "Which one of the following minerals is formed by decomposition of rocks, leaving a residual mass of weathered material?",
  [("coal", "Coal forms in sedimentary layers."), ("bauxite", ""), ("gold", "Gold is found in placer deposits."), ("zinc", "Zinc occurs in veins and lodes.")],
  "Bauxite forms when soluble constituents of surface rocks are removed.", "easy", ex("1(i)"), correct=1)
M("ex1ii", MET, "Koderma, in Jharkhand is the leading producer of which one of the following minerals?",
  [("bauxite", "Bauxite comes from Amarkantak, Maikal and Koraput."), ("mica", ""), ("iron ore", "Iron ore comes from belts like Odisha-Jharkhand."), ("copper", "Copper comes from Balaghat, Khetri and Singhbhum.")],
  "The Koderma-Gaya-Hazaribagh belt leads in mica.", "easy", ex("1(ii)"), correct=1)
M("ex1iii", OCC, "Minerals are deposited and accumulated in the strata of which of the following rocks?",
  [("sedimentary rocks", ""), ("metamorphic rocks", "Minerals there occur in cracks and crevices."), ("igneous rocks", "Minerals there occur in veins and lodes."), ("none of the above", "Sedimentary rocks have beds or layers.")],
  "In sedimentary rocks minerals occur in beds or layers.", "easy", ex("1(iii)"), correct=0)
M("ex1iv", NONC, "Which one of the following minerals is contained in the Monazite sand?",
  [("oil", "Oil is found in anticlines."), ("uranium", "Uranium is in Jharkhand and the Aravallis."), ("thorium", ""), ("coal", "Coal is in sedimentary rocks.")],
  "The monazite sands of Kerala are rich in thorium.", "easy", ex("1(iv)"), correct=2)
W("ex2i", "short_answer", MET, "Distinguish between ferrous and non-ferrous minerals. Give examples.",
  ["Ferrous minerals contain iron, e.g. iron ore and manganese; they account for about three-fourths of the value of metallic mineral production.",
   "Non-ferrous minerals do not contain iron, e.g. copper, bauxite, lead, zinc and gold.",
   "India is rich in ferrous minerals, but its reserves and production of non-ferrous minerals are not very satisfactory."], source=ex("2(i)"))
W("ex2ii", "short_answer", CONV, "Distinguish between conventional and non-conventional sources of energy.",
  ["Conventional sources have been used for a long time: firewood, cattle dung cake, coal, petroleum, natural gas and electricity (hydel and thermal).",
   "Non-conventional sources are newer: solar, wind, tidal, geothermal, biogas and atomic energy.",
   "Most conventional sources (fossil fuels) are non-renewable and polluting; most non-conventional sources are renewable and cleaner."], source=ex("2(ii)"))
W("ex3i", "long_answer", CONS, "Why do we need to conserve mineral resources?",
  ["Workable mineral deposits are an insignificant fraction (one per cent) of the Earth's crust.",
   "Geological processes of mineral formation are so slow that the rate of replenishment is infinitely small compared with consumption.",
   "Minerals are finite and non-renewable; rich deposits are being used up fast.",
   "Continued extraction raises costs as minerals come from greater depths with lower quality.",
   "So we must use minerals in a planned and sustainable way, use technology for low-grade ores, and recycle metals and use scrap and substitutes."], source=ex("3(i)"))
W("ex3ii", "long_answer", NONC, "Describe the distribution of non-conventional energy resources in India.",
  ["Nuclear: uranium and thorium in Jharkhand and the Aravallis of Rajasthan; thorium in the monazite sands of Kerala; plants at Narora, Kakrapara, Tarapur and Kalpakkam.",
   "Solar: India is tropical; one of the largest solar plants is near Bhuj (Madhapur), where it sterilises milk cans.",
   "Wind: the largest cluster is from Nagarcoil to Madurai in Tamil Nadu; also Andhra Pradesh, Karnataka, Gujarat, Kerala, Maharashtra and Lakshadweep; Jaisalmer is well known.",
   "Biogas: gobar gas plants in rural areas at municipal, co-operative and individual levels.",
   "Tidal: Gulf of Khambhat and Gulf of Kachchh (Gujarat) and the Sunderban delta (West Bengal); geothermal: Parvati valley (Himachal Pradesh) and Puga Valley (Ladakh)."], source=ex("3(ii)"))

# ---------------- MCQs ----------------
M("mcq01", OCC, "Which is the hardest mineral?",
  [("Diamond", ""), ("Talc", "Talc is the softest."), ("Mica", "Mica splits into sheets."), ("Limestone", "Limestone is a rock mineral.")], "Minerals range from the hardest diamond to the softest talc.")
M("mcq02", OCC, "An ore is:",
  [("an accumulation of a mineral mixed with other elements, rich enough to mine profitably", ""), ("any rock", "Not every rock is an ore."), ("a pure metal", "Ores contain minerals mixed with other elements."), ("a fossil fuel", "Fossil fuels are energy minerals.")], "The concentration must make extraction commercially viable.")
M("mcq03", OCC, "Small occurrences of minerals in the cracks of igneous rocks are called:",
  [("veins", ""), ("lodes", "Lodes are larger occurrences."), ("beds", "Beds are layers in sedimentary rocks."), ("placers", "Placers are alluvial deposits.")], "Tin, copper, zinc and lead come from veins and lodes.")
M("mcq04", OCC, "Which minerals form by evaporation, especially in arid regions?",
  [("Gypsum, potash salt and sodium salt", ""), ("Gold and platinum", "These are placer deposits."), ("Tin and copper", "These occur in veins and lodes."), ("Bauxite", "Bauxite forms by decomposition.")], "They form in sedimentary rocks.")
M("mcq05", OCC, "Which minerals are largely derived from ocean waters?",
  [("Common salt, magnesium and bromine", ""), ("Iron and manganese", "Manganese nodules lie on the ocean bed, but iron comes from land."), ("Coal and petroleum", "These are fossil fuels on land and offshore rocks."), ("Mica and limestone", "These come from rocks.")], "Ocean beds are also rich in manganese nodules.")
M("mcq06", OCC, "'Rat-hole' mining is practised in:",
  [("Meghalaya", ""), ("Jharkhand", "The chapter names Meghalaya."), ("Goa", "Goa mines iron ore."), ("Rajasthan", "The chapter names Meghalaya.")], "Coal is dug by family members through long, narrow tunnels.")
M("mcq07", MET, "Ferrous minerals account for what share of the value of metallic mineral production?",
  [("About three-fourths", ""), ("About one-tenth", "It is much more."), ("About half", "It is about three-fourths."), ("All of it", "Non-ferrous minerals also count.")], "They support metallurgical industries.")
M("mcq08", MET, "Hematite contains about:",
  [("50-60 per cent iron", ""), ("up to 70 per cent iron", "That is magnetite."), ("10 per cent iron", "Hematite is much richer."), ("100 per cent iron", "No ore is pure iron.")], "Hematite is the most used industrial iron ore.")
M("mcq09", MET, "Badampahar mines, with high-grade hematite, are in:",
  [("Mayurbhanj and Kendujhar districts of Odisha", ""), ("Bastar district of Chhattisgarh", "That is Bailadila."), ("Western Ghats of Karnataka", "That is Kudremukh."), ("Goa", "Goa is in the Maharashtra-Goa belt.")], "They belong to the Odisha-Jharkhand belt.")
M("mcq10", MET, "Iron ore from the Bailadila hills is exported to Japan and South Korea through:",
  [("Visakhapatnam port", ""), ("Marmagao port", "Marmagao exports Goa's ore."), ("Mangaluru port", "That takes Kudremukh ore."), ("Kandla port", "The chapter names Visakhapatnam.")], "Bailadila has 14 deposits of super high-grade hematite.")
M("mcq11", MET, "Iron ore of the Maharashtra-Goa belt is exported through:",
  [("Marmagao port", ""), ("Visakhapatnam port", "That exports Bailadila ore."), ("Paradip port", "Not named for Goa ore."), ("Kolkata port", "Not named for Goa ore.")], "Goa's ore is not very high quality but efficiently exploited.")
M("mcq12", MET, "About how much manganese is needed to make one tonne of steel?",
  [("10 kg", ""), ("1 kg", "It is about 10 kg."), ("100 kg", "It is about 10 kg."), ("1 tonne", "It is about 10 kg.")], "Manganese is used in steel and ferro-manganese alloy.")
M("mcq13", MET, "In which mineral is India critically deficient?",
  [("Copper", ""), ("Iron ore", "India is rich in iron ore."), ("Mica", "India has large mica reserves."), ("Coal", "Coal is abundant.")], "Copper comes from Balaghat, Khetri and Singhbhum.")
M("mcq14", MET, "The Khetri copper mines are in:",
  [("Rajasthan", ""), ("Madhya Pradesh", "Balaghat is in Madhya Pradesh."), ("Jharkhand", "Singhbhum is in Jharkhand."), ("Odisha", "Odisha is known for bauxite.")], "Copper is malleable, ductile and a good conductor.")
M("mcq15", MET, "Which is NOT a property of aluminium?",
  [("Very heavy weight", ""), ("Strength like iron", "This is a property."), ("Good conductivity", "This is a property."), ("Great malleability", "This is a property.")], "Aluminium is extremely light.")
M("mcq16", MET, "India's bauxite deposits are mainly in:",
  [("the Amarkantak plateau, Maikal hills and the Bilaspur-Katni plateau", ""), ("the Thar desert", "Not a bauxite area."), ("the Ganga plains", "Plains are alluvial."), ("the Himalayas", "Not named for bauxite.")], "Odisha's Panchpatmali deposits (Koraput) are also important.")
M("mcq17", MET, "The most important bauxite deposits of Odisha are at:",
  [("Panchpatmali, Koraput district", ""), ("Badampahar", "Badampahar has iron ore."), ("Talcher", "Talcher has coal."), ("Kendujhar", "Kendujhar has iron ore.")], "Odisha was the largest bauxite producer (2016-17).")
M("mcq18", MET, "Mica is indispensable in electrical industries because of its:",
  [("di-electric strength, insulating properties and resistance to high voltage", ""), ("magnetic quality", "That is magnetite."), ("heavy weight", "Mica splits into thin sheets."), ("high carbon content", "That describes anthracite coal.")], "It splits easily into thin sheets.")
M("mcq19", MET, "In Rajasthan, the major mica area is around:",
  [("Ajmer", ""), ("Khetri", "Khetri has copper."), ("Jaisalmer", "Jaisalmer is known for wind energy."), ("Kota", "The chapter names Ajmer.")], "Nellore (Andhra Pradesh) is another mica belt.")
M("mcq20", MET, "Limestone is the basic raw material for:",
  [("the cement industry", ""), ("the aluminium industry", "That uses bauxite."), ("the electrical industry", "That uses mica and copper."), ("the jute industry", "That uses jute.")], "It is also used to smelt iron ore in blast furnaces.")
M("mcq21", CONS, "Miners inhaling dust and noxious fumes are vulnerable to:",
  [("pulmonary diseases", ""), ("malaria", "Not caused by dust."), ("broken bones only", "The chapter names lung diseases."), ("eye colour change", "Not a mining hazard.")], "Mining is a hazardous industry.")
M("mcq22", CONS, "Workable mineral deposits make up what fraction of the Earth's crust?",
  [("About one per cent", ""), ("About 50 per cent", "It is insignificant."), ("About 25 per cent", "It is about one per cent."), ("About 10 per cent", "It is about one per cent.")], "That is why minerals must be conserved.")
M("mcq23", CONV, "More than 70 per cent of energy in rural households comes from:",
  [("firewood and cattle dung cake", ""), ("solar panels", "Not yet the main source."), ("petrol", "Not the main rural source."), ("nuclear energy", "Not a household source.")], "Dung cake is better used as manure.")
M("mcq24", CONV, "Which coal is the highest quality hard coal?",
  [("Anthracite", ""), ("Lignite", "Lignite is low-grade brown coal."), ("Peat", "Peat has low carbon."), ("Bituminous", "Bituminous is the most popular, but anthracite is the highest quality.")], "Anthracite is the best coal.")
M("mcq25", CONV, "The principal lignite reserves of India are at:",
  [("Neyveli", ""), ("Jharia", "Jharia has Gondwana coal."), ("Raniganj", "Raniganj has Gondwana coal."), ("Digboi", "Digboi is an oil field.")], "Neyveli lignite is used for electricity.")
M("mcq26", CONV, "Gondwana coal is about:",
  [("a little over 200 million years old", ""), ("55 million years old", "That is tertiary coal."), ("1,000 years old", "Coal takes millions of years."), ("5 million years old", "It is about 200 million years.")], "It is found in the Damodar valley.")
M("mcq27", CONV, "Tertiary coal occurs in:",
  [("Meghalaya, Assam, Arunachal Pradesh and Nagaland", ""), ("the Damodar valley", "That has Gondwana coal."), ("Neyveli", "Neyveli has lignite."), ("Kerala", "Not named for coal.")], "Tertiary coal is about 55 million years old.")
M("mcq28", CONV, "Which is NOT a coalfield of the Damodar valley?",
  [("Digboi", ""), ("Jharia", "Jharia is a Damodar coalfield."), ("Raniganj", "Raniganj is a Damodar coalfield."), ("Bokaro", "Bokaro is a Damodar coalfield.")], "Digboi is an oil field in Assam.")
M("mcq29", CONV, "Petroleum refineries act as a nodal industry for:",
  [("synthetic textile, fertiliser and chemical industries", ""), ("cotton textile only", "Cotton uses raw cotton."), ("sugar mills", "Sugar uses sugarcane."), ("handloom", "Handloom does not depend on refineries.")], "Refinery products are raw materials for many industries.")
M("mcq30", CONV, "Most of India's petroleum occurs in:",
  [("anticlines and fault traps in tertiary rocks", ""), ("Gondwana coal beds", "That is coal."), ("placer deposits", "Those hold gold and tin."), ("veins and lodes", "Those hold metals.")], "Oil collects in porous limestone or sandstone layers.")
M("mcq31", CONV, "The most important oil field of Gujarat is:",
  [("Ankleshwar", ""), ("Digboi", "Digboi is in Assam."), ("Naharkatia", "Naharkatia is in Assam."), ("Mumbai High", "Mumbai High is offshore Maharashtra.")], "Kalol is another field in Gujarat.")
M("mcq32", CONV, "Natural gas is considered environment-friendly because of:",
  [("low carbon dioxide emissions", ""), ("high smoke", "It burns cleaner."), ("being renewable", "It is a fossil fuel."), ("producing ash", "Coal produces ash.")], "It is a clean energy resource.")
M("mcq33", CONV, "Large reserves of natural gas have been found in the:",
  [("Krishna-Godavari basin", ""), ("Thar desert", "Not named."), ("Damodar valley", "That has coal."), ("Western Ghats", "Not named.")], "Mumbai High, the Gulf of Cambay and the Andaman and Nicobar Islands also have gas.")
M("mcq34", CONV, "Which is a multipurpose hydel project named in the chapter?",
  [("Kopili Hydel Project", ""), ("Tarapur", "Tarapur is nuclear."), ("Singrauli", "Singrauli is thermal."), ("Neyveli", "Neyveli is a lignite plant.")], "Bhakra Nangal and Damodar Valley Corporation are others.")
M("mcq35", NONC, "Uranium and thorium are available in:",
  [("Jharkhand and the Aravalli ranges of Rajasthan", ""), ("Punjab and Haryana", "Not named."), ("Goa", "Goa has iron ore."), ("Assam", "Assam has oil.")], "Monazite sands of Kerala are rich in thorium.")
M("mcq36", NONC, "Near Bhuj, solar energy is used to:",
  [("sterilise milk cans", ""), ("smelt iron", "That needs coal."), ("run ships", "Not mentioned."), ("make cement", "Not mentioned.")], "It is one of the largest solar plants (Madhapur).")
M("mcq37", NONC, "The largest wind farm cluster in India is in:",
  [("Tamil Nadu, from Nagarcoil to Madurai", ""), ("Punjab", "Not named."), ("Bihar", "Not named."), ("Uttar Pradesh", "Not named.")], "Jaisalmer is also known for wind energy.")
M("mcq38", NONC, "Which place provides ideal conditions for tidal energy?",
  [("Gulf of Khambhat", ""), ("Puga Valley", "That is geothermal."), ("Manikarn", "That is geothermal."), ("Neyveli", "That is lignite.")], "Also the Gulf of Kachchh and the Sunderban delta.")
M("mcq39", NONC, "Geothermal energy comes from:",
  [("heat from the interior of the Earth", ""), ("ocean tides", "That is tidal energy."), ("cattle dung", "That is biogas."), ("sunlight", "That is solar energy.")], "Hot springs show this heat at the surface.")
M("mcq40", NONC, "Which is NOT a way to conserve energy?",
  [("Leaving lights on when not in use", ""), ("Using public transport", "This conserves energy."), ("Using power-saving devices", "This conserves energy."), ("Using non-conventional energy", "This conserves fossil fuels.")], "Energy saved is energy produced.")
# ---------------- Map work ----------------
M("map1", MAP, "Map work: Kudremukh and Ballari iron ore mines are in:",
  [("Karnataka", ""), ("Odisha", "Mayurbhanj is in Odisha."), ("Chhattisgarh", "Durg and Bailadila are in Chhattisgarh."), ("Goa", "Goa is a separate belt.")], "Both are in Karnataka.", "medium")
M("map2", MAP, "Map work: the Talcher coal field is in:",
  [("Odisha", ""), ("West Bengal", "Raniganj is in West Bengal."), ("Jharkhand", "Bokaro is in Jharkhand."), ("Tamil Nadu", "Neyveli is in Tamil Nadu.")], "Talcher is in Odisha.", "medium")
M("map3", MAP, "Map work: Kalol and Ankleshwar oil fields are in:",
  [("Gujarat", ""), ("Assam", "Digboi and Naharkatia are in Assam."), ("Maharashtra", "Mumbai High and Bassien are offshore Maharashtra."), ("Rajasthan", "Not on the map list.")], "Both are in Gujarat.", "medium")
M("map4", MAP, "Map work: which is a nuclear power plant on the map list?",
  [("Kakrapara", ""), ("Namrup", "Namrup is thermal (Assam)."), ("Ramagundam", "Ramagundam is thermal (Telangana)."), ("Singrauli", "Singrauli is thermal.")], "Narora, Kakrapara, Tarapur and Kalpakkam are nuclear.", "medium")
W("map5", "very_short_answer", MAP, "Map work: name the states of (a) the Namrup thermal power plant and (b) the Kalpakkam nuclear power plant.",
  ["(a) Assam.", "(b) Tamil Nadu."])
W("map6", "very_short_answer", MAP, "Map work: name two oil fields of Assam and two iron ore mines of Chhattisgarh.",
  ["Oil fields of Assam: Digboi and Naharkatia.", "Iron ore mines of Chhattisgarh: Durg and Bailadila."])
# ---------------- True / false ----------------
C.tf("tf1", MET, "Magnetite is the finest iron ore, with up to 70 per cent iron.", True, "It also has excellent magnetic qualities.")
C.tf("tf2", CONV, "Natural gas usually occurs below oil in traps.", False, "Gas, being lighter, usually occurs above the oil.")
C.tf("tf3", NONC, "The monazite sands of Kerala are rich in thorium.", True, "Thorium is used for nuclear power.")
C.tf("tf4", CONV, "Thermal power is a renewable source of energy.", False, "Thermal power uses non-renewable fossil fuels; hydel power is renewable.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", OCC, "What are placer deposits? Name two minerals found in them.",
  ["Placer deposits are alluvial deposits in the sands of valley floors and the base of hills, containing minerals not corroded by water.", "Examples: gold, silver, tin and platinum (any two)."])
W("vsa2", "very_short_answer", CONS, "Give two hazards of mining for miners.",
  ["Inhaling dust and noxious fumes makes miners vulnerable to pulmonary diseases.", "Collapsing mine roofs, inundation and fires in coal mines are constant threats."])
W("vsa3", "very_short_answer", NONC, "What are the twin benefits of biogas plants?",
  ["They provide energy (gas with higher thermal efficiency than kerosene, dung cake and charcoal).", "They improve the quality of manure and prevent the loss of trees and manure from burning wood and dung cakes."])
W("sa1", "short_answer", OCC, "Describe three modes of occurrence of minerals.",
  ["In igneous and metamorphic rocks, minerals occur in cracks, crevices, faults or joints as veins and lodes (tin, copper, zinc, lead).",
   "In sedimentary rocks, minerals occur in beds or layers (coal, some iron ore; gypsum, potash and sodium salt from evaporation).",
   "By decomposition of surface rocks, a residual mass of ores remains (bauxite); also placer deposits (gold, tin) and ocean waters (salt, magnesium, bromine)."])
W("sa2", "short_answer", CONV, "How is petroleum trapped in rocks?",
  ["Most petroleum in India occurs in anticlines and fault traps in tertiary rocks.", "In anticlines or domes, oil is trapped in the crest of the upfold within porous limestone or sandstone, held by non-porous layers above and below.",
   "In fault traps, oil is held between porous and non-porous rocks; gas, being lighter, usually occurs above the oil."])
W("sa3", "short_answer", NONC, "Explain how tidal energy is produced and name the places in India suited for it.",
  ["Floodgate dams are built across inlets; at high tide, water flows in and is trapped when the gate is closed.",
   "When the tide falls outside, the stored water flows back to the sea through a pipe that turns a power-generating turbine.",
   "Ideal places: the Gulf of Khambhat and the Gulf of Kachchh (Gujarat) and the Gangetic delta in the Sunderban (West Bengal)."])
W("la1", "long_answer", MET, "Describe the distribution of iron ore in India.",
  ["Odisha-Jharkhand belt: high-grade hematite at Badampahar (Mayurbhanj and Kendujhar, Odisha) and Gua and Noamundi (Singhbhum, Jharkhand).",
   "Durg-Bastar-Chandrapur belt (Chhattisgarh and Maharashtra): super high-grade hematite in the Bailadila hills of Bastar, exported to Japan and South Korea via Visakhapatnam.",
   "Ballari-Chitradurga-Chikkamagaluru-Tumakuru belt (Karnataka): large reserves; Kudremukh is a 100% export unit sending ore as slurry by pipeline to a port near Mangaluru.",
   "Maharashtra-Goa belt: Goa and Ratnagiri; ore not of very high quality but efficiently exploited and exported through Marmagao.",
   "Magnetite (up to 70% iron) is the finest ore; hematite (50-60%) is the most used."])
W("la2", "long_answer", NONC, "Why is there a need to develop non-conventional sources of energy? Describe any three.",
  ["Growing consumption makes India dependent on fossil fuels; rising oil and gas prices and possible shortages threaten energy security, and fossil fuels cause pollution.",
   "Nuclear energy: altering atoms releases heat; uranium and thorium from Jharkhand, the Aravallis and Kerala's monazite sands.",
   "Solar energy: photovoltaic technology turns sunlight into electricity; a large plant near Bhuj sterilises milk cans; it reduces rural dependence on firewood and dung cakes.",
   "Wind energy: the largest cluster is from Nagarcoil to Madurai in Tamil Nadu; Jaisalmer is also known for wind energy.",
   "Geothermal (Parvati valley, Puga Valley), tidal (Gulf of Khambhat, Kachchh, Sunderban) and biogas are other renewable options."])
W("cb1", "case_based", CONV, "Read the source and answer the questions.\n\n*\"In India coal occurs in rock series of two main geological ages, namely Gondwana, a little over 200 million years in age and in tertiary deposits which are only about 55 million years old. The major resources of Gondwana coal, which are metallurgical coal, are located in Damodar valley (West Bengal-Jharkhand).\"* (NCERT)\n\n"
  "(i) How old is Gondwana coal? (1)\n\n(ii) Name one coalfield of the Damodar valley. (1)\n\n(iii) Why are heavy industries and thermal power stations located on or near coalfields? (2)",
  ["(i) A little over 200 million years.", "(ii) Jharia, Raniganj or Bokaro.",
   "(iii) Coal is a bulky material that loses weight on use as it is reduced to ash, so carrying it far is costly; industries and power plants are built close to the coalfields."])
W("cb2", "case_based", NONC, "Read the source and answer the questions.\n\n*\"Biogas plants using cattle dung are known as 'Gobar gas plants' in rural India. These provide twin benefits to the farmer in the form of energy and improved quality of manure.\"* (NCERT)\n\n"
  "(i) What are biogas plants using cattle dung called? (1)\n\n(ii) Which materials are used to produce biogas? (1)\n\n(iii) Why is biogas better than burning dung cakes and firewood? (2)",
  ["(i) Gobar gas plants.", "(ii) Shrubs, farm waste, and animal and human waste.",
   "(iii) It has higher thermal efficiency than kerosene, dung cake and charcoal, improves the quality of manure, and prevents the loss of trees and manure caused by burning fuel wood and dung cakes."])
# ---------------- Assertion-reason ----------------
C.arq("ar1", CONV, "Thermal power stations are located near coalfields.", "Coal is bulky and loses weight on use as it is reduced to ash.", 0,
      "R explains A.", "transport of coal is costly.", "coal turns to ash.")
C.arq("ar2", CONV, "Natural gas is called an environment-friendly fuel.", "It has low carbon dioxide emissions.", 0,
      "R explains A.", "it is a clean fuel.", "it emits less carbon dioxide.")
C.arq("ar3", MET, "India is self-sufficient in copper.", "Copper is malleable, ductile and a good conductor.", 3,
      "A is false: India is critically deficient in copper. R is true.", "India lacks copper.", "these are copper's properties.")
C.arq("ar4", CONS, "Minerals must be conserved.", "The rate of replenishment of minerals is infinitely small compared with consumption.", 0,
      "R explains A.", "they are finite.", "they form very slowly.")
C.arq("ar5", OCC, "Gold is found in placer deposits.", "Placer deposits contain minerals not corroded by water.", 0,
      "R explains A.", "gold occurs in valley sands.", "water does not corrode gold.")
C.arq("ar6", NONC, "Kerala is important for nuclear energy.", "Wind farms are located from Nagarcoil to Madurai.", 1,
      "Both are true, but R is about wind energy in Tamil Nadu; Kerala matters for its thorium-rich monazite sands.", "monazite sands contain thorium.", "that is the wind cluster.")

chapter = header(SUBJ, N, "Minerals and Energy Resources", ["mineral_occurrence", "metallic_nonmetallic", "mineral_conservation", "conventional_energy", "non_conventional_energy", "minerals_energy_map"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: this chapter is fully in the board examination (Geography: 17 marks + 3 map marks). Map work from this chapter: iron ore mines, coal mines, oil fields, and thermal and nuclear power plants (given here as text questions).")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
