import json
import os

source_file = "/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/gseb_class8.json"
with open(source_file, 'r') as f:
    gseb_data = json.load(f)

# Create CBSE
cbse_data = dict(gseb_data)
cbse_data["curriculum_id"] = "cbse_class8"
cbse_data["board"] = "CBSE"
with open("/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/cbse_class8.json", "w") as f:
    json.dump(cbse_data, f, indent=2)

# Create NCERT
ncert_data = dict(gseb_data)
ncert_data["curriculum_id"] = "ncert_class8"
ncert_data["board"] = "NCERT"
with open("/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/ncert_class8.json", "w") as f:
    json.dump(ncert_data, f, indent=2)

print("Created cbse_class8.json and ncert_class8.json")
