import json
import os

chapter_data = {
  "metadata": {
    "id": "SCI_CH10",
    "title": "Gravitation",
    "subtitle": "The Force that Binds the Universe",
    "subject": "Science",
    "grade": 9,
    "board": "GSEB",
    "curriculum": ["GSEB", "CBSE"],
    "language": "English",
    "difficulty": "Intermediate",
    "estimated_minutes": 120,
    "version": "1.0",
    "author": "Antigravity",
    "reviewed_by": "Antigravity",
    "last_updated": "2026-08-07T22:23:34+05:30",
    "tags": ["physics", "gravity", "mass", "weight", "buoyancy"],
    "learning_outcomes": ["Understand the universal law of gravitation", "Distinguish between mass and weight", "Understand free fall", "Explain buoyancy"],
    "ai_context": {
      "learning_goal": "Master the concepts of gravitation, mass vs weight, and buoyancy.",
      "common_misconceptions": ["Mass and weight are the same.", "Heavier objects fall faster.", "There is no gravity in space."],
      "tutor_hint": "If a student says objects fall at different speeds, ask them to imagine dropping a feather and a rock on the moon.",
      "next_topics": ["KOBJ_WORK_ENERGY"]
    }
  },
  "blocks": [
    # Concept 1: Universal Law of Gravitation
    {
      "id": "BLK_GRAV_1_HOOK",
      "type": "real_world_example",
      "difficulty": "Beginner",
      "estimated_minutes": 5,
      "bloom": "Understand",
      "content": {
        "title": "The Cosmic Dance",
        "text": "Have you ever wondered why the moon doesn't just fall into the Earth? Or why the water in the ocean rises and falls every day? The ancient Indians observed these celestial movements and called the attractive force 'Gurutvakarshan'."
      }
    },
    {
      "id": "BLK_GRAV_1_SOCRATIC",
      "type": "ai_tutor_prompt",
      "difficulty": "Beginner",
      "estimated_minutes": 2,
      "bloom": "Analyze",
      "content": {
        "question": "If Earth's gravity is pulling the moon, why doesn't the moon crash into the Earth?"
      }
    },
    {
      "id": "BLK_GRAV_1_DISCOVERY",
      "type": "animated_diagram",
      "difficulty": "Intermediate",
      "estimated_minutes": 8,
      "bloom": "Understand",
      "content": {
        "title": "Orbital Motion",
        "description": "Imagine throwing a ball really fast. It falls, but Earth curves away beneath it. The moon is 'falling' but moving sideways so fast it never hits the ground!",
        "svg": "<svg viewBox=\"0 0 400 300\"><circle cx=\"200\" cy=\"150\" r=\"50\" fill=\"blue\"/><circle cx=\"300\" cy=\"150\" r=\"10\" fill=\"gray\"/><path d=\"M200 150 A100 100 0 1 0 300 150 A100 100 0 1 0 200 150\" stroke=\"white\" fill=\"none\" stroke-dasharray=\"5,5\"/></svg>"
      }
    },
    {
      "id": "BLK_GRAV_1_REVEAL",
      "type": "definition",
      "difficulty": "Intermediate",
      "estimated_minutes": 5,
      "bloom": "Remember",
      "content": {
        "term": "Universal Law of Gravitation",
        "text": "Every object in the universe attracts every other object with a force directed along the line of centers for the two objects that is proportional to the product of their masses and inversely proportional to the square of the separation between the two objects."
      }
    },
    {
      "id": "BLK_GRAV_1_DICT_LINK",
      "type": "dictionary_link",
      "difficulty": "Beginner",
      "estimated_minutes": 1,
      "bloom": "Remember",
      "content": {
        "term_id": "DICT_GRAVITATION",
        "text": "Learn more about Gravitation."
      }
    },
    {
      "id": "BLK_GRAV_1_CHECK",
      "type": "quiz",
      "difficulty": "Intermediate",
      "estimated_minutes": 3,
      "bloom": "Apply",
      "content": {
        "question": "What happens to the gravitational force between two objects if the distance between them is doubled?",
        "options": ["It doubles", "It halves", "It becomes one-fourth", "It becomes four times"],
        "answer": "It becomes one-fourth",
        "distractor_rationale": "Because gravity follows the inverse square law, doubling the distance divides the force by 2^2 (which is 4)."
      }
    },
    {
      "id": "BLK_GRAV_1_REFLECT",
      "type": "reflection",
      "difficulty": "Intermediate",
      "estimated_minutes": 3,
      "bloom": "Evaluate",
      "content": {
        "text": "Explain in your own words how the universal law of gravitation applies to you and your computer screen right now."
      }
    },
    {
      "id": "BLK_GRAV_1_CONNECT",
      "type": "cross_subject_link",
      "difficulty": "Advanced",
      "estimated_minutes": 2,
      "bloom": "Create",
      "content": {
        "title": "Math Connection: Inverse Square Law",
        "text": "The 1/r^2 relationship in gravity is also found in light intensity and electric force! It's a universal pattern of spreading in 3D space."
      }
    },
    {
      "id": "BLK_GRAV_1_MASTERY",
      "type": "challenge_question",
      "difficulty": "Advanced",
      "estimated_minutes": 5,
      "bloom": "Create",
      "content": {
        "question": "If you could change the mass of the Earth, what would you do to keep the moon in its exact same orbit? Show your reasoning."
      }
    },
    
    # Concept 2: Mass vs Weight
    {
      "id": "BLK_MASS_WEIGHT_HOOK",
      "type": "real_world_example",
      "difficulty": "Beginner",
      "estimated_minutes": 2,
      "bloom": "Understand",
      "content": {
        "title": "The Astronaut's Diet",
        "text": "If you want to lose 'weight' instantly without dieting, just go to the moon! You will instantly weigh 6 times less. But will you be any thinner? No!"
      }
    },
    {
      "id": "BLK_MASS_WEIGHT_SOCRATIC",
      "type": "ai_tutor_prompt",
      "difficulty": "Beginner",
      "estimated_minutes": 2,
      "bloom": "Analyze",
      "content": {
        "question": "Why does a weighing machine show a different number on the moon, even though your body is exactly the same?"
      }
    },
    {
      "id": "BLK_MASS_WEIGHT_DISCOVERY",
      "type": "animated_diagram",
      "difficulty": "Intermediate",
      "estimated_minutes": 3,
      "bloom": "Understand",
      "content": {
        "title": "Spring Scale vs Balance",
        "description": "A spring scale measures the pull of gravity (Weight). A balance scale compares amount of matter (Mass). On the moon, the spring scale reading drops, but the balance scale stays balanced!",
        "svg": "<svg viewBox=\"0 0 400 300\"><rect x=\"150\" y=\"200\" width=\"100\" height=\"20\" fill=\"brown\"/><circle cx=\"200\" cy=\"150\" r=\"30\" fill=\"red\"/><text x=\"170\" y=\"155\" fill=\"white\">Mass</text></svg>"
      }
    },
    {
      "id": "BLK_MASS_WEIGHT_REVEAL",
      "type": "definition",
      "difficulty": "Intermediate",
      "estimated_minutes": 3,
      "bloom": "Remember",
      "content": {
        "term": "Mass vs Weight",
        "text": "Mass is the amount of matter in an object (measured in kg) and never changes. Weight is the force of gravity acting on that mass (W = mg) and changes depending on local gravity."
      }
    },
    {
      "id": "BLK_MASS_WEIGHT_DICT_LINK",
      "type": "dictionary_link",
      "difficulty": "Beginner",
      "estimated_minutes": 1,
      "bloom": "Remember",
      "content": {
        "term_id": "DICT_MASS",
        "text": "Learn more about Mass."
      }
    },
    {
      "id": "BLK_MASS_WEIGHT_DICT_LINK_2",
      "type": "dictionary_link",
      "difficulty": "Beginner",
      "estimated_minutes": 1,
      "bloom": "Remember",
      "content": {
        "term_id": "DICT_WEIGHT",
        "text": "Learn more about Weight."
      }
    },
    {
      "id": "BLK_MASS_WEIGHT_CHECK",
      "type": "quiz",
      "difficulty": "Intermediate",
      "estimated_minutes": 3,
      "bloom": "Apply",
      "content": {
        "question": "An object has a mass of 10 kg on Earth. What is its mass on the moon?",
        "options": ["10 kg", "1.67 kg", "60 kg", "0 kg"],
        "answer": "10 kg",
        "distractor_rationale": "Mass is the amount of matter. It does not change with location. Weight changes, but mass remains constant."
      }
    },
    {
      "id": "BLK_MASS_WEIGHT_REFLECT",
      "type": "reflection",
      "difficulty": "Intermediate",
      "estimated_minutes": 3,
      "bloom": "Evaluate",
      "content": {
        "text": "Teach your younger sibling the difference between mass and weight using everyday objects."
      }
    },
    {
      "id": "BLK_MASS_WEIGHT_CONNECT",
      "type": "cross_subject_link",
      "difficulty": "Intermediate",
      "estimated_minutes": 2,
      "bloom": "Understand",
      "content": {
        "title": "Chemistry Connection: Molar Mass",
        "text": "In chemistry, we count atoms using 'moles' and find their 'molar mass'. This is completely independent of gravity!"
      }
    },
    {
      "id": "BLK_MASS_WEIGHT_MASTERY",
      "type": "challenge_question",
      "difficulty": "Advanced",
      "estimated_minutes": 5,
      "bloom": "Create",
      "content": {
        "question": "Design an experiment to measure the mass of an object in a space station where it is weightless."
      }
    },
    
    # Concept 3: Free Fall
    {
      "id": "BLK_FREEFALL_HOOK",
      "type": "real_world_example",
      "difficulty": "Beginner",
      "estimated_minutes": 2,
      "bloom": "Understand",
      "content": {
        "title": "The Galileo Mystery",
        "text": "If you drop a heavy hammer and a light feather, the hammer hits the ground first. But what if you take away the air? Apollo 15 astronaut David Scott actually did this on the moon!"
      }
    },
    {
      "id": "BLK_FREEFALL_SOCRATIC",
      "type": "ai_tutor_prompt",
      "difficulty": "Beginner",
      "estimated_minutes": 2,
      "bloom": "Analyze",
      "content": {
        "question": "Why does a feather fall slower than a rock on Earth, but at the exact same speed on the moon?"
      }
    },
    {
      "id": "BLK_FREEFALL_DISCOVERY",
      "type": "animated_diagram",
      "difficulty": "Intermediate",
      "estimated_minutes": 5,
      "bloom": "Understand",
      "content": {
        "title": "Vacuum Chamber",
        "description": "When air resistance is removed, gravity accelerates all objects equally, regardless of their mass.",
        "svg": "<svg viewBox=\"0 0 400 300\"><rect x=\"100\" y=\"50\" width=\"200\" height=\"200\" fill=\"#222\" stroke=\"gray\" stroke-width=\"4\"/><circle cx=\"150\" cy=\"150\" r=\"15\" fill=\"silver\"/><path d=\"M250 140 Q260 150 250 160 Q240 150 250 140\" fill=\"white\"/></svg>"
      }
    },
    {
      "id": "BLK_FREEFALL_REVEAL",
      "type": "definition",
      "difficulty": "Intermediate",
      "estimated_minutes": 3,
      "bloom": "Remember",
      "content": {
        "term": "Free Fall",
        "text": "When an object falls solely under the influence of gravity, it is said to be in free fall. The acceleration due to gravity (g) is constant for all objects near Earth's surface (~9.8 m/s²)."
      }
    },
    {
      "id": "BLK_FREEFALL_DICT_LINK",
      "type": "dictionary_link",
      "difficulty": "Beginner",
      "estimated_minutes": 1,
      "bloom": "Remember",
      "content": {
        "term_id": "DICT_FREEFALL",
        "text": "Learn more about Free Fall."
      }
    },
    {
      "id": "BLK_FREEFALL_CHECK",
      "type": "quiz",
      "difficulty": "Intermediate",
      "estimated_minutes": 3,
      "bloom": "Apply",
      "content": {
        "question": "In a vacuum, if a 10 kg iron ball and a 0.1 kg feather are dropped from the same height, which hits the ground first?",
        "options": ["Iron ball", "Feather", "Both hit at the same time", "Depends on the height"],
        "answer": "Both hit at the same time",
        "distractor_rationale": "In a vacuum, there is no air resistance. Gravity accelerates all objects equally."
      }
    },
    {
      "id": "BLK_FREEFALL_REFLECT",
      "type": "reflection",
      "difficulty": "Intermediate",
      "estimated_minutes": 3,
      "bloom": "Evaluate",
      "content": {
        "text": "Imagine living in a world with no air resistance. How would sports like badminton or cricket change?"
      }
    },
    {
      "id": "BLK_FREEFALL_CONNECT",
      "type": "cross_subject_link",
      "difficulty": "Intermediate",
      "estimated_minutes": 2,
      "bloom": "Understand",
      "content": {
        "title": "History Connection: Galileo's Tower of Pisa",
        "text": "Galileo Galilei famously demonstrated this principle (or so the legend goes) by dropping two spheres of different masses from the Leaning Tower of Pisa."
      }
    },
    {
      "id": "BLK_FREEFALL_MASTERY",
      "type": "challenge_question",
      "difficulty": "Advanced",
      "estimated_minutes": 5,
      "bloom": "Create",
      "content": {
        "question": "If you throw a ball upwards with a velocity of 19.6 m/s, how long will it take to reach its highest point? (Assume g = 9.8 m/s²)"
      }
    },
    
    # Concept 4: Buoyancy
    {
      "id": "BLK_BUOYANCY_HOOK",
      "type": "real_world_example",
      "difficulty": "Beginner",
      "estimated_minutes": 2,
      "bloom": "Understand",
      "content": {
        "title": "The Floating Iron",
        "text": "A tiny iron nail sinks in water immediately. But a massive ship made of thousands of tons of the same iron floats effortlessly on the ocean! How is that possible?"
      }
    },
    {
      "id": "BLK_BUOYANCY_SOCRATIC",
      "type": "ai_tutor_prompt",
      "difficulty": "Beginner",
      "estimated_minutes": 2,
      "bloom": "Analyze",
      "content": {
        "question": "What is the difference between a solid block of iron and a ship made of iron that allows one to float and the other to sink?"
      }
    },
    {
      "id": "BLK_BUOYANCY_DISCOVERY",
      "type": "animated_diagram",
      "difficulty": "Intermediate",
      "estimated_minutes": 5,
      "bloom": "Understand",
      "content": {
        "title": "Water Displacement",
        "description": "When an object enters a fluid, it pushes fluid out of the way. The fluid pushes back up! This upward push is called Buoyancy.",
        "svg": "<svg viewBox=\"0 0 400 300\"><rect x=\"50\" y=\"150\" width=\"300\" height=\"100\" fill=\"#4ea5d9\"/><path d=\"M100 150 L150 200 L250 200 L300 150 Z\" fill=\"#888\"/><line x1=\"200\" y1=\"200\" x2=\"200\" y2=\"130\" stroke=\"red\" stroke-width=\"4\" marker-end=\"url(#arrow)\"/><text x=\"210\" y=\"140\" fill=\"red\">Buoyant Force</text></svg>"
      }
    },
    {
      "id": "BLK_BUOYANCY_REVEAL",
      "type": "definition",
      "difficulty": "Intermediate",
      "estimated_minutes": 3,
      "bloom": "Remember",
      "content": {
        "term": "Buoyancy (Archimedes' Principle)",
        "text": "When an object is wholly or partially immersed in a fluid, it experiences an upward force (buoyant force) equal to the weight of the fluid displaced by it."
      }
    },
    {
      "id": "BLK_BUOYANCY_DICT_LINK",
      "type": "dictionary_link",
      "difficulty": "Beginner",
      "estimated_minutes": 1,
      "bloom": "Remember",
      "content": {
        "term_id": "DICT_BUOYANCY",
        "text": "Learn more about Buoyancy."
      }
    },
    {
      "id": "BLK_BUOYANCY_CHECK",
      "type": "quiz",
      "difficulty": "Intermediate",
      "estimated_minutes": 3,
      "bloom": "Apply",
      "content": {
        "question": "Why does a hot air balloon rise?",
        "options": ["It has anti-gravity material", "The hot air inside is less dense than the cold air outside", "The wind blows it up", "It is lighter than a feather"],
        "answer": "The hot air inside is less dense than the cold air outside",
        "distractor_rationale": "Because the hot air is less dense, it displaces cooler, heavier air, creating an upward buoyant force greater than its weight."
      }
    },
    {
      "id": "BLK_BUOYANCY_REFLECT",
      "type": "reflection",
      "difficulty": "Intermediate",
      "estimated_minutes": 3,
      "bloom": "Evaluate",
      "content": {
        "text": "Have you ever tried to push an empty plastic bottle underwater? Describe the force you felt pushing back against your hand."
      }
    },
    {
      "id": "BLK_BUOYANCY_CONNECT",
      "type": "cross_subject_link",
      "difficulty": "Intermediate",
      "estimated_minutes": 2,
      "bloom": "Understand",
      "content": {
        "title": "Biology Connection: Swim Bladder in Fishes",
        "text": "Fishes have a special organ called a swim bladder that they fill with gas to control their buoyancy and float at different depths without sinking!"
      }
    },
    {
      "id": "BLK_BUOYANCY_MASTERY",
      "type": "challenge_question",
      "difficulty": "Advanced",
      "estimated_minutes": 5,
      "bloom": "Create",
      "content": {
        "question": "Calculate the volume of water a 10,000-ton ship must displace in order to float."
      }
    }
  ]
}

