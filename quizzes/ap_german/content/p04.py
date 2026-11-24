from ap_wl.model import Doc

STEM = "04-science-technology"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 4: Science and Technology", r"Unit 4 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 4 asks how science and technology change daily life, communication and society, and who benefits. Its recommended contexts are innovations and emerging technologies, personal technology and communication, science in everyday life, and the societal impacts of science and technology. This guide gives the vocabulary of technology and science, inventions from the German-speaking world, attitudes to privacy and cash, recycling and the deposit system, the energy transition, the structures for predictions, the passive with modal verbs and data, and an Argumentative Essay kit focused on reading charts. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Chart verbs I can use: \blank[10em]",
        short="Unit 4", sub="Science and Technology")

G.sec("Inventions and discoveries")
G.tex(r"""
\begin{vocab}
die Erfindung / die Entdeckung & invention / discovery & \emph{erfinden} vs. \emph{entdecken} \\
die künstliche Intelligenz (KI) & artificial intelligence & \\
der Algorithmus / die Daten & algorithm / data & \\
der Buchdruck & printing & \\
die Röntgenstrahlen & X-rays & \\
der Computer / der Rechner & computer & \\
das Patent & patent & \\
\end{vocab}

\begin{compare}{Invention or discovery}{Who, where, when}{Note}
printing with movable type & Johannes Gutenberg, Mainz, around 1450 & books for many, not only for the few \\
the automobile & Carl Benz, 1886 & \\
X-rays & Wilhelm Conrad Röntgen, 1895; first Nobel Prize in Physics, 1901 & medicine changed overnight \\
the Z3, an early programmable computer & Konrad Zuse, Berlin, 1941 & \\
the MP3 format & Fraunhofer Institute, 1990s & music compression \\
\end{compare}
""")
G.q("1 Erfindung", r"Warum war Gutenbergs Buchdruck so bedeutend?",
    "weil Bücher schneller und günstiger hergestellt werden konnten", [("weil er das Papier erfand", "Paper was invented earlier, in China."),
                                                                        ("weil er das erste Auto baute", "That was Carl Benz."),
                                                                        ("weil er die Röntgenstrahlen entdeckte", "That was Röntgen.")],
    "Movable type → cheaper books.", "Printing with movable type (around 1450) made books faster and cheaper to produce, spreading knowledge.",
    ["bewegliche Lettern → mehr Bücher für mehr Menschen."])
G.q("1 Erfindung", r"Wilhelm Conrad Röntgen received the first Nobel Prize in Physics for",
    "discovering X-rays", [("inventing the automobile", "That was Carl Benz."),
                           ("building an early computer", "That was Konrad Zuse."),
                           ("developing the MP3 format", "That was the Fraunhofer Institute.")],
    "Röntgen → X-rays, Nobel 1901.", "In German, X-rays are still called Röntgenstrahlen.",
    ["Röntgenstrahlen."])

G.sec("Personal technology, privacy and cash")
G.tex(r"""
\begin{vocab}
das Handy / das Smartphone & cell phone & \emph{Handy} is a pseudo-anglicism \\
die sozialen Medien / Netzwerke & social media & \\
der Datenschutz & data protection, privacy & \\
die DSGVO & the EU General Data Protection Regulation (2018) & \\
das Bargeld / bar zahlen & cash / to pay cash & \\
das Funkloch & dead zone (no mobile signal) & common in rural areas \\
die digitale Kluft & digital divide & \\
\end{vocab}

\textbf{Privacy.} When Google Street View came to Germany in 2010, hundreds of thousands of households asked for their houses to be blurred. \textbf{Cash.} Germans and Austrians still pay cash more often than most Europeans; many say it protects their privacy and helps them control spending. Both practices reflect a perspective shaped partly by history: personal data in the hands of a state or company can be misused.
""")
G.q("2 Datenschutz", r"Warum zahlen viele Deutsche noch gern bar?",
    "weil Bargeld ihre Privatsphäre schützt und hilft, die Ausgaben zu kontrollieren", [("weil Kartenzahlung in Deutschland verboten ist", "It is legal and common."),
                                                                                       ("weil Bargeld Zinsen bringt", "No."),
                                                                                       ("weil es keine Banken gibt", "No.")],
    "Cash ↔ privacy and control.", "Paying cash is a practice linked to a perspective on privacy and budgeting.",
    ["Bargeld → keine Datenspur, Kontrolle."])
