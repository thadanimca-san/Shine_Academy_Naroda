"""Builds Hindi/Gujarati option lists in the stored (rotated) option order.
Reads the chapter folder given to apply_translations.py."""
import json, sys
from common_translations import is_math_only

_FOLDER = sys.argv[1]
_ITEMS = {}
_chapter = json.load(open(f"{_FOLDER}/chapter.json", encoding="utf-8"))
for _s in _chapter["sections"]:
    for _b in _s["blocks"]:
        _ITEMS[_b["id"]] = _b
for _q in json.load(open(f"{_FOLDER}/questions.json", encoding="utf-8"))["questions"]:
    _ITEMS[_q["id"]] = _q


def _pick(item_id, mapping, passthrough):
    hi, gu = [], []
    for option in _ITEMS[item_id]["options"]:
        if option in mapping:
            h, g = mapping[option]
        elif passthrough and is_math_only(option):
            h = g = option
        else:
            raise KeyError(f"{item_id}: no translation for option {option!r}")
        hi.append(h); gu.append(g)
    return hi, gu


def by_option(item_id, mapping):
    """Translated options; maths-only options are copied."""
    return _pick(item_id, mapping, True)


def feedback(item_id, mapping):
    """Translated option_feedback, keyed by the English option text."""
    return _pick(item_id, mapping, False)


def steps(item_id, overrides, field="answer_steps"):
    """Full translated list: given entries by index, the rest auto-translated
    (maths-only text or a shared template). Raises if anything is left."""
    from common_translations import by_template
    hi, gu = [], []
    for i, english in enumerate(_ITEMS[item_id][field]):
        if i in overrides:
            h, g = overrides[i]
        elif is_math_only(english):
            h = g = english
        else:
            h, g = by_template(english, "hi"), by_template(english, "gu")
            if h is None:
                raise KeyError(f"{item_id}.{field}[{i}] needs a translation: {english!r}")
        hi.append(h); gu.append(g)
    return hi, gu
