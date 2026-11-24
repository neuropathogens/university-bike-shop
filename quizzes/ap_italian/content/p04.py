from ap_wl.model import Doc

STEM = "04-science-technology"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 4: Science and Technology", r"Unit 4 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 4 asks how science and technology change daily life, communication and society, and who benefits. Its recommended contexts are innovations and emerging technologies, personal technology and communication, science in everyday life, and the societal impacts of science and technology. This guide gives the vocabulary of technology and science, Italian inventors and scientists from Galileo to Rita Levi-Montalcini, privacy, cash and digital identity, recycling and energy choices, the future and the condizionale for predictions and reported data, the passive with modal verbs, and an Argumentative Essay kit focused on reading charts. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Chart verbs I can use: \blank[10em]",
        short="Unit 4", sub="Science and Technology")

G.sec("Inventions and discoveries")
G.tex(r"""
\begin{vocab}
l'invenzione / la scoperta & invention / discovery & \emph{inventare} vs. \emph{scoprire} \\
l'intelligenza artificiale (IA) & artificial intelligence & \\
il brevetto & patent & \\
la pila & battery & \\
il ricercatore / la ricercatrice & researcher & \\
la fuga dei cervelli & brain drain & young researchers leaving Italy \\
\end{vocab}

\begin{compare}{Invention or discovery}{Who, when}{Note}
the telescope turned to the sky & Galileo Galilei, 1609--10 & moons of Jupiter; science based on observation \\
the electric battery & Alessandro Volta, 1800 & the volt is named after him \\
wireless telegraphy (radio) & Guglielmo Marconi; Nobel Prize in Physics 1909 & \\
the first nuclear reactor & Enrico Fermi, Chicago, 1942 & Nobel Prize 1938 \\
the Programma 101, an early desktop computer & Olivetti, 1965 & Italian design and electronics \\
nerve growth factor & Rita Levi-Montalcini; Nobel Prize in Medicine 1986 & \\
\end{compare}
""")
G.q("1 Invenzioni", r"Perché l'unità di misura «volt» si chiama così?",
    "in onore di Alessandro Volta, inventore della pila", [("in onore di Galileo Galilei", "Galileo is linked to the telescope."),
                                                           ("perché significa «veloce» in latino", "No."),
                                                           ("in onore di una città italiana", "No.")],
    "Volta → volt.", "Volta built the first electric battery (1800); the unit of voltage bears his name.",
    ["pila → Volta → volt."])
G.q("1 Invenzioni", r"Which Italian received the Nobel Prize in Physics in 1909 for work on wireless telegraphy?",
    "Guglielmo Marconi", [("Enrico Fermi", "Fermi won in 1938."),
                          ("Alessandro Volta", "Volta died long before the Nobel Prize existed."),
                          ("Rita Levi-Montalcini", "She won in Medicine, 1986.")],
    "Marconi → radio, 1909.", "Marconi shared the 1909 Physics Nobel for wireless telegraphy.",
    ["radio → Marconi."])

G.sec("Personal technology, privacy and cash")
G.tex(r"""
\begin{vocab}
il cellulare / il telefonino & cell phone & \\
i social (network) & social media & \\
la privacy / la protezione dei dati & privacy / data protection & \\
il Garante della privacy & Italy's data protection authority & \\
lo SPID & public digital identity & used for online public services \\
i contanti / pagare in contanti & cash / to pay cash & \\
il POS & card terminal & shops must accept cards \\
il divario digitale & digital divide & \\
\end{vocab}

\textbf{Privacy.} In March 2023 Italy's data protection authority temporarily blocked a popular AI chatbot until its company changed how it handled users' data, the first such decision in the West. \textbf{Cash.} Italians still use cash more than many Europeans; since 2022 shops can be fined if they refuse card payments. Both cases show a tension between convenience, control of personal data and the fight against tax evasion.
""")
G.q("2 Privacy", r"Perché nel 2023 il Garante della privacy ha bloccato temporaneamente un chatbot di intelligenza artificiale?",
    "per problemi nel trattamento dei dati degli utenti", [("perché il chatbot parlava solo inglese", "No."),
                                                          ("perché era troppo costoso", "No."),
                                                          ("perché era vietato usare Internet", "No.")],
    "Data protection.", "The authority suspended the service until the company changed how it handled personal data.",
    ["Garante → protezione dei dati."])
