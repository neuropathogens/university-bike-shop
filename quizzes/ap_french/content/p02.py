from ap_wl.model import Doc

STEM = "02-language-culture"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 2: Language and Culture", r"Unit 2 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 2 asks how language and customs express identity, and how French lives alongside other languages around the world. Its recommended contexts are customs and celebrations, linguistics, and French in the world. This guide gives the vocabulary of celebrations and of language itself, the traditions most often tested (le 14 juillet, la Fête de la musique, la galette des rois, le Carnaval de Québec, la Tabaski), la francophonie and the varieties of French (Quebec, Belgium, Switzerland, Africa, the Caribbean), anglicisms and false friends, \emph{on} and the causative \emph{faire}, and a Project Q\&A kit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Traditions I can explain in 40 seconds: \blank[8em]",
        short="Unit 2", sub="Language and Culture")

G.sec("Celebrations and traditions")
G.tex(r"""
\begin{vocab}
fêter / célébrer & to celebrate & \\
le défilé / le feu d'artifice & parade / fireworks & le 14 juillet \\
la galette des rois / la fève & kings' cake / the charm inside & whoever finds it is king or queen for the day \\
la Chandeleur & Candlemas, February 2 & crêpes \\
le poisson d'avril & April fool & a paper fish stuck on someone's back \\
le réveillon & Christmas Eve or New Year's Eve dinner & \\
la Tabaski & West African name for Eid al-Adha & a sheep is shared with family and neighbors \\
le patrimoine immatériel & intangible heritage & \\
\end{vocab}

\begin{compare}{Tradition}{When and where}{Perspective it reflects}
Le 14 juillet & France; storming of the Bastille, 1789 & the Republic and its values: liberté, égalité, fraternité \\
La Fête de la musique & June 21, since 1982; now worldwide & music belongs to everyone, amateurs included \\
La galette des rois & January (Epiphany), France and Belgium & sharing; chance decides the ``king'' \\
Le Carnaval de Québec & winter, Quebec City & embracing the cold; joie de vivre \\
La Fête nationale du Québec & June 24 & Quebec identity and the French language \\
La Tabaski & Senegal, Mali, Côte d'Ivoire & faith, family and sharing with those in need \\
\end{compare}
""")
G.q("1 Fêtes", r"Que se passe-t-il quand on trouve la fève dans la galette des rois~?",
    "on devient le roi ou la reine et on porte la couronne", [("on doit payer le gâteau", "Not the tradition."),
                                                             ("on quitte la table", "No."),
                                                             ("on fait une farce aux autres", "That is the poisson d'avril.")],
    "Fève → roi/reine.", "The galette des rois (Epiphany) hides a fève; whoever finds it is crowned for the day.",
    ["fève + couronne → king or queen."])
G.q("1 Fêtes", r"Which perspective does the Fête de la musique (June 21) most directly reflect?",
    "Music belongs to everyone, not only to professionals.", [("Music should only be performed in concert halls.", "The festival takes music into the streets."),
                                                             ("Only classical music is part of culture.", "All genres take part."),
                                                             ("Festivals should be reserved for tourists.", "It is for residents and amateurs.")],
    "Free, open, amateurs welcome → culture as shared.", "The practice (anyone can play in the street) reflects the perspective that culture is a shared good.",
    ["Practice: free street concerts by anyone.", "Perspective: music for all."])
G.q("1 Fêtes", r"Le 14 juillet commémore",
    "la prise de la Bastille en 1789", [("la fin de la Seconde Guerre mondiale", "That is May 8."),
                                        ("la naissance de Napoléon", "No."),
                                        ("la création de l'Union européenne", "No.")],
    "14 juillet = Bastille, 1789.", "The national holiday recalls the storming of the Bastille, a symbol of the Revolution.",
    ["1789 → Révolution."])

