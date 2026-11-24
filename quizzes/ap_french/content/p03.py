from ap_wl.model import Doc

STEM = "03-art-creativity"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 3: Art and Creativity", r"Unit 3 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 3 asks how art expresses identity and values, and how traditions are preserved and reinvented. Its recommended contexts are artistic heritage, architecture, beauty and aesthetics, fashion and design, literature, and the visual and performing arts. Music is the lens of the 2026--27 course project, so this guide gives it the most space: genres and instruments across the French-speaking world, what they express, and how they change. It also covers architecture, painting, literature and comics, the language for describing and evaluating art, and a Project Presentation kit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 11+ \qquad Three factors for my project: \blank[10em]",
        short="Unit 3", sub="Art and Creativity")

G.sec("Music across the French-speaking world")
G.tex(r"""
\begin{vocab}
le genre musical / le rythme & genre / rhythm & \\
les paroles / le refrain & lyrics / chorus & \\
la chanson à texte & song valued for its lyrics & Brel, Brassens, Barbara \\
la kora & West African harp-lute with 21 strings & played by griots \\
le griot, la griotte & hereditary musician and keeper of family history & Mali, Senegal, Guinea \\
l'accordéon & accordion & the \emph{bal musette}; Cajun music \\
le métissage musical & musical blending & \\
composer / interpréter / enregistrer & compose / perform / record & \\
\end{vocab}

\begin{compare}{Genre}{Origin}{What it often expresses}
La chanson française & 20th-century France and Belgium (Piaf, Brel, Brassens) & poetry of everyday life, love, social critique \\
Le zouk & Guadeloupe and Martinique, 1980s (Kassav') & Antillean identity; Creole language \\
Le raï & Oran, Algeria; spread through France & youth, freedom, exile \\
La musique mandingue & Mali, Senegal, Guinea; griots and the kora & memory, genealogy, praise \\
La musique cadienne & Louisiana; accordion and fiddle & survival of French in America \\
Le rap francophone & France, Senegal, Quebec, Belgium & the city, identity, social commentary \\
\end{compare}

\begin{keyidea}[Products, practices, perspectives in music]
\textbf{Product}: a song, the kora, a genre. \textbf{Practice}: griots singing a family's history at a wedding; dancing zouk at a family party; playing in the street on June 21. \textbf{Perspective}: the value behind it (memory, pride in a language, freedom, community). The presentation's culture row asks for the link: practice + \emph{parce que} / \emph{ce qui montre que} + perspective.
\end{keyidea}
""")
G.q("1 Musique", r"Au Mali et au Sénégal, quel est le rôle traditionnel du griot~?",
    "conserver et chanter l'histoire des familles et de la communauté", [("fabriquer des instruments pour les touristes", "Not the traditional role."),
                                                                        ("diriger les cérémonies religieuses", "Griots are musicians and historians, not clergy."),
                                                                        ("enseigner le français à l'école", "Unrelated.")],
    "Griot = musician-historian.", "Griots are hereditary keepers of memory: they recite genealogies and history in song, often with the kora.",
    ["griot → mémoire, généalogie, kora."])
G.q("1 Musique", r"Which sentence links a musical practice to a cultural perspective?",
    "Aux Antilles, on chante le zouk en créole dans les fêtes de famille, ce qui montre la fierté d'une langue longtemps méprisée.",
    [("Le zouk est un genre musical des Antilles.", "A fact about origin, no practice or perspective."),
     ("Kassav' a été fondé en 1979.", "A date, no perspective."),
     ("J'adore danser le zouk.", "A personal preference, not a cultural example.")],
    "Practice + ce qui montre + perspective.", "The top culture score needs a specific practice or product tied to the value behind it.",
    ["Practice: singing zouk in Creole at family parties.", "Perspective: pride in the language."])
G.q("1 Musique", r"Le raï est né",
    "en Algérie, dans la région d'Oran", [("au Québec, à Montréal", "Montreal is known for its jazz festival."),
                                         ("en Louisiane", "Louisiana is the home of Cajun music."),
                                         ("en Belgique", "Belgium gave Brel and Stromae, not raï.")],
    "Raï ← Oran.", "Raï developed in western Algeria and spread through the Algerian community in France.",
    ["raï → Oran, Algérie."])

