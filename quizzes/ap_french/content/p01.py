from ap_wl.model import Doc

STEM = "01-families-communities"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 1: Families and Communities", r"Unit 1 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 1 asks what makes a family, how families shape values and traditions, and how communities are changing. Its recommended contexts are family relationships, community activities, social interactions and relationships, and urban and rural communities. This guide gives the vocabulary the exam assumes, the structures for describing relationships and routines, the cultural products, practices and perspectives most often tested (new family forms, la bise, associations, the Senegalese teranga, rural depopulation), and an Argumentative Essay kit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Words I keep forgetting: \blank[10em]",
        short="Unit 1", sub="Families and Communities")

G.sec("Family and relationships")
G.tex(r"""
\begin{vocab}
les parents / les proches & parents; relatives / close family & \emph{parents} also means relatives \\
la famille recomposée / monoparentale & blended / single-parent family & \\
le PACS & civil union (since 1999) & \emph{se pacser} \\
le beau-père, la belle-mère & stepfather / father-in-law; stepmother / mother-in-law & \\
élever / l'éducation & to raise / upbringing & \emph{élever ses enfants} \\
s'occuper de, garder & to look after & \emph{garder les petits-enfants} \\
s'entendre bien avec & to get along with & \emph{je m'entends bien avec ma sœur} \\
le repas de famille & family meal & Sunday lunch, often long \\
quitter le nid / décohabiter & to leave home & \\
\end{vocab}

\textbf{Products, practices, perspectives.} French law recognizes several family forms: marriage, the PACS (a civil partnership created in 1999), and many \emph{familles recomposées}. The long Sunday family meal reflects the value placed on time together at the table. Grandparents often look after grandchildren on Wednesdays, when many primary schools have no classes.
""")
G.q("1 Famille", r"Que signifie «~une famille recomposée~»~?",
    "une famille où au moins un des parents a des enfants d'une union précédente", [("une famille de trois générations sous le même toit", "That is une famille élargie or multigénérationnelle."),
                                                                                    ("une famille avec un seul parent", "That is une famille monoparentale."),
                                                                                    ("une famille qui a déménagé récemment", "Unrelated.")],
    "Recomposée = blended.", "A famille recomposée brings together children from previous relationships.",
    ["recomposer = put back together → blended family."])
G.q("1 Famille", r"Choose the best word: Mes grands-parents m'ont aidé à \blank\ mes petits frères quand mes parents travaillaient.",
    "garder", [("regarder", "Regarder means to watch (TV, a film), not to look after."),
               ("grandir", "Grandir is intransitive: children grow, they are not grown."),
               ("rester", "Rester means to stay.")],
    "garder = to look after (children).", "Garder des enfants = to look after children; grandir = to grow up.",
    ["aider à + infinitive with a direct object → garder."])
G.q("1 Famille", r"What is the PACS?",
    "a civil partnership recognized in French law since 1999", [("a family allowance for large families", "Family allowances are les allocations familiales."),
                                                               ("a religious wedding ceremony", "The PACS is civil, not religious."),
                                                               ("a school holiday", "Unrelated.")],
    "PACS = civil partnership.", "The pacte civil de solidarité (1999) is a legal union with fewer formalities than marriage.",
    ["se pacser → civil partnership."])

G.sec("Community and social life")
G.tex(r"""
\begin{vocab}
le quartier / les voisins & neighborhood / neighbors & \\
une association (loi 1901) & a nonprofit association & millions of French people volunteer in one \\
le bénévolat / le bénévole & volunteering / volunteer & \\
la fête des voisins & neighbors' day & neighbors share a meal outdoors once a year \\
la bise / se faire la bise & greeting kiss on the cheeks & the number varies by region \\
la teranga & Senegalese hospitality & welcoming guests and sharing the meal \\
la solidarité & solidarity, mutual help & \\
\end{vocab}

\textbf{Associations.} The 1901 law makes it easy to found a nonprofit \emph{association}; they run sports clubs, food banks, festivals and cultural centers. The perspective: civic life happens through citizens organizing themselves, not only through the state.

\textbf{La teranga.} In Senegal, guests are welcomed and invited to share the meal from a common dish (the \emph{thiéboudienne}). Teranga, the Wolof word for this hospitality, is a source of national pride.
""")
G.q("2 Communauté", r"Au Sénégal, que signifie le mot «~teranga~»~?",
    "l'hospitalité et l'accueil des invités", [("une fête religieuse", "Teranga is hospitality, not a holiday."),
                                              ("un plat de riz et de poisson", "That dish is the thiéboudienne."),
                                              ("une association de quartier", "Unrelated.")],
    "Teranga = hospitality.", "Teranga (Wolof) names Senegal's tradition of welcoming guests and sharing the meal.",
    ["teranga → welcome, hospitality."])
