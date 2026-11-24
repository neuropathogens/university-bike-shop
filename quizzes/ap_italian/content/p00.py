from ap_wl.model import Doc

STEM = "00-exam-playbook"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Part 0: The Revised Exam and the Task Playbook", r"Part 0 \textperiodcentered\ Study Guide",
        abstract=r"""This guide is written for the revised AP Italian Language and Culture course (effective fall 2026) and its first exam, in May 2027, which runs entirely in Bluebook. The revised Italian exam has the same structure as the revised French, German and Spanish exams: a course project presented and discussed in Italian, an Argumentative Essay, and 55 multiple-choice questions. This guide sets out what each task asks you to do, how the free-response questions are scored, and the language that moves a response up a scoring row. Read it before the unit guides: every unit guide ends with a task kit that assumes the rubrics here. Sources: the College Board AP world language revision pages and the Course and Exam Description (CED), effective fall 2026. Check AP Central for any later change.""",
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
2 Language and Culture & customs and celebrations, linguistics, Italian in the world \\
3 Art and Creativity & artistic heritage, architecture, literature, fashion and design, visual and performing arts \\
4 Science and Technology & innovation, personal technology and communication, science in everyday life, societal impact \\
5 Contemporary Life & education and career, entertainment and media, food and health, pop culture, sports, travel \\
6 Global Contexts & global communication, the natural world, history, policy and planning, transportation \\
\end{terms}

\begin{keyidea}[What the units are for]
The exam does not test a unit by name. Multiple-choice sources and the essay topic can come from any theme and any Italian-speaking community: Italy, San Marino, Vatican City, Italian-speaking Switzerland, and Italian communities abroad, from Argentina to Australia. The units are where you build the vocabulary and cultural knowledge every task draws on.
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
 & Promotional Material & an ad, flyer or invitation: who it is for, what it offers, how to respond \\
\end{compare}

\begin{trap}
In Audio and Chart and Article and Chart sets, at least one question can be answered only from the chart, and one only by connecting the chart to the text. Read the chart's title, units and dates before the first listening.
\end{trap}
""")
G.q("2 Task types", r"In which multiple-choice task type are you most likely to be asked about the order of steps in a process?",
    "Instructional Guidance", [("Literary Text", "A literary excerpt is about character, tone and meaning, not procedures."),
                               ("Promotional Material", "Ads and flyers ask about audience, offer and how to respond."),
                               ("Interview", "An interview asks about a guest's experience and views.")],
    "Instructional Guidance = how to do something.", "Instructional Guidance sources explain a procedure, so questions ask about steps, order and advice.",
    ["Steps in a process → Instructional Guidance."])
G.q("2 Task types", r"Which source belongs to the reading section, not the listening section?",
    "a poster for a village sagra", [("a radio report on a new tram line", "A radio report is an Audio Report, a listening task."),
                                     ("a recorded interview with a chef", "Interviews are listening sources."),
                                     ("a recorded lecture on dialects", "A lecture is a Presentation, a listening task.")],
    "Poster = Promotional Material.", "The reading section has four task types: Article, Article and Chart, Literary Text, Promotional Material.",
    ["A poster is read → Promotional Material."])

G.sec("Interpretive skills and question types")
G.tex(r"""
Every multiple-choice question tests one interpretive skill from the CED. The question sets in this series tag each item with one, so your score report shows which skill to work on.

\begin{compare}{Skill}{Question stems sound like}{How to answer}
1.A.1 Details & Secondo l'articolo\ldots? / Che cosa si dice di\ldots? & find the sentence; match meaning, not words \\
1.A.2 Data & Che cosa mostra il grafico? & read units and dates; compare the right rows \\
1.B.1 Main idea, purpose & Qual è lo scopo\ldots? / il tema principale & title, first and last paragraph \\
1.B.2 Audience & A chi si rivolge\ldots? & who would act on it \\
1.B.3 Tone, point of view & Qual è l'atteggiamento di\ldots? & evaluative words: \emph{purtroppo, finalmente, senza dubbio} \\
1.B.4 Organization & Come è organizzato il testo? & cause/effect, contrast, problem/solution markers \\
1.B.5 Word meaning & Che cosa significa\ldots? & reread the sentence; test each choice in place \\
1.C.1 Connect sources & Che cosa hanno in comune\ldots? & one fact from each source \\
1.C.2 Conclusions & Che cosa si può concludere? & supported by the text, not just plausible \\
1.C.3 Implied meaning & Che cosa si può dedurre? & the most likely reason or consequence \\
\end{compare}

