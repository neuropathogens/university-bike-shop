from ap_wl.model import Doc

STEM = "03-art-creativity"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 3: Art and Creativity", r"Unit 3 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 3 asks how art expresses identity and values, and how traditions are preserved and reinvented. Its recommended contexts are artistic heritage, architecture, beauty and aesthetics, fashion and design, literature, and the visual and performing arts. Music is the lens of the 2026--27 course project, so this guide gives it the most space: from Bach and Beethoven to brass bands, yodeling, Schlager, Kraftwerk and techno, and what each expresses. It also covers architecture (the Gothic, the Bauhaus), literature from Goethe to Kafka, the language for describing and evaluating art, and a Project Presentation kit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 11+ \qquad Three factors for my project: \blank[10em]",
        short="Unit 3", sub="Art and Creativity")

G.sec("Music in the German-speaking world")
G.tex(r"""
\begin{vocab}
die Musikrichtung / das Genre & genre & \\
der Text / der Refrain & lyrics / chorus & \\
die Blaskapelle / die Blasmusik & brass band / brass-band music & village festivals in Bavaria and Austria \\
das Jodeln & yodeling & Switzerland, Austria, Bavaria \\
der Chor / das Ensemble & choir / ensemble & many towns have several amateur choirs \\
der Schlager & popular sentimental song & \\
die Orgel / der Orgelbau & organ / organ building & UNESCO intangible heritage (2017) \\
komponieren / aufführen / aufnehmen & compose / perform / record & \\
\end{vocab}

\begin{compare}{Tradition}{Where and when}{What it often expresses}
Classical music (Bach, Mozart, Beethoven, Brahms) & Leipzig, Salzburg, Bonn, Vienna; 18th--19th c. & universal ideals; Beethoven's ``Ode to Joy'' (text by Schiller) is the European anthem \\
Volksmusik and Blasmusik & Alpine regions & community, the village, the seasons \\
Liedermacher (singer-songwriters) & 1960s--80s, East and West & political and social critique \\
Kraftwerk & Düsseldorf, from 1970 & pioneers of electronic pop; machines and modernity \\
Techno & Berlin, after 1989 & freedom and reunion in a reunified city \\
Deutschrap & from the 1990s & urban life, identity, migration \\
\end{compare}

\begin{keyidea}[Products, practices, perspectives in music]
\textbf{Product}: a song, the organ, a genre. \textbf{Practice}: the brass band playing at every village festival; singing in a choir; dancing at a Viennese ball. \textbf{Perspective}: the value behind it (community, tradition, freedom, a shared European ideal). The presentation's culture row asks for the link: practice + \emph{weil} / \emph{was zeigt, dass} + perspective.
\end{keyidea}
""")
G.q("1 Musik", r"Warum ist Beethovens „Ode an die Freude“ heute auch politisch bedeutend?",
    "weil sie die Hymne der Europäischen Union ist", [("weil sie die deutsche Nationalhymne ist", "The German anthem is the Deutschlandlied (third stanza)."),
                                                     ("weil sie im Fernsehen verboten wurde", "No."),
                                                     ("weil Kraftwerk sie geschrieben hat", "Beethoven composed it; Schiller wrote the text.")],
    "Ode to Joy = EU anthem.", "Beethoven's setting of Schiller's poem is the anthem of the European Union.",
    ["Schiller + Beethoven → Europahymne."])
G.q("1 Musik", r"Which sentence links a musical practice to a cultural perspective?",
    "In vielen Alpendörfern spielt die Blaskapelle bei jedem Fest, was zeigt, wie wichtig Gemeinschaft und Tradition sind.",
    [("Eine Blaskapelle hat Trompeten und eine Tuba.", "A product described with no perspective."),
     ("Kraftwerk wurde 1970 gegründet.", "A date, no perspective."),
     ("Ich höre gern Schlager.", "A personal preference, not a cultural example.")],
    "Practice + was zeigt + perspective.", "The top culture score needs a specific practice or product tied to the value behind it.",
    ["Practice: the brass band at every festival.", "Perspective: community and tradition."])
