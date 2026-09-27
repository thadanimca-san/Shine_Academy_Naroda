import json

filepath = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch9.json'
with open(filepath, 'r') as f:
    data = json.load(f)

blocks = data.get('blocks', [])
for i in range(8, 17):
    if i < len(blocks):
        b = blocks[i]
        print(f"\n--- Block {i}: {b.get('title')} ---")
        print("Question:", b.get('question'))
        print("Options:", b.get('options'))
        print("Hindi Q:", b.get('question_hi'))
        print("Gujarati Q:", b.get('question_gu'))