\begin{trap}
Wrong choices often repeat a word from the source with a different meaning, or say something true about the topic that the source never states. A choice is right only if the source supports it.
\end{trap}
""")
G.q("3 Skills", r"A question asks: Qual è lo scopo principale di questo annuncio? Which skill does it test?",
    "determining the main idea or purpose", [("identifying data points", "No chart is involved."),
                                            ("determining the meaning of a word from context", "The question is about the whole ad."),
                                            ("connecting two sources", "There is one source.")],
    "Scopo = purpose (1.B.1).", "Purpose questions (1.B.1) ask why the text exists: to inform, persuade, invite, warn.",
    ["scopo principale → purpose → 1.B.1."])
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
0--6 min & read the prompt and sources 1 and 2; note one usable fact from each \\
6--12 min & audio twice; write down two facts and the speaker's view \\
12--18 min & decide your position; plan two claims, each with evidence from two sources \\
18--50 min & write five paragraphs (about 300--350 words in all) \\
50--55 min & check the congiuntivo after opinion verbs and conjunctions, agreement of nouns, adjectives and participles, and that all three sources are named \\
\end{terms}

\begin{keyidea}[Citing sources]
Name a source by number, title or author: \emph{Secondo la fonte 2\ldots}, \emph{Come dimostra l'articolo «\ldots», \ldots}, \emph{Il grafico mostra che\ldots}, \emph{Nella registrazione, l'esperta spiega che\ldots} Paraphrase; copied sentences earn nothing in the language row.
\end{keyidea}

\begin{trap}
A qualified position (\emph{sì, ma solo se\ldots}) still earns Row A, as long as it answers the question. A position that only lists both sides does not.
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
The College Board releases the Course Project Packet in January of the exam year (January 2027) through the AP Digital Portfolio. For 2026--27 the project uses \textbf{music} as a lens on cultural products, practices and perspectives (the Unit 3 theme, Art and Creativity); you choose a focus within Italian-speaking communities, research it in class, and practice presenting.

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
A product (a song, an instrument, a festival) or a practice (singing in a choir, playing in the town band) earns the top culture score only when you say what it shows about what people value: \emph{In molti paesi del Sud la banda suona a ogni festa patronale, il che dimostra quanto contino la comunità e la tradizione.}
\end{keyidea}
""")
G.q("5 Project", r"Which sentence best earns the top cultural understanding score in a presentation about music?",
    "In molti paesi del Sud la banda suona a ogni festa patronale, il che dimostra quanto siano importanti la comunità e la tradizione.",
    [("Una banda ha trombe, tromboni e una tuba.", "This describes a product but links it to no perspective."),
     ("A me piace molto la musica delle bande.", "A personal preference is not a cultural example."),
     ("Per il mio progetto ho trovato molte fonti.", "The research process earns nothing for culture.")],
    "Perspective + product/practice, linked.", "Row B's top score needs a specific example that ties a product or practice to the perspective behind it.",
    ["Practice: the town band at every patron-saint festival.", "Perspective: community and tradition.", "il che dimostra links them."])
G.q("5 Project", r"What may you do with your Personalized Project Reference during the presentation?",
    "glance at its keywords to stay organized", [("read a full script from it word for word", "The PPR is an outline; reading a script hurts delivery and may break the rules."),
                                                ("add new notes in the testing room", "You get the copy you submitted."),
                                                ("ask your teacher to rewrite it on exam morning", "It is due April 30 and must be your own work.")],
    "PPR = your submitted outline, printed for you.", "The PPR is a keyword outline submitted by April 30 and printed for you on exam day.",
    ["Use it to stay on track, not to read aloud."])

