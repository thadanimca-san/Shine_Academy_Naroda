import os
import json
import time
from google import genai
from google.genai import types

import PyPDF2

OUTPUT_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"
PDF_DIR = "/home/ubuntu/Shine_Academy_Naroda/SAN/shineboard_library/class_10/english"

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            t = page.extract_text()
            if t: text += t + "\n"
    return text

def generate_chapter_json(client, text_content, chapter_num):
    print(f"\n[{time.strftime('%X')}] 🚀 Generating GSEB Class 10 English Chapter {chapter_num}...")
    
    prompt = f"""
    You are an expert educational content creator for Shine Academy.
    I am providing you with the text of GSEB Class 10 English Chapter {chapter_num}.
    
    Your task is to convert it into a highly structured JSON according to our EduOS Standards.
    
    CRITICAL RULES:
    1. Every block must have an id starting with `gseb_class10_english_ch{chapter_num}_`
    2. Every single block of content MUST include its Hindi equivalent (e.g., `body_hi`, `title_hi`) AND its Gujarati equivalent (`body_gu`, `title_gu`).
    3. Follow the 8-Step Socratic Discovery Arc where possible (Hook, Socratic Question, Exploration, Reveal, Knowledge Check, Reflection, Connection, Mastery).
    4. Ensure the JSON is 100% valid. Do not output markdown code blocks.
    
    Here is the full text of the chapter:
    {text_content}
    """
    
    response = client.models.generate_content(
        model='gemini-3.1-pro-preview',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.2,
        ),
    )
    return response.text

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        api_key = input("Please enter your Gemini API Key: ")
        
    client = genai.Client(api_key=api_key)
    
    missing_chapters = [1, 4, 5, 6, 10]
    
    for ch in missing_chapters:
        pdf_path = os.path.join(PDF_DIR, f"textbook_gseb_ch{ch}.pdf")
        if not os.path.exists(pdf_path):
            print(f"Skipping Chapter {ch}: {pdf_path} not found.")
            continue
            
        print(f"Extracting text from {pdf_path}...")
        text_content = extract_text_from_pdf(pdf_path)
        
        success = False
        while not success:
            try:
                json_str = generate_chapter_json(client, text_content, ch)
                parsed_json = json.loads(json_str)
                
                output_file = os.path.join(OUTPUT_DIR, f"gseb_class10_english_ch{ch}.json")
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(parsed_json, f, indent=2, ensure_ascii=False)
                    
                print(f"Successfully saved Chapter {ch} to {output_file}")
                success = True
                time.sleep(5)
            except Exception as e:
                error_str = str(e)
                print(f"Failed to generate Chapter {ch}: {error_str}")
                if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                    time.sleep(15)
                else:
                    time.sleep(5)

if __name__ == "__main__":
    main()
