from ap_wl.model import Doc

STEM = "03-seventeenth-century"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 3: El siglo XVII", r"Unit 3 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 3 reads five required works of the Baroque: Cervantes's \emph{Don Quijote} (Part I, chapters 1--5, 8 and 9; Part II, chapter 74), Góngora's Soneto CLXVI, Quevedo's Salmo XVII, Sor Juana Inés de la Cruz's ``Hombres necios que acusáis'' and Tirso de Molina's \emph{El burlador de Sevilla y convidado de piedra}. This guide sets out the Baroque context (desengaño, conceptismo and culteranismo, honor, the comedia nueva), each work's structure, devices and themes, and a Text Comparison kit. Quotations are from public-domain editions. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 11+ \qquad Quotations I can use: \blank[10em]",
        short="Unit 3", sub="El siglo XVII")

G.sec("Context: the Baroque")
G.tex(r"""
\begin{compare}{Idea}{What it means}{Where you see it}
Desengaño & disillusion: the world is appearance; time and death undo everything & Góngora, Quevedo \\
Conceptismo & density of ideas: wordplay, paradox, wit & Quevedo, Sor Juana \\
Culteranismo & density of form: Latinate words, hyperbaton, rich imagery & Góngora \\
Honor and appearances & reputation as social life or death & \emph{El burlador}, the \emph{comedia} \\
Comedia nueva & Lope's model: three acts (jornadas), mixed verse forms, a comic servant (gracioso) & \emph{El burlador} \\
Barroco de Indias & the Baroque in the viceroyalties & Sor Juana in New Spain \\
\end{compare}

Spain in the 17th century still rules a vast empire, but faces economic crisis, wars and decline. Literature turns from Renaissance harmony to contrast, tension and a sharp awareness of time.
""")
G.q("1 Barroco", r"Which idea is most typical of Baroque literature?",
    "desengaño: the recognition that worldly things are fleeting and deceptive", [("harmony between humans and idealized nature", "That is Renaissance."),
                                                                                  ("the scientific study of heredity", "That is Naturalism."),
                                                                                  ("the expression of national identity in the Americas", "That is closer to Modernismo.")],
    "Desengaño.", "The Baroque replaces Renaissance confidence with awareness of time, death and appearances.",
    ["Barroco → desengaño."])
G.q("1 Barroco", r"Góngora's poetry, rich in Latinate vocabulary, hyperbaton and imagery, is the model of",
    "culteranismo", [("conceptismo", "Conceptismo concentrates ideas and wit; Quevedo is its model."),
                     ("Naturalismo", "No."),
                     ("Modernismo", "No.")],
    "Góngora → culteranismo.", "Both currents seek difficulty: culteranismo in form, conceptismo in ideas.",
    ["forma culta → culteranismo."])

G.sec("Cervantes, Don Quijote (1605, 1615)")
G.tex(r"""
\textbf{Opening.} ``En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor.''

\begin{compare}{Chapters}{What happens}{What to say}
I, 1 & an hidalgo reads chivalric romances until he loses his mind; he names himself, his horse and his lady & reading shapes reality; parody of the romances \\
I, 2--5 & first sally: an inn he takes for a castle; ``knighted'' by the innkeeper; beaten and brought home by a neighbor & the gap between imagination and the world \\
I, 8 & the windmills he takes for giants; Sancho warns him & idealism against reality; the comic pair \\
I, 9 & the narrator finds the rest of the story in an Arabic manuscript by Cide Hamete Benengeli & metafiction: who tells the story? (la creación literaria) \\
II, 74 & Alonso Quijano regains his sanity, renounces the romances and dies & the end of illusion; the hero becomes ``el Bueno'' \\
\end{compare}

\begin{keyidea}[Themes]
Reality and appearance; reading and the power of fiction; idealism and its cost; the relation between Don Quijote and Sancho; the novel reflecting on how novels are made.
\end{keyidea}
""")
G.q("2 Quijote", r"What causes the hidalgo's madness in Part I, chapter 1?",
    "reading too many chivalric romances", [("a blow to the head at an inn", "He is beaten later."),
                                            ("the death of Dulcinea", "Dulcinea is his invention."),
                                            ("a curse by an enchanter", "He later blames enchanters for his defeats.")],
    "Lectura → locura.", "Cervantes opens with the power, and the danger, of fiction.",
    ["se le secó el celebro."])
