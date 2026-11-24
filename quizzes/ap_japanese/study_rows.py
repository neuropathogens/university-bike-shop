"""Write the AP Japanese section of /study (python3 -I quizzes/ap_japanese/study_rows.py; needs pypdf), then run link_study.py."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from ap_wl.study_rows import write_section  # noqa: E402
from ap_japanese.lang import L  # noqa: E402
from ap_japanese.content import DOCS  # noqa: E402

BLURB = ("Written for the revised course (fall 2026) and its first exam in May 2027: free response first (a course project "
         "presented and discussed in Japanese, then a Story Narration and an Email Response), and 55 multiple-choice questions "
         "in ten task types. Start with Part 0, then read each unit&rsquo;s study guide before its question set. As on the exam, "
         "questions are in English and sources in Japanese (kanji and kana, no furigana); listening sets are printed as "
         "transcripts, and every set ends with a free-response task, a scoring guide and a model response.")
SUBS = {
    "00-exam-playbook-guide": "Exam format for May 2027, the ten multiple-choice task types, the four free-response rubrics, the project and PPR, register and language control",
    "00-exam-playbook-questions": "Particles, giving and receiving, conditionals, the passive and causative, noun modification, connectors and keigo, with a Story Narration; answer key with explanations",
    "01-families-communities-guide": "In-group and out-group, respect for elders, neighborhood associations and the notice board, depopulation and hometown tax donations; Email Response kit",
    "01-families-communities-questions": "Audio Report, Article and Chart, Correspondence and Conversation sets plus an Email Response about a homestay",
    "02-language-culture-guide": "New Year, Setsubun, Tanabata and Obon, three scripts and made-in-Japan English, dialects, Nikkei communities, keigo and hearsay; Story Narration kit",
    "02-language-culture-questions": "Presentation, Literary Text, Article and Audio and Chart sets plus a Story Narration at a summer festival",
    "03-art-creativity-guide": "Music (the 2026–27 project lens): Japanese instruments, Bon dances, enka, choirs and Vocaloid; Ise and Ryōanji; kabuki, ukiyo-e and kintsugi; Project Presentation kit",
    "03-art-creativity-questions": "Audio and Chart, Conversation, Article and Chart and Correspondence sets plus a practice Project Presentation on taiko",
    "04-science-technology-guide": "The shinkansen, emoji and iPS cells, stickers and read receipts, care robots and earthquake warnings, によって and おかげで; polite Email Response kit",
    "04-science-technology-questions": "Instructional Guidance, Article, Literary Text and Audio Report sets plus an Email Response to a librarian",
    "05-contemporary-life-guide": "The April school year, clubs, cleaning time and school lunch, job hunting, washoku and itadakimasu, hot springs and Kōshien; narrating events in time",
    "05-contemporary-life-questions": "Conversation, Article and Chart, Promotional Material and Presentation sets plus a Story Narration at a culture festival",
    "06-global-contexts-guide": "Disaster drills and preparedness, garbage sorting and mottainai, Hiroshima and the paper cranes, overtourism and coexistence; Project Q&A kit",
    "06-global-contexts-questions": "Presentation, Audio and Chart, Article and Literary Text sets plus a practice Project Q&A on taiko",
}

if __name__ == "__main__":
    write_section(L, DOCS, "Japanese Language and Culture", BLURB, SUBS, before_id="ap-macroeconomics")
