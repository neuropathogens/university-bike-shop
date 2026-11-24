from ap_wl.model import Doc

STEM = "05-contemporary-life"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 5: Contemporary Life", r"Unit 5 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 5 asks how traditions shape daily life today: school and work, food and health, entertainment, sports and travel. Its recommended contexts are education and career, entertainment and media, food and health, pop culture, sports and leisure, and travel and tourism. This guide gives the vocabulary of daily life, the practices most often tested (meal times in Spain, sharing mate, free public universities, front-of-package warning labels, baseball in the Caribbean, sustainable tourism), the subjunctive in adjective clauses and commands, and a second Project Presentation kit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Practices I can link to a perspective: \blank[8em]",
        short="Unit 5", sub="Contemporary Life")

G.sec("Education and careers")
G.tex(r"""
\begin{vocab}
la carrera & university degree program; career & \emph{¿Qué carrera estudias?} = What is your major? \\
el colegio / el liceo / el bachillerato & school / secondary school / secondary diploma & \emph{colegio} is not college \\
la beca & scholarship & \\
las prácticas / la pasantía & internship & \\
el desempleo / el paro (Esp.) & unemployment & \\
la fuga de cerebros & brain drain & \\
la universidad pública & public university & tuition-free in Argentina; nearly free at Mexico's UNAM \\
\end{vocab}

\textbf{Practices and perspectives.} In much of the Spanish-speaking world, students choose a \emph{carrera} at 18 and study it from the first year, instead of choosing a major later. Tuition-free public universities (Argentina) reflect a view of higher education as a public right. Many young people live at home while they study.
""")
G.q("1 Educación", r"Un estudiante dice: «Estudio la carrera de Medicina». ¿Qué significa?",
    "Está estudiando un programa universitario de Medicina.", [("Corre en una competencia de medicina.", "Carrera also means race, but not in this context."),
                                                            ("Ya trabaja como médico.", "He is studying, not working."),
                                                            ("Va a un colegio de secundaria.", "Colegio is school; carrera is a university program.")],
    "Carrera = degree program.", "Word meaning from context (1.B.5): estudiar la carrera de… = to study a degree in…",
    ["estudio la carrera de → university program."])
G.q("1 Educación", r"Argentina's public universities charge no tuition. Which perspective does this practice most directly reflect?",
    "Higher education is a public right, not a privilege.", [("Universities should be run as businesses.", "The opposite view."),
                                                             ("Only wealthy families should study.", "Free tuition opens access."),
                                                             ("Students should choose their major late.", "Unrelated.")],
    "Free tuition ↔ education as a right.", "Linking the practice (no tuition) to the perspective (equal access) is what the culture rows reward.",
    ["Practice: no tuition.", "Perspective: education as a right."])

G.sec("Food and health")
G.tex(r"""
\begin{vocab}
el desayuno / el almuerzo (la comida) / la merienda / la cena & breakfast / lunch / afternoon snack / dinner & \\
la dieta mediterránea & Mediterranean diet & UNESCO intangible heritage (2010, extended 2013) \\
compartir el mate & sharing mate & Argentina, Uruguay, Paraguay \\
la comida chatarra / ultraprocesada & junk / ultra-processed food & \\
los sellos (octógonos) de advertencia & front-of-package warning labels & Chile 2016, Mexico 2020 \\
el impuesto a las bebidas azucaradas & tax on sugary drinks & Mexico, 2014 \\
\end{vocab}

\textbf{Schedules.} In Spain, lunch is usually the main meal, eaten around 2 to 3 p.m., and dinner is often at 9 or 10 p.m. \textbf{Mate} is shared from one gourd passed around a circle; refusing it can seem cold, and saying \emph{gracias} means you are done. The practice reflects the value of friendship and trust.

\textbf{Public health.} Black octagon labels (\emph{ALTO EN AZÚCARES}, \emph{ALTO EN SODIO}) on packaged food aim to make unhealthy content obvious at a glance.
""")
G.q("2 Alimentación", r"En España, ¿a qué hora suele ser el almuerzo, la comida principal del día?",
    "entre las dos y las tres de la tarde", [("a las doce del mediodía en punto", "Earlier than usual in Spain."),
                                            ("a las seis de la tarde", "That is merienda time."),
                                            ("a las nueve de la mañana", "That is breakfast.")],
    "Spanish lunch: about 2–3 p.m.", "Meal times are a classic cultural practice; in Spain lunch is late and dinner is later.",
    ["Main meal ≈ 14:00–15:00."])
