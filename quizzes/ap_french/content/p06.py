from ap_wl.model import Doc

STEM = "06-global-contexts"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 6: Global Contexts", r"Unit 6 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 6 asks how global issues affect families and communities, and how people and governments respond. Its recommended contexts are global communication, the natural world, history, policy and planning, and transportation. This guide gives the vocabulary of the environment, history and public policy, the cases most often tested (the Paris Agreement, the Great Green Wall, the Congo rainforest, hydroelectricity in Quebec, the Revolution of 1789, decolonization, the Quiet Revolution, trams and low-emission zones), the language for proposing solutions, and an Argumentative Essay kit on counterarguments. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Solutions I can propose: \blank[10em]",
        short="Unit 6", sub="Global Contexts")

G.sec("The natural world")
G.tex(r"""
\begin{vocab}
l'environnement / la nature & environment / nature & \\
le réchauffement climatique & global warming & \\
la sécheresse / la désertification & drought / desertification & the Sahel \\
la forêt tropicale & rainforest & the Congo basin, the world's second-largest \\
l'hydroélectricité & hydroelectric power & almost all of Quebec's electricity \\
les énergies renouvelables & renewable energy & \\
la montée des eaux & rising sea level & \\
\end{vocab}

\textbf{Cases.} The Paris Agreement (COP21, 2015) set the goal of limiting warming to well below 2~°C. The Great Green Wall, launched by African countries in 2007, aims to restore land across the Sahel, from Senegal to Djibouti, by planting trees and reviving farmland. Quebec produces nearly all of its electricity from water, thanks to huge dams in the north.
""")
G.q("1 Nature", r"Quel est l'objectif de la Grande Muraille verte en Afrique~?",
    "restaurer les terres du Sahel et lutter contre la désertification", [("construire un mur pour protéger les frontières", "Despite the name, it is a belt of restored land, not a wall."),
                                                                          ("produire de l'électricité nucléaire", "No."),
                                                                          ("créer une autoroute entre le Sénégal et Djibouti", "No.")],
    "Great Green Wall = land restoration.", "Trees and farmland across the Sahel fight desertification and support villages.",
    ["Sahel + arbres → contre la désertification."])
G.q("1 Nature", r"The Paris Agreement (2015) set the goal of",
    "limiting global warming to well below 2 °C", [("banning all cars by 2020", "No."),
                                                     ("closing every coal mine within a year", "No."),
                                                     ("making French the language of the UN", "No.")],
    "Paris Agreement = below 2 °C.", "COP21 in Paris produced the agreement to keep warming well below 2 °C.",
    ["COP21 → 2 °C goal."])

G.sec("History and global communication")
G.tex(r"""
\begin{vocab}
la Révolution française & the French Revolution, 1789 & \\
la Déclaration des droits de l'homme et du citoyen & Declaration of the Rights of Man, 1789 & \\
la colonisation / la décolonisation & colonization / decolonization & \\
l'indépendance & independence & 1960, ``the year of Africa'': seventeen countries \\
la Révolution tranquille & the Quiet Revolution & Quebec, 1960s \\
le devoir de mémoire & the duty to remember & \\
la francophonie & the French-speaking world & TV5Monde, RFI \\
\end{vocab}

\textbf{Independence.} In 1960 seventeen African countries became independent, most of them former French colonies such as Senegal, Mali and Côte d'Ivoire; Algeria followed in 1962 after a long war. \textbf{The Quiet Revolution} transformed Quebec in the 1960s: a modern state, secular schools, and a new pride in being \emph{Québécois}.
""")
G.q("2 Histoire", r"Pourquoi appelle-t-on 1960 «~l'année de l'Afrique~»~?",
    "parce que dix-sept pays africains sont devenus indépendants cette année-là", [("parce que l'Afrique a accueilli les Jeux olympiques", "No."),
                                                                                   ("parce que la Grande Muraille verte a été achevée", "It began in 2007 and is unfinished."),
                                                                                   ("parce que l'Algérie a gagné la Coupe du monde", "No.")],
    "1960 → seventeen independences.", "Most of French West and Central Africa became independent in 1960.",
    ["1960 → indépendances."])
