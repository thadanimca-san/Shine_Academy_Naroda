import json

def fix_file(filepath, ch_num):
    with open(filepath, 'r') as f:
        data = json.load(f)
    if isinstance(data, list):
        new_data = {
            "metadata": {
                "id": f"gseb_class10_maths_ch{ch_num}_questions",
                "title": f"Chapter {ch_num}: Practice Test",
                "title_hi": f"अध्याय {ch_num}: अभ्यास टेस्ट",
                "title_gu": f"પ્રકરણ {ch_num}: પ્રેક્ટિસ ટેસ્ટ",
                "subject": "Maths",
                "grade": "10",
                "board": "GSEB/CBSE",
                "version": "1.0",
                "estimated_minutes": 60,
                "tags": ["maths", "practice"]
            },
            "blocks": data
        }
        with open(filepath, 'w') as f:
            json.dump(new_data, f, indent=2)
            f.write("\n")
        print(f"Fixed {filepath}")

fix_file("app_core/assessment/gseb_class10_maths_ch1_questions.json", 1)
fix_file("app_core/assessment/gseb_class10_maths_ch3_questions.json", 3)
