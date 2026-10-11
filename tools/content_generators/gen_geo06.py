"""CBSE Class 10 Geography Ch 6: Manufacturing Industries (fully in the 2025-26 board syllabus; map: textile, steel, software parks)."""
import sys
from ss_common import make, header, path, SQP, SHINE, CB

ROOT = sys.argv[1]
SUBJ, N = "geography", 6
PATH = path(SUBJ, "ch06_manufacturing_industries")
C = make(SUBJ, N, "geo10ch06")
blk, M, W = C.blk, C.m, C.w
IMP, CLS, AGRO, MIN, POL, MAP = ["manufacturing_importance"], ["industry_classification"], ["agro_based"], ["mineral_based"], ["industrial_pollution"], ["industry_map"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 6 exercises", "question": n}

CLASSES = ("| Basis | Types | Examples |\n|---|---|---|\n| **Source of raw material** | agro-based / mineral-based | cotton, jute, silk, woollen textiles, sugar, edible oil / iron and steel, cement, aluminium, machine tools, petrochemicals |\n"
           "| **Prime role** | basic or key / consumer | iron and steel, copper and aluminium smelting / sugar, toothpaste, paper, sewing machines, fans |\n"
           "| **Capital investment** | small scale / large scale | maximum investment on assets of a small-scale unit is one crore rupees (as given in the textbook); above that is large scale |\n"
           "| **Ownership** | public / private / joint / co-operative | BHEL, SAIL / TISCO, Bajaj Auto, Dabur / Oil India Ltd (OIL) / sugar in Maharashtra, coir in Kerala |\n"
           "| **Bulk and weight** | heavy / light | iron and steel / electrical goods |")
MAPTAB = ("| Category | Centres to locate |\n|---|---|\n| Cotton textile | Mumbai, Indore, Surat, Kanpur, Coimbatore |\n| Iron and steel plants | Durgapur, Bokaro, Jamshedpur, Bhilai, Vijayanagar, Salem |\n"
          "| Software technology parks | Noida, Gandhinagar, Mumbai, Pune, Hyderabad, Bengaluru, Chennai, Thiruvananthapuram |")
POLL = ("| Type of pollution | Main causes |\n|---|---|\n| **Air** | sulphur dioxide and carbon monoxide; smoke from chemical and paper factories, brick kilns, refineries, smelting plants; toxic gas leaks |\n"
        "| **Water** | organic and inorganic effluents from paper, pulp, chemical, textile and dyeing industries, refineries, tanneries, electroplating; fly ash, phospho-gypsum, steel slag |\n"
        "| **Thermal (water)** | hot water from factories and thermal plants drained into rivers and ponds before cooling |\n"
        "| **Land** | dumping of glass, harmful chemicals, effluents, packaging, salts and garbage; pollutants seep into groundwater |\n"
        "| **Noise** | industrial and construction activities, machinery, generators, saws, pneumatic and electric drills |")

sections = [
 {"id": "s1", "title": "From raw material to finished goods", "blocks": [
  blk("s1.hook", "hook", title="How does a bale of cotton become your school shirt?",
    body="Cotton picked in Gujarat is ginned, spun into yarn in a mill, woven into cloth on a power-loom, dyed, cut and stitched. At every step, the cotton becomes more valuable. That is **manufacturing**.\n\n"
         "A country grows rich not just by growing or digging raw materials, but by turning them into goods of higher value. This chapter explains why manufacturing matters, how industries are classified, where India's major industries are located, and how they pollute and can be cleaned up."),
  blk("s1.inspiration", "inspiration", title="The dream of Indian steel", person="Jamsetji Nusserwanji Tata", years="1839–1904",
    body="In the late 19th century, Jamsetji Tata dreamed of an Indian steel plant at a time when British rulers doubted Indians could make steel. He sent geologists to search for iron ore and coal.\n\n"
         "He died in 1904, but his son Dorabji carried on: the **Tata Iron and Steel Company (TISCO)** was founded in **1907** at Sakchi, later named **Jamshedpur**, near the iron ore and coal of the Chota Nagpur plateau. It became the base of India's industrial growth.",
    future="This chapter leads to careers in industrial engineering, metallurgy, textile technology, environmental engineering and business."),
  C.socratic("s1.socratic", "Why is manufacturing called the backbone of development?",
    ["It turns raw materials into goods of higher value, creates jobs and earns foreign exchange", "It only uses up raw materials", "It replaces agriculture completely"], 0,
    "Manufacturing modernises agriculture, reduces dependence on farm income, removes unemployment and poverty, and brings foreign exchange."),
 ]},
 {"id": "s2", "title": "Why manufacturing matters", "blocks": [
  blk("s2.thm", "theory", title="Importance, contribution and location", revision=True,
    body="Production of goods in large quantities after processing from raw materials to more valuable products is called **manufacturing**. Paper is manufactured from wood, sugar from sugarcane, iron and steel from iron ore, and aluminium from bauxite. People engaged in manufacturing are in the **secondary sector**.\n\n"
         "**Importance of manufacturing:**\n- Manufacturing industries not only help in **modernising agriculture**, the backbone of our economy, but also **reduce the heavy dependence of people on agricultural income** by providing jobs in the secondary and tertiary sectors.\n"
         "- Industrial development is a precondition for the **eradication of unemployment and poverty**. This was the philosophy behind public sector industries and joint sector ventures in India, and also behind bringing industries to tribal and backward areas to reduce **regional disparities**.\n"
         "- **Export of manufactured goods** expands trade and commerce and brings much-needed **foreign exchange**.\n"
         "- Countries that transform their raw materials into a wide variety of finished goods of **higher value** are prosperous.\n\n"
         "**Agriculture and industry go hand in hand:** agro-industries in India have given a major boost to agriculture by raising its productivity. Industries depend on agriculture for raw materials, and sell products like **irrigation pumps, fertilisers, insecticides, pesticides, PVC pipes, machines and tools** to farmers.\n\n"
         "**Contribution to the national economy:** over the last two decades the share of manufacturing has stagnated at about **17 per cent of GDP**, out of a total of **27 per cent** for industry (which includes **10 per cent** for mining, quarrying, electricity and gas). The government set up the **National Manufacturing Competitiveness Council (NMCC)** to improve productivity, and the desired growth rate of manufacturing over the next decade is **12 per cent**.\n\n"
         "**Industrial location:** industrial locations are complex in nature, influenced by the availability of **raw material, labour, capital, power and market**. It is rarely possible to find all these at one place, so manufacturing tends to locate at the most appropriate place where all the factors are available or can be arranged at lower cost.\n"
         "- **Industrialisation and urbanisation go hand in hand.** Cities provide markets and services such as banking, insurance, transport, labour, consultants and financial advice. Many industries tend to come together to use the advantages offered by urban centres, known as **agglomeration economies**.\n"
         "- Before Independence, most manufacturing units were located from the point of view of **overseas trade**, e.g. **Mumbai, Kolkata and Chennai**."),
  C.kc("s2.check", "What is the share of manufacturing in India's GDP, stagnant over the last two decades?",
    [("About 17 per cent", ""), ("About 27 per cent", "27 per cent is the share of all industry."), ("About 10 per cent", "10 per cent is mining, quarrying, electricity and gas."), ("About 12 per cent", "12 per cent is the desired growth rate.")],
    "Manufacturing is about 17 per cent of GDP; the NMCC was set up to raise it."),
  C.kc("s2.check2", "When many industries come together to use the advantages of urban centres, it is called:",
    [("agglomeration economies", ""), ("disguised unemployment", "That is an Economics term for surplus workers."), ("regional disparity", "That means unequal development."), ("decontrol", "Decontrol means removing government controls.")],
    "Cities offer markets, banking, insurance, transport and labour."),
 ]},
 {"id": "s3", "title": "Classification of industries", "blocks": [
  blk("s3.thm", "theory", title="Five ways to classify industries", revision=True,
    body="Industries can be classified in several ways:\n\n"
         "1. **On the basis of source of raw materials:** **agro-based** industries use plant and animal products (cotton, woollen, jute, silk textile, rubber, sugar, tea, coffee, edible oil); **mineral-based** industries use minerals (iron and steel, cement, aluminium, machine tools, petrochemicals).\n"
         "2. **According to their main role:** **basic or key industries** supply their products or raw materials to manufacture other goods (iron and steel, copper smelting, aluminium smelting); **consumer industries** produce goods for direct use by consumers (sugar, toothpaste, paper, sewing machines, fans).\n"
         "3. **On the basis of capital investment:** the maximum investment allowed on the assets of a unit decides whether it is a **small-scale** industry; the limit has changed over time, and the textbook gives it as **one crore rupees**. If the investment is more than that, it is a **large-scale** industry.\n"
         "4. **On the basis of ownership:**\n   - **Public sector:** owned and operated by government agencies, e.g. **BHEL, SAIL**.\n   - **Private sector:** owned and operated by individuals or a group of individuals, e.g. **TISCO, Bajaj Auto Ltd, Dabur Industries**.\n"
         "   - **Joint sector:** jointly run by the state and individuals or a group of individuals, e.g. **Oil India Ltd (OIL)**.\n   - **Co-operative sector:** owned and operated by the producers or suppliers of raw materials, workers or both; they pool resources and share profits or losses, e.g. the **sugar industry in Maharashtra** and the **coir industry in Kerala**.\n"
         "5. **Based on the bulk and weight of raw material and finished goods:** **heavy industries** such as iron and steel; **light industries** that use light raw materials and produce light goods, such as electrical industries."),
  blk("s3.table", "markdown_table", title="Classification of industries", revision=True, body=CLASSES),
  C.kc("s3.check", "The sugar industry of Maharashtra and the coir industry of Kerala belong to which sector?",
    [("Co-operative sector", ""), ("Public sector", "Public sector units like SAIL are government-owned."), ("Private sector", "Private units like Dabur are owned by individuals."), ("Joint sector", "Joint sector units like Oil India are run by the state and individuals together.")],
    "Producers of raw materials and workers own and run co-operatives and share profits or losses."),
  C.kc("s3.check2", "Iron and steel, which supplies raw material for other industries, is a:",
    [("basic or key industry", ""), ("consumer industry", "Consumer industries make goods for direct use."), ("light industry", "Iron and steel is heavy."), ("co-operative industry", "That is classification by ownership.")],
    "Basic industries supply products used to make other goods."),
 ]},
 {"id": "s4", "title": "Agro-based industries", "blocks": [
  blk("s4.thm", "theory", title="Cotton textiles, jute and sugar", revision=True,
    body="**Textile industry:** it occupies a unique position in the Indian economy because it contributes significantly to industrial production, employment generation and foreign exchange earnings. It is the **only industry in the country which is self-reliant and complete in the value chain**, from raw material to the highest value-added products.\n\n"
         "**Cotton textiles:** in ancient India, cotton textiles were produced with **hand spinning and handloom weaving**. After the 18th century, **power-looms** came into use. Our traditional industries suffered a setback during the **colonial period** because they could not compete with mill-made cloth from England.\n"
         "- The **first successful textile mill** was established in **Mumbai in 1854**.\n"
         "- In the early years, the industry was concentrated in the **cotton-growing belt of Maharashtra and Gujarat**, because of the availability of **raw cotton, market, transport including accessible port facilities, labour and moist climate**.\n"
         "- The industry has close links with agriculture and provides a living to farmers, cotton boll pluckers and workers engaged in ginning, spinning, weaving, dyeing, designing, packaging, tailoring and sewing. It creates demand for many other industries like chemicals and dyes, packaging materials and engineering works.\n"
         "- **Spinning** is centralised in **Maharashtra, Gujarat and Tamil Nadu**, while **weaving is highly decentralised** to provide scope for traditional skills and designs in cotton, silk, zari and embroidery. India has world-class production in spinning, but weaving supplies low-quality fabric as it cannot use much of the high-quality yarn produced in the country.\n"
         "- **Problems:** erratic **power supply**, machinery that needs **upgrading** in weaving and processing, **low output of labour**, and stiff **competition with the synthetic fibre** industry.\n\n"
         "**Jute textiles:** India is the **largest producer of raw jute and jute goods** and stands at **second place as an exporter after Bangladesh**.\n"
         "- Most jute mills are in **West Bengal**, mainly along the banks of the **Hugli river**, in a narrow belt (**98 km long and 3 km wide**).\n"
         "- The **first jute mill** was set up near **Kolkata** in **1855** at **Rishra**. After Partition in **1947**, the jute mills remained in India, but **three-fourths of the jute-producing area went to Bangladesh** (then East Pakistan).\n"
         "- **Factors for location in the Hugli basin:** proximity of the jute-producing areas, **inexpensive water transport**, supported by a good network of railways, roadways and waterways, **abundant water** for processing raw jute, **cheap labour** from West Bengal and adjoining states of Bihar, Odisha and Uttar Pradesh, and **Kolkata** as a large urban centre providing banking, insurance and **port facilities** to export jute goods.\n"
         "- **Challenges:** stiff competition in the international market from **synthetic substitutes** and from other competitors like Bangladesh, Brazil, the Philippines, Egypt and Thailand. The **National Jute Policy (2005)** aimed at increasing productivity, improving quality, ensuring good prices to jute farmers and enhancing the yield per hectare. The growing global concern for **environment-friendly, biodegradable** materials has again opened an opportunity for jute products.\n\n"
         "**Sugar industry:** India stands **second** as a world producer of **sugar** but occupies the **first place** in the production of **gur and khandsari**.\n"
         "- The raw material (sugarcane) is **bulky**, and in haulage its **sucrose content reduces**, so mills are located near cane-growing areas. Mills are located in **Uttar Pradesh, Bihar, Maharashtra, Karnataka, Tamil Nadu, Andhra Pradesh and Gujarat**, along with Punjab, Haryana and Madhya Pradesh. Being **seasonal**, the industry is ideally suited to the **co-operative sector**.\n"
         "- In recent years, mills have tended to shift to the **southern and western states, especially Maharashtra**, because the cane produced there has a **higher sucrose content**, the **cooler climate** ensures a **longer crushing season**, and **co-operatives** are more successful in these states.\n"
         "- **Challenges:** the seasonal nature of the industry, old and inefficient methods of production, transport delays in reaching cane to factories, and the need to maximise the use of **baggase**."),
  C.kc("s4.check", "Where was the first successful cotton textile mill in India set up, and when?",
    [("Mumbai, in 1854", ""), ("Rishra near Kolkata, in 1855", "That was the first jute mill."), ("Chennai, in 1904", "That was the first cement plant."), ("Jamshedpur, in 1907", "That was TISCO, a steel company.")],
    "The industry first grew in the cotton belt of Maharashtra and Gujarat."),
  C.kc("s4.check2", "Why are sugar mills shifting towards Maharashtra and the south?",
    [("Higher sucrose content, a longer crushing season in a cooler climate, and successful co-operatives", ""), ("Sugarcane does not grow in the north", "UP and Bihar grow plenty of cane."),
     ("There are no co-operatives in the south", "Co-operatives are more successful there."), ("The south has the hottest climate", "The cooler climate gives a longer crushing season.")],
    "These advantages raise the efficiency of sugar mills."),
 ]},
 {"id": "s5", "title": "Mineral-based industries", "blocks": [
  blk("s5.thm", "theory", title="Steel, aluminium, chemicals, fertilisers, cement, automobiles and IT", revision=True,
    body="**Iron and steel industry:** a **basic industry**, since all other industries, heavy, medium and light, depend on it for their machinery. Steel is needed for engineering goods, construction material, defence, medical, telephonic and scientific equipment and consumer goods. "
         "**Production and consumption of steel** is often regarded as the **index of a country's development**. It is a **heavy industry** because all its raw materials and finished goods are heavy and bulky, with heavy transport costs.\n"
         "- **Iron ore, coking coal and limestone** are required in the ratio of about **4 : 2 : 1**; some **manganese** is also needed to harden the steel.\n"
         "- India is among the world's largest producers of crude steel (second in 2019). Most public sector steel is marketed through the **Steel Authority of India Limited (SAIL)**, while TISCO markets through Tata Steel.\n"
         "- The **Chota Nagpur plateau** has the maximum concentration of iron and steel industries, because of the **low cost of iron ore**, high-grade raw materials in proximity, **cheap labour** and vast growth potential in the home market.\n"
         "- India is not able to perform to its full potential because of the **high costs and limited availability of coking coal**, **lower productivity of labour**, **irregular supply of energy** and **poor infrastructure**. Liberalisation and foreign direct investment have given a boost to the industry.\n\n"
         "**Aluminium smelting:** the **second most important metallurgical industry** in India. Aluminium is **light, resistant to corrosion, a good conductor of heat, malleable** and becomes strong when mixed with other metals. It is used to manufacture **aircraft, utensils and wires**, and has gained popularity as a substitute for steel, copper, zinc and lead. "
         "Plants are located in **Odisha, West Bengal, Kerala, Uttar Pradesh, Chhattisgarh, Maharashtra and Tamil Nadu**. **Bauxite**, a dark reddish-coloured rock, is the raw material. **Regular supply of electricity** and an **assured source of raw material at minimum cost** are the two prime factors for location.\n\n"
         "**Chemical industries:** India's chemical industry is fast growing and diversifying. It has both small and large-scale units.\n"
         "- **Inorganic chemicals** include **sulphuric acid** (used to make fertilisers, synthetic fibres, plastics, adhesives, paints and dyes), nitric acid, alkalies, **soda ash** (used to make glass, soaps, detergents and paper) and caustic soda; these industries are widely spread.\n"
         "- **Organic chemicals** include **petrochemicals**, used to manufacture synthetic fibres, synthetic rubber, plastics, dye-stuffs, drugs and pharmaceuticals; these are located near **oil refineries or petrochemical plants**.\n"
         "- The chemical industry is **its own largest consumer**: basic chemicals are processed to produce other chemicals used for industrial application, agriculture or directly for consumer markets.\n\n"
         "**Fertiliser industry:** centred around the production of **nitrogenous fertilisers (mainly urea)**, **phosphatic fertilisers** and **ammonium phosphate (DAP)**, and complex fertilisers with a combination of **nitrogen (N), phosphate (P) and potash (K)**. "
         "**Potash is entirely imported**, as India has no reserves of commercially usable potash. The industry expanded after the **Green Revolution**. **Gujarat, Tamil Nadu, Uttar Pradesh, Punjab and Kerala** contribute half of the fertiliser production.\n\n"
         "**Cement industry:** cement is essential for construction: houses, factories, bridges, roads, airports, dams and commercial buildings. It needs **bulky and heavy raw materials** like **limestone, silica and gypsum**, and coal, electric power and rail transport. "
         "The **first cement plant** was set up in **Chennai in 1904**. **Decontrol of price and distribution since 1989** and other policy reforms led to rapid growth. Plants in **Gujarat** have suitable access to markets in the **Gulf countries**. Improved quality has opened markets in East Asia, the Middle East, Africa and South Asia.\n\n"
         "**Automobile industry:** vehicles are vehicles for quick transport of goods, services and passengers. Trucks, buses, cars, motorcycles, scooters, three-wheelers and multi-utility vehicles are made at centres like **Delhi, Gurugram, Mumbai, Pune, Chennai, Kolkata, Lucknow, Indore, Hyderabad, Jamshedpur and Bengaluru**. After **liberalisation**, new and contemporary models stimulated demand, and **foreign direct investment** brought new technology.\n\n"
         "**Information technology and electronics:** this industry covers a wide range of products, from transistor sets to television, telephones, cellular telecom, telephone exchanges, radars, computers and other equipment. **Bengaluru** has emerged as the **electronic capital of India**; Mumbai, Delhi, Hyderabad, Pune, Chennai, Kolkata, Lucknow and Coimbatore are other centres. "
         "**Software technology parks** provide a **single-window service** and **high-speed data communication** to software experts. The industry's major impact has been on **employment generation**, including many women, and on earning foreign exchange through business process outsourcing (BPO)."),
  blk("s5.map", "markdown_table", title="Map list: industrial centres (2025-26)", revision=True, body=MAPTAB),
  C.kc("s5.check", "In what ratio are iron ore, coking coal and limestone used in making steel?",
    [("About 4 : 2 : 1", ""), ("About 1 : 1 : 1", "Iron ore is needed in the largest amount."), ("About 2 : 4 : 1", "Iron ore, not coal, is the largest share."), ("About 1 : 2 : 4", "Limestone is the smallest share.")],
    "Some manganese is also added to harden the steel."),
  C.kc("s5.check2", "Which city is called the electronic capital of India?",
    [("Bengaluru", ""), ("Mumbai", "Mumbai is a centre, but Bengaluru is the electronic capital."), ("Kolkata", "Kolkata is a centre, but not the capital."), ("Jamshedpur", "Jamshedpur is known for steel.")],
    "Software technology parks give single-window service and high-speed data links."),
 ]},
 {"id": "s6", "title": "Industry and the environment", "blocks": [
  blk("s6.thm", "theory", title="Industrial pollution and how to control it", revision=True,
    body="Industries have contributed to India's growth, but they have also increased **pollution and environmental degradation**. Industries are responsible for four types of pollution: **air, water, land and noise**.\n\n"
         "- **Air pollution** is caused by undesirable gases like **sulphur dioxide and carbon monoxide**, and air-borne particulate materials (dust, sprays, mist and smoke). **Smoke** is emitted by chemical and paper factories, brick kilns, refineries and smelting plants, and by burning fossil fuels in factories that ignore pollution norms. **Toxic gas leaks** can be very hazardous with long-term effects; the gas leak at a pesticide factory in **Bhopal in December 1984** killed thousands of people.\n"
         "- **Water pollution** is caused by organic and inorganic industrial wastes and effluents discharged into rivers. The main culprits are **paper, pulp, chemical, textile and dyeing industries, petroleum refineries, tanneries and electroplating** industries that let out dyes, detergents, acids, salts and heavy metals like **lead and mercury**, pesticides, fertilisers, synthetic chemicals, plastics and rubber. **Fly ash, phospho-gypsum and iron and steel slags** are the major solid wastes.\n"
         "- **Thermal pollution** of water occurs when **hot water** from factories and thermal plants is drained into rivers and ponds **before cooling**. Wastes from nuclear power plants and weapon facilities can cause cancers, birth defects and miscarriages.\n"
         "- **Soil (land) pollution:** dumping of wastes, especially glass, harmful chemicals, industrial effluents, packaging, salts and garbage, renders the soil useless. Rainwater percolates into the soil carrying pollutants, and **groundwater** also gets contaminated.\n"
         "- **Noise pollution** results in irritation and anger, and can cause **hearing impairment, increased heart rate and blood pressure**. It comes from industrial and construction activities, machinery, generators, saws and pneumatic and electric drills.\n\n"
         "**Control of environmental degradation:**\n"
         "- Minimise the use of water for processing by **reusing and recycling** it in two or more successive stages; **harvest rainwater** to meet water requirements; **treat hot water and effluents** before releasing them into rivers and ponds.\n"
         "- Treatment of industrial effluents can be done in **three phases**: (a) **primary treatment** by mechanical means: screening, grinding, flocculation and sedimentation; (b) **secondary treatment** by a biological process; (c) **tertiary treatment** by biological, chemical and physical processes, involving recycling of wastewater.\n"
         "- **Overdrawing of groundwater** by industries should be regulated legally where it threatens groundwater resources.\n"
         "- **Particulate matter** in the air can be reduced by fitting smoke stacks with **electrostatic precipitators, fabric filters, scrubbers and inertial separators**; smoke can be reduced by using **oil or gas instead of coal**.\n"
         "- Machinery and generators can be fitted with **silencers**; machinery can be redesigned for energy efficiency and less noise; noise-absorbing material and **earplugs and earphones** can be used.\n\n"
         "**NTPC shows the way:** the National Thermal Power Corporation has a proactive approach to preserving the environment: optimum use of equipment with the latest techniques, **minimising waste** by maximising **ash utilisation**, providing **green belts** for ecological balance, reducing pollution through **ash pond management, ash water recycling** and liquid waste management, and **ecological monitoring** and online database management for all its power stations."),
  blk("s6.table", "markdown_table", title="Types of industrial pollution", revision=True, body=POLL),
  C.kc("s6.check", "Thermal pollution of water is caused by:",
    [("hot water from factories and thermal plants drained into rivers before cooling", ""), ("loud machinery", "That causes noise pollution."), ("sulphur dioxide in the air", "That is air pollution."), ("dumping of glass and packaging", "That is land pollution.")],
    "Water must be cooled and treated before it is released."),
  C.kc("s6.check2", "Screening, grinding, flocculation and sedimentation of effluents are part of:",
    [("primary treatment", ""), ("secondary treatment", "Secondary treatment is biological."), ("tertiary treatment", "Tertiary treatment involves recycling of wastewater."), ("ash pond management", "That is an NTPC practice for fly ash.")],
    "Primary treatment uses mechanical means.")
 ]},
 {"id": "s7", "title": "Remember, avoid, practise", "blocks": [
  blk("s7.memory", "memory_trick", title="Memory tricks",
    body="- **Five bases of classification: \"Really Rich Countries Own Big industries\"** = Raw material, Role, Capital, Ownership, Bulk.\n- **Ownership examples: Public = SAIL/BHEL; Private = TISCO/Dabur; Joint = OIL; Co-op = sugar (Maharashtra), coir (Kerala).**\n"
         "- **Firsts: textile mill Mumbai 1854 → jute mill Rishra 1855 → cement Chennai 1904 → TISCO 1907.**\n- **Steel recipe 4 : 2 : 1** = iron ore : coking coal : limestone.\n"
         "- **Jute belt: 98 km × 3 km along the Hugli.**\n- **Effluent treatment: Primary = mechanical, Secondary = biological, Tertiary = all three + recycling.**"),
  blk("s7.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Calling iron and steel a consumer industry: it is a **basic (key)** industry.\n2. Saying India is the largest exporter of jute goods: India is the **largest producer** but **second exporter after Bangladesh**.\n"
         "3. Saying India is the first in sugar: India is **second** in sugar but **first in gur and khandsari**.\n4. Mixing up joint sector (**Oil India Ltd**) and co-operative sector (**sugar in Maharashtra, coir in Kerala**).\n"
         "5. Saying potash is produced in India: potash is **entirely imported**.\n6. Saying weaving is centralised: **spinning** is centralised in Maharashtra, Gujarat and Tamil Nadu; **weaving is decentralised**."),
  blk("s7.tip", "teacher_tip", title="Try this in class",
    body="Bring five everyday objects (a shirt, a sugar packet, a steel spoon, a cement sample photo, a phone) and let students trace each back to its raw material, its industry and the industry's type. "
         "Then mark the cotton textile centres, steel plants and software parks on an outline map."),
  blk("s7.reflection", "reflection", title="Think and explain",
    body="Suppose a new factory is planned near your town. List two benefits it would bring and two kinds of pollution it might cause, and suggest one control measure for each."),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 4 (Agriculture):** cotton, jute and sugarcane feed agro-based industries.\n- **Chapter 5 (Minerals and Energy):** iron ore, coal, limestone and bauxite feed mineral-based industries.\n"
         "- **Chapter 7 (Lifelines):** transport and ports carry raw materials and finished goods.\n- **Economics, Sectors of the Economy:** manufacturing is the secondary sector."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="'Pollution undermines sustainable economic growth.' Using the 2025-26 sample paper case, explain how manufacturing industries cause pollution and how it can be controlled, in about 120 words.\n\n"
         "**Model answer:** Manufacturing industries cause air pollution through smoke from chemical and paper factories, brick kilns, refineries and smelting plants, and through toxic gas leaks. They cause water pollution by discharging effluents with dyes, acids, salts and heavy metals like lead and mercury from paper, textile, refinery, tannery and electroplating units, and thermal pollution by releasing hot water. "
         "Dumping of glass, chemicals and packaging makes soil useless and contaminates groundwater, while machinery and generators create noise. Pollution can be controlled by recycling water, treating effluents in primary, secondary and tertiary stages, fitting electrostatic precipitators and scrubbers, using gas instead of coal and fitting silencers. "
         "Since poor people suffer most from pollution, controlling it also reduces inequality."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- Manufacturing turns raw materials into goods of higher value; it modernises agriculture, creates jobs, reduces poverty and earns foreign exchange; its share of GDP is about 17%.\n"
         "- Location depends on raw material, labour, capital, power and market; cities create agglomeration economies.\n"
         "- Industries are classified by raw material, role, capital, ownership and bulk.\n"
         "- Agro-based: cotton textiles (Mumbai 1854), jute (Hugli belt, Rishra 1855), sugar (shifting to Maharashtra and the south).\n"
         "- Mineral-based: iron and steel (4:2:1, Chota Nagpur), aluminium, chemicals, fertilisers, cement (Chennai 1904), automobiles and IT (Bengaluru).\n"
         "- Industries cause air, water, thermal, land and noise pollution; recycling, effluent treatment, filters, cleaner fuels and silencers help control it."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- The 2025-26 sample paper had a 4-mark case study on global pollution: why waste will rise (intensive material production and consumption), how manufacturing causes different types of pollution, and how pollution worsens poverty and inequality.\n"
         "- 3/5-mark favourites: importance of manufacturing, classification, cotton and jute industries, sugar mills shifting south, iron and steel problems, pollution and its control.\n"
         "- **Map work:** cotton textile centres, iron and steel plants and software technology parks."),
  blk("s7.flash1", "flashcard", front="What are agglomeration economies?", back="The advantages industries get by coming together in urban centres: markets, banking, insurance, transport, labour and services."),
  blk("s7.flash2", "flashcard", front="Give one example each of public, private, joint and co-operative sector industries.", back="Public: SAIL or BHEL. Private: TISCO or Dabur. Joint: Oil India Ltd. Co-operative: sugar in Maharashtra or coir in Kerala."),
  blk("s7.flash3", "flashcard", front="Why is the jute industry concentrated along the Hugli?", back="Nearby jute areas, cheap water transport, rail and road links, abundant water, cheap labour, and Kolkata's banking, insurance and port."),
  blk("s7.flash4", "flashcard", front="Name the three phases of effluent treatment.", back="Primary (mechanical: screening, grinding, flocculation, sedimentation), secondary (biological) and tertiary (biological, chemical, physical with recycling)."),
 ]},
]

