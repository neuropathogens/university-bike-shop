from ap_wl.model import Doc

STEM = "06-course-project-poetry"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 6: The Course Project and Teacher's Choice: Latin Poetry", r"Unit 6 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 6 centers on the Course Project: four authentic passages, two prose and two poetry, released each summer and studied in class, which return on the exam as Questions 4 and 5. This guide sets out a working method for the project, the poetic genres and meters you may meet beyond Vergil (elegy, lyric, epigram, post-classical verse), how to build an interpretation of a main idea, an effect or a point of view, how to cite and explain Latin evidence, and a kit for the Project Poetry Passage Short Essay. The official project passages are released in the AP Digital Portfolio; this series practices with public-domain passages chosen for the purpose. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 9+ \qquad My four project passages: \blank[10em]",
        short="Unit 6", sub="The Course Project and Teacher's Choice: Latin Poetry")

G.sec("Working on the four project passages")
G.tex(r"""
\begin{terms}
Preread & read all four passages with the glossary and commentary; note the speaker, the situation and the shape of each \\
Translate & produce a careful literal translation of each passage, then a fluent one \\
Summarize & write a 4--5 sentence summary (sentence + beginning, middle, end): this is Part A and Checkpoint 1 \\
Interpret & for each passage, prepare one interpretation for each kind of prompt: a main idea, an effect or purpose, a point of view \\
Collect evidence & for each interpretation, two Latin citations of more than one word, with translations \\
Know without supports & on the exam the title, attribution, glossary and commentary are removed: reread until you can read each passage unaided \\
\end{terms}
""")
G.q("1 Project", r"Why should you be able to read each project passage without its glossary?",
    "The exam prints the passage without title, attribution, glossary or commentary.", [("The glossary is wrong.", "No."),
                                                                                         ("Teachers may not use glossaries.", "No."),
                                                                                         ("The passages change on the exam.", "The Latin text is printed as studied.")],
    "Supports removed.", "Q4 and Q5 test passages you have studied, without their supports.",
    ["know the passages cold."])
G.q("1 Project", r"Which checkpoint asks for a written draft summary of one passage?",
    "Checkpoint 1", [("Checkpoint 2", "Checkpoint 2 is an interpretation product or presentation."),
                     ("Question 2", "Q2 is the translation."),
                     ("Question 1", "Q1 is the short answer.")],
    "Checkpoint 1 = summary (2 points).", "Checkpoint 2 = interpretation with evidence (3 points).",
    ["2 + 3 = 5 points, 2% of the score."])

G.sec("Latin poetry beyond Vergil")
G.tex(r"""
\begin{compare}{Genre}{Meter}{Authors and features}
Elegy & elegiac couplet: a hexameter + a pentameter & Ovid, Tibullus, Sulpicia, Propertius; love, loss, the poet's persona \\
Lyric & varied: hendecasyllables, Sapphics, Alcaics & Catullus, Horace; personal voice, friendship, love \\
Epigram & often elegiac couplets & Martial; short, witty, with a final point \\
Narrative epic & dactylic hexameter & Ovid's \emph{Metamorphoses}: stories of transformation \\
Post-classical & classical and accentual meters & medieval hymns, the \emph{Carmina Burana}, Renaissance and Early Modern poets \\
\end{compare}

\textbf{Elegiac couplet.} The pentameter line has two halves of two and a half feet each: \textendash\ u u | \textendash\ u u | \textendash\ \(\|\) \textendash\ u u | \textendash\ u u | \textendash. Couplets usually close a thought, which encourages balance and antithesis.
""")
G.q("2 Poetry", r"What is an elegiac couplet?",
    "a dactylic hexameter followed by a pentameter", [("two hexameters", "No."),
                                                      ("eleven-syllable lines", "Those are hendecasyllables."),
                                                      ("a rhymed pair of lines", "Classical Latin verse does not rhyme.")],
    "hexameter + pentameter.", "The meter of elegy and much epigram.",
    ["Catullus 85: Odi et amo …"])
