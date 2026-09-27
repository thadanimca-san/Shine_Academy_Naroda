import json
with open('/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/class6.json') as f:
    data = json.load(f)
    for s in data['subjects']:
        if s['name'] == 'Science':
            for c in s.get('chapters', []):
                print(c)
