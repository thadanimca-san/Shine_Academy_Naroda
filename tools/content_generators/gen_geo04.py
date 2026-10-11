"""CBSE Class 10 Geography Ch 4: Agriculture (fully in the 2025-26 board syllabus; map: crop areas and producer states)."""
import sys
from ss_common import make, header, path, SQP, SHINE, CB

ROOT = sys.argv[1]
SUBJ, N = "geography", 4
PATH = path(SUBJ, "ch04_agriculture")
C = make(SUBJ, N, "geo10ch04")
blk, M, W = C.blk, C.m, C.w
TYPES, SEAS, FOOD, NONFOOD, REF, MAP = ["farming_types"], ["cropping_seasons"], ["food_crops"], ["non_food_crops"], ["agri_reforms"], ["crops_map"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 4 exercises", "question": n}

SLASH = ("| Region | Local name of slash-and-burn farming |\n|---|---|\n| North-eastern states (Assam, Meghalaya, Mizoram, Nagaland) | **Jhumming** |\n| Madhya Pradesh | Bewar or Dahiya |\n| Andhra Pradesh | Podu or Penda |\n"
         "| Odisha | Pama Dabi, Koman or Bringa |\n| Western Ghats | Kumari |\n| South-eastern Rajasthan | Valre or Waltre |\n| Himalayan belt | Khil |\n| Jharkhand | Kuruwa |")
SEASONS = ("| Season | Sown | Harvested | Main crops |\n|---|---|---|---|\n| **Rabi** | winter, October to December | summer, April to June | wheat, barley, peas, gram, mustard |\n"
           "| **Kharif** | with the onset of monsoon | September to October | paddy, maize, jowar, bajra, tur (arhar), moong, urad, cotton, jute, groundnut, soyabean |\n"
           "| **Zaid** | short summer season between rabi and kharif | summer | watermelon, muskmelon, cucumber, vegetables, fodder crops |")
CROPS = ("| Crop | Season | Climate and soil | Major states |\n|---|---|---|---|\n"
         "| **Rice** | kharif | above 25°C, high humidity, rainfall above 100 cm (irrigation where less) | West Bengal, Uttar Pradesh, Punjab, plains of north and north-east, coastal and deltaic areas |\n"
         "| **Wheat** | rabi | cool growing season, bright sunshine at ripening, 50-75 cm rainfall | Punjab, Haryana, Uttar Pradesh, Madhya Pradesh, Bihar, Rajasthan |\n"
         "| **Maize** | kharif (rabi too in Bihar) | 21°C to 27°C, old alluvial soil | Karnataka, Madhya Pradesh, Uttar Pradesh, Bihar, Andhra Pradesh, Telangana |\n"
         "| **Sugarcane** | about a year | 21°C to 27°C, hot humid, 75-100 cm rainfall | Uttar Pradesh, Maharashtra, Karnataka, Tamil Nadu, Andhra Pradesh, Telangana, Bihar, Punjab, Haryana |\n"
         "| **Tea** | plantation | warm, moist, frost-free; deep fertile well-drained soil rich in humus | Assam, Darjeeling and Jalpaiguri (West Bengal), Tamil Nadu, Kerala |\n"
         "| **Coffee** | plantation | Arabica variety; hill slopes | Karnataka, Kerala, Tamil Nadu (Nilgiris) |\n"
         "| **Rubber** | plantation | above 25°C, rainfall over 200 cm, moist and humid | Kerala, Tamil Nadu, Karnataka, Andaman and Nicobar, Garo hills (Meghalaya) |\n"
         "| **Cotton** | kharif, 6-8 months | black soil, high temperature, light rain, 210 frost-free days | Maharashtra, Gujarat, Madhya Pradesh, Karnataka, Telangana, Andhra Pradesh, Tamil Nadu, Punjab, Haryana, Uttar Pradesh |\n"
         "| **Jute** | kharif | fertile floodplain soils renewed every year, high temperature | West Bengal, Bihar, Assam, Odisha, Meghalaya |")

sections = [
 {"id": "s1", "title": "The land that feeds a billion", "blocks": [
  blk("s1.hook", "hook", title="Why is the same rice a business in Punjab and dinner in Odisha?",
    body="A farmer in Punjab grows rice and sells almost all of it to government procurement centres. A farmer in Odisha grows rice too, but keeps most of it to feed the family. Same crop, two very different kinds of farming.\n\n"
         "India is an agriculturally important country: about **two-thirds** of its population is engaged in agricultural activities. This chapter explains the types of farming, the cropping seasons, where our major crops grow, and the reforms that changed Indian agriculture."),
  blk("s1.inspiration", "inspiration", title="The scientist who fed India", person="M. S. Swaminathan", years="1925–2023",
    body="In the 1960s India depended on food imports and feared famine. Agricultural scientist **M. S. Swaminathan** worked with farmers to test new **high-yielding varieties (HYV)** of wheat in Punjab and other states.\n\n"
         "Wheat harvests soared, and India became largely self-sufficient in grain. This became known as the **Green Revolution**. Later he warned that soil and water must be protected too, calling for an 'evergreen revolution'.",
    future="This chapter leads to careers in agricultural science, agronomy, food technology, horticulture and agri-business."),
  C.socratic("s1.socratic", "Why is rice a commercial crop in Punjab but a subsistence crop in Odisha?",
    ["Punjab has assured irrigation, modern inputs and access to markets; Odisha's farming is more rain-fed and for family use", "Odisha does not grow rice", "Rice grows only in Punjab"], 0,
    "The degree of commercialisation depends on irrigation, technology and markets, not just on the crop."),
 ]},
 {"id": "s2", "title": "Types of farming", "blocks": [
  blk("s2.thm", "theory", title="Subsistence, commercial and plantation farming", revision=True,
    body="Agriculture is an age-old economic activity in India. Farming varies from **subsistence to commercial** type, depending on physical environment, technology and socio-cultural practices.\n\n"
         "**1. Primitive subsistence farming:** practised on small patches of land with **primitive tools** like the hoe, dao and digging sticks, and **family or community labour**. It depends on **monsoon**, the natural fertility of the soil and suitability of other environmental conditions. "
         "It is **'slash and burn' agriculture**: farmers clear a patch of land and produce cereals and other food crops to sustain their family. When the soil fertility decreases, farmers shift and clear a fresh patch. This allows nature to replenish the fertility of the soil through natural processes. "
         "Land productivity is low because the farmer does not use fertilisers or other modern inputs. It is known by different names in different parts of the country (see the table); in the north-eastern states it is called **jhumming**.\n\n"
         "**2. Intensive subsistence farming:** practised in areas of **high population pressure** on land. It is **labour-intensive**, with high doses of **biochemical inputs and irrigation** for higher production. "
         "Though the 'right of inheritance' leads to the **division of land** among successive generations and makes land-holding size uneconomical, farmers continue to take maximum output from the limited land because they have no alternative source of livelihood.\n\n"
         "**3. Commercial farming:** uses **higher doses of modern inputs**: **high-yielding variety (HYV) seeds, chemical fertilisers, insecticides and pesticides**. The degree of commercialisation varies from region to region: for example, **rice** is a commercial crop in **Punjab and Haryana**, but in **Odisha** it is a **subsistence** crop.\n\n"
         "**4. Plantation farming:** a type of commercial farming in which a **single crop** is grown on a **large area**. It has an interface of agriculture and industry. Plantations cover large tracts of land, use **capital-intensive inputs** and **migrant labourers**; all the produce is used as raw material in industries. "
         "Important plantation crops are **tea, coffee, rubber, sugarcane and banana**. **Tea in Assam and North Bengal** and **coffee in Karnataka** are important plantation crops. Since production is mainly for the market, a well-developed network of transport and communication connecting plantations, processing industries and markets plays an important role."),
  blk("s2.table", "markdown_table", title="Slash-and-burn farming in India: local names", revision=True, body=SLASH),
  C.kc("s2.check", "In which type of farming is a single crop grown on a large area for industry?",
    [("Plantation farming", ""), ("Primitive subsistence farming", "That is small-scale, for the family."), ("Intensive subsistence farming", "That grows food on small, crowded holdings."), ("Jhumming", "Jhumming is slash-and-burn farming.")],
    "Tea, coffee, rubber, sugarcane and banana are plantation crops."),
  C.kc("s2.check2", "What is slash-and-burn farming called in the north-eastern states?",
    [("Jhumming", ""), ("Podu", "Podu is in Andhra Pradesh."), ("Bewar", "Bewar is in Madhya Pradesh."), ("Kuruwa", "Kuruwa is in Jharkhand.")],
    "In the north-east it is called jhumming."),
 ]},
 {"id": "s3", "title": "Cropping seasons", "blocks": [
  blk("s3.thm", "theory", title="Rabi, kharif and zaid", revision=True,
    body="India has three major cropping seasons.\n\n"
         "**Rabi:** crops are sown in **winter from October to December** and harvested in **summer from April to June**. Important rabi crops are **wheat, barley, peas, gram and mustard**. They are grown in large parts of India, but states from the north and north-western parts such as **Punjab, Haryana, Himachal Pradesh, Jammu and Kashmir, Uttarakhand and Uttar Pradesh** are important for wheat and other rabi crops. "
         "Precipitation during winter from **western temperate cyclones** helps the success of these crops. The success of the **Green Revolution** in Punjab, Haryana, western Uttar Pradesh and parts of Rajasthan has also been important.\n\n"
         "**Kharif:** crops are grown with the **onset of monsoon** in different parts of the country and harvested in **September-October**. Important kharif crops are **paddy, maize, jowar, bajra, tur (arhar), moong, urad, cotton, jute, groundnut and soyabean**. "
         "Important rice-growing regions are **Assam, West Bengal, coastal Odisha, Andhra Pradesh, Telangana, Tamil Nadu, Kerala and Maharashtra, particularly the Konkan coast**, along with **Uttar Pradesh and Bihar**; recently paddy has also become an important crop of **Punjab and Haryana**. "
         "In **Assam, West Bengal and Odisha**, **three crops of paddy** are grown in a year: **Aus, Aman and Boro**.\n\n"
         "**Zaid:** a **short season during the summer months**, between the rabi and kharif seasons. Crops include **watermelon, muskmelon, cucumber, vegetables and fodder crops**. **Sugarcane** takes almost a year to grow."),
  blk("s3.table", "markdown_table", title="The three cropping seasons", revision=True, body=SEASONS),
  C.kc("s3.check", "Which crop is a rabi crop?",
    [("Wheat", ""), ("Paddy", "Paddy is a kharif crop."), ("Watermelon", "Watermelon is a zaid crop."), ("Cotton", "Cotton is a kharif crop.")],
    "Wheat is sown October-December and harvested April-June."),
  C.kc("s3.check2", "Aus, Aman and Boro are three crops of paddy grown in:",
    [("Assam, West Bengal and Odisha", ""), ("Punjab and Haryana", "These grow one main paddy crop."), ("Rajasthan", "Rajasthan is dry."), ("Kerala only", "The chapter names Assam, West Bengal and Odisha.")],
    "Three paddy crops a year are grown there."),
 ]},
 {"id": "s4", "title": "Major crops: grains", "blocks": [
  blk("s4.thm", "theory", title="Rice, wheat, millets, maize and pulses", revision=True,
    body="A variety of food and non-food crops are grown in different parts of India, depending on soil, climate and cultivation practices.\n\n"
         "**Rice:** the **staple food crop** of a majority of the people in India. India is the **second largest producer of rice** in the world after **China**. It is a **kharif** crop which requires **high temperature (above 25°C)**, **high humidity** and **annual rainfall above 100 cm**; in areas of less rainfall it grows with the help of **irrigation**. "
         "Rice is grown in the plains of north and north-eastern India, coastal areas and deltaic regions. Development of a dense network of **canal irrigation and tubewells** has made it possible to grow rice in areas of less rainfall such as **Punjab, Haryana, western Uttar Pradesh and parts of Rajasthan**.\n\n"
         "**Wheat:** the second most important cereal crop and the main food crop in the **north and north-western** part of the country. This **rabi** crop requires a **cool growing season** and **bright sunshine at the time of ripening**, with **50 to 75 cm** of annual rainfall evenly distributed over the growing season. "
         "There are two important wheat-growing zones: the **Ganga-Satluj plains** in the north-west and the **black soil region of the Deccan**. Major wheat-producing states are **Punjab, Haryana, Uttar Pradesh, Madhya Pradesh, Bihar and Rajasthan**.\n\n"
         "**Millets:** **jowar, bajra and ragi** are the important millets grown in India. Though known as **coarse grains**, they have **very high nutritional value**: ragi is very rich in **iron, calcium**, other micronutrients and roughage.\n"
         "- **Jowar** is the third most important food crop with respect to area and production. It is **rain-fed**, grown mostly in moist areas, hardly needing irrigation. **Maharashtra** is the largest producer, followed by Karnataka, Andhra Pradesh and Madhya Pradesh.\n"
         "- **Bajra** grows well on **sandy soils and shallow black soil**. **Rajasthan** is the largest producer, followed by Uttar Pradesh, Maharashtra, Gujarat and Haryana.\n"
         "- **Ragi** is a crop of **dry regions** and grows well on red, black, sandy, loamy and shallow black soils. **Karnataka** is the largest producer, followed by Tamil Nadu; it is also grown in Himachal Pradesh, Uttarakhand, Sikkim, Jharkhand and Arunachal Pradesh.\n\n"
         "**Maize:** used both as **food and fodder**. It is a **kharif** crop which requires a temperature between **21°C and 27°C** and grows well in **old alluvial soil**; in states like **Bihar**, maize is grown in the **rabi** season too. Use of HYV seeds, fertilisers and irrigation has increased its production. "
         "Major states: **Karnataka, Madhya Pradesh, Uttar Pradesh, Bihar, Andhra Pradesh and Telangana**.\n\n"
         "**Pulses:** India is the **largest producer as well as consumer of pulses** in the world. They are the major source of **protein** in a vegetarian diet. Major pulses are **tur (arhar), urad, moong, masur, peas and gram**. They need **less moisture** and survive even in dry conditions. "
         "Being **leguminous** crops, all these crops **except arhar** help in **restoring soil fertility by fixing nitrogen from the air**, so they are mostly grown in **rotation** with other crops. Major pulse-producing states are **Madhya Pradesh, Rajasthan, Maharashtra, Uttar Pradesh and Karnataka**."),
  blk("s4.crops", "markdown_table", title="Major crops at a glance", revision=True, body=CROPS),
  C.kc("s4.check", "Which millet is very rich in iron and calcium?",
    [("Ragi", ""), ("Jowar", "Jowar is the third most important food crop by area and production."), ("Bajra", "Bajra grows on sandy and shallow black soils."), ("Maize", "Maize is not a millet in the chapter's list.")],
    "Ragi is rich in iron, calcium, other micronutrients and roughage."),
  C.kc("s4.check2", "Which state is the largest producer of bajra?",
    [("Rajasthan", ""), ("Maharashtra", "Maharashtra is the largest producer of jowar."), ("Karnataka", "Karnataka is the largest producer of ragi."), ("Punjab", "Punjab is known for wheat and rice.")],
    "Bajra grows well on the sandy soils of Rajasthan."),
 ]},
 {"id": "s5", "title": "Major crops: beyond grains", "blocks": [
  blk("s5.thm", "theory", title="Sugarcane, oilseeds, tea, coffee, horticulture and fibres", revision=True,
    body="**Sugarcane:** a tropical as well as subtropical crop. It grows well in **hot and humid climate** with a temperature of **21°C to 27°C** and annual rainfall between **75 cm and 100 cm**; irrigation is required in regions of low rainfall. It can be grown on a variety of soils and needs **manual labour** from sowing to harvesting. "
         "India is the **second largest producer of sugarcane** after **Brazil**. It is the main source of **sugar, gur (jaggery), khandsari and molasses**. Major states: **Uttar Pradesh, Maharashtra, Karnataka, Tamil Nadu, Andhra Pradesh, Telangana, Bihar, Punjab and Haryana**.\n\n"
         "**Oilseeds:** different oilseeds cover about **12 per cent** of the total cropped area of the country. The main oilseeds are **groundnut, mustard, coconut, sesamum (til), soyabean, castor seeds, cotton seeds, linseed and sunflower**. Most are edible and used as cooking mediums; some are also used as raw material for soap, cosmetics and ointments. "
         "**Groundnut** is a **kharif** crop and accounts for about half of the major oilseeds produced in the country; **Gujarat** was the largest producer of groundnut, followed by Rajasthan and Tamil Nadu (2019-20). **Linseed and mustard** are **rabi** crops; **sesamum** is a **kharif crop in the north and a rabi crop in south India**; **castor seed** is grown as both rabi and kharif crop.\n\n"
         "**Tea:** an important beverage crop introduced in India initially by the **British**. Today most tea plantations are owned by Indians. The tea plant grows well in **tropical and subtropical climates** endowed with **deep and fertile well-drained soil, rich in humus and organic matter**. "
         "Tea bushes require a **warm and moist frost-free climate** all through the year, and **frequent showers evenly distributed** over the year ensure continuous growth of tender leaves. Tea is a **labour-intensive** industry needing abundant, cheap and skilled labour; it is processed within the tea garden to keep it fresh. "
         "Major tea-producing states are **Assam, the hills of Darjeeling and Jalpaiguri districts (West Bengal), Tamil Nadu and Kerala**; also Himachal Pradesh, Uttarakhand, Meghalaya, Andhra Pradesh and Tripura.\n\n"
         "**Coffee:** Indian coffee is known in the world for its good quality. The **Arabica** variety, initially brought from **Yemen**, is produced in the country. Its cultivation was introduced on the **Baba Budan Hills** and even today it is confined to the **Nilgiri** in **Karnataka, Kerala and Tamil Nadu**.\n\n"
         "**Horticulture crops:** India is a major producer of **fruits and vegetables** in the world, of both tropical and temperate varieties. Mangoes of **Maharashtra, Andhra Pradesh, Telangana, Uttar Pradesh and West Bengal**; oranges of **Nagpur and Cherrapunji (Meghalaya)**; bananas of **Kerala, Mizoram, Maharashtra and Tamil Nadu**; lichi and guava of **Uttar Pradesh and Bihar**; pineapples of **Meghalaya**; grapes of **Andhra Pradesh, Telangana and Maharashtra**; and apples, pears, apricots and walnuts of **Jammu and Kashmir and Himachal Pradesh** are in great demand.\n\n"
         "**Non-food crops:**\n"
         "- **Rubber:** an **equatorial** crop, but under special conditions also grown in tropical and sub-tropical areas. It requires a **moist and humid climate** with **rainfall of more than 200 cm** and a **temperature above 25°C**. It is an important industrial raw material, grown mainly in **Kerala, Tamil Nadu, Karnataka, the Andaman and Nicobar Islands and the Garo hills of Meghalaya**.\n"
         "- **Fibre crops:** **cotton, jute, hemp and natural silk**. The first three come from crops grown in the soil; silk is obtained from cocoons of silkworms fed on green mulberry leaves. Rearing silkworms for silk is called **sericulture**.\n"
         "- **Cotton:** India is believed to be the **original home of the cotton plant**. Cotton grows well in the drier parts of the **black cotton soil of the Deccan plateau**. It requires **high temperature, light rainfall or irrigation, 210 frost-free days and bright sunshine**. It is a **kharif** crop taking **6 to 8 months** to mature. "
         "Major states: **Maharashtra, Gujarat, Madhya Pradesh, Karnataka, Andhra Pradesh, Telangana, Tamil Nadu, Punjab, Haryana and Uttar Pradesh**.\n"
         "- **Jute:** known as the **golden fibre**. It grows well on well-drained fertile soils in the **flood plains where soils are renewed every year**; **high temperature** is required during growth. **West Bengal, Bihar, Assam, Odisha and Meghalaya** are the major producers. It is used for gunny bags, mats, ropes, yarn, carpets and other artefacts. "
         "Due to its high cost, it is losing the market to **synthetic fibres** and packing materials, particularly **nylon**."),
  C.kc("s5.check", "Which crop needs more than 200 cm of rainfall and temperature above 25°C?",
    [("Rubber", ""), ("Cotton", "Cotton needs light rainfall."), ("Wheat", "Wheat needs 50-75 cm."), ("Sugarcane", "Sugarcane needs 75-100 cm.")],
    "Rubber is an equatorial crop of moist, humid climates."),
  C.kc("s5.check2", "Why is jute called the 'golden fibre', and why is it losing its market?",
    [("For its golden colour and value; it is losing out to cheaper synthetic fibres like nylon", ""), ("It is mined like gold; it is running out", "Jute is a crop, not a mineral."),
     ("It grows only in deserts; deserts are shrinking", "Jute grows in fertile floodplains."), ("It is used for jewellery; jewellery is out of fashion", "It is used for bags, mats and ropes.")],
    "Its high cost makes it lose the market to synthetic packing materials."),
 ]},
 {"id": "s6", "title": "Reforms in agriculture", "blocks": [
  blk("s6.thm", "theory", title="Technological and institutional reforms", revision=True,
    body="Agriculture has been practised in India for thousands of years, and sustained use of land without matching technological and institutional changes hindered its development. Despite irrigation, most farmers still depend on the **monsoon** and natural fertility.\n\n"
         "**Institutional reforms after Independence:** **collectivisation, consolidation of holdings, co-operation and abolition of zamindari** were given priority in the **First Five Year Plan**. Land reform was the main focus.\n\n"
         "**Technological reforms:** the **Green Revolution**, based on the use of package technology (HYV seeds, fertilisers, irrigation), and the **White Revolution (Operation Flood)** for milk, were introduced in the 1960s and 1970s. But this led to the concentration of development in a few selected areas.\n\n"
         "**Comprehensive land development programme** in the 1980s and 1990s included both institutional and technical reforms:\n"
         "- provision of **crop insurance** against drought, flood, cyclone, fire and disease;\n- establishment of **Grameen banks, co-operative societies and banks** for loans at lower rates of interest;\n"
         "- **Kisan Credit Card (KCC)** and **Personal Accident Insurance Scheme (PAIS)**;\n- special **weather bulletins and agricultural programmes** for farmers on radio and television;\n"
         "- the government announces **minimum support price (MSP)**, remunerative and procurement prices for important crops to check exploitation of farmers by speculators and middlemen.\n\n"
         "**Bhoodan-Gramdan:** **Vinoba Bhave**, a disciple of Gandhiji, walked across India. At Pochampalli (Andhra Pradesh, now Telangana), landless villagers asked for land, and a landowner offered 80 acres. This began the **Bhoodan** (gift of land) movement; some zamindars offered whole villages, called **Gramdan**. It is also known as the **'blood-less revolution'**."),
  C.kc("s6.check", "Which is a technological reform that increased milk production?",
    [("White Revolution (Operation Flood)", ""), ("Green Revolution", "The Green Revolution was about food grains."), ("Bhoodan", "Bhoodan was about gifting land."), ("Abolition of zamindari", "That was an institutional reform.")],
    "The White Revolution boosted milk production."),
 ]},
 {"id": "s7", "title": "Remember, avoid, practise", "blocks": [
  blk("s7.memory", "memory_trick", title="Memory tricks",
    body="- **Seasons: \"Rabi = Rest in winter, reap in summer\" (Oct–Dec → Apr–Jun); \"Kharif = Comes with the monsoon\"; \"Zaid = Zippy summer fruits\" (melons, cucumber).**\n"
         "- **Largest producers: \"Jowar–Maharashtra, Bajra–Rajasthan, Ragi–Karnataka\" (J-M, B-R, R-K).**\n- **Second after: rice after China; sugarcane after Brazil.**\n"
         "- **Rainfall ladder: wheat 50-75 cm < sugarcane 75-100 cm < rice 100+ cm < rubber 200+ cm.**\n- **Paddy trio in the east: \"Aus, Aman, Boro\".**\n- **Pulses fix nitrogen, except arhar.**"),
  blk("s7.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Calling wheat a kharif crop: it is **rabi**.\n2. Saying all pulses fix nitrogen: **arhar is the exception**.\n3. Saying India is the largest producer of rice: it is **second after China** (and second in sugarcane after Brazil).\n"
         "4. Mixing up jowar (Maharashtra), bajra (Rajasthan) and ragi (Karnataka).\n5. Saying coffee in India is Robusta from Brazil: the chapter's variety is **Arabica from Yemen**, first grown on the **Baba Budan Hills**.\n"
         "6. Saying cotton needs heavy rain: it needs **light rainfall or irrigation**, high temperature and **210 frost-free days**."),
  blk("s7.tip", "teacher_tip", title="Try this in class",
    body="Give each group a calendar and crop cards. Students place each crop in its sowing and harvesting months, then colour the rabi, kharif and zaid seasons. "
         "Next, on an outline map, mark the largest producer states of jowar, bajra, ragi, sugarcane, tea, coffee, rubber and jute."),
  blk("s7.reflection", "reflection", title="Think and explain",
    body="A farmer with two acres keeps dividing land among children. Explain how this affects farming, and suggest one institutional reform that could help."),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 1:** soils decide which crops grow where (black soil and cotton, alluvial soil and wheat and rice).\n- **Chapter 3:** irrigation and multipurpose projects.\n"
         "- **Chapter 6 (Manufacturing):** agro-based industries like cotton textiles, jute and sugar.\n- **Economics, Sectors of the Economy:** agriculture as the primary sector and disguised unemployment."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="Explain why rice is a commercial crop in Punjab and Haryana but a subsistence crop in Odisha (2025-26 sample paper idea), in about 100 words.\n\n"
         "**Model answer:** Climate and irrigation: Punjab and Haryana have well-developed canal and tubewell irrigation, which allows large-scale rice cultivation even with less rain, and HYV seeds suit the area. Odisha's rice is mostly rain-fed, grown in a monsoonal climate without large irrigation systems. "
         "Economic factors: Punjab and Haryana have government procurement, good transport and access to national markets, so farmers grow rice for sale; in Odisha, rice is grown mainly for family and local use. "
         "Farming practices: Punjab and Haryana use machinery, fertilisers and modern techniques, while Odisha's farming is more traditional."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- Types of farming: primitive subsistence (slash and burn, jhumming), intensive subsistence, commercial and plantation.\n"
         "- Cropping seasons: rabi (wheat, mustard), kharif (rice, cotton, jute) and zaid (melons, vegetables).\n"
         "- Rice needs heat, humidity and 100+ cm rain; wheat needs a cool season and 50-75 cm rain; millets are nutritious coarse grains; India is the largest producer and consumer of pulses.\n"
         "- Sugarcane, oilseeds, tea, coffee and horticulture crops; rubber, cotton and jute are important non-food crops.\n"
         "- Reforms: land reforms, Green and White Revolutions, crop insurance, Grameen banks, KCC, MSP and the Bhoodan-Gramdan movement."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- The 2025-26 sample paper asked why rice is commercial in Haryana and Punjab but subsistence in Odisha (2 marks: at least one climate point and one economic point).\n"
         "- 3/5-mark favourites: types of farming, cropping seasons, conditions for rice, wheat, tea, sugarcane, cotton and jute, and reforms.\n"
         "- **Map work:** major rice and wheat areas, and the largest or major producer states of sugarcane, tea, coffee, rubber, cotton and jute."),
  blk("s7.flash1", "flashcard", front="Name the three cropping seasons and one crop each.", back="Rabi: wheat. Kharif: rice. Zaid: watermelon."),
  blk("s7.flash2", "flashcard", front="What conditions does tea need?", back="Warm, moist, frost-free climate; frequent, evenly distributed showers; deep, fertile, well-drained soil rich in humus; cheap skilled labour."),
  blk("s7.flash3", "flashcard", front="Why are pulses grown in rotation?", back="Being leguminous (except arhar), they fix nitrogen from the air and restore soil fertility."),
  blk("s7.flash4", "flashcard", front="What is the Bhoodan-Gramdan movement?", back="Vinoba Bhave's movement in which landowners gifted land (Bhoodan) or whole villages (Gramdan) to the landless: a 'blood-less revolution'."),
 ]},
]