G.q("2 Privacy", r"Since 2022, Italian shops can be fined if they refuse card payments. Which goal does this rule most directly serve?",
    "making payments traceable and fighting tax evasion", [("forcing everyone to give up cash", "Cash remains legal."),
                                                           ("raising prices", "No."),
                                                           ("protecting shopkeepers' privacy", "Not the aim.")],
    "Traceability.", "Card payments leave a record; accepting them helps fight undeclared sales.",
    ["POS → tracciabilità."])

G.sec("Science in everyday life and its impact")
G.tex(r"""
\begin{vocab}
la raccolta differenziata & separate waste collection & bins differ from town to town \\
l'umido / la plastica / il vetro & food waste / plastic / glass & \\
il porta a porta & door-to-door collection & \\
le energie rinnovabili & renewable energy & \\
la geotermia & geothermal energy & Larderello, Tuscany: power since the early 1900s \\
il nucleare & nuclear power & rejected in referendums in 1987 and 2011 \\
la bufala & fake news (literally buffalo) & \\
\end{vocab}

\textbf{Questions about impact} ask who benefits and who is left out, what the risks are, and who should decide (\emph{Chi dovrebbe regolare l'IA?}). Good answers weigh both: \emph{È vero che l'IA facilita le diagnosi, ma solleva problemi di privacy.}
""")
G.q("3 Quotidiano", r"Che cos'è una «bufala» nel linguaggio dei media?",
    "una notizia falsa", [("un formaggio tipico", "That is mozzarella di bufala, the literal sense."),
                          ("un animale protetto", "Literal sense."),
                          ("un articolo scientifico", "No.")],
    "bufala = hoax.", "In everyday Italian, una bufala is a fake story or hoax.",
    ["notizia falsa → bufala."])
G.q("3 Quotidiano", r"Which sentence weighs a benefit against a risk, as impact questions reward?",
    "È vero che le app per la salute aiutano a prevenire le malattie, ma raccolgono dati molto personali.",
    [("Le app per la salute sono fantastiche.", "One-sided and vague."),
     ("Molte persone usano le app per la salute.", "A fact with no evaluation."),
     ("Bisognerebbe vietare subito tutte le app.", "One-sided, with no reasoning.")],
    "È vero che X, ma Y.", "Concessive structures let you weigh both sides in one sentence.",
    ["benefit + risk."])

G.sec("Structures: predictions, reported data, the passive with modals")
G.tex(r"""
\begin{compare}{Purpose}{Structure}{Example}
Predict & futuro semplice & Nel 2030 metà delle auto sarà elettrica. \\
Probability & futuro di probabilità & Che ore sono? Saranno le otto. (It's probably eight.) \\
Reported, unconfirmed data & condizionale (journalistic) & Secondo lo studio, un giovane su tre userebbe l'IA ogni giorno. \\
Hypothesize & periodo ipotetico & Se tutti avessero Internet veloce, il divario digitale sparirebbe. \\
Passive with modals & dovere / potere + essere + participle & I rifiuti devono essere separati. \\
Data: change & aumentare, crescere, diminuire, calare, raddoppiare, dimezzarsi & L'uso è raddoppiato tra il 2019 e il 2024. \\
Data: share & la maggioranza, la metà, un terzo, uno su quattro & Uno studente su quattro\ldots \\
\end{compare}

\begin{trap}
In the passive with a modal verb, the participle agrees with the subject: \emph{Le bottiglie devono essere \textbf{lavate}.} Do not confuse the journalistic condizionale (\emph{sarebbero}) with a statement of fact when you report a source: it signals that the information is not confirmed.
\end{trap}
""")
G.q("4 Strutture", r"Scegli la forma corretta: Le pile usate non devono essere \blank\ nei rifiuti normali.",
    "gettate", [("gettato", "The participle agrees with the subject le pile (feminine plural)."),
                ("gettare", "The passive needs the participle."),
                ("gettati", "Pile is feminine.")],
    "Agreement in the passive.", "Dovere + essere + participle; the participle agrees with the subject.",
    ["le pile → gettate."])