G.q("2 Quijote", r"What is the effect of the narrator's discovery of Cide Hamete Benengeli's manuscript in chapter 9?",
    "It calls attention to the act of storytelling and makes the narrator's authority uncertain.", [("It proves the events really happened.", "It complicates, rather than proves, the story's truth."),
                                                                                                     ("It ends Part I.", "Part I continues."),
                                                                                                     ("It introduces Sancho Panza.", "Sancho appears in chapter 7.")],
    "Metaficción.", "A translated Arabic manuscript, by a historian the narrator calls a liar by nation, adds layers of narration.",
    ["autor → manuscrito → traductor → narrador."])

G.sec("Baroque poetry: Góngora and Quevedo")
G.tex(r"""
\begin{tcolorbox}[colback=white,colframe=black!15,boxrule=0.4pt,arc=0pt,left=8pt,right=8pt]
\small \textbf{Góngora, Soneto CLXVI (1582)}\\[2pt]
Mientras por competir con tu cabello,\\ oro bruñido al sol relumbra en vano;\\ mientras con menosprecio en medio el llano\\ mira tu blanca frente el lilio bello;\\[2pt]
mientras a cada labio, por cogello,\\ siguen más ojos que al clavel temprano,\\ y mientras triunfa con desdén lozano\\ del luciente cristal tu gentil cuello,\\[2pt]
goza cuello, cabello, labio y frente,\\ antes que lo que fue en tu edad dorada\\ oro, lilio, clavel, cristal luciente,\\[2pt]
no sólo en plata o víola troncada\\ se vuelva, mas tú y ello juntamente\\ en tierra, en humo, en polvo, en sombra, en nada.
\end{tcolorbox}

\begin{compare}{Feature}{Góngora CLXVI}{Garcilaso XXIII (Unit 2)}
Structure & ``Mientras\ldots'' four times, then ``goza'' & ``En tanto que\ldots'' twice, then ``coged'' \\
Beauty & surpasses gold, lily, carnation, crystal & compared to rose, lily, gold \\
Ending & ``en tierra, en humo, en polvo, en sombra, en nada'' & ``todo lo mudará la edad ligera'' \\
Perspective & Baroque desengaño: beauty ends in nothing & Renaissance carpe diem: enjoy youth with balance \\
\end{compare}

\textbf{Quevedo, Salmo XVII (1613).} The speaker looks at his country's walls, the countryside, his house, his staff and his sword, and finds everything worn by time: ``y no hallé cosa en que poner los ojos / que no fuese recuerdo de la muerte''. The movement is from outside to inside, from the nation to the self.
""")
G.q("3 Poesía", r"Which device organizes the last line of Góngora's sonnet, ``en tierra, en humo, en polvo, en sombra, en nada''?",
    "a descending gradation that reduces beauty to nothing", [("a simile", "No comparison word."),
                                                             ("an apostrophe to the reader", "No one is addressed in this line."),
                                                             ("onomatopoeia", "No sound imitation.")],
    "Gradación.", "Each term is less substantial than the last, ending in nada.",
    ["tierra → … → nada."])
G.q("3 Poesía", r"How does the end of Góngora's sonnet differ from the end of Garcilaso's Soneto XXIII?",
    "Góngora ends in annihilation, a Baroque desengaño; Garcilaso ends with time's change, closer to Renaissance balance.", [
        ("Both end by praising old age.", "Neither praises old age."),
        ("Garcilaso is more pessimistic than Góngora.", "The reverse."),
        ("Góngora removes the carpe diem altogether.", "He keeps «goza».")],
    "nada vs. mudanza.", "A standard comparison: the same topos, two periods.",
    ["Góngora → nada; Garcilaso → mudanza."])
