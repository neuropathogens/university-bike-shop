from ap_wl.model import Doc

STEM = "00-exam-playbook"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Part 0: The Revised Exam and the Task Playbook", r"Part 0 \textperiodcentered\ Study Guide",
        abstract=r"""This guide is written for the revised AP French Language and Culture course (effective fall 2026) and its first exam, in May 2027, which runs entirely in Bluebook. It sets out what each of the three free-response questions and the nine multiple-choice task types asks you to do, how the free-response questions are scored, and the language that moves a response up a scoring row. Read it before the unit guides: every unit guide ends with a task kit that assumes the rubrics here. Sources: the College Board AP French exam page and the Course and Exam Description (CED), effective fall 2026. Check AP Central for any later change.""",
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

The pre-2027 exam's email reply, simulated conversation and cultural comparison are gone. Interpersonal speaking now happens in the Project Q\&A, and cultural comparison is one of two ways to earn its culture row. Spellings of the 1990 reform (\emph{la nouvelle orthographe}: \emph{connaitre}, \emph{evènement}) are not penalized.

\subsection{The six units}
\begin{terms}
1 Families and Communities & family relationships, community activities, social interactions, urban and rural life \\
2 Language and Culture & customs and celebrations, linguistics, French in the world (la francophonie) \\
3 Art and Creativity & artistic heritage, architecture, literature, fashion and design, visual and performing arts \\
4 Science and Technology & innovation, personal technology and communication, science in everyday life, societal impact \\
5 Contemporary Life & education and career, entertainment and media, food and health, pop culture, sports, travel \\
6 Global Contexts & global communication, the natural world, history, policy and planning, transportation \\
\end{terms}

\begin{keyidea}[What the units are for]
The exam does not test a unit by name. Multiple-choice sources and the essay topic can come from any theme and any part of the French-speaking world, from Quebec to Senegal to Belgium. The units are where you build the vocabulary and cultural knowledge every task draws on.
\end{keyidea}
""")
G.q("1 Format", r"On the revised exam, how much of the score does the Argumentative Essay carry?",
    r"15\%", [(r"25\%", "25% is the listening part or the reading part of the multiple choice."),
              (r"20\%", "20% is the Project Presentation."),
              (r"50\%", "50% is the whole free-response section: presentation 20%, Q&A 15%, essay 15%.")],
    "Essay: Q3, 55 min, 15%.", "The free-response section is 50%: Project Presentation 20%, Project Q&A 15%, Argumentative Essay 15%.",
    ["Free response = 50%.", "20 + 15 leaves 15% for the essay."])
G.q("1 Format", r"A student writes «~connaitre~» without the circumflex, following the 1990 spelling reform. On the AP exam this is",
    "accepted", [("penalized as a spelling error", "The exam page states that nouvelle orthographe spellings are not penalized."),
                 ("accepted only in Quebec", "The rule applies to all students."),
                 ("worth extra points", "It is simply accepted.")],
    "Nouvelle orthographe = not penalized.", "The College Board accepts the 1990 reform spellings (connaitre, evènement, nénufar) in the writing task.",
    ["Reform spelling → no penalty."])

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
                                            ("a recorded lecture on bilingual schools", "A lecture is a Presentation, a listening task.")],
    "Poster = Promotional Material.", "The reading section has four task types: Article, Article and Chart, Literary Text, Promotional Material.",
    ["A poster is read → Promotional Material."])

G.sec("Interpretive skills and question types")
G.tex(r"""
Every multiple-choice question tests one interpretive skill from the CED. The question sets in this series tag each item with one, so your score report shows which skill to work on.

