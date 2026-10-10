"""Per-option explanations for Ch 13 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/maths/ncert_rationalised/ch13_statistics"

F = {
 "ch13.s2.check": {"$25$": "Correct! $\\dfrac{20 + 30}{2}$.", "$20$": "That is the lower limit.", "$30$": "That is the upper limit.", "$10$": "That is the class size."},
 "ch13.s3.check": {"the class just before the modal class": "Correct!", "the modal class": "The modal class frequency is $f_1$.", "the class just after the modal class": "That is $f_2$.", "the first class": "$f_0$ is the neighbour just before the modal class."},
 "ch13.s4.check": {"$20 - 30$": "Correct!", "$10 - 20$": "Its $cf$ is 13, less than 20.", "$30 - 40$": "$25$ already reaches 20 in the class before.", "$0 - 10$": "Its $cf$ is only 5."},
 "ch13.q.sqp17": {"is increased by 2": "Correct!", "is decreased by 2": "Every value goes up, so the middle value goes up.", "is two times the original number": "Adding 2 does not double anything.", "remains the same as that of the original observations": "The middle observation itself increases by 2."},
 "ch13.q.mcq01": {"$17.5$": "Correct!", "$15$": "That is the class size.", "$10$": "That is the lower limit.", "$35$": "That is the sum; halve it."},
 "ch13.q.mcq02": {"$\\dfrac{x_i - a}{h}$": "Correct!", "$x_i - a$": "That is $d_i$; divide by $h$.", "$\\dfrac{x_i}{h}$": "Subtract the assumed mean first.", "$\\dfrac{a - x_i}{h}$": "The order is $x_i - a$."},
 "ch13.q.mcq03": {"highest frequency": "Correct!", "highest class mark": "Mode is about how often, not how big.", "highest cumulative frequency": "That is always the last class.", "middle position": "That is the idea of the median."},
 "ch13.q.mcq04": {"cumulative frequencies": "Correct!", "class marks": "Class marks are for the mean.", "modal class": "The modal class is for the mode.", "assumed mean": "The assumed mean is for the mean."},
 "ch13.q.mcq05": {"$3 \\times$ Median $=$ Mode $+ 2 \\times$ Mean": "Correct!", "$3 \\times$ Mean $=$ Mode $+ 2 \\times$ Median": "Median and mean are swapped.", "$3 \\times$ Mode $=$ Median $+ 2 \\times$ Mean": "It is 3 times the median.", "Mode $=$ Mean $+$ Median": "Mode $= 3 \\times$ Median $- 2 \\times$ Mean."},
 "ch13.q.mcq06": {"$26$": "Correct!", "$24$": "Mode $= 66 - 40$.", "$21$": "That is the average of 20 and 22.", "$18$": "Mode $= 3 \\times 22 - 2 \\times 20$."},
 "ch13.q.mcq07": {"$30$": "Correct!", "$75$": "Divide 1500 by 50, not 20.", "$1450$": "Divide, do not subtract.", "$3$": "$1500 \\div 50 = 30$."},
 "ch13.q.mcq08": {"the class before the median class": "Correct!", "the median class": "Use the running total before the median class.", "the last class": "That is the total $n$.", "the class after the median class": "Use the class before it."},
 "ch13.q.mcq09": {"the class after the modal class": "Correct!", "the class before the modal class": "That is $f_0$.", "the modal class": "That is $f_1$.", "the last class": "$f_2$ is the modal class's next neighbour."},
 "ch13.q.mcq10": {"$117.5 - 126.5$": "Correct!", "$118 - 127$": "Move both limits by 0.5.", "$117 - 126$": "Subtract 0.5, not 1.", "$118.5 - 126.5$": "The lower limit goes down to 117.5."},
}
AR = {
 "ch13.q.ar1": ("$\\dfrac{10 + 25}{2} = 17.5$.", "this formula is exactly what gives 17.5."),
 "ch13.q.ar2": ("the modal class has the highest frequency.", "it is true, but it is about the mean, not the mode."),
 "ch13.q.ar3": ("the continuous class is 126.5–135.5, so the lower limit is 126.5.", "the formulas need classes without gaps."),
 "ch13.q.ar4": ("the assumed mean only shifts the numbers and shifts them back.", "any number can be the assumed mean."),
 "ch13.q.ar5": ("the median is $\\dfrac{3 + 5}{2} = 4$.", "with an even count there are two middle values."),
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
