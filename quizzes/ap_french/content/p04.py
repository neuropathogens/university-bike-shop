from ap_wl.model import Doc

STEM = "04-science-technology"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 4: Science and Technology", r"Unit 4 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 4 asks how science and technology change daily life, communication and society, and who benefits. Its recommended contexts are innovations and emerging technologies, personal technology and communication, science in everyday life, and the societal impacts of science and technology. This guide gives the vocabulary of technology and science, French and francophone inventions and projects, the digital divide, the right to disconnect and misinformation, the structures for predictions, probability and data, and an Argumentative Essay kit focused on reading charts. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Chart verbs I can use: \blank[10em]",
        short="Unit 4", sub="Science and Technology")

G.sec("Innovation and discovery")
G.tex(r"""
\begin{vocab}
l'intelligence artificielle (IA) & artificial intelligence & \\
l'algorithme / les données & algorithm / data & \\
l'invention / la découverte & invention / discovery & \emph{inventer} vs. \emph{découvrir} \\
le vaccin / la pasteurisation & vaccine / pasteurization & Louis Pasteur \\
l'énergie nucléaire / renouvelable & nuclear / renewable energy & \\
la fusée / le lanceur & rocket / launcher & Ariane \\
\end{vocab}

\begin{compare}{Innovation}{Who, where, when}{Note}
the rabies vaccine; pasteurization & Louis Pasteur, 1880s & science for public health \\
radioactivity & Marie Curie: Nobel Prizes in 1903 (physics) and 1911 (chemistry) & first person with two Nobel Prizes \\
the smart card (\emph{la carte à puce}) & Roland Moreno, patented 1974 & today's bank and SIM cards \\
the Minitel & France Télécom, 1980s & an online network before the web \\
the TGV & high-speed train, 1981 & \\
Ariane rockets & launched from Kourou, French Guiana & Europe's spaceport near the equator \\
\end{compare}
""")
G.q("1 Innovation", r"Qu'est-ce qui rend Marie Curie unique dans l'histoire des prix Nobel~?",
    "Elle a reçu deux prix Nobel dans deux sciences différentes.", [("Elle a inventé la carte à puce.", "That was Roland Moreno."),
                                                                     ("Elle a créé le premier vaccin contre la rage.", "That was Louis Pasteur."),
                                                                     ("Elle a construit la première fusée Ariane.", "No.")],
    "Nobels in 1903 (physics) and 1911 (chemistry).", "Marie Curie is the only person to win Nobel Prizes in two different sciences.",
    ["physique 1903 + chimie 1911."])
G.q("1 Innovation", r"Why is Europe's spaceport located in Kourou, French Guiana?",
    "its position near the equator helps rockets reach orbit", [("because it is the coldest place in France", "It is tropical."),
                                                              ("because no one lives in French Guiana", "Many people do."),
                                                              ("because it is close to Paris", "It is in South America.")],
    "Near the equator.", "Launching near the equator gives rockets extra speed from Earth's rotation.",
    ["équateur → advantage for launches."])

G.sec("Personal technology and communication")
G.tex(r"""
\begin{vocab}
le portable / le smartphone & cell phone & \\
les réseaux sociaux & social media & \\
télécharger / publier / partager & download / post / share & \\
la fracture numérique & the digital divide & gaps in access between groups or regions \\
le cyberharcèlement & cyberbullying & \\
le droit à la déconnexion & right to disconnect & French labor law since 2017 \\
la majorité numérique & ``digital majority'' & a 2023 French law: parental consent for social media under 15 \\
l'infox & fake news & official French term \\
\end{vocab}

\textbf{The right to disconnect.} Since 2017, French companies with 50 or more employees must negotiate rules so that employees are not expected to answer work email outside working hours. The perspective: private life and rest deserve protection from constant connection.

\textbf{Mobile money.} In West Africa, many people without a bank account pay, save and send money by phone, for example with Orange Money. The practice reflects how technology can jump over missing infrastructure.
""")
G.q("2 Communication", r"Que garantit «~le droit à la déconnexion~» en France~?",
    "que les salariés ne soient pas obligés de répondre aux messages professionnels en dehors du travail", [("que tout le monde ait internet gratuit", "Unrelated."),
                                                                                                           ("que les enfants n'aient pas de portable", "No."),
                                                                                                           ("que les entreprises ferment le week-end", "No.")],
    "Déconnexion = no work messages off hours.", "The 2017 law protects rest time from constant connection.",
    ["droit à la déconnexion → private life protected."])
