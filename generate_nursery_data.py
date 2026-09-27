import os
import json
import shutil

BASE_DIR = "app_core/learning_modules"
CURRICULUM_FILE = "app_core/curriculum/nursery.json"

rhymes = [
    ("Twinkle Twinkle", "Twinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky."),
    ("Baa Baa Black Sheep", "Baa, baa, black sheep,\nHave you any wool?\nYes, sir, yes, sir,\nThree bags full."),
    ("Humpty Dumpty", "Humpty Dumpty sat on a wall,\nHumpty Dumpty had a great fall.\nAll the king's horses and all the king's men\nCouldn't put Humpty together again."),
    ("Jack and Jill", "Jack and Jill went up the hill\nTo fetch a pail of water.\nJack fell down and broke his crown,\nAnd Jill came tumbling after."),
    ("Mary Had a Little Lamb", "Mary had a little lamb,\nIts fleece was white as snow;\nAnd everywhere that Mary went\nThe lamb was sure to go."),
    ("Incy Wincy Spider", "Incy wincy spider climbed up the waterspout.\nDown came the rain and washed the spider out.\nOut came the sun and dried up all the rain,\nAnd the incy wincy spider climbed up the spout again."),
    ("Ring-a-Ring o' Roses", "Ring-a-ring o' roses,\nA pocket full of posies,\nA-tishoo! A-tishoo!\nWe all fall down."),
    ("Row, Row, Row Your Boat", "Row, row, row your boat\nGently down the stream,\nMerrily merrily, merrily, merrily,\nLife is but a dream."),
    ("Johny Johny Yes Papa", "Johny, Johny. Yes, Papa?\nEating sugar? No, Papa.\nTelling lies? No, Papa.\nOpen your mouth. Ha-ha-ha!"),
    ("Wheels on the Bus", "The wheels on the bus go round and round,\nRound and round,\nRound and round.\nThe wheels on the bus go round and round,\nAll through the town.")
]

art_shapes = [
    ("Apple", "apple"),
    ("Star", "star"),
    ("Heart", "favorite"), # mapped to Icons.favorite
    ("Sun", "sunny"), # mapped to Icons.sunny
    ("Car", "directions_car") # mapped to Icons.directions_car
]

def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# 1. Generate Rhymes
rhyme_chapters = []
for i, (title, content) in enumerate(rhymes):
    ch_num = i + 1
    mod_id = f"nursery_rhymes_ch{ch_num}"
    mod_dir = os.path.join(BASE_DIR, mod_id)
    make_dir(mod_dir)
    
    meta = {
        "id": mod_id,
        "title": title,
        "subtitle": "Sing along and learn!",
        "subject": "Rhymes & Poems",
        "grade": "Nursery",
        "difficulty": "Beginner",
        "estimated_minutes": 5,
        "learning_outcomes": ["Improve pronunciation", "Develop memory through rhyme"],
        "ai_context": {
            "learning_goal": f"The student should learn the rhyme {title}.",
            "common_misconceptions": [],
            "tutor_hint": "Sing it loudly!"
        }
    }
    with open(os.path.join(mod_dir, "metadata.json"), "w") as f: json.dump(meta, f, indent=2)
        
    blocks = [{
        "type": "nursery_rhyme",
        "title": title,
        "difficulty": "Beginner",
        "bloom": "Remember",
        "estimated_minutes": 5,
        "content": content
    }]
    with open(os.path.join(mod_dir, "blocks.json"), "w") as f: json.dump(blocks, f, indent=2)
        
    rhyme_chapters.append({
        "chapter_number": ch_num,
        "title": title,
        "module_id": mod_id,
        "is_available": True
    })

