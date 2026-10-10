"""CBSE Class 10 Science Ch 9: Light - Reflection and Refraction.
Every numerical answer is recomputed below with exact fractions (New Cartesian sign convention)."""
import sys
from fractions import Fraction as Fr
from sci_common import Chapter, check, SQP, SHINE, pyq_gseb

ROOT = sys.argv[1]
CH_ID = "cbse.c10.science.ncert_rationalised.ch09"
PATH = "app_core/content/cbse/class10/science/ncert_rationalised/ch09_light_reflection_and_refraction"
C = Chapter("sci10ch09")
blk = C.blk

def mirror_v(u, f): return 1 / (Fr(1) / f - Fr(1) / u)          # 1/v + 1/u = 1/f
def lens_v(u, f): return 1 / (Fr(1) / f + Fr(1) / u)            # 1/v - 1/u = 1/f
def lens_u(v, f): return 1 / (Fr(1) / v - Fr(1) / f)
# Exercises
check(lens_v(-25, 10) == Fr(50, 3) and Fr(50, 3) / -25 == Fr(-2, 3) and 5 * Fr(-2, 3) == Fr(-10, 3), "ex 10")
check(lens_u(-10, -15) == -30 and Fr(-10, -30) == Fr(1, 3), "ex 11 / GSEB 2024 Q44")
check(mirror_v(-10, 15) == 6 and -Fr(6, -10) == Fr(3, 5), "ex 12")
check(mirror_v(-20, 15) == Fr(60, 7) and -Fr(60, 7) / -20 == Fr(3, 7) and 5 * Fr(3, 7) == Fr(15, 7), "ex 14")
check(mirror_v(-27, -18) == -54 and -Fr(-54, -27) == -2, "ex 15")
check(1 / Fr(-2) == Fr(-1, 2) and 1 / Fr(3, 2) == Fr(2, 3), "ex 16, 17")
# In-text
check(-3 * -10 == 30, "concave mirror, m = -3, u = -10 cm: v = -30 cm")
check(lens_v(-50, 25) == 50 and 1 / Fr(25, 100) == 4, "convex lens, image at 50 cm equal size: u = -50 cm, f = 25 cm, P = +4 D")
check(Fr(3, 1) / Fr(3, 2) == 2, "speed in glass 2 x 10^8 m/s")
# SQP
check(mirror_v(-26, 26) == 13, "SQP 32: convex mirror f = 26 cm, u = -26 cm gives v = +13 cm, not infinity")
check(lens_u(-10, -20) == -20 and 1 / (Fr(1, -10) - Fr(1, -20)) == -20, "SQP 33: u = -20, v = -10 gives f = -20 cm")
check(lens_u(60, 50) == -300, "SQP 38C: u = -300 mm")
check(Fr(-20, 80) * -150 == Fr(75, 2) and 1 / (Fr(2, 75) + Fr(1, 150)) == 30, "SQP 38D: v = 37.5 mm, f = 30 mm")
# Worked examples in the lesson
check(mirror_v(-20, -15) == -60 and -Fr(-60, -20) == -3, "lesson mirror example")
check(lens_v(-15, 10) == 30 and Fr(30, -15) == -2, "lesson lens example")

MIRROR_FORMULA = "$\\dfrac{1}{v} + \\dfrac{1}{u} = \\dfrac{1}{f}$"
MIRROR_M = "$m = \\dfrac{h'}{h} = -\\dfrac{v}{u}$"
LENS_FORMULA = "$\\dfrac{1}{v} - \\dfrac{1}{u} = \\dfrac{1}{f}$"
LENS_M = "$m = \\dfrac{h'}{h} = \\dfrac{v}{u}$"
POWER = "$P = \\dfrac{1}{f}$"
SNELL = "$\\dfrac{\\sin i}{\\sin r} = \\text{constant}$"
N_SPEED = "$n_{m} = \\dfrac{c}{v}$"

CONCAVE = ("| Position of object | Position of image | Size of image | Nature of image |\n|---|---|---|---|\n"
           "| At infinity | At the focus F | Highly diminished, point-sized | Real and inverted |\n| Beyond C | Between F and C | Diminished | Real and inverted |\n"
           "| At C | At C | Same size | Real and inverted |\n| Between C and F | Beyond C | Enlarged | Real and inverted |\n"
           "| At F | At infinity | Highly enlarged | Real and inverted |\n| Between P and F | Behind the mirror | Enlarged | Virtual and erect |")
CONVEX_LENS = ("| Position of object | Position of image | Size of image | Nature of image |\n|---|---|---|---|\n"
               "| At infinity | At the focus F₂ | Highly diminished, point-sized | Real and inverted |\n| Beyond 2F₁ | Between F₂ and 2F₂ | Diminished | Real and inverted |\n"
               "| At 2F₁ | At 2F₂ | Same size | Real and inverted |\n| Between F₁ and 2F₁ | Beyond 2F₂ | Enlarged | Real and inverted |\n"
               "| At F₁ | At infinity | Highly enlarged | Real and inverted |\n| Between F₁ and the optical centre O | On the same side as the object | Enlarged | Virtual and erect |")
INDEX = ("| Medium | Refractive index | Medium | Refractive index |\n|---|---|---|---|\n| Air | 1.0003 | Canada balsam | 1.53 |\n| Ice | 1.31 | Rock salt | 1.54 |\n"
         "| Water | 1.33 | Carbon disulphide | 1.63 |\n| Alcohol | 1.36 | Dense flint glass | 1.65 |\n| Kerosene | 1.44 | Ruby | 1.71 |\n| Fused quartz | 1.46 | Sapphire | 1.77 |\n"
         "| Turpentine oil | 1.47 | Diamond | 2.42 |\n| Benzene | 1.50 | Crown glass | 1.52 |")

