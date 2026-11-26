from ap_wl.model import Doc

STEM = "05-aeneid-4-12"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 5: Vergil's Aeneid, Books 4, 6, 7, 11 and 12", r"Unit 5 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 5 follows the Aeneid to its end: Dido's love and anger in Book 4 (74--89, 165--197, 305--361), the Underworld in Book 6 (Dido's shade, 450--476; Augustus and the Roman mission, 788--800 and 847--853), King Latinus and Turnus's preparations in Book 7 (45--58, 783--792, 803--817), the story of Camilla in Book 11 (532--594), and the settlement between Jupiter and Juno and the death of Turnus in Book 12 (791--796, 803--812, 818--828, 919--952). This guide sets out each passage's content and key Latin, the themes the exam asks about (pietas and furor, the cost of empire, the Augustan vision and its tensions), and a Short Answer kit with scansion. Latin is quoted without macrons from a public-domain text. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Lines I can scan: \blank[10em]",
        short="Unit 5", sub="Vergil's Aeneid, Books 4, 6, 7, 11 and 12")

G.sec("Book 4: Dido and Aeneas")
G.tex(r"""
\begin{compare}{Lines}{What happens}{Key Latin}
74--89 & Dido, in love, shows Aeneas her city, asks again for the story of Troy; building in Carthage stops & ``pendent opera interrupta'' (4.88) \\
165--197 & in a storm Dido and Aeneas shelter in a cave, and she calls it marriage; Rumor spreads the news to King Iarbas & ``Extemplo Libyae magnas it Fama per urbes, / Fama, malum qua non aliud velocius ullum'' \\
305--361 & Dido confronts Aeneas, who is secretly preparing to leave; he answers that the gods command him & ``dissimulare etiam sperasti, perfide''; ``Italiam non sponte sequor'' \\
\end{compare}

\textbf{Two duties in conflict.} Dido's case rests on love, the right hand given (\emph{data dextera}) and her sacrifice; Aeneas's on Mercury's message and his duty to his son and to Italy. Vergil gives Dido the stronger rhetoric and Aeneas the stronger obligation: a tragic conflict, not a simple verdict.
""")
G.q("1 Book 4", r"What does \emph{pendent opera interrupta} (4.88) show?",
    "Dido's love has halted the building of Carthage.", [("Carthage is finished and safe.", "The work hangs interrupted."),
                                                         ("The Trojans are building ships.", "Different scene."),
                                                         ("The gods destroyed the walls.", "No.")],
    "Love distracts the queen from her city.", "A sign of the cost of passion for the state.",
    ["pendent = hang (unfinished)."])
G.q("1 Book 4", r"What does Aeneas mean by \emph{Italiam non sponte sequor} (4.361)?",
    "He seeks Italy not by his own choice but by the gods' command.", [("He does not want to go to Italy, so he will stay.", "He goes, unwillingly."),
                                                                       ("He follows Dido to Italy.", "No."),
                                                                       ("He has already reached Italy.", "No.")],
    "non sponte = not of his own will.", "Pietas over personal desire.",
    ["sequor = I seek, follow."])

G.sec("Book 6: Dido's shade and Rome's future")
G.tex(r"""
\textbf{450--476.} In the Fields of Mourning Aeneas sees Dido, ``recens a vulnere'', dim like the new moon seen through clouds. He weeps and swears he left her unwillingly. She keeps her eyes fixed on the ground, unmoved ``quam si dura silex aut stet Marpesia cautes'', and turns away to her first husband Sychaeus, who ``respondet curis aequatque \ldots\ amorem''.

\textbf{788--800.} Anchises shows Aeneas Augustus: ``hic vir, hic est, tibi quem promitti saepius audis, / Augustus Caesar, divi genus, aurea condet / saecula''. A golden age will return to Latium; his empire will stretch beyond the stars.

\textbf{847--853.} Others (the Greeks) will cast bronze, carve marble, plead cases and chart the heavens; Rome's arts will be to rule: ``tu regere imperio populos, Romane, memento \ldots\ parcere subiectis et debellare superbos.''
""")
G.q("2 Book 6", r"How does Dido respond to Aeneas in the Underworld?",
    "She remains silent, unmoved like stone, and turns away to Sychaeus.", [("She forgives him and embraces him.", "She refuses to speak."),
                                                                             ("She curses him aloud.", "She is silent."),
                                                                             ("She asks him to stay with her.", "No.")],
    "dura silex.", "Her silence reverses their scene in Book 4.",
    ["inimica refugit."])
