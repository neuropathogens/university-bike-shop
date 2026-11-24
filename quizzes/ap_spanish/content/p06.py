from ap_wl.model import Doc

STEM = "06-global-contexts"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 6: Global Contexts", r"Unit 6 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 6 asks how global issues affect families and communities, and how people and governments respond. Its recommended contexts are global communication, the natural world, history, policy and planning, and transportation. This guide gives the vocabulary of the environment, history and public policy, the cases most often tested (Andean glaciers and water, renewable energy in Costa Rica, lithium, the wave of independence, Bogotá's ciclovía and TransMilenio, cable cars in Medellín and La Paz, pedestrian city centers), the language for proposing solutions, and an Argumentative Essay kit on counterarguments. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Solutions I can propose: \blank[10em]",
        short="Unit 6", sub="Global Contexts")

G.sec("The natural world")
G.tex(r"""
\begin{vocab}
el medio ambiente / la naturaleza & environment / nature & \\
el cambio climático / el calentamiento global & climate change / global warming & \\
la sequía / la escasez de agua & drought / water shortage & Montevideo, 2023 \\
el glaciar / el deshielo & glacier / melting & Andean glaciers supply water to cities like La Paz \\
la deforestación / la selva amazónica & deforestation / the Amazon rainforest & \\
las energías renovables & renewable energy & hydro, wind, solar, geothermal \\
el litio / el salar & lithium / salt flat & Bolivia, Chile, Argentina: the ``lithium triangle'' \\
\end{vocab}

\textbf{Cases.} Costa Rica produces almost all of its electricity from renewable sources (mostly hydroelectric). Tropical Andean glaciers have shrunk sharply, threatening water for cities and farms. Lithium for electric-car batteries lies under the salt flats of Bolivia, Chile and Argentina, raising questions about water use and Indigenous communities' rights.
""")
G.q("1 Naturaleza", r"¿Por qué el deshielo de los glaciares andinos preocupa a ciudades como La Paz?",
    "porque los glaciares son una fuente de agua para la ciudad", [("porque produce terremotos", "Melting does not cause earthquakes."),
                                                                  ("porque atrae demasiados turistas", "Not the concern."),
                                                                  ("porque aumenta la temperatura del mar", "La Paz is inland; the concern is water supply.")],
    "Glaciers = water reserve.", "Cause and effect: glaciers store water released in the dry season; when they shrink, so does the supply.",
    ["deshielo → less stored water → shortages."])
G.q("1 Naturaleza", r"The ``lithium triangle'' refers to salt flats in",
    "Bolivia, Chile and Argentina", [("Mexico, Guatemala and Honduras", "Not lithium regions."),
                                     ("Spain, Portugal and France", "No."),
                                     ("Peru, Ecuador and Colombia", "Not the triangle.")],
    "Lithium triangle = Bolivia, Chile, Argentina.", "These salt flats hold much of the world's known lithium, used in batteries.",
    ["Salar de Uyuni (Bolivia), Atacama (Chile), Argentina's puna."])

G.sec("History and global communication")
G.tex(r"""
\begin{vocab}
la conquista / la colonización & conquest / colonization & \\
la independencia & independence & most of Spanish America, 1810--1825 \\
el virreinato & viceroyalty & colonial administrative unit \\
la dictadura / la democracia & dictatorship / democracy & \\
la memoria histórica & historical memory & how societies remember past violence \\
el exilio / la diáspora & exile / diaspora & \\
la traducción / el intérprete & translation / interpreter & \\
\end{vocab}

\textbf{Independence.} Between 1810 and 1825 most of Spanish America became independent; leaders such as Simón Bolívar and José de San Martín led campaigns across several future countries. Cuba and Puerto Rico remained Spanish until 1898.

\textbf{Memory.} Several countries have museums or days of remembrance for victims of dictatorships (Chile's Museo de la Memoria y los Derechos Humanos, Argentina's former ESMA). The perspective: remembering is a duty, so that the past is not repeated (\emph{nunca más}).
""")
G.q("2 Historia", r"¿En qué período se independizó la mayor parte de Hispanoamérica?",
    "entre 1810 y 1825", [("en el siglo XVI", "That is the period of conquest."),
                          ("después de 1950", "Too late."),
                          ("en 1492", "1492 is Columbus's first voyage.")],
    "1810–1825.", "Most independence wars ran from 1810 to the mid-1820s; Cuba and Puerto Rico remained Spanish until 1898.",
    ["Bolívar, San Martín → 1810–1825."])
