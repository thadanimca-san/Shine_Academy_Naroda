"""Diagrams for Class 10 Science Ch 10 (The Human Eye and the Colourful World).

Prism rays follow Snell's law (n = 1.5, A = 60°). In the dispersion figure the
spread between colours is exaggerated so the seven bands can be seen.
Usage: python3 tools/diagrams/sci10_eye.py <chapter folder>
"""
import math
import sys
from figlib import Fig, BLACK, GREY, RED, BLUE, GREEN, ORANGE, GLASS, lerp

# ---------------- vector helpers ----------------
def unit(v):
    n = math.hypot(*v)
    return (v[0] / n, v[1] / n)


def refract(d, normal, n1, n2):
    """Refract unit direction d at a surface with unit normal pointing against d."""
    cos_i = -(d[0] * normal[0] + d[1] * normal[1])
    k = n1 / n2
    cos_t = math.sqrt(1 - k * k * (1 - cos_i * cos_i))
    return unit((k * d[0] + (k * cos_i - cos_t) * normal[0], k * d[1] + (k * cos_i - cos_t) * normal[1]))


def hit(p, d, a, b):
    """Where the ray p + t d meets the line through a and b."""
    ex, ey = b[0] - a[0], b[1] - a[1]
    den = d[0] * ey - d[1] * ex
    t = ((a[0] - p[0]) * ey - (a[1] - p[1]) * ex) / den
    return (p[0] + t * d[0], p[1] + t * d[1])


def rotate(v, deg):
    a = math.radians(deg)
    return (v[0] * math.cos(a) - v[1] * math.sin(a), v[0] * math.sin(a) + v[1] * math.cos(a))


S3 = math.sqrt(3)
B, C, A = (-3.0, 0.0), (3.0, 0.0), (0.0, 3 * S3)       # equilateral prism, A = 60°
LEFT_OUT = unit((-S3 / 2, 0.5))                         # outward normal of face BA
RIGHT_OUT = unit((S3 / 2, 0.5))                         # outward normal of face AC


def prism_path(n, i_deg=48):
    p = lerp(B, A, 0.5)
    d_in = unit(rotate((-LEFT_OUT[0], -LEFT_OUT[1]), i_deg))
    d_glass = refract(d_in, LEFT_OUT, 1.0, n)
    q = hit(p, d_glass, A, C)
    d_out = refract(d_glass, (-RIGHT_OUT[0], -RIGHT_OUT[1]), n, 1.0)
    return p, d_in, q, d_glass, d_out


def draw_prism(fig):
    fig.polygon([B, C, A], GLASS, BLACK, 2.5)


def prism_refraction(path):
    fig = Fig(-8.5, 9.5, -1.8, 6.6)
    draw_prism(fig)
    p, d_in, q, d_glass, d_out = prism_path(1.5)
    start = (p[0] - 5 * d_in[0], p[1] - 5 * d_in[1])
    end = (q[0] + 5.5 * d_out[0], q[1] + 5.5 * d_out[1])
    fig.ray(start, p)
    fig.ray(p, q)
    fig.ray(q, end)
    # Normals at both faces.
    for pt, nrm in ((p, LEFT_OUT), (q, RIGHT_OUT)):
        fig.line((pt[0] + 1.6 * nrm[0], pt[1] + 1.6 * nrm[1]), (pt[0] - 1.3 * nrm[0], pt[1] - 1.3 * nrm[1]), GREY, 1.8, dash=(8, 6))
    # Incident ray produced, to show the angle of deviation.
    far = (p[0] + 7.5 * d_in[0], p[1] + 7.5 * d_in[1])
    fig.line(p, far, BLUE, 1.8, dash=(6, 6))
    meet = hit(p, d_in, q, (q[0] + d_out[0], q[1] + d_out[1]))
    a_in = math.degrees(math.atan2(d_in[1], d_in[0]))
    a_out = math.degrees(math.atan2(d_out[1], d_out[0]))
    fig.line(meet, q, ORANGE, 1.8, dash=(6, 6))
    fig.arc(meet, 0.9, a_out, a_in, ORANGE, 2.5)
    mid = math.radians((a_in + a_out) / 2)
    fig.text((meet[0] + 1.25 * math.cos(mid), meet[1] + 1.25 * math.sin(mid)), "D", 20, ORANGE, bold=True)
    fig.arc(A, 0.9, 240, 300, BLACK, 2)
    fig.text((A[0], A[1] - 1.35), "A", 20, BLACK, bold=True)
    fig.text(lerp(start, p, 0.3), "Incident ray", 16, RED, "rb", dx=-6, dy=-6)
    fig.text(lerp(q, end, 0.6), "Emergent ray", 16, RED, "lt", dx=6, dy=10)
    fig.text((0, 0.7), "Refracted ray", 15, RED, "mm")
    fig.text((-6.5, 6.0), "A = angle of the prism", 16, BLACK, "lm")
    fig.text((-6.5, 5.3), "D = angle of deviation", 16, ORANGE, "lm")
    fig.save(path)


