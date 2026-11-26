from ap_wl.model import Doc

STEM = "00-exam-playbook"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Part 0: The Revised Exam and the Reading Toolkit", r"Part 0 \textperiodcentered\ Study Guide",
        abstract=r"""This guide covers the revised AP Latin course and exam described in the College Board's Course and Exam Description (effective fall 2025). The syllabus authors are now Pliny the Younger (\emph{Letters}) and Vergil (\emph{Aeneid}); Caesar is no longer required. The exam runs in Bluebook: 52 multiple-choice questions on sight and syllabus Latin, then five free-response questions, two of them on the four passages of the in-class Course Project, whose two teacher-scored checkpoints add 2\% of the score. This guide sets out each task, how the free-response questions are scored, and the toolkit the exam assumes: the grammar it names, stylistic devices, the epistolary and epic genres, and dactylic hexameter. Read it before the unit guides. Latin texts are quoted without macrons, as on the exam. Check AP Central for any later change.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 12+ \qquad Constructions I still miss: \blank[10em]",
        short="Part 0", sub="The Revised Exam and the Reading Toolkit")

G.sec("The revised exam at a glance")
G.tex(r"""
\begin{compare}{Part}{What you do}{Count, time, weight}
I Multiple choice & 20 discrete questions on short sight Latin (20 words at most); four short sets (3 questions each: sight Pliny, sight Vergil, syllabus Pliny, syllabus Vergil); two long sets (10 questions each: syllabus Pliny, syllabus Vergil) & 52 questions, 65 min, 50\% \\
II Q1 & \textbf{Short Answer}: 6--8 subquestions on a syllabus passage (5--10 lines of Vergil or 50--75 words of Pliny) & about 15 min; 10\% \\
II Q2 & \textbf{Translation}: translate about 35 words of Vergil or 40 of Pliny as literally as possible; 15 scored segments & about 15 min; 10\% \\
II Q3 & \textbf{Short Essay}: Part A comprehension with Latin support; Part B a 3--4 sentence interpretation with a Latin citation & about 25 min; 10\% \\
II Q4, Q5 & \textbf{Project Prose / Poetry Passage Short Essay}: one of the two prose and one of the two poetry Course Project passages; Part A summary, Part B interpretation & about 30 min each; 9\% each \\
Checkpoints & two in-class Course Project tasks scored by the teacher & 2\% \\
\end{compare}

\subsection{The six units}
\begin{terms}
1 & Teacher's Choice: Latin prose \\
2 & Pliny, \emph{Letters} 6.16 and 6.20: the eruption of Vesuvius \\
3 & Pliny, \emph{Letters} 7.27 (ghosts), 10.5--7, 10.37 and 10.90 (to Trajan), 6.4 and 6.7 (to Calpurnia); Teacher's Choice prose \\
4 & Teacher's Choice poetry; \emph{Aeneid} 1.1--33, 88--107, 496--508; 2.40--56, 201--249 \\
5 & \emph{Aeneid} 4.74--89, 165--197, 305--361; 6.450--476, 788--800, 847--853; 7.45--58, 783--792, 803--817; 11.532--594; 12.791--796, 803--812, 818--828, 919--952 \\
6 & The Course Project and Teacher's Choice poetry \\
\end{terms}
""")
G.q("1 Format", r"Which syllabus author was dropped in the revised AP Latin course?",
    "Caesar", [("Vergil", "The Aeneid remains the poetry syllabus."),
               ("Pliny the Younger", "Pliny's Letters are the new prose syllabus."),
               ("No author was dropped", "Caesar's Gallic War is no longer required.")],
    "Pliny replaced Caesar.", "The revised course (fall 2025) pairs Vergil's Aeneid with Pliny's Letters.",
    ["Pliny + Vergil."])
G.q("1 Format", r"How is the Translation question (Q2) scored?",
    "in 15 segments, one point each, for a literal translation", [("holistically, 0--5", "It is scored by segments."),
                                                                  ("by the number of words translated", "Each segment is checked for accuracy."),
                                                                  ("on style and fluency only", "Accuracy to the Latin is what counts.")],
    "15 segments.", "Each segment earns a point if every word in it is rendered accurately in context.",
    ["as literally as possible."])
G.q("1 Format", r"How much of the score comes from the two Course Project essays together?",
    r"18\%", [(r"2\%", "2% is the teacher-scored checkpoints."),
              (r"10\%", "10% is one of Q1--Q3."),
              (r"50\%", "50% is the whole free-response section.")],
    "9% + 9%.", "Q4 and Q5 are 9% each; with the checkpoints, the project is 20%.",
    ["2 × 9 = 18."])

G.sec("Multiple choice: discrete questions, short sets and long sets")
G.tex(r"""
\begin{compare}{Type}{Stimulus}{What it asks}
Discrete (20) & a sight sentence of Pliny, Vergil or other prose or poetry, at most 20 words & meaning of a word or phrase, grammar, translation of the sentence \\
Short sets (4 $\times$ 3) & 20--30 words of prose or 3--4 lines of poetry, sight or syllabus & comprehension, grammar, a stylistic or metrical feature \\
Long sets (2 $\times$ 10) & 75--90 words of Pliny or 10--12 lines of Vergil from the syllabus & translation of phrases, grammar terms, comprehension, scansion, style, context \\
\end{compare}

