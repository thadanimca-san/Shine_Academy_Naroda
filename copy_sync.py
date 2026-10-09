import json

with open('app_core/chapters/cbse_class10_math_ch1.json', 'r') as f:
    data = json.load(f)

# Change ID to what GSEB file had
data['metadata']['id'] = "NCERT_MATH_10_CH1_LEARN"

with open('app_core/chapters/gseb_class10_maths_ch1.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Copied and synced to GSEB!")
