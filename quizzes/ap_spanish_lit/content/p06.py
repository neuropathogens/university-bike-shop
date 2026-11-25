from ap_wl.model import Doc

STEM = "06-twentieth-century-theater-poetry"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 6: Teatro y poesía del siglo XX", r"Unit 6 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 6 reads eight required works of twentieth-century theater and poetry: Federico García Lorca's \emph{La casa de Bernarda Alba} and ``Prendimiento de Antoñito el Camborio en el camino de Sevilla'', Osvaldo Dragún's \emph{El hombre que se convirtió en perro}, Pablo Neruda's ``Walking around'', Nicolás Guillén's ``Balada de los dos abuelos'', Nancy Morejón's ``Mujer negra'', Julia de Burgos's ``A Julia de Burgos'' and Alfonsina Storni's ``Peso ancestral''. This guide sets out their contexts (the Generation of 1927 and the Civil War, the avant-garde, Afro-Caribbean poetry, women's voices, political theater), each work's plot or argument, devices and themes, and a Text and Art Comparison kit. Storni (1919) and Lorca's ballad (1928) are quoted from public-domain editions; the other works are summarized, not quoted. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 11+ \qquad Works I can summarize: \blank[8em]",
        short="Unit 6", sub="Teatro y poesía del siglo XX")

G.sec("Context: avant-gardes, war and new voices")
G.tex(r"""
\begin{compare}{Context}{When and where}{Works}
Generación del 27; Civil War & Spain, 1920s; war 1936--1939 & Lorca, murdered in 1936 \\
Vanguardias and surrealism & Spain and Latin America, 1920s--30s & Neruda's \emph{Residencia en la tierra} (1935) \\
Poesía afroantillana & Cuba, 1930s; after the 1959 Revolution & Guillén (1934); Morejón (1975) \\
Women poets & Argentina, Puerto Rico & Storni (1919), Burgos (1938) \\
Political, absurdist theater & Argentina, 1950s & Dragún (1957) \\
\end{compare}

Twentieth-century writers renewed form (free verse, surreal images, the stage as open space) and gave voice to people long excluded from literature: women, Afro-descendants, workers. Many of these works speak of identity under pressure from society, history or power.
""")
G.q("1 Context", r"Which event ended Lorca's life in 1936?",
    "He was murdered at the start of the Spanish Civil War.", [("He died in exile in Mexico.", "No."),
                                                               ("He died of illness in New York.", "No."),
                                                               ("He was killed in the 1898 war.", "No.")],
    "1936 → Guerra Civil.", "Lorca was shot by Nationalist forces near Granada in August 1936.",
    ["Lorca (1898–1936)."])
G.q("1 Context", r"What links the poems of Guillén and Morejón?",
    "Afro-Cuban identity and the history of slavery and mestizaje", [("Baroque desengaño", "No."),
                                                                     ("the landscape of Castile", "That is the Generation of 1898."),
                                                                     ("the Mexican Revolution", "No.")],
    "Poesía afrocubana.", "Both give voice to Afro-Cuban experience and history.",
    ["Cuba, esclavitud, mestizaje."])

