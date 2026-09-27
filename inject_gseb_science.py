import json
import os

db_path = "app_core/learning_modules/master_curriculum.json"

with open(db_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

# CHAPTER 1: CROP PRODUCTION AND MANAGEMENT
db["gseb_class8_science_ch1"] = [
    {
        "type": "theory",
        "id": "c8s_ch1_b1_hook",
        "data": {
            "title": "The Global Food Challenge 🌍",
            "content": "Have you ever wondered how enough food is produced to feed over 1.4 billion people in India alone? It’s not just about planting seeds and hoping for the best. Agriculture is a massive, highly organized science. Today, we are going to explore the journey of your food—from the muddy fields all the way to your dinner plate!"
        }
    },
    {
        "type": "media",
        "id": "c8s_ch1_b2_media",
        "data": {
            "mediaType": "image",
            "url": "assets/images/particulate_ch7.jpg",
            "caption": "Farmers working diligently in an agricultural field."
        }
    },
    {
        "type": "dictionary_link",
        "id": "c8s_ch1_b3_dict",
        "data": {
            "term_id": "agriculture",
            "preview": "Agriculture: The science or practice of farming, including cultivation of the soil for the growing of crops and the rearing of animals."
        }
    },
    {
        "type": "theory",
        "id": "c8s_ch1_b4_types",
        "data": {
            "title": "Kharif vs Rabi Crops 🌾",
            "content": "In India, crops are broadly classified into two categories based on the seasons they are grown in:\n\n**1. Kharif Crops:** These are sown in the rainy season (June to September). They require a lot of water. Examples: Paddy (rice), maize, soyabean, groundnut, and cotton.\n\n**2. Rabi Crops:** These are grown in the winter season (October to March). They require less water and cooler temperatures. Examples: Wheat, gram, pea, mustard, and linseed."
        }
    },
    {
        "type": "memory_trick",
        "id": "c8s_ch1_b5_memory",
        "data": {
            "content": "To remember the seasons: \n🌧️ KHARIF = K for 'Knee-deep in water' (Rainy season, Rice).\n❄️ RABI = R for 'Roasting fires' (Winter season, Wheat)."
        }
    },
    {
        "type": "teacher_tip",
        "id": "c8s_ch1_b6_tip",
        "data": {
            "content": "Always remember: Paddy cannot be grown in the winter season because it requires a tremendous amount of water. That is why it is strictly a Kharif crop!"
        }
    },
    {
        "type": "theory",
        "id": "c8s_ch1_b7_practices",
        "data": {
            "title": "The 7 Basic Practices of Crop Production 🚜",
            "content": "To successfully grow a crop, a farmer must perform a series of activities in a specific sequence over a period of time. These are called Agricultural Practices:\n\n1. Preparation of Soil\n2. Sowing of Seeds\n3. Adding Manure and Fertilisers\n4. Irrigation\n5. Protection from Weeds\n6. Harvesting\n7. Storage"
        }
    },
    {
        "type": "flashcard",
        "id": "c8s_ch1_b8_flash",
        "data": {
            "front": "What is the very first step in growing a crop?",
            "back": "The preparation of the soil (turning it and loosening it)."
        }
    },
    {
        "type": "theory",
        "id": "c8s_ch1_b9_tilling",
        "data": {
            "title": "Step 1: Preparation of Soil (Tilling)",
            "content": "Turning and loosening the soil is the most important task in agriculture. This process is called tilling or ploughing. \n\nWhy is this important?\n• It allows the roots to penetrate deep into the soil.\n• Loose soil allows the roots to breathe easily.\n• It helps in the growth of earthworms and friendly microbes."
        }
    },
    {
        "type": "common_mistakes",
        "id": "c8s_ch1_b10_mistake",
        "data": {
            "content": "Don't confuse Manure with Fertiliser!\nManure is a natural organic substance obtained from the decomposition of plant/animal waste. Fertilisers are artificial chemicals produced in factories (like Urea or NPK)."
        }
    },
    {
        "type": "quiz",
        "id": "c8s_ch1_b11_quiz",
        "data": {
            "question": "Which of the following is an example of a Rabi crop?",
            "options": ["Paddy", "Maize", "Cotton", "Wheat"],
            "correct_index": 3
        }
    }
]

# CHAPTER 2: MICROORGANISMS: FRIEND AND FOE
db["gseb_class8_science_ch2"] = [
    {
        "type": "theory",
        "id": "c8s_ch2_b1_hook",
        "data": {
            "title": "The Invisible Empire 🔬",
            "content": "Right now, as you read this, there are billions of tiny creatures living on your skin, in your stomach, and in the air you are breathing. They are too small to be seen with the naked eye. Some of them are your best friends, keeping you alive. Others are deadly foes. Welcome to the invisible empire of Microorganisms!"
        }
    },
    {
        "type": "media",
        "id": "c8s_ch2_b2_media",
        "data": {
            "mediaType": "image",
            "url": "assets/images/invisible_world_ch2.jpg",
            "caption": "Various microscopic bacteria and viruses under high magnification."
        }
    },
    {
        "type": "dictionary_link",
        "id": "c8s_ch2_b3_dict",
        "data": {
            "term_id": "microorganism",
            "preview": "Microorganism: A microscopic organism, especially a bacterium, virus, or fungus."
        }
    },
    {
        "type": "theory",
        "id": "c8s_ch2_b4_types",
        "data": {
            "title": "The 4 Major Groups of Microorganisms 🧫",
            "content": "Microorganisms are broadly classified into four major groups:\n\n1. **Bacteria:** Single-celled organisms. Some cause diseases like typhoid and tuberculosis (TB).\n2. **Fungi:** Look like plants but cannot make their own food. E.g., bread mould, penicillin, and mushrooms.\n3. **Protozoa:** Single-celled animals like Amoeba and Paramecium. They cause diseases like dysentery and malaria.\n4. **Algae:** Simple plant-like organisms. E.g., Chlamydomonas and Spirogyra."
        }
    },
    {
        "type": "teacher_tip",
        "id": "c8s_ch2_b5_tip",
        "data": {
            "content": "Wait! What about Viruses? Viruses are also microscopic, but they are different! They only reproduce inside the cells of a host organism (like a human, plant, or bacterium). Outside a host, they act like non-living particles."
        }
    },
    {
        "type": "flashcard",
        "id": "c8s_ch2_b6_flash",
        "data": {
            "front": "Which microorganism causes Malaria?",
            "back": "Malaria is caused by a Protozoan (specifically, Plasmodium, which is carried by the female Anopheles mosquito)."
        }
    },
    {
        "type": "theory",
        "id": "c8s_ch2_b7_friends",
        "data": {
            "title": "Friendly Microorganisms 🍞",
            "content": "Microorganisms are not all bad! They play a crucial role in our lives and the environment:\n\n• **Making Curd and Bread:** The bacterium Lactobacillus promotes the formation of curd from milk. Yeast reproduces rapidly and produces carbon dioxide, making bread dough rise.\n• **Commercial Use:** Yeast is used for commercial production of alcohol and wine through a process called fermentation.\n• **Medicines:** Antibiotics (like Penicillin) are manufactured by growing specific fungi and bacteria.\n• **Cleaning the Environment:** Bacteria decompose organic waste (like dead plants) into harmless, usable substances."
        }
    },
    {
        "type": "memory_trick",
        "id": "c8s_ch2_b8_memory",
        "data": {
            "content": "Remember the Yeast magic: Yeast + Sugar = Alcohol + Carbon Dioxide. This process is called Fermentation (discovered by Louis Pasteur in 1857)."
        }
    },
    {
        "type": "quiz",
        "id": "c8s_ch2_b9_quiz",
        "data": {
            "question": "Which of the following is NOT a group of microorganisms?",
            "options": ["Bacteria", "Fungi", "Insects", "Protozoa"],
            "correct_index": 2
        }
    }
]

with open(db_path, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print("GSEB Chapters 1 and 2 injected successfully!")
