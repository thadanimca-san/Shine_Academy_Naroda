import os

def chunk_file():
    in_file = "/home/ubuntu/Shine_Academy_Naroda/SAN/shineboard_library/class_12/accounts/textbook_gseb_class12_accounts_ch4.txt"
    out_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ch4_chunks"
    
    os.makedirs(out_dir, exist_ok=True)
    
    with open(in_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    exercise_start_idx = 2658 # 0-indexed, line 2659
    theory_lines = lines[:exercise_start_idx]
    exercise_lines = lines[exercise_start_idx:]
    
    chunk_index = 1
    
    # Theory chunks (~800 lines)
    for i in range(0, len(theory_lines), 800):
        chunk_lines = theory_lines[i:i+800]
        with open(os.path.join(out_dir, f"chunk_{chunk_index}.txt"), 'w', encoding='utf-8') as f:
            f.writelines(chunk_lines)
        print(f"Created Theory chunk_{chunk_index}.txt ({len(chunk_lines)} lines)")
        chunk_index += 1
        
    # Exercise chunks (~150 lines)
    for i in range(0, len(exercise_lines), 150):
        chunk_lines = exercise_lines[i:i+150]
        with open(os.path.join(out_dir, f"chunk_{chunk_index}.txt"), 'w', encoding='utf-8') as f:
            f.writelines(chunk_lines)
        print(f"Created Exercise chunk_{chunk_index}.txt ({len(chunk_lines)} lines)")
        chunk_index += 1

if __name__ == "__main__":
    chunk_file()
