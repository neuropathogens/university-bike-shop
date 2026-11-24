from ap_wl.model import Doc

STEM = "04-science-technology"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 4: Science and Technology", r"Unit 4 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 4 asks how science and technology change daily life, communication and society, and who benefits. Its recommended contexts are innovations and emerging technologies, personal technology and communication, science in everyday life, and the societal impacts of science and technology. This guide gives the vocabulary of technology and science, inventions and scientific projects from the Spanish-speaking world, the digital divide and misinformation, the structures for predictions, hypotheses and data, and an Argumentative Essay kit focused on reading charts. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Chart verbs I can use: \blank[10em]",
        short="Unit 4", sub="Science and Technology")

G.sec("Innovation and emerging technologies")
G.tex(r"""
\begin{vocab}
la inteligencia artificial (IA) & artificial intelligence & \\
el algoritmo / los datos & algorithm / data & \emph{los datos} is plural \\
el invento / el descubrimiento & invention / discovery & \emph{inventar} vs. \emph{descubrir} \\
la energía renovable / solar / eólica & renewable / solar / wind energy & \\
el avance / el desarrollo & advance / development & \\
la patente & patent & \\
el observatorio / el telescopio & observatory / telescope & \\
\end{vocab}

\begin{compare}{Innovation}{Who, where}{Note}
the ballpoint pen (\emph{birome}) & László (Ladislao) Biro, in Argentina, patented 1943 & still called \emph{birome} in Argentina \\
a color television system & Guillermo González Camarena, Mexico, patent 1940 & an early color TV system \\
an electric submarine & Isaac Peral, Spain, launched 1888 & \\
astronomy in the Atacama Desert & international observatories in Chile & dry, clear skies make it one of the best places on Earth for observing \\
\end{compare}
""")
G.q("1 Innovación", r"¿Por qué el desierto de Atacama, en Chile, es un lugar ideal para la astronomía?",
    "porque su cielo es muy seco y despejado", [("porque está muy cerca del mar", "Being by the sea is not the reason."),
                                               ("porque allí no viven científicos", "Many scientists work there."),
                                               ("porque tiene muchas ciudades iluminadas", "Light pollution would hurt observation.")],
    "Dry, clear skies.", "Very dry air and clear skies most nights make the Atacama one of the best observing sites on Earth.",
    ["Seco y despejado → ideal for telescopes."])
G.q("1 Innovación", r"In Argentina, a ballpoint pen is often called a birome. Why?",
    "after László Biro, who developed and patented it in Argentina", [("because it was invented in Spain", "It was patented in Argentina."),
                                                                      ("after a famous brand of paper", "Birome comes from Biro (and his partner Meyne)."),
                                                                      ("because it uses two inks", "Unrelated.")],
    "Birome ← Biro.", "Product names often keep the inventor's name: birome from Biro and Meyne.",
    ["Biro + Meyne → birome."])

G.sec("Personal technology and communication")
G.tex(r"""
\begin{vocab}
el celular (Am.) / el móvil (Esp.) & cell phone & \\
las redes sociales & social media & \\
descargar / subir / compartir & download / upload / share & \\
el mensaje de voz / el audio & voice message & very common in Latin America \\
la brecha digital & the digital divide & gap in access between groups or regions \\
la privacidad / los datos personales & privacy / personal data & \\
el ciberacoso & cyberbullying & \\
las noticias falsas / los bulos (Esp.) & fake news & \\
\end{vocab}

\textbf{The digital divide.} In many countries, rural areas, older people and low-income households have less internet access. During the 2020 school closures, students without a connection or a computer fell behind; some governments broadcast classes on television and radio to reach them.

\textbf{Messaging habits.} Messaging apps are the main way many families and businesses communicate, often with voice messages rather than calls. Family group chats keep relatives in touch across countries, and are also where false news spreads fastest.
""")
G.q("2 Comunicación", r"¿Qué es la brecha digital?",
    "la diferencia en el acceso a la tecnología entre grupos o regiones", [("un error en un programa informático", "That is un error or un fallo."),
                                                                         ("una red social para jóvenes", "No."),
                                                                         ("la velocidad de una conexión", "Not the definition.")],
    "Brecha = gap.", "La brecha digital is the gap in access to technology and internet between groups (rural/urban, old/young, rich/poor).",
    ["brecha (gap) + digital."])
