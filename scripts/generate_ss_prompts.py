import json
import os
import csv
import re

CHAPTERS_DIR = "app_core/chapters"
OUTPUT_CSV = "ncert_social_science_prompts.csv"

# Keywords that suggest a visual concept
VISUAL_KEYWORDS = ["map", "diagram", "process", "cycle", "system", "structure", "comparison", "types", "architecture", "war", "movement", "industry", "agriculture", "resource", "soil"]

def process_chapters():
    prompts = []
    
    files_to_process = []
    for subject in ["history", "geography", "civics", "economics"]:
        for filename in os.listdir(CHAPTERS_DIR):
            if filename.startswith(f"ncert_class10_{subject}") and filename.endswith(".json"):
                files_to_process.append((subject, filename))
                
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
        
        # We want to pick 3-4 good concepts per chapter
        concepts_chosen = 0
        
        for block in blocks:
            if block.get("type") in ["theory", "definition", "example"]:
                title = block.get("title", "")
                if not title:
                    continue
                    
                # Skip trivial titles
                if len(title.split()) < 2:
                    continue
                    
                title_clean = title.replace("\n", " ").strip()
                
                # Generate a prompt
                prompt = f"An educational, high-quality textbook illustration or infographic about '{title_clean}' in the context of Class 10 {subject.capitalize()}. Clean white background, clear visual structure, photorealistic details combined with vector graphics, professional and highly informative."
                
                prompts.append([filename, "Social Science", title_clean, prompt])
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
