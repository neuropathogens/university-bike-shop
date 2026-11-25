from ap_wl.model import Doc

STEM = "02-sixteenth-century"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 2: El siglo XVI", r"Unit 2 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 2 reads four required works from the sixteenth century: the anonymous \emph{Lazarillo de Tormes} (Prólogo; Tratados 1, 2, 3 and 7), Hernán Cortés's \emph{Segunda carta de relación}, two sections of Miguel León-Portilla's \emph{Visión de los vencidos}, and Garcilaso de la Vega's Soneto XXIII. This guide sets out the Renaissance and conquest contexts, the picaresque narrator and his irony, the two opposed accounts of the conquest of Mexico, Garcilaso's carpe diem, and a Text and Art Comparison kit. Quotations are from public-domain editions; \emph{Visión de los vencidos} (1959) is summarized, not quoted. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Quotations I can use: \blank[10em]",
        short="Unit 2", sub="El siglo XVI")

G.sec("Context: the Renaissance, empire and conquest")
G.tex(r"""
\begin{compare}{Date}{Event}{Link to the texts}
1492 & fall of Granada; Columbus reaches the Caribbean & Spain turns outward \\
1519--1521 & Cortés's expedition; fall of Tenochtitlan (August 1521) & Cortés's letters; the Nahua accounts \\
1520 & Cortés writes the \emph{Segunda carta} to Charles V & a conqueror's report and self-justification \\
1543 & Garcilaso's poems published (he died in 1536) & the Italian sonnet naturalized in Spanish \\
1554 & \emph{Lazarillo de Tormes} printed, anonymously & the first picaresque novel \\
\end{compare}

\textbf{Renaissance} ideals (harmony, classical models, idealized nature and love) coexist with the realities of empire: conquest, a rigid society of honor and lineage, and poverty at home. The literature of the century shows both faces.
""")
G.q("1 Context", r"To whom does Cortés address his \emph{Segunda carta de relación}?",
    "Emperor Charles V", [("the Aztec ruler Moctezuma", "Moctezuma is a character in the letter."),
                          ("the Pope", "No."),
                          ("his soldiers", "No.")],
    "Carta de relación → to the king.", "Cortés reports to Charles V to win royal support for an expedition he had begun without authorization.",
    ["relación = report to the crown."])
G.q("1 Context", r"Why was \emph{Lazarillo de Tormes} probably published anonymously?",
    "Its satire of clergy and of the obsession with honor was risky.", [("Its author was a famous king.", "No."),
                                                                        ("It was translated from Italian.", "It was written in Spanish."),
                                                                        ("Anonymous publication was required for novels.", "No.")],
    "Satire → anonymity.", "The book mocks a blind beggar, priests and a proud squire; it was placed on the Index of 1559.",
    ["crítica religiosa y social → riesgo."])

G.sec("Lazarillo de Tormes (1554)")
G.tex(r"""
\textbf{Structure.} A prologue and seven \emph{tratados}, written as a letter to ``vuestra merced'', who has asked Lázaro to explain ``el caso''. Lázaro tells his life from birth by the river Tormes to his present as a town crier in Toledo.

\begin{compare}{Section}{Master and episode}{What it shows}
Prólogo & Lázaro wants fame and explains ``el caso'' & ironic self-justification \\
Tratado 1 & the blind man: the stone bull of Salamanca, the wine jug, the grapes, the post & hunger; learning to deceive: ``el mozo del ciego un punto ha de saber más que el diablo'' \\
Tratado 2 & the priest of Maqueda and the locked bread chest & greater hunger under a stingier, ``religious'' master \\
Tratado 3 & the squire, a poor hidalgo who pretends to have eaten & honor as empty appearance; Lázaro feeds his master \\
Tratado 7 & Lázaro, town crier, marries the archpriest's servant & ``el caso'': rumors he chooses to ignore; ``en la cumbre de toda buena fortuna'' \\
\end{compare}

\begin{keyidea}[The narrator's irony]
Lázaro presents his life as a rise from poverty to good fortune. The reader sees that his ``fortune'' rests on tolerating his wife's relationship with the archpriest. The gap between what Lázaro says and what the reader understands is the book's main irony and its social critique.
\end{keyidea}
""")
G.q("2 Lazarillo", r"What does Lázaro learn from the blind man's trick at the stone bull of Salamanca?",
    "that he must stay alert and rely on himself", [("that animals are dangerous", "The bull is made of stone."),
                                                  ("that blind men cannot be trusted with money", "Not the lesson he draws."),
                                                  ("that he should return to his mother", "He leaves with the blind man.")],
    "«me cumple avivar el ojo y avisar, pues solo soy».", "The blow awakens him from childish innocence.",
    ["«desperté de la simpleza en que, como niño dormido, estaba»."])
