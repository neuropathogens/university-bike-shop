from ap_wl.model import Doc

STEM = "02-language-culture"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 2: Language and Culture", r"Unit 2 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 2 asks how language and customs express identity, and how Italian lives alongside dialects and in communities around the world. Its recommended contexts are customs and celebrations, linguistics, and Italian in the world. This guide gives the vocabulary of celebrations and of language itself, the traditions most often tested (Carnevale, the Befana, Ferragosto, the Palio di Siena, national holidays, the presepe), where Italian is spoken, how a language of writers became the language of a nation, dialects and regional languages, false friends and loanwords, the si impersonale and the passive, and a Project Q\&A kit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad False friends I can explain: \blank[10em]",
        short="Unit 2", sub="Language and Culture")

G.sec("Celebrations and traditions")
G.tex(r"""
\begin{vocab}
il Carnevale & Carnival & masks in Venice, parade floats in Viareggio \\
la Befana & the Epiphany witch & brings sweets (or coal) on the night of January 5 \\
Ferragosto & August 15 & the height of summer holidays \\
il Palio di Siena & horse race in the main square & July 2 and August 16 \\
la Festa della Repubblica & Republic Day, June 2 & the 1946 referendum \\
il 25 aprile & Liberation Day & end of Fascism and occupation (1945) \\
il presepe & nativity scene & Naples' Via San Gregorio Armeno \\
l'onomastico & name day & the feast of your namesake saint \\
\end{vocab}

\begin{compare}{Tradition}{Practice}{Perspective often cited}
Palio di Siena & each of the 17 contrade races for the banner; members are baptized into their contrada & lifelong belonging to a neighborhood \\
La Befana & children hang stockings; a piece of sugar ``coal'' for the naughty & family storytelling; teaching good behavior with humor \\
2 giugno & parades and the Frecce Tricolori over Rome & pride in the Republic and in voting: in 1946 women voted nationally for the first time \\
\end{compare}
""")
G.q("1 Feste", r"Chi porta dolci ai bambini nella notte tra il 5 e il 6 gennaio?",
    "la Befana", [("Babbo Natale", "He comes at Christmas."),
                  ("San Martino", "His day is November 11."),
                  ("la contrada", "A contrada is a neighborhood of Siena.")],
    "Befana → Epiphany.", "The Befana fills stockings on the eve of the Epiphany; naughty children get sugar coal.",
    ["5–6 gennaio → Befana."])
G.q("1 Feste", r"In Siena, children are baptized into their contrada and stay members for life. Which perspective does this practice reflect?",
    "Belonging to one's neighborhood is a deep, lifelong identity.", [("The Palio is only a tourist show.", "Lifelong membership shows it is much more."),
                                                                     ("Neighborhoods should compete in business.", "No."),
                                                                     ("Horses are sacred animals.", "Not the perspective.")],
    "Contrada ↔ belonging.", "A practice (baptism into a contrada) linked to a perspective (local identity and loyalty).",
    ["membership for life → identity."])
G.q("1 Feste", r"Che cosa si festeggia in Italia il 2 giugno?",
    "la nascita della Repubblica con il referendum del 1946", [("la fine dell'estate", "No."),
                                                              ("l'unità d'Italia del 1861", "That is March 17."),
                                                              ("la Liberazione", "That is April 25.")],
    "2 giugno → Repubblica.", "On June 2–3, 1946, Italians voted for a republic over the monarchy.",
    ["1946 referendum → Festa della Repubblica."])