G.q("2 Communauté", r"Which perspective does the French tradition of associations (under the 1901 law) most directly reflect?",
    "Citizens can organize themselves to meet community needs.", [("Only the state should provide services.", "Associations show the opposite."),
                                                                 ("Volunteering should always be paid.", "Bénévoles are unpaid."),
                                                                 ("Families should live far from their neighbors.", "Unrelated.")],
    "Associations ↔ civic self-organization.", "A practice (founding an association) linked to a perspective (citizens act for the common good).",
    ["Practice: associations.", "Perspective: civic initiative."])

G.sec("Urban and rural communities")
G.tex(r"""
\begin{vocab}
la campagne / le milieu rural & the countryside / rural areas & \\
l'exode rural / la désertification rurale & rural flight / rural depopulation & \\
la diagonale du vide & sparsely populated band from the northeast to the southwest of France & \\
les services de proximité & local services (post office, doctor, school) & \\
le télétravail & remote work & \\
le loyer / le logement & rent / housing & \\
la banlieue & suburbs (often large housing estates) & not always wealthy, unlike many U.S. suburbs \\
\end{vocab}

\textbf{Causes and effects.} Questions in this context ask why people leave the countryside (\emph{le manque d'emplois, de médecins}) and what happens to those who stay. Since 2020, remote work has brought some families back to villages, but only where there is fast internet and basic services.
""")
G.q("3 Rural", r"Dans un article~: «~Depuis la fermeture de l'école, beaucoup de jeunes familles sont parties en ville.~» Quel est le lien entre les deux idées~?",
    "cause et conséquence", [("opposition", "No opposing ideas; one event explains the other."),
                             ("exemple", "The second clause is not an example of the first."),
                             ("suite d'instructions", "This is narration, not instructions.")],
    "Depuis → cause, then consequence.", "Organization questions (1.B.4) ask how ideas relate.",
    ["school closed → families left."])
G.q("3 Rural", r"What is la diagonale du vide?",
    "a band of sparsely populated rural areas across France", [("a highway between Paris and Marseille", "Not a road."),
                                                              ("the border between France and Belgium", "No."),
                                                              ("a new suburban district", "The opposite: rural and empty.")],
    "Diagonale du vide = rural depopulation belt.", "The name describes a diagonal band from the northeast to the southwest with low population density.",
    ["vide = empty → sparsely populated."])

G.sec("Structures for relationships and routines")
G.tex(r"""
\begin{compare}{Structure}{Use}{Example}
avoir l'habitude de + infinitive & habits & Le dimanche, nous avons l'habitude de déjeuner chez mes grands-parents. \\
depuis + present & how long something has gone on & J'habite dans ce quartier depuis dix ans. \\
venir de + infinitive & something just happened & Ma sœur vient de quitter la maison. \\
reciprocal se & each other & Les voisins s'entraident beaucoup. \\
aussi\ldots que / plus\ldots que & comparisons & La vie au village est plus calme qu'en ville. \\
pendant que + imparfait & background actions & Pendant que ma mère travaillait, ma grand-mère nous gardait. \\
pour que + subjunctive & purpose with a new subject & Ils économisent pour que leurs enfants fassent des études. \\
\end{compare}

\begin{trap}
English \emph{I have lived here for ten years} uses a perfect tense; French uses the present with \emph{depuis}: \emph{J'habite ici depuis dix ans}. \emph{J'ai habité ici pendant dix ans} means you no longer live there.
\end{trap}
""")
G.q("4 Structures", r"Choose the best way to say: ``We have been living in this neighborhood for ten years.''",
    "Nous habitons dans ce quartier depuis dix ans.", [("Nous avons habité dans ce quartier depuis dix ans.", "Depuis with an ongoing situation takes the present."),
                                                       ("Nous habitons dans ce quartier pendant dix ans.", "Pendant does not express an ongoing duration up to now."),
                                                       ("Nous habiterons dans ce quartier il y a dix ans.", "Il y a + time refers to the past; the future does not fit.")],
    "present + depuis.", "Ongoing actions that began in the past: present tense + depuis.",
    ["still living there → present + depuis."])