G.q("1 Musik", r"Die Band Kraftwerk aus Düsseldorf ist bekannt als",
    "Pionier der elektronischen Popmusik", [("berühmtester Chor Österreichs", "That would be the Wiener Sängerknaben."),
                                           ("Erfinderin des Jodelns", "Yodeling is far older."),
                                           ("Komponistin der Europahymne", "That is Beethoven.")],
    "Kraftwerk = electronic pioneers.", "From 1970 Kraftwerk shaped electronic pop and later techno.",
    ["Düsseldorf, Synthesizer → elektronische Musik."])

G.sec("Heritage and architecture")
G.tex(r"""
\begin{vocab}
das Erbe / das Weltkulturerbe & heritage / World Heritage & \\
das Meisterwerk & masterpiece & \\
der Dom / die Kathedrale & cathedral & \\
das Fachwerkhaus & half-timbered house & \\
das Schloss / die Burg & palace / castle & \\
restaurieren / erhalten & to restore / to preserve & \\
\end{vocab}

\begin{compare}{Work or place}{What it is}{Why it matters}
Kölner Dom & Gothic cathedral, begun 1248, completed 1880 & a symbol of Cologne; survived the bombing of the Second World War \\
Bauhaus & art and design school founded by Walter Gropius in Weimar in 1919 & ``form follows function''; modern design worldwide \\
Schloss Neuschwanstein & 19th-century castle of Ludwig II of Bavaria & Romantic dreams; a model for fairy-tale castles \\
Wiener Ringstraße & 19th-century boulevard around Vienna's center & opera, parliament, museums: culture as a public good \\
\end{compare}

\textbf{The Bauhaus} brought artists and craftspeople together to design simple, functional objects for everyday life. The perspective: good design should be affordable and useful for everyone, not only decorative.
""")
G.q("2 Erbe", r"Was war das Ziel des Bauhauses?",
    "einfache, funktionale Gegenstände für den Alltag zu gestalten", [("prächtige Schlösser für Könige zu bauen", "That is Neuschwanstein's world."),
                                                                     ("gotische Kirchen zu restaurieren", "No."),
                                                                     ("Volksmusik zu fördern", "No.")],
    "Form follows function.", "The Bauhaus (1919) joined art and craft to design functional, affordable objects.",
    ["Bauhaus → Funktion, Alltag."])
G.q("2 Erbe", r"The Kölner Dom was begun in 1248 and finished in",
    "1880", [("1350", "Work stopped for centuries."),
             ("1919", "1919 is the founding of the Bauhaus."),
             ("1990", "1990 is reunification.")],
    "1248–1880.", "Construction paused for about 300 years and resumed in the 19th century.",
    ["completed 1880."])

G.sec("Literature and visual art")
G.tex(r"""
\begin{compare}{Author or artist}{Known for}{Theme}
Johann Wolfgang von Goethe & \emph{Faust} & the striving human being; knowledge and its price \\
Friedrich Schiller & dramas; the ``Ode to Joy'' & freedom, brotherhood \\
Brüder Grimm & \emph{Kinder- und Hausmärchen} (1812) & collected folk tales; the German language \\
Franz Kafka (Prague) & \emph{Die Verwandlung} (1915) & alienation, bureaucracy \\
Thomas Mann & \emph{Buddenbrooks}; Nobel Prize 1929 & the decline of a family \\
Gustav Klimt (Vienna) & \emph{Der Kuss} & gold, ornament, Jugendstil \\
\end{compare}

\textbf{The Grimms' tales} were collected as part of an effort to preserve popular German culture and language at a time when Germany was not yet a unified state. The perspective: stories told in families are a shared heritage.
""")
G.q("3 Literatur", r"Warum sammelten die Brüder Grimm Märchen?",
    "um volkstümliche Geschichten und die deutsche Sprache zu bewahren", [("um Werbung für Schlösser zu machen", "No."),
                                                                          ("um Kinder zu erschrecken", "Not the purpose."),
                                                                          ("um englische Märchen zu übersetzen", "They collected German-language tales.")],
    "Preserve folk culture.", "The Grimms collected tales to preserve a shared culture and language.",
    ["sammeln → bewahren."])
G.q("3 Literatur", r"Franz Kafka wrote in German but lived in",
    "Prague", [("Vienna only", "He visited Vienna, but lived and wrote in Prague."),
               ("Zurich", "No."),
               ("Berlin his whole life", "He lived briefly in Berlin at the end of his life; his home was Prague.")],
    "Kafka → Prague.", "German-language literature was written across Central Europe, not only in Germany and Austria.",
    ["Prague, German-language."])