# ---------------- Sample paper ----------------
W("sqp18", "case_based", POL, "Read the given text and answer the questions.\n\n*\"Global pollution is rising due to rapid economic growth, population increases, and insufficient environmental management... the global economy relies on deeply intertwined supply chains, sustained by more than 100 billion tons of raw materials entering the system each year. Intensive material consumption depletes natural resources and causes negative environmental impacts at every stage of the product lifecycle. Global waste is expected to increase to 3.4 billion tons by 2050. Pollution of all types hinders development outcomes... Pollution undermines sustainable economic growth, exacerbates poverty and inequality in both urban and rural areas... Poor people, who cannot afford to protect themselves from the negative impacts of pollution, end up suffering the most.\"* (World Bank)\n\n"
  "(i) Why do you think global waste is expected to increase by 2050? (1)\n\n(ii) How do manufacturing industries cause pollution of different types? Explain with examples. (2)\n\n(iii) Is it correct to consider pollution as a possible cause for worsening of the current global trends of poverty and inequality? Justify. (1)",
  ["(i) Because of intensive material production and consumption.",
   "(ii) Any two: air pollution from smoke of chemical and paper factories, brick kilns, refineries and smelting plants and toxic gas leaks; water pollution from effluents of paper, pulp, textile, dyeing, refinery, tannery and electroplating industries (dyes, acids, heavy metals like lead and mercury); thermal pollution from hot water; land pollution from dumped wastes; noise from machinery and generators.",
   "(iii) Yes: poor people cannot afford to protect themselves from the effects of pollution, so they suffer the most, which worsens poverty and social inequality."],
  ["(i) 1 mark", "(ii) 2 marks", "(iii) 1 mark"], source=SQP(18))

