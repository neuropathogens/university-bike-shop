from ap_wl.model import Doc

STEM = "05-contemporary-life"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 5: Contemporary Life", r"Unit 5 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 5 asks how traditions shape daily life today: school and work, food and health, leisure, sports and travel. Its recommended contexts are education and career, entertainment and media, food and health, pop culture, sports and leisure, and travel and tourism. This guide gives the vocabulary of daily life, the practices most often tested (the baccalauréat and the cégep, meal times and the goûter, the French gastronomic meal, the Nutri-Score, five weeks of paid holiday, the Tour de France), the subjunctive in relative clauses and the imperative, and a second Project Presentation kit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Practices I can link to a perspective: \blank[8em]",
        short="Unit 5", sub="Contemporary Life")

G.sec("Education and careers")
G.tex(r"""
\begin{vocab}
le collège / le lycée & middle school / high school & \emph{collège} is not college \\
le baccalauréat (le bac) & national exam at the end of high school & \\
Parcoursup & national platform for applying to higher education & \\
les grandes écoles & selective schools (engineering, business, public service) & entered after \emph{classes préparatoires} \\
le cégep & Quebec college between high school and university & \\
l'alternance / l'apprentissage & work-study / apprenticeship & \\
le chômage & unemployment & \\
la fuite des cerveaux & brain drain & \\
\end{vocab}

\textbf{Practices and perspectives.} French public universities charge low fees, reflecting a view of higher education as a public service. The bac is a national rite of passage; results are published and celebrated. In Quebec, almost all students attend a free public cégep after high school, either for two years before university or for a three-year technical program.
""")
G.q("1 Éducation", r"Une élève québécoise dit~: «~L'an prochain, j'entre au cégep~». Où va-t-elle étudier~?",
    "dans un établissement entre l'école secondaire et l'université", [("dans une école primaire", "No."),
                                                                     ("dans une grande école de commerce", "That is a French institution."),
                                                                     ("dans une entreprise, comme apprentie", "Not the meaning.")],
    "Cégep = Quebec college.", "The cégep comes after secondary school and before university or a technical career.",
    ["cégep → between high school and university."])
G.q("1 Éducation", r"French public universities charge low tuition. Which perspective does this practice most directly reflect?",
    "Higher education is a public service open to all.", [("Universities should be run as private businesses.", "The opposite view."),
                                                         ("Only wealthy families should study.", "Low fees open access."),
                                                         ("Students should not choose a major.", "Unrelated.")],
    "Low fees ↔ education as a public service.", "Practice (low fees) linked to a perspective (equal access) earns culture credit.",
    ["Practice: low tuition.", "Perspective: public service."])

G.sec("Food and health")
G.tex(r"""
\begin{vocab}
le petit-déjeuner / le déjeuner / le goûter / le dîner & breakfast / lunch / afternoon snack / dinner & in Quebec: déjeuner, dîner, souper \\
le repas gastronomique des Français & the French gastronomic meal & UNESCO intangible heritage, 2010 \\
la cantine & school cafeteria & a full multi-course lunch \\
le Nutri-Score & A--E nutrition label on food packages & France, since 2017 \\
la Sécurité sociale / la carte Vitale & public health insurance / health card & \\
le thiéboudienne (ceebu jën) & Senegal's national dish of fish and rice & UNESCO, 2021 \\
la poutine & fries, cheese curds and gravy & Quebec \\
\end{vocab}

\textbf{Schedules.} In France, lunch is usually between noon and 2 p.m. and dinner around 8 p.m.; children have a \emph{goûter} after school. In Quebec, the same words shift: \emph{déjeuner} is breakfast, \emph{dîner} is lunch and \emph{souper} is dinner. The gastronomic meal (aperitif, starter, main course, cheese, dessert, wine chosen to match) reflects the value placed on eating together and taking one's time.
""")
G.q("2 Alimentation", r"Au Québec, à quel repas correspond le «~dîner~»~?",
    "au repas de midi", [("au repas du soir", "In Quebec, the evening meal is le souper."),
                         ("au petit-déjeuner", "In Quebec, breakfast is le déjeuner."),
                         ("au goûter de l'après-midi", "No.")],
    "Quebec: déjeuner–dîner–souper.", "The same meal names shift between France and Quebec.",
    ["Quebec dîner = noon meal."])