G.q("4 Strutture", r"Secondo un grafico, i pagamenti con carta sono passati dal 20~\% al 40~\% in cinque anni. Quale frase lo descrive con precisione?",
    "In cinque anni la quota dei pagamenti con carta è raddoppiata.", [("La quota è aumentata del 20~\\% ogni anno.", "It rose 20 points over five years, not 20% a year."),
                                                                       ("La quota si è dimezzata.", "It rose."),
                                                                       ("La maggioranza paga con la carta.", "40% is not a majority.")],
    "20 → 40 = doubled.", "Precise chart language: è raddoppiata, è aumentata di 20 punti percentuali, è passata dal 20 al 40 per cento.",
    ["40 = 2 × 20 → raddoppiata."])
G.q("4 Strutture", r"In a news report you read: «Secondo fonti non ufficiali, il nuovo telefono costerebbe 900 euro.» What does the condizionale costerebbe signal?",
    "that the price is reported but not confirmed", [("that the phone would cost 900 euros only if bought abroad", "No condition is stated."),
                                                     ("that the phone is free", "No."),
                                                     ("that the price is certain", "The condizionale signals the opposite.")],
    "Condizionale giornalistico = unconfirmed.", "Italian journalism uses the condizionale to report claims it has not verified.",
    ["fonti non ufficiali + costerebbe → unconfirmed."])

G.sec("Task kit: the Argumentative Essay with a chart")
G.tex(r"""
Unit 4 topics are often debates about benefits and risks: \emph{Lo smart working dovrebbe diventare la norma?}, \emph{Le scuole dovrebbero permettere l'IA?} The chart source is easy to misread under time pressure.

\begin{terms}
Read the chart first & title, units (\%, milioni, ore), years, who was surveyed \\
Pick one comparison & the biggest change, a majority, or a surprising gap \\
Say it precisely & \emph{Secondo il grafico della fonte 2, il 62~\% dei\ldots, ma solo il 25~\% dei\ldots} \\
Explain it & \emph{Questo dimostra che\ldots / Questi dati indicano che\ldots} \\
\end{terms}

\begin{trap}
Misreading a chart (switching columns, treating a percentage as a number of people) costs points in source use. Quote the numbers with their labels.
\end{trap}
""")
G.q("5 Saggio", r"A chart shows 62\% of workers under 35 prefer hybrid work and 25\% of workers over 55 do. Which sentence uses the chart correctly?",
    r"Secondo la fonte 2, il 62~\% dei lavoratori sotto i 35 anni preferisce il lavoro ibrido, contro il 25~\% di quelli sopra i 55.", [("Secondo la fonte 2, il 62~\\% dei lavoratori sopra i 55 anni preferisce il lavoro ibrido.", "Switches the groups."),
                                                                                                                                        ("Secondo la fonte 2, 62 giovani preferiscono il lavoro ibrido.", "Turns a percentage into a number of people."),
                                                                                                                                        ("La fonte 2 dice che tutti vogliono lavorare da casa.", "Overstates the data.")],
    "Numbers + labels + source.", "Chart evidence must keep the groups and units straight and name the source.",
    ["62% → under 35; 25% → over 55."])
G.q("5 Saggio", r"Which phrase best explains what a statistic shows?",
    "Questi dati indicano che…", [("C'era una volta…", "A storytelling opener."),
                                  ("A proposito…", "An aside, not an explanation."),
                                  ("Per cominciare la storia…", "Not an explanation.")],
    "Questi dati indicano che…", "Argumentation (Row C) needs the step from evidence to claim.",
    ["Data → claim: questi dati indicano che."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 4: Science and Technology: Question Set", r"Unit 4 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Audio and Chart and an Audio Report for listening, an Article and a Literary Text for reading) on recycling, an early Italian desktop computer, a grandmother and her video calls, and fake news, followed by an Argumentative Essay with three sources and the 10-point scoring guide. As on the exam, questions and choices are in Italian; listening sources are printed as transcripts. All sources and data are original and fictional, written for practice. Allow about 25 minutes for the multiple choice and 55 minutes for the essay.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Essay: \blank\ / 10 \qquad Target: 15+ MCQ and 7+ essay \qquad Pace: 75 s per item",
        short="Unit 4", sub="Science and Technology")