G.q("2 Datenschutz", r"When Street View arrived in 2010, many German households asked for their houses to be blurred. Which perspective does this reflect?",
    "Personal privacy deserves strong protection.", [("Everyone should share as much data as possible.", "The opposite."),
                                                    ("Houses should not have addresses.", "No."),
                                                    ("Technology should never be used.", "Too extreme.")],
    "Blurring ↔ privacy.", "Practice (opting out) ↔ perspective (privacy as a right).",
    ["Verpixeln → Datenschutz."])

G.sec("Science in everyday life and its impact")
G.tex(r"""
\begin{vocab}
die Mülltrennung / der gelbe Sack & waste sorting / yellow bag for packaging & \\
die Biotonne & organic waste bin & \\
das Pfand / die Pfandflasche & deposit / deposit bottle & 25 cents on single-use bottles and cans since 2003 \\
die Energiewende & energy transition & the last nuclear plants closed in April 2023 \\
die erneuerbaren Energien & renewable energy & wind and solar \\
die Falschmeldung / die Fake News & false report & \\
\end{vocab}

\textbf{Questions about impact} ask who benefits and who is left out, what the risks are, and who should decide (\emph{Wer sollte KI regulieren?}). Good answers weigh both: \emph{Zwar erleichtert KI die Diagnose, aber sie wirft Fragen des Datenschutzes auf.}
""")
G.q("3 Alltag", r"Was bekommt man zurück, wenn man eine Pfandflasche in den Laden zurückbringt?",
    "das Pfand, zum Beispiel 25 Cent", [("eine neue Flasche gratis", "No."),
                                         ("einen Strafzettel", "No."),
                                         ("nichts, es ist nur Recycling", "The deposit is refunded.")],
    "Pfand = deposit refund.", "The deposit system pays back the deposit and makes returning bottles worthwhile.",
    ["Pfand zurück → 25 Cent."])
G.q("3 Alltag", r"Which sentence weighs a benefit against a risk, as impact questions reward?",
    "Zwar helfen Gesundheits-Apps, Krankheiten früh zu erkennen, aber sie sammeln sehr persönliche Daten.",
    [("Gesundheits-Apps sind super.", "One-sided and vague."),
     ("Viele Leute benutzen Gesundheits-Apps.", "A fact with no evaluation."),
     ("Man sollte Gesundheits-Apps sofort verbieten.", "One-sided, with no reasoning.")],
    "Zwar X, aber Y.", "Concessive structures let you weigh both sides in one sentence.",
    ["benefit + risk."])

G.sec("Structures: predictions, the passive with modals, data")
G.tex(r"""
\begin{compare}{Purpose}{Structure}{Example}
Predict & Futur I (werden + infinitive) & 2030 wird die Hälfte der Autos elektrisch fahren. \\
Probability & wahrscheinlich, vermutlich; es ist wahrscheinlich, dass & Es ist wahrscheinlich, dass KI viele Berufe verändert. \\
Hypothesize & Konjunktiv II & Wenn alle schnelles Internet hätten, gäbe es keine digitale Kluft. \\
Passive with modals & modal + participle + werden & Der Müll muss getrennt werden. \\
Data: change & steigen, zunehmen, sinken, abnehmen, sich verdoppeln & Die Nutzung hat sich zwischen 2019 und 2024 verdoppelt. \\
Data: share & die Mehrheit, die Hälfte, ein Drittel, jeder Vierte & Jeder vierte Schüler\ldots \\
\end{compare}

\begin{trap}
In the passive with a modal verb, the modal is conjugated and \emph{werden} goes to the very end: \emph{Die Flaschen müssen zurückgebracht werden.} In a subordinate clause: \emph{\ldots, weil die Flaschen zurückgebracht werden müssen.}
\end{trap}
""")
G.q("4 Strukturen", r"Wählen Sie die richtige Form: Leere Batterien dürfen nicht in den Hausmüll \blank.",
    "geworfen werden", [("werden geworfen", "With a modal, the passive infinitive is participle + werden, at the end."),
                        ("geworfen", "The passive needs werden as well."),
                        ("werfen", "The active infinitive does not fit the passive meaning.")],
    "Modal + participle + werden.", "Passive with modals: dürfen … geworfen werden.",
    ["dürfen nicht … geworfen werden."])
