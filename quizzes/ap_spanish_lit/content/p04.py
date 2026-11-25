from ap_wl.model import Doc

STEM = "04-romantic-realist-naturalist"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 4: La literatura romántica, realista y naturalista", r"Unit 4 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 4 reads three required works from the nineteenth century and its end: José María Heredia's ``En una tempestad'', Gustavo Adolfo Bécquer's Rima LIII and Emilia Pardo Bazán's ``Las medias rojas''. This guide sets out the movements behind them (Romanticism and its sublime, Bécquer's intimate post-Romanticism, Realism and Naturalism), each text's structure, devices and themes, and a Text Explanation kit. Quotations are from public-domain editions, with modern spelling. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Quotations I can use: \blank[10em]",
        short="Unit 4", sub="La literatura romántica, realista y naturalista")

G.sec("Context: from Romanticism to Naturalism")
G.tex(r"""
\begin{compare}{Movement}{Values and techniques}{In this unit}
Romanticismo (c. 1820--1860) & the self and its passions; nature as sublime and divine; freedom; exclamations and apostrophes & Heredia, ``En una tempestad'' (1822) \\
Posromanticismo & intimate, musical, brief poems; love, memory, the ineffable & Bécquer, \emph{Rimas} (published 1871) \\
Realismo (c. 1850--1890) & society observed in detail; ordinary people; an objective narrator & the background of Pardo Bazán \\
Naturalismo (c. 1880--1900) & characters determined by heredity and environment; crude detail; poverty and violence & Pardo Bazán, ``Las medias rojas'' (1914) \\
\end{compare}

José María Heredia (1803--1839), Cuban, is a founding voice of Spanish-American Romanticism; he lived much of his life in exile for supporting Cuban independence. Emilia Pardo Bazán (1851--1921), from Galicia, introduced the debate on Naturalism in Spain with \emph{La cuestión palpitante} (1883) and defended women's education and rights.
""")
G.q("1 Context", r"Which feature is most typical of Naturalism?",
    "characters shaped and limited by heredity, poverty and environment", [("the poet's ecstasy before sublime nature", "That is Romanticism."),
                                                                          ("the carpe diem invitation", "That is Renaissance."),
                                                                          ("musical, exotic imagery", "That is Modernismo.")],
    "Determinism.", "Naturalism, after Zola, presents lives determined by environment and heredity.",
    ["Naturalismo → determinismo."])
G.q("1 Context", r"Why is Heredia an important figure in Spanish-American literature?",
    "He is a founding Romantic poet, writing in exile for Cuban independence.", [("He wrote the first picaresque novel.", "That is Lazarillo (1554)."),
                                                                                ("He founded Modernismo.", "That is Darío, later in the century."),
                                                                                ("He was a Naturalist novelist.", "He was a poet.")],
    "Heredia → Romanticismo hispanoamericano.", "His exile and his sublime nature poetry make him a key early Romantic.",
    ["exilio + naturaleza sublime."])

G.sec("Heredia, ``En una tempestad'' (1822)")
G.tex(r"""
\textbf{What happens.} The poet senses a hurricane approaching, greets it (``Huracán, huracán, venir te siento''), watches the earth fall silent and a bull call to the storm, then sees darkness, lightning and rain cover the world until ``el huracán y yo solos estamos''. In the last stanza he feels lifted ``al trono del Señor'' and weeps in adoration.

\begin{compare}{Feature}{In the text}{Effect}
Apostrophe & ``Huracán, huracán, venir te siento'' & the poet addresses nature as a living power \\
Exclamations, questions & ``¡Qué nubes! ¡qué furor!''; ``¿Al toro no miráis?'' & emotion and immediacy \\
Personification & the sun ``temblando''; the hurricane as ``Gigante de los aires'' & nature as a grand, divine actor \\
Silva & free mix of 7- and 11-syllable lines & freedom of form for intense feeling \\
The sublime & terror and delight together: ``¡Sublime tempestad!'' & the self elevated, then united with God \\
\end{compare}
""")
G.q("2 Heredia", r"How does the poet feel before the hurricane?",
    "exalted and drawn to it, with awe rather than simple fear", [("calm and indifferent", "He is «entusiasmado»."),
                                                                  ("only afraid, wanting to flee", "He greets it: «te saludo»."),
                                                                  ("bored by the bad weather", "No.")],
    "Lo sublime.", "Romantic sublime: terror and delight at once.",
    ["«respiro entusiasmado» … «¡Sublime tempestad!»"])
