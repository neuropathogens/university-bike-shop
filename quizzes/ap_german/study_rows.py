"""Write the AP German section of /study (python3 -I quizzes/ap_german/study_rows.py; needs pypdf), then run link_study.py."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from ap_wl.study_rows import write_section  # noqa: E402
from ap_german.lang import L  # noqa: E402
from ap_german.content import DOCS  # noqa: E402

BLURB = ("Written for the revised course (fall 2026) and its first exam in May 2027: free response first (a course project "
         "presented and discussed in German, then an Argumentative Essay with three sources), and 55 multiple-choice questions "
         "in nine task types. Start with Part 0, then read each unit&rsquo;s study guide before its question set. As on the exam, "
         "the question sets are in German and draw on Germany, Austria, Switzerland and the rest of the German-speaking world; "
         "listening sets are printed as transcripts, and every set ends with a free-response task, a scoring guide and a model response.")
SUBS = {
    "00-exam-playbook-guide": "Exam format for May 2027, the nine multiple-choice task types, the three free-response rubrics, the project and PPR, and language control",
    "00-exam-playbook-questions": "Word order, Konjunktiv II, cases and prepositions, Perfekt and Präteritum, relative clauses, the passive and connectors, with a full Argumentative Essay; answer key with explanations",
    "01-families-communities-guide": "Parental leave and Kita, Vereine and the volunteer fire brigade, multigenerational houses, Swiss local democracy and rural flight; Argumentative Essay kit",
    "01-families-communities-questions": "Audio Report, Article and Chart, Promotional Material and Interview sets plus an Argumentative Essay on city and village life",
    "02-language-culture-guide": "Karneval, Sankt Martin and the Christmas market, German across seven countries, Swiss German, compounds, anglicisms and false friends; Project Q&A kit",
    "02-language-culture-questions": "Presentation, Literary Text, Article and Audio and Chart sets plus a practice Project Q&A on Berlin techno",
    "03-art-creativity-guide": "Music (the 2026–27 project lens): Bach to Beethoven, brass bands and yodeling, Kraftwerk and techno; the Kölner Dom and the Bauhaus; Goethe to Kafka; Project Presentation kit",
    "03-art-creativity-questions": "Instructional Guidance, Article and Chart, Promotional Material and Interview sets plus a practice Project Presentation on Vienna's music culture",
    "04-science-technology-guide": "Gutenberg, Röntgen and Zuse, privacy and cash, the bottle deposit and the energy transition, the passive with modals and chart language",
    "04-science-technology-questions": "Audio and Chart, Article, Literary Text and Audio Report sets plus an Argumentative Essay on abolishing cash",
    "05-contemporary-life-guide": "The Abitur and dual vocational training, Abendbrot and the Viennese coffeehouse, Sunday rest and allotment gardens, relative clauses with prepositions",
    "05-contemporary-life-questions": "Audio Report, Article and Chart, Promotional Material and Presentation sets plus a practice Project Presentation on music and German division",
    "06-global-contexts-guide": "The energy transition and Alpine glaciers, 1989 and 1990, Stolpersteine, the Deutschlandticket and the Gotthard tunnel, proposing solutions; counterargument kit",
    "06-global-contexts-questions": "Interview, Article, Article and Chart and Instructional Guidance sets plus an Argumentative Essay on an Autobahn speed limit",
}

if __name__ == "__main__":
    write_section(L, DOCS, "German Language and Culture", BLURB, SUBS, before_id="ap-macroeconomics")