G.q("2 Alimentation", r"What does a Nutri-Score of E on a package tell the buyer?",
    "the product has the least favorable nutritional quality on the scale", [("the product is organic", "The score is about nutrition, not farming methods."),
                                                                            ("the product is made in Europe", "E is a grade, not a region."),
                                                                            ("the product is on sale", "Unrelated.")],
    "A (best) → E (worst).", "The Nutri-Score grades packaged food from A (dark green) to E (dark orange).",
    ["E → lowest grade."])
G.q("2 Alimentation", r"Which perspective does the UNESCO listing of the French gastronomic meal most directly reflect?",
    "Sharing a long meal together is part of social life and identity.", [("Meals should be eaten quickly and alone.", "The opposite."),
                                                                         ("Only restaurants matter in French cuisine.", "The listing is about a social practice at home."),
                                                                         ("Food should be cheap above all.", "Not the point.")],
    "Meal as social ritual.", "The heritage listed is a practice (the structured, shared meal), not a recipe.",
    ["courses + time + company → shared ritual."])

G.sec("Leisure, sports and travel")
G.tex(r"""
\begin{vocab}
les congés payés & paid holidays & five weeks in France since 1982 \\
les grandes vacances & summer holidays & \\
la colonie de vacances (la colo) & summer camp & \\
le Tour de France & cycling race, since 1903 & \\
la pétanque & boules game & southern France \\
le hockey & ice hockey & Quebec's passion \\
le tourisme durable / le surtourisme & sustainable tourism / overtourism & \\
\end{vocab}

\textbf{Paid holidays} began in 1936 with two weeks under the Popular Front and grew to five weeks by 1982. The practice reflects a perspective that rest and leisure are rights, not luxuries; in August many businesses close and cities empty as families leave for the coast or the mountains.
""")
G.q("3 Loisirs", r"Depuis 1982, combien de semaines de congés payés les salariés français ont-ils au minimum~?",
    "cinq", [("deux", "Two weeks was the 1936 law."),
             ("trois", "Three weeks came in 1956."),
             ("dix", "No.")],
    "5 weeks since 1982.", "2 (1936) → 3 (1956) → 4 (1969) → 5 (1982).",
    ["1982 → cinq semaines."])
G.q("3 Loisirs", r"Which perspective do France's five weeks of paid holiday most directly reflect?",
    "Rest and leisure are workers' rights.", [("Work should never stop.", "The opposite."),
                                             ("Only children need holidays.", "No."),
                                             ("Tourism should be banned.", "No.")],
    "Paid holidays ↔ leisure as a right.", "The law (product) and the August exodus (practice) reflect the value of rest.",
    ["congés payés → droit au repos."])

G.sec("Structures: relative clauses, the imperative, manquer")
G.tex(r"""
\begin{compare}{Structure}{Use}{Example}
Subjunctive in relative clauses & the thing sought may not exist & Je cherche un travail qui \emph{soit} flexible. \\
Indicative in relative clauses & it exists and is known & J'ai un travail qui \emph{est} flexible. \\
Il n'y a personne qui / aucun & non-existent & Il n'y a aucun restaurant qui \emph{ouvre} à 18 heures. \\
Imperative + pronouns & affirmative: verb-pronoun; negative: ne + pronoun + verb & Mange-les~! Ne les mange pas~! Donne-le-moi. \\
manquer à & to be missed by & Tu me manques (= I miss you). \\
\end{compare}

\begin{trap}
\emph{Tu me manques} means \emph{I miss you}: the person missed is the subject. \emph{Mes amis me manquent} = I miss my friends.
\end{trap}
""")
G.q("4 Structures", r"Choisissez la bonne forme~: Je cherche une formation qui me \blank\ de voyager.",
    "permette", [("permet", "The training is not yet known or chosen, so the relative clause takes the subjunctive."),
                 ("permettra", "The future does not fit an unknown antecedent here."),
                 ("permettre", "A conjugated verb is needed after qui.")],
    "Unknown antecedent → subjunctive.", "When the noun described is hypothetical (une formation qui…), the relative clause can take the subjunctive.",
    ["une formation (not yet found) → permette."])