sections = [
 {"id": "s1", "title": "Seeing the world with light", "blocks": [
  blk("s1.hook", "hook", title="Why does the spoon look bent?",
    body="Put a spoon in a glass of water and it looks broken at the surface. Look into the back of a shining steel spoon and your face appears upside down; turn it over and your face is upright but smaller.\n\n"
         "All of this happens because light **reflects** from surfaces and **bends** when it passes from one material into another. "
         "In this chapter you will learn the rules of reflection by mirrors and refraction by lenses, and use simple formulas to find exactly where an image is formed."),
  blk("s1.inspiration", "inspiration", title="Light that bends around corners", person="Narinder Singh Kapany", years="1926–2020",
    body="Narinder Singh Kapany, born in Moga, Punjab, showed in the 1950s that images can be sent through a bundle of thin glass fibres, because light keeps reflecting inside them. "
         "He coined the term **fibre optics**.\n\nToday optical fibres carry internet signals across oceans and let doctors look inside the body with an endoscope.",
    future="Optics leads to careers in engineering, telecommunications, ophthalmology and optometry, photography, astronomy and laser technology."),
  blk("s1.socratic", "socratic_question", question="You stand far from a shop's security mirror and still see your image upright but small. What kind of mirror is it?",
    options=["Convex", "Concave", "Plane"], correct_index=0,
    explanation="A convex mirror always gives a virtual, erect, diminished image and a wide field of view."),
 ]},
 {"id": "s2", "title": "Reflection and spherical mirrors", "blocks": [
  blk("s2.reveal", "theory", title="Laws of reflection and mirror words", revision=True,
    body="**Laws of reflection** (true for all reflecting surfaces, plane or curved):\n1. The angle of incidence equals the angle of reflection.\n2. The incident ray, the normal at the point of incidence and the reflected ray all lie in the same plane.\n\n"
         "A plane mirror forms an image that is virtual, erect, of the same size, as far behind the mirror as the object is in front, and laterally inverted.\n\n"
         "A **spherical mirror** is part of a hollow sphere. If the reflecting surface curves inwards, it is **concave**; if it bulges outwards, it is **convex**.\n"
         "- **Pole (P):** the centre of the reflecting surface.\n- **Centre of curvature (C):** the centre of the sphere of which the mirror is a part; it is in front of a concave mirror and behind a convex mirror.\n"
         "- **Radius of curvature (R):** the radius of that sphere.\n- **Principal axis:** the straight line through P and C.\n"
         "- **Principal focus (F):** rays parallel to the principal axis, after reflection, meet at F (concave mirror) or appear to come from F (convex mirror).\n"
         "- **Focal length (f):** the distance PF. For mirrors of small aperture, **R = 2f**."),
  blk("s2.check", "knowledge_check", question="The radius of curvature of a spherical mirror is 20 cm. Its focal length is:",
    options=["10 cm", "20 cm", "40 cm", "5 cm"], correct_index=0,
    explanation="f = R/2 = 20/2 = 10 cm."),
 ]},
 {"id": "s3", "title": "Images formed by spherical mirrors", "blocks": [
  blk("s3.thm", "theory", title="Rays that make drawing easy", revision=True,
    body="To draw an image, use any two of these rays from the top of the object; the image is where the reflected rays meet (real) or appear to meet (virtual):\n"
         "1. A ray parallel to the principal axis passes through F after reflection (concave), or appears to come from F (convex).\n"
         "2. A ray through F (concave), or directed towards F (convex), becomes parallel to the principal axis.\n"
         "3. A ray through C (concave), or directed towards C (convex), is reflected back along the same path.\n"
         "4. A ray hitting the pole obliquely is reflected obliquely, making equal angles with the principal axis.\n\n"
         "**Convex mirror:** whatever the position of the object, the image is **virtual, erect and diminished**, behind the mirror between P and F (at F when the object is at infinity).\n\n"
         "**Uses:** concave mirrors in torches and headlights (strong parallel beam), shaving and dentists' mirrors (enlarged image), and solar furnaces (to concentrate sunlight). "
         "Convex mirrors as rear-view mirrors in vehicles, because they always give an erect image and a much wider field of view."),
  blk("s3.table", "markdown_table", title="Image formation by a concave mirror", revision=True, body=CONCAVE),
  blk("s3.check", "knowledge_check", question="To get a virtual, erect and enlarged image from a concave mirror, the object must be placed:",
    options=["between P and F", "at C", "beyond C", "at F"], correct_index=0,
    explanation="Only when the object is between the pole and the focus does a concave mirror give a virtual, erect, enlarged image."),
 ]},
 {"id": "s4", "title": "Mirror formula and magnification", "blocks": [
  blk("s4.thm", "theory", title="New Cartesian sign convention", revision=True,
    body="**Sign convention:** the pole is the origin and the principal axis is the x-axis. The object is placed to the left of the mirror.\n"
         "- Distances measured in the direction of the incident light (to the right) are **positive**; against it (to the left) are **negative**.\n"
         "- Heights measured upwards are **positive**; downwards are **negative**.\n\n"
         "So the object distance u is always negative; f is negative for a concave mirror and positive for a convex mirror.\n\n"
         f"**Mirror formula:** {MIRROR_FORMULA}\n\n**Magnification:** {MIRROR_M}\n\n"
         "A negative m means a real, inverted image; a positive m means a virtual, erect image. |m| > 1 means enlarged."),
  blk("s4.example", "worked_example", title="Worked example: concave mirror",
    problem="An object is placed 20 cm in front of a concave mirror of focal length 15 cm. Find the position and nature of the image.",
    steps=["$u = -20$ cm, $f = -15$ cm", "$\\dfrac{1}{v} = \\dfrac{1}{f} - \\dfrac{1}{u} = -\\dfrac{1}{15} + \\dfrac{1}{20} = -\\dfrac{1}{60}$, so $v = -60$ cm",
           "$m = -\\dfrac{v}{u} = -\\dfrac{-60}{-20} = -3$"],
    answer="The image is 60 cm in front of the mirror, real, inverted and three times enlarged (the object is between C and F)."),
  blk("s4.check", "knowledge_check", question="A mirror gives magnification m = −2. The image is:",
    options=["real, inverted and enlarged", "virtual, erect and enlarged", "real, erect and diminished", "virtual, inverted and diminished"], correct_index=0,
    explanation="Negative m means real and inverted; |m| = 2 means twice the size."),
 ]},
 {"id": "s5", "title": "Refraction of light", "blocks": [
  blk("s5.thm", "theory", title="Bending at a boundary", revision=True,
    body="Light changes direction when it goes obliquely from one transparent medium into another, because its **speed** changes. This is **refraction**. It explains why a pond looks shallower and a pencil in water looks bent.\n\n"
         "- Going from a rarer to a denser medium (air to glass), light slows down and bends **towards** the normal.\n- Going from a denser to a rarer medium, it speeds up and bends **away** from the normal.\n"
         "- Through a rectangular glass slab, the emergent ray is **parallel** to the incident ray but shifted sideways (lateral displacement).\n- A ray along the normal goes straight through.\n\n"
         f"**Laws of refraction:**\n1. The incident ray, the refracted ray and the normal at the point of incidence lie in the same plane.\n"
         f"2. **Snell's law:** for a given pair of media and a given colour of light, {SNELL}.\n\n"
         f"**Refractive index:** the constant above is the refractive index of the second medium with respect to the first. The **absolute refractive index** of a medium is {N_SPEED}, "
         "where c is the speed of light in vacuum (3 × 10⁸ m/s) and v its speed in the medium. A medium with a larger refractive index is **optically denser**; optical density is not the same as mass density "
         "(kerosene is optically denser than water, but lighter)."),
  blk("s5.table", "markdown_table", title="Absolute refractive index of some media", revision=True, body=INDEX),
  blk("s5.check", "knowledge_check", question="In which of these does light travel fastest?",
    options=["Water (1.33)", "Kerosene (1.44)", "Turpentine oil (1.47)", "Crown glass (1.52)"], correct_index=0,
    explanation="The smaller the refractive index, the faster light travels; water has the smallest of these."),
 ]},
 {"id": "s6", "title": "Spherical lenses", "blocks": [
  blk("s6.thm", "theory", title="Convex and concave lenses", revision=True,
    body="A **convex lens** is thicker in the middle and **converges** parallel rays to a point; a **concave lens** is thicker at the edges and **diverges** them. "
         "The centre of a lens is its **optical centre (O)**; a ray through O goes straight. A lens has two principal foci, F₁ and F₂, one on each side, and 2F₁, 2F₂ at twice the focal length.\n\n"
         "**Concave lens:** whatever the position of the object, the image is **virtual, erect and diminished**, on the same side as the object, between the focus and O.\n\n"
         "**Sign convention** is the same as for mirrors, measured from O: f is **positive** for a convex lens and **negative** for a concave lens.\n\n"
         f"**Lens formula:** {LENS_FORMULA}\n\n**Magnification:** {LENS_M}\n\n"
         f"**Power of a lens:** {POWER}, with f in metres. Its SI unit is the **dioptre (D)**: 1 D is the power of a lens of focal length 1 m. A convex lens has positive power; a concave lens, negative power. "
         "For lenses in contact, the powers add: P = P₁ + P₂ + ..."),
  blk("s6.table", "markdown_table", title="Image formation by a convex lens", revision=True, body=CONVEX_LENS),
  blk("s6.example", "worked_example", title="Worked example: convex lens",
    problem="An object is placed 15 cm from a convex lens of focal length 10 cm. Find the position and nature of the image.",
    steps=["$u = -15$ cm, $f = +10$ cm", "$\\dfrac{1}{v} = \\dfrac{1}{f} + \\dfrac{1}{u} = \\dfrac{1}{10} - \\dfrac{1}{15} = \\dfrac{1}{30}$, so $v = 30$ cm",
           "$m = \\dfrac{v}{u} = \\dfrac{30}{-15} = -2$"],
    answer="The image is 30 cm on the other side of the lens, real, inverted and twice the size (the object is between F₁ and 2F₁)."),
  blk("s6.check", "knowledge_check", question="A lens has a power of −2.0 D. It is a:",
    options=["concave lens of focal length 50 cm", "convex lens of focal length 50 cm", "concave lens of focal length 2 m", "convex lens of focal length 2 m"], correct_index=0,
    explanation="f = 1/P = 1/(−2) m = −0.5 m = −50 cm; negative f means a concave lens."),
  blk("s6.memory", "memory_trick", title="Signs and formulas without confusion",
    body="- **Mirror: plus; lens: minus.** Mirror formula 1/v **+** 1/u = 1/f; lens formula 1/v **−** 1/u = 1/f.\n"
         "- **Magnification:** mirror m = **−**v/u; lens m = v/u.\n- **Concave mirror and convex lens** are the converging pair (f of the mirror is negative, of the lens positive). **Convex mirror and concave lens** always give virtual, erect, diminished images.\n"
         "- **u is always negative** (the object is on the left)."),
  blk("s6.mistakes", "common_mistakes", title="Common mistakes",
    body="- Forgetting signs: putting u = +20 cm for an object in front of a mirror or lens.\n- Using the mirror formula for a lens, or −v/u for a lens.\n"
         "- Writing power with f in centimetres: always convert f to metres first.\n- Saying a convex mirror can form a real image: it never does.\n"
         "- Mixing up optical density with mass density."),
  blk("s6.tip", "teacher_tip", title="Try it in class",
    body="Use a magnifying glass to focus the image of a distant tree or window on a sheet of paper; the distance from the lens to the paper is its approximate focal length. "
         "Move a candle closer to a concave mirror to show the image growing and finally becoming virtual. Students can verify the mirror formula with their own readings."),
 ]},
 {"id": "s7", "title": "Think, connect, master", "blocks": [
  blk("s7.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend why vehicles use a convex mirror as a rear-view mirror, and why a concave mirror is used in a torch."),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 10, The Human Eye and the Colourful World:** the eye lens, defects of vision corrected by lenses, and refraction through a prism.\n"
         "- **Class 12 Physics:** ray optics, total internal reflection and optical instruments in detail.\n- **Everyday life:** cameras, spectacles, microscopes, telescopes and optical fibres all use these rules."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="An object 4 cm tall is placed 30 cm from a lens, and a real image is formed 60 cm on the other side.\n\n(a) Is the lens convex or concave? (b) Find its focal length and power. (c) Find the size of the image.\n\n"
         "**Answer:** (a) Convex, because a real image is formed. (b) $u = -30$ cm, $v = +60$ cm: $\\dfrac{1}{f} = \\dfrac{1}{v} - \\dfrac{1}{u} = \\dfrac{1}{60} + \\dfrac{1}{30} = \\dfrac{1}{20}$, so $f = 20$ cm and $P = \\dfrac{1}{0.2} = +5$ D. "
         "(c) $m = \\dfrac{v}{u} = \\dfrac{60}{-30} = -2$, so $h' = -8$ cm: the image is 8 cm tall and inverted."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- Light reflects with the angle of incidence equal to the angle of reflection; spherical mirrors are concave or convex, with R = 2f.\n"
         "- A concave mirror gives real, inverted images except when the object is between P and F; a convex mirror always gives virtual, erect, diminished images.\n"
         "- With the New Cartesian sign convention: mirror formula 1/v + 1/u = 1/f, m = −v/u.\n"
         "- Refraction is due to the change in the speed of light; sin i / sin r is constant (Snell's law), and n = c/v.\n"
         "- A convex lens converges and a concave lens diverges light; lens formula 1/v − 1/u = 1/f, m = v/u.\n- Power P = 1/f (f in metres), in dioptres; convex lenses have positive power."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- Write the given values with signs first (u, f, v, h), then the formula, then substitute.\n- Always state the nature of the image (real/virtual, erect/inverted, enlarged/diminished) and its position.\n"
         "- Practise ray diagrams for all six object positions of a concave mirror and of a convex lens, and one each for a convex mirror and a concave lens.\n"
         "- Convert focal length to metres before finding power."),
  blk("s7.flash1", "flashcard", front="Relation between focal length and radius of curvature", back="R = 2f"),
  blk("s7.flash2", "flashcard", front="Lens formula", back="1/v − 1/u = 1/f"),
  blk("s7.flash3", "flashcard", front="1 dioptre", back="The power of a lens of focal length 1 metre."),
 ]},
]
chapter = {"schema_version": 1, "id": CH_ID, "title": "Light – Reflection and Refraction",
  "book": "NCERT Science, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "science", "chapter_number": 9,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: reflection of light by curved surfaces; images formed by spherical mirrors, centre of curvature, principal axis, principal focus, focal length, mirror formula (derivation not required), magnification; refraction, laws of refraction, significance of refractive index; refraction of light by spherical lens; image formed by spherical lenses; lens formula (derivation not required); magnification; power of a lens.",
  "concepts": ["reflection", "refraction", "lenses"], "sections": sections}

