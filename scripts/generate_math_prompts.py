import json
import os
import csv
import re

CHAPTERS_DIR = "app_core/chapters"
OUTPUT_CSV = "ncert_math_prompts.csv"

def process_chapters():
    prompts = []
    
    files_to_process = []
    for filename in os.listdir(CHAPTERS_DIR):
        if filename.startswith("ncert_class10_maths_") and filename.endswith(".json"):
            files_to_process.append(("maths", filename))
                
    files_to_process.sort()
    
    for subject, filename in files_to_process:
        filepath = os.path.join(CHAPTERS_DIR, filename)
        
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            continue
            
        blocks = data if isinstance(data, list) else data.get("blocks", [])
        
        concepts_chosen = 0
        
        for block in blocks:
            if block.get("type") in ["theory", "definition", "example"]:
                title = block.get("title", "")
                if not title:
                    continue
                    
                if len(title.split()) < 2:
                    continue
                    
                title_clean = title.replace("\n", " ").strip()
                
                prompt = f"An educational, high-quality textbook diagram or infographic about '{title_clean}' in Mathematics. Clean white background, precise geometric or visual structure, clear labels, professional and highly informative."
                
                prompts.append([filename, "Maths", title_clean, prompt])
                concepts_chosen += 1
                
                if concepts_chosen >= 4:
                    break
                    
    with open(OUTPUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for row in prompts:
            writer.writerow(row)
            
    print(f"Generated {len(prompts)} prompts across {len(files_to_process)} chapters. Saved to {OUTPUT_CSV}")

if __name__ == "__main__":
    process_chapters()
