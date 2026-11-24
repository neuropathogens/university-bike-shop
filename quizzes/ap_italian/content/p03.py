from ap_wl.model import Doc

STEM = "03-art-creativity"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 3: Art and Creativity", r"Unit 3 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 3 asks how art expresses identity and values, and how traditions are preserved and reinvented. Its recommended contexts are artistic heritage, architecture, beauty and aesthetics, fashion and design, literature, and the visual and performing arts. Music is the lens of the 2026--27 course project, so this guide gives it the most space: from opera and the town band to Neapolitan song, the cantautori, Sanremo, the pizzica and Sardinian canto a tenore, and what each expresses. It also covers architecture from the Colosseum to Brunelleschi, literature, cinema and design, the language for describing and evaluating art, and a Project Presentation kit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 11+ \qquad Three factors for my project: \blank[10em]",
        short="Unit 3", sub="Art and Creativity")

G.sec("Music in the Italian-speaking world")
G.tex(r"""
\begin{vocab}
l'opera lirica / il melodramma & opera & \\
il loggione & top gallery of an opera house & cheap seats, passionate fans \\
la banda & town band & plays at processions and patron-saint festivals \\
il cantautore / la cantautrice & singer-songwriter & \\
la pizzica / la tarantella & fast folk dances of the South & \\
il canto a tenore & Sardinian four-voice singing & UNESCO intangible heritage \\
la liuteria & violin making & Cremona; UNESCO (2012) \\
il testo / il ritornello & lyrics / chorus & \\
\end{vocab}

\begin{compare}{Tradition}{Where and when}{What it often expresses}
Opera (Verdi, Puccini, Rossini) & from about 1600; La Scala in Milan, the Arena di Verona & national pride; the practice of opera singing in Italy is UNESCO heritage (2023) \\
Neapolitan song & Naples, from the 19th century & love, nostalgia, pride in the city's language \\
Cantautori (De André, Dalla, Battisti) & 1960s--80s & poetry, social and political critique \\
Festival di Sanremo & since 1951 & a national ritual watched by millions every February \\
Pizzica & Salento (Apulia); revived by the Notte della Taranta & community, healing, rediscovered roots \\
\end{compare}

\begin{keyidea}[Products, practices, perspectives in music]
\textbf{Product}: an aria, a violin from Cremona, a genre. \textbf{Practice}: the band playing at the procession; booing or cheering from the loggione; dancing the pizzica in the square. \textbf{Perspective}: the value behind it (community, devotion, pride, a shared national story). The presentation's culture row asks for the link: practice + \emph{il che dimostra} / \emph{perché} + perspective.
\end{keyidea}
""")
G.q("1 Musica", r"Perché la liuteria di Cremona è riconosciuta dall'UNESCO?",
    "perché è un'arte tradizionale di costruzione di violini tramandata da secoli", [("perché Cremona produce automobili famose", "No."),
                                                                                     ("perché a Cremona è nata la pizzica", "The pizzica is from Salento."),
                                                                                     ("perché Cremona ha il teatro d'opera più grande", "That is not the reason.")],
    "Cremona = violin making.", "Traditional violin craftsmanship in Cremona (Stradivari's city) is UNESCO intangible heritage (2012).",
    ["liuteria → violini → Cremona."])
G.q("1 Musica", r"Which sentence links a musical practice to a cultural perspective?",
    "In molti paesi la banda accompagna la processione del santo patrono, il che dimostra quanto contino la fede e la comunità.",
    [("La banda ha clarinetti, trombe e tamburi.", "A product described with no perspective."),
     ("Il Festival di Sanremo è nato nel 1951.", "A date, no perspective."),
     ("A me piace l'opera.", "A personal preference, not a cultural example.")],
    "Practice + il che dimostra + perspective.", "The top culture score needs a specific practice or product tied to the value behind it.",
    ["Practice: the band at the procession.", "Perspective: faith and community."])
