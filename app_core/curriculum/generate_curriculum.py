import json
import os

curriculum_dir = "."

classes = [
    {'title': 'Nursery', 'id': 'nursery', 'type': 'preschool'},
    {'title': 'LKG', 'id': 'lkg', 'type': 'preschool'},
    {'title': 'UKG', 'id': 'ukg', 'type': 'preschool'},
    {'title': 'Class 1', 'id': 'class1', 'type': 'primary'},
    {'title': 'Class 2', 'id': 'class2', 'type': 'primary'},
    {'title': 'Class 3', 'id': 'class3', 'type': 'primary'},
    {'title': 'Class 4', 'id': 'class4', 'type': 'primary'},
    {'title': 'Class 5', 'id': 'class5', 'type': 'primary'},
    {'title': 'Class 6', 'id': 'class6', 'type': 'middle'},
    {'title': 'Class 7', 'id': 'gseb_class7', 'type': 'middle'},
    {'title': 'Class 8', 'id': 'gseb_class8', 'type': 'middle'},
    {'title': 'Class 10', 'id': 'gseb_class10', 'type': 'secondary'},
    {'title': 'Class 11 Science', 'id': 'class11_science', 'type': 'science'},
    {'title': 'Class 11 Commerce', 'id': 'class11_commerce', 'type': 'commerce'},
    {'title': 'Class 11 Arts', 'id': 'class11_arts', 'type': 'arts'},
    {'title': 'Class 12 Science', 'id': 'class12_science', 'type': 'science'},
    {'title': 'Class 12 Arts', 'id': 'class12_arts', 'type': 'arts'},
    {'title': 'NEET', 'id': 'neet', 'type': 'medical'},
    {'title': 'JEE', 'id': 'jee', 'type': 'engineering'},
    {'title': 'UPSC', 'id': 'upsc', 'type': 'civil_services'},
    {'title': 'CA Foundation', 'id': 'ca_foundation', 'type': 'ca'},
    {'title': 'CS Executive', 'id': 'cs_executive', 'type': 'cs'},
]