os.makedirs('/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/gseb_class9_science_ch10/', exist_ok=True)
with open('/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/gseb_class9_science_ch10/blocks.json', 'w') as f:
    json.dump(chapter_data, f, indent=2)

dict_gravitation = {
  "term": {
    "english": "Gravitation",
    "gujarati": "ગુરુત્વાકર્ષણ (Gurutvakarshan)",
    "hindi": "गुरुत्वाकर्षण (Gurutvakarshan)"
  },
  "definition": {
    "simple": "The invisible pull that brings two things together. It's why we stay on Earth and the moon stays in orbit.",
    "academic": "The universal force of attraction acting between all matter."
  },
  "examples": ["An apple falling from a tree.", "The moon orbiting the Earth."],
  "media": {},
  "knowledge_graph_links": {
    "related": ["DICT_MASS", "DICT_WEIGHT"],
    "prerequisites": [],
    "used_in": ["SCI_CH10"]
  },
  "ai_context": {
    "common_misconceptions": ["Gravitation only acts on Earth (False, it acts everywhere in the universe)."],
    "tutor_hint": "Ask the student what would happen to the oceans without the moon's gravity."
  }
}

dict_mass = {
  "term": {
    "english": "Mass",
    "gujarati": "દ્રવ્યમાન (Dravyaman)",
    "hindi": "द्रव्यमान (Dravyaman)"
  },
  "definition": {
    "simple": "The amount of 'stuff' (matter) inside something.",
    "academic": "A quantitative measure of an object's resistance to acceleration; the amount of matter in a body."
  },
  "examples": ["A bowling ball has more mass than a balloon of the same size."],
  "media": {},
  "knowledge_graph_links": {
    "related": ["DICT_WEIGHT", "DICT_GRAVITATION"],
    "prerequisites": [],
    "used_in": ["SCI_CH10"]
  },
  "ai_context": {
    "common_misconceptions": ["Mass is the same as weight."],
    "tutor_hint": "Remind the student that mass doesn't change when you go to the moon."
  }
}

