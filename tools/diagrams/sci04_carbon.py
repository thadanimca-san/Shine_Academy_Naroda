"""Diagrams for Class 10 Science Ch 4 (Carbon and its Compounds): electron-dot
structures, structural formulae, isomers, rings and the micelle.
Usage: python3 tools/diagrams/sci04_carbon.py <chapter folder>
"""
import math
import sys
from figlib import Fig, BLACK, GREY, RED, BLUE, GREEN, ORANGE, PURPLE, lerp

CARBON, HYDROGEN = (30, 30, 30), (9, 105, 218)
COLOURS = {"C": CARBON, "H": HYDROGEN, "O": (214, 48, 49), "N": (142, 68, 173)}
GAP = 0.32  # bonds stop this far from the atom centre


def atom(fig, p, el, size=26):
    fig.text(p, el, size, COLOURS.get(el, BLACK), bold=True)


def bond(fig, p, q, order=1):
    d = math.dist(p, q)
    ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    a = (p[0] + ux * GAP, p[1] + uy * GAP)
    b = (q[0] - ux * GAP, q[1] - uy * GAP)
    offs = {1: [0], 2: [-0.07, 0.07], 3: [-0.11, 0, 0.11]}[order]
    for o in offs:
        fig.line((a[0] - uy * o, a[1] + ux * o), (b[0] - uy * o, b[1] + ux * o), BLACK, 2.5)


def molecule(fig, atoms, bonds):
    """atoms: {name: (element, (x, y))}; bonds: [(a, b, order)]."""
    for a, b, order in bonds:
        bond(fig, atoms[a][1], atoms[b][1], order)
    for el, p in atoms.values():
        atom(fig, p, el)


def add_h(atoms, bonds, carbon, directions, length=1.15):
    cx, cy = atoms[carbon][1]
    for k, ang in enumerate(directions):
        name = f"{carbon}h{k}"
        atoms[name] = ("H", (cx + length * math.cos(math.radians(ang)), cy + length * math.sin(math.radians(ang))))
        bonds.append((carbon, name, 1))


def chain(n, ox, oy, step=1.5):
    atoms = {f"c{i}": ("C", (ox + i * step, oy)) for i in range(n)}
    bonds = [(f"c{i}", f"c{i + 1}", 1) for i in range(n - 1)]
    for i in range(n):
        dirs = [90, 270] + ([180] if i == 0 else []) + ([0] if i == n - 1 else [])
        add_h(atoms, bonds, f"c{i}", dirs)
    return atoms, bonds


def caption(fig, p, title, formula):
    fig.text(p, title, 19, BLACK, "mt", bold=True)
    fig.text((p[0], p[1] - 0.5), formula, 17, GREY, "mt")


# ---------------- Figures ----------------
def shared_pair(fig, p, q, k, n_pairs, own_p="dot", own_q="cross"):
    """The k-th of n_pairs shared electron pairs between atoms p and q."""
    m = lerp(p, q, 0.5)
    d = math.dist(p, q)
    ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    off = (k - (n_pairs - 1) / 2) * 0.32
    c = (m[0] - uy * off, m[1] + ux * off)
    electron(fig, (c[0] - ux * 0.12, c[1] - uy * 0.12), own_p)
    electron(fig, (c[0] + ux * 0.12, c[1] + uy * 0.12), own_q)


def electron(fig, p, kind):
    if kind == "dot":
        fig.dot(p, 4.5, BLACK)
    else:
        fig.text(p, "×", 17, RED, bold=True)


def lone_pair(fig, p, ang, kind):
    a = math.radians(ang)
    c = (p[0] + 0.5 * math.cos(a), p[1] + 0.5 * math.sin(a))
    for s in (-0.12, 0.12):
        electron(fig, (c[0] - math.sin(a) * s, c[1] + math.cos(a) * s), kind)


