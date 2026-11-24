from ap_wl.model import Doc

STEM = "06-global-contexts"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 6: Global Contexts", r"Unit 6 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 6 asks how global issues affect families and communities, and how people and governments respond. Its recommended contexts are global communication, the natural world, history, policy and planning, and transportation. This guide gives the vocabulary of the environment, history and public policy, the cases most often tested (drought and glaciers, earthquakes and the Protezione Civile, Venice's MOSE barriers, unification and the Republic, emigration and immigration, Italy in Europe, high-speed rail, limited-traffic zones and overtourism), the language for proposing solutions, and an Argumentative Essay kit on counterarguments. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Solutions I can propose: \blank[10em]",
        short="Unit 6", sub="Global Contexts")

G.sec("The natural world")
G.tex(r"""
\begin{vocab}
il cambiamento climatico & climate change & \\
la siccità & drought & the Po, Italy's longest river, hit record lows in 2022 \\
il ghiacciaio & glacier & Alpine glaciers are shrinking fast \\
il dissesto idrogeologico & landslide and flood risk & \\
il terremoto / la Protezione Civile & earthquake / civil protection agency & thousands of volunteers \\
l'acqua alta / il MOSE & high tide in Venice / mobile flood barriers & in operation since 2020 \\
il parco nazionale & national park & Gran Paradiso, the first, dates from 1922 \\
\end{vocab}

\textbf{Cases.} Italy is exposed to earthquakes, volcanoes, floods and droughts. After every disaster, volunteers of the Protezione Civile and of associations arrive from all over the country. In Venice, the MOSE barriers rise from the sea floor to close the lagoon during exceptional high tides.
""")
G.q("1 Natura", r"A che cosa serve il MOSE di Venezia?",
    "a proteggere la città dall'acqua alta chiudendo la laguna", [("a produrre energia elettrica", "No."),
                                                                  ("a portare i turisti con le gondole", "No."),
                                                                  ("a misurare i terremoti", "No.")],
    "MOSE = flood barriers.", "Mobile barriers rise at the lagoon inlets during exceptional high tides.",
    ["acqua alta → MOSE."])
G.q("1 Natura", r"After earthquakes and floods, thousands of Protezione Civile volunteers from all over Italy come to help. Which perspective does this reflect?",
    "Solidarity in an emergency is a duty shared by the whole country.", [("Each region should manage disasters alone.", "Volunteers come from everywhere."),
                                                                         ("Only professionals should help.", "Volunteers are central."),
                                                                         ("Disasters cannot be prevented or managed.", "Not implied.")],
    "Volunteers ↔ national solidarity.", "Practice (volunteering in emergencies) ↔ perspective (solidarity across regions).",
    ["volontari da tutta Italia → solidarietà."])

G.sec("History and memory")
G.tex(r"""
\begin{vocab}
il Risorgimento & the movement for unification & \\
l'Unità d'Italia & unification & March 17, 1861 \\
la Repubblica / la Costituzione & the Republic / the Constitution & referendum 1946; Constitution in force January 1, 1948 \\
i Trattati di Roma & Treaties of Rome & 1957: Italy co-founds the EEC \\
l'emigrazione / l'immigrazione & emigration / immigration & \\
la memoria & remembrance & January 27, Giorno della Memoria \\
\end{vocab}

\textbf{From emigration to immigration.} Between the 1870s and the 1970s, millions of Italians emigrated to the Americas, Australia and northern Europe, and many moved from the South to the industrial North. Since the 1980s Italy has also become a country of immigration. The perspective many Italians cite: a country that knows emigration should understand those who arrive.
""")
G.q("2 Storia", r"Quando è entrata in vigore la Costituzione della Repubblica italiana?",
    "il 1° gennaio 1948", [("il 17 marzo 1861", "That is unification."),
                           ("il 2 giugno 1946", "That is the referendum on the Republic."),
                           ("il 25 marzo 1957", "That is the Treaties of Rome.")],
    "Costituzione → 1948.", "The Constitution was approved in December 1947 and took effect on January 1, 1948.",
    ["1946 referendum → 1948 Costituzione."])
G.q("2 Storia", r"In 1957 Italy signed the Treaties of Rome. What did they create?",
    "the European Economic Community, ancestor of today's EU", [("the Italian Republic", "That was 1946."),
                                                               ("NATO", "NATO was founded in 1949 in Washington."),
                                                               ("the United Nations", "Founded in 1945.")],
    "Trattati di Roma → CEE.", "Italy was one of the six founding members of the EEC.",
    ["1957 → CEE."])

