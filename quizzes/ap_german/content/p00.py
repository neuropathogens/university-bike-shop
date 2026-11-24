from ap_wl.model import Doc

STEM = "00-exam-playbook"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Part 0: The Revised Exam and the Task Playbook", r"Part 0 \textperiodcentered\ Study Guide",
        abstract=r"""This guide is written for the revised AP German Language and Culture course (effective fall 2026) and its first exam, in May 2027, which runs entirely in Bluebook. The revised German exam has the same structure as the revised French and Spanish exams: a course project presented and discussed in German, an Argumentative Essay, and 55 multiple-choice questions. This guide sets out what each task asks you to do, how the free-response questions are scored, and the language that moves a response up a scoring row. Read it before the unit guides: every unit guide ends with a task kit that assumes the rubrics here. Sources: the College Board AP world language revision pages and the Course and Exam Description (CED), effective fall 2026. Check AP Central for any later change.""",
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
2 Language and Culture & customs and celebrations, linguistics, German in the world \\
3 Art and Creativity & artistic heritage, architecture, literature, fashion and design, visual and performing arts \\
4 Science and Technology & innovation, personal technology and communication, science in everyday life, societal impact \\
5 Contemporary Life & education and career, entertainment and media, food and health, pop culture, sports, travel \\
6 Global Contexts & global communication, the natural world, history, policy and planning, transportation \\
\end{terms}

\begin{keyidea}[What the units are for]
The exam does not test a unit by name. Multiple-choice sources and the essay topic can come from any theme and any German-speaking country: Germany, Austria, Switzerland, Liechtenstein, Luxembourg. The units are where you build the vocabulary and cultural knowledge every task draws on.
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
    "a poster for a neighborhood festival", [("a radio report on a new tram line", "A radio report is an Audio Report, a listening task."),
                                            ("a recorded interview with a chef", "Interviews are listening sources."),
                                            ("a recorded lecture on dialects", "A lecture is a Presentation, a listening task.")],
    "Poster = Promotional Material.", "The reading section has four task types: Article, Article and Chart, Literary Text, Promotional Material.",
    ["A poster is read → Promotional Material."])

G.sec("Interpretive skills and question types")
G.tex(r"""
Every multiple-choice question tests one interpretive skill from the CED. The question sets in this series tag each item with one, so your score report shows which skill to work on.

\begin{compare}{Skill}{Question stems sound like}{How to answer}
1.A.1 Details & Laut dem Artikel\ldots? / Was wird über\ldots gesagt? & find the sentence; match meaning, not words \\
1.A.2 Data & Was zeigt die Grafik? & read units and dates; compare the right rows \\
1.B.1 Main idea, purpose & Was ist der Zweck\ldots? / das Hauptthema & title, first and last paragraph \\
1.B.2 Audience & An wen richtet sich\ldots? & who would act on it \\
1.B.3 Tone, point of view & Welche Einstellung hat\ldots? & evaluative words: \emph{leider, endlich, zweifellos} \\
1.B.4 Organization & Wie ist der Text aufgebaut? & cause/effect, contrast, problem/solution markers \\
1.B.5 Word meaning & Was bedeutet\ldots? & reread the sentence; test each choice in place \\
1.C.1 Connect sources & Was haben\ldots gemeinsam? & one fact from each source \\
1.C.2 Conclusions & Was kann man daraus schließen? & supported by the text, not just plausible \\
1.C.3 Implied meaning & Was kann man vermuten? & the most likely reason or consequence \\
\end{compare}

\begin{trap}
Wrong choices often repeat a word from the source with a different meaning, or say something true about the topic that the source never states. A choice is right only if the source supports it.
\end{trap}
""")
G.q("3 Skills", r"A question asks: Was ist der Hauptzweck dieser Anzeige? Which skill does it test?",
    "determining the main idea or purpose", [("identifying data points", "No chart is involved."),
                                            ("determining the meaning of a word from context", "The question is about the whole ad."),
                                            ("connecting two sources", "There is one source.")],
    "Zweck = purpose (1.B.1).", "Purpose questions (1.B.1) ask why the text exists: to inform, persuade, invite, warn.",
    ["Hauptzweck → purpose → 1.B.1."])
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
50--55 min & check word order (verb second; verb last after weil, dass, obwohl), case endings, and that all three sources are named \\
\end{terms}

