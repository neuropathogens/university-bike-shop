from ap_wl.model import Doc

STEM = "01-families-communities"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 1: Families and Communities", r"Unit 1 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 1 asks what makes a family, how families shape values and traditions, and how communities are changing. Its recommended contexts are family relationships, community activities, social interactions and relationships, and urban and rural communities. This guide gives the vocabulary the exam assumes, the structures for describing relationships and routines, the cultural products, practices and perspectives most often tested (grandparents and childcare, leaving home late, the piazza and the passeggiata, the Misericordie and civil service, villages emptying and houses for one euro), and an Argumentative Essay kit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Words I keep forgetting: \blank[10em]",
        short="Unit 1", sub="Families and Communities")

G.sec("Family and relationships")
G.tex(r"""
\begin{vocab}
i genitori / i parenti & parents / relatives & \emph{parenti} is a false friend \\
i nonni / i nipoti & grandparents / grandchildren (also nephews and nieces) & \\
il figlio unico & only child & \\
la famiglia allargata & extended or blended family & \\
l'unione civile & civil union & recognized in Italy since 2016 \\
il congedo parentale & parental leave & \\
volersi bene & to love each other (family, friends) & \emph{ti voglio bene} \\
\end{vocab}

\begin{compare}{Practice}{What it looks like}{Perspective often cited}
Grandparents as childcare & many grandparents collect grandchildren from school and look after them daily & family solidarity across generations \\
Leaving home late & on average young Italians leave the parental home around age 30 & strong family ties; also high rents and insecure jobs \\
Sunday lunch & the extended family meets for a long midday meal & time together matters more than speed \\
\end{compare}

\begin{keyidea}[Two explanations, both on the exam]
When a source explains why young Italians leave home late, look for both kinds of reasons: \textbf{economic} (rents, precarious work) and \textbf{cultural} (close family ties). Questions often ask which one a speaker emphasizes.
\end{keyidea}
""")
G.q("1 Famiglia", r"Che cosa significa la parola «parenti»?",
    "relatives", [("parents", "Parents are i genitori: parenti is a false friend."),
                  ("grandparents only", "Grandparents are i nonni."),
                  ("neighbors", "Neighbors are i vicini.")],
    "parenti = relatives.", "A classic false friend: i genitori are your parents; i parenti are all your relatives.",
    ["genitori ≠ parenti."])
G.q("1 Famiglia", r"In Italy many grandparents collect their grandchildren from school and look after them every afternoon. Which perspective does this practice most directly reflect?",
    "Families support each other across generations.", [("Children should become independent very early.", "The practice keeps children close to the extended family."),
                                                       ("Schools should end later in the day.", "Not implied."),
                                                       ("Grandparents prefer to live alone.", "The practice shows close contact.")],
    "Grandparent care ↔ intergenerational solidarity.", "Practice (daily care by grandparents) linked to a perspective (family as a support network).",
    ["Practice: nonni look after grandchildren.", "Perspective: family solidarity."])

G.sec("Community and social life")
G.tex(r"""
\begin{vocab}
la piazza & town square & the heart of social life \\
la passeggiata & evening stroll & to see and be seen, greet neighbors \\
la festa patronale & patron-saint festival & processions, bands, fireworks \\
la sagra & local food festival & sagra della castagna, del tartufo \\
il volontariato / il volontario & volunteering / volunteer & \\
la Misericordia & volunteer confraternity & ambulances, care; Florence's dates from 1244 \\
il servizio civile universale & voluntary national civil service & 8--12 months, ages 18--28 \\
la contrada & city ward & Siena's 17 contrade and the Palio \\
\end{vocab}

\textbf{Practices and perspectives.} In the evening many Italians walk through the main street or the piazza: the \emph{passeggiata}. It reflects a perspective that public space belongs to everyone and that being part of a community means being seen in it. In Tuscany, the \emph{Misericordie} have run ambulances and care with volunteers for centuries, a sign of how much value is placed on helping one's neighbors.
""")
G.q("2 Comunità", r"Che cos'è la passeggiata?",
    "una camminata serale per incontrare gente in centro o in piazza", [("una gara di corsa in montagna", "No."),
                                                                         ("una festa religiosa", "That would be a festa patronale."),
                                                                         ("una gita scolastica", "No.")],
    "passeggiata = evening stroll.", "The passeggiata is a social practice: walking, greeting and chatting in public.",
    ["sera + piazza + incontrare → passeggiata."])
