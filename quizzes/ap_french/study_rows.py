"""Write the AP French section of /study (python3 -I quizzes/ap_french/study_rows.py; needs pypdf), then run link_study.py."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from ap_wl.study_rows import write_section  # noqa: E402
from ap_french.lang import L  # noqa: E402
from ap_french.content import DOCS  # noqa: E402

BLURB = ("Written for the revised course (fall 2026) and its first exam in May 2027: free response first (a course project "
         "presented and discussed in French, then an Argumentative Essay with three sources), and 55 multiple-choice questions "
         "in nine task types. Start with Part 0, then read each unit&rsquo;s study guide before its question set. As on the exam, "
         "the question sets are in French and draw on the whole French-speaking world; listening sets are printed as transcripts, "
         "and every set ends with a free-response task, a scoring guide and a model response.")
SUBS = {
    "00-exam-playbook-guide": "Exam format for May 2027, the nine multiple-choice task types, the three free-response rubrics, the project and PPR, and language control",
    "00-exam-playbook-questions": "Subjunctive, passé composé and imparfait, si-clauses, pronouns, participle agreement, relative pronouns and connectors, with a full Argumentative Essay; answer key with explanations",
    "01-families-communities-guide": "New family forms and the PACS, associations, the Senegalese teranga, rural France and Quebec villages; Argumentative Essay kit",
    "01-families-communities-questions": "Audio Report, Article and Chart, Promotional Material and Interview sets plus an Argumentative Essay",
    "02-language-culture-guide": "July 14, the Fête de la musique and the galette des rois, la francophonie and Quebec French, verlan and false friends; Project Q&A kit",
    "02-language-culture-questions": "Presentation, Literary Text, Article and Audio and Chart sets plus a practice Project Q&A on zouk",
    "03-art-creativity-guide": "Music (the 2026–27 project lens): chanson, zouk, raï, griots and the kora; Djenné and Notre-Dame; Négritude; Project Presentation kit",
    "03-art-creativity-questions": "Instructional Guidance, Article and Chart, Promotional Material and Interview sets plus a practice Project Presentation on Cajun music",
    "04-science-technology-guide": "Pasteur, Curie, the smart card and Kourou, the right to disconnect, mobile money, probability and chart language",
    "04-science-technology-questions": "Audio and Chart, Article, Literary Text and Audio Report sets plus an Argumentative Essay on social media under 15",
    "05-contemporary-life-guide": "The bac, cégep and apprenticeships, meal times and the Nutri-Score, five weeks of paid holiday, relative clauses and manquer",
    "05-contemporary-life-questions": "Audio Report, Article and Chart, Promotional Material and Presentation sets plus a practice Project Presentation on Quebec song",
    "06-global-contexts-guide": "The Paris Agreement and the Great Green Wall, 1789 and 1960, trams and low-emission zones, proposing solutions; counterargument kit",
    "06-global-contexts-questions": "Interview, Article, Article and Chart and Instructional Guidance sets plus an Argumentative Essay on short-haul flights",
}

if __name__ == "__main__":
    write_section(L, DOCS, "French Language and Culture", BLURB, SUBS, before_id="ap-macroeconomics")
