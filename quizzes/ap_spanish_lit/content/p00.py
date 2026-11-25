from ap_wl.model import Doc

STEM = "00-exam-playbook"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Part 0: The Exam and the Analysis Toolkit", r"Part 0 \textperiodcentered\ Study Guide",
        abstract=r"""This guide covers AP Spanish Literature and Culture as described in the College Board's Course and Exam Description (effective fall 2023). The course is built on 38 required works, read in eight chronological units, and six themes. The exam keeps its content and structure; it moves to Bluebook no earlier than May 2027. Section I has 15 listening and 50 reading multiple-choice questions; Section II has two short-answer questions and two essays, all answered in Spanish. The guide sets out what each task asks you to do, how the free-response questions are scored, and the toolkit the exam assumes: literary devices, versification, narrative voice, periods and movements, and the Spanish of literary analysis. Read it before the unit guides; every unit guide ends with a task kit that assumes the rubrics here. Check AP Central for any later change.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 13+ \qquad Devices I still confuse: \blank[10em]",
        short="Part 0", sub="The Exam and the Analysis Toolkit")

G.sec("The exam at a glance")
G.tex(r"""
The exam takes about 3 hours and is entirely in Spanish: questions, answer choices, prompts and your responses.

\begin{compare}{Part}{What you do}{Count, time, weight}
I-A Listening & Three audio sets: an interview with an author, a recited poem not on the list (heard twice), a presentation on a literary topic. & 15 questions, about 20 min, 10\% \\
I-B Reading & Six sets of 7--10 questions on required and non-required texts, including one passage of literary criticism and one pair of thematically related texts. & 50 questions, 60 min, 40\% \\
II Q1 & \textbf{Text Explanation}: identify the author and period of an excerpt from a required work; explain how a theme develops in the whole work. & about 15 min; 7.5\% \\
II Q2 & \textbf{Text and Art Comparison}: compare how a theme appears in a required text and a work of art; connect it to the text's genre, period or movement. & about 15 min; 7.5\% \\
II Q3 & \textbf{Analysis of a Single Text}: analyze how a required text represents a genre and a historical, cultural or social context. & about 35 min; 17.5\% \\
II Q4 & \textbf{Text Comparison}: analyze how two texts (one required, one not) use literary devices to develop a given theme. & about 35 min; 17.5\% \\
\end{compare}

\subsection{Units and themes}
\begin{terms}
Units & 1 La época medieval \textperiodcentered\ 2 El siglo XVI \textperiodcentered\ 3 El siglo XVII \textperiodcentered\ 4 La literatura romántica, realista y naturalista \textperiodcentered\ 5 La Generación del 98 y el Modernismo \textperiodcentered\ 6 Teatro y poesía del siglo XX \textperiodcentered\ 7 El Boom latinoamericano \textperiodcentered\ 8 Escritores contemporáneos de Estados Unidos y España \\
Themes & Las sociedades en contacto \textperiodcentered\ La construcción del género \textperiodcentered\ El tiempo y el espacio \textperiodcentered\ Las relaciones interpersonales \textperiodcentered\ La dualidad del ser \textperiodcentered\ La creación literaria \\
\end{terms}

\begin{keyidea}[What the free response assumes]
Three of the four free-response questions print an excerpt from a \emph{required} work and expect you to know the whole work: its author, period, genre, plot and themes. The list is the syllabus. The eight unit guides in this series cover every required work.
\end{keyidea}
""")
G.q("1 Format", r"Which free-response question asks you to identify the author and period of an excerpt?",
    "Text Explanation", [("Text Comparison", "Text Comparison asks how devices develop a theme in two texts."),
                         ("Analysis of a Single Text", "This essay asks about genre and context; identification is not scored."),
                         ("Text and Art Comparison", "This compares a text with a work of art and connects the theme to genre, period or movement.")],
    "Q1 = identify + explain the theme in the whole work.", "The Text Explanation rubric rewards correctly identifying the period (and the author) and explaining the theme's development.",
    ["Identification appears only in Q1."])
G.q("1 Format", r"How much of the exam score do the two essays carry together?",
    r"35\%", [(r"50\%", "50% is the whole free-response section, including the two short answers."),
              (r"15\%", "15% is the two short answers together."),
              (r"10\%", "10% is the listening part of the multiple choice.")],
    "17.5% + 17.5%.", "Each essay is 17.5%; each short answer 7.5%; together 50%.",
    ["2 × 17.5 = 35."])

G.sec("Multiple choice: listening and reading")
G.tex(r"""
\begin{compare}{Set}{Source}{What the questions target}
Listening: interview & an author talks about writing or a work & the author's views, purpose, context \\
Listening: poem (heard twice) & a recited poem not on the list & theme, tone, imagery, devices \\
Listening: presentation & a talk on a literary topic related to the course & main idea, examples, connections to required works \\
Reading: required work & an excerpt from the list & theme, devices, narrator, context \\
Reading: non-required work & prose, poetry or drama from any period & the same skills applied to new texts \\
Reading: criticism & a critic's analysis of a required work or author & the critic's claim, evidence, attitude \\
Reading: paired texts & one required and one non-required text on one theme & similarities and differences \\
\end{compare}

