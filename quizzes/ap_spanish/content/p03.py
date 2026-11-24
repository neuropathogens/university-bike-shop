from ap_wl.model import Doc

STEM = "03-art-creativity"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 3: Art and Creativity", r"Unit 3 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 3 asks how art expresses identity and values, and how traditions are preserved and reinvented. Its recommended contexts are artistic heritage, architecture, beauty and aesthetics, fashion and design, literature, and the visual and performing arts. Music is the lens of the 2026--27 course project, so this guide gives it the most space: genres and instruments, what they express, and how they change. It also covers architecture, painting and literature, the language for describing and evaluating art, and a Project Presentation kit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 11+ \qquad Three factors for my project: \blank[10em]",
        short="Unit 3", sub="Art and Creativity")

G.sec("Music: genres, instruments and what they express")
G.tex(r"""
\begin{vocab}
el género musical / el ritmo & genre / rhythm & \\
la letra / el estribillo & lyrics / chorus & \emph{letra} also means letter of the alphabet \\
el bandoneón & accordion-like instrument of the tango & German origin, adopted in Buenos Aires \\
el charango / la quena & small Andean string instrument / Andean flute & \\
el cajón & box drum from Afro-Peruvian music & declared Peruvian national heritage in 2001 \\
el güiro / las maracas & scraper / shakers & Caribbean and Indigenous roots \\
la fusión & mixing genres & \emph{fusión de flamenco y pop} \\
componer / interpretar / grabar & compose / perform / record & \\
\end{vocab}

\begin{compare}{Genre}{Origin}{What it often expresses}
Tango & Buenos Aires and Montevideo, late 19th c.; UNESCO 2009 & nostalgia, immigrant life, love and loss \\
Flamenco & Andalusia, Romani and other roots; UNESCO 2010 & deep emotion (\emph{duende}), identity of a marginalized people \\
Mariachi & western Mexico; UNESCO 2011 & family celebrations, regional and national pride \\
Cumbia & Colombian Caribbean coast; spread across Latin America & Indigenous, African and Spanish roots; dancing together \\
Salsa & Cuban son, developed in New York in the 1960s--70s & Latino identity in the U.S., the barrio \\
Reguetón & Panama and Puerto Rico, 1990s & urban youth culture; now global \\
\end{compare}

\begin{keyidea}[Products, practices, perspectives in music]
\textbf{Product}: a song, an instrument, a genre. \textbf{Practice}: dancing tango at a \emph{milonga}, hiring mariachis for a birthday, singing in Guaraní at a family party. \textbf{Perspective}: the value behind it (family, memory, pride in mixed roots, resistance). The presentation's culture row asks for the link: practice + \emph{porque} + perspective.
\end{keyidea}
""")
G.q("1 Música", r"El cajón, el instrumento de percusión con forma de caja, es asociado sobre todo con la música",
    "afroperuana", [("andina de Bolivia", "Andean music uses the charango and the quena."),
                    ("del tango argentino", "Tango's emblematic instrument is the bandoneón."),
                    ("mariachi mexicana", "Mariachi uses violins, trumpets and guitars.")],
    "Cajón = Afro-Peruvian box drum.", "The cajón developed in Afro-Peruvian communities and is now heard in flamenco and pop.",
    ["cajón → Peru, Afro-Peruvian music."])
G.q("1 Música", r"Which sentence links a musical practice to a cultural perspective?",
    "En Buenos Aires se baila tango en las milongas de barrio porque la gente valora encontrarse y conservar la memoria de los inmigrantes.",
    [("El tango usa un instrumento llamado bandoneón.", "This names a product with no perspective."),
     ("El tango es un género musical de Argentina y Uruguay.", "A fact about origin, no practice or perspective."),
     ("Me encanta escuchar tango los domingos.", "A personal preference, not a cultural example.")],
    "Practice + porque + perspective.", "The top culture score needs a specific practice or product tied to the value behind it.",
    ["Practice: dancing tango at neighborhood milongas.", "Perspective: valuing meeting together and immigrant memory."])
