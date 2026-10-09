import json
import os

with open("app_core/learning_modules/master_curriculum.json", "r") as f:
    curriculum = json.load(f)

print("Checking CBSE Class 10 English:")
for key, value in curriculum.items():
    if "class10" in key and "english" in key and "cbse" in key:
        print(f"Curriculum Key: {key}")

print("\nChecking GSEB Class 10 English:")
for key, value in curriculum.items():
    if "class10" in key and "english" in key and "gseb" in key:
        print(f"Curriculum Key: {key}")

print("\nChecking Grammar (Govind Sir):")
count = 0
for key, value in curriculum.items():
    if "govindsir" in key and "english" in key:
        count += 1
print(f"Total Grammar Chapters: {count}")

print("\nChecking JSON files in app_core/chapters/:")
files = os.listdir("app_core/chapters/")
cbse = [f for f in files if "cbse_class10_english" in f]
gseb = [f for f in files if "gseb_class10_english" in f]
govindsir = [f for f in files if "govindsir_english" in f]
print(f"CBSE Class 10 English JSON files: {len(cbse)}")
print(f"GSEB Class 10 English JSON files: {len(gseb)}")
print(f"Govind Sir English JSON files: {len(govindsir)}")