# ---------------------------------------------------------------- questions
RF, RR, LN = "reflection", "refraction", "lenses"
def it(sec, n): return {"kind": "ncert_intext", "section": sec, "question": n}
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 9 exercises", "question": n}
def gseb(year, n, marks=None):
    s = pyq_gseb(year, n)
    if marks: s["original_marks"] = marks
    return s
MS2P = ["1 mark: first point", "1 mark: second point"]
MS3 = ["1 mark: first point", "1 mark: second point", "1 mark: third point"]
MSN = ["1 mark: formula", "1 mark: substitution", "1 mark: answer"]

# In-text
C.q("it1.q1", "very_short_answer", 2, [RF], it("9.2", 1), "Define the principal focus of a concave mirror.", "easy",
    answer_steps=["Rays of light parallel to the principal axis of a concave mirror, after reflection, all meet at a point on the principal axis.", "This point is the principal focus (F) of the concave mirror."], marking_scheme=MS2P)
C.q("it1.q2", "very_short_answer", 2, [RF], it("9.2", 2), "The radius of curvature of a spherical mirror is 20 cm. What is its focal length?", "easy",
    answer_steps=["$f = \\dfrac{R}{2}$", "$= \\dfrac{20}{2} = 10$ cm"], marking_scheme=["1 mark: formula", "1 mark: answer"])
