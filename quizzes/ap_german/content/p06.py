from ap_wl.model import Doc

STEM = "06-global-contexts"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 6: Global Contexts", r"Unit 6 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 6 asks how global issues affect families and communities, and how people and governments respond. Its recommended contexts are global communication, the natural world, history, policy and planning, and transportation. This guide gives the vocabulary of the environment, history and public policy, the cases most often tested (the energy transition, Alpine glaciers, the Berlin Wall and reunification, the culture of remembrance, Austrian and Swiss neutrality, the Deutschlandticket, the Gotthard Base Tunnel, direct democracy), the language for proposing solutions, and an Argumentative Essay kit on counterarguments. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Solutions I can propose: \blank[10em]",
        short="Unit 6", sub="Global Contexts")

G.sec("The natural world")
G.tex(r"""
\begin{vocab}
die Umwelt / der Umweltschutz & environment / environmental protection & \\
der Klimawandel / die Erderwärmung & climate change / global warming & \\
die Energiewende & energy transition & nuclear exit 2023; coal exit by 2038 at the latest \\
der Gletscher / die Gletscherschmelze & glacier / glacier melt & the Alps \\
der Wald / der Borkenkäfer & forest / bark beetle & drought-weakened spruce forests \\
der Nationalpark & national park & Bayerischer Wald, Germany's first (1970) \\
die erneuerbaren Energien & renewable energy & \\
\end{vocab}

\textbf{Cases.} Germany closed its last nuclear power plants in April 2023 and plans to end coal power by 2038 at the latest, while expanding wind and solar. Alpine glaciers are shrinking fast, which threatens water supplies, hydropower and tourism in Switzerland and Austria.
""")
G.q("1 Natur", r"Was bedeutet „Energiewende“?",
    "den Umbau der Energieversorgung weg von Atomkraft und Kohle hin zu erneuerbaren Energien", [("die Erfindung eines neuen Motors", "No."),
                                                                                                ("eine Wende in der Politik 1989", "Die Wende usually refers to 1989; Energiewende is about energy."),
                                                                                                ("einen Stromausfall", "No.")],
    "Energiewende = energy transition.", "The policy replaces nuclear and fossil power with renewables.",
    ["Atomausstieg + Kohleausstieg + Wind/Solar."])
G.q("1 Natur", r"Why does glacier melt in the Alps worry Swiss and Austrian communities?",
    "Glaciers store water for drinking, hydropower and agriculture.", [("Glaciers cause earthquakes when they melt.", "No."),
                                                                       ("Melting glaciers make the mountains taller.", "No."),
                                                                       ("Tourists prefer melting glaciers.", "Tourism suffers.")],
    "Glaciers = water reserve.", "When glaciers shrink, summer water for rivers, power plants and farms decreases.",
    ["Gletscher → Wasserspeicher."])

G.sec("History and remembrance")
G.tex(r"""
\begin{vocab}
die Teilung / die Mauer & division / the Wall & built August 13, 1961 \\
der Mauerfall & fall of the Wall & November 9, 1989 \\
die Wiedervereinigung & reunification & October 3, 1990 \\
die Erinnerungskultur & culture of remembrance & \\
der Stolperstein & ``stumbling stone'' & small brass plaques for victims of Nazism \\
die Neutralität & neutrality & Switzerland; Austria since 1955 \\
die Europäische Union & European Union & West Germany co-founded the EEC (1957) \\
\end{vocab}

\textbf{Remembrance.} Since 1992 the artist Gunter Demnig has set more than 100,000 \emph{Stolpersteine} into sidewalks across Europe, each in front of the last home a victim of Nazism chose freely. The practice reflects a perspective that remembering is a shared, everyday responsibility, not only a matter for museums.
""")
G.q("2 Geschichte", r"Was sind Stolpersteine?",
    "kleine Gedenktafeln im Gehweg für Opfer des Nationalsozialismus", [("Steine, die Unfälle verursachen sollen", "Literal misreading."),
                                                                         ("Grenzsteine zwischen Ost und West", "No."),
                                                                         ("Steine aus der Berliner Mauer", "No.")],
    "Stolpersteine = memorial plaques.", "Each brass plaque names a victim in front of their last freely chosen home.",
    ["Stolpersteine → Erinnerung im Alltag."])