def electron_dot(path):
    fig = Fig(-2.6, 14.4, -3.6, 2.8)
    # Methane: C (dots) shares one pair with each H (crosses).
    c = (0, 0)
    atom(fig, c, "C")
    for ang in (0, 90, 180, 270):
        h = (1.6 * math.cos(math.radians(ang)), 1.6 * math.sin(math.radians(ang)))
        atom(fig, h, "H")
        shared_pair(fig, c, h, 0, 1)
    caption(fig, (0, -2.3), "Methane", "CH₄: four single bonds")
    # Oxygen: two shared pairs (double bond), two lone pairs on each atom.
    o1, o2 = (4.9, 0), (6.5, 0)
    atom(fig, o1, "O")
    atom(fig, o2, "O")
    for k in range(2):
        shared_pair(fig, o1, o2, k, 2)
    for ang in (135, 225):   # two lone pairs on each O (6 valence electrons)
        lone_pair(fig, o1, ang, "dot")
        lone_pair(fig, o2, 180 - ang, "cross")
    caption(fig, (5.7, -2.3), "Oxygen", "O₂: double bond")
    # Nitrogen: three shared pairs (triple bond), one lone pair on each atom.
    n1, n2 = (10.4, 0), (12.0, 0)
    atom(fig, n1, "N")
    atom(fig, n2, "N")
    for k in range(3):
        shared_pair(fig, n1, n2, k, 3)
    lone_pair(fig, n1, 180, "dot")
    lone_pair(fig, n2, 0, "cross")
    caption(fig, (11.2, -2.3), "Nitrogen", "N₂: triple bond")
    fig.text((14.2, 2.4), "•  ×  electrons of the two atoms", 15, GREY, "rm")
    fig.save(path)


def bonds_c2(path):
    fig = Fig(-1.6, 16.6, -3.4, 2.0)
    atoms, bonds = chain(2, 0, 0)
    molecule(fig, atoms, bonds)
    caption(fig, (0.75, -1.7), "Ethane", "C₂H₆: single bond")
    ox = 6.6
    atoms = {"c0": ("C", (ox, 0)), "c1": ("C", (ox + 1.5, 0))}
    bonds = [("c0", "c1", 2)]
    add_h(atoms, bonds, "c0", [135, 225])
    add_h(atoms, bonds, "c1", [45, 315])
    molecule(fig, atoms, bonds)
    caption(fig, (ox + 0.75, -1.7), "Ethene", "C₂H₄: double bond")
    ox = 12.5
    atoms = {"c0": ("C", (ox, 0)), "c1": ("C", (ox + 1.5, 0))}
    bonds = [("c0", "c1", 3)]
    add_h(atoms, bonds, "c0", [180])
    add_h(atoms, bonds, "c1", [0])
    molecule(fig, atoms, bonds)
    caption(fig, (ox + 0.75, -1.7), "Ethyne", "C₂H₂: triple bond")
    fig.save(path)


def butane_isomers(path):
    fig = Fig(-1.6, 15.2, -5.0, 2.2)
    atoms, bonds = chain(4, 0, 0)
    molecule(fig, atoms, bonds)
    caption(fig, (2.25, -1.9), "Butane (straight chain)", "C₄H₁₀")
    ox = 9.6
    atoms = {"c0": ("C", (ox, 0)), "c1": ("C", (ox + 1.5, 0)), "c2": ("C", (ox + 3.0, 0)), "c3": ("C", (ox + 1.5, -1.5))}
    bonds = [("c0", "c1", 1), ("c1", "c2", 1), ("c1", "c3", 1)]
    add_h(atoms, bonds, "c0", [90, 180, 270])
    add_h(atoms, bonds, "c1", [90])
    add_h(atoms, bonds, "c2", [90, 0, 270])
    add_h(atoms, bonds, "c3", [270, 205, 335])
    molecule(fig, atoms, bonds)
    caption(fig, (ox + 1.5, -3.6), "Isobutane (branched chain)", "C₄H₁₀")
    fig.save(path)


def rings(path):
    fig = Fig(-3.4, 11.4, -4.6, 3.2)
    r = 1.45
    def ring(ox, h_dirs_per_c, double):
        atoms, bonds = {}, []
        for i in range(6):
            a = math.radians(90 + 60 * i)
            atoms[f"c{i}"] = ("C", (ox + r * math.cos(a), r * math.sin(a)))
        for i in range(6):
            bonds.append((f"c{i}", f"c{(i + 1) % 6}", 2 if double and i % 2 == 0 else 1))
        for i in range(6):
            base = 90 + 60 * i
            add_h(atoms, bonds, f"c{i}", [base + d for d in h_dirs_per_c], length=1.0)
        molecule(fig, atoms, bonds)
    ring(0, (-28, 28), False)
    caption(fig, (0, -3.0), "Cyclohexane", "C₆H₁₂: saturated ring")
    ring(8.0, (0,), True)
    caption(fig, (8.0, -3.0), "Benzene", "C₆H₆: alternate single and double bonds")
    fig.save(path)