G.q("4 Structures", r"Comment dit-on «~I miss my family~»~?",
    "Ma famille me manque.", [("Je manque ma famille.", "That means I miss (fail to catch) my family, as you miss a train."),
                              ("Je me manque ma famille.", "Not a structure."),
                              ("Ma famille manque à moi.", "Use the pronoun me before the verb.")],
    "X me manque = I miss X.", "With manquer à, the person or thing missed is the subject.",
    ["what I miss (ma famille) = subject → me manque."])

G.sec("Task kit: developing a factor in the presentation")
G.tex(r"""
Each factor in the Project Presentation should follow the same four steps, about 40 seconds in all:

\begin{terms}
1 Claim & \emph{Le deuxième facteur, c'est la radio.} \\
2 Evidence & one specific fact or example from your research: a place, a date, a name, a practice \\
3 Perspective & \emph{Cela reflète\ldots / Cela montre l'importance de\ldots} \\
4 Link & connect to the prompt or the next factor: \emph{C'est pourquoi\ldots / De plus\ldots} \\
\end{terms}

\begin{keyidea}[Change over time]
Prompts often ask how a tradition has changed. Use time markers (\emph{dans les années soixante, de nos jours, à partir de}) and the passé composé / imparfait contrast: \emph{Autrefois, on écoutait les chansonniers dans les boîtes à chansons~; aujourd'hui, on les découvre sur les plateformes}.
\end{keyidea}
""")
G.q("5 Présentation", r"Which sequence develops a factor most completely?",
    "claim, specific example from research, perspective it reflects, link to the next idea", [("claim, then the next factor", "No detail or perspective."),
                                                                                              ("example, then a personal opinion", "No claim or perspective."),
                                                                                              ("a definition of the genre only", "No claim, example or perspective.")],
    "Claim → evidence → perspective → link.", "Full task and culture credit come from detailed factors that reach a perspective.",
    ["All four steps → full development."])
G.q("5 Présentation", r"Choisissez la bonne forme~: Autrefois, on \blank\ les chansonniers dans de petites salles~; aujourd'hui, on les écoute en ligne.",
    "écoutait", [("a écouté", "A habitual past description takes the imparfait."),
                 ("écoute", "Autrefois contrasts with aujourd'hui; the first clause is past."),
                 ("écoutera", "The future contradicts autrefois.")],
    "Autrefois + imparfait for habit.", "Contrast past habit (imparfait) with the present.",
    ["autrefois (habit) → écoutait."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 5: Contemporary Life: Question Set", r"Unit 5 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Audio Report and a Presentation for listening, an Article and Chart and a Promotional Material for reading) on the Nutri-Score, apprenticeships, summer camps and paid holidays, followed by a second practice Project Presentation on music, with the 11-point scoring guide and a model script. The presentation prompt is a practice prompt, not the official 2027 project prompt. As on the exam, questions and choices are in French; listening sources are printed as transcripts. All sources and data are original and fictional. Allow about 25 minutes for the multiple choice and 6 minutes for the presentation.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Presentation: \blank\ / 11 \qquad Target: 15+ MCQ and 8+ presentation",
        short="Unit 5", sub="Contemporary Life")

Q.sec("Listening: Audio Report")
Q.src(r"Listening 1 \textperiodcentered\ Audio Report (transcript) \textperiodcentered\ «~Les lettres de la santé~», Radio Santé", [
    r"(JOURNALISTE) Depuis 2017, de nombreux emballages en France affichent le Nutri-Score, une échelle de cinq lettres, de A en vert foncé à E en orange foncé. L'objectif~: permettre aux consommateurs de comparer d'un coup d'œil la qualité nutritionnelle des produits.",
    r"(JOURNALISTE) Est-ce efficace~? Selon une étude d'une université française, les familles qui font attention au logo achètent un peu plus de produits notés A ou B. Et plusieurs fabricants ont modifié leurs recettes, en réduisant le sucre ou le sel, pour obtenir une meilleure note.",
    r"(NUTRITIONNISTE) Ce qui m'intéresse le plus, c'est l'effet sur les enfants. Ils comprennent les couleurs sans savoir lire une étiquette, et ce sont souvent eux qui convainquent leurs parents de reposer un paquet de céréales.",
    r"(JOURNALISTE) Certains industriels critiquent un système qu'ils jugent trop simple, mais les médecins répondent que l'obésité infantile est un problème trop grave pour attendre.",
], 5)
Q.q("1.A.1 Detail", r"Que représente la lettre A du Nutri-Score~?",
    "la meilleure qualité nutritionnelle", [("la moins bonne qualité nutritionnelle", "That is E."),
                                            ("un produit d'origine française", "The score is about nutrition, not origin."),
                                            ("un produit en promotion", "No.")],
    "A = best, dark green.", "Detail (1.A.1).",
    ["de A en vert foncé à E en orange foncé."])
