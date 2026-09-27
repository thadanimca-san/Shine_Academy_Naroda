import os
import re
import json

def find_capitalized_words():
    dirs = ['lib', 'assets', 'raw_data', 'SAN']
    words = set()
    for d in dirs:
        for root, _, files in os.walk(d):
            for file in files:
                if file.endswith('.json') or file.endswith('.dart'):
                    path = os.path.join(root, file)
                    try:
                        with open(path, 'r', encoding='utf-8') as f:
                            text = f.read()
                            # Find Capitalized words that might be names
                            matches = re.findall(r'\b[A-Z][a-z]+\b', text)
                            words.update(matches)
                    except:
                        pass
    return words

words = find_capitalized_words()
# Basic filter for some common Muslim names
muslim_names = ["Ahmed", "Ali", "Mohammed", "Fatima", "Ayesha", "Abdul", "Imran", "Hassan", "Hussain", "Tariq", "Zainab", "Omar", "Usman", "Amir", "Bilal", "Zoya", "Sana", "Zeeshan", "Salman", "Aamir", "Saif", "Irfan", "Javed", "Shabana", "Azhar", "Shoaib", "Farhan", "Akhtar", "Zafar", "Iqbal", "Akbar", "Babar", "Siraj", "Sultan", "Begum", "Sheikh", "Syed", "Mirza", "Baig", "Khan", "Pathan", "Ansari", "Qureshi", "Rizvi", "Naqvi", "Siddiqui", "Alvi", "Afsana", "Ruksana", "Farida", "Hamid", "Rashid", "Majid", "Sajid", "Wajid", "Zahid", "Shahid", "Kareem", "Raheem", "Fahad", "Saad", "Zaid", "Taha", "Yaseen", "Musa", "Isa", "Haroon", "Yahya", "Yusuf", "Ibrahim", "Ismail", "Ishaq", "Yaqoob", "Ayyub", "Yunus", "Dawud", "Sulaiman", "Ilyas", "Alyasa", "Zakariya", "Arshad", "Aslam", "Akram", "Anwar", "Amjad", "Ajmal", "Akmal", "Ashraf", "Asghar", "Akbar", "Ameen", "Aman", "Arif", "Asif", "Atif", "Aaqib", "Aamir", "Aabid", "Aadil", "Aalim", "Aashiq", "Aarif", "Asim"]

found = []
for n in muslim_names:
    if n in words:
        found.append(n)

print("Found Muslim names:", found)
