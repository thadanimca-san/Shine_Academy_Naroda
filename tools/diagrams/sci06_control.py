"""Labelled schematic diagrams for Class 10 Science Ch 6 (Control and Coordination).
Usage: python3 tools/diagrams/sci06_control.py <chapter folder>
"""
import math
import sys
from figlib import Fig, BLACK, GREY, RED, BLUE, GREEN, ORANGE, PURPLE, label, box, lerp

NEURON, NUCLEUS = (230, 160, 60), (150, 80, 160)


def branch(fig, start, ang, length, depth, color, width):
    """A small branching tree, used for dendrites and nerve endings."""
    a = math.radians(ang)
    end = (start[0] + length * math.cos(a), start[1] + length * math.sin(a))
    fig.line(start, end, color, width)
    if depth:
        for turn in (-30, 30):
            branch(fig, end, ang + turn, length * 0.62, depth - 1, color, max(1.5, width * 0.7))
    return end


def neuron(path):
    fig = Fig(-4.6, 15.6, -3.2, 3.4)
    body = (0, 0)
    for ang in (100, 150, 200, 250, 300):
        branch(fig, (body[0] + 0.7 * math.cos(math.radians(ang)), 0.7 * math.sin(math.radians(ang))), ang, 1.1, 2, NEURON, 3.5)
    fig.circle(body, 0.95, (180, 110, 30), 3, fill=(250, 220, 170))
    fig.circle((-0.1, 0.05), 0.35, NUCLEUS, 2, fill=(215, 185, 235))
    # Axon with a myelin-like sheath, then nerve endings.
    fig.line((0.95, 0), (12.0, 0), NEURON, 5)
    for x in (2.0, 4.3, 6.6, 8.9):
        fig.rect((x, -0.28), (x + 1.9, 0.28), (255, 240, 200), (200, 150, 70), 2)
    for ang in (-40, 0, 40):
        branch(fig, (12.0, 0), ang, 1.0, 1, NEURON, 3)
    fig.arrow((4.0, -1.6), (9.0, -1.6), RED, 3)
    fig.text((6.5, -1.75), "Direction of the nerve impulse", 15, RED, "mt")
    label(fig, (-1.75, 1.5), (-3.2, 2.9), "Dendrites", anchor="mm")
    label(fig, (0.5, 0.75), (2.0, 2.6), "Cell body")
    label(fig, (-0.1, 0.05), (-3.6, -2.0), "Nucleus", anchor="mm")
    label(fig, (7.7, 0.05), (7.7, 2.4), "Axon", anchor="mm")
    label(fig, (13.5, 0.9), (13.2, 2.6), "Nerve endings", anchor="mm")
    fig.save(path)


def reflex_arc(path):
    fig = Fig(-1.0, 17.0, -6.2, 4.6)
    # Spinal cord, cut across: an oval with grey matter in the middle.
    cord = (12.5, 0.4)
    fig.ellipse(cord, 3.2, 2.6, (120, 120, 120), 3, fill=(245, 245, 245))
    fig.ellipse(cord, 1.3, 1.6, (150, 150, 150), 2, fill=(215, 215, 215))
    fig.text((cord[0], cord[1] + 2.9), "Spinal cord", 18, BLACK, "mb", bold=True)
    # Receptor in the skin (left, top) and effector muscle (left, bottom).
    box(fig, (2.0, 2.6), 3.6, 1.4, "Receptor", fill=(225, 245, 225), outline=GREEN, sub="in the skin (senses heat)")
    box(fig, (2.0, -3.4), 3.6, 1.4, "Effector", fill=(255, 225, 225), outline=RED, sub="muscle (pulls the hand away)")
    # Sensory neuron: receptor → into the dorsal side of the cord.
    sens = [(3.8, 2.6), (8.5, 2.6), (11.2, 1.3), (12.1, 0.9)]
    fig.polyline(sens, BLUE, 4)
    fig.head(lerp(sens[0], sens[1], 0.55), (1, 0), BLUE, 16)
    fig.circle((8.0, 2.6), 0.32, BLUE, 2.5, fill="white")
    fig.text((6.0, 2.6), "Sensory neuron", 16, BLUE, "mb", dy=-12, bold=True)
    # Relay neuron in the grey matter.
    fig.line((12.1, 0.9), (12.6, -0.2), PURPLE, 4)
    fig.dot((12.1, 0.9), 6, PURPLE)
    fig.dot((12.6, -0.2), 6, PURPLE)
    label(fig, (12.35, 0.35), (14.6, -3.0), "Relay neuron (in grey matter)", anchor="mm")
    # Motor neuron: out of the ventral side → effector.
    mot = [(12.6, -0.2), (11.2, -1.0), (8.5, -3.4), (3.8, -3.4)]
    fig.polyline(mot, RED, 4)
    fig.head(lerp(mot[2], mot[3], 0.45), (-1, 0), RED, 16)
    fig.text((6.0, -3.4), "Motor neuron", 16, RED, "mt", dy=12, bold=True)
    fig.text((2.0, 0.0), "Quick, automatic response:", 15, GREY)
    fig.text((2.0, -0.6), "the brain is not involved", 15, GREY)
    fig.save(path)


