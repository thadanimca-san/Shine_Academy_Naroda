import json
import glob

hindi_mapping = {
    "Chapter 1: Prabhuji Tum Chandan Hum Pani": "पाठ १: प्रभुजी तुम चंदन हम पानी",
    "Chapter 2: Meera Ke Pad": "पाठ २: मीरा के पद",
    "Chapter 3: Savaiye": "पाठ ३: सवैये",
    "Chapter 4: Ek Kutta Aur Ek Maina": "पाठ ४: एक कुत्ता और एक मैना",
    "Chapter 5: Tota": "पाठ ५: तोता",
    "Chapter 6: Mahadevi Varma - Gilu": "पाठ ६: गिल्लू (महादेवी वर्मा)",
    "Chapter 7: Surdas Ke Pad": "पाठ ७: सूरदास के पद",
    "Chapter 8: Niti Ke Dohe": "पाठ ८: नीति के दोहे",
    "Chapter 9: Kutta Aur Parchhai": "पाठ ९: कुत्ता और परछाईं",
    "Chapter 10: Jeene Ki Kala": "पाठ १०: जीने की कला",
}

gujarati_mapping = {
    "Chapter 1: Morli": "પાઠ ૧: મોરલી",
    "Chapter 2: Vaishnavjan To Tene Kahiye": "પાઠ ૨: વૈષ્ણવજન તો તેને કહીએ",
    "Chapter 3: Shilvant Sadhune": "પાઠ ૩: શીલવંત સાધુને",
    "Chapter 4: Dikri": "પાઠ ૪: દીકરી",
    "Chapter 5: Vatanthi Viday Thata": "પાઠ ૫: વતનથી વિદાય થતાં",
    "Chapter 6: Boliye Na Kain": "પાઠ ૬: બોલીએ ના કાંઈ",
    "Chapter 7: Jeev Ma Jeev Aavyo": "પાઠ ૭: જીવમાં જીવ આવ્યો",
    "Chapter 8: Chopda Ni Indrajal": "પાઠ ૮: ચોપડાની ઇન્દ્રજાળ",
    "Chapter 9: Dhingli": "પાઠ ૯: ઢીંગલી",
    "Chapter 10: Bhukh Thi Ye Bhundi Bhikh": "પાઠ ૧૦: ભૂખથી યે ભૂંડી ભીખ",
}

files_to_update = [
    "app_core/curriculum/cbse_class10.json",
    "app_core/curriculum/gseb_class10.json",
    "app_core/curriculum/ncert_class10.json"
]

for file_path in files_to_update:
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        
        changed = False
        for s in data.get("subjects", []):
            if "hindi" in s["name"].lower():
                s["name"] = "हिन्दी (Second Language)"
                for ch in s["chapters"]:
                    if ch["title"] in hindi_mapping:
                        ch["title"] = hindi_mapping[ch["title"]]
                        changed = True
            elif "gujarati" in s["name"].lower():
                s["name"] = "ગુજરાતી (Second Language)"
                for ch in s["chapters"]:
                    if ch["title"] in gujarati_mapping:
                        ch["title"] = gujarati_mapping[ch["title"]]
                        changed = True
                        
        if changed:
            with open(file_path, "w") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Updated {file_path}")
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

