from ap_wl.model import Doc

STEM = "00-exam-playbook"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Part 0: The Revised Exam and the Task Playbook", r"Part 0 \textperiodcentered\ Study Guide",
        abstract=r"""This guide is written for the revised AP Spanish Language and Culture course (effective fall 2026) and its first exam, in May 2027, which runs entirely in Bluebook. It sets out what each of the three free-response questions and the nine multiple-choice task types asks you to do, how the free-response questions are scored, and the language that moves a response up a scoring row. Read it before the unit guides: every unit guide ends with a task kit that assumes the rubrics here. Sources: the College Board AP Spanish exam page and the Course and Exam Description (CED), effective fall 2026. Check AP Central for any later change.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 11+ \qquad Rubric rows I still mix up: \blank[10em]",
        short="Part 0", sub="The Revised Exam and the Task Playbook")

G.sec("The revised exam at a glance")
G.tex(r"""
The exam takes about 2 hours 30 minutes. The free-response section now comes \emph{first}. Its two speaking questions are built on a course project you research before exam day; the essay is independent of the project.

\begin{compare}{Part}{What you do}{Count, time, weight}
I-A Speaking & Q1 \textbf{Project Presentation}: present what you learned in your project research. & 3 min to prepare, 3 min to present; 20\% \\
 & Q2 \textbf{Project Q\&A}: answer four recorded questions about your presentation and research. & Each question heard twice; 40 s per answer; 15\% \\
I-B Writing & Q3 \textbf{Argumentative Essay}: take a position and defend it with three sources (print and audio). & 55 min, audio heard twice; 15\% \\
II-A Listening & Five sets of five questions. & 25 questions, 40 min, 25\% \\
II-B Reading & Six sets of five questions. & 30 questions, 40 min, 25\% \\
\end{compare}

The pre-2027 exam's email reply, simulated conversation and cultural comparison are gone. Interpersonal speaking now happens in the Project Q\&A, and cultural comparison is one of two ways to earn its culture row.

\subsection{The six units}
\begin{terms}
1 Families and Communities & family relationships, community activities, social interactions, urban and rural life \\
2 Language and Culture & customs and celebrations, linguistics, Spanish in the world \\
3 Art and Creativity & artistic heritage, architecture, literature, fashion and design, visual and performing arts \\
4 Science and Technology & innovation, personal technology and communication, science in everyday life, societal impact \\
5 Contemporary Life & education and career, entertainment and media, food and health, pop culture, sports, travel \\
6 Global Contexts & global communication, the natural world, history, policy and planning, transportation \\
\end{terms}

\begin{keyidea}[What the units are for]
The exam does not test a unit by name. Multiple-choice sources and the essay topic can come from any theme, so the units are where you build the vocabulary and cultural knowledge every task draws on.
\end{keyidea}
""")
G.q("1 Format", r"On the revised exam, how much of the score does the Argumentative Essay carry?",
    r"15\%", [(r"25\%", "25% is the listening part or the reading part of the multiple choice."),
              (r"20\%", "20% is the Project Presentation."),
              (r"50\%", "50% is the whole free-response section: presentation 20%, Q&A 15%, essay 15%.")],
    "Essay: Q3, 55 min, 15%.", "The free-response section is 50%: Project Presentation 20%, Project Q&A 15%, Argumentative Essay 15%.",
    ["Free response = 50%.", "20 + 15 leaves 15% for the essay."])
G.q("1 Format", r"How long do you have to answer each Project Q\&A question?",
    "40 seconds", [("20 seconds", "20 seconds was the turn length in the old simulated conversation."),
                   ("2 minutes", "2 minutes was the old cultural comparison; no revised task uses it."),
                   ("3 minutes", "3 minutes is the time to prepare, or to deliver, the Project Presentation.")],
    "Q&A: 4 questions, each heard twice, 40 s each.", "Each Q&A question is played twice; you then have 40 seconds to answer.",
    ["Q2 has four recorded questions.", "Each answer gets 40 seconds."])

G.sec("Multiple choice: the nine task types")
G.tex(r"""
Every set has five questions on one or two sources. Listening sources play twice; you see the questions and a short introduction before the first play.

\begin{compare}{Part}{Task type}{What to expect}
Listening & Audio and Chart & a report or conversation plus a chart; questions link the two \\
 & Audio Report & a radio or podcast segment: facts, causes, the speaker's view \\
 & Instructional Guidance & someone explains how to do something: steps, order, advice \\
 & Interview & questions and answers: the guest's experience and opinions \\
 & Presentation & a talk or lecture: main idea, organization, conclusion \\
Reading & Article & a news or magazine article \\
 & Article and Chart & an article plus a table or graph \\
 & Literary Text & an excerpt from a story, novel, poem or play \\
 & Promotional Material & an ad, flyer, or invitation: who it is for, what it offers, how to respond \\
