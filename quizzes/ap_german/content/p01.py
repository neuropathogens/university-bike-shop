from ap_wl.model import Doc

STEM = "01-families-communities"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 1: Families and Communities", r"Unit 1 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 1 asks what makes a family, how families shape values and traditions, and how communities are changing. Its recommended contexts are family relationships, community activities, social interactions and relationships, and urban and rural communities. This guide gives the vocabulary the exam assumes, the structures for describing relationships and routines, the cultural products, practices and perspectives most often tested (parental leave and childcare, clubs and volunteer fire brigades, multigenerational houses, local democracy in Switzerland, rural flight), and an Argumentative Essay kit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Words I keep forgetting: \blank[10em]",
        short="Unit 1", sub="Families and Communities")

G.sec("Family and relationships")
G.tex(r"""
\begin{vocab}
die Verwandten / die Angehörigen & relatives / family members & \\
die Patchworkfamilie & blended family & \\
alleinerziehend & single (parent) & \emph{eine alleinerziehende Mutter} \\
die Elternzeit / das Elterngeld & parental leave / parental allowance & Germany, since 2007 \\
die Kita (Kinder\-tages\-stätte) & daycare & a legal right to a place from age one (since 2013) \\
erziehen / die Erziehung & to raise / upbringing & \\
sich um jemanden kümmern & to look after someone & \emph{sich um die Enkel kümmern} \\
sich gut verstehen mit & to get along well with & \\
ausziehen / ``Hotel Mama'' & to move out / living at home as an adult & \\
\end{vocab}

\textbf{Products, practices, perspectives.} Germany's paid parental leave (Elterngeld) can be shared between both parents, with extra months if fathers take part. The policy reflects a perspective that raising children is a shared responsibility of both parents and of society. Sunday afternoon \emph{Kaffee und Kuchen} with the family remains a common ritual.
""")
G.q("1 Familie", r"Was ist eine Patchworkfamilie?",
    "eine Familie, in der mindestens ein Elternteil Kinder aus einer früheren Beziehung hat", [("eine Familie mit drei Generationen unter einem Dach", "That is a Mehrgenerationenfamilie."),
                                                                                             ("eine Familie mit nur einem Elternteil", "That is an alleinerziehende Familie."),
                                                                                             ("eine Familie, die oft umzieht", "Unrelated.")],
    "Patchwork = blended.", "A Patchworkfamilie brings together children from previous relationships.",
    ["patchwork → pieces joined → blended family."])
G.q("1 Familie", r"Choose the best word: Meine Großeltern \blank\ sich mittwochs um meine kleinen Geschwister.",
    "kümmern", [("pflegen", "Pflegen takes a direct object without sich um."),
                ("erziehen", "Erziehen does not take sich um."),
                ("bleiben", "Sich um … bleiben is not a structure.")],
    "sich kümmern um = to look after.", "Sich um jemanden kümmern = to look after someone.",
    ["sich … um → kümmern."])
G.q("1 Familie", r"Which perspective does Germany's shared parental allowance, with extra months when fathers take part, most directly reflect?",
    "Raising children is the responsibility of both parents.", [("Only mothers should care for babies.", "The extra months encourage fathers."),
                                                               ("Children should start school at age one.", "Unrelated."),
                                                               ("Grandparents should pay for childcare.", "Unrelated.")],
    "Policy ↔ shared parenting.", "A product (the law) linked to a perspective (equal parenting) earns culture credit.",
    ["extra months for fathers → shared responsibility."])

G.sec("Community and social life")
G.tex(r"""
\begin{vocab}
der Verein / das Vereinsleben & club, association / club life & Germany has more than 600,000 registered clubs \\
das Ehrenamt / ehrenamtlich & volunteer work / as a volunteer & \\
die Freiwillige Feuerwehr & volunteer fire brigade & most German firefighters are volunteers \\
das Mehrgenerationenhaus & multigenerational community center & young and old meet and help each other \\
die Nachbarschaft / die Nachbarn & neighborhood / neighbors & \\
die Gemeindeversammlung & communal assembly & citizens vote directly in many Swiss communes \\
das Schützenfest & marksmen's festival & a village tradition in parts of Germany \\
\end{vocab}

\textbf{Clubs and volunteering.} Sports clubs, choirs, volunteer fire brigades and carnival clubs organize much of community life. The perspective: community is built by citizens who give their time, not only by the state. In many Swiss communes, residents decide local budgets and projects themselves in an assembly.
""")
G.q("2 Gemeinschaft", r"Was ist eine Freiwillige Feuerwehr?",
    "eine Feuerwehr, deren Mitglieder ehrenamtlich arbeiten", [("eine Feuerwehr, die nur Freiwillige rettet", "Literal misreading."),
                                                              ("eine private Firma für Feuerschutz", "It is public and volunteer."),
                                                              ("ein Fest mit Feuerwerk", "Unrelated.")],
    "Freiwillig = voluntary.", "Volunteer fire brigades protect most German towns and villages.",
    ["freiwillig → ehrenamtlich."])