G.q("2 Alimentación", r"While sharing mate with Uruguayan friends, you say gracias as the gourd is handed to you. What will your friends understand?",
    "that you do not want any more", [("that you want a second turn immediately", "Gracias signals you are finished."),
                                      ("that the mate is too hot", "Not what gracias means here."),
                                      ("that you will prepare the next round", "The cebador prepares it.")],
    "Gracias = I'm done.", "Small rules of a shared practice (who serves, when to say thanks) reflect the value of the circle of friends.",
    ["In the mate circle, gracias means no more for me."])
G.q("2 Salud", r"¿Cuál es el objetivo de los sellos negros de advertencia en los alimentos envasados?",
    "que los consumidores vean rápidamente si un producto tiene exceso de azúcar, sodio o grasas", [("decorar los paquetes", "They are warnings, not decoration."),
                                                                                                  ("indicar que el producto es orgánico", "They warn about excess, not about origin."),
                                                                                                  ("mostrar el precio con descuento", "Unrelated.")],
    "Warning labels = make excess obvious.", "ALTO EN… octagons show high sugar, sodium, fat or calories at a glance.",
    ["ALTO EN AZÚCARES → excess sugar."])

G.sec("Entertainment, sports and travel")
G.tex(r"""
\begin{vocab}
el partido / el equipo / la afición & match / team / fans & \\
el clásico & big rivalry match & Real Madrid--Barcelona; Boca--River in Buenos Aires \\
el béisbol & baseball & the main sport in the Dominican Republic, Cuba and Venezuela \\
la lucha libre & Mexican masked wrestling & \\
la telenovela / la serie & soap opera / series & \\
el turismo sostenible / el ecoturismo & sustainable tourism / ecotourism & Costa Rica's national parks \\
el turismo masivo & mass tourism & residents' protests in Barcelona and other cities \\
el Camino de Santiago & medieval pilgrimage route to Santiago de Compostela & walked today for faith, sport or reflection \\
\end{vocab}

\textbf{Perspectives in sport and leisure.} A club is often a neighborhood identity passed from parents to children. Costa Rica built tourism around protected nature, reflecting a view that conservation and the economy can go together; cities with mass tourism debate limits so that neighborhoods stay livable.
""")
G.q("3 Ocio", r"In which country is baseball, not soccer, the most popular sport?",
    "the Dominican Republic", [("Argentina", "Soccer is dominant in Argentina."),
                               ("Spain", "Soccer is dominant in Spain."),
                               ("Chile", "Soccer is dominant in Chile.")],
    "Caribbean baseball.", "Baseball dominates in the Dominican Republic, Cuba and Venezuela.",
    ["Dominican Republic → baseball."])
G.q("3 Turismo", r"¿Qué perspectiva refleja el modelo de turismo de Costa Rica, basado en parques nacionales y reservas?",
    "que proteger la naturaleza y desarrollar la economía pueden ir juntos", [("que el turismo debe prohibirse", "Costa Rica welcomes tourists."),
                                                                             ("que los hoteles grandes son la prioridad", "The model centers protected nature."),
                                                                             ("que la naturaleza no tiene valor económico", "The opposite.")],
    "Ecotourism: conservation + economy.", "The practice (ecotourism) reflects the perspective that conservation pays.",
    ["Protected areas attract visitors → conservation as an economic asset."])

