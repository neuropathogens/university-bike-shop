from ap_wl.model import Doc

STEM = "01-families-communities"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 1: Families and Communities", r"Unit 1 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 1 asks what makes a family, how families shape values and traditions, and how communities are changing. Its recommended contexts are family relationships, community activities, social interactions and relationships, and urban and rural communities. This guide gives the vocabulary the exam assumes, the structures for describing relationships and routines, the cultural products, practices and perspectives most often tested (the extended family, godparents, the sobremesa, collective community work, rural depopulation), and an Argumentative Essay kit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Words I keep forgetting: \blank[10em]",
        short="Unit 1", sub="Families and Communities")

G.sec("Family and relationships")
G.tex(r"""
\begin{vocab}
los parientes / la familia política & relatives / in-laws & \emph{pariente} is a false friend: not \emph{parent} \\
los padrinos / el compadre, la comadre & godparents / co-parents & the bond between parents and godparents \\
el apellido paterno, materno & first and second surname & María López García: López from her father \\
criar / la crianza & to raise / upbringing & \emph{criar a los hijos} \\
cuidar a, ocuparse de & to look after & \emph{cuidar a los nietos} \\
convivir / la convivencia & to live together / coexistence & \emph{la convivencia entre generaciones} \\
llevarse bien / mal con & to get along well / badly with & \emph{me llevo bien con mi suegra} \\
la sobremesa & time talking at the table after a meal & a practice, not a dish \\
independizarse & to move out, become independent & \emph{se independizó a los 28 años} \\
el hogar & home (the household) & \emph{hogar} is warmer than \emph{casa} \\
\end{vocab}

\textbf{Products, practices, perspectives.} Two surnames (a product of naming law and custom) reflect a perspective that both lines of the family count. Godparents (\emph{padrinos}) are chosen at baptism and often stay close for life; \emph{compadrazgo} turns friends into family. The long Sunday meal and the \emph{sobremesa} reflect the value placed on unhurried time together. In many Spanish-speaking countries young adults live with their parents longer than in the United States, often for economic reasons as well as by choice.
""")
G.q("1 Familia", r"María Fernández Ruiz is the daughter of Andrés Fernández Gil and Lucía Ruiz Paz. Which surname comes from her mother?",
    "Ruiz", [("Fernández", "Fernández, the first surname, is her father's first surname."),
             ("Gil", "Gil is her father's second surname, not passed to María."),
             ("Paz", "Paz is her mother's second surname, not passed to María.")],
    "Second surname = mother's first surname.", "Children take the father's first surname and the mother's first surname, in that order (the order can now be changed by agreement in Spain).",
    ["Mother: Lucía Ruiz Paz → first surname Ruiz.", "María Fernández Ruiz: Ruiz is from her mother."])
G.q("1 Familia", r"Which word best completes: Mis abuelos ayudaron a \blank\ a mis primos cuando sus padres trabajaban en otra ciudad.",
    "criar", [("crear", "Crear means to create; criar means to raise children."),
              ("crecer", "Crecer (to grow up) is intransitive: the children grow, they are not grown."),
              ("parientes", "A noun cannot follow ayudaron a here.")],
    "criar a = to raise (children).", "Criar is to bring up or raise; crecer is to grow; crear is to create.",
    ["ayudaron a + infinitive with a direct object (a mis primos) → criar."])
G.q("1 Familia", r"In a reading, a family stays at the table talking for two hours after Sunday lunch. This practice is called",
    "la sobremesa", [("el postre", "El postre is dessert, a dish."),
                     ("la merienda", "La merienda is an afternoon snack."),
                     ("el compadrazgo", "Compadrazgo is the bond with godparents.")],
    "Sobremesa = talk after the meal.", "The sobremesa is the unhurried conversation after a meal, a practice that reflects the value of time together.",
    ["After the meal, talking at the table → la sobremesa."])

