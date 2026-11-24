from ap_wl.model import Doc

STEM = "05-contemporary-life"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 5: Contemporary Life", r"Unit 5 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 5 asks how traditions shape daily life today: school and work, food and health, leisure, sports and travel. Its recommended contexts are education and career, entertainment and media, food and health, pop culture, sports and leisure, and travel and tourism. This guide gives the vocabulary of daily life, the practices most often tested (the liceo, oral tests and the maturità, breakfast at the bar, the aperitivo and the Mediterranean diet, the national health service, August holidays and the Giro d'Italia), relative clauses with cui, the imperative with pronouns, and a second Project Presentation kit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Practices I can link to a perspective: \blank[8em]",
        short="Unit 5", sub="Contemporary Life")

G.sec("School and work")
G.tex(r"""
\begin{vocab}
la scuola primaria / le medie & primary school (5 years) / middle school (3 years) & \\
il liceo / l'istituto tecnico / il professionale & academic / technical / vocational high school & 5 years \\
il liceo classico & high school with Latin and ancient Greek & \\
l'interrogazione & oral test in front of the class & \\
la maturità (l'esame di Stato) & final high-school exam & written and oral parts \\
i voti da 1 a 10 & grades from 1 to 10 & 6 is a pass \\
la laurea triennale / magistrale & bachelor's (3 years) / master's (2 years) & \\
il precariato & job insecurity & \\
\end{vocab}

\textbf{Practices and perspectives.} Italian students are often tested orally: the teacher calls a student to the front for an \emph{interrogazione}, and the maturità ends with an oral exam. The practice reflects a perspective that being able to explain and connect ideas aloud is as important as writing them. The \emph{liceo classico}, with Latin and Greek, reflects the value placed on a broad humanistic culture.
""")
G.q("1 Scuola", r"Che cos'è un'interrogazione nella scuola italiana?",
    "una verifica orale in cui lo studente risponde alle domande del professore", [("un test scritto a scelta multipla", "It is oral."),
                                                                                    ("una gita scolastica", "No."),
                                                                                    ("una lezione di educazione fisica", "No.")],
    "interrogazione = oral test.", "A very common practice: students answer questions aloud, often in front of the class.",
    ["interrogare = to question orally."])
G.q("1 Scuola", r"In Italy the final high-school exam ends with an oral exam in which students connect topics from different subjects. Which perspective does this reflect?",
    "Explaining and connecting ideas aloud is a key sign of education.", [("Only written work proves knowledge.", "The oral exam shows the opposite."),
                                                                         ("Subjects should be studied separately.", "The exam asks students to connect them."),
                                                                         ("Exams should be as short as possible.", "Not implied.")],
    "Oral exam ↔ value of spoken reasoning.", "Practice (oral maturità) linked to a perspective (education as the ability to reason and speak).",
    ["orale + collegamenti → cultura generale."])

G.sec("Food and health")
G.tex(r"""
\begin{vocab}
la colazione al bar & breakfast at a café & cappuccino and cornetto, often standing at the counter \\
il pranzo / la cena & lunch / dinner & dinner around 8 p.m. or later \\
l'aperitivo & pre-dinner drink with snacks & \\
la dieta mediterranea & Mediterranean diet & UNESCO intangible heritage (2010) \\
Slow Food & movement for local, traditional food & founded in Bra, Piedmont, in 1986 \\
DOP & protected designation of origin & Parmigiano Reggiano, Prosciutto di Parma \\
il Servizio Sanitario Nazionale (SSN) & national health service & universal since 1978 \\
\end{vocab}

\textbf{Coffee.} Many Italians drink cappuccino only in the morning and an espresso after meals; at the bar, a coffee at the counter costs less than at a table. In Naples, the tradition of the \emph{caffè sospeso} (paying for an extra coffee for a stranger who cannot afford one) reflects a perspective of everyday generosity.
""")
G.q("2 Cibo", r"Che cos'è il «caffè sospeso» napoletano?",
    "un caffè pagato in anticipo per una persona sconosciuta che non può permetterselo", [("un caffè servito freddo", "No."),
                                                                                          ("un caffè che si beve in piedi", "That is just a coffee at the counter."),
                                                                                          ("un caffè vietato dopo pranzo", "No.")],
    "Pay it forward.", "The caffè sospeso is a gesture of anonymous solidarity.",
    ["sospeso → pagato per qualcun altro."])