G.sec("Language control: structures that raise the score")
G.tex(r"""
The language rows (3 points in each free-response question) reward \emph{variety and control}. In Italian, the congiuntivo, the choice of past tense, and pronouns are where control shows first.

\begin{compare}{Structure}{Use}{Example}
Congiuntivo & opinion, doubt, emotion, necessity; after benché, affinché, prima che & Credo che la musica \emph{sia} un ponte tra generazioni. \\
Periodo ipotetico & se + congiuntivo imperfetto, condizionale & Se le scuole \emph{avessero} più fondi, più ragazzi \emph{imparerebbero} uno strumento. \\
Passato prossimo vs. imperfetto & completed events vs. background and habits & Ieri \emph{ho sentito} un concerto. / Da bambina \emph{suonava} il violino. \\
Pronouns & direct, indirect, combined; ne and ci & \emph{Gliel'}ho detto. \emph{Ne} ho comprati tre. \\
Si impersonale e passivante & general statements & In Italia \emph{si cena} tardi. \emph{Si vendono} biglietti. \\
Relative pronouns & che; preposition + cui & È una tradizione \emph{che} molte famiglie mantengono. La città \emph{in cui} vivo\ldots \\
Passive & essere or venire + participle & La festa \emph{viene celebrata} ogni anno a giugno. \\
\end{compare}

\begin{trap}
Variety does not mean forcing every structure in. One accurate periodo ipotetico and a few correct congiuntivi beat five broken ones; errors that impede comprehension cost more than plain sentences. Never put the condizionale after \emph{se}: \emph{se avessi}, not \emph{se avrei}.
\end{trap}
""")
G.q("6 Congiuntivo", r"Choose the correct sentence: ``I think young people should vote.''",
    "Credo che i giovani debbano votare.", [("Credo che i giovani devono votare.", "Opinion verbs like credere che take the congiuntivo in standard Italian."),
                                           ("Credo che i giovani dovere votare.", "A conjugated verb is needed in the che-clause."),
                                           ("Credo i giovani che debbano votare.", "Che must introduce the clause, before its subject.")],
    "credere che → congiuntivo.", "Verbs of opinion, doubt, wish and emotion followed by che take the congiuntivo.",
    ["credo che … debbano."])
G.q("6 Ipotetico", r"Which sentence correctly expresses a hypothetical situation?",
    "Se avessi più tempo, imparerei la chitarra.", [("Se avrei più tempo, imparerei la chitarra.", "The condizionale never goes after se."),
                                                    ("Se ho più tempo, imparerei la chitarra.", "A real condition (ho) does not pair with the condizionale."),
                                                    ("Se avessi più tempo, imparassi la chitarra.", "The main clause needs the condizionale, not the congiuntivo.")],
    "Se + congiuntivo imperfetto, condizionale.", "Hypotheticals in the present: se + congiuntivo imperfetto in the if-clause, condizionale presente in the main clause.",
    ["se avessi …, imparerei …"])

G.sec("Cohesive devices and register")
G.tex(r"""
\begin{compare}{Purpose}{Devices}{Example}
Add & inoltre, per di più, non solo\ldots ma anche & Non solo è divertente, ma è anche istruttivo. \\
Contrast & ma, però, tuttavia, invece, mentre & La città è cara; tuttavia molti vogliono viverci. \\
Concede & benché, sebbene, nonostante (+ congiuntivo); è vero che\ldots ma & Benché la tecnologia aiuti, può isolare. \\
Cause & perché, poiché, siccome, dato che & Siccome pioveva poco, i prezzi sono saliti. \\
Result & quindi, perciò, di conseguenza & Pioveva poco; di conseguenza i prezzi sono saliti. \\
Example & per esempio, come dimostra & Come dimostra il grafico, \ldots \\
Conclude & in conclusione, per concludere, insomma (spoken) & In conclusione, i vantaggi prevalgono. \\
\end{compare}

\textbf{Mood with connectors.} \emph{Benché, sebbene, nonostante, affinché, prima che, a meno che} require the congiuntivo. \emph{Perché} meaning ``because'' takes the indicative; \emph{perché} meaning ``so that'' takes the congiuntivo.

\textbf{Register.} The essay is for a college course: formal Italian, no slang (\emph{figo}, \emph{un casino}, \emph{tipo} as a filler). In the Q\&A the interlocutor addresses you as \emph{tu} or \emph{Lei}; answer in the same register and stay consistent.
""")
G.q("7 Cohesion", r"Which connector must be followed by the congiuntivo?",
    "benché", [("perché, meaning because", "Causal perché takes the indicative."),
               ("quindi", "Quindi introduces a result clause in the indicative."),
               ("mentre", "Mentre takes the indicative.")],
    "benché → congiuntivo.", "Concessive conjunctions (benché, sebbene, nonostante) require the congiuntivo.",
    ["Benché la città sia cara, …"])