G.sec("Policy, planning and transportation")
G.tex(r"""
\begin{vocab}
l'alta velocità & high-speed rail & Milan to Rome in about three hours \\
la ZTL (zona a traffico limitato) & limited-traffic zone & historic centers closed to most cars \\
la pista ciclabile & bike lane & \\
il sovraturismo / l'overtourism & overtourism & \\
il contributo di accesso & entry fee for day-trippers & Venice, from 2024, on peak days \\
gli affitti brevi & short-term rentals & residents priced out \\
\end{vocab}

\textbf{Cases.} Historic centers protect their streets with ZTLs: only residents and authorized vehicles may enter, and cameras fine the others. High-speed trains have made the train faster than the plane between Milan and Rome. In 2024 Venice became the first city to charge day-trippers an entry fee on peak days. The perspective in all three: shared heritage and public space must be protected and planned.
""")
G.q("3 Trasporti", r"Che cos'è una ZTL?",
    "una zona del centro dove solo i veicoli autorizzati possono entrare", [("una strada con il limite di velocità più alto", "No."),
                                                                            ("un parcheggio gratuito", "No."),
                                                                            ("una linea di treni veloci", "That is alta velocità.")],
    "ZTL = limited-traffic zone.", "ZTLs restrict cars in historic centers; cameras fine unauthorized vehicles.",
    ["zona a traffico limitato."])
G.q("3 Trasporti", r"In 2024 Venice began charging day-trippers an entry fee on peak days. Which goal does this policy most directly pursue?",
    "reducing crowding to protect the city and its residents", [("attracting as many day-trippers as possible", "The opposite."),
                                                               ("closing the city to all tourists", "Overnight visitors and many others are exempt."),
                                                               ("raising money for new hotels", "Not the aim.")],
    "Fee ↔ managing overtourism.", "The fee aims to discourage day-trips on the busiest days.",
    ["contributo di accesso → meno folla."])

G.sec("Structures: proposing solutions")
G.tex(r"""
\begin{compare}{Purpose}{Structure}{Example}
Necessity & bisogna / occorre + infinitive; bisogna che + congiuntivo & Bisogna risparmiare acqua. \\
Recommendation & si dovrebbe; sarebbe opportuno che + congiuntivo imperfetto & Sarebbe opportuno che il comune investisse nei treni. \\
Obligation (passive) & andare + participle & I rifiuti vanno differenziati. \\
Purpose & per + infinitive; affinché + congiuntivo & Si piantano alberi affinché la città sia più fresca. \\
Proportion & più\ldots, più / meno\ldots & Più persone usano il treno, meno traffico c'è. \\
Condition & purché, a condizione che (+ congiuntivo) & Sono favorevole, purché i residenti siano esenti. \\
\end{compare}

\begin{trap}
After a condizionale main clause (\emph{vorrei che, sarebbe opportuno che}) use the congiuntivo \emph{imperfetto}: \emph{Sarebbe meglio che tutti \textbf{usassero} i mezzi pubblici}, not \emph{usino}.
\end{trap}
""")
G.q("4 Soluzioni", r"Scegli la forma corretta: Sarebbe opportuno che il comune \blank\ più piste ciclabili.",
    "costruisse", [("costruisce", "Sarebbe opportuno che requires the congiuntivo."),
                   ("costruisca", "After a condizionale main clause, use the congiuntivo imperfetto."),
                   ("costruirebbe", "The condizionale does not follow che here.")],
    "condizionale + che → congiuntivo imperfetto.", "Sequence of tenses: sarebbe opportuno che + congiuntivo imperfetto.",
    ["sarebbe opportuno che … costruisse."])
G.q("4 Soluzioni", r"Scegli la forma corretta: Le bottiglie di vetro \blank\ nel contenitore verde.",
    "vanno buttate", [("vanno buttato", "The participle agrees with le bottiglie."),
                      ("va buttate", "The subject le bottiglie is plural."),
                      ("vanno buttare", "Andare + participle, not infinitive.")],
    "andare + participle = must be.", "The passive with andare expresses obligation; the participle agrees with the subject.",
    ["le bottiglie → vanno buttate."])