# ---------------- Sample paper ----------------
W("sqp16", "very_short_answer", TYPES, "Rice is grown as a commercial crop in Haryana and Punjab, but as a subsistence crop in Odisha. Using your understanding of geographical factors and economic practices, explain why rice cultivation differs in these regions.",
  ["Climate and irrigation: Haryana and Punjab have well-developed canal and tubewell irrigation, so high-yielding rice can be grown on a large scale; Odisha's rice is mostly rain-fed under a monsoonal climate, with fewer large irrigation systems.",
   "Economic factors: in Punjab and Haryana, government procurement, transport networks and market access let farmers sell surplus rice; in Odisha, rice is grown mostly for family and local use, with traditional farming methods."],
  ["One point on climate/irrigation: 1 mark", "One point on economic factors or farming practices: 1 mark"], source=SQP(16))

# ---------------- NCERT exercises ----------------
M("ex1i", TYPES, "Which one of the following describes a system of agriculture where a single crop is grown on a large area?",
  [("Shifting Agriculture", "Shifting agriculture is small-scale slash and burn."), ("Plantation Agriculture", ""), ("Horticulture", "Horticulture is fruits and vegetables."), ("Intensive Agriculture", "Intensive farming uses small holdings with high inputs.")],
  "Plantation agriculture grows a single crop on a large area.", "easy", ex("1(i)"), correct=1)