G.sec("Describing and evaluating art")
G.tex(r"""
\begin{compare}{Purpose}{Language}{Example}
Describe & zeigt, stellt dar, im Vordergrund / im Hintergrund & Im Vordergrund sieht man ein Paar in goldenen Gewändern. \\
Interpret & symbolisiert, drückt aus, erinnert an & Das Gold symbolisiert Wert und Ewigkeit. \\
Evaluate & Was mir besonders auffällt, ist\ldots; Ich finde es beeindruckend, dass\ldots & Was mir auffällt, ist die Mischung aus Alt und Neu. \\
Concede & obwohl + verb last; zwar\ldots aber & Obwohl manche Schlager kitschig finden, ist er sehr beliebt. \\
Influence & beeinflussen, sich inspirieren lassen von & Die Band ließ sich von der Volksmusik inspirieren. \\
\end{compare}

\begin{trap}
\emph{Obwohl} sends the verb to the end; \emph{trotzdem} takes first position with the verb second. \emph{Obwohl es kitschig ist, \ldots} / \emph{Es ist kitschig. Trotzdem ist es beliebt.}
\end{trap}
""")
G.q("4 Beschreiben", r"Wählen Sie den richtigen Satz.",
    "Obwohl manche Kritiker Schlager kitschig finden, hören ihn Millionen Menschen.", [("Obwohl manche Kritiker finden Schlager kitschig, hören ihn Millionen Menschen.", "Obwohl sends the verb to the end."),
                                                                                       ("Obwohl manche Kritiker Schlager kitschig finden, Millionen Menschen hören ihn.", "After the subordinate clause, the main verb comes first."),
                                                                                       ("Trotzdem manche Kritiker Schlager kitschig finden, hören ihn Millionen.", "Trotzdem is not a subordinating conjunction.")],
    "obwohl → verb last; then verb first.", "A fronted subordinate clause fills position one; the main clause begins with the verb.",
    ["Obwohl … finden, hören …"])
G.q("4 Beschreiben", r"Wählen Sie die richtige Form: Die Band \blank\ sich von alten Volksliedern inspirieren.",
    "ließ", [("ließen", "Die Band is singular: ließ."),
             ("hat", "Hat sich … inspirieren would need lassen: hat sich … inspirieren lassen."),
             ("wurde", "Wurde would need a participle: wurde … inspiriert.")],
    "sich inspirieren lassen.", "Lassen + infinitive: sich von etwas inspirieren lassen (to be inspired by).",
    ["ließ sich … inspirieren."])

G.sec("Task kit: the Project Presentation")
G.tex(r"""
You have 3 minutes to prepare (with your PPR) and 3 minutes to present, about 350--400 words. The prompt asks what you learned in your research; the rubric rewards \textbf{three or more factors, each explained with details}, and a cultural perspective linked to a product or practice.

\begin{terms}
0:00--0:25 & introduction: the question, your focus, the three factors \\
0:25--2:30 & three factors, about 40 seconds each: fact or example from research + why it matters (perspective) \\
2:30--3:00 & conclusion: what the factors show together; a comparison or reflection \\
\end{terms}

\begin{compare}{Move}{Phrases}{}
Open & Heute spreche ich über\ldots; Ich habe mich auf drei Aspekte konzentriert: \ldots & \\
Move on & Erstens / Zweitens / Schließlich & \\
Evidence & Bei meiner Recherche habe ich herausgefunden, dass\ldots; Zum Beispiel\ldots & \\
Perspective & Das spiegelt wider, dass\ldots; das zeigt, wie wichtig\ldots ist & \\
Close & Zusammenfassend\ldots; Ich habe gelernt, dass\ldots & \\
\end{compare}

\begin{trap}
Three factors named with no detail earn only 1 point for task; so does one factor explained in depth. Budget time so the third factor gets real detail.
\end{trap}
""")
G.q("5 Präsentation", r"A presentation explains three factors, each with a specific example from research, but never links them to what people value. Which row is it most likely to lose points in?",
    "Cultural understanding", [("Task execution", "Three factors with relevant details earn full task credit."),
                               ("Delivery", "Delivery is about pronunciation and pace."),
                               ("Organization", "Nothing suggests poor organization.")],
    "No perspective link → culture row.", "Row B's top score needs a relationship between a perspective and a product or practice.",
    ["Factors and details → task OK.", "No perspective → culture 1 point."])