\begin{compare}{Skill}{Question stems sound like}{How to answer}
1.A.1 Details & Selon l'article, \ldots~? / Qu'est-ce qui est mentionné\ldots~? & find the sentence; match meaning, not words \\
1.A.2 Data & Que montre le graphique~? & read units and dates; compare the right rows \\
1.B.1 Main idea, purpose & Quel est le but\ldots~? / l'idée principale & title, first and last paragraph \\
1.B.2 Audience & À qui s'adresse\ldots~? & who would act on it \\
1.B.3 Tone, point of view & Quelle est l'attitude de\ldots~? & evaluative words: \emph{hélas, enfin, sans doute} \\
1.B.4 Organization & Comment le texte est-il organisé~? & cause/effect, contrast, problem/solution markers \\
1.B.5 Word meaning & Que signifie\ldots~? & reread the sentence; test each choice in place \\
1.C.1 Connect sources & Qu'ont en commun\ldots~? & one fact from each source \\
1.C.2 Conclusions & Que peut-on conclure\ldots~? & supported by the text, not just plausible \\
1.C.3 Implied meaning & Que peut-on déduire\ldots~? & the most likely reason or consequence \\
\end{compare}

\begin{trap}
Wrong choices often repeat a word from the source with a different meaning, or say something true about the topic that the source never states. A choice is right only if the source supports it.
\end{trap}
""")
G.q("3 Skills", r"A question asks: Quel est le but principal de cette annonce~? Which skill does it test?",
    "determining the main idea or purpose", [("identifying data points", "No chart is involved."),
                                            ("determining the meaning of a word from context", "The question is about the whole ad."),
                                            ("connecting two sources", "There is one source.")],
    "But = purpose (1.B.1).", "Purpose questions (1.B.1) ask why the text exists: to inform, persuade, invite, warn.",
    ["but principal → purpose → 1.B.1."])
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
50--55 min & check agreement, past participles, accents, and that all three sources are named \\
\end{terms}

\begin{keyidea}[Citing sources]
Name a source by number, title or author: \emph{D'après la source 2, \ldots}, \emph{Comme l'explique l'article «~\ldots~», \ldots}, \emph{Le graphique montre que\ldots}, \emph{Dans l'extrait audio, la journaliste affirme que\ldots} Paraphrase; copied sentences earn nothing in the language row.
\end{keyidea}

\begin{trap}
A qualified position (\emph{oui, à condition que\ldots}) still earns Row A, as long as it answers the question. A position that only lists both sides does not.
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
The College Board releases the Course Project Packet in January of the exam year (January 2027) through the AP Digital Portfolio. For 2026--27 the project uses \textbf{music} as a lens on cultural products, practices and perspectives (the Unit 3 theme, Art and Creativity); you choose a focus within French-speaking communities, research it in class, and practice presenting.

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
A product (a song, an instrument, a festival) or a practice (singing in the street on June 21) earns the top culture score only when you say what it shows about what people value: \emph{Le 21 juin, tout le monde peut jouer dans la rue pendant la Fête de la musique, ce qui montre que la culture est considérée comme un bien partagé.}
\end{keyidea}
""")
G.q("5 Project", r"Which sentence best earns the top cultural understanding score in a presentation about music?",
    "Au Sénégal, les griots chantent l'histoire des familles lors des cérémonies, ce qui montre l'importance de la mémoire collective.",
    [("Les griots jouent de la kora, un instrument à 21 cordes.", "This describes a product but links it to no perspective."),
     ("J'aime beaucoup la musique africaine.", "A personal preference is not a cultural example."),
     ("J'ai trouvé beaucoup de sources pendant ma recherche.", "The research process earns nothing for culture.")],
    "Perspective + product/practice, linked.", "Row B's top score needs a specific example that ties a product or practice to the perspective behind it.",
    ["Practice: griots singing family history at ceremonies.", "Perspective: the value of collective memory.", "ce qui montre links them."])
G.q("5 Project", r"What may you do with your Personalized Project Reference during the presentation?",
    "glance at its keywords to stay organized", [("read a full script from it word for word", "The PPR is an outline; reading a script hurts delivery and may break the rules."),
                                                ("add new notes in the testing room", "You get the copy you submitted."),
                                                ("ask your teacher to rewrite it on exam morning", "It is due April 30 and must be your own work.")],
    "PPR = your submitted outline, printed for you.", "The PPR is a keyword outline submitted by April 30 and printed for you on exam day.",
    ["Use it to stay on track, not to read aloud."])