G.q("7 Register", r"Which sentence best fits the register of the Argumentative Essay?",
    "Secondo me, le città dovrebbero investire di più nei trasporti pubblici.", [("Il bus è tipo troppo figo, no?", "Fillers and slang are too informal for a college essay."),
                                                                                ("C'ho una voglia di autobus...", "C'ho and the trailing tone are casual speech."),
                                                                                ("Bus, bus, evviva!", "A slogan is not a position explained in formal prose.")],
    "Formal, precise, no slang.", "The essay is written for a college course: formal register, precise vocabulary.",
    ["Opinion marker + condizionale (dovrebbero)."])

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
        abstract=r"""Seventeen items on the structures that the language rows of all three free-response questions reward (the congiuntivo, the periodo ipotetico, pronouns, the passato prossimo and imperfetto, relative pronouns, the si impersonale, and connectors), followed by a full practice Argumentative Essay with three original sources and the 10-point scoring guide. All sources are original and fictional, written for practice. Allow about 15 minutes for the drill and 55 minutes for the essay.""",
        scoring=r"Drill: \blank\ / \qtotal \qquad Essay: \blank\ / 10 \qquad Target: 16+ drill and 7+ essay",
        short="Part 0", sub="Language Control Drill")

Q.sec("Congiuntivo")
Q.q("6 Congiuntivo", r"Penso che i nonni \blank\ un ruolo importante nella famiglia italiana.",
    "abbiano", [("hanno", "Pensare che takes the congiuntivo in standard Italian."),
                ("abbia", "The subject i nonni is plural."),
                ("avere", "A conjugated verb is needed.")],
    "pensare che → congiuntivo, agreeing with the subject.", "After verbs of opinion + che, use the congiuntivo; it agrees with its subject.",
    ["i nonni (plural) … abbiano."])
Q.q("6 Congiuntivo", r"Benché \blank, il concerto si è svolto in piazza.",
    "piovesse", [("pioveva", "Benché requires the congiuntivo."),
                 ("piova", "The main clause is in the past, so the congiuntivo imperfetto is needed."),
                 ("piovuto", "A conjugated verb is needed.")],
    "benché + congiuntivo; past → imperfetto.", "Benché always takes the congiuntivo; with a past main clause, use the congiuntivo imperfetto.",
    ["Benché piovesse, … si è svolto."])
Q.q("6 Congiuntivo", r"È importante che tutti i cittadini \blank\ alle elezioni.",
    "partecipino", [("partecipano", "Impersonal expressions of necessity take the congiuntivo."),
                    ("partecipi", "Tutti i cittadini is plural."),
                    ("partecipare", "After che a conjugated verb is needed.")],
    "è importante che → congiuntivo.", "Impersonal expressions (è importante, è necessario, bisogna che) take the congiuntivo.",
    ["tutti i cittadini … partecipino."])

Q.sec("Periodo ipotetico")
Q.q("6 Ipotetico", r"Se \blank\ ricco, viaggerei per il mondo.",
    "fossi", [("sono", "A real condition (sono) does not pair with the condizionale."),
              ("sarei", "The condizionale never goes after se."),
              ("ero", "The imperfetto is not a standard hypothesis.")],
    "essere → fossi.", "Hypothetical: se + congiuntivo imperfetto (fossi, avessi), condizionale in the main clause.",
    ["se fossi …, viaggerei …"])
