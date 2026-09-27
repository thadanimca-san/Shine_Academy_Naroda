import os
import shutil

base_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules"

# The mappings from my generated folders to the correct rationalized folders
mappings = [
    ("gseb_class9_science_ch8", "gseb_class9_science_ch7"),   # Motion
    ("gseb_class9_science_ch9", "gseb_class9_science_ch8"),   # Force
    ("gseb_class9_science_ch10", "gseb_class9_science_ch9"),  # Gravitation
    ("gseb_class9_science_ch11", "gseb_class9_science_ch10"), # Work
    ("gseb_class9_science_ch12", "gseb_class9_science_ch11"), # Sound
    ("gseb_class9_science_ch15", "gseb_class9_science_ch12")  # Food
]

# We must move them to temporary files first to avoid overwriting issues
temp_files = []
for src, dest in mappings:
    src_file = os.path.join(base_dir, src, "blocks.json")
    temp_file = os.path.join(base_dir, dest, "blocks_temp.json")
    
    if os.path.exists(src_file):
        shutil.copy(src_file, temp_file)
        temp_files.append((temp_file, os.path.join(base_dir, dest, "blocks.json")))

# Now overwrite the correct destinations
for temp_file, dest_file in temp_files:
    shutil.move(temp_file, dest_file)
    print(f"Moved to {dest_file}")

# Clean up the unused/invalid directories I created
for ch in [13, 14, 15]:
    bad_dir = os.path.join(base_dir, f"gseb_class9_science_ch{ch}")
    if os.path.exists(bad_dir):
        shutil.rmtree(bad_dir)
        print(f"Removed unused directory {bad_dir}")