G.q("2 Gemeinschaft", r"In many Swiss communes, citizens vote on local budgets in a Gemeindeversammlung. Which perspective does this practice reflect?",
    "Citizens should decide local matters directly.", [("Only national leaders should make decisions.", "The opposite."),
                                                      ("Taxes should be decided by companies.", "No."),
                                                      ("Local matters are unimportant.", "The opposite.")],
    "Direct democracy.", "Practice (assembly vote) ↔ perspective (citizens govern themselves).",
    ["citizens vote directly → direct democracy."])

G.sec("Urban and rural communities")
G.tex(r"""
\begin{vocab}
das Land / auf dem Land & the countryside / in the country & \\
die Landflucht & rural flight & \\
der Pendler / pendeln & commuter / to commute & \\
der Dorfladen & village shop, often run by residents & \\
die Miete / die Wohnungsnot & rent / housing shortage & \\
die WG (Wohngemeinschaft) & shared flat & common for students \\
das Homeoffice & remote work & \\
\end{vocab}

\textbf{Causes and effects.} Young people leave villages for universities and jobs; the shops, doctors and bus lines that remain become fewer. In some villages, residents have founded cooperative \emph{Dorfläden} to keep a shop open. In big cities, rising rents push students and families into shared flats or into the suburbs.
""")
G.q("3 Land", r"In einem Artikel: „Seit die Schule geschlossen hat, sind viele junge Familien in die Stadt gezogen.“ Wie hängen die beiden Ideen zusammen?",
    "Ursache und Folge", [("Gegensatz", "No opposing ideas; one event explains the other."),
                          ("Beispiel", "The second clause is not an example of the first."),
                          ("Anleitung", "This is narration, not instructions.")],
    "Seit → cause, then effect.", "Organization questions (1.B.4) ask how ideas relate.",
    ["school closed → families moved."])
G.q("3 Land", r"Why have residents of some German villages founded their own Dorfläden?",
    "to keep a local shop open when commercial stores close", [("to sell souvenirs to tourists", "The purpose is basic supplies."),
                                                              ("to compete with city banks", "Unrelated."),
                                                              ("to replace the school", "Unrelated.")],
    "Cooperative village shops.", "A community response to rural decline: residents run the shop themselves.",
    ["shops close → residents organize."])

G.sec("Structures for relationships and routines")
G.tex(r"""
\begin{compare}{Structure}{Use}{Example}
seit + present & how long something has gone on & Wir wohnen seit zehn Jahren in diesem Viertel. \\
gerade / gerade erst & just now & Meine Schwester ist gerade ausgezogen. \\
reflexive verbs & sich treffen, sich verstehen & Die Nachbarn helfen sich gegenseitig. \\
Comparative & als / so\ldots wie & Das Leben auf dem Land ist ruhiger als in der Stadt. \\
während & while, background & Während meine Mutter arbeitete, passte meine Oma auf uns auf. \\
damit / um\ldots zu & purpose & Sie sparen, damit ihre Kinder studieren können. \\
\end{compare}

\begin{trap}
English \emph{We have lived here for ten years} uses a perfect tense; German uses the present with \emph{seit}: \emph{Wir wohnen seit zehn Jahren hier}.
\end{trap}
""")
G.q("4 Strukturen", r"Choose the best way to say: ``We have been living in this neighborhood for ten years.''",
    "Wir wohnen seit zehn Jahren in diesem Viertel.", [("Wir haben seit zehn Jahren in diesem Viertel gewohnt.", "With seit and an ongoing situation, German uses the present."),
                                                       ("Wir wohnen für zehn Jahren in diesem Viertel.", "Für does not express ongoing duration."),
                                                       ("Wir wohnten vor zehn Jahren in diesem Viertel.", "Vor zehn Jahren means ten years ago.")],
    "present + seit.", "Ongoing actions that began in the past: present tense + seit.",
    ["still living there → present + seit."])
G.q("4 Strukturen", r"Meine Eltern arbeiten viel, \blank\ wir studieren können.",
    "damit", [("um", "Um … zu needs the same subject and an infinitive; here the subjects differ."),
              ("weil", "Weil gives a reason, not a purpose."),
              ("deshalb", "Deshalb would need verb-second word order.")],
    "Different subjects → damit.", "Purpose: um … zu when the subject is the same, damit when it changes.",
    ["parents work / we study → damit."])