G.q("5 Präsentation", r"About how many words fit in the 3-minute presentation at a natural pace?",
    "350 to 400", [("100 to 150", "That would leave long silences."),
                   ("800 to 900", "That would require rushing, which hurts delivery."),
                   ("50", "That is one short paragraph.")],
    "3 min ≈ 350–400 words.", "At about two words per second, three minutes holds 350–400 words.",
    ["Plan about 120 words per factor."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 3: Art and Creativity: Question Set", r"Unit 3 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Instructional Guidance and an Interview for listening, an Article and Chart and a Promotional Material for reading) on yodeling, streaming, a lakeside music festival and a young brass musician, followed by a practice Project Presentation on music, the 2026--27 project lens, with the 11-point scoring guide and a model script. The presentation prompt is a practice prompt written for this set, not the official 2027 project prompt. As on the exam, questions and choices are in German; listening sources are printed as transcripts. All sources and data are original and fictional. Allow about 25 minutes for the multiple choice and 6 minutes to prepare and deliver the presentation.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Presentation: \blank\ / 11 \qquad Target: 15+ MCQ and 8+ presentation",
        short="Unit 3", sub="Art and Creativity")

Q.sec("Listening: Instructional Guidance")
Q.src(r"Listening 1 \textperiodcentered\ Instructional Guidance (transcript) \textperiodcentered\ „Dein erster Jodelkurs“, ein Video-Tutorial", [
    r"(LEHRERIN) Grüezi! Heute lernst du die Grundlage des Jodelns: den Wechsel zwischen Brust- und Kopfstimme. Stell dich zuerst gerade hin, die Füße schulterbreit auseinander, und atme tief in den Bauch.",
    r"(LEHRERIN) Sing jetzt einen tiefen Ton auf „o“ mit deiner normalen Sprechstimme, das ist die Bruststimme. Dann spring auf einen hohen Ton auf „i“, ganz leicht, fast wie ein Kinderlachen, das ist die Kopfstimme.",
    r"(LEHRERIN) Wiederhole langsam: tief, hoch, tief, hoch. Der kleine Bruch in der Stimme, dieser „Kehlkopfschlag“, ist kein Fehler, sondern genau das, was das Jodeln ausmacht.",
    r"(LEHRERIN) Ein letzter Tipp: Früher riefen sich Hirten in den Bergen mit solchen Rufen über die Täler hinweg zu. Wenn du jodelst, stell dir vor, dass dich jemand auf der anderen Seite hören soll.",
], 5)
Q.q("1.A.1 Detail", r"Was soll man laut der Lehrerin zuerst tun?",
    "sich gerade hinstellen und tief in den Bauch atmen", [("einen hohen Ton auf „i“ singen", "That comes later."),
                                                          ("schnell zwischen den Tönen wechseln", "She says to repeat slowly."),
                                                          ("ein Jodellied auswendig lernen", "Not one of the steps.")],
    "Stell dich zuerst gerade hin…", "Instructional Guidance: zuerst marks the first step.",
    ["Stell dich zuerst gerade hin … atme tief in den Bauch."])
Q.q("1.A.1 Detail", r"Wie entsteht laut Tutorial die Kopfstimme?",
    "durch einen leichten, hohen Ton auf „i“", [("durch einen tiefen Ton auf „o“", "That is the chest voice."),
                                               ("durch lautes Schreien", "She says ganz leicht."),
                                               ("durch Summen mit geschlossenem Mund", "Not described.")],
    "hoch + „i“ + leicht = Kopfstimme.", "Detail (1.A.1): match each voice with its description.",
    ["einen hohen Ton auf „i“, ganz leicht → Kopfstimme."])
Q.q("1.B.3 Point of view", r"Wie bewertet die Lehrerin den kleinen Bruch in der Stimme?",
    "als typisches Merkmal des Jodelns", [("als Fehler, den man vermeiden muss", "She says it is not a mistake."),
                                         ("als Zeichen von Müdigkeit", "No."),
                                         ("als Problem nur für Anfänger", "No.")],
    "kein Fehler, sondern…", "Point of view (1.B.3): kein … sondern states her view.",
    ["…kein Fehler, sondern genau das, was das Jodeln ausmacht."])
