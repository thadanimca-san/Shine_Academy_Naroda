"""Circuit diagrams for Class 10 Science Ch 11 (Electricity), using NCERT symbols.

Every component sits on a horizontal wire: comp(fig, kind, cx, y) draws it centred
at (cx, y), and wire() joins the gaps.
Usage: python3 tools/diagrams/sci11_electricity.py <chapter folder>
"""
import sys
from figlib import Fig, BLACK, GREY, RED, BLUE, GREEN, ORANGE

W = 2.5          # wire width
HALF = {"cell": 0.18, "battery": 0.75, "key_open": 0.35, "key_closed": 0.35, "bulb": 0.4,
        "resistor": 0.7, "rheostat": 0.7, "ammeter": 0.42, "voltmeter": 0.42}


def wire(fig, p, q):
    fig.line(p, q, BLACK, W)


def zigzag(fig, cx, y, half, color=BLACK):
    n = 6
    pts = [(cx - half, y)]
    for i in range(n):
        pts.append((cx - half + (i + 0.5) * 2 * half / n, y + (0.28 if i % 2 == 0 else -0.28)))
    pts.append((cx + half, y))
    fig.polyline(pts, color, W)


def cell(fig, cx, y, plus=True):
    fig.line((cx - 0.18, y + 0.5), (cx - 0.18, y - 0.5), BLACK, 2.5)     # long plate (+)
    fig.line((cx + 0.18, y + 0.25), (cx + 0.18, y - 0.25), BLACK, 6)     # short plate (-)
    if plus:
        fig.text((cx - 0.18, y + 0.5), "+", 18, RED, "rb", dx=-2, bold=True)


def meter(fig, cx, y, letter):
    fig.circle((cx, y), 0.42, BLACK, W, fill="white")
    fig.text((cx, y), letter, 20, BLACK, bold=True)
    fig.text((cx - 0.42, y + 0.3), "+", 15, RED, "rb", bold=True)


def comp(fig, kind, cx, y):
    if kind == "cell":
        cell(fig, cx, y)
    elif kind == "battery":
        cell(fig, cx - 0.57, y)
        cell(fig, cx + 0.57, y, plus=False)
        fig.line((cx - 0.39, y), (cx + 0.39, y), BLACK, 2, dash=(5, 5))
    elif kind in ("key_open", "key_closed"):
        fig.arc((cx - 0.05, y), 0.3, 110, 250, BLACK, W)
        fig.arc((cx + 0.05, y), 0.3, -70, 70, BLACK, W)
        if kind == "key_closed":
            fig.dot((cx, y), 5)
    elif kind == "bulb":
        fig.circle((cx, y), 0.4, BLACK, W, fill="white")
        fig.line((cx - 0.28, y - 0.28), (cx + 0.28, y + 0.28), BLACK, 2)
        fig.line((cx - 0.28, y + 0.28), (cx + 0.28, y - 0.28), BLACK, 2)
    elif kind == "resistor":
        zigzag(fig, cx, y, 0.7)
    elif kind == "rheostat":
        zigzag(fig, cx, y, 0.7)
        fig.arrow((cx - 0.6, y - 0.55), (cx + 0.65, y + 0.6), BLACK, 2, size=11)
    elif kind == "ammeter":
        meter(fig, cx, y, "A")
    elif kind == "voltmeter":
        meter(fig, cx, y, "V")


def run(fig, y, x0, x1, parts):
    """A horizontal wire from x0 to x1 with components [(kind, cx), ...] in order."""
    x = x0
    for kind, cx in parts:
        h = HALF[kind]
        if kind in ("key_open", "key_closed"):
            h = 0.25
        wire(fig, (x, y), (cx - h, y))
        comp(fig, kind, cx, y)
        x = cx + h
    wire(fig, (x, y), (x1, y))


def current_arrow(fig, p, q):
    fig.head(p, (q[0] - p[0], q[1] - p[1]), BLUE, 15)