G.q("2 Communication", r"Which perspective does mobile money in West Africa most directly reflect?",
    "Technology can provide services where traditional infrastructure is missing.", [("Banks should be the only way to save money.", "Mobile money reaches people without banks."),
                                                                                    ("Phones should be used only for calls.", "The opposite."),
                                                                                    ("Cash should be banned.", "Not the point.")],
    "Leapfrogging.", "Practice (paying by phone without a bank account) ↔ perspective (technology bridging gaps).",
    ["no bank branch nearby → phone as bank."])

G.sec("Science in everyday life and its impact")
G.tex(r"""
\begin{vocab}
la santé publique & public health & \\
l'environnement / la pollution & environment / pollution & \\
la centrale nucléaire & nuclear power plant & France gets about two thirds of its electricity from nuclear power \\
vérifier une information & to fact-check & \\
les effets secondaires & side effects & \\
la désinformation & misinformation & \\
\end{vocab}

\textbf{Questions about impact} ask who benefits and who is left out, what the risks are, and who should decide (\emph{Qui devrait encadrer l'IA~?}). Good answers weigh both: \emph{Certes, l'IA facilite le diagnostic, mais elle pose des problèmes de confidentialité.}
""")
G.q("3 Impact", r"Choisissez le meilleur mot~: Avant de partager une information, il vaut mieux \blank\ si la source est fiable.",
    "vérifier", [("vérifié", "After il vaut mieux you need an infinitive."),
                 ("vérifie", "With no new subject, il vaut mieux takes an infinitive."),
                 ("vérification", "A noun cannot follow il vaut mieux here.")],
    "il vaut mieux + infinitive.", "Il vaut mieux, il faut, mieux vaut + infinitive give general advice.",
    ["il vaut mieux vérifier."])
G.q("3 Impact", r"Which sentence weighs a benefit against a risk, as impact questions reward?",
    "Certes, les applications de santé aident à repérer les maladies, mais elles collectent des données très personnelles.",
    [("Les applications de santé sont géniales.", "One-sided and vague."),
     ("Beaucoup de gens utilisent des applications de santé.", "A fact with no evaluation."),
     ("Il faut interdire tout de suite les applications de santé.", "One-sided, with no reasoning.")],
    "Certes X, mais Y.", "Concessive structures let you weigh both sides in one sentence.",
    ["benefit + risk."])

G.sec("Structures: predictions, probability and data")
G.tex(r"""
\begin{compare}{Purpose}{Structure}{Example}
Predict & futur / aller + infinitive & En 2030, la moitié des voitures seront électriques. \\
Probability & il est probable que + \textbf{indicative} & Il est probable que l'IA changera de nombreux métiers. \\
Possibility & il est possible que + \textbf{subjunctive} & Il est possible que l'IA remplace certains emplois. \\
Hypothesize & si + imparfait, conditionnel & Si tout le monde avait internet, la fracture disparaîtrait. \\
Means & en + present participle (gérondif) & On apprend en pratiquant. \\
Data: change & augmenter, progresser, diminuer, baisser, doubler & L'usage a doublé entre 2019 et 2024. \\
Data: share & la majorité, la moitié, un tiers, un sur quatre & Un élève sur quatre\ldots \\
\end{compare}

\begin{trap}
\emph{Il est probable que} takes the indicative, but \emph{il est possible que} and \emph{il se peut que} take the subjunctive. The exam's language row rewards getting this right.
\end{trap}
""")
G.q("4 Structures", r"Choisissez la bonne forme~: Il est possible que les nouveaux satellites \blank\ internet aux zones rurales.",
    "apportent", [("apporteront", "Il est possible que takes the subjunctive, not the future."),
                  ("apporter", "With a new subject (les satellites), use que + subjunctive."),
                  ("apportaient", "The imparfait indicative does not follow il est possible que.")],
    "Il est possible que + subjunctive.", "Possibility (il est possible que, il se peut que) → subjunctive; probability (il est probable que) → indicative.",
    ["il est possible que → apportent (subjonctif)."])
