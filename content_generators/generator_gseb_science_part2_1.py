import json
import os

CURRICULUM_PATH = '/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/master_curriculum.json'

def ch6_blocks():
    return [
        {"type": "theory", "id": "c8s_ch6_b1", "data": {"title": "The Science of Fire 🔥", "content": "Have you ever stared at a campfire and wondered what fire actually is? It's not a solid, liquid, or gas—it is a chemical reaction! In this chapter, we explore Combustion and Flame."}},
        {"type": "media", "id": "c8s_ch6_b2", "data": {"mediaType": "image", "url": "assets/images/cyclones_ch6.jpg", "caption": "The destructive power of uncontrolled heat and energy."}},
        {"type": "theory", "id": "c8s_ch6_b3", "data": {"title": "What is Combustion?", "content": "A chemical process in which a substance reacts with oxygen to give off heat is called combustion. The substance that undergoes combustion is said to be combustible (or a fuel). The fuel may be solid, liquid, or gas."}},
        {"type": "teacher_tip", "id": "c8s_ch6_b4", "data": {"content": "Remember the Fire Triangle: To make a fire, you need three things: Fuel, Oxygen, and Heat (Ignition Temperature)."}},
        {"type": "theory", "id": "c8s_ch6_b5", "data": {"title": "Ignition Temperature", "content": "The lowest temperature at which a substance catches fire is called its ignition temperature. A matchstick does not catch fire on its own at room temperature because its ignition temperature is much higher."}},
        {"type": "flashcard", "id": "c8s_ch6_b6", "data": {"front": "What is the lowest temperature at which a substance catches fire called?", "back": "Ignition Temperature"}},
        {"type": "quiz", "id": "c8s_ch6_b7", "data": {"question": "Which of the following is essential for combustion to take place?", "options": ["Nitrogen", "Carbon Dioxide", "Oxygen", "Argon"], "correct_index": 2, "explanation": "Oxygen supports combustion. Without it, a fire will go out."}},
        {"type": "theory", "id": "c8s_ch6_b8", "data": {"title": "How Do We Control Fire?", "content": "To extinguish a fire, we must remove at least one of the requirements from the Fire Triangle (Fuel, Oxygen, Heat). Throwing water cools the combustible material so its temperature drops below its ignition temperature. A carbon dioxide (CO2) fire extinguisher cuts off the supply of oxygen."}},
        {"type": "theory", "id": "c8s_ch6_b9", "data": {"title": "Types of Combustion", "content": "1. Rapid Combustion: The gas burns rapidly and produces heat and light (e.g., LPG stove).\n2. Spontaneous Combustion: A material suddenly bursts into flames, without the application of any apparent cause (e.g., phosphorus burning at room temperature).\n3. Explosion: A sudden reaction with the evolution of heat, light, and sound, and the release of a large amount of gas (e.g., firecrackers)."}},
        {"type": "theory", "id": "c8s_ch6_b10", "data": {"title": "Flame Structure", "content": "A candle flame has three different zones:\n- Dark zone (innermost): Unburnt wax vapours, least hot.\n- Luminous zone (middle): Partial combustion, yellow flame, moderately hot.\n- Non-luminous zone (outermost): Complete combustion, blue flame, hottest part."}},
    ]

