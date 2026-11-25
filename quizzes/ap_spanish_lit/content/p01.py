from ap_wl.model import Doc

STEM = "01-medieval"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 1: La época medieval", r"Unit 1 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 1 reads two required works from medieval Spain: the anonymous \emph{Romance de la pérdida de Alhama} and Don Juan Manuel's \emph{El conde Lucanor}, Exemplo XXXV. This guide sets out their historical context (al-Andalus, the Reconquista, oral tradition), how each work is built, its themes and the course themes it serves (las sociedades en contacto, las relaciones interpersonales, la construcción del género), the medieval Spanish you need to read the originals, and an Analysis of a Single Text kit. Quotations are from public-domain editions. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Quotations I can use: \blank[10em]",
        short="Unit 1", sub="La época medieval")

G.sec("Context: al-Andalus, the Reconquista and oral tradition")
G.tex(r"""
\begin{compare}{Date}{Event}{Why it matters for the texts}
711 & Muslim armies cross into Iberia; al-Andalus is founded & centuries of contact among Muslims, Christians and Jews \\
1335 & Don Juan Manuel, nephew of Alfonso X, finishes \emph{El conde Lucanor} & didactic prose in Castilian for a noble reader \\
1482 & Christian forces take the town of Alhama, near Granada & the event behind the romance \\
1492 & Granada, the last Muslim kingdom, falls & the end the romance foresees \\
\end{compare}

\textbf{Oral tradition.} Romances were sung and recited long before they were printed in the 16th century; they survived in many versions, including among Sephardic Jews after 1492 and in Latin America. The \emph{romances fronterizos} tell episodes of the war on the Granada frontier, often with striking sympathy for the Moorish side.
""")
G.q("1 Context", r"Which event does the \emph{Romance de la pérdida de Alhama} anticipate in its final lines?",
    "the fall of Granada in 1492", [("the Muslim arrival in 711", "That began al-Andalus; the romance looks forward, not back."),
                                     ("the writing of \\emph{El conde Lucanor}", "Unrelated."),
                                     ("the voyage of Columbus", "Not mentioned.")],
    "«y aquí se pierda Granada».", "The alfaquí's prophecy points to the loss of the whole kingdom.",
    ["pérdida de Alhama (1482) → pérdida de Granada (1492)."])
G.q("1 Context", r"Why do several versions of the same romance exist?",
    "Romances were transmitted orally before being written down.", [("Each was written by several known authors.", "They are anonymous."),
                                                                    ("Printers changed them on purpose to avoid censorship.", "Not the main reason."),
                                                                    ("They were translated from Arabic.", "They were composed in Castilian.")],
    "Oral transmission → variants.", "Singers adapted and remembered romances differently over generations.",
    ["oral → many versions."])

G.sec("Romance de la pérdida de Alhama (anonymous, 15th century)")
G.tex(r"""
\textbf{What happens.} The Moorish king of Granada learns that Alhama has been taken; he burns the letters and kills the messenger, rides to the Alhambra and calls his people to war. An old Moor asks why; the king announces the loss; an alfaquí (Muslim scholar) answers that the king deserves it for killing the Bencerrajes (Abencerrajes), ``la flor de Granada'', and prophesies that he will lose the kingdom too.

\begin{compare}{Feature}{In the text}{Effect}
Form & romance: octosyllables, assonance á-a in the even lines (Granada, ganada, matara) & oral, memorable, musical \\
Refrain & ``¡Ay de mi Alhama!'' after every stanza & a collective lament; grief grows with each repetition \\
Dialogue & the old Moor, the king, the alfaquí & dramatizes the scene; voices judge the king \\
Perspective & the loss is told from the Moorish side & sympathy for the defeated (las sociedades en contacto) \\
Verb tenses & mix of past forms (matara, hablara) as preterites & archaic, oral style \\
\end{compare}

\begin{keyidea}[Themes to write about]
Loss and punishment; the abuse of power (the king kills the messenger and the Bencerrajes); contact between Muslim and Christian societies, seen with sympathy for the enemy.
\end{keyidea}
""")
G.q("2 Alhama", r"Why does the alfaquí say the king deserves the loss?",
    "because the king killed the Bencerrajes, ``la flor de Granada''", [("because the king refused to pay the Christians", "Not in the text."),
                                                                          ("because the king lost a battle by cowardice", "Not his accusation."),
                                                                          ("because the king burned the Alhambra", "He burned the letters.")],
    "Crime → punishment.", "The alfaquí frames the loss as just punishment for past cruelty.",
    ["«Mataste los Bencerrajes, / que eran la flor de Granada»."])
