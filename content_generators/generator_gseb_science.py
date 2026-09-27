import json
import os

CURRICULUM_PATH = '/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/master_curriculum.json'

def generate_blocks_ch2():
    return [
        {
            "type": "theory",
            "id": "c8s_ch2_b1_hook",
            "data": {
                "title": "The Invisible World Around Us 🦠",
                "content": "Have you ever wondered why milk turns into curd, or why bread gets moldy if left out? The answer lies in a hidden world of living organisms so tiny, you cannot see them with your naked eye. Today, we dive into the world of microorganisms—some are our best friends, while others are deadly foes!"
            }
        },
        {
            "type": "media",
            "id": "c8s_ch2_b2_media",
            "data": {
                "mediaType": "image",
                "url": "assets/images/invisible_world_ch2.jpg",
                "caption": "A microscopic view of various microorganisms."
            }
        },
        {
            "type": "theory",
            "id": "c8s_ch2_b3_types",
            "data": {
                "title": "What are Microorganisms?",
                "content": "Microorganisms (or microbes) are classified into four major groups:\n\n1. **Bacteria:** Single-celled organisms. Some cause diseases like typhoid and tuberculosis (TB).\n2. **Fungi:** Includes yeast and molds.\n3. **Protozoa:** Includes amoeba and paramecium. Causes diseases like dysentery and malaria.\n4. **Algae:** Plant-like microbes that can perform photosynthesis (e.g., Spirogyra).\n\n*Note: Viruses are also microscopic but are considered different because they only reproduce inside the cells of a host organism.*"
            }
        },
        {
            "type": "dictionary_link",
            "id": "c8s_ch2_b4_dict",
            "data": {
                "term_id": "virus",
                "preview": "Virus: A microscopic infectious agent that can only replicate inside the living cells of an organism."
            }
        },
        {
            "type": "theory",
            "id": "c8s_ch2_b5_friends",
            "data": {
                "title": "Microorganisms as Friends 🤝",
                "content": "Not all microbes are bad! They play a crucial role in our lives:\n\n- **Food Production:** *Lactobacillus* bacterium promotes the formation of curd from milk. Yeast is used in baking bread, cakes, and pastries because it produces carbon dioxide gas during respiration.\n- **Commercial Use:** Yeast is used for the large-scale production of alcohol and wine through a process called *fermentation*.\n- **Medicinal Use:** Antibiotics (like Penicillin) are medicines produced from bacteria and fungi that kill or stop the growth of disease-causing microorganisms.\n- **Cleaning the Environment:** Bacteria decompose organic waste (like dead plants and animals) into harmless and usable substances."
            }
        },
        {
            "type": "teacher_tip",
            "id": "c8s_ch2_b6_tip",
            "data": {
                "content": "Fermentation was discovered by Louis Pasteur in 1857. Without it, we wouldn't have fluffy bread or vinegar!"
            }
        },
        {
            "type": "theory",
            "id": "c8s_ch2_b7_vaccine",
            "data": {
                "title": "Vaccines: The Ultimate Shield 🛡️",
                "content": "When a disease-carrying microbe enters our body, the body produces **antibodies** to fight the invader. \n\nA **vaccine** contains dead or weakened microbes. When introduced into a healthy body, the body fights and kills the invading bacteria by producing suitable antibodies. The body remembers how to fight the microbe if it enters again!"
            }
        },
        {
            "type": "theory",
            "id": "c8s_ch2_b8_foes",
            "data": {
                "title": "Microorganisms as Foes ☠️",
                "content": "Disease-causing microorganisms are called **pathogens**.\n\nCommunicable diseases can spread from an infected person to a healthy person through air, water, food, or physical contact (e.g., cholera, common cold, chickenpox, tuberculosis).\n\nInsects and animals that carry disease-causing microbes are called **carriers**. For example, the female *Anopheles* mosquito carries the parasite of malaria, and the female *Aedes* mosquito acts as a carrier of the dengue virus."
            }
        },
        {
            "type": "flashcard",
            "id": "c8s_ch2_b9_fc1",
            "data": {
                "front": "What bacterium is responsible for turning milk into curd?",
                "back": "Lactobacillus"
            }
        },
        {
            "type": "flashcard",
            "id": "c8s_ch2_b10_fc2",
            "data": {
                "front": "What do we call the process of conversion of sugar into alcohol?",
                "back": "Fermentation"
            }
        },
        {
            "type": "quiz",
            "id": "c8s_ch2_b11_quiz1",
            "data": {
                "question": "Which of the following is a carrier of the dengue virus?",
                "options": ["Housefly", "Female Anopheles mosquito", "Female Aedes mosquito", "Cockroach"],
                "correct_index": 2,
                "explanation": "The female Aedes mosquito acts as a carrier of the dengue virus, while the female Anopheles mosquito carries the malaria parasite."
            }
        },
        {
            "type": "theory",
            "id": "c8s_ch2_b12_preservation",
            "data": {
                "title": "Food Preservation 🥫",
                "content": "To prevent microbes from spoiling our food, we use various methods:\n\n1. **Chemical Method:** Adding salt and edible oils (like in pickles) or using preservatives like sodium benzoate.\n2. **Preservation by Sugar:** Sugar reduces moisture content, inhibiting the growth of bacteria (used in jams and jellies).\n3. **Heat and Cold Treatments:** Boiling kills many microbes. Storing food in the refrigerator stops them from growing.\n4. **Pasteurisation:** Milk is heated to about 70°C for 15-30 seconds and then suddenly chilled and stored. This prevents the growth of microbes."
            }
        },
        {
            "type": "theory",
            "id": "c8s_ch2_b13_nitrogen",
            "data": {
                "title": "Nitrogen Fixation 🌱",
                "content": "Our atmosphere has 78% nitrogen gas, but plants and animals cannot take atmospheric nitrogen directly. \n\nCertain bacteria (like *Rhizobium*, which lives in the root nodules of leguminous plants) and blue-green algae can fix nitrogen from the atmosphere to enrich soil with nitrogen and increase its fertility. This continuous cycle of nitrogen moving from the atmosphere to the soil and back is called the **Nitrogen Cycle**."
            }
        },
        {
            "type": "quiz",
            "id": "c8s_ch2_b14_quiz2",
            "data": {
                "question": "The process of pasteurisation involves heating milk to what temperature?",
                "options": ["100°C for 5 minutes", "70°C for 15-30 seconds", "50°C for 1 hour", "30°C for 10 seconds"],
                "correct_index": 1,
                "explanation": "Pasteurisation involves heating milk to about 70°C for 15 to 30 seconds and then suddenly chilling it."
            }
        }
    ]