# ---------------- NCERT exercises ----------------
M("ex1i", MIN, "Which one of the following industries uses limestone as a raw material?",
  [("Aluminium", "Aluminium uses bauxite."), ("Cement", ""), ("Plastic", "Plastic uses petrochemicals."), ("Automobile", "Automobiles use steel and many parts.")],
  "Cement needs limestone, silica and gypsum.", "easy", ex("1(i)"), correct=1)
M("ex1ii", CLS, "Which one of the following agencies markets steel for the public sector plants?",
  [("HAIL", "Not a steel marketing agency."), ("SAIL", ""), ("TATA Steel", "Tata Steel markets for TISCO, a private company."), ("MNCC", "Not a steel marketing agency.")],
  "Steel Authority of India Limited markets public sector steel.", "easy", ex("1(ii)"), correct=1)
M("ex1iii", MIN, "Which one of the following industries uses bauxite as a raw material?",
  [("Aluminium", ""), ("Cement", "Cement uses limestone."), ("Jute", "Jute uses raw jute."), ("Steel", "Steel uses iron ore.")],
  "Bauxite gives alumina and then aluminium.", "easy", ex("1(iii)"), correct=0)
M("ex1iv", MIN, "Which one of the following industries manufactures telephones, computer, etc?",
  [("Steel", "Steel makes steel."), ("Electronic", ""), ("Aluminium", "Aluminium makes aluminium."), ("Information Technology", "IT is linked, but the manufacturing industry is electronics.")],
  "The electronics industry makes telephones, computers, radars and more.", "easy", ex("1(iv)"), correct=1)