G.q("2 Alhama", r"What is the main effect of the refrain ``¡Ay de mi Alhama!''?",
    "It turns the news into a collective, growing lament.", [("It gives the date of the battle.", "No."),
                                                            ("It introduces a new speaker each time.", "It is a repeated cry, not a new voice."),
                                                            ("It mocks the king.", "Its tone is grief, not mockery.")],
    "Refrain → lament.", "Repetition after every stanza makes grief the poem's constant.",
    ["estribillo → dolor colectivo."])
G.q("2 Alhama", r"The rhyme in the even lines (Granada, ganada, matara) is",
    "assonant, on á-a", [("consonant, on -ada", "Matara and Granada share only the vowels."),
                         ("absent: the poem is free verse", "The even lines rhyme."),
                         ("on every line, aabb", "Only the even lines rhyme.")],
    "Same vowels, different consonants.", "Romances use assonance in the even lines.",
    ["ga-NA-da / ma-TA-ra → á-a."])

G.sec("El conde Lucanor, Exemplo XXXV (Don Juan Manuel, 1335)")
G.tex(r"""
\textbf{Frame.} Each exemplo follows the same pattern: Count Lucanor describes a problem; his counselor Patronio tells a story; he applies it to the count's problem; the count follows the advice; Don Juan writes a moral in verse (\emph{viesos}).

\textbf{Exemplo XXXV.} A servant of the count may marry a rich woman known as ``la más fuerte et más brava cosa del mundo''. Patronio tells of a poor young Moor who asks to marry the fiercest woman in town. On the wedding night, he orders a dog, a cat and his only horse to bring him water for his hands, and kills each when it does not obey. The terrified bride obeys at once, and is obedient ever after. Her father tries the same trick on his own wife by killing a rooster; she answers that it is too late: ``ya bien nos conoscemos''. The moral: ``Si al comienzo non muestras qui eres, / nunca podrás después cuando quisieres''.

\begin{compare}{Feature}{In the text}{What to say about it}
Didactic purpose & a lesson for a noble reader & teaching through an entertaining story (enseñar deleitando) \\
Frame narrative & Lucanor--Patronio--story--moral & the story is a tool for practical counsel \\
Gradation & dog, then cat, then the only horse & rising violence and cost: the threat becomes credible \\
Ending & the father-in-law's failed rooster & humor and confirmation of the moral \\
Gender & the wife's ``bravura'' is tamed by violence & a patriarchal model of marriage; today read critically \\
\end{compare}
""")
G.q("3 Lucanor", r"What is the role of Patronio in \emph{El conde Lucanor}?",
    "the count's counselor, who answers each problem with a story", [("the young man who marries", "That is the character in the story."),
                                                                    ("the author of the book", "The author is Don Juan Manuel."),
                                                                    ("the count's enemy", "He is his trusted adviser.")],
    "Patronio = consejero.", "The frame dialogue Lucanor–Patronio introduces every exemplo.",
    ["Lucanor pregunta → Patronio cuenta."])
G.q("3 Lucanor", r"Why does the young man kill his only horse after the dog and the cat?",
    "to make his threat credible by showing he will destroy even what he cannot replace", [("because the horse attacked the bride", "The horse simply did not obey."),
                                                                                           ("because horses were forbidden at weddings", "No."),
                                                                                           ("because he wanted to sell its meat", "No.")],
    "Gradation of cost.", "Killing his only horse shows the bride that nothing is spared: «non ha cosa viva… que non faga lo que yo mandare».",
    ["perro → gato → único caballo."])
