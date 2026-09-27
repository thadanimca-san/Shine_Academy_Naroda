import json
import glob

def fix_json(filepath, route):
    with open(filepath, 'r') as f:
        data = json.load(f)
        
    for sub in data.get('subjects', []):
        if sub['id'] == 'english':
            sub['app_route'] = route
            
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

for i in range(3, 7):
    fix_json(f'app_core/curriculum/class{i}.json', '/learning/eng3to6')

for i in range(7, 11):
    fix_json(f'app_core/curriculum/gseb_class{i}.json', '/learning/english_sim')

print("Routes injected successfully!")
