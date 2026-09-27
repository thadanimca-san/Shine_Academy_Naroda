import json

file_path = "app_core/learning_modules/gseb_class10_maths_ch2/blocks.json"

with open(file_path, "r", encoding="utf-8") as f:
    blocks = json.load(f)

new_blocks = [
  {
    "id": "KOBJ_C10_MATH_CH2_WORKED_002",
    "type": "worked_example",
    "title": "Exercise 2.2 Q1 (i)",
    "title_hi": "प्रश्नावली 2.2 प्रश्न 1 (i)",
    "body": "Find the zeroes of x² - 2x - 8 and verify the relationship.\n\nLet p(x) = x² - 2x - 8 = 0\nWe need two numbers that multiply to -8 and add to -2. The numbers are -4 and 2.\nx² - 4x + 2x - 8 = 0\nx(x - 4) + 2(x - 4) = 0\n(x - 4)(x + 2) = 0\nSo, x = 4 or x = -2. Zeroes are α = 4, β = -2.\n\nVerification: a=1, b=-2, c=-8\nSum = α+β = 4+(-2) = 2. Also -b/a = -(-2)/1 = 2.\nProduct = αβ = 4(-2) = -8. Also c/a = -8/1 = -8.",
    "body_hi": "x² - 2x - 8 के शून्यक ज्ञात कीजिए और संबंध की जाँच कीजिए।\n\nमाना p(x) = x² - 2x - 8 = 0\nहमें ऐसी संख्याएँ चाहिए जिनका गुणनफल -8 और योग -2 हो। संख्याएँ -4 और 2 हैं।\nx² - 4x + 2x - 8 = 0\nx(x - 4) + 2(x - 4) = 0\n(x - 4)(x + 2) = 0\nइसलिए, x = 4 या x = -2. शून्यक हैं α = 4, β = -2.\n\nजाँच: a=1, b=-2, c=-8\nयोग = α+β = 4+(-2) = 2. और -b/a = -(-2)/1 = 2.\nगुणनफल = αβ = 4(-2) = -8. और c/a = -8/1 = -8."
  },
  {
    "id": "KOBJ_C10_MATH_CH2_WORKED_003",
    "type": "worked_example",
    "title": "Exercise 2.2 Q1 (ii)",
    "title_hi": "प्रश्नावली 2.2 प्रश्न 1 (ii)",
    "body": "Find the zeroes of 4s² - 4s + 1.\n\nLet p(s) = 4s² - 4s + 1 = 0\nMultiply to 4, add to -4. The numbers are -2 and -2.\n4s² - 2s - 2s + 1 = 0\n2s(2s - 1) - 1(2s - 1) = 0\n(2s - 1)(2s - 1) = 0\nSo, s = 1/2 or s = 1/2. Zeroes are α = 1/2, β = 1/2.\n\nVerification: a=4, b=-4, c=1\nSum = 1/2 + 1/2 = 1. -b/a = -(-4)/4 = 1.\nProduct = (1/2) * (1/2) = 1/4. c/a = 1/4.",
    "body_hi": "4s² - 4s + 1 के शून्यक ज्ञात कीजिए।\n\nमाना p(s) = 4s² - 4s + 1 = 0\nगुणनफल 4 और योग -4 चाहिए। संख्याएँ -2 और -2 हैं।\n4s² - 2s - 2s + 1 = 0\n2s(2s - 1) - 1(2s - 1) = 0\n(2s - 1)(2s - 1) = 0\nइसलिए, s = 1/2 या s = 1/2. शून्यक हैं α = 1/2, β = 1/2.\n\nजाँच: a=4, b=-4, c=1\nयोग = 1/2 + 1/2 = 1. -b/a = -(-4)/4 = 1.\nगुणनफल = (1/2) * (1/2) = 1/4. c/a = 1/4."
  },
  {
    "id": "KOBJ_C10_MATH_CH2_WORKED_004",
    "type": "worked_example",
    "title": "Exercise 2.2 Q1 (iii)",
    "title_hi": "प्रश्नावली 2.2 प्रश्न 1 (iii)",
    "body": "Find the zeroes of 6x² - 3 - 7x.\n\nArrange in standard form: 6x² - 7x - 3 = 0\nMultiply to -18, add to -7. Numbers are -9 and 2.\n6x² - 9x + 2x - 3 = 0\n3x(2x - 3) + 1(2x - 3) = 0\n(2x - 3)(3x + 1) = 0\nSo, x = 3/2 or x = -1/3. Zeroes are α = 3/2, β = -1/3.\n\nVerification: a=6, b=-7, c=-3\nSum = 3/2 - 1/3 = 7/6. -b/a = -(-7)/6 = 7/6.\nProduct = (3/2)*(-1/3) = -3/6 = -1/2. c/a = -3/6 = -1/2.",
    "body_hi": "6x² - 3 - 7x के शून्यक ज्ञात कीजिए।\n\nमानक रूप में व्यवस्थित करें: 6x² - 7x - 3 = 0\nगुणनफल -18 और योग -7 चाहिए। संख्याएँ -9 और 2 हैं।\n6x² - 9x + 2x - 3 = 0\n3x(2x - 3) + 1(2x - 3) = 0\n(2x - 3)(3x + 1) = 0\nइसलिए, x = 3/2 या x = -1/3. शून्यक हैं α = 3/2, β = -1/3.\n\nजाँच: a=6, b=-7, c=-3\nयोग = 3/2 - 1/3 = 7/6. -b/a = -(-7)/6 = 7/6.\nगुणनफल = (3/2)*(-1/3) = -3/6 = -1/2. c/a = -3/6 = -1/2."
  },
  {
    "id": "KOBJ_C10_MATH_CH2_WORKED_005",
    "type": "worked_example",
    "title": "Exercise 2.2 Q2 - All Parts",
    "title_hi": "प्रश्नावली 2.2 प्रश्न 2 - सभी भाग",
    "body": "Find quadratic polynomials with given sum and product of zeroes. Formula: k[x² - (Sum)x + (Product)]\n\n(i) Sum=1/4, Product=-1\nk[x² - (1/4)x - 1] -> Multiply by 4 (k=4) -> 4x² - x - 4\n\n(ii) Sum=√2, Product=1/3\nk[x² - √2x + 1/3] -> Multiply by 3 (k=3) -> 3x² - 3√2x + 1\n\n(iii) Sum=0, Product=√5\n1[x² - 0x + √5] -> x² + √5\n\n(iv) Sum=1, Product=1\n1[x² - 1x + 1] -> x² - x + 1\n\n(v) Sum=-1/4, Product=1/4\nk[x² - (-1/4)x + 1/4] -> 4[x² + x/4 + 1/4] -> 4x² + x + 1\n\n(vi) Sum=4, Product=1\n1[x² - 4x + 1] -> x² - 4x + 1",
    "body_hi": "दिए गए शून्यकों के योग और गुणनफल वाले द्विघात बहुपद ज्ञात कीजिए। सूत्र: k[x² - (योग)x + (गुणनफल)]\n\n(i) योग=1/4, गुणनफल=-1\nk[x² - (1/4)x - 1] -> 4 से गुणा करें (k=4) -> 4x² - x - 4\n\n(ii) योग=√2, गुणनफल=1/3\nk[x² - √2x + 1/3] -> 3 से गुणा करें (k=3) -> 3x² - 3√2x + 1\n\n(iii) योग=0, गुणनफल=√5\n1[x² - 0x + √5] -> x² + √5\n\n(iv) योग=1, गुणनफल=1\n1[x² - 1x + 1] -> x² - x + 1\n\n(v) योग=-1/4, गुणनफल=1/4\nk[x² - (-1/4)x + 1/4] -> 4[x² + x/4 + 1/4] -> 4x² + x + 1\n\n(vi) योग=4, गुणनफल=1\n1[x² - 4x + 1] -> x² - 4x + 1"
  }
]

# Insert before the mastery block
mastery_idx = next(i for i, b in enumerate(blocks) if b.get('type') == 'mastery')
for b in reversed(new_blocks):
    blocks.insert(mastery_idx, b)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(blocks, f, indent=2, ensure_ascii=False)

print("Appended new practice blocks to blocks.json")
