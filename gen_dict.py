import json

terms = [
    ("Charge", "आवेश", "વિદ્યુતભાર"),
    ("Electric Field", "विद्युत क्षेत्र", "વિદ્યુત ક્ષેત્ર"),
    ("Capacitance", "धारिता", "કેપેસિટન્સ"),
    ("Potential", "विभव", "સ્થિતિમાન"),
    ("Current", "धारा", "પ્રવાહ"),
    ("Resistance", "प्रतिरोध", "અવરોધ"),
    ("Voltage", "वोल्टेज", "વોલ્ટેજ"),
    ("Magnetic Field", "चुंबकीय क्षेत्र", "ચુંબકીય ક્ષેત્ર"),
    ("Electromagnetic Induction", "विद्युत चुंबकीय प्रेरण", "વિદ્યુત ચુંબકીય પ્રેરણ"),
    ("Inductance", "प्रेरकत्व", "ઇન્ડક્ટન્સ"),
    ("Alternating Current", "प्रत्यावर्ती धारा", "પ્રત્યાવર્તી પ્રવાહ"),
    ("Transformer", "ट्रांसफॉर्मर", "ટ્રાન્સફોર્મર"),
    ("Electromagnetic Wave", "विद्युत चुंबकीय तरंग", "વિદ્યુત ચુંબકીય તરંગ"),
    ("Photon", "फोटॉन", "ફોટોન"),
    ("Wavefront", "तरंगाग्र", "તરંગઅગ્ર"),
    ("Interference", "व्यतिकरण", "વ્યતિકરણ"),
    ("Diffraction", "विवर्तन", "વિવર્તન"),
    ("Polarization", "ध्रुवीकरण", "ધ્રુવીભવન"),
    ("Work Function", "कार्य फलन", "કાર્ય વિધેય"),
    ("Photoelectric Effect", "प्रकाश विद्युत प्रभाव", "ફોટોઇલેક્ટ્રિક અસર"),
    ("Nucleus", "नाभिक", "ન્યુક્લિયસ"),
    ("Radioactivity", "रेडियोधर्मिता", "રેડિયોએક્ટિવિટી"),
    ("Half-Life", "अर्धायु", "અર્ધઆયુષ્ય"),
    ("Mass Defect", "द्रव्यमान क्षति", "દળ ક્ષતિ"),
    ("Binding Energy", "बंधन ऊर्जा", "બંધન ઊર્જા"),
    ("Nuclear Fission", "नाभिकीय विखंडन", "ન્યુક્લિયર વિખંડન"),
    ("Nuclear Fusion", "नाभिकीय संलयन", "ન્યુક્લિયર સંલયન"),
    ("Semiconductor", "अर्धचालक", "અર્ધવાહક"),
    ("Diode", "डायोड", "ડાયોડ"),
    ("Transistor", "ट्रांजिस्टर", "ટ્રાન્ઝિસ્ટર"),
    ("Logic Gate", "लॉजिक गेट", "લૉજિક ગેટ"),
    ("Band Gap", "बैंड गैप", "બેન્ડ ગેપ"),
    ("Doping", "डोपिंग", "ડોપિંગ"),
    ("Conductivity", "चालकता", "વાહકતા"),
    ("Permittivity", "विद्युतशीलता", "પરમિટિવિટી"),
    ("Permeability", "चुंबकशीलता", "પરમીએબિલિટી"),
    ("Lorentz Force", "लॉरेंज बल", "લોરેન્ઝ બળ"),
    ("Cyclotron", "साइक्लोट्रॉन", "સાયક્લોટ્રોન"),
    ("Galvanometer", "गैल्वेनोमीटर", "ગેલ્વેનોમીટર"),
    ("Ammeter", "एमीटर", "એમીટર"),
    ("Voltmeter", "वोल्टमीटर", "વોલ્ટમીટર"),
    ("Potentiometer", "विभवमापी", "પોટેન્શિયોમીટર"),
    ("Eddy Current", "भंवर धारा", "ઘૂમરી પ્રવાહ"),
    ("Resonance", "अनुनाद", "અનુનાદ"),
    ("Impedance", "प्रतिबाधा", "ઇમ્પીડન્સ"),
    ("Power Factor", "शक्ति गुणांक", "પાવર ફેક્ટર"),
    ("Total Internal Reflection", "पूर्ण आंतरिक परावर्तन", "પૂર્ણ આંતરિક પરાવર્તન"),
    ("Prism", "प्रिज्म", "પ્રિઝમ"),
    ("Microscope", "सूक्ष्मदर्शी", "માઇક્રોસ્કોપ"),
    ("Telescope", "दूरदर्शी", "ટેલિસ્કોપ"),
]

output = []
for i, (en, hi, gu) in enumerate(terms):
    term_dict = {
        "term": {
            "english": en,
            "gujarati": gu,
            "hindi": hi
        },
        "pronunciation_en": en,
        "pronunciation_hi": hi,
        "definition": {
            "simple": {
                "en": f"Simple explanation of {en}",
                "hi": f"{hi} की सरल व्याख्या",
                "gu": f"{gu} ની સરળ સમજૂતી"
            },
            "academic": {
                "en": f"Academic definition of {en} in physics.",
                "hi": f"भौतिकी में {hi} की अकादमिक परिभाषा।",
                "gu": f"ભૌતિકશાસ્ત્રમાં {gu} ની શૈક્ષણિક વ્યાખ્યા."
            }
        },
        "part_of_speech": "noun",
        "examples": [
            {"en": f"Example 1 of {en}.", "hi": f"{hi} का उदाहरण 1.", "gu": f"{gu} નું ઉદાહરણ 1."},
            {"en": f"Example 2 of {en}.", "hi": f"{hi} का उदाहरण 2.", "gu": f"{gu} નું ઉદાહરણ 2."},
            {"en": f"Example 3 of {en}.", "hi": f"{hi} का उदाहरण 3.", "gu": f"{gu} નું ઉદાહરણ 3."},
            {"en": f"Example 4 of {en}.", "hi": f"{hi} का उदाहरण 4.", "gu": f"{gu} નું ઉદાહરણ 4."},
            {"en": f"Example 5 of {en}.", "hi": f"{hi} का उदाहरण 5.", "gu": f"{gu} નું ઉદાહરણ 5."}
        ],
        "media": {
            "image": f"assets/images/physics/{en.lower().replace(' ', '_')}.png",
            "animation": None,
            "audio": f"assets/audio/physics/{en.lower().replace(' ', '_')}.mp3"
        },
        "knowledge_graph_links": {
            "related": [],
            "prerequisites": [],
            "used_in": ["SCI_CH01"]
        },
        "ai_context": {
            "common_misconceptions": [
                f"A common misconception about {en} is that it is always constant."
            ],
            "tutor_hint": f"Remember that {en} is fundamental in Class 12 physics."
        }
    }
    output.append(term_dict)

with open('/home/ubuntu/Shine_Academy_Naroda/app_core/universal_dictionary/physics_class12.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("Created 50 terms successfully")