Q.q("1.B.4 Organization", r"Wie ist das Tutorial aufgebaut?",
    "in Schritten, von der Haltung über die Stimme bis zu einem letzten Tipp", [("als Vergleich zwischen zwei Ländern", "No comparison."),
                                                                               ("als Geschichte des Jodelns von Anfang an", "History appears only in the last tip."),
                                                                               ("als Liste von Fragen und Antworten", "No Q&A.")],
    "zuerst … jetzt … dann … ein letzter Tipp.", "Organization (1.B.4): sequence markers order the steps.",
    ["posture → voices → practice → tip."])
Q.q("1.C.3 Inference", r"Was will die Lehrerin mit ihrem letzten Tipp vermitteln?",
    "dass Jodeln ursprünglich eine Art war, sich über weite Entfernungen zu verständigen", [("dass man nur in den Bergen jodeln darf", "No."),
                                                                                             ("dass Hirten heute noch jodeln müssen", "Früher refers to the past."),
                                                                                             ("dass man leise jodeln soll", "The opposite.")],
    "Calls across valleys.", "Inference (1.C.3): the history explains the practice's purpose.",
    ["Hirten riefen sich über die Täler hinweg zu → communication."])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 1 \textperiodcentered\ Article and Chart \textperiodcentered\ „Was hört die Generation Z?“, Zeitung Die Brücke", [
    r"Eine Studie einer Streaming-Plattform mit 50.000 Nutzerinnen und Nutzern zwischen 16 und 24 Jahren in Deutschland, Österreich und der Schweiz bestätigt, was viele Eltern vermutet haben: Deutschrap dominiert die Kopfhörer der Jugendlichen.",
    r"Doch die Studie enthält eine Überraschung. Volksmusik und Blasmusik sind im letzten Jahr stärker gewachsen als jedes andere Genre, auch wenn sie nur einen kleinen Teil ausmachen. „Jugendliche entdecken diese Musik über Remixe und kurze Clips in sozialen Netzwerken“, erklärt die Musikwissenschaftlerin Eva Lang. „Ein DJ sampelt eine Tuba, und plötzlich suchen Tausende die Original-Blaskapelle.“",
    r"Für Lang verschwindet die Tradition nicht, sondern sie verändert ihre Form. „Jede Generation hört ihre Großeltern auf ihre eigene Weise.“",
], 5, table=(["Genre", "Anteil an der Hörzeit", "Veränderung in einem Jahr"],
             [["Deutschrap und Urban", "46~\\%", "+4~\\%"], ["Pop", "27~\\%", "−2~\\%"], ["Rock", "12~\\%", "−5~\\%"], ["Volks- und Blasmusik", "6~\\%", "+31~\\%"]]),
      note="Fiktive Daten.")
Q.q("1.A.2 Data", r"Welches Genre hat laut Tabelle den größten Anteil an der Hörzeit?",
    "Deutschrap und Urban", [("Volks- und Blasmusik", "It grew most but is only 6%."),
                             ("Pop", "27%."),
                             ("Rock", "12%.")],
    "46%.", "Data (1.A.2): read the share column, not growth.",
    ["Share column → 46%."])
Q.q("1.C.1 Connect", r"Welche Zahl in der Tabelle passt zur „Überraschung“ im Artikel?",
    "das Wachstum der Volks- und Blasmusik um 31~\\%", [("die 46~\\% des Deutschraps", "That confirms what parents suspected."),
                                                       ("der Rückgang des Rocks um 5~\\%", "Rock is not discussed."),
                                                       ("die 27~\\% des Pops", "Not discussed.")],
    "Surprise = folk and brass grew most.", "Connect (1.C.1): match the article's surprise to the +31% figure.",
    ["stärker gewachsen als jedes andere Genre → +31%."])
Q.q("1.B.5 Word meaning", r"Im Artikel bedeutet „sampelt“, dass der DJ",
    "einen aufgenommenen Ausschnitt einer Tuba in seinen Track einbaut", [("Tuba spielen lernt", "He uses a recording."),
                                                                         ("die Blasmusik kritisiert", "No criticism."),
                                                                         ("eine alte Tuba verkauft", "Unrelated.")],
    "sampeln = to sample.", "Word meaning (1.B.5): context (Remixe, Clips, Original-Blaskapelle) shows reuse of a recording.",
    ["Remixe + Original suchen → a sample."])