G.q("2 Geschichte", r"On which date did the Berlin Wall fall?",
    "November 9, 1989", [("October 3, 1990", "That is reunification day."),
                         ("August 13, 1961", "That is when the Wall was built."),
                         ("May 8, 1945", "That is the end of the war in Europe.")],
    "9. November 1989.", "Keep the dates apart: built 1961, fell 1989, reunification 1990.",
    ["Mauerfall → 9.11.1989."])

G.sec("Policy, planning and transportation")
G.tex(r"""
\begin{vocab}
der öffentliche Nahverkehr (ÖPNV) & local public transportation & \\
das Deutschlandticket & monthly ticket for all local transit nationwide & since May 2023 \\
die Fahrradstadt & cycling city & Münster \\
das Tempolimit & speed limit & much of the Autobahn has only an advisory 130 km/h \\
der Gotthard-Basistunnel & 57-km rail tunnel under the Alps, opened 2016 & the world's longest rail tunnel \\
die Volksabstimmung & referendum & Switzerland votes several times a year \\
die Alpen-Initiative & 1994 Swiss vote to move freight from road to rail & \\
\end{vocab}

\textbf{Cases.} With the Deutschlandticket, one monthly ticket covers buses, trams and regional trains across Germany. In Switzerland, voters decided in 1994 to protect the Alps by moving freight traffic onto rail, which led to huge tunnels like the Gotthard. The perspective in both: affordable, shared transport and protected landscapes are public goods.
""")
G.q("3 Verkehr", r"Was ermöglicht das Deutschlandticket?",
    "mit einem Monatsticket Busse, Bahnen und Regionalzüge in ganz Deutschland zu nutzen", [("kostenlose Flüge innerhalb Deutschlands", "No."),
                                                                                           ("schnelleres Fahren auf der Autobahn", "No."),
                                                                                           ("ICE-Fahrten ohne Aufpreis", "It covers local and regional transit, not long-distance ICE trains.")],
    "One ticket, all local transit.", "The Deutschlandticket covers local and regional public transport nationwide.",
    ["Monatsticket → Nah- und Regionalverkehr bundesweit."])
G.q("3 Verkehr", r"In 1994, Swiss voters decided to move freight traffic from roads to rail to protect the Alps. Which perspective does this reflect?",
    "Citizens may directly decide to protect landscapes for future generations.", [("Only trucks should cross the Alps.", "The opposite."),
                                                                                     ("Voters should not decide on transport.", "The vote shows the opposite."),
                                                                                     ("Tunnels are bad for the environment.", "Tunnels were the solution.")],
    "Referendum + protection.", "Practice (popular vote) ↔ perspective (direct democracy, environmental stewardship).",
    ["Volksabstimmung → Alpenschutz."])

G.sec("Structures: proposing solutions")
G.tex(r"""
\begin{compare}{Purpose}{Structure}{Example}
Necessity & man muss / es ist notwendig, \ldots zu & Man muss Wasser sparen. \\
Recommendation & man sollte / man müsste (Konjunktiv II) & Man müsste mehr in die Bahn investieren. \\
Polite proposal & Es wäre sinnvoll, wenn\ldots & Es wäre sinnvoll, wenn mehr Radwege gebaut würden. \\
Purpose & damit / um\ldots zu & Man pflanzt Bäume, damit die Stadt kühler wird. \\
Proportion & je\ldots, desto\ldots & Je mehr Menschen Bahn fahren, desto weniger Staus gibt es. \\
Passive with modals & muss / sollte + participle + werden & Der Verkehr sollte verringert werden. \\
\end{compare}

\begin{trap}
\emph{Je} sends the verb to the end; \emph{desto} is followed by the comparative and then the verb: \emph{Je mehr Menschen Bahn fahren, desto weniger Staus gibt es.}
\end{trap}
""")
G.q("4 Lösungen", r"Wählen Sie den richtigen Satz.",
    "Je mehr Menschen Rad fahren, desto sauberer wird die Luft.", [("Je mehr Menschen fahren Rad, desto sauberer wird die Luft.", "After je, the verb goes to the end."),
                                                                   ("Je mehr Menschen Rad fahren, desto die Luft wird sauberer.", "After desto + comparative, the verb comes next."),
                                                                   ("Je mehr Menschen Rad fahren, desto sauberer die Luft wird.", "The desto-clause is a main clause: verb second.")],
    "je … verb last, desto … verb next.", "Je-clause: subordinate (verb last); desto-clause: desto + comparative + verb.",
    ["Je … fahren, desto sauberer wird…"])