# ---------------- Figures ----------------
SYMBOLS = [("cell", "Electric cell"), ("battery", "Battery (combination of cells)"), ("key_open", "Plug key or switch (open)"),
           ("key_closed", "Plug key or switch (closed)"), ("joint", "Wire joint"), ("cross", "Wires crossing without joining"),
           ("bulb", "Electric bulb"), ("resistor", "Resistor of resistance R"), ("rheostat", "Variable resistance (rheostat)"),
           ("ammeter", "Ammeter"), ("voltmeter", "Voltmeter")]


def symbols(path):
    rows = len(SYMBOLS)
    fig = Fig(0, 13, -rows * 1.25 + 0.4, 0.9)
    for i, (kind, name) in enumerate(SYMBOLS):
        y = -i * 1.25
        if kind == "joint":
            wire(fig, (0.6, y), (3.4, y))
            wire(fig, (2.0, y), (2.0, y - 0.55))
            fig.dot((2.0, y), 6)
        elif kind == "cross":
            wire(fig, (0.6, y), (3.4, y))
            wire(fig, (2.0, y + 0.5), (2.0, y - 0.5))
        else:
            run(fig, y, 0.6, 3.4, [(kind, 2.0)])
        fig.text((4.4, y), name, 20, BLACK, "lm")
        if i:
            fig.line((0.3, y + 0.62), (12.7, y + 0.62), (230, 230, 230), 1.5)
    fig.save(path)


def ohm_circuit(path):
    fig = Fig(-1.2, 11.2, -3.6, 5.0)
    top, bot = 4.0, 0.0
    run(fig, top, 0, 10, [("battery", 3.2), ("key_closed", 7.0)])
    wire(fig, (0, top), (0, bot))
    wire(fig, (10, top), (10, bot))
    run(fig, bot, 0, 10, [("resistor", 3.2), ("ammeter", 7.0)])
    # Voltmeter in parallel with the resistor.
    a, b, yv = 1.7, 4.7, -2.0
    fig.dot((a, bot), 6)
    fig.dot((b, bot), 6)
    wire(fig, (a, bot), (a, yv))
    wire(fig, (b, bot), (b, yv))
    run(fig, yv, a, b, [("voltmeter", 3.2)])
    fig.text((3.2, bot + 0.45), "R", 20, BLACK, "mb", bold=True)
    fig.text((3.2, top + 1.0), "Battery", 16, GREY, "mb")
    fig.text((7.0, top + 0.45), "Key", 16, GREY, "mb")
    fig.text((7.0, bot - 0.55), "Ammeter (in series)", 16, GREY, "mt")
    fig.text((3.2, yv - 0.55), "Voltmeter (in parallel with R)", 16, GREY, "mt")
    # Conventional current flows from the + terminal (long plate, on the left of the battery).
    current_arrow(fig, (1.0, top), (0, top))
    current_arrow(fig, (0, 2.2), (0, 0))
    current_arrow(fig, (9.0, bot), (10, bot))
    current_arrow(fig, (10, 1.8), (10, 4))
    fig.text((-0.15, 2.2), "I", 20, BLUE, "rm", dx=-8, bold=True)
    fig.save(path)


def vi_graph(path):
    fig = Fig(-1.4, 8.2, -1.2, 6.4)
    fig.arrow((0, 0), (7.6, 0), BLACK, 2.5)
    fig.arrow((0, 0), (0, 6.0), BLACK, 2.5)
    fig.text((7.6, 0), "I (ampere)", 18, BLACK, "rt", dy=10)
    fig.text((0, 6.0), "V (volt)", 18, BLACK, "lm", dx=12)
    fig.text((0, 0), "O", 18, BLACK, "rt", dx=-6, dy=6)
    pts = [(i * 1.3, i * 0.98) for i in range(1, 6)]
    fig.line((0, 0), (7.0, 7.0 * 0.98 / 1.3), BLUE, 3.5)
    for p in pts:
        fig.dot(p, 6, RED)
    x1, x2 = pts[1], pts[3]
    fig.line(x1, (x2[0], x1[1]), ORANGE, 2, dash=(6, 5))
    fig.line((x2[0], x1[1]), x2, ORANGE, 2, dash=(6, 5))
    fig.text(((x1[0] + x2[0]) / 2, x1[1]), "ΔI", 17, ORANGE, "mt", dy=6)
    fig.text((x2[0], (x1[1] + x2[1]) / 2), "ΔV", 17, ORANGE, "lm", dx=8)
    fig.text((1.0, 5.4), "Slope = ΔV / ΔI = R", 19, BLACK, "lm", bold=True)
    fig.save(path)