G.q("4 Structures", r"Ma sœur \blank\ de partir à l'université~; la maison est très calme.",
    "vient", [("va", "Aller + infinitive is the near future, but the house is already quiet."),
              ("a", "Avoir de partir is not a structure."),
              ("est", "Être de partir is not a structure.")],
    "venir de + infinitive = has just.", "Venir de + infinitive expresses the recent past.",
    ["the house is already quiet → she has just left → vient de partir."])
G.q("4 Structures", r"Mes parents travaillent beaucoup pour que nous \blank\ aller à l'université.",
    "puissions", [("pouvons", "Pour que always takes the subjunctive."),
                  ("pouvoir", "With a new subject (nous), use pour que + subjunctive."),
                  ("pourrons", "The future cannot follow pour que.")],
    "pour que + subjunctive.", "Pour que expresses purpose and always takes the subjunctive.",
    ["pour que → puissions."])

G.sec("Task kit: the Argumentative Essay")
G.tex(r"""
Unit 1 essay topics ask about family roles and community life: \emph{Les grands-parents doivent-ils s'occuper des petits-enfants~?}, \emph{Vaut-il mieux vivre en ville ou à la campagne~?}, \emph{Le bénévolat devrait-il être obligatoire~?}

\begin{compare}{Move}{Phrases}{Example}
Position & À mon avis, / J'estime que & J'estime que le bénévolat ne devrait pas être obligatoire. \\
Evidence & D'après la source 1 / Le graphique montre que & Le graphique montre que seulement 18~\% des jeunes\ldots \\
Explain & Cela montre que / Par conséquent & Cela montre que la motivation compte plus que l'obligation. \\
Concede & Certes\ldots, mais / Il est vrai que\ldots ; cependant, & Certes, beaucoup de villages ont besoin d'aide~; cependant, \ldots \\
Conclude & En somme / Pour toutes ces raisons & Pour toutes ces raisons, \ldots \\
\end{compare}
""")
G.q("5 Essai", r"Which sentence best explains a piece of evidence, as the argumentation row requires?",
    r"La source 2 indique que 60~\% des bénévoles ont continué à aider après le programme, ce qui montre que l'expérience crée un engagement durable.",
    [("La source 2 contient un graphique sur les bénévoles.", "Naming a source without using its content earns nothing."),
     ("Le bénévolat est très bien et très important.", "A claim with no evidence."),
     (r"D'après la source 2, 60~\% des bénévoles ont continué à aider.", "Evidence without explanation; the link to the position is missing.")],
    "Claim + evidence + explanation.", "Row C rewards explaining how the evidence supports the claim (ce qui montre que…).",
    ["Evidence: 60%.", "Explanation: ce qui montre que…"])
G.q("5 Essai", r"Which transition best introduces a counterargument before rebutting it?",
    "Certes", [("Par conséquent", "Par conséquent draws a conclusion."),
               ("De plus", "De plus adds a point on the same side."),
               ("Tout d'abord", "Tout d'abord begins a list of your own points.")],
    "Concede, then rebut.", "Certes…, mais… concedes a point and answers it, which strengthens the argument.",
    ["Counterargument → certes… mais."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 1: Families and Communities: Question Set", r"Unit 1 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Audio Report and an Interview for listening, an Article and Chart and a Promotional Material for reading) on grandparents, rural life and neighborhood solidarity, followed by an Argumentative Essay with three sources and the 10-point scoring guide. As on the exam, questions and choices are in French. Listening sources are printed as transcripts: read each once at normal speed, then answer without rereading. All sources and data are original and fictional, written for practice. Allow about 25 minutes for the multiple choice and 55 minutes for the essay.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Essay: \blank\ / 10 \qquad Target: 15+ MCQ and 7+ essay \qquad Pace: 75 s per item",
        short="Unit 1", sub="Families and Communities")