COLOURS = [("Red", (220, 30, 30)), ("Orange", (245, 130, 20)), ("Yellow", (225, 190, 0)), ("Green", (20, 160, 60)),
           ("Blue", (30, 90, 230)), ("Indigo", (75, 0, 160)), ("Violet", (150, 40, 200))]


def dispersion(path):
    fig = Fig(-8.5, 11.5, -4.2, 6.6)
    draw_prism(fig)
    screen_x = 10.0
    fig.line((screen_x, 2.6), (screen_x, -4.0), BLACK, 5)
    fig.text((screen_x, 2.6), "Screen", 16, BLACK, "mb", dy=-8)
    p = None
    for k, (name, rgb) in enumerate(COLOURS):
        n = 1.47 + 0.025 * k   # exaggerated: red bends least, violet most
        p, d_in, q, d_glass, d_out = prism_path(n)
        t = (screen_x - q[0]) / d_out[0]
        end = (screen_x, q[1] + t * d_out[1])
        fig.line(p, q, rgb, 2)
        fig.line(q, end, rgb, 2.5)
        fig.text(end, name, 15, rgb, "lm", dx=12, bold=True)
    start = (p[0] - 5 * d_in[0], p[1] - 5 * d_in[1])
    fig.line(start, p, BLACK, 5)
    fig.head(lerp(start, p, 0.6), d_in, BLACK, 16)
    fig.text(lerp(start, p, 0.3), "White light", 17, BLACK, "rb", dx=-6, dy=-6, bold=True)
    fig.text((0, -0.9), "Glass prism", 16, BLACK)
    fig.save(path)


# ---------------- Eye ----------------
R_EYE = 2.0
LENS_X = 0.45
RETINA_X = 2 * R_EYE


def draw_eye(fig, oy, label=True):
    fig.circle((R_EYE, oy), R_EYE, BLACK, 2.5, fill=(250, 246, 238))
    fig.arc((R_EYE, oy), R_EYE, -35, 35, ORANGE, 6)
    fig.ellipse((LENS_X, oy), 0.22, 0.85, BLACK, 2, fill=GLASS)
    if label:
        fig.text((RETINA_X, oy - 1.2), "Retina", 15, ORANGE, "lm", dx=14)
        fig.text((LENS_X, oy + 0.85), "Eye lens", 15, BLACK, "mb", dy=-6)


def corr_lens(fig, x, oy, concave):
    n = 30
    ys = [1.4 * (2 * i / n - 1) for i in range(n + 1)]
    if concave:
        right = [(x + 0.1 + 0.25 * (y / 1.4) ** 2, oy + y) for y in ys]
    else:
        right = [(x + 0.3 * math.cos(math.pi / 2 * (2 * i / n - 1)), oy + 1.4 * math.sin(math.pi / 2 * (2 * i / n - 1))) for i in range(n + 1)]
    left = [(2 * x - px, py) for px, py in reversed(right)]
    fig.polygon(right + left, GLASS, BLACK, 2)


def panel_title(fig, x, oy, text):
    fig.text((x, oy + 2.4), text, 18, BLACK, "lm", bold=True)


