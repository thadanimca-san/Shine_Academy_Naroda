import json
import os

output_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
prefixes = ['ncert', 'gseb', 'cbse']

for prefix in prefixes:
    for i in range(2, 8):
        ch_id = f"{prefix}_class10_deo_bank_2026_ch{i}"
        title = "question Bank 2026"
        if i == 2: title = "Science question Bank 2026 (Part 2 - Subjective)"
        elif i == 3: title = "Maths (Basic) question Bank 2026"
        elif i == 4: title = "Maths (Standard) question Bank 2026"
        elif i == 5: title = "Social Science question Bank 2026"
        elif i == 6: title = "English (FL) question Bank 2026"
        elif i == 7: title = "Gujarati (SL) question Bank 2026"
        
        json_data = {
            "metadata": {
                "id": ch_id,
                "title": title,
                "subject": "question Question Bank 2026",
                "grade": "10",
                "curriculum": ["GSEB", "NCERT", "CBSE"],
                "difficulty": "Advanced",
                "version": "4.0.0-question-BANK"
            },
            "blocks": [
                {
                    "type": "hook",
                    "content": "Welcome to the question Bank! This section is currently being parsed by the AI Swarm from the official PDF. Check back soon for the full interactive content!"
                }
            ]
        }
        with open(os.path.join(output_dir, f"{ch_id}.json"), "w") as f:
            json.dump(json_data, f, indent=2)
            
print("Generated placeholders for Ch2-Ch7.")