G.q("2 Lazarillo", r"In Tratado 3, what is ironic about Lázaro's life with the squire?",
    "The servant ends up feeding the master, who hides his hunger to keep up his honor.", [("The squire is rich but stingy.", "That is closer to the priest of Tratado 2; the squire is poor."),
                                                                                         ("The squire teaches Lázaro to read.", "No."),
                                                                                         ("The squire marries Lázaro's mother.", "No.")],
    "Honra vacía.", "The hidalgo pretends to have eaten; appearance matters more than survival.",
    ["el amo come lo que Lázaro mendiga."])
G.q("2 Lazarillo", r"What is ``el caso'' that \emph{vuestra merced} asks about?",
    "the rumors about Lázaro's wife and the archpriest", [("the death of Lázaro's father", "That is in Tratado 1, but it is not «el caso»."),
                                                          ("the theft of the bread chest", "That is Tratado 2."),
                                                          ("Lázaro's appointment as a priest", "He becomes a town crier.")],
    "El caso → Tratado 7.", "The whole narrative explains how Lázaro came to his present situation.",
    ["vuestra merced escribe se le escriba y relate el caso."])

G.sec("Two accounts of the conquest: Cortés and the Nahua voices")
G.tex(r"""
\textbf{Cortés, \emph{Segunda carta de relación} (1520).} Cortés describes Tenochtitlan for the emperor with admiration: a city on a lake, joined to land by causeways, with markets, temples and order he compares to Spanish cities. He presents his own actions (including the seizure of Moctezuma) as loyal service to the crown, and reports Moctezuma's speech as a voluntary submission. The letter is both a description and an argument.

\textbf{León-Portilla, \emph{Visión de los vencidos} (1959).} An anthology of Nahua accounts of the conquest, translated from Nahuatl. ``Los presagios, según los informantes de Sahagún'' lists eight omens that announced disaster before the Spaniards arrived (a column of fire in the sky, a temple burned, voices weeping at night). ``Se ha perdido el pueblo mexica'' is a lament for the fallen city, with images of broken spears, destroyed houses and grief.

\begin{compare}{}{Cortés}{\emph{Visión de los vencidos}}
Voice & the conqueror, to the king & the conquered, recorded by Nahua informants \\
Purpose & inform, justify, gain favor & remember, mourn, explain \\
Tenochtitlan & a marvel to be won for the crown & a home and a world destroyed \\
Theme & conquest as service and achievement & conquest as catastrophe; las sociedades en contacto \\
\end{compare}
""")
G.q("3 Conquest", r"What is the main difference in perspective between Cortés's letter and \emph{Visión de los vencidos}?",
    "Cortés writes as the conqueror justifying himself; the Nahua accounts mourn the conquest from the side of the defeated.", [
        ("Both are written by Spanish soldiers.", "The Nahua accounts come from Indigenous informants."),
        ("Cortés criticizes the conquest; the Nahua accounts celebrate it.", "The reverse."),
        ("Both describe only the landscape.", "No.")],
    "Vencedor vs. vencidos.", "Reading them together is a standard course comparison under las sociedades en contacto.",
    ["Cortés → rey; Visión → los vencidos."])
