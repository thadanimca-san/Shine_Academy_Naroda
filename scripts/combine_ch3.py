import json
import os

chapter_id = "gseb_class10_maths_ch3"
module_dir = f"app_core/learning_modules/{chapter_id}"
output_file = f"app_core/chapters/{chapter_id}.json"

with open(f"{module_dir}/metadata.json", "r", encoding="utf-8") as f:
    metadata = json.load(f)

with open(f"{module_dir}/blocks.json", "r", encoding="utf-8") as f:
    blocks = json.load(f)

final_json = {
    "metadata": metadata,
    "blocks": blocks
}

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(final_json, f, ensure_ascii=False, indent=2)

print(f"Created {output_file}")