G.q("2 Comunicación", r"During the 2020 school closures, some Latin American governments broadcast classes on television and radio. Which perspective does this practice reflect?",
    "Education should reach every student, including those without internet.", [("Television is better than teachers.", "It was a response to a lack of access."),
                                                                               ("Only urban students need school.", "The opposite: it targeted those left out."),
                                                                               ("Students should stop using technology.", "TV and radio are technology too.")],
    "Practice → value of equal access.", "Using older, universal media to reach disconnected students shows a commitment to access for all.",
    ["Problem: digital divide.", "Practice: TV and radio classes.", "Perspective: education for everyone."])

G.sec("Science in everyday life and its impact on society")
G.tex(r"""
\begin{vocab}
la salud pública / la vacuna & public health / vaccine & \\
el medio ambiente / la contaminación & environment / pollution & \\
la sequía / el agua potable & drought / drinking water & \\
comprobar / verificar los datos & to check / verify the facts & \emph{verificadores de datos} = fact-checkers \\
los efectos secundarios & side effects & \\
la desinformación & misinformation & \\
\end{vocab}

\textbf{Questions about impact} ask who benefits and who is left out, what the risks are, and who should decide (\emph{¿Quién debería regular la IA?}). Good answers weigh both: \emph{Si bien la IA facilita el diagnóstico, también plantea problemas de privacidad.}

\textbf{Fact-checking.} Independent fact-checking organizations operate across the Spanish-speaking world; many let users forward a suspicious message to a number and receive a verdict.
""")
G.q("3 Impacto", r"Elige la mejor palabra: Antes de compartir una noticia, conviene \blank\ si la fuente es confiable.",
    "verificar", [("verificado", "After conviene you need an infinitive."),
                  ("verifique", "With no new subject, conviene takes an infinitive."),
                  ("verificación", "A noun cannot follow conviene without an article.")],
    "conviene + infinitive.", "Conviene, es mejor, hay que + infinitive give general advice.",
    ["conviene verificar."])
G.q("3 Impacto", r"Which sentence weighs a benefit against a risk, as impact questions reward?",
    "Si bien las aplicaciones de salud ayudan a detectar enfermedades, también recogen datos muy personales.",
    [("Las aplicaciones de salud son geniales.", "One-sided and vague."),
     ("Mucha gente usa aplicaciones de salud.", "A fact with no evaluation."),
     ("Las aplicaciones de salud deben prohibirse ya.", "One-sided, with no reasoning.")],
    "Si bien X, también Y.", "Concessive structures let you weigh both sides in one sentence.",
    ["benefit (detect illness) + risk (personal data)."])

G.sec("Structures: predictions, hypotheses and data")
G.tex(r"""
\begin{compare}{Purpose}{Structure}{Example}
Predict & future / ir a + infinitive & En 2030 la mitad de los autos será eléctrica. \\
Expect & se espera que + subjunctive & Se espera que la IA cambie muchos empleos. \\
Hypothesize & si + imperfect subjunctive, conditional & Si todos tuvieran internet, la brecha desaparecería. \\
Passive with ser & ser + participle (+ por) & El bolígrafo fue patentado por Biro en 1943. \\
Data: change & aumentar, crecer, disminuir, bajar, duplicarse & El uso se duplicó entre 2019 y 2024. \\
Data: share & la mayoría, la mitad, un tercio, uno de cada cuatro & Uno de cada cuatro estudiantes\ldots \\
\end{compare}

\begin{trap}
\emph{La mayoría de los estudiantes usa} (singular agreement with \emph{mayoría}) and \emph{usan} (agreement with \emph{estudiantes}) are both accepted. Choose one and be consistent.
\end{trap}
""")
G.q("4 Estructuras", r"Elige la forma correcta: Se espera que los nuevos satélites \blank\ internet a las zonas rurales.",
    "lleven", [("llevan", "Se espera que expresses expectation and takes the subjunctive."),
               ("llevarán", "The future cannot follow se espera que."),
               ("llevar", "With a new subject (los satélites), use que + subjunctive.")],
    "Se espera que + subjunctive.", "Se espera que, ojalá que and es probable que take the subjunctive.",
    ["se espera que → lleven."])