\begin{trap}
In this series the listening sets are printed as transcripts. Read each one once at normal speed and do not reread before answering. On the exam, the interview and presentation play once and the poem twice; practice with real recordings too.
\end{trap}
""")
G.q("2 Sets", r"Which listening source is played twice on the exam?",
    "the recited poem", [("the interview with an author", "The interview plays once."),
                         ("the presentation on a literary topic", "The presentation plays once."),
                         ("all three sources", "Only the poem is repeated.")],
    "Poem twice.", "The interview and presentation are heard once; the poem twice.",
    ["Poem → twice."])
G.q("2 Sets", r"One reading set always pairs two texts. What do they have in common?",
    "a theme; one text is on the required list and the other is not", [("the same author", "They are related by theme, not author."),
                                                                      ("the same period", "Not necessarily."),
                                                                      ("both are works of criticism", "Only one set is criticism, and it has one passage.")],
    "Paired set = theme link, required + non-required.", "The paired set rehearses the skills of the Text Comparison essay.",
    ["One required + one non-required, same theme."])

G.sec("Skills and question types")
G.tex(r"""
Every multiple-choice question tests a skill from the CED. The question sets in this series tag each item with one, so your score report shows which skill to work on.

\begin{compare}{Skill}{Question stems sound like}{How to answer}
1.A Comprehend & Según el fragmento, ¿qué hace\ldots? & find the line; paraphrase it \\
1.B, 1.H Theme & ¿Cuál es el tema principal? ¿Cómo se desarrolla\ldots? & what the text says about love, time, power\ldots, not just the topic \\
1.C, 1.E Devices & ¿Qué recurso se emplea en\ldots? ¿Qué función tiene\ldots? & name the device, then its effect \\
1.D, 1.G Tone, perspective & ¿Cuál es la actitud del narrador? & evaluative words, irony \\
1.F Inference & ¿Qué se puede inferir? ¿Qué sugiere\ldots? & what the text implies, not what is merely plausible \\
1.I Character & ¿Qué revela sobre el personaje\ldots? & actions and words as evidence \\
2.C, 2.E Context & ¿Qué rasgo del Barroco\ldots? ¿Qué refleja sobre la época? & period and movement features \\
3.A, 3.B Comparison & ¿Qué tienen en común los dos textos? & one feature from each text \\
\end{compare}