def brain(path):
    fig = Fig(-7.6, 9.0, -7.4, 5.2)
    # Cerebrum (fore-brain): a large dome, front to the left.
    dome = [(5.4 * math.cos(math.radians(a)), 0.6 + 3.9 * math.sin(math.radians(a))) for a in range(0, 181, 4)]
    dome += [(-5.4, 0.6), (-5.0, -0.9), (-2.0, -1.4), (1.0, -1.0), (4.6, -0.6), (5.4, 0.6)]
    fig.polygon(dome, (250, 215, 205), (170, 90, 80), 3)
    for k in range(5):  # a few folds
        x = -3.6 + 1.8 * k
        fig.polyline([(x, 3.2 - abs(x) * 0.2), (x + 0.5, 2.2), (x - 0.2, 1.3), (x + 0.4, 0.4)], (190, 120, 110), 2)
    # Mid-brain, pons, medulla, spinal cord.
    fig.polygon([(0.6, -1.0), (2.2, -0.8), (2.0, -2.0), (0.8, -2.0)], (245, 200, 160), (170, 110, 60), 2.5)
    fig.ellipse((1.6, -2.7), 0.95, 0.75, (170, 110, 60), 2.5, fill=(245, 190, 150))
    fig.polygon([(1.0, -3.3), (2.2, -3.3), (2.0, -5.0), (1.2, -5.0)], (240, 180, 140), (170, 110, 60), 2.5)
    fig.polygon([(1.2, -5.0), (2.0, -5.0), (1.9, -7.0), (1.3, -7.0)], (235, 225, 200), (150, 140, 110), 2.5)
    # Cerebellum: behind and below the cerebrum.
    fig.ellipse((4.3, -2.3), 1.9, 1.3, (120, 90, 60), 3, fill=(230, 200, 170))
    for k in range(4):
        fig.arc((4.3, -2.3), 0.4 + 0.35 * k, 200, 340, (150, 110, 80), 1.5)
    label(fig, (-2.5, 2.8), (-6.4, 4.6), "Fore-brain (cerebrum)", anchor="lm")
    label(fig, (1.4, -1.4), (-5.0, -2.2), "Mid-brain", anchor="rm")
    label(fig, (1.4, -2.7), (-5.0, -3.4), "Pons", anchor="rm")
    label(fig, (1.6, -4.2), (-5.0, -4.6), "Medulla", anchor="rm")
    label(fig, (1.6, -6.3), (-5.0, -6.3), "Spinal cord", anchor="rm")
    label(fig, (5.2, -2.6), (6.4, -4.4), "Cerebellum", anchor="lm")
    fig.text((6.6, -5.2), "Pons, medulla and cerebellum", 13, GREY, "lm")
    fig.text((6.6, -5.75), "form the hind-brain", 13, GREY, "lm")
    fig.text((-6.4, 0.6), "Front", 14, GREY, "rm")
    fig.save(path)


