# Hindi / Gujarati for Class 10 Geography Ch 3 lesson.
# Templates use {0}, {1}, ... for the formulas (equations) of the English text, in order.
import re
from tr_ch04_common import by_option, feedback, _ITEMS

_FORMULA = re.compile(r"\$\$[\s\S]+?\$\$|\$[^$]+\$")
P = "geo10ch03"
def fill(english, hi, gu):
    f = _FORMULA.findall(english)
    return hi.format(*f), gu.format(*f)
def fx(iid, field, hi, gu): return fill(_ITEMS[f"{P}.{iid}"][field], hi, gu)
def fb(iid, mapping):
    it = _ITEMS[f"{P}.{iid}"]
    english = dict(zip(it["options"], it["option_feedback"]))
    return feedback(f"{P}.{iid}", {o: fill(english[o], *t) for o, t in mapping.items()})
def opts(iid, mapping): return by_option(f"{P}.{iid}", mapping)
def table(iid, pairs):
    body = _ITEMS[f"{P}.{iid}"]["body"]
    out = []
    for lang in (0, 1):
        b = body
        for en, tr in pairs:
            assert en in b, (iid, en)
            b = b.replace(en, tr[lang])
        out.append(b)
    return tuple(out)
def check_block(iid, q, ex, table_):
    out = {f"{P}.{iid}.question": q, f"{P}.{iid}.explanation": fill(_ITEMS[f"{P}.{iid}"]["explanation"], *ex),
           f"{P}.{iid}.option_feedback": fb(iid, {k: v[1] for k, v in table_.items()})}
    words = {k: v[0] for k, v in table_.items() if v[0] is not None}
    if words: out[f"{P}.{iid}.options"] = opts(iid, words)
    return out
from tr_geo03_lesson_a import META, SECTIONS, TEXT_A
from tr_geo03_lesson_b import TEXT_B
from tr_geo03_checks import OK, SOCRATIC_OPTS, CHECKS
T = {f"{P}.{k}": v for k, v in {**TEXT_A, **TEXT_B}.items()}
for _iid, _m in SOCRATIC_OPTS.items():
    T[f"{P}.{_iid}.options"] = opts(_iid, _m)
for _iid, (_q, _ex, _tab) in CHECKS.items():
    T.update(check_block(_iid, _q, _ex, _tab))