Q.q("1.A.1 Detail", r"Selon l'étude, comment certains fabricants ont-ils réagi~?",
    "Ils ont modifié leurs recettes pour obtenir une meilleure note.", [("Ils ont retiré leurs produits des magasins.", "Not stated."),
                                                                       ("Ils ont augmenté le sucre.", "The opposite."),
                                                                       ("Ils ont supprimé le logo.", "Not stated.")],
    "Recettes modifiées.", "Detail (1.A.1).",
    ["plusieurs fabricants ont modifié leurs recettes… pour obtenir une meilleure note."])
Q.q("1.B.3 Point of view", r"Qu'est-ce que la nutritionniste souligne~?",
    "que les enfants comprennent les couleurs et influencent les achats de leurs parents", [("que le logo est trop petit", "She says children understand it easily."),
                                                                                            ("que les enfants ne devraient pas aller au supermarché", "Not her point."),
                                                                                            ("que le logo ne fonctionne pas avec les adultes", "Not stated.")],
    "Ce qui m'intéresse le plus…", "Point of view (1.B.3): ce qui m'intéresse le plus flags her emphasis.",
    ["…ce sont souvent eux qui convainquent leurs parents…"])
Q.q("1.B.4 Organization", r"Comment se termine le reportage~?",
    "par les positions opposées des industriels et des médecins", [("par une recette saine", "No."),
                                                                  ("par l'histoire du logo", "History is at the start."),
                                                                  ("par une interview d'enfant", "No.")],
    "critiquent… mais les médecins répondent…", "Organization (1.B.4): the ending sets two views against each other.",
    ["critiquent… mais… répondent."])
Q.q("1.B.5 Word meaning", r"Dans le reportage, «~d'un coup d'œil~» signifie",
    "très rapidement, en regardant à peine", [("avec attention et longtemps", "The opposite."),
                                             ("avec un appareil photo", "No."),
                                             ("en fermant un œil", "Literal misreading.")],
    "d'un coup d'œil = at a glance.", "Word meaning (1.B.5): the logo is designed for quick comparison.",
    ["comparer d'un coup d'œil → at a glance."])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 1 \textperiodcentered\ Article and Chart \textperiodcentered\ «~Apprendre en travaillant~», magazine Avenir", [
    r"Pendant longtemps, en France, l'apprentissage avait mauvaise réputation~: on y envoyait les élèves «~qui n'aimaient pas l'école~». Aujourd'hui, l'image change. Les formations en alternance, où l'on partage son temps entre une école et une entreprise, attirent des étudiants de tous les niveaux, jusqu'aux écoles d'ingénieurs.",
    r"«~Je gagne un salaire, je n'ai pas de dette, et j'ai déjà deux ans d'expérience à 22 ans~», explique Lucas, apprenti dans une entreprise d'énergie solaire. Pour la conseillère d'orientation Anne Leroy, «~autrefois, les familles voulaient un enfant avocat ou médecin~; aujourd'hui, un bon technicien trouve un emploi plus vite~».",
    r"Leroy reconnaît toutefois que les préjugés n'ont pas disparu~: certains jeunes qui choisissent un métier manuel doivent encore justifier leur choix auprès de leur famille.",
], 5, table=(["Domaine choisi par les jeunes", "2015", "2025"], [["Santé et droit", "38~\\%", "30~\\%"], ["Numérique et informatique", "14~\\%", "26~\\%"], ["Métiers techniques en alternance", "9~\\%", "19~\\%"], ["Autres", "39~\\%", "25~\\%"]]),
      note="Pourcentage de jeunes qui choisissent chaque domaine (données fictives).")
Q.q("1.A.2 Data", r"Selon le tableau, quel domaine a presque doublé entre 2015 et 2025~?",
    "le numérique et l'informatique", [("la santé et le droit", "It fell from 38% to 30%."),
                                       ("les autres domaines", "They fell."),
                                       ("aucun domaine n'a changé", "Several changed.")],
    "14 → 26 (almost double).", "Data (1.A.2): compare the two columns.",
    ["14 % → 26 %: ×1.86."])
