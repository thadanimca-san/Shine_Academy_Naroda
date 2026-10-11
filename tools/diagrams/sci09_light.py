"""Ray diagrams for Class 10 Science Ch 9 (Light: Reflection and Refraction).

Image positions come from the mirror formula 1/v + 1/u = 1/f and the lens formula
1/v - 1/u = 1/f (New Cartesian sign convention), so every figure is to scale.
Usage: python3 tools/diagrams/sci09_light.py <chapter folder>
"""
import math
import sys
from figlib import Fig, BLACK, GREY, LIGHT, RED, BLUE, GREEN, ORANGE, GLASS, lerp

F = 4.0     # focal length (world units)
H = 1.2     # object height
AP = 3.0    # half-aperture of mirrors and lenses


def axis(fig, x0, x1, label="Principal axis"):
    fig.line((x0, 0), (x1, 0), GREY, 1.8)
    if label:
        fig.text((x0 + 0.1, 0), label, 15, GREY, "lb", dy=-6)


def obj(fig, x, h=H):
    fig.arrow((x, 0), (x, h), BLUE, 4, size=16)
    fig.text((x, h / 2), "Object", 17, BLUE, "rm", dx=-10)


def image(fig, x, h, virtual):
    fig.arrow((x, 0), (x, h), GREEN, 4, dash=(9, 6) if virtual else None, size=16)
    label = "Image" + (" (virtual)" if virtual else "")
    if 0 < h < 0.8:  # small upright image: label it under the axis, clear of the rays
        fig.text((x, 0), label, 17, GREEN, "mt", dy=34)
    else:
        fig.text((x, h), label, 17, GREEN, "mb" if h > 0 else "mt", dy=-8 if h > 0 else 8)


def pole(fig, x):
    fig.dot((x, 0), 4.5)
    fig.text((x, 0), "P", 19, BLACK, "rt", dx=-8, dy=8, bold=True)


def mark(fig, x, name, below=True):
    fig.dot((x, 0), 4.5)
    fig.text((x, 0), name, 19, BLACK, "mt" if below else "mb", dy=8 if below else -8, bold=True)


# ---------------- Mirrors ----------------
def mirror_x(y, concave):
    """x of the mirror surface at height y (pole at x = 0, radius 2F)."""
    R = 2 * F
    sag = R - math.sqrt(R * R - y * y)
    return -sag if concave else sag


def draw_mirror(fig, concave):
    ys = [AP * (i / 40 - 1) * 1 for i in range(81)]
    pts = [(mirror_x(y, concave), y) for y in ys]
    fig.polyline(pts, BLACK, 4)
    for y in ys[2::5]:  # hatching on the back (non-reflecting) side
        x = mirror_x(y, concave)
        fig.line((x, y), (x + 0.35, y + 0.25), GREY, 1.8)


def mirror_diagram(path, u, concave, xmin, xmax):
    f = -F if concave else F
    v = 1 / (1 / f - 1 / u)
    m = -v / u
    hi = m * H
    virtual = v > 0
    ymax = max(AP, H, hi) + 0.9
    ymin = min(-AP, hi) - 0.9
    fig = Fig(xmin, xmax, ymin, ymax)
    axis(fig, xmin, xmax, None)
    draw_mirror(fig, concave)
    pole(fig, 0)
    mark(fig, f, "F")
    mark(fig, 2 * f, "C")
    obj(fig, u)
    image(fig, v, hi, virtual)
    top, img = (u, H), (v, hi)
    # Ray 1: parallel to the axis, reflected through (or as if from) F.
    m1 = (mirror_x(H, concave), H)
    fig.ray(top, m1)
    if virtual:
        d = (m1[0] - img[0], m1[1] - img[1])
        end = (xmin + 0.3, m1[1] + d[1] / d[0] * (xmin + 0.3 - m1[0]))
        fig.ray(m1, end)
        fig.line(m1, img if concave else (f, 0), RED, 2, dash=(8, 6))
    else:
        fig.ray(m1, img, at=0.5)
    # Ray 2: to the pole, reflected at an equal angle to the axis.
    fig.ray(top, (0, 0))
    if virtual:
        d = (u, -H)
        fig.ray((0, 0), (xmin + 0.3, d[1] / d[0] * (xmin + 0.3)))
        fig.line((0, 0), img, RED, 2, dash=(8, 6))
    else:
        fig.ray((0, 0), img, at=0.5)
    fig.save(path)
    return v, m


