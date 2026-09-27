import json

gp_chapters = [
    {"id": "cbse_class6_maths_gp_ch1", "title": "Chapter 1: Patterns in Mathematics"},
    {"id": "cbse_class6_maths_gp_ch2", "title": "Chapter 2: Lines and Angles"},
    {"id": "cbse_class6_maths_gp_ch3", "title": "Chapter 3: Number Play"},
    {"id": "cbse_class6_maths_gp_ch4", "title": "Chapter 4: Data Handling and Presentation"},
    {"id": "cbse_class6_maths_gp_ch5", "title": "Chapter 5: Prime Time"},
    {"id": "cbse_class6_maths_gp_ch6", "title": "Chapter 6: Perimeter and Area"},
    {"id": "cbse_class6_maths_gp_ch7", "title": "Chapter 7: Fractions"},
    {"id": "cbse_class6_maths_gp_ch8", "title": "Chapter 8: Playing with Constructions"},
    {"id": "cbse_class6_maths_gp_ch9", "title": "Chapter 9: Symmetry"},
    {"id": "cbse_class6_maths_gp_ch10", "title": "Chapter 10: The Other Side of Zero"}
]

with open('app_core/learning_modules/master_curriculum.json', 'r') as f:
    data = json.load(f)

for chap in gp_chapters:
    data[chap['id']] = {
        "metadata": {
            "id": chap['id'],
            "title": chap['title'],
            "subject": "Maths",
            "difficulty": "Beginner",
            "estimated_minutes": 30
        },
        "blocks": [
            {
                "type": "theory",
                "id": chap['id'] + "_theory",
                "title": "Welcome",
                "body": "Welcome to " + chap['title'] + " from the new Ganita Prakash textbook!"
            }
        ]
    }

with open('app_core/learning_modules/master_curriculum.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Added Ganita Prakash chapters to master_curriculum.json")