G.q("1 Musica", r"Che cos'è il Festival di Sanremo?",
    "una gara di canzoni seguita ogni anno da milioni di italiani", [("un festival di opera lirica all'aperto", "That would be the Arena di Verona."),
                                                                     ("una scuola di liuteria", "No."),
                                                                     ("una danza popolare del Sud", "That is the pizzica or tarantella.")],
    "Sanremo = song contest.", "Since 1951 the Sanremo festival has been a national television ritual.",
    ["Sanremo → canzoni, gara, televisione."])

G.sec("Heritage and architecture")
G.tex(r"""
\begin{vocab}
il patrimonio & heritage & \emph{patrimonio dell'umanità} = World Heritage \\
il capolavoro & masterpiece & \\
il duomo / la cupola & cathedral / dome & \\
il centro storico & historic center & \\
restaurare / il restauro & to restore / restoration & \\
il borgo medievale & medieval village & \\
\end{vocab}

\begin{compare}{Work or place}{What it is}{Why it matters}
Colosseo & Roman amphitheater, inaugurated in 80 CE & a symbol of Rome and of engineering \\
Cupola del Duomo di Firenze & Brunelleschi's dome, completed 1436 & built without a full wooden frame; the Renaissance begins \\
Ville palladiane & villas by Andrea Palladio in the Veneto, 16th century & classical harmony; copied worldwide \\
Renzo Piano & architect of the Centre Pompidou and of Genoa's new bridge (2020) & tradition and innovation together \\
\end{compare}

Italy has one of the highest numbers of World Heritage sites of any country. Restoring them is a whole profession: Italian restorers are known worldwide, and the perspective is that heritage belongs to future generations as much as to the present.
""")
G.q("2 Patrimonio", r"Perché la cupola di Brunelleschi è considerata un capolavoro?",
    "perché fu costruita senza un'impalcatura di legno completa, con una tecnica innovativa", [("perché è la più antica d'Italia", "The Pantheon's dome is much older."),
                                                                                             ("perché fu costruita in un anno", "It took about 16 years."),
                                                                                             ("perché è fatta d'oro", "No.")],
    "Engineering innovation.", "Brunelleschi's dome (completed 1436) used an innovative self-supporting technique.",
    ["senza impalcatura completa → innovazione."])
G.q("2 Patrimonio", r"Il Colosseo fu inaugurato nell'anno",
    "80 d.C.", [("1436", "That is Brunelleschi's dome."),
                ("1861", "That is Italian unification."),
                ("1951", "That is the first Sanremo festival.")],
    "80 CE.", "The Flavian Amphitheater opened under Emperor Titus in 80 CE.",
    ["Colosseo → 80 d.C."])

G.sec("Literature, cinema and design")
G.tex(r"""
\begin{compare}{Author, artist or work}{Known for}{Theme}
Dante Alighieri & \emph{Divina Commedia} (early 14th c.) & a journey through Hell, Purgatory and Paradise \\
Carlo Collodi & \emph{Le avventure di Pinocchio} (1883) & growing up; honesty \\
Italo Calvino & \emph{Le città invisibili} (1972) & imagination, cities as ideas \\
Elena Ferrante & \emph{L'amica geniale} (2011) & friendship, Naples, women's lives \\
Michelangelo & the \emph{David} (1504); the Sistine Chapel ceiling (1508--12) & the human body; ambition \\
Neorealismo & \emph{Ladri di biciclette} (De Sica, 1948) & poverty and dignity after the war \\
Federico Fellini & \emph{La dolce vita} (1960) & glamour and emptiness \\
Italian design & the Vespa (1946), the Fiat 500 (1957) & beauty in everyday objects \\
\end{compare}

\textbf{Neorealism} filmed real streets with non-professional actors to show ordinary people's lives after the war. The perspective: cinema should bear witness to reality and give dignity to the poor.
""")
G.q("3 Letteratura", r"Che cosa caratterizza il cinema neorealista?",
    "riprese nelle strade vere e attori spesso non professionisti", [("effetti speciali e fantascienza", "The opposite."),
                                                                     ("storie di re e regine", "No."),
                                                                     ("film musicali con grandi orchestre", "No.")],
    "Real streets, real people.", "Neorealism (Rossellini, De Sica) showed postwar life with non-professional actors.",
    ["neorealismo → realtà quotidiana."])