def micelle(path):
    fig = Fig(-6.4, 9.6, -4.4, 4.4)
    # One soap molecule, labelled.
    tail = [(-6.0 + 0.45 * i, 2.9 + (0.18 if i % 2 else -0.18)) for i in range(9)]
    fig.polyline(tail, BLACK, 3)
    head = (tail[-1][0] + 0.45, 2.9)
    fig.circle(head, 0.3, RED, 3, fill=(255, 220, 220))
    fig.text((-4.2, 3.6), "Hydrocarbon tail (hydrophobic)", 14, BLACK, "mb")
    fig.text((head[0], 3.4), "Ionic head (hydrophilic)", 14, RED, "lb", dx=-20)
    fig.text((-4.2, 2.2), "A soap molecule", 15, GREY, "mt")
    # The micelle: tails inside the oil drop, heads outside in water.
    c, r_oil = (4.8, -0.6), 1.25
    fig.circle(c, r_oil, (180, 140, 20), 2.5, fill=(250, 225, 140))
    fig.text(c, "Oily dirt", 16, (120, 85, 0), bold=True)
    n = 16
    for k in range(n):
        a = 2 * math.pi * k / n
        ux, uy = math.cos(a), math.sin(a)
        pts = []
        for i in range(8):
            rr = 0.55 + 0.3 * i
            w = 0.12 if i % 2 else -0.12
            pts.append((c[0] + rr * ux - uy * w, c[1] + rr * uy + ux * w))
        fig.polyline(pts, BLACK, 2.2)
        h = (c[0] + 2.85 * ux, c[1] + 2.85 * uy)
        fig.circle(h, 0.25, RED, 2.5, fill=(255, 220, 220))
    fig.text((c[0] - 4.0, -3.6), "Water", 17, BLUE, "lm", bold=True)
    fig.text((c[0], c[1] - 3.3), "Micelle", 18, BLACK, "mt", bold=True)
    fig.save(path)