G.q("4 Strukturen", r"Laut einer Grafik stieg der Anteil der Kartenzahlungen in fünf Jahren von 20~\% auf 40~\%. Welcher Satz beschreibt das genau?",
    "Der Anteil der Kartenzahlungen hat sich in fünf Jahren verdoppelt.", [("Der Anteil ist jedes Jahr um 20~\\% gestiegen.", "The total rose 20 points over five years, not 20% a year."),
                                                                           ("Der Anteil hat sich halbiert.", "It rose."),
                                                                           ("Die Mehrheit zahlt mit Karte.", "40% is not a majority.")],
    "20 → 40 = doubled.", "Precise chart language: hat sich verdoppelt, ist um 20 Prozentpunkte gestiegen, stieg von 20 auf 40 Prozent.",
    ["40 = 2 × 20 → verdoppelt."])
G.q("4 Strukturen", r"Choose the passive sentence.",
    "Die ersten Computer der Firma wurden von Ingenieurinnen entwickelt.", [("Ingenieurinnen entwickelten die ersten Computer der Firma.", "Active voice."),
                                                                           ("Ingenieurinnen entwickeln gerade Computer.", "Active present."),
                                                                           ("Ingenieurinnen würden Computer entwickeln.", "Active Konjunktiv II.")],
    "werden + participle (+ von).", "The passive puts the thing affected first: wurden … entwickelt.",
    ["wurden von … entwickelt → passive."])

G.sec("Task kit: the Argumentative Essay with a chart")
G.tex(r"""
Unit 4 topics are often debates about benefits and risks: \emph{Sollte Bargeld abgeschafft werden?}, \emph{Sollten Schulen KI erlauben?} The chart source is easy to misread under time pressure.

\begin{terms}
Read the chart first & title, units (\%, Millionen, Stunden), years, who was surveyed \\
Pick one comparison & the biggest change, a majority, or a surprising gap \\
Say it precisely & \emph{Laut der Grafik in Quelle 2 zahlen 62~\% der\ldots, aber nur 25~\% der\ldots} \\
Explain it & \emph{Das zeigt, dass\ldots / Diese Zahlen belegen, dass\ldots} \\
\end{terms}

\begin{trap}
Misreading a chart (switching columns, treating a percentage as a number of people) costs points in source use. Quote the numbers with their labels.
\end{trap}
""")
G.q("5 Aufsatz", r"A chart shows 62\% of people under 30 pay mostly by card and 25\% of people over 65 do. Which sentence uses the chart correctly?",
    r"Laut Quelle 2 zahlen 62~\% der unter 30-Jährigen meistens mit Karte, aber nur 25~\% der über 65-Jährigen.", [("Laut Quelle 2 zahlen 62~\\% der über 65-Jährigen mit Karte.", "Switches the groups."),
                                                                                                                   ("Laut Quelle 2 zahlen 62 junge Leute mit Karte.", "Turns a percentage into a number of people."),
                                                                                                                   ("Quelle 2 sagt, dass alle mit Karte zahlen.", "Overstates the data.")],
    "Numbers + labels + source.", "Chart evidence must keep the groups and units straight and name the source.",
    ["62% → under 30; 25% → over 65."])
G.q("5 Aufsatz", r"Which phrase best explains what a statistic shows?",
    "Diese Zahlen belegen, dass…", [("Es war einmal…", "A storytelling opener."),
                                   ("Übrigens…", "An aside, not an explanation."),
                                   ("Um die Geschichte zu beginnen…", "Not an explanation.")],
    "Diese Zahlen belegen, dass…", "Argumentation (Row C) needs the step from evidence to claim.",
    ["Data → claim: diese Zahlen belegen, dass."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 4: Science and Technology: Question Set", r"Unit 4 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Audio and Chart and an Audio Report for listening, an Article and a Literary Text for reading) on bottle deposits, an early computer, a grandfather and his navigation system, and rural dead zones, followed by an Argumentative Essay with three sources and the 10-point scoring guide. As on the exam, questions and choices are in German; listening sources are printed as transcripts. All sources and data are original and fictional, written for practice. Allow about 25 minutes for the multiple choice and 55 minutes for the essay.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Essay: \blank\ / 10 \qquad Target: 15+ MCQ and 7+ essay \qquad Pace: 75 s per item",
        short="Unit 4", sub="Science and Technology")