Q.sec("Listening: Audio Report")
Q.src(r"Listening 1 \textperiodcentered\ Audio Report (transcript) \textperiodcentered\ «~Le mercredi des grands-parents~», Radio Info", [
    r"(JOURNALISTE) En France, près d'un enfant sur deux de moins de six ans est gardé régulièrement par ses grands-parents, selon une étude publiée ce mois-ci. Le mercredi, quand de nombreuses écoles primaires n'ont pas cours, ils sont encore plus nombreux à prendre le relais.",
    r"(JOURNALISTE) Pour beaucoup de familles, la raison est d'abord économique~: le prix de la garde d'enfants a augmenté de 30~\% en dix ans. Mais ce n'est pas tout. Les chercheurs constatent que de nombreux parents souhaitent que leurs enfants grandissent près de la famille.",
    r"(GRAND-MÈRE, MONIQUE) Je garde mes deux petits-enfants tous les mercredis. C'est fatigant, je ne vais pas vous mentir, mais je me sens utile. Et je leur apprends les comptines que me chantait ma mère.",
    r"(JOURNALISTE) Les spécialistes, cependant, rappellent que les grands-parents ont aussi besoin de repos. Ils recommandent que les communes proposent des activités et des lieux d'accueil pour ces grands-parents très sollicités.",
], 5)
Q.q("1.B.1 Main idea", r"Quel est le sujet principal du reportage~?",
    "le rôle des grands-parents dans la garde des jeunes enfants", [("la hausse du nombre de naissances en France", "Births are not discussed."),
                                                                   ("l'histoire des comptines françaises", "Nursery rhymes are one detail Monique mentions."),
                                                                   ("la réforme des écoles primaires", "School schedules are only the context.")],
    "Main idea: grandparents as caregivers.", "The report opens with the statistic, gives reasons, a testimony and expert advice, all about grandparents caring for children.",
    ["Opening statistic + every segment → grandparents caring for grandchildren."])
Q.q("1.A.1 Detail", r"D'après le reportage, comment a évolué le prix de la garde d'enfants~?",
    "Il a augmenté de 30~\\% en dix ans.", [("Il a baissé de moitié.", "The report says it rose."),
                                            ("Il a augmenté de 30~\\% cette année.", "The figure is 30% over ten years."),
                                            ("Il n'a pas changé.", "It rose 30%.")],
    "+30% in ten years.", "Detail questions (1.A.1) match the figure and its time frame exactly.",
    ["a augmenté de 30 % en dix ans."])
Q.q("1.B.3 Attitude", r"Quelle est l'attitude de Monique envers son rôle de grand-mère~?",
    "Elle le trouve fatigant mais gratifiant.", [("Elle le fait par obligation et veut arrêter.", "She says she feels useful."),
                                                ("Elle le trouve facile et reposant.", "She says it is tiring."),
                                                ("Elle préfère que ses petits-enfants aillent à la crèche.", "She never says so.")],
    "C'est fatigant… mais je me sens utile.", "Attitude questions (1.B.3) weigh both parts of a mixed statement.",
    ["fatigant → tiring.", "je me sens utile → rewarding."])
Q.q("1.C.3 Inference", r"Que peut-on déduire au sujet des comptines que Monique apprend à ses petits-enfants~?",
    "Elles permettent de transmettre une tradition familiale.", [("Elle les a apprises dans un atelier de la commune.", "She learned them from her mother."),
                                                                ("Ce sont des chansons modernes de la radio.", "They are rhymes her mother sang."),
                                                                ("Les enfants refusent de les apprendre.", "Nothing suggests that.")],
    "From her mother → tradition passed down.", "Inference (1.C.3): rhymes passed across three generations carry family tradition.",
    ["les comptines que me chantait ma mère → three generations."])
Q.q("1.A.1 Detail", r"Que recommandent les spécialistes~?",
    "que les communes proposent des activités et des lieux d'accueil pour les grands-parents", [("que les grands-parents arrêtent de garder leurs petits-enfants", "They recommend support, not stopping."),
                                                                                               ("que les parents travaillent moins", "Not mentioned."),
                                                                                               ("que les crèches baissent leurs prix", "Not mentioned.")],
    "Activités et lieux d'accueil.", "The recommendation is in the last segment.",
    ["Ils recommandent que les communes proposent…"])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 1 \textperiodcentered\ Article and Chart \textperiodcentered\ «~Retour au village~», magazine Territoires", [
    r"Pendant des décennies, l'histoire des villages du centre de la France était toujours la même~: les jeunes partaient étudier en ville et ne revenaient pas. Aujourd'hui, de nombreuses communes comptent moins de cinq cents habitants, et certaines n'ont plus ni boulangerie ni médecin.",
    r"Pourtant, quelque chose commence à changer. Depuis 2020, le télétravail a permis à certaines familles de s'installer à la campagne sans perdre leur emploi. À Saint-Aubin, un village de 300 habitants, l'école qui devait fermer a rouvert l'an dernier avec onze nouveaux élèves.",
    r"«~Ce n'est pas un retour massif~», prévient la géographe Claire Martin. «~Sans internet rapide, sans médecins et sans transports, les familles qui arrivent repartent au bout de deux ou trois ans.~» Pour elle, l'avenir des villages dépend moins de la nostalgie que des services.",
], 5, table=(["Année", "De la ville vers un village", "D'un village vers la ville"],
             [["2018", "41~000", "96~000"], ["2020", "73~000", "88~000"], ["2022", "82~000", "84~000"], ["2024", "79~000", "86~000"]]),
      note="Personnes ayant déménagé entre des communes de moins de 5~000 habitants et des villes (données fictives).")
