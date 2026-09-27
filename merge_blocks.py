import json
import os

base_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/gseb_class8_science_ch1"
merged_blocks = []

for i in range(1, 9):
    file_path = os.path.join(base_dir, f"blocks_{i}.json")
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            try:
                blocks = json.load(f)
                if isinstance(blocks, list):
                    merged_blocks.extend(blocks)
                else:
                    print(f"Warning: {file_path} does not contain a JSON array.")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    else:
        print(f"Warning: {file_path} not found.")

master_file = os.path.join(base_dir, "blocks.json")
with open(master_file, 'w') as f:
    json.dump(merged_blocks, f, indent=2)

print(f"Successfully merged {len(merged_blocks)} blocks into blocks.json!")

# Clean up the intermediate files
for i in range(1, 9):
    file_path = os.path.join(base_dir, f"blocks_{i}.json")
    if os.path.exists(file_path):
        os.remove(file_path)
