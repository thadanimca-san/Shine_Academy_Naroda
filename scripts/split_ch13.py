import os

def split_chapter():
    input_file = "/home/ubuntu/Shine_Academy_Naroda/SAN/shineboard_library/class_12/accounts/textbook_gseb_class12_accounts_ch13.txt"
    out_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ch13_chunks"
    
    os.makedirs(out_dir, exist_ok=True)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    chunks = []
    current_chunk = []
    in_exercise = False
    
    for i, line in enumerate(lines):
        # Line 3155 (index 3154) is Exercise
        if i >= 3154:
            in_exercise = True
            
        current_chunk.append(line)
        
        limit = 150 if in_exercise else 800
        
        if len(current_chunk) >= limit:
            chunks.append("".join(current_chunk))
            current_chunk = []
            
    if current_chunk:
        chunks.append("".join(current_chunk))
        
    for idx, chunk_text in enumerate(chunks, 1):
        out_file = os.path.join(out_dir, f"chunk_{idx}.txt")
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(chunk_text)
        print(f"Created {out_file} with {chunk_text.count(chr(10))} lines")

if __name__ == "__main__":
    split_chapter()