Q.q("1.B.1 Purpose", r"Quel est le but principal de l'article~?",
    "présenter un changement récent dans les campagnes et ses limites", [("convaincre les lecteurs de s'installer à Saint-Aubin", "It reports and analyzes; it does not persuade."),
                                                                        ("critiquer les jeunes qui partent étudier", "The first paragraph describes the past without criticism."),
                                                                        ("expliquer le fonctionnement du télétravail", "Remote work is a cause, not the subject.")],
    "Change + its limits.", "The article sets up the old pattern, shows a recent change, then qualifies it.",
    ["Paragraph 2: quelque chose commence à changer.", "Paragraph 3: ce n'est pas un retour massif."])
Q.q("1.A.2 Data", r"Selon le graphique, quelle année présente la plus petite différence entre les deux mouvements~?",
    "2022", [("2018", "In 2018 the gap was the largest: 96,000 vs. 41,000."),
             ("2020", "In 2020 the gap was 15,000."),
             ("2024", "In 2024 the gap was 7,000, larger than in 2022.")],
    "2022: 84,000 − 82,000 = 2,000.", "Data questions (1.A.2): compute each year's gap and compare.",
    ["Gaps: 55,000; 15,000; 2,000; 7,000."])
Q.q("1.C.1 Connect", r"Quelle information de l'article explique les données du graphique à partir de 2020~?",
    "Le télétravail a permis à certaines familles de s'installer à la campagne.", [("De nombreuses communes comptent moins de cinq cents habitants.", "This describes the situation, not the post-2020 change."),
                                                                                    ("Certaines communes n'ont plus de boulangerie.", "This explains decline, not the rise after 2020."),
                                                                                    ("Les jeunes partaient étudier en ville.", "This is the old pattern.")],
    "Depuis 2020, le télétravail…", "Connect (1.C.1): the chart's jump after 2020 matches the article's cause.",
    ["Chart: moves to villages 41,000 → 73,000 by 2020.", "Article: depuis 2020, le télétravail…"])
Q.q("1.B.3 Point of view", r"Quelle est l'opinion de la géographe Claire Martin~?",
    "Les nouvelles familles ne resteront que s'il y a des services de base.", [("C'est la nostalgie qui fera revenir les gens.", "She says the future depends less on nostalgia than on services."),
                                                                              ("Les villages ont déjà résolu leurs problèmes.", "She says it is not a mass return."),
                                                                              ("Les écoles de village devraient fermer.", "She never says so.")],
    "Services > nostalgie.", "Point of view (1.B.3): her quotes stress internet, doctors and transport.",
    ["Sans internet rapide, sans médecins et sans transports, … repartent."])
Q.q("1.B.5 Word meaning", r"Dans l'article, le verbe «~repartent~» signifie",
    "s'en vont", [("se marient", "Repartir means to leave again."),
                  ("se plaignent", "Se plaindre is to complain."),
                  ("restent", "Rester is the opposite.")],
    "repartir = leave (again).", "Word meaning (1.B.5): the sentence contrasts families who arrive with families who leave.",
    ["les familles qui arrivent repartent → leave."])