G.q("3 Poesía", r"In Quevedo's sonnet, the speaker moves from the walls of his country to the countryside, his house and his sword. What does this movement suggest?",
    "Decay reaches everything, from the nation to the speaker himself.", [("The speaker is traveling to a new country.", "No."),
                                                                          ("The speaker is preparing for battle.", "His sword is «vencida de la edad»."),
                                                                          ("Nature is renewing itself.", "Everything recalls death.")],
    "De lo exterior a lo interior.", "The poem narrows from the patria to the self, all marked by time.",
    ["muros → campo → casa → báculo → espada → muerte."])

G.sec("Sor Juana Inés de la Cruz, ``Hombres necios que acusáis''")
G.tex(r"""
\begin{tcolorbox}[colback=white,colframe=black!15,boxrule=0.4pt,arc=0pt,left=8pt,right=8pt]
\small Hombres necios que acusáis\\ a la mujer sin razón,\\ sin ver que sois la ocasión\\ de lo mismo que culpáis:\\[2pt]
si con ansia sin igual\\ solicitáis su desdén,\\ ¿por qué queréis que obren bien\\ si las incitáis al mal? [\ldots]\\[2pt]
¿O cuál es de más culpar,\\ aunque cualquiera mal haga:\\ la que peca por la paga\\ o el que paga por pecar?
\end{tcolorbox}

\textbf{Argument.} In redondillas (octosyllabic quatrains, abba), Sor Juana addresses men directly (apostrophe) and shows the contradiction in their judgment: they pursue women, then condemn them both for refusing (``ingrata'') and for accepting (``liviana''). Her weapons are Baroque wit: antithesis, chiasmus (``la que peca por la paga / o el que paga por pecar''), rhetorical questions. Theme: la construcción del género; a woman's intellectual voice in 17th-century New Spain.
""")
G.q("4 Sor Juana", r"Which device appears in ``la que peca por la paga / o el que paga por pecar''?",
    "chiasmus: the same words repeated in reverse order", [("simile", "No comparison word."),
                                                         ("onomatopoeia", "No."),
                                                         ("enjambment only", "The key device is the inverted repetition.")],
    "peca–paga / paga–pecar.", "Quiasmo: A-B / B-A, a conceptista device.",
    ["peca por la paga ↔ paga por pecar."])
G.q("4 Sor Juana", r"What is the main argument of ``Hombres necios''?",
    "Men blame women for faults that men themselves provoke, judging by a double standard.", [("Women should obey men without question.", "The opposite."),
                                                                                               ("Love is an illusion that ends in death.", "That is closer to Baroque desengaño poems."),
                                                                                               ("Men and women never meet.", "No.")],
    "Doble moral.", "The poem exposes contradiction in men's demands.",
    ["sois la ocasión de lo mismo que culpáis."])

G.sec("Tirso de Molina, El burlador de Sevilla y convidado de piedra (c. 1630)")
G.tex(r"""
\textbf{Plot.} Don Juan Tenorio deceives four women: the duchess Isabela in Naples (pretending to be her fiancé), the fisherwoman Tisbea, Doña Ana in Seville (whose father, Don Gonzalo de Ulloa, he kills), and the peasant bride Aminta. Whenever he is warned that he will pay before God, he answers ``¡Qué largo me lo fiáis!'' (you give me a long time to pay). He mockingly invites the stone statue of Don Gonzalo to dinner; the statue returns the invitation and drags him to hell without time to repent.

\begin{compare}{Feature}{In the play}{What to say}
Comedia nueva & three jornadas, varied verse forms, the gracioso Catalinón & the Baroque public theater \\
Honor & each deception dishonors a woman and her family & honor as the social order Don Juan attacks \\
Divine justice & ``¡Qué largo me lo fiáis!''; the statue & the danger of postponing repentance \\
Gender & women as victims of deception, and as agents who seek redress & la construcción del género \\
\end{compare}
""")
G.q("5 Burlador", r"What does Don Juan mean by ``¡Qué largo me lo fiáis!''?",
    "that divine punishment is far off, so he has time before he must repent", [("that he will marry soon", "No."),
                                                                                 ("that he owes money to a friend", "Fiar here refers to the debt of sin."),
                                                                                 ("that he fears the statue", "He mocks it.")],
    "Deuda con Dios.", "The refrain shows his arrogance toward death and judgment.",
    ["plazo largo → no se arrepiente."])
