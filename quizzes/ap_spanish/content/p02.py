from ap_wl.model import Doc

STEM = "02-language-culture"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 2: Language and Culture", r"Unit 2 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 2 asks how language and customs express identity, and how Spanish lives alongside other languages. Its recommended contexts are customs and celebrations, linguistics, and Spanish in the world. This guide gives the vocabulary of celebrations and of language itself, the major traditions most often tested (Día de Muertos, las posadas, the quinceañera, Inti Raymi, las Fallas), the regional variety of Spanish (voseo, vosotros, seseo), the languages Spanish shares space with (Guaraní, Quechua, Nahuatl, English), the impersonal and accidental \emph{se}, and a Project Q\&A kit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Traditions I can explain in 40 seconds: \blank[8em]",
        short="Unit 2", sub="Language and Culture")

G.sec("Customs and celebrations")
G.tex(r"""
\begin{vocab}
celebrar / festejar & to celebrate & \emph{festejar} is common in the Americas \\
la ofrenda / el altar & offering / altar & Día de Muertos \\
el cempasúchil & Mexican marigold & its color and scent guide the souls \\
las posadas & nine nights before Christmas (Dec. 16--24) & reenacting the search for lodging \\
la quinceañera / los quince & a girl's 15th birthday / the celebration & \\
la rosca de Reyes & ring-shaped cake for January 6 & whoever finds the figurine hosts on Feb. 2 \\
el desfile / la procesión & parade / religious procession & Semana Santa \\
la herencia / el patrimonio & heritage & \emph{patrimonio cultural inmaterial} \\
\end{vocab}

\begin{compare}{Tradition}{When and where}{Perspective it reflects}
Día de Muertos & Nov. 1--2, Mexico (UNESCO intangible heritage, 2008) & death as part of life; the dead stay part of the family \\
Las posadas & Dec. 16--24, Mexico and Central America & hospitality and community faith \\
La quinceañera & a girl's 15th birthday, across Latin America and the U.S. & a family's pride in a coming of age \\
Inti Raymi & June 24, Cusco, Peru & Inca heritage and gratitude to the sun at the winter solstice \\
Las Fallas & March 15--19, Valencia, Spain & satire, renewal: giant figures are burned \\
Día de Reyes & January 6, Spain and Latin America & gifts tied to the Magi, not Santa Claus \\
\end{compare}
""")
G.q("1 Celebraciones", r"En una ofrenda de Día de Muertos, ¿para qué se usan las flores de cempasúchil?",
    "para guiar a las almas con su color y su aroma", [("para decorar el árbol de Navidad", "Día de Muertos is not Christmas."),
                                                     ("para preparar el pan de muerto", "The bread is baked, not made from flowers."),
                                                     ("para alejar a los visitantes vivos", "Families welcome both the living and the dead.")],
    "Cempasúchil guides the souls.", "Product (cempasúchil) ↔ perspective: the dead return and are welcomed home.",
    ["The marigolds' color and scent mark the path home for the souls."])
G.q("1 Celebraciones", r"Which perspective does the Día de Muertos ofrenda most directly reflect?",
    "Those who have died remain part of the family.", [("Death should not be mentioned in public.", "The holiday celebrates the dead openly."),
                                                       ("Only children take part in the celebration.", "The whole family takes part."),
                                                       ("Gifts should be exchanged on January 6.", "That is Día de Reyes.")],
    "Ofrenda → the dead stay part of the family.", "Photos, favorite foods and personal objects on the altar express that the dead are remembered and welcomed.",
    ["Practice: building an altar with the person's favorite food.", "Perspective: the dead remain family."])
G.q("1 Celebraciones", r"A text describes a festival in Cusco on June 24 that honors the sun. Which festival is it?",
    "Inti Raymi", [("Las Fallas", "Las Fallas is in Valencia in March."),
                   ("Las posadas", "Las posadas are Dec. 16--24 in Mexico."),
                   ("La Tomatina", "La Tomatina is a tomato fight in Buñol, Spain, in August.")],
    "Inti Raymi = Inca festival of the sun.", "Inti Raymi (Quechua: festival of the sun) is held in Cusco at the June solstice.",
    ["Cusco + sun + June 24 → Inti Raymi."])

