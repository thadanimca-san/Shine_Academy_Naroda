"""Diagrams for Class 10 Science Ch 12 (Magnetic Effects of Electric Current).

Field lines outside a bar magnet and a solenoid are traced numerically from
pole strengths spread over the end faces, so their shape is physically right.
Usage: python3 tools/diagrams/sci12_magnetism.py <chapter folder>
"""
import math
import sys
from figlib import Fig, BLACK, GREY, RED, BLUE, GREEN, ORANGE, PURPLE

NCOL, SCOL = (214, 48, 49), (9, 105, 218)
LINE = (60, 60, 60)


def field(p, poles):
    bx = by = 0.0
    for (x, y), q in poles:
        dx, dy = p[0] - x, p[1] - y
        r3 = (dx * dx + dy * dy) ** 1.5 + 1e-9
        bx += q * dx / r3
        by += q * dy / r3
    return bx, by


def trace(start, poles, box, sinks, step=0.03, limit=4000):
    """Points along the field line from start; the flag says whether it reached a sink."""
    pts = [start]
    p = start
    for _ in range(limit):
        bx, by = field(p, poles)
        n = math.hypot(bx, by)
        p = (p[0] + step * bx / n, p[1] + step * by / n)
        pts.append(p)
        if any(s(p) for s in sinks):
            return pts, True
        if not (box[0] < p[0] < box[1] and box[2] < p[1] < box[3]):
            break
    return pts, False


def draw_line(fig, pts, color=LINE, arrows=(0.5,)):
    fig.polyline(pts, color, 2.2)
    for a in arrows:
        i = int(len(pts) * a)
        if 0 < i < len(pts) - 1:
            q, r = pts[i], pts[i + 1]
            fig.head(r, (r[0] - q[0], r[1] - q[1]), color, 13)


def draw_field_line(fig, traced):
    """A line that leaves the picture is drawn again mirrored, entering the S end,
    since the pattern is symmetric left to right."""
    pts, closed = traced
    if closed:
        draw_line(fig, pts)
    else:
        draw_line(fig, pts, arrows=(0.35,))
        draw_line(fig, [(-x, y) for x, y in reversed(pts)], arrows=(0.65,))


def spread_poles(x, half, q, n=7):
    return [((x, half * (2 * i / (n - 1) - 1)), q / n) for i in range(n)]


def bar_magnet(path):
    box = (-9.5, 9.5, -6.2, 6.2)
    fig = Fig(*box)
    half_len, half_w = 3.0, 0.7
    poles = spread_poles(half_len - 0.3, half_w * 0.8, 1.0) + spread_poles(-half_len + 0.3, half_w * 0.8, -1.0)
    def at_s(p):
        return p[0] < -half_len + 0.5 and p[0] > -half_len - 0.3 and abs(p[1]) < half_w
    for side in (1, -1):
        for k in range(8):
            ang = math.radians(12 + 160 * k / 7)
            start = (half_len - 0.3 + 0.5 * math.cos(ang), side * 0.5 * math.sin(ang))
            draw_field_line(fig, trace(start, poles, box, [at_s], step=0.02))
    fig.rect((0, -half_w), (half_len, half_w), NCOL, BLACK, 2.5)
    fig.rect((-half_len, -half_w), (0, half_w), SCOL, BLACK, 2.5)
    fig.text((half_len / 2, 0), "N", 30, (255, 255, 255), bold=True)
    fig.text((-half_len / 2, 0), "S", 30, (255, 255, 255), bold=True)
    fig.save(path)


def straight_wire(path):
    fig = Fig(-9.0, 9.0, -4.4, 4.6)
    # (a) Side view: vertical wire, current upwards, circles seen in perspective.
    x0 = -4.5
    fig.text((-8.8, 4.2), "(a) Current upwards", 18, BLACK, "lm", bold=True)
    for r in (1.0, 1.9, 2.8):
        y = -0.6
        fig.ellipse((x0, y), r, r * 0.3, LINE, 2.2)
        # Anticlockwise seen from above: the near (lower) side moves to the right.
        t = math.radians(-60)
        fig.head((x0 + r * math.cos(t), y + 0.3 * r * math.sin(t)), (-math.sin(t), 0.3 * math.cos(t)), LINE, 13)
        t = math.radians(120)
        fig.head((x0 + r * math.cos(t), y + 0.3 * r * math.sin(t)), (-math.sin(t), 0.3 * math.cos(t)), LINE, 13)
    fig.line((x0, -3.9), (x0, 3.6), ORANGE, 6)
    fig.head((x0, 3.9), (0, 1), ORANGE, 20)
    fig.text((x0, 3.9), "I", 22, ORANGE, "lm", dx=16, bold=True)
    # (b) Top view: current coming out of the page.
    c = (4.8, -0.2)
    fig.text((0.8, 4.2), "(b) Seen from above (I out of the page)", 18, BLACK, "lm", bold=True)
    for r in (1.0, 1.9, 2.8, 3.7):
        fig.circle(c, r, LINE, 2.2)
        for ang in (0, 180):
            a = math.radians(ang)
            p = (c[0] + r * math.cos(a), c[1] + r * math.sin(a))
            fig.head(p, (-math.sin(a), math.cos(a)), LINE, 13)
    fig.circle(c, 0.35, ORANGE, 3, fill="white")
    fig.dot(c, 5, ORANGE)
    fig.save(path)