G.q("2 Cibo", r"Which perspective does the Slow Food movement, founded in Bra in 1986, most directly express?",
    "Food should be local, traditional and enjoyed with time.", [("Meals should be as fast as possible.", "The opposite of its name."),
                                                                ("Only imported food is good.", "It promotes local food."),
                                                                ("Cooking at home is outdated.", "No.")],
    "Slow Food ↔ local, slow, traditional.", "A movement (product) born in reaction to fast food, linked to a perspective on food and time.",
    ["Slow vs. fast food."])
G.q("2 Salute", r"Da quando esiste in Italia il Servizio Sanitario Nazionale universale?",
    "dal 1978", [("dal 1861", "That is unification."),
                 ("dal 2010", "That is the Mediterranean diet on the UNESCO list."),
                 ("dal 1946", "That is the Republic.")],
    "SSN 1978.", "The 1978 reform created a universal national health service.",
    ["SSN → 1978."])

G.sec("Leisure, sports and travel")
G.tex(r"""
\begin{vocab}
le ferie / le vacanze & paid leave / holidays & many take them in August \\
chiuso per ferie & closed for the holidays & a common sign in August \\
lo stabilimento balneare & private beach club & umbrellas and sunbeds \\
il tifo / il tifoso & fandom / fan & \\
il Giro d'Italia & cycling race, since 1909 & the leader wears the pink jersey (maglia rosa) \\
la gita fuori porta & day trip out of town & \\
\end{vocab}

\textbf{August.} Around Ferragosto many cities slow down: small shops close, families go to the sea or the mountains, and the same beach club is chosen year after year. The perspective: summer holidays are a shared, almost collective right, and time with family comes before business.
""")
G.q("3 Tempo libero", r"Che cosa indossa il ciclista in testa alla classifica del Giro d'Italia?",
    "la maglia rosa", [("la maglia gialla", "That is the Tour de France."),
                       ("la maglia azzurra", "Azzurro is the color of Italy's national teams."),
                       ("la maglia nera", "No.")],
    "Giro → rosa.", "The pink jersey matches the pink pages of the sports newspaper that founded the race.",
    ["Giro d'Italia → maglia rosa."])
G.q("3 Tempo libero", r"Many small shops in Italian cities hang the sign «chiuso per ferie» in August. Which perspective does this most directly reflect?",
    "A shared summer break with family comes before business.", [("Shops should stay open every day of the year.", "The opposite."),
                                                                ("Tourists are not welcome.", "Not the point."),
                                                                ("Summer is the busiest time for work.", "The opposite.")],
    "August closures ↔ collective holiday.", "A practice (closing in August) linked to a perspective (rest and family time as a shared right).",
    ["chiuso per ferie → vacanze collettive."])

G.sec("Structures: relative clauses with cui, the imperative")
G.tex(r"""
\begin{compare}{Structure}{Use}{Example}
preposition + cui & relative after a preposition & La squadra per cui tifo ha vinto. \\
il cui / la cui & whose & Lo chef, il cui ristorante è famoso, \ldots \\
Imperative (tu / voi / Lei) & instructions, advice & Mangia più frutta! Mangiate\ldots! Mangi\ldots! \\
Negative tu-imperative & non + infinitive & Non mangiare troppi dolci! \\
Imperative + pronouns & attached to tu/voi forms; before the Lei form & Dimmi! Fallo! / Me lo dica! \\
ci vuole / ci vogliono & it takes (time, things) & Ci vogliono due ore per arrivare. \\
\end{compare}

\begin{trap}
The negative tu-imperative is \emph{non} + infinitive: \emph{Non parlare!}, not \emph{Non parla!} (which is a statement: he does not speak). With \emph{ci vuole / ci vogliono}, the verb agrees with what is needed: \emph{ci vuole un'ora}, \emph{ci vogliono due ore}.
\end{trap}
""")
G.q("4 Strutture", r"Scegli la forma corretta: Questa è la squadra per \blank\ tifo da quando ero bambino.",
    "cui", [("che", "After a preposition, use cui."),
            ("quale", "Quale needs the article: per la quale."),
            ("dove", "Dove refers to places.")],
    "per cui.", "Preposition + cui: la squadra per cui tifo.",
    ["per + relative → cui."])
