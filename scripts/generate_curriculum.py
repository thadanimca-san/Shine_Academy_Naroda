import json
import os

data = {
    "EVS": {
        1: {"title": "Super Senses", "fact1": "Dogs mark their area with urine", "fact2": "Ants leave a smell on the ground", "fact3": "Silkworms can find their female from many kilometres", "fact4": "Some birds have eyes on either side of their head"},
        2: {"title": "A Snake Charmer's Story", "fact1": "Kalbeliyas are snake charmers", "fact2": "Snakes are friends of farmers", "fact3": "Only four types of snakes are poisonous in India", "fact4": "Snakebite medicines are made from snake poison"},
        3: {"title": "From Tasting to Digesting", "fact1": "Digestion begins in the mouth", "fact2": "The stomach acts like a churner", "fact3": "Glucose drip gives instant energy", "fact4": "Different areas of the tongue taste different things"},
        4: {"title": "Mangoes Round the Year", "fact1": "Mamidi tandra is made from ripe mangoes", "fact2": "Glass jars are dried in the sun to prevent fungus", "fact3": "Food can be preserved by drying, pickling, and sweetening", "fact4": "Spoiled food changes smell, color, and texture"},
        5: {"title": "Seeds and Seeds", "fact1": "Seeds can travel by wind, water, and animals", "fact2": "Pitcher plants trap insects", "fact3": "Sprouted seeds are healthy", "fact4": "Velcro was inspired by seeds sticking to dog fur"}
    },
    "Maths": {
        1: {"title": "The Fish Tale", "fact1": "Whale sharks can be 18m long", "fact2": "One crore has seven zeros", "fact3": "Motorboats travel faster than log boats", "fact4": "Fish are dried to preserve them for longer"},
        2: {"title": "Shapes and Angles", "fact1": "A right angle measures 90 degrees", "fact2": "Angles less than 90 are acute", "fact3": "A straight angle is 180 degrees", "fact4": "Closed shapes have no open ends"},
        3: {"title": "How Many Squares?", "fact1": "Area of a rectangle is length times width", "fact2": "Perimeter is the total boundary length", "fact3": "A square has all equal sides", "fact4": "Different shapes can have the same area"},
        4: {"title": "Parts and Wholes", "fact1": "A fraction represents part of a whole", "fact2": "1/2 is equal to 2/4", "fact3": "Numerator is the top number in a fraction", "fact4": "Denominator shows total equal parts"},
        5: {"title": "Does it Look the Same?", "fact1": "A mirror half completes the full picture", "fact2": "Symmetry means both sides match perfectly", "fact3": "A half-turn rotates by 180 degrees", "fact4": "Some letters look same after a half-turn"}
    },
    "English": {
        1: {"title": "Ice-cream Man", "fact1": "The ice-cream man brings joy in summer", "fact2": "His cart is compared to a flower bed", "fact3": "He sells vanilla, chocolate, and strawberry", "fact4": "Children cluster around him like honeybees"},
        2: {"title": "Wonderful Waste", "fact1": "Avial was created in Travancore", "fact2": "The Maharaja ordered a grand feast", "fact3": "Vegetable scraps were used to make a new dish", "fact4": "Waste can be useful if we use our minds"},
        3: {"title": "Bamboo Curry", "fact1": "Santhal tribes eat bamboo curry", "fact2": "The mother-in-law cooked the door", "fact3": "He used a bamboo door to make curry", "fact4": "Bamboo shoot is edible, but bamboo wood is not"},
        4: {"title": "Flying Together", "fact1": "Geese lived in a tall tree", "fact2": "A creeper destroyed their safety", "fact3": "The wise old bird warned them", "fact4": "They pretended to be dead to escape the hunter"},
        5: {"title": "My Shadow", "fact1": "The shadow grows and shrinks", "fact2": "It follows the child everywhere", "fact3": "It is tallest in the morning", "fact4": "It seems to have no understanding of how children play"}
    },
    "Hindi": {
        1: {"title": "Raakh ki Rassi", "fact1": "Lonpogar was a minister of Tibet", "fact2": "His son was very innocent", "fact3": "A girl helped the son with sheep hair", "fact4": "The girl made a rope of ash"},
        2: {"title": "Faslon ke Tyohar", "fact1": "Makar Sankranti is a harvest festival", "fact2": "Different states celebrate it differently", "fact3": "Khichdi is eaten on this day", "fact4": "People fly kites in Gujarat"},
        3: {"title": "Khiloune Wala", "fact1": "The toy seller brings many toys", "fact2": "The child wants a sword or bow", "fact3": "He wants to become like Ram", "fact4": "The mother gives him money"},
        4: {"title": "Nanha Fankar", "fact1": "Keshav was a young stone carver", "fact2": "He was making bells", "fact3": "Emperor Akbar appreciated his art", "fact4": "Keshav learned from his father"},
        5: {"title": "Jahan Chah Wahan Raah", "fact1": "Ila Sachani could not use her hands", "fact2": "She learned embroidery with her feet", "fact3": "She did beautiful Kathiawari embroidery", "fact4": "Her strong will helped her succeed"}
    }
}