G.sec("Community and social life")
G.tex(r"""
\begin{vocab}
el barrio / el vecindario & neighborhood & \emph{la vida de barrio} \\
los vecinos / la junta de vecinos & neighbors / residents' association & \\
el voluntariado / ser voluntario & volunteering / to volunteer & \\
la minga (Andes) / el tequio (México) & collective community work & a whole village builds or repairs together \\
la solidaridad & solidarity, mutual help & \\
el comedor comunitario / el banco de alimentos & community kitchen / food bank & \\
la plaza & town square & the center of social life \\
el huerto urbano & community garden & \\
las fiestas patronales & town festival for the patron saint & \\
\end{vocab}

\textbf{Collective work.} The Andean \emph{minga} and the Mexican \emph{tequio} are practices of shared, unpaid work for the community (repairing a road, a harvest). They reflect a perspective that the community's needs come before individual convenience; many towns still organize them, and cities have borrowed the name for volunteer campaigns.

\textbf{The plaza.} The central square, with church, town hall and cafés, is a product that supports a practice (the evening \emph{paseo}, meeting neighbors) and a perspective (public space belongs to everyone).
""")
G.q("2 Comunidad", r"Un pueblo de Ecuador organiza una minga para reparar el camino. ¿Qué significa minga?",
    "trabajo colectivo y voluntario de la comunidad", [("una fiesta religiosa del pueblo", "A religious town festival is las fiestas patronales."),
                                                      ("un impuesto que pagan los vecinos", "A minga is unpaid work, not a tax."),
                                                      ("una empresa privada de construcción", "The community itself does the work.")],
    "Minga = collective community work.", "The minga (Andes) and tequio (Mexico) are traditions of shared unpaid work for the common good.",
    ["minga → whole community works together."])
G.q("2 Comunidad", r"Which perspective does the tradition of the minga most directly reflect?",
    "The community's needs come before individual convenience.", [("Work should always be paid by the hour.", "The minga is unpaid by design."),
                                                                  ("Only the government should repair roads.", "The practice is the community acting for itself."),
                                                                  ("Young people should leave rural areas.", "Nothing about migration.")],
    "Practice (minga) ↔ perspective (community first).", "A practice earns cultural credit when it is linked to the value behind it: shared responsibility.",
    ["Practice: everyone works together.", "Perspective: the common good comes first."])

G.sec("Urban and rural communities")
G.tex(r"""
\begin{vocab}
el campo / el medio rural & the countryside / rural areas & \\
el éxodo rural / la despoblación & rural flight / depopulation & \\
la España vaciada & ``emptied Spain'': depopulated rural Spain & a political term since 2019 \\
emigrar / la migración interna & to emigrate / internal migration & \\
las remesas & remittances & money sent home by emigrants \\
el teletrabajo / los nómadas digitales & remote work / digital nomads & bringing people back to villages \\
el costo (Am.) / coste (Esp.) de vida & cost of living & \\
la vivienda / el alquiler & housing / rent & \\
\end{vocab}

\textbf{Causes and effects.} Questions in this context ask why people leave (\emph{la falta de empleo, de servicios}) and what happens to those who stay (\emph{envejecimiento, cierre de escuelas}). Remittances are a major source of income in several Central American countries, and they keep family ties across borders.
""")
G.q("3 Rural", r"En un artículo: «Desde que cerró la escuela, muchas familias jóvenes se mudaron a la ciudad». ¿Qué relación hay entre las dos ideas?",
    "causa y efecto", [("contraste", "No opposing ideas; one event explains the other."),
                       ("ejemplo", "The second clause is not an example of the first."),
                       ("secuencia de instrucciones", "This is narration, not instructions.")],
    "Desde que → cause, then effect.", "Organization questions (1.B.4) ask how ideas relate; desde que, por eso, debido a mark cause and effect.",
    ["School closed → families moved."])
G.q("3 Rural", r"What are remesas?",
    "money that emigrants send to their families back home", [("rural public transport", "Unrelated to transport."),
                                                             ("a type of housing loan", "Not a loan."),
                                                             ("seasonal farm jobs", "Not a job.")],
    "Remesas = remittances.", "Remittances connect families across borders and are a major part of some economies.",
    ["remesas → money sent home."])

G.sec("Structures for relationships and routines")
G.tex(r"""
\begin{compare}{Structure}{Use}{Example}
soler + infinitive & habits & Los domingos solemos comer en casa de mis abuelos. \\
llevar + time + gerund & how long something has gone on & Llevo tres años viviendo en esta ciudad. \\
acabar de + infinitive & something just happened & Mi hermana acaba de independizarse. \\
reciprocal se & each other & Los vecinos se ayudan mucho. \\
tan\ldots como / más\ldots que & comparisons & La vida en el pueblo es más tranquila que en la ciudad. \\
mientras + imperfect & background actions & Mientras mi madre trabajaba, mi abuela nos cuidaba. \\
para que + subjunctive & purpose with a new subject & Ahorran para que sus hijos estudien. \\
\end{compare}

\begin{trap}
\emph{Llevarse bien con} (to get along) is not \emph{llevar} (to carry, to have spent time). \emph{Me llevo bien con mi hermano}; \emph{llevo dos años aquí}.
\end{trap}
""")
G.q("4 Estructuras", r"Choose the best way to say: ``We have been living in this neighborhood for ten years.''",
    "Llevamos diez años viviendo en este barrio.", [("Vivimos en este barrio desde hace diez años atrás.", "Desde hace and atrás cannot be combined."),
                                                     ("Hemos vivido en este barrio por diez años hace.", "Hace cannot end the sentence like this."),
                                                     ("Estamos diez años viviendo en este barrio.", "Duration with a gerund uses llevar, not estar.")],
    "llevar + time + gerund.", "Llevar + time + gerund (or hace + time + que + present) expresses how long an ongoing situation has lasted.",
    ["llevamos diez años viviendo."])