\end{compare}

\begin{trap}
In Audio and Chart and Article and Chart sets, at least one question can be answered only from the chart, and one only by connecting the chart to the text. Read the chart's title, units and dates before the first listening.
\end{trap}
""")
G.q("2 Task types", r"In which multiple-choice task type are you most likely to be asked about the order of steps in a process?",
    "Instructional Guidance", [("Literary Text", "A literary excerpt is about character, tone and meaning, not procedures."),
                               ("Promotional Material", "Ads and flyers ask about audience, offer and how to respond, not steps."),
                               ("Interview", "An interview asks about a guest's experience and views.")],
    "Instructional Guidance = how to do something.", "Instructional Guidance sources explain a procedure, so questions ask about steps, order and advice.",
    ["Steps in a process → a how-to source → Instructional Guidance."])
G.q("2 Task types", r"Which source is part of the reading section, not the listening section?",
    "a flyer for a community festival", [("a radio segment about a new bike lane", "A radio segment is an Audio Report, a listening task."),
                                        ("a recorded interview with a chef", "Interviews are listening sources."),
                                        ("a recorded lecture on bilingual education", "A lecture is a Presentation, a listening task.")],
    "Flyer = Promotional Material, a reading task.", "The reading section has four task types: Article, Article and Chart, Literary Text, Promotional Material.",
    ["A flyer is Promotional Material, which is read."])

G.sec("Interpretive skills and question types")
G.tex(r"""
Every multiple-choice question tests one interpretive skill from the CED. The question sets in this series tag each item with one, so your score report shows which skill to work on.

\begin{compare}{Skill}{Question stems sound like}{How to answer}
1.A.1 Details & ¿Qué se menciona sobre\ldots? / According to the article\ldots & find the sentence; match meaning, not words \\
1.A.2 Data & ¿Qué indica la gráfica? / Which trend\ldots & read units and dates; compare the right rows \\
1.B.1 Main idea, purpose & ¿Cuál es el propósito\ldots? / main idea & title, first and last paragraph \\
1.B.2 Audience & ¿A quién va dirigido\ldots? & who would act on it \\
1.B.3 Tone, point of view & ¿Qué actitud\ldots? & the evaluative words: \emph{lamentablemente, por fin, sin duda} \\
1.B.4 Organization & ¿Cómo está organizado\ldots? & cause/effect, contrast, problem/solution markers \\
1.B.5 Word meaning & ¿Qué significa\ldots en la línea\ldots? & reread the sentence; test each choice in place \\
1.C.1 Connect sources & ¿Qué tienen en común\ldots? & one fact from each source \\
1.C.2 Conclusions & ¿Qué se puede concluir\ldots? & supported by the text, not just plausible \\
1.C.3 Implied meaning & ¿Qué se puede inferir\ldots? & the most likely reason or consequence \\
\end{compare}

\begin{trap}
Wrong choices often repeat a word from the source with a different meaning, or say something true about the topic that the source never states. A choice is right only if the source supports it.
\end{trap}
""")
G.q("3 Skills", r"A question asks: ¿Cuál es el propósito principal del anuncio? Which skill does it test?",
    "determining the main idea or purpose", [("identifying data points", "No chart or numbers are involved."),
                                            ("determining the meaning of a word from context", "The question is about the whole ad, not one word."),
                                            ("connecting two sources", "There is one source, the ad.")],
    "Propósito = purpose (1.B.1).", "Purpose questions (1.B.1) ask why the text exists: to inform, persuade, invite, warn.",
    ["propósito principal → purpose → 1.B.1."])
G.q("3 Skills", r"A choice for a reading question is true about the topic in real life, but the article never says it. The choice is",
    "wrong, because answers must be supported by the source", [("right, because it is accurate", "Accuracy outside the source does not count."),
                                                              ("right if it repeats a word from the article", "Repeated words are a classic trap."),
                                                              ("usually the main idea", "The main idea must come from the article.")],
    "Supported by the source, not just true.", "Interpretive questions reward what the source states or clearly implies.",
    ["The article does not support it → eliminate it."])

G.sec("The Argumentative Essay")
G.tex(r"""
You get three sources that take different views on one question: an article, a chart or infographic, and an audio report heard twice. A 6-minute countdown before the audio lets you read the prompt and the print sources. Write an essay for a college course that takes a position and defends it with all three sources.

\begin{compare}{Row (points)}{Full credit}{What loses it}
A Position (1) & a clear position that answers the question & restating the prompt; no position \\
B Source use (2) & evidence from all three sources, understood correctly, cited & two sources (1 point); misreading a source \\
C Argumentation (2) & claims, each explained with evidence & summaries with no link to your position \\
D Organization (2) & introduction, body around claims, conclusion; varied transitions & source-by-source summaries \\
E Language control (3) & wide vocabulary, varied structures, errors do not impede & simple sentences only; copying source wording \\
\end{compare}