G.sec("Structures: adjective clauses and commands")
G.tex(r"""
\begin{compare}{Structure}{Use}{Example}
Subjunctive in adjective clauses & the thing is unknown or may not exist & Busco un trabajo que \emph{tenga} horario flexible. \\
Indicative in adjective clauses & the thing exists and is known & Tengo un trabajo que \emph{tiene} horario flexible. \\
No hay nadie que / ningún & non-existent & No hay ningún restaurante que \emph{abra} a las seis. \\
Commands, tú & affirmative = 3rd sg. present; negative = subjunctive & Come más frutas. No comas tanta sal. \\
Commands, usted & subjunctive & Siga recto. No olvide su pasaporte. \\
Gustar-type verbs & interesar, preocupar, encantar, hacer falta & A los jóvenes les preocupa el empleo. \\
\end{compare}
""")
G.q("4 Estructuras", r"Elige la forma correcta: Quiero estudiar una carrera que me \blank\ viajar.",
    "permita", [("permite", "The career is not yet known or chosen, so the clause takes the subjunctive."),
                ("permitirá", "The future does not fit an unknown antecedent."),
                ("permitir", "A conjugated verb is needed after que.")],
    "Unknown antecedent → subjunctive.", "When the noun described is hypothetical (una carrera que…), the adjective clause uses the subjunctive.",
    ["una carrera (not yet chosen) → permita."])
G.q("4 Estructuras", r"Elige el mandato negativo correcto (tú): \blank\ comida chatarra antes de entrenar.",
    "No comas", [("No come", "Negative tú commands use the subjunctive form."),
                 ("No comes", "That is a statement, not a command."),
                 ("No comer", "An infinitive is used on signs, not when addressing someone as tú.")],
    "Negative tú command = no + subjunctive.", "Affirmative: come; negative: no comas.",
    ["no + comas."])

G.sec("Task kit: developing a factor in the presentation")
G.tex(r"""
Each factor in the Project Presentation should follow the same four steps, about 40 seconds in all:

\begin{terms}
1 Claim & \emph{El segundo factor es la migración.} \\
2 Evidence & one specific fact or example from your research: a place, a date, a name, a practice \\
3 Perspective & \emph{Esto refleja\ldots / Esto muestra la importancia de\ldots} \\
4 Link & connect to the prompt or the next factor: \emph{Por eso, \ldots / Además, \ldots} \\
\end{terms}

\begin{keyidea}[Change over time]
Prompts often ask how a tradition has changed. Use time markers (\emph{en los años sesenta, hoy en día, a partir de}) and the preterite/imperfect contrast: \emph{Antes la cumbia se tocaba con gaitas; hoy se mezcla con sintetizadores}.
\end{keyidea}
""")
G.q("5 Presentación", r"Which sequence develops a factor most completely?",
    "claim, specific example from research, perspective it reflects, link to the next idea", [("claim, then the next factor", "No detail or perspective."),
                                                                                              ("example, then a personal opinion", "No claim or perspective."),
                                                                                              ("a definition of the genre only", "No claim, example or perspective.")],
    "Claim → evidence → perspective → link.", "Full task and culture credit come from detailed factors that reach a perspective.",
    ["All four steps → full development."])
G.q("5 Presentación", r"Elige la forma correcta: Antes la cumbia \blank\ con gaitas y tambores; hoy se mezcla con sintetizadores.",
    "se tocaba", [("se tocó", "A habitual past description takes the imperfect."),
                  ("se toca", "Antes contrasts with hoy; the first clause is past."),
                  ("se tocará", "The future contradicts antes.")],
    "Antes + imperfect for habit.", "Contrast past habit (imperfect) with the present.",
    ["antes (habit) → se tocaba."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 5: Contemporary Life: Question Set", r"Unit 5 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Audio Report and a Presentation for listening, an Article and Chart and a Promotional Material for reading) on food labels, careers, the Camino de Santiago and meal times, followed by a second practice Project Presentation on music, with the 11-point scoring guide and a model script. The presentation prompt is a practice prompt, not the official 2027 project prompt. As on the exam, questions and choices are in Spanish; listening sources are printed as transcripts. All sources and data are original and fictional. Allow about 25 minutes for the multiple choice and 6 minutes for the presentation.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Presentation: \blank\ / 11 \qquad Target: 15+ MCQ and 8+ presentation",
        short="Unit 5", sub="Contemporary Life")