def mirror_parts(path):
    fig = Fig(-10, 12.5, -3.9, 3.9)
    axis(fig, -10, -0.6, None)
    fig.text((-9.9, 0), "Principal axis", 15, GREY, "lb", dy=-6)
    draw_mirror(fig, True)
    pole(fig, 0)
    for x, n in [(-F, "F"), (-2 * F, "C")]:
        mark(fig, x, n)
    fig.arrow((-2 * F, -2.4), (0, -2.4), ORANGE, 2)
    fig.arrow((0, -2.4), (-2 * F, -2.4), ORANGE, 2)
    fig.text((-F, -2.4), "R = 2f", 18, ORANGE, "mt", dy=6)
    fig.text((-0.4, 3.4), "Concave mirror", 20, BLACK, "rm", bold=True)
    # Convex mirror on the right, pole at x = 3.
    ox = 3.0
    fig.line((ox - 0.5, 0), (12.5, 0), GREY, 1.8)
    ys = [AP * (i / 40 - 1) for i in range(81)]
    fig.polyline([(ox + mirror_x(y, False), y) for y in ys], BLACK, 4)
    for y in ys[2::5]:
        x = ox + mirror_x(y, False)
        fig.line((x, y), (x + 0.35, y + 0.25), GREY, 1.8)
    pole(fig, ox)
    for x, n in [(ox + F, "F"), (ox + 2 * F, "C")]:
        mark(fig, x, n)
    fig.text((ox + 0.6, 3.4), "Convex mirror", 20, BLACK, "lm", bold=True)
    fig.text((ox + F, 0), "(behind the mirror)", 14, GREY, "mt", dy=34)
    fig.save(path)


# ---------------- Lenses ----------------
def draw_lens(fig, convex):
    n = 40
    if convex:
        right = [(0.55 * math.cos(math.pi / 2 * (2 * i / n - 1)), AP * math.sin(math.pi / 2 * (2 * i / n - 1))) for i in range(n + 1)]
        left = [(-x, y) for x, y in reversed(right)]
        fig.polygon(right + left, GLASS, BLACK, 2.5)
    else:
        ys = [AP * (2 * i / n - 1) for i in range(n + 1)]
        right = [(0.15 + 0.45 * (y / AP) ** 2, y) for y in ys]
        left = [(-x, y) for x, y in reversed(right)]
        fig.polygon(right + left, GLASS, BLACK, 2.5)


def lens_diagram(path, u, convex, xmin, xmax):
    f = F if convex else -F
    v = 1 / (1 / f + 1 / u)
    m = v / u
    hi = m * H
    virtual = v < 0
    ymax = max(AP, H, hi) + 0.9
    ymin = min(-AP, hi) - 0.9
    fig = Fig(xmin, xmax, ymin, ymax)
    axis(fig, xmin, xmax, None)
    draw_lens(fig, convex)
    mark(fig, 0, "O")
    for x, n in [(-F, "F₁"), (F, "F₂"), (-2 * F, "2F₁"), (2 * F, "2F₂")]:
        if xmin < x < xmax:
            mark(fig, x, n)
    obj(fig, u)
    image(fig, v, hi, virtual)
    top, img = (u, H), (v, hi)
    # Ray 1: parallel to the axis, refracted through (or as if from) the focus.
    l1 = (0, H)
    fig.ray(top, l1)
    if virtual:
        d = (l1[0] - img[0], l1[1] - img[1])
        x_end = xmax - 0.3
        fig.ray(l1, (x_end, l1[1] + d[1] / d[0] * (x_end - l1[0])))
        fig.line(img if convex else (f, 0), l1, RED, 2, dash=(8, 6))
    else:
        x_end = min(xmax - 0.3, v + 0.8)
        fig.ray(l1, (x_end, l1[1] + (img[1] - l1[1]) / (img[0] - l1[0]) * x_end), at=0.4)
    # Ray 2: through the optical centre, undeviated.
    s = H / u  # slope of the line from the object top through O
    if virtual:
        x_end = xmax - 0.3
        fig.ray(top, (x_end, s * x_end + 0), at=0.3)
        fig.line(img, top, RED, 2, dash=(8, 6))
    else:
        x_end = min(xmax - 0.3, v + 0.8)
        fig.ray(top, (x_end, s * x_end), at=0.3)
    fig.save(path)
    return v, m