G.q("4 Estructuras", r"Según una gráfica, el uso de pagos con el celular pasó del 20 \% al 40 \% en cinco años. ¿Cuál frase lo describe con precisión?",
    "El uso de pagos con el celular se duplicó en cinco años.", [("El uso de pagos con el celular aumentó un 20 \\% cada año.", "The total rose by 20 points over five years, not 20% a year."),
                                                                ("El uso de pagos con el celular bajó a la mitad.", "It rose."),
                                                                ("La mayoría de las personas paga con el celular.", "40% is not a majority.")],
    "20 → 40 = double.", "Precise chart language: se duplicó (doubled), aumentó 20 puntos, pasó del 20 % al 40 %.",
    ["40 is twice 20 → se duplicó."])
G.q("4 Estructuras", r"Choose the passive sentence.",
    "Las primeras computadoras del país fueron diseñadas por ingenieras.", [("Las ingenieras diseñaron las primeras computadoras del país.", "Active voice: the agent is the subject."),
                                                                           ("Las ingenieras están diseñando computadoras.", "Active progressive."),
                                                                           ("Las ingenieras diseñarían computadoras.", "Active conditional.")],
    "ser + participle (+ por agent).", "The passive with ser puts the thing affected first: fueron diseñadas por…",
    ["fueron diseñadas por → passive."])

G.sec("Task kit: the Argumentative Essay with a chart")
G.tex(r"""
Unit 4 topics are often debates about benefits and risks: \emph{¿Deben las escuelas permitir la IA?}, \emph{¿Es positiva la vida conectada?} The chart source is easy to misread under time pressure.

\begin{terms}
Read the chart first & title, units (\%, millions, hours), years, who was surveyed \\
Pick one comparison & the biggest change, a majority, or a surprising gap \\
Say it precisely & \emph{Según la gráfica de la Fuente 2, el 62 \% de\ldots, frente al 25 \% de\ldots} \\
Explain it & \emph{Esto indica que\ldots / Estos datos demuestran que\ldots} \\
\end{terms}

\begin{trap}
Misreading a chart (switching columns, treating a percentage as a number of people) costs points in source use. Quote the numbers with their labels.
\end{trap}
""")
G.q("5 Ensayo", r"A chart shows 62\% of students use AI tools for homework and 25\% of teachers allow it. Which sentence uses the chart correctly?",
    "Según la Fuente 2, el 62 \\% de los estudiantes usa la IA para las tareas, aunque solo el 25 \\% de los profesores lo permite.", [("Según la Fuente 2, el 62 \\% de los profesores usa la IA.", "Switches the groups."),
                                                                                                                                       ("Según la Fuente 2, 62 estudiantes usan la IA.", "Turns a percentage into a number of people."),
                                                                                                                                       ("La Fuente 2 dice que todos usan la IA.", "Overstates the data.")],
    "Numbers + labels + source.", "Chart evidence must keep the groups and units straight and name the source.",
    ["62% → students; 25% → teachers."])
G.q("5 Ensayo", r"Which phrase best explains what a statistic shows?",
    "Estos datos demuestran que…", [("Había una vez…", "A storytelling opener."),
                                        ("Por cierto, …", "An aside, not an explanation."),
                                        ("Para empezar a contar…", "Not an explanation.")],
    "Estos datos demuestran que…", "Argumentation (Row C) needs the step from evidence to claim.",
    ["Data → claim: estos datos demuestran que."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 4: Science and Technology: Question Set", r"Unit 4 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Audio and Chart and an Audio Report for listening, an Article and a Literary Text for reading) on screen time, astronomy, family technology and misinformation, followed by an Argumentative Essay with three sources and the 10-point scoring guide. As on the exam, questions and choices are in Spanish; listening sources are printed as transcripts. All sources and data are original and fictional, written for practice. Allow about 25 minutes for the multiple choice and 55 minutes for the essay.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Essay: \blank\ / 10 \qquad Target: 15+ MCQ and 7+ essay \qquad Pace: 75 s per item",
        short="Unit 4", sub="Science and Technology")