Q.q("6 Ipotetico", r"Choose the most polite request.",
    "Potrebbe aiutarmi, per favore?", [("Mi aiuti!", "An imperative is direct, not polite."),
                                       ("Lei mi aiuta.", "A statement, not a request."),
                                       ("Puoi aiutarmi?", "Informal tu and the indicative.")],
    "Condizionale for politeness.", "The condizionale (potrebbe, vorrei, sarebbe possibile) softens requests.",
    ["Potrebbe … → polite."])

Q.sec("Pronomi")
Q.q("6 Pronomi", r"— Quanti fratelli hai? — \blank\ ho due.",
    "Ne", [("Li", "With a number and no noun, Italian uses the partitive ne."),
           ("Ci", "Ci replaces a place or a + noun."),
           ("Gli", "Gli is an indirect object pronoun.")],
    "Quantity → ne.", "Ne replaces a noun after a number or quantity: ne ho due, ne voglio un po'.",
    ["due (fratelli) → ne ho due."])
Q.q("6 Pronomi", r"Le foto della festa? Le ho \blank\ ieri sera.",
    "viste", [("visto", "With a third-person direct object pronoun before avere, the participle must agree."),
              ("vista", "Le foto is plural."),
              ("visti", "Foto is feminine.")],
    "le … viste.", "Avere + lo/la/li/le: the participle agrees with the pronoun (le ho viste).",
    ["le (feminine plural) → viste."])
Q.q("6 Pronomi", r"Voglio molto bene a mia nonna: \blank\ scrivo una lettera ogni settimana.",
    "le", [("la", "Scrivere a qualcuno takes an indirect object: a lei → le."),
           ("lo", "Lo is a masculine direct object."),
           ("li", "Li is a masculine plural direct object.")],
    "a lei → le.", "Indirect object pronouns: mi, ti, gli (a lui), le (a lei), ci, vi, gli (a loro).",
    ["scrivere a mia nonna → le scrivo."])

Q.sec("Passato prossimo e imperfetto")
Q.q("6 Passato", r"Ieri \blank\ al cinema con i miei amici.",
    "sono andato", [("ho andato", "Andare forms the passato prossimo with essere."),
                    ("andavo", "Ieri marks a single completed event, not a habit or background."),
                    ("vado", "The present does not fit ieri.")],
    "Motion verbs → essere.", "Verbs of motion and change of state (andare, venire, diventare) form compound tenses with essere.",
    ["andato → sono andato."])
Q.q("6 Passato", r"Quando \blank\ bambina, suonavo il pianoforte ogni giorno.",
    "ero", [("sono stata", "Describing a period of life in the past takes the imperfetto."),
            ("fossi", "The congiuntivo is not needed after quando."),
            ("sarei", "The condizionale is hypothetical.")],
    "Background, age, habits → imperfetto.", "The imperfetto describes ongoing states and habits in the past: ero, suonavo.",
    ["quando ero bambina."])

Q.sec("Relativi e si impersonale")
Q.q("6 Relativi", r"Questo è il musicista \blank\ ho conosciuto ieri.",
    "che", [("cui", "Cui is used after a preposition."),
            ("chi", "Chi means whoever and has no antecedent."),
            ("dove", "Dove refers to a place.")],
    "Direct object → che.", "Che replaces a subject or direct object; cui follows a preposition.",
    ["ho conosciuto il musicista → che."])
Q.q("6 Relativi", r"La città in \blank\ sono nata si trova in Toscana.",
    "cui", [("che", "After a preposition, use cui, not che."),
            ("quale", "Quale needs the article: nella quale."),
            ("dove", "In dove is ungrammatical; use in cui or dove alone.")],
    "preposition + cui.", "After a preposition, the relative pronoun is cui (or the article + quale).",
    ["in cui."])
Q.q("6 Relativi", r"In molte città italiane \blank\ i biglietti dell'autobus dal tabaccaio.",
    "si comprano", [("si compra", "With si passivante, the verb agrees with the plural noun i biglietti."),
                    ("si comprare", "A conjugated verb is needed."),
                    ("comprano si", "Si goes before the verb.")],
    "si passivante agrees with the noun.", "Si + verb + plural noun: the verb is plural (si comprano i biglietti).",
    ["i biglietti (plural) → si comprano."])

