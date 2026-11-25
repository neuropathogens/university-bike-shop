from ap_wl.model import Doc

STEM = "05-generation-98-modernismo"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 5: La Generación del 98 y el Modernismo", r"Unit 5 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 5 reads five required works from the turn of the twentieth century: José Martí's ``Nuestra América'', Rubén Darío's ``A Roosevelt'', Antonio Machado's ``He andado muchos caminos'', Miguel de Unamuno's \emph{San Manuel Bueno, mártir} and Horacio Quiroga's ``El hijo''. This guide sets out the two movements behind them (Modernismo in Spanish America, the Generation of 1898 in Spain), each work's argument or plot, devices and themes, and an Analysis of a Single Text kit for the essay genre. Martí, Darío, Machado and Quiroga are quoted from public-domain editions; Unamuno's novel is summarized. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 11+ \qquad Quotations I can use: \blank[10em]",
        short="Unit 5", sub="La Generación del 98 y el Modernismo")

G.sec("Context: 1898, Modernismo and the Generation of 1898")
G.tex(r"""
\begin{compare}{Date}{Event}{Link to the texts}
1888 & Darío's \emph{Azul} opens Modernismo & renewal of poetic language \\
1891 & Martí publishes ``Nuestra América'' & Latin American identity and unity \\
1898 & Spanish--American War: Spain loses Cuba, Puerto Rico, the Philippines & crisis of Spanish identity; U.S. power in the hemisphere \\
1903--1905 & U.S. role in Panama; Darío's \emph{Cantos de vida y esperanza} with ``A Roosevelt'' & Hispanic America against U.S. expansion \\
1931 & Unamuno publishes \emph{San Manuel Bueno, mártir} & faith, doubt and the meaning of life \\
\end{compare}

\begin{compare}{}{Modernismo}{Generación del 98}
Where & Spanish America, then Spain & Spain \\
Aims & beauty, musicality, exotic and refined imagery; later, Hispanic American identity & reflection on Spain's decline; the essence of Castile; existential anguish \\
Style & rich, sonorous, cosmopolitan & sober, introspective, plain \\
Authors in the course & Martí, Darío & Unamuno, Machado \\
\end{compare}
""")
G.q("1 Context", r"Which event of 1898 gave its name to a generation of Spanish writers?",
    "Spain's defeat in the Spanish--American War and the loss of its last colonies", [("the fall of Granada", "That was 1492."),
                                                                                       ("the publication of Darío's \\emph{Azul}", "That was 1888 and began Modernismo."),
                                                                                       ("the Mexican Revolution", "That began in 1910.")],
    "1898 → Generación del 98.", "The «Desastre» led writers to reflect on Spain's identity and decline.",
    ["pérdida de Cuba, Puerto Rico y Filipinas."])
G.q("1 Context", r"Which description fits Modernismo rather than the Generation of 1898?",
    "musical, refined language with exotic images, and a defense of Hispanic American identity", [("sober reflection on the landscape of Castile", "That is the Generation of 1898."),
                                                                                                  ("Naturalist determinism", "No."),
                                                                                                  ("Baroque desengaño", "No.")],
    "Modernismo → belleza + identidad.", "Darío and Martí renew the language and affirm Hispanic America.",
    ["Darío, Martí."])

G.sec("José Martí, ``Nuestra América'' (1891)")
G.tex(r"""
\textbf{Genre and argument.} An essay, published in New York and Mexico, that calls the peoples of Latin America to know and unite themselves before a powerful neighbor. Martí attacks the ``aldeano vanidoso'' who thinks his village is the world, and the ``sietemesinos'' (born prematurely) who despise their Indigenous roots and imitate Europe. He argues that good government must come from knowledge of one's own land.

\begin{compare}{Quotation}{Device}{Point}
``Trincheras de ideas valen más que trincheras de piedra'' & antithesis, aphorism & thought as the defense of the continent \\
``el gigante de las siete leguas'' & metaphor from folk tales & a powerful neighbor (the U.S.) \\
``Los que no tienen fe en su tierra son hombres de siete meses'' & metaphor & imitators lack courage and roots \\
``como la plata en las raíces de los Andes'' & simile & unity as natural strength \\
\end{compare}

\begin{keyidea}[Genre: the essay]
An essay argues from a personal point of view, with images, aphorisms and direct address rather than data. Martí's prose is \emph{modernista}: dense metaphors and rhythm serve a political argument.
\end{keyidea}
""")
G.q("2 Martí", r"What does Martí mean by ``Trincheras de ideas valen más que trincheras de piedra''?",
    "Knowledge and ideas defend a people better than military fortifications.", [("Latin America should build stone walls.", "The opposite."),
                                                                                 ("War is the only solution.", "He favors «las armas del juicio»."),
                                                                                 ("Ideas are useless in politics.", "No.")],
    "Ideas > piedra.", "An aphorism built on antithesis: the weapons of judgment win.",
    ["las armas del juicio, que vencen a las otras."])
