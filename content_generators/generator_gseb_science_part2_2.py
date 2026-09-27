import json
import os

CURRICULUM_PATH = '/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/master_curriculum.json'

def ch13_blocks():
    return [
        {"type": "theory", "id": "c8s_ch13_b1", "data": {"title": "The World of Sound 🎶", "content": "How do you know when your school period is over? You hear the bell! Sound plays an important role in our lives, helping us communicate. Let's learn how sound is produced and how it travels."}},
        {"type": "media", "id": "c8s_ch13_b2", "data": {"mediaType": "image", "url": "assets/images/earth_ch13.jpg", "caption": "Waves vibrating through a medium to produce sound."}},
        {"type": "theory", "id": "c8s_ch13_b3", "data": {"title": "Sound is Produced by a Vibrating Body", "content": "Touch the school bell when not in use. Now touch it when it is producing sound. Can you feel it vibrating? Sound is produced by vibrating objects. Vibration is a rapid to-and-fro or back-and-forth motion of an object."}},
        {"type": "teacher_tip", "id": "c8s_ch13_b4", "data": {"content": "Place your fingers lightly on your throat and say 'Ahhhh'. You will feel your vocal cords vibrating!"}},
        {"type": "theory", "id": "c8s_ch13_b5", "data": {"title": "Sound Needs a Medium", "content": "When you call your friend who is standing at a distance, your friend can hear your voice. Sound needs a material medium like air, water, or wood to travel. **Sound cannot travel through a vacuum.**"}},
        {"type": "flashcard", "id": "c8s_ch13_b6", "data": {"front": "Can sound travel through space (a vacuum)?", "back": "No! Sound needs a medium to travel."}},
        {"type": "quiz", "id": "c8s_ch13_b7", "data": {"question": "In which of the following mediums does sound travel the fastest?", "options": ["Air", "Water", "Steel", "Vacuum"], "correct_index": 2, "explanation": "Sound travels fastest in solids (like steel) because the particles are closely packed together."}},
        {"type": "theory", "id": "c8s_ch13_b8", "data": {"title": "Amplitude, Time Period, and Frequency", "content": "The number of oscillations per second is called the **frequency** (measured in Hertz, Hz).\nThe maximum displacement of the vibrating object from its central position is called the **amplitude**. Amplitude determines the loudness of sound."}},
        {"type": "theory", "id": "c8s_ch13_b9", "data": {"title": "Audible and Inaudible Sounds", "content": "Humans can hear sounds with frequencies between 20 Hz and 20,000 Hz. \nSounds below 20 Hz are infrasonic. Sounds above 20,000 Hz are ultrasonic (dogs and bats can hear these!)."}},
    ]

def ch14_blocks():
    return [
        {"type": "theory", "id": "c8s_ch14_b1", "data": {"title": "Chemical Effects of Electric Current ⚡", "content": "Your parents might have warned you never to touch an electrical appliance with wet hands. Why? Because water can conduct electricity! Let's explore what happens when electricity passes through liquids."}},
        {"type": "media", "id": "c8s_ch14_b2", "data": {"mediaType": "image", "url": "assets/images/science_method.jpg", "caption": "Experimenting with electricity and liquids."}},
        {"type": "theory", "id": "c8s_ch14_b3", "data": {"title": "Do Liquids Conduct Electricity?", "content": "Some liquids are good conductors of electricity (like tap water, lemon juice, and vinegar). Some are poor conductors (like distilled water, honey, and vegetable oil). Most liquids that conduct electricity are solutions of acids, bases, and salts."}},
        {"type": "flashcard", "id": "c8s_ch14_b4", "data": {"front": "Why does distilled water NOT conduct electricity?", "back": "Because it has no dissolved salts or minerals in it."}},
        {"type": "theory", "id": "c8s_ch14_b5", "data": {"title": "Chemical Effects", "content": "The passage of an electric current through a conducting solution causes chemical reactions. This may cause:\n- Formation of gas bubbles on the electrodes.\n- Deposits of metal on electrodes.\n- Changes in the color of the solution."}},
        {"type": "quiz", "id": "c8s_ch14_b6", "data": {"question": "The process of depositing a layer of any desired metal on another material by means of electricity is called:", "options": ["Electrolysis", "Electroplating", "Galvanization", "Electro-printing"], "correct_index": 1, "explanation": "Electroplating is widely used for coating cheaper metals with more expensive ones, like gold-plating jewelry."}},
        {"type": "theory", "id": "c8s_ch14_b7", "data": {"title": "Electroplating in Real Life", "content": "Chromium plating is done on car parts, bath taps, and bicycle handlebars because it has a shiny appearance and resists scratches. Tin cans used for storing food are made by electroplating tin onto iron."}},
    ]

