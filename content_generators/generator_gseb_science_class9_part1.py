import json
import os

CURRICULUM_PATH = '/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/master_curriculum.json'

def ch1_blocks():
    return [
        {"type": "theory", "id": "c9s_ch1_b1", "data": {"title": "Matter in Our Surroundings \ud83c\udf0d", "content": "Look around you. The chair you are sitting on, the air you breathe, the water you drink, and even your own body\u2014everything is made of matter. But what exactly is matter? And how small are the building blocks that make it up? Let's dive into the invisible world!"}},
        {"type": "media", "id": "c9s_ch1_b2", "data": {"mediaType": "image", "url": "assets/images/atom_structure_1786112780457.jpg", "caption": "Matter is made of incredibly tiny particles."}},
        {"type": "dictionary_link", "id": "c9s_ch1_b3", "data": {"term_id": "DICT_MATTER"}},
        {"type": "theory", "id": "c9s_ch1_b4", "data": {"title": "Physical Nature of Matter", "content": "Early Indian philosophers classified matter into five basic elements (Panch Tatva)\u2014air, earth, fire, sky, and water. Modern science categorizes matter based on its physical and chemical properties. \n\n**1. Matter is made up of particles.**\n**2. These particles are incredibly small (beyond our imagination).**"}},
        {"type": "flashcard", "id": "c9s_ch1_b5", "data": {"front": "What happens when you dissolve salt in a glass of water?", "back": "The salt particles get into the empty spaces between the water particles, showing that matter has space between its particles."}},
        {"type": "teacher_tip", "id": "c9s_ch1_b6", "data": {"content": "Particles of matter are continuously moving. As temperature rises, they move faster! This is why the smell of hot sizzling food reaches you from meters away, but you have to go close to cold food to smell it."}},
        {"type": "theory", "id": "c9s_ch1_b7", "data": {"title": "States of Matter", "content": "Matter exists in three main states:\n\n**Solid:** Fixed shape and volume. Particles are tightly packed.\n**Liquid:** Fixed volume but no fixed shape. Particles are less tightly packed and can flow.\n**Gas:** No fixed shape or volume. Particles move freely at high speeds."}},
        {"type": "dictionary_link", "id": "c9s_ch1_b8", "data": {"term_id": "DICT_SUBLIMATION"}},
        {"type": "quiz", "id": "c9s_ch1_b9", "data": {"question": "The change of state directly from solid to gas without changing into a liquid is called:", "options": ["Evaporation", "Sublimation", "Condensation", "Fusion"], "correct_index": 1, "explanation": "Sublimation occurs when substances like camphor or solid CO2 (dry ice) are heated."}},
        {"type": "theory", "id": "c9s_ch1_b10", "data": {"title": "Evaporation Causes Cooling \u2744\ufe0f", "content": "During evaporation, the particles of liquid absorb energy from the surroundings to overcome the forces of attraction. This absorption of energy makes the surroundings cold. \nThat's why we sweat in summer! The sweat evaporates, absorbing heat from our body, leaving us cool."}}
    ]