G.q("4 Estructuras", r"Los domingos mi familia \blank\ almorzar en casa de mi abuela.",
    "suele", [("acostumbra", "Acostumbrar needs a: acostumbra a almorzar."),
              ("sabe", "Saber + infinitive means to know how to."),
              ("acaba", "Acaba (de) means has just done something.")],
    "soler + infinitive = habit.", "Soler + infinitive expresses what someone usually does.",
    ["habit on Sundays → suele almorzar."])
G.q("4 Estructuras", r"Mis padres trabajan mucho para que nosotros \blank\ ir a la universidad.",
    "podamos", [("podemos", "Para que always takes the subjunctive."),
                ("poder", "With a new subject (nosotros), para que + subjunctive is needed."),
                ("pudimos", "The preterite does not follow para que.")],
    "para que + subjunctive.", "Para que expresses purpose and always takes the subjunctive.",
    ["para que → podamos."])

G.sec("Task kit: the Argumentative Essay")
G.tex(r"""
Unit 1 essay topics ask about family roles and community life: \emph{¿Deben los abuelos ocuparse de los nietos?}, \emph{¿Es mejor vivir en la ciudad o en el campo?}, \emph{¿Debe ser obligatorio el voluntariado?}

\begin{compare}{Move}{Phrases}{Example}
Position & En mi opinión, / Considero que & Considero que el voluntariado no debería ser obligatorio. \\
Evidence & Según la Fuente 1 / La gráfica muestra que & La gráfica muestra que solo el 18\% de los jóvenes\ldots \\
Explain & Esto demuestra que / Por lo tanto & Esto demuestra que la motivación importa más que la obligación. \\
Concede & Es cierto que\ldots; sin embargo, & Es cierto que muchos pueblos necesitan ayuda; sin embargo, \ldots \\
Conclude & En definitiva / Por todo lo anterior & Por todo lo anterior, \ldots \\
\end{compare}

\begin{keyidea}[A perspective in the essay]
The essay rubric does not require culture, but a culturally relevant example (the minga, the sobremesa) shows range in the language row and makes claims concrete.
\end{keyidea}
""")
G.q("5 Ensayo", r"Which sentence best explains a piece of evidence, as the argumentation row requires?",
    r"La Fuente 2 indica que el 60\% de los voluntarios siguió ayudando después del programa, lo cual demuestra que la experiencia crea compromiso.",
    [("La Fuente 2 tiene una gráfica sobre voluntarios.", "Naming a source without using its content earns nothing."),
     ("El voluntariado es muy bueno y muy importante.", "A claim with no evidence."),
     ("Según la Fuente 2, el 60\\% de los voluntarios siguió ayudando.", "Evidence without explanation; the link to the position is missing.")],
    "Claim + evidence + explanation.", "Row C rewards explaining how the evidence supports the claim (lo cual demuestra que…).",
    ["Evidence: 60%.", "Explanation: lo cual demuestra que…"])
G.q("5 Ensayo", r"Which transition best introduces a counterargument before rebutting it?",
    "Es cierto que", [("Por lo tanto", "Por lo tanto draws a conclusion."),
                      ("Además", "Además adds a point on the same side."),
                      ("En primer lugar", "En primer lugar begins a list of your own points.")],
    "Concede, then rebut.", "Es cierto que…; sin embargo… concedes a point and answers it, which strengthens the argument.",
    ["Counterargument → es cierto que… sin embargo."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 1: Families and Communities: Question Set", r"Unit 1 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Audio Report and an Interview for listening, an Article and Chart and a Promotional Material for reading) on family roles, community work and rural life, followed by an Argumentative Essay with three sources and the 10-point scoring guide. As on the exam, questions and choices are in Spanish. Listening sources are printed as transcripts: read each once at normal speed, then answer without rereading. All sources and data are original and fictional, written for practice. Allow about 25 minutes for the multiple choice and 55 minutes for the essay.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Essay: \blank\ / 10 \qquad Target: 15+ MCQ and 7+ essay \qquad Pace: 75 s per item",
        short="Unit 1", sub="Families and Communities")