G.q("1 Música", r"Salsa took shape in which setting?",
    "Latino communities in New York, from Cuban and Caribbean music", [("the royal court of Spain", "Salsa is a 20th-century popular music."),
                                                                      ("Andean villages of Peru", "That is the setting of huayno and other Andean music."),
                                                                      ("the Argentine pampas", "That is the setting of folk music such as the chacarera.")],
    "Salsa: Cuban son + New York barrio.", "Salsa developed in New York in the 1960s–70s from Cuban son and other Caribbean genres.",
    ["Caribbean roots, New York Latino community."])

G.sec("Artistic heritage and architecture")
G.tex(r"""
\begin{vocab}
el patrimonio artístico & artistic heritage & \\
la obra maestra & masterpiece & \\
el mural / el muralismo & mural / muralism & Mexico after the Revolution \\
el estilo mudéjar & Christian architecture with Islamic decoration & Spain, 12th--16th c. \\
la fachada / la cúpula / el azulejo & façade / dome / glazed tile & \\
restaurar / conservar & restore / preserve & \\
\end{vocab}

\begin{compare}{Work or place}{What it is}{Why it matters}
La Alhambra (Granada) & Nasrid palace and fortress, 13th--14th c. & Islamic heritage of Spain \\
La Sagrada Familia (Barcelona) & Gaudí's basilica, begun 1882, still being built & modernisme; nature as a model \\
Murales de Diego Rivera (Mexico) & public murals of history and work & art for everyone, national identity \\
Machu Picchu (Peru) & 15th-century Inca citadel & Inca engineering and heritage \\
\end{compare}

\textbf{Muralism.} After the Mexican Revolution, the government commissioned murals on public buildings so that people who could not read could see their history. The perspective: art belongs to the people, not only to museums.
""")
G.q("2 Patrimonio", r"¿Por qué el gobierno mexicano encargó murales en edificios públicos después de la Revolución?",
    "para que el pueblo, incluso quienes no sabían leer, conociera su historia", [("para decorar las casas de los ricos", "The murals were on public buildings."),
                                                                                  ("para vender las obras en el extranjero", "Murals are painted on walls and are not sold."),
                                                                                  ("para reemplazar las escuelas", "They complemented education; they did not replace schools.")],
    "Muralism: art for the people.", "Muralism (Rivera, Orozco, Siqueiros) put history on public walls, reflecting the view that art belongs to everyone.",
    ["Public walls + history → education and identity."])
G.q("2 Patrimonio", r"The Alhambra in Granada is an example of",
    "the Islamic heritage of Spain", [("Inca architecture", "Inca architecture is in the Andes (Machu Picchu)."),
                                      ("Gaudí's modernisme", "Gaudí worked in Barcelona, centuries later."),
                                      ("Mexican muralism", "Muralism is 20th-century Mexican painting.")],
    "Alhambra = Nasrid (Islamic) palace.", "The Alhambra was built by the Nasrid dynasty, the last Muslim kingdom in Iberia (until 1492).",
    ["Granada, 13th–14th c., Nasrid → Islamic heritage."])

G.sec("Visual arts and literature")
G.tex(r"""
\begin{compare}{Artist or writer}{Known for}{Theme}
Frida Kahlo (Mexico) & self-portraits & pain, identity, Mexican Indigenous dress \\
Pablo Picasso, \emph{Guernica} (1937) & painting of the bombing of Guernica & the horror of war \\
Fernando Botero (Colombia) & enlarged, rounded figures & humor, critique of power \\
Gabriel García Márquez & \emph{Cien años de soledad} (1967), magical realism; Nobel 1982 & Latin American history and family \\
Gabriela Mistral (Chile) & poetry; first Latin American Nobel in literature (1945) & childhood, motherhood, teaching \\
Miguel de Cervantes & \emph{Don Quijote} (1605, 1615) & ideals versus reality \\
\end{compare}

\textbf{Magical realism} presents extraordinary events (a woman who rises to heaven while folding sheets) in a matter-of-fact tone, as part of everyday life.
""")
G.q("3 Artes", r"Un texto describe una pintura de 1937 sobre el bombardeo de un pueblo vasco. ¿Qué obra es?",
    "el Guernica de Picasso", [("La persistencia de la memoria de Dalí", "Dalí's 1931 painting of melting clocks."),
                               ("un autorretrato de Frida Kahlo", "Kahlo painted herself, not this bombing."),
                               ("un mural de Diego Rivera", "Rivera's murals show Mexican history.")],
    "Guernica, 1937.", "Picasso painted Guernica in 1937 after the bombing of the Basque town during the Spanish Civil War.",
    ["1937 + Basque town bombing → Guernica."])