def ch7_blocks():
    return [
        {"type": "theory", "id": "c8s_ch7_b1", "data": {"title": "The Web of Life 🌳", "content": "Imagine a world without tigers, elephants, or ancient forests. As human populations grow, our wild spaces are shrinking rapidly. Let's learn how we can conserve plants and animals before they disappear forever."}},
        {"type": "media", "id": "c8s_ch7_b2", "data": {"mediaType": "image", "url": "assets/images/particulate_ch7.jpg", "caption": "The delicate balance of nature and the particles that affect it."}},
        {"type": "theory", "id": "c8s_ch7_b3", "data": {"title": "Deforestation and Its Causes", "content": "Deforestation means clearing of forests and using that land for other purposes, such as procuring land for cultivation, building houses and factories, or using wood as fuel. \n\nConsequences: Deforestation increases the temperature and pollution level on the earth. It increases the level of carbon dioxide in the atmosphere, leading to global warming."}},
        {"type": "theory", "id": "c8s_ch7_b4", "data": {"title": "Biosphere Reserves", "content": "To protect our flora and fauna and their habitats, protected areas called sanctuaries, national parks, and biosphere reserves have been earmarked. \n- **Sanctuary:** Areas where animals are protected from any disturbance to them and their habitat.\n- **National Park:** Reserves large and diverse enough to protect whole sets of ecosystems."}},
        {"type": "flashcard", "id": "c8s_ch7_b5", "data": {"front": "What do we call the clearing of forests and using the land for other purposes?", "back": "Deforestation"}},
        {"type": "quiz", "id": "c8s_ch7_b6", "data": {"question": "Which of the following leads to an increase in the earth's temperature (global warming)?", "options": ["Planting trees", "Increase in Oxygen", "Increase in Carbon Dioxide", "Rainfall"], "correct_index": 2, "explanation": "Plants absorb CO2. Deforestation reduces the number of trees, leading to an accumulation of CO2 in the atmosphere, which traps heat."}},
        {"type": "theory", "id": "c8s_ch7_b7", "data": {"title": "Flora and Fauna", "content": "The plants found in a particular area are termed flora of that area. The animals found in a particular area are termed fauna. Endemic species are those species of plants and animals which are found exclusively in a particular area. They are not naturally found anywhere else."}},
        {"type": "teacher_tip", "id": "c8s_ch7_b8", "data": {"content": "Remember: Flora sounds like 'Flower' (Plants). Fauna sounds like 'Fawn' (Animals, like a baby deer)."}},
        {"type": "theory", "id": "c8s_ch7_b9", "data": {"title": "Red Data Book", "content": "Red Data Book is the source book which keeps a record of all the endangered animals and plants. Endangered animals are those whose numbers are diminishing to a level that they might face extinction."}},
        {"type": "theory", "id": "c8s_ch7_b10", "data": {"title": "Migration", "content": "Migration is the phenomenon of movement of a species from its own habitat to some other habitat for a particular time period every year for a specific purpose like breeding or escaping harsh weather."}},
    ]

def ch8_blocks():
    return [
        {"type": "theory", "id": "c8s_ch8_b1", "data": {"title": "The Building Blocks of Life 🔬", "content": "Just as a house is made of bricks, every living organism on Earth is made of tiny building blocks called cells. Some organisms are made of just a single cell, while you are made of over 30 trillion cells!"}},
        {"type": "media", "id": "c8s_ch8_b2", "data": {"mediaType": "image", "url": "assets/images/elements_ch8.jpg", "caption": "The fundamental building blocks forming complex structures."}},
        {"type": "theory", "id": "c8s_ch8_b3", "data": {"title": "Discovery of the Cell", "content": "Robert Hooke in 1665 observed slices of cork under a simple magnifying device. He noticed partitioned boxes or compartments and coined the term 'cell' for each box."}},
        {"type": "theory", "id": "c8s_ch8_b4", "data": {"title": "Cell Number, Shape, and Size", "content": "Organisms made of more than one cell are called multicellular organisms. Organisms made of a single cell are called unicellular organisms (e.g., Amoeba, Paramecium).\nCells can be spherical, elongated, or branched (like the nerve cell, which receives and transfers messages)."}},
        {"type": "flashcard", "id": "c8s_ch8_b5", "data": {"front": "Who discovered the cell in 1665?", "back": "Robert Hooke"}},
        {"type": "quiz", "id": "c8s_ch8_b6", "data": {"question": "An organism made up of a single cell is called:", "options": ["Multicellular", "Unicellular", "Acellular", "Polycellular"], "correct_index": 1, "explanation": "Organisms like Amoeba and Paramecium consist of only a single cell and are called unicellular."}},
        {"type": "theory", "id": "c8s_ch8_b7", "data": {"title": "Parts of the Cell", "content": "1. **Cell Membrane:** Encloses the cell, gives it shape, and is porous to allow movement of substances.\n2. **Cytoplasm:** The jelly-like substance between the nucleus and the cell membrane.\n3. **Nucleus:** The control center of the cell. It contains thread-like structures called chromosomes, which carry genes for inheritance."}},
        {"type": "teacher_tip", "id": "c8s_ch8_b8", "data": {"content": "Plant cells have an extra, thick outer layer called the Cell Wall to protect against temperature variations, high wind speed, and atmospheric moisture."}},
        {"type": "theory", "id": "c8s_ch8_b9", "data": {"title": "Prokaryotic vs Eukaryotic Cells", "content": "Cells having nuclear material without a nuclear membrane are termed prokaryotic cells (e.g., bacteria). \nCells having a well-organized nucleus with a nuclear membrane are designated as eukaryotic cells (e.g., plant and animal cells)."}},
        {"type": "theory", "id": "c8s_ch8_b10", "data": {"title": "Plastids and Vacuoles", "content": "Plant cells contain colored bodies called plastids. Green plastids contain chlorophyll and are called chloroplasts. Animal cells have very small vacuoles, whereas plant cells usually have a single large central vacuole."}},
    ]