G.sec("French in the world")
G.tex(r"""
French is spoken by more than 300 million people on five continents, and most of them now live in Africa. The Organisation internationale de la Francophonie (OIF) brings together close to 90 states and governments. In France, the Académie française (1635) issues recommendations on usage; in Quebec, the Office québécois de la langue française coins French terms for new things.

\begin{compare}{Place}{Feature}{Example}
Quebec & French is the only official language of the province (Charte de la langue française, ``loi 101'', 1977) & \emph{courriel} (email), \emph{magasiner} (to shop), \emph{la fin de semaine} \\
Belgium, Switzerland & different numbers & \emph{septante} (70), \emph{nonante} (90); \emph{huitante} (80) in some Swiss cantons \\
West Africa & French as a shared language among many local languages & Côte d'Ivoire's \emph{nouchi} mixes French and local languages \\
Caribbean, Indian Ocean & French-based creoles & Haitian Creole, the creoles of Guadeloupe, Martinique, Réunion \\
Louisiana & Cajun French & \\
\end{compare}
""")
G.q("2 Francophonie", r"Dans quel pays ou région entendrait-on «~J'ai reçu ton courriel cette fin de semaine~»~?",
    "au Québec", [("en France, uniquement dans les journaux", "France tends to use e-mail/mail and le week-end."),
                  ("en Belgique, uniquement à Bruxelles", "Courriel and fin de semaine are typical of Quebec."),
                  ("au Sénégal, uniquement en wolof", "The sentence is in French.")],
    "courriel + fin de semaine → Quebec.", "Quebec French prefers French coinages (courriel, magasiner, fin de semaine) to English borrowings.",
    ["courriel + fin de semaine → Québec."])
G.q("2 Francophonie", r"Where do most French speakers live today?",
    "in Africa", [("in France", "France is the largest single country, but African countries together have more speakers."),
                  ("in North America", "Quebec and Louisiana are a small share."),
                  ("in Asia", "French is rare in Asia today.")],
    "Most francophones are African.", "Population growth in West and Central Africa means most French speakers now live in Africa.",
    ["OIF data → Africa."])

G.sec("Linguistics: borrowings, false friends, slang")
G.tex(r"""
\begin{compare}{Topic}{What happens}{Examples}
Anglicisms & English words used in French & le week-end, le parking, le streaming; Quebec prefers French forms \\
Official equivalents & coined by France or Quebec & \emph{courriel}, \emph{baladodiffusion} / \emph{balado} (podcast), \emph{clavarder} (to chat online) \\
Verlan & syllables reversed (\emph{l'envers}) & \emph{meuf} (femme), \emph{relou} (lourd), \emph{chelou} (louche) \\
Words from Arabic & centuries of contact & \emph{algèbre}, \emph{café}, \emph{magasin}, \emph{toubib} \\
\end{compare}

\begin{trap}[False friends]
\emph{la librairie} = bookstore (library: \emph{la bibliothèque}); \emph{actuellement} = currently; \emph{éventuellement} = possibly; \emph{assister à} = to attend; \emph{sensible} = sensitive; \emph{rester} = to stay.
\end{trap}
""")
G.q("3 Linguistique", r"Le mot «~relou~» est un exemple de",
    "verlan", [("créole haïtien", "Relou comes from reversing lourd."),
               ("québécisme officiel", "It is slang, not an official term."),
               ("mot d'origine arabe", "No.")],
    "relou ← lourd (verlan).", "Verlan reverses syllables: lourd → relou, femme → meuf.",
    ["lourd reversed → relou."])
G.q("3 Linguistique", r"Un étudiant écrit~: «~Je vais à la librairie pour emprunter un livre~». Quel mot aurait-il dû utiliser~?",
    "la bibliothèque", [("la libraire", "A libraire is a bookseller."),
                        ("le livre", "A livre is a book."),
                        ("la boutique", "A boutique is a shop.")],
    "library = bibliothèque.", "La librairie is a false friend: it means bookstore, where you buy, not borrow.",
    ["borrow (emprunter) → bibliothèque."])

