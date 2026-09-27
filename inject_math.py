import json
import os

db_path = "app_core/learning_modules/master_curriculum.json"

with open(db_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

# Chapter 1: Real Numbers
db["cbse_class10_math_ch1"] = [
    {
        "type": "theory",
        "id": "cbse_class10_math_ch1_b1",
        "data": {
            "title": "Introduction to Real Numbers",
            "content": "Real numbers consist of rational numbers (like fractions and integers) and irrational numbers (like √2 and π). Every real number can be represented as a point on the number line."
        }
    },
    {
        "type": "worked_example",
        "id": "cbse_class10_math_ch1_b2",
        "data": {
            "title": "Example 1: Fundamental Theorem of Arithmetic",
            "problem": "Find the prime factorization of 140.",
            "given": "The number 140",
            "formula": "Express the number as a product of prime numbers.",
            "steps": [
                "140 = 2 × 70",
                "70 = 2 × 35",
                "35 = 5 × 7",
                "Therefore, 140 = 2 × 2 × 5 × 7"
            ],
            "answer": "140 = 2² × 5 × 7"
        }
    },
    {
        "type": "worked_example",
        "id": "cbse_class10_math_ch1_b3",
        "data": {
            "title": "Example 2: Finding LCM and HCF",
            "problem": "Find the LCM and HCF of 26 and 91 and verify that LCM × HCF = product of the two numbers.",
            "given": "Two numbers: a = 26, b = 91",
            "formula": "HCF × LCM = a × b",
            "steps": [
                "Prime factorization of 26 = 2 × 13",
                "Prime factorization of 91 = 7 × 13",
                "HCF is the smallest power of each common prime factor. Common factor is 13. So, HCF = 13",
                "LCM is the product of the greatest power of each prime factor. LCM = 2 × 7 × 13 = 182",
                "Verification: LCM × HCF = 182 × 13 = 2366",
                "Product of numbers: 26 × 91 = 2366"
            ],
            "answer": "HCF = 13, LCM = 182. Verified that 2366 = 2366."
        }
    }
]

# Chapter 2: Polynomials
db["cbse_class10_math_ch2"] = [
    {
        "type": "theory",
        "id": "cbse_class10_math_ch2_b1",
        "data": {
            "title": "Degree of a Polynomial",
            "content": "The highest power of x in p(x) is called the degree of the polynomial p(x).\nA polynomial of degree 1 is linear (e.g., 2x-3).\nA polynomial of degree 2 is quadratic (e.g., x²-5x+6)."
        }
    },
    {
        "type": "worked_example",
        "id": "cbse_class10_math_ch2_b2",
        "data": {
            "title": "Example 1: Finding Zeroes",
            "problem": "Find the zeroes of the quadratic polynomial x² + 7x + 10.",
            "given": "p(x) = x² + 7x + 10",
            "formula": "Set p(x) = 0 and factorize by splitting the middle term.",
            "steps": [
                "We need two numbers whose product is 10 and sum is 7. Those numbers are 5 and 2.",
                "x² + 5x + 2x + 10 = 0",
                "x(x + 5) + 2(x + 5) = 0",
                "(x + 2)(x + 5) = 0",
                "Therefore, x = -2 or x = -5"
            ],
            "answer": "The zeroes are -2 and -5."
        }
    }
]

# Chapter 3: Linear Equations
db["cbse_class10_math_ch3"] = [
    {
        "type": "theory",
        "id": "cbse_class10_math_ch3_b1",
        "data": {
            "title": "Pair of Linear Equations in Two Variables",
            "content": "An equation of the form ax + by + c = 0, where a, b, and c are real numbers, and a and b are not both zero, is a linear equation in two variables x and y.\nA pair of linear equations can have:\n1. A unique solution (intersecting lines)\n2. Infinitely many solutions (coincident lines)\n3. No solution (parallel lines)"
        }
    },
    {
        "type": "worked_example",
        "id": "cbse_class10_math_ch3_b2",
        "data": {
            "title": "Example 1: Substitution Method",
            "problem": "Solve the following pair of linear equations by substitution method: 7x - 15y = 2 and x + 2y = 3",
            "given": "Equation 1: 7x - 15y = 2\nEquation 2: x + 2y = 3",
            "formula": "Express one variable in terms of the other from one equation, and substitute in the other equation.",
            "steps": [
                "From Equation 2, express x: x = 3 - 2y",
                "Substitute x in Equation 1: 7(3 - 2y) - 15y = 2",
                "21 - 14y - 15y = 2",
                "-29y = 2 - 21",
                "-29y = -19",
                "y = 19/29",
                "Substitute y back into x = 3 - 2y",
                "x = 3 - 2(19/29) = 3 - 38/29 = (87 - 38)/29 = 49/29"
            ],
            "answer": "x = 49/29, y = 19/29"
        }
    }
]

with open(db_path, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print("Math injected successfully!")