Q.sec("Listening: Audio and Chart")
Q.src(r"Listening 1 \textperiodcentered\ Audio and Chart (transcript) \textperiodcentered\ «Il porta a porta funziona?», Radio Ambiente", [
    r"(GIORNALISTA) Quattro anni fa il comune di Montebello ha tolto i grandi cassonetti dalle strade e ha introdotto la raccolta porta a porta: ogni famiglia lascia fuori casa i sacchi della plastica, della carta e dell'umido in giorni precisi.",
    r"(GIORNALISTA) La percentuale di raccolta differenziata è cresciuta ogni anno, tranne nel 2024, quando è rimasta ferma. Il motivo? Il calendario è cambiato e molti abitanti si sono confusi.",
    r"(ASSESSORA) Il sistema funziona perché ognuno si sente responsabile del proprio sacco. Ma deve essere semplice: quando le regole cambiano troppo spesso, la gente si stanca. Quest'anno abbiamo creato un'app che ricorda il giorno giusto.",
], 5, table=(["Anno", "Raccolta differenziata"], [["2021", "48~\\%"], ["2022", "61~\\%"], ["2023", "72~\\%"], ["2024", "72~\\%"], ["2025", "79~\\%"]]),
      note="Percentuale dei rifiuti raccolti separatamente (dati fittizi).")
Q.q("1.A.2 Data", r"Secondo la tabella, in quale anno la raccolta differenziata ha raggiunto il valore più alto?",
    "nel 2025", [("nel 2023", "72%, lower than 2025."),
                 ("nel 2024", "72%: it stayed level."),
                 ("nel 2021", "48%, the lowest.")],
    "79% in 2025.", "Data (1.A.2): find the maximum.",
    ["79 % is the highest value."])
Q.q("1.C.1 Connect", r"Come spiega il servizio il dato del 2024 nella tabella?",
    "Il cambio del calendario ha confuso molti abitanti.", [("Il comune ha rimesso i cassonetti.", "Not stated."),
                                                           ("La gente ha smesso di comprare plastica.", "No."),
                                                           ("L'app non funzionava.", "The app came later.")],
    "Table: 72 → 72; audio: new calendar.", "Connect (1.C.1): match the flat year with its cause.",
    ["è rimasta ferma … il calendario è cambiato."])
Q.q("1.B.3 Point of view", r"Secondo l'assessora, perché il sistema porta a porta funziona?",
    "perché ognuno si sente responsabile del proprio sacco", [("perché le multe sono altissime", "Not mentioned."),
                                                             ("perché i cassonetti sono più grandi", "They were removed."),
                                                             ("perché la gente ama le regole complicate", "The opposite.")],
    "Responsibility.", "Point of view (1.B.3).",
    ["…ognuno si sente responsabile del proprio sacco."])
Q.q("1.A.1 Detail", r"Che cosa ha creato il comune quest'anno?",
    "un'app che ricorda il giorno giusto per ogni sacco", [("nuovi cassonetti", "No."),
                                                          ("un corso obbligatorio", "No."),
                                                          ("una tassa sulla plastica", "No.")],
    "Un'app.", "Detail (1.A.1).",
    ["abbiamo creato un'app che ricorda il giorno giusto."])
Q.q("1.C.3 Inference", r"Che cosa si può dedurre dalle parole dell'assessora?",
    "Che la semplicità delle regole è importante quanto la buona volontà dei cittadini.", [("Che i cittadini non vogliono riciclare.", "Rates rose."),
                                                                                         ("Che il porta a porta va abolito.", "No."),
                                                                                         ("Che le app sono inutili.", "She created one.")],
    "Simplicity matters.", "Inference (1.C.3).",
    ["deve essere semplice … la gente si stanca."])