def ch15_blocks():
    return [
        {"type": "theory", "id": "c8s_ch15_b1", "data": {"title": "Some Natural Phenomena 🌩️", "content": "Lightning and earthquakes are two of the most destructive natural phenomena on Earth. What causes them, and how can we protect ourselves? Let's dive in."}},
        {"type": "media", "id": "c8s_ch15_b2", "data": {"mediaType": "image", "url": "assets/images/science_method.jpg", "caption": "Understanding the forces of nature."}},
        {"type": "theory", "id": "c8s_ch15_b3", "data": {"title": "Lightning: A Giant Spark", "content": "Lightning is just an electric spark, but on a massive scale. It is caused by the accumulation of electrical charges in the clouds. Benjamin Franklin proved that the spark in the clouds and the spark from static electricity are the same phenomenon."}},
        {"type": "theory", "id": "c8s_ch15_b4", "data": {"title": "Charging by Rubbing", "content": "When you rub a plastic scale on your dry hair, it acquires a small electrical charge and can attract tiny pieces of paper. This is called static electricity. The charges generated by rubbing are static—they do not move by themselves."}},
        {"type": "flashcard", "id": "c8s_ch15_b5", "data": {"front": "What device is used to test whether an object is carrying a charge or not?", "back": "An Electroscope"}},
        {"type": "quiz", "id": "c8s_ch15_b6", "data": {"question": "What happens when two objects with the SAME (like) charges are brought near each other?", "options": ["They attract", "They repel", "They spark", "Nothing"], "correct_index": 1, "explanation": "Like charges repel each other, while unlike (opposite) charges attract each other."}},
        {"type": "theory", "id": "c8s_ch15_b7", "data": {"title": "Earthquakes", "content": "An earthquake is a sudden shaking or trembling of the earth which lasts for a very short time. It is caused by a disturbance deep inside the earth's crust. The outermost layer of the earth is not in one piece; it is fragmented. Each fragment is called a tectonic plate."}},
        {"type": "teacher_tip", "id": "c8s_ch15_b8", "data": {"content": "The power of an earthquake is expressed in terms of a magnitude on a scale called the Richter scale. Really destructive earthquakes have magnitudes higher than 7 on the Richter scale."}},
    ]

def ch16_blocks():
    return [
        {"type": "theory", "id": "c8s_ch16_b1", "data": {"title": "Light: The Window to the World 👁️", "content": "We see the world around us through our eyes. But eyes alone cannot see anything in complete darkness. We need Light! Let's explore how light reflects and bounces to let us see."}},
        {"type": "media", "id": "c8s_ch16_b2", "data": {"mediaType": "image", "url": "assets/images/science_method.jpg", "caption": "The science of reflection and optics."}},
        {"type": "theory", "id": "c8s_ch16_b3", "data": {"title": "Laws of Reflection", "content": "When light strikes a shiny surface like a mirror, it bounces back. \n1. **First Law:** The angle of incidence is always equal to the angle of reflection.\n2. **Second Law:** The incident ray, the reflected ray, and the normal (perpendicular line) at the point of incidence all lie in the same plane."}},
        {"type": "theory", "id": "c8s_ch16_b4", "data": {"title": "Regular vs Diffused Reflection", "content": "When all the parallel rays reflected from a smooth surface (like a mirror) are parallel, it is called **regular reflection**.\nWhen rays reflected from a rough surface (like cardboard) are not parallel, it is called **diffused or irregular reflection**."}},
        {"type": "flashcard", "id": "c8s_ch16_b5", "data": {"front": "What phenomenon splits white light into its seven constituent colors (like a rainbow)?", "back": "Dispersion"}},
        {"type": "quiz", "id": "c8s_ch16_b6", "data": {"question": "The part of the eye which gives it its distinctive color (black, brown, blue) and controls the size of the pupil is called:", "options": ["Cornea", "Retina", "Iris", "Lens"], "correct_index": 2, "explanation": "The iris controls the amount of light entering into the eye by adjusting the pupil size."}},
        {"type": "theory", "id": "c8s_ch16_b7", "data": {"title": "The Human Eye", "content": "Light enters the eye through a transparent front part called the **cornea**. Behind it is the **iris** and the **pupil**. The **lens** focuses light on the back of the eye, on a layer called the **retina**. The retina contains light-sensitive nerve cells (rods and cones)."}},
    ]