G.q("4 Structures", r"Selon un graphique, le paiement par téléphone est passé de 20~\% à 40~\% en cinq ans. Quelle phrase le décrit avec précision~?",
    "Le paiement par téléphone a doublé en cinq ans.", [("Le paiement par téléphone a augmenté de 20~\\% chaque année.", "The total rose 20 points over five years, not 20% a year."),
                                                         ("Le paiement par téléphone a baissé de moitié.", "It rose."),
                                                         ("La majorité des gens paient par téléphone.", "40% is not a majority.")],
    "20 → 40 = double.", "Precise chart language: a doublé, a augmenté de 20 points, est passé de 20 % à 40 %.",
    ["40 = 2 × 20 → a doublé."])
G.q("4 Structures", r"Choose the passive sentence.",
    "Les premiers ordinateurs de l'entreprise ont été conçus par des ingénieures.", [("Des ingénieures ont conçu les premiers ordinateurs de l'entreprise.", "Active voice."),
                                                                                    ("Des ingénieures sont en train de concevoir des ordinateurs.", "Active progressive."),
                                                                                    ("Des ingénieures concevraient des ordinateurs.", "Active conditional.")],
    "être + participle (+ par).", "The passive with être puts the thing affected first.",
    ["ont été conçus par → passive."])

G.sec("Task kit: the Argumentative Essay with a chart")
G.tex(r"""
Unit 4 topics are often debates about benefits and risks: \emph{Faut-il interdire les réseaux sociaux aux moins de 15 ans~?}, \emph{L'IA est-elle une chance pour l'école~?} The chart source is easy to misread under time pressure.

\begin{terms}
Read the chart first & title, units (\%, millions, heures), years, who was surveyed \\
Pick one comparison & the biggest change, a majority, or a surprising gap \\
Say it precisely & \emph{D'après le graphique de la source 2, 62~\% des\ldots, contre 25~\% des\ldots} \\
Explain it & \emph{Cela indique que\ldots / Ces chiffres montrent que\ldots} \\
\end{terms}

\begin{trap}
Misreading a chart (switching columns, treating a percentage as a number of people) costs points in source use. Quote the numbers with their labels.
\end{trap}
""")
G.q("5 Essai", r"A chart shows 62\% of students use AI tools for homework and 25\% of teachers allow it. Which sentence uses the chart correctly?",
    r"D'après la source 2, 62~\% des élèves utilisent l'IA pour leurs devoirs, alors que seulement 25~\% des professeurs l'autorisent.", [("D'après la source 2, 62~\\% des professeurs utilisent l'IA.", "Switches the groups."),
                                                                                                                                          ("D'après la source 2, 62 élèves utilisent l'IA.", "Turns a percentage into a number of people."),
                                                                                                                                          ("La source 2 dit que tout le monde utilise l'IA.", "Overstates the data.")],
    "Numbers + labels + source.", "Chart evidence must keep the groups and units straight and name the source.",
    ["62% → students; 25% → teachers."])
G.q("5 Essai", r"Which phrase best explains what a statistic shows?",
    "Ces chiffres montrent que…", [("Il était une fois…", "A storytelling opener."),
                                  ("Au fait, …", "An aside, not an explanation."),
                                  ("Pour commencer l'histoire…", "Not an explanation.")],
    "Ces chiffres montrent que…", "Argumentation (Row C) needs the step from evidence to claim.",
    ["Data → claim: ces chiffres montrent que."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 4: Science and Technology: Question Set", r"Unit 4 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Audio and Chart and an Audio Report for listening, an Article and a Literary Text for reading) on sleep and screens, the Guiana Space Centre, family technology and mobile money, followed by an Argumentative Essay with three sources and the 10-point scoring guide. As on the exam, questions and choices are in French; listening sources are printed as transcripts. All sources and data are original and fictional, written for practice. Allow about 25 minutes for the multiple choice and 55 minutes for the essay.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Essay: \blank\ / 10 \qquad Target: 15+ MCQ and 7+ essay \qquad Pace: 75 s per item",
        short="Unit 4", sub="Science and Technology")

