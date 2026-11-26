from ap_wl.model import Doc

STEM = "02-pliny-vesuvius"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 2: Pliny's Letters: The Eruption of Vesuvius", r"Unit 2 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 2 reads Pliny's two letters to the historian Tacitus about the eruption of Vesuvius in 79 CE: 6.16, on the death of his uncle Pliny the Elder, and 6.20, on his own and his mother's escape from Misenum. This guide sets out the historical context, the structure of each letter section by section with the key Latin, the themes the exam asks about (heroism and Stoic calm, memory and fame, the power of nature, Pliny's self-portrait), the style that makes these letters vivid, and a Short Answer kit. Latin is quoted without macrons from a public-domain text. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Latin I can cite: \blank[10em]",
        short="Unit 2", sub="Pliny's Letters: The Eruption of Vesuvius")

G.sec("Context: August 79 CE")
G.tex(r"""
\begin{compare}{Fact}{Detail}{In the letters}
Date & ``Nonum Kal. Septembres'': August 24, 79 CE (a date some scholars now place in autumn) & 6.16.4 \\
Place & Misenum, base of the Roman fleet on the Bay of Naples; Stabiae, Pompeii and Herculaneum to the southeast & 6.16.4, 12 \\
Pliny the Elder & admiral of the fleet (\emph{classem imperio praesens regebat}), author of the \emph{Natural History} & 6.16 \\
Pliny the Younger & about 17, at Misenum with his mother & 6.20 \\
Tacitus & the historian, who asked for an account for his \emph{Histories} & 6.16.1, 6.20.1 \\
\end{compare}

\textbf{Purpose.} ``Petis ut tibi avunculi mei exitum scribam, quo verius tradere posteris possis'' (6.16.1): Pliny writes so that Tacitus may hand down an accurate account to posterity, and so that his uncle's death may win ``immortalem gloriam''.
""")
G.q("1 Context", r"Why does Pliny write letter 6.16?",
    "Tacitus asked for an account of his uncle's death to use in his history.", [("Trajan ordered a report on the eruption.", "The letters are to Tacitus."),
                                                                                 ("His mother asked him to record the event.", "No."),
                                                                                 ("He wanted to describe Pompeii's buildings.", "Not the purpose.")],
    "Petis ut … scribam.", "The letter answers Tacitus's request (6.16.1).",
    ["quo verius tradere posteris possis."])
G.q("1 Context", r"What was Pliny the Elder's position at Misenum?",
    "commander of the Roman fleet", [("governor of Bithynia", "That was his nephew, later."),
                                      ("priest of Neptune", "No."),
                                      ("mayor of Pompeii", "No.")],
    "classem … regebat.", "He commanded the fleet stationed at Misenum.",
    ["praesens regebat."])

G.sec("Letter 6.16: the death of Pliny the Elder")
G.tex(r"""
\begin{compare}{Sections}{What happens}{Key Latin}
1--3 & purpose; praise of the uncle, who wrote and did things worth recording & ``immortalem gloriam'' \\
4--6 & his sister reports a strange cloud; it rises from Vesuvius, shaped like a pine tree & ``nubem inusitata et magnitudine et specie''; ``non alia magis arbor quam pinus'' \\
7--10 & he plans to observe it scientifically; a note from Rectina asks for rescue; he turns the expedition into a rescue & ``Vertit ille consilium''; ``Properat illuc unde alii fugiunt'' \\
11--15 & ash and stones fall on the ships; ``Fortes fortuna iuvat''; at Stabiae with Pomponianus he bathes, dines and sleeps to calm others & ``aut hilaris aut \ldots\ similis hilari'' \\
16--20 & they go out with pillows on their heads; on the shore he collapses and dies; his body is found intact & ``quiescenti quam defuncto similior'' \\
21--22 & Pliny stops: a letter is not a history & ``aliud est enim epistulam aliud historiam'' \\
\end{compare}
""")
G.q("2 Letter 6.16", r"What does \emph{Vertit ille consilium} mark in Pliny the Elder's actions?",
    "his change from a scientific expedition to a rescue mission", [("his decision to flee from the cloud", "He heads toward danger."),
                                                                     ("his refusal to help Rectina", "He helps her."),
                                                                     ("his decision to write a book about the eruption", "No.")],
    "From study to rescue.", "After Rectina's note, he launches the quadriremes to bring help.",
    ["quod studioso animo incohaverat obit maximo."])