M("ex1ii", SEAS, "Which one of the following is a rabi crop?",
  [("Rice", "Rice is a kharif crop."), ("Gram", ""), ("Millets", "Millets are mostly kharif."), ("Cotton", "Cotton is a kharif crop.")],
  "Gram is sown in winter and harvested in summer.", "easy", ex("1(ii)"), correct=1)
M("ex1iii", FOOD, "Which one of the following is a leguminous crop?",
  [("Pulses", ""), ("Jowar", "Jowar is a millet."), ("Millets", "Millets are not leguminous."), ("Sesamum", "Sesamum is an oilseed.")],
  "Pulses (except arhar) fix nitrogen from the air.", "easy", ex("1(iii)"), correct=0)
W("ex2i", "short_answer", NONFOOD, "Name one important beverage crop and specify the geographical conditions required for its growth.",
  ["Tea is an important beverage crop.", "It needs a tropical or subtropical climate: warm, moist and frost-free throughout the year, with frequent showers evenly distributed.",
   "It needs deep, fertile, well-drained soil rich in humus and organic matter, and abundant cheap skilled labour."], source=ex("2(i)"))
W("ex2ii", "short_answer", FOOD, "Name one staple crop of India and the regions where it is produced.",
  ["Rice is the staple food crop of a majority of Indians.", "It is grown in the plains of north and north-east India, coastal areas and deltaic regions (West Bengal, Uttar Pradesh, Assam, Odisha, Andhra Pradesh, Tamil Nadu, Kerala).",
   "With canal and tubewell irrigation, it is also grown in less rainy Punjab, Haryana, western Uttar Pradesh and parts of Rajasthan."], source=ex("2(ii)"))