Q.sec("Listening: Audio Report")
Q.src(r"Listening 1 \textperiodcentered\ Audio Report (transcript) \textperiodcentered\ «Abuelos a tiempo completo», Radio Sur", [
    r"(LOCUTOR) En Chile, uno de cada tres niños menores de seis años pasa la mayor parte del día con sus abuelos. Así lo indica un estudio de la Universidad del Pacífico publicado este mes.",
    r"(LOCUTOR) Para muchas familias, la razón es económica: el costo de las guarderías ha subido un cuarenta por ciento en cinco años. Pero no es solo eso. Los investigadores encontraron que muchos padres prefieren que sus hijos crezcan cerca de la familia.",
    r"(ABUELA, GLORIA) Yo cuido a mis dos nietos desde las ocho hasta las seis. Es cansador, no le voy a mentir, pero me hace sentir útil. Además, les enseño las canciones que me cantaba mi madre.",
    r"(LOCUTOR) Los expertos, sin embargo, advierten que el cuidado diario puede afectar la salud de las personas mayores. Recomiendan que los municipios ofrezcan talleres y espacios de descanso para los abuelos cuidadores.",
], 5)
Q.q("1.B.1 Main idea", r"¿Cuál es el tema principal del informe?",
    "el papel de los abuelos en el cuidado diario de los niños", [("el aumento de la natalidad en Chile", "Births are not discussed."),
                                                                ("la historia de las canciones infantiles chilenas", "Songs are one detail Gloria mentions."),
                                                                ("los nuevos programas de las guarderías", "Daycare appears only as a cost.")],
    "Main idea: grandparents as daily caregivers.", "The report opens with the statistic, gives reasons, a testimony and expert advice, all about grandparents caring for children.",
    ["Opening statistic + every segment → grandparents caring for grandchildren."])
Q.q("1.A.1 Detail", r"Según el informe, ¿qué pasó con el costo de las guarderías?",
    "Subió un 40\\% en cinco años.", [("Bajó a la mitad.", "The report says it rose."),
                                     ("Subió un 30\\% este año.", "The figure is 40% over five years."),
                                     ("No cambió en cinco años.", "It rose 40%.")],
    "40% rise in five years.", "Detail questions (1.A.1) match the figure and its time frame exactly.",
    ["ha subido un cuarenta por ciento en cinco años."])
Q.q("1.B.3 Attitude", r"¿Qué actitud tiene Gloria hacia su papel de abuela cuidadora?",
    "Lo encuentra agotador pero satisfactorio.", [("Lo hace solo por obligación y quiere dejarlo.", "She says it makes her feel useful."),
                                                ("Cree que es fácil y no le cuesta esfuerzo.", "She says it is tiring (cansador)."),
                                                ("Prefiere que sus nietos vayan a una guardería.", "She never says so.")],
    "Es cansador… pero me hace sentir útil.", "Attitude questions (1.B.3) weigh both parts of a mixed statement: tiring but rewarding.",
    ["cansador → tiring.", "me hace sentir útil → satisfying."])
Q.q("1.C.3 Inference", r"¿Qué se puede inferir sobre las canciones que Gloria enseña a sus nietos?",
    "Son una forma de transmitir tradiciones familiares.", [("Las aprendió en un taller del municipio.", "She learned them from her mother."),
                                                          ("Son canciones modernas de la radio.", "They are songs her mother sang to her."),
                                                          ("Los niños no quieren aprenderlas.", "Nothing suggests that.")],
    "Songs from her mother → tradition passed down.", "Inference (1.C.3): songs passed from great-grandmother to grandchildren carry family tradition across generations.",
    ["las canciones que me cantaba mi madre → three generations."])