G.sec("Heritage and architecture")
G.tex(r"""
\begin{vocab}
le patrimoine & heritage & \\
le chef-d'\oe uvre & masterpiece & \\
la cathédrale / la flèche & cathedral / spire & \\
restaurer / la restauration & to restore / restoration & \\
l'architecture en terre & earthen architecture & Djenné \\
le Vieux-Québec & the walled historic center of Quebec City & UNESCO World Heritage \\
\end{vocab}

\begin{compare}{Work or place}{What it is}{Why it matters}
Notre-Dame de Paris & Gothic cathedral; fire in 2019, reopened in December 2024 & national heritage; rebuilt with traditional crafts \\
La Grande Mosquée de Djenné (Mali) & the largest earthen building in the world & every year the town replasters it together (\emph{le crépissage}) \\
La tour Eiffel & built for the 1889 World's Fair & engineering and modernity \\
Le Vieux-Québec & fortified French colonial city & French presence in North America \\
\end{compare}

\textbf{A community practice.} In Djenné, the annual replastering of the mosque is a festival: the whole town takes part, each neighborhood with its task. The practice preserves the building and expresses a perspective: heritage is maintained by the community, not only by experts.
""")
G.q("2 Patrimoine", r"Pourquoi le crépissage annuel de la Grande Mosquée de Djenné est-il un exemple de pratique culturelle~?",
    "parce que toute la communauté participe à l'entretien du bâtiment", [("parce que seuls des architectes étrangers y travaillent", "The townspeople do the work."),
                                                                         ("parce que la mosquée est construite en béton", "It is earthen."),
                                                                         ("parce qu'il a lieu seulement tous les cent ans", "It is annual.")],
    "Community maintenance.", "The practice (collective replastering) reflects the perspective that heritage belongs to and is kept up by the community.",
    ["annuel + toute la ville → pratique collective."])
G.q("2 Patrimoine", r"In December 2024, Notre-Dame de Paris",
    "reopened after its restoration following the 2019 fire", [("was built for the first time", "It dates from the Middle Ages."),
                                                              ("was closed permanently", "It reopened."),
                                                              ("was moved to another city", "No.")],
    "Fire 2019, reopened 2024.", "The cathedral reopened five years after the fire, restored with traditional techniques.",
    ["2019 fire → 2024 reopening."])

G.sec("Visual arts, literature and comics")
G.tex(r"""
\begin{compare}{Artist or movement}{Known for}{Theme}
L'impressionnisme (Monet, \emph{Impression, soleil levant}, 1872) & light, outdoor painting & capturing a moment \\
La négritude (Senghor, Césaire, Damas, 1930s) & poetry and essays & pride in Black identity against colonial contempt \\
Léopold Sédar Senghor & poet; first president of Senegal (1960); Académie française (1983) & culture and politics \\
Victor Hugo, \emph{Les Misérables} (1862) & novel & justice and poverty \\
Antoine de Saint-Exupéry, \emph{Le Petit Prince} (1943) & tale & friendship; ``l'essentiel est invisible pour les yeux'' \\
La bande dessinée (Hergé's \emph{Tintin}, \emph{Astérix}) & comics, the ``ninth art'' & Belgium and France \\
\end{compare}

\textbf{La négritude} was a literary movement founded in Paris by students from Africa and the Caribbean. It reflects the perspective that colonized peoples' cultures deserve pride and a voice of their own.
""")
G.q("3 Arts", r"Le mouvement de la négritude, fondé par Senghor, Césaire et Damas, voulait surtout",
    "affirmer la fierté et la valeur des cultures noires", [("imiter la poésie française classique", "It challenged colonial cultural dominance."),
                                                          ("créer un nouveau style de peinture", "It was literary."),
                                                          ("défendre la colonisation", "The opposite.")],
    "Négritude = Black pride, anti-colonial.", "The movement (1930s) asserted the value of African and Caribbean cultures.",
    ["Senghor, Césaire → fierté noire."])