G.q("2 Histoire", r"What was the Quiet Revolution (la Révolution tranquille)?",
    "a period of rapid modernization in Quebec in the 1960s", [("a peaceful revolution in France in 1789", "1789 was violent and French."),
                                                              ("a protest movement in Senegal", "No."),
                                                              ("a new law on noise", "Literal misreading.")],
    "Quebec, 1960s.", "The Quiet Revolution modernized Quebec's state, schools and identity without violence.",
    ["tranquille + Québec + 1960s."])

G.sec("Policy, planning and transportation")
G.tex(r"""
\begin{vocab}
les transports en commun & public transportation & \\
le tramway & tram & back in many French cities since the 1980s \\
le TER (Dakar) & regional express train & Dakar's line opened in 2021 \\
la piste cyclable / le vélo en libre-service & bike lane / bike share & Vélib' in Paris since 2007 \\
la zone à faibles émissions (ZFE) & low-emission zone & older, polluting cars banned \\
le bouchon / l'embouteillage & traffic jam & \\
l'aménagement du territoire & regional planning & \\
\end{vocab}

\textbf{Cases.} Many French cities brought trams back from the 1980s on to reduce car traffic. Paris turned riverbanks of the Seine into a pedestrian promenade and built hundreds of kilometers of bike lanes. In 2023 France banned some domestic flights on routes where a train makes the trip in under two and a half hours. The perspective: public space and clean air are shared goods that planning must protect.
""")
G.q("3 Transports", r"Qu'est-ce qu'une ZFE~?",
    "une zone où les véhicules les plus polluants ne peuvent pas circuler", [("une zone réservée aux trains", "No."),
                                                                            ("une zone sans électricité", "No."),
                                                                            ("une zone franche sans impôts", "Not this meaning.")],
    "ZFE = low-emission zone.", "Zones à faibles émissions restrict older, polluting vehicles.",
    ["faibles émissions → pollution limits."])
G.q("3 Transports", r"Paris turned roads along the Seine into a pedestrian promenade. Which perspective does this practice reflect?",
    "Public space should serve people, not only cars.", [("Cars should have priority everywhere.", "The opposite."),
                                                       ("Rivers should be hidden from residents.", "The opposite."),
                                                       ("Only tourists should use the riverbanks.", "Residents use them.")],
    "Riverbanks for people.", "Practice (pedestrianized riverbanks) → perspective (shared public space, health).",
    ["roads → promenade → people first."])

G.sec("Structures: proposing solutions")
G.tex(r"""
\begin{compare}{Purpose}{Structure}{Example}
Necessity & il faut / il est nécessaire de + infinitive & Il faut économiser l'eau. \\
Urgency & il est urgent que + subjunctive & Il est urgent que les gouvernements agissent. \\
Recommendation & il faudrait que, on devrait + infinitive & On devrait investir dans les trains. \\
Condition & à condition que, pourvu que, à moins que (+ ne) + subjunctive & Rien ne changera à moins que chacun ne participe. \\
Purpose & pour que, afin que + subjunctive & On plante des arbres pour que la ville soit plus fraîche. \\
Regret & conditionnel passé & On aurait dû agir plus tôt. \\
\end{compare}

\begin{trap}
\emph{À moins que} often takes an expletive \emph{ne} with the subjunctive: \emph{à moins qu'il ne pleuve}. The \emph{ne} is not a negation.
\end{trap}
""")
G.q("4 Solutions", r"Choisissez la bonne forme~: Le projet ne réussira pas à moins que les habitants ne \blank.",
    "participent", [("participeront", "À moins que always takes the subjunctive."),
                    ("participer", "With a subject (les habitants), a conjugated verb is needed."),
                    ("participaient", "The imparfait indicative does not follow à moins que.")],
    "à moins que (ne) + subjunctive.", "Conjunctions of condition and purpose (à moins que, à condition que, pour que) always take the subjunctive; the ne is expletive.",
    ["à moins que… ne → participent (subjonctif)."])
