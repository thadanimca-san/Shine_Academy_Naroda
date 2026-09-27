import json

filepath = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch9.json'
with open(filepath, 'r') as f:
    data = json.load(f)

blocks = data.get('blocks', [])
for i, b in enumerate(blocks):
    if b.get('title') is None:
        print(f"Block {i} missing title! Keys: {list(b.keys())}")
    if b.get('id') is None or b.get('id') == "UNKNOWN_ID":
        print(f"Block {i} missing ID! Keys: {list(b.keys())}")
