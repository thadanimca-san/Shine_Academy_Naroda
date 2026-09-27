import os
import json
import time
import google.generativeai as genai
import argparse

# NOTE: You will need to install PyPDF2 if you haven't already:
# pip install PyPDF2

try:
    import PyPDF2
except ImportError:
    print("PyPDF2 is required to parse the sample papers.")
    print("Please run: pip install PyPDF2")
    exit(1)

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def chunk_text(text, chunk_size=30000):
    """Splits text into chunks to avoid overwhelming the model's output window."""
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def process_chunk(chunk, model, prompt_template):
    prompt = prompt_template.replace("{{TEXT}}", chunk)
    
    max_retries = 5
    retry_delay = 10
    
    for attempt in range(max_retries):
        try:
            response = model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(
                    response_mime_type="application/json",
                )
            )
            return json.loads(response.text)
        except Exception as e:
            error_str = str(e)
            if "429" in error_str:
                print(f"    [Quota Exceeded] Waiting {retry_delay} seconds before retrying (Attempt {attempt+1}/{max_retries})...")
                time.sleep(retry_delay)
                retry_delay *= 2  # Exponential backoff
                continue
            else:
                print(f"Error calling Gemini API: {e}")
                # In case the JSON parsing fails because it output markdown
                try:
                    if "```json" in error_str or "```json" in getattr(e, 'text', ''):
                        return json.loads(error_str.split("```json")[1].split("```")[0].strip())
                except:
                    pass
                return None
    
    print("FAILED after maximum retries due to quota limits.")
    return None

def main():
    print("==========================================================")
    print(" SHINE ACADEMY - CBSE SAMPLE PAPER TO JSON PROCESSOR")
    print("==========================================================")
    
    parser = argparse.ArgumentParser(description="Process CBSE sample papers into Shine Academy JSON format.")
    parser.add_argument("--input_folder", type=str, default="raw_data/sample_papers", help="Folder containing PDF sample papers")
    parser.add_argument("--output_folder", type=str, default="app_core/chapters", help="Folder to save generated JSONs")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY", "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA")

    genai.configure(api_key=api_key)
    
    # We use gemini-2.5-flash as it is the stable production model with a generous 1500 request/day free tier limit
    model = genai.GenerativeModel("gemini-2.5-flash")

    if not os.path.exists(args.input_folder):
        os.makedirs(args.input_folder)
        print(f"Created folder {args.input_folder}. Please place your CBSE sample paper PDFs inside it and run this script again.")
        return

    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    pdf_files = [f for f in os.listdir(args.input_folder) if f.endswith('.pdf')]
    
    if not pdf_files:
        print(f"No PDF files found in {args.input_folder}.")
        return

    system_prompt = """
You are an expert curriculum extractor for Shine Academy EduOS.
I will give you raw text from a CBSE sample paper.
You MUST extract ALL questions (multiple choice, short answer, long answer) and convert them into the EduOS JSON Block format.

CRITICAL RULES (Master Standards):
1. HINDI AND GUJARATI TRANSLATION IS MANDATORY. Every field must have _hi and _gu counterparts.
2. Data must NOT be inside a "content": {} wrapper. Put fields at the root level.
3. For MCQ questions, use integer "correct_index" (0-based). Do not use string correct_answer.
4. Output MUST be a pure JSON array of block objects.

Structure for MCQs ('mcq'):
{
  "type": "mcq",
  "id": "CBSE_SP_MCQ_...",
  "question": "English question text",
  "question_hi": "Hindi question text",
  "question_gu": "Gujarati question text",
  "options": ["A", "B", "C", "D"],
  "options_hi": ["A_hi", "B_hi", "C_hi", "D_hi"],
  "options_gu": ["A_gu", "B_gu", "C_gu", "D_gu"],
  "correct_index": 0,
  "explanation": "Detailed step-by-step solution",
  "explanation_hi": "Hindi explanation",
  "explanation_gu": "Gujarati explanation"
}

Structure for Subjective Questions ('socratic_question' or 'theory' with solution):
{
  "type": "theory",
  "id": "CBSE_SP_THEORY_...",
  "title": "Q: [English Question Text]",
  "title_hi": "Q: [Hindi Question]",
  "title_gu": "Q: [Gujarati Question]",
  "body": "Solution: [English Solution]",
  "body_hi": "Solution: [Hindi Solution]",
  "body_gu": "Solution: [Gujarati Solution]"
}

Parse the following text and return the JSON array:
{{TEXT}}
"""

    for pdf_file in pdf_files:
        output_filename = pdf_file.replace('.pdf', '_blocks.json')
        output_path = os.path.join(args.output_folder, output_filename)
        
        if os.path.exists(output_path):
            print(f"SKIPPING: {pdf_file} is already processed (found {output_filename}).")
            continue

        pdf_path = os.path.join(args.input_folder, pdf_file)
        print(f"\nProcessing {pdf_file}...")
        
        text = extract_text_from_pdf(pdf_path)
        if not text.strip():
            print(f"Could not extract text from {pdf_file}. It might be a scanned image.")
            continue
            
        chunks = chunk_text(text)
        print(f"Split into {len(chunks)} chunks.")
        
        all_blocks = []
        for i, chunk in enumerate(chunks):
            print(f"  Sending chunk {i+1}/{len(chunks)} to Gemini...")
            blocks = process_chunk(chunk, model, system_prompt)
            if blocks:
                if isinstance(blocks, list):
                    all_blocks.extend(blocks)
                elif isinstance(blocks, dict) and "blocks" in blocks:
                    all_blocks.extend(blocks["blocks"])
            
            # Sleep to avoid hitting rate limits on free tier
            time.sleep(3)
            
        if all_blocks:
            output_filename = pdf_file.replace('.pdf', '_blocks.json')
            output_path = os.path.join(args.output_folder, output_filename)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(all_blocks, f, ensure_ascii=False, indent=2)
            print(f"SUCCESS: Saved {len(all_blocks)} extracted questions to {output_path}")
        else:
            print(f"FAILED: No valid blocks extracted from {pdf_file}.")

if __name__ == "__main__":
    main()
