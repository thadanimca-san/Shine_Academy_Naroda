"""Labelled schematic diagrams for Class 10 Science Ch 5 (Life Processes).
Usage: python3 tools/diagrams/sci05_life.py <chapter folder>
"""
import math
import sys
from figlib import Fig, BLACK, GREY, RED, BLUE, GREEN, ORANGE, PURPLE, label, box, lerp

LEAFGREEN, CELL = (40, 150, 70), (215, 240, 200)
OXY, DEOXY = (214, 48, 49), (40, 90, 200)


def ellipse_pts(c, rx, ry, a0, a1, n=40):
    return [(c[0] + rx * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + ry * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]


def guard_cells(fig, cx, pore):
    """Two kidney-shaped guard cells around a pore of half-width `pore`."""
    for side in (-1, 1):
        if side < 0:
            outer = ellipse_pts((cx, 0), 1.25, 2.1, 90, 270)
            inner = [(cx - abs(x - cx), y) for x, y in ellipse_pts((cx, 0), pore, 1.55, 270, 90)]
        else:
            outer = ellipse_pts((cx, 0), 1.25, 2.1, -90, 90)
            inner = [(cx + abs(x - cx), y) for x, y in ellipse_pts((cx, 0), pore, 1.55, 90, -90)]
        fig.polygon(outer + inner, CELL, LEAFGREEN, 2.5)
        for k in range(6):  # chloroplasts
            y = -1.35 + 0.55 * k
            x = cx + side * (pore + (1.25 - pore) * 0.55) * math.sqrt(max(0.0, 1 - (y / 2.0) ** 2))
            fig.ellipse((x, y), 0.12, 0.08, None, 1, fill=LEAFGREEN)
        fig.ellipse((cx + side * (pore + 0.35), 0.1), 0.16, 0.2, PURPLE, 1.5, fill=(200, 170, 230))


def stomata(path):
    fig = Fig(-4.2, 11.6, -3.4, 3.2)
    guard_cells(fig, 0, 0.45)
    fig.text((0, -2.8), "Open stoma", 19, BLACK, "mm", bold=True)
    guard_cells(fig, 7.0, 0.06)
    fig.text((7.0, -2.8), "Closed stoma", 19, BLACK, "mm", bold=True)
    label(fig, (0, 0.6), (-3.0, 2.7), "Stomatal pore", anchor="mm")
    label(fig, (0.8, -1.3), (2.6, -2.0), "Guard cell")
    c = 0.45 + (1.25 - 0.45) * 0.55
    label(fig, (c * math.sqrt(1 - (0.85 / 2) ** 2) + 0.0, 0.85), (2.6, 1.9), "Chloroplast")
    label(fig, (7.0 + 0.41, 0.1), (9.4, 1.9), "Nucleus")
    fig.text((3.5, 2.85), "Guard cells swell → pore opens", 15, GREY, "mm")
    fig.save(path)


def digestive_flow(path):
    fig = Fig(-6.2, 6.6, -16.2, 0.8)
    steps = [("Mouth", "teeth chew; saliva: salivary amylase, starch → sugar"),
             ("Oesophagus", "food pushed down by peristalsis"),
             ("Stomach", "HCl, pepsin (proteins), mucus"),
             ("Small intestine", "complete digestion; villi absorb food"),
             ("Large intestine", "absorbs water"),
             ("Anus", "undigested waste removed")]
    ys = [-1.2 - 2.75 * i for i in range(len(steps))]
    for (name, sub), y in zip(steps, ys):
        box(fig, (-1.6, y), 8.4, 1.75, name, sub=sub, size=18)
    for a, b in zip(ys, ys[1:]):
        fig.arrow((-1.6, a - 0.9), (-1.6, b + 0.9), BLACK, 3, size=15)
    glands = [(ys[0], "Salivary glands", "saliva"), (ys[3] + 0.9, "Liver", "bile (stored in gall bladder)"),
              (ys[3] - 0.9, "Pancreas", "pancreatic juice")]
    for y, name, sub in glands:
        box(fig, (4.6, y), 3.4, 1.5, name, fill=(255, 240, 225), outline=ORANGE, sub=sub, size=16)
        fig.arrow((2.9, y), (2.65, y if y == ys[0] else ys[3]), ORANGE, 2.5, size=13)
    fig.save(path)


def double_circulation(path):
    fig = Fig(-7.5, 7.5, -8.0, 8.0)
    # Chambers: right side of the heart is on the viewer's left.
    ch = {"RA": (-1.6, 1.3), "LA": (1.6, 1.3), "RV": (-1.6, -1.6), "LV": (1.6, -1.6)}
    names = {"RA": "Right atrium", "LA": "Left atrium", "RV": "Right ventricle", "LV": "Left ventricle"}
    for k, (x, y) in ch.items():
        col = DEOXY if k[0] == "R" else OXY
        fill = (215, 225, 250) if k[0] == "R" else (250, 215, 215)
        h = 1.6 if k[1] == "A" else 2.2
        fig.rect((x - 1.45, y - h / 2), (x + 1.45, y + h / 2), fill, col, 2.5)
        fig.text((x, y), names[k], 15, col, bold=True)
    fig.arrow((-1.6, 0.45), (-1.6, -0.45), DEOXY, 3, size=13)
    fig.arrow((1.6, 0.45), (1.6, -0.45), OXY, 3, size=13)
    box(fig, (0, 6.6), 6.0, 1.4, "Lungs", fill=(240, 240, 240), outline=GREY, sub="blood takes in O₂, gives out CO₂")
    box(fig, (0, -6.6), 6.0, 1.4, "Body organs", fill=(240, 240, 240), outline=GREY, sub="blood gives O₂, takes CO₂")
    # Pulmonary circuit (right ventricle → lungs → left atrium).
    fig.polyline([(-3.05, -1.6), (-5.2, -1.6), (-5.2, 6.6), (-3.0, 6.6)], DEOXY, 3.5)
    fig.head((-3.0, 6.6), (1, 0), DEOXY, 15)
    fig.text((-5.2, 3.2), "Pulmonary artery", 14, DEOXY, "rm", dx=-8)
    fig.polyline([(3.0, 6.6), (5.2, 6.6), (5.2, 1.3), (3.05, 1.3)], OXY, 3.5)
    fig.head((3.05, 1.3), (-1, 0), OXY, 15)
    fig.text((5.2, 4.0), "Pulmonary vein", 14, OXY, "lm", dx=8)
    # Systemic circuit (left ventricle → body → right atrium).
    fig.polyline([(3.05, -1.6), (6.4, -1.6), (6.4, -6.6), (3.0, -6.6)], OXY, 3.5)
    fig.head((3.0, -6.6), (-1, 0), OXY, 15)
    fig.text((6.4, -4.0), "Aorta", 14, OXY, "rm", dx=-8)
    fig.polyline([(-3.0, -6.6), (-6.4, -6.6), (-6.4, 1.3), (-3.05, 1.3)], DEOXY, 3.5)
    fig.head((-3.05, 1.3), (1, 0), DEOXY, 15)
    fig.text((-6.4, -4.0), "Vena cava", 14, DEOXY, "lm", dx=8)
    fig.text((0, 3.2), "Blood passes through the heart twice in one round", 14, GREY)
    fig.save(path)


def nephron(path):
    fig = Fig(-6.0, 10.6, -8.6, 4.4)
    # Bowman's capsule: a cup around the glomerulus.
    cup = ellipse_pts((0, 2.0), 1.6, 1.4, 110, 430 - 40)
    fig.polyline(cup, (120, 80, 40), 4)
    for k in range(5):  # glomerulus: tangled capillaries
        a = math.radians(72 * k)
        fig.circle((0.45 * math.cos(a), 2.0 + 0.45 * math.sin(a)), 0.45, RED, 2.5)
    # Arterioles.
    fig.polyline([(-4.0, 3.9), (-1.2, 3.9), (-0.35, 2.6)], RED, 3)
    fig.head((-0.35, 2.6), (0.85, -1.3), RED, 12)
    fig.polyline([(0.35, 2.6), (1.2, 3.9), (4.0, 3.9)], (170, 40, 40), 3)
    fig.head((4.0, 3.9), (1, 0), (170, 40, 40), 12)
    # Tubule: from the capsule, coiled, a loop down, coiled again, into the collecting duct.
    t = [(1.45, 1.2)]
    for i in range(1, 30):
        s = i / 29
        t.append((1.45 + 2.2 * s, 1.2 - 1.0 * s + 0.45 * math.sin(s * 4 * math.pi)))
    t += [(3.7, -0.5), (3.7, -6.2), (4.3, -6.7), (4.9, -6.2), (4.9, -1.6)]
    for i in range(1, 20):
        s = i / 19
        t.append((4.9 + 1.4 * s, -1.6 + 0.6 * s + 0.35 * math.sin(s * 3 * math.pi)))
    t.append((7.0, -1.0))
    fig.polyline(t, (200, 140, 30), 5)
    fig.line((7.0, 2.5), (7.0, -8.0), (150, 110, 30), 7)
    fig.arrow((7.0, -7.0), (7.0, -8.2), (150, 110, 30), 3, size=14)
    label(fig, (-1.5, 1.4), (-4.4, 0.4), "Bowman's capsule")
    label(fig, (-0.6, 2.1), (-4.4, 2.2), "Glomerulus")
    fig.text((-4.0, 3.9), "Blood in (renal artery branch)", 14, RED, "lb", dy=-6)
    fig.text((4.0, 3.9), "Blood out", 14, (170, 40, 40), "rb", dy=-6)
    label(fig, (3.7, -3.5), (1.0, -3.5), "Tubule", anchor="rm")
    label(fig, (7.0, 1.5), (7.9, 1.5), "Collecting duct")
    fig.text((7.0, -8.2), "Urine to ureter", 14, (150, 110, 30), "lt", dx=10)
    fig.text((1.0, -5.2), "Useful substances (glucose, amino acids,", 13, GREY, "rm")
    fig.text((1.0, -5.75), "salts, much water) are reabsorbed", 13, GREY, "rm")
    fig.save(path)


def kidney_shape(c, flip):
    pts = []
    for i in range(61):
        a = 2 * math.pi * i / 60
        r = 1.0 - 0.28 * max(0.0, math.cos(a)) ** 6
        x = 1.0 * r * math.cos(a)
        pts.append((c[0] + (x if flip else -x), c[1] + 1.7 * r * math.sin(a)))
    return pts


def excretory_system(path):
    fig = Fig(-7.0, 7.0, -8.6, 4.2)
    fig.line((-0.35, 3.8), (-0.35, -4.4), OXY, 8)        # aorta
    fig.line((0.35, 3.8), (0.35, -4.4), DEOXY, 8)        # vena cava
    for side in (-1, 1):
        k = (side * 3.2, 1.0)
        fig.polygon(kidney_shape(k, side > 0), (200, 120, 110), (140, 60, 50), 2.5)
        fig.line((-0.35, 1.3), (side * 2.4, 1.3), OXY, 3)     # renal artery from the aorta
        fig.line((0.35, 0.7), (side * 2.4, 0.7), DEOXY, 3)    # renal vein to the vena cava
        fig.polyline([(side * 2.5, 0.2), (side * 2.0, -2.0), (side * 1.2, -4.9)], (200, 160, 40), 4)
    fig.ellipse((0, -5.6), 1.6, 1.2, (180, 140, 40), 3, fill=(250, 235, 170))
    fig.line((0, -6.8), (0, -8.2), (180, 140, 40), 4)
    label(fig, (-3.9, 1.6), (-5.0, 3.4), "Kidney", anchor="mm")
    label(fig, (-1.4, 1.3), (-3.0, 3.6), "Renal artery", anchor="rm")
    label(fig, (1.4, 0.7), (4.6, 3.6), "Renal vein", anchor="lm")
    label(fig, (-0.35, 2.6), (-2.6, 4.1), "Aorta", anchor="rm")
    label(fig, (0.35, 2.6), (2.6, 4.1), "Vena cava", anchor="lm")
    label(fig, (-1.8, -2.8), (-4.6, -2.8), "Ureter")
    label(fig, (1.2, -5.3), (4.0, -5.3), "Urinary bladder")
    label(fig, (0, -7.6), (2.6, -7.6), "Urethra")
    fig.save(path)


FIGURES = [
 {"id": "s2.fig1", "after": "s2.reveal", "file": "fig_stomata.png",
  "title": ("Open and closed stomata", "खुला और बंद रंध्र", "ખુલ્લું અને બંધ રંધ્ર"),
  "body": ("Each stoma is a pore between two **guard cells**. When water flows into the guard cells they swell and the pore **opens**; when they lose water they shrink and the pore **closes**. Gases are exchanged and water is lost through these pores.",
           "हर रंध्र दो **द्वार कोशिकाओं** के बीच का छिद्र है। जब द्वार कोशिकाओं में पानी जाता है तो वे फूलती हैं और छिद्र **खुल** जाता है; पानी निकलने पर वे सिकुड़ती हैं और छिद्र **बंद** हो जाता है। इन्हीं छिद्रों से गैसों का आदान-प्रदान और पानी की हानि होती है।",
           "દરેક રંધ્ર બે **રક્ષક કોષો** વચ્ચેનું છિદ્ર છે. રક્ષક કોષોમાં પાણી જાય ત્યારે તે ફૂલે છે અને છિદ્ર **ખૂલે** છે; પાણી ગુમાવે ત્યારે તે સંકોચાય છે અને છિદ્ર **બંધ** થાય છે. આ છિદ્રો દ્વારા વાયુઓની આપ-લે અને પાણીનો વ્યય થાય છે.")},
 {"id": "s3.fig1", "after": "s3.table", "file": "fig_digestive_flow.png",
  "title": ("The path of food (alimentary canal)", "भोजन का मार्ग (आहार नाल)", "ખોરાકનો માર્ગ (પાચનમાર્ગ)"),
  "body": ("Food passes from the mouth to the anus through the alimentary canal. The **salivary glands, liver and pancreas** pour their juices into it. Most digestion and absorption happen in the **small intestine**, whose villi increase the surface for absorption.",
           "भोजन आहार नाल से होकर मुँह से गुदा तक जाता है। **लार ग्रंथियाँ, यकृत और अग्न्याशय** इसमें अपने रस डालते हैं। अधिकांश पाचन और अवशोषण **क्षुद्रांत्र** में होता है, जिसके दीर्घरोम अवशोषण का क्षेत्र बढ़ाते हैं।",
           "ખોરાક પાચનમાર્ગ દ્વારા મોંથી મળદ્વાર સુધી જાય છે. **લાળગ્રંથિઓ, યકૃત અને સ્વાદુપિંડ** તેમાં પોતાના રસ ઠાલવે છે. મોટા ભાગનું પાચન અને શોષણ **નાના આંતરડા**માં થાય છે, જેના રસાંકુરો શોષણ માટેની સપાટી વધારે છે.")},
 {"id": "s5.fig1", "after": "s5.thm", "file": "fig_double_circulation.png",
  "title": ("Double circulation through the heart", "हृदय से दोहरा परिसंचरण", "હૃદય દ્વારા બેવડું પરિવહન"),
  "body": ("The right side of the heart (blue) sends **deoxygenated** blood to the lungs; the left side (red) sends **oxygenated** blood to the body. Blood goes through the heart **twice** in each round, and the two kinds of blood never mix.",
           "हृदय का दायाँ भाग (नीला) **विऑक्सीजनित** रुधिर फुफ्फुसों को भेजता है; बायाँ भाग (लाल) **ऑक्सीजनित** रुधिर शरीर को भेजता है। हर चक्र में रुधिर हृदय से **दो बार** गुज़रता है, और दोनों प्रकार का रुधिर कभी नहीं मिलता।",
           "હૃદયનો જમણો ભાગ (વાદળી) **ઑક્સિજનરહિત** રુધિર ફેફસાંમાં મોકલે છે; ડાબો ભાગ (લાલ) **ઑક્સિજનયુક્ત** રુધિર શરીરમાં મોકલે છે. દરેક ચક્રમાં રુધિર હૃદયમાંથી **બે વાર** પસાર થાય છે, અને બંને પ્રકારનું રુધિર ક્યારેય ભળતું નથી.")},
 {"id": "s6.fig1", "after": "s6.thm", "file": "fig_excretory_system.png",
  "title": ("Human excretory system", "मानव उत्सर्जन तंत्र", "માનવ ઉત્સર્જનતંત્ર"),
  "body": ("A pair of **kidneys** filters the blood. Urine flows through the **ureters** to the **urinary bladder**, where it is stored, and is passed out through the **urethra**.",
           "एक जोड़ी **वृक्क** रुधिर को छानते हैं। मूत्र **मूत्रवाहिनियों** से होकर **मूत्राशय** में जाता है, जहाँ वह जमा होता है, और **मूत्रमार्ग** से बाहर निकलता है।",
           "**મૂત્રપિંડ**ની એક જોડ રુધિરનું ગાળણ કરે છે. મૂત્ર **મૂત્રવાહિનીઓ** દ્વારા **મૂત્રાશય**માં જાય છે, જ્યાં તે સંગ્રહાય છે, અને **મૂત્રમાર્ગ** દ્વારા બહાર નીકળે છે.")},
 {"id": "s6.fig2", "after": "s6.fig1", "file": "fig_nephron.png",
  "title": ("Structure of a nephron", "वृक्काणु की संरचना", "ઉત્સર્ગ એકમ (નેફ્રૉન)ની રચના"),
  "body": ("The **glomerulus** (a cluster of capillaries) sits in the cup-shaped **Bowman's capsule**, where blood is filtered. As the filtrate moves along the tubule, useful substances are **reabsorbed**; what remains becomes urine and flows into the collecting duct.",
           "**केशिका गुच्छ** (केशिकाओं का गुच्छा) प्याले जैसी **बोमन संपुट** में होता है, जहाँ रुधिर छनता है। निस्यंद जब नलिका में आगे बढ़ता है तो उपयोगी पदार्थ **पुनः अवशोषित** हो जाते हैं; जो बचता है वह मूत्र बनकर संग्राहक वाहिनी में जाता है।",
           "**કેશિકાગુચ્છ** (કેશિકાઓનો ઝૂમખો) પ્યાલા જેવી **બાઉમેનની કોથળી**માં હોય છે, જ્યાં રુધિરનું ગાળણ થાય છે. ગાળણ નલિકામાં આગળ વધે ત્યારે ઉપયોગી પદાર્થો **ફરી શોષાય** છે; બાકી રહેલું મૂત્ર બનીને સંગ્રાહક નલિકામાં જાય છે.")},
]


if __name__ == "__main__":
    from insert import insert_figures
    out = sys.argv[1].rstrip("/")
    stomata(f"{out}/fig_stomata.png")
    digestive_flow(f"{out}/fig_digestive_flow.png")
    double_circulation(f"{out}/fig_double_circulation.png")
    excretory_system(f"{out}/fig_excretory_system.png")
    nephron(f"{out}/fig_nephron.png")
    if "--draw-only" not in sys.argv:
        insert_figures(out, FIGURES)
