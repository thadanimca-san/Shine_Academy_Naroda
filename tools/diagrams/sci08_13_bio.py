"""Charts for Class 10 Science Ch 8 (Mendel's cross, sex determination) and
Ch 13 (food chain and the 10 per cent energy law).
Usage: python3 tools/diagrams/sci08_13_bio.py <ch08 folder> <ch13 folder>
"""
import sys
from figlib import Fig, BLACK, GREY, RED, BLUE, GREEN, ORANGE, PURPLE, box

TALL, SHORT = (40, 140, 70), (200, 120, 40)
MALE, FEMALE = (40, 100, 200), (200, 60, 130)


def arrow_down(fig, x, y0, y1, color=GREY):
    fig.arrow((x, y0), (x, y1), color, 2.5, size=13)


def monohybrid(path):
    fig = Fig(-7.0, 7.0, -11.6, 3.4)
    fig.text((-6.8, 2.6), "Parents", 16, GREY, "lm", bold=True)
    box(fig, (-2.6, 2.2), 3.6, 1.3, "TT", fill=(220, 240, 225), outline=TALL, sub="pure tall")
    fig.text((0, 2.2), "×", 26, BLACK, bold=True)
    box(fig, (2.6, 2.2), 3.6, 1.3, "tt", fill=(250, 235, 215), outline=SHORT, sub="pure short")
    arrow_down(fig, 0, 1.4, 0.3)
    fig.text((-6.8, -0.4), "F1", 16, GREY, "lm", bold=True)
    box(fig, (0, -0.4), 4.4, 1.3, "Tt", fill=(220, 240, 225), outline=TALL, sub="all tall")
    arrow_down(fig, 0, -1.15, -2.2)
    fig.text((0, -2.6), "F1 self-pollinated: Tt × Tt", 16, BLACK, bold=True)
    # F2 Punnett square.
    fig.text((-6.8, -6.3), "F2", 16, GREY, "lm", bold=True)
    x0, y0, c = -2.0, -4.0, 2.0
    fig.text((x0 - 0.6, y0 + 0.5), "♂ / ♀", 14, GREY)
    for i, g in enumerate("Tt"):
        fig.text((x0 + c * (i + 0.5), y0 + 0.5), g, 20, BLACK, bold=True)
        fig.text((x0 - 0.6, y0 - c * (i + 0.5)), g, 20, BLACK, bold=True)
    cells = [["TT", "Tt"], ["Tt", "tt"]]
    for r in range(2):
        for k in range(2):
            g = cells[r][k]
            col, fill = (TALL, (220, 240, 225)) if "T" in g else (SHORT, (250, 235, 215))
            fig.rect((x0 + c * k, y0 - c * (r + 1)), (x0 + c * (k + 1), y0 - c * r), fill, col, 2.5)
            fig.text((x0 + c * (k + 0.5), y0 - c * (r + 0.5)), g, 22, col, bold=True)
    fig.text((0, -8.9), "Phenotype ratio  tall : short = 3 : 1", 17, BLACK, bold=True)
    fig.text((0, -9.7), "Genotype ratio  TT : Tt : tt = 1 : 2 : 1", 17, GREY)
    fig.text((0, -10.6), "T (tall) is dominant; t (short) is recessive", 14, GREY)
    fig.save(path)


def sex_determination(path):
    fig = Fig(-7.4, 7.4, -7.6, 3.2)
    box(fig, (-3.4, 2.0), 4.6, 1.3, "Father: XY", fill=(220, 232, 252), outline=MALE)
    box(fig, (3.4, 2.0), 4.6, 1.3, "Mother: XX", fill=(252, 225, 238), outline=FEMALE)
    fig.text((-6.9, -0.6), "Sperms", 15, MALE, "lm", bold=True)
    fig.text((6.9, -0.6), "Eggs", 15, FEMALE, "rm", bold=True)
    sperm = [(-4.6, "X"), (-2.2, "Y")]
    eggs = [(2.2, "X"), (4.6, "X")]
    for x, g in sperm:
        fig.arrow((-3.4, 1.3), (x, -0.05), MALE, 2.2, size=11)
        fig.circle((x, -0.6), 0.5, MALE, 2.5, fill="white")
        fig.text((x, -0.6), g, 18, MALE, bold=True)
    for x, g in eggs:
        fig.arrow((3.4, 1.3), (x, -0.05), FEMALE, 2.2, size=11)
        fig.circle((x, -0.6), 0.5, FEMALE, 2.5, fill="white")
        fig.text((x, -0.6), g, 18, FEMALE, bold=True)
    kids = [(-5.1, "XX", "Girl", FEMALE), (-1.7, "XY", "Boy", MALE), (1.7, "XX", "Girl", FEMALE), (5.1, "XY", "Boy", MALE)]
    for x, g, who, col in kids:
        box(fig, (x, -4.0), 2.9, 1.5, g, fill=(250, 250, 250), outline=col, sub=who, size=18)
    # Each sperm meets each egg: X sperm → girls (XX), Y sperm → boys (XY).
    links = {sperm[0][0]: (0, 2), sperm[1][0]: (1, 3), eggs[0][0]: (0, 1), eggs[1][0]: (2, 3)}
    for x, kid_ids in links.items():
        for k in kid_ids:
            fig.line((x, -1.1), (kids[k][0], -3.25), (205, 205, 205), 1.5)
    fig.text((0, -5.6), "Girl : Boy = 1 : 1", 18, BLACK, bold=True)
    fig.text((0, -6.5), "The father's sperm (X or Y) decides the sex of the child", 15, GREY)
    fig.save(path)