G.q("2 Historia", r"Which perspective does the phrase «nunca más», used by memory museums, express?",
    "Remembering past violence helps prevent it from happening again.", [("The past should be forgotten.", "The opposite."),
                                                                        ("History is only for experts.", "Museums are for the public."),
                                                                        ("Dictatorships were beneficial.", "No.")],
    "Nunca más = never again.", "Memory sites (product) and commemorations (practice) reflect the perspective that remembering protects democracy.",
    ["nunca más → prevention through memory."])

G.sec("Policy, planning and transportation")
G.tex(r"""
\begin{vocab}
el transporte público & public transportation & \\
el carril exclusivo / el BRT & dedicated lane / bus rapid transit & TransMilenio, Bogotá (2000) \\
el teleférico / el metrocable & cable car & Medellín (2004), La Paz (2014) \\
la ciclovía & bike lane; street closed to cars for bikes & Bogotá's Sunday ciclovía since the 1970s \\
peatonal / la peatonalización & pedestrian / pedestrianization & Pontevedra, Spain, since 1999 \\
el atasco / el embotellamiento & traffic jam & \\
la planificación urbana & urban planning & \\
\end{vocab}

\textbf{Cases.} Medellín's Metrocable connected hillside neighborhoods to the metro, cutting commutes that once took hours. Every Sunday, Bogotá closes main roads to cars so that residents can walk, run and cycle. Pontevedra removed most cars from its center starting in 1999. The perspective common to these projects: streets are public space for everyone, not only for cars.
""")
G.q("3 Transporte", r"¿Qué problema resolvió el Metrocable de Medellín?",
    "conectar barrios de las laderas con el metro", [("unir Medellín con Bogotá", "It is an urban system."),
                                                    ("transportar mercancías al puerto", "It carries passengers."),
                                                    ("reemplazar todos los autobuses", "It complements the metro.")],
    "Hillside neighborhoods → metro.", "Cable cars reach steep hillside neighborhoods where roads are slow and narrow.",
    ["laderas + metro → Metrocable."])
G.q("3 Transporte", r"Every Sunday, Bogotá closes major roads to cars for walkers and cyclists. Which perspective does this practice reflect?",
    "Streets are public space that belongs to everyone, not only to cars.", [("Cars should be banned forever.", "It is a weekly closure, not a ban."),
                                                                            ("Exercise should happen only in gyms.", "The opposite."),
                                                                            ("Only athletes may use the roads.", "Everyone may.")],
    "Ciclovía ↔ public space for all.", "Practice (Sunday ciclovía) → perspective (shared public space, health, community).",
    ["Weekly practice + who uses it → perspective."])

G.sec("Structures: proposing solutions")
G.tex(r"""
\begin{compare}{Purpose}{Structure}{Example}
Necessity & hay que / es necesario + infinitive & Hay que ahorrar agua. \\
Urgency & es urgente que + subjunctive & Es urgente que los gobiernos actúen. \\
Recommendation & habría que, deberíamos + infinitive & Habría que invertir en trenes. \\
Condition & a menos que, con tal de que + subjunctive & No habrá cambios a menos que todos participen. \\
Purpose & para que + subjunctive & Plantan árboles para que la ciudad sea más fresca. \\
Consequence & de modo que, por consiguiente & Llovió poco; por consiguiente, faltó agua. \\
\end{compare}

\begin{trap}
\emph{A menos que}, \emph{con tal de que}, \emph{para que} and \emph{antes de que} always take the subjunctive.
\end{trap}
""")
G.q("4 Soluciones", r"Elige la forma correcta: El plan no funcionará a menos que los vecinos \blank.",
    "participen", [("participan", "A menos que always takes the subjunctive."),
                   ("participarán", "The future cannot follow a menos que."),
                   ("participar", "With a subject (los vecinos), a conjugated verb is needed.")],
    "a menos que + subjunctive.", "Conjunctions of condition and purpose (a menos que, con tal de que, para que) always take the subjunctive.",
    ["a menos que → participen."])