G.q("4 Solutions", r"Which sentence proposes a solution politely and clearly?",
    "Il faudrait multiplier les pistes cyclables pour que plus de gens laissent leur voiture.", [("Les pistes cyclables.", "A fragment, not a proposal."),
                                                                                                ("Les bouchons, ça m'est égal.", "Indifference, not a solution."),
                                                                                                ("Les bouchons sont un problème grave et très mauvais.", "States the problem, proposes nothing.")],
    "Il faudrait + infinitive + pour que.", "A conditional recommendation plus a purpose clause makes a clear, polite proposal.",
    ["il faudrait (recommendation) + pour que (purpose)."])

G.sec("Task kit: answering the other side")
G.tex(r"""
Global-context essays (\emph{Faut-il interdire les vols courts~?}, \emph{Faut-il privilégier l'environnement sur l'emploi~?}) almost always come with one source that disagrees with you. Use it: a counterargument answered well shows argumentation and earns credit for that source.

\begin{terms}
Concede & \emph{Certes, \ldots / Il faut reconnaître que\ldots} + the opposing point with its source \\
Answer & \emph{Cependant, \ldots / Néanmoins, \ldots} + evidence from another source or a solution \\
Limit & \emph{à condition que, pourvu que} + subjunctive: under what conditions your position holds \\
\end{terms}

\begin{keyidea}[Qualified positions]
\emph{Il faut interdire les vols courts, à condition qu'il existe un train rapide et abordable} is a clear position (Row A) that already includes the reply to the strongest objection.
\end{keyidea}
""")
G.q("5 Essai", r"A source says a flight ban hurt a regional business at first. How should an essay in favor of the ban use this source?",
    "concede the point and answer it with evidence or a solution", [("ignore it so the essay stays one-sided", "Ignoring a source loses source-use points."),
                                                                     ("change position to agree with it", "One objection does not require abandoning a position."),
                                                                     ("quote it with no comment", "Evidence without explanation does not earn argumentation credit.")],
    "Concede + answer.", "Answering the opposing source strengthens argumentation and still counts toward using all three sources.",
    ["Certes… Cependant…"])
G.q("5 Essai", r"Choisissez la bonne forme~: Je soutiens cette mesure, à condition que l'État \blank\ des trains moins chers.",
    "propose", [("proposera", "À condition que takes the subjunctive."),
                ("proposer", "A conjugated verb is needed."),
                ("proposait", "The imparfait indicative cannot follow à condition que.")],
    "à condition que + subjunctive.", "À condition que (provided that) → subjunctive; the subjunctive of proposer (il) is propose.",
    ["condition → propose (subjonctif)."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 6: Global Contexts: Question Set", r"Unit 6 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Interview and an Instructional Guidance for listening, an Article and an Article and Chart for reading) on the Great Green Wall, trams and new trains, renewable energy and recycling, followed by an Argumentative Essay with three sources and the 10-point scoring guide. As on the exam, questions and choices are in French; listening sources are printed as transcripts. All sources and data are original and fictional, written for practice. Allow about 25 minutes for the multiple choice and 55 minutes for the essay.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Essay: \blank\ / 10 \qquad Target: 15+ MCQ and 7+ essay \qquad Pace: 75 s per item",
        short="Unit 6", sub="Global Contexts")