def ch9_blocks():
    return [
        {"type": "theory", "id": "c8s_ch9_b1", "data": {"title": "The Circle of Life 🐣", "content": "How do species survive generation after generation without going extinct? Through the biological process of reproduction! Let's explore how new animals are brought into the world."}},
        {"type": "media", "id": "c8s_ch9_b2", "data": {"mediaType": "image", "url": "assets/images/solutions_ch9.jpg", "caption": "Microscopic view of cellular interaction."}},
        {"type": "theory", "id": "c8s_ch9_b3", "data": {"title": "Modes of Reproduction", "content": "Just like plants, animals reproduce in two ways:\n1. **Sexual Reproduction:** Requires two parents (male and female) and the fusion of male and female gametes.\n2. **Asexual Reproduction:** Requires only a single parent. No fusion of gametes occurs."}},
        {"type": "theory", "id": "c8s_ch9_b4", "data": {"title": "Sexual Reproduction", "content": "The male reproductive organs include a pair of testes, two sperm ducts, and a penis. The testes produce the male gametes called sperms.\nThe female reproductive organs are a pair of ovaries, oviducts (fallopian tubes), and the uterus. The ovary produces female gametes called ova (eggs)."}},
        {"type": "teacher_tip", "id": "c8s_ch9_b5", "data": {"content": "A single sperm is a single cell, but it has a head, a middle piece, and a tail to help it swim!"}},
        {"type": "theory", "id": "c8s_ch9_b6", "data": {"title": "Fertilisation", "content": "The first step in the process of reproduction is the fusion of a sperm and an ovum. This fusion is called fertilisation. During fertilisation, the nuclei of the sperm and the egg fuse to form a single nucleus. This results in the formation of a fertilised egg or **zygote**."}},
        {"type": "flashcard", "id": "c8s_ch9_b7", "data": {"front": "What do we call the fertilised egg resulting from the fusion of a sperm and an ovum?", "back": "Zygote"}},
        {"type": "quiz", "id": "c8s_ch9_b8", "data": {"question": "Fertilisation that takes place inside the female body is called:", "options": ["External fertilisation", "Internal fertilisation", "In-vitro fertilisation", "Asexual fertilisation"], "correct_index": 1, "explanation": "Internal fertilisation occurs in many animals including humans, cows, and dogs."}},
        {"type": "theory", "id": "c8s_ch9_b9", "data": {"title": "Development of Embryo", "content": "The zygote divides repeatedly to give rise to a ball of cells. The cells then begin to form groups that develop into different tissues and organs of the body. This developing structure is termed an **embryo**. The stage of the embryo in which all the body parts can be identified is called a **foetus**."}},
        {"type": "theory", "id": "c8s_ch9_b10", "data": {"title": "Asexual Reproduction", "content": "In microscopic animals like hydra, new individuals develop from bulges called buds. This is called **budding**.\nIn Amoeba, the animal reproduces by dividing into two individuals. This type of asexual reproduction is called **binary fission**."}},
    ]