def myopia(path):
    fig = Fig(-8.6, 6.8, -5.0, 5.2)
    xl, far = -2.0, -7.0
    # (a) defect: parallel rays meet in front of the retina.
    oy = 2.3
    panel_title(fig, -8.4, oy, "(a) Myopic eye")
    draw_eye(fig, oy)
    focus = (RETINA_X - 1.0, oy)
    for h in (0.6, -0.6):
        e = (LENS_X, oy + h)
        fig.ray((-8.0, oy + h), e)
        beyond = lerp(e, focus, (RETINA_X - 0.08 - LENS_X) / (focus[0] - LENS_X))
        fig.line(e, beyond, (214, 48, 49), 2.5)
    fig.dot(focus, 4, BLUE)
    fig.text((focus[0], oy - R_EYE), "Image in front of the retina", 14, BLUE, "mt", dy=6)
    fig.text((-8.0, oy - 0.9), "From a distant object", 14, GREY, "lm")
    # (b) correction: a concave lens makes the rays seem to come from the far point.
    oy = -2.6
    panel_title(fig, -8.4, oy, "(b) Corrected with a concave lens")
    draw_eye(fig, oy, label=False)
    corr_lens(fig, xl, oy, concave=True)
    fig.dot((far, oy), 4.5)
    fig.text((far, oy), "F (far point)", 14, BLACK, "mt", dy=8)
    for h in (0.45, -0.45):
        l = (xl, oy + h)
        fig.ray((-8.4, oy + h), l, at=0.5)
        hh = h * (LENS_X - far) / (xl - far)
        e = (LENS_X, oy + hh)
        fig.line(l, e, (214, 48, 49), 2.5)
        fig.line((far, oy), l, (214, 48, 49), 1.5, dash=(6, 6))
        fig.ray(e, (RETINA_X, oy), at=0.5)
    fig.dot((RETINA_X, oy), 4, BLUE)
    fig.text((RETINA_X, oy), "Image on the retina", 14, BLUE, "lm", dx=12)
    fig.save(path)


def hypermetropia(path):
    fig = Fig(-10.6, 7.6, -5.0, 5.2)
    xl, near, near_d = -2.0, -5.0, -9.5
    # (a) defect: rays from the normal near point meet behind the retina.
    oy = 2.3
    panel_title(fig, -10.4, oy, "(a) Hypermetropic eye")
    draw_eye(fig, oy)
    focus = (RETINA_X + 1.0, oy)
    fig.dot((near, oy), 4.5)
    fig.text((near, oy), "N (normal near point)", 14, BLACK, "mt", dy=8)
    for h in (0.6, -0.6):
        e = (LENS_X, oy + h)
        fig.ray((near, oy), e)
        on_retina = lerp(e, focus, (RETINA_X - LENS_X) / (focus[0] - LENS_X))
        fig.line(e, on_retina, (214, 48, 49), 2.5)
        fig.line(on_retina, focus, (214, 48, 49), 1.5, dash=(6, 6))
    fig.dot(focus, 4, BLUE)
    fig.text(focus, "Image behind the retina", 14, BLUE, "lm", dx=10)
    # (b) correction: a convex lens makes rays from N seem to come from N'.
    oy = -2.6
    panel_title(fig, -10.4, oy, "(b) Corrected with a convex lens")
    draw_eye(fig, oy, label=False)
    corr_lens(fig, xl, oy, concave=False)
    for x, name, below in ((near, "N", True), (near_d, "N′", True)):
        fig.dot((x, oy), 4.5)
        fig.text((x, oy), name, 15, BLACK, "mt", dy=8, bold=True)
    for h in (0.75, -0.75):
        l = (xl, oy + h)
        fig.ray((near, oy), l)
        hh = h * (LENS_X - near_d) / (xl - near_d)
        e = (LENS_X, oy + hh)
        fig.line(l, e, (214, 48, 49), 2.5)
        fig.line((near_d, oy), l, (214, 48, 49), 1.5, dash=(6, 6))
        fig.ray(e, (RETINA_X, oy), at=0.5)
    fig.dot((RETINA_X, oy), 4, BLUE)
    fig.text((RETINA_X, oy), "Image on the retina", 14, BLUE, "lm", dx=12)
    fig.save(path)