Q.q("1.A.1 Detail", r"¿Qué recomiendan los expertos?",
    "que los municipios ofrezcan apoyo y descanso a los abuelos cuidadores", [("que los abuelos dejen de cuidar a los nietos", "They recommend support, not stopping."),
                                                                              ("que los padres trabajen menos horas", "Not mentioned."),
                                                                              ("que las guarderías bajen sus precios", "Not mentioned.")],
    "Talleres y espacios de descanso.", "The experts' recommendation is the last segment: workshops and rest spaces from municipalities.",
    ["Recomiendan que los municipios ofrezcan talleres y espacios de descanso."])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 1 \textperiodcentered\ Article and Chart \textperiodcentered\ «Volver al pueblo», revista Territorios", [
    r"Durante décadas, la historia de los pueblos del interior de España fue la misma: los jóvenes se iban a estudiar a la ciudad y no volvían. Hoy más de la mitad de los municipios del país tiene menos de mil habitantes, y en muchos no nace un niño desde hace años.",
    r"Sin embargo, algo empieza a cambiar. Desde 2020, el teletrabajo ha permitido que algunas familias se instalen en zonas rurales sin perder su empleo. En Valdemora, un pueblo de 300 habitantes, la escuela que iba a cerrar abrió el curso pasado con once alumnos nuevos.",
    r"«No es una vuelta masiva», advierte la geógrafa Elena Saldaña. «Sin internet rápido, médicos y transporte, las familias que llegan se marchan en dos o tres años». Para Saldaña, el futuro de los pueblos depende menos de la nostalgia que de los servicios.",
], 5, table=(["Año", "De la ciudad a un pueblo", "De un pueblo a la ciudad"],
             [["2018", "41.000", "96.000"], ["2020", "73.000", "88.000"], ["2022", "82.000", "84.000"], ["2024", "79.000", "86.000"]]),
      note="Gráfica: personas que se mudaron entre municipios de menos de 5.000 habitantes y ciudades (datos ficticios).")
Q.q("1.B.1 Purpose", r"¿Cuál es el propósito principal del artículo?",
    "presentar un cambio reciente en la despoblación rural y sus límites", [("convencer a los lectores de mudarse a Valdemora", "It reports and analyzes; it does not persuade readers to move."),
                                                                            ("criticar a los jóvenes que se van a estudiar", "The first paragraph describes the past without criticism."),
                                                                            ("explicar cómo funciona el teletrabajo", "Remote work is a cause, not the subject.")],
    "Change + its limits.", "The article sets up the old pattern, shows a recent change, then qualifies it with the geographer's warning.",
    ["Paragraph 2: algo empieza a cambiar.", "Paragraph 3: no es una vuelta masiva."])
Q.q("1.A.2 Data", r"Según la gráfica, ¿en qué año fue menor la diferencia entre las personas que se fueron a la ciudad y las que se mudaron a un pueblo?",
    "2022", [("2018", "In 2018 the gap was the largest: 96,000 vs. 41,000."),
             ("2020", "In 2020 the gap was 15,000."),
             ("2024", "In 2024 the gap was 7,000, larger than in 2022.")],
    "2022: 84,000 − 82,000 = 2,000.", "Data questions (1.A.2): compute each year's gap and compare.",
    ["Gaps: 55,000 (2018), 15,000 (2020), 2,000 (2022), 7,000 (2024)."])
Q.q("1.C.1 Connect", r"¿Qué información del artículo ayuda a explicar los datos de la gráfica a partir de 2020?",
    "El teletrabajo permitió que algunas familias se instalaran en zonas rurales.", [("Más de la mitad de los municipios tiene menos de mil habitantes.", "This describes the situation, not the post-2020 change."),
                                                                                    ("En muchos pueblos no nace un niño desde hace años.", "This explains decline, not the rise after 2020."),
                                                                                    ("Los jóvenes se iban a estudiar a la ciudad.", "This is the old pattern.")],
    "Desde 2020, el teletrabajo…", "Connect (1.C.1): the chart's jump after 2020 matches the article's cause, remote work since 2020.",
    ["Chart: moves to villages rise from 41,000 to 73,000 by 2020.", "Article: desde 2020, el teletrabajo…"])
Q.q("1.B.3 Point of view", r"¿Qué opina la geógrafa Elena Saldaña?",
    "La llegada de familias solo durará si hay servicios básicos.", [("La nostalgia es lo que hará volver a la gente.", "She says the future depends less on nostalgia than on services."),
                                                                     ("Los pueblos ya han resuelto la despoblación.", "She says it is not a mass return."),
                                                                     ("Las escuelas rurales deberían cerrar.", "She never says so.")],
    "Servicios > nostalgia.", "Point of view (1.B.3): her quotes stress internet, doctors and transport as conditions for staying.",
    ["Sin internet rápido, médicos y transporte, se marchan."])
Q.q("1.B.5 Word meaning", r"En el artículo, la expresión «se marchan» significa",
    "se van", [("se casan", "Marcharse is to leave."),
               ("se quejan", "Quejarse is to complain."),
               ("se quedan", "Quedarse is the opposite: to stay.")],
    "marcharse = irse.", "Word meaning (1.B.5): the sentence contrasts families who arrive with families who leave.",
    ["las familias que llegan se marchan → leave."])

