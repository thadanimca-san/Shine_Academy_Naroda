"""Per-option explanations for Ch 6 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/maths/ncert_rationalised/ch06_triangles"

F = {
 "ch06.s2.check": {
  "Two squares": "Correct! All angles are $90^\\circ$ and all sides are equal, so any two squares are similar.",
  "Two rectangles": "A 2 × 2 and a 2 × 5 rectangle have equal angles but sides not in the same ratio.",
  "Two rhombuses": "Rhombuses can have different angles, e.g. $60^\\circ$ and $90^\\circ$.",
  "Two isosceles triangles": "Their angles can differ, e.g. $70^\\circ, 70^\\circ, 40^\\circ$ and $30^\\circ, 30^\\circ, 120^\\circ$.",
 },
 "ch06.s3.check": {
  "$6$ cm": "Correct! $\\dfrac{2}{3} = \\dfrac{4}{EC}$ gives $EC = 6$ cm.",
  "$\\dfrac{8}{3}$ cm": "That uses $\\dfrac{AD}{DB} = \\dfrac{EC}{AE}$ upside down. Use $\\dfrac{AD}{DB} = \\dfrac{AE}{EC}$.",
  "$1.5$ cm": "Check: $\\dfrac{4}{1.5} \\neq \\dfrac{2}{3}$. Use $\\dfrac{AD}{DB} = \\dfrac{AE}{EC}$.",
  "$5$ cm": "Adding the same amount does not keep the ratio. $\\dfrac{2}{3} = \\dfrac{4}{EC}$.",
 },
 "ch06.s4.check1": {
  "SSS": "Correct! $\\dfrac{3}{6} = \\dfrac{4}{8} = \\dfrac{5}{10}$.",
  "SAS": "SAS needs a known equal angle; here only sides are given.",
  "AAA": "No angles are given; the sides are what we can compare.",
  "RHS": "RHS is a congruence criterion, not a similarity criterion.",
 },
 "ch06.s4.check2": {
  "$\\dfrac{AB}{PQ} = \\dfrac{AC}{PR}$": "Correct! $AB \\leftrightarrow PQ$ and $AC \\leftrightarrow PR$.",
  "$\\dfrac{AB}{PR} = \\dfrac{BC}{QR}$": "$AB$ matches $PQ$, not $PR$.",
  "$\\dfrac{AB}{QR} = \\dfrac{AC}{PQ}$": "Match letters in order: $AB$ with $PQ$, $AC$ with $PR$.",
  "$\\dfrac{AB}{PQ} = \\dfrac{AC}{QR}$": "$AC$ matches $PR$, not $QR$.",
 },
 "ch06.q.ex6_1.q1.i": {
  "similar": "Correct! All circles have the same shape.",
  "congruent": "Circles of different radii are not the same size, so not congruent.",
  "equal in area": "A bigger circle has a bigger area.",
  "concentric": "Concentric means having the same centre; circles can be anywhere.",
 },
 "ch06.q.ex6_1.q1.ii": {
  "similar": "Correct! Equal angles and proportional sides.",
  "congruent": "Squares of different sides are not the same size.",
  "equal in area": "A bigger square has a bigger area.",
  "equal in perimeter": "A bigger square has a bigger perimeter.",
 },
 "ch06.q.ex6_1.q1.iii": {
  "equilateral": "Correct! Every equilateral triangle has angles $60^\\circ, 60^\\circ, 60^\\circ$.",
  "isosceles": "Isosceles triangles can have different angles.",
  "right-angled": "Right triangles can have different acute angles, like $30^\\circ$ or $45^\\circ$.",
  "scalene": "Scalene triangles can have any angles.",
 },
 "ch06.q.ex6_1.q1.iv": {
  "equal; proportional": "Correct! Equal angles and sides in the same ratio.",
  "proportional; equal": "It is the other way round: angles equal, sides proportional.",
  "equal; equal": "Equal sides would make them congruent; similar needs only proportional sides.",
  "supplementary; proportional": "Corresponding angles must be equal, not supplementary.",
 },
 "ch06.q.mcq01": {
  "$6$ cm": "Correct! $\\dfrac{2}{3} = \\dfrac{4}{EC}$ gives $EC = 6$ cm.",
  "$\\dfrac{8}{3}$ cm": "The ratio is upside down. Use $\\dfrac{AD}{DB} = \\dfrac{AE}{EC}$.",
  "$1.5$ cm": "Check: $\\dfrac{4}{1.5} \\neq \\dfrac{2}{3}$.",
  "$5$ cm": "Adding 1 does not keep the ratio: $\\dfrac{2}{3} = \\dfrac{4}{EC}$.",
 },
 "ch06.q.mcq02": {
  "$12$ cm": "Correct! $\\dfrac{8}{QR} = \\dfrac{2}{3}$ gives $QR = 12$ cm.",
  "$\\dfrac{16}{3}$ cm": "That multiplies by $\\dfrac{2}{3}$. $QR$ is the larger side: $8 \\times \\dfrac{3}{2}$.",
  "$10$ cm": "Use the ratio, not a difference: $8 \\times \\dfrac{3}{2} = 12$.",
  "$24$ cm": "That is $8 \\times 3$; divide by 2 as well.",
 },
 "ch06.q.mcq03": {
  "two squares": "Correct! Equal angles and proportional sides always.",
  "two rectangles": "Their sides need not be in the same ratio.",
  "two rhombuses": "Their angles can differ.",
  "two isosceles triangles": "Their angles can differ.",
 },
 "ch06.q.mcq04": {
  "$70^\\circ$": "Correct! $\\angle B = 60^\\circ$, so $\\angle C = 180^\\circ - 110^\\circ = 70^\\circ$.",
  "$60^\\circ$": "$60^\\circ$ is $\\angle B$ (equal to $\\angle E$).",
  "$50^\\circ$": "$50^\\circ$ is $\\angle A$.",
  "$110^\\circ$": "$110^\\circ$ is $\\angle A + \\angle B$; subtract it from $180^\\circ$.",
 },
 "ch06.q.mcq05": {
  "SSS": "Correct! All three sides are in the ratio $1 : 2$.",
  "SAS": "No angle is given.",
  "AAA": "No angles are given.",
  "RHS": "RHS is a congruence criterion.",
 },
 "ch06.q.mcq06": {
  "$DE \\parallel BC$": "Correct! This is the converse of the Basic Proportionality Theorem.",
  "$DE \\perp BC$": "Equal ratios make $DE$ parallel to $BC$, not perpendicular.",
  "$DE = BC$": "$DE$ is shorter than $BC$ when $D$ and $E$ lie between the vertices.",
  "$AD = AE$": "Equal ratios do not make the lengths equal.",
 },
 "ch06.q.mcq07": {
  "$9$ m": "Correct! $\\dfrac{h}{1.5} = \\dfrac{12}{2}$ gives $h = 9$ m.",
  "$16$ m": "That puts the ratio upside down: $\\dfrac{h}{12} = \\dfrac{1.5}{2}$.",
  "$8$ m": "Check: $\\dfrac{8}{12} \\neq \\dfrac{1.5}{2}$.",
  "$10$ m": "Check: $\\dfrac{10}{12} \\neq \\dfrac{1.5}{2}$.",
 },
 "ch06.q.mcq08": {
  "$\\dfrac{AB}{PQ} = \\dfrac{AC}{PR}$": "Correct! Matching letters in order.",
  "$\\dfrac{AB}{PR} = \\dfrac{BC}{QR}$": "$AB$ matches $PQ$, not $PR$.",
  "$\\dfrac{AB}{QR} = \\dfrac{AC}{PQ}$": "$AB$ matches $PQ$ and $AC$ matches $PR$.",
  "$\\dfrac{AB}{PQ} = \\dfrac{AC}{QR}$": "$AC$ matches $PR$, not $QR$.",
 },
 "ch06.q.mcq09": {
  "$16$ cm": "Correct! $EC = 10$ cm, so $AC = 16$ cm.",
  "$10$ cm": "$10$ cm is $EC$. Add $AE = 6$ cm.",
  "$18$ cm": "$\\dfrac{6}{EC} = \\dfrac{3}{5}$ gives $EC = 10$, so $AC = 16$.",
  "$14$ cm": "$\\dfrac{6}{EC} = \\dfrac{3}{5}$ gives $EC = 10$, so $AC = 16$.",
 },
 "ch06.q.mcq10": {
  "AAA": "Correct! Equal corresponding angles give the AAA criterion.",
  "SSS": "SSS compares sides, not angles.",
  "SAS": "SAS needs two sides in proportion as well.",
  "ASA": "ASA is a congruence criterion.",
 },
 "ch06.q.mcq11": {
  "$27$ cm": "Correct! $18 \\times \\dfrac{6}{4} = 27$ cm.",
  "$12$ cm": "$\\triangle DEF$ is the larger triangle, so its perimeter is more than 18 cm.",
  "$24$ cm": "Adding $6 - 4 = 2$ to each side does not keep the ratio.",
  "$36$ cm": "That doubles it; the ratio is $\\dfrac{6}{4} = 1.5$.",
 },
 "ch06.q.mcq12": {
  "All congruent figures are similar.": "Correct! Same shape and size means same shape.",
  "All similar figures are congruent.": "Similar figures can have different sizes.",
  "Similar figures always have equal areas.": "A bigger similar figure has a bigger area.",
  "Two rectangles are always similar.": "Rectangles can have different side ratios.",
 },
 "ch06.q.sqp14": {
  "$28$ cm": "Perimeter of $\\triangle DEF$ is 27 cm; multiply by $\\dfrac{6}{9}$.",
  "$28.5$ cm": "$\\triangle ABC$ is smaller ($\\dfrac{6}{9} < 1$), so its perimeter is less than 27 cm.",
  "$18$ cm": "Correct! $27 \\times \\dfrac{2}{3} = 18$ cm.",
  "$23$ cm": "The ratio is $\\dfrac{2}{3}$: $27 \\times \\dfrac{2}{3} = 18$ cm.",
 },
}

AR = {
 "ch06.q.ar1": ("$\\dfrac{2}{4} = \\dfrac{3}{EC}$ gives $EC = 6$ cm.", "this is the Basic Proportionality Theorem, which gives the answer directly."),
 "ch06.q.ar2": ("all their angles are $60^\\circ$.", "their sides can have different lengths, so they need not be congruent."),
 "ch06.q.ar3": ("the angles ($90^\\circ$ and $60^\\circ$) are not equal.", "each has four equal sides, so the sides are proportional."),
 "ch06.q.ar4": ("$\\dfrac{2}{4} = \\dfrac{3}{6} = \\dfrac{4}{8}$.", "this is the SSS criterion, which is exactly why they are similar."),
 "ch06.q.ar5": ("congruent triangles have the same shape.", "it is true, but A holds because congruent triangles have the same shape, not because of the angle sum."),
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