G.q("2 Comunità", r"The Misericordia of Florence, a volunteer confraternity, has run care and transport for the sick since 1244. Which perspective does this reflect?",
    "Helping one's neighbors is a shared civic duty.", [("Only the state should care for the sick.", "The volunteers show the opposite."),
                                                       ("Charity is a private family matter only.", "It is organized at the city level."),
                                                       ("Old institutions should be replaced.", "Its continuity suggests the opposite.")],
    "Volunteering ↔ civic solidarity.", "A long-lived institution (product) and the practice of volunteering linked to a perspective (solidarity).",
    ["1244 → centuries of volunteering."])

G.sec("Urban and rural communities")
G.tex(r"""
\begin{vocab}
il borgo / il paese & historic village / small town & \emph{paese} also means country \\
lo spopolamento & depopulation & \\
il comune / il sindaco & municipality / mayor & Italy has about 7,900 comuni \\
il pendolare & commuter & \\
il quartiere & neighborhood & \\
le case a un euro & houses sold for one euro & to bring residents back \\
il lavoro da remoto / lo smart working & remote work & \\
\end{vocab}

\textbf{Cases.} Many hill villages in the Apennines and the South have lost most of their residents as young people moved to cities or abroad. Some mayors sell abandoned houses for one euro, on condition that the buyer restores them within a few years. Remote work has brought some families back; but villages still lack schools, doctors and fast internet.
""")
G.q("3 Città e campagna", r"Perché alcuni sindaci vendono case a un euro?",
    "per riportare abitanti nei borghi che si stanno spopolando", [("per fare soldi con il turismo di massa", "One euro brings no money; the aim is new residents."),
                                                                   ("perché le case sono troppo grandi", "No."),
                                                                   ("per costruire nuovi grattacieli", "No.")],
    "Repopulation.", "One-euro houses come with an obligation to restore them: the goal is new life in the village.",
    ["spopolamento → case a un euro."])
G.q("3 Città e campagna", r"In una frase come «Il paese ha solo seicento abitanti», la parola «paese» significa",
    "piccola città o villaggio", [("nazione", "Paese can mean country, but seicento abitanti points to a village."),
                                  ("campagna senza case", "No."),
                                  ("regione", "No.")],
    "Context decides.", "Paese means country or village; context (600 inhabitants) chooses the meaning.",
    ["seicento abitanti → villaggio."])

G.sec("Structures for relationships and routines")
G.tex(r"""
\begin{compare}{Structure}{Use}{Example}
Possessives with family & no article with a singular, unmodified family noun & mia madre, tuo fratello; but \emph{i miei genitori}, \emph{la mia sorellina} \\
da + present & an action that started in the past and continues & Abito a Napoli \emph{da} tre anni. \\
Reciprocal verbs & each other & Ci sentiamo ogni giorno. Si vogliono bene. \\
stare + gerundio & action in progress & Sto aiutando mia nonna. \\
stare per + infinitive & about to & Il treno sta per partire. \\
\end{compare}

\begin{trap}
\emph{Da} + present for ongoing actions: \emph{Studio l'italiano da due anni} (I have been studying for two years). \emph{Per} is for a finished period: \emph{Ho studiato a Roma per due anni.} \emph{Fa} means ago: \emph{due anni fa}.
\end{trap}
""")
G.q("4 Strutture", r"Scegli la forma corretta: \blank\ madre lavora in ospedale.",
    "Mia", [("La mia", "With a singular, unmodified family noun, the article is dropped."),
            ("Il mio", "Madre is feminine, and the article is dropped."),
            ("Mie", "Madre is singular.")],
    "mia madre.", "Possessives drop the article with singular family nouns (mia madre, tuo zio), but not in the plural (i miei zii).",
    ["singular family noun → no article."])