Q.sec("Listening: Audio and Chart")
Q.src(r"Listening 1 \textperiodcentered\ Audio and Chart (transcript) \textperiodcentered\ «Desconectados», Radio Ciencia", [
    r"(LOCUTORA) ¿Cuánto tiempo pasan los adolescentes frente a una pantalla fuera de la escuela? Un estudio de la Universidad de Montevideo siguió a 900 jóvenes uruguayos de 13 a 17 años durante cuatro años.",
    r"(LOCUTORA) El resultado: el tiempo frente a la pantalla subió de forma constante hasta 2023 y, por primera vez, bajó un poco en 2024. Los investigadores relacionan esa bajada con la nueva norma que obliga a guardar los celulares durante el horario escolar y con campañas en las familias.",
    r"(INVESTIGADOR) No queremos demonizar la tecnología. El problema no es la pantalla en sí, sino lo que deja de hacerse: dormir, moverse, conversar. Los jóvenes que redujeron su tiempo dijeron que dormían mejor.",
], 5, table=(["Año", "Horas diarias (promedio)"], [["2021", "4,1"], ["2022", "4,6"], ["2023", "5,0"], ["2024", "4,7"]]),
      note="Tiempo frente a pantallas fuera de la escuela, adolescentes de 13 a 17 años (datos ficticios).")
Q.q("1.A.2 Data", r"Según la tabla, ¿en qué año pasaron los adolescentes más tiempo frente a las pantallas?",
    "2023", [("2021", "2021 is the lowest, 4.1 hours."),
             ("2022", "4.6 hours, less than 2023."),
             ("2024", "4.7 hours: it fell after 2023.")],
    "Peak: 5.0 h in 2023.", "Data (1.A.2): find the maximum.",
    ["5,0 is the highest value."])
Q.q("1.C.1 Connect", r"¿Cómo explican los investigadores el cambio que muestra la tabla en 2024?",
    "con la norma de guardar los celulares en la escuela y las campañas familiares", [("con el aumento de las tareas escolares", "Not mentioned."),
                                                                                       ("con la llegada de nuevas redes sociales", "That would explain a rise."),
                                                                                       ("con el cierre de las escuelas", "Not mentioned.")],
    "Table: 5.0 → 4.7; audio: norma + campañas.", "Connect (1.C.1): match the dip in the table with the cause given in the audio.",
    ["bajó un poco en 2024 → la nueva norma… y campañas."])
Q.q("1.B.3 Point of view", r"¿Qué opina el investigador sobre la tecnología?",
    "El problema es lo que se deja de hacer por usarla, no la pantalla misma.", [("La tecnología es peligrosa y hay que prohibirla.", "No queremos demonizar la tecnología."),
                                                                                ("Los jóvenes deberían usar más las pantallas.", "Not his view."),
                                                                                ("Las pantallas mejoran el sueño.", "Those who reduced screen time slept better.")],
    "No es la pantalla en sí, sino lo que deja de hacerse.", "Point of view (1.B.3): no… sino… states his position.",
    ["El problema no es la pantalla en sí, sino…"])
Q.q("1.A.1 Detail", r"¿Qué dijeron los jóvenes que redujeron su tiempo frente a la pantalla?",
    "que dormían mejor", [("que sacaban mejores notas", "Not mentioned."),
                          ("que se aburrían más", "Not mentioned."),
                          ("que hablaban menos con su familia", "Not mentioned.")],
    "dormían mejor.", "Detail (1.A.1): the last sentence.",
    ["dijeron que dormían mejor."])
Q.q("1.B.5 Word meaning", r"En la grabación, «demonizar» significa",
    "presentar algo como totalmente malo", [("usar algo con frecuencia", "No."),
                                           ("estudiar algo científicamente", "No."),
                                           ("vender algo caro", "No.")],
    "demonizar = present as evil.", "Word meaning (1.B.5): no queremos demonizar is followed by a more balanced view.",
    ["The next sentence balances the view → demonizar = make it the villain."])