G.sec("Task kit: answering the other side")
G.tex(r"""
Global-context essays (\emph{Le città d'arte dovrebbero far pagare un biglietto ai turisti?}, \emph{La tutela dell'ambiente è più importante del lavoro?}) almost always come with one source that disagrees with you. Use it: a counterargument answered well shows argumentation and earns credit for that source.

\begin{terms}
Concede & \emph{È vero che\ldots / Certo, \ldots} + the opposing point with its source \\
Answer & \emph{Tuttavia\ldots / Eppure\ldots} + evidence from another source or a solution \\
Limit & \emph{purché / a condizione che} (+ congiuntivo): under what conditions your position holds \\
\end{terms}

\begin{keyidea}[Qualified positions]
\emph{Un biglietto d'ingresso è utile, purché i residenti e chi lavora in città siano esenti} is a clear position (Row A) that already includes the reply to the strongest objection.
\end{keyidea}
""")
G.q("5 Saggio", r"A source says an entry fee would turn the city into a theme park. How should an essay in favor of the fee use this source?",
    "concede the point and answer it with evidence or a solution", [("ignore it so the essay stays one-sided", "Ignoring a source loses source-use points."),
                                                                     ("change position to agree with it", "One objection does not require abandoning a position."),
                                                                     ("quote it with no comment", "Evidence without explanation does not earn argumentation credit.")],
    "Concede + answer.", "Answering the opposing source strengthens argumentation and still counts toward using all three sources.",
    ["È vero che… tuttavia…"])
G.q("5 Saggio", r"Scegli la forma corretta: Sono favorevole al biglietto, purché i residenti \blank\ esenti.",
    "siano", [("sono", "Purché requires the congiuntivo."),
              ("saranno", "Purché requires the congiuntivo, not the future."),
              ("essere", "A conjugated verb is needed.")],
    "purché + congiuntivo.", "Conditional conjunctions (purché, a condizione che) take the congiuntivo.",
    ["purché … siano."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 6: Global Contexts: Question Set", r"Unit 6 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Interview and an Instructional Guidance for listening, an Article and an Article and Chart for reading) on a civil protection volunteer, high-speed rail, ski resorts without snow and what to do in an earthquake, followed by an Argumentative Essay with three sources and the 10-point scoring guide. As on the exam, questions and choices are in Italian; listening sources are printed as transcripts. All sources and data are original and fictional, written for practice. Allow about 25 minutes for the multiple choice and 55 minutes for the essay.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Essay: \blank\ / 10 \qquad Target: 15+ MCQ and 7+ essay \qquad Pace: 75 s per item",
        short="Unit 6", sub="Global Contexts")

Q.sec("Listening: Interview")
Q.src(r"Listening 1 \textperiodcentered\ Interview (transcript) \textperiodcentered\ Una volontaria della Protezione Civile", [
    r"(GIORNALISTA) Elisa, lei ha 24 anni e fa la volontaria della Protezione Civile. Dove è stata l'ultima volta?",
    r"(ELISA) In Romagna, dopo l'alluvione. Per due settimane abbiamo spalato fango dalle case e dalle cantine, insieme ai ragazzi del posto. Molti di loro non avevano mai preso in mano una pala.",
    r"(GIORNALISTA) Che cosa l'ha colpita di più?",
    r"(ELISA) Le persone anziane che ci offrivano il caffè anche quando avevano perso tutto. La casa era piena d'acqua, ma l'ospitalità no.",
    r"(GIORNALISTA) Che cosa si potrebbe fare meglio?",
    r"(ELISA) La prevenzione. Noi arriviamo dopo, ma molti danni si potrebbero evitare pulendo i fiumi e non costruendo dove l'acqua è sempre passata. Spalare il fango è importante; non doverlo spalare sarebbe meglio.",
], 5)
Q.q("1.A.1 Detail", r"Che cosa ha fatto Elisa in Romagna?",
    "ha spalato il fango dalle case insieme ai giovani del posto", [("ha costruito nuove case", "No."),
                                                                   ("ha organizzato una raccolta fondi", "Not mentioned."),
                                                                   ("ha studiato i fiumi", "No.")],
    "Spalare fango.", "Detail (1.A.1).",
    ["abbiamo spalato fango dalle case e dalle cantine."])
