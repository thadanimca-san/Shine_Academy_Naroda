"""Labelled schematic diagrams for Class 10 Science Ch 7 (How do Organisms Reproduce?).
Human reproductive organs are left to teacher-supplied pictures.
Usage: python3 tools/diagrams/sci07_reproduction.py <chapter folder>
"""
import math
import sys
from figlib import Fig, BLACK, GREY, RED, BLUE, GREEN, ORANGE, PURPLE, label, lerp

CYTO, NUC = (205, 230, 250), (120, 80, 170)
HYDRA = (240, 200, 150)


def blob(c, rx, ry, wobble=0.08, n=60, seed=0):
    return [(c[0] + rx * (1 + wobble * math.sin(3 * a + seed)) * math.cos(a), c[1] + ry * (1 + wobble * math.cos(2 * a + seed)) * math.sin(a))
            for a in (2 * math.pi * i / n for i in range(n))]


def stage_arrow(fig, x, y):
    fig.arrow((x - 0.5, y), (x + 0.5, y), GREY, 3, size=14)


def binary_fission(path):
    fig = Fig(-1.6, 21.2, -2.8, 2.4)
    y = 0.0
    # 1: one cell
    fig.polygon(blob((0.4, y), 1.6, 1.3), CYTO, BLUE, 2.5)
    fig.ellipse((0.4, y), 0.45, 0.35, NUC, 2, fill=(210, 190, 235))
    stage_arrow(fig, 3.0, y)
    # 2: nucleus divides
    fig.polygon(blob((5.8, y), 1.9, 1.2), CYTO, BLUE, 2.5)
    fig.ellipse((5.2, y), 0.35, 0.3, NUC, 2, fill=(210, 190, 235))
    fig.ellipse((6.4, y), 0.35, 0.3, NUC, 2, fill=(210, 190, 235))
    stage_arrow(fig, 8.6, y)
    # 3: cytoplasm pinches in the middle
    pts = []
    for i in range(80):
        a = 2 * math.pi * i / 80
        x = 2.2 * math.cos(a)
        r = 1.15 * (1 - 0.65 * math.exp(-(x / 0.6) ** 2))
        pts.append((11.6 + x, y + r * math.sin(a)))
    fig.polygon(pts, CYTO, BLUE, 2.5)
    fig.ellipse((10.6, y), 0.35, 0.3, NUC, 2, fill=(210, 190, 235))
    fig.ellipse((12.6, y), 0.35, 0.3, NUC, 2, fill=(210, 190, 235))
    stage_arrow(fig, 14.4, y)
    # 4: two daughter cells
    for cx in (16.4, 19.4):
        fig.polygon(blob((cx, y), 1.2, 1.0, seed=cx), CYTO, BLUE, 2.5)
        fig.ellipse((cx, y), 0.35, 0.3, NUC, 2, fill=(210, 190, 235))
    for x, t in ((0.4, "Parent cell"), (5.8, "Nucleus divides"), (11.6, "Cytoplasm divides"), (17.9, "Two daughter cells")):
        fig.text((x, -2.0), t, 15, BLACK, bold=True)
    fig.save(path)


def hydra_body(fig, base, height, lean=0.0):
    """A simple hydra: a tube with a ring of tentacles at the top."""
    bx, by = base
    w = 0.45
    top = (bx + lean, by + height)
    fig.polygon([(bx - w, by), (bx + w, by), (top[0] + w * 0.8, top[1]), (top[0] - w * 0.8, top[1])], HYDRA, (170, 110, 50), 2.5)
    for ang in (60, 85, 105, 125):
        a = math.radians(ang)
        fig.line(top, (top[0] + 1.3 * math.cos(a) * (1 if ang < 95 else 1), top[1] + 1.3 * math.sin(a)), (170, 110, 50), 2.5)
    return top