# ---------------- Refraction through a glass slab ----------------
def glass_slab(path):
    n = 1.5
    i = math.radians(45)
    r = math.asin(math.sin(i) / n)
    t = 3.0  # thickness
    fig = Fig(-5.5, 7.5, -5.2, 4.2)
    fig.rect((-5, 0), (7, -t), GLASS, BLACK, 2.5)
    fig.text((6.8, -t / 2), "Glass slab", 18, BLACK, "rm")
    O = (0.0, 0.0)
    A = (-3.6, 3.6)
    B = (t * math.tan(r), -t)
    C = (B[0] + 1.9, B[1] - 1.9)
    fig.ray(A, O)
    fig.ray(O, B)
    fig.ray(B, C)
    # Normals
    fig.line((0, 2.5), (0, -1.6), GREY, 1.8, dash=(8, 6))
    fig.line((B[0], -t + 1.6), (B[0], -t - 2.0), GREY, 1.8, dash=(8, 6))
    fig.text((0, 2.5), "Normal", 15, GREY, "mb", dy=-4)
    # Incident ray continued, to show the lateral displacement.
    fig.line(O, (4.6, -4.6), BLUE, 1.8, dash=(6, 6))
    # Perpendicular distance between the incident line (y = -x) and the emergent ray.
    foot = ((B[0] - B[1]) / 2, -(B[0] - B[1]) / 2)
    fig.arrow(foot, B, ORANGE, 2, size=10)
    fig.arrow(B, foot, ORANGE, 2, size=10)
    fig.text(lerp(foot, B, 0.5), "Lateral displacement", 15, ORANGE, "lm", dx=40, dy=10)
    fig.arc(O, 0.9, 90, 135, BLACK, 2)
    fig.text((-0.35, 1.3), "i", 20, BLACK)
    fig.arc(O, 0.9, 270, 270 + math.degrees(r), BLACK, 2)
    fig.text((0.25, -1.25), "r", 20, BLACK)
    fig.arc(B, 0.9, 270, 315, BLACK, 2)
    fig.text((B[0] + 0.35, B[1] - 1.3), "e", 20, BLACK)
    fig.text(lerp(A, O, 0.35), "Incident ray", 16, RED, "rb", dx=-10)
    fig.text(lerp(O, B, 0.45), "Refracted ray", 16, RED, "rm", dx=-16)
    fig.text(lerp(B, C, 0.6), "Emergent ray", 16, RED, "lm", dx=18)
    fig.text((-4.8, 0.3), "Air", 16, GREY, "lb")
    fig.text((-4.8, -t - 0.3), "Air", 16, GREY, "lt")
    fig.save(path)