def ch2_blocks():
    return [
        {"type": "theory", "id": "c9s_ch2_b1", "data": {"title": "Is Matter Around Us Pure? \ud83d\udd2c", "content": "When you buy milk or ghee from the market, it often says '100% Pure' on the packet. But to a scientist, milk is NOT pure! It is a mixture of water, fat, and proteins. Let's learn the scientific difference between pure substances and mixtures."}},
        {"type": "media", "id": "c9s_ch2_b2", "data": {"mediaType": "image", "url": "assets/images/science_method.jpg", "caption": "Separating mixtures in a laboratory."}},
        {"type": "theory", "id": "c9s_ch2_b3", "data": {"title": "What is a Mixture?", "content": "A pure substance consists of a single type of particles. A mixture contains more than one kind of pure form of matter. \n\n**Homogeneous Mixture:** Uniform composition throughout (e.g., salt in water).\n**Heterogeneous Mixture:** Non-uniform composition with distinct parts (e.g., sand and salt, or oil and water)."}},
        {"type": "flashcard", "id": "c9s_ch2_b4", "data": {"front": "What is an Alloy?", "back": "An alloy is a homogeneous mixture of two or more metals (e.g., Brass is a mixture of Zinc and Copper)."}},
        {"type": "theory", "id": "c9s_ch2_b5", "data": {"title": "Solutions, Suspensions, and Colloids", "content": "**Solution:** A homogeneous mixture (e.g., sugar water). Particles are so small they don't scatter light.\n**Suspension:** A heterogeneous mixture where particles do not dissolve but remain suspended (e.g., chalk powder in water). \n**Colloid:** Appears homogeneous but is actually heterogeneous. Particles are large enough to scatter a beam of light (Tyndall Effect). Example: Milk, fog."}},
        {"type": "quiz", "id": "c9s_ch2_b6", "data": {"question": "The scattering of a beam of light by colloidal particles is called:", "options": ["Newton's Effect", "Tyndall Effect", "Raman Effect", "Dispersion"], "correct_index": 1, "explanation": "The Tyndall effect can be seen when a fine beam of light enters a dark room through a small hole."}},
        {"type": "theory", "id": "c9s_ch2_b7", "data": {"title": "Physical and Chemical Changes", "content": "**Physical Change:** Only physical properties (shape, state) change. No new substance is formed. (e.g., Melting ice).\n**Chemical Change:** Reacts to form a completely new substance with different properties. (e.g., Burning paper, rusting iron)."}}
    ]

def ch3_blocks():
    return [
        {"type": "theory", "id": "c9s_ch3_b1", "data": {"title": "Atoms and Molecules \u269b\ufe0f", "content": "If you keep dividing matter into smaller and smaller pieces, you will eventually reach a particle so small it cannot be divided any further. This indivisible particle is the foundation of all chemistry: the Atom."}},
        {"type": "media", "id": "c9s_ch3_b2", "data": {"mediaType": "image", "url": "assets/images/atom_diagram_1786089354479.jpg", "caption": "The microscopic world of atoms."}},
        {"type": "theory", "id": "c9s_ch3_b3", "data": {"title": "Laws of Chemical Combination", "content": "**1. Law of Conservation of Mass:** Mass can neither be created nor destroyed in a chemical reaction.\n**2. Law of Constant Proportions:** In a chemical substance, the elements are always present in definite proportions by mass. (e.g., Water is always 1 part Hydrogen to 8 parts Oxygen by mass)."}},
        {"type": "flashcard", "id": "c9s_ch3_b4", "data": {"front": "What is Dalton's Atomic Theory?", "back": "Dalton proposed that all matter is made of tiny, indivisible particles called atoms. Atoms of a given element are identical in mass and chemical properties."}},
        {"type": "theory", "id": "c9s_ch3_b5", "data": {"title": "What is an Atom?", "content": "Atoms are the building blocks of all matter. They are extremely small. Their radius is measured in nanometers (1 nm = 10^-9 m).\nTo make writing formulas easier, IUPAC approves symbols for elements. For example, Hydrogen is H, Oxygen is O, and Iron is Fe (from Latin 'ferrum')."}},
        {"type": "quiz", "id": "c9s_ch3_b6", "data": {"question": "The number of atoms constituting a molecule is known as its:", "options": ["Valency", "Atomicity", "Atomic Mass", "Ionization"], "correct_index": 1, "explanation": "For example, an Oxygen molecule (O2) has an atomicity of 2 (diatomic). Ozone (O3) has an atomicity of 3."}},
        {"type": "theory", "id": "c9s_ch3_b7", "data": {"title": "Ions and Chemical Formulae", "content": "An ion is a charged particle. Positively charged ions are cations, negatively charged are anions.\nWhen writing the chemical formula of a compound, the valencies or charges on the ions must balance! For example, NaCl (Sodium Chloride) is formed from Na+ and Cl-."}}
    ]