Q.sec("Listening: Audio and Chart")
Q.src(r"Listening 1 \textperiodcentered\ Audio and Chart (transcript) \textperiodcentered\ «~Écrans et sommeil~», Radio Science", [
    r"(JOURNALISTE) Combien de temps les adolescents passent-ils devant un écran le soir, et quel effet cela a-t-il sur leur sommeil~? Une équipe de l'Université de Genève a suivi 900 jeunes Suisses de 13 à 17 ans pendant quatre ans.",
    r"(JOURNALISTE) Résultat~: le temps d'écran du soir a augmenté régulièrement jusqu'en 2023, puis il a légèrement diminué en 2024. Les chercheurs associent cette baisse à une campagne nationale et aux règles adoptées par de nombreuses familles, comme laisser les téléphones hors de la chambre.",
    r"(CHERCHEUR) Nous ne voulons pas diaboliser la technologie. Le problème, ce n'est pas l'écran en lui-même, mais ce qu'il remplace~: le sommeil, le sport, la conversation. Les jeunes qui ont réduit leur temps d'écran disent qu'ils dorment mieux.",
], 5, table=(["Année", "Heures d'écran le soir (moyenne)"], [["2021", "2,1"], ["2022", "2,6"], ["2023", "3,0"], ["2024", "2,7"]]),
      note="Temps passé devant un écran après 18 heures, adolescents de 13 à 17 ans (données fictives).")
Q.q("1.A.2 Data", r"Selon le tableau, en quelle année les adolescents passaient-ils le plus de temps devant un écran le soir~?",
    "2023", [("2021", "2021 is the lowest, 2.1 hours."),
             ("2022", "2.6 hours, less than 2023."),
             ("2024", "2.7 hours: it fell after 2023.")],
    "Peak: 3.0 h in 2023.", "Data (1.A.2): find the maximum.",
    ["3,0 is the highest value."])
Q.q("1.C.1 Connect", r"Comment les chercheurs expliquent-ils l'évolution de 2024 visible dans le tableau~?",
    "par une campagne nationale et des règles adoptées par les familles", [("par l'augmentation des devoirs", "Not mentioned."),
                                                                           ("par l'arrivée de nouveaux réseaux sociaux", "That would explain a rise."),
                                                                           ("par la fermeture des écoles", "Not mentioned.")],
    "Table: 3.0 → 2.7; audio: campagne + règles.", "Connect (1.C.1): match the dip in the table with the cause in the audio.",
    ["a légèrement diminué en 2024 → une campagne nationale et aux règles…"])
Q.q("1.B.3 Point of view", r"Quelle est l'opinion du chercheur sur la technologie~?",
    "Le problème est ce que l'écran remplace, pas l'écran lui-même.", [("La technologie est dangereuse et il faut l'interdire.", "Nous ne voulons pas diaboliser la technologie."),
                                                                        ("Les jeunes devraient passer plus de temps devant les écrans.", "Not his view."),
                                                                        ("Les écrans améliorent le sommeil.", "Those who reduced screen time sleep better.")],
    "ce n'est pas l'écran… mais ce qu'il remplace.", "Point of view (1.B.3): ce n'est pas… mais… states his position.",
    ["Le problème, ce n'est pas l'écran en lui-même, mais…"])
Q.q("1.A.1 Detail", r"Quelle règle familiale est donnée en exemple~?",
    "laisser les téléphones hors de la chambre", [("éteindre la télévision le matin", "Not mentioned."),
                                                 ("interdire les jeux vidéo le week-end", "Not mentioned."),
                                                 ("faire du sport tous les soirs", "Not mentioned.")],
    "téléphones hors de la chambre.", "Detail (1.A.1).",
    ["comme laisser les téléphones hors de la chambre."])
Q.q("1.B.5 Word meaning", r"Dans l'enregistrement, «~diaboliser~» signifie",
    "présenter quelque chose comme entièrement mauvais", [("utiliser quelque chose souvent", "No."),
                                                         ("étudier quelque chose scientifiquement", "No."),
                                                         ("vendre quelque chose cher", "No.")],
    "diaboliser = present as evil.", "Word meaning (1.B.5): followed by a more balanced view.",
    ["Nous ne voulons pas diaboliser… → not make it the villain."])