Q.sec("Reading: Article")
Q.src(r"Reading 1 \textperiodcentered\ Article \textperiodcentered\ «La Perottina: il computer sulla scrivania»", [
    r"Nel 1965 l'Olivetti, l'azienda di macchine per scrivere di Ivrea, presentò a New York una macchina che sorprese il pubblico: la Programma 101. Era abbastanza piccola da stare su una scrivania e poteva essere programmata con schede magnetiche. Molti la considerano uno dei primi personal computer della storia.",
    r"Il gruppo di ingegneri era guidato da Pier Giorgio Perotto, e per questo la macchina fu soprannominata «Perottina». Il suo aspetto elegante, disegnato da Mario Bellini, era pensato perché chiunque potesse usarla, non solo gli specialisti.",
    r"«Olivetti dimostrò che la tecnologia poteva essere anche bella e umana», spiega la curatrice di un museo del design, Paola Sarti. «Ma l'Italia non riuscì a trasformare quel successo in un'industria informatica: un'occasione persa.»",
], 5)
Q.q("1.B.1 Main idea", r"Di che cosa parla principalmente l'articolo?",
    "della nascita e del significato della Programma 101 dell'Olivetti", [("della storia delle macchine per scrivere", "Only background."),
                                                                          ("della vita di Mario Bellini", "One detail."),
                                                                          ("dei computer moderni", "No.")],
    "Programma 101.", "Main idea (1.B.1).",
    ["presentation → team and design → legacy."])
Q.q("1.A.1 Detail", r"Perché la macchina fu soprannominata «Perottina»?",
    "dal nome dell'ingegnere che guidava il progetto", [("perché era piccola come una pera", "Wordplay misreading."),
                                                       ("dal nome di una città", "No."),
                                                       ("perché costava poco", "Not stated.")],
    "Perotto → Perottina.", "Detail (1.A.1).",
    ["…guidato da Pier Giorgio Perotto, e per questo…"])
Q.q("1.C.3 Inference", r"Che cosa voleva ottenere il design di Mario Bellini?",
    "che la macchina fosse facile da usare per tutti", [("che la macchina fosse molto pesante", "The opposite."),
                                                       ("che solo gli ingegneri la capissero", "The opposite."),
                                                       ("che sembrasse una macchina per scrivere", "Not stated.")],
    "Usability.", "Inference (1.C.3): perché chiunque potesse usarla.",
    ["…perché chiunque potesse usarla."])
Q.q("1.B.3 Point of view", r"Che cosa pensa Paola Sarti del dopo Programma 101?",
    "che l'Italia abbia perso l'occasione di creare una grande industria informatica", [("che l'Italia sia diventata leader mondiale dei computer", "She calls it a missed chance."),
                                                                                        ("che la macchina fosse brutta", "She praises its beauty."),
                                                                                        ("che la tecnologia debba essere solo utile", "She praises beauty too.")],
    "un'occasione persa.", "Point of view (1.B.3).",
    ["l'Italia non riuscì … un'occasione persa."])
Q.q("1.B.5 Word meaning", r"Nell'articolo, «soprannominata» significa",
    "chiamata con un nome scherzoso o affettuoso", [("venduta a un prezzo alto", "No."),
                                                   ("premiata", "No."),
                                                   ("vietata", "No.")],
    "soprannome = nickname.", "Word meaning (1.B.5).",
    ["soprannominata «Perottina» → nickname."])