Q.sec("Listening: Audio and Chart")
Q.src(r"Listening 1 \textperiodcentered\ Audio and Chart (transcript) \textperiodcentered\ „Die Flasche kommt zurück“, Radio Wissen", [
    r"(REPORTERIN) Wie viele Einwegflaschen und Dosen bringen die Menschen tatsächlich in den Laden zurück? Ein Institut hat die Rückgabequote in einer mittelgroßen Stadt über vier Jahre gemessen.",
    r"(REPORTERIN) Ergebnis: Die Quote stieg bis 2023 stetig an und sank 2024 zum ersten Mal leicht. Die Forscher erklären das mit neuen Getränkeautomaten an Bahnhöfen, deren Flaschen oft im normalen Mülleimer landen.",
    r"(FORSCHER) Das Pfandsystem funktioniert, weil es einen kleinen, aber direkten Vorteil gibt: 25 Cent pro Flasche. Wo aber kein Rückgabeautomat in der Nähe ist, wird die Flasche weggeworfen. Bequemlichkeit ist der größte Feind des Recyclings.",
], 5, table=(["Jahr", "Rückgabequote"], [["2021", "91~\\%"], ["2022", "94~\\%"], ["2023", "97~\\%"], ["2024", "95~\\%"]]),
      note="Anteil der zurückgegebenen Pfandflaschen und -dosen (fiktive Daten).")
Q.q("1.A.2 Data", r"In welchem Jahr war die Rückgabequote laut Tabelle am höchsten?",
    "2023", [("2021", "2021 is the lowest, 91%."),
             ("2022", "94%, less than 2023."),
             ("2024", "95%: it fell after 2023.")],
    "Peak: 97% in 2023.", "Data (1.A.2): find the maximum.",
    ["97 % is the highest value."])
Q.q("1.C.1 Connect", r"Wie erklären die Forscher die Veränderung von 2024 in der Tabelle?",
    "mit neuen Getränkeautomaten an Bahnhöfen, deren Flaschen oft im Müll landen", [("mit einer Erhöhung des Pfands", "Not mentioned."),
                                                                                       ("mit der Schließung der Supermärkte", "Not mentioned."),
                                                                                       ("mit weniger Verkäufen von Getränken", "Not mentioned.")],
    "Table: 97 → 95; audio: station vending machines.", "Connect (1.C.1): match the dip in the table with the cause in the audio.",
    ["sank 2024 … neue Getränkeautomaten an Bahnhöfen."])
Q.q("1.B.3 Point of view", r"Was ist laut dem Forscher „der größte Feind des Recyclings“?",
    "die Bequemlichkeit", [("das Pfand", "He says the deposit makes the system work."),
                           ("die Supermärkte", "Not stated."),
                           ("die Plastikflasche selbst", "Not stated.")],
    "Bequemlichkeit.", "Point of view (1.B.3): his conclusion.",
    ["Bequemlichkeit ist der größte Feind des Recyclings."])
Q.q("1.A.1 Detail", r"Wie hoch ist das Pfand pro Flasche laut Bericht?",
    "25 Cent", [("2,50 Euro", "No."),
                ("5 Cent", "No."),
                ("1 Euro", "No.")],
    "25 Cent.", "Detail (1.A.1).",
    ["25 Cent pro Flasche."])
Q.q("1.C.3 Inference", r"Was würde die Rückgabequote laut Forscher wahrscheinlich erhöhen?",
    "mehr Rückgabeautomaten in der Nähe der Menschen", [("ein Verbot von Getränken", "Not suggested."),
                                                       ("niedrigeres Pfand", "That would reduce the incentive."),
                                                       ("weniger Mülleimer", "Not suggested.")],
    "Convenience → returns.", "Inference (1.C.3): if inconvenience causes waste, nearby machines would help.",
    ["Wo kein Rückgabeautomat in der Nähe ist, wird die Flasche weggeworfen."])