Q.sec("Listening: Audio Report")
Q.src(r"Listening 1 \textperiodcentered\ Audio Report (transcript) \textperiodcentered\ «Los octógonos negros», Radio Salud", [
    r"(PERIODISTA) Hace unos años, los paquetes de galletas, cereales y refrescos en México empezaron a mostrar octógonos negros con mensajes como «exceso de azúcares» o «exceso de sodio». La idea vino de Chile, que adoptó un sistema parecido en 2016.",
    r"(PERIODISTA) ¿Funcionan? Según un estudio de una universidad mexicana, en el primer año la compra de refrescos con sellos bajó un 7 por ciento. Además, muchas empresas cambiaron sus recetas para reducir el azúcar y evitar los sellos.",
    r"(NUTRIÓLOGA) Lo más interesante es el efecto en los niños. Ellos entienden los octógonos sin saber leer las etiquetas pequeñas, y muchas veces son ellos quienes convencen a sus padres de no comprar un producto.",
    r"(PERIODISTA) Las empresas critican que los sellos asustan a los consumidores, pero los médicos responden que la obesidad infantil es un problema demasiado grave para esperar.",
], 5)
Q.q("1.A.1 Detail", r"¿De dónde vino la idea de los octógonos negros?",
    "de Chile", [("de España", "Not mentioned."),
                 ("de Estados Unidos", "Not mentioned."),
                 ("de una empresa de refrescos", "Companies criticize the labels.")],
    "La idea vino de Chile.", "Detail (1.A.1).",
    ["La idea vino de Chile, que adoptó un sistema parecido en 2016."])
Q.q("1.A.1 Detail", r"Según el estudio, ¿qué pasó en el primer año?",
    "Bajó un 7 \\% la compra de refrescos con sellos.", [("Subió un 7 \\% la venta de galletas.", "Wrong product and direction."),
                                                        ("Desaparecieron todos los refrescos.", "Exaggeration."),
                                                        ("Bajó un 70 \\% la obesidad infantil.", "No such figure.")],
    "−7% purchases of labeled sodas.", "Detail (1.A.1): match product, direction and figure.",
    ["la compra de refrescos con sellos bajó un 7 por ciento."])
Q.q("1.C.3 Inference", r"¿Por qué muchas empresas cambiaron sus recetas?",
    "para que sus productos no tuvieran sellos", [("para bajar los precios", "Not stated."),
                                                 ("porque los niños lo pidieron por carta", "Not stated."),
                                                 ("para vender en Chile", "Not stated.")],
    "para… evitar los sellos.", "The purpose is stated: reduce sugar to avoid the labels.",
    ["cambiaron sus recetas para… evitar los sellos."])
Q.q("1.B.3 Point of view", r"¿Qué destaca la nutrióloga?",
    "que los niños entienden los sellos e influyen en las compras de sus padres", [("que los sellos son demasiado pequeños", "She says children understand them without reading small labels."),
                                                                                  ("que los niños no deberían ir al supermercado", "Not her point."),
                                                                                  ("que los sellos no funcionan con los adultos", "Not stated.")],
    "Lo más interesante es el efecto en los niños.", "Point of view (1.B.3): lo más interesante es… flags her emphasis.",
    ["…son ellos quienes convencen a sus padres."])
