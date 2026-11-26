"""Write the AP Latin section of /study (python3 -I quizzes/ap_latin/study_rows.py; needs pypdf), then run link_study.py."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from ap_wl.study_rows import write_section  # noqa: E402
from ap_latin.lang import L  # noqa: E402
from ap_latin.content import DOCS  # noqa: E402

BLURB = ("Written for the revised course (CED effective fall 2025): Pliny the Younger&rsquo;s <i>Letters</i> and Vergil&rsquo;s "
         "<i>Aeneid</i>, Teacher&rsquo;s Choice prose and poetry, and the in-class Course Project. Start with Part 0 (the exam, "
         "the five free-response rubrics, the grammar the exam names, style and meter), then read each unit&rsquo;s study guide "
         "before its question set. Each question set follows the exam&rsquo;s formats (a long set, short sight and syllabus sets, "
         "discrete sight questions) and ends with a free-response question, a scoring guide and a model answer. Latin is quoted "
         "without macrons, as on the exam.")
SUBS = {
    "00-exam-playbook-guide": "The revised exam, the five free-response questions and their scoring, the Course Project, the grammar the exam names, style, genre and meter",
    "00-exam-playbook-questions": "Constructions, cases, style, genre and meter, with a 15-segment Translation of Aeneid 1.1–4",
    "01-teachers-choice-prose-guide": "Reading prose at sight, Pliny and the letter, Roman society (patronage, slavery, Arria), participles and the ablative absolute",
    "01-teachers-choice-prose-questions": "Pliny 3.16 (Arria), adapted sight prose and discrete sentences, plus a practice project prose essay on Seneca, Letter 47",
    "02-pliny-vesuvius-guide": "Letters 6.16 and 6.20: the death of Pliny the Elder and the escape from Misenum, section by section; Short Answer kit",
    "02-pliny-vesuvius-questions": "6.16.4–5 and 6.16.10, Pliny 1.6 at sight and discrete sentences, plus a Short Answer on 6.20.14–15",
    "03-pliny-ghosts-trajan-calpurnia-guide": "Letter 7.27 (ghosts), the letters to Trajan on citizenship and aqueducts, the letters to Calpurnia; Translation kit",
    "03-pliny-ghosts-trajan-calpurnia-questions": "7.27.5–6, 6.7.2–3, adapted sight prose and discrete sentences, plus a Translation of 7.27.7",
    "04-aeneid-1-2-guide": "Vergil and Augustus; the proem, the storm and Dido (Book 1); Laocoön and the horse (Book 2); epic devices and scansion",
    "04-aeneid-1-2-questions": "Aeneid 1.88–99, 1.503–506 and 2.268–271, discrete sentences, plus a Short Essay on Laocoön's warning",
    "05-aeneid-4-12-guide": "Dido (Book 4), the Underworld and Rome's mission (Book 6), Latinus, Turnus and Camilla (7, 11), the ending (12)",
    "05-aeneid-4-12-questions": "Aeneid 4.305–316, 6.469–471 and 6.268–272, discrete sentences, plus a Short Answer on 6.847–853",
    "06-course-project-poetry-guide": "Working on the four project passages, elegy, lyric and epigram, building and supporting an interpretation",
    "06-course-project-poetry-questions": "Aeneid 12.940–952, Catullus 5 and 85, discrete sentences, plus a practice project poetry essay on Ovid's Pyramus and Thisbe",
}

if __name__ == "__main__":
    write_section(L, DOCS, "Latin", BLURB, SUBS, before_id="ap-macroeconomics")