G.q("4 Strukturen", r"Das Leben auf dem Land ist ruhiger \blank\ in der Stadt.",
    "als", [("wie", "Wie follows so + adjective (so ruhig wie); a comparative takes als."),
            ("dann", "Dann means then."),
            ("wenn", "Wenn means if or when.")],
    "Comparative + als.", "ruhiger als; so ruhig wie.",
    ["ruhiger → als."])

G.sec("Task kit: the Argumentative Essay")
G.tex(r"""
Unit 1 essay topics ask about family roles and community life: \emph{Sollten Großeltern regelmäßig ihre Enkel betreuen?}, \emph{Lebt man besser in der Stadt oder auf dem Land?}, \emph{Sollte ein soziales Jahr Pflicht sein?}

\begin{compare}{Move}{Phrases}{Example}
Position & Meiner Meinung nach / Ich bin der Ansicht, dass & Ich bin der Ansicht, dass ein soziales Jahr freiwillig bleiben sollte. \\
Evidence & Laut Quelle 1 / Die Grafik zeigt, dass & Die Grafik zeigt, dass nur 18~\% der Jugendlichen\ldots \\
Explain & Das zeigt, dass / Daraus folgt, dass & Das zeigt, dass Motivation wichtiger ist als Zwang. \\
Concede & Zwar\ldots, aber / Es stimmt, dass\ldots; jedoch & Zwar brauchen viele Dörfer Hilfe, aber\ldots \\
Conclude & Zusammenfassend / Aus all diesen Gründen & Aus all diesen Gründen\ldots \\
\end{compare}
""")
G.q("5 Aufsatz", r"Which sentence best explains a piece of evidence, as the argumentation row requires?",
    r"Laut Quelle 2 haben 60~\% der Freiwilligen nach dem Programm weitergeholfen, was zeigt, dass die Erfahrung langfristiges Engagement schafft.",
    [("Quelle 2 enthält eine Grafik über Freiwillige.", "Naming a source without using its content earns nothing."),
     ("Ehrenamt ist sehr gut und sehr wichtig.", "A claim with no evidence."),
     (r"Laut Quelle 2 haben 60~\% der Freiwilligen weitergeholfen.", "Evidence without explanation; the link to the position is missing.")],
    "Claim + evidence + explanation.", "Row C rewards explaining how the evidence supports the claim (was zeigt, dass…).",
    ["Evidence: 60%.", "Explanation: was zeigt, dass…"])
G.q("5 Aufsatz", r"Which transition best introduces a counterargument before rebutting it?",
    "Zwar", [("Deshalb", "Deshalb draws a conclusion."),
             ("Außerdem", "Außerdem adds a point on the same side."),
             ("Zuerst", "Zuerst begins a list of your own points.")],
    "Concede, then rebut.", "Zwar…, aber… concedes a point and answers it, which strengthens the argument.",
    ["Counterargument → zwar … aber."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 1: Families and Communities: Question Set", r"Unit 1 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Audio Report and an Interview for listening, an Article and Chart and a Promotional Material for reading) on grandparents and childcare, village life and volunteering, followed by an Argumentative Essay with three sources and the 10-point scoring guide. As on the exam, questions and choices are in German. Listening sources are printed as transcripts: read each once at normal speed, then answer without rereading. All sources and data are original and fictional, written for practice. Allow about 25 minutes for the multiple choice and 55 minutes for the essay.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Essay: \blank\ / 10 \qquad Target: 15+ MCQ and 7+ essay \qquad Pace: 75 s per item",
        short="Unit 1", sub="Families and Communities")

Q.sec("Listening: Audio Report")
Q.src(r"Listening 1 \textperiodcentered\ Audio Report (transcript) \textperiodcentered\ „Oma und Opa als Betreuer“, Radio Info", [
    r"(REPORTER) In Deutschland betreuen Großeltern fast jedes zweite Kind unter sechs Jahren regelmäßig, so eine neue Studie. Besonders in Städten, wo Kita-Plätze knapp sind, springen sie oft ein.",
    r"(REPORTER) Für viele Familien ist der Grund vor allem praktisch: Die Öffnungszeiten der Kitas passen nicht immer zu den Arbeitszeiten der Eltern. Aber es geht nicht nur um Organisation. Viele Eltern wünschen sich, dass ihre Kinder eine enge Beziehung zu den Großeltern haben.",
    r"(GROSSMUTTER, HELGA) Ich hole meine beiden Enkel jeden Dienstag und Donnerstag von der Kita ab. Das ist anstrengend, ehrlich gesagt, aber ich fühle mich gebraucht. Und ich singe mit ihnen die Lieder, die meine Mutter mir vorgesungen hat.",
    r"(REPORTER) Fachleute erinnern allerdings daran, dass auch Großeltern Pausen brauchen. Sie empfehlen, dass Gemeinden Angebote wie Großelterncafés schaffen, in denen sich betreuende Großeltern austauschen und erholen können.",
], 5)
Q.q("1.B.1 Main idea", r"Worum geht es hauptsächlich in dem Bericht?",
    "um die Rolle der Großeltern bei der Betreuung kleiner Kinder", [("um die steigende Geburtenrate in Deutschland", "Births are not discussed."),
                                                                    ("um die Geschichte deutscher Kinderlieder", "Songs are one detail Helga mentions."),
                                                                    ("um eine Reform der Schulen", "Schools are not discussed.")],
    "Main idea: grandparents as caregivers.", "The report opens with the statistic, gives reasons, a testimony and expert advice, all about grandparents caring for children.",
    ["Opening statistic + every segment → grandparents caring for grandchildren."])
