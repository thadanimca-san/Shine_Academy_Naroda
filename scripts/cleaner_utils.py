import re

def clean_textbook_text(text):
    # Remove weird bullet points like "n n n" or standalone "n " that come from PDF bullets
    text = re.sub(r'(?m)^[n\-\*•]\s+', '', text)
    text = re.sub(r'(?m)^\s*n\s*$', '', text)
    # Remove page numbers or footer artifacts like "Reprint 2025-26"
    text = re.sub(r'Reprint \d{4}-\d{2}', '', text)
    text = re.sub(r'(?m)^\s*\d+\s*$', '', text) # standalone page numbers
    # Remove excessive newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Clean up weird characters
    text = text.replace('\x0c', '') # Form feed character
    text = text.replace('', '')
    
    # Final strip
    return text.strip()