G.sec("Italian in the world")
G.tex(r"""
\begin{compare}{Place}{Status of Italian}{Note}
Italy, San Marino & official language & \\
Vatican City & official and working language & \\
Switzerland & one of four national languages & Ticino and parts of Graubünden (Grigioni) \\
Slovenia and Croatia (Istria) & co-official in some municipalities & historic Italian communities \\
Argentina, Brazil, United States, Canada, Australia & heritage language & millions of descendants of emigrants \\
\end{compare}

\textbf{Emigration.} Between the 1870s and the 1970s millions of Italians emigrated to the Americas, Australia and northern Europe. Their languages and dialects shaped local speech: Buenos Aires Spanish has a strongly Italian intonation and words like \emph{laburar} (from \emph{lavorare}). Today about 6 million Italian citizens live abroad.

\textbf{Italian as a language of culture.} Music still uses Italian: \emph{piano, forte, allegro, adagio, soprano, opera}. So do food and design words worldwide.
""")
G.q("2 Italiano nel mondo", r"In quale paese l'italiano è una delle lingue nazionali, accanto al tedesco, al francese e al romancio?",
    "in Svizzera", [("in Argentina", "There Italian is a heritage language, not an official one."),
                    ("in Austria", "No."),
                    ("in Australia", "A heritage language.")],
    "Switzerland: four national languages.", "Italian is a national language of Switzerland, spoken mainly in Ticino.",
    ["Ticino → Svizzera."])
G.q("2 Italiano nel mondo", r"Why are terms like allegro, adagio and soprano Italian in English?",
    "Italian became the international language of music during the Baroque and the birth of opera.", [("Because English has no words for music.", "It borrowed them."),
                                                                                                     ("Because they were invented in the 20th century.", "Much older."),
                                                                                                     ("Because they came from Latin through French only.", "They came directly from Italian.")],
    "Italian = language of music.", "Opera was born in Italy around 1600, and Italian musical terms spread across Europe.",
    ["opera + Baroque → Italian terms."])

G.sec("Dialects and the history of Italian")
G.tex(r"""
\begin{vocab}
il dialetto & dialect, often a separate Romance language & napoletano, siciliano, veneto, milanese \\
la lingua minoritaria & minority language & sardo, friulano, ladino, recognized by law (1999) \\
l'Accademia della Crusca & Florence academy for the Italian language & founded 1583 \\
la lingua standard & standard language & based on literary Florentine \\
\end{vocab}

\textbf{From writers to a nation.} Standard Italian grew from the Florentine of Dante, Petrarch and Boccaccio. Alessandro Manzoni revised \emph{I promessi sposi} (final edition 1840--42) into Florentine, to ``rinse his clothes in the Arno''. At unification in 1861 only a small minority of Italians spoke Italian in daily life; school, military service, migration within Italy and, above all, television spread it. From 1960 the RAI program \emph{Non è mai troppo tardi} taught adults to read and write.

\begin{keyidea}[Dialects are not ``bad Italian'']
Most Italian dialects developed directly from Latin, side by side with Florentine: they are sister languages, not corruptions of standard Italian. Many Italians switch between dialect at home and Italian at work.
\end{keyidea}
""")
G.q("3 Dialetti", r"Secondo la guida, da dove derivano la maggior parte dei dialetti italiani?",
    "direttamente dal latino, come il fiorentino", [("dall'italiano standard, come forme scorrette", "Most are sister languages, not corruptions."),
                                                   ("dal francese", "No."),
                                                   ("dalla televisione", "TV spread standard Italian.")],
    "Sister languages from Latin.", "Dialects and Florentine both developed from Latin.",
    ["latino → dialetti e fiorentino."])
G.q("3 Dialetti", r"What did Manzoni mean by ``rinsing his clothes in the Arno''?",
    "rewriting his novel in the Florentine of educated speech", [("washing clothes in Florence's river", "Literal misreading."),
                                                                 ("translating his novel into Latin", "No."),
                                                                 ("moving to Florence to open a laundry", "No.")],
    "Arno = Florence = Florentine.", "Manzoni revised I promessi sposi to bring its language closer to living Florentine.",
    ["Arno → fiorentino."])