Q.q("1.A.1 Detail", r"Welchen praktischen Grund nennt der Bericht?",
    "Die Öffnungszeiten der Kitas passen nicht immer zu den Arbeitszeiten.", [("Die Kitas sind zu teuer geworden.", "Cost is not the reason given."),
                                                                             ("Die Großeltern wohnen bei den Familien.", "Not stated."),
                                                                             ("Die Kinder wollen nicht in die Kita.", "Not stated.")],
    "Öffnungszeiten vs. Arbeitszeiten.", "Detail (1.A.1).",
    ["Die Öffnungszeiten der Kitas passen nicht immer zu den Arbeitszeiten."])
Q.q("1.B.3 Attitude", r"Welche Einstellung hat Helga zu ihrer Rolle als Großmutter?",
    "Sie findet sie anstrengend, aber erfüllend.", [("Sie macht es nur aus Pflicht und will aufhören.", "She says she feels needed."),
                                                   ("Sie findet es leicht und erholsam.", "She says it is tiring."),
                                                   ("Sie möchte, dass die Enkel länger in der Kita bleiben.", "She never says so.")],
    "anstrengend … aber ich fühle mich gebraucht.", "Attitude questions (1.B.3) weigh both parts of a mixed statement.",
    ["anstrengend → tiring.", "gebraucht → fulfilling."])
Q.q("1.C.3 Inference", r"Was kann man über die Lieder vermuten, die Helga mit ihren Enkeln singt?",
    "Sie geben eine Familientradition weiter.", [("Sie hat sie in einem Kurs der Gemeinde gelernt.", "She learned them from her mother."),
                                                ("Es sind neue Lieder aus dem Radio.", "They are songs her mother sang."),
                                                ("Die Enkel wollen sie nicht lernen.", "Nothing suggests that.")],
    "From her mother → tradition passed down.", "Inference (1.C.3): songs passed across three generations carry family tradition.",
    ["die Lieder, die meine Mutter mir vorgesungen hat → three generations."])
Q.q("1.A.1 Detail", r"Was empfehlen die Fachleute?",
    "dass Gemeinden Treffpunkte wie Großelterncafés schaffen", [("dass Großeltern nicht mehr betreuen", "They recommend support, not stopping."),
                                                               ("dass Eltern weniger arbeiten", "Not mentioned."),
                                                               ("dass Kitas billiger werden", "Not mentioned.")],
    "Großelterncafés.", "The recommendation is in the last segment.",
    ["Sie empfehlen, dass Gemeinden … Großelterncafés schaffen…"])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 1 \textperiodcentered\ Article and Chart \textperiodcentered\ „Zurück aufs Dorf“, Magazin Heimat", [
    r"Jahrzehntelang war die Geschichte vieler Dörfer in Ostdeutschland dieselbe: Die jungen Leute gingen zum Studium in die Stadt und kamen nicht zurück. Heute haben viele Gemeinden weniger als 500 Einwohner, und in manchen gibt es weder Bäcker noch Arzt.",
    r"Doch langsam ändert sich etwas. Seit 2020 hat das Homeoffice einigen Familien erlaubt, aufs Land zu ziehen, ohne ihre Arbeit zu verlieren. In Wiesenfeld, einem Dorf mit 300 Einwohnern, öffnete die Grundschule, die schließen sollte, im letzten Jahr mit elf neuen Kindern.",
    r"„Das ist keine Massenbewegung“, warnt die Geografin Katrin Vogel. „Ohne schnelles Internet, Ärzte und Busverbindungen ziehen die neuen Familien nach zwei, drei Jahren wieder weg.“ Für sie hängt die Zukunft der Dörfer weniger von Nostalgie ab als von Dienstleistungen.",
], 5, table=(["Jahr", "Von der Stadt aufs Dorf", "Vom Dorf in die Stadt"],
             [["2018", "41.000", "96.000"], ["2020", "73.000", "88.000"], ["2022", "82.000", "84.000"], ["2024", "79.000", "86.000"]]),
      note="Umzüge zwischen Gemeinden unter 5.000 Einwohnern und Städten (fiktive Daten).")