G.q("3 Letteratura", r"Which perspective do the Vespa and the Fiat 500 best represent?",
    "Everyday objects can be beautiful as well as affordable.", [("Design should be only for the rich.", "Both were affordable mass products."),
                                                                ("Function does not matter.", "Both were practical."),
                                                                ("Only art in museums has value.", "The opposite.")],
    "Design for everyday life.", "Postwar Italian design made practical, affordable objects with style.",
    ["Vespa, 500 → bellezza quotidiana."])

G.sec("Describing and evaluating art")
G.tex(r"""
\begin{compare}{Purpose}{Language}{Example}
Describe & rappresenta, raffigura, in primo piano, sullo sfondo & In primo piano si vede una donna con un ventaglio. \\
Interpret & simboleggia, esprime, ricorda & Il rosso simboleggia la passione. \\
Evaluate & mi colpisce che (+ congiuntivo); trovo affascinante che & Mi colpisce che l'artista usi materiali poveri. \\
Concede & sebbene, benché (+ congiuntivo); è vero che\ldots ma & Sebbene alcuni la trovino kitsch, la canzone è amatissima. \\
Influence & ispirarsi a, essere influenzato da & Il cantautore si è ispirato alla musica popolare. \\
\end{compare}

\begin{trap}
Evaluative expressions with \emph{che} take the congiuntivo: \emph{mi colpisce che sia}, \emph{trovo strano che abbia}. With a past main verb, use the congiuntivo imperfetto: \emph{mi ha colpito che fosse}.
\end{trap}
""")
G.q("4 Descrivere", r"Scegli la frase corretta.",
    "Sebbene alcuni critici trovino Sanremo superficiale, milioni di persone lo guardano.", [("Sebbene alcuni critici trovano Sanremo superficiale, milioni di persone lo guardano.", "Sebbene requires the congiuntivo."),
                                                                                         ("Sebbene alcuni critici trovino Sanremo superficiale, milioni di persone lo guardino.", "The main clause takes the indicative."),
                                                                                         ("Sebbene alcuni critici trovare Sanremo superficiale, milioni di persone lo guardano.", "A conjugated verb is needed.")],
    "sebbene + congiuntivo; main clause indicative.", "Only the concessive clause takes the congiuntivo.",
    ["Sebbene … trovino, … guardano."])
G.q("4 Descrivere", r"Scegli la forma corretta: Il cantautore \blank\ alle canzoni popolari della sua regione.",
    "si è ispirato", [("ha ispirato", "Without si, the meaning is that he inspired the songs."),
                      ("si è ispirata", "Il cantautore is masculine."),
                      ("si ha ispirato", "Reflexive verbs take essere.")],
    "ispirarsi a: reflexive, with essere.", "Ispirarsi a qualcosa = to be inspired by; reflexive verbs form compound tenses with essere.",
    ["si è ispirato a."])

G.sec("Task kit: the Project Presentation")
G.tex(r"""
You have 3 minutes to prepare (with your PPR) and 3 minutes to present, about 350--400 words. The prompt asks what you learned in your research; the rubric rewards \textbf{three or more factors, each explained with details}, and a cultural perspective linked to a product or practice.

\begin{terms}
0:00--0:25 & introduction: the question, your focus, the three factors \\
0:25--2:30 & three factors, about 40 seconds each: fact or example from research + why it matters (perspective) \\
2:30--3:00 & conclusion: what the factors show together; a comparison or reflection \\
\end{terms}

\begin{compare}{Move}{Phrases}{}
Open & Oggi parlerò di\ldots; Mi sono concentrato/a su tre aspetti: \ldots & \\
Move on & Innanzitutto / In secondo luogo / Infine & \\
Evidence & Dalla mia ricerca è emerso che\ldots; Per esempio\ldots & \\
Perspective & Questo riflette\ldots; il che dimostra quanto sia importante\ldots & \\
Close & In conclusione\ldots; Ho imparato che\ldots & \\
\end{compare}

\begin{trap}
Three factors named with no detail earn only 1 point for task; so does one factor explained in depth. Budget time so the third factor gets real detail.
\end{trap}
""")
G.q("5 Presentazione", r"A presentation explains three factors, each with a specific example from research, but never links them to what people value. Which row is it most likely to lose points in?",
    "Cultural understanding", [("Task execution", "Three factors with relevant details earn full task credit."),
                               ("Delivery", "Delivery is about pronunciation and pace."),
                               ("Organization", "Nothing suggests poor organization.")],
    "No perspective link → culture row.", "Row B's top score needs a relationship between a perspective and a product or practice.",
    ["Factors and details → task OK.", "No perspective → culture 1 point."])
