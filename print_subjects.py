import json, glob
for file in glob.glob('/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/class[1-6].json'):
    with open(file) as f:
        data = json.load(f)
        subjects = [s['name'] for s in data.get('subjects', [])]
        print(f"{file.split('/')[-1]}: {subjects}")
