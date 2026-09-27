import os
import json
import requests
import glob

# NOTE: To run this script when your model quota is over, you need to use an external API 
# (e.g. Google Gemini API, OpenAI API, Anthropic API) with your own API key.
# This script provides a template for how you would call an LLM API to process your chunks.

API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={API_KEY}"

def process_chunk_with_llm(chunk_text, subject, chapter_num, chunk_num):
    prompt = f"""
Your ONLY task is to read the textbook chunk below.

Extract the information, translate it to Hindi and Gujarati, and format it as a JSON array of blocks according to the EduOS standard (no content wrapper, root-level properties, unique IDs starting with KOBJ_{subject.upper()}_CH{chapter_num}_{chunk_num}_).
- For Theory chunks, use the 8-Step Socratic Discovery Arc if applicable.
- For Exercise chunks, extract EVERY SINGLE QUESTION perfectly into 'mcq' or 'practice_question' or 'worked_example'. Format tables as markdown tables.

Textbook Chunk:
{chunk_text}

Output ONLY valid JSON. No markdown backticks.
    """
    
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseMimeType": "application/json",
        }
    }
    
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        data = response.json()
        result_text = data["candidates"][0]["content"]["parts"][0]["text"]
        return result_text
    else:
        print(f"Error calling API: {response.status_code} - {response.text}")
        return None

def run():
    # Example: Process class 12 statistics chapter 1
    subject = "STAT"
    chapter_num = 1
    chunk_dir = f"../app_core/chapters/ch{chapter_num}_{subject.lower()}_chunks"
    
    chunk_files = sorted(glob.glob(f"{chunk_dir}/chunk_*.txt"))
    for chunk_file in chunk_files:
        chunk_num = chunk_file.split("_")[-1].split(".")[0]
        out_file = chunk_file.replace(".txt", ".json")
        
        if os.path.exists(out_file):
            print(f"Skipping {out_file}, already exists.")
            continue
            
        print(f"Processing {chunk_file} with LLM...")
        with open(chunk_file, "r", encoding="utf-8") as f:
            chunk_text = f.read()
            
        json_output = process_chunk_with_llm(chunk_text, subject, chapter_num, chunk_num)
        
        if json_output:
            with open(out_file, "w", encoding="utf-8") as out_f:
                out_f.write(json_output)
            print(f"Saved {out_file}")
            
if __name__ == "__main__":
    # run()
    print("Script template ready. Edit run() to point to the correct directories and add your API key.")