G.sec("Language control: structures that raise the score")
G.tex(r"""
The language rows (3 points in each free-response question) reward \emph{variety and control}. These structures show range in any topic.

\begin{compare}{Structure}{Use}{Example}
Subjunctive after necessity, emotion & il faut que, je souhaite que, je suis content que & Il faut que les jeunes \emph{puissent} découvrir la musique traditionnelle. \\
Subjunctive after conjunctions & bien que, pour que, avant que, à condition que & Bien que la ville \emph{soit} chère, beaucoup veulent y vivre. \\
Passé composé vs. imparfait & completed event vs. background or habit & Quand j'\emph{étais} petit, ma grand-mère m'\emph{a appris} une chanson. \\
Si-clauses & hypothetical: si + imparfait, conditionnel & Si les écoles \emph{proposaient} plus d'arts, les élèves \emph{participeraient} davantage. \\
Pronouns y, en & replace à + thing, de + thing / quantity & J'y pense souvent. Il en a parlé. \\
Relative pronouns & dont, ce que, lequel & C'est une tradition \emph{dont} je suis fier. \\
Agreement of the past participle & avoir + preceding direct object & Les chansons qu'elle a \emph{chantées}\ldots \\
\end{compare}

\begin{trap}
Variety does not mean forcing every structure in. One accurate subjunctive and one si-clause in context beat five broken ones; errors that impede comprehension cost more than plain sentences.
\end{trap}
""")
G.q("6 Subjonctif", r"Choose the correct form: Il faut que le gouvernement \blank\ plus de parcs.",
    "crée", [("créait", "The imparfait cannot follow il faut que."),
             ("créera", "Il faut que requires the subjunctive, not the future."),
             ("créer", "An infinitive fits only without que: il faut créer.")],
    "Il faut que + subjunctive.", "Expressions of necessity (il faut que, il est nécessaire que) take the subjunctive.",
    ["il faut que → subjonctif → crée."])
G.q("6 Si", r"Which sentence correctly expresses a hypothetical situation?",
    "Si j'avais plus de temps, j'apprendrais la guitare.", [("Si j'aurais plus de temps, j'apprendrais la guitare.", "Never use the conditional after si."),
                                                             ("Si j'ai plus de temps, j'apprendrais la guitare.", "Si + present pairs with the future, not the conditional."),
                                                             ("Si j'avais plus de temps, j'apprendrai la guitare.", "Si + imparfait pairs with the conditional, not the future.")],
    "Si + imparfait, conditionnel.", "Hypothetical: si + imparfait in the si clause, conditionnel présent in the result clause.",
    ["si j'avais … j'apprendrais."])

G.sec("Cohesive devices and register")
G.tex(r"""
\begin{compare}{Purpose}{Devices}{Example}
Add & de plus, en outre, par ailleurs, non seulement\ldots mais aussi & Non seulement c'est amusant, mais c'est aussi éducatif. \\
Contrast & cependant, en revanche, pourtant, bien que & En revanche, les villes manquent d'espace. \\
Cause/effect & car, puisque, en raison de, donc, par conséquent & En raison de la sécheresse, les prix ont augmenté. \\
Example & par exemple, notamment, comme le montre\ldots & Comme le montre le graphique, \ldots \\
Concede & certes\ldots, mais; il est vrai que\ldots, cependant & Certes, la technologie aide, mais elle isole aussi. \\
Conclude & en conclusion, en somme, pour conclure & En somme, les avantages l'emportent. \\
\end{compare}

\textbf{Register.} The essay is for a college course: use formal French, no slang (\emph{bouquin}, \emph{boulot}, \emph{trop bien}). In the Q\&A the interlocutor addresses you as \emph{tu} or \emph{vous}; answer in the same register and stay consistent.
""")
G.q("7 Cohesion", r"Which connector best introduces a contrasting idea in an essay?",
    "en revanche", [("par conséquent", "Par conséquent introduces a consequence."),
                    ("de plus", "De plus adds a point."),
                    ("par exemple", "Par exemple introduces an example.")],
    "En revanche = on the other hand.", "Contrast connectors: cependant, en revanche, pourtant, néanmoins.",
    ["Contrast → en revanche."])