def generate_blocks_ch3():
    return [
        {
            "type": "theory",
            "id": "c8s_ch3_b1_hook",
            "data": {
                "title": "The Magic of Man-Made Materials 🧵",
                "content": "Look at the clothes you are wearing, the chair you are sitting on, or the water bottle on your desk. Chances are, they are not made from cotton or wood. They are made from synthetic fibres and plastics! Today we will uncover how scientists turn simple chemicals into durable fabrics and versatile plastics that power the modern world."
            }
        },
        {
            "type": "theory",
            "id": "c8s_ch3_b2_polymer",
            "data": {
                "title": "What are Synthetic Fibres?",
                "content": "A synthetic fibre is a chain of small chemical units joined together. Each small unit is a chemical substance. Many such small units combine to form a large single unit called a **polymer**.\n\nThe word polymer comes from two Greek words: 'poly' meaning many, and 'mer' meaning part/unit. So, a polymer is made of many repeating units.\n\n*Note: Cotton is a natural polymer called cellulose, which is made up of a large number of glucose units.*"
            }
        },
        {
            "type": "teacher_tip",
            "id": "c8s_ch3_b3_tip",
            "data": {
                "content": "Think of a polymer like a necklace made of identical beads. Each bead is a small chemical unit (monomer), and the entire necklace is the polymer!"
            }
        },
        {
            "type": "theory",
            "id": "c8s_ch3_b4_types",
            "data": {
                "title": "Types of Synthetic Fibres",
                "content": "Let's look at the four main types of synthetic fibres:\n\n1. **Rayon (Artificial Silk):** Made by chemical treatment of wood pulp. Although obtained from a natural source, it is a man-made fibre. It is cheaper than silk and can be woven like silk fibres.\n\n2. **Nylon:** The first fully synthetic fibre (made in 1931 without using any natural raw material from plants or animals). It was prepared from coal, water, and air. Nylon is strong, elastic, and light. It is used to make parachutes and ropes for rock climbing because a nylon thread is actually stronger than a steel wire!\n\n3. **Polyester:** Fabric made from this fibre does not get wrinkled easily. It remains crisp and is easy to wash. PET (polyethylene terephthalate) is a very familiar form of polyester, used for making bottles and utensils.\n\n4. **Acrylic:** Resembles wool. Clothes made from acrylic are relatively cheap and available in a variety of colors compared to natural wool."
            }
        },
        {
            "type": "flashcard",
            "id": "c8s_ch3_b5_fc1",
            "data": {
                "front": "Which synthetic fibre is also known as artificial silk?",
                "back": "Rayon"
            }
        },
        {
            "type": "quiz",
            "id": "c8s_ch3_b6_quiz1",
            "data": {
                "question": "Which of the following fibres is prepared without using any natural raw material from plants or animals?",
                "options": ["Rayon", "Cotton", "Nylon", "Wool"],
                "correct_index": 2,
                "explanation": "Nylon was the first fully synthetic fibre, prepared from coal, water, and air."
            }
        },
        {
            "type": "theory",
            "id": "c8s_ch3_b7_plastics",
            "data": {
                "title": "Plastics: The Indispensable Polymer 🥤",
                "content": "Like synthetic fibres, plastic is also a polymer. Plastics do not have the same type of arrangement of units. In some it is linear, whereas in others it is cross-linked.\n\n**Types of Plastics:**\n1. **Thermoplastics:** Plastics which get deformed easily on heating and can be bent easily. Examples: Polythene and PVC. Used for making toys and containers.\n2. **Thermosetting Plastics:** Plastics which when moulded once, cannot be softened by heating. Examples: Bakelite and Melamine.\n\n- **Bakelite:** A poor conductor of heat and electricity. Used for making electrical switches and handles of various utensils.\n- **Melamine:** A versatile material that resists fire and can tolerate heat better than other plastics. Used for making floor tiles and kitchenware."
            }
        },
        {
            "type": "common_mistakes",
            "id": "c8s_ch3_b8_mistake",
            "data": {
                "content": "Don't confuse Thermoplastics and Thermosetting plastics. Remember: 'Setting' means it is 'set' in place and cannot be melted again!"
            }
        },
        {
            "type": "theory",
            "id": "c8s_ch3_b9_environment",
            "data": {
                "title": "Plastics and the Environment 🌍",
                "content": "A material which gets decomposed through natural processes (such as action by bacteria) is called **biodegradable** (e.g., peels of vegetables, paper, cotton).\n\nA material which is not easily decomposed by natural processes is termed **non-biodegradable** (e.g., plastics, tin, aluminum cans).\n\nSince plastics take several years to decompose, they are not environment friendly. It causes environmental pollution. Besides, the burning process of synthetic material is quite slow and it releases lots of poisonous fumes into the atmosphere.\n\n**The 5R Principle for Plastics:**\nReduce, Reuse, Recycle, Recover, and Refuse."
            }
        },
        {
            "type": "quiz",
            "id": "c8s_ch3_b10_quiz2",
            "data": {
                "question": "Which of the following is an example of a thermosetting plastic?",
                "options": ["PVC", "Polythene", "Bakelite", "Nylon"],
                "correct_index": 2,
                "explanation": "Bakelite and Melamine are thermosetting plastics, meaning they cannot be softened by heating once moulded."
            }
        }
    ]