Q.q("1.B.3 Point of view", r"Welche Meinung vertritt Eva Lang?",
    "Die musikalische Tradition verschwindet nicht, sondern verändert sich.", [("Jugendliche interessieren sich nicht mehr für Volksmusik.", "She says they discover it."),
                                                                                ("Deutschrap zerstört die Volkskultur.", "She never says so."),
                                                                                ("Remixe sind respektlos.", "She describes them as a way in.")],
    "verändert ihre Form.", "Point of view (1.B.3): her final quote states her view.",
    ["…verschwindet nicht, sondern … verändert ihre Form."])
Q.q("1.C.2 Conclusion", r"Welche Schlussfolgerung erlaubt der Artikel?",
    "Remixe können Jugendliche zur Musik ihrer Großeltern führen.", [("Volksmusik wird nächstes Jahr Deutschrap überholen.", "6% versus 46%: not supported."),
                                                                      ("Pop wächst stärker denn je.", "Pop fell 2%."),
                                                                      ("Jugendliche hören nur noch Volksmusik.", "Only 6%.")],
    "Remix → discovery.", "Conclusions (1.C.2) must stay within the evidence.",
    ["A DJ's sample sends listeners to the original band."])

Q.sec("Reading: Promotional Material")
Q.src(r"Reading 2 \textperiodcentered\ Promotional Material \textperiodcentered\ Ein Festivalplakat", [
    r"\textbf{MUSIKSOMMER AM SEE 2027 \textperiodcentered\ Bregenz, Bodensee}",
    r"Drei Tage, vier Bühnen, über vierzig Bands aus fünf Ländern. Von der Blaskapelle bis zum Elektro-Jodel, vom Alphorn bis zum Rap im Dialekt: Tradition kann man auch tanzen!",
    r"\textbf{Neu in diesem Jahr:} kostenlose Workshops für Alphorn, Hackbrett und Jodeln, direkt mit den Musikerinnen und Musikern. Anmeldung am Infostand (begrenzte Plätze, wer zuerst kommt, mahlt zuerst).",
    r"\textbf{Tickets:} 3-Tages-Pass 90 Euro; Kinder unter 12 Jahren frei. Studierende mit Ausweis: 50~\% Ermäßigung.",
    r"7. bis 9. Juli \textperiodcentered\ Seebühne \textperiodcentered\ Glasflaschen sind auf dem Gelände verboten.",
], 5)
Q.q("1.B.1 Purpose", r"Was ist der Hauptzweck des Plakats?",
    "das Publikum zu einem Festival für traditionelle und moderne Musik einzuladen", [("die Eröffnung einer Musikschule anzukündigen", "Workshops are one feature of a festival."),
                                                                                       ("Musikinstrumente zu verkaufen", "Only tickets are sold."),
                                                                                       ("einen Tanzwettbewerb vorzustellen", "No contest.")],
    "Festival poster → invite.", "Purpose (1.B.1): title, dates, place and prices invite people to attend.",
    ["Promotional Material → invitation."])
Q.q("1.A.1 Detail", r"Wie kann man an den Workshops teilnehmen?",
    "durch Anmeldung am Infostand des Festivals", [("mit einem speziellen Online-Ticket", "The workshops are free; registration is at the stand."),
                                                   ("mit dem eigenen Alphorn", "Not stated."),
                                                   ("mit einem Bewerbungsvideo", "Not stated.")],
    "Anmeldung am Infostand.", "Detail (1.A.1).",
    ["Anmeldung am Infostand."])
Q.q("1.C.2 Conclusion", r"Eine Studentin mit Ausweis kauft einen 3-Tages-Pass. Wie viel zahlt sie?",
    "45 Euro", [("90 Euro", "Students get 50% off."),
                ("nichts", "Only children under 12 enter free."),
                ("50 Euro", "50 is the discount percentage, not a price.")],
    "90 − 50% = 45.", "Apply the details: the pass costs 90 euros, and students pay half.",
    ["90 × 0,5 = 45."])