G.q("3 Artes", r"In magical realism, extraordinary events are typically",
    "told in a matter-of-fact tone, as part of everyday life", [("explained as dreams at the end", "They are not explained away."),
                                                              ("limited to fairy tales for children", "Magical realism is literary fiction for adults."),
                                                              ("presented as science fiction in the future", "It is set in ordinary, often historical, life.")],
    "Ordinary tone, extraordinary events.", "Magical realism (García Márquez) treats the marvelous as normal.",
    ["Matter-of-fact tone is the defining trait."])

G.sec("Describing and evaluating art")
G.tex(r"""
\begin{compare}{Purpose}{Language}{Example}
Describe & representa, muestra, se ve(n), en primer plano / al fondo & En primer plano se ve a una mujer con un rebozo. \\
Interpret & refleja, simboliza, expresa, transmite & El color rojo simboliza la pasión y la violencia. \\
Evaluate & me parece que, lo que más destaca es, lo + adjective & Lo interesante es cómo mezcla lo antiguo y lo moderno. \\
Concede & aunque + subjunctive, si bien & Aunque algunos lo consideren comercial, el reguetón refleja la vida urbana. \\
Influence & influir en, inspirarse en, tener sus raíces en & La salsa tiene sus raíces en el son cubano. \\
\end{compare}

\begin{trap}
\emph{Lo + adjective} names an idea: \emph{lo bello} (what is beautiful), \emph{lo importante} (the important thing). \emph{Lo} does not change for gender or number.
\end{trap}
""")
G.q("4 Describir", r"Elige la forma correcta: Es posible que algunos críticos \blank\ que el reguetón es solo comercial, pero muchos jóvenes lo ven como una forma de expresión.",
    "digan", [("dicen", "Es posible que expresses possibility, which requires the subjunctive."),
              ("dirán", "The future indicative cannot follow es posible que."),
              ("decir", "With a subject (algunos críticos), a conjugated verb is needed after que.")],
    "Es posible que + subjunctive.", "Expressions of possibility and doubt (es posible que, puede que, quizás) take the subjunctive; this is how you concede a view without asserting it.",
    ["es posible que → digan."])
G.q("4 Describir", r"Elige la mejor opción: \blank\ más me impresionó del museo fueron los colores de los murales.",
    "Lo que", [("El que", "El que refers to a specific masculine noun."),
               ("Que", "A sentence-initial noun clause needs lo que."),
               ("Cual", "Cual alone cannot introduce this clause.")],
    "Lo que = what.", "Lo que introduces an idea with no specific antecedent.",
    ["what impressed me most → lo que."])

G.sec("Task kit: the Project Presentation")
G.tex(r"""
You have 3 minutes to prepare (with your PPR) and 3 minutes to present, about 350--400 words. The prompt asks what you learned in your research; the rubric rewards \textbf{three or more factors, each explained with details}, and a cultural perspective linked to a product or practice.

\begin{terms}
0:00--0:25 & introduction: the question, your focus, the three factors \\
0:25--2:30 & three factors, about 40 seconds each: fact or example from research + why it matters (perspective) \\
2:30--3:00 & conclusion: what the factors show together; a comparison or reflection \\
\end{terms}

\begin{compare}{Move}{Phrases}{}
Open & Hoy voy a hablar de\ldots; Me enfoqué en tres aspectos: \ldots & \\
Move on & En primer lugar / En segundo lugar / Por último & \\
Evidence & Según lo que investigué, \ldots; Por ejemplo, \ldots & \\
Perspective & Esto refleja\ldots; lo que demuestra la importancia de\ldots & \\
Close & En conclusión, \ldots; Lo que aprendí es que\ldots & \\
\end{compare}

\begin{trap}
Three factors named with no detail earn only 1 point for task; so does one factor explained in depth. Budget time so the third factor gets real detail.
\end{trap}
""")
G.q("5 Presentación", r"A presentation explains three factors, each with a specific example from research, but never links them to what people value. Which row is it most likely to lose points in?",
    "Cultural understanding", [("Task execution", "Three factors with relevant details earn full task credit."),
                               ("Delivery", "Delivery is about pronunciation and pace."),
                               ("Organization", "Nothing suggests poor organization.")],
    "No perspective link → culture row.", "Row B's top score needs a relationship between a perspective and a product or practice.",
    ["Factors and details → task OK.", "No perspective → culture 1 point."])