\textbf{Sight versus syllabus.} Sight passages come from parts of Pliny and Vergil outside the syllabus, or from other authors and topics, often underrepresented in the traditional corpus. Syllabus passages reward having read and understood the required readings closely: you should recognize them.

\begin{trap}
On syllabus sets, do not answer from memory of a translation: answer from the Latin printed. Distractors often match a loose translation but not the grammar of the phrase asked about.
\end{trap}
""")
G.q("2 Sets", r"How long is a long-set Vergil passage?",
    "10--12 lines", [("3--4 lines", "That is a short set."),
                     ("at most 20 words", "That is a discrete question."),
                     ("a whole book", "No.")],
    "Long set = 10–12 lines (poetry) or 75–90 words (prose).", "Long sets are always syllabus passages.",
    ["Long set → syllabus, 10 questions."])

G.sec("Skills and question types")
G.tex(r"""
\begin{compare}{Skill}{Questions sound like}{How to answer}
1.A Meaning of words & What does \emph{rima} mean? & context and the glossary; not English look-alikes \\
1.B Grammar & What is the case and use of \emph{fato}? Which word does \emph{saevae} modify? & name the form, then its function \\
1.C Summary & What does Pliny say about\ldots? What happens in lines 4--6? & translate mentally, then choose the paraphrase \\
1.D Translation & Which is the best translation of\ldots? & match every word: tense, voice, case, number \\
2.A Style and meter & What device appears in\ldots? What is the scansion of\ldots? & name the device and its effect; count feet \\
2.B Context & Whom does \emph{Tydide} refer to? Why does Pliny write to Trajan? & mythology, history, Roman practice \\
3.A, 3.B Interpretation & free response only & a claim + Latin citation + explanation \\
\end{compare}

\begin{trap}
Translation choices differ by one feature: an active verb made passive, a participle read as a main verb, a subjunctive read as indicative. Check verbs first.
\end{trap}
""")
G.q("3 Skills", r"A question asks: ``What is the case and use of \emph{vi} in \emph{vi superum}?'' Which skill does it test?",
    "describing how grammar contributes to meaning", [("summarizing a passage", "It asks about one word's form and function."),
                                                     ("scanning a line", "No meter is involved."),
                                                     ("describing cultural context", "No.")],
    "Case and use → 1.B.", "Grammar questions ask for a form and its function in context.",
    ["vi: ablative of means/cause → 1.B."])
G.q("3 Skills", r"Two translation choices differ only in ``was carrying'' versus ``had carried''. What should you check first?",
    "the tense of the Latin verb", [("the case of the subject", "Subjects do not change tense."),
                                    ("the meter of the line", "Irrelevant to translation choices."),
                                    ("the author's biography", "No.")],
    "Verbs first.", "Imperfect (gerebat) vs. pluperfect (gesserat) decides it.",
    ["tense, voice, mood."])

G.sec("Free response: Short Answer, Translation, Short Essay")
G.tex(r"""
\begin{compare}{Question}{What earns points}{How to work}
Q1 Short Answer (8 points) & one point per subquestion: translate a phrase in context; identify a case or use; identify a referent; scan a line; identify a device; connect to context & answer exactly what is asked, one item only when told ``one and only one'' \\
Q2 Translation (15 points) & one point per segment translated accurately: every word, tense, case and connection & literal English; keep the Latin's structure; translate every word \\
Q3 Short Essay (8 points) & A: comprehension (1), Latin that supports it (1), accurate translation of that Latin (1). B: interpretation (1), Latin citation (2), explanation (2) & cite more than one word; translate or paraphrase it; explain \emph{how} it supports the claim \\
\end{compare}

