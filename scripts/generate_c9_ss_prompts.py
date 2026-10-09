import json
import os
import csv
import re

CHAPTERS_DIR = "app_core/chapters"
OUTPUT_CSV = "ncert_class9_social_science_prompts.csv"

def process_chapters():
    prompts = []
    
    files_to_process = []
    for filename in os.listdir(CHAPTERS_DIR):
        if filename.startswith("ncert_class9_social_science_") and filename.endswith(".json"):
            files_to_process.append(("social_science", filename))
                
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
            if block.get("type") in ["theory", "definition", "history", "mind_map"]:
                title = block.get("title", "")
                content = block.get("content", "")
                
                if not title and not content:
                    continue
                    
                if not title:
                    if block.get("type") == "definition":
                        match = re.search(r'\*\*(.*?)\*\*', content)
                        if match:
                            title = match.group(1).strip()
                    elif block.get("type") in ["mind_map", "timeline"]:
                        title = content.split('\n')[0].strip(':* ')
                    else:
                        title = " ".join(content.split()[:7]) + "..."
                        
                if not title or len(title.split()) < 2:
                    if block.get("type") != "definition":
                        continue
                    
                title_clean = title.replace("\n", " ").replace("*", "").strip()
                
                prompt = f"An educational, high-quality textbook diagram or infographic about '{title_clean}' in Class 9 Social Science. Clean white background, precise historical or geographical visual structure, clear labels, professional and highly informative."
                
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
