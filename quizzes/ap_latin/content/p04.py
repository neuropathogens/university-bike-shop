from ap_wl.model import Doc

STEM = "04-aeneid-1-2"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 4: Vergil's Aeneid, Books 1 and 2", r"Unit 4 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 4 begins the poetry half of the course with Teacher's Choice poetry and the first Aeneid readings: Book 1, lines 1--33 (the proem and Juno's anger), 88--107 (the storm), 496--508 (Dido's entrance), and Book 2, lines 40--56 and 201--249 (Laocoön and the wooden horse). This guide sets out Vergil and the Augustan context, each passage's content and key Latin, the conventions of epic, the devices and meter the exam asks about, and a Short Essay kit. Latin is quoted without macrons from a public-domain text. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Lines I can scan: \blank[10em]",
        short="Unit 4", sub="Vergil's Aeneid, Books 1 and 2")

G.sec("Vergil, Augustus and the Aeneid")
G.tex(r"""
\begin{compare}{Fact}{Detail}{Why it matters}
Vergil & 70--19 BCE; also wrote the \emph{Eclogues} and \emph{Georgics} & the poet of Augustan Rome \\
Augustus & sole ruler after Actium (31 BCE); claimed descent from Aeneas through Iulus & the epic gives Rome and its ruler a destiny \\
The poem & 12 books of dactylic hexameter, unfinished at Vergil's death & Books 1--6 recall the \emph{Odyssey}, 7--12 the \emph{Iliad} \\
Aeneas & Trojan prince, son of Venus, marked by \emph{pietas} (duty to gods, family, country) & ``insignem pietate virum'' (1.10) \\
Juno & hostile to the Trojans: she loves Carthage, resents the judgment of Paris & ``Tantaene animis caelestibus irae?'' (1.11) \\
\end{compare}

``Tantae molis erat Romanam condere gentem'' (1.33): ``so great a labor it was to found the Roman race''. The proem announces the poem's subject (arms and the man), its goal (Rome) and its cost.
""")
G.q("1 Context", r"What quality does Vergil attribute to Aeneas in \emph{insignem pietate virum} (1.10)?",
    "pietas: devotion to gods, family and country", [("furor: rage", "Furor is the opposite force."),
                                                     ("dolus: trickery", "That is Ulysses."),
                                                     ("luxuria: luxury", "No.")],
    "pietas.", "Aeneas's defining virtue.",
    ["insignem pietate = outstanding in devotion."])
G.q("1 Context", r"Why is Juno hostile to the Trojans at the start of the Aeneid?",
    "She favors Carthage and still resents Paris's judgment and other Trojan slights.", [("Aeneas insulted her temple in Rome.", "Rome is not yet founded."),
                                                                                       ("She is Aeneas's mother.", "Venus is."),
                                                                                       ("Jupiter ordered her to oppose them.", "No.")],
    "Carthage + old resentments.", "Lines 12–33 set out her motives.",
    ["iudicium Paridis, spretaeque iniuria formae."])

G.sec("Book 1: the proem, the storm and Dido")
G.tex(r"""
\begin{compare}{Lines}{What happens}{Key Latin}
1--11 & the poet sings of arms and the man; invokes the Muse to explain Juno's anger & ``Arma virumque cano''; ``Musa, mihi causas memora'' \\
12--33 & Carthage, Juno's favorite city; her fear of the Trojans' descendants & ``Tantae molis erat Romanam condere gentem'' \\
88--107 & the storm darkens the sky; Aeneas's first speech: those who died at Troy were blessed & ``O terque quaterque beati''; ``Tydide'' \\
496--508 & Dido enters the temple, compared to Diana leading her dancers; she sits to give laws & ``talis erat Dido''; ``iura dabat legesque viris'' \\
\end{compare}

\textbf{The storm speech.} Aeneas's first words are not heroic boasts but despair: ``Extemplo Aeneae solvuntur frigore membra'' (1.92). He envies those who died ``ante ora patrum'' and wishes he had fallen to Diomedes (Tydides).
""")
G.q("2 Book 1", r"How does Aeneas react to the storm in his first speech?",
    "with despair, wishing he had died at Troy", [("with confidence, sure of victory", "His limbs go slack with cold fear."),
                                                  ("with anger at Dido", "Dido has not appeared."),
                                                  ("with a prayer to Juno", "He addresses the dead and Diomedes.")],
    "O terque quaterque beati.", "A human, vulnerable hero at the outset.",
    ["solvuntur frigore membra."])