Q.sec("Reading: Literary Text")
Q.src(r"Reading 2 \textperiodcentered\ Literary Text \textperiodcentered\ «Nonna Rosa e lo schermo» (racconto)", [
    r"Quando mio fratello partì per l'Australia, nonna Rosa disse che ormai l'avrebbe rivisto solo in paradiso. Per lei l'Australia era più lontana della luna: la luna almeno si vedeva dal balcone.",
    r"Fu mia cugina a installarle le videochiamate sul tablet. La prima volta, nonna Rosa si mise il rossetto e la collana delle feste. Quando il viso di Marco apparve sullo schermo, lei lo toccò con un dito, come per controllare che fosse vero, e poi gli chiese subito se mangiava abbastanza.",
    r"Da allora la chiamata della domenica è sacra quanto la messa. Nonna Rosa tiene il tablet troppo vicino, così Marco vede soprattutto il suo naso. Ma nessuno ha il coraggio di dirglielo.",
], 5)
Q.q("1.A.1 Detail", r"Che cosa pensava nonna Rosa quando Marco partì?",
    "che non l'avrebbe più rivisto in vita", [("che sarebbe tornato presto", "She said only in paradise."),
                                             ("che l'Australia fosse vicina", "The opposite."),
                                             ("che lo avrebbe raggiunto", "No.")],
    "solo in paradiso.", "Detail (1.A.1).",
    ["l'avrebbe rivisto solo in paradiso."])
Q.q("1.C.3 Inference", r"Perché nonna Rosa si mise il rossetto e la collana delle feste?",
    "perché considerava la prima videochiamata un'occasione speciale", [("perché doveva andare a messa", "Not stated."),
                                                                         ("perché aveva una festa", "No."),
                                                                         ("perché il tablet lo richiedeva", "No.")],
    "A special occasion.", "Inference (1.C.3).",
    ["rossetto + collana delle feste → occasione speciale."])
Q.q("1.B.3 Tone", r"Quale tono prevale nel racconto?",
    "affettuoso e umoristico", [("tragico", "The ending is comic and tender."),
                               ("polemico", "No."),
                               ("tecnico", "It is a personal story.")],
    "Tender humor.", "Tone (1.B.3): the nose on screen, the question about food.",
    ["…vede soprattutto il suo naso → comic; tenerezza."])
Q.q("1.B.5 Word meaning", r"Nel testo, «sacra quanto la messa» significa che la chiamata della domenica",
    "è un appuntamento importantissimo che non si salta mai", [("si fa in chiesa", "Figurative."),
                                                              ("è molto noiosa", "No."),
                                                              ("è vietata", "No.")],
    "Comparison of importance.", "Word meaning (1.B.5): figurative.",
    ["sacra → inviolabile."])
Q.q("1.C.2 Conclusion", r"Che cosa suggerisce il racconto sul rapporto tra la nonna e la tecnologia?",
    "che la tecnologia ha accorciato una distanza che sembrava insuperabile", [("che la nonna odia il tablet", "The call is now sacred."),
                                                                              ("che Marco non chiama mai", "He calls every Sunday."),
                                                                              ("che la tecnologia ha diviso la famiglia", "The opposite.")],
    "Distance bridged.", "Conclusions (1.C.2): from luna and paradiso to a weekly call.",
    ["più lontana della luna → chiamata della domenica."])

Q.sec("Listening: Audio Report")
Q.src(r"Listening 2 \textperiodcentered\ Audio Report (transcript) \textperiodcentered\ «Le bufale corrono veloci»", [
    r"(GIORNALISTA) Una foto di squali nelle strade allagate, una cura miracolosa, un falso annuncio del governo: le notizie false, le cosiddette bufale, girano sui telefoni più velocemente delle smentite.",
    r"(GIORNALISTA) In un liceo di Bari, un professore di storia ha creato un corso di «caccia alla bufala». Gli studenti ricevono ogni settimana una notizia virale e devono verificarla: cercano la fonte originale, controllano la data e l'autore della foto.",
    r"(PROFESSORE) Non insegno a diffidare di tutto, ma a verificare. Chi pensa che tutto sia falso è manipolabile quanto chi crede a tutto.",
    r"(GIORNALISTA) Il risultato? Alla fine dell'anno, gli studenti riconoscono quattro bufale su cinque, contro una su due all'inizio.",
], 5)
Q.q("1.B.5 Word meaning", r"Nel servizio, «le smentite» sono",
    "le dichiarazioni che dimostrano che una notizia è falsa", [("le notizie false stesse", "The opposite."),
                                                               ("i messaggi pubblicitari", "No."),
                                                               ("le foto di animali", "No.")],
    "smentita = denial, correction.", "Word meaning (1.B.5): bufale vs. smentite.",
    ["girano più velocemente delle smentite → corrections."])
