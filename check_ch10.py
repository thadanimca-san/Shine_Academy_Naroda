import json
import os

filepath = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch10.json'
if os.path.exists(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    print("Title:", data.get('metadata', {}).get('title'))
    blocks = data.get('blocks', [])
    print(f"Total blocks in Chapter 10: {len(blocks)}")
    
    print("\n--- Top 10 blocks ---")
    for i in range(min(10, len(blocks))):
        b = blocks[i]
        title = b.get('title') or b.get('question')
        print(f"Block {i}: {title[:70] if title else 'No Title'} (Type: {b.get('type')})")
        
    print("\n--- Last 10 blocks ---")
    for i in range(max(0, len(blocks)-10), len(blocks)):
        b = blocks[i]
        title = b.get('title') or b.get('question')
        print(f"Block {i}: {title[:70] if title else 'No Title'} (Type: {b.get('type')})")
else:
    print(f"{filepath} does NOT exist.")
