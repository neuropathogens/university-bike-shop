from ap_wl.model import Doc

STEM = "07-boom"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 7: El Boom latinoamericano", r"Unit 7 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 7 reads seven required stories and prose texts by the writers of the Boom and their immediate precursors: Jorge Luis Borges's ``Borges y yo'' and ``El Sur'', Julio Cortázar's ``La noche boca arriba'', Carlos Fuentes's ``Chac Mool'', Gabriel García Márquez's ``La siesta del martes'' and ``El ahogado más hermoso del mundo'', and Juan Rulfo's ``No oyes ladrar los perros''. This guide sets out the context and the two modes most often tested (lo fantástico and el realismo mágico), each work's plot, techniques and themes, and a Text Explanation kit. All seven works are under copyright, so they are summarized and analyzed here, not quoted; the question set's free-response task uses the public-domain ending of Quiroga's ``El hijo'' (Unit 5), a precursor of the Boom's play between reality and illusion. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 11+ \qquad Endings I can explain: \blank[8em]",
        short="Unit 7", sub="El Boom latinoamericano")

G.sec("Context: the Boom, lo fantástico and el realismo mágico")
G.tex(r"""
\begin{compare}{Term}{What it means}{In the course}
El Boom & the international success of Latin American fiction in the 1960s, with Barcelona publishers and the Cuban Revolution (1959) as backdrop & Cortázar, Fuentes, García Márquez; Borges and Rulfo as masters before it \\
Lo fantástico & an impossible event breaks into a realistic world and leaves the reader in doubt & Borges, Cortázar, Fuentes \\
El realismo mágico & the extraordinary is told as ordinary, from a collective, matter-of-fact point of view & García Márquez \\
Narrative techniques & fragmented or circular time, inversion of dream and reality, unreliable or plural narrators, open endings & all \\
\end{compare}

\begin{keyidea}[Fantastic or magical?]
In \textbf{lo fantástico}, characters and readers are disturbed by the impossible (a statue that comes alive, a dream that becomes real). In \textbf{realismo mágico}, no one in the story is surprised (a drowned giant is simply measured, dressed and named). Ask: does the text treat the extraordinary as a problem or as normal?
\end{keyidea}
""")
G.q("1 Boom", r"How does magical realism differ from the fantastic?",
    "Magical realism narrates the extraordinary as normal; the fantastic presents it as a disturbing break in reality.", [
        ("Magical realism uses only realistic events.", "It includes extraordinary events, told as normal."),
        ("The fantastic never includes realistic settings.", "It needs a realistic world to break."),
        ("They are the same thing.", "The course distinguishes them.")],
    "Normal vs. inquietante.", "The narrator's and characters' reaction is the key.",
    ["¿Sorpresa o naturalidad?"])
G.q("1 Boom", r"Which writer is most associated with magical realism?",
    "Gabriel García Márquez", [("Jorge Luis Borges", "Borges is a master of the fantastic and metaphysical."),
                               ("Antonio Machado", "Unit 5, Spanish poetry."),
                               ("Garcilaso de la Vega", "Unit 2.")],
    "García Márquez → realismo mágico.", "Cien años de soledad (1967) defined the mode for readers worldwide.",
    ["Macondo."])

G.sec("Jorge Luis Borges: ``Borges y yo'' and ``El Sur''")
G.tex(r"""
\textbf{``Borges y yo'' (1960).} A brief prose text in which the speaker (``yo'') describes ``Borges'', the famous writer whose name appears in literary circles and anthologies, as a separate person who takes over his tastes and habits. The private self feels he is gradually yielding everything to the public one, and ends unsure which of the two is writing. Themes: la dualidad del ser; identity and authorship (la creación literaria).

\textbf{``El Sur'' (1953).} Juan Dahlmann, a librarian in Buenos Aires of mixed German and criollo descent, hits his head on a window, develops septicemia and nearly dies in a sanatorium. Released, he travels south to his family's ranch. In a general store, young men provoke him; an old gaucho throws him a dagger, and he walks out to a knife fight he cannot win. Borges suggested the story can also be read as Dahlmann's dream in the sanatorium: the romantic death he would have wished for.

\begin{compare}{Feature}{In ``El Sur''}{Effect}
Two lineages & German grandfather vs. criollo grandfather & dualidad del ser; Argentine identity \\
Parallels & the sanatorium and the store; the knife fight and the operation & the second half may mirror the first \\
Ambiguity & real journey or dream & the reader must choose \\
\end{compare}
""")
G.q("2 Borges", r"What is the central idea of ``Borges y yo''?",
    "the split between the private self and the public writer", [("a journey to the south of Argentina", "That is «El Sur»."),
                                                                 ("a quarrel between two friends", "Both are the same man."),
                                                                 ("the history of the Argentine library", "No.")],
    "Dualidad: yo / Borges.", "The speaker doubts which of the two writes the page.",
    ["el hombre privado vs. el autor famoso."])