def budding(path):
    fig = Fig(-1.6, 17.6, -1.6, 6.6)
    ground = 0.0
    for k, (x, bud) in enumerate(((0.8, 0.0), (6.0, 0.6), (11.2, 1.0))):
        hydra_body(fig, (x, ground), 4.2)
        if bud:
            # Bud grows out of the side and develops tentacles.
            b0 = (x + 0.4, 1.8)
            tip = (x + 0.4 + 1.6 * bud, 1.8 + 1.4 * bud)
            fig.polygon([(b0[0], b0[1] - 0.35), (b0[0], b0[1] + 0.35), (tip[0] - 0.2, tip[1] + 0.25), (tip[0] + 0.2, tip[1] - 0.25)], HYDRA, (170, 110, 50), 2.5)
            if bud > 0.8:
                for ang in (30, 60, 90):
                    a = math.radians(ang)
                    fig.line(tip, (tip[0] + 0.8 * math.cos(a), tip[1] + 0.8 * math.sin(a)), (170, 110, 50), 2)
        if k < 2:
            stage_arrow(fig, x + 2.6, 2.0)
    # Last stage: the bud detaches as a new hydra.
    stage_arrow(fig, 13.6, 2.0)
    hydra_body(fig, (15.6, ground), 3.0)
    fig.line((-1.0, ground), (17.2, ground), GREY, 2)
    label(fig, (6.0 + 0.4 + 0.5, 2.3), (8.0, 5.6), "Bud", anchor="mm")
    fig.text((15.6, 4.9), "New hydra", 15, BLACK, bold=True)
    fig.text((0.8, 6.0), "Parent hydra", 15, BLACK, bold=True)
    fig.save(path)


def flower(path):
    fig = Fig(-8.2, 8.2, -6.4, 7.0)
    stalk = (0, -6.0)
    fig.line(stalk, (0, -3.0), (60, 140, 60), 6)
    # Thalamus and sepals.
    fig.ellipse((0, -2.8), 1.2, 0.45, (60, 140, 60), 2.5, fill=(150, 200, 120))
    for s in (-1, 1):
        fig.polygon([(s * 0.6, -2.7), (s * 2.6, -1.4), (s * 1.0, -1.9)], (120, 190, 100), (60, 140, 60), 2.5)
        # Petals: large curved shapes behind the inner parts.
        petal = [(s * 0.9, -2.3)] + [(s * (1.2 + 3.0 * math.sin(math.pi * t)), -2.3 + 6.2 * t) for t in [i / 20 for i in range(21)]]
        fig.polygon(petal, (255, 200, 220), (210, 90, 140), 2.5)
    # Pistil: ovary with ovules, style, stigma; pollen tube growing down to an ovule.
    fig.ellipse((0, -1.4), 1.1, 1.2, (110, 160, 60), 2.5, fill=(200, 230, 160))
    for y in (-1.9, -1.0):
        fig.ellipse((0.35, y), 0.25, 0.2, (90, 120, 40), 2, fill=(250, 245, 200))
    fig.ellipse((-0.35, -1.45), 0.25, 0.2, (90, 120, 40), 2, fill=(250, 245, 200))
    fig.rect((-0.18, -0.25), (0.18, 3.3), (200, 230, 160), (110, 160, 60), 2.5)
    fig.ellipse((0, 3.55), 0.75, 0.32, (110, 160, 60), 2.5, fill=(230, 210, 90))
    # Stamens: filament + anther, with pollen grains.
    for s in (-1, 1):
        fig.line((s * 0.6, -2.4), (s * 1.9, 2.4), (200, 150, 40), 3)
        fig.ellipse((s * 1.95, 2.75), 0.35, 0.5, (190, 120, 20), 2.5, fill=(250, 200, 60))
    for p in ((-0.3, 3.85), (0.25, 3.9), (0.6, 3.75)):
        fig.dot(p, 5, (230, 150, 0))
    fig.polyline([(0.25, 3.85), (0.05, 3.0), (0.06, 0.0), (0.12, -0.6), (0.35, -0.85)], ORANGE, 2.5)
    label(fig, (0.0, 3.7), (-4.0, 6.0), "Stigma", anchor="rm")
    label(fig, (0.0, 1.5), (-5.5, 1.5), "Style", anchor="rm")
    label(fig, (-0.9, -1.2), (-5.5, -0.6), "Ovary", anchor="rm")
    label(fig, (-0.35, -1.45), (-5.5, -1.7), "Ovule", anchor="rm")
    label(fig, (1.95, 2.95), (4.6, 5.6), "Anther", anchor="lm")
    label(fig, (1.4, 0.4), (5.0, 1.5), "Filament", anchor="lm")
    label(fig, (3.6, 1.0), (5.0, 3.2), "Petal", anchor="lm")
    label(fig, (2.0, -1.6), (5.0, -1.6), "Sepal", anchor="lm")
    label(fig, (0.1, 0.5), (5.0, -0.2), "Pollen tube", anchor="lm", color=ORANGE)
    label(fig, (0.6, 3.75), (4.6, 6.6), "Pollen grains", anchor="lm")
    fig.text((-5.5, -3.6), "Pistil = stigma + style + ovary", 14, GREY, "lm")
    fig.text((-5.5, -4.2), "Stamen = anther + filament", 14, GREY, "lm")
    fig.save(path)