FIGURES = [
 {"id": "s2.fig1", "after": "s2.reveal", "file": "fig_neuron.png",
  "title": ("Structure of a neuron", "तंत्रिका कोशिका (न्यूरॉन) की संरचना", "ચેતાકોષ (ન્યુરૉન)ની રચના"),
  "body": ("**Dendrites** pick up information, the **cell body** passes it on as an electrical impulse along the **axon**, and at the **nerve endings** the impulse is passed to the next cell by chemicals.",
           "**द्रुमिकाएँ** सूचना ग्रहण करती हैं, **कोशिकाकाय** उसे विद्युत आवेग के रूप में **तंत्रिकाक्ष** से आगे भेजता है, और **तंत्रिका सिरों** पर रसायनों द्वारा आवेग अगली कोशिका तक पहुँचता है।",
           "**શિખાતંતુઓ** માહિતી ગ્રહણ કરે છે, **કોષકાય** તેને વિદ્યુત આવેગ તરીકે **ચેતાક્ષ** દ્વારા આગળ મોકલે છે, અને **ચેતાના છેડા** પર રસાયણો દ્વારા આવેગ પછીના કોષ સુધી પહોંચે છે.")},
 {"id": "s2.fig2", "after": "s2.fig1", "file": "fig_reflex_arc.png",
  "title": ("Reflex arc", "प्रतिवर्ती चाप", "પરાવર્તી ચાપ"),
  "body": ("When you touch something hot: the **receptor** senses it, the **sensory neuron** carries the message to the **spinal cord**, a **relay neuron** passes it to the **motor neuron**, and the **effector muscle** pulls the hand away, before the brain even knows.",
           "गर्म वस्तु छूने पर: **ग्राही** उसे महसूस करता है, **संवेदी तंत्रिका** संदेश **मेरुरज्जु** तक ले जाती है, **मध्यवर्ती (रिले) तंत्रिका** उसे **प्रेरक तंत्रिका** को देती है, और **प्रभावी पेशी** हाथ को हटा देती है; यह मस्तिष्क के जानने से पहले हो जाता है।",
           "ગરમ વસ્તુને અડકતાં: **ગ્રાહી** તેને અનુભવે છે, **સંવેદી ચેતા** સંદેશો **કરોડરજ્જુ** સુધી લઈ જાય છે, **મધ્યવર્તી (રિલે) ચેતા** તેને **ચાલક ચેતા**ને આપે છે, અને **કાર્યકારી સ્નાયુ** હાથ ખેંચી લે છે; આ મગજને ખબર પડે તે પહેલાં થઈ જાય છે.")},
 {"id": "s3.fig1", "after": "s3.thm", "file": "fig_brain.png",
  "title": ("Parts of the human brain", "मानव मस्तिष्क के भाग", "માનવ મગજના ભાગો"),
  "body": ("The **fore-brain (cerebrum)** thinks and controls voluntary actions. The **mid-brain** and the **hind-brain** (pons, medulla, cerebellum) control involuntary actions; the **cerebellum** keeps posture and balance, and the **medulla** controls blood pressure, salivation and vomiting.",
           "**अग्रमस्तिष्क (प्रमस्तिष्क)** सोचता है और ऐच्छिक क्रियाओं का नियंत्रण करता है। **मध्यमस्तिष्क** और **पश्चमस्तिष्क** (पॉन्स, मेडुला, अनुमस्तिष्क) अनैच्छिक क्रियाओं का नियंत्रण करते हैं; **अनुमस्तिष्क** शरीर की स्थिति और संतुलन बनाए रखता है, और **मेडुला** रक्तचाप, लार आना और वमन का नियंत्रण करता है।",
           "**અગ્રમગજ (પ્રમસ્તિષ્ક)** વિચારે છે અને ઐચ્છિક ક્રિયાઓનું નિયંત્રણ કરે છે. **મધ્યમગજ** અને **પશ્ચમગજ** (પોન્સ, લંબમજ્જા, અનુમસ્તિષ્ક) અનૈચ્છિક ક્રિયાઓનું નિયંત્રણ કરે છે; **અનુમસ્તિષ્ક** શરીરની સ્થિતિ અને સંતુલન જાળવે છે, અને **લંબમજ્જા** રુધિરનું દબાણ, લાળ ઝરવી અને ઊલટીનું નિયંત્રણ કરે છે.")},
]


if __name__ == "__main__":
    from insert import insert_figures
    out = sys.argv[1].rstrip("/")
    neuron(f"{out}/fig_neuron.png")
    reflex_arc(f"{out}/fig_reflex_arc.png")
    brain(f"{out}/fig_brain.png")
    if "--draw-only" not in sys.argv:
        insert_figures(out, FIGURES)