G.sec("Federico García Lorca")
G.tex(r"""
\textbf{\emph{La casa de Bernarda Alba} (1936; premiered 1945).} Subtitled ``drama de mujeres en los pueblos de España''. After her second husband's death, Bernarda imposes eight years of mourning on her five unmarried daughters, shut inside a house of white walls. Pepe el Romano courts Angustias, the eldest and the only one with money, but meets Adela, the youngest, at night. Adela rebels, breaks her mother's cane, and declares herself his. Bernarda shoots at Pepe; told he is dead, Adela hangs herself. Bernarda's last words impose silence: her daughter ``ha muerto virgen''.

\begin{compare}{Element}{Function}{Theme}
The house, the white walls & enclosure; a village of watching neighbors & repression; ``el qué dirán'' \\
Bernarda's cane (bastón) & her authority; Adela breaks it & tyranny and rebellion \\
Adela's green dress; the stallion & desire and freedom & the body against convention \\
``¡Silencio!'' & opening and closing commands & honor and appearances over truth \\
\end{compare}

\textbf{``Prendimiento de Antoñito el Camborio'' (\emph{Romancero gitano}, 1928).} Antonio Torres Heredia, ``hijo y nieto de Camborios'', walks to Seville with a ``vara de mimbre'', throwing lemons into the water, and is arrested by the Guardia Civil. A voice reproaches him: a true Camborio would have fought; ``¡Se acabaron los gitanos / que iban por el monte solos!''. Romance form; striking metaphors (``Moreno de verde luna''); the Guardia Civil as an oppressive force; the decline of an heroic Gypsy identity.
""")
G.q("2 Lorca", r"What does Bernarda's command ``¡Silencio!'' at the end of the play reveal?",
    "Her priority is appearances and honor, even over her daughter's death.", [("She is overcome by grief and cannot speak.", "She orders silence to impose a version of events."),
                                                                                ("She wants to hear the neighbors.", "The opposite."),
                                                                                ("She forgives Adela.", "No.")],
    "Honra y apariencias.", "Bernarda insists Adela died a virgin: what others say matters most.",
    ["¡Silencio! … ha muerto virgen."])
G.q("2 Lorca", r"In ``Prendimiento'', what does the voice reproach Antoñito for?",
    "not fighting back as a true Camborio would", [("stealing lemons", "He throws lemons into the water."),
                                                   ("going to Seville to see the bulls", "Not the reproach."),
                                                   ("drinking lemonade with the guards", "The guards drink it.")],
    "Falta de valor.", "The ballad laments a lost heroic ideal.",
    ["Si te llamaras Camborio, / hubieras hecho una fuente / de sangre con cinco chorros."])

G.sec("Women's voices: Storni, Burgos, Morejón")
G.tex(r"""
\begin{tcolorbox}[colback=white,colframe=black!15,boxrule=0.4pt,arc=0pt,left=8pt,right=8pt]
\small \textbf{Alfonsina Storni, ``Peso ancestral'' (1919)}\\[2pt]
Tú me dijiste: no lloró mi padre;\\ tú me dijiste: no lloró mi abuelo;\\ no han llorado los hombres de mi raza,\\ eran de acero.\\[2pt]
Así diciendo te brotó una lágrima\\ y me cayó en la boca\ldots; más veneno\\ yo no he bebido nunca en otro vaso\\ así pequeño.\\[2pt]
Débil mujer, pobre mujer que entiende,\\ dolor de siglos conocí al beberlo.\\ Oh, el alma mía soportar no puede\\ todo su peso.
\end{tcolorbox}

\textbf{Storni.} A man boasts that the men of his line never cried (``eran de acero''); his single tear falls into the speaker's mouth like poison. She tastes in it ``dolor de siglos'': the suffering of women who bore men's repressed pain. Ancestral weight works both ways: men forbidden to feel, women forced to carry it.

\textbf{Julia de Burgos, ``A Julia de Burgos'' (1938).} The poetic ``yo'' addresses ``tú'', the public Julia: the speaker is free, true, passionate; the other is obedient to husband, church and society. A dialogue of the divided self (la dualidad del ser) and a protest against social roles for women.

\textbf{Nancy Morejón, ``Mujer negra'' (1975).} A Black woman narrates, in an epic first person, the history of Afro-Cubans: forced crossing from Africa, slavery, rebellion, the Revolution. The voice moves from victim to protagonist of history.
""")
G.q("3 Storni", r"What does the man's tear represent for the speaker in ``Peso ancestral''?",
    "centuries of suppressed suffering that women have had to bear", [("a sign of happiness", "She calls it poison."),
                                                                     ("proof that men cry often", "The man boasts that men of his line never cried."),
                                                                     ("a cure for her sadness", "The opposite.")],
    "Lágrima = dolor de siglos.", "The tear concentrates an inherited weight.",
    ["dolor de siglos conocí al beberlo."])