G.q("4 Strutture", r"Scegli la forma corretta: Abito a Roma \blank\ cinque anni.",
    "da", [("per", "Per marks a finished period; here the action continues."),
           ("fa", "Fa means ago and goes with a past tense."),
           ("tra", "Tra places an event in the future.")],
    "da + present = ongoing.", "Italian uses the present + da for an action still going on.",
    ["abito (still) … da cinque anni."])
G.q("4 Strutture", r"Scegli la forma corretta: I miei cugini e io \blank\ ogni domenica a pranzo dai nonni.",
    "ci vediamo", [("si vedono", "The subject includes io, so the first person plural: ci vediamo."),
                   ("vi vedete", "That is the voi form."),
                   ("ci vedono", "The verb must agree with noi.")],
    "noi → ci vediamo.", "Reciprocal verbs use the reflexive pronoun of the subject: ci vediamo (we see each other).",
    ["i miei cugini e io = noi → ci vediamo."])

G.sec("Task kit: the Argumentative Essay")
G.tex(r"""
Unit 1 topics often ask about the balance between family and independence, or about local communities: \emph{I giovani dovrebbero lasciare presto la casa dei genitori?}, \emph{Il servizio civile dovrebbe essere obbligatorio?}

\begin{compare}{Move}{Phrases}{}
State a position & Ritengo che\ldots; Sono convinto/a che\ldots; A mio parere\ldots & \\
Introduce evidence & Secondo la fonte 1\ldots; Come dimostra il grafico\ldots; L'esperto spiega che\ldots & \\
Explain & Questo dimostra che\ldots; Ciò significa che\ldots & \\
Concede and reply & È vero che\ldots; tuttavia\ldots / Alcuni sostengono che\ldots, ma\ldots & \\
Conclude & In conclusione\ldots; Per concludere\ldots & \\
\end{compare}

\begin{trap}
\emph{Ritengo che}, \emph{credo che} and \emph{penso che} take the congiuntivo; \emph{sono sicuro che} and \emph{è chiaro che} express certainty and take the indicative.
\end{trap}
""")
G.q("5 Saggio", r"Which sentence states a clear position for the essay?",
    "Ritengo che il servizio civile debba restare volontario, ma che lo Stato debba incoraggiarlo di più.", [("Il servizio civile è un tema interessante.", "No position."),
                                                                                                             ("Ci sono vantaggi e svantaggi.", "Listing both sides is not a position."),
                                                                                                             ("Secondo la fonte 2, il 20~\\% dei giovani fa volontariato.", "Evidence, not a position.")],
    "Ritengo che + clear claim.", "Row A needs a clear position; a qualified one is fine.",
    ["volontario, ma incoraggiato → clear, qualified."])
G.q("5 Saggio", r"Scegli la forma corretta: Sono sicuro che il volontariato \blank\ utile ai giovani.",
    "è", [("sia", "Sono sicuro che expresses certainty and takes the indicative."),
          ("fosse", "Certainty in the present takes the present indicative."),
          ("essere", "A conjugated verb is needed.")],
    "Certainty → indicative.", "Expressions of certainty (sono sicuro che, è chiaro che, so che) take the indicative.",
    ["sono sicuro che … è."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 1: Families and Communities: Question Set", r"Unit 1 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Audio Report and an Interview for listening, an Article and Chart and a Promotional Material for reading) on remote workers in a mountain village, leaving the parental home, an intergenerational volunteer program and a neighborhood network, followed by an Argumentative Essay with three sources and the 10-point scoring guide. As on the exam, questions and choices are in Italian; listening sources are printed as transcripts. All sources and data are original and fictional, written for practice. Allow about 25 minutes for the multiple choice and 55 minutes for the essay.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Essay: \blank\ / 10 \qquad Target: 15+ MCQ and 7+ essay \qquad Pace: 75 s per item",
        short="Unit 1", sub="Families and Communities")

