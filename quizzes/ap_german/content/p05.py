from ap_wl.model import Doc

STEM = "05-contemporary-life"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 5: Contemporary Life", r"Unit 5 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 5 asks how traditions shape daily life today: school and work, food and health, leisure, sports and travel. Its recommended contexts are education and career, entertainment and media, food and health, pop culture, sports and leisure, and travel and tourism. This guide gives the vocabulary of daily life, the practices most often tested (the school system and the Abitur, dual vocational training, the warm lunch and the cold Abendbrot, bread culture and the Viennese coffeehouse, Sunday rest, clubs and allotment gardens), relative clauses with prepositions and the imperative, and a second Project Presentation kit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Practices I can link to a perspective: \blank[8em]",
        short="Unit 5", sub="Contemporary Life")

G.sec("School, training and work")
G.tex(r"""
\begin{vocab}
die Grundschule & primary school (usually grades 1--4) & \\
das Gymnasium / die Realschule / die Gesamtschule & academic / intermediate / comprehensive secondary school & \\
das Abitur (Matura in Austria and Switzerland) & university-entrance exam & \\
die duale Ausbildung & dual training: company plus vocational school & \\
der Azubi (Auszubildende) & apprentice & \\
die Studiengebühren & tuition fees & public universities in Germany charge almost none \\
die Lehre & apprenticeship & about two thirds of Swiss teenagers start one \\
\end{vocab}

\textbf{Practices and perspectives.} In the dual system, apprentices spend most of the week in a company and one or two days at a vocational school, earning a wage from the start. The model reflects a perspective that practical skills are as valuable as academic ones; in Switzerland, many bank and IT careers begin with an apprenticeship rather than a university degree.
""")
G.q("1 Bildung", r"Was ist die duale Ausbildung?",
    "eine Ausbildung, die im Betrieb und in der Berufsschule stattfindet", [("ein Studium an zwei Universitäten", "No."),
                                                                           ("eine Schule nur für Zwillinge", "Literal misreading."),
                                                                           ("ein Praktikum ohne Schule", "There is a school part.")],
    "Betrieb + Berufsschule.", "Dual training combines paid work in a company with classes at a vocational school.",
    ["dual = zwei Lernorte."])
G.q("1 Bildung", r"In Switzerland, about two thirds of teenagers start an apprenticeship, including in banking and IT. Which perspective does this reflect?",
    "Practical training is valued as much as academic study.", [("Only university graduates deserve good jobs.", "The opposite."),
                                                               ("Teenagers should not work.", "Apprentices work and earn a wage."),
                                                               ("Schools should teach only theory.", "The opposite.")],
    "Apprenticeship ↔ value of practical skills.", "Practice (apprenticeship as the main path) linked to a perspective (respect for skilled work).",
    ["two thirds + banking/IT → prestige of training."])

G.sec("Food and health")
G.tex(r"""
\begin{vocab}
das Frühstück / das Mittagessen / das Abendbrot & breakfast / (warm) lunch / (cold) supper & \\
Kaffee und Kuchen & afternoon coffee and cake & weekends, family visits \\
die Brotkultur & bread culture & more than 3,000 registered bread varieties in Germany \\
das Kaffeehaus & Viennese coffeehouse & a place to read and talk for hours \\
die Krankenversicherung & health insurance & compulsory; Germany's system dates from 1883 \\
die Kur & health cure at a spa & \\
Bio & organic & \emph{Bioprodukte} \\
\end{vocab}

\textbf{Meals.} Traditionally the main warm meal is at midday, and supper (\emph{Abendbrot}) is bread with cheese and cold cuts. In a Viennese \emph{Kaffeehaus}, a guest may sit for hours over one coffee and the newspapers; the waiter brings a glass of water unasked. The practice reflects a value placed on unhurried time, conversation and reading.
""")
G.q("2 Essen", r"Was isst man traditionell beim Abendbrot?",
    "Brot mit Käse oder Wurst", [("ein warmes Drei-Gänge-Menü", "The warm meal is traditionally at midday."),
                                 ("nur Kuchen", "Cake is for Kaffee und Kuchen."),
                                 ("nichts, man fastet abends", "No.")],
    "Abendbrot = bread supper.", "The name says it: Abend + Brot.",
    ["Abendbrot → kaltes Abendessen mit Brot."])
