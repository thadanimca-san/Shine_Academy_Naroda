import json
import os

chapters_dir = 'app_core/chapters/'

files_to_create = [
    {
        "id": "gseb_class10_science_mock_exam_1",
        "title": "Board Exam: Full Science Paper 1 (With Solutions)",
        "subject": "Science",
        "board": "GSEB",
        "type": "exam"
    },
    {
        "id": "ncert_class10_science_mock_exam_1",
        "title": "Board Exam: Full Science Paper 1 (With Solutions)",
        "subject": "Science",
        "board": "NCERT",
        "type": "exam"
    },
    {
        "id": "cbse_class10_deo_bank_2026_ch9",
        "title": "English (FL) DEO Bank (Part 1 - MCQs)",
        "subject": "English",
        "board": "CBSE",
        "type": "deo"
    },
    {
        "id": "cbse_class10_deo_bank_2026_ch10",
        "title": "English (FL) DEO Bank (Part 2 - Subject)",
        "subject": "English",
        "board": "CBSE",
        "type": "deo"
    },
    {
        "id": "cbse_class10_deo_bank_2026_ch11",
        "title": "Gujarati (SL) DEO Bank (Part 1 - MCQs)",
        "subject": "Gujarati",
        "board": "CBSE",
        "type": "deo"
    },
    {
        "id": "cbse_class10_deo_bank_2026_ch12",
        "title": "Gujarati (SL) DEO Bank (Part 2 - Subject)",
        "subject": "Gujarati",
        "board": "CBSE",
        "type": "deo"
    },
    {
        "id": "ncert_class10_deo_bank_2026_ch8",
        "title": "Social Science DEO Bank (Part 2 - Subject)",
        "subject": "Social Science",
        "board": "NCERT",
        "type": "deo"
    },
    {
        "id": "ncert_class10_deo_bank_2026_ch9",
        "title": "English (FL) DEO Bank (Part 1 - MCQs)",
        "subject": "English",
        "board": "NCERT",
        "type": "deo"
    },
    {
        "id": "ncert_class10_deo_bank_2026_ch10",
        "title": "English (FL) DEO Bank (Part 2 - Subject)",
        "subject": "English",
        "board": "NCERT",
        "type": "deo"
    },
    {
        "id": "ncert_class10_deo_bank_2026_ch11",
        "title": "Gujarati (SL) DEO Bank (Part 1 - MCQs)",
        "subject": "Gujarati",
        "board": "NCERT",
        "type": "deo"
    },
    {
        "id": "ncert_class10_deo_bank_2026_ch12",
        "title": "Gujarati (SL) DEO Bank (Part 2 - Subject)",
        "subject": "Gujarati",
        "board": "NCERT",
        "type": "deo"
    }
]

def generate_exam_blocks(ch_id):
    return [
        {
            "id": f"{ch_id.upper()}_EXAMTIPS_001",
            "type": "exam_tips",
            "title": "Mock Exam Strategy",
            "title_hi": "मॉक परीक्षा रणनीति",
            "body": "Read the entire paper in the first 15 minutes. Attempt the questions you are most confident about first.",
            "body_hi": "पहले १५ मिनट में पूरा पेपर पढ़ें। उन सवालों को पहले हल करें जिन पर आपको सबसे ज्यादा भरोसा हो।"
        },
        {
            "id": f"{ch_id.upper()}_MCQ_002",
            "type": "mcq",
            "question": "Which of the following is a balanced chemical equation?",
            "question_hi": "निम्नलिखित में से कौन सा एक संतुलित रासायनिक समीकरण है?",
            "options": [
                "Mg + O2 -> MgO",
                "2Mg + O2 -> 2MgO",
                "Mg + 2O2 -> 2MgO",
                "2Mg + O2 -> MgO"
            ],
            "options_hi": [
                "Mg + O2 -> MgO",
                "2Mg + O2 -> 2MgO",
                "Mg + 2O2 -> 2MgO",
                "2Mg + O2 -> MgO"
            ],
            "correct_index": 1,
            "explanation": "2Mg + O2 -> 2MgO has equal number of Mg and O atoms on both sides.",
            "explanation_hi": "2Mg + O2 -> 2MgO के दोनों तरफ Mg और O परमाणुओं की संख्या बराबर है।"
        }
    ]

def generate_deo_blocks(ch_id, title):
    return [
        {
            "id": f"{ch_id.upper()}_THEORY_001",
            "type": "theory",
            "title": "DEO Question Bank Overview",
            "title_hi": "DEO प्रश्न बैंक अवलोकन",
            "body": f"This chapter contains important questions from the {title}.",
            "body_hi": f"इस अध्याय में {title} के महत्वपूर्ण प्रश्न हैं।"
        },
        {
            "id": f"{ch_id.upper()}_PRACTICE_002",
            "type": "practice_question",
            "title": "Sample Question",
            "title_hi": "नमूना प्रश्न",
            "body": "Write a short note on the topic.",
            "body_hi": "विषय पर एक संक्षिप्त नोट लिखें।"
        }
    ]

for f_info in files_to_create:
    file_path = os.path.join(chapters_dir, f_info['id'] + '.json')
    data = {
        "metadata": {
            "id": f_info['id'],
            "title": f_info['title'],
            "subject": f_info['subject'],
            "grade": "10",
            "board": f_info['board']
        },
        "blocks": generate_exam_blocks(f_info['id']) if f_info['type'] == 'exam' else generate_deo_blocks(f_info['id'], f_info['title'])
    }
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Created {file_path}")

print("Successfully generated all 11 files.")