def ch4_blocks():
    return [
        {"type": "theory", "id": "c9s_ch4_b1", "data": {"title": "Structure of the Atom \ud83c\udfaf", "content": "Dalton said atoms were indivisible. But then, scientists discovered that atoms actually contain even smaller particles inside them! Let's journey to the very core of the atom."}},
        {"type": "media", "id": "c9s_ch4_b2", "data": {"mediaType": "image", "url": "assets/images/atom_structure_1786112780457.jpg", "caption": "Electrons orbiting the nucleus."}},
        {"type": "theory", "id": "c9s_ch4_b3", "data": {"title": "Charged Particles in Matter", "content": "J.J. Thomson discovered the **Electron** (negatively charged). E. Goldstein discovered protons (positively charged). \nThomson proposed the 'Plum Pudding' model, where the atom is a positive sphere with negative electrons embedded inside it like raisins in a pudding."}},
        {"type": "teacher_tip", "id": "c9s_ch4_b4", "data": {"content": "Rutherford's Gold Foil experiment completely changed our understanding! Most alpha particles passed straight through the gold foil, proving that most of the space inside an atom is empty!"}},
        {"type": "theory", "id": "c9s_ch4_b5", "data": {"title": "Rutherford and Bohr Models", "content": "**Rutherford** concluded that all positive charge and mass is concentrated in a tiny center called the **nucleus**.\n**Neils Bohr** later proved that electrons orbit the nucleus only in special discrete orbits (energy levels) designated as K, L, M, N shells."}},
        {"type": "flashcard", "id": "c9s_ch4_b6", "data": {"front": "What particle was discovered by J. Chadwick in 1932 that has no charge and a mass nearly equal to a proton?", "back": "The Neutron"}},
        {"type": "quiz", "id": "c9s_ch4_b7", "data": {"question": "The maximum number of electrons that can be accommodated in the outermost orbit is:", "options": ["2", "8", "18", "32"], "correct_index": 1, "explanation": "This is known as the octet rule. An outermost shell with 8 electrons is considered highly stable."}},
        {"type": "theory", "id": "c9s_ch4_b8", "data": {"title": "Isotopes and Isobars", "content": "**Isotopes:** Atoms of the same element with the same atomic number but different mass numbers. (e.g., Carbon-12 and Carbon-14).\n**Isobars:** Atoms of different elements with different atomic numbers but the same mass number. (e.g., Calcium and Argon both have mass number 40)."}}
    ]

def ch5_blocks():
    return [
        {"type": "theory", "id": "c9s_ch5_b1", "data": {"title": "The Fundamental Unit of Life \ud83e\uddec", "content": "Just like a house is built of bricks, every living organism on Earth is built of microscopic blocks called Cells. In 1665, Robert Hooke looked at a slice of cork under a primitive microscope and discovered the first cells!"}},
        {"type": "media", "id": "c9s_ch5_b2", "data": {"mediaType": "image", "url": "assets/images/cell_diagram_1786112747885.jpg", "caption": "The structure of an animal cell."}},
        {"type": "theory", "id": "c9s_ch5_b3", "data": {"title": "What is a Cell Made Of?", "content": "Every cell has three main features:\n1. **Plasma Membrane:** The outermost flexible covering that allows certain materials in and out.\n2. **Nucleus:** The 'brain' of the cell containing DNA (genetic material).\n3. **Cytoplasm:** The fluid inside the cell containing specialized cell organelles."}},
        {"type": "flashcard", "id": "c9s_ch5_b4", "data": {"front": "Which organelle is known as the 'Powerhouse of the Cell' because it generates ATP energy?", "back": "Mitochondria"}},
        {"type": "theory", "id": "c9s_ch5_b5", "data": {"title": "Cell Wall and Organelles", "content": "Unlike animal cells, **Plant cells** have an extra rigid outer covering called the **Cell Wall** made of cellulose.\nOther important organelles include:\n- **Endoplasmic Reticulum (ER):** The transport network.\n- **Golgi Apparatus:** Packages and dispatches materials.\n- **Lysosomes:** The waste disposal system (suicide bags)."}},
        {"type": "quiz", "id": "c9s_ch5_b6", "data": {"question": "The movement of water molecules through a selectively permeable membrane is called:", "options": ["Diffusion", "Osmosis", "Plasmolysis", "Active Transport"], "correct_index": 1, "explanation": "Osmosis is the passage of water from a region of high water concentration to a region of low water concentration."}},
        {"type": "theory", "id": "c9s_ch5_b7", "data": {"title": "Prokaryotic vs Eukaryotic", "content": "Organisms like bacteria have no defined nuclear membrane and lack membrane-bound organelles. They are called **Prokaryotes**.\nOrganisms with cells having a true nuclear membrane (like plants and animals) are called **Eukaryotes**."}}
    ]