Q.sec("Listening: Audio Report")
Q.src(r"Listening 1 \textperiodcentered\ Audio Report (transcript) \textperiodcentered\ «Il ritorno al borgo», Radio Appennino", [
    r"(GIORNALISTA) Vent'anni fa Roccafonda, in Abruzzo, aveva novecento abitanti. Cinque anni fa erano rimasti in trecento. Oggi, per la prima volta da decenni, la popolazione è di nuovo in crescita.",
    r"(GIORNALISTA) Il merito, dice il sindaco, è del lavoro da remoto. «Il comune ha portato la fibra ottica e ha aperto uno spazio di coworking nella vecchia scuola. Sono arrivate venti famiglie da Roma, Milano e perfino dalla Germania.»",
    r"(GIORNALISTA) Ma non è tutto facile. Il pediatra viene solo due volte alla settimana, e l'autobus per la città più vicina parte tre volte al giorno.",
    r"(SINDACO) Le case e la connessione non bastano. Se vogliamo che queste famiglie restino, dobbiamo riaprire la scuola elementare. Senza bambini, un paese non ha futuro.",
], 5)
Q.q("1.A.1 Detail", r"Secondo il servizio, come è cambiata la popolazione di Roccafonda negli ultimi anni?",
    "Dopo un lungo calo, ha ricominciato a crescere.", [("È diminuita costantemente fino a oggi.", "It is growing again for the first time in decades."),
                                                       ("È rimasta stabile per vent'anni.", "It fell from 900 to 300."),
                                                       ("È raddoppiata in un anno.", "Not stated.")],
    "900 → 300 → growing.", "Detail (1.A.1): follow the numbers and the turning point.",
    ["per la prima volta da decenni … in crescita."])
Q.q("1.A.1 Detail", r"Che cosa ha fatto il comune per attirare nuovi abitanti?",
    "Ha portato la fibra ottica e ha aperto un coworking nella vecchia scuola.", [("Ha costruito un ospedale.", "The pediatrician comes only twice a week."),
                                                                                 ("Ha aumentato gli autobus.", "Only three a day."),
                                                                                 ("Ha regalato automobili.", "No.")],
    "Fiber + coworking.", "Detail (1.A.1): the mayor's quotation.",
    ["…la fibra ottica … uno spazio di coworking…"])
Q.q("1.B.4 Organization", r"Come è organizzato il servizio?",
    "Presenta un cambiamento, ne spiega la causa, indica i problemi e finisce con una proposta.", [("Racconta la storia del paese dal Medioevo.", "No history."),
                                                                                                    ("Confronta due paesi italiani.", "Only one village."),
                                                                                                    ("Elenca le opinioni di molti abitanti.", "Only the mayor speaks.")],
    "Change → cause → problems → proposal.", "Organization (1.B.4): Ma non è tutto facile marks the turn to problems.",
    ["crescita → merito → Ma… → dobbiamo riaprire."])
Q.q("1.B.3 Point of view", r"Secondo il sindaco, che cosa serve perché le nuove famiglie restino?",
    "riaprire la scuola elementare", [("costruire più case", "He says houses are not enough."),
                                      ("aumentare la connessione", "He says connection is not enough."),
                                      ("attirare turisti", "Not mentioned.")],
    "La scuola.", "Point of view (1.B.3): non bastano … dobbiamo riaprire la scuola.",
    ["Se vogliamo che restino, dobbiamo riaprire la scuola elementare."])
