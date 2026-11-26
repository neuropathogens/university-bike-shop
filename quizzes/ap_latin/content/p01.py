from ap_wl.model import Doc

STEM = "01-teachers-choice-prose"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 1: Teacher's Choice: Latin Prose", r"Unit 1 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 1 has no syllabus text: teachers choose about 1,650 words of Latin prose across the course to rebuild reading fluency and to introduce the world of Pliny's \emph{Letters}. This guide gives a method for reading Latin prose at sight, an introduction to Pliny and the letter as a genre, Roman social contexts that recur in prose passages (patrons and clients, slaves and freed people, women's voices, Stoic ideals), the constructions that most often decide sight questions, and a kit for the Project Prose Passage Short Essay. Latin is quoted from public-domain texts without macrons. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 9+ \qquad Constructions I still miss: \blank[10em]",
        short="Unit 1", sub="Teacher's Choice: Latin Prose")

G.sec("Reading Latin prose at sight")
G.tex(r"""
\begin{terms}
1 Read the whole sentence & before translating anything; note punctuation and the main verb(s) \\
2 Find the core & subject (nominative), verb, object; then attach the rest \\
3 Group words by agreement & adjectives and participles with their nouns, even when separated \\
4 Mark subordinate clauses & cum, ut, ne, quod, qui/quae/quod, si: bracket each one \\
5 Use the glossary & it is part of the passage; unglossed words are on the required vocabulary list \\
6 Paraphrase, then choose & for comprehension questions, predict the answer before reading the choices \\
\end{terms}

\begin{trap}
Latin word order is flexible: the first noun is not necessarily the subject. \emph{Huic illa ita funus paravit}: \emph{illa} (nom.) is the subject, \emph{huic} (dat.) is ``for him''.
\end{trap}
""")
G.q("1 Reading", r"What should you look for first in a long Latin sentence?",
    "the main verb and its subject", [("the longest word", "Length does not reveal structure."),
                                      ("the first noun, which is always the subject", "Word order is flexible."),
                                      ("every adjective", "Adjectives attach to nouns after the core is found.")],
    "Core first.", "Subject and main verb give the frame for everything else.",
    ["verb → subject → object → modifiers."])
G.q("1 Reading", r"In \emph{Huic illa ita funus paravit}, which word is the subject?",
    "illa", [("huic", "Huic is dative."),
             ("funus", "Funus is the object (neuter accusative)."),
             ("ita", "Ita is an adverb.")],
    "illa (nom. sg. fem.).", "The case ending, not the position, identifies the subject.",
    ["she prepared the funeral for him."])

G.sec("Pliny the Younger and the letter as literature")
G.tex(r"""
\begin{compare}{Fact}{Detail}{Why it matters}
Life & c. 61--c. 113 CE; nephew and adopted son of Pliny the Elder; senator, consul in 100 CE; governor of Bithynia-Pontus c. 110--112 & a voice from the elite of Trajan's Rome \\
The collection & nine books of letters to friends, published by Pliny himself, and a tenth book of correspondence with Trajan & letters shaped for readers, not just for one recipient \\
Style & elegant, balanced sentences; variety; vivid detail; a carefully crafted self-portrait & the ``epistolary genre'' \\
\end{compare}

\textbf{Features of a letter.} A salutation (sender in the nominative, recipient in the dative, \emph{s.} = \emph{salutem}); a single topic announced at once; a personal, conversational tone; a closing such as \emph{Vale}. Pliny also writes \emph{to be remembered}: many letters praise exemplary people and invite posterity to remember them.
""")
G.q("2 Pliny", r"Which statement about Pliny's letters is accurate?",
    "Pliny published his own letters, shaping them for a wider audience.", [("They were private and never meant to be read by others.", "He selected and published them."),
                                                                             ("They were all written to Trajan.", "Only Book 10 is to Trajan."),
                                                                             ("They are in verse.", "They are prose.")],
    "Letters as literature.", "Books 1–9 were published by Pliny; Book 10 contains his official correspondence.",
    ["published collection."])
G.q("2 Pliny", r"What is the relationship between Pliny the Younger and Pliny the Elder?",
    "The Elder was his uncle, who adopted him.", [("The Elder was his son.", "No."),
                                                  ("They were unrelated rivals.", "No."),
                                                  ("The Elder was his teacher only.", "He was his uncle and adoptive father.")],
    "avunculus.", "Pliny calls him avunculus meus in 6.16.",
    ["avunculi mei exitum."])