Q.sec("Reading: Article")
Q.src(r"Reading 1 \textperiodcentered\ Article \textperiodcentered\ „Der Rechner im Wohnzimmer“", [
    r"Im Jahr 1941 stellte der Bauingenieur Konrad Zuse in Berlin eine Maschine vor, die heute als einer der ersten programmierbaren Rechner der Welt gilt: die Z3. Schon seine erste Rechenmaschine, die Z1, hatte er größtenteils in der Wohnung seiner Eltern gebaut, weil ihm die endlosen Berechnungen in seinem Beruf zu langweilig waren.",
    r"Die Z3 rechnete mit Relais, also elektrischen Schaltern, und mit dem binären System aus Nullen und Einsen, das bis heute die Grundlage aller Computer ist. Lange blieb Zuses Leistung im Ausland wenig bekannt, auch weil die Originalmaschine 1943 bei einem Bombenangriff zerstört wurde.",
    r"Heute kann man einen Nachbau im Deutschen Museum in München besichtigen. „Zuse zeigt, dass große Erfindungen nicht immer in großen Laboren entstehen“, sagt die Museumspädagogin Ines Hartmann, „sondern manchmal aus Langeweile und Neugier.“",
], 5)
Q.q("1.B.1 Main idea", r"Worum geht es hauptsächlich in dem Artikel?",
    "um die Entstehung und Bedeutung von Zuses früher Rechenmaschine", [("um die Geschichte des Deutschen Museums", "The museum is one detail."),
                                                                         ("um den Bombenkrieg in Berlin", "The bombing is one detail."),
                                                                         ("um moderne Smartphones", "No.")],
    "Z3: origin and significance.", "Main idea (1.B.1).",
    ["origin → how it worked → legacy."])
Q.q("1.A.1 Detail", r"Warum begann Zuse, Rechenmaschinen zu bauen?",
    "weil ihm die vielen Berechnungen in seinem Beruf zu langweilig waren", [("weil die Regierung es ihm befahl", "Not stated."),
                                                                             ("weil er Musik komponieren wollte", "No."),
                                                                             ("weil er ein Museum eröffnen wollte", "No.")],
    "aus Langeweile.", "Detail (1.A.1).",
    ["…weil ihm die endlosen Berechnungen … zu langweilig waren."])
Q.q("1.B.5 Word meaning", r"Im Artikel bedeutet „Relais“",
    "elektrische Schalter", [("kleine Glühbirnen", "No."),
                             ("Bücher mit Formeln", "No."),
                             ("Kabel für das Internet", "No.")],
    "Defined in the text.", "Word meaning (1.B.5): also elektrische Schalter.",
    ["Relais, also elektrischen Schaltern."])
Q.q("1.C.3 Inference", r"Warum war Zuses Leistung im Ausland lange wenig bekannt?",
    "auch weil die Originalmaschine im Krieg zerstört wurde", [("weil er sie geheim verkaufte", "Not stated."),
                                                              ("weil sie nicht funktionierte", "Not stated."),
                                                              ("weil sie zu klein war", "No.")],
    "Destroyed in 1943.", "Inference/detail: the text gives one reason with auch weil.",
    ["…auch weil die Originalmaschine 1943 … zerstört wurde."])
Q.q("1.B.3 Point of view", r"Was will Ines Hartmann mit ihrer Aussage zeigen?",
    "dass Erfindungen auch aus Neugier und Langeweile entstehen können", [("dass nur große Labore Erfindungen machen", "She says the opposite."),
                                                                          ("dass Museen langweilig sind", "No."),
                                                                          ("dass Zuse kein Ingenieur war", "He was a civil engineer.")],
    "nicht immer in großen Laboren.", "Point of view (1.B.3).",
    ["…sondern manchmal aus Langeweile und Neugier."])

Q.sec("Reading: Literary Text")
Q.src(r"Reading 2 \textperiodcentered\ Literary Text \textperiodcentered\ „Opa und das Navi“ (Auszug aus einer Erzählung)", [
    r"Mein Großvater hatte vierzig Jahre lang Lastwagen durch halb Europa gefahren, ohne je eine Landkarte zu falten. „Die Straßen stehen hier drin“, sagte er und tippte sich an die Stirn. Als wir ihm zum achtzigsten Geburtstag ein Navi schenkten, bedankte er sich höflich und legte es in die Schublade.",
    r"Erst im Frühling, als er mich zu einem Konzert nach Hamburg fahren wollte, holte er es heraus. Die Stimme sagte: „Bitte wenden.“ Opa fuhr geradeaus. „Bitte wenden.“ Opa fuhr weiter geradeaus und brummte: „Junge Frau, ich bin diese Strecke schon gefahren, da waren Sie noch nicht einmal programmiert.“",
    r"Wir kamen tatsächlich pünktlich an, über eine Landstraße, die auf keiner Karte des Geräts verzeichnet war. Auf dem Rückweg aber, im Dunkeln, ließ er das Navi die ganze Strecke reden, ohne ein Wort zu sagen. Vielleicht war es Müdigkeit. Vielleicht war es auch ein Waffenstillstand.",
], 5)
Q.q("1.A.1 Detail", r"Was tat der Großvater zuerst mit dem Navi?",
    "Er legte es in die Schublade.", [("Er benutzte es sofort auf jeder Fahrt.", "He put it away until spring."),
                                     ("Er gab es zurück.", "No."),
                                     ("Er verkaufte es.", "No.")],
    "…legte es in die Schublade.", "Detail (1.A.1).",
    ["bedankte er sich höflich und legte es in die Schublade."])