def ch10_blocks():
    return [
        {"type": "theory", "id": "c8s_ch10_b1", "data": {"title": "Growing Up: The Age of Adolescence 🧬", "content": "Growing up is a natural process. But suddenly, around the age of 10 or 11, the body begins to undergo massive, rapid changes. Let's explore the science behind adolescence and puberty."}},
        {"type": "media", "id": "c8s_ch10_b2", "data": {"mediaType": "image", "url": "assets/images/light_ch10.jpg", "caption": "The transition and growth from childhood to adulthood."}},
        {"type": "theory", "id": "c8s_ch10_b3", "data": {"title": "Adolescence and Puberty", "content": "The period of life, when the body undergoes changes, leading to reproductive maturity, is called adolescence. It begins around the age of 11 and lasts up to 18 or 19 years of age. \nThe human body undergoes several changes during adolescence. These changes mark the onset of puberty."}},
        {"type": "theory", "id": "c8s_ch10_b4", "data": {"title": "Changes at Puberty", "content": "1. Increase in Height.\n2. Change in Body Shape (broader shoulders in boys, wider region below the waist in girls).\n3. Voice Change (boys develop larger voice boxes called Adam's apple, resulting in a deep voice).\n4. Increased Activity of Sweat and Sebaceous (oil) Glands (often causing acne/pimples)."}},
        {"type": "teacher_tip", "id": "c8s_ch10_b5", "data": {"content": "Acne and pimples are completely normal during puberty! They are just the result of your oil glands working in overdrive due to hormones."}},
        {"type": "flashcard", "id": "c8s_ch10_b6", "data": {"front": "What is the protruding part of the throat in boys called?", "back": "Adam's Apple"}},
        {"type": "theory", "id": "c8s_ch10_b7", "data": {"title": "Hormones: The Chemical Messengers", "content": "The changes which occur at adolescence are controlled by hormones. Hormones are chemical substances secreted by endocrine glands.\n- Male hormone: **Testosterone** (causes growth of facial hair).\n- Female hormone: **Estrogen** (causes breasts to develop)."}},
        {"type": "quiz", "id": "c8s_ch10_b8", "data": {"question": "Which gland is known as the master gland because it controls the production of other hormones?", "options": ["Thyroid", "Adrenal", "Pituitary", "Pancreas"], "correct_index": 2, "explanation": "The pituitary gland secretes hormones that stimulate other endocrine glands to secrete their hormones."}},
        {"type": "theory", "id": "c8s_ch10_b9", "data": {"title": "Sex Determination of the Baby", "content": "Inside the fertilised egg or zygote is the instruction for determining the sex of the baby. This instruction is present in the thread-like structures called chromosomes. \nHuman cells have 23 pairs of chromosomes. One pair is the sex chromosomes (X and Y).\nA female has two X chromosomes (XX). A male has one X and one Y chromosome (XY)."}},
        {"type": "theory", "id": "c8s_ch10_b10", "data": {"title": "Nutritional Needs of the Adolescents", "content": "Adolescence is a stage of rapid growth and development. The diet for an adolescent has to be carefully planned. It should be a balanced diet containing proteins, carbohydrates, fats, and vitamins in requisite proportions. Iron builds blood, so iron-rich food (leafy vegetables, jaggery, meat) is vital."}},
    ]

def ch11_blocks():
    return [
        {"type": "theory", "id": "c8s_ch11_b1", "data": {"title": "The Invisible Push and Pull 🧲", "content": "Why does a ball rolling on the ground eventually stop? Why do you need to push a heavy box to make it move? Let's uncover the secrets of Force and Pressure!"}},
        {"type": "media", "id": "c8s_ch11_b2", "data": {"mediaType": "image", "url": "assets/images/time_ch11.jpg", "caption": "Visualizing abstract concepts in physical science."}},
        {"type": "theory", "id": "c8s_ch11_b3", "data": {"title": "What is Force?", "content": "A push or a pull on an object is called a force. Forces are due to an interaction between at least two objects. The strength of a force is usually expressed by its magnitude. Force also has a direction in which it acts."}},
        {"type": "theory", "id": "c8s_ch11_b4", "data": {"title": "Effects of Force", "content": "A force can:\n1. Make an object move from rest.\n2. Change the speed of a moving object.\n3. Change the direction of motion of an object.\n4. Change the shape of an object (like squeezing a sponge)."}},
        {"type": "teacher_tip", "id": "c8s_ch11_b5", "data": {"content": "If two equal forces act on an object in opposite directions, the net force is zero and the object will not move!"}},
        {"type": "flashcard", "id": "c8s_ch11_b6", "data": {"front": "A push or pull on an object is called:", "back": "Force"}},
        {"type": "theory", "id": "c8s_ch11_b7", "data": {"title": "Contact vs Non-Contact Forces", "content": "**Contact Forces:** The force that can be applied only when it is in contact with an object (e.g., Muscular force, Friction).\n**Non-Contact Forces:** The force exerted by an object on another without touching it (e.g., Magnetic force, Electrostatic force, Gravitational force)."}},
        {"type": "quiz", "id": "c8s_ch11_b8", "data": {"question": "Which of the following is a non-contact force?", "options": ["Friction", "Muscular Force", "Gravitational Force", "Air Resistance"], "correct_index": 2, "explanation": "Gravitational force pulls objects toward the earth even when they are not in physical contact with it."}},
        {"type": "theory", "id": "c8s_ch11_b9", "data": {"title": "Pressure", "content": "The force acting on a unit area of a surface is called pressure.\nPressure = Force / Area on which it acts.\nThis is why a sharp knife cuts easily: the area of the edge is very small, so the pressure exerted is very large!"}},
        {"type": "theory", "id": "c8s_ch11_b10", "data": {"title": "Atmospheric Pressure", "content": "There is air all around us. The envelope of air is known as the atmosphere. The pressure exerted by this air is known as atmospheric pressure. Our body is not crushed by this massive pressure because the pressure of the blood inside our body is equal to the atmospheric pressure."}},
    ]