dict_weight = {
  "term": {
    "english": "Weight",
    "gujarati": "વજન (Vajan)",
    "hindi": "वजन (Vajan)"
  },
  "definition": {
    "simple": "How heavily gravity pulls on your mass.",
    "academic": "The force exerted on a body by gravity."
  },
  "examples": ["You weigh less on the moon because the moon's gravity is weaker."],
  "media": {},
  "knowledge_graph_links": {
    "related": ["DICT_MASS", "DICT_GRAVITATION"],
    "prerequisites": ["DICT_MASS"],
    "used_in": ["SCI_CH10"]
  },
  "ai_context": {
    "common_misconceptions": ["Weight is measured in kilograms (It is actually measured in Newtons)."],
    "tutor_hint": "Ask them if a scale measures mass or weight."
  }
}

dict_freefall = {
  "term": {
    "english": "Free Fall",
    "gujarati": "મુક્ત પતન (Mukt Patan)",
    "hindi": "मुक्त पतन (Mukt Patan)"
  },
  "definition": {
    "simple": "Falling with nothing slowing you down but gravity pulling you.",
    "academic": "The state of motion of an object subject only to the influence of gravity."
  },
  "examples": ["An astronaut floating in space is actually in continuous free fall."],
  "media": {},
  "knowledge_graph_links": {
    "related": ["DICT_GRAVITATION"],
    "prerequisites": ["DICT_GRAVITATION"],
    "used_in": ["SCI_CH10"]
  },
  "ai_context": {
    "common_misconceptions": ["Heavy objects fall faster in free fall."],
    "tutor_hint": "Ask them what happens if you remove air resistance."
  }
}