\begin{keyidea}[Citing sources]
Name a source by number, title or author: \emph{Laut Quelle 2\ldots}, \emph{Wie der Artikel „\ldots“ zeigt, \ldots}, \emph{Die Grafik zeigt, dass\ldots}, \emph{Im Hörtext erklärt die Expertin, dass\ldots} Paraphrase; copied sentences earn nothing in the language row.
\end{keyidea}

\begin{trap}
A qualified position (\emph{ja, aber nur wenn\ldots}) still earns Row A, as long as it answers the question. A position that only lists both sides does not.
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
The College Board releases the Course Project Packet in January of the exam year (January 2027) through the AP Digital Portfolio. For 2026--27 the project uses \textbf{music} as a lens on cultural products, practices and perspectives (the Unit 3 theme, Art and Creativity); you choose a focus within German-speaking communities, research it in class, and practice presenting.

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
A product (a song, an instrument, a festival) or a practice (singing in a choir, playing in the village brass band) earns the top culture score only when you say what it shows about what people value: \emph{In vielen Dörfern spielt die Blaskapelle bei jedem Fest, was zeigt, wie wichtig Gemeinschaft und Tradition sind.}
\end{keyidea}
""")
G.q("5 Project", r"Which sentence best earns the top cultural understanding score in a presentation about music?",
    "In vielen bayerischen Dörfern spielt die Blaskapelle bei jedem Fest, was zeigt, wie wichtig den Menschen Gemeinschaft und Tradition sind.",
    [("Eine Blaskapelle hat Trompeten, Posaunen und eine Tuba.", "This describes a product but links it to no perspective."),
     ("Ich finde Blasmusik sehr schön.", "A personal preference is not a cultural example."),
     ("Ich habe für mein Projekt viele Quellen gefunden.", "The research process earns nothing for culture.")],
    "Perspective + product/practice, linked.", "Row B's top score needs a specific example that ties a product or practice to the perspective behind it.",
    ["Practice: the brass band at every village festival.", "Perspective: community and tradition.", "was zeigt links them."])
G.q("5 Project", r"What may you do with your Personalized Project Reference during the presentation?",
    "glance at its keywords to stay organized", [("read a full script from it word for word", "The PPR is an outline; reading a script hurts delivery and may break the rules."),
                                                ("add new notes in the testing room", "You get the copy you submitted."),
                                                ("ask your teacher to rewrite it on exam morning", "It is due April 30 and must be your own work.")],
    "PPR = your submitted outline, printed for you.", "The PPR is a keyword outline submitted by April 30 and printed for you on exam day.",
    ["Use it to stay on track, not to read aloud."])

G.sec("Language control: structures that raise the score")
G.tex(r"""
The language rows (3 points in each free-response question) reward \emph{variety and control}. In German, word order and case endings are where control shows first.

\begin{compare}{Structure}{Use}{Example}
Verb-final subordinate clauses & weil, dass, obwohl, wenn, damit & Viele Jugendliche ziehen in die Stadt, \emph{weil es dort mehr Arbeit gibt}. \\
Verb second, inversion & a fronted element moves the subject after the verb & \emph{Deshalb} ziehen viele in die Stadt. \\
Konjunktiv II & wishes, hypotheses, polite requests & Wenn die Schulen mehr Musikunterricht \emph{hätten}, \emph{würden} mehr Kinder ein Instrument lernen. \\
Perfekt vs. Präteritum & speech vs. written narration & Gestern \emph{habe} ich ein Konzert \emph{gehört}. / Als Kind \emph{spielte} sie Geige. \\
Passive & werden + participle & Das Fest \emph{wird} jedes Jahr im Herbst \emph{gefeiert}. \\
Relative clauses & der, die, das (verb last) & Das ist eine Tradition, \emph{die} viele Familien \emph{pflegen}. \\
Two-way prepositions & accusative for motion, dative for location & Ich gehe \emph{in den} Park. Ich bin \emph{im} Park. \\
\end{compare}