G.q("2 Book 1", r"To whom is Dido compared when she enters the temple?",
    "Diana leading her bands of dancers", [("Juno on Olympus", "No."),
                                           ("Venus rising from the sea", "No."),
                                           ("Penthesilea in battle", "Penthesilea appears just before, in the temple images.")],
    "qualis … Diana.", "The simile stresses Dido's beauty, majesty and leadership.",
    ["talis erat Dido."])

G.sec("Book 2: Laocoön and the horse")
G.tex(r"""
\begin{compare}{Lines}{What happens}{Key Latin}
40--56 & Laocoön runs down from the citadel, warns the Trojans that the horse is a trick, and hurls his spear into its belly & ``equo ne credite, Teucri. / quidquid id est, timeo Danaos et dona ferentis'' \\
201--227 & two serpents come from Tenedos across the calm sea, kill Laocoön's two sons and then Laocoön & ``horresco referens''; ``sibila lambebant linguis vibrantibus ora'' \\
228--249 & the Trojans think Laocoön was punished for striking the horse; they breach the walls and drag it in; Cassandra is not believed & ``quater ipso in limine portae / substitit''; ``non umquam credita Teucris'' \\
\end{compare}

\textbf{Narrator.} Book 2 is told by Aeneas himself to Dido: ``horresco referens'' (I shudder as I tell it) reminds us of the survivor reliving the night Troy fell.
""")
G.q("3 Book 2", r"What does Laocoön mean by \emph{timeo Danaos et dona ferentis}?",
    "I fear the Greeks even when they bring gifts.", [("I fear the gifts the Trojans bring.", "Danaos = Greeks."),
                                                       ("The Greeks fear our gifts.", "Timeo is first person."),
                                                       ("I fear the Greeks who carry spears.", "Dona = gifts.")],
    "et = even.", "The most famous warning in Latin.",
    ["Danaos (acc.) … ferentis (= ferentes, acc.)."])
G.q("3 Book 2", r"How do the Trojans interpret Laocoön's death?",
    "as punishment for striking the sacred horse with his spear", [("as an accident at sea", "No."),
                                                                   ("as a sign that the Greeks were defeated", "No."),
                                                                   ("as the work of Cassandra", "No.")],
    "scelus expendisse merentem.", "Their misreading leads them to bring the horse in.",
    ["sacrum qui cuspide robur laeserit."])
G.q("3 Book 2", r"What is ironic about Cassandra in lines 246--247?",
    "she foretells the truth but is never believed by the Trojans", [("she lies and is believed", "The reverse."),
                                                                     ("she helps the Greeks", "No."),
                                                                     ("she is a Greek spy", "No.")],
    "non umquam credita Teucris.", "Dramatic irony: the reader knows she is right.",
    ["fatis … futuris."])

G.sec("Epic conventions, devices and meter")
G.tex(r"""
\begin{compare}{Convention or device}{Example}{Effect}
Invocation & ``Musa, mihi causas memora'' (1.8) & epic authority \\
In medias res & the poem opens in the seventh year of wandering & Book 2 flashes back to Troy \\
Epic simile & Dido like Diana (1.498--502) & elevation; characterization \\
Apostrophe & ``O Danaum fortissime gentis / Tydide!'' (1.96--97) & emotion \\
Rhetorical question & ``Tantaene animis caelestibus irae?'' (1.11) & the poem's moral question \\
Polysyndeton & ``caelumque diemque'' (1.88) & fullness; nothing is left in sight \\
Alliteration, onomatopoeia & ``sibila lambebant linguis vibrantibus ora'' (2.211) & the serpents' hissing \\
Enjambment & ``Laviniaque venit / litora'' (1.2--3) & sense carried over the line break \\
\end{compare}

\textbf{Scanning.} Mark elisions; mark syllables long by position; the fifth foot is usually a dactyl and the sixth two syllables; fill feet 1--4 from what is left.
""")
G.q("4 Style", r"Which device makes the serpents audible in \emph{sibila lambebant linguis vibrantibus ora}?",
    "alliteration of s and l (with onomatopoeia)", [("chiasmus", "No ABBA arrangement of meaning."),
                                                     ("apostrophe", "No address."),
                                                     ("litotes", "No understatement.")],
    "Sound effects.", "The repeated sibilants and l's imitate hissing and licking.",
    ["sibila … lambebant … linguis."])