\begin{trap}
Distinguish \emph{topic} (tema as subject: the sea) from \emph{theme} (what the work says about it: the sea as a symbol of death). Answer choices often offer a true topic where the question asks for a theme.
\end{trap}
""")
G.q("3 Skills", r"A question asks: ¿Qué función tiene la repetición del verso «¡Ay de mi Alhama!»? Which skill does it test?",
    "explaining the function of a rhetorical or structural feature", [("identifying the period of the text", "The question is about a device's effect."),
                                                                     ("comprehending a detail of the plot", "It asks for function, not a detail."),
                                                                     ("comparing two texts", "There is one text.")],
    "función → 1.E.", "Function questions (1.E) ask what a feature does: emphasis, rhythm, emotion, structure.",
    ["¿Qué función tiene…? → 1.E."])
G.q("3 Skills", r"A poem's topic is autumn. Which statement names a theme rather than a topic?",
    "Autumn represents the passing of youth and the approach of death.", [("The poem is about autumn.", "That is the topic."),
                                                                          ("The poem has four stanzas.", "That is structure."),
                                                                          ("The poem mentions leaves and wind.", "Those are images.")],
    "Theme = a claim about the topic.", "A theme says what the work suggests about its subject.",
    ["autumn (topic) → passing of youth (theme)."])

G.sec("The toolkit: devices, versification and narrative")
G.tex(r"""
\begin{vocab}
la metáfora & metaphor & ``oro bruñido'' for hair \\
el símil (la comparación) & simile & ``como la grupa de un potro'' \\
la personificación & personification & ``el tiempo airado'' \\
el hipérbaton & inverted word order & ``del monte quejosos los ganados'' \\
la anáfora & repetition at the start of lines & ``Volverán\ldots / Volverán\ldots'' \\
el encabalgamiento & enjambment & a sentence runs over the line break \\
el apóstrofe & address to an absent person or thing & ``Huracán, huracán, venir te siento'' \\
la antítesis / la paradoja & opposition / apparent contradiction & \\
la gradación & climax, intensifying series & ``en tierra, en humo, en polvo, en sombra, en nada'' \\
la sinécdoque / la metonimia & part for whole / association & ``cinco tricornios'' for five guards \\
el estribillo & refrain & ``¡Ay de mi Alhama!'' \\
\end{vocab}

\begin{compare}{Form}{Shape}{Examples}
soneto & 14 hendecasyllables: two quartets, two tercets & Garcilaso, Góngora, Quevedo \\
romance & octosyllables, assonant rhyme in even lines & ``Romance de la pérdida de Alhama'', Lorca \\
redondilla & quatrains of octosyllables, abba & Sor Juana \\
verso libre & no fixed meter or rhyme & Neruda, Burgos \\
\end{compare}

\textbf{Counting syllables.} Join a final vowel with the next initial vowel (\emph{sinalefa}); add one syllable if the line ends in a stressed word (\emph{aguda}), subtract one if it ends in an \emph{esdrújula}. \textbf{Narrative voice}: first person (protagonist or witness), third person (omniscient or limited), second person; note the narrator's reliability and distance.
""")
G.q("4 Devices", r"In ``en tierra, en humo, en polvo, en sombra, en nada'' (Góngora), which device dominates?",
    "gradación (an intensifying series)", [("símil", "There is no comparison with como."),
                                           ("hipérbaton", "The word order is not inverted."),
                                           ("apóstrofe", "No one is addressed.")],
    "Series that climbs (or descends) to nothing.", "Gradación orders terms by increasing intensity, here toward annihilation.",
    ["tierra → humo → polvo → sombra → nada."])
G.q("4 Versification", r"Which form has fourteen hendecasyllabic lines in two quartets and two tercets?",
    "el soneto", [("el romance", "Romances use octosyllables in an open series."),
                  ("la redondilla", "Redondillas are octosyllabic quatrains."),
                  ("el verso libre", "Free verse has no fixed pattern.")],
    "14 × 11 syllables = soneto.", "The sonnet came to Spanish from Italy in the 16th century (Garcilaso, Boscán).",
    ["4 + 4 + 3 + 3 lines."])
G.q("4 Narrative", r"Lázaro tells his own life and comments on it years later. What kind of narrator is he?",
    "a first-person protagonist narrator", [("a third-person omniscient narrator", "He says yo."),
                                            ("a witness narrator in the third person", "He is the protagonist."),
                                            ("a second-person narrator", "He addresses ``vuestra merced'', but narrates in the first person.")],
    "Yo + protagonist.", "The picaresque novel is a first-person autobiography of a low-born narrator.",
    ["«a mí me llaman Lázaro de Tormes»."])

G.sec("Periods and movements")
G.tex(r"""
\begin{compare}{Period or movement}{Dates (approx.)}{Features to name in an answer}
Edad Media & to the late 15th c. & oral tradition, didactic exempla, romances, Reconquista \\
Renacimiento & 16th c. & Italian forms, carpe diem, harmony, idealized nature; conquest chronicles \\
Barroco & 17th c. & desengaño, time and death, contrast and wit (conceptismo, culteranismo), honor \\
Romanticismo & early--mid 19th c. & feeling, the sublime in nature, freedom, the self \\
Realismo, Naturalismo & late 19th c. & objective description, social class, determinism of heredity and environment \\
Modernismo & 1880s--1910s & beauty, musicality, exotic imagery, Latin American identity \\
Generación del 98 & 1898--1920s & Spain's crisis, Castile, existential doubt \\
Vanguardias, Generación del 27 & 1920s--30s & bold imagery, popular forms renewed (Lorca) \\
Boom & 1960s & magical realism, the fantastic, fragmented time \\
Contemporánea & 1970s-- & identity, migration, women's voices, Latino literature in the U.S. \\
\end{compare}
""")
G.q("5 Periods", r"A sonnet laments that time destroys everything and sees in every object a reminder of death. Which period's perspective does it most reflect?",
    "el Barroco", [("el Renacimiento", "Renaissance poems urge enjoyment of youth with balance, not desengaño."),
                   ("el Romanticismo", "Romantic poems center the self's emotions and nature's sublime power."),
                   ("el Modernismo", "Modernismo seeks beauty and musicality.")],
    "Desengaño + death = Barroco.", "The 17th century's crises produced a literature of disillusion with time and death.",
    ["«recuerdo de la muerte» → Barroco."])
G.q("5 Periods", r"A story explains a character's fate by heredity and environment, with crude, objective detail. Which movement does it fit?",
    "el Naturalismo", [("el Modernismo", "Modernismo stresses beauty and sound."),
                       ("el Renacimiento", "No."),
                       ("el Boom", "The Boom favors the fantastic and fragmented time.")],
    "Determinism → Naturalismo.", "Naturalism (Zola; Pardo Bazán in Spain) shows characters shaped by environment and heredity.",
    ["herencia + medio → Naturalismo."])

G.sec("Short answers: Text Explanation and Text and Art Comparison")
G.tex(r"""
Each short answer is scored out of 6: \textbf{content} (1--3) and \textbf{language} (1--3). Aim for 150--200 well-chosen words.

