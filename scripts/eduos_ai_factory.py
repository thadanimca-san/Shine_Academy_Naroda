import os
import json
import subprocess
import google.generativeai as genai
import re

def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"[Missing standard: {filepath}]"

def main():
    print("==================================================")
    print(" SHINE ACADEMY - EduOS AI CONTENT FACTORY")
    print("==================================================")
    print("This tool generates Gold Standard Chapters automatically.\n")

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        api_key = input("Enter your Google Gemini API Key: ").strip()
        if not api_key:
            print("Error: API Key is required.")
            return

    genai.configure(api_key=api_key)

    grade = input("Class (e.g., 10): ").strip()
    subject = input("Subject (e.g., Science): ").strip()
    chapter_num = input("Chapter Number (e.g., 9): ").strip()
    chapter_topic = input("Chapter Topic/Name: ").strip()

    print("\nReading EduOS Master Standards...")
    master_standard = read_file("standards/MASTER_CONTENT_STANDARD.yaml")
    chapter_standard = read_file("standards/CHAPTER_STANDARD.yaml")
    question_standard = read_file("standards/QUESTION_STANDARD.yaml")
    media_standard = read_file("standards/MEDIA_STANDARD.yaml")

    system_instruction = f"""
You are the Chief Academic Architect for Shine Academy's EduOS platform.
You are tasked with generating a COMPLETE 'Gold Standard' chapter in JSON format.
This JSON will be parsed by a Flutter application.

CRITICAL RULES:
1. You MUST generate ONLY valid JSON. Do not include markdown code blocks (like ```json), just output the raw JSON object starting with {{ and ending with }}.
2. Follow the 8-Step Pedagogy Directive: Hook -> Socratic Thinking -> Discovery -> Reveal -> Knowledge Check -> Reflection -> Connection -> Mastery.
3. Every block must have an "id" field (use a placeholder like "KOBJ_CLASS_{grade}_{subject[:3].upper()}_CH{chapter_num}_...").
4. NEVER nest fields inside a "content": {{}} wrapper unless explicitly required by the schema. All fields like "body", "title", "question", "options", "correct_index" must be at the root level of the block object.
5. In quiz/socratic questions, ALWAYS use an integer "correct_index" (0-indexed). NEVER use a string "correct_answer".
6. The JSON structure MUST match the following standards perfectly:

=== CHAPTER STANDARD ===
{chapter_standard}

=== QUESTION STANDARD ===
{question_standard}

=== MASTER CONTENT STANDARD ===
{master_standard}
"""

    prompt = f"""
Please generate the complete JSON for Class {grade}, Subject: {subject}, Chapter {chapter_num}: "{chapter_topic}".
Make it comprehensive, engaging, and fully compliant with the 8-Step Pedagogy Standard. Include at least 8-10 high-quality blocks (hooks, socratic, theory, interactive diagrams, knowledge_checks) and 5 summative assessments. 
"""

    print("\nConnecting to Gemini AI (gemini-1.5-pro)... This usually takes 30-60 seconds.")
    try:
        # Use a large context model suitable for generation
        model = genai.GenerativeModel(
            model_name='gemini-1.5-pro',
            system_instruction=system_instruction
        )
        
        response = model.generate_content(prompt)
        raw_json = response.text.strip()
        
        # Clean up markdown formatting if the AI ignored the instruction
        if raw_json.startswith("```json"):
            raw_json = raw_json[7:]
        if raw_json.startswith("```"):
            raw_json = raw_json[3:]
        if raw_json.endswith("```"):
            raw_json = raw_json[:-3]
        
        raw_json = raw_json.strip()

        # Parse to verify it's valid JSON
        try:
            parsed_json = json.loads(raw_json)
        except json.JSONDecodeError as e:
            print(f"Error parsing generated JSON: {e}")
            print("Saving raw output to failed_generation.txt for manual inspection.")
            with open("failed_generation.txt", "w", encoding="utf-8") as f:
                f.write(raw_json)
            return

        file_name = f"gseb_class{grade}_{subject.lower()}_ch{chapter_num}.json"
        file_path = os.path.join("app_core", "chapters", file_name)

        print(f"\nWriting chapter to {file_path}...")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(parsed_json, f, indent=4)
        
        print("\nSuccessfully generated chapter!")
        
        print("Running automatic validation and ID generation script (scripts/fix_all_blocks.py)...")
        try:
            subprocess.run(["python3", "scripts/fix_all_blocks.py"], check=True)
            print("Validation successful. All block IDs and schema rules applied.")
        except subprocess.CalledProcessError:
            print("Warning: Validation script encountered an error. You may need to run it manually.")

        print(f"\nDONE! Your new chapter is ready at: {file_path}")
        print("You can now build the app or edit the chapter directly on your digital panel!")

    except Exception as e:
        print(f"An error occurred while generating the chapter: {e}")

if __name__ == "__main__":
    main()
