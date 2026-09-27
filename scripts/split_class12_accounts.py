import os

DIR = "/home/ubuntu/Shine_Academy_Naroda/SAN/shineboard_library/class_12/accounts"
PART1 = os.path.join(DIR, "Std-12 Elements of Accounts Part-1 E.M..txt")
PART2 = os.path.join(DIR, "Std-12 Elements of Accounts Part-2 E.M..txt")

# We will read both files and split them based on the known chapter titles.

part1_titles = [
    "Introduction to Partnership",
    "Final Accounts (Financial Statements)",
    "Valuation of Goodwill",
    "Reconstruction of Partnership",
    "Admission of a Partner",
    "Retirement / Death of a Partner",
    "Dissolution of Partnership Firm"
]

part2_titles = [
    "Accounting for Share Capital",
    "Accounting for Debentures",
    "Company Final Accounts",
    "Analysis of Financial Statements",
    "Accounting Ratios and Analysis",
    "Cash Flow Statement"
]

def split_file(filepath, titles, start_ch_num):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    indices = []
    search_start = 5000 
    
    for title in titles:
        idx = text.find(title, search_start)
        if idx == -1:
            idx = text.find(title.upper(), search_start)
        
        if idx != -1:
            indices.append((idx, title))
        else:
            print(f"WARNING: Could not find title '{title}' in {filepath}")

    indices.sort(key=lambda x: x[0])
    
    ch_num = start_ch_num
    for i in range(len(indices)):
        start_idx = indices[i][0]
        end_idx = indices[i+1][0] if i+1 < len(indices) else len(text)
        
        ch_text = text[start_idx:end_idx]
        out_name = f"textbook_gseb_class12_accounts_ch{ch_num}.txt"
        out_path = os.path.join(DIR, out_name)
        
        with open(out_path, 'w', encoding='utf-8') as out_f:
            out_f.write(ch_text)
        print(f"Wrote {out_name} (approx {len(ch_text)} chars)")
        ch_num += 1

def main():
    print("Splitting Part 1...")
    split_file(PART1, part1_titles, 1)
    print("Splitting Part 2...")
    split_file(PART2, part2_titles, 8)
    
if __name__ == "__main__":
    main()