Q.q("1.C.3 Inference", r"Che cosa vuole dire il sindaco con «Senza bambini, un paese non ha futuro»?",
    "Una comunità sopravvive solo se ci sono nuove generazioni.", [("I bambini devono lavorare in paese.", "Literal misreading."),
                                                                 ("Gli anziani devono lasciare il paese.", "No."),
                                                                 ("Il paese deve diventare una città.", "No.")],
    "Children = continuity.", "Inference (1.C.3): the school matters because young families are the village's future.",
    ["bambini → futuro della comunità."])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 1 \textperiodcentered\ Article and Chart \textperiodcentered\ «A trent'anni ancora a casa?», rivista Generazioni", [
    r"In Italia i giovani lasciano la casa dei genitori in media verso i trent'anni, molto più tardi che nel Nord Europa. Spesso vengono chiamati «mammoni», ma secondo la sociologa Laura Conti l'etichetta è ingiusta.",
    r"«Gli affitti nelle città universitarie sono cresciuti molto più degli stipendi, e molti primi contratti di lavoro sono a tempo determinato», spiega Conti. «Non è pigrizia: è un calcolo economico.»",
    r"Conti riconosce però anche un fattore culturale. «In molte famiglie italiane vivere insieme da adulti non è visto come un fallimento. I genitori aiutano i figli, e più tardi i figli aiuteranno i genitori. È un patto tra generazioni.»",
], 5, table=(["Paese", "Età media all'uscita dalla casa dei genitori"], [["Svezia", "22 anni"], ["Germania", "24 anni"], ["Francia", "25 anni"], ["Italia", "30 anni"], ["Croazia", "32 anni"]]),
      note="Dati fittizi.")
Q.q("1.A.2 Data", r"Secondo la tabella, in quale paese i giovani lasciano la casa dei genitori più tardi?",
    "in Croazia", [("in Italia", "Italy is 30; Croatia is 32."),
                   ("in Svezia", "Sweden is the earliest."),
                   ("in Germania", "24.")],
    "Croazia: 32.", "Data (1.A.2): find the maximum; the article is about Italy, but the chart includes other countries.",
    ["32 > 30."])
Q.q("1.A.2 Data", r"Quanti anni in più rispetto ai giovani svedesi restano a casa, in media, i giovani italiani?",
    "otto", [("sei", "30 − 22 = 8."),
             ("trenta", "That is Italy's average age."),
             ("due", "That is the gap between Croatia and Italy.")],
    "30 − 22 = 8.", "Data (1.A.2): compare two rows.",
    ["Italia 30, Svezia 22 → 8."])
Q.q("1.B.3 Point of view", r"Che cosa pensa Laura Conti della parola «mammoni»?",
    "che sia un'etichetta ingiusta", [("che descriva bene i giovani italiani", "She calls it unfair."),
                                     ("che sia un complimento", "No."),
                                     ("che si usi solo in Croazia", "No.")],
    "l'etichetta è ingiusta.", "Point of view (1.B.3).",
    ["…secondo la sociologa … l'etichetta è ingiusta."])
Q.q("1.B.4 Organization", r"Quale funzione ha la parola «però» nell'ultimo paragrafo?",
    "introduce un secondo tipo di spiegazione, quella culturale", [("conclude il ragionamento economico", "It adds a different factor."),
                                                                  ("contraddice tutto l'articolo", "It complements, not contradicts."),
                                                                  ("introduce un esempio di pigrizia", "She rejects laziness.")],
    "però → another factor.", "Organization (1.B.4): economic reasons, then però + cultural reasons.",
    ["Conti riconosce però anche un fattore culturale."])
Q.q("1.C.2 Conclusion", r"Che cosa si può concludere dall'articolo?",
    "Il ritardo nell'uscita di casa ha cause sia economiche sia culturali.", [("I giovani italiani sono pigri.", "Conti rejects that."),
                                                                             ("Gli affitti italiani sono i più bassi d'Europa.", "They rose faster than salaries."),
                                                                             ("Nessun genitore vuole aiutare i figli.", "The opposite.")],
    "Both causes.", "Conclusions (1.C.2): the article gives an economic and a cultural explanation.",
    ["affitti + contratti / patto tra generazioni."])