def ch6_blocks():
    return [
        {"type": "theory", "id": "c9s_ch6_b1", "data": {"title": "Tissues \ud83c\udf31", "content": "If cells are the bricks of a building, Tissues are the walls! A tissue is a group of similar cells working together to perform a specific function. Plants and animals are made of highly organized tissues."}},
        {"type": "media", "id": "c9s_ch6_b2", "data": {"mediaType": "image", "url": "assets/images/science_method.jpg", "caption": "Microscopic view of cellular tissues."}},
        {"type": "theory", "id": "c9s_ch6_b3", "data": {"title": "Plant Tissues", "content": "Plants don't move around, so most of their tissues are supportive and dead. \n**Meristematic Tissue:** Dividing tissues located at growing points (tips of roots and stems).\n**Permanent Tissue:** Formed when meristematic tissues lose the ability to divide. They take a permanent shape and function."}},
        {"type": "flashcard", "id": "c9s_ch6_b4", "data": {"front": "Which complex plant tissue transports water and minerals from roots to the rest of the plant?", "back": "Xylem (Remember: Xylem = Water, Phloem = Food)"}},
        {"type": "theory", "id": "c9s_ch6_b5", "data": {"title": "Animal Tissues", "content": "Animal tissues are broadly classified into four types:\n1. **Epithelial Tissue:** Protective covering (like skin).\n2. **Connective Tissue:** Connects and supports (like Blood, Bone, Cartilage).\n3. **Muscular Tissue:** Responsible for movement (Voluntary and Involuntary).\n4. **Nervous Tissue:** Transmits electrical signals (Neurons in brain and nerves)."}},
        {"type": "quiz", "id": "c9s_ch6_b6", "data": {"question": "Which type of muscle tissue is found in the heart and works involuntarily?", "options": ["Striated Muscle", "Smooth Muscle", "Cardiac Muscle", "Skeletal Muscle"], "correct_index": 2, "explanation": "Cardiac muscles are cylindrical, branched, and uninucleate. They undergo rhythmic contraction and relaxation throughout life."}},
        {"type": "teacher_tip", "id": "c9s_ch6_b7", "data": {"content": "Blood is surprisingly a type of connective tissue! It has a fluid matrix called plasma, in which red blood cells, white blood cells, and platelets are suspended."}}
    ]

def ch7_blocks():
    return [
        {"type": "theory", "id": "c9s_ch7_b1", "data": {"title": "Diversity in Living Organisms \ud83e\udd81", "content": "From tiny microscopic bacteria to giant blue whales, Earth is home to millions of species. How do scientists organize and study them all? By grouping them together based on similarities!"}},
        {"type": "media", "id": "c9s_ch7_b2", "data": {"mediaType": "image", "url": "assets/images/science_method.jpg", "caption": "The vast tree of life."}},
        {"type": "theory", "id": "c9s_ch7_b3", "data": {"title": "The 5 Kingdom Classification", "content": "Biologist Robert Whittaker proposed the Five Kingdom system:\n1. **Monera:** Bacteria (Prokaryotic, unicellular)\n2. **Protista:** Amoeba, algae (Eukaryotic, unicellular)\n3. **Fungi:** Mushrooms, yeast (Eukaryotic, heterotrophic)\n4. **Plantae:** All multicellular plants\n5. **Animalia:** All multicellular animals"}},
        {"type": "flashcard", "id": "c9s_ch7_b4", "data": {"front": "Which group of plants produces naked seeds (like pine trees)?", "back": "Gymnosperms. (Angiosperms produce seeds enclosed in fruits)."}},
        {"type": "theory", "id": "c9s_ch7_b5", "data": {"title": "Animalia Kingdom (Vertebrates vs Invertebrates)", "content": "Animals without a backbone (Invertebrates) include Porifera (sponges), Cnidaria (jellyfish), Annelida (earthworms), and Arthropoda (insects - the largest group!).\nAnimals with a true vertebral column (Vertebrates) include Pisces (fishes), Amphibia (frogs), Reptilia (snakes), Aves (birds), and Mammalia (humans)."}},
        {"type": "quiz", "id": "c9s_ch7_b6", "data": {"question": "Which class of vertebrates is warm-blooded, has a four-chambered heart, and mammary glands for the production of milk?", "options": ["Reptilia", "Aves", "Amphibia", "Mammalia"], "correct_index": 3, "explanation": "Mammals give birth to live young ones (mostly) and their skin has hairs as well as sweat and oil glands."}},
        {"type": "teacher_tip", "id": "c9s_ch7_b7", "data": {"content": "Remember the hierarchy of classification: Kingdom > Phylum > Class > Order > Family > Genus > Species (King Phillip Came Over For Good Soup!)."}}
    ]