\subsection{A 55-minute plan}
\begin{terms}
0--6 min & read the prompt and sources 2 and 3; note one usable fact from each \\
6--12 min & audio twice; write down two facts and the speaker's view \\
12--18 min & decide your position; plan two claims, each with evidence from two sources \\
18--50 min & write five paragraphs (about 300--350 words in all) \\
50--55 min & check agreement, accents, verb tenses, and that all three sources are named \\
\end{terms}

\begin{keyidea}[Citing sources]
Name a source by number, title or author: \emph{Según la Fuente 2\ldots}, \emph{Como se explica en el artículo ``\ldots'',} \emph{La gráfica muestra que\ldots}, \emph{En el audio, la entrevistada afirma que\ldots}. Paraphrase; copied sentences earn nothing in the language row.
\end{keyidea}

\begin{trap}
A qualified position (\emph{depende de\ldots}) still earns Row A, as long as it answers the question. A position that only lists both sides does not.
\end{trap}
""")
G.q("4 Essay", r"An essay uses the article and the chart well but never mentions the audio. What is the most it can earn for source use (Row B)?",
    "1 of 2", [("2 of 2", "Row B's top score requires all three sources."),
               ("0 of 2", "Two sources used correctly earn 1 point."),
               ("It loses Row A as well", "Row A is only about stating a position.")],
    "Row B: 2 points need all three sources.", "Source use: two sources (or three with misreadings) earn 1 point; all three, understood, earn 2.",
    ["Two of three sources → 1 point."])
G.q("4 Essay", r"Which paragraph plan best fits the organization row?",
    "Introduction with position; one paragraph per claim, each using two sources; counterargument and reply; conclusion",
    [("One paragraph summarizing each source, in order, then a conclusion", "Source-by-source summaries are the typical 1-point organization."),
     ("A single long paragraph with all the evidence", "No paragraphing or progression of ideas."),
     ("A conclusion first, then the sources", "Without an introduction and logical progression, the essay is hard to follow.")],
    "Organize around claims, not sources.", "Row D rewards an essay built around your argument, with an introduction, a conclusion and varied transitions.",
    ["Claims organize the essay; sources support each claim."])

G.sec("The course project: Presentation, Q\\&A and the PPR")
G.tex(r"""
The College Board releases the Course Project Packet in January of the exam year (January 2027) through the AP Digital Portfolio. For 2026--27 the project uses \textbf{music} as a lens on cultural products, practices and perspectives (the Unit 3 theme, Art and Creativity); you choose a focus within Spanish-speaking communities, research it in class, and practice presenting.

The \textbf{Personalized Project Reference (PPR)} is an outline of your presentation that you write and submit in the AP Digital Portfolio by \textbf{April 30, 2027}. You get a printed copy on exam day. Write keywords and facts, not sentences you plan to read aloud; check the packet for the exact length limit and the rules on outside help.

\subsection{Q1 Project Presentation (11 points)}
\begin{compare}{Row (points)}{Full credit}{What loses it}
A Task (2) & three or more factors, each explained with relevant details & three factors with no detail, or only one or two factors \\
B Culture (2) & specific examples showing how a perspective relates to a product or practice & examples with no perspective, or a vague one \\
C Organization (2) & logical order; varied transitions & a list of facts \\
D Language (3) & wide vocabulary, varied structures, culturally relevant expressions & a limited set of basic structures \\
E Delivery (2) & clear pronunciation, natural pace and intonation & hesitant, monotone, rushed \\
\end{compare}

\subsection{Q2 Project Q\&A (9 points)}
\begin{compare}{Row (points)}{Full credit}{What loses it}
A Task (2) & four relevant, complete answers & incomplete or off-topic answers \\
B Culture (2) & in at least one answer, a cultural comparison or a reflection on a perspective and a product or practice & only describing products or practices (1 point) \\
C Language (3) & as in the presentation & \\
D Fluency (2) & fluid, natural pace, clear pronunciation & long pauses, restarts \\
\end{compare}

