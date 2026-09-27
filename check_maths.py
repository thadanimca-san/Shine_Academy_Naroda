import json

filepath = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch9.json'
try:
    with open(filepath, 'r') as f:
        data = json.load(f)
    print("Loaded maths chapter 9.")
    blocks = data.get('blocks', [])
    for i, b in enumerate(blocks[:5]):
        print(f"Block {i} question: {b.get('question')}")
        print(f"Block {i} title: {b.get('title')}")
except Exception as e:
    print("Error:", e)