G.q("3 Arts", r"Which country is especially known for la bande dessinée, home of Tintin?",
    "Belgium", [("Senegal", "No."),
                ("Switzerland", "Not Tintin."),
                ("Canada", "Not Tintin.")],
    "Tintin → Hergé → Belgium.", "Comics are called the ninth art and are central to Belgian culture.",
    ["Hergé, Brussels → Belgium."])

G.sec("Describing and evaluating art")
G.tex(r"""
\begin{compare}{Purpose}{Language}{Example}
Describe & représente, montre, on voit, au premier plan / à l'arrière-plan & Au premier plan, on voit une femme qui joue de la kora. \\
Interpret & évoque, symbolise, exprime, met en valeur & Le bleu évoque la mer et la mélancolie. \\
Evaluate & ce qui me frappe, c'est\ldots; ce que j'apprécie, c'est\ldots & Ce qui me frappe, c'est le mélange de l'ancien et du moderne. \\
Concede & bien que + subjunctive; même si + indicative & Bien que certains la trouvent commerciale, cette musique reflète la vie urbaine. \\
Influence & s'inspirer de, avoir ses racines dans & Le zouk a ses racines dans la biguine et le gwo ka. \\
\end{compare}

\begin{trap}
\emph{Bien que} takes the subjunctive; \emph{même si} takes the indicative. \emph{Bien qu'il soit jeune} / \emph{même s'il est jeune}.
\end{trap}
""")
G.q("4 Décrire", r"Choisissez la bonne forme~: Bien que certains critiques \blank\ que cette musique est trop commerciale, beaucoup de jeunes s'y reconnaissent.",
    "disent", [("dire", "A conjugated verb is needed after bien que."),
               ("diront", "The future cannot follow bien que."),
               ("disaient", "The imparfait indicative cannot follow bien que.")],
    "Bien que + subjunctive (disent).", "Bien que always takes the subjunctive; the subjunctive of dire (ils) is disent, identical to the indicative.",
    ["bien que → subjonctif → (qu'ils) disent."])
G.q("4 Décrire", r"Choisissez la bonne option~: \blank\ me frappe le plus dans ce musée, ce sont les couleurs des tableaux.",
    "Ce qui", [("Ce que", "Ce que is an object; here the clause needs a subject of frappe."),
               ("Qui", "Qui alone cannot introduce this clause."),
               ("Lequel", "Lequel refers to a specific noun.")],
    "Ce qui = what (subject).", "Ce qui (subject) / ce que (object) introduce ideas with no specific antecedent.",
    ["what strikes me (subject) → ce qui."])

G.sec("Task kit: the Project Presentation")
G.tex(r"""
You have 3 minutes to prepare (with your PPR) and 3 minutes to present, about 350--400 words. The prompt asks what you learned in your research; the rubric rewards \textbf{three or more factors, each explained with details}, and a cultural perspective linked to a product or practice.

\begin{terms}
0:00--0:25 & introduction: the question, your focus, the three factors \\
0:25--2:30 & three factors, about 40 seconds each: fact or example from research + why it matters (perspective) \\
2:30--3:00 & conclusion: what the factors show together; a comparison or reflection \\
\end{terms}

\begin{compare}{Move}{Phrases}{}
Open & Aujourd'hui, je vais vous parler de\ldots; Je me suis concentré(e) sur trois aspects~: \ldots & \\
Move on & Premièrement / Deuxièmement / Enfin & \\
Evidence & D'après mes recherches, \ldots; Par exemple, \ldots & \\
Perspective & Cela reflète\ldots; ce qui montre l'importance de\ldots & \\
Close & En conclusion, \ldots; Ce que j'ai appris, c'est que\ldots & \\
\end{compare}

\begin{trap}
Three factors named with no detail earn only 1 point for task; so does one factor explained in depth. Budget time so the third factor gets real detail.
\end{trap}
""")
G.q("5 Présentation", r"A presentation explains three factors, each with a specific example from research, but never links them to what people value. Which row is it most likely to lose points in?",
    "Cultural understanding", [("Task execution", "Three factors with relevant details earn full task credit."),
                               ("Delivery", "Delivery is about pronunciation and pace."),
                               ("Organization", "Nothing suggests poor organization.")],
    "No perspective link → culture row.", "Row B's top score needs a relationship between a perspective and a product or practice.",
    ["Factors and details → task OK.", "No perspective → culture 1 point."])
