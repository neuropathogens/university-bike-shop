"""Write the AP Spanish section of /study (python3 -I quizzes/ap_spanish/study_rows.py; needs pypdf), then run link_study.py."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from ap_wl.study_rows import write_section  # noqa: E402
from ap_spanish.lang import L  # noqa: E402
from ap_spanish.content import DOCS  # noqa: E402

BLURB = ("Written for the revised course (fall 2026) and its first exam in May 2027: free response first (a course project "
         "presented and discussed in Spanish, then an Argumentative Essay with three sources), and 55 multiple-choice questions "
         "in nine task types. Start with Part 0, then read each unit&rsquo;s study guide before its question set. As on the exam, "
         "the question sets are in Spanish; listening sets are printed as transcripts, and every set ends with a free-response "
         "task, a scoring guide and a model response.")
SUBS = {
    "00-exam-playbook-guide": "Exam format for May 2027, the nine multiple-choice task types, the three free-response rubrics, the project and PPR, and language control",
    "00-exam-playbook-questions": "Subjunctive, preterite and imperfect, si-clauses, ser/estar, por/para, pronouns and connectors, with a full Argumentative Essay; answer key with explanations",
    "01-families-communities-guide": "Family and surnames, godparents and the sobremesa, the minga, rural depopulation; Argumentative Essay kit",
    "01-families-communities-questions": "Audio Report, Article and Chart, Promotional Material and Interview sets plus an Argumentative Essay",
    "02-language-culture-guide": "Celebrations, Spanish around the world (voseo, Guaraní, Spanglish), loanwords and false friends, uses of se; Project Q&A kit",
    "02-language-culture-questions": "Presentation, Literary Text, Article and Audio and Chart sets plus a practice Project Q&A on music",
    "03-art-creativity-guide": "Music (the 2026–27 project lens), heritage and architecture, painting and literature, evaluating art; Project Presentation kit",
    "03-art-creativity-questions": "Instructional Guidance, Article and Chart, Promotional Material and Interview sets plus a practice Project Presentation on music",
    "04-science-technology-guide": "Inventions and astronomy, the digital divide, misinformation, predictions and chart language; essay kit for charts",
    "04-science-technology-questions": "Audio and Chart, Article, Literary Text and Audio Report sets plus an Argumentative Essay on AI and homework",
    "05-contemporary-life-guide": "Careers and universities, meal times and mate, food labels, sports and tourism, adjective clauses and commands",
    "05-contemporary-life-questions": "Audio Report, Article and Chart, Promotional Material and Presentation sets plus a practice Project Presentation",
    "06-global-contexts-guide": "Glaciers, water and energy, independence and memory, cable cars and ciclovías, proposing solutions; counterargument kit",
    "06-global-contexts-questions": "Interview, Article, Article and Chart and Instructional Guidance sets plus an Argumentative Essay on car-free centers",
}

if __name__ == "__main__":
    write_section(L, DOCS, "Spanish Language and Culture", BLURB, SUBS, before_id="ap-statistics")