G.q("4 Strutture", r"Quale imperativo è corretto per dire a un amico (tu) di non mangiare troppi dolci?",
    "Non mangiare troppi dolci!", [("Non mangia troppi dolci!", "That is a statement (he doesn't eat), not a negative tu-imperative."),
                                  ("Non mangiate troppi dolci!", "That is the voi form, for several people."),
                                  ("Non mangi troppi dolci!", "That is the formal Lei form.")],
    "non + infinitive.", "The negative tu-imperative uses non + infinitive.",
    ["tu, negative → non mangiare."])

G.sec("Task kit: developing a factor in the presentation")
G.tex(r"""
Each factor in the Project Presentation should follow the same four steps, about 40 seconds in all:

\begin{terms}
1 Claim & \emph{Il secondo fattore è il boom economico.} \\
2 Evidence & one specific fact or example from your research: a place, a date, a name, a practice \\
3 Perspective & \emph{Questo riflette\ldots / il che dimostra quanto fosse importante\ldots} \\
4 Link & connect to the prompt or the next factor: \emph{Per questo\ldots / Inoltre\ldots} \\
\end{terms}

\begin{keyidea}[Change over time]
Prompts often ask how a tradition has changed. Use time markers (\emph{negli anni Cinquanta, dopo la guerra, oggi}) and contrast the imperfetto with the present: \emph{Allora le famiglie ascoltavano il festival alla radio; oggi lo commentano sui social.}
\end{keyidea}
""")
G.q("5 Presentazione", r"Which sequence develops a factor most completely?",
    "claim, specific example from research, perspective it reflects, link to the next idea", [("claim, then the next factor", "No detail or perspective."),
                                                                                              ("example, then a personal opinion", "No claim or perspective."),
                                                                                              ("a definition of the genre only", "No claim, example or perspective.")],
    "Claim → evidence → perspective → link.", "Full task and culture credit come from detailed factors that reach a perspective.",
    ["All four steps → full development."])
G.q("5 Presentazione", r"Scegli la forma corretta: Negli anni Cinquanta molte famiglie \blank\ il festival alla radio.",
    "ascoltavano", [("hanno ascoltato", "A repeated habit in the past takes the imperfetto."),
                    ("ascoltano", "Negli anni Cinquanta places the sentence in the past."),
                    ("ascoltava", "Molte famiglie is plural.")],
    "Past habit → imperfetto.", "The imperfetto describes habits and repeated actions in the past.",
    ["negli anni Cinquanta + habit → ascoltavano."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 5: Contemporary Life: Question Set", r"Unit 5 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Audio Report and a Presentation for listening, an Article and Chart and a Promotional Material for reading) on August closures, choices after the maturità, a farm stay and Italian café culture, followed by a second practice Project Presentation on music, with the 11-point scoring guide and a model script. The presentation prompt is a practice prompt, not the official 2027 project prompt. As on the exam, questions and choices are in Italian; listening sources are printed as transcripts. All sources and data are original and fictional. Allow about 25 minutes for the multiple choice and 6 minutes for the presentation.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Presentation: \blank\ / 11 \qquad Target: 15+ MCQ and 8+ presentation",
        short="Unit 5", sub="Contemporary Life")

Q.sec("Listening: Audio Report")
Q.src(r"Listening 1 \textperiodcentered\ Audio Report (transcript) \textperiodcentered\ «Chiuso per ferie?», Radio Città", [
    r"(GIORNALISTA) In agosto, nel centro di Valmonte, quasi un negozio su due abbassa la saracinesca. Ma quest'anno l'associazione dei commercianti propone di organizzare dei turni, perché la città sia sempre servita.",
    r"(COMMERCIANTE) I turisti arrivano proprio in agosto e trovano tutto chiuso. Se ci organizzassimo a turni, nessuno perderebbe i clienti e tutti potrebbero comunque fare le ferie.",
    r"(GIORNALISTA) Non tutti sono d'accordo.",
    r"(PANETTIERA) Io chiudo da trent'anni nelle due settimane di Ferragosto. È l'unico momento in cui la mia famiglia è tutta insieme: i miei figli lavorano con me tutto l'anno. Per me le ferie in agosto non sono un capriccio, sono un diritto.",
], 5)
Q.q("1.A.1 Detail", r"Che cosa propone l'associazione dei commercianti?",
    "di organizzare dei turni per non chiudere tutti insieme", [("di vietare le ferie in agosto", "Everyone could still take holidays."),
                                                               ("di aprire nuovi negozi", "No."),
                                                               ("di chiudere tutto l'anno la domenica", "No.")],
    "Turni.", "Detail (1.A.1).",
    ["…propone di organizzare dei turni…"])
