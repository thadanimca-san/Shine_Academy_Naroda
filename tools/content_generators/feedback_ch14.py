"""Per-option explanations for Ch 14 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/maths/ncert_rationalised/ch14_probability"

F = {
 "ch14.s2.check1": {"$0.95$": "Correct! $1 - 0.05$.", "$0.05$": "That is $P(E)$ itself.", "$1.05$": "Subtract from 1, do not add.", "$0.5$": "$1 - 0.05 = 0.95$."},
 "ch14.s2.check2": {"$-1.5$": "Correct! A probability is never negative.", "$\\dfrac{2}{3}$": "It lies between 0 and 1, so it can be a probability.", "$15\\%$": "15% is 0.15, which lies between 0 and 1.", "$0.7$": "It lies between 0 and 1."},
 "ch14.s3.check": {"$\\dfrac{3}{4}$": "Correct!", "$\\dfrac{1}{2}$": "HH also has a head: count HH, HT, TH.", "$\\dfrac{1}{4}$": "That is exactly two heads.", "$\\dfrac{2}{3}$": "There are 4 equally likely outcomes, not 3."},
 "ch14.q.ex14_1.q1.i": {"$1$": "Correct!", "$0$": "They are complementary: together they are certain.", "$2$": "No probability adds up to more than 1 here.", "$\\dfrac{1}{2}$": "That is true only when both are equally likely."},
 "ch14.q.ex14_1.q1.ii": {"$0$, an impossible event": "Correct!", "$1$, a sure event": "That is for an event that is certain.", "$0$, a sure event": "The value 0 is right, but the event is impossible.", "$1$, an impossible event": "An impossible event has probability 0."},
 "ch14.q.ex14_1.q1.iii": {"$1$, a sure or certain event": "Correct!", "$0$, an impossible event": "That is for an event that cannot happen.", "$1$, an impossible event": "The value 1 is right, but the event is sure.", "$\\dfrac{1}{2}$, a sure event": "A sure event has probability 1."},
 "ch14.q.ex14_1.q1.iv": {"$1$": "Correct!", "$0$": "Together they cover every outcome.", "the number of outcomes": "Each probability is a fraction; together they make 1.", "$\\dfrac{1}{2}$": "Together they cover every outcome, so the sum is 1."},
 "ch14.q.ex14_1.q1.v": {"$0$ and $1$": "Correct!", "$-1$ and $1$": "A probability is never negative.", "$0$ and $100$": "That is for percentages; as a number it is 0 to 1.", "$1$ and $2$": "A probability is at most 1."},
 "ch14.q.ex14_1.q4": {"$\\dfrac{2}{3}$": "It lies between 0 and 1.", "$-1.5$": "Correct!", "$15\\%$": "15% is 0.15.", "$0.7$": "It lies between 0 and 1."},
 "ch14.q.sqp8": {"$\\dfrac{5}{36}$": "That is the probability of getting the sum 8.", "$\\dfrac{31}{36}$": "Correct!", "$\\dfrac{5}{18}$": "The sum 8 occurs 5 times out of 36.", "$\\dfrac{5}{9}$": "Use $1 - \\dfrac{5}{36}$."},
 "ch14.q.sqp15": {"$\\dfrac{4}{11}$": "That is the probability itself.", "$\\dfrac{9}{4}$": "Correct!", "$\\dfrac{11}{4}$": "That is $2x$; solve $2x + 1 = \\dfrac{11}{2}$.", "$\\dfrac{4}{9}$": "Solve $\\dfrac{2}{2x + 1} = \\dfrac{4}{11}$."},
 "ch14.q.mcq01": {"$1$": "Correct!", "$0$": "That is an impossible event.", "$\\dfrac{1}{2}$": "A sure event always happens.", "$-1$": "A probability is never negative."},
 "ch14.q.mcq02": {"$0.7$": "Correct!", "$0.3$": "That is $P(E)$.", "$1.3$": "Subtract from 1.", "$0.03$": "$1 - 0.3 = 0.7$."},
 "ch14.q.mcq03": {"$0$": "Correct!", "$1$": "No face is greater than 6.", "$\\dfrac{1}{6}$": "No face is greater than 6.", "$\\dfrac{5}{6}$": "No face is greater than 6."},
 "ch14.q.mcq04": {"$\\dfrac{3}{4}$": "Correct!", "$\\dfrac{1}{2}$": "Count HH too.", "$\\dfrac{1}{4}$": "That is two heads only.", "$1$": "TT has no head."},
 "ch14.q.mcq05": {"$\\dfrac{1}{13}$": "Correct!", "$\\dfrac{1}{52}$": "That is one particular ace.", "$\\dfrac{1}{4}$": "That is one suit.", "$\\dfrac{4}{13}$": "4 aces among 52, not 13."},
 "ch14.q.mcq06": {"$\\dfrac{2}{11}$": "Correct!", "$\\dfrac{1}{11}$": "B appears twice.", "$\\dfrac{1}{10}$": "The word has 11 letters.", "$\\dfrac{2}{9}$": "Count all 11 letters, repeats included."},
 "ch14.q.mcq07": {"$\\dfrac{1}{6}$": "Correct!", "$\\dfrac{1}{36}$": "That is one particular doublet.", "$\\dfrac{1}{12}$": "There are 6 doublets out of 36.", "$\\dfrac{1}{3}$": "There are 6 doublets out of 36."},
 "ch14.q.mcq08": {"$\\dfrac{1}{4}$": "Correct!", "$\\dfrac{1}{5}$": "There are 5 multiples of 4, not 4.", "$\\dfrac{4}{20}$": "20 is also a multiple of 4.", "$\\dfrac{1}{2}$": "That is for even numbers."},
 "ch14.q.mcq09": {"$0$": "Correct!", "$\\dfrac{1}{36}$": "Even 6 + 6 is only 12.", "$\\dfrac{1}{13}$": "A sum of 13 cannot happen.", "$1$": "A sum of 13 cannot happen."},
 "ch14.q.mcq10": {"$\\dfrac{3}{5}$": "Correct!", "$\\dfrac{2}{5}$": "That is for red.", "$\\dfrac{1}{6}$": "6 blue out of 10 balls.", "$\\dfrac{3}{2}$": "Divide by the total, 10, not by 4."},
}
AR = {
 "ch14.q.ar1": ("every face of a die is less than 7.", "a sure event is exactly what A describes."),
 "ch14.q.ar2": ("head and tail are two equally likely outcomes.", "it is true, but A comes from the two equally likely outcomes."),
 "ch14.q.ar3": ("HT and TH both give one of each, so it is $\\dfrac{2}{4} = \\dfrac{1}{2}$.", "these four outcomes are equally likely."),
 "ch14.q.ar4": ("E and 'not E' are complementary.", "for example, $P(E) = 0.2$ is less than $P(\\text{not } E) = 0.8$."),
 "ch14.q.ar5": ("$\\dfrac{6}{52} = \\dfrac{3}{26}$.", "6 red face cards is exactly the count used in A."),
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
