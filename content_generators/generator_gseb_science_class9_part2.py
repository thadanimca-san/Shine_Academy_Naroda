import json
import os

CURRICULUM_PATH = '/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/master_curriculum.json'

def ch9_blocks():
    return [
        {"type": "theory", "id": "c9s_ch9_b1", "data": {"title": "Force and Laws of Motion \ud83d\udcaa", "content": "What causes motion? Why does a football move when you kick it, but a heavy stone doesn't? The answer is FORCE! Let's explore the hidden rules that govern how everything in the universe pushes and pulls."}},
        {"type": "media", "id": "c9s_ch9_b2", "data": {"mediaType": "image", "url": "assets/images/forces_ch5_1786202726393.jpg", "caption": "Unbalanced forces cause acceleration."}},
        {"type": "theory", "id": "c9s_ch9_b3", "data": {"title": "Newton's First Law (Inertia)", "content": "An object remains in a state of rest or of uniform motion in a straight line unless compelled to change that state by an applied force. \nThis tendency of undisturbed objects to stay at rest or keep moving is called **Inertia**."}},
        {"type": "flashcard", "id": "c9s_ch9_b4", "data": {"front": "Why do you fall backward when a bus suddenly starts moving?", "back": "Because of Inertia of Rest. Your lower body moves with the bus, but your upper body tries to stay at rest!"}},
        {"type": "theory", "id": "c9s_ch9_b5", "data": {"title": "Newton's Second Law", "content": "The rate of change of momentum of an object is proportional to the applied unbalanced force in the direction of the force.\nThis gives us the famous equation: **F = m \u00d7 a** (Force = mass \u00d7 acceleration). The SI unit of force is the Newton (N)."}},
        {"type": "quiz", "id": "c9s_ch9_b6", "data": {"question": "What is the momentum (p) of an object?", "options": ["Mass / Velocity", "Mass + Velocity", "Mass \u00d7 Velocity", "Velocity / Mass"], "correct_index": 2, "explanation": "Momentum (p = mv) has both direction and magnitude. Its SI unit is kg m/s."}},
        {"type": "theory", "id": "c9s_ch9_b7", "data": {"title": "Newton's Third Law", "content": "To every action, there is an equal and opposite reaction.\nWhen you walk, you push the ground backward (action). The ground pushes you forward with an equal force (reaction). Both forces act on different bodies!"}}
    ]

def ch10_blocks():
    return [
        {"type": "theory", "id": "c9s_ch10_b1", "data": {"title": "Gravitation \ud83c\udf4e", "content": "Why did the apple fall on Newton's head? Why doesn't the moon crash into the Earth? The answer is Gravitation\u2014the invisible force that holds the entire universe together!"}},
        {"type": "media", "id": "c9s_ch10_b2", "data": {"mediaType": "image", "url": "assets/images/earth_ch13_1786204499579.jpg", "caption": "Earth's gravity holding the moon in orbit."}},
        {"type": "theory", "id": "c9s_ch10_b3", "data": {"title": "Universal Law of Gravitation", "content": "Every object in the universe attracts every other object with a force which is proportional to the product of their masses and inversely proportional to the square of the distance between them.\nEquation: **F = G(M \u00d7 m) / d\u00b2**"}},
        {"type": "flashcard", "id": "c9s_ch10_b4", "data": {"front": "What is the difference between Mass (m) and Weight (W)?", "back": "Mass is the amount of matter (constant everywhere). Weight is the force of gravity acting on that mass (W = m \u00d7 g). Weight changes depending on the planet!"}},
        {"type": "theory", "id": "c9s_ch10_b5", "data": {"title": "Free Fall and Acceleration Due to Gravity (g)", "content": "When objects fall towards the earth under gravity alone, we say they are in free fall. \nThe earth's gravity produces an acceleration called 'g', which is approximately **9.8 m/s\u00b2** on the surface of the earth."}},
        {"type": "quiz", "id": "c9s_ch10_b6", "data": {"question": "If your mass is 60 kg on Earth, what will be your mass on the Moon?", "options": ["10 kg", "60 kg", "360 kg", "0 kg"], "correct_index": 1, "explanation": "Mass remains CONSTANT everywhere! Your weight would change (it would be 1/6th on the moon), but your mass stays 60 kg."}},
        {"type": "theory", "id": "c9s_ch10_b7", "data": {"title": "Thrust and Pressure", "content": "The force acting on an object perpendicular to the surface is called **thrust**.\nThe thrust on unit area is called **pressure**. Pressure = Thrust / Area.\nThis is why a sharp knife cuts better than a blunt one (smaller area = higher pressure!)."}}
    ]