G.q("5 Presentación", r"About how many words fit in the 3-minute presentation at a natural pace?",
    "350 to 400", [("100 to 150", "That would leave long silences."),
                   ("800 to 900", "That would require rushing, which hurts delivery."),
                   ("50", "That is one short paragraph.")],
    "3 min ≈ 350–400 words.", "At about two words per second, three minutes holds 350–400 words.",
    ["Plan about 120 words per factor."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 3: Art and Creativity: Question Set", r"Unit 3 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Instructional Guidance and an Interview for listening, an Article and Chart and a Promotional Material for reading) on music, festivals and artistic tradition, followed by a practice Project Presentation on music, the 2026--27 project lens, with the 11-point scoring guide and a model script. The presentation prompt is a practice prompt written for this set, not the official 2027 project prompt. As on the exam, questions and choices are in Spanish; listening sources are printed as transcripts. All sources and data are original and fictional. Allow about 25 minutes for the multiple choice and 6 minutes to prepare and deliver the presentation.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Presentation: \blank\ / 11 \qquad Target: 15+ MCQ and 8+ presentation",
        short="Unit 3", sub="Art and Creativity")

Q.sec("Listening: Instructional Guidance")
Q.src(r"Listening 1 \textperiodcentered\ Instructional Guidance (transcript) \textperiodcentered\ «Tu primera clase de cajón», un videotutorial", [
    r"(PROFESOR) ¡Hola! Hoy vas a aprender el ritmo básico del cajón peruano. Primero, siéntate sobre el cajón, con la espalda recta y los pies bien apoyados en el suelo. Inclina el cajón un poco hacia atrás.",
    r"(PROFESOR) Ahora, fíjate en las dos zonas de la tapa. Si golpeas en el centro con la palma de la mano, obtienes un sonido grave, el «bajo». Si golpeas cerca del borde superior con los dedos, obtienes un sonido agudo y seco.",
    r"(PROFESOR) Empieza despacio: bajo, agudo, agudo; bajo, agudo, agudo. No te preocupes por la velocidad. Lo importante es que el ritmo sea constante.",
    r"(PROFESOR) Un último consejo: el cajón nació en las comunidades afroperuanas cuando no tenían otros tambores. Cuando toques, recuerda que estás continuando esa historia.",
], 5)
Q.q("1.A.1 Detail", r"¿Qué es lo primero que hay que hacer, según el profesor?",
    "sentarse sobre el cajón con la espalda recta", [("golpear el centro de la tapa", "That comes after sitting correctly."),
                                                   ("tocar el ritmo rápidamente", "He says to start slowly."),
                                                   ("escuchar música afroperuana", "Not one of the steps.")],
    "Primero, siéntate…", "Instructional Guidance: primero marks the first step.",
    ["Primero, siéntate sobre el cajón…"])
Q.q("1.A.1 Detail", r"¿Cómo se obtiene el sonido grave?",
    "golpeando el centro de la tapa con la palma", [("golpeando el borde con los dedos", "That gives the high, dry sound."),
                                                   ("inclinando el cajón hacia adelante", "He says to tilt it back."),
                                                   ("golpeando el suelo con los pies", "The feet stay flat on the floor.")],
    "Centro + palma = bajo.", "Detail (1.A.1): match each zone with its sound.",
    ["en el centro con la palma de la mano → grave."])