G.q("2 Letter 6.16", r"Why does the Elder bathe, dine and sleep at Pomponianus's house?",
    "to calm the frightened Pomponianus by showing his own composure", [("because he did not understand the danger", "Pliny presents it as deliberate."),
                                                                        ("because he was injured", "No."),
                                                                        ("because Pomponianus ordered him to", "No.")],
    "utque timorem eius sua securitate leniret.", "Stoic calm as leadership.",
    ["purpose clause: to soothe his fear."])

G.sec("Letter 6.20: Pliny and his mother at Misenum")
G.tex(r"""
\begin{compare}{Sections}{What happens}{Key Latin}
1 & Pliny begins, echoing Aeneas's words before telling the fall of Troy & ``Quamquam animus meminisse horret, \ldots\ incipiam'' (\emph{Aeneid} 2.12--13) \\
2--10 & earthquakes; he keeps reading Livy; at dawn they leave the town; the sea draws back; a black cloud & ``Iam dies\ldots'' \\
11--12 & his mother begs him to flee without her; he refuses & ``Ego contra salvum me nisi una non futurum'' \\
13--17 & darkness ``qualis in locis clausis lumine exstincto''; shrieks and prayers; ash they shake off & ``Audires ululatus feminarum'' \\
18--20 & the light returns, everything covered in ash ``tamquam nive''; they wait for news of the uncle & ``Haec nequaquam historia digna'' \\
\end{compare}
""")
G.q("3 Letter 6.20", r"What does Pliny refuse to do when his mother urges him to flee?",
    "to save himself without her", [("to read Livy", "He had been reading earlier."),
                                     ("to return to Misenum", "They return later."),
                                     ("to write to Tacitus", "No.")],
    "salvum me nisi una non futurum.", "He will not be saved unless together with her: pietas toward his mother.",
    ["una = together."])
G.q("3 Letter 6.20", r"Pliny opens 6.20 with words of Aeneas from \emph{Aeneid} 2. What is the effect?",
    "He casts his own escape as an epic story of a city's destruction, like Aeneas telling the fall of Troy.", [
        ("He shows he has not read Vergil.", "The opposite."),
        ("He criticizes Aeneas.", "No."),
        ("He announces that his uncle survived.", "No.")],
    "Intertext.", "Quamquam animus meminisse horret… incipiam: Pliny becomes a narrator like Aeneas.",
    ["Aeneid 2.12–13."])

G.sec("Themes and style")
G.tex(r"""
\begin{compare}{Theme or feature}{Evidence}{What to say}
Heroism and Stoic calm & ``Fortes fortuna iuvat''; the bath, dinner and sleep & virtus shown in action and composure \\
Memory and fame & ``immortalem gloriam''; writing for posterity & literature confers immortality \\
Nature's power & the pine-tree cloud; ``torrentis modo''; darkness ``lumine exstincto'' & vivid similes make the unseen visible \\
Religion & ``plures nusquam iam deos ullos'' & many believed the gods were gone and the world ending \\
Pliny's self-portrait & a 17-year-old reading Livy, loyal to his mother & modest on the surface, flattering underneath \\
Historical present & ``poscit soleas, ascendit locum'' & vividness and speed \\
Tricolon, asyndeton & ``orare hortari iubere''; ``ululatus feminarum, infantum quiritatus, clamores virorum'' & urgency, chaos \\
\end{compare}
""")
G.q("4 Themes", r"In \emph{Tum mater orare hortari iubere}, the infinitives are historical infinitives in",
    "asyndeton, a rising tricolon of pleas", [("polysyndeton", "No conjunctions."),
                                               ("chiasmus", "No ABBA pattern."),
                                               ("indirect statement", "They are historical infinitives (= imperfects).")],
    "begging, urging, ordering.", "The series intensifies the mother's pleas.",
    ["orare → hortari → iubere."])