G.q("4 Soluciones", r"Which sentence proposes a solution politely and clearly?",
    "Habría que ampliar las ciclovías para que más personas dejen el auto.", [("Las ciclovías.", "A fragment, not a proposal."),
                                                                               ("Me da igual el tráfico.", "Indifference, not a solution."),
                                                                               ("El tráfico es un problema muy grave y muy malo.", "States the problem, proposes nothing.")],
    "Habría que + infinitive + para que.", "A conditional recommendation plus a purpose clause makes a clear, polite proposal.",
    ["habría que (recommendation) + para que (purpose)."])

G.sec("Task kit: answering the other side")
G.tex(r"""
Global-context essays (\emph{¿Deben limitarse los autos en el centro?}, \emph{¿Debe priorizarse el medio ambiente sobre el empleo?}) almost always come with one source that disagrees with you. Use it: a counterargument answered well shows argumentation and earns credit for that source.

\begin{terms}
Concede & \emph{Es cierto que\ldots / Hay que reconocer que\ldots} + the opposing point with its source \\
Answer & \emph{Sin embargo, \ldots / No obstante, \ldots} + evidence from another source or a solution \\
Limit & \emph{siempre que, con tal de que} + subjunctive: under what conditions your position holds \\
\end{terms}

\begin{keyidea}[Qualified positions]
\emph{Las ciudades deben limitar los autos en el centro, siempre que ofrezcan transporte público eficiente} is a clear position (Row A) that already includes the reply to the strongest objection.
\end{keyidea}
""")
G.q("5 Ensayo", r"A source says closing the city center to cars hurt some shops at first. How should an essay in favor of closing it use this source?",
    "concede the point and answer it with evidence or a solution", [("ignore it so the essay stays one-sided", "Ignoring a source loses source-use points."),
                                                                     ("change position to agree with it", "One objection does not require abandoning a position."),
                                                                     ("quote it with no comment", "Evidence without explanation does not earn argumentation credit.")],
    "Concede + answer.", "Answering the opposing source strengthens argumentation and still counts toward using all three sources.",
    ["Es cierto que… Sin embargo…"])
G.q("5 Ensayo", r"Elige la forma correcta: Apoyo la medida, siempre que el gobierno \blank\ más autobuses.",
    "ofrezca", [("ofrece", "Siempre que meaning provided that takes the subjunctive."),
                ("ofrecerá", "The future cannot follow siempre que in this sense."),
                ("ofrecer", "A conjugated verb is needed.")],
    "siempre que (condition) + subjunctive.", "Siempre que = provided that, as a condition → subjunctive. (Siempre que = whenever, for a habit, takes the indicative.)",
    ["condition → ofrezca."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 6: Global Contexts: Question Set", r"Unit 6 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Interview and an Instructional Guidance for listening, an Article and an Article and Chart for reading) on glaciers, urban mobility, renewable energy and saving water, followed by an Argumentative Essay with three sources and the 10-point scoring guide. As on the exam, questions and choices are in Spanish; listening sources are printed as transcripts. All sources and data are original and fictional, written for practice. Allow about 25 minutes for the multiple choice and 55 minutes for the essay.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Essay: \blank\ / 10 \qquad Target: 15+ MCQ and 7+ essay \qquad Pace: 75 s per item",
        short="Unit 6", sub="Global Contexts")

