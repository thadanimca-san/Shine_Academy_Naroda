import json

all_blocks = []
for i in range(1, 13):
    with open(f"/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ch2_chunks/chunk_{i}.json", "r") as f:
        blocks = json.load(f)
        all_blocks.extend(blocks)

# Fix IDs to be sequential and uniform
for idx, block in enumerate(all_blocks):
    block["id"] = f"KOBJ_GSEB_CLASS12_ACCOUNTS_CH2_{idx+1:03d}"

chapter_data = {
    "metadata": {
        "id": "gseb_class12_accounts_ch2",
        "title": "Chapter 2: Final Accounts of Partnership Firm",
        "subject": "Accounts",
        "grade": "12",
        "language": "en, hi, gu"
    },
    "blocks": all_blocks
}

out_file = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_accounts_ch2.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(chapter_data, f, indent=2, ensure_ascii=False)

print(f"Merged successfully! Total blocks: {len(all_blocks)}. Size: {len(json.dumps(chapter_data))} bytes.")