G.q("4 Lösungen", r"Which sentence proposes a solution politely and clearly?",
    "Es wäre sinnvoll, wenn die Stadt mehr Radwege bauen würde, damit weniger Menschen mit dem Auto fahren.", [("Radwege.", "A fragment, not a proposal."),
                                                                                                               ("Staus sind mir egal.", "Indifference, not a solution."),
                                                                                                               ("Staus sind ein großes und sehr schlimmes Problem.", "States the problem, proposes nothing.")],
    "Es wäre sinnvoll, wenn… damit…", "A Konjunktiv II proposal plus a purpose clause is clear and polite.",
    ["Konjunktiv II + damit."])

G.sec("Task kit: answering the other side")
G.tex(r"""
Global-context essays (\emph{Sollte es ein Tempolimit auf Autobahnen geben?}, \emph{Ist Umweltschutz wichtiger als Arbeitsplätze?}) almost always come with one source that disagrees with you. Use it: a counterargument answered well shows argumentation and earns credit for that source.

\begin{terms}
Concede & \emph{Zwar\ldots / Es stimmt, dass\ldots} + the opposing point with its source \\
Answer & \emph{Dennoch\ldots / Allerdings\ldots} + evidence from another source or a solution \\
Limit & \emph{wenn / sofern / vorausgesetzt, dass}: under what conditions your position holds \\
\end{terms}

\begin{keyidea}[Qualified positions]
\emph{Ein Tempolimit ist sinnvoll, vorausgesetzt, dass es mit einem besseren Bahnangebot verbunden wird} is a clear position (Row A) that already includes the reply to the strongest objection.
\end{keyidea}
""")
G.q("5 Aufsatz", r"A source says a speed limit would make some long commutes slower. How should an essay in favor of a speed limit use this source?",
    "concede the point and answer it with evidence or a solution", [("ignore it so the essay stays one-sided", "Ignoring a source loses source-use points."),
                                                                     ("change position to agree with it", "One objection does not require abandoning a position."),
                                                                     ("quote it with no comment", "Evidence without explanation does not earn argumentation credit.")],
    "Concede + answer.", "Answering the opposing source strengthens argumentation and still counts toward using all three sources.",
    ["Zwar… dennoch…"])
G.q("5 Aufsatz", r"Wählen Sie die richtige Wortstellung: Ich unterstütze das Tempolimit, vorausgesetzt, dass die Bahn \blank.",
    "zuverlässiger wird", [("wird zuverlässiger", "After dass, the conjugated verb goes to the end."),
                           ("zuverlässiger werden", "The subject die Bahn is singular: wird."),
                           ("zuverlässiger geworden", "A conjugated verb is needed.")],
    "dass → verb last.", "Vorausgesetzt, dass… introduces a subordinate clause: verb last.",
    ["…dass die Bahn zuverlässiger wird."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 6: Global Contexts: Question Set", r"Unit 6 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Interview and an Instructional Guidance for listening, an Article and an Article and Chart for reading) on Alpine glaciers, the Deutschlandticket, renewable energy and heat waves, followed by an Argumentative Essay with three sources and the 10-point scoring guide. As on the exam, questions and choices are in German; listening sources are printed as transcripts. All sources and data are original and fictional, written for practice. Allow about 25 minutes for the multiple choice and 55 minutes for the essay.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Essay: \blank\ / 10 \qquad Target: 15+ MCQ and 7+ essay \qquad Pace: 75 s per item",
        short="Unit 6", sub="Global Contexts")