W("ex2i", "short_answer", IMP, "What is manufacturing?",
  ["Manufacturing is the production of goods in large quantities after processing raw materials into more valuable products.",
   "Examples: paper from wood, sugar from sugarcane, iron and steel from iron ore, aluminium from bauxite.",
   "People engaged in it work in the secondary sector."], source=ex("2(i)"))
W("ex2ii", "short_answer", IMP, "Name any three physical factors for the location of industries.",
  ["Availability of raw material.", "Availability of power (energy) and water.", "Suitable climate and land (for example, a moist climate suits cotton textiles)."], source=ex("2(ii)"))
W("ex2iii", "short_answer", IMP, "Name any three human factors for the location of an industry.",
  ["Availability of labour.", "Availability of capital (and banking and insurance).", "Market and transport facilities (government policies also matter)."], source=ex("2(iii)"))
W("ex2iv", "short_answer", CLS, "What are basic industries? Give an example.",
  ["Basic or key industries supply their products or raw materials to manufacture other goods.",
   "Other industries depend on them for machinery and materials.", "Examples: iron and steel, copper smelting and aluminium smelting."], source=ex("2(iv)"))
W("ex3i", "long_answer", AGRO, "How are integrated steel plants different from mini steel plants? What problems does the industry face? What recent developments have led to a rise in the production capacity?",
  ["Integrated steel plants are large and handle everything in one complex: putting together raw materials, making iron and steel, rolling and shaping.",
   "Mini steel plants are smaller, use steel scrap and sponge iron in electric furnaces, and produce mild and alloy steel of given specifications.",
   "Problems: high costs and limited availability of coking coal, lower productivity of labour, irregular supply of energy and poor infrastructure.",
   "Recent developments: liberalisation and foreign direct investment have brought new technology and investment.",
   "Private entrepreneurs have entered the industry, raising production capacity; India is now among the largest steel producers."], source=ex("3(i)"))
