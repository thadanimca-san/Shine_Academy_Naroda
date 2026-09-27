import os
import json
import time
import google.generativeai as genai

API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-3.5-flash-lite')

OUTPUT_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

CURRICULUM = [
    {"ch_num": 1, "title": "Introduction to the Abacus", "topics": ["The Frame, Beam, and Rods", "Earth Beads and Heaven Beads", "Clearing the Abacus"]},
    {"ch_num": 2, "title": "Counting 1 to 9", "topics": ["Using the Thumb for Earth Beads", "Using the Index Finger for Heaven Beads", "Reading the Value on the Abacus"]},
    {"ch_num": 3, "title": "Simple Addition (No Carry)", "topics": ["Adding 1, 2, 3, 4", "Adding 5", "Adding mixed Earth and Heaven beads (e.g., 5+2)"]},
    {"ch_num": 4, "title": "Simple Subtraction", "topics": ["Subtracting Earth Beads", "Subtracting Heaven Beads", "Mixed Simple Subtraction"]},
    {"ch_num": 5, "title": "Big Friends Concept (+9 to +6)", "topics": ["What are Big Friends? (Base 10)", "Adding 9 (Add 10, Less 1)", "Adding 8 (Add 10, Less 2)"]},
]

SYSTEM_PROMPT = """
You are a master Abacus (Soroban) Teacher for Shine Academy.
Generate a JSON output for the requested chapter.
You MUST STRICTLY follow the CHAPTER_STANDARD.yaml.
You MUST output exactly ONE valid JSON object, starting with { and ending with }. No markdown fences.

CRITICAL RULES:
1. Every block MUST have fields at the ROOT level. DO NOT wrap data in a "content": {} object.
2. Every string MUST be translated into Hindi and Gujarati (e.g., body, body_hi, body_gu).
3. We have a NEW block type called "abacus_simulation". When you want the student to physically practice counting or adding on the abacus, output this block:
   {"id": "CH_ABACUS_SIM_1", "type": "abacus_simulation"}
   This will render an interactive digital abacus on their screen! You should output this block right after teaching a concept so they can try it.
4. Follow the 8-Step Socratic Gold Pedagogy (Hook -> Socratic Question -> Discovery -> Reveal -> Knowledge Check -> Mastery).
"""

def generate_chapter(ch_data):
    ch_num = ch_data["ch_num"]
    title = ch_data["title"]
    topics = ", ".join(ch_data["topics"])
    
    filepath = os.path.join(OUTPUT_DIR, f"abacus_level1_ch{ch_num}.json")
    if os.path.exists(filepath):
        print(f"Skipping Abacus Chapter {ch_num} (already generated).")
        return
        
    
    prompt = f"""
    Generate a JSON chapter for Class 1 (or general beginner) Abacus Training.
    Chapter Number: {ch_num}
    Chapter Title: {title}
    Topics to cover: {topics}
    
    Make it highly interactive. Use the 'abacus_simulation' block so they can practice what you just taught them!
    Remember to provide Hindi and Gujarati translations for ALL text fields.
    """
    
    print(f"Generating Abacus Chapter {ch_num}: {title}...")
    try:
        response = model.generate_content(
            contents=[{"role": "user", "parts": [SYSTEM_PROMPT + "\n\n" + prompt]}],
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                response_mime_type="application/json"
            )
        )
        json_str = response.text.strip()
        data = json.loads(json_str)
        
        filepath = os.path.join(OUTPUT_DIR, f"abacus_level1_ch{ch_num}.json")
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Saved: {filepath}")
        
    except Exception as e:
        print(f"Failed to generate Chapter {ch_num}: {e}")
        if 'response' in locals():
            print("Raw output:", response.text)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Starting Zero-Shot Abacus Curriculum Generation...")
    for ch in CURRICULUM:
        generate_chapter(ch)
        time.sleep(2)
    print("Abacus curriculum generation complete!")

if __name__ == "__main__":
    main()
