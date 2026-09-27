import os

def split_chapter():
    input_file = "/home/ubuntu/Shine_Academy_Naroda/SAN/shineboard_library/class_12/accounts/textbook_gseb_class12_accounts_ch6.txt"
    output_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ch6_chunks"
    os.makedirs(output_dir, exist_ok=True)
    
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    theory_lines = lines[:4323]
    exercise_lines = lines[4323:]
    
    chunk_index = 1
    
    # Split theory (800 lines max)
    theory_chunk_size = 800
    for i in range(0, len(theory_lines), theory_chunk_size):
        chunk = theory_lines[i:i + theory_chunk_size]
        output_file = os.path.join(output_dir, f"chunk_{chunk_index}.txt")
        with open(output_file, "w", encoding="utf-8") as out_f:
            out_f.writelines(chunk)
        print(f"Created Theory chunk {chunk_index} with {len(chunk)} lines.")
        chunk_index += 1
        
    # Split exercise (150 lines max)
    exercise_chunk_size = 150
    for i in range(0, len(exercise_lines), exercise_chunk_size):
        chunk = exercise_lines[i:i + exercise_chunk_size]
        output_file = os.path.join(output_dir, f"chunk_{chunk_index}.txt")
        with open(output_file, "w", encoding="utf-8") as out_f:
            out_f.writelines(chunk)
        print(f"Created Exercise chunk {chunk_index} with {len(chunk)} lines.")
        chunk_index += 1

if __name__ == "__main__":
    split_chapter()