G.q("7 Register", r"Which sentence best fits the register of the Argumentative Essay?",
    "À mon avis, il est essentiel que les villes investissent dans les transports en commun.", [("Franchement, le bus, c'est trop bien, quoi.", "Fillers and slang are too informal for a college essay."),
                                                                                                ("Moi, je kiffe le bus.", "Kiffer is slang."),
                                                                                                ("Vive le bus~!", "A slogan is not a position explained in formal prose.")],
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
        abstract=r"""Eighteen items on the structures that the language rows of all three free-response questions reward (the subjunctive, passé composé and imparfait, si-clauses, pronouns, past-participle agreement, relative pronouns and cohesive devices), followed by a full practice Argumentative Essay with three original sources and the 10-point scoring guide. All sources are original and fictional, written for practice. Allow about 15 minutes for the drill and 55 minutes for the essay.""",
        scoring=r"Drill: \blank\ / \qtotal \qquad Essay: \blank\ / 10 \qquad Target: 17+ drill and 7+ essay",
        short="Part 0", sub="Language Control Drill")

Q.sec("The subjunctive")
Q.q("6 Subjonctif", r"Mes parents veulent que je \blank\ médecin.",
    "devienne", [("deviens", "Vouloir que requires the subjunctive."),
                 ("devenir", "With a change of subject (parents → je), use que + subjunctive."),
                 ("deviendrai", "The future cannot follow vouloir que.")],
    "Vouloir que + new subject → subjunctive.", "Verbs of will and wish trigger the subjunctive when the subject changes.",
    ["veulent que, different subject → devienne."])
Q.q("6 Subjonctif", r"Je doute que cette loi \blank\ le problème.",
    "résolve", [("résout", "Douter que expresses doubt, which requires the subjunctive."),
                ("résoudra", "The future cannot follow douter que."),
                ("a résolu", "The passé composé indicative cannot follow douter que.")],
    "Doubt → subjunctive.", "Doubt and denial (je doute que, je ne crois pas que) take the subjunctive.",
    ["je doute que → résolve."])
Q.q("6 Subjonctif", r"Je pense que la musique \blank\ un rôle important dans les fêtes.",
    "joue", [("joues", "Joues is second person; la musique takes joue."),
             ("jouer", "A conjugated verb is needed after que."),
             ("jouât", "The imperfect subjunctive is literary and unwarranted here.")],
    "Penser que (affirmative) → indicative.", "Affirmative belief (je pense que, je crois que) takes the indicative; its negation takes the subjunctive.",
    ["je pense que → indicative → joue."])
Q.q("6 Subjonctif", r"Quand je \blank\ grand, je serai médecin.",
    "serai", [("suis", "A future event after quand takes the future in French."),
              ("sois", "Quand never takes the subjunctive."),
              ("serais", "The conditional does not fit a future plan stated as fact.")],
    "Quand + future event → future.", "Unlike English and Spanish, French uses the future (not the present or subjunctive) after quand, dès que and lorsque for future events.",
    ["future time → quand je serai."])

Q.sec("Passé composé and imparfait")
Q.q("6 Passé", r"Quand j'\blank\ petit, nous allions toujours chez ma grand-mère l'été.",
    "étais", [("ai été", "Age and background in the past take the imparfait."),
              ("fus", "The passé simple is literary and does not describe background."),
              ("serais", "The conditional is not a past description.")],
    "Background, age → imparfait.", "The imparfait describes ongoing states and habits in the past: j'étais petit, nous allions.",
    ["description of a past state → étais."])
Q.q("6 Passé", r"Nous dînions quand soudain le téléphone \blank.",
    "a sonné", [("sonnait", "Soudain marks a single interrupting event: passé composé."),
                ("sonne", "The narration is in the past."),
                ("sonnera", "The future does not fit.")],
    "Interrupting event → passé composé.", "An ongoing action (imparfait: nous dînions) is interrupted by a completed one (passé composé: a sonné).",
    ["soudain → completed event → a sonné."])