G.q("2 Book 6", r"According to Anchises (6.847--853), what will be Rome's particular arts?",
    "to rule peoples, impose peace, spare the conquered and defeat the proud", [("sculpture, oratory and astronomy", "Those are left to others (alii)."),
                                                                                ("sailing and trade", "No."),
                                                                                ("poetry and music", "No.")],
    "hae tibi erunt artes.", "Rule, law, mercy and war.",
    ["parcere subiectis et debellare superbos."])

G.sec("Books 7, 11 and 12: war in Italy and the end")
G.tex(r"""
\begin{compare}{Lines}{What happens}{Key point}
7.45--58 & old King Latinus rules in peace; his only child, Lavinia, is sought by many, above all Turnus, favored by the queen & Lavinia's marriage will decide the future \\
7.783--792, 803--817 & Turnus, huge in arms, with the Chimaera on his helmet; then Camilla the Volscian warrior, admired by all & the Italian heroes \\
11.532--594 & Diana tells Opis how Metabus, fleeing, tied the infant Camilla to his spear and hurled her across the river Amasenus, vowing her to Diana & Camilla's origin; Diana's grief at her coming death \\
12.791--828 & Jupiter grants Juno's last request: the Latins will keep their name, language and dress; the Trojans will merge with them & ``occidit, occideritque sinas cum nomine Troia'' \\
12.919--952 & Aeneas wounds Turnus, hesitates at his plea, sees Pallas's sword belt and kills him in rage & ``furiis accensus et ira''; ``vitaque cum gemitu fugit indignata sub umbras'' \\
\end{compare}
""")
G.q("3 Books 7--12", r"Why does Aeneas kill Turnus after hesitating?",
    "He sees the sword belt Turnus took from the young Pallas and is seized by rage.", [("Turnus attacks him again.", "Turnus has asked for mercy."),
                                                                                       ("Jupiter orders him to.", "Not in the passage."),
                                                                                       ("Lavinia asks him to.", "No.")],
    "balteus … Pallantis.", "Revenge for Pallas: pietas or furor?",
    ["furiis accensus et ira."])
G.q("3 Books 7--12", r"What does Juno obtain from Jupiter in Book 12?",
    "that the Latins keep their name, language and customs", [("that Troy be rebuilt in Italy", "She asks that Troy's name die."),
                                                              ("that Aeneas die in battle", "No."),
                                                              ("that Carthage rule Italy", "No.")],
    "occidit … cum nomine Troia.", "Rome will be Italian in name and speech.",
    ["sit Romana potens Itala virtute propago."])

G.sec("Themes and tensions")
G.tex(r"""
\begin{compare}{Theme}{Evidence}{What to say}
Pietas and furor & ``Italiam non sponte sequor''; ``furiis accensus et ira'' & the hero of duty ends the poem in rage \\
The cost of empire & Dido's death; Camilla, Turnus & each step toward Rome destroys someone \\
Augustan vision & ``aurea condet saecula''; ``parcere subiectis'' & the poem celebrates Rome's mission \\
Tension & Aeneas does not spare Turnus, who is ``subiectus'' & readers debate whether the ending fulfills or questions the ideal \\
Women of the epic & Dido, Camilla, Juno & powerful figures whose stories the poem mourns \\
\end{compare}
""")
G.q("4 Themes", r"Why do readers find the ending of the Aeneid troubling in light of 6.853?",
    "Aeneas kills a defeated, pleading enemy instead of sparing the conquered.", [("Aeneas spares Turnus, contrary to the gods.", "He kills him."),
                                                                                  ("Turnus kills Aeneas.", "No."),
                                                                                  ("The poem never mentions mercy.", "Anchises does.")],
    "parcere subiectis vs. the final blow.", "A tension between ideal and act.",
    ["parcere subiectis … ferrum condit."])