G.q("2 Martí", r"Whom does Martí criticize as ``hombres de siete meses''?",
    "those who have no faith in their own land and imitate foreign models", [("Indigenous peoples", "He defends them."),
                                                                             ("farmers who work the land", "No."),
                                                                             ("poets of the Golden Age", "No.")],
    "Sietemesinos.", "He mocks elites ashamed of their roots who look to Madrid or Paris.",
    ["el brazo de Madrid o de París."])

G.sec("Rubén Darío, ``A Roosevelt'' (1904)")
G.tex(r"""
\textbf{Argument.} The poem addresses Theodore Roosevelt as ``Cazador'' and as the embodiment of the United States: ``Eres los Estados Unidos, / eres el futuro invasor / de la América ingenua que tiene sangre indígena, / que aún reza a Jesucristo y aún habla en español''. It concedes U.S. power and wealth, then answers with ``la América nuestra'', ancient, poetic, Indigenous and Hispanic, Catholic and alive, and closes: ``Y, pues contáis con todo, falta una cosa: ¡Dios!''.

\begin{compare}{Feature}{In the text}{Effect}
Apostrophe & ``Es con voz de la Biblia, o verso de Walt Whitman, / que habría que llegar hasta ti, Cazador!'' & a solemn, direct challenge \\
Anaphora & ``Eres\ldots eres\ldots''; ``la América\ldots la América\ldots'' & accumulation and rhythm \\
Antithesis & U.S. (Hércules, Mammón, ``incendio'') vs. Hispanic America (poetry, love, God) & the poem's argument \\
Cultural references & Netzahualcóyotl, Moctezuma, the Inca, Guatemoc & an identity older than the U.S. \\
\end{compare}
""")
G.q("3 Darío", r"Which contrast organizes ``A Roosevelt''?",
    "U.S. power and wealth against the spiritual, cultural and historical strength of Hispanic America", [("city and countryside in Spain", "No."),
                                                                                                         ("youth and old age", "No."),
                                                                                                         ("Romanticism and Realism", "No.")],
    "EE. UU. vs. la América nuestra.", "Antithesis drives the poem's political argument.",
    ["Juntáis al culto de Hércules el culto de Mammón / Mas la América nuestra…"])
G.q("3 Darío", r"What does the last line, ``falta una cosa: ¡Dios!'', suggest?",
    "that for all its power the U.S. lacks the spiritual dimension Darío claims for Hispanic America", [("that the U.S. has too many churches", "No."),
                                                                                                         ("that Darío rejects religion", "The opposite."),
                                                                                                         ("that Roosevelt is a priest", "No.")],
    "Poder material vs. espiritual.", "The closing turns the argument from power to spirit.",
    ["pues contáis con todo, falta una cosa."])

G.sec("Antonio Machado, ``He andado muchos caminos'' (1903)")
G.tex(r"""
\textbf{The poem.} A traveler who has ``andado muchos caminos'' describes two kinds of people he has seen everywhere: arrogant, melancholy ``pedantones'' who think they know because they do not drink the taverns' wine (``Mala gente que camina / y va apestando la tierra\ldots''), and ``buenas gentes'' who dance, play and work ``sus cuatro palmos de tierra'', never ask where they arrive, and ``en un día como tantos, / descansan bajo la tierra''.

\textbf{Features.} Octosyllabic quatrains with assonance in é-a; simple, conversational language; anaphora ``he andado\ldots he abierto\ldots he navegado''; the earth as both work and grave. Themes: authentic, humble life against pretension; time and death accepted with serenity, in the sober style of the Generation of 1898.
""")
G.q("4 Machado", r"Which people does the speaker admire?",
    "the ``buenas gentes'' who live, work and dream simply", [("the ``pedantones'' who think they know", "He calls them «mala gente»."),
                                                              ("the travelers who sail a hundred seas", "That is the speaker."),
                                                              ("the rich landowners", "Not mentioned.")],
    "Buenas gentes.", "The poem praises simplicity over arrogance.",
    ["Son buenas gentes que viven, / laboran, pasan y sueñan."])