C.q("it1.q3", "very_short_answer", 2, [RF], it("9.2", 3), "Name a mirror that can give an erect and enlarged image of an object.", "easy",
    answer_steps=["A concave mirror.", "It gives an erect, enlarged (virtual) image when the object is placed between its pole and principal focus."], marking_scheme=["1 mark: answer", "1 mark: condition"])
C.q("it1.q4", "very_short_answer", 2, [RF], it("9.2", 4), "Why do we prefer a convex mirror as a rear-view mirror in vehicles?", "easy",
    answer_steps=["A convex mirror always gives an erect, though diminished, image.", "It also has a much wider field of view because it curves outwards, so the driver can see a large area behind."], marking_scheme=MS2P)
C.q("it2.q1", "very_short_answer", 2, [RF], it("9.2.4", 1), "Find the focal length of a convex mirror whose radius of curvature is 32 cm.", "easy",
    answer_steps=["$f = \\dfrac{R}{2}$", "$= \\dfrac{32}{2} = 16$ cm (positive, since the focus of a convex mirror is behind it)"], marking_scheme=["1 mark: formula", "1 mark: answer"])
C.q("it2.q2", "very_short_answer", 2, [RF], it("9.2.4", 2), "A concave mirror produces three times magnified (enlarged) real image of an object placed at 10 cm in front of it. Where is the image located?",
    answer_steps=["Real image, so $m = -3$; $u = -10$ cm.", "$m = -\\dfrac{v}{u}$ gives $v = -mu = -(-3)(-10) = -30$ cm. The image is 30 cm in front of the mirror."], marking_scheme=["1 mark: m = −3", "1 mark: answer"])
C.q("it3.q1", "very_short_answer", 2, [RR], it("9.3", 1), "A ray of light travelling in air enters obliquely into water. Does the light ray bend towards the normal or away from the normal? Why?", "easy",
    answer_steps=["Towards the normal.", "Water is optically denser than air, so light slows down on entering it and bends towards the normal."], marking_scheme=["1 mark: answer", "1 mark: reason"])
C.q("it3.q2", "very_short_answer", 2, [RR], it("9.3", 2), "Light enters from air to glass having refractive index 1.50. What is the speed of light in the glass? The speed of light in vacuum is 3 × 10⁸ m s⁻¹.",
    answer_steps=["$n = \\dfrac{c}{v}$, so $v = \\dfrac{c}{n}$", "$= \\dfrac{3 \\times 10^{8}}{1.50} = 2 \\times 10^{8}$ m/s"], marking_scheme=["1 mark: formula", "1 mark: answer"])
C.q("it3.q3", "very_short_answer", 2, [RR], it("9.3", 3), "Find out, from Table 9.3, the medium having highest optical density. Also find the medium with lowest optical density.", "easy",
    answer_steps=["Highest optical density: diamond (refractive index 2.42).", "Lowest optical density: air (refractive index 1.0003)."], marking_scheme=MS2P)
C.q("it3.q4", "very_short_answer", 2, [RR], it("9.3", 4), "You are given kerosene, turpentine and water. In which of these does the light travel fastest? Use the information given in Table 9.3.",
    answer_steps=["Refractive indices: water 1.33, kerosene 1.44, turpentine oil 1.47.", "Light travels fastest in water, since it has the lowest refractive index (v = c/n)."], marking_scheme=["1 mark: values", "1 mark: answer"])
C.q("it3.q5", "very_short_answer", 2, [RR], it("9.3", 5), "The refractive index of diamond is 2.42. What is the meaning of this statement?",
    answer_steps=["The ratio of the speed of light in vacuum (air) to the speed of light in diamond is 2.42.", "So light travels 2.42 times slower in diamond than in vacuum: about $1.24 \\times 10^{8}$ m/s."], marking_scheme=MS2P)
C.q("it4.q1", "very_short_answer", 2, [LN], it("9.3.6", 1), "Define 1 dioptre of power of a lens.", "easy",
    answer_steps=["1 dioptre is the power of a lens whose focal length is 1 metre.", "$1 \\text{ D} = 1 \\text{ m}^{-1}$"], marking_scheme=["1 mark: definition", "1 mark: unit"])
C.q("it4.q2", "short_answer", 3, [LN], it("9.3.6", 2), "A convex lens forms a real and inverted image of a needle at a distance of 50 cm from it. Where is the needle placed in front of the convex lens if the image is equal to the size of the object? Also, find the power of the lens.",
    answer_steps=["A real image of the same size forms when the object is at 2F₁ and the image at 2F₂, so the needle is 50 cm in front of the lens: $u = -50$ cm.",
                  "$2f = 50$ cm, so $f = 25$ cm $= 0.25$ m.", "$P = \\dfrac{1}{f} = \\dfrac{1}{0.25} = +4$ D"], marking_scheme=["1 mark: position", "1 mark: focal length", "1 mark: power"])