Q.sec("Reading: Article")
Q.src(r"Reading 1 \textperiodcentered\ Article \textperiodcentered\ «Los ojos del mundo miran desde Chile»", [
    r"En lo alto del desierto de Atacama, a más de 2.500 metros de altura, el aire es tan seco y el cielo tan limpio que los astrónomos lo llaman «la ventana al universo». Allí funcionan algunos de los telescopios más potentes del planeta, construidos por consorcios internacionales.",
    r"Para la ingeniera chilena Daniela Soto, que trabaja en uno de los observatorios, la presencia de estos proyectos ha cambiado su región. «Cuando era niña, nadie de mi pueblo pensaba en ser científico. Hoy hay becas, talleres en las escuelas y un festival de astronomía cada invierno».",
    r"No todo es positivo. Las comunidades indígenas de la zona reclaman que se respeten sus lugares sagrados, y algunos vecinos critican que los empleos mejor pagados sean para extranjeros. Las autoridades respondieron con un programa de formación técnica para jóvenes de la región.",
    r"Además, la luz de las ciudades amenaza la calidad del cielo. Por eso Chile aprobó normas que limitan el alumbrado público hacia arriba: proteger la oscuridad es, aquí, una cuestión económica.",
], 5)
Q.q("1.B.1 Main idea", r"¿Cuál es la idea principal del artículo?",
    "Los observatorios de Atacama aportan beneficios a la región, pero también generan desafíos.", [("Chile quiere cerrar los observatorios.", "Nothing suggests closing them."),
                                                                                                     ("La astronomía no interesa a los chilenos.", "A festival and scholarships show interest."),
                                                                                                     ("Los telescopios fueron construidos solo por Chile.", "They were built by international consortia.")],
    "Benefits + No todo es positivo.", "Main idea (1.B.1): positive effects, then problems and responses.",
    ["Paragraph 2 benefits; paragraphs 3–4 challenges."])
Q.q("1.A.1 Detail", r"Según Daniela Soto, ¿qué ha cambiado en su región?",
    "Ahora hay becas, talleres y un festival de astronomía.", [("Ya no hay escuelas.", "Workshops are held in schools."),
                                                              ("Todos los vecinos trabajan en los observatorios.", "Not stated."),
                                                              ("Su pueblo se ha quedado sin agua.", "Not mentioned.")],
    "Hoy hay becas, talleres… y un festival.", "Detail (1.A.1).",
    ["Hoy hay becas, talleres en las escuelas y un festival…"])
Q.q("1.B.3 Point of view", r"¿Qué reclaman las comunidades indígenas?",
    "que se respeten sus lugares sagrados", [("que se construyan más telescopios", "Not their demand."),
                                            ("que se aumente el alumbrado público", "Not their demand."),
                                            ("que los científicos se vayan del país", "Not stated.")],
    "respeto a lugares sagrados.", "Point of view (1.B.3): attribute each concern to the right group.",
    ["reclaman que se respeten sus lugares sagrados."])
Q.q("1.C.3 Inference", r"¿Por qué el artículo dice que «proteger la oscuridad es una cuestión económica»?",
    "porque los observatorios, que dependen de cielos oscuros, son importantes para la región", [("porque la electricidad es muy cara en el desierto", "The point is about sky quality, not energy prices."),
                                                                                                  ("porque las empresas venden la oscuridad", "Figurative misreading."),
                                                                                                  ("porque los turistas prefieren las ciudades", "Not stated.")],
    "Dark skies = observatories = jobs and investment.", "Inference (1.C.3): light threatens the sky, the sky supports the observatories, the observatories support the economy.",
    ["luz → amenaza el cielo → observatorios → economía."])
Q.q("1.B.4 Organization", r"¿Qué función tiene la expresión «No todo es positivo» al comienzo del tercer párrafo?",
    "introducir los problemas después de presentar los beneficios", [("resumir la conclusión del artículo", "The article continues after it."),
                                                                    ("dar un ejemplo de los beneficios", "It introduces drawbacks."),
                                                                    ("cambiar de tema a otro país", "Still Chile.")],
    "Transition to the counterpoint.", "Organization (1.B.4): a contrast transition.",
    ["benefits → No todo es positivo → problems."])