Q.sec("Listening: Interview")
Q.src(r"Listening 1 \textperiodcentered\ Interview (transcript) \textperiodcentered\ Una glacióloga boliviana", [
    r"(PERIODISTA) Doctora Mamani, usted estudia los glaciares de la cordillera Real desde hace veinte años. ¿Qué ha observado?",
    r"(DRA. MAMANI) Que se están yendo. Algunos glaciares pequeños que medía cuando era estudiante ya no existen. Los más grandes han perdido una parte importante de su superficie.",
    r"(PERIODISTA) ¿Por qué debería importarle eso a una familia de El Alto?",
    r"(DRA. MAMANI) Porque una parte del agua que sale de sus grifos viene del deshielo, sobre todo en la época seca. Cuando no llueve, el glaciar es como una cuenta de ahorros. Si la gastamos toda, el día que la necesitemos estará vacía.",
    r"(PERIODISTA) ¿Hay algo que se pueda hacer?",
    r"(DRA. MAMANI) No podemos detener el deshielo solos; depende del clima de todo el planeta. Pero sí podemos prepararnos: construir pequeñas represas, reparar las tuberías que pierden agua y enseñar a ahorrarla. La adaptación también es una forma de responsabilidad.",
], 5)
Q.q("1.A.1 Detail", r"¿Qué ha observado la doctora Mamani en veinte años?",
    "que algunos glaciares han desaparecido y otros se han reducido", [("que los glaciares han crecido", "The opposite."),
                                                                      ("que no hay cambios importantes", "She describes major losses."),
                                                                      ("que llueve más en la época seca", "Not stated.")],
    "Se están yendo.", "Detail (1.A.1).",
    ["ya no existen… han perdido una parte importante…"])
Q.q("1.C.3 Inference", r"¿Qué quiere decir la comparación del glaciar con «una cuenta de ahorros»?",
    "que el glaciar guarda agua para cuando no llueve", [("que el agua de los glaciares se vende", "Figurative misreading."),
                                                        ("que los bancos financian los glaciares", "No."),
                                                        ("que el glaciar produce dinero para la ciudad", "No.")],
    "Savings account = stored reserve.", "Figurative language (1.C.3): savings are kept for when income stops; the glacier stores water for the dry season.",
    ["Cuando no llueve, el glaciar es como una cuenta de ahorros."])
Q.q("1.B.3 Point of view", r"Según la glacióloga, ¿qué se puede hacer?",
    "adaptarse con medidas como pequeñas represas y la reparación de tuberías", [("detener el deshielo con tecnología local", "She says it cannot be stopped locally."),
                                                                                  ("trasladar la ciudad a otro lugar", "Not proposed."),
                                                                                  ("no hacer nada, porque es inevitable", "She proposes preparation.")],
    "Adaptación.", "Point of view (1.B.3): no podemos… pero sí podemos…",
    ["construir pequeñas represas, reparar las tuberías…"])
Q.q("1.B.4 Organization", r"¿Cómo está organizada la última respuesta de la doctora?",
    "reconoce un límite y luego propone acciones posibles", [("cuenta una historia de su infancia", "No."),
                                                            ("compara dos ciudades", "No."),
                                                            ("enumera causas del cambio climático", "She does not list causes.")],
    "No podemos… Pero sí podemos…", "Organization (1.B.4): limitation, then solutions.",
    ["Concession + proposal."])
Q.q("1.B.5 Word meaning", r"En la entrevista, la palabra «grifos» se refiere a",
    "las llaves por donde sale el agua en las casas", [("los ríos de montaña", "The water comes out of them at home."),
                                                      ("los glaciares pequeños", "No."),
                                                      ("los tanques de la ciudad", "Tanks store water; grifos are where it comes out in each home.")],
    "grifo = faucet/tap.", "Word meaning (1.B.5): el agua que sale de sus grifos.",
    ["sale de sus grifos → faucets."])