C.q("it4.q3", "very_short_answer", 2, [LN], it("9.3.6", 3), "Find the power of a concave lens of focal length 2 m.", "easy",
    answer_steps=["$f = -2$ m (concave lens)", "$P = \\dfrac{1}{f} = \\dfrac{1}{-2} = -0.5$ D"], marking_scheme=["1 mark: sign", "1 mark: answer"])
# Exercises
C.mcq("ex.q1", [LN], "Which one of the following materials cannot be used to make a lens?", ["Water", "Glass", "Plastic", "Clay"], 3, "A lens must be transparent; clay is opaque.", source=ex(1))
C.mcq("ex.q2", [RF], "The image formed by a concave mirror is observed to be virtual, erect and larger than the object. Where should be the position of the object?",
      ["Between the principal focus and the centre of curvature", "At the centre of curvature", "Beyond the centre of curvature", "Between the pole of the mirror and its principal focus."], 3,
      "Only an object between P and F gives a virtual, erect, enlarged image.", source=ex(2))
C.mcq("ex.q3", [LN], "Where should an object be placed in front of a convex lens to get a real image of the size of the object?",
      ["At the principal focus of the lens", "At twice the focal length", "At infinity", "Between the optical centre of the lens and its principal focus."], 1, "At 2F₁ the image forms at 2F₂, real and of the same size.", source=ex(3))
C.mcq("ex.q4", [RF, LN], "A spherical mirror and a thin spherical lens have each a focal length of –15 cm. The mirror and the lens are likely to be",
      ["both concave.", "both convex.", "the mirror is concave and the lens is convex.", "the mirror is convex, but the lens is concave."], 0,
      "Negative focal length means a concave mirror and a concave lens.", "medium", source=ex(4))
C.mcq("ex.q5", [RF], "No matter how far you stand from a mirror, your image appears erect. The mirror is likely to be", ["only plane.", "only concave.", "only convex.", "either plane or convex."], 3,
      "Plane and convex mirrors always give erect images; a concave mirror gives an inverted image when you are far away.", "medium", source=ex(5))
C.mcq("ex.q6", [LN], "Which of the following lenses would you prefer to use while reading small letters found in a dictionary?",
      ["A convex lens of focal length 50 cm.", "A concave lens of focal length 50 cm.", "A convex lens of focal length 5 cm.", "A concave lens of focal length 5 cm."], 2,
      "A convex lens of short focal length gives a large virtual, erect image: a magnifying glass.", "medium", source=ex(6))
C.q("ex.q7", "short_answer", 3, [RF], ex(7), "We wish to obtain an erect image of an object, using a concave mirror of focal length 15 cm. What should be the range of distance of the object from the mirror? What is the nature of the image? Is the image larger or smaller than the object? Draw a ray diagram to show the image formation in this case.",
    answer_steps=["The object must be between the pole and the focus: less than 15 cm from the mirror.", "The image is virtual and erect, formed behind the mirror, and larger than the object.",
                  "Ray diagram: a ray parallel to the axis reflects through F, and a ray towards the pole reflects symmetrically; the reflected rays diverge, and their backward extensions meet behind the mirror to form the enlarged, erect image."],
    marking_scheme=["1 mark: range", "1 mark: nature and size", "1 mark: ray diagram"])
C.q("ex.q8", "short_answer", 3, [RF], ex(8), "Name the type of mirror used in the following situations.\n\n(a) Headlights of a car.\n\n(b) Side/rear-view mirror of a vehicle.\n\n(c) Solar furnace.\n\nSupport your answer with reason.",
    answer_steps=["(a) Concave mirror: with the bulb at its focus, it sends out a strong parallel beam of light.", "(b) Convex mirror: it always gives an erect image and has a wider field of view.",
                  "(c) Concave mirror: it concentrates sunlight at its focus, producing a lot of heat."], marking_scheme=["1 mark: (a)", "1 mark: (b)", "1 mark: (c)"])
C.q("ex.q9", "short_answer", 3, [LN], ex(9), "One-half of a convex lens is covered with a black paper. Will this lens produce a complete image of the object? Verify your answer experimentally. Explain your observations.",
    answer_steps=["Yes, the lens still forms a complete image.", "Experiment: form the image of a candle flame on a screen with a convex lens, then cover half the lens with black paper; the full image remains on the screen.",
                  "Every part of the lens receives rays from every point of the object, so the uncovered half still forms the whole image; it is only less bright."], marking_scheme=["1 mark: answer", "1 mark: experiment", "1 mark: explanation"])
C.q("ex.q10", "long_answer", 5, [LN], ex(10), "An object 5 cm in length is held 25 cm away from a converging lens of focal length 10 cm. Draw the ray diagram and find the position, size and the nature of the image formed.", "medium",
    answer_steps=["$h = 5$ cm, $u = -25$ cm, $f = +10$ cm", "$\\dfrac{1}{v} = \\dfrac{1}{f} + \\dfrac{1}{u} = \\dfrac{1}{10} - \\dfrac{1}{25} = \\dfrac{3}{50}$, so $v = \\dfrac{50}{3} \\approx 16.7$ cm",
                  "$m = \\dfrac{v}{u} = \\dfrac{50/3}{-25} = -\\dfrac{2}{3}$", "$h' = m \\times h = -\\dfrac{2}{3} \\times 5 \\approx -3.3$ cm",
                  "The image is about 16.7 cm on the other side of the lens, real, inverted and diminished (3.3 cm tall). Ray diagram: object beyond 2F₁, image between F₂ and 2F₂."],
    marking_scheme=["1 mark: values with signs", "1 mark: v", "1 mark: m", "1 mark: h'", "1 mark: nature and ray diagram"])
C.q("ex.q11", "short_answer", 3, [LN], ex(11), "A concave lens of focal length 15 cm forms an image 10 cm from the lens. How far is the object placed from the lens? Draw the ray diagram.",
    answer_steps=["$f = -15$ cm; the image of a concave lens is virtual, on the same side: $v = -10$ cm", "$\\dfrac{1}{u} = \\dfrac{1}{v} - \\dfrac{1}{f} = -\\dfrac{1}{10} + \\dfrac{1}{15} = -\\dfrac{1}{30}$",
                  "$u = -30$ cm: the object is 30 cm in front of the lens. (Ray diagram: the image is virtual, erect and diminished, between F₁ and O.)"], marking_scheme=MSN)
C.q("ex.q12", "short_answer", 3, [RF], ex(12), "An object is placed at a distance of 10 cm from a convex mirror of focal length 15 cm. Find the position and nature of the image.",
    answer_steps=["$u = -10$ cm, $f = +15$ cm", "$\\dfrac{1}{v} = \\dfrac{1}{f} - \\dfrac{1}{u} = \\dfrac{1}{15} + \\dfrac{1}{10} = \\dfrac{1}{6}$, so $v = +6$ cm",
                  "The image is 6 cm behind the mirror, virtual and erect; $m = -\\dfrac{v}{u} = 0.6$, so it is diminished."], marking_scheme=MSN)