FIGURES = [
 {"id": "s2.fig1", "after": "s2.reveal", "file": "fig_mirror_parts.png",
  "title": ("Parts of spherical mirrors", "गोलीय दर्पणों के भाग", "ગોળીય અરીસાના ભાગો"),
  "body": ("P is the pole, F the principal focus and C the centre of curvature. For a concave mirror F and C are in front of the mirror; for a convex mirror they are behind it. The radius of curvature is twice the focal length: **R = 2f**.",
           "P ध्रुव है, F मुख्य फ़ोकस और C वक्रता केंद्र। अवतल दर्पण में F और C दर्पण के सामने होते हैं; उत्तल दर्पण में वे दर्पण के पीछे होते हैं। वक्रता त्रिज्या फ़ोकस दूरी की दोगुनी होती है: **R = 2f**।",
           "P ધ્રુવ છે, F મુખ્ય કેન્દ્ર અને C વક્રતાકેન્દ્ર. અંતર્ગોળ અરીસામાં F અને C અરીસાની સામે હોય છે; બહિર્ગોળ અરીસામાં તે અરીસાની પાછળ હોય છે. વક્રતાત્રિજ્યા કેન્દ્રલંબાઈ કરતાં બમણી હોય છે: **R = 2f**.")},
 {"id": "s3.fig1", "after": "s3.table", "file": "fig_concave_beyond_c.png",
  "title": ("Concave mirror: object beyond C", "अवतल दर्पण: बिंब C से परे", "અંતર્ગોળ અરીસો: વસ્તુ C થી દૂર"),
  "body": ("A ray parallel to the axis reflects through F; a ray to the pole P reflects at an equal angle. The image forms **between F and C**: real, inverted and diminished.",
           "अक्ष के समांतर किरण परावर्तन के बाद F से गुज़रती है; ध्रुव P पर पड़ने वाली किरण बराबर कोण पर परावर्तित होती है। प्रतिबिंब **F और C के बीच** बनता है: वास्तविक, उलटा और छोटा।",
           "અક્ષને સમાંતર કિરણ પરાવર્તન પછી F માંથી પસાર થાય છે; ધ્રુવ P પર પડતું કિરણ સમાન ખૂણે પરાવર્તિત થાય છે. પ્રતિબિંબ **F અને C ની વચ્ચે** રચાય છે: વાસ્તવિક, ઊલટું અને નાનું.")},
 {"id": "s3.fig2", "after": "s3.fig1", "file": "fig_concave_between_c_f.png",
  "title": ("Concave mirror: object between C and F", "अवतल दर्पण: बिंब C और F के बीच", "અંતર્ગોળ અરીસો: વસ્તુ C અને F ની વચ્ચે"),
  "body": ("The image forms **beyond C**: real, inverted and enlarged. Here the object is at 1.5f, so the image is at 3f and twice as tall.",
           "प्रतिबिंब **C से परे** बनता है: वास्तविक, उलटा और बड़ा। यहाँ बिंब 1.5f पर है, इसलिए प्रतिबिंब 3f पर और दोगुना ऊँचा है।",
           "પ્રતિબિંબ **C થી દૂર** રચાય છે: વાસ્તવિક, ઊલટું અને મોટું. અહીં વસ્તુ 1.5f પર છે, તેથી પ્રતિબિંબ 3f પર અને બમણું ઊંચું છે.")},
 {"id": "s3.fig3", "after": "s3.fig2", "file": "fig_concave_between_f_p.png",
  "title": ("Concave mirror: object between F and P", "अवतल दर्पण: बिंब F और P के बीच", "અંતર્ગોળ અરીસો: વસ્તુ F અને P ની વચ્ચે"),
  "body": ("The reflected rays spread out, so they never meet. Extended backwards (dashed), they seem to come from a point **behind the mirror**: the image is virtual, erect and enlarged. This is how a shaving or make-up mirror works.",
           "परावर्तित किरणें फैल जाती हैं, इसलिए कभी नहीं मिलतीं। पीछे की ओर बढ़ाने पर (डैश रेखाएँ) वे **दर्पण के पीछे** के एक बिंदु से आती लगती हैं: प्रतिबिंब आभासी, सीधा और बड़ा होता है। शेविंग या मेकअप दर्पण ऐसे ही काम करता है।",
           "પરાવર્તિત કિરણો ફેલાય છે, તેથી ક્યારેય મળતાં નથી. પાછળ લંબાવતાં (તૂટક રેખાઓ) તે **અરીસાની પાછળ**ના એક બિંદુમાંથી આવતાં લાગે છે: પ્રતિબિંબ આભાસી, સીધું અને મોટું હોય છે. દાઢીનો કે મેકઅપનો અરીસો આ રીતે કામ કરે છે.")},
 {"id": "s3.fig4", "after": "s3.fig3", "file": "fig_convex_mirror.png",
  "title": ("Convex mirror: object anywhere in front", "उत्तल दर्पण: बिंब सामने कहीं भी", "બહિર્ગોળ અરીસો: વસ્તુ સામે ગમે ત્યાં"),
  "body": ("The parallel ray reflects as if it came from F behind the mirror. The image is always **between P and F**, virtual, erect and diminished, which gives a wide view. That is why vehicles use convex rear-view mirrors.",
           "समांतर किरण ऐसे परावर्तित होती है मानो दर्पण के पीछे F से आ रही हो। प्रतिबिंब हमेशा **P और F के बीच**, आभासी, सीधा और छोटा बनता है, जिससे दृश्य-क्षेत्र बड़ा मिलता है। इसीलिए वाहनों में उत्तल पश्च-दृश्य दर्पण लगते हैं।",
           "સમાંતર કિરણ જાણે અરીસાની પાછળના F માંથી આવતું હોય તેમ પરાવર્તિત થાય છે. પ્રતિબિંબ હંમેશાં **P અને F ની વચ્ચે**, આભાસી, સીધું અને નાનું રચાય છે, જેથી વિશાળ દૃશ્ય મળે છે. તેથી વાહનોમાં બહિર્ગોળ રિયર-વ્યૂ અરીસા વપરાય છે.")},
 {"id": "s5.fig1", "after": "s5.thm", "file": "fig_glass_slab.png",
  "title": ("Refraction through a rectangular glass slab", "काँच के आयताकार स्लैब से अपवर्तन", "કાચના લંબઘન સ્લૅબમાંથી વક્રીભવન"),
  "body": ("Entering glass, the ray bends **towards** the normal (r < i); leaving it, the ray bends **away** from the normal. The emergent ray is **parallel** to the incident ray (e = i) but shifted sideways: this shift is the lateral displacement.",
           "काँच में जाते समय किरण अभिलंब की **ओर** मुड़ती है (r < i); बाहर निकलते समय अभिलंब से **दूर** मुड़ती है। निर्गत किरण आपतित किरण के **समांतर** होती है (e = i), पर बगल में खिसक जाती है: इसी खिसकाव को पार्श्व विस्थापन कहते हैं।",
           "કાચમાં પ્રવેશતાં કિરણ લંબ **તરફ** વળે છે (r < i); બહાર નીકળતાં લંબથી **દૂર** વળે છે. નિર્ગમન કિરણ આપાત કિરણને **સમાંતર** હોય છે (e = i), પણ બાજુ પર ખસી જાય છે: આ ખસવાને પાર્શ્વીય સ્થાનાંતર કહે છે.")},
 {"id": "s6.fig1", "after": "s6.table", "file": "fig_convex_lens_beyond_2f.png",
  "title": ("Convex lens: object beyond 2F₁", "उत्तल लेंस: बिंब 2F₁ से परे", "બહિર્ગોળ લેન્સ: વસ્તુ 2F₁ થી દૂર"),
  "body": ("A ray parallel to the axis refracts through F₂; a ray through the optical centre O goes straight. The image forms **between F₂ and 2F₂**: real, inverted and diminished, as in a camera.",
           "अक्ष के समांतर किरण अपवर्तन के बाद F₂ से गुज़रती है; प्रकाशिक केंद्र O से जाने वाली किरण सीधी निकल जाती है। प्रतिबिंब **F₂ और 2F₂ के बीच** बनता है: वास्तविक, उलटा और छोटा, जैसे कैमरे में।",
           "અક્ષને સમાંતર કિરણ વક્રીભવન પછી F₂ માંથી પસાર થાય છે; પ્રકાશીય કેન્દ્ર O માંથી જતું કિરણ સીધું નીકળી જાય છે. પ્રતિબિંબ **F₂ અને 2F₂ ની વચ્ચે** રચાય છે: વાસ્તવિક, ઊલટું અને નાનું, જેમ કૅમેરામાં.")},
 {"id": "s6.fig2", "after": "s6.fig1", "file": "fig_convex_lens_between_f_2f.png",
  "title": ("Convex lens: object between F₁ and 2F₁", "उत्तल लेंस: बिंब F₁ और 2F₁ के बीच", "બહિર્ગોળ લેન્સ: વસ્તુ F₁ અને 2F₁ ની વચ્ચે"),
  "body": ("The image forms **beyond 2F₂**: real, inverted and enlarged, as in a projector. Here the object is at 1.5f, so the image is at 3f and twice as tall.",
           "प्रतिबिंब **2F₂ से परे** बनता है: वास्तविक, उलटा और बड़ा, जैसे प्रोजेक्टर में। यहाँ बिंब 1.5f पर है, इसलिए प्रतिबिंब 3f पर और दोगुना ऊँचा है।",
           "પ્રતિબિંબ **2F₂ થી દૂર** રચાય છે: વાસ્તવિક, ઊલટું અને મોટું, જેમ પ્રોજેક્ટરમાં. અહીં વસ્તુ 1.5f પર છે, તેથી પ્રતિબિંબ 3f પર અને બમણું ઊંચું છે.")},
 {"id": "s6.fig3", "after": "s6.fig2", "file": "fig_convex_lens_magnifier.png",
  "title": ("Convex lens: object between F₁ and O", "उत्तल लेंस: बिंब F₁ और O के बीच", "બહિર્ગોળ લેન્સ: વસ્તુ F₁ અને O ની વચ્ચે"),
  "body": ("The refracted rays spread out; extended backwards (dashed) they meet on the **same side as the object**. The image is virtual, erect and enlarged: the lens works as a magnifying glass.",
           "अपवर्तित किरणें फैल जाती हैं; पीछे बढ़ाने पर (डैश रेखाएँ) वे **बिंब की ओर ही** मिलती हैं। प्रतिबिंब आभासी, सीधा और बड़ा होता है: लेंस आवर्धक लेंस की तरह काम करता है।",
           "વક્રીભૂત કિરણો ફેલાય છે; પાછળ લંબાવતાં (તૂટક રેખાઓ) તે **વસ્તુની બાજુએ જ** મળે છે. પ્રતિબિંબ આભાસી, સીધું અને મોટું હોય છે: લેન્સ બિલોરી કાચ તરીકે કામ કરે છે.")},
 {"id": "s6.fig4", "after": "s6.fig3", "file": "fig_concave_lens.png",
  "title": ("Concave lens: object anywhere", "अवतल लेंस: बिंब कहीं भी", "અંતર્ગોળ લેન્સ: વસ્તુ ગમે ત્યાં"),
  "body": ("The parallel ray diverges as if it came from F₁. The image is always **between F₁ and O**, on the object's side: virtual, erect and diminished.",
           "समांतर किरण ऐसे फैलती है मानो F₁ से आ रही हो। प्रतिबिंब हमेशा बिंब की ओर **F₁ और O के बीच** बनता है: आभासी, सीधा और छोटा।",
           "સમાંતર કિરણ જાણે F₁ માંથી આવતું હોય તેમ ફેલાય છે. પ્રતિબિંબ હંમેશાં વસ્તુની બાજુએ **F₁ અને O ની વચ્ચે** રચાય છે: આભાસી, સીધું અને નાનું.")},
]