W("ex2iii", "short_answer", REF, "Enlist the various institutional reform programmes introduced by the government in the interest of farmers.",
  ["Land reforms: collectivisation, consolidation of holdings, co-operation and abolition of zamindari.",
   "Crop insurance against drought, flood, cyclone, fire and disease; Grameen banks, co-operative societies and banks for cheap loans; Kisan Credit Card and Personal Accident Insurance Scheme.",
   "Weather bulletins and agricultural programmes on radio and TV, and minimum support prices to protect farmers from middlemen."], source=ex("2(iii)"))
W("ex3i", "long_answer", REF, "Suggest the initiative taken by the government to ensure the increase in agricultural production.",
  ["Land reforms after Independence: consolidation of holdings, co-operation and abolition of zamindari.",
   "The Green Revolution introduced HYV seeds, fertilisers and irrigation; the White Revolution (Operation Flood) raised milk production.",
   "Crop insurance and cheap credit through Grameen banks, co-operatives, Kisan Credit Cards and PAIS.",
   "Weather bulletins and farm programmes on radio and television spread knowledge.",
   "Minimum support prices and procurement give farmers fair returns and protect them from speculators and middlemen."], source=ex("3(i)"))
W("ex3ii", "long_answer", FOOD, "Describe the geographical conditions required for the growth of rice.",
  ["Rice is a kharif crop requiring high temperature, above 25°C.", "It needs high humidity and annual rainfall above 100 cm.",
   "In areas of less rainfall, it is grown with irrigation (Punjab, Haryana, western UP, parts of Rajasthan).",
   "It grows in the plains of north and north-east India, coastal areas and deltaic regions, mostly on alluvial soil.",
   "In Assam, West Bengal and Odisha, three crops (Aus, Aman, Boro) are grown in a year."], source=ex("3(ii)"))

