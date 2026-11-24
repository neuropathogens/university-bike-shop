from ap_wl.model import Doc

STEM = "01-families-communities"

# ======================================================================================= guide
G = Doc(STEM, "guide", "Unit 1: Families and Communities", r"Unit 1 \textperiodcentered\ Study Guide",
        abstract=r"""Unit 1 asks what makes a family, how families shape values and traditions, and how communities are changing. Its recommended contexts are family relationships, community activities, social interactions and relationships, and urban and rural communities. This guide gives the vocabulary the exam assumes, the cultural products, practices and perspectives most often tested (in-group and out-group, respect for elders, neighborhood associations and the circulating notice board, sharing with neighbors, depopulation, vacant houses and hometown tax donations), the structures for relationships and routines, and an Email Response kit. Each section ends with check questions; the key is on the last page.""",
        scoring=r"Check questions: \blank\ / \qtotal \qquad Target: 10+ \qquad Words I keep forgetting: \blank[10em]",
        short="Unit 1", sub="Families and Communities")

G.sec("Family and relationships")
G.tex(r"""
\begin{vocab}
家族（かぞく） & family & \\
核家族（かくかぞく） & nuclear family & now the most common household with children \\
三世代同居（さんせだいどうきょ） & three generations under one roof & less common than before \\
共働き（ともばたらき） & both parents working & \\
育児休業（いくじきゅうぎょう） & parental leave & often shortened to 育休 \\
親孝行（おやこうこう） & devotion to one's parents & \\
敬老の日（けいろうのひ） & Respect for the Aged Day & third Monday of September \\
\end{vocab}

\begin{keyidea}[内と外: in-group and out-group]
Japanese distinguishes 内 (\emph{uchi}, one's own group: family, company, team) from 外 (\emph{soto}, outsiders). The distinction shapes language: you use humble forms for your own family when speaking to outsiders (母, not お母さん: 母は今出かけております) and honorific forms for the other person's family (お母さんはお元気ですか). It also shapes practices such as gift-giving and greetings.
\end{keyidea}

\begin{compare}{Practice}{What it looks like}{Perspective often cited}
敬老の日 & a national holiday; communities honor older residents, grandchildren send cards & respect for elders and their experience \\
Grandparents' help & grandparents often help with childcare when both parents work & mutual support across generations \\
Family terms & older siblings are called お兄さん, お姉さん rather than by name & age and position in the family matter \\
\end{compare}
""")
G.q("1 Family", r"Which word describes a household in which both parents work?",
    "共働き", [("核家族", "核家族 means a nuclear family, regardless of who works."),
              ("三世代同居", "三世代同居 means three generations living together."),
              ("親孝行", "親孝行 means devotion to one's parents.")],
    "共働き = dual income.", "共 (together) + 働き (working): both partners work.",
    ["共働き → both parents work."])
G.q("1 Family", r"Speaking to a visitor, a student says 母は今出かけております, not お母さんは今出かけています. Which perspective does this reflect?",
    "Speakers lower their own in-group when talking to outsiders.", [("Mothers are less important than fathers.", "The humble form is about in-group and out-group, not rank in the family."),
                                                                     ("Visitors should not ask about family.", "Not implied."),
                                                                     ("Polite language is only for teachers.", "Humble forms are used with any outsider.")],
    "内と外 → humble forms for one's own family.", "Calling your own mother 母 and using humble おります shows respect to the listener by lowering your in-group.",
    ["母 (my mother, humble) + おります (humble) → speaking to an outsider."])