FIGURES = [
 {"id": "s3.fig1", "after": "s3.table", "file": "fig_myopia.png",
  "title": ("Myopia and its correction", "निकट-दृष्टि दोष और उसका निवारण", "લઘુદૃષ્ટિની ખામી અને તેનું નિવારણ"),
  "body": ("(a) Light from a distant object meets **in front of the retina**, so far things look blurred. (b) A **concave lens** of suitable power spreads the rays so they seem to come from the far point F; the eye then focuses them **on the retina**.",
           "(a) दूर की वस्तु का प्रकाश **दृष्टिपटल के सामने** मिलता है, इसलिए दूर की चीज़ें धुँधली दिखती हैं। (b) उचित क्षमता का **अवतल लेंस** किरणों को फैला देता है, जिससे वे दूर बिंदु F से आती लगती हैं; तब आँख उन्हें **दृष्टिपटल पर** फ़ोकस करती है।",
           "(a) દૂરની વસ્તુનો પ્રકાશ **નેત્રપટલની આગળ** મળે છે, તેથી દૂરની વસ્તુઓ ઝાંખી દેખાય છે. (b) યોગ્ય પાવરનો **અંતર્ગોળ લેન્સ** કિરણોને ફેલાવે છે, જેથી તે દૂરબિંદુ F માંથી આવતાં લાગે છે; પછી આંખ તેમને **નેત્રપટલ પર** કેન્દ્રિત કરે છે.")},
 {"id": "s3.fig2", "after": "s3.fig1", "file": "fig_hypermetropia.png",
  "title": ("Hypermetropia and its correction", "दीर्घ-दृष्टि दोष और उसका निवारण", "ગુરુદૃષ્ટિની ખામી અને તેનું નિવારણ"),
  "body": ("(a) Light from a near object (at N, 25 cm) would meet **behind the retina**, so near things look blurred. (b) A **convex lens** makes the rays seem to come from N′, the near point of this eye, which it can focus **on the retina**.",
           "(a) पास की वस्तु (N, 25 cm पर) का प्रकाश **दृष्टिपटल के पीछे** मिलता, इसलिए पास की चीज़ें धुँधली दिखती हैं। (b) **उत्तल लेंस** किरणों को ऐसा बना देता है मानो वे N′ से आ रही हों, जो इस आँख का निकट बिंदु है; आँख उन्हें **दृष्टिपटल पर** फ़ोकस कर लेती है।",
           "(a) નજીકની વસ્તુ (N, 25 cm પર)નો પ્રકાશ **નેત્રપટલની પાછળ** મળત, તેથી નજીકની વસ્તુઓ ઝાંખી દેખાય છે. (b) **બહિર્ગોળ લેન્સ** કિરણોને એવાં બનાવે છે જાણે તે N′ માંથી આવતાં હોય, જે આ આંખનું નજીકબિંદુ છે; આંખ તેમને **નેત્રપટલ પર** કેન્દ્રિત કરી શકે છે.")},
 {"id": "s4.fig1", "after": "s4.thm", "file": "fig_prism_refraction.png",
  "title": ("Refraction through a glass prism", "काँच के प्रिज़्म से अपवर्तन", "કાચના પ્રિઝમમાંથી વક્રીભવન"),
  "body": ("The ray bends **towards the base** at both faces. The angle between the incident ray (produced, dashed) and the emergent ray is the **angle of deviation D**; A is the angle of the prism.",
           "किरण दोनों फलकों पर **आधार की ओर** मुड़ती है। आपतित किरण (आगे बढ़ाई गई, डैश रेखा) और निर्गत किरण के बीच का कोण **विचलन कोण D** है; A प्रिज़्म कोण है।",
           "કિરણ બંને સપાટીઓ પર **પાયા તરફ** વળે છે. આપાત કિરણ (લંબાવેલું, તૂટક રેખા) અને નિર્ગમન કિરણ વચ્ચેનો ખૂણો **વિચલનકોણ D** છે; A પ્રિઝમકોણ છે.")},
 {"id": "s4.fig2", "after": "s4.fig1", "file": "fig_dispersion.png",
  "title": ("Dispersion of white light", "श्वेत प्रकाश का विक्षेपण", "શ્વેત પ્રકાશનું વિભાજન"),
  "body": ("A prism splits white light into the seven colours of the spectrum. **Red bends the least and violet the most.** (The spread is drawn larger than real so each colour can be seen.)",
           "प्रिज़्म श्वेत प्रकाश को स्पेक्ट्रम के सात रंगों में बाँट देता है। **लाल सबसे कम और बैंगनी सबसे अधिक मुड़ता है।** (हर रंग दिख सके, इसलिए फैलाव असल से बड़ा दिखाया गया है।)",
           "પ્રિઝમ શ્વેત પ્રકાશને વર્ણપટના સાત રંગોમાં વહેંચી દે છે. **લાલ સૌથી ઓછો અને જાંબલી સૌથી વધુ વળે છે.** (દરેક રંગ દેખાય તે માટે ફેલાવો ખરેખર કરતાં મોટો દર્શાવ્યો છે.)")},
]


if __name__ == "__main__":
    from insert import insert_figures
    out = sys.argv[1].rstrip("/")
    myopia(f"{out}/fig_myopia.png")
    hypermetropia(f"{out}/fig_hypermetropia.png")
    prism_refraction(f"{out}/fig_prism_refraction.png")
    dispersion(f"{out}/fig_dispersion.png")
    if "--draw-only" not in sys.argv:
        insert_figures(out, FIGURES)