G.q("5 Presentazione", r"About how many words fit in the 3-minute presentation at a natural pace?",
    "350 to 400", [("100 to 150", "That would leave long silences."),
                   ("800 to 900", "That would require rushing, which hurts delivery."),
                   ("50", "That is one short paragraph.")],
    "3 min ≈ 350–400 words.", "At about two words per second, three minutes holds 350–400 words.",
    ["Plan about 120 words per factor."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 3: Art and Creativity: Question Set", r"Unit 3 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Instructional Guidance and an Interview for listening, an Article and Chart and a Promotional Material for reading) on dancing the pizzica, young audiences at the opera, a folk music festival and a young violin maker, followed by a practice Project Presentation on music, the 2026--27 project lens, with the 11-point scoring guide and a model script. The presentation prompt is a practice prompt written for this set, not the official 2027 project prompt. As on the exam, questions and choices are in Italian; listening sources are printed as transcripts. All sources and data are original and fictional. Allow about 25 minutes for the multiple choice and 6 minutes to prepare and deliver the presentation.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Presentation: \blank\ / 11 \qquad Target: 15+ MCQ and 8+ presentation",
        short="Unit 3", sub="Art and Creativity")

Q.sec("Listening: Instructional Guidance")
Q.src(r"Listening 1 \textperiodcentered\ Instructional Guidance (transcript) \textperiodcentered\ «Impara la pizzica in cinque minuti», video-lezione", [
    r"(INSEGNANTE) Ciao a tutti! Oggi impariamo il passo base della pizzica, la danza del Salento. Prima di tutto togliete le scarpe col tacco: si balla meglio scalzi o con scarpe basse.",
    r"(INSEGNANTE) Il ritmo lo dà il tamburello. Ascoltate: uno-due-tre, uno-due-tre. Sul primo colpo saltellate leggermente sul piede destro, poi sul sinistro, sempre restando sulle punte.",
    r"(INSEGNANTE) Adesso aggiungete le braccia: alzatele morbide sopra la testa, come se teneste un fazzoletto. Le ragazze, tradizionalmente, lo fanno girare per invitare il compagno.",
    r"(INSEGNANTE) Un'ultima cosa: la pizzica non si balla da soli davanti allo specchio. Si balla in cerchio, guardandosi negli occhi. È una conversazione senza parole.",
], 5)
Q.q("1.A.1 Detail", r"Che cosa bisogna fare prima di cominciare a ballare?",
    "togliere le scarpe col tacco", [("comprare un tamburello", "Not required."),
                                    ("riscaldarsi correndo", "Not mentioned."),
                                    ("mettersi davanti allo specchio", "She says the opposite at the end.")],
    "Prima di tutto…", "Instructional Guidance: prima di tutto marks the first step.",
    ["Prima di tutto togliete le scarpe col tacco."])
Q.q("1.A.1 Detail", r"Quale strumento dà il ritmo della pizzica?",
    "il tamburello", [("la chitarra", "Not mentioned."),
                      ("il violino", "Not mentioned."),
                      ("la fisarmonica", "Not mentioned.")],
    "tamburello.", "Detail (1.A.1).",
    ["Il ritmo lo dà il tamburello."])
