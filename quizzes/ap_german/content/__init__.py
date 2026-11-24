"""The AP German series, in reading order: Part 0, then Units 1-6, each a study guide and a question set."""
import importlib

UNITS = ["p00", "p01", "p02", "p03", "p04", "p05", "p06"]
DOCS = []
for _m in UNITS:
    try:
        _mod = importlib.import_module(f"ap_german.content.{_m}")
    except ModuleNotFoundError as e:
        if e.name != f"ap_german.content.{_m}":
            raise
        continue
    DOCS += [_mod.GUIDE, _mod.QSET]