Q.q("6 Passé", r"L'année dernière, ma sœur \blank\ à jouer du violon.",
    "a appris", [("apprenait", "A completed accomplishment in a defined period takes the passé composé."),
                 ("apprend", "L'année dernière places the event in the past."),
                 ("apprendra", "The future contradicts l'année dernière.")],
    "Defined past period, completed → passé composé.", "L'année dernière frames a completed event.",
    ["a appris."])

Q.sec("Si-clauses and the conditional")
Q.q("6 Si", r"Si j'\blank\ de l'argent, je voyagerais au Sénégal.",
    "avais", [("aurais", "The conditional never follows si."),
              ("ai", "A present si clause pairs with the future, not voyagerais."),
              ("eus", "The passé simple does not express a hypothesis.")],
    "Si + imparfait, conditionnel.", "Hypothetical present: si + imparfait, then the conditionnel présent.",
    ["voyagerais (conditional) → si j'avais."])
Q.q("6 Si", r"S'il pleut demain, le concert \blank\ dans le gymnase.",
    "aura lieu", [("aurait lieu", "A likely condition with si + present takes the future, not the conditional."),
                  ("avait lieu", "The imparfait belongs in the si clause of a hypothesis."),
                  ("ait lieu", "The subjunctive does not follow si.")],
    "Real condition: si + present, future.", "Likely conditions: si + présent, result in the future, present or imperative.",
    ["s'il pleut (likely) → aura lieu."])

Q.sec("Pronouns and agreement")
Q.q("6 Pronoms", r"Tu as donné le cadeau à ta grand-mère~? — Oui, je \blank\ ai donné hier.",
    "le lui", [("lui le", "Le/la/les come before lui/leur."),
               ("la lui", "Le cadeau is masculine: le."),
               ("le leur", "Ta grand-mère is one person: lui.")],
    "le + lui.", "Order of object pronouns: me/te/se/nous/vous before le/la/les before lui/leur before y before en.",
    ["le cadeau → le; à ta grand-mère → lui."])
Q.q("6 Pronoms", r"Tu vas au festival~? — Oui, j'\blank\ vais samedi.",
    "y", [("en", "En replaces de + place (j'en viens); y replaces à + place."),
          ("le", "Le replaces a direct object, not a destination."),
          ("lui", "Lui replaces à + person.")],
    "à + place → y.", "Y replaces à (or en, dans, chez) + place or thing.",
    ["aller au festival → j'y vais."])
Q.q("6 Accord", r"Les chansons que ma grand-mère a \blank\ sont très anciennes.",
    "chantées", [("chanté", "With avoir, the participle agrees with a direct object placed before it (que = les chansons)."),
                 ("chantés", "Chansons is feminine."),
                 ("chantée", "Chansons is plural.")],
    "Preceding direct object → agreement.", "With avoir, the past participle agrees with a preceding direct object: les chansons qu'elle a chantées.",
    ["que = les chansons (f. pl.) → chantées."])

Q.sec("Relative pronouns")
Q.q("6 Relatifs", r"C'est une tradition \blank\ je suis très fier.",
    "dont", [("que", "Être fier de takes de, so the relative pronoun is dont."),
             ("qui", "Qui is a subject; je is the subject here."),
             ("où", "Où refers to place or time.")],
    "fier de → dont.", "Dont replaces de + noun: une tradition dont je suis fier (je suis fier de cette tradition).",
    ["être fier de → dont."])
Q.q("6 Relatifs", r"\blank\ m'a le plus surpris, c'est le nombre de jeunes au festival.",
    "Ce qui", [("Ce que", "Ce que is an object; here the clause needs a subject (ce qui m'a surpris)."),
               ("Qui", "Qui alone cannot introduce this clause."),
               ("Lequel", "Lequel refers back to a specific noun.")],
    "Ce qui = what (subject).", "Ce qui (subject) and ce que (object) introduce ideas with no specific antecedent.",
    ["what surprised me (subject of a surpris) → ce qui."])