Q.q("1.C.3 Inference", r"Che cosa vuole dire Elisa con «La casa era piena d'acqua, ma l'ospitalità no»?",
    "che le persone restavano generose anche nella disgrazia", [("che le case erano asciutte", "Literal misreading."),
                                                               ("che gli anziani non volevano aiuto", "No."),
                                                               ("che il caffè era finito", "No.")],
    "Generosity in disaster.", "Figurative language (1.C.3): wordplay on piena.",
    ["offrivano il caffè anche quando avevano perso tutto."])
Q.q("1.B.3 Point of view", r"Secondo Elisa, che cosa si dovrebbe migliorare?",
    "la prevenzione, per esempio pulendo i fiumi e non costruendo nelle zone a rischio", [("il numero di volontari", "Not her point."),
                                                                                          ("la velocità degli aiuti", "Not her point."),
                                                                                          ("le pale dei volontari", "No.")],
    "Prevenzione.", "Point of view (1.B.3).",
    ["La prevenzione … pulendo i fiumi e non costruendo…"])
Q.q("1.B.5 Word meaning", r"Nell'intervista, «spalare» significa",
    "togliere qualcosa con una pala", [("pulire con l'acqua", "No."),
                                       ("costruire muri", "No."),
                                       ("trasportare persone", "No.")],
    "pala → spalare.", "Word meaning (1.B.5): derived from pala (shovel).",
    ["spalare fango → with a shovel."])
Q.q("1.B.4 Organization", r"Come è costruita l'ultima risposta di Elisa?",
    "riconosce il valore dell'aiuto e propone di agire prima del disastro", [("racconta un ricordo d'infanzia", "No."),
                                                                             ("confronta due paesi", "No."),
                                                                             ("elenca le cause del cambiamento climatico", "No.")],
    "Concession + proposal.", "Organization (1.B.4): Noi arriviamo dopo, ma… / è importante; … sarebbe meglio.",
    ["after vs. before → prevention."])

Q.sec("Reading: Article")
Q.src(r"Reading 1 \textperiodcentered\ Article \textperiodcentered\ «Il treno che ha accorciato l'Italia»", [
    r"Fino a vent'anni fa, per andare da Milano a Roma conveniva prendere l'aereo. Oggi l'alta velocità collega le due città in circa tre ore, da centro a centro, e molti viaggiatori d'affari hanno abbandonato i voli.",
    r"«Posso lavorare durante il viaggio e arrivo direttamente in ufficio, senza code all'aeroporto», racconta Luca, avvocato, che fa la tratta due volte a settimana. Il treno, inoltre, inquina molto meno dell'aereo.",
    r"Ma il geografo Carlo Pace avverte: «L'alta velocità ha accorciato le distanze tra le grandi città, ma non ovunque. In molte zone del Sud e nelle aree interne i treni regionali sono lenti e rari. Il rischio è un Paese a due velocità.»",
], 5)
Q.q("1.B.1 Main idea", r"Qual è l'idea principale dell'articolo?",
    "L'alta velocità ha cambiato i viaggi tra le grandi città, ma non tutta l'Italia ne beneficia.", [("L'aereo resta il mezzo più veloce tra Milano e Roma.", "The train now wins."),
                                                                                                      ("I treni regionali sono più veloci di quelli ad alta velocità.", "The opposite."),
                                                                                                      ("Nessuno usa più il treno.", "No.")],
    "Benefit + limit.", "Main idea (1.B.1).",
    ["tre ore … Ma … non ovunque."])
Q.q("1.A.1 Detail", r"Quanto dura oggi, circa, il viaggio in treno da Milano a Roma?",
    "tre ore", [("un'ora", "No."),
                ("sei ore", "No."),
                ("un giorno", "No.")],
    "circa tre ore.", "Detail (1.A.1).",
    ["…collega le due città in circa tre ore."])
Q.q("1.A.1 Detail", r"Quale vantaggio del treno cita Luca?",
    "può lavorare durante il viaggio e arrivare in centro senza code", [("costa sempre meno dell'aereo", "Not his point."),
                                                                         ("può dormire in cabina", "No."),
                                                                         ("non deve comprare il biglietto", "No.")],
    "Work + city center.", "Detail (1.A.1).",
    ["Posso lavorare durante il viaggio e arrivo direttamente in ufficio…"])
Q.q("1.B.5 Word meaning", r"Che cosa intende Carlo Pace con «un Paese a due velocità»?",
    "un'Italia in cui alcune zone sono ben collegate e altre restano indietro", [("un Paese con due tipi di treni veloci", "Figurative."),
                                                                                ("un Paese con due capitali", "No."),
                                                                                ("un Paese dove si guida a due velocità", "No.")],
    "Inequality.", "Word meaning (1.B.5): figurative.",
    ["Sud e aree interne lenti → due velocità."])