G.q("2 Essen", r"In a Viennese Kaffeehaus, guests may stay for hours over one coffee. Which perspective does this practice reflect?",
    "Unhurried time for conversation and reading is valuable.", [("Guests should leave as quickly as possible.", "The opposite."),
                                                                 ("Coffee should be drunk standing up.", "No."),
                                                                 ("Cafés are only for tourists.", "Locals use them daily.")],
    "Kaffeehaus ↔ slowness, sociability.", "Practice (staying for hours) ↔ perspective (time for talk and newspapers).",
    ["stunden lang + Zeitung → Muße."])
G.q("2 Gesundheit", r"Seit wann gibt es in Deutschland eine gesetzliche Krankenversicherung?",
    "seit 1883", [("seit 1990", "1990 is reunification."),
                  ("seit 2018", "2018 is the data protection regulation."),
                  ("seit 1810", "1810 is the first Oktoberfest.")],
    "1883, under Bismarck.", "Germany introduced compulsory health insurance in 1883, one of the first countries to do so.",
    ["Bismarck → 1883."])

G.sec("Leisure, sports and travel")
G.tex(r"""
\begin{vocab}
der Urlaub & vacation & four weeks minimum by law; about 30 days is common \\
die Sonntagsruhe / der Ladenschluss & Sunday rest / shop closing hours & most shops are closed on Sundays \\
der Schrebergarten (Kleingarten) & allotment garden & \\
die Bundesliga / die 50+1-Regel & top soccer league / rule keeping clubs majority-owned by members & \\
das Wandern / die Hütte & hiking / mountain hut & \\
der Reiseweltmeister & ``world travel champion'' & Germans travel abroad a lot \\
\end{vocab}

\textbf{Sunday rest.} On Sundays most shops in Germany and Austria are closed by law, and loud work like mowing the lawn is frowned on. The perspective: a shared day of rest belongs to families, churches, clubs and walks, not to shopping.
""")
G.q("3 Freizeit", r"Was bedeutet die Sonntagsruhe in Deutschland?",
    "Die meisten Geschäfte haben sonntags geschlossen, und laute Arbeiten sind unerwünscht.", [("Am Sonntag darf man nicht wandern.", "Hiking is typical on Sundays."),
                                                                                              ("Am Sonntag sind alle Restaurants geschlossen.", "Restaurants are open."),
                                                                                              ("Am Sonntag gibt es keine Züge.", "Trains run.")],
    "Sunday rest = closed shops, quiet.", "Shop-closing laws and quiet hours protect Sunday as a day of rest.",
    ["Ladenschluss + Ruhe."])
G.q("3 Freizeit", r"Which perspective do Germany's Sunday shop closures most directly reflect?",
    "A shared day of rest is more important than shopping.", [("Shopping should be possible at all times.", "The opposite."),
                                                             ("Families should work on Sundays.", "No."),
                                                             ("Shops should close every day at noon.", "No.")],
    "Sunday rest ↔ shared time off.", "A law (product) and a custom (practice) linked to a value (rest, family, community).",
    ["geschlossen → Zeit für Familie und Erholung."])