Q.sec("Reading: Promotional Material")
Q.src(r"Reading 2 \textperiodcentered\ Promotional Material \textperiodcentered\ Volantino dell'associazione «Ponti d'argento»", [
    r"\textbf{ADOTTA UN NONNO! \textperiodcentered\ Associazione Ponti d'argento, Torino}",
    r"Hai tra i 16 e i 25 anni e un paio d'ore libere alla settimana? Tanti anziani del quartiere vivono soli e aspettano qualcuno con cui fare due chiacchiere, giocare a carte o imparare a usare lo smartphone.",
    r"\textbf{Come funziona:} partecipi a un incontro di formazione di tre ore, poi ti presentiamo un «nonno» o una «nonna» che vive vicino a te. Vi vedete almeno una volta alla settimana, a casa sua o al centro anziani.",
    r"\textbf{Che cosa ci guadagni:} un attestato valido come credito formativo per la scuola, e tante storie che nessun libro ti racconterà.",
    r"Iscrizioni entro il 31 ottobre sul nostro sito. Partecipazione gratuita.",
], 5)
Q.q("1.B.2 Audience", r"A chi si rivolge il volantino?",
    "ai ragazzi tra i 16 e i 25 anni", [("agli anziani che vivono soli", "They are the people to be visited."),
                                         ("ai genitori di bambini piccoli", "No."),
                                         ("ai medici del quartiere", "No.")],
    "16–25 anni.", "Audience (1.B.2): the opening question addresses young people.",
    ["Hai tra i 16 e i 25 anni…?"])
Q.q("1.A.1 Detail", r"Che cosa deve fare un volontario prima di conoscere il suo «nonno»?",
    "partecipare a un incontro di formazione", [("pagare una quota", "Participation is free."),
                                               ("superare un esame di italiano", "Not mentioned."),
                                               ("trasferirsi a Torino", "Not mentioned.")],
    "Formazione di tre ore.", "Detail (1.A.1).",
    ["partecipi a un incontro di formazione di tre ore, poi…"])
Q.q("1.B.5 Word meaning", r"Nel volantino, «fare due chiacchiere» significa",
    "parlare un po' in modo informale", [("discutere in modo aggressivo", "No."),
                                        ("fare due telefonate", "No."),
                                        ("scrivere due lettere", "No.")],
    "Idiom: to have a chat.", "Word meaning (1.B.5).",
    ["due chiacchiere = a little chat."])
Q.q("1.A.1 Detail", r"Quale vantaggio scolastico offre il programma?",
    "un attestato valido come credito formativo", [("un viaggio all'estero", "Not offered."),
                                                  ("uno stipendio mensile", "Not offered."),
                                                  ("l'esonero dagli esami", "Not offered.")],
    "Credito formativo.", "Detail (1.A.1).",
    ["un attestato valido come credito formativo per la scuola."])
Q.q("1.C.3 Inference", r"Che cosa suggerisce la frase «tante storie che nessun libro ti racconterà»?",
    "che i giovani possono imparare dall'esperienza degli anziani", [("che gli anziani scrivono libri", "Figurative misreading."),
                                                                    ("che i libri sono inutili", "Too extreme."),
                                                                    ("che l'associazione vende libri", "No.")],
    "Learning from elders.", "Inference (1.C.3): the exchange goes both ways.",
    ["storie → esperienza degli anziani."])

Q.sec("Listening: Interview")
Q.src(r"Listening 2 \textperiodcentered\ Interview (transcript) \textperiodcentered\ «La via che è diventata una famiglia»", [
    r"(GIORNALISTA) Signora Rinaldi, tre anni fa lei ha creato un gruppo di messaggi per gli abitanti della sua via. Com'è nata l'idea?",
    r"(SIG.RA RINALDI) Mi ero appena trasferita e non conoscevo nessuno. Ho lasciato un biglietto in ogni cassetta della posta: «Chi vuole conoscere i vicini?» Il primo giorno hanno risposto in dodici.",
    r"(GIORNALISTA) E oggi?",
    r"(SIG.RA RINALDI) Siamo in trecento. Ci prestiamo il trapano, ci scambiamo i libri, d'estate organizziamo una cena lunga tutta la via. Durante un'ondata di caldo i ragazzi hanno fatto la spesa per gli anziani.",
    r"(GIORNALISTA) C'è qualcosa che non funziona?",
    r"(SIG.RA RINALDI) A volte il gruppo diventa troppo rumoroso, con cento messaggi al giorno. Ma preferisco questo al silenzio di quando sono arrivata.",
], 5)
Q.q("1.A.1 Detail", r"Perché la signora Rinaldi ha creato il gruppo?",
    "perché si era appena trasferita e non conosceva nessuno", [("perché voleva vendere qualcosa", "No."),
                                                               ("perché il comune glielo aveva chiesto", "No."),
                                                               ("perché c'era un'ondata di caldo", "That came later.")],
    "New in the street.", "Detail (1.A.1).",
    ["Mi ero appena trasferita e non conoscevo nessuno."])