Q.q("1.B.3 Point of view", r"Qual è l'argomento principale del commerciante?",
    "Con i turni i negozi non perderebbero i clienti e tutti farebbero comunque le ferie.", [("I turisti non spendono abbastanza.", "Not his argument."),
                                                                                             ("Le ferie sono inutili.", "He wants everyone to have them."),
                                                                                             ("Agosto è il mese meno importante.", "The opposite.")],
    "Win-win.", "Point of view (1.B.3).",
    ["Se ci organizzassimo a turni, nessuno perderebbe…"])
Q.q("1.B.3 Point of view", r"Perché la panettiera vuole chiudere a Ferragosto?",
    "perché è l'unico periodo in cui tutta la famiglia è insieme", [("perché in agosto non vende niente", "Not her reason."),
                                                                    ("perché fa troppo caldo per fare il pane", "Not stated."),
                                                                    ("perché la legge lo impone", "No.")],
    "Family time.", "Point of view (1.B.3): her reason concerns family.",
    ["È l'unico momento in cui la mia famiglia è tutta insieme."])
Q.q("1.B.5 Word meaning", r"Nel servizio, «abbassa la saracinesca» significa",
    "chiude il negozio", [("abbassa i prezzi", "No."),
                          ("cambia proprietario", "No."),
                          ("apre un nuovo reparto", "No.")],
    "saracinesca = roller shutter.", "Word meaning (1.B.5): lowering the shutter = closing.",
    ["saracinesca giù → chiuso."])
Q.q("1.C.3 Inference", r"Che cosa rivela la frase «non sono un capriccio, sono un diritto»?",
    "che per la panettiera le ferie hanno un valore sociale e familiare", [("che vuole aumentare i prezzi", "No."),
                                                                           ("che non ama il suo lavoro", "Not implied."),
                                                                           ("che i turisti hanno sempre ragione", "No.")],
    "Holidays as a right.", "Inference (1.C.3).",
    ["capriccio vs. diritto → valore."])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 1 \textperiodcentered\ Article and Chart \textperiodcentered\ «Dopo la maturità», rivista Futuro", [
    r"Per decenni la strada sembrava segnata: dopo il liceo, l'università. Oggi le scelte si moltiplicano. Cresce il numero di diplomati che si iscrive agli ITS, istituti tecnici superiori, con percorsi di solito biennali, che preparano a professioni molto richieste, dalla meccatronica al turismo digitale.",
    r"«Faccio stage in azienda fin dal primo anno e a vent'anni avrò già un mestiere», racconta Giulia, studentessa di un ITS a Bergamo. Per l'orientatrice Anna Ferri non è una sorpresa: «Le aziende cercano tecnici qualificati e spesso non li trovano.»",
    r"Ferri ammette però che i pregiudizi resistono: «Molte famiglie considerano ancora l'università l'unica scelta prestigiosa.»",
], 5, table=(["Scelta dopo il diploma", "2015", "2025"], [["Università", "51~\\%", "48~\\%"], ["ITS e formazione tecnica", "4~\\%", "11~\\%"], ["Lavoro", "27~\\%", "26~\\%"], ["Altro", "18~\\%", "15~\\%"]]),
      note="Percentuale dei diplomati (dati fittizi).")
Q.q("1.A.2 Data", r"Secondo la tabella, quale scelta è quasi triplicata tra il 2015 e il 2025?",
    "ITS e formazione tecnica", [("Università", "It fell from 51% to 48%."),
                                 ("Lavoro", "Almost unchanged."),
                                 ("Altro", "It fell.")],
    "4 → 11.", "Data (1.A.2): 4 × 3 = 12 ≈ 11.",
    ["ITS: 4 % → 11 %."])