C.q("ex.q13", "very_short_answer", 2, [RF], ex(13), "The magnification produced by a plane mirror is +1. What does this mean?", "easy",
    answer_steps=["|m| = 1: the image is of the same size as the object.", "The + sign means the image is virtual and erect."], marking_scheme=MS2P)
C.q("ex.q14", "short_answer", 3, [RF], ex(14), "An object 5.0 cm in length is placed at a distance of 20 cm in front of a convex mirror of radius of curvature 30 cm. Find the position of the image, its nature and size.",
    answer_steps=["$h = 5$ cm, $u = -20$ cm, $f = \\dfrac{R}{2} = +15$ cm", "$\\dfrac{1}{v} = \\dfrac{1}{15} + \\dfrac{1}{20} = \\dfrac{7}{60}$, so $v = \\dfrac{60}{7} \\approx 8.6$ cm behind the mirror",
                  "$m = -\\dfrac{v}{u} = \\dfrac{3}{7}$, $h' = \\dfrac{3}{7} \\times 5 \\approx 2.1$ cm: virtual, erect and diminished."], marking_scheme=MSN)
C.q("ex.q15", "long_answer", 5, [RF], ex(15), "An object of size 7.0 cm is placed at 27 cm in front of a concave mirror of focal length 18 cm. At what distance from the mirror should a screen be placed, so that a sharp focussed image can be obtained? Find the size and the nature of the image.", "medium",
    answer_steps=["$h = 7$ cm, $u = -27$ cm, $f = -18$ cm", "$\\dfrac{1}{v} = \\dfrac{1}{f} - \\dfrac{1}{u} = -\\dfrac{1}{18} + \\dfrac{1}{27} = -\\dfrac{1}{54}$, so $v = -54$ cm",
                  "The screen should be placed 54 cm in front of the mirror.", "$m = -\\dfrac{v}{u} = -\\dfrac{-54}{-27} = -2$, $h' = -2 \\times 7 = -14$ cm",
                  "The image is real, inverted and enlarged (14 cm tall)."], marking_scheme=["1 mark: values with signs", "1 mark: v", "1 mark: screen position", "1 mark: size", "1 mark: nature"])
C.q("ex.q16", "very_short_answer", 2, [LN], ex(16), "Find the focal length of a lens of power – 2.0 D. What type of lens is this?", "easy",
    answer_steps=["$f = \\dfrac{1}{P} = \\dfrac{1}{-2} = -0.5$ m $= -50$ cm", "Negative focal length: it is a concave (diverging) lens."], marking_scheme=["1 mark: f", "1 mark: type"])
C.q("ex.q17", "very_short_answer", 2, [LN], ex(17), "A doctor has prescribed a corrective lens of power +1.5 D. Find the focal length of the lens. Is the prescribed lens diverging or converging?", "easy",
    answer_steps=["$f = \\dfrac{1}{P} = \\dfrac{1}{1.5} \\approx 0.67$ m $\\approx 66.7$ cm", "Positive focal length: it is a converging (convex) lens."], marking_scheme=["1 mark: f", "1 mark: type"])
# CBSE sample paper
C.mcq("sqp30", [RF], "Arnav was making notes and he wrote down the following statements from his understanding of reflection from curved surfaces.\n\nI. Concave mirrors can produce both real and virtual images depending on the position of the object.\n\n"
      "II. Convex mirrors always produce real, inverted images regardless of the object's position.\n\nIII. In both concave and convex mirrors, the image location can be determined using the mirror formula " + "$\\dfrac{1}{f} = \\dfrac{1}{v} + \\dfrac{1}{u}$" +
      " where f is the focal length, v is the image distance, and u is the object distance.\n\nChoose from the following the correct option that lists the correct statements about reflection from curved surfaces.",
      ["I and II", "I, II and III", "II and III", "I and III"], 3, "Statement II is wrong: a convex mirror always gives virtual, erect images. I and III are correct.", "medium", source=SQP(30))
C.ar("sqp32", [RF], "A point object is placed at a distance of 26 cm from a convex mirror of focal length 26 cm. The image will not form at infinity.",
     "For above given system the equation " + "$\\dfrac{1}{f} = \\dfrac{1}{v} + \\dfrac{1}{u}$" + " gives v = ∞.", 2,
     "A is true: with u = −26 cm and f = +26 cm, the mirror formula gives v = +13 cm, a virtual image behind the mirror. R is false: v is not infinite.", source=SQP(32))
C.q("sqp33", "very_short_answer", 2, [LN], SQP(33), "An object is placed 20 cm in front of an optical instrument (shown as a box). A virtual, erect, diminished image forms 10 cm from the instrument, on the same side as the object.\n\n"
    "A. Identify the optical instrument.\n\nB. What type of image is formed in this case?\n\nC. Calculate the focal length of the instrument.", "medium",
    answer_steps=["A. A concave lens. B. A virtual image.", "C. $u = -20$ cm, $v = -10$ cm: $\\dfrac{1}{f} = \\dfrac{1}{v} - \\dfrac{1}{u} = -\\dfrac{1}{10} + \\dfrac{1}{20} = -\\dfrac{1}{20}$, so $f = -20$ cm"],
    marking_scheme=["1 mark: A and B", "1 mark: C"])