Q.sec("Reading: Promotional Material")
Q.src(r"Reading 2 \textperiodcentered\ Promotional Material \textperiodcentered\ Un dépliant de la mairie", [
    r"\textbf{Votre quartier a besoin de vous~! Programme «~Voisins solidaires~»}",
    r"Vous avez plus de 16 ans et quelques heures libres par semaine~? Rejoignez notre réseau de bénévoles. Vous pourrez rendre visite à des personnes âgées qui vivent seules, aider au jardin partagé ou donner du soutien scolaire aux enfants du quartier.",
    r"\textbf{Ce que nous offrons~:} une formation gratuite, une attestation d'heures de bénévolat (utile pour Parcoursup et les candidatures) et le plaisir de rencontrer vos voisins.",
    r"\textbf{Comment participer~:} inscrivez-vous à l'accueil de la maison de quartier (12, rue de la Mairie) ou sur voisinssolidaires.fr avant le 15 octobre. Les activités commencent le 1\textsuperscript{er} novembre. Places limitées.",
], 5)
Q.q("1.B.2 Audience", r"À qui s'adresse principalement ce dépliant~?",
    "aux habitants du quartier âgés de plus de 16 ans", [("aux personnes âgées qui cherchent de la compagnie", "They are the people helped, not the audience recruited."),
                                                        ("aux enseignants qui cherchent un emploi", "It recruits unpaid volunteers."),
                                                        ("aux entreprises qui veulent financer des activités", "No sponsorship is mentioned.")],
    "Vous avez plus de 16 ans…~?", "Audience (1.B.2): the direct address names who should act.",
    ["Rejoignez notre réseau de bénévoles → residents over 16."])
Q.q("1.A.1 Detail", r"Qu'est-ce que le programme offre aux participants~?",
    "une attestation utile pour les candidatures", [("un salaire mensuel", "Volunteers are not paid."),
                                                   ("un voyage à la fin du programme", "Not mentioned."),
                                                   ("des cours universitaires gratuits", "It offers training, not university classes.")],
    "Attestation utile pour Parcoursup.", "The Ce que nous offrons section lists training, a certificate, and meeting neighbors.",
    ["une attestation d'heures de bénévolat (utile pour Parcoursup…)."])
Q.q("1.A.1 Detail", r"Laquelle de ces activités N'est PAS mentionnée dans le dépliant~?",
    "nettoyer les rues du quartier", [("rendre visite à des personnes âgées", "Listed."),
                                      ("aider au jardin partagé", "Listed."),
                                      ("donner du soutien scolaire", "Listed.")],
    "Street cleaning is not listed.", "NOT questions: check each choice against the list.",
    ["Listed: visits, garden, tutoring."])
Q.q("1.C.2 Conclusion", r"Une personne s'inscrit le 20 octobre. Que va-t-il probablement se passer~?",
    "Elle ne pourra pas participer, car la date limite est passée.", [("Elle commencera les activités le 1er novembre sans problème.", "Registration closes on October 15."),
                                                                     ("Elle recevra l'attestation immédiatement.", "The certificate is for hours completed."),
                                                                     ("Elle devra payer des frais d'inscription tardive.", "No fee is mentioned.")],
    "Deadline: before October 15.", "Conclusions (1.C.2) apply the text's details to a new case.",
    ["avant le 15 octobre → too late."])
Q.q("1.B.3 Tone", r"Quel ton le dépliant adopte-t-il~?",
    "enthousiaste et chaleureux", [("froid et administratif", "It uses exclamations and a friendly appeal."),
                                    ("ironique", "Nothing is said ironically."),
                                    ("triste et inquiet", "The tone is upbeat.")],
    "Votre quartier a besoin de vous~!", "Tone (1.B.3): exclamations and direct appeals make the flyer warm and enthusiastic.",
    ["Exclamations + direct address → enthusiastic."])

Q.sec("Listening: Interview")
Q.src(r"Listening 2 \textperiodcentered\ Interview (transcript) \textperiodcentered\ Une maire d'un village du Québec", [
    r"(JOURNALISTE) Madame Tremblay, vous êtes mairesse de Saint-Rémi depuis quatre ans. Quel était le plus grand problème à votre arrivée~?",
    r"(MAIRESSE) Les jeunes s'en allaient. Ils finissaient le secondaire et partaient à Montréal, parce qu'ici il n'y avait ni emplois ni cégep.",
    r"(JOURNALISTE) Et qu'avez-vous fait~?",
    r"(MAIRESSE) D'abord, nous les avons écoutés. Ils nous ont dit qu'ils ne voulaient pas partir, mais qu'ils avaient besoin de possibilités. Alors, nous avons ouvert un centre de formation en agriculture durable et en tourisme, avec des cours à distance du cégep. Nous organisons aussi une corvée chaque mois pour réparer les sentiers et l'école.",
    r"(JOURNALISTE) Est-ce que ça a marché~?",
    r"(MAIRESSE) Il reste beaucoup à faire. Mais cette année, pour la première fois, plus de jeunes sont revenus qu'il n'en est parti. Le plus important, c'est qu'ils sentent que le village leur appartient aussi.",
], 5)
Q.q("1.A.1 Detail", r"Selon la mairesse, pourquoi les jeunes partaient-ils~?",
    "parce qu'il n'y avait ni emplois ni cégep dans le village", [("parce qu'ils n'aimaient pas la vie à la campagne", "They said they did not want to leave."),
                                                                ("parce que l'école était fermée", "The school needed repairs; that is not the reason given."),
                                                                ("parce que leurs familles avaient déménagé", "They left alone after school.")],
    "ni emplois ni cégep.", "The reason is stated directly in her first answer.",
    ["ici il n'y avait ni emplois ni cégep."])