Q.sec("Connettivi e registro")
Q.q("7 Coesione", r"Il comune ha costruito nuove piste ciclabili; \blank\ il traffico è diminuito del 10 per cento.",
    "di conseguenza", [("tuttavia", "Tuttavia introduces a contrast, but the second clause is a result."),
                       ("benché", "Benché is concessive and needs the congiuntivo."),
                       ("per esempio", "The second clause is not an example of the first.")],
    "Result → di conseguenza / quindi.", "Consequence connectors: quindi, perciò, di conseguenza.",
    ["bike lanes caused less traffic → result."])
Q.q("7 Coesione", r"\blank\ la tecnologia faciliti la comunicazione, può anche isolare le persone.",
    "Sebbene", [("Perciò", "Perciò introduces a result and does not take the congiuntivo."),
                ("Poiché", "Poiché means because and takes the indicative."),
                ("In conclusione", "This introduces a summary.")],
    "Sebbene = although (+ congiuntivo).", "Sebbene concedes a point; faciliti is congiuntivo, which only a concessive conjunction fits here.",
    ["concession + congiuntivo → sebbene."])
Q.q("7 Coesione", r"Gli adulti preferiscono la radio, \blank\ i giovani ascoltano musica in streaming.",
    "mentre", [("perché", "Perché introduces a cause."),
               ("quindi", "Quindi introduces a result."),
               ("affinché", "Affinché introduces a purpose and takes the congiuntivo.")],
    "Contrast between two groups → mentre.", "Mentre (whereas) contrasts two parallel facts.",
    ["adults: radio / young people: streaming → contrast."])
Q.q("7 Registro", r"Which opening best suits the formal Argumentative Essay?",
    "La questione se i musei debbano essere gratuiti è da anni al centro di un acceso dibattito.", [("Allora, i musei, boh.", "Fillers belong in casual speech."),
                                                                                                   ("Ciao prof! Adesso ti dico cosa penso.", "Addressing the reader informally does not fit a college essay."),
                                                                                                   ("I musei gratis sono una figata, punto.", "Slangy and absolute, with no context.")],
    "Formal introduction: context + issue.", "A formal opening names the issue and its importance before the position.",
    ["Context + debate → formal register."])