G.q("2 Heredia", r"What does ``El huracán y yo solos estamos'' express?",
    "the Romantic self alone with nature, separated from the ordinary world", [("the poet's fear of being alone", "He feels exalted."),
                                                                               ("that the storm has ended", "It is at its height."),
                                                                               ("that his friends have left the city", "No.")],
    "Yo + naturaleza.", "The storm erases the world; only the self and nature remain.",
    ["mundo fatal, nos separamos."])

G.sec("Bécquer, Rima LIII (``Volverán las oscuras golondrinas'')")
G.tex(r"""
\begin{tcolorbox}[colback=white,colframe=black!15,boxrule=0.4pt,arc=0pt,left=8pt,right=8pt]
\small Volverán las oscuras golondrinas\\ en tu balcón sus nidos a colgar,\\ y otra vez con el ala a sus cristales\\ \hspace*{2em}jugando llamarán.\\[2pt]
Pero aquellas que el vuelo refrenaban\\ tu hermosura y mi dicha a contemplar,\\ aquellas que aprendieron nuestros nombres\ldots\\ \hspace*{2em}ésas\ldots\ ¡no volverán!\\[2pt]
[\ldots]\ Volverán del amor en tus oídos\\ las palabras ardientes a sonar;\\ tu corazón de su profundo sueño\\ \hspace*{2em}tal vez despertará;\\[2pt]
pero mudo y absorto y de rodillas,\\ como se adora a Dios ante su altar,\\ como yo te he querido\ldots, desengáñate,\\ \hspace*{2em}¡así no te querrán!
\end{tcolorbox}

\textbf{Structure.} Three pairs of stanzas. Each pair opens with ``Volverán'' (swallows, honeysuckle, words of love) and answers with ``Pero\ldots'' and a negation (``¡no volverán!'', ``¡no volverán!'', ``¡así no te querrán!''). Lines of 11 syllables close with a short line of 7; the even lines share the assonance in stressed \emph{a} (colgar, llamarán, contemplar, volverán).

\textbf{Theme.} Nature repeats itself; a unique love does not. The poem moves from the shared past (``nuestros nombres'') to a direct address that turns into a final, bitter claim about the speaker's own love.
""")
G.q("3 Bécquer", r"What contrast structures Rima LIII?",
    "what returns in nature against what will never return: their unique love", [("day against night", "Not the structure."),
                                                                                ("the city against the countryside", "No."),
                                                                                ("youth against old age", "Not the central contrast.")],
    "Volverán / no volverán.", "Anaphora and antithesis build the poem's argument.",
    ["Volverán … Pero … ¡no volverán!"])
G.q("3 Bécquer", r"In the last stanza, what does the simile ``como se adora a Dios ante su altar'' suggest about the speaker's love?",
    "It was devoted and absolute, almost religious.", [("It was casual and brief.", "The opposite."),
                                                       ("It was only a friendship.", "No."),
                                                       ("It was forced by the family.", "No.")],
    "Amor como adoración.", "The religious image raises his love above any future one.",
    ["mudo y absorto y de rodillas."])
G.q("3 Bécquer", r"Which feature makes Bécquer a post-Romantic rather than a full Romantic like Heredia?",
    "an intimate, restrained, musical lyric instead of grand exclamatory rhetoric", [("a didactic moral at the end", "No."),
                                                                                     ("a third-person narrator", "It is a lyric in the first person."),
                                                                                     ("the use of medieval Spanish", "No.")],
    "Intimidad y sencillez.", "Bécquer's Rimas are brief and suggestive, unlike Romantic grandiloquence.",
    ["sencillez + musicalidad."])

