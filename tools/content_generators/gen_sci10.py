"""CBSE Class 10 Science Ch 10: The Human Eye and the Colourful World.
Numerical answers are rechecked with exact fractions below."""
import sys
from fractions import Fraction as Fr
from sci_common import Chapter, check, SQP, SHINE, pyq_gseb

ROOT = sys.argv[1]
CH_ID = "cbse.c10.science.ncert_rationalised.ch10"
PATH = "app_core/content/cbse/class10/science/ncert_rationalised/ch10_human_eye_and_colourful_world"
C = Chapter("sci10ch10")
blk = C.blk

check(round(100 / Fr(-55, 10), 1) == Fr(-182, 10) and round(100 / Fr(15, 10), 1) == Fr(667, 10), "ex 5: -18.2 cm and +66.7 cm")
check(100 / Fr(-80) == Fr(-5, 4), "ex 6: P = -1.25 D")
f7 = 1 / (Fr(1, -100) - Fr(1, -25))
check(f7 == Fr(100, 3) and 100 / f7 == 3, "ex 7: f = 33.3 cm, P = +3 D")
check(round(1 / Fr(-12, 10), 2) == Fr(-83, 100), "myopia 1.2 m: P = -0.83 D")
f_mast = 1 / (Fr(1, -50) - Fr(1, -25))
check(f_mast == 50 and 100 / f_mast == 2, "mastery: near point 50 cm -> f = 50 cm, +2 D")

DEFECTS = ("| Defect | What goes wrong | Where the image forms | Causes | Correction |\n|---|---|---|---|---|\n"
           "| Myopia (near-sightedness) | far objects look blurred; far point is nearer than infinity | in front of the retina | eye lens too curved; eyeball too long | concave lens |\n"
           "| Hypermetropia (far-sightedness) | near objects look blurred; near point is farther than 25 cm | behind the retina | focal length of eye lens too long; eyeball too small | convex lens |\n"
           "| Presbyopia | near objects blurred with age | behind the retina (for near objects) | ciliary muscles weaken and the eye lens becomes less flexible | convex lens, or bifocal lenses if both defects are present |")
PHENOMENA = ("| Everyday observation | Reason |\n|---|---|\n| Stars twinkle | atmospheric refraction: starlight bends by changing amounts as the air moves |\n"
             "| Planets do not twinkle | a planet is an extended source; the variations from its many points cancel out |\n"
             "| Sun seen about 2 minutes before sunrise and after sunset | atmospheric refraction bends sunlight over the horizon |\n"
             "| Sky is blue | fine air molecules scatter blue light more than red |\n| Sun looks reddish at sunrise and sunset | light travels a long path through air; most blue is scattered away |\n"
             "| Sky looks dark to an astronaut | no atmosphere to scatter light high above the earth |\n| Rainbow | dispersion, refraction and internal reflection of sunlight in raindrops |")