G.q("2 Borges", r"Why can ``El Sur'' be read in two ways?",
    "The journey and the knife fight may be real, or a dream Dahlmann has while dying in the sanatorium.", [("The story has two different narrators who disagree.", "One narrator."),
                                                                                                         ("Borges wrote two endings.", "One ending, ambiguous."),
                                                                                                         ("Dahlmann has a twin brother.", "No.")],
    "Ambigüedad realidad / sueño.", "Parallels between the two halves support the dream reading.",
    ["sanatorio ↔ almacén."])

G.sec("Cortázar and Fuentes: the past breaks into the present")
G.tex(r"""
\textbf{Cortázar, ``La noche boca arriba'' (1956).} A man has a motorcycle accident in a modern city and is taken to a hospital. In fever he dreams that he is a Moteca fleeing Aztec warriors during the ``guerra florida'', the war fought to capture victims for sacrifice. The two stories alternate, the dream growing more vivid. In the end the Moteca lies on the sacrificial stone and understands that the ``dream'' was the other one: the city and the motorcycle were the dream. Techniques: alternation, inversion, the sense of smell and sound as bridges between worlds; theme: el tiempo y el espacio, reality and dream.

\textbf{Fuentes, ``Chac Mool'' (1954).} After Filiberto drowns, a friend reads his diary. Filiberto bought a statue of Chac Mool, the rain god; it softened, came alive, filled the house with water and took control of his life. At the end, the friend arrives at the house and a strange, aging Indigenous man opens the door. Theme: the indigenous past is not dead in modern Mexico; lo fantástico through a diary whose reliability is uncertain.
""")
G.q("3 Cortázar", r"What is revealed at the end of ``La noche boca arriba''?",
    "The Moteca's world is real, and the modern city was the dream.", [("The motorcyclist wakes up healthy.", "The inversion is the twist."),
                                                                      ("The Aztecs and the doctors are the same people.", "Not stated."),
                                                                      ("It was all a film.", "No.")],
    "Inversión.", "The story overturns the reader's assumption about which world is the dream.",
    ["la ciudad moderna era el sueño."])
G.q("3 Fuentes", r"Through what does the reader learn Filiberto's story in ``Chac Mool''?",
    "his diary, read by a friend after his death", [("a letter Filiberto sends to the Chac Mool", "No."),
                                                    ("a police report", "No."),
                                                    ("Filiberto's own spoken confession", "No.")],
    "Diario → narrador poco fiable.", "The diary format makes the fantastic events hard to verify.",
    ["diario + amigo lector."])