Q.sec("Reading: Literary Text")
Q.src(r"Reading 2 \textperiodcentered\ Literary Text \textperiodcentered\ «La pantalla de la abuela» (fragmento de un relato)", [
    r"La primera vez que mi abuela Rosario hizo una videollamada, sostuvo el teléfono a la altura de la oreja, como siempre. «¿Me oyes, Pablito? ¡No te veo!», gritaba, mientras yo, desde Madrid, solo veía el techo de su cocina en Lima.",
    r"Tardó una semana en aprender a mirarme. Después aprendió a enviar audios de cinco minutos, a reenviar cadenas de oración y, para mi desgracia, a descubrir mis fotos de las fiestas.",
    r"Un domingo me llamó a las siete de la mañana, hora de Madrid. «Es que quería que vieras las rosas», dijo, girando el teléfono hacia el jardín. No le dije que estaba dormido. Mirando aquellas rosas, tan lejos y tan cerca, pensé que la tecnología no había acortado la distancia: solo nos había dado una ventana para asomarnos.",
], 5)
Q.q("1.A.1 Detail", r"¿Cuál fue el problema de la abuela en su primera videollamada?",
    "sostenía el teléfono junto a la oreja, como en una llamada normal", [("no tenía internet en Lima", "The call connected."),
                                                                         ("no quería hablar con su nieto", "She was eager to talk."),
                                                                         ("hablaba en otro idioma", "No.")],
    "a la altura de la oreja.", "Detail (1.A.1).",
    ["sostuvo el teléfono a la altura de la oreja… ¡No te veo!"])
Q.q("1.B.3 Tone", r"¿Qué tono predomina en el segundo párrafo?",
    "humorístico", [("trágico", "Nothing tragic happens."),
                    ("indignado", "The narrator jokes rather than complains seriously."),
                    ("científico", "The text is personal.")],
    "para mi desgracia… cadenas de oración.", "Tone (1.B.3): exaggeration (audios de cinco minutos) and mock complaint create humor.",
    ["para mi desgracia → playful complaint."])
Q.q("1.C.3 Inference", r"¿Por qué el narrador no le dijo a su abuela que estaba dormido?",
    "porque no quería quitarle la ilusión de mostrarle sus rosas", [("porque estaba enojado con ella", "His reflection is tender."),
                                                                   ("porque no sabía usar el teléfono", "He is the expert."),
                                                                   ("porque la llamada se cortó", "No.")],
    "Tenderness.", "Inference (1.C.3): he lets her share the moment, which shows affection.",
    ["Es que quería que vieras las rosas → he does not spoil it."])
Q.q("1.B.5 Word meaning", r"En el texto, «asomarnos» significa",
    "mirar a través de algo hacia otro lugar", [("despedirnos", "No."),
                                               ("viajar juntos", "The point is that they cannot."),
                                               ("discutir", "No.")],
    "asomarse = to look out (through a window).", "Word meaning (1.B.5): una ventana para asomarnos.",
    ["ventana + asomarse → look through."])
Q.q("1.C.2 Conclusion", r"¿Qué conclusión saca el narrador sobre la tecnología?",
    "Permite ver a la familia lejana, aunque no elimina la distancia.", [("Ha eliminado completamente la distancia entre él y su abuela.", "He says it has not shortened the distance."),
                                                                         ("Es inútil para las personas mayores.", "His grandmother learned to use it well."),
                                                                         ("Debería prohibirse los domingos.", "No.")],
    "no había acortado la distancia: solo nos había dado una ventana.", "Conclusions (1.C.2): the final sentence states the narrator's reflection.",
    ["no… acortado la distancia + una ventana para asomarnos."])

Q.sec("Listening: Audio Report")
Q.src(r"Listening 2 \textperiodcentered\ Audio Report (transcript) \textperiodcentered\ «El virus de las noticias falsas»", [
    r"(PERIODISTA) En Colombia, el 70 por ciento de las personas recibe noticias a través de grupos de mensajería, según una encuesta reciente. El problema es que muchas de esas noticias son falsas.",
    r"(PERIODISTA) Para combatirlas, un grupo de periodistas creó «Verifica Ya», un servicio gratuito: los usuarios reenvían un mensaje sospechoso a un número y, en menos de un día, reciben una respuesta con la información comprobada.",
    r"(DIRECTORA) Lo que más se comparte no son mentiras políticas, sino consejos falsos de salud: remedios caseros que supuestamente curan enfermedades graves. Mucha gente los reenvía con buena intención, para proteger a su familia.",
    r"(PERIODISTA) Los expertos recomiendan una regla sencilla: si un mensaje provoca miedo o rabia inmediata, hay que detenerse y verificar antes de compartir.",
], 5)
Q.q("1.A.1 Detail", r"¿Cómo funciona el servicio «Verifica Ya»?",
    "Los usuarios reenvían un mensaje dudoso y reciben una verificación.", [("Los periodistas borran los mensajes falsos de los teléfonos.", "They verify; they do not delete."),
                                                                            ("Cobra una suscripción mensual.", "It is free."),
                                                                            ("Envía noticias políticas cada día.", "Not described.")],
    "reenvían… reciben una respuesta.", "Detail (1.A.1) on the procedure.",
    ["reenvían un mensaje sospechoso… reciben una respuesta."])