G.q("2 Poetry", r"Which work is a long narrative poem of transformations in hexameters?",
    "Ovid's \\emph{Metamorphoses}", [("Martial's \\emph{Epigrams}", "Short poems."),
                                       ("Catullus's poems", "Mostly short lyric and elegiac poems."),
                                       ("Pliny's \\emph{Letters}", "Prose.")],
    "Metamorphoses.", "Pyramus and Thisbe is one of its stories (Book 4).",
    ["Ovid, 8 CE."])

G.sec("Building an interpretation")
G.tex(r"""
\begin{compare}{Prompt type (CED)}{Question form}{Example claim}
INT-1 main idea & Describe the relationship / the idea\ldots; explain how the passage expresses it & Pyramus and Thisbe's love grows stronger precisely because it is forbidden. \\
INT-2 effect or purpose & Identify an aspect that creates an effect; explain how & The narrator's apostrophe to the lovers creates sympathy for them. \\
INT-3 point of view & Describe a speaker's attitude; explain how the passage develops it & The narrator admires the lovers' ingenuity and blames the parents. \\
\end{compare}

\begin{keyidea}[A specific, arguable claim]
``The passage is about love'' is a topic, not an interpretation. Make a claim someone could check against the Latin: what the passage shows, how, and why it matters.
\end{keyidea}
""")
G.q("3 Interpretation", r"Which is a strong interpretation for a Part B prompt about Pyramus and Thisbe?",
    "The obstacles placed in the lovers' way only intensify their love, as the narrator stresses with a paradox about hidden fire.", [
        ("The passage is about two people.", "Too general."),
        ("Ovid wrote the Metamorphoses.", "A fact, not an interpretation."),
        ("The wall is made of brick.", "A detail with no claim.")],
    "Specific + checkable.", "The claim names the idea and how it is expressed.",
    ["quoque magis tegitur, tectus magis aestuat ignis."])

G.sec("Citing and explaining Latin evidence")
G.tex(r"""
\begin{compare}{Row}{What earns full credit}{Model}
Latin citation & more than one word, accurate, with line number and translation or accurate paraphrase & ``quoque magis tegitur, tectus magis aestuat ignis'' (line 10), ``the more it is covered, the more the covered fire burns'' \\
Explanation & how this evidence supports the claim & the paradox shows that concealment strengthens their love \\
Second example & a different citation, also explained & ``quid non sentit amor?'' (line 14) \\
Style or context & a device or fact, explained in relation to the claim & apostrophe (``primi vidistis amantes''); Babylon and Semiramis as an exotic setting \\
\end{compare}
""")
G.q("4 Evidence", r"Which citation would earn credit?",
    "``vetuere patres'' (line 7), ``the fathers forbade it''", [("``amor''", "A single word."),
                                                                  ("lines 1--16", "A whole passage is not a specific citation."),
                                                                  ("``the parents were strict''", "No Latin or line reference.")],
    "Latin + line + translation.", "Specific, accurate and translated.",
    ["more than one word."])