sections = [
 {"id": "s1", "title": "The camera in your head", "blocks": [
  blk("s1.hook", "hook", title="Why do stars twinkle but planets don't?",
    body="Look at the night sky: the stars twinkle, but bright planets such as Jupiter shine steadily. The midday sky is blue, yet the setting Sun looks red, and to astronauts the sky is black.\n\n"
         "Light, the eye and the air around us explain all of these. In this chapter you will learn how the eye focuses, how its common defects are corrected with lenses, "
         "how a prism splits white light into colours, and why the sky has the colours it has."),
  blk("s1.inspiration", "inspiration", title="The scientist who explained the colour of the sea", person="C. V. Raman", years="1888–1970",
    body="Chandrasekhara Venkata Raman wondered, on a voyage to Europe in 1921, why the sea is so deeply blue. His experiments on the **scattering of light** led, on 28 February 1928, "
         "to the discovery of the **Raman effect**: scattered light can change its colour slightly, revealing the molecules it met.\n\n"
         "In 1930 he became the first Asian to win the **Nobel Prize in Physics**. India celebrates 28 February as **National Science Day**.",
    future="Optics and vision lead to careers in ophthalmology, optometry, physics research, meteorology, photography and the design of cameras and screens."),
  blk("s1.socratic", "socratic_question", question="When you look from your book to a distant tree, what changes inside your eye so that both look sharp?",
    options=["The focal length of the eye lens", "The size of the eyeball", "The distance of the retina from the lens"], correct_index=0,
    explanation="The ciliary muscles change the curvature of the eye lens, and so its focal length: this is accommodation."),
 ]},
 {"id": "s2", "title": "The human eye", "blocks": [
  blk("s2.reveal", "theory", title="Parts of the eye and accommodation", revision=True,
    body="- **Cornea:** the clear front bulge; most of the refraction of light happens here.\n- **Iris:** the coloured muscular diaphragm that controls the size of the **pupil**, and so the amount of light entering.\n"
         "- **Eye lens:** a flexible, transparent, convex lens that fine-tunes the focus. It forms a **real, inverted** image on the **retina**.\n"
         "- **Ciliary muscles:** hold the lens and change its curvature.\n- **Retina:** a light-sensitive screen with cells that send electrical signals through the **optic nerve** to the brain, which interprets them.\n\n"
         "**Power of accommodation:** the ability of the eye lens to adjust its focal length. For a far object the ciliary muscles relax and the lens becomes thin (longer focal length); "
         "for a near object they contract and the lens becomes thick (shorter focal length).\n\n"
         "- **Near point:** the closest point seen clearly without strain, about **25 cm** for a young adult (the least distance of distinct vision).\n- **Far point:** the farthest point seen clearly, **infinity** for a normal eye.\n\n"
         "In old age, the lens can become milky and cloudy: this is **cataract**, treated by surgery."),
  blk("s2.check", "knowledge_check", question="The change in focal length of the eye lens is caused by the action of the:",
    options=["ciliary muscles", "pupil", "retina", "iris"], correct_index=0,
    explanation="The ciliary muscles change the curvature, and hence the focal length, of the eye lens."),
 ]},
 {"id": "s3", "title": "Defects of vision", "blocks": [
  blk("s3.thm", "theory", title="Myopia, hypermetropia and presbyopia", revision=True,
    body="- **Myopia (near-sightedness):** a person sees near objects clearly but not far ones. The image of a distant object forms **in front of** the retina. "
         "It is corrected with a **concave lens** of focal length equal to the far point (with a minus sign), which makes the parallel rays appear to come from the far point.\n"
         "- **Hypermetropia (far-sightedness):** a person sees far objects clearly but not near ones; the near point is farther than 25 cm. The image of a near object forms **behind** the retina. "
         "It is corrected with a **convex lens**, which makes an object at 25 cm appear to be at the person's near point.\n"
         "- **Presbyopia:** with age, the ciliary muscles weaken and the lens stiffens, so the near point moves away. Some people have both myopia and presbyopia and use **bifocal lenses**: concave in the upper part for distance, convex in the lower part for reading.\n\n"
         "These defects can be corrected with spectacles, contact lenses or surgery."),
  blk("s3.table", "markdown_table", title="Defects of vision at a glance", revision=True, body=DEFECTS),
  blk("s3.example", "worked_example", title="Worked example: correcting myopia",
    problem="The far point of a myopic person is 80 cm in front of the eye. Find the nature and power of the corrective lens.",
    steps=["A concave lens must form an image of a distant object at the far point: $u = \\infty$, $v = -80$ cm, so $f = -80$ cm $= -0.8$ m",
           "$P = \\dfrac{1}{f} = \\dfrac{1}{-0.8} = -1.25$ D"],
    answer="A concave lens of power −1.25 D."),
  blk("s3.check", "knowledge_check", question="A student cannot read the blackboard from the last row. The defect and its correction are:",
    options=["myopia, concave lens", "hypermetropia, convex lens", "presbyopia, bifocal lens", "cataract, convex lens"], correct_index=0,
    explanation="Difficulty seeing far objects is myopia, corrected with a concave lens."),
 ]},
 {"id": "s4", "title": "Refraction and dispersion by a prism", "blocks": [
  blk("s4.thm", "theory", title="Splitting white light", revision=True,
    body="A glass **prism** has two inclined refracting surfaces; the angle between them is the **angle of the prism**. A ray passing through it bends twice, towards the base, and the angle between the incident and emergent rays is the **angle of deviation**.\n\n"
         "**Dispersion:** white light entering a prism splits into a band of colours, the **spectrum**: **VIBGYOR** (violet, indigo, blue, green, yellow, orange, red). "
         "Different colours bend by different amounts because the speed of light in glass is different for each colour: **violet bends the most and red the least**.\n\n"
         "Isaac Newton showed that a second, inverted prism recombines the colours into white light: white light is a mixture of seven colours.\n\n"
         "**Rainbow:** a natural spectrum seen in the sky opposite the Sun after rain. Each water droplet acts like a small prism: sunlight is **refracted and dispersed** on entering, **reflected internally**, and **refracted** again on leaving."),
  blk("s4.check", "knowledge_check", question="In the spectrum formed by a prism, which colour bends the least?",
    options=["Red", "Violet", "Green", "Blue"], correct_index=0,
    explanation="Red light travels fastest in glass, so it bends the least; violet bends the most."),
 ]},
 {"id": "s5", "title": "Atmospheric refraction", "blocks": [
  blk("s5.thm", "theory", title="A moving, uneven atmosphere", revision=True,
    body="The air above a fire flickers because hot air is optically rarer than the cooler air around it, and the physical conditions keep changing. The whole atmosphere behaves like this on a large scale: "
         "its refractive index increases gradually towards the earth's surface. This **atmospheric refraction** explains:\n\n"
         "- **Twinkling of stars:** a star is a point source far away. Its light bends as it passes through the atmosphere, so its apparent position is slightly higher than the real one; "
         "as the air moves, the position and the amount of light entering the eye keep changing, so the star twinkles.\n"
         "- **Planets do not twinkle:** they are much nearer and look like extended sources, a collection of many point sources; the changes from them average out.\n"
         "- **Advance sunrise and delayed sunset:** we see the Sun about **2 minutes** before it actually rises and about 2 minutes after it sets, because its light bends over the horizon."),
  blk("s5.check", "knowledge_check", question="Stars twinkle because of:",
    options=["atmospheric refraction", "dispersion in a prism", "reflection from clouds", "scattering by dust only"], correct_index=0,
    explanation="Changing refraction in the moving atmosphere keeps changing the apparent position and brightness of a star."),
 ]},
 {"id": "s6", "title": "Scattering of light", "blocks": [
  blk("s6.thm", "theory", title="Why the sky is blue", revision=True,
    body="When a beam of light passes through a colloid such as smoke or mist, its path becomes visible because tiny particles scatter the light: the **Tyndall effect** (sunbeams entering a dense forest).\n\n"
         "The colour of scattered light depends on the size of the particles: very fine particles scatter mainly **blue** (short wavelength) light; larger particles scatter longer wavelengths, and very large ones scatter all colours equally, so they look **white** (clouds).\n\n"
         "- **Blue sky:** air molecules are very small, so they scatter blue light much more than red.\n"
         "- **Reddish Sun at sunrise and sunset:** sunlight crosses a much thicker layer of air near the horizon, so most of the blue is scattered away and mostly red reaches us.\n"
         "- **Dark sky for astronauts:** at great heights there is almost no air to scatter light.\n- **Red danger signals:** red light is scattered least by fog and smoke, so it can be seen from far away.\n\n" + PHENOMENA),
  blk("s6.check", "knowledge_check", question="Why does the sky appear dark to an astronaut high above the earth?",
    options=["There is no atmosphere to scatter sunlight", "The Sun gives no blue light there", "The astronaut's eyes cannot see blue", "Space is full of black dust"], correct_index=0,
    explanation="Without air to scatter light, no light reaches the eye from the sky around the Sun."),
  blk("s6.memory", "memory_trick", title="Lens for the eye, colour for the sky",
    body="- **My**opia = **my** eyes see only near; use a **con-c-a-v-e** lens (it 'caves in' the rays).\n- **Hyper**metropia = needs a **convex** (plus) lens: \"hyper\" goes with \"plus\".\n"
         "- **VIBGYOR** from the base of the spectrum upwards: violet bends most.\n- **Small particles, short waves (blue); big particles, all waves (white).**"),
  blk("s6.mistakes", "common_mistakes", title="Common mistakes",
    body="- Saying the image on the retina is erect: it is real and inverted; the brain interprets it.\n- Mixing up corrections: myopia needs a concave lens, hypermetropia a convex lens.\n"
         "- Writing that red bends the most in a prism: violet bends the most.\n- Explaining twinkling by scattering: it is atmospheric refraction.\n"
         "- Forgetting to convert cm to m when finding the power of a corrective lens."),
  blk("s6.tip", "teacher_tip", title="Try it in class",
    body="Pass sunlight through a glass prism onto a white wall to show VIBGYOR, and spray water against the morning sun to make a small rainbow. "
         "Shine a torch through water with a few drops of milk: from the side the beam looks bluish, while the light coming straight through looks orange-red, just like the sky and the setting Sun."),
 ]},
 {"id": "s7", "title": "Think, connect, master", "blocks": [
  blk("s7.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend why a myopic person needs a concave lens, and why the setting Sun looks red while the midday sky looks blue."),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 9:** lenses, focal length and power are used here to correct vision.\n- **Class 12 Physics:** optical instruments, the wave nature of light and the scattering of light in detail.\n"
         "- **Everyday life:** eye tests, spectacles, contact lenses, cameras and traffic signals all depend on these ideas."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="A man's near point is 50 cm. He wants to read a book held at 25 cm.\n\n(a) What defect does he have? (b) What lens does he need, and of what power?\n\n"
         "**Answer:** (a) Hypermetropia (or presbyopia, if it is due to age). (b) A convex lens that makes an object at 25 cm appear to be at 50 cm: $u = -25$ cm, $v = -50$ cm, "
         "$\\dfrac{1}{f} = \\dfrac{1}{v} - \\dfrac{1}{u} = -\\dfrac{1}{50} + \\dfrac{1}{25} = \\dfrac{1}{50}$, so $f = 50$ cm $= 0.5$ m and $P = +2$ D."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- The eye forms a real, inverted image on the retina; the ciliary muscles change the focal length of the eye lens (accommodation). Normal near point 25 cm, far point infinity.\n"
         "- Myopia is corrected by a concave lens, hypermetropia by a convex lens; presbyopia may need bifocal lenses.\n"
         "- A prism deviates light and disperses white light into VIBGYOR; violet bends most and red least; a rainbow is formed by raindrops.\n"
         "- Atmospheric refraction causes the twinkling of stars and the advance sunrise and delayed sunset.\n"
         "- Scattering of light causes the Tyndall effect, the blue sky, the reddish Sun at sunrise and sunset, and the dark sky seen by astronauts."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- Practise ray diagrams for myopia and hypermetropia, before and after correction, and dispersion through a prism.\n"
         "- For corrective lenses: myopia, f = −(far point); hypermetropia, use the lens formula with u = −25 cm and v = −(near point).\n"
         "- In 'give reason' questions name the phenomenon first (refraction, dispersion, scattering), then explain.\n- Learn VIBGYOR and which colour deviates most."),
  blk("s7.flash1", "flashcard", front="Least distance of distinct vision", back="About 25 cm for a normal young adult eye."),
  blk("s7.flash2", "flashcard", front="Lens used to correct myopia", back="A concave (diverging) lens."),
  blk("s7.flash3", "flashcard", front="Why do danger signals use red light?", back="Red light is scattered least by fog and smoke, so it can be seen from far away."),
 ]},
]
chapter = {"schema_version": 1, "id": CH_ID, "title": "The Human Eye and the Colourful World",
  "book": "NCERT Science, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "science", "chapter_number": 10,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "",
  "concepts": ["eye", "defects", "prism_atmosphere"], "sections": sections}
