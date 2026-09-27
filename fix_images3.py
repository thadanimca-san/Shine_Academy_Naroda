import json

configs = [
    {"ch": 10, "img": "light_ch10.jpg", "title": "Light and Lenses", "desc": "A laser beam converging perfectly off a concave mirror."},
    {"ch": 11, "img": "time_ch11.jpg", "title": "Ancient Timekeeping", "desc": "A sundial casting a sharp shadow under the sun, with moon phases above."},
    {"ch": 12, "img": "harmony_ch12.jpg", "title": "A Natural Ecosystem", "desc": "Energy flowing from the Sun to plants, herbivores, predators, and decomposers."},
    {"ch": 13, "img": "earth_ch13.jpg", "title": "Our Planet Earth", "desc": "A cutaway cross-section of Earth showing the Lithosphere, Hydrosphere, and Atmosphere."}
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

print("Updated Chapters 10, 11, 12, 13 with AI-generated images!")