Q.q("1.B.4 Organization", r"¿Cómo termina el reportaje?",
    "con las posturas opuestas de las empresas y de los médicos", [("con una receta saludable", "No."),
                                                                  ("con la historia de Chile", "Chile is mentioned at the start."),
                                                                  ("con una entrevista a un niño", "No.")],
    "Las empresas critican… pero los médicos responden…", "Organization (1.B.4): the ending sets two views against each other.",
    ["critican… pero… responden."])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 1 \textperiodcentered\ Article and Chart \textperiodcentered\ «¿Qué quieren ser?», revista Futuro", [
    r"Una encuesta a 3.000 jóvenes peruanos de entre 16 y 20 años revela cómo han cambiado sus aspiraciones. Las carreras tradicionales, como Derecho o Medicina, siguen siendo populares, pero las relacionadas con la tecnología han crecido con fuerza.",
    r"La sorpresa está en los oficios técnicos. Cada vez más jóvenes eligen formaciones cortas en gastronomía, mecánica de autos eléctricos o turismo. «Antes, la familia esperaba que el hijo fuera doctor o abogado. Hoy un buen técnico gana igual o más, y empieza a trabajar antes», explica el orientador vocacional Raúl Cárdenas.",
    r"Cárdenas advierte, sin embargo, que la presión familiar no ha desaparecido: muchos jóvenes que prefieren un oficio todavía sienten que deben justificar su decisión.",
], 5, table=(["Área elegida", "2015", "2025"], [["Salud y Derecho", "38 \\%", "30 \\%"], ["Tecnología e informática", "14 \\%", "26 \\%"], ["Oficios técnicos", "9 \\%", "19 \\%"], ["Otras", "39 \\%", "25 \\%"]]),
      note="Porcentaje de jóvenes que eligen cada área (datos ficticios).")
Q.q("1.A.2 Data", r"Según la tabla, ¿qué área casi duplicó su porcentaje entre 2015 y 2025?",
    "Tecnología e informática", [("Salud y Derecho", "It fell from 38% to 30%."),
                                 ("Otras", "It fell."),
                                 ("Ninguna área cambió", "Several changed.")],
    "14 → 26 (almost double).", "Data (1.A.2): compare the two columns for each row. Oficios técnicos (9 → 19) more than doubled; tecnología almost doubled.",
    ["14% → 26%: ×1.86."])
Q.q("1.C.1 Connect", r"¿Qué dato de la tabla confirma «la sorpresa» del artículo?",
    "el aumento de los oficios técnicos del 9 \\% al 19 \\%", [("la bajada de Salud y Derecho", "The article says those remain popular."),
                                                               ("el 39 \\% de Otras en 2015", "Not the surprise."),
                                                               ("el 26 \\% de Tecnología", "That is the growth of technology, mentioned before the surprise.")],
    "Sorpresa = oficios técnicos.", "Connect (1.C.1): La sorpresa está en los oficios técnicos ↔ 9% → 19%.",
    ["Article: sorpresa → oficios.", "Chart: 9% → 19%."])
Q.q("1.B.3 Point of view", r"Según Raúl Cárdenas, ¿por qué los jóvenes eligen oficios técnicos?",
    "porque un buen técnico puede ganar igual o más y empieza a trabajar antes", [("porque sus familias se lo exigen", "Families traditionally expected professions."),
                                                                                    ("porque las universidades cerraron", "Not stated."),
                                                                                    ("porque no les interesa la tecnología", "Technology careers grew too.")],
    "gana igual o más, y empieza a trabajar antes.", "Point of view (1.B.3).",
    ["Hoy un buen técnico gana igual o más…"])
Q.q("1.B.5 Word meaning", r"En el artículo, «oficios» se refiere a",
    "trabajos prácticos que requieren una formación técnica", [("oficinas del gobierno", "False friend with oficina."),
                                                              ("carreras universitarias largas", "They are described as short training."),
                                                              ("cartas formales", "Oficio can mean an official letter, but not here.")],
    "oficio = trade.", "Word meaning (1.B.5): examples (gastronomía, mecánica, turismo) define it.",
    ["formaciones cortas en gastronomía, mecánica… → trades."])