G.sec("Structures: on, the passive and the causative faire")
G.tex(r"""
\begin{compare}{Use}{Pattern}{Example}
on & people in general; spoken ``we'' & En France, on fête la Chandeleur avec des crêpes. \\
Pronominal passive & se + verb, often for customs & La galette se partage entre amis. \\
Passive with être & être + participle (+ par) & La fête a été créée en 1982. \\
Causative faire & faire + infinitive: have something done & Nous avons fait venir un groupe de musique. \\
Reflexive & to oneself & Les gens se déguisent pour le carnaval. \\
\end{compare}

\begin{keyidea}[Why it matters]
\emph{On} and the pronominal passive let you describe customs without naming who does them: \emph{On mange des crêpes~; la galette se partage}. That is exactly what Q\&A answers about traditions need.
\end{keyidea}
""")
G.q("4 Structures", r"Choisissez la bonne forme~: Pendant le carnaval, les enfants \blank\ en personnages célèbres.",
    "se déguisent", [("déguisent", "Se déguiser (to dress up) is pronominal."),
                     ("se déguise", "The verb agrees with les enfants (plural)."),
                     ("sont déguiser", "Être + infinitive is not a structure.")],
    "se déguiser, plural.", "Pronominal verbs keep their pronoun: les enfants se déguisent.",
    ["les enfants (plural) + se déguiser → se déguisent."])
G.q("4 Structures", r"Which sentence means ``We had a band come for the party''?",
    "Nous avons fait venir un groupe pour la fête.", [("Nous sommes venus avec un groupe pour la fête.", "This says we came with a band."),
                                                       ("Nous avons venu un groupe pour la fête.", "Venir takes être and cannot take a direct object."),
                                                       ("Un groupe nous a fait la fête.", "Faire la fête means to party.")],
    "faire + infinitive = have someone do something.", "The causative faire: faire venir, faire construire, faire réparer.",
    ["have a band come → faire venir un groupe."])

G.sec("Task kit: the Project Q\\&A")
G.tex(r"""
The four recorded questions follow your presentation. You hear each twice and have 40 seconds to answer. Questions usually ask you to expand on a factor, give an example, compare with your own community, and reflect on what you learned.

\begin{compare}{Question type}{Opening}{Then}
Expand & Comme je l'ai dit dans ma présentation, \ldots & add one new fact from your research \\
Example & Un bon exemple, c'est\ldots & say why it matters (perspective) \\
Compare & Dans ma communauté, en revanche, \ldots & one similarity or difference, then why \\
Reflect & Ce qui m'a le plus surpris, c'est\ldots & what it taught you about the culture \\
\end{compare}

\begin{keyidea}[The culture row in 40 seconds]
You need one answer with a cultural comparison \emph{or} a link between a perspective and a product or practice. Plan it before the exam: \emph{Aux Antilles, on danse le zouk en famille aux fêtes, ce qui montre la fierté de la langue créole~; chez moi, en revanche, \ldots}
\end{keyidea}

\begin{trap}
Forty seconds is about 70--90 words. Answer the question in the first sentence, then support it. Do not restart your presentation.
\end{trap}
""")
G.q("5 Q&A", r"The interlocutor asks: En quoi la tradition que vous avez étudiée ressemble-t-elle à une tradition de votre communauté~? What does a strong answer need?",
    "a specific similarity or difference and what it shows about each culture", [("a summary of the whole presentation", "Repeating the presentation does not answer the question."),
                                                                                 ("a list of facts about the tradition only", "The question asks for a comparison."),
                                                                                 ("a description of how you did the research", "The research process is not the topic.")],
    "Compare + explain.", "A cultural comparison that explains what each practice reflects can earn the top culture score.",
    ["Similarity/difference → why → perspective."])