# ---------------- MCQs ----------------
M("mcq01", TYPES, "Primitive subsistence farming depends mainly on:",
  [("the monsoon and natural fertility of the soil", ""), ("HYV seeds and fertilisers", "That is commercial farming."), ("migrant labour and capital", "That is plantation farming."), ("canal irrigation", "It depends on rain.")], "It uses primitive tools and family labour.")
M("mcq02", TYPES, "In slash-and-burn farming, when soil fertility falls, the farmer:",
  [("shifts and clears a fresh patch of land", ""), ("adds chemical fertilisers", "Fertilisers are not used."), ("builds terraces", "Terracing is a conservation method."), ("starts a plantation", "Plantations are commercial.")], "Nature replenishes the old patch.")
M("mcq03", TYPES, "Slash-and-burn farming is called 'Podu' or 'Penda' in:",
  [("Andhra Pradesh", ""), ("Madhya Pradesh", "There it is Bewar or Dahiya."), ("Jharkhand", "There it is Kuruwa."), ("the Western Ghats", "There it is Kumari.")], "Each region has its own name.")
M("mcq04", TYPES, "Which local name of slash-and-burn farming is used in Jharkhand?",
  [("Kuruwa", ""), ("Khil", "Khil is in the Himalayan belt."), ("Valre", "Valre is in south-eastern Rajasthan."), ("Koman", "Koman is in Odisha.")], "Kuruwa.")