def food_chain(path):
    fig = Fig(-1.0, 25.0, -4.4, 3.4)
    steps = [("Grass", "Producer", "1st trophic level", (220, 245, 215), GREEN),
             ("Grasshopper", "Herbivore", "2nd: primary consumer", (250, 245, 210), (180, 150, 20)),
             ("Frog", "Carnivore", "3rd: secondary consumer", (225, 240, 250), BLUE),
             ("Snake", "Carnivore", "4th: tertiary consumer", (250, 230, 215), ORANGE),
             ("Eagle", "Top carnivore", "5th trophic level", (245, 225, 240), PURPLE)]
    w, gap = 4.2, 1.0
    for i, (name, kind, level, fill, col) in enumerate(steps):
        x = i * (w + gap) + w / 2
        box(fig, (x, 0.9), w, 1.9, name, fill=fill, outline=col, sub=kind, size=19)
        fig.text((x, -0.5), level, 14, col, "mt")
        if i:
            fig.arrow((x - w / 2 - gap + 0.1, 0.9), (x - w / 2 - 0.1, 0.9), BLACK, 3, size=14)
    fig.text((12.0, -2.2), "Arrows show the direction in which food (energy) passes", 15, GREY)
    fig.text((12.0, -3.1), "Energy comes from the Sun; producers capture it by photosynthesis", 15, GREY)
    fig.save(path)


def energy_pyramid(path):
    fig = Fig(-9.0, 9.0, -1.0, 9.4)
    levels = [("Producers", "10,000 J", (150, 210, 130)), ("Herbivores", "1,000 J", (240, 220, 120)),
              ("Carnivores", "100 J", (130, 180, 230)), ("Top carnivores", "10 J", (220, 150, 200))]
    h = 2.0
    for i, (name, energy, col) in enumerate(levels):
        y0, y1 = i * h, (i + 1) * h
        hw0, hw1 = 8.0 - 1.5 * i, 8.0 - 1.5 * (i + 1)
        fig.polygon([(-hw0, y0), (hw0, y0), (hw1, y1), (-hw1, y1)], col, BLACK, 2)
        fig.text((0, (y0 + y1) / 2), f"{name}: {energy}", 17, BLACK, bold=True)
    fig.text((0, 8.6), "Only about 10% of the energy passes to the next level", 16, BLACK, bold=True)
    fig.text((0, -0.5), "The rest is used for life processes or lost as heat", 14, GREY)
    fig.save(path)