Q.q("1.B.3 Point of view", r"Según el profesor, ¿qué es lo más importante al principio?",
    "mantener un ritmo constante", [("tocar muy rápido", "No te preocupes por la velocidad."),
                                   ("tocar muy fuerte", "Not mentioned."),
                                   ("improvisar ritmos nuevos", "He gives one basic pattern.")],
    "Lo importante es que el ritmo sea constante.", "Lo importante es… signals the speaker's priority.",
    ["Lo importante es que el ritmo sea constante."])
Q.q("1.B.4 Organization", r"¿Cómo está organizado el tutorial?",
    "en pasos ordenados, de la postura al ritmo, con un consejo final", [("como una comparación entre dos instrumentos", "Only the cajón is discussed."),
                                                                     ("como una historia del cajón desde el principio", "History appears only in the last tip."),
                                                                     ("como una lista de preguntas y respuestas", "There is no Q&A.")],
    "Primero… Ahora… Empieza… Un último consejo.", "Organization (1.B.4): sequence markers order the steps.",
    ["posture → zones → rhythm → tip."])
Q.q("1.C.3 Inference", r"¿Qué quiere transmitir el profesor con su último consejo?",
    "que tocar el cajón conecta al estudiante con la historia afroperuana", [("que el cajón es un instrumento moderno", "He says it was born in Afro-Peruvian communities long ago."),
                                                                              ("que solo los peruanos pueden tocarlo", "He invites everyone to continue the history."),
                                                                              ("que es mejor comprar otro tambor", "The opposite.")],
    "estás continuando esa historia.", "Inference (1.C.3): the closing remark gives the practice a cultural meaning.",
    ["Origin story + you continue it → connection to heritage."])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 1 \textperiodcentered\ Article and Chart \textperiodcentered\ «¿Qué escucha la generación Z?», diario El Puente", [
    r"Un estudio de una plataforma de \emph{streaming} sobre 50.000 usuarios de entre 16 y 24 años en América Latina confirma lo que muchos padres ya sospechaban: el reguetón domina los auriculares de los jóvenes.",
    r"Sin embargo, el estudio esconde una sorpresa. Las listas de música tradicional, como la cumbia o el folclore andino, crecieron más que cualquier otro género en el último año, aunque todavía representan una parte pequeña del total. «Los jóvenes descubren estas canciones a través de fusiones», explica la musicóloga Inés Paredes. «Un rapero sampleó una quena y, de repente, miles de chicos buscan quién es la intérprete original».",
    r"Para Paredes, la tradición no desaparece: cambia de forma. «Cada generación escucha a sus abuelos a su manera».",
], 5, table=(["Género", "Parte del tiempo de escucha", "Crecimiento en un año"],
             [["Reguetón y urbano", "46 \\%", "+4 \\%"], ["Pop", "27 \\%", "−2 \\%"], ["Rock", "12 \\%", "−5 \\%"], ["Cumbia y folclore", "6 \\%", "+31 \\%"]]),
      note="Datos ficticios.")
Q.q("1.A.2 Data", r"Según la tabla, ¿qué género ocupa la mayor parte del tiempo de escucha?",
    "el reguetón y la música urbana", [("la cumbia y el folclore", "They grew most but are only 6%."),
                                       ("el pop", "Pop is 27%."),
                                       ("el rock", "Rock is 12%.")],
    "46%.", "Data (1.A.2): read the right column (share, not growth).",
    ["Share column → 46% reggaeton/urban."])
Q.q("1.C.1 Connect", r"¿Qué dato de la tabla corresponde a la «sorpresa» que menciona el artículo?",
    "el crecimiento del 31 \\% de la cumbia y el folclore", [("el 46 \\% del reguetón", "That confirms what parents suspected, not the surprise."),
                                                              ("la bajada del 5 \\% del rock", "The article does not discuss rock."),
                                                              ("el 27 \\% del pop", "Not discussed.")],
    "Sorpresa = traditional music grew most.", "Connect (1.C.1): match sin embargo… sorpresa to the +31% growth figure.",
    ["crecieron más que cualquier otro género → +31%."])
Q.q("1.B.5 Word meaning", r"En el artículo, «sampleó» significa que el rapero",
    "usó un fragmento grabado de una quena en su canción", [("aprendió a tocar la quena", "He used a recording."),
                                                          ("criticó la música andina", "No criticism."),
                                                          ("vendió una quena antigua", "Unrelated.")],
    "samplear = use a recorded fragment.", "Word meaning (1.B.5): the context (fusiones, intérprete original) shows reuse of a recording.",
    ["fusiones + buscan la intérprete original → a sample."])
