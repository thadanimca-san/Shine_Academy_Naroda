import json
import os
import glob

chapters_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

for i in range(1, 16):
    ncert_file = os.path.join(chapters_dir, f"ncert_class10_science_ch{i}.json")
    gseb_file = os.path.join(chapters_dir, f"gseb_class10_science_ch{i}.json")
    
    if os.path.exists(ncert_file):
        with open(ncert_file, "r") as f:
            data = json.load(f)
            
        data["metadata"]["id"] = f"gseb_class10_science_ch{i}"
        
        with open(gseb_file, "w") as f:
            json.dump(data, f, indent=2)
            
print("Copied NCERT Class 10 Science to GSEB Class 10 Science.")