Q.q("1.B.4 Organization", r"Come è organizzata la video-lezione?",
    "in passaggi successivi, dai piedi alle braccia fino a un consiglio finale", [("come un confronto tra due danze", "No comparison."),
                                                                                  ("come la storia della pizzica dal Medioevo", "No history."),
                                                                                  ("come un'intervista", "One speaker.")],
    "Prima di tutto … Adesso … Un'ultima cosa.", "Organization (1.B.4): step markers.",
    ["shoes → feet → arms → final advice."])
Q.q("1.B.5 Word meaning", r"Nella lezione, «scalzi» significa",
    "senza scarpe", [("con scarpe speciali", "No."),
                     ("con i calzini colorati", "No."),
                     ("in piedi su una sedia", "No.")],
    "scalzo = barefoot.", "Word meaning (1.B.5): contrast with scarpe basse.",
    ["si balla meglio scalzi o con scarpe basse."])
Q.q("1.C.3 Inference", r"Che cosa intende l'insegnante con «una conversazione senza parole»?",
    "che la pizzica è un dialogo tra i ballerini fatto di gesti e sguardi", [("che bisogna ballare in silenzio assoluto", "Literal misreading."),
                                                                            ("che la musica non ha testo", "Not the point."),
                                                                            ("che i ballerini non si conoscono", "No.")],
    "Dance as dialogue.", "Inference (1.C.3): in cerchio, guardandosi negli occhi.",
    ["cerchio + sguardi → conversazione."])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 1 \textperiodcentered\ Article and Chart \textperiodcentered\ «I giovani tornano all'opera?», quotidiano Il Ponte", [
    r"Tre anni fa il Teatro Comunale di Valmonte ha lanciato «Under 30 all'opera»: biglietti a 10 euro per chi ha meno di trent'anni, prove generali aperte agli studenti e un'app con i sottotitoli in tempo reale. I risultati sono sorprendenti.",
    r"«La quota di spettatori giovani è più che raddoppiata», spiega la direttrice artistica Silvia Marchi. «Molti ragazzi pensavano che l'opera fosse noiosa o elitaria. Quando scoprono che parla di amore, potere e tradimento, cambiano idea.»",
    r"Non tutti gli abbonati storici sono contenti: alcuni lamentano telefoni accesi in sala. Ma per Marchi il rischio più grande sarebbe un teatro pieno solo di capelli grigi.",
], 5, table=(["Fascia d'età degli spettatori", "Prima del progetto", "Oggi"],
             [["Under 30", "8~\\%", "19~\\%"], ["30--59 anni", "47~\\%", "45~\\%"], ["60 anni e oltre", "45~\\%", "36~\\%"]]),
      note="Dati fittizi.")
Q.q("1.A.2 Data", r"Secondo la tabella, quale fascia d'età rappresenta oggi la quota più grande del pubblico?",
    "30--59 anni", [("Under 30", "19%."),
                    ("60 anni e oltre", "36%."),
                    ("Tutte uguali", "They differ.")],
    "45%.", "Data (1.A.2): read the Oggi column.",
    ["Oggi: 19 / 45 / 36."])
Q.q("1.C.1 Connect", r"Quale dato della tabella conferma che la quota di giovani «è più che raddoppiata»?",
    "il passaggio dall'8~\\% al 19~\\% degli under 30", [("il passaggio dal 47~\\% al 45~\\%", "That is the 30–59 group."),
                                                         ("il 36~\\% degli over 60", "That fell."),
                                                         ("il 45~\\% degli over 60 prima del progetto", "That is the older audience.")],
    "8 → 19.", "Connect (1.C.1): 8 × 2 = 16 < 19.",
    ["Under 30: 8 % → 19 %."])
Q.q("1.B.3 Point of view", r"Secondo Silvia Marchi, perché molti giovani cambiano idea sull'opera?",
    "perché scoprono che parla di temi vicini alla loro vita", [("perché i biglietti sono gratuiti", "They cost 10 euros."),
                                                               ("perché possono usare il telefono", "Not her reason."),
                                                               ("perché le opere sono più corte", "Not mentioned.")],
    "amore, potere, tradimento.", "Point of view (1.B.3).",
    ["Quando scoprono che parla di amore, potere e tradimento, cambiano idea."])