Q.q("1.B.3 Point of view", r"¿Cuál es la opinión de Inés Paredes?",
    "La tradición musical no desaparece, sino que se transforma.", [("Los jóvenes ya no se interesan por la música tradicional.", "She says they discover it through fusions."),
                                                                     ("El reguetón destruye la cultura latinoamericana.", "She never says so."),
                                                                     ("Las fusiones son una falta de respeto.", "She describes them as a way in.")],
    "No desaparece: cambia de forma.", "Point of view (1.B.3): her final quote states her view.",
    ["la tradición no desaparece: cambia de forma."])
Q.q("1.C.2 Conclusion", r"¿Qué conclusión apoya mejor el artículo?",
    "Las fusiones pueden acercar a los jóvenes a la música de sus abuelos.", [("La cumbia superará al reguetón el próximo año.", "6% versus 46%: not supported."),
                                                                              ("El pop está creciendo más que nunca.", "Pop fell 2%."),
                                                                              ("Los jóvenes escuchan solo música tradicional.", "Traditional music is 6%.")],
    "Fusion → discovery.", "Conclusions (1.C.2) must stay within the evidence: the article shows discovery through fusion, not a takeover.",
    ["Example: a rapper's sample led listeners to the original artist."])

Q.sec("Reading: Promotional Material")
Q.src(r"Reading 2 \textperiodcentered\ Promotional Material \textperiodcentered\ Un cartel de festival", [
    r"\textbf{FESTIVAL RAÍCES 2027 \textperiodcentered\ Música que viene de lejos}",
    r"Tres días, cuatro escenarios y más de cuarenta artistas de diez países. Del son jarocho al tango, de la bomba puertorriqueña al rap en quechua. ¡La tradición también se baila!",
    r"\textbf{Novedad este año:} talleres gratuitos de jarana, cajón y zapateado con los propios músicos. Inscripción en la carpa de bienvenida (cupos limitados, por orden de llegada).",
    r"\textbf{Entradas:} abono de tres días, 60 dólares; menores de 12 años, gratis. Estudiantes con credencial: 50 \% de descuento.",
    r"Del 7 al 9 de mayo \textperiodcentered\ Parque Central \textperiodcentered\ Prohibido entrar con bebidas de vidrio.",
], 5)
Q.q("1.B.1 Purpose", r"¿Cuál es el propósito principal del cartel?",
    "invitar al público a un festival de música tradicional y de fusión", [("anunciar la apertura de una escuela de música", "Workshops are one feature of a festival."),
                                                                         ("vender instrumentos musicales", "Nothing is sold except tickets."),
                                                                         ("informar sobre un concurso de baile", "No contest is mentioned.")],
    "Festival poster → invite.", "Purpose (1.B.1): the title, dates, place and ticket prices invite people to attend.",
    ["Promotional Material → invitation to an event."])
Q.q("1.A.1 Detail", r"¿Cómo se puede participar en los talleres?",
    "inscribiéndose en la carpa de bienvenida del festival", [("comprando una entrada especial por internet", "The workshops are free; registration is at the tent."),
                                                             ("llevando su propio instrumento", "Not stated."),
                                                             ("enviando un video previo", "Not stated.")],
    "Inscripción en la carpa de bienvenida.", "Detail (1.A.1) from the Novedad paragraph.",
    ["Inscripción en la carpa de bienvenida."])
Q.q("1.C.2 Conclusion", r"Una estudiante universitaria con credencial compra un abono. ¿Cuánto paga?",
    "30 dólares", [("60 dólares", "Students get 50% off."),
                   ("nada", "Only children under 12 enter free."),
                   ("50 dólares", "50 is the discount percentage, not the price.")],
    "$60 − 50% = $30.", "Apply the details: the three-day pass costs 60 dollars, and students pay half.",
    ["60 × 0.5 = 30."])