G.sec("Structures: relative clauses with prepositions, the imperative")
G.tex(r"""
\begin{compare}{Structure}{Use}{Example}
Relative clause with preposition & preposition + relative pronoun (case from the preposition) & Der Verein, in dem ich spiele, ist hundert Jahre alt. \\
wo / worüber & places / things & Das ist das Café, wo wir uns treffen. \\
Imperative (du / ihr / Sie) & instructions, advice & Iss mehr Obst! Esst mehr Obst! Essen Sie mehr Obst! \\
sich lohnen & to be worth it & Eine Ausbildung lohnt sich. \\
es gibt + accusative & there is / are & Es gibt viele Ausbildungsberufe. \\
\end{compare}

\begin{trap}
In relative clauses the preposition comes first and decides the case: \emph{der Freund, mit \textbf{dem} ich wandere} (mit + dative), \emph{die Stadt, für \textbf{die} ich arbeite} (für + accusative).
\end{trap}
""")
G.q("4 Strukturen", r"Wählen Sie die richtige Form: Das ist der Verein, in \blank\ ich seit zehn Jahren Fußball spiele.",
    "dem", [("den", "In + location takes the dative: in dem Verein."),
            ("der", "Verein is masculine; der would be the nominative."),
            ("das", "Verein is masculine.")],
    "in + dative, masculine → dem.", "The preposition decides the case; the noun decides the gender.",
    ["in dem Verein → in dem."])
G.q("4 Strukturen", r"Welcher Imperativ passt für einen Freund (du)?",
    "Iss weniger Zucker!", [("Esst weniger Zucker!", "That is the ihr form (several friends)."),
                           ("Essen Sie weniger Zucker!", "That is the formal Sie form."),
                           ("Isst weniger Zucker!", "Isst is the statement form (du isst), not the imperative.")],
    "du-imperative: iss.", "Du-imperative drops -st and the pronoun: du isst → iss!",
    ["du → iss."])

G.sec("Task kit: developing a factor in the presentation")
G.tex(r"""
Each factor in the Project Presentation should follow the same four steps, about 40 seconds in all:

\begin{terms}
1 Claim & \emph{Der zweite Faktor ist die Zensur in der DDR.} \\
2 Evidence & one specific fact or example from your research: a place, a date, a name, a practice \\
3 Perspective & \emph{Das spiegelt wider, dass\ldots / Das zeigt, wie wichtig\ldots war.} \\
4 Link & connect to the prompt or the next factor: \emph{Deshalb\ldots / Außerdem\ldots} \\
\end{terms}

\begin{keyidea}[Change over time]
Prompts often ask how a tradition has changed. Use time markers (\emph{in den Siebzigerjahren, nach dem Mauerfall, heute}) and the Präteritum in narration: \emph{Damals durften viele Lieder nicht gespielt werden; heute hört man sie überall.}
\end{keyidea}
""")
G.q("5 Präsentation", r"Which sequence develops a factor most completely?",
    "claim, specific example from research, perspective it reflects, link to the next idea", [("claim, then the next factor", "No detail or perspective."),
                                                                                              ("example, then a personal opinion", "No claim or perspective."),
                                                                                              ("a definition of the genre only", "No claim, example or perspective.")],
    "Claim → evidence → perspective → link.", "Full task and culture credit come from detailed factors that reach a perspective.",
    ["All four steps → full development."])
G.q("5 Präsentation", r"Wählen Sie die richtige Form: Damals \blank\ viele Lieder im Radio nicht gespielt werden.",
    "durften", [("dürfen", "Damals places the sentence in the past."),
                ("darf", "Viele Lieder is plural, and the sentence is past."),
                ("gedurft", "A conjugated modal is needed.")],
    "Past modal: durften.", "Präteritum of modals in narration: durften, konnten, mussten.",
    ["damals + plural → durften."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 5: Contemporary Life: Question Set", r"Unit 5 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Audio Report and a Presentation for listening, an Article and Chart and a Promotional Material for reading) on Sunday shopping, apprenticeships, allotment gardens and bread culture, followed by a second practice Project Presentation on music, with the 11-point scoring guide and a model script. The presentation prompt is a practice prompt, not the official 2027 project prompt. As on the exam, questions and choices are in German; listening sources are printed as transcripts. All sources and data are original and fictional. Allow about 25 minutes for the multiple choice and 6 minutes for the presentation.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Presentation: \blank\ / 11 \qquad Target: 15+ MCQ and 8+ presentation",
        short="Unit 5", sub="Contemporary Life")