\begin{compare}{Task}{Content: what a 3 requires}{Method}
Text Explanation & correctly identifies the period (and may identify the author); explains how the theme develops in the whole work, with relevant evidence & sentence 1: author, work, period; then 3--4 sentences tracing the theme from beginning to end, with a quoted phrase \\
Text and Art Comparison & compares how the theme appears in both the text and the artwork, with evidence from each; connects the theme to the text's genre, period or movement & one similarity or difference; a detail from each; one sentence on period or movement \\
\end{compare}

\begin{trap}
The Text Explanation prompt says \emph{en la obra completa}: the excerpt starts you, but the top score needs the theme traced through the whole work. Writing only about the excerpt caps content at 2.
\end{trap}
""")
G.q("6 Short answer", r"A Text Explanation response explains the theme well using only the excerpt and identifies the author but not the period. What limits its content score?",
    "It must identify the period correctly and treat the whole work for a 3.", [("It needs at least 500 words.", "Length is not the criterion."),
                                                                               ("It must compare the text with another text.", "That is Q4."),
                                                                               ("It must describe a work of art.", "That is Q2.")],
    "Period + whole work.", "The top content score requires the correct period and the theme's development in the work, with evidence.",
    ["period missing + excerpt only → below 3."])

G.sec("Essays: Analysis of a Single Text and Text Comparison")
G.tex(r"""
Each essay is scored out of 10: \textbf{content} (1--5) and \textbf{language} (1--5). Plan five minutes, write 25, check five.

\begin{compare}{Essay}{Content: what a 5 requires}{Shape}
Analysis of a Single Text & a thesis that analyzes how the text represents its genre \emph{and} the given historical, cultural or social context; precise textual evidence; analysis, not summary & intro with thesis; one paragraph on genre features, one on context, with quotations; conclusion \\
Text Comparison & a thesis comparing how literary devices in both texts develop the given theme; evidence from both; analysis of effects & intro; paragraphs organized by device or idea, each discussing both texts; conclusion \\
\end{compare}

