import json

with open("app_core/learning_modules/master_curriculum.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

for mod_id, mod_data in data.items():
    json_str = json.dumps(mod_data)
    if "What is the most important aspect of Chapter 10: New Empires and Kingdoms" in json_str:
        print(f"FOUND IN: {mod_id}")