Q.q("1.B.5 Word meaning", r"Nell'articolo, «un teatro pieno solo di capelli grigi» significa",
    "un pubblico composto solo da persone anziane", [("un teatro con decorazioni grigie", "Figurative."),
                                                    ("un pubblico di parrucchieri", "No."),
                                                    ("un teatro vecchio e sporco", "No.")],
    "Metonymy: grey hair = old people.", "Word meaning (1.B.5).",
    ["capelli grigi → anziani."])
Q.q("1.C.2 Conclusion", r"Che cosa si può concludere dall'articolo?",
    "Il progetto ha attirato giovani, anche se ha creato qualche tensione con il pubblico abituale.", [("Il progetto è stato un fallimento.", "Young audiences more than doubled."),
                                                                                                         ("Gli anziani non vanno più all'opera.", "They are still 36%."),
                                                                                                         ("Tutti gli abbonati sono entusiasti.", "Some complain.")],
    "Success + tension.", "Conclusions (1.C.2): both sides of the article.",
    ["raddoppiata + alcuni lamentano."])

Q.sec("Reading: Promotional Material")
Q.src(r"Reading 2 \textperiodcentered\ Promotional Material \textperiodcentered\ Locandina di un festival", [
    r"\textbf{NOTE IN VALLE 2027 \textperiodcentered\ Festival di musica popolare \textperiodcentered\ Valle del Sorbo}",
    r"Tre sere, tre piazze, trenta gruppi: dalle zampogne dell'Appennino alla pizzica elettronica, dai cori di montagna al rap in dialetto. La tradizione non sta ferma: si balla!",
    r"\textbf{Novità:} laboratori gratuiti di tamburello, organetto e canto popolare con i musicisti del festival. Iscrizione obbligatoria al punto informazioni (posti limitati: chi tardi arriva male alloggia).",
    r"\textbf{Biglietti:} abbonamento tre sere 45 euro; under 12 gratis; studenti con tessera: metà prezzo.",
    r"8--10 luglio \textperiodcentered\ Navette gratuite dalla stazione ogni 30 minuti \textperiodcentered\ Vietato portare bottiglie di vetro.",
], 5)
Q.q("1.B.1 Purpose", r"Qual è lo scopo principale della locandina?",
    "invitare il pubblico a un festival di musica tradizionale e moderna", [("annunciare l'apertura di una scuola di musica", "Workshops are one feature."),
                                                                            ("vendere strumenti musicali", "Only tickets are sold."),
                                                                            ("presentare una gara di ballo", "No contest.")],
    "Festival poster → invite.", "Purpose (1.B.1): title, dates, places and prices.",
    ["Promotional Material → invitation."])
Q.q("1.A.1 Detail", r"Come si partecipa ai laboratori?",
    "iscrivendosi al punto informazioni", [("comprando un biglietto speciale online", "They are free; registration is at the info point."),
                                          ("portando il proprio strumento", "Not stated."),
                                          ("inviando un video", "Not stated.")],
    "Iscrizione al punto informazioni.", "Detail (1.A.1).",
    ["Iscrizione obbligatoria al punto informazioni."])
Q.q("1.C.2 Conclusion", r"Uno studente con tessera compra l'abbonamento per tre sere. Quanto paga?",
    "22,50 euro", [("45 euro", "Students pay half."),
                   ("niente", "Only under-12s are free."),
                   ("30 euro", "Not half of 45.")],
    "45 ÷ 2.", "Apply the details: the pass costs 45 euros, half price for students.",
    ["45 × 0,5 = 22,50."])