Q.sec("Listening: Audio Report")
Q.src(r"Listening 1 \textperiodcentered\ Audio Report (transcript) \textperiodcentered\ „Shoppen am Sonntag?“, Radio Stadt", [
    r"(REPORTERIN) In fast allen Bundesländern bleiben die Geschäfte am Sonntag geschlossen, nur an wenigen verkaufsoffenen Sonntagen im Jahr dürfen sie öffnen. Jetzt fordern einige Händler, dass die Regeln gelockert werden.",
    r"(HÄNDLER) Die Leute bestellen am Sonntag einfach online. Wenn wir nicht öffnen dürfen, verlieren wir Kunden an große Internetfirmen.",
    r"(REPORTERIN) Gewerkschaften und Kirchen widersprechen. Für sie geht es um mehr als Einkaufen.",
    r"(GEWERKSCHAFTERIN) Viele Verkäuferinnen haben kleine Kinder. Der Sonntag ist oft der einzige Tag, an dem die ganze Familie zusammen ist. Wenn wir ihn aufgeben, gibt es keinen gemeinsamen freien Tag mehr.",
], 5)
Q.q("1.A.1 Detail", r"Wann dürfen die Geschäfte laut Bericht am Sonntag öffnen?",
    "nur an wenigen verkaufsoffenen Sonntagen im Jahr", [("jeden Sonntag am Vormittag", "No."),
                                                        ("nie", "A few Sundays are allowed."),
                                                        ("nur in Großstädten", "Not stated.")],
    "wenige verkaufsoffene Sonntage.", "Detail (1.A.1).",
    ["nur an wenigen verkaufsoffenen Sonntagen…"])
Q.q("1.B.3 Point of view", r"Was ist das Hauptargument des Händlers?",
    "Ohne Sonntagsöffnung verlieren die Geschäfte Kunden an Online-Händler.", [("Die Verkäuferinnen wollen am Sonntag arbeiten.", "Not his argument."),
                                                                              ("Die Kirchen sollten mehr verkaufen.", "No."),
                                                                              ("Am Sonntag gibt es zu viel Verkehr.", "No.")],
    "Online competition.", "Point of view (1.B.3).",
    ["…verlieren wir Kunden an große Internetfirmen."])
Q.q("1.B.3 Point of view", r"Warum ist der Sonntag für die Gewerkschafterin wichtig?",
    "weil er oft der einzige Tag ist, an dem die Familie zusammen ist", [("weil am Sonntag mehr verkauft wird", "The opposite of her point."),
                                                                         ("weil die Geschäfte sonntags billiger sind", "No."),
                                                                         ("weil die Kirchen es so befehlen", "She argues from family life.")],
    "Family day.", "Point of view (1.B.3): her reason concerns family time.",
    ["…der einzige Tag, an dem die ganze Familie zusammen ist."])
Q.q("1.B.4 Organization", r"Wie ist der Bericht aufgebaut?",
    "Er stellt eine Forderung vor und lässt dann beide Seiten zu Wort kommen.", [("Er erzählt die Geschichte eines Geschäfts.", "No narrative."),
                                                                                ("Er gibt Tipps zum Online-Einkauf.", "No tips."),
                                                                                ("Er vergleicht Deutschland mit den USA.", "No comparison.")],
    "Demand → both sides.", "Organization (1.B.4): situation, demand, one side, the other side.",
    ["Händler vs. Gewerkschaft."])