G.q("4 Style", r"\emph{Tantaene animis caelestibus irae?} (1.11) is",
    "a rhetorical question about divine anger", [("a command to the gods", "No."),
                                                 ("a simile", "No."),
                                                 ("an answer from the Muse", "The Muse has just been asked.")],
    "Can heavenly minds hold such anger?", "The poem's central moral question.",
    ["-ne marks the question."])

G.sec("Task kit: the Short Essay (Q3) on Vergil")
G.tex(r"""
\begin{compare}{Part}{What earns points}{Example (Laocoön, 2.42--49)}
A(i) & comprehension: answer the question & Laocoön suspects Greeks are hidden inside the horse \\
A(ii) & the Latin that supports it & ``hoc inclusi ligno occultantur Achivi'' \\
A(iii) & an accurate translation of that Latin & ``the Greeks are hidden, shut inside this wood'' \\
B interpretation & a claim answering the prompt & Laocoön is urgent and contemptuous of Greek trickery \\
B citation (2) & more than one word of Latin, translated & ``sic notus Ulixes?'' ``is this how you know Ulysses?'' \\
B explanation (2) & how the citation supports the claim & sarcasm reminds the Trojans of Ulysses's notorious deceit \\
\end{compare}
""")
G.q("5 Short Essay", r"In Part B, why is ``\emph{sic notus Ulixes?}'' good evidence for Laocoön's distrust?",
    "It sarcastically reminds the Trojans of Ulysses's reputation for trickery.", [("It praises Ulysses as a friend of Troy.", "The question is sarcastic."),
                                                                                   ("It is a single word.", "It is three words, with meaning in context."),
                                                                                   ("It describes the horse's size.", "No.")],
    "Sarcastic question.", "Rhetorical questions reveal attitude.",
    ["notus = known (for deceit)."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 4: Vergil's Aeneid, Books 1 and 2: Question Set", r"Unit 4 \textperiodcentered\ Question Set",
        abstract=r"""Three sets and four discrete questions in the exam's formats: a long set on \emph{Aeneid} 1.88--99 (the storm), a short syllabus set on 1.503--506 (Dido), a short sight set on 2.268--271 (Hector's ghost), and four discrete sight sentences, followed by a Short Essay (8 points) on Laocoön's warning, 2.42--49, with the scoring guide and a model response. Questions are in English, as on the exam; Latin is quoted without macrons. Allow about 25 minutes for the multiple choice and 25 for the short essay.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Short Essay: \blank\ / 8 \qquad Target: 15+ MCQ and 6+ short essay",
        short="Unit 4", sub="Vergil's Aeneid, Books 1 and 2")

Q.sec("Long set: Aeneid 1.88-99")
Q.src(r"Long set (syllabus poetry) \textperiodcentered\ Vergil, \emph{Aeneid} 1.88--99", [
    r"Eripiunt subito nubes caelumque diemque\\ Teucrorum ex oculis; ponto nox incubat atra.\\ Intonuere poli, et crebris micat ignibus aether,\\ praesentemque viris intentant omnia mortem.\\ Extemplo Aeneae solvuntur frigore membra:\\ ingemit, et duplicis tendens ad sidera palmas\\ talia voce refert: `O terque quaterque beati,\\ quis ante ora patrum Troiae sub moenibus altis\\ contigit oppetere! O Danaum fortissime gentis\\ Tydide! Mene Iliacis occumbere campis\\ non potuisse, tuaque animam hanc effundere dextra,\\ saevus ubi Aeacidae telo iacet Hector [\ldots]'",
], 10, note="intono, -are, -ui: to thunder. polus, -i, m.: sky, pole. duplex, -icis: both. oppeto, -ere: to meet death. Tydides, -ae, m.: son of Tydeus (Diomedes). Aeacides, -ae, m.: descendant of Aeacus (Achilles).")
Q.q("1.C Summary", r"According to lines 1--2, what do the clouds do?",
    "They snatch the sky and daylight from the Trojans' eyes.", [("They bring rain to the fields.", "No."),
                                                                 ("They reveal the shore.", "The opposite."),
                                                                 ("They carry the ships to Italy.", "No.")],
    "Eripiunt … ex oculis.", "Darkness falls suddenly.",
    ["caelumque diemque."])
Q.q("2.A Style", r"\emph{caelumque diemque} (line 1) contains",
    "polysyndeton", [("asyndeton", "There are conjunctions."),
                     ("chiasmus", "No ABBA."),
                     ("apostrophe", "No address.")],
    "-que … -que.", "Repeated conjunctions slow and fill the line.",
    ["caelum-que diem-que."])
Q.q("1.D Translation", r"\emph{ponto nox incubat atra} is best translated",
    "black night broods over the sea", [("the sea lies on the black night", "Ponto is dative with incubat."),
                                        ("night falls into the black sea", "Atra agrees with nox."),
                                        ("the black sea broods at night", "Nox is the subject.")],
    "incubo + dative.", "atra (nom. fem.) with nox.",
    ["ponto (dat.)."])
Q.q("1.B Grammar", r"\emph{Intonuere} (line 3) is",
    "perfect tense, third person plural (= intonuerunt)", [("present infinitive", "The -ere ending here is the alternative perfect ending."),
                                                           ("imperative plural", "No."),
                                                           ("future tense", "No.")],
    "-ere = -erunt.", "Poetic perfect ending.",
    ["intonuere poli = the skies thundered."])
Q.q("1.C Summary", r"What does everything threaten the men with in line 4?",
    "immediate death", [("exile to Italy", "No."),
                        ("Juno's anger", "Not stated here."),
                        ("a long voyage", "No.")],
    "praesentem … mortem.", "Interlocked: praesentem … mortem.",
    ["intentant omnia mortem."])
Q.q("1.D Translation", r"\emph{Extemplo Aeneae solvuntur frigore membra} is best translated",
    "At once Aeneas's limbs go slack with cold (fear).", [("At once Aeneas loosened his cold limbs.", "Solvuntur is passive; membra is the subject."),
                                                          ("Aeneas freed his men from the cold.", "No."),
                                                          ("The cold limbs of Aeneas were freed by the storm.", "Frigore is the cause, not the agent.")],
    "Aeneae: dative of reference (possession).", "frigore: ablative of cause.",
    ["solvuntur membra."])
Q.q("1.B Grammar", r"\emph{duplicis \ldots\ palmas} (line 6) means",
    "both hands", [("double palms", "Duplicis = both (= duplices, acc. pl.)."),
                   ("two palm trees", "Palmae here = hands."),
                   ("the palms of two men", "No.")],
    "duplicis = acc. pl. (-is for -es).", "He stretches both hands to the stars.",
    ["tendens ad sidera palmas."])
Q.q("1.C Summary", r"Whom does Aeneas call \emph{terque quaterque beati}?",
    "those who died at Troy before their fathers' eyes", [("the gods on Olympus", "No."),
                                                         ("his companions on the ships", "No."),
                                                         ("the Greeks who survived", "No.")],
    "quis … contigit oppetere.", "He envies the dead.",
    ["ante ora patrum Troiae sub moenibus altis."])
Q.q("2.B Context", r"Who is \emph{Tydide} (line 10)?",
    "Diomedes, the Greek hero who fought Aeneas at Troy", [("Hector, the Trojan prince", "Hector is mentioned next."),
                                                           ("Achilles, the son of Peleus", "That is Aeacides."),
                                                           ("Ulysses", "No.")],
    "Tydides = son of Tydeus.", "Aeneas wishes he had died at Diomedes's hand (Iliad 5).",
    ["patronymic."])
Q.q("2.A Meter", r"Which is the correct pattern of the first four feet of \emph{Eripiunt subito nubes caelumque diemque}?",
    "DDSS", [("DSDS", "Foot 2 (unt subi) is a dactyl."),
             ("SDDS", "Foot 1 (Eripi) is a dactyl."),
             ("DDSD", "Foot 4 (bes cae) is a spondee: nubes ends in a long -es, and ae is a diphthong.")],
    "Eripi | unt subi | to nu | bes cae | lumque di | emque.", "Feet: D D S S D S.",
    ["– u u | – u u | – – | – – | – u u | – x."])

Q.sec("Short set: Aeneid 1.503-506")
Q.src(r"Short set (syllabus poetry) \textperiodcentered\ Vergil, \emph{Aeneid} 1.503--506", [
    r"talis erat Dido, talem se laeta ferebat\\ per medios, instans operi regnisque futuris.\\ Tum foribus divae, media testudine templi,\\ saepta armis, solioque alte subnixa resedit.",
], 3, note="testudo, -inis, f.: vaulted roof. solium, -i, n.: throne. subnixus, -a, -um: supported, resting on.")
Q.q("2.A Style", r"\emph{talis erat Dido, talem se laeta ferebat} contains",
    "anaphora (polyptoton) of talis, closing the simile", [("an apostrophe to Dido", "No address."),
                                                           ("asyndeton of verbs", "No."),
                                                           ("a rhetorical question", "No.")],
    "talis … talem.", "Closes the Diana simile and returns to Dido.",
    ["qualis (simile) → talis."])
Q.q("1.C Summary", r"How does Dido carry herself among her people?",
    "joyfully, urging on the work of her future kingdom", [("sadly, mourning her husband", "Laeta = joyful."),
                                                          ("fearfully, hiding from the Trojans", "No."),
                                                          ("angrily, punishing workers", "No.")],
    "laeta … instans operi regnisque futuris.", "A queen absorbed in building Carthage.",
    ["laeta, instans."])
Q.q("1.C Summary", r"Where does Dido sit down?",
    "on a high throne at the doors of the goddess's temple", [("in the harbor", "No."),
                                                              ("in Aeneas's ship", "No."),
                                                              ("on the city walls", "No.")],
    "foribus divae … solio alte.", "Center of the temple; surrounded by armed men.",
    ["saepta armis."])

Q.sec("Short set: sight poetry")
Q.src(r"Short set (sight poetry) \textperiodcentered\ Vergil, \emph{Aeneid} 2.268--271", [
    r"Tempus erat quo prima quies mortalibus aegris\\ incipit et dono divum gratissima serpit.\\ in somnis, ecce, ante oculos maestissimus Hector\\ visus adesse mihi largosque effundere fletus.",
], 3, note="divum = divorum. serpo, -ere: to creep. fletus, -us, m.: weeping.")
Q.q("1.C Summary", r"At what time does Hector appear to Aeneas?",
    "at the time of the first sleep, at night", [("at dawn", "Prima quies = first rest."),
                                                 ("at midday", "No."),
                                                 ("during battle", "In a dream.")],
    "prima quies.", "Sleep creeps over weary mortals.",
    ["in somnis."])
Q.q("1.D Translation", r"\emph{visus adesse mihi} is best translated",
    "seemed to be present to me", [("saw me present", "Visus (est) = seemed."),
                                   ("was seen to help me", "Adesse = to be present."),
                                   ("I seemed to be present", "Mihi is dative.")],
    "videor = seem.", "Passive of video: to seem.",
    ["visus (est)."])
Q.q("2.A Style", r"\emph{maestissimus Hector} and \emph{largos effundere fletus} emphasize",
    "Hector's grief", [("Hector's anger at the Greeks", "No."),
                       ("Hector's joy at returning", "No."),
                       ("Aeneas's fear of Hector", "No.")],
    "Superlative + tears.", "The ghost weeps for Troy.",
    ["maestissimus = most sorrowful."])

Q.sec("Discrete sight questions")
Q.q("1.D Translation", r"\emph{Rex iussit portas claudi ne hostes urbem intrarent.} This sentence means",
    "The king ordered the gates to be closed so that the enemy would not enter the city.", [("The king closed the gates after the enemy entered.", "Claudi is a passive infinitive; ne marks purpose."),
                                                                                            ("The enemy ordered the king to close the gates.", "Rex is the subject."),
                                                                                            ("The king ordered the enemy to close the gates.", "Hostes is the subject of intrarent.")],
    "iubeo + acc. + passive inf.; ne + subj.", "Purpose clause.",
    ["claudi = to be closed."])
Q.q("1.A Meaning", r"In \emph{Fama volat per urbes}, \emph{fama} means",
    "rumor", [("hunger", "That is fames."),
              ("family", "That is familia."),
              ("fate", "That is fatum.")],
    "fama = rumor, report.", "Vergil personifies Fama in Book 4.",
    ["Fama volat."])
Q.q("1.B Grammar", r"In \emph{Troia capta, Aeneas fugit}, \emph{Troia capta} is",
    "an ablative absolute", [("the subject of fugit", "Aeneas is the subject."),
                             ("a vocative", "No."),
                             ("a nominative absolute", "Latin uses the ablative.")],
    "noun + PPP, ablative.", "Troy having been captured, Aeneas fled.",
    ["Troiā captā."])
Q.q("1.D Translation", r"\emph{Venus filio apparuit dixitque eum in Africam venisse.} This sentence means",
    "Venus appeared to her son and said that he had come to Africa.", [("Venus appeared and said that she had come to Africa.", "Eum refers to the son."),
                                                                       ("The son appeared to Venus in Africa.", "Venus is the subject."),
                                                                       ("Venus said to her son, ``Come to Africa.''", "Indirect statement, perfect infinitive.")],
    "Indirect statement, perfect infinitive.", "venisse = had come.",
    ["dixit eum … venisse."])

Q.frq(kind="Short Essay", head=r"Question 3 \textperiodcentered\ Short Essay \textperiodcentered\ 8 points \textperiodcentered\ about 25 minutes", mins=25,
      directions=[r"Read the passage, then answer Parts A and B in English unless a question asks for Latin."],
      sources=[dict(title=r"Vergil, \emph{Aeneid} 2.42--49", paras=[
          r"et procul `o miseri, quae tanta insania, cives?\\ creditis avectos hostis? aut ulla putatis\\ dona carere dolis Danaum? sic notus Ulixes?\\ aut hoc inclusi ligno occultantur Achivi,\\ aut haec in nostros fabricata est machina muros,\\ inspectura domos venturaque desuper urbi,\\ aut aliquis latet error; equo ne credite, Teucri.\\ quidquid id est, timeo Danaos et dona ferentis.'",
          r"\emph{aveho, -ere, -vexi, -vectum}: to carry away \quad \emph{careo, -ere} + abl.: to lack \quad \emph{Danai, -orum} and \emph{Achivi, -orum}: Greeks \quad \emph{hostis} = \emph{hostes}; \emph{ferentis} = \emph{ferentes}"])],
      prompt=[r"\textbf{A.} (i) Identify one possibility Laocoön suggests about the horse. (ii) Provide the Latin word(s) that support your answer in part (i). (iii) Translate in context the Latin word(s) you cited in part (ii).",
              r"\textbf{B.} Describe Laocoön's attitude toward the Greeks and explain how the passage expresses it. Your response should be 3 to 4 complete sentences. Respond to the prompt with an interpretation; include at least one specific Latin citation (more than a single word), with a translation or accurate paraphrase; and explain how the citation supports your response."],
      model=[r"\textbf{A.} (i) Greek soldiers may be hidden inside the horse. (ii) \emph{hoc inclusi ligno occultantur Achivi} (line 4). (iii) ``The Greeks, shut in, are hidden in this wood.''",
             r"\textbf{B.} Laocoön regards the Greeks as treacherous and is contemptuous of the Trojans' trust in them. He asks sarcastically, ``sic notus Ulixes?'' (line 3), ``is this how you know Ulysses?'', reminding the Trojans that Ulysses is famous for tricks, so the horse cannot be an innocent gift. His final words, ``timeo Danaos et dona ferentis'' (line 8), ``I fear the Greeks even when they bring gifts'', show that in his view even a Greek gift is a weapon."],
      rows=[("A(i) Comprehension", 1, "a possibility from the text (Greeks hidden inside; a machine against the walls; some other trick)", "a possibility not in the text"),
            ("A(ii) Latin", 1, "Latin that supports A(i)", "Latin for a different idea"),
            ("A(iii) Translation", 1, "accurate translation of the cited Latin", "inaccurate tense, voice or case"),
            ("B Interpretation", 1, "a claim about Laocoön's attitude (distrust, contempt, urgency)", "restating the prompt"),
            ("B Latin citation", 2, "a specific citation of more than one word, translated or accurately paraphrased", "a single word; no translation"),
            ("B Explanation", 2, "explains how the citation supports the claim", "quotation with no explanation")],
      tips=["A(ii) and A(iii) quote and translate exactly the Latin that supports A(i).", "Part B cites two phrases, each translated and tied to the claim.",
            "Three sentences: claim, evidence and explanation, evidence and explanation."],
      ask="Answer Parts A and B in English, then mark each row.", lines=12)

GUIDE, QSET = G, Q
