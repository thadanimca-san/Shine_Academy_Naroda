import os
import json
import time
import glob
import csv
import google.generativeai as genai

API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-3.5-flash-lite')

CHAPTERS_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"
OUTPUT_CSV = "/home/ubuntu/Shine_Academy_Naroda/science_image_prompts.csv"

def generate_image_prompts(chapter_title, chapter_text):
    prompt = f"""
    You are an expert Educational Illustrator and Prompt Engineer.
    
    Read the following Science chapter content. Identify up to 3 core concepts that would benefit immensely from a visual diagram or illustration (e.g., The structure of a cell, a physics experiment, the water cycle).
    
    For each concept, write a highly detailed, perfect image generation prompt that can be copy-pasted into ChatGPT (DALL-E 3) or Midjourney to generate an educational, hyper-realistic, textbook-quality diagram.
    
    The prompt MUST include styling instructions like "white background, high quality educational diagram, clear labels, vector style, photorealistic".
    
    Chapter Title: {chapter_title}
    
    Chapter Content (excerpt):
    {chapter_text[:5000]}  # Limiting length to save tokens
    
    Expected JSON Output (Return ONLY a valid JSON array):
    [
      {{
        "concept": "The concept name (e.g., Human Heart Anatomy)",
        "prompt": "The detailed ChatGPT image prompt..."
      }}
    ]
    """
    
    while True:
        try:
            response = model.generate_content(prompt)
            res_text = response.text.strip()
            if res_text.startswith("```json"):
                res_text = res_text[7:-3].strip()
            elif res_text.startswith("```"):
                res_text = res_text[3:-3].strip()
                
            data = json.loads(res_text)
            return data
            
        except Exception as e:
            if "429" in str(e) or "Quota" in str(e):
                print("  * Rate limit hit. Waiting 60 seconds...")
                time.sleep(60)
            else:
                print(f"  * JSON parse error: {e}. Retrying in 5s...")
                time.sleep(5)

def main():
    print("--- 🔬 Scanning 922 Science Chapters for Image Opportunities ---")
    
    # Find all JSON files containing 'science' in their name
    science_files = glob.glob(os.path.join(CHAPTERS_DIR, "*science*.json"))
    
    if not science_files:
        print("No Science chapters found.")
        return
        
    print(f"Found {len(science_files)} Science chapters to analyze.\n")
    
    # Check if CSV already exists to resume, otherwise create new with headers
    file_exists = os.path.isfile(OUTPUT_CSV)
    
    processed_files = set()
    if file_exists:
        try:
            with open(OUTPUT_CSV, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if 'Chapter_File' in row:
                        processed_files.add(row['Chapter_File'])
        except Exception:
            pass
            
    with open(OUTPUT_CSV, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Chapter_File', 'Chapter_Title', 'Concept', 'ChatGPT_Prompt']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
            
        for i, filepath in enumerate(sorted(science_files)):
            filename = os.path.basename(filepath)
            
            if filename in processed_files:
                print(f"[{i+1}/{len(science_files)}] Skipping {filename} (already processed)...")
                continue
                
            print(f"[{i+1}/{len(science_files)}] Analyzing {filename}...")
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    chapter_data = json.load(f)
                    
                title = chapter_data.get('metadata', {}).get('title', filename)
                
                # Convert blocks to a single text string for AI analysis
                blocks = chapter_data.get('blocks', [])
                if not blocks:
                    continue
                    
                chapter_text = ""
                for block in blocks:
                    chapter_text += block.get('title', '') + "\n"
                    chapter_text += block.get('body', '') + "\n"
                    
                prompts = generate_image_prompts(title, chapter_text)
                
                for p in prompts:
                    writer.writerow({
                        'Chapter_File': filename,
                        'Chapter_Title': title,
                        'Concept': p.get('concept', ''),
                        'ChatGPT_Prompt': p.get('prompt', '')
                    })
                
                csvfile.flush() # Ensure data is written immediately
                time.sleep(3) # API safety
                
            except Exception as e:
                print(f"  Error processing {filename}: {e}")
                
    print(f"\n✅ All prompts generated! Open '{OUTPUT_CSV}' in Excel to see your ChatGPT prompts.")

if __name__ == "__main__":
    main()
