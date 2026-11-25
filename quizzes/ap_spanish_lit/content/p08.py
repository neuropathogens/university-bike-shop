from ap_wl.model import Doc

STEM = "08-contemporary"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 8: Escritores contemporáneos de Estados Unidos y España", r"Unit 8 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 8 reads four required works from the 1960s to the 1980s (five readings, counting Rivera's two chapters): Tomás Rivera's \emph{\ldots y no se lo tragó la tierra} (two chapters), Sabine Ulibarrí's ``Mi caballo mago'', Isabel Allende's ``Dos palabras'' and Rosa Montero's ``Como la vida misma''. This guide sets out their contexts (Chicano literature and migrant labor, Hispanic New Mexico, Latin American women writers in exile, Spain after Franco), each work's plot, narrative techniques and themes, and a Text Comparison kit. All of these works are under copyright, so they are summarized and analyzed here, not quoted; the question set's essay pairs a public-domain required text (Darío's ``A Roosevelt'', Unit 5) with a contemporary poem written for this series. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Works I can summarize: \blank[8em]",
        short="Unit 8", sub="Escritores contemporáneos de Estados Unidos y España")

G.sec("Context: new voices in the United States and Spain")
G.tex(r"""
\begin{compare}{Context}{Dates}{Works}
Hispanic New Mexico & Spanish-speaking communities since the 1600s, in the U.S. since 1848 & Ulibarrí, \emph{Tierra Amarilla} (1964) \\
The Chicano movement and migrant farm labor & 1960s--70s & Rivera, \emph{\ldots y no se lo tragó la tierra} (1971) \\
Latin American women writers; exile after the 1973 coup in Chile & 1970s--80s & Allende, \emph{Cuentos de Eva Luna} (1989) \\
Spain's transition to democracy & Franco dies 1975; Constitution 1978; journalism and new urban life & Montero, ``Como la vida misma'' \\
\end{compare}

These works give literary form to communities that had been at the margins: Spanish speakers in the United States, migrant workers, women. Common themes: identity between two cultures (las sociedades en contacto), coming of age, the power of language, and the alienation of modern life.
""")
G.q("1 Context", r"Which community's experience is at the center of Tomás Rivera's book?",
    "Mexican American migrant farmworkers in the 1940s--50s", [("the gauchos of the Argentine pampa", "No."),
                                                                 ("the nobility of 17th-century Spain", "No."),
                                                                 ("office workers in Madrid", "That is closer to Montero.")],
    "Trabajadores migrantes.", "Rivera, himself the son of migrant workers, wrote a founding work of Chicano literature.",
    ["campos, sol, familias migrantes."])
G.q("1 Context", r"Why is Hispanic New Mexico important for understanding Ulibarrí?",
    "Spanish-speaking communities lived there for centuries before it became part of the U.S.", [("It was the capital of the Aztec empire.", "No."),
                                                                                                ("It was settled only after 1950.", "The opposite."),
                                                                                                ("It is where Allende lived in exile.", "No.")],
    "Herencia hispana.", "Ulibarrí writes from a long-rooted rural Hispanic culture.",
    ["Tierra Amarilla, Nuevo México."])

G.sec("Tomás Rivera, \\ldots y no se lo tragó la tierra (1971)")
G.tex(r"""
\textbf{Form.} A book of short chapters and vignettes from one year in the life of a migrant community, filtered through a boy's memory. The course reads two chapters.

\textbf{``\ldots y no se lo tragó la tierra''.} After his father and then his younger brother suffer sunstroke while working in the fields, and while his mother prays, a boy angrily curses God, expecting the earth to swallow him as he had been told it would. It does not. He feels a new strength and a new freedom: the fear that had controlled him is gone. Themes: faith and doubt, injustice of the work, coming of age.

\textbf{``La noche buena''.} Doña María, who almost never leaves the house, decides to go into town alone to buy Christmas presents for her children. The noise, the crowds and the language overwhelm her; confused, she walks out of a store with items she has not paid for, is accused of stealing and faints. Her husband brings her home. Themes: isolation, fear and the barriers of language and class (las sociedades en contacto); a mother's love.
""")
G.q("2 Rivera", r"What does the boy discover when the earth does not swallow him?",
    "that the fear imposed on him had no power, and he feels free and strong", [("that God has punished his family", "He discovers the punishment does not come."),
                                                                               ("that he must stop working in the fields", "No."),
                                                                               ("that his brother has died", "No.")],
    "Liberación del miedo.", "A coming-of-age moment of rebellion and self-assertion.",
    ["la tierra no se lo traga → libertad."])