Q.q("1.B.3 Tone", r"Welcher Ton herrscht im zweiten Absatz vor?",
    "humorvoll", [("tragisch", "Nothing tragic happens."),
                  ("feindselig", "The grumbling is comic, not hostile."),
                  ("wissenschaftlich", "It is a personal story.")],
    "Arguing with a machine's voice.", "Tone (1.B.3): the grandfather answers the GPS voice as if it were a person.",
    ["Junge Frau, … noch nicht einmal programmiert → comic."])
Q.q("1.C.3 Inference", r"Was zeigt die Bemerkung „Die Straßen stehen hier drin“?",
    "dass der Großvater stolz auf sein Gedächtnis und seine Erfahrung ist", [("dass er Kopfschmerzen hat", "Literal misreading."),
                                                                             ("dass er Landkarten sammelt", "He never folded one."),
                                                                             ("dass er nicht lesen kann", "Not stated.")],
    "Pride in experience.", "Inference (1.C.3): tapping his forehead means the roads are in his memory.",
    ["hier drin + Stirn → memory."])
Q.q("1.B.5 Word meaning", r"Im Text bedeutet „Waffenstillstand“",
    "ein vorläufiger Frieden nach einem Streit", [("ein Unfall auf der Straße", "No."),
                                                  ("ein Halt an der Tankstelle", "No."),
                                                  ("eine neue Navigationsfunktion", "No.")],
    "truce.", "Word meaning (1.B.5): figurative: the grandfather and the GPS stop arguing.",
    ["ließ das Navi … reden, ohne ein Wort → truce."])
Q.q("1.C.2 Conclusion", r"Was deutet das Ende über die Beziehung des Großvaters zur Technik an?",
    "Er akzeptiert sie langsam, ohne seinen Stolz ganz aufzugeben.", [("Er hasst Technik für immer.", "He lets it guide him on the way home."),
                                                                     ("Er vertraut nur noch dem Navi.", "He took his own road on the way there."),
                                                                     ("Er verkauft sein Auto.", "No.")],
    "Gradual acceptance.", "Conclusions (1.C.2): the ambiguous ending (Müdigkeit or Waffenstillstand) suggests a truce, not surrender.",
    ["way there: his road; way back: the GPS → truce."])

Q.sec("Listening: Audio Report")
Q.src(r"Listening 2 \textperiodcentered\ Audio Report (transcript) \textperiodcentered\ „Leben im Funkloch“", [
    r"(REPORTER) In vielen Dörfern in Deutschland bricht das Handygespräch ab, sobald man aus dem Haus geht. Funklöcher, also Gebiete ohne Mobilfunkempfang, sind auf dem Land immer noch verbreitet.",
    r"(REPORTER) Für Landwirtin Petra Schmid in der Eifel ist das mehr als ein Ärgernis. „Mein Traktor könnte mit GPS viel genauer düngen und Wasser sparen. Aber ohne Netz funktioniert die Technik nicht.“",
    r"(EXPERTE) Das Problem ist wirtschaftlich: Für die Mobilfunkfirmen lohnt sich ein Mast in einem kleinen Dorf kaum. Deshalb fordern Gemeinden, dass der Staat den Ausbau stärker fördert.",
    r"(REPORTER) Bis dahin helfen sich manche Dörfer selbst: In einigen Orten haben Bürger Genossenschaften gegründet, um eigene Glasfaserleitungen zu verlegen.",
], 5)
Q.q("1.B.5 Word meaning", r"Was ist laut Bericht ein „Funkloch“?",
    "ein Gebiet ohne Mobilfunkempfang", [("ein Loch in der Straße", "Literal misreading."),
                                         ("ein Radiosender", "No."),
                                         ("ein kaputtes Handy", "No.")],
    "Defined in the source.", "Word meaning (1.B.5): also Gebiete ohne Mobilfunkempfang.",
    ["Funklöcher, also Gebiete ohne Mobilfunkempfang."])