Q.q("1.C.1 Connect", r"Quale dato della tabella corrisponde all'affermazione «Cresce il numero di diplomati che si iscrive agli ITS»?",
    "il passaggio dal 4~\\% all'11~\\%", [("il 48~\\% dell'università nel 2025", "That is the university."),
                                          ("il 27~\\% del lavoro nel 2015", "Not about ITS."),
                                          ("il passaggio dal 18~\\% al 15~\\%", "That is Altro.")],
    "ITS row.", "Connect (1.C.1).",
    ["Cresce … ITS ↔ 4 % → 11 %."])
Q.q("1.B.3 Point of view", r"Secondo Anna Ferri, perché gli ITS attirano più studenti?",
    "perché le aziende cercano tecnici qualificati", [("perché sono gratuiti per tutti", "Not stated."),
                                                     ("perché l'università è stata chiusa", "No."),
                                                     ("perché durano cinque anni", "They usually last two years.")],
    "Demand for technicians.", "Point of view (1.B.3).",
    ["Le aziende cercano tecnici qualificati e spesso non li trovano."])
Q.q("1.B.5 Word meaning", r"Nell'articolo, «la strada sembrava segnata» significa che",
    "il percorso dopo la scuola sembrava già deciso", [("le strade erano piene di segnali", "Literal misreading."),
                                                      ("gli studenti si perdevano", "No."),
                                                      ("le scuole erano lontane", "No.")],
    "Figurative: a set path.", "Word meaning (1.B.5).",
    ["dopo il liceo, l'università → percorso deciso."])
Q.q("1.C.2 Conclusion", r"Che cosa si può concludere dall'ultimo paragrafo?",
    "Le aspettative delle famiglie influenzano ancora le scelte dei giovani.", [("Le famiglie non hanno più opinioni.", "Prejudices remain."),
                                                                                ("Gli ITS sono più prestigiosi dell'università.", "Not claimed."),
                                                                                ("Tutti i diplomati scelgono gli ITS.", "Only 11%.")],
    "Pregiudizi resistono.", "Conclusions (1.C.2).",
    ["Molte famiglie considerano ancora l'università l'unica scelta prestigiosa."])

Q.sec("Reading: Promotional Material")
Q.src(r"Reading 2 \textperiodcentered\ Promotional Material \textperiodcentered\ Annuncio di un agriturismo", [
    r"\textbf{AGRITURISMO IL NOCE \textperiodcentered\ Colline del Montefeltro}",
    r"Stanchi del traffico? Venite a vivere la campagna come una volta! Camere in un casale del Settecento, piscina tra gli ulivi e una cucina che usa solo prodotti della nostra azienda agricola.",
    r"\textbf{Ogni sabato:} corso di pasta fresca con nonna Ida (tagliatelle, cappelletti e i suoi segreti). Prenotazione obbligatoria entro il giovedì.",
    r"\textbf{Prezzi:} camera doppia con colazione 95 euro a notte; mezza pensione +30 euro a persona. Bambini sotto i 6 anni gratis. Soggiorno minimo: due notti.",
    r"Gli animali domestici sono i benvenuti, ma non in piscina!",
], 5)
Q.q("1.B.2 Audience", r"A chi si rivolge principalmente l'annuncio?",
    "a persone di città che cercano una vacanza tranquilla in campagna", [("a contadini che cercano lavoro", "No."),
                                                                         ("a studenti che cercano una stanza in affitto", "No."),
                                                                         ("a cuochi professionisti", "The course is with a grandmother.")],
    "Stanchi del traffico?", "Audience (1.B.2).",
    ["Stanchi del traffico? → city dwellers."])
Q.q("1.A.1 Detail", r"Che cosa bisogna fare per partecipare al corso di pasta fresca?",
    "prenotare entro il giovedì", [("pagare 95 euro", "That is the room."),
                                   ("portare la propria farina", "Not stated."),
                                   ("essere maggiorenni", "Not stated.")],
    "Prenotazione entro il giovedì.", "Detail (1.A.1).",
    ["Prenotazione obbligatoria entro il giovedì."])