Q.sec("Listening: Interview")
Q.src(r"Listening 1 \textperiodcentered\ Interview (transcript) \textperiodcentered\ Eine Schweizer Glaziologin", [
    r"(REPORTER) Frau Dr. Meier, Sie vermessen seit zwanzig Jahren Gletscher im Wallis. Was haben Sie beobachtet?",
    r"(DR. MEIER) Dass sie verschwinden. Einige kleine Gletscher, die ich als Studentin vermessen habe, gibt es nicht mehr. Die großen haben einen erheblichen Teil ihres Volumens verloren.",
    r"(REPORTER) Warum sollte das eine Familie im Tal interessieren?",
    r"(DR. MEIER) Weil ein Teil ihres Trinkwassers und ihres Stroms aus dem Schmelzwasser kommt, besonders im Sommer. Der Gletscher ist wie ein Sparkonto: Wenn wir alles ausgeben, ist es leer, wenn wir es am dringendsten brauchen.",
    r"(REPORTER) Kann man etwas tun?",
    r"(DR. MEIER) Das Abschmelzen allein können wir hier nicht stoppen, es hängt vom Klima der ganzen Welt ab. Aber wir können uns vorbereiten: neue Wasserspeicher bauen, undichte Leitungen reparieren und lernen, sparsamer mit Wasser umzugehen. Anpassung ist auch eine Form von Verantwortung.",
], 5)
Q.q("1.A.1 Detail", r"Was hat Dr. Meier in zwanzig Jahren beobachtet?",
    "Manche Gletscher sind verschwunden, andere sind stark geschrumpft.", [("Die Gletscher sind gewachsen.", "The opposite."),
                                                                           ("Es gab keine großen Veränderungen.", "She describes big losses."),
                                                                           ("Es regnet im Sommer mehr.", "Not stated.")],
    "Sie verschwinden.", "Detail (1.A.1).",
    ["…gibt es nicht mehr … erheblichen Teil ihres Volumens verloren."])
Q.q("1.C.3 Inference", r"Was bedeutet der Vergleich des Gletschers mit einem „Sparkonto“?",
    "dass der Gletscher Wasser für trockene Zeiten speichert", [("dass man mit Gletscherwasser Geld verdient", "Figurative misreading."),
                                                               ("dass Banken die Gletscher finanzieren", "No."),
                                                               ("dass der Gletscher Strom verkauft", "No.")],
    "Savings account = stored reserve.", "Figurative language (1.C.3): a reserve for when it is needed most.",
    ["Sparkonto → Reserve für den Sommer."])
Q.q("1.B.3 Point of view", r"Was kann man laut Dr. Meier tun?",
    "sich anpassen, zum Beispiel mit neuen Wasserspeichern und reparierten Leitungen", [("das Abschmelzen lokal stoppen", "She says it cannot be stopped locally."),
                                                                                        ("das Tal verlassen", "Not proposed."),
                                                                                        ("nichts, weil es unvermeidlich ist", "She proposes preparation.")],
    "Anpassung.", "Point of view (1.B.3): Das … können wir nicht … Aber wir können…",
    ["neue Wasserspeicher bauen, undichte Leitungen reparieren…"])
Q.q("1.B.4 Organization", r"Wie ist die letzte Antwort von Dr. Meier aufgebaut?",
    "Sie nennt eine Grenze und schlägt dann mögliche Maßnahmen vor.", [("Sie erzählt eine Geschichte aus ihrer Kindheit.", "No."),
                                                                      ("Sie vergleicht zwei Länder.", "No."),
                                                                      ("Sie zählt Ursachen des Klimawandels auf.", "She does not list causes.")],
    "Limit + proposals.", "Organization (1.B.4): concession, then solutions.",
    ["…nicht stoppen … Aber wir können…"])
Q.q("1.B.5 Word meaning", r"Im Interview bedeutet „undichte Leitungen“",
    "Rohre, aus denen Wasser verloren geht", [("neue Stromkabel", "No."),
                                              ("Gletscherspalten", "No."),
                                              ("leere Flaschen", "No.")],
    "undicht = leaking.", "Word meaning (1.B.5): repairing them saves water.",
    ["undichte Leitungen reparieren → leaking pipes."])