Q.q("1.B.4 Organization", r"Quale funzione ha la parola «Ma» all'inizio dell'ultimo paragrafo?",
    "introduce un limite dopo la descrizione dei vantaggi", [("riassume l'articolo", "No."),
                                                            ("aggiunge un altro vantaggio", "It introduces a limit."),
                                                            ("cambia completamente argomento", "Same topic.")],
    "Contrast transition.", "Organization (1.B.4).",
    ["advantages → Ma → limits."])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 2 \textperiodcentered\ Article and Chart \textperiodcentered\ «Montagna senza neve?»", [
    r"Nelle stazioni sciistiche dell'Appennino la neve naturale è sempre più rara. Per salvare la stagione, molti impianti usano la neve artificiale, che però richiede grandi quantità di acqua e di energia.",
    r"Alcuni comuni scelgono un'altra strada: puntano su escursioni, mountain bike e turismo tutto l'anno. «La montagna non è solo lo sci», dice il sindaco di un piccolo paese. «Se ci adattiamo, i turisti verranno anche in estate.»",
], 5, table=(["Stagione (località fittizia)", "Giorni con neve naturale", "Giorni con neve artificiale"],
             [["1995--96", "98", "12"], ["2005--06", "81", "30"], ["2015--16", "55", "61"], ["2025--26", "38", "79"]]),
      note="Dati fittizi.")
Q.q("1.A.2 Data", r"Secondo la tabella, in quale stagione i giorni con neve artificiale hanno superato per la prima volta quelli con neve naturale?",
    "nel 2015--16", [("nel 1995--96", "98 natural vs. 12 artificial."),
                     ("nel 2005--06", "81 vs. 30."),
                     ("nel 2025--26", "It had already happened in 2015–16.")],
    "61 > 55.", "Data (1.A.2): compare the two columns row by row.",
    ["2015–16: 55 natural, 61 artificial."])
Q.q("1.C.1 Connect", r"Quale dato della tabella conferma che la neve naturale è «sempre più rara»?",
    "il calo da 98 a 38 giorni", [("l'aumento da 12 a 79 giorni", "That is artificial snow."),
                                  ("i 30 giorni del 2005--06", "That is artificial snow."),
                                  ("i 61 giorni del 2015--16", "That is artificial snow.")],
    "Natural column: 98 → 38.", "Connect (1.C.1).",
    ["98 → 81 → 55 → 38."])
Q.q("1.C.2 Conclusion", r"Che cosa si può concludere dall'articolo e dalla tabella insieme?",
    "Le stazioni dipendono sempre di più da una neve che consuma acqua ed energia.", [("Nevica più di trent'anni fa.", "The opposite."),
                                                                                       ("La neve artificiale non si usa più.", "It rose to 79 days."),
                                                                                       ("Il turismo estivo è vietato.", "No.")],
    "Dependence on artificial snow.", "Conclusions (1.C.2): combine the chart's trend with the article's cost.",
    ["79 days + acqua ed energia."])
Q.q("1.B.3 Point of view", r"Qual è la posizione del sindaco?",
    "La montagna deve adattarsi offrendo attività in tutte le stagioni.", [("Bisogna produrre più neve artificiale.", "He proposes another way."),
                                                                          ("Il turismo in montagna è finito.", "He is optimistic."),
                                                                          ("Lo sci deve essere vietato.", "Too extreme.")],
    "Adattarsi.", "Point of view (1.B.3).",
    ["La montagna non è solo lo sci … Se ci adattiamo…"])
Q.q("1.B.5 Word meaning", r"Nell'articolo, «puntano su» significa",
    "investono in, scommettono su", [("indicano con il dito", "Literal misreading."),
                                    ("rifiutano", "No."),
                                    ("vendono", "No.")],
    "puntare su = to bet on.", "Word meaning (1.B.5).",
    ["puntano su escursioni… → invest in."])

