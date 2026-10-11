"""Diagrams for Class 10 Science Ch 2 (pH scale) and Ch 3 (electrolytic refining).
Usage: python3 tools/diagrams/sci02_03_chemistry.py <ch02 folder> <ch03 folder>
"""
import sys
from figlib import Fig, BLACK, GREY, RED, BLUE, GREEN, ORANGE, lerp

# Universal indicator colours for pH 0..14.
PH_COLOURS = [(200, 20, 30), (230, 40, 30), (240, 90, 30), (245, 140, 30), (250, 190, 30), (240, 225, 40), (190, 220, 50),
              (60, 170, 60), (40, 150, 110), (30, 130, 160), (40, 100, 190), (50, 70, 180), (80, 50, 160), (100, 40, 140), (90, 30, 110)]
EXAMPLES = [(1.2, "Gastric juice"), (2.2, "Lemon juice"), (7.0, "Pure water"), (7.4, "Blood"),
            (10.0, "Milk of magnesia"), (14.0, "Sodium hydroxide solution")]


def ph_scale(path):
    fig = Fig(-1.0, 16.0, -3.6, 4.6)
    for i, rgb in enumerate(PH_COLOURS):
        fig.rect((i + 0.5, 0), (i + 1.5, 1.0), rgb, None)
    fig.rect((0.5, 0), (15.5, 1.0), None, BLACK, 2)
    for i in range(15):
        x = i + 1.0
        fig.text((x, 0.5), str(i), 18, (255, 255, 255) if i not in (5, 6) else BLACK, bold=True)
    # Examples above the strip, alternating heights so labels do not collide.
    for k, (ph, name) in enumerate(EXAMPLES):
        x = ph + 1.0
        top = 2.0 if k % 2 == 0 else 3.3
        fig.line((x, 1.05), (x, top - 0.15), GREY, 1.8)
        fig.dot((x, 1.05), 4, BLACK)
        label = f"{name} ({ph:g})" if ph in (7.0, 14.0) else f"{name} (~{ph:g})"
        fig.text((x, top), label, 15, BLACK, "rb" if x > 13 else "mb", dx=10 if x > 13 else 0)
    fig.text((4.0, -0.35), "Acidic", 19, RED, "mt", bold=True)
    fig.text((8.0, -0.35), "Neutral", 19, GREEN, "mt", bold=True)
    fig.text((12.0, -0.35), "Basic (alkaline)", 19, BLUE, "mt", bold=True)
    fig.arrow((7.4, -1.6), (0.8, -1.6), RED, 3)
    fig.text((4.1, -1.75), "Increasing H⁺ ion concentration", 15, RED, "mt")
    fig.arrow((8.6, -1.6), (15.2, -1.6), BLUE, 3)
    fig.text((11.9, -1.75), "Increasing OH⁻ ion concentration", 15, BLUE, "mt")
    fig.save(path)


def electrolytic_refining(path):
    fig = Fig(-7.6, 7.6, -5.4, 4.6)
    # Tank and solution.
    fig.rect((-4.5, -4.6), (4.5, 0.6), (225, 240, 255), BLACK, 3)
    fig.rect((-4.5, -4.6), (4.5, -0.3), (150, 200, 240), None)
    fig.rect((-4.5, -4.6), (4.5, 0.6), None, BLACK, 3)
    fig.text((0, -2.3), "Acidified copper", 15, (20, 60, 120), "mb")
    fig.text((0, -2.3), "sulphate solution", 15, (20, 60, 120), "mt", dy=4)
    # Anode (impure copper, thick) and cathode (pure copper, thin).
    fig.rect((-3.2, -3.6), (-2.2, 1.6), (150, 100, 60), BLACK, 2)
    fig.rect((2.4, -3.6), (2.8, 1.6), (205, 120, 60), BLACK, 2)
    # Anode mud below the anode.
    fig.polygon([(-3.8, -4.6), (-1.6, -4.6), (-2.2, -4.15), (-3.0, -4.05)], (110, 90, 70), None)
    fig.text((-1.4, -4.3), "Anode mud", 15, BLACK, "lm", halo=True)
    # Battery and wires.
    fig.line((-2.7, 1.6), (-2.7, 3.2), BLACK, 2.5)
    fig.line((-2.7, 3.2), (-0.35, 3.2), BLACK, 2.5)
    fig.line((-0.3, 3.7), (-0.3, 2.7), BLACK, 2.5)   # long plate (+)
    fig.line((0.3, 3.45), (0.3, 2.95), BLACK, 6)     # short plate (-)
    fig.text((-0.3, 3.75), "+", 20, RED, "rb", dx=-4, bold=True)
    fig.text((0.3, 3.75), "−", 22, BLACK, "lb", dx=4, bold=True)
    fig.line((0.35, 3.2), (2.6, 3.2), BLACK, 2.5)
    fig.line((2.6, 3.2), (2.6, 1.6), BLACK, 2.5)
    fig.text((-3.3, 2.3), "Anode (+)", 16, BLACK, "rm", dx=-6, bold=True)
    fig.text((-3.3, 1.7), "impure copper", 14, GREY, "rm", dx=-6)
    fig.text((2.9, 2.3), "Cathode (−)", 16, BLACK, "lm", dx=6, bold=True)
    fig.text((2.9, 1.7), "pure copper", 14, GREY, "lm", dx=6)
    # Cu2+ ions move from anode to cathode.
    for y in (-1.0, -3.0):
        fig.arrow((-1.6, y), (1.9, y), ORANGE, 2.5)
    fig.text((0.15, -1.0), "Cu²⁺", 16, ORANGE, "mb", dy=-6, bold=True)
    fig.save(path)


