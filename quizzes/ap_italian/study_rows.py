"""Write the AP Italian section of /study (python3 -I quizzes/ap_italian/study_rows.py; needs pypdf), then run link_study.py."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from ap_wl.study_rows import write_section  # noqa: E402
from ap_italian.lang import L  # noqa: E402
from ap_italian.content import DOCS  # noqa: E402

BLURB = ("Written for the revised course (fall 2026) and its first exam in May 2027: free response first (a course project "
         "presented and discussed in Italian, then an Argumentative Essay with three sources), and 55 multiple-choice questions "
         "in nine task types. Start with Part 0, then read each unit&rsquo;s study guide before its question set. As on the exam, "
         "the question sets are in Italian and draw on Italy, Italian-speaking Switzerland and Italian communities abroad; "
         "listening sets are printed as transcripts, and every set ends with a free-response task, a scoring guide and a model response.")
SUBS = {
    "00-exam-playbook-guide": "Exam format for May 2027, the nine multiple-choice task types, the three free-response rubrics, the project and PPR, and language control",
    "00-exam-playbook-questions": "The congiuntivo, the periodo ipotetico, pronouns, passato prossimo and imperfetto, relative pronouns, the si and connectors, with a full Argumentative Essay; answer key with explanations",
    "01-families-communities-guide": "Grandparents and childcare, leaving home late, the piazza and the passeggiata, the Misericordie and civil service, villages and one-euro houses; Argumentative Essay kit",
    "01-families-communities-questions": "Audio Report, Article and Chart, Promotional Material and Interview sets plus an Argumentative Essay on compulsory civil service",
    "02-language-culture-guide": "The Palio, the Befana and June 2, Italian in Switzerland and abroad, dialects and the history of Italian, false friends and the si; Project Q&A kit",
    "02-language-culture-questions": "Presentation, Literary Text, Article and Audio and Chart sets plus a practice Project Q&A on Neapolitan song",
    "03-art-creativity-guide": "Music (the 2026–27 project lens): opera, the town band, Sanremo, the pizzica and Cremona's violins; Brunelleschi, neorealism and design; Project Presentation kit",
    "03-art-creativity-questions": "Instructional Guidance, Article and Chart, Promotional Material and Interview sets plus a practice Project Presentation on opera in Italy",
    "04-science-technology-guide": "Volta, Marconi, Fermi and the Programma 101, privacy and cash, recycling and energy, the journalistic condizionale and chart language",
    "04-science-technology-questions": "Audio and Chart, Article, Literary Text and Audio Report sets plus an Argumentative Essay on remote work",
    "05-contemporary-life-guide": "The liceo, oral tests and the maturità, breakfast at the bar and Slow Food, August holidays and the Giro, relative clauses with cui and the imperative",
    "05-contemporary-life-questions": "Audio Report, Article and Chart, Promotional Material and Presentation sets plus a practice Project Presentation on the Sanremo festival",
    "06-global-contexts-guide": "Drought, earthquakes and the MOSE, 1861, 1946 and 1957, high-speed rail, ZTLs and Venice's entry fee, proposing solutions; counterargument kit",
    "06-global-contexts-questions": "Interview, Article, Article and Chart and Instructional Guidance sets plus an Argumentative Essay on entry fees for art cities",
}

if __name__ == "__main__":
    write_section(L, DOCS, "Italian Language and Culture", BLURB, SUBS, before_id="ap-macroeconomics")