\begin{trap}
Variety does not mean forcing every structure in. One accurate Konjunktiv II and correct verb-final clauses beat five broken ones; errors that impede comprehension cost more than plain sentences.
\end{trap}
""")
G.q("6 Wortstellung", r"Choose the correct sentence: ``Many young people move to the city because there is more work there.''",
    "Viele junge Leute ziehen in die Stadt, weil es dort mehr Arbeit gibt.", [("Viele junge Leute ziehen in die Stadt, weil es gibt dort mehr Arbeit.", "After weil, the conjugated verb goes to the end."),
                                                                                ("Viele junge Leute ziehen in die Stadt, weil gibt es dort mehr Arbeit.", "Weil is a subordinating conjunction: verb last, not inversion."),
                                                                                ("Viele junge Leute in die Stadt ziehen, weil es dort mehr Arbeit gibt.", "In the main clause, the verb is second.")],
    "weil → verb last.", "Subordinating conjunctions (weil, dass, obwohl, wenn) send the conjugated verb to the end of their clause.",
    ["main clause verb second; weil-clause verb last."])
G.q("6 Konjunktiv", r"Which sentence correctly expresses a hypothetical situation?",
    "Wenn ich mehr Zeit hätte, würde ich Gitarre lernen.", [("Wenn ich mehr Zeit habe, würde ich Gitarre lernen.", "A real condition (habe) does not pair with würde."),
                                                             ("Wenn ich mehr Zeit hätte, ich würde Gitarre lernen.", "After a fronted wenn-clause, the verb (würde) comes first in the main clause."),
                                                             ("Wenn ich hätte mehr Zeit, würde ich Gitarre lernen.", "In the wenn-clause, the verb goes to the end.")],
    "Wenn + Konjunktiv II…, würde…", "Hypotheticals use Konjunktiv II in both clauses (hätte / würde + infinitive); the wenn-clause counts as the first position.",
    ["wenn ich … hätte, würde ich …"])

G.sec("Cohesive devices and register")
G.tex(r"""
\begin{compare}{Purpose}{Devices}{Example}
Add & außerdem, zudem, darüber hinaus, nicht nur\ldots sondern auch & Das ist nicht nur lustig, sondern auch lehrreich. \\
Contrast & aber, jedoch, dagegen, trotzdem, obwohl & Die Stadt ist teuer; trotzdem wollen viele dort leben. \\
Cause/effect & weil, da, denn, deshalb, daher, folglich & Es regnete kaum; deshalb stiegen die Preise. \\
Example & zum Beispiel, wie\ldots zeigt & Wie die Grafik zeigt, \ldots \\
Concede & zwar\ldots, aber; es stimmt, dass\ldots & Zwar hilft die Technik, aber sie isoliert auch. \\
Conclude & zusammenfassend, abschließend, insgesamt & Zusammenfassend überwiegen die Vorteile. \\
\end{compare}

\textbf{Word order with connectors.} \emph{Deshalb, trotzdem, außerdem} take the first position: the verb follows (\emph{Deshalb ziehen viele\ldots}). \emph{Weil, obwohl, dass} send the verb to the end. \emph{Denn, aber, und} change nothing.