def series_parallel(path):
    fig = Fig(-0.8, 23.0, -4.2, 5.4)
    # (a) Series
    top, bot = 3.0, -1.0
    fig.text((0, 4.6), "(a) Resistors in series", 19, BLACK, "lm", bold=True)
    run(fig, top, 0, 9.5, [("resistor", 1.8), ("resistor", 4.75), ("resistor", 7.7)])
    for x, n in ((1.8, "R₁"), (4.75, "R₂"), (7.7, "R₃")):
        fig.text((x, top + 0.45), n, 18, BLACK, "mb", bold=True)
    wire(fig, (0, top), (0, bot))
    wire(fig, (9.5, top), (9.5, bot))
    run(fig, bot, 0, 9.5, [("battery", 2.5), ("key_closed", 5.2), ("ammeter", 7.6)])
    fig.text((4.75, bot - 0.8), "Same current I in every resistor", 15, GREY, "mt")
    fig.text((4.75, bot - 1.5), "R = R₁ + R₂ + R₃", 18, BLUE, "mt", bold=True)
    # (b) Parallel
    ox = 12.5
    fig.text((ox, 4.6), "(b) Resistors in parallel", 19, BLACK, "lm", bold=True)
    xa, xb = ox + 1.6, ox + 8.4
    ys = (3.4, 2.1, 0.8)
    for y, n in zip(ys, ("R₁", "R₂", "R₃")):
        run(fig, y, xa, xb, [("resistor", (xa + xb) / 2)])
        fig.text(((xa + xb) / 2, y + 0.3), n, 15, BLACK, "mb", bold=True)
    wire(fig, (xa, ys[0]), (xa, bot))
    wire(fig, (xb, ys[0]), (xb, bot))
    for y in ys[1:]:
        fig.dot((xa, y), 6)
        fig.dot((xb, y), 6)
    run(fig, bot, xa, xb, [("battery", xa + 1.8), ("key_closed", xa + 4.0), ("ammeter", xa + 5.6)])
    fig.text(((xa + xb) / 2, bot - 0.8), "Same potential difference V across each", 15, GREY, "mt")
    fig.text(((xa + xb) / 2, bot - 1.5), "1/R = 1/R₁ + 1/R₂ + 1/R₃", 18, BLUE, "mt", bold=True)
    fig.save(path)


