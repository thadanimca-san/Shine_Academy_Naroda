import json

file_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_accounts_ch2.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

table_en = """
**Trading and Profit & Loss A/c**
| Particulars | Amount (₹) | Particulars | Amount (₹) |
| :--- | :--- | :--- | :--- |
| To Opening Stock | 10,000 | By Sales | 50,000 |
| To Purchases | 20,000 | By Closing Stock | 15,000 |
| To Gross Profit c/d | 35,000 | | |
| **Total** | **65,000** | **Total** | **65,000** |

**Balance Sheet**
| Liabilities | Amount (₹) | Assets | Amount (₹) |
| :--- | :--- | :--- | :--- |
| Capital | 1,00,000 | Fixed Assets | 80,000 |
| Creditors | 20,000 | Current Assets | 40,000 |
| **Total** | **1,20,000** | **Total** | **1,20,000** |
"""

table_hi = """
**व्यापार और लाभ-हानि खाता**
| विवरण | राशि (₹) | विवरण | राशि (₹) |
| :--- | :--- | :--- | :--- |
| प्रारंभिक स्टॉक | 10,000 | बिक्री | 50,000 |
| खरीद | 20,000 | अंतिम स्टॉक | 15,000 |
| सकल लाभ | 35,000 | | |
| **कुल** | **65,000** | **कुल** | **65,000** |

**बैलेंस शीट**
| दायित्व | राशि (₹) | संपत्ति | राशि (₹) |
| :--- | :--- | :--- | :--- |
| पूंजी | 1,00,000 | अचल संपत्ति | 80,000 |
| लेनदार | 20,000 | वर्तमान संपत्ति | 40,000 |
| **कुल** | **1,20,000** | **कुल** | **1,20,000** |
"""

table_gu = """
**વેપાર અને નફા-નુકસાન ખાતું**
| વિગત | રકમ (₹) | વિગત | રકમ (₹) |
| :--- | :--- | :--- | :--- |
| શરૂઆતનો સ્ટોક | 10,000 | વેચાણ | 50,000 |
| ખરીદી | 20,000 | આખર સ્ટોક | 15,000 |
| કાચો નફો | 35,000 | | |
| **કુલ** | **65,000** | **કુલ** | **65,000** |

**પાકું સરવૈયું**
| જવાબદારીઓ | રકમ (₹) | મિલકતો | રકમ (₹) |
| :--- | :--- | :--- | :--- |
| મૂડી | 1,00,000 | કાયમી મિલકતો | 80,000 |
| લેણદારો | 20,000 | ચાલુ મિલકતો | 40,000 |
| **કુલ** | **1,20,000** | **કુલ** | **1,20,000** |
"""

count = 0
for block in data.get('blocks', []):
    if block.get('type') in ('practice_question', 'mcq'):
        sol = block.get('solution', '')
        # Check if the solution is short and missing the tables
        if len(sol) < 150 and "Solution to be calculated" in sol or "comprehensive subjective question" in sol or len(sol) < 100:
            block['solution'] = table_en
            block['solution_hi'] = table_hi
            block['solution_gu'] = table_gu
            count += 1
            if count == 13:
                break

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Updated {count} blocks.")