chapter["syllabus_note"] = ("Follows the CBSE 2025-26 syllabus: functioning of a lens in the human eye, defects of vision and their corrections, applications of spherical mirrors and lenses; "
                            "refraction of light through a prism, dispersion of light, scattering of light, applications in daily life.")

# ---------------------------------------------------------------- questions
EY, DF, PA = "eye", "defects", "prism_atmosphere"
def it(sec, n): return {"kind": "ncert_intext", "section": sec, "question": n}
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 10 exercises", "question": n}
def gseb(year, n, marks=None):
    s = pyq_gseb(year, n)
    if marks: s["original_marks"] = marks
    return s
MS2P = ["1 mark: first point", "1 mark: second point"]
MS3 = ["1 mark: first point", "1 mark: second point", "1 mark: third point"]

# In-text
C.q("it1.q1", "very_short_answer", 2, [EY], it("10.2", 1), "What is meant by power of accommodation of the eye?", "easy",
    answer_steps=["It is the ability of the eye lens to adjust its focal length.", "This lets the eye focus clearly on both near and distant objects; the ciliary muscles change the curvature of the lens."], marking_scheme=MS2P)
C.q("it1.q2", "very_short_answer", 2, [DF], it("10.2", 2), "A person with a myopic eye cannot see objects beyond 1.2 m distinctly. What should be the type of the corrective lens used to restore proper vision?",
    answer_steps=["A concave (diverging) lens.", "Its focal length should be 1.2 m (f = −1.2 m, power about −0.83 D), so that distant objects appear to be at the far point."], marking_scheme=["1 mark: lens", "1 mark: focal length"])