G.sec("Spanish in the world")
G.tex(r"""
Spanish has about 500 million native speakers and is official in 20 countries plus Puerto Rico; more than 40 million people in the United States speak it at home. The Real Academia Española (1713) and the 23 academies of the ASALE describe the language together, so \emph{the} standard is pan-Hispanic, not Spain's.

\begin{compare}{Feature}{Where}{Example}
voseo & Argentina, Uruguay, much of Central America & \emph{Vos tenés razón} (= tú tienes) \\
vosotros & Spain & \emph{¿Vosotros venís?}; in the Americas, \emph{ustedes} for all \\
seseo & the Americas, the Canary Islands, Andalusia & \emph{ce, ci, z} sound like \emph{s} \\
words that differ & everywhere & bus: \emph{guagua} (Caribbean), \emph{colectivo} (Argentina), \emph{camión} (Mexico) \\
\end{compare}

\textbf{Languages alongside Spanish.} Paraguay is officially bilingual: most people speak Guaraní, and switching between the two languages (\emph{jopara}) is normal. Quechua is spoken by millions in Peru, Bolivia and Ecuador; Nahuatl and other Indigenous languages in Mexico. In the U.S., bilingual speakers move between English and Spanish (code-switching), sometimes called Spanglish.
""")
G.q("2 Variedades", r"In which country would you most likely hear: «¿Vos querés venir al cine?»",
    "Argentina", [("España", "Spain uses tú (and vosotros), not vos."),
                  ("México", "Mexico uses tú."),
                  ("Cuba", "Cuba uses tú.")],
    "Voseo → Río de la Plata, Central America.", "Voseo (vos querés, vos tenés) is standard in Argentina and Uruguay and common in Central America.",
    ["vos + querés → voseo → Argentina."])
G.q("2 Variedades", r"Which statement about Paraguay is accurate?",
    "Spanish and Guaraní are both official, and most people speak Guaraní.", [("Only Spanish is official, and Guaraní is no longer spoken.", "Guaraní is co-official and widely spoken."),
                                                                             ("Quechua is the most widely spoken language.", "Quechua is mainly Andean (Peru, Bolivia, Ecuador)."),
                                                                             ("Portuguese is the official language.", "Portuguese is Brazil's language.")],
    "Paraguay: bilingual Spanish–Guaraní.", "Paraguay is the clearest case of widespread bilingualism with an Indigenous language.",
    ["Spanish + Guaraní, both official."])

G.sec("Linguistics: where words come from")
G.tex(r"""
\begin{compare}{Source}{When and why}{Examples}
Arabic & 711--1492, al-Andalus & almohada, aceite, azúcar, ojalá, ajedrez \\
Nahuatl & contact in Mexico & chocolate, tomate, aguacate, chicle \\
Quechua & contact in the Andes & papa, llama, cóndor, cancha \\
Taíno & first contact, Caribbean & huracán, canoa, hamaca, barbacoa \\
English & technology, sports, business & el fútbol, el wifi, el estrés, hacer clic \\
\end{compare}

\begin{trap}[False friends]
\emph{embarazada} = pregnant (not embarrassed: \emph{avergonzado}); \emph{éxito} = success (exit: \emph{salida}); \emph{realizar} = to carry out (to realize: \emph{darse cuenta}); \emph{actual} = current (actual: \emph{real}); \emph{carpeta} = folder.
\end{trap}
""")
G.q("3 Lingüística", r"Words like almohada, aceite and ojalá entered Spanish from",
    "Arabic", [("Latin", "Spanish comes from Latin, but these words came later, from Arabic."),
               ("Nahuatl", "Nahuatl gave words like chocolate and tomate."),
               ("English", "English gave recent words like wifi and estrés.")],
    "al-Andalus (711–1492) → Arabic loanwords.", "Eight centuries of Arabic-speaking rule in Iberia left thousands of words, many beginning with a-/al-.",
    ["al- prefix + ojalá → Arabic."])