def ch12_blocks():
    return [
        {"type": "theory", "id": "c8s_ch12_b1", "data": {"title": "The Force that Slows Us Down 🛑", "content": "Have you ever slipped on a banana peel? Or wondered why your bicycle brakes work? The answer to both is a silent, invisible force called Friction!"}},
        {"type": "media", "id": "c8s_ch12_b2", "data": {"mediaType": "image", "url": "assets/images/harmony_ch12.jpg", "caption": "The balance of forces in physical systems."}},
        {"type": "theory", "id": "c8s_ch12_b3", "data": {"title": "What is Friction?", "content": "Friction is a force that opposes the relative motion between two surfaces in contact. It always acts in the direction opposite to the applied force."}},
        {"type": "theory", "id": "c8s_ch12_b4", "data": {"title": "Cause of Friction", "content": "Friction is caused by the irregularities on the two surfaces in contact. Even surfaces that appear very smooth have a large number of minute irregularities on them. These irregularities interlock with one another, causing resistance to motion."}},
        {"type": "flashcard", "id": "c8s_ch12_b5", "data": {"front": "What force opposes the relative motion between two surfaces in contact?", "back": "Friction"}},
        {"type": "quiz", "id": "c8s_ch12_b6", "data": {"question": "Which type of friction is the highest?", "options": ["Rolling friction", "Sliding friction", "Static friction", "Fluid friction"], "correct_index": 2, "explanation": "Static friction comes into play to get an object at rest to move. It is higher than sliding and rolling friction."}},
        {"type": "theory", "id": "c8s_ch12_b7", "data": {"title": "Friction: A Necessary Evil", "content": "**Why it is necessary:** You could not walk, write with a pen, or stop a car without friction. Nails and screws hold things together due to friction.\n**Why it is an evil:** It wears out materials (like shoe soles and car tyres). It also produces heat, which causes energy loss in machines."}},
        {"type": "theory", "id": "c8s_ch12_b8", "data": {"title": "Increasing and Reducing Friction", "content": "**Increasing:** Tyres are treaded (grooved) and athletes wear spiked shoes to increase friction and get a better grip.\n**Reducing:** Lubricants (oil, grease, graphite) are applied between moving parts of machines to reduce friction. Ball bearings convert sliding friction into rolling friction, which is much smaller."}},
        {"type": "theory", "id": "c8s_ch12_b9", "data": {"title": "Fluid Friction (Drag)", "content": "Gases and liquids exert force of friction on objects in motion through them. This is called fluid friction or drag. \nTo minimize fluid friction, objects like airplanes, boats, and birds are given special streamlined shapes that easily cut through the fluid."}},
    ]

def update_curriculum():
    print("Loading master curriculum...")
    with open(CURRICULUM_PATH, 'r') as f:
        data = json.load(f)

    data["gseb_class8_science_ch6"] = ch6_blocks()
    data["gseb_class8_science_ch7"] = ch7_blocks()
    data["gseb_class8_science_ch8"] = ch8_blocks()
    data["gseb_class8_science_ch9"] = ch9_blocks()
    data["gseb_class8_science_ch10"] = ch10_blocks()
    data["gseb_class8_science_ch11"] = ch11_blocks()
    data["gseb_class8_science_ch12"] = ch12_blocks()

    print("Saving updated curriculum (Part 1/2)...")
    with open(CURRICULUM_PATH, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    update_curriculum()