G.q("5 Présentation", r"About how many words fit in the 3-minute presentation at a natural pace?",
    "350 to 400", [("100 to 150", "That would leave long silences."),
                   ("800 to 900", "That would require rushing, which hurts delivery."),
                   ("50", "That is one short paragraph.")],
    "3 min ≈ 350–400 words.", "At about two words per second, three minutes holds 350–400 words.",
    ["Plan about 120 words per factor."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 3: Art and Creativity: Question Set", r"Unit 3 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Instructional Guidance and an Interview for listening, an Article and Chart and a Promotional Material for reading) on drumming, streaming, a music festival and a young griotte, followed by a practice Project Presentation on music, the 2026--27 project lens, with the 11-point scoring guide and a model script. The presentation prompt is a practice prompt written for this set, not the official 2027 project prompt. As on the exam, questions and choices are in French; listening sources are printed as transcripts. All sources and data are original and fictional. Allow about 25 minutes for the multiple choice and 6 minutes to prepare and deliver the presentation.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Presentation: \blank\ / 11 \qquad Target: 15+ MCQ and 8+ presentation",
        short="Unit 3", sub="Art and Creativity")

Q.sec("Listening: Instructional Guidance")
Q.src(r"Listening 1 \textperiodcentered\ Instructional Guidance (transcript) \textperiodcentered\ «~Votre premier cours de djembé~», un tutoriel vidéo", [
    r"(PROFESSEUR) Bonjour~! Aujourd'hui, vous allez apprendre les trois sons de base du djembé. D'abord, asseyez-vous sur une chaise sans accoudoirs et serrez le djembé entre vos genoux, en l'inclinant légèrement vers l'avant.",
    r"(PROFESSEUR) Ensuite, regardez la peau du tambour. Si vous frappez au centre avec la main à plat, vous obtenez un son grave, la «~basse~». Près du bord, avec les doigts serrés, vous obtenez le son «~tonique~»~; et avec les doigts un peu écartés, le son «~claqué~», plus sec.",
    r"(PROFESSEUR) Commencez lentement~: basse, tonique, tonique~; basse, tonique, tonique. Ne cherchez pas la vitesse. L'essentiel, c'est que le rythme soit régulier.",
    r"(PROFESSEUR) Un dernier conseil~: en Afrique de l'Ouest, le djembé accompagne les fêtes, les mariages et les danses du village. Quand vous jouez, pensez que vous faites partie d'une conversation, pas d'un concert.",
], 5)
Q.q("1.A.1 Detail", r"Selon le professeur, que faut-il faire en premier~?",
    "s'asseoir et tenir le djembé entre ses genoux", [("frapper le centre du tambour", "That comes after sitting correctly."),
                                                     ("jouer le rythme très vite", "He says to start slowly."),
                                                     ("écouter de la musique malienne", "Not one of the steps.")],
    "D'abord, asseyez-vous…", "Instructional Guidance: d'abord marks the first step.",
    ["D'abord, asseyez-vous… serrez le djembé entre vos genoux."])
Q.q("1.A.1 Detail", r"Comment obtient-on le son grave, la «~basse~»~?",
    "en frappant le centre avec la main à plat", [("en frappant le bord avec les doigts serrés", "That gives the tonique."),
                                                 ("en inclinant le djembé vers l'arrière", "He says to tilt it forward."),
                                                 ("en frappant le sol avec les pieds", "No.")],
    "Centre + main à plat = basse.", "Detail (1.A.1): match each zone with its sound.",
    ["au centre avec la main à plat → la basse."])
Q.q("1.B.3 Point of view", r"Selon le professeur, qu'est-ce qui est le plus important au début~?",
    "garder un rythme régulier", [("jouer très vite", "Ne cherchez pas la vitesse."),
                                  ("jouer très fort", "Not mentioned."),
                                  ("improviser de nouveaux rythmes", "He gives one basic pattern.")],
    "L'essentiel, c'est que le rythme soit régulier.", "L'essentiel, c'est… signals the speaker's priority.",
    ["L'essentiel, c'est que le rythme soit régulier."])