def ch11_blocks():
    return [
        {"type": "theory", "id": "c9s_ch11_b1", "data": {"title": "Work and Energy \u26a1", "content": "In daily life, studying hard is 'work'. But in physics, studying is ZERO work! Physics has a very specific definition of Work and Energy. Let's find out what it is."}},
        {"type": "media", "id": "c9s_ch11_b2", "data": {"mediaType": "image", "url": "assets/images/electricity_ch4_1786202713539.jpg", "caption": "Energy makes work possible."}},
        {"type": "theory", "id": "c9s_ch11_b3", "data": {"title": "Scientific Definition of Work", "content": "Work is said to be done only when a force applied on an object causes a displacement in the direction of the force.\n**W = F \u00d7 s** (Work = Force \u00d7 displacement).\nIf you push a wall all day and it doesn't move, you have done ZERO work according to physics!"}},
        {"type": "flashcard", "id": "c9s_ch11_b4", "data": {"front": "What is the SI unit of Work and Energy?", "back": "The Joule (J)."}},
        {"type": "theory", "id": "c9s_ch11_b5", "data": {"title": "Forms of Energy", "content": "**Kinetic Energy (KE):** Energy possessed by an object due to its motion. Formula: \u00bd(mv\u00b2).\n**Potential Energy (PE):** Energy possessed by an object due to its position or shape. Formula: mgh (mass \u00d7 gravity \u00d7 height).\nMechanical Energy = KE + PE."}},
        {"type": "quiz", "id": "c9s_ch11_b6", "data": {"question": "The Law of Conservation of Energy states that:", "options": ["Energy can be created.", "Energy can be destroyed.", "Energy can only be transformed from one form to another.", "Total energy of the universe is decreasing."], "correct_index": 2, "explanation": "Energy can neither be created nor destroyed. The total energy before and after transformation remains exactly the same."}},
        {"type": "theory", "id": "c9s_ch11_b7", "data": {"title": "Power", "content": "Power is defined as the rate of doing work or the rate of transfer of energy.\n**P = W / t** (Power = Work / time).\nThe SI unit of power is the Watt (W). 1 kilowatt (kW) = 1000 Watts."}}
    ]

def ch12_blocks():
    return [
        {"type": "theory", "id": "c9s_ch12_b1", "data": {"title": "Sound \ud83d\udd0a", "content": "How do you hear your friend's voice? Sound is a form of energy that produces a sensation of hearing in our ears. Let's look at how sound waves travel through the air."}},
        {"type": "media", "id": "c9s_ch12_b2", "data": {"mediaType": "image", "url": "assets/images/earth_ch13_1786204499579.jpg", "caption": "Sound travels as longitudinal waves."}},
        {"type": "theory", "id": "c9s_ch12_b3", "data": {"title": "Production and Propagation of Sound", "content": "Sound is produced by vibrating objects. As an object vibrates, it sets the particles of the medium around it vibrating. \nSound is a mechanical wave and needs a material medium (air, water, steel) for its propagation. It cannot travel through a vacuum!"}},
        {"type": "teacher_tip", "id": "c9s_ch12_b4", "data": {"content": "Sound waves in air are longitudinal waves. This means the individual particles of the medium move in a direction parallel to the direction of propagation of the disturbance (creating compressions and rarefactions)."}},
        {"type": "theory", "id": "c9s_ch12_b5", "data": {"title": "Characteristics of a Sound Wave", "content": "**Frequency (\u03bd):** Number of oscillations per second. Determines the **pitch** of the sound (shrillness).\n**Amplitude (A):** The maximum displacement. Determines the **loudness** of the sound.\n**Wavelength (\u03bb):** The distance between two consecutive compressions."}},
        {"type": "quiz", "id": "c9s_ch12_b6", "data": {"question": "What is the audible range of hearing for an average human being?", "options": ["20 Hz to 20,000 Hz", "2 Hz to 2,000 Hz", "200 Hz to 200,000 Hz", "0 Hz to 20 Hz"], "correct_index": 0, "explanation": "Sounds below 20 Hz are infrasonic, and above 20,000 Hz are ultrasonic (which bats and dolphins can hear)."}},
        {"type": "theory", "id": "c9s_ch12_b7", "data": {"title": "Reflection of Sound (Echo)", "content": "Sound bounces off solid or liquid surfaces just like light. The sensation of sound persists in our brain for about 0.1s. To hear a distinct echo, the time interval between the original sound and the reflected one must be at least 0.1s!"}}
    ]