Q.q("1.B.1 Main idea", r"Qual è il tema principale dell'intervista?",
    "come un gruppo di vicini ha creato legami di solidarietà", [("i problemi degli smartphone", "A minor point."),
                                                               ("la storia della città", "No."),
                                                               ("il caldo estivo", "One example.")],
    "Neighborhood solidarity.", "Main idea (1.B.1).",
    ["biglietto → 12 → 300 → prestiti, cene, aiuto."])
Q.q("1.B.5 Word meaning", r"Nell'intervista, «ci prestiamo il trapano» significa che i vicini",
    "si danno gli attrezzi per un periodo e poi li restituiscono", [("comprano insieme un trapano", "Prestare means to lend."),
                                                                   ("vendono attrezzi usati", "No."),
                                                                   ("riparano la strada", "No.")],
    "prestare = to lend.", "Word meaning (1.B.5): reciprocal ci + prestare.",
    ["prestarsi → lend to each other."])
Q.q("1.C.3 Inference", r"Che cosa mostra l'esempio dell'ondata di caldo?",
    "che il gruppo aiuta concretamente le persone più fragili", [("che i ragazzi non escono d'estate", "No."),
                                                                 ("che gli anziani organizzano le cene", "No."),
                                                                 ("che il gruppo è solo virtuale", "The help was concrete.")],
    "Concrete help.", "Inference (1.C.3): online contact led to real support.",
    ["i ragazzi hanno fatto la spesa per gli anziani."])
Q.q("1.B.3 Attitude", r"Come giudica la signora Rinaldi i troppi messaggi del gruppo?",
    "un piccolo difetto, preferibile all'isolamento", [("un motivo per chiudere il gruppo", "She prefers it to silence."),
                                                       ("un grave pericolo", "Too strong."),
                                                       ("un vantaggio", "She calls it a problem.")],
    "Ma preferisco questo al silenzio.", "Attitude (1.B.3): she admits the flaw and weighs it.",
    ["A volte … troppo rumoroso. Ma preferisco questo al silenzio."])