Q.q("1.B.5 Word meaning", r"Che cosa significa qui «chi tardi arriva male alloggia»?",
    "chi si iscrive tardi rischia di non trovare posto", [("chi arriva tardi deve dormire in albergo", "Literal misreading of a proverb."),
                                                         ("i laboratori finiscono tardi", "No."),
                                                         ("le navette sono lente", "No.")],
    "Proverb: first come, first served.", "Word meaning (1.B.5): explained by posti limitati.",
    ["posti limitati + proverbio → iscriversi presto."])
Q.q("1.A.1 Detail", r"Come si può arrivare al festival senza auto?",
    "con le navette gratuite dalla stazione", [("con il treno fino alla piazza", "Shuttles run from the station."),
                                               ("solo a piedi", "No."),
                                               ("con un autobus a pagamento", "The shuttles are free.")],
    "Navette gratuite.", "Detail (1.A.1).",
    ["Navette gratuite dalla stazione ogni 30 minuti."])

Q.sec("Listening: Interview")
Q.src(r"Listening 2 \textperiodcentered\ Interview (transcript) \textperiodcentered\ Una giovane liutaia di Cremona", [
    r"(GIORNALISTA) Marta, lei ha 27 anni e costruisce violini a Cremona. Come ha cominciato?",
    r"(MARTA) Per caso. Suonavo il violino al liceo e un giorno il mio si è rotto. Il liutaio che l'ha riparato mi ha fatto vedere la bottega: il profumo del legno, gli attrezzi antichi. Ho deciso lì.",
    r"(GIORNALISTA) Oggi alcuni violini si costruiscono con l'aiuto del computer. Lei cosa ne pensa?",
    r"(MARTA) Non sono contraria alla tecnologia: uso anche la scansione 3D per studiare gli strumenti antichi. Ma il suono nasce dalle mani. Ogni pezzo di legno è diverso, e solo l'orecchio e l'esperienza ti dicono quando fermarti.",
    r"(GIORNALISTA) Che cosa la rende più orgogliosa?",
    r"(MARTA) Sapere che un mio violino suonerà ancora tra duecento anni, quando io non ci sarò più. È come scrivere una lettera al futuro.",
], 5)
Q.q("1.A.1 Detail", r"Come ha deciso Marta di diventare liutaia?",
    "dopo aver visitato la bottega del liutaio che le aveva riparato il violino", [("dopo un corso universitario di ingegneria", "Not mentioned."),
                                                                                    ("perché i suoi genitori erano liutai", "Not stated."),
                                                                                    ("dopo un concerto alla Scala", "Not mentioned.")],
    "Per caso: a broken violin.", "Detail (1.A.1).",
    ["Il liutaio che l'ha riparato mi ha fatto vedere la bottega…"])
Q.q("1.B.3 Attitude", r"Qual è l'atteggiamento di Marta verso la tecnologia?",
    "La usa come aiuto, ma ritiene essenziale il lavoro manuale.", [("La rifiuta completamente.", "She uses 3D scanning."),
                                                                   ("Pensa che sostituirà i liutai.", "She says the sound comes from the hands."),
                                                                   ("Non la conosce.", "She uses it.")],
    "Non sono contraria … Ma…", "Attitude (1.B.3): balanced.",
    ["uso anche la scansione 3D … Ma il suono nasce dalle mani."])
Q.q("1.C.3 Inference", r"Che cosa significa «il suono nasce dalle mani»?",
    "che la qualità del violino dipende dall'abilità artigianale", [("che si suona il violino con le mani", "Literal misreading."),
                                                                    ("che le mani fanno rumore", "No."),
                                                                    ("che i computer suonano meglio", "The opposite.")],
    "Craft skill.", "Inference (1.C.3): figurative.",
    ["mani → esperienza artigianale."])
Q.q("1.B.5 Word meaning", r"Nell'intervista, «la bottega» è",
    "il laboratorio dove lavora l'artigiano", [("un negozio di vestiti", "No."),
                                              ("una bottiglia", "False friend of sound."),
                                              ("una sala da concerto", "No.")],
    "bottega = workshop.", "Word meaning (1.B.5): wood, tools → workshop.",
    ["profumo del legno, attrezzi antichi → bottega."])