Q.sec("Listening: Interview")
Q.src(r"Listening 1 \textperiodcentered\ Interview (transcript) \textperiodcentered\ Un agronome sénégalais et la Grande Muraille verte", [
    r"(JOURNALISTE) Monsieur Ndiaye, vous travaillez depuis quinze ans sur la Grande Muraille verte, dans le nord du Sénégal. Qu'avez-vous observé~?",
    r"(M. NDIAYE) Au début, on plantait beaucoup d'arbres, mais une grande partie mourait dès la première saison sèche. On a compris qu'il ne suffisait pas de planter~: il fallait que les villages s'occupent des jeunes arbres.",
    r"(JOURNALISTE) Comment avez-vous impliqué les villages~?",
    r"(M. NDIAYE) Nous avons créé des jardins polyvalents, gérés surtout par des femmes. On y cultive des légumes et des arbres fruitiers, comme le jujubier. Les familles ont ainsi un intérêt direct à protéger les plantations~: elles mangent et vendent ce qu'elles produisent.",
    r"(JOURNALISTE) Et l'avenir~?",
    r"(M. NDIAYE) Le désert n'est pas une fatalité. Mais aucun mur, même vert, ne tiendra si les gens qui vivent à côté n'en profitent pas.",
], 5)
Q.q("1.A.1 Detail", r"Quel problème M. Ndiaye a-t-il observé au début du projet~?",
    "Beaucoup d'arbres mouraient pendant la première saison sèche.", [("Les villages refusaient de planter des arbres.", "Not stated."),
                                                                       ("Il n'y avait pas assez de graines.", "Not stated."),
                                                                       ("Les arbres grandissaient trop vite.", "The opposite.")],
    "mourait dès la première saison sèche.", "Detail (1.A.1).",
    ["une grande partie mourait dès la première saison sèche."])
Q.q("1.C.3 Inference", r"Pourquoi les jardins polyvalents ont-ils aidé le projet~?",
    "parce que les familles profitent directement des plantations et ont donc intérêt à les protéger", [("parce qu'ils remplacent complètement les arbres", "They include fruit trees."),
                                                                                                         ("parce qu'ils sont gérés par l'État", "Mainly by women from the villages."),
                                                                                                         ("parce qu'ils attirent les touristes", "Not stated.")],
    "Direct benefit → protection.", "Inference (1.C.3): people protect what feeds and pays them.",
    ["elles mangent et vendent ce qu'elles produisent → intérêt direct."])
Q.q("1.B.4 Organization", r"Comment l'agronome présente-t-il l'évolution du projet~?",
    "Il décrit une erreur du début, puis la solution trouvée.", [("Il raconte l'histoire du Sahara depuis l'Antiquité.", "No."),
                                                                ("Il compare le Sénégal et la France.", "No."),
                                                                ("Il énumère des chiffres sur le climat.", "No figures.")],
    "Au début… On a compris… Nous avons créé…", "Organization (1.B.4): problem → lesson → solution.",
    ["mistake → lesson → gardens."])
Q.q("1.B.3 Point of view", r"Selon M. Ndiaye, à quelle condition la Grande Muraille verte réussira-t-elle~?",
    "si les habitants en profitent", [("si l'on construit un vrai mur", "Aucun mur, même vert…"),
                                     ("si l'on arrête de planter", "No."),
                                     ("si les pluies augmentent", "Not his condition.")],
    "si les gens… en profitent.", "Point of view (1.B.3): his final sentence.",
    ["ne tiendra si les gens… n'en profitent pas."])
Q.q("1.B.5 Word meaning", r"Que veut dire «~le désert n'est pas une fatalité~»~?",
    "qu'on peut agir contre l'avancée du désert", [("que le désert est dangereux", "Not the meaning."),
                                                   ("que le désert va disparaître tout seul", "No."),
                                                   ("qu'il ne faut rien faire", "The opposite.")],
    "fatalité = something inevitable.", "Word meaning (1.B.5): not a fatalité → can be changed.",
    ["pas une fatalité → not inevitable."])