# 2. Generate Alphabets (A to Z)
alphabet_chapters = []
for i in range(26):
    letter = chr(65 + i)
    ch_num = i + 1
    mod_id = f"nursery_alphabets_ch{ch_num}"
    mod_dir = os.path.join(BASE_DIR, mod_id)
    make_dir(mod_dir)
    
    meta = {
        "id": mod_id,
        "title": f"Tracing Letter {letter}",
        "subtitle": "Learn to write your first letters!",
        "subject": "Alphabets",
        "grade": "Nursery",
        "difficulty": "Beginner",
        "estimated_minutes": 2,
        "learning_outcomes": [f"Identify letter {letter}", "Develop fine motor skills"],
        "ai_context": {
            "learning_goal": f"The student should trace the letter {letter}.",
            "common_misconceptions": [],
            "tutor_hint": "Start at the top!"
        }
    }
    with open(os.path.join(mod_dir, "metadata.json"), "w") as f: json.dump(meta, f, indent=2)
        
    blocks = [{
        "type": "trace_alphabet",
        "letter": letter,
        "difficulty": "Beginner",
        "bloom": "Apply",
        "estimated_minutes": 2
    }]
    with open(os.path.join(mod_dir, "blocks.json"), "w") as f: json.dump(blocks, f, indent=2)
        
    alphabet_chapters.append({
        "chapter_number": ch_num,
        "title": f"Tracing Letter {letter}",
        "module_id": mod_id,
        "is_available": True
    })

# 3. Generate Numbers (1 to 10)
number_chapters = []
for i in range(1, 11):
    ch_num = i
    mod_id = f"nursery_numbers_ch{ch_num}"
    mod_dir = os.path.join(BASE_DIR, mod_id)
    make_dir(mod_dir)
    
    meta = {
        "id": mod_id,
        "title": f"Counting to {ch_num}",
        "subtitle": "Pop the balloons to count!",
        "subject": "Numbers",
        "grade": "Nursery",
        "difficulty": "Beginner",
        "estimated_minutes": 2,
        "learning_outcomes": [f"Count up to {ch_num}", f"Identify number {ch_num} visually"],
        "ai_context": {
            "learning_goal": f"The student should count to {ch_num} by popping balloons.",
            "common_misconceptions": [],
            "tutor_hint": "Pop them one by one!"
        }
    }
    with open(os.path.join(mod_dir, "metadata.json"), "w") as f: json.dump(meta, f, indent=2)
        
    blocks = [{
        "type": "counting_game",
        "target_number": ch_num,
        "item_emoji": "🎈",
        "difficulty": "Beginner",
        "bloom": "Apply",
        "estimated_minutes": 2
    }]
    with open(os.path.join(mod_dir, "blocks.json"), "w") as f: json.dump(blocks, f, indent=2)
        
    number_chapters.append({
        "chapter_number": ch_num,
        "title": f"Counting to {ch_num}",
        "module_id": mod_id,
        "is_available": True
    })

# 4. Generate Art (5 Shapes)
art_chapters = []
for i, (title, shape) in enumerate(art_shapes):
    ch_num = i + 1
    mod_id = f"nursery_art_ch{ch_num}"
    mod_dir = os.path.join(BASE_DIR, mod_id)
    make_dir(mod_dir)
    
    meta = {
        "id": mod_id,
        "title": f"Color the {title}",
        "subtitle": "Fill the shapes with beautiful colors!",
        "subject": "Art & Craft",
        "grade": "Nursery",
        "difficulty": "Beginner",
        "estimated_minutes": 5,
        "learning_outcomes": ["Identify basic colors", "Develop hand-eye coordination"],
        "ai_context": {
            "learning_goal": "The student should select a color and fill the shape.",
            "common_misconceptions": [],
            "tutor_hint": f"What color is a {title}?"
        }
    }
    with open(os.path.join(mod_dir, "metadata.json"), "w") as f: json.dump(meta, f, indent=2)
        
    blocks = [{
        "type": "color_canvas",
        "shape": shape,
        "difficulty": "Beginner",
        "bloom": "Apply",
        "estimated_minutes": 5
    }]
    with open(os.path.join(mod_dir, "blocks.json"), "w") as f: json.dump(blocks, f, indent=2)
        
    art_chapters.append({
        "chapter_number": ch_num,
        "title": f"Color the {title}",
        "module_id": mod_id,
        "is_available": True
    })

# Update nursery.json
with open(CURRICULUM_FILE, "r") as f:
    nursery = json.load(f)

for subject in nursery["subjects"]:
    if subject["id"] == "rhymes":
        subject["chapters"] = rhyme_chapters
    elif subject["id"] == "alphabets":
        subject["chapters"] = alphabet_chapters
    elif subject["id"] == "numbers":
        subject["chapters"] = number_chapters
    elif subject["id"] == "art":
        subject["chapters"] = art_chapters

with open(CURRICULUM_FILE, "w") as f:
    json.dump(nursery, f, indent=2)

print("Successfully generated rich Nursery data!")
