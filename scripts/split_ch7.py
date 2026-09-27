import os

def split_file(input_file, output_dir, max_lines_theory=800, max_lines_exercises=150):
    os.makedirs(output_dir, exist_ok=True)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    chunk_index = 1
    current_chunk = []
    current_lines = 0
    in_exercises = False
    
    for line in lines:
        current_chunk.append(line)
        current_lines += 1
        
        # Check if we transitioned into exercises
        if line.strip().upper() == "EXERCISE":
            in_exercises = True
            
        limit = max_lines_exercises if in_exercises else max_lines_theory
        
        if current_lines >= limit:
            # try to break at an empty line if possible
            if line.strip() == "":
                output_file = os.path.join(output_dir, f"chunk_{chunk_index}.txt")
                with open(output_file, 'w', encoding='utf-8') as out_f:
                    out_f.writelines(current_chunk)
                print(f"Created {output_file} with {current_lines} lines")
                chunk_index += 1
                current_chunk = []
                current_lines = 0
                
    if current_chunk:
        output_file = os.path.join(output_dir, f"chunk_{chunk_index}.txt")
        with open(output_file, 'w', encoding='utf-8') as out_f:
            out_f.writelines(current_chunk)
        print(f"Created {output_file} with {current_lines} lines")

if __name__ == "__main__":
    input_txt = "/home/ubuntu/Shine_Academy_Naroda/SAN/shineboard_library/class_12/accounts/textbook_gseb_class12_accounts_ch7.txt"
    out_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ch7_chunks"
    split_file(input_txt, out_dir)