Q.q("1.C.3 Inference", r"Was meint die Gewerkschafterin mit „Für sie geht es um mehr als Einkaufen“?",
    "dass der freie Sonntag einen sozialen Wert hat", [("dass Einkaufen sonntags teurer wäre", "No."),
                                                       ("dass Kirchen Geschäfte besitzen", "No."),
                                                       ("dass Händler zu viel verdienen", "No.")],
    "Social value.", "Inference (1.C.3): the issue is framed as family and community, not commerce.",
    ["mehr als Einkaufen → Familie, Gemeinschaft."])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 1 \textperiodcentered\ Article and Chart \textperiodcentered\ „Lernen im Betrieb“, Magazin Zukunft", [
    r"Lange Zeit galt in Deutschland: Wer Abitur hat, studiert. Heute ändert sich das Bild. Immer mehr Abiturientinnen und Abiturienten beginnen eine duale Ausbildung, etwa als Mechatroniker, Bankkauffrau oder Fachinformatiker.",
    r"„Ich verdiene vom ersten Tag an Geld, habe keine Schulden und mit 21 schon drei Jahre Berufserfahrung“, sagt Mia, Auszubildende bei einem Solarunternehmen. Für die Berufsberaterin Anke Lehmann ist das kein Zufall: „Früher wollten Eltern, dass ihr Kind Arzt oder Anwalt wird. Heute findet ein guter Facharbeiter oft schneller eine Stelle.“",
    r"Lehmann räumt jedoch ein, dass Vorurteile bleiben: Manche Jugendliche müssen ihre Entscheidung für einen Handwerksberuf in der Familie immer noch rechtfertigen.",
], 5, table=(["Bereich", "2015", "2025"], [["Medizin und Jura", "38~\\%", "30~\\%"], ["IT und Informatik", "14~\\%", "26~\\%"], ["Duale Ausbildung nach dem Abitur", "9~\\%", "19~\\%"], ["Sonstige", "39~\\%", "25~\\%"]]),
      note="Anteil der Abiturienten, die den jeweiligen Weg wählen (fiktive Daten).")
Q.q("1.A.2 Data", r"Welcher Bereich hat sich laut Tabelle zwischen 2015 und 2025 fast verdoppelt?",
    "IT und Informatik", [("Medizin und Jura", "It fell from 38% to 30%."),
                          ("Sonstige", "It fell."),
                          ("Kein Bereich hat sich verändert", "Several changed.")],
    "14 → 26 (almost double).", "Data (1.A.2): compare the two columns.",
    ["14 % → 26 %: ×1.86."])
Q.q("1.C.1 Connect", r"Welche Zahl in der Tabelle passt am besten zum veränderten Bild, das der Artikel beschreibt?",
    "der Anstieg der dualen Ausbildung nach dem Abitur von 9~\\% auf 19~\\%", [("der Rückgang bei Medizin und Jura", "Not the article's focus."),
                                                                              ("die 39~\\% Sonstige im Jahr 2015", "Not relevant."),
                                                                              ("die 26~\\% IT", "Not about apprenticeships.")],
    "Dual training 9 → 19.", "Connect (1.C.1): the article is about apprenticeships gaining appeal.",
    ["Heute ändert sich das Bild ↔ 9 % → 19 %."])
Q.q("1.B.3 Point of view", r"Warum entscheiden sich laut Anke Lehmann mehr junge Leute für eine Ausbildung?",
    "weil ein guter Facharbeiter oft schneller eine Stelle findet", [("weil ihre Eltern es verlangen", "Parents traditionally preferred professions."),
                                                                     ("weil die Universitäten geschlossen haben", "Not stated."),
                                                                     ("weil sie keine IT mögen", "Not stated.")],
    "schneller eine Stelle.", "Point of view (1.B.3).",
    ["Heute findet ein guter Facharbeiter oft schneller eine Stelle."])
Q.q("1.B.5 Word meaning", r"Im Artikel bedeutet „räumt … ein“",
    "gibt zu", [("räumt auf", "Aufräumen means to tidy up."),
                ("lehnt ab", "Ablehnen means to reject."),
                ("lädt ein", "Einladen means to invite.")],
    "einräumen = concede.", "Word meaning (1.B.5): jedoch + a limitation → she concedes.",
    ["räumt jedoch ein, dass Vorurteile bleiben → concedes."])