Q.q("1.B.4 Organization", r"Comment le tutoriel est-il organisé~?",
    "en étapes successives, de la posture au rythme, avec un conseil final", [("comme une comparaison entre deux instruments", "Only the djembé is discussed."),
                                                                             ("comme une histoire du djembé depuis ses origines", "History appears only in the last tip."),
                                                                             ("comme une série de questions et de réponses", "There is no Q&A.")],
    "D'abord… Ensuite… Commencez… Un dernier conseil.", "Organization (1.B.4): sequence markers order the steps.",
    ["posture → sounds → rhythm → tip."])
Q.q("1.C.3 Inference", r"Que veut dire le professeur par «~vous faites partie d'une conversation, pas d'un concert~»~?",
    "que le djembé sert à partager et à dialoguer avec les autres, pas à se montrer", [("qu'il faut parler pendant qu'on joue", "Figurative misreading."),
                                                                                        ("que le djembé est un instrument de concert classique", "The opposite."),
                                                                                        ("qu'il vaut mieux jouer seul", "The opposite.")],
    "Conversation = participation.", "Inference (1.C.3): in its context (fêtes, mariages, danses), the drum is communal.",
    ["Djembé in village life → sharing, not performing."])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 1 \textperiodcentered\ Article and Chart \textperiodcentered\ «~Qu'écoute la génération Z~?», journal Le Pont", [
    r"Une étude réalisée par une plateforme de streaming auprès de 50~000 utilisateurs francophones de 16 à 24 ans confirme ce que beaucoup de parents soupçonnaient~: le rap domine les écouteurs des jeunes.",
    r"Mais l'étude cache une surprise. Les chansons «~patrimoniales~» --- la chanson française classique, les musiques traditionnelles africaines et antillaises --- ont progressé plus que tous les autres genres l'an dernier, même si elles restent minoritaires. «~Les jeunes découvrent ces chansons grâce aux reprises et aux extraits utilisés sur les réseaux sociaux~», explique la musicologue Hélène Roy. «~Un rappeur échantillonne une kora, et des milliers d'adolescents cherchent qui est la musicienne d'origine.~»",
    r"Pour Roy, la tradition ne disparaît pas~: elle change de forme. «~Chaque génération écoute ses grands-parents à sa manière.~»",
], 5, table=(["Genre", "Part du temps d'écoute", "Évolution en un an"],
             [["Rap et musiques urbaines", "46~\\%", "+4~\\%"], ["Pop", "27~\\%", "−2~\\%"], ["Rock", "12~\\%", "−5~\\%"], ["Chanson et musiques traditionnelles", "6~\\%", "+31~\\%"]]),
      note="Données fictives.")
Q.q("1.A.2 Data", r"Selon le tableau, quel genre représente la plus grande part du temps d'écoute~?",
    "le rap et les musiques urbaines", [("la chanson et les musiques traditionnelles", "They grew most but are only 6%."),
                                        ("la pop", "27%."),
                                        ("le rock", "12%.")],
    "46%.", "Data (1.A.2): read the share column, not growth.",
    ["Share column → 46%."])
Q.q("1.C.1 Connect", r"Quelle donnée du tableau correspond à la «~surprise~» dont parle l'article~?",
    "la hausse de 31~\\% de la chanson et des musiques traditionnelles", [("les 46~\\% du rap", "That confirms what parents suspected."),
                                                                        ("la baisse de 5~\\% du rock", "Rock is not discussed."),
                                                                        ("les 27~\\% de la pop", "Not discussed.")],
    "Surprise = traditional genres grew most.", "Connect (1.C.1): match the article's surprise to the +31% figure.",
    ["ont progressé plus que tous les autres genres → +31%."])
Q.q("1.B.5 Word meaning", r"Dans l'article, «~échantillonne~» signifie que le rappeur",
    "utilise un extrait enregistré de kora dans sa chanson", [("apprend à jouer de la kora", "He uses a recording."),
                                                             ("critique la musique africaine", "No criticism."),
                                                             ("vend une kora ancienne", "Unrelated.")],
    "échantillonner = to sample.", "Word meaning (1.B.5): context (reprises, extraits, musicienne d'origine) shows reuse of a recording.",
    ["extraits + musicienne d'origine → a sample."])