def ch17_blocks():
    return [
        {"type": "theory", "id": "c8s_ch17_b1", "data": {"title": "Stars and the Solar System 🌌", "content": "Look up at the night sky! You will see countless twinkling stars, the glowing moon, and maybe even a planet. Let's travel through space and explore our Solar System."}},
        {"type": "media", "id": "c8s_ch17_b2", "data": {"mediaType": "image", "url": "assets/images/science_method.jpg", "caption": "Exploring the cosmos."}},
        {"type": "theory", "id": "c8s_ch17_b3", "data": {"title": "The Moon and Its Phases", "content": "The moon does not produce its own light; it reflects the sunlight falling on it. The various shapes of the bright part of the moon seen during a month are called phases of the moon. The day on which the whole disc of the moon is visible is the Full Moon day."}},
        {"type": "teacher_tip", "id": "c8s_ch17_b4", "data": {"content": "We always see the same face of the moon from Earth because it takes exactly the same time to rotate on its axis as it takes to complete one revolution around Earth!"}},
        {"type": "theory", "id": "c8s_ch17_b5", "data": {"title": "Stars and Constellations", "content": "Stars are huge spheres of hot gas that emit their own light. The Sun is also a star! \nThe stars forming a group that has a recognizable shape (like a bear or a hunter) is called a **constellation** (e.g., Ursa Major, Orion)."}},
        {"type": "quiz", "id": "c8s_ch17_b6", "data": {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "correct_index": 1, "explanation": "Mars appears slightly reddish, hence it is called the red planet."}},
        {"type": "theory", "id": "c8s_ch17_b7", "data": {"title": "The Solar System", "content": "The Sun and the celestial bodies which revolve around it form the solar system. It consists of large numbers of bodies such as planets, comets, asteroids, and meteors.\nThe 8 planets are: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune."}},
    ]

def ch18_blocks():
    return [
        {"type": "theory", "id": "c8s_ch18_b1", "data": {"title": "Pollution of Air and Water 🏭", "content": "Our planet provides us with clean air and fresh water. But human activities are rapidly contaminating these precious resources. It's time to understand pollution and how to stop it."}},
        {"type": "media", "id": "c8s_ch18_b2", "data": {"mediaType": "image", "url": "assets/images/science_method.jpg", "caption": "The impact of human industrial activity on nature."}},
        {"type": "theory", "id": "c8s_ch18_b3", "data": {"title": "Air Pollution", "content": "When air is contaminated by unwanted substances which have a harmful effect on both the living and the non-living, it is referred to as air pollution. The substances which contaminate the air are called air pollutants (e.g., smoke, dust, carbon monoxide, sulfur dioxide)."}},
        {"type": "theory", "id": "c8s_ch18_b4", "data": {"title": "The Greenhouse Effect", "content": "The sun's rays warm the earth's surface. A part of the radiation is trapped by the atmosphere. This trapped radiation further warms the earth. This is called the greenhouse effect. Gases like Carbon Dioxide, Methane, and Nitrous Oxide are greenhouse gases."}},
        {"type": "flashcard", "id": "c8s_ch18_b5", "data": {"front": "What global phenomenon is caused by the excessive increase of greenhouse gases in the atmosphere?", "back": "Global Warming"}},
        {"type": "quiz", "id": "c8s_ch18_b6", "data": {"question": "Which gas binds with hemoglobin in our blood and reduces its oxygen-carrying capacity?", "options": ["Oxygen", "Carbon Dioxide", "Carbon Monoxide", "Nitrogen"], "correct_index": 2, "explanation": "Carbon Monoxide is a highly poisonous gas produced from incomplete combustion of fuels."}},
        {"type": "theory", "id": "c8s_ch18_b7", "data": {"title": "Water Pollution", "content": "Water which is suitable for drinking is called potable water. \nWhen toxic chemicals, sewage, and agricultural chemicals get mixed with water, the water becomes polluted. This can cause deadly diseases like cholera, typhoid, and jaundice."}},
        {"type": "teacher_tip", "id": "c8s_ch18_b8", "data": {"content": "Remember the 3 Rs to save our environment: Reduce, Reuse, and Recycle!"}},
    ]

def update_curriculum():
    print("Loading master curriculum...")
    with open(CURRICULUM_PATH, 'r') as f:
        data = json.load(f)

    data["gseb_class8_science_ch13"] = ch13_blocks()
    data["gseb_class8_science_ch14"] = ch14_blocks()
    data["gseb_class8_science_ch15"] = ch15_blocks()
    data["gseb_class8_science_ch16"] = ch16_blocks()
    data["gseb_class8_science_ch17"] = ch17_blocks()
    data["gseb_class8_science_ch18"] = ch18_blocks()

    print("Saving updated curriculum (Part 2/2)...")
    with open(CURRICULUM_PATH, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    update_curriculum()