Q.sec("Reading: Promotional Material")
Q.src(r"Reading 2 \textperiodcentered\ Promotional Material \textperiodcentered\ Un folleto municipal", [
    r"\textbf{¡Tu barrio te necesita! Programa «Vecinos que Suman»}",
    r"¿Tienes más de 16 años y un par de horas libres a la semana? Únete a nuestra red de voluntarios. Puedes acompañar a personas mayores que viven solas, ayudar en el huerto comunitario o dar clases de apoyo escolar a niños del barrio.",
    r"\textbf{Lo que ofrecemos:} formación gratuita, un certificado de horas de voluntariado (válido para becas universitarias) y la satisfacción de conocer a tus vecinos.",
    r"\textbf{Cómo participar:} inscríbete en la oficina del Centro Cívico (calle Mayor, 12) o en vecinosquesuman.es antes del 15 de octubre. Las actividades empiezan el 1 de noviembre. Plazas limitadas.",
], 5)
Q.q("1.B.2 Audience", r"¿A quién va dirigido principalmente el folleto?",
    "a residentes del barrio mayores de 16 años", [("a personas mayores que buscan compañía", "They are the people helped, not the audience recruited."),
                                                   ("a profesores que buscan empleo", "It recruits unpaid volunteers."),
                                                   ("a empresas que quieren patrocinar actividades", "No sponsorship is mentioned.")],
    "¿Tienes más de 16 años…?", "Audience (1.B.2): the direct address names who should act: people over 16 with free hours.",
    ["Únete a nuestra red de voluntarios → residents over 16."])
Q.q("1.A.1 Detail", r"¿Qué ofrece el programa a los participantes?",
    "un certificado útil para solicitar becas", [("un pago mensual", "Volunteers are not paid."),
                                                ("un viaje al final del programa", "Not mentioned."),
                                                ("clases universitarias gratuitas", "It offers training, not university classes.")],
    "Certificado válido para becas.", "The Lo que ofrecemos section lists training, a certificate for scholarships, and meeting neighbors.",
    ["certificado de horas… válido para becas."])
Q.q("1.A.1 Detail", r"¿Cuál de las siguientes actividades NO se menciona en el folleto?",
    "limpiar las calles del barrio", [("acompañar a personas mayores", "Listed: acompañar a personas mayores que viven solas."),
                                    ("trabajar en el huerto comunitario", "Listed: ayudar en el huerto comunitario."),
                                    ("dar clases de apoyo escolar", "Listed: dar clases de apoyo escolar.")],
    "Street cleaning is not listed.", "NOT questions: check each choice against the list; the one with no match is the answer.",
    ["Listed: companionship, garden, tutoring."])
Q.q("1.C.2 Conclusion", r"Si alguien se inscribe el 20 de octubre, ¿qué es más probable?",
    "No podrá participar porque el plazo ya terminó.", [("Empezará las actividades el 1 de noviembre sin problema.", "Registration closes on October 15."),
                                                        ("Recibirá el certificado inmediatamente.", "The certificate is for hours completed."),
                                                        ("Tendrá que pagar una inscripción tardía.", "No fee is mentioned.")],
    "Deadline: before October 15.", "Conclusions (1.C.2) apply the text's details to a new case: October 20 is after the deadline.",
    ["antes del 15 de octubre → too late."])
Q.q("1.B.3 Tone", r"¿Qué tono usa el folleto?",
    "entusiasta y cercano", [("formal y distante", "It uses tú and exclamations."),
                            ("irónico", "Nothing is said ironically."),
                            ("triste y preocupado", "The tone is upbeat.")],
    "¡Tu barrio te necesita! + tú.", "Tone (1.B.3): exclamations, questions and informal tú make the flyer warm and enthusiastic.",
    ["Exclamations + tú → enthusiastic, friendly."])