Q.sec("Reading: Article")
Q.src(r"Reading 1 \textperiodcentered\ Article \textperiodcentered\ „Ein Ticket für das ganze Land“", [
    r"Seit Mai 2023 gibt es in Deutschland das Deutschlandticket. Für einen festen Monatspreis kann man damit alle Busse, Straßenbahnen, U-Bahnen und Regionalzüge im ganzen Land nutzen, vom Bodensee bis zur Ostsee. Nur Fernzüge wie der ICE sind ausgenommen.",
    r"Für viele Pendlerinnen und Pendler ist das Ticket eine große Erleichterung. „Früher habe ich für die Strecke in die Stadt fast das Doppelte bezahlt, und ich musste die Tarifzonen studieren wie ein Wörterbuch“, erzählt Sabine, Krankenpflegerin aus Brandenburg.",
    r"Verkehrsexperten weisen jedoch darauf hin, dass ein günstiges Ticket allein nicht reicht. „Auf dem Land fährt der Bus manchmal nur zweimal am Tag“, sagt der Verkehrsplaner Jan Köhler. „Ein Ticket ist eine Tür; entscheidend ist, ob dahinter auch ein Bus kommt.“",
], 5)
Q.q("1.B.1 Main idea", r"Was ist die Hauptaussage des Artikels?",
    "Das Deutschlandticket erleichtert vielen das Reisen, aber ohne gutes Angebot reicht es nicht.", [("Das Deutschlandticket gilt auch für alle ICE-Züge.", "Long-distance trains are excluded."),
                                                                                                     ("Das Ticket ist ein Misserfolg.", "Many commuters benefit."),
                                                                                                     ("Auf dem Land gibt es keine Busse.", "There are some, but few.")],
    "Benefit + limit.", "Main idea (1.B.1): description, testimony, caveat.",
    ["Paragraphs 1–2 benefits; 3 nicht reicht."])
Q.q("1.A.1 Detail", r"Welche Züge kann man mit dem Deutschlandticket NICHT benutzen?",
    "Fernzüge wie den ICE", [("Regionalzüge", "Included."),
                             ("Straßenbahnen", "Included."),
                             ("U-Bahnen", "Included.")],
    "Fernzüge ausgenommen.", "Detail (1.A.1).",
    ["Nur Fernzüge wie der ICE sind ausgenommen."])
Q.q("1.C.3 Inference", r"Was meint Sabine mit „die Tarifzonen studieren wie ein Wörterbuch“?",
    "dass das alte Tarifsystem kompliziert war", [("dass sie gern Wörterbücher liest", "Figurative."),
                                                  ("dass sie eine Sprache lernen musste", "No."),
                                                  ("dass Fahrkarten in Büchern verkauft wurden", "No.")],
    "Complex zones.", "Inference (1.C.3): comparing fare zones to a dictionary stresses complexity.",
    ["Tarifzonen + Wörterbuch → kompliziert."])
Q.q("1.B.3 Point of view", r"Was ist laut Jan Köhler entscheidend?",
    "ob es auch genug Busse und Bahnen gibt", [("dass das Ticket noch billiger wird", "He says a cheap ticket alone is not enough."),
                                               ("dass mehr Menschen Auto fahren", "No."),
                                               ("dass ICE-Züge gratis werden", "No.")],
    "Ein Ticket ist eine Tür…", "Point of view (1.B.3).",
    ["…ob dahinter auch ein Bus kommt."])
Q.q("1.B.4 Organization", r"Welche Funktion hat das Wort „jedoch“ im dritten Absatz?",
    "Es leitet eine Einschränkung nach den Vorteilen ein.", [("Es fasst den Artikel zusammen.", "It does not summarize."),
                                                             ("Es gibt ein weiteres Beispiel für Vorteile.", "It introduces a limit."),
                                                             ("Es wechselt das Thema.", "Same topic.")],
    "Contrast transition.", "Organization (1.B.4): jedoch introduces a counterpoint.",
    ["benefits → jedoch → limitation."])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 2 \textperiodcentered\ Article and Chart \textperiodcentered\ „Woher kommt unser Strom?“", [
    r"Seit dem Atomausstieg 2023 setzt Deutschland vor allem auf Wind und Sonne. An manchen Tagen decken sie mehr als die Hälfte des Stromverbrauchs, an windstillen, dunklen Wintertagen aber deutlich weniger.",
    r"Experten empfehlen deshalb, die Energiequellen zu mischen und Speicher auszubauen: Wenn eine Quelle schwächelt, sollen andere einspringen. Je vielfältiger ein Stromsystem ist, desto sicherer ist es.",
], 5, table=(["Region (fiktive Daten)", "Wind", "Sonne", "Wasser", "Kohle und Gas"],
             [["Region A", "15~\\%", "3~\\%", "72~\\%", "10~\\%"], ["Region B", "38~\\%", "4~\\%", "30~\\%", "28~\\%"], ["Region C", "35~\\%", "20~\\%", "40~\\%", "5~\\%"]]),
      note="Herkunft des Stroms in drei Regionen (fiktive Daten).")