def solenoid(path):
    box = (-9.5, 9.5, -5.6, 5.6)
    fig = Fig(*box)
    L, R = 3.6, 1.0
    poles = spread_poles(L, R * 0.9, 1.0, 9) + spread_poles(-L, R * 0.9, -1.0, 9)
    def at_s(p):
        return abs(p[0] + L) < 0.05 and abs(p[1]) < R
    for side in (1, -1):
        for k in range(6):
            y0 = side * (0.2 + 0.14 * k)
            draw_field_line(fig, trace((L + 0.05, y0), poles, box, [at_s], step=0.02))
    # Inside: uniform field from S to N.
    for y in (-0.6, -0.2, 0.2, 0.6):
        fig.line((-L, y), (L, y), LINE, 2.2)
        fig.head((0.3, y), (1, 0), LINE, 13)
    # The coil: turns drawn as tall thin ellipses.
    n = 12
    for i in range(n + 1):
        x = -L + 2 * L * i / n
        fig.ellipse((x, 0), 0.16, R, ORANGE, 3)
    fig.line((-L, -R), (-L - 0.8, -R - 1.3), ORANGE, 3)
    fig.line((L, -R), (L + 0.8, -R - 1.3), ORANGE, 3)
    fig.head((-L - 0.5, -R - 0.8), (0.8, 1.3), ORANGE, 15)
    fig.text((-L - 0.85, -R - 1.4), "Current in", 15, ORANGE, "rt", halo=True)
    fig.head((L + 0.8, -R - 1.3), (0.8, -1.3), ORANGE, 15)
    fig.text((L + 0.85, -R - 1.4), "Current out", 15, ORANGE, "lt", halo=True)
    fig.text((L + 0.6, 0), "N", 26, NCOL, "lm", dx=10, bold=True, halo=True)
    fig.text((-L - 0.6, 0), "S", 26, SCOL, "rm", dx=-10, bold=True, halo=True)
    fig.save(path)


def fleming(path):
    fig = Fig(-5.2, 6.8, -3.8, 4.8)
    o = (0.0, 0.0)
    ux, uy, uz = (1.0, 0.0), (0.0, 1.0), (-0.62, -0.5)   # oblique projection
    def p(a, b, c):
        return (o[0] + a * ux[0] + b * uy[0] + c * uz[0], o[1] + a * ux[1] + b * uy[1] + c * uz[1])
    fig.arrow(o, p(4.2, 0, 0), BLUE, 5, size=20)
    fig.arrow(o, p(0, 3.8, 0), RED, 5, size=20)
    fig.arrow(o, p(0, 0, 4.6), GREEN, 5, size=20)
    s = 0.45  # right-angle marks
    for a, b in (((s, 0, 0), (0, s, 0)), ((s, 0, 0), (0, 0, s)), ((0, s, 0), (0, 0, s))):
        fig.polyline([p(*a), p(a[0] + b[0], a[1] + b[1], a[2] + b[2]), p(*b)], GREY, 1.8)
    fig.text(p(4.2, 0, 0), "Forefinger: Field (B)", 18, BLUE, "lm", dx=-150, dy=-26, bold=True)
    fig.text(p(0, 3.8, 0), "Thumb: Force / motion (F)", 18, RED, "lm", dx=16, bold=True)
    fig.text(p(0, 0, 4.6), "Middle finger: Current (I)", 18, GREEN, "lt", dx=-60, dy=14, bold=True)
    fig.text((6.6, -3.2), "Left hand: all three at right angles", 16, GREY, "rm")
    fig.save(path)


