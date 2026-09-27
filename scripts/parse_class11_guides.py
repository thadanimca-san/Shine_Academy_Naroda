import re
import json
import os
from cleaner_utils import clean_textbook_text

def extract_pearls_from_class11_guide(text, ch_title, subject):
    blocks = [
        {
            "type": "hook",
            "content": f"Welcome to '{ch_title}' in Class 11 {subject}! Let's dive straight into the most important concepts."
        }
    ]
    
    # In Commerce, summaries are often named "Summary", "Points to Remember", "Introduction"
    gist_match = re.search(r'(SUMMARY|POINTS TO REMEMBER|INTRODUCTION|GIST OF THE CHAPTER)(.*?)(?:QUESTIONS|EXERCISE|\Z)', text, re.DOTALL | re.IGNORECASE)
    
    if gist_match:
        gist_content = clean_textbook_text(gist_match.group(2)).strip()
        if len(gist_content) > 3000:
            gist_content = gist_content[:3000] + "...\n\n(Rest of the concepts available in class)"
            
        blocks.append({
            "type": "theory",
            "title": "Key Concepts (Guide Summary)",
            "content": gist_content
        })
    else:
        clean_text = clean_textbook_text(text)
        blocks.append({
            "type": "theory",
            "title": "Key Concepts",
            "content": clean_text[:1500] + "...\n\n(Detailed explanation available in class)"
        })
        
    blocks.append({
        "type": "knowledge_check",
        "content": {
            "question": f"Have you understood the key concepts of '{ch_title}'?",
            "options": [
                "Yes, perfectly.",
                "I need to review the summary.",
                "I need to read the textbook.",
                "All of the above."
            ],
            "correct_answer": "All of the above.",
            "explanation": "Understanding Class 11 Commerce requires focus!"
        }
    })
    
    return blocks

def parse_guide_chapter(txt_file, ch_id, ch_title, subject, output_dir):
    if not os.path.exists(txt_file):
        return

    with open(txt_file, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    if len(raw_text.strip()) < 100:
        return

    blocks = extract_pearls_from_class11_guide(raw_text, ch_title, subject)

    sub_id = subject.lower().replace(" ", "_")
    chapter_json = {
        "metadata": {
            "title": ch_title,
            "subject": subject,
            "grade": "11",
            "curriculum": ["GSEB", "NCERT", "CBSE"],
            "difficulty": "Intermediate",
            "version": "4.0.0"
        },
        "blocks": blocks
    }
    
    for prefix in ['ncert', 'gseb', 'cbse']:
        ch_json = dict(chapter_json)
        ch_json["metadata"]["id"] = f"{prefix}_class11_{sub_id}_ch{ch_id}"
        with open(os.path.join(output_dir, f"{ch_json['metadata']['id']}.json"), 'w') as f:
            json.dump(ch_json, f, indent=2)

if __name__ == "__main__":
    out_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
    
    # Class 11 Economics (11 chapters typically)
    eco_titles = ["Economics: An Introduction", "Fundamental Concepts and Terminologies", "Demand", "Supply", "Cost of Production and Concepts of Revenue", "Market", "Indian Economy", "Economic Reforms", "National Income", "Budget", "Economic Ideas"]
    for i in range(1, 12):
        txt_file = f'/home/ubuntu/Shine_Academy_Naroda/raw_data/class11/economics/ch{i}g.txt'
        parse_guide_chapter(txt_file, i, eco_titles[i-1], "Economics", out_dir)
        
    # Class 11 Accounts (Part 1 and 2 usually have around 11-12 chapters total, we'll do 11)
    acc_titles = ["Accounting and its Terminology", "Dual Effect of Transactions", "Introduction to GST", "Journal", "Accounting Equation", "Subsidiary Books", "Cash Book", "Journal Proper", "Ledger Posting", "Trial Balance", "Bank Reconciliation Statement"]
    for i in range(1, 12):
        txt_file = f'/home/ubuntu/Shine_Academy_Naroda/raw_data/class11/accounts/ch{i}g.txt'
        parse_guide_chapter(txt_file, i, acc_titles[i-1], "Accounts", out_dir)

    # Class 11 OC (Organization of Commerce)
    oc_titles = ["Nature, Purpose and Scope of Business", "Business Services 1", "Business Services 2", "Information Communication, E-Commerce and Outsourcing", "Forms of Business Organization 1", "Forms of Business Organization 2", "Public Sector, Private Sector and Global Enterprises", "Sources of Business Finance", "Internal Trade", "International Trade", "Social Responsibility of Business"]
    for i in range(1, 12):
        txt_file = f'/home/ubuntu/Shine_Academy_Naroda/raw_data/class11/oc/ch{i}g.txt'
        parse_guide_chapter(txt_file, i, oc_titles[i-1], "OC", out_dir)
        
    # Class 11 Statistics
    stat_titles = ["Collection of Data", "Presentation of Data", "Measures of Central Tendency", "Measures of Dispersion", "Skewness of Frequency Distribution", "Permutations, Combinations and Binomial Expansion", "Sampling Methods", "Function", "Geometric Progression", "Indices and Logarithm"]
    for i in range(1, 11):
        txt_file = f'/home/ubuntu/Shine_Academy_Naroda/raw_data/class11/statistics/ch{i}g.txt'
        # Pad titles list if i > len(stat_titles)
        title = stat_titles[i-1] if i <= len(stat_titles) else f"Chapter {i}"
        parse_guide_chapter(txt_file, i, title, "Statistics", out_dir)

    print("Cleaned and Parsed Guides (Moti) for Class 11 Commerce!")