Q.q("1.A.2 Data", r"Welche Region bezieht laut Tabelle den größten Anteil ihres Stroms aus Wasserkraft?",
    "Region A", [("Region B", "B gets most from wind (38%)."),
                 ("Region C", "C has 40% hydro, less than A."),
                 ("alle drei gleich", "The shares differ.")],
    "Region A: 72%.", "Data (1.A.2).",
    ["72 % > 40 % > 30 %."])
Q.q("1.C.1 Connect", r"Welche Region folgt laut Artikel am besten der Empfehlung der Experten?",
    "Region C, weil sie mehrere Quellen mischt und wenig Kohle und Gas nutzt", [("Region A, weil sie viel Wasserkraft nutzt", "Concentration is what the experts warn against."),
                                                                                ("Region B, weil sie 28~\\% Kohle und Gas nutzt", "High fossil use is not the goal."),
                                                                                ("keine", "C does.")],
    "Mix → Region C.", "Connect (1.C.1): the recommendation (mischen) matches C's balanced mix.",
    ["C: 35/20/40/5 → gemischt."])
Q.q("1.C.2 Conclusion", r"Welche Region wäre in einem sehr trockenen Jahr am stärksten gefährdet?",
    "Region A, weil sie am meisten von Wasserkraft abhängt", [("Region C, weil sie Solarstrom nutzt", "Solar does not depend on rain."),
                                                             ("Region B, weil sie Wind nutzt", "Wind does not depend on rain."),
                                                             ("keine, Trockenheit spielt keine Rolle", "Hydropower needs water.")],
    "Drought hurts hydro → A.", "Conclusions (1.C.2): apply the logic of the article to a new case.",
    ["trocken → weniger Wasserkraft → A."])
Q.q("1.B.5 Word meaning", r"Im Artikel bedeutet „schwächelt“",
    "liefert vorübergehend weniger", [("wird verboten", "No."),
                                      ("wird teurer", "Not the meaning."),
                                      ("wird repariert", "No.")],
    "schwächeln = to falter.", "Word meaning (1.B.5): other sources should step in when one falters.",
    ["Wenn eine Quelle schwächelt, sollen andere einspringen."])
Q.q("1.A.1 Detail", r"Wann decken Wind und Sonne laut Artikel deutlich weniger Strom?",
    "an windstillen, dunklen Wintertagen", [("an sonnigen Sommertagen", "Then they cover more."),
                                           ("nachts im Sommer", "Not stated."),
                                           ("nur am Wochenende", "No.")],
    "windstill + dunkel.", "Detail (1.A.1).",
    ["an windstillen, dunklen Wintertagen aber deutlich weniger."])

Q.sec("Listening: Instructional Guidance")
Q.src(r"Listening 2 \textperiodcentered\ Instructional Guidance (transcript) \textperiodcentered\ Hinweise der Stadt zur Hitzewelle", [
    r"(SPRECHERIN) Der Wetterdienst warnt vor einer Hitzewelle mit über 35 Grad. Die Stadt bittet alle Bürgerinnen und Bürger, die folgenden Hinweise zu beachten.",
    r"(SPRECHERIN) Erstens: Trinken Sie regelmäßig Wasser, auch wenn Sie keinen Durst haben, und meiden Sie Alkohol. Zweitens: Lüften Sie Ihre Wohnung frühmorgens und schließen Sie tagsüber Fenster und Vorhänge.",
    r"(SPRECHERIN) Drittens: Verschieben Sie Sport und Gartenarbeit auf den frühen Morgen oder den Abend. Viertens: Die Stadtbibliothek und das Rathaus sind als kühle Räume bis 20 Uhr geöffnet.",
    r"(SPRECHERIN) Und denken Sie an Ihre Nachbarn: Ältere Menschen, die allein leben, sind besonders gefährdet. Ein kurzer Anruf oder ein Klingeln an der Tür kann Leben retten.",
], 5)
Q.q("1.A.1 Detail", r"Wann sollte man laut Durchsage die Wohnung lüften?",
    "frühmorgens", [("mittags", "Windows should be closed during the day."),
                    ("am Nachmittag", "Windows should be closed during the day."),
                    ("gar nicht", "Ventilation early in the morning is advised.")],
    "frühmorgens.", "Instructional Guidance: match each instruction with its time.",
    ["Lüften Sie Ihre Wohnung frühmorgens…"])