if __name__ == "__main__":
    from insert import insert_figures
    out = sys.argv[1].rstrip("/")
    mirror_parts(f"{out}/fig_mirror_parts.png")
    print("concave beyond C", mirror_diagram(f"{out}/fig_concave_beyond_c.png", -11, True, -12.5, 1.2))
    print("concave C-F", mirror_diagram(f"{out}/fig_concave_between_c_f.png", -6, True, -13.5, 1.2))
    print("concave F-P", mirror_diagram(f"{out}/fig_concave_between_f_p.png", -2.5, True, -9.5, 7.5))
    print("convex mirror", mirror_diagram(f"{out}/fig_convex_mirror.png", -8, False, -9.5, 9.5))
    glass_slab(f"{out}/fig_glass_slab.png")
    print("convex lens beyond 2F", lens_diagram(f"{out}/fig_convex_lens_beyond_2f.png", -11, True, -12.5, 9.5))
    print("convex lens F-2F", lens_diagram(f"{out}/fig_convex_lens_between_f_2f.png", -6, True, -9.5, 13.5))
    print("convex lens F-O", lens_diagram(f"{out}/fig_convex_lens_magnifier.png", -2.5, True, -9.5, 7.5))
    print("concave lens", lens_diagram(f"{out}/fig_concave_lens.png", -8, False, -9.5, 7.5))
    insert_figures(out, FIGURES)