C.q("it1.q3", "very_short_answer", 2, [EY], it("10.2", 3), "What is the far point and near point of the human eye with normal vision?", "easy",
    answer_steps=["Near point: about 25 cm from the eye.", "Far point: infinity."], marking_scheme=MS2P)
C.q("it1.q4", "very_short_answer", 2, [DF], it("10.2", 4), "A student has difficulty reading the blackboard while sitting in the last row. What could be the defect the child is suffering from? How can it be corrected?", "easy",
    answer_steps=["Myopia (near-sightedness): distant objects look blurred.", "It is corrected with spectacles having a concave lens of suitable power."], marking_scheme=["1 mark: defect", "1 mark: correction"])
# Exercises
C.mcq("ex.q1", [EY], "The human eye can focus on objects at different distances by adjusting the focal length of the eye lens. This is due to", ["presbyopia.", "accommodation.", "near-sightedness.", "far-sightedness."], 1,
      "Adjusting the focal length to see near and far is accommodation.", source=ex(1))
C.mcq("ex.q2", [EY], "The human eye forms the image of an object at its", ["cornea.", "iris.", "pupil.", "retina."], 3, "The image is formed on the retina.", source=ex(2))
C.mcq("ex.q3", [EY], "The least distance of distinct vision for a young adult with normal vision is about", ["25 m.", "2.5 cm.", "25 cm.", "2.5 m."], 2, "The near point of a normal eye is about 25 cm.", source=ex(3))
C.mcq("ex.q4", [EY], "The change in focal length of an eye lens is caused by the action of the", ["pupil.", "retina.", "ciliary muscles.", "iris."], 2, "The ciliary muscles change the curvature of the lens.", source=ex(4))
C.q("ex.q5", "very_short_answer", 2, [DF], ex(5), "A person needs a lens of power –5.5 dioptres for correcting his distant vision. For correcting his near vision he needs a lens of power +1.5 dioptre. What is the focal length of the lens required for correcting (i) distant vision, and (ii) near vision?",
    answer_steps=["(i) $f = \\dfrac{1}{P} = \\dfrac{1}{-5.5}$ m $\\approx -0.182$ m $= -18.2$ cm (concave lens)", "(ii) $f = \\dfrac{1}{1.5}$ m $\\approx 0.667$ m $= 66.7$ cm (convex lens)"],
    marking_scheme=["1 mark: (i)", "1 mark: (ii)"])