Q.q("6 Relatifs", r"La ville \blank\ je suis né est au bord de la mer.",
    "où", [("dont", "Dont replaces de + noun; naître dans une ville → où."),
           ("que", "Que is a direct object."),
           ("qui", "Qui is a subject.")],
    "Place → où.", "Où is the relative pronoun of place and time.",
    ["la ville (place) → où."])

Q.sec("Cohesive devices")
Q.q("7 Cohésion", r"La ville a construit des pistes cyclables~; \blank, la circulation a baissé de 10~\%.",
    "par conséquent", [("en revanche", "En revanche introduces a contrast, but the second clause is a result."),
                       ("malgré cela", "This concedes an obstacle; the result is positive and expected."),
                       ("par exemple", "The second clause is not an example of the first.")],
    "Result → par conséquent / donc.", "Consequence connectors: donc, par conséquent, c'est pourquoi, ainsi.",
    ["bike lanes caused less traffic → result."])
Q.q("7 Cohésion", r"\blank\ la technologie facilite la communication, elle peut aussi isoler les gens.",
    "Bien que", [("Par conséquent", "This introduces a conclusion, not a concession."),
                 ("À cause de", "À cause de needs a noun and expresses cause."),
                 ("En somme", "En somme introduces a summary.")],
    "Bien que + subjunctive = although.", "Bien que concedes a point before the main claim (and takes the subjunctive: facilite is subjunctive too).",
    ["concession → bien que."])
Q.q("7 Registre", r"Which opening best suits the formal Argumentative Essay?",
    "La question de savoir si les écoles doivent interdire les téléphones suscite un vif débat.", [("Bon, ben, les portables, quoi.", "Fillers belong in casual speech."),
                                                                                                    ("Salut, prof~! Je vais te dire ce que je pense.", "Addressing the reader informally does not fit a college essay."),
                                                                                                    ("Les portables, c'est nul, point.", "Slangy and absolute, with no context.")],
    "Formal introduction: context + issue.", "A formal opening names the issue and its importance before the position.",
    ["Context + debate → formal register."])

