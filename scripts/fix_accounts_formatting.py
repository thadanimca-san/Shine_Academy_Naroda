import os
import json

def process_accounts_chapter(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    new_blocks = []
    
    for block in data:
        # Example processing for worked_example -> theory + markdown_table
        if block.get('type') == 'worked_example':
            # Create the theory block for the question
            theory_block = {
                "id": block["id"] + "_Q",
                "type": "theory",
                "title": block.get("title", ""),
                "title_hi": block.get("title_hi", ""),
                "title_gu": block.get("title_gu", ""),
                "body": block.get("question", ""),
                "body_hi": block.get("question_hi", ""),
                "body_gu": block.get("question_gu", "")
            }
            new_blocks.append(theory_block)
            
            # Create the markdown_table block for the solution
            table_block = {
                "id": block["id"] + "_SOL",
                "type": "markdown_table",
                "title": "Solution",
                "title_hi": "समाधान",
                "title_gu": "ઉકેલ",
                "body": block.get("explanation", ""),
                "body_hi": block.get("explanation_hi", ""),
                "body_gu": block.get("explanation_gu", "")
            }
            # Note: This is where an LLM should be used to convert raw explanation text into markdown tables.
            # For this MVP script, we just copy the text. A full LLM pipeline can be added here using eduos_ai_engine.
            new_blocks.append(table_block)
            
        elif block.get('type') == 'practice_question':
            # For practice questions, we just ensure explanation is present.
            # Real LLM logic would parse the question and generate the answer markdown table here.
            new_blocks.append(block)
        else:
            new_blocks.append(block)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(new_blocks, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(f"Finished processing {filepath}.")

if __name__ == "__main__":
    chapters_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/"
    for filename in os.listdir(chapters_dir):
        if filename.startswith("gseb_class12_accounts_") and filename.endswith(".json"):
            process_accounts_chapter(os.path.join(chapters_dir, filename))