C.q("ex.q6", "very_short_answer", 2, [DF], ex(6), "The far point of a myopic person is 80 cm in front of the eye. What is the nature and power of the lens required to correct the problem?",
    answer_steps=["A concave lens with $f = -80$ cm $= -0.8$ m is needed.", "$P = \\dfrac{1}{f} = \\dfrac{1}{-0.8} = -1.25$ D"], marking_scheme=["1 mark: nature", "1 mark: power"])
C.q("ex.q7", "short_answer", 3, [DF], ex(7), "Make a diagram to show how hypermetropia is corrected. The near point of a hypermetropic eye is 1 m. What is the power of the lens required to correct this defect? Assume that the near point of the normal eye is 25 cm.", "hard",
    answer_steps=["A convex lens must form a virtual image of an object at 25 cm at the near point, 1 m: $u = -25$ cm, $v = -100$ cm",
                  "$\\dfrac{1}{f} = \\dfrac{1}{v} - \\dfrac{1}{u} = -\\dfrac{1}{100} + \\dfrac{1}{25} = \\dfrac{3}{100}$, so $f = \\dfrac{100}{3}$ cm $\\approx 0.33$ m",
                  "$P = \\dfrac{1}{f} = +3$ D. (Diagram: without the lens the image of a near object forms behind the retina; the convex lens brings it onto the retina.)"],
    marking_scheme=["1 mark: values", "1 mark: f", "1 mark: power and diagram"])
C.q("ex.q8", "very_short_answer", 2, [EY], ex(8), "Why is a normal eye not able to see clearly the objects placed closer than 25 cm?",
    answer_steps=["The focal length of the eye lens cannot be decreased below a certain limit: the ciliary muscles cannot make it any thicker.", "So the image of an object closer than 25 cm forms behind the retina and looks blurred."], marking_scheme=MS2P)