\begin{keyidea}[How to cite Latin]
Write the Latin and its line number, then translate or paraphrase: ``\emph{nox incubat atra} (line 2), `black night lies upon the sea', shows\ldots'' A single Latin word does not earn the citation point.
\end{keyidea}
""")
G.q("4 Free response", r"In Q3 Part B, which citation can earn credit?",
    "``ponto nox incubat atra'' (line 2), ``black night broods over the sea''", [("``nox'', night", "A single word does not earn the citation point."),
                                                                                   ("``the storm is scary''", "No Latin."),
                                                                                   ("lines 1--14", "A line reference with no Latin or paraphrase is not specific.")],
    "More than one word + translation.", "The citation must give the Latin (or line) and translate or paraphrase it accurately.",
    ["Latin + line + translation."])
G.q("4 Free response", r"A Translation segment reads \emph{iactatus} (``having been tossed''). A student writes ``tossing''. The segment earns",
    "no point, because the voice and tense are wrong", [("the point, because the meaning is close", "Segments require accurate form."),
                                                        ("half a point", "Segments are all-or-nothing."),
                                                        ("two points", "No.")],
    "Perfect passive participle.", "Active ``tossing'' renders a present active participle, not iactatus.",
    ["iactatus = having been tossed."])

G.sec("The Course Project and the project passage essays")
G.tex(r"""
\textbf{The project.} Each summer the AP Latin program releases four authentic passages (two prose, two poetry, about 100--150 words each) in the AP Digital Portfolio, with a title, attribution, introduction, glossary and brief commentary. Classes study them during the year. Two checkpoints, scored by the teacher, make up 2\% of the exam score: a written summary of one passage, and a product or presentation interpreting one passage with evidence.

\textbf{On the exam.} Q4 prints one of the two prose passages and Q5 one of the two poetry passages, without title, attribution, glossary or commentary. Which passages appear is not announced.

\begin{compare}{Part}{Prompt}{Rows (points)}
A (4) & ``In your own words, summarize the passage in 4 to 5 complete sentences.'' & summary sentence (1); beginning, middle, end (1 each) \\
B (7) & a short essay making an interpretation about a main idea, an effect or purpose, or a point of view & interpretation (1); first Latin example with explanation (2); second example (2); stylistic or contextual information (2) \\
\end{compare}
""")
G.q("5 Project", r"What does Part A of a project passage essay ask for?",
    "a 4--5 sentence summary of the whole passage", [("a literal translation of every line", "That is Q2."),
                                                     ("the author's biography", "Attribution is removed on the exam."),
                                                     ("scansion of three lines", "No.")],
    "Summary: sentence + beginning, middle, end.", "Part A has four rows, one for an overall summary sentence and one for each third.",
    ["4 points."])
G.q("5 Project", r"Which information is removed from a project passage on the exam?",
    "the title, attribution, introduction, glossary and commentary", [("the Latin text itself", "The text is printed as studied."),
                                                                      ("the line numbers", "Line numbers help citations."),
                                                                      ("nothing", "Supporting material is removed.")],
    "Know your passages.", "Students must know the passages well enough to read them without supports.",
    ["study all four passages."])

G.sec("Grammar and syntax the exam names")
G.tex(r"""
\begin{compare}{Construction}{Signals}{Example}
Ablative absolute & noun + participle in the ablative, grammatically separate & \emph{magna comitante caterva}, ``with a great crowd accompanying'' \\
Indirect statement & verb of saying/thinking + accusative + infinitive & \emph{creditis avectos hostis?} ``do you believe the enemy has sailed away?'' \\
Purpose clause & \emph{ut / ne} + subjunctive & \emph{ne \ldots\ obteramur}, ``so that we may not be trampled'' \\
Result clause & \emph{tam, ita, adeo} + \emph{ut} + subjunctive & \emph{adeo solutus metu, ut \ldots\ dictaret} \\
Cum clause & \emph{cum} + subjunctive & \emph{cum \ldots\ lacrimae vincerent}, ``when the tears were overcoming her'' \\
Relative clause of characteristic & \emph{erant qui, sunt qui} + subjunctive & \emph{erant qui \ldots\ mortem precarentur} \\
Potential subjunctive & ``you could have\ldots'' & \emph{Audires ululatus feminarum} \\
Passive periphrastic & gerundive + \emph{esse} (necessity) & \emph{agenda erit}, ``will have to be done'' \\
Historical present & present tense in past narration & \emph{poscit soleas, ascendit locum} \\
\end{compare}
""")
G.q("6 Syntax", r"In \emph{magna comitante caterva} (\emph{Aeneid} 2.40), the construction is",
    "an ablative absolute", [("an indirect statement", "No verb of saying or accusative + infinitive."),
                             ("a purpose clause", "No ut + subjunctive."),
                             ("a dative of possession", "The case is ablative.")],
    "Noun + participle, ablative, separate.", "``with a great crowd accompanying (him)''.",
    ["caterva (abl.) + comitante (pres. part., abl.)."])
G.q("6 Syntax", r"\emph{erant qui metu mortis mortem precarentur} (Pliny 6.20.14) is best translated",
    "there were those who prayed for death out of fear of death", [("they were praying to death because of fear", "Misses the relative clause of characteristic."),
                                                                   ("whoever feared death was praying", "Wrong structure."),
                                                                   ("death was feared by those who were praying", "Wrong voice.")],
    "Relative clause of characteristic.", "erant qui + subjunctive: ``there were people of the kind who…''.",
    ["metu mortis = from fear of death."])

G.sec("Style, genre and meter")
G.tex(r"""
\begin{compare}{Device}{Definition}{Example}
anaphora & repetition at the start of clauses & \emph{alii parentes alii liberos alii coniuges} \\
asyndeton & omission of conjunctions & \emph{ferrum stringere, perfodere pectus, extrahere pugionem} \\
chiasmus & ABBA order & \\
synchesis (interlocked order) & ABAB order of adjectives and nouns & \emph{saevae memorem Iunonis ob iram} \\
hyperbaton & separation of words that belong together & \\
tricolon & three parallel units, often growing & \\
apostrophe & address to someone absent & \emph{O Danaum fortissime gentis / Tydide!} \\
simile & comparison with \emph{qualis, ut, velut} & \emph{qualem \ldots\ lunam} (6.453--454) \\
\end{compare}

\textbf{Genres.} \emph{Epistolary}: salutation (\emph{C. Plinius Tacito suo s.}, ``sends greetings''), a purpose stated at once, a personal voice shaped for publication, \emph{Vale} at the end. \emph{Epic}: invocation of the Muse, gods intervening, speeches, similes, a hero bearing a people's destiny.

\textbf{Dactylic hexameter.} Six feet: the first four dactyls (\textendash\ u u) or spondees (\textendash\ \textendash), the fifth usually a dactyl, the sixth two syllables. A vowel is long by nature or by position (before two consonants or x, z); elide a final vowel or vowel + m before a vowel or h.
""")
G.q("7 Meter", r"Which is the pattern of the first four feet of \emph{Arma virumque cano, Troiae qui primus ab oris}? (D = dactyl, S = spondee)",
    "DDSS", [("DSDS", "Foot 2 is a dactyl (rumque ca)."),
             ("SSDD", "Foot 1 Arma vi is a dactyl."),
             ("DDDS", "Foot 3 no Tro is a spondee.")],
    "Ar-ma vi | rum-que ca | no Tro | iae qui.", "Feet 1–2 dactyls, 3–4 spondees, then primus ab (D) and oris.",
    ["– u u | – u u | – – | – – | – u u | – x."])
G.q("7 Style", r"In \emph{saevae memorem Iunonis ob iram}, the adjectives and nouns are arranged",
    "in interlocked order (synchesis): saevae with Iunonis, memorem with iram", [("in chiasmus: saevae with iram, memorem with Iunonis", "Saevae agrees with Iunonis (genitive)."),
                                                                                 ("in simple order with no separation", "They are separated."),
                                                                                 ("as a tricolon", "There are not three parallel units.")],
    "A B A B.", "Saevae (gen.) … Iunonis (gen.); memorem (acc.) … iram (acc.).",
    ["agreement shows the pairs."])

G.sec("A study plan", "A study plan")
G.tex(r"""
\begin{compare}{When}{Do this}{Using}
Fall & Units 1--3: Pliny and Teacher's Choice prose. Read every syllabus letter until you can translate it at sight; drill the constructions in \S6 weekly. & Unit guides 1--3 \\
Winter & Units 4--5: the Aeneid. Scan two lines a day; memorize the outline of each syllabus passage. & Unit guides 4--5 \\
All year & The four project passages: summarize each in 4--5 sentences; prepare one interpretation per passage with two Latin citations. & Part 0 \S5, Unit 6 \\
April--May & Timed sight sets (discrete and short); one full free-response section per week. & this series, AP Classroom \\
\end{compare}
""")

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Part 0: Reading Toolkit Drill", r"Part 0 \textperiodcentered\ Question Set",
        abstract=r"""Eighteen items on the toolkit every task assumes (constructions, cases, translation choices, style, genre and meter), using lines from the syllabus readings, followed by a Translation question (15 points) on \emph{Aeneid} 1.1--4 with the segment-by-segment scoring guide. Latin is quoted from public-domain editions without macrons. Allow about 20 minutes for the drill and 15 for the translation.""",
        scoring=r"Drill: \blank\ / \qtotal \qquad Translation: \blank\ / 15 \qquad Target: 16+ drill and 12+ translation",
        short="Part 0", sub="Reading Toolkit Drill")

Q.sec("Constructions")
Q.q("6 Syntax", r"\emph{creditis avectos hostis?} (\emph{Aeneid} 2.43). The case and use of \emph{hostis} is",
    "accusative, subject of the infinitive in indirect statement", [("nominative, subject of creditis", "The subject of creditis is ``you''."),
                                                                    ("genitive singular, of the enemy", "Here -is is the accusative plural ending."),
                                                                    ("dative, with credo", "Credo takes an indirect statement here.")],
    "Indirect statement.", "avectos (esse) is the infinitive; hostis (= hostes) its subject.",
    ["creditis + acc. + inf."])
Q.q("6 Syntax", r"\emph{ne in via strati comitantium turba in tenebris obteramur} (Pliny 6.20.13) is",
    "a negative purpose clause: ``so that we may not be trampled''", [("a result clause: ``with the result that we were trampled''", "No ita/tam; ne marks purpose."),
                                                                     ("a command: ``do not trample us''", "The verb is passive first person."),
                                                                     ("an indirect question", "No question word.")],
    "ne + subjunctive → purpose.", "Pliny proposes turning aside so as not to be trampled by the crowd in the dark.",
    ["obteramur: present passive subjunctive."])
Q.q("6 Syntax", r"\emph{Audires ululatus feminarum} (Pliny 6.20.14) is best translated",
    "you could have heard the shrieks of women", [("you heard the shrieks of women", "Audires is subjunctive, not indicative."),
                                                  ("the women heard your shrieks", "Feminarum is genitive with ululatus."),
                                                  ("hear the shrieks of women!", "Not an imperative.")],
    "Potential subjunctive.", "Imperfect subjunctive with an indefinite ``you'': ``you could have heard''.",
    ["Audires: 2nd sg. imperfect subjunctive."])
Q.q("6 Syntax", r"\emph{aliqua pars \ldots\ testaceo opere agenda erit} (Pliny 10.37.2) means",
    "some part will have to be done in brickwork", [("some part was done in brickwork", "Erit is future; the gerundive expresses necessity."),
                                                     ("some part is doing brickwork", "Passive and obligation are missed."),
                                                     ("some part will act as brickwork", "Agenda is from ago, to do.")],
    "Passive periphrastic.", "gerundive + esse = obligation: ``must be done''.",
    ["agenda erit = will have to be done."])
Q.q("6 Syntax", r"In \emph{Huic illa ita funus paravit} (Pliny 3.16.4), \emph{Huic} is",
    "dative: ``for him'' (the son)", [("ablative: ``by him''", "Huic is dative."),
                                      ("nominative: ``this woman''", "The subject is illa."),
                                      ("genitive: ``of this one''", "Genitive is huius.")],
    "Dative of advantage.", "Arria prepared the funeral for her son.",
    ["huic = dat. sg. of hic."])
Q.q("6 Syntax", r"\emph{cum diu cohibitae lacrimae vincerent prorumperentque} (Pliny 3.16.5) is best translated",
    "when her tears, long held back, were overcoming her and bursting out", [("because she held back her tears for a long time", "Cohibitae is a participle modifying lacrimae."),
                                                                              ("although the tears had conquered", "Tense and sense are wrong."),
                                                                              ("with the tears that will burst out", "Not future.")],
    "cum + imperfect subjunctive.", "A circumstantial cum clause; cohibitae is a perfect passive participle.",
    ["vincerent, prorumperent: imperfect subjunctive."])

Q.sec("Cases and forms")
Q.q("6 Syntax", r"In \emph{vi superum} (\emph{Aeneid} 1.4), \emph{superum} is",
    "genitive plural: ``of the gods above''", [("accusative singular: ``the god above''", "The -um here is a contracted genitive plural (= superorum)."),
                                               ("nominative neuter: ``the higher thing''", "No."),
                                               ("an adverb: ``above''", "No.")],
    "-um = -orum.", "Poetic genitive plural: deum, superum, virum.",
    ["vi superum = by the force of the gods."])
Q.q("6 Syntax", r"\emph{Tydide!} (\emph{Aeneid} 1.97) is in the vocative because Aeneas",
    "addresses Diomedes, son of Tydeus, directly", [("is speaking about a city", "Tydide is a person."),
                                                    ("is giving a command to the winds", "No."),
                                                    ("is writing a letter", "No.")],
    "Apostrophe → vocative.", "A patronymic in the vocative: ``O son of Tydeus''.",
    ["O … Tydide!"])
Q.q("6 Syntax", r"\emph{poscit soleas, ascendit locum} (Pliny 6.16.5) uses the present tense to narrate past events. This is the",
    "historical present", [("future present", "There is no such term."),
                           ("subjunctive of wish", "The verbs are indicative."),
                           ("perfect tense", "Poscit and ascendit are present.")],
    "Historical present.", "Vividness: the reader watches the elder Pliny act.",
    ["present for past → vividness."])

Q.sec("Style and genre")
Q.q("7 Style", r"\emph{alii parentes alii liberos alii coniuges vocibus requirebant} (Pliny 6.20.14) features",
    "anaphora and tricolon", [("chiasmus", "No ABBA pattern."),
                              ("simile", "No comparison."),
                              ("litotes", "No understatement by negation.")],
    "alii … alii … alii.", "The repeated alii in three parallel units conveys panic and searching.",
    ["three groups, one verb."])
Q.q("7 Style", r"\emph{ferrum stringere, perfodere pectus, extrahere pugionem, porrigere marito} (Pliny 3.16.6) uses",
    "asyndeton, with a series of infinitives that speeds the action", [("polysyndeton", "There are no conjunctions."),
                                                                      ("a golden line", "This is prose."),
                                                                      ("an ablative absolute", "No.")],
    "No conjunctions.", "Asyndeton makes Arria's deed swift and decisive.",
    ["stringere, perfodere, extrahere, porrigere."])
Q.q("7 Style", r"In \emph{O terque quaterque beati} (\emph{Aeneid} 1.94), Aeneas",
    "exclaims that those who died at Troy were blessed many times over", [("prays to three or four gods", "Terque quaterque means thrice and four times."),
                                                                          ("counts the ships lost", "No."),
                                                                          ("blesses Dido", "Dido has not appeared yet.")],
    "Exclamation, hyperbole.", "In the storm, Aeneas envies those who died in battle before their fathers' eyes.",
    ["beati = blessed."])
Q.q("7 Genre", r"In the salutation \emph{C. PLINIUS TACITO SUO S.}, \emph{S.} stands for",
    "salutem (dicit): ``sends greetings''", [("Senator", "No."),
                                            ("Suus, his own", "Suo already appears."),
                                            ("Scripsit, wrote", "No.")],
    "Epistolary formula.", "Letters open with sender (nom.), recipient (dat.) and s. (salutem).",
    ["salutem dicit."])
Q.q("7 Genre", r"Which feature belongs to epic rather than to letters?",
    "an invocation of the Muse", [("a salutation to a named recipient", "That is epistolary."),
                                  ("a closing Vale", "That is epistolary."),
                                  ("a request to an emperor", "Pliny's letters to Trajan.")],
    "Musa, mihi causas memora.", "Epic opens with a theme and an invocation (Aeneid 1.8).",
    ["Muse → epic."])

Q.sec("Meter")
Q.q("7 Meter", r"In \emph{litora, multum ille et terris iactatus et alto}, which elisions occur?",
    "the -um of multum and the -e of ille", [("none", "multum and ille end before vowels."),
                                             ("the -a of litora", "Litora is followed by multum (consonant)."),
                                             ("the -s of terris", "A final -s is not elided.")],
    "mult(um) ill(e) et.", "Final vowels or vowel + m elide before a vowel or h.",
    ["multum ille → mult' ille; ille et → ill' et."])
Q.q("7 Meter", r"Which syllable is long by position?",
    "the first syllable of \\emph{terris}", [("the second syllable of \\emph{litora}", "The o of litora is short and followed by one consonant."),
                                              ("the first syllable of \\emph{virumque}", "The i of vi- is short and followed by a single consonant."),
                                              ("the last syllable of \\emph{cano}", "Final o in cano is long by nature, not position.")],
    "Vowel + two consonants.", "ter-ris: e before rr is long by position.",
    ["rr → long."])
Q.q("7 Meter", r"The fifth foot of a hexameter is usually",
    "a dactyl", [("a spondee", "Spondaic fifth feet are rare and marked."),
                 ("a single long syllable", "No."),
                 ("an anapest", "Not in hexameter.")],
    "– u u in foot 5.", "A spondaic fifth foot (spondeiazon) is rare.",
    ["foot 5: dactyl."])
Q.q("7 Meter", r"How many feet does a dactylic hexameter line have?",
    "six", [("five", "That is a pentameter."),
            ("four", "No."),
            ("eight", "No.")],
    "hexa = six.", "Six feet; the last has two syllables.",
    ["hexameter → 6."])

Q.frq(kind="Translation", head=r"Question 2 \textperiodcentered\ Translation \textperiodcentered\ 15 points \textperiodcentered\ about 15 minutes", mins=15,
      directions=[r"Translate the passage below as literally as possible."],
      sources=[dict(title=r"Vergil, \emph{Aeneid} 1.1--4", paras=[
          r"Arma virumque cano, Troiae qui primus ab oris\\ Italiam, fato profugus, Laviniaque venit\\ litora, multum ille et terris iactatus et alto\\ vi superum saevae memorem Iunonis ob iram;",
          r"\emph{Lavinius, -a, -um}: of Lavinium (a town in Italy) \quad \emph{profugus, -a, -um}: exiled \quad \emph{superum} = \emph{superorum}"])],
      model=[r"I sing of arms and the man who, an exile by fate, first came from the shores of Troy to Italy and the Lavinian shores; he (that man) was much tossed both on lands and on the deep by the force of the gods above, on account of the unforgetting anger of cruel Juno."],
      rows=[("1 Arma virumque", 1, "arms and the man", "omitting -que"),
            ("2 cano", 1, "I sing (of)", "he sings; sang"),
            ("3 Troiae ab oris", 1, "from the shores of Troy", "to the shores"),
            ("4 qui primus", 1, "who first", "the first man (no relative)"),
            ("5 Italiam venit", 1, "came to Italy", "comes; Italy came"),
            ("6 fato profugus", 1, "an exile by fate", "fate exiled (wrong construction)"),
            ("7 Laviniaque litora", 1, "and (to) the Lavinian shores", "Lavinian shores as subject"),
            ("8 multum ille", 1, "he (that man) much / greatly", "omitting ille"),
            ("9 et terris", 1, "both on lands", "to the lands"),
            ("10 iactatus", 1, "having been tossed / was tossed", "tossing (active)"),
            ("11 et alto", 1, "and on the deep (sea)", "high"),
            ("12 vi superum", 1, "by the force (violence) of the gods above", "the gods' violence as subject"),
            ("13 saevae Iunonis", 1, "of cruel (savage) Juno", "cruel anger (wrong agreement)"),
            ("14 memorem iram", 1, "the unforgetting (mindful) anger", "Juno's memory (wrong agreement)"),
            ("15 ob", 1, "on account of / because of", "omitted")],
      tips=["Every word is translated, and each Latin form keeps its function: cano present, iactatus passive participle, superum genitive plural.", "Agreement decides the synchesis: saevae with Iunonis, memorem with iram.",
            "Literal order may stay awkward; accuracy earns the segments."],
      ask="Write your translation, then mark each segment you rendered accurately.", lines=8)

GUIDE, QSET = G, Q