C.q("sqp38", "case_based", 4, [LN], SQP(38), "A Digital Single Lens Reflex (DSLR) camera is used by photographers to take high-resolution photographs. Inside it, a lens forms an image of the object on the camera's sensor.\n\n"
    "(i) What type of lens is used in the DSLR camera? (1)\n\n(ii) What type of image is formed on the sensor? (1)\n\n"
    "(iii) A photographer is using a lens of focal length f = 50 mm to take a close-up photograph of a small object. The lens projects an image onto the sensor located 60 mm behind the lens. Calculate the object distance. "
    "OR A flower is positioned 150 mm away from the camera lens. The actual height of the flower is 80 mm, and the image height on the sensor is 20 mm. Calculate the focal length of the lens. (2)", "hard",
    answer_steps=["(i) Convex lens.", "(ii) Real and inverted.",
                  "(iii) $f = 50$ mm, $v = 60$ mm: $\\dfrac{1}{u} = \\dfrac{1}{v} - \\dfrac{1}{f} = \\dfrac{1}{60} - \\dfrac{1}{50} = -\\dfrac{1}{300}$, so $u = -300$ mm: the object is 300 mm in front of the lens.",
                  "OR $m = \\dfrac{h'}{h} = \\dfrac{-20}{80} = -0.25$; $v = m \\times u = -0.25 \\times (-150) = 37.5$ mm; $\\dfrac{1}{f} = \\dfrac{1}{37.5} + \\dfrac{1}{150} = \\dfrac{1}{30}$, so $f = 30$ mm."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
# GSEB
C.q("gseb2024_44", "short_answer", 3, [LN], gseb(2024, "44"), "A concave lens has focal length of 15 cm. At what distance should the object from the lens be placed so that it forms an image at 10 cm from the lens? Also, find the magnification produced by the lens.",
    answer_steps=["$f = -15$ cm, $v = -10$ cm", "$\\dfrac{1}{u} = \\dfrac{1}{v} - \\dfrac{1}{f} = -\\dfrac{1}{10} + \\dfrac{1}{15} = -\\dfrac{1}{30}$, so $u = -30$ cm",
                  "$m = \\dfrac{v}{u} = \\dfrac{-10}{-30} = +\\dfrac{1}{3} \\approx 0.33$: virtual, erect and diminished."], marking_scheme=["1 mark: values", "1 mark: u", "1 mark: m"])
C.q("gseb2024_45", "short_answer", 3, [RF], gseb(2024, "45"), "(a) Draw a neat labelled ray diagram for the formation of image by a concave mirror, when the object is placed at the centre of curvature.\n\n(b) Write the uses of concave mirror.",
    answer_steps=["(a) A ray parallel to the axis reflects through F; a ray through F reflects parallel to the axis. They meet at C, below the axis.",
                  "The image is at C, real, inverted and of the same size as the object.", "(b) Torches, searchlights and headlights; shaving mirrors; dentists' mirrors; solar furnaces."],
    marking_scheme=["1 mark: ray diagram", "1 mark: image", "1 mark: uses"])
C.mcq("gseb2025_6", [RF], "No matter how far you stand from a mirror, your image appears erect. The mirror is likely to be", ["only plane", "only concave", "only convex", "either plane or convex"], 3,
      "Plane and convex mirrors always give erect images.", "medium", source=gseb(2025, "6"))
C.mcq("gseb2025_11", [LN], "The lens formula is ____.", ["$\\dfrac{1}{v} - \\dfrac{1}{u} = \\dfrac{1}{f}$", "$\\dfrac{1}{v} + \\dfrac{1}{u} = \\dfrac{1}{f}$", "$\\dfrac{1}{u} - \\dfrac{1}{v} = \\dfrac{1}{f}$"], 0,
      "For a lens, 1/v − 1/u = 1/f; 1/v + 1/u = 1/f is the mirror formula.", source=gseb(2025, "11"))
C.q("gseb2025_44", "short_answer", 3, [RF], gseb(2025, "44"), "Name the type of mirror used in the following situations, with reason: (a) Headlights of a car (b) Rear-view mirror of a vehicle (c) Solar furnace",
    answer_steps=["(a) Concave mirror: it gives a strong parallel beam with the bulb at its focus.", "(b) Convex mirror: erect image and a wider field of view.", "(c) Concave mirror: it concentrates sunlight at its focus."],
    marking_scheme=["1 mark: (a)", "1 mark: (b)", "1 mark: (c)"])
C.q("gseb2025_45", "short_answer", 3, [LN], gseb(2025, "45"), "Draw a ray diagram showing the image formation by a convex lens when an object is placed between F₁ and 2F₁ of the lens.",
    answer_steps=["Ray 1: a ray parallel to the principal axis passes through F₂ after refraction.", "Ray 2: a ray through the optical centre O goes straight without deviation.",
                  "The rays meet beyond 2F₂: the image is real, inverted and enlarged."], marking_scheme=["1 mark: first ray", "1 mark: second ray", "1 mark: image"])
# Shine MCQs
C.mcq("mcq01", [RF], "The focal length of a concave mirror is 12 cm. Its radius of curvature is:", ["24 cm", "6 cm", "12 cm", "36 cm"], 0, "R = 2f = 24 cm.")
C.mcq("mcq02", [RF], "The image formed by a convex mirror is always:", ["virtual, erect and diminished", "real, inverted and diminished", "virtual, erect and enlarged", "real, erect and same size"], 0, "A convex mirror never forms a real image.")
C.mcq("mcq03", [RF], "Which mirror is used by dentists to see a large image of the teeth?", ["Concave", "Convex", "Plane", "None of these"], 0, "With the tooth between P and F, a concave mirror gives an enlarged, erect image.")
C.mcq("mcq04", [RR], "When light goes from glass into air, it:", ["speeds up and bends away from the normal", "slows down and bends towards the normal", "goes straight without bending", "stops at the boundary"], 0, "Air is optically rarer than glass.", "medium")
C.mcq("mcq05", [RR], "The SI unit of refractive index is:", ["it has no unit", "m/s", "dioptre", "metre"], 0, "Refractive index is a ratio of two speeds, so it has no unit.")
C.mcq("mcq06", [LN], "A convex lens forms a virtual, erect and enlarged image when the object is placed:", ["between F₁ and O", "at 2F₁", "beyond 2F₁", "at F₁"], 0, "That is how a magnifying glass works.")
C.mcq("mcq07", [LN], "The power of a convex lens of focal length 25 cm is:", ["+4 D", "−4 D", "+0.25 D", "+25 D"], 0, "P = 1/f = 1/0.25 m = +4 D.", "medium")
C.mcq("mcq08", [LN], "Two lenses of power +3 D and −1 D are kept in contact. The power of the combination is:", ["+2 D", "+4 D", "−2 D", "−3 D"], 0, "Powers add: 3 + (−1) = +2 D.", "medium")
C.mcq("mcq09", [RF], "According to the New Cartesian sign convention, the object distance u for a real object is always:", ["negative", "positive", "zero", "equal to f"], 0, "The object is on the left, against the direction of the incident light.")
C.mcq("mcq10", [RR], "The refractive index of glass with respect to air is 1.5. The speed of light in glass is:", ["$2 \\times 10^{8}$ m/s", "$3 \\times 10^{8}$ m/s", "$4.5 \\times 10^{8}$ m/s", "$1.5 \\times 10^{8}$ m/s"], 0, "v = c/n = 3 × 10⁸ / 1.5 = 2 × 10⁸ m/s.", "medium")
# Assertion-reason
C.ar("ar1", [RF], "A convex mirror is used as a rear-view mirror in vehicles.", "A convex mirror always gives an erect image and has a wider field of view.", 0, "An erect image of a wide area behind is exactly what a driver needs: R explains A.")
C.ar("ar2", [RR], "A pencil partly dipped in water appears bent at the surface.", "Light bends when it passes obliquely from water into air.", 0, "Refraction at the water surface makes the dipped part appear displaced: R explains A.")
C.ar("ar3", [LN], "The power of a concave lens is positive.", "A concave lens diverges light.", 3, "A is false: a concave lens has a negative focal length, so its power is negative. R is true.")
C.ar("ar4", [RR], "Kerosene is optically denser than water.", "Kerosene has a greater mass density than water.", 2, "A is true (refractive index 1.44 > 1.33). R is false: kerosene is lighter than water; optical density is not mass density.")
C.ar("ar5", [LN], "A lens with half of it covered still forms a complete image.", "Every part of a lens receives light from every point of the object.", 0, "The uncovered half still collects rays from all points: R explains A; only the brightness falls.")
# Written Shine
C.q("vsa1", "very_short_answer", 2, [RR], SHINE, "State the two laws of refraction.", "easy",
    answer_steps=["The incident ray, the refracted ray and the normal at the point of incidence all lie in the same plane.", "For a given pair of media and a given colour of light, sin i / sin r is constant (Snell's law)."], marking_scheme=MS2P)
C.q("vsa2", "very_short_answer", 2, [RF], SHINE, "Write the New Cartesian sign convention for spherical mirrors.", "easy",
    answer_steps=["The pole is the origin; the object is placed to the left; distances in the direction of incident light (right) are positive, and against it (left) are negative.",
                  "Heights above the principal axis are positive; below it are negative."], marking_scheme=MS2P)
C.q("sa1", "short_answer", 3, [RF], SHINE, "An object is placed 30 cm in front of a concave mirror of focal length 10 cm. Find the position, nature and magnification of the image.",
    answer_steps=["$u = -30$ cm, $f = -10$ cm", "$\\dfrac{1}{v} = \\dfrac{1}{f} - \\dfrac{1}{u} = -\\dfrac{1}{10} + \\dfrac{1}{30} = -\\dfrac{1}{15}$, so $v = -15$ cm",
                  "$m = -\\dfrac{v}{u} = -\\dfrac{-15}{-30} = -0.5$: real, inverted and diminished, 15 cm in front of the mirror."], marking_scheme=MSN)
C.q("sa2", "short_answer", 3, [LN], SHINE, "An object is placed 12 cm from a convex lens of focal length 8 cm. Find the position and magnification of the image.",
    answer_steps=["$u = -12$ cm, $f = +8$ cm", "$\\dfrac{1}{v} = \\dfrac{1}{f} + \\dfrac{1}{u} = \\dfrac{1}{8} - \\dfrac{1}{12} = \\dfrac{1}{24}$, so $v = 24$ cm",
                  "$m = \\dfrac{v}{u} = \\dfrac{24}{-12} = -2$: real, inverted, twice the size, 24 cm on the other side."], marking_scheme=MSN)
check(mirror_v(-30, -10) == -15 and lens_v(-12, 8) == 24, "Shine sa1, sa2")
C.q("la1", "long_answer", 5, [RF], SHINE, "Describe with ray diagrams the images formed by a concave mirror when the object is (i) beyond C (ii) between C and F (iii) between P and F. Give one use of the concave mirror for each case where possible.", "medium",
    answer_steps=["(i) Beyond C: image between F and C, real, inverted and diminished.", "(ii) Between C and F: image beyond C, real, inverted and enlarged.",
                  "(iii) Between P and F: image behind the mirror, virtual, erect and enlarged.", "Rays used: one parallel to the axis (reflects through F) and one through C (reflects back along itself), or one towards P (reflects symmetrically).",
                  "Uses: (iii) shaving mirror and dentist's mirror; the focus property gives headlights and solar furnaces."],
    marking_scheme=["1 mark: (i)", "1 mark: (ii)", "1 mark: (iii)", "1 mark: rays", "1 mark: uses"])
C.q("la2", "long_answer", 5, [LN], SHINE, "An object 2 cm tall is placed 20 cm from a concave lens of focal length 10 cm. Find the position, size and nature of the image. What is the power of the lens?", "medium",
    answer_steps=["$h = 2$ cm, $u = -20$ cm, $f = -10$ cm", "$\\dfrac{1}{v} = \\dfrac{1}{f} + \\dfrac{1}{u} = -\\dfrac{1}{10} - \\dfrac{1}{20} = -\\dfrac{3}{20}$, so $v = -\\dfrac{20}{3} \\approx -6.7$ cm",
                  "$m = \\dfrac{v}{u} = \\dfrac{-20/3}{-20} = \\dfrac{1}{3}$, $h' = \\dfrac{2}{3} \\approx 0.67$ cm", "The image is virtual, erect and diminished, about 6.7 cm from the lens on the same side as the object.",
                  "$P = \\dfrac{1}{f} = \\dfrac{1}{-0.1} = -10$ D"],
    marking_scheme=["1 mark: values with signs", "1 mark: v", "1 mark: size", "1 mark: nature", "1 mark: power"])
check(lens_v(-20, -10) == Fr(-20, 3) and Fr(-20, 3) / -20 == Fr(1, 3), "Shine la2")
C.q("cb1", "case_based", 4, [RF], SHINE,
    "In a car showroom, Ishaan noticed that the side mirrors showed a wide view of the road with small, upright images. In the workshop, the headlight had a curved shiny reflector behind the bulb.\n\n"
    "(i) What type of mirror is used as a side mirror? (1)\n\n(ii) What type of mirror is used behind the headlight bulb? (1)\n\n(iii) Where is the bulb placed in the headlight, and why? OR Why are images in the side mirror smaller than the actual vehicles? (2)",
    answer_steps=["(i) Convex mirror.", "(ii) Concave mirror.", "(iii) At the principal focus, so that the reflected rays form a strong parallel beam. OR A convex mirror always forms diminished, virtual images between P and F."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
C.q("cb2", "case_based", 4, [LN], SHINE,
    "A watchmaker uses a small convex lens of focal length 5 cm to see the tiny parts of a watch. His optician has prescribed reading glasses of power +2 D for him.\n\n"
    "(i) What is the power of the watchmaker's lens? (1)\n\n(ii) What is the focal length of his reading glasses? (1)\n\n(iii) Where must the watch part be placed for the lens to act as a magnifier, and what image does it give? OR Why is a lens of short focal length preferred for this work? (2)",
    answer_steps=["(i) $P = \\dfrac{1}{0.05} = +20$ D", "(ii) $f = \\dfrac{1}{2} = 0.5$ m $= 50$ cm",
                  "(iii) Between the optical centre and the focus (closer than 5 cm): a virtual, erect and enlarged image. OR A shorter focal length gives a larger magnification for small objects held close to the lens."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])

C.write(ROOT, PATH, chapter, keep=lambda item: item["id"].startswith("sci10ch09.q.ex."))
