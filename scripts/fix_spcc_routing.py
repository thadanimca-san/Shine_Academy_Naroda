import json
import os

def update_class11():
    file_path = 'app_core/curriculum/gseb_class11.json'
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Find SPCC subject
    for subject in data.get('subjects', []):
        if subject.get('id') == 'gseb_class11_spcc':
            # Update the chapters to match my generated ones
            subject['chapters'] = [
                {
                    "chapter_id": "gseb_class11_spcc_part1_ch3",
                    "title": "Part 1 Chapter 3: Physical Appearance of Business Letter",
                    "module_id": "gseb_class11_spcc_part1_ch3"
                },
                {
                    "chapter_id": "gseb_class11_spcc_part1_ch4",
                    "title": "Part 1 Chapter 4: Layout of Business Letter",
                    "module_id": "gseb_class11_spcc_part1_ch4"
                },
                {
                    "chapter_id": "gseb_class11_spcc_part1_ch5",
                    "title": "Part 1 Chapter 5: Inquiry Letters and their Replies",
                    "module_id": "gseb_class11_spcc_part1_ch5"
                },
                {
                    "chapter_id": "gseb_class11_spcc_part2_ch1",
                    "title": "Part 2 Chapter 1: Meaning and Types of Secretary",
                    "module_id": "gseb_class11_spcc_part2_ch1"
                },
                {
                    "chapter_id": "gseb_class11_spcc_part2_ch3",
                    "title": "Part 2 Chapter 3: Incorporation of a Company",
                    "module_id": "gseb_class11_spcc_part2_ch3"
                },
                {
                    "chapter_id": "gseb_class11_spcc_part2_ch4",
                    "title": "Part 2 Chapter 4: Memorandum of Association",
                    "module_id": "gseb_class11_spcc_part2_ch4"
                }
            ]
            break

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Class 11 updated.")

def update_class12():
    file_path = 'app_core/curriculum/gseb_class12_commerce.json'
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Check if SPCC is already there
    has_spcc = False
    for subject in data.get('subjects', []):
        if subject.get('id') == 'spcc':
            has_spcc = True
            break
            
    if not has_spcc:
        spcc_subject = {
            "id": "spcc",
            "name": "SPCC (Secretarial Practice)",
            "icon": "assignment",
            "color_hex": "0xFF9E9E9E",
            "chapters": [
                {
                    "chapter_number": 1,
                    "title": "Chapter 1: Bank Correspondence",
                    "module_id": "gseb_class12_spcc_ch1",
                    "is_available": True,
                    "status": "Available"
                },
                {
                    "chapter_number": 2,
                    "title": "Chapter 2: Correspondence with Government Departments",
                    "module_id": "gseb_class12_spcc_ch2",
                    "is_available": True,
                    "status": "Available"
                },
                {
                    "chapter_number": 3,
                    "title": "Chapter 3: Inter Departmental and Employee Related Correspondence",
                    "module_id": "gseb_class12_spcc_ch3",
                    "is_available": True,
                    "status": "Available"
                },
                {
                    "chapter_number": 4,
                    "title": "Chapter 4: Insurance Letters",
                    "module_id": "gseb_class12_spcc_ch4",
                    "is_available": True,
                    "status": "Available"
                },
                {
                    "chapter_number": 5,
                    "title": "Chapter 5: E-Communication",
                    "module_id": "gseb_class12_spcc_ch5",
                    "is_available": True,
                    "status": "Available"
                },
                {
                    "chapter_number": 6,
                    "title": "Chapter 6: Presentation Skills",
                    "module_id": "gseb_class12_spcc_ch6",
                    "is_available": True,
                    "status": "Available"
                },
                {
                    "chapter_number": 7,
                    "title": "Chapter 7: Issue of Shares",
                    "module_id": "gseb_class12_spcc_ch7",
                    "is_available": True,
                    "status": "Available"
                },
                {
                    "chapter_number": 8,
                    "title": "Chapter 8: Transfer and Transmission of Share",
                    "module_id": "gseb_class12_spcc_ch8",
                    "is_available": True,
                    "status": "Available"
                },
                {
                    "chapter_number": 9,
                    "title": "Chapter 9: Debenture",
                    "module_id": "gseb_class12_spcc_ch9",
                    "is_available": True,
                    "status": "Available"
                },
                {
                    "chapter_number": 10,
                    "title": "Chapter 10: Membership",
                    "module_id": "gseb_class12_spcc_ch10",
                    "is_available": True,
                    "status": "Available"
                },
                {
                    "chapter_number": 11,
                    "title": "Chapter 11: Directors of a Company",
                    "module_id": "gseb_class12_spcc_ch11",
                    "is_available": True,
                    "status": "Available"
                },
                {
                    "chapter_number": 12,
                    "title": "Chapter 12: The Meetings of the Company",
                    "module_id": "gseb_class12_spcc_ch12",
                    "is_available": True,
                    "status": "Available"
                },
                {
                    "chapter_number": 13,
                    "title": "Chapter 13: Dissolution of a Company",
                    "module_id": "gseb_class12_spcc_ch13",
                    "is_available": True,
                    "status": "Available"
                }
            ]
        }
        data['subjects'].append(spcc_subject)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("Class 12 updated.")
        
if __name__ == '__main__':
    update_class11()
    update_class12()
