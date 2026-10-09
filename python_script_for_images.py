import csv
import os
import time
import urllib.parse
import re
import requests

# ---------------------------------------------------------
# SETUP & CONFIGURATION
# ---------------------------------------------------------
INPUT_CSV = "science_image_prompts.csv"
CLEANED_CSV = "cleaned_science_image_prompts.csv"
OUTPUT_DIR = "generated_images"

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>| ]+', '_', filename)

# ---------------------------------------------------------
# 1. CLEAN CSV & EXTRACT PROMPTS
# ---------------------------------------------------------
print(f"--> CSV Processing start: '{INPUT_CSV}'...")

prompts_list = []

if not os.path.exists(INPUT_CSV):
    print(f"[ERROR] File '{INPUT_CSV}' nahi mili.")
    exit(1)

with open(INPUT_CSV, mode="r", encoding="utf-8-sig") as infile:
    reader = csv.reader(infile)
    
    with open(CLEANED_CSV, mode="w", encoding="utf-8", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Column_1_Fix", "Extracted_Prompt"])
        
        for row in reader:
            if not row or len(row) < 2:
                continue
            
            col1 = row[0].strip()
            remaining_cols = row[1:]
            longest_prompt = max(remaining_cols, key=lambda x: len(x.strip())).strip()
            
            writer.writerow([col1, longest_prompt])
            prompts_list.append((col1, longest_prompt))

print(f"--> CSV Cleaned! Total Prompts found: {len(prompts_list)}\n")

# ---------------------------------------------------------
# 2. HIGH DEFINITION SHARP GENERATION ENGINE
# ---------------------------------------------------------
os.makedirs(OUTPUT_DIR, exist_ok=True)
print(f"--> HD Sharp Diagram Generation Started ({len(prompts_list)} Prompts)...")

# High Quality HF / SD URL Engine
def get_hd_image(prompt, seed):
    # High resolution parameters to force crisp, clean vectors
    clean_p = f"ultra sharp, high resolution, detailed vector illustration, educational textbook diagram, pure white background, vibrant colors, sharp lines, 8k resolution, no blur: {prompt}"
    encoded = urllib.parse.quote(clean_p)
    
    # Using specialized model endpoint for high clarity
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=1280&height=1280&model=flux-realism&nologo=true&seed={seed}&enhance=true"
    
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers, timeout=60)
    return res

for idx, (fix_val, raw_prompt) in enumerate(prompts_list, start=1):
    safe_col1 = sanitize_filename(fix_val)
    image_name = f"{safe_col1}_{idx:04d}.png"
    image_path = os.path.join(OUTPUT_DIR, image_name)
    
    # Resume check
    if os.path.exists(image_path) and os.path.getsize(image_path) > 50000:
        print(f"[{idx}/{len(prompts_list)}] Skip: '{image_name}' pehle se high quality ban chuka hai.")
        continue
    
    print(f"[{idx}/{len(prompts_list)}] Generating Sharp HD Diagram for [{safe_col1}]...")
    
    success = False
    for attempt in range(1, 4):
        try:
            response = get_hd_image(raw_prompt, idx)
            
            # File size filter: 50KB se badi file matlab high quality image hai
            if response.status_code == 200 and len(response.content) > 50000:
                with open(image_path, "wb") as f:
                    f.write(response.content)
                print(f"   [SUCCESS] Saved HD Image as '{image_name}' ({round(len(response.content)/1024, 1)} KB)")
                success = True
                break
            else:
                print(f"   [RETRY] Attempt {attempt} - Low quality or server busy (Size: {len(response.content) if response else 0} bytes)")
                time.sleep(3)

        except Exception as e:
            print(f"   [ERROR] Attempt {attempt} failed: {e}")
            time.sleep(3)

    if not success:
        print(f"   [SKIP] Could not generate index {idx}")

    time.sleep(1)

print("\n--> Process complete!")
