"""Write the AP Spanish Literature section of /study (python3 -I quizzes/ap_spanish_lit/study_rows.py; needs pypdf), then run link_study.py."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from ap_wl.study_rows import write_section  # noqa: E402
from ap_spanish_lit.lang import L  # noqa: E402
from ap_spanish_lit.content import DOCS  # noqa: E402

BLURB = ("Built on the course's 38 required works, read in the eight chronological units of the Course and Exam Description, "
         "and its six themes. Start with Part 0 (the exam, the scoring guides and the analysis toolkit), then read each "
         "unit&rsquo;s study guide before its question set. As on the exam, the question sets are in Spanish: an audio set "
         "(printed as a transcript), two reading sets, and one of the four free-response tasks with a scoring guide and a model "
         "response. Public-domain works are quoted; works still under copyright are summarized and analyzed, not quoted.")
SUBS = {
    "00-exam-playbook-guide": "The exam, the four free-response rubrics, devices and versification, narrative voice, periods and movements, the Spanish of literary analysis",
    "00-exam-playbook-questions": "Devices, meter and forms, narrators, periods and the language of analysis, with a Text Explanation on the Romance de la pérdida de Alhama",
    "01-medieval-guide": "Al-Andalus and the Reconquista, the Romance de la pérdida de Alhama, El conde Lucanor (Exemplo XXXV), medieval Spanish; Analysis of a Single Text kit",
    "01-medieval-questions": "Romancero presentation, Conde Lucanor and a frontier ballad, plus an Analysis of a Single Text essay on Exemplo XXXV",
    "02-sixteenth-century-guide": "Lazarillo de Tormes, Cortés and Visión de los vencidos, Garcilaso's Soneto XXIII; Text and Art Comparison kit",
    "02-sixteenth-century-questions": "Novelist interview, Lazarillo's Tratado 1 and criticism on Lázaro's irony, plus a Text and Art Comparison on Garcilaso",
    "03-seventeenth-century-guide": "Don Quijote, Góngora, Quevedo, Sor Juana and El burlador de Sevilla; the Baroque; Text Comparison kit",
    "03-seventeenth-century-questions": "Recited poem, Sor Juana's redondillas and Góngora's Soneto CLXVI, plus a Text Comparison on Quevedo's Salmo XVII",
    "04-romantic-realist-naturalist-guide": "Heredia's “En una tempestad”, Bécquer's Rima LIII, Pardo Bazán's “Las medias rojas”; Text Explanation kit",
    "04-romantic-realist-naturalist-questions": "Presentation on Romanticism and Realism, Heredia, a paired set with Bécquer, plus a Text Explanation on “Las medias rojas”",
    "05-generation-98-modernismo-guide": "Martí's “Nuestra América”, Darío's “A Roosevelt”, Machado, San Manuel Bueno, mártir and Quiroga's “El hijo”",
    "05-generation-98-modernismo-questions": "Interview on Unamuno, “A Roosevelt” and “El hijo”, plus an Analysis of a Single Text essay on “Nuestra América”",
    "06-twentieth-century-theater-poetry-guide": "Bernarda Alba and Lorca's “Prendimiento”, Dragún, Neruda, Guillén, Morejón, Burgos and Storni; Text and Art kit",
    "06-twentieth-century-theater-poetry-questions": "Presentation on 20th-century theater, Lorca's ballad and criticism on Afro-Cuban poetry, plus a Text and Art Comparison on Storni and Kahlo",
    "07-boom-guide": "Borges, Cortázar, Fuentes, García Márquez and Rulfo; the fantastic and magical realism; narrative techniques",
    "07-boom-questions": "Presentation on the fantastic, criticism on “La noche boca arriba” and a magical-realist fragment, plus a Text Explanation on “El hijo”",
    "08-contemporary-guide": "Rivera, Ulibarrí, Allende and Montero: Chicano literature, Hispanic New Mexico, the power of words, urban life; Text Comparison kit",
    "08-contemporary-questions": "Interview on Rivera, criticism on “Dos palabras” and a second-person narrative, plus a Text Comparison on “A Roosevelt”",
}

if __name__ == "__main__":
    write_section(L, DOCS, "Spanish Literature and Culture", BLURB, SUBS, before_id="ap-statistics")
