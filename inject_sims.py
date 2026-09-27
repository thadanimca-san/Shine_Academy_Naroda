import json
import os

simulations = {
    "gseb_class10_science_ch2.json": [
        {
            "type": "animated_diagram",
            "id": "SCI_CH2_ANIM_1",
            "difficulty": "Intermediate",
            "bloom": "Understand",
            "content": {
                "title": "The Color Changing Magic",
                "title_hi": "रंग बदलने का जादू",
                "title_gu": "રંગ બદલવાનો જાદુ",
                "description": "Animation showing drops of a mysterious juice falling into an acid and turning red, then falling into a base and turning blue.",
                "description_hi": "एनीमेशन में एक रहस्यमय रस की बूंदें एक अम्ल (acid) में गिरकर लाल हो जाती हैं, और फिर एक क्षार (base) में गिरकर नीली हो जाती हैं।",
                "description_gu": "એનિમેશનમાં એક રહસ્યમય રસનાં ટીપાં એસિડમાં પડીને લાલ થાય છે, અને પછી બેઝમાં પડીને ભૂરા થાય છે.",
                "paths": []
            }
        },
        {
            "type": "animated_diagram",
            "id": "SCI_CH2_ANIM_2",
            "difficulty": "Intermediate",
            "bloom": "Understand",
            "content": {
                "title": "The Neutralization Battle",
                "title_hi": "उदासीनीकरण की लड़ाई",
                "title_gu": "તટસ્થીકરણની લડાઈ",
                "description": "Animation showing red acid particles and blue base particles colliding and turning into harmless white salt crystals and water droplets.",
                "description_hi": "एनीमेशन में लाल अम्ल के कण और नीले क्षार के कण आपस में टकराकर हानिरहित सफेद नमक के क्रिस्टल और पानी की बूंदों में बदल जाते हैं।",
                "description_gu": "એનિમેશનમાં લાલ એસિડના કણો અને ભૂરા બેઝના કણો એકબીજા સાથે ટકરાઈને હાનિરહિત સફેદ મીઠાના સ્ફટિકો અને પાણીના ટીપાંમાં ફેરવાય છે.",
                "paths": []
            }
        },
        {
            "type": "animated_diagram",
            "id": "SCI_CH2_ANIM_3",
            "difficulty": "Intermediate",
            "bloom": "Understand",
            "content": {
                "title": "Calming the Acid Fire",
                "title_hi": "अम्ल की आग को शांत करना",
                "title_gu": "એસિડની આગ શાંત કરવી",
                "description": "Animation showing an irritated stomach full of red acid. A blue antacid pill enters, neutralizes the acid, and the stomach smiles.",
                "description_hi": "एनीमेशन में लाल अम्ल से भरा एक परेशान पेट दिखाया गया है। एक नीली एंटासिड गोली प्रवेश करती है, अम्ल को निष्क्रिय करती है, और पेट मुस्कुराता है।",
                "description_gu": "એનિમેશનમાં લાલ એસિડથી ભરેલું એક પરેશાન પેટ દર્શાવવામાં આવ્યું છે. એક ભૂરી એન્ટાસિડ ગોળી પ્રવેશે છે, એસિડને તટસ્થ કરે છે, અને પેટ સ્મિત કરે છે.",
                "paths": []
            }
        }
    ],
    "gseb_class10_science_ch5.json": [
        {
            "type": "animated_diagram",
            "id": "SCI_CH5_ANIM_1",
            "difficulty": "Intermediate",
            "bloom": "Understand",
            "content": {
                "title": "Energy Factory in the Cell",
                "title_hi": "कोशिका में ऊर्जा कारखाना",
                "title_gu": "કોષમાં ઊર્જાનું કારખાનું",
                "description": "An animation showing a piece of food (glucose) and oxygen entering a cell, then a small explosion of energy being released along with water and carbon dioxide.",
                "description_hi": "एक एनीमेशन जो भोजन (ग्लूकोज) के एक टुकड़े और ऑक्सीजन को एक कोशिका में प्रवेश करते हुए दिखाता है, फिर पानी और कार्बन डाइऑक्साइड के साथ ऊर्जा का एक छोटा सा विस्फोट होता है।",
                "description_gu": "એક એનિમેશન જે ખોરાક (ગ્લુકોઝ) ના ટુકડા અને ઓક્સિજનને કોષમાં પ્રવેશતા દર્શાવે છે, ત્યારબાદ પાણી અને કાર્બન ડાયોક્સાઇડ સાથે ઊર્જાનો નાનો વિસ્ફોટ થાય છે.",
                "paths": []
            }
        }
    ],
    "gseb_class10_science_ch8.json": [
        {
            "type": "animated_diagram",
            "id": "SCI_CH8_ANIM_1",
            "difficulty": "Intermediate",
            "bloom": "Understand",
            "content": {
                "title": "Discovery: The Blueprint of Life",
                "title_hi": "खोज: जीवन का खाका",
                "title_gu": "શોધ: જીવનની બ્લુપ્રિન્ટ",
                "description": "Just like a builder uses a blueprint to build a house, our bodies have a hidden blueprint passed down from our parents. This diagram represents how traits from a mother and father combine in a child.",
                "description_hi": "जिस तरह एक बिल्डर घर बनाने के लिए ब्लूप्रिंट का उपयोग करता है, उसी तरह हमारे शरीर में हमारे माता-पिता से प्राप्त एक छिपा हुआ ब्लूप्रिंट होता है। यह आरेख दर्शाता है कि एक बच्चे में माता और पिता के लक्षण कैसे मिलते हैं।",
                "description_gu": "જેમ ઘર બનાવવા માટે બિલ્ડર બ્લુપ્રિન્ટનો ઉપયોગ કરે છે, તેમ આપણા શરીરમાં આપણા માતાપિતા પાસેથી વારસામાં મળેલ છુપાયેલ બ્લુપ્રિન્ટ હોય છે. આ આકૃતિ દર્શાવે છે કે બાળકમાં માતા અને પિતાના લક્ષણો કેવી રીતે જોડાય છે.",
                "paths": ["M 100,50 L 150,100 L 200,50","M 150,100 L 150,180","M 150,180 m -30, 0 a 30,30 0 1,0 60,0 a 30,30 0 1,0 -60,0"]
            }
        }
    ],
    "gseb_class10_science_ch9.json": [
        {
            "type": "animated_diagram",
            "id": "SCI_CH9_ANIM_1",
            "difficulty": "Beginner",
            "bloom": "Understand",
            "content": {
                "title": "The Straight Tube vs Bent Tube Experiment",
                "title_hi": "सीधी ट्यूब बनाम मुड़ी हुई ट्यूब प्रयोग",
                "title_gu": "સીધી ટ્યુબ વિરુદ્ધ વળેલી ટ્યુબ પ્રયોગ",
                "description": "An animation showing a student looking through a straight pipe and successfully seeing a candle flame. Then, the pipe is bent, and the light rays from the candle hit the inside wall of the pipe and stop, showing that they cannot curve around the bend.",
                "description_hi": "एक एनीमेशन जिसमें एक छात्र सीधी पाइप से मोमबत्ती की लौ को सफलतापूर्वक देखता है। फिर, पाइप को मोड़ दिया जाता है, और मोमबत्ती से प्रकाश की किरणें पाइप की अंदरूनी दीवार से टकराकर रुक जाती हैं, यह दर्शाता है कि वे मोड़ के चारों ओर नहीं घूम सकती हैं।",
                "description_gu": "એક એનિમેશન જેમાં વિદ્યાર્થી સીધી પાઇપમાંથી મીણબત્તીની જ્યોતને સફળતાપૂર્વક જુએ છે. પછી, પાઇપને વાળવામાં આવે છે, અને મીણબત્તીમાંથી પ્રકાશના કિરણો પાઇપની અંદરની દિવાલ સાથે ટકરાઈને અટકી જાય છે, જે દર્શાવે છે કે તેઓ વળાંકની આસપાસ વળી શકતા નથી.",
                "paths": []
            }
        },
        {
            "type": "animated_diagram",
            "id": "SCI_CH9_ANIM_2",
            "difficulty": "Intermediate",
            "bloom": "Understand",
            "content": {
                "title": "Bouncing Ball vs Bouncing Light",
                "title_hi": "उछलती गेंद बनाम उछलता प्रकाश",
                "title_gu": "ઉછળતો દડો વિરુદ્ધ ઉછળતો પ્રકાશ",
                "description": "A split-screen animation. On the left, a rubber ball is thrown at an angle against a wall and bounces off at the same angle. On the right, a beam of light hits a flat mirror and bounces off perfectly at the same angle, demonstrating reflection.",
                "description_hi": "एक स्प्लिट-स्क्रीन एनीमेशन। बाईं ओर, एक रबर की गेंद को दीवार पर एक कोण (angle) पर फेंका जाता है और उसी कोण पर वापस उछलती है। दाईं ओर, प्रकाश की किरण एक समतल दर्पण से टकराती है और पूरी तरह से उसी कोण पर वापस उछलती है, जो परावर्तन को प्रदर्शित करता है।",
                "description_gu": "એક સ્પ્લિટ-સ્ક્રીન એનિમેશન. ડાબી બાજુએ, રબરના દડાને દિવાલ પર એક ખૂણે (angle) ફેંકવામાં આવે છે અને તે જ ખૂણે પાછો ઉછળે છે. જમણી બાજુએ, પ્રકાશનું કિરણ સપાટ અરીસા સાથે ટકરાય છે અને સંપૂર્ણપણે તે જ ખૂણે પાછું ઉછળે છે, જે પરાવર્તન (reflection) દર્શાવે છે.",
                "paths": []
            }
        }
    ],
    "gseb_class10_science_ch10.json": [
        {
            "type": "animated_diagram",
            "id": "SCI_CH10_ANIM_1",
            "difficulty": "Intermediate",
            "bloom": "Understand",
            "content": {
                "title": "The Prism and the Rainbow",
                "title_hi": "प्रिज्म और इंद्रधनुष",
                "title_gu": "પ્રિઝમ અને મેઘધનુષ્ય",
                "description": "A beam of white light enters a triangular glass prism. As it passes through, it magically splits apart, fanning out into the seven colors of the rainbow: Red, Orange, Yellow, Green, Blue, Indigo, and Violet.",
                "description_hi": "सफेद प्रकाश की एक किरण त्रिकोणीय कांच के प्रिज्म में प्रवेश करती है। जैसे ही यह गुजरती है, यह जादुई रूप से विभाजित हो जाती है, और इंद्रधनुष के सात रंगों: लाल, नारंगी, पीला, हरा, नीला, जामुनी और बैंगनी में फैल जाती है।",
                "description_gu": "સફેદ પ્રકાશનું કિરણ ત્રિકોણાકાર કાચના પ્રિઝમમાં પ્રવેશે છે. જેમ તે પસાર થાય છે, તે જાદુઈ રીતે વિભાજિત થાય છે, અને મેઘધનુષ્યના સાત રંગોમાં ફેલાય છે: લાલ, નારંગી, પીળો, લીલો, વાદળી, ઈન્ડિગો અને જાંબલી.",
                "paths": []
            }
        }
    ],
    "gseb_class10_science_ch11.json": [
        {
            "type": "animated_diagram",
            "id": "SCI_CH11_ANIM_1",
            "difficulty": "Intermediate",
            "bloom": "Understand",
            "content": {
                "title": "Electrons Moving Through a Wire",
                "title_hi": "तार के माध्यम से घूमते इलेक्ट्रॉन",
                "title_gu": "તાર દ્વારા ફરતા ઈલેક્ટ્રોન",
                "description": "Animation showing electrons flowing through a wire and colliding with atoms, producing heat energy due to resistance.",
                "description_hi": "एनीमेशन में एक तार के माध्यम से बहते हुए और परमाणुओं से टकराते हुए इलेक्ट्रॉनों को दिखाया गया है, जो प्रतिरोध के कारण ऊष्मा ऊर्जा (heat energy) पैदा करते हैं।",
                "description_gu": "એનિમેશનમાં એક તારમાંથી વહેતા અને પરમાણુઓ સાથે અથડાતા ઈલેક્ટ્રોન દર્શાવવામાં આવ્યા છે, જે અવરોધને કારણે ઉષ્મા ઊર્જા (heat energy) પેદા કરે છે.",
                "paths": []
            }
        }
    ],
    "gseb_class10_science_ch12.json": [
        {
            "type": "animated_diagram",
            "id": "SCI_CH12_ANIM_1",
            "difficulty": "Advanced",
            "bloom": "Understand",
            "content": {
                "title": "Oersted's Experiment",
                "title_hi": "ऑर्स्टेड का प्रयोग",
                "title_gu": "ઑર્સ્ટેડનો પ્રયોગ",
                "description": "Animation showing a compass needle deflecting when an electric current is passed through a nearby wire, demonstrating the magnetic field.",
                "description_hi": "एनीमेशन में कंपास की सुई को विक्षेपित होते हुए दिखाया गया है जब पास के तार से विद्युत धारा प्रवाहित की जाती है, जो चुंबकीय क्षेत्र (magnetic field) को प्रदर्शित करता है।",
                "description_gu": "એનિમેશનમાં હોકાયંત્રની સોયને વિચલિત થતી દર્શાવવામાં આવી છે જ્યારે નજીકના તારમાંથી વિદ્યુત પ્રવાહ પસાર થાય છે, જે ચુંબકીય ક્ષેત્ર (magnetic field) ને દર્શાવે છે.",
                "paths": []
            }
        }
    ],
    "gseb_class10_science_ch13.json": [
        {
            "type": "animated_diagram",
            "id": "SCI_CH13_ANIM_1",
            "difficulty": "Intermediate",
            "bloom": "Understand",
            "content": {
                "title": "The Forest Ecosystem: A Living Machine",
                "title_hi": "वन पारिस्थितिकी तंत्र: एक जीवित मशीन",
                "title_gu": "જંગલ નિવસનતંત્ર: એક જીવંત મશીન",
                "description": "An animated view showing a forest with different layers. Sunlight filters through the canopy, rain falls and is absorbed by the roots, and animals interact across the understory and forest floor. Dead leaves fall to the ground and turn into humus. It visually demonstrates how a forest is an interconnected, living system.",
                "description_hi": "विभिन्न परतों वाले जंगल को दिखाने वाला एक एनिमेटेड दृश्य। सूरज की रोशनी छतरी के माध्यम से छनती है, बारिश गिरती है और जड़ों द्वारा अवशोषित की जाती है, और जानवर जंगल के फर्श पर बातचीत करते हैं। मृत पत्तियां जमीन पर गिरती हैं और ह्यूमस में बदल जाती हैं। यह दृष्टिगत रूप से प्रदर्शित करता है कि जंगल एक परस्पर जुड़ी, जीवित प्रणाली कैसे है।",
                "description_gu": "વિવિધ સ્તરો ધરાવતા જંગલને દર્શાવતું એનિમેટેડ દ્રશ્ય. સૂર્યપ્રકાશ છત્ર દ્વારા ગળાય છે, વરસાદ પડે છે અને મૂળ દ્વારા શોષાય છે, અને પ્રાણીઓ જંગલના તળિયે સંપર્ક કરે છે. સૂકા પાંદડા જમીન પર પડે છે અને હ્યુમસમાં ફેરવાય છે. તે દૃષ્ટિગત રીતે દર્શાવે છે કે જંગલ કેવી રીતે એકબીજા સાથે જોડાયેલી, જીવંત પ્રણાલી છે.",
                "paths": []
            }
        }
    ]
}

base_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

for filename, sims in simulations.items():
    filepath = os.path.join(base_path, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        # We will inject the simulations at index 1 (after the hook/intro) or append if only 1 block
        if "blocks" in data:
            for s in reversed(sims):
                if len(data["blocks"]) > 1:
                    data["blocks"].insert(1, s)
                else:
                    data["blocks"].append(s)
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
            f.write("\n")
        print(f"Injected {len(sims)} simulations into {filename}")
    else:
        print(f"Error: {filepath} not found")