Q.q("1.B.3 Point of view", r"Quelle est l'opinion d'Hélène Roy~?",
    "La tradition musicale ne disparaît pas, elle se transforme.", [("Les jeunes ne s'intéressent plus aux musiques traditionnelles.", "She says they discover them."),
                                                                     ("Le rap détruit la culture francophone.", "She never says so."),
                                                                     ("Les reprises sont un manque de respect.", "She describes them as a way in.")],
    "elle change de forme.", "Point of view (1.B.3): her final quote states her view.",
    ["la tradition ne disparaît pas : elle change de forme."])
Q.q("1.C.2 Conclusion", r"Quelle conclusion l'article permet-il de tirer~?",
    "Les reprises et les extraits peuvent faire découvrir aux jeunes la musique de leurs grands-parents.", [("La chanson traditionnelle dépassera le rap l'an prochain.", "6% versus 46%: not supported."),
                                                                                                            ("La pop progresse plus que jamais.", "Pop fell 2%."),
                                                                                                            ("Les jeunes n'écoutent que de la musique traditionnelle.", "Only 6%.")],
    "Samples → discovery.", "Conclusions (1.C.2) must stay within the evidence.",
    ["A rapper's sample sends listeners to the original musician."])

Q.sec("Reading: Promotional Material")
Q.src(r"Reading 2 \textperiodcentered\ Promotional Material \textperiodcentered\ Une affiche de festival", [
    r"\textbf{FESTIVAL SONS DU FLEUVE 2027 \textperiodcentered\ Saint-Louis du Sénégal}",
    r"Trois jours, quatre scènes et plus de quarante artistes de dix pays. De la kora au zouk, du mbalax au rap en wolof~: la tradition, ça se danse aussi~!",
    r"\textbf{Nouveauté cette année~:} ateliers gratuits de kora, de sabar et de danse avec les musiciens eux-mêmes. Inscription au stand d'accueil (places limitées, premiers arrivés, premiers servis).",
    r"\textbf{Billets~:} pass trois jours, 30~000~FCFA~; gratuit pour les moins de 12 ans. Étudiants sur présentation de la carte~: 50~\% de réduction.",
    r"Du 7 au 9 mai \textperiodcentered\ Quai Henry-Jay \textperiodcentered\ Bouteilles en verre interdites sur le site.",
], 5)
Q.q("1.B.1 Purpose", r"Quel est le but principal de cette affiche~?",
    "inviter le public à un festival de musiques traditionnelles et actuelles", [("annoncer l'ouverture d'une école de musique", "Workshops are one feature of a festival."),
                                                                                ("vendre des instruments de musique", "Only tickets are sold."),
                                                                                ("présenter un concours de danse", "No contest is mentioned.")],
    "Festival poster → invite.", "Purpose (1.B.1): title, dates, place and prices invite people to attend.",
    ["Promotional Material → invitation."])
Q.q("1.A.1 Detail", r"Comment peut-on participer aux ateliers~?",
    "en s'inscrivant au stand d'accueil du festival", [("en achetant un billet spécial en ligne", "The workshops are free; registration is at the stand."),
                                                       ("en apportant son propre instrument", "Not stated."),
                                                       ("en envoyant une vidéo", "Not stated.")],
    "Inscription au stand d'accueil.", "Detail (1.A.1) from the Nouveauté paragraph.",
    ["Inscription au stand d'accueil."])
Q.q("1.C.2 Conclusion", r"Une étudiante avec sa carte achète un pass trois jours. Combien paie-t-elle~?",
    "15~000~FCFA", [("30~000~FCFA", "Students get 50% off."),
                    ("rien", "Only children under 12 enter free."),
                    ("50~FCFA", "50 is the discount percentage, not a price.")],
    "30,000 − 50% = 15,000.", "Apply the details: the pass costs 30,000 FCFA, and students pay half.",
    ["30 000 × 0,5 = 15 000."])