def generate_blocks_ch4():
    return [
        {
            "type": "theory",
            "id": "c8s_ch4_b1_hook",
            "data": {
                "title": "The World of Metals and Non-Metals ⚙️",
                "content": "Look at the electrical wires in your house, the jewelry you wear, and the coal used in barbecues. You can easily distinguish between them by how they look and feel. This is because elements are broadly classified into Metals and Non-Metals based on their physical and chemical properties!"
            }
        },
        {
            "type": "media",
            "id": "c8s_ch4_b2_media",
            "data": {
                "mediaType": "image",
                "url": "assets/images/metals_ch4.jpg",
                "caption": "Comparison of shiny, malleable metals against dull, brittle non-metals."
            }
        },
        {
            "type": "theory",
            "id": "c8s_ch4_b3_physical",
            "data": {
                "title": "Physical Properties",
                "content": "Let's explore the physical properties that separate metals from non-metals:\n\n1. **Malleability:** The property of metals by which they can be beaten into thin sheets (e.g., aluminium foil). Non-metals break into pieces (they are brittle).\n2. **Ductility:** The property of metals by which they can be drawn into wires (e.g., copper wires).\n3. **Sonorousness:** Metals produce a ringing sound when struck hard. Non-metals do not.\n4. **Conductivity:** Metals are good conductors of heat and electricity. Non-metals are poor conductors.\n5. **Appearance:** Metals are generally hard and lustrous (shiny). Non-metals are soft and dull.\n\n*Exceptions:* Sodium and potassium are metals but are soft and can be cut with a knife. Mercury is the only metal found in liquid state at room temperature."
            }
        },
        {
            "type": "flashcard",
            "id": "c8s_ch4_b4_fc1",
            "data": {
                "front": "What property of metals allows them to be drawn into wires?",
                "back": "Ductility"
            }
        },
        {
            "type": "theory",
            "id": "c8s_ch4_b5_chemical",
            "data": {
                "title": "Chemical Properties: Reaction with Oxygen & Water",
                "content": "**1. Reaction with Oxygen:**\nMetals react with oxygen to form metallic oxides, which are basic in nature. For example, iron rusts when exposed to oxygen and water.\n*Non-metals* react with oxygen to form non-metallic oxides, which are generally acidic in nature (e.g., sulphur dioxide).\n\n**2. Reaction with Water:**\nSome metals react vigorously with water. For example, Sodium is highly reactive and catches fire if exposed to oxygen or water, so it is stored in kerosene.\nGenerally, non-metals do not react with water, though some (like phosphorus) may be very reactive in air and are stored in water."
            }
        },
        {
            "type": "teacher_tip",
            "id": "c8s_ch4_b6_tip",
            "data": {
                "content": "A simple trick: Metallic oxides are Basic (M-B). Non-Metallic oxides are Acidic (N-A)."
            }
        },
        {
            "type": "theory",
            "id": "c8s_ch4_b7_acids",
            "data": {
                "title": "Reaction with Acids & Displacement Reactions",
                "content": "**Reaction with Acids:**\nMetals generally react with acids and produce hydrogen gas that burns with a 'pop' sound. Non-metals generally do not react with acids.\n\n**Displacement Reactions:**\nA more reactive metal can replace a less reactive metal from its compound in an aqueous solution. For example, if you put an iron nail in copper sulphate solution (blue), the iron displaces the copper, turning the solution green (iron sulphate) and leaving a brown coating of copper on the nail."
            }
        },
        {
            "type": "quiz",
            "id": "c8s_ch4_b8_quiz1",
            "data": {
                "question": "Which of the following metals is stored in kerosene because it is highly reactive?",
                "options": ["Gold", "Iron", "Sodium", "Copper"],
                "correct_index": 2,
                "explanation": "Sodium reacts vigorously with oxygen and water, generating a lot of heat, so it is stored in kerosene."
            }
        },
        {
            "type": "theory",
            "id": "c8s_ch4_b9_uses",
            "data": {
                "title": "Uses of Metals and Non-Metals",
                "content": "**Uses of Metals:**\nUsed in making machinery, automobiles, airplanes, trains, satellites, industrial gadgets, cooking utensils, and water boilers due to their strength and conductivity.\n\n**Uses of Non-Metals:**\n- Oxygen is essential for life and respiration.\n- Nitrogen and Phosphorus are used in fertilizers to enhance plant growth.\n- Chlorine is used in water purification.\n- Iodine solution is used as an antiseptic on wounds."
            }
        }
    ]