Q.q("1.B.3 Tone", r"¿Qué sugiere la frase «¡La tradición también se baila!»?",
    "que la música tradicional puede ser alegre y participativa", [("que solo los expertos pueden bailar", "The tone is inclusive."),
                                                                   ("que el festival es un concurso de baile", "No contest is mentioned."),
                                                                   ("que la tradición es aburrida", "The opposite: it contradicts that stereotype.")],
    "Tradition is lively, for everyone.", "Tone and implied meaning: también answers the stereotype that tradition is only for listening or for the old.",
    ["también → contrary to expectation, it is danceable."])
Q.q("1.A.1 Detail", r"¿Qué está prohibido en el festival?",
    "entrar con bebidas en envases de vidrio", [("entrar con menores de 12 años", "Children under 12 enter free."),
                                               ("bailar frente a los escenarios", "Dancing is encouraged."),
                                               ("sacar fotos", "Not mentioned.")],
    "Prohibido… vidrio.", "Detail (1.A.1) from the last line.",
    ["Prohibido entrar con bebidas de vidrio."])

Q.sec("Listening: Interview")
Q.src(r"Listening 2 \textperiodcentered\ Interview (transcript) \textperiodcentered\ Una bailaora joven de flamenco", [
    r"(ENTREVISTADORA) Lucía, tienes 23 años y ya bailas en los teatros más importantes de Sevilla. ¿Cómo empezó todo?",
    r"(LUCÍA) En la cocina de mi abuela. Ella cantaba mientras cocinaba y yo zapateaba sobre las baldosas. Nadie me enseñó formalmente hasta los doce años; el flamenco se aprendía en casa, en las fiestas, escuchando.",
    r"(ENTREVISTADORA) Ahora mezclas el flamenco con música electrónica. ¿Qué dicen los puristas?",
    r"(LUCÍA) Algunos dicen que es una traición. Yo los respeto, pero no estoy de acuerdo. El flamenco siempre ha mezclado: tiene raíces gitanas, árabes, judías, andaluzas. Si no cambiara, ya estaría muerto.",
    r"(ENTREVISTADORA) ¿Qué es lo que nunca cambiarías?",
    r"(LUCÍA) El duende, esa emoción profunda que sale de dentro. Con cajón o con sintetizador, si no hay duende, no es flamenco.",
], 5)
Q.q("1.A.1 Detail", r"¿Dónde empezó Lucía a bailar?",
    "en la cocina de su abuela", [("en una academia a los cinco años", "No one taught her formally until age twelve."),
                                  ("en un teatro de Sevilla", "She dances there now."),
                                  ("en una discoteca", "Not mentioned.")],
    "En la cocina de mi abuela.", "Detail (1.A.1): her first answer.",
    ["En la cocina de mi abuela."])
Q.q("1.C.3 Inference", r"¿Qué se puede inferir sobre la forma tradicional de aprender flamenco?",
    "Se transmitía de manera informal, en la familia y en las fiestas.", [("Solo se aprendía en conservatorios.", "She says it was learned at home."),
                                                                         ("Era un arte prohibido para las mujeres.", "Not stated."),
                                                                         ("Se aprendía leyendo partituras.", "She says by listening.")],
    "se aprendía en casa, en las fiestas, escuchando.", "Inference (1.C.3): learning at home and at parties = informal family transmission.",
    ["en casa, en las fiestas, escuchando."])
Q.q("1.B.3 Attitude", r"¿Cuál es la actitud de Lucía hacia los puristas?",
    "Los respeta, aunque no comparte su opinión.", [("Los desprecia.", "She says she respects them."),
                                                   ("Está totalmente de acuerdo con ellos.", "No estoy de acuerdo."),
                                                   ("Nunca ha oído sus críticas.", "She quotes their criticism.")],
    "Los respeto, pero no estoy de acuerdo.", "Attitude (1.B.3): respectful disagreement.",
    ["Yo los respeto, pero no estoy de acuerdo."])
Q.q("1.B.4 Organization", r"¿Qué argumento usa Lucía para defender la fusión?",
    "que el flamenco siempre ha mezclado influencias diferentes", [("que la música electrónica es más popular", "She does not argue from popularity."),
                                                                   ("que los puristas no saben bailar", "She does not attack them."),
                                                                   ("que el público joven lo exige", "Not stated.")],
    "Raíces gitanas, árabes, judías, andaluzas.", "She supports her view with history: mixing is part of flamenco's origin.",
    ["El flamenco siempre ha mezclado…"])