Q.sec("Reading: Article")
Q.src(r"Reading 1 \textperiodcentered\ Article \textperiodcentered\ «Ciudades que se mueven distinto»", [
    r"Durante décadas, las ciudades latinoamericanas crecieron pensando en el automóvil. Hoy algunas buscan otro camino. En Bogotá, cada domingo y festivo, más de cien kilómetros de avenidas se cierran a los autos para que la gente camine, corra o pedalee. La ciclovía, que empezó en los años setenta, se ha copiado en ciudades de todo el mundo.",
    r"En Medellín, el Metrocable llevó el transporte público a barrios construidos en las laderas de las montañas, donde las calles son estrechas y empinadas. Para muchas familias, un viaje al centro que antes duraba más de una hora ahora dura minutos. Y en La Paz, Mi Teleférico se convirtió en el sistema de cable urbano más grande del mundo.",
    r"Los urbanistas coinciden en que la tecnología no basta. «Un teleférico no cambia un barrio si no llegan también escuelas, bibliotecas y espacios públicos», advierte la arquitecta Sofía Linares. «La movilidad es una puerta; lo importante es lo que hay al otro lado».",
], 5)
Q.q("1.B.1 Main idea", r"¿Cuál es la idea principal del artículo?",
    "Algunas ciudades latinoamericanas buscan alternativas al automóvil, aunque el transporte por sí solo no basta.", [("Las ciudades deben prohibir todos los autos.", "Not proposed."),
                                                                                                                    ("La ciclovía de Bogotá es un fracaso.", "It has been copied worldwide."),
                                                                                                                    ("Los teleféricos son solo atracciones turísticas.", "They serve residents.")],
    "Alternatives + limits.", "Main idea (1.B.1): examples of alternatives, then the urbanists' caveat.",
    ["Paragraphs 1–2 examples; paragraph 3 la tecnología no basta."])
Q.q("1.A.1 Detail", r"¿Cuándo funciona la ciclovía de Bogotá?",
    "los domingos y días festivos", [("todos los días por la tarde", "No."),
                                     ("solo en vacaciones de verano", "No."),
                                     ("una vez al año", "Every Sunday and holiday.")],
    "cada domingo y festivo.", "Detail (1.A.1).",
    ["cada domingo y festivo…"])
Q.q("1.A.1 Detail", r"Según el artículo, ¿qué cambió el Metrocable para muchas familias?",
    "Redujo mucho el tiempo de viaje al centro.", [("Aumentó el precio de las viviendas en el centro.", "Not stated."),
                                                  ("Eliminó las calles de los barrios.", "No."),
                                                  ("Obligó a las familias a mudarse.", "No.")],
    "de más de una hora a minutos.", "Detail (1.A.1).",
    ["antes duraba más de una hora ahora dura minutos."])
Q.q("1.B.3 Point of view", r"¿Qué opina la arquitecta Sofía Linares?",
    "que el transporte debe acompañarse de servicios y espacios públicos", [("que los teleféricos son innecesarios", "She does not reject them."),
                                                                            ("que la tecnología lo resuelve todo", "She says it is not enough."),
                                                                            ("que las bibliotecas son más importantes que las escuelas", "No ranking is made.")],
    "La movilidad es una puerta.", "Point of view (1.B.3).",
    ["si no llegan también escuelas, bibliotecas y espacios públicos."])
Q.q("1.C.3 Inference", r"¿Qué quiere decir «la movilidad es una puerta; lo importante es lo que hay al otro lado»?",
    "que el transporte da acceso a oportunidades, y esas oportunidades son lo esencial", [("que hay que construir más puertas en las estaciones", "Literal misreading."),
                                                                                          ("que la movilidad no sirve para nada", "She calls it a door, which is useful."),
                                                                                          ("que los barrios deben cerrarse", "No.")],
    "Door = access.", "Figurative meaning (1.C.3): mobility gives access; what matters is what people reach.",
    ["puerta (access) → opportunities on the other side."])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 2 \textperiodcentered\ Article and Chart \textperiodcentered\ «La electricidad que viene del agua, del viento y del sol»", [
    r"Uruguay y Costa Rica suelen aparecer en las noticias como ejemplos de energía limpia. Costa Rica depende sobre todo de sus ríos, mientras que Uruguay transformó su sistema en solo una década gracias a cientos de molinos de viento.",
    r"Pero depender del agua tiene riesgos. En los años de sequía, las represas producen menos y los países tienen que quemar más combustibles fósiles. Por eso los expertos recomiendan diversificar: combinar hidroeléctrica, eólica y solar para que la falta de una fuente no deje a nadie sin luz.",
], 5, table=(["País (datos ficticios)", "Hidroeléctrica", "Eólica", "Solar", "Fósil"],
             [["País A", "72 \\%", "15 \\%", "3 \\%", "10 \\%"], ["País B", "30 \\%", "38 \\%", "4 \\%", "28 \\%"], ["País C", "40 \\%", "35 \\%", "20 \\%", "5 \\%"]]),
      note="Origen de la electricidad en tres países (datos ficticios).")