Q.q("1.C.2 Conclusion", r"Una coppia vuole restare una sola notte in camera doppia. Che cosa succede?",
    "Non è possibile, perché il soggiorno minimo è di due notti.", [("Paga 95 euro.", "One night is below the minimum stay."),
                                                                   ("Paga 125 euro.", "Same problem."),
                                                                   ("Dorme gratis.", "No.")],
    "Minimum stay: two nights.", "Apply the details.",
    ["Soggiorno minimo: due notti."])
Q.q("1.B.5 Word meaning", r"Nell'annuncio, «mezza pensione» significa",
    "colazione e un pasto principale inclusi", [("metà del prezzo", "No."),
                                               ("soggiorno di mezza giornata", "No."),
                                               ("pensione per anziani", "Literal misreading.")],
    "half board.", "Word meaning (1.B.5): hotel term.",
    ["mezza pensione = half board."])
Q.q("1.C.3 Inference", r"Che cosa suggerisce l'espressione «la campagna come una volta»?",
    "un'esperienza autentica legata alle tradizioni del passato", [("una campagna sempre più industriale", "The opposite."),
                                                                  ("una vacanza di un solo giorno", "No."),
                                                                  ("un luogo senza comodità", "There is a pool.")],
    "Nostalgia, authenticity.", "Inference (1.C.3): casale, nonna Ida, own products.",
    ["come una volta → tradizione."])

Q.sec("Listening: Presentation")
Q.src(r"Listening 2 \textperiodcentered\ Presentation (transcript) \textperiodcentered\ «Il bar all'italiana»", [
    r"(PROFESSORESSA) Per molti stranieri il bar italiano è un mistero. Si entra, si paga alla cassa, si mostra lo scontrino al barista e si beve il caffè in piedi, al banco, in pochi minuti.",
    r"(PROFESSORESSA) Perché in piedi? Una ragione è economica: in quasi tutti i bar il caffè al banco costa meno che al tavolo. Ma c'è anche una ragione sociale. Il banco è un luogo democratico: l'avvocato e l'operaio bevono lo stesso caffè, allo stesso prezzo, uno accanto all'altro.",
    r"(PROFESSORESSA) Il bar è anche un punto di riferimento del quartiere. Il barista conosce i clienti per nome e spesso sa come prendono il caffè prima che lo chiedano.",
    r"(PROFESSORESSA) Oggi le grandi catene internazionali arrivano anche in Italia. Riusciranno i piccoli bar di quartiere a resistere? Dipenderà anche dalle nostre abitudini.",
], 5)
Q.q("1.B.1 Main idea", r"Qual è il tema centrale della presentazione?",
    "le abitudini del bar italiano e il loro significato sociale", [("la storia delle catene internazionali", "One detail at the end."),
                                                                   ("come si coltiva il caffè", "No."),
                                                                   ("i prezzi dei ristoranti", "No.")],
    "Café culture.", "Main idea (1.B.1).",
    ["rituale → ragioni → quartiere → futuro."])
Q.q("1.A.1 Detail", r"Che cosa si fa, di solito, prima di ordinare al banco?",
    "si paga alla cassa e si mostra lo scontrino", [("ci si siede a un tavolo", "The coffee is drunk standing."),
                                                    ("si prenota online", "No."),
                                                    ("si lascia la mancia al barista", "Not mentioned.")],
    "Cassa → scontrino → banco.", "Detail (1.A.1).",
    ["si paga alla cassa, si mostra lo scontrino al barista…"])
Q.q("1.C.3 Inference", r"Perché la professoressa definisce il banco «un luogo democratico»?",
    "perché persone di classi sociali diverse bevono lo stesso caffè allo stesso prezzo", [("perché si vota al bar", "Literal misreading."),
                                                                                         ("perché il caffè è gratuito", "It is cheaper, not free."),
                                                                                         ("perché lo gestisce il comune", "No.")],
    "Equality at the counter.", "Inference (1.C.3).",
    ["l'avvocato e l'operaio … uno accanto all'altro."])
Q.q("1.B.4 Organization", r"Come è organizzata la presentazione?",
    "descrive un'abitudine, ne spiega le ragioni e termina con una domanda sul futuro", [("racconta la vita di un barista", "No narrative."),
                                                                                        ("dà una ricetta del caffè", "No."),
                                                                                        ("confronta l'Italia con la Francia", "No.")],
    "Description → reasons → question.", "Organization (1.B.4): Perché in piedi? … Riusciranno…?",
    ["Structure follows the questions."])