G.sec("Community and social life")
G.tex(r"""
\begin{vocab}
町内会（ちょうないかい） / 自治会 & neighborhood association & runs festivals, cleanups, disaster drills \\
回覧板（かいらんばん） & circulating notice board & passed by hand from house to house \\
近所づきあい & relations with neighbors & \\
お裾分け（おすそわけ） & sharing extra food or gifts with neighbors & \\
引っ越しのあいさつ & greeting new neighbors when moving in & often with a small gift such as towels or sweets \\
夏祭り / 盆踊り & summer festival / Bon dance & \\
ボランティア & volunteer & \\
\end{vocab}

\textbf{Practices and perspectives.} The 回覧板 travels from door to door with news about cleanups and festivals; each household reads it, stamps it and passes it on. When someone moves in, they visit the neighbors with a small gift. Both practices reflect a perspective that a neighborhood runs on small, shared responsibilities and on being considerate to those around you.
""")
G.q("2 Community", r"What is a 回覧板?",
    "a notice board passed by hand from house to house in a neighborhood", [("a bulletin board at a train station", "It travels between homes."),
                                                                             ("a school report card", "No."),
                                                                             ("a festival float", "No.")],
    "回覧 = circulate and read.", "Neighborhood associations use the 回覧板 to share news; each household reads it and passes it on.",
    ["回覧 (circulating) + 板 (board)."])
G.q("2 Community", r"A family receives more persimmons than they can eat and shares some with the neighbors (お裾分け). Which perspective does this practice most directly reflect?",
    "Good relations with neighbors are kept up through small acts of sharing.", [("Food should never be wasted, so it should be sold.", "The food is given, not sold."),
                                                                                ("Neighbors should not talk to each other.", "The opposite."),
                                                                                ("Only relatives should receive gifts.", "Neighbors receive them.")],
    "お裾分け ↔ neighborliness.", "Sharing extra food (practice) keeps neighborhood relationships warm (perspective).",
    ["お裾分け → share with neighbors."])

G.sec("Urban and rural communities")
G.tex(r"""
\begin{vocab}
都会（とかい） / 地方（ちほう） & big city / the regions outside the big cities & \\
東京一極集中 & concentration of people and jobs in Tokyo & \\
過疎化（かそか） & depopulation & villages losing young people \\
空き家（あきや） & vacant house & about 9 million in 2023 \\
地方移住（ちほういじゅう） & moving from a city to the regions & \\
Uターン / Iターン & returning to one's hometown / moving to a region one is not from & \\
ふるさと納税 & hometown tax donation & since 2008: donate to a town, receive local products \\
\end{vocab}

\textbf{Cases.} As young people move to Tokyo and other big cities, many rural towns are aging and shrinking, and vacant houses multiply. Towns respond with vacant-house banks (空き家バンク) that match houses with newcomers, support for remote workers, and the hometown tax donation system, which lets city residents send part of their taxes to a town of their choice in exchange for local products.
""")
G.q("3 City and region", r"Which word describes a village losing most of its young people?",
    "過疎化", [("共働き", "That means both parents working."),
              ("お裾分け", "That means sharing extra food with neighbors."),
              ("一極集中", "That describes the concentration in Tokyo, the other side of the trend.")],
    "過疎 = sparse population.", "過疎化 is the process of a community becoming depopulated.",
    ["過 (too) + 疎 (sparse) + 化 (becoming)."])
G.q("3 City and region", r"What does a city resident receive for a hometown tax donation (ふるさと納税)?",
    "local products from the town that receives the donation", [("a new house in the town", "Vacant-house banks are a different program."),
                                                               ("free train tickets to Tokyo", "No."),
                                                               ("a job in the town hall", "No.")],
    "Donation → thank-you gift of local products.", "Since 2008, residents can direct part of their taxes to a town and receive local specialties in return.",
    ["ふるさと (hometown) + 納税 (paying tax)."])

G.sec("Structures for relationships and routines")
G.tex(r"""
\begin{compare}{Structure}{Use}{Example}
V-てくれる / てもらう / てあげる & favors between people & 祖母が昔の話をしてくれました。 \\
V-ことにする & I decide to & 毎週祖父母の家に行くことにしました。 \\
V-ことになる & it has been decided (by others or circumstances) & 来月、引っ越すことになりました。 \\
V-ようになる & change: come to, start to & 一人で料理ができるようになりました。 \\
V-ために & purpose & 家族と話すために、日本語を勉強しています。 \\
V-ながら & while & 母と話しながら、夕飯を作りました。 \\
\end{compare}

\begin{trap}
ことにする is your own decision; ことになる reports a decision made by others or by circumstances. 留学することにしました (I decided to study abroad) vs. 父の仕事で、大阪に引っ越すことになりました (we are moving because of my father's job).
\end{trap}
""")
G.q("4 Structures", r"Choose the correct ending: 祖母が昔の話をして\blank。（My grandmother told me stories about the old days.）",
    "くれました", [("あげました", "あげる is for favors from the speaker's side outward."),
                   ("もらいました", "With もらう the receiver is the subject: 祖母に話をしてもらいました."),
                   ("さしあげました", "さしあげる is humble giving from the speaker to a superior.")],
    "Someone does a favor for me → てくれる.", "The giver is marked with が; the favor comes toward the speaker.",
    ["祖母が (giver) … → くれました."])