G.q("3 Lucanor", r"What does the episode of the father-in-law and the rooster add?",
    "It confirms the moral: authority must be shown at the beginning.", [("It shows the father is crueler than his son-in-law.", "His attempt fails; the point is timing."),
                                                                         ("It proves the bride was never fierce.", "No."),
                                                                         ("It introduces a new problem for Lucanor.", "No.")],
    "Too late → «ya bien nos conoscemos».", "The comic coda illustrates the verse moral about beginnings.",
    ["«tarde vos acordastes»."])

G.sec("Reading medieval Spanish")
G.tex(r"""
\begin{vocab}
fablar, fazer / facer, fijo & hablar, hacer, hijo & Latin f- later became h- \\
et / e & y & \\
homne & hombre & \\
catar & mirar & ``cató en derredor de la mesa'' \\
bravo / brava & fierce, wild & not ``brave'' \\
sañudo & furious & from saña \\
gelo & se lo & ``non gelo consejedes'' \\
cras & mañana & \\
-ades / -edes & -áis / -éis (vos forms) & ``¿qué facedes?'' \\
\end{vocab}

\begin{trap}
\emph{Bravo} in medieval Spanish means fierce or wild (``una mujer muy fuerte et muy brava''), not courageous. Reading it as ``brave'' reverses the meaning of the exemplo.
\end{trap}
""")
G.q("4 Language", r"In ``cató el novio en derredor de la mesa'', \emph{cató} means",
    "looked", [("tasted", "Modern catar can mean to taste; in medieval Spanish it means to look."),
               ("sang", "No."),
               ("sat", "No.")],
    "catar = mirar.", "Medieval catar: to look, to examine.",
    ["cató en derredor → looked around."])
G.q("4 Language", r"A woman described as ``muy fuerte et muy brava'' is",
    "strong-willed and fierce", [("brave in battle", "Bravo here means fierce or wild."),
                                 ("physically weak", "The opposite."),
                                 ("very rich", "Rich is rica.")],
    "brava = fierce.", "False friend across time: medieval bravo ≠ modern brave.",
    ["fuerte et brava → difficult, wild."])