Q.q("1.C.2 Conclusion", r"¿Qué conclusión se puede sacar del último párrafo?",
    "Las expectativas familiares todavía influyen en las decisiones de los jóvenes.", [("Las familias ya no opinan sobre las carreras.", "La presión familiar no ha desaparecido."),
                                                                                     ("Los oficios están mal pagados.", "The article says the opposite."),
                                                                                     ("Todos los jóvenes eligen oficios.", "Only 19%.")],
    "La presión familiar no ha desaparecido.", "Conclusions (1.C.2) from Cárdenas's warning.",
    ["…todavía sienten que deben justificar su decisión."])

Q.sec("Reading: Promotional Material")
Q.src(r"Reading 2 \textperiodcentered\ Promotional Material \textperiodcentered\ Un anuncio de una agencia de viajes", [
    r"\textbf{CAMINO DE SANTIAGO SIN PRISAS \textperiodcentered\ Los últimos 100 kilómetros}",
    r"Camina de Sarria a Santiago de Compostela en siete etapas cortas y recibe la Compostela, el certificado oficial del peregrino. Nosotros llevamos tu mochila de alojamiento en alojamiento: tú solo disfruta del paisaje gallego.",
    r"\textbf{Incluye:} alojamiento en albergues privados y casas rurales, desayunos, traslado de equipaje, credencial del peregrino y seguro de viaje. \textbf{No incluye:} almuerzos ni cenas.",
    r"\textbf{Importante:} para obtener la Compostela debes sellar tu credencial al menos dos veces al día. Recomendamos entrenar caminando 10 kilómetros diarios durante el mes anterior.",
    r"Salidas de abril a octubre. Grupos de máximo 12 personas.",
], 5)
Q.q("1.B.2 Audience", r"¿A quién va dirigido el anuncio?",
    "a personas que quieren hacer el Camino con comodidad y organización", [("a peregrinos que quieren caminar desde Francia", "It covers only the last 100 km."),
                                                                           ("a empresas que buscan oficinas en Galicia", "Unrelated."),
                                                                           ("a ciclistas profesionales", "It is a walking trip.")],
    "Sin prisas + we carry your backpack.", "Audience (1.B.2): the offer (short stages, luggage transfer) targets walkers who want comfort.",
    ["sin prisas, etapas cortas, llevamos tu mochila."])
Q.q("1.A.1 Detail", r"¿Qué NO está incluido en el precio?",
    "los almuerzos y las cenas", [("el traslado de equipaje", "Included."),
                                  ("los desayunos", "Included."),
                                  ("el seguro de viaje", "Included.")],
    "No incluye: almuerzos ni cenas.", "Detail (1.A.1) from the No incluye line.",
    ["No incluye: almuerzos ni cenas."])
Q.q("1.A.1 Detail", r"¿Qué hay que hacer para recibir la Compostela?",
    "sellar la credencial al menos dos veces al día", [("caminar 10 kilómetros diarios durante un mes", "That is training advice, not the requirement."),
                                                     ("viajar en un grupo de 12 personas", "That is the group size."),
                                                     ("dormir en albergues públicos", "The trip uses private albergues and rural houses.")],
    "Sellar… dos veces al día.", "Distinguish requirement from recommendation.",
    ["para obtener la Compostela debes sellar tu credencial…"])
Q.q("1.B.5 Word meaning", r"En el anuncio, «etapas» significa",
    "partes del recorrido que se hacen cada día", [("estaciones de tren", "No trains are involved."),
                                                  ("tipos de alojamiento", "No."),
                                                  ("certificados", "The certificate is the Compostela.")],
    "etapa = stage.", "Word meaning (1.B.5): siete etapas cortas over a 100 km walk → daily stages.",
    ["100 km in siete etapas → daily sections."])
