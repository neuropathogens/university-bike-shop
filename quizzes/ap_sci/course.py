"""One AP science course: names, paths and exam facts shared by the PDFs, the quiz pages and /study."""
import importlib
from dataclasses import dataclass


@dataclass
class Course:
    family: str      # "ap_physics_1" (the package under quizzes/)
    slug: str        # "ap-physics-1" (public/study/ap/<slug>/ and the /study section id)
    name: str        # "AP Physics 1: Algebra-Based" (title block)
    short: str       # "AP Physics 1" (running heads, quiz titles)
    prefix: str      # "ap-phys1-" (file names)
    nums: list       # unit numbers, e.g. range(1, 9)
    heading: str     # /study heading, e.g. "Physics 1: Algebra-Based"
    before_id: str   # the /study section the new one goes before
    blurb: str       # /study blurb (HTML)
    pace: float      # exam minutes per multiple-choice question
    tools: str       # abstract sentence: what to keep at hand
    setup: str       # quiz setup note
    exam_mc: str     # "42 multiple-choice questions in 85 minutes" (for abstracts)

    def units(self, nums=None):
        out = []
        for n in nums or self.nums:
            u = importlib.import_module(f"{self.family}.u{n:02d}").UNIT
            u.prefix = self.prefix
            assert u.n == n, (self.family, n)
            out.append(u)
        return out

    @property
    def tex_short(self):
        return self.short.replace("&", "\\&")