G.q("3 Conquest", r"In ``Los presagios'', what function do the omens have?",
    "They frame the conquest as a disaster foretold, from the Nahua point of view.", [("They prove the Spaniards were gods.", "Not what the text claims."),
                                                                                      ("They describe Spanish weapons.", "They come before the Spaniards arrive."),
                                                                                      ("They are jokes told by soldiers.", "No.")],
    "Presagios = foreshadowing.", "The omens give meaning to the catastrophe within Nahua cosmology.",
    ["ocho presagios antes de la llegada."])

G.sec("Garcilaso de la Vega, Soneto XXIII")
G.tex(r"""
\begin{tcolorbox}[colback=white,colframe=black!15,boxrule=0.4pt,arc=0pt,left=8pt,right=8pt]
\small En tanto que de rosa y azucena\\ se muestra la color en vuestro gesto,\\ y que vuestro mirar ardiente, honesto,\\ enciende el corazón y lo refrena;\\[2pt]
y en tanto que el cabello, que en la vena\\ del oro se escogió, con vuelo presto,\\ por el hermoso cuello blanco, enhiesto,\\ el viento mueve, esparce y desordena:\\[2pt]
coged de vuestra alegre primavera\\ el dulce fruto, antes que el tiempo airado\\ cubra de nieve la hermosa cumbre.\\[2pt]
Marchitará la rosa el viento helado,\\ todo lo mudará la edad ligera\\ por no hacer mudanza en su costumbre.
\end{tcolorbox}

\begin{compare}{Part}{What it does}{Devices}
Quartets & portrait of youthful beauty, each beginning ``En tanto que'' & metaphors of color (rosa, azucena, oro); the wind ``mueve, esparce y desordena'' \\
First tercet & the command: ``coged'' & carpe diem; ``primavera'' = youth; ``nieve'' on the ``cumbre'' = white hair \\
Last tercet & the warning and the final paradox & time changes everything in order not to change its own habit \\
\end{compare}
""")
G.q("4 Garcilaso", r"What do ``nieve'' and ``la hermosa cumbre'' stand for in the first tercet?",
    "white hair on the head in old age", [("a real mountain in Italy", "Metaphor, not landscape."),
                                          ("winter weather in Toledo", "No."),
                                          ("the poet's sadness", "No.")],
    "cumbre = cabeza; nieve = canas.", "Classical metaphors: youth is spring, old age is winter.",
    ["tiempo airado → nieve → vejez."])
G.q("4 Garcilaso", r"What is paradoxical about the final line, ``por no hacer mudanza en su costumbre''?",
    "Time changes everything precisely because its only constant habit is to change.", [("The lady refuses to change her habits.", "The subject is la edad ligera."),
                                                                                        ("The poet will never change his love.", "Not stated."),
                                                                                        ("The rose does not wither.", "It will wither.")],
    "Change as time's unchanging custom.", "Mudará / no hacer mudanza: wordplay that closes the sonnet.",
    ["todo lo mudará … por no hacer mudanza."])