Q.sec("Listening: Interview")
Q.src(r"Listening 2 \textperiodcentered\ Interview (transcript) \textperiodcentered\ Una alcaldesa de un pueblo de Colombia", [
    r"(ENTREVISTADOR) Señora Rentería, usted es alcaldesa de San Isidro desde hace cuatro años. ¿Cuál era el mayor problema cuando llegó?",
    r"(ALCALDESA) Que los jóvenes se iban. Terminaban el colegio y se marchaban a Medellín porque aquí no había trabajo ni universidad.",
    r"(ENTREVISTADOR) ¿Y qué hicieron?",
    r"(ALCALDESA) Primero hablamos con ellos. Nos dijeron que no querían irse, pero que necesitaban oportunidades. Entonces abrimos un centro de formación técnica en agricultura sostenible y turismo, con clases virtuales de la universidad. También organizamos una minga cada mes para arreglar caminos y escuelas.",
    r"(ENTREVISTADOR) ¿Funcionó?",
    r"(ALCALDESA) Todavía nos falta mucho. Pero este año, por primera vez, volvieron más jóvenes de los que se fueron. Lo más importante es que ahora sienten que el pueblo también es de ellos.",
], 5)
Q.q("1.A.1 Detail", r"Según la alcaldesa, ¿por qué se iban los jóvenes?",
    "porque en el pueblo no había trabajo ni universidad", [("porque no les gustaba la vida en el campo", "They told her they did not want to leave."),
                                                           ("porque las escuelas estaban cerradas", "Schools needed repair, but that is not the reason given."),
                                                           ("porque sus familias se mudaron a Medellín", "They left alone after school.")],
    "No había trabajo ni universidad.", "The reason is stated directly in her first answer.",
    ["aquí no había trabajo ni universidad."])
Q.q("1.B.4 Organization", r"¿Cómo describe la alcaldesa el proceso que siguieron?",
    "Primero escucharon a los jóvenes y después crearon soluciones.", [("Primero construyeron la universidad y después hablaron con los jóvenes.", "She says primero hablamos con ellos."),
                                                                         ("Contrataron a una empresa extranjera.", "Not mentioned."),
                                                                         ("Esperaron a que el gobierno nacional actuara.", "The town acted itself.")],
    "Primero… entonces…", "Organization (1.B.4): primero and entonces mark the order: listen, then act.",
    ["Primero hablamos con ellos.", "Entonces abrimos un centro…"])
Q.q("1.A.1 Detail", r"¿Para qué organizan una minga cada mes?",
    "para reparar caminos y escuelas", [("para celebrar al santo del pueblo", "That would be the fiestas patronales."),
                                       ("para recaudar dinero", "The minga is collective work, not fundraising."),
                                       ("para dar clases de agricultura", "Classes are at the training center.")],
    "Arreglar caminos y escuelas.", "She names the minga's purpose directly.",
    ["una minga cada mes para arreglar caminos y escuelas."])
Q.q("1.B.3 Attitude", r"¿Qué actitud muestra la alcaldesa sobre los resultados?",
    "optimista pero consciente de que falta trabajo", [("totalmente satisfecha", "Todavía nos falta mucho."),
                                                      ("decepcionada", "She reports progress."),
                                                      ("indiferente", "She cares about the outcome.")],
    "Todavía nos falta mucho. Pero…", "Mixed attitude (1.B.3): a concession followed by progress.",
    ["Concession + progress → cautiously optimistic."])
Q.q("1.C.3 Inference", r"¿Qué quiere decir la alcaldesa con «sienten que el pueblo también es de ellos»?",
    "Los jóvenes se sienten parte de la comunidad y responsables de ella.", [("Los jóvenes compraron casas en el pueblo.", "She speaks of belonging, not ownership."),
                                                                                ("Los jóvenes gobiernan ahora el pueblo.", "She is still the mayor."),
                                                                                ("Los jóvenes quieren vender el pueblo.", "Nonsensical reading.")],
    "Belonging, not property.", "Implied meaning (1.C.3): es de ellos expresses belonging and ownership in a figurative sense.",
    ["After being consulted and working in the minga, they feel the town is theirs too."])