Q.q("1.C.2 Conclusion", r"Che cosa rivela il paragone con «una lettera al futuro»?",
    "che Marta vede il suo lavoro come un'eredità per le generazioni future", [("che Marta scrive lettere ai clienti", "Figurative."),
                                                                              ("che i violini durano poco", "The opposite."),
                                                                              ("che Marta vuole smettere presto", "No.")],
    "Legacy.", "Conclusions (1.C.2): duecento anni → legacy.",
    ["suonerà ancora tra duecento anni → eredità."])

Q.frq(kind="Project Presentation", head=r"Question 1 \textperiodcentered\ Project Presentation (practice prompt) \textperiodcentered\ 11 points \textperiodcentered\ 3 + 3 minutes", mins=6,
      directions=[r"Imagine that your project examined how music reflects the values of an Italian-speaking community. You have 3 minutes to prepare, using your notes, and 3 minutes to present. Explain at least three factors, with specific examples from your research, and show how cultural perspectives relate to cultural products or practices."],
      prompt=[r"Prompt: \textbf{In che modo la musica riflette i valori di una comunità italofona che ha studiato?}",
              r"Practice focus (example): opera in Italy."],
      model=[r"Oggi parlerò dell'opera lirica in Italia e di che cosa ci dice sui valori degli italiani. Mi sono concentrata su tre aspetti: la prima della Scala a Milano, il pubblico del loggione e il riconoscimento dell'UNESCO.",
             r"Innanzitutto, la prima della Scala. Dalla mia ricerca è emerso che la stagione si apre ogni anno il 7 dicembre, giorno di Sant'Ambrogio, il patrono di Milano. È un evento trasmesso in televisione, con politici e artisti in sala. Questo riflette quanto l'opera sia ancora un rito civico: la città celebra il suo santo e la sua cultura nello stesso giorno.",
             r"In secondo luogo, il loggione. È la galleria più alta, con i biglietti più economici. Gli appassionati che siedono lassù applaudono con entusiasmo, ma fischiano anche i cantanti che sbagliano. Questa pratica dimostra che per molti italiani l'opera non è un museo, ma una passione popolare, di cui tutti si sentono un po' giudici.",
             r"Infine, nel 2023 l'UNESCO ha riconosciuto la pratica del canto lirico in Italia come patrimonio culturale immateriale dell'umanità. Ho scoperto che questa tecnica si tramanda da maestro ad allievo, spesso in piccole scuole e conservatori. Il riconoscimento dimostra che gli italiani considerano il canto lirico un sapere da proteggere e trasmettere alle nuove generazioni.",
             r"In conclusione, l'opera in Italia unisce fede e città, passione popolare e tradizione da custodire. Ho imparato che, quando un italiano canticchia un'aria di Verdi, non canta solo una melodia: racconta un pezzo della propria identità."],
      rows=[("A Task", 2, "three or more factors, each explained with relevant details from research", "three factors named with no detail, or only one or two factors"),
            ("B Culture", 2, "specific examples linking perspectives (civic ritual, popular passion, heritage) to products or practices", "examples with no perspective, or a vague one (1 point)"),
            ("C Organization", 2, "clear introduction, ordered factors, conclusion; varied transitions", "a list of facts with no progression"),
            ("D Language", 3, "wide vocabulary, varied structures (congiuntivo, relative clauses, si passivante)", "a limited set of basic structures"),
            ("E Delivery", 2, "clear pronunciation, natural pace and intonation, little hesitation", "hesitant, monotone or rushed speech")],
      tips=["The introduction names the three factors, so the listener can follow.", "Each factor has a specific example (December 7, the loggione's whistles, UNESCO 2023) and a perspective (questo riflette, questa pratica dimostra).",
            "The conclusion pulls the factors together and adds a reflection.", "About 360 words: three minutes at a natural pace."],
      ask="Prepare for 3 minutes using keywords only, then present aloud for 3 minutes (record yourself if you can). Then mark your presentation.", lines=14)

GUIDE, QSET = G, Q