Q.sec("Reading: Article")
Q.src(r"Reading 1 \textperiodcentered\ Article \textperiodcentered\ «~Des villes qui se déplacent autrement~»", [
    r"Pendant des décennies, les villes françaises se sont développées autour de la voiture. Puis, à partir des années 1980, le tramway, disparu après la guerre, a fait son retour~: Nantes, Grenoble, Strasbourg, puis des dizaines d'autres villes. Plus silencieux qu'un bus, il a aussi servi à réaménager les centres, avec des trottoirs plus larges et des arbres.",
    r"En Afrique de l'Ouest, Dakar a choisi un autre chemin. Le TER, un train express régional ouvert en 2021, relie le centre-ville aux banlieues de l'est, où vivent des centaines de milliers de travailleurs. Pour beaucoup, un trajet qui prenait plus d'une heure dans les embouteillages ne dure plus que quelques dizaines de minutes.",
    r"Les urbanistes rappellent cependant que les rails ne suffisent pas. «~Un tram ne transforme pas un quartier s'il n'apporte pas aussi des écoles, des commerces et des espaces publics~», explique l'architecte Awa Sy. «~La mobilité est une porte~; ce qui compte, c'est ce qu'il y a derrière.~»",
], 5)
Q.q("1.B.1 Main idea", r"Quelle est l'idée principale de l'article~?",
    "Des villes cherchent des alternatives à la voiture, mais le transport seul ne suffit pas.", [("Les villes doivent interdire toutes les voitures.", "Not proposed."),
                                                                                                  ("Le tramway est un échec en France.", "Dozens of cities adopted it."),
                                                                                                  ("Dakar a construit un tramway comme Nantes.", "Dakar built a regional train.")],
    "Alternatives + limits.", "Main idea (1.B.1): two examples, then the urbanists' caveat.",
    ["Paragraphs 1–2 examples; 3 les rails ne suffisent pas."])
Q.q("1.A.1 Detail", r"Selon l'article, à partir de quand le tramway a-t-il fait son retour en France~?",
    "à partir des années 1980", [("juste après la guerre", "It disappeared after the war."),
                                 ("en 2021", "2021 is the Dakar TER."),
                                 ("au XIX\\textsuperscript{e} siècle", "No.")],
    "années 1980.", "Detail (1.A.1): keep the dates apart.",
    ["à partir des années 1980, le tramway… a fait son retour."])
Q.q("1.A.1 Detail", r"Qu'est-ce que le TER a changé pour beaucoup d'habitants de Dakar~?",
    "Il a fortement réduit la durée de leur trajet.", [("Il a augmenté le prix des logements du centre.", "Not stated."),
                                                      ("Il a remplacé toutes les routes.", "No."),
                                                      ("Il a obligé les familles à déménager.", "No.")],
    "plus d'une heure → quelques dizaines de minutes.", "Detail (1.A.1).",
    ["ne dure plus que quelques dizaines de minutes."])
Q.q("1.B.3 Point of view", r"Que pense l'architecte Awa Sy~?",
    "que les transports doivent être accompagnés de services et d'espaces publics", [("que les tramways sont inutiles", "She does not reject them."),
                                                                                     ("que la technologie résout tout", "She says rails are not enough."),
                                                                                     ("que les commerces sont plus importants que les écoles", "No ranking.")],
    "La mobilité est une porte.", "Point of view (1.B.3).",
    ["s'il n'apporte pas aussi des écoles, des commerces et des espaces publics."])
Q.q("1.C.3 Inference", r"Que signifie «~la mobilité est une porte~; ce qui compte, c'est ce qu'il y a derrière~»~?",
    "que le transport donne accès à des possibilités, et que ces possibilités sont l'essentiel", [("qu'il faut installer plus de portes dans les gares", "Literal misreading."),
                                                                                                ("que la mobilité ne sert à rien", "A door is useful."),
                                                                                                ("que les quartiers doivent être fermés", "No.")],
    "Door = access.", "Figurative meaning (1.C.3): what matters is what people can reach.",
    ["porte (access) → opportunities behind it."])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 2 \textperiodcentered\ Article and Chart \textperiodcentered\ «~D'où vient notre électricité~?~»", [
    r"Le Québec est souvent cité comme un modèle d'énergie propre~: presque toute son électricité vient de grands barrages hydroélectriques construits dans le nord de la province. D'autres régions misent sur le vent ou le soleil.",
    r"Mais dépendre de l'eau comporte des risques. Les années de sécheresse, les barrages produisent moins et il faut acheter de l'électricité ailleurs ou brûler davantage de combustibles fossiles. C'est pourquoi les experts recommandent de diversifier~: combiner hydraulique, éolien et solaire pour que la faiblesse d'une source ne prive personne de courant.",
], 5, table=(["Région (données fictives)", "Hydraulique", "Éolien", "Solaire", "Fossile"],
             [["Région A", "72~\\%", "15~\\%", "3~\\%", "10~\\%"], ["Région B", "30~\\%", "38~\\%", "4~\\%", "28~\\%"], ["Région C", "40~\\%", "35~\\%", "20~\\%", "5~\\%"]]),
      note="Origine de l'électricité dans trois régions (données fictives).")