G.sec("García Márquez and Rulfo")
G.tex(r"""
\textbf{García Márquez, ``La siesta del martes'' (1962).} A poor woman and her daughter arrive by train in a hot town at siesta time to visit the grave of her son, Carlos Centeno, shot dead while trying to break into a house. The priest is reluctant; the mother answers with calm dignity that her son was a good man. As they leave, the townspeople gather to watch. Themes: a mother's dignity against the town's judgment; poverty and justice. A realist story without magic.

\textbf{García Márquez, ``El ahogado más hermoso del mundo'' (1968).} Children find a drowned man on the beach of a poor fishing village. He is the tallest, strongest, most beautiful man they have seen; the women dress him, name him Esteban and imagine his life. The village gives him a splendid funeral and decides to make its houses wider and more colorful so it will be remembered. Magical realism; theme: imagination and community transform a place.

\textbf{Rulfo, ``No oyes ladrar los perros'' (1953).} At night, a father carries his wounded adult son on his shoulders toward the town of Tonaya, looking for a doctor and asking the son whether he can hear dogs barking. The son, who has become a bandit, answers less and less. The father reproaches him and recalls his dead mother. At the end, they arrive; the dogs are barking, and the father realizes the son never helped even with that hope. Themes: father and son, guilt, love and resentment; spare dialogue, rural Mexico after the Revolution.
""")
G.q("4 García Márquez", r"In ``El ahogado más hermoso del mundo'', what changes in the village because of the drowned man?",
    "The villagers decide to make their houses and lives larger and more beautiful.", [("They leave the village forever.", "No."),
                                                                                      ("They become rich by selling his body.", "No."),
                                                                                      ("They forget him immediately.", "The opposite.")],
    "Transformación colectiva.", "The extraordinary visitor reshapes the community's imagination.",
    ["casas más anchas, colores alegres."])
G.q("4 Rulfo", r"In ``No oyes ladrar los perros'', why does the father keep asking whether the son can hear dogs?",
    "Barking dogs would mean they have reached the town and a doctor.", [("He wants to buy a dog.", "No."),
                                                                         ("Dogs are chasing them.", "No."),
                                                                         ("He is testing his son's memory.", "No.")],
    "Perros = pueblo = esperanza.", "The dogs are the sign of arrival and of hope.",
    ["Tonaya, médico."])
G.q("4 García Márquez", r"What defines the mother in ``La siesta del martes''?",
    "her calm dignity in the face of the town's judgment of her son", [("her anger and desire for revenge", "She is serene."),
                                                                       ("her fear of the priest", "She is firm."),
                                                                       ("her wealth", "She is poor.")],
    "Dignidad.", "The story turns on how the mother holds herself.",
    ["el pueblo mira; ella no baja la cabeza."])