W("ex3ii", "long_answer", IMP, "How do industries pollute the environment?",
  ["Air pollution: sulphur dioxide, carbon monoxide and smoke from chemical and paper factories, brick kilns, refineries and smelting plants; toxic gas leaks.",
   "Water pollution: effluents with dyes, acids, salts and heavy metals like lead and mercury from paper, pulp, textile, dyeing, refinery, tannery and electroplating industries.",
   "Thermal pollution: hot water from factories and thermal plants drained into rivers before cooling.",
   "Land pollution: dumping of glass, chemicals, effluents, packaging and garbage, which also contaminates groundwater.",
   "Noise pollution: machinery, generators, saws and drills cause hearing problems and stress."], source=ex("3(ii)"))
W("ex3iii", "long_answer", POL, "Discuss the steps to be taken to minimise environmental degradation by industry.",
  ["Reuse and recycle water in successive stages, harvest rainwater, and treat hot water and effluents before release.",
   "Treat effluents in three phases: primary (mechanical), secondary (biological) and tertiary (biological, chemical and physical with recycling).",
   "Regulate overdrawing of groundwater by industries legally.",
   "Fit smoke stacks with electrostatic precipitators, fabric filters, scrubbers and inertial separators, and use oil or gas instead of coal.",
   "Fit silencers on machinery and generators, redesign machines for less noise, and use earplugs; follow NTPC's example of ash utilisation and green belts."], source=ex("3(iii)"))