Q.q("1.A.2 Data", r"Selon le tableau, quelle région dépend le plus de l'hydraulique~?",
    "la région A", [("la région B", "B gets most from wind (38%)."),
                    ("la région C", "C has 40% hydro, less than A."),
                    ("les trois à égalité", "The shares differ.")],
    "Région A: 72%.", "Data (1.A.2).",
    ["72 % > 40 % > 30 %."])
Q.q("1.C.1 Connect", r"D'après l'article, quelle région du tableau serait la plus vulnérable en cas de sécheresse~?",
    "la région A, parce qu'elle dépend surtout de l'eau", [("la région C, parce qu'elle utilise le solaire", "Solar does not depend on rain."),
                                                          ("la région B, parce qu'elle utilise plus de fossile", "Drought hurts hydro, not fossil fuels."),
                                                          ("aucune, car la sécheresse n'affecte pas l'électricité", "The article says it does.")],
    "Drought hurts hydro → A.", "Connect (1.C.1): apply the article's risk to the table.",
    ["sécheresse → barrages produisent moins → most hydro-dependent = A."])
Q.q("1.C.2 Conclusion", r"Quelle région suit le mieux la recommandation des experts~?",
    "la région C, parce qu'elle combine plusieurs sources et utilise peu de fossile", [("la région A, parce qu'elle utilise beaucoup d'hydraulique", "Concentration is the risk the experts warn about."),
                                                                                       ("la région B, parce qu'elle utilise 28~\\% de fossile", "High fossil use is not the goal."),
                                                                                       ("aucune ne la suit", "C does.")],
    "Diversify → C.", "Conclusions (1.C.2): the recommendation (diversifier) matches C's balanced mix.",
    ["C: 40/35/20/5 → diversified."])
Q.q("1.B.5 Word meaning", r"Dans l'article, «~diversifier~» signifie",
    "utiliser plusieurs sources différentes", [("économiser l'énergie", "Not the meaning."),
                                               ("construire plus de barrages", "That would increase concentration."),
                                               ("vendre de l'électricité à l'étranger", "No.")],
    "diversifier = diversify.", "Word meaning (1.B.5): explained after the colon.",
    ["combiner hydraulique, éolien et solaire."])
Q.q("1.A.1 Detail", r"D'où vient presque toute l'électricité du Québec, selon l'article~?",
    "de grands barrages hydroélectriques", [("de centrales nucléaires", "No."),
                                            ("de panneaux solaires", "No."),
                                            ("de centrales au charbon", "No.")],
    "barrages.", "Detail (1.A.1).",
    ["presque toute son électricité vient de grands barrages."])

Q.sec("Listening: Instructional Guidance")
Q.src(r"Listening 2 \textperiodcentered\ Instructional Guidance (transcript) \textperiodcentered\ Un message de la mairie sur le tri des déchets", [
    r"(VOIX) À partir du 1\textsuperscript{er} janvier, la ville simplifie le tri. Voici comment faire, en quatre étapes.",
    r"(VOIX) Premièrement, tous les emballages et tous les papiers vont dans la poubelle jaune~: bouteilles en plastique, pots de yaourt, cartons, journaux. Inutile de les laver~: il suffit de bien les vider. Deuxièmement, le verre va dans les conteneurs de quartier, jamais dans la poubelle jaune.",
    r"(VOIX) Troisièmement, les restes de repas et les épluchures vont dans le nouveau bac marron, qui sera collecté deux fois par semaine pour fabriquer du compost. Enfin, les piles et les petits appareils électriques doivent être déposés en déchetterie ou dans les magasins qui les reprennent.",
    r"(VOIX) Rappelez-vous~: un déchet bien trié, c'est une ressource. Mieux nous trierons, moins la ville paiera pour incinérer, et plus nous économiserons ensemble.",
], 5)
Q.q("1.A.1 Detail", r"Où faut-il mettre une bouteille en plastique vide~?",
    "dans la poubelle jaune", [("dans le bac marron", "That is for food scraps."),
                               ("dans les conteneurs à verre", "Glass only."),
                               ("à la déchetterie", "That is for batteries and small appliances.")],
    "Emballages → jaune.", "Instructional Guidance: match each item to its bin.",
    ["tous les emballages… vont dans la poubelle jaune."])