Q.q("1.A.2 Data", r"Según la tabla, ¿qué país depende más de la energía hidroeléctrica?",
    "el País A", [("el País B", "B gets most from wind (38%)."),
                  ("el País C", "C has 40% hydro, less than A."),
                  ("los tres por igual", "The shares differ.")],
    "País A: 72% hydro.", "Data (1.A.2).",
    ["72% > 40% > 30%."])
Q.q("1.C.1 Connect", r"Según el artículo, ¿qué país de la tabla correría más riesgo en un año de sequía?",
    "el País A, porque depende sobre todo del agua", [("el País C, porque usa energía solar", "Solar does not depend on rain."),
                                                     ("el País B, porque usa más energía fósil", "Fossil use is not hurt by drought; hydro is."),
                                                     ("ninguno, porque la sequía no afecta la electricidad", "The article says it does.")],
    "Drought hurts hydro → País A.", "Connect (1.C.1): apply the article's risk to the table.",
    ["sequía → represas producen menos → most hydro-dependent = A."])
Q.q("1.C.2 Conclusion", r"¿Qué país de la tabla sigue mejor la recomendación de los expertos?",
    "el País C, porque combina varias fuentes y usa poca energía fósil", [("el País A, porque usa mucha hidroeléctrica", "Concentration is the risk the experts warn about."),
                                                                          ("el País B, porque usa 28 \\% de energía fósil", "High fossil use is not the goal."),
                                                                          ("ninguno sigue la recomendación", "C does.")],
    "Diversify → País C.", "Conclusions (1.C.2): the recommendation (diversify) matches C's balanced mix.",
    ["C: 40/35/20/5 → diversified."])
Q.q("1.B.5 Word meaning", r"En el artículo, «diversificar» significa",
    "usar varias fuentes diferentes", [("ahorrar energía", "Not the meaning."),
                                       ("construir más represas", "That would increase concentration."),
                                       ("vender electricidad a otros países", "No.")],
    "diversificar = diversify.", "Word meaning (1.B.5): defined right after the colon.",
    ["combinar hidroeléctrica, eólica y solar."])
Q.q("1.A.1 Detail", r"¿Cómo transformó Uruguay su sistema eléctrico, según el artículo?",
    "con cientos de molinos de viento", [("con nuevas represas en sus ríos", "That describes Costa Rica."),
                                         ("con centrales nucleares", "Not mentioned."),
                                         ("importando electricidad", "Not mentioned.")],
    "molinos de viento.", "Detail (1.A.1): keep the two countries apart.",
    ["Uruguay… gracias a cientos de molinos de viento."])

Q.sec("Listening: Instructional Guidance")
Q.src(r"Listening 2 \textperiodcentered\ Instructional Guidance (transcript) \textperiodcentered\ Un mensaje de la compañía de agua durante una sequía", [
    r"(LOCUTORA) Debido a la sequía, la compañía de agua pide a todos los hogares que reduzcan su consumo. Le explicamos cómo hacerlo en cuatro pasos.",
    r"(LOCUTORA) Primero, revise las canillas y el inodoro: una pérdida pequeña puede desperdiciar cientos de litros al mes. Segundo, dúchese en menos de cinco minutos y cierre la canilla mientras se cepilla los dientes.",
    r"(LOCUTORA) Tercero, riegue las plantas solo de noche, cuando el agua no se evapora tan rápido, y nunca lave el auto con manguera. Por último, use la lavadora solo con carga completa.",
    r"(LOCUTORA) Recuerde: el agua de la represa es de todos. Si cada familia ahorra un poco, evitaremos los cortes de suministro en los barrios más altos de la ciudad.",
], 5)
Q.q("1.A.1 Detail", r"¿Qué hay que hacer primero, según el mensaje?",
    "revisar si hay pérdidas en las canillas y el inodoro", [("regar las plantas de noche", "That is the third step."),
                                                           ("usar la lavadora con carga completa", "That is the last step."),
                                                           ("ducharse en menos de cinco minutos", "That is the second step.")],
    "Primero, revise…", "Instructional Guidance: follow the sequence markers.",
    ["Primero, revise las canillas y el inodoro."])
