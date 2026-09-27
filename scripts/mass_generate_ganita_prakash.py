import os
import json
import time
import subprocess
import google.generativeai as genai

def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"[Missing standard: {filepath}]"

def main():
    print("==================================================")
    print(" SHINE ACADEMY - GANITA PRAKASH BATCH GENERATOR")
    print("==================================================")
    print("This script runs while you sleep to generate all missing chapters.\n")

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        api_key = input("Enter your Google Gemini API Key: ").strip()
        if not api_key:
            print("Error: API Key is required.")
            return

    genai.configure(api_key=api_key)
    
    # Use gemini-1.5-pro for high-quality structured generation
    model = genai.GenerativeModel('gemini-1.5-pro')

    print("Loading Standards and Rules...")
    master_standard = read_file("standards/MASTER_CONTENT_STANDARD.yaml")
    chapter_standard = read_file("standards/CHAPTER_STANDARD.yaml")
    question_standard = read_file("standards/QUESTION_STANDARD.yaml")
    
    # Extract the TOP PRIORITY rule from AGENTS.md
    agents_md = read_file(".agents/AGENTS.md")
    hindi_directive = ""
    for line in agents_md.split('\n'):
        if "HINDI TRANSLATION IS A MUST EVERYWHERE" in agents_md:
            hindi_directive = """
=========================================================
TOP PRIORITY: HINDI TRANSLATION IS MANDATORY EVERYWHERE
=========================================================
This application is mainly for Indian students. The average student does not know English well. 
* HINDI TRANSLATION IS A MUST EVERYWHERE.
* Every single block of content (titles, bodies, questions, options, explanations, teacher tips) MUST include its Hindi equivalent (e.g., body_hi, title_hi, question_hi, options_hi, explanation_hi).
* Never generate a JSON payload that contains only English text.
"""
            break

    system_instruction = f"""
You are the Chief Academic Architect for Shine Academy's EduOS platform.
You are tasked with generating a COMPLETE 'Gold Standard' chapter in JSON format.
This JSON will be parsed by a Flutter application.

{hindi_directive}

CRITICAL RULES:
1. You MUST generate ONLY valid JSON (a single array of block objects). Do not include markdown wrappers (like ```json), just output the raw JSON array starting with [ and ending with ].
2. Follow the 8-Step Pedagogy Directive: Hook -> Socratic Thinking -> Discovery -> Reveal -> Knowledge Check -> Reflection -> Connection -> Mastery.
3. Every block must have an "id" field (e.g. "KOBJ_CLASS6_MATH_GP_CHX_...").
4. NEVER nest fields inside a "content": {{}} wrapper. Put them at the root level of the block.
5. In quiz/socratic questions, ALWAYS use an integer "correct_index". NEVER use a string "correct_answer".
6. The JSON structure MUST match the following standards perfectly:

=== CHAPTER STANDARD ===
{chapter_standard}

=== QUESTION STANDARD ===
{question_standard}

=== MASTER CONTENT STANDARD ===
{master_standard}
"""

    chapters_to_generate = [
        {"num": 2, "title": "Lines and Angles"},
        {"num": 3, "title": "Number Play"},
        {"num": 4, "title": "Data Handling and Presentation"},
        {"num": 5, "title": "Prime Time"},
        {"num": 6, "title": "Perimeter and Area"},
        {"num": 7, "title": "Fractions"},
        {"num": 8, "title": "Playing with Constructions"},
        {"num": 9, "title": "Symmetry"},
        {"num": 10, "title": "The Other Side of Zero"}
    ]

    for chapter in chapters_to_generate:
        ch_num = chapter["num"]
        ch_title = chapter["title"]
        file_name = f"cbse_class6_maths_gp_ch{ch_num}.json"
        file_path = os.path.join("app_core", "chapters", file_name)
        
        if os.path.exists(file_path):
            print(f"Skipping Chapter {ch_num}: {file_name} already exists.")
            continue
            
        print(f"\n==================================================")
        print(f" GENERATING: Class 6 Maths (Ganita Prakash) - Ch {ch_num}: {ch_title}")
        print(f"==================================================")
        
        prompt = f"Please generate the complete JSON array of blocks for Class 6 Maths, Ganita Prakash (New Syllabus), Chapter {ch_num}: '{ch_title}'. Make it highly engaging, bilingual (English + Hindi), and fully compliant with the 8-Step Pedagogy Standard. Generate at least 10-15 blocks to thoroughly cover the chapter."
        
        try:
            print("Sending request to Gemini... (This usually takes 60-90 seconds for a full chapter)")
            # Inject system instructions into the model config
            generation_model = genai.GenerativeModel(
                model_name='gemini-1.5-pro',
                system_instruction=system_instruction
            )
            response = generation_model.generate_content(prompt)
            
            raw_json = response.text.strip()
            if raw_json.startswith("```json"):
                raw_json = raw_json[7:]
            if raw_json.startswith("```"):
                raw_json = raw_json[3:]
            if raw_json.endswith("```"):
                raw_json = raw_json[:-3]
            
            raw_json = raw_json.strip()
            
            try:
                parsed_json = json.loads(raw_json)
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(parsed_json, f, indent=4)
                print(f"SUCCESS! Saved to {file_path}")
            except json.JSONDecodeError as e:
                print(f"ERROR: AI returned invalid JSON. Skipping. Details: {e}")
                err_path = f"failed_ch{ch_num}.txt"
                with open(err_path, "w", encoding="utf-8") as f:
                    f.write(raw_json)
                print(f"Saved raw AI output to {err_path} for manual fixing.")
                
        except Exception as e:
            print(f"API Error occurred: {e}")
            
        print("Sleeping for 10 seconds to respect API rate limits...")
        time.sleep(10)
        
    print("\nBatch generation complete!")
    print("Running automatic validation and ID generation script (scripts/fix_all_blocks.py)...")
    try:
        subprocess.run(["python3", "scripts/fix_all_blocks.py"], check=True)
        print("Validation successful. All block IDs and schema rules applied.")
    except Exception as e:
        print(f"Warning: Validation script encountered an error: {e}")

if __name__ == "__main__":
    main()