Q.sec("Reading: Article")
Q.src(r"Reading 1 \textperiodcentered\ Article \textperiodcentered\ «~Kourou, la porte de l'espace~»", [
    r"En Guyane, sur la côte de l'Amérique du Sud, se trouve le Centre spatial guyanais, d'où partent les fusées européennes. Sa position, tout près de l'équateur, donne un élan supplémentaire aux lanceurs grâce à la rotation de la Terre.",
    r"Pour l'ingénieure guyanaise Laura Joseph, la base a transformé sa région. «~Quand j'étais petite, personne dans mon village ne pensait devenir scientifique. Aujourd'hui, il y a des bourses, des ateliers dans les écoles et une fête de la science chaque année.~»",
    r"Tout n'est pas rose pour autant. Des habitants regrettent que les emplois les mieux payés reviennent souvent à des personnes venues de l'Hexagone, et des communautés amérindiennes demandent davantage de respect pour leurs terres. Les autorités ont répondu par un programme de formation technique pour les jeunes Guyanais.",
    r"Enfin, la base pose une question environnementale~: comment concilier lancements de fusées et protection d'une forêt tropicale exceptionnelle~?",
], 5)
Q.q("1.B.1 Main idea", r"Quelle est l'idée principale de l'article~?",
    "La base spatiale apporte des avantages à la Guyane, mais soulève aussi des problèmes.", [("La Guyane veut fermer la base spatiale.", "Nothing suggests closing it."),
                                                                                              ("Les sciences n'intéressent pas les Guyanais.", "Scholarships and a festival show interest."),
                                                                                              ("Les fusées sont construites uniquement en Guyane.", "Not stated.")],
    "Benefits + Tout n'est pas rose.", "Main idea (1.B.1): positive effects, then problems and responses.",
    ["Paragraph 2 benefits; 3–4 challenges."])
Q.q("1.A.1 Detail", r"Pourquoi la position de la base est-elle avantageuse~?",
    "parce qu'elle est proche de l'équateur", [("parce qu'elle est loin de la mer", "It is on the coast."),
                                              ("parce qu'il y fait froid", "It is tropical."),
                                              ("parce qu'elle est proche de Paris", "It is in South America.")],
    "près de l'équateur.", "Detail (1.A.1).",
    ["tout près de l'équateur, donne un élan supplémentaire…"])
Q.q("1.B.3 Point of view", r"Que demandent les communautés amérindiennes~?",
    "davantage de respect pour leurs terres", [("plus de lancements de fusées", "Not their demand."),
                                              ("des emplois à Paris", "Not their demand."),
                                              ("la fin de la fête de la science", "No.")],
    "respect pour leurs terres.", "Point of view (1.B.3): attribute each concern to the right group.",
    ["demandent davantage de respect pour leurs terres."])
Q.q("1.B.5 Word meaning", r"Dans l'article, «~l'Hexagone~» désigne",
    "la France métropolitaine", [("une figure géométrique sur la base", "Figurative name."),
                                 ("la Guyane", "Guyane is the place being contrasted."),
                                 ("un pays voisin de la Guyane", "No.")],
    "l'Hexagone = mainland France.", "Word meaning (1.B.5): mainland France is called l'Hexagone for its six-sided shape.",
    ["personnes venues de l'Hexagone → from mainland France."])
Q.q("1.B.4 Organization", r"Quelle est la fonction de l'expression «~Tout n'est pas rose pour autant~»~?",
    "introduire les problèmes après avoir présenté les avantages", [("résumer la conclusion de l'article", "The article continues."),
                                                                   ("donner un exemple d'avantage", "It introduces drawbacks."),
                                                                   ("changer de sujet", "Still Guiana.")],
    "Transition to the counterpoint.", "Organization (1.B.4): a contrast transition.",
    ["benefits → Tout n'est pas rose → problems."])

Q.sec("Reading: Literary Text")
Q.src(r"Reading 2 \textperiodcentered\ Literary Text \textperiodcentered\ «~L'écran de grand-père~» (extrait d'une nouvelle)", [
    r"La première fois que mon grand-père Abdou a fait un appel vidéo, il a collé le téléphone contre son oreille, comme d'habitude. «~Tu m'entends, Moussa~? Je ne te vois pas~!~» criait-il, tandis que moi, depuis Montréal, je ne voyais que le plafond de sa maison à Dakar.",
    r"Il lui a fallu une semaine pour apprendre à me regarder. Puis il a appris à envoyer des messages vocaux de cinq minutes, à transférer des proverbes à toute la famille et, pour mon malheur, à découvrir mes photos de soirée.",
    r"Un dimanche, il m'a appelé à six heures du matin, heure de Montréal. «~Je voulais que tu voies le manguier~», m'a-t-il dit en tournant le téléphone vers la cour. Je ne lui ai pas dit que je dormais. En regardant cet arbre, si loin et si proche, j'ai pensé que la technologie n'avait pas réduit la distance~: elle nous avait seulement donné une fenêtre pour nous y pencher.",
], 5)
Q.q("1.A.1 Detail", r"Quel était le problème du grand-père lors de son premier appel vidéo~?",
    "Il tenait le téléphone contre son oreille, comme pour un appel normal.", [("Il n'avait pas internet à Dakar.", "The call connected."),
                                                                              ("Il ne voulait pas parler à son petit-fils.", "He was eager to talk."),
                                                                              ("Il parlait une autre langue.", "No.")],
    "collé le téléphone contre son oreille.", "Detail (1.A.1).",
    ["il a collé le téléphone contre son oreille… Je ne te vois pas !"])