Q.q("1.A.1 Detail", r"¿Por qué se recomienda regar las plantas de noche?",
    "porque el agua se evapora menos", [("porque el agua es más barata de noche", "Not stated."),
                                       ("porque las plantas duermen", "No."),
                                       ("porque de día está prohibido por ley", "Not stated.")],
    "no se evapora tan rápido.", "Detail (1.A.1): the reason follows cuando.",
    ["cuando el agua no se evapora tan rápido."])
Q.q("1.B.5 Word meaning", r"En el mensaje, «canilla» significa",
    "llave del agua (grifo)", [("lavadora", "No."),
                               ("manguera", "A hose is a manguera."),
                               ("ducha", "A shower is a ducha.")],
    "canilla = faucet (Río de la Plata).", "Regional vocabulary: canilla (Uruguay, Argentina) = grifo (Spain) = llave (other countries).",
    ["cierre la canilla mientras se cepilla los dientes."])
Q.q("1.B.2 Audience", r"¿A quién se dirige el mensaje?",
    "a todos los hogares de la ciudad", [("solo a los agricultores", "Farms are not mentioned."),
                                         ("a los empleados de la compañía", "It addresses customers."),
                                         ("a los turistas", "No.")],
    "pide a todos los hogares…", "Audience (1.B.2): stated in the first sentence; usted commands address households.",
    ["la compañía de agua pide a todos los hogares…"])
Q.q("1.C.3 Inference", r"¿Qué se puede inferir sobre los barrios más altos de la ciudad?",
    "que son los primeros en quedarse sin agua cuando hay poca", [("que tienen su propia represa", "Not stated."),
                                                                 ("que consumen menos agua", "Not stated."),
                                                                 ("que no sufren la sequía", "The opposite.")],
    "Cuts would hit higher neighborhoods.", "Inference (1.C.3): if saving avoids cuts there, they are the most vulnerable.",
    ["evitaremos los cortes… en los barrios más altos."])