G.sec("Pardo Bazán, ``Las medias rojas'' (1914)")
G.tex(r"""
\textbf{What happens.} In a poor Galician village, Ildara comes home with firewood and prepares the meal while her widowed father, tío Clodio, smokes. He notices her new red stockings and demands where she got the money. She claims she sold eggs; in fact, a ``gancho'' (an agent who recruits emigrants) has advanced her money for the passage to America. Her father beats her savagely. She loses a tooth and the sight of one eye, and with them her chance to emigrate: ``Los que allá vayan, han de ir sanos, válidos\ldots''

\begin{compare}{Feature}{In the text}{What to say}
Naturalist detail & the father's horn-like nail, the smoke, the blood washed in the stream & a crude, objective picture of poverty \\
Dialect & ``novidá'', ``ninguén'', ``merqué'' & Galician-tinged speech: realism of setting and class \\
Symbol & the red stockings & desire, vanity, freedom, a future, and the blood to come \\
Determinism & father, poverty, violence block her escape & environment decides fate \\
Ending & ``nunca más el barco la recibió'' & a cold, laconic close: no hope \\
\end{compare}

\begin{keyidea}[Themes]
Violence against women in a patriarchal, impoverished world; emigration as the dream of escape; the body and beauty as a woman's only capital (``la esperaba el barco''); the father's fear of being left alone.
\end{keyidea}
""")
G.q("4 Pardo Bazán", r"What do the red stockings represent for Ildara?",
    "her desire for a different life, and the first step toward emigrating", [("a gift from her father", "He is furious about them."),
                                                                             ("the uniform of her school", "No."),
                                                                             ("her mother's memory", "Not stated.")],
    "Medias rojas = deseo de futuro.", "She bought them with the recruiter's advance; they announce her escape.",
    ["de los cuales habían salido las famosas medias."])
G.q("4 Pardo Bazán", r"Why can Ildara no longer emigrate at the end?",
    "The beating leaves her blind in one eye and missing a tooth, and emigrants must be healthy.", [("Her father forbids it by law.", "The cause is physical."),
                                                                                                    ("The ship sinks.", "No."),
                                                                                                    ("She decides to stay and marry.", "No.")],
    "Cuerpo dañado = futuro cerrado.", "The laconic ending states the consequence of the violence.",
    ["han de ir sanos, válidos."])
G.q("4 Pardo Bazán", r"Which feature of the story is most typical of Naturalism?",
    "the crude, physical detail of poverty and violence that determines the character's fate", [("an idealized pastoral setting", "The village is poor and harsh."),
                                                                                                ("a supernatural ending", "No."),
                                                                                                ("a poem in sonnet form", "It is a short story.")],
    "Detalle crudo + determinismo.", "Pardo Bazán applies Naturalist technique to a Galician village.",
    ["uña córnea, sangre, diente."])