Q.q("1.C.2 Conclusion", r"Una persona quiere hacer el Camino en diciembre con esta agencia. ¿Qué le dirán?",
    "Que no hay salidas en esa fecha.", [("Que el grupo será de 30 personas.", "Maximum 12."),
                                        ("Que recibirá la Compostela sin caminar.", "Contradicts the requirements."),
                                        ("Que el viaje incluye todas las comidas.", "Lunches and dinners are not included.")],
    "Salidas de abril a octubre.", "Apply the schedule to the new case: December is outside it.",
    ["Salidas de abril a octubre."])

Q.sec("Listening: Presentation")
Q.src(r"Listening 2 \textperiodcentered\ Presentation (transcript) \textperiodcentered\ «¿Por qué cenan tan tarde los españoles?»", [
    r"(PROFESOR) Muchos turistas se sorprenden cuando ven restaurantes vacíos a las siete de la tarde en Madrid. La explicación es en parte histórica: en 1940, España adelantó sus relojes una hora para alinearse con Alemania, y nunca volvió al horario de su zona geográfica.",
    r"(PROFESOR) Así, aunque el reloj marque las dos, el sol está en un punto que en otros países corresponde a la una. Las comidas siguieron al sol, no al reloj.",
    r"(PROFESOR) Pero no todo es geografía. La comida principal, el almuerzo, sigue siendo larga y social, y el día laboral a menudo tiene una pausa al mediodía. Eso empuja la cena hacia las nueve o las diez.",
    r"(PROFESOR) Hoy hay un debate: algunos expertos proponen volver al huso horario original y adoptar jornadas laborales continuas para mejorar el descanso y la conciliación familiar. Otros defienden el horario como parte del estilo de vida español.",
], 5)
Q.q("1.B.1 Main idea", r"¿Cuál es el tema central de la presentación?",
    "las razones de los horarios de comida en España", [("la historia de los restaurantes de Madrid", "Restaurants are just the opening example."),
                                                       ("la relación política entre España y Alemania", "Mentioned only as a cause."),
                                                       ("las recetas típicas de la cena española", "No recipes.")],
    "Why Spaniards eat late.", "Main idea (1.B.1): the title question and every paragraph give reasons.",
    ["historical, solar, work-day reasons."])
Q.q("1.A.1 Detail", r"¿Qué ocurrió en 1940, según el profesor?",
    "España adelantó sus relojes una hora para coincidir con Alemania.", [("España cambió su comida principal a la noche.", "Not stated."),
                                                                          ("Se prohibió cenar antes de las nueve.", "No such law."),
                                                                          ("España volvió a su huso horario geográfico.", "It never went back.")],
    "1940: clocks moved forward.", "Detail (1.A.1).",
    ["España adelantó sus relojes una hora…"])
Q.q("1.C.3 Inference", r"¿Qué quiere decir «las comidas siguieron al sol, no al reloj»?",
    "que la gente come según la luz del día, aunque la hora oficial sea más tardía", [("que los españoles no usan relojes", "Figurative misreading."),
                                                                                     ("que se come al aire libre", "No."),
                                                                                     ("que el sol se pone más tarde en invierno", "Not the point.")],
    "Solar time vs. clock time.", "Implied meaning (1.C.3): meal times stayed tied to the sun's position.",
    ["Clock says 2:00, sun says 1:00 → meals look late."])
Q.q("1.B.4 Organization", r"¿Cómo está organizada la presentación?",
    "Presenta una pregunta, explica varias causas y termina con un debate actual.", [("Narra la vida de un turista de principio a fin.", "No narrative."),
                                                                                   ("Compara España con Alemania en cada párrafo.", "Germany appears once."),
                                                                                   ("Da instrucciones para adaptarse al horario.", "No instructions.")],
    "Question → causes → debate.", "Organization (1.B.4): Pero no todo es geografía adds a second cause; Hoy hay un debate closes.",
    ["Structure follows the markers."])
