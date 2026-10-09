import json

file_path = "app_core/chapters/ncert_class10_science_ch1.json"
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for block in data['blocks']:
    if block.get('id') == "KOBJ_NCERT_C10_SCI_CH1_021":
        block['image_url'] = "assets/images/science/exothermic_endothermic_reactions.png"
        block['caption'] = "Comparison of Exothermic and Endothermic Reactions"
        block['caption_hi'] = "ऊष्माक्षेपी और ऊष्माशोषी अभिक्रियाओं की तुलना"
        block['caption_gu'] = "ઉષ્માક્ષેપક અને ઉષ્માશોષક પ્રક્રિયાઓની સરખામણી"
        break

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Image added successfully!")
