"""Per-option explanations for Science Ch 11 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/science/ncert_rationalised/ch11_electricity"

F = {
 "sci10ch11.s2.check": {"In parallel with the resistor": "Correct!", "In series with the resistor": "That is how an ammeter is connected.", "Across the battery only": "It must be across the two points being measured.", "Either way, it does not matter": "In series it would block the current."},
 "sci10ch11.s3.check": {"one-fourth": "Correct!", "half": "Area depends on the square of the diameter.", "double": "A thicker wire has less resistance.", "four times": "A thicker wire has less, not more, resistance."},
 "sci10ch11.s4.check": {"2 Ω": "Correct!", "18 Ω": "That is the series value.", "6 Ω": "Parallel gives less than the smallest.", "3 Ω": "That is two 6 Ω in parallel."},
 "sci10ch11.s5.check": {"The cord has a much lower resistance than the element": "Correct!", "The cord carries less current": "The same current flows through both.", "The cord is made of tungsten": "The cord is made of copper.", "The element is connected in parallel with the cord": "They are in series."},
 "sci10ch11.s6.check": {"6 units": "Correct!", "1.5 units": "Multiply power by time, do not divide.", "5 units": "2 × 3 = 6.", "0.67 units": "Multiply, do not divide."},
 "sci10ch11.q.ex.q1": {"1/25": "That is R′/R.", "1/5": "Each piece is R/5; in parallel they give R/25.", "5": "Each piece is R/5, but five in parallel give R/25.", "25": "Correct!"},
 "sci10ch11.q.ex.q2": {"$I^{2}R$": "I²R is power.", "$IR^{2}$": "Correct!", "$VI$": "VI is power.", "$\\dfrac{V^{2}}{R}$": "V²/R is power."},
 "sci10ch11.q.ex.q3": {"100 W": "That is at 220 V.", "75 W": "P = V²/R; halving V gives a quarter.", "50 W": "Power depends on V², not V.", "25 W": "Correct!"},
 "sci10ch11.q.ex.q4": {"1:2": "Series 2R, parallel R/2: the ratio is 1 : 4.", "2:1": "Less heat is produced in series.", "1:4": "Correct!", "4:1": "That is parallel to series."},
 "sci10ch11.q.gseb2025_3": {"$10^{-6}$": "Correct!", "$10^{-3}$": "That is milli.", "$10^{3}$": "That is kilo.", "$10^{6}$": "That is mega."},
 "sci10ch11.q.gseb2025_8": {"Andre-Marie Ampere": "The ampere is the unit of current.", "Alessandro Volta": "Correct!", "Georg Simon Ohm": "The ohm is the unit of resistance."},
 "sci10ch11.q.mcq01": {"coulomb": "Correct!", "ampere": "That is current.", "volt": "That is potential difference.", "ohm": "That is resistance."},
 "sci10ch11.q.mcq02": {"in series": "Correct!", "in parallel": "That is for a voltmeter.", "across the battery only": "That would not measure the current through a device.", "either way": "It must be in series."},
 "sci10ch11.q.mcq03": {"20 Ω": "Correct!", "5 Ω": "A longer wire has more resistance.", "40 Ω": "R ∝ l, not l².", "10 Ω": "Length changes the resistance."},
 "sci10ch11.q.mcq04": {"ohm metre": "Correct!", "ohm": "That is resistance.", "ohm per metre": "ρ = RA/l gives Ω m.", "volt metre": "That is not resistivity."},
 "sci10ch11.q.mcq05": {"3 Ω": "Correct!", "16 Ω": "That is the series value.", "8 Ω": "Parallel gives less than 4 Ω.", "0.33 Ω": "That is 1/R; take the reciprocal."},
 "sci10ch11.q.mcq06": {"four times": "Correct!", "double": "H depends on I².", "half": "More current gives more heat.", "the same": "H depends on I²."},
 "sci10ch11.q.mcq07": {"$3.6 \\times 10^{6}$ J": "Correct!", "$3.6 \\times 10^{3}$ J": "Multiply 1000 W by 3600 s.", "1000 J": "That is 1 kW for 1 s.", "3600 J": "That is 1 W for 1 hour."},
 "sci10ch11.q.mcq08": {"tungsten": "Correct!", "copper": "Copper would melt.", "nichrome": "Nichrome is used in heaters.", "aluminium": "Aluminium would melt."},
 "sci10ch11.q.mcq09": {"a low melting point": "Correct!", "a high melting point": "Then it would not melt in time.", "very low resistance like copper": "It must heat up and melt.", "no resistance": "Then it would never heat up."},
 "sci10ch11.q.mcq10": {"60 kWh": "Correct!", "2 kWh": "That is one day.", "60 000 kWh": "Use kW, not W.", "6 kWh": "1 × 2 × 30 = 60."},
}
AR = {
 "sci10ch11.q.ar1": ("homes use parallel wiring.", "full voltage and independent switching are what a home needs."),
 "sci10ch11.q.ar2": ("the filament glows but the wires stay cool.", "with the same current, a higher resistance gives far more heat."),
 "sci10ch11.q.ar3": ("it is less than the smallest resistance.", "in parallel the reciprocals add."),
 "sci10ch11.q.ar4": ("a thick wire has less resistance.", "a larger area gives less resistance."),
 "sci10ch11.q.ar5": ("a voltmeter is connected in parallel.", "a voltmeter does have a very high resistance."),
}
_TRUTH = {0: (True, True, True), 1: (True, True, False), 2: (True, False, None), 3: (False, True, None)}
_CLAIMS = [(True, True, True), (True, True, False), (True, False, None), (False, True, None)]
def ar_fb(ci, wa, wr):
    a, r, e = _TRUTH[ci]; out = []
    for ca, cr, ce in _CLAIMS:
        if (ca, cr) == (a, r) and (ce is None or ce == e):
            out.append(f"Correct! A is {'true' if a else 'false'}: {wa} R is {'true' if r else 'false'}: {wr}")
        elif ca != a: out.append(f"Check the Assertion again: it is {'true' if a else 'false'}, because {wa}")
        elif cr != r: out.append(f"Check the Reason again: it is {'true' if r else 'false'}, because {wr}")
        else: out.append(("R does explain A: " if e else "Both are true, but R is not the reason A is true: ") + wr)
    return out

def apply(item):
    if item.get("type") == "assertion_reason":
        item["option_feedback"] = ar_fb(item["correct_index"], *AR[item["id"]]); return
    spec = F[item["id"]]
    missing = [o for o in item["options"] if o not in spec]
    assert not missing, (item["id"], missing)
    item["option_feedback"] = [spec[o] for o in item["options"]]
    assert item["option_feedback"][item["correct_index"]].startswith("Correct!"), item["id"]

qp, cp = f"{BASE}/questions.json", f"{BASE}/chapter.json"
bank, chapter = json.load(open(qp)), json.load(open(cp))
n = 0
for q in bank["questions"]:
    if q["type"] in ("mcq", "assertion_reason"): apply(q); n += 1
for s in chapter["sections"]:
    for blk in s["blocks"]:
        if blk["type"] == "knowledge_check": apply(blk); n += 1
for p, d in ((qp, bank), (cp, chapter)):
    with open(p, "w", encoding="utf-8") as f: json.dump(d, f, ensure_ascii=False, indent=2); f.write("\n")
print("items with feedback:", n)