Q.frq(kind="Argumentative Essay", head=r"Question 3 \textperiodcentered\ Argumentative Essay \textperiodcentered\ 10 points \textperiodcentered\ 55 minutes", mins=55,
      directions=[r"Scrivi un saggio argomentativo per un corso universitario. Leggi il tema e le fonti scritte; poi ascolta la fonte audio (qui come trascrizione). Scrivi un saggio che usi informazioni tratte da tutte e tre le fonti per sostenere la tua posizione. Cita le fonti con il numero, il titolo o l'autore."],
      sources=[dict(title=r"Fonte 1 \textperiodcentered\ Articolo \textperiodcentered\ «La domenica in cui il museo si riempie»", paras=[
          r"Da quando i musei statali italiani sono gratuiti la prima domenica del mese, la Galleria Civica di Valmonte vive due mondi diversi. «Nei giorni normali abbiamo duecento visitatori; la domenica gratuita ne arrivano più di mille», racconta la direttrice, Chiara Neri.",
          r"Molti sono famiglie che non erano mai entrate in un museo. «Mio figlio ha visto un Caravaggio dal vivo per la prima volta», dice Paolo, operaio di 42 anni. «Con tre figli, il biglietto intero per tutti è una spesa che non possiamo fare spesso.»",
          r"Non tutti sono entusiasti. Le code arrivano fino alla piazza, le sale sono affollate e il personale è stanco. «Con i soldi dei biglietti paghiamo anche i restauri», ricorda la direttrice."]),
               dict(title=r"Fonte 2 \textperiodcentered\ Grafico \textperiodcentered\ Perché non visiti i musei più spesso?", paras=[
          r"Sondaggio su 1.500 adulti residenti in Italia (dati fittizi). Motivo principale indicato."],
                    table=(["Motivo", "Percentuale"], [["Il prezzo del biglietto", "38~\\%"], ["La mancanza di tempo", "31~\\%"], ["Lo scarso interesse", "19~\\%"], ["La distanza", "12~\\%"]])),
               dict(title=r"Fonte 3 \textperiodcentered\ Audio (trascrizione) \textperiodcentered\ Intervista a «Radio Cultura»", paras=[
          r"(GIORNALISTA) Oggi parliamo con l'economista della cultura Marco Ferri. Professore, i musei dovrebbero essere gratuiti per tutti?",
          r"(MARCO FERRI) La gratuità totale sembra generosa, ma qualcuno deve pagare: la manutenzione, la sicurezza, i restauri. Se i musei rinunciassero a tutti i biglietti, finirebbero per dipendere solo dai fondi pubblici, che spesso non bastano.",
          r"(GIORNALISTA) Che cosa propone, allora?",
          r"(MARCO FERRI) Biglietti gratuiti o molto ridotti per i giovani, gli studenti e chi ha un reddito basso, e un prezzo pieno per gli altri, compresi i turisti. Così il museo resta aperto a tutti senza impoverirsi."])],
      prompt=[r"Tema del saggio: \textbf{I musei pubblici dovrebbero essere gratuiti per tutti?}"],
      model=[r"In Italia, un Paese con un patrimonio artistico immenso, ci si chiede spesso chi debba pagare per la cultura. Sebbene un museo gratuito per tutti sembri l'ideale, ritengo che la soluzione migliore sia la gratuità per chi ne ha più bisogno, non per tutti.",
             r"Prima di tutto, il prezzo è davvero un ostacolo. Secondo il grafico della fonte 2, il 38~\% degli adulti indica il costo del biglietto come motivo principale per non visitare i musei, più della mancanza di tempo (31~\%). L'articolo della fonte 1 lo conferma: Paolo, operaio con tre figli, spiega che il biglietto intero per tutta la famiglia è una spesa che non può fare spesso. Questi dati dimostrano che, se il biglietto non ci fosse, molte famiglie scoprirebbero l'arte.",
             r"D'altra parte, la gratuità totale ha un costo. Come ricorda la direttrice della Galleria Civica di Valmonte nella fonte 1, i soldi dei biglietti servono anche a pagare i restauri. L'economista Marco Ferri, nella fonte 3, aggiunge che un museo senza biglietti dipenderebbe soltanto dai fondi pubblici, che spesso non bastano.",
             r"È vero che una regola uguale per tutti è più semplice. Tuttavia, le domeniche gratuite descritte nella fonte 1 mostrano anche i limiti di questo modello: code fino alla piazza e sale affollate. Per questo la proposta di Ferri mi sembra la più equilibrata: ingresso gratuito o ridotto per giovani, studenti e famiglie a basso reddito, prezzo pieno per gli altri, compresi i turisti.",
             r"In conclusione, i musei pubblici dovrebbero essere gratuiti per chi altrimenti non potrebbe entrarci, ma non per tutti. In questo modo l'arte resterebbe un bene comune e i musei avrebbero ancora le risorse per proteggerla."],
      rows=[("A Position", 1, "states a clear position that answers the question (a qualified one is fine)", "restates the topic or only lists both sides"),
            ("B Source use", 2, "uses all three sources correctly and names each one", "uses two sources (1 point) or misreads them"),
            ("C Argumentation", 2, "makes claims and explains how the evidence supports them", "summarizes sources without linking them to the position"),
            ("D Organization", 2, "introduction, paragraphs built around claims, conclusion; varied transitions", "source-by-source summary; no introduction or conclusion"),
            ("E Language control", 3, "wide vocabulary, varied structures (congiuntivo, periodo ipotetico, relative clauses), errors that do not impede", "basic sentences, copied phrases, errors that impede")],
      tips=["The position is qualified but clear (free for those who need it, not for everyone).", "Each body paragraph uses two sources, named by number.",
            "The counterargument paragraph concedes a point (è vero che) and answers it (tuttavia).", "The congiuntivo (debba, sembri, sia) and a periodo ipotetico (se … non ci fosse, scoprirebbero) show control."],
      ask="Write your essay in Italian (about 300–350 words), then mark it against each row.", lines=22)

GUIDE, QSET = G, Q
