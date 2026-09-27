import json
with open('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch1.json') as f:
    data = json.load(f)
print("Blocks:", len(data.get('blocks', [])))