G.q("4 Structures", r"Choose the form that means ``I decided to visit my grandparents every week.'' 毎週祖父母の家に行く\blank。",
    "ことにしました", [("ことになりました", "ことになる reports a decision made by others or by circumstances."),
                       ("ようになりました", "ようになる describes a gradual change, not a decision."),
                       ("ために", "ために expresses purpose and cannot end the sentence here.")],
    "My decision → ことにする.", "Use ことにする for a decision the speaker makes.",
    ["I decided → ことにしました."])
G.q("4 Structures", r"Choose the form that means ``I can now cook by myself.'' 一人で料理ができる\blank。",
    "ようになりました", [("ことにしました", "That means “I decided to be able to cook,” which is not a decision."),
                         ("ことになりました", "That means “it was decided that I can cook.”"),
                         ("ながら", "ながら means “while.”")],
    "Change in ability → ようになる.", "Potential form + ようになる expresses a new ability or habit.",
    ["できる + ようになりました → can now."])

G.sec("Task kit: the Email Response")
G.tex(r"""
Unit 1 emails often come from a friend preparing a homestay, a host family, or a neighbor asking for help. Each contains two questions or requests; answer both, each with a reason or example.

\begin{compare}{Move}{To a friend (plain style)}{To a host family or neighbor (polite style)}
Open & メールありがとう！元気？ & メールをありがとうございました。お元気ですか。 \\
Restate request 1 & ～のことだけど、 & ～についてですが、 \\
Give an opinion & ～と思うよ。だって、～から。 & ～と思います。なぜなら、～からです。 \\
Suggest & ～たらどう？ / ～ほうがいいよ。 & ～たらいかがでしょうか。 \\
Move to request 2 & それから、～ね。 & それから、～のことですが、 \\
Close & じゃあ、またね！ & どうぞよろしくお願いいたします。 \\
\end{compare}
""")
G.q("5 Email", r"Which sentence gives a suggestion in polite style, suitable for a reply to a host father?",
    "駅まで迎えに来ていただけたら、とても助かります。", [("駅まで迎えに来てよ。", "Casual request; too direct for a host father."),
                                                      ("駅まで迎えに来い。", "A blunt command."),
                                                      ("駅まで迎えに来てくれる？", "Casual style for a friend.")],
    "Polite request → ～ていただけたら助かります.", "Requests to a host family use polite, indirect forms such as ～ていただけますか or ～ていただけたら助かります.",
    ["ていただけたら (if you could) + 助かります (it would help)."])
G.q("5 Email", r"A friend asks two things: what gift to bring a host family, and how to get along with them. A reply that answers only the gift question can earn at most",
    "2 of 3 for message development", [("3 of 3 for message development", "3 requires clear answers to both requests."),
                                       ("1 of 3 for organization", "Organization is out of 2 and is not the row affected."),
                                       ("0 for the whole task", "One request answered still earns credit.")],
    "One of two requests → 2 at most.", "Message development needs both requests answered with details for the top score.",
    ["Gift answered, getting along ignored → 2."])

# ======================================================================================= question set
Q = Doc(STEM, "questions", "Unit 1: Families and Communities: Question Set", r"Unit 1 \textperiodcentered\ Question Set",
        abstract=r"""Four multiple-choice sets in the exam's task types (an Audio Report and a Conversation for listening, an Article and Chart and a Correspondence for reading) on a children's cafeteria run by a neighborhood association, people living alone, a letter from a host mother and a choice between Tokyo and the countryside, followed by an Email Response (8 points) with a scoring guide and a model reply. Questions are in English, as on the exam; listening sources are printed as transcripts. All sources and data are original and fictional, written for practice. Allow about 25 minutes for the multiple choice and 15 minutes for the email.""",
        scoring=r"MCQ: \blank\ / \qtotal \qquad Email: \blank\ / 8 \qquad Target: 15+ MCQ and 6+ email",
        short="Unit 1", sub="Families and Communities")

