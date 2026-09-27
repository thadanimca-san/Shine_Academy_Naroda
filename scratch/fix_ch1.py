import json
import re

file_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/cbse_class10_maths_ch1.json'
out_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch1.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Update ID
data['id'] = 'ncert_class10_maths_ch1'

muslim_names = ['Sana', 'Irfan', 'Farhan', 'Sheikh', 'Farida', 'Zaid', 'Yusuf', 'Aman', 'Ahmed', 'Ali', 'Fatima', 'Salma', 'Modemian', 'Muslim', 'Sohail', 'Rizwan', 'Ayesha', 'Imran', 'Tariq', 'Zainab', 'Omar', 'Usman']
approved_names = ['Dwija', 'Vedant', 'Chahat', 'Vivek', 'Pranav', 'Maahi', 'Samarth', 'Parv', 'Bhavya', 'Priyanshi', 'Ishani', 'Aahna', 'Anju', 'Dev', 'Dhruvi', 'Janvi', 'Jaymin', 'Krishna', 'Nandini', 'Prachi', 'Swati', 'Trisha', 'Aarva', 'Aarvi', 'Atharva', 'Bhagyaraj', 'Jenny', 'Jiansh', 'Nitya', 'Pranshu', 'Purv', 'Riansh', 'Roshni', 'Sanvi', 'Tirth', 'Twesha', 'Vrishti', 'Yashwardhan']

def replace_text(text):
    if not isinstance(text, str):
        return text
    # Replace DEO
    text = re.sub(r'\bDEO Office\b', 'Board Preparations', text, flags=re.IGNORECASE)
    text = re.sub(r'\bDEO\b', 'Board', text, flags=re.IGNORECASE)
    
    # Replace names
    for i, name in enumerate(muslim_names):
        replacement = approved_names[i % len(approved_names)]
        text = re.sub(rf'\b{name}\b', replacement, text, flags=re.IGNORECASE)
    return text

def process_dict(d):
    for k, v in list(d.items()):
        if k == 'is_deo_challenge':
            d['is_board_challenge'] = v
            del d[k]
        elif isinstance(v, str):
            d[k] = replace_text(v)
        elif isinstance(v, list):
            d[k] = [process_dict(item) if isinstance(item, dict) else replace_text(item) for item in v]
        elif isinstance(v, dict):
            process_dict(v)
    return d

data = process_dict(data)

with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Fixed and saved to", out_path)