Q.q("1.B.1 Purpose", r"Was ist der Hauptzweck des Artikels?",
    "eine neue Entwicklung auf dem Land und ihre Grenzen darzustellen", [("die Leser zu überzeugen, nach Wiesenfeld zu ziehen", "It reports and analyzes; it does not persuade."),
                                                                         ("junge Leute zu kritisieren, die studieren", "The first paragraph describes the past without criticism."),
                                                                         ("zu erklären, wie Homeoffice funktioniert", "Remote work is a cause, not the subject.")],
    "Change + its limits.", "The article sets up the old pattern, shows a recent change, then qualifies it.",
    ["Paragraph 2: Doch langsam ändert sich etwas.", "Paragraph 3: keine Massenbewegung."])
Q.q("1.A.2 Data", r"In welchem Jahr war laut Grafik der Unterschied zwischen beiden Umzugsrichtungen am kleinsten?",
    "2022", [("2018", "In 2018 the gap was the largest: 96,000 vs. 41,000."),
             ("2020", "In 2020 the gap was 15,000."),
             ("2024", "In 2024 the gap was 7,000, larger than in 2022.")],
    "2022: 84,000 − 82,000 = 2,000.", "Data questions (1.A.2): compute each year's gap and compare.",
    ["Gaps: 55,000; 15,000; 2,000; 7,000."])
Q.q("1.C.1 Connect", r"Welche Information aus dem Artikel erklärt die Daten der Grafik ab 2020?",
    "Das Homeoffice erlaubte einigen Familien, aufs Land zu ziehen.", [("Viele Gemeinden haben weniger als 500 Einwohner.", "This describes the situation, not the change."),
                                                                       ("In manchen Dörfern gibt es keinen Bäcker.", "This explains decline, not the rise after 2020."),
                                                                       ("Die jungen Leute gingen zum Studium in die Stadt.", "This is the old pattern.")],
    "Seit 2020 hat das Homeoffice…", "Connect (1.C.1): the chart's jump after 2020 matches the article's cause.",
    ["Chart: 41,000 → 73,000 by 2020.", "Article: Seit 2020 … Homeoffice."])
Q.q("1.B.3 Point of view", r"Welche Meinung vertritt die Geografin Katrin Vogel?",
    "Neue Familien bleiben nur, wenn es grundlegende Dienstleistungen gibt.", [("Nostalgie wird die Menschen zurückbringen.", "She says the future depends less on nostalgia."),
                                                                              ("Die Dörfer haben ihre Probleme schon gelöst.", "She says it is not a mass movement."),
                                                                              ("Dorfschulen sollten schließen.", "She never says so.")],
    "Dienstleistungen > Nostalgie.", "Point of view (1.B.3): her quotes stress internet, doctors and buses.",
    ["Ohne schnelles Internet, Ärzte und Busverbindungen ziehen … wieder weg."])
Q.q("1.B.5 Word meaning", r"Im Artikel bedeutet „ziehen … wieder weg“",
    "verlassen den Ort wieder", [("heiraten", "Wegziehen means to move away."),
                                 ("beschweren sich", "Sich beschweren means to complain."),
                                 ("bleiben", "The opposite.")],
    "wegziehen = move away.", "Word meaning (1.B.5): the sentence contrasts arriving families with those who leave.",
    ["die neuen Familien … ziehen wieder weg → leave."])

Q.sec("Reading: Promotional Material")
Q.src(r"Reading 2 \textperiodcentered\ Promotional Material \textperiodcentered\ Ein Flyer der Stadt", [
    r"\textbf{Dein Viertel braucht dich! Programm „Nachbarn helfen Nachbarn“}",
    r"Du bist über 16 und hast ein paar Stunden pro Woche Zeit? Werde Teil unseres Ehrenamt-Netzwerks. Du kannst ältere Menschen besuchen, die allein leben, im Gemeinschaftsgarten helfen oder Kindern aus dem Viertel Nachhilfe geben.",
    r"\textbf{Was wir bieten:} eine kostenlose Schulung, eine Bescheinigung über deine ehrenamtlichen Stunden (nützlich für Bewerbungen und Stipendien) und die Chance, deine Nachbarn kennenzulernen.",
    r"\textbf{So machst du mit:} Melde dich bis zum 15. Oktober im Bürgerzentrum (Rathausstraße 12) oder auf nachbarnhelfen.de an. Die Aktivitäten beginnen am 1. November. Begrenzte Plätze.",
], 5)
Q.q("1.B.2 Audience", r"An wen richtet sich der Flyer vor allem?",
    "an Bewohner des Viertels, die über 16 sind", [("an ältere Menschen, die Gesellschaft suchen", "They are the people helped, not the audience recruited."),
                                                    ("an Lehrkräfte, die eine Stelle suchen", "It recruits unpaid volunteers."),
                                                    ("an Firmen, die Aktivitäten finanzieren wollen", "No sponsorship is mentioned.")],
    "Du bist über 16…?", "Audience (1.B.2): the direct address names who should act.",
    ["Werde Teil unseres Ehrenamt-Netzwerks → residents over 16."])