Q.q("1.B.4 Organization", r"Comment la mairesse décrit-elle la démarche suivie~?",
    "D'abord, on a écouté les jeunes, puis on a créé des solutions.", [("D'abord, on a construit une université, puis on a parlé aux jeunes.", "She says d'abord, nous les avons écoutés."),
                                                                       ("On a engagé une entreprise étrangère.", "Not mentioned."),
                                                                       ("On a attendu que le gouvernement agisse.", "The village acted itself.")],
    "D'abord… Alors…", "Organization (1.B.4): d'abord and alors mark the order.",
    ["D'abord, nous les avons écoutés.", "Alors, nous avons ouvert…"])
Q.q("1.B.5 Word meaning", r"Dans l'entretien, une «~corvée~» est",
    "un travail collectif et bénévole fait ensemble pour la communauté", [("une fête religieuse du village", "No."),
                                                                         ("un impôt payé par les habitants", "It is unpaid work, not a tax."),
                                                                         ("une entreprise de construction", "The residents do the work.")],
    "Corvée (Quebec) = collective volunteer work.", "Word meaning (1.B.5): une corvée chaque mois pour réparer les sentiers — the community works together.",
    ["monthly + repairing paths and the school → collective work."])
Q.q("1.B.3 Attitude", r"Quelle attitude la mairesse montre-t-elle à propos des résultats~?",
    "optimiste, mais consciente qu'il reste du travail", [("totalement satisfaite", "Il reste beaucoup à faire."),
                                                         ("déçue", "She reports progress."),
                                                         ("indifférente", "She cares about the outcome.")],
    "Il reste beaucoup à faire. Mais…", "Mixed attitude (1.B.3): a concession followed by progress.",
    ["Concession + progress → cautiously optimistic."])
Q.q("1.C.3 Inference", r"Que veut dire la mairesse par «~ils sentent que le village leur appartient aussi~»~?",
    "Les jeunes se sentent membres de la communauté et responsables d'elle.", [("Les jeunes ont acheté des maisons au village.", "She speaks of belonging, not property."),
                                                                                ("Les jeunes dirigent maintenant le village.", "She is still the mayor."),
                                                                                ("Les jeunes veulent vendre le village.", "Nonsensical reading.")],
    "Belonging, not property.", "Implied meaning (1.C.3): appartenir is used figuratively.",
    ["After being heard and working together, they feel the village is theirs too."])