G.q("4 Machado", r"In the final lines, ``descansan bajo la tierra'' refers to",
    "death, presented as a natural rest", [("a nap after lunch", "Literal misreading."),
                                           ("working in the fields", "That was «laboran sus cuatro palmos de tierra»."),
                                           ("a journey to America", "No.")],
    "Eufemismo de la muerte.", "Death is accepted serenely as part of a simple life.",
    ["en un día como tantos."])

G.sec("Miguel de Unamuno, San Manuel Bueno, mártir (1931)")
G.tex(r"""
\textbf{Plot.} Ángela Carballino writes her memories of Don Manuel, the beloved priest of Valverde de Lucerna, a village between a lake (with the legend of a sunken village) and a mountain. Don Manuel gives his life to his people, but cannot recite the line of the Creed about eternal life. Ángela's brother Lázaro returns from America as a skeptic; Don Manuel confides to him that he does not believe in the afterlife, yet preaches so that the villagers may live and die in peace. Lázaro joins his work. After Don Manuel's death, the Church begins his beatification; Ángela wonders whether she herself believes.

\begin{compare}{Element}{In the novel}{What to say}
Narrator & Ángela, first person, years later & a witness whose own faith wavers; a ``found'' memoir framed by a final note \\
Lake and mountain & the sunken village; the steady peak & doubt and faith; dualidad del ser \\
Don Manuel & a saint who does not believe & sacrifice: happiness for others over truth \\
Lázaro & from progressive skeptic to collaborator & the name recalls the biblical Lazarus raised from the dead \\
\end{compare}

\begin{keyidea}[Themes]
La dualidad del ser: faith and doubt, outer life and inner anguish; truth versus consolation; the existential concern with death typical of Unamuno and the Generation of 1898.
\end{keyidea}
""")
G.q("5 Unamuno", r"What is Don Manuel's secret?",
    "He does not believe in eternal life, though he preaches it to keep his people's faith.", [("He is not really a priest.", "He is an ordained priest."),
                                                                                               ("He plans to leave the village for America.", "Lázaro comes back from America."),
                                                                                               ("He is Ángela's father.", "No.")],
    "Fe ajena, duda propia.", "The novel's paradox: a saint of a faith he does not share.",
    ["no puede decir «creo en la resurrección de la carne y la vida perdurable»."])
G.q("5 Unamuno", r"Which course theme does the novel most directly develop?",
    "la dualidad del ser", [("las sociedades en contacto", "Not the central theme."),
                            ("la creación literaria only", "The memoir frame matters, but the core is the divided self."),
                            ("las relaciones entre amos y criados", "No.")],
    "Dualidad.", "Faith and doubt, public role and private anguish.",
    ["lago / montaña; fe / duda."])

G.sec("Horacio Quiroga, ``El hijo'' (1928)")
G.tex(r"""
\textbf{Plot.} On a ``poderoso día de verano en Misiones'', a widowed father sends his thirteen-year-old son hunting alone, proud of having raised him to be self-reliant. The father suffers from hallucinations. He hears one shot, then nothing; the boy does not return by noon. Anxiety grows into certainty of disaster as he searches the forest. He then ``finds'' his son, smiling, and walks home with him, happy. The narrator reveals the truth: the father walks alone; his son lies dead since morning, caught on a wire fence.

\begin{compare}{Feature}{In the text}{Effect}
Present tense & ``Es un poderoso día de verano'' & immediacy; time moves with the father's anxiety \\
Free indirect style & the father's thoughts blend with the narration & we share his hope, and his illusion \\
Foreshadowing & the hallucination of the boy covered in blood; ``al cruzar un alambrado\ldots'' & tension and the coming tragedy \\
Nature & heat, silence, the forest ``detenida\ldots esperándolo'' & a powerful, indifferent setting \\
Twist & the happy reunion is a hallucination & reality and illusion; the brutality of fate \\
\end{compare}
""")
G.q("6 Quiroga", r"What is revealed at the end of ``El hijo''?",
    "The reunion is the father's hallucination; the son died that morning on a wire fence.", [("The son was hiding to play a joke.", "No."),
                                                                                              ("The father had dreamed the whole day.", "The death is real; the reunion is not."),
                                                                                              ("Juan, the son's friend, was the one who died.", "No.")],
    "Alucinación final.", "The twist overturns the apparent happy ending.",
    ["el padre vuelve solo; el hijo yace en el alambrado."])