Q.sec("Listening: Instructional Guidance")
Q.src(r"Listening 2 \textperiodcentered\ Instructional Guidance (transcript) \textperiodcentered\ «Che cosa fare durante un terremoto», messaggio del comune", [
    r"(VOCE) Durante una scossa di terremoto, se sei in casa, non correre verso le scale e non usare l'ascensore. Riparati sotto un tavolo robusto o vicino a un muro portante, lontano da finestre e mobili alti.",
    r"(VOCE) Se sei all'aperto, allontanati da edifici, alberi e linee elettriche, e raggiungi uno spazio aperto.",
    r"(VOCE) Quando la scossa è finita, esci con calma, indossando le scarpe: per terra potrebbero esserci vetri rotti. Non usare il telefono se non per un'emergenza, per lasciare libere le linee.",
    r"(VOCE) E prima che succeda: in famiglia, decidete insieme un punto di incontro all'aperto. In un'emergenza, sapere dove ritrovarsi fa la differenza.",
], 5)
Q.q("1.A.1 Detail", r"Che cosa bisogna fare se si è in casa durante la scossa?",
    "ripararsi sotto un tavolo robusto o vicino a un muro portante", [("correre verso le scale", "The message says not to."),
                                                                      ("prendere l'ascensore", "Explicitly forbidden."),
                                                                      ("affacciarsi alla finestra", "Stay away from windows.")],
    "Riparati sotto un tavolo.", "Instructional Guidance: match each instruction to the situation.",
    ["Riparati sotto un tavolo robusto o vicino a un muro portante."])
Q.q("1.A.1 Detail", r"Perché bisogna uscire con le scarpe dopo la scossa?",
    "perché per terra potrebbero esserci vetri rotti", [("perché fa freddo", "Not stated."),
                                                        ("perché bisogna correre", "Esci con calma."),
                                                        ("perché lo chiede la polizia", "No.")],
    "Vetri rotti.", "Detail (1.A.1).",
    ["…indossando le scarpe: per terra potrebbero esserci vetri rotti."])
Q.q("1.B.2 Audience", r"A chi si rivolge il messaggio?",
    "a tutti i cittadini, in casa e all'aperto", [("solo ai vigili del fuoco", "No."),
                                                  ("solo ai bambini", "No."),
                                                  ("ai turisti stranieri", "No.")],
    "Everyone.", "Audience (1.B.2): tu-instructions for any situation.",
    ["se sei in casa / se sei all'aperto → tutti."])
Q.q("1.C.3 Inference", r"Perché non si dovrebbe usare il telefono dopo la scossa, salvo emergenze?",
    "per non intasare le linee necessarie ai soccorsi", [("perché il telefono potrebbe esplodere", "No."),
                                                         ("perché è vietato dalla legge", "Not stated."),
                                                         ("perché costa troppo", "No.")],
    "Keep lines free.", "Inference (1.C.3).",
    ["per lasciare libere le linee."])
Q.q("1.B.4 Organization", r"Come è organizzato il messaggio?",
    "segue l'ordine durante, dopo e prima della scossa", [("racconta la storia di un terremoto", "No narrative."),
                                                          ("confronta due città", "No."),
                                                          ("elenca le cause dei terremoti", "No.")],
    "During → after → before.", "Organization (1.B.4): Durante … Quando la scossa è finita … E prima che succeda.",
    ["time markers order the steps."])

