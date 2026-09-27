import json
import os

print("Class 10 Maths Completion Status:")
print("-" * 50)

for i in range(1, 15):
    learn_file = f"app_core/chapters/gseb_class10_maths_ch{i}.json"
    test_file = f"app_core/assessment/gseb_class10_maths_ch{i}_questions.json"
    
    learn_blocks = 0
    test_blocks = 0
    title = f"Chapter {i}"
    
    if os.path.exists(learn_file):
        with open(learn_file, 'r') as f:
            data = json.load(f)
            if isinstance(data, dict):
                title = data.get("metadata", {}).get("title", f"Chapter {i}")
                learn_blocks = len(data.get("blocks", []))
            elif isinstance(data, list):
                learn_blocks = len(data)
                print(f"WARNING: {learn_file} is a list!")
            
    if os.path.exists(test_file):
        with open(test_file, 'r') as f:
            data = json.load(f)
            if isinstance(data, dict):
                test_blocks = len(data.get("blocks", []))
            elif isinstance(data, list):
                test_blocks = len(data)
                print(f"WARNING: {test_file} is a list!")
            
    print(f"Ch {i:2d}: {title[:35]:35} | Learn Blocks: {learn_blocks:3d} | Test Blocks: {test_blocks:3d}")