Q.frq(kind="Argumentative Essay", head=r"Question 3 \textperiodcentered\ Argumentative Essay \textperiodcentered\ 10 points \textperiodcentered\ 55 minutes", mins=55,
      directions=[r"Vous allez écrire un essai argumentatif pour un cours universitaire. Lisez le sujet et les sources écrites~; ensuite, écoutez la source audio (ici, la transcription). Écrivez un essai qui intègre des éléments des trois sources pour soutenir votre position. Indiquez les sources utilisées par leur numéro, leur titre ou leur auteur."],
      sources=[dict(title=r"Source 1 \textperiodcentered\ Article \textperiodcentered\ «~Le collège qui a éteint les écrans~»", paras=[
          r"Il y a deux ans, le collège Jean-Moulin de Lyon a décidé que les élèves déposeraient leur téléphone dans un casier pendant toute la journée. Au début, les élèves ont protesté. «~On pensait que c'était une punition~», se souvient Inès, 15 ans.",
          r"Aujourd'hui, la principale, Mme Durand, présente d'autres chiffres~: les conflits dans la cour ont diminué de près de moitié, et le CDI est plein à l'heure du déjeuner. «~Les jeunes ont recommencé à se parler~», affirme-t-elle.",
          r"Tout le monde n'est pas convaincu. Certains parents regrettent de ne pas pouvoir joindre leurs enfants en cas d'urgence, et plusieurs professeurs regrettent les applications éducatives qu'ils utilisaient en classe."]),
               dict(title=r"Source 2 \textperiodcentered\ Graphique \textperiodcentered\ À quoi les élèves utilisent-ils leur téléphone à l'école~?", paras=[
          r"Enquête auprès de 1~200 élèves de France, de Belgique et du Québec (données fictives). Pourcentage qui réalise chaque activité au moins une fois par jour d'école."],
                    table=(["Activité", "Pourcentage"], [["Réseaux sociaux", "71~\\%"], ["Messages avec des amis", "68~\\%"], ["Recherches pour un cours", "44~\\%"], ["Applications de la classe", "29~\\%"], ["Appeler la famille", "12~\\%"]])),
               dict(title=r"Source 3 \textperiodcentered\ Audio (transcription) \textperiodcentered\ Entretien sur «~Radio Campus~»", paras=[
          r"(ANIMATRICE) Nous recevons le psychologue Marc Lefebvre. Faut-il interdire les téléphones à l'école~?",
          r"(MARC) Interdire, c'est la solution la plus simple, mais pas toujours la meilleure. Les jeunes vont utiliser leur téléphone toute leur vie~; l'école est l'endroit idéal pour apprendre à bien s'en servir. Je propose des règles claires~: le téléphone est rangé pendant les cours, sauf quand le professeur le demande pour une activité.",
          r"(ANIMATRICE) Et pendant les récréations~?",
          r"(MARC) Là, je recommande des espaces sans écrans. Les études montrent que le jeu et la conversation en face à face réduisent l'anxiété."])],
      prompt=[r"Sujet de l'essai~: \textbf{Les écoles doivent-elles interdire l'usage du téléphone portable pendant toute la journée~?}"],
      model=[r"Ces dernières années, de nombreuses écoles ont dû décider quoi faire des téléphones portables. Bien qu'une interdiction totale semble être une solution simple, je pense qu'il vaut mieux limiter leur usage par des règles claires que le supprimer complètement.",
             r"Tout d'abord, il est vrai que les écrans peuvent isoler les élèves. D'après la source 1, après que le collège Jean-Moulin a fait ranger les téléphones, les conflits dans la cour ont diminué de près de moitié et les élèves «~ont recommencé à se parler~». De plus, le graphique de la source 2 montre que 71~\% des élèves utilisent les réseaux sociaux chaque jour d'école, une activité qui a peu à voir avec l'apprentissage. Il est donc raisonnable que les récréations soient des espaces sans écrans, comme le recommande le psychologue de la source 3.",
             r"Cependant, une interdiction totale supprime des usages précieux. Le même graphique indique que 44~\% des élèves font des recherches pour un cours avec leur téléphone, et, dans la source 1, plusieurs professeurs regrettent les applications éducatives. Comme l'explique Marc Lefebvre dans la source 3, les jeunes utiliseront leur téléphone toute leur vie~; l'école devrait donc leur apprendre à bien s'en servir au lieu de le cacher.",
             r"Certains parents soulignent, à juste titre, qu'ils doivent pouvoir joindre leurs enfants en cas d'urgence (source 1). Une règle qui autorise le téléphone à des moments précis résout aussi ce problème.",
             r"En conclusion, si les écoles rangeaient les téléphones pendant les cours et les récréations, mais permettaient leur usage quand le professeur le demande, elles conserveraient les avantages du numérique sans perdre la convivialité que les élèves de Lyon ont retrouvée."],
      rows=[("A Position", 1, "states a clear position that answers the question (a qualified one is fine)", "restates the topic or only lists both sides"),
            ("B Source use", 2, "uses all three sources correctly and names each one", "uses two sources (1 point) or misreads them"),
            ("C Argumentation", 2, "makes claims and explains how the evidence supports them", "summarizes sources without linking them to the position"),
            ("D Organization", 2, "introduction, paragraphs built around claims, conclusion; varied transitions", "source-by-source summary; no introduction or conclusion"),
            ("E Language control", 3, "wide vocabulary, varied structures (subjunctive, si-clause), errors that do not impede", "basic sentences, copied phrases, errors that impede")],
      tips=["The position is qualified but clear (limit, not ban).", "Each body paragraph uses two sources, named by number.",
            "The counterargument paragraph concedes a point (à juste titre) and answers it.", "The conclusion uses a si-clause (si + imparfait, conditionnel)."],
      ask="Write your essay in French (about 300–350 words), then mark it against each row.", lines=22)

GUIDE, QSET = G, Q