FIGURES = [
 {"id": "s2.fig1", "after": "s2.reveal", "file": "fig_bar_magnet_field.png",
  "title": ("Field lines around a bar magnet", "छड़ चुंबक के चारों ओर क्षेत्र रेखाएँ", "ગજિયા ચુંબકની આસપાસ ક્ષેત્રરેખાઓ"),
  "body": ("Outside the magnet the lines go from the **north pole to the south pole**; inside they go from S to N, so each line is a closed loop. Lines are **crowded near the poles**, where the field is strongest, and they never cross.",
           "चुंबक के बाहर रेखाएँ **उत्तर ध्रुव से दक्षिण ध्रुव** की ओर जाती हैं; अंदर वे S से N की ओर जाती हैं, इसलिए हर रेखा एक बंद वक्र है। **ध्रुवों के पास रेखाएँ घनी** होती हैं, जहाँ क्षेत्र सबसे प्रबल होता है, और वे कभी एक-दूसरे को नहीं काटतीं।",
           "ચુંબકની બહાર રેખાઓ **ઉત્તર ધ્રુવથી દક્ષિણ ધ્રુવ** તરફ જાય છે; અંદર તે S થી N તરફ જાય છે, તેથી દરેક રેખા બંધ વક્ર છે. **ધ્રુવો પાસે રેખાઓ ગીચ** હોય છે, જ્યાં ક્ષેત્ર સૌથી પ્રબળ હોય છે, અને તે ક્યારેય એકબીજીને છેદતી નથી.")},
 {"id": "s3.fig1", "after": "s3.thm", "file": "fig_straight_wire_field.png",
  "title": ("Field around a straight current-carrying wire", "धारावाही सीधे तार के चारों ओर क्षेत्र", "વિદ્યુતપ્રવાહધારિત સીધા તારની આસપાસ ક્ષેત્ર"),
  "body": ("The field lines are **concentric circles** centred on the wire. For a current flowing upwards (out of the page), they run **anticlockwise** seen from above, as the right-hand thumb rule says. The circles get farther apart away from the wire because the field becomes weaker.",
           "क्षेत्र रेखाएँ तार को केंद्र मानकर **संकेंद्री वृत्त** होती हैं। ऊपर की ओर (पृष्ठ से बाहर) बहती धारा के लिए ऊपर से देखने पर वे **वामावर्त** चलती हैं, जैसा दक्षिण-हस्त अंगुष्ठ नियम बताता है। तार से दूर जाने पर क्षेत्र कमज़ोर होता है, इसलिए वृत्त दूर-दूर होते जाते हैं।",
           "ક્ષેત્રરેખાઓ તારને કેન્દ્ર રાખીને **સમકેન્દ્રી વર્તુળો** હોય છે. ઉપર તરફ (પાનાની બહાર) વહેતા પ્રવાહ માટે ઉપરથી જોતાં તે **વિષમઘડી દિશામાં** ચાલે છે, જેમ જમણા હાથના અંગૂઠાનો નિયમ કહે છે. તારથી દૂર જતાં ક્ષેત્ર નબળું પડે છે, તેથી વર્તુળો દૂર દૂર થતાં જાય છે.")},
 {"id": "s3.fig2", "after": "s3.fig1", "file": "fig_solenoid_field.png",
  "title": ("Field of a current-carrying solenoid", "धारावाही परिनालिका का क्षेत्र", "વિદ્યુતપ્રવાહધારિત સોલેનોઇડનું ક્ષેત્ર"),
  "body": ("Outside, the pattern is like that of a **bar magnet**, with one end acting as N and the other as S. **Inside, the lines are parallel straight lines**: the field is uniform. A soft iron core inside makes it an electromagnet.",
           "बाहर का पैटर्न **छड़ चुंबक** जैसा होता है: एक सिरा N और दूसरा S की तरह काम करता है। **अंदर रेखाएँ समांतर सीधी रेखाएँ** होती हैं: क्षेत्र एकसमान होता है। अंदर नर्म लोहे का क्रोड रखने पर यह विद्युत चुंबक बन जाती है।",
           "બહારની ભાત **ગજિયા ચુંબક** જેવી હોય છે: એક છેડો N અને બીજો S તરીકે વર્તે છે. **અંદર રેખાઓ સમાંતર સીધી રેખાઓ** હોય છે: ક્ષેત્ર સમાન હોય છે. અંદર નરમ લોખંડનો ગર્ભ મૂકતાં તે વિદ્યુતચુંબક બને છે.")},
 {"id": "s4.fig1", "after": "s4.thm", "file": "fig_fleming_left_hand.png",
  "title": ("Fleming's left-hand rule", "फ्लेमिंग का वामहस्त नियम", "ફ્લેમિંગનો ડાબા હાથનો નિયમ"),
  "body": ("Stretch the thumb, forefinger and middle finger of the **left hand** at right angles to each other. If the forefinger points along the **field** and the middle finger along the **current**, the thumb gives the direction of the **force** on the conductor.",
           "**बाएँ हाथ** का अंगूठा, तर्जनी और मध्यमा एक-दूसरे के लंबवत फैलाइए। यदि तर्जनी **क्षेत्र** की दिशा में और मध्यमा **धारा** की दिशा में हो, तो अंगूठा चालक पर लगने वाले **बल** की दिशा बताता है।",
           "**ડાબા હાથ**નો અંગૂઠો, પહેલી આંગળી અને મધ્યમા એકબીજીને લંબ રહે તેમ ફેલાવો. જો પહેલી આંગળી **ક્ષેત્ર**ની દિશામાં અને મધ્યમા **પ્રવાહ**ની દિશામાં હોય, તો અંગૂઠો વાહક પર લાગતા **બળ**ની દિશા બતાવે છે.")},
]


if __name__ == "__main__":
    from insert import insert_figures
    out = sys.argv[1].rstrip("/")
    bar_magnet(f"{out}/fig_bar_magnet_field.png")
    straight_wire(f"{out}/fig_straight_wire_field.png")
    solenoid(f"{out}/fig_solenoid_field.png")
    fleming(f"{out}/fig_fleming_left_hand.png")
    if "--draw-only" not in sys.argv:
        insert_figures(out, FIGURES)