G.q("5 Burlador", r"Who is the ``convidado de piedra'' of the title?",
    "the statue of Don Gonzalo de Ulloa, whom Don Juan killed", [("Catalinón, Don Juan's servant", "He is the gracioso."),
                                                                 ("the king of Castile", "No."),
                                                                 ("Tisbea's father", "No.")],
    "La estatua.", "The stone guest brings divine justice.",
    ["Don Gonzalo → estatua → castigo."])

G.sec("Task kit: the Text Comparison")
G.tex(r"""
You analyze how literary devices in two texts (one required, one not) develop a theme the prompt gives. Scored on content (1--5) and language (1--5).

\begin{compare}{Plan}{What to do}{Example: Quevedo and a modern poem on time}
Thesis & say how both use devices to develop the theme, and how they differ & ambos usan el recorrido por un espacio para mostrar el paso del tiempo, pero\ldots \\
Body by device & one paragraph per device or idea, discussing both texts & personificación; el espacio de la casa; el final \\
Evidence & a short quotation from each text in each paragraph & ``Entré en mi casa'' / ``Volví a la casa de mi infancia'' \\
Effect & what the device does for the theme & la casa como espejo del yo \\
Conclusion & what the comparison shows & desengaño barroco vs. aceptación melancólica \\
\end{compare}

\begin{trap}
Two separate summaries, one per text, earn 2 at most. Organize by idea and keep both texts in every body paragraph.
\end{trap}
""")
G.q("6 Comparison", r"Which plan best fits the Text Comparison essay?",
    "paragraphs organized by device, each discussing both texts", [("one paragraph summarizing each text, then a conclusion", "Summaries side by side earn little."),
                                                                   ("a biography of each author", "Not asked."),
                                                                   ("a list of every device in the required text", "Devices must be tied to the given theme, in both texts.")],
    "Comparar por ideas.", "Content rewards analysis of devices in both texts in relation to the theme.",
    ["párrafo = recurso + ambos textos."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 3: El siglo XVII: Question Set", r"Unit 3 \textperiodcentered\ Question Set",
        abstract=r"""Three multiple-choice sets as on the exam: a recited poem not on the list (printed as a transcript; on the exam it plays twice), Sor Juana's ``Hombres necios que acusáis'' and Góngora's Soneto CLXVI, followed by a Text Comparison essay (10 points) on Quevedo's Salmo XVII and a modern poem, with the scoring guide and a model essay. Questions are in Spanish. Required works are quoted from public-domain editions; the recited poem and the modern poem are original. Allow about 25 minutes for the multiple choice and 35 for the essay.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Essay: \blank\ / 10 \qquad Target: 15+ MCQ and 7+ essay",
        short="Unit 3", sub="El siglo XVII")

Q.sec("Comprensión auditiva: poema recitado")
Q.src(r"Audio 1 \textperiodcentered\ Poema recitado (transcripción) \textperiodcentered\ «Reloj de arena» (poema escrito para esta práctica)", [
    r"Arena que cae, ¿adónde vas tan aprisa?\\ Fuiste montaña, fuiste playa, fuiste desierto;\\ ahora eres sólo un hilo\\ que cuenta mis horas sin mirarme.",
    r"Cuando te doy la vuelta, crees que empiezas de nuevo,\\ pero yo no empiezo de nuevo:\\ cada grano que pasa\\ me lleva un poco más hacia el fondo de cristal.",
    r"Y sin embargo, te miro caer\\ como quien mira la lluvia:\\ con miedo, sí, pero también con asombro,\\ porque en tu caída hay una luz\\ que no tiene la arena quieta.",
], 5, note="Poema original escrito para esta práctica. En el examen, el poema se escucha dos veces.")
Q.q("1.C Recursos", r"En el primer verso, la voz poética se dirige a la arena. El recurso es",
    "el apóstrofe", [("la sinécdoque", "No se nombra la parte por el todo."),
                     ("el hipérbaton", "El orden es normal."),
                     ("la aliteración", "No es el recurso principal.")],
    "Interpelación → apóstrofe.", "1.C: la voz habla a un objeto.",
    ["Arena que cae, ¿adónde vas…?"])
Q.q("1.E Función", r"¿Qué función tiene la enumeración «Fuiste montaña, fuiste playa, fuiste desierto»?",
    "mostrar la larga historia de la arena frente a su breve función actual", [("describir un viaje de la voz poética", "Habla de la arena."),
                                                                              ("establecer la rima del poema", "No hay rima regular."),
                                                                              ("presentar a otros personajes", "No.")],
    "Pasado grandioso → presente mínimo.", "1.E: la anáfora de «fuiste» contrasta con «ahora eres sólo un hilo».",
    ["fuiste … ahora eres sólo."])
Q.q("1.F Inferencia", r"¿Qué contraste establece la segunda estrofa?",
    "El reloj puede reiniciarse, pero la vida humana no.", [("La arena es más rápida que el agua.", "No."),
                                                           ("El día es más largo que la noche.", "No."),
                                                           ("El cristal es más fuerte que la arena.", "No.")],
    "Tiempo cíclico vs. vida lineal.", "1.F: «crees que empiezas de nuevo, / pero yo no».",
    ["yo no empiezo de nuevo."])
Q.q("1.D Tono", r"¿Cómo cambia el tono en la última estrofa?",
    "del temor a una mezcla de miedo y asombro", [("de la alegría a la ira", "No hay ira."),
                                                  ("de la tristeza a la indiferencia", "Hay asombro, no indiferencia."),
                                                  ("del humor a la burla", "No.")],
    "Y sin embargo… asombro.", "1.D: el giro final matiza la angustia.",
    ["con miedo, sí, pero también con asombro."])
Q.q("3.B Comparación", r"¿Con qué tópico del Barroco se relaciona el poema?",
    "la fugacidad del tiempo y la conciencia de la muerte", [("el amor cortés", "No."),
                                                            ("la exaltación del héroe guerrero", "No."),
                                                            ("la crítica de la honra", "No.")],
    "Tempus fugit.", "3.B: el reloj de arena es emblema barroco del paso del tiempo.",
    ["reloj de arena → fugacidad."])

Q.sec("Lectura: obra de la lista")
Q.src(r"Texto 1 \textperiodcentered\ Sor Juana Inés de la Cruz, «Hombres necios que acusáis» (fragmento)", [
    r"Hombres necios que acusáis\\ a la mujer sin razón,\\ sin ver que sois la ocasión\\ de lo mismo que culpáis:",
    r"si con ansia sin igual\\ solicitáis su desdén,\\ ¿por qué queréis que obren bien\\ si las incitáis al mal?",
    r"Combatís su resistencia\\ y luego, con gravedad,\\ decís que fue liviandad\\ lo que hizo la diligencia.",
    r"[\ldots] Opinión, ninguna gana,\\ pues la que más se recata,\\ si no os admite, es ingrata,\\ y si os admite, es liviana.",
    r"[\ldots] ¿O cuál es de más culpar,\\ aunque cualquiera mal haga:\\ la que peca por la paga\\ o el que paga por pecar?",
], 8, note="Edición de dominio público.")
Q.q("1.B Tema", r"¿Cuál es el tema principal del fragmento?",
    "la doble moral con que los hombres juzgan a las mujeres", [("la belleza física de la mujer", "No se describe la belleza."),
                                                               ("el amor de Dios", "No."),
                                                               ("la vida en el convento", "No.")],
    "Doble moral.", "1.B: tema explícito desde la primera estrofa.",
    ["acusáis a la mujer … sois la ocasión."])
Q.q("1.C Recursos", r"La voz poética se dirige a los «hombres necios». El recurso es",
    "el apóstrofe", [("la prosopopeya", "No se personifica nada."),
                     ("la metonimia", "No."),
                     ("la onomatopeya", "No.")],
    "Interpelación directa.", "1.C: apóstrofe y segunda persona (vosotros).",
    ["Hombres necios que acusáis…"])
Q.q("1.E Función", r"¿Qué función tienen las preguntas retóricas del poema?",
    "poner en evidencia la contradicción de los hombres sin necesidad de respuesta", [("pedir información a los lectores", "No esperan respuesta."),
                                                                                      ("expresar duda de la voz poética", "La voz está segura de su argumento."),
                                                                                      ("introducir un diálogo teatral", "No es teatro.")],
    "Pregunta retórica = argumento.", "1.E: refuerzan la acusación.",
    ["¿por qué queréis que obren bien / si las incitáis al mal?"])
Q.q("1.F Inferencia", r"Según la estrofa «Opinión, ninguna gana…», la mujer",
    "es criticada tanto si rechaza como si acepta a un hombre", [("es admirada si acepta a un hombre", "Es llamada «liviana»."),
                                                                 ("es libre de elegir sin consecuencias", "Lo contrario."),
                                                                 ("nunca es juzgada por los hombres", "No.")],
    "ingrata / liviana.", "1.F: la contradicción que denuncia el poema.",
    ["si no os admite, es ingrata, / y si os admite, es liviana."])
Q.q("1.C Recursos", r"En «la que peca por la paga / o el que paga por pecar» hay",
    "un quiasmo", [("una sinécdoque", "No."),
                   ("un símil", "No."),
                   ("una hipérbole", "No.")],
    "A-B / B-A.", "1.C: inversión de términos típica del conceptismo.",
    ["peca–paga / paga–pecar."])
Q.q("1.G Perspectiva", r"¿Qué actitud tiene la voz poética hacia los hombres?",
    "crítica y argumentativa", [("sumisa y temerosa", "Lo contrario."),
                                ("admirativa", "Los llama «necios»."),
                                ("indiferente", "Argumenta con pasión.")],
    "Acusación razonada.", "1.G: el adjetivo «necios» marca la actitud.",
    ["Hombres necios…"])
Q.q("2.C Forma", r"¿En qué forma métrica está escrito el poema?",
    "redondillas: estrofas de cuatro octosílabos con rima abba", [("sonetos endecasílabos", "No."),
                                                                 ("verso libre", "Tiene métrica y rima."),
                                                                 ("romance con rima asonante", "La rima es consonante, abba.")],
    "razón / ocasión, acusáis / culpáis.", "2.C: forma métrica.",
    ["a b b a."])
Q.q("2.E Contexto", r"¿Qué hace notable este poema en el contexto del siglo XVII?",
    "una mujer critica con rigor intelectual la moral de los hombres", [("es el primer poema escrito en español", "No."),
                                                                        ("defiende el poder absoluto del rey", "No."),
                                                                        ("fue escrito en Madrid por un soldado", "Sor Juana escribe en la Nueva España.")],
    "Voz femenina e intelectual.", "2.E: Sor Juana en la Nueva España barroca.",
    ["construcción del género."])

Q.sec("Lectura: obra de la lista")
Q.src(r"Texto 2 \textperiodcentered\ Luis de Góngora, Soneto CLXVI", [
    r"Mientras por competir con tu cabello,\\ oro bruñido al sol relumbra en vano;\\ mientras con menosprecio en medio el llano\\ mira tu blanca frente el lilio bello;",
    r"mientras a cada labio, por cogello,\\ siguen más ojos que al clavel temprano,\\ y mientras triunfa con desdén lozano\\ del luciente cristal tu gentil cuello,",
    r"goza cuello, cabello, labio y frente,\\ antes que lo que fue en tu edad dorada\\ oro, lilio, clavel, cristal luciente,",
    r"no sólo en plata o víola troncada\\ se vuelva, mas tú y ello juntamente\\ en tierra, en humo, en polvo, en sombra, en nada.",
], 7, note="Edición de dominio público.")
Q.q("1.C Recursos", r"La repetición de «mientras» al inicio de varios versos es",
    "una anáfora", [("un quiasmo", "No hay inversión."),
                    ("una onomatopeya", "No."),
                    ("una metonimia", "No.")],
    "Repetición inicial.", "1.C: la anáfora organiza los cuartetos.",
    ["Mientras … mientras … mientras … y mientras."])
Q.q("1.A Comprensión", r"Según el primer cuarteto, el oro «relumbra en vano» porque",
    "no puede igualar la belleza del cabello de la dama", [("está escondido en la tierra", "No."),
                                                          ("el sol no brilla", "El oro brilla «al sol»."),
                                                          ("la dama no lo quiere", "No.")],
    "Hipérbole: el cabello supera al oro.", "1.A: el oro compite «en vano».",
    ["por competir con tu cabello."])
Q.q("1.E Función", r"El verso «goza cuello, cabello, labio y frente» recoge los elementos de los cuartetos. ¿Qué función tiene?",
    "resumir la belleza descrita y exhortar a disfrutarla", [("introducir un nuevo personaje", "No."),
                                                            ("describir un paisaje", "No."),
                                                            ("contradecir los cuartetos", "Los resume.")],
    "Recolección + carpe diem.", "1.E: estructura de diseminación y recolección.",
    ["cuello, cabello, labio, frente ← cuartetos."])
Q.q("1.C Recursos", r"«oro, lilio, clavel, cristal luciente» corresponde, en el mismo orden, a",
    "cabello, frente, labio y cuello", [("frente, cabello, cuello y labio", "El orden sigue los cuartetos."),
                                        ("labio, cuello, frente y cabello", "No."),
                                        ("cuatro flores del jardín", "Son metáforas del cuerpo.")],
    "Correlación.", "1.C: el poema repite en orden las metáforas de los cuartetos.",
    ["oro→cabello, lilio→frente, clavel→labio, cristal→cuello."])
Q.q("1.H Tema", r"¿Cómo se desarrolla el tema en el último terceto?",
    "La belleza no solo envejece, sino que la persona entera termina reducida a nada.", [("La belleza se conserva para siempre.", "Lo contrario."),
                                                                                         ("La dama se convierte en una flor.", "La víola troncada es una imagen de decadencia."),
                                                                                         ("El poeta promete amor eterno.", "No.")],
    "Más allá de la vejez: la nada.", "1.H: el tema culmina en la muerte.",
    ["no sólo en plata … mas tú y ello juntamente … en nada."])
Q.q("3.A Comparación", r"Comparado con el Soneto XXIII de Garcilaso, el final de Góngora es",
    "más pesimista: termina en la nada y no en el cambio", [("más optimista: promete juventud eterna", "No."),
                                                           ("idéntico", "El final es distinto."),
                                                           ("ajeno al tema del tiempo", "El tema es el mismo.")],
    "Desengaño barroco.", "3.A: mismo tópico, distinta perspectiva.",
    ["Garcilaso: mudanza; Góngora: nada."])
Q.q("2.C Período", r"¿Qué rasgo del verso final es característico del Barroco?",
    "la visión desengañada de la vida como camino hacia la nada", [("la serenidad ante la naturaleza", "Eso es renacentista."),
                                                                   ("la denuncia social", "No."),
                                                                   ("el exotismo modernista", "No.")],
    "Desengaño.", "2.C: rasgo del período.",
    ["en tierra, en humo, en polvo, en sombra, en nada."])

Q.frq(kind="Text Comparison", head=r"Question 4 \textperiodcentered\ Text Comparison \textperiodcentered\ 10 points \textperiodcentered\ about 35 minutes", mins=35,
      directions=[r"Lee los dos textos. Luego, escribe un ensayo en español en el que analices los efectos de los recursos literarios que los autores emplean en los textos para desarrollar el tema del paso del tiempo. Apoya tu análisis con ejemplos de los dos textos."],
      sources=[dict(title=r"Texto 1 \textperiodcentered\ Francisco de Quevedo, Salmo XVII", paras=[
          r"Miré los muros de la patria mía,\\ si un tiempo fuertes, ya desmoronados,\\ de la carrera de la edad cansados,\\ por quien caduca ya su valentía.",
          r"Salíme al campo, vi que el sol bebía\\ los arroyos del hielo desatados,\\ y del monte quejosos los ganados,\\ que con sombras hurtó su luz al día.",
          r"Entré en mi casa; vi que, amancillada,\\ de anciana habitación era despojos;\\ mi báculo, más corvo y menos fuerte.",
          r"Vencida de la edad sentí mi espada,\\ y no hallé cosa en que poner los ojos\\ que no fuese recuerdo de la muerte."]),
               dict(title=r"Texto 2 \textperiodcentered\ «La casa» (poema escrito para esta práctica)", paras=[
          r"Volví a la casa de mi infancia.\\ El portón, que antes se abría con un empujón de niño,\\ ahora cede apenas, quejándose como un viejo.\\ En el patio, la higuera que trepábamos\\ es un esqueleto gris que no da sombra.",
          r"Busco en la pared las marcas de lápiz\\ con que mi madre medía nuestra estatura:\\ la cal las ha cubierto, como la nieve cubre los caminos.",
          r"Me miro en el espejo del pasillo\\ y no encuentro al niño que corría por aquí,\\ sino a un hombre de pelo blanco\\ que también, algún día,\\ será sólo una marca borrada en la pared."])],
      model=[r"El soneto de Quevedo, poeta del Barroco español, y el poema moderno «La casa» desarrollan el tema del paso del tiempo mediante un recorrido por espacios que se deterioran y que terminan reflejando al propio yo. Sin embargo, mientras Quevedo llega a una visión desengañada en la que todo anuncia la muerte, el poema moderno expresa una melancolía más íntima y serena.",
             r"En primer lugar, ambos textos utilizan el recorrido espacial como estructura. En Quevedo, la voz poética avanza de lo general a lo particular: mira «los muros de la patria mía», sale «al campo», entra «en mi casa» y llega a su báculo y su espada. En «La casa», el hablante también entra («Volví a la casa de mi infancia») y avanza del portón al patio, a la pared y al espejo. En los dos poemas, este movimiento hacia el interior hace que el deterioro del espacio se convierta en el deterioro de la persona.",
             r"En segundo lugar, los dos poemas emplean la personificación para mostrar el desgaste. Los muros de Quevedo están «de la carrera de la edad cansados» y los ganados aparecen «quejosos»; en el poema moderno, el portón cede «quejándose como un viejo» y la higuera es «un esqueleto gris». Estas imágenes atribuyen a las cosas el cansancio y la muerte de un cuerpo humano, de modo que el tiempo parece actuar sobre todo lo que existe.",
             r"Por último, el final de cada poema revela su perspectiva. Quevedo concluye con una afirmación absoluta: «no hallé cosa en que poner los ojos / que no fuese recuerdo de la muerte»; el tono es grave y propio del desengaño barroco. El poema moderno, en cambio, termina ante un espejo: el hablante descubre a «un hombre de pelo blanco» que será «sólo una marca borrada en la pared». La muerte está presente, pero se expresa como olvido y con nostalgia, no como advertencia moral.",
             r"En conclusión, los dos poemas convierten un lugar en un espejo del tiempo. Quevedo lo hace para enseñar el desengaño ante la fugacidad de la vida; el poema moderno, para expresar la pérdida personal de la infancia."],
      rows=[("Content", 5, "a comparative thesis on how devices (spatial movement, personification, imagery, the endings) develop the theme in both texts; quotations from both in each paragraph; analysis of effects; perspective (desengaño vs. melancholy)", "two separate summaries; devices named without effects; only one text analyzed"),
            ("Language", 5, "accurate, varied Spanish; comparison connectors (mientras, en cambio, ambos, sin embargo); literary vocabulary; organized paragraphs", "frequent errors; repetitive structures")],
      tips=["The thesis states a similarity and a difference.", "Each body paragraph treats one device in both texts, with a quotation from each.",
            "The conclusion names each text's perspective in a sentence.", "About 470 words."],
      ask="Escribe tu ensayo en español (unas 350–450 palabras). Luego, puntúalo con la guía.", lines=22)

GUIDE, QSET = G, Q