G.q("3 Burgos", r"Whom does the speaker address as ``tú'' in ``A Julia de Burgos''?",
    "the public, conventional side of herself", [("her husband", "He is part of the social world, not the «tú»."),
                                                 ("God", "No."),
                                                 ("her mother", "No.")],
    "Yo vs. tú = dos Julias.", "The poem splits the self into the authentic poet and the social woman.",
    ["dualidad del ser."])

G.sec("Neruda, Guillén and Dragún")
G.tex(r"""
\textbf{Pablo Neruda, ``Walking around'' (1935).} The speaker, tired of being a man, walks through a city of shops, offices, tailors and hospitals and feels alienated, almost dead, among objects. Long free-verse lines, surreal images and enumeration express the anguish of modern urban life.

\textbf{Nicolás Guillén, ``Balada de los dos abuelos'' (1934).} The speaker sees two shadows that accompany him: his African grandfather and his Spanish grandfather. The poem recalls the slave trade and the colonial past, then ends with the two grandfathers embracing, reconciled in the speaker's mixed identity. Rhythm and repetition echo Afro-Caribbean music.

\textbf{Osvaldo Dragún, \emph{El hombre que se convirtió en perro} (1957).} Three actors and an actress tell the story of an unemployed worker who accepts the only job available, as a factory watchdog, and gradually becomes a dog. Bare stage, actors playing several roles, absurd humor; a denunciation of a society that dehumanizes workers.
""")
G.q("4 Guillén", r"How does ``Balada de los dos abuelos'' end?",
    "the African and the Spanish grandfathers embrace, reconciled in the speaker", [("the two grandfathers fight to the death", "The poem moves from conflict to reconciliation."),
                                                                                    ("the speaker rejects both grandfathers", "No."),
                                                                                    ("the speaker leaves Cuba", "No.")],
    "Reconciliación mestiza.", "The ending affirms a mixed Cuban identity.",
    ["los dos abuelos se abrazan."])
G.q("4 Dragún", r"What does the man's transformation into a dog criticize?",
    "a society and economy that strip workers of their humanity", [("the treatment of pets", "Literal misreading."),
                                                                   ("the Spanish monarchy", "No."),
                                                                   ("romantic love", "No.")],
    "Deshumanización.", "Absurd theater as social denunciation.",
    ["trabajo de perro → hombre-perro."])
G.q("4 Neruda", r"Which feeling dominates ``Walking around''?",
    "weariness and alienation in the modern city", [("joy at urban progress", "The opposite."),
                                                    ("nostalgia for the countryside of Castile", "No."),
                                                    ("religious exaltation", "No.")],
    "Angustia urbana.", "Surreal images and enumeration convey disgust and fatigue.",
    ["el hablante cansado de ser hombre."])