G.sec("Task kit: the Project Poetry Passage Short Essay")
G.tex(r"""
\begin{terms}
0--3 min & read the passage twice; recall your prepared summary and interpretations \\
3--10 min & Part A: summary sentence; then beginning, middle, end, each in a sentence \\
10--27 min & Part B: one claim; two cited and explained examples; one style or context point tied to the claim \\
27--30 min & check that every citation has a line number and a translation \\
\end{terms}

\begin{trap}
A Part B that retells the passage earns only what it accidentally argues. Lead with the claim, and make every sentence after it support the claim.
\end{trap}
""")
G.q("5 Essay", r"How many points does Part B of a project passage essay carry?",
    "7", [("4", "That is Part A."),
          ("11", "That is the whole question."),
          ("15", "That is the Translation question.")],
    "1 + 2 + 2 + 2.", "Interpretation, two examples, style or context.",
    ["Part B = 7."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 6: The Course Project and Teacher's Choice: Latin Poetry: Question Set", r"Unit 6 \textperiodcentered\ Question Set",
        abstract=r"""Three sets and four discrete questions in the exam's formats: a long set on \emph{Aeneid} 12.940--952 (the death of Turnus), two short sight sets on Catullus 5.1--3 and 85, and four discrete sight sentences, followed by a practice Project Poetry Passage Short Essay (11 points) on Ovid, \emph{Metamorphoses} 4.55--70 (Pyramus and Thisbe), with the scoring guide and a model response. The Ovid passage is a practice passage, not one of the official Course Project passages. Questions are in English, as on the exam; Latin is quoted without macrons. Allow about 25 minutes for the multiple choice and 30 for the essay.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Essay: \blank\ / 11 \qquad Target: 15+ MCQ and 8+ essay",
        short="Unit 6", sub="The Course Project and Teacher's Choice: Latin Poetry")

Q.sec("Long set: Aeneid 12.940-952")
Q.src(r"Long set (syllabus poetry) \textperiodcentered\ Vergil, \emph{Aeneid} 12.940--952", [
    r"et iam iamque magis cunctantem flectere sermo\\ coeperat, infelix umero cum apparuit alto\\ balteus et notis fulserunt cingula bullis\\ Pallantis pueri, victum quem vulnere Turnus\\ straverat atque umeris inimicum insigne gerebat.\\ ille, oculis postquam saevi monimenta doloris\\ exuviasque hausit, furiis accensus et ira\\ terribilis: `tune hinc spoliis indute meorum\\ eripiare mihi? Pallas te hoc vulnere, Pallas\\ immolat et poenam scelerato ex sanguine sumit.'\\ hoc dicens ferrum adverso sub pectore condit\\ fervidus; ast illi solvuntur frigore membra\\ vitaque cum gemitu fugit indignata sub umbras.",
], 10, note="cunctor, -ari: to hesitate. balteus, -i, m.: sword belt. bulla, -ae, f.: stud. Pallas, -antis, m.: young ally of Aeneas killed by Turnus. exuviae, -arum, f. pl.: spoils. immolo, -are: to sacrifice.")
Q.q("1.C Summary", r"In lines 1--2, what was Turnus's speech beginning to do?",
    "to sway Aeneas, who was hesitating", [("to anger Aeneas further", "Flectere = to bend, persuade."),
                                           ("to call his soldiers", "No."),
                                           ("to pray to Jupiter", "No.")],
    "cunctantem flectere sermo coeperat.", "Aeneas hesitates; Turnus's plea is working.",
    ["cunctantem = Aeneas."])
Q.q("1.B Grammar", r"In line 2, \emph{cum apparuit} is",
    "an inverted cum clause: ``when suddenly (the belt) appeared''", [("a causal cum clause with the subjunctive", "Apparuit is indicative."),
                                                                     ("a concessive clause", "No."),
                                                                     ("a preposition with the ablative", "Here cum is a conjunction.")],
    "cum inversum + indicative.", "The main event comes in the cum clause.",
    ["iam … coeperat, … cum apparuit."])
Q.q("1.C Summary", r"Whose belt does Aeneas see on Turnus's shoulder?",
    "the belt of young Pallas, whom Turnus had killed", [("Turnus's own father's belt", "No."),
                                                         ("Aeneas's belt", "No."),
                                                         ("Camilla's belt", "No.")],
    "balteus … Pallantis pueri.", "Turnus wore it as a hostile trophy.",
    ["victum quem vulnere Turnus straverat."])
Q.q("1.D Translation", r"\emph{victum quem vulnere Turnus / straverat} (lines 4--5) is best translated",
    "whom Turnus had laid low, defeated by a wound", [("who had laid Turnus low with a wound", "Turnus is the subject."),
                                                      ("whom Turnus will defeat with a wound", "Pluperfect."),
                                                      ("the wound by which Turnus was defeated", "No.")],
    "quem → Pallas.", "victum agrees with quem.",
    ["straverat: pluperfect."])
Q.q("1.C Summary", r"Who is \emph{ille} in line 6?",
    "Aeneas", [("Turnus", "Turnus is the one addressed."),
               ("Pallas", "Pallas is dead."),
               ("Jupiter", "No.")],
    "ille = Aeneas.", "He drinks in the sight of the spoils.",
    ["ille … hausit … terribilis."])
Q.q("1.D Translation", r"\emph{furiis accensus et ira / terribilis} is best translated",
    "inflamed by fury and terrible in his anger", [("he set fire to the Furies", "Accensus is passive."),
                                                   ("terrified by the anger of the Furies", "No."),
                                                   ("calm and without anger", "The opposite.")],
    "Ablatives of cause.", "Furor overcomes pietas.",
    ["accensus (PPP)."])
Q.q("1.B Grammar", r"\emph{eripiare} (line 9) is",
    "present passive subjunctive, second person singular (= eripiaris)", [("present active infinitive", "Eripere would be the infinitive."),
                                                                          ("imperative", "No."),
                                                                          ("future indicative", "No.")],
    "-re = -ris.", "Deliberative/indignant question: ``are you to be snatched from me?''",
    ["tune … eripiare mihi?"])
Q.q("2.A Style", r"In \emph{Pallas te hoc vulnere, Pallas / immolat}, the repetition of \emph{Pallas}",
    "emphasizes that the killing is vengeance for Pallas", [("shows that Pallas is still alive", "He is dead; the name is invoked."),
                                                           ("is a simile", "No comparison."),
                                                           ("forms a chiasmus", "Not an ABBA pattern.")],
    "Repetition (epanalepsis) + sacrificial verb.", "Aeneas presents the blow as Pallas's sacrifice of Turnus.",
    ["Pallas … Pallas immolat."])
Q.q("2.A Style", r"\emph{ast illi solvuntur frigore membra} (line 12) echoes \emph{Aeneae solvuntur frigore membra} in Book 1. The effect is to",
    "frame the poem: Aeneas's first appearance and Turnus's death share the same words", [("show that Aeneas dies at the end", "Illi refers to Turnus."),
                                                                                          ("repeat a scansion error", "No."),
                                                                                          ("introduce a new storm", "No.")],
    "Ring composition.", "The echo links the hero's fear at the start to the enemy's death at the end.",
    ["1.92 / 12.951."])
Q.q("2.A Meter", r"What is the pattern of the first four feet of \emph{vitaque cum gemitu fugit indignata sub umbras}?",
    "DDDS", [("DDSS", "Foot 3 (tu fugit) is a dactyl."),
             ("SDDS", "Foot 1 (vitaque) is a dactyl."),
             ("DSDS", "Foot 2 (cum gemi) is a dactyl.")],
    "vitaque | cum gemi | tu fugit | in dig | nata sub | umbras.", "Foot 4 in-dig: both long by position.",
    ["– u u | – u u | – u u | – – | – u u | – –."])

Q.sec("Short set: sight poetry")
Q.src(r"Short set (sight poetry) \textperiodcentered\ Catullus 5.1--3", [
    r"Vivamus, mea Lesbia, atque amemus,\\ rumoresque senum severiorum\\ omnes unius aestimemus assis!",
], 3, note="severus, -a, -um: strict. as, assis, m.: a coin of little value.")
Q.q("1.B Grammar", r"\emph{Vivamus \ldots\ amemus} are",
    "hortatory subjunctives: ``let us live, let us love''", [("future indicatives: ``we will live''", "The -amus/-emus forms here are subjunctive."),
                                                             ("imperatives: ``live, love''", "Imperatives would be vive, ama."),
                                                             ("perfect indicatives", "No.")],
    "Hortatory subjunctive.", "First person plural subjunctive: ``let us…''.",
    ["vivamus, amemus, aestimemus."])
Q.q("1.C Summary", r"How does the speaker want to value the gossip of strict old men?",
    "as worth a single penny", [("as very wise advice", "The opposite."),
                                ("as a reason to stop loving", "No."),
                                ("as a song to remember", "No.")],
    "unius … assis.", "Genitive of value: at one as.",
    ["aestimemus assis."])
Q.q("2.A Style", r"What is the tone of these lines?",
    "joyful defiance of disapproving elders", [("fearful obedience", "The opposite."),
                                               ("formal mourning", "No."),
                                               ("bitter regret", "Not here.")],
    "Defiant celebration.", "Love against social censure.",
    ["rumores … assis!"])

Q.sec("Short set: sight poetry")
Q.src(r"Short set (sight poetry) \textperiodcentered\ Catullus 85", [
    r"Odi et amo. quare id faciam, fortasse requiris?\\ nescio, sed fieri sentio et excrucior.",
], 3, note="requiro, -ere: to ask. excrucio, -are: to torture.")
Q.q("2.A Style", r"\emph{Odi et amo} is built on",
    "antithesis", [("anaphora", "No repetition."),
                   ("simile", "No comparison."),
                   ("hyperbaton", "No separation.")],
    "Opposites joined.", "Hate and love at once.",
    ["odi / amo."])
Q.q("1.D Translation", r"\emph{fieri sentio et excrucior} is best translated",
    "I feel it happening and I am tortured", [("I feel it was done and I torture myself", "Fieri is present; excrucior is passive."),
                                               ("I torture you and feel nothing", "No."),
                                               ("it will happen and torture me", "No.")],
    "fieri = to happen.", "excrucior: present passive.",
    ["sentio + inf."])
Q.q("2.A Meter", r"In what meter is this poem written?",
    "an elegiac couplet", [("two dactylic hexameters", "The second line is a pentameter."),
                           ("hendecasyllables", "That is Catullus 5."),
                           ("iambic trimeter", "No.")],
    "hexameter + pentameter.", "Two lines, one couplet.",
    ["nescio, sed fieri sentio et excrucior: pentameter."])

Q.sec("Discrete sight questions")
Q.q("1.D Translation", r"\emph{Poeta, qui multa carmina scripserat, a populo laudabatur.} This sentence means",
    "The poet, who had written many poems, was praised by the people.", [("The poet praised the people who had written many poems.", "Laudabatur is passive."),
                                                                          ("The people, who had written many poems, praised the poet.", "Qui refers to poeta."),
                                                                          ("The poet will write many poems for the people.", "Tenses wrong.")],
    "Relative clause + passive.", "a populo: ablative of agent.",
    ["laudabatur = was being praised."])
Q.q("1.B Grammar", r"In \emph{Amor vincit omnia}, \emph{omnia} is",
    "accusative plural neuter, object of vincit", [("nominative singular feminine", "Omnia is neuter plural."),
                                                  ("ablative plural", "No."),
                                                  ("genitive plural", "That is omnium.")],
    "omnia (n. pl. acc.).", "Love conquers all things (after Vergil, Eclogue 10.69: omnia vincit Amor).",
    ["amor (subject) vincit omnia (object)."])
Q.q("1.A Meaning", r"In \emph{Puella, lacrimis effusis, abiit}, \emph{lacrimis effusis} means",
    "her tears having been shed", [("with happy laughter", "Lacrimae = tears."),
                                   ("having poured wine", "No."),
                                   ("the tears she will shed", "Perfect passive participle.")],
    "Ablative absolute.", "effundo → effusus.",
    ["lacrimis (abl. pl.)."])
Q.q("1.D Translation", r"\emph{Dum spiro, spero.} This sentence means",
    "While I breathe, I hope.", [("While I hope, I breathe.", "The clauses are reversed."),
                                 ("I breathed until I hoped.", "Present tense."),
                                 ("Breathe and hope!", "Indicatives, not imperatives.")],
    "dum + present.", "A traditional motto.",
    ["spiro = I breathe; spero = I hope."])

Q.frq(kind="Project Poetry Passage Short Essay", head=r"Question 5 \textperiodcentered\ Project Poetry Passage Short Essay (practice passage) \textperiodcentered\ 11 points \textperiodcentered\ about 30 minutes", mins=30,
      directions=[r"This is a practice passage in the format of the Course Project questions. On the exam, the passage is one of your two poetry project passages, printed without title, attribution, glossary or commentary. Read the passage, then answer Parts A and B in English."],
      sources=[dict(title=r"Ovid, \emph{Metamorphoses} 4.55--70", paras=[
          r"Pyramus et Thisbe, iuvenum pulcherrimus alter,\\ altera, quas Oriens habuit, praelata puellis,\\ contiguas tenuere domos, ubi dicitur altam\\ coctilibus muris cinxisse Semiramis urbem.\\ notitiam primosque gradus vicinia fecit,\\ tempore crevit amor; taedae quoque iure coissent,\\ sed vetuere patres: quod non potuere vetare,\\ ex aequo captis ardebant mentibus ambo.\\ conscius omnis abest; nutu signisque loquuntur,\\ quoque magis tegitur, tectus magis aestuat ignis.\\ fissus erat tenui rima, quam duxerat olim,\\ cum fieret, paries domui communis utrique.\\ id vitium nulli per saecula longa notatum ---\\ quid non sentit amor? --- primi vidistis amantes\\ et vocis fecistis iter, tutaeque per illud\\ murmure blanditiae minimo transire solebant."])],
      prompt=[r"\textbf{Part A.} In your own words, summarize the passage in 4 to 5 complete sentences. Provide a summary sentence that identifies what the passage as a whole is about, and address the beginning, middle and end.",
              r"\textbf{Part B.} Describe how the passage presents the effect of the obstacles on the lovers. Explain how the passage develops this. Support your interpretation with at least two specific Latin citations (Latin, or line references, with a translation or accurate paraphrase) and with a stylistic or contextual feature of the text."],
      model=[r"\textbf{Part A.} The passage tells how two young neighbors in Babylon fell in love despite their fathers' opposition and found a way to talk through a crack in their shared wall. Pyramus and Thisbe, the most beautiful youth and girl of the East, lived in adjoining houses in the city that Semiramis surrounded with brick walls. Their nearness led to acquaintance and love, and they would have married, but their fathers forbade it; still, they burned with equal passion, speaking only by nods and signs. Finally, they discovered a thin crack in the wall between their houses, unnoticed for ages, and used it as a path for their voices, whispering endearments through it.",
             r"\textbf{Part B.} The passage shows that every obstacle placed in the lovers' way only makes their love stronger and more inventive. When the fathers forbid marriage (``sed vetuere patres'', line 7, ``but the fathers forbade it''), Ovid answers at once that what they could not forbid was that both burned with captured minds (``quod non potuere vetare, / ex aequo captis ardebant mentibus ambo'', lines 7--8): the prohibition cannot reach their feelings. The paradox ``quoque magis tegitur, tectus magis aestuat ignis'' (line 10), ``the more it is covered, the more the covered fire seethes'', turns secrecy itself into fuel, so concealment intensifies the passion. Stylistically, the narrator's apostrophe to the lovers (``primi vidistis amantes'', line 14, ``you lovers were the first to see it'') and the rhetorical question ``quid non sentit amor?'' (``what does love not notice?'') present their discovery of the crack as a triumph of love's ingenuity over the wall that divides them, inviting the reader's sympathy."],
      rows=[("A1 Summary sentence", 1, "identifies what the whole passage is about (forbidden love that finds a way through the wall)", "a sentence on one detail"),
            ("A2 Beginning", 1, "the lovers, their beauty, neighboring houses in Babylon", "omitting or misreading"),
            ("A3 Middle", 1, "love grows, marriage forbidden by the fathers, secret signs", "omitting or misreading"),
            ("A4 End", 1, "the crack in the wall, used for whispered words", "omitting or misreading"),
            ("B1 Interpretation", 1, "a specific claim about the effect of the obstacles (love grows stronger, more inventive)", "restating the prompt"),
            ("B2 First example", 2, "a citation of more than one word, translated, explained (e.g., the fathers' prohibition and what they could not forbid)", "a single word; no explanation"),
            ("B3 Second example", 2, "a different citation, translated and explained (e.g., the hidden fire)", "repeating the first"),
            ("B4 Style or context", 2, "a device (paradox, apostrophe, rhetorical question, metaphor of fire) or context (Babylon, Semiramis) explained in relation to the claim", "naming a device with no link")],
      tips=["Part A follows the passage in order, with an overall sentence first.", "Part B leads with the claim and gives two translated citations, each explained.",
            "The style point (apostrophe and question) is connected to the claim, not just named."],
      ask="Write Part A and Part B in English, then mark each row.", lines=22)

GUIDE, QSET = G, Q
