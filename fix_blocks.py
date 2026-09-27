import json
import os
import glob

def fix_file(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (does not exist)")
        return
        
    with open(filepath, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"Error decoding {filepath}")
            return
            
    # Normalize root structure to a flat list
    blocks = []
    if isinstance(data, dict) and "blocks" in data:
        blocks = data["blocks"]
    elif isinstance(data, list):
        blocks = data
    else:
        print(f"Unknown structure in {filepath}")
        return
        
    # Map hallucinated types to supported types
    for block in blocks:
        old_type = block.get("type", "")
        
        if old_type == "ai_tutor_prompt":
            block["type"] = "theory"
            # if content is an object, try to extract string
            if isinstance(block.get("content"), dict):
                block["content"] = block["content"].get("question", "") or block["content"].get("prompt", str(block["content"]))
                
        elif old_type == "animation":
            block["type"] = "animated_diagram"
            
        elif old_type == "definition":
            # If it has term_id, it's a dictionary link
            if isinstance(block.get("content"), dict) and "term_id" in block.get("content", {}):
                block["type"] = "dictionary_link"
            else:
                block["type"] = "theory"
                if isinstance(block.get("content"), dict):
                    block["content"] = str(block["content"].get("text", block["content"]))
                    
        elif old_type == "mcq":
            block["type"] = "quiz"
            if "content" in block:
                # the subagent might have put question inside content
                c = block["content"]
                if isinstance(c, dict):
                    if "question" not in block: block["question"] = c.get("question", "")
                    if "options" not in block: block["options"] = c.get("options", [])
                    if "correct_index" not in block: block["correct_index"] = c.get("correct_index", 0)
                del block["content"]
                
        elif old_type in ["reflection", "cross_subject_link", "challenge_question", "project"]:
            block["type"] = "theory"
            if isinstance(block.get("content"), dict):
                # Flatten the object to a string
                title = block["content"].get("title", old_type.title())
                desc = block["content"].get("description", block["content"].get("text", ""))
                block["content"] = f"**{title}**: {desc}"
                
        elif old_type == "real_world_example":
            # Just ensure content is a dict with title and description
            pass
            
    # Write back flat list
    with open(filepath, 'w') as f:
        json.dump(blocks, f, indent=2)
    print(f"Fixed {filepath}")

# Find all blocks.json in gseb_class9_science_ch*
for file in glob.glob("/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/gseb_class9_science_ch*/blocks.json"):
    fix_file(file)