G.sec("Task kit: the Text and Art Comparison")
G.tex(r"""
You compare how a theme appears in a required text and an image, then connect the theme to the text's genre, period or movement. Scored on content (1--3) and language (1--3).

\begin{compare}{Step}{What to write}{Garcilaso and a painting of youth and death}
1 Thesis & the theme in both works, similar or different & ambos representan la belleza juvenil amenazada por el tiempo \\
2 Text evidence & one quoted image & ``antes que el tiempo airado / cubra de nieve la hermosa cumbre'' \\
3 Art evidence & one visual detail & the young woman held by an old woman whom Death, with an hourglass, takes by the arm \\
4 Comparison & how each medium treats the theme & the sonnet urges enjoyment; the painting stresses the threat \\
5 Context & genre, period or movement & carpe diem, Renaissance sonnet, Italian form \\
\end{compare}

\begin{trap}
Describing the image at length without comparing earns little. Every sentence about the painting should connect back to the text's theme.
\end{trap}
""")
G.q("5 Text and Art", r"Which sentence best compares the sonnet and an image of a young woman beside Death?",
    "Mientras el soneto invita a gozar la juventud antes de que llegue la vejez, la pintura muestra la muerte ya presente junto a la belleza, como advertencia.", [
        ("La pintura tiene colores oscuros.", "Description with no comparison."),
        ("El soneto tiene catorce versos.", "Form with no link to the theme."),
        ("Me gusta más la pintura que el poema.", "Personal preference.")],
    "Comparison of how each treats the theme.", "Content credit needs the theme in both works, compared.",
    ["mientras el soneto … la pintura …"])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 2: El siglo XVI: Question Set", r"Unit 2 \textperiodcentered\ Question Set",
        abstract=r"""Three multiple-choice sets as on the exam: a listening interview with a novelist about rewriting the conquest (printed as a transcript), an excerpt from \emph{Lazarillo de Tormes}, Tratado 1, and a passage of literary criticism on Lázaro's irony, followed by a Text and Art Comparison (6 points) on Garcilaso's Soneto XXIII and a sixteenth-century painting, with the scoring guide and a model response. Questions are in Spanish. Required-work excerpts are from public-domain editions; the transcript and the criticism are original. Allow about 25 minutes for the multiple choice and 15 for the short answer.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Text and Art: \blank\ / 6 \qquad Target: 15+ MCQ and 5+ short answer",
        short="Unit 2", sub="El siglo XVI")

Q.sec("Comprensión auditiva: entrevista")
Q.src(r"Audio 1 \textperiodcentered\ Entrevista (transcripción) \textperiodcentered\ Una novelista habla de la conquista", [
    r"(PERIODISTA) Su nueva novela cuenta la caída de Tenochtitlan. ¿Por qué volver a un tema tan conocido?",
    r"(NOVELISTA) Porque lo conocemos casi siempre por una sola voz: la de Cortés. Sus cartas al emperador son extraordinarias, describen la ciudad con admiración, pero también son una defensa de sí mismo. Yo quería escuchar las otras voces.",
    r"(PERIODISTA) ¿Cuáles?",
    r"(NOVELISTA) Las de los informantes nahuas que recogieron los frailes, las de los cantares tristes que lloran la ciudad perdida. Y la de una mujer que fue intérprete y de la que casi nadie quiso escuchar su versión.",
    r"(PERIODISTA) ¿No teme que la acusen de inventar?",
    r"(NOVELISTA) La novela no sustituye a la historia; la interroga. Si la crónica dice «así fue», la literatura pregunta «¿y quién lo cuenta?».",
], 5)
Q.q("1.A Comprensión", r"Según la novelista, ¿por qué volvió al tema de la conquista?",
    "porque casi siempre se ha contado desde una sola voz", [("porque nadie había escrito sobre Tenochtitlan", "Dice que es un tema «tan conocido»."),
                                                             ("porque quería celebrar a Cortés", "Quiere escuchar otras voces."),
                                                             ("porque un editor se lo pidió", "No lo dice.")],
    "una sola voz: la de Cortés.", "1.A: razón explícita.",
    ["lo conocemos casi siempre por una sola voz."])
Q.q("1.G Perspectiva", r"¿Cómo describe la novelista las cartas de Cortés?",
    "como textos admirables que también son una defensa de sí mismo", [("como documentos falsos", "No dice que sean falsas."),
                                                                       ("como poemas líricos", "Son cartas."),
                                                                       ("como textos sin valor literario", "Dice que son extraordinarias.")],
    "Admiración + autojustificación.", "1.G: la actitud de la novelista es matizada.",
    ["extraordinarias … pero también una defensa de sí mismo."])
Q.q("2.E Contexto", r"¿A qué obra de la lista se refiere probablemente al hablar de «los informantes nahuas que recogieron los frailes»?",
    "a «Visión de los vencidos»", [("a «Lazarillo de Tormes»", "No trata de la conquista."),
                                   ("a la «Segunda carta de relación»", "Esa es la voz de Cortés."),
                                   ("al Soneto XXIII de Garcilaso", "No.")],
    "Informantes de Sahagún.", "2.E: conexión con una obra de la lista.",
    ["informantes nahuas → Visión de los vencidos."])
Q.q("1.F Inferencia", r"¿A quién alude probablemente «una mujer que fue intérprete»?",
    "a la intérprete indígena de Cortés, conocida como Malinche", [("a la reina Isabel", "No fue intérprete."),
                                                                   ("a una fraile franciscana", "No."),
                                                                   ("a la esposa de Moctezuma", "No se describe así.")],
    "Intérprete de la conquista.", "1.F: inferencia a partir del contexto histórico.",
    ["intérprete + conquista → Malinche."])
Q.q("1.B Tema", r"Según la novelista, ¿qué diferencia hay entre la crónica y la literatura?",
    "La crónica afirma lo que pasó; la literatura pregunta quién lo cuenta.", [("La crónica inventa; la literatura no.", "Lo contrario de lo que sugiere."),
                                                                              ("Ambas dicen exactamente lo mismo.", "No."),
                                                                              ("La literatura sustituye a la historia.", "Dice que no la sustituye.")],
    "«¿y quién lo cuenta?»", "1.B: idea principal de su respuesta final.",
    ["la interroga."])

Q.sec("Lectura: obra de la lista")
Q.src(r"Texto 1 \textperiodcentered\ Anónimo, \emph{Lazarillo de Tormes}, Tratado primero (fragmento)", [
    r"Salimos de Salamanca, y llegando a la puente, está a la entrada de ella un animal de piedra, que casi tiene forma de toro, y el ciego mandóme que llegase cerca del animal y, allí puesto, me dijo:",
    r"---Lázaro: llega el oído a este toro y oirás gran ruido dentro de él.",
    r"Yo simplemente llegué, creyendo ser así. Y como sintió que tenía la cabeza par de la piedra, afirmó recio la mano y dióme una gran calabazada en el diablo del toro, que más de tres días me duró el dolor de la cornada, y díjome:",
    r"---Necio, aprende, que el mozo del ciego un punto ha de saber más que el diablo.",
    r"Y rió mucho la burla. Parescióme que en aquel instante desperté de la simpleza en que, como niño dormido, estaba. Dije entre mí: «Verdad dice éste, que me cumple avivar el ojo y avisar, pues solo soy, y pensar cómo me sepa valer».",
    r"Comenzamos nuestro camino, y en muy pocos días me mostró jerigonza. Y como me viese de buen ingenio, holgábase mucho y decía: ---Yo oro ni plata no te lo puedo dar; mas avisos para vivir muchos te mostraré.",
    r"Y fue así: que, después de Dios, éste me dio la vida, y siendo ciego me alumbró y adiestró en la carrera de vivir.",
], 8, note="Edición de 1921 (dominio público), con ortografía levemente modernizada.")
Q.q("1.A Comprensión", r"¿Qué hace el ciego cuando Lázaro acerca la cabeza al toro de piedra?",
    "le golpea la cabeza contra la piedra", [("le enseña a oír el ruido del río", "Es una burla; no hay ruido."),
                                              ("le da una moneda", "No."),
                                              ("le pide que lo guíe al puente", "Ya están en el puente.")],
    "calabazada = golpe en la cabeza.", "1.A: acción explícita.",
    ["dióme una gran calabazada en el diablo del toro."])
Q.q("1.C Recursos", r"«cornada», para referirse al golpe contra el toro de piedra, es",
    "un juego de palabras irónico, porque el toro no puede cornear", [("una metáfora del amor", "No."),
                                                                      ("una descripción literal", "El toro es de piedra."),
                                                                      ("un error del narrador", "Es intencional.")],
    "Humor verbal.", "1.C: el narrador usa la palabra propia del toro vivo para un golpe con un toro de piedra.",
    ["toro de piedra + cornada → ironía."])
Q.q("1.H Tema", r"¿Qué aprende Lázaro de este episodio?",
    "que, estando solo, debe estar atento y valerse por sí mismo", [("que debe volver con su madre", "Sigue con el ciego."),
                                                                   ("que los ciegos son buenas personas", "No es la lección."),
                                                                   ("que los toros son peligrosos", "El toro es de piedra.")],
    "avivar el ojo y avisar.", "1.H: el despertar del pícaro.",
    ["me cumple avivar el ojo y avisar, pues solo soy."])
Q.q("1.E Función", r"¿Qué función tiene la comparación «como niño dormido»?",
    "señalar el paso de la inocencia infantil a la conciencia del pícaro", [("describir el cansancio del viaje", "Es figurado."),
                                                                            ("mostrar que Lázaro tenía sueño", "No."),
                                                                            ("introducir un sueño profético", "No.")],
    "Despertar = madurez.", "1.E: la imagen marca un rito de paso.",
    ["desperté de la simpleza en que, como niño dormido, estaba."])
Q.q("1.F Inferencia", r"Cuando el ciego dice «avisos para vivir muchos te mostraré», sugiere que",
    "le enseñará astucia en lugar de riqueza", [("le dará oro y plata", "Dice que no puede."),
                                                ("le enseñará a leer y escribir", "No."),
                                                ("le enseñará a rezar", "No.")],
    "Avisos = lecciones de astucia.", "1.F: la verdadera herencia del ciego.",
    ["Yo oro ni plata no te lo puedo dar."])
Q.q("1.D Tono", r"¿Qué tono tiene la frase final, «siendo ciego me alumbró y adiestró en la carrera de vivir»?",
    "irónico y paradójico", [("trágico", "No hay lamento."),
                             ("épico", "No."),
                             ("indiferente", "No.")],
    "Ciego que alumbra.", "1.D: la paradoja del ciego que da luz.",
    ["ciego → alumbró."])
Q.q("1.C Recursos", r"«siendo ciego me alumbró» contiene",
    "una paradoja", [("una anáfora", "No hay repetición inicial."),
                     ("un símil", "No hay comparación."),
                     ("un hipérbaton", "El orden no es lo esencial.")],
    "Contradicción aparente.", "1.C: un ciego no puede alumbrar, salvo en sentido figurado.",
    ["ciego / alumbró."])
Q.q("2.C Género", r"¿Qué rasgo de la novela picaresca se observa en el fragmento?",
    "un narrador de origen humilde que cuenta en primera persona su aprendizaje con un amo", [("un caballero que busca aventuras", "Eso es la novela de caballerías."),
                                                                                               ("pastores idealizados que hablan de amor", "Eso es la novela pastoril."),
                                                                                               ("un narrador omnisciente en tercera persona", "Lázaro narra en primera persona.")],
    "Pícaro + amo + primera persona.", "2.C: rasgos del género.",
    ["yo + ciego (amo) + aprendizaje."])

Q.sec("Lectura: crítica literaria")
Q.src(r"Texto 2 \textperiodcentered\ Crítica literaria (texto escrito para esta práctica) \textperiodcentered\ «La fortuna de Lázaro»", [
    r"Al final del libro, Lázaro afirma que está «en la cumbre de toda buena fortuna». Muchos lectores han tomado la frase al pie de la letra: el niño hambriento del río Tormes tiene ahora un oficio real, una casa y una esposa. Pero el texto ofrece demasiadas pistas para aceptar esa lectura.",
    r"Lázaro le escribe a «vuestra merced» para explicar «el caso», es decir, los rumores sobre su mujer y el arcipreste. Toda la narración es, en el fondo, una defensa. Por eso el narrador selecciona, ordena y calla: insiste en el hambre de su infancia para que comprendamos su presente, y presenta como prudencia lo que el lector reconoce como resignación.",
    r"La ironía del Lazarillo no está en lo que Lázaro dice, sino en la distancia entre lo que dice y lo que el lector entiende. En esa distancia se encuentra la crítica más dura del libro: en una sociedad obsesionada con la honra, la única manera de «subir» es aceptar la deshonra con una sonrisa.",
], 7, note="Texto original escrito para esta práctica.")
Q.q("1.B Tema", r"¿Cuál es la tesis principal del crítico?",
    "La «buena fortuna» de Lázaro debe leerse con ironía, como una defensa de una situación deshonrosa.", [("Lázaro alcanza una felicidad verdadera.", "El crítico rechaza esa lectura."),
                                                                                                         ("El libro no tiene crítica social.", "Lo contrario."),
                                                                                                         ("El arcipreste es el narrador.", "No.")],
    "Ironía de la «fortuna».", "1.B: idea central del texto crítico.",
    ["el texto ofrece demasiadas pistas para aceptar esa lectura."])
Q.q("1.A Comprensión", r"Según el crítico, ¿qué es «el caso»?",
    "los rumores sobre la mujer de Lázaro y el arcipreste", [("el robo del arca del clérigo", "No."),
                                                            ("la muerte del ciego", "No."),
                                                            ("el nombramiento de Lázaro como pregonero", "Es parte de su situación, no «el caso».")],
    "el caso = los rumores.", "1.A: definición explícita.",
    ["los rumores sobre su mujer y el arcipreste."])
Q.q("1.F Inferencia", r"¿Por qué dice el crítico que «toda la narración es, en el fondo, una defensa»?",
    "porque Lázaro cuenta su vida para justificar su situación presente ante vuestra merced", [("porque Lázaro está ante un tribunal", "Escribe una carta."),
                                                                                               ("porque el libro es un manual de leyes", "No."),
                                                                                               ("porque el ciego lo acusa", "No.")],
    "Narración interesada.", "1.F: el propósito del narrador.",
    ["escribe … para explicar «el caso»."])
Q.q("1.G Perspectiva", r"¿Qué actitud tiene el crítico hacia la interpretación literal de la frase final?",
    "la considera ingenua", [("la apoya totalmente", "La rechaza."),
                             ("le es indiferente", "Argumenta en contra."),
                             ("la considera la única posible", "No.")],
    "Rechazo argumentado.", "1.G: actitud del crítico.",
    ["Muchos lectores … Pero el texto ofrece demasiadas pistas…"])
Q.q("1.E Función", r"En el segundo párrafo, ¿qué función tienen los verbos «selecciona, ordena y calla»?",
    "mostrar que el narrador manipula su relato", [("describir el oficio de pregonero", "No."),
                                                  ("enumerar los amos de Lázaro", "No."),
                                                  ("resumir el prólogo", "No.")],
    "Narrador no fiable.", "1.E: la enumeración subraya la manipulación.",
    ["selecciona, ordena y calla."])
Q.q("2.E Contexto", r"Según el crítico, ¿qué rasgo de la sociedad del siglo XVI critica el libro?",
    "la obsesión por la honra", [("el exceso de libertad religiosa", "No."),
                                 ("la falta de ciudades", "No."),
                                 ("la conquista de América", "No es el tema de este texto.")],
    "Honra.", "2.E: contexto social del Lazarillo.",
    ["en una sociedad obsesionada con la honra…"])
Q.q("1.C Recursos", r"La afirmación «la única manera de “subir” es aceptar la deshonra» resume",
    "la ironía central de la obra", [("una metáfora del río Tormes", "No."),
                                     ("el argumento del Tratado 2", "No."),
                                     ("una opinión del ciego", "Es la conclusión del crítico.")],
    "Subir aceptando la deshonra.", "1.C: formulación de la ironía.",
    ["subir ↔ deshonra."])

Q.frq(kind="Text and Art Comparison", head=r"Question 2 \textperiodcentered\ Text and Art Comparison \textperiodcentered\ 6 points \textperiodcentered\ about 15 minutes", mins=15,
      directions=[r"Lee el texto y observa la imagen (aquí descrita con palabras). Luego, contesta en español: compara cómo se representa el tema del paso del tiempo y la belleza en el texto y en la imagen. Luego, relaciona el tema con el período, el movimiento o el género del texto."],
      sources=[dict(title=r"Texto \textperiodcentered\ Garcilaso de la Vega, Soneto XXIII", paras=[
          r"En tanto que de rosa y azucena\\ se muestra la color en vuestro gesto,\\ y que vuestro mirar ardiente, honesto,\\ enciende el corazón y lo refrena;",
          r"y en tanto que el cabello, que en la vena\\ del oro se escogió, con vuelo presto,\\ por el hermoso cuello blanco, enhiesto,\\ el viento mueve, esparce y desordena:",
          r"coged de vuestra alegre primavera\\ el dulce fruto, antes que el tiempo airado\\ cubra de nieve la hermosa cumbre.",
          r"Marchitará la rosa el viento helado,\\ todo lo mudará la edad ligera\\ por no hacer mudanza en su costumbre."]),
               dict(title=r"Imagen \textperiodcentered\ Hans Baldung Grien, \emph{Las edades y la muerte}, hacia 1541--1544 (Museo del Prado)", paras=[
          r"Descripción para esta práctica: en un paisaje oscuro, una mujer joven de piel muy blanca y cabello largo y dorado está de pie junto a una anciana. La Muerte, representada como un cadáver, sostiene un reloj de arena y toma del brazo a la anciana, que a su vez sujeta a la joven. Un niño duerme en el suelo. Al fondo, un árbol seco y un cielo sombrío."])],
      model=[r"Tanto el soneto de Garcilaso como la pintura de Baldung Grien representan la belleza juvenil amenazada por el paso del tiempo. En el soneto, la juventud aparece en metáforas de color y luz: el rostro es «rosa y azucena» y el cabello está hecho de «la vena del oro»; en la pintura, la joven tiene la piel blanca y el cabello dorado, como la dama del poema.",
             r"Sin embargo, el tratamiento es distinto. Garcilaso sitúa la vejez en el futuro, «antes que el tiempo airado / cubra de nieve la hermosa cumbre», y por eso su mensaje es una invitación a gozar: «coged de vuestra alegre primavera / el dulce fruto». La pintura, en cambio, muestra la amenaza ya presente: la anciana y la Muerte con el reloj de arena están junto a la joven, y el árbol seco anuncia el final. Es una advertencia más sombría que la del poema.",
             r"El tema corresponde al tópico del carpe diem, que el Renacimiento recupera de la poesía clásica. Garcilaso lo expresa en un soneto, forma italiana que él mismo introdujo en la poesía española, con el equilibrio y la armonía propios del período."],
      rows=[("Content", 3, "compares how both works treat the theme, with a detail from each (rosa y azucena, nieve / reloj de arena, anciana); connects the theme to the Renaissance, carpe diem and the sonnet", "describing the painting without comparing; no link to period, movement or genre"),
            ("Language", 3, "accurate Spanish; comparison connectors (tanto… como, sin embargo, en cambio); literary vocabulary", "frequent errors; no connectors")],
      tips=["The answer opens with what the two works share, then turns (Sin embargo) to how they differ.", "Each claim has evidence: a quotation from the sonnet, a visual detail from the painting.",
            "The last paragraph meets the second half of the prompt: carpe diem, the Renaissance, the Italian sonnet.", "About 200 words."],
      ask="Escribe tu respuesta en español (unas 150–200 palabras). Luego, puntúala con la guía.", lines=12)

GUIDE, QSET = G, Q