Q.q("1.B.3 Tone", r"Que suggère la phrase «~la tradition, ça se danse aussi~!~»~?",
    "que la musique traditionnelle peut être joyeuse et participative", [("que seuls les experts peuvent danser", "The tone is inclusive."),
                                                                        ("que le festival est un concours de danse", "No contest is mentioned."),
                                                                        ("que la tradition est ennuyeuse", "It contradicts that stereotype.")],
    "Tradition is lively.", "Tone and implied meaning: aussi answers the stereotype that tradition is only for listening.",
    ["aussi → contrary to expectation, it is danceable."])
Q.q("1.A.1 Detail", r"Qu'est-ce qui est interdit sur le site du festival~?",
    "les bouteilles en verre", [("les enfants de moins de 12 ans", "They enter free."),
                                ("la danse devant les scènes", "Dancing is encouraged."),
                                ("les photos", "Not mentioned.")],
    "Bouteilles en verre interdites.", "Detail (1.A.1) from the last line.",
    ["Bouteilles en verre interdites sur le site."])

Q.sec("Listening: Interview")
Q.src(r"Listening 2 \textperiodcentered\ Interview (transcript) \textperiodcentered\ Une jeune griotte malienne", [
    r"(JOURNALISTE) Fatoumata, vous avez 23 ans et vous jouez déjà dans de grands festivals. Comment tout a commencé~?",
    r"(FATOUMATA) Dans la cour de la maison de ma grand-mère, à Bamako. Elle chantait en préparant le repas, et moi, je répétais les noms des ancêtres qu'elle citait. Personne ne m'a donné de cours avant mes douze ans~: chez les griots, on apprend en écoutant, pendant les mariages et les baptêmes.",
    r"(JOURNALISTE) Aujourd'hui, vous mélangez la kora et le hip-hop. Que disent les traditionalistes~?",
    r"(FATOUMATA) Certains pensent que c'est une trahison. Je les respecte, mais je ne suis pas d'accord. La musique mandingue a toujours voyagé et emprunté~; si elle ne changeait pas, elle serait déjà morte.",
    r"(JOURNALISTE) Qu'est-ce que vous ne changeriez jamais~?",
    r"(FATOUMATA) La parole. Un griot est d'abord la mémoire des familles. Avec une kora ou un synthétiseur, si on oublie de transmettre cette mémoire, ce n'est plus notre musique.",
], 5)
Q.q("1.A.1 Detail", r"Où Fatoumata a-t-elle commencé à apprendre la musique~?",
    "dans la cour de la maison de sa grand-mère", [("dans un conservatoire à cinq ans", "No one taught her formally until twelve."),
                                                   ("dans un grand festival", "She plays there now."),
                                                   ("dans une école de hip-hop", "Not mentioned.")],
    "Dans la cour de… ma grand-mère.", "Detail (1.A.1): her first answer.",
    ["Dans la cour de la maison de ma grand-mère…"])
Q.q("1.C.3 Inference", r"Que peut-on déduire sur la manière traditionnelle d'apprendre chez les griots~?",
    "On apprend de façon informelle, en famille et lors des cérémonies.", [("On apprend seulement au conservatoire.", "She says one learns by listening."),
                                                                           ("C'est un art interdit aux femmes.", "Not stated."),
                                                                           ("On apprend en lisant des partitions.", "By listening.")],
    "on apprend en écoutant, pendant les mariages et les baptêmes.", "Inference (1.C.3): informal family transmission.",
    ["en écoutant + mariages et baptêmes."])
Q.q("1.B.3 Attitude", r"Quelle est l'attitude de Fatoumata envers les traditionalistes~?",
    "Elle les respecte, même si elle n'est pas d'accord avec eux.", [("Elle les méprise.", "She says she respects them."),
                                                                     ("Elle est entièrement d'accord avec eux.", "Je ne suis pas d'accord."),
                                                                     ("Elle n'a jamais entendu leurs critiques.", "She quotes them.")],
    "Je les respecte, mais je ne suis pas d'accord.", "Attitude (1.B.3): respectful disagreement.",
    ["Je les respecte, mais…"])
Q.q("1.B.4 Organization", r"Quel argument Fatoumata utilise-t-elle pour défendre le mélange des styles~?",
    "La musique mandingue a toujours voyagé et emprunté.", [("Le hip-hop est plus populaire.", "She does not argue from popularity."),
                                                           ("Les traditionalistes ne savent pas jouer.", "She does not attack them."),
                                                           ("Le public jeune l'exige.", "Not stated.")],
    "a toujours voyagé et emprunté.", "She supports her view with history.",
    ["La musique mandingue a toujours voyagé…"])