\begin{keyidea}[The perspective link]
A product (a song, an instrument, a festival) or a practice (singing at a celebration) earns the top culture score only when you say what it shows about what people value: \emph{La cumbia se baila en las fiestas familiares porque\ldots refleja la importancia de\ldots}
\end{keyidea}
""")
G.q("5 Project", r"Which sentence best earns the top cultural understanding score in a presentation about music?",
    "En México, muchas familias contratan mariachis para los cumpleaños porque la música en vivo muestra cuánto valoran celebrar juntos.",
    [("Los mariachis usan trompetas, violines y guitarras.", "This describes a product but links it to no perspective."),
     ("A mí me gusta mucho la música mexicana.", "A personal preference is not a cultural example."),
     ("Investigué mucho y encontré muchas fuentes.", "Talking about the research process earns nothing for culture.")],
    "Perspective + product/practice, linked.", "Row B's top score needs a specific example that ties a product or practice to the perspective behind it.",
    ["Practice: hiring mariachis for birthdays.", "Perspective: valuing celebrating together.", "porque links them."])
G.q("5 Project", r"What may you do with your Personalized Project Reference during the presentation?",
    "glance at its keywords to stay organized", [("read a full script from it word for word", "The PPR is an outline; reading a script hurts delivery and may break the rules."),
                                                ("add new notes in the testing room", "You get the copy you submitted; you cannot add to it."),
                                                ("ask your teacher to rewrite it on exam morning", "It is due April 30 and must be your own work.")],
    "PPR = your submitted outline, printed for you.", "The PPR is a keyword outline submitted by April 30 and printed for you on exam day.",
    ["Use it to stay on track, not to read aloud."])

G.sec("Language control: structures that raise the score")
G.tex(r"""
The language rows (3 points in each free-response question) reward \emph{variety and control}. These structures show range in any topic.

\begin{compare}{Structure}{Use}{Example}
Subjunctive after opinion & es importante que, es posible que, dudo que & Es importante que los jóvenes \emph{aprendan} música tradicional. \\
Subjunctive after wish/advice & quiero que, recomiendo que, para que & Los padres quieren que sus hijos \emph{conozcan} sus raíces. \\
Preterite vs. imperfect & completed event vs. background or habit & Cuando \emph{era} niña, mi abuela me \emph{enseñó} una canción. \\
Si-clauses & hypothetical: imperfect subjunctive + conditional & Si las escuelas \emph{ofrecieran} más clases de arte, los estudiantes \emph{participarían} más. \\
Ser vs. estar & identity/characteristic vs. state/location & La fiesta \emph{es} en la plaza; la plaza \emph{está} llena. \\
Por vs. para & cause, means, exchange vs. purpose, recipient, deadline & Lo hizo \emph{por} su familia, \emph{para} ganar dinero. \\
Relative clauses & lo que, el cual, cuyo, donde & Es una tradición \emph{cuyo} origen es indígena. \\
Passive se & general or impersonal statements & \emph{Se celebra} en todo el país. \\
\end{compare}

\begin{trap}
Variety does not mean forcing every structure in. One accurate subjunctive and one si-clause in context beat five broken ones; errors that impede comprehension cost more than plain sentences.
\end{trap}
""")
G.q("6 Subjuntivo", r"Choose the correct form: Es necesario que el gobierno \blank\ más parques.",
    "construya", [("construye", "Es necesario que requires the subjunctive."),
                  ("construirá", "A future indicative cannot follow es necesario que."),
                  ("construir", "An infinitive fits only without que: es necesario construir.")],
    "Es necesario que + subjunctive.", "Impersonal expressions of necessity, opinion or possibility take the subjunctive in the que clause.",
    ["es necesario que → subjunctive → construya."])
G.q("6 Si", r"Which sentence correctly expresses a hypothetical situation?",
    "Si tuviera más tiempo, aprendería a tocar la guitarra.", [("Si tendría más tiempo, aprendería a tocar la guitarra.", "Never use the conditional after si in this pattern."),
                                                               ("Si tengo más tiempo, aprendería a tocar la guitarra.", "Present after si pairs with future or present, not the conditional."),
                                                               ("Si tuviera más tiempo, aprenderé a tocar la guitarra.", "Imperfect subjunctive pairs with the conditional, not the future.")],
    "Si + imperfect subjunctive, conditional.", "Contrary-to-fact: si + imperfect subjunctive in the si clause, conditional in the result clause.",
    ["si tuviera … aprendería."])

G.sec("Cohesive devices and register")
G.tex(r"""
\begin{compare}{Purpose}{Devices}{Example}
Add & además, también, asimismo, no solo\ldots sino también & No solo es divertido, sino también educativo. \\
Contrast & sin embargo, en cambio, aunque, a pesar de (que) & A pesar de los costos, vale la pena. \\
Cause/effect & porque, ya que, debido a, por lo tanto, así que & Debido a la sequía, el precio subió. \\
Example & por ejemplo, como, tal como & Como muestra la gráfica\ldots \\
Concede & es cierto que\ldots, pero; si bien & Si bien la tecnología ayuda, también aísla. \\
Conclude & en conclusión, en resumen, en definitiva & En definitiva, los beneficios superan los riesgos. \\
\end{compare}