M("mcq05", TYPES, "Intensive subsistence farming is practised in areas of:",
  [("high population pressure on land", ""), ("very low population", "It needs much labour on small plots."), ("large plantations", "Plantations are commercial."), ("deserts only", "It needs irrigation and inputs.")], "Farmers take maximum output from limited land.")
M("mcq06", TYPES, "Why do land holdings become uneconomical in intensive subsistence farming?",
  [("The right of inheritance divides land among successive generations", ""), ("Land is sold to companies", "The chapter names inheritance."), ("Plantations take over", "Not the reason given."), ("Floods wash land away", "Not the reason given.")], "Holdings keep getting smaller.")
M("mcq07", TYPES, "Which is NOT a feature of plantation farming?",
  [("Use of family labour on small patches", ""), ("A single crop on a large area", "This is a feature."), ("Capital-intensive inputs", "This is a feature."), ("Produce used as industrial raw material", "This is a feature.")], "Plantations use migrant labour on large areas.")
M("mcq08", TYPES, "Coffee plantations are important in:",
  [("Karnataka", ""), ("Punjab", "Punjab is known for wheat and rice."), ("Rajasthan", "Rajasthan is dry."), ("Bihar", "Bihar is not a coffee state.")], "Tea in Assam and North Bengal, coffee in Karnataka.")
M("mcq09", SEAS, "Rabi crops are sown in:",
  [("October to December", ""), ("June to July", "That is kharif sowing."), ("March to May", "That is zaid."), ("September only", "Rabi sowing is October to December.")], "They are harvested April to June.")
M("mcq10", SEAS, "Winter rain that helps rabi crops comes from:",
  [("western temperate cyclones", ""), ("the south-west monsoon", "That helps kharif crops."), ("tropical cyclones of the Bay of Bengal", "The chapter names western temperate cyclones."), ("sea breezes", "Not the source.")], "Western disturbances bring winter rain to the north-west.")
M("mcq11", SEAS, "Which is a kharif crop?",
  [("Soyabean", ""), ("Barley", "Barley is rabi."), ("Mustard", "Mustard is rabi."), ("Peas", "Peas are rabi.")], "Kharif crops grow with the monsoon.")
M("mcq12", SEAS, "Watermelon, muskmelon and cucumber are grown in the:",
  [("zaid season", ""), ("rabi season", "Rabi crops are winter crops."), ("kharif season", "Kharif crops are monsoon crops."), ("all seasons equally", "They are zaid crops.")], "Zaid is the short summer season.")
M("mcq13", SEAS, "Which crop takes almost a year to grow?",
  [("Sugarcane", ""), ("Wheat", "Wheat grows in one season."), ("Moong", "Moong is a short kharif crop."), ("Watermelon", "Watermelon is a short zaid crop.")], "Sugarcane needs almost a year.")
M("mcq14", FOOD, "India is the second largest producer of rice after:",
  [("China", ""), ("Brazil", "India is second to Brazil in sugarcane."), ("USA", "Not in rice."), ("Bangladesh", "India produces more rice than Bangladesh.")], "Rice is India's staple food.")
M("mcq15", FOOD, "Rice requires annual rainfall of:",
  [("above 100 cm", ""), ("50-75 cm", "That is for wheat."), ("75-100 cm", "That is for sugarcane."), ("more than 200 cm", "That is for rubber.")], "In less rainy areas rice needs irrigation.")
M("mcq16", FOOD, "The two important wheat-growing zones are:",
  [("the Ganga-Satluj plains and the black soil region of the Deccan", ""), ("the Konkan coast and Kerala", "These are rice areas."), ("Assam and West Bengal", "These grow rice and tea."), ("the Thar desert and Kutch", "These are too dry.")], "Wheat is the main crop of the north and north-west.")
M("mcq17", FOOD, "Wheat needs at the time of ripening:",
  [("bright sunshine", ""), ("heavy rainfall", "Heavy rain harms ripening."), ("frost", "Frost harms crops."), ("floods", "Floods destroy crops.")], "It needs a cool growing season and bright sunshine at ripening.")
M("mcq18", FOOD, "Which is the third most important food crop with respect to area and production?",
  [("Jowar", ""), ("Bajra", "Bajra is not named third."), ("Ragi", "Ragi is not named third."), ("Maize", "The chapter names jowar.")], "Jowar is mostly rain-fed.")
M("mcq19", FOOD, "The largest producer of ragi is:",
  [("Karnataka", ""), ("Rajasthan", "Rajasthan leads in bajra."), ("Maharashtra", "Maharashtra leads in jowar."), ("Punjab", "Punjab is known for wheat.")], "Tamil Nadu is second.")
M("mcq20", FOOD, "Maize is grown in the rabi season too in:",
  [("Bihar", ""), ("Kerala", "The chapter names Bihar."), ("Punjab", "The chapter names Bihar."), ("Rajasthan", "The chapter names Bihar.")], "Maize is mainly a kharif crop.")
M("mcq21", FOOD, "Maize grows well in:",
  [("old alluvial soil at 21°C to 27°C", ""), ("laterite soil at 10°C", "Not the conditions."), ("sandy desert soil without water", "Not suitable."), ("snow-covered areas", "Too cold.")], "It is used as food and fodder.")
M("mcq22", FOOD, "India's position in pulses is:",
  [("the largest producer and consumer in the world", ""), ("the largest exporter only", "India consumes most of its pulses."), ("second after China", "India is the largest."), ("a small producer", "India is the largest.")], "Pulses are the main protein source for vegetarians.")
M("mcq23", FOOD, "Which pulse does NOT fix nitrogen like other leguminous crops?",
  [("Arhar", ""), ("Gram", "Gram fixes nitrogen."), ("Moong", "Moong fixes nitrogen."), ("Urad", "Urad fixes nitrogen.")], "All except arhar restore soil fertility.")
M("mcq24", FOOD, "India is the second largest producer of sugarcane after:",
  [("Brazil", ""), ("China", "India is second to China in rice."), ("Cuba", "The chapter names Brazil."), ("USA", "The chapter names Brazil.")], "Sugarcane gives sugar, gur, khandsari and molasses.")
