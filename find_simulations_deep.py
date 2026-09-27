import os
import json

def find_simulations_in_obj(obj, filepath):
    results = []
    if isinstance(obj, dict):
        if obj.get('type') in ['simulation', 'animated_diagram']:
            results.append((filepath, obj.get('type'), obj.get('title', ''), obj.get('body', '')[:50]))
        for v in obj.values():
            results.extend(find_simulations_in_obj(v, filepath))
    elif isinstance(obj, list):
        for item in obj:
            results.extend(find_simulations_in_obj(item, filepath))
    return results

def search_json(directory):
    all_res = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r') as f:
                        data = json.load(f)
                    res = find_simulations_in_obj(data, filepath)
                    if res:
                        all_res.extend(res)
                except Exception:
                    pass
    return all_res

res = search_json('app_core')
for r in res:
    print(f"File: {r[0]} | Type: {r[1]} | Title: {r[2]} | Body: {r[3]}")