Q.q("1.A.1 Detail", r"Warum ist das Funkloch für Petra Schmid ein Problem?",
    "weil ihr Traktor ohne Netz nicht mit GPS arbeiten kann", [("weil sie nicht mit ihrer Familie telefonieren kann", "Not her example."),
                                                              ("weil sie keine Musik streamen kann", "No."),
                                                              ("weil ihr Hof zu klein ist", "No.")],
    "GPS tractor needs network.", "Detail (1.A.1).",
    ["…ohne Netz funktioniert die Technik nicht."])
Q.q("1.C.3 Inference", r"Warum gibt es laut Experte in kleinen Dörfern oft keinen Mast?",
    "weil es sich für die Firmen wirtschaftlich kaum lohnt", [("weil die Bewohner keine Handys haben", "No."),
                                                             ("weil Masten verboten sind", "No."),
                                                             ("weil das Wetter zu schlecht ist", "No.")],
    "Not profitable.", "Detail/inference: das Problem ist wirtschaftlich.",
    ["…lohnt sich ein Mast … kaum."])
Q.q("1.B.1 Purpose", r"Was ist der Hauptzweck des Berichts?",
    "ein Problem auf dem Land und mögliche Lösungen darzustellen", [("ein neues Handy zu bewerben", "No sales pitch."),
                                                                    ("Landwirte zu kritisieren", "No."),
                                                                    ("die Geschichte des Telefons zu erzählen", "No.")],
    "Problem + solutions.", "Purpose (1.B.1): problem, example, cause, responses.",
    ["Funklöcher → example → cause → state support and cooperatives."])
Q.q("1.C.2 Conclusion", r"Was zeigt das Beispiel der Genossenschaften?",
    "dass manche Dörfer selbst handeln, statt auf den Staat zu warten", [("dass der Staat alles bezahlt", "They act before state support arrives."),
                                                                         ("dass Glasfaser verboten ist", "No."),
                                                                         ("dass niemand Internet will", "The opposite.")],
    "Self-help.", "Conclusions (1.C.2): Bis dahin helfen sich manche Dörfer selbst.",
    ["Bürger gründen Genossenschaften → self-help."])