G.q("3 Lingüística", r"Un estudiante escribe: «Estoy muy embarazado por mi error». ¿Qué palabra debía usar?",
    "avergonzado", [("embarazada", "Embarazada means pregnant."),
                    ("excitado", "Excitado suggests arousal or agitation, not embarrassment."),
                    ("realizado", "Realizado means fulfilled or carried out.")],
    "embarrassed = avergonzado.", "Embarazada is a false friend: it means pregnant.",
    ["False friend → avergonzado."])

G.sec("Structures: the many uses of se")
G.tex(r"""
\begin{compare}{Use}{Pattern}{Example}
Passive se & se + verb agrees with the thing & Se celebran muchas fiestas en verano. \\
Impersonal se & se + 3rd-person singular, people in general & En Paraguay se habla guaraní. \\
Accidental se & se + me/te/le + verb: unplanned events & Se me olvidó la tarea. Se le rompieron los platos. \\
Reciprocal & each other & Los primos se escriben cada semana. \\
Reflexive & to oneself & Nos vestimos de blanco para la fiesta. \\
\end{compare}

\begin{keyidea}[Why it matters]
Passive and impersonal \emph{se} let you describe customs without naming who does them: \emph{Se come pan de muerto; se visitan los cementerios}. That is exactly what presentations and Q\&A answers about traditions need.
\end{keyidea}
""")
G.q("4 Se", r"Choose the correct form: En Valencia \blank\ figuras enormes de cartón durante las Fallas.",
    "se queman", [("se quema", "With passive se, the verb agrees with figuras (plural)."),
                  ("se queman a", "No preposition before a thing in passive se."),
                  ("quemamos se", "The pronoun goes before the conjugated verb.")],
    "Passive se agrees with the thing.", "In passive se, the verb agrees with the noun: se queman figuras.",
    ["figuras (plural) → se queman."])
G.q("4 Se", r"Which sentence presents losing the keys as an accident?",
    "Se me perdieron las llaves.", [("Perdí las llaves a propósito.", "A propósito means on purpose."),
                                   ("Me perdí las llaves.", "Perderse means to get lost oneself."),
                                   ("Se perdí las llaves.", "Se cannot pair with a first-person verb this way.")],
    "Accidental se: se + me + verb agrees with the thing.", "Se me perdieron las llaves: the keys got lost on me (not my intention).",
    ["se + me + perdieron (agrees with llaves)."])

G.sec("Task kit: the Project Q\\&A")
G.tex(r"""
The four recorded questions follow your presentation. You hear each twice and have 40 seconds to answer. Questions usually ask you to expand on a factor, give an example, compare with your own community, and reflect on what you learned.

\begin{compare}{Question type}{Opening}{Then}
Expand & Como mencioné en mi presentación, \ldots & add one new fact from your research \\
Example & Un buen ejemplo es\ldots & say why it matters (perspective) \\
Compare & En mi comunidad, en cambio, \ldots & one similarity or difference, then why \\
Reflect & Lo que más me sorprendió fue\ldots & what it taught you about the culture \\
\end{compare}

\begin{keyidea}[The culture row in 40 seconds]
You need one answer with a cultural comparison \emph{or} a link between a perspective and a product or practice. Plan it before the exam: \emph{En Paraguay se canta en guaraní en las fiestas familiares, lo que muestra el orgullo por la lengua; en mi familia, en cambio, \ldots}
\end{keyidea}

\begin{trap}
Forty seconds is about 70--90 words. Answer the question in the first sentence, then support it. Do not restart your presentation.
\end{trap}
""")
G.q("5 Q&A", r"The interlocutor asks: ¿En qué se parece la tradición que investigaste a una tradición de tu comunidad? What does a strong answer need?",
    "a specific similarity or difference and what it shows about each culture", [("a summary of the whole presentation", "Repeating the presentation does not answer the question."),
                                                                                 ("a list of facts about the tradition only", "The question asks for a comparison."),
                                                                                 ("a description of how you did the research", "The research process is not the topic.")],
    "Compare + explain.", "A cultural comparison that explains what each practice reflects can earn the top culture score.",
    ["Similarity/difference → why → perspective."])