templates = {
    'preschool': [
        {"id": "rhymes", "name": "Rhymes & Poems", "color_hex": "0xFFE91E63", "icon": "book"},
        {"id": "alphabets", "name": "Alphabets", "color_hex": "0xFF2196F3", "icon": "language"},
        {"id": "numbers", "name": "Numbers", "color_hex": "0xFFFF9800", "icon": "calculate"},
        {"id": "art", "name": "Art & Craft", "color_hex": "0xFF9C27B0", "icon": "book"}
    ],
    'primary': [
        {"id": "maths", "name": "Mathematics", "color_hex": "0xFFE91E63", "icon": "calculate"},
        {"id": "english", "name": "English", "color_hex": "0xFF2196F3", "icon": "language"},
        {"id": "evs", "name": "EVS", "color_hex": "0xFF4CAF50", "icon": "science"},
        {"id": "hindi", "name": "Hindi", "color_hex": "0xFFFF9800", "icon": "language"}
    ],
    'middle': [
        {"id": "maths", "name": "Mathematics", "color_hex": "0xFFE91E63", "icon": "calculate"},
        {"id": "science", "name": "Science", "color_hex": "0xFF2196F3", "icon": "science"},
        {"id": "social", "name": "Social Science", "color_hex": "0xFF9C27B0", "icon": "book"},
        {"id": "english", "name": "English", "color_hex": "0xFF4CAF50", "icon": "language"}
    ],
    'secondary': [
        {"id": "maths", "name": "Mathematics", "color_hex": "0xFFE91E63", "icon": "calculate"},
        {"id": "science", "name": "Science", "color_hex": "0xFF2196F3", "icon": "science"},
        {"id": "social", "name": "Social Science", "color_hex": "0xFF9C27B0", "icon": "book"},
        {"id": "english", "name": "English", "color_hex": "0xFF4CAF50", "icon": "language"}
    ],
    'science': [
        {"id": "physics", "name": "Physics", "color_hex": "0xFF2196F3", "icon": "science"},
        {"id": "chemistry", "name": "Chemistry", "color_hex": "0xFF9C27B0", "icon": "biotech"},
        {"id": "biology", "name": "Biology", "color_hex": "0xFF4CAF50", "icon": "biotech"},
        {"id": "maths", "name": "Mathematics", "color_hex": "0xFFE91E63", "icon": "calculate"}
    ],
    'commerce': [
        {"id": "accounts", "name": "Accountancy", "color_hex": "0xFF4CAF50", "icon": "account_balance"},
        {"id": "business", "name": "Business Studies", "color_hex": "0xFF2196F3", "icon": "book"},
        {"id": "economics", "name": "Economics", "color_hex": "0xFF9C27B0", "icon": "bar_chart"},
        {"id": "english", "name": "English", "color_hex": "0xFFFF9800", "icon": "language"}
    ],
    'arts': [
        {"id": "history", "name": "History", "color_hex": "0xFF795548", "icon": "book"},
        {"id": "geography", "name": "Geography", "color_hex": "0xFF4CAF50", "icon": "language"},
        {"id": "political", "name": "Political Science", "color_hex": "0xFF2196F3", "icon": "account_balance"},
        {"id": "english", "name": "English", "color_hex": "0xFFFF9800", "icon": "language"}
    ],
    'medical': [
        {"id": "physics", "name": "Physics", "color_hex": "0xFF2196F3", "icon": "science"},
        {"id": "chemistry", "name": "Chemistry", "color_hex": "0xFF9C27B0", "icon": "biotech"},
        {"id": "botany", "name": "Botany", "color_hex": "0xFF4CAF50", "icon": "biotech"},
        {"id": "zoology", "name": "Zoology", "color_hex": "0xFFE91E63", "icon": "biotech"}
    ],
    'engineering': [
        {"id": "physics", "name": "Physics", "color_hex": "0xFF2196F3", "icon": "science"},
        {"id": "chemistry", "name": "Chemistry", "color_hex": "0xFF9C27B0", "icon": "biotech"},
        {"id": "maths", "name": "Mathematics", "color_hex": "0xFFE91E63", "icon": "calculate"}
    ],
    'civil_services': [
        {"id": "history", "name": "History of India", "color_hex": "0xFF795548", "icon": "book"},
        {"id": "geography", "name": "Geography", "color_hex": "0xFF4CAF50", "icon": "language"},
        {"id": "polity", "name": "Indian Polity", "color_hex": "0xFF2196F3", "icon": "account_balance"},
        {"id": "economy", "name": "Economy", "color_hex": "0xFF9C27B0", "icon": "bar_chart"}
    ],
    'ca': [
        {"id": "accounting", "name": "Principles of Accounting", "color_hex": "0xFF4CAF50", "icon": "account_balance"},
        {"id": "law", "name": "Business Laws", "color_hex": "0xFF795548", "icon": "book"},
        {"id": "maths", "name": "Business Maths", "color_hex": "0xFFE91E63", "icon": "calculate"},
        {"id": "economics", "name": "Business Economics", "color_hex": "0xFF9C27B0", "icon": "bar_chart"}
    ],
    'cs': [
        {"id": "jurisprudence", "name": "Jurisprudence", "color_hex": "0xFF795548", "icon": "book"},
        {"id": "company_law", "name": "Company Law", "color_hex": "0xFF2196F3", "icon": "account_balance"},
        {"id": "tax", "name": "Tax Laws", "color_hex": "0xFF4CAF50", "icon": "calculate"},
        {"id": "corporate_accounting", "name": "Corporate Accounting", "color_hex": "0xFF9C27B0", "icon": "bar_chart"}
    ]
}

for c in classes:
    filepath = os.path.join(curriculum_dir, f"{c['id']}.json")
    if os.path.exists(filepath):
        continue  # Don't overwrite existing files like gseb_class9.json
    
    data = {
        "curriculum_id": c['id'],
        "curriculum_name": c['title'],
        "description": f"Curriculum for {c['title']}",
        "subjects": templates[c['type']]
    }
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    
    print(f"Generated {filepath}")

print("All framework files generated successfully!")