# ---------------- MCQs ----------------
M("mcq01", IMP, "People engaged in manufacturing belong to the:",
  [("secondary sector", ""), ("primary sector", "Agriculture and mining are primary."), ("tertiary sector", "Services are tertiary."), ("quaternary sector", "The chapter uses secondary.")], "Manufacturing processes raw materials.")
M("mcq02", IMP, "Which is NOT a reason why manufacturing is important?",
  [("It increases dependence on agricultural income", ""), ("It helps modernise agriculture", "This is a reason."), ("It earns foreign exchange through exports", "This is a reason."), ("It helps remove unemployment and poverty", "This is a reason.")], "It reduces dependence on farm income.")
M("mcq03", IMP, "The share of industry (including mining, electricity and gas) in India's GDP is about:",
  [("27 per cent", ""), ("17 per cent", "That is manufacturing alone."), ("10 per cent", "That is mining, quarrying, electricity and gas."), ("50 per cent", "It is about 27 per cent.")], "Manufacturing alone is about 17 per cent.")
M("mcq04", IMP, "The council set up to improve the productivity of manufacturing is the:",
  [("National Manufacturing Competitiveness Council", ""), ("Steel Authority of India", "SAIL markets steel."), ("National Thermal Power Corporation", "NTPC produces power."), ("National Jute Policy", "That is a policy, not a council.")], "NMCC aims at higher manufacturing growth.")
M("mcq05", IMP, "Before Independence, most industries were located to suit:",
  [("overseas trade, in cities like Mumbai, Kolkata and Chennai", ""), ("tribal areas", "That was a post-Independence aim."), ("hill stations", "Not the reason."), ("forest areas", "Not the reason.")], "Ports made overseas trade easy.")
M("mcq06", IMP, "Which is a product industries sell to agriculture?",
  [("Irrigation pumps", ""), ("Raw cotton", "Industry buys raw cotton from farmers."), ("Sugarcane", "Industry buys sugarcane."), ("Raw jute", "Industry buys raw jute.")], "Also fertilisers, pesticides, PVC pipes and tools.")
M("mcq07", CLS, "Cotton, jute and sugar industries are:",
  [("agro-based", ""), ("mineral-based", "They use plant products."), ("basic industries", "They make consumer goods."), ("heavy industries", "They are not classed as heavy.")], "They use agricultural raw materials.")
M("mcq08", CLS, "Toothpaste, sugar and sewing machines are made by:",
  [("consumer industries", ""), ("basic industries", "Basic industries supply other industries."), ("joint sector only", "Ownership is a separate basis."), ("mineral-based industries", "Sugar is agro-based.")], "Consumer industries make goods for direct use.")
M("mcq09", CLS, "BHEL and SAIL are examples of:",
  [("public sector industries", ""), ("private sector industries", "TISCO and Dabur are private."), ("joint sector industries", "Oil India is joint."), ("co-operative industries", "Sugar in Maharashtra is co-operative.")], "They are owned by government agencies.")
M("mcq10", CLS, "Oil India Ltd (OIL) is an example of the:",
  [("joint sector", ""), ("public sector", "BHEL and SAIL are public."), ("private sector", "TISCO is private."), ("co-operative sector", "Coir in Kerala is co-operative.")], "It is run jointly by the state and private parties.")
M("mcq11", CLS, "TISCO, Bajaj Auto and Dabur are examples of:",
  [("private sector industries", ""), ("public sector industries", "These are owned by individuals or groups."), ("joint sector industries", "OIL is joint."), ("co-operative industries", "These are not co-operatives.")], "Private sector units are owned by individuals or groups.")
M("mcq12", CLS, "Electrical goods industries are examples of:",
  [("light industries", ""), ("heavy industries", "Iron and steel is heavy."), ("basic industries", "They make consumer goods."), ("agro-based industries", "They use minerals and metals.")], "They use light raw materials and make light goods.")
M("mcq13", AGRO, "The only industry self-reliant and complete in the value chain is:",
  [("the textile industry", ""), ("the steel industry", "Steel depends on imported coking coal."), ("the fertiliser industry", "Potash is imported."), ("the automobile industry", "It uses imported technology.")], "From raw material to the highest value-added products.")
M("mcq14", AGRO, "Why did India's traditional cotton industry suffer during colonial rule?",
  [("It could not compete with mill-made cloth from England", ""), ("Cotton stopped growing", "Cotton was still grown."), ("Power-looms were banned", "Not the reason."), ("Indians stopped wearing cotton", "Not the reason.")], "Machine-made cloth was cheaper.")
M("mcq15", AGRO, "The cotton textile industry was first concentrated in Maharashtra and Gujarat because of:",
  [("raw cotton, market, port and transport, labour and moist climate", ""), ("cold climate", "Moist climate suited spinning."), ("coal mines", "Not the main factor."), ("jute fields", "That is the jute industry.")], "Both states had the cotton-growing belt.")
M("mcq16", AGRO, "Spinning is centralised in:",
  [("Maharashtra, Gujarat and Tamil Nadu", ""), ("West Bengal and Bihar", "These are known for jute."), ("Punjab and Haryana", "Not the centres named."), ("Kerala and Karnataka", "Not the centres named.")], "Weaving is highly decentralised.")
M("mcq17", AGRO, "Which is NOT a problem of the cotton textile industry?",
  [("Shortage of raw cotton in India", ""), ("Erratic power supply", "This is a problem."), ("Machinery needing upgrades", "This is a problem."), ("Competition from synthetic fibres", "This is a problem.")], "Low labour output is another problem.")
M("mcq18", AGRO, "India's position in jute is:",
  [("largest producer, second largest exporter after Bangladesh", ""), ("largest exporter", "Bangladesh exports more."), ("second producer after China", "India is the largest producer."), ("a minor producer", "India is the largest producer.")], "The Hugli belt is the centre.")
M("mcq19", AGRO, "The jute mill belt along the Hugli is about:",
  [("98 km long and 3 km wide", ""), ("1,000 km long", "It is a narrow belt."), ("3 km long and 98 km wide", "The numbers are reversed."), ("10 km long and 10 km wide", "It is 98 km by 3 km.")], "Most jute mills are in West Bengal.")
M("mcq20", AGRO, "The first jute mill in India was set up at:",
  [("Rishra, near Kolkata, in 1855", ""), ("Mumbai, in 1854", "That was the first cotton mill."), ("Chennai, in 1904", "That was the first cement plant."), ("Kanpur, in 1907", "Not the first jute mill.")], "After Partition, three-fourths of jute areas went to Bangladesh.")
M("mcq21", AGRO, "The National Jute Policy was formulated in:",
  [("2005", ""), ("1947", "1947 was Partition."), ("1989", "1989 was cement decontrol."), ("1855", "1855 was the first jute mill.")], "It aims to improve productivity, quality and farmers' prices.")