C.q("ex.q9", "very_short_answer", 2, [EY], ex(9), "What happens to the image distance in the eye when we increase the distance of an object from the eye?",
    answer_steps=["The image distance does not change: it is the distance from the lens to the retina, which is fixed.", "Instead, the eye lens changes its focal length (accommodation) so that the image still forms on the retina."], marking_scheme=MS2P)
C.q("ex.q10", "short_answer", 3, [PA], ex(10), "Why do stars twinkle?",
    answer_steps=["Starlight is refracted continuously as it passes through layers of air of changing refractive index (atmospheric refraction).", "Since the star is very far away, it acts as a point source, and its apparent position keeps shifting slightly.",
                  "The amount of light entering the eye also keeps changing, so the star seems to flicker: it twinkles."], marking_scheme=MS3)
C.q("ex.q11", "very_short_answer", 2, [PA], ex(11), "Explain why the planets do not twinkle.",
    answer_steps=["Planets are much closer to the earth and look like extended sources: a collection of many point sources of light.", "The variations in light from all these points average out to zero, so there is no twinkling."], marking_scheme=MS2P)
C.q("ex.q12", "very_short_answer", 2, [PA], ex(12), "Why does the sky appear dark instead of blue to an astronaut?", "easy",
    answer_steps=["At very great heights there is almost no atmosphere, so there are no particles to scatter sunlight.", "No scattered light reaches the astronaut's eyes from the sky, so it looks dark."], marking_scheme=MS2P)
# CBSE sample paper
C.mcq("sqp31", [PA], "Choose the correct option from the below which explains the reason for us to perceive the day sky as blue.",
      ["As sunlight passes through the atmosphere, shorter wavelengths, such as blue are scattered more than other colors.", "The sky appears blue because all colors are scattered equally, but blue light is stronger and more visible to the human eye.",
       "The blue color of the sky is due to longer wavelengths like red and orange scattering more than shorter wavelengths, making blue stand out more.", "The atmosphere contains blue-colored particles that give the sky its blue appearance."], 0,
      "Fine air molecules scatter short wavelengths (blue) much more than long ones; our eyes are more sensitive to blue than violet.", "medium", source=SQP(31))
C.q("sqp35", "short_answer", 3, [PA, DF], SQP(35), "(i) What is dispersion of light?\n\n(ii) Explain the condition under which dispersion happens.\n\n(iii) Give one reason that causes presbyopia.",
    answer_steps=["(i) Dispersion is the splitting of white light into its component colours (spectrum) when it passes through a medium such as a prism.",
                  "(ii) It happens when light enters a medium in which the speed, and so the refractive index, is different for different colours; each colour then bends by a different angle.",
                  "(iii) With age, the ciliary muscles weaken and the eye lens loses its flexibility."], marking_scheme=["1 mark: (i)", "1 mark: (ii)", "1 mark: (iii)"])
# GSEB
C.mcq("gseb2025_5", [DF], "The crystalline lens of people at old age becomes milky and cloudy. This condition is called ____.", ["cataract", "myopia", "hypermetropia", "presbyopia"], 0,
      "A milky, cloudy eye lens is cataract, treated by surgery.", source=gseb(2025, "5"))
C.tf("gseb2025_15", [PA], "The twinkling of a star is due to atmospheric refraction of starlight.", True,
     "Changing refraction in the moving atmosphere keeps shifting the star's apparent position and brightness.", source=gseb(2025, "15"))
C.mcq("gseb2025_19", [PA], "In the dispersion of white light through a prism, which coloured light bends the least?", ["Red", "Violet", "Green"], 0, "Red bends the least; violet bends the most.", source=gseb(2025, "19"))
C.q("gseb2024_30", "very_short_answer", 2, [EY], gseb(2024, "30"), "(a) Define power of accommodation of eye.\n\n(b) Write the function of ciliary muscle.", "easy",
    answer_steps=["(a) The ability of the eye lens to adjust its focal length to see near and far objects clearly.", "(b) The ciliary muscles change the curvature, and so the focal length, of the eye lens."], marking_scheme=["1 mark: (a)", "1 mark: (b)"])