Q.frq(kind="Argumentative Essay", head=r"Question 3 \textperiodcentered\ Argumentative Essay \textperiodcentered\ 10 points \textperiodcentered\ 55 minutes", mins=55,
      directions=[r"Sie schreiben einen argumentativen Aufsatz für einen Universitätskurs. Lesen Sie das Thema und die schriftlichen Quellen; hören Sie dann die Audioquelle (hier als Transkript). Schreiben Sie einen Aufsatz, der Informationen aus allen drei Quellen verwendet, um Ihre Position zu unterstützen. Geben Sie die Quellen mit Nummer, Titel oder Autor an."],
      sources=[dict(title=r"Quelle 1 \textperiodcentered\ Artikel \textperiodcentered\ „Das Café ohne Kasse“", paras=[
          r"Seit einem Jahr nimmt das Café „Bohne“ in Hamburg kein Bargeld mehr an. „Wir sparen jeden Abend eine Stunde Kassenabrechnung, und es gibt keine Überfälle mehr“, erklärt die Besitzerin Julia Petersen.",
          r"Die meisten jungen Gäste finden das praktisch. Doch nicht alle sind zufrieden: Einige ältere Stammgäste, die keine Karte benutzen wollen, kommen seitdem seltener. „Ich möchte nicht, dass jemand weiß, wann ich wo meinen Kaffee trinke“, sagt Herr Kowalski, 78."]),
               dict(title=r"Quelle 2 \textperiodcentered\ Grafik \textperiodcentered\ Wie zahlen die Menschen im Laden am häufigsten?", paras=[
          r"Umfrage in Deutschland und Österreich nach Altersgruppen (fiktive Daten). Anteil, der meistens mit Karte oder Handy zahlt."],
                    table=(["Altersgruppe", "Meistens Karte oder Handy"], [["18--29 Jahre", "62~\\%"], ["30--49 Jahre", "51~\\%"], ["50--64 Jahre", "38~\\%"], ["65 Jahre und älter", "25~\\%"]])),
               dict(title=r"Quelle 3 \textperiodcentered\ Audio (Transkript) \textperiodcentered\ „Geld und Daten“, Radiosendung", paras=[
          r"(MODERATORIN) Wir sprechen mit der Datenschutzexpertin Dr. Katharina Wolf. Sollte man Bargeld abschaffen?",
          r"(DR. WOLF) Digitales Bezahlen ist bequem, keine Frage. Aber jede Kartenzahlung hinterlässt eine Datenspur: wo, wann, wofür. Bargeld ist die einzige Zahlungsart, die wirklich anonym ist. Außerdem funktioniert es auch bei einem Stromausfall oder einem Cyberangriff.",
          r"(MODERATORIN) Was schlagen Sie vor?",
          r"(DR. WOLF) Wahlfreiheit. Wer digital zahlen will, soll das tun können. Aber Geschäfte sollten weiterhin verpflichtet sein, Bargeld anzunehmen."])],
      prompt=[r"Thema des Aufsatzes: \textbf{Sollte Bargeld abgeschafft werden?}"],
      model=[r"In vielen Ländern zahlen die Menschen immer seltener bar, und manche Geschäfte nehmen gar kein Bargeld mehr an. Sollte man Bargeld also ganz abschaffen? Ich bin der Ansicht, dass Bargeld erhalten bleiben sollte, auch wenn digitales Bezahlen viele Vorteile hat.",
             r"Erstens schützt Bargeld die Privatsphäre. Wie die Datenschutzexpertin Dr. Katharina Wolf in Quelle 3 erklärt, hinterlässt jede Kartenzahlung eine Datenspur, die zeigt, wo, wann und wofür man Geld ausgibt. Herr Kowalski in Quelle 1 drückt genau diese Sorge aus: Er möchte nicht, dass jemand weiß, wann er wo seinen Kaffee trinkt. Das zeigt, dass Bargeld für viele Menschen mehr ist als ein Zahlungsmittel: Es ist ein Stück Freiheit.",
             r"Zweitens würde eine Abschaffung vor allem ältere Menschen ausschließen. Laut der Grafik in Quelle 2 zahlen nur 25~\% der über 65-Jährigen meistens mit Karte oder Handy, während es bei den 18- bis 29-Jährigen 62~\% sind. Diese Zahlen belegen, dass ein großer Teil der Bevölkerung noch auf Bargeld angewiesen ist. Das Café in Quelle 1 hat bereits erlebt, dass ältere Stammgäste seltener kommen.",
             r"Zwar spart bargeldloses Zahlen Zeit und erhöht die Sicherheit, wie die Besitzerin des Cafés betont (Quelle 1). Dennoch spricht auch die Sicherheit für Bargeld: Laut Dr. Wolf funktioniert es sogar bei einem Stromausfall oder einem Cyberangriff, wenn digitale Systeme versagen.",
             r"Zusammenfassend lässt sich sagen: Wenn Bargeld abgeschafft würde, verlören viele Menschen ein Stück Freiheit und Sicherheit. Die beste Lösung ist deshalb Wahlfreiheit, wie Dr. Wolf sie vorschlägt: Jeder sollte selbst entscheiden können, wie er bezahlt."],
      rows=[("A Position", 1, "a clear position (keep cash; freedom of choice)", "only lists advantages and disadvantages"),
            ("B Source use", 2, "all three sources used accurately and named; age groups kept straight", "two sources, or mixing up the chart's groups"),
            ("C Argumentation", 2, "each claim explained with evidence (das zeigt, diese Zahlen belegen)", "quotes and numbers with no link to the claims"),
            ("D Organization", 2, "introduction, two claims, concession and rebuttal, conclusion", "one paragraph per source"),
            ("E Language control", 3, "varied structures: passive with Konjunktiv II, verb-final clauses, während", "basic structures; copying the sources")],
      tips=["The position is clear and keeps the opposing view in view (auch wenn…).", "The concession uses the café owner's argument, then turns security into a reason for cash (Dr. Wolf).",
            "Every source is named and paraphrased.", "The conclusion's Konjunktiv II passive (wenn Bargeld abgeschafft würde, verlören…) shows control."],
      ask="Write your essay in German (about 300–350 words), then mark it against each row.", lines=22)

GUIDE, QSET = G, Q