Q.q("1.C.1 Connect", r"Quelle donnée du tableau illustre le mieux le changement d'image décrit dans l'article~?",
    "la hausse des métiers techniques en alternance, de 9~\\% à 19~\\%", [("la baisse de la santé et du droit", "Not the article's focus."),
                                                                        ("les 39~\\% d'autres domaines en 2015", "Not relevant."),
                                                                        ("les 26~\\% du numérique", "Not about apprenticeships.")],
    "Alternance 9 → 19.", "Connect (1.C.1): the article is about apprenticeships gaining appeal.",
    ["l'image change ↔ 9 % → 19 %."])
Q.q("1.B.3 Point of view", r"Selon Anne Leroy, pourquoi les jeunes choisissent-ils davantage les métiers techniques~?",
    "parce qu'un bon technicien trouve un emploi plus vite", [("parce que leurs familles les y obligent", "Families traditionally preferred professions."),
                                                              ("parce que les universités ont fermé", "Not stated."),
                                                              ("parce qu'ils n'aiment pas le numérique", "Not stated.")],
    "trouve un emploi plus vite.", "Point of view (1.B.3).",
    ["un bon technicien trouve un emploi plus vite."])
Q.q("1.B.5 Word meaning", r"Dans l'article, «~en alternance~» signifie",
    "en partageant son temps entre une école et une entreprise", [("en changeant d'école chaque année", "No."),
                                                                 ("en étudiant uniquement le soir", "No."),
                                                                 ("en travaillant sans salaire", "Lucas earns a salary.")],
    "alternance = work-study.", "Word meaning (1.B.5): defined in the same sentence.",
    ["où l'on partage son temps entre une école et une entreprise."])
Q.q("1.C.2 Conclusion", r"Que peut-on conclure du dernier paragraphe~?",
    "Les attentes familiales influencent encore les choix des jeunes.", [("Les familles ne donnent plus leur avis.", "Prejudices have not disappeared."),
                                                                        ("Les métiers manuels sont mal payés.", "Not stated."),
                                                                        ("Tous les jeunes choisissent l'alternance.", "Only 19%.")],
    "Les préjugés n'ont pas disparu.", "Conclusions (1.C.2) from Leroy's caveat.",
    ["doivent encore justifier leur choix…"])

Q.sec("Reading: Promotional Material")
Q.src(r"Reading 2 \textperiodcentered\ Promotional Material \textperiodcentered\ Une annonce de colonie de vacances", [
    r"\textbf{COLO «~LES PIEDS DANS L'EAU~» \textperiodcentered\ Presqu'île de Crozon, Bretagne}",
    r"Deux semaines de voile, de kayak et de randonnée pour les 12--15 ans. Hébergement sous tente dans un camping au bord de la mer, avec des animateurs diplômés (un pour huit jeunes).",
    r"\textbf{Inclus~:} pension complète, matériel nautique, transport en train depuis Paris et assurance. \textbf{Non inclus~:} argent de poche.",
    r"\textbf{Important~:} un test d'aisance aquatique est obligatoire avant le départ~; il peut être passé dans n'importe quelle piscine municipale. Prévoir un duvet et une lampe de poche.",
    r"Séjours en juillet et en août. Les familles peuvent demander une aide de la caisse d'allocations familiales.",
], 5)
Q.q("1.B.2 Audience", r"À qui s'adresse cette annonce~?",
    "aux familles d'adolescents de 12 à 15 ans", [("aux adultes qui cherchent un emploi d'animateur", "It describes a camp for teenagers."),
                                                  ("aux propriétaires de bateaux", "No."),
                                                  ("aux enfants de moins de 8 ans", "The age range is 12–15.")],
    "pour les 12–15 ans.", "Audience (1.B.2).",
    ["pour les 12–15 ans + aide pour les familles."])
Q.q("1.A.1 Detail", r"Qu'est-ce qui N'est PAS inclus dans le prix~?",
    "l'argent de poche", [("le transport en train", "Included."),
                          ("le matériel nautique", "Included."),
                          ("l'assurance", "Included.")],
    "Non inclus~: argent de poche.", "Detail (1.A.1).",
    ["Non inclus : argent de poche."])