Q.sec("Listening: Audio Report")
Q.src(r"Listening 1 \textperiodcentered\ Audio Report (transcript) \textperiodcentered\ 地域のニュース「みんなの食堂」", [
    r"（アナウンサー）さくら町の町内会が、毎週土曜日に「みんなの食堂」を開いています。子どもは無料、大人は三百円で、温かい晩ご飯が食べられます。",
    r"（アナウンサー）始めたのは、町内会長の山本さんです。「共働きの家が増えて、一人でご飯を食べる子どもが多いと聞きました。それで、地域のみんなで一緒に食べる場所を作ろうと思ったんです。」",
    r"（アナウンサー）料理を作るのは、近所のお年寄りと高校生のボランティアです。野菜は、近くの農家がお裾分けしてくれます。",
    r"（アナウンサー）山本さんは、「子どもだけでなく、一人暮らしのお年寄りも来てくれるようになりました。食堂が、世代をつなぐ場所になっています」と話しています。",
], 5)
Q.q("1.A.1 Detail", "How much does a meal cost for a child?",
    "nothing", [("300 yen", "300 yen is the price for adults."),
                ("100 yen", "Not mentioned."),
                ("It depends on the day", "The price is fixed.")],
    "子どもは無料.", "Detail (1.A.1): 無料 means free.",
    ["子どもは無料、大人は三百円."])
Q.q("1.B.1 Purpose", "Why did Mr. Yamamoto start the cafeteria?",
    "Many children were eating alone because both parents work.", [("He wanted to make money for the association.", "Children eat for free."),
                                                                    ("The school asked him to.", "Not mentioned."),
                                                                    ("The farmers had too many vegetables.", "The vegetables are a detail, not the reason.")],
    "共働き → 一人で食べる子ども.", "Purpose (1.B.1): his own explanation.",
    ["共働きの家が増えて、一人でご飯を食べる子どもが多い."])
Q.q("1.A.1 Detail", "Who cooks the meals?",
    "older neighbors and high-school volunteers", [("professional chefs", "Not mentioned."),
                                                  ("the children's parents", "Not mentioned."),
                                                  ("local farmers", "Farmers provide vegetables.")],
    "お年寄りと高校生のボランティア.", "Detail (1.A.1).",
    ["料理を作るのは、近所のお年寄りと高校生のボランティアです."])
Q.q("1.B.5 Word meaning", r"In the report, お裾分けしてくれます most likely means that the farmers",
    "share some of their vegetables with the cafeteria", [("sell vegetables at a discount", "お裾分け is sharing, not selling."),
                                                         ("teach the children to farm", "No."),
                                                         ("cook the vegetables", "No.")],
    "お裾分け = share a portion.", "Word meaning (1.B.5): てくれる shows the farmers do it as a favor.",
    ["お裾分け + てくれる → share as a favor."])
Q.q("1.C.2 Conclusion", "What does Mr. Yamamoto's last comment suggest?",
    "The cafeteria now connects different generations, not only children.", [("Older people are no longer welcome.", "They come now too."),
                                                                             ("The cafeteria will close soon.", "No."),
                                                                             ("Children prefer to eat alone.", "The opposite.")],
    "世代をつなぐ.", "Conclusions (1.C.2): 子どもだけでなく … お年寄りも.",
    ["世代をつなぐ場所 → connects generations."])