Q.q("1.B.3 Point of view", r"Secondo la professoressa, da che cosa dipende il futuro dei bar di quartiere?",
    "anche dalle abitudini dei clienti", [("solo dalle leggi del governo", "She says it depends on habits too."),
                                         ("dal prezzo del caffè nel mondo", "No."),
                                         ("dalle catene internazionali soltanto", "Not her conclusion.")],
    "Dipenderà anche dalle nostre abitudini.", "Point of view (1.B.3): her final sentence.",
    ["Dipenderà anche dalle nostre abitudini."])

Q.frq(kind="Project Presentation", head=r"Question 1 \textperiodcentered\ Project Presentation (practice prompt) \textperiodcentered\ 11 points \textperiodcentered\ 3 + 3 minutes", mins=6,
      directions=[r"Imagine that your project examined how music has accompanied the history of an Italian-speaking community. You have 3 minutes to prepare, using your notes, and 3 minutes to present. Explain at least three factors, with specific examples from your research, and show how cultural perspectives relate to cultural products or practices."],
      prompt=[r"Prompt: \textbf{In che modo la musica ha accompagnato la storia di una comunità italofona?}",
              r"Practice focus (example): the Festival di Sanremo and Italy since 1951."],
      model=[r"Oggi parlerò di come il Festival di Sanremo abbia accompagnato la storia dell'Italia dal dopoguerra a oggi. Mi sono concentrato su tre fattori: il festival come rito nazionale, il boom economico e la rinascita dopo la pandemia.",
             r"Innanzitutto, Sanremo è diventato un rito che unisce il Paese. Dalla mia ricerca è emerso che la prima edizione, nel 1951, fu trasmessa solo alla radio, e che dal 1955 il festival arrivò in televisione. In un'Italia dove molti parlavano soprattutto dialetto, milioni di famiglie ascoltavano le stesse canzoni in italiano nello stesso momento. Questo dimostra quanto la musica abbia contribuito a creare un'identità comune.",
             r"In secondo luogo, il boom economico. Nel 1958 Domenico Modugno vinse con «Nel blu dipinto di blu», la canzone che il mondo conosce come «Volare», che vinse anche due Grammy. Il ritornello sul volare nel cielo esprimeva l'ottimismo di un Paese che si stava ricostruendo e sognava un futuro migliore.",
             r"Infine, la rinascita dopo la pandemia. Nel 2021, con il teatro senza pubblico, vinse una giovane band rock, i Måneskin, che poco dopo vinse anche l'Eurovision. Molti giovani si sono riconosciuti nel loro stile libero e provocatorio. Il loro successo riflette il desiderio di una nuova generazione di farsi sentire, anche all'estero.",
             r"In conclusione, Sanremo è uno specchio dell'Italia: ha unito un Paese diviso dai dialetti, ha cantato la speranza del boom e ha dato voce ai giovani. Ho imparato che una gara di canzoni può raccontare la storia di una nazione meglio di molti libri."],
      rows=[("A Task", 2, "three or more factors, each explained with relevant details", "factors named with no detail, or only one or two factors"),
            ("B Culture", 2, "examples linking perspectives (national unity, optimism, youth) to products or practices", "examples with no perspective (1 point)"),
            ("C Organization", 2, "introduction naming the factors, ordered body, conclusion; varied transitions", "a list of facts"),
            ("D Language", 3, "varied vocabulary and structures (passato remoto and imperfetto, congiuntivo, relative clauses)", "a limited set of basic structures"),
            ("E Delivery", 2, "clear pronunciation, natural pace and intonation", "hesitant or rushed speech")],
      tips=["Each factor follows claim → specific example → perspective (questo dimostra, esprimeva, riflette).", "Change over time is shown with dates (1951, 1955, 1958, 2021).",
            "The festival as a shared ritual is a vivid practice that earns the culture row.", "About 370 words."],
      ask="Prepare for 3 minutes using keywords only, then present aloud for 3 minutes. Then mark your presentation.", lines=14)

GUIDE, QSET = G, Q
