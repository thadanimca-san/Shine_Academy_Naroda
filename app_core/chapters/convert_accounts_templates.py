import json
import os
import glob

# Convert legacy accounts JSON to CHAPTER_STANDARD format

chapters_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"
files = glob.glob(os.path.join(chapters_dir, "*accounts_ch*.json"))

def convert_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if "metadata" in data and "blocks" in data:
            # Already converted
            return
            
        new_data = {
            "metadata": {
                "title": data.get("title", "Untitled"),
                "subject": data.get("subject", "Accountancy"),
                "grade": data.get("class", "12").replace("Class ", ""),
                "curriculum": [data.get("board", "GSEB")],
                "difficulty": "Intermediate",
                "version": "2.0.0",
                "id": data.get("chapter_id", os.path.basename(filepath).replace('.json', ''))
            },
            "blocks": []
        }
        
        # Add a hook
        new_data["blocks"].append({
            "type": "hook",
            "content": f"Welcome to the chapter on {data.get('title')}. Have you ever wondered how businesses keep track of their complex financial transactions?"
        })
        
        # Theory sections (apply socratic arc roughly)
        for i, theory in enumerate(data.get("theory_sections", [])):
            new_data["blocks"].append({
                "type": "theory",
                "content": f"### {theory.get('section_title', '')}\n\n{theory.get('content', '')}"
            })
            # Insert a quick check after every theory to break it up (as per standard)
            new_data["blocks"].append({
                "type": "reflection",
                "content": "Take a moment to think about what you just read. Can you explain this concept to someone else?"
            })
            
        # Definitions
        for definition in data.get("definitions", []):
            new_data["blocks"].append({
                "type": "definition",
                "content": f"**{definition.get('term', '')}**: {definition.get('meaning', '')}"
            })
            
        # Examples
        for example in data.get("examples", []):
            new_data["blocks"].append({
                "type": "example",
                "content": f"### {example.get('title', '')}\n\n{example.get('description', '')}"
            })
            
        # Exercises -> quizzes
        for exercise in data.get("exercises", []):
            options = exercise.get("options", [])
            correct_answer = exercise.get("correct_answer")
            try:
                correct_index = options.index(correct_answer)
            except ValueError:
                correct_index = 0
                
            # The standard for quiz is: question, options, correct_index.
            # But the content goes inside 'content' according to default_blocks.dart?
            # Wait, default_blocks.dart says: BlockValidationUtils.require(block, 'question', String)
            # So they are at the top level of the block, or inside data? 
            # In learning_engine_screen.dart it passes 'block' to the widget.
            new_data["blocks"].append({
                "type": "quiz",
                "question": exercise.get("question", ""),
                "options": options,
                "correct_index": correct_index,
                "explanation": exercise.get("explanation", "")
            })
            
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, indent=2)
            
        print(f"Converted {os.path.basename(filepath)}")
    except Exception as e:
        print(f"Failed to convert {os.path.basename(filepath)}: {e}")

for f in files:
    convert_file(f)

print("Conversion complete.")