Q.frq(kind="Argumentative Essay", head=r"Question 3 \textperiodcentered\ Argumentative Essay \textperiodcentered\ 10 points \textperiodcentered\ 55 minutes", mins=55,
      directions=[r"Scrivi un saggio argomentativo per un corso universitario. Leggi il tema e le fonti scritte; poi ascolta la fonte audio (qui come trascrizione). Scrivi un saggio che usi informazioni tratte da tutte e tre le fonti per sostenere la tua posizione. Cita le fonti con il numero, il titolo o l'autore."],
      sources=[dict(title=r"Fonte 1 \textperiodcentered\ Articolo \textperiodcentered\ «Castelmare mette il biglietto»", paras=[
          r"Dopo Venezia, che nel 2024 ha introdotto un contributo di accesso per i turisti giornalieri nei giorni di punta, anche la città d'arte di Castelmare ha sperimentato un biglietto di 5 euro per chi visita il centro storico senza pernottare.",
          r"Il primo bilancio è positivo per l'assessora al turismo, Marta Gallo: «Nei weekend la folla sul ponte principale si è ridotta e i soldi raccolti finanziano la pulizia delle strade.» Alcuni commercianti, però, lamentano un calo di clienti, e diversi visitatori parlano di «una città trasformata in un museo a pagamento»."]),
               dict(title=r"Fonte 2 \textperiodcentered\ Grafico \textperiodcentered\ Residenti e turisti giornalieri nel centro storico di Castelmare", paras=[
          r"Dati fittizi."],
                    table=(["Anno", "Residenti", "Turisti giornalieri in un giorno di punta"], [["1980", "62.000", "18.000"], ["2000", "48.000", "40.000"], ["2020", "33.000", "65.000"], ["2025", "30.000", "71.000"]])),
               dict(title=r"Fonte 3 \textperiodcentered\ Audio (trascrizione) \textperiodcentered\ «Una città non è un museo», Radio Viaggi", paras=[
          r"(GIORNALISTA) Ne parliamo con la sociologa del turismo Laura Bassi. Professoressa, il biglietto è la soluzione al sovraturismo?",
          r"(LAURA BASSI) È un segnale, ma da solo non basta. Una città si svuota soprattutto quando i residenti non riescono più a pagare l'affitto, perché le case diventano affitti brevi per turisti. Cinque euro non fermano chi ha già deciso di venire.",
          r"(GIORNALISTA) Che cosa propone?",
          r"(LAURA BASSI) Limitare gli affitti brevi, aiutare le famiglie e i negozi di quartiere a restare, e usare le prenotazioni per distribuire i visitatori nei giorni meno affollati. Il biglietto può aiutare, purché i soldi servano a chi in città ci vive."])],
      prompt=[r"Tema del saggio: \textbf{Le città d'arte dovrebbero far pagare un biglietto d'ingresso ai turisti giornalieri?}"],
      model=[r"Molte città d'arte italiane sono diventate vittime del proprio successo: troppi visitatori e sempre meno abitanti. Alcune hanno introdotto un biglietto d'ingresso per i turisti giornalieri. A mio parere, il biglietto è una misura utile, purché faccia parte di un piano più ampio a favore dei residenti.",
             r"Innanzitutto, il problema è reale e urgente. Secondo il grafico della fonte 2, nel centro storico di Castelmare i residenti sono passati da 62.000 nel 1980 a 30.000 nel 2025, mentre i turisti giornalieri in un giorno di punta sono saliti da 18.000 a 71.000. Questi dati indicano che oggi, nei giorni di punta, i visitatori sono più del doppio degli abitanti.",
             r"In secondo luogo, il biglietto dà risultati concreti. Come spiega l'assessora Marta Gallo nella fonte 1, nei weekend la folla sul ponte principale si è ridotta e i soldi raccolti finanziano la pulizia delle strade, un servizio di cui beneficiano anzitutto i residenti.",
             r"È vero che alcuni commercianti lamentano un calo di clienti e che certi visitatori parlano di «una città trasformata in un museo a pagamento» (fonte 1). Inoltre, la sociologa Laura Bassi, nella fonte 3, avverte che cinque euro non fermano chi ha già deciso di venire e che le città si svuotano soprattutto a causa degli affitti brevi. Tuttavia, la stessa Bassi ammette che il biglietto può aiutare, purché i soldi servano a chi in città ci vive.",
             r"In conclusione, le città d'arte dovrebbero far pagare un biglietto ai turisti giornalieri, ma non basta. Se i proventi venissero usati per limitare gli affitti brevi e sostenere le famiglie e i negozi di quartiere, le città potrebbero tornare a essere luoghi vivi e non solo musei."],
      rows=[("A Position", 1, "a clear, qualified position (yes, as part of a wider plan for residents)", "only lists both sides"),
            ("B Source use", 2, "all three sources used accurately and named; the chart's two columns kept straight", "two sources, or mixing up residents and visitors"),
            ("C Argumentation", 2, "claims explained with evidence; the opposing source answered", "summaries with no link to the claims"),
            ("D Organization", 2, "introduction, two claims, concession and rebuttal, conclusion", "one paragraph per source"),
            ("E Language control", 3, "varied structures: purché + congiuntivo, periodo ipotetico, relative clauses with cui", "basic structures; copied phrases")],
      tips=["The qualified position already answers the strongest objection.", "The opposing source (Bassi) is conceded and then shown to accept the fee under a condition.",
            "The chart is quoted with its labels (residenti vs. turisti giornalieri) and years.", "The conclusion's periodo ipotetico (se … venissero usati, potrebbero) rounds off the argument."],
      ask="Write your essay in Italian (about 300–350 words), then mark it against each row.", lines=22)

GUIDE, QSET = G, Q