Q.q("1.A.1 Detail", r"Según la directora, ¿qué tipo de noticias falsas se comparte más?",
    "consejos falsos sobre salud", [("mentiras políticas", "She says not political lies."),
                                    ("noticias de deportes", "Not mentioned."),
                                    ("anuncios de empleo", "Not mentioned.")],
    "no son mentiras políticas, sino consejos falsos de salud.", "No… sino… marks the correction.",
    ["sino consejos falsos de salud."])
Q.q("1.C.3 Inference", r"¿Por qué, según la directora, muchas personas reenvían estos mensajes?",
    "porque quieren proteger a sus seres queridos", [("porque quieren engañar a su familia", "She says buena intención."),
                                                    ("porque les pagan por hacerlo", "Not stated."),
                                                    ("porque no saben leer", "Not stated.")],
    "con buena intención, para proteger a su familia.", "Inference/detail: motive stated in her last sentence.",
    ["buena intención → proteger."])
Q.q("1.B.1 Purpose", r"¿Cuál es el propósito principal del reportaje?",
    "informar sobre un problema y una herramienta para combatirlo", [("vender una aplicación de mensajería", "The service is free and not an app sale."),
                                                                    ("criticar a los periodistas", "Journalists created the solution."),
                                                                    ("explicar cómo funcionan las vacunas", "Not the topic.")],
    "Problem + solution.", "Purpose (1.B.1): the report presents the problem, a response and advice.",
    ["fake news → Verifica Ya → advice."])
Q.q("1.C.2 Conclusion", r"Recibes un mensaje que dice «¡Urgente! Este té cura el cáncer. ¡Compártelo!». Según los expertos, ¿qué deberías hacer?",
    "detenerte y verificarlo antes de compartirlo", [("compartirlo enseguida para ayudar", "That is how false news spreads."),
                                                    ("borrar todas tus aplicaciones", "Not the advice."),
                                                    ("enviarlo solo a tu familia", "Still spreading it.")],
    "Miedo o urgencia → stop and verify.", "Conclusions (1.C.2): apply the experts' rule to a new case.",
    ["provoca miedo… hay que detenerse y verificar."])

