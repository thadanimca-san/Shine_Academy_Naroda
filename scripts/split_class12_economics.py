import os

DIR = "/home/ubuntu/Shine_Academy_Naroda/SAN/shineboard_library/class_12/economics"
FILE = os.path.join(DIR, "GSEB-Class-12-Economics-textbook-E.M..txt")

# We found the exact line numbers where each chapter's first sub-heading (X.1) starts.
# We will step back 30 lines from these to ensure we capture the chapter title and introduction.
# However, splitting exactly by line number is safest.
chapter_start_lines = [
    275,   # Ch 1
    1305,  # Ch 2
    2435,  # Ch 3
    2815,  # Ch 4
    3565,  # Ch 5
    4675,  # Ch 6
    5550,  # Ch 7
    6720,  # Ch 8
    7420,  # Ch 9
    8590,  # Ch 10
    9125,  # Ch 11
]

def split_file(filepath, start_lines):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i in range(len(start_lines)):
        start_line = start_lines[i] - 1  # 0-indexed
        end_line = start_lines[i+1] - 1 if i+1 < len(start_lines) else len(lines)
        
        ch_lines = lines[start_line:end_line]
        ch_text = "".join(ch_lines)
        
        ch_num = i + 1
        out_name = f"textbook_gseb_class12_economics_ch{ch_num}.txt"
        out_path = os.path.join(DIR, out_name)
        
        with open(out_path, 'w', encoding='utf-8') as out_f:
            out_f.write(ch_text)
        print(f"Wrote {out_name} (approx {len(ch_text)} chars)")

def main():
    print("Splitting Economics Textbook using explicit line numbers...")
    split_file(FILE, chapter_start_lines)
    
if __name__ == "__main__":
    main()