G.q("2 Rivera", r"What overwhelms doña María in ``La noche buena''?",
    "the crowds, the noise and the unfamiliar language and spaces of the town", [("a flood in the fields", "No."),
                                                                                  ("a conflict with her children", "She goes out for them."),
                                                                                  ("an illness of her husband", "No.")],
    "Aislamiento.", "Her fear shows the isolation of migrant families in an Anglo world.",
    ["sale sola al pueblo → se pierde."])

G.sec("Sabine Ulibarrí, ``Mi caballo mago'' (1964)")
G.tex(r"""
\textbf{Plot.} The first-person narrator recalls his boyhood in rural New Mexico and the legend of a wild white stallion that no one could catch. He sees the horse in summer and dreams of it. In winter, he tracks it through the snow and finally ropes it and leads it home, proud. The next morning the horse has escaped; only its tracks remain in the snow. He weeps, but feels that the horse is now his forever in memory, and his father recognizes him as a young man.

\textbf{Features.} Retrospective first person; lyrical, almost legendary prose; the horse as symbol of freedom, beauty and dream; the passage from childhood to adulthood. Themes: coming of age, freedom versus possession, nature and Hispanic rural tradition.
""")
G.q("3 Ulibarrí", r"What does the white horse most likely symbolize?",
    "freedom and an ideal that cannot be possessed", [("wealth for the family", "He does not sell it."),
                                                     ("danger and death", "No."),
                                                     ("the Spanish crown", "No.")],
    "Caballo = libertad, sueño.", "Capturing it and losing it teaches the narrator that some ideals cannot be owned.",
    ["mago, blanco, libre."])
G.q("3 Ulibarrí", r"How does the narrator feel at the end?",
    "sad at the loss but fulfilled, as if he has grown up", [("only angry at his father", "No."),
                                                            ("indifferent", "No."),
                                                            ("afraid of the horse", "No.")],
    "Crecimiento.", "A coming-of-age ending: loss becomes maturity.",
    ["llora y sonríe."])

G.sec("Isabel Allende, ``Dos palabras'' and Rosa Montero, ``Como la vida misma''")
G.tex(r"""
\textbf{Allende, ``Dos palabras'' (1989).} Belisa Crepusculario, born into extreme poverty, discovers that words can be sold and makes a living selling them: letters, poems, insults, speeches. The Mulato kidnaps her for the Coronel, a feared warlord who wants to become president. She writes him a speech that wins the people, and as a gift gives him two secret words. The words obsess him; he cannot forget her. The Mulato brings Belisa back, and the story suggests the Coronel is tamed by love. Themes: the power of language (la creación literaria), gender and power, politics; touches of magical realism.

\textbf{Montero, ``Como la vida misma'' (1980s).} Narrated in the second person, the text follows fifteen tense minutes of a driver in a Madrid traffic jam: aggressive drivers, insults, small victories, until a hard-won parking spot. The ironic title suggests that ordinary life itself is this kind of struggle. Themes: urban alienation, aggression and isolation in modern society; el tiempo y el espacio.
""")
G.q("4 Allende", r"What does Belisa Crepusculario sell?",
    "words: letters, poems, speeches and more", [("fruit at the market", "No."),
                                                 ("horses", "No."),
                                                 ("newspapers", "No.")],
    "Vende palabras.", "Her trade makes language the story's subject.",
    ["oficio de vender palabras."])
G.q("4 Montero", r"What is the effect of the second-person narration in ``Como la vida misma''?",
    "It places the reader in the driver's seat, sharing the stress and aggression.", [("It shows the story is a letter to a friend.", "Not a letter."),
                                                                                       ("It creates distance and objectivity.", "The opposite."),
                                                                                       ("It identifies the narrator as a woman named Rosa.", "No.")],
    "Tú = lector implicado.", "The ``tú'' makes the reader live the jam from inside.",
    ["segunda persona → inmersión."])