Q.frq(kind="Argumentative Essay", head=r"Question 3 \textperiodcentered\ Argumentative Essay \textperiodcentered\ 10 points \textperiodcentered\ 55 minutes", mins=55,
      directions=[r"Vous allez écrire un essai argumentatif pour un cours universitaire. Lisez le sujet et les sources écrites~; ensuite, écoutez la source audio (ici, la transcription). Écrivez un essai qui intègre des éléments des trois sources pour soutenir votre position. Indiquez les sources utilisées par leur numéro, leur titre ou leur auteur."],
      sources=[dict(title=r"Source 1 \textperiodcentered\ Article \textperiodcentered\ «~Vivre en grand~»", paras=[
          r"Pour Karim, ingénieur de 29 ans, quitter son village pour Lyon a été la meilleure décision de sa vie. «~Ici, j'ai un travail dans mon domaine, des musées, des concerts et des gens venus de partout~», raconte-t-il.",
          r"Les grandes villes concentrent les universités, les hôpitaux spécialisés et la plupart des emplois qualifiés. Selon l'urbaniste Thomas Bernard, «~la ville multiplie les occasions~: plus il y a de monde, plus les idées se croisent~».",
          r"Mais Karim reconnaît le prix à payer~: il passe près de deux heures par jour dans les transports et consacre la moitié de son salaire à son loyer."]),
               dict(title=r"Source 2 \textperiodcentered\ Graphique \textperiodcentered\ Satisfaction selon le lieu de résidence", paras=[
          r"Enquête auprès de 4~000 adultes en France, en Belgique et au Québec. Pourcentage de personnes «~satisfaites~» ou «~très satisfaites~» de chaque aspect (données fictives)."],
                    table=(["Aspect", "Grande ville", "Petite commune"], [["Possibilités d'emploi", "64~\\%", "31~\\%"], ["Temps libre", "38~\\%", "67~\\%"], ["Relations avec les voisins", "29~\\%", "72~\\%"], ["Accès aux soins", "71~\\%", "40~\\%"]])),
               dict(title=r"Source 3 \textperiodcentered\ Audio (transcription) \textperiodcentered\ «~Depuis le village~», balado", paras=[
          r"(ANIMATRICE) Aujourd'hui, nous recevons Aminata Diallo, qui est revenue il y a trois ans dans son village près de Thiès, au Sénégal.",
          r"(AMINATA) À Dakar, je gagnais plus, c'est vrai. Mais je ne connaissais pas mes voisins et mon fils ne pouvait pas jouer dehors. Ici, tout le monde se connaît~; si quelqu'un tombe malade, le village s'organise pour l'aider.",
          r"(ANIMATRICE) Et le travail~?",
          r"(AMINATA) Je travaille en ligne pour une agence de graphisme. Sans internet, je n'aurais jamais pu revenir. C'est pour cela que je dis que le village peut être l'avenir, mais seulement si les services arrivent."])],
      prompt=[r"Sujet de l'essai~: \textbf{Vaut-il mieux vivre dans une grande ville que dans une petite commune~?}"],
      model=[r"Au cours du dernier siècle, des millions de personnes ont quitté la campagne pour chercher une vie meilleure en ville. Aujourd'hui, la question se pose à nouveau. Bien que la ville offre plus de possibilités professionnelles, j'estime que, grâce à la technologie, une petite commune peut offrir une vie plus épanouissante.",
             r"Tout d'abord, les relations humaines y sont plus fortes. Le graphique de la source 2 montre que 72~\% des habitants des petites communes sont satisfaits de leurs relations avec leurs voisins, contre seulement 29~\% dans les grandes villes. Aminata Diallo le confirme dans la source 3~: à Dakar, elle ne connaissait pas ses voisins, alors que dans son village «~le village s'organise pour l'aider~» quand quelqu'un tombe malade. Cette solidarité, que les Sénégalais appellent la teranga quand il s'agit d'accueillir, est difficile à trouver dans une métropole.",
             r"Ensuite, la vie dans une petite commune laisse plus de temps libre. Selon la source 2, 67~\% des habitants des petites communes sont satisfaits de leur temps libre, soit presque le double qu'en ville. Le cas de Karim, dans la source 1, explique pourquoi~: il passe près de deux heures par jour dans les transports.",
             r"Il est vrai que la ville concentre les emplois qualifiés et les hôpitaux, comme le souligne l'urbaniste Thomas Bernard (source 1), et le graphique confirme l'écart d'accès aux soins. Cependant, l'exemple d'Aminata prouve que le télétravail permet déjà d'avoir un bon emploi loin de la capitale, à condition qu'il y ait internet.",
             r"En somme, si les gouvernements apportaient internet et des services de santé dans les campagnes, la petite commune deviendrait pour beaucoup un choix meilleur que la grande ville~: plus de temps, plus de liens et, désormais, des possibilités d'emploi."],
      rows=[("A Position", 1, "clear position (here: a small town can offer a fuller life, given services)", "only lists pros and cons of each place"),
            ("B Source use", 2, "all three sources used accurately and named", "two sources, or a misread chart (e.g., reversing the columns)"),
            ("C Argumentation", 2, "each claim explained with evidence (le confirme, explique pourquoi)", "a summary of each source with no link to the position"),
            ("D Organization", 2, "introduction, claim paragraphs, concession, conclusion; varied transitions", "source-by-source paragraphs"),
            ("E Language control", 3, "varied vocabulary and structures (bien que + subjunctive, relative clauses, si-clause)", "basic sentences, copied phrases")],
      tips=["Every body paragraph combines two sources.", "The cultural reference (la teranga) adds range without leaving the topic.",
            "The concession uses Il est vrai que… Cependant…", "The conclusion's si-clause (si les gouvernements apportaient…, deviendrait) shows control."],
      ask="Write your essay in French (about 300–350 words), then mark it against each row.", lines=22)

GUIDE, QSET = G, Q