FIGURES_CH2 = [
 {"id": "s5.fig1", "after": "s5.table", "file": "fig_ph_scale.png",
  "title": ("The pH scale with everyday examples", "दैनिक उदाहरणों के साथ pH स्केल", "રોજિંદાં ઉદાહરણો સાથે pH માપક્રમ"),
  "body": ("pH runs from **0 (very acidic)** to **14 (very basic)**; **7 is neutral**. Lower pH means more H⁺ ions; higher pH means more OH⁻ ions. The colours are those of a universal indicator.",
           "pH **0 (अत्यधिक अम्लीय)** से **14 (अत्यधिक क्षारकीय)** तक होता है; **7 उदासीन** है। कम pH का अर्थ है अधिक H⁺ आयन; अधिक pH का अर्थ है अधिक OH⁻ आयन। रंग सार्वत्रिक सूचक के हैं।",
           "pH **0 (ખૂબ ઍસિડિક)** થી **14 (ખૂબ બેઝિક)** સુધી હોય છે; **7 તટસ્થ** છે. ઓછો pH એટલે વધુ H⁺ આયન; વધુ pH એટલે વધુ OH⁻ આયન. રંગો સાર્વત્રિક સૂચકના છે.")},
]
FIGURES_CH3 = [
 {"id": "s5.fig1", "after": "s5.extract", "file": "fig_electrolytic_refining.png",
  "title": ("Electrolytic refining of copper", "ताँबे का विद्युत अपघटनी परिष्करण", "તાંબાનું વિદ્યુતવિભાજનીય શુદ્ધીકરણ"),
  "body": ("The **impure copper is the anode** and a thin strip of **pure copper is the cathode**; the electrolyte is acidified copper sulphate solution. Copper dissolves from the anode and an equal amount of pure copper deposits on the cathode. Insoluble impurities settle below the anode as **anode mud**.",
           "**अशुद्ध ताँबा ऐनोड** है और **शुद्ध ताँबे की पतली पट्टी कैथोड**; विद्युत अपघट्य अम्लीय कॉपर सल्फ़ेट विलयन है। ऐनोड से ताँबा घुलता है और उतना ही शुद्ध ताँबा कैथोड पर जमा होता है। अघुलनशील अशुद्धियाँ ऐनोड के नीचे **ऐनोड पंक** के रूप में बैठ जाती हैं।",
           "**અશુદ્ધ તાંબું ઍનોડ** છે અને **શુદ્ધ તાંબાની પાતળી પટ્ટી કૅથોડ**; વિદ્યુતવિભાજ્ય ઍસિડિક કૉપર સલ્ફેટનું દ્રાવણ છે. ઍનોડમાંથી તાંબું ઓગળે છે અને તેટલું જ શુદ્ધ તાંબું કૅથોડ પર જમા થાય છે. અદ્રાવ્ય અશુદ્ધિઓ ઍનોડ નીચે **ઍનોડ પંક** તરીકે બેસી જાય છે.")},
]


if __name__ == "__main__":
    from insert import insert_figures
    ch2, ch3 = (a.rstrip("/") for a in sys.argv[1:3])
    ph_scale(f"{ch2}/fig_ph_scale.png")
    electrolytic_refining(f"{ch3}/fig_electrolytic_refining.png")
    if "--draw-only" not in sys.argv:
        insert_figures(ch2, FIGURES_CH2)
        insert_figures(ch3, FIGURES_CH3)