Q.q("1.C.2 Conclusion", r"Was kann man aus dem letzten Absatz schließen?",
    "Die Erwartungen der Familie beeinflussen die Berufswahl noch immer.", [("Familien äußern keine Meinung mehr.", "Prejudices remain."),
                                                                            ("Handwerksberufe sind schlecht bezahlt.", "Not stated."),
                                                                            ("Alle Abiturienten machen eine Ausbildung.", "Only 19%.")],
    "Vorurteile bleiben.", "Conclusions (1.C.2) from Lehmann's caveat.",
    ["…müssen ihre Entscheidung … rechtfertigen."])

Q.sec("Reading: Promotional Material")
Q.src(r"Reading 2 \textperiodcentered\ Promotional Material \textperiodcentered\ Eine Anzeige eines Kleingartenvereins", [
    r"\textbf{Gartenfreunde Sonnenhang e.\,V. \textperiodcentered\ Leipzig-Süd}",
    r"Sie träumen von eigenen Tomaten mitten in der Stadt? Bei uns sind drei Parzellen frei! Jede ist etwa 300 Quadratmeter groß und hat eine kleine Laube mit Wasseranschluss.",
    r"\textbf{Kosten:} Pacht und Mitgliedsbeitrag zusammen ca. 350 Euro im Jahr. Die Laube wird vom Vorpächter übernommen; der Preis wird von einem Gutachter festgelegt.",
    r"\textbf{Bitte beachten:} Laut Bundeskleingartengesetz muss ein Teil der Fläche für Obst und Gemüse genutzt werden. Außerdem erwarten wir von jedem Mitglied fünf Stunden Gemeinschaftsarbeit pro Jahr.",
    r"Besichtigung jeden Samstag von 10 bis 12 Uhr am Vereinsheim. Familien mit Kindern sind besonders willkommen!",
], 5)
Q.q("1.B.2 Audience", r"An wen richtet sich die Anzeige?",
    "an Stadtbewohner, die einen eigenen Garten möchten", [("an Landwirte, die Felder suchen", "The plots are small and in the city."),
                                                           ("an Touristen in Leipzig", "No."),
                                                           ("an Firmen, die Büros mieten", "No.")],
    "Tomaten mitten in der Stadt.", "Audience (1.B.2).",
    ["Sie träumen von eigenen Tomaten mitten in der Stadt?"])
Q.q("1.A.1 Detail", r"Was muss laut Gesetz auf einem Teil der Fläche wachsen?",
    "Obst und Gemüse", [("nur Rasen", "No."),
                        ("Blumen für den Verkauf", "No."),
                        ("Bäume aus dem Ausland", "No.")],
    "Obst und Gemüse.", "Detail (1.A.1).",
    ["muss ein Teil der Fläche für Obst und Gemüse genutzt werden."])
Q.q("1.A.1 Detail", r"Was erwartet der Verein von jedem Mitglied?",
    "fünf Stunden Gemeinschaftsarbeit im Jahr", [("eine Spende von 300 Euro", "Not stated."),
                                                  ("einen Bauernhof", "No."),
                                                  ("jeden Samstag zu arbeiten", "Viewings are on Saturdays.")],
    "Gemeinschaftsarbeit.", "Detail (1.A.1).",
    ["fünf Stunden Gemeinschaftsarbeit pro Jahr."])
Q.q("1.B.5 Word meaning", r"In der Anzeige bedeutet „Parzelle“",
    "ein einzelnes Gartenstück", [("ein Paket", "No."),
                                  ("ein Gartengerät", "No."),
                                  ("eine Wohnung", "No.")],
    "Parzelle = plot.", "Word meaning (1.B.5): each one is 300 square meters with a hut.",
    ["etwa 300 Quadratmeter groß … Laube → plot."])
Q.q("1.C.2 Conclusion", r"Eine Familie möchte eine Parzelle ansehen. Was sollte sie tun?",
    "an einem Samstag zwischen 10 und 12 Uhr zum Vereinsheim kommen", [("jeden Tag um 18 Uhr anrufen", "Not stated."),
                                                                       ("sofort 350 Euro überweisen", "Not the first step."),
                                                                       ("einen Gutachter bestellen", "The association arranges the valuation.")],
    "Saturday viewing.", "Apply the details: Besichtigung jeden Samstag von 10 bis 12 Uhr.",
    ["Besichtigung jeden Samstag…"])