\begin{keyidea}[Analysis versus summary]
Summary says what happens. Analysis says how the text makes it mean: \emph{Mediante la gradación final, el poeta reduce la belleza a ``nada'', lo cual expresa el desengaño barroco.} Every paragraph should have at least one device + effect + link to the thesis.
\end{keyidea}
""")
G.q("7 Essays", r"Which sentence analyzes rather than summarizes?",
    "La anáfora de «Volverán» crea un ritmo de regreso que contrasta con el «¡no volverán!» final y subraya lo irrepetible del amor.", [("En el poema, las golondrinas vuelven al balcón.", "Summary of content."),
                                                                                                                                       ("El poema tiene seis estrofas.", "A structural fact with no effect."),
                                                                                                                                       ("Bécquer es un poeta del siglo XIX.", "Context with no link to the text.")],
    "Device + effect + meaning.", "Analysis names a feature and explains what it does.",
    ["anáfora → ritmo → contraste → tema."])

G.sec("The Spanish of literary analysis")
G.tex(r"""
\begin{compare}{Purpose}{Phrases}{}
Thesis & En este fragmento, el autor plantea / denuncia / sugiere que\ldots & \\
Device + effect & Mediante (A través de) la metáfora de\ldots, el poeta\ldots; lo cual subraya\ldots & \\
Evidence & como se observa en el verso\ldots; cuando el narrador afirma: «\ldots» & \\
Inference & Esto sugiere / revela / pone de manifiesto que\ldots & \\
Contrast & En cambio, \ldots; mientras que\ldots; a diferencia de\ldots & \\
Context & Este rasgo es propio del Barroco, que\ldots; refleja la sociedad de\ldots & \\
Conclusion & En definitiva, \ldots; Así, la obra\ldots & \\
\end{compare}

