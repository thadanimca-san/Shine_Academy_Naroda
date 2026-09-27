import os
import sys
import argparse
import subprocess
from pathlib import Path

def process_pdf(pdf_path, lang, force_ocr, skip_text):
    """
    Converts a single PDF to text using ocrmypdf and pdftotext.
    """
    pdf_path = Path(pdf_path)
    if not pdf_path.is_file() or pdf_path.suffix.lower() != '.pdf':
        print(f"Skipping {pdf_path.name} (Not a valid PDF)")
        return

    # Don't process files that are already the output of our OCR
    if pdf_path.name.startswith("searchable_"):
        print(f"Skipping {pdf_path.name} (Already processed)")
        return

    searchable_pdf = pdf_path.parent / f"searchable_{pdf_path.name}"
    text_file = pdf_path.with_suffix('.txt')

    print(f"\n--- Processing {pdf_path.name} ---")

    # Step 1: Run OCR if requested or needed
    if lang:
        ocr_lang = f"{lang}+eng"
        
        ocr_cmd = ["ocrmypdf"]
        if force_ocr:
            ocr_cmd.append("--force-ocr")
        elif skip_text:
            ocr_cmd.append("--skip-text")
        
        ocr_cmd.extend(["-l", ocr_lang, str(pdf_path), str(searchable_pdf)])
        
        print(f"Running OCR: {' '.join(ocr_cmd)}")
        try:
            subprocess.run(ocr_cmd, check=True)
            target_pdf_for_text = searchable_pdf
        except subprocess.CalledProcessError as e:
            print(f"OCR failed for {pdf_path.name}. Error: {e}")
            return
    else:
        # If no language specified, we skip OCR and just try to extract existing text
        target_pdf_for_text = pdf_path

    # Step 2: Extract text from the PDF
    print(f"Extracting text to {text_file.name}...")
    try:
        subprocess.run(["pdftotext", str(target_pdf_for_text), str(text_file)], check=True)
        print(f"Success! Text saved to {text_file.name}")
    except subprocess.CalledProcessError as e:
        print(f"Text extraction failed for {pdf_path.name}. Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Convert PDFs in a folder to text using OCR.")
    parser.add_argument("folder", help="Path to the folder containing PDF files")
    parser.add_argument("--lang", choices=['guj', 'hin'], help="Language for OCR (guj or hin). If omitted, OCR is skipped and direct text extraction is attempted.")
    parser.add_argument("--force-ocr", action="store_true", help="Force OCR on all pages (rasterize all vector text)")
    parser.add_argument("--skip-text", action="store_true", help="Skip OCR on pages that already contain text")
    
    args = parser.parse_args()

    folder_path = Path(args.folder)
    
    if not folder_path.is_dir():
        print(f"Error: {args.folder} is not a valid directory.")
        sys.exit(1)
        
    if args.force_ocr and args.skip_text:
        print("Error: You cannot use both --force-ocr and --skip-text at the same time.")
        sys.exit(1)

    print(f"Scanning folder: {folder_path.resolve()}")
    
    pdf_files = list(folder_path.glob("*.pdf"))
    if not pdf_files:
        print("No PDF files found in the directory.")
        return
        
    print(f"Found {len(pdf_files)} PDF files.")

    for pdf_file in pdf_files:
        process_pdf(pdf_file, args.lang, args.force_ocr, args.skip_text)

if __name__ == "__main__":
    main()
