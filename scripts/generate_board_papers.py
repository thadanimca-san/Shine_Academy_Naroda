import json
import os

papers_data = {
    "ncert_class10_board_papers_ch1": {
        "title": "Science - March 2023 (Solved)",
        "subject": "Board Papers",
        "hook": "Welcome to the official Gujarat Board (GSEB) Science Paper of March 2023! Let's solve the real paper together and see exactly how the board awards marks step-by-step.",
        "blocks": [
            {
                "type": "theory",
                "title": "Section A: Objective Type Questions",
                "content": "In Section A, you are required to answer 1-mark questions. These include MCQs, True/False, and Fill in the blanks. Let's test your knowledge on the actual questions asked in 2023."
            },
            {
                "type": "knowledge_check",
                "content": {
                    "question": "Which of the following is an example of an olfactory indicator?",
                    "options": ["Methyl orange", "Onion", "Litmus", "Phenolphthalein"],
                    "correct_answer": "Onion",
                    "explanation": "Correct! Onion and Vanilla are olfactory indicators because their smell changes in acidic or basic media."
                }
            },
            {
                "type": "knowledge_check",
                "content": {
                    "question": "An object is placed at the center of curvature (C) of a concave mirror. Where is the image formed?",
                    "options": ["At Focus (F)", "Between F and C", "At C", "Beyond C"],
                    "correct_answer": "At C",
                    "explanation": "When an object is placed at C, the image is also formed at C. It is real, inverted, and of the same size."
                }
            },
            {
                "type": "theory",
                "title": "Section B: 2-Mark Subjective Questions",
                "content": "Let's look at how to properly structure a 2-mark answer to ensure you get full marks.\n\n**Question 17:** What are amphoteric oxides? Give two examples of amphoteric oxides.\n\n**Step 1:** Define Amphoteric Oxides.\nMetal oxides which react with both acids as well as bases to produce salt and water are known as amphoteric oxides.\n\n**Step 2:** Give Examples.\n1. Aluminium Oxide (Al₂O₃)\n2. Zinc Oxide (ZnO)"
            },
            {
                "type": "teacher_tip",
                "content": "💯 **Marking Scheme:** The Board Examiner gives 1 mark for the correct definition and 1 mark for providing the two correct examples. If you only write the definition, you will only get 1 mark!"
            },
            {
                "type": "theory",
                "title": "Section C: 3-Mark Questions",
                "content": "**Question 27:** State Fleming's Left-Hand Rule. Explain its application in an electric motor.\n\n**Answer:**\n**Fleming's Left-Hand Rule:** Stretch the thumb, forefinger, and middle finger of your left hand such that they are mutually perpendicular. If the forefinger points in the direction of the magnetic field and the middle finger in the direction of current, then the thumb will point in the direction of motion or the force acting on the conductor.\n\n**Application:** In an electric motor, a rectangular coil is placed in a magnetic field. When current passes through it, the magnetic field exerts a force on the arms of the coil, causing it to rotate continuously."
            },
            {
                "type": "exam_tips",
                "content": "📝 **Exam Tip:** For 3-mark physics questions involving rules, drawing a small, neat diagram of the hand or the motor coil guarantees full marks even if your text explanation is slightly weak."
            }
        ]
    },
    "ncert_class10_board_papers_ch2": {
        "title": "Maths (Standard) - March 2023 (Solved)",
        "subject": "Board Papers",
        "hook": "Mathematics Standard 2023 Paper! Time to conquer theorems, quadratic equations, and trigonometry. Let's see how steps carry marks.",
        "blocks": [
            {
                "type": "theory",
                "title": "Section A: Objectives",
                "content": "Let's practice a real 1-mark question from the 2023 paper."
            },
            {
                "type": "knowledge_check",
                "content": {
                    "question": "If the roots of the quadratic equation x² - 4x + k = 0 are real and equal, find the value of k.",
                    "options": ["2", "4", "8", "-4"],
                    "correct_answer": "4",
                    "explanation": "For real and equal roots, Discriminant D = 0. So, b² - 4ac = 0 => (-4)² - 4(1)(k) = 0 => 16 - 4k = 0 => k = 4."
                }
            },
            {
                "type": "theory",
                "title": "Section C: 3-Mark Solution",
                "content": "**Question:** Prove that √5 is an irrational number.\n\n**Step 1: Assumption**\nLet us assume, to the contrary, that √5 is rational.\nThen √5 = a/b, where a and b are coprime integers and b ≠ 0.\n\n**Step 2: Squaring**\nSquaring both sides, we get 5 = a²/b²\n=> 5b² = a²  (Equation 1)\nThis means 5 divides a².\nTherefore, 5 divides a.\n\n**Step 3: Substitution**\nLet a = 5c for some integer c.\nSubstitute a in Eq 1:\n5b² = (5c)² => 5b² = 25c² => b² = 5c².\nThis means 5 divides b².\nTherefore, 5 divides b.\n\n**Step 4: Conclusion**\nSince 5 divides both a and b, they have a common factor 5. This contradicts the fact that a and b are coprime. Hence, our assumption is wrong, and √5 is irrational."
            },
            {
                "type": "teacher_tip",
                "content": "💯 **Marking Scheme:** 1 mark for the assumption, 1 mark for proving 5 divides 'a', and 1 mark for the final contradiction conclusion. Missing the final statement loses you 1 mark!"
            }
        ]
    },
    "ncert_class10_board_papers_ch3": {
        "title": "Social Science - March 2023 (Solved)",
        "subject": "Board Papers",
        "hook": "The 2023 Social Science paper required analytical thinking. Let's look at how to write long answers that impress the examiner.",
        "blocks": [
            {
                "type": "theory",
                "title": "Section A: MCQs",
                "content": "Let's test your historical knowledge with a real 2023 board question."
            },
            {
                "type": "knowledge_check",
                "content": {
                    "question": "Which of the following books was written by Megasthenes?",
                    "options": ["Arthashastra", "Indica", "Rajatarangini", "Geet Govind"],
                    "correct_answer": "Indica",
                    "explanation": "Megasthenes was a Greek ambassador who wrote 'Indica' describing India under Chandragupta Maurya."
                }
            },
            {
                "type": "theory",
                "title": "Section D: Long Answers (4 Marks)",
                "content": "**Question:** Explain the meaning of 'Globalisation' and describe any three of its impacts on Indian agriculture.\n\n**Answer:**\n**Meaning:** Globalisation means integrating the economy of a country with the world economy under conditions of free flow of trade, capital, and movement of persons across borders.\n\n**Impacts on Indian Agriculture:**\n1. **Export Opportunities:** Farmers can now sell their agricultural products (like spices, cotton, and tea) in international markets.\n2. **Advanced Technology:** Access to modern farming machinery, high-yielding variety (HYV) seeds, and advanced irrigation techniques.\n3. **Fierce Competition:** Indian farmers face tough competition from developed countries where agriculture is highly subsidized, making it harder for small farmers to survive."
            },
            {
                "type": "exam_tips",
                "content": "📝 **Exam Tip:** For 4-mark questions, always write the definition as the introduction (1 mark) and then provide 3 solid points with headings (3 marks). Underlining headings is highly recommended!"
            }
        ]
    },
    "ncert_class10_board_papers_ch4": {
        "title": "English (First Language) - March 2023 (Solved)",
        "subject": "Board Papers",
        "hook": "English 2023 focused heavily on unseen passages and grammar. Let's dive into the solved paper.",
        "blocks": [
            {
                "type": "theory",
                "title": "Section B: Grammar (Do as directed)",
                "content": "**Question:** The teacher said to the students, \"Do not make noise.\" (Change into Indirect Speech)\n\n**Answer:** The teacher forbade the students to make noise. \n*(OR)* The teacher ordered the students not to make noise."
            },
            {
                "type": "theory",
                "title": "Section C: Literature (2 Marks)",
                "content": "**Question:** Why was Lencho angry when he counted the money?\n\n**Answer:** Lencho had unwavering faith in God and had asked for 100 pesos. When he counted the money, he found only 70 pesos. He was confident that God could neither make a mistake nor deny him what he requested. Therefore, he became angry, assuming the post office employees had stolen the remaining 30 pesos."
            },
            {
                "type": "teacher_tip",
                "content": "💡 **Teacher Tip:** Notice how the answer mentions *both* parts: why he wasn't angry at God (unwavering faith) and who he blamed (post office employees). This ensures a full 2/2 score."
            }
        ]
    }
}

def main():
    prefixes = ['ncert', 'gseb', 'cbse']
    output_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
    os.makedirs(output_dir, exist_ok=True)
    
    for prefix in prefixes:
        for i in range(1, 5):
            # Read template data using the ncert key
            data_key = f"ncert_class10_board_papers_ch{i}"
            if data_key not in papers_data:
                continue
                
            data = papers_data[data_key]
            ch_id = f"{prefix}_class10_board_papers_ch{i}"
            
            blocks = []
            blocks.append({
                "type": "hook",
                "content": data["hook"]
            })
            
            blocks.extend(data["blocks"])
            
            json_data = {
                "metadata": {
                    "id": ch_id,
                    "title": data["title"],
                    "subject": data["subject"],
                    "grade": "10",
                    "curriculum": ["GSEB", "NCERT", "CBSE"],
                    "difficulty": "Advanced",
                    "version": "4.0.0-SOLVED-PAPER"
                },
                "blocks": blocks
            }
            
            with open(os.path.join(output_dir, f"{ch_id}.json"), "w") as f:
                json.dump(json_data, f, indent=2)
                
    print("Successfully generated Board Papers!")

if __name__ == "__main__":
    main()
