import json

configs = [
    {"ch": 6, "img": "cyclones_ch6.jpg", "title": "Anatomy of a Cyclone", "desc": "A cross-section of a cyclone showing the calm eye and high-speed winds."},
    {"ch": 7, "img": "particulate_ch7.jpg", "title": "The Particulate Nature of Matter", "desc": "A macro-zoom view of tightly packed, vibrating spherical particles in a solid."},
    {"ch": 8, "img": "elements_ch8.jpg", "title": "Elements vs Compounds", "desc": "Comparing pure gold atoms (element) to water molecules (compound)."},
    {"ch": 9, "img": "solutions_ch9.jpg", "title": "Forming a Solution", "desc": "A glowing blue solute crystal actively dissolving uniformly into a solvent."}
]

for conf in configs:
    filepath = f"/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/gseb_class8_science_ch{conf['ch']}/blocks.json"
    with open(filepath, 'r') as f:
        data = json.load(f)

    for block in data:
        if block.get("type") == "animated_diagram":
            block["type"] = "theory"
            block["title"] = block.get("content", {}).get("title", conf["title"])
            block["content"] = block.get("content", {}).get("description", conf["desc"])
            block["visual_url"] = f"assets/images/{conf['img']}"

    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

print("Updated Chapters 6, 7, 8, 9 with AI-generated images!")