Q.frq(kind="Argumentative Essay", head=r"Question 3 \textperiodcentered\ Argumentative Essay \textperiodcentered\ 10 points \textperiodcentered\ 55 minutes", mins=55,
      directions=[r"Vas a escribir un ensayo argumentativo para un curso universitario. Lee el tema y las fuentes escritas; después escucha la fuente auditiva (aquí, la transcripción). Escribe un ensayo que integre material de las tres fuentes para apoyar tu posición. Indica las fuentes que usas por número, título o autor."],
      sources=[dict(title=r"Fuente 1 \textperiodcentered\ Artículo \textperiodcentered\ «El tutor que nunca duerme»", paras=[
          r"En el Liceo Bicentenario de Temuco, los estudiantes de matemáticas tienen un asistente de inteligencia artificial que les explica los ejercicios paso a paso, a cualquier hora. «Antes, si no entendía algo en casa, me quedaba atascada. Ahora pregunto hasta entenderlo», cuenta Valentina, de 15 años.",
          r"El profesor Hernán Lagos ha notado que los alumnos llegan a clase con mejores preguntas. Pero también advierte: «El asistente está programado para guiar, no para dar la respuesta. Si fuera una herramienta que lo resuelve todo, sería un desastre»."]),
               dict(title=r"Fuente 2 \textperiodcentered\ Gráfica \textperiodcentered\ Estudiantes que usan IA para las tareas: ¿para qué?", paras=[
          r"Encuesta a 2.500 estudiantes de secundaria de España y México (datos ficticios). Porcentaje que usa la IA para cada fin al menos una vez por semana."],
                    table=(["Uso", "Porcentaje"], [["Entender un tema que no comprendió", "58 \\%"], ["Revisar la ortografía de un texto", "49 \\%"], ["Copiar una respuesta completa", "37 \\%"], ["Practicar para un examen", "33 \\%"]])),
               dict(title=r"Fuente 3 \textperiodcentered\ Audio (transcripción) \textperiodcentered\ «Aula Abierta», programa de radio", paras=[
          r"(LOCUTOR) Hablamos con la pedagoga Carmen Ruiz. ¿Es la inteligencia artificial una amenaza para el aprendizaje?",
          r"(CARMEN) Depende de cómo se use. Aprender requiere esfuerzo: equivocarse, volver a intentarlo. Si un estudiante le pide a la máquina que escriba su ensayo, se salta justo esa parte. Pero si la usa para entender, para practicar o para recibir comentarios, puede ser como tener un profesor particular, algo que antes solo podían pagar las familias ricas.",
          r"(LOCUTOR) ¿Qué deberían hacer las escuelas?",
          r"(CARMEN) Enseñar a usarla. Prohibirla es inútil: los jóvenes la usarán igual, pero sin criterio."])],
      prompt=[r"Tema del ensayo: \textbf{¿Es positivo que los estudiantes usen la inteligencia artificial para hacer sus tareas?}"],
      model=[r"La inteligencia artificial ha llegado a las mochilas de los estudiantes, y muchos se preguntan si les ayuda a aprender o si hace el trabajo por ellos. En mi opinión, usar la IA para las tareas es positivo, siempre que sirva para comprender y no para copiar.",
             r"En primer lugar, la IA puede ofrecer a todos los estudiantes una ayuda que antes era un privilegio. Como explica la pedagoga Carmen Ruiz en la Fuente 3, usarla para entender o practicar «puede ser como tener un profesor particular», algo que antes solo podían pagar las familias ricas. El caso de Valentina en la Fuente 1 lo confirma: gracias al asistente de su liceo, ya no se queda atascada en casa. Por lo tanto, la IA puede reducir la desigualdad entre estudiantes.",
             r"En segundo lugar, la mayoría de los jóvenes ya la usa con fines útiles. Según la gráfica de la Fuente 2, el 58 \% de los estudiantes la utiliza para entender un tema que no comprendió y el 33 \% para practicar para un examen. Estos datos demuestran que la IA no es solo una herramienta para hacer trampa.",
             r"Es cierto que existe un riesgo: la misma gráfica muestra que el 37 \% copia respuestas completas, y Ruiz advierte que así el estudiante se salta el esfuerzo que exige aprender. Sin embargo, la solución no es prohibirla, ya que, como ella afirma, los jóvenes la usarían igual, pero sin criterio. El liceo de Temuco ofrece un modelo mejor: un asistente programado para guiar, no para dar la respuesta (Fuente 1).",
             r"En conclusión, si las escuelas enseñaran a usar la inteligencia artificial con criterio, los estudiantes tendrían a su alcance un tutor incansable. El problema no es la herramienta, sino el uso que hagamos de ella."],
      rows=[("A Position", 1, "a clear, qualified position (positive, if used to understand)", "only lists advantages and disadvantages"),
            ("B Source use", 2, "all three sources used accurately and named", "two sources, or misreading the chart's percentages"),
            ("C Argumentation", 2, "each claim explained with evidence (por lo tanto, estos datos demuestran)", "quotes and numbers with no link to the claims"),
            ("D Organization", 2, "introduction, two claims, concession and rebuttal, conclusion", "one paragraph per source"),
            ("E Language control", 3, "varied structures: siempre que + subjunctive, si-clause, relative clauses", "basic structures; copying the sources")],
      tips=["The position is conditional but clear (siempre que sirva para comprender).", "The concession uses the chart's own 37% against itself, then answers it with Sources 1 and 3.",
            "Every source is named and paraphrased, with a short quotation at most.", "The conclusion's si-clause and final antithesis (no es la herramienta, sino el uso) round off the argument."],
      ask="Write your essay in Spanish (about 300–350 words), then mark it against each row.", lines=22)

GUIDE, QSET = G, Q