Q.q("1.A.1 Detail", r"Que faut-il faire avant le départ~?",
    "passer un test d'aisance aquatique", [("acheter une tente", "Accommodation is provided in tents at the campsite."),
                                          ("apprendre la voile", "Sailing is taught at camp."),
                                          ("venir en voiture", "Transport by train is included.")],
    "test d'aisance aquatique obligatoire.", "Distinguish requirement from things to bring.",
    ["un test d'aisance aquatique est obligatoire avant le départ."])
Q.q("1.B.5 Word meaning", r"Dans l'annonce, «~pension complète~» signifie",
    "que tous les repas sont compris", [("que la colonie est complète", "No."),
                                         ("qu'on dort à l'hôtel", "They sleep in tents."),
                                         ("que la retraite est payée", "Pension here means board.")],
    "pension complète = full board.", "Word meaning (1.B.5): in travel contexts, pension = meals.",
    ["pension complète → all meals."])
Q.q("1.C.2 Conclusion", r"Une famille aux revenus modestes trouve le séjour trop cher. Que lui conseille l'annonce~?",
    "de demander une aide à la caisse d'allocations familiales", [("de choisir un séjour en décembre", "Stays are in July and August only."),
                                                                 ("de ne pas payer l'assurance", "Insurance is included."),
                                                                 ("d'envoyer l'enfant sans duvet", "Unrelated.")],
    "Aide de la CAF.", "Apply the last line to the case.",
    ["Les familles peuvent demander une aide…"])

Q.sec("Listening: Presentation")
Q.src(r"Listening 2 \textperiodcentered\ Presentation (transcript) \textperiodcentered\ «~Pourquoi la France part en vacances en août~»", [
    r"(PROFESSEUR) Les touristes s'étonnent parfois de trouver Paris à moitié vide en août, avec des boulangeries fermées «~pour congés annuels~». Pour comprendre, il faut remonter à 1936~: cette année-là, le gouvernement du Front populaire accorde aux salariés deux semaines de congés payés.",
    r"(PROFESSEUR) Des milliers d'ouvriers découvrent alors la mer pour la première fois. Ensuite, les congés s'allongent~: trois semaines en 1956, quatre en 1969, cinq en 1982.",
    r"(PROFESSEUR) Mais ce n'est pas seulement une question de loi. Pendant longtemps, les usines fermaient toutes en même temps, au mois d'août, ce qui a créé l'habitude de partir tous ensemble.",
    r"(PROFESSEUR) Aujourd'hui, le débat porte sur l'étalement~: certains proposent de mieux répartir les vacances sur l'année pour éviter les embouteillages et le surtourisme. D'autres défendent le mois d'août comme un moment de vie collective.",
], 5)
Q.q("1.B.1 Main idea", r"Quel est le sujet central de la présentation~?",
    "l'origine et l'évolution des vacances d'été en France", [("l'histoire des boulangeries parisiennes", "Bakeries are the opening example."),
                                                             ("la vie des ouvriers dans les usines", "Factories are one cause."),
                                                             ("les plages les plus célèbres de France", "No.")],
    "Why France leaves in August.", "Main idea (1.B.1): history, causes and today's debate.",
    ["1936 → extensions → August habit → debate."])
Q.q("1.A.1 Detail", r"Que se passe-t-il en 1936~?",
    "Les salariés obtiennent deux semaines de congés payés.", [("Les salariés obtiennent cinq semaines de congés.", "That was 1982."),
                                                              ("Les usines ferment définitivement.", "No."),
                                                              ("Paris interdit le tourisme.", "No.")],
    "1936: two weeks.", "Detail (1.A.1).",
    ["accorde aux salariés deux semaines de congés payés."])
Q.q("1.C.3 Inference", r"Pourquoi le professeur mentionne-t-il que les usines fermaient en août~?",
    "pour expliquer pourquoi tout le monde part en vacances en même temps", [("pour critiquer les patrons", "No criticism."),
                                                                            ("pour montrer que les usines étaient dangereuses", "No."),
                                                                            ("pour parler de la pollution", "No.")],
    "Factory closures → shared August habit.", "Inference (1.C.3): mais ce n'est pas seulement une question de loi introduces this second cause.",
    ["usines fermaient… en même temps → habitude de partir ensemble."])