def ch13_blocks():
    return [
        {"type": "theory", "id": "c9s_ch13_b1", "data": {"title": "Why Do We Fall Ill? \ud83e\udd12", "content": "Sometimes we get a cold, sometimes a fever. What happens inside our bodies when we get sick? Let's explore health, diseases, and how our immune system fights back."}},
        {"type": "media", "id": "c9s_ch13_b2", "data": {"mediaType": "image", "url": "assets/images/health_ch3_1786202700935.jpg", "caption": "Microbes and human health."}},
        {"type": "theory", "id": "c9s_ch13_b3", "data": {"title": "Health vs Disease-Free", "content": "Health is a state of physical, mental, and social well-being. Being 'disease-free' just means you don't have a specific sickness right now. Good health requires proper nutrition, a clean environment, and a stress-free life."}},
        {"type": "flashcard", "id": "c9s_ch13_b4", "data": {"front": "What is the difference between Acute and Chronic diseases?", "back": "Acute diseases last for only very short periods (e.g., common cold). Chronic diseases last for a long time, even as much as a lifetime (e.g., diabetes, elephantiasis)."}},
        {"type": "theory", "id": "c9s_ch13_b5", "data": {"title": "Infectious vs Non-Infectious Diseases", "content": "**Infectious Diseases:** Caused by microbes (pathogens) like viruses, bacteria, fungi, or protozoa. They can spread from person to person. Example: COVID-19, Malaria, Tuberculosis.\n**Non-Infectious Diseases:** Not caused by microbes and do not spread. Example: Cancer, High blood pressure."}},
        {"type": "quiz", "id": "c9s_ch13_b6", "data": {"question": "Malaria is a deadly infectious disease. What type of pathogen causes Malaria?", "options": ["Virus", "Bacteria", "Fungi", "Protozoan"], "correct_index": 3, "explanation": "Malaria is caused by a protozoan called Plasmodium, which is transmitted by the bite of a female Anopheles mosquito."}},
        {"type": "theory", "id": "c9s_ch13_b7", "data": {"title": "Principles of Prevention", "content": "Prevention is better than cure! We can prevent infectious diseases by:\n1. **General ways:** Clean water, sanitation, and avoiding overcrowding.\n2. **Specific ways:** Vaccination (Immunization) which trains the immune system to fight specific pathogens before they attack."}}
    ]

def ch14_blocks():
    return [
        {"type": "theory", "id": "c9s_ch14_b1", "data": {"title": "Natural Resources \ud83c\udf33", "content": "Earth is the only planet we know that has life. Life on Earth depends on a beautiful balance of land (Lithosphere), water (Hydrosphere), and air (Atmosphere). Let's learn how these natural resources sustain us."}},
        {"type": "media", "id": "c9s_ch14_b2", "data": {"mediaType": "image", "url": "assets/images/earth_ch13_1786204499579.jpg", "caption": "The Biosphere where life thrives."}},
        {"type": "theory", "id": "c9s_ch14_b3", "data": {"title": "The Breath of Life: Air", "content": "Air is a mixture of many gases like nitrogen, oxygen, carbon dioxide, and water vapour. Oxygen is essential for respiration and combustion. Carbon dioxide is fixed by plants during photosynthesis.\nThe atmosphere also acts as a climate control blanket, keeping the Earth's temperature steady."}},
        {"type": "flashcard", "id": "c9s_ch14_b4", "data": {"front": "What is the function of the Ozone Layer?", "back": "It absorbs harmful ultraviolet (UV) radiations from the Sun, preventing them from reaching the surface of the Earth."}},
        {"type": "theory", "id": "c9s_ch14_b5", "data": {"title": "Water: A Wonder Liquid", "content": "Water occupies a very large area of the Earth's surface (about 71%). All cellular processes take place in a water medium. The availability of water decides the number of individuals of each species that are able to survive in a particular area, and it dictates the diversity of life there."}},
        {"type": "quiz", "id": "c9s_ch14_b6", "data": {"question": "Which biogeochemical cycle involves evaporation, transpiration, and precipitation?", "options": ["Carbon Cycle", "Nitrogen Cycle", "Water Cycle", "Oxygen Cycle"], "correct_index": 2, "explanation": "The Water Cycle (hydrological cycle) describes the continuous movement of water on, above, and below the surface of the Earth."}},
        {"type": "theory", "id": "c9s_ch14_b7", "data": {"title": "Biogeochemical Cycles", "content": "The constant interaction between the biotic (living) and abiotic (non-living) components of the biosphere makes it a dynamic system. \nImportant cycles include:\n1. The Water Cycle\n2. The Nitrogen Cycle (bacteria fix atmospheric nitrogen into the soil).\n3. The Carbon Cycle (carbon moves from CO2 in the air to plants, animals, and back)."}}
    ]

