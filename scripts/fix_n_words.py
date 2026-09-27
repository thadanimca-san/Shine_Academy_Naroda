import json
import os

FILE_PATH = 'app_core/universal_dictionary/generated_massive_dict.json'

def load_data():
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(data):
    # Ensure directory exists if needed (it should since we're modifying an existing file)
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    if not os.path.exists(FILE_PATH):
        print(f"Error: Could not find {FILE_PATH}")
        return

    print("Loading massive dictionary (this may take a few seconds)...")
    data = load_data()
    terms = data.get('terms', [])
    
    # Collect all words starting with 'n' (case-insensitive)
    n_terms = []
    for idx, term in enumerate(terms):
        word = term.get('term', {}).get('english', '')
        # Only look at words starting with lowercase 'n' followed by another letter, 
        # to filter out things like "n" alone.
        if isinstance(word, str) and word.startswith('n') and len(word) > 2:
            n_terms.append((idx, word))
            
    if not n_terms:
        print("No words starting with 'n' were found!")
        return
        
    print(f"\nFound {len(n_terms)} words starting with 'n'.")
    print("Instructions:")
    print(" - Type 'y' and press Enter to remove the extra 'n'.")
    print(" - Press Enter (or type 'n') to skip the word (if it's a real word like 'noodles').")
    print(" - Type 'q' to quit and save your progress at any time.\n")
    
    changes_made = 0
    try:
        for idx, word in n_terms:
            proposed = word[1:]
            ans = input(f"Change '{word}' to '{proposed}'? [y/N/q]: ").strip().lower()
            
            if ans == 'q':
                break
            elif ans == 'y':
                terms[idx]['term']['english'] = proposed
                changes_made += 1
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        
    if changes_made > 0:
        print(f"\nSaving {changes_made} changes to the dictionary...")
        save_data(data)
        print("Done! You can run this script again later if you didn't finish.")
    else:
        print("\nNo changes made.")

if __name__ == '__main__':
    main()