Q.q("1.A.1 Detail", r"Faut-il laver les emballages avant de les jeter~?",
    "Non, il suffit de bien les vider.", [("Oui, il faut les laver à l'eau chaude.", "Inutile de les laver."),
                                         ("Oui, mais seulement le verre.", "Not stated."),
                                         ("Non, il faut les mettre dans le bac marron.", "Packaging goes in the yellow bin.")],
    "Inutile de les laver.", "Detail (1.A.1).",
    ["Inutile de les laver : il suffit de bien les vider."])
Q.q("1.B.5 Word meaning", r"Dans le message, «~les épluchures~» sont",
    "les peaux des fruits et des légumes qu'on enlève", [("les vieux journaux", "Those go in the yellow bin."),
                                                        ("les piles usagées", "Those go to the déchetterie."),
                                                        ("les bouteilles en verre", "Those go in the glass containers.")],
    "épluchures = peelings.", "Word meaning (1.B.5): listed with restes de repas for compost.",
    ["restes de repas et épluchures → food waste."])
Q.q("1.B.2 Audience", r"À qui ce message s'adresse-t-il~?",
    "aux habitants de la ville", [("aux employés des magasins seulement", "Shops are one drop-off point."),
                                  ("aux agriculteurs", "No."),
                                  ("aux touristes", "No.")],
    "la ville simplifie le tri…", "Audience (1.B.2): a city announcement to residents.",
    ["mairie → residents."])
Q.q("1.C.3 Inference", r"Pourquoi la mairie dit-elle que «~mieux nous trierons, plus nous économiserons~»~?",
    "parce que brûler les déchets coûte cher à la ville, donc aux habitants", [("parce que les habitants seront payés pour trier", "Not stated."),
                                                                              ("parce que le compost est vendu très cher", "Not stated."),
                                                                              ("parce que les poubelles jaunes sont gratuites", "Not the point.")],
    "Less incineration → lower costs.", "Inference (1.C.3): moins la ville paiera pour incinérer.",
    ["better sorting → less incineration → savings."])