Q.q("1.B.5 Word meaning", r"Selon Fatoumata, ce qu'elle ne changerait jamais, c'est «~la parole~», c'est-à-dire",
    "le rôle du griot comme mémoire des familles", [("le fait de parler pendant les concerts", "Literal misreading."),
                                                   ("la langue française", "No."),
                                                   ("le prix des billets", "No.")],
    "La parole = the griot's word, memory.", "Word meaning (1.B.5): she explains it in the next sentence.",
    ["Un griot est d'abord la mémoire des familles."])

Q.frq(kind="Project Presentation", head=r"Question 1 \textperiodcentered\ Project Presentation (practice prompt) \textperiodcentered\ 11 points \textperiodcentered\ 3 + 3 minutes", mins=6,
      directions=[r"Imagine that your project examined how music reflects the values of a French-speaking community. You have 3 minutes to prepare, using your notes, and 3 minutes to present. Explain at least three factors, with specific examples from your research, and show how cultural perspectives relate to cultural products or practices."],
      prompt=[r"Prompt: \textbf{De quelle manière la musique reflète-t-elle les valeurs d'une communauté francophone que vous avez étudiée~?}",
              r"Practice focus (example): Cajun music in Louisiana."],
      model=[r"Aujourd'hui, je vais vous parler de la musique cadienne en Louisiane et de ce qu'elle révèle sur les valeurs de cette communauté francophone. Je me suis concentrée sur trois aspects~: la survie de la langue française, la place de la famille et la transmission entre les générations.",
             r"Premièrement, la musique cadienne a protégé la langue française. D'après mes recherches, à partir de 1921, l'école en Louisiane se faisait uniquement en anglais, et beaucoup d'enfants étaient punis s'ils parlaient français. Pourtant, on continuait à chanter en français dans les bals. Cela montre que la musique était un refuge pour une identité menacée.",
             r"Deuxièmement, cette musique est liée à la famille et à la fête. Le samedi soir, les familles se retrouvaient au bal de maison, le «~fais-dodo~», où l'on dansait au son de l'accordéon et du violon pendant que les bébés dormaient dans une pièce voisine. Cette pratique reflète l'importance de se réunir en famille et entre voisins.",
             r"Enfin, la tradition se transmet aujourd'hui de façon active. Depuis les années 1970, des festivals comme les Festivals acadiens et créoles de Lafayette et des écoles d'immersion en français ont redonné de la fierté aux jeunes. De nombreux musiciens ont appris l'accordéon avec leurs grands-parents, ce qui prouve que la communauté tient à garder ses racines.",
             r"En conclusion, la musique cadienne n'est pas seulement un style~: c'est une façon de résister, de rassembler et de transmettre. Ce que j'ai appris, c'est qu'une chanson peut sauver une langue."],
      rows=[("A Task", 2, "three or more factors, each explained with relevant details from research", "three factors named with no detail, or only one or two factors"),
            ("B Culture", 2, "specific examples linking perspectives (identity, family, roots) to products or practices", "examples with no perspective, or a vague one (1 point)"),
            ("C Organization", 2, "clear introduction, ordered factors, conclusion; varied transitions", "a list of facts with no progression"),
            ("D Language", 3, "wide vocabulary, varied structures, culturally relevant expressions", "a limited set of basic structures"),
            ("E Delivery", 2, "clear pronunciation, natural pace and intonation, little hesitation", "hesitant, monotone or rushed speech")],
      tips=["The introduction names the three factors, so the listener can follow.", "Each factor has a specific example (1921, the fais-dodo, the Lafayette festivals) and a perspective (cela montre, cette pratique reflète).",
            "The conclusion pulls the factors together and adds a reflection.", "About 360 words: three minutes at a natural pace."],
      ask="Prepare for 3 minutes using keywords only, then present aloud for 3 minutes (record yourself if you can). Then mark your presentation.", lines=14)

GUIDE, QSET = G, Q