Q.q("1.A.1 Detail", r"Welche Orte bietet die Stadt als kühle Räume an?",
    "die Stadtbibliothek und das Rathaus", [("das Schwimmbad und das Kino", "Not mentioned."),
                                           ("die Schulen", "Not mentioned."),
                                           ("die Supermärkte", "Not mentioned.")],
    "Bibliothek + Rathaus.", "Detail (1.A.1).",
    ["Die Stadtbibliothek und das Rathaus sind als kühle Räume … geöffnet."])
Q.q("1.B.2 Audience", r"An wen richtet sich die Durchsage?",
    "an alle Bürgerinnen und Bürger der Stadt", [("nur an Sportler", "Sport is one instruction."),
                                                ("an Touristen", "No."),
                                                ("an Ärzte", "No.")],
    "alle Bürgerinnen und Bürger.", "Audience (1.B.2).",
    ["Die Stadt bittet alle Bürgerinnen und Bürger…"])
Q.q("1.B.5 Word meaning", r"In der Durchsage bedeutet „meiden Sie Alkohol“",
    "trinken Sie keinen Alkohol", [("trinken Sie mehr Alkohol", "The opposite."),
                                   ("kaufen Sie Alkohol im Voraus", "No."),
                                   ("mischen Sie Alkohol mit Wasser", "No.")],
    "meiden = avoid.", "Word meaning (1.B.5).",
    ["Trinken Sie Wasser … und meiden Sie Alkohol → avoid."])
Q.q("1.C.3 Inference", r"Warum betont die Durchsage am Ende die Nachbarn?",
    "weil allein lebende ältere Menschen bei Hitze besonders gefährdet sind und Hilfe brauchen", [("weil die Nachbarn zu laut sind", "No."),
                                                                                                  ("weil Nachbarn Wasser verkaufen", "No."),
                                                                                                  ("weil die Stadt keine Mitarbeiter hat", "Not stated.")],
    "Solidarity saves lives.", "Inference (1.C.3).",
    ["Ein kurzer Anruf … kann Leben retten."])