M("mcq25", FOOD, "Sugarcane requires annual rainfall of:",
  [("75-100 cm", ""), ("above 200 cm", "That is rubber."), ("50-75 cm", "That is wheat."), ("below 25 cm", "Too dry without irrigation.")], "It grows in hot, humid climate at 21°C to 27°C.")
M("mcq26", FOOD, "Groundnut is a:",
  [("kharif crop", ""), ("rabi crop", "Linseed and mustard are rabi."), ("zaid crop", "Zaid crops are melons and vegetables."), ("plantation crop", "It is a field crop.")], "It is about half of India's major oilseeds.")
M("mcq27", FOOD, "Sesamum is grown as:",
  [("kharif in the north and rabi in the south", ""), ("rabi everywhere", "It differs by region."), ("zaid only", "Not zaid."), ("a plantation crop", "It is a field crop.")], "Castor is grown in both seasons.")
M("mcq28", NONFOOD, "Tea was introduced in India initially by the:",
  [("British", ""), ("Portuguese", "The chapter names the British."), ("Dutch", "The chapter names the British."), ("Mughals", "The chapter names the British.")], "Today most tea gardens are owned by Indians.")
M("mcq29", NONFOOD, "Which is NOT required for tea?",
  [("Frost during winter", ""), ("Warm and moist climate", "This is required."), ("Fertile well-drained soil rich in humus", "This is required."), ("Frequent showers evenly distributed", "This is required.")], "Tea needs a frost-free climate all year.")
M("mcq30", NONFOOD, "The Arabica variety of coffee was first brought to India from:",
  [("Yemen", ""), ("Brazil", "The chapter names Yemen."), ("Ethiopia", "The chapter names Yemen."), ("Kenya", "The chapter names Yemen.")], "It was first grown on the Baba Budan Hills.")
M("mcq31", NONFOOD, "Coffee cultivation in India was first introduced on the:",
  [("Baba Budan Hills", ""), ("Garo hills", "Rubber grows in the Garo hills."), ("Darjeeling hills", "Darjeeling is famous for tea."), ("Aravalli hills", "Too dry.")], "Today it is confined to the Nilgiri in Karnataka, Kerala and Tamil Nadu.")
M("mcq32", NONFOOD, "Oranges are famous from:",
  [("Nagpur and Cherrapunji", ""), ("Jammu and Kashmir", "J&K is known for apples and walnuts."), ("Kerala and Mizoram", "These are famous for bananas."), ("Meghalaya only for pineapples", "Meghalaya has pineapples, but Nagpur leads in oranges.")], "Horticulture varies by region.")
M("mcq33", NONFOOD, "Rubber is mainly grown in:",
  [("Kerala, Tamil Nadu, Karnataka, Andaman and Nicobar, and the Garo hills", ""), ("Punjab and Haryana", "Too dry and cool."), ("Rajasthan and Gujarat", "Too dry."), ("Himachal Pradesh", "Too cold.")], "Rubber needs more than 200 cm rain and above 25°C.")
M("mcq34", NONFOOD, "Rearing silkworms for silk is called:",
  [("sericulture", ""), ("horticulture", "That is fruits and vegetables."), ("pisciculture", "That is fish farming."), ("viticulture", "That is grape growing.")], "Silkworms feed on mulberry leaves.")
M("mcq35", NONFOOD, "Cotton requires:",
  [("high temperature, light rainfall or irrigation, 210 frost-free days and bright sunshine", ""), ("heavy rainfall above 200 cm", "That is rubber."), ("cool climate with frost", "Cotton needs frost-free days."), ("floodplain soil renewed every year", "That is jute.")], "It grows well in black soil of the Deccan.")
M("mcq36", NONFOOD, "Jute grows best in:",
  [("fertile floodplain soils renewed every year", ""), ("dry sandy soils", "That suits bajra."), ("laterite soils of hills", "That suits tea and cashew."), ("black soils of the Deccan", "That suits cotton.")], "West Bengal is the main producer.")
M("mcq37", REF, "Which was given priority in the First Five Year Plan?",
  [("Land reforms such as consolidation of holdings and abolition of zamindari", ""), ("Plantations by foreign companies", "Not a reform."), ("Shifting cultivation", "Not a reform."), ("Ban on irrigation", "Not a reform.")], "Collectivisation, consolidation, co-operation and abolition of zamindari.")
M("mcq38", REF, "Minimum support price is announced to:",
  [("protect farmers from exploitation by speculators and middlemen", ""), ("increase food prices for consumers", "It protects farmers."), ("stop farmers from selling", "It ensures fair sale."), ("reduce crop production", "It encourages production.")], "MSP gives fair returns to farmers.")
M("mcq39", REF, "The Bhoodan-Gramdan movement was started by:",
  [("Vinoba Bhave", ""), ("M. S. Swaminathan", "He led the Green Revolution."), ("Jawaharlal Nehru", "Not Bhoodan."), ("Sunderlal Bahuguna", "He led Chipko.")], "It is called a blood-less revolution.")
# ---------------- Map work ----------------
M("map1", MAP, "Map work: which state is the largest producer of sugarcane?",
  [("Uttar Pradesh", ""), ("Kerala", "Kerala leads in rubber."), ("Assam", "Assam leads in tea."), ("West Bengal", "West Bengal leads in jute.")], "Uttar Pradesh leads sugarcane production.", "medium")
M("map2", MAP, "Map work: the leading tea-producing state to mark is:",
  [("Assam", ""), ("Karnataka", "Karnataka leads in coffee."), ("Punjab", "Punjab is a wheat and rice state."), ("Rajasthan", "Rajasthan is too dry.")], "Assam, followed by the Darjeeling and Jalpaiguri hills of West Bengal.", "medium")
M("map3", MAP, "Map work: the leading coffee-producing state to mark is:",
  [("Karnataka", ""), ("Assam", "Assam leads in tea."), ("Uttar Pradesh", "UP leads in sugarcane."), ("Gujarat", "Gujarat is a cotton state.")], "Coffee grows in the Nilgiri in Karnataka, Kerala and Tamil Nadu.", "medium")
M("map4", MAP, "Map work: the leading rubber-producing state to mark is:",
  [("Kerala", ""), ("Bihar", "Bihar is not a rubber state."), ("Haryana", "Haryana is too dry."), ("Punjab", "Punjab is too dry.")], "Rubber needs heavy rain and high temperature.", "medium")
W("map5", "very_short_answer", MAP, "Map work: name (a) the leading jute-producing state and (b) two major cotton-producing states.",
  ["(a) West Bengal.", "(b) Any two: Maharashtra, Gujarat, Madhya Pradesh, Karnataka, Telangana, Andhra Pradesh."])