Q.q("1.B.5 Word meaning", r"Según Lucía, el «duende» es",
    "una emoción profunda que sale de dentro", [("un tipo de zapato para bailar", "She defines it as an emotion."),
                                               ("un instrumento electrónico", "No."),
                                               ("un baile de los gitanos", "No.")],
    "esa emoción profunda que sale de dentro.", "Definitions in the source answer word-meaning questions.",
    ["El duende, esa emoción profunda…"])

Q.frq(kind="Project Presentation", head=r"Question 1 \textperiodcentered\ Project Presentation (practice prompt) \textperiodcentered\ 11 points \textperiodcentered\ 3 + 3 minutes", mins=6,
      directions=[r"Imagine that your project examined how music reflects the values of a Spanish-speaking community. You have 3 minutes to prepare, using your notes, and 3 minutes to present. Explain at least three factors, with specific examples from your research, and show how cultural perspectives relate to cultural products or practices."],
      prompt=[r"Prompt: \textbf{¿De qué manera refleja la música los valores de una comunidad hispanohablante que investigaste?}",
              r"Practice focus (example): mariachi music in Mexican and Mexican American communities."],
      model=[r"Hoy voy a hablar de cómo la música de mariachi refleja los valores de las comunidades mexicanas y mexicoamericanas. Me enfoqué en tres aspectos: la familia, el orgullo regional y la manera en que se transmite la tradición.",
             r"En primer lugar, el mariachi está presente en los momentos más importantes de la familia. Según lo que investigué, es muy común contratar mariachis para cantar «Las mañanitas» en un cumpleaños, para una boda o incluso para despedir a un ser querido. Esta práctica refleja la importancia de celebrar juntos: la música en vivo convierte un evento privado en un acontecimiento compartido.",
             r"En segundo lugar, el mariachi expresa orgullo regional y nacional. Nació en el occidente de México, sobre todo en Jalisco, y en 2011 la UNESCO lo reconoció como patrimonio cultural inmaterial. El traje de charro y canciones como «Cielito lindo» son productos que muchas personas asocian con la identidad mexicana; por eso, cuando se cantan en el extranjero, recuerdan a los migrantes de dónde vienen.",
             r"Por último, la tradición se transmite de generación en generación. En varias ciudades de Estados Unidos existen escuelas de mariachi para jóvenes, y muchos músicos aprendieron de sus padres y abuelos. Esto demuestra que la comunidad valora conservar sus raíces, aunque viva en otro país y hable otro idioma en la escuela.",
             r"En conclusión, el mariachi no es solo un género musical: es una forma de unir a la familia, de mostrar orgullo por el origen y de pasar la cultura a los más jóvenes. Lo que más aprendí es que, para muchas familias, una canción puede ser un puente entre dos países."],
      rows=[("A Task", 2, "three or more factors, each explained with relevant details from research", "three factors named with no detail, or only one or two factors"),
            ("B Culture", 2, "specific examples linking perspectives (family, pride, roots) to products or practices", "examples with no perspective, or a vague one (1 point)"),
            ("C Organization", 2, "clear introduction, ordered factors, conclusion; varied transitions", "a list of facts with no progression"),
            ("D Language", 3, "wide vocabulary, varied structures, culturally relevant expressions", "a limited set of basic structures"),
            ("E Delivery", 2, "clear pronunciation, natural pace and intonation, little hesitation", "hesitant, monotone or rushed speech")],
      tips=["The introduction names the three factors, so the listener can follow.", "Each factor has a specific example (Las mañanitas, UNESCO 2011, mariachi schools) and a perspective (esto refleja, esto demuestra).",
            "The conclusion pulls the factors together and adds a reflection.", "About 380 words: three minutes at a natural pace."],
      ask="Prepare for 3 minutes using keywords only, then present aloud for 3 minutes (record yourself if you can). Then mark your presentation.", lines=14)

GUIDE, QSET = G, Q
