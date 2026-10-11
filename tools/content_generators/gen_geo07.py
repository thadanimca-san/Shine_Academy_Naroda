"""CBSE Class 10 Geography Ch 7: Lifelines of National Economy (2025-26: only map pointing in the board exam)."""
import sys
from ss_common import make, header, path, SQP, SHINE, CB

ROOT = sys.argv[1]
SUBJ, N = "geography", 7
PATH = path(SUBJ, "ch07_lifelines_of_national_economy")
C = make(SUBJ, N, "geo10ch07")
blk, M, W = C.blk, C.m, C.w
LAND, WATER, AIR, COMM, PORTS, AIRPORTS = ["roads_railways_pipelines"], ["waterways"], ["airways"], ["communication_trade"], ["sea_ports_map"], ["airports_map"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 7 exercises", "question": n}

PORTTAB = ("| Major sea port (map list) | State | Key fact |\n|---|---|---|\n| **Kandla** (Deendayal) | Gujarat | first port developed after Independence (Karachi went to Pakistan); a tidal port |\n"
           "| **Mumbai** | Maharashtra | biggest port, with a spacious natural, well-sheltered harbour |\n| **Marmagao** | Goa | premier iron ore exporting port |\n"
           "| **New Mangalore** | Karnataka | exports iron ore concentrates from Kudremukh |\n| **Kochi** | Kerala | extreme south-western port, at the entrance of a lagoon with a natural harbour |\n"
           "| **Tuticorin** | Tamil Nadu | extreme south-eastern port; natural harbour; trade with Sri Lanka and Maldives |\n| **Chennai** | Tamil Nadu | one of the oldest artificial ports; next to Mumbai in trade |\n"
           "| **Visakhapatnam** | Andhra Pradesh | deepest landlocked and well-protected port; built for iron ore exports |\n| **Paradip** | Odisha | specialises in iron ore export |\n"
           "| **Haldia** | West Bengal | subsidiary port to relieve pressure on Kolkata (an inland riverine port on the Hugli) |")
AIRTAB = ("| International airport (map list) | City / State |\n|---|---|\n| Raja Sansi (Sri Guru Ram Dass Jee) | Amritsar, Punjab |\n| Indira Gandhi | Delhi |\n| Chhatrapati Shivaji | Mumbai, Maharashtra |\n"
          "| Meenambakkam | Chennai, Tamil Nadu |\n| Netaji Subhash Chandra Bose | Kolkata, West Bengal |\n| Rajiv Gandhi | Hyderabad, Telangana |")
NW = ("| National waterway | Stretch |\n|---|---|\n| **NW 1** | Ganga between Allahabad (Prayagraj) and Haldia (1,620 km) |\n| **NW 2** | Brahmaputra between Sadiya and Dhubri (891 km) |\n"
      "| **NW 3** | West Coast Canal in Kerala: Kottapuram–Kollam, Udyogamandal and Champakkara canals (205 km) |\n"
      "| **NW 4** | stretches of the Godavari and Krishna with the Kakinada–Puducherry canals (1,078 km) |\n| **NW 5** | stretches of the Brahmani with the Matai, the Mahanadi–Brahmani delta channels and the East Coast Canal (588 km) |")

sections = [
 {"id": "s1", "title": "The veins of a nation", "blocks": [
  blk("s1.hook", "hook", title="How did your breakfast travel to you?",
    body="The wheat in your chapati may have come by train from Punjab, the tea by truck from Assam, the cooking gas through a pipeline from the coast, and the news you read by satellite. Without transport and communication, none of it would reach you.\n\n"
         "That is why roads, railways, pipelines, waterways, airways and communication are called the **lifelines of the national economy**. "
         "**Note for 2025-26:** in the board examination, this chapter is tested **only through map work** (locating and labelling major sea ports and international airports). The rest of the chapter supports the interdisciplinary project with History Chapter 3 and Economics Chapter 4."),
  blk("s1.inspiration", "inspiration", title="The Metro Man", person="E. Sreedharan", years="born 1932",
    body="Engineer **E. Sreedharan** led the building of the **Konkan Railway** along India's rugged west coast, through hills, rivers and hundreds of tunnels and bridges. It opened fully in **1998**, linking a rich coastal region that had been hard to reach.\n\n"
         "He then led the **Delhi Metro**, finishing projects on time and within budget, and earned the nickname 'Metro Man'. His work shows how transport lines change people's lives and the economy.",
    future="This chapter leads to careers in civil engineering, logistics, shipping, aviation, telecommunications and tourism."),
  C.socratic("s1.socratic", "Why are transport and communication called the lifelines of a nation's economy?",
    ["They move goods, people and information that production, trade and services depend on", "They only carry tourists", "They are needed only in big cities"], 0,
    "Efficient means of transport and communication are prerequisites for fast development."),
 ]},
 {"id": "s2", "title": "Roads, railways and pipelines", "blocks": [
  blk("s2.thm", "theory", title="Transport on land", revision=True,
    body="**Roadways:** India has one of the largest road networks in the world. Roads score over railways because:\n"
         "- the **construction cost** of roads is much **lower** than that of railway lines;\n- roads can traverse comparatively more **dissected and undulating** topography and negotiate high gradients and mountains such as the Himalayas;\n"
         "- road transport is **economical** for a few persons and small amounts of goods over **short distances**;\n- it provides **door-to-door service**, so the cost of loading and unloading is lower;\n"
         "- it is used as a **feeder** to other modes, providing a link between railway stations, air and sea ports.\n\n"
         "**Classification of roads:**\n"
         "- **Golden Quadrilateral Super Highways:** six-lane highways connecting **Delhi–Kolkata–Chennai–Mumbai–Delhi**. The **North-South corridor** links **Srinagar** (J&K) and **Kanyakumari** (Tamil Nadu); the **East-West corridor** connects **Silchar** (Assam) and **Porbandar** (Gujarat). They are implemented by the **National Highway Authority of India (NHAI)**.\n"
         "- **National Highways** link extreme parts of the country; the historical **Sher-Shah Suri Marg** is called National Highway No. 1, between Delhi and Amritsar.\n"
         "- **State Highways** link a state capital with district headquarters; built and maintained by the State Public Works Department.\n- **District roads** connect district headquarters with other places; maintained by the Zila Parishad.\n"
         "- **Other roads** (rural roads) link rural areas and villages with towns; they received a boost under the **Pradhan Mantri Grameen Sadak Yojana**.\n"
         "- **Border roads:** the **Border Roads Organisation**, set up in **1960**, builds strategic roads in the northern and north-eastern border areas.\n"
         "- **Road density** is the length of roads per 100 sq km of area. Problems: the road network is inadequate for traffic, many roads are unmetalled, highways lack side-ways and amenities, and bridges and culverts are old and narrow.\n\n"
         "**Railways:** the principal mode of transport for freight and passengers, and the largest public sector undertaking. The **first train** ran from **Mumbai to Thane in 1853**, covering **34 km**.\n"
         "- **Distribution** is influenced by physiographic, economic and administrative factors. The **northern plains**, with vast level land, high population density and rich agriculture, favour railways, though many rivers need bridges.\n"
         "- In the **peninsular** region, tracks pass through low hills, gaps or tunnels. The **Himalayan** region is unfavourable due to high relief, sparse population and lack of economic opportunities. The sandy plains of western Rajasthan, swamps of Gujarat and forested tracts of Madhya Pradesh, Chhattisgarh, Odisha and Jharkhand also make construction difficult.\n"
         "- The **Konkan Railway** along the west coast has helped movement in this important economic region, though it faces problems like **sinking of tracks and landslides**.\n"
         "- Problems: many passengers travel without tickets, and railway property is stolen or damaged.\n\n"
         "**Pipelines:** a new arrival on the transport map, used to carry **crude oil, petroleum products and natural gas** from fields to refineries, fertiliser factories and big thermal power plants. **Solids** can also be carried when converted into **slurry**. "
         "Inland refineries like **Barauni, Mathura and Panipat** and gas-based fertiliser plants became possible because of pipelines. The **initial cost is high**, but **running costs are minimal**, and pipelines **rule out trans-shipment losses or delays**. Three important networks:\n"
         "1. From the oil field in **upper Assam to Kanpur** (Uttar Pradesh), via Guwahati, Barauni and Allahabad, with branches from Barauni to Haldia, Rajbandh to Maurigram and Guwahati to Siliguri.\n"
         "2. From **Salaya** (Gujarat) to **Jalandhar** (Punjab), via Viramgam, Mathura, Delhi and Sonipat, with branches to Koyali (near Vadodara) and Chakshu.\n"
         "3. The gas pipeline from **Hazira** (Gujarat) through **Vijaipur** (Madhya Pradesh) to **Jagdishpur** (Uttar Pradesh), the **HVJ pipeline**, with branches to Kota (Rajasthan), Shahjahanpur and Babrala (Uttar Pradesh)."),
  C.kc("s2.check", "The East-West corridor connects:",
    [("Silchar and Porbandar", ""), ("Srinagar and Kanyakumari", "That is the North-South corridor."), ("Delhi and Amritsar", "That is the Sher-Shah Suri Marg."), ("Mumbai and Thane", "That was the first railway line.")],
    "Silchar is in Assam and Porbandar in Gujarat."),
  C.kc("s2.check2", "Which mode of transport rules out trans-shipment losses and delays?",
    [("Pipelines", ""), ("Railways", "Goods are loaded and unloaded at stations."), ("Roadways", "Goods are loaded and unloaded."), ("Waterways", "Goods are trans-shipped at ports.")],
    "Pipelines have a high initial cost but minimal running costs."),
 ]},
 {"id": "s3", "title": "Waterways, sea ports and airways", "blocks": [
  blk("s3.thm", "theory", title="Transport on water and in the air", revision=True,
    body="**Waterways:** the **cheapest** means of transport, most suitable for **heavy and bulky** goods. It is **fuel-efficient and environment-friendly**. India has five national waterways (see the table). Other inland waterways include the **Mandavi, Zuari and Cumberjua**, the **Sunderbans**, the **Barak** and the **backwaters of Kerala**.\n\n"
         "**Major sea ports:** with a long coastline, India has **12 major ports** and many non-major ports, which handle most of the country's foreign trade.\n"
         "- **Kandla** (also called **Deendayal Port**) in Kachchh was the **first port developed after Independence**, to ease trade on Mumbai port after the loss of **Karachi** port to Pakistan at Partition. It is a **tidal port** serving the granary and industrial belt from Jammu and Kashmir to Gujarat.\n"
         "- **Mumbai** is the **biggest port**, with a spacious **natural and well-sheltered harbour**. The **Jawaharlal Nehru Port** was planned to decongest Mumbai and serve as a hub port.\n"
         "- **Marmagao** (Goa) is the **premier iron ore exporting port**. **New Mangalore** (Karnataka) exports **iron ore concentrates from Kudremukh**. **Kochi** (Kerala) is the extreme south-western port, at the entrance of a **lagoon** with a natural harbour.\n"
         "- **Tuticorin** (Tamil Nadu) is the extreme south-eastern port with a natural harbour, trading with **Sri Lanka, Maldives** and coastal India. **Chennai** is one of the **oldest artificial ports**, next to Mumbai in volume of trade.\n"
         "- **Visakhapatnam** (Andhra Pradesh) is the **deepest landlocked and well-protected port**, originally conceived as an outlet for **iron ore** exports. **Paradip** (Odisha) specialises in **iron ore** export.\n"
         "- **Kolkata** is an **inland riverine port** serving the Ganga-Brahmaputra basin; being a tidal port, it needs constant **dredging** of the Hugli. **Haldia** was developed as a **subsidiary port** to relieve the pressure on Kolkata.\n\n"
         "**Airways:** the **fastest**, most comfortable and prestigious mode of transport. It can cover very difficult terrain like **high mountains, dreary deserts, dense forests and long oceanic stretches** with ease, and has made access to the **north-east** much easier. "
         "Air transport was **nationalised in 1953**. **Air India** provides domestic and international services. **Pawan Hans Helicopters Ltd** provides helicopter services to the **Oil and Natural Gas Corporation (ONGC)** for its offshore operations, and to inaccessible areas and difficult terrain in the north-eastern states and the interior of Jammu and Kashmir, Himachal Pradesh and Uttarakhand. Air travel is still beyond the reach of most common people."),
  blk("s3.nw", "markdown_table", title="National waterways", revision=True, body=NW),
  blk("s3.ports", "markdown_table", title="Map list: major sea ports (2025-26)", revision=True, body=PORTTAB),
  blk("s3.airports", "markdown_table", title="Map list: international airports (2025-26)", revision=True, body=AIRTAB),
  C.kc("s3.check", "Which is the deepest landlocked and well-protected port on the east coast?",
    [("Visakhapatnam", ""), ("Chennai", "Chennai is one of the oldest artificial ports."), ("Tuticorin", "Tuticorin is the extreme south-eastern port."), ("Paradip", "Paradip specialises in iron ore export.")],
    "It was first built as an outlet for iron ore exports."),
  C.kc("s3.check2", "Why was Kandla port developed soon after Independence?",
    [("To ease trade on Mumbai after Karachi port went to Pakistan", ""), ("To export tea from Assam", "Tea goes through Kolkata."), ("To replace Kochi", "Kochi is on the south-west coast."), ("To handle only fishing boats", "It is a major trade port.")],
    "Kandla (Deendayal Port) is a tidal port in Kachchh, Gujarat."),
 ]},
 {"id": "s4", "title": "Communication, trade and tourism", "blocks": [
  blk("s4.thm", "theory", title="Linking people and markets", revision=True,
    body="**Communication:** includes **personal communication** (letters, telephone) and **mass communication** (television, radio, press and films).\n"
         "- The **Indian postal network** is the **largest in the world**. **First-class mail** (cards and envelopes) is airlifted between stations; **second-class mail** (book packets, registered newspapers and periodicals) is carried by surface mail, by land and water. To speed up delivery, **six mail channels** were introduced: **Rajdhani, Metro, Green, Business, Bulk Mail and Periodical** channels.\n"
         "- India has one of the **largest telecom networks in Asia**, with STD facilities across the country.\n"
         "- Mass communication: **All India Radio (Akashwani)** broadcasts in national, regional and local languages; **Doordarshan** is one of the largest terrestrial networks in the world. India is the **largest producer of feature films** in the world. The **Central Board of Film Certification (CBFC)** certifies both Indian and foreign films.\n\n"
         "**International trade:** the exchange of goods among people, states and countries is **trade**; the **market** is the place where such exchanges happen. Trade between two countries is **international trade**, by sea, air or land. "
         "**Local trade** happens in cities, towns and villages; **state-level trade** between two or more states. The advancement of international trade is an **index of a country's economic prosperity**.\n"
         "- **Exports and imports** are the components of trade. The **balance of trade** is the difference between a country's exports and imports. When exports exceed imports, the balance is **favourable**; when imports exceed exports, it is **unfavourable**.\n"
         "- India exports agriculture and allied products, ores and minerals, **gems and jewellery**, chemicals, engineering goods and petroleum products; it imports **petroleum and crude products**, gems and precious stones, chemicals, base metals, electronic items, machinery and agricultural products.\n"
         "- India has emerged as a **software giant**, earning large foreign exchange through **information technology**.\n\n"
         "**Tourism as a trade:** tourism in India has grown substantially over the last three decades. It promotes **national integration**, supports **local handicrafts and cultural pursuits**, and helps develop international understanding of our culture and heritage. "
         "Foreign tourists come for **heritage, eco, adventure, cultural, medical and business tourism**."),
  C.kc("s4.check", "When the value of exports exceeds the value of imports, the balance of trade is:",
    [("favourable", ""), ("unfavourable", "That is when imports exceed exports."), ("zero always", "It is the difference, which can be positive or negative."), ("local trade", "That is a type of trade, not a balance.")],
    "Balance of trade = exports minus imports."),
  C.kc("s4.check2", "Which body certifies Indian and foreign films in India?",
    [("Central Board of Film Certification", ""), ("Doordarshan", "Doordarshan is a TV network."), ("All India Radio", "AIR is a radio network."), ("Pawan Hans", "Pawan Hans provides helicopter services.")],
    "India is the largest producer of feature films in the world."),
 ]},
 {"id": "s5", "title": "Remember, avoid, practise", "blocks": [
  blk("s5.memory", "memory_trick", title="Memory tricks",
    body="- **West coast ports, north to south: \"Kandla Makes Mumbai Merry, Now Kochi Tours\"** = Kandla, Mumbai, Marmagao, New Mangalore, Kochi, Tuticorin.\n"
         "- **East coast ports, south to north: \"Chennai Visits Paradip, Haldia\"** = Chennai, Visakhapatnam, Paradip, Haldia.\n"
         "- **Airports: \"A Delhi Mumbai Chennai Kolkata Hyderabad\" map** = Amritsar (Raja Sansi), Delhi (Indira Gandhi), Mumbai (Chhatrapati Shivaji), Chennai (Meenambakkam), Kolkata (Netaji Subhash Chandra Bose), Hyderabad (Rajiv Gandhi).\n"
         "- **Corridors: N-S = Srinagar–Kanyakumari; E-W = Silchar–Porbandar.**\n- **Firsts: train Mumbai–Thane 1853; air transport nationalised 1953; BRO 1960.**"),
  blk("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Marking Kolkata as the West Bengal port in the 2025-26 map list: the list names **Haldia**.\n2. Calling Mumbai an artificial port: Mumbai has a **natural** harbour; **Chennai** is one of the oldest **artificial** ports.\n"
         "3. Mixing up Marmagao (Goa, iron ore) and New Mangalore (Karnataka, Kudremukh ore).\n4. Saying the HVJ pipeline passes through Maharashtra: it links **Gujarat, Madhya Pradesh and Uttar Pradesh**.\n"
         "5. Mixing up the North-South (Srinagar–Kanyakumari) and East-West (Silchar–Porbandar) corridors.\n6. Placing Meenambakkam in Hyderabad: Meenambakkam is **Chennai**; Hyderabad's is **Rajiv Gandhi** airport."),
  blk("s5.tip", "teacher_tip", title="Try this in class",
    body="Play 'Port Pass': draw India's outline on the floor or board. Students take turns placing cards for the ten ports and six airports in the right places, saying one fact about each. "
         "Then trace the path of a tea packet from Assam to your town: which modes of transport did it use?"),
  blk("s5.reflection", "reflection", title="Think and explain",
    body="If all trucks in India stopped for a week, which goods in your home would run out first? What does this show about roads as lifelines?"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Chapter 5:** pipelines carry oil and gas; ports export iron ore from Bailadila and Kudremukh.\n- **Chapter 6:** industries need transport for raw materials and markets.\n"
         "- **History Ch 3 and Economics Ch 4:** the interdisciplinary project on global trade and globalisation."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="On an outline map of India, locate and label the ten major sea ports and six international airports from memory. Then write one fact about any five of them.\n\n"
         "**Model answer (facts):** Kandla (Gujarat) was the first port built after Independence and is a tidal port; Mumbai has the biggest natural harbour; Marmagao (Goa) is the premier iron ore port; Visakhapatnam is the deepest landlocked port; Haldia supports Kolkata port. "
         "Airports: Amritsar (Raja Sansi), Delhi (Indira Gandhi), Mumbai (Chhatrapati Shivaji), Chennai (Meenambakkam), Kolkata (Netaji Subhash Chandra Bose), Hyderabad (Rajiv Gandhi)."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Transport and communication are the lifelines of the economy.\n- Roads: Golden Quadrilateral, N-S and E-W corridors, national and state highways, district, rural and border roads.\n"
         "- Railways began in 1853 (Mumbai–Thane); pipelines carry oil, gas and slurry with low running costs; waterways are the cheapest.\n"
         "- Ten map-list sea ports and six international airports are tested on the map in 2025-26.\n"
         "- Communication, international trade (balance of trade) and tourism link India with the world."),
  blk("s5.examtips", "exam_tips", title="Board exam tips",
    body="- **2025-26:** only map work from this chapter is examined. The sample paper asked for a major sea port in West Bengal (Haldia), an international airport in Tamil Nadu (Chennai, Meenambakkam) and one in Punjab (Amritsar, Raja Sansi).\n"
         "- Learn the state of every port and airport on the list, and practise marking them with proper symbols.\n"
         "- Visually impaired candidates are asked to name these places instead of marking them."),
  blk("s5.flash1", "flashcard", front="Name the two international airports in the map list for Punjab and Tamil Nadu.", back="Amritsar (Raja Sansi – Sri Guru Ram Dass Jee) and Chennai (Meenambakkam)."),
  blk("s5.flash2", "flashcard", front="Which port is the premier iron ore exporter?", back="Marmagao, in Goa."),
  blk("s5.flash3", "flashcard", front="What is the HVJ pipeline?", back="The gas pipeline from Hazira (Gujarat) via Vijaipur (Madhya Pradesh) to Jagdishpur (Uttar Pradesh)."),
  blk("s5.flash4", "flashcard", front="What is a favourable balance of trade?", back="When the value of exports is greater than the value of imports."),
 ]},
]

# ---------------- Sample paper (map) ----------------
M("sqp19a", PORTS, "Map work (sample paper): a major sea port in West Bengal is:",
  [("Haldia", ""), ("Paradip", "Paradip is in Odisha."), ("Visakhapatnam", "Visakhapatnam is in Andhra Pradesh."), ("Tuticorin", "Tuticorin is in Tamil Nadu.")],
  "Haldia was developed to relieve the pressure on Kolkata port.", "easy", SQP(19), correct=0)
M("sqp19b", AIRPORTS, "Map work (sample paper): an international airport in Tamil Nadu is:",
  [("Chennai (Meenambakkam)", ""), ("Hyderabad (Rajiv Gandhi)", "Hyderabad is in Telangana."), ("Kolkata (Netaji Subhash Chandra Bose)", "Kolkata is in West Bengal."), ("Amritsar (Raja Sansi)", "Amritsar is in Punjab.")],
  "Meenambakkam is Chennai's international airport.", "easy", SQP(19), correct=0)
M("sqp19c", AIRPORTS, "Map work (sample paper): an international airport in Punjab is:",
  [("Amritsar (Raja Sansi – Sri Guru Ram Dass Jee)", ""), ("Delhi (Indira Gandhi)", "Delhi is not in Punjab."), ("Mumbai (Chhatrapati Shivaji)", "Mumbai is in Maharashtra."), ("Chennai (Meenambakkam)", "Chennai is in Tamil Nadu.")],
  "Raja Sansi airport serves Amritsar.", "easy", SQP(19), correct=0)

# ---------------- NCERT exercises ----------------
M("ex1i", LAND, "Which two of the following extreme locations are connected by the east-west corridor?",
  [("Mumbai and Nagpur", "Not the corridor's ends."), ("Silchar and Porbandar", ""), ("Mumbai and Kolkata", "These are on the Golden Quadrilateral."), ("Nagpur and Siliguri", "Not the corridor's ends.")],
  "The East-West corridor links Silchar (Assam) and Porbandar (Gujarat).", "easy", ex("1(i)"), correct=1)
M("ex1ii", LAND, "Which mode of transportation reduces trans-shipment losses and delays?",
  [("Railways", "Goods are loaded and unloaded."), ("Roadways", "Goods are loaded and unloaded."), ("Pipeline", ""), ("Waterways", "Goods are trans-shipped at ports.")],
  "Pipelines carry goods continuously without trans-shipment.", "easy", ex("1(ii)"), correct=2)
M("ex1iii", LAND, "Which one of the following states is not connected with the H.V.J. pipeline?",
  [("Madhya Pradesh", "Vijaipur is in Madhya Pradesh."), ("Maharashtra", ""), ("Gujarat", "Hazira is in Gujarat."), ("Uttar Pradesh", "Jagdishpur is in Uttar Pradesh.")],
  "HVJ: Hazira (Gujarat) – Vijaipur (MP) – Jagdishpur (UP).", "easy", ex("1(iii)"), correct=1)
M("ex1iv", PORTS, "Which one of the following ports is the deepest land-locked and well protected port along the east coast?",
  [("Chennai", "Chennai is an old artificial port."), ("Tuticorin", "Tuticorin is the south-eastern port."), ("Paradip", "Paradip exports iron ore."), ("Visakhapatnam", "")],
  "Visakhapatnam was built as an outlet for iron ore.", "easy", ex("1(iv)"), correct=3)
M("ex1v", LAND, "Which one of the following is the most important mode of transportation in India?",
  [("Pipeline", "Pipelines carry mainly oil and gas."), ("Railways", ""), ("Roadways", "Roads are important, but railways are the principal mode for freight and passengers."), ("Airways", "Air travel is beyond most people's reach.")],
  "Railways are the principal mode for freight and passengers.", "easy", ex("1(v)"), correct=1)
M("ex1vi", COMM, "Which one of the following terms is used to describe trade between two or more countries?",
  [("Internal trade", "That is within a country."), ("International trade", ""), ("External trade", "The textbook term is international trade."), ("Local trade", "That is within cities, towns and villages.")],
  "Trade between countries is international trade.", "easy", ex("1(vi)"), correct=1)
W("ex2i", "short_answer", LAND, "State any three merits of roadways.",
  ["Construction cost is much lower than that of railway lines, and roads can cross dissected, undulating and mountainous terrain.",
   "Road transport is economical for a few persons and small amounts of goods over short distances, with door-to-door service and low loading costs.",
   "Roads act as feeders to other modes, linking railway stations, airports and sea ports."], source=ex("2(i)"))
W("ex2ii", "short_answer", LAND, "Where and why is rail transport the most convenient means of transportation?",
  ["Rail transport is most convenient in the northern plains.", "The plains have vast level land, so construction is easy.",
   "They also have high population density and rich agricultural resources, giving plenty of passengers and freight."], source=ex("2(ii)"))
W("ex2iii", "short_answer", LAND, "What is the significance of the border roads?",
  ["The Border Roads Organisation (1960) builds roads in the northern and north-eastern border areas.", "These roads are of strategic importance for defence.",
   "They improve accessibility in difficult terrain and help the economic development of border areas."], source=ex("2(iii)"))
W("ex2iv", "short_answer", COMM, "What is meant by trade? What is the difference between international and local trade?",
  ["Trade is the exchange of goods among people, states and countries; the market is where it happens.",
   "Local trade is carried on in cities, towns and villages within a country.", "International trade is carried on between two or more countries, through sea, air or land routes."], source=ex("2(iv)"))
W("ex3i", "long_answer", COMM, "Why are the means of transportation and communication called the lifelines of a nation and its economy?",
  ["Transport moves raw materials to factories and finished goods to markets, linking producers and consumers.",
   "It moves people for work, trade and tourism across the country.",
   "Communication carries information quickly, helping business, administration and services.",
   "Together they connect remote areas, reduce regional imbalance and help national integration.",
   "They support international trade through ports and airports, so the economy cannot function without them."], source=ex("3(i)"))
W("ex3ii", "long_answer", COMM, "Write a note on the changing nature of the international trade in the last fifteen years.",
  ["International trade has grown, and India now trades with all major trading blocks and regions of the world.",
   "Exports have diversified into engineering goods, chemicals, gems and jewellery and petroleum products, besides agricultural products and minerals.",
   "India has emerged as a software giant, earning large foreign exchange from information technology services.",
   "Imports include petroleum and crude products, machinery, electronics, chemicals and gems.",
   "Better ports, airports and communication have made trade faster, and services trade has grown alongside goods."], source=ex("3(ii)"))

# ---------------- MCQs (content) ----------------
M("mcq01", LAND, "Which is NOT a merit of roadways over railways?",
  [("Roads are best for carrying very heavy goods over long distances", ""), ("Lower construction cost", "This is a merit."), ("Door-to-door service", "This is a merit."), ("Can cross mountains and undulating land", "This is a merit.")], "Railways and waterways suit heavy goods over long distances.")
M("mcq02", LAND, "The Golden Quadrilateral connects:",
  [("Delhi, Kolkata, Chennai and Mumbai", ""), ("Srinagar and Kanyakumari", "That is the N-S corridor."), ("Silchar and Porbandar", "That is the E-W corridor."), ("Delhi and Amritsar only", "That is the Sher-Shah Suri Marg.")], "It is a six-lane super highway network.")
M("mcq03", LAND, "The Golden Quadrilateral and corridors are implemented by:",
  [("the National Highway Authority of India", ""), ("the Zila Parishad", "It maintains district roads."), ("the Border Roads Organisation", "It builds border roads."), ("Pawan Hans", "It provides helicopters.")], "NHAI implements the super highways.")
M("mcq04", LAND, "The historical Sher-Shah Suri Marg runs between:",
  [("Delhi and Amritsar", ""), ("Mumbai and Thane", "That was the first railway."), ("Silchar and Porbandar", "That is the E-W corridor."), ("Hazira and Jagdishpur", "That is the HVJ pipeline.")], "It is called National Highway No. 1.")
M("mcq05", LAND, "District roads are maintained by the:",
  [("Zila Parishad", ""), ("NHAI", "NHAI handles super highways."), ("State PWD", "State PWD maintains state highways."), ("Indian Railways", "Not roads.")], "District roads connect district headquarters with other places.")
M("mcq06", LAND, "Rural roads got a special boost under the:",
  [("Pradhan Mantri Grameen Sadak Yojana", ""), ("Pradhan Mantri Krishi Sinchayee Yojana", "That is about irrigation."), ("National Jute Policy", "Unrelated."), ("Project Tiger", "Unrelated.")], "It links villages with towns.")
M("mcq07", LAND, "The Border Roads Organisation was set up in:",
  [("1960", ""), ("1853", "1853 was the first train."), ("1953", "1953 was air transport nationalisation."), ("1998", "1998 was the Konkan Railway's full opening.")], "It builds strategic border roads.")
M("mcq08", LAND, "Road density is measured as:",
  [("length of roads per 100 sq km of area", ""), ("number of vehicles per road", "That is traffic density."), ("roads per person", "Not the definition."), ("width of roads", "Not the definition.")], "It shows how well an area is served by roads.")
M("mcq09", LAND, "The first train in India ran in 1853 between:",
  [("Mumbai and Thane", ""), ("Delhi and Agra", "Not the first line."), ("Kolkata and Howrah", "Not the first line."), ("Chennai and Arakkonam", "Not the first line.")], "It covered 34 km.")
M("mcq10", LAND, "Why are railways scarce in the Himalayan region?",
  [("High relief, sparse population and lack of economic opportunities", ""), ("Too many rivers", "That affects the plains."), ("Too much flat land", "The Himalayas are mountainous."), ("Laws ban railways there", "Not the reason.")], "Physiographic and economic factors affect railways.")
M("mcq11", LAND, "The Konkan Railway faces problems like:",
  [("sinking of tracks and landslides", ""), ("desert sandstorms", "It runs along the west coast."), ("snowfall", "Not on the coast."), ("lack of passengers", "It serves an important region.")], "It runs through rugged coastal terrain.")
M("mcq12", LAND, "Pipelines made inland refineries possible at:",
  [("Barauni, Mathura and Panipat", ""), ("Kochi, Mumbai and Chennai", "These are coastal."), ("Kandla and Haldia", "These are ports."), ("Shimla and Darjeeling", "Not refinery sites.")], "Gas-based fertiliser plants also became possible.")
M("mcq13", LAND, "The pipeline from Salaya in Gujarat goes to:",
  [("Jalandhar in Punjab", ""), ("Kanpur in Uttar Pradesh", "That starts in upper Assam."), ("Jagdishpur", "That is the HVJ gas pipeline from Hazira."), ("Haldia", "That is a branch from Barauni.")], "It passes via Viramgam, Mathura, Delhi and Sonipat.")
M("mcq14", WATER, "The cheapest means of transport is:",
  [("waterways", ""), ("airways", "Airways are the costliest."), ("roadways", "Roads are costlier for bulky goods."), ("pipelines", "Pipelines carry only fluids and slurry.")], "Waterways suit heavy and bulky goods.")
M("mcq15", WATER, "National Waterway No. 1 is on the:",
  [("Ganga, between Allahabad and Haldia", ""), ("Brahmaputra, between Sadiya and Dhubri", "That is NW 2."), ("West Coast Canal in Kerala", "That is NW 3."), ("Godavari and Krishna", "That is part of NW 4.")], "It is 1,620 km long.")
M("mcq16", WATER, "National Waterway No. 2 is on the:",
  [("Brahmaputra, between Sadiya and Dhubri", ""), ("Ganga, between Allahabad and Haldia", "That is NW 1."), ("Brahmani and Mahanadi channels", "That is NW 5."), ("Mandavi and Zuari", "Those are other inland waterways.")], "It is 891 km long.")
M("mcq17", PORTS, "Which is a tidal port in Kachchh, developed after Independence?",
  [("Kandla", ""), ("Kochi", "Kochi is in Kerala."), ("Paradip", "Paradip is in Odisha."), ("Chennai", "Chennai is an old artificial port.")], "Also called Deendayal Port.")
M("mcq18", PORTS, "Which port has the biggest spacious natural, well-sheltered harbour?",
  [("Mumbai", ""), ("Chennai", "Chennai is artificial."), ("Haldia", "Haldia is a subsidiary port."), ("Kandla", "Kandla is a tidal port.")], "Mumbai is the biggest port.")
M("mcq19", PORTS, "New Mangalore port exports iron ore concentrates from:",
  [("Kudremukh", ""), ("Bailadila", "Bailadila ore goes via Visakhapatnam."), ("Badampahar", "Not this port."), ("Goa mines", "Goa ore goes via Marmagao.")], "New Mangalore is in Karnataka.")
M("mcq20", PORTS, "Which port trades with Sri Lanka and Maldives from the extreme south-east?",
  [("Tuticorin", ""), ("Kochi", "Kochi is the south-western port."), ("Haldia", "Haldia is in West Bengal."), ("Kandla", "Kandla is in Gujarat.")], "Tuticorin has a natural harbour and rich hinterland.")
M("mcq21", PORTS, "Which is one of the oldest artificial ports of India?",
  [("Chennai", ""), ("Mumbai", "Mumbai is natural."), ("Kochi", "Kochi is at a natural lagoon."), ("Tuticorin", "Tuticorin is natural.")], "Chennai is next to Mumbai in volume of trade.")
M("mcq22", PORTS, "Kolkata port needs constant dredging of the Hugli because it is:",
  [("an inland riverine tidal port", ""), ("a deep-sea port", "It is riverine."), ("a landlocked lagoon port", "That is Visakhapatnam's type."), ("an artificial port", "That is Chennai.")], "Haldia was built to relieve Kolkata.")
M("mcq23", AIR, "Air transport in India was nationalised in:",
  [("1953", ""), ("1853", "1853 was the first train."), ("1960", "1960 was the BRO."), ("1947", "1947 was Independence.")], "Air India provides domestic and international services.")
M("mcq24", AIR, "Pawan Hans Helicopters Ltd provides services to:",
  [("ONGC offshore operations and inaccessible hilly areas", ""), ("only foreign tourists", "Not only tourists."), ("railway passengers", "Not railways."), ("cargo ships", "Not ships.")], "It serves the north-east, J&K, Himachal and Uttarakhand.")
M("mcq25", COMM, "The largest postal network in the world belongs to:",
  [("India", ""), ("China", "The textbook names India."), ("USA", "The textbook names India."), ("Russia", "The textbook names India.")], "Six mail channels speed up delivery.")
M("mcq26", COMM, "Which is NOT one of the six mail channels?",
  [("Express Channel", ""), ("Rajdhani Channel", "This is a mail channel."), ("Green Channel", "This is a mail channel."), ("Bulk Mail Channel", "This is a mail channel.")], "The six are Rajdhani, Metro, Green, Business, Bulk Mail and Periodical.")
M("mcq27", COMM, "First-class mail includes:",
  [("cards and envelopes, airlifted between stations", ""), ("book packets", "That is second-class mail."), ("registered newspapers", "That is second-class mail."), ("periodicals", "That is second-class mail.")], "Second-class mail goes by surface.")
M("mcq28", COMM, "India is the largest producer in the world of:",
  [("feature films", ""), ("television sets", "Not stated."), ("newspapers in English", "Not stated."), ("satellites", "Not stated.")], "CBFC certifies the films.")
M("mcq29", COMM, "The balance of trade is:",
  [("the difference between a country's exports and imports", ""), ("the total of exports and imports", "It is the difference."), ("only exports", "It compares both."), ("only imports", "It compares both.")], "It can be favourable or unfavourable.")
M("mcq30", COMM, "When imports exceed exports, the balance of trade is:",
  [("unfavourable", ""), ("favourable", "That is when exports exceed imports."), ("local", "Not a balance."), ("neutral always", "It is unfavourable.")], "India imports much petroleum.")
M("mcq31", COMM, "India has emerged as a giant in:",
  [("software", ""), ("automobile exports only", "The textbook names software."), ("crude oil exports", "India imports crude oil."), ("raw jute imports", "India produces jute.")], "IT earns large foreign exchange.")
M("mcq32", COMM, "Which is a benefit of tourism named in the chapter?",
  [("It promotes national integration and supports local handicrafts", ""), ("It increases pollution only", "Not a benefit."), ("It reduces foreign exchange", "It earns foreign exchange."), ("It stops cultural exchange", "It increases understanding.")], "Heritage, eco, adventure, cultural, medical and business tourism attract visitors.")
# ---------------- Map work (ports and airports) ----------------
M("map1", PORTS, "Map work: Marmagao port is in:",
  [("Goa", ""), ("Karnataka", "New Mangalore is in Karnataka."), ("Kerala", "Kochi is in Kerala."), ("Gujarat", "Kandla is in Gujarat.")], "Marmagao is the premier iron ore port.", "medium")
M("map2", PORTS, "Map work: Paradip port is in:",
  [("Odisha", ""), ("West Bengal", "Haldia is in West Bengal."), ("Andhra Pradesh", "Visakhapatnam is in Andhra Pradesh."), ("Tamil Nadu", "Chennai and Tuticorin are in Tamil Nadu.")], "Paradip exports iron ore.", "medium")
M("map3", PORTS, "Map work: which two map-list ports are in Tamil Nadu?",
  [("Chennai and Tuticorin", ""), ("Kochi and Tuticorin", "Kochi is in Kerala."), ("Chennai and Visakhapatnam", "Visakhapatnam is in Andhra Pradesh."), ("Paradip and Haldia", "These are in Odisha and West Bengal.")], "Chennai is on the east coast; Tuticorin is at the south-eastern tip.", "medium")
M("map4", PORTS, "Map work: the port in Kerala on the map list is:",
  [("Kochi", ""), ("New Mangalore", "That is in Karnataka."), ("Marmagao", "That is in Goa."), ("Tuticorin", "That is in Tamil Nadu.")], "Kochi is at the entrance of a lagoon.", "medium")
M("map5", PORTS, "Map work: Kandla port is in:",
  [("Gujarat", ""), ("Maharashtra", "Mumbai is in Maharashtra."), ("Goa", "Marmagao is in Goa."), ("Karnataka", "New Mangalore is in Karnataka.")], "Kandla is in Kachchh.", "medium")
M("map6", PORTS, "Map work: Visakhapatnam port is in:",
  [("Andhra Pradesh", ""), ("Odisha", "Paradip is in Odisha."), ("Tamil Nadu", "Chennai is in Tamil Nadu."), ("West Bengal", "Haldia is in West Bengal.")], "It is the deepest landlocked port.", "medium")
M("map7", PORTS, "Map work: which map-list port is on the west coast?",
  [("New Mangalore", ""), ("Paradip", "Paradip is on the east coast."), ("Haldia", "Haldia is on the east coast."), ("Visakhapatnam", "Visakhapatnam is on the east coast.")], "West coast: Kandla, Mumbai, Marmagao, New Mangalore, Kochi.", "medium")
M("map8", AIRPORTS, "Map work: Meenambakkam international airport is at:",
  [("Chennai", ""), ("Hyderabad", "Hyderabad's airport is Rajiv Gandhi."), ("Kolkata", "Kolkata's airport is Netaji Subhash Chandra Bose."), ("Mumbai", "Mumbai's airport is Chhatrapati Shivaji.")], "Chennai is in Tamil Nadu.", "medium")
M("map9", AIRPORTS, "Map work: the Rajiv Gandhi international airport is at:",
  [("Hyderabad", ""), ("Delhi", "Delhi's airport is Indira Gandhi."), ("Amritsar", "Amritsar's airport is Raja Sansi."), ("Chennai", "Chennai's airport is Meenambakkam.")], "Hyderabad is in Telangana.", "medium")
M("map10", AIRPORTS, "Map work: the Netaji Subhash Chandra Bose international airport is at:",
  [("Kolkata", ""), ("Delhi", "Delhi's airport is Indira Gandhi."), ("Mumbai", "Mumbai's airport is Chhatrapati Shivaji."), ("Hyderabad", "Hyderabad's airport is Rajiv Gandhi.")], "Kolkata is in West Bengal.", "medium")
M("map11", AIRPORTS, "Map work: the Chhatrapati Shivaji international airport is at:",
  [("Mumbai", ""), ("Pune", "Not on the map list."), ("Chennai", "Chennai's is Meenambakkam."), ("Delhi", "Delhi's is Indira Gandhi.")], "Mumbai is in Maharashtra.", "medium")
M("map12", AIRPORTS, "Map work: which international airport is in Delhi?",
  [("Indira Gandhi", ""), ("Rajiv Gandhi", "That is Hyderabad."), ("Raja Sansi", "That is Amritsar."), ("Meenambakkam", "That is Chennai.")], "Indira Gandhi International Airport, Delhi.", "medium")
W("map13", "very_short_answer", PORTS, "Map work: name (a) the premier iron ore exporting port and its state, and (b) the subsidiary port built to relieve Kolkata.",
  ["(a) Marmagao, Goa.", "(b) Haldia, West Bengal."])
W("map14", "very_short_answer", AIRPORTS, "Map work: name the international airports of (a) Punjab and (b) Telangana.",
  ["(a) Amritsar (Raja Sansi – Sri Guru Ram Dass Jee).", "(b) Hyderabad (Rajiv Gandhi)."])
W("map15", "very_short_answer", PORTS, "Map work: name two major sea ports each on (a) the west coast and (b) the east coast from the map list.",
  ["(a) Any two of Kandla, Mumbai, Marmagao, New Mangalore, Kochi.", "(b) Any two of Tuticorin, Chennai, Visakhapatnam, Paradip, Haldia."])
# ---------------- True / false ----------------
C.tf("tf1", PORTS, "Chennai is one of the oldest artificial ports of India.", True, "It is next to Mumbai in volume of trade.")
C.tf("tf2", LAND, "The North-South corridor links Silchar and Porbandar.", False, "The N-S corridor links Srinagar and Kanyakumari; Silchar–Porbandar is the E-W corridor.")
C.tf("tf3", WATER, "Waterways are the cheapest means of transport.", True, "They suit heavy and bulky goods and are fuel-efficient.")
C.tf("tf4", AIRPORTS, "Meenambakkam international airport is in Hyderabad.", False, "Meenambakkam is in Chennai; Hyderabad has the Rajiv Gandhi airport.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", LAND, "State two advantages of pipelines.",
  ["Running costs are minimal after the high initial cost.", "They rule out trans-shipment losses and delays, and can carry solids as slurry."])
W("vsa2", "very_short_answer", PORTS, "Why was Haldia port developed?",
  ["Kolkata is an inland riverine tidal port that needs constant dredging of the Hugli.", "Haldia was developed as a subsidiary port to relieve the growing pressure on Kolkata."])
W("vsa3", "very_short_answer", AIR, "Why is air transport important for the north-eastern states?",
  ["The north-east has difficult terrain of hills, forests and rivers.", "Air transport covers such terrain with ease and has made access to the region much easier."])
W("sa1", "short_answer", PORTS, "Describe any three major sea ports of India's west coast.",
  ["Kandla (Gujarat): the first port developed after Independence to ease trade on Mumbai after Karachi went to Pakistan; a tidal port.",
   "Mumbai (Maharashtra): the biggest port, with a spacious natural and well-sheltered harbour.",
   "Marmagao (Goa): the premier iron ore exporting port (also New Mangalore for Kudremukh ore, and Kochi at a lagoon)."])
W("sa2", "short_answer", LAND, "Describe the three important pipeline networks of India.",
  ["From upper Assam to Kanpur (UP) via Guwahati, Barauni and Allahabad, with branches to Haldia and Siliguri.",
   "From Salaya (Gujarat) to Jalandhar (Punjab) via Viramgam, Mathura, Delhi and Sonipat.",
   "The HVJ gas pipeline from Hazira (Gujarat) via Vijaipur (MP) to Jagdishpur (UP), with branches to Kota, Shahjahanpur and Babrala."])
W("la1", "long_answer", LAND, "Describe the classification of roads in India.",
  ["Golden Quadrilateral super highways link Delhi, Kolkata, Chennai and Mumbai; N-S (Srinagar–Kanyakumari) and E-W (Silchar–Porbandar) corridors; built by NHAI.",
   "National highways link extreme parts of the country; Sher-Shah Suri Marg (Delhi–Amritsar) is NH 1.",
   "State highways link state capitals with district headquarters; maintained by the State PWD.",
   "District roads link district headquarters with other places (Zila Parishad); rural roads link villages with towns under PMGSY.",
   "Border roads built by the Border Roads Organisation (1960) serve strategic northern and north-eastern border areas."])
W("cb1", "case_based", PORTS, "Read the source and answer the questions.\n\n*\"Kandla in Kuchchh was the first port developed soon after Independence to ease the volume of trade on the Mumbai port, in the wake of loss of Karachi port to Pakistan after the Partition. Kandla, also known as the Deendayal Port, is a tidal port.\"* (NCERT)\n\n"
  "(i) Why was Kandla port developed? (1)\n\n(ii) What type of port is Kandla? (1)\n\n(iii) Name two other major ports on the west coast and one fact about each. (2)",
  ["(i) To ease trade on Mumbai port after Karachi port went to Pakistan at Partition.", "(ii) A tidal port.",
   "(iii) Any two: Mumbai has the biggest natural harbour; Marmagao is the premier iron ore port; New Mangalore exports Kudremukh ore; Kochi is at the entrance of a lagoon."])
W("cb2", "case_based", COMM, "Read the source and answer the questions.\n\n*\"Exports and imports are the components of trade. The balance of trade of a country is the difference between its export and import. When the value of export exceeds the value of imports, it is called a favourable balance of trade.\"* (NCERT)\n\n"
  "(i) What are the two components of trade? (1)\n\n(ii) What is an unfavourable balance of trade? (1)\n\n(iii) Name two goods India exports and two it imports. (2)",
  ["(i) Exports and imports.", "(ii) When the value of imports exceeds the value of exports.",
   "(iii) Exports: gems and jewellery, engineering goods, chemicals, agricultural products, petroleum products; imports: petroleum and crude products, machinery, electronic items, gems (any two each)."])
# ---------------- Assertion-reason ----------------
C.arq("ar1", LAND, "Railways are dense in the northern plains.", "The plains have vast level land, high population density and rich agriculture.", 0,
      "R explains A.", "the plains favour railways.", "these are favourable factors.")
C.arq("ar2", LAND, "Pipelines have reduced trans-shipment losses.", "Pipelines carry oil and gas continuously from fields to refineries and plants.", 0,
      "R explains A.", "goods need not be reloaded.", "pipelines carry fluids directly.")
C.arq("ar3", PORTS, "Visakhapatnam is the deepest landlocked and well-protected port.", "It was originally built as an outlet for iron ore exports.", 1,
      "Both are true, but R tells its purpose, not why it is deep and protected.", "it is landlocked and deep.", "it was built for iron ore.")
C.arq("ar4", PORTS, "Mumbai has an artificial harbour.", "Chennai is one of the oldest artificial ports.", 3,
      "A is false: Mumbai has a natural harbour. R is true.", "Mumbai's harbour is natural.", "Chennai is artificial.")
C.arq("ar5", AIR, "Air transport has made access to the north-east easier.", "Airways can cover high mountains, dense forests and long stretches with ease.", 0,
      "R explains A.", "the north-east has difficult terrain.", "airways cross such terrain.")
C.arq("ar6", COMM, "A favourable balance of trade means imports exceed exports.", "Balance of trade is the difference between exports and imports.", 3,
      "A is false: favourable means exports exceed imports. R is true.", "that is unfavourable.", "this defines balance of trade.")

chapter = header(SUBJ, N, "Lifelines of National Economy", ["roads_railways_pipelines", "waterways", "airways", "communication_trade", "sea_ports_map", "airports_map"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: from this chapter, ONLY map pointing is evaluated in the board examination (locating and labelling the major sea ports Kandla, Mumbai, Marmagao, New Mangalore, Kochi, Tuticorin, Chennai, Visakhapatnam, Paradip, Haldia, and the international airports Amritsar, Delhi, Mumbai, Chennai, Kolkata, Hyderabad). The rest of the chapter supports the interdisciplinary project with History Ch 3 and Economics Ch 4 and is not tested in the board exam. Map items are given here as text questions.")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