\textbf{Register.} The essay is for a college course: use formal Spanish, no slang. In the Q\&A the interlocutor addresses you as \emph{tú} or \emph{usted}; answer in the same register and stay consistent.
""")
G.q("7 Cohesion", r"Which connector best introduces a contrasting idea in an essay?",
    "sin embargo", [("por lo tanto", "Por lo tanto introduces a consequence."),
                    ("además", "Además adds a point."),
                    ("por ejemplo", "Por ejemplo introduces an example.")],
    "Sin embargo = however.", "Contrast connectors: sin embargo, en cambio, no obstante, aunque, a pesar de.",
    ["Contrast → sin embargo."])
G.q("7 Register", r"Which sentence best fits the register of the Argumentative Essay?",
    "En mi opinión, es fundamental que las ciudades inviertan en transporte público.", [("O sea, el bus está súper bien, ¿no?", "Fillers (o sea, súper, ¿no?) are too informal for a college essay."),
                                                                                     ("Yo creo que el bus mola.", "Mola is slang."),
                                                                                     ("¡Viva el bus!", "A slogan is not a position explained in formal prose.")],
    "Formal, precise, no slang.", "The essay is written for a college course: formal register, precise vocabulary.",
    ["Formal opinion marker + subjunctive."])

G.sec("A study plan", "A study plan")
G.tex(r"""
\begin{terms}
September--December & Units 1--3: vocabulary, one practice essay per unit, a 3-minute talk on each unit theme \\
January & Course Project Packet released: choose your focus and three factors; start the research \\
February--March & Units 4--6; research and practice the presentation weekly; record yourself \\
April & Write and submit the PPR by April 30; practice the Q\&A with a partner asking unknown questions \\
May & Timed full exam: free response first, then multiple choice \\
\end{terms}
""")

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Part 0: Language Control Drill", r"Part 0 \textperiodcentered\ Question Set",
        abstract=r"""Twenty-one items on the structures that the language rows of all three free-response questions reward (the subjunctive, preterite and imperfect, si-clauses, ser and estar, por and para, pronouns, and cohesive devices), followed by a full practice Argumentative Essay with three original sources and the 10-point scoring guide. All sources are original and fictional, written for practice. Allow about 15 minutes for the drill and 55 minutes for the essay.""",
        scoring=r"Drill: \blank\ / \qtotal \qquad Essay: \blank\ / 10 \qquad Target: 18+ drill and 7+ essay",
        short="Part 0", sub="Language Control Drill")

Q.sec("The subjunctive")
Q.q("6 Subjuntivo", r"Mis padres quieren que yo \blank\ medicina.",
    "estudie", [("estudio", "Quieren que (wish) requires the subjunctive."),
                ("estudiar", "With a change of subject (padres → yo) you need que + subjunctive, not an infinitive."),
                ("estudiaré", "The future indicative cannot follow a verb of wanting + que.")],
    "Wish + que + new subject → subjunctive.", "Verbs of wish, advice and request trigger the subjunctive when the subject changes.",
    ["quieren que (wish), different subject → estudie."])
Q.q("6 Subjuntivo", r"Dudo que la nueva ley \blank\ el problema.",
    "resuelva", [("resuelve", "Dudar expresses doubt, which requires the subjunctive."),
                 ("resolverá", "After dudo que, use the subjunctive, not the future."),
                 ("resolvió", "The preterite indicative cannot follow dudo que.")],
    "Doubt → subjunctive.", "Doubt and denial (dudo que, no creo que, no es cierto que) take the subjunctive.",
    ["dudo que → resuelva."])
Q.q("6 Subjuntivo", r"Creo que la música \blank\ un papel importante en las fiestas.",
    "tiene", [("tenga", "Creo que affirms a belief, so it takes the indicative; no creo que would take the subjunctive."),
              ("tener", "A conjugated verb is needed after que."),
              ("tuviera", "There is no reason for the imperfect subjunctive here.")],
    "Creo que (belief) → indicative.", "Affirmative belief (creo, pienso, es cierto) takes the indicative; its negation takes the subjunctive.",
    ["creo que → tiene."])
Q.q("6 Subjuntivo", r"Te llamo en cuanto \blank\ a casa.",
    "llegue", [("llego", "En cuanto refers to a future event here, so it takes the subjunctive."),
               ("llegué", "The preterite would describe a past habit or event, not a future one."),
               ("llegaré", "The future cannot follow en cuanto.")],
    "Time conjunction + future event → subjunctive.", "Cuando, en cuanto, hasta que and después de que take the subjunctive for events that have not happened yet.",
    ["The call happens after a future arrival → llegue."])

Q.sec("Preterite and imperfect")
Q.q("6 Pasado", r"Cuando \blank\ pequeño, siempre íbamos al pueblo en verano.",
    "era", [("fui", "Age and background in the past take the imperfect."),
            ("fue", "Fue is third person and preterite; the speaker is describing himself as a child."),
            ("sería", "The conditional is not a past description.")],
    "Background, age → imperfect.", "The imperfect describes ongoing states and habits in the past: era pequeño, siempre íbamos.",
    ["Description of a past state → era."])
Q.q("6 Pasado", r"Estábamos cenando cuando de repente \blank\ el teléfono.",
    "sonó", [("sonaba", "De repente marks a single interrupting event, which takes the preterite."),
             ("suena", "The narration is in the past."),
             ("ha sonado", "The present perfect does not fit a past narrative interrupting an action.")],
    "Interrupting event → preterite.", "An ongoing action (imperfect: estábamos cenando) is interrupted by a completed one (preterite: sonó).",
    ["de repente → completed event → sonó."])
Q.q("6 Pasado", r"El año pasado mi hermana \blank\ a tocar el violín.",
    "aprendió", [("aprendía", "A completed accomplishment in a defined period takes the preterite."),
                 ("aprende", "El año pasado places the event in the past."),
                 ("aprenderá", "The future contradicts el año pasado.")],
    "Defined past period, completed → preterite.", "El año pasado frames a completed event: preterite.",
    ["aprendió."])

Q.sec("Si-clauses and the conditional")
Q.q("6 Si", r"Si \blank\ dinero, viajaría a Perú para conocer Machu Picchu.",
    "tuviera", [("tendría", "The conditional never follows si in a hypothetical clause."),
                ("tengo", "A present si clause pairs with the present or future, not viajaría."),
                ("tuve", "The preterite does not express a hypothesis.")],
    "Si + imperfect subjunctive, conditional.", "Contrary-to-fact present: si + imperfect subjunctive, then the conditional.",
    ["viajaría (conditional) → si tuviera."])
Q.q("6 Si", r"Si llueve mañana, el concierto \blank\ en el gimnasio.",
    "será", [("sería", "A real (likely) condition with si + present takes the future or present, not the conditional."),
             ("fuera", "The imperfect subjunctive belongs in the si clause of a hypothesis."),
             ("haya sido", "The perfect subjunctive does not fit a future result.")],
    "Real condition: si + present, future.", "Likely conditions: si + present indicative, result in the present, future or a command.",
    ["si llueve (likely) → será."])

Q.sec("Ser, estar, por and para")
Q.q("6 Ser/estar", r"La reunión \blank\ en la biblioteca a las seis.",
    "es", [("está", "Events take ser for location: la fiesta es en…"),
           ("hay", "Hay introduces something new (hay una reunión), not where a known event takes place."),
           ("tiene", "Tener does not express location.")],
    "Event location → ser.", "Ser locates events (la boda es en la iglesia); estar locates people and things.",
    ["reunión = event → es."])
Q.q("6 Ser/estar", r"Después del partido, los jugadores \blank\ muy cansados.",
    "estaban", [("eran", "Tiredness after a game is a temporary state: estar."),
                ("fueron", "Ser does not express a temporary condition."),
                ("habían", "Haber is an auxiliary and needs a participle.")],
    "Temporary state → estar.", "Estar expresses conditions and results (cansado, listo, abierto).",
    ["cansados after a game → estaban."])
Q.q("6 Por/para", r"Estudio mucho \blank\ sacar una buena nota en el examen.",
    "para", [("por", "Por expresses cause or exchange; purpose (in order to) is para."),
             ("de", "De does not express purpose."),
             ("con", "Con means with.")],
    "Purpose → para + infinitive.", "Para expresses purpose, destination, recipient and deadline.",
    ["in order to → para."])
Q.q("6 Por/para", r"Gracias \blank\ tu ayuda con el proyecto.",
    "por", [("para", "Gracias por is fixed: thanks for (because of)."),
            ("a", "Gracias a means thanks to, and would need a different structure."),
            ("de", "Gracias de is not used.")],
    "Gracias por.", "Por expresses cause, exchange and gratitude: gracias por, por eso, por la mañana.",
    ["gracias por."])

Q.sec("Pronouns and agreement")
Q.q("6 Pronombres", r"¿Le diste el regalo a tu abuela? — Sí, \blank\ di ayer.",
    "se lo", [("le lo", "Le becomes se before lo/la/los/las."),
              ("lo le", "The indirect object comes first."),
              ("se la", "El regalo is masculine: lo.")],
    "le + lo → se lo.", "When an indirect object pronoun (le, les) precedes lo/la/los/las, it becomes se.",
    ["a tu abuela → le → se; el regalo → lo."])
Q.q("6 Pronombres", r"A muchos jóvenes les \blank\ las canciones de reguetón.",
    "gustan", [("gusta", "The subject is las canciones (plural), so the verb is plural."),
               ("gustamos", "The verb agrees with the thing liked, not with the people."),
               ("gustan a", "No preposition follows the verb here.")],
    "Gustar agrees with what is liked.", "With gustar, the subject is the thing liked: les gustan las canciones.",
    ["las canciones → gustan."])
Q.q("6 Acuerdo", r"Las tradiciones \blank\ por los abuelos se conservan en muchas familias.",
    "transmitidas", [("transmitido", "The participle used as an adjective agrees with tradiciones (feminine plural)."),
                     ("transmitiendo", "A gerund cannot modify a noun this way."),
                     ("transmitidos", "Tradiciones is feminine.")],
    "Participle as adjective agrees.", "A past participle used as an adjective agrees in gender and number.",
    ["tradiciones (f. pl.) → transmitidas."])

Q.sec("Relative clauses")
Q.q("6 Relativos", r"Es una costumbre \blank\ origen se remonta a la época colonial.",
    "cuyo", [("cuya", "Cuyo agrees with what is possessed (origen, masculine), not with costumbre."),
             ("que su", "Que su is a common error for cuyo in writing."),
             ("la cual", "La cual cannot express possession.")],
    "Cuyo = whose, agrees with the possessed noun.", "Cuyo/cuya/cuyos/cuyas means whose and agrees with the noun that follows.",
    ["origen (m. sg.) → cuyo."])
Q.q("6 Relativos", r"\blank\ más me sorprendió fue la cantidad de jóvenes en el festival.",
    "Lo que", [("Que", "A sentence-initial noun clause needs lo que."),
               ("El cual", "El cual refers back to a specific noun."),
               ("Cual", "Cual alone cannot introduce this clause.")],
    "Lo que = what (the thing that).", "Lo que introduces an idea with no specific antecedent: lo que me sorprendió.",
    ["what surprised me → lo que."])

Q.sec("Cohesive devices")
Q.q("7 Cohesión", r"La ciudad construyó más ciclovías; \blank, el tráfico disminuyó un 10\%.",
    "como resultado", [("en cambio", "En cambio introduces a contrast, but the second clause is a result."),
                       ("a pesar de eso", "This concedes an obstacle; the result is positive and expected."),
                       ("por ejemplo", "The second clause is not an example of the first.")],
    "Result → como resultado / por lo tanto.", "Consequence connectors: por lo tanto, como resultado, así que, por consiguiente.",
    ["Ciclovías caused less traffic → result."])
Q.q("7 Cohesión", r"\blank\ la tecnología facilita la comunicación, también puede aislar a las personas.",
    "Si bien", [("Por lo tanto", "This introduces a conclusion, not a concession."),
                ("Debido a", "Debido a needs a noun and expresses cause."),
                ("En resumen", "En resumen introduces a summary.")],
    "Si bien = although (concession).", "Si bien and aunque concede a point before the main claim.",
    ["concession + también → si bien."])
Q.q("7 Registro", r"Which opening best suits the formal Argumentative Essay?",
    "El tema de si los colegios deben prohibir los celulares ha generado un intenso debate.", [("Bueno, pues, los celulares, ¿no?", "Fillers belong in casual speech."),
                                                                                              ("¡Hola, profe! Te voy a contar mi opinión.", "Addressing the reader informally does not fit a college essay."),
                                                                                              ("Los celulares son lo peor, punto.", "Slangy and absolute, with no context.")],
    "Formal introduction: context + issue.", "A formal opening names the issue and its importance before the position.",
    ["Context + debate → formal register."])

GUIDE, QSET = G, Q

Q.frq(kind="Argumentative Essay", head=r"Question 3 \textperiodcentered\ Argumentative Essay \textperiodcentered\ 10 points \textperiodcentered\ 55 minutes", mins=55,
      directions=[r"Vas a escribir un ensayo argumentativo para un curso universitario. Lee el tema y las fuentes escritas; después escucha la fuente auditiva (aquí, la transcripción). Escribe un ensayo que integre material de las tres fuentes para apoyar tu posición. Indica las fuentes que usas por número, título o autor."],
      sources=[dict(title=r"Fuente 1 \textperiodcentered\ Artículo \textperiodcentered\ «La escuela que apagó las pantallas»", paras=[
          r"Hace dos años, el Colegio Nuevo Horizonte, en Valparaíso, decidió que los estudiantes guardarían sus celulares en casilleros durante toda la jornada. Al principio hubo protestas. «Pensábamos que era un castigo», recuerda Martina, de 16 años.",
          r"Hoy la directora, Rosa Iturra, presenta otros datos: las faltas por conflictos en el recreo bajaron casi a la mitad y la biblioteca se llena a la hora del almuerzo. «Los chicos volvieron a hablar entre ellos», afirma.",
          r"No todos están convencidos. Algunos padres se quejan de que no pueden comunicarse con sus hijos en una emergencia, y varios profesores echan de menos las aplicaciones educativas que usaban en clase."]),
               dict(title=r"Fuente 2 \textperiodcentered\ Gráfica \textperiodcentered\ ¿Para qué usan el celular los estudiantes en la escuela?", paras=[
          r"Encuesta a 1.200 estudiantes de secundaria de cinco países. Porcentaje que realiza cada actividad al menos una vez por día escolar."],
                    table=(["Actividad", "Porcentaje"], [["Redes sociales", "71 \\%"], ["Mensajes con amigos", "68 \\%"], ["Buscar información para una clase", "44 \\%"], ["Aplicaciones de la clase", "29 \\%"], ["Llamar a la familia", "12 \\%"]])),
               dict(title=r"Fuente 3 \textperiodcentered\ Audio (transcripción) \textperiodcentered\ Entrevista en «Radio Aula»", paras=[
          r"(PRESENTADORA) Hoy hablamos con el psicólogo Andrés Molina. Andrés, ¿hay que prohibir los celulares en la escuela?",
          r"(ANDRÉS) Prohibir es la solución más fácil, pero no siempre la mejor. Los jóvenes van a usar el teléfono toda la vida; la escuela es el lugar ideal para aprender a usarlo bien. Yo propongo reglas claras: el celular se guarda durante la clase, salvo cuando el profesor lo pide para una actividad.",
          r"(PRESENTADORA) ¿Y los recreos?",
          r"(ANDRÉS) Ahí sí recomiendo espacios sin pantallas. Los estudios muestran que el juego y la conversación cara a cara reducen la ansiedad."])],
      prompt=[r"Tema del ensayo: \textbf{¿Deben las escuelas prohibir el uso de los celulares durante toda la jornada escolar?}"],
      model=[r"En los últimos años, muchas escuelas han tenido que decidir qué hacer con los celulares. Aunque prohibirlos durante toda la jornada parece una solución sencilla, creo que es más eficaz limitar su uso con reglas claras que eliminarlo por completo.",
             r"En primer lugar, es cierto que las pantallas pueden aislar a los estudiantes. Según la Fuente 1, después de que el Colegio Nuevo Horizonte guardó los celulares, las faltas por conflictos en el recreo bajaron casi a la mitad y los alumnos «volvieron a hablar entre ellos». Además, la gráfica de la Fuente 2 muestra que el 71 \% de los estudiantes usa las redes sociales cada día escolar, una actividad que poco tiene que ver con aprender. Por eso, es razonable que los recreos sean espacios sin pantallas, como recomienda el psicólogo de la Fuente 3.",
             r"Sin embargo, una prohibición total elimina usos valiosos. La misma gráfica indica que el 44 \% de los estudiantes busca información para una clase con el celular, y en la Fuente 1 varios profesores echan de menos las aplicaciones educativas. Como explica Andrés Molina en la Fuente 3, los jóvenes usarán el teléfono toda la vida, así que la escuela debería enseñarles a usarlo bien en lugar de esconderlo.",
             r"Algunos padres señalan, con razón, que necesitan comunicarse con sus hijos en una emergencia (Fuente 1). Una regla que permita el celular en momentos y lugares concretos resuelve también este problema.",
             r"En conclusión, si las escuelas guardaran los celulares durante la clase y los recreos, pero permitieran su uso cuando el profesor lo pidiera, conservarían los beneficios del aprendizaje digital sin perder la convivencia que los estudiantes recuperaron en Valparaíso."],
      rows=[("A Position", 1, "states a clear position that answers the question (a qualified one is fine)", "restates the topic or only lists both sides"),
            ("B Source use", 2, "uses all three sources correctly and names each one", "uses two sources (1 point) or misreads them"),
            ("C Argumentation", 2, "makes claims and explains how the evidence supports them", "summarizes sources without linking them to the position"),
            ("D Organization", 2, "introduction, paragraphs built around claims, conclusion; varied transitions", "source-by-source summary; no introduction or conclusion"),
            ("E Language control", 3, "wide vocabulary, varied structures (subjunctive, si-clause), errors that do not impede", "basic sentences, copied phrases, errors that impede")],
      tips=["The position is qualified but clear (limit, not ban).", "Each body paragraph uses two sources, named by number.",
            "The counterargument paragraph concedes a point (con razón) and answers it.", "The conclusion uses a si-clause with the imperfect subjunctive and conditional."],
      ask="Write your essay in Spanish (about 300–350 words), then mark it against each row.", lines=22)