Q.sec("Listening: Presentation")
Q.src(r"Listening 2 \textperiodcentered\ Presentation (transcript) \textperiodcentered\ „Warum Deutschland ein Brotland ist“", [
    r"(PROFESSOR) Wer aus dem Ausland kommt, staunt oft in einer deutschen Bäckerei: Roggenbrot, Vollkornbrot, Brezeln, Brötchen in Dutzenden Sorten. Im deutschen Brotregister sind über 3.000 Brotsorten verzeichnet.",
    r"(PROFESSOR) Ein Grund ist die Geografie. Im Norden und Osten wuchs auf kargen Böden vor allem Roggen, daraus entstanden dunkle, schwere Brote. Im Süden gab es mehr Weizen und damit hellere Backwaren wie die Brezel.",
    r"(PROFESSOR) Ein zweiter Grund ist die politische Geschichte. Deutschland bestand jahrhundertelang aus vielen kleinen Staaten, und jede Region entwickelte ihre eigenen Rezepte.",
    r"(PROFESSOR) Seit 2014 gehört die deutsche Brotkultur zum immateriellen Kulturerbe auf nationaler Ebene. Heute machen allerdings viele kleine Bäckereien zu, weil Supermärkte billiger sind. Ob die Vielfalt überlebt, hängt auch von den Kunden ab.",
], 5)
Q.q("1.B.1 Main idea", r"Was ist das zentrale Thema des Vortrags?",
    "die Gründe für die große Vielfalt der deutschen Brotkultur", [("die Geschichte der Supermärkte", "Supermarkets are one detail."),
                                                                   ("Rezepte für Brezeln", "No recipes."),
                                                                   ("die Landwirtschaft in Österreich", "No.")],
    "Why so many breads.", "Main idea (1.B.1): description, two reasons, current situation.",
    ["Vielfalt → Geografie → Geschichte → heute."])
Q.q("1.A.1 Detail", r"Warum gibt es im Norden und Osten viele dunkle Brote?",
    "weil dort auf kargen Böden vor allem Roggen wuchs", [("weil dort mehr Weizen wuchs", "Wheat was more common in the south."),
                                                          ("weil die Menschen dort keine Brezeln mögen", "No."),
                                                          ("weil es dort mehr Supermärkte gibt", "No.")],
    "Rye on poor soils.", "Detail (1.A.1).",
    ["…wuchs auf kargen Böden vor allem Roggen…"])
Q.q("1.C.3 Inference", r"Warum erwähnt der Professor, dass Deutschland aus vielen kleinen Staaten bestand?",
    "um zu erklären, warum es so viele regionale Rezepte gibt", [("um über Kriege zu sprechen", "Not the point."),
                                                                ("um zu zeigen, dass Bäcker reich waren", "No."),
                                                                ("um die Supermärkte zu kritisieren", "No.")],
    "Many states → many recipes.", "Inference (1.C.3): political fragmentation explains regional variety.",
    ["jede Region entwickelte ihre eigenen Rezepte."])
Q.q("1.B.4 Organization", r"Wie ist der Vortrag aufgebaut?",
    "Er beschreibt ein Phänomen, nennt zwei Gründe und endet mit einer aktuellen Frage.", [("Er erzählt die Geschichte einer Bäckerfamilie.", "No narrative."),
                                                                                           ("Er gibt eine Anleitung zum Backen.", "No instructions."),
                                                                                           ("Er vergleicht Deutschland mit Frankreich.", "No comparison.")],
    "Phenomenon → reasons → question.", "Organization (1.B.4): ein Grund / ein zweiter Grund / heute.",
    ["Structure follows the markers."])
