import os

def split_statistics_ch1():
    input_file = "/home/ubuntu/Shine_Academy_Naroda/SAN/shineboard_library/class_12/statistics/Std-12 Statistics Part-1 E.M.txt"
    output_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ch1_stat_chunks"
    
    os.makedirs(output_dir, exist_ok=True)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    start_line = 272 # 0-indexed for 273
    end_line = 5616
    
    ch1_lines = lines[start_line:end_line]
    
    chunk_size = 400
    chunk_num = 1
    
    for i in range(0, len(ch1_lines), chunk_size):
        chunk = ch1_lines[i:i + chunk_size]
        chunk_file = os.path.join(output_dir, f"chunk_{chunk_num}.txt")
        with open(chunk_file, 'w', encoding='utf-8') as f:
            f.writelines(chunk)
        print(f"Created {chunk_file} with {len(chunk)} lines.")
        chunk_num += 1

if __name__ == "__main__":
    split_statistics_ch1()