G.sec("Roman society in prose passages")
G.tex(r"""
\begin{compare}{Topic}{Key terms}{Example}
Patronage & patronus, cliens, beneficium, gratia & Pliny asks Trajan for favors for his doctor (Unit 3) \\
Slavery and freedom & servus, libertus, manumissio, dominus & Seneca, \emph{Epistulae} 47: ``Servi sunt.'' Immo homines. \\
Women's voices & matrona, uxor, exemplum & Arria: ``Paete, non dolet'' (Pliny 3.16) \\
Stoicism & virtus, constantia, animus, fortuna & calm before death; equality of souls \\
\end{compare}

\textbf{Arria (Pliny 3.16).} When her son died while her husband Caecina Paetus was gravely ill, Arria hid her grief, telling her husband the boy had slept well and eaten; later, when Paetus was condemned, she stabbed herself first and handed him the dagger: ``Paete, non dolet'' (``Paetus, it does not hurt''). Pliny uses her as an \emph{exemplum} of courage that did not seek glory.
""")
G.q("3 Society", r"What does Arria's ``Paete, non dolet'' show in Pliny's account?",
    "her courage and her support for her husband facing death", [("that she felt no grief for her son", "She hid her grief, which is different."),
                                                                 ("that she was a doctor", "No."),
                                                                 ("that Paetus was not ill", "He was."),],
    "Exemplum of virtus.", "Her words encourage Paetus to die bravely.",
    ["non dolet = it does not hurt."])
G.q("3 Society", r"What is a \emph{libertus}?",
    "a freed slave", [("a free-born citizen", "That is an ingenuus."),
                      ("a book", "That is liber/libellus."),
                      ("a child", "That is liberi (children).")],
    "libertus = freedman.", "Freed people kept ties to their former masters, now patrons.",
    ["manumissio → libertus."])

G.sec("Constructions that decide sight questions")
G.tex(r"""
\begin{compare}{Form}{Recognize it}{Translate it}
Perfect passive participle & -tus, -sus & having been\ldots; (who was)\ldots \\
Present active participle & -ns, -ntis & (while) \ldots-ing \\
Future active participle & -urus & about to\ldots, going to\ldots \\
Ablative absolute & noun + participle, ablative, set off & with\ldots; when/after/since\ldots \\
Relative pronoun & qui, quae, quod; antecedent agrees in gender and number & who, which, that \\
Indirect statement & accusative + infinitive after a verb of saying, thinking, perceiving & that\ldots \\
Gerund / gerundive & -ndum, -ndi, -ndo / -ndus, -a, -um & ad + gerundive = for the purpose of \\
\end{compare}
""")
G.q("4 Constructions", r"\emph{auditoque pretio} (Pliny 7.27.7) is best translated",
    "and when the price had been heard", [("and hearing the price", "Auditus is perfect passive, not present active."),
                                          ("and the price will be heard", "No."),
                                          ("by the heard price", "An ablative absolute, not means.")],
    "Ablative absolute with -que.", "noun + perfect passive participle in the ablative.",
    ["audito pretio + -que."])
G.q("4 Constructions", r"\emph{moritura} in \emph{nec moritura tenet crudeli funere Dido?} (\emph{Aeneid} 4.308) is",
    "a future active participle: ``about to die''", [("a perfect passive participle: ``having died''", "-urus is future active."),
                                                     ("a present participle: ``dying''", "Present participles end in -ns."),
                                                     ("a gerundive: ``to be killed''", "Gerundives end in -ndus.")],
    "-ura = future active.", "Dido, about to die, should hold him back.",
    ["mori → moriturus."])