G.sec("Task kit: the Analysis of a Single Text")
G.tex(r"""
The essay asks how a text represents its \textbf{genre} and a \textbf{historical, cultural or social context}. Organize it around both halves of the prompt.

\begin{compare}{Paragraph}{Content}{Example for Exemplo XXXV}
Introduction & author, work, period; thesis on genre + context & Don Juan Manuel usa el marco del exemplo para enseñar una lección práctica que refleja la sociedad patriarcal del siglo XIV. \\
Genre & frame, didactic purpose, moral in verse, examples from the text & el diálogo Lucanor--Patronio; la moraleja final \\
Context & what the text shows about its society; quotations & el matrimonio como alianza económica; la autoridad del marido; personajes moros \\
Conclusion & what the two halves show together & la forma didáctica legitima un modelo social \\
\end{compare}

\begin{trap}
A plot summary of the dog, the cat and the horse earns little. Use each event as evidence for a claim about genre (gradation as narrative technique) or context (marriage as hierarchy).
\end{trap}
""")
G.q("5 Essay", r"Which thesis best answers a prompt about genre and context for Exemplo XXXV?",
    "Mediante la estructura del exemplo, con su marco, su historia y su moraleja, Don Juan Manuel ofrece al noble un consejo práctico que refleja el ideal patriarcal del matrimonio en el siglo XIV.", [
        ("El cuento trata de un joven que se casa con una mujer brava.", "Summary, not a thesis."),
        ("El cuento es muy violento y no me gusta.", "A personal reaction."),
        ("Don Juan Manuel nació en 1282.", "A fact with no claim.")],
    "Genre + context + claim.", "A strong thesis names how the genre works and what context it reflects.",
    ["estructura del exemplo + ideal patriarcal."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 1: La época medieval: Question Set", r"Unit 1 \textperiodcentered\ Question Set",
        abstract=r"""Three multiple-choice sets as on the exam: a listening presentation on the romancero (printed as a transcript), an excerpt from \emph{El conde Lucanor}, Exemplo XXXV, and a non-required ballad written for this set in the frontier tradition, followed by an Analysis of a Single Text essay (10 points) with the scoring guide and a model essay. Questions are in Spanish. Required-work excerpts are from public-domain editions; the transcript and the ballad are original. Allow about 25 minutes for the multiple choice and 35 for the essay.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Essay: \blank\ / 10 \qquad Target: 15+ MCQ and 7+ essay",
        short="Unit 1", sub="La época medieval")

Q.sec("Comprensión auditiva: presentación")
Q.src(r"Audio 1 \textperiodcentered\ Presentación (transcripción) \textperiodcentered\ «El romancero, una literatura que se canta»", [
    r"(PROFESORA) Durante siglos, la mayoría de la gente en Castilla no sabía leer. Sin embargo, conocía decenas de historias en verso: los romances. Los cantaban los juglares en las plazas y los repetían las familias en casa.",
    r"(PROFESORA) El romance tiene una forma muy sencilla de recordar: versos de ocho sílabas y una misma rima asonante en los versos pares. Por eso podía pasar de boca en boca. Pero también por eso cambiaba: cada cantor añadía, olvidaba o transformaba algo.",
    r"(PROFESORA) Los romances fronterizos cuentan episodios de la guerra de Granada. Lo sorprendente es que muchos adoptan el punto de vista de los vencidos: escuchamos el dolor del rey moro, no la alegría de los vencedores.",
    r"(PROFESORA) Cuando los judíos fueron expulsados en 1492, se llevaron estos romances. Todavía hoy, en comunidades sefardíes, se cantan versiones que en España se habían perdido. El romancero es, en ese sentido, una memoria compartida que cruzó fronteras.",
], 5)
Q.q("1.A Comprensión", r"Según la profesora, ¿por qué conocía la gente los romances aunque no supiera leer?",
    "porque los juglares los cantaban y las familias los repetían", [("porque se enseñaban en las escuelas", "No se mencionan escuelas."),
                                                                    ("porque se imprimían en libros baratos", "La transmisión era oral."),
                                                                    ("porque eran obligatorios en la iglesia", "No se dice.")],
    "Transmisión oral.", "1.A: detalle explícito.",
    ["Los cantaban los juglares … los repetían las familias."])
Q.q("1.E Función", r"Según la presentación, ¿qué función tenía la forma métrica del romance?",
    "facilitar la memorización y la transmisión oral", [("demostrar la cultura del autor", "Los romances son anónimos."),
                                                        ("imitar la poesía italiana", "El soneto italiano llega en el siglo XVI."),
                                                        ("ocultar el significado a los moros", "No.")],
    "Octosílabo + asonancia → memoria.", "1.E: la forma sirve a la transmisión oral.",
    ["una forma muy sencilla de recordar."])
Q.q("1.F Inferencia", r"¿Qué se puede inferir de la frase «cada cantor añadía, olvidaba o transformaba algo»?",
    "que existen varias versiones de un mismo romance", [("que los romances eran escritos por un solo autor", "Lo contrario."),
                                                        ("que los romances se prohibieron", "No."),
                                                        ("que los cantores no sabían música", "No.")],
    "Variantes.", "1.F: la transmisión oral produce versiones distintas.",
    ["añadía, olvidaba, transformaba → variantes."])
Q.q("2.E Contexto", r"¿Qué rasgo de los romances fronterizos le parece sorprendente a la profesora?",
    "que muchos adoptan el punto de vista de los vencidos", [("que se escribieron en árabe", "No."),
                                                            ("que celebran la expulsión de los judíos", "No."),
                                                            ("que no tienen rima", "Tienen rima asonante.")],
    "Simpatía por el vencido.", "2.E: relación entre el texto y su contexto histórico.",
    ["escuchamos el dolor del rey moro."])
Q.q("1.B Tema", r"¿Cuál es la idea principal de la última parte de la presentación?",
    "El romancero sobrevivió fuera de España como memoria compartida.", [("Los romances desaparecieron en 1492.", "Siguen cantándose."),
                                                                          ("Solo los cristianos conservaron los romances.", "Los sefardíes también."),
                                                                          ("Los romances sefardíes son traducciones del inglés.", "No.")],
    "Memoria que cruzó fronteras.", "1.B: idea principal de un fragmento.",
    ["se cantan versiones que en España se habían perdido."])

Q.sec("Lectura: obra de la lista")
Q.src(r"Texto 1 \textperiodcentered\ Don Juan Manuel, \emph{El conde Lucanor}, Exemplo XXXV (fragmento)", [
    r"E luego que ellos fincaron solos en casa, asentáronse a la mesa, et ante que ella hubiese a decir cosa, cató el novio en derredor de la mesa, et vió un perro et dijol ya cuanto bravamente:",
    r"---¡Perro, danos agua a las manos!",
    r"E el perro non lo fizo. Et él comenzose a ensañar et dijol más bravamente que les diese agua a las manos. Et el perro non lo fizo. Et desque vió que lo non facía, levantose muy sañudo de la mesa et metió mano a la espada et enderezó al perro. [\ldots]",
    r"Et desque hobo catado a cada parte, vió un su caballo que estaba en casa, et él non había más de aquel et dijol muy bravamente que les diese agua a las manos: e el caballo non lo fizo [\ldots]. E cuando la mujer vió que mataba el caballo non habiendo otro et que dicía que esto faría a quiquier que su mandado non cumpliese, tovo que esto ya non se facía por juego, et hobo tan grand miedo que non sabía si era muerta o viva.",
    r"Et él así bravo et sañudo et ensangrentado tornose a la mesa [\ldots] volvió los ojos contra su mujer muy bravamente et dijol con grand saña teniendo la espada en la mano:",
    r"---Levantavos et datme agua a las manos.",
    r"E la mujer que non esperaba otra cosa sinón que la despedazaría toda, levantose muy apriesa et diol agua a las manos.",
], 8, note="Edición de 1920 (dominio público), con la ortografía medieval.")
Q.q("1.A Comprensión", r"¿Qué pide el novio al perro, al caballo y finalmente a la mujer?",
    "que le den agua para lavarse las manos", [("que le sirvan la cena", "La cena se pide después."),
                                               ("que salgan de la casa", "No."),
                                               ("que guarden silencio", "No.")],
    "agua a las manos.", "1.A: la misma orden se repite tres veces.",
    ["«danos agua a las manos»."])
Q.q("1.C Recursos", r"La repetición de la misma orden al perro, al caballo y a la mujer crea",
    "una gradación que culmina en la mujer", [("una metáfora del agua como pureza", "El agua es literal aquí."),
                                              ("un diálogo entre iguales", "Solo habla el novio."),
                                              ("una contradicción", "No hay contradicción.")],
    "Estructura en gradación.", "1.C: la repetición con variación prepara el clímax.",
    ["perro → caballo → mujer."])
Q.q("1.E Función", r"¿Qué función tiene el detalle «él non había más de aquel» al hablar del caballo?",
    "mostrar que el novio sacrifica lo único que tiene para que su amenaza sea creíble", [("indicar que el novio es rico", "Lo contrario: es pobre."),
                                                                                          ("explicar por qué el caballo no obedece", "No lo explica."),
                                                                                          ("introducir un nuevo personaje", "El caballo ya estaba en casa.")],
    "Único caballo → amenaza creíble.", "1.E: un detalle subraya el costo y la seriedad del gesto.",
    ["non había más de aquel → sacrificio."])
Q.q("1.F Inferencia", r"La frase «tovo que esto ya non se facía por juego» sugiere que la mujer",
    "comprende que el novio es capaz de matarla", [("cree que el novio está bromeando", "Lo contrario."),
                                                   ("quiere defender al caballo", "No."),
                                                   ("piensa huir de la casa", "No se dice.")],
    "Ya no es un juego.", "1.F: la mujer interpreta la escena como amenaza real.",
    ["non se facía por juego → peligro real."])
Q.q("1.A Comprensión", r"En el texto, «sañudo» significa",
    "furioso", [("asustado", "Asustada está la mujer."),
                ("cansado", "No."),
                ("prudente", "No.")],
    "saña = furia.", "1.A: vocabulario medieval en contexto.",
    ["muy sañudo … metió mano a la espada."])
Q.q("1.I Personajes", r"¿Qué revela la escena sobre el novio?",
    "que actúa con un plan calculado para imponer su autoridad desde el principio", [("que pierde el control por la locura", "La mujer lo cree, pero el cuento muestra un plan."),
                                                                                     ("que odia a los animales", "Los animales son instrumentos del plan."),
                                                                                     ("que teme a su esposa", "Lo contrario.")],
    "Plan calculado.", "1.I: las acciones revelan la intención del personaje.",
    ["ante que ella hubiese a decir cosa → actúa primero."])
Q.q("2.E Contexto", r"¿Qué rasgo de la sociedad medieval refleja el desenlace de la escena?",
    "una concepción del matrimonio basada en la autoridad del marido", [("la igualdad entre esposos", "Lo contrario."),
                                                                        ("la prohibición del matrimonio entre moros", "Los personajes son moros y se casan."),
                                                                        ("la libertad de la mujer para elegir esposo", "No.")],
    "Autoridad patriarcal.", "2.E: el texto legitima un modelo social de su época.",
    ["la mujer obedece por miedo → jerarquía."])
Q.q("2.C Género", r"¿A qué género pertenece el texto?",
    "el exemplo o cuento didáctico medieval", [("el romance épico", "Es prosa narrativa."),
                                               ("la novela picaresca", "La picaresca es del siglo XVI."),
                                               ("el teatro barroco", "No es teatro.")],
    "Exemplo = cuento con enseñanza.", "2.C: género de El conde Lucanor.",
    ["Patronio cuenta → moraleja."])

Q.sec("Lectura: obra fuera de la lista")
Q.src(r"Texto 2 \textperiodcentered\ «Romance del moro Hamete» (romance escrito para esta práctica)", [
    r"Por la vega de Antequera\\ cabalga un moro sin lanza;\\ lleva el caballo cansado\\ y la frente ensangrentada.",
    r"---¿Dónde vas, moro Hamete,\\ con la color tan mudada?\\ ---Vengo de ver mi castillo\\ en manos de gente extraña,",
    r"que ayer era de mi padre\\ y es hoy de quien lo ganara.\\ Las torres que yo guardaba\\ hoy tienen cruz levantada,",
    r"y suenan unas campanas\\ donde rezaba mi casa.\\ Mas no lloro por las torres\\ ni por la tierra ganada:",
    r"lloro porque en la frontera\\ quedó mi madre cristiana,\\ y entre la cruz y la luna\\ yo llevo partida el alma.",
], 7, note="Texto original escrito para esta práctica, en la tradición de los romances fronterizos.")
Q.q("1.A Comprensión", r"¿Qué le ha ocurrido al castillo de Hamete?",
    "Lo han conquistado los cristianos.", [("Lo ha vendido su padre.", "Fue «ganado», es decir, conquistado."),
                                          ("Lo ha destruido un terremoto.", "No."),
                                          ("Lo ha heredado Hamete.", "Lo ha perdido.")],
    "en manos de gente extraña; cruz levantada.", "1.A: detalle explícito.",
    ["hoy tienen cruz levantada."])
Q.q("1.C Recursos", r"En «hoy tienen cruz levantada» y «entre la cruz y la luna», la cruz y la luna representan",
    "el cristianismo y el islam, mediante símbolos", [("dos momentos del día", "No."),
                                                     ("dos personajes del romance", "No."),
                                                     ("la guerra y la paz", "No.")],
    "Símbolo / metonimia religiosa.", "1.C: imágenes que remiten a dos religiones.",
    ["cruz → cristianos; luna (creciente) → musulmanes."])
Q.q("3.A Comparación", r"¿Qué rasgo formal comparte este romance con el «Romance de la pérdida de Alhama»?",
    "versos octosílabos con rima asonante á-a en los pares", [("un estribillo repetido", "Este romance no tiene estribillo."),
                                                             ("catorce versos endecasílabos", "No es un soneto."),
                                                             ("prosa con diálogo", "Está en verso.")],
    "Octosílabo + á-a.", "3.A: semejanza formal entre dos textos.",
    ["lanza, ensangrentada, mudada → á-a."])
Q.q("1.E Función", r"¿Qué función tiene el diálogo inicial («¿Dónde vas, moro Hamete…?»)?",
    "dramatizar la escena y dar voz al protagonista", [("presentar al autor del romance", "Es anónimo."),
                                                       ("describir el paisaje", "El diálogo revela al personaje."),
                                                       ("resumir la guerra de Granada", "No.")],
    "Diálogo → dramatismo.", "1.E: rasgo típico del romancero.",
    ["pregunta → respuesta de Hamete."])
Q.q("1.H Tema", r"Según la última estrofa, ¿cuál es la verdadera causa del dolor de Hamete?",
    "estar dividido entre dos culturas y dos familias", [("la pérdida de sus riquezas", "Dice «no lloro por las torres»."),
                                                        ("el cansancio de su caballo", "No."),
                                                        ("una herida en la frente", "Es un detalle, no la causa.")],
    "Alma partida.", "1.H: el giro final redefine el tema.",
    ["Mas no lloro por las torres … yo llevo partida el alma."])
Q.q("1.D Tono", r"¿Qué tono predomina en el romance?",
    "melancólico", [("burlón", "No hay burla."),
                    ("triunfal", "Habla un vencido."),
                    ("indiferente", "Hamete expresa su dolor.")],
    "Lamento.", "1.D: el tono del vencido.",
    ["frente ensangrentada, color mudada, lloro."])
Q.q("3.B Comparación", r"¿Qué tema comparten este romance y el «Romance de la pérdida de Alhama»?",
    "el dolor de los vencidos en la frontera entre culturas", [("la burla del rey cristiano", "Ninguno se burla."),
                                                              ("el amor cortés", "No."),
                                                              ("la alegría de la conquista", "Ambos adoptan el punto de vista del vencido.")],
    "Sociedades en contacto.", "3.B: semejanza temática.",
    ["Alhama: dolor del rey; Hamete: alma partida."])

Q.frq(kind="Analysis of a Single Text", head=r"Question 3 \textperiodcentered\ Analysis of a Single Text \textperiodcentered\ 10 points \textperiodcentered\ about 35 minutes", mins=35,
      directions=[r"Lee el fragmento. Luego, escribe un ensayo en español en el que analices cómo el texto representa las características del exemplo medieval (el cuento didáctico) y la sociedad patriarcal de la Edad Media. Apoya tu análisis con ejemplos del texto."],
      sources=[dict(title=r"Don Juan Manuel, \emph{El conde Lucanor}, Exemplo XXXV (fragmentos)", paras=[
          r"Otra vez fablaba el conde Lucanor con su consejero Patronio, et díjole: ---Patronio, un mio criado me dijo quel tratan casamiento con una mujer muy rica et aun que es más honrrada que él, et que es el casamiento muy bueno para él sinón por un embargo que y ha, et el embargo es este: díjome quel dijeran, que aquella mujer, que era la más fuerte et más brava cosa del mundo. [\ldots]",
          r"[\ldots] Et daquel día adelante, fué aquella su mujer muy bien mandada et hobieron muy buena vida. Et dende a pocos dias su suegro quiso facer asi como ficiera su yerno, et por aquella manera mató un gallo: et díjole su mujer: ---A la fe, don fulano, tarde vos acordastes, ca ya non vos valdría nada si matásedes cient caballos, que ante lo hobiérades a comenzar, ca ya bien nos conoscemos.",
          r"Et vos señor conde, si aquel vuestro criado quiere casar con tal mujer, si fuere él tal como aquel mancebo consejalde que case seguramente, ca él sabrá como ha de pasar en su casa [\ldots] E el conde tovo este por buen consejo, et fízolo así et fallose dello bien. Et porque don Johan lo tovo por buen enjiemplo, fízolo escribir en este libro, et fizo estos viesos que dicen así:",
          r"Si al comienzo non muestras qui eres,\\ Nunca podrás despues cuando quisieres."])],
      model=[r"El conde Lucanor (1335), de Don Juan Manuel, es una colección de cuentos didácticos de la Edad Media. En el Exemplo XXXV, el autor utiliza la estructura del exemplo, con su marco, su historia y su moraleja, para dar un consejo práctico que, al mismo tiempo, refleja y legitima el modelo patriarcal del matrimonio de su época.",
             r"En primer lugar, el fragmento muestra con claridad la estructura del género. El texto comienza con el marco: el conde plantea un problema concreto a su consejero Patronio, el posible casamiento de un criado con una mujer «muy fuerte et muy brava». La historia que Patronio cuenta no es un fin en sí misma, sino un instrumento: al terminar, Patronio la aplica al caso del conde («si fuere él tal como aquel mancebo consejalde que case»). Finalmente, el narrador cierra con una moraleja en verso, «Si al comienzo non muestras qui eres, / nunca podrás después cuando quisieres», que resume la enseñanza de forma fácil de recordar. Así, el exemplo cumple el principio de enseñar deleitando: la historia entretiene, pero su función es aconsejar.",
             r"En segundo lugar, el texto refleja la sociedad patriarcal de la Edad Media. El matrimonio se presenta como un acuerdo económico y social: la novia es «muy rica» y «más honrrada» que el criado, y el único «embargo» es su carácter. El final feliz consiste en que la mujer queda «muy bien mandada», es decir, obediente, y por eso «hobieron muy buena vida». El episodio del suegro, que mata un gallo sin éxito porque su esposa le responde que «ya bien nos conoscemos», es cómico, pero confirma la misma idea: la autoridad del marido debe imponerse desde el principio. La voz de la mujer solo aparece para reconocer ese orden.",
             r"En conclusión, la forma didáctica del exemplo, con un consejero sabio y una moraleja breve, da autoridad a un modelo social jerárquico. Leído hoy, el texto permite ver cómo la literatura medieval enseñaba no solo prudencia política, sino también una visión del género que justificaba el dominio masculino."],
      rows=[("Content", 5, "a thesis on both genre (frame, story as tool, verse moral, enseñar deleitando) and context (marriage as an economic and hierarchical institution); precise quotations analyzed, not summarized", "summary of the dog, cat and horse; treating only genre or only context; quotations with no analysis"),
            ("Language", 5, "accurate, varied Spanish with literary vocabulary (marco, moraleja, didáctico, patriarcal); clear organization with transitions; correct accents", "frequent errors; repetitive structures; no paragraphs")],
      tips=["The thesis names both halves of the prompt.", "Each body paragraph opens with a claim and uses short quotations from the excerpt as evidence.",
            "The coda (the rooster) is used as evidence, not retold as plot.", "About 420 words: a full essay in 35 minutes."],
      ask="Escribe tu ensayo en español (unas 350–450 palabras). Luego, puntúalo con la guía.", lines=22)

GUIDE, QSET = G, Q