Q.sec("Reading: Article and Chart")
Q.src(r"Reading 1 \textperiodcentered\ Article and Chart \textperiodcentered\ 「一人で暮らす人が増えている」", [
    r"日本では、一人で暮らす人が増えています。若い人だけでなく、子どもが独立したあとの高齢者の一人暮らしも多くなりました。",
    r"社会学者の中村さんは、「一人暮らしは悪いことではありません。自由に生活できるからです。しかし、困ったときに相談できる人がいないと、孤立してしまうことがあります」と言います。",
    r"そこで、いくつかの町では、一人暮らしの人が気軽に集まれる「地域のサロン」を作っています。お茶を飲みながら話したり、体操をしたりする場所です。",
], 5, table=(["世帯の種類", "1990年", "2020年"], [["一人暮らし", "23\\%", "38\\%"], ["夫婦と子ども", "37\\%", "25\\%"], ["夫婦のみ", "16\\%", "20\\%"], ["その他", "24\\%", "17\\%"]]),
      note="世帯の割合（架空のデータ）")
Q.q("1.A.2 Data", "According to the chart, which type of household was the most common in 2020?",
    "people living alone", [("couples with children", "25% in 2020; it was the most common in 1990."),
                            ("couples only", "20%."),
                            ("other", "17%.")],
    "一人暮らし 38%.", "Data (1.A.2): read the 2020 column.",
    ["2020: 38 > 25 > 20 > 17."])
Q.q("1.A.2 Data", "Which change does the chart show between 1990 and 2020?",
    "Couples with children fell from the largest group to second place.", [("Couples with children rose to 37%.", "They fell from 37% to 25%."),
                                                                          ("People living alone fell.", "They rose from 23% to 38%."),
                                                                          ("Couples only fell to 16%.", "They rose from 16% to 20%.")],
    "37 → 25; 23 → 38.", "Data (1.A.2): compare the two columns.",
    ["1990 largest: 夫婦と子ども; 2020 largest: 一人暮らし."])
Q.q("1.B.3 Point of view", "What is Mr. Nakamura's view of living alone?",
    "It is not bad in itself, but people without someone to talk to can become isolated.", [("It is always harmful.", "He says it is not bad."),
                                                                                             ("It is only for young people.", "Not stated."),
                                                                                             ("It should be discouraged by the government.", "Not stated.")],
    "悪いことではありません。しかし…", "Point of view (1.B.3): a balanced view marked by しかし.",
    ["自由 (freedom) / 孤立 (isolation)."])
Q.q("1.B.5 Word meaning", r"In the article, 孤立してしまう most likely means",
    "to end up cut off from others", [("to become very rich", "No."),
                                     ("to move to a new town", "No."),
                                     ("to start a new job", "No.")],
    "孤立 = isolation.", "Word meaning (1.B.5): 相談できる人がいないと → isolated; てしまう adds regret.",
    ["困ったときに相談できる人がいない → 孤立."])
Q.q("1.C.1 Connect", "How do the community salons respond to the problem the article describes?",
    "They give people who live alone a place to meet and talk.", [("They find roommates for people living alone.", "Not mentioned."),
                                                                 ("They build new houses for families.", "No."),
                                                                 ("They encourage young people to marry.", "No.")],
    "サロン → 集まれる場所.", "Connect (1.C.1): problem (isolation) → solution (a gathering place).",
    ["気軽に集まれる … 話したり、体操をしたり."])

Q.sec("Reading: Correspondence")
Q.src(r"Reading 2 \textperiodcentered\ Correspondence \textperiodcentered\ ホストマザーからのメール", [
    r"エマさん、はじめまして。来月からエマさんのホストファミリーになる佐藤です。家族は夫と私、高校二年生の娘のあかりと、犬のポチです。みんなエマさんに会えるのを楽しみにしています。",
    r"うちのルールを少しだけ書きますね。家に入るときは、玄関でくつをぬいでください。お風呂は、夜九時までに入ってくれると助かります。それから、夕飯は家族みんなで七時に食べるので、遅くなるときは連絡してください。",
    r"エマさんは、何か食べられないものがありますか。それから、日本でしてみたいことがあったら、教えてください。週末にいろいろなところへ連れて行きたいと思っています。",
    r"では、空港で会いましょう。気をつけて来てくださいね。　佐藤ゆみ",
], 5)
Q.q("1.B.1 Purpose", "What is the main purpose of the email?",
    "to welcome Emma and explain some house rules before she arrives", [("to cancel the homestay", "No."),
                                                                         ("to ask Emma to bring a gift", "Not mentioned."),
                                                                         ("to describe the school Emma will attend", "Not mentioned.")],
    "Welcome + rules + questions.", "Purpose (1.B.1).",
    ["はじめまして … うちのルール … 教えてください."])