G.sec("Task kit: the Text Explanation")
G.tex(r"""
\begin{compare}{Step}{What to write}{Example: ``Las medias rojas''}
1 Identify & author, work, period or movement & Emilia Pardo Bazán, ``Las medias rojas'', Naturalismo (principios del siglo XX) \\
2 Theme in the excerpt & how the excerpt shows the theme & the father's violence when he discovers the stockings \\
3 Theme in the whole work & how it develops before and after the excerpt & the dream of the ship; the irreversible ending \\
4 Evidence & two short quotations & ``la esperaba el barco''; ``nunca más el barco la recibió'' \\
\end{compare}

\begin{trap}
The period is scored. ``Las medias rojas'' was published in 1914 but belongs to Naturalism; ``Realismo/Naturalismo'' is acceptable, ``Romanticismo'' is not.
\end{trap}
""")
G.q("5 Text Explanation", r"For ``Las medias rojas'', which identification earns the period point?",
    "Naturalismo (Realismo y Naturalismo)", [("Romanticismo", "Romanticism belongs to the first half of the 19th century."),
                                             ("Barroco", "No."),
                                             ("el Boom", "No.")],
    "Pardo Bazán → Naturalismo.", "The period must be identified correctly for the top content score.",
    ["determinismo, detalle crudo → Naturalismo."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 4: La literatura romántica, realista y naturalista: Question Set", r"Unit 4 \textperiodcentered\ Question Set",
        abstract=r"""Three multiple-choice sets as on the exam: a listening presentation on Romanticism and Realism (printed as a transcript), an excerpt from Heredia's ``En una tempestad'', and a paired set (Bécquer's Rima LIII with a modern poem not on the list), followed by a Text Explanation (6 points) on ``Las medias rojas'', with the scoring guide and a model response. Questions are in Spanish. Required works are quoted from public-domain editions with modern spelling; the transcript and the modern poem are original. Allow about 25 minutes for the multiple choice and 15 for the short answer.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Text Explanation: \blank\ / 6 \qquad Target: 15+ MCQ and 5+ short answer",
        short="Unit 4", sub="La literatura romántica, realista y naturalista")

Q.sec("Comprensión auditiva: presentación")
Q.src(r"Audio 1 \textperiodcentered\ Presentación (transcripción) \textperiodcentered\ «Del yo al mundo: Romanticismo y Realismo»", [
    r"(PROFESOR) Imaginen a un poeta romántico frente a una tormenta. No describe la tormenta para informarnos del tiempo: la describe para hablar de sí mismo, de su pasión, de su deseo de libertad. La naturaleza es un espejo del yo.",
    r"(PROFESOR) Ahora imaginen a un novelista realista frente a la misma aldea después de la tormenta. Le interesan las casas inundadas, los precios del pan, las familias que deben emigrar. El narrador se aparta y observa. Ya no es el yo lo que importa, sino la sociedad.",
    r"(PROFESOR) El Naturalismo va un paso más allá: no solo observa, sino que intenta explicar. Los personajes son producto de su herencia y de su medio, como en un experimento científico. Por eso los finales naturalistas suelen ser duros y sin salida.",
    r"(PROFESOR) No piensen, sin embargo, que estos movimientos se suceden como capítulos cerrados. Bécquer escribe en plena época realista una poesía íntima, y muchos realistas conservan una mirada romántica sobre el paisaje.",
], 5)
Q.q("1.A Comprensión", r"Según el profesor, ¿para qué describe la tormenta el poeta romántico?",
    "para hablar de sí mismo y de sus emociones", [("para informar sobre el tiempo", "Lo niega explícitamente."),
                                                   ("para denunciar la pobreza de la aldea", "Eso le interesa al realista."),
                                                   ("para explicar la herencia de los personajes", "Eso es naturalista.")],
    "La naturaleza como espejo del yo.", "1.A: idea explícita.",
    ["La naturaleza es un espejo del yo."])
Q.q("2.C Movimientos", r"¿Qué le interesa al novelista realista, según la presentación?",
    "la sociedad y las condiciones concretas de la vida", [("su propia pasión", "Eso es romántico."),
                                                          ("los mitos antiguos", "No."),
                                                          ("la musicalidad del verso", "No.")],
    "Realismo → sociedad.", "2.C: rasgos del movimiento.",
    ["casas inundadas, precios del pan, familias que deben emigrar."])
Q.q("1.F Inferencia", r"¿Por qué, según el profesor, los finales naturalistas suelen ser «duros y sin salida»?",
    "porque los personajes están determinados por su herencia y su medio", [("porque los autores querían entretener al público", "No."),
                                                                            ("porque los personajes son héroes románticos", "No."),
                                                                            ("porque se escribían en verso", "No.")],
    "Determinismo → final cerrado.", "1.F: relación causa–efecto.",
    ["producto de su herencia y de su medio."])
Q.q("1.E Función", r"¿Qué función tiene la comparación con «un experimento científico»?",
    "explicar la pretensión de objetividad y causalidad del Naturalismo", [("burlarse de la ciencia", "No."),
                                                                           ("describir el laboratorio de un autor", "Es una analogía."),
                                                                           ("presentar el Romanticismo", "No.")],
    "Analogía científica.", "1.E: aclara un concepto con una imagen.",
    ["como en un experimento científico."])
Q.q("1.B Tema", r"¿Qué advierte el profesor al final?",
    "Los movimientos literarios conviven y se mezclan, no son etapas cerradas.", [("El Romanticismo desapareció en 1850.", "Dice lo contrario."),
                                                                                  ("Bécquer fue un novelista realista.", "Fue poeta."),
                                                                                  ("El Naturalismo es mejor que el Realismo.", "No lo valora así.")],
    "Convivencia de movimientos.", "1.B: idea de la conclusión.",
    ["no se suceden como capítulos cerrados."])

Q.sec("Lectura: obra de la lista")
Q.src(r"Texto 1 \textperiodcentered\ José María Heredia, «En una tempestad» (fragmentos)", [
    r"Huracán, huracán, venir te siento,\\ y en tu soplo abrasado\\ respiro entusiasmado\\ del señor de los aires el aliento.",
    r"En las alas del viento suspendido\\ vedle rodar por el espacio inmenso,\\ silencioso, tremendo, irresistible,\\ en su curso veloz. La tierra en calma,\\ siniestra, misteriosa,\\ contempla con pavor su faz terrible.",
    r"[\ldots] ¡Sublime tempestad! ¡Cómo en tu seno,\\ de tu solemne inspiración henchido,\\ al mundo vil y miserable olvido,\\ y alzo la frente, de delicia lleno!\\ ¿Dó está el alma cobarde\\ que teme tu rugir\ldots? Yo en ti me elevo\\ al trono del Señor: oigo en las nubes\\ el eco de su voz; siento a la tierra\\ escucharle y temblar. Ferviente lloro\\ desciende por mis pálidas mejillas,\\ y su alta majestad trémulo adoro.",
], 7, note="Edición de dominio público, con ortografía modernizada.")
Q.q("1.C Recursos", r"En «Huracán, huracán, venir te siento», el poeta",
    "se dirige al huracán con un apóstrofe", [("compara el huracán con un toro", "El toro aparece más adelante."),
                                              ("narra en tercera persona", "Habla en primera persona."),
                                              ("describe el huracán con ironía", "No hay ironía.")],
    "Apóstrofe.", "1.C: interpelación a una fuerza natural.",
    ["Huracán, huracán…"])
Q.q("1.C Recursos", r"«silencioso, tremendo, irresistible» es",
    "una enumeración de adjetivos que intensifica la grandeza del huracán", [("una metáfora del poeta", "Describe el huracán."),
                                                                            ("un estribillo", "No se repite."),
                                                                            ("una pregunta retórica", "No.")],
    "Enumeración.", "1.C: acumulación expresiva.",
    ["tres adjetivos en un verso."])
Q.q("1.A Comprensión", r"¿Cómo reacciona la tierra ante el huracán?",
    "lo contempla con miedo, en un silencio inquietante", [("lo recibe con alegría", "Lo contempla «con pavor»."),
                                                          ("lo ignora", "No."),
                                                          ("lo combate", "No.")],
    "con pavor.", "1.A: detalle explícito.",
    ["La tierra en calma, siniestra, misteriosa, contempla con pavor…"])
Q.q("1.G Perspectiva", r"En la última estrofa, ¿qué actitud tiene el yo poético ante la tempestad?",
    "exaltación y adoración: se siente elevado hacia Dios", [("miedo y deseo de huir", "Lo llama «¡Sublime tempestad!»."),
                                                            ("indiferencia", "No."),
                                                            ("ironía y desprecio", "No.")],
    "Lo sublime.", "1.G: la tormenta eleva al poeta.",
    ["Yo en ti me elevo / al trono del Señor."])
Q.q("1.F Inferencia", r"¿Qué sugiere el verso «al mundo vil y miserable olvido»?",
    "que la experiencia de la naturaleza libera al poeta de la vida ordinaria", [("que el poeta odia a sus amigos", "No."),
                                                                                ("que el mundo ha sido destruido", "Es un olvido interior."),
                                                                                ("que el poeta ha perdido la memoria", "Literal; no.")],
    "Evasión romántica.", "1.F: la naturaleza como escape del mundo social.",
    ["mundo vil → olvido; frente alzada → delicia."])
Q.q("2.C Movimiento", r"¿Qué rasgo romántico es más evidente en el fragmento?",
    "la fusión de las emociones del yo con una naturaleza grandiosa y divina", [("el detalle objetivo de la pobreza", "Eso es naturalista."),
                                                                               ("el carpe diem renacentista", "No."),
                                                                               ("el humor del pícaro", "No.")],
    "Yo + naturaleza sublime.", "2.C: el Romanticismo en Heredia.",
    ["entusiasmado, sublime, me elevo, adoro."])
Q.q("1.E Función", r"¿Qué función tiene la pregunta «¿Dó está el alma cobarde / que teme tu rugir?»?",
    "subrayar, por contraste, el valor y la exaltación del poeta", [("pedir ayuda a otra persona", "Es retórica."),
                                                                    ("describir a un personaje", "No hay personaje."),
                                                                    ("cambiar de tema", "No.")],
    "Pregunta retórica.", "1.E: el «alma cobarde» contrasta con el yo valiente.",
    ["¿Dó está el alma cobarde…?"])

Q.sec("Lectura: textos relacionados")
Q.src(r"Textos 2 y 3 \textperiodcentered\ Bécquer, Rima LIII (fragmento), y «Lo que vuelve» (poema escrito para esta práctica)", [
    r"\textbf{Texto 2 (Bécquer).} Volverán las oscuras golondrinas\\ en tu balcón sus nidos a colgar,\\ y otra vez con el ala a sus cristales\\ jugando llamarán.\\ Pero aquellas que el vuelo refrenaban\\ tu hermosura y mi dicha a contemplar,\\ aquellas que aprendieron nuestros nombres\ldots\\ ésas\ldots\ ¡no volverán!",
    r"\textbf{Texto 3.} Vuelven las hojas al castaño de la plaza,\\ vuelve el olor a pan por la mañana,\\ vuelven, puntuales, los trenes de las siete.\\ Todo lo que se va sabe el camino de regreso.\\ Sólo tu voz, que tantas veces dijo mi nombre\\ en esta misma esquina,\\ se perdió en un idioma que ya nadie habla.",
], 8, note="Rima LIII: edición de dominio público, ortografía modernizada. «Lo que vuelve»: poema original escrito para esta práctica.")
Q.q("3.A Comparación", r"¿Qué recurso comparten los dos poemas?",
    "la anáfora del verbo «volver»", [("el soneto", "Ninguno es un soneto completo."),
                                      ("la rima consonante en todos los versos", "No."),
                                      ("el narrador en tercera persona", "Ambos tienen un yo lírico.")],
    "Volverán / Vuelven.", "3.A: repetición inicial en ambos.",
    ["Volverán… / Vuelven… vuelve… vuelven…"])
Q.q("3.B Comparación", r"¿Qué tema comparten?",
    "lo que regresa frente a lo que se pierde para siempre", [("la alegría del regreso del amor", "El amor no regresa."),
                                                             ("la crítica a la ciudad moderna", "No."),
                                                             ("el miedo a la naturaleza", "No.")],
    "Retorno vs. pérdida.", "3.B: semejanza temática.",
    ["¡no volverán! / se perdió."])
Q.q("3.A Comparación", r"¿En qué se diferencian las imágenes de los dos poemas?",
    "Bécquer usa imágenes de la naturaleza; el texto 3 añade imágenes urbanas y cotidianas", [("Ambos usan solo imágenes religiosas.", "No."),
                                                                                             ("El texto 3 no tiene imágenes.", "Tiene trenes, pan, plaza."),
                                                                                             ("Bécquer describe trenes.", "No.")],
    "Golondrinas vs. trenes.", "3.A: diferencia estilística.",
    ["golondrinas, balcón / plaza, pan, trenes."])
Q.q("1.C Recursos", r"En el texto 3, «Todo lo que se va sabe el camino de regreso» atribuye a las cosas",
    "una cualidad humana: es una personificación", [("un color: es una sinestesia", "No."),
                                                    ("un sonido: es una onomatopeya", "No."),
                                                    ("una exageración numérica", "No.")],
    "Saber el camino → personificación.", "1.C: las cosas «saben» volver.",
    ["sabe el camino de regreso."])
Q.q("1.E Función", r"En Bécquer, ¿qué función tienen los puntos suspensivos en «ésas… ¡no volverán!»?",
    "crear una pausa emotiva antes de la negación final", [("indicar que falta texto", "No es una omisión."),
                                                          ("señalar una pregunta", "No."),
                                                          ("marcar un cambio de hablante", "No.")],
    "Pausa expresiva.", "1.E: la puntuación intensifica la emoción.",
    ["ésas… ¡no volverán!"])
Q.q("1.F Inferencia", r"En el texto 3, «se perdió en un idioma que ya nadie habla» sugiere que",
    "la persona amada ya no está y su modo de hablar solo vive en el recuerdo", [("la persona hablaba una lengua extranjera", "Es figurado."),
                                                                                ("la voz del hablante ha cambiado", "No."),
                                                                                ("la plaza ha cambiado de nombre", "No.")],
    "Pérdida irreparable.", "1.F: metáfora del final.",
    ["idioma que ya nadie habla → ausencia."])
Q.q("1.D Tono", r"¿Qué diferencia de tono hay entre los dos finales?",
    "Bécquer termina con una exclamación; el texto 3, con una afirmación serena y melancólica", [("Ambos terminan con humor.", "No."),
                                                                                                ("El texto 3 es más exaltado que Bécquer.", "Lo contrario."),
                                                                                                ("Ninguno expresa emoción.", "Ambos la expresan.")],
    "Exclamación vs. serenidad.", "1.D: diferencia de tono.",
    ["¡no volverán! / se perdió…"])
Q.q("2.C Movimiento", r"¿Qué rasgo del posromanticismo muestra la rima de Bécquer?",
    "la expresión íntima y musical de un sentimiento amoroso", [("la denuncia social de la pobreza", "No."),
                                                               ("la visión épica de la historia", "No."),
                                                               ("la experimentación tipográfica de vanguardia", "No.")],
    "Intimidad lírica.", "2.C: Bécquer frente al Romanticismo grandilocuente.",
    ["tú / yo, amor, recuerdo, música."])

Q.frq(kind="Text Explanation", head=r"Question 1 \textperiodcentered\ Text Explanation \textperiodcentered\ 6 points \textperiodcentered\ about 15 minutes", mins=15,
      directions=[r"Lee el fragmento. Luego, contesta la pregunta en español. Identifica al autor y el período de la obra a la que pertenece este fragmento. Luego, explica el desarrollo del tema de los sueños frustrados en la obra completa."],
      sources=[dict(title=r"Fragmento", paras=[
          r"Ildara, apretando los dientes por no gritar de dolor, se defendía la cara con las manos. Era siempre su temor de mociña guapa y requebrada, que el padre «la mancase», como le había sucedido a la Mariola, su prima, señalada por su propia madre en la frente con el aro de la criba, que le desgarró los tejidos. Y tanto más defendía su belleza, hoy que se acercaba el momento de fundar en ella un sueño de porvenir. Cumplida la mayor edad, libre de la autoridad paterna, la esperaba el barco, en cuyas entrañas tantos de su parroquia y de las parroquias circunvecinas se habían ido hacia la suerte, hacia lo desconocido de los lejanos países donde el oro rueda por las calles y no hay sino bajarse para cogerlo."])],
      model=[r"Este fragmento pertenece a «Las medias rojas», cuento de Emilia Pardo Bazán publicado en 1914, que corresponde al Naturalismo (dentro del Realismo y el Naturalismo españoles).",
             r"El tema de los sueños frustrados se desarrolla a lo largo de todo el cuento. Al principio, las medias rojas que lleva Ildara son el primer signo de su sueño: las ha comprado con el dinero que le adelantó el «gancho» para el viaje a América. En el fragmento, el narrador revela ese sueño, idealizado con una hipérbole: los países lejanos son lugares «donde el oro rueda por las calles». Ildara protege su cara porque su belleza es su único capital para «fundar en ella un sueño de porvenir». Sin embargo, la violencia del padre, que teme quedarse solo, destruye ese futuro: la golpea hasta que pierde un diente y la vista de un ojo. El final es seco y definitivo: «nunca más el barco la recibió». Así, el cuento muestra, con el determinismo propio del Naturalismo, cómo la pobreza y la autoridad patriarcal cierran todas las salidas."],
      rows=[("Content", 3, "identifies the period (Naturalismo) and the author; explains how the theme develops in the whole story (the stockings and the recruiter's money, the dream of America, the father's violence, the closed ending) with evidence", "writing only about the excerpt; wrong or missing period; summary without the theme's development"),
            ("Language", 3, "accurate Spanish; literary vocabulary (Naturalismo, determinismo, hipérbole); connectors of sequence", "frequent errors; limited vocabulary")],
      tips=["The first sentence identifies author, work, year and movement.", "The theme is traced from the stockings to the last line of the story.",
            "Quotations from inside and outside the excerpt show knowledge of the whole work.", "About 200 words."],
      ask="Escribe tu respuesta en español (unas 150–200 palabras). Luego, puntúala con la guía.", lines=12)

GUIDE, QSET = G, Q