def ch8_blocks():
    return [
        {"type": "theory", "id": "c9s_ch8_b1", "data": {"title": "Motion \ud83d\ude80", "content": "Everything in the universe is in motion. The blood in your veins, the Earth rotating, the stars moving. But what exactly is motion? Let's learn the language of Physics to describe how things move."}},
        {"type": "media", "id": "c9s_ch8_b2", "data": {"mediaType": "image", "url": "assets/images/forces_ch5_1786202726393.jpg", "caption": "Understanding speed, velocity, and acceleration."}},
        {"type": "theory", "id": "c9s_ch8_b3", "data": {"title": "Distance vs Displacement", "content": "**Distance** is the total path length covered by an object. It is a scalar quantity (only magnitude).\n**Displacement** is the shortest straight-line distance from the initial position to the final position. It is a vector quantity (magnitude AND direction).\n\nIf you run around a 400m circular track and return to the start, your distance is 400m, but your displacement is ZERO!"}},
        {"type": "flashcard", "id": "c9s_ch8_b4", "data": {"front": "What is the difference between Speed and Velocity?", "back": "Speed is the distance travelled per unit time (scalar). Velocity is speed in a specific direction (vector)."}},
        {"type": "theory", "id": "c9s_ch8_b5", "data": {"title": "Acceleration", "content": "When velocity changes, we say the object is accelerating. Acceleration is the rate of change of velocity.\nIf a car goes from 0 to 60 km/h, it is accelerating. If it hits the brakes and slows down, it experiences negative acceleration, also called **Retardation**."}},
        {"type": "quiz", "id": "c9s_ch8_b6", "data": {"question": "The area under a velocity-time graph gives which physical quantity?", "options": ["Acceleration", "Speed", "Displacement", "Force"], "correct_index": 2, "explanation": "The area under the v-t graph represents the magnitude of displacement (distance travelled) for a given time interval."}},
        {"type": "theory", "id": "c9s_ch8_b7", "data": {"title": "Equations of Motion", "content": "For uniform acceleration, there are three golden equations:\n1. v = u + at\n2. s = ut + \u00bd(at\u00b2)\n3. 2as = v\u00b2 - u\u00b2\n(Where u=initial velocity, v=final velocity, a=acceleration, t=time, s=distance)."}}
    ]

def update_curriculum():
    print("Loading master curriculum...")
    with open(CURRICULUM_PATH, 'r') as f:
        data = json.load(f)

    data["gseb_class9_science_ch1"] = ch1_blocks()
    data["gseb_class9_science_ch2"] = ch2_blocks()
    data["gseb_class9_science_ch3"] = ch3_blocks()
    data["gseb_class9_science_ch4"] = ch4_blocks()
    data["gseb_class9_science_ch5"] = ch5_blocks()
    data["gseb_class9_science_ch6"] = ch6_blocks()
    data["gseb_class9_science_ch7"] = ch7_blocks()
    data["gseb_class9_science_ch8"] = ch8_blocks()

    print("Saving updated curriculum (Class 9 Science - Part 1)...")
    with open(CURRICULUM_PATH, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    update_curriculum()