M("mcq22", AGRO, "Why is there a new opportunity for jute products?",
  [("Growing global concern for environment-friendly, biodegradable materials", ""), ("Nylon has been banned worldwide", "It has not."), ("Jute became cheaper than plastic everywhere", "Its high cost is still a problem."), ("Bangladesh stopped producing jute", "It has not.")], "Jute is biodegradable.")
M("mcq23", AGRO, "India is first in the world in the production of:",
  [("gur and khandsari", ""), ("sugar", "India is second in sugar."), ("raw jute exports", "Bangladesh exports more."), ("crude steel", "India is among the top, but not first.")], "Sugar mills are ideal for the co-operative sector.")
M("mcq24", AGRO, "Why are sugar mills located near cane fields?",
  [("Sugarcane is bulky and loses sucrose in haulage", ""), ("Sugar is light", "The raw material is the issue."), ("Cane grows only near factories", "Factories follow the cane."), ("Mills need sea water", "Not needed.")], "Long transport reduces sucrose.")
M("mcq25", AGRO, "Which is a challenge of the sugar industry?",
  [("Its seasonal nature and old, inefficient methods", ""), ("Too much demand for jute", "Unrelated."), ("Shortage of bauxite", "Unrelated."), ("Too many software parks", "Unrelated.")], "Transport delays and baggase use are other issues.")
M("mcq26", MIN, "Steel production and consumption is regarded as an index of a country's:",
  [("development", ""), ("population", "Not the index."), ("rainfall", "Not related."), ("forest cover", "Not related.")], "Steel is a basic industry.")
M("mcq27", MIN, "Which mineral is added to harden steel?",
  [("Manganese", ""), ("Mica", "Mica is used in electrical industries."), ("Bauxite", "Bauxite gives aluminium."), ("Gypsum", "Gypsum is used in cement.")], "Small amounts of manganese harden steel.")
M("mcq28", MIN, "The maximum concentration of iron and steel industries is in the:",
  [("Chota Nagpur plateau", ""), ("Thar desert", "No iron and coal there."), ("Ganga delta", "Not the main region."), ("Western Ghats only", "The chapter names Chota Nagpur.")], "Low-cost iron ore and nearby raw materials.")
M("mcq29", MIN, "Which is NOT a problem of the Indian iron and steel industry?",
  [("Abundant cheap coking coal", ""), ("High costs and limited availability of coking coal", "This is a problem."), ("Irregular energy supply", "This is a problem."), ("Poor infrastructure", "This is a problem.")], "Coking coal is costly and limited.")
M("mcq30", MIN, "The two prime factors for locating aluminium smelters are:",
  [("regular supply of electricity and assured raw material at low cost", ""), ("cheap jute and water", "That is jute."), ("sea breeze and sunshine", "Not the factors."), ("cotton and moist climate", "That is cotton textiles.")], "Smelting needs much electricity.")
M("mcq31", MIN, "Which is NOT a property of aluminium?",
  [("It rusts easily", ""), ("It is light", "This is a property."), ("It resists corrosion", "This is a property."), ("It is a good conductor of heat", "This is a property.")], "Aluminium resists corrosion.")
M("mcq32", MIN, "Organic chemical (petrochemical) plants are located near:",
  [("oil refineries or petrochemical plants", ""), ("jute mills", "Not related."), ("coal mines only", "They use oil products."), ("tea gardens", "Not related.")], "They make synthetic fibres, rubber, plastics and drugs.")
M("mcq33", MIN, "Soda ash is used to make:",
  [("glass, soaps, detergents and paper", ""), ("steel", "Steel uses iron ore."), ("cement", "Cement uses limestone."), ("jute bags", "Jute bags use jute.")], "Soda ash is an inorganic chemical.")
M("mcq34", MIN, "Which fertiliser raw material is entirely imported?",
  [("Potash", ""), ("Urea", "Urea is made in India."), ("Phosphate", "Phosphatic fertilisers are made in India."), ("Ammonia", "Ammonia is made in India.")], "India has no commercially usable potash.")
M("mcq35", MIN, "The first cement plant in India was set up in:",
  [("Chennai, in 1904", ""), ("Mumbai, in 1854", "That was the first cotton mill."), ("Rishra, in 1855", "That was the first jute mill."), ("Jamshedpur, in 1907", "That was TISCO.")], "Decontrol since 1989 boosted the industry.")
M("mcq36", MIN, "Cement plants in Gujarat have an advantage because of access to markets in:",
  [("the Gulf countries", ""), ("Japan", "The chapter names the Gulf countries."), ("Bangladesh", "Not the market named."), ("Australia", "Not the market named.")], "Gujarat is close to the Gulf by sea.")
M("mcq37", MIN, "Which city is known as the electronic capital of India?",
  [("Bengaluru", ""), ("Pune", "Pune is a centre but not the capital."), ("Kanpur", "Kanpur is a cotton textile centre."), ("Durgapur", "Durgapur has a steel plant.")], "Many software parks are located there.")
M("mcq38", MIN, "Software technology parks provide:",
  [("single-window service and high-speed data communication", ""), ("free raw cotton", "Not related."), ("coking coal", "Not related."), ("cheap jute", "Not related.")], "They support software experts.")
M("mcq39", POL, "Fly ash, phospho-gypsum and steel slag are major:",
  [("solid wastes from industries", ""), ("raw materials for sugar", "Not related."), ("sources of noise", "They are solid wastes."), ("fertiliser types", "They are wastes.")], "They pollute land and water.")
M("mcq40", POL, "Particulate matter in factory smoke can be reduced by:",
  [("electrostatic precipitators, fabric filters, scrubbers and inertial separators", ""), ("silencers", "Silencers reduce noise."), ("earplugs", "Earplugs protect from noise."), ("dumping waste in rivers", "That causes pollution.")], "Using oil or gas instead of coal also reduces smoke.")
M("mcq41", POL, "Secondary treatment of effluents is done by:",
  [("a biological process", ""), ("mechanical screening and grinding", "That is primary treatment."), ("burning", "Not a treatment phase."), ("dumping in ponds", "Not a treatment.")], "Tertiary treatment adds chemical and physical processes and recycling.")
M("mcq42", POL, "Which practice is followed by NTPC to protect the environment?",
  [("Maximising ash utilisation and providing green belts", ""), ("Releasing hot water directly into rivers", "That causes thermal pollution."), ("Using more coal without filters", "That increases pollution."), ("Ignoring monitoring", "NTPC monitors its plants.")], "NTPC also manages ash ponds and recycles ash water.")
# ---------------- Map work ----------------
M("map1", MAP, "Map work: which is a cotton textile centre on the map list?",
  [("Coimbatore", ""), ("Bhilai", "Bhilai has a steel plant."), ("Noida", "Noida has a software park."), ("Bokaro", "Bokaro has a steel plant.")], "Mumbai, Indore, Surat, Kanpur and Coimbatore.", "medium")
M("map2", MAP, "Map work: the Bhilai iron and steel plant is in:",
  [("Chhattisgarh", ""), ("Jharkhand", "Bokaro and Jamshedpur are in Jharkhand."), ("West Bengal", "Durgapur is in West Bengal."), ("Karnataka", "Vijayanagar is in Karnataka.")], "Bhilai is in Chhattisgarh.", "medium")