types = ['quiz', 'true_false', 'fill_blank', 'short_note']

output_json = {}

for subject, chapters in data.items():
    for ch_num, ch_info in chapters.items():
        module_id = f"ncert_class5_{subject.lower()}_ch{ch_num}_mock"
        chapter_questions = []
        for i in range(8):
            q_type = types[i % 4]
            # Cycle through the facts
            fact_index = (i % 4) + 1
            if i >= 4:
                # Slight variation for the second set of 4 questions
                fact_index = 4 - (i % 4)
            
            fact_key = f"fact{fact_index}"
            fact = ch_info[fact_key]
            
            q_id = f"Q_{subject}_{ch_num}_{i+1}"
            
            if q_type == 'quiz':
                text = f"Which of the following is an accurate fact about {ch_info['title']}?"
                ans = fact
                exp = f"In the chapter, it is explicitly mentioned that {fact}."
                dist = "Other options contradict the story."
            elif q_type == 'true_false':
                text = f"True or False: {fact}."
                ans = "True"
                exp = f"This is a stated fact in the chapter."
                dist = "False is incorrect because the chapter verifies this fact."
            elif q_type == 'fill_blank':
                # Remove last word to create a blank
                words = fact.split()
                if len(words) > 1:
                    blank_word = words[-1]
                    text = " ".join(words[:-1]) + " ______."
                else:
                    blank_word = fact
                    text = "______."
                ans = blank_word
                exp = f"The missing word is {blank_word}."
                dist = "Other words do not complete the factual statement."
            elif q_type == 'short_note':
                text = f"Explain the context of the following statement: '{fact}'"
                ans = f"This statement is a key point in {ch_info['title']}. It signifies important events or facts discussed in the lesson."
                exp = "A short note should cover the context and meaning of the statement."
                dist = "N/A"
            
            question = {
                "id": q_id,
                "chapter_id": f"CH{ch_num}",
                "topic_id": ch_info['title'],
                "type": q_type,
                "difficulty": "Beginner",
                "board": ["CBSE"],
                "marks": 2,
                "bloom_taxonomy": "Understanding",
                "keywords": [subject, "Class 5", ch_info['title']],
                "estimated_time_minutes": 3,
                "exam_frequency": "High",
                "question_text": text,
                "answer": ans,
                "explanation": exp,
                "distractor_rationale": dist,
                "ai_context": {
                    "learning_goal": f"To understand {ch_info['title']}",
                    "common_misconceptions": ["Misinterpreting the text"],
                    "hint": "Read the chapter summary."
                }
            }
            chapter_questions.append(question)
        
        output_json[module_id] = chapter_questions

os.makedirs('/home/ubuntu/.gemini/antigravity/brain/fec251e7-56c6-4b62-97ea-fb1fb0fb087d/scratch', exist_ok=True)
output_path = '/home/ubuntu/.gemini/antigravity/brain/fec251e7-56c6-4b62-97ea-fb1fb0fb087d/scratch/class5_curriculum.json'
with open(output_path, 'w') as f:
    json.dump(output_json, f, indent=4)
print(f"File created successfully at {output_path}")
