import json
import os

curriculum_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum'

# Define standard chapters
chapters = {
    "class6": {
        "science": [
            "Food: Where does it come from?", "Components of Food", "Fibre to Fabric", "Sorting Materials into Groups",
            "Separation of Substances", "Changes Around Us", "Getting to Know Plants", "Body Movements",
            "The Living Organisms and Their Surroundings", "Motion and Measurement of Distances", 
            "Light, Shadows and Reflections", "Electricity and Circuits", "Fun with Magnets", "Water", 
            "Air Around Us", "Garbage In, Garbage Out"
        ]
    },
    "class5": {
        "evs": [
            "Super Senses", "A Snake Charmer's Story", "From Tasting to Digesting", "Mangoes Round the Year",
            "Seeds and Seeds", "Every Drop Counts", "Experiments with Water", "A Treat for Mosquitoes",
            "Up You Go!", "Walls Tell Stories", "Sunita in Space", "What if it Finishes...?",
            "A Shelter so High!", "When the Earth Shook!", "Blow Hot, Blow Cold", "Who will do this Work?",
            "Across the Wall", "No Place for Us?", "A Seed tells a Farmer's Story", "Whose Forests?", "Like Father, Like Daughter"
        ]
    },
    "class4": {
        "evs": [
            "Going to School", "Ear to Ear", "A Day with Nandu", "The Story of Amrita", "Anita and the Honeybees",
            "Omana's Journey", "From the Window", "Reaching Grandmother's House", "Changing Families", 
            "Hu Tu Tu, Hu Tu Tu", "The Valley of Flowers", "Changing Times", "A River's Tale", "Basva's Farm",
            "From Market to Home", "A Busy Month", "Nandita in Mumbai", "Too Much Water, Too Little Water", 
            "Abdul in the Garden", "Eating Together", "Food and Fun", "The World in my Home", "Pochampalli",
            "Home and Abroad", "Spicy Riddles", "Defence Officer: Wahida", "Chuskit Goes to School"
        ]
    },
    "class3": {
        "evs": [
            "Poonam's Day Out", "The Plant Fairy", "Water O' Water!", "Our First School", "Chhotu's House",
            "Foods We Eat", "Saying without Speaking", "Flying High", "It's Raining", "What is Cooking",
            "From Here to There", "Work We Do", "Sharing Our Feelings", "The Story of Food", "Making Pots",
            "Games We Play", "Here comes a Letter", "A House Like This", "Our Friends - Animals",
            "Drop by Drop", "Families can be Different", "Left-Right", "A Beautiful Cloth", "Web of Life"
        ]
    },
    "class2": {
        "evs": [
            "My Body", "My Family", "Food", "Water", "Shelter", "Clothes", "Air", "Cleanliness and Health",
            "Safety Rules", "Neighbourhood", "Festivals", "Plants Around Us", "Animals Around Us", "Transport",
            "Communication", "Earth and Sky", "Time and Directions"
        ]
    },
    "class1": {
        "evs": [
            "About Me", "My Body", "My Family", "My Home", "My School", "Food We Eat", "Water", "Clothes We Wear",
            "Air", "Keeping Clean and Healthy", "Safety Habits", "People Who Help Us", "Festivals", "Plants",
            "Animals", "Transport", "The Sky Above Us"
        ]
    }
}

for class_id, subjects in chapters.items():
    file_path = os.path.join(curriculum_dir, f"{class_id}.json")
    if not os.path.exists(file_path):
        print(f"Missing {file_path}")
        continue
        
    with open(file_path, 'r') as f:
        data = json.load(f)
        
    for subj_id, ch_list in subjects.items():
        # Find the subject in the curriculum
        target_subject = None
        for s in data.get('subjects', []):
            # Check if it's science or evs (EVS might be id "evs" or name "EVS")
            if s['id'] == subj_id or s['name'].lower() == subj_id:
                target_subject = s
                break
                
        if target_subject:
            # Rebuild the chapters array
            target_subject['chapters'] = []
            for i, title in enumerate(ch_list):
                module_prefix = f"gseb_{class_id}" if "gseb" in data.get("curriculum_id", "") else class_id
                target_subject['chapters'].append({
                    "chapter_number": i + 1,
                    "title": title,
                    "module_id": f"{module_prefix}_{subj_id}_ch{i + 1}",
                    "is_available": True,
                    "status": "Available"
                })
            print(f"Updated {class_id} -> {subj_id} with {len(ch_list)} chapters.")
        else:
            print(f"Warning: Subject {subj_id} not found in {class_id}.json")
            
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

print("Curriculum update complete.")