Q.q("1.A.1 Detail", r"Che cosa devono fare gli studenti ogni settimana?",
    "verificare una notizia virale cercando la fonte, la data e l'autore", [("scrivere una notizia falsa", "No."),
                                                                           ("cancellare i social", "No."),
                                                                           ("studiare la storia di Bari", "No.")],
    "Verify.", "Detail (1.A.1).",
    ["…devono verificarla: cercano la fonte originale…"])
Q.q("1.B.3 Point of view", r"Che cosa vuole insegnare il professore?",
    "a verificare le notizie, non a diffidare di tutto", [("a non credere mai a nessuna notizia", "He says that makes people manipulable too."),
                                                          ("a non usare il telefono", "Not stated."),
                                                          ("a scrivere articoli", "No.")],
    "Non diffidare, verificare.", "Point of view (1.B.3).",
    ["Non insegno a diffidare di tutto, ma a verificare."])
Q.q("1.C.3 Inference", r"Perché, secondo il professore, chi pensa che tutto sia falso è «manipolabile»?",
    "perché non sa più distinguere le informazioni vere da quelle false", [("perché legge troppi libri", "No."),
                                                                           ("perché crede solo ai giornali", "No."),
                                                                           ("perché non usa Internet", "Not implied.")],
    "Can't tell true from false.", "Inference (1.C.3).",
    ["tutto falso = tutto vero → nessuna distinzione."])
Q.q("1.A.1 Detail", r"Quale risultato ha ottenuto il corso?",
    "Gli studenti riconoscono quattro bufale su cinque invece di una su due.", [("Gli studenti riconoscono tutte le bufale.", "Four in five."),
                                                                                ("Gli studenti hanno smesso di usare il telefono.", "Not stated."),
                                                                                ("Il corso è stato chiuso.", "No.")],
    "1/2 → 4/5.", "Detail (1.A.1).",
    ["quattro bufale su cinque, contro una su due."])

