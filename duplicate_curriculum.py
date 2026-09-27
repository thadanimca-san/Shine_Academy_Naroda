import json
import os

source_file = "/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/gseb_class9.json"
with open(source_file, 'r') as f:
    gseb_data = json.load(f)

# Create CBSE
cbse_data = dict(gseb_data)
cbse_data["curriculum_id"] = "cbse_class9"
cbse_data["board"] = "CBSE"

cbse_file = "/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/cbse_class9.json"
with open(cbse_file, 'w') as f:
    json.dump(cbse_data, f, indent=2)

# Create NCERT
ncert_data = dict(gseb_data)
ncert_data["curriculum_id"] = "ncert_class9"
ncert_data["board"] = "NCERT"

ncert_file = "/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/ncert_class9.json"
with open(ncert_file, 'w') as f:
    json.dump(ncert_data, f, indent=2)

print("Created CBSE and NCERT Class 9 curriculums successfully.")