G.q("3 Dialetti", r"What helped most to spread spoken Italian across the country after 1950?",
    "television", [("the Accademia della Crusca", "Founded in 1583; it codified the written language."),
                   ("Latin in schools", "No."),
                   ("emigration to Argentina", "That took Italians abroad.")],
    "TV unified spoken Italian.", "RAI television (from 1954) brought a common spoken Italian into every home.",
    ["TV → spoken Italian everywhere."])

G.sec("Linguistics and structures: false friends, the si, the passive")
G.tex(r"""
\begin{vocab}
la camera & room (not camera) & \emph{la macchina fotografica} = camera \\
la libreria & bookshop (not library) & \emph{la biblioteca} = library \\
la fattoria & farm (not factory) & \emph{la fabbrica} = factory \\
morbido & soft (not morbid) & \\
educato & polite (not educated) & \emph{istruito} = educated \\
il paparazzo & intrusive photographer & from a character in Fellini's \emph{La dolce vita} (1960) \\
lo smart working & remote work & a pseudo-anglicism \\
\end{vocab}

\begin{compare}{Structure}{Use}{Example}
Si impersonale & people in general & In Italia si mangia tardi. \\
Si passivante & the verb agrees with the noun & Si vendono biglietti all'ingresso. \\
Passive with essere & a state or one-time event & La chiesa è stata costruita nel Cinquecento. \\
Passive with venire & a regular process (simple tenses only) & Il Palio viene corso due volte l'anno. \\
\end{compare}
""")
G.q("4 Linguistica", r"Una ragazza dice: «Ho comprato il libro in libreria». Dove è andata?",
    "in un negozio di libri", [("in una biblioteca", "Biblioteca is library: libreria is a false friend."),
                               ("in una fabbrica", "No."),
                               ("in una fattoria", "No.")],
    "libreria = bookshop.", "False friend: libreria (bookshop) vs. biblioteca (library).",
    ["comprare → negozio."])
G.q("4 Linguistica", r"Scegli la forma corretta: In Italia \blank\ molti dialetti diversi.",
    "si parlano", [("si parla", "With si passivante the verb agrees with the plural noun dialetti."),
                   ("si parlare", "A conjugated verb is needed."),
                   ("parlano si", "Si goes before the verb.")],
    "si + plural verb + plural noun.", "Si passivante: si parlano molti dialetti.",
    ["molti dialetti (plural) → si parlano."])

G.sec("Task kit: the Project Q\\&A")
G.tex(r"""
The four recorded questions follow your presentation. You hear each twice and have 40 seconds to answer. Questions usually ask you to expand on a factor, give an example, compare with your own community, and reflect on what you learned.

\begin{compare}{Question type}{Opening}{Then}
Expand & Come ho detto nella presentazione, \ldots & add one new fact from your research \\
Example & Un buon esempio è\ldots & say why it matters (perspective) \\
Compare & Nella mia comunità, invece, \ldots & one similarity or difference, then why \\
Reflect & Quello che mi ha sorpreso di più è che\ldots & what it taught you about the culture \\
\end{compare}

\begin{keyidea}[The culture row in 40 seconds]
You need one answer with a cultural comparison \emph{or} a link between a perspective and a product or practice. Plan it before the exam: \emph{Gli emigranti cantavano «Santa Lucia luntana», il che dimostra quanto fosse forte il legame con Napoli; nella mia comunità, invece, \ldots}
\end{keyidea}

\begin{trap}
Forty seconds is about 70--90 words. Answer the question in the first sentence, then support it. In answers about what surprised you, \emph{mi ha sorpreso che} takes the congiuntivo: \emph{mi ha sorpreso che una canzone fosse così importante}.
\end{trap}
""")
G.q("5 Q&A", r"The interlocutor asks: In che modo la tradizione che ha studiato assomiglia a una tradizione della Sua comunità? What does a strong answer need?",
    "a specific similarity or difference and what it shows about each culture", [("a summary of the whole presentation", "Repeating the presentation does not answer the question."),
                                                                                 ("a list of facts about the tradition only", "The question asks for a comparison."),
                                                                                 ("a description of how you did the research", "The research process is not the topic.")],
    "Compare + explain.", "A cultural comparison that explains what each practice reflects can earn the top culture score.",
    ["Similarity/difference → why → perspective."])
