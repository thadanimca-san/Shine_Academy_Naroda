import json
import glob
import os

files = glob.glob("/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_*.json")
files.extend(glob.glob("/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/cbse_class10_*.json"))

print("Missing or incomplete chapters:")
for f in sorted(files):
    try:
        with open(f, 'r') as file:
            data = json.load(file)
            
            blocks = []
            if isinstance(data, list):
                blocks = data
            elif isinstance(data, dict):
                blocks = data.get("blocks", [])
                if not blocks and "chapters" in data:
                    blocks = data["chapters"]
                    
            practice_questions = [b for b in blocks if isinstance(b, dict) and b.get("type") == "practice_question"]
            if len(practice_questions) < 5:
                print(f"{os.path.basename(f)}: {len(practice_questions)} practice questions")
    except Exception as e:
        print(f"Error reading {f}: {e}")