G.sec("Task kit: the Project Prose Passage Short Essay")
G.tex(r"""
\begin{compare}{Part}{Do this}{Example (Seneca, \emph{Epistulae} 47)}
A summary (4) & one sentence on the whole; one on each third & Seneca praises his friend for living familiarly with his slaves, rejects contempt for them, and describes how cruelly some masters treat them at dinner. \\
B interpretation (1) & a specific claim that answers the prompt & Seneca presents slaves as fellow human beings and shows the masters' arrogance as the real shame. \\
B examples (2 + 2) & Latin + translation + how it supports the claim & ``Servi sunt.' Immo homines.'' / ``superbissima consuetudo'' \\
B style or context (2) & a device or a fact that sharpens the claim & anaphora of ``Servi sunt'' and the corrections with ``Immo''; Stoic belief in the equality of souls \\
\end{compare}
""")
G.q("5 Project essay", r"In Part B, what earns the two points for each example?",
    "an accurate Latin citation with translation, and an explanation of how it supports the interpretation", [
        ("a long summary of the passage", "Summary belongs to Part A."),
        ("a single Latin word", "More than one word is needed."),
        ("a list of devices with no link to the claim", "The explanation must connect evidence to the claim.")],
    "Citation + explanation.", "Rows 6 and 7 reward Latin evidence and its explanation.",
    ["Latin → translation → how it supports."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 1: Teacher's Choice: Latin Prose: Question Set", r"Unit 1 \textperiodcentered\ Question Set",
        abstract=r"""Three sets and four discrete questions in the exam's formats: a long set on Pliny 3.16 (Arria), two short sight sets in adapted Latin written for this practice, and four discrete sight sentences, followed by a practice Project Prose Passage Short Essay (11 points) on Seneca, \emph{Epistulae} 47.1--3, with the scoring guide and a model response. The Seneca passage is a practice passage, not one of the official Course Project passages. Questions are in English, as on the exam; Latin is quoted without macrons. Allow about 25 minutes for the multiple choice and 30 for the essay.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Essay: \blank\ / 11 \qquad Target: 15+ MCQ and 8+ essay",
        short="Unit 1", sub="Teacher's Choice: Latin Prose")

Q.sec("Long set: Pliny, Epistulae 3.16")
Q.src(r"Long set (sight prose) \textperiodcentered\ Pliny, \emph{Epistulae} 3.16.4--6 (adapted only by omission)", [
    r"Huic illa ita funus paravit, ita duxit exsequias, ut ignoraret maritus; quin immo quotiens cubiculum eius intraret, vivere filium atque etiam commodiorem esse simulabat, ac persaepe interroganti, quid ageret puer, respondebat: `Bene quievit, libenter cibum sumpsit.' Deinde, cum diu cohibitae lacrimae vincerent prorumperentque, egrediebatur; tunc se dolori dabat; satiata siccis oculis composito vultu redibat, tamquam orbitatem foris reliquisset. Praeclarum quidem illud eiusdem, ferrum stringere, perfodere pectus, extrahere pugionem, porrigere marito, addere vocem immortalem ac paene divinam: `Paete, non dolet.'",
], 10, note="Huic: the son, who has died. commodior, -ius: better (in health). simulo, -are: to pretend. orbitas, -atis, f.: loss of a child. pugio, -onis, m.: dagger. Paetus: Arria's husband.")
Q.q("1.C Summary", r"According to the first sentence, how did Arria arrange her son's funeral?",
    "so that her husband would not know about it", [("so that the whole city would attend", "The point is secrecy."),
                                                    ("so that her husband could lead it", "He was ill and unaware."),
                                                    ("so that it would be delayed until her husband recovered", "Not stated.")],
    "ut ignoraret maritus.", "Result clause: so that her husband did not know.",
    ["ita … ut ignoraret maritus."])
Q.q("1.B Grammar", r"\emph{ut ignoraret maritus} is",
    "a result clause", [("a purpose clause", "Ita … ut marks result; the sense is result as well."),
                        ("an indirect question", "No question word."),
                        ("a temporal clause", "Ut + subjunctive after ita.")],
    "ita … ut.", "Ita signals a result clause.",
    ["ita paravit … ut ignoraret."])
Q.q("1.C Summary", r"What did Arria pretend when she entered her husband's room?",
    "that their son was alive and even better", [("that she herself was ill", "No."),
                                                 ("that the doctor had come", "No."),
                                                 ("that she had been away", "No.")],
    "vivere filium … simulabat.", "Indirect statement after simulabat.",
    ["vivere filium atque etiam commodiorem esse."])
Q.q("1.D Translation", r"\emph{persaepe interroganti, quid ageret puer, respondebat} is best translated",
    "very often she answered him when he asked how the boy was doing", [("the boy often asked what she was doing", "Ageret's subject is puer, and interroganti refers to the husband."),
                                                                        ("she often asked the boy what he was doing", "She answers; he asks."),
                                                                        ("very often the boy answered questions", "Respondebat's subject is Arria.")],
    "interroganti = to (him) asking.", "Dative participle; quid ageret puer is an indirect question.",
    ["interroganti (dat.) → to him as he asked."])
Q.q("1.A Meaning", r"In \emph{Bene quievit, libenter cibum sumpsit}, \emph{libenter} means",
    "willingly, with appetite", [("freely, without paying", "Context: eating."),
                                 ("by himself", "No."),
                                 ("as a free man", "Libenter is an adverb of manner.")],
    "libenter = gladly.", "The reassuring lie: the boy slept well and ate gladly.",
    ["libens, libenter."])
Q.q("1.B Grammar", r"In \emph{cum diu cohibitae lacrimae vincerent prorumperentque}, \emph{cohibitae} modifies",
    "lacrimae", [("diu", "Diu is an adverb."),
                 ("vincerent", "A verb."),
                 ("Arria, understood", "It is feminine plural, agreeing with lacrimae.")],
    "Agreement: fem. pl.", "``tears, long held back''.",
    ["cohibitae lacrimae."])
Q.q("1.C Summary", r"What did Arria do when her tears overcame her?",
    "she went out of the room and gave herself to grief", [("she told her husband the truth", "She kept the secret."),
                                                           ("she cried in front of her husband", "She left the room."),
                                                           ("she called the doctor", "No.")],
    "egrediebatur; tunc se dolori dabat.", "Detail.",
    ["went out → grieved → returned composed."])
Q.q("2.A Style", r"\emph{ferrum stringere, perfodere pectus, extrahere pugionem, porrigere marito} contains",
    "asyndeton", [("polysyndeton", "No conjunctions are repeated."),
                  ("chiasmus only", "The main feature is the unconnected series."),
                  ("simile", "No comparison.")],
    "Series without conjunctions.", "Asyndeton speeds Arria's decisive actions.",
    ["four infinitives, no et."])
Q.q("1.D Translation", r"\emph{tamquam orbitatem foris reliquisset} is best translated",
    "as if she had left her loss outside", [("because she had left the house", "Tamquam = as if."),
                                            ("when she lost her child outside", "No."),
                                            ("so that she would leave her loss", "Pluperfect, not purpose.")],
    "tamquam + subjunctive.", "A conditional comparison: as if.",
    ["reliquisset: pluperfect subjunctive."])
Q.q("2.B Context", r"Why does Pliny call Arria's words \emph{immortalem ac paene divinam}?",
    "They became a famous example of courage remembered for generations.", [("They were spoken by a goddess.", "Arria was a woman."),
                                                                           ("They were carved on a temple.", "Not stated."),
                                                                           ("They were part of a prayer.", "No.")],
    "Exemplum.", "Roman writers repeated ``Paete, non dolet'' as a model of virtus.",
    ["vox immortalis."])

Q.sec("Short set: sight prose")
Q.src(r"Short set (sight prose, adapted) \textperiodcentered\ A schoolboy's morning", [
    r"Puer, ne a magistro verberaretur, ante lucem surrexit; tabellas stilumque raptim collegit et per vias obscuras ad ludum cucurrit.",
], 3, note="Latin adapted for this practice. ludus, -i, m.: school. tabellae, -arum, f. pl.: writing tablets. raptim: hastily.")
Q.q("1.B Grammar", r"\emph{ne a magistro verberaretur} expresses",
    "purpose: so that he would not be beaten by the teacher", [("result: so that he was beaten", "Ne marks a negative purpose clause."),
                                                               ("cause: because the teacher beat him", "No."),
                                                               ("time: while the teacher beat him", "No.")],
    "ne + subjunctive.", "Negative purpose clause; passive verb with a + ablative of agent.",
    ["a magistro = by the teacher."])
Q.q("1.C Summary", r"What did the boy do before running to school?",
    "He gathered his writing tablets and stylus.", [("He ate breakfast.", "Not mentioned."),
                                                    ("He woke his teacher.", "No."),
                                                    ("He lit a lamp.", "Not mentioned.")],
    "tabellas stilumque collegit.", "Detail.",
    ["collegit."])
Q.q("1.A Meaning", r"\emph{ante lucem} means",
    "before dawn", [("in front of the light", "Idiomatic: before daylight."),
                    ("after the lesson", "No."),
                    ("near the lamp", "No.")],
    "ante lucem = before daybreak.", "Roman school began very early.",
    ["lux = daylight."])

Q.sec("Short set: sight prose")
Q.src(r"Short set (sight prose, adapted from Valerius Maximus 8.3.3) \textperiodcentered\ Hortensia", [
    r"Hortensia, Q. Hortensii oratoris filia, cum matronae gravi tributo a triumviris onerarentur, causam earum apud triumviros constanter et feliciter egit.",
], 3, note="Latin adapted for this practice. tributum, -i, n.: tax. triumviri, -orum, m. pl.: the three rulers of Rome in 42 BCE. constanter: steadfastly.")
Q.q("1.C Summary", r"What did Hortensia do?",
    "She pleaded the women's case before the triumvirs.", [("She paid the tax for all the women.", "She argued their case."),
                                                           ("She became a triumvir.", "No."),
                                                           ("She wrote a book of speeches for her father.", "Not stated.")],
    "causam earum … egit.", "causam agere = to plead a case.",
    ["apud triumviros."])
Q.q("1.B Grammar", r"\emph{cum matronae gravi tributo \ldots\ onerarentur} is best translated",
    "when the married women were being burdened with a heavy tax", [("because the women burdened the triumvirs", "Onerarentur is passive."),
                                                                    ("although the tax was light", "Gravi = heavy."),
                                                                    ("with the women who burden the tax", "No.")],
    "cum + imperfect passive subjunctive.", "Tributo: ablative of means.",
    ["onerarentur = were being burdened."])
Q.q("2.B Context", r"Why might this passage appear on the AP Latin exam?",
    "It gives voice to a woman speaking in public, a topic underrepresented in the traditional corpus.", [("It is from the Aeneid.", "It is prose."),
                                                                                                         ("It describes Pliny's uncle.", "No."),
                                                                                                         ("It is a letter to Trajan.", "No.")],
    "Underrepresented voices.", "The CED calls for sight passages about underrepresented topics and authors.",
    ["Hortensia's speech (42 BCE)."])

Q.sec("Discrete sight questions")
Q.q("1.D Translation", r"\emph{Servi, quamquam fessi erant, domino cenanti diu adstabant.} This sentence means",
    "Although the slaves were tired, they stood by their master for a long time while he dined.", [("The slaves were tired because their master dined for a long time.", "Quamquam = although."),
                                                                                                    ("The master stood by the tired slaves while they dined.", "Cases reversed."),
                                                                                                    ("The tired slaves dined with their master.", "Cenanti modifies domino.")],
    "quamquam + indicative; dative participle.", "domino cenanti: dative with adstabant.",
    ["adsto + dative."])
Q.q("1.B Grammar", r"In \emph{Epistulam tibi scribo ut scias me valere}, \emph{me valere} is",
    "an indirect statement: ``that I am well''", [("a purpose clause", "Ut scias is the purpose clause; me valere depends on scias."),
                                                  ("an ablative absolute", "Accusative + infinitive."),
                                                  ("a command", "No.")],
    "Accusative + infinitive.", "After scias (know), an indirect statement.",
    ["scias me valere."])
Q.q("1.A Meaning", r"In \emph{Nihil est tam difficile quod non virtute vinci possit}, \emph{vinci} means",
    "to be conquered", [("to conquer", "Vinci is passive."),
                        ("having been conquered", "Infinitive, not participle."),
                        ("wine", "That is vinum.")],
    "present passive infinitive.", "``Nothing is so difficult that it cannot be overcome by courage.''",
    ["vincere → vinci."])
Q.q("1.D Translation", r"\emph{Urbe capta, cives in silvas fugerunt.} This sentence means",
    "After the city was captured, the citizens fled into the woods.", [("The citizens captured the city and fled.", "Urbe capta is an ablative absolute."),
                                                                       ("The citizens fled from the captured woods.", "No."),
                                                                       ("The city will be captured by the citizens in the woods.", "Tense and roles wrong.")],
    "Ablative absolute.", "noun + perfect passive participle in the ablative.",
    ["urbe capta = the city having been captured."])

Q.frq(kind="Project Prose Passage Short Essay", head=r"Question 4 \textperiodcentered\ Project Prose Passage Short Essay (practice passage) \textperiodcentered\ 11 points \textperiodcentered\ about 30 minutes", mins=30,
      directions=[r"This is a practice passage in the format of the Course Project questions. On the exam, the passage is one of your two prose project passages, printed without title, attribution, glossary or commentary. Read the passage, then answer Parts A and B in English."],
      sources=[dict(title=r"Seneca, \emph{Epistulae Morales} 47.1--3", paras=[
          r"Libenter ex iis qui a te veniunt cognovi familiariter te cum servis tuis vivere: hoc prudentiam tuam, hoc eruditionem decet. `Servi sunt.' Immo homines. `Servi sunt.' Immo contubernales. `Servi sunt.' Immo humiles amici. `Servi sunt.' Immo conservi, si cogitaveris tantundem in utrosque licere fortunae.",
          r"Itaque rideo istos qui turpe existimant cum servo suo cenare: quare, nisi quia superbissima consuetudo cenanti domino stantium servorum turbam circumdedit? Est ille plus quam capit [\ldots].",
          r"At infelicibus servis movere labra ne in hoc quidem ut loquantur, licet; virga murmur omne compescitur [\ldots]; nocte tota ieiuni mutique perstant."])],
      prompt=[r"\textbf{Part A.} In your own words, summarize the passage in 4 to 5 complete sentences. Provide a summary sentence that identifies what the passage as a whole is about, and address the beginning, middle and end.",
              r"\textbf{Part B.} Describe Seneca's attitude toward slaves in this passage. Explain how the passage develops this attitude. Support your interpretation with at least two specific Latin citations (Latin, or line references, with a translation or accurate paraphrase) and with a stylistic or contextual feature of the text."],
      model=[r"\textbf{Part A.} Seneca writes to a friend to praise the humane way he treats his slaves. He begins by saying he is glad to hear that his friend lives on familiar terms with his slaves, and he answers the objection ``they are slaves'' by calling them human beings, companions, humble friends and fellow slaves. He then mocks masters who think it shameful to dine with a slave and blames arrogant custom, which surrounds an overeating master with a crowd of standing slaves. Finally, he describes how these unfortunate slaves may not even move their lips: every murmur is punished with the rod, and they stand all night hungry and silent.",
             r"\textbf{Part B.} Seneca regards slaves as fellow human beings and treats the cruelty of their masters, not slavery itself, as the true disgrace. He develops this attitude first through a series of corrections: to the repeated objection ``Servi sunt'' (``they are slaves'') he answers ``Immo homines'' and ``Immo humiles amici'' (``no, human beings'', ``no, humble friends''). Each ``Immo'' replaces a social label with a moral one, so that the reader moves from status to shared humanity. He then turns the charge of shame against the masters: he laughs at those who think it ``turpe'' (shameful) to dine with a slave and blames ``superbissima consuetudo'', ``a most arrogant custom''. The superlative shows that the problem lies in the masters' pride. Stylistically, the anaphora of ``Servi sunt'' imitates the stubborn voice of the objector, which Seneca defeats four times; contextually, his view reflects Stoic teaching that fortune (``tantundem in utrosque licere fortunae'') rules masters and slaves alike, so no one is free from the chance of becoming a slave."],
      rows=[("A1 Summary sentence", 1, "identifies what the whole passage is about (Seneca praises humane treatment of slaves and criticizes masters' arrogance)", "a sentence on one detail only"),
            ("A2 Beginning", 1, "praise of the friend; the corrections to ``they are slaves''", "omitting the beginning or misreading it"),
            ("A3 Middle", 1, "mockery of masters who will not dine with slaves; arrogant custom", "inaccurate or missing"),
            ("A4 End", 1, "slaves forbidden to speak, punished, standing hungry and silent all night", "inaccurate or missing"),
            ("B1 Interpretation", 1, "a specific claim about Seneca's attitude", "restating the prompt"),
            ("B2 First example", 2, "accurate Latin citation of more than one word, translated, with an explanation of how it supports the claim", "single word; no explanation"),
            ("B3 Second example", 2, "a second, different citation, translated and explained", "repeating the first example"),
            ("B4 Style or context", 2, "a stylistic feature (anaphora of ``Servi sunt'', ``Immo'', superlative) or context (Stoic equality, fortune) explained in relation to the claim", "a device named with no link to the claim")],
      tips=["Part A covers beginning, middle and end in order, with an overall summary sentence first.", "Each Part B citation gives the Latin, translates it, and explains its effect.",
            "The style point (anaphora) and the context point (Stoicism) are both tied back to the interpretation."],
      ask="Write Part A and Part B in English, then mark each row.", lines=22)

GUIDE, QSET = G, Q