M("map3", MAP, "Map work: the Salem steel plant is in:",
  [("Tamil Nadu", ""), ("Karnataka", "Vijayanagar is in Karnataka."), ("Odisha", "Not on the list."), ("Maharashtra", "Not on the list.")], "Salem is in Tamil Nadu.", "medium")
M("map4", MAP, "Map work: which is a software technology park in Gujarat?",
  [("Gandhinagar", ""), ("Surat", "Surat is a cotton textile centre."), ("Indore", "Indore is in Madhya Pradesh."), ("Pune", "Pune is in Maharashtra.")], "Gandhinagar is on the software park list.", "medium")
W("map5", "very_short_answer", MAP, "Map work: name (a) two iron and steel plants of Jharkhand and (b) the software technology park in Kerala.",
  ["(a) Bokaro and Jamshedpur.", "(b) Thiruvananthapuram."])
# ---------------- True / false ----------------
C.tf("tf1", CLS, "Iron and steel is a consumer industry.", False, "It is a basic (key) industry that supplies other industries.")
C.tf("tf2", AGRO, "India is the second largest exporter of jute goods after Bangladesh.", True, "India is the largest producer of raw jute and jute goods.")
C.tf("tf3", MIN, "Potash for fertilisers is entirely imported.", True, "India has no commercially usable potash reserves.")
C.tf("tf4", AGRO, "Weaving is centralised while spinning is decentralised in India.", False, "Spinning is centralised in Maharashtra, Gujarat and Tamil Nadu; weaving is decentralised.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", IMP, "How do agriculture and industry help each other?",
  ["Agro-industries raise agricultural productivity and depend on agriculture for raw materials like cotton, jute and sugarcane.", "Industries sell irrigation pumps, fertilisers, pesticides, PVC pipes, machines and tools to farmers."])
W("vsa2", "very_short_answer", AGRO, "Why is the sugar industry suited to the co-operative sector?",
  ["It is seasonal, working only during the cane-crushing season.", "Cane growers can pool resources, own the mills and share profits, as in Maharashtra."])
W("vsa3", "very_short_answer", POL, "What is thermal pollution and how can it be prevented?",
  ["Thermal pollution occurs when hot water from factories and thermal plants is drained into rivers and ponds before cooling.", "It can be prevented by cooling and treating hot water before releasing it."])
W("sa1", "short_answer", AGRO, "Why is the jute industry concentrated along the banks of the Hugli?",
  ["Jute-producing areas are nearby, and cheap water transport is supported by railways and roads.",
   "There is abundant water for processing raw jute and cheap labour from West Bengal, Bihar, Odisha and Uttar Pradesh.",
   "Kolkata provides banking, insurance and port facilities for export."])
W("sa2", "short_answer", AGRO, "Why are sugar mills shifting to the southern and western states?",
  ["The cane produced there has a higher sucrose content.", "The cooler climate ensures a longer crushing season.", "Co-operatives are more successful in these states, especially Maharashtra."])
W("sa3", "short_answer", MIN, "What are the problems faced by the Indian iron and steel industry?",
  ["High costs and limited availability of coking coal.", "Lower productivity of labour and irregular supply of energy.", "Poor infrastructure (liberalisation and FDI have helped)."])
W("la1", "long_answer", CLS, "Classify industries on the basis of ownership and of raw material, with examples.",
  ["By raw material: agro-based industries use plant and animal products, e.g. cotton, jute, sugar, edible oil.",
   "Mineral-based industries use minerals, e.g. iron and steel, cement, aluminium, petrochemicals.",
   "By ownership: public sector units are owned by government agencies (BHEL, SAIL); private sector units by individuals or groups (TISCO, Bajaj Auto, Dabur).",
   "Joint sector units are run by the state and individuals together (Oil India Ltd).",
   "Co-operative sector units are owned by producers of raw materials, workers or both, who share profits or losses (sugar in Maharashtra, coir in Kerala)."])
W("cb1", "case_based", AGRO, "Read the source and answer the questions.\n\n*\"India is the largest producer of raw jute and jute goods and stands at second place as an exporter after Bangladesh. Most of the mills are located in West Bengal, mainly along the banks of the Hugli river, in a narrow belt (98 km long and 3 km wide).\"* (NCERT)\n\n"
  "(i) Which country exports more jute goods than India? (1)\n\n(ii) Where are most jute mills located? (1)\n\n(iii) Give two challenges and one new opportunity for the jute industry. (2)",
  ["(i) Bangladesh.", "(ii) In West Bengal, along the banks of the Hugli river.",
   "(iii) Challenges: stiff competition from synthetic substitutes and from countries like Bangladesh, Brazil, the Philippines, Egypt and Thailand; opportunity: growing demand for environment-friendly, biodegradable materials."])
W("cb2", "case_based", POL, "Read the source and answer the questions.\n\n*\"Treatment of industrial effluents can be done in three phases: (a) primary treatment by mechanical means. This involves screening, grinding, flocculation and sedimentation. (b) secondary treatment by biological process. (c) tertiary treatment by biological, chemical and physical processes. This involves recycling of wastewater.\"* (NCERT)\n\n"
  "(i) Which phase of treatment uses mechanical means? (1)\n\n(ii) Which phase involves recycling of wastewater? (1)\n\n(iii) Suggest two other ways industries can reduce water pollution. (2)",
  ["(i) Primary treatment.", "(ii) Tertiary treatment.",
   "(iii) Reuse and recycle water in successive stages, harvest rainwater, cool and treat hot water before release, and regulate overdrawing of groundwater (any two)."])
# ---------------- Assertion-reason ----------------
C.arq("ar1", AGRO, "Jute mills are concentrated along the Hugli river.", "The Hugli basin offers cheap water transport, abundant water and cheap labour.", 0,
      "R explains A.", "most mills are in West Bengal.", "these are the location factors.")
C.arq("ar2", AGRO, "Sugar mills are located near sugarcane fields.", "Sugarcane is bulky and its sucrose content falls during haulage.", 0,
      "R explains A.", "mills follow the cane.", "long transport reduces sucrose.")
C.arq("ar3", MIN, "Iron and steel is a heavy industry.", "Its raw materials and finished goods are heavy and bulky, with high transport costs.", 0,
      "R explains A.", "it handles bulky goods.", "transport costs are high.")
C.arq("ar4", CLS, "Oil India Ltd is a co-operative sector industry.", "Joint sector industries are run by the state and individuals together.", 3,
      "A is false: Oil India Ltd is a joint sector industry. R is true.", "OIL is joint sector.", "this defines the joint sector.")
C.arq("ar5", MIN, "Aluminium is used in making aircraft.", "Aluminium is light, strong when alloyed and resistant to corrosion.", 0,
      "R explains A.", "aircraft need light, strong metal.", "these are aluminium's properties.")
C.arq("ar6", POL, "Pollution worsens poverty and inequality.", "Bengaluru is the electronic capital of India.", 1,
      "Both are true, but R is about the IT industry; pollution hurts the poor most because they cannot protect themselves.", "the poor suffer most.", "Bengaluru leads in electronics.")

chapter = header(SUBJ, N, "Manufacturing Industries", ["manufacturing_importance", "industry_classification", "agro_based", "mineral_based", "industrial_pollution", "industry_map"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: this chapter is fully in the board examination (Geography: 17 marks + 3 map marks). Map work from this chapter: cotton textile centres, iron and steel plants and software technology parks (given here as text questions).")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