G.sec("Task kit: the Short Answer (Q1) on Vergil")
G.tex(r"""
\begin{terms}
Scansion & mark elisions first; then syllables long by position; foot 5 is usually D, foot 6 two syllables \\
Case and use & name both: ``imperio: ablative of means'' \\
Referent & who is ``alii''? who speaks? to whom? \\
Device & name it and quote the words \\
Context & Anchises speaks to Aeneas in the Underworld; Rome; Augustus \\
\end{terms}

\begin{trap}
In scansion, a vowel before two consonants is long by position even if short by nature, but a mute + liquid (pr, tr, cl) may leave it short. And remember elision: \emph{regere imperio} is scanned \emph{reger' imperio}.
\end{trap}
""")
G.q("5 Short Answer", r"How is \emph{tu regere imperio populos, Romane, memento} scanned in feet 1--4?",
    "DDDS", [("DSDS", "Foot 2 (r'imperi) is a dactyl after elision."),
             ("SDDS", "Foot 1 (tu rege) is a dactyl."),
             ("DDSS", "Foot 3 (o popu) is a dactyl.")],
    "tu rege | r'imperi | o popu | los Ro | mane me | mento.", "Elide regere before imperio.",
    ["– u u | – u u | – u u | – – | – u u | – –."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 5: Vergil's Aeneid, Books 4, 6, 7, 11 and 12: Question Set", r"Unit 5 \textperiodcentered\ Question Set",
        abstract=r"""Three sets and four discrete questions in the exam's formats: a long set on \emph{Aeneid} 4.305--316 (Dido confronts Aeneas), a short syllabus set on 6.469--471 (Dido's silence), a short sight set on 6.268--272 (the descent), and four discrete sight sentences, followed by a Short Answer question (8 points) on 6.847--853 with the scoring guide. Questions are in English, as on the exam; Latin is quoted without macrons. Allow about 25 minutes for the multiple choice and 15 for the short answer.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Short Answer: \blank\ / 8 \qquad Target: 15+ MCQ and 6+ short answer",
        short="Unit 5", sub="Vergil's Aeneid, Books 4, 6, 7, 11 and 12")

Q.sec("Long set: Aeneid 4.305-316")
Q.src(r"Long set (syllabus poetry) \textperiodcentered\ Vergil, \emph{Aeneid} 4.305--316", [
    r"`dissimulare etiam sperasti, perfide, tantum\\ posse nefas tacitusque mea decedere terra?\\ nec te noster amor nec te data dextera quondam\\ nec moritura tenet crudeli funere Dido?\\ quin etiam hiberno moliri sidere classem\\ et mediis properas Aquilonibus ire per altum,\\ crudelis? quid, si non arva aliena domosque\\ ignotas peteres, et Troia antiqua maneret,\\ Troia per undosum peteretur classibus aequor?\\ mene fugis? per ego has lacrimas dextramque tuam te\\ (quando aliud mihi iam miserae nihil ipsa reliqui),\\ per conubia nostra, per inceptos hymenaeos [\ldots]'",
], 10, note="dissimulo, -are: to conceal. moliri: to prepare. hibernus, -a, -um: wintry. Aquilo, -onis, m.: north wind. hymenaeus, -i, m.: wedding.")
Q.q("1.C Summary", r"What does Dido accuse Aeneas of hoping in lines 1--2?",
    "that he could hide so great a wrong and leave her land in silence", [("that he could marry her secretly", "No."),
                                                                          ("that he could bring her to Italy", "No."),
                                                                          ("that she would forgive him", "Not stated.")],
    "dissimulare … tacitus … decedere.", "Indirect statement after sperasti.",
    ["tantum nefas."])
Q.q("1.A Meaning", r"\emph{perfide} (line 1) means",
    "traitor", [("perfect one", "Perfidus = faithless."),
                ("friend", "No."),
                ("stranger", "No.")],
    "perfidus = treacherous.", "Vocative of perfidus.",
    ["per + fides → breaking faith."])
Q.q("2.A Style", r"\emph{nec te \ldots\ nec te \ldots\ nec} (lines 3--4) is",
    "anaphora in a tricolon", [("chiasmus", "No ABBA."),
                               ("simile", "No."),
                               ("litotes", "No.")],
    "nec … nec … nec.", "Three bonds that should hold him: love, the pledge, her coming death.",
    ["amor, dextera, Dido moritura."])
Q.q("1.B Grammar", r"\emph{moritura} (line 4) agrees with",
    "Dido", [("dextera", "Different referent."),
             ("funere", "Funere is ablative neuter."),
             ("amor", "Masculine.")],
    "Dido moritura.", "Future active participle: Dido, about to die.",
    ["moritura … Dido."])
Q.q("1.C Summary", r"What does Dido say Aeneas is hurrying to do in lines 5--6?",
    "to sail across the deep in the middle of winter's north winds", [("to fight Turnus", "No."),
                                                                      ("to return to Troy", "No."),
                                                                      ("to build a new city in Carthage", "No.")],
    "hiberno … sidere … mediis Aquilonibus.", "Leaving in winter storms shows his haste.",
    ["ire per altum."])
Q.q("1.D Translation", r"\emph{quid, si non arva aliena domosque / ignotas peteres, et Troia antiqua maneret} is best translated",
    "what if you were not seeking foreign fields and unknown homes, and ancient Troy still stood", [("what if you sought foreign fields and Troy fell", "Non and maneret are missed."),
                                                                                                    ("why did you seek unknown homes in ancient Troy", "Wrong structure."),
                                                                                                    ("if Troy had remained, you would have sought foreign fields", "Wrong sense.")],
    "Contrary-to-fact (imperfect subjunctive).", "She argues he would not sail even to Troy in winter.",
    ["peteres, maneret: imperfect subjunctive."])
Q.q("1.C Inference", r"What is Dido's point in lines 7--9?",
    "Even to reach Troy itself he would not sail in such weather, so his haste shows he is fleeing her.", [("She wants him to return to Troy.", "A hypothetical argument."),
                                                                                                         ("She thinks Troy is still standing.", "Contrary to fact."),
                                                                                                         ("She will go with him.", "No.")],
    "Argument a fortiori.", "If not for Troy, why for Italy, unless to escape her?",
    ["Troia per undosum peteretur …?"])
Q.q("2.A Style", r"\emph{per ego has lacrimas dextramque tuam te} (line 10) separates \emph{per} from \emph{te} and inserts \emph{ego}. This word order",
    "places Dido's plea and her own self between the preposition and its object", [("is a simile", "No comparison."),
                                                                                   ("shows Dido is calm", "The order is broken and emotional."),
                                                                                   ("is a scansion error", "No.")],
    "Hyperbaton in an oath.", "per … te: ``by these tears… I beg you''.",
    ["per … oro te."])
Q.q("1.B Grammar", r"\emph{mene fugis?} (line 10) means",
    "Is it from me that you flee?", [("Do you flee to me?", "Me is the object of fugis."),
                                    ("I flee from you.", "Fugis is second person."),
                                    ("You fled me yesterday.", "Present tense.")],
    "me + -ne.", "A question stressing ``me''.",
    ["fugio + acc. = flee from."])
Q.q("2.B Context", r"Why does Dido invoke \emph{conubia nostra} and \emph{inceptos hymenaeos}?",
    "She considers their union a marriage, which Aeneas is breaking.", [("She plans to marry Iarbas.", "No."),
                                                                         ("She is inviting him to a wedding feast.", "No."),
                                                                         ("She speaks of her marriage to Sychaeus.", "These are with Aeneas.")],
    "conubium = marriage.", "After the cave scene, Dido calls it coniugium (4.172).",
    ["per conubia nostra."])

Q.sec("Short set: Aeneid 6.469-471")
Q.src(r"Short set (syllabus poetry) \textperiodcentered\ Vergil, \emph{Aeneid} 6.469--471", [
    r"illa solo fixos oculos aversa tenebat\\ nec magis incepto vultum sermone movetur\\ quam si dura silex aut stet Marpesia cautes.",
], 3, note="silex, -icis, m./f.: flint. Marpesius, -a, -um: of Marpesus (a mountain famous for marble). cautes, -is, f.: crag.")
Q.q("1.C Summary", r"Where does Dido keep her eyes?",
    "fixed on the ground", [("on Aeneas's face", "Aversa = turned away."),
                            ("on Sychaeus", "Not yet."),
                            ("on the sky", "No.")],
    "solo fixos oculos.", "Solo: dative/ablative, on the ground.",
    ["aversa tenebat."])
Q.q("2.A Style", r"The comparison in line 3 likens Dido to",
    "hard flint or a Marpesian crag", [("a cloud", "No."),
                                       ("a flower", "No."),
                                       ("a burning fire", "No.")],
    "Simile of stone.", "Her stony silence answers his tears.",
    ["quam si dura silex."])
Q.q("1.C Inference", r"What does the simile suggest about Dido's feelings toward Aeneas?",
    "She is unmoved and will not forgive him.", [("She longs to speak with him.", "She turns away."),
                                                 ("She is frightened of him.", "Not suggested."),
                                                 ("She does not recognize him.", "She hears his words.")],
    "Unmoved.", "Inference from the image of stone.",
    ["nec … movetur."])

Q.sec("Short set: sight poetry")
Q.src(r"Short set (sight poetry) \textperiodcentered\ Vergil, \emph{Aeneid} 6.268--272", [
    r"Ibant obscuri sola sub nocte per umbram\\ perque domos Ditis vacuas et inania regna:\\ quale per incertam lunam sub luce maligna\\ est iter in silvis, ubi caelum condidit umbra\\ Iuppiter, et rebus nox abstulit atra colorem.",
], 3, note="Dis, Ditis, m.: Pluto, god of the Underworld. malignus, -a, -um: grudging, faint.")
Q.q("2.A Style", r"\emph{Ibant obscuri sola sub nocte} is often cited as an example of",
    "transferred epithet (hypallage): ``obscure'' belongs to the night, ``alone'' to the travelers", [("onomatopoeia", "No sound imitation."),
                                                                                                    ("chiasmus", "No."),
                                                                                                    ("apostrophe", "No.")],
    "Hypallage.", "The adjectives seem swapped: dark travelers, lonely night.",
    ["obscuri (they) / sola (night)."])
Q.q("1.C Summary", r"To what is the journey compared in lines 3--5?",
    "a walk in the woods by faint, uncertain moonlight when Jupiter has hidden the sky", [("a sea voyage in a storm", "No."),
                                                                                        ("a battle at night", "No."),
                                                                                        ("a feast in a palace", "No.")],
    "quale … iter in silvis.", "Simile of dim moonlight.",
    ["per incertam lunam."])
Q.q("1.D Translation", r"\emph{rebus nox abstulit atra colorem} is best translated",
    "black night has taken color away from things", [("things took away the black night's color", "Nox is the subject."),
                                                     ("night brought black color to things", "Abstulit = took away."),
                                                     ("the black color of things removed the night", "No.")],
    "rebus: dative of separation.", "aufero: take away from (dat.).",
    ["abstulit < aufero."])

Q.sec("Discrete sight questions")
Q.q("1.D Translation", r"\emph{Si Dido Aeneam retinuisset, Roma numquam condita esset.} This sentence means",
    "If Dido had held Aeneas back, Rome would never have been founded.", [("If Dido holds Aeneas back, Rome will never be founded.", "Pluperfect subjunctive: past contrary to fact."),
                                                                          ("Dido held Aeneas back, so Rome was founded.", "No."),
                                                                          ("If Rome had been founded, Dido would have kept Aeneas.", "Reversed.")],
    "Past contrary-to-fact.", "si + pluperfect subjunctive in both clauses.",
    ["retinuisset, condita esset."])
Q.q("1.B Grammar", r"In \emph{Turnus, ut regnum sibi pararet, bellum gessit}, \emph{ut \ldots\ pararet} is",
    "a purpose clause", [("a result clause", "No tam/ita; the sense is purpose."),
                         ("an indirect question", "No."),
                         ("a temporal clause with ut = when", "Ut + subjunctive here expresses aim.")],
    "ut + subjunctive = purpose.", "Turnus waged war to win the kingdom.",
    ["sibi = for himself."])
Q.q("1.A Meaning", r"In \emph{Camilla hastam validam manu torsit}, \emph{torsit} means",
    "hurled", [("carried", "That is portavit."),
               ("broke", "That is fregit."),
               ("hid", "That is celavit.")],
    "torqueo = twist, hurl.", "Camilla, the warrior.",
    ["torsit < torqueo."])
Q.q("1.D Translation", r"\emph{Iuno, quamquam irata erat, Iovi tandem paruit.} This sentence means",
    "Although Juno was angry, she finally obeyed Jupiter.", [("Because Juno was angry, Jupiter obeyed her.", "Iovi is dative with paruit."),
                                                            ("Juno was angry at last with Jupiter.", "No."),
                                                            ("Jupiter, although angry, obeyed Juno.", "Iuno is the subject.")],
    "pareo + dative.", "Iovi = to Jupiter.",
    ["paruit Iovi."])

Q.frq(kind="Short Answer", head=r"Question 1 \textperiodcentered\ Short Answer \textperiodcentered\ 8 points \textperiodcentered\ about 15 minutes", mins=15,
      directions=[r"Read the passage, then answer the questions in English unless a question asks for Latin."],
      sources=[dict(title=r"Vergil, \emph{Aeneid} 6.847--853", paras=[
          r"excudent alii spirantia mollius aera\\ (credo equidem), vivos ducent de marmore vultus,\\ orabunt causas melius, caelique meatus\\ describent radio et surgentia sidera dicent:\\ tu regere imperio populos, Romane, memento\\ (hae tibi erunt artes), pacique imponere morem,\\ parcere subiectis et debellare superbos.",
          r"\emph{excudo, -ere}: to hammer out, cast \quad \emph{aes, aeris, n.}: bronze \quad \emph{meatus, -us, m.}: course, movement \quad \emph{radius, -i, m.}: measuring rod \quad \emph{debello, -are}: to subdue in war"])],
      prompt=[r"A. (i) Translate in context \emph{excudent alii spirantia mollius aera} (line 1). (ii) Identify the people whom Vergil means by \emph{alii}.",
              r"B. Identify one and only one of the arts that the \emph{alii} will practice in lines 2--4 (\emph{vivos \ldots\ dicent}).",
              r"C. Identify the case and use of \emph{imperio} (line 5).",
              r"D. Identify the case of \emph{Romane} (line 5).",
              r"E. Indicate the scansion of the first four feet of line 5: \emph{tu regere imperio populos, Romane, memento}.",
              r"F. Translate \emph{parcere subiectis et debellare superbos} (line 7).",
              r"G. Identify who speaks these lines, and to whom."],
      model=[r"A. (i) Others will hammer out (cast) more softly breathing bronzes. (ii) The Greeks.",
             r"B. Carving lifelike faces from marble (or pleading cases better, or charting the movements of the heavens, or naming the rising stars).",
             r"C. Ablative of means.",
             r"D. Vocative.",
             r"E. DDDS: tu rege | r' imperi | o popu | los Ro | (mane me | mento).",
             r"F. To spare the conquered and to subdue the proud.",
             r"G. Anchises, speaking to his son Aeneas in the Underworld."],
      rows=[("A(i) Translation", 1, "others will cast more softly breathing (lifelike) bronzes", "missing the future tense or the comparative"),
            ("A(ii) Referent", 1, "the Greeks", "the Trojans; the gods"),
            ("B One art", 1, "sculpture in marble, oratory, astronomy (one only)", "listing several"),
            ("C Case and use", 1, "ablative of means (by command, rule)", "dative; ablative of place"),
            ("D Case", 1, "vocative", "nominative"),
            ("E Scansion", 1, "DDDS (with elision of regere before imperio)", "no elision; foot errors"),
            ("F Translation", 1, "to spare the conquered (subjected) and to subdue (war down) the proud", "wrong roles: the proud spare"),
            ("G Speaker", 1, "Anchises to Aeneas, in the Underworld", "Jupiter to Juno")],
      tips=["A(ii) uses context: Greek achievements in sculpture, oratory and astronomy.", "E marks the elision first.", "B gives exactly one art."],
      ask="Answer each part in English, then mark each row.", lines=12)

GUIDE, QSET = G, Q