Q.frq(kind="Argumentative Essay", head=r"Question 3 \textperiodcentered\ Argumentative Essay \textperiodcentered\ 10 points \textperiodcentered\ 55 minutes", mins=55,
      directions=[r"Scrivi un saggio argomentativo per un corso universitario. Leggi il tema e le fonti scritte; poi ascolta la fonte audio (qui come trascrizione). Scrivi un saggio che usi informazioni tratte da tutte e tre le fonti per sostenere la tua posizione. Cita le fonti con il numero, il titolo o l'autore."],
      sources=[dict(title=r"Fonte 1 \textperiodcentered\ Articolo \textperiodcentered\ «Da Milano al mare, con il computer»", paras=[
          r"Davide, ingegnere informatico di 34 anni, lavora per un'azienda di Milano, ma da due anni vive di nuovo nel suo paese in Sicilia. «Pago la metà d'affitto, vedo i miei genitori e la sera vado al mare», racconta. «E lavoro meglio: niente due ore di treno al giorno.»",
          r"Il fenomeno ha anche un nome, «south working». Non tutti però ne vedono solo i vantaggi. «Il martedì ci vediamo in videochiamata, ma le idee migliori nascevano alla macchinetta del caffè», ammette la sua responsabile, Francesca Ricci."]),
               dict(title=r"Fonte 2 \textperiodcentered\ Grafico \textperiodcentered\ Dove preferiscono lavorare gli impiegati?", paras=[
          r"Sondaggio su lavoratori d'ufficio in Italia, per età (dati fittizi). Percentuale che preferisce ciascuna modalità."],
                    table=(["Età", "Sempre da casa", "Ibrido", "Sempre in ufficio"], [["Sotto i 35 anni", "21~\\%", "62~\\%", "17~\\%"], ["35--54 anni", "18~\\%", "54~\\%", "28~\\%"], ["55 anni e oltre", "12~\\%", "25~\\%", "63~\\%"]])),
               dict(title=r"Fonte 3 \textperiodcentered\ Audio (trascrizione) \textperiodcentered\ «La città si svuota?», Radio Economia", paras=[
          r"(GIORNALISTA) Parliamo con l'urbanista Giorgio Lanza. Professore, che cosa succede alle città se tutti lavorano da casa?",
          r"(GIORGIO LANZA) I quartieri degli uffici si svuotano: bar, ristoranti e negozi perdono clienti. E c'è un costo umano: molti giovani assunti durante la pandemia non hanno mai conosciuto di persona i loro colleghi, e imparano meno.",
          r"(GIORNALISTA) Dunque è contrario?",
          r"(GIORGIO LANZA) Assolutamente no. Il lavoro da remoto può ridurre il traffico e riportare vita nei piccoli paesi. Ma servono alcuni giorni in presenza: la fiducia e la creatività nascono anche dagli incontri."])],
      prompt=[r"Tema del saggio: \textbf{Lo smart working dovrebbe diventare la norma per chi può lavorare da casa?}"],
      model=[r"Dopo la pandemia, milioni di italiani hanno scoperto che molte attività d'ufficio si possono svolgere da casa. Ci si chiede ora se lo smart working debba diventare la norma. A mio parere, la soluzione migliore non è il lavoro sempre da casa, ma un modello ibrido.",
             r"Innanzitutto, il lavoro da remoto migliora la qualità della vita e può far rinascere i piccoli paesi. Nella fonte 1, Davide racconta che, tornato in Sicilia, paga la metà d'affitto, vede i suoi genitori e risparmia due ore di treno al giorno. Anche l'urbanista Giorgio Lanza, nella fonte 3, riconosce che il lavoro da remoto può ridurre il traffico e riportare vita nei paesi.",
             r"Tuttavia, lavorare sempre da casa ha costi reali. Secondo Lanza, i quartieri degli uffici si svuotano e molti giovani assunti a distanza imparano meno, perché non hanno mai conosciuto di persona i colleghi. La responsabile di Davide, Francesca Ricci, ammette nella fonte 1 che le idee migliori nascevano «alla macchinetta del caffè».",
             r"Inoltre, sono gli stessi lavoratori a preferire una via di mezzo. Secondo il grafico della fonte 2, il 62~\% degli impiegati sotto i 35 anni sceglierebbe il lavoro ibrido, mentre solo il 21~\% vorrebbe lavorare sempre da casa. Questi dati indicano che i giovani apprezzano la flessibilità, ma non vogliono rinunciare all'ufficio.",
             r"In conclusione, lo smart working non dovrebbe diventare la norma assoluta, ma una parte stabile di un modello ibrido. Se le aziende alternassero giorni a casa e in ufficio, i lavoratori avrebbero più tempo per sé senza perdere la fiducia e la creatività che, come dice Lanza, nascono dagli incontri."],
      rows=[("A Position", 1, "a clear, qualified position (hybrid, not fully remote)", "only lists advantages and disadvantages"),
            ("B Source use", 2, "all three sources used accurately and named; age groups and columns kept straight", "two sources, or mixing up the chart's columns"),
            ("C Argumentation", 2, "each claim explained with evidence (questi dati indicano che)", "quotes and numbers with no link to the claims"),
            ("D Organization", 2, "introduction, claims, counterpoint, conclusion; varied transitions", "one paragraph per source"),
            ("E Language control", 3, "varied structures: si passivante, condizionale, periodo ipotetico, relative clauses", "basic structures; copying the sources")],
      tips=["The position is qualified but clear: hybrid as the norm.", "The chart is quoted with the right row (under 35) and columns (ibrido vs. sempre da casa).",
            "Lanza's view is used on both sides of the argument, accurately.", "The conclusion's periodo ipotetico (se … alternassero, avrebbero) rounds off the argument."],
      ask="Write your essay in Italian (about 300–350 words), then mark it against each row.", lines=22)

GUIDE, QSET = G, Q