Q.q("1.B.4 Organization", r"Comment la présentation est-elle organisée~?",
    "Elle part d'une observation, explique l'histoire et les causes, puis présente un débat actuel.", [("Elle raconte la vie d'un touriste du début à la fin.", "No narrative."),
                                                                                                       ("Elle compare la France et le Québec.", "No comparison."),
                                                                                                       ("Elle donne des conseils pour réserver un hôtel.", "No."),],
    "Observation → history → causes → debate.", "Organization (1.B.4): markers like pour comprendre, ensuite, mais, aujourd'hui.",
    ["Structure follows the markers."])
Q.q("1.B.3 Point of view", r"Que proposent certaines personnes, selon le professeur~?",
    "mieux répartir les vacances sur l'année", [("supprimer les congés payés", "No."),
                                                 ("obliger tout le monde à partir en août", "The opposite."),
                                                 ("fermer les plages en été", "No.")],
    "L'étalement.", "Point of view (1.B.3): separate the two sides of the debate.",
    ["certains proposent de mieux répartir les vacances sur l'année."])

Q.frq(kind="Project Presentation", head=r"Question 1 \textperiodcentered\ Project Presentation (practice prompt) \textperiodcentered\ 11 points \textperiodcentered\ 3 + 3 minutes", mins=6,
      directions=[r"Imagine that your project examined how songs have accompanied the identity of a French-speaking community over time. You have 3 minutes to prepare, using your notes, and 3 minutes to present. Explain at least three factors, with specific examples from your research, and show how cultural perspectives relate to cultural products or practices."],
      prompt=[r"Prompt: \textbf{Comment la chanson a-t-elle accompagné l'identité d'une communauté francophone au fil du temps~?}",
              r"Practice focus (example): Quebec song from Félix Leclerc to today."],
      model=[r"Aujourd'hui, je vais vous parler de la chanson québécoise et de la manière dont elle a accompagné l'identité du Québec. Je me suis concentré sur trois facteurs~: les chansonniers, une chanson devenue rituelle, et la protection de la chanson en français à la radio.",
             r"Premièrement, les chansonniers ont donné une voix au Québec. D'après mes recherches, Félix Leclerc a connu le succès à Paris au début des années cinquante, puis, pendant les années soixante, des auteurs comme Gilles Vigneault ont chanté le pays, l'hiver et la langue dans de petites salles appelées «~boîtes à chansons~». Cela montre que la chanson était un moyen d'affirmer une identité distincte.",
             r"Deuxièmement, une chanson est devenue un rituel. «~Gens du pays~», de Gilles Vigneault, a été chantée pour la première fois lors de la Fête nationale de 1975. Aujourd'hui, les Québécois la chantent à leurs anniversaires~: «~Mon cher ami, c'est à ton tour de te laisser parler d'amour~». Cette pratique reflète l'attachement à une culture partagée, jusque dans la vie familiale.",
             r"Enfin, la société protège la chanson en français. Au Canada, les radios francophones doivent diffuser une majorité de chansons en français. Cela démontre que les Québécois considèrent leur langue comme un patrimoine à défendre, entourés comme ils le sont de millions d'anglophones.",
             r"En conclusion, la chanson québécoise a été à la fois un cri, un rituel et un patrimoine protégé. Ce que j'ai appris, c'est qu'au Québec, chanter en français n'est pas seulement un choix artistique~: c'est une façon de dire qui l'on est."],
      rows=[("A Task", 2, "three or more factors, each explained with relevant details", "factors named with no detail, or only one or two factors"),
            ("B Culture", 2, "examples linking perspectives (identity, shared culture, language as heritage) to products or practices", "examples with no perspective (1 point)"),
            ("C Organization", 2, "introduction naming the factors, ordered body, conclusion; varied transitions", "a list of facts"),
            ("D Language", 3, "varied vocabulary and structures (passive, passé composé/imparfait, relative clauses)", "a limited set of basic structures"),
            ("E Delivery", 2, "clear pronunciation, natural pace and intonation", "hesitant or rushed speech")],
      tips=["Each factor follows claim → specific example → perspective (cela montre, cette pratique reflète).", "Change over time is shown with dates (années cinquante, 1975) and past tenses.",
            "The birthday ritual is a vivid practice that earns the culture row.", "About 380 words."],
      ask="Prepare for 3 minutes using keywords only, then present aloud for 3 minutes. Then mark your presentation.", lines=14)

GUIDE, QSET = G, Q