Q.q("1.B.3 Tone", r"Quel ton domine dans le deuxième paragraphe~?",
    "humoristique", [("tragique", "Nothing tragic happens."),
                     ("indigné", "The narrator jokes rather than complains."),
                     ("scientifique", "The text is personal.")],
    "pour mon malheur… messages de cinq minutes.", "Tone (1.B.3): exaggeration and mock complaint create humor.",
    ["pour mon malheur → playful complaint."])
Q.q("1.C.3 Inference", r"Pourquoi le narrateur n'a-t-il pas dit à son grand-père qu'il dormait~?",
    "parce qu'il ne voulait pas gâcher la joie de son grand-père", [("parce qu'il était fâché contre lui", "His reflection is tender."),
                                                                   ("parce qu'il ne savait pas utiliser le téléphone", "He is the expert."),
                                                                   ("parce que l'appel a été coupé", "No.")],
    "Tenderness.", "Inference (1.C.3): he lets his grandfather share the moment.",
    ["Je voulais que tu voies le manguier → he does not spoil it."])
Q.q("1.B.5 Word meaning", r"Dans le texte, «~nous y pencher~» évoque l'idée de",
    "regarder à travers une fenêtre vers un autre lieu", [("se dire au revoir", "No."),
                                                         ("voyager ensemble", "The point is that they cannot."),
                                                         ("se disputer", "No.")],
    "se pencher à une fenêtre = to lean out of a window.", "Word meaning (1.B.5): une fenêtre pour nous y pencher.",
    ["fenêtre + se pencher → look out through it."])
Q.q("1.C.2 Conclusion", r"Quelle conclusion le narrateur tire-t-il sur la technologie~?",
    "Elle permet de voir sa famille lointaine, mais elle n'efface pas la distance.", [("Elle a complètement supprimé la distance.", "He says it has not reduced the distance."),
                                                                                     ("Elle est inutile pour les personnes âgées.", "His grandfather learned to use it well."),
                                                                                     ("Elle devrait être interdite le dimanche.", "No.")],
    "n'avait pas réduit la distance : … une fenêtre.", "Conclusions (1.C.2): the final sentence states the reflection.",
    ["pas réduit la distance + une fenêtre."])

Q.sec("Listening: Audio Report")
Q.src(r"Listening 2 \textperiodcentered\ Audio Report (transcript) \textperiodcentered\ «~La banque dans la poche~»", [
    r"(JOURNALISTE) En Côte d'Ivoire, comme dans une grande partie de l'Afrique de l'Ouest, beaucoup d'habitants n'ont jamais eu de compte bancaire. Pourtant, ils paient, épargnent et envoient de l'argent tous les jours~: avec leur téléphone.",
    r"(JOURNALISTE) Le principe est simple~: on dépose de l'argent liquide chez un agent de quartier, souvent un petit commerçant, et cet argent apparaît sur le téléphone. On peut ensuite payer une facture ou envoyer de l'argent à sa famille au village en quelques secondes.",
    r"(ÉCONOMISTE) Pour les commerçantes des marchés, c'est une révolution. Elles n'ont plus besoin de transporter de grosses sommes en liquide, ce qui réduit les risques de vol.",
    r"(JOURNALISTE) Les experts rappellent toutefois quelques règles de prudence~: ne jamais communiquer son code secret, même à quelqu'un qui dit appeler de la part de l'opérateur.",
], 5)
Q.q("1.A.1 Detail", r"Comment fonctionne le paiement par téléphone, selon le reportage~?",
    "On dépose du liquide chez un agent, puis l'argent apparaît sur le téléphone.", [("On doit d'abord ouvrir un compte dans une grande banque.", "Many users have no bank account."),
                                                                                     ("On achète un téléphone spécial dans la capitale.", "Not stated."),
                                                                                     ("On envoie des chèques par la poste.", "No.")],
    "agent de quartier → téléphone.", "Detail (1.A.1) on the procedure.",
    ["on dépose de l'argent liquide chez un agent… cet argent apparaît sur le téléphone."])