dict_buoyancy = {
  "term": {
    "english": "Buoyancy",
    "gujarati": "ઉત્પ્લાવકતા (Utplavakata)",
    "hindi": "उत्प्लावकता (Utplavakata)"
  },
  "definition": {
    "simple": "The upward push of water or air that helps things float.",
    "academic": "The upward force exerted by a fluid that opposes the weight of an immersed object."
  },
  "examples": ["A ship floating on the ocean.", "A helium balloon floating in the air."],
  "media": {},
  "knowledge_graph_links": {
    "related": ["DICT_WEIGHT", "DICT_GRAVITATION"],
    "prerequisites": [],
    "used_in": ["SCI_CH10"]
  },
  "ai_context": {
    "common_misconceptions": ["Heavy things always sink (False, shape and density matter)."],
    "tutor_hint": "Ask why a giant metal ship floats but a small metal coin sinks."
  }
}

dict_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/knowledge_graph/dictionary'
os.makedirs(dict_dir, exist_ok=True)

with open(os.path.join(dict_dir, 'DICT_GRAVITATION.json'), 'w') as f:
    json.dump(dict_gravitation, f, indent=2)

with open(os.path.join(dict_dir, 'DICT_MASS.json'), 'w') as f:
    json.dump(dict_mass, f, indent=2)

with open(os.path.join(dict_dir, 'DICT_WEIGHT.json'), 'w') as f:
    json.dump(dict_weight, f, indent=2)

with open(os.path.join(dict_dir, 'DICT_FREEFALL.json'), 'w') as f:
    json.dump(dict_freefall, f, indent=2)
    
with open(os.path.join(dict_dir, 'DICT_BUOYANCY.json'), 'w') as f:
    json.dump(dict_buoyancy, f, indent=2)