def ch15_blocks():
    return [
        {"type": "theory", "id": "c9s_ch15_b1", "data": {"title": "Improvement in Food Resources \ud83c\udf3e", "content": "With India's population soaring over 1.4 billion, we need more than a billion tonnes of grain every year! We can't just find more land to farm. We need to improve our food production efficiently."}},
        {"type": "media", "id": "c9s_ch15_b2", "data": {"mediaType": "image", "url": "assets/images/science_method.jpg", "caption": "Agricultural science in action."}},
        {"type": "theory", "id": "c9s_ch15_b3", "data": {"title": "Improvement in Crop Yields", "content": "Major groups of activities for improving crop yields:\n1. **Crop Variety Improvement:** Using hybridization or genetically modified crops (GMOs) to get higher yield, disease resistance, and better quality.\n2. **Crop Production Management:** Proper nutrient management (manures/fertilizers), irrigation, and cropping patterns.\n3. **Crop Protection Management:** Protecting crops from weeds, insects, pests, and diseases."}},
        {"type": "teacher_tip", "id": "c9s_ch15_b4", "data": {"content": "Did you know? The Green Revolution contributed to increased food-grain production, while the White Revolution led to better and more efficient use as well as availability of milk!"}},
        {"type": "theory", "id": "c9s_ch15_b5", "data": {"title": "Cropping Patterns", "content": "**Mixed Cropping:** Growing two or more crops simultaneously on the same piece of land (e.g., wheat + gram).\n**Intercropping:** Growing two or more crops in a definite row pattern (e.g., soybean + maize).\n**Crop Rotation:** Growing different crops on a piece of land in a pre-planned succession."}},
        {"type": "quiz", "id": "c9s_ch15_b6", "data": {"question": "What are Macronutrients for plants?", "options": ["Nutrients required in small quantities (like Iron, Zinc).", "Nutrients required in large quantities (like Nitrogen, Phosphorus, Potassium).", "Nutrients obtained only from water.", "Nutrients that harm the plant."], "correct_index": 1, "explanation": "Macronutrients are needed in large amounts. The most common fertilizers supply Nitrogen, Phosphorus, and Potassium (NPK)."}},
        {"type": "theory", "id": "c9s_ch15_b7", "data": {"title": "Animal Husbandry", "content": "Farming is not just about plants! Animal husbandry is the scientific management of animal livestock. It includes feeding, breeding, and disease control.\nIt covers:\n- **Cattle Farming:** For milk (dairy) and draught labor (agricultural work).\n- **Poultry Farming:** Rearing fowls for egg production and chicken meat.\n- **Fish Production:** Aquaculture and capture fishing."}}
    ]

def update_curriculum():
    print("Loading master curriculum...")
    with open(CURRICULUM_PATH, 'r') as f:
        data = json.load(f)

    data["gseb_class9_science_ch9"] = ch9_blocks()
    data["gseb_class9_science_ch10"] = ch10_blocks()
    data["gseb_class9_science_ch11"] = ch11_blocks()
    data["gseb_class9_science_ch12"] = ch12_blocks()
    data["gseb_class9_science_ch13"] = ch13_blocks()
    data["gseb_class9_science_ch14"] = ch14_blocks()
    data["gseb_class9_science_ch15"] = ch15_blocks()

    print("Saving updated curriculum (Class 9 Science - Part 2)...")
    with open(CURRICULUM_PATH, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    update_curriculum()
