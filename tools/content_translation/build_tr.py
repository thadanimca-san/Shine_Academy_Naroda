"""Assembles tr_<name>_lesson.py and tr_<name>_questions.py from data parts:
   tr_<name>_lesson_a.py / _b.py (TEXT_A, TEXT_B, META, SECTIONS in _a), tr_<name>_checks.py (SOCRATIC_OPTS, CHECKS), tr_<name>_q_body.txt.
Usage: python3 build_tr.py his02 his10ch02 'History Ch 2'"""
import sys
name, P, label = sys.argv[1], sys.argv[2], sys.argv[3]
head = open("tr_sci06_lesson.py").read().splitlines(True)[:32]
head = "".join(head).replace("Class 10 Science Ch 6", f"Class 10 {label}").replace("sci10ch06", P)
lesson = head + f'''from tr_{name}_lesson_a import META, SECTIONS, TEXT_A
from tr_{name}_lesson_b import TEXT_B
from tr_{name}_checks import OK, SOCRATIC_OPTS, CHECKS
T = {{f"{{P}}.{{k}}": v for k, v in {{**TEXT_A, **TEXT_B}}.items()}}
for _iid, _m in SOCRATIC_OPTS.items():
    T[f"{{P}}.{{_iid}}.options"] = opts(_iid, _m)
for _iid, (_q, _ex, _tab) in CHECKS.items():
    T.update(check_block(_iid, _q, _ex, _tab))
'''
open(f"tr_{name}_lesson.py", "w").write(lesson)
qhead = "".join(open("tr_sci06_questions.py").read().splitlines(True)[:42]).replace("Class 10 Science Ch 6", f"Class 10 {label}").replace("sci10ch06", P)
s12 = open("tr_sci12_questions.py").read()
arblock = s12[s12.index("# Assertion-reason"):s12.index("return (a_hi")] + s12[s12.index("return (a_hi"):].split("\n", 1)[0] + "\n"
open(f"tr_{name}_questions.py", "w").write(qhead + arblock + open(f"tr_{name}_q_body.txt").read())
print("built", name)