Q.q("1.A.1 Detail", r"Was bietet das Programm den Teilnehmenden?",
    "eine Bescheinigung, die bei Bewerbungen nützlich ist", [("ein monatliches Gehalt", "Volunteers are not paid."),
                                                            ("eine Reise am Ende des Programms", "Not mentioned."),
                                                            ("kostenlose Universitätskurse", "It offers training, not university courses.")],
    "Bescheinigung für Bewerbungen.", "The Was wir bieten section lists training, a certificate, and meeting neighbors.",
    ["eine Bescheinigung … nützlich für Bewerbungen und Stipendien."])
Q.q("1.A.1 Detail", r"Welche Tätigkeit wird im Flyer NICHT erwähnt?",
    "die Straßen des Viertels putzen", [("ältere Menschen besuchen", "Listed."),
                                       ("im Gemeinschaftsgarten helfen", "Listed."),
                                       ("Nachhilfe geben", "Listed.")],
    "Street cleaning is not listed.", "NOT questions: check each choice against the list.",
    ["Listed: visits, garden, tutoring."])
Q.q("1.C.2 Conclusion", r"Jemand meldet sich am 20. Oktober an. Was passiert wahrscheinlich?",
    "Die Person kann nicht mitmachen, weil die Anmeldefrist vorbei ist.", [("Sie beginnt ohne Problem am 1. November.", "Registration closes on October 15."),
                                                                           ("Sie bekommt sofort die Bescheinigung.", "The certificate is for hours completed."),
                                                                           ("Sie muss eine Verspätungsgebühr zahlen.", "No fee is mentioned.")],
    "Deadline: by October 15.", "Conclusions (1.C.2) apply the text's details to a new case.",
    ["bis zum 15. Oktober → too late."])
Q.q("1.B.3 Tone", r"Welchen Ton hat der Flyer?",
    "begeistert und persönlich", [("kühl und bürokratisch", "It uses du and exclamations."),
                                  ("ironisch", "Nothing is said ironically."),
                                  ("traurig und besorgt", "The tone is upbeat.")],
    "Dein Viertel braucht dich! + du.", "Tone (1.B.3): exclamations and informal du make the flyer warm and enthusiastic.",
    ["Exclamations + du → enthusiastic, personal."])

Q.sec("Listening: Interview")
Q.src(r"Listening 2 \textperiodcentered\ Interview (transcript) \textperiodcentered\ Eine Bürgermeisterin in Tirol", [
    r"(REPORTER) Frau Hofer, Sie sind seit vier Jahren Bürgermeisterin von Steinach. Was war das größte Problem, als Sie angefangen haben?",
    r"(BÜRGERMEISTERIN) Die Jungen sind weggegangen. Nach der Schule sind sie nach Innsbruck oder Wien gezogen, weil es hier weder Arbeit noch eine Fachhochschule gab.",
    r"(REPORTER) Und was haben Sie gemacht?",
    r"(BÜRGERMEISTERIN) Zuerst haben wir ihnen zugehört. Sie haben gesagt, dass sie eigentlich bleiben wollten, aber Chancen brauchten. Dann haben wir ein Ausbildungszentrum für nachhaltigen Tourismus und Holzbau eröffnet, mit Online-Kursen der Fachhochschule. Außerdem gibt es jeden Monat einen Arbeitseinsatz, bei dem das ganze Dorf Wege und die Schule repariert.",
    r"(REPORTER) Hat es funktioniert?",
    r"(BÜRGERMEISTERIN) Es gibt noch viel zu tun. Aber dieses Jahr sind zum ersten Mal mehr junge Leute zurückgekommen als weggezogen. Das Wichtigste ist, dass sie spüren: Das Dorf gehört auch ihnen.",
], 5)
Q.q("1.A.1 Detail", r"Warum sind die jungen Leute laut der Bürgermeisterin weggegangen?",
    "weil es im Dorf weder Arbeit noch eine Fachhochschule gab", [("weil sie das Landleben nicht mochten", "They said they wanted to stay."),
                                                                 ("weil die Schule geschlossen war", "The school needed repairs; that is not the reason given."),
                                                                 ("weil ihre Familien umgezogen waren", "They left on their own after school.")],
    "weder Arbeit noch Fachhochschule.", "The reason is stated directly in her first answer.",
    ["weil es hier weder Arbeit noch eine Fachhochschule gab."])