Q.q("1.B.5 Word meaning", r"Was bedeutet hier „wer zuerst kommt, mahlt zuerst“?",
    "Die Plätze bekommen die Ersten, die sich anmelden.", [("Man muss Getreide mahlen.", "Literal misreading of a proverb."),
                                                          ("Man muss früh frühstücken.", "No."),
                                                          ("Die Workshops beginnen sehr früh.", "Not the meaning.")],
    "Proverb: first come, first served.", "Word meaning (1.B.5): an idiom explained by begrenzte Plätze.",
    ["begrenzte Plätze + Sprichwort → first come, first served."])
Q.q("1.A.1 Detail", r"Was ist auf dem Festivalgelände verboten?",
    "Glasflaschen", [("Kinder unter 12 Jahren", "They enter free."),
                     ("Tanzen vor den Bühnen", "Dancing is encouraged."),
                     ("Fotografieren", "Not mentioned.")],
    "Glasflaschen verboten.", "Detail (1.A.1) from the last line.",
    ["Glasflaschen sind auf dem Gelände verboten."])

Q.sec("Listening: Interview")
Q.src(r"Listening 2 \textperiodcentered\ Interview (transcript) \textperiodcentered\ Ein junger Tubist aus Tirol", [
    r"(REPORTERIN) Lukas, du bist 23 und spielst mit deiner Band auf großen Festivals. Wie hat alles angefangen?",
    r"(LUKAS) In der Blaskapelle meines Dorfes. Mein Opa hat dort Trompete gespielt, mein Vater Posaune, und mit acht habe ich die Tuba bekommen. Bei uns lernt man nicht zuerst Noten, sondern man spielt bei jedem Fest mit, bei der Prozession, beim Feuerwehrfest, bei Hochzeiten.",
    r"(REPORTERIN) Heute mischst du Blasmusik mit Techno. Was sagen die Traditionalisten?",
    r"(LUKAS) Manche sagen, das sei Verrat. Ich respektiere sie, aber ich sehe das anders. Die Blasmusik hat immer Neues aufgenommen, Märsche, Polkas, später Pop. Wenn sie sich nicht verändern würde, wäre sie längst tot.",
    r"(REPORTERIN) Was würdest du nie ändern?",
    r"(LUKAS) Das Gemeinsame. Eine Blaskapelle ist keine Show, sondern ein Dorf, das zusammen spielt. Wenn das verloren geht, ist es keine Blasmusik mehr.",
], 5)
Q.q("1.A.1 Detail", r"Wo hat Lukas angefangen, Musik zu machen?",
    "in der Blaskapelle seines Dorfes", [("in einer Musikschule in Wien", "Not mentioned."),
                                          ("auf einem großen Festival", "He plays there now."),
                                          ("in einem Techno-Club", "Not mentioned.")],
    "In der Blaskapelle meines Dorfes.", "Detail (1.A.1): his first answer.",
    ["In der Blaskapelle meines Dorfes."])
Q.q("1.C.3 Inference", r"Was kann man über die traditionelle Art vermuten, in der Blaskapelle zu lernen?",
    "Man lernt durch Mitspielen bei Festen im Dorf und in der Familie.", [("Man lernt nur am Konservatorium.", "He says one plays along at every festival."),
                                                                          ("Man darf erst als Erwachsener mitspielen.", "He started at eight."),
                                                                          ("Man lernt nur aus Büchern.", "Not notes first.")],
    "nicht zuerst Noten … bei jedem Fest.", "Inference (1.C.3): informal, community-based learning.",
    ["…man spielt bei jedem Fest mit."])
Q.q("1.B.3 Attitude", r"Welche Haltung hat Lukas gegenüber den Traditionalisten?",
    "Er respektiert sie, ist aber anderer Meinung.", [("Er verachtet sie.", "He says he respects them."),
                                                     ("Er stimmt ihnen völlig zu.", "Ich sehe das anders."),
                                                     ("Er hat ihre Kritik nie gehört.", "He quotes it.")],
    "Ich respektiere sie, aber…", "Attitude (1.B.3): respectful disagreement.",
    ["Ich respektiere sie, aber ich sehe das anders."])
Q.q("1.B.4 Organization", r"Mit welchem Argument verteidigt Lukas die Mischung?",
    "Die Blasmusik hat immer Neues aufgenommen.", [("Techno ist beliebter als Blasmusik.", "He does not argue from popularity."),
                                                  ("Die Traditionalisten können nicht spielen.", "He does not attack them."),
                                                  ("Das junge Publikum verlangt es.", "Not stated.")],
    "hat immer Neues aufgenommen.", "He supports his view with history.",
    ["Märsche, Polkas, später Pop."])