G.q("4 Montero", r"What does the title ``Como la vida misma'' suggest?",
    "that the stressful traffic jam reflects everyday life in general", [("that the story is a biography", "No."),
                                                                         ("that the driver is happy", "No."),
                                                                         ("that cars are dangerous", "Too literal.")],
    "Ironía del título.", "The jam becomes a metaphor for modern life.",
    ["atasco = vida cotidiana."])

G.sec("Task kit: Text Comparison across periods")
G.tex(r"""
The Text Comparison pairs a required text with a non-required one; the two may be a century apart. Compare the \emph{devices}, not only the ideas.

\begin{compare}{Device}{Darío, ``A Roosevelt'' (1904)}{A contemporary bilingual poem}
Voice & a public, prophetic ``yo'' that speaks for a continent & a private ``yo'' that speaks for a family \\
Address & apostrophe to Roosevelt, the U.S. & memory of a grandmother; the reader \\
Imagery & Hercules, Mammon, the lion, the sun & a river, a kitchen, a word \\
Identity & ``la América española'', Indigenous and Catholic & between two languages \\
\end{compare}
""")
G.q("5 Comparison", r"Which sentence compares devices rather than only themes?",
    "Mientras Darío usa el apóstrofe para desafiar a Roosevelt con una voz pública, el poema contemporáneo usa el recuerdo íntimo de la abuela.", [
        ("Los dos poemas hablan de la identidad.", "Theme only."),
        ("Darío escribió en 1904.", "Fact only."),
        ("Me gusta más el poema moderno.", "Preference.")],
    "Recurso + efecto en ambos.", "Content rewards analysis of devices in both texts.",
    ["apóstrofe público / recuerdo íntimo."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 8: Escritores contemporáneos de Estados Unidos y España: Question Set", r"Unit 8 \textperiodcentered\ Question Set",
        abstract=r"""Three multiple-choice sets as on the exam: a listening interview with a writer about Rivera's book (printed as a transcript), a passage of literary criticism on Allende's ``Dos palabras'' and a non-required second-person narrative in the manner of contemporary urban fiction, followed by a Text Comparison essay (10 points) on Darío's ``A Roosevelt'' and a contemporary bilingual poem, with the scoring guide and a model essay. Questions are in Spanish. Darío is quoted from a public-domain edition; the transcript, the criticism, the narrative and the poem are original and do not quote the copyrighted works they discuss. Allow about 25 minutes for the multiple choice and 35 for the essay.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Essay: \blank\ / 10 \qquad Target: 15+ MCQ and 7+ essay",
        short="Unit 8", sub="Escritores contemporáneos de Estados Unidos y España")

Q.sec("Comprensión auditiva: entrevista")
Q.src(r"Audio 1 \textperiodcentered\ Entrevista (transcripción) \textperiodcentered\ Un escritor habla de Tomás Rivera", [
    r"(PERIODISTA) Usted dice que leer a Tomás Rivera le cambió la vida. ¿Por qué?",
    r"(ESCRITOR) Porque yo también crecí siguiendo las cosechas. Hasta que leí su libro, pensaba que nuestra vida no era materia de literatura. Rivera me enseñó lo contrario: que el calor del campo, las oraciones de una madre y el miedo de un niño también merecen ser contados.",
    r"(PERIODISTA) El libro está hecho de fragmentos. ¿No resulta difícil de leer?",
    r"(ESCRITOR) Al principio, sí. Pero así funciona la memoria de un niño que se muda cada pocos meses: recuerda escenas sueltas, voces, un año que se mezcla con otro. La forma del libro es la forma de esa vida.",
    r"(PERIODISTA) ¿Qué capítulo recomienda a quien lo lea por primera vez?",
    r"(ESCRITOR) El del niño que maldice. Muchos lo leen como un acto de rebeldía religiosa, y lo es, pero sobre todo es el momento en que alguien descubre que el miedo no es una ley de la naturaleza.",
], 5, note="Transcripción original escrita para esta práctica.")
Q.q("1.A Comprensión", r"¿Qué tiene en común el escritor con los personajes de Rivera?",
    "creció en una familia de trabajadores migrantes", [("nació en España", "No."),
                                                       ("fue maestro de Rivera", "No."),
                                                       ("vive en Nuevo México desde niño", "No se dice.")],
    "siguiendo las cosechas.", "1.A: detalle explícito.",
    ["yo también crecí siguiendo las cosechas."])
Q.q("1.B Tema", r"Según el escritor, ¿qué le enseñó el libro de Rivera?",
    "que la vida de su comunidad también merecía ser literatura", [("que debía dejar de escribir", "Lo contrario."),
                                                                  ("que la religión no importa", "No."),
                                                                  ("que la vida en la ciudad es mejor", "No.")],
    "Dignidad literaria.", "1.B: idea central de su primera respuesta.",
    ["también merecen ser contados."])
Q.q("1.E Función", r"Según el escritor, ¿por qué el libro está hecho de fragmentos?",
    "porque reproduce la memoria de un niño que se muda constantemente", [("porque Rivera no tuvo tiempo de terminarlo", "No."),
                                                                          ("porque es una antología de varios autores", "No."),
                                                                          ("porque así es más fácil de leer", "Dice que al principio es difícil.")],
    "Forma = vida.", "1.E: la estructura imita la experiencia.",
    ["La forma del libro es la forma de esa vida."])
Q.q("1.G Perspectiva", r"¿Cómo interpreta el escritor el capítulo del niño que maldice?",
    "como el descubrimiento de que el miedo puede superarse, más allá de la rebeldía religiosa", [("solo como un pecado del niño", "No."),
                                                                                                 ("como un error de Rivera", "No."),
                                                                                                 ("como un episodio cómico", "No.")],
    "Más allá de la rebeldía.", "1.G: una lectura matizada.",
    ["el miedo no es una ley de la naturaleza."])
Q.q("2.E Contexto", r"¿A qué contexto pertenece la obra de Rivera, según la entrevista?",
    "la vida de las familias mexicoamericanas que trabajaban en las cosechas", [("la España de la Transición", "Eso es Montero."),
                                                                                ("la conquista de México", "No."),
                                                                                ("la Argentina rural del gaucho", "No.")],
    "Literatura chicana.", "2.E: contexto social.",
    ["cosechas, mudanzas, oraciones."])

Q.sec("Lectura: crítica literaria")
Q.src(r"Texto 1 \textperiodcentered\ Crítica literaria (texto escrito para esta práctica) \textperiodcentered\ «El poder de dos palabras»", [
    r"En «Dos palabras», Isabel Allende convierte el lenguaje en mercancía y, al mismo tiempo, en magia. Belisa Crepusculario nace en la pobreza más absoluta y descubre que las palabras pueden venderse; con ese oficio sobrevive y se vuelve libre. Lo que para otros es aire, para ella es un tesoro.",
    r"El Coronel, en cambio, tiene armas y hombres, pero no tiene palabras. Quiere ser presidente y necesita un discurso para ganar a la gente. La relación entre ambos invierte los papeles habituales: el hombre armado depende de la mujer que domina el lenguaje.",
    r"El regalo final de Belisa, dos palabras secretas que el lector nunca conoce, es el centro del cuento. Allende no nos dice cuáles son, y ese silencio es parte de su poder: cada lector las imagina. Así, el cuento termina por demostrar lo que afirma: las palabras más eficaces son las que dejan espacio a la imaginación.",
], 8, note="Texto crítico original escrito para esta práctica.")
Q.q("1.A Comprensión", r"Según el crítico, ¿cómo sobrevive Belisa Crepusculario?",
    "vendiendo palabras", [("vendiendo armas", "Las armas son del Coronel."),
                           ("trabajando para el gobierno", "No."),
                           ("como maestra de escuela", "No.")],
    "Oficio de palabras.", "1.A: detalle explícito.",
    ["descubre que las palabras pueden venderse."])
Q.q("1.I Personajes", r"¿Qué le falta al Coronel, según el crítico?",
    "palabras para ganarse al pueblo", [("armas", "Las tiene."),
                                        ("hombres", "Los tiene."),
                                        ("valor", "No se dice.")],
    "Poder sin palabras.", "1.I: caracterización del Coronel.",
    ["tiene armas y hombres, pero no tiene palabras."])
Q.q("1.F Inferencia", r"¿Qué inversión de papeles señala el crítico?",
    "el hombre armado depende de una mujer que domina el lenguaje", [("Belisa se convierte en coronel", "No."),
                                                                     ("el Mulato se vuelve presidente", "No."),
                                                                     ("el pueblo enseña a hablar a Belisa", "No.")],
    "Género y poder.", "1.F: la palabra vence a la fuerza.",
    ["invierte los papeles habituales."])
Q.q("1.B Tema", r"¿Cuál es el tema central del cuento, según el crítico?",
    "el poder del lenguaje", [("la violencia de la guerra", "Aparece, pero no es el centro."),
                              ("la pobreza del campo", "Es el punto de partida."),
                              ("la historia de un país concreto", "No.")],
    "Lenguaje = poder.", "1.B: tesis del texto crítico.",
    ["convierte el lenguaje en mercancía y en magia."])
Q.q("1.E Función", r"Según el crítico, ¿qué efecto tiene que el lector nunca conozca las dos palabras?",
    "hace que cada lector las imagine, lo cual aumenta su poder", [("crea un error en el argumento", "No."),
                                                                  ("muestra que Belisa olvidó las palabras", "No."),
                                                                  ("indica que las palabras son insultos", "No.")],
    "Silencio productivo.", "1.E: la omisión como recurso.",
    ["ese silencio es parte de su poder."])
Q.q("1.G Perspectiva", r"¿Qué actitud tiene el crítico hacia el final del cuento?",
    "lo considera coherente con lo que el cuento afirma sobre las palabras", [("lo considera incompleto y fallido", "No."),
                                                                              ("le parece demasiado violento", "No."),
                                                                              ("lo encuentra irrelevante", "No.")],
    "Valoración positiva.", "1.G: actitud del crítico.",
    ["el cuento termina por demostrar lo que afirma."])
Q.q("2.C Modo", r"«en mercancía y, al mismo tiempo, en magia» alude a que el cuento combina",
    "elementos realistas y toques de realismo mágico", [("rasgos barrocos y medievales", "No."),
                                                        ("teatro y poesía", "Es un cuento."),
                                                        ("crónica histórica y ensayo", "No.")],
    "Realidad + magia.", "2.C: modo narrativo.",
    ["mercancía (real) + magia."])
Q.q("3.B Conexión", r"¿Con qué obra de la lista comparte «Dos palabras» el tema de la creación literaria y el poder de narrar?",
    "con «Borges y yo», que reflexiona sobre quién escribe", [("con «La siesta del martes»", "Su tema central es la dignidad de una madre."),
                                                             ("con «Peso ancestral»", "Su tema es el dolor heredado."),
                                                             ("con «En una tempestad»", "Su tema es la naturaleza sublime.")],
    "La creación literaria.", "3.B: conexión temática entre obras.",
    ["palabras, escritura, identidad del autor."])

Q.sec("Lectura: obra fuera de la lista")
Q.src(r"Texto 2 \textperiodcentered\ «Las ocho y diez» (narración escrita para esta práctica)", [
    r"Bajas al andén a las ocho y diez y ya sabes que no vas a llegar a tiempo. El metro llega lleno; te empujan, empujas, alguien te pisa y nadie pide perdón. Pegas la nariz a una espalda desconocida que huele a colonia barata y a lluvia.",
    r"En la estación siguiente sube una mujer con un niño dormido. Por un segundo piensas en cederle tu sitio, pero no tienes sitio: tienes veinte centímetros de suelo que defiendes como si fueran tuyos. Miras el teléfono para no mirar a nadie.",
    r"Cuando por fin sales a la calle, el aire frío te parece un premio. Llegas a la oficina a las nueve menos cinco, sudado y orgulloso, como quien vuelve de una guerra. Nadie te pregunta cómo estás. Mañana, a las ocho y diez, volverás a bajar al andén.",
], 7, note="Texto original escrito para esta práctica.")
Q.q("1.C Técnica", r"¿Qué tipo de narrador usa el texto?",
    "un narrador en segunda persona que interpela al lector", [("un narrador en primera persona", "No hay «yo»."),
                                                              ("un narrador omnisciente en tercera persona", "Se usa «tú»."),
                                                              ("un diálogo teatral", "No.")],
    "Tú narrativo.", "1.C: voz narrativa.",
    ["Bajas … sabes … te empujan."])
Q.q("1.E Función", r"¿Qué efecto tiene la segunda persona?",
    "hace que el lector viva la experiencia desde dentro", [("aleja al lector de la escena", "Lo contrario."),
                                                           ("indica que el texto es una carta", "No."),
                                                           ("presenta al autor como personaje histórico", "No.")],
    "Inmersión.", "1.E: efecto del «tú».",
    ["te empujan, empujas."])
Q.q("1.F Inferencia", r"¿Qué revela la frase «tienes veinte centímetros de suelo que defiendes como si fueran tuyos»?",
    "el egoísmo y la hostilidad que impone la vida urbana", [("que el personaje es propietario del metro", "Es irónico."),
                                                            ("que el vagón está vacío", "Lo contrario."),
                                                            ("que el personaje es muy generoso", "No cede su sitio.")],
    "Hostilidad urbana.", "1.F: ironía.",
    ["como si fueran tuyos."])
Q.q("1.D Tono", r"¿Qué tono predomina en «como quien vuelve de una guerra»?",
    "irónico", [("épico y solemne", "La comparación es exagerada a propósito."),
                ("trágico", "No."),
                ("religioso", "No.")],
    "Hipérbole irónica.", "1.D: la guerra diaria del metro.",
    ["sudado y orgulloso, como quien vuelve de una guerra."])
Q.q("1.E Estructura", r"¿Qué función tiene la última frase, «Mañana, a las ocho y diez, volverás a bajar al andén»?",
    "mostrar que la experiencia se repite cada día, en un ciclo sin salida", [("anunciar un cambio en la vida del personaje", "No hay cambio."),
                                                                               ("resolver el conflicto con la mujer del niño", "No."),
                                                                               ("indicar que el personaje se muda", "No.")],
    "Estructura circular.", "1.E: el final vuelve al principio.",
    ["ocho y diez … ocho y diez."])
Q.q("3.A Comparación", r"¿Con qué obra de la lista comparte este texto la narración y el tema?",
    "con «Como la vida misma», de Rosa Montero", [("con «Mi caballo mago»", "No es en segunda persona ni urbano."),
                                                 ("con «La noche buena»", "No es en segunda persona."),
                                                 ("con «Lazarillo de Tormes»", "No.")],
    "Segunda persona + ciudad.", "3.A: semejanza formal y temática.",
    ["atasco / metro; tú."])
Q.q("1.B Tema", r"¿Cuál es el tema principal del texto?",
    "la alienación y la hostilidad de la vida cotidiana en la ciudad", [("la belleza de los viajes", "No."),
                                                                       ("la solidaridad entre pasajeros", "Lo contrario."),
                                                                       ("el éxito profesional", "No.")],
    "Alienación urbana.", "1.B: tema.",
    ["Nadie te pregunta cómo estás."])

Q.frq(kind="Text Comparison", head=r"Question 4 \textperiodcentered\ Text Comparison \textperiodcentered\ 10 points \textperiodcentered\ about 35 minutes", mins=35,
      directions=[r"Lee los dos textos. Luego, escribe un ensayo en español en el que analices los efectos de los recursos literarios que los autores emplean para desarrollar el tema de la identidad hispana frente a Estados Unidos. Apoya tu análisis con ejemplos de los dos textos."],
      sources=[dict(title=r"Texto 1 \textperiodcentered\ Rubén Darío, «A Roosevelt» (1904, fragmento)", paras=[
          r"Los Estados Unidos son potentes y grandes.\\ Cuando ellos se estremecen hay un hondo temblor\\ que pasa por las vértebras enormes de los Andes.\\ Si clamáis, se oye como el rugir del león.\\ {[\ldots]} Sois ricos.\\ Juntáis al culto de Hércules el culto de Mammón;\\ y alumbrando el camino de la fácil conquista,\\ la Libertad levanta su antorcha en Nueva York.",
          r"[\ldots] Tened cuidado. ¡Vive la América española!\\ Hay mil cachorros sueltos del León Español.\\ Se necesitaría, Roosevelt, ser por Dios mismo,\\ el Riflero terrible y el fuerte Cazador,\\ para poder tenernos en vuestras férreas garras.\\ Y, pues contáis con todo, falta una cosa: ¡Dios!"]),
               dict(title=r"Texto 2 \textperiodcentered\ «El río» (poema escrito para esta práctica)", paras=[
          r"Mi abuela cruzó el río con una maleta de cartón\\ y una lengua que no cabía en la aduana.\\ En la escuela me enseñaron a decir mi nombre\\ como si pidiera perdón: Hó-say, no José.",
          r"Pero en la cocina, entre el comal y la radio,\\ el español volvía como vuelve el agua a su cauce:\\ oraciones, refranes, canciones de cuna,\\ y la palabra «mijo», que no cabe en ningún diccionario.",
          r"Hoy hablo dos idiomas y a veces ninguno.\\ Pero cuando digo «abuela», el río\\ ya no me separa de nada:\\ me lleva."])],
      model=[r"«A Roosevelt», de Rubén Darío, y el poema contemporáneo «El río» tratan el tema de la identidad hispana frente a Estados Unidos, pero desde lugares opuestos. Darío, poeta del Modernismo, habla con una voz pública que desafía al poder norteamericano en nombre de todo un continente; el poema contemporáneo, en cambio, usa una voz íntima para mostrar una identidad que se construye entre dos lenguas dentro de Estados Unidos.",
             r"En primer lugar, la voz y el destinatario son muy diferentes. Darío usa el apóstrofe para dirigirse directamente a Estados Unidos y a Roosevelt: «Tened cuidado. ¡Vive la América española!». Las exclamaciones y la segunda persona del plural dan al poema un tono de advertencia y de orgullo colectivo. En «El río», en cambio, no hay un adversario al que hablar: el hablante recuerda a su abuela y cuenta su propia experiencia, por lo que la identidad aparece como algo vivido y no proclamado.",
             r"En segundo lugar, las imágenes revelan dos maneras de entender el encuentro entre culturas. Darío recurre a imágenes de fuerza y de mito: Estados Unidos hace temblar «las vértebras enormes de los Andes» y une «el culto de Hércules» con «el culto de Mammón», es decir, la fuerza y el dinero; frente a ellos, la América española son «mil cachorros sueltos del León Español». El poema contemporáneo usa, en cambio, imágenes cotidianas: «una maleta de cartón», «el comal y la radio». La metáfora de la lengua que «no cabía en la aduana» y la escena del nombre pronunciado «como si pidiera perdón» muestran que el conflicto ya no es entre naciones, sino dentro de una persona.",
             r"Por último, los finales resumen la perspectiva de cada texto. Darío cierra con una antítesis rotunda: Estados Unidos lo tiene todo, pero «falta una cosa: ¡Dios!», afirmando la superioridad espiritual hispana. «El río» termina con una metáfora reconciliadora: el río que separaba ahora «me lleva». La identidad hispana ya no se defiende contra Estados Unidos, sino que se conserva y se transforma en él.",
             r"En conclusión, mientras Darío construye una identidad continental mediante el apóstrofe, la exclamación y las imágenes míticas, el poema contemporáneo la construye mediante la memoria familiar y la metáfora del río, mostrando cómo el tema ha pasado del enfrentamiento a la convivencia de culturas."],
      rows=[("Content", 5, "a comparative thesis on how devices (voice and apostrophe, imagery, the endings) develop the theme in both texts; quotations from both, analyzed for their effect; awareness of the shift from confrontation to coexistence", "two separate summaries; themes without devices; only one text analyzed"),
            ("Language", 5, "accurate, varied Spanish; comparison connectors; literary vocabulary (apóstrofe, antítesis, metáfora, voz poética)", "frequent errors; repetitive structures")],
      tips=["The thesis names the shared theme and the opposite perspectives.", "Each body paragraph treats one device in both texts, with a quotation from each.",
            "The conclusion restates the comparison in terms of devices and their effects.", "About 480 words."],
      ask="Escribe tu ensayo en español (unas 350–450 palabras). Luego, puntúalo con la guía.", lines=22)

GUIDE, QSET = G, Q