Q.frq(kind="Argumentative Essay", head=r"Question 3 \textperiodcentered\ Argumentative Essay \textperiodcentered\ 10 points \textperiodcentered\ 55 minutes", mins=55,
      directions=[r"Sie schreiben einen argumentativen Aufsatz für einen Universitätskurs. Lesen Sie das Thema und die schriftlichen Quellen; hören Sie dann die Audioquelle (hier als Transkript). Schreiben Sie einen Aufsatz, der Informationen aus allen drei Quellen verwendet, um Ihre Position zu unterstützen. Geben Sie die Quellen mit Nummer, Titel oder Autor an."],
      sources=[dict(title=r"Quelle 1 \textperiodcentered\ Artikel \textperiodcentered\ „130 oder freie Fahrt?“", paras=[
          r"Deutschland ist eines der wenigen Länder der Welt, in denen auf großen Teilen der Autobahn kein festes Tempolimit gilt; empfohlen werden 130 Kilometer pro Stunde. Umweltverbände fordern seit Jahren ein verbindliches Limit, weil bei hohen Geschwindigkeiten deutlich mehr Kraftstoff verbraucht wird.",
          r"„Ein Tempolimit würde sofort wirken und fast nichts kosten“, sagt Lea Hoffmann von einem Umweltverband. Gegner sehen darin dagegen einen Eingriff in die persönliche Freiheit und verweisen darauf, dass die Autobahn im Vergleich zu Landstraßen relativ sicher ist."]),
               dict(title=r"Quelle 2 \textperiodcentered\ Grafik \textperiodcentered\ Durchschnittlicher Kraftstoffverbrauch eines Mittelklassewagens", paras=[
          r"Liter pro 100 Kilometer bei gleichmäßiger Fahrt (fiktive Daten)."],
                    table=(["Geschwindigkeit", "Liter pro 100 km"], [["100 km/h", "5,4"], ["130 km/h", "6,9"], ["160 km/h", "9,2"], ["190 km/h", "12,1"]])),
               dict(title=r"Quelle 3 \textperiodcentered\ Audio (Transkript) \textperiodcentered\ „Unterwegs“, Radiosendung", paras=[
          r"(MODERATOR) Wir sprechen mit Stefan Krause, der als Außendienstmitarbeiter jedes Jahr 60.000 Kilometer fährt.",
          r"(STEFAN KRAUSE) Ich bin nicht grundsätzlich gegen ein Tempolimit. Aber für Leute wie mich, die lange Strecken fahren müssen, bedeutet es mehr Zeit im Auto. In meiner Region gibt es keine gute Bahnverbindung, ich habe also keine Alternative.",
          r"(MODERATOR) Was wünschen Sie sich?",
          r"(STEFAN KRAUSE) Wenn man ein Tempolimit einführt, dann bitte gleichzeitig die Bahn ausbauen. Sonst bestraft man die Menschen auf dem Land."])],
      prompt=[r"Thema des Aufsatzes: \textbf{Sollte Deutschland ein allgemeines Tempolimit auf Autobahnen einführen?}"],
      model=[r"Deutschland ist eines der wenigen Länder, in denen man auf vielen Autobahnabschnitten so schnell fahren darf, wie man will. Sollte sich das ändern? Ich bin der Meinung, dass ein allgemeines Tempolimit sinnvoll ist, vorausgesetzt, dass gleichzeitig die Bahn ausgebaut wird.",
             r"Erstens würde ein Tempolimit viel Kraftstoff sparen. Die Grafik in Quelle 2 zeigt, dass ein Mittelklassewagen bei 130 km/h 6,9 Liter pro 100 Kilometer verbraucht, bei 190 km/h aber 12,1 Liter, also fast doppelt so viel. Diese Zahlen belegen, dass schnelles Fahren Umwelt und Geldbeutel stark belastet. Wie Lea Hoffmann in Quelle 1 betont, würde ein Tempolimit „sofort wirken und fast nichts kosten“.",
             r"Zweitens ist ein Limit eine einfache Maßnahme mit großer Wirkung. Im Gegensatz zu neuen Kraftwerken oder Leitungen braucht es nur Schilder und Kontrollen. Je mehr Menschen langsamer fahren, desto weniger Kraftstoff wird verbraucht.",
             r"Zwar sehen die Gegner, die in Quelle 1 zitiert werden, darin einen Eingriff in die Freiheit, und Stefan Krause erklärt in Quelle 3, dass er durch ein Limit mehr Zeit im Auto verbringen würde, weil es in seiner Region keine gute Bahnverbindung gibt. Dennoch ist Krause „nicht grundsätzlich gegen ein Tempolimit“: Er verlangt nur, dass die Bahn gleichzeitig ausgebaut wird. Sein Einwand spricht also nicht gegen das Limit, sondern für eine bessere Verkehrspolitik.",
             r"Zusammenfassend lässt sich sagen: Wenn Deutschland ein Tempolimit einführen und zugleich in die Bahn investieren würde, könnte es Kraftstoff sparen, ohne die Menschen auf dem Land zu benachteiligen."],
      rows=[("A Position", 1, "a clear, qualified position (yes, provided rail is expanded)", "only lists both sides"),
            ("B Source use", 2, "all three sources used accurately and named; the chart's units kept straight", "two sources, or misreading liters and speeds"),
            ("C Argumentation", 2, "claims explained with evidence; the opposing source answered", "summaries with no link to the claims"),
            ("D Organization", 2, "introduction, two claims, concession and rebuttal, conclusion", "one paragraph per source"),
            ("E Language control", 3, "varied structures: vorausgesetzt, dass; je … desto; Konjunktiv II; nicht … sondern", "basic structures; copied phrases")],
      tips=["The qualified position already answers the strongest objection.", "The opposing source (Krause) is conceded and then shown to support the principle.",
            "The chart is quoted with its units (Liter pro 100 Kilometer).", "The conclusion's Konjunktiv II (würde … einführen, könnte) rounds off the argument."],
      ask="Write your essay in German (about 300–350 words), then mark it against each row.", lines=22)

GUIDE, QSET = G, Q