Q.q("1.B.4 Organization", r"Wie beschreibt die Bürgermeisterin das Vorgehen?",
    "Zuerst hörten sie den Jugendlichen zu, dann schufen sie Lösungen.", [("Zuerst bauten sie eine Universität, dann sprachen sie mit den Jugendlichen.", "She says zuerst haben wir ihnen zugehört."),
                                                                          ("Sie engagierten eine ausländische Firma.", "Not mentioned."),
                                                                          ("Sie warteten auf die Regierung in Wien.", "The village acted itself.")],
    "Zuerst… Dann…", "Organization (1.B.4): zuerst and dann mark the order.",
    ["Zuerst haben wir ihnen zugehört.", "Dann haben wir … eröffnet."])
Q.q("1.A.1 Detail", r"Was passiert beim monatlichen Arbeitseinsatz?",
    "Das ganze Dorf repariert gemeinsam Wege und die Schule.", [("Das Dorf feiert ein religiöses Fest.", "No."),
                                                               ("Die Bewohner sammeln Geld.", "It is work, not fundraising."),
                                                               ("Es gibt Kurse für Holzbau.", "Courses are at the training center.")],
    "Gemeinsame Reparaturen.", "Detail (1.A.1).",
    ["bei dem das ganze Dorf Wege und die Schule repariert."])
Q.q("1.B.3 Attitude", r"Welche Haltung zeigt die Bürgermeisterin gegenüber den Ergebnissen?",
    "optimistisch, aber sie weiß, dass noch viel zu tun ist", [("völlig zufrieden", "Es gibt noch viel zu tun."),
                                                              ("enttäuscht", "She reports progress."),
                                                              ("gleichgültig", "She cares about the outcome.")],
    "Es gibt noch viel zu tun. Aber…", "Mixed attitude (1.B.3): a concession followed by progress.",
    ["Concession + progress → cautiously optimistic."])
Q.q("1.C.3 Inference", r"Was meint die Bürgermeisterin mit „Das Dorf gehört auch ihnen“?",
    "Die Jugendlichen fühlen sich als Teil der Gemeinschaft und verantwortlich für sie.", [("Die Jugendlichen haben Häuser im Dorf gekauft.", "She speaks of belonging, not property."),
                                                                                          ("Die Jugendlichen regieren jetzt das Dorf.", "She is still the mayor."),
                                                                                          ("Die Jugendlichen wollen das Dorf verkaufen.", "Nonsensical reading.")],
    "Belonging, not property.", "Implied meaning (1.C.3): gehören is used figuratively.",
    ["After being heard and working together, they feel the village is theirs too."])