Q.q("1.A.1 Detail", "What should Emma do if she will be late for dinner?",
    "contact the family", [("eat dinner alone at nine", "Nine o'clock is the bath time."),
                          ("cook her own meal", "Not stated."),
                          ("ask Akari to wait", "Not stated.")],
    "遅くなるときは連絡してください.", "Detail (1.A.1).",
    ["夕飯は … 七時 … 遅くなるときは連絡してください."])
Q.q("1.B.5 Word meaning", r"In the email, 入ってくれると助かります is closest to",
    "it would help us if you took your bath by then", [("you must never take a bath", "No."),
                                                      ("please help us clean the bath", "Misreading of 助かる."),
                                                      ("we will help you with your bath", "No.")],
    "～てくれると助かる = a soft request.", "Word meaning (1.B.5): a polite, indirect way of asking.",
    ["助かる = it helps (us)."])
Q.q("1.A.1 Detail", "What two things does Mrs. Sato ask Emma?",
    "whether there is food she cannot eat, and what she would like to do in Japan", [("her flight number and arrival time", "Not asked."),
                                                                                    ("whether she likes dogs and cats", "Not asked."),
                                                                                    ("what time she gets up and goes to bed", "Not asked.")],
    "食べられないもの / してみたいこと.", "Detail (1.A.1): the two questions Emma's reply must answer.",
    ["何か食べられないものがありますか / 日本でしてみたいこと."])
Q.q("1.C.3 Inference", "What can be inferred about the Sato family?",
    "They value sharing meals and want to show Emma around.", [("They rarely spend time together.", "They eat together every night."),
                                                               ("They do not want a guest.", "They are looking forward to meeting her."),
                                                               ("They live far from any airport.", "Not stated.")],
    "Family dinner + weekend trips.", "Inference (1.C.3).",
    ["家族みんなで七時に食べる / いろいろなところへ連れて行きたい."])

Q.sec("Listening: Conversation")
Q.src(r"Listening 2 \textperiodcentered\ Conversation (transcript) \textperiodcentered\ 大学生の二人", [
    r"（女）ねえ、たけし君、卒業したらどうするの？",
    r"（男）実は、おばあちゃんの住んでいる町に引っ越そうと思ってるんだ。山の中の小さい町なんだけど、空き家がたくさんあって、町が安く貸してくれるんだって。",
    r"（女）えっ、東京で働くんじゃなかったの？　仕事はどうするの？",
    r"（男）パソコンがあれば、どこでもできる仕事なんだ。それに、町の人が少なくなって、おばあちゃんも寂しそうだから。",
    r"（女）でも、コンビニも遠いし、冬は雪が大変でしょう？",
    r"（男）うん、不便なのはわかってる。でも、近所の人がみんな知り合いっていうのも、いいなと思って。まず一年住んでみることにしたよ。",
], 5)
Q.q("1.A.1 Detail", "What does Takeshi plan to do after graduation?",
    "move to the small town where his grandmother lives", [("work in an office in Tokyo", "The woman thought so, but he has other plans."),
                                                          ("study abroad", "Not mentioned."),
                                                          ("open a convenience store", "Not mentioned.")],
    "おばあちゃんの住んでいる町に引っ越そう.", "Detail (1.A.1).",
    ["実は、おばあちゃんの住んでいる町に引っ越そうと思ってる."])
Q.q("1.A.1 Detail", "How will Takeshi work there?",
    "He has a job he can do anywhere with a computer.", [("He will farm with his grandmother.", "Not mentioned."),
                                                         ("He will commute to Tokyo every day.", "Not mentioned."),
                                                         ("He will work at the town office.", "Not mentioned.")],
    "パソコンがあれば、どこでもできる.", "Detail (1.A.1).",
    ["パソコンがあれば、どこでもできる仕事なんだ."])