\textbf{Register.} The essay is for a college course: formal German, no slang (\emph{krass}, \emph{voll}, \emph{Bock haben}). In the Q\&A the interlocutor addresses you as \emph{du} or \emph{Sie}; answer in the same register and stay consistent.
""")
G.q("7 Cohesion", r"Which sentence uses deshalb correctly?",
    "Es gibt kaum Arbeit im Dorf. Deshalb ziehen viele junge Leute weg.", [("Es gibt kaum Arbeit im Dorf. Deshalb viele junge Leute ziehen weg.", "Deshalb takes first position, so the verb must come next."),
                                                                            ("Es gibt kaum Arbeit im Dorf, deshalb viele junge Leute wegziehen.", "Deshalb is not a subordinating conjunction; the verb is not last."),
                                                                            ("Es gibt kaum Arbeit im Dorf. Deshalb weg ziehen viele junge Leute.", "The separable prefix weg goes to the end.")],
    "Deshalb + verb + subject.", "Adverbial connectors (deshalb, trotzdem, außerdem) occupy the first position; the verb is second.",
    ["Deshalb ziehen viele … weg."])
G.q("7 Register", r"Which sentence best fits the register of the Argumentative Essay?",
    "Meiner Meinung nach sollten die Städte mehr in den öffentlichen Nahverkehr investieren.", [("Der Bus ist halt voll cool, oder?", "Fillers and slang are too informal for a college essay."),
                                                                                                 ("Ich hab echt Bock auf Bus.", "Bock haben is slang."),
                                                                                                 ("Bus, Bus, hurra!", "A slogan is not a position explained in formal prose.")],
    "Formal, precise, no slang.", "The essay is written for a college course: formal register, precise vocabulary.",
    ["Formal opinion marker + Konjunktiv II (sollten)."])

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
        abstract=r"""Seventeen items on the structures that the language rows of all three free-response questions reward (word order, Konjunktiv II, cases and prepositions, Perfekt and Präteritum, relative clauses, the passive, and connectors), followed by a full practice Argumentative Essay with three original sources and the 10-point scoring guide. All sources are original and fictional, written for practice. Allow about 15 minutes for the drill and 55 minutes for the essay.""",
        scoring=r"Drill: \blank\ / \qtotal \qquad Essay: \blank\ / 10 \qquad Target: 16+ drill and 7+ essay",
        short="Part 0", sub="Language Control Drill")

Q.sec("Word order")
Q.q("6 Wortstellung", r"Ich glaube, dass die Musik eine wichtige Rolle \blank.",
    "spielt", [("spielen", "The subject die Musik is singular."),
               ("spielte es", "No pronoun is needed; the verb simply goes last."),
               ("gespielt", "A conjugated verb is needed.")],
    "dass → verb last, agreeing with the subject.", "In a dass-clause, the conjugated verb goes to the end and agrees with its subject.",
    ["die Musik (singular) … spielt."])
Q.q("6 Wortstellung", r"Choose the correct sentence.",
    "Obwohl es regnete, fand das Konzert im Park statt.", [("Obwohl es regnete, das Konzert fand im Park statt.", "After a fronted subordinate clause, the main verb comes first."),
                                                          ("Obwohl regnete es, fand das Konzert im Park statt.", "In the obwohl-clause, the verb goes last."),
                                                          ("Obwohl es regnete, fand statt das Konzert im Park.", "The separable prefix statt goes to the end.")],
    "Subordinate clause first → verb next.", "A fronted subordinate clause fills position one, so the main clause starts with the verb.",
    ["Obwohl … regnete, fand … statt."])
Q.q("6 Wortstellung", r"Morgen \blank\ wir mit dem Zug nach Wien.",
    "fahren", [("wir fahren", "After Morgen in first position, the verb comes second, before the subject."),
               ("gefahren", "A conjugated verb is needed."),
               ("fährt", "The subject wir needs fahren.")],
    "Verb second.", "In main clauses the conjugated verb is always the second element, whatever comes first.",
    ["Morgen (1) fahren (2) wir …"])

Q.sec("Konjunktiv II")
Q.q("6 Konjunktiv", r"Wenn ich reich \blank, würde ich um die Welt reisen.",
    "wäre", [("bin", "A hypothetical needs Konjunktiv II, not the present."),
             ("sei", "Sei is Konjunktiv I, used for reported speech, not for hypotheses."),
             ("war", "The Präteritum is not a hypothesis.")],
    "sein → wäre.", "Konjunktiv II of sein and haben is usually wäre and hätte, not würde + infinitive.",
    ["hypothetical + sein → wäre."])
Q.q("6 Konjunktiv", r"Choose the most polite request.",
    "Könnten Sie mir bitte helfen?", [("Helfen Sie mir!", "An imperative is direct, not polite."),
                                      ("Sie helfen mir.", "A statement, not a request."),
                                      ("Kannst du mir helfen?", "Informal du and indicative kannst.")],
    "Konjunktiv II for politeness.", "Konjunktiv II (könnten, würden, hätten gern) softens requests.",
    ["Könnten Sie … → polite."])

Q.sec("Cases and prepositions")
Q.q("6 Kasus", r"Ich schenke \blank\ Großmutter ein Buch.",
    "meiner", [("meine", "Schenken takes a dative person: meiner Großmutter."),
               ("meinen", "Großmutter is feminine; meinen would be masculine accusative or dative plural."),
               ("mein", "Großmutter is feminine.")],
    "Dative indirect object, feminine → meiner.", "The person who receives (indirect object) is in the dative: meiner Großmutter.",
    ["jemandem etwas schenken → dative."])
Q.q("6 Präpositionen", r"Wir gehen heute Abend in \blank\ Konzert.",
    "das", [("dem", "In with motion toward takes the accusative: in das (ins) Konzert."),
            ("der", "Konzert is neuter."),
            ("den", "Konzert is neuter, not masculine.")],
    "Motion → accusative.", "Two-way prepositions take the accusative for motion (wohin?) and the dative for location (wo?).",
    ["gehen (wohin?) → in das Konzert."])
Q.q("6 Präpositionen", r"Nach der Schule treffen wir uns \blank\ Park.",
    "im", [("in den", "Treffen in a place is location (wo?), so dative: im Park."),
           ("ins", "Ins is accusative (motion)."),
           ("in die", "Park is masculine; in die would be feminine accusative.")],
    "Location → dative.", "Wo? → dative: im (= in dem) Park.",
    ["sich treffen (wo?) → im Park."])

Q.sec("Perfekt and Präteritum")
Q.q("6 Vergangenheit", r"Gestern \blank\ ich mit meinen Freunden ins Kino gegangen.",
    "bin", [("habe", "Gehen is a verb of motion and forms the Perfekt with sein."),
            ("werde", "Werde + participle would form a future or passive, which contradicts gestern."),
            ("wurde", "Werden forms the passive or future.")],
    "Motion verbs → sein.", "Verbs of motion or change of state (gehen, fahren, werden) form the Perfekt with sein.",
    ["gegangen → bin."])
Q.q("6 Vergangenheit", r"Als ich ein Kind \blank, spielte ich jeden Tag Klavier.",
    "war", [("bin", "The clause describes the past."),
            ("wäre", "Konjunktiv II is hypothetical."),
            ("gewesen", "A conjugated verb is needed.")],
    "Als + Präteritum for a past period.", "Als introduces a single past period or event; sein is usually in the Präteritum (war).",
    ["als ich ein Kind war."])

Q.sec("Relative clauses and the passive")
Q.q("6 Relativ", r"Das ist der Musiker, \blank\ ich gestern getroffen habe.",
    "den", [("der", "The relative pronoun is the object of treffen: accusative den."),
            ("dem", "Treffen takes an accusative object."),
            ("die", "Musiker is masculine.")],
    "Relative pronoun: gender from the noun, case from its clause.", "Der Musiker (masculine) is the object of getroffen in the relative clause → den.",
    ["ich habe den Musiker getroffen → den."])
Q.q("6 Relativ", r"Die Stadt, in \blank\ ich geboren bin, liegt am Rhein.",
    "der", [("die", "In + location takes the dative: in der Stadt."),
            ("dem", "Stadt is feminine."),
            ("das", "Stadt is feminine.")],
    "in + dative, feminine → der.", "The preposition decides the case of the relative pronoun.",
    ["in der Stadt → in der."])
Q.q("6 Passiv", r"Das Oktoberfest \blank\ jedes Jahr in München gefeiert.",
    "wird", [("ist", "Ist gefeiert would be the state passive; a recurring action uses werden."),
             ("hat", "Haben does not form the passive."),
             ("werden", "Das Oktoberfest is singular.")],
    "werden + participle.", "The process passive uses werden + past participle.",
    ["wird … gefeiert."])

Q.sec("Cohesive devices")
Q.q("7 Kohäsion", r"Die Stadt baute neue Radwege; \blank\ sank der Autoverkehr um 10 Prozent.",
    "dadurch", [("trotzdem", "Trotzdem introduces a contrast, but the second clause is a result."),
                ("obwohl", "Obwohl is subordinating and would need the verb last."),
                ("zum Beispiel", "The second clause is not an example of the first.")],
    "Result → dadurch / deshalb.", "Consequence connectors: deshalb, daher, dadurch, folglich.",
    ["bike lanes caused less traffic → result."])
Q.q("7 Kohäsion", r"\blank\ die Technik die Kommunikation erleichtert, kann sie Menschen auch isolieren.",
    "Obwohl", [("Deshalb", "Deshalb would need the verb next, not last, and introduces a result."),
               ("Denn", "Denn means because and does not send the verb to the end."),
               ("Zusammenfassend", "This introduces a summary.")],
    "Obwohl = although.", "Obwohl concedes a point; the verb (erleichtert) goes to the end.",
    ["concession + verb last → obwohl."])
Q.q("7 Kohäsion", r"Choose the correct sentence with zwar\ldots aber.",
    "Zwar ist die Stadt teuer, aber das Kulturangebot ist groß.", [("Zwar die Stadt ist teuer, aber das Kulturangebot ist groß.", "Zwar takes first position: the verb must follow."),
                                                                    ("Zwar ist die Stadt teuer, aber ist das Kulturangebot groß.", "Aber does not cause inversion."),
                                                                    ("Zwar teuer die Stadt ist, aber das Kulturangebot groß ist.", "Neither clause has the verb second.")],
    "Zwar → verb second; aber → no change.", "Zwar fills first position; aber is a coordinating conjunction (position zero).",
    ["Zwar ist …, aber das … ist …"])
Q.q("7 Register", r"Which opening best suits the formal Argumentative Essay?",
    "Die Frage, ob Schulen Handys verbieten sollten, wird seit Jahren heftig diskutiert.", [("Also, Handys, na ja.", "Fillers belong in casual speech."),
                                                                                             ("Hallo, Lehrer! Ich sag dir jetzt meine Meinung.", "Addressing the reader informally does not fit a college essay."),
                                                                                             ("Handys sind voll nervig, Punkt.", "Slangy and absolute, with no context.")],
    "Formal introduction: context + issue.", "A formal opening names the issue and its importance before the position.",
    ["Context + debate → formal register."])

Q.frq(kind="Argumentative Essay", head=r"Question 3 \textperiodcentered\ Argumentative Essay \textperiodcentered\ 10 points \textperiodcentered\ 55 minutes", mins=55,
      directions=[r"Sie schreiben einen argumentativen Aufsatz für einen Universitätskurs. Lesen Sie das Thema und die schriftlichen Quellen; hören Sie dann die Audioquelle (hier als Transkript). Schreiben Sie einen Aufsatz, der Informationen aus allen drei Quellen verwendet, um Ihre Position zu unterstützen. Geben Sie die Quellen mit Nummer, Titel oder Autor an."],
      sources=[dict(title=r"Quelle 1 \textperiodcentered\ Artikel \textperiodcentered\ „Die Schule, die die Bildschirme abschaltete“", paras=[
          r"Vor zwei Jahren beschloss das Goethe-Gymnasium in Freiburg, dass die Schülerinnen und Schüler ihre Handys während des ganzen Schultags in einem Schließfach lassen müssen. Am Anfang gab es Proteste. „Wir dachten, es sei eine Strafe“, erinnert sich Lena, 16.",
          r"Heute präsentiert die Schulleiterin, Frau Becker, andere Zahlen: Die Konflikte auf dem Schulhof sind fast um die Hälfte zurückgegangen, und die Bibliothek ist in der Mittagspause voll. „Die Jugendlichen reden wieder miteinander“, sagt sie.",
          r"Nicht alle sind überzeugt. Einige Eltern bedauern, dass sie ihre Kinder im Notfall nicht erreichen können, und mehrere Lehrkräfte vermissen die Lern-Apps, die sie im Unterricht benutzt haben."]),
               dict(title=r"Quelle 2 \textperiodcentered\ Grafik \textperiodcentered\ Wofür nutzen Schüler ihr Handy in der Schule?", paras=[
          r"Umfrage unter 1.200 Schülerinnen und Schülern in Deutschland, Österreich und der Schweiz (fiktive Daten). Anteil, der die Tätigkeit mindestens einmal pro Schultag ausführt."],
                    table=(["Tätigkeit", "Anteil"], [["Soziale Netzwerke", "71~\\%"], ["Nachrichten an Freunde", "68~\\%"], ["Recherche für den Unterricht", "44~\\%"], ["Lern-Apps der Klasse", "29~\\%"], ["Anrufe bei der Familie", "12~\\%"]])),
               dict(title=r"Quelle 3 \textperiodcentered\ Audio (Transkript) \textperiodcentered\ Interview im „Schulradio“", paras=[
          r"(MODERATORIN) Heute ist der Psychologe Markus Weber bei uns. Herr Weber, sollte man Handys an Schulen verbieten?",
          r"(MARKUS WEBER) Ein Verbot ist die einfachste Lösung, aber nicht immer die beste. Junge Menschen werden ihr Leben lang ein Handy benutzen; die Schule ist der ideale Ort, um den richtigen Umgang damit zu lernen. Ich schlage klare Regeln vor: Im Unterricht bleibt das Handy weg, außer die Lehrkraft verlangt es für eine Aufgabe.",
          r"(MODERATORIN) Und in den Pausen?",
          r"(MARKUS WEBER) Da empfehle ich bildschirmfreie Zonen. Studien zeigen, dass Spielen und persönliche Gespräche Ängste verringern."])],
      prompt=[r"Thema des Aufsatzes: \textbf{Sollten Schulen Handys während des ganzen Schultags verbieten?}"],
      model=[r"In den letzten Jahren mussten viele Schulen entscheiden, wie sie mit Handys umgehen. Obwohl ein komplettes Verbot einfach erscheint, bin ich der Meinung, dass klare Regeln besser sind als ein Verbot für den ganzen Tag.",
             r"Zunächst stimmt es, dass Bildschirme Schülerinnen und Schüler isolieren können. Laut Quelle 1 sind die Konflikte auf dem Schulhof am Goethe-Gymnasium fast um die Hälfte zurückgegangen, seit die Handys im Schließfach bleiben, und die Jugendlichen „reden wieder miteinander“. Außerdem zeigt die Grafik in Quelle 2, dass 71~\% der Schüler jeden Schultag soziale Netzwerke nutzen, was mit Lernen wenig zu tun hat. Deshalb ist es sinnvoll, dass die Pausen bildschirmfrei sind, wie es der Psychologe in Quelle 3 empfiehlt.",
             r"Ein komplettes Verbot verhindert jedoch auch sinnvolle Nutzungen. Dieselbe Grafik zeigt, dass 44~\% der Schüler das Handy für Recherchen im Unterricht verwenden, und in Quelle 1 vermissen mehrere Lehrkräfte ihre Lern-Apps. Wie Markus Weber in Quelle 3 erklärt, werden junge Menschen ihr Leben lang ein Handy benutzen; die Schule sollte ihnen also den richtigen Umgang beibringen, statt das Handy zu verstecken.",
             r"Einige Eltern weisen zu Recht darauf hin, dass sie ihre Kinder im Notfall erreichen müssen (Quelle 1). Eine Regel, die das Handy zu bestimmten Zeiten erlaubt, löst auch dieses Problem.",
             r"Zusammenfassend lässt sich sagen: Wenn Schulen die Handys im Unterricht und in den Pausen wegschließen und sie nur für bestimmte Aufgaben erlauben würden, könnten sie die Vorteile des digitalen Lernens nutzen, ohne das Miteinander zu verlieren, das die Freiburger Schüler wiedergefunden haben."],
      rows=[("A Position", 1, "states a clear position that answers the question (a qualified one is fine)", "restates the topic or only lists both sides"),
            ("B Source use", 2, "uses all three sources correctly and names each one", "uses two sources (1 point) or misreads them"),
            ("C Argumentation", 2, "makes claims and explains how the evidence supports them", "summarizes sources without linking them to the position"),
            ("D Organization", 2, "introduction, paragraphs built around claims, conclusion; varied transitions", "source-by-source summary; no introduction or conclusion"),
            ("E Language control", 3, "wide vocabulary, varied structures (verb-final clauses, Konjunktiv II), errors that do not impede", "basic sentences, copied phrases, errors that impede")],
      tips=["The position is qualified but clear (rules, not a full ban).", "Each body paragraph uses two sources, named by number.",
            "The counterargument paragraph concedes a point (zu Recht) and answers it.", "The conclusion uses Konjunktiv II (würden, könnten) and correct verb-final clauses."],
      ask="Write your essay in German (about 300–350 words), then mark it against each row.", lines=22)

GUIDE, QSET = G, Q