G.sec("Task kit: Text and Art Comparison with a 20th-century text")
G.tex(r"""
\begin{compare}{Step}{Storni and Frida Kahlo, \emph{Las dos Fridas} (1939)}{}
Theme & women's inherited or divided suffering; la dualidad del ser & \\
Text evidence & ``dolor de siglos conocí al beberlo''; ``el alma mía soportar no puede / todo su peso'' & \\
Art evidence & two seated Fridas, hearts exposed and joined by one artery; the one in a white European dress holds forceps on the cut artery as blood drips & \\
Comparison & both show pain in the body (a tear drunk, a bleeding heart); Storni's pain is inherited and shared, Kahlo's divided within one woman & \\
Context & Storni's early 20th-century poetry of women's voice, in brief rhymed stanzas & \\
\end{compare}
""")
G.q("5 Text and Art", r"Which sentence links Storni's poem to its period or movement?",
    "Storni pertenece a la generación de poetas que, a principios del siglo XX, abrieron un espacio para la voz femenina y su crítica de los roles de género.", [
        ("Storni escribe en el Siglo de Oro.", "Wrong period."),
        ("El poema es naturalista porque habla del cuerpo.", "Not the right movement label."),
        ("Storni era argentina.", "A fact, not a link to period or movement.")],
    "Voz femenina, siglo XX.", "The prompt's second half asks to connect the theme to period, movement or genre.",
    ["voz femenina + roles de género + siglo XX."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 6: Teatro y poesía del siglo XX: Question Set", r"Unit 6 \textperiodcentered\ Question Set",
        abstract=r"""Three multiple-choice sets as on the exam: a listening presentation on twentieth-century theater (printed as a transcript), Lorca's ``Prendimiento de Antoñito el Camborio'' and a passage of literary criticism on Afro-Cuban poetry, followed by a Text and Art Comparison (6 points) on Storni's ``Peso ancestral'' and Frida Kahlo's \emph{Las dos Fridas}, with the scoring guide and a model response. Questions are in Spanish. Lorca and Storni are quoted from public-domain editions; the transcript and the criticism are original and do not quote the works they discuss. Allow about 25 minutes for the multiple choice and 15 for the short answer.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Text and Art: \blank\ / 6 \qquad Target: 15+ MCQ and 5+ short answer",
        short="Unit 6", sub="Teatro y poesía del siglo XX")

Q.sec("Comprensión auditiva: presentación")
Q.src(r"Audio 1 \textperiodcentered\ Presentación (transcripción) \textperiodcentered\ «Dos escenarios del siglo XX»", [
    r"(PROFESORA) Hoy comparamos dos obras de teatro muy distintas. La casa de Bernarda Alba, de Lorca, ocurre en un solo espacio: una casa cerrada de paredes blancas. Todo sucede dentro, mientras afuera el pueblo vigila. La tensión crece porque nadie puede salir.",
    r"(PROFESORA) El hombre que se convirtió en perro, de Dragún, hace lo contrario: no hay casa, no hay decorado realista. Cuatro actores cuentan la historia y cambian de papel ante el público. El espectador nunca olvida que está en un teatro.",
    r"(PROFESORA) Sin embargo, las dos obras denuncian una forma de opresión. En Lorca, es la autoridad de Bernarda y el miedo al qué dirán; en Dragún, es un sistema económico que reduce a un hombre a la condición de animal.",
    r"(PROFESORA) Por eso conviene preguntarse no solo qué cuenta una obra, sino cómo usa el espacio escénico. En Lorca, el encierro es el tema. En Dragún, el escenario vacío nos obliga a pensar en lugar de identificarnos con los personajes.",
], 5, note="Transcripción original escrita para esta práctica.")
Q.q("1.A Comprensión", r"Según la profesora, ¿dónde ocurre toda la acción de «La casa de Bernarda Alba»?",
    "dentro de una casa cerrada", [("en las calles del pueblo", "El pueblo está afuera, vigilando."),
                                   ("en un escenario vacío", "Eso describe la obra de Dragún."),
                                   ("en una fábrica", "No.")],
    "Espacio único.", "1.A: detalle explícito.",
    ["una casa cerrada de paredes blancas."])
Q.q("3.A Comparación", r"¿En qué se diferencia el uso del espacio escénico en las dos obras?",
    "Lorca usa un espacio cerrado y realista; Dragún, un escenario sin decorado donde los actores cambian de papel.", [("Ambas usan el mismo decorado.", "No."),
                                                                                                                      ("Dragún usa una casa y Lorca un escenario vacío.", "Al revés."),
                                                                                                                      ("Ninguna usa el espacio de manera significativa.", "Lo contrario.")],
    "Encierro vs. vacío.", "3.A: diferencia estructural.",
    ["casa cerrada / no hay decorado realista."])
Q.q("3.B Comparación", r"¿Qué tienen en común las dos obras, según la presentación?",
    "Ambas denuncian una forma de opresión.", [("Ambas son comedias.", "No."),
                                               ("Ambas ocurren en Sevilla.", "No."),
                                               ("Ambas tienen un final feliz.", "No.")],
    "Opresión.", "3.B: semejanza temática.",
    ["las dos obras denuncian una forma de opresión."])
Q.q("1.F Inferencia", r"¿Por qué, según la profesora, «el espectador nunca olvida que está en un teatro» en la obra de Dragún?",
    "porque los actores cambian de papel ante el público y no hay decorado realista", [("porque la obra es muy larga", "No."),
                                                                                        ("porque el público participa en la acción", "No se dice."),
                                                                                        ("porque la obra ocurre en un teatro real", "No.")],
    "Distanciamiento.", "1.F: la técnica rompe la ilusión.",
    ["cambian de papel ante el público."])
Q.q("1.E Función", r"Según la conclusión, ¿qué función tiene el escenario vacío en Dragún?",
    "obligar al público a pensar en lugar de identificarse con los personajes", [("ahorrar dinero en decorados", "No es el argumento."),
                                                                                 ("representar una casa abandonada", "No."),
                                                                                 ("crear un ambiente romántico", "No.")],
    "Pensar, no identificarse.", "1.E: función de un recurso escénico.",
    ["nos obliga a pensar."])

Q.sec("Lectura: obra de la lista")
Q.src(r"Texto 1 \textperiodcentered\ Federico García Lorca, «Prendimiento de Antoñito el Camborio en el camino de Sevilla»", [
    r"Antonio Torres Heredia,\\ hijo y nieto de Camborios,\\ con una vara de mimbre\\ va a Sevilla a ver los toros.\\ Moreno de verde luna\\ anda despacio y garboso.\\ Sus empavonados bucles\\ le brillan entre los ojos.\\ A la mitad del camino\\ cortó limones redondos,\\ y los fue tirando al agua\\ hasta que la puso de oro.\\ Y a la mitad del camino,\\ bajo las ramas de un olmo,\\ guardia civil caminera\\ lo llevó codo con codo.",
    r"El día se va despacio,\\ la tarde colgada a un hombro,\\ dando una larga torera\\ sobre el mar y los arroyos.\\ {[\ldots]} Antonio Torres Heredia,\\ hijo y nieto de Camborios,\\ viene sin vara de mimbre\\ entre los cinco tricornios.",
    r"---Antonio, ¿quién eres tú?\\ Si te llamaras Camborio,\\ hubieras hecho una fuente\\ de sangre con cinco chorros.\\ Ni tú eres hijo de nadie,\\ ni legítimo Camborio.\\ ¡Se acabaron los gitanos\\ que iban por el monte solos!\\ Están los viejos cuchillos\\ tiritando bajo el polvo.",
    r"A las nueve de la noche\\ lo llevan al calabozo,\\ mientras los guardias civiles\\ beben limonada todos.\\ Y a las nueve de la noche\\ le cierran el calabozo,\\ mientras el cielo reluce\\ como la grupa de un potro.",
], 8, note="Edición de 1928 (dominio público en EE. UU.).")
Q.q("1.A Comprensión", r"¿Qué le ocurre a Antonio a la mitad del camino?",
    "lo detiene la guardia civil", [("pierde su caballo", "No."),
                                    ("se pelea con otro gitano", "No pelea."),
                                    ("llega a la plaza de toros", "No llega.")],
    "Prendimiento = arresto.", "1.A: el título y la primera estrofa.",
    ["guardia civil caminera / lo llevó codo con codo."])
Q.q("1.C Recursos", r"En «Moreno de verde luna», el color verde aplicado a la luna es",
    "una imagen sorprendente, de tipo metafórico, típica de Lorca", [("una descripción realista del cielo", "No es realista."),
                                                                     ("una hipérbole numérica", "No."),
                                                                     ("una pregunta retórica", "No.")],
    "Imagen vanguardista.", "1.C: la metáfora lorquiana asocia colores de forma inesperada.",
    ["verde luna."])
Q.q("1.E Función", r"¿Qué función tiene el contraste entre «con una vara de mimbre» y «viene sin vara de mimbre»?",
    "marcar la pérdida de dignidad y libertad de Antonio tras el arresto", [("indicar que ha vendido la vara", "No."),
                                                                            ("mostrar que ha llegado a Sevilla", "No llega."),
                                                                            ("describir el paisaje", "No.")],
    "Vara = dignidad.", "1.E: el objeto perdido simboliza lo perdido.",
    ["con una vara / sin vara."])
Q.q("1.C Recursos", r"«entre los cinco tricornios» designa a los guardias por su sombrero. El recurso es",
    "la metonimia", [("el símil", "No hay «como»."),
                     ("la anáfora", "No."),
                     ("el apóstrofe", "No.")],
    "Tricornio por guardia.", "1.C: metonimia.",
    ["cinco tricornios = cinco guardias."])
Q.q("1.G Perspectiva", r"¿Qué actitud expresa la voz que dice «Antonio, ¿quién eres tú?»?",
    "reproche y decepción porque Antonio no se defendió", [("admiración por su valentía", "Lo contrario."),
                                                           ("alegría por su arresto", "No."),
                                                           ("indiferencia", "No.")],
    "Reproche.", "1.G: la voz niega que sea un verdadero Camborio.",
    ["Ni tú eres hijo de nadie, / ni legítimo Camborio."])
Q.q("1.F Inferencia", r"¿Qué sugiere «Están los viejos cuchillos / tiritando bajo el polvo»?",
    "que el antiguo valor guerrero de los gitanos está olvidado", [("que hace frío en el camino", "Es figurado."),
                                                                   ("que los guardias esconden cuchillos", "No."),
                                                                   ("que Antonio tiene un cuchillo nuevo", "No.")],
    "Decadencia del ideal.", "1.F: personificación de los cuchillos.",
    ["viejos cuchillos … bajo el polvo."])
Q.q("1.E Función", r"¿Qué efecto tiene el detalle de que los guardias «beben limonada todos» mientras Antonio está en el calabozo?",
    "subrayar con ironía la tranquilidad de los guardias frente a la humillación de Antonio", [("mostrar que los guardias son amables", "Es irónico."),
                                                                                                ("indicar que hace calor en Sevilla", "No es la función principal."),
                                                                                                ("anunciar una fiesta", "No.")],
    "Ironía y contraste.", "1.E: los limones de Antonio vuelven como limonada de los guardias.",
    ["limones … limonada."])
Q.q("2.C Forma", r"¿Qué forma métrica usa Lorca en este poema?",
    "el romance: octosílabos con rima asonante en los versos pares", [("el soneto", "No tiene catorce versos."),
                                                                     ("el verso libre", "Tiene métrica y rima."),
                                                                     ("la redondilla", "No hay rima abba.")],
    "Romance (ó-o).", "2.C: Lorca renueva la forma tradicional.",
    ["Camborios, toros, garboso, ojos → ó-o."])

Q.sec("Lectura: crítica literaria")
Q.src(r"Texto 2 \textperiodcentered\ Crítica literaria (texto escrito para esta práctica) \textperiodcentered\ «Dos voces de la Cuba negra»", [
    r"Entre la «Balada de los dos abuelos» de Nicolás Guillén (1934) y «Mujer negra» de Nancy Morejón (1975) median cuatro décadas y una revolución. Ambos poemas vuelven a la historia de la esclavitud, pero la miran desde lugares distintos.",
    r"Guillén convierte esa historia en una herencia doble. Su hablante ve a sus dos abuelos, el africano y el español, como sombras que lo acompañan; el poema recorre la violencia del pasado colonial y termina con un abrazo entre ellos. La identidad cubana, para Guillén, es mestiza: no borra el dolor, pero lo reconcilia.",
    r"Morejón elige otro camino. Su voz no es la de un descendiente que recuerda, sino la de una mujer que lo ha vivido todo en primera persona: el viaje forzado, el trabajo, la rebelión. No hay reconciliación con el amo, sino una toma de la historia: la mujer negra deja de ser objeto del relato para convertirse en su protagonista.",
    r"Leídos juntos, los dos poemas muestran cómo la poesía afrocubana pasó de reclamar un lugar en la identidad nacional a reclamar la voz misma de la historia.",
], 7, note="Texto crítico original escrito para esta práctica.")
Q.q("1.B Tema", r"¿Cuál es la tesis principal del texto crítico?",
    "Los dos poemas miran la historia de la esclavitud desde perspectivas distintas: la reconciliación mestiza y la voz protagonista.", [("Los dos poemas son idénticos.", "Subraya las diferencias."),
                                                                                                                                        ("Morejón rechaza la poesía afrocubana.", "No."),
                                                                                                                                        ("Guillén escribe después de la revolución.", "Escribe en 1934.")],
    "Dos miradas.", "1.B: tesis del crítico.",
    ["la miran desde lugares distintos."])
Q.q("1.A Comprensión", r"Según el crítico, ¿cómo termina la «Balada de los dos abuelos»?",
    "con un abrazo entre los dos abuelos", [("con la muerte del abuelo español", "No."),
                                            ("con una rebelión de esclavos", "No."),
                                            ("con el viaje del hablante a África", "No.")],
    "Abrazo.", "1.A: detalle explícito.",
    ["termina con un abrazo entre ellos."])
Q.q("3.B Comparación", r"Según el crítico, ¿qué diferencia hay entre la voz de Guillén y la de Morejón?",
    "Guillén habla como descendiente que recuerda; Morejón da voz a una mujer que vivió la historia en primera persona.", [("Guillén habla en primera persona y Morejón en tercera.", "No es lo que se afirma."),
                                                                                                                           ("Ambos hablan como amos.", "No."),
                                                                                                                           ("Morejón habla como el abuelo español.", "No.")],
    "Descendiente vs. protagonista.", "3.B: contraste de perspectivas.",
    ["no es la de un descendiente que recuerda."])
Q.q("2.E Contexto", r"¿Qué hecho histórico separa los dos poemas, según el crítico?",
    "la Revolución cubana", [("la independencia de Cuba en 1898", "Ambos poemas son posteriores."),
                             ("la Guerra Civil española", "No se menciona."),
                             ("la llegada de Colón", "No.")],
    "1959.", "2.E: «cuatro décadas y una revolución».",
    ["median cuatro décadas y una revolución."])
Q.q("1.F Inferencia", r"¿Qué quiere decir el crítico con «una toma de la historia»?",
    "que la mujer negra se apropia del relato y se convierte en sujeto de la historia", [("que la mujer conquista un territorio", "Es figurado."),
                                                                                         ("que la historia se borra", "No."),
                                                                                         ("que la poeta escribe un libro de historia", "No.")],
    "Apropiación del relato.", "1.F: metáfora del crítico.",
    ["deja de ser objeto del relato para convertirse en su protagonista."])
Q.q("1.G Perspectiva", r"¿Qué actitud tiene el crítico hacia los dos poemas?",
    "analítica y respetuosa hacia ambos", [("despectiva hacia Guillén", "No."),
                                           ("indiferente", "No."),
                                           ("burlona", "No.")],
    "Análisis equilibrado.", "1.G: actitud del crítico.",
    ["Leídos juntos, los dos poemas muestran…"])
Q.q("1.E Función", r"¿Qué función tiene el último párrafo?",
    "sintetizar la comparación en una conclusión sobre la evolución de la poesía afrocubana", [("introducir un tercer poema", "No."),
                                                                                                 ("narrar la biografía de Morejón", "No."),
                                                                                                 ("contradecir la tesis", "La confirma.")],
    "Conclusión.", "1.E: función estructural.",
    ["pasó de reclamar un lugar … a reclamar la voz."])

Q.frq(kind="Text and Art Comparison", head=r"Question 2 \textperiodcentered\ Text and Art Comparison \textperiodcentered\ 6 points \textperiodcentered\ about 15 minutes", mins=15,
      directions=[r"Lee el texto y observa la imagen (aquí descrita con palabras). Luego, contesta en español: compara cómo se representa el tema del dolor femenino en el texto y en la imagen. Luego, relaciona el tema con el período, el movimiento o el género del texto."],
      sources=[dict(title=r"Texto \textperiodcentered\ Alfonsina Storni, «Peso ancestral» (1919)", paras=[
          r"Tú me dijiste: no lloró mi padre;\\ tú me dijiste: no lloró mi abuelo;\\ no han llorado los hombres de mi raza,\\ eran de acero.",
          r"Así diciendo te brotó una lágrima\\ y me cayó en la boca\ldots; más veneno\\ yo no he bebido nunca en otro vaso\\ así pequeño.",
          r"Débil mujer, pobre mujer que entiende,\\ dolor de siglos conocí al beberlo.\\ Oh, el alma mía soportar no puede\\ todo su peso."]),
               dict(title=r"Imagen \textperiodcentered\ Frida Kahlo, \emph{Las dos Fridas}, 1939 (Museo de Arte Moderno, Ciudad de México)", paras=[
          r"Descripción para esta práctica: dos mujeres idénticas, las dos Fridas, están sentadas una junto a la otra y se dan la mano. Una lleva un vestido blanco de estilo europeo; la otra, un traje tradicional mexicano. Ambas tienen el corazón visible fuera del pecho, unidos por una arteria. La Frida del vestido blanco sujeta con unas pinzas la arteria cortada, y la sangre mancha su falda. Detrás, un cielo gris y tormentoso."])],
      model=[r"Tanto el poema de Storni como el cuadro de Kahlo representan el dolor femenino a través del cuerpo. En «Peso ancestral», el dolor se recibe físicamente: la lágrima del hombre «me cayó en la boca» y la hablante la bebe como «veneno». En Las dos Fridas, el dolor también es corporal: los corazones están fuera del pecho y la sangre gotea sobre el vestido blanco.",
             r"Sin embargo, el origen del dolor es distinto. En Storni, el sufrimiento es heredado y compartido: la hablante descubre «dolor de siglos» que los hombres «de acero» no expresan y que las mujeres deben cargar. En Kahlo, el dolor nace de una división interior: dos versiones de la misma mujer, una europea y otra mexicana, unidas por una arteria cortada que una de ellas intenta cerrar. Mientras Storni habla de un peso que viene de fuera, Kahlo muestra una herida dentro del propio yo.",
             r"El tema se relaciona con la poesía femenina de principios del siglo XX, en la que autoras como Storni critican los roles de género. Sus estrofas breves, con un verso final corto («eran de acero», «todo su peso»), concentran el golpe emocional."],
      rows=[("Content", 3, "compares how both works represent women's pain, with evidence from each (the tear as poison, «dolor de siglos» / exposed hearts, cut artery, blood); notes a difference (inherited vs. internal division); connects to early 20th-century women's poetry", "describing the painting without comparison; no link to period or movement"),
            ("Language", 3, "accurate Spanish; comparison connectors; precise vocabulary", "frequent errors")],
      tips=["The first paragraph states the shared theme with a detail from each work.", "Sin embargo introduces the key difference, supported from both works.",
            "The last paragraph connects theme and form to the period.", "About 210 words."],
      ask="Escribe tu respuesta en español (unas 150–200 palabras). Luego, puntúala con la guía.", lines=12)

GUIDE, QSET = G, Q
