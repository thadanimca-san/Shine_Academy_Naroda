import subprocess
import time
import os

SYLLABUS = {
    "Physics": [
        "Electrostatic Potential and Capacitance",
        "Current Electricity",
        "Moving Charges and Magnetism",
        "Magnetism and Matter",
        "Electromagnetic Induction",
        "Alternating Current",
        "Electromagnetic Waves",
        "Ray Optics and Optical Instruments",
        "Wave Optics",
        "Dual Nature of Radiation and Matter",
        "Atoms",
        "Nuclei",
        "Semiconductor Electronics"
    ],
    "Chemistry": [
        "Solutions",
        "Electrochemistry",
        "Chemical Kinetics",
        "d and f Block Elements",
        "Coordination Compounds",
        "Haloalkanes and Haloarenes",
        "Alcohols, Phenols and Ethers",
        "Aldehydes, Ketones and Carboxylic Acids",
        "Amines",
        "Biomolecules"
    ],
    "Maths": [
        "Relations and Functions",
        "Inverse Trigonometric Functions",
        "Matrices",
        "Determinants",
        "Continuity and Differentiability",
        "Application of Derivatives",
        "Integrals",
        "Application of Integrals",
        "Differential Equations",
        "Vector Algebra",
        "Three Dimensional Geometry",
        "Linear Programming",
        "Probability"
    ],
    "Biology": [
        "Sexual Reproduction in Flowering Plants",
        "Human Reproduction",
        "Reproductive Health",
        "Principles of Inheritance and Variation",
        "Molecular Basis of Inheritance",
        "Evolution",
        "Human Health and Disease",
        "Microbes in Human Welfare",
        "Biotechnology Principles and Processes",
        "Biotechnology and its Applications",
        "Organisms and Populations",
        "Ecosystem",
        "Biodiversity and Conservation"
    ],
    "Accountancy": [
        "Accounting for Partnership Firms Fundamentals",
        "Goodwill Nature and Valuation",
        "Change in Profit Sharing Ratio",
        "Admission of a Partner",
        "Retirement of a Partner",
        "Death of a Partner",
        "Dissolution of a Partnership Firm",
        "Accounting for Share Capital",
        "Accounting for Debentures",
        "Financial Statements of a Company",
        "Financial Statement Analysis",
        "Accounting Ratios",
        "Cash Flow Statement"
    ],
    "Business_Studies": [
        "Nature and Significance of Management",
        "Principles of Management",
        "Business Environment",
        "Planning",
        "Organising",
        "Staffing",
        "Directing",
        "Controlling",
        "Financial Management",
        "Financial Markets",
        "Marketing Management",
        "Consumer Protection"
    ],
    "Economics": [
        "National Income and Related Aggregates",
        "Money and Banking",
        "Determination of Income and Employment",
        "Government Budget and the Economy",
        "Balance of Payments",
        "Indian Economy on the Eve of Independence",
        "Indian Economy 1950 to 1990",
        "Economic Reforms Since 1991",
        "Human Capital Formation in India",
        "Rural Development",
        "Employment Growth",
        "Environment and Sustainable Development",
        "Comparative Development Experiences"
    ]
}

def generate_all():
    print("Starting massive generation of CBSE Class 12 Science and Commerce...")
    for subject, chapters in SYLLABUS.items():
        # Physics chapter 1 was already done
        start_idx = 2 if subject == "Physics" else 1
        
        for idx, title in enumerate(chapters, start=start_idx):
            chapter_num = idx
            print(f"\n=======================================================")
            print(f"Generating {subject} Chapter {chapter_num}: {title}")
            print(f"=======================================================")
            
            # Use subprocess to call the generate script
            cmd = [
                "python3",
                "scripts/generate_gold_content.py",
                "--board", "CBSE",
                "--grade", "12",
                "--subject", subject,
                "--chapter_num", str(chapter_num),
                "--chapter_title", title
            ]
            
            try:
                # Run the command and stream output
                subprocess.run(cmd, check=True)
                print(f"✅ Successfully completed {subject} Chapter {chapter_num}")
            except subprocess.CalledProcessError as e:
                print(f"❌ ERROR: Generation failed for {subject} Chapter {chapter_num}.")
                print(f"Exiting script so you can check API limits.")
                return
            
            # Sleep a bit to be nice to the API
            time.sleep(5)

if __name__ == "__main__":
    generate_all()