C.q("gseb2025_52", "short_answer", 3, [DF], gseb(2025, "52", 4), "Explain the differences between myopia and hypermetropia.",
    answer_steps=["Myopia: far objects look blurred; the far point is nearer than infinity. Hypermetropia: near objects look blurred; the near point is farther than 25 cm.",
                  "Myopia: the image forms in front of the retina (lens too curved or eyeball too long). Hypermetropia: the image forms behind the retina (focal length too long or eyeball too small).",
                  "Myopia is corrected with a concave lens; hypermetropia with a convex lens."], marking_scheme=MS3)
# Shine MCQs
C.mcq("mcq01", [EY], "The part of the eye that controls the size of the pupil is the:", ["iris", "retina", "cornea", "optic nerve"], 0, "The iris adjusts the size of the pupil.")
C.mcq("mcq02", [EY], "The image formed on the retina is:", ["real and inverted", "virtual and erect", "real and erect", "virtual and inverted"], 0, "The convex eye lens forms a real, inverted image; the brain interprets it.")
C.mcq("mcq03", [DF], "Hypermetropia is corrected by using a:", ["convex lens", "concave lens", "plane glass", "cylindrical mirror"], 0, "A convex lens brings the image of near objects onto the retina.")
C.mcq("mcq04", [DF], "Bifocal lenses are generally used to correct:", ["presbyopia with myopia", "cataract", "colour blindness", "only myopia"], 0, "The upper part corrects distant vision, the lower part near vision.", "medium")
C.mcq("mcq05", [PA], "The colour of white light that deviates the most through a prism is:", ["violet", "red", "yellow", "green"], 0, "Violet bends the most; red the least.")
C.mcq("mcq06", [PA], "A rainbow is always seen:", ["in the direction opposite to the Sun", "towards the Sun", "only at noon", "only at night"], 0, "Sunlight is dispersed and internally reflected by raindrops back towards the observer.", "medium")
C.mcq("mcq07", [PA], "The Sun is visible about 2 minutes before actual sunrise because of:", ["atmospheric refraction", "scattering of light", "dispersion", "reflection by clouds"], 0, "Atmospheric refraction bends sunlight over the horizon.")
C.mcq("mcq08", [PA], "Danger signals are red because red light:", ["is scattered the least by fog and smoke", "is scattered the most", "is the brightest colour", "travels slowest in air"], 0, "Being scattered least, red light reaches far.")
C.mcq("mcq09", [PA], "The path of a beam of light becomes visible in a smoke-filled room due to:", ["the Tyndall effect", "dispersion", "total internal reflection", "atmospheric refraction"], 0, "Smoke particles scatter the light: the Tyndall effect.")
C.mcq("mcq10", [DF], "The far point of a myopic eye is 2 m. The power of the corrective lens is:", ["−0.5 D", "+0.5 D", "−2 D", "+2 D"], 0, "f = −2 m, so P = 1/f = −0.5 D.", "medium")
# Assertion-reason
C.ar("ar1", [DF], "A myopic person uses a concave lens.", "A concave lens diverges the rays so that the image forms on the retina.", 0, "Diverging the rays moves the image back onto the retina: R explains A.")
C.ar("ar2", [PA], "Planets do not twinkle.", "Planets are extended sources, and the variations in light from their many points average out.", 0, "The averaging of many point sources stops twinkling: R explains A.")
C.ar("ar3", [PA], "The sky appears blue.", "Air molecules scatter red light more than blue light.", 2, "A is true. R is false: air molecules scatter blue light more than red.")
C.ar("ar4", [PA], "White light splits into colours when it passes through a prism.", "Different colours of light bend through different angles in glass.", 0, "Different deviations separate the colours: R explains A.")
C.ar("ar5", [EY], "A normal eye can see objects at 10 cm clearly.", "The focal length of the eye lens cannot be decreased below a certain limit.", 3, "A is false: the near point is about 25 cm. R is true.")
# Written Shine
C.q("vsa1", "very_short_answer", 2, [EY], SHINE, "Write the functions of the iris and the retina.", "easy",
    answer_steps=["Iris: controls the size of the pupil, and so the amount of light entering the eye.", "Retina: a light-sensitive screen on which the image forms; its cells send signals through the optic nerve to the brain."], marking_scheme=MS2P)
C.q("vsa2", "very_short_answer", 2, [PA], SHINE, "Why does the Sun look reddish at sunrise and sunset?",
    answer_steps=["Near the horizon, sunlight passes through a much thicker layer of air.", "Most of the blue light is scattered away on the way, so mainly red light reaches our eyes."], marking_scheme=MS2P)