FIGURES = [
 {"id": "s2.fig1", "after": "s2.table", "file": "fig_electron_dot.png",
  "title": ("Electron-dot structures", "इलेक्ट्रॉन बिंदु संरचनाएँ", "ઇલેક્ટ્રૉન-બિંદુ રચનાઓ"),
  "body": ("Each shared pair (one • and one ×, from the two atoms) is one covalent bond. Methane has four single bonds; oxygen shares **two pairs** (double bond) and nitrogen **three pairs** (triple bond). The pairs not shared are lone pairs.",
           "हर साझा युग्म (दोनों परमाणुओं का एक • और एक ×) एक सहसंयोजक आबंध है। मेथेन में चार एकल आबंध हैं; ऑक्सीजन **दो युग्म** (द्वि-आबंध) और नाइट्रोजन **तीन युग्म** (त्रि-आबंध) साझा करती है। जो युग्म साझा नहीं होते, वे एकाकी युग्म हैं।",
           "દરેક ભાગીદારીવાળું યુગ્મ (બંને પરમાણુઓનો એક • અને એક ×) એક સહસંયોજક બંધ છે. મિથેનમાં ચાર એકલ બંધ છે; ઑક્સિજન **બે યુગ્મ** (દ્વિબંધ) અને નાઇટ્રોજન **ત્રણ યુગ્મ** (ત્રિબંધ)ની ભાગીદારી કરે છે. જે યુગ્મની ભાગીદારી નથી થતી તે અબંધકારક યુગ્મ છે.")},
 {"id": "s3.fig1", "after": "s3.thm", "file": "fig_single_double_triple.png",
  "title": ("Single, double and triple bonds", "एकल, द्वि और त्रि-आबंध", "એકલ, દ્વિ અને ત્રિબંધ"),
  "body": ("Ethane is **saturated** (only single bonds). Ethene (double bond) and ethyne (triple bond) are **unsaturated** and more reactive. In every case each carbon forms **four bonds**.",
           "एथेन **संतृप्त** है (केवल एकल आबंध)। एथीन (द्वि-आबंध) और एथाइन (त्रि-आबंध) **असंतृप्त** हैं और अधिक अभिक्रियाशील हैं। हर स्थिति में प्रत्येक कार्बन **चार आबंध** बनाता है।",
           "ઇથેન **સંતૃપ્ત** છે (ફક્ત એકલ બંધ). ઇથીન (દ્વિબંધ) અને ઇથાઇન (ત્રિબંધ) **અસંતૃપ્ત** છે અને વધુ પ્રતિક્રિયાશીલ છે. દરેક કિસ્સામાં દરેક કાર્બન **ચાર બંધ** બનાવે છે.")},
 {"id": "s3.fig2", "after": "s3.fig1", "file": "fig_butane_isomers.png",
  "title": ("Structural isomers of butane", "ब्यूटेन के संरचनात्मक समावयवी", "બ્યુટેનના બંધારણીય સમઘટકો"),
  "body": ("Both have the formula **C₄H₁₀** but different arrangements of carbon atoms: a straight chain and a branched chain. Compounds like these are **structural isomers**.",
           "दोनों का सूत्र **C₄H₁₀** है, पर कार्बन परमाणुओं की व्यवस्था अलग है: एक सीधी श्रृंखला और एक शाखित श्रृंखला। ऐसे यौगिक **संरचनात्मक समावयवी** कहलाते हैं।",
           "બંનેનું સૂત્ર **C₄H₁₀** છે, પણ કાર્બન પરમાણુઓની ગોઠવણી જુદી છે: એક સીધી શૃંખલા અને એક શાખાવાળી શૃંખલા. આવાં સંયોજનો **બંધારણીય સમઘટકો** કહેવાય છે.")},
 {"id": "s3.fig3", "after": "s3.fig2", "file": "fig_cyclohexane_benzene.png",
  "title": ("Carbon rings: cyclohexane and benzene", "कार्बन वलय: साइक्लोहेक्सेन और बेन्ज़ीन", "કાર્બન વલય: સાયક્લોહેક્ઝેન અને બેન્ઝિન"),
  "body": ("Carbon atoms can also join in a **ring**. In cyclohexane each carbon has two hydrogens and all bonds are single; benzene has **alternate single and double bonds** and one hydrogen on each carbon.",
           "कार्बन परमाणु **वलय** में भी जुड़ सकते हैं। साइक्लोहेक्सेन में हर कार्बन पर दो हाइड्रोजन हैं और सभी आबंध एकल हैं; बेन्ज़ीन में **एकांतर एकल और द्वि-आबंध** हैं और हर कार्बन पर एक हाइड्रोजन है।",
           "કાર્બન પરમાણુઓ **વલય**માં પણ જોડાઈ શકે છે. સાયક્લોહેક્ઝેનમાં દરેક કાર્બન પર બે હાઇડ્રોજન છે અને બધા બંધ એકલ છે; બેન્ઝિનમાં **એકાંતરે એકલ અને દ્વિબંધ** છે અને દરેક કાર્બન પર એક હાઇડ્રોજન છે.")},
 {"id": "s6.fig1", "after": "s6.thm", "file": "fig_micelle.png",
  "title": ("How soap forms a micelle", "साबुन मिसेल कैसे बनाता है", "સાબુ મિસેલ કેવી રીતે બનાવે છે"),
  "body": ("A soap molecule has a long **hydrocarbon tail** that dissolves in oil and an **ionic head** that dissolves in water. In water, the tails point into the oily dirt and the heads face the water, forming a **micelle** that is rinsed away.",
           "साबुन के अणु की एक लंबी **हाइड्रोकार्बन पूँछ** होती है जो तेल में घुलती है, और एक **आयनिक सिरा** जो पानी में घुलता है। पानी में पूँछें तैलीय मैल की ओर और सिरे पानी की ओर रहते हैं; इस तरह **मिसेल** बनता है जो धुलकर निकल जाता है।",
           "સાબુના અણુની એક લાંબી **હાઇડ્રોકાર્બન પૂંછ** હોય છે જે તેલમાં ઓગળે છે, અને એક **આયનીય છેડો** જે પાણીમાં ઓગળે છે. પાણીમાં પૂંછ તૈલી મેલ તરફ અને છેડા પાણી તરફ રહે છે; આમ **મિસેલ** બને છે જે ધોવાઈ જાય છે.")},
]


if __name__ == "__main__":
    from insert import insert_figures
    out = sys.argv[1].rstrip("/")
    electron_dot(f"{out}/fig_electron_dot.png")
    bonds_c2(f"{out}/fig_single_double_triple.png")
    butane_isomers(f"{out}/fig_butane_isomers.png")
    rings(f"{out}/fig_cyclohexane_benzene.png")
    micelle(f"{out}/fig_micelle.png")
    if "--draw-only" not in sys.argv:
        insert_figures(out, FIGURES)