# ---------------- True / false ----------------
C.tf("tf1", SEAS, "Wheat is a kharif crop.", False, "Wheat is a rabi crop, sown in winter and harvested in summer.")
C.tf("tf2", FOOD, "Ragi is very rich in iron and calcium.", True, "Millets have very high nutritional value.")
C.tf("tf3", NONFOOD, "Jute is losing its market to synthetic fibres like nylon because of its high cost.", True, "Synthetic packing materials are cheaper.")
C.tf("tf4", TYPES, "Rice is a subsistence crop in Punjab and a commercial crop in Odisha.", False, "It is the other way round: commercial in Punjab and Haryana, subsistence in Odisha.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", TYPES, "Distinguish between primitive subsistence farming and commercial farming.",
  ["Primitive subsistence farming uses primitive tools, family labour and natural fertility on small patches, mainly to feed the family.", "Commercial farming uses HYV seeds, chemical fertilisers, insecticides and pesticides to produce for the market."])
W("vsa2", "very_short_answer", FOOD, "Why are millets called nutritious coarse grains? Give two examples.",
  ["They are coarse grains but have very high nutritional value; ragi is rich in iron, calcium, micronutrients and roughage.", "Examples: jowar, bajra and ragi."])
W("vsa3", "very_short_answer", NONFOOD, "State two conditions needed for rubber.",
  ["A moist and humid climate with rainfall of more than 200 cm.", "A temperature above 25°C."])
W("sa1", "short_answer", SEAS, "Describe the three cropping seasons of India.",
  ["Rabi: sown October-December, harvested April-June; wheat, barley, peas, gram, mustard; helped by winter rain from western temperate cyclones.",
   "Kharif: sown with the monsoon, harvested September-October; paddy, maize, jowar, bajra, tur, moong, urad, cotton, jute, groundnut, soyabean.",
   "Zaid: a short summer season between rabi and kharif; watermelon, muskmelon, cucumber, vegetables and fodder crops."])
W("sa2", "short_answer", NONFOOD, "Describe the conditions for growing cotton and name its major producing states.",
  ["Cotton grows well in the drier parts of the black cotton soil of the Deccan plateau.", "It needs high temperature, light rainfall or irrigation, 210 frost-free days and bright sunshine; it is a kharif crop taking 6-8 months.",
   "Major states: Maharashtra, Gujarat, Madhya Pradesh, Karnataka, Andhra Pradesh, Telangana, Tamil Nadu, Punjab, Haryana and Uttar Pradesh."])
W("sa3", "short_answer", FOOD, "Why are pulses important in Indian agriculture?",
  ["India is the largest producer and consumer of pulses; they are the main source of protein in a vegetarian diet.", "They need less moisture and survive even in dry conditions.",
   "Being leguminous (except arhar), they fix nitrogen from the air and restore soil fertility, so they are grown in rotation with other crops."])
W("la1", "long_answer", TYPES, "Describe the four types of farming in India.",
  ["Primitive subsistence farming: slash-and-burn on small patches with hoe, dao and digging sticks and family labour; depends on monsoon and soil fertility; called jhumming in the north-east.",
   "Intensive subsistence farming: in areas of high population, labour-intensive with high doses of biochemical inputs and irrigation; inheritance divides land into small holdings.",
   "Commercial farming: uses HYV seeds, chemical fertilisers, insecticides and pesticides; commercialisation varies, e.g. rice is commercial in Punjab and Haryana but subsistence in Odisha.",
   "Plantation farming: a single crop on a large area, capital-intensive with migrant labour; produce used by industries.",
   "Examples of plantation crops: tea in Assam and North Bengal, coffee in Karnataka, rubber, sugarcane and banana; it needs good transport linking plantations, industries and markets."])
W("cb1", "case_based", NONFOOD, "Read the source and answer the questions.\n\n*\"Tea cultivation is an example of plantation agriculture. It is also an important beverage crop introduced in India initially by the British. Today, most of the tea plantations are owned by Indians. The tea plant grows well in tropical and subtropical climates endowed with deep and fertile well-drained soil, rich in humus and organic matter.\"* (NCERT)\n\n"
  "(i) Who first introduced tea in India? (1)\n\n(ii) What kind of soil suits tea? (1)\n\n(iii) Why is tea processed within the garden, and what labour does it need? (2)",
  ["(i) The British.", "(ii) Deep, fertile, well-drained soil rich in humus and organic matter.",
   "(iii) Tea leaves are processed within the garden to restore their freshness; tea is labour-intensive and needs abundant, cheap and skilled labour."])
W("cb2", "case_based", FOOD, "Read the source and answer the questions.\n\n*\"Rice is the staple food crop of a majority of the people in India. Our country is the second largest producer of rice in the world after China. It is a kharif crop which requires high temperature (above 25°C) and high humidity with annual rainfall above 100 cm.\"* (NCERT)\n\n"
  "(i) Which country produces more rice than India? (1)\n\n(ii) In which season is rice grown? (1)\n\n(iii) How is rice grown in areas of less rainfall such as Punjab and Haryana? (2)",
  ["(i) China.", "(ii) Kharif.",
   "(iii) A dense network of canal irrigation and tubewells supplies the water needed, so rice is grown in Punjab, Haryana, western Uttar Pradesh and parts of Rajasthan."])
# ---------------- Assertion-reason ----------------
C.arq("ar1", TYPES, "Primitive subsistence farming has low land productivity.", "Farmers do not use fertilisers or other modern inputs.", 0,
      "R explains A.", "yields are low.", "only natural fertility is used.")
C.arq("ar2", SEAS, "Western temperate cyclones help rabi crops.", "They bring winter rain to the north and north-west.", 0,
      "R explains A.", "rabi crops grow in winter.", "winter rain helps wheat.")
C.arq("ar3", FOOD, "Pulses are grown in rotation with other crops.", "Most pulses fix nitrogen from the air and restore soil fertility.", 0,
      "R explains A.", "rotation keeps soil fertile.", "pulses are leguminous.")
C.arq("ar4", NONFOOD, "Jute is gaining markets over synthetic fibres.", "Jute is known as the golden fibre.", 3,
      "A is false: jute is losing markets to cheaper synthetic fibres like nylon. R is true.", "its high cost loses markets.", "it is called the golden fibre.")
C.arq("ar5", FOOD, "Rice is grown in Punjab and Haryana.", "These states have a dense network of canals and tubewells.", 0,
      "R explains A: irrigation makes rice possible in less rainy areas.", "rice is now important there.", "irrigation provides water.")
C.arq("ar6", NONFOOD, "Tea is processed within the tea garden.", "Tea needs a frost-free climate.", 1,
      "Both are true, but R is about climate; tea is processed in the garden to keep it fresh.", "this keeps leaves fresh.", "frost harms tea.")

chapter = header(SUBJ, N, "Agriculture", ["farming_types", "cropping_seasons", "food_crops", "non_food_crops", "agri_reforms", "crops_map"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: this chapter is fully in the board examination (Geography: 17 marks + 3 map marks). Map work from this chapter: major rice and wheat areas, and the largest or major producer states of sugarcane, tea, coffee, rubber, cotton and jute (given here as text questions).")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