G.q("5 Q&A", r"Scegli la forma corretta: Mi ha sorpreso che la canzone \blank\ così famosa all'estero.",
    "fosse", [("era", "Mi ha sorpreso che expresses emotion and takes the congiuntivo."),
              ("fossero", "La canzone is singular."),
              ("sarà", "The future does not fit a past surprise.")],
    "Emotion + past → congiuntivo imperfetto.", "Mi ha sorpreso che + congiuntivo; the past main clause requires the imperfetto (fosse).",
    ["mi ha sorpreso che … fosse."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 2: Language and Culture: Question Set", r"Unit 2 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (a Presentation and an Audio and Chart for listening, a Literary Text and an Article for reading) on dialects, the night of the Befana, Italian words around the world and the languages spoken at home, followed by a practice Project Q\&A on music, the 2026--27 project lens, with the 9-point scoring guide and model answers. The Q\&A is a practice task written for this set, not the official 2027 project prompt. As on the exam, questions and choices are in Italian; listening sources are printed as transcripts. All sources and data are original and fictional. Allow about 25 minutes for the multiple choice and 8 minutes for the Q\&A.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Q\&A: \blank\ / 9 \qquad Target: 15+ MCQ and 6+ Q\&A",
        short="Unit 2", sub="Language and Culture")

Q.sec("Listening: Presentation")
Q.src(r"Listening 1 \textperiodcentered\ Presentation (transcript) \textperiodcentered\ «Lingua o dialetto?», lezione all'università", [
    r"(PROFESSORE) Molti stranieri pensano che il napoletano o il veneziano siano un italiano «sbagliato». In realtà, quasi tutti i dialetti italiani sono nati dal latino, esattamente come il fiorentino da cui viene l'italiano standard. Sono lingue sorelle, non figlie.",
    r"(PROFESSORE) Perché allora l'italiano ha vinto? Prima per ragioni di prestigio: Dante, Petrarca e Boccaccio scrivevano in fiorentino, e i letterati di tutta la penisola li imitavano. Poi, dopo l'Unità, la scuola, il servizio militare e soprattutto la televisione hanno portato l'italiano parlato in ogni casa.",
    r"(PROFESSORE) Oggi pochi giovani parlano solo dialetto, ma molti lo usano con i nonni o per scherzare con gli amici. E alcuni cantanti rap lo hanno riportato di moda.",
    r"(PROFESSORE) Il mio consiglio? Non chiamatelo un errore. Un dialetto è un pezzo di storia che si può ascoltare.",
], 5)
Q.q("1.B.1 Main idea", r"Qual è il messaggio principale della lezione?",
    "I dialetti sono lingue sorelle dell'italiano, non forme sbagliate.", [("I dialetti stanno per sparire completamente.", "Young people still use them."),
                                                                          ("Il napoletano deriva dal veneziano.", "No."),
                                                                          ("La televisione ha distrutto la cultura italiana.", "Not his claim.")],
    "Sister languages.", "Main idea (1.B.1): stated at the start and repeated at the end.",
    ["Sono lingue sorelle, non figlie."])
Q.q("1.A.1 Detail", r"Secondo il professore, perché il fiorentino è diventato la base dell'italiano?",
    "perché grandi scrittori lo usavano e venivano imitati", [("perché Firenze era la capitale del Regno", "Not his explanation."),
                                                             ("perché era il dialetto più facile", "Not stated."),
                                                             ("per decisione della televisione", "TV came much later.")],
    "Literary prestige.", "Detail (1.A.1): prima per ragioni di prestigio.",
    ["Dante, Petrarca e Boccaccio … i letterati li imitavano."])
Q.q("1.B.4 Organization", r"Come è organizzata la seconda parte della lezione?",
    "spiega le cause in ordine cronologico, dal prestigio letterario alla televisione", [("confronta l'Italia con la Spagna", "No comparison."),
                                                                                         ("racconta una storia personale", "No story."),
                                                                                         ("elenca parole dialettali", "No word list.")],
    "Prima … Poi …", "Organization (1.B.4): chronological causes.",
    ["Prima per ragioni di prestigio … Poi, dopo l'Unità…"])
Q.q("1.C.3 Inference", r"Che cosa si può dedurre sull'uso del dialetto tra i giovani di oggi?",
    "Lo usano soprattutto in situazioni familiari o scherzose.", [("Lo parlano in tutte le situazioni formali.", "No."),
                                                                  ("Non lo capiscono più.", "Many use it with grandparents."),
                                                                  ("È vietato a scuola.", "Not stated.")],
    "Informal settings.", "Inference (1.C.3): con i nonni, per scherzare.",
    ["con i nonni o per scherzare con gli amici."])
Q.q("1.B.3 Point of view", r"Che cosa consiglia il professore agli studenti?",
    "di considerare il dialetto un patrimonio storico, non un errore", [("di non parlare mai in dialetto", "The opposite."),
                                                                       ("di imparare solo l'italiano standard", "Not his point."),
                                                                       ("di ascoltare solo musica rap", "No.")],
    "Non chiamatelo un errore.", "Point of view (1.B.3): his closing advice.",
    ["Un dialetto è un pezzo di storia che si può ascoltare."])

Q.sec("Reading: Literary Text")
Q.src(r"Reading 1 \textperiodcentered\ Literary Text \textperiodcentered\ «La calza» (racconto)", [
    r"La sera del 5 gennaio la nonna appendeva la calza al camino con una cerimonia che sembrava una messa. «Se sei stato buono, la Befana ti lascia i dolci», diceva in dialetto, «e se no, carbone.» Io passavo l'anno intero a fare i conti dei miei peccati.",
    r"Quell'anno avevo rotto il vaso della zia e avevo dato la colpa al gatto. Non riuscii a dormire. Ogni scricchiolio della casa mi sembrava una scopa che atterrava sul tetto.",
    r"La mattina, nella calza c'erano mandarini, cioccolatini e, in fondo, un pezzo di carbone nero e lucido. Lo morsi per la disperazione: era dolce. Alzai gli occhi e vidi la nonna che rideva in silenzio. Il gatto, sul davanzale, mi guardava con aria di chi sa.",
], 5)
Q.q("1.A.1 Detail", r"Che cosa faceva la nonna la sera del 5 gennaio?",
    "appendeva la calza al camino", [("preparava una torta", "Not mentioned."),
                                     ("andava a messa", "The ceremony only seemed like a mass."),
                                     ("regalava carbone", "The Befana brings it.")],
    "appendeva la calza.", "Detail (1.A.1).",
    ["…la nonna appendeva la calza al camino…"])
Q.q("1.C.3 Inference", r"Perché il narratore non riuscì a dormire?",
    "perché temeva di ricevere il carbone per quello che aveva fatto", [("perché aveva mangiato troppi dolci", "No."),
                                                                        ("perché il gatto faceva rumore", "Noises scared him because of guilt."),
                                                                        ("perché la nonna parlava in dialetto", "No.")],
    "Guilt.", "Inference (1.C.3): he broke the vase and blamed the cat.",
    ["vaso rotto + colpa al gatto → paura del carbone."])
Q.q("1.B.5 Word meaning", r"Nel testo, «uno scricchiolio» è",
    "un piccolo rumore secco", [("una luce improvvisa", "No."),
                                ("un odore di fumo", "No."),
                                ("un tipo di dolce", "No.")],
    "creak.", "Word meaning (1.B.5): he imagines a broom landing on the roof.",
    ["ogni scricchiolio della casa → noise."])
Q.q("1.B.3 Tone", r"Quale tono domina l'ultimo paragrafo?",
    "ironico e affettuoso", [("tragico", "The coal is sweet; the grandmother laughs."),
                            ("arrabbiato", "No anger."),
                            ("scientifico", "No.")],
    "Gentle irony.", "Tone (1.B.3): the sweet coal and the knowing cat.",
    ["era dolce … la nonna rideva … il gatto … con aria di chi sa."])
Q.q("1.C.2 Conclusion", r"Che cosa rivela la fine del racconto sulla tradizione della Befana in quella famiglia?",
    "che serviva a insegnare le buone maniere con umorismo, non a punire davvero", [("che la nonna voleva punire il nipote severamente", "The coal is sugar."),
                                                                                   ("che la Befana non portava mai dolci", "There were sweets too."),
                                                                                   ("che la famiglia non credeva nelle feste", "No.")],
    "A lesson with humor.", "Conclusions (1.C.2): sweet coal + laughter.",
    ["carbone dolce → lezione, non punizione."])

Q.sec("Reading: Article")
Q.src(r"Reading 2 \textperiodcentered\ Article \textperiodcentered\ «Parole italiane in viaggio»", [
    r"Dalla pizza all'opera, dal ciao al paparazzo: molte parole italiane hanno fatto il giro del mondo. Ma non sempre sono arrivate a destinazione con lo stesso significato.",
    r"Prendiamo «latte». In molti bar all'estero, se ordinate un «latte», vi portano un caffè con latte caldo e schiuma. In Italia, invece, rischiate di ricevere un semplice bicchiere di latte. Lo stesso vale per «panini»: all'estero spesso è usato al singolare, mentre in italiano «panini» è plurale.",
    r"Secondo la linguista Elena Galli, questi viaggi delle parole non sono errori da correggere, ma storie da raccontare. «Ogni parola che cambia significato ci dice qualcosa sull'incontro tra due culture», spiega. «È la prova che l'italiano è vivo anche fuori dall'Italia.»",
], 5)
Q.q("1.B.1 Main idea", r"Di che cosa tratta principalmente l'articolo?",
    "di parole italiane che hanno cambiato significato all'estero", [("della storia della pizza", "Pizza is only an example."),
                                                                     ("di come si prepara un buon caffè", "No."),
                                                                     ("degli errori grammaticali degli stranieri", "Galli rejects that view.")],
    "Words that travel.", "Main idea (1.B.1).",
    ["non sempre sono arrivate … con lo stesso significato."])
Q.q("1.A.1 Detail", r"Che cosa rischia di ricevere chi ordina «un latte» in un bar italiano?",
    "un semplice bicchiere di latte", [("un caffè con latte e schiuma", "That is what you get abroad."),
                                       ("un panino", "No."),
                                       ("un gelato", "No.")],
    "latte = milk.", "Detail (1.A.1).",
    ["In Italia … un semplice bicchiere di latte."])
Q.q("1.A.1 Detail", r"Che cosa osserva l'articolo sulla parola «panini»?",
    "In italiano è plurale, ma all'estero spesso si usa al singolare.", [("Non esiste in italiano.", "It does."),
                                                                         ("Significa pizza.", "No."),
                                                                         ("È una parola dialettale.", "Not stated.")],
    "panino / panini.", "Detail (1.A.1).",
    ["…«panini» è plurale."])
Q.q("1.B.3 Point of view", r"Qual è l'opinione di Elena Galli sui cambiamenti di significato?",
    "che raccontano l'incontro tra culture e mostrano la vitalità dell'italiano", [("che sono errori da correggere", "She says the opposite."),
                                                                                  ("che danneggiano l'italiano", "No."),
                                                                                  ("che dovrebbero essere vietati", "No.")],
    "Stories, not errors.", "Point of view (1.B.3).",
    ["non sono errori … ma storie da raccontare."])
Q.q("1.B.5 Word meaning", r"Nell'articolo, «hanno fatto il giro del mondo» significa che le parole",
    "si sono diffuse in molti paesi", [("sono tornate in Italia", "No."),
                                       ("sono state dimenticate", "No."),
                                       ("sono diventate più lunghe", "No.")],
    "fare il giro del mondo = spread everywhere.", "Word meaning (1.B.5): an idiom.",
    ["giro del mondo → diffuse ovunque."])

Q.sec("Listening: Audio and Chart")
Q.src(r"Listening 2 \textperiodcentered\ Audio and Chart (transcript) \textperiodcentered\ «Che lingua si parla a casa?», Radio Lingua", [
    r"(GIORNALISTA) Un istituto di ricerca ha chiesto a migliaia di famiglie quale lingua parlano a casa, confrontando i dati di oggi con quelli di venticinque anni fa.",
    r"(GIORNALISTA) Il cambiamento più forte riguarda chi parla prevalentemente dialetto: un gruppo che si è più che dimezzato. Ma attenzione, spiega il ricercatore: la quota di chi alterna italiano e dialetto è rimasta quasi stabile.",
    r"(RICERCATORE) Il dialetto non scompare, si trasforma: non è più l'unica lingua di casa, ma una seconda lingua, quella degli affetti e delle battute.",
], 5, table=(["Lingua usata a casa", "2000", "2025"], [["Solo o prevalentemente italiano", "44~\\%", "58~\\%"], ["Italiano e dialetto", "32~\\%", "30~\\%"], ["Prevalentemente dialetto", "19~\\%", "8~\\%"], ["Un'altra lingua", "5~\\%", "4~\\%"]]),
      note="Dati fittizi.")
Q.q("1.A.2 Data", r"Secondo la tabella, quale gruppo è cresciuto tra il 2000 e il 2025?",
    "chi parla solo o prevalentemente italiano", [("chi parla prevalentemente dialetto", "It fell from 19% to 8%."),
                                                 ("chi alterna italiano e dialetto", "It went from 32% to 30%."),
                                                 ("chi parla un'altra lingua", "It went from 5% to 4%.")],
    "44 → 58.", "Data (1.A.2): only one row rises.",
    ["Solo italiano: 44 % → 58 %."])
Q.q("1.C.1 Connect", r"Quale dato della tabella corrisponde al gruppo che, secondo il servizio, «si è più che dimezzato»?",
    "Prevalentemente dialetto: dal 19~\\% all'8~\\%", [("Italiano e dialetto: dal 32~\\% al 30~\\%", "That is the almost stable group."),
                                                   ("Solo italiano: dal 44~\\% al 58~\\%", "That group grew."),
                                                   ("Un'altra lingua: dal 5~\\% al 4~\\%", "Not halved.")],
    "19 → 8 = more than halved.", "Connect (1.C.1): match the description to the numbers.",
    ["19 / 2 = 9.5 > 8 → più che dimezzato."])
Q.q("1.C.1 Connect", r"Quale dato conferma che la quota di chi alterna italiano e dialetto è «quasi stabile»?",
    "il passaggio dal 32~\\% al 30~\\%", [("il passaggio dal 44~\\% al 58~\\%", "That is the Italian-only group."),
                                          ("il passaggio dal 19~\\% all'8~\\%", "That is the dialect-only group."),
                                          ("il 4~\\% del 2025", "That is another language.")],
    "32 → 30.", "Connect (1.C.1).",
    ["Italiano e dialetto: 32 % → 30 %."])
Q.q("1.B.3 Point of view", r"Secondo il ricercatore, che cosa sta succedendo al dialetto?",
    "Si sta trasformando in una seconda lingua, legata agli affetti.", [("Sta scomparendo del tutto.", "He says it does not disappear."),
                                                                         ("Sta sostituendo l'italiano.", "No."),
                                                                         ("Si usa solo a scuola.", "No.")],
    "si trasforma.", "Point of view (1.B.3).",
    ["Il dialetto non scompare, si trasforma."])
Q.q("1.B.5 Word meaning", r"Nel servizio, «le battute» sono",
    "frasi scherzose", [("colpi alla porta", "Another meaning of battuta; not here."),
                        ("partite di calcio", "No."),
                        ("errori di grammatica", "No.")],
    "battute = jokes.", "Word meaning (1.B.5): affetti e battute = feelings and jokes.",
    ["la lingua degli affetti e delle battute."])

Q.frq(kind="Project Q&A", head=r"Question 2 \textperiodcentered\ Project Q\&A (practice) \textperiodcentered\ 9 points \textperiodcentered\ 4 answers of 40 seconds", mins=8,
      directions=[r"Imagine that your project examined how music expresses identity in an Italian-speaking community, and that your presentation focused on Neapolitan song (songs such as ``'O sole mio'', 1898, written in Neapolitan and once launched at the Festa di Piedigrotta, later carried abroad by emigrants). You will hear four questions. Each is played twice; you have 40 seconds to answer each one. Answer in Italian."],
      prompt=[r"1. Nella Sua presentazione ha parlato della canzone napoletana. Perché queste canzoni sono scritte in napoletano e non in italiano?",
              r"2. Può fare un esempio concreto di come gli emigranti hanno usato queste canzoni?",
              r"3. Nella Sua comunità esiste una musica che ha un ruolo simile? Faccia un confronto.",
              r"4. Che cosa L'ha sorpresa di più nella Sua ricerca?"],
      model=[r"\textbf{1.} Perché il napoletano era, ed è ancora, la lingua della vita quotidiana a Napoli. Quando sono nate le grandi canzoni, alla fine dell'Ottocento, la maggior parte dei napoletani non parlava italiano a casa. Scrivere in napoletano significava parlare al cuore della gente, e dimostra quanto la città fosse orgogliosa della propria lingua.",
             r"\textbf{2.} Sì. Una canzone del 1919, «Santa Lucia luntana», racconta la nostalgia di chi lascia Napoli in nave. Gli emigranti a New York e a Buenos Aires la cantavano nelle feste e nei locali. Questo dimostra che la musica serviva a tenere vivo il legame con la città d'origine.",
             r"\textbf{3.} Nella mia comunità irlandese-americana di Boston esistono canzoni sull'emigrazione molto simili. Anche lì si canta la nostalgia di una terra lasciata per povertà. La differenza è che le canzoni irlandesi che conosco sono in inglese, mentre quelle napoletane conservano il dialetto, che per gli emigranti era un'identità in sé.",
             r"\textbf{4.} Mi ha sorpreso che «'O sole mio» fosse conosciuta in tutto il mondo come una canzone «italiana», anche se è scritta in napoletano. Ho capito che, per molti stranieri, Napoli e l'Italia sono la stessa cosa, mentre per i napoletani la loro lingua è un motivo di grande orgoglio."],
      rows=[("A Task", 2, "four relevant, complete answers that address each question", "answers that drift back to the presentation or stop after one sentence"),
            ("B Culture", 2, "in at least one answer, a cultural comparison (answer 3) or a perspective linked to a product or practice (answers 1 and 2)", "only describing the songs (1 point)"),
            ("C Language", 3, "varied vocabulary and structures (congiuntivo after mi ha sorpreso che, relative clauses, imperfetto)", "short, repetitive sentences"),
            ("D Fluency", 2, "natural pace and intonation, clear pronunciation, few pauses", "long silences, many restarts")],
      tips=["Each answer starts by answering the question directly.", "Answer 3 is a full cultural comparison: similarity, difference, and why.",
            "Answers 1 and 2 link products (songs in Neapolitan) and practices (singing in emigrant communities) to perspectives (pride, nostalgia).", "About 70–80 words each fits 40 seconds."],
      ask="Answer each question aloud in Italian (40 seconds each), jotting keywords first; then mark your answers.", lines=12)

GUIDE, QSET = G, Q