Q.q("1.B.3 Attitude", "How does the woman react to his plan?",
    "She is surprised and worried about the inconvenience.", [("She is jealous and wants to go too.", "Not stated."),
                                                              ("She is completely indifferent.", "She asks several questions."),
                                                              ("She is angry with him.", "No.")],
    "えっ … でも、…大変でしょう？", "Attitude (1.B.3): surprise (えっ) and concern (でも…大変でしょう).",
    ["えっ → surprise; コンビニも遠いし、雪が大変 → worry."])
Q.q("1.C.3 Inference", "Which reason for moving shows that Takeshi values community?",
    "He likes the idea that everyone in the neighborhood knows each other.", [("He wants cheaper convenience stores.", "Stores are far away."),
                                                                             ("He prefers heavy snow.", "No."),
                                                                             ("He wants to be far from his family.", "The opposite.")],
    "近所の人がみんな知り合い.", "Inference (1.C.3).",
    ["近所の人がみんな知り合い … いいなと思って."])
Q.q("1.C.2 Conclusion", "What has Takeshi decided?",
    "to try living there for one year first", [("to stay in Tokyo after all", "No."),
                                               ("to buy a house immediately", "The town rents houses; he will try for a year."),
                                               ("to wait until his grandmother moves", "No.")],
    "まず一年住んでみることにした.", "Conclusions (1.C.2): ことにした marks his decision; てみる means try.",
    ["まず一年住んでみることにしたよ."])

Q.frq(kind="Email Response", head=r"Question 4 \textperiodcentered\ Email Response \textperiodcentered\ 8 points \textperiodcentered\ about 15 minutes",
      mins=15,
      directions=[r"\textbf{Directions.} Read the email from a friend. Write a reply in Japanese that responds to all the questions and requests in the email, in a culturally appropriate way."],
      prompt=[r"\textbf{差出人：}はるか \quad \textbf{件名：}ホームステイのこと、教えて！",
              "元気？　実は、来月から一か月、北海道のホストファミリーの家にホームステイすることになったんだ！　すごく楽しみだけど、ちょっと心配なこともあって……。まず、ホストファミリーへのおみやげは何がいいと思う？　それから、家族と仲良くなるために、どんなことをしたらいいかな？　アドバイスしてくれたらうれしい！",
              "はるか"],
      ask="Write your reply to はるか in Japanese.",
      model=["はるかさん",
             "メールありがとう！　ホームステイ、おめでとう。北海道はきっと楽しいと思うよ。",
             "まず、おみやげのことだけど、自分の住んでいる町の有名なお菓子がいいと思う。日本では、相手の家を訪ねるときに小さいおみやげを持っていく習慣があるし、家族みんなで食べられるからね。それに、町の写真を何枚か持っていったら、それを見ながら自分の町のことを話せるよ。",
             "それから、家族と仲良くなる方法だけど、一番大切なのは、自分から話しかけることだと思う。たとえば、晩ご飯のあとで料理を手伝ったり、お皿を洗ったりしたらどうかな。家のルールがわからないときは、遠慮しないで聞いたほうがいいよ。ホストファミリーも、はるかさんのことをもっと知りたいと思っているはずだから。",
             "何かあったら、いつでも連絡してね。北海道の写真、楽しみにしてるよ！",
             "じゃあ、またね。　ゆうき"],
      rows=[("Message development", 3, "Answers both questions directly (a gift: a famous sweet from one's town, plus photos; getting along: start conversations, help with chores, ask about house rules) with reasons and examples.", "Answering only one question; ideas with no reason; a list with no detail."),
            ("Organization", 2, "Opening and closing; one paragraph per question; cohesive devices (まず、～だけど / それに / それから / たとえば / ～から).", "No opening or closing; both answers mixed in one paragraph."),
            ("Language control", 3, "Varied structures (～ことになる, ～たら, ～たり～たり, ～ほうがいい, ～はずだ, noun modification) and a culturally relevant practice (bringing a small gift when visiting, 遠慮しないで) in consistent plain style for a friend.", "Switching between plain and です・ます endings; basic vocabulary only; frequent particle errors.")],
      tips=[r"The reply restates each question before answering it (おみやげのことだけど / 仲良くなる方法だけど), so a reader can see both requests are covered. The gift advice is explained with a cultural practice (bringing a small gift when visiting), and the plain style matches an email between friends from start to finish."])

GUIDE, QSET = G, Q