Q.q("1.B.3 Point of view", r"Wovon hängt laut Professor die Zukunft der Brotvielfalt ab?",
    "auch von den Kunden", [("nur von der Regierung", "He says it depends on customers too."),
                            ("vom Wetter", "No."),
                            ("von den Supermärkten allein", "Not his conclusion.")],
    "hängt auch von den Kunden ab.", "Point of view (1.B.3): his final sentence.",
    ["Ob die Vielfalt überlebt, hängt auch von den Kunden ab."])

Q.frq(kind="Project Presentation", head=r"Question 1 \textperiodcentered\ Project Presentation (practice prompt) \textperiodcentered\ 11 points \textperiodcentered\ 3 + 3 minutes", mins=6,
      directions=[r"Imagine that your project examined how music has accompanied the history of a German-speaking community. You have 3 minutes to prepare, using your notes, and 3 minutes to present. Explain at least three factors, with specific examples from your research, and show how cultural perspectives relate to cultural products or practices."],
      prompt=[r"Prompt: \textbf{Wie hat die Musik die Geschichte einer deutschsprachigen Gemeinschaft begleitet?}",
              r"Practice focus (example): music during Germany's division and reunification."],
      model=[r"Heute spreche ich darüber, wie die Musik die Teilung Deutschlands und die Wiedervereinigung begleitet hat. Ich habe mich auf drei Faktoren konzentriert: die Liedermacher und die Zensur, die Rockmusik als Brücke zwischen Ost und West und die Techno-Kultur nach dem Mauerfall.",
             r"Erstens die Liedermacher. Bei meiner Recherche habe ich herausgefunden, dass Wolf Biermann in der DDR jahrelang nicht auftreten durfte, weil seine Lieder die Regierung kritisierten. 1976 wurde er nach einem Konzert im Westen ausgebürgert. Das zeigt, welche Macht Lieder hatten: Der Staat hatte Angst vor Worten, die viele Menschen mitsingen konnten.",
             r"Zweitens wurde die Rockmusik zu einer Brücke. Die DDR-Band Karat veröffentlichte 1978 das Lied „Über sieben Brücken musst du gehn“. Zwei Jahre später sang der westdeutsche Sänger Peter Maffay es neu, und es wurde in beiden Teilen Deutschlands bekannt. Das spiegelt wider, dass sich die Menschen trotz der Mauer eine gemeinsame Kultur bewahrten.",
             r"Schließlich die Zeit nach dem Mauerfall. In leeren Fabriken und Bunkern in Ost-Berlin entstanden Techno-Clubs, in denen junge Leute aus Ost und West zum ersten Mal zusammen feierten. Diese Praxis zeigt, wie wichtig ihnen Freiheit und ein neuer Anfang waren. Seit 2024 gehört die Berliner Technokultur sogar zum immateriellen Kulturerbe Deutschlands.",
             r"Zusammenfassend kann man sagen, dass Musik in Deutschland Widerstand, Verbindung und Neubeginn ausgedrückt hat. Ich habe gelernt, dass ein Lied manchmal Grenzen überwinden kann, die Politiker gebaut haben."],
      rows=[("A Task", 2, "three or more factors, each explained with relevant details", "factors named with no detail, or only one or two factors"),
            ("B Culture", 2, "examples linking perspectives (freedom, shared culture, a new beginning) to products or practices", "examples with no perspective (1 point)"),
            ("C Organization", 2, "introduction naming the factors, ordered body, conclusion; varied transitions", "a list of facts"),
            ("D Language", 3, "varied vocabulary and structures (passive, Präteritum, relative clauses with prepositions)", "a limited set of basic structures"),
            ("E Delivery", 2, "clear pronunciation, natural pace and intonation", "hesitant or rushed speech")],
      tips=["Each factor follows claim → specific example → perspective (das zeigt, das spiegelt wider).", "Change over time is shown with dates (1976, 1978, nach dem Mauerfall) and the Präteritum.",
            "The song that crossed the Wall is a vivid product that earns the culture row.", "About 380 words."],
      ask="Prepare for 3 minutes using keywords only, then present aloud for 3 minutes. Then mark your presentation.", lines=14)

GUIDE, QSET = G, Q