\textbf{Language row.} Accurate accents (\emph{él/el, más/mas, qué/que}), agreement, the present tense for literary analysis (\emph{el narrador cuenta}), and precise literary vocabulary all count.
""")
G.q("8 Language", r"Which tense is standard for discussing what happens in a literary work?",
    "the present: el narrador cuenta, el poeta afirma", [("the preterite throughout: el narrador contó", "Literary analysis conventionally uses the present."),
                                                         ("the future: el narrador contará", "No."),
                                                         ("the conditional: el narrador contaría", "No.")],
    "Literary present.", "Analysis describes the text as always present: Lázaro narra, Ildara sueña.",
    ["present for plot and analysis."])

G.sec("A study plan", "A study plan")
G.tex(r"""
\begin{compare}{When}{Do this}{Using}
September--March & One unit every three to four weeks: read the required works, then the guide, its checks and its question set. Keep a one-page card per work: author, period, genre, themes, two quotations. & Unit guides 1--8 \\
Every two weeks & One short answer (15 minutes) and one essay (35 minutes), scored with the rubrics. & Part 0 \S\S6--7 \\
April & Review cards by theme: for each of the six themes, three works and how each treats it. & your cards \\
May & Two full timed free-response sections; listening practice with real recordings. & AP Classroom, this series \\
\end{compare}
""")

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Part 0: Toolkit Drill", r"Part 0 \textperiodcentered\ Question Set",
        abstract=r"""Seventeen items on the toolkit every task assumes (devices, versification, narrative voice, periods and movements, the language of analysis), followed by a Text Explanation (6 points) on the \emph{Romance de la pérdida de Alhama}, with the scoring guide and a model response. As on the exam, questions and the free-response task are in Spanish. Quotations from required works are from public-domain editions. Allow about 15 minutes for the drill and 15 for the short answer.""",
        scoring=r"Drill: \blank\ / \qtotal \qquad Text Explanation: \blank\ / 6 \qquad Target: 15+ drill and 5+ short answer",
        short="Part 0", sub="Toolkit Drill")

Q.sec("Recursos literarios")
Q.q("4 Recursos", r"¿Qué recurso aparece en «oro bruñido al sol relumbra en vano» para referirse al cabello?",
    "la metáfora", [("el símil", "No hay un nexo comparativo como «como»."),
                    ("la anáfora", "No hay repetición al comienzo de versos."),
                    ("el apóstrofe", "No se dirige a nadie ausente.")],
    "Identificación sin «como»: metáfora.", "La metáfora identifica dos realidades: el cabello es «oro bruñido».",
    ["oro = cabello → metáfora."])
Q.q("4 Recursos", r"En «el cielo reluce / como la grupa de un potro» (Lorca), el recurso es",
    "el símil", [("la metáfora", "Aparece el nexo «como»: es una comparación explícita."),
                 ("la personificación", "El cielo no realiza acciones humanas."),
                 ("el hipérbaton", "El orden de las palabras es normal.")],
    "«como» → símil.", "El símil compara dos realidades con un nexo explícito.",
    ["como la grupa de un potro."])
Q.q("4 Recursos", r"«y del monte quejosos los ganados» (Quevedo) altera el orden habitual «y los ganados quejosos del monte». ¿Cómo se llama este recurso?",
    "el hipérbaton", [("la anáfora", "No hay repetición."),
                      ("la gradación", "No hay serie que se intensifique."),
                      ("el encabalgamiento", "El encabalgamiento divide una frase entre dos versos; aquí se altera el orden.")],
    "Orden alterado → hipérbaton.", "El hipérbaton invierte el orden sintáctico habitual, típico de la poesía barroca.",
    ["del monte quejosos los ganados."])
Q.q("4 Recursos", r"En «Volverán las oscuras golondrinas… / Volverán las tupidas madreselvas… / Volverán del amor…» (Bécquer), ¿qué recurso estructura el poema?",
    "la anáfora", [("la paradoja", "No hay contradicción aparente."),
                   ("el apóstrofe", "La voz se dirige a «tú», pero el recurso que estructura las estrofas es la repetición inicial."),
                   ("la sinécdoque", "No se nombra la parte por el todo.")],
    "Repetición al inicio → anáfora.", "La anáfora repite una palabra al principio de versos o estrofas.",
    ["Volverán… / Volverán… / Volverán…"])
Q.q("4 Recursos", r"«Huracán, huracán, venir te siento» (Heredia). El poeta",
    "se dirige directamente al huracán, un apóstrofe", [("compara el huracán con un animal", "No hay comparación en este verso."),
                                                        ("cuenta una historia en tercera persona", "Habla en primera persona y se dirige al huracán."),
                                                        ("usa una ironía", "El tono es de exaltación, no irónico.")],
    "Invocación → apóstrofe.", "El apóstrofe interpela a un ser o fuerza ausente o inanimado.",
    ["Huracán, huracán, … te siento."])
Q.q("4 Recursos", r"En el «Prendimiento» de Lorca, «entre los cinco tricornios» designa a los guardias civiles por su sombrero. El recurso es",
    "la metonimia", [("la hipérbole", "No hay exageración."),
                     ("la antítesis", "No hay ideas opuestas."),
                     ("el estribillo", "No es un verso que se repita.")],
    "Objeto asociado por la persona → metonimia.", "La metonimia nombra algo por otra cosa relacionada (el tricornio por el guardia).",
    ["tricornios = guardias."])

Q.sec("Métrica y formas")
Q.q("4 Métrica", r"¿Cuántas sílabas métricas tiene «Paseábase el rey moro»?",
    "ocho: es un octosílabo", [("siete: es un heptasílabo", "Cuente: Pa-se-á-ba-se el-rey-mo-ro, con sinalefa en «se el»."),
                                ("once: es un endecasílabo", "Es un verso de arte menor."),
                                ("seis: es un hexasílabo", "Faltan sílabas en el cómputo.")],
    "Octosílabo del romance.", "Pa-se-á-ba-sel-rey-mo-ro: 8 sílabas con sinalefa (se-el).",
    ["sinalefa: se + el = una sílaba."])
Q.q("4 Métrica", r"Un poema de versos octosílabos con rima asonante en los versos pares y número indefinido de versos es",
    "un romance", [("un soneto", "El soneto tiene catorce endecasílabos."),
                   ("una redondilla", "La redondilla es una estrofa de cuatro octosílabos con rima abba."),
                   ("verso libre", "El verso libre no tiene métrica fija.")],
    "Octosílabos + asonancia en pares → romance.", "El romance es la forma de la poesía tradicional y de Lorca en el Romancero gitano.",
    ["Alhama, Prendimiento → romance."])
Q.q("4 Métrica", r"«Hombres necios que acusáis / a la mujer, sin razón, / sin ver que sois la ocasión / de lo mismo que culpáis» está escrito en",
    "redondillas: cuartetas de octosílabos con rima abba", [("tercetos endecasílabos", "Son versos de ocho sílabas."),
                                                           ("verso libre", "Hay rima consonante regular."),
                                                           ("un soneto", "La composición es una serie de cuartetas.")],
    "acusáis/culpáis, razón/ocasión: abba.", "La redondilla: cuatro octosílabos con rima consonante abba.",
    ["a b b a."])

Q.sec("Narrador y punto de vista")
Q.q("4 Narrador", r"«Es un poderoso día de verano en Misiones… el padre abre también su corazón a la naturaleza» (Quiroga). El narrador",
    "es de tercera persona y conoce los pensamientos del padre", [("es el padre, que narra en primera persona", "El texto dice «el padre», no «yo»."),
                                                                 ("es el hijo, que recuerda su infancia", "No hay «yo»."),
                                                                 ("se dirige al lector en segunda persona", "No."),],
    "Tercera persona con acceso a la mente.", "El narrador en tercera persona focaliza al padre y revela sus pensamientos y temores.",
    ["«el padre» + sus pensamientos."])
Q.q("4 Narrador", r"Lázaro escribe a «vuestra merced» para explicar «el caso». ¿Qué forma adopta la novela?",
    "una autobiografía en forma de carta", [("un diario íntimo sin destinatario", "Tiene destinatario: vuestra merced."),
                                            ("una obra de teatro", "Es narrativa."),
                                            ("una crónica histórica oficial", "Es la vida ficticia de un pícaro.")],
    "Epístola autobiográfica.", "La forma epistolar justifica la narración en primera persona del pícaro.",
    ["vuestra merced = destinatario."])

Q.sec("Períodos y movimientos")
Q.q("5 Períodos", r"«coged de vuestra alegre primavera / el dulce fruto, antes que el tiempo airado / cubra de nieve la hermosa cumbre» expresa el tópico",
    "carpe diem, propio del Renacimiento", [("el desengaño barroco ante la muerte", "Aquí predomina la invitación a gozar, con armonía renacentista."),
                                             ("el amor cortés medieval", "No hay vasallaje amoroso."),
                                             ("la denuncia social del Naturalismo", "No.")],
    "Goza la juventud → carpe diem.", "Garcilaso adapta el tópico horaciano con el equilibrio del Renacimiento.",
    ["coged … el dulce fruto → carpe diem."])
Q.q("5 Períodos", r"Una obra exalta la sangre indígena y la lengua española de «nuestra América» frente al poder de los Estados Unidos con imágenes exóticas y musicales. Corresponde al",
    "Modernismo", [("Barroco", "No."),
                   ("Realismo", "No."),
                   ("Boom", "El Boom es de los años sesenta.")],
    "Darío, Martí → Modernismo.", "El Modernismo une renovación estética e identidad hispanoamericana.",
    ["«A Roosevelt» (1904)."])
Q.q("5 Períodos", r"¿Qué rasgo caracteriza mejor el Romanticismo?",
    "la expresión intensa del yo y lo sublime de la naturaleza", [("la objetividad científica y el determinismo", "Eso es el Naturalismo."),
                                                                 ("el desengaño y la brevedad de la vida", "Eso es el Barroco."),
                                                                 ("la fragmentación del tiempo y el realismo mágico", "Eso es el Boom.")],
    "Yo + naturaleza sublime.", "Heredia y Bécquer: emoción, libertad, naturaleza grandiosa.",
    ["«¡Sublime tempestad!»"])

Q.sec("El lenguaje del análisis")
Q.q("8 Lenguaje", r"¿Qué oración presenta mejor una tesis analítica?",
    "En el romance, el estribillo «¡Ay de mi Alhama!» convierte la noticia militar en un lamento colectivo y anticipa la caída de Granada.", [("El romance trata de un rey moro.", "Es un resumen del tema, no una tesis."),
                                                                                                                                                ("El romance tiene muchos versos.", "Es un dato sin análisis."),
                                                                                                                                                ("Me gusta mucho este romance.", "Es una opinión personal.")],
    "Recurso + efecto + significado.", "Una tesis analítica afirma cómo y para qué funciona el texto.",
    ["estribillo → lamento → caída de Granada."])
Q.q("8 Lenguaje", r"Elige la forma correcta: El narrador \blank\ su vida a vuestra merced para justificar «el caso».",
    "cuenta", [("contó", "En el análisis literario se usa el presente."),
               ("contaba", "El imperfecto no es la convención del análisis."),
               ("contará", "No.")],
    "Presente literario.", "Se analiza el texto en presente: el narrador cuenta, el poeta afirma.",
    ["presente → cuenta."])
Q.q("8 Lenguaje", r"Elige la oración correctamente acentuada.",
    "Él sabe más de lo que el narrador cuenta.", [("El sabe mas de lo que él narrador cuenta.", "«Él» (pronombre) lleva tilde; «el» (artículo) no; «más» (cantidad) lleva tilde."),
                                                 ("Él sabe mas de lo que el narrador cuenta.", "«más» de cantidad lleva tilde."),
                                                 ("El sabé más de lo que el narrador cuenta.", "«sabe» no lleva tilde; «Él» sí.")],
    "Él/el, más/mas.", "La tilde diacrítica distingue el pronombre «él» del artículo «el», y «más» (cantidad) de «mas» (pero).",
    ["Él (pronombre) … más (cantidad) … el (artículo)."])

Q.frq(kind="Text Explanation", head=r"Question 1 \textperiodcentered\ Text Explanation \textperiodcentered\ 6 points \textperiodcentered\ about 15 minutes", mins=15,
      directions=[r"Lee el fragmento. Luego, contesta la pregunta en español. Identifica al autor (si se conoce) y el período de la obra a la que pertenece este fragmento. Luego, explica el desarrollo del tema de la pérdida en la obra completa."],
      sources=[dict(title=r"Fragmento", paras=[
          r"Paseábase el rey moro\\ por la ciudad de Granada,\\ desde la puerta de Elvira\\ hasta la de Vivarambla.\\ ---¡Ay de mi Alhama!",
          r"Cartas le fueron venidas\\ que Alhama era ganada.\\ Las cartas echó en el fuego,\\ y al mensajero matara.\\ ---¡Ay de mi Alhama!",
          r"[\ldots]",
          r"Por eso mereces, rey,\\ una pena muy doblada:\\ que te pierdas tú y el reino,\\ y aquí se pierda Granada.\\ ---¡Ay de mi Alhama!"])],
      model=[r"Este fragmento pertenece al «Romance de la pérdida de Alhama», un romance anónimo de la Edad Media, de finales del siglo XV, compuesto durante la última fase de la Reconquista. Como todo romance de la tradición oral, no tiene autor conocido.",
             r"El tema de la pérdida se desarrolla de manera progresiva. Al principio, el rey moro se pasea tranquilo por Granada, y la noticia de que «Alhama era ganada» rompe esa calma; su reacción violenta, que echa las cartas al fuego y mata al mensajero, muestra que se niega a aceptar la pérdida. Luego, el rey convoca a sus moros, y la pérdida se vuelve colectiva: el estribillo «¡Ay de mi Alhama!», que se repite tras cada estrofa, transforma la noticia en un lamento compartido. Finalmente, el alfaquí interpreta la pérdida como un castigo por los crímenes del rey contra los Bencerrajes y profetiza una pérdida mayor: «que te pierdas tú y el reino, / y aquí se pierda Granada». Así, la pérdida de una ciudad anticipa la caída del reino nazarí en 1492."],
      rows=[("Content", 3, "identifies the period (Edad Media, finales del siglo XV) and that the romance is anonymous; explains how the theme of loss develops through the whole poem (denial, collective lament, punishment and prophecy) with quoted evidence", "writing only about the first stanza; no period, or a wrong one; summary with no development"),
            ("Language", 3, "accurate, varied Spanish; literary vocabulary (estribillo, romance, Reconquista); correct accents and agreement", "errors that make meaning unclear; very limited vocabulary")],
      tips=["The first sentence identifies work, author (anonymous) and period.", "The theme is traced from beginning to end, with three stages marked (Al principio, Luego, Finalmente).",
            "Two short quotations and the function of the refrain show analysis, not just plot.", "About 190 words."],
      ask="Escribe tu respuesta en español (unas 150–200 palabras). Luego, puntúa tu respuesta con la guía.", lines=12)

GUIDE, QSET = G, Q