Q.frq(kind="Argumentative Essay", head=r"Question 3 \textperiodcentered\ Argumentative Essay \textperiodcentered\ 10 points \textperiodcentered\ 55 minutes", mins=55,
      directions=[r"Vous allez écrire un essai argumentatif pour un cours universitaire. Lisez le sujet et les sources écrites~; ensuite, écoutez la source audio (ici, la transcription). Écrivez un essai qui intègre des éléments des trois sources pour soutenir votre position. Indiquez les sources utilisées par leur numéro, leur titre ou leur auteur."],
      sources=[dict(title=r"Source 1 \textperiodcentered\ Article \textperiodcentered\ «~Le train plutôt que l'avion~»", paras=[
          r"Depuis 2023, la France interdit certains vols intérieurs lorsqu'un train permet de faire le même trajet en moins de deux heures et demie. Entre Paris et Bordeaux, par exemple, les voyageurs prennent désormais le TGV.",
          r"«~Je mets à peine plus de temps qu'en avion, si l'on compte l'aéroport, et je peux travailler pendant le trajet~», témoigne Claire, consultante. Les défenseurs de la mesure soulignent qu'un trajet en train émet beaucoup moins de gaz à effet de serre qu'un vol.",
          r"Les critiques, eux, jugent la mesure surtout symbolique~: elle ne concerne que quelques lignes, et les vols longs, bien plus polluants, ne sont pas touchés."]),
               dict(title=r"Source 2 \textperiodcentered\ Graphique \textperiodcentered\ Émissions de CO\textsubscript{2} par passager pour un trajet de 500 km", paras=[
          r"Estimations moyennes (données fictives). Kilogrammes de CO\textsubscript{2} par passager."],
                    table=(["Mode de transport", "kg de CO\\textsubscript{2}"], [["Avion", "120"], ["Voiture (une personne)", "95"], ["Car (autobus)", "15"], ["Train à grande vitesse", "3"]])),
               dict(title=r"Source 3 \textperiodcentered\ Audio (transcription) \textperiodcentered\ «~Voix des régions~», radio locale", paras=[
          r"(ANIMATRICE) Nous recevons Jérôme Martin, chef d'une petite entreprise dans une ville moyenne du Massif central.",
          r"(JÉRÔME) Pour nous, l'avion n'était pas un luxe. Notre ville n'a pas de TGV~; pour rejoindre Paris, le train met plus de quatre heures. Si on supprimait aussi notre ligne aérienne, mes clients étrangers ne viendraient plus.",
          r"(ANIMATRICE) La loi actuelle ne concerne pourtant pas votre ligne.",
          r"(JÉRÔME) Justement~: je ne suis pas contre la mesure là où le train est rapide. Mais avant d'aller plus loin, il faut construire des trains dignes de ce nom pour les régions."])],
      prompt=[r"Sujet de l'essai~: \textbf{Faut-il interdire les vols intérieurs quand un train rapide existe~?}"],
      model=[r"Le transport aérien est l'un des modes de déplacement les plus polluants. Faut-il pour autant interdire les vols intérieurs lorsqu'un train rapide peut les remplacer~? À mon avis, oui, à condition que cette interdiction s'accompagne d'investissements dans le train pour toutes les régions.",
             r"Tout d'abord, l'écart de pollution entre l'avion et le train est énorme. Le graphique de la source 2 indique que, pour un trajet de 500 kilomètres, un passager émet 120 kg de CO\textsubscript{2} en avion, contre seulement 3 kg en train à grande vitesse. Ces chiffres montrent que remplacer un vol par un train réduit les émissions de façon spectaculaire. La source 1 confirme que c'est l'argument principal des défenseurs de la mesure.",
             r"Ensuite, pour les trajets concernés, le train n'est pas un sacrifice. Comme le raconte Claire dans la source 1, entre Paris et Bordeaux, elle met «~à peine plus de temps qu'en avion~» si l'on compte l'aéroport, et elle peut travailler pendant le voyage.",
             r"Certes, la mesure a des limites. Les critiques cités dans la source 1 la jugent symbolique, et Jérôme Martin, dans la source 3, rappelle que sa ville n'a pas de TGV et que, sans avion, ses clients étrangers ne viendraient plus. Néanmoins, Jérôme lui-même n'est «~pas contre la mesure là où le train est rapide~»~; il demande seulement de meilleurs trains pour les régions. Ces critiques ne remettent donc pas en cause le principe, mais montrent qu'il faut l'accompagner.",
             r"En conclusion, si l'État interdisait les vols courts tout en modernisant le réseau ferroviaire des régions, la France réduirait ses émissions sans abandonner les territoires éloignés."],
      rows=[("A Position", 1, "a clear, qualified position (yes, provided trains are improved everywhere)", "only lists both sides"),
            ("B Source use", 2, "all three sources used accurately and named; the chart's units kept straight", "two sources, or misreading the chart"),
            ("C Argumentation", 2, "claims explained with evidence; the opposing source answered", "summaries with no link to the claims"),
            ("D Organization", 2, "introduction, two claims, concession and rebuttal, conclusion", "one paragraph per source"),
            ("E Language control", 3, "varied structures: à condition que + subjunctive, si-clause, ne… que, non pas… mais", "basic structures; copied phrases")],
      tips=["The qualified position already answers the strongest objection.", "The opposing source (Jérôme) is conceded and then shown to support the principle.",
            "The chart is quoted with its units (kg de CO2 par passager).", "The conclusion proposes a concrete condition drawn from Source 3."],
      ask="Write your essay in French (about 300–350 words), then mark it against each row.", lines=22)

GUIDE, QSET = G, Q