G.q("4 Themes", r"What does \emph{plures nusquam iam deos ullos \ldots\ interpretabantur} report?",
    "Many believed there were no gods anywhere any longer.", [("Most people prayed to the gods for help.", "Multi prayed; plures thought the gods were gone."),
                                                               ("Pliny became a priest.", "No."),
                                                               ("The gods appeared in the sky.", "No.")],
    "nusquam deos ullos.", "A last night for the world: religious despair.",
    ["plures > multi."])

G.sec("Task kit: the Short Answer (Q1) on Pliny")
G.tex(r"""
\begin{compare}{Subquestion type}{How to answer}{Example}
Translate in context & a literal translation of the phrase as used & \emph{Audires ululatus feminarum}: ``you could have heard the shrieks of women'' \\
Identify case or use & name the case and the use & \emph{metu}: ablative of cause \\
Identify a referent & who or what a pronoun or word refers to & \emph{ille} = Pliny the Elder \\
One and only one & give exactly one item; extra items may cancel the point & ``one group that searched'' \\
Device & name it and point to the words & tricolon: \emph{alii parentes alii liberos alii coniuges} \\
Context & a fact about Roman culture or history & the fleet at Misenum; Tacitus's \emph{Histories} \\
\end{compare}
""")
G.q("5 Short Answer", r"A subquestion asks for ``one and only one'' group the people searched for. A student writes ``parents, children and wives''. What happens?",
    "The response may not earn the point, because it does not give just one.", [("It earns three points.", "Each subquestion is one point."),
                                                                                ("It always earns the point.", "Extra answers can cancel credit."),
                                                                                ("It earns half a point.", "No half points.")],
    "Answer exactly what is asked.", "Follow the instruction to give one and only one.",
    ["one item only."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 2: Pliny's Letters: The Eruption of Vesuvius: Question Set", r"Unit 2 \textperiodcentered\ Question Set",
        abstract=r"""Three sets and four discrete questions in the exam's formats: a long set on 6.16.4--5 (the cloud), a short syllabus set on 6.16.10, a short sight set on Pliny 1.6 (the boar hunt), and four discrete sight sentences, followed by a Short Answer question (8 points) on 6.20.14--15 with the scoring guide. Questions are in English, as on the exam; Latin is quoted without macrons. Allow about 25 minutes for the multiple choice and 15 for the short answer.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Short Answer: \blank\ / 8 \qquad Target: 15+ MCQ and 6+ short answer",
        short="Unit 2", sub="Pliny's Letters: The Eruption of Vesuvius")

Q.sec("Long set: Pliny, Epistulae 6.16")
Q.src(r"Long set (syllabus prose) \textperiodcentered\ Pliny, \emph{Epistulae} 6.16.4--5", [
    r"Erat Miseni classemque imperio praesens regebat. Nonum Kal. Septembres hora fere septima mater mea indicat ei apparere nubem inusitata et magnitudine et specie. Usus ille sole, mox frigida, gustaverat iacens studebatque; poscit soleas, ascendit locum ex quo maxime miraculum illud conspici poterat. Nubes --- incertum procul intuentibus ex quo monte; Vesuvium fuisse postea cognitum est --- oriebatur, cuius similitudinem et formam non alia magis arbor quam pinus expresserit.",
], 10, note="Misenum, -i, n.: Misenum (locative Miseni). Kal. = Kalendas. frigida (aqua): a cold bath. soleae, -arum, f. pl.: sandals. pinus, -us, f.: pine tree.")
Q.q("1.B Grammar", r"\emph{Miseni} is in the",
    "locative case: ``at Misenum''", [("genitive: ``of Misenum''", "With a town name and erat, the form is locative."),
                                      ("nominative plural", "Misenum is singular."),
                                      ("dative: ``to Misenum''", "No.")],
    "Locative.", "Town names use the locative for ``at''.",
    ["Erat Miseni = he was at Misenum."])
Q.q("1.C Summary", r"What was Pliny the Elder doing at Misenum?",
    "commanding the fleet in person", [("building ships", "No."),
                                       ("visiting his sister for a holiday", "He commanded the fleet."),
                                       ("observing Vesuvius from a tower", "Later he climbed to look.")],
    "classemque imperio praesens regebat.", "Detail.",
    ["regebat = was commanding."])
Q.q("1.C Summary", r"Who first told him about the cloud?",
    "Pliny's mother, his sister", [("Rectina", "Her note comes later."),
                                   ("Tacitus", "No."),
                                   ("a sailor of the fleet", "No.")],
    "mater mea indicat.", "Pliny's mother was the Elder's sister.",
    ["mater mea."])
Q.q("1.B Grammar", r"\emph{inusitata et magnitudine et specie} is best translated",
    "unusual in both size and appearance", [("used both for size and for show", "Inusitata = unusual."),
                                            ("and the size and appearance were usual", "No."),
                                            ("by unusual size and by a species", "Ablative of respect, not means.")],
    "Ablative of respect.", "et … et = both … and.",
    ["magnitudine, specie: ablatives of respect."])
Q.q("1.C Summary", r"What had the Elder done before he heard about the cloud?",
    "He had sunbathed, taken a cold bath, eaten while lying down and was studying.", [("He had sailed to Stabiae.", "That comes later."),
                                                                                      ("He had climbed Vesuvius.", "No."),
                                                                                      ("He had written a letter to Tacitus.", "No.")],
    "Usus ille sole, mox frigida, gustaverat iacens studebatque.", "His ordinary routine, interrupted.",
    ["sun → cold bath → light meal → study."])
Q.q("1.B Grammar", r"\emph{poscit soleas, ascendit locum} are in the present tense to",
    "make the narration vivid (historical present)", [("show the actions are still happening as Pliny writes", "Historical present narrates past events vividly."),
                                                      ("express a command", "They are indicative."),
                                                      ("describe the future", "No.")],
    "Historical present.", "2.A/1.B: a narrative technique.",
    ["poscit, ascendit."])
Q.q("1.D Translation", r"\emph{ex quo maxime miraculum illud conspici poterat} is best translated",
    "from which that wonder could best be seen", [("from which he could see that greatest wonder", "Conspici is passive; maxime is an adverb."),
                                                  ("from which the wonder was seen by most people", "No."),
                                                  ("which could see the wonder from far away", "No.")],
    "conspici = to be seen.", "Passive infinitive with poterat.",
    ["conspicio → conspici."])
Q.q("1.C Summary", r"According to the passage, what was uncertain to those watching from afar?",
    "from which mountain the cloud was rising", [("whether the cloud was real", "No."),
                                                 ("when the eruption would end", "No."),
                                                 ("who commanded the fleet", "No.")],
    "incertum … ex quo monte.", "Only later was it known to be Vesuvius.",
    ["Vesuvium fuisse postea cognitum est."])
Q.q("2.A Style", r"In comparing the cloud to a pine tree, Pliny uses",
    "a comparison that helps the reader visualize an unfamiliar sight", [("a pun on the word nubes", "No."),
                                                                         ("a metaphor for his uncle's death", "Not here."),
                                                                         ("a prayer to the gods", "No.")],
    "Pine-tree comparison.", "2.A: the famous image of a column with spreading branches.",
    ["non alia magis arbor quam pinus."])
Q.q("1.B Grammar", r"\emph{Vesuvium fuisse postea cognitum est} contains",
    "an indirect statement depending on cognitum est", [("an ablative absolute", "Vesuvium (acc.) + fuisse (inf.)."),
                                                         ("a purpose clause", "No."),
                                                         ("a result clause", "No.")],
    "Accusative + infinitive.", "``It was learned later that it had been Vesuvius.''",
    ["cognitum est + Vesuvium fuisse."])

Q.sec("Short set: Pliny, Epistulae 6.16")
Q.src(r"Short set (syllabus prose) \textperiodcentered\ Pliny, \emph{Epistulae} 6.16.10", [
    r"Properat illuc unde alii fugiunt, rectumque cursum recta gubernacula in periculum tenet adeo solutus metu, ut omnes illius mali motus omnes figuras ut deprenderat oculis dictaret enotaretque.",
], 3, note="gubernaculum, -i, n.: rudder. deprendo, -ere, -di: to catch sight of. enoto, -are: to note down.")
Q.q("2.A Style", r"\emph{Properat illuc unde alii fugiunt} emphasizes the Elder's courage through",
    "a contrast between his movement and everyone else's", [("a simile", "No comparison word."),
                                                            ("an apostrophe", "No address."),
                                                            ("a tricolon", "Two parts, not three.")],
    "illuc / unde; properat / fugiunt.", "Antithesis shows his courage.",
    ["he hurries where others flee."])
Q.q("1.B Grammar", r"\emph{adeo solutus metu, ut \ldots\ dictaret} contains",
    "a result clause", [("a purpose clause", "Adeo … ut signals result."),
                        ("a fear clause", "No verb of fearing."),
                        ("an indirect command", "No.")],
    "adeo … ut.", "So free from fear that he dictated…",
    ["result clause."])
Q.q("1.C Summary", r"What did the Elder do as he sailed?",
    "He dictated notes on every movement and shape of the disaster.", [("He hid below deck.", "No."),
                                                                       ("He prayed to Neptune.", "No."),
                                                                       ("He ordered the ships to turn back.", "Not here.")],
    "dictaret enotaretque.", "The scientist observes even in danger.",
    ["omnes … motus omnes figuras."])

Q.sec("Short set: sight prose")
Q.src(r"Short set (sight prose) \textperiodcentered\ Pliny, \emph{Epistulae} 1.6.1 (to Tacitus)", [
    r"Ridebis, et licet rideas. Ego, ille quem nosti, apros tres et quidem pulcherrimos cepi. `Ipse?' inquis. Ipse; non tamen ut omnino ab inertia mea et quiete discederem.",
], 3, note="aper, apri, m.: wild boar. inertia, -ae, f.: inactivity.")
Q.q("1.C Summary", r"What does Pliny tell Tacitus he did?",
    "He caught three very fine boars.", [("He wrote three books.", "No."),
                                         ("He laughed at three friends.", "No."),
                                         ("He ran away from boars.", "No.")],
    "apros tres … cepi.", "Detail.",
    ["cepi = I caught."])
Q.q("1.D Translation", r"\emph{Ridebis, et licet rideas} is best translated",
    "You will laugh, and you are allowed to laugh.", [("You laughed, and he laughs.", "Future and subjunctive."),
                                                      ("Laugh, and let them laugh.", "No imperative."),
                                                      ("You will laugh, but you may not.", "Licet = it is allowed.")],
    "licet + subjunctive.", "Playful opening of a letter.",
    ["ridebis (fut.), rideas (subj.)."])
Q.q("2.A Style", r"What is the tone of the passage?",
    "playful and self-mocking", [("tragic", "No."),
                                 ("angry", "No."),
                                 ("formal and official", "This is a light letter to a friend.")],
    "Ego, ille quem nosti.", "Pliny jokes that a man known for inactivity hunted.",
    ["Ridebis … Ipse?"])

Q.sec("Discrete sight questions")
Q.q("1.D Translation", r"\emph{Nautae, quamvis mare saeviret, navem in portum duxerunt.} This sentence means",
    "Although the sea was raging, the sailors led the ship into the harbor.", [("Because the sea was raging, the sailors left the harbor.", "Quamvis = although."),
                                                                               ("The sailors raged at the sea in the harbor.", "Saeviret's subject is mare."),
                                                                               ("The ship led the sailors into the harbor.", "Navem is the object.")],
    "quamvis + subjunctive.", "Concessive clause.",
    ["quamvis = although."])
Q.q("1.B Grammar", r"In \emph{Cinere decidente, cives fugerunt}, \emph{cinere decidente} is",
    "an ablative absolute: ``as the ash was falling''", [("the subject of fugerunt", "Cives is the subject."),
                                                        ("a dative of purpose", "No."),
                                                        ("an indirect statement", "No.")],
    "noun + present participle, ablative.", "Present participle: simultaneous action.",
    ["cinis, cineris → cinere."])
Q.q("1.A Meaning", r"In \emph{Mater filium monuit ne domum rediret}, \emph{monuit} means",
    "warned", [("remembered", "That is meminit."),
               ("built", "That is struxit."),
               ("moved", "That is movit.")],
    "moneo = warn.", "monere ne + subjunctive: indirect command.",
    ["warned him not to return."])
Q.q("1.D Translation", r"\emph{Tanta erat caligo ut nemo viam videre posset.} This sentence means",
    "The darkness was so great that no one could see the road.", [("The darkness was great so that no one would see the road.", "Tanta … ut marks result, not purpose."),
                                                                  ("No one saw the great darkness on the road.", "No."),
                                                                  ("The road was so dark that no one walked.", "No.")],
    "tanta … ut.", "Result clause.",
    ["so great that…"])

Q.frq(kind="Short Answer", head=r"Question 1 \textperiodcentered\ Short Answer \textperiodcentered\ 8 points \textperiodcentered\ about 15 minutes", mins=15,
      directions=[r"Read the passage, then answer the questions in English unless a question asks for Latin."],
      sources=[dict(title=r"Pliny, \emph{Epistulae} 6.20.14--15", paras=[
          r"Audires ululatus feminarum, infantum quiritatus, clamores virorum; alii parentes alii liberos alii coniuges vocibus requirebant, vocibus noscitabant; hi suum casum, illi suorum miserabantur; erant qui metu mortis mortem precarentur; multi ad deos manus tollere, plures nusquam iam deos ullos aeternamque illam et novissimam noctem mundo interpretabantur.",
          r"\emph{ululatus, -us, m.}: shriek \quad \emph{quiritatus, -us, m.}: wail \quad \emph{noscito, -are}: to recognize \quad \emph{interpretor, -ari}: to understand, believe"])],
      prompt=[r"A. (i) Translate in context \emph{Audires ululatus feminarum}. (ii) Identify the mood of \emph{Audires}.",
              r"B. Identify one and only one group of people whom the survivors searched for.",
              r"C. Identify the stylistic device in \emph{alii parentes alii liberos alii coniuges}.",
              r"D. Translate \emph{erant qui metu mortis mortem precarentur}.",
              r"E. Identify the case and use of \emph{metu}.",
              r"F. According to the passage, what did many people (\emph{plures}) believe about the gods?",
              r"G. Pliny wrote this letter at the request of a famous historian. Identify the historian."],
      model=[r"A. (i) You could have heard the shrieks of women. (ii) Subjunctive (potential).",
             r"B. Parents (or children, or spouses).",
             r"C. Anaphora (of alii), forming a tricolon.",
             r"D. There were those who, out of fear of death, prayed for death.",
             r"E. Ablative of cause.",
             r"F. That there were no gods anywhere any longer, and that this was the eternal, final night for the world.",
             r"G. Tacitus."],
      rows=[("A(i) Translation", 1, "you could have heard / you would have heard the shrieks of women", "you heard (indicative)"),
            ("A(ii) Mood", 1, "subjunctive", "indicative; tense instead of mood"),
            ("B One group", 1, "parents, or children, or spouses (one only)", "listing more than one"),
            ("C Device", 1, "anaphora (also accept tricolon)", "asyndeton alone"),
            ("D Translation", 1, "there were (those) who prayed for death because of fear of death", "missing the relative clause of characteristic"),
            ("E Case and use", 1, "ablative of cause", "ablative of means; dative"),
            ("F Belief", 1, "no gods anywhere any longer; the eternal last night of the world", "that the gods were helping"),
            ("G Historian", 1, "Tacitus", "Livy (whom Pliny was reading)")],
      tips=["Each answer is short and exact.", "B gives one and only one item.", "D keeps every element: erant qui, metu mortis, mortem precarentur (subjunctive)."],
      ask="Answer each part in English, then mark each row.", lines=12)

GUIDE, QSET = G, Q