Q.frq(kind="Argumentative Essay", head=r"Question 3 \textperiodcentered\ Argumentative Essay \textperiodcentered\ 10 points \textperiodcentered\ 55 minutes", mins=55,
      directions=[r"Scrivi un saggio argomentativo per un corso universitario. Leggi il tema e le fonti scritte; poi ascolta la fonte audio (qui come trascrizione). Scrivi un saggio che usi informazioni tratte da tutte e tre le fonti per sostenere la tua posizione. Cita le fonti con il numero, il titolo o l'autore."],
      sources=[dict(title=r"Fonte 1 \textperiodcentered\ Articolo \textperiodcentered\ «Un anno in ambulanza»", paras=[
          r"Giulia ha 20 anni e da dieci mesi fa il servizio civile in un'associazione di volontariato a Prato. Accompagna gli anziani alle visite mediche, risponde al telefono di notte e ha imparato il primo soccorso. «All'inizio l'ho fatto per il piccolo rimborso mensile», ammette. «Adesso so cosa voglio fare: l'infermiera.»",
          r"La responsabile, Anna Bellini, vorrebbe che tutti i giovani facessero un'esperienza simile. «Qui ragazzi di quartieri diversi lavorano insieme e scoprono la città che non vedevano», dice. Ma i posti disponibili sono pochi: quest'anno le domande sono state il doppio dei posti."]),
               dict(title=r"Fonte 2 \textperiodcentered\ Grafico \textperiodcentered\ Giovani che fanno volontariato almeno una volta al mese", paras=[
          r"Percentuale per fascia d'età (dati fittizi)."],
                    table=(["Fascia d'età", "Percentuale"], [["15--19 anni", "14~\\%"], ["20--24 anni", "11~\\%"], ["25--29 anni", "9~\\%"], ["Media della popolazione adulta", "12~\\%"]])),
               dict(title=r"Fonte 3 \textperiodcentered\ Audio (trascrizione) \textperiodcentered\ «Obbligo o scelta?», Radio Città", paras=[
          r"(GIORNALISTA) Ne parliamo con il pedagogista Luca Moretti. Professore, il servizio civile dovrebbe diventare obbligatorio?",
          r"(LUCA MORETTI) Capisco l'idea, ma il volontariato nasce da una scelta. Se lo rendessimo obbligatorio, molti ragazzi lo vivrebbero come una punizione, e le associazioni si ritroverebbero con persone poco motivate.",
          r"(GIORNALISTA) Allora che cosa propone?",
          r"(LUCA MORETTI) Di aumentare i posti e i riconoscimenti: crediti universitari, punti nei concorsi pubblici. Bisogna rendere il servizio civile attraente, non imposto."])],
      prompt=[r"Tema del saggio: \textbf{Il servizio civile dovrebbe essere obbligatorio per tutti i giovani?}"],
      model=[r"In un'epoca in cui molti giovani si sentono lontani dalla vita della loro comunità, alcuni propongono di rendere obbligatorio il servizio civile. Pur riconoscendone il valore, ritengo che il servizio debba restare volontario, ma che lo Stato debba renderlo molto più accessibile e attraente.",
             r"Innanzitutto, il servizio civile può cambiare la vita di un giovane. Nella fonte 1, Giulia racconta che dopo dieci mesi in un'associazione di volontariato ha capito di voler diventare infermiera. La responsabile, Anna Bellini, aggiunge che il servizio fa incontrare ragazzi di quartieri diversi. Questo dimostra che l'esperienza costruisce competenze e senso di comunità.",
             r"Tuttavia, un obbligo rischierebbe di distruggere proprio ciò che rende prezioso il volontariato. Come spiega il pedagogista Luca Moretti nella fonte 3, se il servizio diventasse obbligatorio, molti ragazzi lo vivrebbero come una punizione e le associazioni avrebbero volontari poco motivati.",
             r"È vero che pochi giovani fanno volontariato: secondo il grafico della fonte 2, solo l'11~\% dei ragazzi tra i 20 e i 24 anni lo fa almeno una volta al mese, meno della media degli adulti (12~\%). Ma il problema non sembra la mancanza di interesse: nella fonte 1 si legge che le domande sono state il doppio dei posti. Bisognerebbe quindi aumentare i posti e, come propone Moretti, offrire crediti universitari e punti nei concorsi pubblici.",
             r"In conclusione, il servizio civile non dovrebbe essere imposto, ma offerto a tutti coloro che lo desiderano. Se lo Stato investisse di più, molti altri giovani come Giulia potrebbero scoprire la propria strada aiutando gli altri."],
      rows=[("A Position", 1, "a clear position (voluntary, but expanded and encouraged)", "only lists advantages and disadvantages"),
            ("B Source use", 2, "all three sources used accurately and named; the chart's age groups kept straight", "two sources, or misreading the chart"),
            ("C Argumentation", 2, "each claim explained with evidence (questo dimostra che)", "quotes with no link to the claims"),
            ("D Organization", 2, "introduction, claims, concession and reply, conclusion", "one paragraph per source"),
            ("E Language control", 3, "congiuntivo (debba, diventasse), periodo ipotetico, varied connectors", "basic structures; copying the sources")],
      tips=["The concession uses the chart honestly, then turns it with a detail from source 1 (twice as many applications as places).", "Every source is named and paraphrased.",
            "Two periodi ipotetici (se … diventasse, vivrebbero; se … investisse, potrebbero) show control.", "About 340 words."],
      ask="Write your essay in Italian (about 300–350 words), then mark it against each row.", lines=22)

GUIDE, QSET = G, Q