Q.q("1.B.5 Word meaning", r"Was meint Lukas mit „das Gemeinsame“?",
    "dass ein ganzes Dorf zusammen musiziert", [("einen gemeinsamen Bus zum Festival", "Literal misreading."),
                                               ("dieselbe Uniform für alle", "No."),
                                               ("ein gemeinsames Bankkonto", "No.")],
    "Community music-making.", "Word meaning (1.B.5): he explains it in the next sentence.",
    ["…ein Dorf, das zusammen spielt."])

Q.frq(kind="Project Presentation", head=r"Question 1 \textperiodcentered\ Project Presentation (practice prompt) \textperiodcentered\ 11 points \textperiodcentered\ 3 + 3 minutes", mins=6,
      directions=[r"Imagine that your project examined how music reflects the values of a German-speaking community. You have 3 minutes to prepare, using your notes, and 3 minutes to present. Explain at least three factors, with specific examples from your research, and show how cultural perspectives relate to cultural products or practices."],
      prompt=[r"Prompt: \textbf{Wie spiegelt die Musik die Werte einer deutschsprachigen Gemeinschaft wider, die Sie untersucht haben?}",
              r"Practice focus (example): Vienna's music culture."],
      model=[r"Heute spreche ich über die Musikkultur Wiens und darüber, was sie über die Werte der Wienerinnen und Wiener zeigt. Ich habe mich auf drei Aspekte konzentriert: das Neujahrskonzert, die Ballkultur und die Musikerziehung.",
             r"Erstens das Neujahrskonzert der Wiener Philharmoniker. Bei meiner Recherche habe ich herausgefunden, dass es jedes Jahr am 1. Januar in viele Länder übertragen wird. Am Ende klatscht das Publikum beim Radetzky-Marsch im Takt mit. Das zeigt, wie wichtig es den Wienern ist, das neue Jahr gemeinsam mit einer Tradition zu beginnen, und wie stolz sie auf ihre Musikgeschichte sind.",
             r"Zweitens die Ballkultur. Im Winter finden in Wien hunderte Bälle statt, vom Opernball bis zu Bällen von Berufsgruppen. Viele Jugendliche lernen dafür in der Tanzschule Walzer. Diese Praxis spiegelt wider, dass Musik und Tanz in Wien nicht nur Unterhaltung sind, sondern ein gesellschaftliches Ritual, das Generationen verbindet.",
             r"Schließlich die Musikerziehung. Die Wiener Sängerknaben gibt es seit 1498, und in ganz Österreich lernen viele Kinder in Musikschulen ein Instrument. Das zeigt, dass Musik als Teil der Bildung gilt und an die nächste Generation weitergegeben werden soll.",
             r"Zusammenfassend kann man sagen, dass Musik in Wien eine Gemeinschaft schafft, Stolz ausdrückt und Wissen weitergibt. Ich habe gelernt, dass ein Walzer für viele Österreicher mehr ist als ein Tanz: Er ist ein Stück Identität."],
      rows=[("A Task", 2, "three or more factors, each explained with relevant details from research", "three factors named with no detail, or only one or two factors"),
            ("B Culture", 2, "specific examples linking perspectives (tradition, community, education) to products or practices", "examples with no perspective, or a vague one (1 point)"),
            ("C Organization", 2, "clear introduction, ordered factors, conclusion; varied transitions", "a list of facts with no progression"),
            ("D Language", 3, "wide vocabulary, varied structures (passive, relative clauses, dass-clauses)", "a limited set of basic structures"),
            ("E Delivery", 2, "clear pronunciation, natural pace and intonation, little hesitation", "hesitant, monotone or rushed speech")],
      tips=["The introduction names the three factors, so the listener can follow.", "Each factor has a specific example (Radetzky-Marsch, the Opernball, 1498) and a perspective (das zeigt, diese Praxis spiegelt wider).",
            "The conclusion pulls the factors together and adds a reflection.", "About 360 words: three minutes at a natural pace."],
      ask="Prepare for 3 minutes using keywords only, then present aloud for 3 minutes (record yourself if you can). Then mark your presentation.", lines=14)

GUIDE, QSET = G, Q
