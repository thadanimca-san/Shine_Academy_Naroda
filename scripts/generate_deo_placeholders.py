import json
import os

output_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
prefixes = ['ncert', 'gseb', 'cbse']

for prefix in prefixes:
    for i in range(2, 8):
        ch_id = f"{prefix}_class10_deo_bank_2026_ch{i}"
        title = "DEO Bank 2026"
        if i == 2: title = "Science DEO Bank 2026 (Part 2 - Subjective)"
        elif i == 3: title = "Maths (Basic) DEO Bank 2026"
        elif i == 4: title = "Maths (Standard) DEO Bank 2026"
        elif i == 5: title = "Social Science DEO Bank 2026"
        elif i == 6: title = "English (FL) DEO Bank 2026"
        elif i == 7: title = "Gujarati (SL) DEO Bank 2026"
        
        json_data = {
            "metadata": {
                "id": ch_id,
                "title": title,
                "subject": "DEO Question Bank 2026",
                "grade": "10",
                "curriculum": ["GSEB", "NCERT", "CBSE"],
                "difficulty": "Advanced",
                "version": "4.0.0-DEO-BANK"
            },
            "blocks": [
                {
                    "type": "hook",
                    "content": "Welcome to the DEO Bank! This section is currently being parsed by the AI Swarm from the official PDF. Check back soon for the full interactive content!"
                }
            ]
        }
        with open(os.path.join(output_dir, f"{ch_id}.json"), "w") as f:
            json.dump(json_data, f, indent=2)
            
print("Generated placeholders for Ch2-Ch7.")