FIGURES = [
 {"id": "s3.fig1", "after": "s3.table", "file": "fig_binary_fission.png",
  "title": ("Binary fission in Amoeba", "अमीबा में द्विखंडन", "અમીબામાં દ્વિભાજન"),
  "body": ("The nucleus divides first, then the cytoplasm pinches in the middle, giving **two daughter cells**. In Amoeba the cell can split in any plane; in Leishmania it splits in a definite plane.",
           "पहले केंद्रक विभाजित होता है, फिर कोशिकाद्रव्य बीच से सिकुड़ता है और **दो संतति कोशिकाएँ** बनती हैं। अमीबा में कोशिका किसी भी तल में बँट सकती है; लेस्मानिया में एक निश्चित तल में।",
           "પહેલાં કોષકેન્દ્ર વિભાજિત થાય છે, પછી કોષરસ વચ્ચેથી સંકોચાય છે અને **બે બાળકોષો** બને છે. અમીબામાં કોષ કોઈ પણ સમતલમાં વિભાજિત થઈ શકે; લીશ્માનિયામાં ચોક્કસ સમતલમાં.")},
 {"id": "s3.fig2", "after": "s3.fig1", "file": "fig_budding_hydra.png",
  "title": ("Budding in Hydra", "हाइड्रा में मुकुलन", "હાઇડ્રામાં કલિકાસર્જન"),
  "body": ("A **bud** grows out from the side of the parent by repeated cell division. It develops tentacles, becomes a tiny hydra and then **detaches** to live on its own.",
           "बार-बार कोशिका विभाजन से जनक के एक ओर **मुकुल** (कलिका) निकलती है। उसमें स्पर्शक बनते हैं, वह छोटा हाइड्रा बन जाती है और फिर **अलग** होकर स्वतंत्र रहने लगती है।",
           "વારંવાર કોષવિભાજનથી પિતૃની એક બાજુએ **કલિકા** ઊપસે છે. તેમાં સૂત્રાંગો વિકસે છે, તે નાનો હાઇડ્રા બને છે અને પછી **છૂટી પડી** સ્વતંત્ર જીવે છે.")},
 {"id": "s4.fig1", "after": "s4.thm", "file": "fig_flower_ls.png",
  "title": ("Longitudinal section of a flower", "पुष्प की अनुदैर्ध्य काट", "પુષ્પનો ઊભો છેદ"),
  "body": ("The **stamen** (anther + filament) makes pollen; the **pistil** (stigma + style + ovary) holds the ovules. After pollination a **pollen tube** grows from the pollen grain on the stigma, down the style, to reach an ovule for fertilisation.",
           "**पुंकेसर** (परागकोश + तंतु) पराग बनाता है; **स्त्रीकेसर** (वर्तिकाग्र + वर्तिका + अंडाशय) में बीजांड होते हैं। परागण के बाद वर्तिकाग्र पर पड़े परागकण से **पराग नलिका** निकलकर वर्तिका से होती हुई बीजांड तक पहुँचती है, जहाँ निषेचन होता है।",
           "**પુંકેસર** (પરાગાશય + તંતુ) પરાગ બનાવે છે; **સ્ત્રીકેસર** (પરાગાસન + પરાગવાહિની + બીજાશય)માં અંડકો હોય છે. પરાગનયન પછી પરાગાસન પરના પરાગરજમાંથી **પરાગનલિકા** નીકળી પરાગવાહિની દ્વારા અંડક સુધી પહોંચે છે, જ્યાં ફલન થાય છે.")},
]


if __name__ == "__main__":
    from insert import insert_figures
    out = sys.argv[1].rstrip("/")
    binary_fission(f"{out}/fig_binary_fission.png")
    budding(f"{out}/fig_budding_hydra.png")
    flower(f"{out}/fig_flower_ls.png")
    if "--draw-only" not in sys.argv:
        insert_figures(out, FIGURES)