G.sec("Task kit: Analysis of a Single Text (the essay genre)")
G.tex(r"""
\begin{compare}{Paragraph}{Genre}{Context}
Martí & essay: first-person argument, aphorisms, metaphors, direct address to the reader & late 19th-century Latin America: young republics, elites imitating Europe, the rising U.S. \\
Evidence & ``Trincheras de ideas\ldots''; ``el gigante de las siete leguas'' & ``Los que no tienen fe en su tierra\ldots'' \\
Claim & the modernista essay persuades through images as much as through reasoning & the essay defines a shared identity against two threats: internal imitation and external power \\
\end{compare}
""")
G.q("7 Essay", r"Which sentence analyzes Martí's essay as a genre?",
    "Martí no argumenta con datos, sino con aforismos y metáforas que buscan persuadir y despertar al lector.", [("Martí nació en La Habana en 1853.", "Biography."),
                                                                                                                 ("El ensayo es muy largo.", "No analysis."),
                                                                                                                 ("En el ensayo, Martí habla de América.", "Topic only.")],
    "Género: cómo persuade.", "Genre analysis explains how the form works.",
    ["aforismos + metáforas → persuasión."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 5: La Generación del 98 y el Modernismo: Question Set", r"Unit 5 \textperiodcentered\ Question Set",
        abstract=r"""Three multiple-choice sets as on the exam: a listening interview with a critic about \emph{San Manuel Bueno, mártir} (printed as a transcript), an excerpt from Darío's ``A Roosevelt'' and the opening of Quiroga's ``El hijo'', followed by an Analysis of a Single Text essay (10 points) on Martí's ``Nuestra América'', with the scoring guide and a model essay. Questions are in Spanish. Darío, Quiroga and Martí are quoted from public-domain editions; the interview is original. Allow about 25 minutes for the multiple choice and 35 for the essay.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Essay: \blank\ / 10 \qquad Target: 15+ MCQ and 7+ essay",
        short="Unit 5", sub="La Generación del 98 y el Modernismo")

Q.sec("Comprensión auditiva: entrevista")
Q.src(r"Audio 1 \textperiodcentered\ Entrevista (transcripción) \textperiodcentered\ Una crítica habla de \emph{San Manuel Bueno, mártir}", [
    r"(PERIODISTA) Usted ha dedicado un libro a esta novela de Unamuno. ¿Por qué sigue conmoviendo a los lectores?",
    r"(CRÍTICA) Porque plantea una pregunta que no tiene respuesta fácil: ¿es mejor una verdad que nos desespera o una ilusión que nos permite vivir? Don Manuel elige lo segundo, no para sí mismo, sino para su pueblo.",
    r"(PERIODISTA) Muchos lo ven como un hipócrita.",
    r"(CRÍTICA) Es la lectura más rápida, pero la novela la complica. Don Manuel no gana nada con su secreto; al contrario, sufre. Por eso es «mártir»: da testimonio de una fe que él mismo no tiene. Es una paradoja muy unamuniana.",
    r"(PERIODISTA) ¿Y el paisaje?",
    r"(CRÍTICA) El lago y la montaña no son decorado. La montaña se alza firme, como la fe del pueblo; el lago, con su aldea sumergida, guarda en el fondo lo que no se ve: la duda. Unamuno convierte el paisaje en un retrato del alma.",
], 5, note="Transcripción original escrita para esta práctica.")
Q.q("1.B Tema", r"Según la crítica, ¿qué pregunta plantea la novela?",
    "si es preferible una verdad que desespera o una ilusión que permite vivir", [("si un sacerdote debe casarse", "No."),
                                                                                  ("si el campo es mejor que la ciudad", "No."),
                                                                                  ("si la ciencia puede explicar el lago", "No.")],
    "Verdad vs. ilusión.", "1.B: tema central según la crítica.",
    ["¿es mejor una verdad que nos desespera o una ilusión…?"])
Q.q("1.G Perspectiva", r"¿Cómo responde la crítica a quienes ven a Don Manuel como un hipócrita?",
    "Reconoce esa lectura, pero la considera demasiado simple.", [("Está totalmente de acuerdo.", "La complica."),
                                                                  ("Se niega a responder.", "Responde."),
                                                                  ("Dice que Unamuno odiaba a Don Manuel.", "No.")],
    "Lectura matizada.", "1.G: actitud de la crítica.",
    ["Es la lectura más rápida, pero la novela la complica."])
Q.q("1.F Inferencia", r"Según la crítica, ¿por qué es Don Manuel un «mártir»?",
    "porque sufre para dar testimonio de una fe que no comparte", [("porque muere asesinado", "No se dice."),
                                                                   ("porque es perseguido por el gobierno", "No."),
                                                                   ("porque pierde su fortuna", "No.")],
    "Mártir = testigo.", "1.F: la paradoja del título.",
    ["da testimonio de una fe que él mismo no tiene."])
Q.q("1.C Símbolos", r"Según la crítica, ¿qué representa el lago con su aldea sumergida?",
    "la duda oculta bajo la superficie", [("la fe firme del pueblo", "Eso es la montaña."),
                                          ("la riqueza de la región", "No."),
                                          ("el viaje de Lázaro a América", "No.")],
    "Lago = duda.", "1.C: símbolo del paisaje.",
    ["guarda en el fondo lo que no se ve: la duda."])
Q.q("2.C Movimiento", r"¿Qué rasgo de la Generación del 98 refleja la novela, según la entrevista?",
    "la angustia existencial y la reflexión sobre la fe y la muerte", [("la exaltación del exotismo oriental", "Eso es modernista."),
                                                                       ("el determinismo científico", "Eso es naturalista."),
                                                                       ("el humor picaresco", "No.")],
    "Angustia existencial.", "2.C: Unamuno en su contexto.",
    ["paradoja unamuniana; verdad que desespera."])

Q.sec("Lectura: obra de la lista")
Q.src(r"Texto 1 \textperiodcentered\ Rubén Darío, «A Roosevelt» (fragmento)", [
    r"Es con voz de la Biblia, o verso de Walt Whitman,\\ que habría que llegar hasta ti, ¡Cazador!\\ ¡Primitivo y moderno, sencillo y complicado,\\ con un algo de Washington y cuatro de Nemrod!\\ Eres los Estados Unidos,\\ eres el futuro invasor\\ de la América ingenua que tiene sangre indígena,\\ que aún reza a Jesucristo y aún habla en español.",
    r"[\ldots] Mas la América nuestra, que tenía poetas\\ desde los viejos tiempos de Netzahualcóyotl,\\ {[\ldots]} la América del grande Moctezuma, del Inca,\\ la América fragante de Cristóbal Colón,\\ la América católica, la América española,\\ {[\ldots]} esa América\\ que tiembla de huracanes y que vive de Amor,\\ hombres de ojos sajones y alma bárbara, vive.\\ Y sueña. Y ama, y vibra; y es la hija del Sol.",
], 8, note="Edición de dominio público (1905).")
Q.q("1.C Recursos", r"El poema se dirige directamente a Roosevelt como «¡Cazador!». El recurso es",
    "el apóstrofe", [("la sinécdoque", "No."),
                     ("el símil", "No."),
                     ("la aliteración", "No es lo esencial.")],
    "Interpelación.", "1.C: apóstrofe.",
    ["hasta ti, ¡Cazador!"])
Q.q("1.C Recursos", r"«Primitivo y moderno, sencillo y complicado» se basa en",
    "antítesis que muestran a Roosevelt como contradictorio", [("una gradación hacia la nada", "No."),
                                                               ("una metáfora del paisaje", "No."),
                                                               ("un quiasmo", "No hay inversión de términos.")],
    "Opuestos.", "1.C: pares contrarios.",
    ["primitivo / moderno; sencillo / complicado."])
Q.q("1.F Inferencia", r"¿Qué sugiere la expresión «el futuro invasor»?",
    "que Estados Unidos amenaza con dominar a Hispanoamérica", [("que Roosevelt es un viajero", "No."),
                                                               ("que España invadirá América", "No."),
                                                               ("que el poeta desea la invasión", "Lo contrario.")],
    "Amenaza imperialista.", "1.F: contexto de 1904.",
    ["Eres los Estados Unidos, eres el futuro invasor."])
Q.q("1.A Comprensión", r"Según la primera estrofa, ¿cómo es «la América ingenua»?",
    "indígena por su sangre, cristiana y de lengua española", [("anglosajona y protestante", "No."),
                                                               ("rica e industrial", "Esa es la imagen de EE. UU."),
                                                               ("sin tradición poética", "Lo contrario.")],
    "Sangre indígena, Jesucristo, español.", "1.A: detalles explícitos.",
    ["que tiene sangre indígena, que aún reza a Jesucristo y aún habla en español."])
Q.q("1.E Función", r"¿Qué función tiene la anáfora de «la América» en el segundo fragmento?",
    "acumular rasgos de una identidad hispanoamericana rica y antigua", [("enumerar los países que visitó el poeta", "No."),
                                                                         ("criticar a Colón", "No."),
                                                                         ("describir un mapa", "No.")],
    "Acumulación identitaria.", "1.E: la repetición construye la identidad.",
    ["la América del grande Moctezuma… la América católica…"])
Q.q("2.E Contexto", r"¿Por qué menciona el poeta a Netzahualcóyotl, Moctezuma y el Inca?",
    "para mostrar que la cultura del continente es anterior a la llegada de los europeos y de Estados Unidos", [("para celebrar la conquista", "No."),
                                                                                                                  ("para hablar de Grecia", "No."),
                                                                                                                  ("para criticar a los pueblos indígenas", "Lo contrario.")],
    "Herencia indígena.", "2.E: identidad hispanoamericana.",
    ["tenía poetas desde los viejos tiempos de Netzahualcóyotl."])
Q.q("1.D Tono", r"¿Qué tono predomina en el poema?",
    "desafiante y orgulloso", [("humilde y sumiso", "Lo contrario."),
                               ("melancólico y resignado", "No."),
                               ("humorístico", "No.")],
    "Desafío.", "1.D: la voz se enfrenta al poder.",
    ["Tened cuidado. ¡Vive la América española!"])
Q.q("2.C Movimiento", r"¿Qué rasgo del Modernismo se observa en el fragmento?",
    "el lenguaje sonoro y rico en referencias culturales al servicio de la identidad hispanoamericana", [("la sobriedad de la Generación del 98", "No."),
                                                                                                         ("el desengaño barroco", "No."),
                                                                                                         ("el realismo mágico", "Es posterior.")],
    "Modernismo comprometido.", "2.C: Darío en Cantos de vida y esperanza.",
    ["Nemrod, Netzahualcóyotl, hija del Sol."])

Q.sec("Lectura: obra de la lista")
Q.src(r"Texto 2 \textperiodcentered\ Horacio Quiroga, «El hijo» (fragmento)", [
    r"Es un poderoso día de verano en Misiones, con todo el sol, el calor y la calma que puede deparar la estación. La naturaleza plenamente abierta, se siente satisfecha de sí. Como el sol, el calor y la calma ambiente, el padre abre también su corazón a la naturaleza.",
    r"---Ten cuidado, chiquito ---dice a su hijo; abreviando en esa frase todas las observaciones del caso y que su hijo comprende perfectamente. ---Sí, papá ---responde la criatura mientras coge la escopeta y carga de cartuchos los bolsillos de su camisa, que cierra con cuidado. ---Vuelve a la hora de almorzar ---observa aún el padre. ---Sí, papá ---repite el chico.",
    r"[\ldots] No es fácil, sin embargo, para un padre viudo, sin otra fe ni esperanza que la vida de su hijo, educarlo como lo ha hecho él, libre en su corto radio de acción, seguro de sus pequeños pies y manos desde que tenía cuatro años, consciente de la inmensidad de ciertos peligros y de la escasez de sus propias fuerzas.",
    r"[\ldots] De este modo ha educado el padre a su hijo. Y para conseguirlo ha debido resistir no sólo a su corazón, sino a sus tormentos morales; porque ese padre, de estómago y vista débiles, sufre desde hace un tiempo de alucinaciones.",
], 7, note="Edición de dominio público (1928).")
Q.q("1.A Comprensión", r"¿Qué le pide el padre al hijo antes de que salga?",
    "que tenga cuidado y vuelva a la hora de almorzar", [("que cace una paloma para la cena", "No."),
                                                         ("que no lleve la escopeta", "La lleva."),
                                                         ("que busque a su amigo Juan", "No en este fragmento.")],
    "Cuidado + almuerzo.", "1.A: detalles explícitos.",
    ["Ten cuidado … Vuelve a la hora de almorzar."])
Q.q("1.E Función", r"¿Qué efecto tiene el uso del tiempo presente («Es un poderoso día…», «dice a su hijo»)?",
    "crear inmediatez, como si los hechos ocurrieran ante el lector", [("indicar que la historia es un sueño", "No."),
                                                                       ("situar la historia en el futuro", "No."),
                                                                       ("mostrar que el narrador es el hijo", "No.")],
    "Presente narrativo.", "1.E: el lector vive el día junto al padre.",
    ["Es … dice … responde."])
Q.q("1.I Personajes", r"¿Qué revela el fragmento sobre la relación entre padre e hijo?",
    "una confianza mutua y un amor profundo, con el hijo como única esperanza del padre", [("una relación fría y distante", "Lo contrario."),
                                                                                             ("una rivalidad entre los dos", "No."),
                                                                                             ("que el hijo desobedece siempre", "Responde «Sí, papá»." )],
    "Confianza + amor.", "1.I: el padre viudo vive por su hijo.",
    ["sin otra fe ni esperanza que la vida de su hijo."])
Q.q("1.F Inferencia", r"¿Por qué es importante el detalle de que el padre «sufre desde hace un tiempo de alucinaciones»?",
    "porque prepara la ambigüedad entre realidad e ilusión del final", [("porque explica por qué el hijo caza", "No."),
                                                                        ("porque indica que el padre es médico", "No."),
                                                                        ("porque es un detalle sin importancia", "Es clave para el desenlace.")],
    "Anticipación.", "1.F: el detalle prepara el final.",
    ["alucinaciones → final ilusorio."])
Q.q("1.C Recursos", r"«La naturaleza, plenamente abierta, se siente satisfecha de sí» es",
    "una personificación", [("una hipérbole", "No exagera una cantidad."),
                            ("un símil", "No hay «como» en esta frase."),
                            ("una antítesis", "No.")],
    "Naturaleza con sentimientos.", "1.C: la naturaleza «se siente satisfecha».",
    ["se siente satisfecha de sí."])
Q.q("1.H Tema", r"¿Qué tensión sobre la educación del hijo plantea el narrador?",
    "la libertad que da al hijo frente al peligro y el miedo del padre", [("la escuela frente a la casa", "No."),
                                                                         ("la religión frente a la ciencia", "No."),
                                                                         ("la riqueza frente a la pobreza", "No.")],
    "Libertad vs. peligro.", "1.H: el padre ha luchado contra su propio miedo.",
    ["ha debido resistir no sólo a su corazón."])
Q.q("2.E Contexto", r"¿Qué papel tiene el ambiente de Misiones en el cuento?",
    "es una naturaleza poderosa que marca el destino de los personajes", [("es un fondo decorativo sin importancia", "Lo contrario."),
                                                                          ("es una ciudad moderna", "Es la selva."),
                                                                          ("es un lugar imaginario", "Misiones es una región real de Argentina.")],
    "Naturaleza determinante.", "2.E: el regionalismo de Quiroga.",
    ["poderoso día de verano en Misiones."])

Q.frq(kind="Analysis of a Single Text", head=r"Question 3 \textperiodcentered\ Analysis of a Single Text \textperiodcentered\ 10 points \textperiodcentered\ about 35 minutes", mins=35,
      directions=[r"Lee el fragmento. Luego, escribe un ensayo en español en el que analices cómo el texto representa las características del ensayo como género y el contexto histórico y cultural de Hispanoamérica a finales del siglo XIX. Apoya tu análisis con ejemplos del texto."],
      sources=[dict(title=r"José Martí, «Nuestra América» (fragmento)", paras=[
          r"Cree el aldeano vanidoso que el mundo entero es su aldea, y con tal que él quede de alcalde, o le mortifique al rival que le quitó la novia, o le crezcan en la alcancía los ahorros, ya da por bueno el orden universal, sin saber de los gigantes que llevan siete leguas en las botas y le pueden poner la bota encima [\ldots]. Lo que quede de aldea en América ha de despertar. Estos tiempos no son para acostarse con el pañuelo a la cabeza, sino con las armas de almohada [\ldots]: las armas del juicio, que vencen a las otras. Trincheras de ideas valen más que trincheras de piedra.",
          r"[\ldots] Los pueblos que no se conocen han de darse prisa para conocerse, como quienes van a pelear juntos. [\ldots] Es la hora del recuento, y de la marcha unida, y hemos de andar en cuadro apretado, como la plata en las raíces de los Andes.",
          r"A los sietemesinos sólo les faltará el valor. Los que no tienen fe en su tierra son hombres de siete meses. Porque les falta el valor a ellos, se lo niegan a los demás. No les alcanza al árbol difícil el brazo canijo, el brazo de uñas pintadas y pulsera, el brazo de Madrid o de París, y dicen que no se puede alcanzar el árbol. [\ldots] ¡Estos nacidos en América, que se avergüenzan, porque llevan delantal indio, de la madre que los crió, y reniegan, ¡bribones!, de la madre enferma, y la dejan sola en el lecho de las enfermedades!"])],
      model=[r"En «Nuestra América» (1891), José Martí, figura clave del Modernismo, utiliza el ensayo para convocar a los pueblos hispanoamericanos a conocerse y unirse. Mediante un lenguaje cargado de metáforas, aforismos y apelaciones directas, el texto responde a un contexto doble: la amenaza de un vecino poderoso y la debilidad interna de unas élites que desprecian su propia tierra.",
             r"En primer lugar, el fragmento muestra los rasgos del ensayo como género. Martí no expone datos ni estadísticas, sino que argumenta desde una voz personal y apasionada. Abre con una figura reconocible, «el aldeano vanidoso» que cree que «el mundo entero es su aldea», para criticar la mirada estrecha de los pueblos que no ven el peligro. Condensa sus ideas en aforismos memorables, como «Trincheras de ideas valen más que trincheras de piedra», cuya antítesis resume la tesis: la defensa de América es intelectual. Además, se dirige al lector con exclamaciones e insultos («¡bribones!»), propios de un texto que busca persuadir y movilizar, no solo informar.",
             r"En segundo lugar, el texto refleja el contexto de Hispanoamérica a finales del siglo XIX. Las repúblicas recién independizadas estaban divididas, y Martí, que escribía desde Nueva York, percibía el poder creciente de Estados Unidos. Por eso alude a «los gigantes que llevan siete leguas en las botas», una metáfora del cuento popular que sugiere una potencia capaz de «poner la bota encima» de los pueblos débiles. Frente a ella, propone la unidad: hay que andar «en cuadro apretado, como la plata en las raíces de los Andes». Al mismo tiempo, critica a los «sietemesinos», las élites que imitan «el brazo de Madrid o de París» y se avergüenzan de «la madre» que «lleva delantal indio». Así, la identidad que defiende Martí es mestiza y propia.",
             r"En conclusión, Martí convierte el ensayo en un instrumento político: la belleza modernista de sus imágenes no es adorno, sino una forma de despertar a «lo que quede de aldea en América» ante las amenazas internas y externas de su tiempo."],
      rows=[("Content", 5, "a thesis on both genre (personal voice, aphorisms, metaphors, direct address, persuasion) and context (divided young republics, the rising U.S., elites imitating Europe, mestizo identity); precise quotations analyzed", "summary of the essay; only genre or only context; quotations not explained"),
            ("Language", 5, "accurate, varied Spanish; literary and historical vocabulary (aforismo, antítesis, mestizo, élites); clear paragraphs and transitions", "frequent errors; repetitive structures")],
      tips=["The thesis names genre and context in one sentence.", "Each body paragraph opens with a claim and analyzes two or three short quotations.",
            "The conclusion links the modernista style to the political purpose.", "About 450 words."],
      ask="Escribe tu ensayo en español (unas 350–450 palabras). Luego, puntúalo con la guía.", lines=22)

GUIDE, QSET = G, Q