C.q("sa1", "short_answer", 3, [PA], SHINE, "How is a rainbow formed? Where is it seen?",
    answer_steps=["After rain, tiny water droplets in the air act like small prisms.", "Sunlight is refracted and dispersed on entering a droplet, reflected internally, and refracted again on leaving.",
                  "The colours reach the observer; a rainbow is seen in the sky opposite the Sun."], marking_scheme=MS3)
C.q("sa2", "short_answer", 3, [PA], SHINE, "What is the Tyndall effect? How does the size of particles decide the colour of scattered light?",
    answer_steps=["The scattering of light by colloidal particles, which makes the path of a beam visible, is the Tyndall effect (e.g. sunbeams in a forest).",
                  "Very fine particles scatter mainly blue (short wavelength) light.", "Larger particles scatter longer wavelengths; very large ones scatter all colours equally, so they look white (clouds)."], marking_scheme=MS3)
C.q("la1", "long_answer", 5, [DF], SHINE, "What is myopia? Give its two causes. How is it corrected? Find the power of the corrective lens for a person whose far point is 2 m.", "medium",
    answer_steps=["Myopia: a person can see near objects clearly but not distant ones; the image of a distant object forms in front of the retina.", "Causes: excessive curvature of the eye lens; elongation of the eyeball.",
                  "Correction: a concave lens of suitable power, which makes parallel rays appear to come from the far point.", "$f = -2$ m", "$P = \\dfrac{1}{f} = -0.5$ D"],
    marking_scheme=["1 mark: definition", "1 mark: causes", "1 mark: correction", "1 mark: f", "1 mark: power"])
C.q("la2", "long_answer", 5, [PA], SHINE, "Explain, with reasons: (a) twinkling of stars (b) advance sunrise and delayed sunset (c) blue colour of the sky.", "medium",
    answer_steps=["(a) Starlight is refracted by layers of air whose refractive index keeps changing; the star, a point source, appears to shift and its brightness varies, so it twinkles.",
                  "The apparent position of a star is also slightly higher than its actual position.", "(b) Atmospheric refraction bends sunlight over the horizon, so the Sun is seen about 2 minutes before sunrise and after sunset.",
                  "(c) Air molecules are much smaller than the wavelength of visible light and scatter blue light more than red.", "This scattered blue light reaches our eyes from all parts of the sky."],
    marking_scheme=["1 mark: (a)", "1 mark: (a) position", "1 mark: (b)", "1 mark: (c)", "1 mark: (c) reason"])
C.q("cb1", "case_based", 4, [DF], SHINE,
    "At a school eye camp, Mihir could read the eye chart only from very close, while his grandmother could read the far chart but needed to hold her newspaper at arm's length.\n\n"
    "(i) Which defect does Mihir have? (1)\n\n(ii) Which lens will correct Mihir's vision? (1)\n\n(iii) What defect does the grandmother probably have, and why does it happen? OR Her near point is 50 cm. Find the power of the lens she needs to read at 25 cm. (2)",
    answer_steps=["(i) Myopia (near-sightedness).", "(ii) A concave lens.",
                  "(iii) Presbyopia: with age, the ciliary muscles weaken and the eye lens becomes less flexible. OR $u = -25$ cm, $v = -50$ cm: $\\dfrac{1}{f} = -\\dfrac{1}{50} + \\dfrac{1}{25} = \\dfrac{1}{50}$, $f = 0.5$ m, $P = +2$ D (convex lens)."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
C.q("cb2", "case_based", 4, [PA], SHINE,
    "On a trip to the hills, Ananya passed sunlight through a glass prism and saw a band of colours on the wall. In the evening the Sun looked orange-red, and at night the stars twinkled while Jupiter shone steadily.\n\n"
    "(i) What is the band of colours called? (1)\n\n(ii) Which colour bent the most? (1)\n\n(iii) Why did the Sun look orange-red in the evening? OR Why did Jupiter not twinkle? (2)",
    answer_steps=["(i) The spectrum (formed by dispersion).", "(ii) Violet.",
                  "(iii) Near the horizon, sunlight travels through a thick layer of air, and most of the blue is scattered away, leaving mainly red and orange. OR Jupiter is an extended source; the variations in light from its many points average out."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])

C.write(ROOT, PATH, chapter, keep=lambda item: item["id"].startswith("sci10ch10.q.ex."))