Q.q("1.A.1 Detail", r"Selon l'économiste, quel avantage le paiement mobile apporte-t-il aux commerçantes~?",
    "Elles transportent moins d'argent liquide et risquent moins le vol.", [("Elles paient moins d'impôts.", "Not stated."),
                                                                           ("Elles vendent plus cher.", "Not stated."),
                                                                           ("Elles ferment le marché plus tôt.", "No.")],
    "Moins de liquide, moins de vol.", "Detail (1.A.1).",
    ["plus besoin de transporter de grosses sommes… réduit les risques de vol."])
Q.q("1.C.3 Inference", r"Que peut-on déduire au sujet des agents de quartier~?",
    "Ils rendent le service accessible là où il n'y a pas d'agence bancaire.", [("Ils travaillent pour le gouvernement.", "They are often small shopkeepers."),
                                                                               ("Ils interdisent les paiements en liquide.", "They take cash."),
                                                                               ("Ils réparent les téléphones.", "No.")],
    "Local shops = access points.", "Inference (1.C.3): shopkeepers in every neighborhood replace bank branches.",
    ["souvent un petit commerçant → nearby access."])
Q.q("1.B.1 Purpose", r"Quel est le but principal du reportage~?",
    "expliquer un service et ses avantages, avec des conseils de prudence", [("vendre un nouveau téléphone", "No sales pitch."),
                                                                            ("critiquer les banques ivoiriennes", "Not the focus."),
                                                                            ("raconter l'histoire de la monnaie", "No.")],
    "Explain + benefits + caution.", "Purpose (1.B.1): description, testimony and advice.",
    ["how it works → benefits → precautions."])
Q.q("1.C.2 Conclusion", r"Quelqu'un vous appelle en disant~: «~Je travaille pour votre opérateur, donnez-moi votre code secret.~» Selon les experts, que devez-vous faire~?",
    "refuser de donner son code", [("donner le code pour vérifier son compte", "That is exactly the scam they warn about."),
                                   ("envoyer le code par message", "Still sharing it."),
                                   ("donner seulement la moitié du code", "Never share it.")],
    "Never share the code.", "Conclusions (1.C.2): apply the experts' rule to a new case.",
    ["ne jamais communiquer son code secret, même à quelqu'un qui dit appeler de la part de l'opérateur."])