G.q("5 Q&A", r"About how many words fit in a 40-second Q\&A answer at a natural pace?",
    "70 to 90", [("15 to 20", "That is about one sentence, too short to be complete."),
                 ("200 to 250", "That would require very fast speech."),
                 ("400", "That is a full written essay.")],
    "40 s ≈ 70–90 words.", "At about two words per second, 40 seconds holds four to six sentences.",
    ["Plan: answer + example + why."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 2: Language and Culture: Question Set", r"Unit 2 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (a Presentation and an Audio and Chart for listening, a Literary Text and an Article for reading) on French in Africa, the galette des rois, Quebec French and celebrations, followed by a practice Project Q\&A on music, the 2026--27 project lens, with the 9-point scoring guide and model answers. The Q\&A questions are practice questions written for this set, not official prompts. As on the exam, questions and choices are in French; listening sources are printed as transcripts. All sources and data are original and fictional. Allow about 25 minutes for the multiple choice and 10 minutes for the Q\&A.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Q\&A: \blank\ / 9 \qquad Target: 15+ MCQ and 6+ Q\&A \qquad Pace: 75 s per item",
        short="Unit 2", sub="Language and Culture")

Q.sec("Listening: Presentation")
Q.src(r"Listening 1 \textperiodcentered\ Presentation (transcript) \textperiodcentered\ Une conférence sur le français en Afrique", [
    r"(PROFESSEURE) Quand on pense à la langue française, on imagine souvent Paris. Pourtant, aujourd'hui, la majorité des francophones vivent en Afrique, et ce sera encore plus vrai dans les prochaines décennies.",
    r"(PROFESSEURE) Dans des pays comme la Côte d'Ivoire ou le Sénégal, le français est la langue de l'école et de l'administration, mais il cohabite avec des dizaines de langues locales. Les jeunes d'Abidjan ont même créé le «~nouchi~», un parler qui mélange le français, le dioula et d'autres langues, et qu'on entend dans la musique et sur les réseaux sociaux.",
    r"(PROFESSEURE) Certains puristes y voient une menace pour le «~bon français~». Les linguistes, eux, y voient la preuve que la langue est vivante~: elle s'adapte à ceux qui la parlent.",
    r"(PROFESSEURE) En conclusion, l'avenir du français ne se décidera pas seulement à Paris, mais à Abidjan, à Dakar et à Kinshasa.",
], 5)
Q.q("1.B.1 Main idea", r"Quelle est l'idée principale de la conférence~?",
    "L'avenir du français se joue de plus en plus en Afrique.", [("Le français disparaît en Afrique.", "The speaker describes growth, not decline."),
                                                                 ("Paris reste le seul centre de la langue française.", "The conclusion says the opposite."),
                                                                 ("Le nouchi est une langue officielle.", "Nouchi is an informal way of speaking.")],
    "Conclusion = main idea.", "The concluding sentence (en conclusion…) states the main idea.",
    ["l'avenir du français ne se décidera pas seulement à Paris…"])
Q.q("1.A.1 Detail", r"Selon la professeure, quel est le rôle du français dans des pays comme le Sénégal~?",
    "C'est la langue de l'école et de l'administration.", [("C'est la seule langue parlée à la maison.", "It coexists with dozens of local languages."),
                                                          ("C'est une langue interdite.", "No."),
                                                          ("C'est la langue des personnes âgées uniquement.", "No.")],
    "école + administration.", "Detail (1.A.1).",
    ["le français est la langue de l'école et de l'administration."])
Q.q("1.B.5 Word meaning", r"D'après la conférence, qu'est-ce que le «~nouchi~»~?",
    "un parler qui mélange le français et des langues locales", [("une danse traditionnelle ivoirienne", "It is a way of speaking."),
                                                               ("une loi sur la langue", "No."),
                                                               ("un dialecte du portugais", "No.")],
    "Defined in the source.", "Definitions inside the source answer word-meaning questions.",
    ["un parler qui mélange le français, le dioula…"])
Q.q("1.B.3 Point of view", r"Que pensent les linguistes du nouchi, selon la professeure~?",
    "qu'il prouve que la langue est vivante", [("qu'il menace le bon français", "That is the purists' view."),
                                              ("qu'il faut l'interdire à l'école", "Not stated."),
                                              ("que seuls les adultes le parlent", "Young people created it.")],
    "Les linguistes, eux, y voient…", "Point of view (1.B.3): separate the purists' view from the linguists'.",
    ["Les linguistes, eux, y voient la preuve que la langue est vivante."])
Q.q("1.B.4 Organization", r"Comment la professeure commence-t-elle sa conférence~?",
    "en corrigeant une idée reçue", [("par une définition du nouchi", "That comes in the second paragraph."),
                                    ("par une statistique sur Paris", "No statistic is given."),
                                    ("par une anecdote personnelle", "No anecdote.")],
    "On imagine souvent… Pourtant…", "Organization (1.B.4): a common assumption, then pourtant and the correction.",
    ["on imagine souvent Paris. Pourtant…"])

Q.sec("Reading: Literary Text")
Q.src(r"Reading 1 \textperiodcentered\ Literary Text \textperiodcentered\ «~La fève~» (extrait d'une nouvelle)", [
    r"Chaque année, le premier dimanche de janvier, ma grand-mère posait la galette au milieu de la table comme on pose une couronne sur un coussin. Cette année-là, j'avais neuf ans, et c'était à moi, la plus jeune, de me glisser sous la table.",
    r"—~Pour qui ce morceau~? demandait mamie en levant le couteau.",
    r"—~Pour papa~! criais-je, puis pour tonton, pour maman, pour mamie\ldots~ J'attribuais les parts au hasard, ou du moins je le croyais.",
    r"Quand ma dent heurta quelque chose de dur, je compris tout de suite. Je levai la petite fève de porcelaine comme un trophée. Mamie me posa la couronne de papier doré sur la tête et sourit d'un air entendu à mon père. Ce n'est que des années plus tard que j'ai su qu'elle marquait toujours, d'un petit trait de couteau, la part du plus jeune.",
], 5)
Q.q("1.A.1 Detail", r"Quel était le rôle de la narratrice pendant le partage de la galette~?",
    "Elle se cachait sous la table et désignait à qui donner chaque part.", [("Elle coupait la galette avec le couteau.", "Her grandmother cut it."),
                                                                             ("Elle préparait la galette avec sa grand-mère.", "Not stated."),
                                                                             ("Elle distribuait les couronnes.", "The grandmother placed the crown.")],
    "Sous la table + Pour papa~!", "Detail (1.A.1).",
    ["me glisser sous la table… Pour papa !"])
Q.q("1.C.3 Inference", r"Que suggère la dernière phrase du texte~?",
    "La grand-mère s'arrangeait pour que la plus jeune trouve la fève.", [("La narratrice trichait pour gagner.", "She believed the shares were random."),
                                                                          ("Le père avait caché la fève.", "The grandmother marked the slice."),
                                                                          ("La fève était perdue chaque année.", "No.")],
    "Marked slice → guaranteed win.", "Inference (1.C.3): the grandmother's knowing smile and the knife mark show a loving trick.",
    ["elle marquait toujours… la part du plus jeune."])
Q.q("1.B.5 Word meaning", r"Dans le texte, «~d'un air entendu~» signifie",
    "avec un air de complicité, comme quelqu'un qui partage un secret", [("avec un air fatigué", "No."),
                                                                         ("après avoir bien écouté", "Entendu here does not mean heard."),
                                                                         ("avec colère", "No.")],
    "air entendu = knowing look.", "Word meaning (1.B.5): the smile to the father reveals a shared secret.",
    ["sourit d'un air entendu à mon père → complicity."])
Q.q("1.B.3 Tone", r"Quel ton domine dans cet extrait~?",
    "tendre et nostalgique", [("tragique", "Nothing tragic happens."),
                              ("indigné", "The narrator is not angry."),
                              ("scientifique", "The text is a personal memory.")],
    "Childhood memory + discovered kindness.", "Tone (1.B.3): an affectionate memory told from adulthood.",
    ["Ce n'est que des années plus tard… → looking back fondly."])
Q.q("1.C.2 Conclusion", r"Que révèle cette scène sur la tradition familiale~?",
    "La tradition sert surtout à faire plaisir aux enfants et à réunir la famille.", [("La tradition est une compétition sérieuse entre adultes.", "The grandmother makes sure the child wins."),
                                                                                       ("La famille n'aime pas la galette.", "No."),
                                                                                       ("La tradition a disparu dans cette famille.", "It happens every year.")],
    "Ritual for the child and family.", "Conclusions (1.C.2): the staged chance shows the ritual's real purpose.",
    ["A rigged game for the youngest → the point is joy and togetherness."])

Q.sec("Reading: Article")
Q.src(r"Reading 2 \textperiodcentered\ Article \textperiodcentered\ «~Pourquoi le Québec dit courriel~», magazine Langues vivantes", [
    r"«~Envoie-moi un courriel~», «~je vais magasiner en fin de semaine~»~: pour un Français, ces phrases sonnent parfois étrangement. Pour un Québécois, elles sont parfaitement normales.",
    r"Entouré de plus de 300 millions d'anglophones en Amérique du Nord, le Québec protège sa langue avec soin. Depuis 1977, la Charte de la langue française, surnommée «~loi 101~», fait du français la langue officielle de la province, de l'affichage commercial et, en grande partie, de l'école.",
    r"L'Office québécois de la langue française propose aussi des mots français pour les nouvelles réalités. Le mot «~courriel~», contraction de «~courrier électronique~», est né au Québec avant d'être recommandé en France. «~Ici, utiliser un mot anglais quand il existe un mot français, c'est presque un choix politique~», explique la linguiste Julie Gagnon.",
    r"Les jeunes Montréalais, pourtant, mélangent volontiers le français et l'anglais entre amis. Pour Gagnon, ce n'est pas contradictoire~: «~On peut aimer sa langue et jouer avec elle.~»",
], 5)
Q.q("1.B.1 Purpose", r"Quel est le but de l'article~?",
    "expliquer pourquoi le Québec utilise des mots français à la place de mots anglais", [("critiquer le français de France", "No criticism."),
                                                                                         ("apprendre l'anglais aux Québécois", "No."),
                                                                                         ("raconter l'histoire de Montréal", "Montreal is a detail.")],
    "Pourquoi le Québec dit courriel.", "Purpose (1.B.1): the title and paragraphs explain the reasons.",
    ["context → law → Office → nuance."])
Q.q("1.A.1 Detail", r"Que fait la loi 101, selon l'article~?",
    "Elle fait du français la langue officielle du Québec.", [("Elle interdit l'anglais à la maison.", "It covers public life, not homes."),
                                                             ("Elle crée l'Office de la langue française de France.", "No."),
                                                             ("Elle oblige les Français à dire courriel.", "No.")],
    "Langue officielle de la province.", "Detail (1.A.1).",
    ["fait du français la langue officielle de la province…"])
Q.q("1.C.3 Inference", r"Pourquoi l'article mentionne-t-il «~plus de 300 millions d'anglophones~»~?",
    "pour expliquer pourquoi le Québec ressent le besoin de protéger le français", [("pour montrer que l'anglais est facile", "Not the point."),
                                                                                   ("pour comparer les populations du Canada et de la France", "No."),
                                                                                   ("pour encourager l'apprentissage de l'anglais", "No.")],
    "Minority position → protection.", "Inference (1.C.3): the number explains the need that follows (protège sa langue avec soin).",
    ["surrounded by English speakers → protection."])
Q.q("1.B.3 Point of view", r"Selon Julie Gagnon, que signifie utiliser un mot anglais au Québec~?",
    "C'est presque un choix politique.", [("C'est une preuve d'intelligence.", "No."),
                                         ("C'est interdit par la loi.", "She does not say it is illegal."),
                                         ("C'est sans importance.", "She says the opposite.")],
    "presque un choix politique.", "Point of view (1.B.3): quoted directly.",
    ["c'est presque un choix politique."])
Q.q("1.C.2 Conclusion", r"Quelle conclusion peut-on tirer du dernier paragraphe~?",
    "Protéger le français n'empêche pas les jeunes de mélanger les langues entre amis.", [("Les jeunes Montréalais refusent de parler français.", "They mix languages; they do not refuse French."),
                                                                                          ("La loi 101 interdit de parler anglais entre amis.", "No."),
                                                                                          ("Julie Gagnon condamne les jeunes.", "She says it is not contradictory.")],
    "On peut aimer sa langue et jouer avec elle.", "Conclusions (1.C.2): the final quote reconciles the two facts.",
    ["mélangent volontiers… ce n'est pas contradictoire."])

Q.sec("Listening: Audio and Chart")
Q.src(r"Listening 2 \textperiodcentered\ Audio and Chart (transcript) \textperiodcentered\ «~Les fêtes qui comptent~», Radio Jeunes", [
    r"(ANIMATEUR) Un institut de sondage a demandé à 2~000 jeunes Français de 15 à 24 ans quelles fêtes comptaient le plus pour eux. Les résultats surprennent.",
    r"(ANIMATEUR) Noël reste en tête, mais la Fête de la musique a beaucoup progressé~: il y a dix ans, elle était quatrième~; aujourd'hui, elle est deuxième. Les chercheurs pensent que les concerts gratuits et la possibilité de jouer soi-même dans la rue attirent les jeunes.",
    r"(ANIMATEUR) En revanche, le 14 juillet recule. Beaucoup de jeunes disent qu'ils regardent le feu d'artifice, mais qu'ils pensent moins à la signification historique de la fête.",
], 5, table=(["Fête", "2014", "2024"], [["Noël", "1\\textsuperscript{re}", "1\\textsuperscript{re}"], ["Fête de la musique", "4\\textsuperscript{e}", "2\\textsuperscript{e}"], ["14 juillet", "2\\textsuperscript{e}", "3\\textsuperscript{e}"], ["Nouvel An", "3\\textsuperscript{e}", "4\\textsuperscript{e}"]]),
      note="Tableau~: rang de chaque fête parmi les plus importantes pour les jeunes (données fictives).")
Q.q("1.A.2 Data", r"Que montre le tableau sur les changements entre 2014 et 2024~?",
    "Le 14 juillet et le Nouvel An ont chacun perdu une place.", [("La Fête de la musique a perdu deux places.", "It gained two places."),
                                                                  ("Noël a perdu une place.", "Noël stayed first."),
                                                                  ("Seul le Nouvel An a reculé, de deux places.", "Nouvel An fell one place, and the 14 juillet also fell.")],
    "14 juillet 2→3, Nouvel An 3→4.", "Data (1.A.2): compare each row's two columns.",
    ["Two holidays each fell one place."])
Q.q("1.C.1 Connect", r"Comment l'enregistrement explique-t-il l'évolution de la Fête de la musique visible dans le tableau~?",
    "par les concerts gratuits et la possibilité de jouer dans la rue", [("par un changement de date", "The date did not change."),
                                                                        ("par une nouvelle loi", "Not mentioned."),
                                                                        ("par la baisse du tourisme", "Not mentioned.")],
    "Table: 4e → 2e; audio: free concerts + playing.", "Connect (1.C.1): the table shows the rise; the audio explains it.",
    ["concerts gratuits et la possibilité de jouer soi-même dans la rue."])
Q.q("1.C.3 Inference", r"Que peut-on déduire de l'attitude des jeunes envers le 14 juillet~?",
    "Ils apprécient le spectacle mais accordent moins d'importance à son histoire.", [("Ils ne le fêtent pas du tout.", "They watch the fireworks."),
                                                                                      ("C'est leur fête préférée.", "It is third."),
                                                                                      ("Ils le préfèrent à Noël.", "Noël is first.")],
    "Feu d'artifice, oui; histoire, moins.", "Inference (1.C.3) from the stated reason.",
    ["ils regardent le feu d'artifice, mais… pensent moins à la signification."])
Q.q("1.A.1 Detail", r"Combien de jeunes ont été interrogés~?",
    "2~000", [("15", "15–24 is the age range."),
              ("24", "15–24 is the age range."),
              ("10~000", "Not stated.")],
    "2,000 young people.", "Detail (1.A.1): keep numbers apart (sample size vs. ages).",
    ["a demandé à 2 000 jeunes Français de 15 à 24 ans."])
Q.q("1.B.1 Main idea", r"Quelle est l'idée centrale de ce reportage~?",
    "Les préférences des jeunes pour les fêtes ont changé en dix ans.", [("Les jeunes ne fêtent plus rien.", "They rank several holidays."),
                                                                          ("Le Nouvel An est la fête la plus importante.", "It is fourth."),
                                                                          ("Les concerts n'intéressent pas les jeunes.", "Free concerts attract them.")],
    "Change over ten years.", "Main idea (1.B.1): two years compared and explained.",
    ["2014 vs. 2024 + reasons."])

Q.frq(kind="Project Q&A", head=r"Question 2 \textperiodcentered\ Project Q\&A (practice) \textperiodcentered\ 9 points \textperiodcentered\ 4 answers of 40 seconds", mins=8,
      directions=[r"Imagine that your project examined how music expresses identity in a French-speaking community, and that your presentation focused on zouk in Guadeloupe and Martinique (for example, the group Kassav', founded in 1979, which sings in Antillean Creole). You will hear four questions. Each is played twice; you have 40 seconds to answer each one. Answer in French."],
      prompt=[r"1. Dans votre présentation, vous avez parlé du zouk. Pourquoi est-il important que beaucoup de chansons soient en créole~?",
              r"2. Pouvez-vous donner un exemple concret de la place de cette musique dans la vie des familles~?",
              r"3. Existe-t-il dans votre communauté une musique qui joue un rôle semblable~? Comparez.",
              r"4. Qu'est-ce qui vous a le plus surpris pendant votre recherche~?"],
      model=[r"\textbf{1.} C'est important parce que le créole est la langue de la maison pour beaucoup d'Antillais. Pendant longtemps, on le considérait comme une langue inférieure, et on l'interdisait parfois à l'école. Quand Kassav' a chanté en créole dans le monde entier, cela a montré une grande fierté pour cette identité antillaise.",
             r"\textbf{2.} Oui. Dans les fêtes de famille, par exemple les mariages ou les anniversaires, il est très courant qu'on danse le zouk, des grands-parents aux petits-enfants. La musique n'est pas seulement un spectacle~: c'est une manière de réunir la famille.",
             r"\textbf{3.} Dans ma communauté haïtienne, à Miami, le kompa joue un rôle semblable. Comme le zouk, on le danse dans les fêtes familiales et il rappelle d'où vient la famille. La différence, c'est que nous l'écoutons loin de notre pays d'origine, alors il représente aussi la nostalgie.",
             r"\textbf{4.} Ce qui m'a le plus surpris, c'est que des groupes de jeunes mélangent aujourd'hui le zouk avec le rap et l'électro. Je pensais que c'était une musique de nos parents, mais les jeunes se l'approprient, ce qui prouve qu'une tradition peut se renouveler."],
      rows=[("A Task", 2, "four relevant, complete answers that address each question", "answers that drift back to the presentation or stop after one sentence"),
            ("B Culture", 2, "in at least one answer, a cultural comparison (answer 3) or a perspective linked to a product or practice (answers 1 and 2)", "only describing the songs (1 point)"),
            ("C Language", 3, "varied vocabulary and structures (on, passive, subjunctive, relative clauses)", "short, repetitive sentences"),
            ("D Fluency", 2, "natural pace and intonation, clear pronunciation, few pauses", "long silences, many restarts")],
      tips=["Each answer starts by answering the question directly.", "Answer 3 is a full cultural comparison: similarity, difference, and why.",
            "Answer 1 links a product (songs in Creole) to a perspective (pride in Antillean identity).", "About 70–80 words each fits 40 seconds."],
      ask="Answer each question aloud in French (40 seconds each), jotting keywords first; then mark your answers.", lines=12)

GUIDE, QSET = G, Q