FIGURES_CH8 = [
 {"id": "s3.fig1", "after": "s3.table", "file": "fig_monohybrid_cross.png",
  "title": ("Mendel's monohybrid cross", "मेंडल का एकसंकर संकरण", "મેન્ડલનું એકસંકરણ"),
  "body": ("A pure tall plant (TT) crossed with a pure short plant (tt) gives **all tall** F1 plants (Tt). When F1 plants are self-pollinated, the F2 generation shows **tall : short = 3 : 1**, so the trait for shortness was hidden, not lost.",
           "शुद्ध लंबे पौधे (TT) का शुद्ध बौने पौधे (tt) से संकरण कराने पर F1 के **सभी पौधे लंबे** (Tt) होते हैं। F1 पौधों के स्वपरागण से F2 पीढ़ी में **लंबे : बौने = 3 : 1** मिलते हैं, यानी बौनेपन का लक्षण छिपा था, खोया नहीं था।",
           "શુદ્ધ ઊંચા છોડ (TT)નું શુદ્ધ નીચા છોડ (tt) સાથે સંકરણ કરતાં F1ના **બધા છોડ ઊંચા** (Tt) થાય છે. F1 છોડના સ્વપરાગનયનથી F2 પેઢીમાં **ઊંચા : નીચા = 3 : 1** મળે છે, એટલે કે નીચાપણાનું લક્ષણ છુપાયું હતું, ખોવાયું ન હતું.")},
 {"id": "s6.fig1", "after": "s6.thm", "file": "fig_sex_determination.png",
  "title": ("Sex determination in human beings", "मनुष्य में लिंग निर्धारण", "મનુષ્યમાં લિંગ નિશ્ચયન"),
  "body": ("A mother's eggs always carry an **X** chromosome. Half of a father's sperms carry **X** and half carry **Y**. An X sperm gives a girl (XX) and a Y sperm gives a boy (XY), so the chance is **1 : 1** and the father's sperm decides the sex.",
           "माता के अंडों में हमेशा **X** गुणसूत्र होता है। पिता के आधे शुक्राणुओं में **X** और आधे में **Y** होता है। X शुक्राणु से पुत्री (XX) और Y शुक्राणु से पुत्र (XY) होता है, इसलिए संभावना **1 : 1** है और लिंग पिता का शुक्राणु तय करता है।",
           "માતાના અંડકોષમાં હંમેશાં **X** રંગસૂત્ર હોય છે. પિતાના અડધા શુક્રકોષમાં **X** અને અડધામાં **Y** હોય છે. X શુક્રકોષથી છોકરી (XX) અને Y શુક્રકોષથી છોકરો (XY) થાય છે, તેથી સંભાવના **1 : 1** છે અને લિંગ પિતાનો શુક્રકોષ નક્કી કરે છે.")},
]
FIGURES_CH13 = [
 {"id": "s3.fig1", "after": "s3.table", "file": "fig_food_chain.png",
  "title": ("A food chain and its trophic levels", "एक आहार श्रृंखला और उसके पोषी स्तर", "એક આહારશૃંખલા અને તેના પોષક સ્તર"),
  "body": ("Each step of a food chain is a **trophic level**. Producers (green plants) form the first level; herbivores, then carnivores, form the next levels. Energy flows in **one direction only**, from producers to consumers.",
           "आहार श्रृंखला का हर चरण एक **पोषी स्तर** है। उत्पादक (हरे पौधे) पहला स्तर बनाते हैं; शाकाहारी और फिर मांसाहारी अगले स्तर बनाते हैं। ऊर्जा **केवल एक दिशा** में, उत्पादकों से उपभोक्ताओं की ओर बहती है।",
           "આહારશૃંખલાનું દરેક પગથિયું એક **પોષક સ્તર** છે. ઉત્પાદકો (લીલી વનસ્પતિ) પહેલું સ્તર બનાવે છે; તૃણાહારી અને પછી માંસાહારી પછીનાં સ્તર બનાવે છે. ઊર્જા **ફક્ત એક જ દિશામાં**, ઉત્પાદકોથી ઉપભોક્તાઓ તરફ વહે છે.")},
 {"id": "s3.fig2", "after": "s3.fig1", "file": "fig_energy_pyramid.png",
  "title": ("The 10 per cent law of energy flow", "ऊर्जा प्रवाह का 10 प्रतिशत नियम", "ઊર્જા પ્રવાહનો 10 ટકાનો નિયમ"),
  "body": ("Only about **10%** of the energy at one trophic level reaches the next. So food chains are short (usually 3 or 4 steps) and there are fewer animals at each higher level.",
           "एक पोषी स्तर की ऊर्जा का केवल लगभग **10%** ही अगले स्तर तक पहुँचता है। इसलिए आहार श्रृंखलाएँ छोटी (प्रायः 3 या 4 चरण) होती हैं और ऊँचे स्तरों पर जीव कम होते जाते हैं।",
           "એક પોષક સ્તરની ઊર્જાનો ફક્ત આશરે **10%** ભાગ જ પછીના સ્તર સુધી પહોંચે છે. તેથી આહારશૃંખલાઓ ટૂંકી (સામાન્ય રીતે 3 કે 4 પગથિયાં) હોય છે અને ઉપલાં સ્તરે સજીવો ઓછા થતા જાય છે.")},
]


if __name__ == "__main__":
    from insert import insert_figures
    ch8, ch13 = (a.rstrip("/") for a in sys.argv[1:3])
    monohybrid(f"{ch8}/fig_monohybrid_cross.png")
    sex_determination(f"{ch8}/fig_sex_determination.png")
    food_chain(f"{ch13}/fig_food_chain.png")
    energy_pyramid(f"{ch13}/fig_energy_pyramid.png")
    if "--draw-only" not in sys.argv:
        insert_figures(ch8, FIGURES_CH8)
        insert_figures(ch13, FIGURES_CH13)