G.q("5 Q&A", r"About how many words fit in a 40-second Q&A answer at a natural pace?",
    "70 to 90", [("15 to 20", "That is about one sentence, too short to be complete."),
                 ("200 to 250", "That would require very fast speech."),
                 ("400", "That is a full written essay.")],
    "40 s ≈ 70–90 words.", "At about two words per second, 40 seconds holds four to six sentences.",
    ["Plan: answer + example + why."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 2: Language and Culture: Question Set", r"Unit 2 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (a Presentation and an Audio and Chart for listening, a Literary Text and an Article for reading) on bilingualism, celebrations and the Spanish language, followed by a practice Project Q\&A on music, the 2026--27 project lens, with the 9-point scoring guide and model answers. The Q\&A questions are practice questions written for this set, not official prompts. As on the exam, questions and choices are in Spanish; listening sources are printed as transcripts. All sources and data are original and fictional. Allow about 25 minutes for the multiple choice and 10 minutes for the Q\&A.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Q\&A: \blank\ / 9 \qquad Target: 15+ MCQ and 6+ Q\&A \qquad Pace: 75 s per item",
        short="Unit 2", sub="Language and Culture")

Q.sec("Listening: Presentation")
Q.src(r"Listening 1 \textperiodcentered\ Presentation (transcript) \textperiodcentered\ Una conferencia sobre el bilingüismo en Paraguay", [
    r"(PROFESORA) Paraguay es un caso único en América: casi siete de cada diez paraguayos hablan guaraní, una lengua indígena, y la mayoría de ellos también habla español. Desde 1992, la Constitución reconoce las dos lenguas como oficiales.",
    r"(PROFESORA) Durante mucho tiempo, sin embargo, hablar guaraní en la escuela estaba mal visto. Mi propia abuela recibía castigos si lo hablaba en clase. Hoy los niños estudian en las dos lenguas, y el guaraní aparece en la radio, en las redes sociales y hasta en las canciones de rock.",
    r"(PROFESORA) En la vida diaria, muchos paraguayos mezclan las dos lenguas en una misma frase. A esa mezcla se le llama «jopara». Algunos la critican, pero los lingüistas la consideran una muestra de la vitalidad de las dos lenguas.",
    r"(PROFESORA) En conclusión, el caso paraguayo demuestra que una lengua indígena puede sobrevivir y crecer cuando la comunidad la valora y la ley la protege.",
], 5)
Q.q("1.B.1 Main idea", r"¿Cuál es la idea principal de la conferencia?",
    "El guaraní sigue vivo en Paraguay gracias al valor que le da la comunidad y a la protección legal.", [("El guaraní está desapareciendo de Paraguay.", "The speaker describes growth, not decline."),
                                                                                                       ("Los paraguayos prefieren el español en todas las situaciones.", "Most speak Guaraní and mix the two."),
                                                                                                       ("La mezcla de lenguas es un error que hay que corregir.", "Linguists see jopara as vitality.")],
    "Conclusion = main idea.", "The concluding sentence (en conclusión…) states the main idea: valued and protected, the language survives and grows.",
    ["En conclusión, … puede sobrevivir y crecer…"])
Q.q("1.A.1 Detail", r"Según la profesora, ¿qué le pasaba a su abuela?",
    "La castigaban si hablaba guaraní en clase.", [("No sabía hablar español.", "Not stated."),
                                                  ("Enseñaba guaraní en la universidad.", "Not stated."),
                                                  ("Cantaba canciones de rock en guaraní.", "Rock in Guaraní is today's situation.")],
    "Recibía castigos si lo hablaba en clase.", "Detail (1.A.1): match the anecdote exactly.",
    ["Mi abuela recibía castigos…"])
Q.q("1.B.4 Organization", r"¿Cómo organiza la profesora la información en el segundo párrafo?",
    "Compara la situación del pasado con la de hoy.", [("Da instrucciones para aprender guaraní.", "No instructions."),
                                                      ("Presenta una lista de causas económicas.", "Nothing about the economy."),
                                                      ("Describe un problema sin solución.", "The paragraph shows change for the better.")],
    "Durante mucho tiempo… Hoy…", "Organization (1.B.4): time markers set up a before/after contrast.",
    ["durante mucho tiempo vs. hoy → past vs. present."])
Q.q("1.B.5 Word meaning", r"Según la conferencia, ¿qué es el «jopara»?",
    "la mezcla de guaraní y español en una misma frase", [("una canción tradicional paraguaya", "It is a way of speaking."),
                                                         ("una ley que protege las lenguas", "The law is the Constitution."),
                                                         ("un dialecto del portugués", "Portuguese is not mentioned.")],
    "A esa mezcla se le llama «jopara».", "Definitions inside the source answer word-meaning questions.",
    ["se le llama «jopara» → the mixing."])
Q.q("1.B.3 Point of view", r"¿Qué opinan los lingüistas sobre el jopara, según la profesora?",
    "que demuestra la vitalidad de las dos lenguas", [("que daña el aprendizaje del español", "That is the critics' view, not the linguists'."),
                                                     ("que debería prohibirse en la escuela", "Not stated."),
                                                     ("que solo lo usan las personas mayores", "Not stated.")],
    "Muestra de vitalidad.", "Point of view (1.B.3): separate the critics' view (algunos la critican) from the linguists'.",
    ["pero los lingüistas la consideran una muestra de la vitalidad…"])

Q.sec("Reading: Literary Text")
Q.src(r"Reading 1 \textperiodcentered\ Literary Text \textperiodcentered\ «El altar de la abuela» (fragmento de un cuento)", [
    r"Cada primero de noviembre, la casa de la abuela Toña olía a naranja y a cempasúchil. Aquel año yo tenía doce y me tocó, por primera vez, poner la foto del abuelo en el altar. La sostuve con las dos manos, como si pudiera romperse.",
    r"—Ponla arriba, mija, donde pueda vernos a todos —dijo la abuela, sin dejar de cortar el papel picado.",
    r"Yo no entendía cómo un muerto iba a vernos, pero obedecí. Junto a la foto pusimos un vasito de mezcal, su sombrero de los domingos y un plato de mole que la abuela había cocinado desde el amanecer. «Le gustaba más picante», murmuró, y añadió otro chile.",
    r"Esa noche, cuando las velas temblaron sin que hubiera viento, la abuela sonrió como quien recibe una visita esperada. Yo dejé de preguntar.",
], 5)
Q.q("1.A.1 Detail", r"¿Qué le tocó hacer a la narradora por primera vez?",
    "poner la foto de su abuelo en el altar", [("cocinar el mole", "The grandmother cooked it."),
                                               ("cortar el papel picado", "The grandmother was cutting it."),
                                               ("comprar las flores", "Not mentioned.")],
    "Me tocó poner la foto del abuelo.", "Detail (1.A.1) from the opening paragraph.",
    ["me tocó, por primera vez, poner la foto…"])
Q.q("1.C.3 Inference", r"¿Qué sugiere la frase «la sostuve con las dos manos, como si pudiera romperse»?",
    "que la narradora sentía la importancia del momento", [("que la foto estaba rota", "The comparison is figurative: como si."),
                                                         ("que la narradora tenía miedo de su abuela", "Nothing suggests fear of the grandmother."),
                                                         ("que la foto era muy pesada", "Weight is not the point of como si pudiera romperse.")],
    "Care with the photo → solemnity.", "Implied meaning (1.C.3): handling the photo as if fragile shows how much the moment meant.",
    ["como si pudiera romperse → she treats it as precious."])
Q.q("1.B.3 Attitude", r"¿Qué actitud tiene la abuela hacia los muertos?",
    "los trata como miembros de la familia que vienen de visita", [("les tiene miedo", "She smiles when the candles move."),
                                                                  ("prefiere no hablar de ellos", "She talks about the grandfather's tastes."),
                                                                  ("cree que la celebración es solo para los niños", "She leads the preparations herself.")],
    "Le gustaba más picante; sonrió como quien recibe una visita.", "Attitude (1.B.3): she cooks to his taste and welcomes him like a guest.",
    ["Adds a chile for him; smiles as at an expected visit."])
Q.q("1.B.5 Word meaning", r"En el texto, «mija» es una forma",
    "cariñosa de decir «mi hija»", [("formal de llamar a una desconocida", "It is affectionate and informal."),
                                     ("de nombrar un ingrediente del mole", "It is a form of address."),
                                     ("de pedir silencio", "It is a form of address.")],
    "mija = mi hija (affectionate).", "Word meaning (1.B.5): the grandmother addresses her granddaughter.",
    ["mi + hija → mija."])
Q.q("1.C.2 Conclusion", r"¿Qué cambio se produce en la narradora al final del fragmento?",
    "Deja de dudar y acepta el sentido de la tradición.", [("Decide no participar nunca más en el altar.", "Nothing suggests that."),
                                                          ("Empieza a tener miedo de las velas.", "She stops asking; there is no fear."),
                                                          ("Se enoja con su abuela.", "No conflict.")],
    "Yo dejé de preguntar.", "Conclusions (1.C.2): at the start she does not understand; at the end she stops questioning.",
    ["Yo no entendía… → Yo dejé de preguntar."])

Q.sec("Reading: Article")
Q.src(r"Reading 2 \textperiodcentered\ Article \textperiodcentered\ «¿Hablas spanglish?», revista Puentes", [
    r"«Voy a parquear el carro y te llamo pa'trás». Para muchos jóvenes de Miami o Los Ángeles, esta frase es completamente normal. Para otros hablantes, suena incorrecta. ¿Quién tiene razón?",
    r"La lingüista Ana Celia Zentella, que estudió durante años a familias puertorriqueñas en Nueva York, explica que alternar el inglés y el español no es una señal de que la persona no domine ninguna de las dos lenguas. Al contrario, cambiar de lengua en el momento justo exige conocer bien las reglas de ambas.",
    r"Otros expertos advierten que algunas expresiones, como «llamar para atrás» (calco de \emph{call back}), pueden confundir a hispanohablantes de otros países. Por eso recomiendan que los jóvenes bilingües aprendan también el español general, sin avergonzarse de su forma de hablar en casa.",
    r"Más de cuarenta millones de personas hablan español en casa en Estados Unidos. El spanglish, guste o no, forma parte de la identidad de muchas de ellas.",
], 5)
Q.q("1.B.1 Purpose", r"¿Cuál es el propósito del artículo?",
    "presentar diferentes opiniones sobre el spanglish", [("prohibir el spanglish en las escuelas", "No one proposes a ban."),
                                                         ("enseñar a hablar spanglish", "It discusses it; it does not teach it."),
                                                         ("contar la historia de Puerto Rico", "Puerto Rican families are one detail.")],
    "¿Quién tiene razón? + two views.", "Purpose (1.B.1): the article asks a question and presents the linguist's view and the other experts' view.",
    ["Opening question → paragraph 2 (defense) → paragraph 3 (caution)."])
Q.q("1.A.1 Detail", r"Según Ana Celia Zentella, alternar las dos lenguas",
    "requiere conocer bien las reglas de ambas", [("demuestra que la persona no domina ninguna", "She says the opposite."),
                                                ("solo ocurre en Puerto Rico", "She studied families in New York."),
                                                ("es un fenómeno nuevo de las redes sociales", "Not stated.")],
    "exige conocer bien las reglas de ambas.", "Detail (1.A.1): al contrario introduces her actual claim.",
    ["Al contrario, … exige conocer bien las reglas de ambas."])
Q.q("1.B.5 Word meaning", r"En el artículo, la palabra «calco» se refiere a",
    "una expresión traducida palabra por palabra de otra lengua", [("una palabra de origen indígena", "Unrelated."),
                                                                  ("un error de pronunciación", "It is about meaning, not sound."),
                                                                  ("una palabra muy antigua", "Unrelated.")],
    "calco = loan translation.", "Word meaning (1.B.5): llamar para atrás copies call back word for word.",
    ["llamar para atrás ← call back."])
Q.q("1.B.3 Point of view", r"¿Qué recomiendan los «otros expertos»?",
    "aprender también el español general sin avergonzarse del habla de casa", [("dejar de hablar spanglish en casa", "They say not to be ashamed of it."),
                                                                                  ("hablar solo inglés en Estados Unidos", "Not stated."),
                                                                                  ("inventar nuevas expresiones", "Not stated.")],
    "Recomiendan… sin avergonzarse.", "Point of view (1.B.3): the recommendation keeps both varieties.",
    ["recomiendan que… aprendan también el español general, sin avergonzarse…"])
Q.q("1.C.2 Conclusion", r"¿Qué conclusión se puede sacar del último párrafo?",
    "El spanglish está ligado a la identidad de muchos hispanohablantes en EE. UU.", [("Pocas personas hablan español en Estados Unidos.", "More than forty million do."),
                                                                                    ("El spanglish desaparecerá pronto.", "Not stated."),
                                                                                    ("Todos los expertos aprueban el spanglish.", "Paragraph 3 shows they do not.")],
    "forma parte de la identidad.", "Conclusions (1.C.2): the last paragraph ties the numbers to identity.",
    ["guste o no, forma parte de la identidad…"])

Q.sec("Listening: Audio and Chart")
Q.src(r"Listening 2 \textperiodcentered\ Audio and Chart (transcript) \textperiodcentered\ «Las fiestas que más nos importan», Radio Universidad", [
    r"(LOCUTOR) La Universidad de Guadalajara preguntó a 2.000 jóvenes mexicanos de entre 15 y 24 años qué celebraciones consideran más importantes. Los resultados sorprenden.",
    r"(LOCUTOR) La Navidad sigue en primer lugar, pero el Día de Muertos ha subido mucho: hace diez años estaba en cuarto lugar y hoy está en segundo. Los investigadores creen que películas como \emph{Coco} y el desfile de la Ciudad de México, que empezó en 2016, han renovado el interés de los jóvenes.",
    r"(LOCUTOR) En cambio, el Día de la Independencia ha bajado. Muchos jóvenes dicen que lo celebran más por la fiesta que por el significado histórico.",
], 5, table=(["Celebración", "2014", "2024"], [["Navidad", "1.º", "1.º"], ["Día de Muertos", "4.º", "2.º"], ["Día de la Independencia", "2.º", "3.º"], ["Día de Reyes", "3.º", "4.º"]]),
      note="Tabla: lugar de cada celebración entre las más importantes para los jóvenes (datos ficticios).")
Q.q("1.A.2 Data", r"¿Qué muestra la tabla sobre los cambios entre 2014 y 2024?",
    "El Día de la Independencia y el Día de Reyes bajaron una posición cada uno.", [("El Día de Muertos bajó dos posiciones.", "It rose two places, from 4th to 2nd."),
                                                                                    ("La Navidad bajó una posición.", "It stayed 1st."),
                                                                                    ("Solo el Día de Reyes bajó, dos posiciones.", "Reyes fell one place (3rd to 4th), and Independencia also fell.")],
    "Independencia 2→3, Reyes 3→4.", "Data (1.A.2): compare each row's two columns.",
    ["Two celebrations each fell one place."])
Q.q("1.C.1 Connect", r"¿Qué explicación da el informe para el cambio del Día de Muertos que muestra la tabla?",
    "el efecto de películas como Coco y del nuevo desfile", [("un cambio en la fecha de la celebración", "The date did not change."),
                                                            ("una ley que obligó a celebrarlo", "Not mentioned."),
                                                            ("la disminución del turismo", "Not mentioned.")],
    "Coco + desfile desde 2016.", "Connect (1.C.1): the table shows the rise; the audio explains it.",
    ["Table: 4th → 2nd.", "Audio: películas como Coco y el desfile."])
Q.q("1.A.1 Detail", r"¿Desde cuándo existe el desfile de Día de Muertos en la Ciudad de México?",
    "desde 2016", [("desde hace un siglo", "It is recent."),
                   ("desde 2024", "2024 is the survey year."),
                   ("desde 2014", "2014 is the earlier survey year.")],
    "El desfile empezó en 2016.", "Detail (1.A.1): keep the dates apart (survey years vs. the parade).",
    ["que empezó en 2016."])
Q.q("1.C.3 Inference", r"¿Qué se puede inferir sobre la actitud de muchos jóvenes hacia el Día de la Independencia?",
    "Lo disfrutan como fiesta, pero le dan menos importancia a su historia.", [("No lo celebran de ninguna manera.", "They celebrate it, for the party."),
                                                                              ("Es su celebración favorita.", "It is third."),
                                                                              ("Lo consideran más importante que la Navidad.", "Navidad is first.")],
    "Más por la fiesta que por el significado.", "Inference (1.C.3) from the stated reason.",
    ["lo celebran más por la fiesta que por el significado histórico."])
Q.q("1.B.1 Main idea", r"¿Cuál es la idea central del informe?",
    "Las preferencias de los jóvenes por las celebraciones han cambiado en diez años.", [("Los jóvenes ya no celebran ninguna fiesta.", "They rank several."),
                                                                                       ("El Día de Reyes es la fiesta más importante.", "It is fourth."),
                                                                                       ("Las películas no influyen en las tradiciones.", "The researchers say they do.")],
    "Change over ten years.", "Main idea (1.B.1): the report compares two years and explains the changes.",
    ["2014 vs. 2024 + explanations."])

Q.frq(kind="Project Q&A", head=r"Question 2 \textperiodcentered\ Project Q\&A (practice) \textperiodcentered\ 9 points \textperiodcentered\ 4 answers of 40 seconds", mins=8,
      directions=[r"Imagine that your project examined how music expresses identity in a Spanish-speaking community, and that your presentation focused on Paraguayan music sung in Guaraní (the polca paraguaya and the guarania). You will hear four questions. Each is played twice; you have 40 seconds to answer each one. Answer in Spanish."],
      prompt=[r"1. En tu presentación hablaste de la guarania. ¿Por qué es importante que muchas canciones se canten en guaraní?",
              r"2. ¿Puedes dar un ejemplo concreto de cómo se usa esta música en la vida de las familias?",
              r"3. ¿Hay alguna música en tu comunidad que cumpla una función parecida? Compárala.",
              r"4. ¿Qué fue lo más sorprendente que aprendiste en tu investigación?"],
      model=[r"\textbf{1.} Es importante porque el guaraní es la lengua del hogar para la mayoría de los paraguayos. Cuando un compositor como José Asunción Flores creó la guarania, eligió una lengua que antes estaba mal vista en la escuela. Cantar en guaraní muestra orgullo por una identidad mestiza y bilingüe; por eso estas canciones se sienten tan cercanas.",
             r"\textbf{2.} Sí. En las fiestas familiares, por ejemplo en un cumpleaños o en las fiestas patronales del pueblo, es común que alguien toque el arpa paraguaya y que todos canten juntos. La música no es un espectáculo: es una forma de reunir a la familia.",
             r"\textbf{3.} En mi comunidad mexicoamericana, las rancheras cumplen una función parecida. Igual que la guarania, se cantan en las reuniones familiares y recuerdan de dónde viene la familia. La diferencia es la lengua: en Paraguay se celebra una lengua indígena, mientras que nosotros celebramos el español frente al inglés.",
             r"\textbf{4.} Lo que más me sorprendió fue que hoy hay grupos de rock y de rap que cantan en guaraní. Pensaba que era una lengua solo de los abuelos, pero los jóvenes la usan para expresarse, lo cual demuestra que una tradición puede renovarse."],
      rows=[("A Task", 2, "four relevant, complete answers that address each question", "answers that drift back to the presentation or stop after one sentence"),
            ("B Culture", 2, "in at least one answer, a cultural comparison (answer 3) or a perspective linked to a product or practice (answers 1 and 2)", "only describing the songs (1 point)"),
            ("C Language", 3, "varied vocabulary and structures (passive se, subjunctive, relative clauses)", "short, repetitive sentences"),
            ("D Fluency", 2, "natural pace and intonation, clear pronunciation, few pauses", "long silences, many restarts")],
      tips=["Each answer starts by answering the question directly.", "Answer 3 is a full cultural comparison: similarity, difference, and why.",
            "Answer 1 links a product (songs in Guaraní) to a perspective (pride in a bilingual identity).", "About 70–80 words each fits 40 seconds."],
      ask="Answer each question aloud in Spanish (40 seconds each), jotting keywords first; then mark your answers.", lines=12)

GUIDE, QSET = G, Q