Q.frq(kind="Argumentative Essay", head=r"Question 3 \textperiodcentered\ Argumentative Essay \textperiodcentered\ 10 points \textperiodcentered\ 55 minutes", mins=55,
      directions=[r"Vous allez écrire un essai argumentatif pour un cours universitaire. Lisez le sujet et les sources écrites~; ensuite, écoutez la source audio (ici, la transcription). Écrivez un essai qui intègre des éléments des trois sources pour soutenir votre position. Indiquez les sources utilisées par leur numéro, leur titre ou leur auteur."],
      sources=[dict(title=r"Source 1 \textperiodcentered\ Article \textperiodcentered\ «~Un collège sans réseaux~»", paras=[
          r"Au collège Victor-Hugo de Rennes, les parents d'une classe de 6\textsuperscript{e} ont signé un pacte~: aucun de leurs enfants n'aurait de compte sur les réseaux sociaux avant 15 ans. «~Quand tout le monde s'engage, personne n'est exclu~», explique Sophie, une mère à l'origine du projet.",
          r"Un an plus tard, les enseignants observent moins de conflits nés en ligne et des élèves plus reposés. Mais certains enfants disent se sentir à l'écart lorsqu'ils retrouvent des amis d'autres collèges, qui, eux, échangent sur les réseaux."]),
               dict(title=r"Source 2 \textperiodcentered\ Graphique \textperiodcentered\ Effets ressentis par les 11--14 ans qui utilisent les réseaux sociaux", paras=[
          r"Enquête auprès de 3~000 jeunes en France, en Belgique et en Suisse (données fictives). Pourcentage qui déclare chaque effet."],
                    table=(["Effet déclaré", "Pourcentage"], [["Se sentir plus proche de ses amis", "64~\\%"], ["Dormir moins à cause des réseaux", "47~\\%"], ["Avoir déjà subi du cyberharcèlement", "21~\\%"], ["Se comparer négativement aux autres", "39~\\%"]])),
               dict(title=r"Source 3 \textperiodcentered\ Audio (transcription) \textperiodcentered\ «~Parents connectés~», émission de radio", paras=[
          r"(ANIMATEUR) Nous recevons la sociologue Nadia Benali. Faut-il interdire les réseaux sociaux aux moins de 15 ans~?",
          r"(NADIA BENALI) Une interdiction envoie un signal clair, et elle protège le sommeil et l'estime de soi des plus jeunes. Mais une loi ne suffit pas~: beaucoup d'enfants mentent sur leur âge en deux clics. Si on interdit sans éduquer, ils découvriront les réseaux seuls, sans adulte pour les guider.",
          r"(ANIMATEUR) Que proposez-vous~?",
          r"(NADIA BENALI) Retarder l'accès, oui, mais en même temps apprendre aux enfants, dès l'école primaire, à se protéger en ligne."])],
      prompt=[r"Sujet de l'essai~: \textbf{Faut-il interdire les réseaux sociaux aux moins de 15 ans~?}"],
      model=[r"Les réseaux sociaux font aujourd'hui partie de la vie de la plupart des adolescents, parfois dès 11 ans. Faut-il les leur interdire avant 15 ans~? À mon avis, il faut retarder l'accès aux réseaux sociaux jusqu'à 15 ans, à condition que cette règle s'accompagne d'une véritable éducation numérique.",
             r"Tout d'abord, les réseaux sociaux nuisent au bien-être des plus jeunes. D'après le graphique de la source 2, 47~\% des 11--14 ans qui les utilisent dorment moins à cause d'eux, et 39~\% se comparent négativement aux autres. Ces chiffres montrent que les risques touchent une grande partie des jeunes utilisateurs, et pas seulement une minorité. La sociologue Nadia Benali le confirme dans la source 3~: une interdiction protège «~le sommeil et l'estime de soi des plus jeunes~».",
             r"Ensuite, une règle collective évite l'exclusion. Dans la source 1, les parents d'une classe de Rennes se sont engagés ensemble, car, comme le dit Sophie, «~quand tout le monde s'engage, personne n'est exclu~». Un an plus tard, les enseignants constatent moins de conflits nés en ligne et des élèves plus reposés.",
             r"Certes, les réseaux ont aussi des avantages~: 64~\% des jeunes interrogés se sentent plus proches de leurs amis grâce à eux (source 2), et certains élèves de Rennes se sentent à l'écart. De plus, Nadia Benali rappelle que beaucoup d'enfants mentent sur leur âge. Cependant, ces limites prouvent non pas qu'il faut renoncer, mais qu'il faut éduquer~: retarder l'accès tout en apprenant aux enfants à se protéger, comme elle le propose.",
             r"En conclusion, si l'on interdisait les réseaux sociaux avant 15 ans tout en formant les élèves dès l'école primaire, on protégerait leur sommeil et leur confiance sans les laisser découvrir seuls le monde numérique."],
      rows=[("A Position", 1, "a clear, qualified position (delay access, provided there is digital education)", "only lists advantages and disadvantages"),
            ("B Source use", 2, "all three sources used accurately and named; percentages kept with their labels", "two sources, or misreading the chart"),
            ("C Argumentation", 2, "each claim explained with evidence (ces chiffres montrent, le confirme)", "quotes and numbers with no link to the claims"),
            ("D Organization", 2, "introduction, two claims, concession and rebuttal, conclusion", "one paragraph per source"),
            ("E Language control", 3, "varied structures: à condition que + subjunctive, si-clause, non pas… mais", "basic structures; copying the sources")],
      tips=["The position is conditional but clear (à condition que…).", "The concession uses the chart's positive figure (64%) and Source 3's warning, then answers them.",
            "Every source is named and paraphrased, with short quotations at most.", "The conclusion's si-clause (si l'on interdisait…, on protégerait) rounds off the argument."],
      ask="Write your essay in French (about 300–350 words), then mark it against each row.", lines=22)

GUIDE, QSET = G, Q