def generate_blocks_ch5():
    return [
        {
            "type": "theory",
            "id": "c8s_ch5_b1_hook",
            "data": {
                "title": "The Black Gold of the Earth 🛢️",
                "content": "Imagine a world without petrol for cars, diesel for trucks, or electricity generated from coal. Our modern world runs on fossil fuels, but these resources took hundreds of millions of years to form deep underground. Today, we will explore Coal and Petroleum, the buried treasures of the Earth."
            }
        },
        {
            "type": "media",
            "id": "c8s_ch5_b2_media",
            "data": {
                "mediaType": "image",
                "url": "assets/images/coal_petroleum_ch5.jpg",
                "caption": "A cross-section of the Earth showing deep underground layers of coal and petroleum reservoirs."
            }
        },
        {
            "type": "theory",
            "id": "c8s_ch5_b3_resources",
            "data": {
                "title": "Natural Resources",
                "content": "Natural resources are classified into two main kinds:\n\n1. **Inexhaustible Natural Resources:** These are present in unlimited quantity in nature and are not likely to be exhausted by human activities. Examples: Sunlight, air.\n\n2. **Exhaustible Natural Resources:** The amount of these resources in nature is limited. They can be exhausted by human activities. Examples: Forests, wildlife, minerals, coal, petroleum, natural gas."
            }
        },
        {
            "type": "theory",
            "id": "c8s_ch5_b4_coal",
            "data": {
                "title": "Coal and Its Products",
                "content": "Coal is as hard as stone and is black in colour. About 300 million years ago, the earth had dense forests in low-lying wetland areas. Due to natural processes like flooding, these forests got buried under the soil. Under high pressure and high temperature, dead plants got slowly converted to coal. This slow process is called **carbonisation**.\n\nWhen heated in air, coal burns and produces mainly carbon dioxide gas.\n\n**Products obtained from processing coal:**\n- **Coke:** A tough, porous, and black substance. It is an almost pure form of carbon, used in the manufacture of steel and in the extraction of many metals.\n- **Coal Tar:** A black, thick liquid with an unpleasant smell. It is a mixture of about 200 substances used in manufacturing synthetic dyes, drugs, explosives, and perfumes.\n- **Coal Gas:** Obtained during the processing of coal to get coke. It is used as a fuel."
            }
        },
        {
            "type": "flashcard",
            "id": "c8s_ch5_b5_fc1",
            "data": {
                "front": "What is the slow process of conversion of dead vegetation into coal called?",
                "back": "Carbonisation"
            }
        },
        {
            "type": "theory",
            "id": "c8s_ch5_b6_petroleum",
            "data": {
                "title": "Petroleum: The Liquid Gold",
                "content": "Petroleum was formed from organisms living in the sea. As these organisms died, their bodies settled at the bottom of the sea and got covered with layers of sand and clay. Over millions of years, absence of air, high temperature, and high pressure transformed the dead organisms into petroleum and natural gas.\n\nPetroleum is a dark oily liquid with an unpleasant odour. It is a mixture of various constituents such as petroleum gas, petrol, diesel, lubricating oil, paraffin wax, etc."
            }
        },
        {
            "type": "theory",
            "id": "c8s_ch5_b7_refining",
            "data": {
                "title": "Refining of Petroleum",
                "content": "The process of separating the various constituents/fractions of petroleum is known as **refining**. It is carried out in a petroleum refinery.\n\nMany useful substances are obtained from petroleum and natural gas, termed as 'petrochemicals'. Due to its great commercial importance, petroleum is also called **'black gold'**."
            }
        },
        {
            "type": "quiz",
            "id": "c8s_ch5_b8_quiz1",
            "data": {
                "question": "Which of the following is an almost pure form of carbon obtained from coal?",
                "options": ["Coal tar", "Coke", "Coal gas", "Petroleum"],
                "correct_index": 1,
                "explanation": "Coke is a tough, porous, black substance that is an almost pure form of carbon."
            }
        },
        {
            "type": "theory",
            "id": "c8s_ch5_b9_naturalgas",
            "data": {
                "title": "Natural Gas and Conservation",
                "content": "Natural gas is a very important fossil fuel because it is easy to transport through pipes. When stored under high pressure, it is called **Compressed Natural Gas (CNG)**. CNG is a cleaner fuel and is used for power generation and as fuel for transport vehicles.\n\n**Conservation:**\nFossil fuels take millions of years to form. Burning them is a major cause of air pollution and global warming. PCRA (Petroleum Conservation Research Association) advises people how to save petrol/diesel while driving (e.g., drive at a constant speed, ensure correct tyre pressure)."
            }
        }
    ]

def update_curriculum():
    print("Loading master curriculum...")
    with open(CURRICULUM_PATH, 'r') as f:
        data = json.load(f)

    print("Injecting Chapter 2...")
    data["gseb_class8_science_ch2"] = generate_blocks_ch2()
    
    print("Injecting Chapter 3...")
    data["gseb_class8_science_ch3"] = generate_blocks_ch3()
    
    print("Injecting Chapter 4...")
    data["gseb_class8_science_ch4"] = generate_blocks_ch4()
    
    print("Injecting Chapter 5...")
    data["gseb_class8_science_ch5"] = generate_blocks_ch5()

    print("Saving updated curriculum...")
    with open(CURRICULUM_PATH, 'w') as f:
        json.dump(data, f, indent=2)
        
    print("Done! Chapters 2, 3, 4, and 5 have been fully upgraded.")

if __name__ == '__main__':
    update_curriculum()