Q.q("1.B.3 Point of view", r"¿Qué proponen algunos expertos?",
    "volver al huso horario original y tener jornadas laborales continuas", [("cenar a las siete de la tarde por ley", "No law proposed."),
                                                                             ("eliminar el almuerzo", "No."),
                                                                             ("cerrar los restaurantes por la noche", "No.")],
    "Huso horario + jornada continua.", "Point of view (1.B.3): separate the two sides of the debate.",
    ["proponen volver al huso horario original y adoptar jornadas laborales continuas."])

Q.frq(kind="Project Presentation", head=r"Question 1 \textperiodcentered\ Project Presentation (practice prompt) \textperiodcentered\ 11 points \textperiodcentered\ 3 + 3 minutes", mins=6,
      directions=[r"Imagine that your project examined how a musical tradition from a Spanish-speaking community has changed as it reaches new generations and places. You have 3 minutes to prepare, using your notes, and 3 minutes to present. Explain at least three factors, with specific examples from your research, and show how cultural perspectives relate to cultural products or practices."],
      prompt=[r"Prompt: \textbf{¿Cómo ha cambiado una tradición musical del mundo hispanohablante al llegar a nuevas generaciones y lugares?}",
              r"Practice focus (example): the cumbia, from the Colombian Caribbean coast to Peru, Mexico and Argentina."],
      model=[r"Hoy voy a hablar de cómo ha cambiado la cumbia desde sus orígenes en la costa caribeña de Colombia hasta hoy. Me enfoqué en tres factores: la mezcla de raíces, la migración de la música a otros países y su papel en las fiestas populares.",
             r"El primer factor es la mezcla de raíces. Según lo que investigué, la cumbia nació de la unión de tradiciones indígenas, como las gaitas, africanas, como los tambores, y españolas, como el canto y la vestimenta. Esta mezcla refleja la identidad mestiza de la región: la cumbia no pertenece a un solo pueblo, sino al encuentro de varios.",
             r"El segundo factor es la migración. Cuando la cumbia llegó a Perú en los años sesenta, los músicos la mezclaron con guitarras eléctricas y con melodías andinas, y así nació la chicha, la música de los migrantes andinos en Lima. En México y en Argentina también surgieron estilos propios. Esto demuestra que cada comunidad adapta la música para contar su propia historia.",
             r"Por último, la cumbia sigue siendo la música de las fiestas. En muchas bodas, cumpleaños y celebraciones de barrio, es el ritmo que hace bailar a abuelos y nietos al mismo tiempo. Esta práctica refleja la importancia de celebrar en comunidad, sin distinción de edad.",
             r"En conclusión, la cumbia ha cambiado de instrumentos, de países y de público, pero conserva su función de unir a la gente. Lo que más me sorprendió fue que una música nacida de la mezcla haya seguido mezclándose: quizás por eso nunca ha dejado de ser popular."],
      rows=[("A Task", 2, "three or more factors, each explained with relevant details", "factors named with no detail, or only one or two factors"),
            ("B Culture", 2, "examples linking perspectives (mixed identity, community) to products or practices", "examples with no perspective (1 point)"),
            ("C Organization", 2, "introduction naming the factors, ordered body, conclusion; varied transitions", "a list of facts"),
            ("D Language", 3, "varied vocabulary and structures (passive se, preterite/imperfect, subjunctive after sorprender)", "a limited set of basic structures"),
            ("E Delivery", 2, "clear pronunciation, natural pace and intonation", "hesitant or rushed speech")],
      tips=["Each factor follows claim → specific example → perspective (refleja, demuestra).", "Change over time is shown with dates (los años sesenta) and preterite narration.",
            "The conclusion uses a subjunctive after me sorprendió que (haya seguido).", "About 370 words."],
      ask="Prepare for 3 minutes using keywords only, then present aloud for 3 minutes. Then mark your presentation.", lines=14)

GUIDE, QSET = G, Q
