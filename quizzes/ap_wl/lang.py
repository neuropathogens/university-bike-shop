"""Per-language settings for an AP world language series (one instance in each family's lang.py)."""


class Lang:
    def __init__(self, family, short, course, slug, ask, vocabheads, cjk=False):
        self.family = family          # python package, e.g. "ap_spanish"
        self.short = short            # "AP Spanish", used in quiz titles
        self.course = course          # "AP Spanish Language and Culture"
        self.slug = slug              # "ap-spanish": /study/ap/<slug>/, the /study anchor, the file prefix
        self.prefix = slug + "-"
        self.base = f"/study/ap/{slug}/"
        self.ask = ask                # default instruction under a free-response task
        self.vocabheads = vocabheads  # "{Español}{Uso}{English}": vocab table column heads
        self.cjk = cjk                # Japanese: CJK font switching in the PDFs