Q.frq(kind="Argumentative Essay", head=r"Question 3 \textperiodcentered\ Argumentative Essay \textperiodcentered\ 10 points \textperiodcentered\ 55 minutes", mins=55,
      directions=[r"Sie schreiben einen argumentativen Aufsatz für einen Universitätskurs. Lesen Sie das Thema und die schriftlichen Quellen; hören Sie dann die Audioquelle (hier als Transkript). Schreiben Sie einen Aufsatz, der Informationen aus allen drei Quellen verwendet, um Ihre Position zu unterstützen. Geben Sie die Quellen mit Nummer, Titel oder Autor an."],
      sources=[dict(title=r"Quelle 1 \textperiodcentered\ Artikel \textperiodcentered\ „Leben in der Großstadt“", paras=[
          r"Für Jonas, 29, Ingenieur, war der Umzug von seinem Heimatdorf nach München die beste Entscheidung seines Lebens. „Hier habe ich einen Job in meinem Fach, Museen, Konzerte und Menschen aus der ganzen Welt“, erzählt er.",
          r"Großstädte bündeln Universitäten, spezialisierte Krankenhäuser und die meisten qualifizierten Arbeitsplätze. „Die Stadt vervielfacht die Möglichkeiten: Je mehr Menschen, desto mehr Ideen“, sagt der Stadtplaner Thomas Braun.",
          r"Doch Jonas kennt auch den Preis: Er verbringt fast zwei Stunden täglich in Bus und Bahn und gibt die Hälfte seines Gehalts für die Miete aus."]),
               dict(title=r"Quelle 2 \textperiodcentered\ Grafik \textperiodcentered\ Zufriedenheit nach Wohnort", paras=[
          r"Umfrage unter 4.000 Erwachsenen in Deutschland, Österreich und der Schweiz. Anteil der Befragten, die mit dem jeweiligen Bereich „zufrieden“ oder „sehr zufrieden“ sind (fiktive Daten)."],
                    table=(["Bereich", "Großstadt", "Kleine Gemeinde"], [["Arbeitsmöglichkeiten", "64~\\%", "31~\\%"], ["Freizeit", "38~\\%", "67~\\%"], ["Beziehung zu den Nachbarn", "29~\\%", "72~\\%"], ["Ärztliche Versorgung", "71~\\%", "40~\\%"]])),
               dict(title=r"Quelle 3 \textperiodcentered\ Audio (Transkript) \textperiodcentered\ Podcast „Vom Land“", paras=[
          r"(MODERATORIN) Heute zu Gast ist Anna Gruber, die vor drei Jahren in ihr Dorf im Bregenzerwald zurückgekehrt ist.",
          r"(ANNA) In Wien habe ich mehr verdient, das stimmt. Aber ich kannte meine Nachbarn nicht, und mein Sohn konnte nicht draußen spielen. Hier kennt jeder jeden; wenn jemand krank wird, organisiert das Dorf Hilfe.",
          r"(MODERATORIN) Und die Arbeit?",
          r"(ANNA) Ich arbeite online für eine Designagentur. Ohne schnelles Internet hätte ich nie zurückkommen können. Deshalb sage ich: Das Dorf kann die Zukunft sein, aber nur, wenn die Infrastruktur kommt."])],
      prompt=[r"Thema des Aufsatzes: \textbf{Lebt man in einer Großstadt besser als in einer kleinen Gemeinde?}"],
      model=[r"Im letzten Jahrhundert haben Millionen Menschen das Land verlassen, um in der Stadt ein besseres Leben zu suchen. Heute stellt sich die Frage neu. Obwohl die Großstadt mehr berufliche Möglichkeiten bietet, bin ich der Ansicht, dass eine kleine Gemeinde dank der Technik heute ein erfüllteres Leben ermöglichen kann.",
             r"Erstens sind die menschlichen Beziehungen in kleinen Gemeinden enger. Die Grafik in Quelle 2 zeigt, dass 72~\% der Bewohner kleiner Gemeinden mit ihrer Nachbarschaft zufrieden sind, aber nur 29~\% in Großstädten. Anna Gruber bestätigt das in Quelle 3: In Wien kannte sie ihre Nachbarn nicht, während in ihrem Dorf „das Dorf Hilfe organisiert“, wenn jemand krank wird. Diese Solidarität, die man auch in Vereinen und bei der Freiwilligen Feuerwehr sieht, findet man in einer Großstadt selten.",
             r"Zweitens lässt das Leben auf dem Land mehr Freizeit. Laut Quelle 2 sind 67~\% der Bewohner kleiner Gemeinden mit ihrer Freizeit zufrieden, fast doppelt so viele wie in der Stadt. Der Fall von Jonas in Quelle 1 erklärt, warum: Er verbringt fast zwei Stunden täglich in Bus und Bahn.",
             r"Zwar bündeln Großstädte qualifizierte Arbeitsplätze und Krankenhäuser, wie der Stadtplaner Thomas Braun betont (Quelle 1), und die Grafik bestätigt den Unterschied bei der ärztlichen Versorgung. Das Beispiel von Anna zeigt jedoch, dass man dank Homeoffice heute auch fern der Hauptstadt einen guten Job haben kann, wenn das Internet schnell genug ist.",
             r"Zusammenfassend lässt sich sagen: Wenn die Regierungen schnelles Internet und ärztliche Versorgung aufs Land bringen würden, wäre die kleine Gemeinde für viele die bessere Wahl: mehr Zeit, mehr Gemeinschaft und inzwischen auch berufliche Chancen."],
      rows=[("A Position", 1, "clear position (here: a small town can offer a fuller life, given infrastructure)", "only lists pros and cons of each place"),
            ("B Source use", 2, "all three sources used accurately and named", "two sources, or a misread chart (e.g., reversing the columns)"),
            ("C Argumentation", 2, "each claim explained with evidence (bestätigt das, erklärt, warum)", "a summary of each source with no link to the position"),
            ("D Organization", 2, "introduction, claim paragraphs, concession, conclusion; varied transitions", "source-by-source paragraphs"),
            ("E Language control", 3, "varied structures (obwohl, relative clauses, Konjunktiv II), correct word order", "basic sentences, copied phrases")],
      tips=["Every body paragraph combines two sources.", "The cultural reference (Vereine, Freiwillige Feuerwehr) adds range without leaving the topic.",
            "The concession uses Zwar… jedoch…", "The conclusion's Konjunktiv II (würden… bringen, wäre) shows control."],
      ask="Write your essay in German (about 300–350 words), then mark it against each row.", lines=22)

GUIDE, QSET = G, Q