Q.frq(kind="Argumentative Essay", head=r"Question 3 \textperiodcentered\ Argumentative Essay \textperiodcentered\ 10 points \textperiodcentered\ 55 minutes", mins=55,
      directions=[r"Vas a escribir un ensayo argumentativo para un curso universitario. Lee el tema y las fuentes escritas; después escucha la fuente auditiva (aquí, la transcripción). Escribe un ensayo que integre material de las tres fuentes para apoyar tu posición. Indica las fuentes que usas por número, título o autor."],
      sources=[dict(title=r"Fuente 1 \textperiodcentered\ Artículo \textperiodcentered\ «Una ciudad para caminar»", paras=[
          r"Desde 1999, la ciudad gallega de Pontevedra retiró la mayoría de los autos de su centro. Las plazas que antes eran estacionamientos se convirtieron en espacios para niños y mayores, y las calles volvieron a llenarse de gente.",
          r"«Antes no dejaba salir sola a mi hija; ahora va caminando al colegio», cuenta Lorena, vecina del centro. Los defensores del modelo destacan que hay menos ruido y contaminación, y que el comercio de barrio ganó clientes que pasean en lugar de pasar en auto.",
          r"El cambio, sin embargo, exigió años de inversión en estacionamientos en las afueras, buses y aceras amplias para personas con movilidad reducida."]),
               dict(title=r"Fuente 2 \textperiodcentered\ Gráfica \textperiodcentered\ Opinión de los residentes un año después de cerrar el centro al tráfico", paras=[
          r"Encuesta en cuatro ciudades que limitaron los autos en su centro (datos ficticios). Porcentaje de residentes que está de acuerdo con cada afirmación."],
                    table=(["Afirmación", "Residentes del centro", "Residentes de las afueras"], [["El aire es más limpio", "81 \\%", "64 \\%"], ["Llegar al centro es más difícil", "22 \\%", "57 \\%"], ["Volvería al sistema anterior", "12 \\%", "34 \\%"]])),
               dict(title=r"Fuente 3 \textperiodcentered\ Audio (transcripción) \textperiodcentered\ «Voces del barrio», radio local", paras=[
          r"(LOCUTOR) Hablamos con Ernesto Ruiz, dueño de una ferretería en el centro de una ciudad que acaba de prohibir los autos.",
          r"(ERNESTO) Al principio fue muy duro. Mis clientes de los pueblos cercanos venían en camioneta a cargar materiales y dejaron de venir. Los primeros seis meses vendí casi un treinta por ciento menos.",
          r"(LOCUTOR) ¿Y ahora?",
          r"(ERNESTO) La alcaldía creó zonas de carga y descarga, y empecé a hacer envíos a domicilio. Recuperé a muchos clientes. No digo que la medida sea mala, pero hay que pensar en todos, no solo en los que viven en el centro."])],
      prompt=[r"Tema del ensayo: \textbf{¿Deben las ciudades prohibir los automóviles en el centro?}"],
      model=[r"Muchas ciudades se preguntan si deben sacar los automóviles de su centro. En mi opinión, las ciudades sí deberían prohibirlos, siempre que ofrezcan alternativas para quienes viven lejos o trabajan con vehículos.",
             r"En primer lugar, un centro sin autos mejora la calidad de vida. La Fuente 1 explica que en Pontevedra las antiguas zonas de estacionamiento se convirtieron en espacios para niños y mayores, y que hoy hay menos ruido y contaminación. Los datos de la Fuente 2 lo confirman: el 81 \% de los residentes del centro y el 64 \% de los de las afueras creen que el aire es más limpio. Esto demuestra que el beneficio no se limita a quienes viven en el centro.",
             r"En segundo lugar, las calles peatonales devuelven la ciudad a las personas más vulnerables. Como cuenta Lorena en la Fuente 1, su hija ahora puede ir caminando sola al colegio. Además, según el mismo artículo, el comercio de barrio ganó clientes que pasean en lugar de pasar en auto.",
             r"Es cierto que la medida tiene costos. Ernesto Ruiz, el ferretero de la Fuente 3, vendió casi un 30 \% menos durante los primeros meses, y la gráfica muestra que el 57 \% de los residentes de las afueras siente que llegar al centro es más difícil. Sin embargo, el propio Ernesto recuperó a sus clientes cuando la alcaldía creó zonas de carga y él empezó a hacer envíos. Por lo tanto, el problema no es la prohibición en sí, sino hacerla sin planificar.",
             r"En conclusión, si las ciudades acompañan la prohibición con transporte público, estacionamientos en las afueras y zonas de carga, como hizo Pontevedra, el centro puede ser más limpio, más seguro y más vivo para todos."],
      rows=[("A Position", 1, "a clear, qualified position (yes, provided there are alternatives)", "only lists both sides"),
            ("B Source use", 2, "all three sources used accurately and named; the chart's two columns kept straight", "two sources, or mixing up center and outskirts residents"),
            ("C Argumentation", 2, "claims explained with evidence; the opposing source answered", "summaries with no link to the claims"),
            ("D Organization", 2, "introduction, two claims, concession and rebuttal, conclusion", "one paragraph per source"),
            ("E Language control", 3, "varied structures: siempre que + subjunctive, si-clause, no… sino", "basic structures; copied phrases")],
      tips=["The qualified position already answers the strongest objection.", "The opposing source (Ernesto) is conceded and then turned into support.",
            "Both columns of the chart are used precisely.", "The conclusion proposes concrete conditions drawn from Source 1."],
      ask="Write your essay in Spanish (about 300–350 words), then mark it against each row.", lines=22)

GUIDE, QSET = G, Q