FIGURES = [
 {"id": "s2.fig1", "after": "s2.reveal", "file": "fig_circuit_symbols.png",
  "title": ("Symbols used in circuit diagrams", "परिपथ आरेख में प्रयुक्त प्रतीक", "પરિપથ આકૃતિમાં વપરાતી સંજ્ઞાઓ"),
  "body": ("These are the NCERT symbols. In a cell the **longer plate is the positive (+) terminal** and the shorter, thicker plate is negative. A dot shows wires that are joined.",
           "ये NCERT के प्रतीक हैं। सेल में **लंबी प्लेट धन (+) टर्मिनल** है और छोटी, मोटी प्लेट ऋण टर्मिनल। बिंदु दिखाता है कि तार जुड़े हुए हैं।",
           "આ NCERTની સંજ્ઞાઓ છે. કોષમાં **લાંબી પ્લેટ ધન (+) ટર્મિનલ** છે અને ટૂંકી, જાડી પ્લેટ ઋણ ટર્મિનલ. ટપકું બતાવે છે કે તાર જોડાયેલા છે.")},
 {"id": "s3.fig1", "after": "s3.table", "file": "fig_ohms_law_circuit.png",
  "title": ("Circuit to verify Ohm's law", "ओम के नियम की जाँच का परिपथ", "ઓહ્મના નિયમની ચકાસણીનો પરિપથ"),
  "body": ("The **ammeter is in series** to measure the current I through R; the **voltmeter is in parallel** with R to measure the potential difference V across it. The + terminals of both meters connect towards the + terminal of the battery. Arrows show the direction of conventional current.",
           "R से बहने वाली धारा I मापने के लिए **ऐमीटर श्रेणीक्रम में** है; R के सिरों के बीच विभवांतर V मापने के लिए **वोल्टमीटर पार्श्वक्रम में** है। दोनों मीटरों के + टर्मिनल बैटरी के + टर्मिनल की ओर जुड़ते हैं। तीर परंपरागत धारा की दिशा दिखाते हैं।",
           "R માંથી વહેતો પ્રવાહ I માપવા **એમીટર શ્રેણીમાં** છે; R ના છેડા વચ્ચેનો વિદ્યુતસ્થિતિમાનનો તફાવત V માપવા **વૉલ્ટમીટર સમાંતર** છે. બંને મીટરના + ટર્મિનલ બૅટરીના + ટર્મિનલ તરફ જોડાય છે. તીર પ્રણાલીગત પ્રવાહની દિશા બતાવે છે.")},
 {"id": "s3.fig2", "after": "s3.fig1", "file": "fig_vi_graph.png",
  "title": ("V–I graph for a resistor", "प्रतिरोधक के लिए V–I ग्राफ़", "અવરોધક માટે V–I આલેખ"),
  "body": ("The graph is a **straight line through the origin**, so V ∝ I (Ohm's law). Its slope ΔV/ΔI is the resistance R: a steeper line means a larger resistance.",
           "ग्राफ़ **मूल बिंदु से गुज़रने वाली सीधी रेखा** है, इसलिए V ∝ I (ओम का नियम)। इसका ढाल ΔV/ΔI प्रतिरोध R है: ज़्यादा ढलवाँ रेखा का अर्थ है ज़्यादा प्रतिरोध।",
           "આલેખ **ઊગમબિંદુમાંથી પસાર થતી સીધી રેખા** છે, તેથી V ∝ I (ઓહ્મનો નિયમ). તેનો ઢાળ ΔV/ΔI અવરોધ R છે: વધુ ઢોળાવવાળી રેખા એટલે વધુ અવરોધ.")},
 {"id": "s4.fig1", "after": "s4.thm", "file": "fig_series_parallel.png",
  "title": ("Resistors in series and in parallel", "श्रेणीक्रम और पार्श्वक्रम में प्रतिरोधक", "શ્રેણી અને સમાંતર જોડાણમાં અવરોધકો"),
  "body": ("(a) In **series** the same current flows through each resistor and the resistances add up. (b) In **parallel** each resistor has the same potential difference, and the reciprocals add up, so the total is less than the smallest resistance.",
           "(a) **श्रेणीक्रम** में हर प्रतिरोधक से एक ही धारा बहती है और प्रतिरोध जुड़ जाते हैं। (b) **पार्श्वक्रम** में हर प्रतिरोधक पर एक ही विभवांतर होता है, और व्युत्क्रम जुड़ते हैं, इसलिए कुल प्रतिरोध सबसे छोटे प्रतिरोध से भी कम होता है।",
           "(a) **શ્રેણી જોડાણ**માં દરેક અવરોધકમાંથી એક જ પ્રવાહ વહે છે અને અવરોધો ઉમેરાય છે. (b) **સમાંતર જોડાણ**માં દરેક અવરોધક પર એક જ વિદ્યુતસ્થિતિમાનનો તફાવત હોય છે, અને વ્યસ્તો ઉમેરાય છે, તેથી કુલ અવરોધ સૌથી નાના અવરોધ કરતાં પણ ઓછો હોય છે.")},
]


if __name__ == "__main__":
    from insert import insert_figures
    out = sys.argv[1].rstrip("/")
    symbols(f"{out}/fig_circuit_symbols.png")
    ohm_circuit(f"{out}/fig_ohms_law_circuit.png")
    vi_graph(f"{out}/fig_vi_graph.png")
    series_parallel(f"{out}/fig_series_parallel.png")
    if "--draw-only" not in sys.argv:
        insert_figures(out, FIGURES)