Q.frq(kind="Argumentative Essay", head=r"Question 3 \textperiodcentered\ Argumentative Essay \textperiodcentered\ 10 points \textperiodcentered\ 55 minutes", mins=55,
      directions=[r"Vas a escribir un ensayo argumentativo para un curso universitario. Lee el tema y las fuentes escritas; después escucha la fuente auditiva (aquí, la transcripción). Escribe un ensayo que integre material de las tres fuentes para apoyar tu posición. Indica las fuentes que usas por número, título o autor."],
      sources=[dict(title=r"Fuente 1 \textperiodcentered\ Artículo \textperiodcentered\ «Vivir en grande»", paras=[
          r"Para Javier Ortiz, ingeniero de 29 años, mudarse de su pueblo a Ciudad de México fue la mejor decisión de su vida. «Aquí tengo trabajo en mi profesión, museos, conciertos y gente de todo el país», dice.",
          r"Las grandes ciudades concentran las universidades, los hospitales especializados y la mayoría de los empleos calificados. Según el urbanista Tomás Vela, «la ciudad multiplica las oportunidades: cuantas más personas hay, más ideas se cruzan».",
          r"Pero Javier reconoce el precio: pasa casi dos horas al día en el transporte y paga la mitad de su sueldo en alquiler."]),
               dict(title=r"Fuente 2 \textperiodcentered\ Gráfica \textperiodcentered\ Satisfacción con la vida según el lugar de residencia", paras=[
          r"Encuesta a 4.000 adultos de Argentina, Colombia y México. Porcentaje que se declara «satisfecho» o «muy satisfecho» con cada aspecto (datos ficticios)."],
                    table=(["Aspecto", "Ciudad grande", "Pueblo pequeño"], [["Oportunidades de empleo", "64 \\%", "31 \\%"], ["Tiempo libre", "38 \\%", "67 \\%"], ["Relación con los vecinos", "29 \\%", "72 \\%"], ["Acceso a la salud", "71 \\%", "40 \\%"]])),
               dict(title=r"Fuente 3 \textperiodcentered\ Audio (transcripción) \textperiodcentered\ «Desde el pueblo», pódcast", paras=[
          r"(LOCUTORA) Hoy nos acompaña Rosa Quispe, que volvió hace tres años a su pueblo en el valle del Colca, en Perú.",
          r"(ROSA) En Lima ganaba más, eso es verdad. Pero no conocía a mis vecinos y mi hijo no podía jugar en la calle. Aquí todos nos conocemos; si alguien se enferma, la comunidad se organiza para ayudar.",
          r"(LOCUTORA) ¿Y el trabajo?",
          r"(ROSA) Trabajo en línea para una empresa de diseño. Sin internet no habría podido volver. Por eso digo que el pueblo puede ser el futuro, pero solo si llegan los servicios."])],
      prompt=[r"Tema del ensayo: \textbf{¿Es mejor vivir en una ciudad grande que en un pueblo pequeño?}"],
      model=[r"Durante el último siglo, millones de personas en América Latina dejaron el campo para buscar una vida mejor en la ciudad. Hoy la pregunta vuelve a plantearse. Aunque la ciudad ofrece más oportunidades profesionales, considero que, gracias a la tecnología, un pueblo pequeño puede ofrecer una vida más plena.",
             r"En primer lugar, la calidad de las relaciones humanas es mayor en los pueblos. La gráfica de la Fuente 2 muestra que el 72 \% de los habitantes de pueblos pequeños está satisfecho con su relación con los vecinos, frente al 29 \% en las ciudades grandes. Rosa Quispe lo confirma en la Fuente 3: en Lima no conocía a sus vecinos, mientras que en su pueblo «la comunidad se organiza para ayudar» cuando alguien se enferma. Esta solidaridad, que en los Andes se expresa en tradiciones como la minga, es difícil de encontrar en una metrópoli.",
             r"En segundo lugar, la vida en el pueblo deja más tiempo libre. Según la Fuente 2, el 67 \% de quienes viven en pueblos está satisfecho con su tiempo libre, casi el doble que en la ciudad. El caso de Javier Ortiz en la Fuente 1 explica por qué: pasa casi dos horas al día en el transporte.",
             r"Es cierto que la ciudad concentra el empleo calificado y los hospitales, como señala el urbanista Tomás Vela (Fuente 1), y la gráfica confirma la diferencia en el acceso a la salud. Sin embargo, el ejemplo de Rosa demuestra que el teletrabajo ya permite tener un buen empleo lejos de la capital, siempre que haya internet.",
             r"En definitiva, si los gobiernos llevaran internet y servicios de salud a las zonas rurales, el pueblo sería para muchas personas una opción mejor que la ciudad: más tiempo, más comunidad y, ahora, también oportunidades."],
      rows=[("A Position", 1, "clear position (here: the village can offer a fuller life, given services)", "only lists pros and cons of each place"),
            ("B Source use", 2, "all three sources used accurately and named", "two sources, or a misread chart (e.g., reversing the columns)"),
            ("C Argumentation", 2, "each claim explained with evidence (esto demuestra, lo confirma)", "a summary of each source with no link to the position"),
            ("D Organization", 2, "introduction, claim paragraphs, concession, conclusion; varied transitions", "source-by-source paragraphs"),
            ("E Language control", 3, "varied vocabulary and structures (relative clauses, si-clause, comparisons)", "basic sentences, copied phrases")],
      tips=["Every body paragraph combines two sources.", "The cultural reference (la minga) adds range without leaving the topic.",
            "The concession uses Es cierto que… Sin embargo…", "The conclusion's si-clause (si los gobiernos llevaran…, sería…) shows control."],
      ask="Write your essay in Spanish (about 300–350 words), then mark it against each row.", lines=22)

GUIDE, QSET = G, Q