G.sec("Task kit: explaining a theme across a whole story")
G.tex(r"""
\begin{compare}{Technique}{What it does}{Example}
Circular or mirrored structure & the ending repeats or reflects the beginning & ``El Sur'': sanatorium and store \\
Inversion & what seemed real becomes the dream & ``La noche boca arriba'' \\
Unreliable narrator & the reader doubts the account & ``Chac Mool'' (a diary); ``El hijo'' (a hallucinating father) \\
Final twist & a last sentence changes the meaning of all that came before & Quiroga, ``El hijo'': ``Pues ese padre va solo.'' \\
Open ending & the text leaves a question unanswered & ``El Sur'' \\
\end{compare}

\begin{trap}
In a Text Explanation, the excerpt may come from any point in the story. Explain the theme from the beginning to the end of the work, and name the period correctly: ``El hijo'' (1928) belongs with Modernismo and the regional story of the early 20th century, not with the Boom itself.
\end{trap}
""")
G.q("5 Techniques", r"Which technique does ``El hijo'' share with ``La noche boca arriba''?",
    "a final twist that reverses what the reader believed was real", [("a circular plot set in Buenos Aires", "No."),
                                                                      ("a narrator who is a stone statue", "No."),
                                                                      ("a moral in verse at the end", "That is Conde Lucanor.")],
    "Giro final.", "Both overturn the reader's sense of reality in the last lines.",
    ["Quiroga: «Pues ese padre va solo»; Cortázar: la ciudad era el sueño."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 7: El Boom latinoamericano: Question Set", r"Unit 7 \textperiodcentered\ Question Set",
        abstract=r"""Three multiple-choice sets as on the exam: a listening presentation on the fantastic and magical realism (printed as a transcript), a passage of literary criticism on ``La noche boca arriba'' and a non-required story fragment in the manner of magical realism, followed by a Text Explanation (6 points) on the ending of Quiroga's ``El hijo'', with the scoring guide and a model response. Questions are in Spanish. Quiroga is quoted from a public-domain edition; the transcript, the criticism and the story fragment are original and do not quote the copyrighted works they discuss. Allow about 25 minutes for the multiple choice and 15 for the short answer.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Text Explanation: \blank\ / 6 \qquad Target: 15+ MCQ and 5+ short answer",
        short="Unit 7", sub="El Boom latinoamericano")

Q.sec("Comprensión auditiva: presentación")
Q.src(r"Audio 1 \textperiodcentered\ Presentación (transcripción) \textperiodcentered\ «Lo imposible en la página»", [
    r"(PROFESOR) Pensemos en dos maneras de contar lo imposible. En un cuento fantástico, un hombre descubre que la estatua que compró se está volviendo humana. Él se asusta, duda de su razón, escribe un diario para entender. Lo imposible es una amenaza.",
    r"(PROFESOR) En un cuento de realismo mágico, en cambio, el mar trae a la playa a un ahogado gigantesco, y nadie se pregunta si eso es posible: las mujeres le cosen ropa, le ponen nombre y hasta discuten sobre su vida. Lo extraordinario se cuenta con la misma voz con que se cuenta el precio del pescado.",
    r"(PROFESOR) Esa diferencia no es solo de técnica. En el realismo mágico, la comunidad comparte una manera de ver el mundo en la que lo maravilloso tiene un lugar. En lo fantástico, el individuo moderno se queda solo frente a algo que su razón no puede explicar.",
    r"(PROFESOR) Por eso, al leer, pregúntense siempre: ¿quién se sorprende? Si nadie se sorprende, probablemente estamos ante el realismo mágico.",
], 5, note="Transcripción original escrita para esta práctica.")
Q.q("1.A Comprensión", r"Según el profesor, ¿cómo reacciona el personaje del cuento fantástico ante la estatua?",
    "se asusta y duda de su razón", [("la acepta con naturalidad", "Eso es el realismo mágico."),
                                     ("la vende inmediatamente", "No."),
                                     ("la destruye", "No.")],
    "Miedo y duda.", "1.A: detalle explícito.",
    ["Él se asusta, duda de su razón."])
Q.q("2.E Obras", r"¿A qué obra de la lista alude el ejemplo del ahogado gigantesco?",
    "a «El ahogado más hermoso del mundo»", [("a «La noche boca arriba»", "No hay ahogado en ese cuento."),
                                             ("a «El Sur»", "No."),
                                             ("a «La siesta del martes»", "No.")],
    "García Márquez.", "2.E: conexión con una obra de la lista.",
    ["las mujeres le cosen ropa, le ponen nombre."])
Q.q("1.E Función", r"¿Qué función tiene la comparación con «el precio del pescado»?",
    "mostrar que en el realismo mágico lo extraordinario se narra con tono cotidiano", [("indicar que el pueblo es pobre", "No es la función."),
                                                                                        ("criticar a los pescadores", "No."),
                                                                                        ("introducir un nuevo cuento", "No.")],
    "Tono cotidiano.", "1.E: una imagen concreta aclara el concepto.",
    ["con la misma voz con que se cuenta el precio del pescado."])
Q.q("1.B Tema", r"Según el profesor, ¿qué diferencia de fondo hay entre los dos modos?",
    "El realismo mágico refleja una visión compartida del mundo; lo fantástico, la soledad del individuo ante lo inexplicable.", [("Solo se diferencian en la extensión.", "Dice que no es solo técnica."),
                                                                                                                                 ("Lo fantástico es más antiguo que el realismo mágico.", "No se dice."),
                                                                                                                                 ("El realismo mágico excluye a la comunidad.", "Lo contrario.")],
    "Comunidad vs. individuo.", "1.B: idea central.",
    ["la comunidad comparte una manera de ver el mundo."])
Q.q("1.F Inferencia", r"Según la pregunta final del profesor, ¿cómo se reconoce el realismo mágico?",
    "porque ningún personaje se sorprende ante lo extraordinario", [("porque el cuento ocurre en el mar", "No."),
                                                                    ("porque hay un narrador en primera persona", "No."),
                                                                    ("porque el final es feliz", "No.")],
    "¿Quién se sorprende?", "1.F: criterio práctico.",
    ["Si nadie se sorprende…"])

Q.sec("Lectura: crítica literaria")
Q.src(r"Texto 1 \textperiodcentered\ Crítica literaria (texto escrito para esta práctica) \textperiodcentered\ «El otro lado de la noche»", [
    r"«La noche boca arriba» empieza como un relato realista: una ciudad, una motocicleta, un accidente, un hospital. El lector se siente seguro: sabe dónde está la realidad. Por eso acepta sin inquietud que el protagonista, con fiebre, sueñe que es un moteca perseguido por guerreros aztecas durante la guerra florida.",
    r"Cortázar construye entonces un vaivén. Las secciones del hospital y las de la selva se alternan, y lo que parecía un sueño gana cada vez más presencia: olores de pantano, el sonido de los tambores, el miedo físico. El hospital, en cambio, se vuelve cada vez más borroso, como si fuera él el lugar soñado.",
    r"El final no es un simple golpe de efecto. Cuando el moteca, tendido boca arriba en la piedra del sacrificio, comprende que la ciudad era el sueño, el lector descubre que había confiado en la versión equivocada. El cuento no solo invierte dos mundos: pone en duda nuestra costumbre de considerar «real» lo moderno y «primitivo» lo antiguo.",
], 8, note="Texto crítico original escrito para esta práctica.")
Q.q("1.A Comprensión", r"Según el crítico, ¿cómo empieza el cuento?",
    "como un relato realista sobre un accidente en una ciudad moderna", [("con la guerra florida", "Esta aparece después, como sueño."),
                                                                          ("con la muerte del protagonista", "No."),
                                                                          ("con un diálogo entre aztecas", "No.")],
    "Inicio realista.", "1.A: detalle explícito.",
    ["una ciudad, una motocicleta, un accidente, un hospital."])
Q.q("1.C Técnica", r"¿Qué técnica narrativa describe el crítico con la palabra «vaivén»?",
    "la alternancia entre las secciones del hospital y las de la selva", [("el uso del monólogo interior en verso", "No."),
                                                                          ("la narración en segunda persona", "No."),
                                                                          ("el orden cronológico estricto", "No.")],
    "Alternancia.", "1.C: estructura del cuento.",
    ["se alternan."])
Q.q("1.E Función", r"¿Qué efecto tienen los «olores de pantano» y el «sonido de los tambores», según el crítico?",
    "hacer que el mundo del sueño parezca cada vez más real", [("situar el cuento en Buenos Aires", "No."),
                                                               ("mostrar que el protagonista está sano", "No."),
                                                               ("introducir un humor absurdo", "No.")],
    "Sensaciones → realidad.", "1.E: los sentidos dan presencia al sueño.",
    ["lo que parecía un sueño gana cada vez más presencia."])
Q.q("1.F Inferencia", r"¿Por qué dice el crítico que el lector «había confiado en la versión equivocada»?",
    "porque asumió que la ciudad moderna era la realidad y la selva el sueño", [("porque el narrador miente sobre su nombre", "No."),
                                                                                ("porque el cuento tiene dos autores", "No."),
                                                                                ("porque el hospital no existe en ningún momento", "Demasiado absoluto.")],
    "Inversión de expectativas.", "1.F: el final corrige la lectura del lector.",
    ["la ciudad era el sueño."])
Q.q("1.B Tema", r"Según el último párrafo, ¿qué pone en duda el cuento?",
    "la costumbre de considerar real lo moderno y primitivo lo antiguo", [("la existencia de las motocicletas", "No."),
                                                                         ("la eficacia de los hospitales", "No."),
                                                                         ("la historia de los aztecas", "No.")],
    "Crítica de una jerarquía.", "1.B: tesis del crítico.",
    ["pone en duda nuestra costumbre…"])
Q.q("1.G Perspectiva", r"¿Qué actitud tiene el crítico hacia el final del cuento?",
    "lo valora como algo más profundo que un golpe de efecto", [("lo considera un truco barato", "Dice que no es un simple golpe de efecto."),
                                                                ("lo encuentra confuso y fallido", "No."),
                                                                ("le es indiferente", "No.")],
    "Valoración positiva.", "1.G: actitud del crítico.",
    ["El final no es un simple golpe de efecto."])
Q.q("2.C Modo", r"Según el texto, ¿a qué modo narrativo pertenece «La noche boca arriba»?",
    "a lo fantástico, porque lo imposible rompe un mundo realista e inquieta al lector", [("al realismo mágico, porque nadie se sorprende", "El protagonista y el lector se inquietan."),
                                                                                          ("al Naturalismo", "No."),
                                                                                          ("a la novela picaresca", "No.")],
    "Lo fantástico.", "2.C: modo del cuento.",
    ["El lector se siente seguro … luego duda."])
Q.q("2.E Contexto", r"¿Qué es la «guerra florida» mencionada en el texto?",
    "una guerra de los aztecas para capturar prisioneros destinados al sacrificio", [("una fiesta de flores en la ciudad moderna", "No."),
                                                                                     ("una guerra entre españoles y franceses", "No."),
                                                                                     ("un concurso de jardinería", "No.")],
    "Guerra florida = captura para el sacrificio.", "2.E: contexto cultural mesoamericano.",
    ["piedra del sacrificio."])

Q.sec("Lectura: obra fuera de la lista")
Q.src(r"Texto 2 \textperiodcentered\ «El río que subía» (fragmento de un cuento escrito para esta práctica)", [
    r"El martes en que el río empezó a correr hacia arriba, nadie en San Telmo pensó en llamar al gobernador. El padre Anselmo lo bendijo desde el puente, por si acaso, y las mujeres siguieron lavando la ropa como siempre, aunque ahora tenían que levantar los brazos para alcanzar el agua.",
    r"Los niños fueron los primeros en aprovecharlo: pescaban sardinas en el aire, de pie sobre los tejados, con anzuelos de alfiler. El alcalde, en cambio, pasó tres noches sin dormir calculando si un río que sube debía pagar los mismos impuestos que uno que baja.",
    r"Sólo mi abuela no dio importancia al asunto. «Ya lo vi una vez», dijo, mientras pelaba papas, «el año en que nació tu madre. Duró hasta que alguien se enamoró de verdad». Y como en San Telmo nadie se había enamorado de verdad en mucho tiempo, el río siguió subiendo durante todo el verano.",
], 7, note="Texto original escrito para esta práctica.")
Q.q("1.A Comprensión", r"¿Cómo reaccionan los habitantes de San Telmo ante el río que sube?",
    "con naturalidad, adaptando su vida diaria al fenómeno", [("con pánico, huyendo del pueblo", "No."),
                                                             ("llamando al gobernador", "Nadie lo llama."),
                                                             ("negando que ocurra", "Lo aprovechan.")],
    "Naturalidad.", "1.A: reacciones explícitas.",
    ["siguieron lavando la ropa como siempre."])
Q.q("2.C Modo", r"¿Qué rasgo del realismo mágico se observa en el fragmento?",
    "lo extraordinario se narra como algo cotidiano", [("el protagonista duda de su razón", "Eso es lo fantástico."),
                                                       ("un narrador científico explica el fenómeno", "No."),
                                                       ("el texto es un poema en verso", "Es prosa.")],
    "Lo maravilloso cotidiano.", "2.C: rasgo del modo.",
    ["pescaban sardinas en el aire."])
Q.q("1.D Tono", r"¿Qué tono tiene la descripción del alcalde?",
    "humorístico e irónico", [("trágico", "No."),
                              ("solemne", "No."),
                              ("indignado", "No.")],
    "Humor.", "1.D: el impuesto de un río que sube.",
    ["si un río que sube debía pagar los mismos impuestos…"])
Q.q("1.C Recursos", r"«pescaban sardinas en el aire, de pie sobre los tejados» es",
    "una imagen hiperbólica y maravillosa", [("una descripción realista", "No es posible en la realidad."),
                                             ("una metonimia", "No."),
                                             ("un apóstrofe", "No.")],
    "Hipérbole maravillosa.", "1.C: imagen típica del modo.",
    ["sardinas en el aire."])
Q.q("1.I Personajes", r"¿Qué revela la reacción de la abuela?",
    "que el fenómeno forma parte de la memoria del pueblo y no la sorprende", [("que tiene miedo del río", "No."),
                                                                               ("que no cree lo que ve", "Lo acepta."),
                                                                               ("que quiere irse de San Telmo", "No.")],
    "Memoria colectiva.", "1.I: el personaje encarna la tradición.",
    ["«Ya lo vi una vez»."])
Q.q("1.F Inferencia", r"Según la abuela, ¿qué haría que el río volviera a su curso normal?",
    "que alguien se enamorara de verdad", [("que el alcalde cobrara impuestos", "No."),
                                           ("que el padre Anselmo lo bendijera", "Ya lo bendijo."),
                                           ("que llegara el invierno", "No.")],
    "Amor verdadero.", "1.F: la causa maravillosa.",
    ["Duró hasta que alguien se enamoró de verdad."])
Q.q("3.A Comparación", r"¿Qué tiene en común este fragmento con «El ahogado más hermoso del mundo»?",
    "una comunidad que acepta y transforma lo extraordinario sin asombro", [("un narrador que duda de su cordura", "No."),
                                                                            ("una estatua que cobra vida", "Eso es «Chac Mool»."),
                                                                            ("un final de guerra y sacrificio", "No.")],
    "Comunidad + maravilla.", "3.A: semejanza de modo.",
    ["pueblo, naturalidad, transformación."])

Q.frq(kind="Text Explanation", head=r"Question 1 \textperiodcentered\ Text Explanation \textperiodcentered\ 6 points \textperiodcentered\ about 15 minutes", mins=15,
      directions=[r"Lee el fragmento. Luego, contesta la pregunta en español. Identifica al autor y el período de la obra a la que pertenece este fragmento. Luego, explica el desarrollo del tema de la realidad y la ilusión en la obra completa."],
      sources=[dict(title=r"Fragmento", paras=[
          r"Nimio detalle, después de todo. Bajo el cielo y el aire candentes, a la descubierta por el abra de espartillo, el hombre devuelve a casa con su hijo, sobre cuyos hombros, casi del alto de los suyos, lleva pasado su feliz brazo de padre. Regresa empapado de sudor, y aunque quebrantado de cuerpo y alma, sonríe de felicidad.",
          r"Sonríe de alucinada felicidad\ldots\ Pues ese padre va solo.",
          r"A nadie ha encontrado, y su brazo se apoya en el vacío. Porque tras él, al pie de un poste y con las piernas en alto, enredadas en el alambre de púa, su hijo bienamado yace al sol, muerto desde las diez de la mañana."])],
      model=[r"Este fragmento pertenece a «El hijo», cuento del uruguayo Horacio Quiroga publicado en 1928. Corresponde a las primeras décadas del siglo XX, en la estela del Modernismo y del cuento regional, y anticipa técnicas que luego desarrollaría el Boom.",
             r"El tema de la realidad y la ilusión se desarrolla a lo largo de todo el cuento. Desde el principio, el narrador advierte que el padre, «de estómago y vista débiles, sufre desde hace un tiempo de alucinaciones»: una vez vio a su hijo cubierto de sangre cuando en realidad limaba una hebilla. Cuando el chico no vuelve a mediodía, la angustia del padre crece y el narrador, en estilo indirecto libre, nos hace compartir su esperanza. Por eso, cuando el hijo aparece «bruscamente» y ambos conversan sobre las garzas, el lector también cree en el reencuentro. El fragmento final rompe esa ilusión: el padre sonríe «de alucinada felicidad», pero «va solo» y «su brazo se apoya en el vacío». El hijo está muerto desde las diez, enredado en el alambrado. Así, Quiroga muestra cómo el amor y el dolor pueden construir una realidad falsa, y obliga al lector a descubrir que también él ha sido engañado."],
      rows=[("Content", 3, "identifies author and period (early 20th century, Modernismo / regional story); explains how the theme develops in the whole story (the hallucinations announced at the start, the growing anxiety, the false reunion, the revelation) with evidence", "writing only about the excerpt; wrong period (for example, the Boom itself); summary without development"),
            ("Language", 3, "accurate Spanish; narrative vocabulary (estilo indirecto libre, giro final, narrador); sequence connectors", "frequent errors; limited vocabulary")],
      tips=["The first sentence identifies author, work, year and period, and notes the link to the Boom without mislabeling it.", "The theme is traced from the first mention of hallucinations to the final twist.",
            "The answer explains how the narration deceives the reader as well as the father.", "About 210 words."],
      ask="Escribe tu respuesta en español (unas 150–200 palabras). Luego, puntúala con la guía.", lines=12)

GUIDE, QSET = G, Q
